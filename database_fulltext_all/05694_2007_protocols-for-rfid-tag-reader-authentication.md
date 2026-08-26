---
otero_id: 5694
otero_key: "3ZKNVFYP"
title: "Protocols for RFID tag/reader authentication"
authors: "Selwyn Piramuthu"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.01.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Protocols for RFID tag/reader authentication

Selwyn Piramuthu

Decision and Information Sciences, University of Florida, Gainesville, FL 32611-7169, USA

Received 23 June 2006; received in revised form 2 January 2007; accepted 22 January 2007 Available online 27 January 2007

## Abstract

Radio-Frequency Identification (RFID) tags are poised to supplant barcodes in the very near future. Their information storage capacity as well as their ability to transfer information through contactless means without line-of-sight translates to significant advantage over barcodes. However, cost and privacy issues are major impediments to their widespread use. We consider the latter issue, specifically those that relate to securely authenticating RFID tags and readers. Light-weight authentication protocols are necessary in RFID applications due to tag-level constraints. Over the past few years, several streams of research have emerged approaching the RFID tag/reader privacy/security problem from different perspectives. We study and evaluate a few protocols from each of those streams, identify possible vulnerabilities, and provide alternate solutions when possible. We provide security analysis of the proposed solutions.

© 2007 Elsevier B.V. All rights reserved.

Keywords: RFID; Light-weight cryptography; Secure authentication

## 1. Introduction and background

Radio-Frequency Identification (RFID) refers to technologies and systems that use radio waves (wireless) to transmit and uniquely identify objects [14,21]. It generally involves an RFID transponder or tag, which comprises a chip and an antenna that are together attached to an object that is to be identified and/or tracked. The antenna allows the chip to transmit stored information about the object of interest to a reader. These chips can store about 2 kb of data. Tag readers are used to retrieve data stored in RFID tags. Antennas are used to send and receive radio waves and signals between tag readers and RFID tags. The tag reader is connected to a back-end server and database for relatively heavy-duty processing (e.g., authenticating a tag using an identifier that is embedded in a keyed hash function).

RFIDs were first used in WW-II as IFF (Identify Friend or Foe system). Although RFID technology is decades old, there has been renewed interest in utilizing its beneficial properties from researchers and practitioners alike. RFID technology is used to facilitate information sharing in decentralized business environments such as supply chains [18]. Based just on WalMart's mandate and that of U.S. Department of Defense (US-DOD), the RFID tag market in the U.S. retail supply chain was \$91.5 million in 2003, and is expected to be around \$1.3 billion in 2008 (U.S. RFID for the Retail Supply Chain Spending Forecast and Analysis, 2003–2008, IDC.com, 2005). The value of total market, including systems and services, is projected to be around \$26.9 billion in 2015 [20]. Gartner [15] estimates the market for RFID tags to be around \$3 billion in 2010.

Privacy and security issues play a major role in the success of RFID tag implementations due to the ease with which the object they are attached to can be identified and/or tracked by an adversary. Most existing implementations of RFID tags are not secure, and can leak data about the object to which they are attached. An adversary can also silently track/monitor the object. Some common types of attacks on RFID tags include eavesdropping, replay attack, man-in-the-middle attack, loss of data including DoS (denial of service) and message hijacking, skimming and forgery (including cloning), and physical attack. The reader is referred to Avoine and Oechslin [2] for detailed description of these and other types of attack on RFID tag/reader. Although there are means to protect tags against some of these attacks, newer vulnerabilities are discovered often enough that there seems to be no such thing as perfect protection (e.g., [6] show how they defeated the security of an RFID device known as a Digital Signature Transponder manufactured by Texas Instruments that helps secure millions of highway toll payment transponders and automobile ignition keys; [33] present details of virus attack on RFID tags; SCISSEC [36] present a DoS attack against Frequency Hopping Spread Spectrum). For excellent surveys on security/privacy issues as related to RFID tags, the reader is referred to Garfinkel et al. [42] and Rieback et al. [34].

Privacy and security issues play critical role in acceptance of RFID tags by the general public since most people are circumspect of being monitored/tracked watched/etc. (see, for example, www.rfidkills.com, www. stoprfid.org, www.spy.org.uk/cgi-bin/rfid.pl). Although other means of tracking people (e.g., video surveillance) are already in widespread use, some of the inherent properties of RFID tags renders opportunities for suspicion including their low cost, physical size, extended lifespan when battery power is not used, extensive data generation capability, and the absence of an off switch.

There exist a few means to disable tags from being read. For example, the Blocker tag presented in Juels et al. [27], Clipped tags presented in Karjoth and Moskowitz [28], metal or foil-lined containers (e.g., wallets) that are impenetrable to radio-frequency waves (Faraday cage), and the case where the user simply destroys the tag along with the tagged object [39]. Castelluccia and Avoine [9] propose ‘noisy’ tags to confuse an adversary from deciphering reader/tag conversation. Although these are important issues, we are interested only in the technical aspects of RFID security/privacy. Given the cost, limited storage and computational capacity of these tags, resource allocation addressing security/privacy concerns invariably are insufficient. Market forces dictate lower cost with more usable functionality, whereas security/ privacy issues generally do not improve bottom lines. Even if the entire set of resources available on an RFID tag are used for cryptographic protocols, standard cryptographic algorithms (e.g., RSA) cannot be used to support authentication protocols in passive RFID tags due to their storage and processing limitations. For example, even the higher-end passive tags have at most 2000 gates for security purposes while a standard cryptographic algorithm would require gates in the order of tens of thousands [26]. Moreover, storage requirements for these algorithms prove to be insufficient as well. Moore's Law is not a consolation here due to market price pressures [26].

When dealing with privacy/security issues in passive RFID tag implementations, their processing power and memory constraints therefore dictate lightweight authentication protocols. Several researchers have proposed and evaluated protocols that fit the bill of being lightweight and at the same time being secure to a reasonable extent [2,13,40].

Over the past few years, several streams of research have emerged that deal with authenticating tags and tag readers. We consider a few such streams of research and their resulting authentication protocols. Specifically, we consider the following: single round protocols for single tag, multiple round protocols for single tag, single round protocols for multiple tags, and protection against relay attacks. These protocols, by their very nature, tend to be heuristic-based or are sometimes based on reduction to NP-hard problems.

The contribution of this paper are three-fold: we present an overview of various streams of research involving RFID tag/reader authentication; we present privacy/security vulnerabilities in existing protocols identified by other researchers as well as new ones; we propose modifications to existing vulnerable protocols without proof.

This paper is organized as follows: the next section provides an overview of several single round protocols for single tag. Section 3 presents an overview of several multiple round protocols for single tag. Section 4 presents an overview of single round protocols for multiple tags. Section 5 presents an overview of relay attacks. The final section concludes the paper with discussion of overview as well as modifications presented in this paper.

## 2. Single round protocols for single tag

By far, the most studied among secure protocols for authenticating single RFID tags are the single round protocols. These protocols typically involve a few (most commonly about 3) repeated challenge-response messages between the RFID tag (prover) and the tag reader (verifier). Other things being equal, the single round protocols are preferable to multiple round protocols in time critical applications. In terms of security, again with other things being equal, an adversary gets fewer opportunities to observe and retrieve critical information in single round protocols. Several single round protocols for single tags have been proposed by researchers over the past few years.

![](/api/attachments/3ZKNVFYP/fulltext/images/3ca8d109489e16195e31053766bb0f9fccc58ba3fc0ae143302fda7b16009ac1.jpg)  
Fig. 1. Protocol of Weis, Sarma, Rivest, and Engels [40].

We briefly describe a few of them and evaluate them in terms of privacy/security vulnerabilities.

Notations used in this paper:

$s , r , r _ { \mathrm { A } } , r _ { \mathrm { B } } .$ random l-bit (or k-bit) vectors

• $s _ { i } ,$ ID: tag identifier

$x , x ^ { \prime } , x _ { I } , x _ { 2 } , x _ { A } , x _ { B } , x _ { R } , y , y ^ { \prime } ; \ l \mathrm { - b i t ~ ( o r ~ } k \mathrm { - b i t ) }$ secret vectors

• $h ,$ , H, G: hash functions — $\{ 0 , \ 1 \} ^ { * }  \{ 0 , \ 1 \} ^ { l }$ (or, $\{ 0 , 1 \} ^ { k } )$

• $h _ { k } :$ keyed (k) hash function

• ν: noise bit (=1 with probability $\eta \in \left[ 0 , \frac { 1 } { 2 } \right] )$

• sn: session number

• TS: time stamp

• V: verifier for MAC

• MAC: Message Authentication Code

$\mathrm { M A C } _ { x } [ \mathrm { m } ] .$ : MAC using secret key x on message m

$P _ { \mathrm { A B } } { \mathrm { : } }$ proof A and B scanned simultaneously

## 2.1. Protocol of Weis, Sarma, Rivest, and Engels [40]

One of the earliest among these protocols was proposed by Weis et al. [40]. Fig. 1 provides a sketch of their protocol. In Fig. 1 as well as in the remaining figures in this paper, the time scale runs from top to bottom. I.e., the top-most message is sent first and the bottom-most message is sent last. The concatenation and exclusive-or (XOR) operators are represented by || and ⊕ respectively. Here, $f _ { x } ( r )$ is a pseudorandom function ensemble. Both tag and reader share secret x.

