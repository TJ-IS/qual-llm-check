---
otero_id: 15056
otero_key: "CXX6DECT"
title: "Secure attribute-based search in RFID-based inventory control systems"
authors: "Robin Doss; Rolando Trujillo-Rasua; Selwyn Piramuthu"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113270"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Secure attribute-based search in RFID-based inventory control systems

Robin Doss<sup>a</sup>, Rolando Trujillo-Rasua<sup>a</sup>, Selwyn Piramuthu<sup>b,∗</sup>

![](/api/attachments/CXX6DECT/fulltext/images/a910dcc788b8b6d5625d239232cc01943e2c5c4143638aebd864562d2ff0b5c1.jpg)

<sup>a</sup> Deakin University, Geelong, Australia Centre for Cyber Security Research and Innovation (CSRI), Australia

<sup>b</sup> Information Systems and Operations Management, University of Florida, USA

## A R T I C L E I N F O

Keywords: RFID secure search Attribute-based search EPC C1G2 passive tags Security protocols Formal verification

## A B S T R A C T

We develop a secure attribute-based search protocol for Radio Frequency Identification (RFID) systems. This protocol can be used to simultaneously identify groups of items that share a set of attribute values. To the best of our knowledge, this is the first such work with the potential to significantly enhance the security and intelligence of RFID-enabled applications in inventory control and supply chain management. The protocol is designed to be lightweight, suited for resource-constrained basic passive tags, and compliant with the Electronic Product Code (EPC) standards. This is achieved by exploiting the zero knowledge properties of quadratic residues. The security and privacy properties ofered by the protocol are rigorously proven through formal verification.

## 1. Introduction

Radio Frequency Identification (RFID) tags use radio waves [1] to operate in automated identification applications [2,3]. RFID tags are used as a replacement for barcodes in a majority of such applications due to their beneficial properties. For example, unlike barcodes that need to be on a flat surface to be read, RFID tags operate perfectly well regardless of the tagged object shape. RFID tags can be embedded and protected inside the object since direct line-of-sight is not a requirement, while barcodes sufer the consequences of being exposed to the elements as they are required to be on the outside of the object. Direct bright light could render barcodes unreadable, as visible contrast between diferent printed patterns is a requirement. Unlike sequential barcode reads, RFID allows for simultaneous batch reads of multiple tags, thereby increasing the read rate by several orders of magnitude. These and other related advantages render RFID applications to be more efective and eficient as compared to their barcode counterparts.

An RFID-based system comprises RFID tags, RFID readers, and associated back-end components. Each RFID tag has (limited) memory and processing power, which allow for information to be locally stored and processed on the tag for quick response. The readers communicate with the tags for various purposes that include authentication as well as information storage and retrieval. While the more expensive active tags can initiate communication with a reader, the more commonly used passive tags require the reader to initiate communication [4].

A significant diferentiating factor between RFID and barcode is the possibility of item-level information in the former whereas only classlevel information is possible in the latter. It is also possible for a user to search and locate specific RFID tags of interest. For instance, in a retail or warehousing setting, using an RFID reader, a user is able to search for specific RFID tags. Among currently available technologies that could be used for such applications, only RFID tags fit the bill with respect to reasonable unit cost and form factor. Between RFID tags and barcodes, although the unit cost of a barcode is orders of magnitude lower than that of even the cheapest passive RFID tag, RFID tags generally dominate when both costs and benefits are simultaneously considered together. To this end, several retailers (e.g., Macy's, Kohl's) have already begun rolling out item-level RFID tags on a specific few items (e.g., shoes, jeans) if not the complete set of items that are for sale (e.g., American Apparel) at their stores. The primary motivation behind RFID adoption in these scenarios include inventory control and shrinkage management.

Inventory control is an important facet in the retailing business since improper inventory management has the potential to significantly afect the bottom-line. Too much unnecessary inventory has the deleterious efects of associated inventory holding cost and the risk of obsolescence of items in inventory, among others. Too little inventory has the potential for stock-out situations, which could lead to loss of customers in addition to already lost sales. When an item that a customer requires is unavailable, in addition to this lost sale for the retailer, the customer might look at a competitor's ofering for that item and might even switch loyalty toward that competitor.

An important element in inventory control is item-level visibility of items [5]. In a typical retail setting, the existence of an item is determined from its entry (e.g., to the store or warehouse) and exit (e.g., from the store through the checkout counter). However, shrinkage can and does occur in-between the entry/exit events. Examples of shrinkage include theft (by employee and/or others), spoilage, misplacement, ticket-switching, improper checkout, among others. Shrinkage directly leads to incorrect inventory control since an item that is known or not known to exist may or may not be available at the store or warehouse. Stock-out situations can arise when an item is unavailable and the system registers it as available. Conversely, when an item is available but the system registers it as unavailable, more orders might be placed for that item which could lead to too much inventory of that item. When an item's existence and its other attributes (e.g., expiry date, outof-fashion) are known, appropriate actions can be taken to reduce such eventualities that are related to improper inventory control. With the help of item-level RFID, the size of a tag (and therefore, the corresponding tagged item) population can be readily determined.

While the development of eficient communication schemes for determining or estimating the size of a tag population has attracted attention from researchers, such schemes have not incorporated privacy and security measures [6-8]. This leaves them open for compromise by adversaries. For example, even without knowing a tag's identity, an adversary who listens in on the conversation between that tag and another entity (e.g., reader) can potentially track that tag. Even worse, a resourceful adversary can possibly even impersonate a tag or reader. To address such vulnerabilities, researchers have developed secure search protocols for RFID-based systems.

## 1.1. Motivation

The aim of secure search protocols is to enable a legitimate reader to securely query a tag population for one or more tags of interest. Predominantly, secure search protocols have been based on individual tag-identifiers and designed to enable a reader to locate a single tag within the area of coverage [9-12]. While there are applications for such protocols for instance in asset tracking and localization, in in ventory control there is often the need to query for stock levels of a particular product (e.g., shoes) in a secure manner. This work aims to extend tag search protocols in this direction to enable attribute-based search in a secure and privacy-preserving manner.

The motivation for our work is essentially two-fold. Firstly, while several secure search protocols have been proposed by researchers, all such protocols only support identifier(ID)-based tag searching [10,11,13-17]. This requires a reader to possess a priori knowledge of the ID of a particular tag of interest. Such knowledge is impractical to possess in large scale applications and particularly challenging for inventory control applications where the focus is on identifying the stock levels of diferent items rather than on locating individual tags. Therefore, there is a need for secure search protocols that can enable the safe and private searching of a tag population to identify the presence of one or more tags that share a common list of attributes. For example, an inventory control application where the stock level of a certain product type needs to be reconciled. We refer to this new type of RFID protocol as attribute-based search protocol.

Secondly, although the commonly used passive RFID tags do not allow for implementations that necessitate computationally expensive operations and large storage requirements, security and privacy measures still need to be taken to ensure their safe operation. For instance, secure hash functions usually require between 8 K to 10 K gates for implementation [12], whereas cheap passive RFID tags allow only about 2.5 K gates to be used to implement security features [12,18]. Cipher primitives such as Rivest-Shamir-Adleman (RSA) and Advanced Encryption Standard (AES) are dificult to embed in RFID tags with such hardware constraints [19,20]. Even relatively cheap options such as Elliptic Curve Cryptography (ECC) hardly meet the gate count and power consumption requirements of low-cost tags [21].

