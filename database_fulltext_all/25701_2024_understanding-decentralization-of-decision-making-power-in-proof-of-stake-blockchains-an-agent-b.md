---
otero_id: 25701
otero_key: "QSQTXXE2"
title: "Understanding decentralization of decision-making power in proof-of-stake blockchains: an agent-based simulation approach"
authors: "Christoph Mueller-Bloch; Jonas Valbjørn Andersen; Jason Spasovski; Jungpil Hahn"
year: "2024"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2022.2125840"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Understanding decentralization of decisionmaking power in proof-of-stake blockchains: an agent-based simulation approach

Christoph Mueller-Bloch, Jonas Valbjørn Andersen, Jason Spasovski & Jungpil Hahn

To cite this article: Christoph Mueller-Bloch, Jonas Valbjørn Andersen, Jason Spasovski & Jungpil Hahn (2022): Understanding decentralization of decision-making power in proof-of-stake blockchains: an agent-based simulation approach. European Journal of Information Systems. DOl: 10.1080/0960085X.2022.2125840

To link to this article: https://doi.org/10.1080/0960085X.2022.2125840

![](/api/attachments/QSQTXXE2/fulltext/images/ca562afbdad11059ff8dedf81d0bdbe725cfecc9e0eb91e9ec4a13adef4e095f.jpg)

Published online: 19 Sep 2022.

![](/api/attachments/QSQTXXE2/fulltext/images/790f4dbd5479a1f9e74ced71853c17cf4115dd265a3615fcaad0f212aed79867.jpg)

Submit your article to this journal

![](/api/attachments/QSQTXXE2/fulltext/images/01f21b8a07f0f100136167cf32b80424e9db0e6638050dfeddac6942c0f48761.jpg)

Article views: 169

![](/api/attachments/QSQTXXE2/fulltext/images/48f140580f0f31790f09bc2d99ac2e75edcbd55e3c199153c96460b767ad0b79.jpg)

View related articles

![](/api/attachments/QSQTXXE2/fulltext/images/1133e7887b65a90f35da0a23618e1f3efa97696716106dfb1b12834bdc8652aa.jpg)

View Crossmark data

Check for updates

# Understanding decentralization of decision-making power in proof-of-stake blockchains: an agent-based simulation approach

Christoph Mueller-Bloch <sup>a</sup>, Jonas Valbjørn Andersen<sup>b</sup>, Jason Spasovski<sup>c</sup> and Jungpil Hahn<sup>d</sup>

<sup>a</sup>Department of Information Systems, Decision Sciences and Statistics (IDS), ESSEC Business School, Cergy-Pontoise, France; <sup>b</sup>Department of Business IT, IT University of Copenhagen, Copenhagen, Denmark; <sup>c</sup>ZTLment, Copenhagen, Denmark; <sup>d</sup>Department of Information Systems and Analytics, National University of Singapore, Singapore

## ABSTRACT

Blockchain systems allow for securely keeping shared records of transactions in a decentralised way. This is enabled by algorithms called consensus mechanisms. Proof-of-work is the most prominent consensus mechanism, but environmentally unsustainable. Here, we focus on proof-of-stake, its best-known alternative. Importantly, decentralised decision-making power is not an inherent feature of blockchain systems, but a technological possibility. Numerous security incidents illustrate that decentralised control cannot be taken for granted. We therefore study how key parameters afect the degree of decentralisation in proof-of-stake blockchain systems. Based on a real-world implementation of a proof-of-stake blockchain system, we conduct agent-based simulations to study how a range of parameters impact decentralisation. The results suggest that high numbers of initial potential validator nodes, large transactions, a high number of transactions, and a very high or very low positive validator network growth rate increase decentralisation. We find weak support for an impact of changes in transaction fees and initial stake distributions. Our study highlights how blockchain challenges our understanding of decentralisation in information systems research, and contributes to understanding the governance mechanisms that lead to decentralisation in proof-of-stake blockchain systems as well as to designing proof-of-stake blockchain systems that are prone to decentralisation and therefore more secure.

ARTICLE HISTORY Received 10 September 2021 Accepted 5 September 2022

KEYWORDS Blockchain; consensus mechanism; centralisation; decentralisation; decisionmaking power; governance

## 1. Introduction

Since their inception (Nakamoto, 2008), blockchain systems have gradually achieved mainstream recognition, and their potential to fundamentally afect organisations, industries, and economies is now widely acknowledged (Beck et al., 2018; Clemons et al., 2017; Risius & Spohrer, 2017). While historically shared records of transactions would be kept by a centralised authority or institution, the main value proposition of blockchain systems is to securely keep shared records in a decentralised way (Constantinides et al., 2018). To function without a designated central operator, a blockchain system requires a protocol to generate consensus among the nodes that jointly administer the blockchain, which is an append-only, distributed database (Lumineau et al., 2021; Rossi et al., 2019; Zachariadis et al., 2019). This socalled consensus mechanism (or consensus protocol) sets the basic rules by which a node is selected to decide on the contents of a block (which contains an array of transaction records) that is added to the blockchain (Bano et al., 2017). Some of the most prominent consensus mechanisms include proof-of-work (PoW) and proof-of-stake (PoS). In PoW, the main determinant of the right to validate the next block is the amount of computing power a node possesses (Nakamoto, 2008). In PoS, the right to validate the next block is determined primarily by the proportion of cryptocurrency a node owns (King & Nadal, 2012). PoW is widely criticised for its high energy costs without external utility and associated environmental and other welfare concerns (Benetton et al., 2021). In response, PoS is increasingly gaining ground. In 2019 and 2020, more blockchains based on PoS than on PoW were launched, making PoS the most common consensus mechanism in new blockchain systems (Irresberger et al., 2021). Moreover, prominent blockchain systems such as Ethereum are in the process of migrating to PoS at the time of writing.<sup>1</sup> In this paper, we therefore focus on PoS, which has received little attention in prior research, despite its importance in practice.

Consensus mechanisms such as PoW and PoS are not only meant to facilitate coordination and thereby agreement among the nodes; they are also designed with the intention of ensuring a high degree of decentralisation of the right to decide on the content of blocks. Decentralisation implies that decision-making power (or control) is more dispersed across a larger group of individuals, whereas centralisation implies that decision-making power is concentrated in a single person or a small group (King, 1983). Despite the intent of achieving decentralisation, consensus mechanisms do not necessarily guarantee decentralisation in practice. In other words, decentralisation is not an inherent feature of blockchain systems, but a desired outcome (Cong et al., 2021; Halaburda & Mueller-Bloch, 2020). The reason decentralisation is desirable is that highly centralised decision-making power in blockchain systems gives rise to a major security threat, the so-called 51% attack. In a 51% attack, a malicious node obtains a majority of the decision-making power and uses its power to compromise the integrity of the blockchain. This is not just a theoretical concern: 51% attacks are becoming increasingly frequent in practice (Shanaev et al., 2019). Overall, centralisation of decision-making power in blockchain systems causes the technology to lose its main value proposition of ensuring the integrity of shared records without the need for trusted third parties, since it implies that a single entity can gain the ability to compromise the integrity of the blockchain. Even if that entity were non-malicious, its power would require all other system participants to trust its benevolence. Therefore, centralisation is a major factor that might prevent blockchain technology from realising its aspired potential of making trusted third parties redundant.

The critical role of the distribution of decisionmaking power in blockchains prompts us to study how decentralisation, or centralisation, simultaneously emerges from both node behaviour and the consensus mechanism. While previous research has studied the specific trade-of between coin inflation and decentralisation of PoS blockchains (Irresberger, 2018), so far there is no comprehensive study on how changes in a number of diferent key parameters impact decentralisation in PoS blockchains. We study this issue by adopting a complex adaptive systems (CAS) perspective. The CAS framework is a powerful tool to study how the micro-level interaction of agents within a system environment results in emergent outcomes at the macro level (Holland, 1992; Miller & Page, 2009). It is regularly used in information systems research (e.g., Haki et al., 2020; Nan, 2011; Zhang et al., 2020) to study settings with high complexity. We conceptualise blockchain systems as CAS, in which blockchain nodes are represented as agents within the environment of a blockchain system, that interact based on rules specified by a PoS consensus mechanism. We rely on an agent-based simulation to study how changes in node behaviour (transaction amount, transaction volume, and network growth) and the setup of blockchain systems (initial network size, initial stake distribution, transac tion fees) afect the distribution of decision-making power in blockchain systems and thus their integrity. The agent-based simulation is validated using real world data from NXT, the first blockchain system based on PoS.

We find that a high number of initial potential validator nodes, large transactions, and a high number of transactions increase the degree of decentralisation. Our results also suggest that a very high or very low positive network growth rate increases the degree of decentralisation. We only find weak support for an impact of changes in transaction fees and initial stake distributions on the degree of decentralisation. Based on our analysis, we can derive concrete measures for blockchain system design to address the risk of overtly centralised decision-making power in PoS blockchain systems. Our study is one of the first in information systems research to look at the blockchain protocol. While there are many studies focusing on blockchain applications, few have investigated how to design blockchain systems as such (Rossi et al., 2019). In doing so, our paper fills a major gap: achieving decentralisation is critical to ensure the security and trustworthiness of blockchain systems.

The remainder of this paper is structured as follows. In section two, we introduce the prior literature on centralisation, decentralisation, and PoS blockchain systems. In section three, we introduce the CAS framework that we adopt to study blockchain consensus mechanisms. In section four, we describe the agentbased model of the PoS consensus mechanism, discuss its validation and the simulation procedure. In section five, we present the results of the simulation experiments and further scenario testing. In section six, we discuss the findings and conclude the paper.

## 2. Background

In this section, we provide a brief overview of prior information systems research on centralisation and decentralisation and explain how the emergence of blockchain systems changes how we view these concepts. Subsequently, we discuss the importance of decentralisation for blockchain systems, provide an overview of threats associated with centralisation, and position this study in the context of extant literature on blockchain systems.

## 2.1. Centralisation and decentralisation of information systems

While information systems research has held a keen interest in centralisation and decentralisation for many decades, the interpretation of these concepts has not always been fully consistent (Ein-Dor & Segev, 1978). Importantly, centralisation and decentralisation have often been conceptualised as multidimensional, covering not only how decision-making power is allocated, but also other aspects, for instance the geographical location of computing equipment (Ein-Dor & Segev, 1978; King, 1983). In this paper, we use the terms centralisation and decentralisation only to refer to the dispersion of decision-making power.<sup>2</sup>

