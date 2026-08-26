---
otero_id: 12400
otero_key: "WHG2TDEV"
title: "Governance in the Blockchain Economy: A Framework and Research Agenda"
authors: "Roman Beck; Christoph Müller-Bloch; John Leslie King"
year: "2018"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00518"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Governance in the Blockchain Economy: A Framework and Research Agenda

Roman Beck<sup>1</sup>, Christoph Müller-Bloch<sup>2</sup>, John Leslie King<sup>3</sup>

<sup>1</sup>IT University of Copenhagen, Denmark, beck@itu.dk <sup>2</sup> IT University of Copenhagen, Denmark, chmy@itu.dk <sup>3</sup>University of Michigan, U.S.A., jlking@umich.edu

## Abstract

Blockchain technology is often referred to as a groundbreaking innovation and the harbinger of a new economic era. Blockchains may be capable of engendering a new type of economic system: the blockchain economy. In the blockchain economy, agreed-upon transactions would be enforced autonomously, following rules defined by smart contracts. The blockchain economy would manifest itself in a new form of organizational design—decentralized autonomous organizations (DAO)—which are organizations with governance rules specified in the blockchain. We discuss the blockchain economy along dimensions defined in the IT governance literature: decision rights, accountability, and incentives. Our case study of a DAO illustrates that governance in the blockchain economy may depart radically from established notions of governance. Using the three governance dimensions, we propose a novel IT governance framework and a research agenda for governance in the blockchain economy. We challenge common assumptions in the blockchain discourse, and propose promising information systems research related to these assumptions.

Keywords: Blockchain, Distributed Ledger Technology, Smart Contracts, Decentralized Autonomous Organization, Governance, Agency Theory, Decision Rights, Accountability, Incentives.

Jason Thatcher was the accepting senior editor. This research article was submitted on June 9, 2017 and went through two revisions.

## 1 Introduction

This paper is devoted to a discussion of some important elements characterizing a blockchain-based economic system that we call the “blockchain economy.” The blockchain economy may fundamentally change our understanding of governance. Therefore, we explore the case of an emerging blockchain-based organization—a “decentralized autonomous organization” (DAO)— for the purpose of exploring decision rights, accountability, and incentives related to governance (Weill, 2004). Building on Weill’s work, we provide a novel IT governance framework and a research agenda in order to examine changes to governance that may accompany the emergence of the blockchain economy. While a recent paper suggests a practical research agenda for studying blockchain (Risius & Spohrer, 2017), our efforts here will focus on theorizing in information systems (IS) research and on challenging implicit assumptions apparent in the blockchain discourse. Our work sheds light on some “dark” issues of blockchain, and identifies important avenues for research concerning governance in the blockchain economy.

Blockchain can be described as a decentralized, transactional database technology that facilitates validated, tamper-resistant transactions that are consistent across a large number of network participants called nodes (Glaser, 2017). Blockchain can be characterized as a class of technologies (sometimes called distributed ledger technologies) that give users confidence that archived information (e.g., a certificate) has not been tampered with. In principle, this guarantees a “single truth” across different agents who may or may not trust each other. As such, it is not surprising that financial services has been one of the first industries to express an interest in blockchain (Beck & Müller-Bloch, 2017; Walsh et al., 2016). For centuries, the financial industry has relied on double-entry bookkeeping as a trustworthy method of determining “who owns what” and “who owes whom.” In addition to financial services, however, blockchain technology has also been explored in other industries—for instance, as a means of reducing uncertainty in supply chains (Nærland, Müller-Bloch, Beck, & Palmund, 2017), fostering environmental sustainability (Chapron, 2017), and preventing fraudulent tax returns (Hyvärinen, Risius, & Friis, 2017).

Recently, academia has also expressed interest in blockchain (Beck, Avital, Rossi, & Thatcher, 2017; Tapscott & Tapscott, 2016). Thus far, most academic research has focused on cryptocurrencies like Bitcoin (e.g., Böhme, Christin, Edelman, & Moore, 2015; Kazan, Tan, & Lim, 2015; Li & Wang, 2017; Nakamoto, 2008); however, at this point, blockchain has evolved beyond Bitcoin. The release of the freely programmable Ethereum blockchain in 2014 enabled smart contracts, software code that runs exactly as programmed without risk of downtime, censorship, or fraud (Buterin, 2014). Smart contracts facilitate many different kinds of transactions, going far beyond simple cryptocurrency transfer.

Little is known about the implications of blockchain for the governance of economic activities. Blockchain and the smart contracts it enables could give rise to a new type of economic system, which we refer to here as the blockchain economy. While the digital economy, where “goods and services traded are in digital format” (Kim, Barua, & Whinston, 2002), has become omnipresent (Bharadwaj, El Sawy, Pavlou, & Venkatraman, 2013), the blockchain economy extends beyond the digital economy, in that blockchain makes it possible for agreed-upon transactions to be autonomously enforced, following rules defined in smart contracts. The blockchain economy could enable new organizational designs in the form of DAOs—autonomous entities using governance rules that conform to the business logic of the blockchain (Jentzsch, n.d.)—challenging established notions of governance. In the following sections, we provide a research framework and agenda for governance for the blockchain economy by comparing the blockchain economy to the digital economy.

## 2 Literature Background

For the purposes of this analysis, we consider blockchain to be a foundational technology for the blockchain economy. The theoretical foundations for this paper are drawn from the relevant IT governance literature. In this section we discuss the foundations of blockchain technology, introduce the idea of the blockchain economy, and discuss the issue of governance.

## 2.1 Blockchain Foundations

While it is not possible to predict the future of blockchain, at this point it is widely assumed that it is destined to become a highly important technology. Some researchers describe it as being as important as the Internet, due to its potential attendant impacts on business and society (e.g., Beck, 2018). Research suggests that blockchain has the capacity to reduce uncertainty, insecurity, and ambiguity in transactions by providing full transactional disclosure and by producing a single truth for all network participants (Beck, Czepluch, Lollike, & Malone, 2016; Nærland et al., 2017).