Contributions. We design a lightweight RFID search protocol suitable for the commonly used cheap passive RFID tags. Our design exploits the properties of Quadratic Residues (QR) [22], making it possible to implement the newly proposed protocol that relies only on 128 bit Pseudo-Random Number Generator (PRNG) and modular (MOD) operations on the tag side. As modular squaring is implemented with a few hundred gates [23] and a 128 bit PRNG is implemented with as little as 1.5 K gates [24], operationalization of the proposed protocol requires less than 2.5 K gates.

We deliver formal proofs on the security of the proposed protocol, showing that it can operate correctly in the presence of a Dolev-Yao adversary [25], i.e., an adversary that can block, manipulate and send messages. We also provide suficient conditions that, if met during the initialization phase of the protocol, allow our design to respect the privacy of individual tags as well as the privacy of the inventory stock as a whole. Using standard terminology from the RFID protocol literature [26,27], the proposed protocol is secure and supports the following properties.

Tag Anonymity: The proposed protocol resists information leakage, which can precipitate in the revelation of the tag's identification information to unauthorized parties (Proposition 1).

• Tag Untraceability: The messages in the proposed protocol appear to be random to an eavesdropper. This protects the tag against its location-based information being used to reveal social information on the tagged object or its owner (Corollary 1 and Proposition 2).

Resistance to Replay Attacks: With suficient variations in the messages that are communicated between any pair of entities (tag, reader, back-end) across diferent authentication rounds, the pro posed protocol does not allow messages to be replayed for successful authentication (Lemma 1 and Theorem 1).

• Resistance to Impersonation Attacks: With appropriate controls in place, the proposed protocol does not provide the opportunity for an adversary to impersonate tag, reader, or back-end (Lemma 1 and Theorem 1).

Organization. The remainder of the paper is organized as follows. We provide a brief discussion of published research studies on secure search in Section 2. We present and discuss the proposed attribute-based search protocol in Section 3. We then provide formal security and privacy analysis of the proposed protocol in Section 4, as well as a feature-based comparison with other similar protocols. We conclude our paper in Section 5.

## 2. Related work

The problem of searching or localizing an RFID tag among many is regarded as an important functionality of RFID systems. This is typically achieved by determining the presence, within the interrogation field of a reader, of a tag with a given identifier. Protocols with such a functional requirement are known as search protocols. Whether secure search is conducted respecting the anonymity of the tagged object or relying on expensive cryptographic primitives, varies from design to design.

While there are no extant attribute-based secure search protocols, researchers have developed other secure search protocols. We now consider some of these related published protocols, with specific focus on the security aspect. The scheme proposed by Huang and Shieh [14] conducts search directly on cipher texts, hence boosting performance. Their protocol is designed to detect the presence of a compromised reader, allowing readers and tags to recover from adversarial actions. However, their protocol is not in compliance with Electronic Product Code (EPC) standard compliant. Won et al. [28] developed a search method that utilizes the AES-128 block cipher and timestamps. This protocol was shown to be secure against reader privacy, tag cloning, Denial of Service (DoS), and desynchronization attacks. However, it is not EPC standard compliant, as it relies on a complex method such as AES that requires about 3400 gates for implementation [29]. Tan et al. [30] proposed a serverless secure search protocol in which the tags are required to store a list of all previous nonces in order to protect tag anonymity. This places a significant storage burden on the tag. A possible means to address this is to let only the tags with the same first m bits of the id respond. This method fails when the tag IDs are structured. For tag anonymity, as in Ref. [11], noise tag has been suggested as a solution wherein each tag responds with a probability of λ regardless of the intended query recipient. Won et al. [28] show that this fails to address the issues associated with illegal tag tracking.

The serverless search protocol developed by Kim et al. [10] does not require a trusted third party. This method has issues related to tag anonymity especially in scenarios that involve a small number of tags. Zuo [11] developed a secure search protocol that incorporates a pseudo-random function as well as a one-way hash function. Noisy tags are used to make tag responses indistinguishable, requiring the reader to only decrypt to ascertain if the response is from a non-noisy or a noisy tag in order to reduce the computational load on the reader. An issue with this method is that the reader is required to keep track of all tag IDs which in the event of a reader being stolen provides a significant advantage for an adversary to clone tags. A solution based on Physical Unclonable Functions (PUFs) was proposed by Kulseng et al., [12]. However, it was shown to be vulnerable to attacks that include tracking and desynchronization [31]. The search protocol with symmetric en cryption proposed by Chun et al., [15] is plagued by DoS attack vulnerability [32]. A few other protocols $[ 1 6 , 1 7 , 3 3 , 1 3 ]$ that have been developed for this purpose are not EPC standard compliant since they are not lightweight.

Hash-based schemes have been proposed by Mtita et al. [34], Zheng and Li [35] and Chen et al. [36]. In Ref. [34], Hashed Message Authentication Codes (HMAC) are employed while in Refs. [35] and [36] hash functions in conjunction with Bloom Filters are proposed. These functions are resource-intensive and underline the fact that simultaneous achievement of compliance with the EPC standard requirements and standard security goals is a non-trivial challenge. It has been shown that implementation of ECC requires about 8.2 K to 15 K gates [37]. Moreover, symmetric encryption methods that include AES require about 3400 gates [29]. As EPC standards, that include EPC G2v2, recommend usage of 16 bit Cyclic Redundancy Check (CRC) and 16 bit PRNG for passive tags, there is a need for more robust security without increasing tag cost. However, these are known to be vulnerable to brute-force attacks. 128 bit PRNG-based methods implementable on cheap passive RFID tags were proposed by Lee and Hong [24] and more recently Sundaresan et al. [38]. The 128bit PRNG in Ref. [24] is implemented using a Self-Shrinking Generator (SSG) that is based on a Linear Feedback Shift Register (LFSR) developed by Meier and Staffelback [39]. Molina-Gil et al. [40] resolve the linearity issues in SSG with a protocol that is shown to be resistant to exhaustive search. entropy, man-in-the-middle and relay attacks [41].

In contrast to previous work, our protocol does conform with the EPC standard, while it solves a more general problem than searching tags by identity matching. Our protocol allows readers to look for tags satisfying any property that can be defined as a list of attribute values, one of which could be the tag identity itself.

## 3. An attribute-based secure search protocol

We now present the proposed search protocol based on lightweight operations such as quadratic residues, modular and 128 bit PRNG operations. We first introduce a correctness property for search protocols that we prove our protocol satisfies, in Section 4. Then, we describe a lightweight cryptographic primitive based on quadratic residues, which we use in our scheme for encryption/decryption. Finally, we provide details on the setup and operational phases of the protocol.

## 3.1. Correctness of attribute-based search protocols

We provide a natural extension of identity-based search protocols to attribute-based search protocols by allowing a verifier (RFID reader) to execute arbitrary queries over a collection of provers (RFID tags). This assumes that provers are characterized by a set of attributes, as is the case in RFID systems where tags store information on the tagged object.

Let be the universe of attribute values. Given a tag $T ,$ we use the auxiliary function tag-info( $T ) \subseteq { \mathcal { A } }$ to represent the set of attribute values that are stored in T. We also use prod-info( )T to represent the set of attribute values characterizing the product T is attached to. Note that, typically one would expect equality between tag-info (T) and prod-info (T), i.e., the tag faithfully conveys the product information. However, in the next section we show that a relation of the type prodinfo (T) ⊆ tag-info (T) leads to a useful trade-of between privacy and scalability.

