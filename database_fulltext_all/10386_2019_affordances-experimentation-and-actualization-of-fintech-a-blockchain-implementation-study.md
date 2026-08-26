---
otero_id: 10386
otero_key: "YNAWESN3"
title: "Affordances, experimentation and actualization of FinTech: A blockchain implementation study"
authors: "Wenyu (Derek) Du; Shan L. Pan; Dorothy E. Leidner; Wenchi Ying"
year: "2019"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/j.jsis.2018.10.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Afordances, experimentation and actualization of FinTech: A blockchain implementation study

![](/api/attachments/YNAWESN3/fulltext/images/b16fa6cf9b0e706e0b963d692880bb6d0d29973dfa231dd9f92c9a6c49eed72e.jpg)

Wenyu (Derek) Du<sup>a</sup>, Shan L. Pan<sup>b</sup>, Dorothy E. Leidner<sup>c,d</sup>, Wenchi Ying

<sup>a</sup> School of Economics and Management, Beihang University, China

<sup>b</sup> UNSW Business School, University of New South Wales, Australia

<sup>c</sup> Baylor University, USA

<sup>d</sup> Lund University, Sweden

## ARTICLE INFO

Keywords: FinTech Blockchain Organizational afordances Experimentation Actualization Case study

## A B S T R A C T

Blockchain, the technology underlying bitcoin, is an emerging financial technology (FinTech) that is poised to have strategic impacts on organizations. Because it is a new phenomenon, there are few studies on blockchain, and those studies have focused mainly on the technology’s po tential impacts, whereas how to efectively implement it in an organization remains unknown. Our study intends to fill that gap. Using afordance-actualization (A-A) theory as the theoretical lens, we conducted a case study of blockchain implementation in an organization that has ef fectively implemented it. We identify three afordances of blockchain in the organization and a process model whereby these afordances are actualized. The process model extends A-A theory by adding an experimentation phase where blockchain’s use cases within the organization are identified, developed and tested through conceptual adaptation and constraint mitigation. Our study makes important theoretical contributions to the literature on A-A theory, blockchain. information technology (IT) implementation, and strategic information systems (SIS). Our study can also help IT practitioners to implement blockchain efectively and extract value from their investment.

## Introduction

Blockchain is a financial technology (FinTech) first developed as the distributed ledgers for bitcoin. It used to be overshadowed by bitcoin, but in recent years it has started to attract attention in its own right and is becoming a core technology in the FinTech family (Economist, 2015b). Many practitioners and researchers have realized that the impacts of blockchain extend beyond bitcoin and even beyond the financial industry to drive change in many businesses (Economist, 2015a; Notheisen et al., 2017; Ølnes et al., 2017; Underwood, 2016). An article published in Harvard Business Review predicts that it is blockchain, and not big data, robotics, the social web, or even artificial intelligence, that is positioned to drive the most organizational changes in the coming decade (Tapscott and Tapscott, 2016).

The strategic information systems (SIS) literature has a tradition of publishing papers that examine emerging technologies with strategic impacts (Gable, 2010; Galliers et al., 2012). However, it has not yet examined the blockchain phenomenon. In general, information systems (IS) research on blockchain is limited, and scholars have mainly focused on its impacts (e.g., Kshetri, 2018;

Notheisen et al., 2017; Ølnes et al., 2017; Underwood, 2016). Although these impact studies ofer rich insights into how blockchain can change business operations, they ofer limited insights into how blockchain should be implemented within organizations. A survey conducted by State Street shows that most of the senior managers interviewed saw blockchain as the technology of the future, but few knew how to implement it (State Street Corporation, 2016). Because efective implementation is a precondition for impacts, this gap in the literature will limit organizations’ ability to extract value from their investment.

Our study is intended to unpack the black box of blockchain implementation. To guide our exploration, we adopt afordanceactualization (A-A) theory as the theoretical lens (Strong et al., 2014). The concept of afordances was first introduced by Gibson (1986), an ecological psychologist, who used it to explain how animals perceive an object. According to Gibson, animals perceive an object in terms of the action potentials that it afords rather than its physical properties. Markus and Silver (2008) define afordances in the context of IS research as “the possibility for goal-oriented actions aforded to specific user groups by technical objects” (p. 622)

Afordances do not guarantee results, because they refer to action potentials rather than actual actions or final outcomes. To transform potentials into results, actors must take goal-oriented actions to use the technology to achieve an outcome, a process known as “affordance actualization" (Burton-Jones and Volkoff, 2017: Strong et al., 2014). An effective implementation of blockchain can thus be seen as a process in which its afordances are actualized. We thus derive two research questions: (1) what are the afordances of blockchain in an organization? (2) How does an organization actualize these affordances?

To answer these two questions, we conducted an in-depth case study of blockchain implementation in an organization that has efectively implemented the technology. Our case analysis reveals three afordances of blockchain in the organization and a process model in which these afordances are actualized. The process model extends A-A theory by adding an experimentation phase, whereby blockchain’s use cases within the organization are identified, developed, and tested through conceptual adaptation and constraint mitigation.

Our study makes four important theoretical contributions. First, it extends A-A theory by adding an experimentation phase and extends the applicability of A-A theory to blockchain. Second, our study contributes to the blockchain literature by ofering insights into how the technology can be implemented efectively. Third, our study contributes to the IT implementation literature by deriving success factors that fit the specifics of blockchain and difer from prior findings. Fourth, our study contributes to the SIS literature by enriching studies on blockchain and extending A-A theory, which SIS scholars can use to examine how to implement emerging digita technologies to realize strategic impacts. From a practical perspective, our study can help IT practitioners efectively implement blockchain and extract value from their investment.

## Literature review

## Existing perspective on blockchain

Blockchain is one of the most promising technologies in the upcoming FinTech revolution (Economist, 2015b). Although it was first developed to serve as distributed ledgers tracking bitcoin transactions. blockchain's potential extends bevond bitcoin: it can change many business operations in both financial and commercial domains (Kshetri, 2018; Notheisen et al., 2017; Ølnes et al., 2017; Underwood, 2016).

A blockchain is a chain of data blocks each of which is created to record a transaction. A block has four components. The main component records the key information of a transaction. For example, in the case of a payment, the key information includes the payer’s ID, the receiver’s ID, and the amount. The hash function takes the key information and returns a hash number. The hash number can then be used to validate a transaction, because in the event that a transaction record is modified, even minimally, the hash number will be vastly diferent. If one block’s hash number difers from that of the majority in the network, the content of that block will be overwritten by the content of the majority. The hash number also helps the formation of the blockchain, because each block contains the hash number of the preceding block.

Here, we use a payment transaction as an example to illustrate how blockchain works (see Fig. 1). First, the payer initiates a transaction on the blockchain. The transaction information is recorded by a block, which is broadcast to all the nodes. The nodes validate the block by authenticating the paver and the receiver, and verifving that the paver has sufficient credit for the transaction After the validation, a confirmation message is broadcast to all the nodes, and the confirmed block is added to the chain of every node. Finally, credits are deducted from the payer and credited to the receiver. The transaction cannot be repudiated because it has been recorded by all the nodes.

Supporting this transaction is an amalgamation of IT artifacts of blockchain. The key ones are distributed ledgers, consensus mechanism, encryption mechanism, smart contracts, and immutable audit trails (see Table 1). Because we use A-A theory as our theoretical lens and affordances arise from the interactions of IT artifacts and actors, we need to understand the IT artifacts of the technology (Strong et al., 2014).

As mentioned above. because blockchain is an emerging FinTech. blockchain studies have so far been limited and researchers have mainly examined its potential impacts. Examples include data security (Underwood, 2016), supply chain integration (Kshetri, 2018), secure information sharing (Ølnes et al., 2017), and reduced transaction cost (Notheisen et al., 2017). In contrast, how blockchain should be implemented in organizations to realize these impacts remains unknown (Beck et al., 2017; Risius and Spohrer, 2017). Moreover, existing studies on the impacts are mainly based on theoretical exposition rather than empirical evidence. Our study is intended to fill these gaps

