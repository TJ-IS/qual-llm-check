---
otero_id: 20977
otero_key: "ET9PFTFP"
title: "Establishing online trust through a community responsibility system"
authors: "Sulin Ba"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00144-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Establishing online trust through a community responsibility system

Sulin Ba<sup>)</sup>

Department of Information and Operations Management, Marshall School of Business, UniÕersity of Southern California, Los Angeles, CA 90089, USA

## Abstract

Much of the research on trust building in electronic commerce takes a descriptive approach. The question of what social structures are more appropriate to promote trust in the online world has not been extensively studied. We analyze in this paper, using a prescriptive approach, how a certain social structure—a community responsibility system, supported by present technology, can be set up. We use game theoretic tools to prove that under the community responsibility system for trust building, online transactions that are impersonal can be supported and can preserve at the same time anonymity to a large extent. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Trust; Online community; Game theory; Community responsibility system; Online transactions

## 1. Introduction

Technology enables market exchanges in ways that were not possible before, such as online exchange of goods and services in the electronic market without ever meeting the trading partner. While the electronic market brings people together AvirtuallyB from all over the world and opens up new business opportunities, there are also some significant social implications resulting from the existing technology infrastructure. For example, one concern constantly raised is that Aon the Internet, no one knows you are a dog,B meaning online trading parties can easily remain anonymous or change their identities. Online transactions therefore turn to impersonal exchanges, which introduces opportunities to misbehave without paying reputational consequences. In fact, the number of reported Internet frauds has increased significantly over the last few years. In 1999 alone, consumers lost over US\$3.2 million to Internet fraud. A 38% increase in Internet fraud complaints in 1999 coupled with an average consumer loss of as much as US\$580 is significantly affecting consumer trust towards online business 15 .<sup>w</sup> <sup>x</sup>

In the conventional marketplace, a set of social, economic, and legal systems provides the basis for protecting business activities and consequently induces trust towards business transactions. Unfortunately, the social, economic, and legal systems have not yet caught up with the growth of electronic commerce. For instance, on the legal side, the Uniform Commercial Code which defines US law aboutŽ business transactions has not been extended to elec-. tronic commerce. Even when it is, there is no legal system that could support, at low cost, the enforcement required for such exchange. From a social perspective, trust is often built through repeated interactions over time or through established social networks 19,20,23,28 . However, most of these<sup>w</sup> <sup>x</sup> forms of exchange are not well established in electronic markets since many online transactions occur between buyers and sellers who have no prior relationships. Many buyers and sellers are new entrants to the marketplace without established brand name or recognition. In addition, these online transactions are often characterized by separation between the quid and the quo Žwhat is acquired and what it is acquired for over time and space. In this environ- . ment, the traditional setting for establishing trust based on repeated interactions not only may be unrealistic, but could also restrict the flexibility of transacting parties to explore new opportunities 26 . <sup>w</sup> <sup>x</sup> Consequently, the question of how to establish online trust necessary for electronic transactions becomes of paramount importance.

Much of the research on trust building in electronic commerce takes a descriptive approach <sup>w</sup> <sup>x</sup> 7,9,16 . The question of what social structures are more appropriate to promote trust in the online world has not been extensively studied. We analyze in this paper, using a prescriptive approach, how a certain proper social structure, supported by present technology, can be set up. We use game theoretic tools to prove that online transactions that are impersonal can be supported and can preserve at the same time anonymity to a large extent. Our level of study is at the individual to individual level—how to promote trust between individuals when transactions are impersonal? We argue that an anonymous individual’s behavior as well as the present social structural setup to secure trust between transacting parties can be analyzed using game theory. The design and implementation of systems that are geared towards providing trust require a formal investigation to obtain the levels of trust that will ultimately be offered.

Historical studies of contract enforcement institutions that supported inter-community and impersonal exchange in pre-modern Europe indicate that a community responsibility system was effective in enforcing honest behaviors during impersonal exchanges that were not expected to take place frequently. In the online world, there is a strong move towards community as a social structure, such as in the case of eBay and iVillage. In fact, community has been taunted as the Holy Grail of the Internet. The implication for practitioners is how to take advantage of communities and use communities as a social structure to support impersonal exchange. This community might be an online community such as The Well or a religious community that influences the ethical values and behaviors of individuals. We provide a normative analysis in this paper to illustrate how, by expanding communities’ responsibilities, communities can be used as a social structure to provide online trust.

The rest of the paper is organized as follows: Section 2 summarizes different types of trust and trust building processes, and identifies the major online barriers to trust. Section 3 gives a brief overview of the major trust building mechanisms currently in use or proposed by researchers. In Section 4, a formal analysis of a community structure is given that is aimed at promoting trust and ensuring secure online impersonal transactions. Section 5 provides insights to the sustainability of such a social structure. Section 6 concludes the paper.

## 2. Developing online trust

## 2.1. Types of trust

In the definitions of trust that appear in the literature, researchers have viewed trust from many angles. For example, economists suggest that trust is a form of implicit contracting 1,4 . Psychologists ap- <sup>w</sup> <sup>x</sup> proach trust as the generalized expectation of an individual that the promise of another individual can be relied upon 24 . In general, trust is defined in<sup>w</sup> <sup>x</sup> terms of three central characteristics: reliability, predictability, and fairness. The exchange partner is expected to be credible such that its word or promise can be relied on 24 ; the exchange partner will <sup>w</sup> <sup>x</sup> behave in ways that equitably protect the welfare of both parties 3,21 ; and the exchange partners are <sup>w</sup> <sup>x</sup> dedicated to reciprocating the obligations and commitments between them under an environment of uncertainty and vulnerability.

Trust is a binding force in most buyer–seller transactions. It is especially critical when two situational factors are present in a transaction: uncertainty

Ž . Ž risk and incomplete product information information asymmetry . Many researchers proposed that . trust is essential for understanding interpersonal behavior and economic exchanges e.g., Ref. 13 .Ž <sup>w</sup> <sup>x</sup>.

