---
otero_id: 10506
otero_key: "UAK665F4"
title: "Is code law? Current legal and technical adoption issues and remedies for blockchain-enabled smart contracts"
authors: "Daniel Drummer; Dirk Neumann"
year: "2020"
journal: "Journal of Information Technology"
doi: "10.1177/0268396220924669"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research Paper

# Is code law? Current legal and technical adoption issues and remedies for blockchain-enabled smart contracts

Daniel Drummer and Dirk Neumann

Journal of Information Technology 1–24 © Association for Information Technology Trust 2020 Article reuse guidelines: sagepub.com/journals-permissions https://doi.org/10.1177/026839622092466DOI: 10.1177/0268396220924669 Journals.sagepub.com/jinf ⑤SAGE

## Abstract

Blockchain technology has enabled so-called smart contracts between different parties on a decentralized network. These self-enforceable and self-executable computerized contracts could initiate a fundamental paradigm shift in the understanding and functioning of our legal practices. Opportunities for their application are increasingly understood, and numerous tests of feasibility have been completed. However, only very few use cases have yet been implemented at scale. This article—as the first of its kind—comprehensively analyzes the underlying challenges and locates a key reason for the slow adoption in the discrepancy between legal requirements and IT capabilities. Our work combines a wide range of academic sources and interviews with 30 domain experts from IT, the legal domain and private industry. First, we establish that smart contracts still fall within the boundaries of the general legal framework. We then systematically dissect current shortcomings of smart contracts on three distinct levels, namely, (1) how smart contracts are likely to cause conflicts with existing laws, (2) how smart contracts are intrinsically limited on an individual contract level and (3) how they are impeded by their current technical design. Across those levels, we dissect 20 distinct issues concerning the current implementation of smart contracts for which we derive potential remedies. We further outline implications for policy-makers as well as IT management, and examine how information systems research can play an important role in advancing smart contracts. Finally, we show how managerial and organizational issues might represent an ongoing challenge for the widespread adoption of smart contracts.

## Keywords

Blockchain, smart contracts, information systems, legal

Smart contracts [. . .] may well augur new era in contracting practices

—Prof. Sarah Green, Faculty of Law, Oxford University

## Introduction

Smart contracts have been named a central element to the fourth industrial revolution by the World Economic Forum (Schwab, 2016). Smart contracts are, in essence, computer programs that embed the terms and conditions of a contract between two or more parties. By being fully self-enforceable and self-executable, they remove the need for interpretation and subsequent human intervention (Egelund-Müller et al., 2017; Kiviat, 2015; Nofer et al., 2017). Hence, thi represents a radical paradigm shift in the developing understanding of contracts (Künnapas, 2016; Savelyev, 2017) and the ways in which information systems (ISs) interact with one another (Glaser, 2017; Niederman et al., 2017).

There are a number of potential advantages associated with smart contracts compared to the established way of contracting (Avital et al., 2016; Temte, 2019). In theory, smart contracts allow transactions between anonymous parties, without the need for recordkeeping. Since there should be no possibility of fraud, the need for third-party enforcement and other administrative functions is drastically reduced (Kiviat, 2015; Nofer et al., 2017). In consequence, this could establish an unprecedented level of trust and market integrity, a critical ingredient for any well-functioning market infrastructure (Beck et al., 2016; Kiviat, 2015; Siering et al., 2017). Therefore, the implementation of smart contracts based on blockchain technology could lead to the creation and execution of contracts that occur at higher speed, lower costs and more reliability as compared to classical paper contracts (Low and Mik, 2020; Yli-Huumo et al., 2016). On a market structure level, smart contracts could circumvent intermediaries and thus provide direct access to services that are currently highly intermediated, for instance, in the world of banking and financial trading (Cong and He, 2019; Drummer et al., 2017). Accordingly, the industry that first started to consider the potential of smart contracts has been the financial industry (Egelund-Müller et al., 2017; Glaser, 2017; Nofer et al., 2017; Puschmann, 2017; Zavolokina et al., 2017). Potential use cases within the financial industry are manifold and include international payments (Lindman et al., 2017), tax processing and auditing (Hyvärinen et al., 2017), clearing and settlement (Guo and Liang, 2016), verification of financial transactions (Parra Moyano and Ross, 2017) and even more recent developments such as crowdfunding (Al-Saqaf and Seidler, 2017; Kosba et al., 2016). Beyond the financial industry, applications of smart contracts span numerous areas, including real estate (Mashatan and Roberts, 2017), medicine (Dubovitskaya et al., 2017; Zhang et al., 2018), the sharing economy (Huckle, 2016), account ing (Dai and Vasarhelyi, 2017), tourism (Korže, 2019), digital rights management (Bodó et al., 2018; Kishigami et al., 2015) and insurance (Cant et al., 2017; Gatteschi et al., 2018; Hans et al., 2017). Furthermore, smart contracts can facilitate specific tasks of businesses involving the Internet of Things (Christidis and Devetsikiotis, 2016; Novo, 2018; Sultana et al., 2020) or help in optimizing supply chain management (Kim and Laskowski, 2018; Korpel et al., 2017). Altogether, smart contracts promise enormous value creation across industries. For instance, the consulting firm Capgemini estimated that smart contracts could lead to additional revenues of up to US\$19 billion per year in banking alone (Cant et al., 2017)

## Problem statement and research gap

However, despite the initial promises and significant potential of smart contracts across manifold use cases, evidence of smart contracts being utilized at scale by established industry players is rather scarce (Tsai et al., 2019). In light of this intriguing paradox, it seems surprising that there is little empirical evidence available on what challenges are impeding the faster roll-out of smart contracts, despite their evident potential.

To close this gap and contribute to the available body of research, we built upon existing research and consulted a wide panel of IT experts including potential corporate users of smart contracts and academic advisers in this space (see Appendix). The consulted practitioners stem from a broad range of domains, backgrounds and functions within the business. With overwhelming consistency, almost all pointed out considerable challenges due to which smart contracts have not yet gone live in their businesses. Their feedback congruently points toward an array of shortcomings at the intersection of technological capabilities and legal requirements. According to our experts, it is this discrepancy which still fundamentally impedes a faster proliferation of smart contracts.

Hence, this article is the first of its kind to follow an IT-based view aimed at understanding the underlying legal issues that hinder the adoption of smart contracts and locates these issues in the interplay between the domain of technology and law. As such, this article advances the body of research by comprehensively analyzing both the legal dimension of smart contracts as well as technical aspects, following an interdisciplinary approach, and then outlining concrete solutions. We build upon the growing body of IS research pertaining to smart contracts and enrich this with the first available research from the legal domain in a structured manner.

The outline of this article is as follows: The first background section begins with a brief analysis and technical overview of smart contracts and identifies prevailing research gaps. The following section provides an analysis of the legal status of smart contracts and their interrelationship with the established juridical system. Based on this, we analyze where smart contracts will inevitably trigger conflicts with existing laws and then categorize current limitations on a regulatory, contract and technological level. The following discussion section then elaborates on potential public policy approaches, industry solutions and IT remedies to overcome these limitations. After analyzing organizational and managerial implications, this article concludes with an overarching synthesis.

## IT background on smart contracts

This section first reviews the fundamentals of blockchain technology, which has enabled the underlying infrastructure used by current smart contract platforms, and provides an overview of the working principles behind current smart contract technology itself. In addition, we establish a more detailed summary of the existing research streams on smart contracts as a frame for our further analysis.

It is noteworthy that the concept of smart contracts precedes the emergence of blockchain technology, as the term itself can be traced back to the 1990s. In the initial vision, smart contracts were defined as machine-readable transaction protocols which create a contract with predetermined terms and execute the contractual terms of an agreement (Szabo, 1997; Zheng et al., 2020). Yet preceding the emergence of blockchain technology, the critical question around trust and data integrity of the storage and execution of such a program proved to be a non-starter for smart contracts and the idea remained a mostly theoretical concept for more than 15 years. It was, thus, only with the emergence of blockchain technology after 2008 that smart contracts experienced their real-world breakthrough. Given the apparent advantages and superiority in practice, we will therefore focus on blockchain-enabled smart contracts, while acknowledging that smart contracts could theoretically be implemented outside of a blockchain context, albeit with more limited practical scope.

## Underlying blockchain technology

Blockchain technology was first introduced to the public in 2008. In short, it provides a distributed data structure that is replicated and shared among the members of a network (Cong and He, 2019; Tapscott and Tapscott, 2016). It thereby resolves the problem of ensuring the integrity of decentralized networks by using the principles of replication and verification (Cong and He, 2019; Glaser, 2017; Zohar, 2015). This problem of data integrity had been subject to extensive research in the IT discipline and is historically known as the Byzantine consensus problem (Lamport et al., 1982). Replication means that rather than splitting and distributing information among network nodes, each node holds a copy of the entire database. This continuously growing database is kept in sync at all times across the network (Coblenz et al., 2019; Tapscott and Tapscott, 2016; Zohar, 2015). Verification of data integrity is conducted through mathematical methods from the field of computer crypotography to ensure the consistency of such a distributed network. It thereby circumvents the need for central governance by storing data in a sequence of blocks (Casey et al., 2018; Yli-Huumo et al., 2016). The initial use case of blockchain technology resembled a ledger for digital currencies, most notably the cryptocurrency Bitcoin. A growing amount of academic literature is devoted to analyzing and advancing the intricacies of blockchain technology. As of January 2020, the online catalog of Harvard Library lists more than 7000 peer-reviewed articles which explicitly cover blockchain technology.<sup>1</sup> Given the availability of this significant amount of research on blockchain technology in general, we will not expand on this further, but refer to other sources for a more detailed technical description (Avital et al., 2016; Egelund-Müller et al., 2017; Glaser, 2017; Nofer et al., 2017).

## Working principles of smart contracts

Building upon the working principles of blockchain technology described above, a meaningful implementation of decentralized smart contracts eventually became feasible. In 2014, the launch of the Ethereum network first applied blockchain technology far beyond virtual currencies. With

Ethereum as a second-generation blockchain, a number of the previous shortcomings of the Bitcoin scripting language were overcome (Bartoletti and Pompianu, 2017). On Ethereum, it became possible to store data of arbitrary structures and build programs in a Turing-complete programming language (Saraph and Herlihy, 2019; Zheng et al., 2020). Looking at the potential industry-shaping impact of smart contracts, the Harvard Business Review concluded the following in 2017: “Smart contracts may be the most transformative blockchain application at the moment” (Iansiti and Lakhani, 2017).

For the purpose of this article, we define a smart contract as a machine-readable program that is stored on a decentralized network, which will execute itself when a set of predetermined conditions are met and will enforce the contract terms automatically without any human intervention (Clark, 2016). As a result, simple pre-coded contracts can be turned into autonomous units, capable of self-execution and self-enforcement (Künnapas, 2016; Savelyev, 2017). Theoretically, any contractual agreement between two parties could thus be put into code instead of a written legal document (Cong and He, 2019; Kim and Laskowski, 2017; Wright and de Filippi, 2015). Given the features of blockchain technology, there will only be one golden source of truth, which effectively binds both parties. The contracting parties can rely on the fact that the contract will self-execute automatically and neither party is able to unilaterally alter the terms after the initial mutual agreement.

An illustrative example stems from the area of trading, namely, over-the-counter interest rate swaps. Both their settlement process and execution involve a rather lengthy process with multiple parties whereby clearing and settlements often takes several days to be processed (Egelund-Müller et al., 2017). Using smart contracts instead, the execution and settlement of swaps could potentially be fully automated and executed without delay (Low and Mik, 2020). However, despite the technical feasibility and numerous successful proof of concepts, this example has not yet gone live on a meaningfully large scale. Accordingly, this article searches for potential underlying reasons.

## Literature review of smart contracts

The academic literature has only recently started to investigate the field of decentralized smart contracts in detail. A first meta-study from 2016 assessed the state of research on blockchain technology and identified only few papers that specifically dealt with smart contracts (Yli-Huumo et al., 2016). As of January 2020, the body of literature has grown significantly. However, most of the available papers are looking into a specific subaspect of smart contracts. We have included a brief set of relevant references in Table 1, listing some of the most relevant papers on the subject to date. Those sources, together with many others, have formed the basis upon which we have built our further analysis.

Table 1. Overview of relevant works dealing with smart contracts, categorized by technical, (socio-) economic and legal aspects.

<table><tr><td rowspan="2">Source</td><td rowspan="2">Research topic</td><td colspan="3">Focus</td><td rowspan="2">Industry</td></tr><tr><td>Technical.</td><td>Economic</td><td>Legal</td></tr><tr><td>1. Idelberger et al. (2016)</td><td>Scripting language</td><td>√</td><td>√</td><td></td><td>General</td></tr><tr><td>2. Kosba et al. (2016)</td><td>Privacy</td><td>√</td><td></td><td></td><td>Financial industry</td></tr><tr><td>3. Chanson et al. (2017)</td><td>Privacy</td><td>√</td><td></td><td></td><td>General</td></tr><tr><td>4. Nugent et al. (2016)</td><td>Data integrity</td><td>√</td><td></td><td></td><td>Health care</td></tr><tr><td>5. Peters and Panayi (2016)</td><td>Transaction processing</td><td>√</td><td></td><td>√</td><td>Financial industry</td></tr><tr><td>6. Watanabe et al. (2016)</td><td>Security</td><td>√</td><td>√</td><td>√</td><td>General</td></tr><tr><td>7. Juels et al. (2016)</td><td>Security (leakage, theft)</td><td>√</td><td></td><td></td><td>General</td></tr><tr><td>8. Christidis and Devetsikiotis (2016)</td><td>Deployment</td><td>√</td><td>√</td><td></td><td>Internet of Things</td></tr><tr><td>9. Eenmaa-Dimitrieva and Schmidt-Kessen (2019)</td><td>Market structure and trust</td><td></td><td>√</td><td></td><td>General</td></tr><tr><td>10. Venegas and Krabec (2017)</td><td>Market dynamics</td><td></td><td>√</td><td></td><td>Financial industry</td></tr><tr><td>11. Zheng et al. (2020)</td><td>Industry applications</td><td></td><td>√</td><td></td><td>Cross-industry</td></tr><tr><td>12. Wall and Malm (2016)</td><td>Market infrastructure</td><td></td><td>√</td><td></td><td>Financial industry</td></tr><tr><td>13. Hans et al. (2017)</td><td>Market structure</td><td>√</td><td>√</td><td></td><td>Insurance</td></tr><tr><td>14. Al-Saqaf and Seidler (2017)</td><td>Social impact</td><td></td><td>√</td><td></td><td>Finance</td></tr><tr><td>15. Cong and He (2019)</td><td>Market structure</td><td></td><td>√</td><td></td><td>General</td></tr><tr><td>16. Levy (2017)</td><td>Social implications</td><td></td><td>√</td><td>√</td><td>General</td></tr><tr><td>17. O&#x27;Shields (2017)</td><td>Regulatory issues</td><td></td><td></td><td>√</td><td>Financial industry</td></tr><tr><td>18. Frankenreiter (2019)</td><td>Legal status and limitations</td><td></td><td></td><td>√</td><td>General</td></tr><tr><td>19. Lauslahti et al. (2017)</td><td>Contractual practices</td><td></td><td></td><td>√</td><td>General</td></tr><tr><td>20. Koulu (2016)</td><td>Online dispute resolution</td><td>√</td><td></td><td>√</td><td>General</td></tr><tr><td>21. Wright and de Filippi (2015)</td><td>Regulation</td><td></td><td></td><td>√</td><td>General</td></tr><tr><td>22. Tai (2018)</td><td>Unforeseeable circumstances</td><td></td><td></td><td>√</td><td>General</td></tr></table>

