---
otero_id: 21634
otero_key: "Z6YS3S2J"
title: "Anonymous mechanisms in group decision support systems communication"
authors: "B. Gavish; J.H. Gerdes"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00057-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Anonymous mechanisms in group decision support systems communication

B. Gavish <sup>a</sup>, J.H. Gerdes Jr. <sup>b,)</sup>

Owen Graduate School of Management, Vanderbilt UniÕersity, NashÕille, TN 37203, USA

<sup>b</sup> A. Gary Anderson Graduate School of Management, UniÕersity of California-RiÕerside, RiÕerside, CA 92521, USA

Accepted 3 September 1998

## Abstract

Using group decision support systems GDSS as a backdrop, this paper looks at the issues surrounding anonymity, withŽ . particular emphasis on how it may be achieved. Ensuring anonymity requires more than simple encryption. Anonymity is viewed as a composite of three types of anonymity—environmental, content-based and procedural. Each type is investigated and procedures developed to improve the anonymity of the system. Behavioral and operational costs are identified for each of the three types of anonymity. For some meetings, the benefits of supporting anonymous communication may not justify the costs. Mechanisms providing complete procedural anonymity in various system configurations are presented. It is shown that five separate mechanisms can be used to provide procedural anonymity. The impact of relaxing each of these mechanisms is also investigated. Even though a system provides anonymity, participants may be skeptical. This skepticism can reduce the overall efficiency of the group. For this reason it is important to be able to convince groups that their comments are indeed anonymous. The issue of how to convince individuals that their anonymity is secure is discussed and a partial solution to this problem is presented. q 1998 Elsevier Science B.V. All rights reserved

Keywords: Anonymity; Cost; Decision support; Encryption; GDSS; Privacy

## 1. Introduction

Anonymity, and its impact on individual and group dynamics, has been studied in many different contexts. The public choice literature has reported that individuals experience a pressure to conform to a perceived viewpoint when opinions and positions are expressed publicly rather than anonymously 49 . A <sup>w</sup> <sup>x</sup> study of the anonymous journal review process found that reviewers and editors held moderately negative opinions of non-anonymous reviews of academic papers. Of those responding, 9% indicated that they would refuse to participate in a non-anonymous review process 7 . The impact of anonymity on group <sup>w</sup> <sup>x</sup> interaction is also well documented in the social psychological literature. Anonymity has been found to cause a deindividualizing effect—the perception of the group as a single body rather than a group of individuals 22,24 . This can lead to social loafing <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 56 , and affect an individual’s willingness to disclose confidential information 47 .<sup>w</sup> <sup>x</sup>

Research has shown that anonymity can have both a positive and negative impact on group interaction

Žsee Fig. 1; Refs. 36–41,43,44,53,62,63,65 . On the<sup>w</sup> <sup>x</sup>. positive side, anonymity eliminates many elements which can limit a group’s productivity. By disassociating the message from its source, the group can focus more on content and not be influenced by the stature or reputation of the commentor. Anonymity lessens risk of group think by allowing the expression of dissenting viewpoints in a less politically risky environment. Unfortunately, anonymity can also negatively impact individual and group interaction. Some individuals are emboldened by the veil of anonymity and engage in antisocial behavior which disrupts the exchange of information 24,46 . <sup>w</sup> <sup>x</sup>

Anonymity has also been an active area of research in group decision support systems GDSS .Ž . Early work focused on empirical studies to determine anonymity’s impact under different system configurations see Fig. 2 . Recent work has studiedŽ . anonymity’s economic impact 32–35 , and how to<sup>w</sup> <sup>x</sup> provide participants with incentives in an anonymous environment 5,29 .<sup>w</sup> <sup>x</sup>

Although there have been many behavioral GDSS studies focusing on anonymity, there has been little investigation into how this anonymity can be achieved. Most research has dealt with systems which only suppress explicit attribution of user contribution while maintaining attribution links within the system for research purposes 15,64 .<sup>w</sup> <sup>x</sup>

Providing anonymity is more problematic than simply posting encrypted messages without attribution tags. Standard communication systems append headers to all transactions. These headers contain routing information which the network uses to facilitate replies and message confirmation. Unfortunately, this same header information can be used to identify the source of the transmission. Even in the absence of this type of information, monitoring of user activity can jeopardize anonymity. If it is known that a single user is actively generating messages, then all messages can be attributed to that individual. Similarly, knowing that a given individual did not generate any messages means that he or she can effectively be eliminated from the list of possible authors.

These issues relate to system and communication protocols. As such, they must be addressed through appropriate changes in these protocols. Unfortunately, even if all these procedural clues are eliminated, message content can still reveal information about the author’s identity.

General protocols have been published which address the procedural aspects of anonymous communication 11,12,61 . However, they do not address<sup>w</sup> <sup>x</sup> other aspects of anonymity which can be equally important, such as environmental factors and message content. They also do not address the issue of convincing participants that their anonymity is indeed secure.

## 1.1. Contributions

This paper investigates the various components of anonymous communication in a computer network using GDSS examples. The contributions of this paper are two-fold. Various researchers have mentioned some of the aspects which jeopardize anonymity. This paper consolidates these issues, analyzes their risks, and proposes specific mechanisms to combat these risks. It also looks at the consequences of using protocols which provide limited anonymity.

The second contribution deals with the issue of convincing participants that their anonymity is indeed secure. A participant’s perceived anonymity can influence his or her willingness to discuss sensitive or embarrassing issues. If individuals are not convinced that their anonymity is protected by the system, interactions will be guarded, reducing the system’s effectiveness. This issue has not previously been discussed in the literature. A solution is provided for the centralized meeting case.

The remainder of the paper is laid out as follows. Section 2 defines terms used throughout paper and reviews prior research relevant to anonymous communication. This includes a brief introduction of encryption techniques and a discussion of how an intermediary can be used to provide secure, anonymous communication. Section 3 looks at both the process and implications of providing anonymous communications. For the purpose of this work, anonymity is viewed as a composite of three types of anonymity—environmental, content-based and procedural.

Section 4 reviews the impact of anonymous interaction. Three issues are discussed. The first looks at the costs and benefits of providing anonymous com-

Positive Aspects of Anonymity

<table><tr><td>Depersonalizes discussion: Limits the association between participants and the positions they express, which can lead to more honest interaction. Comments must be evaluated on their own merits. Also, individuals can distance themselves from their comments [38,53]. Participants can change earlier stated positions without appearing indecisive.</td><td>Reduces Groupthink: Groupthink is defined as the ‘deterioration of moral efficiency, reality testing, and moral judgment in the interest of group solidarity’ [41]. Participants may withhold concerns so not to appear weak and unintelligent or not committed to the group effort [42]. Groupthink has been hypothesized to have played a role in many prominent fiascoes, including: the Bay of Pigs, the U.S. involvement in Vietnam conflict, and the Watergate cover-up [41].</td></tr><tr><td>Deinhibiting effect: Anonymity can have a deinhibiting effect in situations where there is a perceived risk or cost of participation [43,44]. It provides a veil behind which individuals may express positions or engage in activities they are otherwise unwilling to share.</td><td>Increased focus on content: Participants often speculate on the source of comments during anonymous sessions [64]. Absolute anonymity may help to shift participant’s focus from trying to breach anonymity to the content of comments generated.</td></tr><tr><td>Reduction in participant anxiety: Anonymity lowers the risk of interaction. It can increase the level of participation by reducing the risk of direct reprisals [21,36,39,40,65]. Shy individuals can participate more equally. This reduced anxiety can lead to a broader exploration of the issues.</td><td>Provides the luxury of denial: Absolute anonymity means no comment can be directly attributed to a given participant. In such an environment, individuals may feel freer to express divergent or unpopular opinions than in non-anonymous environments.</td></tr><tr><td>Allows the discussion of sensitive issues: Some issues are very difficult to address in an open forum. These include review of management by their subordinates, sexual harassment, and substance abuse.</td><td>Physical traits of commentators are hidden: Knowing a participant’s race, nationality, age, sex, religion, education, or disability status can impact opinions and influence comments which are made.</td></tr><tr><td>Allows Devil’s Advocate position: Individuals can take a Devil’s Advocate stance to test a group’s commitment to a course of action [62].</td><td></td></tr><tr><td colspan="2">Negative Aspects of Anonymity</td></tr><tr><td>Lack of accountability: Anonymity can increase free-riding, (not productively participating in group activities) [4,14,21,45]. Without accountability, participants may engage in disruptive, or generally unacceptable behavior such as flaming (posting of caustic, highly degrading replies to messages) on Internet discussion groups.</td><td>Hide contributor’s credentials: In an open meeting discussing a complicated medical procedure, contributions of an experienced doctor or recognized expert would probably be given more weight than comments of a new intern or nonprofessional. Anonymity prevents participants from taking such experience into account.</td></tr><tr><td>Attribution may be desirable: Participants may want to receive recognition for their contributions. If this is not possible, users may withhold their contributions and express them in a forum where they may receive credit [63,64].</td><td>Relationships may be significant: Anonymity eliminates potentially significant social cues. In some setting, interpersonal relationships are important and therefore should not be eliminated through anonymity [37].</td></tr><tr><td>Risk if anonymity is breached: Anonymity can be used to get individuals to contribute information they are unwilling to express openly (i.e., whistle blowers). If this anonymity is breached, the contributor risks retaliation.</td><td>Legal implications of anonymity: In an anonymous system, who is libel for any illegal actions (i.e., slanderous messages)?</td></tr></table>

Fig. 1. Summary of anonymity’s positive and negative effects.

<table><tr><td>Focus of Study</td><td>Results</td><td>Conclusions</td></tr><tr><td>Effect of anonymity on group problem solving [42,63]</td><td>Anonymity had no effect on the number of comments generated. Anonymous groups were more critical, more probing.</td><td>Anonymity may be beneficial to promote free-flowing exchange of ideas and opinions.</td></tr><tr><td>Anonymity and group proximity [44]</td><td>Remote-anonymous groups produced the most comments, proximate-identified groups produced the least comments.</td><td>Physical dispersion may increase the level of anonymity, for it becomes more difficult to determine who is contributing at any given time. Also, there are different levels and types of anonymity.</td></tr><tr><td>Anonymity and evaluative tone [15]</td><td>Anonymous groups with a critical evaluative tone produced the most output. Average solution quality and average solution rarity were unaffected.</td><td>Hypothesized that the evaluative tone had a cueing effect. A critical tone prompted more critical comments. The lack of an effect on quality and rarity was likely due to the small, artificial problem solved.</td></tr><tr><td>Anonymity and group size [63]</td><td>Larger groups generated more, higher quality ideas and more output than smaller groups. Anonymity was found to have no impact.</td><td>Hypothesized that the ‘non-aversive nature of the task and group composition mitigated the influence of anonymity on group performance.’ [63]</td></tr><tr><td>Deindividualizing effects of anonymity [15,38,42,43,63]</td><td>Results are mixed. Most studies have shown anonymous groups tend to be more critical [15,43,63]. Some studies found no statistically significant impact on the critical nature of the meeting [38]. Other studies found anonymity reduced the number of critical comments made [44].</td><td>Participants are more likely to react strongly and do things they otherwise would not do. Anonymity may be useful since it permits participants to distance themselves from their comments.</td></tr><tr><td>Anonymity and satisfaction [15,44,63]</td><td>Results are mixed. Some studies show identified groups are more satisfied than anonymous groups. [15, 63] Another study indicated participant proximity may impact the satisfaction of the group. Anonymous—dispersed and identified—face-to-face groups were more satisfied than anonymous—face-to-face and identified—dispersed groups [44].</td><td></td></tr><tr><td>Anonymity and perceived effectiveness [15,44,63]</td><td>Results are mixed. Some studies found perceived meeting effectiveness was higher under anonymous conditions [44], while participants in other studies felt identified sessions to be more effective [15,63].</td><td></td></tr><tr><td>Group composition and anonymity [15,42,44,63]</td><td>Ad hoc groups with little history will tend to have a higher degree of anonymity than established groups.</td><td></td></tr></table>

Fig. 2. Group decision support research relating to anonymity and its effects.

munication. The second deals with the impact of message imitation—the process of generating dummy messages to hide the existence of a useful message and<sup>r</sup>or the identity of its author. This is followed by a discussion of liability issues related to anonymous communication. Section 5 summarizes the results of this work and gives some direction for future research. Appendix A provides proofs of various mechanisms used to provide anonymous communication.

## 2. Prior research

Anonymity has played a major role in early GDSS research. Fig. 1 summarizes both the positive and negative impacts that anonymity can have on group interaction. Fig. 2 summarizes the results of various studies investigating the effect of anonymity within a GDSS environment. This work illustrates that anonymity can be an important issue in a group environment. Unfortunately, there has not been any investigation into how this anonymity is achieved.

A field critical to anonymous communication is cryptography. Cryptography deals with the encryption mechanisms needed to securely transmit a message. Because of the importance of cryptography and encryption schemes in anonymous communication, we define the terms used throughout the paper in Section 2.1 and provide a brief introduction of the basic concepts in the Section 2.2. These concepts are presented in sufficient detail to provide a basis for the remainder of the paper. The interested reader is directed to Refs. 9,17,52,61 for a more complete treatment. Section 2.3 provides an overview of two anonymous communication protocols which serve as a basis for subsequent discussions.

## 2.1. Definition of terms

The system of interest consists of a network of one or more intermediary message servers through which a closed group of individuals communicate. This closed group will be referred to as the set of authorized participants with the complement being the set of unauthorized indiÕiduals. The set of message servers and authorized participants need not be disjoint—some authorized participants may also act as message servers. As discussed in Section 2.3.1, incorporating the authorized participants into the set of message servers can be beneficial since it tends to increase procedural anonymity.

## 2.1.1. Anonymous remailers

Standard network protocols attach a routing header to all messages before they are transmitted. The purpose of this header is to ensure that messages arrive at their proper destination. Unfortunately, these headers not only identify the destination, but also their source thereby linking the message to its author.

To support anonymity, this header information must be removed before the message reaches its destination. This can be done through an anonymous remailer a special type of message server 16 .Ž . <sup>w</sup> <sup>x</sup> Anonymous remailers receive a message packet, removes information identifying the source, and then remails the packet to its destination anonymousŽ remailers are discussed in more detail in Section 2.3.1 ..

