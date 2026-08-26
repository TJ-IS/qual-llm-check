---
otero_id: 26419
otero_key: "EED6UYFX"
title: "Research Commentary: Introducing a Third Dimension in Information Systems Design—The Case for Incentive Alignment"
authors: "Sulin Ba; Jan Stallaert; Andrew B. Whinston"
year: "2001"
journal: "Information Systems Research"
doi: "10.1287/isre.12.3.225.9712"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/EED6UYFX/fulltext/images/77b4b3662056b16aa6d46181f8d7b29db3afff111d62b72c698051d0f1745317.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Commentary: Introducing a Third Dimension in Information Systems Design—The Case for Incentive Alignment

Sulin Ba, Jan Stallaert, Andrew B. Whinston,

To cite this article:

Sulin Ba, Jan Stallaert, Andrew B. Whinston, (2001) Research Commentary: Introducing a Third Dimension in Information Systems Design—The Case for Incentive Alignment. Information Systems Research 12(3):225-239. http://dx.doi.org/10.1287/ isre.12.3.225.9712

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2001 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/EED6UYFX/fulltext/images/74ab68afb50c33968c4a821690430b0d1024c61556fa96132c7670e041804c17.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Commentary: Introducing a Third Dimension in Information Systems Design—The Case for Incentive Alignment

Sulin Ba • Jan Stallaert • Andrew B. Whinston

Electronic Economy Research Lab, Department of Information and Operations Management, Marshall School of Business, University of Southern California, Los Angeles, California 90089

Electronic Economy Research Lab, Department of Information and Operations Management, Marshall School of Business, University of Southern California, Los Angeles, California 90089

Center for Research in Electronic Commerce, McCombs School of Business,

University of Texas at Austin, Austin, Texas 78712

sulin@usc.edu • stallaer@usc.edu • abw@uts.cc.utexas.edu

rior research has generated considerable knowledge on information systems design from software engineering and user-acceptance perspectives. As organizational processes are increasingly embedded within information systems, one of the key considerations of many business processes—organizational incentives—should become an important dimension of any information systems design and evaluation, which we categorize as the third dimension: incentive alignment. Incentive issues have become important in many IS areas, including distributed decision support systems (DSS), knowledge management, and e-business supply chain coordination. In this paper we outline why incentives are important in each of these areas and specify requirements for designing incentive-aligned information systems. We identify and define important unresolved problems along the incentive-alignment dimension of information systems and present a research agenda to address them.

(Information Systems Design; Incentive Alignment; Distributed Decision Support Systems; Knowledge Management; Supply Chain Coordination)

## 1. Introduction

Organizations in the new digital economy face unprecedented challenges with the rapidity of change in both the competitive environment and the technology. To operate effectively, real-time decision making requires inputs from multiple participants with differing knowledge, skills, and objectives. To better leverage an organization’s intellectual asset for value generation, knowledge management has become the center of many companies’ core competency. And increasingly, the shift towards e-business demands that organizations restructure their business models and processes so that information and products can move smoothly across the value chain. Critical to the success of all these business activities and initiatives are information systems designed to meet the challenges of today’s business.

Given the increasingly important role of information systems (IS) in organizations, IS-design issues have been the focus of a substantial amount of IS literature. Previous research dealt with at least two dimensions in the design and implementation of information systems to support organizational processes. The software engineering dimension addresses the challenges of creating a cost-effective implementation of a system that is reliable, is easy to modify when users need change, and can be upgraded to new hardware platforms. The user-acceptance dimension is based on the evaluation by system users in terms of its relevance, usefulness, ease of use, satisfaction with the outcomes, the ability to exchange information with other participants, etc.

However, a system that takes into account only principles from the above two dimensions will not necessarily lead to a successful organizational outcome. A personal anecdote illustrates this phenomenon. As part of its knowledge-management initiative, a big consulting firm created a new knowledge repository where consultants could record their knowledge gained from past experience, so that the knowledge could be used by their associates facing similar situations. The organizational objective was to leverage the consultants’ collective knowledge for value generation. In marketing this knowledge repository, a consultant from this company boasted that by hiring his firm, a client was hiring not just one consultant, but rather a network consisting of thousands of consultants who had made their knowledge available in this knowledge repository. When asked whether he had contributed his knowledge to the system, the consultant answered that he would have liked to, but that he had not yet done so because he had been too busy. So, while the knowledge-repository software may have qualified as a well-built system from a software engineering perspective, and the users may have perceived the system to be useful, the system did not lead to a satisfactory organizational outcome because there was no incentive for consultants to make the effort to input their individual knowledge into the system’s knowledge repository.

We believe that as organizational processes are increasingly embedded in information systems, one of the key considerations of many business processes— organizational incentives—should become the third dimension of any information systems design and evaluation. We call this third dimension incentive alignment. It addresses the high-level design issues that recognize the interests and incentives of the users participating in the process (e.g., users’ own objectives may differ from the corporate objectives), the differences in the distribution of information across the users, and the desirability of the eventual collective choice from the organization’s standpoint. There are two fundamental, interrelated issues in this dimension. First, given the organizational process embedded in the information system, are organizational incentives in place for users to use the system as intended? That is, will the users make the effort to produce correct information? Will they input the true and accurate information they have? Or can they gain from distorting information? Second, will the use of the information system for a business process yield outcomes that contribute to reaching the organization’s objectives? Is it robust against information misrepresentation from its users? Systems can be fault tolerant and easy to use but may fail to contribute to the organizational goal. A design methodology is needed that ensures that the new system and the embedded organizational process will be aligned with the organizational goals. Consequently, an information system should be evaluated along this dimension as well.

Incentive issues have become important in many IS areas, among which are distributed decision support systems (DSS), knowledge management, and e-business supply chain coordination. In this paper we outline why incentives are important in each of the three areas and specify requirements for the design of incentivealigned information systems. We argue that the collection of processes that are eventually implemented need to satisfy the requirements of how it affects the alignment of user incentives to organizational objectives.

The rest of the paper is organized as follows. Section 2 provides a background on how the three dimensions of information systems design relate to each other, and how the third dimension has been treated in the literature. Sections 3, 4, and 5 focus on the specific incentive requirements in distributed DSS, knowledge management, and supply chain coordination, respectively. Section 6 provides a research agenda with research questions that need to be addressed in designing incentive-aligned information systems. The last section concludes the paper.

## 2. Background