This protocol is not secure against an adversary who mounts a replay attack [1]. For example, the adversary can eavesdrop on the messages passed between a tag and the reader and record the messages. At some later point in time, the adversary can replay the message from the tag to the reader, and the reader will accept it as a valid tag. I.e., the adversary would be able to impersonate the tag to a legitimate reader [1]. We can make it harder to mount a replay attack by letting the reader generate r and sending it to the tag along with the request. It is relatively hard for replay attacks when fresh random values are generated and used during each new authentication process. Another vulnerability is due to the open broadcast of the tag's identity (ID). This can be used by an adversary to track tags.

## 2.2. Protocol of Ohkubo, Suzuki, and Kinoshita [43]

The next single round protocol we consider is also among the earliest ones for a single RFID tag [43]. Fig. 2 provides a sketch of this protocol, which relies on two hash chains (G and H ) to update a random identifier that is stored both in the tag as well as the system's database. The random identifier begins with $s _ { 1 }$ . When the reader sends a request to the tag, the tag computes $G ( s _ { i } )$ and sends it to the reader and then updates the identifier using the other hash function $H \left( { { s _ { i + 1 } } } = H ( { { s _ { i } } } ) \right)$ ). The backend database linked to the reader maintains pairs of $\mathrm { \Delta ^ { \prime } ( I D } ^ { k }$ $s _ { 1 } ^ { k } )$ where $\mathrm { I D } ^ { k }$ is the identifier and $s _ { 1 } ^ { k }$ is the initial secret information for tag k. After receiving the second message, the back-end database does an exhaustive search of hashed values to identify the tag.

This protocol assures privacy since the information sent by the tag is indistinguishable from a random value in a random oracle model. It also assures forward privacy (i.e., an adversary cannot track its past events even by tampering with the tag) because of the one-way hash functions. However, it is not immune against replay attacks. For example, an adversary can send a request to the tag and record its reply and replay it to the reader at some later point in time without the $\mathrm { t a g } ^ { \prime } \mathrm { s }$ presence. Avoine, Dysli, and Oechslin [3] propose a modification to this protocol to prevent replay attacks (Fig. 3). The modified protocol uses a fresh challenge (r) sent by the reader, thus preventing replay attacks since the adversary cannot replay $G ( s _ { i } \oplus r )$ with a different r.

![](/api/attachments/3ZKNVFYP/fulltext/images/491a9292158775823c3f427b322459012d5a3e52bac6515fa0f40049211ff290.jpg)  
Fig. 2. Protocol of Ohkubo, Suzuki, and Kinoshita [43].

![](/api/attachments/3ZKNVFYP/fulltext/images/98be4f2d848c0c92fe49865ef32055e34b091fd644895a9adaf1c04546c2103d.jpg)  
Fig. 3. Modified protocol of Ohkubo, Suzuki, and Kinoshita [43].

## 2.3. Protocol of Henrici and Müller [22]

Unlike the previous two protocols, this protocol (Fig. 4) keeps track of its session number (sn). Upon receiving the request from the reader, the tag increases its session number by one and sends the hash of its ID, a conjunction of its ID and session number, and Δsn which is the difference between its current and previous session numbers. Here, h(ID) is used to identify the tag and (h(ID) ○ sn) is used to prevent replay attack since it changes every time the tag is read. Δsn, which has a value of 1 if the previous transaction was a legitimate one between the tag and reader and not an adversary, is used by the reader to compute the current session number.

Avoine and Oechslin [2] find several scenarios under which this protocol can be compromised including attack based on the non-randomness of transmitted information, refreshment avoidance, and database desynchronization. An adversary can use the non-randomness of Δsn (=1 under normal conditions) to abnormally increase sn (and, Δsn) and later identify this tag by recognizing its unusually high Δsn value. The attack based on refreshment avoidance is due to the fact that refreshment of ID value in the tag is based on signal received from outside (here, the reader). The adversary can use this to its advantage. The attack based on database desynchronization, assuming ○ is the XOR operator (⊕), the adversary can replace r (in the third message) by a null bit string and thus h(r ○ sn ○ ID) by h(sn ○ ID). Here, the adversary can obtain h(sn ○ ID) by eavesdropping the second message of the current round. The tag does not realize the attack and updates its new ID (=0 ⊕ ID) as well as sn. In the next round, the tag and database will be desynchronized and it will never again send the third message to the tag to refresh the tag's identifier. I.e., the tag will be traceable from then on. Dimitriou [13] also notes this possible attack using k.

## 2.4. Protocol of Molnar and Wagner [44]

In the protocol proposed by Molnar and Wagner [44], both the reader and tag share a secret (x). A sketch of the algorithm is given in Fig. 5. Both reader and tag generate random nonces $( r _ { \mathrm { A } } , \ r _ { \mathrm { B } } )$ and share them. By refreshing the random nonces during every instantiation of the protocol, replay attacks through eavesdropping are avoided.

## 2.5. Protocol of Tsudik [37]

One of the recent single round protocols is that of Tsudik [37]. It uses monotonically increasing timestamps to provide tag authentication (Fig. 6). The tag, reader, and the back-end server share a common secret that is different for each tag. The protocol begins when the reader sends the current timestamp (TS′) to the tag. The tag checks to see if this new timestamp is newer than the previous timestamp it had processed from the reader (TS) and also if the new timestamp is greater than $\mathrm { T S } _ { \mathrm { m a x } } .$ . If these are untrue, the tag just uses a pseudo random number generator to generate an l-bit random number (H). Otherwise, it records the new timestamp and computes the hash value (H) of the new timestamp with the secret key (x). H is then sent to the reader which sends it to the server for validation.

Tsudik [37] identifies two drawbacks of this protocol: it is susceptible to denial of service (DoS) attack when an adversary sends an inaccurate timestamp and incapacitates the tag either temporarily or permanently; since the tag assumes that it is not authenticated more than once within a short duration of time. Depending on the time granularity, the tag could mis-identify a valid request from a reader as invalid.

Another vulnerability (replay attack) also arises due to usage of just timestamps for authentication. An adversary can send a series of some future timestamps to the tag and record its responses. When the times in these timestamps eventually become true, it can respond to requests from the reader appropriately without the tag being present.

![](/api/attachments/3ZKNVFYP/fulltext/images/ae0580e7387a865c8f32940cedf0c641d783b265667268ae5012f59469defbf9.jpg)  
Fig. 4. Protocol of Henrici and Müller [22].

![](/api/attachments/3ZKNVFYP/fulltext/images/9bce9713ed8c6efda2c874e88d23e1cff9f5b93f70235723520ffcfc3e5c0991.jpg)  
Fig. 5. Protocol of Molnar and Wagner [44].

## 2.6. Protocol of Lee, Asano, and Kim [45]

The protocol of Lee, Asano, and Kim [45] uses both XOR and hash chains to authenticate tags and readers (Fig. 7). The secret key (x) is shared between the tag and the back-end server. An adversary eavesdropping on the conversation among the tag, reader, and back-end server will not be able to recover any identifying information since all the messages passed appear to be random. For example, $r _ { \mathrm { B } }$ is generated using two random values (s and $r _ { \mathrm { A } } )$ and $r _ { \mathrm { C } } ^ { \prime }$ is generated using two random values as well (s and $r _ { B } )$ . The authors claim that, because of these seemingly random values being passed as messages, an adversary will not be able to violate the privacy and secrecy of this protocol. This protocol also prevents database desynchronization by maintaining the secret key from the previous and current authentication rounds. If an adversary intercepts the fifth message $( r _ { \mathrm { C } } ^ { \prime } )$ between the reader and tag, it can prevent the tag from updating its secret. However, the back-end server has already updated its secret. This could cause database desynchronization were it not for stored secret key from the previous authentication process. The back-end server therefore uses its previously stored secret for the next authentication round to authenticate the valid tag.

Although the messages passed seem random, an active adversary has some control over some of the messages being passed. For example, the adversary can block the first message s and send an l-bit null vector as s to the tag. The tag now computes $r _ { \mathrm { B } }$ as $h ( r _ { \mathrm { A } } \oplus x \oplus 0 )$ $h ( r _ { \mathrm { A } } \oplus x )$ . Next, the adversary can modify $r _ { \mathrm { A } } \mathrm { t o } \left( r _ { \mathrm { A } } \oplus s \right)$ and send it to the reader. When the back-end server computes $r _ { \mathrm { B } } = h ( ( r _ { \mathrm { A } } \oplus s ) \oplus x \oplus s ) = h ( r _ { \mathrm { A } } \oplus x )$ from $( s , \ ( r _ { \mathrm { A } } \oplus s ) , \ r _ { \mathrm { B } } )$ it receives from the reader, it would not be able to detect the adversary modified messages. The adversary can also send a random $r _ { \mathrm { C } } ^ { \prime }$ to the tag as the fifth message. The tag will not update its key since $r _ { \mathrm { C } } ^ { \prime } \neq r _ { \mathrm { C } } .$ . The adversary can then impersonate the tag by always sending $( r _ { \mathrm { A } } \oplus s , \ h ( r _ { \mathrm { A } } \oplus x ) )$ to the reader. This attack can be prevented if the reader has some mechanism to detect repetition of same messages from the tag. However, it is also possible that the adversary only needs to use this attack once (e.g., to replace an expensive item by a cheap item during check-out) to be successful.