Research suggests that in the beginning of a business relationship, trust is often deterrence or calculus based 25 . Individuals will do what they<sup>w</sup> <sup>x</sup> say because they fear the consequences of not doing what they say. Trust is an on-going economic calculation whose value is derived by comparing the outcomes resulting from creating and sustaining the relationship to the costs of maintaining or severing it. At this stage, the parties Aattempt to determine the nature of their interdependence, what they will get from the relationship and give to it, and what their risks and vulnerabilities areB <sup>w</sup> <sup>x</sup> 18 . Any inconsistency in behavior on the part of either party can easily destroy the relationship and result in one or both parties terminating the relationship.

As the relationship develops, the transacting parties gain more and more information about each other through their experiences. The presence of information communicated by the exchange partners contributes to the relationship by creating a level of predictability of the other partner and makes it possible to move trust to the next level: information-based trust. Because of the knowledge that the partners have of one another, they can better estimate the likely actions of the other, thus reducing the sense of uncertainty and risk. The development of this level of trust grows over repeated contact and communication; the partners monitor one another to learn about the other’s preferences and behaviors. They cultivate their knowledge of one another by interacting with each other in different contexts and building upon those past experiences 18 . <sup>w</sup> <sup>x</sup>

The above two types of trust provide a strong foundation for an even higher level of trust: transference based trust. Because of the strong trust the trustor has developed towards a third party, he is willing to use this trusted third party’s definition ofŽ . another as a basis for defining that other as trustworthy. In other words, although the trustor may have no previous direct experience at all with the other party, he forms his trust by transferring his trust of the third party to the latter. In this level of trust, the trusted third party plays a significant role. For example, research indicates that when a web site is allied with a bank which is normally considered credible and Ž trustworthy for payment processing, people tend to . trust the web site more. Fig. 1 adapted from Ref.Ž <sup>w</sup> <sup>x</sup> 18 represents how different levels of trust develop . over time.

## 2.2. Major online trust barriers

Electronic commerce is a new form of exchange where online transactions could occur among entities that have never met before. As in traditional exchanges, trust has been considered crucial in the online transaction process 5,6 , perhaps more so<sup>w</sup> <sup>x</sup> given the impersonal nature of the online environment uncertainty and the inability to judge product Ž . quality prior to purchase information asymmetry .Ž . With the global, but insecure, Internet being the primary carrier of electronic commerce transactions, web sites can be counterfeited, identities can be forged, and the nature of transactions can be altered. Since the inception of commercial activities on the Internet, information asymmetry, which means that both parties do not have the same information 2 ,<sup>w</sup> <sup>x</sup> has been perceived by some to be a significant barrier to the extensive acceptance of the electronic market. As FTC Chairman Robert Pitofsky said in his opening remarks at a consumer protection workshop: AThe informal nature of the medium, the lack of personal contact between buyer and seller, and the geographic dispersion of sellers create new and unprecedented opportunities for consumer abuse through fraud and deceptionB. That is, there exists asymmetric information on the authenticity and integrity of business transactions. If not effectively addressed, these market imperfections Acan undermine the full development of global competition itselfB.<sup>1</sup>

Among the many aspects of information asymmetry, two are closely related to online fraud: one being the identity of online trading parties, the other the product quality uncertainty. As manifested by the famous New Yorker cartoon that Aon the Internet, no one knows you are a dogB, online trading parties can easily remain anonymous or change their identities.

![](/api/attachments/ET9PFTFP/fulltext/images/6a2bf0b2b94047459da29db0610fbf6efb63332188e5c334e60e950acd1e9ead.jpg)  
Fig. 1. The stages of trust development. A At this point, some calculus-based trust develops into information-based trust, while otherŽ . relationships never move past calculus-based trust. B At this point, some information-based trust develops into transference-based trustŽ . <sup>w</sup> <sup>x</sup> 18 .

For example, in the auction market where numerous individuals participate in transactions, it is very hard to bind one identity to one trader. Most of the auction sites identify sellers or bidders by email addresses, which can be easily obtained without monetary cost from multiple sources.

Information asymmetry with respect to product quality uncertainty means that transacting parties do not have the same information about the product quality. In the traditional business setting, people get to know the quality of products by looking, touching, and feeling. However, when bidders view a product listing at an online auction site, for example, they do not have ready or easy access to information regarding the true quality of the product. Recognizing the difficulty of verifying user identity and guaranteeing product quality, eBay excuses itself from the responsibility in its User Agreement:

Because user authentication on the Internet is difficult, eBay cannot and does not confirm each user’s purported identity.

eBay have no control over the quality, safety or legality of the items advertised, the truth or accuracy of the listings.<sup>2</sup>

Without a doubt, the two aspects of information asymmetry expose electronic market participants to more risks and fraudulent transactions. Many, therefore, lack the trust necessary to engage in e-commerce transactions.

With an understanding of different types of trust and how trust develops, clearly, the more critical question is: what forms of mechanisms can help generate trust, thus facilitating electronic commerce?

## 3. Reputation systems

Many of the studies on trust focus on trust development in the context of a close, personal relationship 14,22 . In other words, repeated interactions<sup>w</sup> <sup>x</sup> and long term relationships are key to developing trust. However, this basic assumption is no longer valid in the online environment. In many situations, individuals or organizations need to decide whether they can trust a person or an organization without any prior interactions. How to develop this initial trust? In this section, we summarize several approaches based on the trust-building processes identified in Section 2.

## 3.1. Feedback systems

Several models have been proposed using game theory approaches. Transactions are analyzed as repeated games. When business entities engage in repeated transactions in a market, they need to be concerned about their reputation. This basically is a calculus-based trust building approach. Compliance with calculus-based trust is often ensured both by the rewards of being trustworthy e.g., continued busi-Ž ness and by the. AthreatB of trust being violated. Therefore, reputation ideally should serve as an effective enforcement measure for honest behavior. This is the philosophy behind eBay’s Feedback Forum, where consumers can use the forum to rate their satisfaction towards their trading partners. Other users are encouraged to check their trading partners’ ratings before transactions and leave feedback about their trading partners after their transactions. The enforcement comes from the idea that dishonest behavior against one agent causes sanctions or retaliations by other agents in the same market.