These works are categorized by their underlying research stream into technical, (socio-)economic and legal aspects. We observe that, in many cases, these works predominantly garner research agendas and detail open questions that warrant further analysis.

First, economic issues have been raised by various references; for instance, Levy (2017) puts an emphasis on the expected social implications, while Cong and He (2019) and Hans et al. (2017) expect considerable changes in the market structure. One central concept is the notion of trust and the related question how to create market economies in an anonymous, no-trust environment (Eenmaa-Dimitrieva and Schmidt-Kessen, 2019).

Second, in the legal category, we list scholars who have investigated the legal implications of smart contracts in a decentralized network. However, most of them deal with the phenomenon rather in the abstract, raise the general awareness of legal issues in the context of specific domestic legal systems or rather identify future research topics. In general, most of them content themselves with discussing the legality and neglect to identify the interplay with IT, for example, Kiviat (2015); Künnapas (2016); Savelyev (2017). For instance, Kiviat (2015) discusses schemes for regulating blockchain transactions, but merely from a policy viewpoint without fully considering relevant technical capabilities. Similarly, Künnapas (2016) simply conclude with the statement that “the law seems to be not able to address these new appearances.”

Third, IS research has often focused on technical issues of the underlying smart contract-enabling blockchain technology in isolation, such as the lack of privacy, security or scalability and different development standards (Atzei et al., 2017; Christidis and Devetsikiotis, 2016; Coblenz et al., 2019; Destefanis et al., 2018). For example, previous research has developed protocols that allow for preserving data integrity (Nugent et al., 2016) or privacy (Chanson et al., 2017; Kosba et al., 2016) features.

In this context, a panel discussion at International Conference on Information Systems (ICIS) 2016 (Avital et al., 2016) already noted risks with regard to the development of infrastructure, since a platform might be replaced when forks appear.

This article intends to build upon the research agenda established by previous scholars. With the help of our expert interviewee panel, we are, however, taking an interdisciplinary approach looking at the problem at the intersection of economics, law and information technology.

## The relationship between computer code and law

We begin our discussion on the legal status of smart contracts with the notion that the label smart contracts itself already implies a certain assumption which is far from being undisputed, namely, that smart contracts should be considered contracts from a legal perspective. This section sheds light on this critical question which will form the basis of our further discourse. We analyze whether smart questions are part of our established legal system, with its court system, regulation and case law, as well as the underlying principles and written laws. We follow input from our expert partners at leading law firms and discuss the validity of two different view points:

Smart contracts bound by established law: In what way shall smart contracts represent a legally binding contract? (The relationship between smart contracts and a real-world contract)

Smart contracts outside established law: Could smart contracts create a new technology-driven domain outside of our established legal system (A paradigm shift at the horizon: code as law?)?

## The relationship between smart contracts and a real-world contract

The seemingly trivial question about the contractual nature of smart contracts is, in fact, at the heart of the debate (Bourque and Tsui, 2014; Frankenreiter, 2019; Murphy et al., 2016). Two main schools of thought can be distinguished:

In the more mainstream code as representation view, smart contracts are the codified representation of a real-word legal document, containing prose and structured legal lan guage. Even if the counterparties only agree on smart contract code and no separate legal prose exists, the smart contract might be presumed to give rise to a fictional realworld contract which is the basis for all subsequent claims and enforceable in court. In any case, a court would take into consideration the intent of the counterparties beyond the pure computer code (Alces, 2011; Furmston and Tolhurst, 2010).

A subform of the idea of code as representation is a split contract where contractual obligations, remedial and warranties are written into natural language, but some performance triggers, for example, payout upon certain conditions, are encoded into computer code (Wright and de Filippi, 2015). In all cases, the contract terms in the smart contract are leading, but all other governing rules of the jurisdictional system apply as well. This would inevitably create some conflicts which will be discussed later. According to the contrarian code as contract view, the computer code is equivalent to the actual contract that two parties agree on. That is, no other additional agreement beyond the pure code exists. For a better understanding, a parallel, duplicated natural language code of the contract may be created, but legal enforceability is only carried by the computer code (Bodó et al., 2018).

## A paradigm shift on the horizon: code as law?

Some more radical proponents of smart contract technology argue that to judge smart contracts within the confines of our current legal system, as in the views stated above, is flawed to begin with (Waltl et al., 2018; Wang et al., 2019). According to this view, there is no connection between the two domains. Here, code is not only the actual contract but code is law itself, as famously pronounced by Lawrence Lessig (1999, 2006). Lessig had pointed out that developers and software architects make critical choices about the structure of networks and, thus, about rules under which the systems is governed. In a way, architects of the underlying system could therefore replace traditional legislators.

Building upon that idea, smart contracts could allow actors to organize and regulate their relationship without interference from central authorities as a form of self-help (Raskin, 2017). Following from the concept of a general Freedom of Contract (Cornelius, 2018), proponents argue that smart contracts use technology to enforce party autonomy in a more effective manner than the established system with its three-pronged structure of a legislative process, a multi-stage court system and law enforcement authorities, a general structure that has been in existence since the times of the Roman Empire (Hartnell, 2015; Koulu, 2016).

In the future, there could be a competition of systems: the established centralized system, regulated and enforced by public authorities, and a private, self-enforced system, decentralized and organized by code. According to its most vocal proponents and some voices within our expert panel, managing relationships through code has certain advantages over the current legal system, which is inherently prone to errors or human biases and is highly inefficient, with court decisions often taking years. Technology and state law are seen as two different mechanisms of social order. State law may still be important to govern our daily interactions with each other. But, in a private and business context, some proponents expect a competition between legal rules and technical rules, sometimes labeled lex informatica (Reidenberg, 1997) or lex cryptographia (Wright and de Filippi, 2015).

## Why code is (probably) still not law

We now synthesize the previous perceptions of smart contracts based on our interviews and review of the existing literature. In overwhelming agreement across the mainstream opinion, from legal scholars as well as practitioners and legal experts in our interviewee sample, it is highly unlikely that smart contracts would be expected to create a separate realm outside of any state influence (Frankenreiter, 2019). Their arguments can be grouped into pragmatic and principles-based standpoints:

First, from a pragmatic standpoint, political powers throughout the legislature, the executive and the judiciary are not expected to easily give up the state monopoly on the use of force, which is often backed by the constitution. As one interviewee assessed the situation, “Nation states will always have a natural reflex to defend their power and influence. [. . .] They won’t just surrender.” (Filby, 2013). As a case in point, the US Securities and Exchange Commission (USSEC) unambiguously stated the following:

Those who offer and sell securities in the United States must comply with the federal securities laws [. . .] regardless whether the issuing entity is a traditional company or a decentralized autonomous organization, regardless whether those securities are purchased using U.S. dollars or virtual currencies, and regardless whether they are distributed in certificated form or through distributed ledger technology. (USSEC, 2017b)

This underscores the clear understanding that the traditional legal system should have absolute dominion over the use of any smart contract (Eyassu, 2019).

Second, from a principles-based standpoint, an inherent human sense of justice seems to demand the possibility to reverse what is perceived to be clear injustice, that is, a contradiction to the basic norms of our established legal system or human rights. This reasoning seems to also apply to the smart contract world, showcased by the prominent DAO hack in June 2016. Here, hackers had used an undetected loophole in the smart contracts of the online crowdfunding platform The DAO to divert about US\$40 million worth of cryptotokens to another account (Dhillon et al., 2017a; Mehar, 2019; USSEC, 2017b). Thereby, hackers exploited some pieces of code that investors in this company had—technically speaking—agreed on, but which was clearly against their intent and against basic legal norms. After this hack, the Ethereum community decided to conduct a so-called hard fork to reverse the fraudulent transaction and hand the cryptotokens back to the original owners. Hence, this represents a clear contradiction to the code-is-law paradigm. Our interviewees pointed out that, if not even the strongest proponents of the new technology follow a code-is-law paradigm, how much less will the often status quo-preserving institutions (O’Hara, 2017). Hence, our experts conclude that, for the foreseeable future, the current legal and regulatory framework will still apply to any smart contract setting (Giancaspro, 2017). This, in turn, leads to a number of critical issues about the concrete interplay between smart contracts and the legal system, bringing to light existing limitations of smart contracts which we discuss in the following section.

## Legal and technical limitations of smart contracts

The previous section argued that our current legal system still applies to the realm of smart contracts. In other words, smart contracts fall under the dominion of the respective constitutional and legal framework. Hence, this directly triggered concerns among our interviewees about the extent to which the technical capabilities of smart contracts fulfill legal demands. For this reason, we dissect potential legal and technical limitations in current implementations of smart contracts and specifically embed appropriate literature from the legal domain. We follow the framework of so-called nested institutions (Ostrom, 2012) and organize our arguments based on this:

1. The first layer refers to laws and regulations which might be in conflict with smart contracts. Here, the next paragraphs analyze potential areas where issues may arise with regard to states, corporates and individuals.

2. The subsequent layer refers to the contract level. Smart contracts might be an insufficient tool to capture more complex agreements between two parties which we elaborate in the section on intrinsic limitations.

3. On a technical implementation level, the current state-of-the-art public blockchain technology may not yet allow the deployment of decentralized smart contracts at an enterprise-ready scale.

## Limitations on a legal and regulatory level

As long as smart contracts fall within the domain of our current legal system, they are bound by its statutes, laws and regulation. As a result, there are a number of legal areas that could potentially come into conflict with smart contracts. In the following analysis, we highlight key areas which are common across jurisdictions and apply regardless of the specific legal system such as civil law or common law. Based on our expert discussions, we have grouped those by the interactions between different entities where conflicts may arise, namely, state, corporates and individuals (see Table 2). We have illustrated those areas as a relationship matrix. For example, at the intersection where corporate- and state-level interests meet, a potential conflict might arise regarding Securities laws.

State–state. In international law, the respective jurisdiction that should govern a specific smart contract is a critical question. According to established legal practice, the contract usually specifies the governance of laws of a certain country and states an exclusive place of jurisdiction for any disputes. Otherwise, the respective place of jurisdiction would be implied by the residency of the contracting parties. This, however, cannot be applied in a smart contract setting. The unclear domiciling and jurisdiction of a smart contract creates significant uncertainty and the potential for international regulatory arbitrage (a1; Rhim and Park, 2019).

State–corporate. Smart contracts may also be in conflict with Securities Law (a2); for instance, with regard to the recent phenomenon of so-called Initial Coin Offerings (ICOs) which typically rely on the use of smart contracts. Companies and early-stage ventures can attempt to raise funds in exchange for tokens that incorporate certain ownership rights. In many respects, ICOs resemble the issuance of traditional securities, for example, for common stock, which is highly regulated in most jurisdictions (Conley, 2017). Money raised through the crowdfunding of token sales via such ICOs has increased dramatically. In more than 1600 ICOs, at least US\$28 billion have been raised between 2013 and 2018 alone (Domingo et al., 2020; Masiak, 2019). Not surprisingly, the USSEC announced in July 2017 that it would start to investigate the practice of ICOs and take a more restrictive stance in the future: “ [. . .] the offer and sale of these virtual coins or tokens in an ICO are subject to the federal securities laws” (USSEC, 2017a). More recently, in the much-watched Zachary Coburn case, the SEC ruled that tokens issued by the EtherDelta platform were to be considered securities and its smart contract platform represented an exchange according to the Securities Act of 1934 (USSEC, 2018).

Table 2. Limitations on a legal and regulatory level.

<table><tr><td></td><td>State</td><td>Corporate</td><td>Individual</td></tr><tr><td>State</td><td>International law: Unclear domiciling and jurisdiction of smart contracts (a1)</td><td>Securities law: Violation of securities offerings regulations (a2)</td><td>Criminal law: Anonymity prevents criminal action (a3)</td></tr><tr><td>Corporate</td><td>—</td><td>Corporate/trade law: No legal recourse in case of contract breach (a4)</td><td>Consumer protection: Violation of consumer rights (a5)</td></tr><tr><td>Individual</td><td>—</td><td>—</td><td>Civil law: No possibility to reverse void contracts (a6)</td></tr></table>

Potential conflicts arise at the intersection between two entities. For each combination, we first state the applicable area of law, as well as the current shortfall.

Next, data protection regulations such as the prominent EU General Data Protection Regulation (GDPR) might prove especially challenging for the implementation of blockchain technology (Herian, 2018b; Jackson, 2018) and was listed by some interviewees as another point of concern for smart contracts. In most jurisdictions, strict rules apply to specific kinds of data, for example, on ethnic origin, polit ical opinion, religion or health. Discrimination based on those characteristics is often prohibited. In a decentralized environment, however, no single legal entity can be clearly held responsible as data controller. Moreover, many jurisdictions also limit the sharing of data across their borders which is almost impossible to enforce in a global, decentralized blockchain network (Bu-Pasha, 2017; Gutwirth et al., 2016). Again, in the European Union, individuals also have a right to be forgotten and have all their personal data deleted upon request (Gutwirth et al., 2016; Sury, 2019). This remains hardly achievable in a decentralized blockchain network which has data immutability as one of its defining properties (Beck et al., 2016; Tsai et al., 2019).

State–individual. In Criminal Law, concerns center around what happens if an individual enters into a smart contract that is outright illegal such as one related to terrorism or cybercrime. This is critical since current smart contract platforms do not employ any mechanism to determine legality before releasing smart contracts and have no means to retrospectively stop illegal smart contracts from being executed. As one interviewee puts it, this is still, frankly, Wild West territory. A comprehensive paper (Juels et al., 2016) analyzed the issue of criminal smart contracts early on and dissected how those could facilitate leakage of confidential information, theft of cryptographic keys and other crimes such as terrorism. The general notion of the anonymity of smart contracts makes it further challenging for state prosecutors to identify and track down individuals involved in a crime to bring them to court later (a3).

Corporate–corporate. In Corporate Law and Trade Law, our current legal system provides for clear guidelines by regulating the performance requirements and responsibility of a seller in case of malperformance (Brekoulakis and Devaney, 2017). For instance, if the seller is responsible for a late delivery, the buyer might be entitled to receive recompense from the seller (Tai, 2018). However, potential breaches in performance by smart contracts raise the important question of liability; currently, there is no clear answer and the harmed party has no guaranteed rights (a4) (Tai, 2018).

