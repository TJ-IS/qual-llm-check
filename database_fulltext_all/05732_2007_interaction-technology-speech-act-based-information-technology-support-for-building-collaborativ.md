---
otero_id: 5732
otero_key: "WCREVG7N"
title: "Interaction technology: Speech act based information technology support for building collaborative relationships and trust"
authors: "Kuldeep Kumar; Irma Becerra-Fernandez"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.017"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Interaction technology: Speech act based information technology support for building collaborative relationships and trust

Kuldeep Kumar <sup>\*</sup>, Irma Becerra-Fernandez

Alvah H. Chapman Graduate School of Business, College of Business, Florida International University, 11200 SW 8th Street, Miami, FL 33199, United States

Available online 27 September 2005

## Abstract

This paper describes an Internet-based process for building trust between collaborative commerce partners. Integrating concepts from Winograd and Flores’ concept of speech act theory based <sup>b</sup>conversations for action<sup>Q</sup> with research on <sup>b</sup>closed loop cycles<sup>Q</sup> of trust and relationships in the disciplines of management and marketing, the paper first develops a framework for understanding trust and trust-building processes. The framework characterizes the process of building of trust as the management of commitments inherent in speech acts between requesters (customers) and performers. Furthermore, joint sense making during the conversation for action contributes to greater transparency thereby also increasing the levels of mutual trust.

The process framework is used to develop requirements for information technology support for a process and tool for building trust. The paper then goes on to describe an implementation of the conversations for action and the closed loop cycles through a web-based software tool based upon Winograd and Flores’ work. Experiences with managing commitments and closing the loop are presented through a case study in an organization that develops and maintains menu-driven voice applications for the call center industry. The case study shows the inadequacy of traditional communication technologies in managing complex, geographically distributed collaborative commitments, and shows how the use of the software tool contributes to a greater level of satisfaction and closing of the performance loop. The paper ends with a reflection on the nature of the tool, its possible uses and misuses, and the role of human wisdom in its use.

<sup>D</sup> 2005 Published by Elsevier B.V.

Keywords: Speech act theory; Conversations for action; Building relationships and trust; Interaction technology

## 1. Introduction

‘‘Fresh flowers are blooming on the battle-scarred landscape where once-bitter rivalries among suppliers, customers and competitors once took place.<sup>Q</sup> (Daft [9], p. 179)

While collaboration is the sine qua non of any organized human endeavor, it has only recently been recognized as an important idea underlying business. After decades of building upon an adversarial, Porterian<sup>2</sup> view of strategy and inter-organizational relationships, business and academic press is now embracing the religion of trust and relationships [31]. Trust is being trusted again.

Implicit in the Porterian view of inter-organizational relationships is a view of the transacting partners as opportunistic, and consequently strategy as a means for controlling the potential opportunism of the trading partners. This view of the other party as an adversarial opportunist derives from and underlies economic theories such as transaction cost economics [42], agency theory [4], and resource dependency theory [30]. In transaction cost theory and agency theory, transaction costs and agency costs are costs deemed to be incurred for protecting against and controlling the potential opportunistic behavior of the other party in the business transaction or, in case of an agency relationship, of the firm’s agents. In resource dependency theory, the focus of strategy is on minimizing dependency on others while maximizing others’ dependency on us. Hence, the approach to managing transaction costs is either to supervise closely the other party or agent, or alternately, use contracts, incentives, punishments, or technology to monitor and ensure their compliance with the contract. The former ultimately culminates into the total incorporation of the other party or the agent into the organizational hierarchy thereby achieving full control over them; in the case of the latter, instruments of control are designed and implemented to align the agent’s behavior with the firm’s interests. In either case, the key strategic thrust is one of controlling the other party’s potential opportunism:

<sup>b</sup>We agree that control is an overarching issue for business organizations. According to Yates [44], most technologies and organizational forms have had as their main objective the creation of more advanced control instruments—instruments that enable us to enhance and extend our control over processes in society and nature. Correspondingly, most of the management literature continues to provide models and tools to enhance and support control over business processes—production, distribution, marketing, sales, and so on.<sup>Q</sup> (Ciborra [6], p. 3)

In information systems, the Porterian view of the inter-organizational relationships manifests itself as the much-heralded strategic role of IT for competitive advantage, and the characterization of IS as a competitive weapon, as presented, for example, in the work of Applegate, Mc Farlan, and Mc Kenny [1]. Likewise, the logical outcome of the transaction cost perspective in information systems is the proposition that information and communication technologies are strategic mechanisms for controlling transaction risks and transaction costs of necessary, but inherently risky, intra- and interorganizational interdependencies and relationships [7,27].

However, we are beginning to realize that it is not always possible to impose complete control over our organizations or our business partners [6]. This is especially the case in those situations where the power between the two parties is evenly matched. Even in the case of unequal power, it is not always possible to observe, monitor, and control the variety of ways in which a subordinate in a hierarchy or a trading partner in a business relationship can stray from the desired behavior. The notion of incomplete contracting and consequent need for relational contracts suggests that not all possible contingencies in a relationship can be anticipated, explicitly contracted for, and monitored. Moreover, severe problems of work specification and work monitoring and acceptance can arise when the object of trade or collaboration is abstract (such as a business plan or R&D effort), uncertain, complex, and in general, less specifiable. Furthermore, in the case of international trade and global e-business, two additional complications arise [22]. First, global distances make it problematic to supervise or to observe and monitor compliance at a distance. Second, international differences in culture, legal systems and jurisdictions, and governance can make the interpretation and enforcement of contracts difficult. Ciborra, in continuing with his discussion of control observes:

<sup>b</sup>But we submit that control is difficult to achieve. Nature, society, and the economy have always been unpredictable and uncontrollable. Although technology allows us to sharpen our governance capabilities, we seem to end up deploying technology to create a world that resists control. That is what globalization is all about: not just extended transactions or higher cross-border investments. We are experiencing governance in the age of globalization is more limited than ever.<sup>Q</sup> (Ciborra, [6], p. 3)

Consequently, organizations have no recourse but to search for alternatives to control. Economists suggest control by markets as an option. Extending transaction cost economics, Malone et al. [27] predict that with information technology’s ability to reduce transaction costs, increasingly firms would be operating in a market. On the other hand, large organizations such as automobile companies and electronic companies are moving towards developing intense, long-term relationships with a few preferred suppliers. Concepts such as supplier and customer relationship management are gaining acceptance in business. Keen [21] states that relationships and trust, instead of technology, drives the growth of e-commerce. Handy [17] observed that virtual organizations tend to rely more on trust, than their traditional counterparts operating in markets.

This brings us to trust and relationships as an alternative to control. Bradach and Eccles [3] conceptualize trust as a form of control, together with traditional forms of control, markets (price mechanisms) and authority (hierarchy). However, the notion of trust implies that we are ceding a measure of control to the trusted party, thereby actually substituting trust for control. Therefore, rather than considering trust as a form of control, we prefer to characterize trust as a substitute for and complement to power and control. Business press and academic researchers have discovered that intra and inter-organizational transactions do not always exist in an atmosphere of distrust and suspicion, thus requiring reliance on control [10,18]. There are a number of real-world situations, both in the new and the old worlds, where business is conducted based upon relationship and trust between the trading parties [23]. This focus on relationships is a response to the idea of opportunism that pervades transaction cost economics and agency theory. Even as organizational theorists have been developing the concept of trust and relationships for nearly half a decade, the awareness of the role of trust and its relationship to technology in information systems literature is only recent, dating only back to the work by [19,20,23].

But all this talk about the importance of trust does little to help us understand how relationships and trust come into being. While the above literature examines the meaning of trust, and recognizes its importance in business relationships, with few exceptions, it does not address the question as to how trust can be created and sustained [38]. Decades of dwelling on strategies and tactics for guarding against possible opportunism and betrayal from our trading partners have left us with very little guidance as to how can we create and build the trust that now seems so vital to conducting business. We either naively assume that an atmosphere of trust already exists, in which case business transactions can be initiated, or a lack of such pre-existing relationships can leave us at a loss for initiating potentially mutually beneficial business endeavors. Lacking a pre-existing set of relationships, trading partners have no guidelines for initiating business transactions or building a business relationship. Despite all the attention to trust by leading observers in business and academe, very few have actually examined the mechanisms and processes by which relationships and trust are created. Finally, the role that technology plays in building relationships has been largely ignored.

The objective of this paper is to develop and describe an information technology-based process for building relationships and trust between business partners. For the purpose of this paper, business partners include customers, suppliers, co-operating companies, complementors, and competitors, both within and across organizations. Such a trust-building process will be relevant to both practice and theory building. From a practice perspective, the guidance provided by this theory-based process will provide guidelines and tools for building trust in business transactions and relationships.