![](/api/attachments/YNAWESN3/fulltext/images/90f34e88aaea728044263814d6ed341c09e060f3f8d38f89c3ce48aed4324a25.jpg)  
Fig. 1. Structure of a blockchain and a payment transaction on blockchain.

Table 1  
IT artifacts of blockchain.

<table><tr><td>IT artifact</td><td>Description</td><td>Reference</td></tr><tr><td>Distributed ledgers</td><td>Distributed ledgers are databases maintained at different nodes instead of a central location. They are identical and each contains all the transactions</td><td>Beck et al. (2016), ∅lnes et al. (2017)</td></tr><tr><td>Consensus mechanism</td><td>The consensus mechanism is an algorithm that allows secure updating of records. The ledgers can only be updated when the majority of the nodes agree on the value of the data</td><td>Notheisen et al. (2017), Tapscott and Tapscott (2016)</td></tr><tr><td>Encryption mechanism</td><td>The encryption mechanism consists of a public key and a private key. The public key is used to encrypt the data and the private key is used to authenticate the participant</td><td>∅lnes et al. (2017), Underwood (2016)</td></tr><tr><td>Smart contracts</td><td>Smart contracts are digitally signed, computable, self-executing agreements among participants. They automatically verify and enforce the terms of the agreement</td><td>Kshetri (2018), Morrison (2016)</td></tr><tr><td>Immutable audit trail</td><td>Participants can access, inspect, and add to a ledger, thus creating an audit trail. Because the ledgers cannot be modified or deleted, the audit trail is immutable</td><td>Kshetri (2018), Underwood (2016)</td></tr></table>

## Afordance-actualization theory

Afordances have recently received much attention from IS scholars (e.g., vom Brocke et al., 2012; Burton-Jones and Volkof, 2017; Leonardi, 2013; Tim et al., 2018). An important reason is that an afordance is a property of the relationship between an object and an actor. Hence, it offers researchers a perspective from which to study both technical and social aspects (Maichrzak and Markus. 2013: Volkoff and Strong. 2013), whereas existing IT implementation studies tend to overemphasize the social aspects and treat the technical specifics as irrelevant (Strong et al., 2014; Zammuto et al., 2007). This relational property is especially important in the case of blockchain implementation. because the IT artifacts of blockchain are complex and confusing by nature (Beck et al., 2017) and their influence should not be overlooked (Strong et al., 2014).

A technology not only affords but also constrains actors from achieving certain goals (Maichrzak and Markus. 2013). Constraints arise at the intersections of IT artifacts and actors, and, in concert with afordances, help explain a phenomenon (Leonardi, 2011). IS afordance research has examined afordances at the individual (Leonardi, 2011; Majchrzak and Markus, 2013), organizational (Burton-Jones and Volkof, 2017; Leonardi, 2013), and community level (Tim et al., 2018; Vaast et al., 2017). Our study focuses on organizational-level afordances, which arise from the interactions of IT artifacts and a group of actors motivated by organizationa goals.

We adopt A-A theory as our theoretical lens (Strong et al., 2014). because it considers affordances and their actualization separately (see Fig. 2), whereas many extant afordance studies implicitly assume that afordances are de facto actualized when there are appropriate actors (Majchrzak and Markus, 2013; Seidel et al., 2013). Strong et al. (2014) define afordance actualization as “the actions taken by actors as they take advantage of one or more afordances through their use of the technology to achieve immediate concrete outcomes in support of organizational goals” (p. 70). This definition sufers from a tautology given that to “take advantage of one or more afordances” is the same as actualizing one or more afordances. Hence, we refine the definition of afordance actualization as the goal-oriented actions taken by actors as they use a technology to achieve an outcome. We remove the term “concrete” from our definition, because the term has not been formally defined and, as such, it is dificult to separate concrete from non-concrete outcomes. We also remove the word “immediate” because not all afordances will have outcomes occurring instantly at the point in time of affordance actualization, particularly in cases where the outcomes are organizational and contingent upon multiple individuals actualizing an afordance. Actions and outcomes also provide feedback to afordances, because some outcomes are unexpected (Tim et al., 2018) and because realizing basic afordances improves actors’ knowledge and this improved knowledge enables them to use the technology in a more advanced fashion (Bygstad et al., 2016).

![](/api/attachments/YNAWESN3/fulltext/images/c5e92f47a7d9c101e917211e3297a1402733ede2ec79656876863acbfa5211af.jpg)  
Fig. 2. Afordance-actualization theory (adapted from Strong et al. (2014)).

Organizational context plays an important role in afordance actualization. For example, Strong et al. (2014) find that a culture that supports patient data as a clinical resource rather than belonging to individuals facilitates the actualization of the potential to capture and archive digital data regarding patients. This is consistent with Bygstad et al. (2016), who suggest that a conducive organizational context stimulates afordance actualization, while an adverse context sufocates actualization.

Although A-A theory ofers a sound perspective to examine blockchain implementation, it has two limitations. First, the theory was developed by Strong et al. (2014) as a mid-range theory to explain the implementation of electronic health records (EHR), a packaged software with use cases based on industrial best practices. The theory may not be readily applicable to the implementation of blockchain, which lacks use cases for actors to undertake goal-oriented actions (Strong et al., 2014). A Deloitte study also re commends that organizations first explore appropriate use cases of blockchain before deploying it to mainstream users (Deano et al., 2016). This exploration aspect of afordance is not covered in A-A theory and could be an opportunity to extend the theory.

Second, although afordances and outcomes are conceptually diferent, in practice, much of the IS afordance literature, including Strong et al. (2014), does not distinguish between them suficiently (for details, see the literature review in Leidner et al., 2018). In Strong et al. (2014), afordances, such as capturing and archiving digital data and monitoring organizational operations, are in fact outcomes. An important value of affordance theory for IS research is that it captures the non-deterministic nature of outcomes by separating the action potentials that a technology can aford from the outcomes of using the technology. If we label afordances “outcomes," we are falling back on traditional IS outcomes research, which has largely failed to explain why outcomes are actualized in a particular organization but not in others and which characteristics of that organization matter.<sup>1</sup>

Moreover, some of the IS afordance studies also fail to carefully distinguish technology afordances from technology use. For example, in Majchrzak et al. (2013), the afordance of metavoicing, defined as the actions of reacting online to others’ presence, profiles, content and activities, is direct use of technology rather than afordance (Leidner et al., 2018). In our study, we carefully and intentionally separate afordances from both outcomes and use.

## Method

We chose a case study as our research method for two reasons. First, our research questions are exploratory in nature and are better answered through qualitative data (Walsham, 2006). Second, because organizational afordances and their actualization are reflected in the intricate actions of a group, a case study is needed to uncover embedded insights (e.g., Leonardi, 2013; Seidel et al., 2013; Strong et al., 2014). We used A-A theory to guide both data collection and analysis.

## Field site

We selected blockchain implementation at AirSouth Group (a pseudonym) as our research site. Founded in 2000, AirSouth Group is a Chinese conglomerate with business in aviation, tourism, logistics, financial services, real estate and other industries. The company adopted a decentralized governance structure and maintained over 400 subsidiaries served by over 15,000 suppliers. The company’s annual procurement was about RMB¥ 10 billion (about US\$ 1.5 billion). To consolidate similar procurement deals across subsidiaries and to increase control over subsidiaries’ procurement, the headquarters established a procurement division to manage procurement across all subsidiaries.

The director in charge of the procurement division knew that his team could not manage the procurement between 400 subsidiaries and 15,000 suppliers without IT support. In 2006, the division started to develop a procurement system based on Oracle’s E-Business Suite. As of 2012, the system manages all major procurement activities, from tender issuing to bidding and final selection, making the entire procurement process visible. However, despite the success of the procurement system, the division still faced two issues. First, payment between subsidiaries and suppliers was slow. For example, when a subsidiary paid a supplier, it needed to send a request to its bank, which then wired the money to the supplier’s bank. The process took three to five days, and because it occurred ofline, the payment was not digitally recorded by the procurement division. Second, a business transaction was a manually intensive process, because the participants all maintained their own ledgers and a transaction involved many manual verifications and reconciliations across these ledgers.

