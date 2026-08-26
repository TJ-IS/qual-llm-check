---
otero_id: 5690
otero_key: "BBCX33K9"
title: "Model checking for design and assurance of e-Business processes"
authors: "Bonnie Brinton Anderson; James V. Hansen; Paul Benjamin Lowry; Scott L. Summers"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.12.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 39 (2005) 333 – 344

www.elsevier.com/locate/dsw

# Model checking for design and assurance of e-Business processes

Bonnie Brinton Anderson, James V. Hansen\*, Paul Benjamin Lowry, Scott L. Summers

Marriott School of Management and Kevin Rollins Center for e-Business, Brigham Young University, 538 Tanner Building, Provo, UT 84602, USA

Received 29 April 2003; received in revised form 23 July 2003; accepted 22 December 2003

## Abstract

Use of the Internet for electronic business has the potential to revolutionize the way many businesses are conducted. Yet, several businesses have fallen victim to problems in information systems that facilitate e-Business. These problems are characterized by uncertainties due to system complexity, rapid development, interconnectivity, and a lack of familiarity with the new technologically based economy. This paper demonstrates how model checking can aid in the design and assurance of e-Business processes in environments characterized by distributed processing, parallelism, concurrency, communication uncertainties, and continuous operations. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: e-Business; Model checking; Money atomicity; Goods atomicity; Valid receipt; Process and communication protocols

## 1. Introduction

Electronic business (e-Business) on the Internet has the potential to revolutionize the way many businesses are conducted. Using the Internet as a medium for managing commercial transactions enhances accessibility to a wide variety of information and services, and greatly facilitates remote payments. Consequently, many firms are able to leverage critical business operations through Internet-based electronic processes. That this revolution has already begun is evidenced by the increasing number of resources that are procured, managed, created, and consumed over the Internet, Intranets, and Extranets. Even the world’s financial markets, telecommunications, and management of water and power supplies depend on the operations of massive Internet-based information systems [1].

At the same time, many businesses have fallen victim to problems in information systems that facilitate e-Business. Such problems include inadequate security, flawed controls, and poorly designed backend systems. In the e-Business environment, these issues are compounded by uncertainties that evolve from rapid development, system complexity, increased risk through interconnectivity, and lack of understanding of the new technology and networkbased economy [9].

It follows that as firms become progressively more dependent on Internet-based information systems, they are increasingly vulnerable to defects in those systems. These defects can lead to errors, undetected fraud, and a lack of defense against malicious intrusion. For example, an error in an information system designed for stock trading, banking, or air traffic control can be catastrophic; resulting damages can include lost revenue, lost data, lost trust, and increased costs. [9]

Accordingly, effective design of e-Business processes is essential for the avoidance of defects that could otherwise lead to errors, fraud, and intrusion. Carefully designed e-Business protocols can perform well within most expected situations. Yet guaranteeing correct processing under all circumstances is extremely complex and difficult. Hidden flaws and errors that occur only under unexpected, hard-toanticipate circumstances can lead to subtle mistakes and potentially ruinous failures. Continued growth of e-Business will in large part depend on protocols designed to ensure that the information exchanged between trading parties is protected from unauthorized disclosure and modification. While the model checking we propose cannot guarantee correct processing under all circumstances, given appropriate specifications of system requirements, those specifications can be accurately verified in the implementation. [7]

Verifying that an e-Business protocol is robust against hidden flaws and errors can be a daunting task. Manual methods are slow and error-prone. Even theorem provers, which provide a formal structure for verifying protocol characteristics, may require human intervention and can be time consuming. Moreover, if a failure is found with a theorem prover, it may provide little help in locating the source of the failure. Simulations offer computational power, but they are ad hoc in nature, and there is no guarantee they will explore all important contingencies. [9]

Model checking, on the other hand, is an evolving technology that offers a platform for effective and efficient evaluation of e-Business protocols. Current model checking technology is based on automated techniques that are considerably faster and more robust than other approaches such as simulation or theorem proving. With the best of today’s model checkers, very large state spaces can be analyzed in minutes. Additionally, model checkers are able to extend their analysis by supplying counterexamples that indicate the precise location where a protocol failure is discovered. [6]

