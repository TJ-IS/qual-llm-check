---
otero_id: 21089
otero_key: "29NTAEMU"
title: "Integration of digital rights management into the Internet Open Trading Protocol"
authors: "S.H Kwok; S.C Cheung; K.C Wong; K.F Tsang; S.M Lui; K.Y Tam"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00067-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integration of digital rights management into the Internet Open Trading Protocol

S.H. Kwok <sup>a,</sup>\*, S.C. Cheung <sup>b,1</sup>, K.C. Wong <sup>b,1</sup>, K.F. Tsang a,2 S.M. Lu i <sup>a,</sup> <sup>2</sup>, K.Y. Tam <sup>a,2</sup>

<sup>a</sup>Department of Information and Systems Management, The Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong, China

<sup>b</sup>Department of Computer Science, The Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong, China

Accepted 31 January 2002

## Abstract

Although digital rights management (DRM) has gained increasing importance in today’s digital services and electronic commerce, it is not addressed explicitly in the Internet Open Trading Protocol (IOTP) specification. In this paper, we propose a digital rights management system (RMS) that is integrated into IOTP for electronic commerce applications and services. We introduce a rights insertion phase and a rights verification phase for IOTP. In the proposed framework, digital watermarking plays a very important role in facilitating digital rights management. The proposed digital rights management system was implemented on an online music web site and the proposed concepts and approaches proved to be successful. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Digital rights management; Digital watermarking; Internet Open Trading Protocol; Copyright protection; Intellectual property protection; Electronic commerce

## 1. Introduction

Advances in multimedia and Internet technologies have transformed the way digital information is packaged, distributed and consumed. Information content, no matter if it is text, image, audio, or video, can now be digitised and distributed over the Internet at very low cost. Information technology has significantly reduced the reproduction and the distribution costs of information content. However, the ease of copying digital content and the close-to-zero reproduction cost also create a strong incentive for people to perform unlawful acts. The publishing and music industries have incurred considerable loss due to copyright violations. News of copyright infringement has appeared continuously in media headlines in recent years. It is estimated that the music industry alone has suffered losses of hundreds of millions of dollars. Digital rights protection is a pressing issue that, if unresolved, will create a major barrier to public enjoyment of voice recordings and music over the Internet. Digital rights management (DRM) prevents unauthorized use of digital files (in any format— sound, images, text, documents or data) and/or identifies the source of such use [13]. The term rights management refers to the process of honouring the copyright provisions, license terms and usage agreements established by the owner of intellectual property [1]. As such, it is important to establish a rights management system that controls the usage and distribution of digital content. With the initiation of a rights management system, new payment models such as pay-per-day and pay-per-view can be implemented in Internet commerce settings.

Techniques to protect digital rights are mostly based on either cryptography or digital watermarking. Examples of systems supporting cryptographic techniques are InterTrust [8] and Window Media Technologies [14]. These systems achieve rights management through access control. Digital contents are always distributed in their encrypted forms. Given proper permission from the content provider or owner, clients are allowed to access the encrypted contents. However, when a piece of encrypted digital content is decrypted, it becomes ordinary digital content that is no longer protected and that does not carry any rights information. As a result, when the decrypted digital content is distributed to unauthorized consumers illegally, it is almost impossible for the cryptographicbased rights management system to trace the person who has distributed the illegal copy of the digital content or to discover from where it actually came. To address this problem, other systems achieve rights protection using digital watermarking.

Yi et al. [15] proposed a rights management system that uses watermarks to identify the owner of the digital property. The system adds watermarks into digital contents before distribution, and it allows only content providers or distributors to manage the watermark insertion process. The idea behind watermarking is that it will provide sufficient evidence if someone abuses the rights of the digital holder content while the quality of the digital content is not degraded noticeably. The watermarking process makes it impossible for others to erase and extract the inserted watermark. The system contains mobile agents that recognize a set of predefined business logic. The mobile agents are run at the client end and control the usage of digital content media by exchanging information with selected host machines.

Anderson and Lotspiech [1] proposed an enforcement system for both access control and copyright protection in an electronic library system. Access control is achieved through user authentication and session encryption, while copyright protection is enforced by visible and invisible watermarks. For instance, a user must provide a valid Lotus Notes password prior to accessing copyright-protected library materials. A bar code that acts as a visible watermark is attached to the front page of each digital article in the electronic library. A digital article is regarded as an illegal printed document if it contains no bar code on its front page. In addition, invisible watermarks are inserted into the digital document. Tracing these invisible watermarks can reveal any other illegal acts.