The feedback-based reputation systems have, to some extent, promoted trust in the online environment. Reputation systems can serve both as a source of information and as a potential source of sanctions. The existence of reputation information is an incentive for the participants in a transaction to be trustworthy because of the damaging effects of acquiring a bad reputation 17 . However, the current reputa-<sup>w</sup> <sup>x</sup> tion systems have several limitations. First, the rationale behind the feedback systems is that the reputation of an online participant is a signal of one’s past trading behavior. A bad reputation i.e., low-feed- Ž back rating will discourage others from conducting. future transactions with the participant. However, the ratings thus the reputation are based on onlineŽ .

identities which are often not more than an email address. Currently auction sites do not provide strong authentication. Consequently, a person with a bad rating can easily acquire a new email address and re-register with no trace of the earlier bad reputation. That is, the past history of a cheater remains private information one aspect of asymmetric informationŽ . and does not serve as an effective deterrent of future transactions. Moreover, a person who has developed a very bad feedback rating at one site can go to another transaction site as a new user and cheat again. Both situations result from the lack of strong authentication of online identities.

## 3.2. Trusted third parties

In addition to the above systems that are already in use, 5 outlines an extralegal mechanism—a <sup>w</sup> <sup>x</sup> trusted third party—that addresses some of the limitations with those systems. Their model not only authenticates the identity of trading agents by issuing digital certificates, but also disseminating information about agents’ behaviors. Specifically, the digital certificate issued by a TTP serves not only as authentication of the certificate holder, but also as a reputation indicator. Anyone who holds a valid digital certificate should be regarded as a reputable agent. If a certificate holder is reported to have cheated in the market, the TTP will investigate the case and ask the cheater to pay a fine. However, the TTP is not a legal institution that could enforce rules, thus paying fines adjudicated by the TTP is voluntary. If the cheater pays the fine, he will keep his digital certificate and others will still treat him as an honest agent in the future; otherwise, his digital certificate will be revoked by the issuing TTP. Without the digital certificate, he risks being regarded not trustworthy and may lose his business in the long run. Using a game theoretical approach, Ba et al. 5 demonstrates <sup>w</sup> <sup>x</sup> that the proposed TTP model is an effective mechanism to promote calculus-based and informationbased trust in the electronic market. This model provides the extra protection that the online market participants cannot change their identities easily and their reputation history is tied to a fixed identify that will follow them no matter which online market they choose to participate in.

Having a digital certificate issued through strong authentication, a market participant would not be able to easily change his identity after committing fraud. The reputation effect will follow the certificate holder no matter where he goes because the certificate is not bound to an email address but to a real world entity. This addresses the limitation of the currently available systems such as the feedback forum at eBay where a participant’s reputation does not reflect the whole past trading history of the participant because of easily changeable identities.

In summary, economic analysis of the above mentioned reputation system indicates that the system is effective under the following conditions: first, the transactions are expected to repeat infinite number of times. Second, each party in the transaction has a fixed identity that cannot be easily changed and is known to all the parties. Third, the previous history of the transactions is common knowledge. That is, the information on how each party behaved in the past is available to all, thus promoting calculus and information-based trust.

Yet, not surprisingly, this model can also be rendered ineffective for the following three reasons: First, when a player adopts a fly-by-night strategy and takes the profit without ever coming back to the market, the reputation left behind does not matter any more. Then, what is a trusting agent’s recourse when such a situation happens? Second, even when people do engage in repeated transactions, each party has a finite lifetime. At the last transaction, cheating can always happen and the cheating party does not bear the consequence of being punished by others. How to promote trust in this situation? Third, an agent’s identity is central to the success of the system. As more agents get concerned about the privacy and anonymity issue in the online world, a fixed identity at the personal level is not desirable. How to achieve trustworthiness without compromising one’s anonymity?

## 4. Community responsibility systems

Economists have discovered that communities play a strong role in impersonal market exchange. Research in economic history has shown that an economic institution able to support impersonal exchange characterized by separation between the quid and the quo over time and space was feasible despite the lack of appropriate legal contract enforcement <sup>w</sup> <sup>x</sup> 10 . During the late medieval period, there were many long-distance trades in which goods were sent first and money received later or vise versa amongŽ . merchants who did not know each other and did not expect to interact frequently. There was no instant exchange of goods and money. In that case, a community responsibility system helped generate the trust necessary to carry out the trades. Each community was responsible for its members trading behavior and disciplined members who cheated. Otherwise, other communities could take collective action and retaliate against the whole community. Therefore, it was the community’s reputation rather than eachŽ individual member’s reputation that traders used to . determine whether its members were trustworthy. The essence of this institutional setup is to condition actions on one’s social affiliation rather than on each individual’s past behavior. By holding all members of a community responsible for the behavior of a particular member, the community is provided with the incentive to employ its intra-community enforcement to ex post punish one who defaulted in intercommunity exchange.

In short, the community social structure enforces economic agents to condition their actions on one’s social affiliations, therefore supporting inter-community, impersonal market exchanges. Yet, commercial enterprises have been slow to make use of the unique community-building capabilities of the Internet and the potential power of online communities that have been a binding force among many net users.

A few authors have recognized the power of online communities also called virtual communities :Ž . AWhen computer networks link people as well as machines, they become social networks, or the basic building blocks of societiesB. 12 . Several authors<sup>w</sup> <sup>x</sup> have proposed that online communities are important drivers of value in electronic commerce 8,11,27 . <sup>w</sup> <sup>x</sup> Online communities have been formed to serve various purposes, such as providing emotional support, socializing with others, sharing information on commonly interested tasks. The participants of these social networks often have a strong commitment to the community. They are linked by common interests and<sup>r</sup>or values. Online communities involve sociability and a sense of belonging as important ends in themselves. In addition, the placeless nature of online community interactions facilitates long-term contact without the loss of relationships that often accompanies residential mobility.

The recognition of the potential power of online communities and the historical evidence of the effectiveness of community responsibility systems motivated us to formally analyze online transactions and the necessary structure of an online community system aimed at promoting online trust.