While still relatively new to the analysis of e-Business processes [3,4,9], model checking has evidenced impressive performance in the practical analysis of complex hardware and software processes [5,8]. In this paper, we define and extend a state-ofthe-art e-Business protocol and use it as the basis to demonstrate how model checking can facilitate analysis of e-Business processes. The protocol we use is more sophisticated and complete than those used by Heintze et al. [4] and Wang et al. [9], as discussed in the next section. This protocol is due mainly to the work of Ray and Ray [6], which incorporates processes fundamental to a broad class of e-Business operations. These processes include distributed processing, parallelism, concurrency, communication uncertainties, and continuous operations.

The remainder of the paper is organized as follows: We first discuss related work on model checking, which has provided a foundation and motivation for our research. We then delineate the processes of a state-of-the-art e-Business model. Our application deals solely with procurement of digitized products, which involves slightly more complex processes than those involving physical goods. This delineation is followed by an implementation of the model in the failures/divergence refinement (FDR) model-checking software. We show in some detail how e-process failures are found and how counterexamples are used to identify the location and type of problem. Finally, we review the motivation for the use of model checking for Internet applications and suggest extensions that might be valuable.

## 2. Related work

Recent studies cf., [6] are finding that e-Business managers, developers, and auditors require robust tools to assure users that e-Business systems are secure and reliable. Designing and implementing highly secure and reliable e-processes is challenging and requires adherence to several specific criteria to be effective.

Adding to the challenge of designing effective e-Business protocols, current research has demonstrated that money atomicity, goods atomicity, and validated receipt are critical e-process requirements.

Money atomicity ensures that money is neither created nor destroyed in the course of an e-Business transaction. Goods atomicity guarantees that a seller receives payment only if the customer receives the product. Validated receipt ensures that the buyer is able to verify the contents of the product about to be received before making payment. [6]

Heintze et al. [4] use a model checker to examine the non-security characteristics of e-processes to verify the money and goods atomicity properties of two e-Business process-Digicash [1] and NetBill [2]. This seminal work demonstrated how to model e-Business processes and their properties of interest in a process algebra language, CSP, which is the language used in FDR. The model checker determined that the NetBill process does achieve money atomicity and goods atomicity. Conversely, the model checker discovered that Digicash failed to ensure money atomicity—an interesting finding in a commercial software package. In the latter case, a detailed counterexample was generated to illustrate a set of actions leading to a state where money atomicity was not realized. The model we use adds two important dimensions of complexity: real-time control of misbehavior by customer or merchant; and automatic control over the integrity of transactions involving digitized products.

Wang et al. [9] make a persuasive case that model checking not only can play a valuable role in designing e-processes, but also can be an effective way of evaluating and auditing existing e-processes. The authors use a ticket sales application to demonstrate the capabilities of two model checkers. While the application is conceptually straightforward, it abstracts the fundamental characteristics of many e-Business systems, including distributed processing, parallelism, concurrency, communication uncertainties, and nonstop operations. The authors emphasize that such properties are common to more complex applications, such as online stock trading and retailing.

Ray and Ray [6] extend the basic structures examined by Heintze et al. [4], who assume that neither the NetBill server nor the communication links to the NetBill server ever fail. Ray and Ray [6] provide a more comprehensive treatment of system and communication failures than addressed by Heintze et al. [4] by allowing a communication link among a customer, a merchant, or a trusted third party to fail arbitrarily. Additional mechanisms were developed that ensure that desirable properties are preserved despite such failures. The result is a realistic and practical platform for many e-Business applications. This platform incorporates the characteristics required by Ref. [9], while extending capability by including a trusted third party.

## 3. Protocol fundamentals

Fig. 1 represents the high-level abstraction of the protocol, and its processes are summarized as follows: Messages are exchanged between a customer, a merchant and a trusted third party (TTP). A merchant has several products to sell. The merchant places a description of each product on an online catalog service with a TTP, along with a copy of the encrypted product. When a customer finds a product of interest by browsing the catalog, he or she downloads the encrypted product and then sends a purchase order to the merchant. The customer cannot use the product unless it has been decrypted, and the merchant does not send the decrypting key unless the merchant receives a payment token through the purchase order process. The customer, in turn, does not pay unless he or she is sure that the correct and complete product has been received. The TTP provides anonymous support for purchase order validation, payment token approval, and approval of the overall transaction between the customer and the merchant.

