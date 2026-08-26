---
otero_id: 3748
otero_key: "CBJHGETB"
title: "Transparent Safe"
authors: "Ying Sai"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.04.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Transparent Safe

Ying Sai

Department of Finance and Computer Information Systems, Loyola Marymount Univesity, 1 LMU Drive, Los Angeles, CA 90045, United State

## a r t i c l e i n f o

Article history: Received 18 December 2007 Received in revised form 30 April 2008 Accepted 30 April 2008 Available online 10 May 2008

Keywords: Transparent Safe Online auction Online fraud Settlement

## a b s t r a c t

To prevent online auction fraud, this study introduces an online auction fund-item exchange mechanism called Transparent Safe. The Transparent Safe allows the buyer and the seller to see the amount of funds inside the safe, without the ability to remove any of it without proper keys. To obtain the necessary keys, both of them have to follow a set of pre-de<sup>fi</sup>ned protocols and perform a series of con<sup>fi</sup>rmable actions. This research shows that the best strategy for both sides of the exchange is to follow this protocol precisely.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Auctions on the Internet have grown from a fascinating new exchange medium into an established business practice. At any time of the day, there are hundreds of online auctions taking place trading goods small and large; as small as a postage stamp and as large as real estate properties. Studies have shown that “online auctions trade billions of dollars' worth of goods each year, and are growing at a rate of more than 10% per month.”[13] This rapid growth is due largely to the advantages that online auctions offer, which can be summarized as follows:

• Lower listing fees — Online auctions have much lower listing fees than traditional auctions, which translate into more pro<sup>fi</sup>t for the sellers and lower costs for the winning bidders.

• Easy access — There are fewer geographical limitations compared to traditional auctions. Online auctions operate through the Internet; anyone can participate as long as he has a computer with an Internet connection.

• Longer bidding time — Online auctions usually last for 7 to 14 days, and are accessible 24 h a day. The sellers can monitor auctions; bidders can submit their bids at their convenience without feeling pressured. A longer bidding window gives the buyers opportunities to participate in multiple auctions simultaneously or do some comparison shopping among different online auctions. The buyers don't have to be professionals; they have time to do research on the market value of the item they intend to buy, even after auctions have started.

Combine the easy access provided by Internet technology and the less intimidating environment and it is not surprising that Internet auctions have outstripped traditional auctions, successfully drawing together far larger numbers of buyers and sellers.

However, with such convenience and a huge number of items to choose from, why isn't the online auction business larger? An interesting phenomenon affecting the major online auction sites, in many categories, is that despite the above advantages and the large number of trades that take place each day, the average sales price is only \$30, which is much lower than traditional auctions. This puzzles some scientists. Is this related to the (still) small incidence of fraud reported in online auctions? Some researchers feel there is nothing to be alarmed about. Lucking-Reiley [13] stated in his empirical study, “Indeed there have been a number of cases of fraud reported by bidders in online auctions. However, the amount of fraud is tiny compared with the number of transactions which take place.”

Sherman Kwok, president of i-Escrow, a pioneering company in online <sup>fi</sup>nancial transactions, indicated that in July 1999 his <sup>fi</sup>rm's average per-sale amount was approximately \$300 [13]. This shows that escrow services were generally used only for the most expensive items purchased online. Other research [1] has identi<sup>fi</sup>ed factors that affect the behavior of buyers in an online auction market. It indicates that under certain high-risk conditions, such as a high item price, or a questionable seller reputation rating, buyers tend to use escrow services more often. The results of these studies all suggest that a more secure fund-item exchange system could, at the very least, lead to higher average sales amounts for the online auction market.

Another study [6] examines the effectiveness of trust mechanisms in Internet auctions. It compares two different types of auctions for collectable stamps: the collectable stamp section of general auction sites such as eBay and the stamp specialty site Michael Rogers, Inc. The general sites' mechanism for providing secure transaction is to rely on a voluntary, self-reported reputation system [11,15]. In contrast, the specialty site usually takes possession of the items from the seller, and then provides the seller with a whole range of value-added services, such as estimating the value of the items, providing standard item descriptions, verifying payment and delivering the items to the buyers. These services have greatly reduced information asymmetry between the sellers and the buyers. Instead of building trust between the sellers and the buyers, Michael Rogers acts as a mediating third party that is trusted by both the buyers and the sellers [6]. This study concludes, “The observed price difference between eBay and Michael Rogers are driven primarily by the relative effectiveness of trust mechanisms in the two markets.” Another insightful study has suggested an economic incentive mechanism — the Trusted Third Party — to serve the online auction community [2].

Our research into building a more trustworthy <sup>fi</sup>nancial transfer instrument for online auctions has led to the design of the Transparent Safe, an automatic fund-item exchange mechanism that would provide secure exchange of items and funds between sellers and winning bidders, without case-bycase intervention or third-party involvement. As soon as users see how automatically and easily problems are cleared up and losses are avoided, they will have ample incentive to demand its use in future transactions.

In this paper: Section 2 reviews the literature on online auctions and building trust online. We show what the challenges are in building trust online and what measures have been taken to improve it. After the literature review, in Section 3, we brie<sup>fl</sup>y introduce terminology and concepts of Internet communication protocols and cryptography. Then in Section 4, we present the fund-item transfer protocol, which is designed for person-to-person fund-item exchange in online auctions. Section 5 represents a mathematical presentation of this protocol, based on automata theory, and proof that there is no advantage to being dishonest in the settlement process. In the concluding section, we examine the implications and potential contributions of the Transparent Safe to the problem of building trust in online auctions, as well as future research that may follow.

## 2. Literature review

