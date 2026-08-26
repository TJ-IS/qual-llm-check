---
otero_id: 15174
otero_key: "QKEPBSQK"
title: "RFID mutual authentication protocols"
authors: "Selwyn Piramuthu"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.09.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# RFID mutual authentication protocols

Selwyn Piramuthu

RFID European Lab, Paris, France

Information Systems and Operations Management, University of Florida, Gainesville, FL 32611-7169, USA

## a r t i c l e i n f o

Article history: Received 19 April 2010 Received in revised form 2 August 2010 Accepted 30 September 2010 Available online 7 October 2010

Keywords: RFID Mutual authentication protocols Vulnerabilities

## a b s t r a c t

As RFID-tagged systems become ubiquitous, the acceptance of this technology by the general public necessitates addressing related security/privacy issues. The past six years have seen an increasing number of publications in this direction, speci<sup>fi</sup>cally using cryptographic approaches. We consider a stream of publications among these that consider mutual authentication of tag and reader, and identify some existing vulnerabilities.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Introduced in the 1940s, RFID tags are used in a wide variety of disparate applications including health care, supply chain, retailing, and manufacturing, among others (e.g., [13,15,16]). As Radio-Frequency Identi<sup>fi</sup>cation (RFID) tags become ubiquitous, concerns with respect to their privacy/security characteristics are increasingly being discussed among relevant entities. In a world where identity theft, counterfeit products, corporate espionage, tracking, etc. are rampant, the urgent need to address privacy/security issues are especially crucial for successful deployment of RFID technology.

Although these issues themselves are not new in a general context, they are new and idiosyncratic to the RFID context primarily due to their item-level (as opposed to class-level in the case of bar codes) identi<sup>fi</sup>cation capabilities. Whereas RFID was introduced about seven decades ago, the major thrust in research addressing its security/ privacy vulnerabilities has existed for less than a decade. Researchers have approached several facets of security/privacy issues from a cryptographic perspective (e.g., [10]). We consider one such facet, namely mutual authentication, and identify vulnerabilities that exist in some of the cryptographic protocols that have been proposed in the literature.

Mutual authentication protocols are those where both sides authenticate each other, unlike the more common RFID authentication protocols where only one side (either the reader or the tag) authenticates the other. Mutual authentication is necessary and critical when each of the parties involved in a transaction needs to verify the identity of the other. Without mutual authentication, it is possible for either or both of the parties to misrepresent their identities. For example, in an automated retail store check-out, the lack of mutual authentication between the check-out mechanism and the customer allows for the possibility for an adversary to impersonate the customer to the store or vice versa. The former could render the transaction useless for the store, which simultaneously also incurs the associated cost (loss) of the items checked-out during this transaction. The latter could lead to privacy/security violations for the customer who also could suffer monetary as well as related consequences associated with identity theft.

The remainder of this paper is organized as follows: we consider several mutual authentication protocols, and identify some of their possible vulnerabilities in the next section. The last section concludes this paper with a brief discussion.

## 2. Mutual authentication protocols

For each protocol considered in this section, due to space considerations, we only provide a sketch to facilitate discussion. Each of the protocol sketch is to be read from top to bottom. The interested reader is referred to the original publications for detailed descriptions of these protocols. We identify some vulnerabilities present in these protocols. In some cases, an adversary exploits a vulnerability by sending a null vector to the tag. This is an operational issue and can easily be prevented by the tag explicitly checking for null vectors in its input.

The notations used in this paper are given as follows:

$r _ { A } , r _ { R } , r _ { T } .$ random l-bit vectors

$s _ { i } , I D \colon$ tag identi<sup>fi</sup>er

x, k: l-bit secret vectors

$h , H , G , E \colon$ hash functions — $\{ 0 , 1 \} ^ { * } \to \{ 0 , 1 \} ^ { l }$

$h _ { x } \mathrm { : }$ keyed (x) one-way hash function

T: tag R: right-half of the message L: left-half of the message c: counter s #: session number PRNG: pseudo-random number generator DATA: tag-related data $( \mathrm { e . g . }$ , shared secret key) $r _ { A } . x \colon$ scalar product of binary vectors $r _ { A }$ and x ⊕: exclusive-OR (XOR) ||: concatenation operator W : ith workable area.