We define a query as a Boolean function q over the power set of attribute values, i.e., q: $\mathcal { P } ( \mathcal { R } )  \{ \mathrm { t r u e }$ , false}. And we use to represent the universe of queries of this type.

Definition 1 (Attribute-based search protocol). Given a collection of tags $T = \{ T _ { 1 } , . . . , T _ { n } \}$ within the interrogation field of a reader $R ,$ a search protocol is a communication protocol P between R and the tags in $T$ whose outcome is a subset of T satisfying a given query q. We say P is

sound if for every pair $( q , s ) ,$ , where s is the output of P based on the query made to the tags in $T ,$ it holds that $s \subseteq T$ and $\forall T _ { i } \in s \colon$ q(prod-$\mathsf { i n f o } ( T _ { i } ) ) = \mathsf { t r u e } .$

• complete if for every pair $( q , s ) ,$ s is the subset of maximum cardinality in T satisfying that $\forall T _ { i } \in \mathsf { ~ \Gamma ~ } s \mathrm { : ~ }$ q(prod-info

(T )) = true.Definition 1 considers soundness and completeness to be the main functional requirements of a search protocol. Soundness states that the output of the protocol should contain no false positive, and completeness that all tags whose attribute information evaluates q to true should be included. That is to say, we consider only attributebased search protocols that give no false positive and, by definition, no false negative.

Certainly, completeness is a strictly stronger property than sound ness. Completeness allows to determine the exact number of products of a given type or whether the product is present at all, while soundness gives a lower-bound on that number. However, completeness is also the hardest to meet in highly adversarial environment. We dedicate the remainder of this section to introduce a protocol that is sound in the presence of an adversary with full control over the network. We prove completeness when the adversary is not allowed to block messages between tags and readers, which is arguably a minor restriction on the adversary's capabilities. This means that our protocol achieves the strongest of the properties in the presence of a restricted, yet still powerful, man-in-the-middle attacker. For the case where the whole network is under adversarial control, then our protocol remains sound.

## 3.2. The quadratic residue property

Before providing details of our protocol, we introduce number theoretical properties of quadratic residues that we use for lightweight public-key encryption/decryption.

If there is an integer n $( 0 < x < n )$ for $x ^ { 2 } = R$ mod n to be valid, then R is a quadratic residue (mod n). For large primes a and $b ( a \neq b )$ such that $n = a b ;$ , assume that R is a quadratic residue (mod n). As per the Chinese Remainder Theorem, four incongruent solutions exist for this scenario. However. given that it is rather difficult to determine a and b, it is equally dificult to determine x [22,42]. If replacing x with $x ^ { 2 }$ results in a valid solution, which is a perfect square, only one of the solutions is a valid quadratic residue modulo n [22].

For implementation of modular squaring on low-end devices such as RFID tags, modular squaring can be replaced with integer squaring of the form $f ( x ) = x ^ { 2 } +$ kn, where k is carefully chosen $( \mathrm { i } . \mathrm { e } . , x ^ { 2 }$ mod n is replaced with $x ^ { 2 } + k n )$ . To compute f(x) for a 1280-bit wide $n ,$ the square $x ^ { 2 }$ and the product kn are computed separately and then combined (with carries bufered for the next iteration). Further, the individual bits of $x ^ { 2 }$ and kn can be evaluated by convoluting x with itself and k with n using a 128 bit register and invoking a PRNG. The cost of implementing such a function f can be estimated as 640 gates for read only storage of the 1280 bit modulus n, a PRNG, and bufers for com putation. The overall complexity of implementing f is less than 1000 gates, as shown in Refs.[43,42].

## 3.3. Initialization phase

Readers and tags are initialized with the necessary secrets and relevant information. Multiple participants are involved in the protocol, acting in three diferent roles: server, reader and tag. For simplicity, we consider a single server, although our scheme can be generalized to multiple servers. We assume that the readers share a secret symmetric key with the server. We use k(S,R) to represent the symmetric secret key between server S and reader R. In addition, readers and tags are setup with the server's public key n, which the server generates as the product of two large and secret prime numbers a and $b , \mathrm { i . e . , } n = a b .$ . Finally, each tag T in the system is initialized with a secret identifier $I D _ { i }$

In addition to the key material, RFID tags are also initialized with attribute information describing the product T is attached to (e.g., Apple, male T-shirt). As stated earlier, the auxiliary functions tag-info (T) and prod-info(T) are used to indicate the information stored in tag T.

## 3.4. The protocol

The protocol assumes an insecure communication channel between all participants. That is to say, we assume a network that is under full control of the standard Dolev-Yao attacker. This ensures that the scheme is suitable for use with both fixed and mobile readers as well as in cloud-based environments where the back-end database (server) can be hosted in the cloud.

In conformance with the interrogator talks first (ITF) approach defined by the EPC global standard, the search query in our proposed scheme is always initiated by a reader. We note here, that distinct from ID-based search, in attribute-based search the tags and readers in the system do not share any secret information with each other. Instead, we incorporate a collaborative authentication process where the tag information is released by the server only after authentication of the reader by the server.

Our protocol consists of two phases (see Fig. 1). During the first phase, R sends a nonce $N _ { R }$ along with a query q. Tags whose attribute values satisfy the query reply by encrypting the reader's nonce, a freshly generated nonce and its secret identity with the public key of the server. Such encryption is performed using a lightweight modular exponentiation based on quadratic residues. The secret identity $I D _ { i }$ of tag $T _ { i }$ is used to identify the tag, while the nonce $N _ { i }$ generated by $T _ { i }$ is used to prevent traceability. Because the reader itself cannot decrypt messages sent from tags, it collects all tag replies and sends that collection to the server, which kicks of the second phase of the protocol. To ensure integrity of the reader-to-server communication, the reader encrypts with the reader-server shared key the initial query $q ,$ its own nonce $N _ { R }$ and the hash $h ( X _ { 1 } ^ { \prime \prime } , . . . , X _ { m } ^ { \prime \prime } )$ of the m responses obtained from the tags.

Upon reception of the reader's message, for every $i \in \{ 1 , . . . , m \}$ , the server decrypts the tag's response $X _ { i } ^ { \prime \prime }$ by solving the quadratic residue problem described previously. This allows the server to obtain $X _ { i } = N _ { R } \lvert \lvert N _ { i } \rvert \lvert I D _ { i } ,$ where $N _ { i }$ and $I D _ { i }$ are the tag's freshly generated nonce and secret identity, respectively. Then the server performs the following sanity checks for each $X _ { i } .$

• The reader's nonce in $X _ { i }$ matches the nonce sent by the reader. This prevents replay attacks that use messages from previous protocol

executions in other sessions.

• The tag identity $I D _ { i }$ is correct, $\mathbf { i . e . , \textit { I D } } _ { i }$ corresponds to a valid tag identity.

q(tag-info(T )) = true and q(prod-info(T )) = true, where $q$ has been sent encrypted by the reader. This is used to meet the soundness property enunciated in Definition 1. More details are given in Section 4 below.

Tag responses not meeting the above conditions are discarded. Let $\{ T _ { i _ { 1 } } , . . . , T _ { i _ { j } } \} \subseteq \{ T _ { 1 } , . . . , T _ { n } \}$ be the subset of tags the server considers valid. The server finalizes the protocol by sending the collection of attribute values {prod- ${ \mathrm { . i n f o } } ( T _ { i _ { 1 } } ) ,$ ,prod-info… $( T _ { i _ { j } } ) \}$ to the reader together with the reader's nonce and query. This information is used by the reader to determine the number of tags that satisfy the query q and to possibly display their information.