In designing and implementing DRM systems, Iannella [6] identified that there are two critical architectures to consider. The first is the functional architecture, which covers the high-level modules or components of the DRM system that together provide an end-to-end management of rights. The second critical architecture is the information architecture, which covers the modeling of the entities within a DRM system as well as their relationships.

We concluded that a successful rights management system uses digital watermarking and that a complete rights management system should involve all parties in a business transaction, such as the merchant, the consumer, the content provider and the authority who manages the rights of the property. The rights management system should be capable of controlling the usage and distribution of digital contents in an electronic commerce setup.

To achieve these ends, we propose to adopt the well-known business transaction model, Internet open trading protocol (IOTP), as an infrastructure for electronic trading and to introduce digital rights management using digital watermarking to this protocol. In this paper, we address the following research questions.

1. What is the role of a digital rights management system in an electronic commerce transaction with IOTP?

2. How can a digital rights management system using digital watermarking technology be integrated into IOTP?

In this paper, we seek to respond to these research questions and to propose an infrastructure and design of a digital rights management system integrated with IOTP to be used in electronic commerce applications. From the technical point of view, digital watermarking is used in this system for rights management. The proposed system is based on the assumption that an IOTP communication channel exists between the consumer and the merchant.

The remainder of this paper is organized as follows. Section 2 introduces some commercial digital rights management systems and identifies their features. In Section 3, the IOTP framework and the baseline transaction information are illustrated in detail. Section 4 illustrates digital rights management using digital watermarking. Digital watermarking processes, including watermark insertion, watermark detection and watermark verification, are described in this section. Section 5 demonstrates the integration of digital rights management with IOTP. The rights insertion phase and the rights verification phase are introduced. Section 6 presents the implementation of proposed framework. Finally, we conclude the paper in Section 7.

## 2. Commercial rights management systems

Commercial rights management solutions using digital watermarking are available in the market. Here is a summary of some relevant commercial rights management solutions.

. Digimarck [4] is a digital watermarking technology that can be used with a variety of visual digital content, including both images and video media. Digimarck provides visual content owners a range of solutions including copyright communication, image licensing and management and enhanced Internet commerce. These solutions are enabled by a set of digital watermarking tools that embed, read and respond to the watermarks as they enable new communications capabilities within traditional and visual digital content.

. The InterTrust Commerce Architecture [9], principally based on DigiBoxk secure containers, Inter-Trust Commerce Nodes and a secure operating system layer extension, enables the creation of a globally distributed Intertrustworthyk environment. This environment provides the basis for a broad range of realworld rights and obligations, including intellectual property right and real-world rules related to rights and obligations, to be securely expressed and enforced. One of the strengths of the technology is that the right to use content can be managed separately from the content itself. The rights to the underlying work (the original creation) can be managed separately from the rights relating to particular expressions of those works, just as they are in the real world.

. MusicMatch [8], developer of the MusicMatch Jukebox, the world’s first personal jukebox software, is participating in Magex’s unique Internet digital music pilot system. The music pilot enables record companies and artists to distribute music over the Internet, protect their copyrights and collect royalty payments. The MusicMatch Jukebox software intends to integrate Magex’s services into its digital audio player, allowing users to download rightsprotected music tracks from the Internet into the MusicMatch Jukebox. Tracks can then be organized into a digital music library, added to custom playlists and played back with CD-quality via the user’s PC. MusicMatch intends to be a SDMI-compliant product.

These commercial systems are mainly designed to protect publishers of digital content. However, publishers are not the only parties in electronic commerce. A rights management system should protect the interests of various actors in a transaction (such as consumers, authors and composers). In view of this, Zhao [16] proposed the use of a hierarchical watermarking scheme to cover all parties involved in electronic trading, including merchants, consumers, logistic partners and so on in the rights management scheme. To achieve this, each piece of digital content is embedded with three watermarks, namely, the public, owner and recipient watermarks. The public watermark containing traditional copyright information is encrypted with a public key, so that consumers will know the publisher of the digital content by successfully decrypting the public watermark. The owner and recipient watermarks provide information about the owner and consumer, respectively. Hierarchical watermarks provide evidence of illicit copying and dissemination. However, inclusion of too much personal information in watermarked digital content can be a risk when the watermarking scheme is abused.