## 2.7. Protocol of Yang, Park, Lee, Ren, and Kim [41]

In a majority of RFID reader/tag authentication protocols, the communication channel between the reader and back-end server is assumed to be secure while that between the reader and tag is assumed to not be secure. Unlike other RFID authentication protocols discussed so far, the communication channels between tag and reader as well as reader and back-end server are not assumed to be secure in the protocol proposed by Yang et al. [41]. A sketch of their protocol is provided in Fig. 8.

![](/api/attachments/3ZKNVFYP/fulltext/images/edc6b2e61c16efcb363219953daa18d20b0150d511fe363d3a88c3fd7f730186.jpg)  
Fig. 6. Protocol of Tsudik [37].

![](/api/attachments/3ZKNVFYP/fulltext/images/bd07ee22570306117bc7c420f551b5fb04a0fb4658d9cd0ea08e481a2d741d55.jpg)  
Fig. 7. Protocol of Lee, Asano, and Kim [45].

The tag and the back-end server share two secrets $( x _ { 1 } ,$ $x _ { 2 } )$ , while the reader and the back-end server share a secret key (k). Each authentication process has its own freshly generated random bit vectors $( r _ { \mathrm { A } } , r _ { \mathrm { B } } )$ to prevent replay attacks. According to the authors, the random nonce generated by the reader $( r _ { \mathrm { A } } )$ is randomized further using keyed one-way hash function $( h _ { k } ( r _ { \mathrm { A } } ) )$ to prevent man-in-the-middle attack. The purpose of A is to verify a legitimate reader through S and also to prevent forgery using ID values by passive eavesdropping. These As are also randomized during every authentication process using the shared secrets $( x _ { 1 } , x _ { 2 } )$

Although the authors randomize all the messages to prevent attacks, an adversary can still track tags as follows: An adversary first sends S = 0 to the tag and saves the reply $A \ ( = h ( x _ { 1 } \oplus 0 \oplus \mathrm { I D } ) = h ( x _ { 1 } \oplus \mathrm { I D } ) )$ sent by the tag in return. Instead of $A ^ { \prime }$ (the fifth message in this protocol), the adversary sends some random l-bit vector to the tag. Since this is invalid, the tag does not update its secrets $( x _ { 1 } , x _ { 2 } )$ . By keeping track of all future communications between the reader and tags, the adversary can track a tag of interest. This can be done as follows: In-between every authentic communication between the reader and the tag, the adversary queries the tag (with $S { = } 0 )$ and retrieves the current value of A. The adversary then sends the last saved $A ^ { \prime }$ as S to the tag, initiating a new authentication process. Let $x _ { 1 } ^ { a }$ and $x _ { 1 } ^ { b }$ be the afterand before- updating values of $x _ { 1 }$ respectively. The tag computes A $( = h ( x _ { 1 } ^ { a } \oplus A ^ { \prime } , \oplus \mathrm { I D } ) = h ( ( x _ { 1 } ^ { b } \oplus A ^ { \prime } ) \oplus A ^ { \prime } \oplus \mathrm { I D } ) =$ $h ( x _ { 1 } ^ { b } \oplus \mathrm { I D } ) )$ and this is exactly the same A that was stored by the adversary from an earlier authentication process. The adversary can use this to track a tag.

Since the channel between the reader and the backend server is not secure, an adversary can also completely bypass the reader as follows: The adversary can send $S { = } 0$ to the tag and send $( A , 0 , r _ { \mathrm { A } } )$ to the back-end server, which validates it. The adversary can then disregard $h _ { k } ( S ) [ \operatorname { D A T } A ]$ from the back-end server and send just the $A ^ { \prime }$ part of the fourth message (from the back-end server to the reader) to the tag.

![](/api/attachments/3ZKNVFYP/fulltext/images/3b7abc4e20371878630e066ee899c6fe492aa17a9055990c640347397c879760.jpg)  
Fig. 8. Protocol due to Yang, Park, Lee, Ren, and Kim [41].

## 3. Multiple round protocols for single tag: HB and its variants

These are variants of the HB protocol proposed by Hopper and Blum [24]. The HB protocol is based on the hardness of the LPN (Learning Parity with Noise) problem, hence is deemed secure to the extent the related LPN problem is secure. Blum, Kalai and Wasserman provide the best known algorithm for solving LPN that requires a runtime of $2 ^ { \overline { { \mathrm { O } } } \left( \frac { k } { \log k } \right) }$ [5]. Earlier, several instances of the LPN problem presented by DIMACS were solved by brute force algorithms by several researchers (e.g., Greentech Computing, [17] using propositional logic; Warners and van Maaren, 1998 using an extension of a variant of Davis-Putnam algorithm published in [10]). Warners and van Maaren [38] solved the LPN problem for keylength k=32 in about 5 minutes. Juels and Weis [26] estimate the runtime required for the problems presented by DIMACS to be in the order of $2 ^ { 2 4 }$ using the algorithm presented in Blum et al. [5]. They also estimate that for a keylength of 160, the runtime would be in the order of $2 ^ { 6 4 }$

Although this protocol works well under most circumstances where passive adversaries exist, an active adversary can break its secureness. Juels and Weis [26] modified HB to include protection against active attacks from adversaries. However, this (HB<sup>+</sup>) too was not completely secure under certain circumstances [16]. Bringer et al. [8] later modified $\mathrm { H B } ^ { + }$ to secure it against active attacks from adversaries as described in Gilbert et al. [16]. We show that the protocols $\mathrm { \left( H B ^ { + + } \right. }$ and $\mathrm { H B } ^ { + + }$ [first attempt]) presented in Bringer et al. [8] are vulnerable to active attacks, and present a modified solution.

We briefly describe and evaluate HB and its variants in this section. After providing a brief introduction to the protocols, we consider some security violations that may occur and discuss possible remedies that were provided in the literature. We then propose modifications to $\mathrm { H B } ^ { + + }$ a recent variant of HB.

## 3.1. HB

An overview of a round of HB protocol is given in Fig. 9. Here, $r _ { \mathrm { A } } \cdot x$ and $r _ { \mathrm { A } } \oplus x$ represent scalar product and exclusive- or (XOR) of k-bit binary vectors $r _ { \mathrm { A } }$ and x respectively. The HB protocol relies on the computational hardness of Learning Parity with Noise (LPN) problem, and not on classical symmetric key cryptography solutions [8]. It is meant only to be secure against passive attacks, and it is not secure against active attacks. The round given in ηr times. A simple active attack where an adversary pretending to be the reader transmits a fixed $r _ { \mathrm { A } }$ to the tag several times can retrieve the value of x.

![](/api/attachments/3ZKNVFYP/fulltext/images/e62d0fa5b2f5da46c89700e572487b66224e2f844a3a1926b64a30b87cbb18ae.jpg)  
Fig. 9. A round of HB protocol [24].

## 3.2. HB<sup>+</sup>

Juels and Weis [26] modified the HB protocol and showed the modified protocol (HB<sup>+</sup>) to be secure against active attacks. A round of $\mathrm { H B } ^ { + }$ is given in Fig. 10. They introduced another k-bit vector secret key ( y) that is shared between the reader and a tag. They also modified the HB protocol such that the tag, and not the reader, initiates the authentication process. The tag first transmits a k-bit blinding vector to the reader. The other modification is in the way z is computed. A scalar product of the newly introduced secret key ( y) and the blinding vector $\left( r _ { \mathrm { B } } \right)$ is XOR-ed with the z in HB.

Although Juels and Weis [26] showed $\mathrm { H B } ^ { + }$ to be secure against active attacks, Gilbert et al. [16] showed that $\mathrm { H B } ^ { + }$ is not secure against a simple man-in-themiddle attack that was not considered in former. A description of this attack is given in Fig. 11. Here, the adversary is assumed to be capable of manipulating challenges sent by a legitimate reader to a legitimate tag during the authentication process. The adversary is also assumed to have the capability to recognize when an authentication procedure succeeds or fails. The core of the attack consists of manipulating the challenge sent by the reader $( \mathrm { i . e . , \ r _ { A } ) }$ by sending the XOR of $r _ { \mathrm { A } }$ and a constant k-bit vector $\delta$ to the tag on all r rounds of the authentication process. If the authentication succeeds, $\delta \cdot x { = } 0$ with a high probability. If the authentication fails, $\delta \cdot x = 1$ with a high probability. Here, an adversary can manipulate δ to reveal each bit of the secret key x one by one. The protocol can be repeated k times to retrieve all bits of the secret key x.

Once x is identified, the adversary can impersonate the tag and send a given blinding vector $r _ { \mathrm { B } }$ to the reader. In return to the reader's response, the adversary can transmit $r _ { \mathrm { A } } \cdot x$ to the reader. When authentication succeeds, the adversary knows that $r _ { \mathrm { B } } \cdot y { = } 0$ with high probability. On the other hand, if authentication fails the adversary knows that $r _ { \mathrm { B } } \cdot y { = } 1$ with high probability. Using these, the adversary is able to derive the other secret key y. When both the secret keys $( x , \ y )$ are revealed to the adversary, the privacy of this tag is under threat.

