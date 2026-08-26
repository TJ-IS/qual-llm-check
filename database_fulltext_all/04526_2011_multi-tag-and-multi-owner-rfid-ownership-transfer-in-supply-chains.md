---
otero_id: 4526
otero_key: "TH7BBEKU"
title: "Multi-tag and multi-owner RFID ownership transfer in supply chains"
authors: "Gaurav Kapoor; Wei Zhou; Selwyn Piramuthu"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.08.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Multi-tag and multi-owner RFID ownership transfer in supply chains

Gaurav Kapoor <sup>a</sup>, Wei Zhou <sup>b,c</sup>, Selwyn Piramuthu <sup>a,c,</sup>⁎

<sup>a</sup> Information Systems and Operations Management, University of Florida, Gainesville, FL 32611-7169, USA

<sup>b</sup> Information and Operations Management, ESCP Europe, Paris, France

<sup>c</sup> RFID European Lab, Paris, France

## a r t i c l e i n f o

Article history: Received 28 January 2011 Received in revised form 31 May 2011 Accepted 1 August 2011 Available online 16 September 2011

Keywords: RFID Ownership transfer Supply chain

## a b s t r a c t

In any supply chain, there is a high likelihood for individual objects to change ownership at least once in their lifetime. As RFID tags enter the supply chain, these RFID-tagged objects should ideally be able to seamlessly accommodate ownership transfer issues while also accomplishing their primary intended purpose. Physical ownership transfer does not translate to strict ownership transfer in the presence of RFID tags given the wireless nature of communication with these tags. Moreover, whereas existing protocols implicitly assume a single tag that is owned by a single entity, it is not uncommon to encounter scenarios where tag ownership is shared among multiple entities. A dual of this is the case of an object with multiple tags. We consider ownership transfer scenarios for shared ownership transfer and single object with multiple RFID tags. In the multiple-tagged object case, we consider the possibility where objects gain and lose tags over time. We also present a protocol for simultaneous transfer of ownership of multiple tags between owners. Since ownership transfer without a trusted third party (TTP) is dif<sup>fi</sup>cult to achieve, we propose a shared ownership sharing protocol and evaluate its properties.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Ownership transfer issues are common in most supply chains where these issues are somewhat readily accomplished when dealing with physical objects (vs. for example, electronic means). In such cases, ownership transfer could involve the transfer of a physical object from the previous owner to the current owner —i.e., after the ownership transfer process, the current owner is likely (but not necessarily) in physical possession of the object. This process gets complicated with the incorporation of item-level RFID-tags to objects that move through supply chains simply because of the need to transfer ownership both physically and otherwise. For example, a previous owner could possibly continue to remain in (RF) contact with an RFID-tagged object even after the object transfers ownership to a new owner. Therefore, physical ownership transfer does not necessarily translate to complete ownership transfer whereby a previous owner cannot access the object of interest after ownership transfer. Researchers and practitioners have addressed this issue through cryptography.

RFID cryptography has been a very active area for researchers over the past decade (e.g., [19,20]) to address issues such as authentication of RFID-tagged objects. A few of these researchers have also developed and studied RFID ownership transfer protocols over the past several years. A majority of these protocols have been developed for the single-tag single-owner case with and without the presence of a trusted third party (TTP). An example of a TTP could be a bank or any neutral third party that all members involved in a (here, ownership transfer) transaction trust. Since it is common for RFID-tagged objects to be owned by a single owner at any point in time and an object is commonly tagged with a single RFID tag, existing protocols address the dynamic associated with these scenarios.

While not as common as the single-tag single-owner scenario, it is not uncommon for the existence of shared ownership (i.e., an item being owned simultaneously by several owners) as well as objects with multiple RFID tags. Extant RFID ownership transfer literature does not adequately address these scenarios. The purpose of this paper, therefore, is to <sup>fi</sup>ll this gap and propose ownership transfer protocols that are speci<sup>fi</sup>cally meant for multi-tagged or multiowner objects as well as scenarios where multiple tags that are required to be present together simultaneously transfer ownership.

## 1.1. Shared ownership transfer

Over its lifetime, an RFID tag can be associated with one or several owners. Although the single RFID tag ownership scenario is common, it is not uncommon for situations that dictate shared (i.e., multiple) ownership of tags. Examples of shared ownership include Vendor Managed Inventory (VMI) in retail stores [25], and access to a tagged object by multiple entities such as PDA, refrigerator, etc. in a smart home.

Using a secure RFID system for inventory management in the supply chain complicates this process. Since the inventory data is based on information provided by RFID tags, and these tags can only be accessed by valid owners/readers, the authorization/ownership needed to access tags has to be shared by all related owners. In other words, the tag has to be simultaneously visible to multiple entities in the supply chain. Operationalizing such a scenario requires communication protocols (for the tag/reader authentication process) that address this issue. A single-tag single-owner ownership transfer protocol may not necessarily scale well when applied to shared ownership. Moreover, although the number of owners who gain access to any given shared tag may increase, the capabilities of the tag itself with respect to its processing power and memory do not change. This necessitates utilizing only lightweight cryptographic means in developing necessary protocols.

## 1.2. Objects with multiple tags

While security/privacy authentication protocols consider singletagged objects, objects with multiple tags do exist and there is a need to address security/privacy issues in this context. We extend our authentication and ownership transfer protocols for con<sup>fi</sup>gurations where multiple tags may be associated with an object. Depending on the shape of a tagged object, it is likely that embedding just one tag may result in high read rate error. It is common for certain objects (e.g., boxes) to be af<sup>fi</sup>xed with several tags, one on each of its several sides for example, to increase its probability of being scanned by the reader thereby improving its read rate accuracy [24]. Another scenario where multiple-tagged objects may be present is when an object is assembled from several RFID-tagged component parts. Here, although each of the tagged component is distinct they are similar in that they all are a part of this aggregate object of interest.

## 1.3. Simultaneous ownership transfer of multiple RFID tags

Another stream of research related to RFID authentication protocols includes published literature that followed as a direct result of the ‘yoking proof’ [11] protocol, ‘grouping proof’ [21] protocol and their variants. Essentially, these protocols purport to simultaneously authenticate the presence of multiple tags in the <sup>fi</sup>eld of the reader. Such a scenario may include, for instance in the example presented in [11], the necessity of simultaneous presence of a given pharmaceutical item along with its instructions. Although the intention is to authenticate the presence of multiple tags simultaneously, these protocols and a majority of their variants accomplish this in a sequential manner whereby the authentication of the <sup>fi</sup>rst tag is immediately followed by the authentication of the next tag, and so on. Since these authentications are done sequentially as a compact batch, the process is almost similar to comparable simultaneous authentication of these tags.

To our knowledge, extant published literature does not include the scenario where tags that need to be simultaneously present together change ownership together from the same previous owner to the same new owner. Given the need for ‘yoking proof’ protocol and its variants and the need for ownership transfer protocols, it is not hard to envision the need for protocols that incorporate the dynamic present in both these scenarios. We purport to <sup>fi</sup>ll this gap in extant literature by proposing a protocol for verifying the simultaneous presence of multiple tags in the <sup>fi</sup>eld of the reader while ownership transfer involving these tags takes place.

We consider the scenario where two tags that need to be simultaneously present in the <sup>fi</sup>eld of the reader change ownership in the presence of a trusted third party (TTP). We do not consider ownership transfer for the case where a TTP is absent. Without the presence of a TTP, it is extremely dif<sup>fi</sup>cult, if not impossible, to transfer ownership of items between two entities without a common shared secret using symmetric key cryptography. In this case, the protocol becomes an ownership sharing one and not an ownership transfer protocol since the previous owner may continue to maintain RF access to the tag. Ownership transfer without a TTP through wireless means using symmetric key cryptography is dif<sup>fi</sup>cult since any secret information shared between previous and current owners who do not share any secret can be readily picked up by an adversary in the vicinity. We do not consider the use of public key cryptography, which could allow for ownership transfer without a TTP, in this paper. This is left as an exercise for a future paper.

This paper is organized as follows: the next section provides a brief overview of some related protocols. The proposed Shared ownership transfer protocol is presented in Section 3. A shared ownership sharing protocol is presented in Section 4. Objects with multiple tags are considered in Section 5. Speci<sup>fi</sup>cally, protocols for inclusion/exclusion of RFID tagged components in an object of interest as well as for shared ownership transfer are considered in Section 5. Protocol for simultaneous ownership transfer of multiple tags is presented in Section 6. Section 7 concludes the paper with a brief discussion.

## 2. Related work

Over the past <sup>fi</sup>ve years, several ownership transfer protocols for RFID tags have been proposed and studied (e.g., [1,4,10,13,22,28]). Most of these ownership transfer protocols deal with the common single tag — single owner scenario. A majority of these have been found to have vulnerabilities that can readily be taken advantage of by a resourceful active adversary (e.g., [13,14]). We <sup>fi</sup>rst present and evaluate a few recently proposed ownership transfer protocols and identify some of their vulnerabilities.

## 2.1. Notation

The following notations are used throughout the paper:

• $N _ { i } { \mathrm { : } }$ random l-bit nonce generated for entity i

$I D _ { R } , I D _ { T } .$ : reader and tag identi<sup>fi</sup>er

$R _ { i } , T _ { i }$ reader/owner i, Tag i

• $\therefore k _ { a } , k _ { a } ^ { \prime } \colon$ authentication keys