## 2.1.2. LeÕels of anonymity

Define the system’s anonymity complexity as the maximum number of colluding entities which cannot defeat the anonymity of the system. Order-N anonymity, represented as OAŽ . N , indicates that N <sup>q</sup>1 entities must collude to defeat the anonymity. Three important cases exist. The first is OA 0 —aŽ . single entity holds sufficient information to defeat anonymity. Routing messages through a single-hop, anonymous remailer is an example of an OA 0Ž . system.

The second is OA 1 —collaboration between twoŽ . entities is needed to breach anonymity. An example of such a system is the United States’ Escrowed Encryption Standard EES 25 which incorporates aŽ . <sup>w</sup> <sup>x</sup> mechanism to allow law enforcement agencies, when authorized by the courts, to easily decrypt encoded messages. Two escrow agents each holds half of the law enforcement key which can be used to gain access to the plain text message through a law enforcement trapdoor built into the encryption protocol. Each key fragment is useless without the other half, thus preventing the escrow agents from independently violating the anonymity of transmissions <sup>w</sup> <sup>x</sup> 18 .

The third important case is OAŽ . n —where all n system message servers must collude or be forced toŽ relinquish their information before anonymity can. be breached. This is defined as complete anonymity. Routing a message through a set of n anonymous remailers is an example of an OAŽ . n system.

Define a message’s attribution chain as the ordered sequence of servers through which the message passes from the source to the destination. Any system which incorporates the contributor into the attribution chain is said to provide absolute anonymity, for to breach anonymity requires the cooperation of the author. If the contributor is not included, the system is said to provide limited anonymity.

## 2.1.3. Artificial messages

Artificial message actiÕity is defined as the process of transmitting non-useful, dummy messages for the purpose of disguising the source of other messages. To completely hide authorship of a transmission, the message server must receive at least one transmission of similar size from each user prior to the message’s posting. Define this process as complete imitation. The issues surrounding message imitation are discussed in more detail in Section 3.3.5.

## 2.2. Cryptographic techniques

Cryptography is the study of coding systems used to provide secret and secure communications, and as such, is central to the process of providing anonymous communications. Cryptographic techniques can be used to provide secure communication, digital signatures, and a means to prevent message tampering. The following provides a brief overview of encryption techniques and protocols useful in supporting anonymous communication.

## 2.2.1. Encryption

Encryption is the primary mechanism used to maintain secrecy and confidentiality in communications. There are two basic types of encryption algo rithms—simple key and dual key. Simple key encryption uses the same key to encrypt and decrypt a message while dual key encryption uses two different keys see Fig. 3 .Ž .

An important special case of the dual key system is the symmetric dual key encryption 58 . The sym-<sup>w</sup> <sup>x</sup> metric dual key algorithm has the useful characteristic that each of the two keys can be used to decrypt messages encrypted by the other key. This characteristic forms the basis for public key encryption schemes. Each individual owns a set of two keys— one is make public while the other is held privately. Anyone wishing to communicate privately with an individual can encrypt the message with the recipient’s public key and then openly transmit the message. Since decryption requires the private key known only by the intended recipient, the communication is secure.

<table><tr><td>Single Key</td><td>Dual Key</td><td>Symmetric Dual Key</td></tr><tr><td> $d_x = e_x$  $e_x[e_x[M]] = M$ </td><td> $d_x \neq e_x$  $d_x[e_x[M]] = M$  $e_x[d_x[M]] \neq M$ </td><td> $d_x \neq e_x$  $d_x[e_x[M]] = e_x[d_x[M]] = M$ </td></tr><tr><td colspan="3">Where: $M$   $e_x$  $d_x$ Plain Text MessageEncryption Key of Entity xDecryption Key of Entity x</td></tr></table>

Fig. 3. Illustration of simple key, dual key and symmetric key encryption schemes.

## 2.2.2. Digital signatures

Digital signatures provide a mechanism by which individuals can both verify the authorship of a message and authenticate that it has not been altered in transit 11,26 . The public key encryption technique <sup>w</sup> <sup>x</sup> discussed above can be used to add a digital signature to a transmission. At the time of submission, the author appends to the message the digital signature derived from the original message and the author’s private key. In principle, this signature could simply be the encrypted version of the message. Any individual can verify the signature by using the author’s public key to decrypt the signature and compare it with the original message. If they are identical, the message is authenticated and authorship confirmed. In practice, a shorter version of the message referredŽ to as the message digest. is used instead of the whole message. The message digest is generated from the original message using a public hashing algorithm. Thus, the authenticator needs to compare the decrypted signature to the result obtained from passing the message through this publicly available algorithm. If the results are identical, the message has been authenticated. If the message has been altered, either innocently or maliciously, the digital signature will not correspond to the message text. Three well-known digital signature systems are the RSA scheme 23,58 , PGP 66 and the U.S. Digital<sup>w</sup> <sup>x</sup> <sup>w x</sup> Signature Standard DSS 26 .Ž . <sup>w</sup> <sup>x</sup>

A digital signature system can also be used to prove non-authorship. An individual needs to show that the digital signature does not correspond to his<sup>r</sup>her public key or keys but does correspond toŽ . some other known public key. The second condition is needed to ensure that the author does not use an unknown encryption key to generate the signature.

Note, any mechanism which can independently prove non-authorship ultimately violates anonymity. Assume there are n participants and it is possible to prove non-authorship. If n<sup>y</sup>1 individuals can prove they did not author a specific contribution, the anonymity of this contribution is lost. This is not to say that a digital signature is not a valuable tool in an anonymous environment. If each member of the group possesses and uses a common session key, then each can generate a digital signature based on this key and their message. This authenticates the source as someone from within the group, but does not compromise the author’s anonymity since all participants have the ability to generate this signature.

## 2.3. Anonymous communication protocols

The body of research dealing with mechanisms to support anonymous communication is quite large. When dealing with GDSS applications, we are particularly interested in those protocols which facilitate anonymous communication across a network. Two important mechanisms in this area are anonymity remailing and Chaum’s 11 untraceable return ad-<sup>w</sup> <sup>x</sup> dress URA protocol.Ž .

Anonymity remailers allow a message to be reliably sent through a standard network while protecting the author’s identity. They can protect against attacks based on message headers as well as traffic analysis. Anonymous remailing is quite useful for one-way anonymous communication. In fact, this technique is often used to post anonymous messages to discussion groups. But what if someone wants to respond privately to an anonymous post? One alternative is for the anonymous remailer to maintain a log identifying each message’s original source. The remailer can then correctly route replies to an earlier anonymous message, creating a two-way ‘anony mous’ dialog. However, such an approach is cumbersome and ultimately impacts the overall system anonymity. There has been at least one instance where the system’s anonymity was breached as a result of such a log kept by an anonymity server 57 .<sup>w</sup> <sup>x</sup>

Chaum’s URA protocol addresses this problem Ž . see Section 2.3.2 . It provides a means to establish a two-way, private discussion while protecting the anonymity of both parties. Combining URA’s with the capabilities of anonymous remailers provide a powerful mechanism to provide anonymous communication.

## 2.3.1. Anonymous remailers

An anonymous remailer is a special type of message server which performs intermediate processing of a message to provide anonymity. Messages sent through anonymous remailers have a special format consisting of the standard network header, an instruction block and the message body 16 . The anony- <sup>w</sup> <sup>x</sup> mous remailer removes the author’s network header Ž . which identifies the source of the message , and processes the message per the directions given in the instruction block. The instructions indicate the next location that the message should be sent, and may request the remailer to encrypt the message or delay its transmission.

The disadvantage of using a single remailer is that this gives a single entity sufficient knowledge to link the author to each message, thereby providing only OA 0 . The level of anonymity can be increased by Ž . passing the message through multiple anonymous remailers, a process referred to as chain remailing. The anonymity level increases because each anonymous remailer in the chain knows only part of the message route—the preceding and succeeding links. All remailers through which the message passes must cooperate to reconstruct the attribution chain linking the author with a posted message.

Thus a remailing chain of length N provides OAŽ . N . Note, a message packet can even pass through the same remailer more than once and still increase the anonymity complexity. Due to encryption, the message packet will change each time it is remailed. As a result a message server will not be able to recognize a packet it has processed previously.

The procedure for preparing a message for a remailer chain is similar to that for a single remailer Ž . see Fig. 4 . The author successively encrypts the message with the public key of each intermediary in the chain. In this example, the contributor is posting a message to a group rather than to a specific individual. Each authorized user possess both the encryption $( e _ { x } )$ and decryption $( d _ { x } )$ keys. None of the remailers have access to the actual plain text message. Since the message is encrypted with a key known only to the group, even if all remailers collude to reconstruct the attribution chain, the content of the message is still secure. The remailers can determine who is communicating, but not the content of the message.

![](/api/attachments/Z6YS3S2J/fulltext/images/fd8d669d6b8b6eb3ff26c49ec2085d1cfb513f6175fce8a5e454e910451ba812.jpg)  
Fig. 4. Representation of a message sent through a remailer chain.

A general chain remailer provides only complete anonymity, since the author is not part of the attribution chain. To provide absolute anonymity, an author could incorporate himself or herself into the remailer chain. Incorporating a single authorized user into the remailer chain creates an asymmetry in routing among the user group. This is undesirable because it is those unique characteristics of a transmission which yield clues as to its source. To achieve symmetry, it would be necessary to include all users in the remailer chain, which for large populations is usually not practical.

There are potential reliability and performance problems with this approach. Implicit in the nested encryption scheme illustrated in Fig. 4 is that the user must specify the message’s exact routing path at the time the message is generated. In essence, this defines a virtual circuit between the source and destination. When this is done, communication reliability is dependent on the reliable operation of each chain server. Failure of any server will cause all messages routed through that server to fail. Also, since the routes are predefined, network congestion cannot be taken into account, tending to increase the transmission time.

This problem can be addressed by using pools of servers, with each server in a given pool having access to that pool’s private key. The user could then specify a logical routing i.e., a pool routing , whereŽ . the physical routing is done dynamically at each hop. This approach provides two benefits. The logical network can be relatively static even through pool membership may change. Dynamic routing would also permit network congestion control, which makes the system less vulnerable to the failure of a server or communication link.

## 2.3.2. Untraceable return address URA protocol ( ) [ ] 11

In an anonymous environment there are situations where participants may want to respond privately to a message. For example, you might want to respond privately to questions posed anonymously in an AIDs or Teen Pregnancy news group while at the same time protecting your own privacy. If you knew the identity and address of the original author, conventional public key encryption would allow private, non-anonymous communication. However, this is not an option since the original message was posted anonymously. It is possible to establish anonymous, non-priÕate communication by anonymously posting your reply to the news group. Unfortunately both fall short of the goal.

Chaum’s 11 URA protocol provides a mecha-<sup>w</sup> <sup>x</sup> nism which enables private, anonymous dialogs using a trusted intermediary such as an anonymity server. Assume that users X and Y are authorized participants in an anonymous GDSS session. As a result, they have access to the group encryption key $( e _ { G } )$ and decryption key $( d _ { G } ) _ { \mathrm { ~ } }$ . A member of the group, User Y, wants to reply to an anonymous posting made by user X Ž . see Fig. 5 .

In Step a, user X submits an encrypted message to the group, routing it through the anonymity server. Included in the message package is the system supplied header, $H _ { \mathrm { U s e r } X }$ , and the doubly encrypted message block. The inner encryption hides the plain text from the anonymity server, while the outer encryption hides the whole message block from everyone else. The message block consists of the plain text message, M, and an untraceable return address $( \mathrm { U R A } _ { M } )$ , and the target destination, which in this case is the GDSS session address, $A _ { G } .$ . The $\mathrm { U R A } _ { M }$ itself consists of three parts—a message specific encryption key, the author’s real address both ofŽ which are encrypted with the anonymity server’s public key and a second message specific encryp- . tion key. These two keys are used to provide a reply message the same level of anonymity and privacy as the original message see steps d and e below . Thus,Ž . the original message’s URA is given by: $\mathrm { U R A } _ { M } \equiv$ $\tilde { e } _ { \mathrm { A S } } [ e _ { M 2 } , A _ { X } ] , e _ { M 1 }$ , where: $\tilde { e } _ { \mathrm { A S } }$ is the anonymity server’s public key, $A _ { X }$ is user $X ^ { \prime } s$ real return address, and $e _ { M 1 }$ , and $e _ { M 2 }$ are message specific encryption keys chosen by user X.

In Step b, the anonymity server removes the user’s header and broadcasts the message to the

$$
U R A _ {R _ {M}} - \tilde {e} _ {A S} [ e _ {M 4}, A _ {Y} ], e _ {M 3}
$$

![](/api/attachments/Z6YS3S2J/fulltext/images/d4b1ab179e5cc44ca9873204c9140f4b94352929eeb107fe463e23bcdde343a3.jpg)  
Fig. 5. Protocol to support Y ’s untraceable reply to an anonymous posting by user X.

authorized group. User Y receives and decrypts the message in Step c yielding the plain text message and the author’s URA. In Step d user Y uses one of the encryption keys $( e _ { M 1 } )$ sent with the original message to encrypt the response, and then uses the URA as a blind address. This encryption blinds the response to all but the original author of the message. This message block is also encrypted with the anonymity server’s public key to keep this transmission private. As shown in Fig. 5, user Y can also include a URA so the original author can continue the anonymous dialog.

In Step e, the anonymity server removes the reply’s header. Decrypting the original message’s URA yields user X ’s true address and the second author-specified encryption key $( e _ { M 2 } ) _ { \it { \Delta } }$ The anonymity server encrypts the reply with this key and transmits the message to user X. This secondary encryption is needed to prevent user Y from tracking the outgoing reply from the anonymity server and thereby identifying the original author of the message userŽ . X . Finally in Step f, user X receives and decrypts the message with the private decryption keys yielding the reply along with a new URA. At this point a private, anonymous dialog has been established.