Technically, a blockchain is a tamper-resistant, decentralized database of transactions consistent across a base of decentralized nodes (Glaser, 2017). It is cryptographically armored against retrospective manipulations, and uses a consensus mechanism to encourage database consistency whenever new transactions are validated. All transactions saved on the blockchain are stored in blocks; transaction data are stored within the blocks in a cryptographic data structure, the most common of these being Merkle trees. In Merkle trees, transactions are hashed and repeatedly paired, merged, and rehashed until only one hash remains, the Merkle root. Each block saves the Merkle root of the previous block. This creates a chain of data that is cryptographically secured and linked. Any retrospective attempt to change a transaction necessitates rehashing not only the block that contains the transaction, but all subsequent blocks as well. While this is theoretically possible, it is highly implausible, since other nodes are constantly adding new blocks to the ever-expanding blockchain (Underwood, 2016). Consensus mechanisms encourage the nodes to validate new transactions and discourage them from creating alternative histories of transactions. These consensus mechanisms often employ economic incentives to keep the database consistent. The most common consensus mechanisms are proof-of-work and proof-of-stake. Proof-of-work requires solving a computationally expensive cryptographic puzzle. The node that first finds the solution to the puzzle validates the next block, and is remunerated with cryptocurrency. Proof-of-stake gives nodes with more cryptocurrency (larger stakes) higher probabilities of being chosen to validate the next block. The stake may be destroyed if the node behaves maliciously, which thus discourages such behavior (see also Tschorsch & Scheuermann, 2016).

The ability to read blockchain data and submit new transactions is determined by access to transactions. Public blockchains allow all nodes to read blockchain data and propose new transactions, whereas private blockchains allow only nodes that are preregistered by a central authority to read blockchain data and submit new transactions (see Table 1). Public blockchains offer either permissioned or permissionless access to transaction validation. In permissionless blockchains, all nodes can validate transactions, while in permissioned blockchains, only nodes that have been preregistered can validate transactions (Peters & Panayi, 2016).

Table 1. Blockchain Typology

<table><tr><td>Access to transactions</td><td colspan="2">Access to transaction validation</td></tr><tr><td></td><td>Permissioned</td><td>Permissionless</td></tr><tr><td>Public</td><td>All nodes can read and submit transactions. Only authorized nodes can validate transactions.</td><td>All nodes can read, submit, and validate transactions.</td></tr><tr><td>Private</td><td>Only authorized nodes can read, submit, and validate transactions.</td><td>Not applicable</td></tr></table>

## 2.2 The Blockchain Economy

While the first blockchain enabled only the transfer of digital tokens—in this case, the cryptocurrency Bitcoin—and was not used for other, more sophisticated transactions, the launch of Ethereum demonstrated that it was possible to program blockchains to support many kinds of transactional logics through smart contracts that execute precoded pieces of software on the blockchain when specific conditions are met (Buterin, 2014). Smart contracts can execute transactions autonomously, without interference from agents or the need for approval from third parties. They can be embedded into digital assets or into the digital representation of physical assets in the form of tokens that enforce autonomous contract fulfillment (Szabo, 1994). The blockchain ensures that contracts are fulfilled and not corrupted. For example, a smart contract could (theoretically) be used to autonomously and remotely lock a leased car if the owner failed to fulfill leasing obligations.

For our purposes, we presume that smart contracts will precipitate the blockchain economy, a new type of economic system where agreed-upon transactions can be enforced autonomously according to rules defined in the contracts. The blockchain economy could potentially manifest itself in machine-tomachine coordination within the Internet of Things (e.g., Christidis & Devetsikiotis, 2016; Zhang & Wen, 2017) or the creation of decentralized electronic marketplaces (e.g., Subramanian, 2018; Wörner, von Bomhard, Schreier, & Bilgeri, 2016). The blockchain economy idea is based on a new kind of governance, which would likely manifest itself in a new form of organizations called DAOs, in which governance would radically depart from the way organizations are commonly governed today (e.g., Swan, 2015; Wright & De Filippi, 2015).

## 2.3 Governance

We use the theoretical perspective of IT governance, which has been a topic of interest for several decades (see Brown & Grant, 2005, for an overview). According to Weill (2004, p. 3), “IT governance represents the framework for decision rights and accountabilities to encourage desirable behavior in the use of IT.” Weill’s definition invokes three key dimensions of IT governance: decision rights, accountability, and incentives.

Decision rights concern the rights governing control over certain assets. Fama and Jensen (1983) describe two types of decision rights. Decision management rights make it possible to generate decision proposals and execute or implement decisions. Decision control rights concern decision ratification (deciding whether to implement decisions) and address how decisions are monitored (measuring performance of decision agents). Decision rights, in general, determine the degree of centralization; that is, whether decisionmaking power is concentrated in a single person or small group (centralized), or dispersed (decentralized) (King, 1983; Sambamurthy & Zmud, 1999).

The right to monitor decisions is linked to accountability. To be called “to account” for one’s actions is the core sense of this (Mulgan, 2000), but is only one part of an accountability relationship. Accountable agents must address actions taken and consequences incurred. Enforcement mechanisms are crucial (Burritt & Welch, 1997); decision management rights are often separated from decision control rights to avoid self-monitoring, self-reward, and self-punishment (Moldoveanu & Martin, 2001). Accountability is enacted, specified and enforced through contracts and legal frameworks governed by institutions, but it can also be enacted through IT infrastructures (Weitzner et al., 2008)—an important consideration for blockchain.

While incentives have been recognized as central to IS design (Ba, Stallaert, & Whinston, 2001), they are underemphasized in Weill’s discussion. Incentives motivate agents to act. Jensen and Meckling (1976) address two types of incentives: pecuniary incentives relate observable agent behavior to monetary rewards (or rewards that can be monetized); nonpecuniary incentives relate observable agent behavior to nonmonetary rewards—such as privileges, visibility, or reputation. Incentive alignment occurs “when the system’s embedded features induce users to employ the system consistent with the design objective” (Ba, Stallaert, & Whinston, 2001, p. 227). A system with aligned incentives allows agents to freely choose their own behaviors, but uses incentives to make them inclined to choose actions that coincide with goals of the system’s design.