Historically, research focused on whether the use of computers would centralise or decentralise organisational decision-making power. The large and expensive mainframe computers that characterised the early days of computing were thought to favour centralisation. Later, as computers became smaller and less expensive over time, there was an expectation this would further decentralisation. As distributed computing became increasingly common, it became clear that the computing architecture by itself would not necessarily preordain centralisation or decentralisation (Bloomfield & Coombs, 1992). Research focus then shifted to why organisations would choose certain governance arrangements, including centralisation or decentralisation, and how and why these arrangements would lead to certain organisational outcomes (King, 1983; Sambamurthy & Zmud, 1999; Weill & Ross, 2004). More recently, the increased need to coordinate across organisational boundaries, brought about by emergence of digital platforms and ecosystems, has reinvigorated the debate on the centralisation and decentralisation of decision-making power. However, this literature stream also views centralisation or decentralisation primarily as a means to an end (Tiwana et al., 2010).

In the realm of blockchain systems, the role of centralisation and decentralisation is fundamentally diferent. Here, decentralised decision-making power is not a means to achieve a goal. Conversely, it is the goal. This is because the idea behind blockchain systems is to eradicate the need for trusted third parties that wield centralised decision-making power. Prior to the emergence of blockchain systems, such trusted third parties were typically taken for granted. For instance, central banks would manage monetary policy, and centrally-controlled online marketplaces would support transactions among parties that do not trust each other and often do not even know each other. The advent of blockchain systems has challenged this status quo, promising to fundamentally disrupt and transform many societies and industries (Beck et al., 2018; Catalini & Gans, 2020; Clemons et al., 2017; Risius & Spohrer, 2017).

Another diference to established information systems research on centralisation and decentralisation lies in the organisational setting. Prior research on centralisation and decentralisation focused on traditional organisations (King, 1983; Sambamurthy & Zmud, 1999; Weill & Ross, 2004) and digital platform ecosystems (Tiwana, 2010). Blockchain systems represent a very diferent type of organisational setting: they are distributed systems, in which participants are not governed by managers, but by a software protocol. This means that the scope of their potential decisions is very restricted, and the source of decision-making power is clearly specified: in blockchain systems, the protocol that governs interaction provides clear rules regarding the distribution of decision-making power (Andersen & Bogusz, 2019; Hsieh et al., 2018; Rossi et al., 2019). Nodes can primarily exercise their decision-making power by deciding about the contents of a block that is to be added to the blockchain (Bano et al., 2017). Conversely, in traditional organisational settings, the scope of potential decisions would be vast, and the origins of decision-making power would be multifaceted and ambivalent (Bloomfield & Coombs, 1992; Markus & Bjørn-Andersen, 1987).

## 2.2. Centralisation and decentralisation in blockchain systems

Technically, a blockchain is a distributed transactional database that is governed by a consensus mechanism (Constantinides et al., 2018; Rossi et al., 2019; Zachariadis et al., 2019). Blockchain transactions are stored in batches called blocks (which may also be empty). The database is distributed across a number of agents called nodes (Nakamoto, 2008). Blockchains are diferent from traditional distributed databases in that they can function without a designated central operator. This requires a mechanism that incentivises agreement among the nodes, thereby avoiding the creation of competing blockchains (i.e., forks). This is achieved by consensus mechanisms, which provide the basic rules with regard to the distribution of decision-making power across the nodes. The node that obtains the decision-making authority, the validator node, obtains the right to decide on the content of the next block that is added to the blockchain (Bano et al., 2017). For every new block to be added to the blockchain, decision-making power is recalculated based on the specifications in the consensus mechanism. This introduces a degree of randomness and serves to disperse decision-making power. How decision-making power is obtained varies across diferent consensus mechanisms (Bano et al., 2017; Bonneau, 2018).

In this paper, we focus on PoS, a consensus mechanism that was devised to address environmental concerns related to PoW. The latter was proposed by Nakamoto (2008) to enable consensus in the Bitcoin blockchain. PoW allocates decision-making power mainly based on a competition of who can solve a cryptographic hash puzzle the soonest. Due to the preimage resistance of cryptographic hash functions, the likelihood of winning the competition is proportional to a node’s expenditure of computing power. In practice, this led to a computational arms race. For Bitcoin alone, the energy consumption is comparable to that of a small, industrialised country (Saleh, 2021). PoS, the most salient current alternative to PoW (Irresberger et al., 2021), addresses this issue by distributing decision-making power mainly based on the size of nodes’ investment (i.e., the “stake”) in the cryptocurrency associated with the blockchain. Nodes with larger stakes therefore are more likely to obtain more decision-making power (Bano et al., 2017; King & Nadal, 2012).

A high degree of centralisation of decision-making power is highly problematic since a node with particularly high decision-making power can compromise the integrity of the blockchain. By monopolising the right to decide upon the content of new blocks, a malicious node could perform a 51% attack. For instance, the attacking node could claim all transaction fees, perform double spending, or reject or include transactions as preferred (Conti et al., 2018). Overall, centralisation is associated with three major threats (see Table 1). First, a node might perform a 51% attack to gain utility within the blockchain system. For instance, the node might want to achieve monetary gain by double-spending cryptocurrency (Nakamoto, 2008). It has been argued that this type of attack is not very likely: a powerful node migh gain more utility from not attacking, since an attack would undermine the validity of its wealth (Krol et al., 2013). However, recent evidence suggests that such attacks take place frequently, which might be explained by the fact that cryptocurrency value only decreases moderately (12 to 15 percent) in the case of such attacks (Shanaev et al., 2019). In Table 1, we term this attack as the Nakamoto attack, since this type of 51% attack is described in Nakamoto’s white paper (2008). Second, a node might perform a socalled Goldfinger attack to gain utility outside of the blockchain system (Kroll et al., 2013). There are three conceivable reasons for conducting this type of 51% attack. One potential reason for a Goldfinger attack might be a government or another institution wanting to achieve some institutional goal, for instance related to law enforcement. Alternatively, a non-state attacker might want to attain some political or socia goal, for instance in a social protest. Finally, an attacker might seek financial gain outside of the blockchain system, for instance after having taken short positions on the blockchain system’s cryptocurrency. Overall, it has been argued that Goldfinger attacks are not an unlikely scenario (Kroll et al.,

2013), in particular since decision-making power need only be acquired temporarily as well, not necessarily permanently (Bonneau, 2018). The third threat posed by centralisation is a scenario in which a nonmalicious node gains a lot of decision-making power so that it possesses the capacity to conduct a 51% attack. While the node is non-malicious and therefore has no intention to attack, the sheer possibility may already have detrimental efects on the blockchain system due to a lack of trust. For instance, other potential validator nodes might leave the system and investors might decide to sell their cryptocurrency. While this scenario has been described (Halaburda & Mueller-Bloch, 2020), we are not aware of any research demonstrating this empirically. Overall, our discussion of the three diferent threats shows that centralisation always poses a threat to blockchain systems, regardless of whether or not the node with a high degree of decision-making power is malicious. Moreover, it is not possible for a malicious node to attack the system as long as the system is suficiently decentralised. Therefore, in this paper we do not focus on whether or not individual nodes are malicious, but whether or not the blockchain system is decentralised.

Other threats specific to PoS-blockchains exist, such as the “Nothing-at-Stake” attack, in which nodes extend every potential fork (Bano et al., 2017). We follow Bonneau (2018) and Saleh (2021) in assuming that a solution exists for these attacks. Bonneau (2018) assumes that a takeover requires that a single node obtains a majority of the overall stake in the blockchain. However, while in PoS-blockchains the main determinant of decision-making power is the stake a node holds, the actual selection of the validator node (and hence the degree of decentralisation) is determined by the combination of stake held by the node together with other parameters built into the consensus mechanism which only materialises at runtime. We therefore devise a separate measure for decision-making power in this paper, based on a realworld implementation of a PoS consensus mechanism. Moreover, despite being named 51% attack, we do not assume that there is a specific amount of decisionmaking power a node needs to obtain to compromise the blockchain (e.g., 51 percent), given that the greater the relative decision-making power the node obtains, the more likely it is that the attack succeeds (Bonneau, 2018). In line with this notion, we conceptualise decision-making power as a continuum, in which a higher degree of decentralisation ensures a higher degree of integrity.

Table 1. Blockchain Centralisation and Associated Threats.

<table><tr><td>Threat</td><td>Description</td><td>Assumptions</td></tr><tr><td>Nakamoto attack</td><td>A node with a high degree of decision-making power attacks the blockchain system to gain utility within the blockchain system (Nakamoto, 2008).</td><td>The node is malicious and maximizes utility within the blockchain system by conducting a 51% attack.</td></tr><tr><td>Goldfinger attack</td><td>A node with a high degree of decision-making power attacks the blockchain system to achieve an extrinsic goal (Kroll et al., 2013).</td><td>The node is malicious and maximizes utility outside of the blockchain system by conducting a 51% attack.</td></tr><tr><td>Centralization vulnerability</td><td>A node possesses a high degree of decision-making power, thereby creating a vulnerability that can have detrimental effects for the blockchain system (Halaburda &amp; Mueller-Bloch, 2020).</td><td>Blockchain users are aware of the centralisation and consider it a threat.</td></tr></table>

In this paper, we focus on the (de-)centralisation of decision-making power related to transaction validation. However, other dimensions of decision-making, and therefore centralisation or decentralisation, are also associated with blockchain systems, thereby introducing potential single points of failure (Halaburda & Mueller-Bloch, 2020; Sai et al., 2021). For instance, the initial system development (Beck et al., 2018) and system update development (Azouvi et al., 2018) are often marked by centralisation in practice. While some kinds of centralisation may in fact be beneficial (e.g., Cennamo et al., 2020), there is reason to believe that not only centralisation of transaction validation, but most kinds of centralisation undermine blockchain’s promise of removing trusted third parties. For instance, if there was only a single person or a small group doing development work, they could introduce backdoors, which could corrupt the integrity of the system if appropriate monitoring by outsiders was lacking.