To address these issues, the director considered blockchain. He is an advocate of blockchain within the company. He once wrote a letter to top management advocating the idea of adopting blockchain in AirSouth. However, the blockchain discussions remained at the conceptual level due to a lack of technical support. In 2014, the director came across ChainSolution (a pseudonym), a company specializing in enterprise blockchain solutions. The two organizations started to collaborate and developed two blockchain-enabled systems. First, the blockchain-enabled wallet system allowed subsidiaries and suppliers to settle payment directly without going through a bank. Second, the blockchain-enabled transaction system allowed the procurement division, suppliers and subsidiaries to automate transactions. The success of these two systems led to the creation of a blockchain-enabled financing system that allowed small suppliers to secure loans from financial institutions

Our case is valuable in that it provides researchers access to a FinTech phenomenon that was previously dificult to investigate. First, the user organization efectively implemented blockchain at a time when few had done so. Second, the case provides us access to both the user organization and the technology provider, granting us a dual perspective on blockchain implementation.

## Data collection

Our data came from both primary and secondary sources. At AirSouth Group, we interviewed employees from the procurement division, relevant business functions (i.e., strategy division and IT division) and supplier and subsidiary representatives. For supplier and subsidiary representatives, we selected early adopters of the blockchain systems. At ChainSolution, we interviewed employees who were key participants in the implementation. In total, we interviewed 24 informants: 14 from AirSouth Group and ten from ChainSolution. The informants ranged from top executives to middle managers to operational staf. This distribution helped us form a balanced view of the implementation (see Table 2) (Klein and Myers, 1999).

We asked informants from the procurement division questions about how they collaborated with ChainSolution to develop use cases and deploy the blockchain systems among suppliers and subsidiaries. We asked informants from subsidiaries and suppliers questions such as how they used the blockchain systems and how these systems changed the ways they worked. Some informants from the procurement division were also system users, and we asked them similar questions. We also had the opportunity to observe these emplovees using the systems in their dav-to-day operations. We asked ChainSolution informants questions such as how to identify use cases, how to align blockchain artifacts with business requirements, and how to deploy the systems. Some informants participated in multiple interview sessions. Interviews were conducted until we reached the point of theoretical saturation, where new information started to repeat existing findings (Eisenhardt. 1989). We also collected secondary data. Both companies were supportive of our research, and provided us with rich internal archival data, such as proposals, business cases and evaluation reports.

Table 2  
Informant list.

<table><tr><td>AirSouth informants</td><td>ChainSolution informants</td></tr><tr><td>Chief Operating Officer (COO)</td><td>Chief Executive Officer (CEO)</td></tr><tr><td>Director, Procurement Division</td><td>President</td></tr><tr><td>Director, Strategy Division</td><td>COO</td></tr><tr><td>Operational Manager, Procurement Division</td><td>Vice President, Product Development</td></tr><tr><td>IT Manager A, Procurement Division</td><td>Chief Technology Officer (CTO)</td></tr><tr><td>IT Manager B, Headquarters IT Division</td><td>Senior Manager, Product Development</td></tr><tr><td>Executive A and B, Procurement Division</td><td>Senior Consultant, Consulting</td></tr><tr><td>Senior Accountant, Airport Operations</td><td>Director A, Business Development</td></tr><tr><td>Accountant, Airport Operations</td><td>Director B, Public Relationship</td></tr><tr><td>Manager A and B, Supplier A</td><td>Director C, Human Resources</td></tr><tr><td>Manager C and D, Supplier B</td><td></td></tr><tr><td>Subtotal: 14 informants</td><td>Subtotal: 10 informants</td></tr></table>

![](/api/attachments/YNAWESN3/fulltext/images/ae22281f8544e029b8aa8350468249ef12f71fe045e6aac012851768f6b8ea58.jpg)  
Fig. 3. Data analysis process and results.

## Data analysis

We went through three rounds of data analysis, a method commonly used in previous case studies (e.g., Andriopoulos and Lewis, 2009; Huang et al., 2017; Kotlarsky et al., 2014). In the first round, we read through interview transcripts and secondary data to code the statements that illustrated activities related to afordances and their actualization. For the data analysis process and results, please refer to Fig. 3. The research team met regularly to review emergent 1st order concepts and to ensure the consistency of the coding (Klein and Myers, 1999; Pan and Tan, 2011).

In the second round of data analysis, we clustered the emergent 1st order concepts into 2nd order themes and compared these themes against the theoretical lens (Pan and Tan, 2011). For example, when we asked AirSouth employees about how the blockchainenabled transaction system allowed them to do things diferently, we derived 1st order concepts such as potential to remove manual verification, potential to remove manual reconciliation and potential to build automatic triggers. These concepts were clustered into the 2nd order theme of potential to automate transactions, which is an afordance of blockchain in AirSouth. This phase is similar to Strauss and Corbin’s (1998) notion of axial coding.

In this phase, we also revealed themes that are not included in A-A theory. For example, when we asked the implementation team how they realized blockchain’s potential within the organization, we derived concepts such as diferentiating blockchain from bitcoin and cryptocurrency, identifying use cases and developing and evaluating use cases. These concepts were clustered into the theme of conceptual adaptation. Conceptual adaptation is not part of the actualization phase, because it is not a goal-oriented action that actors take to use the technology to achieve an outcome. It is an action that prepares the technology for actors to use. By iterating between literature review and data analysis, we confirmed that conceptual adaptation is a new theme that A-A theory has not covered.

<table><tr><td colspan="7">Table 3Summary of findings.</td></tr><tr><td colspan="2">Elements giving rise to an affordance</td><td colspan="2">Experimentation (Actions)</td><td colspan="2">Actualization</td><td>Organizational context</td></tr><tr><td>IT artifacts</td><td>Actors</td><td>Conceptual adaptation</td><td>Constraint mitigation</td><td>Usage actions (use of the technology for goal-oriented actions)</td><td>Actualized outcomes</td><td></td></tr><tr><td colspan="7">Affordance 1: subsidiaries and suppliers can settle payment directly</td></tr><tr><td>Distributed ledgers and consensus mechanism</td><td>Subsidiaries and suppliers</td><td>The implementation team separated blockchain from bitcoin and developed a use case in settling payment</td><td>Blockchain artifacts were difficult for actors to understand. The implementation team packaged the technology into a black box</td><td>Subsidiaries and suppliers settled payment via the blockchain-enabled wallet system instead of going through banks</td><td>Money transfer was instant and digitally recorded</td><td>Subculture that supports collaboration with startups</td></tr><tr><td colspan="7">Affordance 2: transaction participants can automate transactions</td></tr><tr><td>Distributed ledgers, encryption mechanism and smart contracts</td><td>Procurement division, suppliers and subsidiaries</td><td>The implementation team separated blockchain from cryptocurrency and developed a use case in automating transactions</td><td>Distributed database constrained the organization to efficiently process transactions. The implementation team created a dataset essential for transactions and stored it on blockchain</td><td>Procurement division, suppliers and subsidiaries processed transactions via the blockchain-enabled transaction system instead of going through paper-based clearance</td><td>Delays and errors in the transactions were reduced</td><td>Digitalization as the corporate strategy</td></tr><tr><td colspan="7">Affordance 3: small suppliers can secure loans from financial institutions</td></tr><tr><td>Immutable audit trail and smart contracts</td><td>Small suppliers who do not have access to loans from financial institutions</td><td>The development team developed a use case, whereby small suppliers could use blockchain records to prove their solvency and secure loans from financial institutions</td><td>This new financial service could introduce unknown risks. The implementation team started experimentation within a small community</td><td>Suppliers applied for loans by granting financial institutions access to their blockchain records; financial institutions issued loans via smart contracts</td><td>Suppliers avoided costs involved in obtaining loans and procurement division increased revenues</td><td>Culture that supports intrapreneurship</td></tr></table>