These governance dimensions are anchored in agency theory or principal-agent theory (Moldoveanu & Martin, 2001), according to which one party (the principal) delegates work to another party (the agent). The objective is to resolve problems in cases where principals and agents have conflicting desires, goals, or attitudes toward risk (Akerlof, 1970; Eisenhardt, 1989; Jensen & Meckling, 1976). Agency theory can be used as a lens to view the allocation of decision rights, to determine how parties are to be held accountable, and to examine how incentives can be used to overcome diverging goals (Fama & Jensen, 1983). While these theoretical perspectives are common to both economics and political science, our analysis proceeds primarily from an economics perspective.

## 3 The Swarm City Case

Our practical exploration of governance issues is based on our analysis of the Swarm City blockchain case. Swarm City<sup>1</sup> was founded in 2017 as a loosely coupled network of software engineers working on the development of an Ethereum-based blockchain infrastructure to empower sharing economy applications. Swarm City developed out of its predecessor, Arcade City, and seeks to disrupt today’s sharing economy platforms that act as central authorities, aiming to replace these platforms by facilitating direct peer-to-peer transactions. In today’s sharing economy, platform owners are remunerated, typically through a transaction fee. Their business models have been criticized for exploitative labor practices, and strong network effects have transformed some sharing economy platforms into quasimonopolistic organizations that capture monopoly rents (The Economist, 2014). These quasi-monopolies are a concern for regulators and politicians alike.

Swarm City’s goal is to provide a blockchain infrastructure for the sharing economy that facilitates building disintermediated sharing economy applications. Developers will be able to customize the design of sharing economy applications by choosing application areas (e.g., ride sharing) or by defining governance rules (e.g., whether or not transaction fees are charged). Swarm City envisions developing a market for blockchain-based sharing economy applications, where different applications compete with each other. As such, Swarm City serves as an example of how blockchain might engender the blockchain economy and challenges our understanding of IT governance.

Since Swarm City does not offer a well-defined company or location where we could conduct interviews or harvest secondary data, our data collection followed an unconventional approach. Our collected data include the original Arcade City white paper, as well as posts from the Swarm City blog (press.swarm.city).

We also conducted five interviews with Swarm City developers between December 2016 and February 2017, and three additional interviews in February 2018. Each interview was open-ended and semistructured, lasting 40–90 minutes, with an average duration of slightly over 60 minutes. Data sampling aligned with preconceptions about challenges in blockchain governance, but was open, in order to allow for new theoretical insights (Urquhart, Lehmann, & Myers, 2010). In all, our data includes over 110 pages of interview transcriptions and over 230 pages of secondary data (see Table 2).

Table 2. Data Collection

<table><tr><td>Type of Data</td><td>Number of Pages</td></tr><tr><td>Interviews (8 interviews with 8 individuals associated with Swarm City: business leader, principal cofounder, cofounder, system architect, software engineer, liaison officer, communication officer, member of advisory board)</td><td>111</td></tr><tr><td>Swarm City blog posts (49 blog posts from press.swarm.city)</td><td>215</td></tr><tr><td>Arcade City (predecessor of Swarm City) white paper</td><td>17</td></tr><tr><td>Total</td><td>343</td></tr></table>

Our study was inspired by Mingers’ (2004) recommendation of pragmatics. We formulated the problem (Van de Ven, 2007), designed the case study (Yin, 2000), and completed the data collection and analysis. This led to theoretical insights using a pluralistic strategy (Mingers, 2001). We embraced different research perspectives to construct “a useful model of reality” (Van de Ven, 2007), and followed the principle of emergence from grounded theory (Glaser & Strauss, 2008). By employing such techniques we increased theoretical scope and conceptualization, treating literature about governance as additional data points for analysis (Urquhart et al., 2010). Our background of blockchain workshops, panels, and events also informed the work.

## 3.1 Decision Rights

The ownership of Swarm City—in contrast to traditional sharing economy platforms such as Airbnb or Uber—is ostensibly organized in a decentralized fashion. However, the nature of this ownership is limited to decision rights and does not include additional property rights, since anyone can copy the code that instantiates Swarm City and use it. According to a Swarm City business leader: “There is no real ownership. . . . Anyone who wants to copy the code and use it to create their own project can.”

Swarm City developers intend to make the code (and the application itself) increasingly decentralized and autonomous once it is implemented. However, in its current stage of development, decision rights are highly centralized in what Swarm City developers consider a necessary “benevolent dictatorship.” They say initial centralization is a prerequisite for later decentralization. As a system architect explained:

You might say that the initial governance structure is something like a dictatorship. . . . We do it this way because we believe that to build [Swarm City] as a tool, you [need] to do it in a military style. . . .Of course, we are trying to build a totally decentralized open platform that is open source and that anyone can use and add value to. But in order to make the tools, we initially need a really hierarchical governance.

However, the Swarm City development team does plan to relinquish control once initial development is complete. As a business leader explained:

Our goal is to go from centralized governance to decentralized governance over a period of time. That’s something that is totally on our roadmap . . . , for [us who] are planning on becoming obsolete so we don’t . . . have this kind of control, this kind of decision-making power for eternity in Swarm City. The aim would be for everyone using Swarm City . . . to have a decentralized way of managing it.

Swarm City developers did express some concern about the allocation of decision rights. In the future, token owners might make joint management decisions (e.g., concerning new features or whether to offer certain services), but this joint decision-making may not always be feasible. Another approach might be to separate decision management rights from decision control rights, like traditional corporations do. As a software engineer clarified:

Owning a number of tokens would allow you to have a voting right in the decision-making of the company and then you would have a board of directors doing the day-to-day management of the company. They would be appointed by these Swarm token holders.