From the perspective of research, by examining the process of building trust, it will lead to a deeper understanding of what constitutes trust. Herbert Simon [36] once criticized Barnard for being too preoccupied with strategic factors and theories, and failing to provide a general treatment of the design process.<sup>3</sup> Following Simon’s exhortations, understanding how organizations create new products, new methods, new strategies, and new organization forms is important. A more fundamental need is to understand how organizations create trust that underlies the very basis of sustained relationships within and across organizations. In this paper, we embark on this challenging task.

The remaining paper is structured as follows. The next Section, 2, provides an overview of the current literature dealing with building relationships and trust. Section 3 outlines our theoretical framework for the process of building relationships and trust. The next section, Section 4, specifies the requirements for information technology support for the process of building relationships. Section 5 describes ActionWorksR Metro, a tool designed for managing commitments and trust. It is followed by a <sup>b</sup>proof-of-concept<sup>Q</sup> case study describing the use of this tool in a business setting. The last section concludes with a summary and potential issues in the use of such a tool.

## 2. Previous literature on building trust

A review of the literature on trust suggests that trust and social and working relationships are built over time [15]. Dyer and Chu [14] observe that trust requires time to develop, and the longer the duration and history of interaction, the higher the level of trust. Zucker [45] identifies trust as derived from concrete experiences resulting from personal relationships that are tied to the past (process-based), tied to a person (characteristic-based), or tied to societal structures (institutional-based). Dwyer et al. [13] distinguish five phases in relationship development among trading partners: awareness of the trading partner, exploration of the benefits and risks of trading, expansion to increase personal benefits, commitment to continuity in the relationship between partners, and durability over time to develop trust. Similarly, Gabarro [15] recognizes four stages in relationship development: orientation to form an impression, exploration of expectations, testing the relationship trust, and stabilization of interpersonal contract. Lewicki and Bunker [25] point out that trust is easier to destroy than to build and that <sup>b</sup>[while] cooperative processes facilitate trust, some of the types of trust we propose can exist in competitive relationships as well<sup>Q</sup> (p. 134).

Many authors liken the process of building trust to a closed loop cycle [13–15,28,33,45]. They suggest that each successful completion of the cycle contributes to enhanced levels of trust between the partners. The cycle of trust creation is often considered as a loop of repeated interactions, in particular, between the customer’s encounter with their supplier’s salesperson, where trust is built through the repeated delivering by the salespeople on their promises. Moreover, the frequency of business contact positively influences trust, which confirms the positive feedback characteristics in the process of building trust [14,15].

Ring and van de Ven [33] describe interorganizational relationships as starting with small, informal deals that initially require little reliance on trust because they involve little risk. As such transactions are repeated over time, meeting specified norms of equity and efficiency, commitment among parties increase, eventually becoming a long-term <sup>b</sup>web of interdependent commitments<sup>Q</sup> (p. 100). In fact, according to Ring and van de Ven: <sup>b</sup>Increases in trust between parties, which are produced through an accumulation of prior interactions that were judged by the parties as being efficient and equitable, increase the likelihood that parties may be willing to make more significant and risky investments in future transactions<sup>Q</sup> [[33], p. 100].

Although the phases involved in the trust-building loop may vary somewhat among authors, the commonly accepted repetitive and positive feedback characteristics of the process of building trust indicate that successful cooperative relationships as described by this loop result in increased trust [32,33]. Sydow also describes the positive recursiveness of trust, where the cycle of trust begins with <sup>b</sup>a policy of small steps<sup>Q</sup> [[38], p. 39] and trust is the result of a positive experience with persons via <sup>d</sup>facework<sup>T</sup> commitments in exchange relations, with <sup>b</sup>frequent, repeated, and multifaceted contacts among organizations and an open exchange of information<sup>Q</sup> (p. 48) resulting in increased trust.

While the above body of literature does point to a sustainable cyclical strategy for developing and maintaining trust, it is silent on the precise tactics and steps as to how this cycle can be created and managed. Moreover, it does not address the role of information technology in sustaining this cycle. When organizations and persons transact business at a distance, information and communication technologies are key to mediating communication between the transacting parties. Thus, it is important that the role of these technologies is addressed in designing trust creating and sustaining processes.

## 3. On framing the building of trust and relationships

Before we discuss the process of <sup>b</sup>building trust,<sup>Q</sup> we need to be clear about the meaning of trust itself. The literature conceptualizes trust in two ways. First, and most commonly, trust is thought of as a <sup>b</sup>noun<sup>Q</sup> or more precisely, a <sup>b</sup>state-variable.<sup>Q</sup> As a state-variable<sup>4</sup>, it is an attribute or a property with variable values, that is attached either to the trusted party, or to the relationship between the trusting-party and the trusted party. The former deals with the <sup>b</sup>trustworthiness<sup>Q</sup> of the trusted party. The latter results in statements such as <sup>b</sup>the customer has trust in the supplier,<sup>Q</sup> or <sup>b</sup>I have trust in you.<sup>Q</sup> It is reflected in statements such as <sup>b</sup>my trust has to be earned<sup>Q</sup> or <sup>b</sup>trust was lost.<sup>Q</sup> Trust is thus conceptualized as an object like a building or an automobile that the trusting-party either has or owns, the trusted party earns, or either can lose. While in these illustrations, trust is clearly intended as a noun, as we will show later, conceptualizing trust as a state-variable is a more precise and useful conceptualization of the concept.

The second conceptualization of trust is that of a transitive <sup>b</sup>verb<sup>Q</sup> as in <sup>b</sup>In God we trust<sup>Q</sup> or in <sup>b</sup>Firestone does not trust Ford anymore.<sup>Q</sup> In these cases, trust is taken to be an action—a process-based view of trust. Trusting is something you do as opposed to something you have. As a transitive verb, it has both a subject (the trusting-party) and an object (the trusted party) of the action. Trust is thus an interaction between two parties. Following the ontology of entity-relationship modeling, the verb (the act of trusting) establishes the relationship between the subject and the object roles. This brings in an added complication. The roles of the subject and object are not fixed. They are reciprocal. The designated subject A, in acting, interacts with the designated object B. As interactions are often reciprocal (not reflexive), while party A acts on party B, B is concurrently acting on A. Thus, usually an interaction results in party A trusting (or not trusting) party B and at the same time B trusting (or not trusting A). Furthermore, the strength of A’s trust in B need not be the same as the strength of B’s trust in A.

Our assertion is that the verb and the state-variable views of trust are complementary. The act or the process of trusting during an interaction, together with the outcome of the interaction, leads to an increase or decrease in the level of trust. Now trust the noun is no longer static like a building. Its value changes as the result of the interaction. It is, therefore, a dynamically changing <sup>b</sup>state-variable<sup>Q</sup> in a statetransition where trusting during the interaction creates the transition between different levels or states of trust. Sydow [[38], p. 34–35], in the context of inter-organizational trust, uses Gidden’s concept of structuration to develop this duality<sup>5</sup>:

<sup>b</sup>From a structuration perspective one would prefer the notion of trust constitution because, in contrast to other concepts, it emphasizes both the possibility of intentional creation and the emergent development of trust and, in particular, the subtle interplay of these two dimensions of the constitution process. –Trust, even if attributed to certain personal or organizational characteristics, is mainly produced and reproduced via action, in the case of inter-organizational networks, via management interaction in particular.<sup>Q</sup> (Sydow [38])

As we are interested in the problem of building relationships and trust, we take a state-transition or a process perspective on trust. This view of trust builds upon Ring and van de Ven’s [32,33] perspectives on building relationships, Solomon and Flores [37] concept of <sup>b</sup>Building Trust,<sup>Q</sup> and Zucker’s [45] concept of <sup>b</sup>process-based trust.<sup>Q</sup> It is also compatible with Luhman’s [26] functionalist view where trust is taken as a mechanism that reduces the internal complexity of interactions.<sup>6</sup> Zucker’s concept of process-based trust – which is tied to past and expected exchanges – entails the incremental process of building trust through gradual accumulation of knowledge [24]. This <sup>b</sup>experiential knowledge<sup>Q</sup> develops from a concrete experience of social or economic exchange and is brought as an expectation to future transactions [45].

Ring and van de Ven [33] suggest that the process of building inter-organizational relationships, as illustrated in Fig. 1, is one of gradual development and evolution, and consists of a repetitive sequence of cycles made of negotiation, commitment, and execution stages. They further suggest that relationships are products of numerous such interactions and thorough these interactions trust emerges.