![](/api/attachments/3ZKNVFYP/fulltext/images/d6bd9cd8e6b8766fd21f2c6cbae3c820d0c6125a62222e6fe58f6758985cb1e8.jpg)  
Fig. 10. A round of HB<sup>+</sup> protocol [26].

The $\mathrm { H B } ^ { + }$ protocol is not secure against another form of attack from an adversary who pretends to be a valid tag reader. Here, the adversary is assumed to have the capability to intercept all communication between a tag and a reader, and the ability to block transmission of any communication from the tag to the reader. The adversary is also assumed to be capable of transmitting $r _ { \mathrm { A } }$ to the tag before the tag can initiate the next round with a new $r _ { \mathrm { B } }$ value. That is, the reader repeatedly transmits $r _ { \mathrm { A } }$ to the tag, keeping it busy computing zs. The following should also work with different $r _ { B } \mathrm { s }$ during different rounds of the protocol for small values of $k ,$ given that the Learning Parity with Noise (LPN) problem is known to be NP-hard [4].

When the authentication process begins as the tag sends $r _ { \mathrm { B } } ,$ the adversary intercepts it and transmits $r _ { \mathrm { { A } } } { = } 0$ to the tag. The tag then computes z $\left( = \boldsymbol { r } _ { \mathrm { B } } \cdot \boldsymbol { y } \oplus \nu \right)$ and transmits it to the reader, which in this case is the adversary. The process can be repeated enough number of times until r ·y is retrieved. Since $r _ { \mathrm { B } }$ is known to the adversary, y can be inferred. Knowing $r _ { \mathrm { A } } , r _ { \mathrm { B } } ,$ and $y ,$ the process can be repeated until x is identified. The adversary takes advantage of the fact that communication between the tag and the reader is controlled by the reader – i.e., when the authentication succeeds, the protocol ends. Since the adversary is the reader during this attack, it can continue with as many rounds of the protocol as is necessary until it succeeds in identifying the secrets $( x , y )$

In the effective attack against $\mathrm { H B } ^ { + }$ proposed by Gilbert et al. [16], the tag and reader are authenticated by the time the secrets are known to the adversary. It is possible that this tag, once authenticated, may leave the “system” and would no longer interact with any reader. Under these circumstances, the attack presented in the previous two paragraphs has an edge since it happens without any interaction between tag and reader.

## 3.3. HB<sup>++</sup>[first attempt] and $H B ^ { + + }$

In response to Gilbert et al. $\therefore \mathrm { \Omega s }$ [16] attack on $\mathrm { H B } ^ { + }$ Bringer et al. [8] proposed two protocols $( \mathrm { H B } ^ { + + } [ \mathrm { f i r s t }$ attempt] (Fig. 12) and $\mathrm { H B } ^ { + + } \ ( \mathrm { F i g . } \ 1 3 )$ that secures against such man-in-the-middle attacks. However, these protocols are still not immune to attacks from adversary that pretends to be an authentic reader. $\mathrm { H B } ^ { + + }$ [first attempt] was shown to not be immune to attacks in Bringer et al. [8].

Another vulnerability arises from the fact that the protocols $\mathrm { H B } ^ { + + }$ and $\mathrm { H B } ^ { + + }$ [first attempt] contain z as in $\mathrm { H B } ^ { + }$ , and this z can be used to identify the secrets x and y. This is a vulnerability since the adversary can track the tag knowing only z. The adversary can easily compute z using a man-in-the-middle attack [16] or by pretending to be a valid reader as discussed earlier in this section. Ignoring the possibility of this attack, the adversary still needs to identify the other two secrets $( x ^ { \prime } , y ^ { \prime } )$ . Here, the adversary is assumed to have the capability to receive transmissions from the tag and block these transmissions from reaching the reader. The adversary can manipulate $r _ { \mathrm { A } }$ to its advantage to retrieve the secret keys $( x ^ { \prime } , \ y ^ { \prime } )$ . Initially, the adversary can transmit $r _ { \mathrm { { A } } } { = } 0$ to determine $f ( r _ { \mathrm { B } } ) \cdot y ^ { \prime }$ . Once this is accomplished, the adversary can set $r _ { \mathrm { { A } } } { = } 1$ to determine $1 \cdot x ^ { \prime } \oplus f ( r _ { \mathrm { { B } } } ) \cdot y ^ { \prime }$ . The adversary can then identify the secret $x ^ { \prime }$ from $f ( r _ { \mathrm { { B } } } ) \cdot y ^ { \prime }$ and $1 \cdot x ^ { \prime } \oplus f ( r _ { \mathrm { { B } } } ) \cdot y ^ { \prime }$

![](/api/attachments/3ZKNVFYP/fulltext/images/aabf75ed27b22f02f41d5806a110f9ed7ccff4dba5bcfdd68a088ad75788fc1c.jpg)  
Fig. 11. The attack on a round of HB<sup>+</sup> protocol [16].

![](/api/attachments/3ZKNVFYP/fulltext/images/981968d6566a5e22094b1ce50726dbb2f063fc1f7db579cf121b958caa30bd21.jpg)  
Fig. 12. A [first attempt] round of HB<sup>++</sup> protocol [8].

During the next several rounds of the protocol, the adversary can assign $r _ { A } = r _ { B }$ and determine $f ( r _ { \mathrm { B } } ) \cdot ( x ^ { \prime } \oplus y ^ { \prime } )$ . Knowing this, $f ( r _ { \mathrm { B } } ) \cdot y ^ { \prime }$ , and $x ^ { \prime }$ , the adversary can determine $y ^ { \prime } .$

Bringer et al [8] modified $\mathrm { H B } ^ { + } [ \mathrm { f i r s t }$ attempt] to rectify a vulnerability they identify and propose $\mathrm { H B } ^ { + + }$ (Fig. 13) that has protection against these vulnerabilities. However, $\mathrm { H B } ^ { + + }$ too is prone to a similar attack where an adversary pretends to be a valid reader. Here, again, z can be used to retrieve the secrets x and y as in $\mathrm { H B } ^ { + }$ . To retrieve the other two secrets $( x ^ { \prime } , y ^ { \prime } )$ , we make the following assumption: $\rho$ is updated only once during a round, and a round for this purpose is defined as beginning with transmission of $\dot { r } _ { \mathrm { B } }$ by the tag and ending with the checking of z and $z ^ { \prime }$ by the reader. Updates to $\rho$ probably occur at the beginning of each round [8]. However, a fast adversary can communicate with the tag several times in-between two successive transmissions of $r _ { \mathrm { B } }$ by the tag.

As long as $r _ { \mathrm { B } }$ and $\rho$ remain constant when the adversary is communicating with the tag, the following would help reveal the other two secrets $( x ^ { \prime }$ and $y ^ { \prime } )$ . The adversary is assumed to have the capability to intercept $r _ { \mathrm { B } }$ transmitted by the tag and to prevent $r _ { \mathrm { B } }$ from reaching the reader. The adversary can manipulate $r _ { \mathrm { A } }$ to its advantage to retrieve the secret keys $( x ^ { \prime } , y ^ { \prime } )$ . Initially, the adversary can transmit $r _ { \mathrm { { A } } } { = } 0$ to determine rot( $f ( r _ { \mathrm { B } } ) , \rho ) \cdot y ^ { \prime } .$ . Once this is accomplished, the adversary can set $r _ { \mathrm { { A } } } { = } 1$ to determine $1 \cdot x ^ { \prime } \oplus \mathrm { r o t } ( f ( r _ { \mathrm { { B } } } ) , \rho ) \cdot y ^ { \prime }$ . The adversary can then identify the secret $x ^ { \prime }$ from rot $f ( r _ { \mathrm { B } } ) , \rho ) \cdot y ^ { \prime }$ and $1 \cdot x ^ { \prime } \oplus$ rot $( f ( r _ { \mathrm { B } } ) , \rho ) \cdot y ^ { \prime }$

During the next several rounds of the protocol, the adversary can assign $r _ { \mathrm { A } } { = } r _ { \mathrm { B } }$ and determine rot( $f ( r _ { \mathrm { B } } ) { \mathrm { . } }$ $\rho ) \cdot ( x ^ { \prime } \oplus y ^ { \prime } )$ . Knowing this, $\mathrm { r o t } ( f ( r _ { \mathrm { { B } } } ) , \rho ) \cdot y ^ { \prime }$ , and $x ^ { \prime } ,$ the adversary can determine $y ^ { \prime }$

## 3.4. Proposed modifications to $H B ^ { + + }$

In order to maintain the proofs of security for the adversary model presented in Juels and Weis [26], the proposed modifications keep the crux of $\mathrm { H B } ^ { + }$ intact (Fig. 14). The main modifications are as follows:

• Removal of z and related vectors $( x , y )$ and ν. This is to prevent attack mentioned earlier. A side effect of this keeps the protocol ‘lightweight.

• Update ρ every time z is computed. This is to prevent usage of the same $\rho$ before initiation of the next round from the tag's end.

![](/api/attachments/3ZKNVFYP/fulltext/images/8dd8c7f92c12cb48ab4bbc9d8dcc706ad055716c95fa6d966929c699a7165e07.jpg)  
Fig. 13. A round of HB<sup>++</sup> protocol [8].

![](/api/attachments/3ZKNVFYP/fulltext/images/2d301349d27a3d28d27d08018897a1bdb583c69f0561f65a8ab8c325d5ccee8d.jpg)  
Fig. 14. A round of Modified HB<sup>++</sup> protocol.