The concept of the Transparent Safe stems from research in many different <sup>fi</sup>elds. It started with a question of why online auctions usually sell items with values much lower than those sold in traditional auctions. The few existing empirical studies that were mentioned in the Introduction indicate that whenever a more secure fund-item exchange mechanism is used, the average sales price tends to be signi<sup>fi</sup>cantly higher, whether the mechanism is provided through a third-party escrow service or by the auction site itself. Two other questions follow: what have people done to identify the root of the problem and what possible methods of mitigation have been suggested? In this section, we will <sup>fi</sup>rst review the research into building online trust.

## 2.1. Building trust online

E-commerce enables individuals to contact other individuals — complete strangers — who are located hundreds or thousands of miles away, to exchange information, send money back and forth and trade goods with one another. No third-party introductions are made, no face-to-face meetings occur, no long-term commercial relationship is expected. This is one of the major advantages of e-commerce [10]. However, it also gives a few dishonest individuals the opportunity to cheat others for <sup>fi</sup>nancial gain. How can one individual trust another to do what he is supposed to do in a one-off business transaction on the Internet? Online trust is an especially challenging issue in consumer-to-consumer e-commerce [4,7]. For example, a web user is using PayPal [8] (a web service that allows users to send money through the Internet) to send money from his credit card or bank account to another web user. How can he be sure that some hackers in Chelyabinski, Russia, will not steal his credit card number [20]? Alternatively, how can a buyer of a book using Amazon.com be sure that no one is monitoring each keystroke as he browses the Internet for the right book? How can an Internet user be sure that his clickstream will not be collected and sold to someone for some unknown purpose? One study [5] pointed out: “Online interactions represent a complex blend of human actors and technology systems. In light of this complexity, with what or whom can we meaningfully speak of building trust relationships? Should they be with the systems? Should they be with its developers? Website designers? Should they be with online organizations? Other users?” [14].

## 2.2. The SSL security system

Insecurities associated with both consumer-to-consumer and consumer-to-business online transactions have certainly in<sup>fl</sup>uenced consumer behaviors. This has been shown in a study which reveals how consumers' payment choice changes given different levels of uncertainty related to online transactions [25]. Many online businesses have moved toward establishing bettersecured online transactions through certi<sup>fi</sup>cation as a way to gain trust from users, businesses and organizations [2]. Secure Sockets Layer (SSL), a security system marketed by VeriSign, Inc., is a good example [21,23]. SSL, originally developed by Netscape Communications, is an information technology for securely transmitting information over the Internet. The SSL protocol has become the universal standard among authentication websites for web browser users, as well as for encrypting communications between users and web servers.

SSL server authentication allows users to con<sup>fi</sup>rm a web server's identity. Web browsers automatically check the server's certi<sup>fi</sup>cation and public ID to make sure they are valid and were issued by a certi<sup>fi</sup>cation authority. SSL encryption establishes a secure channel that enables all information sent between a user's web browser and a web server to be encrypted by the sending software and decrypted by the receiving software, thus protecting private information from interception over the Internet. In addition, all data sent over an encrypted SSL connection is protected with a mechanism for detecting tampering; that ${ \mathrm { i } } s ,$ to automatically determine whether the data has been altered in transit. This means that users can con<sup>fi</sup>dently send private data, such as credit card numbers, to a web site, trusting that SSL keeps it private and con<sup>fi</sup>dential.

## 2.3. Online escrow service

i-Escrow [12] is an Internet escrow service. Its standard escrow procedure is:

1. The buyer sends payment to the escrow agent.

2. The agent veri<sup>fi</sup>es payment before the seller ships the goods to the buyers.

3. The buyer then has a short examination period, to make sure that the item meets its description in the auction.

4. After the buyer indicates consent to the transaction, the escrow agent releases the funds to the sellers.

i-Escrow essentially veri<sup>fi</sup>es the payment and holds it until the buyer accepts the merchandise; only then will the escrow agent transfer the funds to the sellers. This settlement procedure has been a dramatic improvement over the method for feedback used by eBay. Nevertheless, this service still leaves room for cheats. For example, after receiving an authentic item from the seller, the buyer claims that the item he has received is fake or defective, and refuses to give consent to the escrow service which now has to investigate who the defrauding party is. Did the seller send a counterfeit item? Is the buyer making a fraudulent claim? Is there a misunderstanding about the description of the auctioned item? With all these possible scenarios to contend with, i-Escrow is not the silver bullet for all the problems plaguing fund-item exchanges for online auctions.

Some current analyses of building trust online concentrate on various methods of generating trust from online users by mimicking face-to-face conversation [16], reputation building [15] or certi<sup>fi</sup>cation [21]. These tend to be either too timeconsuming, too dependent on self-reporting, or too intrusive — online users don't want to share a lot of personal information or give up anonymity. Others have developed a technical approach to protecting each transaction [18,19]. I-escrow uses a trustedthird-party business model to solve some online security problems, but it requires extra steps and a mutual agreement by seller and buyers to include this outside agency in the transaction. To make settlement processes more reliable and dependable, a new secured online transaction mechanism has to be in place. Such a system should consider all possible attacks from hackers, dishonest users and even designers or maintenance crews of online organizations. Only after security measures are up to a universal comfort level can high-value commercial relationships can be established. And only then can e-commerce as a whole realize its potential in the larger economy.

A good analogy is the airline industry and airport security systems. In its infancy, neither passengers nor airline executives worried too much about security. But a rash of bombings and hijackings in the 1970s brought security gates, metal detectors, cameras and bomb-snif<sup>fi</sup>ng dogs into airports throughout the United States [3]. Without these measures, the traveling public would have abandoned airlines no matter how convenient they had become. Now, before boarding, all passengers know they will be subject to intrusive screening to detect <sup>fi</sup>rearms and explosives. They don't mind being asked whether they packed their bags by themselves. Most passengers follow these regulations without hesitation, accepting them as the price they pay for their own safety. With these no-nonsense, technically reliable measures, airports and airlines have been able to maintain a level of safety high enough to keep the majority of the population as customers. Without these technologies and equipment in place, it is hard to imagine the airline industry growing as powerful as it is today.