As mentioned in Section 3, currently available systems aimed at solving the above problem utilizes the reputation effect that comes with repeated transactions repeated games . The difficulty is how toŽ . deal with the last move cheat and leave if the gameŽ . is not infinitely repeated. Recognizing the fact that each individual agent has a finite life span, we propose a community structure in which agents can trade with each other across communities at the community level. Agents who want to be perceived as trustworthy and want the protection of the community structure from being cheated by others can join a community that has a good reputation. There will be multiple online communities on the market, each with its own reputation standing. Each community aims to maximize the sum of the lifetime utilities of its constituting members. This mechanism is a transference-based trust promoting mechanism— when a community is trustworthy, the design of the community structure ensures that the members of the community can be trusted as well. When two agents from two different communities trade with each other, the transaction would take place as if the two communities were trading with each other. The game would therefore turn into an infinitely repeated game —it is reasonable to assume that although individual members of a community have a finite time period for trading, the community as a whole will carry on infinitely, replacing old members with new members.

One of the concerns in the online world is how to preserve individual’s privacy and anonymity. The existing mechanisms available to promote trust and ensure secure transactions mostly center around one’s reputation, which is identity based. In the community structure we propose, agents’ identities are only known to their own community. To agents outside of their own community, only their community membership is known. Thus, transactions can still remain impersonal, allowing agents to preserve their anonymity to a large extent. In a particular transaction, if transacting agents are members from several communities, exchange would be impersonal up to one’s community label. The communities serve as a trusted party that others can trust.

The payoff structure of the stage game

<table><tr><td></td><td colspan="2">Player 2</td></tr><tr><td>Player 1</td><td>Honest</td><td>Cheat</td></tr><tr><td>Honest</td><td> $\pi_t, \pi_t$ </td><td> $-l\pi_t, (1 + g)\pi_t$ </td></tr><tr><td>Cheat</td><td> $(1 + g)\pi_t, -l\pi_t$ </td><td>0, 0</td></tr></table>

Next, we formalize our analysis of online transactions to illustrate how the community structure works.

## 4.1. Modeling online transactions

In our analysis, each non-repeated transaction theŽ stage game is assumed to be the Prisoners’ Dilemma. Ž . PD game described by Table 1. By using the PD model, we demonstrate why reputation information just between two transacting parties and reputation information that is restricted to one single trading community are not sufficient; and why other social structures are needed to help promote trust and ensure secure transactions in the global online market.

Suppose that a seller and a bidder are engaged in a single exchange involving a product. Each of them can choose to play one of two strategies: Honest or Cheat. Table 1 presents the payoff structure of the PD game. The first number in each entry indicates the row player seller ’s payoff and the second is the Ž . column player buyer ’s payoff. In periodŽ . t, if both the bidder and the seller are honest, they each have a payoff of $\pi$ . We assume that $\pi _ { t } ^ { \cdot } \mathbf { s }$ are independently identically distributed random variables with the common distribution of $\pi ^ { \prime } s$

In period t, if both the bidder and the seller cheat, each has a payoff of $0 . { } ^ { 3 }$ If one of the players cheats, the cheater gets a payoff of $( 1 + g ) \pi _ { t }$ while the cheated incurs a loss of $l \pi _ { t }$ , where l and g are positive constant coefficients. We also assume $g \pi _ { t }$ $- l \pi _ { t } < \pi _ { t }$ , that is, $0 < g - l < 1$ . If one player decides to cheat while the other is honest, then the cheater has his highest payoff of $( 1 + g ) \pi _ { t }$ , while the honest one gets his lowest of $- l \pi _ { t }$ . This gives both sides an incentive to cheat, even though honest behavior maximizes the total payoff of the two players: $( 1 + g ) \pi _ { t } - l \pi _ { t } < \pi _ { t } + \pi _ { t }$ according to the assumption $g - l < 1$

Obviously, if this transaction is conducted only once, it is to each player’s separate advantage to play Cheat, since that play yields a higher payoff regardless of what the other player does. Accordingly, the only Nash equilibrium of the game is for both players to play Cheat. It is, however, worth noting that both agents are worse off than if they could somehow agree to play honest because the payoff of both playing honest is $\pi _ { t }$ while the payoff is only 0 if both play cheat. The PD game demonstrates the idea that cheating might be profitable in a single business transaction. In the online market, for example, some sellers might find that a fly-by-night strategy of quality reduction is profit maximizing. This problem is exacerbated when agents can easily change or disguise their identities.

## 4.2. Modeling online transactions through community systems

The proposed community system is aimed to mitigate the above mentioned problem. We now formalize the online transaction process with the support of the community system to illustrate the community’s role by structuring the events with the following sequence of play, which we call the online community stage game. For simplicity of writing, in the following we always assume the current time period $t = 0$

Ž . Ž . 1 Before any agent buyer and<sup>r</sup>or seller is engaged in online transactions, he may apply for membership to join a community. Each community has its own membership criteria and reputation standing. The agent’s identity and other historical information are investigated; enquiries to other communities are made to check the agent’s past behavior. If an agent is accepted by a community, then each time the agent conducts a transaction, he will pay the community a fee of $\tau \pi$ where $0 < \tau < 1$

Ž . 2 When two agents meet in an online market to do business transaction, they first check whether the other party belongs to a reputable community. If the other community is considered reputable by his own community, the agent will go ahead and trade.

Ž . 3 The two trading agents interact by playing the Prisoners’ Dilemma game and get the payoffs Ž . according to Table 1 .

Ž . 4 After the exchange, either one of the two agents may make an appeal to his own community at personal cost $C > 0$

Ž . 5 If an agent makes an appeal to his own community, then his community investigates the case when there is no current sanction against the other community and verifies whether or not cheating has occurred. If the community concludes that the other party indeed cheated, the community will demand compensation F from the other community. F should be big enough so that the agent will get at least what he would have if trading has been honest on both sides, that is, $F - l \pi \geq \pi .$ 4