The first modification (removal of z and its related vectors) prevents the tag from being tracked since it is relatively easy to determine z as compared to $z ^ { \prime } .$ The second modification renders $z ^ { \prime }$ more secure since it is difficult to determine z when $\rho$ changes every time $z ^ { \prime }$ is computed.

## 3.5. Security analysis

Following Dimitriou [13], we present a brief security analysis on the proposed modifications to $\mathrm { H B } ^ { + + }$

## 3.5.1. Attack on a tag

This type of attack refers to the scenario where an adversary pretends to be the reader. Since the protocol is based on avoiding exactly this type of attack, it is hoped that the adversary will not be able to succeed.

## 3.5.2. Attack on the reader

Here, the adversary pretends to be a valid tag. This type of attack will not succeed because of the shared secret keys $( x ^ { \prime }$ and $y ^ { \prime } )$ .

## 3.5.3. Attack on the communication between tag and reader

An adversary can block messages between the reader and a tag. When this happens, the authentication process is broken and it doesn't succeed. Repeated interactions, either blocking transmissions or through man-in-themiddle attacks, leaves the door open for an adversary to learn the secret keys.

## 3.5.4. Attack on user privacy

Since no ‘private’ information is transmitted during validation, this is of no concern here.

## 3.5.5. Attack on location privacy

This is of concern since the secrets do not change over different runs of the protocol.

## 3.5.6. Attack against the key

This happens when an attacker listens in on the transaction and tries to identify the key values. Again, if the keys are selected appropriately (e.g., [31]), this is not of concern.

## 3.5.7. Attack against implementation

Provided the keys and the random numbers are generated with caution, this is not of concern.

## 3.5.8. Disassembling the tags

These tags are clearly not tamper-resistant, and can be disassembled to retrieve the structure of $\cdot _ { z ^ { \prime } }$ as well as the secret keys $( x ^ { \prime } , y ^ { \prime } )$

## 4. Single round protocols for multiple tags

These protocols address a specific scenario involving RFID tag applications, namely the case where simultaneous presence of two tags in a reader's field is to be proved. This has been studied by Juels [25] and Saito and Sakurai [35]. Example scenarios where this is relevant are the need for certain medications to be dispensed together with an appropriate leaflet, the need for two parts to leave a factory together, and generally any situation that dictates the combined presence of two entities [25].

This section is organized as follows: we present an overview of related work and provide a brief evaluation of these in the next subsection. We also observe conditions under which these proofs could be compromised. In Section 4.2, we provide a brief discussion on “yoking” and “grouping” proofs. In Section 4.3, we describe the proposed proof for two tags addressing some of the concerns discussed in Sections 4.1 and 4.2. In Section 4.4, we describe the extension to the proposed proof to cover several (N2) tags. This is followed by brief security analysis of the proposed proof in subsection 4.5.

![](/api/attachments/3ZKNVFYP/fulltext/images/faa081fdef2000af4ef606db555b9061dfda9f15078ed7d1d97b9f428ccaff4a.jpg)  
Fig. 15. “Yoking proof” for RFID Tags [25].

## 4.1. Related work

Juels [25] and Saito and Sakurai [35] present proofs for simultaneous presence of two RFID tags in reader's field. In this section, we consider each of these in turn. Specifically, in the next subsection, we describe the “yoking proof” [25] and its critique by Saito and Sakurai [35]. We then provide a brief discussion on “grouping proof” [35] in the following subsection. In a subsequent subsection, we show yet another complementary scenario where “yoking proof” is not immune to ‘replay attack.’ We show that the “grouping proof” too is not immune from ‘replay attack.

## 4.1.1. Yoking proof

Juels [25] presented the “yoking proof” (Fig. 15) for two tags $T _ { \mathrm { A } }$ and $T _ { \mathrm { B } }$ to be simultaneously scanned. Here, the reader interacts with the two RFID tags $( T _ { \mathrm { A } }$ and $T _ { \mathrm { B } } )$ and a back-end trusted server/verifier (V). The tags themselves cannot interact with each other, but only with the reader.

The tags $T _ { \mathrm { A } }$ and $T _ { \mathrm { B } }$ have secrets $x _ { \mathrm { A } }$ and $x _ { \mathrm { B } }$ respectively. The scenario begins when the reader sends a “left proof” to one of the tags indicating its role in the protocol. The ‘left’ tag reacts by generating and transmitting a random number $\left( r _ { \mathrm { A } } \right)$ . The reader forwards this along with “right proof” to the other (‘right’) tag. This tag generates the $\mathbf { M A C } \left( m _ { \mathrm { B } } \right)$ using $x _ { \mathrm { B } }$ on $r _ { \mathrm { A } } .$ . The secret keys $x _ { \mathrm { A } }$ and $x _ { \mathrm { B } }$ are known to the server. The second tag then transmits $m _ { \mathrm { B } }$ along with a randomly generated number $( r _ { \mathrm { { B } } } )$ . This random number is sent by the reader to $T _ { \mathrm { A } }$ , which then uses $x _ { \mathrm { A } }$ to generate MAC on $r _ { \mathrm { B } }$ resulting in $m _ { \mathrm { A } }$ . The tag $T _ { \mathrm { A } }$ then sends $m _ { \mathrm { A } }$ to the reader which assembles everything necessary for the proof $( P _ { \mathrm { A B } }$ ) and sends them to the back-end server for verification that the tags $T _ { \mathrm { A } }$ and $T _ { \mathrm { B } }$ were scanned together.

Saito and Sakurai [35] show how a ‘replay attack’ can be played against “yoking proof” (Fig. 16). Here, the authors separate the interactions between the reader and the tags $( T _ { \mathrm { A } }$ and $T _ { \mathrm { B } } )$ across time (represented by the horizontal lines across $T _ { \mathrm { A } }$ and $T _ { \mathrm { B } }$ in Fig. 16) and show that the interactions between the reader and the tag $T _ { \mathrm { A } }$ can be captured ahead of time and ‘replayed’ to tag $T _ { \mathrm { B } }$ at a later point in time.

Although interactions between the reader and $T _ { \mathrm { A } }$ can be captured earlier in time the interactions between the reader and tag $T _ { \mathrm { A } }$ are not completely independent of the interactions between the reader and the tag $T _ { \mathrm { B } } .$ . For example, although an adversary can generate and transmit a random number (r) to $T _ { \mathrm { A } } ,$ , the MAC generated by $T _ { \mathrm { A } }$ is not independent of the random number $r _ { \mathrm { B } }$ generated by the tag $T _ { \mathrm { B } }$ . Hence, when $P _ { \mathrm { A B } }$ is generated, there will be a mismatch between the random number r that is used by $T _ { \mathrm { A } }$ for $m _ { \mathrm { A } }$ and the random number $\left( r _ { \mathrm { B } } \right)$ generated by $T _ { \mathrm { B } }$ . This issue can be bypassed by submitting $r , r _ { \mathrm { A } } , m _ { \mathrm { A } } ,$ , and $m _ { \mathrm { B } }$ to the verifier (V) since the reader (here, the adversary) has complete control over the content of what is submitted to the verifier.

![](/api/attachments/3ZKNVFYP/fulltext/images/366dde81d18cddb0d04443f256367161c1d03e6d911ef22efa680095a2774f8c.jpg)  
Fig. 16. Replay attack against “yoking proof” [35].

![](/api/attachments/3ZKNVFYP/fulltext/images/683aa2af6396089a92a26e52a3276a4097561ee523e32b785b79a1b87879c57a.jpg)  
Fig. 17. “Yoking proof” using time stamp [35].

## 4.1.2. Grouping proof

Saito and Sakurai [35] present another proof (yoking proof with time stamp) which they call the “grouping proof” (Fig. 17) where “yoking proof”’s ‘replay attack can be avoided.

The grouping proof proceeds as follows: Initially, the reader sends TS, the time stamp, to both the tags. Tag $T _ { \mathrm { A } }$ (the ‘left’ tag) generates $m _ { \mathrm { A } }$ using its secret $( x _ { A } )$ on TS and transmits $m _ { \mathrm { A } }$ to the reader. The reader transmits this to the ‘right’ tag $( T _ { \mathrm { B } } ) _ { \mathrm { \Omega } }$ , which uses its secret $\left( x _ { \mathrm { B } } \right)$ on TS and $m _ { \mathrm { A } }$ to generate $m _ { \mathrm { B } }$ , which is then transmitted to the reader. The reader then assembles TS and $m _ { \mathrm { B } }$ to generate the proof $( P _ { \mathrm { A B } } )$

According to Saito and Sakurai [35], the reason TS was generated by V and used in the proof is to verify the time at which a given MAC was generated. Since these times are known, ‘replay attacks’ reusing these MACs can be prevented.

![](/api/attachments/3ZKNVFYP/fulltext/images/0eeb4bbde7e6bd3811d99346c4d01bbc929b5f295ccc45fd026b1a0189fde112.jpg)  
Fig. 19. Replay attack against “yoking proof” using time stamp.

## 4.2. Discussion on “yoking” and “grouping” proofs