Each transmission consists of three components, namely: a header indicating the sender’s address, the address of the immediate destination, and a message packet readable only by the immediate recipient. If the message packet is being sent to an anonymity server i.e., steps a and d , then the message packetŽ . is composed of two parts: the subsequent address of the ultimate recipient, and an encrypted message block readable only by the ultimate recipient. Message packets leaving the anonymity server also contain two parts: the URA readable only by the anonymity server and the encrypted message block readable only by the ultimate recipient of the message.

## 3. Types of anonymity

Anonymity can be viewed as a composite of three types of anonymity—environmental, content-based and procedural. EnÕironmental anonymity refers to the extent to which environmental factors affect the anonymity of the communication system. These factors include such elements as: the number of individuals involved in the communication session, the proximity of these individuals, and the level of inter-group familiarity.

This concept relates to what Valacich et al. 64<sup>w</sup> <sup>x</sup> defines as process anonymity—‘‘the extent to which group members can determine who is participating by directly observing who is making a contribution to the process’’. In a centralized GDSS meeting where all participants are within close proximity, it may be relatively easy to gain clues as to authorship by observing the activity level of other participants. However, when the group is dispersed, direct observation is not possible, thereby providing a higher degree of environmental anonymity. The factors involved with environmental anonymity are discussed in more detail in Section 3.1.

It is often possible to glean clues as to a message’s source from the message itself. Content-based anonymity is defined as the extent to which the source of a specific contribution can be identified through the contribution’s content. Contextual clues could be as simple as a by-line or signature, or as subtle as an identifiable theme or distinctive phrasing. Valacich et al. 64 makes a distinction between<sup>w</sup> <sup>x</sup> local content anonymity and global content anonymity. ‘‘Local content anonymity refers to the ability or inability of other group members to Ž . identify the source of a specific contribution during the process. Global content anonymity refers to the ability of someone to review the GDSS transcripts and system logs and identify, after the session, who made a specific contribution during the session’’. It is possible to have all combinations of these two types of anonymity—neither global nor local anonymity; both global and local anonymity; and either one without the other. The issues surrounding content-based anonymity are discussed in Section 3.2.

The third anonymity sub-system is procedural anonymity, dealing with the communication protocol. This aspect of anonymous communication has received the most attention in the academic literature <sup>w</sup> <sup>x</sup> 11,12,58,61 . The different principles dealing with procedural anonymity are discussed in Section 3.3.

The system’s overall anonymity is a composite of the anonymity provided in each of these sub-systems. A useful analogy would be to view anonymity like a system of filters as illustrated in Fig. 6. The anonymity provided by each sub-system filters a specific subset of attribution clues from the system. The impact of each filter is additive, in the sense that as the anonymity increases in each sub-system, so does the anonymity within the whole system. Unfortunately, if one sub-system does not adequately filter its set of attribution clues, the anonymity provided by the whole system is at risk. For example, consider a system which provides absolute content-based and procedural anonymity, but has a physical layout which allows participants to directly observe others as they enter their comments into the system i.e., no Ž environmental anonymity . In this case, even though. messages are free of all content clues and are untraceable, anonymity is totally lost due to the lack of environmental anonymity.

## 3.1. EnÕironmental anonymity

Environmental anonymity deals more with the group makeup and physical setting than the actual communication process. One of the most basic environmental factors is the participant’s level of knowledge concerning the other participants. The identity of participants in a conventional meeting is generally known, or at least readily determined. This is also the case for GDSS meetings held in a centralized meeting room environment 54 . However, in decen-<sup>w</sup> <sup>x</sup> tralized meetings, the identity of those participating is not necessarily known. Even if the list of participants is known, the list of currently active participants may not be readily determined.

![](/api/attachments/Z6YS3S2J/fulltext/images/0b7fed7f51dc71b903098791a4c49cd6eacb4d307132c28469edfb4559d5399f.jpg)  
Fig. 6. Three types of anonymity mechanisms act as filters removing information which could violate contributor’s anonymity.

A minimum group size and participation level are needed to provide an anonymous environment. Experience with the $\mathbf { C M } ^ { 3 }$ system $( \mathbf { C M } ^ { 3 }$ stands for Computer Mediated Meeting Management, a group decision support system described in Refs. 27,30,31<sup>w</sup> <sup>x</sup>. indicates that activity-based anonymity in a decision room environment decreases with group size and is jeopardized with very small groups i.e., less thanŽ five participants . However, in a distributed environ- . ment it may be possible to hold effective, anonymous meetings with fewer participants. In these situations special procedures are needed to maintain anonymity. Participation statistics such as the num- Ž ber active in session must be suppressed when only . two individuals are active in the meeting. If participants know there are only two involved in a session, each participant can accurately attribute all comments made, even with absolute procedural anonymity. Simply suppressing the number of active participants can still fail to ensure anonymity. Traffic analysis will defeat anonymity whenever there is a group size of two, even with complete message imitation.

The group’s history or rather the level of priorŽ member interaction can also play an important role . in environmental anonymity 42,64 . Participants who<sup>w</sup> <sup>x</sup> have previously worked together are more likely to recognize the source of comments than participants in ad-hoc groups. This is usually an important consideration in business applications, because group members will often have some history of interaction.

Environmental anonymity can be compromised when participants are within close proximity. In a centralized GDSS meeting room, it is relatively easy to observe the activity level of other participants. It may even be possible to observe other individuals as they enter information into the system 28 . In such<sup>w</sup> <sup>x</sup> situations, environmental anonymity is relatively low compared to a fully distributed system where participant activity cannot be observed.

A related issue is group composition. This includes aspects of group history, as well as the hierarchical makeup of the group. Individual activity can be influenced when a person of authority, such as one’s supervisor, is involved in the meeting 19 .<sup>w</sup> <sup>x</sup> This effect has been observed in sessions held with the CM<sup>3</sup> system. One particular session involved the upper management of a foreign-owned company. Attending the meeting were the group’s foreign-born executive, brought in to turn-around the company’s Ž recent loses and a number of his subordinates. This. particular executive had an aggressive personality. The meeting was a centralized session, with each participant being able to see each of the other participants.

Initially, group activity was not very substantive. It appeared that the U.S. participants, being unfamiliar with the customs and signals of this new, foreign executive, were concerned about the political impli cations of offending their boss. The researchers subsequently suggested that this executive relocate to a different room and interact with the session remotely. This greatly improved the openness of discussion, and allowed a more detailed discussion of some sensitive issues. The participants apparently felt freer to express their opinions and views. The executive also felt freer to ask questions and make comments without fear of loosing face by taking softer positions or showing ignorance in front of the other group members.

## 3.2. Content-based anonymity

Sometimes within the body of a message there are contextual clues—aspects which provide clues about its source of a message. Many of the contextual clues fall into one of three categories: visual presentation, linguistic clues i.e., grammar and spelling and mes-Ž . sage content. Each is discussed below.

## 3.2.1. Visual presentation

The appearance of a message can provide numerous clues as to the source of a message. These include:

<sup>Ø</sup> Messages posted in upper case

<sup>Ø</sup> Use of a specialized font or character

<sup>Ø</sup> Use of an arbitrary line length i.e., 40 or even Ž 120 characters.

<sup>Ø</sup> Line spacing, list formatting, or inclusion of graphic images

<sup>Ø</sup> Length of sentences number of words in a com-Ž ment.

Some of these clues may stem from the heterogeneity of the user environment. Certain hardware and software environments give the user a richer array of communication tools. Some clues stem from the sophistication of the user. Use of the more advanced features found in the available communication tools requires a certain familiarity with these features. So even when users operate in a homogeneous environment, there may be visual clues which distinguish certain messages from others.

In some situations it is possible to remove visual clues by enforcing standards for visual appearance. However, depending on the capabilities of a given user’s hardware and software configuration, full compliance to some standard may not be possible. Limiting the communication standard to the capabilities of the most restrictive environment may impose barriers to effective communication. Alternatively, it might be possible to run all user input through a filter which would then assure compliance to the standard. Such an approach could convert messages to mixed case, and enforce character and paragraph formatting. Unfortunately, this approach is not always desirable. In some cases, people use visual clues to EMPHASIZE a point. This added emphasis would be lost when the comment is passed through a filter. In some environments, it may not even be possible to use a filter to enforce a standard format. With the movement toward formatted document distribution, some documents are in read-only formats which imbed specific formatting and graphic elements i.e., Adobe’s Acrobat . A central message Ž . filter would not be able to modify such a file format and thus could not ensure compliance with a standard.

## 3.2.2. Linguistic elements

Linguistic elements found in the message are the second potential source of clues. Certain phrasing may be linked to a specific cultural, or religious group. For example referring to an elevator as a lift, or a drinking establishment as a pub may suggest the author has a British or possibly Australian background. Spelling can provide other clues. For example, there are specific difference between British and American spellings of some words i.e., colour vs.Ž color . Some individuals may simply be poor spellers. and consistently spell certain words incorrectly. Others may have a problem with improper word selection i.e., always referring to the Howard JohnsonsŽ restaurant chain as ‘Harold Johnsons’ ..

It is difficult to adequately filter grammatical usage to eliminate linguistic clues. Grammatical structure as well as sentence structure can each be potent sources of linguistic clues. People with good writing skills i.e., an elegant style and a large Ž vocabulary will always reveal themselves. However,. it is possible to eliminate most spelling errors by using a common dictionary. This would also address regional spelling differences, such as the differences between British and American spellings.

## 3.2.3. Contextual clues

The third potential source of contextual clues is the content of the message itself. This is particularly true whenever private knowledge is being conveyed. The reference to some specific incident, the use of a certain phrase, or the inclusion of private information may have special significance to a select group. If a posting has information previously known only by two people, these individuals can deduce who posted the message. This is not to imply that such private information should not be shared, only that the sharing of such information can impact the anonymity of the author. This also illustrates that the relative anonymity of an individual will likely vary within the group. Not all contextual clues will have the same significance to all participants.

There are many potential sources of contextual clues. However, care must be exerted when drawing conclusions as to the source of a message based strictly on message content. Linguistic and style clues are imprecise at best. If some recognizable trait is associated with a specific individual, others may mimic this trait in an attempt to mislead others. This last point is exemplified by an incident that occurred during an anonymous, $\mathrm { C } \dot { \mathbf { M } } ^ { 3 }$ brainstorming session. A group of employees met to critically evaluate management’s performance. Since no single meeting time was convenient to all participants, the system was setup to give employees access over a period of a few days. During this comment period, a highly critical and uncomplimentary comment concerning the department head was entered. This comment also included a signature of an employee. This signature was subsequently determined to be a forgery, since the person implicated by the signature happened to be away on a trip during the time the system was available.

## 3.3. Procedural anonymity

Procedural anonymity deals with how well the communication protocol hides the source of a message. Standard network protocols are not designed for anonymous communication. In fact they attach headers to all transmissions which identify its source. This is done in part to improve the reliability of the communications. As a result, additional procedures are needed to provide procedural anonymity. One such approach is the use of anonymous chain remailers.

Consider the dual message server model shown in Fig. 7. This model consists of four entities. The first entity, the set of authorized users, generate and ultimately receive all messages. The authorized users are also the only individuals which have the session encryption Ž . Ž . e and decryption d keys. All messages are routed through the second entity—the first message server designated as the anonymity serÕer. The anonymity server can identify the source of each message based upon the message’s header. After some processing, the anonymity server sends the message to the third entity—the session serÕer. Although the session server is the last intermediary in the routing chain, this may not be apparent to the session server. Since the message packet is encrypted, the server has no way of knowing if the message packet will be subsequently routed one or more times before reaching its ultimate destination. To further obfuscate the message flow, the ultimate destination site, once it has received the message, could send a dummy message through additional intermediaries. The fourth entity in this model is the complement of the authorized user set—the set of the unauthorized users, denoted as Spy in Fig. 7. All individuals, including the unauthorized user set, can monitor message traffic and can access all message server public keys.

![](/api/attachments/Z6YS3S2J/fulltext/images/000aef9a9ef0c1bb9ddf8b9a4e595bda71d5a8a3a11bfd713d656dd30d8de2a5.jpg)  
Fig. 7. Depiction of a dual server protocol using a symmetric dual key encryption scheme.

User x generates a message, triply encrypting it with the session key, session server’s public key, and anonymity server’s public key before sending it to the anonymity server step a . Each message packet Ž . includes the message header, which is plain text, and the encrypted message block. The encrypted message block includes the message text, which may itself be encrypted, a next destination in case of retransmission, and any supplemental instructions. Each encrypted message block must be understandable by the intended recipient, but the format must not be deterministic. Otherwise, when the message is retransmitted, an attacker could capture this outgoing message and reconstruct the message block from which it was derived. For this reason it is assumed that encrypted message blocks include a dummy text block.

Upon receipt of a message block, the anonymity server decrypts the outer level, discards the dummy text, randomizes the retransmission order, and sends it to the session server, as specified in the instructions included with the message block step b . Ž . Similarly, the session server decrypts the outer message, randomizes the retransmission order, and sends it to the authorized group step c . Upon receipt,Ž .

each participant decrypts the encrypted message yielding the plain text message step d . This lastŽ . step also authenticates the message as one that originated from within the group, since only authorized participants have the session encryption key.

Since the authorized participants perform the final decryption process, they can be viewed as a third server in the system. In fact, the session server may not know that it is the last leg in the routing chain. The session server is simply following instructions when it transmits the encrypted message to the next location. It is possible that this next site will subsequently retransmit the message it receives.

The system illustrated in Fig. 7 has complete procedural anonymity, indicating that both message servers and at least one authorized user must collude to breach anonymity. If the anonymity and session servers collude, the authors can be associated with each posted message, but the plain text of these messages is not known. If complete imitation is enforced, than the value of this information is eliminated.

This procedure consists of five mechanisms which are used to provide complete procedural anonymity, namely:

<sup>Ø</sup> Encrypt messages with session key

<sup>Ø</sup> Remove sender’s header information

<sup>Ø</sup> Reencrypt messages before retransmitting

<sup>Ø</sup> Randomization of transmission order

<sup>Ø</sup> Artificial messages to thwart traffic analysis Each of these is discussed below.

## 3.3.1. Encrypt messages with session key

If all authorized user communication is encrypted with the group’s session key, only a holder of the corresponding session decryption key will be able to read the messages. The group’s use of these closely held session keys also allows each authorized user to identify and screen-out unauthorized messages i.e.,Ž messages from those outside the authorized group ..

Similarly, the use of encryption allows only authorized members to access the session’s messages, even though messages are openly broadcast. Broadcasting encrypted messages in this way has the added benefit that it does not identify the recipients.

## 3.3.2. RemoÕe author’s identification

Network communication protocols attach headers to all messages which identify the address of the sender. If these headers are not removed, messages are not anonymous. In a multi-server system, the first server the anonymity server in Fig. 7 shouldŽ . remove this header. The removal of the author’s identification effectively partitions the sender’s identification and message content.

Relaxing this mechanism reduces the level of anonymity of the system. If the header identifying the original source of the message is never removed, anonymity is completely lost. In an N server system, if the $r ^ { \mathrm { t h } }$ server removes the author’s header, the maximum anonymity complexity is $\mathrm { O A } ( N - r + 1 )$ For example, in Fig. 7, the session server corresponds to $r = 2$ . If the session server has access to the original message header, anonymity complexity is reduced from OA 2 to OA 1 . In this case,Ž . Ž . anonymity is breached if the session server and any authorized user collude.

## 3.3.3. Encrypting intermediate messages

As indicated in Section 3.3.1, messages must be encrypted with the session key to provide end-to-end privacy. Doing so permits only the authorized users to gain access to the plain text message. However, simply encrypting a message does not guarantee anonymity. To illustrate, again consider the dual server model see Fig. 8 . If userŽ . X encrypts with just the session key, the message transmitted would be $M _ { A } = \{ H _ { x } , e _ { g } [ M ] \}$ . Any authorized user intercepting this transmission could decrypt the message and thereby breach the author’s anonymity. Thus, to send the message securely, messages sent to the anonymity server must also be encrypted with the server’s public key.

Similarly, the message traffic sent to the session server must be encrypted with the session server’s public key i.e., Ž $M _ { B } = \{ H _ { \mathrm { A S } } , { \widetilde { e } } _ { \mathrm { S S } } [ e _ { g } [ M ] ] \} )$ . This encryption can either be done in two different ways. If the message sent to the anonymity server is doubly encrypted i.e.,Ž $M _ { A } = \{ H _ { x } , { \tilde { e } } _ { \mathrm { A S } } [ e _ { g } [ M ] ] \} )$ , then the anonymity server could decrypt the message and then reencrypt it with the session server’s public key. Unfortunately, this gives the anonymity server access to the message encrypted only with the session key, thereby reducing the system’s anonymity complexity to OA 1 . This negates much of the benefit of havingŽ . two servers in the attribution chain. The alternative is for the original author to triply encrypt the original message. The inner-most encryption is done with the session key. This encrypted block is then encrypted with the session server’s key, and then the block is finally encrypted with the anonymity server’s public key i.e., Ž $M _ { A } = \{ H _ { x } , \tilde { e } _ { \mathrm { A S } } [ \tilde { e } _ { \mathrm { S S } } [ e _ { g } [ M ] ] \} )$ . When the anonymity server receives the message block, it would decrypt the outer layer and send the result to the session server. Likewise the session server would decrypt the message block and send the inner encrypted block to the final destination.