Corporate–individual. Consumer Protection regulation, which aims to ensure the rights of consumers, who are sometimes less educated, is another critical point for smart contracts. For instance, consumer protection has long focused on misrepresentation (Benston, 2000). As a result, customers in most jurisdictions have a right to withdraw from any contract if they have been actively misled. If an individual is being misled or manipulated into a smart contract based on factually incorrect information, however, there is currently no option to withdraw or claim compensation (a5). Even worse, smart contracts rather add to the problem by exponentially increasing the complexity and the consequences of any misunderstanding (Delmolino et al., 2015).

Individual-individual. In many jurisdictions, contracts that are a violation of bonos mores are also void ab initio according to Civil Law, that is, to be treated as if they had never existed (Bix, 2006; Carter, 1980).<sup>2</sup> Some have argued that smart contracts containing flaws that allow individuals to extract money from others would be considered void ab initio by that definition. However, at the moment, there is no possibility to reverse such void contracts (a6).

Table 3. Limitations on a contract level—shortfalls in current smart contract setup.

<table><tr><td></td><td>Current shortfall</td><td>Process step</td></tr><tr><td>b1</td><td>Discrepancy intent and code</td><td>Contract formation</td></tr><tr><td>b2</td><td>Incomplete simulation of future states</td><td>Simulation</td></tr><tr><td>b3</td><td>Potential mismatch between source code vs binary code</td><td>Compilation</td></tr><tr><td>b4</td><td>Lack of context</td><td>Interpretation</td></tr><tr><td>b5</td><td>Reliance on external input</td><td>Execution</td></tr><tr><td>b6</td><td>Limited to electronic enforceability</td><td>Enforcement</td></tr><tr><td>b7</td><td>Lack of contract mutability</td><td>Alteration</td></tr><tr><td>b8</td><td>Lack of arbitration mechanisms</td><td>Dispute</td></tr></table>

## Limitations on a contract level

In summary, across various different areas of our legal system, smart contracts are likely to be in conflict with our established laws and regulation. But even on an individual contract level, there are further intrinsic limitations that limit the ubiquitous application of smart contracts. Many derive from constraints when trying to translate complex legal agreements into a world of binary computer code. To provide a systematic analysis, derived from our interviews with the expert panel, we have contrasted the traditional “contract lifecycle” along five relevant phases, namely, contract formation, compilation, interpretation, execution and enforcement, to a smart contract setting and highlight current shortfalls (see Table 3 for an overview of all identified issues). We further discuss two common events that happen after the initial agreement, namely, the alteration of contract terms and a potential legal dispute.

Contract formation (and simulation for smart contracts). In a traditional setting, lawyers are typically involved in drafting the contract. Their obligation is, not least, to ensure that the legal document reflects the intent of their client and that no existing law is breached. In a smart contract setting, however, lawyers are most often not involved. Further exacerbating the problem, there is a fundamental structural break between agreeing on terms and the actual implementation, written in a programming language such as Solidity.<sup>3</sup> Even if there is a parallel version of the smart contract translated into legal prose, there may be a discrepancy between the legal prose and the smart contract code that is eventually stored on a blockchain platform (b1). In many jurisdictions, there is a fallback such that courts might still follow the underlying intent of the parties at the point of contracting rather than the written word. However, this is something infeasible in a smart contract environment where code always prevails (Furmston and Tolhurst, 2010; Ng, 2017).

In a smart contract setting (only), the simulation phase typically follows, where the contract will perform test runs, simulating different input factors and scenarios (Tsai et al., 2019). This is necessitated since, once agreed, a smart contract cannot be altered afterward. Any potential future event must be foreseen and accounted for in the initial version of the code. Yet technically, computer scientists have long been aware of the halting problem which states that it impossible to determine a priori if an algorithm will halt or run infinitely on some arbitrary input, let alone on all possible inputs (Boyer and Moore, 1984). In other words, any simulation of future states will always remain incomplete, as formally proven by Adam Turing (Reus, 2016) (b2). In contrast, one of the strengths of the legal practice is that it has always been rather probabilistic, not deterministic to also account for unforeseen eventualities.

The following compilation phase is also idiosyncratic to smart contracts. The final smart contract source code needs to be compiled into machine-readable bitcode and uploaded on the blockchain. From then onwards, the binary computer code is the only definitive source of truth for the smart con tract. This, however, also introduces another material structural break. Even if tech-savvy users are able to review the contract source code to verify the terms, there is no guaran tee that the source code provided will actually match the byte code stored on the blockchain. In other words, there is a risk of a potential mismatch between source code and binary code (b3). This is in contrast to a traditional legal document, where the contract terms, written in human prose, will remain the only definitive source of truth and are accessible to third parties (Bhargavan et al., 2016). Even worse, if a contract is only available in its machinereadable compiled code and the underlying source code is not even shared, it is even harder to audit. In fact, Zhou et al. (2018) showed that 77% of all smart contracts stored on the Ethereum platform show such opaqueness.

Interpretation. Once a traditional contract is formed and agreed upon, it remains subject to interpretation. In the traditional understanding of any agreement, legal contractual code is thereby dependent on context. Statutes, legal precedents and principles can be explicitly or implicitly referred to when writing contracts and will play a role within subsequent lawsuits. Certain terms and phrases have been filled with meaning and developed a certain binding interpretation over the years. In contrast, current smart contracts are marked by a complete lack of context (b4). They need to be self-sufficient; therefore, any term or even underlying assumption needs to be explicitly formulated and put into computer code. As one interviewee described the situation, If you genuinely want to create a smart contract as [a] selfstanding tool, you would literally have to code hundreds of years of legal history and court decisions into each contract or set up generally agreed libraries. [. . .] I can’t see any elegant solution for this as of now. Even worse, context may change over time and necessitate a different interpretation some years later, when business conduct or the legal environment might have changed. Furthermore, interpretation of legal documents typically involves certain clauses that make material judgment necessary. For example, common qualitative clauses include material adverse change, good faith or best effort (Garrett, 2010). Those formulations involve human judgment and are a question of degree (Zimmermann and Whittaker, 2000). Sometimes, a determining factor may also be simple common sense. However, coding automated material judgment or formalizing common sense is a very ambitious and mostly unsolved challenge (McCarthy, 1989; Wyatt et al., 2005).

Execution. Following a pre-defined trigger event, a smart contract will execute certain actions. In this context, our experts pointed toward the reliance on external input as a critical condition for adequate performance of smart contracts (b5). However, any outside information can be unreliable, both in terms of availability and accuracy. Data sources can be temporarily incorrect or inaccessible, for instance, when a weather station is out of order or during Internet connection failure. Even more profoundly, if any market gets big enough, it can be worthwhile gaming the system and manipulating the reference data itself, as previous fraud cases around the London Interbank Offered Rate (LIBOR) reference rate have shown (Dooley, 2012). Yet once executed, smart contracts by themselves do not allow for any subsequent recourse in case of fraud or errors in the input data.

Enforcement of contract terms is another critical area. Smart contracts operate in an electronic environment and enforceability is therefore limited to electronically controllable assets (e.g. money that is held in blockchain accounts, software that can be accessed through APIs, connected devices accessible through an IP address, etc.). This has significant ramifications for contracts that involve material payment obligations in a currency outside a blockchain network such as the US dollar. To provide sufficient security, the entire amount of funds needs to be held in an escrow or custodian account, putting enormous constraints on liquidity (b6).

Alteration. A number of experts pointed out that smart contracts are by their nature irreversible after contract terms have been agreed on (b7; Tsai et al., 2019). Unlike any regular software, smart contracts cannot simply be patched (Tikhomirov, 2018). However, in practice, there are often good reasons why contract terms should be altered if all parties agree, for example, to restructure a loan in case of economic difficulties. As Wright and de Filippi point out, people are [. . .] free to decide the particular set of rules to which they want to abide, but after the choice has been made can no longer deviate from these rules, to the extent that smart contracts are automatically enforced by the underlying code of the technology, regardless of the will of the parties (Wright and de Filippi, 2015). This very high degree of certainty is unprecedented in society. As the World Economic Forum noted in its 2017 blockchain White Paper, smart contracts can deliver greater efficiencies and effectively eliminate [. . .] nonperformance risk because we have no choice of breach, no choice of damages. But that’s also a downside. It allows no room for human beings (World Economic Forum, 2017).

Finally, dispute and the right to appeal are a central part of our established legal system. The party that experiences injustice has the option to appeal to a court (Macneil, 1977; Tweeddale and Tweeddale, 2005). In addition, private arbitration according to pre-defined clauses has recently become more common (Brekoulakis and Devaney, 2017). In a smart contract setting, however, those mechanisms are not possible or not yet sufficiently developed (b8).

## Limitations on a technical implementation level

As long as smart contracts rely on blockchain technology, they are also confined by general technical limitations of the underlying blockchain network. Given the available amount of existing literature, we will only briefly elaborate on the most relevant technical issues. In short, they relate to scalability, privacy, security, the lack of unifying standards, the lack of interoperability between different blockchain protocols and open vulnerabilities in the contract code (see Table 4).

With regard to scalability, the most dominant public smart contract platform Ethereum is limited both by maximum throughput as well as latency of data transmission (c1). First, in practice, the potential maximum throughput in the public Ethereum network is currently limited to 20 transactions per second (Chauhan et al., 2018). This is dwarfed by the capabilities of other transaction processing networks, such as VISA, with thousands of transactions per second (Bach et al., 2018; Chauhan et al., 2018; Constantinides et al., 2018). High latency is another concern (Dennis and Disso, 2019). Inherently, any decentralized, fully replicated network will show lower performance than a centralized server (Gatteschi et al., 2018). In the world of financial markets where prices for many assets are being quoted in nanosecond intervals (Gomber and Haferkorn, 2013), a blockchain network with processing times of up to 10–15 min seem to be still out of question.

Table 4. Limitations on a technical implementation level.

<table><tr><td>Area</td><td>Current shortfall</td><td>Explanation</td></tr><tr><td>c1</td><td>Limited scalability</td><td>Limited throughput and high latency of public Ethereum network</td></tr><tr><td>c2</td><td>Privacy concerns</td><td>Anonymity of counterparties cannot be guaranteed</td></tr><tr><td>c3</td><td>Security risks on public blockchains</td><td>Open attack vectors around proof of work mechanisms</td></tr><tr><td>c4</td><td>Lack of unifying standards</td><td>Slower adoption due to a lack of common standards</td></tr><tr><td>c5</td><td>Limited interoperability</td><td>Limited way to connect different architectures</td></tr><tr><td>c6</td><td>Code vulnerabilities</td><td>Exploitable attack vectors in code</td></tr></table>

Furthermore, privacy aspects are another source of concern to many practitioners (c2). On a public blockchain, such as the Ethereum network, all information is by default replicated on all nodes within the network. This implies that, in theory, messages in the blockchain can be read by every network participant. While some argue that users and transactions are anonymous in theory, a number of studies have shown that anonymity is doubtful (Saxena et al., 2014). Individuals and institutions may be identified with only a limited number of data points (Fabian et al., 2016; Moreno-Sanchez et al., 2016). In a financial market setting, where confidentiality of client information is of the utmost importance, any potential leakage of confidential data is an immediate showstopper, according to one interviewee.

When it comes to security, most current blockchain consensus mechanisms rely on proof of work for verification of new blocks (Zheng et al., 2020). That means that whoever controls the majority of computational power will ultimately be able to define and re-write the underlying truth. As such, a public blockchain is vulnerable to a 51% attack where a malicious group of actors would take over the blockchain (Eyal and Sirer, 2013; Xu, 2016). In an extreme case, a single miner node that controls enough computational resources could control the verification of transactions and thus essentially determine the content of a blockchain at will (Xu, 2016). Further out, quantum computing could render current proof of work mechanisms obsolete in their entirety (Xu, 2016; c3).

Lack of unifying standards is also seen as a critical barrier to adoption (c4; Lacity, 2018). With a growing number of diverging blockchain standards and protocols, industry players may be reluctant to invest significant resources into a particular solution until one dominant design has proven itself as superior (Soh, 2010). As one interviewee leading the blockchain efforts at a large global bank remarked, Like most players, we are currently working with [name omitted] out of an array of options. We believe [. . .] is the way forward, but we are unlikely to put all eggs in one basket [. . .] until we know that this will be a mainstream success.

Limited interoperability is another critical impediment, following directly from the above (c5; Lacity, 2018). For now, most implementations remain isolated point solutions. As one interviewee explained, one of the success factors for the rapid spread of the world wide web was that it does not matter which architecture is used on the local end[. . .], because data exchange is governed by unifying protocols such as TCP/IP or FTP. The same cannot be said for blockchain technology. Some pragmatists would concede that, most likely, there will never be one blockchain to rule them all, in the words of Ethereum founder Vitalik Buterin (2016). This is due to the fact that different use cases may, indeed, lend themselves to customized blockchain protocols and architectures. Nevertheless, at the moment, there is limited possibility to connect different systems to each other. This is especially true for more restricted instances of private blockchains, which, by definition, are limited to a few participants and not easily accessible or interoperable with more open architectures, given distinct design choices (Bodó et al., 2018).

Beyond the underlying blockchain infrastructure, there are also a variety of different contract source code languages and scripting syntax in existence (Casey et al., 2018). Given the inherent lack of compatibility, smart contracts written in different languages cannot easily be connected or combined (Schulte et al., 2019).

Code vulnerabilities. Irrespective of the underlying public or private blockchain infrastructure, any given smart contract might contain vulnerabilities in its bytecode or underlying source which leave it exposed to software exploits and attacks (c6; Righi et al., 2020; Wang et al., 2020; Zupan et al., 2020).

## Discussion of remedies and implications

In the previous section, we outlined an array of current shortcomings of smart contracts, relating to legal conflicts, intrinsic contract-level limitations and technical impedi ments. However, in light of the unaltered significant poten tial of smart contracts, some public authorities, private industry players and IS research scholars are actively moving forward to design and build concrete solutions that might overcome some of those shortcomings. These parties could play a pivotal role in furthering the adoption of smart contracts. A number of dedicated projects have been initi ated, aiming to directly address some of the issues outlined above. Hence, the following sections discuss initiatives and ideas that aim to counter and solve previously described shortfalls, namely, from a public policy perspective, from a corporate point of view and from an IS research standpoint.

## Policy implications and public solutions

First, legislators, policy-makers and regulators have recently started to look into the area of smart contracts (Governatori et al., 2018). For instance, some US states, such as Arkansas,<sup>4</sup> Arizona<sup>5</sup>, Nevada<sup>6</sup>, Tennessee<sup>7</sup> and Illinois<sup>8</sup>, have progressively introduced legislation between 2018 and 2020 to permit the usage of smart contracts and clarify their validity in court. Furthermore, national and supranational bodies such as the European Securities and Markets Authority (ESMA), the Bank of England and the British Financial Conduct Authority (FCA) are also increasingly active in the area of smart contracts (ESMA Securities and Markets Stakeholder Group, 2016; Gatteschi et al., 2018; Yeoh, 2017) and have initiated specific research projects dedicated to this topic.