This suggests that some iterations of the blockchain economy might include some centralization. However, Swarm City also suggests tendencies towards a decentralized locus of control. In particular, users offering services via Swarm City would be able to determine their pricing without inference from a third party. As a business leader explained:

Uber always says how much I can earn per kilometer, per ride. So it’s not really something I can decide. . . . We think that whoever owns the item or the skill [they offer], should decide how much they want to ask for it and then see how the market responds.

However, decisions will likely be disputed from time to time, so it is important to consider how to resolve disagreements in decision-making. Swarm City exemplifies one such resolution possibility, albeit a quite drastic one. When the individuals who became Swarm City disagreed with decisions made by the managing individuals of their predecessor, Arcade City, they “forked off,” or split, from Arcade City by copying the code and setting up an alternative, competing project. In the words of one of the Swarm City cofounders: “Arcade City’s still running, but we forked off into a separate organization, ‘cause we had a certain way of wanting to do things.’”

## 3.2 Accountability

Swarm City may delegate legal risks and obligations to network participants. Our findings indicate that the claims that blockchain will entirely eliminate institutional engagement are exaggerated, since compliance with legal institutions will continue to be necessary in the blockchain economy. However, Swarm City neither assumes liability for the transactions it hosts nor does it compel its users to comply with legal regulations, since it perceives itself as merely facilitating peer-to-peer transactions. According to a software engineer:

I think that people who offer any kind of peer-to-peer service, like ride sharing, in their local area, should comply with the local regulations. . . . But it is up to the people who deliver the service to comply with those rules. . . . We are not intermediaries, we just offer a platform and in the end [we are just enabling] a transaction on the blockchain, a peer-to-peer transaction, and we are not involved in that.

Swarm City users may assume some legal liability for engaging in economic exchange, but mitigation mechanisms such as escrow and dispute-resolution assistance would be built into the system. Escrow could be held by a smart contract, but fulfilment of contract conditions (causing the escrow funds to be released) would not be autonomously determinable if transactions were bound to conditions the transacting parties must agree to after the fact. In such cases dispute resolution mechanisms would be necessary, but implementing such mechanisms in smart contracts would be difficult, if not impossible. Therefore, institutional engagement would perhaps be necessary to resolve certain conflicts. As the Swarm City liaison officer explains:

Both [contractual] parties have money in a smart contract once they engage in a . . . transaction; [for instance], ride sharing. The driver and the rider both have money in the contract, and in the end it has to be released. So if one of the parties is not satisfied or has a dispute, then . . . there will be another service like “dispute resolution” . . . in the ecosystem. So dispute resolution will involve another smart contract that gets triggered and there will be a person that steps in to resolve that problem.

In Swarm City, identity is granted to users based on their public address in the blockchain network. The user needs this identity to engage in transactions. However, a user can also choose to use several public addresses. Moreover, the user can decide to remain pseudonymous. Swarm City tries to encourage users to identify themselves by tying all public addresses to reputation scores transferred across all sharing economy applications within Swarm City. This would make it easy for users to switch to new applications, and could be implemented fully on blockchain without institutional engagement. As a business leader explains: “You can earn reputation by riding, you can earn reputation by hosting something or lending something, by renting out your apartment and so forth. This gives you more of a realistic view of the person.”

## 3.3 Incentives

Swarm City’s objectives are to cut fees and redistribute to users the value currently captured by incumbent owners of sharing economy platforms. Swarm City seeks to remove the intermediaries currently responsible for creating and governing sharing economy markets by transferring transactions and governance to blockchain in the context of a peer-to-peer economy. As the liaison officer states:

The big difference with what we are building and what blockchain can offer and how we want to bring blockchain to the people is that . . . almost all the value that you [create] stays with you. So if I rent out a room in my house I [create] tha value, if I rent it to you I want that value to stay with me. So [there is] no central party that is going to come in and claim a percentage of it.

It is hoped that lower transaction fees will incentivize the use of Swarm City. There will also be behaviorinfluencing incentives; for example, offering Swarm City users the opportunity to build a reputation that can be transferred across platforms. As a cofounder explains:

The ones with the really good reputations, people will be inclined to trust them more, but the people with lower reputations will be more inclined to offer less expensive services and do their best to build their reputations, because if they don’t, then they won’t make any money, and then what’s the point of them being there.

Swarm City’s core development team intends to implement a fee system to reimburse those who maintain the Swarm City infrastructure, thus creating an incentive for developers to propose new features. According to the liaison officer:

There will be a small fee, but we are talking about one percent maximum, to sustain the platform. If there are some things that need to be sustained, if bugs show up or something like that, that will need to be fixed. . . . We would like it to be more like a cooperative platform and not like [a platform] where all money goes to one central place and is dispersed from there.

Swarm City developers also derived benefits from issuing their own cryptocurrency. The proceeds from the issuance were used to finance the development of Swarm City. In the future, this cryptocurrency might be used to pay for transactions in Swarm City and might also come with voting rights or participation in decision-making. At present, the main motivation for developing Swarm City is ideological—to drive societal change. A blog post dated June 2, 2017 states: “Now is the time to change society. We all feel it’s up to us to try and become the change we want to see in this world.”

For creators of the individual sharing economy applications run by the Swarm City infrastructure, there is a monetary incentive to set up club goods, since they can embed a transaction fee in their application. Club goods are typically cocreated and used by members and not owned by a single party. However, due to the competition of sharing economy applications, it is hoped that applications with minimal transaction fees will emerge, turning these applications into de facto nonexcludable goods and thus into public goods. Public goods are both nonexcludable and nonrivalrous in nature, which is why there are rarely well-functioning market mechanisms for providing them. Swarm City hopes to change that. As a software engineer explains:

The game-changing thing that I think we are doing is letting . . . everybody create these [sharing economy] storefronts, and letting everyone create their own business models for them. You could even try [to charge] a 30 percent fee like Uber but I imagine that nobody would use that service, because there would be other options with much smaller fees—or no fee at all.

Incentives play a crucial role in blockchain; while incentives represent a key factor for eliciting desirable behavior by those who are developing, maintaining, and using Swarm City, they are also indispensable for ensuring that the underlying blockchain (Ethereum, in the case of Swarm City) functions effectively.