$s , s ^ { \prime } , s _ { i } \colon$ shared keys between entities

• $F _ { u } \mathrm { : }$ update <sup>fl</sup>ag

• V: response value

• $h , g , H , G \colon$ hash functions $- \{ 0 , 1 \} ^ { * }  \{ 0 , 1 \} ^ { l }$

$h _ { k } \mathrm { : }$ keyed (with key k) hash function

$f _ { k } ^ { \prime } , f _ { k } \colon$ keyed (with key k) encryption function

$E _ { x } ( m ) ;$ : encrypt message m using object x's public key

$D _ { x } ( m )$ : decrypt message m using object x's public key

$S _ { x } ( m ) ;$ : signature using message m and x's private key

• Cert : Tag 's ownership certi<sup>fi</sup>cate

• EPC: Electronic Product Code

• CRC: Cyclic redundancy check

• TID: Transaction identi<sup>fi</sup>er

• CID: Current identi<sup>fi</sup>er

• HID: Hashed CID (H(CID))

• SN: Serial number

• Sign (m): Signature of message m by entity x

• t : shared secret between tag and TTP

• $r _ { i \cdot }$ shared secret between reader $R _ { i }$ and TTP

## 2.2. Protocol of Chen et al.

The protocol of Chen et al. [2] comprises three main phases as given in Figs. 1, 2, and 3.

During the <sup>fi</sup>rst phase (Fig. 1), the previous owner passes on important information about the tag (here, Tag i) – the certi<sup>fi</sup>cate of ownership (Cert ) – to the new owner. The second phase (Fig. 2) is for mutual authentication between the tag and server. Since the <sup>fi</sup>rst and third phases can operate together to accomplish ownership transfer, the purpose of the second phase (mutual authentication phase) is not clear from an ownership transfer perspective. The third phase (Fig. 3) completes ownership transfer by generating a new certi<sup>fi</sup>cate (Cert′<sub>i</sub>) and passing the same to the new owner and the tag.

![](/api/attachments/TH7BBEKU/fulltext/images/33f5a9d50c38ee860416c69938d8eb0c6acd7d8add2e0dc066c85238033981a4.jpg)  
Fig. 1. Ownership transfer — initial phase (Chen et al.).

The mutual authentication phase (Fig. 2) is vulnerable to replay attack from an adversary with the capability to capture, store, and replay previous messages. This can be accomplished as follows: the adversary can capture the <sup>fi</sup>rst message from Reader to Tag (i.e., request, $r _ { R } , C R C ( N _ { i } \oplus r _ { R } ) )$ and repeatedly replay it to the tag while blocking the response from the Tag $( \mathrm { i } . \mathrm { e } . , r _ { T } , Y , Z )$ from reaching the Reader. The Tag repeatedly updates its key (k ) whereas the Reader does not have the opportunity to keep in sync. This leads to de-synchronization between the Tag and the Reader and these two will not be able to communicate with each other again, thus leading to Denial of Service from Tag to Reader and vice versa.

The Chen et al. protocol has at least one other vulnerability, which is serious. This vulnerability is present in the third (i.e., ownership transfer) phase. An active adversary can block the message from the new owner to the server (i.e., $I D _ { 1 } , I D _ { 2 } , S _ { 2 } ( I D _ { 1 } , I D _ { 2 } ) , S _ { 1 } ( C e r t _ { i } , I D _ { 2 } )$ , Cert<sub>i</sub>) and retrieve Cert<sub>i</sub>, which is in cleartext. This certi<sup>fi</sup>cate can then be used to provide ownership of the tag to anyone, which includes the adversary. The adversary accomplishes transfer of ownership by knowing Cert and following the <sup>fi</sup>rst phase of this protocol (Fig. 1).

## 2.3. Protocol of Lin et al.

The protocol of Lin et al. [17] purportedly accomplishes ownership transfer in one short phase (Fig. 4).

The structure of this protocol lends itself to attacks by an adversary to result in DoS (Denial of Service) attack. The adversary can block the message from tag to reader, modify it, and then send it to the reader. Specifically, the adversary can modify ΔTID to some large value by XORing this with some large N value. I.e., send N ΔTID $H ( H _ { C I D } ( S N ) \oplus r _ { T } )$

instead of ΔTID⊕H(H (SN)⊕r ). Now, after observing this huge ΔTID value, the reader would be forced to look for the corresponding CID (and other) values in the received message but would fail in its attempts. Another vulnerability is in the message from the reader to the tag. Both $r _ { R }$ and $r _ { R } \oplus H ( H _ { C I D } ( S N ) \oplus ( r _ { T } + 1 ) )$ can be modi<sup>fi</sup>ed by inserting some δ value as follows: instead of $r _ { R } ,$ the adversary can block this entire message from reader to tag and send δ⊕ $r _ { R } \oplus H ( H _ { C I D } ( S N ) \oplus ( r _ { T } + 1 ) )$ $\delta \oplus r _ { R } , H ( r _ { R } \oplus C I D \oplus T I D )$ instead. Now, the tag would use the new $r _ { R } \oplus \delta$ to update its CID value while at the same time retrieving the new TID from $( T I D \oplus r _ { R } \oplus \delta \oplus \delta )$ as (TID⊕δ). This new CID value will be different from the one at the reader's side, therefore leading to de-synchronization between reader and tag. The reader and tag will never be able to communicate with each other.

## 2.4. Protocol of Song and Mitchell

Ownership transfer in Song and Mitchell [23] is accomplished in several steps as follows: (1) the previous owner updates tag secrets for privacy and forward/backward traceability reasons, (2) the previous owner shares these tag secrets with the new owner through a secure channel, and (3) the new owner updates the secrets to prevent the previous owner from gaining (RF) access to the tag. Step (1) is fairly straight-forward and is readily accomplished without any issues since the tag and previous owner share those secrets, which are not known to any other entity. The paper includes a protocol that accomplishes step (1). Step (2) is also readily accomplished assuming the presence of a secure channel between the previous and new owners. The paper does not provide a protocol to accomplish this step, probably due to the assumption that this occurs through a secure channel and the possibility of the absence of encrypting any message passed between the previous and current owners. Unlike the <sup>fi</sup>rst two steps, Step (3) is vulnerable to attacks by an adversary, who could very well be the previous owner. Step (3) is carried out by a secret update protocol (Fig. 5).

The authors mention the following in the Paragraph before Section 6.2.2.: “If P2 completes successfully (and the old owner does not eavesdrop on the messages), S and T share new secrets known only them, and the old owner is no longer able to identify or trace T". Here, P2 is the ownership transfer protocol (Fig. 5), S and T are the new owner and tag respectively. Clearly, the previous owner not having the capability to eavesdrop on any communication is an invalid assumption. If this assumption were valid, why not take it to the extreme and assume that any pair of sender–recipient operates in a sterile environment where no one but the intended recipient receives the intended message without any corruption? Such an assumption would obviate encrypting any of the messages sent between any two parties and the need for such ownership transfer protocols. Even assuming an honest previous owner, this is only an ownership sharing (i.e., not transfer) protocol.

![](/api/attachments/TH7BBEKU/fulltext/images/500aa0e8736afead2151862ac9d4512ed70e525eb3e4ed8250cdc22b099f3bd4.jpg)  
Fig. 2. Ownership transfer — mutual authentication phase (Chen et al.).

![](/api/attachments/TH7BBEKU/fulltext/images/6e33e18201a16b23ee9c8792323be5add5a2825f2819141c6b11a0e091cd5be3.jpg)  
Fig. 3. Ownership transfer phase (Chen et al.).

Since the previous owner knows the tag's secrets, it can block the message from the new owner to the tag and send the appropriate $f _ { k } ( r _ { R } | | x )$ to the new owner as if this message is from the tag. The new owner would validate this to be true and update its s,k, and x values. The previous owner can also modify $r _ { R } , g _ { k } ( x | | r _ { R } ) \oplus ( s | | k ^ { \prime } | | c ^ { \prime } )$ with different $k ^ { \prime }$ and $c ^ { \prime }$ values and send it to the tag. The tag would now update its c and k values to those sent by the previous owner. The new owner and tag will be de-synchronized and will never be able to communicate with each other.