Given these assumptions, the detailed steps of the protocol are as follows. (A use case diagram of these processes is depicted in Fig. 2; the corresponding sequence diagram is shown in Fig. 3.)

First, the customer browses the product catalog located at the TTP and chooses a product. The customer then downloads the encrypted product, along with the product identifier. The product identifier is a file that contains information about the product, such as its description and its identifier. If the identifier of the encrypted product file corresponds to the identifier in the product identifier file, the transaction proceeds. If the identifiers do not match,

![](/api/attachments/BBCX33K9/fulltext/images/e2de76e8ad6bc45f2effee2ef287297c6aa5a11f1e3acd9e840e3603cd2603c8.jpg)  
Fig. 1. High-level use-case diagram for trading digital products over the internet.

## Encrópted goods purchasing system

![](/api/attachments/BBCX33K9/fulltext/images/26d1e2c430426ad3fbe972096f0637679508d722b94574f21053f3e464a70e98.jpg)  
Fig. 2. Use-case diagram for comprehensive e-Business protocol.

![](/api/attachments/BBCX33K9/fulltext/images/f164555767083c94569e18af6adcae7347828e77ca79f05f9b75680a576f22bf.jpg)  
Fig. 3. Sequence diagram for comprehensive e-Business protocol.

advice is send to the TTP and the customer waits for the correct encrypted product. This process ensures that the customer receives the product that was requested from the catalog. Next, the customer prepares a purchase order containing the customer’s identity, the merchant identifier, the product identifier, and the product price. A cryptographic checksum is also prepared. The purchase order (PO), along with the cryptographic checksum, is then sent to the merchant. The combination of the PO and cryptographic checksum allows the merchant to ascertain whether the PO received is complete or whether it was altered while in transit. Upon receipt of the PO, the merchant examines its contents. If the merchant is satisfied with the PO, the merchant endorses the PO and digitally signs the cryptographic checksum of the endorsed PO. This is forwarded to the TTP. The TTP is involved in the process to prevent the merchant from later claiming non-acceptance of the terms and conditions of the transaction. The merchant also sends a single use decrypting key for the product to the TTP. Next, the merchant sends a copy of the encrypted product to the customer, together with a signed cryptographic checksum. The signed cryptographic checksum establishes origin of the product and also provides a check to signify whether the product has been corrupted during transit.

Upon receipt of this second copy of the encrypted product, the customer validates that the first and second copies of the product are identical. Through this process customers can be assured that they received the product ordered. The customer then requests the decrypting key from the TTP. To do this, the customer forwards to the TTP the purchase order and a signed payment token, together with its cryptographic checksum. The payment token contains the customer’s identity, the identity of the customer’s financial institution, the customer’s bank account number with the financial institution, and the amount to be debited from the customer’s account.

To verify the transaction, the TTP first compares the digest included in the PO from the customer with the digest of the same from the merchant. If the two do not match, the TTP aborts the transaction. Otherwise the TTP proceeds by validating the payment token with the customer’s financial institution by presenting the token and the sale price. The financial institution validates the token. If the token is not validated, the TTP aborts the transaction and advises the merchant accordingly. If the token is validated, the TTP sends the decrypting key to the customer and the payment token to the merchant, both digitally signed with the TTP’s private key.

Secure channels guarantee the confidentiality of all messages throughout this protocol. The protocol ensures money atomicity if the payment token generated by the customer contains the amount to be debited from the customer’s account and credited to the merchant’s account. Consequently, no money is created or destroyed in the system by this protocol.

Goods atomicity is guaranteed if the TTP hands over the payment token only when the customer acknowledges the receipt of the product. The process also ensures that the product is actually available to the customer for use when the customer gives the go-ahead for payment by acknowledging the receipt of the good.

Delivery verification is guaranteed if the TTP receives a cryptographic checksum of the product from the merchant. Also, the customer independently generates a checksum of the product received and sends it to the TTP. Using these two copies of the checksums, available at the TTP, both the merchant and the consumer demonstrate proof of the contents of the delivered goods.