## 4 Future IS Governance Research on Blockchain

In contrast to the digital economy, the blockchain economy challenges established notions of governance. Our research agenda is established to explore governance in the blockchain economy. We conclude by examining common assumptions about governance in the blockchain discourse.

## 4.1 Extended IT Governance Framework

The Swarm City case clearly demonstrates that the emergence of the blockchain economy demands a rethinking of governance. At this early point in development, drawing from limited literature and early-stage case studies, it is not possible to predict how blockchain will evolve. However, we can begin to evaluate how the radical changes foreseen for blockchain might affect governance. By juxtaposing the blockchain economy and the digital economy along the governance areas of decision rights, accountability, and incentives, it is clear that the blockchain economy will change how we view governance (see Table 3). The blockchain economy’s emphasis on decentralizing decision rights and the technical enactment of accountability underscores the importance of incentive alignment. However, as our case study suggests, these changes are fraught with tensions and conflicts, especially concerning what degree of centralization is necessary and how accountability is enacted. We continue here by discussing three governance areas in terms of the blockchain economy using the novel IT governance framework illustrated in Figure 1.

Table 3. Blockchain Economy Governance

<table><tr><td>Dimension</td><td>Property (Range)</td><td>Digital economy</td><td>Blockchain economy</td><td>Selected codes/indicators</td></tr><tr><td>Decision rights</td><td>Degree of centralization (centralized—decentralized)</td><td>The specification of decision rights is a known hierarchically organized contracting process. Implicit and explicit contracts define behavior in organizations.Records are decided upon centrally.Strict property rights prevent forking as a mode of resolving disagreement about decision-making.Transaction parameters are primarily defined centrally.</td><td>The specification of decision rights needs to be organized in a decentralized environment. Implicit and explicit contracts are either not available or are solely managed by blockchain, making technology the foundation of the network, instead of written agreements.Records are decided upon decentrally through consensus.Forking is a novel mode of decentrally resolving disagreement about decision-making.Transaction parameters are primarily defined decentrally.Initial high degrees of centralized decision rights will enable decentralized control later on.</td><td>Benevolent dictatorship (overcoming acute emergency situations, system design) Decentralized decision-making (setting transaction parameters, voting on proposals) Hybrid (centralized decision management rights and decentralized decision control rights) Resolving disagreement about decision-making (forking, voicing disagreement)</td></tr><tr><td>Accountability</td><td>Enactment (institutional – technical)</td><td>Network as “nexus of contracts.”Accountability specified in interpersonal as well as inter- and intraorganizational settings.</td><td>Network as “nexus of smart contracts.”Accountability specified in the network, delegated to and by the blockchain.</td><td>Identity (technical origin, institutional verification, reputation, liability)Transaction enforcement (smart-contract-based escrow, institutional involvement)</td></tr></table>

Table 3. Blockchain Economy Governance

<table><tr><td>Incentives</td><td>Alignment (aligned – unaligned)</td><td>Digital processes in hierarchies for value creation of digital goods.Incentive to create private goods and club goods.</td><td>Digital processes in peer-to-peer exchanges for value creation of blockchain-based digital goods.Incentives to create private goods, club goods, and public goods.New network-based processes which incentivize the peer-to-peer nodes to reach consensus.</td><td>Incentives for technical consensusIncentives for system development and maintenanceIncentives for usersIncentives for token holders</td></tr></table>

![](/api/attachments/XQS854FW/fulltext/images/05f4c1cb615e91fa673142d971a9f358fc1e5064c04f322c439d576f05cfd731.jpg)  
Figure 1. Extended IT Governance Framework

The blockchain literature and our case study suggest that the locus of decision rights in the blockchain economy will be more decentralized than in the digital economy. The nature of consensus-making underlines this development in particular. The locus of making consensus is decentralized, which means that the records that form the foundation of the blockchain economy are not only kept in a decentralized manner, but also decided upon in a decentralized manner. Moreover, disagreements can be resolved in a decentralized manner, for example, if users “fork off,” or split, from the main group by copying existing code and developing it further according to their own goals. Our case study illustrates that beyond consensus-making or forking, concrete models for decentralizing decision rights are still under development. Smart contracts might allow for increasingly decentralized governance mechanisms, but the blockchain economy at present continues to be characterized by a high degree of centralized decision-making. In particular, for effective system design, the concept of the “benevolent dictatorship” continues to be deemed necessary. This illustrates that even though the blockchain economy seeks to shift the focus toward decentralized forms of decision-making, at this point, there is still a high degree of centralization.

In the blockchain economy, accountability will increasingly be enacted technically instead of institutionally, in principle at least. Smart contracts allow for specifying and enforcing accountability. However, in some cases it may not be possible to implement autonomous transaction enforcement; thus, there will inevitably be disputes, and institutional involvement will be necessary to resolve these disputes. A key accountability issue concerns identity in the blockchain environment, ostensibly granted through the public addresses that are used to conduct transactions in the blockchain economy. Given multiple and pseudonymous identities, this could be a problem. While many users will wish to identify themselves using more traditional institutional means (e.g., driver licenses linked to their blockchain identities), a more technical approach to instantiate identity in the blockchain economy would be to link reputation scores to public addresses in the blockchain, as the Swarm City case illustrates. Overall, the shift toward the technical enactment of accountability has only just begun, and we expect that institutions will continue to play important roles for accountability in the blockchain economy for some time to come.

As the blockchain economy emerges, incentive alignment will become increasingly important. While incentives are at the core of all economic activity, including the digital economy, the blockchain economy adds a new dimension. Incentives are absolutely crucial for the blockchain economy to function effectively, because incentives are necessary to achieve the consensus that forms the backbone of the blockchain. Unless incentives are properly aligned, the nodes of the blockchain will not contribute to consensus. Improper incentive alignment could threaten the integrity of the entire blockchain and make the blockchain economy untenable.