An adversary, who need not be the previous owner, can also accomplish de-synchronization between tag and new owner as follows: the adversary can block the message from the tag to the new owner (Fig. 5). Now, the tag has already updated its c and k values while the new owner has not. Since the new owner does not know whether the tag received the message it just sent unless it hears from the tag, it will not know what to send next to begin communication with the tag. It has two options: change $r _ { R }$ and resend $r _ { \mathit { R } } , g _ { \mathit { k } } ( x | | r _ { \mathit { R } } ) \oplus ( s | | k ^ { \prime } | | c ^ { \prime } ) \ -$ the tag will not be able to decrypt this message due to different k-value; change r and the encryption key to $k ^ { ' }$ in which case s may not be recognized by the tag (since s and k are related through $k = h ( s ) )$ .

## 2.5. Protocol of Ilic, Michahelles, and Fleisch

Ilic, Michahelles, and Fleisch [9] propose a ‘dual ownership model,’ where they consider simultaneous ownership in the physical and electronic worlds. Fig. 6 illustrates the essence of this protocol, which is operationalized using three entities: a back-end server, a reader, and tags.

The reader (here, new owner) initiates the proof of ownership protocol with a request to the tag, which responds by sending it's ID and secret key k values in cleartext. The new owner then uses its private key to digitally sign these values and sends it to the back-end server. The back-end server veri<sup>fi</sup>es the ID,k values and then generates a new key (k′). It sends this key to the new owner after encrypting it with the new owner's public key. The new owner then updates the tag using this new key.

Unless the authors intended the messages between tag and new owner, this protocol is vulnerable on several counts. The ID of the tag as well as its keys (k,k′) are sent in the open in cleartext. This is a serious vulnerability since knowing these, the tag can readily be tracked/traced. Moreover, even worse, the tag can easily be cloned using this information.

![](/api/attachments/TH7BBEKU/fulltext/images/caff652057ed99e0a9779f174f9b69faf75ad3e246acafd639562734a4e55857.jpg)  
Fig. 4. Ownership transfer protocol of Lin et al.

![](/api/attachments/TH7BBEKU/fulltext/images/e064534397bb8eb3faa5dafc3ecf75c4e8cc84f005f22f0426825ee1d85430ba.jpg)  
Fig. 5. Ownership transfer protocol of Song and Mitchell.

## 3. The shared ownership transfer protocol

From the perspective of key management, shared ownership transfer can be accomplished either by using a single shared key among the tag and all its owners or by using a different key for each tag-owner pair. The latter quickly becomes infeasible due to limitations in tag storage space. The former is feasible in this respect with some minor issues. For example, what if one or few of the owners decide or are forced to give up ownership? This necessitates generating a fresh key for all current owners. How does one accomplish this when the number of owners is dynamic over a tag's lifetime? This is an issue since the owners of a tag have a shared key, what happens when the previous owners of a tag listen in on communication among current owners and attempt to retrieve the new key? We are in the process of exploring these issues, and only present the basic protocol in this paper. We <sup>fi</sup>rst present our shared ownership transfer protocol with a trusted third party and then extend this to the one without a trusted third party.

As in existing ownership transfer protocols, we assume that two sets of entities are interested in transferring ownership of an object that is RFID-tagged. Fig. 7 illustrates this scenario where the number of owners of a tag can vary across time, which increases from left to right in this Figure. Here, the number of owners (i.e., 1m,2m,⋯,nm) could all be different. Please note that in Fig. 7, 1m, 2m, ⋯, nm are just nominal labels and 2m is not twice 1m. The trusted third parties taking part in any ownership transfer process including $T T P _ { 1 } ,$ $T T P _ { 2 } , \cdots , T T P _ { n - 1 }$ need not necessarily be the same. I.e., some of them may be the same while some others are different — the scenario being modeled is <sup>fl</sup>exible in this regard. The ownership transfer process proceeds from left to right over time across (possibly) different sets of owners as illustrated in Fig. 7. The dashed lines between any two entities (i.e., TTP, Tag, Owner) represent wireless communication between them.

For the remainder of the paper, to prevent DoS attacks, the recipient of a freshly generated nonce sent in cleartext (e.g., $N _ { P }$ from TTP to

<table><tr><td>Server(secret: ID, k)</td><td></td><td rowspan="2">R</td><td rowspan="2">requestID, k←→</td><td>Tag(secret: ID, k)</td></tr><tr><td>Verify ID, k, Rk&#x27; ← {0, 1}1</td><td>SignR(ID, k)←→k&#x27;</td><td></td></tr></table>

Fig. 6. Proof of ownership protocol of Ilic et al.

Tag in Fig. 8) accepts it only if this nonce is non-null. We also assume that a message originator waits for a response for a pre-speci<sup>fi</sup>ed amount of time and non-response triggers a fresh message. From hereon, all messages passed between any two entities are assumed to occur through wireless means (except between the two owners as represented in Fig. 11). The rationale for this is that most of the communication with RFID tags (have to) occur through wireless means and a few of those between <sup>fi</sup>xed entities (e.g., reader, backend server) may be constrained to occur through secure wired links. For the shared ownership transfer protocol with a TTP (Section 3) and shared ownership sharing protocol without TTP (Section 4), we assume that all involved owners are simultaneously present or are reachable from the tag. We <sup>fi</sup>rst present a shared ownership transfer protocol with a trusted third party followed by a shared ownership sharing protocol without a trusted third party. Given limitations in existing technology and other resource constraints, it is rather chal lenging to develop a shared ownership transfer protocol in the absence of a trusted third party.

## 3.1. Shared ownership transfer protocol with a TTP

We consider a scenario with the following parties, namely Tag $T _ { i } ,$ TTP, current owner $R _ { 1 }$ (or group $R _ { 1 1 } , R _ { 1 2 } , . . . , R _ { 1 M } )$ and new owner $R _ { 2 }$ (or group $R _ { 2 1 } , R _ { 2 2 } , . . . , R _ { 2 N } )$ . The proposed shared ownership protocol (Fig. 8) in the presence of a TTP is as follows:

Step 1.1 Upon receiving an ownership transfer request, the TTP generates a new key $s _ { 2 } .$ It then generates a fresh nonce $N _ { P } ,$ and sends $f ^ { \prime }$ encrypted with $( N _ { P } \oplus t _ { i } \oplus s _ { 1 } )$ , where $s _ { 1 }$ is the tag's current key. This authenticates the TTP to the tag, which up dates $s _ { 1 } \ t _ { 0 } s _ { 2 } .$

Step 1.2 The tag acknowledges by generating and sending a fresh nonce $N _ { T }$

Repeat the following steps (i.e., 2, 3.1, 3.2, 4.1, 4.2) once for each owner in the two (i.e., new owners and previous owners) groups:

Step 2 The TTP informs current owners $\left( R _ { 1 1 } \cdots R _ { 1 M } \right)$ that their privileges on this tag are being revoked. It sends a simple revoke message and a keyed cryptographic function, $f _ { r _ { 1 i } } ( s _ { 1 } )$ to each of the M current owners (i=1..M).

Step 3.1 Next the TTP grants the new owners $\left( R _ { 2 1 } \cdots R _ { 2 N } \right)$ full permissions along with any delegation privileges for the tag. A grant message is issued, along with a freshly generated nonce N′ and a function encrypted with the key $( r _ { 2 i } )$ shared between new owner and TTP. The function contains the new key (s<sub>2</sub>).

Step 3.2 The new owners send an acknowledgment using a one-way hash with the new key value.

Step 4.1 The new owners then generate a fresh nonce $N _ { R _ { 7 } }$ , and establish contact with the tag by sending $N _ { R _ { 2 } }$ and $N _ { R _ { 2 } }$ in an encrypted function (using $s _ { 2 }$ as the encryption key).

Step 4.2 The tag acknowledges with a one-way hash of a freshly generated nonce $N _ { T } ^ { ' }$ along with $N _ { R _ { 2 } }$ and $s _ { 2 } .$

## 3.2. Authentication

Now that all involved parties know the shared secret (s ) for the tag of interest, we introduce a protocol that can be used for mutual authentication of every member of $R _ { 2 }$ and tag.

The authentication handshake works as follows:

Step 1 The $i ^ { t h }$ new owner queries the tag with $N _ { R _ { 2 i } }$

Step 2 The tag responds with a freshly generated nonce $N _ { T }$ and a keyed (with $N _ { T } \oplus s _ { 2 } )$ hash of $N _ { R _ { 7 i } }$ . Only the tag and its new owners $( R _ { 2 i } ,$ where $i { = } 1 . . N )$ share $s _ { 2 } .$ This authenticates tag to the new owners.

![](/api/attachments/TH7BBEKU/fulltext/images/d7b2aee79053731ce3e736e23f228a9993d4eab7f3fb5b01f3fe59574e17ef4c.jpg)  
Fig. 7. Shared ownership transfer with TTP.

Step 3 The message from owner i to tag now consists of a freshly generated nonce $N _ { R _ { 2 i } } ^ { \prime }$ . This message is encrypted using both the shared key $s _ { 2 }$ between tag and new owners, and the nonce generated by the tag in the previous message $N _ { T } .$ This authenticates owner i to the tag.

Step 4 To acknowledge receipt of the message in Step 3, the tag sends $H _ { s _ { 2 } } ( N _ { R _ { 2 i } } ^ { \prime } )$ to owner i. If owner i does not receive this message within a pre-determined amount of time, the process is repeated from Step 1 (Fig. 9).

## 3.3. Security analysis

We omit detailed security analysis of this protocol since its structure is similar to the one-tag one-reader ownership transfer protocol presented in [13]. In general, the security design of the protocols should not impede normal operations and should prevent a malicious adversary from retrieving or inferring any information. We <sup>fi</sup>rst explain the rationale for some communications (and subsets thereof) and then a sketch of the analysis.

## 1. TTP-to-Tag: $N _ { P } , f _ { \left( N _ { P } \oplus t _ { i } \oplus s _ { 1 } \right) } ^ { \prime } \left( s _ { 2 } \right)$

The nonce $N _ { P }$ provides the randomness necessary to prevent a replay attack (wherein an adversary will just replay a message or some subset thereof). Without the use of nonces, the message sent would now be just $f _ { ( t _ { i } \oplus s _ { 1 } ) } ^ { \prime } \left( s _ { 2 } \right)$ , which would elicit the same response from the tag every time (i.e. $H _ { ( t _ { i } \oplus s _ { 1 } ) } { \big ( } s _ { 2 } { \big ) } )$ , and then an adversary could easily track the tag. Also, we use $N _ { P } \oplus t _ { i } \oplus s _ { 1 }$ as the key for the function f′ because 1) it authenticates (to Tag<sub>i</sub>) the message as coming from TTP, as the key t is only known to these two entities, and 2) not using $N _ { P }$ in the key can possibly (although it is highly unlikely) lead to denial of service (DoS). To see this, assume that the adversary intercepts the message $N _ { P } { , } f _ { ( t _ { i } \oplus s _ { 1 } ) } ^ { \prime }$ (s ), and sends a different nonce $N _ { P } ^ { \prime }$ along with the message. The tag, believing it is from a valid TTP due to the presence of $t _ { i } ,$ would then respond with $N _ { T } , ~ H _ { ( t _ { i } \oplus N _ { T } ) } ( s _ { 2 } \oplus N _ { P } ^ { \prime } )$ . The TTP (having sent $N _ { P }$ and not $N _ { P } ^ { \prime } )$ will now discard this and would have to restart the procedure. An adversary could keep doing this to deny the operation.