Some randomly generated dummy text should be added to a message block before it is encrypted. If a message server executes a known, reproducible transformation of the message block i.e., reencrypt-Ž ing with a public key the message transfer can be. traced. The inclusion of random, dummy text which is discarded before retransmission prevents such an attack. For example, in a single server system, assume that an authorized user intercepted the message block $M _ { A } = \{ H _ { x } , { \tilde { e } } _ { \scriptscriptstyle \mathrm { A S } } [ e _ { g } [ M ] ] \}$ The author’s anonymity would be lost even though the authorized user cannot extract the plain text message from the intercepted message. The doubly encrypted text block can be reconstructed with the known message M, group key $e _ { g } { \mathrm { : } }$ , and anonymity server’s public key $\tilde { e } _ { \mathrm { A S } }$ . Adding the dummy text defeats this attack. Thus the message traffic sent to the anonymity server must be in the form $M _ { A } = \{ H _ { x } , { \tilde { e } } _ { \mathrm { A S } } [ e _ { g } [ M ] + \delta ] \}$ , where represents the random text. In a two server system as given in Fig. 8, the message sent from the server would thus be $M _ { A } = \{ H _ { x } , \tilde { e } _ { \scriptscriptstyle \mathrm { A S } } [ \tilde { e } _ { \scriptscriptstyle \mathrm { S S } } [ e _ { \varrho } [ M ] + \delta _ { 1 } ] +$ $\delta _ { 2 } ] \}$ . Using this approach, the anonymity complexity is now OA 2 .Ž .

![](/api/attachments/Z6YS3S2J/fulltext/images/65dba65c0d82c81959c98cf322bca3b8bac23b3780fa6094bc0f7348c10c1f2e.jpg)  
Fig. 8. Depiction of a dual server protocol using a symmetric dual key encryption scheme.

When messages have unique lengths, they can be tracked by matching the length of the incoming and outgoing message packets. This would be true even if the intermediate server reencrypted the messages before retransmission. This problem can be addressed by using standardized packet lengths, or through complete imitation of all messages. This eliminates the uniqueness of the message, thereby eliminating this type of attack.

If the message server simply retransmits the message without any intermediate processing, as in the two examples given in case 1 of Fig. 9, messages can be tracked by matching byte patterns in the two streams. In the first example, the message is plain text whereas in the second example the message is encrypted. In both cases, since there was not any transformation of the message by the server, each incoming message can be matched to the corresponding message leaving the server.

## 3.3.4. Randomize retransmission order of messages

If a message can be tracked as it passes through an intermediate server, the cooperation of this server is no longer needed to establish a link between a message and its author. This is undesirable since it reduces the system’s anonymity complexity. There are at least three ways to track messages—message length, lexicographic matching byte-wise compari- Ž son of input and output streams , and message se-. quencing.

In case 2 the intermediate message server uses a public key to encrypt each message before retransmission. An attacker can track the message by encrypting the incoming message with the set of known public keys and lexicographically matching them with the outgoing messages. Note, such an attack would only work where the key being used to encrypt the message was available to the attacker. This attack can be prevented in two ways. The server could use a closely held encryption key rather than a publicly available encryption key. Alternatively, the server could append some random dummy text to the message before encrypting it with the public key.

1) Retransmit without subsequent processing.

$$
\begin{array}{c c c c} [ H _ {1}, M ] & \longrightarrow & [ H _ {2}, M ] & \text {byte - wise matching of M} \\ [ H _ {1}, e _ {a} (M) ] & \longrightarrow & [ H _ {2}, e _ {a} (M) ] & \text {byte - wise matching of e_{a} (M)} \end{array}
$$

2) Retransmit after encrypting with public key of next server

$$
[ H _ {1}, M ] \qquad \longrightarrow \qquad [ H _ {2}, \tilde {e} _ {a} (M) ] \qquad \begin{array}{l} \text { Using   known   } \tilde {e} _ {a}, \text {   encrypt   } M \text {   and   perform   byte - wise } \\ \text { matching   on   outgoing   stream } \end{array}
$$

3) Retransmit after decrypting message and reencrypting with public key of next server $[ H _ { 1 } , e _ { a } ( M ) ] \quad \longrightarrow \qquad [ H _ { 2 } , e _ { b } ( M ) ]$ tracking based on known processing order

4) Retransmit after decryption, appending of random text, reencryption, and randomization [H1, ea(M)] → R([H2, eb(M + δ)]) secure

Fig. 9. Methods of tracking messages under different processing assumptions.

This random text would alter the encrypted message block such that an attacker could not be able to associate it with the original message block.

In case 3 the incoming message has been decrypted and reencrypted with a closely held key before it is retransmitted. This defeats tracking through lexicographic matching of the two streams. However, if the processing order of the message server is known i.e., first-come-first-server order ,Ž . then messages could still be tracked. An attacker could establish a baseline by sending a message through the server to himself. Messages could then be tracked based upon their relationship to the baseline message.

Case 4 reencrypts the messages and randomizes the transmission order before retransmitting the messages. Reencrypting and appending dummy text prevents lexicographic tracking of the messages. Randomizing the retransmission order prevents tracking based on message sequencing.

## 3.3.5. Using artificial messages to thwart traffic analysis

For a user to be the author of a posted message, he<sup>r</sup>she must have transmitted that message at some time. From this very basic point it can be seen that user activity can be a potent source of authorship clues. In fact, user inactivity can also give clues as to the source of a particular message. If a GDSS participant does not make any transmission during a session, then that individual cannot be an author for any of the session’s contributions.

To eliminate user activity as a source of authorship clues requires complete imitation of message traffic. To completely hide authorship of a k packet transmission, the message server must receive at least one k packet transmission from each user prior to posting. Imitation need not strictly be accomplished through artificial messages. If session participants transmit useful messages having a nominal size of k packets within the communication cycle, message imitation is not needed.

The situation is different for transmissions exceeding the normal packet size. Large, artificial transmissions are only needed when a large useful message needs to be processed. To address this problem the user should notify the server of a pending large message of size $k ^ { \prime }$ packets. The server would then direct all users to imitate a $k ^ { \prime }$ packet message. Upon receipt of this notice, the user can anonymously transmit the useful message randomly among the block of similarly sized, artificial messages. Such a notification mechanism is needed even if large messages are broken into multiple, uniformly sized blocks. A large message will result in a significant increase in traffic from the author’s station. To hide this traffic, all users must imitate this increased activity. Waiting for normal message generation to create the large number of blocks needed to imitate the large message could delay the message, which is undesirable. By enforcing complete message imitation, user activity is no longer a clue as to a message’s source.

Allowing only limited imitation will help to obfuscate authorship, but could provide sufficient information to breach the system’s anonymity. For example, assume there is a session involving 100 participants including three vice presidents VP who jointly Ž . hold information not available to the other members. If $\mathrm { V P _ { 1 } }$ posts a message which includes some of this information, then all three $\mathrm { { V P } ^ { \prime } { s } }$ would know that it must have originated within their group. Assume that the system does not enforce complete imitation and posts this message after 99 members respond—all except $\mathrm { V P } _ { 3 }$ . If $\mathrm { V P } _ { 2 }$ the VP which imitated theŽ message monitors network activity, he. <sup>r</sup>she has sufficient information to identify the source of the comment. If neither $\mathrm { V P } _ { 2 }$ or $\mathrm { V P } _ { 3 }$ imitates the comment, then all $\mathrm { { V P } ^ { \bullet } \mathbf { s } }$ can accurately identify the source of the comment.

## 3.4. A passiÕe serÕer’s impact on procedural anonymity

Up to this point, it has been assumed that intermediate servers have been capable of more than simple store and forward processing. They have been able to play an active role in the communication process through intermediate processing of the incoming message traffic. The discussion now shifts to the impact of using a passive server. With a passive server, users must submit messages in a form readable by only session participants. This can be done by uploading a file encrypted with the session key or appending the information in encrypted form to a database. Since session communications can be decrypted by the whole group, message broadcasting now becomes feasible. If transmissions are broadcast, the load on the network is greatly reduced.

Copies of broadcast messages could also be stored on the server. In this way a user who did not receive a message could download it from the server or Ž actually any user site which received a valid copy of the message . Storing the file in an encrypted state. has the added benefit that the contents are secure even if someone gains access to the file server. Only session participants have the session key needed to decrypt the file.

The lack of an active server also means that the imitation of transmissions may not be needed. Since the server does not do any intermediate processing of the messages, each participant must have the capabil ity to decrypt messages. By monitoring network traffic, participants would also have access to the message’s original transmission header which identifies the author. Therefore, artificial messages would not improve anonymity among the session members. However, the lack of artificial messages may convey information to network eavesdroppers. For example, assume that it is known that the board of directors of a large company sent out 10 teams to evaluate sites for a planned multi-million dollar expansion. Also assume the company is using a GDSS to compare and contrast the information obtained by these 10 groups. Initial traffic from the 10 group leaders may be fairly uniform. However, as sites are eliminated, it is reasonable to assume that the respective group leader’s relative activity in the GDSS session would decrease.

External monitoring of the encrypted network traffic would not yield content specific information. It would, however, convey information as to which sites are in contention based on the activity level. This knowledge could then be used to make investment decisions before the board announces the winning site. Complete imitation would eliminate this potential source of information. There is a trade-off, however—a significant increase in network traffic vs. hiding of activity based information to outside observers.

Using a passive session server may lead to the distribution of the server function among the session members. The only function a passive server fills is that of central session memory. This function can be distributed as long as members have sufficient processing power to handle and store the communication load.

## 3.5. PerceiÕed anonymity

If anonymity is being used as a device to encourage a more open and frank exchange of information, a system’s perceived level of anonymity may be more important than its actual anonymity. When dealing with modern technology, people are often wary of claims that the communication system will protect the anonymity of the participants. This sentiment is typified by a comment made by a $\mathbf { C M } ^ { 3 }$ participant who, after being assured that the system guarantees anonymity said sarcastically ‘‘ . . . Sure. There isn’t anything in the box which keeps track of what each one of us is doing.’’

In sessions dealing with highly sensitive or controversial topics, this underlying mistrust of the system is counter productive and may reduce the overall effectiveness of the decision making process. Going through and explaining the intricacies of the anonymity scheme is of little use, for most participants are not experts in computer and security protocols. Even experts in the field would have to take it on faith that there is no tagging or secondary channel which fully attributes activities within the session. This raises the question of how to convince GDSS participants that their anonymity is indeed protected.

This dilemma was inadvertently solved by an incident which occurred in a $\mathrm { C M } ^ { 3 }$ meeting. This particular session was being held in a centralized decision room. During the session, individuals occasionally left the room and later return to the meeting. On one occasion, a returning participant inadvertently sat at a different station than the one he had previously occupied. When the original occupant of this now occupied station returned, he quietly sat at another open station and continued with the session.