## 4.2 Research Agenda for Governance in the Blockchain Economy

The blockchain economy demands a reassessment of established notions of governance. However, how exactly governance will change in the emerging blockchain economy is still little understood. Nevertheless, the promise of the blockchain economy is dependent on the implementation of effective governance mechanisms, which are, in turn, dependent on a thorough understanding of the phenomenon. Table 4 summarizes our research agenda, which serves as fruitful ground for further theoretical work.

Table 4. Research Agenda for Governance in the Blockchain Economy

<table><tr><td>Dimension</td><td>Research questions</td></tr><tr><td>Decision rights</td><td>How are decisions made in the blockchain economy?How are decision management rights and decision control rights allocated?How is disagreement about decision-making resolved in the blockchain economy?What is the role of ownership in the blockchain economy?</td></tr><tr><td>Accountability</td><td>How is accountability determined in the blockchain economy?How is identity engrained in the blockchain economy?How is transaction enforcement embedded in the blockchain economy?How are disputed transactions resolved in the blockchain economy?How is trust affected by the blockchain economy?What is the role of institutions in the blockchain economy?</td></tr><tr><td>Incentives</td><td>How is consensus incentivized in the blockchain economy?How does incentive alignment work in the blockchain economy?How is system use incentivized in the blockchain economy?How is system development and maintenance incentivized in the blockchain economy?How do business models shape the blockchain economy?</td></tr></table>

Future research should investigate how decision rights are allocated in the blockchain economy. As the Swarm City case illustrates, blockchain is subject to instances of both centralized and decentralized decision-making. Further research should analyze when centralized vs. decentralized decision rights are advantageous, and explore the mechanisms of transition from one to the other. Similarly, research is needed to articulate how decision-making works, and who is allowed to decide what kinds of things happen under what circumstances? Are decision management rights and decision control rights held by the same individuals or separated, and how does this affect the effectiveness of decision-making? The separation of decision management rights and decision control rights has already been discussed in Swarm City in the context of professional management agents and token holders who might have voting rights. Resolution of disagreements about decision-making in the blockchain economy also needs research attention. With forking a possibility, research should investigate the role of ownership in the blockchain economy. In traditional organizations owners allocate decision rights; however, in the blockchain economy ownership is not yet fully understood. Future research might analyze how ownership and decision rights are interwoven in the blockchain economy.

Researchers should also address how accountability is determined in the blockchain economy and investigate the role of technical and institutional accountability. The topic of how identity—a crucial dimension of accountability—is handled in the blockchain economy should also be further explored. Identity can be both technically and institutionally enacted in the blockchain economy, but research is needed to better understand the associated limits and trade-offs. Transaction enforcement is also a fertile area for future research. Since transactions that are not autonomously enforced might require institutional involvement, researchers should investigate the boundary conditions of autonomous transaction enforcement in the blockchain economy to determine how best to resolve problems. Another promising area for research is the role of trust. Will trust even be needed anymore? Do individuals trust the technology, expert developers, or the institutions that are still present in the blockchain economy? Institutions are likely to remain important in the blockchain economy, but what will happen when institutions are no longer needed? Will they fight back against the blockchain economy?

Finally, the role of incentives in the blockchain economy should be further explored. Among other things, research is needed to gain a better understanding of how incentives relate to consensus in the blockchain economy. What are the differences between incentive mechanisms such as proof-of-work and proof-of-stake? How does incentive alignment work in a blockchain economy that requires incentives not only for consensus, but also for system development, maintenance, and use? Can incentives be developed concurrently? How might they be interwoven, and how do circumstances of incentive alignment change over time? How do incentives affect system use in the blockchain economy? Do lower transaction fees for users create an incentive for system use? How can incentives be best provided for the development and maintenance of the blockchain economy? What effects do transaction fees, which may be necessary for covering costs, have on a blockchain? If every node in a blockchain system can use the blockchain, how are those who create the blockchain compensated? Can blockchain offer the technological means and the incentives to make the creation of public goods attractive, given that traditional markets are typically not able to do this? Research is needed to investigate new business models for providing public goods, and to explore how developers might predict the needs and incentives of network participants.

## 4.3 A Critical Perspective

The blockchain economy is based on assumptions about several sociotechnical issues that remain open to speculation. The widely heralded blockchain “paradise” calls for a critical stance. IS research can contribute to these problems only if research takes a critical view.

Many promises of the blockchain economy are predicated on technology reducing the coordination costs of economic activities. However, the costs of governance in the one DAO we studied appear to be high in spite of smart contracts. Smart contracts are indefinitely valid, but also entail high risk to the involved parties due to autonomous enforcement mechanisms that could introduce major consequences for coding errors or changes in conditions. The negotiation of smart contracts may be associated with substantial coordination costs to mitigate such concerns. It is too simplistic to say that problems will be handled by smart contracts. Mechanisms must be specified and subjected to serious criticism and testing. While researchers may produce evidence that blockchain would lower coordination costs, they should also study DAO governance negotiating mechanisms, and examine how they are created and maintained. Design-oriented research should create solutions for the risks of smart contracts and propose risk management mechanisms that reduce some of these risks.

While user authentication cultivates accountability, it also invokes privacy concerns. These concerns could eventually be overcome, but if every transaction is visible in terms of the initiator and recipient, a cluster analysis could discern associations between different nodes. Private blockchain keys could be divulged, either intentionally or unintentionally, or attackers could eavesdrop on users. Informal exchange of transaction information could be linked to blockchain transaction data. Such privacy concerns are serious, particularly when a link is made between identities and transactions. For example, blockchain-based voting rests on the premise that every vote can be linked to the identity of the voter, making it difficult or impossible to guarantee anonymous voting. Pseudonyms might enable user authentication and thus accountability, but privacy concerns can complicate the use of blockchain and trigger institutional pressures that prevent blockchain from realizing its ascribed potential. IS research needs to explore the entanglement of accountability and privacy, studying how such issues affect individual human behavior, such as willingness to engage in transactions on the blockchain.