Ž . 6 The other community can verify any complaint about its cheating member and can decide whether to impose a punishment on the cheating member and to order the member to furnish the demanded compensation to the complaining community, or to refuse compensation.

Ž . 7 If compensation F is decided, the cheating member may pay the compensation, or he may refuse to pay the fine, at personal cost 0.

Ž . 8 If the cheating agent refuses to pay the compensation, his community revokes his membership, and furnishes the compensation to the other community. It is assumed that the community will furnish information about the expelled agent’s cheating behavior to any other community that requests it. Then the probability $P ( a )$ of the cheating member getting accepted by other communities is $0 \leq P ( a ) < 1$ , with $P ( a )$ assumed to be small.

Ž . 9 If the cheating agent’s community refuses to pay the compensation, the other community imposes sanction on the community: the sanction can be in the form of cheating in any future transactions with any member from this community, which means that all trading will be stopped since the other commu-Ž nity anticipates future cheating ..

According to the design, a cheating agent’s community is motivated to punish the member who cheated because failure to do so implies the loss of future gains from exchange for the whole community. A community whose member complains about being cheated is motivated to verify any complaints and demand compensation if cheating occurred because otherwise a cheated member would not complain, leading other communities to cheat and hence reducing the community’s total payoff.

In the following we describe the desired behavior of the agents, the Online Community System Strategy Ž . OCSS , which is a complete contingent plan describing the desired actions for each agent in each conceivable evolution of the game under the online community system.

Ž . 1 At the first step of the stage game, an agent applies to join a reputable virtual community before he conducts any business transactions in the electronic market.

Ž . 2 At the second step of the stage game, an agent verifies a trading partner’s community membership if he himself belongs to a reputable community.

Ž . 3 At the third step, an agent will trade with an agent from another community if there is no sanction against the other community; the agent will behave honestly if and only if the other community complains after being cheated, and his own community has not refused to pay a compensation.

Ž . 4 At the fourth step, if both agents verified their trading partner’s community membership to be valid at step 2 and exactly one of the two agents played Cheat at step 3, then the cheated agent victimŽ . makes an appeal to his own community; otherwise, no agents appeal to his community.

Ž . 5 At step five, if an appeal is made by a member, the community verifies the complaint. If and only if the complaint is valid, the community then demands compensation from the cheater’s community equal to the present value of the cost imposed on the cheated.

Ž . 6 At step six, the cheating agent’s community demands compensation from its member the cheat- Ž ing agent if and only if it believes the member has. cheated. The cheated community calls for sanction from its members on the cheating community if the cheating agent’s community refuses to pay compensation.

Ž . Ž . 7 At step seven, the cheating agent defendant pays the compensation F if and only if he had a valid community membership before the trading.

Ž .8 A community cheats if it ever cheated when no complaints were made.

We assume that the agents in online markets believe that all other agents and communities have played according to the OCSS in all past plays. We may also assume that they will also adhere to the OCSS in the future plays except those where the agent has actually observed a deviation. Based on the Optimality Principle of Dynamic Programming, we use backward induction to prove the following propositions and therefore obtain the theorem showing conditions under which the OCSS is a subgame perfect equilibrium strategy. In other words, from the proof we want to show that the OCSS would be a SGPE if agents in online markets had the free choice in abiding by it, so the strategy is in fact self-enforcing.

In the following, we define as the discount factor, i.e., $\delta = ( 1 / ( 1 + i ) )$ with i being the interest rate, and we assume $0 < \delta < 1$ . The following propositions give the conditions under which the agents will play according to the desired actions described in the OCSS.

Lemma. When a cheated community does not sanction a cheating community that refused to pay compensation, the dominant strategy for other communities when interacting with this community is to cheat.

Proof. When a cheated community does not sanction, then the cheating community has two choices in future transactions: honest or cheat. If it plays honest, its total payoff $\varPi _ { \mathrm { h } }$ relative to the cheated community in future periods is $\begin{array} { r } { \varPi _ { \mathrm { h } } = \sum _ { n } \sum _ { t = 1 } ^ { \infty } \delta ^ { t } \pi _ { t } } \end{array}$ . If it plays cheat, its total payoff in future periods is instead $\begin{array} { r } { \varPi _ { \mathrm { c } } = \sum _ { n } \sum _ { t = 1 } ^ { \infty } \delta ^ { t } ( 1 + g ) \pi _ { t } } \end{array}$ . Obviously, $\pi _ { \mathrm { c } } >$ $\varPi _ { \mathrm { h } }$ . Therefore, once a community cheats, if no sanction is imposed by the cheated community, the cheating community will always cheat in the future. I

Proposition 1. Under the assumption that the trading behaÕior of other communities is not affected, a community that has been refused compensation when cheated will always call for sanction on the cheating community.

Proof. If the cheated community calls for sanction on the cheating community, the total payoff for this period and the future periods will be 0. If no sanction is executed, however, the other community will cheat again in the future. Then the total payoff for the cheated community relative to the cheating community is:

$$
\Pi = \sum_ {n} \sum_ {t = 0} ^ {\infty} \delta^ {t} (- l \pi_ {t}) = - l \sum_ {n} \sum_ {t = 0} ^ {\infty} \delta^ {t} \pi_ {t}
$$

which is smaller than 0. Therefore, the optimal strategy for the cheated community is to always sanction the cheating community when compensation is refused. I

Proposition 2. A community whose member has cheated will pay the demanded compensation if the following condition holds:

$$
F <   \sum_ {t = 0} ^ {\infty} \delta^ {t} \Pi_ {t}
$$

where is the community’s total payoff relatiÕe to the cheated community.

Proof. If the cheating community $( C _ { \mathrm { c } } )$ pays the compensation, the other community $( C _ { \mathrm { h } } )$ would not call for sanction. Therefore, the expected future payoff for $C _ { \mathrm { c } }$ relative to the cheated community after paying the compensation is:

$$
\Pi = \sum_ {t = 0} ^ {\infty} \delta^ {t} \Pi_ {t} - F
$$