This innocent exchange of physical location was seen as a definitive way to reinforce that the system does indeed preserve anonymity. Disassociating the physical user from the logical user significantly increases the anonymity of the contributor. To exploit this observation, all subsequent session participants were told they could change their physical location whenever they wanted, and that it was their decision to do so. Participants appear to grasp that without some mechanism to log their location, such as a video camera, it is not possible to know who used a specific station at any given time. Since the above procedure has been introduced, hesitation and skepticism regarding anonymity appear to have diminished. It is interesting to note that there has not even been one case in hundreds of sessions in which participants have exercised their right to switch locations. Possible causes for this behavior, include:

1. The issues addressed and comments entered did not cause significant participant anxiety. As a result, participants were not concerned with anonymity.

2. Participants were anxious over anonymity of the system, but this anxiety was not evident in their interaction with the system.

3. Participants were reassured of the system’s ability to maintain anonymity by the researcher’s willingness to allow individuals to migrate to other stations during the session.

In the cases studied, the first alternative does not appear to explain the behavior observed. These sessions focused on a variety of sensitive issues, including sexual harassment, race relations, and managerial performance. During these meetings, participants made many comments detailing personal experiences, with the participants themselves rating many comments as either controversial or highly controversial. Given the subject of the discussions and the personal nature of the messages generated, it is likely that participants were concerned about anonymity. A more detailed study is needed to determine the impact of this simple procedure on the participant’s anxiety over anonymity.

Allowing individuals to change their physical location is well suited for centralized meetings, where all users are in a common room. Unfortunately, when participants are located in different geographic areas, the exchange of user terminals is not viable. Mechanisms are needed to provide this sense of anonymity in distributed environments.

## 4. Implications of anonymous interaction

Maintaining absolute activity-based anonymity through complete imitation comes at a cost of increased network traffic. Consider a system where all messages are routed through an anonymous remailer. Define a communication cycle as the time between initial transmission of a useful message and its eventual posting. Let m be the number of participants in the meeting; n be the nominal message size;  be the fraction of users sending useful messages of nominal size n during a communication cycle; and $\beta _ { i }$ be the size of an extra message sent by user i. The special case $\alpha = 1$ is where all participants have useful messages and therefore there is no need for artificial messages.

Fig. 10 gives the total network load and the fraction of useful load under various user behaviors. Useful load is defined as any movement of useful information. Under these assumptions, a minimum of two messages are required for each useful message —one from the user to the server and another from the server to the users. With complete imitation and identically sized packets the fraction of the useful load increases from $2 / ( m + 1 )$ to 1 as the number of users sending useful messages increases. If all participants send different sized packets, the fraction of the useful load on the network equals $2 / ( m + 1 )$ , which is the same fraction as the unitary traffic case.

## 4.1. Weighing the cost of anonymity

The benefits of supporting anonymous communication must be weighed against the cost of providing that anonymity. Many of the benefits of anonymity are behavioral. It allows a more open discussion of issues and can reduce a participant’s anxiety, which in turn can increase his or her willingness to participate. Since anonymity breaks the link between a contribution and its author, the discussion and analysis of these ideas tends to be depersonalized. This allows individuals to alter their positions without appearing indecisive. It also promotes a less biased analysis of ideas and proposals because these ideas are not associated with a specific individual.

Operational benefits may be derived from these behavioral benefits. Due to increased participation, more information may be shared. Participant anonymity may surface some important information which would not have been presented in a public forum. This is particularly true if participants fear there will be some sort of discrimination or retalia-

<table><tr><td></td><td>Useful Load</td><td>Useful Fraction* of Total Load</td></tr><tr><td>Unitary Traffic(1 useful message)</td><td>2n</td><td> $2/(m+1)$ </td></tr><tr><td>Low Traffic( $\alpha$  messages useful)</td><td> $2\alpha \cdot m \cdot n$ </td><td> $(2\alpha m)/(m+1)$ </td></tr><tr><td>Uniform Traffic(all useful messages)</td><td> $2m \cdot n$ </td><td>1</td></tr><tr><td>Uniform Traffic&amp; user x send  $\beta_{x}$ </td><td> $2m \cdot n + 2\beta_{x}$ </td><td> $\frac{2m \cdot n + 2\beta_{x}}{2m \cdot n + \beta_{x}(m+1)} \xrightarrow{\beta_{x} \gg m \cdot n} \frac{2}{m+1}$ </td></tr><tr><td>All users send unique length messages  $\beta_{i}$ </td><td> $2 \cdot \sum_{i=1}^{m} \beta_{i}$ </td><td> $\frac{2 \sum_{i=1}^{m} \beta_{i}}{(m+1) \cdot \sum_{i=1}^{m} \beta_{i}} = \frac{2}{m+1}$ </td></tr></table>

\* – Useful traffic refers to movement of useful messages

Fig. 10. Traffic load under different user behavior given complete imitation with a single message server. Remailer only rebroadcasts usefu messages. Assumes reliable communication.

tion if the source of this information is made public Že.g., recounting homosexual experiences, or acting as a corporate ‘whistle blower’ . Having more com-. plete information, with greater group participation can improve meeting quality.

Unfortunately, the cost of providing participant anonymity can be significant. As with the benefits, these costs fall into two categories—behavioral and operational costs. Prior anonymity research has highlighted several potential behavioral costs. The tendency toward freeriding and social loafing increases since anonymity prevents the monitoring of participants activity 56 . Anonymity can cause a <sup>w</sup> <sup>x</sup> deindividualizing effect 22,24 . Participants often<sup>w</sup> <sup>x</sup> loose their sense of identity, prompting an increase in disruptive behavior. These by-products of anonymous communication can be disruptive to a meeting thereby reducing the effectiveness of the group.

There are a variety of operational costs associated with supporting anonymity. The support of anonymity can directly impact the type of resources needed. The communication system may have to become more complex to provide the desired level of anonymity. For example, a single intermediate message server can support anonymous communication within a group, however, this provides an anonymity complexity of at most OA 1 . To provide a moreŽ . secure system, the number of intermediate servers must be increased. Also, the support of encryption may require specialized hardware to provide the desired system performance.

Anonymity also impacts resource utilization. Procedures used to provide anonymity often imposes an increased processing and communication load on the system. For example, encrypting communication traffic requires additional processing on both ends— the sender must encrypt the message before transmission and the receiver must decrypt it to be able to read it. This extra processing increases the cost of the system.

A third operational cost is the increased communication delay. This may be unintentional result due to the extra processing required to route a message through multiple servers rather than a single server. Alternatively, the extra delay may be deliberate to thwart traffic analysis attacks.

As previously discussed, a system’s anonymity can be viewed as a composite of three types anonymity: environmental, contextual, and procedural. Each is distinct, with a separate set of benefits and costs. To determine which levels of anonymity to support, it is instructive to look at the benefits and costs for each of the different types of anonymity.

## 4.1.1. Costs and benefits of enÕironmental anonymity

Environmental anonymity involves those factors dealing with the physical communication environment, and how they impact participant anonymity.

Probably the most significant factor is the proximity of participants. A meeting held in a central meeting room tends to provide a much lower environmental anonymity than a fully distributed session. Luckily, software is increasingly available which supports distributed meetings held over local, or even wide area networks 48,59 . Holding GDSS meetings on<sup>w</sup> <sup>x</sup> established corporate networks is a low cost alternative to using dedicated decision room environments. These distributed systems also allow individuals to participate from their offices, thereby eliminating the travel costs.

Environmental anonymity deals with the control over ancillary session information, such as the names of meeting attendees and the number of active participants. Such factors typically fall under software control. Thus, to provide the highest level of environmental anonymity, the underlying GDSS software must be designed to suppress any non-essential information related to the meeting.

The costs associated with providing a high degree of environmental anonymity are relatively low seeŽ Fig. 11 , at least in a distributed environment. There. are no special requirements for the communication network, so the system’s complexity is not significantly increased. System processing demands for environmental anonymity are minimal. Since headers must be removed, message traffic must be routed through at least one intermediate server. This does not represent a significant increase in network load, increasing the network load from n messages in a non-anonymous system to n<sup>q</sup>1 an added messageŽ go to the server; one message is then sent to each participant by the server . Processing loads are low. since the intermediate server would simply remove header information prior to retransmission. Time delays would be minimal, especially if all participants are on the same local network. Artificial delays may be needed to hide performance differences of certain nodes, say due to localized congestion, a slow local network connection or long network routing times.

Strong environmental anonymity is most useful to protect against attacks from within the authorized group. It prevents the direct observation of meeting participants. Under most circumstances, only the authorized group would be in a position to institute such an attack, thus, this type of anonymity is not useful in preventing attacks from other groups.

<table><tr><td></td><td>Environmental Anonymity</td><td>Contextual Anonymity</td><td>Procedural Anonymity</td></tr><tr><td colspan="4">Cost Elements</td></tr><tr><td>System complexity</td><td> $Minimal ^1$ </td><td> $Minimal ^1$ </td><td>Low</td></tr><tr><td>Additional Processing</td><td>Minimal</td><td>Low</td><td>Medium - High</td></tr><tr><td>Communication delay</td><td>Minimal</td><td>Minimal</td><td>Minimal</td></tr><tr><td colspan="4">Usefulness Against Attacker</td></tr><tr><td>Authorized group</td><td>Very Useful</td><td> $Very Useful^2$ </td><td>Very Useful</td></tr><tr><td>Intermediate servers</td><td>Not Useful</td><td>Not Useful</td><td>Very Useful</td></tr><tr><td>Unauthorized group (spys)</td><td>Not Useful</td><td>Not Useful</td><td>Very Useful</td></tr><tr><td colspan="4">Usefulness Against Attack</td></tr><tr><td>Direct observation of activity</td><td>Very Useful</td><td>Not Useful</td><td>Not Useful</td></tr><tr><td>Participant lists</td><td>Very Useful</td><td>Not Useful</td><td>Not Useful</td></tr><tr><td>Analysis of writing style</td><td>Not Useful</td><td>Very Useful</td><td>Not Useful</td></tr><tr><td>Traffic analysis</td><td>Not Useful</td><td>Not Useful</td><td>Very Useful</td></tr><tr><td>Activity analysis</td><td>Very Useful</td><td>Not Useful</td><td>Very Useful</td></tr></table>

1 - Primarily a software implementation issue.  
2 - Contextual anonymity is only useful against authorized user since they are the only group which has access to the plain text messages.

Fig. 11. Costs related to providing different types of anonymity.

Note that increasing environmental anonymity may actually reduce the system’s anonymity, especially from the perspective of those outside the authorized group. If the meeting is held in a centralized meeting room, the GDSS session could use a dedicated communication network. Since the system is self contained, it would be relatively easy to prevent outside monitoring of the session. If the meeting was distributed and held through a shared-use network, the risks would be much greater since the session traffic can now be more easily intercepted.

## 4.1.2. Costs and benefits of content-based anonymity

The second type of anonymity is content-based anonymity—the extent to which the author’s identity can be determined based on contextual clues contained within the contribution. As previously discussed, many content based clues can be eliminated with the use of a message filter through which all messages must pass. Such a filter could correct spelling errors, enforce certain formatting standards Ž . i.e., mixed case rather than upper case , and point out grammatical errors. This could be done in a batch mode, or interactively, such as the spelling and grammar checking incorporated into Microsoft’s Office products. The additional processing demands imposed by such a filter would depend on the extent of the filtering being done. However, based on the capabilities of the on-line filtering built into modern software such as Microsoft Office , the additionalŽ . processing load would likely be modest.

Such a filtering system does limit the flexibility of the system that forces a certain degree of standardization. Individuals would need some minimum system configuration to participate in the meeting. The hardware requirements for text-based GDSS communication are modest compared to those required to run most modern business applications. The use of a filtering system would limit the system’s flexibility with regard to file formats. For a filter to enforce some standard, it must be able to interpret and modify the content of a contribution. This precludes the use of non-editable, preformatted document distribution e.g., Adobe’s Acrobat . This is not a majorŽ . limitation since there are suitable document formats which are editable. Therefore, support of strong content-based anonymity is primarily a software implementation issue, and does not represent a significant on-going expense.

The focus of content-based anonymity is to limit the ability of an attacker to determine the source of a message based on the content of that message. Assuming messages are encrypted with a session key, the usefulness of strong content-based anonymity would be limited to attacks from within the authorized group. Individuals outside this group would not have access to the plain text message, and thus, would not be able to take advantage of the contentbased clues.

## 4.1.3. Costs and benefits of procedural anonymity

The third anonymity sub-system is procedural anonymity, dealing with the communication protocol. The principle benefit of procedural anonymity is that it prevents an attacker from determining the source of a document even with access to the message stream. This is an important feature, especially when messages are sent through public networks. A key component of procedural anonymity is encryption, which has the added benefits that group correspondence can be both private and confidential.

This type of anonymity is unlike the other two in at least two ways—the scope of attacks which it can prevent and the operational costs associated with its implementation. Procedural anonymity is more universal in its ability to prevent attacks. The other two types of anonymity are primarily used to prevent attacks from within the authorized group, whereas procedural anonymity can prevent attacks by individuals which are inside or outside the authorized group. A communication system supporting weak procedural anonymity is susceptible to attack through traffic analysis. For example, if participants transmit their messages in plain text i.e., without any encryption ,Ž . anonymity is trivially breached by any party monitoring the communication channel. Similarly, if there is no attempt to hide the routing of a message i.e., Ž by sending messages through anonymity remailers it . is relatively easy to track message flow, thereby breaching anonymity.

The operational costs associated with procedural anonymity can be quite significant. The protocols used to provide this anonymity can add considerable complexity to the communication system. For example, the support of encryption introduces several non-trivial key management issues. These include: how to remotely negotiate session keys; how are the keys to be managed i.e., escrowed or non-escrowedŽ keys ; how to securely distribution of keys; and how. to deal with individuals joining and leaving the session. Encryption also imposes an additional processing load which may require dedicated hardware.

Encryption alone does not ensure anonymity. One must also prevent the tracking of messages. This necessitates additional mechanisms, such as remailers, message imitation, and the artificial delay of message traffic. Chain remailing further increases the system’s complexity and resource utilization since it routes messages through multiple servers.