## 3.5. Key management

We end this section by discussing the design choice of relying on a single asymmetric encryption key to secure the communication between tags and readers.

Being this protocol the first attribute-based search protocol, we aim for simplicity of design and provable security properties. That is to say, our primary goal is to provide an attribute-based search protocol that is correct with respect to Definition 1, can be proven secure in the presence of standard adversarial models for communication protocols, and optimizes computational complexity, in particular on the tag's side. The latter rules out mutual authentication between readers and tags, as it requires additional secrets and cryptographic operations to be stored and executed, respectively, on tags.

We achieve tag authentication, which is needed to satisfy soundness, by allowing tags to have a unique secret and perform encryption by using the public key of the server. This means that the server can authenticate tags by performing a simple look-up operation in its da tabase. Certainly, a symmetric key, rather than an asymmetric key, would also allow for tag authentication, but at the cost of either dropping tag privacy or requiring the server to exhaustively search for the correct symmetric decryption key. Such trade-of between privacy and scalability in RFID identification protocols based on symmetric keys has been largely studied in literature [44-46] and remains a challenge.

A consequence of relying on a single public key to encrypt the messages sent by tags is that confidentiality is lost if the server secret key is compromised. This means that revoking and updating public keys in RFID tags should be part of the incident response plan in case of an attack to the server. By using best practices in computer security, however, a server compromise is regarded as a rare event. Hence we do not provide details on how revocation and updating can take place in an RFID environment like the one described here and consider these processes out of the scope of this paper.

To summarise, although many RFID protocols do aim at being serverless, achieving mutual authentication between tags and readers, and using symmetric key encryption rather than asymmetric encryption, we do not consider those to be primary goals of an attribute-search protocol. Extending the current design with those properties is an interesting avenue for future work, though.

## 4. Security and privacy analysis

We next prove correctness of the proposed protocol via transformation to a high level specification that can be formally verified by the protocol verification tool Scyther [47]. We also perform a formal privacy analysis of the protocol.

<table><tr><td>Server [n = ab, R, k(S, R)]</td><td>Reader [k(S, R), n]</td><td>Tag [IDi, tag-info(Ti), n]</td></tr><tr><td rowspan="3"></td><td>NR← PRNG(·)A query QQ, NR----&gt;</td><td rowspan="2">If q(tag-info(Ti)) = trueNT← PRNG(·)Compute: Xi=N_R||N_T||ID_iCompute: Xi&#x27;&#x27;=(Xi2)2mod nX&#x27;&#x27;&lt;----</td></tr><tr><td>X=(X1&#x27;&#x27;, ..., Xm&#x27;m)</td></tr><tr><td>X, {q, NR, h(X)}k(S,R)&lt;----</td><td></td></tr><tr><td>Let Resp = ∅For every Xi&quot;Use a and b to decrypt Xi&quot; and obtain NR&#x27;||NT&#x27;||ID&#x27;If NR&#x27; ≠ NR or k&#x27; is invalid, ignore response elseLet Ti be the tag with key ID&#x27;If q(tag-info(Ti)) = q(prod-info(Ti)) = trueadd prod-info(Ti) to Resp{q, NT, Resp}k(S,R)----&gt;</td><td>Decrypts the messageChecks that q and NT are correctDisplays Resp</td><td></td></tr></table>

Fig. 1. Proposed secure attribute-based search protocol.

## 4.1. Security model

We use the symbolic security model introduced in Cremers and Mauw [25]. Their model considers a standard Dolev-Yao adversary who can eavesdrop, block, modify and send messages. The adversary is also capable of compromising protocol participants by learning their long term secret keys. This is particularly important in RFID systems where tags are relatively easy to tamper with. Cremers and Mauw provide their model with a trace-based operational semantics, making it possible to analyze properties of protocols by looking at the properties of their traces.

Protocols in Cremers and Mauw's model are defined as a set of roles, roles as a sequences of events, and events as the action of sending or receiving a message. Events within a given role ought to be executed sequentially, yet they can be interleaved with events from other roles, allowing for an asynchronous execution of the protocol. Because the adversary is in full control of the network, all receive events are triggered by the adversary. In other words, there does not exist a covert or secure channel between protocol participants. A trace or execution of the protocol is thus a valid sequence of events that respect the restrictions above.

The authentication property we use is called non-injective agreement in Ref. [25] and full agreement in Ref. [48]. We describe that property informally, as in Ref. [48], and refer the reader to Cremers and Mauw [25] for a more formal treatment.

Definition 2 (Non-injective agreement). Let P be a protocol and R a role in P. The role R satisfies non-injective agreement in P if for every honest agent A executing the role R, when A completes a protocol run, with another agent B, then B has previously been running the protocol with A and the two agents agreed on all the atomic data items used in the protocol run.

Cremers and Mauw developed an eficient and simple push-button tool called Scyther [47] for the automated verification of authentication properties, such as non-injective agreement. Scyther ofers unbounded verification with guaranteed termination. Our goal next is to specify our protocol within Cremers and Mauw's formalism and use Scyther to formally prove the various security properties that our protocol satisfies, including non-injective agreement.

## 4.2. A high level specification

Cremers and Mauw's model assumes idealized encryption, i.e., encryption is secure, and focuses on detecting logical flaws in protocols. This requires replacing operators that are not supported, such as XOR, concatenation, exponentiation, etc., by symbolic operations with the same functional and security goal. In our case, we only need to replace the exponentiation of m modulo n by a generic public key encryption function, denoted $\left\{ m \right\} _ { n } ,$ where m is the plain text message and n a public key. We write pk(S) and sk(S) to denote the public and private key, respectively, of S. Finally, we assume that nonces are fresh, i.e., nonces do not repeat.

The resulting high level specification of our search protocol is depicted in Fig. 2, using the Message Sequence Chart (MSC) graphical language formalized in Ref. [49]. We also provide a formal specification within the Scyther language in the Appendix section.

We use $P _ { n }$ to denote the protocol depicted in Fig. 2 when it is intended to be executed with n RFID tags. In the remainder of this section, we analyze security and privacy properties of $\boldsymbol { P } _ { n } .$ . Our main claim at this point is that the security of the attribute-based search protocol introduced in the previous section follows from the security of $P _ { n } .$

![](/api/attachments/CXX6DECT/fulltext/images/4eb95d2b833b9af690fc7d6037fddb78a68437993028d7b115c89fb87bd4668c.jpg)  
Fig. 2. A high-level specification of our search protocol for multiple RFID tags; for readability only two tags are displayed. The hexagon represents a security property which is expected to be satisfied.

## 4.3. Security analysis

To verify that $P _ { n }$ operates correctly even in the presence of man-inthe-middle attackers, we show first that it satisfies the security property non-injective agreement, or simply agreement, as introduced by Cremers and Mauw [25]. A protocol is said to satisfy agreement if after the execution of the protocol all parties agree on the content of the messages, as specified by the protocol.

## Lemma 1. $P _ { 1 }$ and $P _ { 2 }$ satisfy non-injective agreement.