## 2. Tag-to-TTP: $N _ { T } , H _ { ( t _ { i } \oplus N _ { T } ) } ( s _ { 2 } \oplus N _ { P } )$

Here, the keyed hash function <sup>fi</sup>rst helps authenticate to the TTP that the message is from Tag , due to the presence of t in the key used. The hash value contains both the new key $s _ { 2 }$ and the nonce $N _ { P }$ to convey that the key $s _ { 2 }$ has been received by Tag well as to prevent the problem described above. Also, suppose an adversary intercepts the message and changes the nonce $N _ { T }$ (sent in the clear) to $N ^ { \prime } { } _ { T }$ In that case the hash key and (therefore the computation of the hash value by the TTP) changes, and so the TTP will discard the message. Thus, the message integrity will be preserved. In such a scenario, the TTP will re-initiate the procedure. Although this too can potentially be a way for a DoS attack, there is a negligible probability of this happening, as the adversary cannot track the tag or any of its messages.

![](/api/attachments/TH7BBEKU/fulltext/images/1cc97e55a241dd902302bf4729489aaa20533a4e043e42f21fc7b471e78a97d3.jpg)  
Fig. 8. Shared ownership transfer protocol with TTP.

![](/api/attachments/TH7BBEKU/fulltext/images/a1eb61ce2a2ce1400cc8de302b242a79035b3018c31f288452f856f2115f7e7e.jpg)  
Fig. 9. The authentication handshake.

The same ideas are applied in each communication between the TTP and owners, and between owners and tags. We now present how the protocol meets the objectives of a general RFID security analysis.

1. Secrecy, Data Integrity and Authenticity: The communications are based on secret keys and keyed cryptographic functions with little or no data sent “in the clear”. To intercept and read any message an adversary must know the secret keys. Using hash functions helps preserve the message integrity. In addition, since there are some keys known only to entity pairs (as described above), most communication can be authenticated as well.

2. DoS and Synchronization problem: Consider a situation where an adversary blocks a message. Since we rely on acknowledgments for the key change and <sup>fi</sup>rst post key change communique from new owner to tag, blocking any message creates no breach in the system. In addition, we do not face the de-synchronization problem (i.e. that the tag is unreachable because it has a different key). At least one entity (be it a previous owner $R _ { 1 } ,$ a new owner $R _ { 2 }$ or the TTP) can always communicate with the tag. Suppose the adversary blocks message (1.1): a member of R can still reach the tag, with key $s _ { 1 } .$ . Suppose the adversary blocks message (1.2): The TTP is waiting for an acknowledgment and will take remedial action. Of course, to commit such attacks, an adversary must know all the parties involved, the sequencing of the messages, and the timing of the messages.

3. Forward Security:Forward security refers to the scenario where the current key of a tag is known to the adversary, and can be used to extract previous messages (assuming that some past conversations are recorded by the adversary). Let's say the adversary somehow knows the current key s . The tag always communicates using a keyed hash function. The adversary cannot use the key to decode any of the tag's previous messages because the one-way hash function H is considered computationally un-invertible. I.e., access to the hash digest table is necessary for any lookups. Moreover, previously used keys cannot be used by the adversary to decipher/recreate any previously sent messages.

![](/api/attachments/TH7BBEKU/fulltext/images/ac6e78df8db59ae335b10eefe989f27d74c1f195d77c0be69fd556064489131d.jpg)  
Fig. 11. Shared ownership sharing without TTP: Initialization.

## 4. Shared ownership sharing protocol without TTP

The shared ownership sharing protocol without a TTP is similar to the one with TTP (Section 1) except for the absence of the TTP. Although this protocol is more secure than those in existing literature, it does not transfer ownership in the strict sense since all previous owners can still access the tag. However, since the previous key is not known to the new owner, it is an improvement over [21].

## 4.1. The proposed protocol