These costs can be significant. As a result, some meetings may not justify the use of strong procedural anonymity. Factors to be considered include: a TheŽ . apprehension level of meeting participants. If participants feel that their anonymity is not secure, then their contributions may be more guarded. This is particularly true when dealing with controversial or politically sensitive issues. b The sensitivity of theŽ . issues being discussed—confidentiality may be crucial. c The consequences if anonymity is breached. Ž . For example, being able to associate a specific individual with a comment may have legal implications Ž . Ž .see discussion in Section 4.2 . d The level of existing support for secure communications. If the primary concern is illicit external monitoring, the existing network security may provide sufficient safeguards.

## 4.2. Anonymity and liability

The legal issues of anonymous communication are important, for they may well dictate the level of anonymity which a network or server is willing to support. Who will be held accountable for user activity under an anonymous environment? When an illegal activity is performed anonymously, who can and should be held liable for any damages incurred? The increased availability of information through electronic sources has brought this issue to the forefront 2 . It is relatively easy to anonymously upload <sup>w</sup> <sup>x</sup> and download information on large computer systems accessible by millions of people all over the world. Some of this information is copyrighted and is being uploaded without the prior consent of the author. Further complicating the issue is the international nature of these systems. What may be illegal in one country may be legal in another.

Another potential legal problem, particularly pertinent to GDSS systems, is the anonymous posting of libelous statements. In conventional print and broadcast media, the laws regarding libel provide a means to compensate those who have been libeled. In an anonymous environment, this deterrent is absent. If it is not possible to determine who posted the libelous statement, then they cannot be held accountable. The only identifiable entities are the group as a whole and the service provider.

Some recent court cases have dealt with this issue. Chubby vs. CompuServe 13 involves a case<sup>w</sup> <sup>x</sup> where defamatory remarks concerning Chubby anŽ electronic newsletter were posted on CompuServe’s . on-line, general information service specifically the Ž Journalism Forum . The court found that Com- . puServe’s product was ‘in essence, an electronic for-profit library’ and ‘had little or no editorial control’ over the information posted on their system <sup>w</sup> <sup>x</sup> 13 . As such this case found CompuServe not liable for the defamatory comments posted on their system.

A second case involved anonymous messages posted to Prodigy’s financial bulletin board Money Talk <sup>w</sup> <sup>x</sup> 3 . In this case Prodigy was found to be liable for the comments made by an anonymous user. Although the cases are similar, two important distinctions account for these opposite results. Prodigy ‘held itself out to the public and its members as controlling the content of its computer bulletin boards’ 3 . They also ‘implemented this control <sup>w</sup> <sup>x</sup> through its automatic software screening program, and the Guidelines which Board Leaders are required to enforce’ 3 . These two actions implied an active<sup>w</sup> <sup>x</sup> editorial role not assumed by CompuServe. This editorial role was seen as a conscious decision by Prodigy to delete messages having offensive material to appeal to a perceived desire for a more family oriented service. By taking on the editorial role, they also assumed the added liability associated with that role.

These decisions will likely shape the future landscape for on-line services. Independent of the anonymity issue, service providers will likely reduce the prescreening of messages. No matter how rigorously messages are screened, it is always possible that a message will be posted that some individual finds offensive. The cost of the resulting legal battles will give service providers an incentive to eliminate the editorial controls placed on the system. In addition, the support for anonymous access will likely decrease. Anonymity has been found to have a deinhibiting effect due to the lack of accountability <sup>w</sup> <sup>x</sup> 4,14,21,45 . This can lead individuals to engage in activities they would not consider in a non-anonymous environment. Using the inverse argument, a non-anonymous environment will tend to promote a more responsible behavior. A system which wants to limit abusive and inappropriate messages and behavior, but cannot use editorial filtering due to liability concerns, will tend to move to a non-anonymous system. Although this will not be as effective as a rigorous filtering policy, it exposes the server to less liability.

Regardless of the behavioral and legal implications, there are situations which can benefit from anonymous interaction. For example, whenever a group is discussing sensitive issues i.e., sexual ha-Ž rassment, racism, drug use, or homosexuality , par-. ticipants would likely be more open to express their true feelings or to relate personal experiences if the discussion is anonymous. Anonymity allows groups to more thoroughly explore such topics.

## 5. Conclusions

Anonymous communication is an important concept and has spawned a great deal of research and debate. Using group decision support systems as a backdrop, this paper takes a comprehensive look at the process of providing an anonymous environment.

Most previous GDSS research involving anonymous interactions looked at the impact of anonymity on the meeting’s outcome. Many researches focused on anonymity’s impact on meeting effectiveness, efficiency, or the satisfaction with the result. The focus was not on the anonymity mechanism. Many of these studies took a limited view of anonymity by dealing with systems which simply withheld explicit identification of contributors. Unfortunately, there are additional avenues through which anonymity can be compromised. Some may only be accessible to sophisticated users i.e., monitoring network activity , Ž .

while others are readily accessible to even casual users i.e., observing user activity in a decision Ž room . Failure to recognize and deal with these. additional channels can have a detrimental impact on group interaction. If individuals are skeptical about the system’s anonymity, they will not be as open with their contributions, thereby reducing the system’s effectiveness.

This work takes the position that anonymity is a composite of multiple layers. Three of these layers are addressed—environmental, content-based and procedural anonymity. These act as filters, removing information which threaten the contributor’s anonymity. Each is investigated and mechanisms developed to provide complete procedural anonymity in various system configurations. It is shown that five separate mechanisms are needed to provide this anonymity. The impact of relaxing each of these mechanisms is also investigated.

An important issue not previously addressed in the literature is how to convince contributors that the system does indeed protect anonymity. A partial solution to this problem is presented. Further work is needed to determine how significant a user’s perception of anonymity is on contribution level. Also, appropriate mechanisms are needed to address perceived anonymity in decentralized meetings.

It should be noted that the mechanisms discussed are general in nature, and are not strictly limited to GDSS applications. They would be applicable in other situations which benefit from anonymous communication, such as negotiation systems or 12 step recovery groups i.e., drug, alcohol, and spousal Ž abuse support groups ..

## Appendix A. Proof of mechanisms to provide anonymity

## A.1. Nomenclature

The following nomenclature is used in the following proofs.

<table><tr><td> $H_{x}$ </td><td>Routing header of message sent from entity  $x$ </td></tr><tr><td> $m$ </td><td>Plain text message</td></tr><tr><td> $M$ </td><td>Message packet</td></tr><tr><td>DS(x,M)</td><td>User x's digital signature of message M</td></tr><tr><td>R(·)</td><td>Randomization function</td></tr><tr><td>ex</td><td>Public encryption key of entity x</td></tr><tr><td>U</td><td>Authorized user set—ultimately generates and receives all messages</td></tr><tr><td>V</td><td>Set of intermediate routers</td></tr><tr><td>s</td><td>Source of a message, s ∈ U</td></tr><tr><td>d</td><td>Destination of a message, d ∈ U</td></tr><tr><td>Csd</td><td>Circuit connecting source s with destination d</td></tr><tr><td>n</td><td>Number of intermediaries used in message routing</td></tr><tr><td>Ij∀j=1,n</td><td>Ijrepresents jthintermediary in message's circuit</td></tr><tr><td colspan="2">C={s,I1,I2,...,In,d}∀Ij∈V; s,d∈U; j=1,n</td></tr><tr><td colspan="2">s≡I0</td></tr><tr><td colspan="2">d≡In+1</td></tr></table>

## A.2. Procedural anonymity

This section provides proofs that the mechanisms identified in Section 3.3 are necessary to provide procedural anonymity. Section A.3 presents an Axiom regarding encryption’s ability to provide secure communications, which is the technical basis for the subsequent proofs.

## A.3. Encryption

Axiom 1 Encryption prevents unauthorized access to messages.

Define crypto-analysis as the process of determining the plain text message from the cyphertext without the prior knowledge of the decryption key. The security of modern encryption methods depends on the intractability of determining plain text message from the encrypted cyphertext. For example, the RSA public key algorithm 58 uses a public modu- <sup>w</sup> <sup>x</sup> lus, r, which is the product of two large primes $p$ and q, $r = p q .$ One crypto-analytic approach used to attack the RSA algorithm is to find the prime factors of this public modulus r, thereby revealing the decryption key. There is no formal proof that i theŽ .

factorization of large numbers is intractable or that Ž . ii factorization is needed for the crypto-analysis of RSA. There is, however, substantial evidence of both Ž . Ž . i and ii 60 .<sup>w</sup> <sup>x</sup>

The difficulty of ‘cracking’ multiplicative encryption algorithms such as RSA is believed to beŽ . roughly equivalent to the difficulty of factoring large numbers 1,6,8,60 . Factorization is known to be<sup>w</sup> <sup>x</sup> difficult for large numbers. Factoring of a 116 digit number took 400 MIPS million instructions perŽ second years 50 . A 120 digit number the largest. <sup>w</sup> <sup>x</sup> Ž number factored with a general purpose algorithm as of 1993 took 825 MIPS years 20 .. <sup>w</sup> <sup>x</sup>

Currently, the best known algorithms for factoring large numbers are the quadratic sieve QS 55 andŽ . <sup>w</sup> <sup>x</sup> the general purpose number field sieve NFS 10 .Ž . <sup>w</sup> <sup>x</sup> To factor an integer n, the QS algorithm has a time complexity of OŽ Ž .. exp ln' n ln ln n . The general purpose number field sieve NFS has a complexity Ž . Ž Ž Žof O exp 1.923 ln $n ) ^ { 1 / 3 } ( \ln$ ln $n ) ^ { 2 / 3 } ) )$ <sup>w</sup> <sup>x</sup> 10 . An optimistic estimate for factoring a number n, would be the special purpose NFS for rarefied numbers Ž Ž Žwhich has a complexity of O exp 1.526 ln $n ) ^ { 1 / 3 }$ Žln ln $n ) ^ { 2 / 3 } ) )$ <sup>w</sup> <sup>x</sup> 51 . Using the time complexities for these algorithms, Figs. 12 and 13 gives the number of MIPS-years years to complete at 1 million instruc- Ž tions per second to factor integers of different mag-. nitudes. Also listed is the elapsed time to factor these numbers on a 3000 MIPS super computer. The assumption made throughout the paper is that keys are used with a sufficiently large number of digits that factorization is intractable.

## A.4. Randomization

If a server processes messages in a deterministic way, such as first-in-first-out FIFO , messages canŽ . be tracked as they pass through an anonymity remailer. This is true even when messages are of fixed length and reencrypted by the server preventing the Ž lexicographic identification of incoming messages in the outgoing traffic . A mechanism is needed to . disassociate outgoing message packets from incoming packets. The randomization of retransmission order provides such a mechanism.

Theorem 1 Randomization prevents message tracking based on processing order.

<table><tr><td rowspan="2">Digits</td><td colspan="2">QS</td><td colspan="2">NFS</td><td colspan="2">Optimistic NFS</td></tr><tr><td>MIPS - years</td><td>years</td><td>MIPS - years</td><td>years</td><td>MIPS - years</td><td>years</td></tr><tr><td>100</td><td>91</td><td>11 days</td><td> $\dagger$ </td><td> $\dagger$ </td><td>.13</td><td>21 min</td></tr><tr><td>116 [50]</td><td>400</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>120 [20]</td><td>825</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>150</td><td> $1.2 * 10^6$ </td><td>410</td><td> $3.7 * 10^5$ </td><td>120</td><td>43</td><td>5.1 days</td></tr><tr><td>200</td><td> $4.4 * 10^9$ </td><td> $1.5 * 10^6$ </td><td> $1.4 * 10^8$ </td><td> $4.8 * 10^4$ </td><td> $4.8 * 10^3$ </td><td>1.6 years</td></tr><tr><td>250</td><td> $6.8 * 10^{12}$ </td><td> $2.3 * 10^9$ </td><td> $2.4 * 10^{10}$ </td><td> $8.0 * 10^6$ </td><td> $2.8 * 10^5$ </td><td>94</td></tr><tr><td>300</td><td> $5.5 * 10^{15}$ </td><td> $1.8 * 10^{12}$ </td><td> $2.2 * 10^{12}$ </td><td> $7.5 * 10^8$ </td><td> $1.0 * 10^7$ </td><td> $3.4 * 10^3$ </td></tr><tr><td>350</td><td> $3.2 * 10^{18}$ </td><td> $1.1 * 10^{15}$ </td><td> $1.5 * 10^{14}$ </td><td> $4.9 * 10^{10}$ </td><td> $2.9 * 10^8$ </td><td> $9.5 * 10^4$ </td></tr><tr><td>400</td><td> $1.2 * 10^{21}$ </td><td> $4.0 * 10^{17}$ </td><td> $6.8 * 10^{15}$ </td><td> $2.3 * 10^{12}$ </td><td> $6.0 * 10^9$ </td><td> $2.0 * 10^6$ </td></tr><tr><td>450</td><td> $3.3 * 10^{23}$ </td><td> $1.1 * 10^{20}$ </td><td> $2.4 * 10^{17}$ </td><td> $7.9 * 10^{13}$ </td><td> $1.0 * 10^{11}$ </td><td> $3.3 * 10^7$ </td></tr><tr><td>500</td><td> $7.0 * 10^{25}$ </td><td> $2.3 * 10^{22}$ </td><td> $6.6 * 10^{18}$ </td><td> $2.2 * 10^{15}$ </td><td> $1.4 * 10^{12}$ </td><td> $4.7 * 10^8$ </td></tr></table>

†– QS provides better performance than NFS for small integers.  
Fig. 12. Computational effort needed to factor integers of different sizes.

Proof by contradiction: Define the randomization function R as:

$$
R \left\{m _ {1}, m _ {2}, \dots , m _ {n} \right\} = \left\{r _ {1}, r _ {2}, \dots , r _ {n} \right\}
$$

such that the output ordering is uncorrelated with the input ordering.

Assume that an attacker can determine one or more reference correlations $m _ { \mathrm { a } } \equiv r _ { \mathrm { b } }$ . This can be accomplished by sending a message to himself<sup>r</sup>herself and monitoring traffic flow. Assume that given this information, the attacker can accurately associate incoming and outgoing traffic based on processing order analysis. This violates definition of the randomization function.