Proof. We use the security protocol verification tool Scyther [47] to prove this result. The specification of $P _ { 1 }$ and $P _ { 2 }$ can be found in the Appendix section. Because the end of the protocol is defined by the message from the server to the reader, we placed a non-injective agreement claim event, depicted in the protocol MSC specification by a hexagon, at the end of the specification of the reader role. This is used by the tool as a placeholder to indicate those execution steps where the property non-injective agreement ought to be satisfied.

The lemma above states that our protocol, when executed with one or two tags, guarantees that all parties agree on the content of the messages. Because Scyther cannot be used to prove non-injective agreement for the general case of multiple tags, i.e., for every protocol $P _ { n }$ with $n \ \geq \ 1$ , we generalize the previous lemma to an arbitrary number of tags next.

Lemma 2. $P _ { n }$ satisfies non-injective agreement.

Proof. We observe that the interaction between reader and each individual tag is a standard challenge-response message exchange that satisfies non-injective agreement. This is proven by Scyther for $P _ { 1 }$ and $P _ { 2 } ,$ and can be generalized to $P _ { n } \left( n \geq 1 \right)$ given that each tag' response is independent of another tag's response.

Now, assume that $P _ { n }$ satisfies non-injective agreement. We prove that $P _ { n + 1 }$ satisfies non-injective agreement as well. Consider $r _ { 1 } , . . . , r _ { n + 1 }$ to be the responses from $n + 1$ tags. Because $P _ { n }$ satisfies agreement, we can correctly finalize the protocol by considering either the responses $r _ { 1 } , . . . , r _ { n }$ or $r _ { 2 } , . . . , r _ { n + 1 }$ . Such executions can be obtained by selectively blocking a tag's reply. This means that reader and server are capable of agreeing on the following messages (hypothesis of induction).

$$
\begin{array}{r l} & {\bullet (r _ {1}, \dots , r _ {n}), \{q, N _ {R}, h (r _ {1}, \dots , r _ {n}) \} _ {k (S, R)}} \\ & {\bullet (r _ {2}, \dots , r _ {n + 1}), \{q, N _ {R}, h (r _ {2}, \dots , r _ {n + 1}) \} _ {k (S, R)}} \end{array}
$$

It follows that from the two messages above, reader and server can agree on $( r _ { 1 } , . . . , r _ { n + 1 } ) , \{ q , N _ { R } , h ( r _ { 1 } , . . . , r _ { n + 1 } ) \} _ { k ( S , R ) } ,$ which implies that reader and server agree on the content of their first message exchange. Agreement on the message between the server and the reader is proven analogously, which concludes the proof.

Non-injective agreement is a strong security property that our protocol has been proven to satisfy, implying that our protocol resists wellknown attacks such as replay and impersonation attacks. It remains to prove that the protocol satisfies correctness with respect to Definition 1. Theorem 1. $P _ { n }$ is a sound search protocol in the presence of a Dolev-Yao adversary. If the adversary does not tamper with the tag-to-reader communication and for every tag T in the system and every query $q$ it holds that q(prod-info(T)) ⟹ q(tag-info(T)), then $P _ { n }$ is both sound and complete.

Proof. Because $P _ { n }$ satisfies agreement, upon finalization of the protocol all parties agree on the content of the messages. Given that the server enforces soundness and both reader and server share the same view on their message exchanges even in the presence of a Dolev-Yao attacker, we conclude that $P _ { n }$ is sound (see Definition 1).

To prove completeness we observe that, given the set of tags $\{ T _ { 1 } ,$ $\ldots , T _ { n } \}$ within the interrogation field of the reader, every tag T such that q(prod-info(T)) = true also satisfies that q(tag-info(T)) = true, hence it will reply to the query q. Therefore, assuming that messages are not blocked, the server will receive responses from the subset Q $\subseteq \{ T _ { 1 } , . . . , T _ { n } \}$ of maximum cardinality such that q(tag-info(T)) = true for every $T \in Q ,$ which concludes the proof.Theorem 1 provides a suficient condition for our RFID attribute-based search protocol to be sound and complete in the presence of a Dolev-Yao adversary, provided that the quadratic residues encryption/decryption scheme is secure. We argue for soundness to be the most interesting and realistic property among the two. Completeness may play a role in critical applications where an adversary-free environment, e.g., via signal jamming, can be established.

## 4.4. Privacy analysis

We start our privacy analysis by proving a simple secrecy property of the proposed protocol.

Proposition 1. Let $T _ { i }$ be a tag that has not been compromised and $\{ N _ { R } , N _ { i } , I D _ { i } \} _ { p k ( R ) }$ its response to a reader's challenge $N _ { R } .$ Then the adversary is unable to learn either $N _ { i }$ or $I D _ { i }$

Proof. We use Scyther to prove that $N _ { i }$ and $I D _ { i }$ remain secret in $P _ { 2 }$ (see specification in the Appendix Section). The same property holds in $P _ { n }$ given that tags reply independently to a reader's query.

The main corollary of the proposition above is that all messages sent by an uncompromised tag are fresh, because the tag's message uses a tag-generated secret nonce. This signifies that a tag's response is indistinguishable from its own previous responses and from the responses of other uncompromised tags.

Corollary 1 (Tag untraceability). Let $T _ { i }$ and $T _ { j }$ be two tags that have not been compromised. Let b $\in _ { R } \{ i , j \}$ a random choice and $r _ { b } = \{ N _ { R } , N _ { b } , I D _ { b } \} _ { p k ( I }$ R) the response of $T _ { b }$ to a reader's challenge $N _ { R } .$ . Given the response $r _ { b } ,$ , the adversary cannot determine with probability higher than $_ { 1 / 2 }$ whether $r _ { b }$ is T<sub>i</sub>’s or $T _ { j } { ' } s$ response.

We remark again that in our security and privacy analyses, we are considering idealized cryptography in which cryptographic primitives cannot be cracked.

Even though RFID tags cannot be traced based on the messages exchanged in our protocol, an adversary can still infer information from the fact that a tag replies to a given query, which indicates that the attribute value of that tag satisfies the query. We use $\sim _ { q }$ to denote the equivalence relation on the set of tags defined by $T _ { 1 } \sim _ { q } T _ { 2 } \Longleftrightarrow q ( { \mathrm { t a g - i n f o } }$ $( T _ { 1 } ) ) = \mathtt { t r u e } \mathtt { \Gamma }$ q(tag-info $( T _ { 2 } ) ) = \mathtt { t r u e }$ , and $[ T ] / \sim _ { q }$ to the equivalence class in $\mathcal { T }$ with $T \in [ T ] / \sim _ { q } .$ . That is to say, we formalize the notion that two tags are indistinguishable with respect to their set of attribute values.

Proposition 2. The probability of correctly associating two messages to a given tag T in response to a query q is equal to