The blockchain depends on the ability to achieve consensus. This presumes efficacy and efficiency of consensus mechanisms. At present these mechanisms are flawed. Blockchain depends on consensus mechanisms that provide the right incentives for nodes to guarantee blockchain integrity. Proof-ofwork, the most common consensus mechanism, employed by both Bitcoin and Ethereum, relies on computing power. This invokes environmental concerns. In early 2018, it was estimated that Bitcoin’s proof-of-work consensus mechanism was on pace to create a yearly CO2 emission equivalent to one million transatlantic flights.<sup>2</sup> This kind of energy usage is hardly desirable if blockchain is to be adopted on a large scale. Research to design more sustainable consensus mechanisms is ongoing, but the IS research community should actively involve itself in this work, studying the impact of mechanism parameters on the integrity of the blockchain, and exploring the effectiveness of proof-of-work mechanisms based on remuneration vs. proof-of-stake mechanisms that may rely on sanctioning. Designoriented research should craft mechanisms to provide incentives that ensure both the integrity of the blockchain and environmental sustainability.

## 5 Conclusion

In this paper, we discuss how blockchain might give rise to a new type of economic system, which we call the blockchain economy. Whether or not the blockchain economy develops as hoped, the ideas it invokes raise many important research questions. Transactions that are enforced autonomously, following rules in smart contracts, look quite different from transactions in the digital economy. We set the stage for exploring such questions by examining the literature on IT governance that focuses on decision rights, accountability, and incentives. A case study of an emerging DAO examines the blockchain economy, and the implications for governance on these dimensions. We offer a research framework and agenda for IT governance in the blockchain economy, and provide additional important avenues for future IS research through critically examining current assumptions present in the blockchain discourse.

## Acknowledgements

We are indebted to Adrian Nedelcu who has supported the data collection. Moreover, we would like to thank Jason Spasovski for his advice on the technical foundations of blockchain. Finally, we acknowledge the truly developmental review process that this paper has gone through under the guidance of the senior editor, and we appreciate the contribution of the entire review team in helping us to improve upon the ideas presented in the paper.

## References

Akerlof, G. (1970). The market for lemons: Qualitative uncertainty and the market mechanism. Quarterly Journal of Economics, 84(3), 488–500.

Ba, S., Stallaert, J., & Whinston, A. B. (2001). Research commentary: Introducing a third dimension in information systems design – the case for incentive alignment. Information Systems Research, 12(3), 225–239.

Beck, R. (2018). Beyond bitcoin: The rise of blockchain. Computer, 51(2), 54–58.

Beck, R., Avital, M., Rossi, M., & Thatcher, J. B. (2017). Blockchain technology in business and information systems research. Business & Information Systems Engineering, 59(6), 381– 384.

Beck, R., Czepluch, J. S., Lollike, N., & Malone, S. O. (2016). Blockchain—the gateway to trustfree cryptographic transactions. Paper presented at the 24th European Conference on Information Systems, Istanbul, Turkey.

Beck, R., & Müller-Bloch, C. (2017). Blockchain as radical innovation: A framework for engaging with distributed ledgers as incumbent organization. Paper presented at the 50th Hawaii International Conference on System Sciences, Waikoloa, Hawaii, U.S.A.

Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital business strategy: Toward a next generation of insights. MIS Quarterly, 37(2), 471–482.

Böhme, R., Christin, N., Edelman, B., & Moore, T. (2015). Bitcoin: Economics, technology, and governance. Journal of Economic Perspectives, 29(2), 213–238.

Brown, A. E., & Grant, G. G. (2005). Framing the frameworks: A review of IT governance research. Communications of the Association for Information Systems, 15(1), 696–712.

Burritt, R. L., & Welch, S. (1997). Accountability for environmental performance of the Australian Commonwealth public sector. Accounting, Auditing & Accountability Journal, 10(4), 532–561.

Buterin, V. (2014). Ethereum white paper. Retrieved from http://www.the-blockchain.com/docs/ Ethereum\_white\_papera\_next\_generation \_smart\_contract\_and\_decentralized\_applicatio n\_platform-vitalik-buterin.pdf

Chapron, G. (2017). The environment needs cryptogovernance. Nature, 545(7655), 403– 405.

Christidis, K., & Devetsikiotis, M. (2016). Blockchains and smart contracts for the internet of things. IEEE Access, 4, 2292–2303.

The Economist. (2014, November). Everybody wants to rule the world. Retrieved from https://www.economist.com/briefing/2014/11/ 27/everybody-wants-to-rule-the-world

Eisenhardt, K. M. (1989). Agency theory: An assessment and review. Academy of Management Review, 14(1), 57–74.

Fama, E. F., & Jensen, M. C. (1983). Separation of ownership and control. The Journal of Law and Economics, 26(2), 301–325.

Glaser, B. G., & Strauss, A. L. (2008). The discovery of grounded theory: Strategies for qualitative research (3rd ed.). New Brunswick, N.J.: AldineTransaction.

Glaser, F. (2017). Pervasive decentralisation of digital infrastructures: A framework for blockchain enabled system and use case analysis. Paper presented at the 50th Hawaii International Conference on System Sciences, Waikoloa, Hawaii, U,S.A.

Hyvärinen, H., Risius, M., & Friis, G. (2017). A blockchain based approach towards overcoming financial fraud in public sector services. Business & Information Systems Engineering, 59(6), 441–456.

Jensen, M. C., & Meckling, W. H. (1976). Theory of the firm: Managerial behavior, agency costs and ownership structure. Journal of Financial Economics, 3(4), 305–360.

Jentzsch, C. (n.d.). Decentralized autonomous organization to automate governance. Retrieved from https://download.slock.it/ public/DAO/WhitePaper.pdf

Kazan, E., Tan, C.-W., & Lim, E. T. K. (2015). Value creation in cryptocurrency networks: Towards a taxonomy of digital business models for bitcoin companies. Paper presented at the 19th Pacific Asia Conference on Information Systems, Singapore.