## 3. Internet open trading protocol

Internet open trading protocol (IOTP) [7] is an interoperable framework for Internet commerce. IOTP provides a virtual environment for many trading methods, such as buying, selling, value exchange and so on. It identifies five major trading roles, i.e., consumer, merchant, payment handler, delivery handler and customer care provider. Their relationships are illustrated in Fig. 1. The consumer and merchant are basically the buyer and seller, respectively. A payment handler provides independent and encapsulated systems, such as SET, Mondex, CyperCash, DigiCash, GeldKarte, etc., while the customer care provider is involved in consumer dispute negotiation and resolution on behalf of the merchant. In addition, a delivery handler delivers the goods or services to the consumer.

## 3.1. Baseline transactions

In the IOTP specification, trading over the Internet can be classified into eight different types of transactions, i.e., authentication, deposit, purchase, refund, withdrawal, value exchange, ping and transaction status inquiry. They are referred to as the baseline transactions. Based on their natures, these baseline transactions are further categorized into three groups: authentication transaction, payment-related transaction and checking transaction. An authentication transaction allows one party to identify its counter party using a variety of authentication methods. A payment-related transaction provides deposit, purchase, refund, withdrawal and value exchange. A checking transaction checks the correct transaction status and detects whether the server involved is still active.

Let us consider the major workflow involved in purchasing a product over the Internet using IOTP as shown in Fig. 2. A consumer who wants to purchase a product over the Internet first submits a valid user name and password through the baseline authentication transaction. The consumer then chooses a suitable payment method through the baseline purchase transaction. The baseline purchase transaction offers two different payment methods: brand-independent payment and brand-dependent payment. The brandindependent payment offers consumers flexibility in selecting a payment brand and protocol, while the brand-dependent payment restricts consumers to a

![](/api/attachments/29NTAEMU/fulltext/images/9567045428d06e10bffd1842799155271f57f0ce448cc7616f194a309019a211.jpg)  
Fig. 1. Different trading roles in IOTP.

![](/api/attachments/29NTAEMU/fulltext/images/b587d5d73fe8e04ef19641dd02739148dc4a370910cf381b1f7f6c67b90425df.jpg)  
Fig. 2. Workflows of baseline transaction in IOTP.

particular payment brand and protocol. For example, in the brand-dependent payment, the consumer may choose from different payment methods, such as Visa or MasterCard credit cards, before buying the product. In the brand-independent payment, the merchant chooses the payment method. After the payment has been made, the payment handler issues a payment receipt to the consumer. The consumer forwards the payment receipt to the delivery handler and the delivery handler delivers goods or provides services.

IOTP supports both business-to-business (B2B) and business-to-consumer (B2C) models. The baseline transactions defined in IOTP support the most common trading logistics over the Internet, such as purchases and refunds. The baseline transaction identifies four major scenarios of data exchange among different trading roles. Each scenario is regarded as a trading exchange in the baseline transaction. The four trading exchanges are listed as follows:

. Offer Trading Exchange. An offer trading exchange results in the merchant providing the consumer with an offer of trade to occur. This is called an offer exchange because the consumer must accept the offer in order to continue the trade.

. Payment Trading Exchange. A payment trading exchange results in a payment of some kind between the consumer and the payment handler. This may occur in either direction.

. Delivery Trading Exchange. A delivery trading exchange transmits either the online goods or delivery information about physical goods from the delivery handler to the consumer.

. Authentication Trading Exchange. An authentication trading exchange can be used by any participant in the transaction to authenticate the identity of another party.

IOTP transactions are basically composed of various combinations of these trading exchanges. For example, an IOTP purchase transaction includes offer, payment and delivery trading exchanges. In another example, an IOTP value exchange transaction is composed of an offer trading exchange and two payment trading exchanges. A new transaction can be derived from the baseline transaction. For example, we add a rights insertion phase in the offer trading exchange to include a new transaction for buying digital music protected by digital rights. We must note here that IOTP is designed to support major trading scenarios over the Internet. However, digital rights management is not explicitly addressed in the specification [7] although it is a growing concern for electronic commerce merchants and consumers and is, in fact, closely related to electronic trading and transactions.

## 4. Digital rights management using digital watermarking

A client/server-based rights management system [1,10,11] is illustrated in Fig. 3. There are three major functional components in this system. They are the media player (MP), the rights management system (RMS) server and the rights management database (RMDB). In the system, the digital watermark is regarded as a message containing rights information travelling between different users.