## 4. Implementation of the protocol

This section discusses an implementation of the above protocol in FDR and an evaluation of its robustness. The FDR model implements key elements of the protocol with respect to money atomicity, goods atomicity, and valid receipt under several options. In order to avoid an overly technical presentation, the next section overviews a subset of representative processes that deal with money atomicity, goods atomicity, and validated receipt. The language of FDR is termed CSP (for communicating sequential processes). The writing of CSP code is greatly simplified by use of a compiler called Casper. Casper allows the user to describe the system in an abstract way, and the compiler converts that description to CSP code. We have included brief explanations of several expressions to assist the reader in understanding. These expressions represent processes that were outlined earlier, which should also aid in following the examples.

## 4.1. Illustrative customer processes

This element of the protocol demonstrates the process that occurs after the customer requests an encrypted product from the catalog hosted by the TTP. The downloading of the encrypted product is expressed as the transmittal of the encrypted product by the TTP and the receipt of the product by the customer. The process can be expressed in the following way:

CUST<sub></sub>DOWNLOAD

$$
= \text { cint }? x \rightarrow \text { ENCRYPTED\_PRODUCT } (x)
$$

The right-hand side is interpreted as follows: ‘cint denotes an incoming communication to the customer (c) from the TTP (t). ‘?x’ denotes that the transmission is x, where x is interpreted as an ENCRYPTED PRODUCT type.

When the customer has downloaded the product, he or she determines if it is the correct product. If the product is incorrect, the downloading process is repeated. This is modeled as follows:

RECEIVED<sub></sub>PRODUCTðx; yÞ

¼ if ðx ¼¼ yÞ then

RECEIVED<sub></sub>CORRECT<sub></sub>PRODUCT

else CUST<sub></sub>DOWNLOAD

## 4.2. Illustrative merchant processes

This element of the protocol shows the process by which the merchant waits to receive a purchase order from a customer, denoted as

$$
\text { MERCHANT\_WAIT } = \text { minc   ?x } \rightarrow \text { if(x == po) }
$$

then PO<sub></sub>RECEIVED Else MERCHANT<sub></sub>WAIT