Our paper contributes to the literature on blockchain consensus mechanisms. So far, most of this literature has focused on PoW blockchains. Papers focusing on this consensus mechanism include Gervais et al. (2016), Arnosti and Weinberg (2022), Biais et al. (2019), Alsabah and Capponi (2020), Benetton et al. (2021), and Cong et al. (2021). However, few papers have focused on PoS blockchains. Irresberger (2018) conducts a simulation study of the trade-ofs between coin inflation and the degree of decentralisation in PoS blockchains. He does not consider cases in which transaction fees are the only block reward, arguing this may undermine consensus (Carlsten et al., 2016). However, a recent paper by Saleh (2021) demonstrates that in PoS, as opposed to PoW, consensus is more likely with low block rewards. This is because low block rewards shift validator incentives towards maximising coin value, which encourages consensus. Consequently, we focus on PoS blockchains without inbuilt inflation, in which transaction fees are the only block reward, thereby complementing the study by Irresberger (2018). Our analysis also goes beyond the study by Irresberger in that we investigate the impact of changes in a number of diferent key parameters on decentralisation, instead of focusing on one specific trade-of. Our results do not generally apply to stake-based onchain blockchain governance, which has recently become more common (Tsoukalas & Falk, 2020), but only to the PoS consensus mechanism.

## 3. Complex adaptive systems modeling of proof-of-stake blockchain systems

So far, we have discussed the proof-of-stake consensus mechanism based on a review of the current literature. This has provided a qualitative description of the phenomenon under study. To study how the degree of decentralisation emerges as a result of interactions among nodes, we need an analytical tool specifically suited for multi-level quantitative theorising. Such a tool is provided in the complex adaptive systems (CAS) framework. The CAS framework allows for studying emergent outcomes of interactions within PoS blockchain systems since it captures how rulebased interactions among individual agents, that is, interactions between nodes governed by the PoS consensus mechanism, result in emergent outcomes at the global system level, that is, the distribution of decision-making power in the blockchain system. A complex adaptive system is defined as being “ . . composed of interacting agents described in terms of rules . . . ” (Holland, 1995, p. 10). The CAS framework has been applied in a wide variety of fields ranging from biology, physics, and healthcare (Peters, 2014) to information systems (Haki et al., 2020; Nan, 2011; Zhang et al., 2020).

In this research, we leverage the CAS framework and its associated computational instruments (e.g., Miller & Page, 2009) to study how interactions among nodes in a PoS blockchain system result in emergent outcomes related to the distribution of decision-making power. By applying the CAS framework, we can identify the impact of specific design choices and behavioural scenarios on the degree of decentralisation.<sup>3</sup> This necessitates a framework capable of accommodating the design and behavioural parameters of blockchain systems as well as accounting for the rules embedded in the consensus mechanism itself. The CAS framework conceptualises complex adaptive systems in terms of the structural levels of a system at large and in terms of the components necessary for generating and perpetuating emergent outcomes (see also Table 2).

The structural levels of a CAS include generative structures, elemental structures, and observed structures (Drazin & Sandelands, 1992). First, generative, or ‘deep’, structures refer to the tacit rules that govern actions of and interactions between actors. These structures are the unobserved, generative, and recursive functions that produce elemental and observed structures. Second, elemental structures include the states of agents and their actualised interactions. These states and interactions produce micro-level structures that can be observed in time and space. Although there is no universally agreed-upon paradigm for describing the elemental structures of a CAS (Gell-Mann,

Table 2. Conceptualising Blockchains as CAS.

<table><tr><td>CAS Structure</td><td>CAS Component</td><td>CAS Model Elements</td><td>Equivalent in Proof-of-stake Blockchain Systems</td></tr><tr><td>Generative structure (unobserved)</td><td>Model Rule</td><td>The behavioral logic of the model specified at the model-level</td><td>Consensus mechanism as an algorithm for choosing the validator node</td></tr><tr><td rowspan="4">Elemental structure (micro-level)</td><td>Agent</td><td>Identity</td><td>A public address that identifies nodes</td></tr><tr><td rowspan="2">Interaction</td><td>Attributes Behavioral rules Connection</td><td>Currency stake Make a transaction Transactions on the blockchain, fee paid to winning validator node</td></tr><tr><td>Flow</td><td>Amount and volume of currency transactions between agents, e.g., nodes&#x27; stakes decrease when making a payment</td></tr><tr><td>Environment</td><td>Initial conditions, model parameters, and parameter settings</td><td>Number of available validator nodes, initial distribution of stake</td></tr><tr><td>Observed structure (macro-level)</td><td>Emergent property</td><td>Output observations at the system level</td><td>Distribution of decision-making power, structure of the validation network</td></tr></table>

1994), three components have been consistently recognised as the core of the theory: agents, interactions, and environment (e.g., Holland, 1995; Nan, 2011). Agents are the basic entities in complex adaptive systems. Depending on the phenomenon under study, they can be representations of, for instance, individuals of a species of animals, organisations, technologies, individual human beings in a social setting, or nodes in a blockchain system. Agents are characterised by a set of attributes and a number of behavioural rules. Attributes refer to parameters that can be defined at the agent level and that define the identity or state of an agent. Behavioural rules specify how each agent interacts with other agents or with input from the model environment. Interactions consist of mutually adaptive behaviours manifested through structural connections between agents through which flows of resources are channelled. The environment represents the medium for agent interaction and is characterised by a structural topography in terms of gradients related to resource distribution and possibilities for interaction. Finally, observed structures refer to the social facts that emerge at the macrolevel from interactions between agents. Even though each agent is oblivious to the properties and behaviour of the system, the aggregation of their interactions results in emergent system outcomes (Holland, 1992). Applying the framework of CAS to study blockchain systems, we can now summarise the structure, components, and elements of CAS. Table 2 provides a summary of the CAS framework and exemplifies each of its components in the blockchain context.

## 4. CAS instrument: agent-based modeling

The agent-based modelling (ABM) approach allows researchers to probe distributed systems and explore how its agents interact at diferent parameter settings to produce emergent structures and behaviours over time. ABM has been used as an analytical tool for studying social behaviour since Schelling’s (1969) study of segregation and has increasingly gained attention as a method for generating theory in the social sciences (Bonabeau, 2002; Epstein, 2006). The value of ABM as a tool for quantitative theorising in information systems and management research has previously been demonstrated by Nan and Tanriverdi (2017), Rivkin and Siggelkow (2007), and Siggelkow and Levinthal (2003), among others.

Extending from its roots in CAS theory, the general idea of ABM is to specify agents within a system environment and endow them with simple theorybased interaction rules and then observe the emergent macro-level outcomes (Holland, 1995; Miller & Page, 2009). Agent-based models can in principle be expressed as a series of mathematical equations. Complex agent-based models are usually expressed in computational processes and are studied using numerical (e.g., Monte Carlo) methods (Epstein, 2006).

## 4.1. Modelling decision-making power through the PoS consensus mechanism

We conceptualise a blockchain system as a CAS of agents (i.e., nodes participating in a blockchain network) in which emergent decisions are made about who gets to validate a block. To ensure the agentbased model reproduces the behaviour of a blockchain system with a high degree of fidelity, we followed the general procedure for validating an agent-based simulation model suggested by Klügl (2008). The procedure focuses specifically on establishing face validity as well as calibrating and validating the model empirically (the latter is described in section 4.3). To establish face validity and to validate the simulation empirically by comparing the outcomes of the simulation with the real-world implementation, we require a real-world implementation of a PoS blockchain as a baseline. We chose the NXT blockchain<sup>4</sup> since it represents a rather prototypical and straightforward implementation of a PoS blockchain system. In particular, in NXT decision-making power does not increase the longer tokens have been in a node’s account (this is known as coin age). Moreover, as one of the first PoS blockchains, at the time of writing NXT has already been running for over six years without any major bugs, suggesting that this is a well-designed implementation of a PoS blockchain. To ensure face validity, we built the simulation model by translating salient features of the Java source code of the actual open-source NXT implementation directly into Python (see APPENDIX A). This ensures that the mechanisms of the simulation model align mechanically with the empirical context it reproduces.

We model the blockchain system as containing $A _ { \mathrm { t } }$ potential validator nodes at any point in time t; the initial number of potential validator nodes is $A _ { 0 } .$ The blockchain system is an open network in which new nodes can freely join the network. The growth of the network is modelled as simple exponential growth using parameter G, which denotes the growth rate – $A _ { \mathrm { t } } { \bf \Pi } _ { + 1 } = A _ { \mathrm { t } }$ (1+G). Each node a is assigned a unique identifier and possesses a currency balance $b _ { \mathrm { { a t } } }$ at time t; a node a is assigned an initial currency balance $b _ { \mathbf { a 0 } } .$ As the PoS consensus mechanism relies on the currency balance of each node $b _ { \mathrm { { a t } } }$ to determine its decision-making power, the initial distribution of stake balances across all nodes B is a key parameter as it efectively determines how decentralised decisionmaking power in the system is at the onset. For each block (or time t), each node can be in one of two states $s _ { \mathrm { a t } } ,$ since it can either be the validator node of the block, or not. A node a obtaining the authority to validate a specific block at time t (here determined by each block) would have state $s _ { \mathrm { a t } } = 1$ , and the remaining nodes (a’) would be assigned state $s _ { \mathrm { a } ^ { \prime } \mathrm { t } } = 0 )$ 0)

As previously described, the PoS consensus mechanism distributes decision-making power among agents. The decision-making power distribution is defined as P(A). To correct for fluctuations in the demand for block validation, that is, spikes and dips in transactions sent per block, the PoS consensus mechanism sets a multiplier $M _ { \mathrm { t } }$ that is determined by the amount of time it took to validate the previous block. Moreover, to further increase decentralisation of decision-making power, each node is assigned a validation threshold $h i t _ { \mathrm { a t } } ,$ which is a randomly generated value unique to each node at time t. The model can then determine the decision-making power ${  { p _ { \mathrm { a t } } } }$ of a node a at a point in time t. This is determined by the product of the global demand multiplier M<sub>t</sub> and the node-specific efective balance $b _ { \mathrm { { a t } } }$ divided by the validation threshold $h i t _ { \mathrm { a t } }$ for node a at time t. Consequently, the decision-making power ${ \mathit { p } } _ { \mathrm { a t } }$ of each node a at each block t is defined by:

$$
p _ {a t} = \frac {M _ {t} \times b _ {a t}}{h i t _ {a t}}
$$

The node with the highest decision-making power $\boldsymbol { \mathbf { \mathit { P } } } \boldsymbol { a } t$ becomes the validator node for the respective block and is assigned validation state $s _ { \mathrm { a t } } = 1$ . The validator node then receives the transaction fee f, which is added to its efective balance $b _ { \mathrm { { a t } } } .$ . The transaction fee f is paid by all transacting nodes for each block. The transaction fee amount for each block depends on the average transaction fee F. We assume that all eligible nodes are in principle willing to validate transactions, since once a node possesses cryptocurrency, there is little additional cost associated with becoming a potential validator node (only an Internet connection is needed), but substantial potential benefit exists in the form of transaction fees. Having specified how the model determines the decision-making power for each agent, we now turn to explaining how the distribution of decision-making power emerges over time from node interactions governed by the PoS consensus mechanism.

The distribution of decision-making power emerges as a result of redistribution of stake through transactions, which is determined by the transaction volume, the amount of currency sent in each transaction, and the transaction fees. Transactions between nodes in the system are modelled so that for each block (i.e., time step t in the model), a number between 0 and A transactions between randomly selected node pairs take place. The transaction volume parameter is denoted by V. Together with the transaction amount, defined in the model as the average amount of stake sent in each transaction and denoted by U, and the average transaction fee denoted by F, it afects the redistribution of efective balance between nodes in the blockchain system. This redistribution afects the distribution of stake, which in turn afects the distribution of decision-making power in the blockchain system at large. Table 3 shows an overview of model parameters as well as agent states for the agent-based simulation of the PoS consensus mechanism.

## 4.2. Measuring the distribution of decision-making power

To measure centralisation or decentralisation of decision-making power, we require a measure that allows quantifying how decision-making power is distributed among the agents that are part of the network. We use a measure of inequality, which can be defined as the dispersion of a distribution of population attributes (Litchfield, 1999). Inequality measures are often used to quantify how income or other welfare indicators are distributed (ibid). We use an inequality measure to assess how decision-making power is distributed. There are several inequality measures, most prominently entropy-based measures, such as the Theil index and the Gini coeficient.

Table 3. Parameters for agent-based simulation of the PoS consensus mechanism.

Both the Theil index and the Gini coeficient adhere to critical principles, in particular mean independence, population size independence, symmetry, and Pigou-Dalton Transfer sensitivity (World Bank Institute, 2005). Mean independence implies that the measure would not change if the population attribute measured (in our case, decision-making power) would be doubled for all agents. For the blockchain context, this means that the measure should not change if the decision-making power of all nodes were to be doubled. Population size independence means that the measure would not change if the population size were to change. This means that changes in the number of potential validator nodes should not afect the measure. Symmetry implies the measure would not change if two agents swapped their fraction of the population attribute (i.e., decision-making power). For our context, this implies that the nodes’ identity should be irrelevant for the measure. Pigou-Dalton Transfer sensitivity means that transferring a fraction of the population attribute (i.e., decision-making power) from powerful to less powerful agents would reduce the measure (ibid). In the blockchain validation context, this means that the transfer of decisionmaking power from powerful to less powerful nodes should lead to a decrease in the measure, indicating a reduction of centralisation. Even though both Theil index and Gini coeficient fulfil these four criteria, they are also marked by diferences. Importantly, the interpretation of the Gini coeficient is more intuitive since it is calculated using the Lorenz curve (Lerman & Yitzhaki, 1984). Due to its superior interpretability, we therefore rely upon the Gini coeficient to measure the distribution of decision-making power.

The Gini coeficient uses the Lorenz curve as the basis for its computation. As illustrated in Figure 1, the Gini coeficient is defined (and calculated) as the ratio of the area X between the line of equality (i.e., the $4 5 ^ { \circ }$ line) and the Lorenz Curve L(p) to the area X+Y under the line of equality (which is 0.5) (Gastwirth, 1972). For discrete distributions, the Gini coeficient can be computed as:

<table><tr><td>Parameter</td><td>Description</td><td>Notation</td></tr><tr><td colspan="3">Model Parameters</td></tr><tr><td>Initial number of nodes</td><td>The initial number of agents available as potential validator nodes (i.e., active and online agents)</td><td> $A_0$ </td></tr><tr><td>Validation multiplier</td><td>A multiplier based on the time it took to validate the previous block</td><td>M</td></tr><tr><td>Transaction fee</td><td>The average transaction fee acquired by the validator node</td><td>F</td></tr><tr><td>Initial stake distribution</td><td>Initial distribution of stake across agents set to either the observed NXT distribution or any of a range of common distributions</td><td>B</td></tr><tr><td>Transaction amount</td><td>The average amount sent for each transaction between agents</td><td>U</td></tr><tr><td>Transaction volume</td><td>Number of transactions between agents</td><td>V</td></tr><tr><td>Blockchain network growth rate</td><td>Multiplier for the growth of the number of potential validator nodes in the network</td><td>G</td></tr><tr><td colspan="3">Agent States</td></tr><tr><td>Validation state</td><td>Binary indicator of whether an agent has validation rights or not</td><td> $s_a$ </td></tr><tr><td>Effective balance</td><td>The balance of currency for each agent</td><td> $b_a$ </td></tr><tr><td>Validation threshold</td><td>A randomly generated value that is unique to each agent</td><td> $hit_a$ </td></tr><tr><td>Decision-making power</td><td>Determined by the global demand multiplier, the validation threshold, and the effective balance of each agent</td><td> $p_a$ </td></tr></table>

![](/api/attachments/QSQTXXE2/fulltext/images/d84daa40846f4ffe195a588d63b8fa807002f36842fcedfa5be1997759d16ebe.jpg)  
Figure 1. The Gini Coeficient and Lorenz Curve.

$$
\begin{array}{r l} G i n i & = \frac {X}{X + Y} = 1 - \frac {Y}{X + Y} \\ & = 1 - 2 \times \sum_ {a = 1} ^ {A} \left(\frac {A - 1 - a}{A + 1}\right) \times \left(\frac {P _ {a}}{P}\right) \end{array}
$$

where P is the sum of all nodes’ decision-making power.

## 4.3. Simulation model calibration and empirical validation

Having replicated the observed source code and specified the outcome variable of the distribution of decisionmaking power, we then calibrated and empirically validated the simulation model. To calibrate the model, its parameters have to be set in a way that a structurally correct model produces a valid outcome (Klügl, 2008). We ran the simulation model with the initial parameter settings observed in the actual NXT blockchain and compared the outputs of the observed versus simulated blockchain systems in terms of distribution of decisionmaking power as measured by the Gini coeficient. We collected transaction data for the initial 120,000 blocks of the NXT blockchain and measured how the distribution of decision-making power changed over time (see Figure 2). We then used the actual observed parameter values of the NXT blockchain system as a baseline to calibrate the simulation model. Specifically, the simulation model used the observed NXT blockchain system data – the initial number of nodes $\left( A _ { 0 } \right)$ was set to 73, the average transaction fee amount (F) to 414 units of currency, the average transaction amount (U) to 39,434 units of currency, average transaction volume per block (V) to 2.54, and the blockchain network growth rate (G) to 0.03. We chose to validate our simulation model against the first 120,000 blocks of the NXT blockchain (equivalent to approximately 125 days), since after 120,000 blocks, the NXT blockchain system’s consensus mechanism was altered. To ensure that our simulation results reflected the underlying structure of the model rather than a particular realisation of a stochastic process, we performed 20 replication runs for each setting and calculated the average. We then took the moving average with a window size of 20 blocks to smoothen out fluctuations and highlight longer-term trends.

![](/api/attachments/QSQTXXE2/fulltext/images/43f881fec9074592cc107a4b8d2c85def6e71109faf7b0b97c21f073bf193d41.jpg)  
Figure 2. Observed versus Simulated Gini Coeficients.

Comparing the results of the simulated Gini coeficients against the actual NXT data, we find that the simulation model after an initial discrepancy converges on a decision-making power distribution similar to the NXT blockchain system (see Figure 2). The initial diference between the simulated and observed distribution of decision-making power can be explained by the fact that the average amount sent per transaction was larger by a factor of ten for the initial 25,000 blocks of the observed blockchain compared to the remaining 95,000 blocks. This can be ascribed to the extraordinary dynamics in the genesis of the NXT blockchain system rather than to a general mechanism of the PoS consensus mechanism.

## 4.4. Simulation experiments

Having validated our agent-based model, we moved on to simulate the efects of changes in relevant simulation parameters (see Table 4) on the decentralisation of decision-making power. We used the parameter settings observed in the NXT blockchain system to establish our simulation baseline. This is to ensure that any subsequent experimental treatments are based on reasonable and realistic values and to allow for discerning the efects of parameter manipulations. We then manipulate each of these parameters with a range of 7 relevant values ranging from 5 to 1,000 percent of the corresponding baseline value (i.e., 5%, 10%, 25%, 50%, 250%, 500% and 1,000% of the baseline value). There are two exceptions here. First, we fixed the validation multiplier parameter (M) to the model baseline value as it represents the demand for validation that is determined by exogenous drivers. Second, the initial stake distribution parameter (B) concerns a matter of kind and not a matter of quantity. Hence, it is not possible to manipulate it using fractions or multiples of a baseline value. Instead, we manipulate the initial stake distribution parameter with various canonical distributions (e.g., uniform, normal, bimodal, power law, etc.) to analyse the impact of changes in the initial stake distribution on the decentralisation of decision-making authority.

Table 4. Experimental Design – Parameters Simulated.