![](/api/attachments/YNAWESN3/fulltext/images/e8bdcdeab6cc11545cd5147aaf6a097e677b7c11ac846029e69ac2e31f324d88.jpg)  
Fig. 4. Afordance 1 - subsidiaries and suppliers can settle payment directly.

In the third round of data analysis, we connected the themes derived from the second round into a model following a coherent logic (Montealegre, 2002). The new model extends A-A theory by adding an experimentation phase, which consists of conceptual adaptation and constraint mitigation. We also presented the model to both AirSouth and ChainSolution employees (Pan and Tan, 2011), who acknowledged that it was accurate and a succinct summary of the reality.

After the three rounds of data analysis, we derived three sets of findings organized around afordances, experimentation and actualization.

## Findings

In this section, we present each set of findings in detail. For a summary of the findings, see Table 3. The table also demonstrates that we have carefully and intentionally separated afordances from both use and outcomes.

## Afordances

Afordances need to first exist before they can be actualized. Afordances exist at the intersections of IT artifacts and actors. We identified three afordances of blockchain at AirSouth.

## Afordance 1: subsidiaries and suppliers can settle payment directly

First, blockchain afords subsidiaries and suppliers the potential to settle payment directly (see Fig. 4). The focal IT artifacts were distributed ledgers and consensus mechanism, which were configured into a blockchain-enabled wallet system. Each subsidiary and supplier was assigned a digital wallet. The wallet contained coins that could be used to settle payment. The coins were like a cryptocurrency issued by AirSouth. One coin equaled one RMB. The initial value of coins depended on the money subsidiaries and suppliers deposited.

The wallet system allowed subsidiaries and suppliers to transfer money to each other without going through banks, and digitally recorded the payment. In the traditional approach, banks were indispensable in the payment because they were trusted intermediaries that ensured the success of the payment. Without banks, subsidiaries and suppliers could not trust each other. Banks could be removed by the blockchain-enabled wallet system because blockchain could also build trust, through distributed ledgers and consensus mechanism. ChainSolution’s senior manager for product development explained:

It’s like when you send money to another person, there are multiple people watching the transfer and the receiver cannot deny it … A record can be tampered with by a hacker, but the tampered records will soon be overwritten by others in the next round of consensus voting.

The trust mechanism underlying this afordance is consistent with previous research that shows that blockchain is a new trustbuilding machine (Economist. 2015c: Notheisen et al., 2017). However. blockchain builds trust differently from the way banks do. Banks build institution-based trust (Pavlou and Gefen. 2004). while blockchain builds what Deloitte labels “democratized trust." or trust maintained by a crowd (Piscini et al., 2016).

However, banks were not entirely removed from the payment. The deposits were still managed by a bank. To withdraw money, a supplier sent a request to the bank, to deduct the coins in its wallet and transfer the money to its bank account.

## Afordance 2: transaction participants can automate transactions

Second, blockchain afords the procurement division, suppliers and subsidiaries the potential to automate transactions (see

![](/api/attachments/YNAWESN3/fulltext/images/9445b914247ed03682018a1060bfb26c10d95d3db60c4f11d8867154fac4607f.jpg)  
Fig. 5. Afordance 2 - transaction participants can automate transactions.

Fig. 5). The term “automate” here is not a click on a button (basic use) to start an automatic process. Rather, the term here refers to an entire process enabled by IT artifacts that removes inputs from an operator and creates automation. This use of the term is similar to that in Zubof’s classification of the four roles of IT: automate, informate up, informate down and transform (Zubof, 1985). The foca IT artifacts were distributed ledgers, encryption mechanism and smart contracts that were configured into a blockchain-enabled transaction system.

Traditionally, a transaction could take days or even weeks to process, because it involved the clearance of many paper-based records. For example, when a supplier requested a payment, it needed to submit many paper-based documents to the procurement division, which verified these documents and then passed the payment request to the subsidiary. The subsidiary’s accounting department would conduct another round of verification before making the payment. During the process, there were many trips back and forth for verifications and reconciliations to resolve commonly occurring discrepancies among diferent participants’ records. Diferent participants maintained their own records and used their own standards in creating their records.

Blockchain’s distributed ledgers allowed participants access to a shared record and, as a result, reduced the need for manua verification and reconciliation. Some participants were concerned about sharing data with others, a concern that was addressed by blockchain’s encryption mechanism. As ChainSolution’s CTO explained,

Blockchain encrypts data before sharing them on the distributed ledgers. Participants can see transactions on blockchain, just like you can see bitcoin transactions in a bitcoin market. But, they don’t know who is behind each transaction, because the IDs and the contents have been encrypted.

Traditionally, after passing a payment request to a subsidiary’s accounting department, the procurement division had to constantly monitor the progress. Sometimes the accounting department forgot a payment request or a request that came later could be processed earlier. Blockchain could address these issues by deploying smart contracts that build self-executing business processes through if-then conditions. For example, if all the contractual requirements were met, money could be automatically transferred from a subsidiary to a supplier.

The mechanisms underlying this afordance are consistent with previous research showing that blockchain can enable secure information sharing between parties that do not trust each other, such as private enterprises and government agencies (Ølnes et al., 2017) and that blockchain is an efective means to automate predefined agreements (Kshetri, 2018).

## Afordance 3: small suppliers can secure loans from financial institution

Third, blockchain affords small suppliers the potential to secure loans from financial institutions (see Fig. 6). The focal IT artifacts were the immutable audit trail and smart contracts that were configured into a blockchain-enabled financing system.

The majority of AirSouth’s 15,000 suppliers were small and medium enterprises (SMEs) that had a strong need for corporate loans. Our interviews with suppliers confirmed this. The potential benefit that the suppliers mentioned most often was the potential to secure loans from financial institutions. Most suppliers could not do so and had to take private loans with high interest.

Financial institutions evaluate a company’s solvency based on formal statements, such as balance sheets, income statements and cash flow statements. Most SMEs do not appear to be strong on these statements. For instance, supplier A is a six-person company specialized in importing vehicles used in airports. Each year, the supplier received two contracts from AirSouth. Each contract was about RMB¥ 10 million (about US\$ 1.5 million). The down payment was RMB¥ 3 million and the company had to raise another RMB ¥ 5 million to start the project. An executive of the procurement division explained:

From a bank’s perspective, supplier A is not in good shape because it is in debt most of the time, except for the two months when AirSouth makes the payment. However. the company is a well-functioning SME that enioys a stable income and handsome profits.

In theory, supplier A could use AirSouth’s contracts to prove its solvency but in reality, most financial institutions do not accept this, because contracts could be forged and verifying them requires significant efort. Moreover, for SMEs, banks do not have an effective means to ensure repayment. because most SMEs lack the collateral. Blockchain can address both issues. First, all the contracts and past transactions are stored on blockchain, and thus cannot be modified or deleted. Suppliers can use this immutable audit trail to prove their solvency. Second, the smart contracts can enforce repayment, because in the event that a supplier fails to repay a loan, the smart contracts can redirect AirSouth’s future payments to the bank.

![](/api/attachments/YNAWESN3/fulltext/images/317f107acca1a2c843b0a668ec6ef29476eda08338cf4b6d9685852b84b27e75.jpg)  
Fig. 6. Afordance 3 - small suppliers can secure loans from financial institutions.

The role that blockchain plays in enabling small suppliers is consistent with prior literature that suggests that FinTech such as blockchain is efective in enabling parties that are excluded from existing financial services (Gupta and Knight, 2017). A reason for this is that blockchain can build financial institutions’ trust in small suppliers that traditional FinTech cannot achieve. The immutable audit trail builds knowledge-based trust and smart contracts build deterrence-based trust (Shapiro et al., 1992; Shapiro, 1987).

## Experimentation

Unlike in A-A theory, in blockchain implementation, an experimentation phase precedes the actualization phase. Affordance actualization refers to actions that actors take in using a technology to achieve an outcome. The precondition for afordance actualization is that the technology is ready for use. However, blockchain does not have any existing use cases other than bitcoin. An experimentation phase is needed to identify, develop and test use cases within an organization.