$$
\left\{ \begin{array}{l l} \frac {1}{| [ T ] / \sim_ {q} |} & \text {if} q (\operatorname{tag - info} (T)) = \operatorname{true} \\ 0 & \text {otherwise,} \end{array} \right.
$$

We observe that our attribute-based search protocol satisfies a classical anonymity property known as k-anonymity [50], whereby responders are grouped into equivalence classes, and the anonymity of a responder is proportional to the size of its equivalence class. Determining the appropriate size for each anonymity class is contextspecific and out of scope for this study.

It is worth remarking that our protocol does not satisfy the untraceability properties introduced by Avoine in Ref. [51], such as Existential-UNT-SEQ. The reason is that those notions are defined based on a non-negligible probability of distinguishing two tags. We cannot attain such a low probability unless we create anonymity classes of large cardinality, which contradicts our goal of decreasing the communication complexity. In fact, we claim that such strong privacy notions are hardly justifiable in low-cost RFID tags with little to no stored sensitive information. Instead, we are interested in the confidentiality of the stock, i.e., of the information contained in the set of RFID tags rather than in individual tags.

Next, we provide a measure of stock privacy as the diference between the attribute information stored in the tags and that which is stored in the server with respect to the set of available queries. Definition 3 (Stock uncertainty). The stock uncertainty is given by

$$
\min _ {q \in Q _ {\mathcal {A}}} \left\{\left| \left\{T \in \mathcal {T} | q (\text { prod - info } (T)) \right\} \right| - \left| \left\{T \in \mathcal {T} | q (\text { tag - info } (T)) \right\} \right| \right\}
$$

Stock uncertainty gives the minimum number of tags an adversary will falsely count as satisfying a given query. It is worth noticing the trade-of between stock privacy and scalability, given that the more tags incorrectly reply to a query, the larger the communication complexity of the protocol. It is thus the task of the stock owner to decide on how to properly balance such a trade-of during the initialization phase. Note that if tag-info(T) = prod-info(T) for every tag T, then the search protocol provides no stock privacy at all.

Security and privacy properties. The list of criteria used in the columns is as follows: P1) Attribute Search, P2) Mutual Authentication, P3) Tag Anonymity, P4) Tag Untraceability, A1: Replay Attack, A2: DoS/De-synchronization and C1) EPC Compliance.

<table><tr><td>Scheme</td><td>P1</td><td>P2</td><td>P3</td><td>P4</td><td>A1</td><td>A2</td><td>C1</td></tr><tr><td>Huang et al. [14]</td><td> $\times$ </td><td> $\times$ </td><td>✓</td><td>NA</td><td>NA</td><td>✓</td><td> $\times$ </td></tr><tr><td>Won et al. [28]</td><td> $\times$ </td><td> $\ddagger$ </td><td>✓</td><td> $\times$ </td><td>✓</td><td>NA</td><td> $\times$ </td></tr><tr><td>Tan et al. [30]</td><td> $\times$ </td><td> $\ddagger$ </td><td>✓</td><td> $\times$ </td><td>✓</td><td>✓</td><td> $\times$ </td></tr><tr><td>Zuo [11]</td><td> $\times$ </td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td> $\times$ </td></tr><tr><td>Kulseng et al. [12]</td><td> $\times$ </td><td>✓</td><td>✓</td><td> $\ddagger$ </td><td>✓</td><td> $\times$ </td><td>✓</td></tr><tr><td>Kim et al. [10]</td><td> $\times$ </td><td> $\times$ </td><td>✓</td><td> $\ddagger$ </td><td>✓</td><td>✓</td><td> $\times$ </td></tr><tr><td>Our Scheme</td><td>✓</td><td> $\times$ </td><td>✓</td><td> $\ddagger$ </td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>✓— Satisfied</td><td> $\times$ — Not Satisfied</td><td> $\ddagger$ — Partially Satisfied</td><td>NA — Not Applicable</td><td></td><td></td><td></td><td></td></tr></table>

Our task is to initialize our protocol, while remaining sound and complete, in such a way that the adversary obtains bogus information. We achieve this by initializing RFID tags with superfluous attribute information and considering queries expressed as a conjunction or disjunction of literals. Formally, given the universe of attributes , we consider a literal to be an element of and query to be any combination of literals in conjunctive or disjunctive form. For example, cloth and food are literals, while cloth∨food is a query stating whether a tag has either attribute cloth or food. We use $Q _ { \mathcal { A } }$ to denote queries of this type over attributes in .

Theorem 2. Let P represent our search protocol and be the universe of tags. If for everyT it holds that prod-info(T) ⊆tag-info(T), then P is sound when restricted to queries $\dot { \boldsymbol { { u } } } \boldsymbol { { Q } } _ { \mathcal { A } }$

Proof. It is easy to prove that for every query $q \in \mathcal { Q } _ { \mathcal { A } }$ it holds that q (prod-info(T)) ⟹ q(tag-info(T)). We then use Theorem 1 to prove soundness of P.

By initializing a tag T with a superset of prod-info(T), we achieve the goal of giving the impression to an attacker that the stock is larger than it actually is. For example, if tag-info( )T = , which represents the absence of meaningful information stored in a tag, then T will respond to any query in $\boldsymbol { Q } _ { \mathcal { A } } .$ Only the server, which stores the correct tag's attribute information tag-info(T), can determine whether a tag actually satisfies a given query. Similar to our remark on the size of the anonymity classes, it is ultimately the analyst who decides how much stock uncertainty is necessary in the system.

## 4.5. Comparison with other protocols

A comparison of the proposed protocol and other secure search protocols [10-12,14,28,30] is displayed in Table 1. Analyses of previous protocols in terms of the properties listed in Table 1 can be found in Refs. [52] and [10]. Next, we compare the results of those analyses with respect to the features of our design.

Firstly, we note that the functional property of attribute search is provided only by our protocol. All other schemes focus purely on identity-based search, which our protocol generalizes. Another distinctive feature of our scheme is that it complies with the EPC standard [4]. The reason being that tags in our protocol are required to generate pseudo-random numbers and calculate a modular squaring. Both these operations can be implemented with less than 1000 gates as shown in Refs.[43,42].

While all protocols in Table 1 protect the anonymity of tags, only Zuo's protocol [11] prevents an adversary from tracing a tag based on the content of a query. However, Zuo's protocol is not EPC compliant. Our protocol, while being EPC compliant, satisfies tag untraceability up to some extent. Tags in our protocol are grouped into anonymity classes, and their privacy protection is proportional to the size of the smallest anonymity class (see Proposition 2). The only property that our scheme fails to satisfy is mutual authentication. As illustrated in Table 1, that is a feature hard to achieve within the constraints of the EPC standard.

Lastly, our protocol has been formally proven correct within a standard Dolev-Yao model, which means it resists replay and impersonation attacks. Moreover, it does not sufer from Denial-of-Service or de-synchronization issues since it does not rely on updated keys.

## 5. Conclusion

Efective inventory management depends on accurate knowledge of current inventory, back-ordered items and when they are expected to be available, estimated demand for carried items, among others. Accurate knowledge of inventory is a significant component since it underestimation or overestimation could respectively result in unnecessary wastage or stock-out situations. In a retail setting, manual inventory-taking is time intensive. Automation of this process is not possible with barcodes since they require individual scanning and this is not feasible as a frequent exercise. Retail stores therefore compromise on knowing the exact inventory through whatever information is available in their database. However, such databases are known to be inaccurate [53]. RFID-based solutions have been successfully used for automated inventory management in retail settings for more than a decade. We considered such a scenario and propose a method that simultaneously identifies the presence of groups of items in the field of the reader.

Specifically, we propose a secure attribute-based lightweight search protocol based on the quadratic residues property. We avoid the use of expensive cryptographic primitives or hash functions, making it possible for use in basic passive RFID tags. The EPS standard is met with the use of quadratic residues and elimination of hash operations. We show that the protocol is secure in an environment with a standard Dolev-Yao adversary, i.e., it resists replay attacks, impersonation, etc. It also provides privacy to individual tags and the stock as a whole, with an increase in computational cost at the server side. In the future, we plan to study how to properly balance such trade-ofs in real-life inventory control systems.