$$
\text { PO\_RECEIVED } = (\text { moutc   !encryptedGoodsG }
$$

$$
\rightarrow \text { ENCRYPTED\_PROD\_SENT }
$$

Recall that minc ?x, refers to an input of x over the transmission link from merchant to customer. Conversely, moutc !encryptedGoodsG denotes an output of valid encrypted goods over the transmission link from merchant to customer.

After the merchant has transmitted the encrypted product, the merchant sends the decryption key to the TTP.

$$
\text { ENCRYPTED\_PROD\_SENT } = \text { moutt   !key }
$$

Following transmission of the key, the merchant waits to receive the payment token from the TTP. The TTP sends either the payment token to the merchant or if the transaction is aborted the TTP sends a transaction abort message.

$$
\begin{array}{c}\text {KEY\_SENT} = \text {mint ?x} \rightarrow \text {if(x==payToken)}\\\text {THEN SUCCESS}\\\text {else if(x==transAborted)}\\\text {then ABORT}\\\text {else KEY\_SENT}\end{array}
$$

## 4.3. Illustrative TTP processes

Recall that the first process shown for the customer was the downloading of an encrypted product from a catalog maintained at the TTP site. From the TTP site this is modeled as

TTP ¼ toutc !encryptedGoodsG

The TTP then waits to receive both a payment token from the customer and the key from the merchant. When the TTP receives a message, it expects either a payment token or a key; which of these two it will receive first is not known. In either case, the TTP must receive both before it can proceed. A corresponding expression is

$$
\begin{array}{l}\text {WAIT\_PAY\_KEY} = (\text {tinc ?u}\\\rightarrow \text {if (u == paymentToken) then WAIT\_KEY(u)}\\\text {else WAIT\_PAY\_KEY} | \sim | (\text {tinm ?v}\\\rightarrow \text {if (v == key) then WAIT\_TOKEN(v)}\\\text {else WAIT\_PAY\_KEY})\end{array}
$$

WAIT<sub></sub>KEY (u) and WAIT<sub></sub>TOKEN (v) are similar in that they wait for the respective object. When both objects have been received, they are checked. Based on the result of those checks, the transaction continues or aborts.

If the payment token and the key are satisfactory, the TTP sends the key to the customer and the payment token to the merchant. These processes can take place in either order.

SEND<sub></sub>KEY<sub></sub>TOKENðr; sÞ ¼ toutm !s

! SEND<sub></sub>TOKENðrÞ AfA toutc !r

! SEND<sub></sub>KEYðsÞ

4.4. Modeling money, goods, and validated receipt properties

Money atomicity is obtained when the payment token sent by the customer is received by the merchant, or when the customer sends the payment token and then receives a transaction abort message due to invalidation by the TTP. In brief, this is modeled in the following way:

ATOM<sub></sub>MONEY¼STOPAfAððcoutt:paymentToken

! mint:paymentToken ! STOPÞ

½ ðcoutt:paymentToken ! cint:transAborted

! STOPÞÞ

The satisfaction of this specification by the implementation guarantees that money atomicity is satisfied by the protocol.

Goods atomicity requires that the customer receives both the correct encrypted product and the keys, and the merchant receives the token; or that the customer receives just the encrypted product, and neither the merchant receives the payment token or the customer receives the keys. (encryptedGoodsB denotes invalid goods.)

ATOM<sub></sub>GOODS ¼ STOP AfA

ððcinm:encryptedGoodsG ! STOPÞ

½ ðcinm:encryptedGoodsB ! STOPÞ

½ ðcinm:encryptedGoodsG ! cint:key

! mint:paymentToken ! STOPÞ

½ ðcinm:encryptedGoodsG ! mint:paymentToken ! cint:key ! STOPÞÞ

Validated receipt is satisfied if the customer receives some encrypted product and does not make payment, or if the customer makes the payment after receiving the correct encrypted product.

VALID<sub></sub>RECEIPT ¼ STOP AfA

ððcinm:encryptedGoodsG! STOP

½ ðcinm:encryptedGoodsG ! STOPÞ

½ ðcinm:encryptedGoodsB ! coutt:paymentToken

! STOPÞÞ

## 5. Protocol verification

After expressing processes and constraints in the manner illustrated above, FDR explores the state space to determine if failures or vulnerabilities exist in the protocol’s processes. Using FDR, we found several problems in the model.

## 5.1. Failure in money atomicity

The first failure was discovered by running the model checker against the money atomicity specification in Section 4.4. For ease of exposition, we include only the money atomicity specification in this section even though the model checker is capable or evaluating multiple specifications in a single run. Underscoring its power, FDR evaluated 325 states and 825 processes in a few seconds. The following sequence of events was generated as automatic output:

toutc.encryptedGoodsG, cint.encryptedGoodsG, coutm.po, minc.po, moutc.encryptedGoodsG, cinm. encryptedGoodsG, moutt.key, coutt.paymentToken, Accepts {}<sup>1</sup>.

FDR shows that the following sequence of actions could be executed, leading to failure:

1. The customer downloads the encrypted product from the TTP.

2. The customer then sends a purchase order to the merchant.

3. The merchant then sends the encrypted product to the customer followed by sending the key to the TTP.

4. The customer then sends the payment token to the TTP, who next receives the key sent by the merchant.

At this point the processing stops (Accepts {}), indicating that money atomicity specification is not guaranteed by the implementation.

Importantly, FDR identifies the point in the process where the failure occurred, because the next step should have been receipt of the payment token by the TTP. By examining this process, we see that the failure is the result of allowing the TTP the option of aborting after the initial process.

WAIT<sub></sub>TOKEN<sub></sub>KEY ¼ ABORT AfA ðtinc ?a !

if ða ¼¼ paymentTokenÞ then WAIT<sub></sub>KEYðaÞ

else WAIT<sub></sub>TOKEN<sub></sub>KEY AfA ðtinm ?b !

if ðb ¼¼ keyÞ then WAIT<sub></sub>TOKENðbÞ

else WAIT<sub></sub>TOKEN<sub></sub>KEYÞ

There are two ways to solve this problem. One solution is to disallow the TTP option of aborting at this transaction point. The second possibility is to create a timeout channel that enables the merchant and customer to send a ‘transaction aborted’ message if no further actions are taken within a reasonable time. We do not pursue those details here.

## 5.2. Failure in money and goods atomicity

In a second run of the model checker using both the money atomicity and goods atomicity specifications we found that both money atomicity and goods atomicity are violated. The following sequence leads to a state where no further action occurs.

toutc.encryptedGoodsG, cint.encryptedGoodsG, coutm.po, minc.po, moutc.encryptedGoodsG, moutt. key, cinm.encryptedGoodsG, coutt.paymentToken, tinm.key, tinc.paymentToken, toutc.key, toutm.paymentToken, cint.key, Accepts {}.

FDR shows that the following sequence of actions could be executed, leading to failure:

1. The customer receives the encrypted goods from the TTP, and then sends a purchase order to the merchant.

2. The merchant then sends the encrypted goods to the customer and sends a key to the TTP, after which the encrypted goods are received by the customer who sends a payment token to the TTP.

3. The TTP then receives the key from the merchant and the payment token from the customer.

4. The TTP then sends the payment token to the merchant, after which the customer receives the key from the TTP. The process then stops. Since the next step should have been the receipt of the payment token by the merchant (from the TTP), we know where to look to examine the failure.

That indicated process in FDR was expressed as

KEY<sub></sub>SENT ¼ SUCCESS AfA mint ?x !

if ðx ¼¼ paymentTokenÞ then SUCCESS

else if ðx ¼¼ transAbortedÞ then ABORT

else KEY<sub></sub>SENT

This indicates that instead of accepting the payment token from the TTP, the merchant has been allowed to declare SUCCESS, an event that halts further processing. Again, the solution here is to use a time-out mechanism or to eliminate the SUCCESS option.

## 5.3. Failure in valid receipt

A third failure found with FDR concerns valid receipt. The valid receipt property ensures that one of the following events occurs [6]:

1. The customer receives an encrypted product and does not make payment (wrong product or decides not to purchase).

2. The customer makes the payment after receiving the correct encrypted product. We run the model checker to evaluate the implementation against the specification, with the following result:

toutc.encryptedGoodsG, cint.encryptedGoodsG, coutm.po, minc.po, moutc.encryptedGoodsG, cinm. encryptedGoodsG, Accepts{}.

In this case, the TTP sends, and the customer receives, valid encrypted goods. The customer then sends a purchase order to the merchant. This is followed by the sending of encrypted goods from the merchant to the customer, and their receipt by the customer. On the surface, this appears to be a logically sound process; however, there is no provision for processing invalid encrypted goods. Examining the process reveals the following:

PO<sub></sub>REC ¼ moutc !encryptedGoodsG

## ! ENCRYPTED<sub></sub>GOODS<sub></sub>SENT

Indeed, the only item sent to the customer in response to the purchase order is valid encrypted goods, a response that does not account for erroneous transmissions as prescribed in the VALID<sup>\_</sup>RE-CEIPT specification of Section 4. This problem is resolved in the following way, as affirmed by another run of the model checker:

$$
\mathrm {PO\_ {R} EC} = (\text { m   o   u   t   c }! \text { e   n   c   r   y   p   t   e   d   G   o   o   d   s   G }
$$

! ENCRYPTED<sub></sub>GOODS<sub></sub>SENTÞ AfA

ðmoutc !encryptedGoodsB

! ENCRYPTED<sub></sub>GOODS<sub></sub>SENTÞ

## 6. Discussion

The objective of this paper is to provide an accessible explication and demonstration of the efficiency and effectiveness of a model checker in evaluating e-Business processes. In particular, when many processes are distributed and automated, a great many states and processes need to be evaluated. Evidence suggests that such evaluation is beyond the practical capabilities of manual procedures, theorem provers, and simulation-leaving e-Business partners vulnerable to unforeseen failures and their corresponding costs. Model checkers do not guarantee the discovery of all vulnerabilities; yet recent implementations provide efficient and effective evaluation of very large state spaces for specified criteria. Notably, model checkers identify counterexamples that define the sequences of processes leading to failure.

The ability to query a model for violations of atomicity or any other deficiency is a powerful tool to combat errors, fraud, and intrusion. Users of model checkers can specify criteria which would allow an error, fraud, or intrusion. The model checker is able to evaluate the entire state space against these criteria and produce output which would either identify where a violation could occur or indicate that the model is robust against the particular criteria. One should note that the violation of money atomicity included in Section 5.1 is a type of fraud. In this case, the TTP could fail to deliver the goods (encrypted key) after the payment token has been sent by the customer. As such the customer is defrauded of their payment.

We have shown that the key elements of a state-ofthe-art e-Business protocol can be modeled using FDR. As the fundamental elements of the e-Business protocol that we have incorporated in our study are implemented in a large class of e-Business applications, there is considerable potential for further application. Given current concerns about Internet security, model checkers may have potential in both design and audit of a variety of system implementations. For example, as web support services develop the capability for accessing public registries of vendors, both search and subsequent transaction processes may benefit from application of model-checking technology. Model checkers may also have value in examining the processes of highly integrated applications as found in enterprise resource planning systems. As one of the reviewers noted, users should be aware of a possible state-space explosion, which can dramatically reduce the model checker’s efficiency. This is of particular concern where there are many parallel operations. Nevertheless, Roscoe (2000) notes that the existence of this barrier does not prevent one from modeling many systems which are both non-trivial and practical. FDR, for example, can deal entirely explicitly with combinations with order $1 0 ^ { 7 }$ states at several million states per hour on a laptop computer.

It should be noted that the example modelchecking language we used, CSP, could be quite complex for practitioners to use. However, a recently developed model checking language, called Casper, has abstracted away this complexity by adding a higher-level language whose interpreter translates its code into CSP. A more important point is that once a specification is correct it can be continually re-used regardless of what systems are used to conduct the process. Thus, the up-front investment in process modeling and model checking bears long-term yields in terms of system reliability, as systems upgrades and changes are implemented.

A feature of model checking that should be of particular interest to e-Business designers is the capability of developing specification statements that must be satisfied by the implementation. For demonstration purposes, our presentation focused on money atomicity, goods atomicity, and valid receipt, because these are fundamental to e-Business. However, model checking can be used to test a wide variety of protocol features. This approach should help not only protocol designers, but also auditors. In other words, these types of systems need to have adequate controls built in prior to implementation and will need adequate auditing after implementation.

## 7. Conclusion

e-Business is moving forward at a rapid pace across the globe. Hence, businesses are exposed to e-Business processes that are increasingly reliant on interdependencies among buyers, vendors, and TTPs. New e-Business foci, such as web services and pervasive computing, will extend the reach of e-Business, but these may increase complexity and exposure possibilities. Thus, the necessity of proactively identifying and rectifying e-process vulnerabilities is a strategic requirement for successful delivery in e-Business. Model checking can be an effective tool in the design of reliable protocols to support this growth.

## Acknowledgements

We would like to acknowledge the Kevin and Debra Rollins e-Business Center at Brigham Young University for providing support for this study. We would also like to thank Douglas Dean, Russell Sperry, and Don Norton for their editing and reviewing assistance.

## References

[1] D. Chaum, A. Fiat, M. Naor, Untraceable electronic cash, Advances in Cryptology—CRYPTO ’88 Proceedings, 1990.

[2] B. Cox, J. Tygar, M. Sirbu, Netbill security and transaction protocol, Proceedings of the First USENIX Workshop in Electronic Commerce, 1995 July.

[3] Ernst, Young, Doing eCommerce Right, 2000 March 15.

[4] N. Heintze, J. Tygar, J. Wing, H. Wong, Model checking electronic commerce protocols, Proceedings of the 2nd USENIX Workshop in Electronic Commerce, 1996 November.

[5] G. Lowe, Breaking and fixing the needham-schroeder publickey protocol using FDR, Tools and Algorithms for the Construction and Analysis of Systems: Second International Workshop, TACAS, 1996 March.

[6] I. Ray, I. Ray, Failure analysis of an e-commerce protocol using model checking, Proceedings of the Second International Workshop on Advanced Issues of e-Commerce and Web-based Information Systems, Milpitas, CA, 2000 June.

[7] I. Ray, I. Ray, N. Narasimhamurthi, A fair exchange e-commerce protocol with automated dispute resolution, Proceedings of the Fourteenth Annual IFIP WG 11.3 Working Conference on Database Security, Schoorl, The Netherlands, 2000 August.

[8] A. Roscoe, The Theory and Practice of Concurrency, Prentice-Hall, Englewood Cliffs, NJ, 2000.

[9] W. Wang, Z. Hidvegi, A. Bailey, A. Whinston, E-process design and assurance using model checking, IEEE Computer 33 (10) (2000 August) 48 – 53.

![](/api/attachments/BBCX33K9/fulltext/images/3aa5cd76f885324bdfc14c93b6ec34456bf64eda42bd183b0ecfd709f5c83995.jpg)  
Bonnie Brinton Anderson received her PhD from Carnegie Mellon University and is currently an Assistant Professor of Information Systems at the Marriott School of Management at Brigham Young University. Her research interests include software engineering, user acceptance of software, and business process reengineering. Dr. Anderson is also interested in computer simulation modeling and online transaction security.

![](/api/attachments/BBCX33K9/fulltext/images/728b0da9818f676951ff03d845a6eb65b979755cf34483b2cd9e0e12c3c49d6a.jpg)

James V. Hansen is Glen Ardis Professor in the Information Systems Group of the Marriott School of Management at Brigham Young University. He also is a faculty researcher at the Rollins Center for e-Business at the Marriott School. He received his PhD from the University of Washington, Seattle. Professor Hansen serves on the editorial boards of IEEE Intelligent Systems, Information Systems Frontiers, and Intelligent Systems in Ac-

counting, Finance and Management, and is listed in Who’s Who in Science and Engineering. His research interests are in machine learning and agent-based systems, with recent publications appearing in Computers and Operations Research, Genetic Programming and Evolvable Machines, IEEE Transactions on Neural Networks, and Journal of Experimental and Theoretical Artificial Intelligence.

![](/api/attachments/BBCX33K9/fulltext/images/8bcdc439e1fc9473fef5b6b0b38c8e4796592be143c286a0f5583b3dceeea355.jpg)

Paul Benjamin Lowry is an Assistant Professor of Information Systems at the School of Accountancy and Information Systems, Marriott School of Management, Brigham Young University. He also is a faculty researcher at the Rollins Center for e-Business at the Marriott School. His research interests include Internet-based collaboration, virtual teams, distributed facilitation, collaborative software, e-Business, and group-based HCI. Dr.

Lowry received his PhD in MIS from the University of Arizona where he was advised by Dr. Jay F. Nunamaker, Jr. His previous degrees include a BS in Information Systems and an MBA, both from Brigham Young University. His work experience includes several Fortune-100 companies, such as Ernst and Young Management Consulting, Ameritech, SoftSolutions/Novell, Price Waterhouse Management Consulting, and IBM. Some of his clients have included organizations such as 3M, Imation, Dial Corporation, the United Nations, the Wyoming Transportation Department, and Vanstar/Computerland. He has published in Journal of the Association for Information Systems (JAIS), Decision Support Systems (DSS), IEEE Transactions on Professional Communication, Journal of Business Comunication (JBC), and the Journal of Information Systems Education (JISE).

![](/api/attachments/BBCX33K9/fulltext/images/0172f8046c135e730fb1791cf73f97f95d6042e8015a119c90f10d194a882c2d.jpg)

Scott Summers is an Associate Professor of Accounting Information Systems as the School of Accounting and Information Systems, Marriott School of Management, Brigham Young University. Dr. Summers’ research interests include the effects of predisposition toward the computer environment, the impact of job characteristics in the modern accounting/ consulting practice on employee outcomes, and the evaluation of audit risk

and fraud detection risk. Dr. Summers received his PhD from Texas A&M University; he also received a MAcc and BS in Accounting from Brigham Young University. He has published in The Accounting Review, Behavioral Research in Accounting, Journal of Information Systems, International Journal of Accounting Information Systems, and The CPA Journal.