<table><tr><td colspan="9">Design Parameters</td></tr><tr><td>Initial stake distribution (B)</td><td>Observed</td><td>Normal</td><td>Power-Law 1</td><td>Power-Law 2</td><td>Bimodal Beta</td><td>Uniform</td><td>Skewed</td><td>NA</td></tr><tr><td>Treatment relative to baseline</td><td>5%</td><td>10%</td><td>25%</td><td>50%</td><td>Baseline</td><td>250%</td><td>500%</td><td>1,000%</td></tr><tr><td>Initial number of nodes ( $A_0$ )</td><td>4</td><td>7</td><td>18</td><td>37</td><td>73</td><td>183</td><td>365</td><td>730</td></tr><tr><td>Transaction fee (F)</td><td>21</td><td>41</td><td>104</td><td>207</td><td>414</td><td>1035</td><td>2070</td><td>4140</td></tr><tr><td colspan="9">Behavioural Parameters</td></tr><tr><td>Transaction amount (U)</td><td>1,972</td><td>3,943</td><td>9,859</td><td>19,717</td><td>39,434</td><td>98,585</td><td>197,170</td><td>394,340</td></tr><tr><td>Transaction volume (V)</td><td>0.13</td><td>0.25</td><td>0.64</td><td>1.27</td><td>2.54</td><td>6.35</td><td>12.7</td><td>25.4</td></tr><tr><td>Blockchain network growth rate (G)</td><td>0.0015</td><td>0.0030</td><td>0.0075</td><td>0.0150</td><td>0.0300</td><td>0.0750</td><td>0.1500</td><td>0.3000</td></tr></table>

We repeated this for all parameters settings to perform a complete sensitivity analysis of the main efects each of the parameters has on the distribution of decision-making power. Having observed the main efects of each parameter in the sensitivity analysis, we then simulated relevant scenarios based on highimpact parameter settings to further explore the implications of the sensitivity analysis. In total, we performed 880 runs across 120,000 simulated time steps per run (i.e., blocks). The actual values tested in the simulation experiments are summarised in Table 4.

## 5. Findings

Our analysis shows that the distribution of decisionmaking power in the observed NXT blockchain system is highly centralised with a Gini coeficient above 0.95 after the initial 25,000 blocks representing the genesis of the blockchain (see Figure 2). This begs the question of how to increase decentralisation (i.e., reduce centralisation) in order to promote the integrity of the blockchain. In the following, we discuss how changes in model parameters afect the degree of decentralisation of decision-making power.

## 5.1. Initial stake distribution

To discern how the distribution of decision-making power is afected by the initial distribution of stakes among nodes, that is, the distribution of cryptocurrency across all nodes, categorical treatments depending on the specific distribution were required. As such, we tested six of the most common distributions along with the observed distribution from the validation data set, a normal stake distribution, two power-law distributions with opposite orientations, that is, with both many ‘poor with few ‘rich’ and many ‘rich’ with few ‘poor’ nodes, a bimodal beta distribution, a uniform distribution where all nodes are given equal stakes, as well as a skewed distribution in which one agent holds 90% of the initial stake. Figure 3 shows how, beyond some initial disparity, all initial stake distributions except the skewed distribution converge on a somewhat stable Gini coeficient of around 0.95, matching the observed NXT distribution. The skewed distribution is designed so that one node is initially assigned 90% of the total stake, with the remaining 10% distributed equally among the remaining nodes. In this case, the blockchain network converges on complete centralisation, that is, the initially dominant node consistently wins validation rights. Similar results for the majority of initial stake distributions indicate that, while given vastly diferent initial distributions, the consensus mechanism redistributes stake over time in such a way that the initial stake distribution, in all but the case of the skewed distribution, has relatively little impact on the distribution of decision-making power. This can be explained as a consequence of the randomness introduced to the blockchain by the PoS consensus mechanism implementation in the form of the random validation multiplier and continuous transactions between nodes.

![](/api/attachments/QSQTXXE2/fulltext/images/9a91792b896b4c31ef70c421ac7ef2b845fe7538015bf0375b6049d600c29b95.jpg)  
Figure 3. Efects of Initial Stake Distribution.

![](/api/attachments/QSQTXXE2/fulltext/images/4746f93b805af5e2660ae2473222f4aa6995299e7794f69ce3d082642fab72d8.jpg)  
Figure 4. Efects of Initial Number of Nodes.

## 5.2. Initial number of nodes

The initial number of nodes denotes the number of potential validator nodes available at the genesis of the blockchain. Because nodes receive a transaction fee that efectively increases their stake and thereby their chance of obtaining the right to validate blocks, the size of the initial blockchain system can be influential in the distribution of decision-making power throughout the evolution of the blockchain. Figure 4 shows that a low number of initial nodes result in very low decentralisation of decision-making power, whereas decentralisation increases as the number of initial nodes increases.

Efectively, in order to achieve substantial decentralisation of decision-making power, the blockchain system should be initiated with a greater number of potential validator nodes, all else being equal. This result has implications for the timing of when a PoS blockchain system should be launched, since a premature initiation with few potential validator nodes reinforces the dynamics leading to lower decentralisation. This also implies that PoS blockchain systems with smaller numbers of initial validator nodes are generally more prone to breaches of integrity.

## 5.3. Transaction fee

Higher transaction fees should intuitively mitigate centralisation by incentivising a larger number of potential validator nodes to participate early on in the lifespan of a blockchain system. However, as shown in Figure 5, the sensitivity analysis for the parameter denoting the average transaction fee for each block reveals only modest efects of changes in the average transaction fee on the distribution of decision-making power. Increased transaction fees have a slightly negative efect on decentralisation, as shown in Figure 5. In the context of the PoS consensus mechanism, this negative efect could be explained by the fact that the validator node for each block is primarily selected based on its currency stake so that the winning validator node is more likely to accumulate even larger stakes from increased transaction fees and thereby, in turn, increase its future decision-making power.

![](/api/attachments/QSQTXXE2/fulltext/images/cfa787fc10f70a2a9a2227f74523b165738af5f6da42c577dff14f1a5435c274.jpg)  
Figure 5. Efects of Transaction Fee.

## 5.4. Transaction amount

Similarly, large average transaction amounts could mean that stake, and thereby decision-making power, would accumulate in the hands of a few nodes. However, as illustrated in Figure 6, higher average transaction amounts positively afect decentralisation. It should be noted that for the settings at which the degree of decision-making power decentralisation starts to substantially increase (i.e., at a threshold of 250 percent of the observed value), transaction amounts are quite substantial – for 250 percent of the observed value, transactions equal to an average amount of at least 98,585 units, equivalent to USD 4,478 per transaction (using the median exchange rate during the first 120,000 blocks of the NXT blockchain). Even larger average transaction amounts lead to even higher degrees of decentralisation. The transaction amount is determined by agent behaviour rather than by blockchain design and is therefore not directly available for manipulation by those designing and managing the blockchain system. However, issues of application context become salient, given that blockchains used in contexts operating with small transaction amounts (e.g., retail, payments) might be more vulnerable than blockchains with mostly large transactions (e.g., financial settlement, assets).

## 5.5. Transaction volume

Another model parameter determined by agent behaviour is the transaction volume in terms of the average number of transactions per block. The sensitivity analysis for this parameter shows a positive efect of increases in transaction volume on decentralisation of decision-making power (see Figure 7). However, the distribution of decision-making power over time converges to a level at which only a slight positive efect remains. There seems to be a positive relationship between average transaction volume and the time it takes for that convergence to take place, as illustrated in particular by the behaviour of the graphs indicating the degree of decentralisation at the levels of 250 percent and 500 percent of the observed value. The graph illustrating the degree of decentralisation at the levels of 1,000 percent of the observed value presumably exerts similar behaviour, only with a greater delay, given that it takes an increasing trend as time passes, similar to the behaviour of the two aforementioned series (i.e., at 250 and 500 percent of the observed value) right before they converge. Efectively, stimulating transaction volume to a threshold of 25.4 transactions per block will slightly increase decentralisation of decision-making power and improve the integrity of the blockchain.

![](/api/attachments/QSQTXXE2/fulltext/images/268fda8867f57e1e27ff5a546cc452c827371b33a05ded641bbfe1f722041d03.jpg)  
Figure 6. Efects of Transaction Amount.

![](/api/attachments/QSQTXXE2/fulltext/images/74ce284da874d9e02ca154f87aa4c630411a4a95e212683eaf955e02160f4592.jpg)  
Figure 7. Efects of Transaction Volume.

![](/api/attachments/QSQTXXE2/fulltext/images/8256500ae279f3255f1dcd4208e95c133f05656f5d398da9c9c6485048448605.jpg)  
Figure 8. Efects of Blockchain Network Growth Rate.

## 5.6. Blockchain network growth rate

The final model parameter to be included in the sensitivity analysis concerns the growth rate of the blockchain network, that is, the rate at which new potential validator nodes join the network. The most substantial positive efect on decentralisation is achieved by either very high or very low settings (see Figure 8). While the low 5 and 10 percent settings produce the highest decentralisation, these are followed by the 1,000 and 500 percent settings. This indicates that there is a nonlinear relation between blockchain network growth rate and decentralisation of decision-making power, favouring either very low (0.15–0.3 percent) or high (15–30 percent) growth rates. In terms of its implications for blockchain governance, this result suggests that simply growing the blockchain network by adding high numbers of new nodes will have slightly adverse efects on the integrity of the blockchain. This can be mitigated only if blockchain operators ensure that new nodes entering the network possess a certain amount of currency stake to increase their chances of actually winning validations, rather than just absorbing currency and detracting from other nodes’ chances at winning validations. If this is achieved, high growth rates may have a slight positive efect on decentralisation of decision-making power.

## 5.6.1. 5.7. summary of sensitivity analysis results

Overall, the sensitivity analysis identifies how changes in key blockchain parameters afect decentralisation in PoS blockchains. Specifically, increases in the initial number of nodes, transaction amount, and transaction volume positively afect decentralisation and thereby increase the integrity of the blockchain. Increases in transaction fees have a marginal negative efect on decentralisation. The relationship between blockchain network growth rate and decentralisation is non-linear, since very high and very low growth rates are associated with increased decentralisation. The initial stake distribution does not afect decentralisation, except for the highly skewed distribution, which is associated with a decreased level of decentralisation. Table 5 provides statistical validation of the efects of model parameters on decentralisation and Table 6 interprets these results for each model parameter.

Table 5. Regression Results.

