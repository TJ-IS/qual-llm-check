---
otero_id: 21101
otero_key: "ZV2FKZMJ"
title: "Building trust in online auction markets through an economic incentive mechanism"
authors: "Sulin Ba; Andrew B. Whinston; Han Zhang"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00074-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Building trust in online auction markets through an economic incentive mechanism

Sulin Ba <sup>a</sup>, Andrew B. Whinston <sup>b</sup>, Han Zhang <sup>c</sup>

<sup>a</sup>Department of Information and Operations Management, Marshall School of Business, University of Southern California Los Angeles, CA 90089, USA

<sup>b</sup>Department of Management Science and Information Systems, Red McCombs School of Business, The University of Texas at Austin, Austin, TX 78712, USA

<sup>c</sup>The DuPree College of Management, Georgia Institute of Technology, Atlanta, GA 30332, USA

Accepted 31 March 2002

## Abstract

Millions of dollars change hands daily through online auction markets. However, fraud has been on the rise in these markets. Using a game theoretic approach, we propose a design of an economic incentive mechanism, the trusted third party (TTP), to serve the online auction communities. The proposed model addresses both the economic and technological aspects of online auction transactions by assigning a digital certificate to each participant. Thus, each participant’s identity as well as his or her reputation can be established by other market participants. The analytical results demonstrate that when online transactions take place with the assistance of digital certificates issued by a TTP, the most utilitarian course of action for a market participant is to behave honestly. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Electronic commerce; Electronic markets; Online auction; Trusted third party; Certification authority; Digital certificate; Trust; Game theory

## 1. Introduction

As a type of electronic market, online auctions are transforming the collectibles business to a potential billion-dollar worldwide market [9]. Feeding on people’s enchantment with the idea of a friction-free economy, online auctions are considered quick and efficient platforms to erase geographical boundaries, and for establishing accurate prices based purely on supply and demand. The use of online auction sites ranges from individuals conducting online ‘‘garage sales’’ to companies liquidating unwanted inventory. However, fraud in this market is on the rise. According to the Internet Fraud Watch operated by the National Consumers League, online auction sales remained the number one source of Internet fraud for the first 10 months of 2001. About 63% of the frauds reported to the Internet fraud watch are online auction frauds. The average loss per person rose from \$310 in 1999 to \$427 in 2000, and to \$478 in the first 10 months of 2001 [14].

The situation raises an increasingly important question: how to enforce honesty to ensure the quality of online product offerings? The answer to the question is critical not only for online auctions, but for the whole electronic markets as well. If neglected, the problem threatens the continued growth of electronic commerce. How to design mechanisms to promote trust in online auction markets when individuals have short run temptations to cheat? What are the conditions under which such a mechanism would work? These are the questions we attempt to answer in this paper.

Trust has been recognized as a very important factor to facilitate online transactions [5,7,13,15,18,20,25]. However, current literature tends to focus on the social or economic functions of trust. For example, Kollock [18] explores the emergence of endogenous solutions to the problems of risky trade and discusses the production of trust in online markets. Lee and Yoo [20] focus on the problem of quality discovery in electronic trading of physical goods. They argue that a third party mechanism can solve the problem of lemons in electronic auction markets, especially for goods that are hard to describe. However, in the prior research, the issue of how to design the third party mechanism or how the mechanism might work is not adequately explored.

Recognizing the lack of sufficient and effective services for trust building in online markets, we present in this paper the design of a trusted third party (TTP). The purpose of the TTP is to facilitate trust building in the online environment, and to help reduce online fraud through the use of reputation. The mechanism combines the economic and technological aspects of online transactions. It takes an economic incentive approach to illustrate how reputation can be used as an effective deterrent of cheating behaviors when future transactions are desirable. In our approach, trust refers to calculus-based trust. That is, it is an ongoing, market-oriented, economic calculation whose value is derived by determining the outcomes resulting from creating and sustaining the relationship relative to the costs of severing it [21]. Therefore, compliance with calculus-based trust is often ensured both by the rewards of being trusting (and trustworthy) and by the ‘‘threat’’ of trust being violated. Since the online auction market magnifies the various risk factors involved in electronic transactions, as elaborated in Section 2, we use online consumer-to-consumer auction markets as the context to illustrate how the mechanism can be used. Although, the mechanism is applicable in other types of online markets as well.

The rest of the paper is organized as follows. Section 2 highlights the asymmetric information problem in online transactions and the limitations of the currently available systems aimed to solve the problem. Section 3 points out that in the absence of enforceable legal systems, extralegal mechanisms can be effective to enforce norms and rules. This provides a strong argument for our design of trusted third parties. Section 4 uses game theory to analyze online transactions and to explain why a new economic incentive mechanism is needed. Section 5 details the design of a trusted third party and provides a theoretical justification to the design. Section 6 discusses the practical implications of our proposed model and concludes the paper.

## 2. Online auction markets: problems and current solutions

Information asymmetry, a situation where two parties do not possess the same information [1], has been recognized as one of the major problems in electronic markets [7]. Among the many aspects of asymmetric information, two are closely related to online fraud: one being the anonymous identities of online trading parties, the other being the uncertain quality of the product. As manifested by the famous New Yorker cartoon that ‘‘on the Internet, no one knows you are a dog,’’ online trading parties can easily remain anonymous or change their identities. In online auction markets where numerous individuals participate in transactions, it is even harder to bind one identity to one participant. Most of the auction sites identify sellers or bidders by email addresses, which can be easily obtained without monetary cost from multiple sources. Recognizing the difficulty of verifying user identity, eBay excuses itself from the responsibility in its User Agreement: ‘‘Because user authentication on the Internet is difficult, eBay cannot and does not confirm each user’s purported identity.’’<sup>1</sup> This introduces opportunities for auction participants to misbehave without paying reputation consequences.

The lack of interpersonal interactions in online markets is another source of fraud. In a traditional face-to-face business environment, eye contact, a handshake, and chatting help develop basic trust between vendors and customers. Customers get to know the quality of products by looking, touching, and feeling. However, such interpersonal contact does not exist in electronic markets. Asymmetric information in this context means that the transacting parties do not have the same information about the product. When bidders view a product listed at an auction site, the true quality of the product is unknown. Auction site operators often claim that they ‘‘have no control over the quality, safety or legality of the items advertised, the truth or accuracy of the listings,’’<sup>1</sup> thus exposing auction bidders to more fraudulent listings and transactions.