## 4.1. Digital watermark

A digital watermark may contain product information, user information and rights information, including usage rights and access rights. The digital watermark is thus dependent on the consumer, product and rights. Such information is usually obtainable through electronic transactions, such as baseline transactions in IOTP. A digital watermark can be created with relevant information when a consumer orders a product. This information is usually kept in the

![](/api/attachments/29NTAEMU/fulltext/images/27d2e9f3a88c705b298334c967f8792de216d2a599ed14a827d3cb59ee0f5bd4.jpg)  
Fig. 3. Client/server-based rights management system using digital watermarking

RMDB and the index of the data entries can be used for watermark creation. The created watermark is then used in later processes, such as watermark insertion, detection and extraction.

## 4.2. Watermarking processes

Three basic watermarking processes are required in digital rights management. They are watermark insertion, watermark detection and watermark extraction. In general, watermark insertion requires (i) digital content, (ii) a digital watermark and (iii) a private key, which is a secret key that is only known by the owner of the digital content. The output is the watermarked digital content as shown in Fig. 4. The watermark can include information about ownership, the user’s identity and a description of the original data, etc. The watermark insertion process embeds a digital watermark into the digital content. The watermark can be perceptible or imperceptible depending on the applications. For applications requiring that the original data not be distorted perceptually, an imperceptible watermark is desired. For applications that require a display of the embedded data, a perceptible watermark is preferred.

The most popular watermark insertion algorithm is the Spread Spectrum Watermarking technique [2], which is usually applied to the frequency domain of the digital content. In the music setting, inserting the watermark sequence in the low frequency range will increase the robustness of the watermark at the cost of the audibility of the watermark. On the other hand, inserting the watermark sequence in the high frequency range will render the watermark inaudible but at the cost of robustness against attacks. Some watermarking algorithms choose the mid-frequency band for watermark insertion.

![](/api/attachments/29NTAEMU/fulltext/images/9ad0ec2cc9b95c83291e68a3987953167c0e48657240e46e72a2a8dc82f58031.jpg)  
Fig. 5. Watermark extraction.

Mathematically, most of the watermarking techniques, including the above two techniques, can be modelled as follows [2]: given an original media, M, the watermarked media MV is formed by $M ^ { \prime } { = } M { + } f ( M ,$ W) such that people would not find any difference between the original media, M, and the watermarked media, M V. Function f is the most critical part of a watermarking algorithm because the robustness of the watermark greatly depends on the design of f. Common detection algorithms correlate the watermark with the watermarked media. If W is chosen at random, the correlation between M and W is very small, as the random F terms cancel themselves out on average, leaving only a residual variance. However, in computing WW, all of the terms are positive and thus add up. For this reason, the product $M ^ { \prime } \cdot W { = } M \cdot W { + } W \cdot W$ can estimate WW accurately. As a result, the embedded watermark can be retrieved without the use of the original media, M.

The generation of the watermark, W, is usually a function of the information bits and a key, K. The key is needed for decoding the embedded information.

![](/api/attachments/29NTAEMU/fulltext/images/159e79c4c6dec81c0a9d12dff211dbcadde2ea47c3a0a18a9565a84c49b2cb5e.jpg)  
Fig. 4. Watermark insertion.  
Fig. 6. Watermark detection.

Some algorithms make the watermark generation dependent on the original host signal, such that it is difficult for attackers to remove the watermark in the absence of the original signal.

Watermark extraction and watermark detection processes as shown in Figs. 5 and 6 are used to retrieve the embedded watermark from the watermarked media. In watermark extraction, a public key, which is known to the general public, is used together with the watermarked media to retrieve the embedded watermark. In the watermark detection process, a public key and a specified ID-watermark are used together with the watermarked content to determine whether the watermark is legitimate.

## 5. Integration of digital rights management with IOTP

To implement digital rights management in Internet commerce, we propose to adopt the client/serverbased rights management system introduced in Section 3 and map it into the IOTP domain. Technically, we need to resolve the following issues in order to realize the integration.

1. How can digital rights management be exercised in electronic commerce using IOTP?

2. What is the relation between digital watermarking and IOTP transactions?