![](/api/attachments/Z6YS3S2J/fulltext/images/7a43850033ab9319c530b0716ac1db6c1f5fbd96ac0d0f8ec456cf770f346ba7.jpg)  
Fig. 13. Computational effort needed to factor integers of different sizes assuming 3000 MIPS computer Bellcore’s Massively Paral- Ž lel machine, MasPar, rated at approximately 3000 MIPS ..

## A.5. Incremental routing

Incremental routing can be recursively defined as:

$$
\mathrm{MP} _ {x} = \left[ H _ {x - 1}, M _ {x} \right]; M _ {x} = e _ {x} \left[ D _ {x + 1}, M _ {x + 1} \right] \forall
$$

$$
x = 1, \ldots , n
$$

where: $\mathbf { M P } _ { x }$ , message packet sent to $I _ { x }$ from $I _ { x - 1 } ;$ $H _ { x - 1 }$ , header for $I _ { x - 1 } ; \ M _ { x }$ , message block for $I _ { x } ;$ $D _ { x + 1 } ,$ , destination address for $I _ { x + 1 } ; ~ e _ { x }$ , public encryption key of $I _ { x }$

Where the following procedures apply.

Ž . T1-a The whole routing path is specified by the sender and accompanies the message.

Ž . T1-b Data packets consist of a routing header and a public key encrypted message packet. The outgoing routing headers are independent of incoming message headers.

Ž . T1-c Routing intermediary $I _ { x }$ can decrypt one level of the message packet, $M _ { x }$ , yielding the address of routing intermediary $I _ { x + 1 }$ and a message packet encrypted with $I _ { x + 1 } \mathrm { ' s }$ public key.

Ž . T1-d The last recipient can decrypt the message received yielding the intended, plain text message.

Theorem 2 Incremental routing prevents intermediate routers from associating the message packet’s original source with the ultimate destination using only the knowledge obtained from the message packet.

Proof: Entity $x + 1$ can determine the immediate source of a received message from this header T1-b .Ž . Routing before x is not available since the headers are independent from incoming message headers Ž . T1-b . From T1-c the entity can determine the immediate destination of the message. No subsequent routing information is obtainable by entity x since the message block containing this information is encrypted by T1-c and Axiom 1 . Thus, eachŽ . intermediate entity x can establish a link only from the immediate source $x - 1$ to the immediate destination $x + 1$ . Therefore, if the routing chain contains more than one intermediate router, no intermediate router can link the overall source of a message packet with the ultimate destination using only information obtained from the message packet.

## A.6. Full imitation

Given a set of users U and intermediaries V, $s \in U$ sends a message $m _ { s }$ to $d \in U$ passing through $x \in V .$ . Let full imitation be defined as the process whereby intermediary x delays retransmission of $m _ { s }$ until it has received messages of similar size from all other members of U. The message handling must satisfy the following properties.

Ž . T2-a All messages must be of similar or like size. For simplicity, assume messages are padded with $\xi$ bytes to provide identically sized messages.

Ž . T2-b All message traffic must be encrypted. Message traffic to $x \in V$ must be encrypted with its public key, $\tilde { e } _ { x }$ Ž i.e., $M _ { j } = \tilde { e } _ { x } [ H _ { j } , d , M _ { j } ^ { d } , \xi ] \forall j \in$ U, where $M _ { j } ^ { d } \equiv e _ { d } [ M , \xi ] )$

Ž . T2-c Messages received by the intermediate router must be reencrypted before they are retransmitted. This can be done by either the intermedi-Ž ary or the author using multiple levels of encryption. ..

Ž . T2-d Message retransmission order must be randomized.

Theorem 3 Full imitation of a message, where its circuit includes at least one intermediary, prevents the determination of its ultimate source and destination by an attack based strictly on traffic analysis.

Proof: Assume that an attacker can monitor all traffic flow, having access to the routing header and associated message packet. Information which can be obtained from traffic analysis is limited to:

<sup>Ø</sup> Message size

<sup>Ø</sup> Message content

<sup>Ø</sup> Message sequencing order receivedŽ <sup>r</sup>transmitted by an intermediary.

<sup>Ø</sup> Message’s source

<sup>Ø</sup> Message’s immediate destination

Further assume this information is sufficient to track messages from its original source to destination.

Requiring that all messages are of a standard size Ž . T2-a eliminates the informational content of message length. Since messages are encrypted T2-b , noŽ . information is available concerning message content Ž . Ž . from Axiom 1 . From T2-c and T2-d , messages are reencrypted and their order randomized before they are retransmitted. Therefore, it is not possible to correctly correlate incoming with outgoing messages based on lexicographic or sequential matching.

It is possible to track a message as it travels between intermediate points by monitoring traffic flow i.e., by intercepting the message and readingŽ its header . However, to track a message to its . ultimate destination, one must be able to associate messages entering an intermediate site to those leaving that site. From the arguments given above, this is not possible.

## A.7. Communication header

One function of communication headers is to provide the underlying network a message confirmation mechanism. This is accomplished by including the address of the message’s source.

Let $H ( I _ { j } )$ be defined as the header generated by intermediary $I _ { j } ,$ then we have:

Theorem 4 If $I _ { i } , 1 \leq j < n .$ deletes all header information received from $I _ { j - 1 }$ , and $H ( I _ { i } )$ is independent of all source information contained in the message and its associated header, determining the source of the message based solely on the message header is prevented.

Proof: Assume the opposite. It must be possible to reconstruct the communication circuit based on the cumulative, remaining intermediate headers. However, the header generated by $I _ { j }$ cannot contain any information concerning intermediaries $I _ { k } , \ 0 \leq k < j$ due to the independence with previous source information. Therefore, it is only possible to reconstruct the circuit from $I _ { j }$ to $I _ { n + 1 }$ , which contradicts the initial assumption.

## A.8. Complete procedural anonymity

Consider the multiple serÕer environment illustrated in Fig. 14. It consists of five entities: message author MS , authorized users AU , anonymityŽ . Ž . server AS , session server SS , and unauthorizedŽ . Ž . users Spy . A member of AU wants to anonymouslyŽ . submit a plain text message M. To accomplish this, the author sends a message $M _ { A }$ to the anonymity server, who sends $M _ { B }$ to the session server, who finally sends $M _ { C }$ to the authorized users. After receiving $M _ { C }$ , the users can extract the plain text message M.

Each entity can monitor network traffic. Spy cannot only monitor network traffic but can also illicitly insert traffic into the network. $\tilde { e } _ { \mathrm { A S } }$ and $\tilde { e } _ { \mathrm { s s } }$ represent the public keys of AS and SS, respectively. Each member in the group has both halves of the session specific encryption key set, $e _ { g }$ and $d _ { g }$ . Message traffic consists of a header which identifies theŽ immediate sender of the message packet , and a . message packet, which could include a digital signature and be encrypted. By definition, under complete procedural anonymity all servers must collude to breach anonymity. Stated differently, a subset of message servers, together with one or more group members, cannot breach anonymity.

Theorem 5 Complete procedural anonymity in a multiple server environment requires the following mechanisms:

Ž . T4-a Messages must be encrypted such that an intermediate recipient does not have access to both the plain text message and the original source.

Ž . T4-b Intermediate messages must be modified Ž . i.e., reencrypted before transmitting to prevent lexicographic matching of input and output streams.

Ž . T4-c Any user specific information attached to the M and $M _ { A }$ must be removed.

Ž . T4-d $M _ { B }$ message order must be randomized.

Ž . T4-e Complete imitation of messages is required before posting.

Ž . T4-f $M _ { C }$ message order must be randomized.

Proof of Necessity: Define the following two types of anonymity breaches.

Class I: Being able to associate a plain text message with its author.

Class II: Being able to trace a message from the source to destination without access to the contents of the message.

Ž . T4-a Messages must be encrypted such that intermediate recipients do not have access to both the plain text message and the original source. If M is not encrypted in $M _ { A }$ then anyone can read the header and the message, leading to a class I failure. If $M _ { A }$ is encrypted such that AS can decrypt the message, class I anonymity is lost.

![](/api/attachments/Z6YS3S2J/fulltext/images/283bd717f77fd14978e32048126719e7fbe263a5b6797ae917f8a8cfa27d65e0.jpg)  
Fig. 14. Multiple server environment. Messages are passed from author user Ž . x to anonymity server to session server and finally to the authorized user group. All traffic can be monitored, and an external agent Spy can mimic all traffic.Ž .

Ž . T4-b Intermediate messages must be modified Ž . i.e., reencrypted before they are retransmitted. If messages are not reencrypted by the intermediate servers before retransmission, the message can be tracked from source to destination through lexico graphic comparison of the input and output streams, leading to a Class II failure.

If each intermediary does the incremental encryption, then the last server must reencrypt the message. This is true even though the message is already encrypted with the session key making the plain text unavailable to an attacker. Consider the case where the author sends $M _ { A } = e _ { \mathrm { A S } } [ e _ { g } [ M ] ]$ to AS. AS can decrypt the message yielding the message encrypted with the group key $e _ { g }$ . AS sends $M _ { B } = e _ { \mathrm { { S S } } } [ e _ { g } [ M ] ]$ SS can decrypt the message and must send $M _ { C }$ to the authorized group. If $M _ { C } = e _ { g } [ M ]$ , then AS could associate this message with its author, since it has access to the source information and the $e _ { g } [ M ]$ message packet class II failure . Any authorizedŽ . group member can collude with AS to cause a class I breach. Therefore, SS must reencrypt outgoing messages.

Ž . T4-c Any user specific information attached to the $M _ { A }$ must be removed. Failure to remove header and trailer information which identifies the author would allow SS to know the source of the document Ž . resulting in a class II failure and the authorized group to know the message’s author class I failure .Ž .

Ž . T4-d $M _ { B }$ message order must be randomized. If AS retransmits the messages in a deterministic way, SS can monitor the AS’s input stream and then correlate its input and output streams. This allows SS to track messages from source to destination, a class II failure.

Ž . T4-e Complete imitation of messages required before posting. If only one member of the group generates messages, there is a class I failure.

Ž . T4-f $M _ { C }$ message order must be randomized. If SS retransmits messages in a deterministic way, AS can monitor the SS’s output stream and then correlate its input and output streams. This allows AS to track messages from source to destination, a class II failure.

Proof of Sufficiency:Assume that mechanisms T4- a–T4-f are not sufficient to ensure complete procedural anonymity. There are two possibilities, namely:

Case 1: Anonymity server, Spy and whole authorized group except the author collude to breachŽ . anonymity.

Case 2: Session server, Spy and whole authorized group except the author collude to breachŽ . anonymity.

Case 1: Anonymity server, Spy and whole authorized group except the author collude to breachŽ . anonymity.

The anonymity server has access to the source information of each message packet. This server also knows $M _ { A } \to M _ { B }$ . The mapping from $M _ { B }  M _ { C }$ is only known to the session server and cannot be determined by traffic analysis from T4-a and T4-e . Ž . Therefore class II anonymity is maintained.Case 2: Session server, Spy and whole authorized group Ž . except the author collude to breach anonymity.

A collaboration between the session server and a group member will allow an association between $M _ { B }$ and plain text messages since the session server has access to the mapping of $M _ { B }  M _ { C }$

The mapping from $M _ { A } \to M _ { B }$ is only known to the anonymity server and cannot be determined by traffic analysis from T4-a, T4-d and T4-e . Informa-Ž . tion identifying the user is also removed T4-c .Ž . Therefore class I and II anonymity is maintained.

## A.9. Hiding extraneous information

Axiom 2 Hiding extraneous information improves anonymity.

Proof: Assume the opposite. Consider the following example. Let there be three individuals with the following characteristics.

Name City Time zone Computer system Allen New York Eastern IBM Betty Philadelphia Eastern VAX Carl Chicago Central VAX

If the message header contained the originating city of the message, the source is immediately identified. If instead only the associated time zone or the host computer system is identified, there is not sufficient information to identify the source althoughŽ each does reduce the number of possible alternatives . Combining the information from both the time. zones and the computer system will uniquely identify the source. To distinguish among n items requires at most $\lceil \log _ { 2 } n \rceil$ discriminating facts.

## References

<sup>w</sup> <sup>x</sup> 1 L.M. Adleman, K.S. McCurley, Open problems in number theoretic complexity, II, in: L.M. Adleman, M. Huang Eds. ,Ž . Algorithmic Number Theory, Lecture Notes in Computer Science, No. 877, Springer-Verlag, Berlin, pp. 291–322.

<sup>w</sup> <sup>x</sup> 2 C. Afzali, Internet’s rise spark copyright concerns, Nashville Business Journal 18 1995 30.Ž .

<sup>w</sup> <sup>x</sup> 3 S.L. Ain, Hon. Justice, Stratton Oakmont, vs. Prodigy Servs., Index No. 31063<sup>r</sup>94, Supreme Court of New York, Nassau County, May 24, 1995.

<sup>w</sup> <sup>x</sup> 4 R. Albanese, D.D. Van Vleet, Rational behavior in groups: the free riding tendency, Academy of Management Review 10 1985 244–255.Ž .

<sup>w</sup> <sup>x</sup>5 A. Barua, C.H.S. Lee, A.B. Whinston, Incentives and computing systems for team-based organizations, Organization Science 6 4 1995 487–504.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 Th. Beth, M. Frisch, G.J. Simmons, Public-Key Cryptography: State of the Art and Future Directions, Lecture Notes in Computer Science, No. 578, Springer-Verlag, Berlin.

<sup>w</sup> <sup>x</sup> 7 R.F. Bornstein, Costs and benefits of reviewer anonymity: a survey of journal editors and manuscript reviewers, Journal of Social Behavior and Personality 8 3 1993 355–370.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 G. Brassard, Modern cryptology, Lecture Notes in Computer Science, No. 325, Springer-Verlag, Berlin, 1988.

<sup>w</sup> <sup>x</sup> 9 W. Brauer, G. Rozenberg, A. Salomaa Eds. , Public-key Ž . Cryptography, EATCS Monographs on Theoretical Computer Science, Springer-Verlag, Berlin, 1990.