<table><tr><td>Variable</td><td>Coefficient</td><td>SE</td><td>t-value</td><td>p-value</td><td>Significance</td></tr><tr><td>Intercept</td><td>1.0309</td><td>0.0080</td><td>128.31</td><td>0.000</td><td>***</td></tr><tr><td>Bimodal</td><td>0.0003</td><td>0.0030</td><td>0.10</td><td>0.919</td><td></td></tr><tr><td>Normal</td><td>0.0025</td><td>0.0030</td><td>0.82</td><td>0.411</td><td></td></tr><tr><td>PowerLaw-1</td><td>0.0030</td><td>0.0030</td><td>0.96</td><td>0.337</td><td></td></tr><tr><td>PowerLaw-2</td><td>0.0015</td><td>0.0030</td><td>0.48</td><td>0.635</td><td></td></tr><tr><td>Skewed</td><td>0.0394</td><td>0.0030</td><td>12.77</td><td>0.000</td><td>***</td></tr><tr><td>Uniform</td><td>-0.0019</td><td>0.0030</td><td>-0.61</td><td>0.544</td><td></td></tr><tr><td> $\ln(A_0)$ </td><td>-0.0067</td><td>0.0006</td><td>-11.04</td><td>0.000</td><td>***</td></tr><tr><td> $\ln(F)$ </td><td>0.0015</td><td>0.0006</td><td>2.49</td><td>0.013</td><td>*</td></tr><tr><td> $\ln(U)$ </td><td>-0.0244</td><td>0.0006</td><td>-40.28</td><td>0.000</td><td>***</td></tr><tr><td> $\ln(V)$ </td><td>-0.0082</td><td>0.0006</td><td>-13.52</td><td>0.000</td><td>***</td></tr><tr><td> $\ln(G)$ </td><td>0.0451</td><td>0.0025</td><td>18.23</td><td>0.000</td><td>***</td></tr><tr><td> $\ln(G)^2$ </td><td>-0.0052</td><td>0.0003</td><td>-18.05</td><td>0.000</td><td>***</td></tr></table>

R<sup>2</sup> = 0.729.  
Significance: \*\*\* p<0.001, \*\* p<0.01, \* p<0.05.  
Notes: The dependent variable is the Gini coeficient, where higher values represent greater centralisation and lower values represent greater decentralisation. Therefore, coeficients that are negative are interpreted as increasing decentralisation of decision-making power.

Table 6. Model Parameter Efects on Decentralisation of Decision-Making Power.

<table><tr><td>Model Parameter</td><td>Summary of Results</td></tr><tr><td colspan="2">Design Parameters</td></tr><tr><td>Initial stake distribution (B)</td><td>The decentralisation of decision-making power is not affected by changes in initial stake distribution, except for stake distributions that are very highly skewed (e.g., one node possessing 90% of the total stake), in which case the centralization of decision-making power increases.</td></tr><tr><td>Initial number of nodes ( $A_0$ )</td><td>The decentralisation of decision-making power increases with a higher number of potential validator nodes available at the genesis of the blockchain.</td></tr><tr><td>Transaction fee (F)</td><td>The decentralisation of decision-making power decreases marginally with higher average transaction fees.</td></tr><tr><td colspan="2">Behavioral Parameters</td></tr><tr><td>Transaction amount (U)</td><td>The decentralisation of decision-making power increases with larger average transaction amounts.</td></tr><tr><td>Transaction volume (V)</td><td>The decentralisation of decision-making power increases with a higher average transaction volume per block.</td></tr><tr><td>Blockchain network growth rate (G)</td><td>The decentralisation of decision-making power increases with either very high or very low blockchain network growth rates.</td></tr></table>

## 5.7. Further scenario testing

Having established the main efects of each of the model parameters, we can now explore various scenarios that can be expected to yield greater degrees of decentralisation. First, we tested a “better design” scenario in which we only use design-related model parameters, that is, parameters that are directly accessible to manipulation in the design of blockchain systems. This is to explore how much decentralisation might have been achievable by a PoS blockchain given its actual use context (i.e., in terms of transaction amounts, transaction volume and organic network growth rate) if the blockchain model parameters were set to levels that could achieve greater decentralisation. Next, we move onto testing a “best-case” scenario by setting all model parameters (i.e., including the behavioural parameters) to settings that yielded positive efects on decentralisation. This is to establish the conditions under which decentralisation might best flourish and to estimate the extent of decentralisation one might expect to achieve if the blockchain operator could also induce maximal decentralisation producing behaviours (within the range of the parameter settings explored in the sensitivity analysis), such as setting the blockchain use context to one where average transactions amounts are very high $( \mathrm { e . g . } ,$ by setting the application domain to contexts such as financial settlements where average transaction amounts are high) and the network growth rate is contained (e.g., by controlling the entry of new nodes onto the network such as in permissioned blockchains).

The “better design” scenario uses settings for blockchain design parameters that yield the highest positive main efects on decentralisation under the assumption that they will be mutually reinforcing (or at least not cancelling each other out) to produce a substantial increase in the degree of decentralisation. More specifically, the design parameters (i.e., initial stake distribution, initial number of nodes, and average transaction fee) were set to maximally efective settings, but the behavioural parameters (i.e., transaction amount, transaction volume, and blockchain network growth) remained at levels that match the model baseline. Given the lack of impact of diferent initial stake distributions, apart from the skewed distribution which had an adverse efect, we set the initial stake distribution (B) as the model baseline; the initial number of nodes $\left( A _ { 0 } \right)$ was set to 730 at 1,000 percent of the model baseline; transaction fees (F) were kept at 5 percent of the baseline value equivalent to 21 NXT per transaction. While behavioural parameters such as transaction amount and volume might be stimulated through ongoing blockchain governance, they are outside the immediate scope of blockchain design. Given that the point of this exercise is to simulate the direct efects that design decisions might have on decentralisation of decision-making power, the behavioural parameters were fixed at the model baseline. Specifically, average transaction amount (U) was set to 39,434 units of currency on average per transaction, transaction volume (V) to an average of 2.54 transactions per block, and the blockchain network growth rate (G) to a 0.03 (3 percent) increase in the number of nodes per block. Overall, as can be seen in Figure 9, optimising the design parameters proved to produce a substantial improvement in overall decentralisation (Gini ≈0.89) as compared to the model baseline (Gini ≈0.97).

![](/api/attachments/QSQTXXE2/fulltext/images/81209e408ddb327724005e3a1d2f3d7887dd7209f372c201fdf4c8a941dc3154.jpg)  
Figure 9. Decentralisation Scenario Simulations.

Next, we explored the “best case” scenario where both design and behavioural parameters were set to maximally efective settings (within the bounds of the parameter settings used in the sensitivity analysis). We based the specific parameter values for the scenario on our results from the sensitivity analysis so that the initial stake distribution (B) was set at the baseline and initial number of nodes $\left( A _ { 0 } \right)$ was set to 730, or 1,000 percent of the model baseline of 73 initial nodes. This was the setting that produced the highest positive main efect, all else being equal. Similarly, the average transaction fee per block (F) was set to the lowest simulated setting at 21 units of currency, or 5 percent of the model baseline of 414 units of currency received by the validator node. Under the assumption that nodes with suficient stake by default participate as potential validators, this might allow for more new potential validator nodes to stand a chance to win the right to validate and thereby lead to more decentralisation. As transaction amount (in terms of the average currency amount in each transaction) displayed relatively large positive efects on decentralisation of decision-making power, average transaction amount (U) was set to the maximum value of 394,340 units of currency at 1,000 percent of the model baseline. At an approximate value of USD 17,913 (using the median exchange rate for the first 120,000 blocks of the NXT blockchain), this is a very large amount to send on average across all transactions and therefore warrants consideration about the context in which the blockchain is implemented. With a large average transaction amount, transaction volume (V) must be kept at or near the model baseline – despite the fact that it shows some positive efect on decentralisation – because a maximum setting for transaction volume in combination with large average transaction amounts comes too close to the market capitalisation of the blockchain to be computationally feasible. We chose to simulate the maximum setting for transaction amount rather than transaction volume, since it shows a greater positive efect on decentralisation of decision-making power. Given that the blockchain network growth rate has a negative efect on decentralisation of decision-making power, we kept this parameter (G) at its lowest setting of 0.0015, or 5 percent of the model baseline at 0.03. Overall, the results show a profound efect in terms of increasing decentralisation. As shown in Figure 9, the Gini coeficient for the “best case” scenario indicates a slight linear increase from approximately 0.78 to around 0.81, whereas the model baseline converges on a significantly higher value (Gini ≈0.97).

## 6. Discussion and Conclusion

Blockchain is a disruptive and transformational force, but the realisation of its potential is highly contingent upon decentralisation of decision-making power. Decentralisation is critical for blockchain integrity and a key factor if blockchain is to fulfill its promise of removing trusted third parties. In this paper, we study how decision-making power in PoS blockchains becomes decentralised. We find that a high number of initial potential validator nodes, large transactions, and a high number of transactions increase the degree of decentralisation. Our results also suggest that a very high or very low positive network growth rate increases the degree of decentralisation. We only find weak support for an impact of changes in transaction fees and initial stake distributions on the degree of decentralisation.

We contribute to the emerging literature on the PoS consensus mechanism. Roşu and Saleh (2021) find that for stable block rewards, the rich do not get richer. Our analysis confirms their results; our findings suggest that the degree of decentralisation converges to a stable level with stable block rewards. Our study complements the study of Irresberger (2018), who focuses on the trade-of between coin inflation and decentralisation, by studying PoS blockchains without inbuilt inflation. We also go beyond Irresberger (2018) in that we investigate the efects of changes in numerous key parameters on the degree of decentralisation, instead of focusing on one specific trade-of. Overall, our findings contribute to a better understanding of the factors driving the decentralisation of decisionmaking power in PoS blockchains, and can be applied to promote the decentralisation of decision-making power, thereby making PoS blockchains less prone to attacks and more secure. In the following, we will discuss design implications of our study, as well as limitations and avenues for future research.

## 6.1. Design implications

Our study provides implications for blockchain system design. With regard to the design parameters (i.e., initial stake distribution, initial number of nodes, and average transaction fee), we can derive several insights. To achieve high levels of decentralisation, those setting up new PoS blockchain systems need to ensure the systems are initiated with a high number of potential validator nodes. To attract potential validator nodes before the launch of a blockchain systems, the initiators could advertise to relevant stakeholders and run a test network to allow interested stakeholders to familiarise themselves with the blockchain system. They could also ofer financial rewards by selling stake at a discount to those willing to participate in transaction validation already from the system launch. Our findings also suggest that highly skewed initial stake distributions, in which a single person or group owns most of the stake, pose a centralisation risk. In many cases, blockchain systems are initiated by a single individual or small group. Even though there may be an initial incentive for this person or group to retain most of the stake themselves, to ensure the longterm feasibility of the blockchain system, they should foster decentralisation by selling of a significant portion of their stake before the blockchain launch. In line with prior research (Roşu and Saleh, 2021), we find that changes in transaction fees only have a marginal impact on the degree of decentralisation. Therefore, design choices with respect to this parameter appear to not be critical for the decentralisation of the blockchain system.