## 2.1. Yang et al. [14]

This protocol (Fig. 1) assumes the existence of communication channels among the tag, reader, and back-end server that are not secure [14].

Each authentication process has its own freshly generated random bit vectors $( r _ { A } , r _ { B } )$ to prevent replay attacks. The random nonce generated by the reader $\left( r _ { A } \right)$ is randomized further using a keyed oneway hash function $\left( h _ { k } ( r _ { A } ) \right)$ to prevent a man-in-the-middle attack. The purpose of the freshly randomized A is to verify a legitimate reader through S and also to prevent forgery using ID values by passive eavesdropping.

Although the messages are randomized, an adversary can track tags as follows: an adversary sends S=0 to the tag and saves the reply $A \left( = h ( x _ { 1 } \oplus 0 \oplus I D ) = h ( x _ { 1 } \oplus I D ) \right)$ sent by the tag in return. Instead of A (the <sup>fi</sup>fth message in this protocol), the adversary sends some random l-bit vector to the tag. Since this is invalid, the tag does not update its secrets $( x _ { 1 } , x _ { 2 } )$

By keeping track of all future communications between the reader and tags, the adversary can track a tag of interest. This can be done as follows: in-between every authentic communication between the reader and the tag, the adversary queries the tag (with S=0) and retrieves the current value of A. The adversary then sends the last saved A′ as S to the tag, initiating a new authentication process. Let x<sup>a</sup> and x<sup>b</sup> be the after- and before-updating values of $x _ { 1 }$ respectively. The tag computes $A \left( = h ( x _ { 1 } ^ { a } \oplus A ^ { \prime } \oplus I D \right) = h ( ( x _ { 1 } ^ { b } \oplus A ^ { \prime } ) \oplus A ^ { \prime } \oplus I D ) = h ( x _ { 1 } ^ { b } \oplus I D ) )$ and this is exactly the same A that was stored by the adversary from an earlier authentication process. The adversary can use this to track a tag.

## 2.2. Luo et al. [8]

The authors purport to extend the protocol presented by Ohkubo et al. [9] in using the two hash functions for updating secret values [8]. They <sup>fi</sup>rst present a sketch of a basic framework where there were three entities (the back-end system, the reader, and the tag) and the reader's purpose was only to relay messages between the back-end system and the tag. Therefore, they omit the reader in their proposed protocol $( \mathrm { F i g . } 2 ) .$ . The tag also keeps a counter that it increments at the end of each successful authentication round. The server begins the mutual authentication process by sending a request to the tag, which responds with the counter and a hash of the counter and a shared secret (s). The server then validates these values and, when valid, replies with a random session number that is later used as an encrypting key.