In addition to the ‘replay attack,’ mentioned in Saito and Sakurai [35], that can be played out on “yoking proof,” there is yet another (complementary) scenario that falls prey to a similar ‘replay attack’ but on the other tag. For example, since $r _ { \mathrm { A } }$ is not used by tag $T _ { \mathrm { A } }$ after it is transmitted to the reader, any random number (r) can be used from this time on and the end result would not be different. I.e., we can capture the transmissions between the reader and tag $T _ { \mathrm { B } }$ and replay it in its absence to the other tag $( T _ { \mathrm { A } } )$ as shown in Fig. 18.

Similar to “yoking proof,” the “grouping proof” too is vulnerable to ‘replay attacks’ as given in Fig. 19. Here, an adversary (“Reader”) begins by repeatedly transmitting messages to the ‘left’ tag $( T _ { \mathrm { A } } )$ using several different time stamps from some later points in time. Various disparate combinations of (TS, $m _ { \mathrm { A } } )$ can be gathered in this manner. Then, at some later point in time when TS becomes true, the ‘replay attacks’ can be instantiated without the presence of $T _ { \mathrm { A } }$ . It is worth noting that, unlike “yoking proof,” the complementary scenario is not vulnerable to ‘replay attack.’ This is because $m _ { \mathrm { B } }$ is dependent on $m _ { \mathrm { A } }$ and therefore cannot be generated before generation of $m _ { \mathrm { A } }$ by the ‘left’ tag $( T _ { \mathrm { A } } )$ We use this principle in the modified proof presented in the next subsection. The fact that $P _ { A B }$ uses only $m _ { \mathrm { B } }$ (and not $m _ { A } )$ could also lead to other vulnerabilities.

![](/api/attachments/3ZKNVFYP/fulltext/images/19e4981ed43bcfeecc79c50bc9d26aab372ec47559bf921b92303d8629db2f8d.jpg)  
Fig. 18. Another replay attack against “yoking proof”.

![](/api/attachments/3ZKNVFYP/fulltext/images/d1333dd641a344fc1c0f86c576102405730efb6a7cd4c12a82003290e19b4b36.jpg)  
Fig. 20. Modified proof [2 tags].

We first present a modified proof for the simultaneous presence of two tags in the next subsection. In the following subsection, we show a possible extension of this proof to several (N 2) tags.

## 4.3. Modified proof — two tags

The proposed modified proof given in Fig. 20 is a variation of “yoking proof.” It uses a principle partially used in the “grouping proof,” as mentioned at the end of the previous section. The idea is to ensure that the inputs to a tag are based on parameters that are necessary for the other tag, and to create dependence of the tags on each other so that they cannot be processed separately in the proof without the presence of the other tag.

We assume that the reader authenticates itself with the back-end verifier before beginning the process of obtaining r from Vas well as when returning $P _ { A B }$ at the end of the process. Although this assumption by itself should provide a reasonable amount of support against attacks on the system, we disregard any such influence. While generating a proof, when a transmission of interest fails to reach its intended receiver, as evidenced by a lack of response within a pre-specified time limit, the transaction is cancelled and started all over again with a fresh r from V. Beyond this, the main differences of the proposed proof (vs. “yoking proof”) are as follows:

• The addition of a random variable (r) sent to both the tags from the verifier through the reader. This helps us keep track of the time duration between the initial transmission from the reader to the ‘left’ tag and final submission of $P _ { \mathrm { A B } }$ for verification by the verifier. The random variable r is also used as seed for generating $r _ { \mathrm { A } }$ and $r _ { \mathrm { B } }$ by the tags.

• The MAC generated by $T _ { \mathrm { B } }$ depends on both r and $r _ { \mathrm { A } } .$ . The use of $r _ { \mathrm { A } }$ in generating $m _ { \mathrm { B } }$ is crucial. Since $r _ { \mathrm { A } }$ is generated and used internally in $T _ { \mathrm { A } }$ for generating $m _ { \mathrm { A } }$ as well, an adversary cannot run ‘replay attack’ on either of the tags. Because r is generated by the verifier, the dependence on r for generating $m _ { \mathrm { B } }$ adds yet another layer of protection against attacks.

• The fifth transmission in the proof is $m _ { \mathrm { B } }$ instead of $r _ { \mathrm { B } }$ (as in “yoking proof”). This helps in the generation of $m _ { A }$