## CRediT authorship contribution statement

Robin Doss: Conceptualization, Methodology, Writing - original draft, Supervision. Rolando Trujillo-Rasua: Software, Formal analysis, Investigation, Writing - review & editing. Selwyn Piramuthu: Conceptualization, Validation, Writing - review & editing.

## Appendix A

```txt
/*
 * Syther specification of the proposed search protocol
 */

usertype String;

const q: String; //represents a query
const attr: String; //represents an attribute

const first, second: String; //to reflect an order on the messages sent by the tags. Otherwise Scyther considers an attack where both Tag roles are played by the same agent

protocol search-protocol(S, R, T1, T2)
{
    hashfunction h;

    role R
    {
    fresh n: Nonce;
    var M1: Nonce;
    var M2: Nonce;

    25
    send_1(R,T1, (q,n)); //Reader sends a query and nonce to tag1
    send_5(R,T2, (q,n)); //Reader sends a query and nonce to tag2
    recv_2(T1,R, {n,M1,k(R,T1), first}pk(R)); // Response from tag1, which reader cannot decrypt
    recv_6(T2,R, {n,M2,k(R,T2), second}pk(R)); // Response from tag2, which reader cannot decrypt
    claim(R,Niagree);

    send_3(R,S, (({n,M1,k(R,T1), first}pk(R), {n,M2,k(R,T2), second}pk(R)), {q, n, h({n,M1,k(R,T1), first}pk(R), {n,M2,k(R,T2), second}pk(R))k(S,R))); //Reader collects all tags answers and forwards them to the server. Encryption is used for authentication and hashing for integrity.
    recv_4(S,R, {q,n,attr}k(S,R)); // Response from the server revealing the attributes of the tag

    claim(R,Niagree);
    }

    role T1
    {
    var N: Nonce;
    fresh m: Nonce;

    recv_1(R,T1, (q,N));
    send_2(T1,R, {N,m,k(R,T1), first}pk(R)); //Tag2 replies if q is correct, which is not modeled in Scyther

    claim(T1,Secret,k(R,T1));
    claim(T1,Secret,m);
    }

    role T2
    {
    var N: Nonce;
    fresh m: Nonce;
    recv_5(R,T2, (q,N));
    send_6(T2,R, {N,m,k(R,T2), second}pk(R)); //Tag2 replies if q is correct, which is not modeled in Scyther

    claim(T2,Secret,k(R,T2));
    claim(T2,Secret,m);
    }

    role S
    {
    var N: Nonce;
    var M1: Nonce;
    var M2: Nonce;

    recv_3(R,S, (({N,M1,k(R,T1), first}pk(R), {N,M2,k(R,T2), second}pk(R)), {q, N, h({N,M1,k(R,T1), first}pk(R), {N,M2,k(R,T2), second}pk(R))k(S,R))); //Server receives request from reader to verify the tag's response. send_4(S,R, {q,N,attr}k(S,R)); // Server replies with the attr associated to the tag. Note that, such association is not modeled by Scyther.

    claim(S,Niagree);
    }
}
```

## References

[1] A. Juels, S. Weiss, Authenticating pervasive devices with human protocols, LNCS 3621 (2005) 293–308.

[2] I. Bose, S. Yan, The green potential of RFID projects: a case-based analysis, IEEE IT Professional 13 (1) (2011) 41–47.

[3] I. Bose, X. Chen, A framework for context sensitive services: a knowledge discovery based approach, Decision Support Systems 48 (1) (2008) 158–168.

[4] EPCGlobal, EPC radio-frequency identity protocols, Class-1 Generation-2 UHF RFID Protocol for Communications at 860 MHz–960 MHz Version 1.2.0, GS1 EPCgloba Inc., 2008.

[5] W. Zhou, RFID and item-level information visibility, European Journal of Operational Research 198 (1) (October 2009) 252–258.

[6] M. Chen, W. Luo, Z. Mo, S. Chen, Y. Fang, An eficient tag search protocol in large scale RFID systems with noisy channel, IEEE/ACM Transactions on Networking 24 (2) (April 2016) 703–716.

[7] X. Liu, B. Xiao, S. Zhang, K. Bu, A. Chan, STEP: a time-eficient tag searching protocol in large RFID systems, IEEE Transactions on Computers 64 (11) (Nov 2015) 3265–3277.

[8] Y. Zheng, M. Li, Fast tag searching protocol for large-scale RFID systems, IEEE/ACM Transactions on Networking 21 (3) (June 2013) 924–934

[9] C. Tan, B. Sheng, Q. Li, Secure and serverless RFID authentication and search protocols, JEEE Transactions on Wireless Communications 7 (4) (April 2008) 1400-1407.

[10] Z. Kim, J. Kim, K. Kim, I. Choi, T. Shon, Untraceable and serverless RFID authen tication and search protocols, 2011 IEEE Ninth International Symposium on Paralle and Distributed Processing with Applications Workshops, 2011, pp. 278–283.

[11] Y. Zuo, Secure and private search protocols for RFID systems, Information Systems Frontiers 12 (5) (2009) 507–519.

[12] L. Kulseng, Z. Yu, Y. Wei, Y. Guan, Lightweight secure search protocols for low-cost RFID systems, 2009 29th IEEE International Conference on Distributed Computing Systems, 2009, pp. 40–48.

[13] C.-F. Lee, H.-Y. Chien, C.-S. Laih, Server-less RFID authentication and searching protocol with enhanced security, International Journal of Communication Systems 25 (2012) 376–385.

[14] S.-I. Huang, S. Shieh, Authentication and secret search mechanisms for RFID-aware wireless sensor networks, International Journal of Security and Networks 5 (1) (2010) 15–25.

[15] L. Chun, J. Hwang, D. Lee, RFID tag search protocol preserving privacy of mobile reader holders, IEICE Electronics Express 08 (2) (2011) 50–56.

[16] S.I. Ahamed, F. Rahman, E. Hoque, F. Kawsar, T. Nakajima, S3PR: secure serverless search protocols for RFID, 2008 International Conference on Information Security and Assurance (isa 2008), April 2008, pp. 187–192.

[17] Y. Zheng, M. Li, Fast tag searching protocol for large-scale RFID systems, IEEE/ACM Transactions On Networking 21 (3) (2013) 924–934.

[18] Y.-J. Huang, C.-C. Yuan, M.-K. Chen, W.-C. Lin, H.-C. Teng, Hardware implementation of RFID mutual authentication protocol. JEEE Transactions on Industrial Electronics 57 (5) (2010) 1573–1582.

[19] L. Fu, X. Shen, L. Zhu, J. Wang, A low-cost UHF RFID tag chip with AES cryptography engine, Security and Communication Networks 7 (2) (2014) 365–375.

[20] A. Moradi, A. Poschmann, S. Ling, C. Paar, H. Wang, Pushing the limits: a very compact and a threshold implementation of AES, in: K.G. Paterson (Ed.), Advances in Cryptology — EUROCRYPT 2011, Springer Berlin Heidelberg, Berlin, Heidelberg, 2011, pp. 69–88.

[21] Y.-P. Liao, C.-M. Hsia, A secure ECC-based RFID authentication scheme integrated with ID-Verifier transfer protocol, Ad Hoc Networks 18 (2014) 133–146.

[22] K.H. Rosen, Elementary Number Theory and its Applications, 4th edition, Addison Wesley, 1999.