For instance, the FCA, in June 2017, published a discussion paper on distributed ledger technology in which they conclude that there will no doubt be situations where smart contracts may be a useful option (Bauer, 2017). However, regulators are also beginning to consider regulating emerging smart contract regimes more tightly, resembling the example of the previously unregulated cryptocurrency Bitcoin, where financial regulators would quickly catch up with the phenomenon and issue far-reaching know-yourcustomer (KYC) requirements. Illegal Bitcoin networks that facilitated drug trading were shut down, such as the Silk Road platform which was taken down by the FBI in 2013 (Huang, 2015). Similarly, smart contracts may fall under a more restrictive, but at the same time more predictable, regulatory regime in the future (a2; Böhme et al., 2015; Lee et al., 2015). As a result, such regulatory certainty might prompt industry players to implement smart contract solutions with higher confidence. Yet regulating smart contracts is less straightforward than it may seem. It is difficult to regulate the technology itself, given its decentralized nature and contract terms which are stored in a disembodied manner across geographic boundaries. Several potential starting points for public policy have been suggested (see Table 5 for an overview of issues and potential remedies).

To ensure consumer protection, a general smart contract pre-approval could be made mandatory for all consumerfacing smart contracts. For instance, a public authority such as the Federal Trade Commission in the United States could be required to approve all generic smart contracts that are to be offered to US citizens. The object of regulation would be the individual contract or the issuing party behind the contract. Approval could be based on the clarity of the smart contract and the appropriateness of automatic consequences for different kinds of breaches.

In addition, to trace individuals that carry out illegal activities through smart contracts, state regulators could enforce mandatory user identification (a3). Here, the object of regulation is the natural person who wants to participate in a smart contract network. Similar to KYC requirements in the cryptocurrency space, individuals could be forced to undergo mandatory identity verification procedures prior to purchasing any cryptotokens, such as Ether, as a prerequisite to active participation in the smart contract platform Ethereum. Even more broadly, verification could be made mandatory when registering at any smart contract platform, similar to opening a bank account.

Others have proposed the idea of neutralizable or mutable smart contracts as a means of regulation. This means that within a smart contract platform, public or private, a central authority is empowered to view, and even potentially remove a contract from the blockchain (Bourque and Tsui, 2014). This could be necessary in case of a clear contradiction to prevailing law, for example, with regard to consumer protection or criminal law. Related to this objective, the consulting firm Accenture introduced the concept of a blockchain-editing technique (mutability) in September 2016 (Higgins, 2017), providing an option to amend contracts after the initial inception (b7). More invasively, a central governing body could even be granted the authority to neutralize smart contracts in case of clear violations of laws (a6). The respective central authority could be the state regulator for public blockchains or even a consortium of designated agents in a permissioned private blockchain (Bauer, 2017; Beck et al., 2016). However, critical open questions from our interview panel concerned the technical requirements and capacity of central authorities to govern and assess the impact of multitudes of complex computer programs. As one interview partner critically remarked, “I deal with [the domestic financial regulator] on a regular basis. But I can’t see how they would [. . .] review thousands of complex computer programs and come up with a definite judgment.” In addition, the implementation of such a gods-eye right would interfere with the very notion of a decentralized system and may not be easy to implement from a technical perspective (Glaser, 2017).

In the medium term, standard setters may find that international harmonization of rules is the best way to deal with global, decentralized blockchain networks (a1) and decide to partner up across borders (Lewis, 2017). Similar to global private consortia that aim to set technical standards, regulators could decide to form international governing boards, similar to the bodies formed to regulate financial markets, such as the Basel Committee on Banking Supervision. Already existing industry representation groups, such as International Swaps and Derivatives Association (ISDA), may contribute to standard setting (c4) and help the industry to settle on commonly agreed norms.

Table 5. Current limitations of smart contracts, potential remedies and main actor(s) toward a solution.

<table><tr><td></td><td>Limitation</td><td>Potential remedy</td><td>Main actor</td></tr><tr><td colspan="4">Legal and regulatory level</td></tr><tr><td>a1</td><td>Unclear domiciling and jurisdiction</td><td>International harmonization of rules</td><td>Financial regulators</td></tr><tr><td>a2</td><td>Violation of securities offerings regulations</td><td>Expansion of Securities Law to SC</td><td>Financial regulators</td></tr><tr><td>a3</td><td>Anonymity prevents criminal action</td><td>Mandatory identification of SC owners</td><td>Financial regulator/legislator</td></tr><tr><td>a4</td><td>No legal recourse in case of contract breach</td><td>Contract alteration</td><td>Private industry</td></tr><tr><td>a5</td><td>Violation of consumer rights</td><td>Mandatory contract pre-approval</td><td>Financial regulator</td></tr><tr><td>a6</td><td>No possibility to reverse void contracts</td><td>Neutralizable SCs</td><td>IS research</td></tr><tr><td colspan="4">Contract level</td></tr><tr><td>b1</td><td>Discrepancy intent and code</td><td>SC templates; novel sources language</td><td>Private industry (R3, Barclays)</td></tr><tr><td>b2</td><td>Incomplete simulation of future states</td><td>Mathematical verification of smart contracts</td><td>IS research, private industry</td></tr><tr><td>b3</td><td>Potential mismatch between source code and binary code</td><td>Solidity decompiler</td><td>Private industry (JP Morgan, Porosity)</td></tr><tr><td>b4</td><td>Lack of context, lack of judgment</td><td>AI approaches</td><td>IS research</td></tr><tr><td>b5</td><td>Reliance on external input</td><td>Trusted oracles</td><td>Private industry (Thomson Reuters)</td></tr><tr><td>b6</td><td>Limited to electronic enforceability</td><td>Netting vehicles</td><td>Private industry</td></tr><tr><td>b7</td><td>Lack of contract mutability</td><td>Blockchain-editing techniques</td><td>Private industry (Accenture)</td></tr><tr><td>b8</td><td>Lack of arbitration mechanisms</td><td>Technical arbitrator; arbitration forum; AI</td><td>IS research</td></tr><tr><td colspan="4">Technical implementation level</td></tr><tr><td>c1</td><td>Limited scalability</td><td>Ethereum Enterprise layer for private blockchains</td><td>Private industry (JP Morgan, Microsoft)</td></tr><tr><td>c2</td><td>Security risks on public blockchains</td><td>Advanced security methods, proof of stake consensus</td><td>IS research</td></tr><tr><td>c3</td><td>Privacy concerns</td><td>Homomorphic encryption, detection methodologies</td><td>IS research</td></tr><tr><td>c4</td><td>Lack of unifying standards</td><td>Industry consortia</td><td>Private industry, industry bodies</td></tr><tr><td>c5</td><td>Lack of interoperability</td><td>Interoperability layer between blockchains</td><td>IS research</td></tr><tr><td>c6</td><td>Code vulnerabilities</td><td>Modeling tools, advanced simulation</td><td>IS research</td></tr></table>

AI: artificial intelligence; IS: information system; SC: Smart Contract.

Finally, the underlying premises on how to deal with this technology might need to be defined by politics. As the US District court New York succinctly declared in the context of an early court case on the legal nature of Bitcoin,

The Court also takes no position on the deeper issue of whether blockchain technology and virtual currencies should be fit into existing regulatory schemes, as opposed to devising new schemes to address a completely new technology. Given the options available for future regulation, any discussion about regulating virtual currencies is best left to the political process. (United States District Court for the Western District of New York, 2016)

In other words, the next step is for the legislators to take (Gurkaynak et al., 2016; Temte, 2019).

## Implications for practitioners and industry solutions

Regardless of the lack of full legal and regulatory clarity, businesses have started to employ smart contract technology in an increasingly engaged manner.

For instance, large IT firms are getting deeply immersed into the space with IBM playing a major role in the Hyperledger project. Similarly, Microsoft made the smart contract protocol Ethereum available on Microsoft Azure in 2017. Following their example, Amazon has launched a Blockchain as a Service product as part of its Amazon Web Service offering (Lu et al., 2019).

Regardless of the lack of full legal and regulatory clarity, businesses have also started to develop concrete solutions which could remedy some of the inherent shortcomings of smart contracts and pave the way for their broader acceptance across industries. This section, therefore, describes currently ongoing industry initiatives and concrete development efforts that directly address some of the shortfalls analyzed earlier.

First, in line with the idea of matching computer code and a parallel natural language contract, industry players such as Barclays Bank have started to work on the creation of smart contract templates to reduce the likelihood of any discrepancy between smart contract terms and the respective computer code (Clack et al., 2016), an effort recently also taken up by the academic community (Tsai et al., 2019). The introduction of standardized templates mirrors previous efforts in the financial industry, where the creation of standardized financial derivative contracts by the ISDA has enormously facilitated the creation and agreement of bilateral contracts over the past decade (US Structured Finance, 2006). Similarly, with an approved smart contract template, counterparties could re-use a template and just fill it with new contract parameters each time (Clack et al., 2016). Contracting parties could then rely on the fact that a standardized, pre-tested and certified smart contract will carry out the transaction as intended. This would help to address a potential mismatch between the intent of parties and eventual representation in code (b1).

With a similar objective, the Accord Project is aiming to develop open source tools for smart legal contracts (Dahmen and Liermann, 2019). As stated in its principles, the Accord Project establishes and maintains a technology neutral foundation for smart legal contracts.<sup>9</sup> This includes a common format for smart contracts, the sharing of reusable smart contract templates across different platforms and the development of an executable business logic. As of January 2020, more than 100 industry members have signed up to the project, including IBM, Hyperledger and DocuSign.

Another step forward was announced in July 2017 when the first decompiler for smart contracts was launched, named Porosity. In certain instances, the binary code stored on the blockchain could now be translated back to the initial source code (Abe et al., 2018; Amani et al., 2018). Independently, Zhou et al. (2018) presented an early ver sion of the tool Erays, which transforms bytecode into higher level representations, making it usable for human analysis (Zhou et al., 2018). Those efforts, for the first time, may allow verification of the congruency between binary computer code and the source code basis (b3). For the time being, however, such tools are predominantly compatible only with the source code language Solidity.

Even more ambitiously, players are working on creating a novel legal source language (Farmer and Hu, 2016) that would replace current source code languages such as Solidity. Instead of having a legal document in human prose that is translated into source code (and then compiled into binary code), legal contracts could be written in a standardized, formal language with clear semantics (Cohen et al., 2018). The contract logic and execution parameters could then automatically and unambiguously be translated both into code and into a natural language version of the contract (b1). Proponents argue that our human language has always been an incomplete and inaccurate tool to precisely specify contracts. In this regard, the development of a new formal Ricardian contract language aims to mirror the properties of best-in-class coding languages. Such properties may include an unambiguous language structure, where every feature has only one particular meaning and there is no contextdependency within a contract (Grigg, 2004). This would lead to significant improvements compared to the status quo, in which there are a number of co-existing languages such as Solidity or Serpent (Wohrer and Zdun, 2018) and underlying client implementations built in C++, Go, Java, Haskell or Python. A new formal language could be easier to use which would enable lawyers to draft legal contracts using this new language directly. Technical standards are still in discussion (Coblenz et al., 2019; Governatori et al., 2018; Idelberger et al., 2016). A first approach was launched in 2018 as a cooperation between the UK-based company Nivaura and the global Law Firm Allen & Overy, utilizing so-called Legal Markup Language (LML). Targeting use cases in capital markets at first, the objective of LML is to introduce a simple human readable set of symbols and rules (syntax) that lawyers can use to mark key parameters, paragraphs and schedules in legal contracts, enabling the contracts to be broken down [. . .], their components extracted into a database and then re-assembled again to create contracts for new deals (Cohen et al., 2018). Similarly, the OpenLaw project aims to bridge the gap between legal contracts and smart contracts. Also employing LML, they aim to facilitate turning legal contracts into code with embedded smart contract features (Goldenfein and Leiter, 2018; Tsai et al., 2019). In the future, further IS research on codifying and standardizing processes into domain-specific languages, also building upon the growing body of research into Natural Language Processing more broadly, is likely to facilitate this development (Dale, 2019; Tsai et al., 2019). Addressing the fact that smart contracts are limited to electronic enforceability and thus require the posting of all required collateral upfront, some have suggested the creation of smart contract netting and insurance vehicles that could enhance liquidity for frequently transacting counterparties (b6; Bai et al. 2019). Ironically, however, this would, in essence, recreate the central financial third parties that smart contracts were aiming to disintermediate.

So-called oracles could address the issue that, both in business contracts and in consumer-facing contracts, there is a need for external data to be reliable as an input factor (b5) (Kiviat, 2015). In B2B contracts, often an external reference rate will be incorporated into the contract to determine prices (e.g. the LIBOR for interest rate derivatives). Oracles can thus incorporate objective external data, such as interest rates, exchange rates and even customer-specific information (Luu et al., 2016; Tsai et al., 2019). In June 2017, the global news firm Thomson Reuters, indeed, announced the first Smart Oracle product by a major industry player. Through its BlockOne IQ product, Thomson Reuters made smart oracle functionality available to the blockchain ecosystem, initially for experimentation purposes. Institutions and individuals are able to use market data in smart contract applications, with digital blockchainbased proof that Thomson Reuters has verified the data.<sup>10</sup>

The issue of privacy has been at the center of efforts from both industry players and academic researchers. For instance, to cater to the specific enterprise needs of large financial institutions (c3), the bank JP Morgan has developed an enterprise layer on top of the Ethereum protocol, named Quorum (Eenmaa-Dimitrieva and Schmidt-Kessen, 2019). The standard was open-sourced to the public in November 2016, to encourage widespread adoption with a growing community of other financial institutions. Second, researchers at IBM have presented a first version of a multiparty computation (MPC) solution, thus extending the Hyperledger Fabric protocol to allow for private data sharing (Benhamouda et al., 2019). MPC, in short, stands for a cryptographic protocol which distributes computational steps across several agents where, at the same time, no single agent is able to get access to all of the other party’s data.

Third, researchers are increasingly exploring the concept of zero-knowledge proofs, an encryption method initially proposed already in 1989 (Eenmaa-Dimitrieva and Schmidt-Kessen, 2019; Goldwasser et al., 1989). As one interviewee explains, A commonly used example of a zeroknowledge proof in a blockchain context means the ability to correctly answer the question “Does Person X have enough funds for transaction Y” without gaining knowledge of the identity of Person X or the exact amount of their funds. One of the first industry applications applying zeroknowledge proofs is the pharmaceutical industry network MediLedger (Pashkov and Soloviov, 2019; Pisa, 2018). Finally, the Hyperledger Fabric protocol provides for socalled private channels for messaging through its access control service (Benhamouda et al., 2019; Dhillon et al., 2017b; Reyna et al., 2018).

Next, the issue of scalability (c1) is being addressed by improvements to the underlying blockchain public network. Potential approaches include the concept of quadratic sharding which would involve setting up separate blockchains, connected by the same system and managed by a so-called validity contract manager. Potentially, this could enhance the number of transactions per seconds from a few dozens to more than 10,000 (Chauhan et al., 2018). However, not least due to security concerns, this solution has not yet been implemented at scale (Chauhan et al., 2018). Second, private permissioned blockchains, such as supported by the Hyperledger Fabric Protocol or Quorum, have shown much faster throughput rates, given that trust protocols such as proof of work are replaced by granular access control (Chauhan et al., 2018). In addition, the concept of State Channels has recently gained more traction, which foresees that more transactions are recorded offchain and the processing and execution of smart contracts of any arbitrary complexity becomes feasible (Dziembowski et al., 2018; Jaiswal, 2018; Kim et al., 2018).