In response to the above questions, we propose enforcing digital rights management by two corresponding phases in the IOTP domain: the rights insertion phase and the rights verification phase. In the rights insertion phase, rights information is embedded in digital contents as watermarks. The resulting watermarked digital content is then distributed in the form of IOTP delivery responses. In the rights verification phase, a designated content provider inspects the embedded watermarks through IOTP document exchanges. The enforcement of rights management introduces two new concepts to IOTP: (i) a content distributor, as an agent to prepare, distribute and inspect watermarks, and (ii) a rights verification transaction, under which watermarks are inspected by a designated content distributor.

## 5.1. The rights insertion phase

Fig. 7 shows the message blocks exchanged in the rights insertion phase. When the consumer requests the offer information of a particular product, the merchant will need to authenticate the identity of the consumer. The consumer then submits an authentication response, which embeds an organization component [7]. The data type definitions of the organization component are given in Table 1. The main purpose of the organization component is to indicate the identity and contact information of the consumer.

Upon successful identity authentication, the consumer and the merchant communicate through a pair of message blocks, called an offer document exchange. Through the offer document exchange, the consumer places an order including particular information, such as the desired license type and the quantity. The order information is stored in an order component [7] whose data type definitions are given in Table 2.

On receiving an order, the merchant returns an offer response, which contains the details of the goods and payment confirmation. The consumer can then forward information in the offer response to a designated content distributor and request delivery. Sometimes, the merchant can also be a content distributor. Each delivery request contains an order component specifying the information about the order and the organization component specifying the details of the trading partners. Content distributors are responsible for generating watermarks, which are composed of rights information, and for embedding them into digital content prior to delivery to consumers.

## 5.2. Rights verification phase

A rights verification phase involves two parties: the license holder and the content distributor. The license holder is the consumer who holds a license for using a piece of digital content distributed through a designated content distributor. Content distributors are responsible for license verification. The main purpose of the rights verification phase is to verify that licenses are owned by the license holders. License verification is performed by designated content distributors based on the watermarks embedded in the digital content being traded. As a watermark is applied repeatedly to every fragment of a digital content, rights verification can be based on a fraction of the whole content. To facilitate rights verification under the IOTP framework, we introduce a new transaction type, called rights verification transaction, which consists mainly of:

![](/api/attachments/29NTAEMU/fulltext/images/6806b0bb202ad0fbd30fc3129389fabbbd62f918d40f7200f3cd9f3e5e5cbc4e.jpg)  
Fig. 7. Rights insertion phase in IOTP.

(i) A Digital Rights Verification Request from a content distributor to a license holder, specifying the information needed for verification.

(ii) A Digital Rights Verification Response from a license holder to a content distributor, supplying the requested information.

<table><tr><td colspan="3">Data type definition of organization component in XML</td></tr><tr><td colspan="3">&lt;!-- ORGANIZATION COMPONENT --&gt;</td></tr><tr><td colspan="3">&lt;!ELEMENT Org (TradingRole+, ContactInfo?, PersonName?,PostalAddress?)&gt;</td></tr><tr><td colspan="3">&lt;!ATTLIST Org</td></tr><tr><td>ID</td><td>ID</td><td>#REQUIRED</td></tr><tr><td>xml:lang</td><td>NMTOKEN</td><td>#REQUIRED</td></tr><tr><td>OrgId</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>LegalName</td><td>CDATA</td><td>#IMPLIED</td></tr><tr><td>ShortDesc</td><td>CDATA</td><td>#IMPLIED</td></tr><tr><td>LogoNetLocn</td><td>CDATA</td><td>#IMPLIED&gt;</td></tr></table>

(iii) A Digital Rights Verification Status returned by the content distributor to the license holder, confirming the validity of a license.

Fig. 8 illustrates the IOTP message blocks exchanged in the rights verification phase. The rights verification transaction starts when a license holder opens a piece of digital content and prompts a designated content distributor to verify the license. If the digital content requires license validation, the content distributor returns a Digital Rights Verification Request, which contains parameters specifying the type of information needed. The license holder can then prepare a Digital Rights Verification Response, an IOTP message block containing the required information, which is often a portion of the watermarked digital content such as a couple of audio frames. Based on the digital content submitted, the content distributor verifies the associated license based on the embedded watermarks. The verification result is then returned to the license holder through another IOTP message block, labelled the Digital Rights Verification Status. This completes the rights verification transaction. Upon receiving a positive response, the license holder is allowed to open the digital content. Details of the extended IOTP and the data type definitions of the associated message blocks are available in a technical report [7].