<sup>w</sup> <sup>x</sup> 10 J.P. Buhler, H.W. Lenstra Jr., C. Pomerance, Factoring integers with the number field sieve, in: A.K. Lenstra, H.W. Lenstra Jr. Eds. , The Development of the Number FieldŽ . Sieve, Lecture Notes in Math, No. 1554, Springer-Verlag, Berlin, 1993, pp. 50–94.

<sup>w</sup> <sup>x</sup> 11 D. Chaum, Untraceable electronic mail, return addresses, and digital pseudonyms, Communications of the ACM 24 2Ž . Ž . 1981 84–87.

<sup>w</sup> <sup>x</sup> 12 D. Chaum, Achieving electronic privacy, Scientific American Ž . 1992 96–101.

<sup>w</sup> <sup>x</sup> 13 Chubby vs. CompuServe, 776 F. Supp. 135, 139, S.D. New York, Oct. 29, 1991.

<sup>w</sup> <sup>x</sup> 14 P.A. Collaros, L.R. Anderson, Effect of perceived expertness upon creativity of members of brainstorming groups, Journal of Applied Psychology 53 1969 159–163.Ž .

<sup>w</sup> <sup>x</sup> 15 T. Connolly, L.M. Jessup, J.S. Valacich, Effects of anonymity and evaluative tone on idea generation in computer-mediated groups, Management Science 36 6 1990 689–703.Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 L. Cottrell, Mixmaster and Remailer Attacks, http:<sup>rr</sup> www.obscura.com<sup>r</sup>loki<sup>r</sup>remailer-essay.html, July 5, 1997.

<sup>w</sup> <sup>x</sup> 17 D.E.R. Denning, Cryptography and Data Security, Reading, PA, Addison-Wesley, 1982.

<sup>w</sup> <sup>x</sup> 18 D.E. Denning, The clipper encryption system, American Scientist 81 1993 319–322.Ž .

<sup>w</sup> <sup>x</sup> 19 A. Dennis, J. Nunamaker Jr., D. Paranka, Supporting the search for competitive advantage, Journal of Management Information Systems 8 1 1991 5–36.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 T. Denny, B. Dodson, A.K. Lenstra, M.S. Manasse, On the factorization of RSA-120, in: D.R. Stinson Ed. , AdvancesŽ . in Cryptology—Crypto ’93, Springer-Verlag, Berlin, 1994, pp. 166–174.

<sup>w</sup> <sup>x</sup> 21 M. Diehl, W. Stroebe, Productivity loss in brainstorming groups: toward the solution of a riddle, Journal of Personality and Social Psychology 53 3 1987 497–509.Ž . Ž .

<sup>w</sup> <sup>x</sup>22 E. Diener, Deindividuation, self-awareness, and disinhibition, Journal of Personality and Social Psychology 37 1979Ž . 1160–1171.

<sup>w</sup> <sup>x</sup> 23 T. El Gamal, A public-key cryptosystem and a signature scheme based on discrete logarithms, IEEE Transactions on Information Theory IT 31 1985 469–472.Ž .

<sup>w</sup> <sup>x</sup> 24 L. Festinger, A. Pepitone, T. Newcomb, Some consequences of deindividuation in a group, Journal of Abnormal and Social Psychology 47 1952 382–389. Ž .

<sup>w</sup> <sup>x</sup> 25 FIPS Publication 185, Federal Information Processing Standards Publication—Escrowed Encryption Standard EES ,Ž . U.S. Department of Commerce, Technology Administration, National Institute of Standards and Technology, U.S. Government Printing Office, Washington, DC, 1994.

<sup>w</sup> <sup>x</sup> 26 FIPS Publication 186, Federal Information Processing Standards Publication—Digital Signature Standard DES , U.S.Ž . Department of Commerce, Technology Administration, National Institute of Standards and Technology, U.S. Government Printing Office, Washington, DC, 1994.

<sup>w</sup> <sup>x</sup> <sup>3</sup> 27 B. Gavish, J. Gerdes Jr., CM , voting mechanisms and their implications, Annals of OR 71 1997 41–74.Ž .

<sup>w</sup> <sup>x</sup> 28 B. Gavish, J. Gerdes, Implications of Wireless GDSS, Working Paper, 1996.

<sup>w</sup> <sup>x</sup> 29 B. Gavish, J. Gerdes, J. Kalvenes, Reward Allocation Mechanisms in an Anonymous GDSS Environment, submitted for publication.

<sup>w</sup> <sup>x</sup> <sup>3</sup> 30 B. Gavish, J. Gerdes, S. Sridhar, CM , Looking into the Third and Fourth Dimensions of GDSS, Integration: Information and Collaboration Models, NATO ASI Series, 1994, pp. 269–299.

<sup>w</sup> <sup>x</sup> <sup>3</sup> 31 B. Gavish, J. Gerdes, S. Sridhar, CM , a distributed group decision support system, IIE Transactions 27 1995 722–733.Ž .

<sup>w</sup> <sup>x</sup> 32 B. Gavish, J. Kalvenes, Economic issues in group decision support systems, Proceedings of the First INFORMS Conference on Information Systems and Technology, 1996, pp. 8–17.

<sup>w</sup> <sup>x</sup> 33 B. Gavish, J. Kalvenes, An economic model of group decision support systems, Proceedings of the 4th International

Conference on Telecommunication Systems—Modeling and Analysis, 1996, pp. 319–329.

<sup>w</sup> <sup>x</sup> 34 B. Gavish, J. Kalvenes, The gains from cooperation in a group decision support system environment, Proceedings of the 4th Industrial Engineering Research Conference, 1995, pp. 410–414.

<sup>w</sup> <sup>x</sup> 35 B. Gavish, J. Kalvenes, Anonymous rewarding in group decision support systems and its implications, Working paper, Owen Graduate School of Management, Vanderbilt University, 1996.

<sup>w</sup> <sup>x</sup> 36 O. Harari, W.K. Graham, Tasks and task consequences as factors in individual and group brainstorming, Journal of Social Psychology 95 1975 61–65.Ž .

<sup>w</sup> <sup>x</sup> 37 M. Hatcher, A video conferencing system for the United States Army, Decision Support Systems 8 1992 181–190.Ž .

<sup>w</sup> <sup>x</sup> 38 S.R. Hiltz, M. Turoff, K. Johnson, Experiments in group decision making: disinhibition, deindividuation, and group process in pen name and real name computer conferences, Decision Support Systems 5 2 1989 217–232.Ž . Ž .

<sup>w</sup> <sup>x</sup> 39 F.M. Jablin, D.R. Seibold, Implications for problem solving groups of empirical research on brainstorming: a critical review of the literature, Central States Speech Journal 43 Ž . 1978 327–356.

<sup>w</sup> <sup>x</sup> 40 F.M. Jablin, D.R. Seibold, Sorenson, Potential inhibitory effects of group participation on brainstorming performance, Central States Speech Journal 28 1977 112–121.Ž .

<sup>w</sup> <sup>x</sup> 41 I.L. Janis, Groupthink, Houghton Mifflin, Boston, 1982.

<sup>w</sup> <sup>x</sup> 42 L.M. Jessup, T. Connolly, J. Galegher, The effects of anonymity on GDSS group process with an idea-generating task, Management Information Systems Quarterly 14 3Ž . Ž . 1990 313–322.

<sup>w</sup> <sup>x</sup> 43 L.M. Jessup, T. Connolly, D.A. Tansik, Toward a theory of automated group work: the deindividuating effects of anonymity, Small Group Research 21 3 1990 333–348.Ž . Ž .

<sup>w</sup> <sup>x</sup> 44 L.M. Jessup, D.A. Tansik, Decision making in an automated environment: the effect of anonymity and proximity on group process and outcome with a group decision support system, Decision Sciences 22 2 266–279.Ž .

<sup>w</sup> <sup>x</sup> 45 N.L. Kerr, S.E. Bruun, Dispensability of member effort and group motivation losses: free-rider effects, Personality and Social Psychology Bulletin 44 1983 78–94.Ž .

<sup>w</sup> <sup>x</sup> 46 S. Kiesler, J. Siegel, T.W. McGuire, Social psychological aspects of computer-mediated communication, American Psychologist 39 10 1984 1123–1134.Ž . Ž .

<sup>w</sup> <sup>x</sup> 47 K. Klein, B. Cheuvront, The subject–experimenter contract: a reexamination of subject pool contamination, Teaching of Psychology 17 3 1990 166–169.Ž . Ž .

<sup>w</sup> <sup>x</sup> 48 M.E. Kranz, V.I. Sessa, Electronic meeting support—meeting makeovers, PC Magazine 13 11 1994 205–211.Ž . Ž .

<sup>w</sup> <sup>x</sup> 49 T. Kuran, Mitigating the tyranny of public opinion: anonymous discourse and the ethic of sincerity, Constitutiona Political Economy 4 1 1993 41–78.Ž . Ž .

<sup>w</sup> <sup>x</sup> 50 A.K. Lenstra, Factoring with two large primes, in: I.B. Damgard Ed. , Advances in Cryptology—Eurocrypt ’90, Ž . Springer-Verlag, Berlin, 1991, pp. 72–82.

<sup>w</sup> <sup>x</sup> 51 A.K. Lenstra, H.W. Lenstra Jr., M.S. Manasse, J.M. Pollard, The number field sieve, in: A.K. Lenstra, H.W. Lenstra Jr. Ž . Eds. , The Development of the Number Field Sieve, Lecture Notes in Mathematics, No. 1554, Springer-Verlag, Berlin, 1993, pp. 11–42.

<sup>w</sup> <sup>x</sup> 52 S. Muftic, Security Mechanisms for Computer Networks, Ellis Horwood, Chichester, England, 1989.

<sup>w</sup> <sup>x</sup> 53 J.F. Nunamaker Jr., L.M. Applegate, B.R. Konsynski, Facilitating group creativity with GDSS, Journal of Management Information Systems 3 4 1987 5–19.Ž . Ž .

<sup>w</sup> <sup>x</sup>54 J.F. Nunamaker Jr., A.R. Dennis, J.S. Valacich, D.R. Vogel, Information technology for negotiating groups: generating options for mutual gain, Management Science 37 10 1991Ž . Ž . 1325–1346.

<sup>w</sup> <sup>x</sup> 55 C. Pomerance, The quadratic sieve factoring algorithm, Lecture Notes in Computer Science, No. 209, Springer-Verlag, Berlin, 1985, pp. 169–182.

<sup>w</sup> <sup>x</sup> 56 K.H. Price, Decision responsibility, task responsibility, identifiability, and social loafing, Organizational Behavior and Human Decision Processes 40 3 1987 330–345.Ž . Ž .

<sup>w</sup> <sup>x</sup> 57 J. Quittner, Unmasked on the Net, Time, New York, March 6, 1995, 72–73.

<sup>w</sup> <sup>x</sup> 58 R.L. Rivest, A. Shamir, L. Adleman, A method for obtaining digital signatures and public-key cryptosystems, Communications of the ACM 2 1978 120–126.Ž .

<sup>w</sup> <sup>x</sup> 59 J. Salemi, Conferencing software—let’s interface, PC Magazine 13 11 1994 191–204.Ž . Ž .

<sup>w</sup> <sup>x</sup> 60 A. Salomaa, Public-key cryptography, Springer-Verlag, Berlin, 1990.

<sup>w</sup> <sup>x</sup> 61 B. Schneier, Applied Cryptography: Protocols, Algorithms, and Source Code in C, 2nd edn., Wiley, January, 1996.

<sup>w</sup> <sup>x</sup> 62 L.L. Tung, A.R. Heminger, The effects of dialectical inquiry, devil’s advocacy and consensus inquiry methods in a GSS environment, Information and Management 25 1 1993Ž . Ž . 33–41.

<sup>w</sup> <sup>x</sup> 63 J.S. Valacich, A.R. Dennis, J.F. Nunamaker Jr., Group size and anonymity effects on computer-mediated idea generation, Small Group Research 23 1 1992 49–73.Ž . Ž .

<sup>w</sup> <sup>x</sup> 64 J.S. Valacich, L.M. Jessup, A.R. Dennis, J.F. Nunamaker Jr., A conceptual framework of anonymity in group support systems, Group Decision and Negotiation 1 3 1992 219–Ž . Ž . 241.

<sup>w</sup> <sup>x</sup> 65 V. Vroom, L. Grant, T. Cotton, The consequences of social interaction in group problem-solving, Organizational Behavior and Human Performance 4 1 1969 77–95.Ž . Ž .

<sup>w</sup> <sup>x</sup> 66 P. Zimmerman, The Official PGP User’s Guide, MIT Press, 1995.

![](/api/attachments/Z6YS3S2J/fulltext/images/238c9865a21b750fe6322ae961e67ded305b2ee02624b6bed45c4b970eda3c05.jpg)

Bezalel Gavish received the BSc in industrial engineering 1967, MSc and PhD degrees in operations research, Technion —Israel Institute of Technology, in 1970 and 1975, respectively. Professor of MIS at Owen Graduate School, Vanderbil University. 1988 Grace Murrey Hopper Professor at the Naval Postgraduate School, Monterey, CA. Was a Visiting Faculty Member at IBM Watson Research Center, Bell Laboratories, GTE Laboratories, NTT Laboratories, among

![](/api/attachments/Z6YS3S2J/fulltext/images/44ca609c657950372e183078213129d81c32697e22adb4eb78193740fc075f96.jpg)

John Gerdes received the BS and MEng degrees in Mechanical Engineering in 1976 and 1977 from Cornell University; a MBA in 1981 from Lehigh University; and a MS and PhD degrees in 1994 and 1996, respectively, from Vanderbilt University. He was a Visiting Faculty Member in the Fisher College of Business, Ohio State University from 1996 to 1997. Currently, he is an Assistant Professor, Information Systems at A. Gary Anderson Graduate School of

others. Consultant to numerous corporations and government agencies. Editor-in-Chief of Telecommunication Systems, and serves on the editorial board of many journals. Published over 100 papers in his areas of expertise. Research interests span the design and analysis of computer communication networks, distributed computing systems, combinatorial optimization, scheduling and routing in manufacturing and logistic systems and Low Earth Orbit satellite systems.

Management, University of California, Riverside. Research interests include group decision support systems, electronic commerce, and telecommunications.