Finally, to facilitate dialogue across institutions, several industry consortia have been launched; among others, the Hyperledger Project, the R3 Foundation and the Enterprise Ethereum Alliance (Swan, 2018). One objective of those semi-formal groups is to align on technical standards (c4) and discuss potential cooperation alongside various use cases. In the long run, further cooperation and integration across those industry initiatives might propel the development of specific interoperability standards across different protocols.

## Open questions for future IS research

Given that smart contracts and the blockchain technology as a whole are still in their early innings, vast opportunity for further research remains to improve the current design of smart contracts and overcome persisting weaknesses. Practitioners in the field could also benefit from further IS research that pertains to the blockchain and distributed ledger technology more broadly. At a conceptual level, game theoretical approaches, such as hypergames, could be investigated for appropriate mechanism design, including randomized mechanisms (Bigi et al., 2015; Dobzinski et al., 2012; Ho and Su, 2013; Zhang et al., 2019).

A critical intrinsic limitation of smart contracts is the need for pre-specification and consideration of all future states (b2). Any simulation of future states will always remain incomplete (Tsai et al., 2019). Therefore, researchers have started applying the concept of formal model verification to smart contracts (Amani et al., 2018; Magazzeni et al., 2017; Nehai and Bobot, 2019), a technique already applied in the airline industry where absolute safety is critical. Researchers have thus started to build first prototypes that verify the future outcomes of smart contracts (Bhargavan et al., 2016; Bigi et al., 2015; Park et al., 2018). Such a solution is intended to be a verification tool derived from a complete and thoroughly tested formal semantics of EVM, rather than only a simulation (Park et al., 2018; Tonelli, 2019).

Research into interoperability could become another criti cal driver for widespread adoption. With a growing number of diverging blockchain standards and protocols, especially smaller players may be reluctant to invest significant resources into one particular solution until one dominant design has proven itself as superior (c5). Interoperability between different blockchain protocols could partially help to address this concern (Beck and Müller-Bloch, 2017); if in the future, dif ferent platforms can “speak to each other” without friction, adoption is expected to increase more rapidly (de Reuver et al., 2017). Potential solutions which have been proposed include centralized notary schemes, where a designated party agrees to perform an action on another blockchain when a particular event on the source blockchain has happened. Another solution foresees so-called sidechains, that is, systems within one blockchain which are directly able to read and verify states and events in another blockchain (Buterin, 2016). Notwithstanding those initial efforts, research and development are still in their infancy and a functioning state of true interoperability is far out into the future, according to our interviewees. According to them, industry participants might currently prefer to forgo some interoperability and limit their scope of action to a smaller sphere to gain a solution that is completely under their control.

The concept of a new legal language at the intersection of law, linguistics and computer science, such as LML, developed by practitioners (see above), could also open up an entirely new area for IS research (b1). This research objective would entail the development of a new joint source languages for legal documents. Documents written in this language would then have an unambiguous representation both in executable code and legal prose (Farmer and Hu, 2016). In the long run, a new formal language could even be directly allowed in court proceedings. As this concept is still in its beginnings, it may well be a relevant area of IS research for years to come.

Research around advanced encryption methods is another area that could further the wider use of smart contracts on public blockchains (Galtier and Marini, 2017; Kosba et al., 2016) and overcome currently prevailing privacy issues. As introduced above, MPC remains a promising field of research. Further out, fully homomorphic encryption is a way of performing calculations on encrypted data without first decrypting them (Dowlin et al., 2017). The use of homomorphic encryption techniques could offer privacy protection and selectively allow access to encrypted data in a smart contract setting (Dowlin et al., 2017). However, at the moment, latency is still far too high to be used in any production setting. For instance, the time needed for a Google search would increase by a factor of 1012 (Gentry, 2009).

To detect malicious attacks and fraudulent behavior early on, research is also starting to investigate the use of machine learning to spot fraudulent transaction attempts. To monitor and detect suspicious patterns of behavior, supervised and unsupervised machine learning approaches, such as convolutional neural networks, are currently being tailored for use in a blockchain setting (Xu, 2016). Research has also expanded to tackle the critical issue of vulnerabilities in smart contracts (c6), seeking different solutions to the problem (Feng et al., 2019; Garcia, 2016). Programs such as Smartcopy aim to identify adversarial attack programs directly, based on their source code, to prevent the exploitation of vulnerabilities in a victim smart contract.

Applying the area of artificial intelligence (AI) and machine learning to the legal domain more broadly is another field of research that has long been envisioned (Rissland, 1989; Wahlgren, 1992), but not yet been achieved at a satisfactory level. In the last few years, projects to address contract drafting and preparation were mostly limited to narrower use cases, such as proofreading assistants or clause checking (Ng, 2017). One of the future use cases would be to overcome the lack of context and lack of judgment (b4) by applying machine learning and AI to a comprehensive body of cases.

In addition, a method of arbitration could be particularly necessary in a smart contract environment (b8). Many smart contracts may still require the involvement of resolution mechanisms over time, either as a pre-defined contract clause, for example, to assess material value judgments such as reasonable effort, or as a dispute resolution mechanism, in case of unforeseen circumstances (Groenbaek, 2016). Synthesizing the input from existing literature and our expert panel, in the world of a decentralized blockchain, an arbitration mechanism could take the following forms:

1. Real-world arbitration (human involvement): A provision in the contract could foresee submission of disputes to a real-world private arbitration, in case of some unforeseen defect in the contract code (Herian, 2018a). This assumes that the counterparties are actual legal or natural persons that could participate in an arbitration process and provide additional, natural language–based input (Koulu, 2016).

2. Arbitration forum (anonymous human involvement): In this scenario, arbitration could be administered via the use of an arbitration forum. The smart contract would identify a body of rules for the arbitration (case law) and a pool of possible arbitrators to whom to assign the case. Those could vary from persons able to assist with common sense logic to certified arbitrators for complex disputes where significant value is at stake (Zou et al., 2016). An anonymous majority vote could also decide on the case. Reputation systems would need to be in place to align incentives (Zhou and Hwang, 2007).

3. Technical arbitrator (no human involvement): a provision in the smart contract code which initiates delegation to an arbitration program. Based on the available data, a library of previous cases or some algorithmic decision logic, the program would automatically return a solution back to the original smart contract (Harz and Boman, 2019; Koulu, 2016).

Even more advanced, deriving a decision logic based on the entire amount of unstructured legal prose, laws and previous court rulings to teach algorithms how to come up with legal reasoning is a promising, while still ambitious, field for future research (Liu, 2016; Omohundro, 2014). It is ambitious, not least because studies have shown that machine learning trained on previous court decisions might also replicate any inherent bias (Mehrabi et al., 2019). Therefore, developing and implementing an arbitration or decision logic that is objectively fair and free of biases will likely remain one of the more challenging fields of research for many years to come.

## The final piece: the organizational perspective

Finally, beyond legal, economic and technical aspects mentioned above, our interviewees pointed out one additional area of inherent conflict, namely, related to managerial and organizational issues. To illustrate this point, we assume for a moment that the previous shortcomings across all levels had all been sufficiently resolved. The regulatory environment has become fully supportive of smart contracts and there is definitive legal certainty about their treatment in court; intrinsic contract-level shortcomings and technical issues have been addressed and smart contract solutions seem to be scalable, standardized and secure. Would this mean that the adoption of smart contract technology must follow rapidly afterward? Not necessarily, at least according to our interviewee panel. Beyond all identifiable and measurable shortcomings (a1–c6), the final element which could potentially slow down institutional adoption seems to relate to softer issues, namely, organizational dynamics, corporate culture and elements of human psychology, as we will describe in this section. It is noteworthy that the organizational perspective has been a consistently mentioned pattern, in particular, by the industry participants in our panel. From all responses, we have distilled five recurring themes, each representing a factor which might slow down the industrial uptake of smart contracts, even in a perfectly conducive external environment.

Network effects. By definition, contracts are agreed between two or more parties. There is limited value in implementing a costly technology when there are few other industry players to contract with. In the presence of significant network effects, a critical determinant for smart contracts to gain significant momentum is that a relevant number of key industry players are spearheading the transformation and roll out those new solutions on a larger scale. Research has shown that innovation diffusion critically depends on an initial positive feedback loop (Abrahamson and Rosenkopf, 1997). There is even a certain factor of randomness whereby seemingly insignificant idiosyncrasies of [network] strictures can have very large effects on the extent of an innovation’s diffusion (Abrahamson and Rosenkopf, 1997). As such, there is a certain initial Catch-22 situation for smart contracts to get wider traction (Choi et al., 2010). As one industry observer remarked, Many companies are progressing with tests but [. . .] are far from turning the switch. [. . .] It is easier to let [others] move first and make those costly first-mover mistakes while waiting for the dominant technology [. . .] to emerge.

Organizational incentives. In the corporate world, a wellresearched phenomenon is the so-called Innovator’s Dilemma, a term coined by Clayton Christensen (2013). According to his theory, when incumbent companies determine whether they should invest in innovative technologies, those new technologies are often not initially developed enough for their existing customer base and their mature value networks. Therefore, the return on investment is perceived as low, compared to the current high-margin business that those incumbents already operate (Alles, 2002). Consequently, incumbent players might have a vested interest in broadly preserving the status quo. For example, in clearing and settlement, industry players such as large investment banks and exchanges derive a considerable part of their revenues from their intermediary role, which smart contracts promise to eliminate. Consequently, such players might not wholeheartedly embrace a new technology that could eventually cannibalize parts of their revenue stream. As one interviewee pointedly remarks, Not to be cynical, but [. . .] they make good money today. [. . .] no matter what they tell you, no incumbent wants efficient markets.

Reputation. Over the past years, blockchain technology, and cryptocurrencies, in particular, have repeatedly been associated with crime, fraud and pyramid schemes. The apparent speculative bubble in the cryptocurrency market, public security failures and numerous ICO fraud cases have contributed to a widely shared negative image of blockchain technology (Dhillon et al., 2017a; Zetzsche et al., 2019). Especially larger, established institutions might, therefore, hesitate to utilize smart contracts based on block chain technology at scale while the latter still has some doubtful by-taste. This is especially true for firms with a more conservative client base such as banks or asset managers. Therefore, CEOs concerned about alienating customers as a result of a controversial technological choice might, in turn, decide not to be among the early adopters.

Risk aversion and individual incentives. As with the implementation of any new technology, a residual risk of failure will always remain. Even if all research and proof of concepts point toward low risk for the eventual roll-out, there will be no guarantee of success. Therefore, senior decision makers might hesitate to bet on a new technology when failure might have fatal consequences and money could be lost. As one interviewee wryly remarks,

As a CEO, you are rarely fired if you maintain the status quo and improve on the margins. But if you were to gamble away the companies’ fortunes on some risky blockchain adventure [that] turns out badly. . . you are toast.

Or, as another corporate interviewee summarized, “in the short term, the downside [of smart contract implementation] is clearly much larger than that upside.”

Knowledge and skill gap. Corporate leaders in charge today have almost all been trained without exposure to smart contracts or blockchain technology up until recently. Deciding to implement smart contracts in a meaningful manner would mean embracing a technology that they have limited experi ence with and knowledge about. From an individual deci sion maker’s perspective, they have to step into territory where they might feel highly uncomfortable. Corporate leaders might feel they lack the knowledge basis to even be able to fully assess those risks in the first place. As a result, executives might be reluctant to make a choice where they need to rely on a few experts. For the legal practice to embrace smart contracts, lawyers would need to become bilingual in traditional law and programming languages to assess and develop smart contract code (Tsai et al., 2019). So far, the typical legal training curriculum does not include any coding training and, accordingly, such bilingually trained legal experts are still a rather rare exception.

To summarize the findings of the previous sections, progress along legal, regulatory, contract and technical levels is critical and a necessary condition for the eventual adoption of smart contracts. To enable this, a fertile environment created by benign regulators and legislators, further progress by industry practitioners and dedicated IS research efforts will be critical. At the same time, the adoption barrier presented by softer organizational and individual factors should not be underestimated and might be one of the reasons why institutional uptake will continue to be slower than some observers had initially anticipated.

## Synthesis and conclusion

Smart contracts present a promising technology with which ISs or arbitrary parties can interact with one another. By being self-executable and self-enforceable, smart contracts reduce transaction costs associated with contracting and enforcement of contracts. Hence, there is little doubt among practitioners and IS scholars that smart contracts offer unprecedented potential to many industries, such as the financial industry or the Internet of Things.

This article sheds light on the prevailing issues that have so far hindered the wider adoption of smart contracts. According to the current majority opinion, smart contracts still fall within the boundaries of our established legal understanding and thus have to comply with its rules and principles. In their current manifestation, smart contracts face both external limitations, where the contract design clashes with existing law, and intrinsic limitations, where current design features of smart contract technology limit their applicability for more complex transactions. Moreover, technical shortcomings, particularly of public blockchain networks, still restrict the usability of smart contracts on a larger scale.

At the same time, we show that public authorities, that is, legislators, policy-makers and regulators, can employ an array of options to create a conducive environment for the adoption of smart contracts. Potential regulatory approaches include mandatory identification, consumer protection regulation and the international harmonization of rules. Similarly, private industry initiatives can drive to resolve some of the technical issues and raise both awareness and acceptance for the application of smart contracts. Promising industry initiatives described in this article include the development of neutralizable smart contracts, the creation of enterprise layers on top of existing infrastructure and the design of smart contract templates.

Finally, IS Research can play a critical role in furthering the proliferation of smart contracts by working on advanced encryption methods, developing forms of technical arbitration that may involve AI and applying aspects of game theory to a blockchain environment. Based on our assessment and expert interviews, the far-reaching potential of smart contracts is still valid, despite their lack of initial adoption. We find that improving technology in a deliberate way and setting the right legal and regulatory boundaries to overcome some of smart contracts’ early shortcomings will be critical for this nascent technology to eventually gain mainstream acceptance. Once more of those initial obstacles are resolved, it will be incumbent upon a number of pioneering institutions to take a firstmover risk. The combination of such concerted efforts might help this promising technology of smart contracts eventually get off the ground and bring to fruition its full potential.

## Declaration of conflicting interests

The author(s) declared no potential conflicts of interest with respect to the research, authorship and/or publication of this article.

## Funding

The author(s) received no financial support for the research, authorship and/or publication of this article.

## ORCID iD

Daniel Drummer https://orcid.org/0000-0002-4131-9064.

## Notes

1. c.f. https://hollis.harvard.edu

2. c.f. German Civil Code BGB, §138 Abs.1; Austrian Civil Code ABGB, supra note 84, §879.

3. https://solidity.readthedocs.io/en/develop/

4. House Bill 1944.

5. House Bill 2417.

6. Legislative Bill 695.