The research on IS design and evaluation is voluminous. For the purpose of illustrating our position, we classify the attributes that are currently used to evaluate information systems into two dimensions—although such classification is by nature an oversimplification.

The first dimension used to evaluate and design information systems has its roots in the 1960’s (Naur and Randell 1969, Buxton and Randell 1970), and the literature dealing with this dimension is huge (for example, Souza 1990, Banker and Kauffman 1991, Henson and Hughes 1991, Swanson et al. 1991, Subramanian and Zarnich 1996, Dekleva and Drehmer 1997). We call it the “software engineering” dimension, because most issues considered along this dimension are concerned with the features of the software product itself (Pressman 2000). The quality of a product is measured with respect to (1) whether the software functions correctly under every possible contingency, (2) whether the system can be transported to other platforms, (3) whether the program code has been well documented in case the system needs to be updated in the future, (4) whether the standards of modularity and architectural design have been adhered to, and (5) whether the whole development effort has been carried out while controlling the overall cost. In terms of analyzing the system’s ergonomic design, user involvement was considered as well, but the primary focus of this first dimension was the design of the software itself.

By contrast, the attributes of the second dimension take the system user as the focal point. The Technology Acceptance Model (TAM) (Davis et al. 1989) and the models of cognitive fit (Vessey and Galletta 1991) and task/technology fit (Benbasat et al. 1986, Goodhue 1995) are examples of attributes by which systems are evaluated in the second dimension. The user is central in these theories, while the models investigate and analyze what system characteristics explain the success or failure of a new technology adoption from the user perspective.

Attributes that we classify as the third-dimension deal with the effect of incentives and rewards on the system’s outcome. For example, in the TAM model, frequency of use would be a measure of technology adoption. In the third dimension, frequency of use would be complemented by how its use contributes to the overall organizational goal: If the system is not well designed, frequency of use might well lead to inferior outcomes at the organizational level, even if the system is perceived as being useful by an individual user. More specifically, third-dimension attributes concern incentive alignment, i.e., when the system has embedded features that induce its users to employ the system in a manner consistent with the design objective, and hence the organization’s overall goals such as profitability and value generation. In game-theoretic terms we call a system incentive aligned when a user’s dominant strategy and the preferred user behavior correspond from an organizational perspective. That is, the agent can still freely determine his own behavior and use of the system, but the most rational action, i.e., the action that is in his best interest, coincides with the action that benefits the organization most.

Some previous research has discussed issues related to incentive alignment. For example, DeSanctis and Poole (1994) use the word spirit to refer to the “general intent with regard to values and goals underlying a given set of structural features” of an advanced system. The user’s incentive for using the system in a way consistent with the design objective is called the “faithful” use of the system’s features. In the knowledgemanagement literature, Davenport and Prusak (1998) discuss a “knowledge market” idea whereby users— especially the knowledge contributors—of a knowledgemanagement system have to be provided with incentives for the system to be a success, although a detailed mechanism and procedure for buying and selling knowledge is lacking in their rather conceptual description. In the enterprise resource planning (ERP) area, some ERP systems were found to fail when information required to be entered by members of one department had to be used by those in another, when those who entered the data were not responsible for the outcome that their inputs had on other parts of the organization (Deckmyn 2000). Recently, the effect of incentives on the decision strategy has been investigated for the case of a single decision-maker’s interaction with a decision support system (Todd and Benbasat 1999). There is no discussion on how one user’s behavior impacts another’s, or how one user could “game” the system by (mis)representing information in a certain way.

In short, while the attributes that are part of the third dimension have been previously alluded to in IS literature, the treatment has been sporadic. We, therefore, call for an exploratory analysis of such attributes which describes those attributes explicitly, and develops a design methodology that expressly evaluates a system based on those attributes. An overview of the attributes considered in the three dimensions is given in Table 1.

The more advanced the information technology is, the more pronounced the importance of the features in the third dimension becomes. For simple operational systems, the individual user’s incentives play less of a role because the role is reduced to a mere clerical task. For example, transaction-processing systems were one of the earliest computerized business systems that automated highly repetitive tasks that tracked business transactions (Turban et al. 2001). The issue of incentive alignment is almost nonexistent in these systems: User involvement is virtually limited to accurate data input that can easily be verified by a sample audit. As the information technology becomes more advanced, such verification controls are no longer in place; e.g., for annual budgeting processes it is common to ask for inputs such as demand forecast for products and product lines, guesstimates of commodity price evolutions, or extrapolation of cash flows. Such information is often not verifiable, but may be distorted by self-interested information contributors who want to influence the decision process.

An example may clarify this. A distributed decision support system to help decide on oil drilling projects was developed and implemented in dozens of oil exploration companies (Hightower et al. 1997). The system required inputs from several exploration managers and engineers about probability distributions of oil and gas reserves, as well as drilling and development costs of the oil rigs for the projects they propose. The system then selected a portfolio of promising drilling projects so that the risk exposure to the entire firm was minimized, honoring the budget constraint for exploration capital. Because the likelihood of getting a drilling project funded increases when the reserve “estimates” are higher, and the drilling and development costs were lower, the system would typically select projects with an expected return of investment of over 35%. Often times, after implementing the decision it was hard to obtain return on investment figures about half that high. Exploration managers always tried to explain this discrepancy as the result of random realization of nature, meaning that “less than expected” oil and gas reserves were discovered. Although this explanation is valid for one individual situation, on an aggregate level (it was observed for every company, in other words more than a hundred projects were sampled), it is probabilistically extremely unlikely that the randomness is to blame for every discrepancy in this sample. A more likely explanation is that exploration managers were inflating their estimates so as to get their project funded; managers who submitted more reliable (and hence lower) estimates would have been penalized by not getting any funding (Hightower 1998).

More and more, such advanced information systems are developed where inputs are required from several users, and the combined outcome will be used as the basis to make decisions that often have enterprisewide consequences. Please note that we do not necessarily assume that users are malevolent, because users may not be aware of their own biases. Incentive-alignment questions arise in situations where the contributions of multiple users are required, where the information provided is not easily verifiable, and where their personal goals may affect their information representation.

Table 1 The Three Dimensions for Information Systems Design and Their Attributes