This protocol has several vulnerabilities. An adversary can track the tag by its counter (c) value if this value is signi<sup>fi</sup>cantly different from those of surrounding tags. An adversary can also replay the <sup>fi</sup>rst message (read/write query) and the tag would reply with the same message $( c , G ( s \oplus c ) )$ as long as the counter and secret values have not been changed by a valid server. This replay attack can be used to track the tag. Another vulnerability occurs when an active adversary captures the second message from the server (s# $\ni G ( s ) , G ( s \oplus s \# \oplus W _ { k } ) , W _ { k } )$ and modi<sup>fi</sup>es $s \# \oplus G ( s )$ to s#⊕G(s)⊕δ and $W _ { k }$ to $W _ { k } \oplus \delta .$ Here, δ can be any number such that $W _ { k }$ ⊕δ is valid for a workable area. Now, the tag would accept this as valid and use s#⊕δ for encrypting messages to the server. However, the server will not be able to decrypt these messages since it has a different s# value. This would result in DoS from the server.

## 2.3. Lee et al. [7]

This protocol [7] uses both XOR and hash chains to authenticate tags and readers (Fig. 3). The secret key (x) is shared between the tag and the back-end server. The authors claim that, because of these seemingly random values being passed as messages, an adversary will not be able to violate the privacy and secrecy of this protocol. This protocol also prevents database desynchronization by maintaining the secret key from the previous and current authentication rounds. This assumes that the updates at the tag-side are performed twice without corresponding updates at the reader-side. This may not necessarily be true, since it is relatively easy to violate.

<table><tr><td>Server secret (x1, x2, ID, k)</td><td></td><td>Reader secret (k)</td><td></td><td>Tag secret (x1, x2, ID)</td></tr><tr><td rowspan="2">IF S == hk(rA)IF A == h(x1 ⊕ S ⊕ ID)A&#x27; = h(x2)ELSE abortx1 ← x1 ⊕ A&#x27;x2 ← x2 ⊕ A</td><td rowspan="2">A, S, rA←A&#x27;, hk(S)[DATA]→</td><td>rA← {0,1}lS ← hk(rA)</td><td>S←A</td><td>A ← h(x1 ⊕ S ⊕ ID)</td></tr><tr><td>hk(S)[DATA]</td><td>A&#x27;→</td><td>IF A&#x27; == h(x2)x1 ← x1 ⊕ A&#x27;x2 ← x2 ⊕ A</td></tr></table>

Fig. 1. Protocol of Yang et al. [14].

![](/api/attachments/QKEPBSQK/fulltext/images/7a77011a72b77279ec4c2b2dbc6105c525f7aa50cc5cc13ba69abceffa41e326.jpg)  
Fig. 2. Authentication protocol of Luo et al. [8].

![](/api/attachments/QKEPBSQK/fulltext/images/c7920c1a264d7376feb7bb62c5a0ec60613ac5d2a74010eeb56250687f532a56.jpg)  
Fig. 3. Protocol of Lee et al. [7].

An active adversary can block the <sup>fi</sup>rst message s and send an l-bit null vector as s to the tag. The tag now computes $r _ { B }$ as $h ( r _ { A } \oplus x \oplus 0 ) =$ $h ( r _ { A } \oplus x )$ . Next, the adversary can modify $r _ { A } \mathrm { t } \mathbf { 0 } \ ( r _ { A } \oplus s )$ and send it to the reader. When the back-end server computes $r _ { B } = h ( ( r _ { A } \oplus s ) \oplus x \oplus s ) =$ $h ( r _ { A } \oplus x )$ from $( s , ( r _ { A } \oplus s ) , r _ { B } )$ it receives from the reader, it would not be able to detect the adversary-modi<sup>fi</sup>ed messages. The adversary can also send a random r′ to the tag as the <sup>fi</sup>fth message. The tag will not update its key since $r _ { C } ^ { \prime } \neq r _ { C } .$ The adversary can then impersonate the tag by always sending $( r _ { A } \oplus s , h ( r _ { A } \oplus x ) )$ to the reader. This attack can be prevented if the reader detects repetition of messages from the tag. However, it is also possible that to be successful, the adversary only needs to use this attack once (e.g., to replace an expensive item by a cheap item during check-out).

## 2.4. Kang and Lee [6]

A sketch of this protocol [6] is shown in Fig. 4.

There are several inconsistencies in notation used in the text vs. those in the <sup>fi</sup>gures to describe the protocols. Nevertheless, since the channel between the database and the reader is not secure, an adversary can passively observe $r _ { R }$ and TS in the <sup>fi</sup>rst message from the reader to the database. Knowing $r _ { R }$ and $T S ,$ the adversary can determine the tag's secret (s) from the <sup>fi</sup>rst message between the reader and the tag that the adversary also observes.

## 2.5. Han et al. [5]

A sketch of this protocol [5] is shown in Fig. 5.

From the description of this protocol, it is not clear whether and when the seed for PRNG (α) is updated. This protocol is vulnerable to replay attack by an adversary. The tag can be tracked by an adversary who always sends the same $h ( r _ { R } ) ~ ( \neq 0 )$ to the tag, which responds with the same $h _ { s \oplus h ( r _ { R } ) } ( s \oplus h ( r _ { R } ) )$ ) as long as the secret key remains the same.