From our review of current research as well as the practical implementation of measures for building trust online, we can see that every common business relationship is covered. Besides the study on i-Escrow, there is no existing research that is particularly focused on the fund-item exchange mechanism for e-commerce. From this literature review, we conclude that:

1. It takes a long-term interaction for two parties to build trust. 2. Trust in a third party solved some of the fund-item exchange problems, but not all.

3. Reputation building [24] from a feedback form is not accurate. It also takes a long time and requires a large number of users. A major shortcoming is that the identity of the user can be changed at will. Whenever the user feels that his reputation is not desirable, the user can assume a brand new identity and continue to trade.

Based on what we have learned, we have developed the Transparent Safe, which is a fund-item exchange mechanism that could assist online trust building without human intervention.

## 3. The design of the Transparent Safe

The concept of Transparent Safe is built upon a foundation of the seller's con<sup>fi</sup>dence for his/her goods. It requires the seller <sup>fi</sup>rst to deposit a certain amount of value in the Transparent Safe to signify his/her seriousness and con<sup>fi</sup>- dence for the goods. This seems counter-intuitive and is very different from the common procedure used in the normal business transactions in the physical world. However, in online transactions where everything seems to be “virtual”, this requirement provides an essential link between the virtual world and the real world. The Transparent Safe protocol begins when the auction is completed and the winning bidder is identi<sup>fi</sup>ed. Transparent Safe, as suggested by its name, consists of a feature that allows both the seller and the buyer to see each other's movement before they make the next decision. The protocol is built upon a mathematically sound procedure so that if any party deviates from the expected norm, s/he will be warned and eventually punished for any cheating actions.

The Transparent Safe is like a regular safe in the sense that it has the function of storing valuables and that only the people with correct keys can withdraw items from the Safe. However, unlike a real-world safe, it is transparent so that both the buyer and the seller can see the amount that is in the Safe. The Safe is not a physical container; instead, it exists in cyberspace, and anyone with permission can have access to it, regardless of his or her geographical distance relative to the Safe. The Transparent Safe is protected from robbers not because it has a tough outer shell, but from its capability of resisting attacks from Internet hackers. The safety also comes from the way it generates and distributes keys [17]. To transfer funds from the Transparent Safe, the seller/buyer needs to have a secret password from the other party. This password works like a key for a physical safe, but it can be transferred via Internet.

## 3.1. The Transparent Safe fund-item exchange protocols

Let VF be the amount of the <sup>fi</sup>nal sales price from the auction. Let Vf be the settlement fee that the seller has to put down. The seller may get all or a partial amount back depending on the result of the sale. Both buyer and seller have two keys each: one private key and one corresponding public key. The Safe (see following protocol step 3) gives these keys to them. The buyer has a private key B1 and a public key B2, they are the keys will be used to open the safe for a particular transaction. Similarly, the seller has a private key S1 and a public key S2. All public keys are displayed so both sides of the transaction would be able to see. The Transparent Safe generates B1, B2, S1 and S2, with a certain limit on the length of time the keys are available. The Transparent Safe protocol consists of the following steps and Fig. 1 is a graphical illustration of the same procedure.

1. The seller and the buyer give their credit card information to the Transparent Safe.

2. The Transparent Safe veri<sup>fi</sup>es their credit card information. If the information is valid, the Transparent Safe charges amount VF on the buyer's card for the item, and charges Vf on the seller's card as the settlement fee. The amount VF and Vf are in the Transparent Safe. Both the buyer and the seller can see VF and Vf in the safe.

3. The Transparent Safe gives B1 and B2 to the buyer, and gives S1 and S2 to the seller. Public keys B2 and S2 can be made public.

4. The buyer gives the seller her e-mail address and mail ing address.

5. The seller encodes message SM1 <sup>fi</sup>rst with the seller's private key S1 and then with the buyer's public key B2, and prints this encoded message on a one-time-useonly sticker. The seller attaches the sticker to the item securely. The seller mails the item to the buyer and requests a return receipt.

6. Upon receiving the item, the buyer signs a return receipt with her regular physical signature.

7. The buyer decodes the message on the sticker <sup>fi</sup>rst with her private key, then with the seller's public key to get SM1. At the same time, the buyer also con<sup>fi</sup>rms that the item comes from the seller, not any other person.

8a. The buyer exams the item. If the item is as described, the buyer sends BM1 encoded with the seller's public key to the seller to con<sup>fi</sup>rm the purchase.

9a. The seller enters both BM1 and B2 and the seller's private key S1 into the safe.

10a. If they are all correct, the Transparent Safe will transfer amount VF to the seller's account.

11a. The Transparent Safe credits Vf back to the seller's credit card. The entire transaction is completed. If the item is not what was described, then the protocol will follow the alternative route.

8b. The buyer exams the item, if the item is not what was described, the buyer will not send BM1 to the seller, and instead, she returns the item to the seller.

9b. The seller acknowledges that the item is fake or defective, the seller encodes SM2 with the buyer's public key B2 and sends it to the buyer via e-mail.

10b. The buyer enters SM2 and the buyer's private key B1 into the Safe.

11b. If everything correct, the Safe will credit VF back to the buyer.

12b. Vf remains in the safe.

If at 10b, the seller does not acknowledge that the item is fake or defective, and does not give S2 to the buyer, then the protocol follows another path.

10c. The seller does not acknowledge that the item is fake or defective, and does not give S2 to the buyer.

11c. After time T (T can be days or a few weeks), the fund VF will be transferred back the buyer's account and the settlement fee Vf will remain in the safe.