On the other hand, Solomon and Flores [37] maintain that trusting is a means to creating, maintaining, deepening, and restoring relationships. Thus, between Ring and van de Ven [33] on one hand, and Solomon and Flores [37] on the other, we have a reciprocal interaction between relationship and trust. Consequently, we interpret the interaction cycle proposed by Ring and van de Ven as a means for building both relationships and trust.

However, Ring and van de Ven’s interaction cycle, consisting of negotiations, commitment, and execution, is not complete. A transaction may only be considered complete when the parties to the transaction either accept the outcomes as satisfactory, rework until satisfaction is achieved, or withdraw from the transaction [[43], p. 64–66]. Declaring acceptance by the requestor or withdrawal by either party is the condition of completion. It is this completed transaction that leads to Zucker’s experiential knowledge, that, in turn, leads to increased (or decreased) levels of trust.

In addition to the experiential nature of building trust (trust as a product of accumulation of knowledge about outcomes of past transactions), the very process of interacting, that is, the process of negotiation, conversation, commitment, performance, and acceptance, by itself, also creates trust. Both Ring and van de Ven [33] and Solomon and Flores [37] come to this conclusion from somewhat different directions. Ring and van de Ven suggest that in the negotiations stage, the parties develop joint (not individual) expectations about their motivations, possible investments, and perceived uncertainties in the business deal [33]. Following the arguments of Commons [8] and Turner [39], they suggest that the development of inter-organizational relationships is grounded in the predispositions of the interacting parties to engage in mutual sense making and bonding. These sense-making and bonding processes permit parties, with initially different views of their potential purposes and expectations of a relationship, to achieve congruency in their relationship. According to them, sense making is an enactment process [40] in which organizational participants come to appreciate the potential for transacting with others by shaping and clarifying the identity of their own organization in the context of the interaction.

Process Framework of the Development of Cooperative IORs  
![](/api/attachments/WCREVG7N/fulltext/images/9fb55ed4ab31678655200455bf0aa76f07b6f24b683870e80b37d133fa5f5603.jpg)  
Fig. 1. Ring and Van de Ven diagram process network [33].

<sup>b</sup>Interaction is based upon the need among transacting parties to feel that they share a congruent understanding of an inflexible world. –Communications among parties produce this shared interpretation, and it often emerges gradually and incrementally.

–Congruency is a cumulative product of numerous interactions; through these interactions emerge trust in the good will of others and an understanding of constraints on the relationship–.<sup>Q</sup> (Ring and van de Ven [33])

Solomon and Flores [37] come to the same understanding from the perspective of authenticity. Their notion of <sup>b</sup>Authentic Trust<sup>Q</sup> is borrowed from the existentialist tradition, particularly from Kierkegaard and Heidegger. In this tradition, authenticity involves a keen awareness, both of one’s own identity and of one’s relationships with others, and a deep awareness that self-identity is fluid and uncertain and that our identities change with our circumstances and our commitments to others (Solomon and Flores [37], p. 91). Thus, interaction and trusting become a process of mutual self-discovery for the transacting parties. This discovery comes about by articulating and clarifying the object of the interaction in a dialog or conversation about it:

<sup>b</sup>People do not develop trust by forming affective attitudes or beliefs about another person. They develop trust through interaction and conversation in relationships with each other. –Authentic trust by its nature is articulated trust, trust that is <sup>b</sup>spelled out.<sup>Q</sup> As such it becomes an issue. This has double significance. For both parties, becoming aware of their obligations and responsibilities intensifies their sense of mutual identity and the significance of the relationship for each of them. –In business contexts trust is always an issue. Whether it is in the quality of product or the promptness of the delivery,—whether it is respect for the importance of confidential information or the need for joint strategy, the issue is trust, which will be articulated and negotiated, whether or not in the form of an explicit verbal agreement or a written contract.<sup>Q</sup> (Solomon and Flores [37], p. 96–97)

![](/api/attachments/WCREVG7N/fulltext/images/b511740b834e6b52c02f91057611c8c2226668073af2559adcb59246e8bab9c7.jpg)  
Fig. 2. The basic conversation for action (from Winograd and Flores [43] p. 65).

At this point, we also need to recognize that this process of mutual discovery and sense making is limited, not only to the negotiation phase of the transaction. The dialog and exchanges dealing with the clarification of requests, negotiations, commitment, and even the dialog during the acceptance stage gradually increase the levels of mutual and joint understanding through out the evolution of the interaction. Trust and relationships evolve not only through repeated cycles of interaction, but also throughout the various stages of the same interaction cycle.

Thus, from the perspective of both sense making and authenticity, the transacting parties participate in interactions through which they come to a mutual understanding of their own and the other’s identities and expectations. This interaction is manifested through a dialog or conversation that takes place between the transacting parties. Request for service, promises to perform the service as requested, the assertion that the performance<sup>7</sup> is concluded and the promise fulfilled, and the acceptance of the outcome as satisfactory, are performed as linguistic acts entered into by the requestor and the performer.

Consequently, an interaction or an exchange can be characterized as a conversation in which parties to the exchange go through cycles of request; negotiation, promises and commitment; statement of performance; and acceptance. Winograd and Flores state that there is a recurrent structure to these conversations acts that can be formalized into a network of speech acts shown in Fig. 2.

In Fig. 2, each circle represents a possible state of conversation and the arrows between them represent speech acts. The diagram outlines a network of speech acts that constitute conversations for action—conversations in which in which an interplay of requests and commissives are directed towards explicit cooperative action (see Appendix A for an explanation of the concept of speech acts).

The fundamental importance of the illocutionary or speech act is that it embodies the specification of meaning in terms of patterns of commitment entered into by the speaker and the hearer by virtue of their taking part in the conversation. Habermas observes the centrality of commitments in speech or illocutionary acts:

<sup>b</sup>The essential presupposition for the success of an illocutionary act consists in the speaker’s entering into a specific engagement so that the hearer can rely on him. An utterance can count as a promise, assertion, request, question, or avowal, if and only if the speaker makes an offer that he is ready to make good insofar as it is accepted by the hearer. The speaker must engage himself,<sup>Q</sup> [[16], p. 61].

The engagement inherent in the speech act based conversation leads to commitment, and repeated meeting of commitments leads to experiential or processbased trust:

<sup>b</sup>Trust is built step by step, commitment by commitment, on every level. –Trust must be built one step (sometimes it seems like a giant step indeed) at a time, by the way of interpersonal confrontations and mutual engagements, by the way of commitments and promises, offers and requests.<sup>Q</sup> (Solomon and Flores, [37], p. 49)

The step-by-step process of building commitment, relationships, and trust can be visualized as a linguistic dance between the interacting parties. Requests and offers and counter-offers, assertions of completion, and declarations of satisfaction, require the use of language to perform the speech acts:

<sup>b</sup>But the essence of building trust is making commitments, and wordless commitments are rare. Indeed making and honoring commitments involve precisely the same combination of words and action that build trust.<sup>Q</sup> [[37], p. 36]

Thus, a series of formalized patterns of speech acts, i.e., <sup>b</sup>conversations for action,<sup>Q</sup> embody the trust and relationship-building process. Trust and relationships are created by both the ongoing process of creating commitments resulting in common mutual understanding of expectations, capabilities, and constraints of each other and the experience-based knowledge of meeting (or not meeting) these commitments.

As a final point, it should also be recognized that during a conversation a variety of <sup>b</sup>breakdowns<sup>Q</sup> could occur. For example, the performer may not precisely understand the request. Or, after the performer declares completion, the originator of the request may not agree that the outcome is acceptable. In these cases, further conversations between the requestor and the performer can take place to resolve the breakdown. The speech acts used to resolve these breakdowns at any point in the cycle in the transaction are also part of the process of interaction and sense making, and therefore can contribute to the process of mutual common understanding and, if resolved satisfactorily, ultimately a strengthened relationship and increased trust.

## 4. Requirements for collaborative technology support for building trust and relationships: tools for conversation

Based upon the concepts from Winograd and Flores [43], Solomon and Flores [37], and Ring and van de Ven [33], in the previous section, we established <sup>b</sup>conversations for action<sup>Q</sup> as central to trust and relationship building. In this section, we discuss the role of computers and information technology in supporting these conversations.

In their seminal work, Understanding Computers and Cognition, Winograd and Flores [[43], p. 157] argue that traditional applications of computers such as decision support systems are <sup>b</sup>–not the most promising domain in which to build tools for managing.<sup>Q</sup> They observe that many systems designed by computer professionals are intended to facilitate the activity of an individual working alone. Although such tools (including word processors, filings systems etc.) are useful, they leave out the essential dimension of collaborative work. Thus, they do not fully exploit the potential of computers.