<table><tr><td>First DimensionSoftware Engineering</td><td>Second DimensionTechnology Acceptance</td><td>Third DimensionIncentive Alignment</td></tr><tr><td>Error-free softwareDocumentationPortabilityModularity &amp; ArchitectureDevelopment costMaintenance costSpeedRobustness</td><td>User friendlinessUser acceptancePerceived ease-of-usePerceived usefulnessUser satisfactionCognitive fitTask/technology fit</td><td>Incentives influencing user behavior and the user&#x27;s interaction with the systemDeterrence of use for personal gainUse consistent with organizational goalRobustness against information misrepresentation</td></tr></table>

Principal-agent problems in the economics literature (Dasgupta et al. 1979, Holmstrom 1982, Myerson 1979) bear some resemblance to the issues of incentive alignment in information systems. However, whereas the literature on principal-agent problems primarily deals with monitoring agent’s efforts and avoiding information hiding or misrepresentation from the agents, it assumes that the information is available to the agent in the first place. Principal-agent theories study the design of an “optimal contract” that links user’s behavior and efforts to rewards. In an information system we are more concerned with giving users the correct incentives to first create or compile information (e.g., figures for demand estimates of a certain product line or region), which entails a cost for the user as an expense of time and effort. Moreover, the user’s information will be used as inputs (e.g., demand forecast of a product) to a decision-making procedure whose outcome will then have repercussions on the user (e.g., allocation of a certain advertising budget to promote the sales of that product). The relationship between inputs submitted and the future impact on the user therefore cannot be explicitly determined and, in many cases, also depends on the inputs of other users.

These issues are especially pertinent in distributed decision support systems (DSS), knowledge management, and e-business supply chain coordination, which are the focus of the rest of this paper. We will identify and discuss the incentive-alignment issues in each of the three areas and propose research strategies to address them.

## 3. Distributed Decision Support Systems

Group support systems (GSS) are the most widely studied tool for collective decision making, and are the first technology to come to mind when implementing distributed DSS in decentralized organizations. As a primary information-technology tool in support of organizational decision making, GSS have been studied extensively by the IS community (Benbasat and Lim 1993) from social, behavioral, and technological perspectives.

## 3.1. Current State

The literature has investigated issues in the first and second dimensions, such as end-user satisfaction, media choices, decision satisfaction, and usefulness of various technology features (Burk and Aytes 1998, Davey and Olson 1998, Dennis and Valacich 1994, Ellis et al. 1990, Gallupe et al. 1988, McGrath and Arrow 1996, Todd and Benbasat 1999, Fjermestad and Hiltz 2000, to cite a few). The effectiveness of these systems is mostly evaluated by measures such as the number of critical comments made and ideas generated; measures which do not necessarily reflect the quality of the decisions.

Among the many features a GSS can implement, the voting mechanism demonstrates most clearly the ramifications of user incentives. A voting mechanism allows users to vote on a set of alternatives. The votes originate locally, based on the decentralized knowledge available to the user, and the vote-tallying process can be seen as the decision coordination function of the IS. Because the voters will be impacted by the final outcome, there is an incentive to cast a vote so as to influence the final choice for one’s self-interest.

Different voting mechanisms exist, but all of them are, to a certain degree, prone to the phenomenon of voting according to one’s self-interest, which was first discovered by Condorcet (1785), and whose implications for GSS design have been described by Gavish and Gerdes (1997). For example, an individual who thinks his or her choice has little chance of being elected may instead cast a vote for a less-preferred alternative. Where others act in a similar fashion, the outcome of the system may display paradoxical behavior, so that alternatives that would have been preferred by a majority of the voters may not be the final outcome of the process. It is an open question in the voting literature whether voting mechanisms exist that are not prone to such behavior: Every system known at present is susceptible to strategic misrepresentation, where voters cast votes for less-preferred alternatives.

Another problem with the current implementation of voting mechanisms in GSS is how one distills a final outcome that is agreeable to most of the participants. If consensus<sup>1</sup> among the group members is the final goal, empirical evidence has shown that individual preference orderings do not necessarily converge to one group-preference ordering after many iterations of interaction and evaluation among the participants (Chen et al. 1994, Briggs et al. 1998). Theoretically, it has been established that a social-preference ordering, given the participants’ individual preference rankings, does not always exist (Arrow 1963).

## 3.2. Research Challenges

To summarize the current state of distributed DSS research, we believe that while the above research has laid the groundwork for IT-supported coordination systems, there is still a major gap in the literature: There is no objective measure of the quality of decisions made using GSS (Fjermestad and Hiltz 1998). Very rarely would the system be measured based on the potential overall (economic) outcomes of the decisions on the organizational level, and the issues of incentive alignment are largely absent. Voting mechanisms have some initial appeal for implementing decentralized decision support systems, but present voting systems lack the capability of incentive alignment. Therefore, more research is needed to develop systems that score better in this dimension: The computational power provided by DSSs has gone unused in present systems, so it remains a promising direction to design new mechanisms that, at the expense of computation and increased complexity, obey the requirements of incentive alignment.

One of the main challenges in accomplishing this task in a distributed organizational environment is when the decisions are made based on local information not available to the headquarters. How does one collect accurate and trustworthy information dispersed throughout the organization to make sound decisions that impact several divisions? If information is processed locally, how do we ensure that the information that is transmitted to make organizationwide decisions isn’t distorted? This distortion can be intentional in cases where the local divisions have an interest in impacting decisions a certain way; or it can be unintentional, when the local divisions have a certain bias that they are not aware of, i.e., when they may be naturally inclined to overvalue the contribution of their division to the organizational performance. Decentralized decision authority supported by distributed information systems is the rule rather than the exception in today’s organizations. Combining local information while making sure that it forms a sound basis for making global decisions brings to light the importance of incentive alignment. Information systems that provide support for strategic companywide decisions should have mechanisms to ensure incentive alignment.

## 4. Knowledge Management

The management of intellectual capital has become a commonly cited source of competitive advantage. Not surprisingly, a wide range of companies have launched IT-based knowledge-management initiatives to help employees share their best ideas and management practices. IS/IT has made it possible to codify, store, and share knowledge more easily than ever before.

## 4.1. Current State

Literature on knowledge management has identified some key steps in any knowledge-management initiative, among which is knowledge sharing (Davenport and Prusak 1998, Hansen et al. 1999, Garvin 1997). How to achieve effective knowledge sharing within organizations and in society has been a focus of research in the organizational literature as well as in economics. In fact, a decade ago, IS researchers had already discovered the difficulties of knowledge acquisition when implementing expert or knowledge-based systems (Byrd 1992). Knowledge engineers faced the problem of how to get an expert to state and explicitly express his knowledge. In today’s knowledge-management systems, knowledge acquisition and sharing, instead of being done by knowledge engineers, rely on knowledge possessors’ effort. The effect of incentives on the knowledge possessor’s behavior regarding knowledge sharing is therefore more pronounced.