[23] H.-Y. Chien. C.-H. Chen, Mutual authentication protocol for RFID conforming to EPC Class 1 Generation 2 Standards, Computer Standards & Interfaces 29 (2) (2007 254-259.

[24] H. Lee, D. Hong, The tag authentication scheme using self-shrinking generator on RFID system, Transactions on Engineering, Computing and Technology 18 (2006) 52–57.

[25] C. Cremers, S. Mauw, Operational semantics of security protocols, Proceedings of the 2003 International Conference on Scenarios: Models. Transformations and Tools, SMTT’03, Springer-Verlag, Berlin, Heidelberg, 2005, pp. 66–89.

[26] D. Duc, K. Kim, Defending RFID authentication protocols against DoS attacks, Computer Communications 34 (3) (Mar 2011) 384–390.

[27] R.D. Pietro, R. Molva, An optimal probabilistic solution for information confinement, privacy and security in RFID systems, Journal of Network and Computer Applications (2010).

[28] T.Y. Won, J.Y. Chun, D.H. Lee, Strong authentication protocol for secure RFID tag search without help of central database, 20o8 JEEE/IFIP International Conference on Embedded and Ubiquitous Computing, December 2008, pp. 153–158.

[29] M. Feldhofer, C. Rechberger, A case against currently used hash functions in RFID protocols, On the Move to Meaningful Internet Systems 2006 — OTM 2006, Lecture Notes in Computer Science, vol, 4277, Nov 2006, pp. 372–381

[30] C.C. Tan, B. Sheng, Q. Li, Serverless search and authentication protocols for RFID, Proceedings of the Fifth Annual IEEE Conference on Pervasive Computing and Communications. 2007.

[31] C. Lv, H. Li, M. Jianfeng, B. Niu, Vulnerability analysis of lightweight secure search protocols for low-cost RFID systems, International Journal for RFID Technology and Applications 4 (1) (2012) 3–12.

[32] E.-J. Yoon, Cryptanalysis of an RFID tag search protocol preserving privacy of mobile reader, International Federation for Information Processing, 2012, pp. 575–580.

[33] J. Lim, S. Kim, H. Oh, K. Donghyun, A designated query protocol for serverless mobile RFID systems with reader and tag privacy, Tsinghua Science and Technology 17 (5) (2012) 521–536.

[34] C. Mtita, M. Laurent, J. Delort, Eficient serverless radio-frequency identification mutual authentication and secure tag search protocols with untrusted readers, IET Information Security (2016) 262–271

[35] Y. Zheng, M. Li, Fast tag searching protocol for large-scale RFID systems, IEEE/ACM Transactions on Networking (2013) 924–934.

[36] M. Chen, W. Luo, Z. Mo, S. Chen, Y. Fang, An eficient tag search protocol in largescale RFID systems with noisy channel, IEEE/ACM Transactions on Networking (2016) 703–716.

[37] L. Batina, J. Guajardo, T. Kerins, N. Mentens, P. Tuyls, I. Verbauwhede, An elliptic curve processor suitable for RFID-tags, Cryptology ePrint Archive, Report 2006/ 227, 2006.

[38] S. Sundaresan, R. Doss, S. Piramuthu, W. Zhou, A robust grouping proof protocol for RFID EPC C1G2 Tags, IEEE Transactions on Information Forensics & Security (2014).

[39] W. Meier, O. Stafelback, The self-shrinking generator, Advances in Cryptology: EUROCRYPT 94, vol. 950, 1994, pp. 205–214

[40] J. Molina-Gil, P. Caballero-Gil, A. Fuster-Sabater, C. Caballero-Gil, Pseudorandom Generator to Strengthen Cooperation in VANETs, EUROCAST 2011, 2012, pp. 365–373.

[41] G. Avoine, M.A. Bingöl, I. Boureanu, S. čapkun, G. Hancke, S. Kardaş, C.H. Kim, C. Lauradoux, B. Martin, J. Munilla, A. Peinado, K.B. Rasmussen, D. Singelée, A. Tchamkerten, R. Trujillo-Rasua, S. Vaudenay, Security of distance-bounding: a survey, ACM Comput. Sury. 51 (5) (2018) 94:1–94:33 September

[42] Y. Chen, J.-S. Chou, H.-M. Sun, A novel mutual authentication scheme based on quadratic residues for RFID systems, Computer Networks 52 (12) (August 2008) 2373-2380.

[43] M. Burmester, B. de Medeiros, R. Motta, Anonymous RFID authentication supporting constant-cost key-lookup against active adversaries, International Journal of Applied Cryptography 1 (2) (2008) 79–90.

[44] B. Alomair, R. Poovendran, Privacy versus scalability in radio frequency identifi cation systems. Computer Communications 33 (18) (2010) 2155–2163

[45] R. Trujillo-Rasua, A. Solanas, Eficient probabilistic communication protocol for the private identification of RFID tags by means of collaborative readers, Computer Networks 55 (15) (2011) 3211–3223

[46] R. Trujillo-Rasua, A. Solanas, P.A. Pérez-Martínez, J. Domingo-Ferrer, Predictive protocol for the scalable identification of RFID tags through collaborative readers, Computers in Industry 63 (6) (2012) 557–573

[47] C. Cremers, The Scyther tool: verification, falsification, and analysis of security protocols, Computer Aided Verification, 20th International Conference, CAV 2008, Princeton, USA, Proc. Lecture Notes in Computer Science, vol. 5123/2008, Springer, 2008, pp. 414–418.

[48] G. Lowe, Breaking and fixing the Needham-Schroeder public-key protocol using FDR. Proceedings of the Second International Workshop on Tools and Algorithms for Construction and Analysis of Systems. TACAS '96. Springer-Verlag. London. UK UK, 1996, pp. 147–166.

[49] S. Mauw, M.A. Reniers, Operational semantics for MSC’96, Computer Networks 31 (17) (1999) 1785–1799.

[50] P. Samarati, Protecting respondents' identities in microdata release, IEEE Trans. on Knowl. and Data Eng. 13 (6) (November 2001) 1010–1027.

[51] G. Avoine, Adversarial model for radio frequency identification, Cryptology ePrint Archive, Report 2005/049, 2005.

[52] S. Sundaresan, R. Doss, S. Piramuthu, W. Zhou, A secure search protocol for low cost passive RFID tags, Computer Networks 122 (2017) 70–82

[53] N. DeHoratius, A. Raman, Inventory record inaccuracy: an empirical analysis, Management Science 54 (4) (2008) 627–641.

Robin Doss is Professor of Information Technology and Deputy Head of the School of Information Technology at Deakin University, In addition, Robin is Director of the Security and Privacy Research in IoT (SPYRIT) lab where he leads a team of researchers and PhD students focused on solving the cyber security challenges presented by IoTenabled smart & critical infrastructures across industry domains

Rolando Trujillo Rasua is Lecturer in Cyber Security at Deakin University. He received the B.Sc. degree in computer science from La Universidad de la Habana, Havana, Cuba, in 2006, and the M.Sc. and Ph.D. degrees in computer engineering from the Universitat Rovira i Virgili, Tarragona, Spain, in 2009 and 2012, respectively. His research interests include Security and privacy of RFID systems, Distance bounding protocols, Location Privacy, Privacy in social networks, Formal methods, and Graph theory.

Selwyn Piramuthu is Professor of Information Systems at the University of Florida. Hi research interests include RFID systems.