If $C _ { \mathrm { c } }$ refuses to pay compensation, community $C _ { \mathrm { h } }$ will call for sanction. Then, the expected future payoff for $C _ { \mathrm { c } }$ relative to community $C _ { \mathrm { h } }$ will be 0. Therefore, community $C _ { \mathrm { c } }$ will pay the compensation if $\begin{array} { r } { I I = \sum _ { t = 0 } ^ { \infty } \delta ^ { t } I I _ { t } - \dot { F } > \dot { 0 } } \end{array}$ . That is,

$$
F <   \sum_ {t = 0} ^ {\infty} \delta^ {t} \Pi_ {t}
$$

I

Proposition 3. A cheated agent will complain to his own community if the following condition holds: $F \geq C .$

Proof. If a cheated agent complains to his community, he incurs a personal cost of C, but the expected payoff is F. Therefore, he will complain if and only if $F \geq C .$ I

Proposition 4. An agent who has cheated is willing to pay the compensation if the following condition holds:

$$
F <   (1 - P (a)) \sum_ {t} \delta^ {t} \pi_ {t}
$$

Proof. If the agent cheats and then pays the compensation, he can continue his community membership and other agents will trade with him honestly, under the online community system strategy. Then his expected total payoff for the current period and future periods will be:

$$
(1 + g) \pi - F + \sum_ {t} \delta^ {t} \pi_ {t}
$$

If the agent refuses to pay the compensation, then he will get expelled by his current community. Since his probability of getting accepted by another community is $P ( a )$ , his expected payoff for the current and future periods will be:

$$
(1 + g) \pi + P (a) \sum_ {t} \delta^ {t} \pi_ {t}
$$

So, the agent will pay the compensation if the following condition holds:

$$
(1 + g) \pi - F + \sum_ {t} \delta^ {t} \pi_ {t} > (1 + g) \pi + P (a) \sum_ {t} \delta^ {t} \pi_ {t}
$$

That is, $\begin{array} { r } { F < ( 1 - P ( a ) ) \sum _ { t } \delta ^ { t } \pi _ { t } . } \end{array}$

Proposition 5. An agent who belongs to a reputable community will play honest if and only if $F \ge g \pi$

Proof. We consider two situations: the trading partner plays honest or he plays cheat.

First, when the partner is honest, an agent can play either honest or cheat. If he plays honest, his expected payoff for the current and future periods will be $\pi + \textstyle \sum _ { t } \delta ^ { t } \pi _ { t }$ . If he plays cheat, his payoff will be $( 1 + g ) \pi - F + \Sigma \delta ^ { t } \pi _ { t }$ . Therefore, the equilibrium in which the agent will play honest requires that the following condition hold:

$$
\pi + \sum_ {t} \delta^ {t} \pi_ {t} \geq (1 + g) \pi - F + \sum_ {t} \delta^ {t} \pi_ {t}
$$

That is, $F \geq g \pi$

Second, when the trading partner cheats, again, an agent can choose to play honest or cheat. If he plays honest, his expected payoff for the current and future periods is: $\begin{array} { r } { - l { \boldsymbol { \pi } } + { \boldsymbol { F } } - { \boldsymbol { C } } + \sum _ { t } \delta ^ { t } { \boldsymbol { \pi } } _ { t } } \end{array}$ . If he plays cheat, the payoff instead will be $\begin{array} { r } { 0 - C + \sum _ { t } \delta ^ { t } \pi _ { t } } \end{array}$ . Since $F \geq \pi + l \pi$ , the payoff for playing honest is greater than that for playing cheat. Therefore, even when the trading partner plays cheat, the agent will still be better off to play honest.

In summary, the agent will play honest, regardless of the other agent’s action, if $F \ge g \pi$ I

Theorem. The impersonal exchange between two agents can be sustained as a subgame perfect equilibrium in the online community system game under the following condition:

$$
\begin{array}{l} \operatorname{Max} [ C, g \pi ] \\ \leq F <   \operatorname{Max} \left[ \sum \delta^ {t} \Pi_ {t}, (1 - P (a)) \sum_ {t} \delta^ {t} \pi_ {t} \right] \end{array}
$$

Proof. From Proposition 3, we have $F \geq \mathbf { C }$ . Combining this with the result of Proposition $5 \ ( F \ge g \pi )$ we have $F \ge \mathbf { M a x } [ C , ~ g \pi ]$ From Proposition 4, we have $F < ( 1 - P ( a ) ) \sum _ { t } \delta ^ { t } \pi _ { t }$ the condition under which a cheating agent will pay the demanded compensation F. If the agent does not Žpay that is, when $F > ( 1 - P ( a ) ) \Sigma _ { t } \delta ^ { t } \pi _ { t } )$ , Proposition 2 indicates that his community will pay if $\begin{array} { r } { F < \sum _ { t = 0 } ^ { \infty } \delta ^ { t } \varPi _ { t } . } \end{array}$ Then it follows that if $F <$ $\begin{array} { r } { \mathbf { M a x } [ \sum \delta ^ { t } \mathcal { \bar { \Pi } } _ { t } , ( \mathrm { i } - P ( a ) ) \sum _ { t } \delta ^ { t } \pi _ { t } ] , } \end{array}$ , at least one of the party either the cheating member or the cheating Ž member’s community will pay the demanded com-. pensation.

Based on the Optimality Principle of Dynamic Programming, we know that there is no situation in which a one-time deviation from the Online Community System Strategy is profitable provided the above condition is satisfied. Therefore, we have proved that the OCSS is a subgame perfect equilibrium strategy of the online community system stage game if the above condition holds. I

## 5. Sustainability of the community system

The online community system strategy requires that the community pay the cheated community the demanded compensation if the cheating member refuses to pay and leaves the community. Then the question that naturally arises is: how sustainable is the community system? In this section, we derive the conditions under which the community is sustainable and analyze how the size of the community is related to its sustainability.