Organizational concerns are about achieving sharing through social exchange so that effective use is made of accumulated knowledge. We briefly review the knowledge-sharing literature and analyze the knowledge-sharing phenomenon from an incentive point of view.

There are various reasons why people or organizations would share or exchange knowledge with others. Some factors are tangible. For example, when a company buys knowledge from outside, the company frequently pays with cash. But within an organization, the terms of exchange are often intangible and the motivations vary. The motivation could simply be one of goodwill—one theory put forth looks at the phenomenon from a social-exchange perspective in which people share knowledge because of their altruistic preferences (Constant et al. 1994, Palfrey and Prisbrey 1997). This theory posits that individuals wish for good outcomes not only for themselves, but also for other employees or for the organization more generally (O’Reilly and Chatman 1986), that they share knowledge because they feel a commitment to the organization, and that employees believe that knowledge sharing could improve organizational efficiency, learning, innovation, and flexibility. In short, individuals help others whether or not they get anything in return. The development of the Linux operating system has come about by programmers who contributed their code to the Linux project without directly expecting anything in return (Tapscott et al. 1999).

In slight contrast, other authors believe that another primary motivation for knowledge sharing is from the reputation the sharing behavior generates (Davenport and Prusak 1998). A knowledge possessor wants to show off, and wants others to know that he is a knowledgeable person with valuable expertise. Although reputation is itself an intangible concept, one’s reputation can result in tangible benefits such as job security and promotion.

Still, obstacles to knowledge sharing abound. It has been recognized that knowledge altruism may be constrained by increasing demands on the time and energy of employees, or that it may not be part of many companies’ culture (Davenport and Prusak 1998), therefore it does not cultivate knowledge sharing in a systematic way. Orlikowski (2000) observed a situation in which consultants avoided their knowledgecontribution effort because many consultants did not see using the knowledge-sharing technology “as an activity that could be billed to clients, they were unwilling to spend time learning or using it, as this would have required them to incur ‘nonchargeable hours’ or to give up some of their personal time.” In addition, employees normally regard tailored knowledge as power, which they naturally may not readily share because they feel that giving up valuable information would threaten their status within the organization. Therefore, although the information technology was deployed very rapidly, anticipated benefits were realized much more slowly. Key to the reluctance to use the knowledge-management technology for knowledge sharing was a perceived incompatibility between the collaborative nature of the technology and the individualistic and competitive nature of the organization (Orlikowski 2000, Orlikowski and Hoffman 1997). Alliances where public goods are voluntarily created by members who have a shared goal are based on gift economies (Tapscott et al. 1999, Kollock 1999), which assume that members are noncompeting, have a common goal, and in which the resources being exchanged are characterized by abundance, rather than scarcity. Hence, it is extremely unlikely that in organizations with competing members, gift economies would be the driving force for the exchange of information.

In summary, knowledge sharing is both constrained and difficult without proper and necessary incentives for doing so. Economic and monetary incentives should be explored in a knowledge-sharing context where, for example, people may be willing to give away certain knowledge when they perceive value in return for having done so. Without providing incentives for individuals to share knowledge, organizations face another knowledge management problem: that of what knowledge to create in the first place. How do we know what we already know? How do we identify the desired knowledge proactively, before it is in its finished form? Oftentimes, because of individuals unwillingness to share, organizations may end up reinventing the wheel: creating knowledge that already exists in the organization but remains unshared.

## 4.2. Research Challenges

One of the solutions proposed to encourage knowledge sharing is the knowledge-market idea. In their 1998 book, Davenport and Prusak articulate why the market idea is suitable for organizational knowledge sharing and list the benefits of knowledge markets. In their vision, a knowledge market is where buyers and sellers of knowledge negotiate a mutually satisfactory price for the knowledge exchanged. The perceived gain from the market exchange of knowledge serves as an incentive for the knowledge possessor to share knowledge. Three factors are at work as the gain: reciprocity, repute, and altruism. Yet these factors do not lend themselves to price theory; the challenge is, therefore, to quantify these factors into monetary value so that a benefit can be assigned to and by the whole organization.

However, were some monetary value to be assigned to the exchange of knowledge, then the knowledge market would essentially be turned into a privategoods market. A complicating factor arises in that knowledge has the characteristics of a public good, i.e., it is nondepletable (Arrow 1962, Mas-Colell 1995, Radner 1986, Adler 2001). Once knowledge is created, it can be freely disseminated to or shared by everybody in the organization. Consumption of such a nondepletable good by one employee does not preclude its consumption by anyone else. Economic theory teaches us that in this case the whole organization would then suffer because treating a public good as a private good leads to under-provision of knowledge (Samuelson 1954)—an outcome which would defeat the very purpose of knowledge management.

From the organization’s standpoint, withholding knowledge from certain individuals will rarely be optimal. Facilitating the accessibility of knowledge to everyone in an organization requires treating knowledge as a public good within the organization. The challenge then arises: How does this comport to market theory?

The difficulty of taking knowledge as a public good to a market situation is the inherent free-rider problem, i.e., the provision of public goods generates an externality—if one individual provides a unit of a public good, all individuals benefit. That is, once the knowledge possessor is compensated for sharing the knowledge, then everyone else in the organization can gain access to it, which leads to a situation where potential knowledge buyers will understate their true valuation of knowledge, hoping that they can use it without contributing much to its sharing. The potential for undercontribution to a public good is particularly clear when contributions are voluntary (viewers of PBS will immediately recognize the problem). In this situation, a traditional information system to facilitate knowledge management—particularly knowledge sharing—will most likely fail to elicit employees’ true opinion of the importance of each piece of knowledge and how to maximize the total value of the knowledge in the organization.

To deal with the free-rider problem associated with nonexcludable goods, there has to be an incentivealigned mechanism that prompts people to reveal their true valuation of knowledge. It was commonly believed, prior to the seminal papers of Clarke (1971) and Groves (1973), that in economies with public goods it would be impossible to devise a decentralized process that would allocate resources efficiently because each participant would have an incentive to “free ride” on others’ provision of those goods to reduce their own share of providing them. There is, therefore, a systematic bias to underreport valuations if the mechanism requires people to contribute according to their reported valuation. Clarke and Groves recognized that the difficulty in providing a valuation for a public good is that there is no incentive to submit bids equal to their marginal valuation. Accordingly, they proposed an incentive-aligned economic method in which truth telling becomes a dominant strategy for the market participants.