With regard to the behavioural parameters (i.e., transaction amount, transaction volume, and network growth), those setting up new PoS blockchain systems have only limited possibilities of manipulation. In particular, this is the case for transaction amount and transaction volume. On the other hand, blockchain network growth is to some extent available for manipulation. We find that high network growth will have slightly adverse efects on the degree of decentralisation. To mitigate this, the blockchain initiators could increase the barriers to access for new nodes joining the network by setting up a permissioned blockchain. Such blockchains are characterised by restricted access for potential validators, and can vir tually guarantee a certain degree of decentralisation (Bakos et al., 2021). However, this is not feasible for PoS blockchain systems, since validation rights are tied to stake ownership, and stake can be acquired be anyone. Moreover, in many blockchain projects open access is highly desired, since a permissioned blockchain requires a central gatekeeper to grant access to transaction validation, which in turn introduces another centralisation vulnerability. A more promising approach to curbing network growth may be to require nodes to own a large amount of stake to be eligible for validation. However, this would exclude less powerful nodes from having a chance to validate transactions, and may therefore also not be an option for many blockchain network designers, who often emphasise inclusivity.

## 6.2. Limitations and future research

Our research has a number of limitations representing important avenues for future research. First, our study focuses on analysing the main efects of salient parameters in the blockchain, while interaction efects are not studied in detail. However, we analysed interaction efects by conducting scenario testing, in which we manipulate several parameters at the same time to study the combined efects on the degree of decentralisation. Our results suggest that both a “best-case” scenario, in which all parameters were set to yield a high degree of decentralisation, and a “better design” scenario, in which all parameters which can be manipulated through design choices were set to yield a high degree of decentralisation, are associated with substantial increases in decentralisation. Even though our analysis does not suggest that the efects are cancelling each other out, future research could investigate these issues in more detail, discerning if there are interaction efects and whether their nature is reinforcing or balancing.

Second, our work only analyzes the PoS consensus mechanism. While we do believe that PoW with its energy expenditure may not be sustainable, less common variants of PoS have sprung up, such as delegated PoS, in which all nodes have voting rights (weighted by stake size) that they use to vote for a limited number of validator nodes. Our findings do not necessarily apply for such cases. However, PoS is the most common alternative to PoW, and indeed the most common consensus mechanism in newly launched blockchains (Irresberger et al., 2021). Since extant research mostly focuses on PoW, we believe more research on PoS is urgently needed; our paper contributes to addressing this research need. We also believe our work can be used as a guiding framework to study variants of PoS. The reason is that agentbased simulations could be used to study how blockchain systems based on consensus mechanisms such as delegated PoS become centralised or decentralised, depending on the node behaviour and design choices. Another recently emerging type of stake-based voting is on-chain blockchain governance, where nodes can vote on governance proposals, such as changes to the consensus mechanism design itself (Tsoukalas & Falk, 2020). This phenomenon is also beyond the scope of our paper.

Third, our measure for the distribution of decisionmaking power in blockchains allows for only limited insights with respect to the concrete implications for blockchain integrity. Changes in the distribution of decision-making power can only reveal general tendencies in terms of their efects on blockchain integrity, yet we do not identify critical levels of centralisation. Our conceptualisation of the efect centralisation of decision-making power has on blockchain integrity is, however, in line with the notion that the greater the relative decision-making power one node obtains, the more likely it is that its attack succeeds.

## Notes

1. https://ethereum.org/en/developers/docs/consensusmechanisms/pos/.

2. A recent paper argues that there has been some confusion regarding the distinction between decentralisation and distribution (Vergne, 2020). Therefore, we will also clarify how we use the term distribution in this paper. First, we use the term to describe computing environments that rely on multiple computers that are connected on a network (such as distributed systems and distributed databases). Note that such distributed computing architectures do neither preordain centralisation or decentralisation (of decisionmaking power). Second, we use the term to refer to how a resource is dispersed across a population (as in wealth distribution or income distribution). In this paper, we focus on the distribution of decision-making power among computing nodes. Note that the use of the term distribution does not imply how decision-making power is dispersed – for this we use the terms centralisation and decentralisation. While our use of the term difers from Vergne’s (2020), it adheres to long-established norms in computer science and economics.

3. A natural experiment could potentially also be suitable to study how changes in behaviour and design choices afect the degree of decentralisation of decision-making power. However, using the CAS perspective in conjunction with agent-based simulations has the advantage of allowing for probing several interventions in parallel and afording control with respect to the kind of intervention being studied.

4. https://nxtplatform.org/.

## Acknowledgements

We would like to thank the Senior Editor, Associate Editor, and the three anonymous referees for a fast and constructive review process.

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## ORCID

Christoph Mueller-Bloch http://orcid.org/0000-0002- 3738-2167

## References

Alsabah, H., & Capponi, A. (2020). Pitfalls of bitcoin’s proof-of-work: R&D arms race and mining centralization. Working paper, Columbia University.

Andersen, J. V., & Bogusz, C. I. (2019). Self-Organizing in blockchain infrastructures: generativity through shifting objectives and forking. Journal of the Association for Information Systems, 20(9), 1242–1273. https://doi.org/ 10.17705/1jais.00566

Arnosti, N., & Weinberg, S. M. (2022). Management Science, 68(7): 4755–4771. https://doi.org/10.1287/mnsc.2021. 4095

Azouvi, S., Maller, M., & Meiklejohn, S. (2018). Egalitarian society or benevolent dictatorship: The state of cryptocurrency governance. In International Conference on Financial Cryptography and Data Security (pp. 127–143). Springer, Berlin, Heidelberg.

Bakos, Y., Halaburda, H., & Mueller-Bloch, C. (2021). When permissioned blockchains deliver more decentralization than permissionless. Communications of the ACM, 64(2), 20–22. https://doi.org/10.1145/3442371

Bano, S., Sonnino, A., Al-Bassam, M., Azouvi, S., McCorry, P., Meiklejohn, S., & Danezis, G. (2017). Consensus in the age of blockchains. Working paper,

University College London and The Alan Turing Institute.

Beck, R., Müller-Bloch, C., & King, J. L. (2018). Governance in the blockchain economy: A framework And research agenda. Journal of the Association for Information Systems, 19(10), 1020–1034. https://doi.org/10.17705/ 1jais.00518

Benetton, M., Compiani, G., & Morse, A. (2021). When cryptomining comes to town: high electricity-use spillovers to the local economy. Working paper, University of California.

Biais, B., Bisière, C., Bouvard, M., & Casamatta, C. (2019). The blockchain folk theorem. The Review of Financial Studies, 32(5), 1662–1715. https://doi.org/10.1093/rfs hhy095

Bloomfield, B. P., & Coombs, R. (1992). Information technology, control and power: The centralization and decentralization debate revisited. Journal of Management Studies, 29(4), 459–484. https://doi.org/10.1111/j.1467- 6486.1992.tb00674.x

Bonabeau, E. (2002). Agent-Based modeling: Methods and techniques for simulating human systems. Proceedings of the National Academy of Sciences, 99(3), 7280–7287.

Bonneau, J. (2018). Hostile blockchain takeovers (short paper). International Conference on Financial Cryptography and Data Security, Nieuwpoort, Curaçao. (pp. 92–100). Springer.

Carlsten, M., Kalodner, H., Weinberg, S. M., & Narayanan, A. (2016). On the instability of bitcoin without the block reward. Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security, Vienna, Austria (pp. 154–167).

Catalini, C., & Gans, J. S. (2020). Some simple economics of the blockchain. Communications of the ACM, 63(7), 80–90. https://doi.org/10.1145/3359552

Cennamo, C., Marchesi, C., & Meyer, T. (2020). Two sides of the same coin? Decentralized versus proprietary blockchains and the performance of digital currencies. Academy of Management Discoveries, 6(3), 382–405.

Clemons, E. K., Dewan, R. M., Kaufman, R. J., & Weber, T. A. (2017). Understanding the information-based transformation of strategy and society. Journal of Management Information Systems, 34 (2), 425–456. https://doi.org/10.1080/07421222.2017. 1334474

Cong, L. W., He, Z., & Li, J. (2021). Decentralized mining in centralized pools. The Review of Financial Studies, 34(3), 1191–1235. https://doi.org/10.1093/rfs/hhaa040

Constantinides, P., Henfridsson, O., & Parker, G. (2018). Introduction—platformS and infrastructures in the digital age. Information Systems Research, 29(2), 381–400. https://doi.org/10.1287/isre.2018.0794

Conti, M., Kumar, E. S., Lal, C., & Ruj, S. (2018). A survey on security and privacy issues of bitcoin. IEEE Communications Surveys & Tutorials, 20(4), 3416–3452. https://doi.org/10.1109/COMST.2018.2842460

Drazin, R., & Sandelands, L. (1992). Autogenesis: A perspective on the process of organizing. Organization Science, 3(2), 230–249. https://doi.org/10. 1287/orsc.3.2.230

Ein-Dor, P., & Segev, E. (1978). Centralization, decentralization and management information systems. Information & Management, 1(3), 169–172. https://doi. org/10.1016/0378-72067890004-6

Epstein, J. M. (2006). Generative social science: Studies in agent-based computational modelling. Princeton University Press.

Gastwirth, J. L. (1972). The estimation of the Lorenz curve and gini index. The Review of Economics and Statistics, 54 (3), 306–316. https://doi.org/10.2307/1937992

Gell-Mann, M. (1994). Complex adaptive systems. In G. Cowan, D. Pines, & D. Meltzer (Eds.), Complexity: Metaphors, models, and reality (pp. 17–29). Addison-Wesley.

Gervais, A., Karame, G. O., Wüst, K., Glykantzis, V., Ritzdorf, H., & Capkun, S. (2016). On the security and performance of proof of work blockchains. In Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security (pp. 3–16).