7. House Bill 1507.

8. Public Act 101-0514.

9. https://www.accordproject.org/about

10. c.f., https://blockoneiq.thomsonreuters.com/—initially, the service is only compatible with networks based on Corda and Ethereum/Quorum.

## References

Abe R, Watanabe H, Ohashi S, et al. (2018) Storage protocol for securing blockchain transparency. In: IEEE 42nd annual computer software and applications conference, Tokyo, Japan, 23–27 July, pp. 577–581. New York: IEEE.

Abrahamson E and Rosenkopf L (1997) Social network effects on the extent of innovation diffusion: A computer simulation. Organization Science 8(3): 289–309.

Alces PA (2011) A Theory of Contract Law: Empirical Insights and Moral Psychology. Oxford: Oxford University Press.

Alles M (2002) A critical analysis of the innovator’s dilemma: Why should new technologies cause great firms to fail? International Journal of Digital Accounting Research 2(4): 235–266.

Al-Saqaf W and Seidler N (2017) Blockchain technology for social impact: Opportunities and challenges ahead. Journal of Cyber Policy 2(3): 338–354.

Amani S, Bégel M, Bortin M, et al. (2018) Towards verifying ethereum smart contract bytecode in Isabelle/HOL. In: 7th ACM SIGPLAN international conference (eds Andronick J and Felty A), pp. 66–77. New York: The Association for Computing Machinery, Inc. DOI: 10.1145/3167084.

Atzei N, Bartoletti M and Cimoli T (2017) A survey of attacks on ethereum smart contracts (SoK). In: Maffei M and Ryan M (eds) International Conference on Principles of Security and Trust. Berlin: Springer, pp. 164–186.

Avital M, Beck R, King J, et al. (2016) Jumping on the blockchain bandwagon: Lessons of the past and outlook to the future. In: International conference on information systems, Dublin (ICIS 2016), Dublin, 11–14 December, pp. 5–25. Atlanta, GA: Association for Information Systems.

Bach LM, Mihaljevic B and Zagar M (2018) Comparative analysis of blockchain consensus algorithms. International Convention on Information and Communication Technology 2018: 1545–1550.

Bai X, Tsai W-T and Jiang X (2019) Blockchain design: A PFMI viewpoint. In: 2019 IEEE international conference on service-oriented system engineering (SOSE), San Francisco, CA, 4–9 April, pp. 146–14609. New York: IEEE.

Bartoletti M and Pompianu L (2017) An empirical analysis of smart contracts: Platforms, applications, and design patterns. In: Brenner M, Rohloff K, Bonneau J and et al. (eds) Financial Cryptography and Data Security. Cham: Springer, pp. 494–509.

Bauer M (2017) Discussion paper on distributed ledger technology. Financial Conduct Authority (FCA) discussion paper DP 17/3. London: Financial Conduct Authority.

Beck R and Müller-Bloch C (2017) Blockchain as radical innovation: A framework for engaging with distributed ledgers. In: Proceedings of the 50th Hawaii international conference on system sciences, pp. 5390–5399. Available at: https://pdfs .semanticscholar.org/cdc3/a80f5c77270bd36f1a0212bcc ea8651de3d4.pdf?\_ga=2.61443562.756206481.1590070587- 2068374151.1587362146 (accessed 21 May 2020).

Beck R, Czepluch JS, Lollike N, et al. (2016) Blockchain: The gateway to a trust-free cryptographic economic world. In: European conference on information systems, Istanbul (ECIS 2016), Istanbul, 12–15 June, pp. 2–25. Atlanta, GA: Association for Information Systems.

Benhamouda F, Halevi S and Halevi T (2019) Supporting private data on hyperledger fabric with secure multiparty computation. IBM Journal of Research and Development 63(2/3): 1–3.

Benston GJ (2000) Consumer protection as justification for regulating financial-services firms and products. Journal of Financial Services Research 17(3): 277–301. Available at: https://link. springer.com/content/pdf/10.1023/A:1008154820305.pdf (accessed 21 May 2020).

Bhargavan K, Swamy N, Zanella-Béguelin S, et al. (2016) Formal verification of smart contracts. In: Proceedings of the 2016 ACM workshop on programming languages and analysis for security (ed Murray T), pp. 91–96. New York: Association for Computing Machinery. Available at: https://dl.acm.org doi/pdf/10.1145/2993600.2993611 (accessed 21 May 2020).

Bigi G, Bracciali A, Meacci G, et al. (2015) Validation of decentralised smart contracts through game theory and formal methods. In: Degano P, Bodei C and Ferrari GL, et al. (eds) Programming Languages With Applications to Biology and Security. Cham: Springer, pp. 142–161.

Bix B (2006) Robert Alexy’s Radbruch formula, and the nature of legal theory. Rechtstheorie 37: 139–149.

Bodó B, Gervais D and Quintais JP (2018) Blockchain and smart contracts: The missing link in copyright licensing? International Journal of Law and Information Technology 26(4): 311–336.

Böhme R, Christin N, Edelman B, et al. (2015) Bitcoin: Economics, technology, and governance. Journal of Economic Perspectives 29(2): 213–238.

Bourque S and Tsui S (2014) A Lawyer’s Introduction to Smart Contracts. Łask: Scientia Nobilitat.

Boyer RS and Moore JS (1984) A mechanical proof of the unsolvability of the halting problem. Journal of the ACM 31(3): 441–458.

Brekoulakis S and Devaney M (2017) Public-private arbitration and the public interest under English law. The Modern Law Review 80(1): 22–56.

Bu-Pasha S (2017) Cross-border issues under EU data protection law with regards to personal data protection. Information & Communications Technology Law 26(3): 213–228.

Buterin V (2016) Ethereum: Platform review. Opportunities and challenges for private and consortium blockchains. Available at: http://www.smallake.kr/wp-content/ uploads/2016/06/314477721-Ethereum-Platform-Review-Opportunities-and-Challenges-for-Private-and-Consortium-Blockchains.pdf (accessed 21 May 2020).

Cant B, Khadikar A, Ruiter A, et al. (2017) Smart contracts in financial services: Getting from hype to reality. Capgemini Whitepaper. Available at: https://www.capgemini.com/consulting-de/wp-content/uploads/sites/32/2017/08/smart\_con tracts\_paper\_long\_0.pdf (accessed 21 May 2020).

Carter PB (1980) B private international law. British Yearbook of International Law 50(1): 241–256.

Casey M, Crane J, Gensler G, et al. (2018) The Impact of Blockchain Technology on Finance: A Catalyst for Change (Vol. 21: Geneva Reports on the World Economy). Geneva: International Center for Monetary and Banking Studies. Available at: https:// www.cimb.ch/uploads/1/1/5/4/115414161/geneva21\_1.pdf (accessed 21 May 2020).

Chanson M, Bogner A, Wortmann F, et al. (2017) Blockchain as a privacy enabler. In: Lee S, Takayama L and Truong K (eds) Proceedings of the 2017 ACM International Joint Conference on Pervasive and Ubiquitous Computing. New York: ACM Press, pp. 13–16.

Chauhan A, Malviya OP, Verma M, et al. (2018) Blockchain and scalability. In: 2018 IEEE 18th international conference on software quality, reliability, and security companion (ed R IEEE International Conference on Software Quality and Security), Lisbon, 16–20 July, pp. 122–128. Piscataway, NJ: IEEE.

Choi H, Kim S and Lee J (2010) Role of network structure and network effects in diffusion of innovations. Industrial Marketing Management 39(1): 170–177.

Christensen CM (2013) The Innovator’s Dilemma: When New Technologies Cause Great Firms to Fail. Boston, MA: Harvard Business Review Press.

Christidis K and Devetsikiotis M (2016) Blockchains and smart contracts for the internet of things. IEEE Access 4: 2292–2303.

Clack C, Bakshi V and Braine L (2016) Smart contract templates: Foundations, design landscape and research directions. arXiv preprint arXiv:1608.00771. Available at: https://arxiv.org/ abs/1608.00771 (accessed 21 May 2020).

Clark J (2016) Financial Cryptography and Data Security: FC 2016 International Workshops (Vol. 9604). Heidelberg: Springer.

Coblenz M, Sunshine J, Aldrich J, et al. (2019) Smarter smart contract development tools. In: Proceedings of 2nd international workshop on emerging trends in software engineering for blockchain (WETSEB), Montreal, QC, Canada, 27 May, pp. 1–4. New York: IEEE.

Cohen R, Smith P, Arulchandran V, et al. (2018) Automation and blockchain in securities issuances. Butterworths Journal of International Banking and Financial Law 33: 144–150.

Cong LW and He Z (2019) Blockchain disruption and smart con tracts. The Review of Financial Studies 32(5): 1754–1797.

Conley J (2017) Blockchain and the economics of crypto-tokens and initial coin offerings. Working paper, Department of Economics, Vanderbilt University, Nashville, TN.

Constantinides P, Henfridsson O and Parker GG (2018) Introduction—Platforms and infrastructures in the digital age. Information Systems Research 29(2): 381–400.

Cornelius K (2018) Smart contracts and the freedom of contract doctrine. Journal of Internet Law 22(5): 3–11.

Dahmen G and Liermann V (2019) Hyperledger composer— Syndicated loans. In: Liermann V and Stegmann C (eds) The Impact of Digital Transformation and FinTech on the Finance Professional. Cham: Palgrave Macmillan, pp. 45–70.

Dai J and Vasarhelyi MA (2017) Towards blockchain-based accounting and assurance. Journal of Information Systems 31: 5–21.

Dale R (2019) Law and word order: NLP in legal tech. Natural Language Engineering 25(1): 211–217.

de Reuver M, Sørensen C and Basole RC (2017) The digital platform: A research agenda. Journal of Information Technology 33: 124–135.

Delmolino K, Arnett M and Miller A (2015) Step by step towards creating a safe smart contract. SSRN working paper. Available at: https://eprint.iacr.org/2015/460.pdf (accessed 21 May 2020).

Dennis R and Disso JP (2019) An analysis into the scalability of Bitcoin and Ethereum. In: Sherratt S, Dey N and Joshi A (eds) Third International Congress on Information and Communication Technology, Advances in Intelligent Systems and Computing. Singapore: Springer, pp. 619–627.

Destefanis G, Marchesi M, Ortu M, et al. (2018) Smart contracts vulnerabilities: A call for blockchain software engineering? In: 2018 IEEE 1st international workshop on blockchain oriented software engineering (IWBOSE), Campobasso, 20 March, pp. 19–25. New York: IEEE.

Dhillon V, Metcalf D and Hooper M (2017a) The DAO hacked. In: Dhillon V, Metcalf D and Hooper M (eds) Blockchain Enabled Applications. New York: Apress, pp. 67–78.

Dhillon V, Metcalf D and Hooper M (2017b) The hyperledger project. In: Dhillon V, Metcalf D and Hooper M (eds) Blockchain Enabled Applications. New York: Apress, pp. 139–149.

Dobzinski S, Nisan N and Schapira M (2012) Truthful randomized mechanisms for combinatorial auctions. Journal of Computer and System Sciences 78(1): 15–25.

Domingo R-S, Piñeiro-Chousa J and López-Cabarcos M (2020) What factors drive returns on initial coin offerings? Technological Forecasting and Social Change 153: 119915.

Dooley K (2012) The LIBOR scandal. Review of Banking and Financial Law 32: 2–565.

Dowlin N, Gilad-Bachrach R, Laine K, et al. (2017) Manual for using homomorphic encryption for bioinformatics. Proceedings of the IEEE 105(3): 552–567.

Drummer D, Feuerriegel S and Neumann D (2017) Crossing the next frontier: The role of ICT in driving the financialization of credit. Journal of Information Technology 32(3): 218–233.

Dubovitskaya A, Xu Z, Ryu S, et al. (2017) Secure and trustable electronic medical records sharing using blockchain. AMIA Annual Symposium Proceedings 2017: 650–659.

Dziembowski S, Faust S and Hostáková K (2018) General state channel networks. In: Proceedings of the 2018 ACM SIGSAC conference on computer and communications security (ed Lie D), Toronto, ON, Canada, 15–19 October, pp. 949–966. ACM.

Eenmaa-Dimitrieva H and Schmidt-Kessen M (2019) Creating markets in no-trust environments: The law and economics of smart contracts. Computer Law & Security Review: The International Journal of Technology Law and Practice 35(1): 69–88.

Egelund-Müller B, Elsman M, Henglein F, et al. (2017) Automated execution of financial contracts on blockchains. Business & Information Systems Engineering 59(6): 457–467.

ESMA Securities and Markets Stakeholder Group (2016) Summary of conclusions: Recent market developments February 2016. ESMA publication 2016/SMSG/004. Paris: ESMA.

Eyal I and Sirer EG (2013) Majority is not enough: Bitcoin mining is vulnerable. arXiv e-prints. Available at: https://arxiv. org/abs/1311.0243 (accessed 21 May 2020).

Eyassu SE (2019) Overview of blockchain legislation and adoption: Status and challenges. Issues in Information Systems 20: 12–21.

Fabian B, Ermakova T and Sander U (2016) Anonymity in Bitcoin? The users’ perspective. In: ICIS 2016 proceedings. Available at: http://aisel.aisnet.org/icis2016/Crowdsourcing/ Presentations/10 (accessed 21 May 2020).

Farmer WM and Hu Q (2016) A formal language for writing contracts. In: 2016 IEEE 17th international conference on information reuse and integration (IRI), Pittsburgh, PA, 28–30 July, pp. 134–141. New York: IEEE.

Feng Y, Torlak E and Bodik R (2019) Precise attack synthesis for smart contracts. Available at: http://arxiv.org/ pdf/1902.06067v1 (accessed 21 May 2020).

Filby M (2013) Code is law: Assessing architectural file sharing regulation in the online environment. Journal of International Commercial Law and Technology 8: 81–103.

Frankenreiter J (2019) The limits of smart contracts. Journal of Institutional and Theoretical Economics 175: 149–162.

Furmston MP and Tolhurst G (2010) Contract Formation: Law and Practice (Cont. Mik E). Oxford: Oxford University Press.

Galtier M and Marini C (2017) Morpheo: Traceable machine learning on hidden data. arXiv preprint arXiv:1704.05017. Available at: https://arxiv.org/abs/1704.05017 (accessed 21 May 2020).

Garcia M (2016) Racist in the machine: The disturbing implications of algorithmic bias. World Policy Journal 33(4): 111–117.

Garrett M (2010) Efficiency and certainty in uncertain times: The material adverse change clause revisited. Columbia Journal of Law and Social Problems 43(3): 333–362.

Gatteschi V, Lamberti F, Demartini C, et al. (2018) Blockchain and smart contracts for insurance: Is the technology mature enough? Future Internet 10(2): 20. Available at: https://www. mdpi.com/1999-5903/10/2/20/pdf (accessed 21 May 2020).

Gentry C (2009) Fully homomorphic encryption using ideal lattices. Symposium on Theory of Computing 9: 169–178.

Giancaspro M (2017) Is a “smart contract” really a smart idea? Insights from a legal perspective. Computer Law & Security Review 33: 825–835.