The results of the Groves-Clarke mechanism shed light on how an internal market for knowledge management might be created (Ba et al. 2000). The key research questions are: What are the necessary market conditions? To what extent does the introduction of the knowledge market attract buyers and sellers? What is the price system for knowledge? How accurate is the value of knowledge, as reflected in the market price, compared to its actual value realized ex post? How should such a knowledge market be implemented with IT? To what extent does the social aspect of knowledge sharing interact with the economic-market approach? How should the interaction be reflected in the design of the system? Does more knowledge get shared in such a market-oriented IT system as opposed to a traditional implementation of a knowledge management system?

The incentive issue has gained attention lately. Many experts believe that people who are rewarded for sharing do more of it, and that incentive systems in a knowledge-management effort are essential to creating a culture in which knowledge sharing is the norm (Szulanski 1996). It is our belief that simply building knowledge management systems from the software engineering and user acceptance perspectives is not enough; incentive issues need to be built into the system so that its effective use and a desirable outcome are guaranteed. Economic findings need to be factored into the design of knowledge management technologies.

## 5. E-Business Supply Chain Coordination

A global supply chain organization is made up of a worldwide network of suppliers, manufacturing facilities, warehouses, distribution centers, and transportation systems, which transform raw materials into final products and delivers them to millions of consumers. The challenge of coordinating global supply chains within global organizations has become increasingly important in recent years. Information technology (IT), especially the recent explosive growth of the Internet and electronic commerce, is having a profound impact on how supply chain coordination is done. In this paper, we focus on the information aspect of supply chain coordination.

## 5.1. Current State

Supply chain management deals with networks of suppliers and channels of distribution. E-businesses are now providing value through the power of information networks while redefining, and sometimes even eliminating, activities in the physical network. Supplyand-demand auctions, collaborative product design, and cross-enterprise workflow processes are examples of how the information network—and e-business—is reshaping the physical network (Cross 2000).

Traditionally, the distortion of information in the global supply chain has been a major obstacle in the process. Information with regard to supply and demand of products and resources is not readily available to the concerned agents, resulting in mismatches between demand and supply and inefficient usage of resources. Many companies have experienced failed attempts to reduce information distortion in supply chains.

Changes in supply chain operations usually involve applications of information technology. Information technology, particularly the Internet, is supposed to significantly reduce the information-distortion problem. The Internet enables fast and cheap processing and storage of information, as well as the exchange of information among multiple agents. Many IT-based supply chain improvement efforts, however, have failed to achieve anticipated benefits because they have failed to recognize how incentives play a role in the business partnerships across the supply chain—sometimes players resist supply chain improvement changes or withhold information because they recognize that they might actually suffer from operating changes that will benefit the supply chain overall (Narayanan and Raman 2000).

A significant problem for global organizations requiring supply chain coordination among multiple units is that the goals of individual divisions are not always aligned with the overall goal of the organization. Too often the myopic behavior of individual agents may benefit the agents, but hurt the overall organization. If, for example, agents are evaluated based on individual performance, and there is no mechanism within the organization for the exchange of corporate resources, agents will likely want to possess or control resources in direct proportion to assurances of individual gains. But this may cause resource-shortage problems for other agents who are producing high-profitmargin products. In this case, the behavior of selfinterested agents is not aligned with the designed organization goal.

To illustrate this point, suppose a multidivision, multiproduct firm allocates its logistics capabilities (transportation, warehouse space, etc.) among the various divisions. We will consider the warehousescheduling problem, where warehouse space has to be allocated among three autonomous units, each with a separate product line. Each unit has its own decision process incorporating its local considerations, preferences, and objectives, and the unit is rewarded as a profit center. Assume their preferences are superadditive, i.e., there is complementarity. The complementarities may arise from the fact that if warehouse space is obtained in Location A for Product X, then it is worth more to the unit to have Location A also store

Product Y (because, for example, most of the orders are for X and Y together). There are often conflicting interests over shared resources: In this case, other units may want to acquire storage space in the warehouse at Location A also. It is common sense to allocate the warehouse space to those products which are “most valuable,” but this intuitive concept is not always easy to operationalize. Divisions that compete to have their products stored in Location A may well have an incentive to inflate the value of their respective products so as to guarantee they will be stored there. Therefore, when asking for local cost and value information to make the companywide allocation decisions, the information will be distorted, and hence the overall decision invalid.

Although the supply chain coordination may be ITenabled and information sharing across the supply chain has become much easier, critical questions still remain to be asked: What information gets shared? Is the information truthful? Is there still hidden information across the supply chain—hidden not because of the inability to share but because of the unwillingness to share? More importantly, how can advanced IT contribute to designing an incentive-aligned supply chain coordination system, so that the outcome serves the overall organizational goal?

## 5.2. Research Challenges

One solution proposed to address the incentivealignment problem in the supply chain has been the introduction of a market mechanism where the storage space in Location A will be sold to the highest bidders so that the divisions utilizing Location A are required to rent the warehouse space. This price mechanism is designed to minimize the problem of value inflation by the divisional units that want to use the warehouse. However, when the firm is operated as a collection of independent profit centers, economics tells us that potential problems exist—if each profit center is allowed to set its own prices for the goods or services it provides, the quantities of the final goods and services produced by the firm are very rarely optimal (e.g., Jensen 1998). Some authors (e.g., Jensen) suggest that the headquarters set the transfer prices between the divisions. But that approach has difficulties as well: The firm has been divisionalized because the headquarters do not have accurate information about all aspects—such as cost and demand figures—of the goods being produced by the divisions. Therefore, it is not realistic to assume that the headquarters then have the knowledge to determine what this good or service is worth within the internal economy of their firm.

Fortunately, the advent of electronic commerce presents opportunities for exploring new forms of organizational-coordination mechanisms that can be used to provide IT support in market organizations. For example, the computational power provided by network servers comes for free and has not been exploited so far (Bayers 2000). With more and more companies implementing electronic-commerce solutions, the possibility of introducing more computations in marketclearing mechanisms opens a new door to market-based applications in situations that were previously thought to have to be coordinated only by hierarchical methods—even by the most fervent proponents of the market organizations—such as organizational-resource allocation when complementarities are present.