<table><tr><td colspan="3">Table 2Date type definition of order component in XML</td></tr><tr><td colspan="3">&lt;!-- ORDER COMPONENT --&gt;</td></tr><tr><td colspan="3">&lt;!ELEMENT Order (PackagedContent*)&gt;</td></tr><tr><td colspan="3">&lt;!ATTLIST Order</td></tr><tr><td>ID</td><td>ID</td><td>#REQUIRED</td></tr><tr><td>xml:lang</td><td>NMTOKEN</td><td>#REQUIRED</td></tr><tr><td>OrderIdentifier</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>ShortDesc</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>OkFrom</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>OkTo</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>ApplicableLaw</td><td>CDATA</td><td>#REQUIRED</td></tr><tr><td>ContentSoftwareId</td><td>CDATA</td><td>#IMPLIED&gt;</td></tr></table>

![](/api/attachments/29NTAEMU/fulltext/images/039b3663d4e4e73665fbfd66460d2972f9b55c0026e8bac0da8e1a8c3ee13166.jpg)  
Fig. 8. IOTP message blocks exchanged in the rights verification phase.

## 6. Implementation

In order to demonstrate the proposed rights management system integrated with IOTP, we applied the system to an online music web site and evaluated the practicality of the system. The online music web site offers online purchasing and downloading services to consumers.

Fig. 9 shows the workflows between the online music web site and a consumer. It is assumed that the merchant is also the content distributor and consumers may order and purchase digital music from the online music web site. With the support of IOTP, ordering and payment can be handled in this system. Our focus and interest are on the rights management aspect of the system. We implemented rights insertion and rights verification phases in this system according to Section 4. We now take a look at how these two phases are involved in the business transaction.

![](/api/attachments/29NTAEMU/fulltext/images/130d4862bf2b6a2753bf9473af990d0bd1701018acf3f370dcbbf10020e6dfc2.jpg)  
Fig. 9. An implementation of the proposed rights management system.

## A walkthrough

Suppose Alice would like to buy a song online from our web site. First, she needs to register with the online music web site by providing information, like her name, address, contact numbers and credit card information. Alice then browses the online catalogue and chooses the song she is looking for. She adds the song to her shopping cart and chooses the ‘‘unlimited’’ option, so that she can play the song without the limitations of the number of times and the period of time. That means she can ‘‘own’’ the song forever. Since Alice is a registered user, she does not need to reenter her information for the checkout process. After she clicks on the checkout button, the transaction then starts. Once the transaction is completed, the rights insertion phase will be initiated on the merchant’s side. After a while, the watermarked song is delivered to Alice through the IOTP delivery transactions.

When Alice attempts to listen to the song on her machine for the first time, her music (or media) player will automatically connect to the RMS server and RMDB to access the rights information for this song by sending a short piece of the song to the RMS server. The results will be returned to the music player through the rights verification transaction of IOTP. The music player will then be notified that the song bares an ‘‘unlimited’’ license, so that Alice may play the song from now on.

## 6.1. Technical analysis

We are also interested in the technical perspectives of the two phases. The following shows how the two phases operate in the proposed system.

## Rights insertion phase

Like other online shops, personal information is usually requested from consumers such as the consumer’s name, credit card number, the credit card’s expiry date, as well as other necessary information, for instance, song ID, usage rights, access rights, etc. Such information is submitted through IOTP transactions to the merchant. On receiving the information, the merchant server will process the order while the RMS server will process the information for rights management and all rights-related information will be stored in the RMDB. Then, the content distributor produces the rights-protected (or watermarked) digital content with a customized digital watermark for the order. A sample audio digital watermark using Cox audio watermarking [3] is given in Fig. 9. The watermarked digital content is then delivered to the consumer through the IOTP delivery transaction.

## Rights verification phase

Whenever the consumer or the content distributor (or the merchant) wants to verify the rights of a particular piece of digital music, the rights verification phase is activated. A communication channel between the content distributor and the media player owned by the consumer is established. The newly proposed rights verification transaction is used in this context.

In the rights verification phase, the media player on the consumer’s side will extract some portions of the rights-protected digital music (a fragment of the digital music in our example is given in Fig. 9) and pass them to the content distributor for rights verification through the rights verification transaction. Embedded digital watermarks are then extracted and compared with information in RMDB on the content distributor’s side. The verification process may be referred to as watermark detection and watermark extraction processes.

## 7. Conclusions and future work