Winograd and Flores’ argument can also be extended to the current generation of computerbased systems such as enterprise resource planning (ERP) systems, supply chain management systems (SCM), and even customer relationship management (CRM) systems. Although business process models embedded in ERP and SCM systems are effective for observing the movement of information and material across the organization:

<sup>b</sup>these models are blind to the human process in which people request work and agree on what will be done, who will do it, and when it will be done; they provide no mechanism for ensuring that any customer is satisfied<sup>Q</sup> (Denning and Medina-Mora [12], p. 45).

While ERP and SCM systems operate at an organizational or inter-organizational level, they merely connect individual <sup>b</sup>desktops<sup>Q</sup> to the system, not people to people. In such systems, individual persons still work alone, albeit now embedded in pre-defined process-structures and interactions with the system.

On the other hand, collaboration and therefore the conversational dimension permeate every realm of coordinated organizational activity, whether it is computer programming, medical care, or selling flowers. The details differ from setting to setting, but there is a common theoretical basis and a common regular structure of these conversations (Winograd and Flores [43], p. 158).

Winograd and Flores suggest that a more promising avenue for utilizing the potential of computers would be the use of computer-based tools for supporting conversations for action. Their basic argument is that organizations exist as networks of speech acts, primarily directives and commissives. Directives include orders, requests, counter-requests, consultations, and offers. Commissives include promises, acceptances, and rejections. Furthermore, breakdowns in the process of interaction inevitably occur. In coping with breakdowns, further networks of directives and commissives are generated. To develop the conversations consisting of patterns of these directives and commissives people issue utterances by speaking or writing. They participate in the creation and maintenance of a process of communication and joint sense making. At the core of this process is the performance of linguistic (or speech) acts that establish different types of commitments. Based on Solomon and Flores’s and Ring and van de Ven’s argument, the process of joint sense making and the experience of satisfied commitments build trust and relationships.

The networks of commitments and the conversations in which people participate become wider in scope as we venture into inter-organizational value production systems. Moreover, if the inter-organizational interaction is among parties who were strangers before the initiation of the interaction, the conversation for joint sense making becomes even more complex as we can no longer rely on previously developed mutual understanding and shorthand for communication. In the case of global trade and e-business, the lack of a common cultural base, global gaps<sup>8</sup>, and poly-contextuality make these conversations even more complex [23].

The complexity of the conversation also increases as often a part of the work needed to perform on the commitment is delegated or outsourced to another person, organizational sub-unit, or another organization. Thus, a commitment to perform some work may generate further commitments, which in turn may generate further sub-commitments, resulting in a network of cascading commitments. The satisfaction of a particular commitment then is contingent on the satisfactory performance of all its cascading sub-commitments. Moreover, any breakdowns in sub-commitments travel upstream the cascade thereby increasing the complexity of the breakdown monitoring and resolution process.

It may argued that traditional communication tools, such as phone-calls, letters, faxes, and e-mails can be used to manage these conversations for action. However, in today’s business interactions and relationships, the complexity of such conversations has gone beyond the point where it can be managed without appropriate tools. In other than the simplest interactions, the task of remembering the structure of roles and associated responsibilities in a business transaction, contexts of interactions, and the cascading networks of speech acts and commitments and responding to them through appropriate reactions and speech acts is beyond the cognitive limits of human information processing. Moreover, given the complexity, participants in the interaction often do not (or cannot) specify the roles, interactions, commitments, and express their satisfaction (or dissatisfaction) with the completion, with adequate explicitness, completeness, and specificity. Winograd and Flores maintain that it is in the realm of supporting such human interactions where computers can provide the most advantage.

In order to realize this, Winograd and Flores exploit the theoretical basis of illocutionary acts and the recurrent structure of conversations for action. They observe that the rules of conversation are not arbitrary conventions like the rules of chess, but reflect the basic nature of human language and action:

<sup>b</sup>There are surprisingly few basic conversational building blocks (such as request/promise, offer/acceptance, and report/acknowledgement) that frequently recur in conversations for action. The development of a conversation requires selection among a certain finite set of possibilities that is defined by the opening directive and the subsequent responses. It is like a dance, giving some initiative to each partner in a specific sequence.<sup>Q</sup> [[43], p. 159].

The taxonomy of speech acts and the diagram of conversation structure presented in Fig. 2 deal with the fundamental ontology of linguistic acts. Winograd and Flores assert that this taxonomy and the ontology provide a basis for design of tools to operate in the linguistic domain of conversations for action [[43], p. 158–159]. These tools can be used in requesting, creating, and monitoring commitments. Using the recurrent structure of conversation, they can provide relevant answers to the questions <sup>b</sup>What can I (or do I need to) do next?<sup>Q</sup> By scanning the network of commitments represented in the tool they can answer, <sup>b</sup>What is the status of my active and unfulfilled commitments?<sup>Q</sup> or <sup>b</sup>breakdowns in which sub-commitments are likely to affect the performance of dependent commitments?<sup>Q</sup>

Winograd and Flores are careful in stating that they are not suggesting that the computer can <sup>b</sup>understand<sup>Q</sup> speech acts by analyzing natural language utterances. What they are suggesting is that the parties to the conversation can be made aware of the structure of the conversation and be provided tools for working with it explicitly. The conversationalists, through a software system on a platform of computers and communications network, can share these tools and the tool-based representation of the network of speech acts. The objective of the computer system would be to make the interactions transparent—<sup>b</sup>to provide a ready-tohand tool that operates in the domain of conversation for action<sup>Q</sup> (Winograd and Flores [43], p. 159). According to them, the functional requirements for such a tool include facilities for speech act origination and identification; monitoring completion; keeping temporal relationships between a network of cascading commitments; and periodic or on request examination of the network to show status of various commitments. Winograd and Flores’ specification of these requirements is excerpted in Appendix B of this paper. By embedding these requirements for the structure of the conversation in a computer-based tool, we can ensure that the conversations are carried out in a manner such that all participants to the interaction have a common understanding of the status of the interaction, and the status of the interaction can be monitored to completion.

## 5. ActionWorksR Metro: technology support for conversations for action