One of the recent research efforts in this direction is the bundle-auction mechanism designed by Fan et al. (1999) and later extended for the supply chain case (Fan et al. 2001). Their method allows the organizational units to demand a combination of warehouses and/or transportation capacity with a single-bid price, and the headquarters allocates the warehouse space so as to maximize the organization’s benefit. The decentralized mechanism is implemented with the headquarters just acting as a market maker. Each unit responds with a bid for resources based on its own managerial objective, and a bid can be in “bundled form,” i.e., it may specify one price for a whole combination or “bundle” of resources. For example, unit 1 may demand space at Warehouse A for Product X and Product Y at the price of $b _ { \mathrm { A } } ( X ,$ Y ). The headquarters collects all the bids and tries to maximize the value of the warehouses at the bid prices received from the units, subject to the limitation of available resource totals. The competition between different units will induce them to state the correct cost/value information, or their best estimate thereof. In Fan et al. (2001) it is proved how this system satisfies the requirements of incentive alignment: No party can be better off by misrepresenting the (private) information they have available—thus reducing information distortion in the supply chain; and the headquarters, by playing the role of market maker maximizing his profit, allocates the warehouse space in a manner that contributes to maximizing firm profit.

What is also noteworthy about this market mechanism is that it takes advantage of the computational power provided by the information system (unlike the more traditional “manual” markets where very little computation is required), making this auction mechanism a feasible real-time procedure for supply chain coordination.

We believe that market-based supply chain coordination can be run efficiently with the proper information systems support. The abovementioned research is only the first attempt towards this direction. To achieve results that could be interpreted as being incentive aligned, many assumptions were made, including ones bearing on the number of agents competing for supply chain resources and the infinite divisibility of available resources. There are still several challenging research issues that need to be faced: (1) How does one design an economic mechanism that allows divisions to trade goods and/or services amongst themselves? Can such a market-oriented system still be implemented when only a small number of agents are involved? (2) How can we measure whether the actual behavior in such a system is consistent with the theoretical prediction? (3) What are the properties of an information system that support the management of such a firm? This third question has so far been largely ignored by economists; however, no system can be operationalized without explicitly considering the interaction between the economic principles of the system and their informational requirements. For example, economists sometimes are satisfied with demonstrating that “an equilibrium (properly defined) exists,” but they fail to show how it is attained, and at times even ignore whether the computational requirements are feasible or not in practice. In short, an operational economic mechanism should explicitly address information systems issues, such as computational feasibility and information requirements.

## 6. Incentive Alignment: A Research Agenda

We have so far argued the case for incentive alignment by focusing on three important IS areas, illustrating both how incentives play a role and what research challenges exist in designing incentive-aligned systems. Summarizing the above discussion, the following issues, from the practitioner’s perspective, need to be addressed when designing an incentive-aligned information system:

1. What is the nature of the information system to be designed? What is the goal of the system? What type of information will be captured, and how is it going to be used or processed in the information system? Who will provide the information? Who will benefit from its use?

2. What is the most appropriate mix of design paradigms? Is user behavior mainly driven by economic incentives, or by social incentives? What is the relationship between the incentives and the expected behavior?

3. Is there a mechanism that induces the appropriate user behavior, while distilling an outcome that contributes to the organizational goal, thus achieving incentive alignment?

4. What are the attributes that we can use to measure incentive alignment of the system?

To answer the above questions, we present in Figure 1 a general framework that helps establish a research agenda for designing incentive-aligned information systems.

Figure 1 shows which factors can be influenced by the information systems designer (square boxes) and which theories or disciplines (rounded boxes) might be relevant to explain the relationship between user behavior, the system’s objectives, and the overall outcome. The factors within the ovals are exogenous variables not under the control of the systems designer, such as the organizational-incentive structure and organizational objectives.<sup>2</sup> An arrow from A to B in Figure 1 means that A (partially) explains B.

Figure 1 Information Systems Design Framework for Incentive Alignment  
![](/api/attachments/EED6UYFX/fulltext/images/f225552ee2481abaa65ef0de4f8a3dc1f805207aa04f0969823f3ff690164fcf.jpg)

Central to our view is the dialectical relationship— represented by the two arrows in the opposite directions—between user behavior and the mechanism incorporated in the information system. On the one hand, the rules embedded in the system affect the user’s behavior; on the other hand, the system is planned as a function of what behavior might be anticipated, and is ultimately designed to induce behavior in line with the system’s and organization’s objectives, hence the arrows in both directions. The user’s behavior, apart from being affected by the rules incorporated in the system, is furthermore determined by the organizational-incentive structure. Pertinent behavioral theories from various disciplines such as psychology, sociology, economics, etc., allow us to anticipate and explain certain user behavior in light of the rules and procedures implemented in the system and the rewards given by the organization for this behavior. This anticipated user behavior, together with the organizational goals and objectives, affects the design choice of the mechanism in the information system. From this general framework, we raise the following research questions.

Design Models. What are the most effective models of information system design that incorporate all three dimensions (i.e., software engineering, technology acceptance, and incentive alignment) as design objectives? How should existing models be modified to reflect the incentive-alignment requirements?

Research Theories. How do theories from other disciplines, such as psychology, economics, and political science affect the design of incentive-aligned information systems? What is the appropriate theoretical mix? For example, there is a rich body of literature on mechanism design in economics which looks at incentive issues from a bounded rationality perspective (e.g., Ledyard 1989, Myerson 1989). The theory of organizational altruism in psychology assumes individuals have a moral commitment to the organization (e.g., Brief and Motowidlo 1986, Organ 1988). To what extent do these theories apply to designing incentivealigned information systems? The study of such topics may shed light on how to resolve incentive-alignment issues in information systems design and may fundamentally change the underlying assumptions of an information system.

Design Tools. What are the appropriate tools to deploy for a system to meet the incentive-alignment requirements? Are traditional tools such as voting mechanisms still applicable under such requirement? Would market mechanisms fare better? Under what conditions is a market mechanism applicable in an internal organizational environment?

Theoretical Results. How do we validate the results of the theoretical design? How do we test that this theoretical behavior is followed in practice?

Measurement Metrics. How do we test the outcome of such an information system? How do we test whether the design objectives are met? What attributes (e.g., degree of information distortion, degree of divergence of actual use from expected use) can we test, and what are the appropriate metrics?