In this paper, we proposed a digital rights management system in the context of the Internet Open Trading Protocol (IOTP) for electronic commerce applications and services. In this system, digital watermarking technology is used for rights insertion, detection and extraction. The major difference between our proposed rights management system and other existing rights management systems is that our system operates in the IOTP domain, which could be a trend and standard for many online business and trading services. In achieving digital rights management in IOTP, we introduced a new party—the content distributor—in the infrastructure of IOTP and two rightsrelated phases—the rights insertion phase and the rights verification phase—to facilitate rights management. We implemented the proposed digital rights management system on an online music web site and worked through all the operations. We showed that the system can provide basic management of the digital rights of digital content. However, rights management may refer to a board set of rules and restrictions. Some of them are addressed and studied in this research, for example, off-line rights verification, rights management with a media player. Adoption of Secure Digital Music Initiative (SDMI) and Motion Picture Expert Group (MPEG 21) in rights management in electronic commerce will be included in future research.

The proposed structure is compatible with the specifications of IOTP. The proposed structure can also be integrated into other trading protocols such as Electronic Business Extensive Markup Language (ebXML) [5] and Universal Description, Discovery, and Integration (UDDI) [12] in a similar way because they all are XML-based. IOTP is just a starting point for our studies of integrating digital rights management into electronic commerce. Further research will be conducted on the interaction in other electronic trading specifications and standards. The ultimate objectives of this research are to provide a rights management system serving most of the electronic commerce and services over the Internet.

## Acknowledgements

This research is supported in part by the Industrial Support Fund of Hong Kong (AF/168/99), the Hong Kong Research Grants Council through a Direct Allocation Grant (DAG99/00.BM38) and an RGC/ CERG Grant (HKUST6088/97E).

## References

[1] L.C. Anderson, J.B. Lotspiech, Rights management and security in the electronic library, Bulletin of the American Society for Information Science 22 (1) (Oct. – Nov. 1995) 21 – 23.

[2] I.J. Cox, J.-P.M.G. Linnartz, Some general methods for tampering with watermarks, IEEE Journal on Selected Areas in Communications 16 (4) (May 1998) 587– 593.

[3] I.J. Cox, J. Killian, F.T. Leighton, T. Shamoon, Secure spread spectrum watermarking for multimedia, IEEE Transactions on Image Processing 6 (12) (Dec. 1997) 1673– 1687.

[4] Digimarc, http://www.digimarc.com/.

[5] Electronic Business Extensive Markup Language (ebXML), http://www.ebxml.org/.

[6] R. Iannella, Digital rights management (DRM) architectures, D-Lib Magazine 7 (6) (June 2001).

[7] Internet Open Trading Protocol—IOTP Version 1.0., http:// www.ietf.org/internet-drafts/draft-ietf-trade-iotp-v1.0-protocol-07.txt.

[8] InterTrust, http://www.intertrust.com/news/partnerspr/musicmatch.html.

[9] InterTrust, InterTrust Announces PowerChord Digital Rights Management Software, M2 Presswire, Coventry, Jun. 16, 1999.

[10] S.H. Kwok, C.C. Yang, K.Y. Tam, J.S.W. Wong, An SDMIbased rights management system for electronic media using digital watermarking, Proceedings of the International Conference on Electronic Commerce (ICEC 2000), August 2000, pp. 139 – 200.

[11] S.H. Kwok, K.C. Wong, K.F. Tsang, S.C. Cheung, K.Y. Tam, Digital rights management in Internet open trading protocol (IOTP), Proceedings of the International Conference on Electronic Commerce (ICEC 2000), August 2000, pp. 179 – 185.

[12] Universal Description, Discovery and Integration (UDDI), http://www.ddi.org.

[13] P. Wayner, Protecting your property in cyberspace, Computerworld 34 (2) (Jan. 10, 2000) 68.

[14] Windows Media Technologies, http://msdn.microsoft.com/ workshop/imedia/windowsmedia/IntroToWMT.asp.

[15] X. Yi, S. Kitazawa, E. Okamoto, X.F. Wang, K.Y. Lam, S. Tu, Agent-based copyright protection architecture for online electronic publishing, SPIE-Int. Soc. Opt. Eng., Proceedings of SPIE—The International Society for Optical Engineering 3657 (1999) 484– 493.

[16] J. Zhao, Applying digital watermarking techniques to online multimedia commerce, Proc. of the International Conference on Imaging Science, System and Applications (June 30 – July 3), 1997.