Haki, K., Beese, J., Aier, S., & Winter, R. (2020). The evolution of information systems architecture: an agent-based simulation model. MIS Quarterly, 44(1), 155–184. https:// doi.org/10.25300/MISQ/2020/14494

Halaburda, H., & Mueller-Bloch, C. (2020). Toward a multidimensional conceptualization of decentralization in blockchain governance: Commentary on “two sides of the same coin? decentralized versus proprietary blockchains and the performance of digital currencies” by cennamo, Marchesi, and Meyer. Academy of Management Discoveries, 6(4), 712–714. https://doi.org/ 10.5465/amd.2020.0134

Holland, J. H. (1992). Adaptation in Natural and Artificial Systems: An Introductory Analysis with Applications to Biology, Control, and Artificial Intelligence. MIT Press.

Holland, J. H. (1995). Hidden Order: How Adaptation Builds Complexity. Addison-Wesley.

Hsieh, Y. Y., Vergne, J. P., Anderson, P., Lakhani, K., & Reitzig, M. (2018). Bitcoin and the rise of decentralized autonomous organizations. Journal of Organization Design, 7(1), 1–16. https://doi.org/10.1186/s41469-018-0038-1

Irresberger, F. (2018). Coin concentration of proof-of-stake blockchains. Working paper, Durham University.

Irresberger, F., John, K., & Saleh, F. (2021). The public blockchain ecosystem: An empirical analysis. Working paper, New York University Stern.

King, J. L. (1983). Centralized versus decentralized computing: Organizational considerations and management options. ACM Computing Surveys (CSUR), 15(4), 319–349. https://doi.org/10.1145/289.290

King, S., & Nadal, S. (2012). Ppcoin: Peer-to-peer crypto-currency with proof-of-stake. self-published paper, August, 19(1).

Klügl, F. (2008). A validation methodology for agent-based simulations. In Proceedings of the 2008 ACM Symposium on Applied Computing (pp. 39–43).

Kroll, J. A., Davey, I. C., & Felten, E. W. (2013). The economics of bitcoin mining, or bitcoin in the presence of adversaries. In Proceedings of the Twelfth Workshop on the Economics of Information Security.

Lerman, R. I., & Yitzhaki, S. (1984). A note on the calculation and interpretation of the Gini index. Economic Letters, 15(3–4), 363–368. https://doi.org/10.1016/0165- 17658490126-5

Litchfield, J. A. (1999). Inequality: Methods and tools. World Bank, available at: https://siteresources.world bank.org/INTPGI/Resources/Inequality/litchfie.pdf

Lumineau, F., Wang, W., & Schilke, O. (2021). Blockchain governance—a new way of organizing collaborations? Organization Science, 32(2), 500–521. https://doi.org/10. 1287/orsc.2020.1379

Markus, M. L., & Bjørn-Andersen, N. (1987). Power over users: Its exercise by system professionals. Communications of the ACM, 30(6), 498–504. https:// doi.org/10.1145/214762.214764

Miller, J. H., & Page, S. E. (2009). Complex Adaptive Systems: An Introduction to Computational Models of Social Life. Princeton University Press.

Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system. White paper, available at https://bitcoin.org/bit coin.pdf .

Nan, N. (2011). Capturing bottom-up information technology use processes: A complex adaptive systems model. MIS Quarterly, 35(2), 505–532. https://doi.org/10.2307/23044054

Nan, N., & Tanriverdi, H. (2017). Unifying the role of IT in hyperturbulence and competitive advantage via a multilevel perspective of is strategy. MIS Quarterly, 41 (3), 937–958. https://doi.org/10.25300/MISQ/2017/41.3.12

Peters, D. H. (2014). The application of systems thinking in health: Why use systems thinking? Health Research Policy and Systems, 12(1), 1–6. https://doi.org/10.1186/1478- 4505-12-51

Risius, M., & Spohrer, K. (2017). A blockchain research framework. Business & Information Systems Engineering, 59(6), 385–409. https://doi.org/10.1007/s12599-017-0506-0

Rivkin, J. W., & Siggelkow, N. (2007). Patterned interactions in complex systems: Implications for exploration. Management Science, 53(7), 1068–1085. https://doi.org 10.1287/mnsc.1060.0626

Rossi, M., Mueller-Bloch, C., Thatcher, J. B., & Beck, R. (2019). BlockchAin research in information systems: Current trends and an inclusive future research agenda. Journal of the Association for Information Systems, 20(09), 1390–1405.

Sai, A. R., Buckley, J., Fitzgerald, B., & Le Gear, A. (2021). Taxonomy of centralization in public blockchain systems: A systematic literature review. Information Processing & Management, 58(4), 102584. https://doi.org/10.1016/j. ipm.2021.102584

Saleh, F. (2021). Blockchain without waste: Proof-of-stake. The Review of Financial Studies, 34(3), 1156–1190. https://doi.org/10.1093/rfs/hhaa075

Sambamurthy, V., & Zmud, R. W. (1999). Arrangements for information technology governance: A theory of multiple contingencies. MIS Quarterly, 23(2), 261–290. https://doi. org/10.2307/249754

Schelling, T. C. (1969). Models of segregation. The American Economic Review, 59(2), 488–493.

Shanaev, S., Shuraeva, A., Vasenin, M., & Kuznetsov, M. (2019). Cryptocurrency value and 51% attacks: Evidence from event studies. The Journal of Alternative Investments, 22(3), 65–77. https://doi.org/10.3905/jai.2019.1.081

Siggelkow, N., & Levinthal, D. A. (2003). Temporarily divide to conquer: Centralized, decentralized, and reintegrated organizational approaches to exploration and adaptation. Organization Science, 14(6), 650–669. https://doi.org/10. 1287/orsc.14.6.650.24840

Tiwana, A., Konsynski, B., & Bush, A. A. (2010). Research commentary—platform evolution: Coevolution of platform architecture, governance, and environmental dynamics. Information Systems Research, 21(4), 675–687. https://doi.org/10.1287/isre.1100.0323

Tsoukalas, G., & Falk, B. H. (2020). Token-Weighted crowdsourcing. Management Science, 66(9), 3843–3859. https://doi.org/10.1287/mnsc.2019.3515

Vergne, J. P. (2020). Decentralized vs. distributed organization: Blockchain, machine learning and the future of the digital platform. Organization Theory, 1(4), 1–26. https:// doi.org/10.1177/2631787720977052

Weill, P., & Ross, J. W. (2004). IT governance: How top performers manage IT decision rights for superior results. Harvard Business Press.

World Bank Institute (2005). Introduction to poverty analysis, available at http://siteresources.worldbank.org/ PGLP/Resources/PovertyManual.pdf

Zachariadis, M., Hileman, G., & Scott, S. V. (2019). Governance and control in distributed ledgers: Understanding the challenges facing blockchain technology in financial services. Information and Organization, 29(2), 105–117. https://doi.org/10.1016/j.infoandorg. 2019.03.001

Zhang, J., Adomavicius, G., Gupta, A., & Ketter, W. (2020). Consumption and performance: Understanding longitudinal dynamics of recommender systems via an agent-based simulation framework. Information Systems Research, 31(1), 76–101. https://doi.org/10.1287/isre. 2019.0876

## APPENDIX A. MODEL PSEUDO CODE

```txt
INPUT:
\\ All input multipliers vary from 0.05 to 100 and are applied to the 5 parameters.

    initial_validator_multiplier
    fee_multiplier,
    send_amount_multiplier,
    transactions_per_block_multiplier,
    current_validator_count_multiplier

CONSTANTS:
\\ All constants are variables that do not change throughout the simulation

    total_stake \\ total stake that exists in the blockchain

GLOBAL VARIABLES:
\\ Global variables are updated throughout the simulation and help maintain the state of the blockchain.

    current_block \\ current state of the blockchain
    timestamp = 0 \\ time in seconds since the first block
    previous_timestamp = the timestamp taken from the previous block

Function simulate_blockchain(input)
\\ This runs the simulation using the classes and functions defined

    simulation_model = new Model(input) \\ creates an instantiation of the model class
    FOR i in 1 to 120000
    simulation_mode.model_step() \\ calls the model_step function for each block
    ENDFOR

class Model(initial_validator_multiplier, fee_multiplier, send_amount_multiplier, transactions_per_block_multiplier, current_validator_count_multiplier)

    previous_generation_signature = DEFAULT NXT VALUE
    base_target = DEFAULT NXT VALUE
    previous_base_target = DEFAULT NXT VALUE
    Initial_validator_count = DEFAULT NXT VALUE * initial_validator_multiplier
    average_fee = DEFAULT NXT VALUE * fee_multiplier
    average_send_amount = DEFAULT NXT VALUE * send_amount_multiplier
    average_transactions_per_block = DEFAULT NXT VALUE * transactions_per_block_multiplier
    needed_validator_count= current_block * current_validator_count_multiplier
    agent_validator_list = [ ]

    FOR 1 to initial_validator_count
    agent_validator_list.append(new Agent(total_stake / initial_validator_count))
    ENDFOR

Function model_step()
\\ Each step in the model simulates a single block in the blockchain

    FOR each Agent in agent_validator_list
    Agent.agent_step() \\ Calls the agent_step function of each agent
    ENDFOR

    create_transactions()
    validate_block(current_block) \\ Rewards the agent with the highest decision-making power
    current_block += 1 \\ Increments the counter variable of the current block

Function create_transactions()
\\ Creates all transactions for current block

    FOR each transaction in average_transactions_per_block
    create_transaction(average_fee, average_send_amount)
    \\ Stake is redistributed by creating a transaction where the sender/recipient is randomly selected unless the needed_validator_count does not match, in which the transaction will go to a new user
    ENDFOR

Class Agent(initial_stake)
\\ Each agent simulates a validator in the blockchain

    stake = initial_stake
public_key \\ A unique identifier for this agent
generation_signature \\ A hash of the previous generation signature and public_key
hit \\ each agent has a unique hit which is highly random integer
decision_power = 1000000.0 / hit / stake
hit_time = hit / stake

Function agent_step()
\\ Recalculate the hit in order to recalculate the decision-making power of an individual agent

    hit = calculate the hit using the previous generation signature and the agent public_key
target = stake * base_target
hit_time = hit / target
decision_power = 1000000.0 / hit / target
```