The scenario considered comprises the following parties, namely Tag, current owner group $R _ { 1 1 } , R _ { 1 2 } , . . . , R _ { 1 N }$ and new owner group $R _ { 2 1 } ,$ $R _ { 2 2 } , . . . , R _ { 2 N } .$ . We assume that each owner group has a “central author-$\mathrm { i t y " }$ who is responsible for initiating communication and later propagating changes in keys/access to the other members in the group. I.e., $R _ { 1 1 }$ could be such a central authority for group 1, and $R _ { 2 1 }$ for group 2. Thus, the ownership transfer steps take place between $R _ { 1 1 }$ and $R _ { 2 1 }$ in the Initialization phase, and between $R _ { 2 1 }$ and Tag in the Key Change phase. These changes are passed on to the other members of the related owner group. Fig. 10 illustrates this scenario from a high-level perspective, with the time scale represented from left to right.

Once the request for transfer of ownership has been invoked and approved, the procedure for the actual transfer of ownership works as follows:

Step 1 Upon receiving an ownership transfer request, $R _ { 1 }$ generates a fresh nonce $N _ { R _ { 1 1 } } ,$ XORs the key shared with the tag (s ) with this nonce and sends it encrypted to the tag and on a secure channel to $R _ { 2 } .$ . This is the “initialization” phase as depicted in Fig. 11.

Step 2.1 Upon receiving $N _ { R _ { 1 } }$ ⊕s from $R _ { 1 } .$ , the tag generates a fresh nonce $N _ { T } ,$ and sends the nonce XORed with the key $s _ { 1 }$ to R (Fig. 12). Now both T and $R _ { 2 }$ know N, (where $N = N _ { R _ { 1 1 } } \oplus N _ { T } )$ As another measure or layer to preserve forward security, $R _ { 2 }$ is not allowed to know $s _ { 1 } .$

![](/api/attachments/TH7BBEKU/fulltext/images/5614dfc638ac76f04cab948e30dc3ecb865da27fd8d85c246b8e2214961f36fb.jpg)  
Fig. 10. Shared ownership sharing without TTP.

<table><tr><td rowspan="3">Tag $s_1, s_2$ </td><td> $f_{N'}(N' \oplus s_2)$ </td><td colspan="3"> $s_2$ </td></tr><tr><td> $H_{s_2}(N' \oplus s_2)$ </td><td rowspan="2"> $R_{21}$ </td><td rowspan="2"> $\cdots$ </td><td rowspan="2"> $R_{2N}$ </td></tr><tr><td> $f_{s_2}(N' \oplus s_2)$ </td></tr></table>

Fig. 12. Shared ownership sharing without TTP: key change.

Step 2.2 The tag now randomly <sup>fl</sup>ips one bit in $N ,$ creating $N _ { \ast } ^ { \prime }$ and generates another fresh nonce $N _ { T } ^ { \prime } .$ . It sends N<sub>T</sub><sup>′</sup> and an encrypted function containing $N ^ { \prime } \oplus N _ { T } ^ { \prime }$ using $N ^ { \prime } \oplus N _ { T } ^ { \prime }$ as the key and a similarly keyed hash function with the same values to $R _ { 2 } .$

Step 3.1 Knowing $N , R _ { 2 }$ uses a brute force technique to determine $N ^ { \prime }$ so as to decrypt the value sent in f. Since $R _ { 2 }$ knows that N′ is really just N with only one <sup>fl</sup>ipped bit, this process is feasible and $R _ { 2 }$ is assumed to possess the necessary computational resources to accomplish this very quickly. $R _ { 2 }$ veri<sup>fi</sup>es the solution obtained using the hashed value.

Step 3.2 The new owner $R _ { 2 }$ now generates and sends a new key to the tag by XORing and encrypting it with N<sup>'</sup>. This step is repeated after a pre-determined time period until step 4 happens.

Step 4 The tag acknowledges receipt of the new key using a hash function, keyed with the new key $s _ { 2 } .$

Step 5 To acknowledge receipt of message in Step 4, R sends $f _ { s _ { 2 } }$ $\left( N ^ { \prime } \oplus s _ { 2 } \right)$ to the tag. If the tag does not receive this within a pre-determined amount of time, the process is repeated beginning with Step 1.

## 4.2. Security analysis

We evaluate the ownership transfer protocol without TTP. It is very similar to the analysis described in Section 3.3, with some notable additions.

1. Indistinguishability/Tracking:Using a freshly generated nonce with almost every message in the protocol, it is dif<sup>fi</sup>cult to track the tag. Assume that an adversary pretends to be a genuine reader. He sends out a query, and receives the hash of a message back. Next time he sends a query, along with a freshly generated nonce, he receives a different message, so he cannot track the tag. Of course, with multiple tags in an area, tracking a speci<sup>fi</sup>c tag without keys is extremely dif<sup>fi</sup>cult.

2. Passive replay:The freshly generated nonce creates an element of randomness. However, passive replay is possible in the absence of a secure channel to do the initialization.

## 5. Protocols for multi-tagged object

## 5.1. Inclusion/exclusion of Tag(s)

It is not uncommon to encounter objects with several RFID tags. However, the tags on these objects are generally mobile and move from or to (or, both) the object. An example scenario that illustrates this includes a primary object (e.g., car chassis) with several attached parts (e.g., car door, wheels) each with its own RFID tag. In such scenarios, both the number of tags as well as the individual tags themselves may vary over time. I.e., when a tire is replaced, the new tire may come with its own embedded RFID tag; when the owner decides to add a GPS system, it may come with its own RFID tag; when the spare tire is removed from the car, there would be one less RFID tag on the car. To our knowledge, no existing RFID authentication protocol addresses this scenario, and there is a clear need for such protocols.

The proposed protocol (Fig. 13) can be used for inclusion and exclusion of tags in a multiple-tagged object. We assume that a TTP mediates between the reader and tags in accomplishing this change in shared secret key. The actors involved in this protocol include the reader, the TTP, and every tag that is a part of the object of interest either before or after components (tags) were added or removed.

We assume that every component (tag) that is a part of the object of interest share a common secret key (s ). This key is updated every time the object of interest experiences addition or removal of a component or group of components. The primary purpose here is to ensure that the updated key is known only to the reader, the TTP, and the tags that are currently attached to the object. The components (tags) that were dropped from this object should not have knowledge of this new shared key. This is a single round protocol that has three main “loops". This protocol is repeated for each tag that is associated with the object including those that are present on the object and those that were just removed from the object.

The <sup>fi</sup>rst loop between the TTP and tag begins the shared key change process when the TTP generates a new shared secret for the tags and distributes this secret to each tag currently attached to the object. The TTP waits for response from the tag for a predetermined amount of time. If the TTP does not hear back from the tag during this time, it generates a fresh nonce $\left( N _ { P } \right)$ and the forward part of the loop is repeated. This process continues until this loop is completed. After completion of the <sup>fi</sup>rst loop, the tag attached to the object knows the new shared secret $\left( s _ { c + 1 } \right)$ . For those tags that are no longer a part of the object of interest, the same process is followed but with $S _ { C + 1 }$ set to some predetermined string (e.g., null bits). The second loop is between the TTP and the reader. Here, the TTP shares the new shared secret key with the reader. This process is repeated for all relevant readers. The <sup>fi</sup>rst term $\bigl ( N _ { P } , f _ { ( r _ { i } \oplus s _ { c } \oplus N _ { P } ) } \bigl ( s _ { c + 1 } \bigr ) \bigr )$ is used to transfer the new shared key. The second term $\bar { ( } f _ { ( r _ { i } \oplus s _ { c } ) } ( I D _ { t _ { i } } \oplus s _ { c + 1 } ) )$ conveys the unique ID value of the tag to the reader so that the reader can associate the ID value with its corresponding shared secret key value. This process is repeated until the TTP hears back from the reader. Once ID and $S _ { C + 1 }$ values are retrieved, the reader veri<sup>fi</sup>es the new common shared secret directly with the tag in the <sup>fi</sup>nal loop. The third loop, initiated by the reader, is between the reader and the tag and it mutually authenticates the tag using the new key $\big ( \mathrm { i } . \mathsf { e } . , s _ { c + 1 } \big ) .$ . The third loop is nested in the second loop. I.e., the reader responds to the TTP only after successful completion of the third loop.

## 5.2. Security analysis

Analyzing the security of protocols used in RFID tags has its issues since a majority of such protocols depend on the hardness of exhaustive enumeration. For example, the HB+ protocol [12] was proved to be secure but was later broken with a simple man-in-the-middle attack in [5] and others (e.g., [15]). Several methods have been proposed to analyze the security properties of cryptographic protocols over the years and these methods have their own issues (e.g., [3,16]).

![](/api/attachments/TH7BBEKU/fulltext/images/c143872206f7d235ca0898410542a03b001448d1b369a794420d0956acc35469.jpg)  
Fig. 13. Tag inclusion/exclusion protocol.

```txt
G1 TTP|≡Ri|~#(NR)
G2 TTP|≡Ri|~#(f_{r_i ⊕ N_R ⊕ N_P}(S_{C+1}))
G3 R_i|≡TTP|~#(NP)
G4 R_i|≡TTP|~#(f_{r_i ⊕ S_c ⊕ N_P}(S_{C+1}))
G5 R_i|≡TTP|~#(f_{r_i ⊕ S_c ⊕ N_P}(ID_{t_j} ⊕ S_{C+1}))
G6 T_j|≡TTP|~#(NP)
G7 T_j|≡TTP|~#(f_{t_j ⊕ S_c ⊕ N_P}(S_{C+1}))
G8 TTP|≡T_j|~#(NT)
G9 TTP|≡T_j|~#(f_{s_{c+1} ⊕ N_T ⊕ N_P}(S_{C+1}))
G10 T_j|≡R_i|~#(N'R)
G11 T_j|≡R_i|~#(f_{s_{c+1} ⊕ N_R'}(S_{C+1}))
G12 R_i|≡T_j|~#(NT)
G13 R_i|≡T_j|~#(f_{s_{c+1} ⊕ N_R'}(NT))
G14 TTP|≡TTP \xleftrightarrow{S_{c+1}} R_i
G15 R_i|≡R_i \xleftrightarrow{S_{c+1}} TTP
G16 TTP|≡T_j \xleftrightarrow{S_{c+1}} TTP
```

GNY logic [7] has been used to check for security issues in a majority of RFID protocols (e.g., [6,8,18,26,27]). As far as we can tell from our experience dealing with related publications, there are very few papers (among those dealing with RFID authentication protocols) that use other methods to prove security of RFID authentication protocols. Therefore, we decided to use GNY logic for security analysis in this paper. In GNY logic, principals are not assumed to be trustworthy and redundancy is always explicitly present in encrypted messages. GNY logic distinguishes between what a principal can possess and what it can believe in. It enables the expression of different trust levels and implicit conditions behind protocol steps. The main issue with GNY logic is that it has more than forty inference rules, which has led many researchers to consider this logic as being impractical. Using GNY logic, we now verify the correctness of the assumptions with respect to message source as well as the beliefs of the sender and recipient of messages. We proceed by including the individual messages in the protocol followed by inherent explicit assumptions and then the goals. We then present proofs of these goals.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Protocol messages:
M1    $TTP \triangleleft \star (N_R), \star (f_{r_i \oplus N_R \oplus N_P}(s_{C+1}))$
M2    $R_i \triangleleft \star (N_P), \star (f_{r_i \oplus s_c \oplus N_P}(s_{C+1})), \star (f_{r_i \oplus s_c \oplus N_P}(ID_{t_j} \oplus s_{C+1}))$
M3    $T_j \triangleleft \star (N_P), \star (f_{t_j \oplus s_c \oplus N_P}(s_{C+1}))$
M4    $TTP \triangleleft \star (N_T), \star (f_{(s_{C+1} \oplus N_T \oplus N_P)}(s_{C+1}))$
M5    $T_j \triangleleft \star (N'_R), \star (f_{s_{C+1} \oplus N'_R}(s_{C+1}))$
M6    $R_i \triangleleft \star (N_T), \star (f_{s_{C+1} \oplus N'_R}(N_T))$

Assumptions:
A1    $TTP \ni N_P$
A2    $T_j \ni N_T$
A3    $R_i \ni (N_R, N'_R)$
A4    $TTP | \equiv TTP \xleftrightarrow{r_i} R_i$
A5    $R_i | \equiv R_i \xleftrightarrow{r_i} TTP$
A6    $TTP | \equiv T_j \xleftrightarrow{t_j, s_{C+1}} TTP$
A7    $T_j | \equiv TTP \xleftrightarrow{t_j, s_{C+1}} T_j$
A8    $TTP | \equiv \# N_P$
A9    $T_j | \equiv \# N_T$
A10    $R_i | \equiv \# (N_R, N'_R)$
</div>

Goals of the correctness proof: The primary goals of the proposed protocol are belief (| ≡), and the freshness (#), of the messages between each pairs of $T T P , R _ { i } , T _ { j } .$ Belief ensures message is from a trusted source. Freshness ensures message was not sent earlier during the same session.

G17

G18

$$
T _ {j} | \equiv T T P \xleftrightarrow {S _ {c + 1}} T _ {j}\tag{G19}
$$

$$
T _ {j} | \equiv R _ {i} \xleftrightarrow {S _ {c + 1}} T _ {j}
$$

$$
R _ {i} | \equiv R _ {i} \xleftrightarrow {S _ {c + 1}} T _ {j}
$$

Proof. The logical postulate numbers (e.g., M1, T1,..) referred to in the following are from [7].

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
[D1:] $TTP \triangleleft N_R, f_{r_i \oplus N_R \oplus N_P}(s_{c+1})$ /* M1,T1 */  
[D2:] $TTP \ni N_R, f_{r_i \oplus N_R \oplus N_P}(s_{c+1})$ /* D1,P1 */  
[D3:] $TTP \mid \equiv \# N_R, \# f_{r_i \oplus N_R \oplus N_P}(s_{c+1})$ /* D2,F10 */  
[D4:] $TTP \mid \equiv R_i \sim \# N_R$ /* A4,A5,D3,I1 */  
[D5:] $TTP \mid \equiv R_i \mid \sim \# f_{r_i \oplus N_R \oplus N_P}(s_{c+1})$ /* A4,A5,D3,I1,P2 */  
[D6:] $R_i \triangleleft (N_P), (f_{r_i \oplus S_c \oplus N_P}(s_{c+1})), (f_{r_i \oplus S_c \oplus N_P}(ID_{t_j} \oplus s_{c+1}))$ /* M2,T1 */  
[D7:] $R_i \ni (N_P), (f_{r_i \oplus S_c \oplus N_P}(s_{c+1})), (f_{r_i \oplus S_c \oplus N_P}(ID_{t_j} \oplus s_{c+1}))$ /* D6,P1 */  
[D8:] $R_i \mid \equiv \# (N_P), \# (f_{r_i \oplus S_c \oplus N_P}(s_{c+1})),$ /* D7,F10 */  
$\#(f_{r_i \oplus S_c \oplus N_P}(ID_{t_j} \oplus s_{c+1}))$  
[D9:] $R_i \mid \equiv TTP \mid \sim \# (N_P)$ /* A4,A5,D8,I1 */  
[D10:] $R_i \mid \equiv TTP \mid \sim \# (f_{r_i \oplus S_c \oplus N_P}(s_{c+1}))$ /* A4,A5,D8,I1,P2 */  
[D11:] $R_i \mid \equiv TTP \mid \sim \# (f_{r_i \oplus S_c \oplus N_P}(ID_{t_j} \oplus s_{c+1}))$ /* A4,A5,D8,I1,P2 */  
[D12:] $T_j \triangleleft (N_P), (f_{t_j \oplus S_c \oplus N_P}(s_{c+1}))$ /* M3,T1 */  
[D13:] $T_j \ni (N_P), (f_{t_j \oplus S_c \oplus N_P}(s_{c+1}))$ /* D12,P1 */  
[D14:] $T_j \mid \equiv \# (N_P), \# (f_{t_j \oplus S_c \oplus N_P}(s_{c+1}))$ /* D13,F10 */  
[D15:] $T_j \mid \equiv TTP \mid \sim \# (N_P)$ /* A6,A7,D14,I1 */  
[D16:] $T_j \mid \equiv TTP \mid \sim \# (f_{t_j \oplus S_c \oplus N_P}(s_{c+1}))$ /* A6,A7,D14,I1,P2 */  
[D17:] $TTP \triangleleft (N_T), (f_{(S_{c+1} \oplus N_T \oplus N_P)}(s_{c+1}))$ /* M4,T1 */  
[D18:] $TTP \ni (N_T), (f_{(S_{c+1} \oplus N_T \oplus N_P)}(s_{c+1}))$ /* D17,P1 */  
[D19:] $TTP \mid \equiv (\mathcal{N}_T), \# (f_{(S_{c+1} \oplus N_T \oplus N_P)}(s_{c+1}))$ /* D18,F10 */  
[D20:] $TTP \mid = T_j | = \# (N_T)$ /* A6,A7,D19,I1 */  
[D21:] $TTP | = T_j | = \# (f_{(S_{c+1} \oplus N_T \oplus N_P)}(s_{c+1}))$ /* A6,A7,D19,I1,P2 */  
[D22:] $T_j &lt; (N_R), (f_{S_{c+1}^{\prime} + NR^{\prime}}(S_{c+1}))$ /* M5,T1 */  
[D23:] $T_j &gt; (N_R), (f_{S_{c+1}^{\prime} + NR^{\prime}}(S_{c+1}))$ /* D22,P1 */  
[D24:] $T_j | = \# (N_R), #(f_{S_{c+1}^{\prime} + NR^{\prime}}(S_{c+1}))$ /* D23,F10 */  
[D25:] $T_j | = R_i | = \# (N_R^{\prime})$ /* D24,F1,I1 */  
[D26:] $T_j | = R_i | = \# (f_{S_{c+1}^{\prime} + N_R^{\prime}}(S_{c+1}))$ /* D24,F1,I1,P2 */  
[D27:] $R_i &lt; (N_T), (f_{S_{c+1}^{\prime} + N_R^{\prime}}(N_T))$ /* M6,T1 */  
[D28:] $R_i &gt; (N_T), (f_{S_{c+1}^{\prime} + N_R^{\prime}}(N_T))$ /* D27,P1 */  
[D29:] $R_i | = \# (N_T), #(f_{S_{c+1}^{\prime} + N_R^{\prime}}(N_T))$ /* D28,F10 */  
[D30:] $R_i | = T_j | = \# (N_T)$ /* D29,F1,I1 */  
[D31:] $R_i | = T_j | = \# (f_{S_{c+1}^{\prime} + N_R^{\prime}}(N_T))$ /* D29,F1,I1,P2 */  
[D32:] $TTP | = TTP, S_{c+1}, R_i$ /* A4,D3,J1 */  
[D33:] $R_i | = R_i, S_{c+1}, TTP, S_{c+1}, TTP, S_{c+1}, TTP, S_{c+1}, Tj, S_{c+1}, Tj, S_{c+1}, Tj, S_{c+1}, Tj, S_{c+1}, Tj, S_{c+1}, Tj, S_{c+1}, Tj, S_{c+1}, Tj, S_{c+1}, Tj, S_{c+1}, Tj, S_{c+1}, Tj, S_{c+1}, Tj,$
</div>

The proof of goals 1–19 is shown by the veri<sup>fi</sup>cation steps D4, D5, D9, D10, D11, D15, D16, D20, D21, D25, D26, D30, D31, D32, D33, D34, D35, D40, and D39 respectively.

![](/api/attachments/TH7BBEKU/fulltext/images/a0846071f0a7b063ad8baa34e27945d9b5c804a1340ba3f8b1be163e848bcc83.jpg)  
Fig. 14. A base object with several components.

![](/api/attachments/TH7BBEKU/fulltext/images/242c7f0635d83572061de8b2d857e350f786969f7441a479134378f479e4c6ef.jpg)  
Fig. 15. An object comprising several components.

## 5.3. Ownership transfer for multiple components

An object (A) can comprise several components $( 1 \ldots ( { } )$ . There are at least two possible variations: (1) The <sup>fi</sup>rst (Fig. 14) is where the object of interest refers to the base object that contains several components, where the object still exists and can be communicated with even when all of its component parts are removed. An example scenario could be where the base object has an active tag while each of the components have passive tags (e.g., master–slave con<sup>fi</sup>guration where the master tag has a longer life-span compared to that of the slave tag), (2) The second (Fig. 15) is where the object comprises only its component parts (i.e., there is no base object). In this scenario, the object ceases to exist when all its component parts are removed. An example of the former (i.e., Fig. 14) is a tag on a pallet containing several tagged items. An example of the latter (i.e., Fig. 15) is a bicycle with tags on each of its component parts.

From an ownership transfer perspective, the way in which an object is assembled (i.e., with or without a base or reference object) affects the communication protocol even if only to a minimal degree. For example, in Fig. 14, the components can be assumed to be a part of the object as a whole and may therefore need not explicitly take part in the ownership transfer protocol. When ownership transfer of the base object occurs, the components remain associated with the base object and this association is independent of the ownership details of the entire object. In this scenario, the base object represents the entire object for communication with external entities. Therefore, there is no need for the component objects to know of the ownership details other than the fact that they belong to this base object. We discuss simultaneous ownership transfer of several components in Section 6.

In Fig. 15, each of the components independently (sequentially or in parallel) take part in ownership transfer. We need to consider the object con<sup>fi</sup>guration (i.e., with or without the base object) and make necessary modi<sup>fi</sup>cations (i.e., one shot ownership transfer for the entire object vs. multiple ownership transfers — one for each component). Simultaneous ownership transfer of all the component parts is explained in detail in Section 6.

## 5.3.1. Ownership transfer

We present a generic case involving the following parties, namely Tag , TTP, previous owner $R _ { 1 }$ and new owner $R _ { 2 } .$ Here, the tag can either be from the base object (as in Fig. 14) or from each of the individual components (as in Fig. 15). Once the request for transfer of ownership has been invoked and approved, the procedure for the actual transfer of ownership works exactly the same as in the protocol presented in Section 3.

## 5.3.2. Authentication

The authentication handshake works exactly the same as the scenario presented in Section 3.

## 6. Simultaneous ownership transfer of multiple RFID tags

It is not hard to imagine a scenario where two items need to be together (e.g., pharmaceutical item and its accompanying information materials; an electronic item and its necessary accessories such as a power cord) through a large part of their presence in a supply chain where they change ownership as a pair (or, as a group of items when there are N2 items). There is, therefore, a need for such a protocol and we attempt to develop a protocol for such a scenario. Fig. 16 illustrates the essence of this scenario with the time scale represented from left to right.

The proposed protocol for simultaneous ownership transfer of two items that belong together is given in Fig. 17. This protocol comprises <sup>fi</sup>ve ‘loops’ between pairs of entities with the <sup>fi</sup>rst three initiated by the trusted third party (TTP) and the other two initiated by the new owner $\left( R _ { 2 } \right)$ . Fig. 17 illustrates transfer of ownership of entities with tags T and T that belong together from previous owner $\left( R _ { 1 } \right)$ to the new owner $\left( R _ { 2 } \right)$ . The process begins when the previous and new owner decide to transfer ownership and inform the TTP of the same. This step is not explicitly or implicitly modeled in the protocol. Although this protocol models transfer of ownership of two related items, this can readily be extended to any number of related items that need to be in close proximity of one another.

The <sup>fi</sup>rst ‘loop’ is between the TTP and one of the two tags (here, $T _ { i } ) .$ . This step $( N _ { P } , f _ { ( N _ { P } \oplus t _ { i } \oplus s _ { 1 } ^ { i } ) } ^ { \prime } ( s _ { 2 } ^ { i } ) )$ from the TTP to tag $T _ { i }$ and $N _ { T _ { i } } ,$ $H _ { ( t _ { i } \oplus N _ { T _ { i } } ) } ( s _ { 2 } ^ { i } \oplus N _ { P } )$ from tag T to the TTP) essentially accomplishes generation of new shared key for the <sup>fi</sup>rst Tag $T _ { i } \left( \mathrm { i } . \mathrm { e } . , s _ { 2 } ^ { i } \right)$ and secure transfer of this key to $T _ { i \cdot }$ If the return message is blocked from getting back to the TTP for whatever reason, the TTP waits for a pre-determined amount of time and re-transmits the <sup>fi</sup>rst message with a new nonce $( N _ { P } ) .$ . Once the <sup>fi</sup>rst loop is completed, the TTP uses the nonce $( \mathrm { i } . { \mathsf { e } } . , N _ { T _ { i } } )$ generated by the <sup>fi</sup>rst tag (or, any tag, if there are several tags) to communicate with the second (or, next, if there are several tags) tag. The message used in the second loop follows a similar pattern as that in the <sup>fi</sup>rst loop and the newly generated shared key (i.e., $s _ { 2 } ^ { j } )$ is securely sent to the second tag (T<sub>j</sub>). The TTP again waits for reply from the second tag. If this reply is not received within a predetermined amount of time, it repeats only this loop with a freshly generated nonce (N″). When there are more than two tags that belong together and need to veri<sup>fi</sup>ed of their simultaneous presence in the <sup>fi</sup>eld of the reader, the second loop is modi<sup>fi</sup>ed appropriately – with the nonce generated by the previous tag in the sequence, the tag's shared key with the TTP, its current key, and its next key that is generated by the TTP – and repeated for each of these tags. The TTP veri<sup>fi</sup>es the acknowledgment from the tags for their authenticity.

![](/api/attachments/TH7BBEKU/fulltext/images/52cec8b44418bbc237390911d04b4b506e961d13eba60bd67b7efacb7153e4fc.jpg)  
Fig. 16. Multi-tag simultaneous ownership transfer [with TTP].

![](/api/attachments/TH7BBEKU/fulltext/images/46d941bd632e9fb7a6d031b9362c8676c7effb305031f910ea4316a38933bf38.jpg)  
Fig. 17. Multi-tag simultaneous ownership transfer protocol with TTP.

The third loop is between the TTP and the new owner and is initiated by the TTP. This loop involves the transfer of the tags' secret keys (here, s<sup>i</sup> , s <sup>j</sup>) to the new owner. The new owner acknowledges receipt of these keys with $H _ { r _ { 2 } } ( s _ { 2 } ^ { i } \oplus s _ { 2 } ^ { j } \oplus N _ { P } ^ { \prime } )$ , where $r _ { 2 }$ is the shared key between the TTP and this owner and N<sup>′</sup> is the nonce generated and sent by the TTP. When there are more than two tags, the messages are modi<sup>fi</sup>ed appropriately to incorporate the same. I.e., when c is the last tag in the sequence, the TTP modi<sup>fi</sup>es and includes the following for every tag that needs to be veri<sup>fi</sup>ed: $f _ { ( r _ { 2 } \oplus N _ { P } ^ { \prime } ) } \big ( S _ { 2 } ^ { C } \oplus r _ { 2 } \big )$ for the last tag in the sequence, with the appropriate s<sup>⁎</sup> for each of the other tags in the sequence. Similarly, the new owner sends $H _ { r _ { 2 } }$ (s<sup>i</sup> ⊕ s <sup>j</sup> ⊕ ⋯ ⊕ s<sup>c</sup> ⊕ N<sup>′</sup>) to the TTP where c is the last tag in the sequence. Like in the <sup>fi</sup>rst two loops, the TTP waits for acknowledgment from the reader. Again, if the acknowledgment fails to materialize, the TTP repeats only this loop with a freshly generated nonce (N<sup>′</sup>).

Upon successful completion of this third loop in the protocol, the new owner is made aware of the tags' keys. The new owner completes the next two loops – i.e., the new owner authenticates the two tags using the next two loops – before acknowledging receipt of message to the TTP. I.e., the fourth and <sup>fi</sup>fth loops are nested within the third loop. These next two loops (i.e., loops four and <sup>fi</sup>ve) are initiated by the new owner (with $N _ { R _ { 2 } } J _ { s _ { 2 } } ^ { \prime } ( N _ { R _ { 2 } } ) )$ and are similar in structure with the use of the same freshly generated nonce $( N _ { R _ { 2 } } )$ , except for the encryption keys used. The new owner waits for response from all the tags in the set that are veri<sup>fi</sup>ed for their simultaneous presence. If it does not hear back from even one of the tags, it retransmits its message to all the tags with a different nonce (i.e., $N _ { R _ { 2 } } )$ . The response from the tags is veri<sup>fi</sup>ed for their authenticity. Once the tags' authenticity is veri<sup>fi</sup>ed, the new owner acknowledges the same to the TTP.

When the TTP gets the acknowledgment from the new owner, it sends the last message in the protocol (i.e., the message from TTP to the previous owner) informing the previous owner $( \mathrm { i } . \mathrm { e } . , R _ { 1 } )$ with a message that is encrypted with the shared key $( \mathrm { i } . \mathrm { e } . , r _ { 1 } )$ between the TTP and the previous owner that the previous keys $( \mathrm { i } . \mathsf { e } . , s _ { 1 } ^ { i } , s _ { 1 } ^ { j } )$ are no longer valid. The previous owner ceases to have access to these tags while the new owner begins to have access to these tags.

The protocol seems rather busy with several messages. However, it is a one-pass protocol between every pair of entities and we believe it is reasonable given what it accomplishes. We kept the following in mind while developing this protocol: (1) generate fresh nonce every time a new loop is run to ensure freshness of the message and to avoid repeating previously sent message, (2) reduce use of one-way hash functions since these are (computational) resource intensive, while using one-way hash function when necessary (3) the originating message in each loop is synchronous in a sense since it expects the recipient to acknowledge with a response, which when not received would trigger repeating the loop with a freshly generated nonce, (4) previous owner should not have access to the new tag secrets while the new owner does, (5) messages sent to the tags after the ‘<sup>fi</sup>rst’ tag depend on and are derived from message sent to or generated by the ‘previous’ tag to ensure dependency among the authenticated set of tags and to prevent insertion of a fake tag by an adversary, and (6) not sending any identi<sup>fi</sup>cation information in cleartext. By following the above, the resulting protocol is free ofobvious vulnerabilities that have been identi<sup>fi</sup>ed in the literature on cryptanalysis of existing RFID protocols. This, however, obviously does not provide any guarantees of the security of the proposed protocol. The security of this protocol can only be ascertained through detailed analysis and even then the nature of RFID protocols precludes any claims to its complete security against attacks from a resourceful adversary.

One issue that is not addressed here is the possibility of ‘de-yoking’ the tags when necessary in-between two consecutive ‘yoked’ ownership transfers. We thank one of the reviewers of this paper for pointing this out. We do not have a solution to this switching issue. We do, however, acknowledge the possibility of such a scenario and defer addressing this issue to future work.

## 6.1. Security analysis

We provide a brief security analysis of the proposed protocol considering some of the common vulnerabilities that are generally present in such protocols and provide brief discussions on each.

## 1. Authenticity, secrecy, data integrity:

The messages that are seemingly vulnerable use one-way hash functions to ensure that they are not easily tampered with and other messages between any pairs of entities (tag, reader, TTP) are also encrypted and no clearly identi<sup>fi</sup>able information is sent in cleartext.

## 2. DoS/synchronization problem:

A means to denial of service (DoS) attack through blocking of messages or de-synchronization of secret keys is prevented through requirement of acknowledgment in all <sup>fi</sup>ve loops in the protocol. I.e., the sender waits for the recipient to acknowledge its message before proceeding further. This mechanism facilitates alleviating issues including those associated with adversaries blocking messages between any two entities.

## 3. Relay attack:

Relay attack and its variants (e.g., Ma<sup>fi</sup>a attack, Terrorist attack) cannot be prevented using the proposed protocol since it is not protected against such attacks. A majority of existing RFID protocols are not immune to relay attacks. Although several means to address relay attacks exist, none of them completely prevent such attacks since these protocols use the round-trip time taken by messages between any two entities and measuring these necessitates access to extremely sensitive devices since these distances are generally small (e.g., a few centimeters to a few meters at the most) and it is extremely dif<sup>fi</sup>cult to identify latency.

## 4. Prevention of replay attack:

The proposed protocol addresses this issue through two means: (1) freshly generated nonce in every loop, and (2) no two messages between different pairs of entities are the same. While the former prevents an adversary from simply capturing and replaying the captured message to the same entity at a later point in time, the latter prevents copying message from an entity and replaying it with or without appropriate modi<sup>fi</sup>cations to another entity.

## 5. Forward security:

Knowing the current key, an adversary will not be able to decipher past messages between the entity of interest and any other entity. This is due to the one-way hash functions used to encrypt messages in every loop in the protocol.

## 7. Discussion

The importance of RFID security/privacy issues and their direct in-<sup>fl</sup>uence on consumers are a relatively recent phenomenon. A majority, if not all, of the literature in this area has addressed these issues from the perspective of a single-tagged object. However, since objects with multiple tags are not uncommon, there is a need to develop privacy/ security protocols that address this con<sup>fi</sup>guration — i.e., protocols for authentication of objects with multiple RFID tags. Although not an issue in the single-tagged scenario, objects with multiple tags face the issue of components (i.e., tags) being added or removed over time. We presented a protocol for inclusion and exclusion of tags on an object of interest. We also considered ownership transfer issues when multiple tags exist on an object.

We considered several variations that can arise when transferring RFID tag ownership. We presented ownership transfer protocols for multiple tag and/or multiple ownership cases. Moreover, we considered scenarios with and without a TTP. We also developed a protocol that simultaneously accomplishes two tasks: verifying the simultaneous presence of multiple tags in the <sup>fi</sup>eld of the reader and ownership transfer of multiple tags between two owners (represented by readers, here) in the presence of a trusted third party. Extant protocols accomplish either of these tasks separately but not both in one protocol. Incorporating both these tasks in one protocol accomplishes these with less overhead when a scenario dictates seamlessly accomplishing both these tasks. While the proposed protocol only considered two tags, extensions to multiple tags are easily accomplished by appropriately modifying and repeating the messages between tag and TTP, tag and new owner, and TTP and new owner. The proposed protocol is certainly not immune to relay attacks like other extant ownership transfer protocols as well as ‘yoking proof’ protocol and its variants.

As was observed earlier (e.g., [13]), it is rather challenging to develop ownership transfer protocols without the presence of a trusted third party. The best one can do in such a situation (i.e., without a TTP) is a ownership m sharing (as opposed to transfer) protocol where every previous owner continues to maintain RF access to the tag. Depending on the context of interest, this may not even be an issue. However, identifying a protocol as an ownership transfer protocol necessitates that it indeed strictly transfers ownership between entities and not a looser version where ownership is shared among current and all previous owners.

Given the track record of protocols developed for RFID authentication, such protocols are secure only until a vulnerability is identi<sup>fi</sup>ed regardless of any proof claiming otherwise. As have been illustrated in numerous other cases where protocols had been proven to be secure against attacks, only to be shown to be vulnerable to some attack by a resourceful adversary using an identi<sup>fi</sup>ed loop-hole. Regardless, as more and more applications using RFID tags become a reality it is necessary to develop secure protocols that can protect and secure RFID-tagged objects from resourceful adversaries that attempt to violate the security and privacy of these objects. We considered a few variations of the single-tag single-owner ownership transfer scenarios that involve multiple tags and/or multiple owners and developed protocols for the same. This is only a <sup>fi</sup>rst step in the direction of developing secure protocols for such scenarios that are not so uncommon in supply chains.

## Acknowledgments

The authors thank the three reviewers for their detailed constructive comments and suggestions that have helped improve both the content and presentation of this paper.

## References

[1] H.-B. Chen, W.-B. Lee, Y.-H. Zhao, Y.-L. Chen, Enhancement of the RFID security method with ownership transfer, Proceedings of the ICUIMC, 2009, pp. 251–254.

[2] C.-L. Chen, Y.-L. Lai, C.-C. Chen, Y.-Y. Deng, Y.-C. Hwang, RFID ownership transfer authorization systems conforming EPCglobal class-1 generation-2 standards, International Journal of Network Security 12 (3) (May 2011) 221–228.

[3] Choo, Boyd, Hitchcock, Examining indistinguishability-based proof models for key establishment protocols, Advances in Cryptology — Asiacrypt05, Springer-Verlag, 2005.

[4] T. Dimitriou, RFIDDOT: RFID delegation and ownership transfer made simple, Proceedings of the 4th International Conference on Security and Privacy for Communication Networks (SecureComm), 2008.

[5] Gilbert, Robshaw, Sibert, An active attack against HB+ — a provably secure lightweight authentication protocol, IEEE Electronic Letters 41 (21) (2005) 1169-1170

[6] G. Godor, M. Antal, Improved lightweight mutual authentication protocol for RFID systems, Wireless and Mobile Networking, IFIP International Federation for Information Processing, Volume 284, 2008, pp. 71–482.

[7] L. Gong, R. Needham, R. Yahalom, Reasoning about belief in cryptographic protocols, Proceedings of the IEEE Symposium on Security and Privacy, 1990, pp. 234–248.

[8] A.M. Hamad, W.I. Khedr, “Ad-hoc on Demand Authentication Chain Protocol — An Authentication Protocol for Ad-hoc Networks". SECRYPT. 2009

[9] A. Ilic, F. Michahelles, E. Fleisch, “The Dual Ownership Model — A Concept for Ef-<sup>fi</sup>cient Access Management of Item-Level Data in Pharmaceutical Supply Chains", Auto-ID Labs White Paper, 2007

[10] P. Jäppinen, H. Hämäläinen, Enhanced RFID Security Method with Ownership Transfer, Proceedings of the International Conference on Computational Intelligence and Security, 2008, pp. 382–385.

[11] A. Juels, Yoking proofs for RFID tags, Proceedings of the First International Workshop on Pervasive Computing and Communication Security, IEEE Press, 2004.

[12] A. Juels, S. Weiss, “Authenticating pervasive devices with human protocol", advances in cryptology — CRYPTO 2005, LNCS 3621 (2005) 293–308.

[13] G. Kapoor, S. Piramuthu, Single RFID tag ownership transfer protocols, IEEE Transactions on Systems, Man, and Cybernetics — Part C, 2011.

[14] G. Kapoor, S. Piramuthu, Vulnerabilities in some recently proposed RFID ownership transfer protocols, IEEE Communications Letters 14 (3) (March 2010) 260–262.

[15] E. Levieil, P.-A. Fouque, An attack of HB+ in the detection-based model, Security and Cryptography for Networks, September 2006.

[16] Li, Ma, Moon, On the security of the Canetti–Krawczyk Model, Proceedings of CIS, Part II, LNAI 3802, Springer-Verlag, 2005, pp. 356–363.

[17] I.-C. Lin, C.-W. Yang, S.-C. Tsaur, Non-identi<sup>fi</sup>able RFID privacy protection with ownership transfer, International Journal of Innovative Computing, Information, and Control 6 (4) (April 2010).

[18] J.-H. Oh, H.-S. Kim, J.-Y. Choi, A secure communication protocol for low-cost RFID system, Proceedings of the 7th IEEE International Conference on Computer and Information Technology, IEEE Computer Society, 2007, pp. 949–954.

[19] S. Piramuthu, Protocols for RFID tag/reader authentication, Decision Support Systems 43 (3) (2007) 897–914.

[20] S. Piramuthu, RFID mutual authentication protocols, Decision Support Systems 50 (2) (2011) 387–393.

[21] J. Saito, K. Sakurai, Grouping proof for RFID tags, Proceedings of the 19th International Conference on Advanced Information Networking and Applications (AINA'05), 2005, pp. 621–624.

[22] B. Song, RFID tag ownership transfer, Proceedings of RFIDSec08, 2008.

[23] B. Song, C.J. Mitchell, Scalable RFID security protocols supporting tag ownership transfer, Computer Communications (2010).

[24] Y.-J. Tu, W. Zhou, S. Piramuthu, Identifying RFID-embedded objects in pervasive healthcare applications, Decision Support Systems 46 (2) (2009) 586–593.

[25] M. Waller, M. Johnson, T. Davis, Vendor-managed inventory in the retail supply chain, Journal of Business Logistics 20 (1) (1999).

[26] X.-F. Wang, J.-G. Liu, J. Xu, S.-L. Liu, Mobile RFID security protocol and its GNY logic analysis, Journal of Computer Applications 28 (9) (2009) 2239–2241.

[27] M.-H. Yang, Lightweight authentication protocol for mobile RFID networks, International Journal of Security and Networks 5 (1) (2009) 53–62.

[28] E.-J. Yoon, K.-Y. Yoo, Two security problems of RFID security method with ownership transfer, Proceedings of the IFIP International Conference on Network and Parallel Computing, 2008, pp. 68–73.

Gaurav Kapoor received his Ph.D. (Information Systems) from the University of Florida in 2008. His research interests include RFID systems (especially issues related to security, privacy and ownership transfer and protocols addressing the same) and text mining. His work has appeared in journals such as Decision Support Systems, European Journal of Information Systems, and IEEE Transactions on Systems, Man and Cybernetics

Wei Zhou received his Ph.D. in Information Systems from the University of Florida in 2008. His research interests include RFID-enabled item-level information visibility, In ternet advertising, and knowledge-based learning systems. His work has appeared in European Journal of Operational Research, IEEE Transactions on Geosciences and Re mote Sensing, International Journal of Electronic Commerce, and Optical Engineering

Selwyn Piramuthu is a professor of Information Systems at the University of Florida. He is also a member of the RFID European Lab in Paris. His research interests include RFID systems, pattern recognition and its application in computer-aided manufacturing, <sup>fi</sup>nancial credit-risk analysis, health care management, and supply chain management.