Gideon L (2012) Handbook of Survey Methodology for the Social Sciences. New York: Springer.

Glaser F (2017) Pervasive decentralisation of digital infrastructures: A framework for blockchain enabled system and use case analysis. In: 50th Hawaii international conference on system sciences (HICSS 2017), pp. 1543–1552. Available at: https://pdfs.semanticscholar.org/859d/0535e16095f274df4d 69df54954b21258a13.pdf (accessed 21 May 2020).

Goldenfein J and Leiter A (2018) Legal engineering on the blockchain: “Smart contracts” as legal conduct. Law and Critique 29(2): 141–149.

Goldwasser S, Micali S and Rackoff C (1989) The knowledge complexity of interactive proof systems. SIAM Journal on Computing 18(1): 186–208.

Gomber P and Haferkorn M (2013) High-frequency-trading. Business & Information Systems Engineering 55(2): 99–102.

Governatori G, Idelberger F, Milosevic Z, et al. (2018) On legal contracts, imperative and declarative smart contracts, and blockchain systems. Artificial Intelligence and Law 26(4): 377–409.

Grigg I (2004) The Ricardian contract. In: WEC 2004 (eds Benatallah B, Godart C and Shan MC), San Diego, CA, 6 July, pp. 25–31. New York: IEEE.

Groenbaek M (2016) Blockchain 2.0, smart contracts and legal challenges. Computers and Law 27(2): 34–37.

Guo Y and Liang C (2016) Blockchain application and outlook in the banking industry. Financial Innovation 2(1): 24.

Gurkaynak G, Yilmaz I and Haksever G (2016) Stifling artificial intelligence: Human perils. Computer Law & Security Review 32(5): 749–758.

Gutwirth S, Leenes R and De Hert P (2016) Data Protection on the Move: Current Developments in ICT and Privacy/Data Protection. Dordrecht: Springer-Verlag.

Hans R, Zuber H, Rizk A, et al. (2017) Blockchain and smart contracts: Disruptive technologies for the insurance market. In: Americas conference on information systems (AMCIS 2017), pp. 1–10. Association for Information Systems. Available at: https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1174&co ntext=amcis2017 (accessed 21 May 2020).

Hartnell HE (2015) Civil justice as governance in the European Union: Reflections on civil procedure, private international law (conflict of laws) and the administration of justice since the Roman empire. Helsinki legal studies research paper no 40. DOI: 10.2139/ssrn.2698610.

Harz D and Boman M (2019) The scalability of trustless trust. In: Zohar A, Eyal I, Teague V and et al. (eds) Financial Cryptography and Data Security. Berlin: Springer, pp. 279–293.

Herian R (2018a) Legal Recognition of Blockchain Registries and Smart Contracts. Milton Keynes: EU Blockchain Observatory and Forum.

Herian R (2018b) Regulating disruption: Blockchain, GDPR and questions of data sovereignty. Journal of Internet Law 22(2): 1–16.

Higgins S (2017) Accenture awarded patent for “editable blockchain.” Coindesk, 26 September. Available at: https://www. coindesk.com/accenture-awarded-patent-editable-blockchain-tech (accessed 21 May 2020).

Ho TH and Su X (2013) A dynamic level- k model in sequential games. Management Science 59(2): 452–469.

Huang A (2015) Reaching within silk road: The need for a new subpoena power. Boston College Law Review 56(85): 2093–2125.

Huckle S (2016) Internet of things, blockchain and shared economy applications. Procedia Computer Science 98(C): 461– 466.

Hyvärinen H, Risius M and Friis G (2017) A blockchain-based approach towards overcoming financial fraud in public sector services. Business & Information Systems Engineering 59: 441–456.

Iansiti M and Lakhani KR (2017) The truth about blockchain. Harvard Business Review 95(1): 118–127.

Idelberger F, Governatori G, Riveret R, et al. (2016) Evaluation of logic-based smart contracts for blockchain systems. In: Alferes JJ, Bertossi L, Governatori G and et al. (eds) Rule Technologies (Lecture Notes in Computer Science). Cham: Springer, pp. 167–183.

Jackson O (2018) Is It Possible to Comply With GDPR Using Blockchain? London: International Financial Law Review.

Jaiswal AK (2018) Parsec: A state channel for the internet of value. arXiv:1807.11378. Available at: http://arxiv.org/ pdf/1807.11378v1 (accessed 21 May 2020).

Juels A, Kosba A and Shi E (2016) The ring of Gyges: Investigating the future of criminal smart contracts. In: ACM conference on computer and communications security (CCS 2016), October, pp. 283–295. ACM. Available at: https://eprint.iacr. org/2016/358.pdf (accessed 21 May 2020).

Kim HM and Laskowski M (2017) A perspective on blockchain smart contracts: Reducing uncertainty and complexity in value exchange. In: 26th international conference on computer communication and networks (ICCCN), Vancouver, BC, Canada, 31 July–3 August. New York: IEEE.

Kim HM and Laskowski M (2018) Toward an ontology-driven blockchain design for supply-chain provenance. Intelligent Systems in Accounting, Finance and Management 25(1): 18–27.

Kim S, Kwon Y and Cho S (2018) A survey of scalability solu tions on blockchain. In: International conference on information and communication technology convergence (ICTC), Jeju, South Korea, 17–19 October, pp. 1204–1207. New York: IEEE.

Kishigami J, Fujimura S, Watanabe H, et al. (2015) The block chain-based digital content distribution system. In: Fifth international conference on big data and cloud computing, Dalian, China, 26–28 August, pp. 187–190. New York: IEEE.

Kiviat TI (2015) Beyond Bitcoin: Issues in regulating blockchain transactions. Duke Law Journal 65(3): 568–608.

Korpela K, Hallikas J and Dahlberg T (2017) Digital supply chain transformation toward blockchain integration. In: Hawaii international conference on system sciences (HICSS 2017), pp. 4182–4191. Available at: https://elk.adalidda. com/2017/05/paper0517.pdf (accessed 21 May 2020).

Korže SZ (2019) How smart tourism embrace blockchains and smart contracts. Mednarodno Inovativno Poslovanje 11(2): 32–40.

Kosba A, Miller A, Shi E, et al. (2016) Hawk: The blockchain model of cryptography and privacy-preserving smart contracts. In: IEEE symposium on security and privacy, San Jose, CA, 22–26 May, pp. 839–858. New York: IEEE.

Koulu R (2016) Blockchains and online dispute resolution: Smart contracts as an alternative to enforcement. SCRIPTed: A Journal of Law, Technology & Society 13(1): 40–69.

Künnapas K (2016) From Bitcoin to smart contracts: Legal revolution or evolution from the perspective of de lege ferenda? In: Kerikmäe T and Rull A (eds) The Future of Law and eTechnologies. Cham: Springer, pp. 111–131.

Lacity MC (2018) Addressing key challenges to making enterprise blockchain applications a reality. MIS Quarterly Executive 17(3): 201–222.

Lamport L, Shostak R and Pease M (1982) The byzantine generals problem. ACM Transactions on Programming Languages and Systems 4(3): 382–401.

Lauslahti K, Mattila J and Seppälä T (2017) Smart Contracts: How Will Blockchain Technology Affect Contractual Practices? Research Institute of the Finnish Economy. Available at: https://www.etla.fi/wp-content/uploads/ETLA-Raportit-Reports-.pdf.68 (accessed 21 May 2020).

Lee J, Long A, McRae M, et al. (2015) Bitcoin basics: A primer on virtual currencies. Business Law International 16(1): 21–481.

Lessig L (1999) Code: And Other Laws of Cyberspace. New York: Basic Books.

Lessig L (2006) Code: Version 2.0. New York: Basic Books.

Levy KEC (2017) Book-smart, not street-smart: Blockchain-based smart contracts and the social workings of law. Engaging Science, Technology, and Society 3: 1–15.

Lewis P (2017) Smart Contracts and Distributed Ledger: A Legal Perspective. New York: International Swaps and Derivatives Association.

Lindman J, Tuunainen VK and Rossi M (2017) Opportunities and risks of blockchain technologies: A research agenda. In: 50th Hawaii international conference on system sciences (HICSS 2017), pp. 1533–1542. Available at: https://pdfs.semanticscholar.org/7e21/09bbea4cc463dff32ab6c141968104817 26b.pdf (accessed 21 May 2020).

Liu B (2016) Can artificial intelligence ever give legal advice? Law Society of Western Australia 43(6): 8–9.

Low K and Mik E (2020) Pause the Blockchain legal revolution. The International and Comparative Law Quarterly 69(1): 135–175.

Lu Q, Xu X, Liu Y, et al. (2019) uBaaS: A unified blockchain as a service platform. Future Generation Computer Systems 101: 564–575.

Luu L, Chu D-H, Olickel H, et al. (2016) Making smart contracts smarter. In: CCS’16 (eds Weippl E, Katzenbeisser S and Kruegel C, et al.), Vienna, 24–28 October, pp. 254–269. New York: The Association for Computing Machinery.

McCarthy J (1989) Artificial intelligence, logic and formalizing common sense. In: Thomason RH (ed.) Philosophical Logic and Artificial Intelligence. Dordrecht: Springer, pp. 161–190.

Macneil IR (1977) Contracts: Adjustment of long-term economic relations under classical, neoclassical, and relational contract law. Northwestern University Law Review 72: 854.

Magazzeni D, McBurney P and Nash W (2017) Validation and verification of smart contracts: A research agenda. Computer 500(9): 50–57.

Mashatan A and Roberts Z (2017) An enhanced real estate transaction process based on blockchain technology. In: Americas conference on information systems (AMCIS 2017), pp. 1–5. Atlanta, GA: Association for Information Systems. Available at: https://pdfs.semanticscholar.org/4af1/12878d7ba2dbce42 a250bdf03da143190940.pdf (accessed 21 May 2020).

Masiak C (2019) Initial coin offerings (ICOs): Market cycles and relationship with Bitcoin and ether. Small Business

Economics. Epub ahead of print May. DOI: 10.1007/s11187- 019-00176-3.

Mehar M (2019) Understanding a revolutionary and flawed grand experiment in blockchain: The DAO attack. Journal of Cases on Information Technology 21(1): 19–32.

Mehrabi N, Morstatter F, Saxena N, et al. (2019) A survey on bias and fairness in machine learning. arXiv preprint. Available at: http://arxiv.org/pdf/1908.09635v2 (accessed 21 May 2020).

Moreno-Sanchez P, Zafar MB and Kate A (2016) Listening to whispers of ripple: Linking wallets and deanonymizing transactions in the ripple network. Proceedings on Privacy Enhancing Technologies 2016(4): 436–453.

Murphy S, Cooper C, Abrahams N, et al. (2016) Can smart contracts be legally binding contracts? Norton Rose Fulbright white paper. Available at: https://www.nortonrosefulbright. com/-/media/files/nrf/nrfweb/imported/norton-rose-ful bright–r3-smart-contracts-white-paper-key-findingsnov-2016.pdf (accessed 21 May 2020).

Nehai Z and Bobot F (2019) Deductive proof of Ethereum smart contracts using why3. ArXiv e-prints. Available at: https:// arxiv.org/pdf/1904.11281 (accessed 21 May 2020).

Ng I (2017) The art of contract drafting in the age of artificial intelligence. Working paper, Transatlantic Technology Law Forum, Stanford Law School, Stanford, CA.

Niederman F, Applegate LM, Beck R, et al. (2017) IS research and policy: Notes from the 2015 ICIS senior scholar’s forum. Communications of the AIS 40: 82–92.

Nofer M, Gomber P, Hinz O, et al. (2017) Blockchain. Business & Information Systems Engineering 59(3): 183–187.

Novo O (2018) Blockchain meets IoT: An architecture for scalable access management in IoT. IEEE Internet of Things Journal 5(2): 1184–1195.

Nugent T, Upton D and Cimpoesu M (2016) Improving data transparency in clinical trials using blockchain smart contracts. F1000Research 5: 2541.

O’Hara K (2017) Smart contracts: Dumb Idea. IEEE Internet Computing 21(2): 97–101.

Omohundro S (2014) Cryptocurrencies, smart contracts, and artificial intelligence. AI Matters 1(2): 19–21.

O’Shields R (2017) Smart contracts: Legal agreements for the blockchain. North Carolina Banking Institute 21: 177–194.

Ostrom E (2012) Nested externalities and polycentric institutions: Must we wait for global solutions to climate change before taking actions at other scales? Economic Theory 49(2): 353–369.

Park D, Zhang Y, Saxena M, et al. (2018) A formal verification tool for Ethereum VM bytecode. In: Proceedings of the 2018 26th ACM joint meeting on European software engineering conference and symposium on the foundations of software engineering, Lake Buena Vista, FL, 4–9 November, pp. 912– 915. New York: ACM.

Parra Moyano J and Ross O (2017) KYC optimization using distributed ledger technology. Business & Information Systems Engineering 59(6): 411–423.

Pashkov V and Soloviov O (2019) Legal implementation of blockchain technology in pharmacy. SHS Web of Conferences 68: 01027.

Peters GW and Panayi E (2016) Understanding modern banking ledgers through blockchain technologies: Future of transaction processing and smart contracts on the internet of money. In: Tasca P, Aste T, Pelizzon L and et al. (eds) Beyond Banks and Money. Cham: Springer, pp. 239–278.

Pisa M (2018) Reassessing expectations for blockchain and development. Available at: https://www.mitpressjournals.org/doi/ pdf/10.1162/inov\_a\_00269 (accessed 21 May 2020).

Puschmann T (2017) Fintech. Business & Information Systems Engineering 59(1): 69–76.

Raskin M (2017) The law and legality of smart contracts. Georgetown Technology Review 1(2): 305–341.

Reidenberg JR (1997) Lex informatica: The formulation of information policy rules through technology. Texas Law Review 76: 553.

Reus B (2016) Limits of Computation: From a Programming Perspective (1st edn). Cham: Springer.

Reyna A, Martín C, Chen J, et al. (2018) On blockchain and its integration with IoT challenges and opportunities. Future Generation Computer Systems 88: 173–190.

Rhim Y-Y and Park K (2019) The applicability of artificial intelligence in international law. Journal of East Asia and International Law 12(1): 7–30.

Righi R., Alberti AM. and Singh M. (eds) (2020) Blockchain Technology for Industry 4.0: Secure, Decentralized, Distributed and Trusted Industry Environment. Singapore: Springer.

Rissland EL (1989) Artificial intelligence and law: Stepping stones to a model of legal reasoning. Yale Law Journal 99: 1957–1981.

Saraph V and Herlihy M (2019) An empirical study of speculative concurrency in Ethereum smart contracts. Cornell University working paper. Available at: http://arxiv.org/ pdf/1901.01376v2 (accessed 21 May 2020).

Savelyev A (2017) Contract law 2.0: “Smart” contracts as the beginning of the end of classic contract law. Information & Communications Technology Law 26(2): 116–134.