The above requirements for a tool for supporting conversations for action are implemented through ActionWorksR Metro. ActionWorksR Metro is a web-based collaborative commerce software developed by Action Technologies (www.actiontech.com), a firm founded by Terry Winograd and Fernando Flores [11]. Collaborative commerce software, also called interaction technology, coordinates human interaction in the uncertain business of inventing, designing, developing, deploying, and supporting new products and services, while negotiating the legal and financial conditions required by the transaction [41]. Collaborative commerce software is based upon the taxonomy of speech acts ("<sup>N</sup>41) and exploits the conversation structure (Fig. 2) described in Section 3 of the paper.

In ActionWorksR Metro, the structure of speech acts in the conversation is organized into a closed loop structure, called the Business Interaction Model, shown in Fig. 3. The closed loop structure is based upon the recurrent structure of conversations shown in Fig. 2 above. Denning and Medina-Mora [12] describe the basic elements of this closed loop:

<sup>b</sup>A closed loop. . .that connects two parties. One of them promises to satisfy a request of the other. . .The loop consists of four stages separated by four speech acts. . .First the customer make a request of the performer. . .Second, they negotiate on the conditions that will satisfy the customer. . .Third, the performer does the work and ends by declaring that it is done. Fourth, the customer accepts the work and declares satisfaction<sup>Q</sup> (p. 45).

![](/api/attachments/WCREVG7N/fulltext/images/cd5f091fad8b467125e9ba1956896eccbc70abc99fe6d0a09d745a9865fd5d06.jpg)  
Fig. 3. Basic elements of the coordination process.

This closed loop structure in Fig. 3 is similar to Ring and van de Ven’s process framework for the development of cooperative inter-organization relationships as described in Fig. 1. Ring and van de Ven observe that the process of building inter-organizational relationships is one of gradual development and evolution, and consists of a repetitive sequence of cycles made of negotiation, commitment, and execution stages [32,33]. They suggest that relationships are products of numerous such interactions and thorough these interactions trust emerges.

However, there are two minor and one major differences between the Ring and van de Ven cycle and ActionWorksR Metro closed loop. First, the former separates the phases of <sup>b</sup>negotiation<sup>Q</sup> and <sup>b</sup>commitment<sup>Q</sup> whereas the latter combines them into a single phase. This difference is easily resolved when one considers the nature of a speech act as conceptualized by Winograd and Flores. A negotiation consists of a series of utterances or speech acts. As discussed in Section 3, a speech act, through engagement, embodies commitment (also [16]). Thus ActionWorksR Metro’s negotiation phase includes Ring and van de Ven’s both negotiation and commitment phases. The second minor difference is the inclusion of the <sup>b</sup>preparation<sup>Q</sup> of the customer’s request in ActionWorksR Metro as the first phase of the loop. This too is easily accounted for, as Ring and van de Ven take this phase to be as part of their opening of the negotiation phase.

The key difference between the two closed loops is the inclusion of the <sup>b</sup>Acceptance<sup>Q</sup> phase in the ActionWorksR Metro loop. According to Winograd and Flores, a transaction can only be considered complete when the parties to the transaction either accept the outcomes as satisfactory, rework until satisfaction is achieved, or withdraw from the transaction.<sup>9</sup> It is this successful completion that closes the loop and leads to strengthening of the relationship and associated increases in trust levels. When each work process loop ends with customer satisfaction, stronger relationships and increased trust are fostered among transacting parties. In order to carry out their commitments, the performer may be the customer of others to whom she or he delegates or out sources work. In this way, performers and customers are engaged in a network of tasks and commitments necessary to complete the original request. On the flip side, breaks in the loop <sup>b</sup>lead to negative outcomes, such as distrust and

## a

## Holly Ross requested on 12/12/2000 02:25 PM

Hello Kathryn,

We need to create a new custom gift book for our customers and we would like you to bid on it. We need 14,000 books chronicling the history and growth of the Pirelli Tire Company. Weíd like each book embossed (on the front cover) with the image of the Pirell P6 tire with Borrani wire wheel. Each of our North American tire dealers will be getting one of these. Please see the attached photo file and history archive file as well as the specs on the wheel design. Our budget is \$140,000 and we need them by March 22, which is the date of our North American dealer meeting. Can you do it under these conditions? Holly

Due date set to 13/Dec/00 05:00P Start date set to 13/Dec/00 09:00A Effort set to 60 hours

## b

Kathryn McGovern commented on 12/12/2000 02:48 PM We'd love to get a chance to work with you on this exciting project. We will need to look carefully at the drawings, text and color pictures; with our current backlog and your deadline, we will need to work overtime to get this done. I can say the minimum price would be \$215,000 and that's still conditional to our full agreement. Holly Ross followed-up on 12/12/2000 02:49 PM If you can do it for that price, and to our specifications, I have received the extra budget. However, I can't go any higher.

Due date changed to 22/Mar/01 05:00P Kathryn McGovern agreed on 12/12/2000 02:53 PM We’d be happy to do it at that price and delivery date.

30 additional hours requested

## c

Kathryn McGovern reported work done on 3/12/2001 02:57 AM This is done. Please note that we did not emboss the books.

Due date changed to 22/Mar/01 05:00P 80 hours reported for manufacturing on 12/Dec/00

## d

Holly Ross did not accept work done on 3/13/2001 07:59 PM The due date of this work item is closed; please consider it in your plans. I'm sorry Kathryn, but this will not work. We need the books embossed as agreed. We did not agree on eliminating the embossing. We consider this to be a key design feature for the not agree on eliminating the embossing. We consider this to be a key design feature for the book.

Kathryn McGovern reported work done on 3/17/2001 07:24 AM Sorry for the oversight, I have embossed the books as you specified. We are losing money on this contract but it was our fault. Even so, we want you to be satisfied and to continue to do business with us.

20 hours reported for Re-work on 12/Dec/00 HOLLY ROSS ACCEPTED WORK DONE AS-IS ON 3/18/2001 09:04 AM Thanks, Kathryn! I received them today and I am completely satisfied. You can be sure you will be our primary supplier of high-end four-color gift books.

damaged reputation, both of which can render an organization ineffective<sup>Q</sup> [[12], p. 55].

In the <sup>b</sup>Business Interaction Model,<sup>Q</sup> the person making the requests assumes the role of the customer, while the person doing the work takes on the role of the performer. The model is a <sup>b</sup>closed loop<sup>Q</sup> because the customer starts the loop of business interactions that becomes closed when the customer declares satisfaction. The customer role decides and accepts work as being complete; satisfaction with the work done is evaluated against explicit conditions. Business interactions that end with customer satisfaction are expected to result in an stronger relationships and increased trust.

The Business Interaction Model describes the relations between customers and performers based on the following concepts:

A strong definition of roles—every agreement clearly defines who is the customer and who is the performer.

Maintaining the context of all business interactions necessary to achieve fulfillment of the customer request—the context defines the current status of the interaction, what actions have been performed, what actions come next, and who is required to do them. The context is based upon the precedence relationships identified through the recurrent structure of conversations outlined in Fig. 2. The tool helps its users in structuring their conversation. Using the precedence relationships in Fig. 2, at the end of each utterance or speech act, the system helps the user select the speech acts that can logically follow it to completion. For any commitment in the network, it also keeps track of the dependencies between it, its delegated or outsourced commitments, and the commitments that depend on it. Thus, the software tool maintains the complete context of the business interaction.

Conditions of satisfaction are explicitly specified so that interactions are focused on completely satisfying the customer—these conditions negotiated in the negotiation phase provide the benchmark against which completion is assessed in the acceptance phase.

Here, we use a simple example to illustrate the use of the business interaction model. Fig. 4a through d illustrate how the technology assists the interaction between the customer (Holly Ross), and the performer (Kathryn McGovern) [41]. To keep the illustration simple, only a single loop with no subsidiary loops is presented. In Fig. 4a, the preparation phase, the customer proposes the work to the performer, in this case a new custom gift book. In Fig. 4b, the negotiation phase, the customer and performer negotiate and agree on the work to be performed, and the conditions of satisfaction are explicitly specified including cost and delivery time. The delivery date could be explicitly specified as a result of the negotiation, or the process could have a predetermined cycle time, say for example 14 days, and the due date would be specified by the system as 14 days after the start date. The speech acts, especially the assertives, directives, and the commissives have commitment inherent in them. In Fig. 4c, the performance phase, the performer performs the work and reports completion. In Fig. 4d, the acceptance phase, the customer evaluates the work done against the specific conditions of satisfaction expressed in the negotiation phase. This phase closes the business interaction loop, and by ensuring the customer’s conditions of satisfaction are met, facilitates the building of trust over time. Moreover, the process of interaction during the four phases increases the mutual awareness and understanding, building relationships [33] and authentic trust [37].

People learn to trust others by observing the consonance of their actions with their speech acts; for example, promising to do something and fulfilling the promise earns trust between transacting parties [29]. Action Technologies’ ActionWorksR Metro enables trust building by repeatedly asking the customer, <sup>b</sup>are you satisfied that we (the performer) have met the conditions we agreed on at the time we negotiated this agreement?<sup>Q</sup> This explicit and recurrent questioning, for every interaction, exposes shortcomings in the relationship, creates opportunities to repair dissatisfaction and produces relationships that are built on trust.

The value of the ActionWorksR Metro technology is in first assisting collaborators to structure the conversations for explicitness, completeness, and specificity, and then keep track of what they have committed to be accountable for, what they have delivered, and if the customer is satisfied. It helps further by assisting the interacting parties in clarifying poorly defined commitments thereby both increasing mutual awareness and reducing expectations ambiguity. In that process, it builds trust among collaborators over time. Organizations lacking such a technology often find themselves relying on traditional communication technologies, such as e-mail, to accomplish this task. Traditional communication technologies have no notion of accountability, and no mechanism to track against a specific task or project [11]. Moreover, they leave the important task of structuring and ensuring the completeness of the conversational elements to people subject to the cognitive limits of human information processing. Therefore, simple communication technologies are not adequate to the tasks of structuring interactions and tracking commitments, processes, and projects. Furthermore, ActionWorksR Metro technology can connect commitment cycles together in a cascading effect (also called dependencies) so that changes in once cycle, for example delivery time, will automatically propagate to interconnected dependencies [11,12].

## 6. ActionWorksR in action: proof of concept at CCPS

In this section, we illustrate the use of the ActionWorksR Metro closed loop in managing the commitment cycles in the new product development process for International Truck and Engine Corporation.<sup>10</sup> International Truck and Engine Corporation manufactures medium-duty to heavy-duty trucks and school buses, has around a 40% market share and is in the top three among its competitors. However, in the fourth quarter of 2002 Navistar faced a net loss for the year, as a result of decreased demand and increased competition. The industry had a massive global overcapacity and was facing a possible consolidation among the top ten players, resulting in each player taking aggressive moves to cut costs primarily through productivity improvements.

To maintain its dominant market position, International needed to launch a new product development process to speed the introduction of new truck models, reduce rework, and cut costs significantly. Traditionally, International’s assembly line was marked by a needless proliferation of the possible number of powertrain combinations, which pushed the individual vendor components’ quantity down and consequent price up. The new business process redesign at International focused on reducing this complexity by limiting the number of combinations available, buying components in bigger volumes, and focusing collaboration efforts with suppliers on improved performance issues. As summarized by Navistar’s CEO John Horne:

<sup>b</sup>Our current medium truck has more than 800 combinations of engines and transmissions. It’s nuts. The new truck has 34 combinations, and every one of them works better than before because our engineering people had the time to really develop them so they feel good to the driver<sup>Q</sup> [5]

In order to accomplish this goal, business process management became a strategic priority at International. In particular, the product change management (PCM) process, associated with new product development, had to be dramatically improved in terms of quality, speed, and reliability. The PCM process needed a better way to collaborate, not only internally, but with customers and suppliers as well. They needed a solution that would reduce cycle times, ensure quality (i.e., applications that met specifications and deadlines), improve productivity, and enhance coordination and relationships with customers and suppliers.

The PCM process involves about 1000 employees in production facilities located across the US, Mexico, and Canada, as well as external suppliers. Since International had dispersed teams across the world, a robust web-based solution with geographically dispersed reach was required. They required a solution that had an interactive, collaborative business structure built into the software that would coordinate work, and by extension, the people performing the work. By doing so, work could be put into context: exactly what work is required? Who is asking for the work to be performed (i.e., who is in the role of the Customer)? Who has to perform the work (i.e., who is in the role of Performer)? When is the work due? What are the conditions for satisfaction? Which of these have been met and which remain unmet? Moreover, International wanted a system that could help achieve continuous process improvement by creating a database of past experiences. This, in turn, would help improve customer and supplier experiences with the system, thereby improving longer term customer satisfaction and customer relationships.

The PCM process has for key phases:

Change request—where all ideas for product change and innovation are created and debated. Initiated in response to a market opportunity or customer demand.

Change proposal—electronically routes the ideas for review, approval, or rejection and results in a detailed functional specification for a new or improved component or system.

Change development—involves establishing and staffing an engineering team, as well as providing the authorization of work and the full design, development and engineering release of the change order. This phase requires intense negotiation.

Change implementation—where new product features or enhancements are put into full production.

Fig. 5a illustrates the PCM process.

To better support the PCM process, International developed the PCM system, a collaborative commerce application centered on managing and coordinating the negotiations that constitute this process: requests, collaborative agreements and commitments, and approvals.<sup>11</sup> Its objective was to coordinate work between its geographically dispersed sales teams, suppliers, and customers in an integrated supply chain.

The streamlined PCM process is described in terms of the loops that form the core of the system design and implementation.

For example, a program manager from one of the product centers acts as the customer in the Business Interaction Model. Typically, a program manager responds to customer requirements and market information by generating the work authorization (or customer request in the Business Interaction Model) and initiates the preparation stage of the model. The lead engineer, acting as the performer in the Business Interaction Model, receives the work authorization. The work authorization can included one to many changes or work packages.

Once those work packages have been reviewed, they are distributed to various internal teams and outside suppliers (performers) according to a set of rules enabled by the principles of the conversation for action (Fig. 2) and the Business Interaction Model (Fig. 3). The Model allows work to be performed by either parallel or sequential processes. The program manager is not obliged to manually advance work since the system does this automatically. Regardless of the group receiving the work package, there is opportunity for negotiation and information sharing between participants. These interactions are unlimited and can be passed back and forth until both parties are satisfied with the results.

One of the key benefits of using the Model is that no step in a process is considered complete until it is done according to the satisfaction of the customer for that particular step. In other words, a business process designed using the Business Interaction Model becomes a series of loops, representing interactions between parties involved at different stages of the overall process. When a step is done correctly a loop is closed, and the process continues. Using this model ensures that each constituent step of a job is done accurately and to closure, leading to a desired end-result of accountability and quality assurance.

In PCMS, the business process is launched by a request from the program manager. The four stages in the Business Interaction Model as handled by PCMS are outlined below:

Preparation: The program manager issues a work authorization through PCMS to the engineering team. As a result, one or many work packages are associated with the work authorization. Once the lead engineer receives the work authorization, the negotiation process begins.

Negotiation: The negotiation process begins with the program manager via the PCM system, to clarify the conditions of satisfaction, which are made explicit via the PCM system, including the work to be performed and the date by which it is to be completed. Only then does the process move into the performance stage.

Fig. 5b represents the work authorization at this stage of the process. The negotiation is a critical step in International’s PCMS. Having a clear understanding of the engineering specifications has reduced the overall rework of International’s product changes by 33%, representing significant cost savings.

Performance: Once the work authorization has been agreed upon, the change request moves into the performance phase of the process. Each of the engineers involved in the change request work on their respective portions of the change. Each work authorization can generate a set of cascading commitments (both in terms of specifications and deadline) within engineering and between engineering and its suppliers. Moreover, the engineers and suppliers are often geographically dispersed thereby creating the need for managing commitments over distance. The production processes to develop and deliver a work authorization is complicated, requiring frequent interaction between various participants: engineers, program managers, and external suppliers. Traditionally, this interaction consisting of customer requirements specification, clarification, negotiation, and approval, took place through voice (telephone and meetings), paper, faxes, and e-mails. In the past, often product changes would sit idle for days or even weeks, lost in the system. Together, the demand and supply side complexities led to problems of unmet specifications, inadequate designs, and missed deadlines. Informally documented requests and casually tracked commitments lead to misunderstandings, frustrations, and potential conflicts between various parties thereby often leading to damaged relationships and trust. Moreover, combined, these issues, together with the frequent breakdowns in the process, made cycle times unnecessarily long and hampered productivity.

Gathering information about the status of the change requests would consume around 16 h of the engineering staff week. The PCM system provides complete visibility into the process to all of those involved. In the words of Lynn Wolfe, head of one engineering group:

<sup>b</sup>In the past I would receive a phone call demanding to know the status of a work package. It would take 20 minutes to find the needed information, and I would often spend 2–3 hours on the phone per day. The new system cuts search time from 20 minutes to under 1 minute, and I get fewer calls, because all the parties involved in the process have access to PCMS.<sup>Q</sup>

Computer support for such a system, in addition to keeping track of the requests and commitments, provides real-time visibility to all participants throughout the supply chain. Everyone involved is able to track the status of a work authorization and its related commitments and their contingent dependencies to deliver particular elements of the application at specific times.

Acceptance: Once a work package is complete, the lead engineer sends the change to the engineering release integrity group (ERIG), to approve or reject the work performed. In addition, a release review board, consisting of representatives from engineering, product centers, manufacturing teams, and program teams further validate the work package completion. The review board utilizes a process named the Gauntlet, for reviewing and approving the work packages. Fig. 5c describes the Gauntlet.

The Gauntlet is used to determine compliance with the conditions of satisfaction: checks the design intent, verifies design standards compliance, enforces data management procedures, interfaces to a myriad of computer systems, performs automatic auditing of databases and CAD models and coordinates anticipated changes at plants prior to the formal introduction of the product change. Successful compliance with the conditions of satisfaction will result in the release of the work package. Fig. 5d illustrates the queue of work packages pending release by the review board.

Work packages that do not conform to the conditions of satisfaction are returned to the performance phase. This closed loop method that requires negotiation of, and commitment to, the conditions of satisfaction, and customer acceptance of all work has enabled International to reduce the rework in its product changes by 33%. Essentially, only approval by the

Review Board followed by actual review by the program manager, who acts as the process customer, can accept the work package and close the loop.

## 7. Summary and conclusions

They key contribution of this paper is the description of an information technology-based process for building relationships and trust. This understanding is important in the current environment where business is being conducted with trading partners across global distances, often with no previous history of interaction. Therefore, it becomes important these transactions are supported with interaction technology, which enables collaborative commerce at a distance and helps to build trust and relationships over time. The process of building relationships is commonly considered to be a closed loop cycle between a request and its satisfaction. Each successful completion of the cycle contributes to enhanced levels of trust between the partners. Moreover through dialog, the parties develop joint awareness of their own and other’s motivations, investments, and perceived uncertainties in the business deal. This mutual sense making between the parties leads to greater understanding about each other and about their own role in the transaction. If successful, the increased transparency leads to improved relationships and trust.

The closed loop request–acceptance cycle and the joint sense making are based upon conversations between the transacting parties. These conversations consist of networks of commitments embodied in speech acts. However, as the interactions become

![](/api/attachments/WCREVG7N/fulltext/images/71662285d195d174b62f7d99a007268221dafe18d6fa94929c214c2b6646c37c.jpg)  
Fig. 5. (a) Product change management process. (b) Work authorization. (c) The Gauntlet process. (d) Release review board queue

d  
![](/api/attachments/WCREVG7N/fulltext/images/095fe05c664b9229ad00abde11191a30ce6390a323fb0652453490ecb2567776.jpg)

![](/api/attachments/WCREVG7N/fulltext/images/18b4129e183de8f6d103cf7074c3bd2e4041bbc40a1d474d014fc3956d127da0.jpg)  
Fig. 5 (continued).

numerous, dynamic, and complex, keeping track of the commitments by informal manual means becomes difficult and error prone. This leads to unmet commitments and consequent conflict between the transacting parties. On the other hand, meticulous management of the speech acts and commitments through information technology can lead to explicit satisfaction of clearly stated conditions for satisfaction, thereby closing the loop. Computer-based commitment management systems, like ActionWorksR Metro help manage complex networks of commitments. By making the speech acts and their structure explicit, they further help in developing a keener mutual understanding between the transacting parties. Together, the ICT support for the two effects, closed loops and joint sense making, improves the relationship between the two parties and increases the levels of trust.

In conversations for action and in ActionWorksR Metro, we have the beginnings of the principles and a prototype tool for building commitments, relationships, and trust. However, this advantage does not come without price. First, there is always the danger that the computer-based tools may be used as instruments of control, and not as intended, for supporting human awareness of networks of commitments. Thus, a control-oriented supervisor could presumably use the tool as a device for tracking his or her subordinates unmet closed loop performance, and use it to penalize or reward the performers. Such use would be a perversion of the spirit of the tool. Second, by insisting on making the speech acts and their relationships explicit very early in the relationship, it is likely that the parties in the transaction may not have opportunity to discover common ground and may prematurely decide not to pursue the relationship. Some ambiguity in early stages of interaction is useful in achieving buy-in from diverse stakeholders (Yates 1985). Initial vagueness gives each party an opportunity to perceive their own interests reflected in the ambiguous statements thus giving them a rationale to participate in the joint sense-making process.<sup>12</sup> The third price could be considered as both a cost and a blessing. Computers, unlike humans, have a long memory unbiased by recent events. Computers never forget, and canno forgive. On the other hand, Solomon and Flores suggest that trust can exist even in the light of past breakdowns. Reliance on a computer-based commitment management system may perpetuate the memory of broken closed loop cycles far beyond their time.

Ultimately, however, trust and relationships are social processes. The underlying processes of joint sense making and the development of mutual understanding are basically results of human interaction. It is human intentions, motivations, and emotions that drive these processes, not the technology based tool. The most such tools can hope to do is to make the participants in the interaction articulate their commitments, help them be aware of them, and help them keep track of them. Thus, for what purposes a tool is used, and how it is used depend, to a very large extent, on the wisdom of the user. Like any other tool, the use of such computer-based interaction tools needs to be tempered with and understood in the context of human intentions and wisdom. As long as the use of these tools supports human processes, and is not intended as a replacement for them, they are likely to be useful tools for building commitment and trust. If on the other hand, interacting parties rely on them as alternatives for commitment, relationships, and trust, they could be disappointed. Tools, however sophisticated, cannot have wisdom built into them. It is up to their users, humans, to supply that.

## Appendix A. A brief introduction to speech acts

Adapted from Winograd and Flores [[43], p. 58–60].

Speech acts, originally conceptualized as performatives by the philosopher J.L. Austin [2], are a class of utterances that do not refer to the state of the world, but in themselves constitute acts such as promising, threatening, or declaring.

Austin’s student Searle [34,35] formalized the structure of the felicity conditions associated with a variety speech acts [[43], p. 58]. In his later work, he classified all speech acts as embodying five fundamental illocutionary points that are supposed to cover all speech acts or performative utterances. These are:

Assertives: Commit the speaker to something being the case—to the truth of the expressed proposition. For example, the assertive <sup>b</sup>we have sufficient inventory of orangutans at this time at this time<sup>Q</sup> commits the speaker to producing a sufficient inventory of orangutans when challenged.

Directives: Attempt to get the hearer to do something. These include both questions (which direct the hearer to make an assertive utterance) and commands (which attempt the hearer to carry out some linguistic or non-linguistic act). Example, <sup>b</sup>Please deliver 300 orangutans by noon tomorrow.<sup>Q</sup> Commissives: Commit the speaker to some future course of action. Example <sup>b</sup>I will deliver 300 orangutans by noon tomorrow.<sup>Q</sup>

Expressives: Express a psychological state of affairs such as apologizing or praising, for example <sup>b</sup>You did well in delivering the orangutans.<sup>Q</sup>

Declaration: Bring about correspondence between the prepositional content of the speech act and reality; for example <sup>b</sup>Now I pronounce you man and wife.<sup>Q</sup> Or <sup>b</sup>I hereby confer upon you the degree of Doctor of Philosophy<sup>Q</sup> or <sup>b</sup>I hereby appoint you as our designated supplier of orangutans.<sup>Q</sup>

Searle distinguishes between the illocutionary point of an utterance, its illocutionary force, and its prepositional content. Illocutionary point is one of the five categories above. Two speech acts may differ in their illocutionary force while having the same illocutionary point (<sup>b</sup>Will it be possible for you to do it by tomorrow?<sup>Q</sup> vs. <sup>b</sup>Do it by tomorrow or else!!<sup>Q</sup>) The fact that an utterance involves a proposition about some topic, such as the delivery of 300 orangutans at a particular time, is prepositional content.

The essential importance of illocutionary point is the specification of meaning in terms of patterns of commitment entered into by the speaker and the hearer by the virtue of taking part in the conversation. The taxonomy classifies the possibilities for what a speaker can do with an utterance. Different cultures may have different unique ways of expressing different speech acts, but the above space of possibilities is the universal basis of our existence in language.

In making a speech act, the speaker is doing something like making a promise—making a commitment to act in appropriate ways in the future. Of course, an assertive or a declarative has a different kind of satisfaction from a commisive. In an assertive, the speaker is committing to the truth of the statement. If the hearer finds the statement not to be true, the speaker is committed to give an account of why it was true. In the case of a declarative, the speaker is committing to the fact that she/he has the authority to declare the state of affairs being declared. (Only a priest, a naval captain, or a justice of peace may declare a couple to be man and wife).

Finally, Winograd and Flores suggest that organizations and business conduct conversations for action where there is a recurrent pattern of speech acts. This recurrent pattern, shown in Fig. 2 in the text, provides for the basis for computer tools for conducting conversations.

Winograd and Flores [[43] p. 58–60] provide a succinct explanation of Searles’ speech act theory. For a complete discussion also see Searle (1975) <sup>b</sup>A Taxonomy of Speech Acts.<sup>Q</sup>

## Appendix B. Functional requirements specification for a tool for conversations for action

Winograd and Flores [[43], p. 159–161].

Speech Act Origination: The parties to an interaction perform a speech act by selecting an illocutionary point from a small set of alternatives (the set of speech acts and their illocutionary points mentioned above); indicating its prepositional content in the text; and explicitly entering temporal relationships to other (past and anticipated) speech acts. By making explicit the declaration of the illocutionary point and force of the speech act, and relating it in time and sequence to other speech acts ambiguities, confusion, and breakdowns due to differences in meaning ascribed by the speaker and the listening parties can be minimized and avoided.

Monitoring Completion: The system, by keeping track of the network of speech acts generated in the interaction, and by exploiting the structure in Fig. 1, can keep track of where things stand and when will they change. This can be used to provide a clear reminder of outstanding commitments, ascertain if the conditions for completion are satisfied, and provide a clear picture of what is happening at any point in time and where potential problems and breakdowns lie ahead.

Keeping Temporal Relations: The system can keep track of time relationships within the network and use them to help anticipate and cope with breakdowns. Time is not an incidental condition, but a critical aspect of every speech act. A promise is really not a promise unless there is a mutually understood (explicitly or implicitly) time for satisfaction. A request is not fully formed unless there is a time specified for reply and completion. As speech acts are made using the system, the user is coached to explicitly represent the temporal relations that are central to the network of commitment. These relations can be used to monitor what needs to be done and warn of potential delays and breakdowns.

Examination of the Network: Any party to the interaction can display part of the conversation network, showing the conversations and their status, the individual commitments and requests, and their relationships to others. It is possible, for example, to find out what requests were generated in anticipation of breakdown in satisfying a particular commitment, or what requests are still awaiting a response from a particular individual.

In addition Winograd and Flores include two additional functional requirements, those of Automated Application of Recurrence by the computer and Recurrence of the Propositional Content in routine conversations. We omit their descriptions here as they are not relevant to our requirements for initiating and monitoring conversations for action needed for requests, negotiations, commitment, performance, and acceptance, that is, conversations for trust building.

## References

[1] L.M. Applegate, F.W. Mc Farlan, J.L. Mc Kenny, Corporate Information Systems Management: The Challenges of Managing in an Information Age, 5th edition, Irwin McGraw-Hill, 1999.

[2] J.L. Austin, How to Do Things with Words, Harvard University Press, Cambridge, 1962.

[3] J.L. Bradach, R.G. Eccles, Prices, authority and trust: from ideal type to plural forms, Annual Review of Sociology 15 (1) (1989) 97–118.

[4] P. Bromiley, L. Cummings, Transaction cost in organizations with trust, Working Paper 28, Strategic Management Research Center, University of Minnesota, Minneapolis, 1992.

[5] S. Brown, International’s better way to build trucks, Fortune (February 19, 2001).

[6] C. Ciborra, From Control to Drift: The Dynamics of Corporate Information Infrastructures, Oxford University Press, 2001.

[7] E.K. Clemons, S.P. Reddi, M.C. Row, The impact of information technology on the organization of economic activity: the move to the middle hypothesis, Journal of Management Information Systems 10 (2) (1993) 9– 35.

[8] J.R. Commons, The Economics of Collective Action, Madison University of Wisconsin Press, 1950.

[9] R.L. Daft, Organization Theory and Design, 8th edition, Thompson South-Western, 2004.

[10] S. Deakin, F. Wilkinson, Contract law and the economics of interorganizational trust, in: C. Lane, R. Bachmann

(Eds.), Trust Within and Between Organizations: Conceptual Issues and Empirical Applications, Oxford University Press, 1998.

[11] P. Denning, Workflow on the web, in: L. Fischer (Ed.), New Tools for New Times: Electric Commerce, Future Strategies Inc., 1996.

[12] P. Denning, R. Medina-Mora, Completing the loops, Interfaces 25 (3) (1995) 42–57.

[13] F.R. Dwyer, S.P. Shurr, P.H., S. Oh, Developing buyer– seller relationships, Journal of Marketing (51) (1987 (April)) 11 – 27.

[14] S. Dyer, Chu, The determinants of trust in supplier–automaker relationships in the U.S., Japan, and Korea, Journal of International Business Studies 31 (2) (2000) 259– 289.

[15] J. Gabarro, The Dynamics of Taking Charge, Harvard Business Review Press, 1987.

[16] J. Habermas, What is universal pragmatics, in: Thomas McCarthy (Translator), Communication and the Evolution of Society (Beacon Press, Boston, 1979, pp. 1–68).

[17] C. Handy, Trust and the virtual organization, Harvard Business Review 73 (3) (1995) 40– 50.

[18] C. Hardy, P. Nelson, T. Lawrence, Distinguishing trust and power in interorganizational relations: forms and facades of trust, in: C. Lane, R. Bachmann (Eds.), Trust within and Between Organizations: Conceptual Issues and Empirical Applications, Oxford University Press, 1998.

[19] P. Hart, C. Saunders, Power and trust: critical factors in adoption and use of electronic data exchange, Organization Science 8 (1) (1997) 23– 42.

[20] S.L. Jarvenpaa, D.E. Leidner, Communication and trust in global virtual teams, Journal of Computer-Mediated Communication 3 (4) (1998 (June).

[21] P.G. Keen, Ensuring E-trust, Computerworld (2000 (March 13).

[22] K. Kumar, P.C. van Fenema, A new era for project management: the challenge of globally distributed projects, Proceedings of the International Research Network on Organizing by Projects (IRNOP), Calgary, Alberta, 1998.

[23] K. Kumar, H.G. van Dissel, P. Bielli, The merchant of Prato— revisited: toward a third rationality of information systems, MIS Quarterly 22 (2) (1998 (June)) 100– 226.

[24] C. Lane, Introduction: theories and issues in the study of trust, in: C. Lane, R. Bachmann (Eds.), Trust within and Between Organizations: Conceptual Issues and Empirical Applications, Oxford University Press, 1998.

[25] R.J. Lewicki, B. Bunker, Developing and maintaining truest in work relationships, in: R.M. Kramer, T.R. Tyler (Eds.), Trust in Organizations: Frontiers of Theory and Research, Sage Publications, Thousand Oaks, CA, 1996, pp. 114– 139.

[26] N. Luhman, Trust and Power, Chichester, John Wiley, 1979.

[27] T.W. Malone, J. Yates, R.I. Benjamin, Electronic markets and electronic hierarchies, Communications of the ACM 30 (6) (1987) 484– 497.

[28] R. Mayer, J. Davis, D. Schoorman, An integrative model of organizational trust, Academy of Management Review 20 (3) (1995) 709– 734.

[29] J. Olson, G. Olson, <sup>b</sup>i2i trust in e-commerce, Communications of the ACM 43 (12) (2000) 41– 44.

[30] J. Pfeffer, G.R. Salancik, The External Control of Organiza tions: A Resource Dependency Perspective, Harper and Row Publishers, 1978.

[31] M. Porter, Competitive Strategy: Techniques for Analyzing Industries and Competitors, The Free Press, NY, 1980.

[32] P.S. Ring, A.H. van de Ven, Structuring cooperative relationships between organizations, Strategic Management Journal (13) (1992) 483– 498.

[33] P.S. Ring, A.H. van de Ven, Development processes of coop erative interorganizational relationships, Academy of Management Review 19 (1) (1994) 90 – 118.

[34] J.R. Searle, Speech Acts, Cambridge University Press, 1969.

[35] J.R. Searle, A taxonomy of illocutionary acts, in: K. Gunderson (Ed.), Language, Mind, and Knowledge, University of Minnesota, 1975, pp. 344–369.

[36] H. Simon, The Sciences of the Artificial, MIT Press, 1996.

[37] R.C. Solomon, F. Flores, Building Trust: In Business, Politics, Relationships, and Life, Oxford University Press, 2001.

[38] J. Sydow, Understanding the constitution of interorganizational trust, in: C. Lane, R. Bachmann (Eds.), Trust within and Between Organizations: Conceptual Issues and Empirica Applications, Oxford University Press, 2000.

[39] J.H. Turner, Towards a sociological theory of motivation, American Sociological Review (15) (1987) 15– 27.

[40] K. Weick, Sensemaking in Organizations, Sage Publications, Calif, 1995.

[41] B. Welty, I. Becerra-Fernandez, Managing trust and commit ment in collaborative supply chain relationships, Communica tions of the ACM 44 (6) (2001 (June)) 67– 73.

[42] E. Williamson, Markets and Hierarchies, Analysis and Anti trust Implications, The Free Press, New York, 1975.

[43] T. Winograd, F. Flores, Understanding Computation and Cog nition: A New Foundation for Design, Addison-Wesley, 1986.

[44] D. Yates, The Politics of Management, Jossey-Bass Management Series, 1985.

[45] L.G. Zucker, Production of trust: institutional sources of economic structure, Research in Organizational Behavior (8) (1986) 53–111.

![](/api/attachments/WCREVG7N/fulltext/images/eec60f8eca33f3940fac72e7d2d581f86aafcd89fbd9dbaaa95dd9eb9c5d1ffd.jpg)

Kuldeep Kumar is Ryder Eminent Scholar and Professor of Information Systems at the Alvah H. Chapman Graduate School of Business, Florida International University. He is also a Professor of Information Systems Research at the Faculty of Business, Rotterdam School of Management, Erasmus University. His current research interests include management of global R&D, management of global software development projects, trust in inter-organizational

relationships, inter-organizational knowledge transfer and integration, communities of practice and global knowledge networks, dynamic supply chains and networks, and global strategic outsourcing. E-mail address: kumark@fiu.edu

![](/api/attachments/WCREVG7N/fulltext/images/4aaeac1a083e691d7adab95a02ca1709e7e48ba79378c122d8dc4c49ad8eaa7d.jpg)

Irma Becerra-Fernandez is an Associate Professor at Florida International University. Her research focuses on knowledge management (KM), KM systems, and enterprise systems. She has studied and advised organizations, in particular NASA, about KM practices. She founded the KM Lab (http:www.kmlab.fiu.edu) to develop innovative KM systems. She has published extensively in leading journals including JMIS, Decision Sciences,

CACM, and EJOR, among others. Dr. Becerra-Fernandez is an author of the book Knowledge Management: Challenges, Solutions, and Technologies (Prentice Hall, 2004). She earned her PhD, Masters, and Bachelors in Electrical Engineering. E-mail address: becferi@fiu.edu.