Recognizing the possibility of fraud caused by asymmetric information, online auction sites have begun to offer various services that are aimed to encourage trustworthiness and reduce fraudulent transactions in the online auction market.

Feedback Systems: Auction participants can use feedback systems to publicly rate their satisfaction towards their trading partners. Specifically, the feedback system is a measure of a user’s reputation in an auction community. The auctioneers encourage all users to check their trading partners’ rating before transactions and leave feedback about their trading partners after their transactions. In essence, the system tries to use one’s reputation as a deterrent for cheating behaviors. That is, if one develops a bad reputation, other auction participants may not transact with the person anymore.<sup>2</sup>

Insurance or Guarantee: Auctioneers offer free or low-cost insurance to protect buyers if they are proven to be victims of fraud. An item is covered by the insurance when the buyer sends money to the seller but does not receive the item, or the item received is significantly different from the item described in the auction.<sup>3</sup>

Escrow Services: An escrow service such as escrow.com (http://www.escrow.com) acts as a trusted third party in a transaction, providing safe methods to transfer items and payments to both parties. First, the escrow collects payment for the merchandise from the buyer. When the payment clears, the seller is notified to ship the item. Second, the buyer notifies the escrow when the merchandise is received and is satisfactory. Finally, the escrow will then release the payment to the seller.

The above-mentioned services have, to some extent, promoted trust in the online auction business. Reputation systems can serve both as a source of information and as a potential source of sanctions [27]. The existence of reputation information is an incentive for the participants in a transaction to be trustworthy because acquiring a bad reputation can have damaging effects [18]. Yet, the current reputation systems have several limitations. First, the rationale behind the feedback systems is that the reputation of an auction participant is representative of one’s past trading behavior. A bad reputation (i.e., low feedback rating) will discourage others from conducting future transactions with the participant. However, the ratings (thus the reputation) are based on online identities that are often not more than an email address. Currently auction sites do not provide strong authentication. Consequently, a person with a bad rating can easily acquire a new email address and re-register with no trace of the earlier bad reputation. That is, the past history of a cheater remains private information (one aspect of asymmetric information) and does not serve as an effective deterrent of future transactions. Moreover, a person who has developed a very bad feedback rating at one site can go to another auction site as a new user and cheat again. Both situations arise from the lack of strong authentication of online identities.

In addition, the feedback system allows anyone to leave feedback on a transaction. Therefore, the ‘‘reputation’’ developed through the feedback system may not be accurate and truthful. There is the possibility that people may abuse their privileges of posting (good or bad) feedback about others; and comments as well as ratings can be manipulated easily. Although the reputation information on an auction participant gets disseminated through the feedback system, the information is not verified, and may be deceiving.

The insurance program also has many limitations. Not all the items in online auctions will be covered by insurance or guarantee. For example, at eBay the seller must have a non-negative feedback rating, otherwise the item will not be covered by insurance; at Amazon.com, the item must bear the Amazon.com A-to-z guarantee logo. Moreover, the insurance and guarantee program can only offer a limited insurance. For example, the purchases will be covered by insurance only for up to \$200 (less a \$25 deductible) at eBay and \$250 at Amazon.com.

Escrow services are useful for large sales, ensuring a safe and pleasant transaction, but they are not convenient for low value transactions. In addition, it will take a long time to finish one business transaction.

In short, due to the presence of asymmetric information and the limitations of the current solutions, it is very difficult for buyers in electronic markets to have full knowledge of the product quality prior to purchase. Conventional means to convey product quality, such as brand name and reputation, are less useful in the current setting of electronic markets, particularly online auction markets. This is because of easily changeable identities and the lack of an information dissemination mechanism that reflects the true transacting history of the market participants. Therefore, buyers inevitably face many difficulties in selecting reliable sellers and quality products, which in turn produces the lemon problem [1], where bad products drive out good products due to asymmetric information such as product quality uncertainty. The lemon problem could potentially lead to a market failure. Thus, there is the need for institutional setups that can encourage trustworthiness among trading partners, minimize misrepresentation of product offerings, and encourage consumer confidence in online auction markets.

## 3. Effectiveness of extralegal mechanisms

When transaction disputes happen, one traditional approach is to involve the legal system. However, the legal mechanisms are not complete in electronic markets. First, legal regulation and control cannot keep pace with the development of electronic commerce; therefore, adequate laws for electronic commerce are lacking. For instance, sellers and bidders may reside halfway around the world, but the universal electronic markets do not have any legal principles generally accepted by the world. Second, the extant laws in conventional commerce might not be strictly enforceable in electronic commerce. Electronic markets are difficult to police when tens of thousands of new on-line businesses pop up every week. People may adopt fly-by-night strategies, for example, which makes laws unenforceable unless the vanished party stands for a real-world party and the connection between them can be traced. Third, resorting to legal enforcement in electronic commerce might be impracticably expensive or even impossible for micro-payment transactions. There are many low-value transactions that might be worthy of only several dollars, which individually may not make economic sense for the transacting parties to settle in court.

Fortunately, literature in the law community (e.g., Refs. [4,10]) and the economics community (e.g., Refs. [3,17,24]) has argued that instead of solely relying on the government as the chief source of rules and enforcement efforts, extralegal mechanisms can also help people interact to their mutual advantage. Extralegal mechanisms usually refer to systems governed by informal social norms [6,16]. These social norms identify the everyday behaviors that call for the informal administration of rewards and punishments. Macaulay [22] points out that ‘‘social pressure’’ and ‘‘reputation’’ are perhaps more widely used than formal contracts and filing suits. People behave honestly in many cases because honesty is rewarded and/ or defection is punished in future transactions or other social activities.

Extralegal mechanisms based on social norms come in many varieties. Gossip of neighbors, reproach of friends, and the evaluation of the community enforces the common rules of everyday conduct. In complicated business settings, companies may comply with intricate financial arrangements mainly to preserve their market reputation, rather than from fear of lawsuit. Literature has shown that extralegal mechanisms work effectively at regulating economic relations among communities that adopt them. Ellickson [10] finds that the residents of rural Shasta County (California) apply informal norms, rather than formal legal rules, to resolve most of the issues that arise among them. Coleman [8] cites the community of the City of London merchant bankers as one in which a verbal agreement is sufficient. Bernstein [4] describes the standard transactional model in the New York diamond industry as one in which a handshake creates a binding agreement. Johnston’s [16] empirical study further demonstrates that extralegal sanctions can deter a breach when the transaction parties have a history of prior dealings that have established a basis of trust and/or a significant prospective future advantage to each in the continuation of the relationship.

The aforementioned cases demonstrate that in a certain business relationship, the trading partner’s reputation can serve as a ‘‘hostage.’’ If one party deviates from the norm and violates the other’s trust, the victim can quickly spread his trading partner’s bad reputation through out the business community. Then others will be cautious about doing business with the disreputable trader. Currently, due to the incompleteness of the legal mechanisms in electronic commerce, there is a need to find an alternative way to patrol dishonest behaviors. The effectiveness of extralegal mechanisms in the conventional market may be translated to electronic markets, and can be used to promote trust and minimize cheating behaviors.

In fact, eBay’s feedback system is a preliminary form of an extralegal mechanism designed to prevent fraud. Its effectiveness is limited because of the reasons we mentioned already: that reputation bound to an online identity can be easily changed, and that the reputation information is subject to manipulation because of the lack of a formal information dissemination mechanism. The reputation system is only effective to the extent that accurate information is collected and disseminated. In this paper, we propose the design of an extralegal mechanism that still uses reputation but addresses the problems by strong authentication. Such a system is an economic incentive system in the sense that when a reputation is bound to an identity that cannot be changed easily, then the reputation will have a stronger impact on the long-term payoff of a market participant. Therefore, the participants will have an incentive to maintain a good reputation.

## 4. Transactions in online auction markets

As of today, almost all online business transactions leave open the possibility of cheating. The temptation of cheating is that cheating normally results in an immediate short-term return. Each and every business transaction, therefore, becomes a decision problem, namely, what is my goal of this transaction? What is my expected return? What role should I play in the interaction? In this section, we use game theory to analyze online auctions where the individual outcomes for the participants involved depend on the strategies chosen by each of the auction participants. It is worth noting that although we place the transaction analysis in the online auction setting, the principles apply to other online transactions as well.

Research on game theory, especially repeated games, demonstrates how people manage to interact to their mutual advantage without the help of the legal enforcement [2,10,16]. The theory of repeated games provides a perspective to understanding the role of extralegal mechanisms in online auction markets. Many business interactions are repeated, such that the threat of future retaliation by the cheated partner or the whole community may enforce cooperative behaviors. In our analysis, each non-repeated transaction (the stage game) is assumed to be the Prisoners’ Dilemma (PD) game described by Table 1. By using the PD model, we demonstrate why reputation information just between two transacting parties and reputation information that is restricted to one single trading community are not sufficient; and why TTPs are needed to disseminate reputation information for the global online auction markets.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Buyer</td></tr><tr><td>Honest</td><td>Cheat</td></tr><tr><td rowspan="2">Seller</td><td>Honest</td><td> $\pi_t, \pi_t$ </td><td> $-l\pi_t,(1+g)\pi_t$ </td></tr><tr><td>Cheat</td><td> $(1+g)\pi_t,-l\pi_t$ </td><td>0,0</td></tr></table>

Suppose that a seller and a bidder are engaged in a single exchange involving a product (Scenario 1). Each of them can choose to play one of two strategies: Honest or Cheat. Table 1 presents the payoff structure of the PD game. The first number in each entry indicates the row player (seller)’s payoff and the second is the column player (buyer)’s payoff. In period t, if both the bidder and the seller are honest, they each have a payoff of $\pi _ { t }$

In period $t ,$ if both the bidder and the seller cheat, each has a payoff of $0 . ^ { 4 }$ If one player decides to cheat while the other is honest, then the cheater has his highest payoff of $( 1 + g ) \pi _ { t } ,$ while the honest one gets his lowest of $- l \pi _ { t } ,$ where l and $g$ are positive constant coefficients. We also assume $g \pi _ { t } - l \pi _ { t } < \pi _ { t } ,$ that is, $g - l < 1$ . This gives both sides an incentive to cheat, even though honest behavior maximizes the total payoff of the two players: $( 1 + g ) \pi _ { t } - l \pi _ { t } < \pi _ { t } + \pi _ { t }$ according to the assumption $g - l < 1$ . In other words, exploitation or being exploited does not produce as good an outcome as mutual cooperation.

Obviously, if this transaction is conducted only once, it is to each player’s separate advantage to play Cheat, since that play yields a higher payoff regardless of what the other player does. Accordingly, the only Nash equilibrium of the game is for both players to play Cheat. It is, however, worth noting that both agents are worse off than if they could somehow agree to play Honest. This is because the payoff of both playing honest is $\pi _ { t }$ while the payoff is only 0 if both plays cheat. The PD game demonstrates the idea that cheating might be profitable in a single business transaction. In the online auction market, for example, some sellers might find that a fly-by-night strategy of quality reduction is profit maximizing.

In reality, transactions are sometimes repeated between a buyer and seller (Scenario 2). In a continuous trading relationship, both the buyer and the seller can conduct their business transactions based on past interactions. In other words, they can use the history of past interactions as the basis to reward past honest behavior, and to punish cheating because information on their trading history is complete and known to both agents. This kind of informal enforcement mechanism is personal enforcement, in which cheating triggers retaliation by the victim. This mechanism works best in frequent and long-term relationships [2,17] between two participants where each participant knows exactly whom the other is, and there is no possibility of hiding identities.

People may also interact with multiple agents and change transaction partners often in an online auction community where a group of people, large or small, can interact with each other, trade with each other, or share information among community members (Scenario 3). For example, when people sell or buy on eBay, repeat transactions between the same seller and buyer are less likely, albeit not impossible. Most often, trading partners change frequently. In this situation, personal enforcement becomes ineffective. There is, however, another form of enforcement mechanisms, community enforcement. That is, agents change their partners over time, but they may be able to cooperate or coordinate their actions because dishonest behavior against one partner causes sanctions by other members in the community [17,24]. eBay’s ‘‘Feedback Forum’’ bears the idea of community enforcement in that consumers can use the forum to rate their satisfaction towards trading partners. Other users are encouraged to check their trading partners’ ratings before transactions, and leave feedback about their trading partners after their transactions, so the entire eBay community can become informed.

The effectiveness of both personal and community enforcement depends upon the assumption that the agents or the members of the community involved are well informed of who has cheated and whom to punish. Most of the time, this assumption cannot be satisfied in the global online auction markets because agents are changing trading partners frequently and may never have to face the same partner again (Scenario 4). In addition, community enforcement loses its power when people participate in multiple online auction communities, and there is no formal information dissemination mechanism to broadcast the reputation information. The possibility of changing one’s identity further renders the reputation system useless. Therefore, cheating is the only Nash equilibrium outcome in such a situation [17,24]. Obviously, unless we have other effective mechanisms to help information dissemination, or to enforce honest behavior, honesty among self-interested agents in the global online auction market would be very hard to maintain. Each individual transaction thus becomes a PD game where it is never to the agent’s advantage to be honest. Therefore, we argue that we need extralegal mechanisms to help enforce honest behavior and to protect agents’ interest.

## 5. Trusted third parties for trust building

Certification authorities (CAs) such as VeriSign and GTE CyberTrust have emerged to serve as one form of trusted third party (TTP). They authenticate the identity of each trading party in a transaction by issuing digital certificates based on public key cryptography and digital signatures.<sup>5</sup> A certificate is a digitally signed statement by a CA that binds the identity of an individ ual or organization to a public key. More specifically, a certificate contains, among other information, the certificate holder’s name, the certificate holder’s public key, and other personal information that can uniquely identify the certificate holder. By digitally signing a certificate, a CA binds the identity of the certificate holder to the public key contained in the certificate, and thus vouches for the identity of the public key holder. As an important element of the extralegal mechanisms, CAs play an important role in electronic commerce in terms of authenticating players and attesting to certain facts about the players. In addition, strong authentication from CAs makes it much more difficult for an online auction participant to change his identity.<sup>6</sup>

What is missing from the services provided by certification authorities, is the certificate holder’s reputation—is the certificate holder a reputable trader? Has the holder ever cheated before? No information is conveyed to the recipient regarding the certificate holder’s past trading behavior. In short, even though certification authorities address trader authentication concerns for electronic transactions, the product quality uncertainty problem remains unsolved because the link between an online identity and the past trading history (i.e., the reputation) of that identity is missing.

Given the incompleteness of the current structure of CAs, we propose a new design of a TTP and a theoretical justification of why such a design is effective in promoting trust and minimizing cheating in online auction markets. By building an information repository on trust, the TTP serves as both an information keeper and an information disseminator, through the issuance of digital certificates. The certificate will only be issued after a strong authentication process. That is, the TTP verifies the information provided by the certificate applicant and traces the history of the applicant to make sure that they cannot change their online identity, or if they have changed their identity the certificate will state such information. The certificate will thus bind an online auction participant to a fixed identity—the real-world person.

The new design is built on the current model of CAs but has enriched functionality. That is, the digital certificate issued by a TTP serves not only as an authentication of the certificate holder, but also as a reputation indicator. Anyone who holds a valid digital certificate should be regarded as a reputable agent who either has never been reported as a cheater, or has paid all the fines adjudicated by the TTP. The TTP is not a legal institution that could enforce rules. Therefore, paying fines adjudicated by the TTP is voluntary. However, if an online seller sells counterfeit products or products that are of a less quality than have been represented, unless the seller paid off all the fines awarded to the cheated parties by the TTP, the seller’s digital certificate will be revoked by the issuing TTP. This will be an indication to any prospective buyers that this seller doesn’t behave honestly. On the other hand, if a buyer fails to submit payment upon receipt of product, the TTP can revoke the buyer’s certificate as well if the fines are not paid. Here, we assume the TTP is fair and honest and it does not make mistakes.

In this design, we assume that agents are only concerned about their own interests. The new TTP would stimulate the formation of new types of social/ business norms in online auction markets. However, we do not assume that people follow a social/business norm for its own sake. In this paper, we will investigate how such a rule is sustained by self-interested agents in online markets. In other words, we will investigate the sequential equilibrium of the game played by buyers and sellers in online consumer-toconsumer auction markets.

Now we formalize the online transaction process to illustrate the trusted third party’s role. The events will be structured with the following sequence of play, which we call the Trusted Third Party system stage game. For simplicity of writing, in the following we always assume the current time period t = 0.

(1) Before any agent (buyer and/or seller) is engaged in online consumer-to-consumer auction transactions, he may apply to a TTP for a digital certificate by paying a one-time initiation fee: F. There may be multiple TTPs in online auction markets. We assume these TTPs are connected and will cooperate with each other, acting like one centralized TTP.<sup>7</sup>

(2) When two agents meet in an online auction market to do business transactions, they may ask each other to provide their digital certificate issued by the TTP. At no cost, agents may verify the validity of their trading agent’s digital certificate through the TTP.<sup>8</sup> The successful verification of a digital certificate means that the certificate holder has not been reported as cheating in the past, or he has paid all the fines. We assume that whatever happens at this step is common knowledge among the two trading agents and the TTP.

(3) The two trading agents interact by playing the Prisoners’ Dilemma game and get the payoffs according to Table 1. We assume that $\pi _ { t } ^ { \cdot } \mathbf { s }$ are independently identically distributed random variables with the common distribution of p’s. Furthermore, we define $\pi _ { \mathrm { M a x } }$ as the value beyond which p has no positive probability density of being at. Let $\theta = \pi _ { \mathrm { M a x } } / E [ \pi ] .$ , where E[p] is the expectation of p. We assume h is finite.

(4) At the current stage, either one of the two agents may make an appeal to the TTP at personal cost $C \pi > 0 ,$ , where C is a positive constant coefficient. This may only occur if the agent has verified his partner’s digital certificate with the TTP, and is aware that his partner’s certificate is valid.

(5) If either one makes an appeal to the TTP, then the TTP investigates the case and makes a judgment. The plaintiff gets compensation Jp if he has played Honest and his trading partner has played Cheat ( J is a positive constant coefficient); otherwise, no judgment is made by the TTP.

(6) If a judgment is decided and the plaintiff gets Jp, the defendant may pay the fine decided by the judgment, at personal cost $f ( J ) \pi ,$ or he may refuse to pay the fine, at personal cost 0. The function $f \colon \mathfrak { R } ^ { + } { \longrightarrow } \mathfrak { R } ^ { + }$ denotes the cost for a defendant to pay a given judgment. We assume that f is increasing and continuous. Therefore, the cost to the defendant is positively related to the amount of the judgment. Moreover, we assume f (x) <sub>z</sub> x, that is, what the cheater ends up paying is more than what the TTP awards to the plaintiff. Some of the difference goes to the TTP to cover the investigation cost.

(7) The TTP revokes the cheating agent’s digital certificate if he does not pay the fine. All the information about the unpaid judgments is stored in the TTP’s database.

In the following, we describe the desired behavior of the agents, the TTP System Strategy (TTPSS), which is a complete contingent plan describing the desired actions for each agent in each conceivable evolution of the game under the TTP system.

(1) At the first step of the stage game, the agent will buy a digital certificate from the TTP before he conducts any business transactions in online auction markets.

(2) At the second step of the stage game, if the agent himself has a valid digital certificate, he will verify his trading partner’s digital certificate with the TTP. Otherwise, he will not.

(3) At the third step, as long as one of the following four possibilities is satisfied, then the agent will play

Cheat.<sup>9</sup> Otherwise, he will play Honest. The four possibilities are: (a) the trading partner does not have a valid digital certificate, (b) the trading partner does not verify the agent’s digital certificate, (c) the agent himself does not have a valid digital certificate, or (d) the agent does not verify the trading partner’s digital certificate.

(4) At the fourth step, if the trading partner has been verified to have a valid digital certificate, has checked the agent’s certificate at Step 2, and has cheated at Step 3, then the current agent will make an appeal to the TTP. Otherwise, the current agent will not.

(5) At the fifth step, if the agent has been a cheater, he will pay the fine $f ( J ) \pi$ after the TTP makes a judgment.

Based on the Optimality Principle of Dynamic Programming,<sup>10</sup> we use backward induction<sup>11</sup> to prove the following propositions and therefore obtain the theorem showing conditions under which the TTPSS is an equilibrium strategy. In other words, from the proof we want to show that the TTPSS would be a sequential equilibrium if agents in online auction markets had the free choice in abiding by it, so the strategy is in fact self-enforcing.

In the following, we define d as the discount factor, i.e., $\delta { = } 1 / ( 1 { + } i )$ with i being the interest rate, and we assume $0 < \delta < 1$ . We further define an agent’s timeweighted average payoff over the whole sequence of trades because it is used throughout the proofs: since the game is an infinite repetition of the stage game (the PD game), an agent’s time-weighted average payoff m is defined as [23]:

$$
\bar {v} = (1 - \delta) V
$$

where $V = \sum _ { t = 0 } ^ { \infty } \ \delta ^ { t } \nu _ { t }$ , because the payoff stream of $\boldsymbol { \nu } _ { t } ,$ $\begin{array} { r } { t = 0 , 1 , 2 , . } \end{array}$ . . has the same net present value as a constant payoff of m¯ in each period: $\sum _ { t = 0 } ^ { \infty } \ \delta ^ { t } \nu _ { t } = V = \sum _ { t = 0 } ^ { \infty } \ \delta ^ { t } \bar { \nu } ;$

thus, maximizing V is equivalent to maximizing m¯. We assume each agent is rational and maximizes his average payoff m¯. The following propositions give the conditions under which the agents will play according to the desired actions described in the TTPSS.

Proposition 1. An agent is willing to pay the judgment if the following inequality holds:

$$
f (J) <   \frac {\delta}{(1 - \delta) \theta}
$$

Proof. In the current period, if the TTP verifies that an agent cheated in a transaction after investigating a claim, the TTP asks the agent to pay $f ( J ) \pi _ { 0 }$ based on a basic judgment $J \pi _ { 0 }$ . Now, the agent has two options: pay the judgment or refuse to pay. If the agent pays $f ( J ) \pi _ { 0 }$ in the current period, then he can still keep his digital certificate. Other agents will treat him as an honest agent in future plays and play Honest with him, so his trading payoff will be $\pi _ { t }$ for all future periods for $t = 1 , 2 , 3 , 4 , . . .$ . according to the PD game in Table 1. Therefore, his expected lifetime average payoff after paying the judgment $f ( J ) \pi _ { 0 }$ is:

$$
\begin{array}{l} \bar {v} = - (1 - \delta) f (J) \pi_ {0} + (1 - \delta) E \left\lfloor \pi_ {1} \delta + \pi_ {2} \delta^ {2} + \pi_ {3} \delta^ {3} \right. \\ \quad \left. + \dots \right\rfloor \end{array}
$$

as $t \longrightarrow \infty .$

If the cheating agent refuses to pay the judgment, his digital certification will be revoked. According to the TTPSS, the revocation of the digital certificate will result in a situation where other agents will play Cheat with him. Thus, the agent’s payoff will be 0 in the present and in the future. The agent’s lifetime average payoff is therefore m¯ = 0. Therefore, the agent will want to pay the judgment if the following inequality holds:

$$
\begin{array}{l} - (1 - \delta) f (J) \pi_ {0} + (1 - \delta) E \left\lfloor \pi_ {1} \delta + \pi_ {2} \delta^ {2} + \pi_ {3} \delta^ {3} \right. \\ \quad + \dots \rfloor > 0 \end{array}
$$

The above inequality’s necessary condition is:

$$
\begin{array}{l} - (1 - \delta) f (J) \pi_ {\text { Max }} + (1 - \delta) E [ \pi ] (\delta + \delta^ {2} + \delta^ {3} + \ldots) \\ > 0 \end{array}
$$

Therefore, we have the following expressions:

$$
\begin{array}{l} - (1 - \delta) f (J) \pi_ {0} + (1 - \delta) E \left\lfloor \pi_ {1} \delta + \pi_ {2} \delta^ {2} + \pi_ {3} \delta^ {3} \right. \\ \quad + \ldots \rfloor > 0 \Leftarrow - (1 - \delta) f (J) \pi_ {\text { Max }} \\ \quad + (1 - \delta) E [ \pi ] (\delta + \delta^ {2} + \delta^ {3} + \ldots) > 0 \\ \Leftrightarrow - (1 - \delta) f (J) \pi_ {\text { Max }} + E [ \pi ] \delta > 0 \\ \Leftrightarrow - (1 - \delta) f (J) \theta E [ \pi ] + E [ \pi ] \delta > 0 \\ \Leftrightarrow - (1 - \delta) f (J) \theta + \delta > 0 \end{array}
$$

That is,

$$
f (J) <   \frac {\delta}{(1 - \delta) \theta}
$$

Proposition 2. A cheated agent will appeal to the TTP if and only $i f J { \ge } C .$

Proof. If an agent is cheated, he must calculate his benefit and cost, then make a decision: appeal to the TTP or not. If he appeals, he needs to pay the cost of the appeal, $C \pi _ { 0 } ,$ but his expected benefit is to get compensation $J \pi _ { 0 }$ . Therefore, the cheated agent would appeal if and only if $J \pi _ { 0 } \geq C \pi _ { 0 } ,$ that is, $J { \ge } C .$ 5

Proposition 3. If both agents have a valid digital certificate and they both have queried the TTP, for a certain agent, an agent will play Honest $i f g \le f ( J ) < \delta /$ $( l - \delta ) \theta .$

Proof. This proposition justifies the ‘‘Honest’’ part of agent’s behavior in Step 3 of the TTPSS. If an agent plays Honest at this time, his current period payoff will be $\pi _ { 0 }$ . If he cheats, his current period payoff will be $( 1 + g ) \pi _ { 0 }$ . If the agent cheats and does not pay the fine, his digital certificate will be revoked. According to the proof of Proposition 1, i $\ : f ( J ) < \delta / ( 1 - \delta ) \theta , \ :$ the cheating agent will pay the fine. If the agent cheats and later sticks to the TTPSS, then his payoff will be $( 1 + g ) \pi _ { 0 } - f ( J ) \pi _ { 0 }$ . Therefore, the equilibrium in which the agent will play Honest requires that the following condition hold:

$$
\pi_ {0} \geq (1 + g) \pi_ {0} - f (J) \pi_ {0}
$$

That is,

$$
f (J) \geq g
$$

Therefore, we get:

$$
g \leq f (J) <   \frac {\delta}{(1 - \delta) \theta}
$$

Proposition 4. If either agent does not have a digital certificate or if either agent does not verify his trading partner’s digital certificate, an agent will play Cheat.

Proof. This proposition justifies the ‘‘Cheat’’ part of the agent’s behavior at Step 3 of the TTPSS. According to the given strategy, his current play in this case will not have any influence on his future opportunities. Therefore, he will play Cheat to get a payoff of 0, which is greater than the payoff of $- \ l \pi _ { 0 }$ from playing Honest. 5

Proposition 5. An agent will query the TTP if he has a valid digital certificate.

Proof. This proposition justifies the first part of agent’s behavior at Step 2 in the TTPSS. If an agent who has a valid certificate queries the TTP, his expected payoff for the current period will be $\pi _ { 0 } ,$ and his expected payoff per period for the subsequent periods is also E[p]. Otherwise, his expected payoff will be 0. Therefore, the agent will query the TTP for a greater payoff. 5

Proposition 6. An agent that does not have a valid certificate will not query the TTP.

Proof. This proposition justifies the second part of agent’s behavior in Step 2 of the TTPSS. According to the Trusted Third Party system stage game, an agent who does not have a valid digital certificate will be punished (i.e., cheated) by his trading partner. No matter if he queries the TTP or not, his expected payoff is 0. In addition, if he plays Honest while the partner plays Cheat, his expected payoff will be $- \ l \pi _ { 0 } < 0$ . Therefore, querying the TTP or not querying the TTP really does not matter to an agent without a valid digital certificate. His equilibrium strategy is to play Cheat. 5

Proposition 7. An agent will buy a certificate if and only if the following inequality holds:

$$
F \leq \frac {E [ \pi ]}{1 - \delta}
$$

5

Proof. We demonstrate under what conditions an agent will find it more profitable to buy a digital certificate. If an agent applies for a digital certificate by paying the certificate initiation fee, $F ,$ and sticks to the TTPSS, then his expected lifetime average payoff is:

$$
\begin{array}{l} \bar {v} = - (1 - \delta) F + (1 - \delta) E [ \pi_ {0} + \pi_ {1} \delta + \pi_ {2} \delta^ {2} + \ldots ] \\ = - (1 - \delta) F + (1 - \delta) E [ \pi ] \sum_ {t = 0} ^ {\infty} \delta^ {t} \\ = - (1 - \delta) F + E [ \pi ] \end{array}
$$

as $t \longrightarrow \infty$

If an agent does not apply for a digital certificate, he does not have to pay the certificate initiation fee, F. According to the TTPSS, however, if either agent does not have a digital certificate, then both agents play Cheat. Therefore, an agent without a digital certificate in the electronic market can receive a payoff of at most 0, that is, $\bar { \nu } = 0 .$ . If no agent has a digital certificate, a single PD game results, for which the Nash equilibrium dictates that both agents cheat. For an agent to be willing to apply for a digital certificate, the following condition should hold:

$$
- (1 - \delta) F + E [ \pi ] \geq 0
$$

That is, $F \le E [ \pi ] / ( 1 - \delta )$

Theorem 1. The Trusted Third Party System Strategy is a symmetric sequential equilibrium strategy<sup>12</sup> of the Trusted Third Party system stage game if the following inequalities hold:

$$
F \leq \frac {E [ \pi ]}{1 - \delta}\tag{1}
$$

and

$$
\operatorname{Max} [ g, f (C) ] \leq f (J) <   \frac {\delta}{(1 - \delta) \theta}\tag{2}
$$

If the above conditions are satisfied, then the average payoff per period for each trading agent is $\bar { \nu } = E / \pi \jmath - ( I - \delta ) F$ at the equilibrium.

Proof. Theorem 1 is based on the above propositions. In other words, from the proofs of the propositions, we have derived the conditions under which the TTPSS is a symmetric sequential equilibrium strategy. From the proof of Proposition $^ { 7 , }$ we have obtained condition (1) for the TTPSS. From the proof of Proposition 2, we have $J { \ge } C$ and since the function $f ( x )$ is increasing and continuous, it follows that $f ( J ) \geq f ( C )$ . Combining this with the result of Proposition $3 \left( f ( J ) \geq g \right)$ , we have $f ( J ) \geq \operatorname { M a x } [ g , f ( C ) ]$ . From Proposition 1, we have $f ( J ) { < } \delta / ( 1 - \delta ) \theta$ . Condition (2) therefore follows. Based on the Optimality Principle of Dynamic Programming, we know that there is no situation in which a one-time deviation from the TTPSS is profitable for an agent provided that conditions (1) and (2) are satisfied. Therefore, we have proven that the TTPSS is a symmetric sequential equilibrium strategy of the TTP system stage game if conditions (1) and (2) hold. If the TTPSS is played by every player in the Trusted Third Party system stage game, then nobody will cheat. Therefore, the average payoff m per period for each player is

$$
\bar {v} = E [ \pi ] - (1 - \delta) F.
$$

The conditions given in the theorem show the relationship among the various parameters for the TTP to support the efficient cooperation. For example, suppose there are repeated transactions where the expected average payoff when behaving honestly is $E [ \pi ] = 1 0 , \theta = 2$ and the gain from cheating $( 1 + g ) \pi$ is 30 where $g = 2$ . We assume that $f ( x ) = ( 1 + p ) x$ where $p$ is the percentage of value that is incurred to investigate when a complaint is made. Let us suppose that $p { = } 0 . 5$ and the cost of appealing Cp is 2 with $C { = } 0 . 2$ We further assume that $\delta = 0 . 9$ . Then, $F \le 1 0 0$ as the initiation fee is sufficient to encourage participants to obtain a digital certificate, and $2 0 \leq f ( J ) \pi < 4 5$ is the judgment that is sufficient enough to provide the incentives for not cheating or complaining about being cheated. In other words, the TTPSS is in equilibrium and supports honest behavior.

In summary, conditions (1) and (2) make the design effective: First, it ensures that market participants are adequately well informed and whether their trading partner has defected before through the use of their digital certificates. This information dissemination process does not require that every participant know the full history of every other participant’s behavior. Second, the design motivates auction participants to keep informed and to sanction against cheaters even though there is a personal cost involved. Finally, the design provides incentives to the participants to report cheating behaviors so that the cheater will not profit from his action.

## 6. Discussions and conclusion

In this paper, we presented an analytical model that is intended to provide guidelines for designing extralegal institutions. Such institutions could be used in the absence of legal enforcement to address some of the critical issues in online auction markets. By introducing a trusted third party that not only issues digital certificate but also punishes cheating behavior, agents can obtain information regarding a trading partner’s past history. This can be done by verifying whether the partner has a valid digital certificate. If a digital certificate is issued through strong authentication, a market participant will not be able to easily change his identity after committing fraud at one online auction site. That is, rather than being simply an authentication tool, a digital certificate also represents an agent’s reputation. In other words, the reputation effect will follow the certificate holder no matter where he goes because the certificate is bound to a real-world entity. This addresses the limitation of the currently available systems, such as the feedback forum at eBay where a participant’s reputation does not reflect the whole past trading history of the participant because of easily changeable identities.

Another advantage of the model is that the reputation information associated with a digital certificate (a participant’s online identity) is more reliable and less prone to individual manipulation. Information is filtered by the TTP before going public. Therefore, the reputation information provided is more credible and has more of an impact in future transactions.

However, there are some limitations to the current design. In this research, we attempt to outline a framework of a trusted third party that can promote trust for online auction communities. Therefore, we have simplified the actual world with some assumptions. For example, we assume that all the TTPs are connected and it does not matter which TTP an agent gets his certificate from. In reality, there could be many TTPs located in different countries. How to efficiently get information distributed from one TTP to another is a big challenge and has to be worked out in the future. Also, we assume that the TTP can investigate each disputed case in a cost-effective way. In addition, we do not address in this paper the technological framework of the TTPs. Since verification of certificates is a critical step of the model, being able to quickly verify certificates and update information on certificate status (e.g., valid or revoked) becomes critical to the success of the model. Realtime certificate verification is a major research topic in the computer science community. The realization of our design model certainly depends a great deal on advances in that area.

Our design has strong practical implications. Although it is widely acknowledged that obtaining complete information about a trading partner is almost impossible in global online auction markets, the trusted third party presents an effective alternative in filling the gap. The economies of online interactions and the available computing power make possible a reputation system that could not be supported otherwise. In other words, with the services of TTPs, we convert the private knowledge that exists between a pair of business partners on their past trading behavior to public knowledge, thus making the reputation system effective again in global online markets. Due to the existence of this knowledge base, business agents have to maintain and protect their reputation if they want to continue their business. Therefore, even though information asymmetry may lead to market inefficiency, we can design and create trusted third parties to reduce asymmetric information, and thus to prevent potential market failure. In a sense, creating this kind of TTP could be a great business opportunity. Just like Trust.e (http://www.truste.com) and BizRate (http://www.bizrate.com) are currently playing an important role in building trust in electronic markets, our proposed TTP model sheds light on a new type of TTP, which may significantly promote trust in online consumer-to-consumer auction markets.

## Acknowledgements

The authors gratefully acknowledge helpful comments from Jian Yang, De Liu, Jan Stallaert, Shijie Deng, Xianjun Geng and the participants of the 1999 International Conference on Information Systems (ICIS).

## References

[1] G. Akerlof, The market for lemons: quality uncertainty and the market mechanism, Quarterly Journal of Economics 84 (3) (1970) 488 – 500.

[2] R. Axelrod, The Evolution of Cooperation, Basic Books, New York, 1984.

[3] J. Bendor, D. Mookherjee, Norms, third-party sanctions, and cooperation, Journal of Law, Economics, and Organization 6 (1) (Spring 1990) 33 – 63.

[4] L. Bernstein, Opting out of the legal system: extralegal contractual relations in the diamond industry, Journal of Legal Studies 21 (1992) 115– 121.

[5] E. Brynjolfsson, M. Smith, Frictionless commerce? A comparison of internet and conventional retailers, Management Science 46 (4) (April 2000) 563 – 585.

[6] D. Charny, Illusions of a spontaneous order: ‘norms’ in contractual relationships, University of Pennsylvania Law Review 144 (5) (1996) 1841– 1858.

[7] S.-Y. Choi, D.O. Stahl, A.B. Whinston, The Economics of Electronic Commerce, Macmillan Technical Publishing, Indianapolis, Indiana, 1997.

[8] J.S. Coleman, Systems of trust: a rough theoretical framework, Angewandte Sozialforschung 10 (1982) 277 – 286.

[9] C. Corcoran, The auction economy, Red Herring 69 (August 1999) http://www.redherring.com/mag/issue69/NEWSauctions.html.

[10] R.C. Ellickson, Order Without Law, Harvard Univ. Press, Cambridge, MA, 1991.

[11] W. Ford, M.S. Baum, Secure Electronic Commerce: Building the Infrastructure for Digital Signatures and Encryption, Prentice-Hall, New Jersey, 1997.

[12] A.M. Froomkin, The essential role of trusted third parties in electronic commerce, in: R. Kalakota, A.B. Whinston (Eds.), Readings in Electronic Commerce, Addison-Wesley, Reading, Massachusetts, (1996) 119 – 176.

[13] X.R. Hu, Z.X. Lin, H. Zhang, Myth or reality: effect of trustpromoting seals in electronic markets, Proceeding of the Eleventh Annual Workshop on Information Technologies and Systems (WITS), New Orleans, Louisiana, (2001) 65 – 70.

[14] Internet Fraud Watch. 2002. Available: http://www.fraud.org/ internet/2001stats10mnt.htm.

[15] S. Jarvenpaa, N. Tractinsky, M. Vitale, Consumer trust in an internet store, Information Technology and Management 1 (1 – 2) (2000) 45– 71.

[16] J. Johnston, The statute of frauds and business norms: a testable game-theoretic model, University of Pennsylvania Law Review 144 (5) (May 1996) 1859 – 1912.

[17] M. Kandori, Social norms and community enforcement, Review of Economic Studies 59 (1992) 63– 80.

[18] P. Kollock, The production of trust in online markets, in: E.J. Lawler, M. Macy, S. Thyne, H.A. Walker (Eds.), Advances in Group Processes, vol. 16, JAI Press, Greenwich, CT, 1999. http://www.sscnet.ucla.edu/soc/faculty/kollock/papers/ online<sup>\_</sup>trust.htm.

[19] D. Kreps, R. Wilson, Sequential equilibria, Econometrica 50 (1982) 863 – 894.

[20] B. Lee, B. Yoo, Internalization of Electronic ‘‘Auction Market’’ and Information Asymmetry in Electronic Commerce, WISE presentation, http://www.gsia.cmu.edu/andrew/sandras/ public/wise/pdf/blee01.pdf (1999).

[21] R.J. Lewicki, B.B. Bunker, Developing and maintaining trust in work relationships, in: R.M. Kramer, T.R. Tyler (Eds.), Trust In Organizations: Frontiers of Theory and Research, SAGE Publications, Thousand Oaks, CA, (1996) 114 –139.

[22] S. Macaulay, Non-contractual relations in business: a preliminary study, American Sociology Review 28 (1) (1963) 55– 67.

[23] A. Mas-Colell, M. Whinston, J. Green, Microeconomic Theory, Oxford Univ. Press, New York, New York, 1995.

[24] P.R. Milgrom, D.C. North, B.R. Weingast, The role of institutions in the revival of trade: the law merchant, private judges, and the champagne fairs, Economics and Politics 2 (1) (March 1990) 1 –23.

[25] P. Resnick, R. Zeckhauser, E. Friedman, K. Kuwabara, Reputation systems: facilitating trust in internet interactions, Communications of the ACM 43 (12) (2000) 45– 48.

[26] B. Schneier, Applied Cryptography: Protocols, Algorithms and Source Code in C, Wiley, New York, 1994.

[27] T. Yamagishi, M. Yamagishi, Trust and commitment in the United States and Japan, Motivation and Emotion 18 (2) (1994) 129 – 166.

![](/api/attachments/ZV2FKZMJ/fulltext/images/d0e8311444ed97f3e9513139a1c946646bf24cdd06a402809b403f2f923c77c5.jpg)  
Sulin Ba is Assistant Professor of Information Systems at the Marshall School of Business at the University of Southern California. Her research interests focus on the design of trust-building intermediaries that facilitate electronic-market transactions. Her work on the institutional set-up to help small business survive and grow in the digital economy has been used as the basis for testimony before the Congressional House Committee on Small Busi-

ness. She has published in Management Science, Information Systems Research, MIS Quarterly, and other academic journals.

![](/api/attachments/ZV2FKZMJ/fulltext/images/e4977ae87136954bb0bcab724cd73ab40911e4e1dec505e365f9098c65a67d91.jpg)

Andrew B. Whinston is currently Professor of Information Systems, Economics, and Computer Science, Hugh Roy Cullen Centennial Chair in Business Administration, Director of Center for Research in Electronic Commerce at The University of Texas, Austin. He has published over 300 papers in top-rated scientific journals. He recently co-authored the following books: The Frontiers of Electronic Commerce, Electronic Commerce—A Manager’s

Guide, The Economics of Electronic Commerce, The Internet Economy: Technology and Practice, and Electronic Commerce and the Revolution in Financial Markets.

![](/api/attachments/ZV2FKZMJ/fulltext/images/39eee85a9aef8802cdc8622c0c74205b4c29dbcda95a3cf527f063e39f535166.jpg)  
Han Zhang is Assistant Professor of Information Technology Management at the DuPree College of Management at Georgia Institute of Technology. He received his PhD in Information Systems from the University of Texas at Austin in August 2000. His research focuses on digital products and digital companies, online trust-related issues and intermediaries, and the evolution of electronic markets.