Saxena A, Misra J and Dhar A (2014) Increasing anonymity in Bitcoin. In: Böhme R (ed.) Financial Cryptography and Data Security (Vol. 8438). Heidelberg: Springer, pp. 122–139.

Schulte S, Sigwart M, Frauenthaler P, et al. (2019) Towards blockchain interoperability. In: Di Ciccio C, Gabryelczyk R and García-Bañuelos L, et al. (eds) Business Process Management: Blockchain and Central and Eastern Europe Forum. Cham: Springer, pp. 3–10.

Schultze U and Avital M (2011) Designing interviews to generate rich data for information systems research. Information and Organization 21(1): 1–16.

Schwab K (2016) The Fourth Industrial Revolution. Geneva: World Economic Forum.

Siering M, Clapham B, Engel O, et al. (2017) A taxonomy of financial market manipulations: Establishing trust and market integrity in the financialized economy through automated fraud detection. Journal of Information Technology 32(3): 251–269.

Soh PH (2010) Network patterns and competitive advantage before the emergence of a dominant design. Strategic Management Journal 31(4): 438–461.

Sultana T, Almogren A, Akbar M, et al. (2020) Data sharing system integrating access control mechanism using blockchain-based smart contracts for IoT devices. Applied Sciences 10(2): 488.

Sury U (2019) The right to be forgotten . . . so what? Informatik Spektrum 42(3): 218–219.

Swan M (2018) Chapter five: Blockchain for business: Nextgeneration enterprise artificial intelligence systems. In: Raj

P and Deka GC (eds) Advances in Computers: Blockchain Technology: Platforms, Tools and Use Cases (Vol. 111). Elsevier, pp. 121–162. Available at: http://www.sciencedirect.com/science/article/pii/S0065245818300287 (accessed 21 May 2020).

Szabo N (1997) Formalizing and securing relationships on public networks. First Monday, 1 September, p. 9.

Tai ETT (2018) Force majeure and excuses in smart contracts. European Review of Private Law 26(6): 787–804.

Tapscott D and Tapscott A (2016) Blockchain Revolution: How the Technology Behind Bitcoin Is Changing Money, Business, and the World. New York: Penguin.

Temte MN (2019) Blockchain challenges traditional contract law: Just how smart are smart contracts. Wyoming Law Review 19(1): 87–117.

Tikhomirov S (2018) Ethereum: State of knowledge and research perspectives. In: Imine A, Fernández JM, Marion JY and et al. (eds) Foundations and Practice of Security. Cham: Springer, pp. 206–221.

Tonelli R. (ed.) (2019) IWBOSE ’19: 2019 IEEE 2nd International Workshop on Blockchain Oriented Software Engineering (IWBOSE ’19). Piscataway, NJ: IEEE.

Tsai W, Ge N, Jiang J, et al. (2019) A new framework for smart contracts taking account of law. In: 13th IEEE International Conference on Service-Oriented System Engineering, San Francisco, CA, 4–9 April, pp. 134–13411. New York: IEEE.

Tweeddale A and Tweeddale K (2005) Arbitration of Commercial Disputes: International and English Law and Practice. Oxford: Oxford University Press.

United States District Court for the Western District of New York (2016) United States of America, v. Richard Petix. US Court ruling no 15-CR-227A. New York: United States District Court for the Western District of New York.

US Securities and Exchange Commission (2017a) Investor bul letin: Initial coin offerings. SEC Investor Alerts. Available at: https://www.sec.gov/oiea/investor-alerts-and-bulletins/ ib\_coinofferings (accessed 21 May 2020).

US Securities and Exchange Commission (2017b) Report of investigation pursuant to section 21(a) of the Securities Exchange Act of 1934: The DAO. Release no 81207. Washington, DC: US Securities and Exchange Commission.

US Securities and Exchange Commission (2018) Order instituting cease-and-desist proceedings pursuant to section 21X of the Securities Exchange Act of 1934. Release no. 84553, SEC announcement file no. 3-18888. Washington, DC: US Securities and Exchange Commission.

US Structured Finance (2006) Thank you ISDA: New templates have caused an explosion in synthetic CDOs. International Financial Law Review 25(11): 20.

Venegas P and Krabec T (2017) Trust design: Balancing smart contracts utility and decentralisation risk. International Advances in Economic Research 23(4): 433–435.

Wahlgren P (1992) Automation of Legal Reasoning: A Study on Artificial Intelligence and Law. Boston, MA: Kluwer Law and Taxation.

Wall E and Malm G (2016) Using blockchain technology and smart contracts to create a distributed securities depository. Working paper, Department of Electrical and Information Technology. Available at: http://lup.lub. lu.se/student-papers/record/8885750/file/8885765.pdf (accessed 21 May 2020).

Waltl B, Sillaber C, Gallersdörfer U, et al. (2018) Blockchains and smart contracts: A threat for the legal industry? In: Treiblmaier H and Beck R (eds) Business Transformation Through Blockchain (Vol. II). Basingstoke: Palgrave Macmillan, pp. 287–315.

Wang S, Ouyang L, Yuan Y, et al. (2019) Blockchain-enabled smart contracts: Architecture, applications, and future trends. IEEE Transactions on Systems, Man, and Cybernetics: Systems 49: 2266–2277.

Wang Z, Dai W, Choo K-KR, et al. (2020) FSFC: An input filter-based secure framework for smart contract. Journal of Network and Computer Applications 154: 102530.

Watanabe H, Fujimura S, Nakadaira A, et al. (2016) Blockchain contract: Securing a blockchain applied to smart contracts. In: IEEE international conference on consumer electronics (ICCE 2016) (eds Bellido FJ, Vun NCH and Dolar C), Las Vegas, NV, 7–11 January, pp. 467–468. New York: IEEE.

Wohrer M and Zdun U (2018) Smart contracts: Security patterns in the ethereum ecosystem and solidity. In: 2018 IEEE 1st international workshop on blockchain oriented software engineering (IWBOSE) (eds Tonelli R, Ducasse S and Fenu G, et al.), Campobasso, 20 March, pp. 2–8. New York: IEEE.

World Economic Forum (2017) Realizing the Potential of Blockchain: A Multistakeholder Approach to the Stewardship of Blockchain and Cryptocurrencies. Geneva: World Economic Forum. Available at: https://www.weforum.org/ whitepapers/realizing-the-potential-of-blockchain (accessed 21 May 2020).

Wright A and de Filippi P (2015) Decentralized blockchain technology and the rise of lex cryptographia. Available at: https:// ssrn.com/abstract=2580664 (accessed 21 May 2020).

Wyatt D, Philipose M and Choudhury T (2005) Unsupervised activity recognition using automatically mined common sense. Available at: https://www.aaai.org/Papers/ AAAI/2005/AAAI05-004.pdf (accessed 21 May 2020).

Xu JJ (2016) Are blockchains immune to all malicious attacks? Financial Innovation 2(1): 25.

Yeoh P (2017) Regulatory issues in blockchain technology. Journal of Financial Regulation and Compliance 25(2): 196–208.

Yli-Huumo J, Ko D, Choi S, et al. (2016) Where is current research on blockchain technology? A systematic review. PLoS ONE 11(10): e0163477.

Zavolokina L, Dolata M and Schwabe G (2017) FinTech transformation: How IT-enabled innovations shape the financial sector. In: Feuerriegel S and Neumann D (eds) Enterprise Applications, Markets and Services in the Finance Industry (FinanceCom 2016) (Lecture Notes in Business Information Processing). Cham: Springer, pp. 75–88.

Zetzsche DA, Buckley RP, Arner DW, et al. (2019) The ICO gold rush: It’s a scam, it’s a bubble, it’s a super challenge for regulators. Harvard International Law Journal 60(2): 315.

Zhang L, Wang Y, Li F, et al. (2019) A game-theoretic method based on Q-learning to invalidate criminal smart contracts. Information Sciences 498: 144–153.

Zhang P, White J, Schmidt DC, et al. (2018) FHIRChain: Applying blockchain to securely and scalably share clinical

data. Computational and Structural Biotechnology Journal 16: 267–278.

Zheng Z, Xie S, Dai H-N, et al. (2020) An overview on smart contracts: Challenges, advances and platforms. Future Generation Computer Systems 105: 475–491.

Zhou R and Hwang K (2007) Gossip-based reputation aggregation for unstructured peer-to-peer networks. In: IEEE international parallel and distributed processing symposium, Rome, 26–30 March, pp. 1–10. Piscataway, NJ: IEEE Operations Center.

Zhou Y, Kumar D, Bakshi S, et al. (2018) Erays: Reverse engineering ethereum’s opaque smart contracts. In: SEC’18 proceedings of the 27th USENIX conference on security symposium, pp. 1371–1385. Available at: https://pdfs. semanticscholar.org/9337/6a6af7a25eddfb8436353c4396 aeac90f8fc.pdf?\_ga=2.4097526.756206481.1590070587- 2068374151.1587362146 (accessed 21 May 2020).

Zimmermann R and Whittaker S (2000) Good Faith in European Contract Law. Cambridge: Cambridge University Press.

Zohar A (2015) Bitcoin: Under the hood. Communications of the ACM 58(9): 104–113.

Zou J, Wang Y and Orgun MA (2016) A dispute arbitration protocol based on a peer-to-peer service contract management scheme. In: IEEE international conference on web services (ICWS), San Francisco, CA, 27 June–2 July, pp. 41–48. New York: IEEE.

Zupan N, Kasinathan P, Cuellar J, et al. (2020) Secure smart contract generation based on petri nets. In: Righi R, Alberti AM and Singh M (eds) Blockchain Technology for Industry 4.0. Singapore: Springer, pp. 73–98.

## Author biography

Daniel Drummer is a PhD candidate at the University of Freiburg within the department for applied computer science. He holds a Master’s Degree (MBA) with Distinction from the University of Oxford (UK), a Master’s Degree (LL.M) from the Frankfurt School of Finance and Management (Germany) and has been appointed as a Visiting Fellow at Harvard University, Boston, MA (USA).

Dirk Neumann is full professor with the Chair of Information Systems of the University of Freiburg, Germany. His research topics include Business Analytics, Text Mining and Cloud Computing. He studied information systems in Giessen (Diploma), Economics in Milwaukee, WI, USA (Master) and received a PhD from Karlsruhe Institute of Technology (KIT) in 2004. He has (co-)authored research publications at European Journal of Operational Research, ACM Transactions on Internet Technology, Decision Support Systems, and Journal of Management Information Systems.

## Appendix

## Expert interviews

We selected our interview partners based on their expertise, availability and accessibility. We have ensured to include a broad range of views, as well as a cross-industry selection. Although this does not constitute a formal random selection, we are confident to have assembled a relevant and representative panel. A complete list of interview partners is available upon request (see Appendix). The interviews typically lasted for 45–60 min and took place over a time period of 7 months in 2018 and 2019.

We follow the suggested methodology of Schultze and Avital (2011) for the design of interviews in information systems research, specifically employing the appreciative interview technique. We have combined retrospective questions about (1) experiences and observations regarding the experience of interview partners and (2) their company with conceptualizing questions regarding the structure and future of smart contracts (Gideon, 2012; Schultze and Avital 2011). Depending on the initial responses during the interview, we would follow up with more specific questions focusing on the research question at hand. Initial questions could include some of the following:

Where do you see potential applications for smart contracts in your industry and how relevant do you see their potential over a multi-year horizon?

What do you see as the biggest impediments to a faster roll-out and to an industrial-scale implementation of smart contracts?

How do you expect the interplay between the established juridical and court system on one side and smart contracts on the other side to evolve?

What technical and legal challenges are or will become relevant with the further proliferation of smart contracts?

Have you tested or implemented any smart contract proof of concepts to date? Are you planning to do so in the near future?

What role can/should information system (IS) research play to further the importance of smart contracts? What are topics at the intersection of law and technology that would warrant further academic or industry research?

Table 6. Interview partners.

<table><tr><td>Organization</td><td>Job title</td><td>Place of interview</td></tr><tr><td>1. Blockchain company</td><td>CEO</td><td>Personal interview (DK)</td></tr><tr><td>2. European bank</td><td>VP Compliance</td><td>Phone interview</td></tr><tr><td>3. US investment bank</td><td>Managing Director</td><td>Personal interview (US)</td></tr><tr><td>4. FinTech incubator in UK</td><td>Director</td><td>Personal interview (GB)</td></tr><tr><td>5. Investment fund</td><td>Principal</td><td>Personal interview (US)</td></tr><tr><td>6. Blockchain news portal</td><td>Journalist</td><td>Phone interview</td></tr><tr><td>7. Ethereum foundation</td><td>Member</td><td>Phone interview</td></tr><tr><td>8. Harvard Law School</td><td>Researcher</td><td>Personal interview (US)</td></tr><tr><td>9. Harvard Business School</td><td>Post-doctoral researcher</td><td>Personal interview (US)</td></tr><tr><td>10. US bank</td><td>Research analyst</td><td>Personal interview (US)</td></tr><tr><td>11. Harvard School of Engineering</td><td>Associate professor</td><td>Personal Interview (US)</td></tr><tr><td>12. Harvard Business School</td><td>Research fellow</td><td>Personal interview (US)</td></tr><tr><td>13. European law firm</td><td>Partner</td><td>Personal interview (CH)</td></tr><tr><td>14. European growth equity fund</td><td>Principal</td><td>Personal interview (US)</td></tr><tr><td>15. Massachusetts Institute of Technology (MIT)</td><td>Post-doctoral researcher</td><td>Personal interview (US)</td></tr><tr><td>16. Blockchain startup</td><td>CFO</td><td>Personal interview (US)</td></tr><tr><td>17. US law firm</td><td>Associate Director</td><td>Personal interview (US)</td></tr><tr><td>18. UK law firm</td><td>Partner, FinTech lead</td><td>Personal interview (GB)</td></tr><tr><td>19. UK law firm</td><td>Managing Associate</td><td>Personal interview (GB)</td></tr><tr><td>20. Massachusetts Institute of Technology (MIT)</td><td>Researcher</td><td>Personal interview (US)</td></tr><tr><td>21. Smart contracts platform startup</td><td>CEO</td><td>Personal interview (GB)</td></tr><tr><td>22. Blockchain startup</td><td>Co-founder, CTO</td><td>Personal interview (DE)</td></tr><tr><td>23. Financial derivatives blockchain startup</td><td>CTO</td><td>Personal interview (DE)</td></tr><tr><td>24. Blockchain startup</td><td>CEO</td><td>Personal interview (GB)</td></tr><tr><td>25. US commercial bank</td><td>Blockchain innovation lead</td><td>Personal interview (US)</td></tr><tr><td>26. US law firm</td><td>Partner</td><td>Personal interview (US)</td></tr><tr><td>27. US bank</td><td>Managing Director</td><td>Personal interview (US)</td></tr><tr><td>28. Financial regulator</td><td>Deputy head for FinTech sandbox</td><td>Personal interview (NL)</td></tr><tr><td>29. Smart contracts developer</td><td>Freelancer</td><td>Personal interview (NL)</td></tr><tr><td>30. Financial derivatives startup</td><td>CEO</td><td>Personal interview (GB)</td></tr></table>