The experimentation is also an action needed to produce final outcomes, but it is different from the usage actions when the system is implemented. Experimentation is an action that explores a technology’s use scenarios and prepares it for actors to use. Hence, our study unveils two types of actions that translate affordances into final outcomes, experimental actions and implementation actions The experimentation phase also demonstrates that afordances, actions and outcomes are three diferent concepts (Leidner et al., 2018: Maichrzak et al., 2013).

The experimentation phase follows afordances, because afordances must first exist before the experimentation can produce feasible use cases. The identification and development of use cases also helps actors to recognize afordances. The use cases are similar to Gaver’s (1996) perceptual information or message of actions that help people to recognize technology afordances. The experimentation phase consisted of two main activities, conceptual adaptation and constraint mitigation. In the following, we wil describe each of them in detail.

## Conceptual adaptation

In their study of a Korean company adopting a managerial technology from the United States, Yu and Zaheer (2010) find that conceptual adaptation is needed when the original framing of a technology does not fit the company's aspirations. Similarly, the framing of blockchain in the context of bitcoin did not fit AirSouth’s aspiration. Therefore, a conceptual adaptation was needed for blockchain to take on new meanings in the local context.

First, when implementing the wallet system, many actors viewed blockchain as a bitcoin technology. For example, some raised the concern that the ethical issues associated with bitcoin could negatively affect the wallet system, but in fact those issues were irrelevant. Second, when implementing the transaction system, some actors still associated blockchain with cryptocurrency. For example, some questioned why a non-financial company such as AirSouth should invest in blockchain, It was therefore imperative to separate blockchain from bitcoin and cryptocurrency in general. As a senior consultant from ChainSolution explained,

If you don’t separate blockchain from bitcoin or cryptocurrency, people will always be confused about their association, which makes it difficult for people to understand why blockchain is relevant to them

Conceptual adaptation also included the identification of new use cases that re-contextualized blockchain within the organization. The key to identifying new use cases was to bridge the gap between blockchain’s IT artifacts and AirSouth’s business. ChainSolution stationed its employees at AirSouth to understand its businesses’ pain points and identify opportunities for blockchain.

However, not all use cases were feasible. For example, AirSouth’s headquarters intended to integrate the loyalty programs of subsidiaries, such as airlines, hotels and tourism, but subsidiaries did not want to give up their customer information. Blockchain provided an alternative approach, whereby subsidiaries could share customer information without giving up control of it. However, after communicating with the key stakeholders, the implementation team realized that this use case was not feasible in the short term because it involved many changes and the stakeholders were still skeptical about the value of the technology. According to the director of the procurement division,

We took an incremental approach rather than a revolutionary approach. We needed to accumulate tangible results to address people’s concerns about the technology before we could launch large-scale projects.

## Constraint mitigation

As an emerging FinTech that had not been widely adopted, blockchain could impose unexpected constraints at the intersections of technology and business context (Kendall, 1997; Leonardi, 2011). One constraint was technical complexity. Initially, the implementation team intended to explain blockchain artifacts to actors in order to stimulate interest and build a community of practice However, IT artifacts are complex and the explanation left actors more confused. Later, the implementation team adjusted its approach and packaged blockchain as a black box. As the IT manager of the procurement division explained,

The [blockchain] technology was too novel and complex for users to understand. Therefore, we kept it as a black box and only demonstrated the business applications [it supported] … In fact, what users really care about is whether the system is useful rather than wha the underlying technology is.

Another constraint was the low eficiency in handling a large number of transactions. Although distributed ledgers have many merits, retrieving, verifying and recording data on them take much longer than on a centralized database (Beck et al., 2016). This constraint was most salient in the implementation of the transaction system, which involved heavy transactions. To overcome this constraint, the implementation team identified a minimal dataset essential for transactions and stored it on blockchain. The rest of the data, which were not essential for transactions, were recorded on traditional databases. For example, for a contract, information such as supplier ID, subsidiary ID, contract amount, key specifications and dates, was recorded on the blockchain while information such as suppliers’ address and contact person was recorded on the traditional databases. As a result, the workload of retrieving and recording data on blockchain was minimized.

In implementing the financing system, the main constraint was the unknown risk. The implementation team believed that using blockchain records to demonstrate a supplier’s solvency was a novel and sound approach but that this radical innovation could also introduce unknown risks because it required the organization to step into unknown territories. To reduce such risks, the implementation team experimented with the system within a small community, where participating suppliers and financial institutions had close relationships with AirSouth. According to an executive of the procurement division,

So far, we have only launched three projects. The objective is to map out the procedure from end to end and identify potential risks. No one has done this before and we need to be yery careful.