As mentioned earlier, for each transaction associated with a community member, the community takes a fee of $\tau \pi$ , where $0 < \tau < 1$ . For a community of size $N ,$ suppose the probability of a member cheating and leaving the community in one time period that is, the member plays the last move of aŽ repeated game is. $P ( \mathrm { c } )$ . Then on average $N P ( { \mathrm { c } } )$ members will cheat and the community will have to pay compensation in a total number of $N P ( { \mathrm { c } } ) F .$ . The income from the transaction fees is $( \tau \varPi _ { \mathrm { t o t } } ) / ( 1 - \tau )$ where $\scriptstyle { \cal I } _ { \mathrm { t o t } }$ is the community’s total payoff in the current period from all of its members’ trading with all other communities. For the community to be sustainable, the following condition has to be satisfied:

$$
N P (\mathsf {c}) F <   \frac {\tau \Pi_ {\mathrm{tot}}}{1 - \tau}
$$

In other words, $\varPi _ { \mathrm { t o t } } = N \overline { { \pi } }$ where $\overline { { \pi } }$ is the average payoff of the community members’ trading. Therefore, we have the following condition

$$
\tau > \frac {P (\mathrm{c}) F}{P (\mathrm{c}) F + \overline {{\pi}}}
$$

for the communities to be sustainable.

In addition, for any given one period, for the community to maintain a positive cash flow, the following has to be satisfied:

$$
\frac {\tau \Pi}{1 - \tau} \geq F N _ {\mathrm{c}}
$$

where $N _ { \mathrm { c } }$ is the number of members who cheated.

We define by $\beta$ the maximum proportion of members that can cheat such that the community does not make a loss in the period. Then we have:

$$
\frac {\tau \Pi}{1 - \tau} = F \beta N, \quad \beta = \frac {\tau \overline {{\pi}}}{(1 - \tau) F}
$$

Assuming people cheat independently, each with a probability of $P ( \mathrm { c } )$ , then the probability that exactly k out of N people cheat is given by a binomial distribution. Then, the probability $P _ { N }$ that at least $\beta N$ out of N people cheat is:

$$
P _ {N} = \sum_ {k = \beta N} ^ {N} \binom {N} {k} P (c) ^ {k} (1 - P (c)) ^ {N - k}
$$

When N is sufficiently large, we can use the normal approximation with mean $P ( \mathrm { c } )$ and variance $[ P ( \mathrm { c } ) ( 1 - P ( \mathrm { c } ) ) ] / N$ to find the probability that at least a proportion $\boldsymbol { \cdot } \beta$ people cheat. And since $\beta >$ $P ( \mathrm { c } )$ , we have that

$$
P _ {N _ {1}} <   P _ {N _ {2}} \text {   for   } N _ {1} > N _ {2}
$$

That is, a bigger community has less probability of going bankrupt since in each period the probability of negative cash flow is less than that for a small community.

## 6. Conclusion

The formal game theory analysis in this paper indicates that impersonal, market exchange can be supported if each member of the society is a member of a community that can establish intra-community contract enforcement and the individuals’ community affiliation can be easily checked. Transferencebased trust building process tells us that if an individual trusts a community, then it is possible for the individual to trust the members of the community, with the understanding that the community will take disciplinary actions against its members when cheating behaviors occur. Therefore, online communities could potentially be an effective way of building trust.

The beauty of this system is that it can take advantage of the existing online community structure and culture and the repeated nature of the interactions among members of a community to support inter-community impersonal exchange. The reputation of the community plays an important role in supporting the exchange.

The proposed online community system has the following differences compared to currently available trust promoting systems. First, the reputation necessary for trust building lies with the community, not with individual agents, ensuring continuity of the trust building process. Second, although each individual agent has a limited life span and limited number of transactions, the community as a whole carries on, making transactions from a particular community infinitely repeated. Consequently, the reputation system for trust building becomes effective again at the community level, instead of the individual level. Third, communities can be organized to reflect different levels of trust that different transaction value requires. Agents, depending on the type of transactions they engage in, can join different communities that best meet their needs for trust building. Finally, the community-based system does not require that each transacting party know the trading history of all others before the transaction. In other words, it does not require complete information. It enables exchange that is impersonal up to one’s community affiliation. Therefore, it respects agents’ privacy and anonymity. The only identity to reveal in a transaction is one’s community membership.

Using an online community’s reputation to facilitate impersonal transactions already exists in some preliminary forms. For example, CNET.com is a community for computer enthusiasts with a positive reputation. Many merchants small and unknownŽ . sell their products through CNET. One of the incentives of associating themselves with CNET is the belief that consumers will transfer their trust towards CNET to them and be more willing to engage in purchasing transactions. More and more communities and merchants are adopting this model. What is currently missing is the intra-community enforcement of honest behavior e.g., disciplinary actionsŽ towards dishonest members as well as inter-com-. munity retaliation e.g., when a community fails toŽ discipline cheating members and compensating cheated, other communities retaliate by boycotting transactions with all members of that community .. As online communities develop, they have the potential of becoming a strong social structure that promotes trust building and facilitates the growth of electronic commerce.

Several issues are left open in this paper but need to be investigated in future research. For example, what is the best control structure of an online community? How does the control structure of a community impact agents’ trust towards the community? What are the dynamics of online communities: how do they get created? How do they evolve over time? Furthermore, what are the attributes that make a community successful? While these issues are important to the success of the community system as a social structure to support impersonal online transactions, we believe that the work presented in this paper is the necessary first step towards such a direction.

## References

<sup>w</sup> <sup>x</sup>1 A. Achian, H. Demsetz, Production, information costs, and economic organization, American Economic Review 62 5Ž . Ž .1972 777–795.

<sup>w</sup> <sup>x</sup> 2 G. Akerlof, The Market for ‘Lemons’: Quality Under Uncertainty and the Market Mechanism, Quarterly Journal of Economics 84 1970 488–500, August.Ž .

<sup>w</sup> <sup>x</sup> 3 A. Argandona, Sharing out alliances: trust and ethics, Journal of Business Ethics 21 1999 217–228.Ž .

<sup>w</sup> <sup>x</sup> 4 K. Arrow, The limits of organization, W.W. Norton, NewYork, 1974.