As a first step towards designing an incentivealigned information system, Ba et al. (2000) describe the theoretical design of a mechanism that can be implemented as a distributed decision support system to select investments in knowledge projects within an organization. The main organizational objective is to maximize the return on its investments in knowledge. The research theory that makes up the underlying assumption of the mechanism is that decision makers are driven by economic incentives. They have local information about the expected value of the knowledge and have control over local budgets. Considering that knowledge is a (local) public good within the organization, user behavior would be affected in that selfinterested economic agents have an incentive to understate their true valuations of a knowledge project.

A robust mechanism is therefore needed to prevent misrepresenting information about knowledge valuation (design objective). That is, a rational economic agent’s dominant strategy should be to accurately derive and submit his true valuation. Submitting a valuation higher than the true will expose the agent to the risk that he will have to pay more for the knowledge than it is worth to him, submitting a valuation lower than the true one may result in the knowledge not being provided. As a design tool, a market mechanism, specifically, a double-auction bundle market, is used to collect and process individual valuation information for knowledge projects. The calculation of each agent’s payment is the crucial point in this mechanism: The payment is guaranteed to be less than the valuation, and is dependent on the valuations submitted by other agents (and therefore one agent cannot individually influence the exact amount he will have to pay for acquiring the knowledge). The theoretical results indicate that the system is incentive aligned: Agents have the right incentives to derive and state accurate inputs, and the system selects the projects that maximize the organization’s return on investment.

## 7. Summary and Conclusions

We have identified a dimension that so far has not received enough attention in the information systems design literature: incentive alignment. The requirements of incentive alignment state that for an information system to be correctly designed, it should embody the right incentives, so that users have no incentive to cheat the system or can never be better off by distorting information. The role of incentive alignment in organization management and design is becoming more important as decentralized organizations opt for distributed information systems. As information systems are used for more advanced tasks, these tasks oftentimes require information that is difficult to verify. Moreover, when users are affected by decisions based upon the information they provide, there is the danger that they will try to influence the decision to their benefit by misrepresenting their information. IS design should be aware of such threats, and more importantly, the methods and procedures that support the decision making should be designed so that no user can derive a benefit from such misrepresentation. In each of these cases, the information system’s goal, which reflects the overall organizational goal, and the user incentives are aligned.

The examples given in this paper were a first step towards designing systems that are incentive aligned. Empirical evidence of their effectiveness, however, is lacking at present. We hope that this paper contributes to at least the following:

• Increase awareness of user-incentive issues when the information they provide is private and/or hard to verify,

• Stimulate research into methods and procedures that guarantee that the system’s goals and user incentives are aligned so that the danger of information distortion is minimized.

Consideration of those issues will improve the quality of decisions that are supported by information systems.

## References

Adler, P. 2001. Market, hierarchy, and trust: The knowledge economy and the future of capitalism. Organ. Sci. 12(2) 214–234.

Arrow, K. 1962. Economic welfare and the allocation of resources for invention. The Rate and Direction of Incentive Activity: Economic and Social Factors. Princeton University Press, Princeton, NJ. 609–625.

——. 1963 Social Choice and Individual Values, 2nd ed. Wiley, New York.

Ba, S., J. Stallaert, A. B. Whinston. 2001. Optimal investment in knowledge within a firm using a market mechanism. Management Sci. 47(9) Forthcoming.

Banker, R., R. Kauffman. 1991. Reuse and productivity in integrated computer-aided software. MIS Quart. 15(3) 375–401.

Bayers, C. 2000. The bot.com future: Capitalist constructions. Wired 8 (March) 210–219.

Benbasat, I., A. S. Dexter, P. Todd. 1986. An experimental program investigating color-enhanced and graphical information presentation: An integration of the findings. Comm. ACM 29(11) 1094–1105.

——, L. H. Lim. 1993. The effects of group, task, context, and technology variables on the usefulness of group support systems: A meta-analysis of experimental studies. Small Group Res. 24(4) 430–462.

Brief, A. P., S. J. Motowidlo. 1986. Prosocial organizational behaviors. Acad. Management Rev. 10 710–725.

Briggs, R., J. Nunamaker, R. Sprague. 1998. 1001 unanswered research questions in GSS. J. Management Inform. Systems 14(3) 3– 21.

Burk, K., K. Aytes. 1998. A longitudinal analysis of the effects of media richness on cohesion development and process satisfaction in

computer-supported workgroups. Proc. Thirty-First Hawaii Internat. Conf. Systems Sci. 1 135–144.

Buxton, J. N., B. Randell, eds, 1969. Software engineering techniques. Rep. Conf. (sponsored by the NATO Science Committee) Rome, Italy, and 1970. Scientific Affairs Division, NATO Brussels, Belgium.

Byrd, T. A. 1992. Implementation and use of expert systems in organizations: Perception of knowledge engineers. J. Management Inform. Systems 8(4) 97–116.

Chen, H., P. Hsu, R. Orwig, L. Hoopes, J. Nunamaker. 1994. Automatic concept classification of text from electronic meetings. Comm. ACM 37(10) 56–72.

Clarke, E. H. 1971. Multipart pricing of public goods. Public Choice 11(1) 17–33.