This approach is similar to a “sandbox” approach adopted by some governments to promote and regulate FinTech. A sandbox is a controlled environment in which FinTech companies can test their solutions with a selected group of users (Lee, 2016; Meola, 2016) A sandbox not only ofers a safe environment for experimentation but also prevents experimentation from disrupting regular operations (O'Reilly and Tushman, 2008)

The experimentation phase provided feedback to elements that gave rise to afordances. For IT artifacts, results from experimentation helped adjustment of their configurations. For example, the payment use cases were used to configure the distributed ledgers and consensus mechanism in the wallet system. For actors, the experimentation changed their preference. For example. after blockchain was separated from bitcoin and cryptocurrency, suppliers and subsidiaries were more receptive to the technology.

## Extension of A-A theory

The experimentation phase is an extension of A-A theory. A-A theory is based on the implementation of EHR, an off-the-shelf packaged software consisting of established use cases also known as “industrial best practices" (Howcroft et al., 2004: Ward et al.. 2005). Because the best practice use cases help ground expectations for how the software should be used and what it can achieve, an experimentation phase is less important. In contrast, blockchain does not have any use cases and how the technology can be used in an organization remains unknown. The experimentation phase not only identifies and develops new use cases but also tests their feasibility. Use case evaluation tests their feasibility from a business perspective and constraint mitigation tests it from a technology perspective. In contrast, the business and technical feasibility of EHR have already been tested through prior installations.

The two activities of the experimentation phase fit the specifics of blockchain and differ from findings in the IT implementation literature. First, blockchain was originally designed to track bitcoin transactions and many people still associate blockchain with bitcoin. It was therefore critical to decouple blockchain from bitcoin and to frame the technology to fit the organization's aspirations. Preceding technologies, such as EHR and enterprise resource planning (ERP), are implemented in scenarios specified by designers and the implementation is often based on an industry-specific baseline solution (Abraham and Junglas, 2011; Lucas et al., 1998; Ward et al.. 2005). In this case, conceptual adaptation is less critical

Second, due to the limited number of real-world installations, blockchain technology has not been tested in practice. As such, unexpected constraints can emerge at the intersection of technology and business context, such as the low eficiency caused by distributed ledgers’ inability to support a large number of transactions. In blockchain implementation, a designated phase is needed to identify and mitigate constraints. Preceding technologies also need constraint mitigation, but it is less critical, because the constraints and their mitigation mechanisms have been documented through previous installations (Abraham and Junglas, 2011; Ward et al., 2005).

## Actualization

The actualization phase was enacted when the use cases were ready for actors to use to achieve an outcome in support of organizational goals.

## Actions and outcomes

To actualize the first afordance, subsidiaries and suppliers settled payment via the blockchain-enabled wallet system instead of going through banks. To actualize the second afordance, the procurement division, suppliers and subsidiaries processed transactions via the blockchain-enabled transaction system instead of going through paper-based clearance. To actualize the third afordance, suppliers applied for loans by granting financial institutions access to their blockchain records and financial institutions issued loans via smart contracts.

Suppliers adopted the new systems and changed their actions because the procurement division had the ability to influence them. It was more dificult to convince subsidiaries to adopt the new systems because subsidiaries were not under the direct influence of the procurement division and their accounting departments are powerful. To reduce resistance, the implementation team minimized the changes required for the accounting departments. For instance, the implementation team built a payment portal that embedded the wallet system within the accounting systems, thereby sparing the accounting departments the need to adopt another system.

Efective use of the technology led to outcomes (Burton-Jones and Volkof, 2017; Strong et al., 2014). First, money transfer between subsidiaries and suppliers became instant and was digitally recorded. Second, delays and errors in payment transactions were reduced. Third, suppliers saved costs in obtaining loans and the procurement division increased revenues.

Consistent with A-A theory, actions and outcomes provided feedback to elements that gave rise to afordances (Strong et al., 2014). Feedback from actual use and outcomes was used to adjust the blockchain systems and enable actors to have a better understanding of the technology. Actions and outcomes also provided feedback to the experimentation phase. For example, after adopting the wallet and transaction systems and deriving positive outcomes, the implementation team identified a new use case, whereby small suppliers could use their blockchain records to secure loans from financial institutions. This case led to the recognition of the third afordance.

## Organizational context

We identified three elements of organizational context that contributed to afordance actualization. In actualizing the first af fordance, a subculture that supports collaboration with startups played an important role. At that stage, several business leaders had concerns about working with a startup. The COO elaborated:

It is unusual for us, a Fortune 500 company, to work with a startup. We prefer working with established vendors. But in the case of blockchain, it seems that there are few established players.

The director of the procurement division preached to the business leaders the value of working with an innovative startup, and created a supportive environment within the procurement division for ChainSolution to innovate. ChainSolution’s employees confirmed that the supportive environment was important. This finding is also consistent with the prior literature, which suggests that incumbents should develop a culture of working with startups in blockchain implementation because startups have more advanced technical and innovative capabilities (Taylor, 2015).

In the case of AirSouth, the culture of working with a startup was not an organizational-level culture, but a subculture at the division level (Martin and Siehl, 1983). Because afordances are pertinent to specific organizational actors, a subculture can be more relevant to afordance actualization than an organizational culture. Our findings are supported by Ravishankar et al. (2011), who find that, in the case of a large knowledge-management system implementation in a global outsourcing company, subcultures have more influence on implementation efectiveness than organizational culture. This subculture of collaborating with startups also fits the specifics of blockchain implementation and difers from findings in the IT implementation literature. For example, in implementing enterprise systems, companies tend to work with established vendors with rich industry experience (Howcroft et al., 2004; Wagner and Newell. 2004).

To actualize the second afordance, the corporate strategy of digitalization played an important role. In 2009, AirSouth’s top management established digitalization as one of the corporate strategies for the next decade and encouraged subsidiaries to adopt new digital technologies to automate business processes. By framing blockchain implementation as a manifestation of this strategy, the procurement division obtained buy-in from stakeholders. This practice is also corroborated by the literature, showing that a technology's alignment with the corporate strategy is an important success factor in technology implementation (Chan et al., 1997: Preston and Karahanna, 2009).

To actualize the third afordance, a culture that supports intrapreneurship played an important role. “Intrapreneurship” refers to entrepreneurship within an established company (Pinchot, 1984). Unlike the wallet and transaction systems, the financing system was bevond the function of the procurement division. In many organizations. such pursuits would be considered a deviation of the core function and discouraged. However, AirSouth encouraged such behavior. According to the director of procurement,

![](/api/attachments/YNAWESN3/fulltext/images/1897b74de9d81b619d8a6c3238c6be240a86e0127ecb7abf4add3db59ebff5e4.jpg)  
Fig. 7. Afordances, experimentation and actualization of blockchain.

AirSouth has been encouraging internal entrepreneurship. That is an important reason why the company is growing and diversifying so fast. Given the number of suppliers and transactions, the opportunity [for the financing service] we have within the AirSouth supplier network is huge. So, next time you see me, I may be working on this new venture.

Without this intrapreneurship culture, the financing system could become a good idea that never materialized. This is common in the context of blockchain, where many ideas still remain at the conceptual level (e.g., Kshetri, 2018; Ølnes et al., 2017). This is consistent with Sambamurthy et al. (2003), who suggest that entrepreneurial actions within organizations are critical to the discovery and exploitation of new market opportunities aforded by digital technologies.

## Theoretical and practical contributions

Our study makes four important theoretical contributions. First, our study extends A-A theory by adding an experimentation phase, where use cases of a technology within an organization are identified, developed and tested through conceptual adaptation and constraint mitigation (see Fig. 7). The original A-A theory does not include an experimentation phase. One explanation is that for EHR implementation, the use cases are already in place and how the technology should be used in an organization is well understood. Although this added experimentation phase is derived from blockchain implementation, we posit that it can be applied to other emerging digital technologies that do not have established use cases, such as artificial intelligence and virtual reality. Moreover, in the original A-A theory, afordances and outcomes are mixed. This limits the potential value of A-A theory. Our study addresses that issue by separating afordances from outcomes.

Second, our study contributes to the blockchain literature by ofering insights into how blockchain can be implemented within an organization. As an emerging FinTech, the extant IS studies on blockchain have mainly focused on its impacts and little is known about how to implement it (Beck et al., 2017; Risius and Spohrer, 2017). Moreover, existing findings on blockchain impacts are based on theoretical exposition rather than empirical evidence. Our study fills that gap by identifving three affordances of blockchain based on a real-world case of implementation.

Third, our study contributes to the IT implementation literature by deriving blockchain-specific success factors that difer from prior findings (Abraham and Junglas, 2011; Howcroft et al., 2004; Koh et al., 2011; Levina and Vaast, 2005; Lucas et al., 1998; Ward et al., 2005). Because blockchain is closely associated with bitcoin, its implementation needs conceptual adaptation to undo this association and re-contextualize blockchain within an organization. Because blockchain lacks prior installations, its implementation can impose unexpected constraints upon an organization and thus requires a phase for constraint mitigation. Moreover, because startups have adyanced technical and innovative capabilities relevant to blockchain, blockchain implementation requires a culture that supports collaboration with startups.

Fourth, our study contributes to the SIS literature by enriching studies on blockchain. Recent SIS studies have examined big data (Ghasemaghaei et al., 2018; Günther et al., 2017), social media (Benthaus et al., 2016; Leidner et al., 2018) and cloud computing (Kaltenecker et al., 2015; Messerschmidt and Hinz, 2013), but little is known about blockchain. Our study will hopefully attract more attention from the SIS community to this promising technology and serve as a guide for future research. Moreover, by extending A-A theory, our study also contributes to the SIS literature, because SIS scholars can use extended A-A theory to examine how to im plement emerging technologies to realize their strategic impacts (Gable, 2010).

Our study also makes three important practical contributions by guiding future IT practitioners to efectively implement blockchain within their organizations and extract value from their investment. First, the three afordances identified here can help IT practitioners understand what blockchain can do for an organization and how blockchain complements its strategy (Chan et al., 1997). For example, because blockchain afords organizations the ability to automate transactions with external stakeholders, organizations which orchestrate a large supplier network can consider investing in blockchain.

Second, the experimentation phase can help IT practitioners re-contextualize blockchain within their organizations and develop use cases for actual use. Our findings suggest that the implementation teams should avoid use cases that introduce major changes to existing behaviors until they accumulate tangible results from incremental changes. Also, the implementation teams should pay particular attention to use cases that require frequent transactions, because the distributed ledgers are less eficient than centralized databases in processing a large amount of data. Our findings also suggest that the implementation teams can build a sandbox to experiment with use cases with unknown risk.

Third, the three elements of organizational context can help managers cultivate an environment conducive to blockchain implementation, for example forming the habit of working with startups, building a corporate strategy that supports digital transformation, and injecting an entrepreneurial spirit.

## Concluding remarks

Although the theoretical and practical contributions are rich, they must be considered in light of the limitations. First, a common criticism of single-case studies is the issue of generalizability (Walsham, 2006). Although our findings are generalizable at the analytical level because they are supported by the literature, generalization in a statistical sense is impossible with our research design (Lee and Baskerville, 2003). Future research could achieve statistical generalization by collecting data from multiple cases of blockchain implementation and statistically validating our findings.

Second, our study is based on a large organization and thus the findings may not be readily applicable to startups. Startups have fewer formal routines and face less resistance to the adoption of new digital technologies than their larger counterparts (Chen et al., 2014; Zhou et al., 2017). Future research can investigate how startups efectively implement blockchain and compare the results with our findings.

Third, our findings are derived from a case in an emerging economy where the financial infrastructure is underdeveloped. For example, the dificulty faced by SMEs in securing loans from financial institutions may not be as salient in a developed economy. Although our case selection makes the theoretical phenomenon more salient (Eisenhardt, 1989) – FinTech such as blockchain is likely to play a more significant role in regions where the financial infrastructure is immature (Gupta and Knight, 2017; Morrison, 2016) – it would be fruitful to conduct a similar study in a developed economy and compare the results with our findings

The added experimentation phase is a key contribution of this study and more research can be done to further unpack this phase. First, future studies can systematically examine blockchain’s constraints in an organization and investigate how to mitigate them. For example, the distributed database’s inability to process large amount of data constrains eficient processing of transactions. This represents a critical constraint that needs to be mitigated when applying blockchain to streamline transactions. Second, although the extended A-A theory has the potential to be generalized to other emerging technologies, such as artificial intelligence and virtual reality, these contexts may have their own specific experimentation activities. Further research could apply the extended model to these contexts and compare the results with our findings.

Finally, in addition to the designated experimentation phase, our study also observed another type of experimentation whereby advanced afordances were recognized as the basic afordances were actualized. This type of experimentation is a continuous process rather than a designated step. Future research might further examine this experimentation, exploring how it best improves learning and subsequent implementation outcomes.

## Acknowledgment

Funding for this research was provided by China’s NSFC Joint Research Fund for Overseas Chinese Scholars and Scholars in Hong Kong and Macao (71529001), and the National Natural Science Foundation of China (71402187, 71402186).

## References

Abraham, C., Junglas, I., 2011. From cacophony to harmony: a case study about the IS implementation process as an opportunity for organizational transformation at Sentara Healthcare. J. Strat. Inf. Syst. 20 (2), 177–197.

Andriopoulos, C., Lewis, M.W., 2009. Exploitation-exploration tensions and organizational ambidexterity: managing paradoxes of innovation. Organ. Sci. 20 (4), 696–717

Beck, R.. Avital, M., Rossi, M., Thatcher, JL.B., 2017, Blockchain technology in business and information systems research, Bus, Inf, Syst, Eng, 59 (6), 381–384

Beck, R., Stenum-Czepluch, J., Lollike, N., Malone, S., 2016. Blockchain: the gateway to trust-free cryptographic transactions. European Conference on Information Systems, İstanbul, Turkey.

Benthaus, J., Risius, M., Beck, R., 2016. Social media management strategies for organizational impression management and their efect on public perception. J. Strat. Inf, Syst. 25 (2). 127–139.

vom Brocke. J., Watson, R.T., Dwver, C., Elliot, S., Melville, N., 2012, Green information systems: directives for the IS discipline. Commun, Assoc, Inf, Syst, 33 (1). 509–520.

Burton-Jones, A., Volkof, O., 2017. How can we develop contextualized theories of efective use? A demonstration in the context of community-care electronic health records. Inf. Syst. Res. 28 (3), 468–489.

Bygstad, B., Munkvold, B.E., Volkoff, O., 2016. Identifying generative mechanisms through affordances: a framework for critical realist data analysis. J. Inf. Technol 31 (1), 83–96.

Chan, Y.E., Huf, S.L., Barclay, D.W., Copeland, D.G., 1997. Business strategic orientation, information systems strategic orientation, and strategic alignment. Inf. Syst. Res. 8 (2), 125–150.

Chen, J.E., Pan, S.L., Ouyang, T.H., 2014. Routine reconfiguration in traditional companies’ e-commerce strategy implementation: a trajectory perspective. Inf. Manage. 51 (2), 270–282.

Deano, D., McGovern, P., Law, M., 2016. Tech trends 2016: innovating in the digital era. Deloitte Tech Trends Reports. < https://www2.deloitte.com/content/dam/ Deloitte/us/Documents/technology/CP\_TechTrends2016\_06-09-2016%20Foreword%20zero%20based%20arch.pdf > .

Economist, 2015a. Blockchain: the next big thing or is it? The Economist. < https://www.economist.com/special-report/2015/05/09/the-next-big-thing > .

Economist, 2015b. The FinTech revolution: a wave of startups is changing finance—for the better. The Economist. < https://www.economist.com/leaders/2015/05/ 09/the-fintech-revolution > .

Economist. 2015c. The promise of the blockchain: the trust machine. The Economist. < https://www.economist.com/leaders/2015/10/31/the-trust-machine >.

Eisenhardt, K.M., 1989. Building theories from case study research. Acad. Manage. Rev. 14 (4), 532–550

Gable, G., 2010. Strategic information systems research: an archival analysis. J. Strat. Inf. Syst. 19 (1), 3–16.

Galliers, R.D., Jarvenpaa, S.L., Chan, Y.E... Lyytinen, K., 2012. Strategic information systems: reflections and prospectives, J. Strat, Inf. Syst. 21 (2). 85–90

Gaver, W.W., 1996, Situating action ii: affordances for interaction: the social is material for design, Ecol. Psychol, 8 (2). 111–129

Ghasemaghaei, M., Ebrahimi, S., Hassanein, K., 2018. Data analytics competency for improving firm decision making performance. J. Strat. Inf. Syst. 27 (1), 101–113

Gibson, J.J., 1986. The Ecological Approach to Visual Perception. Lawrence Erlbaum Associates, Hillsdale, NJ.

Günther, W.A., Mehrizi, M.H.R., Huysman, M., Feldberg, F., 2017. Debating big data: a literature review on realizing value from big data. J. Strat. Inf. Syst. 26 (3), 191–209.

Gupta. V., Knight, R., 2017. How blockchain could help emerging markets leap ahead. Haryard Business Review: < https://hbr.org/2017/05/how-blockchain-could. help-emerging-markets-leap-ahead > .

Howcroft, D., Newell, S., Wagner, E., 2004. Understanding the contextual influences on enterprise system design, implementation, use and evaluation. J. Strat. Inf. Syst. 13 (4), 271–277.

Huang, J.-S., Pan. S.L.. Liu. J., 2017. Boundary permeability and online-offline hybrid organization: a case study of Suning, China, Inf, Manage, 54 (3), 304–316

Kaltenecker, N., Hess, T., Huesig, S., 2015. Managing potentially disruptive innovations in software companies: transforming from on-premises to the on-demand. J. Strat. Inf. Syst. 24 (4), 234–250.

Kendall, K.E., 1997. The significance of information systems research on emerging technologies: seven information technologies that promise to improve manageria effectiveness. Decision Sci. 28 (4), 775–792.

Klein, H.K., Myers, M.D., 1999. A set of principles for conducting and evaluating interpretive field studies in information systems. MIS Q. 23 (1), 67–93.

Koh, S.C.L., Gunasekaran, A., Goodman, T., 2011. Drivers, barriers and critical success factors for ERPii implementation in supply chains: a critical analysis. J. Strat Inf. Syst. 20 (4), 385–402.

Kotlarsky, J., Scarbrough, H., Oshri, I., 2014. Coordinating expertise across knowledge boundaries in offshore-outsourcing projects: the role of codification. MIS O. 38 (2), 607–627.

Kshetri, N., 2018. Blockchain’s roles in meeting key supply chain management objectives. Int. J. Inf. Manage. 39 (1), 80–89

Lee, A.S., Baskerville, R.L., 2003. Generalizing generalizability in information systems research. Inf. Syst. Res. 14 (3), 221–243.

Lee, T., 2016. Singapore wants a regulatory sandbox for FinTech. Here's what it could look like. TechInAsia. < https://www.techinasia.com/mas-singapore-fintech sandbox > .

Leidner, D.E., Gonzalez, E., Koch, H., 2018. An afordance perspective of enterprise social media and organizational socialization. J. Strat. Inf. Syst. 27 (2), 117–138

Leonardi, P.M., 2011. When flexible routines meet flexible technologies: afordance, constraint, and the imbrication of human and material agencies. MIS Q. 35 (1), 147–167.

Leonardi, P.M., 2013. When does technology use enable network change in organizations? A comparative study of feature use and shared afordance. MIS Q. 37 (3), 749–775.

Levina, N., Vaast, E., 2005. The emergence of boundary spanning competence in practice: implications for implementation and use of information systems. MIS Q. 29 (2). 335–363

Lucas, H.C., Walton, E.J., Ginzberg, M.J., 1998. Implementing packaged software. MIS Q. 12 (4), 537–549.

Majchrzak, A., Faraj, S., Kane, G.C., Azad, B., 2013. The contradictory influence of social media afordances on online communal knowledge sharing. J. Comput.- Mediated Commun. 19 (1), 38–55.

Maichrzak, A., Markus, LM., 2013. Technology affordances and constraints theory (of MIS), In: Kessler. E.H. (Ed.). Encyclopedia of Management Theory, SAGE Publications Inc, Thousand Oaks, CA.

Markus. LM., Silver. M.S., 2008. A foundation for the study of IT effects: a new look at DeSanctis and Poole's concepts of structural features and spirit. J. Assoc. Inf Syst. 9 (10), 609–632.

Martin, J., Siehl, C., 1983. Organizational culture and counterculture: an uneasy symbiosis. Organ. Dyn. 12 (2), 52–64.

Meola, A., 2016. UK financial regulator opens sandbox for FinTech companies. Business Insider. < http://www.businessinsider.com/uk-financial-regulator-opens sandbox-for-fintech-companies-2016-5 >.

Messerschmidt, C.M., Hinz, O., 2013. Explaining the adoption of grid computing: an integrated institutional theory and organizational capability approach. J. Strat. Inf. Syst. 22 (2), 137–156.

Montealegre, R., 2002. A process model of capability development: lessons from the electronic commerce strategy at Bolsa de Valores de Guayaquil. Organ. Sci. 13 (5), 514-531

Morrison, A., 2016. Blockchain and smart contract automation: an introduction and forecast. PricewaterhouseCoopers Next Technology. < http://usblogs.pwc.com/ emerging-technology/blockchain-and-smart-contract-automation-an-introduction-and-forecast/ > .

Notheisen. B., Cholewa. J.B., Shanmugam, A.P., 2017. Trading real-world assets on blockchain: an application of trust-free transaction systems in the market for lemons. Bus. Inf. Syst. Eng, 59 (6), 425–440.

O'Reilly, C.A., Tushman, M.L., 2008, Ambidexterity as a dynamic capability: resolving the innovator's dilemma, Res, Organ, Behay, 28 (1). 185–206

Ølnes, S., Ubacht, J., Janssen, M., 2017. Blockchain in government: benefits and implications of distributed ledger technology for information sharing. Gov. Inf. Q. 34 (4), 355–364.

Pan, S.L., Tan, B.C.C., 2011. Demystifying case research: a structured–pragmatic–situational (SPS) approach to conducting case studies. Inf. Organ. 21 (3), 161–176

Pavlou. P A Gefen D 2004, Building effective online marketplaces with institution-based trust, Inf Syst, Bes, 15 (1). 37–59

Pinchot, G., 1984. Intrapreneuring: Why You Don't Have to Leave the Corporation to Become an Entrepreneur. Harper & Row, New York

Piscini, E., Guastella, J., Rozman, A., Nassim, T., 2016. Blockchain: democratized trust. Deloittee Insights. < https://www2.deloitte.com/insights/us/en/focus/tech trends/2016/blockchain-applications-and-trust-in-a-global-economy.html >.

Preston, D.S., Karahanna, E., 2009. Antecedents of IS strategic alignment: a nomological network. Inf. Syst. Res. 20 (2), 159–179.

Ravishankar. M.N., Pan. S.L.. Leidner. D.E.. 2011. Examining the strategic alignment and implementation success of a KMS: a subculture-based multilevel analysis, Inf Syst. Res. 22 (1), 39–59.

Risius, M., Spohrer, K., 2017. A blockchain research framework: what we (don't) know, where we go from here, and how we will get there. Bus. Inf. Syst. Eng. 59 (6), 385-409

Sambamurthy, V., Bharadwaj, A., Grover, V., 2003. Shaping agility through digital options: reconceptualizing the role of information technology in contemporary

firms. MIS Q. 27 (2), 237–263.

Seidel, S., Recker, J., vom Brocke, J., 2013. Sensemaking and sustainable practicing: functional afordances of information systems in green transformations. MIS Q. 37 (4), 1275–1299.

Shapiro, D.L., Sheppard, B.H., Cheraskin, L., 1992. Business on a handshake. Negot. J. 8 (4), 365–377.

Shapiro, S.P., 1987. The social control of impersonal trust. Am. J. Sociol. 93 (3), 623–658.

State Street Corporation, 2016. Despite positive outlook, new research from State Street reveals asset owners, managers lack readiness for Blockchain. in Press Release < http://newsroom.statestreet.com/press-release/corporate/despite-positive-outlook-new-research-state-street-reveals-asset-owners-mana > .

Strauss, A., Corbin, J.M., 1998. Basics of Qualitative Research: Grounded Theory Procedures and Techniques. Sage Publications Inc, Thousand Oaks, CA.

Strong, D.M., Volkof, O., Johnson, S.A., Pelletier, L.R., Tulu, B., Bar-On, I., Trudel, J., Garber, L., 2014. A theory of organization-EHR afordance actualization. J. Assoc. Inf. Syst. 15 (2), 53–85.

Tapscott, D., Tapscott, A., 2016. The impact of the blockchain goes beyond financial services. Harvard Business Review. < https://hbr.org/2016/05/the-impact-of the-blockchain-goes-beyond-financial-services > .

Taylor, S., 2015. Blockchain: understanding the potential. in Barclays Insights and Research. < https://www.barclayscorporate.com/insight-and-research/technology and-digital-innovation/blockchain-understanding-the-potential.html > .

Tim, Y., Pan, S.L., Bahri, S., Fauzi, A., 2018. Digitally enabled afordances for community-driven environmental movement in rural Malaysia. Inf. Syst. J. 28 (1), 48–75. Underwood, S., 2016. Blockchain beyond bitcoin. Commun. ACM 59 (11), 15–17.

Vaast, E., Safadi, H., Lapointe, L., Negoita, B., 2017. Social media afordances for connective action: an examination of microblogging use during the Gulf of Mexico oi spill. MIS Q. 41 (4), 1179–1205.

Volkof, O., Strong, D.M., 2013. Critical realism and afordances: theorizing IT-associated organizational change processes. MIS Q. 37 (3), 819–834

Wagner, E.L., Newell, S., 2004. 'Best' for whom?: The tension between ‘best practice’ ERP packages and diverse epistemic cultures in a university context. J. Strat. Inf. Syst. 13 (4), 305–328.

Walsham, G., 2006. Doing interpretive research. Eur. J. Inf. Syst. 15 (3), 320–330

Ward. J., Hemingway, C., Daniel. E., 2005. A framework for addressing the organisational issues of enterprise systems implementation. J. Strat. Inf. Syst. 14 (2) 97–119.

Yu, J., Zaheer, S., 2010. Building a process model of local adaptation of practices: a study of Six Sigma implementation in Korean and US firms. J. Int. Bus. Stud. 41 (3), 475–499.

Zammuto, R.F., Grifith, T.L., Majchrzak, A., Dougherty, D.J., Faraj, S., 2007. Information technology and the changing fabric of organization. Organ. Sci. 18 (5), 749–762.

Zhou. N., Zhang, S., Chen, J.E., Han, X., 2017. The role of information technologies (ITs) in firms' resource orchestration process: a case analysis of China's "Huangshar 168", Int. J. Inf. Manage. 37 (6), 713–715.

Zubof, S., 1985. Automate/informate: the two faces of intelligent technology. Organ. Dyn. 14 (2), 5–18.