The expense of maintaining a directory of public keys would be large if we publish all the public keys for all the users. Currently, each set of private and public keys is only distributed by the Safe to the winning bidder and the seller, not to anyone else, and each set is only used in association with one Safe (or one settlement). Therefore, it may not be necessary to maintain a large public key directory for all users.

There is a difference between this protocol and regular computer communication protocols. In computer protocols, communication is established between computers not humans. Computers are programmed to follow the protocols exactly; taking any action that is not described in the protocol will result in no response, therefore the system remains in the same state or goes into an error state. In our protocols, the sellers or buyers may not follow the protocols exactly, or not execute them in the prescribed sequence. This requires us to consider actions for every possible state. In the following few sections, we will try to describe all possible situations.

## 3.2. Verification of the Transparent Safe protocols

In this section, we will use automata theory and language [9] to describe and illustrate all the possible states and actions in the Transparent Safe mechanism.

Basic de<sup>fi</sup>nitions:

1) Q is a set of states. Symbols q and p are states. q0 is the initial state.

2) Σ is an input alphabet. Symbols x1 and x2 are input symbols.

3) δ is a transaction function.

4) F is a set of <sup>fi</sup>nal states. Final states are marked with double circles.

5) The transaction diagram is a directed graph. The vertices of the graph correspond to the states. If there is a transaction from state q to state p on input x1, then there is an arc labeled x1 from state q to state p in the transaction diagram (see Appendix A).

![](/api/attachments/CBJHGETB/fulltext/images/7e200b307c2b61868e43d874b26b684ab315dc417045532049dff7d86a6b7795.jpg)  
Fig. 1. Transparent Safe transaction diagram.

## 3.2.1. Description of states

q0 1; 2; 2; 2; 1; 1; 1 :

q0 is the initial state. That is when the online auction ends and the settlement processes begin. In this state, the seller has the item; the winning bidder or the buyer has the funds. The buyer has two keys (or messages): B1 and B2, and the seller has two keys: S1 and S2. The seller has the settlement fee.

Both the seller and the buyer give credit card information to the Transparent Safe. If the buyer's credit card information is valid, the buyer's credit card will be charged with an amount equal to the purchase price. Once this action is taken, the state changes from q0 to q1.

q1 1<sub>ð</sub> <sub>Þ</sub> ; 0; 2; 2; 1; 1; 1 :

In state q1, the seller has the item; the funds are transferred to the Transparent Safe. The status of the keys and the settlement fee remains the same. If the seller's credit card information is valid, the Transparent Safe will charge the seller's account with an amount equal to the settlement fee. The state changes from q1 to q2. If the seller sends the item to the buyer, then q1 moves to q15. If the seller sends the settlement fee to the buyer, q1 moves to q17.

q2 1; 0; 2; 2; 1; 1; 0 :

The settlement fee is charged on the seller's credit card. After that, the seller prints the <sup>fi</sup>rst key (S1) on a one-timeuse sticker and attaches the sticker to the item. Through regular mail service, such as the US Postal Service, United Parcel Service or FedEx, the seller mails the item to the buyer and requests a return receipt. All other variables remain the same.

q3 2<sub>ð</sub> <sub>Þ</sub> ; 0; 2; 2; 2; 1; 0 :

The buyer signs the return receipt and the item is in the buyer's hands (x1 changes from 1 to 2). Along with the item, the buyer also receives S1 — the <sup>fi</sup>rst key from the seller (x5 changed from 1 to 2). Since return receipts are not always reliable, the buyer should send B1 (the buyer's <sup>fi</sup>rst key) to the seller to con<sup>fi</sup>rm receipt of the shipment.

q4 2<sub>ð</sub> <sub>Þ</sub> ; 0; 1; 2; 2; 1; 0 :