Condorcet, Marquis de. 1785. Essai sur l’application de l’analyse a\` la probabilite´ des decisions rendues a\` la pluralite´ des voix. Paris, France.

Constant, D., S. Kiesler, L. Sproull. 1994. What’s mine is ours, or is it? A study of attitudes about information sharing. Inform. Systems Res. 5(4) 400–421.

Cross, G. 2000. How e-business is transforming supply chain management. J. Bus. Strategy (March-April) 21(2) 36–39.

Dasgupta, P., P. Hammond, E. Maskin. 1979. The implementation of social choice rules: Some results on incentive compatibility. Rev. Econom. Stud. 46(2) 185–216.

Davenport, T. H., L. Prusak. 1998. Working Knowledge: How Organizations Manage What They Know. Harvard Bus. School Press, Boston, MA.

Davey, A., D. Olson. 1998. Multiple criteria decision making models in group decision support. Group Decision and Negotiation 7(1) 55–75.

Davis, F. D., R. P. Bagozzi, P. R. Warshaw. 1989. User acceptance of computer technology: A comparison of two theoretical models. Management Sci. 35(8) 982–1003.

Deckmyn, D. 2000. Most enterprise computing efforts fail. Computerworld. (March 21).

Dekleva, S., D. Drehmer. 1997. Measuring software engineering evolution: A Rasch calibration. Inform. Systems Res. March, 8(1) 95– 104.

Dennis, A. R., J. S. Valacich. 1994. Group, subgroup, and nominal group idea generation: New rules for a new media? J. Management 20(4) 723–736.

DeSanctis, G. L., M. S. Poole. 1994. Capturing the complexity in advanced technology use: Adaptive structuration theory. Organ. Sci. 5(2) 121–147.

Ellis, C. A., G. L. Rein, S. L. Jarvenpaa. 1990. Nick experimentation: Selected results concerning effectiveness of meeting support technology. J. Management Inform. Systems 6(3) 7–24.

Fan, M., J. Stallaert, A. B. Whinston. 1999. The design and development of a financial cybermarket with a bundle trading mechanism. Internat. J. Electronic Commerce. 4(1) 5–23.

, ——. 2001. Decentralized mechanism design for supply chain organizations using an auction market. Inform. Systems Res. Forthcoming.

Fjermestad, J., S. R. Hiltz. 1998. An assessment of group support

systems experiment research: Methodology and results. J. Management Inform. Systems 15(3) 7–149.

——, ——. 2000. Group support systems: A descriptive evaluation of case and field studies. J. Management Inform. Systems 17(3) 115–159.

Gallupe, R. B., G DeSanctis, G. W. Dickson. 1988. Computer-based support for group problem-finding: An experimental investigation. MIS Quart. 12(2) 277–296.

Garvin, D. 1997. A note on knowledge management. Harvard Business School article. Product Number: 9–398–031.

Gavish, B., J. H. Gerdes, Jr. 1997. Voting mechanisms and their implications in a GDSS environment. Ann. Oper. Res. 71 41–74.

Goodhue, D. L. 1995. Task-technology fit and individual performance. MIS Quart. 19(2) 213–236.

Groves, T. 1973. Incentives in teams. Econometrica 41 617–631.

Hansen, M., N. Nohria, T. Tierney. 1999. What’s your strategy for managing knowledge? Harvard Bus. Rev. (March-April) 106– 116.

Henson, K. L., C. Hughes. 1991. A two-dimensional approach to systems development. J. Inform. Systems Management, Winter 8(1).

Hightower, L. 1998. Private communication.

——, A. G. Sogomonian, J. Stallaert. 1997. Banking on Monte Carlo. Energy and Power Risk Management 12–14.

Holmstrom, B. 1982. Moral hazard in teams. Bell J. Econom. 13 324– 340.

Jensen, M. C. 1998. Foundations of Organizational Strategy. Harvard University Press, Cambridge, MA.

Kollock, P. 1999. The economies of on-line cooperation. M. Smith and P. Kollock, eds. Communities in Cyberspace. Routledge, London, U.K. 221.

Ledyard, J. 1989. Incentive compatibility. J. Eatwell, M. Milgate, and P. Newman, eds. Allocation, Information and Markets. Norton, New York. 141–151.

Mas-Colell, A., M. D. Whinston, J. R. Green. 1995. Microeconomic Theory. Oxford University Press, Oxford, New York.

Myerson, R. 1979. Incentive compatibility and the bargaining problem. Econometrica 47 61–74.

McGrath, J. E., H. Arrow. 1996. Introduction: The JEMCO 2 study of time, technology and groups. Comput. Supported Cooperative Work. 4(2) 107–126.

Myerson, R. B. 1989. Mechanism design. J. Eatwell, M. Milgate, and P. Newman, eds. Allocation Information, and Markets. Norton, New York. 191–206.

Narayanan, V. G., A. Raman. 2000. Aligning incentives for supply chain efficiency. Harvard Business School article. Product number: 600–110.

Naur, P., B. Randell, eds. 1968. Software engineering. Rep. Conf. (sponsored by the NATO Science Committee) Garmisch, Germany, and 1969. Scientific Affairs Division, NATO Brussels, Belgium.

O’Reilly, C., J. Chatman. 1986. Organizational commitment and psychological attachment: The effects of compliance, identification, and internalization on prosocial behavior. J. Appl. Psych 71(3) 492–499.

Organ, D. W. 1988. Organizational citizenship behavior: The good soldier syndrome. Lexington Books, Lexington, MA.

Orlikowski, W. 2000. Using technology and constituting structures: A practice lens for studying technology in organizations. Organ. Sci. 11(4) 404–428

——, D. Hoffman. 1997. An improvisational model for change management: The case of groupware technologies. Sloan Management Rev. 38(2) 11–21.

Palfrey, T., J. Prisbrey. 1997. Anomalous behavior in public goods experiments: How much and why? Amer. Econom. Rev. 87(5) 829–846.

Pressman, R. S. 2000. Software Engineering: A Practitioner’s Approach. McGraw-Hill College Division 806, Boston, MA.

Radner, R. 1986. The internal economy of large firms. Econom. J. Supplement: Conf. papers 96 1–22.

Samuelson, P. 1954. The pure theory of public expenditure. Rev. Econom. Statistics 36(4) 387–389.

Souza, E. 1990. Strategies for software engineering implementation. J. Inform. Systems Management 7(3) 33–37.

Izak Benbasat, Senior Editor. This paper was received on November 3, 2000.

Subramanian, G. H., G. Zarnich. 1996. An examination of some software development effort and productivity determinants in ICASE tool projects. J. Management Inform. Systems 12(4).

Swanson, K., D. McComb, J. Smith, D. McCubbrey. 1991. The application software factory: Applying total quality techniques to systems development. MIS Quart. 15(4) 566–579.

Szulanski, G. 1996. Exploring internal stickiness: impediments to the transfer of best practice within the firm. Strategic Management J. 17 (Winter) 27–43.

Tapscott, D., D. Ticoll, A. Lowy. 1999. Digital Capital: Harnessing the Power of Business Webs. Harvard Business School Press, Boston, MA 272.

Todd, P., I. Benbasat. 1999. Evaluating the impact of DSS, cognitive effort and incentives on strategy selection. Inform. Systems Res. 10(4) 356–374.

Turban, E., R. K. Rainer, R.E. Potter. 2001. Introduction to information technology. John Wiley & Sons, New York 550.

Vessey, I., D. F. Galletta. 1991. Cognitive fit: An empirical study of information acquisition. Inform. Systems Res. 2(1) 63–84.