![](/api/attachments/QKEPBSQK/fulltext/images/f47a37130f5340413e98bbe6ce781ba61bbf9aacb76d724d47a616607790f443.jpg)  
Fig. 4. Extended authentication protocol of Kang and Lee [6].

<table><tr><td>Database(secret: s)</td><td></td><td>Reader(secret: s)</td><td></td><td>Tag(secret: s)</td></tr><tr><td></td><td rowspan="2"> $\xleftarrow{x_1, r_R}$ </td><td rowspan="3"> $r_R \leftarrow PRNG(\alpha)$ </td><td> $\xrightarrow{h(r_R)}$ </td><td rowspan="2">Check  $h(r_R) \neq \{0\}^k$  $x_1 \leftarrow h_{s \oplus h(r_R)}(s \oplus h(r_R))$ </td></tr><tr><td>Identify sIf ( $s == s_{old}$ ), $M \leftarrow M + 1$ </td><td> $\xleftarrow{x_1}$ </td></tr><tr><td>If  $M < \theta$  $y_1 \leftarrow h(x_1 \oplus s \oplus r_R)$ Else abort</td><td> $\xrightarrow{y_1}$ </td><td> $\xrightarrow{r_R, y_1}$ </td><td>verify  $h(r_R)$ Verify  $y_1 == h(x_1 \oplus s \oplus r_R)$ If valid,  $s \leftarrow h_{s \oplus r_R}(s \oplus r_R)$ </td></tr></table>

Fig. 5. Authentication protocol of Han et al. [5].

Even if the secret key is changed, the adversary can track the tag through the full disclosure of the secret key (s) as follows: by observing the communication between a tag and a reader, the adversary is able to obtain $r _ { R }$ (from the last message from the reader to the tag). The adversary intercepts this last message from the reader to the tag, thus preventing the tag from updating its key (s). It holds this message $( \mathrm { i . e . , } r _ { R } , h ( x _ { 1 } \oplus s \oplus r _ { R } ) )$ and the <sup>fi</sup>rst message from the reader to the tag $\left( \mathrm { i } . \mathrm { e } . , h ( r _ { R } ) \right)$ . The adversary then sends this $r _ { R }$ to the tag in a new authentication round. The tag generates $h _ { s \oplus r _ { R } } ( s \oplus r _ { R } ) \ ( { \mathrm { s a y } } , s _ { n e w } )$ and sends it to the reader (here, the adversary). The adversary can then abort this authentication round. The adversary can trigger a new authentication round that is a replication of the previous authentication round, i.e., the adversary sends the $h ( r _ { R } )$ captured earlier to the tag, which then replies with $h _ { s \oplus h ( r _ { R } ) } ( s \oplus h ( r _ { R } ) )$ . The adversary then sends the previously captured $r _ { R } , h ( x _ { 1 } \oplus s \oplus r _ { R } )$ to the tag, which updates its key $( s  h _ { s \oplus r _ { R } } ( s \oplus r _ { R } ) )$ . However, the adversary knows this $s _ { n e w } .$ The adversary can, therefore, clone the tag and impersonate it from now on.

The adversary can desynchronize information in the database and the tag. This can be accomplished as follows: the adversary can block the last message from the reader to the tag $\left( r _ { R } , y _ { 1 } \right)$ from reaching the tag. When this is accomplished, the reader has the updated secret while the tag has the previous (pre-update) secret (s). Although the database accepts the previous secret $\left( s _ { o l d } \right)$ as being valid, it increments its counter (M) to re<sup>fl</sup>ect the fact that the tag had replied using a previous key. When M reaches a pre-de<sup>fi</sup>ned threshold (θ), the database realizes the presence of an adversary and stops communicating with this tag. The adversary can, therefore, increment the counter (M) until it reaches θ and trigger the database's response to such a high value, thus desynchronizing the reader and the tag.

## 2.6. Ha et al. [4]