After receiving the item, the buyer inspects the item. If the buyer accepts the item, she will send B2 (the buyer's second key) to the seller through e-mail. The state will change from q4 to q5. If the buyer does not accept the item, she will return it to the seller; in that case, the state will change to q8. If the buyer does not take any of the above actions, then after time T, the Safe will transfer the funds to the seller — q4 moves to q18.

q5 2  ; 0; 1; 1; 2; 1; 0 :

The seller receives the second key from the buyer. With B1, B2 and his private key, the seller can open the Safe and transfer the funds to his account.

q6 2<sub>ð</sub> <sub>Þ</sub> ; 1; 1; 1; 2; 1; 0 :

The funds are in the seller's account. In this state, the item-fund settlement process is completed successfully; therefore, the settlement fee will be credited back to the seller's account.

q7 2<sub>ð</sub> <sub>Þ</sub> ; 1; 1; 1; 2; 1; 1 :

The settlement fee is credited back to the seller. q7 is one of the possible <sup>fi</sup>nal states.

q8 1  ; 0; 1; 2; 2; 1; 0 :

If the buyer, at q4, feels the item is not compatible with the description of what was auctioned online, she will return the item to the seller. At q8, the seller receives the returned the item. Once he receives the item, and if the seller acknowledges that the item is indeed counterfeit or of inferior value, he will send S2 (the seller's second key) to the buyer; q8 then moves to q9. If no action is taken, then q8 moves to q19.

q9 1; 0; 1; 2; 2; 2; 0 :

The buyer receives S2 at q9. With S1, S2 and her own private key, the buyer can open the Safe and transfer the funds back to her account, and q9 moves to q10.

q10 1; 2; 1; 2; 2; 2; 0 :

The funds are transferred back to the buyer's account. q10 is one of the possible <sup>fi</sup>nal states, and no further action is necessary.

q11 1<sub>ð</sub> <sub>Þ</sub> ; 1; 2; 2; 1; 1; 1 :

At q11, the seller has both the funds and the item. If the seller is honest, he will mail the item to the buyer, q11 changes to <sup>fi</sup>nal state q12 and the transaction is complete. If not, the seller may choose to keep the funds and not mail out the item to the buyer. The transaction may stay at q11, and not move to a <sup>fi</sup>nal state. So q11 is a risky state for the buyer, since whether the buyer can receive the item or not is at the seller's discretion.

q12 2<sub>ð</sub> <sub>Þ</sub> ; 1; 2; 2; 1; 1; 1 :

The buyer receives the item and the seller has the funds. This is one of the possible <sup>fi</sup>nal states, and no further action is necessary.

q13 2  ; 2; 2; 2; 1; 1; 1 :

Similar to q11, if at q0, the seller does not follow the protocol and chooses to send the item directly to the buyer before the buyer's credit card is charged by the Safe, q0 changes to q13. In this state, the buyer has both the item and the funds in hand. If the buyer is honest, she will send the funds to the seller, and q13 moves to q12. Otherwise, the buyer may keep both the item and the funds. Q13 is a risky state for the seller, since whether the seller receives the funds or not is all at the buyer's discretion.

q14 1; 2; 2; 2; 1; 1; 2 :

For some reason, the seller sends the settlement fee to the buyer at q0. At q14, the buyer has received the settlement fee. If the buyer wants to continue the settlement process, she should send the settlement fee back to the seller, so q14 changes to q0 and the settlement process starts again.

q15 2  ; 0; 2; 2; 1; 1; 1 :

At q1, if the seller sends the item to the buyer, then q1 moves to q15. At q15, the buyer has the item, the funds for the purchase amount are in the Safe but the settlement fee is still at the seller's. In this state, the protocol may continue in one of two ways. The <sup>fi</sup>rst is that the buyer may return the item to the seller, so q15 is back to q1 and the protocol continues. Alternatively, the Safe transfers the settlement fee from the seller's account to the Safe; therefore, q15 moves to q16.

q16 2; 0; 2; 2; 1; 1; 0 :

At q16, the settlement fee has been transferred to the Safe. To continue the process, the seller should give S1 (the seller's <sup>fi</sup>rst key) to the buyer. If so, q16 changes to q3.

q17 1; 0; 2; 2; 1; 1; 2 :

In this state, the item is at the seller's, the funds are in the Safe and the settlement fee is with the buyer. This situation may happen when the seller mistakenly sends the settlement fee to the buyer at q1. The buyer returns the settlement fee to the seller; then q17 moves back to q1.

q18 2  ; 1; 1; 2; 2; 1; 0 :

At q4, if the buyer neither sends B2 to acknowledge the acceptance of the item, nor returns the item to the seller, then after time T, the Safe will transfer the funds to the seller. In this case, q4 moves to q18. So at q18, the funds have been transferred to the seller's account. Following q18, the Safe will transfer the settlement fee to the seller. At q20, the seller has the funds and the settlement fee.

q19 1  ; 2; 1; 2; 2; 1; 0 :

If the seller receives the returned item, and within time T does not send B2 to the buyer, then the Safe will return the funds to the buyer's account. The seller's settlement fee will remain in the Safe.

q20 2  ; 1; 1; 2; 2; 1; 1 :

Following q18, the Safe will transfer the settlement fee to the seller. At q20, the seller has the funds and the settlement fee. If both the seller and the buyer follow the Transparent Safe protocol step-by-step, the transaction should move from q0 to q1, q2, q3, q4, q5, q6… through to the <sup>fi</sup>nal state q7. By following this sequence, the seller as well as the buyer can avoid the “traps” at q11 and q13.

## 3.3. Transaction function in finite automata

The <sup>fi</sup>nite automata (FA) is a mathematical model of a system with discrete inputs and outputs. The system can be in any one of a <sup>fi</sup>nite number of internal states. The state of the system summarizes the information concerning past inputs that is needed to determine the behavior of the system on subsequent inputs. The control mechanism of an elevator is a good example of a <sup>fi</sup>nite state system. That mechanism does not remember all previous requests for service but only the current <sup>fl</sup>oor, the direction of the motion (up or down), and a collection of not yet satis<sup>fi</sup>ed requests for service.

Example of transaction function in deterministic <sup>fi</sup>nite automata:

δ(q5, x2)=q6, this indicates that, at q5, the buyer has opened the Safe with the proper keys and transferred the funds to her account, so the state moves from q5 to q6.

Transaction function δ in non-deterministic <sup>fi</sup>nite automata.

Consider a case in which we modify the <sup>fi</sup>nite automata model to allow more than one transaction on the same input symbol. This new model is called non-deterministic <sup>fi</sup>nite automata (NFA). From the above transaction diagram, observe that there are four edges out of state q0, one going to q1, the second one going to q11, the third going to q14 and the fourth to q13.

Examples for transaction functions in non-deterministic <sup>fi</sup>nite automata:

δ(q0, x2)=q1, this indicates that, at q0, the funds are transferred to the Safe, so the state moves from q0 to q1.

$\delta ( { \tt q } 0 , { \tt x } 2 ) = { \tt q } 1 1$ , this indicates that at q0, the buyer sends the funds to the seller, so the state moves from q0 to q11.

With seven input variables, each able to take any of three different values, there should be $3 ^ { 7 }$ possible states. The transaction function lists all these states. Notice that some of the states are marked by □. This is because these states are either technically impossible or there are no incentives for any of the parties to take such an action.

Input Σ

Input Σ is represented by seven variables, x1, x2, x3, x4, x5, x6, and x7 and empty input ɛ. The de<sup>fi</sup>nition of each variable is listed below.

x1…… The item.

x2…… The funds.

x3…… B1, The buyer's <sup>fi</sup>rst key.

x4…… B2, The buyer's second key.

x5…… S1, The seller's <sup>fi</sup>rst key.

x6…… S2, The seller's second key

$\yen 7\ldots$ The settlement fee.

$\varepsilon _ { \ast \ast \ast \ast }$ Empty input. Time T has passed with no action from both the buyer and the seller.

Each variable can have one of the three values: 0 for being in the Transparent Safe, 1 for being held by the seller, and 2 for being held by the buyer. For example, x1=1 means the seller has the item, x5=2 means the buyer has S1, the seller's <sup>fi</sup>rst key. With these variables, we can describe each state precisely (see Fig. 2).

## 3.4. Mathematical proof

Let VF be the amount of the funds. This value is usually determined by the auction.

Let Vreal be the market value of the real item.

Let Vfake be the market value of the fake item.

Let Vf be the settlement fee.

Assumption 1. To the seller, the value of the funds is greater or equal to the value of the item.

VFzVreal:

Assumption 2. The value of the real item is greater than the value of the fake item.

Vreal≥Vfake and the value of the fake item is a fraction of the value of the real item.

Vfake kVreal where 0<k 1:

3.4.1. The total benefit for an honest seller For an honest seller, the seller's bene<sup>fi</sup>t at q0 is Vreal+Vf. The honest seller's bene<sup>fi</sup>t at q7 is VF+Vf. So the total bene<sup>fi</sup>t that an honest seller gets is

```txt
B_honest seller = Vq7-Vq0 = (VF + Vf)-(Vreal + Vf) = VF-Vreal.
```

<table><tr><td>State</td><td colspan="7">Inputs</td><td></td></tr><tr><td></td><td>x1</td><td>x2</td><td>x3</td><td>x4</td><td>x5</td><td>x6</td><td>x7</td><td> $\varepsilon$ </td></tr><tr><td>{q0}</td><td>{q13}</td><td>{q1, q11}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td>{q14}</td><td> $\text{ⓧ}$ </td></tr><tr><td>{q1}</td><td>{q15}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td>{q2, q17}</td><td> $\text{ⓧ}$ </td></tr><tr><td>{q2}</td><td>{q3}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td>{q3}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td></tr><tr><td>{q3}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td>{q4}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td></tr><tr><td>{q4}</td><td>{q8}</td><td>{q18}</td><td> $\text{ⓧ}$ </td><td>{q5}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td>{q18}</td></tr><tr><td>{q5}</td><td> $\text{ⓧ}$ </td><td>{q6}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td></tr><tr><td>{q6}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td>{q7}</td><td> $\text{ⓧ}$ </td></tr><tr><td>{q7}</td><td>{q7}</td><td>{q7}</td><td>{q7}</td><td>{q7}</td><td>{q7}</td><td>{q7}</td><td>{q7}</td><td>{q7}</td></tr><tr><td>{q8}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td>{q9}</td><td> $\text{ⓧ}$ </td><td>{19}</td></tr><tr><td>{q9}</td><td> $\text{ⓧ}$ </td><td>{q10}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td></tr><tr><td>{q10}</td><td>{q10}</td><td>{q10}</td><td>{q10}</td><td>{q10}</td><td>{q10}</td><td>{q10}</td><td> $\text{ⓧ}$ </td><td>{q10}</td></tr><tr><td>{q11}</td><td>{q12}</td><td>{q11}</td><td>{q11}</td><td>{q11}</td><td>{q11}</td><td>{q11}</td><td>{q11}</td><td>{q11}</td></tr><tr><td>{q12}</td><td>{q12}</td><td>{q12}</td><td>{q12}</td><td>{q12}</td><td>{q12}</td><td>{q12}</td><td>{q12}</td><td>{q12}</td></tr><tr><td>{q13}</td><td>{q13}</td><td>{q12}</td><td>{q13}</td><td>{q13}</td><td>{q13}</td><td>{q13}</td><td>{q13}</td><td>{q13}</td></tr><tr><td>{q14}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td>{q0}</td><td> $\text{ⓧ}$ </td></tr><tr><td>{q15}</td><td>{q1}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td>{q16}</td><td> $\text{ⓧ}$ </td></tr><tr><td>{q16}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td>{q3}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td></tr><tr><td>{q17}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td>{q1}</td><td> $\text{ⓧ}$ </td></tr><tr><td>{q18}</td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td> $\text{ⓧ}$ </td><td>{q20}</td><td> $\text{ⓧ}$ </td></tr><tr><td>{q19}</td><td>{q19}</td><td>{q19}</td><td>{q19}</td><td>{q19}</td><td>{q19}</td><td>{q19}</td><td>{q19}</td><td>{q19}</td></tr><tr><td>{q20}</td><td>{q20}</td><td>{q20}</td><td>{q20}</td><td>{q20}</td><td>{q20}</td><td>{q20}</td><td>{q20}</td><td>{q20}</td></tr></table>

Fig. 2. Mapping transaction function for Transparent Safe transaction diagram.

## 3.4.2. The total benefit for a dishonest seller

However for a dishonest seller with a counterfeit item, there is a chance P that the seller mails the fake item to the buyer, and the buyer accepts it. The settlement process ends at state q7. There is also a (1−P) chance that the buyer returns the fake or defective item. The process ends at q10.

If at q0, the dishonest seller has the fake item and Vf. The seller's bene<sup>fi</sup>t is

$$
\mathrm {V\_fake item + Vf}.
$$

If, with a probability P, the settlement process ends at ${ \mathsf { q } } 7 , { \mathsf { q } } { \mathsf { q } } ,$ the dishonest seller's bene<sup>fi</sup>t is

$$
\mathrm{VF} + \mathrm{Vf}.
$$

If with the probability 1−P, the settlement process ends at q10, the seller's bene<sup>fi</sup>t is

VXfake item:

Therefore, a dishonest seller's bene<sup>fi</sup>t at the end of the settlement process is

$$
\text { B\_dishonest   seller } = P [ \text { Vq7 - Vq0 } ] + (1 - P) [ \text { Vq10 - Vq0 } ]
$$

$$
\begin{array}{r l} \text { B\_dishonest   seller } & = P [ (\mathrm{VF} + \mathrm{Vf}) - (\mathrm{Vfake} + \mathrm{Vf}) ] \\ & + (1 - P) [ \mathrm{Vfake} - (\mathrm{Vfake} + \mathrm{Vf}) ] \end{array}
$$

$$
= P [ \mathrm{VF-Vfake} ] + (1 - P) [ - \mathrm{Vf} ] h = P [ \mathrm{VF-Vfake} ] - (1 - P) \mathrm{Vf}.
$$

$$
\text {   If   } \mathrm{Vfake} = k \mathrm{Vreal} (\text {   assumption   2   })
$$

$$
\text { B\_dishonest   seller } = P [ \text { VF - kVreal } ] - (1 - P) \text { Vf }.
$$

From the above equations, we can see that if a dishonest seller succeeds in defrauding a buyer, then he makes a pro<sup>fi</sup>t of VF − kVreal. Since 0 < k < 1, VF − kVreal NVF − Vreal. That is, if the dishonest seller succeeds in making a fraudulent transaction, he will make more than an honest seller.

$$
\mathrm{VF} - \mathrm{kVreal} - \mathrm{VF} + \mathrm{Vreal} = (1 - k) \mathrm{Vreal}.
$$

From this equation we also can see that the dishonest seller can only make this extra pro<sup>fi</sup>t (1−k) Vreal with a probability of P. There is a (1−P) chance that his pro<sup>fi</sup>t may be eroded away by VF.

To prevent the dishonest seller from committing fraud, Vf has to be suf<sup>fi</sup>ciently large. What factors should be considered in determining Vf? How should the value of Vf be related to VF? These questions will be addressed in the following section.

## 3.4.3. Determining the value of Vf

We need to choose Vf in such a way that the dishonest seller will not bene<sup>fi</sup>t by cheating a buyer. That is

BXhonest seller z BXdishonest seller

$$
\mathrm{VF-Vreal} \geq P [ \mathrm{VF-Vfake} ] - (1 - P) \mathrm{Vf}
$$

$$
(1 - P) \mathrm{Vf} \geq (P - 1) \mathrm{VF} - P k \text { Vreal } + \text { Vreal }
$$

$$
\mathrm{Vf} \geq [ (P - 1) \mathrm{VF} + (1 - P k) \text { Vreal } ] / (1 - P)
$$

$$
\mathrm{Vf} \geq [ - (1 - P) V F + (1 - P k) \text { Vreal } ] / (1 - P)
$$

$$
\mathrm{Vf} \geq (1 - P k) / (1 - P) \text { Vreal   -   VF }.
$$

$$
\text {   If   } \mathrm{Vreal} = \mathrm{VF}
$$

$$
\mathrm{Vf} \geq (1 - P k) / (1 - P) \mathrm{VF-VF}
$$

$$
\mathrm{Vf} \geq P (1 - k) / (1 - P) \mathrm{VF}.
$$

From this result, we can see that the settlement fee should be adjusted according to three factors: probability P, k and the <sup>fi</sup>nal auction price of the item. VF is known when the auction ends. P and k may vary for each auction category. Some empirical studies may be needed to construct P and k, so the Transparent Safe will be more effective.

## 4. Contributions and implications

The Transparent Safe item-fund exchange mechanism is simple and easy to comprehend. We predict it will make a profound contribution to the <sup>fi</sup>eld of e-commerce. It is the <sup>fi</sup>rst online exchange mechanism that involves transferring physical items between two individuals. All existing fund transfer mechanisms on the market work with only digitized information, such as account numbers, sale-price amounts, and credit card numbers. In addition, the Transparent Safe item-fund exchange mechanism is designed to ensure that dishonest sellers will not bene<sup>fi</sup>t from fraudulent schemes. This feature is especially important in e-commerce when the necessary trust is insuf<sup>fi</sup>cient between the two parties and when there is a lack of effective government regulation or legal enforcement in place.

There are a number of implications that the Transparent Safe may bring to e-commerce. First, with the Transparent Safe, the item-fund transfer becomes reliable and dependable. If it is implemented in online auctions, the average sales price might rise signi<sup>fi</sup>cantly. Second, the Transparent Safe can be used as a stand-alone online entity; it can help any two parties requiring a fund-item settlement process, which may or may not be associated with online auctions.

Research into the Transparent Safe is just beginning. The following is a list of possible areas of future inquiry on this subject:

1. Security of the Transparent Safe itself has paramount importance. How to protect it from attacks from many different sources is an essential issue. Attacks may come from hackers or from legitimate users who try to tamper with the Safe.

2. Empirical studies are needed to better determine the value of P and k. In online auctions, some categories may have higher rates of settlement problems than others. It would be best if appropriate values for P and k could be identi<sup>fi</sup>ed for different categories. For example, in the category of automobiles, it would be hard to produce a fake item, so the k value could be comparatively small. It is relatively easy to spot any defects or inconsistency with the description, as the chance of succeeding in fraud is small; therefore, the P value should be small as well.

3. Educating the users of the Transparent Safe is another major future area of endeavor. It would make the Transparent Safe more effective if the sellers and the buyers were well informed about different settlement actions and their consequences, and about the strength of the Transparent Safe.

4. How to motivate sellers to use the Transparent Safe is another challenging issue. There are three cases in which the seller should be motivated:

Case 1. After the auction has ended, it is usually the buyer who pays the seller <sup>fi</sup>rst through online payment services such as PayPal or PayPoint [22]. Once the money is received, the seller mails the item to the buyer. The buyer is at risk of not receiving any item at all or receiving a fake item. If the buyer chooses to use the Transparent Safe, such risk is greatly reduced. The incentive for the buyer to use the Transparent Safe is obvious. In such a situation, once the buyer starts to use the Safe, then the seller has to go along in order to make the sale.

Case 2. In some cases, the seller might send the item to the buyer <sup>fi</sup>rst; then the seller is the one who risks not receiving payment. If the seller is honest, he can rest assured that, using the Safe, the settlement process will be completed and that the settlement fee will be returned to him at the end. Therefore, the honest seller will be motivated to use the Safe.

Case 3. Now, the interesting question is whether the dishonest seller will sign on to using the Safe. The dishonest seller understands that he has 1 − p chance that the buyer will <sup>fi</sup>nd out the item is fake and the settlement fee may be lost. It is likely that he will try to persuade the buyer to send the money through a regular online payment channel rather than use the Transparent Safe. The dishonest seller will be unlikely to send the item <sup>fi</sup>rst, as mentioned in the second case, because he is afraid that the buyer will <sup>fi</sup>nd out that the item is fake and return it or refuse payment. If the dishonest seller asks the buyer to send money <sup>fi</sup>rst, this case turns into Case 1. Where the buyer is well informed about the risk, the buyer will choose to use the Safe, and the dishonest seller has two options: he either follows through on the protocol or quits the settlement process by refusing to sell.

The Transparent Safe is a new way of building more secure settlement processes for online item-fund exchange. By making online auctions and other e-commerce acceptable for a larger number of customers, the market will attract more sellers and higher-value goods for sale. We hope that in the future more people from diverse disciplines get involved and together we can build e-commerce into a signi<sup>fi</sup>cant part of our economy.

## Appendix A

Transaction diagram.

![](/api/attachments/CBJHGETB/fulltext/images/acd6127462e068a47bea6b52544e85f1c489adb624d7e6fc2bd058cf24a6f6ea.jpg)

## References

[1] S. Antony, Z. Lin, B. Xu, Determinants of escrow services adoption in consumer-to-consumer online auction market: an experiment study Decision Support Systems 42 (3) (2006).

[2] S. Ba, A. Whinston, H. Zhang, Building trust in online auction markets through an economic incentive mechanism, decision Support Systems 35 (3) (2003).

[3] Bureau of Transportation Statistics, US Department of Transportation, Transportation Statistics Annual Report, 2000.

[4] J. Cassell, T. Bickmore, External manifestations of trustworthiness in the interface, Communications of the ACM 43 (12) (2000)

[5] P. Chatterjee, D.L. Hoffman, T.P. Novak, Modeling the clickstream: implications for web-based advertising efforts, Marketing Science 22 (4) (2003) 520–541.

[6] S. Dewan, V. Hsu, Trust in Electronic Market: Price Discovery in Generalist Versus Specialty Online Auctions, Working paper, University of Washington, 2001.

[7] B. Friedman, P.H. Kahn, D.C. Howe, Trust online, Communications of the ACM 43 (12) (2000).

[8] A.G. Gonzalez, Paypal and eBay: the Legal Implications of the C2C Electronic Commerce Model 18th BILETA Conference 2003.

[9] J. Hopcroft, J. Ullman, Introduction to Automata Theory, Language and Computation, Addison-Wesley, Boston, 1979.

[10] C. Jensen, S. Farnham, S. Drucker, P. Kollock, The effect of communication modality on cooperation in online environment. Proceeding of CHI'00 ACM Press, New York, 2000, pp. 470–477.

[11] A. Josang, R. Ismail, C. Boyd, A survey of trust and reputation systems for online services provision, Decision Support Systems 43 (2) (2007).

[12] S. Junnarkar, I-Escrow set to acquire rival Trade-Direct, July 15 1999 CNET News.com.

[13] D. Lucking-Reiley, Auctions on the Internet: what's being auctioned, and how? Journal of Industrial Economics 48 (3) (2000) 227–252.

[14] J. Olson, G. Olson, i2i Trust in e-commerce, Communications of the ACM 43 (12) (2000).

[15] P. Resnick, R. Zeckhauser, E. Fridman, K. Kuwabara, Reputation systems, Communications of the ACM 43 (12) (2000).

[16] E. Rocco, Trust breaks down in electronic contexts but can be repaired by some initial face-to-face contact, Proceeding of CHI'98, ACM Press, New York, 1998, pp. 496–502.

[17] B. Schneier, Applied Cryptograph, John Wiley & Sons, New York, 1994.

[18] D. Schoder, P.L. Yin, Building <sup>fi</sup>rm trust online, Communications of the ACM 43 (12) (2000).

[19] B. Shneiderman, Designing trust into online experiences, Communications of the ACM 43 (12) (2000)

[20] B. Stone, Busting the Web Bandits, Newsweek, July 16, (2001).

[21]. S. Thomas SSLand TLS Essentials: Securing the Web John Wiley & Sons 2000

[22] Tradenable.com Home page, http://www.tradenable.com, (2001).

[23] Verisign.com http://www.verisign.com.

[24] J. Zhang, The roles of players and reputation: evidence from eBay online auctions, Decision Support Systems 42 (3) (2006).

[25] H. Zhang, H. Li, Factors affecting payment choices in online auctions: a study of eBay traders, Decision Support Systems 42 (2) (2006).

Ying Sai is an Assistant Professor at Loyola Marymount University. She holds a Bachelor of Science degree from Beijing Institute of Light Industry; a Master of Science degree from Carnegie-Mellon University; a Ph.D from the University of Texas at Austin. Her research interests are online auction, electronic commerce and information technology security.