Kim, B., Barua, A., & Whinston, A. B. (2002). Virtual field experiments for a digital economy: a new research methodology for exploring an information economy. Decision Support Systems, 32, 215–231.

King, J. L. (1983). Centralized versus decentralized computing: organizational considerations and

management options. ACM Computing Surveys, 15(4), 319–349.

Li, X., & Wang, C. (2017). The technology and economic determinants of cryptocurrency exchange rates: The case of Bitcoin. Decision Support Systems, 95, 49–60.

Mingers, J. (2001). Combining IS research methods: Towards a pluralist methodology. Information Systems Research, 12(3), 240–259.

Mingers, J. (2004). Real-izing information systems: Critical realism as an underpinning philosophy for information systems. Information and Organization, 14(2), 87–103.

Moldoveanu, M., & Martin, R. (2001). Agency theory and the design of efficient governance mechanisms (Joint Committee on Corporate Governance). Toronto: Rotman School of Management, University of Toronto.

Mulgan, R. (2000). “Accountability”: An everexpanding concept? Public Administration, 78(3), 555–573.

Nakamoto, S. (2008). Bitcoin: a peer-to-peer electronic cash system. Retrieved from http://s.kwma.kr/pdf/Bitcoin/bitcoin.pdf

Nærland, K., Müller-Bloch, C., Beck, R., & Palmund, S. (2017). Blockchain to rule the waves: Nascent design principles for reducing risk and uncertainty in decentralized environments. Paper presented at the 38th International Conference on Information Systems, Seoul, South Korea.

Peters, G. W., & Panayi, E. (2016). Understanding modern banking ledgers through blockchain technologies: Future of transaction processing and smart contracts on the internet of money. In P. Tasca, T. Aste, L. Pelizzon, & N. Perony (Eds.), Banking beyond banks and money (pp. 239–278). New York, NY: Springer.

Risius, M., & Spohrer, K. (2017). A blockchain research framework. Business & Information Systems Engineering, 59(6), 385–409.

Sambamurthy, V., & Zmud, R. W. (1999). Arrangements for information technology governance: A theory of multiple contingencies. MIS Quarterly, 23(2), 261–290.

Subramanian, H. (2018). Decentralized blockchainbased electronic marketplaces. Communications of the ACM, 61(1), 78–84.

Swan, M. (2015). Blockchain: Blueprint for a new economy. Sebastopol, CA: O’Reilly Media.

Szabo, N. (1994). Smart contracts. Retrieved May 25, 2017, from http://szabo.best.vwh.net/smart. contracts.html

Tapscott, D., & Tapscott, A. (2016, May). The impact of the blockchain goes beyond financial services. Harvard Business Review. Retrieved from https://hbr.org/2016/05/the-impact-ofthe-blockchain-goes-beyond-financial-services

Tschorsch, F., & Scheuermann, B. (2016). Bitcoin and beyond: a technical survey on decentralized digital currencies. IEEE Communications Surveys & Tutorials, 18(3), 2084–2123.

Underwood, S. (2016). Blockchain beyond bitcoin. Communications of the ACM, 59(11), 15–17.

Urquhart, C., Lehmann, H., & Myers, M. (2010). Putting the “theory” back into grounded theory: Guidelines for grounded theory studies in information systems. Information Systems Journal, 20(4), 357–381.

Van de Ven, A. H. (2007). Engaged scholarship: A guide for organizational and social research. New York, NY: Oxford University Press.

Walsh, C., O’Reilly, P., Gleasure, R., Feller, J., Shanping, L., & Cristoforo, J. (2016). New kid on the block: A strategic archetypes approach to understanding the blockchain. Paper presented at the 37th International Conference on Information Systems, Dublin, Ireland.

Weill, P. (2004). Don’t just lead, govern: How topperforming firms govern IT. MIS Quarterly Executive, 3(1), 1–17.

Weitzner, D. J., Abelson, H., Berners-Lee, T., Feigenbaum, J., Hendler, J., & Sussman, G. J. (2008). Information accountability. Communications of the ACM, 51(6), 82–87.

Wörner, D., Von Bomhard, T., Schreier, Y.-P., & Bilgeri, D. (2016). The bitcoin ecosystem: Disruption beyond financial services?. Paper presented at the 24th European Conference on Information Systems, Istanbul, Turkey.

Wright, A., & De Filippi, P. (2015). Decentralized blockchain technology and the rise of lex cryptographia. Available at https://papers.ssrn. com/sol3/papers.cfm?abstract\_id=2580664

Yin, R. K. (2000). Case study research: Design and methods (2nd ed.). Thousand Oaks, CA: SAGE.

Zhang, Y., & Wen, J. (2017). The IoT electric business model: Using blockchain technology for the internet of things. Peer-to-Peer Networking and Applications, 10(4), 983–994.

## About the Authors

Roman Beck is a full professor at the IT University of Copenhagen. He is the head of the Technology, Innovation Management & Entrepreneurship (TIME) research group and head of the European Blockchain Center. His research focuses on blockchain economics and social media analytics. He is interested in institutional logics of organizations, organizational mindfulness, and governance. He has published over 30 journal and 80 peer-reviewed conference articles in outlets such as MIS Quarterly, European Journal of Information Systems, Journal of Information Technology, and Journal of Strategic Information Systems, among others.

Christoph Müller-Bloch is a PhD candidate at the IT University of Copenhagen. His research interests include the governance of information systems—in particular, in the context of blockchain technology. He has presented his research at international conferences, including the International Conference on Information Systems. He holds an M.S. in business administration and information systems from Copenhagen Business School and a B.S. in business administration from the University of Göttingen.

John Leslie King is a W. W. Bishop Professor at the University of Michigan School of Information. His main works deal with computerization in the public sector and municipalities, as well as other organizations. He has also worked on privacy issues and some of the primary computerization projects, such as project SAGE. He is the author (together with Kalle Lyytinen) of Information Systems: The State of The Field, published by Wiley in 2006. Professor King has a B.A. in philosophy, and graduated with a PhD from the University of California, Irvine School of Administration.