• The use of $m _ { \mathrm { B } }$ in generating $m _ { \mathrm { A } }$ is crucial since $T _ { \mathrm { A } }$ has to wait for $T _ { \mathrm { B } }$ to generate $m _ { \mathrm { B } }$ . Therefore, $T _ { \mathrm { A } } { } ^ {  ' } \colon$ s part of the proof cannot occur before $T _ { \mathrm { B } } \mathrm { ^ \bullet s }$ part and $T _ { \mathrm { B } } \mathrm { ^ \bullet s }$ part cannot happen independently since it too is dependent on input from $T _ { \mathrm { A } } ~ ( r _ { \mathrm { A } } ) . ~ T _ { \mathrm { A } }$ also generates $r _ { \mathrm { A } } ,$ which is kept internal $( \mathrm { i . e . }$ , it is not received as input from an outside entity). Hence it cannot be corrupted by an outside entity.

## 4.4. Modified proof — several ( N 2) tags

We discussed the case for proving the simultaneous presence of only two tags in the field of the reader. Depending on the context, it may be necessary to be able to account for the simultaneous presence of several tags. A possible extension would be to collapse the messages sent to tag $T _ { \mathrm { B } }$ into the reader and let the reader generate $m _ { \mathrm { B } _ { i } } ( i { = } 1 , . . . , n ,right.$ , where n is the number of tags of interest) values for each of the tags.

Fig. 21 provides a synopsis of the interactions between the reader and the ith tag (T ). The same r is transmitted by the reader to all n tags. In the end, $P _ { \mathrm { { A } } }$ is evaluated based on $r _ { 1 } , r _ { 2 } , . . . r _ { n } , r , m _ { 1 } , m _ { 2 } , . . . m _ { n }$

## 4.5. Security analysis

Following Dimitriou [13], we present a brief security analysis on the proposed proof for simultaneous scan of two RFID tags.

![](/api/attachments/3ZKNVFYP/fulltext/images/1788874a3bbbcc9967691e756e834816f4788a2018ec8cac58eef29de9a3d501.jpg)  
Fig. 21. Modified proof [N 2 tags].

## 4.5.1. Attack on a tag

This type of attack refers to the scenario where an adversary pretends to be the reader. Since the proof is based on avoiding exactly this type of attack, the adversary will not be able to succeed in completing the proof even if parts of the steps are violated.

## 4.5.2. Attack on the reader

Here, the adversary pretends to be a valid tag. This type of attack will not succeed because of the shared secret keys $( x _ { A }$ and $x _ { B } )$ . The adversary will not succeed with ‘replay attack’ either because each of the tags need fresh input from the other which changes every time the proof is run.

## 4.5.3. Attack on the communication between tag and reader

An adversary can block messages between the reader and tag(s). When this happens, the proof is broken and it doesn't succeed. The entire transaction is re-started with a fresh r from V. If the adversary continues to block messages between reader and tag(s), the proof will not succeed even though both the tags are simultaneously present in the field of the reader.

## 4.5.4. Attack on user privacy

Since no ‘private’ information is transmitted during the proof, this is of no concern here.

## 4.5.5. Attack on location privacy

Since data used in transmissions $( r , a , r _ { \mathrm { A } } , r _ { \mathrm { B } } , B , m _ { \mathrm { A } } ,$ and $m _ { \mathrm { B } } )$ are refreshed every time the proof is run and none of these are stored for future runs of the proof, location privacy is guaranteed.

## 4.5.6. Attack against the key

This happens when an attacker listens in on the transaction and tries to identify the key values. Again, if the keys are selected appropriately (e.g., [31]), this is not of concern.

## 4.5.7. Attack against implementation

Provided the keys and the random numbers are generated with caution, this is not of concern.

## 4.5.8. Disassembling the tags

These tags are clearly not tamper-resistant, and can be disassembled to retrieve MAC as well as xs. Even if this happens, due to the forward privacy of the proof, past transactions are secure.

## 5. Relay attacks

The ISO air-interface protocol (e.g., ISO 14443) requires the tags to be within about 4 inches from the reader. This, in principle, would deter adversaries operating in-between a tag and a reader. However, exploiting or circumventing a weakness in authentication protocols is not the only means to compromise an RFID tag enabled system. Relay attacks are one such attack that does not require physical proximity of a valid tag and reader. An adversary places two devices – a ghost (or proxy) and a leech (or mole) – between a tag and a reader. The ghost relays the reader's signal to the leech, which is in physical proximity to the tag. To the tag, the leech is a valid reader. The adversary then relays messages between the tag and reader without necessarily exploiting any weakness in the authentication protocol. Examples of scenarios that could fall prey to this type of vulnerability include RFID-enabled credit card, building access card, passport, etc.

Pervasive computing has motivated interest in systems that can precisely determine the location of a mobile device. The integrity and privacy of a locationproving system are important to prevent dishonest provers from falsifying location as well as to prevent adversaries from learning or mimicking privileged location information. Although one could verify location through use of GPS coordinates ( e.g., [11]), RFID tags do not lend themselves to such applications. Distance bounding protocols to prevent such distance fraud attacks can be broadly classified as two types, one based on measuring the signal strength and the other based on measuring the round-trip time between prover and verifier.

The proof based on measuring signal strength is not secure. An adversary can easily amplify signal strength as desired or use stronger signals to read from afar. For example, the maximum range of a Bluetooth device is about 10 meters which can be increased to about 100 m (328 ft) by increasing the power. John Hering [23] and his colleagues at Flexilis created the BlueSniper ‘rifle and used it to grab the phone book and text messages from a Nokia 6310i phone that was 1.1 miles away. This example illustrates that measuring signal strength does not prevent distance-based attacks. It has been shown that using only electronics hobbyist supplies and tools, a cheap (for about \$100) skimmer can be built that can read RFID tags from a distance longer than their typical range (e.g., [30,29]).

The proof based on measuring the round-trip time relies on the fact that no information can propagate faster through space-time than light [19]. The adversary under such a scenario can claim only to be farther away from its current location by delaying the response. Since we are dealing with very small numbers, the verifier must be capable of precisely measuring the round-trip time. For most practical purposes, this also implies that processing delay at the prover's end must be negligible compared to propagation delay between prover and verifier. In addition to simple distance fraud attacks, two other types of attacks have been identified under such scenarios: mafia (man-in-the-middle) fraud, and terrorist fraud attacks [12].

The mafia fraud attack is where the adversary consists of a cooperating rogue prover (T<sup>¯</sup>) and rogue verifier (R<sup>¯</sup>) where (T<sup>¯</sup>) interacts with the honest verifier (R) and (R<sup>¯</sup>) interacts with the honest prover (T) as follows: $R { - } \overbar { T } { - } \overbar { R } -$ T. That is, the adversary relays signals between the verifier and prover as if they were in close proximity to each other. Since the adversary does not modify any of the signal it receives, no amount of secure encryption could prevent these types of attacks. Brands and Chaum [7] presented a distance bounding protocol based on a series of rapid bit challenge-response iterations to determine the distance between the prover and the verifier based on round-trip times. The authenticity of the prover and verifier still needs to be done. Clearly, the prover needs additional hardware (e.g., gates, etc.) dedicated to this protocol.

The terrorist fraud attack is where a dishonest prover collaborates with the adversary to convince the honest verifier of its proximity. Here, although the prover and adversary cooperate, the adversary does not know the secret key of the prover. Clearly, if the adversary knows the secret key, it would be hard to distinguish it from the prover.

## 5.1. Protection against mafia attack

Hancke and Kuhn [19] study this problem in RFID tag/reader context and propose a protocol that is resistant against terrorist attacks (Fig. 22).

Both reader and tag share a common secret (x) in this protocol. After exchanging nonces $( r _ { \mathrm { A } } , \ r _ { \mathrm { B } } )$ , both reader and tag apply a pseudorandom one-way keyed hash function (h) to the concatenation of the nonces, and the resulting value is split into two n-bit strings $R ^ { 0 }$ and $R ^ { 1 }$ . The reader then generates a random k-bit string $C .$ This concludes the untimed phase. For the timed phase, the reader iteratively sends $C _ { i } ( i { = } 1 , . . . , n )$ to the tag. Depending on $C _ { i }$ the tag either sends $R _ { i } ^ { 0 }$ or $R _ { i } ^ { 1 }$ to the reader. The clock is started and stopped at the beginning $( t _ { i } )$ and end $( t _ { f } )$ of each iteration respectively. At the end of each iteration, $\Delta t { = } t _ { f } { - } t _ { i } { \le } \Delta t _ { \mathrm { m a x } }$ and $R _ { i }$ are verified.

This protocol is secure against mafia attack since the adversary cannot respond to the reader on time through a relay attack if the tag is indeed farther away from the reader. An adversary can try a man-in-the-middle attack by capturing $r _ { \mathrm { A } }$ from the tag and holding it while it tries to retrieve all $R ^ { 0 } ( \mathrm { o r } , R ^ { 1 } )$ values from the tag. The adversary then sends $r _ { \mathrm { A } }$ to the reader to facilitate the beginning of the timed phase of the protocol. The adversary can correctly reply all $\scriptstyle C _ { i } = R ^ { 0 ^ { - } } ( { \mathrm { o r } } \ R ^ { 1 } )$ cases 100% of the time $\begin{array} { r } { ( P = \frac { 1 } { 2 } ) } \end{array}$ since on an average about half the cases have $C _ { i } { = } 1$ and the other half have $C _ { i } { = } 0$ . In the other half of the cases, the adversary can guess the correct value of $R ^ { 1 } ( \mathrm { o r } R ^ { 0 } )$ about half the time $\textstyle ( P = { \frac { 1 } { 4 } } )$ Therefore the probability that a mafia fraud attacker makes the reader falsely accept is bounded by $\left( { \frac { 3 } { 4 } } \right) ^ { n } [ 1 9 ]$

There is no strong cryptographic relationship between the different (timed and un-timed) phases. That is, the verifier cannot verify that the parties taking part in these phases are indeed the same. Therefore Hancke and Kuhn's protocol is not immune to terrorist fraud attack since the tag can cooperate with an adversary to falsify its location. Note that knowing $R ^ { 0 }$ and $R ^ { 1 }$ , the adversary cannot know the secret (x).

![](/api/attachments/3ZKNVFYP/fulltext/images/6f6ce056e765ce4a4e9ae9ac6ab04e8180d969be4200eac7c213afa54577f5cc.jpg)  
Fig. 22. Distance-bounding protocol due to Hancke and Kuhn [19].

## 5.2. Protection against terrorist fraud attack

Reid et al. [32] propose a modification to the distance bounding protocol proposed by Hancke and Kuhn [19] to prevent terrorist fraud attacks (Fig. 23).

They add the identity of the tag and reader in both the messages as well as in the key derivation function (KDF). Instead of $R ^ { 0 }$ and $R ^ { 1 }$ as in Hancke and Kuhn [19]'s protocol, Reid et al. use key k and ciphertext c where knowing k and c is tantamount to knowing x. Therefore the tag does not share k and c with an adversary. Reid et al. [32] claim this protocol to be immune to both mafia and terrorist attacks and provide the probability that the reader accepts the tag as authentic to be $\left( { \frac { 3 } { 4 } } \right) ^ { n }$

However, an adversary can certainly improve on this probability since $\left( { \frac { 3 } { 4 } } \right) ^ { t h }$ of the input to KDF can be controlled by the adversary as follows: The adversary captures $( \mathrm { I D } _ { T } , r _ { \mathrm { A } } )$ from the tag to the reader and delays sending this. The adversary then retrieves all c values from the tag by sending it a stream of $C _ { 1 } { = } 0$ for the “timed phase.” After this, the adversary can basically take over the role of the reader and send the same combination of $( \mathrm { I D } _ { R } , r _ { \mathrm { B } } )$ to the tag and capture all the k values this time. Since the only variable now is $r _ { \mathrm { A } }$ , k probably changes only $\textstyle { \frac { 1 } { 4 } }$ of its bits across different rounds. The adversary can take a majority vote and approximately guess k. Now, knowing (c, k[approximately 0.75]), the adversary can replay these values to the reader. The probability now becomes $\left( { \frac { 7 } { 8 } } \right) ^ { n }$ . Although it is still hard to render the protocol to not be immune to these attacks, the probability of success for an adversary is higher with the Reid et al. [32] protocol than with the Hancke and Kuhn [19] protocol.

![](/api/attachments/3ZKNVFYP/fulltext/images/69ebd54775107abc6c82017fcfe75140796729288d3ea0d331059ba929b7e7df.jpg)  
Fig. 23. Distance-bounding protocol due to Reid et al. [32].

## 6. Discussion and conclusion

We provided an overview of several protocols that have been proposed over the past few years for RFID tag/reader authentication. Since the field is still evolving, there are ample opportunities for improving currently available protocols. We considered a few “streams” of research under the general rubric of RFID tag/reader authentication protocols with a few examples from each. We also identified vulnerabilities in some of the existing protocols and extended some to avoid specified vulnerabilities.

We considered the single-round protocols for authenticating single tags with several examples of existing protocols. We presented the protocols and discussed security threats identified by other researchers. We also identified further threats that could violate privacy/ security of these tags/readers.

We then discussed and evaluated multiple-round protocols, especially HB and its variants for RFID tag/ reader authentication. In addition to the security compromises that have been mentioned in the literature, we provided yet another security compromise that can occur due to an adversary pretending to be a valid reader. This threat is worse since the valid reader is not involved when the adversary interacts with the tag to identify the secret keys. We also showed the vulnerability of a recent variant of HB $\mathrm { ( H B ^ { + + } ) }$ ), and presented a means to avoid this vulnerability. Although the proposed method is not secure against all types of attack by an adversary, it is reasonably secure against those that were considered while maintaining the ‘lightweight characteristic of the protocol.

We also evaluated the two proofs that have been proposed thus far in the literature for ascertaining the simultaneous presence of two RFID tags in the field of the reader. We showed that both these proofs have minor areas of concern, and proposed a means to address these concerns using minimal processing for tags that cannot execute standard cryptographic primitives. We also provided brief security analysis of the proposed proof.

Finally, we considered relay attacks and the two protocols that have been proposed in an RFID tag/reader context. We discussed the distance bounding proofs due to Hancke and Kuhn [19] and Reid et al. [32] and showed that the latter is also not completely immune from terrorist fraud attacks.