<sup>w</sup> <sup>x</sup> 5 S. Ba, H. Zhang, A.B. Whinston, Building trust in the electronic market using an economic incentive mechanism, Proceedings of the 1999 International Conference on Information Systems. Charlotte, NC. December 12–15, Atlanta Omnipress, 1999.

<sup>w</sup> <sup>x</sup> 6 E. Brynjolfsson, M. Smith, Frictionless Commerce? A Comparison of Internet and Conventional Retailers, Management Science 46 4 2000 563–585.Ž . Ž .

7 M. Culnan, P.K. Armstrong, Information privacy concerns, procedural fairness, and impersonal trust: An empirical investigation, Organization Science 1999 104–115, JanŽ . <sup>r</sup>Feb.

<sup>w</sup> <sup>x</sup> 8 L. Downes, C. Mui, Unleashing the Killer App, Harvard Business School Press, Boston, 1998.

<sup>w</sup> <sup>x</sup> 9 R. Fung, M. Lee, EC-Trust Trust in Electronic Commerce :Ž . Exploring the Antecedent Factors,Proceedings of the 5th Americas Conference on Information Systems, AIS Publishing, Atlanta, 1999, pp. 517–519.

<sup>w</sup> <sup>x</sup> 10 A. Greif, On the social foundations and historical development of institutions that facilitate impersonal exchange: from the community responsibility system to individual legal responsibility in pre-modern Europe. Working paper, Department of Economics, Stanford University, 1997.

<sup>w</sup> <sup>x</sup> 11 J. Hagel, A. Armstrong, Net Gain, Harvard Business School Press, Boston, 1997.

<sup>w</sup> <sup>x</sup> 12 S.R. Hiltz, B. Wellman, Asynchronous learning networks as a virtual classroom, Communications of the ACM 40 9Ž . Ž . 1997 44–49.

<sup>w</sup> <sup>x</sup> 13 F. Hirsch, Social Limits to Growth, Harvard University Press, Cambridge, MA, 1978.

<sup>w</sup> <sup>x</sup> 14 J.G. Holmes, Trust and the appraisal process in close relationships, in: W.H. Jones, D. Perlman Eds. , Advances inŽ . Personal Relationships 2, Jessica Kingsley, London, 1991, pp. 57–104.

<sup>w</sup> <sup>x</sup> 15 Internet Fraud Watch: 1999 Internet Fraud Statistics. http:<sup>rr</sup>www.fraud.org<sup>r</sup>internet<sup>r</sup>99final.htm. 2000.

<sup>w</sup> <sup>x</sup> 16 S.L. Jarvenpaa, N. Tractinsky, M. Vitale, Consumer trust in internet stores, Information Technology and Management 1 Ž . Ž .1–2 2000 .

<sup>w</sup> <sup>x</sup> 17 P. Kollock, The production of trust in online markets, in: E.J. Lawler, M. Macy, S. Thyne, H.A. Walker Eds. , AdvancesŽ . in Group Processes vol. 16, JAI Press, Greenwich, CT, 1999.

<sup>w</sup> <sup>x</sup> 18 R.J. Lewicki, B. Bunker, Trust in relationships: a model of trust development and decline, in: B. Bunker, J. Rubin Ž . Eds. , Conflict, Cooperation and Justice, Jossey-Bass, San Francisco, 1995, pp. 133–173.

<sup>w</sup> <sup>x</sup> 19 W.G. Ouchi, Market, Bureaucracies, and Clans, Administrative Science Quarterly 25 1980 129–141.Ž .

<sup>w</sup> <sup>x</sup> 20 W.W. Powell, Neither market nor hierarchy: network forms of organization, Research in Organizational Behavior 12 Ž .1990 295–336.

<sup>w</sup> <sup>x</sup> 21 R.P. Ramsey, R.S. Sohi, Listening to your customers: the impact of perceived salesperson listening behavior on relationship outcomes, Journal of the Academy of marketing Science 25 1997 127–137.Ž .

<sup>w</sup> <sup>x</sup> 22 J.K. Rempel, J.G. Hotmes, M.P. Zanna, Trust in close relationships, Journal of Personality and Social Psychology 45 Ž . Ž .1 1985 95–112.

<sup>w</sup> <sup>x</sup> 23 P.S. Ring, A.H. Van de Ven, Structuring cooperative relationships between organizations, Strategic Management Journal 13 1992 483–498.Ž .

<sup>w</sup> <sup>x</sup> 24 J.B. Rotter, Generalized expectancies for interpersonal trust, American Psychologist 26 1971 443–452.Ž .

<sup>w</sup> <sup>x</sup> 25 D. Shapiro, B.H. Sheppard, L. Cheraskin, Business as handshake, Negotiation Journal 8 4 1992 365–377.Ž . Ž .

<sup>w</sup> <sup>x</sup> 26 Uzzi, The sources and consequences of embeddedness for the economic performance of organizations: the network effect, American Sociological Review 61 1996 674–698.Ž .

<sup>w</sup> <sup>x</sup> 27 E. Walden, Some value propositions of online communities, Electronic Markets 4 4 2000 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 A. Zaheer, B. McEvily, V. Perrone, Does trust matter? Exploring the effects of interorganizational and interpersonal trust on performance, Organization Science 9 2 1998Ž . Ž . 141–159.

![](/api/attachments/ET9PFTFP/fulltext/images/4397523d2b758a798c54ac3901aac11cf4d6edd5fc4193fdaf0c05483f46ef18.jpg)

Sulin Ba is assistant professor of information systems and the co-Director of the Electronic Economy Research Program ebizlab at the Marshall School ofŽ . Business at the University of Southern California. She received her PhD from the University of Texas at Austin. Her research interests include electronic commerce, knowledge management, and virtual teams. Her current projects involve the design of trusted third parties to help small business overcome the on-

line barriers such as security and product quality uncertainty. Her work on the institutional setup to help small business survive and grow in the digital economy has been used as the basis for testimony before the House Committee on Small Business. In addition, she works on designing new market-oriented organizational coordination mechanisms. She serves as Associate Editor for the Journal of Decision Support Systems.