A sketch of this protocol [4] is shown in Fig. 6. An adversary impersonating a valid reader can desynchronize the tag over several authentication rounds. This vulnerability is illustrated as follows: at <sup>fi</sup>rst, the adversary sets SYNC=1 by sending a random $( Q u e r y , r _ { R } )$ to the tag followed by a random (i.e., incorrect) R(Q′) to the tag. Now, the tag has SYNC=1. Next, the adversary sends $( Q u e r y , r _ { R } { = } n u l l )$ to the tag. The tag then computes $P = Q = H ( I D | | r _ { T } )$ . Since the adversary now knows the entire $Q ,$ it can send $R ( Q ^ { \prime } )$ to the tag. The tag then updates its ID to H(ID). This entire process, when repeated at least one more time, results in desynchronizing the tag from the reader.

<table><tr><td>Database(secret: ID)</td><td></td><td>Reader(secret: ID)</td><td rowspan="2">Query,  $r_R$ </td><td>Tag(secret: ID)</td></tr><tr><td></td><td rowspan="2"> $P, L(Q), r_T, r_R$ </td><td rowspan="3"> $r_R \leftarrow \{0,1\}^k$ </td><td rowspan="2"> $r_T \leftarrow \{0,1\}^k$ If (SYNC == 0) $P = H(ID)$ else  $P = H(ID||r_T)$  $Q = H(ID||r_T||r_R)$ SYNC=1</td></tr><tr><td>(P == HID orH(ID|| $r_T$ )PID = IDelse if (P == H(PID|| $r_T$ ))PID = PIDelse abort</td><td> $P, L(Q), r_T$ </td></tr><tr><td> $Q' = H(PID||r_T||r_R)$ If  $L(Q') = L(Q)$ ID = H(PID|| $r_R$ )HID = H(ID)</td><td> $R(Q')$ </td><td> $R(Q')$ </td><td>If ( $R(Q) == R(Q')$ { ID = H(ID|| $r_R$ )SYNC=0 }</td></tr></table>

Fig. 6. Mutual authentication protocol of Ha et al. [4].

![](/api/attachments/QKEPBSQK/fulltext/images/a325aba9c456d8d49ce582056b0139fc6149a4a530586eb450ef2d540e5a2d3c.jpg)  
Fig. 7. Qingling et al. [11].

This vulnerability is clearly an implementation issue that can be prevented by ensuring $r _ { R } \neq$ null when it reaches the tag.

## 2.7. Qingling et al. [11]

The authors of this protocol [11] claim that this protocol is secure because of the use CRC (Cyclic Redundancy Check) and the introduction of random nonces to encrypt messages (see Fig. 7). However, the protocol is vulnerable from adversaries who want to impersonate either reader or tag to the other. This is a serious vulnerability since (1) mutual authentication, the goal of this protocol, fails, and (2) being able to impersonate something has deleterious consequences.

An adversary can impersonate the reader as follows: the adversary <sup>fi</sup>rst sends $r _ { R } = 0$ to the tag along with Query and receives $( r _ { T } , M )$ from the tag. The adversary can then send this M (instead of M′) to the tag as the last message and the tag would verify it to be true since M′ does not depend on $r _ { R } .$

An adversary can impersonate the tag as follows: the adversary <sup>fi</sup>rst passively observes the communication between the reader and the tag and copies the messages. When it wants to impersonate the tag the next time the reader authenticates the tag, it sends $M ^ { * }$ $r _ { R } \oplus r _ { R } ^ { * } \oplus r _ { T } ^ { * }$ to the reader (second message in the sequence). Here, $M ^ { * }$ $r _ { R } ^ { * } , r _ { T } ^ { * }$ are $M , r _ { R } , r _ { T }$ respectively from the previous authentication round. When the server tries to verify this $M ^ { * } , r _ { R } \oplus r _ { R } ^ { * } \oplus r _ { T } ^ { * }$ combination, it would prove to be true and the server accepts it. Another vulnerability of this protocol using CRC is identi<sup>fi</sup>ed by Burmester et al. [1].

## 2.8. Tan et al. [12]

A sketch of this protocol [12] is shown in Fig. 8. An adversary can track the reader since $I D _ { R }$ is sent in the open in plaintext. An adversary can also track any given tag through $h ( I D _ { R } | | s ) _ { m }$ since this is constant for a given reader $\left( I D _ { R } \right)$ and tag (s). The adversary can send a request to the tag, which responds with a fresh $r _ { T } .$ . The adversary can then respond with a known (from a previous passive observation) $r _ { R } , I D _ { R }$ to the tag. The next response from the tag $\left( \operatorname { i . e . , } h ( I D _ { R } | | s ) \right)$ identi<sup>fi</sup>es it since the tag secret s remains constant.

## 2.9. Chen and Deng [3]

Here ([3]; see Fig. 9), EPC (Electronic Product Code) is used as the identi<sup>fi</sup>er. A critical vulnerability of this protocol is identi<sup>fi</sup>ed by Burmester et al. [1] whereby the tag can be impersonated. Here, the adversary passively listens to the communication between the reader and the tag and stores the conversation. During the next authentication round, when the reader sends out a request message, the adversary can reply with r, X′, Y′. Here, ${ X } ^ { \prime } { = } X \oplus { r } _ { T } \oplus { i }$ r where X and $r _ { T }$ are observed values from the previous authentication round and some random r is the new $r _ { T }$ and $Y ^ { \prime } = Y .$ The value for Y is constant since $Y = C R C ( r _ { T } \oplus s _ { 1 } \oplus X ) = C R C ( r _ { T } \oplus s _ { 1 } \oplus s _ { 2 }$ ⊕EPC⊕r ) and this equals CRC $( s _ { 1 } \oplus s _ { 2 } \oplus E P C )$ , which is constant. As Burmester et al. [1] note, although an implementational issue that can be <sup>fi</sup>xed by the reader checking for duplicate responses from tags, the adversary can just replay a previous message and the reader would accept it since the tag's response does not depend on the nonce sent by the reader (i.e., $r _ { R } ) .$ Moreover, it is easy to track the tag since its response can be easily determined as discussed earlier. It is also trivial to impersonate the reader by replaying the same message and the tag would accept it.

![](/api/attachments/QKEPBSQK/fulltext/images/fc2a63a320e451d4146cc3e9b366e4da8eb2fc5fc12be6178b4466f93ab27d8b.jpg)  
Fig. 8. Authentication protocol of Tan et al. [12].

![](/api/attachments/QKEPBSQK/fulltext/images/a0a1063752b3d1e3f0bae91138bd1054f43953fd58a8807eb2ca840c74c7e447.jpg)  
Fig. 9. Protocol of Chen and Deng [3].

## 2.10. Protocol of Cai et al. [2]

The <sup>fi</sup>rst stage is for mutual authentication between the reader and the tag and the second stage updates the secret [2]. The reader initiates the process by sending a random nonce to the tag, which generates another random nonce and sends a message with these. The reader then contacts the server who validates the information and shares tag information when valid. Now, the reader knows the tag's secrets. The server then generates a new set of secrets and shares them with the tag. The tag validates it and updates its keys when valid. It also responds to the server with random nonces encrypted with a secret key. The server updates the keys after the message is successfully validated.

A vulnerability is due to the desynchronization between the tag and the reader that can arise when the reader has the new key (t,s) while the tag has the previous key when an adversary blocks the last communication $\left( M _ { 3 } \right)$ between the reader and the tag in the mutual authentication protocol (Fig. 10). Another vulnerability is due to the impersonation of tag by an adversary. An adversary can passively observe the communication between the server and the tag (Fig. 11) during a secret update protocol run and copy $r _ { 1 } , r _ { 2 }$ and $M _ { 3 } ,$ . The next time this protocol is run, the adversary impersonating the tag can respond to the server's message (of r′, M′ , M′ ) with r′ , $M _ { 3 } ,$ where $r _ { 2 } ^ { \prime } = r _ { 1 }$ ⊕r ⊕ $r _ { 1 } ^ { \prime } ,$ and the server would accept this as valid and update the key values.

![](/api/attachments/QKEPBSQK/fulltext/images/0fd640e40bfc8ca321a9d67209ba149f0f08b89882cabf792f47af0db9f7030b.jpg)  
Fig. 11. Protocol of Cai et al. — update tag secret.

## 3. Discussion

Mutual authentication has not received as much attention from researchers compared to one-sided authentication where only one of the two parties involved authenticates the other. However, mutual

$$
\begin{array}{c c c c c} \text {Server} & & \text {Reader} & & \text {Tag} \\ (\text {secret:} (t, s), (t ^ {\prime}, s ^ {\prime})) & & (\text {secret} t, s) & \xrightarrow {r _ {1}} & (\text {secret:} t, s) \\ \hline & & r _ {1} \leftarrow \{0, 1 \} ^ {l} & \xrightarrow {r _ {1}} & \\ & R _ {T}, r _ {1}, M _ {1}, M _ {2} & & M _ {1}, M _ {2} \\ \text {find} (t, s) \text {s.t.} & & & & \\ M _ {2} = f _ {t} (r _ {1} | | M _ {1} \oplus t) & & & & \\ r _ {2} = M _ {1} \oplus t & & & & \\ M _ {3} \leftarrow s \oplus h (r _ {2}) & & & & \\ s ^ {\prime} \leftarrow s & & & & \\ t ^ {\prime} \leftarrow t & & & & \\ s \leftarrow (s \ll \frac {l}{4}) \oplus r _ {1} & & & & \\ \oplus (t \gg \frac {l}{4}) \oplus r _ {2} & & & & \\ t \leftarrow h (s) & & M _ {3}, (t, s), \text {Info} & (t, s), \text {Info} & \xrightarrow {M _ {3}} \\ & \xrightarrow {} & & & s \leftarrow M _ {3} \oplus h (r _ {2}) \\ & & & & \text {if} h (s) = = t, \\ & & & & t \leftarrow h ((s \ll \frac {l}{4}) \oplus r _ {1} \\ & & & & \oplus (t \gg \frac {l}{4}) \oplus r _ {2}) \end{array}
$$

Fig. 10. Protocol of Cai et al. — mutual authentication.

Table 1  
Summary of identi<sup>fi</sup>ed vulnerabilities.

<table><tr><td>Protocol</td><td>Vulnerabilities</td></tr><tr><td>Yang et al. [14]</td><td>Replay attack</td></tr><tr><td>Luo et al. [8]</td><td>DoS and replay attack</td></tr><tr><td>Lee et al. [7]</td><td>Tag impersonation</td></tr><tr><td>Kang and Lee [6]</td><td>Tag impersonation</td></tr><tr><td>Han et al. [5]</td><td>DoS, replay attack, and tag impersonation</td></tr><tr><td>Ha et al. [4]</td><td>DoS</td></tr><tr><td>Qingling et al. [11]</td><td>Tag and reader impersonation</td></tr><tr><td>Tan et al. [12]</td><td>Replay attack</td></tr><tr><td>Chen and Deng [3]</td><td>Replay attack, and tag and reader impersonation</td></tr><tr><td>Cai et al. [2]</td><td>DoS and tag impersonation</td></tr></table>

authentication is important and has its own merits depending on the application context. We selected a few among published mutual authentication protocols and considered their vulnerabilities. This list is by no means complete, nor is it meant to be. The purpose here is to show that several existing mutual authentication protocols are vulnerable from a security/privacy perspective. Identifying present vulnerabilities in existing protocols is a step in the direction of generating better mutual authentication protocols.

Table 1 provides a summary of the identi<sup>fi</sup>ed vulnerabilities. The vulnerabilities associated with the protocols considered are DoS, replay attack, and tag and/or reader impersonation. These protocols could possibly have other vulnerabilities that are not identi<sup>fi</sup>ed here. Since a majority of the protocols considered are ad hoc in nature, there is no single pattern associated with any given vulnerability. Regardless, once identi<sup>fi</sup>ed, the vulnerability needs to be addressed before such a protocol can be considered for further use. From a managerial perspective, an implementor of any given mutual authentication protocol is obligated to consider vulnerabilities from both (reader and tag) perspectives and weigh the associated costs should further vulnerabilities be identi<sup>fi</sup>ed. There is no guarantee with respect to the security of any mutual authentication protocol since these protocols depend on the impracticality of exhaustive search or high search cost. Improvements in computing (e.g., quantum computing) could render a majority of these protocols useless. Until then, the best we can do is to ensure that the protocols that are implemented do not contain any obvious vulnerabilities that can be easily exploited by a resourceful adversary.

## References

[1] M. Burmester, B. de Medeiros, J. Munilla, S. Peinado, Secure EPC Gen2 compliant Radio Frequency Identi<sup>fi</sup>cation eprint# 2009/149, International Association for Cryptological Research (2009).

[2] S. Cai, Y. Li, T. Li, R. Deng, Attacks and improvements to an RFID mutual authentication protocol, 2nd ACM Conference on Wireless Network Security (WiSec '09), 2009, pp. 51–58.

[3] C.-L. Chen, Y.-Y. Deng, Conformation of EPC class 1 and generation 2 standards RFID system with mutual authentication and privacy protection, Engineering Applications of Arti<sup>fi</sup>cial Intelligence 22 (8) (2009) 1284–1291.

[4] J. Ha, J. Ha, S. Moon, C. Boyd, LRMAP: lightweight and resynchronous mutual authentication protocol for RFID system, Proceedings of the ICUCT, LNCS 4412, 2007, pp. 80–89.

[5] S. Han, V. Potgar, E. Chang, Mutual authentication protocol for RFID tags based on synchronized secret information with monitor, Proceedings of ICCSA, 4707, LNCS, 2007, pp. 227–238.

[6] S.-Y. Kang, I.-Y. Lee, A Study on low-cost RFID system management with mutual authentication scheme in ubiquitous, Proceedings of APNOMS, 4773, LNCS, 2007, pp. 492–502.

[7] S. Lee, T. Asano, K. Kim, RFID mutual authentication scheme based on synchronized secret information, Proceedings of the 2006 Symposium on Cryptography and Information Security (SCIS), 2006.

[8] Z. Luo, T. Chan, J.S. Li, A lightweight mutual authentication protocol for RFID networks, Proceedings of the IEEE International Conference on e-Business Engineering (ICEBE '05), 2005, pp. 620–625.

[9] M. Ohkubo, K. Suzuki, S. Kinoshita, Cryptographic approach to ‘privacy-friendly tags, Presented at the RFID Privacy Workshop, MIT, Cambridge, MA, Nov. 15 2003.

[10] S. Piramuthu, Protocols for tag/reader authentication, Decision Support Systems 43 (3) (2007) 897–914.

[11] C. Qingling, Z. Yiju, W. Yonghua, A minimalist mutual authentication protocol for RFID system and BAN logic analysis, ISECS International Colloquium on Computing, Communication, Control, and Management (2008) 449–453.

[12] C.C. Tan, B. Sheng, Q. Li, Secure and serverless RFID authentication and search protocols, IEEE Transactions on Wireless Communications 7 (4) (April 2008) 1400–1407.

[13] Y.-J. Tu, W. Zhou, S. Piramuthu, Identifying RFID-embedded objects in pervasive healthcare applications, Decision Support Systems 46 (2) (2009) 586–593.

[14] J. Yang, J. Park, H. Lee, K. Ren, K. Kim, Mutual authentication protocol for low-cost RFID, Proceedings of the Workshop on RFID and Lightweight Cryptography, 2005, pp. 17–24.

[15] W. Zhou, S. Piramuthu, Framework, strategy, and evaluation of healthcare processes with RFID, Decision Support Systems 50 (1) (2010) 222–233.

[16] W. Zhou, Y.-J. Tu, S. Piramuthu, RFID-enabled item-level retail pricing, Decision Support Systems 48 (1) (2009) 169–179.

Selwyn Piramuthu is a Professor in the Information Systems and Operations Management Department at the University of Florida. He is an Associate Researcher at ESCP-Europe (Paris) and a Member of the RFID European Lab (Paris). His research interests include RFID systems, pattern recognition and its application in supply chain management, computer-aided manufacturing, and <sup>fi</sup>nancial credit-risk analysis.