Authentication protocols for RFID tag/reader are important both for secure implementations as well as for allaying consumers' concerns with regard to their privacy/security in environments involving RFID tags. Having gained interest from researchers and industry alike over the past few years, this field is still very much in its infancy. Given the importance of security/privacy and the constant vulnerabilities faced by most such authentication protocols, it is of paramount importance to proactively stay current on possible new threats to security/privacy.

## References

[1] G. Avoine, Radio frequency identification: adversary model and attacks on existing protocols, Technical Report LASEC-RE-PORT-2005-001, September 2005.

[2] G. Avoine, P. Oechslin, RFID traceability: a multilayer problem, Financial Cryptography - FC'05, LNCS, Springer 2005.

[3] G. Avoine, E. Dysli, P. Oechslin, Reducing Time Complexity in RFID Systems, Proceedings of the 12th Annual Workshop on Selected Areas in Cryptography (SAC'05), 2005, pp. 291–306.

[4] E.R. Berlekamp, R.J. McEliece, V. Tilborg, On the inherent intractability of certain coding problems, IEEE Transactions on Information Theory IT-24 (1978) 384–386.

[5] A. Blum, A. Kalai, H. Wasserman, Noise-tolerant learning, the parity problem, and the statistical query model, Journal of the ACM 50 (4) (July 2003) 506–519.

[6] S. Bono, M. Green, A. Stubblefield, A. Juels, A. Rubin, M. Szydlo, Security Analysis of a Cryptographically-Enabled RFID Device, Procedings of the 14th USENIX Security, 2005, pp. 1–16.

[7] S. Brands, D. Chaum, Distance-bounding protocols, Advances in Cryptology — EURO-CRYPT'93, Lecture Notes in Computer Science, vol. 765, 1994, pp. 344–359.

[8] J. Bringer, H. Chabanne, E. Dottax, HB<sup>++</sup>: a lightweight authentication protocol secure against some attacks, IEEE International Conference on Pervasive Services, Workshop on Security, Privacy and Trust in Pervasive and Ubiquitous Computing — SecPerU, 2006.

[9] C. Castelluccia, G. Avoine, Noisy tags: a pretty good key exchange protocol for RFID tags, International Conference on Smart Card Research and Advanced Applications — CARDIS, Lecture Notes in Computer Science, vol. 3928, 2006, pp. 289–299.

[10] M. Davis, H. Putnam, A computing procedure for quantification theory, Journal of the ACM (1960) 201–215.

[11] D.E. Denning, P.F. MacDoran, Location-based authentication: grounding cyberspace for better security, Computer Fraud and Security 1996 (2) (1996) 12–16.

[12] Y. Desmedt, Major Security Problems with the ‘Unforgeable’ (Feige)-Fiat-Shamir Proofs of Identity and How to Overcome Them, Proceedings of the Securicom 88, 6th Worldwide Congress

on Computer and Communications Security and Protection, 1988, pp. 147–159.

[13] T. Dimitriou, A lightweight RFID protocol to protect against traceability and cloning attacks, Proceedings of the IEEE International Conference on Security and Privacy for Emerging Areas in Communication Networks — SECURECOMM, 2005.

[14] K. Finkenzeller, RFID Handbook, second edition, Wiley & Sons, 2002.

[15] Gartner, RFID Market \$3 Billion in 2010, December 13th, 2005.

[16] H. Gilbert, M. Robshaw, H. Sibert, An active attack against HB<sup>+</sup> — a provably secure lightweight protocol, IEE Electronic Letters 41 (21) (2005) 1169–1170.

[17] Greentech Computing, GT6 algorithm solves the extended DIMACS 32-bit parity problem, Technical Report, Greentech Computing Limited, London, England, 1998.

[18] Z. Guo, F. Fang, A.B. Whinston, Supply chain information sharing in a micro prediction market, Decision Support Systems 42 (2006) 1944–1958.

[19] G.P. Hancke, M.G. Kuhn, An RFID distance bounding pro tocol, Proceedings of the IEEE/Create-Net SecureComm, 2005, pp. 67–73.

[20] P. Harrop, R. Das, RFID Forecasts, Players, and Opportunities 2005–2015, IDTechEx, 2005.

[21] H.V.D. Heijden, Mobile decision support for in-store purchase decisions, Decision Support Systems 42 (2006) 656–663.

[22] D. Henrici, P. Müller, Hash-based enhancement of location privacy for radio-frequency identification devices using varying identifiers, Proceedings of the 1st International Workshop on Pervasive Computing and Communication Security (PerSec'04), 2004, pp. 149–153.

[23] J. Hering, The BlueSniper ‘rifle’, Presented at 12th DEFCON, Las Vegas, 2004.

[24] N.J. Hopper, M.M. Blum, Secure human identification protocols, in: C. Boyd (Ed.), Advances in Cryptology — ASIACRYPT 2001, Lecture Notes in Computer Science, vol. 2248, Springer Verlag, 2001, pp. 52–66.

[25] A. Juels, Yoking proofs” for RFID Tags, Proceedings of the First International Workshop on Pervasive Computing and Communication Security, IEEE Press, 2004.

[26] A. Juels, S.A. Weis, Authenticating pervasive devices with human protocols, in: V. Shoup (Ed.), Advanced in Cryptology — CRYPTO'05, Lecture Notes in Computer, vol. 3126, Springer Verlag, 2005, pp. 293–308.

[27] A. Juels, R.L. Rivest, M. Szydlo, The blocker tag: selective blocking of RFID tags for consumer privacy, in: V. Atluri (Ed.), 8th ACM Conference on Computer and Communications Security, 2003, pp. 103–111.

[28] G. Karjoth, P.A. Moskowitz, Disabling RFID tags with visible confirmation: clipped tags are silenced, Proceedings of the 2005 ACM Workshop on Privacy in the Electronic Society (WPES05), 2005, pp. 27–30.

[29] Z. Kfir, A. Wool, Picking virtual pockets using relay attacks on contactless smart-card systems, Proceedings of the 1st Interna

tional Conference on Security and Privacy for Emerging Areas in Communication Networks (SecureComm), 2005, pp. 47–58.

[30] I. Kirschenbaum, A. Wool, How to build a low-cost, extendedrange RFID skimmer, Cryptology ePrint Archive: Report 2006/ 054, 2006.

[31] A.K. Lenstra, E.R. Verheul, Selecting Cryptographic Key Sizes, Journal of Cryptography 14 (4) (2001) 255–293.

[32] J. Reid, J.M. Gonzalez Nieto, T. Tang, B. Senadji, Detecting Relay Attacks with Timing-Based Protocols, Queensland University of Technology, ePrint, 2006, http://eprints.qut.edu.au/view/year/ 2006.html.

[33] M.R. Rieback, B. Crispo, A.S. Tanenbaum, Is your cat infected with a computer virus? Proceedings of 4th IEEE International Conference on Pervasive Computing and Communications. (PerCom 2006), Pisa, Italy, March 2006.

[34] M.R. Rieback, B. Crispo, A.S. Tanenbaum, The Evolution of RFID Security, IEEE Pervasive Computing 5 (1) (2006) 62–69.

[35] J. Saito, K. Sakurai, Grouping Proof for RFID Tags, Proceedings of the 19th International Conference on Advanced Information Networking and Applications (AINA'05), 2005, pp. 621–624.

[36] SCISSEC, RFID DoS Vulnerabilities Uncovered in new UHF Tags, April 6 2006.

[37] G. Tsudik, YA-TRAP: yet another trivial RFID authentication protocol, 4th Annual IEEE International Conference on Pervasive Computing and Communications Workshops (PER-COMW'06), 2006, pp. 640–643.

[38] J.P. Warners, H.V. Maaren, A two-phase algorithm for solving a class of hard satisfiability problems, Operations Research Letters, vol. 23, 1998, pp. 81–88.

[39] S. Warren, Why Some People Put These Credit Cards in the Microwave, The Wall Street Journal Online (April 10 2006) A1–A16.

[40] S.A. Weis, S.E. Sarma, R. Rivest, D.W. Engels, Security and privacy aspects of low-cost radio frequency identification systems, Proceedings of the 1st Security in Pervasive Computing, LNCS, vol. 2802, 2004, pp. 201–212.

[41] J. Yang, J. Park, H. Lee, K. Ren, K. Kim, Mutual Authentication Protocol for Low-Cose RFID, Proceedings of the Workshop on RFID and Lightweight Cryptography, 2005, pp. 17–24.

[42] S. Garfinkel, A. Juels, R. Pappu, RFID privacy: an overview of problems and proposed solutions, IEEE Security and Privacy 3 (3) (May–June 2005) 34–43.

[43] M. Ohkubo, K. Suzuki, S. Kinoshita, A cryptographic approach to a 'privacy-friendly' tags, RFID Privacy Workshop, MIT, November 15 2003.

[44] D. Molnar, D. Wagner, Privacy and security in library RFID: issues, practices, and architectures, Proceedings of the 11th ACM conference on Computer and communications security, ACM Press, 2004, pp. 210–219.

[45] S. Lee, T. Asano, K. Kim, RFID Mutual Authentication Scheme based on Synchronized Secret Information, Symposium on Cryptography and Information Security, Hiroshima, Japan, January 2006.
