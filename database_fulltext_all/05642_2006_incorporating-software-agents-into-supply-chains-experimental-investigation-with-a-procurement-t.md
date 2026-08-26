---
otero_id: 5642
otero_key: "F45SR9AG"
title: "Incorporating Software Agents into Supply Chains: Experimental Investigation with a Procurement Task"
authors: "Mark E. Nissen; Kishore Sengupta"
year: "2006"
journal: "MIS Quarterly"
doi: "10.2307/25148721"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Incorporating Software Agents into Supply Chains: Experimental Investigation with a Procurement Task

Author(s): Mark E. Nissen and Kishore Sengupta

Source: MIS Quarterly, Vol. 30, No. 1 (Mar., 2006), pp. 145-166

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/25148721

Accessed: 28/06/2014 16:16

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# INCORPORATING SOFTWARE AGENTS INTO SUPPLY CHAINS: EXPERIMENTAL INVESTIGATION WITH A PROCUREMENT TASK $^{1}$

By: Mark E. Nissen
Naval Postgraduate School
555 Dyer Road, Code SM/Ni
Monterey, CA 93943-5000
U.S.A.
MNissen@nps.edu

Kishore Sengupta
INSEAD
Boulevard de Constance
77305 Fontainebleau Cedex
FRANCE
kishore.sengupta@insead.edu

## Abstract

Recently, researchers have begun investigating an emerging, technology-enabled innovation that involves the use of intelligent software agents in enterprise supply chains. Software agents combine and integrate capabilities of several information technology classes in a novel manner that enables supply chain management and decision making in modes not supported previously by IT and not reported previously in the information systems literature. Indeed, federations and swarms of software agents today are moving the boundaries of computer-aided decision making more generally. Such moving

boundaries highlight promising new opportunities for competitive advantage in business, in addition to novel theoretical insights. But they also call for shifting research thrusts in information systems. The stream of research associated with this article is taking some first steps to address such issues by examining experimentally the capabilities, limitations, and boundaries of agent technology for computer-based decision support and automation in the procurement domain. Procurement represents an area of particular potential for agent-based process innovation, as well as reflecting some of the greatest technological advances in terms of agents emerging from the laboratory. Procurement is imbued with considerable ambiguity in its task environment, ambiguity that presents a fundamental limitation to IT-based automation of decision making and knowledge work. By investigating the comparative performance of human and software agents across varying levels of ambiguity in the procurement domain, the experimentation described in this article helps to elucidate some new boundaries of computer-based decision making quite broadly. We seek in particular to learn from this domain and to help inform computer-based decision making, agent technological design, and IS research more generally.

Keywords: Agents, artificial intelligence, behavioral decision theory, computer-aided decision making, human performance, procurement; supply chain management

## Introduction

Supply chain management represents a critical competency in today's global business environment (Gebauer et al. 1998; Lee and Billington 1995; Mabert and Venkataramanan 1998; Monczka et al. 1998; Nissen 1997; Swaminathan et al. 1998). A number of technology-enabled practices (e.g., electronic data interchange, justin-time deliveries, supplier inventory management) are employed now to improve the effectiveness of enterprise supply chains. Researchers in information systems are addressing actively numerous and diverse problems and issues associated with the integration of information technology in this regard. For instance, we find studies of electronic marketplaces (e.g., Bakos 1998; Hess and Kemerer 1994), interorganizational IS linking supply chain participants (e.g., Kumar and van Dissel 1996; Mukhopadhyay et al. 1995), and IT-enabled strategy (e.g., Clemons and Row 1991; Johnston and Carrico 1988) among the IS literature contributing to our knowledge in this area.

Recently, IS researchers have begun investigating an emerging, technology-enabled innovation that involves the use of intelligent software agents along the enterprise supply chain. For instance, many scholars (e.g., Collins et al. 1998; Gini and Boddy 1998; Mehra and Nissen 1998; Rodriguez-Aguilar et al. 1998; Wurman et al. 1998) argue that intelligent software agents offer tremendous potential for automation and support of supply chain processes, particularly on the buyer side (e.g., procurement). Software agents combine capabilities of several IT classes (e.g., DSS, expert systems, parallel processors, mobile computing) and integrate such capabilities in a novel manner (e.g., autonomous, mobile decision makers working in massively parallel mode). Early results from the laboratory suggest this enables supply chain management and decision making in modes not supported previously by IT. For instance, emerging, agent-enabled, supply chain functionalities can enable whole new business models and modes of operation (e.g., supply chain re-intermediation; see Nissen 2000).

Indeed, federations and swarms of software agents today are moving the boundaries of computer-aided decision making. The relative capabilities—and hence roles—of people and machines are shifting progressively as a result of software agents. Some of the shifts (e.g., people using agents such as shopping “bots” to gather product information) are technologically incremental, explained well by IS theory, and found broadly in practice today. But other shifts (e.g., software agents using people to clarify procurement ambiguity) are technologically abrupt, explained less well in terms of current theory, and found rarely in practice today.

As the advancing capabilities of software agents enable progressive transition from computer-based decision aids to computer-based decision makers, important questions arise about where to use such agents best, how much decision-making authority to grant them, when people need to intervene in autonomous-agent processes, and how new designs may overcome persistent technological inadequacies of agent software today. In addition to providing novel theoretical insights, these shifting boundaries highlight promising new opportunities for competitive advantage in business. However, they also reveal large gaps in our knowledge about integrating software agents with people in supply chains. This calls for a corresponding new thrust in IS research toward answering the question: What are the issues in understanding the applicability of software agents and the person-agent boundary in procurement processes?

Extant theory on computer-based decision making informs both research and practice incompletely here. The research is extensive in detailing how decision outcomes are influenced by the fit between the type of task and decision support capabilities (e.g., Goodhue and Thompson 1995; Lowe et al. 2002). It also shows how decision processes and strategies further mediate this relationship (Todd and Benbasat 1992, 1994, 1999). Research has also documented the role of decision-maker characteristics such as experience (e.g., Glover et al. 1997). However, most such theory is asymmetric in terms of computers supporting human decision making as opposed to people supporting computer decision making. As the sophistication and capability of autonomous agents continue to increase, people will be called progressively often to support software agent decision making, in addition to software agents being called to support decision making by people. Current theory says very little about such shifting roles and capabilities of human and software decision making and decision support. The research is particularly sparse on the role of decision support in the context of ambiguity, which is both pervasive and pernicious in terms of IT automation and support in the procurement domain (Gebauer et al. 1998).

The stream of research associated with this article is taking some first steps to improve our understanding in this area. Through systematic study all along the supply chain, we examine critically the capabilities, limitations, and boundaries of agent technology for computer-based decision support and automation. In this article, we describe the first study along these lines: an experiment that investigates how to share key decision making and other procurement responsibilities between human and software agents on the buyer side of simple, two-tier supply chains. Specifically, we concentrate on an important class of procurement called maintenance, repairs, and operations (MRO), where the procurement specifications are laden frequently with ambiguity. In terms of importance, spending on such indirect (i.e., non-production) goods and services accounts for over 30 percent of enterprise resources (Kasturi 2000). Many MRO items (e.g., office desks and chairs, personal computers and software, equipment maintenance and repair) are not handled well by current material/ enterprise planning systems. This is due in great part to the unpredictable timing and item diversity associated with MRO procurement. Moreover, the specification ambiguity inherent in many MRO procurements casts considerable doubt on how far the role of people in the supply chain process can be reduced.

In a proximal sense, the paper contributes insights into the suitability of agents for MRO procurement. Considerations such as unpredictable timing, item diversity, technological advance, delegation of tasks to computers and ambiguity, however, are not limited to MRO or even the procurement domain. Rather, our studies of agents here offer potential to inform computer-based decision making, agent technological design, and IS research more generally.

The balance of this article is organized as follows. The next section provides an overview of software and human agents' respective capabilities. Subsequently we detail in turn the research method, report the results, and discuss their implications for research and practice.

## Software and Human Agents

We begin this section by summarizing respective capabilities of software and human agents, which are then considered in the context of behavioral decision theory in order to formulate hypotheses on the performance effects of human or software agent procurement task sharing along the supply chain.

## Agent Concepts, Applications, and Roles in Adaptive Decision Making

Although researchers have yet to agree on a common definition for software agents (Franklin and Graesser 1996), the description by Jennings et al. (1998, p. 8) conveys most of the key ideas:

an agent is a computer system, situated in some environment, that is capable of flexible autonomous action in order to meet its design objectives.

Building upon the literature survey and classification system of Nissen (2001), we can group extant agent applications into three classes that are insightful for studying procurement: (1) information retrieval agents, (2) advisory agents, and (3) performative agents. These three classes both inform and correspond well to the adaptive view of decision making that we discuss below. Table 1 summarizes the key properties associated with each agent class and references several representative applications.

The adaptive view of decision making posits that individuals adopt a multiple-stage decision sequence entailing initial screening of alternatives, followed by detailed evaluation and choice (Payne et al. 1993, pp. 35-37). The notion of multiple steps in procurement decisions has been examined extensively in research on consumer information processing, particularly in regard to forming consideration sets. A core finding in this research is that decision makers employ a tiered decision process (Gensch 1987; Levin et al. 2000; Shocker et al. 1991), typically consisting of three stages (Kardes et al. 1993; Roberts and Lattin 1991, 1997; Shocker et al. 1991).

\- Form a universal set. This refers to all suitable products available in the marketplace (Roberts and Lattin 1991), either within the same product category or encompassing multiple categories (Ratneshwar et al. 1996). In practice, because of their cognitive limitations, decision makers create retrieval sets (i.e., subsets of universal sets; Kardes et al. 1993).

\- Form a consideration set. This subset is formed after an initial screening of the universal or retrieval set. Items in the consideration set can belong to the same or different product categories (Ratneshwar et al. 1996).

• Make a choice. The decision maker scrutinizes the consideration set and exercises a choice mechanism to select one or more items for purchase.

The implications of the tiered view of decision making are key to understanding the role that agents can play in assisting procurement decisions. In operational supply chain environments, retrieval sets are formed generally through volumes of (paper) product catalogs as well as online catalog databases. The use of information retrieval agents is intended to automate this task. The creation of retrieval sets by decision makers is affected largely by memory-oriented factors such as the level of prior knowledge, processing capacity, attention, and comprehension (Alba and Hutchinson 1987, Kardes et al. 1993). When agents perform the task, they bring to bear some advantages over humans (e.g., greater processing capacity and attention) but also some disadvantages (e.g., less prior knowledge and comprehension). For agents to form effective retrieval sets, they must know (from task specifications or prior knowledge of user preferences) what to look for (i.e., product items and categories) and where to search (i.e., specific online catalogs and/or databases). Most agents perform this task using relatively simple rules and other mechanisms (e.g., predefined checkboxes) to select items for inclusion from a larger set (e.g., online product catalog, the Internet). Once set up to reflect users' information preferences, agents in this class can retrieve product and service information autonomously. However, users must still interpret information manually. Also, users remain responsible for making and executing purchase decisions based on the information retrieved.

In most operational environments, the screening process underlying the creation of consideration sets is performed manually (e.g., by looking through catalogs, analyzing the results of search-engine queries). Advisory agents automate this task by applying screening criteria to convert retrieval sets into consideration sets. Advisory agents thus perform in a classical decision-support role. Consideration set formation is primarily a function of cognitive effort oriented factors such as evaluation costs and benefits (Hauser and Wernerfelt 1990; Roberts and Lattin 1991, 1997).

Decision makers often seek to simplify the burden of the task (and create consideration sets of tractable sizes) by using non-compensatory attribute-based rules (Roberts and Lattin 1997). When working with explicit screening criteria, agents can improve the process with enhanced cognitive effort, thereby creating sets with potentially larger numbers of relevant entries than the two to seven items typically found in manually created consideration sets (Desai and Hoyer 2000). Set size is important, because an item cannot be chosen unless it is in the consideration set (Nedungadi 1990). Agents can also enhance cognitive control (Hammond and Summers 1972) by applying criteria consistently, thus creating sets with greater stability (i.e., consistency across similar situations). Taken together, such agent interventions can ensure higher quality consideration sets. For agents to form effective consideration sets, the usually implicit evaluation criteria and problem-solving pro-

<table><tr><td colspan="3">Table 1. Key Agent Properties in Procurement</td></tr><tr><td>Agent Class</td><td>Properties</td><td>Representative Applications</td></tr><tr><td>Information retrieval</td><td>·Focus on collecting information about products and services·Supports formation of buyer retrieval sets·Affected largely by memory-oriented factors·Agents must be told what to look for·Users responsible for making and executing purchase decisions based on information retrieved</td><td>·Compact disk information (Krulwich 1996)·Computer equipment information (see http://www.uvision.com/)·Advertising information (see http://www.pricewatch.com)·Insurance information (see http://www.dmatters.co.uk)·Web indexing (Chen et al. 1998; Etzioni and Weld 1995)·Report writing (see http://www.amulet.com)·Publishing (Knowles 1995)·Assisted browsing (Burke et al. 1997)·Commercial shopping “bots” (see http://www.ecom.cmu.edu/elib_eclbots.htm)</td></tr><tr><td>Advisory</td><td>·Focus on providing intelligent purchase advice·Supports formation of buyer consideration sets·Affected largely by cognitive effort oriented factors·Evaluation factors and processing approaches must be made explicit·Users responsible for making and executing purchase decisions based on agent advice</td><td>·Recommendations for CDs and movies (Maes 1997)·Electronic concierge (Etzioni and Weld 1995)·“Host” for college campus visits (Zeng and Sycara 1995)·Planning support (Maturana and Norrie 1997)·Electronic shopping (e.g., Redmond 2002; Wallace 2000)·Supply chains (e.g., Chen et al. 2003; Kimbrough et al. 2002)</td></tr><tr><td>Performative</td><td>·Focus on decision making and executing binding commercial transactions·Automates buyer choice activity·Affected largely by cognitive effort oriented factors·Choice criteria and processing rules must be made explicit·Users delegate authority to and monitor performance of agents</td><td>·Marketspaces for simple business transactions (e.g., Chavez and Maes 1996)·Coordinate as supply chain participants (Fox and Barbuceanu 2003)·Support knowledge fusion (Preece et al. 1999)·Buy and sell well-defined goods in auctions (Hu, Reeves, and Wong 1999; Hu, Yen, and Chung 1999; Rodriguez-Aguilar et al. 1998; Zeng et al. 2000)·Straightforward price negotiation (Bui 1996)·Scheduling (Sen 1997)·Cooperative-learning environment (Boy 1997)·Digital library services (Mullen and Wellman 1996)</td></tr></table>

cesses $^{2}$ employed by decision makers must be made explicit. Once programmed and set up to reflect users' decision-making criteria and processes, agents in this class can reason intelligently from information collected and can make purchase recommendations autonomously for users. However, multi-attribute decision-making schemes require considerable time and interaction to establish through agents. And as with information retrieval agents above, users remain responsible for making and executing purchase decisions.

Choices of items in operational supply chain environments are made often by procurement specialists, brokers, and like intermediaries on behalf of users in the enterprise. The use of performative agents aims to automate this task. They reflect the greatest degree of delegation from users. Usually, choice entails consideration of alternatives across multiple attributes using compensatory rules (Creyer et al. 1990). Rules used by decision makers consider generally price as well as non-price product attributes (e.g., product capability, supplier reputation, lead time). The cognitive effort entailed in comparing alternatives across multiple attributes can be significant. As a result, decision makers resort often to satisficing behavior. Agents can improve the choice process by providing support for multi-attribute evaluation, thereby ensuring more comprehensive and consistent evaluation. For agents to accomplish the choice activities effectively, they must be delegated responsibility for decision making and executing transactions (e.g., without a person in the loop). Considerable effort and care is required to encode appropriate decision-making methods, task procedures, and enterprise rules. This requires choice criteria to be made explicit, along with the processing rules (e.g., relative importance of price and delivery reliability). However, the ability to make such methods, procedures, and rules explicit, and to guarantee correct agent behaviors, remains beyond the current state of the art for complex procurements and ambiguous decision contexts. For relatively simple procurements and clear decision contexts, however, the use of agents holds the promise of identifying higher quality solutions than those obtained from typical satisficing. Once set up to execute appropriate behaviors on behalf of their users, agents in this class perform important knowledge- and information-work activities autonomously, making decisions and executing commercial transactions through deliberate action. Further, many performative agents integrate capabilities of both information retrieval and advisory agents, in addition to automating the buyer choice activity. This leaves the user with little participation in the procurement task, aside from delegating authority to and monitoring the performance of such agents.

## Human and Agent Decision Making in Ambiguous Procurement Tasks

In behavioral decision theory, ambiguous decision situations are characterized as those in which “available information is scanty or obviously unreliable… and where expressed expectations of different individuals differ widely” (Ellsberg 1961, p. 660-661). $^{3}$ Ambiguous decision situations arise when a task’s specification is incomplete and/or imprecise in some fundamental sense (Muthukrishnan 1995). This can occur from several factors, such as missing information on product characteristics (Hoch and Ha 1986) or decision contexts (e.g., goal conflict or goal ambiguity) that make comparisons among products difficult (Frisch and Baron 1988). Some studies have operationalized ambiguity in a very specific sense: where parts of a task’s probability distribution are not available (e.g., Camerer and

Weber 1992; Einhorn and Hogarth 1985; Heath and Tversky 1991). In this study, we adopt a more general interpretation of ambiguity as implying incompleteness and/or imprecision in procurement specification, rather than incorporating claims about probability distributions. This is the basis of our concept specification ambiguity receiving the focus of attention in this study.

Extending the arguments above, specification ambiguity is an important issue in procurement. This is the case particularly for MRO items, which are notably less-structured and less-routine than are standardized commodities or production-line materials (Gebauer et al. 1998). Such ambiguity also impacts procurement performance as supply chains become more dynamic (e.g., as characterized by supply networks or supply webs) and as product-development cycles shorten (e.g., in time-to-market competition). In the former case, capabilities of new suppliers often are difficult to gauge in advance of placing time-critical orders (e.g., just-in-time). Hence important supplier information (e.g., quality level, trustworthiness) is unlikely to be available or complete, and expectations of different individuals concerning which supplier characteristics (e.g., quality, cost, speed, trustworthiness) are most important may vary considerably. In the latter case, suppliers often are developing new products in parallel with those of the buyer. Hence product information (e.g., performance level, quality, availability date) is likely to be scanty or unreliable. In either case, procurement specifications do not reflect the same level of specificity observed generally for standardized production orders.

Ambiguous procurement specifications often require an additional filter for the task to be executed (i.e., converting the specifications to a more precise and/or complete form). In the case of an office chair, for example, there are many styles (e.g., high back, adjustable, roll-able), models (e.g., leather, cloth, vinyl), colors, and price ranges and associated supplier information (e.g., location, reputation, terms, product availability) upon which a decision ultimately must be made. This requires domain knowledge and experience with products, technologies, and categories (West 1996; Wright and Lynch 1995). Also, ambiguous specifications can contain goal conflicts (e.g., where the specification implies multiple goals such as price, schedule, and/or performance without suggesting relative importance) and goal ambiguities (e.g., where the goals themselves are not clear; see Ratneshwar et al. 1996). Decision makers cope with ambiguity in specifications and/or their goals by including multiple product categories when constructing retrieval and consideration sets (Ratneshwar et al. 1996). They also postpone trade-offs in criteria until there is a clearer understanding of the problem (Huber and Klein 1991).

For agent performance, ambiguous specifications create significantly greater difficulty than do standardized or production counterparts (e.g., where the items can be found by simply looking up a specific part number in some catalog). This suggests the corresponding procurement agents must be able to reason on behalf of engineers, managers, and other principals, and they must be able to implement complicated reasoning strategies. These requirements constitute a territory far beyond the comparatively simple bot technologies.

<table><tr><td colspan="4">Table 2. Purchase Items</td></tr><tr><td>Item</td><td>Quantity</td><td>Specification Ambiguity</td><td>Rationale</td></tr><tr><td>Latitude</td><td>1</td><td>Low</td><td rowspan="4">Information provided is complete; task entails choice of supplier</td></tr><tr><td>Win98</td><td>1</td><td>Low</td></tr><tr><td>123456 (office desk)</td><td>2</td><td>Low</td></tr><tr><td>987654 (office chair)</td><td>3</td><td>Low</td></tr><tr><td>Executive desk</td><td>3</td><td>Moderate</td><td rowspan="4">Information provided is incomplete; difficult to compare products; difficult to create consideration set</td></tr><tr><td>Executive chair</td><td>2</td><td>Moderate</td></tr><tr><td>Mac</td><td>4</td><td>Moderate</td></tr><tr><td>Shake</td><td>4</td><td>Moderate</td></tr><tr><td>Burger</td><td>2</td><td>High</td><td rowspan="4">Information provided is imprecise; difficult to compare products; difficult to create universal and consideration set</td></tr><tr><td>Cola</td><td>3</td><td>High</td></tr><tr><td>PC</td><td>10</td><td>High</td></tr><tr><td>PC operating system</td><td>1</td><td>High</td></tr></table>

Therefore, the overarching implication of ambiguity in procurement specifications is that it places constraints on the extent to which procurement tasks can be automated through agents.

In order to specify these constraints, we outline first a set of example procurement tasks. The list in Table 2 includes an assortment of diverse product categories: electronics, furniture, and food items. The impact of specification ambiguity on the types of procurement tasks listed in Table 2 can be understood in the context of procurement quality, which is perhaps the most important criterion for such tasks (Gebauer et al. 1998; Nissen 2001; Zeng et al. 2000). Procurement quality can be thought of as a composite of two dimensions: accuracy and economy. Accuracy measures whether the procurement process succeeds in obtaining the right item (i.e., one matches the intent of the specification). Once the right item is located, economy is measured traditionally as being able to obtain the best possible price for it.

The four purchase items listed in Table 2 as being of low specification ambiguity represent specific brand names (e.g., Latitude computer) and part numbers (e.g., 123456) that can be purchased with no additional information or even an understanding of the item. The task entails essentially matching keywords or symbol strings (e.g., part number 987654 = office chair). Even rudimentary search engines and primitive shopping bots can accomplish such keyword matching efficiently and effectively. For these kinds of low-ambiguity items, the retrieval and consideration sets both incorporate items in homogeneous categories. Since the information provided is complete, screening can be accomplished by applying well-structured rules. Similarly, choice can be based on well-specified factors such as price differences across suppliers. Here procurement accuracy is almost guaranteed, provided the purchase item is available for sale.

The four purchase items classified with moderate specification ambiguity are not as straightforward, because the information provided is incomplete: the purchase item descriptions make it difficult to compare different products. The task is thus only partially amenable to keyword or string matches. The performance of search engines and shopping bots degrades noticeably when keyword matching becomes unreliable. Both relevant and extraneous items are likely to be retrieved. Although there may be at least a partial symbolic match (e.g., chair), this keyword match is insufficient to ensure procurement accuracy. It is more difficult to create appropriate consideration sets for moderate ambiguity specifications, because the retrieval sets often contain often multiple product categories (e.g., different types of chairs). The incompleteness of the information provided makes it more problematic to ascertain how closely an item being considered actually corresponds to the requirements. This difficulty also complicates the search for the best price.

The four purchase items noted as high specification ambiguity present a particular challenge. For instance, the item labeled "PC" is ambiguous with respect to what, exactly, is required. This symbol does not correspond to any specific brand name or part number. Here descriptive labels (i.e., partial keyword matches) such as "desk" and "chair" are not even available for guidance. Also, no vendor offers an item for sale called "PC," for example. The specifications are imprecise and are, therefore, not amenable to keyword or string matches. This leaves procurement accuracy in great jeopardy. Rather, procurement agents must be sufficiently knowledgeable to convert the specification into a request for some type of personal computer (e.g., Latitude, Mac, other). The same applies to the PC operating system. The burger and cola are similar, in that no product is listed with these labels. Agents must convert the task and search for items such as the Mac and Coke. For such items, even forming an adequate and understandable retrieval set presents challenges and complicates further the other steps (i.e., forming a consideration set and making a choice). In operational supply chains, ambiguity at this high level occurs regularly and can be handled at present only by human procurement agents.

<table><tr><td colspan="3">Table 3. Operationalization of Specification Ambiguity</td></tr><tr><td>Ambiguity Level</td><td>Operationalization</td><td>Forming retrieval/consideration set</td></tr><tr><td>Low</td><td>Specifications are sufficiently detailed</td><td>Keyword/string matches typically result in single-product categories</td></tr><tr><td rowspan="2">Moderate</td><td rowspan="2">Specifications are incomplete</td><td>Keyword/string matches typically result in multiple-product categories</td></tr><tr><td>Requires additional information on product attributes for resolving categories</td></tr><tr><td rowspan="2">High</td><td rowspan="2">Specifications are imprecise</td><td>Keyword/string matches not useful for creating retrieval set: specifications must first be converted to more complete form</td></tr><tr><td>Requires domain knowledge &amp; experience for specification conversion</td></tr></table>

Table 3 summarizes the operationalization of these three levels of specification ambiguity. Requests with low specification ambiguity enable identification of specific products (or even part numbers); keyword searches are sufficient and result generally in retrieval sets of single-product categories. Moderate specification ambiguity occurs when the requests enable identification of product types but not necessarily specific products. Keyword searches help, but only up to a point. The consideration set is likely to contain multiple product categories; information on additional product attributes is needed to resolve the issue. In purchases with high specification ambiguity, the request may enable identification of product classes but not product types or specific products. The initial specifications require conversion to a more precise form before searches can be made. The conversion requires domain knowledge and experience.

Expectations of agent performance can be discussed now in terms of these three levels of ambiguity. Consider first tasks with low specification ambiguity of the type shown in Table 2. For such tasks, creating a good retrieval set depends on the decision maker's capacity to exercise memory and recall. Given the evident advantages of information retrieval agents in this regard, their use should result in more comprehensive retrieval sets than those created by unassisted decision makers. An item cannot be selected unless it is in the retrieval set; the availability of more comprehensive retrieval sets enhances the prospect of making better choices. Therefore, the use of information retrieval agents should improve a decision maker's ability to locate the correct product and obtain the best price. Thus, in tasks with low specification ambiguity,

H1a: The use of information retrieval agents will result in higher quality procurement choices than those made manually (i.e., higher procurement economy and accuracy).

Consider now the use of other agents employed further along the multistage decision sequence. Beginning with advisory agents, they can overcome human limits on cognitive effort and cognitive control. Thus, advisory agents should create higher quality consideration sets than those formed by unassisted decision makers in terms of specific entries contained in the sets, as well as their ordering sequence (Kardes et al. 1993). Similar to the argument stated above, the availability of a higher quality consideration set increases the possibility of making a superior choice in terms of economy and accuracy. Thus, in tasks with low specification ambiguity,

H1b: The use of advisory agents will result in higher quality procurement choices than those made manually (i.e., higher procurement economy and accuracy).

Further, performative agents embody the cumulative operational abilities of information retrieval and advisory agents. Thus, in tasks with low specification ambiguity,

H1c: The use of performative agents will result in higher quality procurement choices than those made manually (i.e., higher procurement economy and accuracy).

H1d: The use of performative agents will result in higher quality procurement choices than those supported by either information retrieval or advisory agents (i.e., higher procurement economy and accuracy).

We address next situations of moderate specification ambiguity. Given incomplete product specifications, a retrieval set created by using information retrieval agents is likely to be composed of multiple product categories that include both relevant and extraneous items. The retrieval set is, thus, somewhat “noisy.” However, it is likely to contain all items relevant to the request (i.e., it is a superset of a “correct” retrieval set) and is, therefore, superior to one that can be created by an unassisted decision maker. Following the logic that an item cannot be chosen unless it is included in the retrieval set, the use of information retrieval agents should enhance the decision maker’s ability to (eventually) locate the correct product at the best price. Thus, in tasks with moderate specification ambiguity,

H2a: The use of information retrieval agents will result in higher quality procurement choices than those made manually (i.e., higher procurement economy and accuracy).

Similar to the situation with information retrieval agents, retrieval sets created by unassisted decision makers for moderate ambiguity specifications can also contain multiple product categories. The effectiveness of advisory agents in resolving across categories is limited today. A consideration set created by advisory agents can, thus, contain items somewhat removed from the intent of the procurement request (e.g., a swivel chair where the intended user simply needs a chair), thereby increasing the possibility of making an incorrect choice. However, in moderate ambiguity situations, advisory agents can still surpass decision makers in the cognitive effort entailed for narrowing the list of relevant items and ordering them. Moreover, the intended use of the item is clear, thereby avoiding the inclusion of items inappropriate to the request (e.g., the screening process for an executive chair will not retain a chair that is useful for homes but not offices). On balance, therefore, in moderate ambiguity tasks, the problem of resolving across categories is a limited one. The principal challenge is to ensure that the consideration set still contains enough relevant items to facilitate a high quality choice. This is where advisory agents should outperform unassisted decision makers. Therefore, in tasks with moderate specification ambiguity,

H2b: The use of advisory agents will result in higher quality procurement choices than those made manually (i.e., higher procurement economy and accuracy).

Finally, because performative agents represent the cumulative capabilities of information retrieval and advisory agents, we posit that in tasks with moderate specification ambiguity,

H2c: The use of performative agents will result in higher quality procurement choices than those made manually (i.e., higher procurement economy and accuracy).

H2d: The use of performative agents will result in higher quality procurement choices than those supported by either information retrieval or advisory agents (i.e., higher procurement economy and accuracy).

Consider finally tasks incorporating high ambiguity in specifications. Processing such requests requires interpretation of the precise item sought and/or its intended use. Experienced buyers cope with such situations by using prior knowledge and domain experience to convert the specifications into less ambiguous form. They use then the revised specifications to create retrieval sets of relevant items (albeit constrained in size by limitations in memory and recall). For information retrieval agents, however, the same lack of precision in specifications can constitute a significant problem in deciding what to look for as well as where to look. Up to a point, ambiguous specifications that are repetitive in nature within a specialized domain can be codified into ontologies. Designers can then develop specialized agents that accommodate these ontologies in their rule bases (see O'Hare and O'Grady 2003). For example, unless stated otherwise, requests that specify simply "paper" could be codified to mean letter-sized paper for laser printers. Agents can also incorporate learning mechanisms wherein they observe repeated examples of ambiguous requests to draw appropriate inferences. However, in MRO procurement environments, there is too much plausible variance in the wording of procurement requests to expect agents to resolve such ambiguity on their own. Moreover, the design of learning and filtering agents remains at a nascent stage (March et al. 2000).

Agents also have difficulty in coping with broken leg cues, that is, specifications or events that are unexpected but can be extremely diagnostic when they do occur (Camerer and Johnson 1997; Meehl 1954). For example, a normally reliable supplier may have severe impending disruption in production and/or distribution. In such a case, an astute buyer may switch suppliers instantly or buy larger quantities in advance, even exceeding normal stock limits to buffer inventory. Given the potentially vast number and unexpected nature of broken leg cues, it is not reasonable to expect agents to cope well with them, nor to expect agent developers to anticipate them all during the design phase.

The implication of the above is that in high specification ambiguity tasks, retrieval sets constructed using information retrieval agents can contain items irrelevant to the intent of procurement request. This is analogous to what occurs in moderate ambiguity situations. However, unlike moderate ambiguity tasks, the imprecision of the request can also lead information retrieval agents to exclude items that should reasonably be included. Thus, the set is not only noisy; it is also incomplete (i.e., the intersection between items that should be included and those actually included is relatively small). The presence in the retrieval set (and by continuation, in the consideration set) of irrelevant items coupled with the paucity of relevant items places significant constraints on eventual choice. The irrelevant items increase the possibility of an incorrect choice. Even if the correct item is chosen eventually, the limited set of appropriate items reduces the possibility of finding the best price. Thus, in tasks with high specification ambiguity,

H3a: The use of information retrieval agents will result in lower quality procurement choices than those made manually (i.e., lower procurement economy and accuracy).

For high specification ambiguity items, advisory agents creating consideration sets can have difficulty in formulating appropriate rules for screening and applying them, especially when the intended use and goal trade-offs are not clear. The consequences can be three-fold. First, the consideration set created can include items spanning multiple categories, as in moderate ambiguity situations. Second, unlike moderate ambiguity situations, a lack of well-defined screening rules also implies that some of the items may be inappropriate to the context of the request. Finally, the agent is liable to exclude items that should reasonably have been included. In high ambiguity situations, these limitations of advisory agents would appear to outweigh their advantages (of substituting the decision maker's cognitive effort in narrowing the list and ordering the items). The consequence is the creation of lower quality consideration sets, leading to the likelihood of making inferior choices than those made by unassisted decision makers. Thus, in tasks with high specification ambiguity,

H3b: The use of advisory agents will result in lower quality procurement choices than those made manually (i.e., lower procurement economy and accuracy).

When performative agents engage their choice mechanisms on such sets, they are confronted with the problem of performing evaluations on lower-quality sets, with ill-defined criteria, and choosing across product categories. To the extent that the goal conflicts are not resolved at this stage, even the relative importance of multiple criteria can be uncertain. Therefore, performative agents are likely to produce lower quality choices than unassisted humans. Furthermore, in high specification ambiguity situations, performative agents will incur the cumulative disadvantages of information retrieval and advisory agents noted above. Thus, in tasks with high specification ambiguity,

H3c: The use of performative agents will result in lower quality procurement choices than those made manually (i.e., lower procurement economy and accuracy).

H3d: The use of performative agents will result in lower quality procurement choices than those supported by either information retrieval or advisory agents (i.e., lower procurement economy and accuracy).

The core intuition of the hypotheses can be summarized by envisaging a metaphorical fault line of cognitive capabilities. On one side of the line—in tasks with low to moderate specification ambiguity—we anticipate that the use of agents will result in positive outcomes compared to the unassisted individual. On the other side of the line—in high specification ambiguity situations—we anticipate that the unassisted decision maker will outperform agents.

## Research Method

In this section, we describe the task environment, experimental design, subjects, dependent variables, and experimental procedure.

## Task Environment

The task environment was constituted by the Intelligent Mall (Nissen 2001), a performative agent system developed for supply chain automation and support. Here we provide a brief overview of its composition, capabilities, and logic. For more information, Intelligent Mall architecture and mechanics are discussed in considerable detail elsewhere (e.g., Nissen 2001; Nissen and Mehra 1998). We also identify specific aspects of the Intelligent Mall task environment that are manipulated and controlled for experimentation. Table 4 summarizes the key capabilities.

The Intelligent Mall is a performative agent developed to automate and support many important process activities along the enterprise supply chain (e.g., procurement, order fulfillment, payment). To support such performative behavior, the Mall also has various information retrieval and advisory capabilities that can be turned discretely on and off in various combinations (e.g., information retrieval and/or advisory mode). As a performative application and an environment for effecting commercial transactions along the supply chain, the Mall relates most closely with the business market-spaces noted above (e.g., Chavez and Maes 1996; Fox and Barbuceanu 2003; Hu, Reeves, and Wong 1999; Hu, Yen, and Chung 1999; Preece et al. 1999). Each of these agent systems—including the Mall—has its relative strengths and weaknesses, and none claims to automate and support all activities along the entire supply chain. Our use of the Mall for experimentation is representative of software agent technology available to support procurement today.

As the name suggests, the Intelligent Mall employs a mall metaphor to characterize its virtual environment, in which (human) buyers and sellers can use small federations of autonomous, intelligent agents to represent them in commercial transactions. This multi-agent system supports two distinct classes of agents: seller agents (called “shops”) and buyer agents (called “shoppers”). From the user’s perspective, either a shop or shopper agent can be instantiated, depending on whether the principal is interested in selling or buying, respectively. In this experiment, we manipulated only the capabilities of shopper agents (i.e., supporting procurement activities). To minimize confounding and unplanned manipulation, we held constant the number and capabilities of shop agents across all experimental trials.

Figure 1 shows a screenshot of two shopper agents at the bottom of the screen and three shop agents toward the middle and top of the screen. Also shown is the price catalog for Shop 1, which lists items for sale by this virtual supplier along with corresponding prices. The other shop agents depicted in Figure 1 have their own comparable price catalogs (not shown). Price catalogs can be small and stored on a single computer, or they can be immense and span multiple networks. In this experiment, we included relatively small catalogs (e.g., listing 5 to 15 items for each shop agent) stored on a single computer. For the reasons noted above (i.e., to minimize confounding and unplanned manipulation), we held constant the catalog sizes and storage locations of shop agents across all experimental trials.

On the buyer side, the shopping list shown in Figure 2 provides an interface for the user of one shopper agent to specify the items to be purchased. The other shopper agents depicted in Figure 2 have their own comparable shopping lists (not shown). The user has a choice of typing the items to be purchased into the form, or the shopper agent can query the specialty agent Host to access a catalog of all items listed for sale in the Mall at that point in time. In this latter respect, the Host agent forms the universal set of items offered for sale in the Intelligent Mall.

<table><tr><td colspan="3">Table 4. Key Intelligent Mall Capabilities</td></tr><tr><td>Capability</td><td>Implication</td><td>Use in Experiment</td></tr><tr><td>Performative agent</td><td>Includes information retrieval and advisory capabilities also.</td><td>Turn discretely on and off the different capabilities to support different experimental conditions.</td></tr><tr><td>Shop and shopper agents interact virtually</td><td>Users can delegate both selling and buying activities to agents.</td><td>All shop agents kept the same for control.Shopper agents manipulated to form different experimental conditions.</td></tr><tr><td>Host agent</td><td>Maintains universal set of all items offered for sale in the Mall.</td><td>Host agent interacts directly with information retrieval agents. No human action is required when agent support is turned on. Human user without agent support cannot interact directly with the Host and must consult paper catalogs instead.</td></tr><tr><td>Information retrieval agent</td><td>Contacts host agent to access universal set. Contacts shop agents to form retrieval set. Uses domain-specific ontology to support symbolic matching.</td><td>No human action is required when agent support is turned on. Human user without agent support must consult a paper catalog and write down onto paper forms product descriptions to be included in retrieval set.</td></tr><tr><td>Advisory agent</td><td>Analyzes quotations from shop agents.Forms consideration set as subset of retrieval set. Recommends product and source using heuristic rules and analytical methods.</td><td>No human action is required when agent support is turned on. Human user without agent support must analyze and compare manually product information listed on paper forms.</td></tr><tr><td>Performative agent</td><td>Uses recommendations from advisory agents to select the preferred product and source for each item on shopping list.Can complete purchase order and execute binding commercial transaction.</td><td>No human action is required when agent support is turned on. Human user without agent support must choose product manually by comparing information on papers forms. Purchase order forms completed manually by all subjects in the experiment, whether performative agents are used or not.</td></tr></table>

In the case of the particular shopping list depicted in Figure 2, one can see the user requires one “LATITUDE,” one “WIN98,” two “123456s,” three “987654s,” and four “MACs.” The items listed represent an assortment of product models, part numbers, and brand names specified through shop agents and registered with the Host. As above, we held constant the manner in which product catalog information was represented across all experimental trials. When the user finishes making entries through this interface, s/he instructs the agents to “start shopping” by clicking on the corresponding action button shown in the figure.

Behaviorally, shopper agents exhibit capabilities of each class of agent discussed above (i.e., information retrieval, advisory, and performative). Such implemented behaviors parallel our theoretical discussion above and also provide the basis for experimental manipulation described below. The agent takes as input a set of purchase items and quantities from its user. This constitutes the purchase specification. The shopper agent in information retrieval mode then sends requests for quotations (RFQs) to the various shops registered in the Mall in order to form the retrieval set. Shopper agents rely principally upon symbolic matching (e.g., including keyword search) to form the retrieval set. A domain-specific ontology of MRO procurement items supports some inferential capability to take action when keywords and other search symbols cannot be matched exactly. When the information retrieval capability of the Mall is turned on, no action is required of the human user to perform this task. When such capability is disabled, the human user must search manually through the paper catalog and write down onto paper forms product descriptions for all items to be included in the retrieval set.

Paralleling our theoretical structure, the shopper agent in advisory mode analyzes quotations from shop agents, forms the consideration set, and includes a recommended product (i.e., specific item description) and source (i.e., a specific vendor shop and price) for each item on the shopping list. Shopper agents have access to many heuristic rules and analytical methods that support such analysis. At this point in Mall development, procurement rules are encoded through methods at the class level for agents in a particular organization or enterprise. Such rules are inherited by all instances of agents in each class. A list of the specific procurement rules used in the experiment is shown in Appendix A. When the Mall's advisory capability is turned on, no action is required of the human user to perform this task. When such capability is disabled, the human user must analyze and compare manually product information listed on paper forms.

![](/api/attachments/F45SR9AG/fulltext/images/11318a14ea750a66aa925c0d72e466512096ba28e3d943ca0f7756588b3e5c72.jpg)  
Figure 1. Intelligent Mall Screenshot: Shop Dialog

![](/api/attachments/F45SR9AG/fulltext/images/89037f0a7d71e15b1ed956a0892ddef1f1cc8ed6104bb6ceb9836165ef25aee7.jpg)  
Figure 2. Intelligent Mall Screenshot: Shopper Dialog

<table><tr><td colspan="3">Table 5. Role of Agent and Subject in Between-Subjects Conditions</td></tr><tr><td>Experimental Condition</td><td>Role of Agent</td><td>Role of Subject</td></tr><tr><td>No support</td><td>No steps</td><td>Steps 1, 2, and 3; complete PO</td></tr><tr><td>Information Retrieval</td><td>Step 1 (conduct market analysis and form retrieval set)</td><td>Steps 2 and 3 (form consideration set and make choice); complete PO</td></tr><tr><td>Advisory</td><td>Step 2 (form consideration set from retrieval set supplied by decision maker) and provide recommendation for step 3</td><td>Step 1 (conduct market analysis and form retrieval set) and step 3 (make choice from agent recommendations); complete PO</td></tr><tr><td>Performative</td><td>Steps 1, 2, and 3</td><td>Complete PO</td></tr></table>

The agent in performative mode selects in turn the preferred source for each item to make a choice. As above, this parallels our theoretical structure as well. The choice is made based on the output of advisory mode. That is, the agent selects whichever sources are recommended in the steps above. When the performative capability of the Mall is turned on, no action is required of the human user to perform this task. When such capability is disabled, the human user must decide manually (e.g., comparing information on paper forms from the consideration set).

## Experimental Design

The experimental design had between-subjects and within-subjects conditions. The four between-subjects conditions were constituted by the type of agent support provided to subjects: (1) no support, (2) information retrieval support, (3) advisory support, and (4) performative support. These conditions correspond to the agent classification scheme and the tiered view of decision making articulated earlier. Paralleling our theoretical discussion, the within-subjects conditions manipulated specification ambiguity at three levels: (1) low, (2) moderate, and (3) high. Operationalization of these levels corresponds to the specification ambiguity factors discussed above.

## Between-Subjects Conditions

In the between-subjects conditions, we manipulated agent support for different phases of the tiered decision sequence. Table 5 summarizes these conditions and maps the respective roles of the software agent and human subject in terms of the multiple-stage decision sequence. In the no support condition, the Intelligent Mall software agents played no role. Here the human subjects were required to perform all procurement tasks: Step 1—access universal sets via paper catalogs; form retrieval sets by matching products listed in paper catalogs to items on shopping lists; Step 2—form consideration sets by analyzing and comparing alternate products and vendor sources included in retrieval sets; recommend a specific product and preferred vendor source for each item on the shopping list; Step 3—make and execute the choice decision. In every experimental condition other than this one, Mall agents played some role in performing the procurement tasks.

In the information retrieval condition, Intelligent Mall shopper agents provided autonomous support for constructing the retrieval set. Subjects in experimental conditions that included agent-based information retrieval support were required to use the Mall to support this step. Subjects assigned to conditions that excluded such agent support were required instead to form retrieval sets manually as described above. In the advisory condition, Mall agents provided support for creating the consideration set and made product or vendor recommendations for choice. Subjects in experimental conditions that included agent-based advisory support were required to use the Mall for this step, whereas those assigned to the no support and information retrieval conditions were required instead to form consideration sets and to make recommendations manually as described above. The performative support condition was a composite of the information retrieval and advisory conditions, plus the responsibility for suggesting a choice (i.e., the performative level of support can be thought of as the combination of information retrieval support + advisory support + choice decision). Subjects in experimental conditions that included agent-based performative support were required to accept the Mall's product or vendor choices. Subjects assigned to other conditions were required instead to accomplish this choice step manually as described above. Once a choice was made (in all four experimental conditions), the human subject completed a paper purchase order (PO) form to document the purchase decision.

## Within-Subjects Conditions

We operationalized specification ambiguity by manipulating purchase-item specificity. The items used in the procurement task are shown in Table 2. The intent was for most subjects to have at least surface-level familiarity with all items on the list. Further, in accordance with Table 3, the items in the low ambiguity condition contain enough information to identify the product (or even part number); the formation of retrieval and consideration sets entails keyword matches. The items in the moderate ambiguity condition contain enough specificity to identify product type, but not the specific product; keyword searches yield only partial success. For example, to purchase a shake, one would still need to know the flavor. The high ambiguity items denote product classes. The specifications (e.g., for a cola) need conversion before keyword matches can even be attempted. For example, nothing called “cola” is offered for sale in the Mall. All subjects were required to purchase the same, 12 items listed in the table. The order in which they were to be bought was randomized, so each subject had a different sequence. The objective of randomization was to minimize between-subjects variation from task order.

## Subjects

Our experimental sample of 84 subjects was drawn from a pool of mid-level managers enrolled in a full-time graduate education program at a U.S. university. Subjects participated in the experiment as part of their graduate school class work. To motivate task performance, course grades for the experiment were calibrated to each subject's performance in his/her experimental condition, and prizes (e.g., lunch at a local restaurant) were offered to the top three performers.

The average age of subjects was 33.3 years (range: 26 to 48), and they had an average of 12.2 years' work experience after graduating from college (range: 0 to 25). Of this, several years were spent on supply chains (average: 3.7 years; range: 0 to 15). Thus, our experiment sample was constituted by mature, educated subjects, the type of mid-career professionals often responsible for procurement work in supply chains (Nissen 1997). Moreover, the subjects' supply chain experience reflects direct familiarity with the types of purchasing tasks and procurement task environment employed in this experiment. These factors serve to enhance the external validity and generalizability of the study. Further, the variability of experience evident across the range of subjects summarized above can also imply variability of performance; hence the analysis below considers this through inclusion of supply chain experience as a covariate.

## Dependent Variables

As introduced above, performance was measured through two variables: procurement economy and accuracy of purchase decisions. To measure procurement economy, we computed the best price available for each item and normalized the price paid by subjects as a percentage deviation from the best price. $^{4}$ To measure procurement accuracy, for each item, we determined which vendor's product should have been selected (e.g., based on the item satisfying user requirements best). Subjects scored one point for an accurate purchase or zero points for an inaccurate purchase. Because each subject procured 12 items, scores on accuracy could range from 0 (no correct choices) to 12 (all choices made correctly).

## Experimental Procedure

We conducted first a pilot study with six test subjects, all of whom had previous supply chain experience. The purpose of the pilot was to ensure that the software worked as intended and that subjects understood the instructions. We also used feedback from test subjects to assess the range of task ambiguity reflected in the experiment. Such feedback was useful further to gauge the relative performance of people and software agents when purchasing items reflecting various levels of task ambiguity and types of agent support (i.e., checking our experimental manipulations). The six subjects were tested sequentially. Comments from each test were used to refine the experiment for the next.

Feedback from these pilot tests was helpful to refine instructions for the experiment. It indicated that the range of specification ambiguity was sufficient to explore performance at the human–software agent frontier. Informal checks also suggested that pilot subjects' interpretation of specification ambiguity was similar to the authors' and was consistent with the intended manipulations of the experiment. For instance, pilot-test subjects described noticeable distinctions between purchase items in each of the three specification ambiguity classes described above. They indicated also that procurement tasks became progressively more difficult as the level of specification ambiguity increased. Data collected during the pilot study were not used in the analyses of results reported below.

The main experiment was conducted in three stages: a lecture, followed by a practice session, and the experimental session itself. The lecture addressed the topic of intelligent supply chain agents. Subjects were shown a demonstration of the Intelligent Mall, and key supply chain activities, relationships, and exchanges were described. After the lecture, each subject participated in a practice session with a training example. The purpose of the experiment was explained, the instructions were clarified, and subjects were asked to perform each of the steps required to purchase a representative test item, just as they would do during the experiment. Subjects were encouraged to ask questions and to indicate any unclear requirements, confusing items, or problems experienced during the training example.

For the experiment itself, each subject was given a personalized set of experimental materials. The materials contained instructions for the experiment—the items to be bought, the order in which they were to be bought (each subject was given a different sequence of items), the purchasing procedure, and six procurement rules (see Appendix A)—in addition to all forms and other information (e.g., product catalogs, Intelligent Mall interface instructions) needed to complete the experimental tasks.

To reiterate from above, subjects in experimental conditions that included one or more types of agent support (i.e., information retrieval, advisory, performative) were instructed to use the Intelligent Mall where appropriate (e.g., to solicit vendor quotations, to make product or vendor recommendations, to execute choice decisions). Subjects in experimental conditions that excluded one or more types of agent support (i.e., no support, information retrieval, advisory) were instructed to use the paper catalogs and forms. In all experimental conditions, the purchasing procedure was consistent with numerous models from the literature that have been developed to describe business-to-business procurement such as this (see Gebauer et al. 1998; Nissen 1997). This serves to enhance the realism and generality of the experimental tasks and the task environment—and hence the external validity and generalizability of the results.

## Analysis and Results

Of the 84 participants, one subject in the performative support condition did not complete the assigned tasks (i.e., submitted blank purchase order forms) and had to be dropped from the analysis. The analysis was thus conducted with 83 subjects. Table 6 shows the descriptive statistics on the subjects' performance in the 12 procurement tasks assigned to them. For statistical analyses, we created averages of performance data for purchase items within each level of task ambiguity (i.e., low, moderate, high).

Box's M test shows that the data satisfy the criteria of normality and homoskedasticity. In order to accommodate variability in the subjects' supply chain experiences, the data were analyzed through a multivariate analysis of covariance model, using such experience as a covariate. Tests showed that for each of the dependent variables, the regression slopes across the experimental conditions were homogeneous. This establishes the suitability of the data for using analysis of covariance models (Stevens 1992, p. 334). Finally, because one subject was dropped from the analysis, the experimental cell sizes were unequal. We used the general linear models procedure in SAS (SAS/STAT Guide 1987). Table 7 summarizes the multivariate (MANCOVA) and univariate (ANCOVA) results of the experiment. The results are discussed in detail below.

## Multivariate Analysis of Covariance

A MANCOVA was conducted with economy and accuracy as dependent variables. We found significant main effects for the type of agent support $(F(6, 470) = 14.31; p < 0.01)$ and task ambiguity $(F(4, 470) = 37.06; p < 0.001)$ , as well as for the covariate supply chain experience $(F(2, 235) = 5.01; p < 0.01)$ . The interaction effect for support\*task was significant also $(F(12, 470) = 8.39; p < 0.01)$ . The multivariate analysis shows that agents as well as the level of task ambiguity affect performance in procurement tasks. Also, the performance differentials among different types of support are contingent on the ambiguity of the task. Finally, experience represents an important covariate of supply chain task performance. We explore the specific effects in greater detail in the context of univariate analyses below.

Table 8 summarizes pairwise comparisons of experimental conditions in terms of significant performance differentials in the dependent variables, using the Bryant-Paulson posterior test (Kirk 1982, p. 736). For each dependent variable listed in the table, we separate performance comparisons into two categories: (1) no support versus agent support conditions, and (2) agent support conditions. The first corresponds to our hypotheses on how the performance of subjects with no agent support would compare to that of subjects using the three types of agents (i.e., no support versus information retrieval support; no support versus advisory support; no support versus performative support).

The second corresponds to our hypotheses on how subjects using different types of agents would perform relative to one another (i.e., information retrieval versus performative support; advisory versus performative support). Each of these performance comparisons is separated further into one of the three different experimental conditions pertaining to specification ambiguity (i.e., low, medium, high). The table summarizes also how results—for each dependent variable, for each ambiguity condition—support our experimental hypotheses. These summaries are discussed in greater detail below.

## Procurement Economy

Figure 3 shows the means $^{5}$ for procurement economy (i.e., percentage deviation from the best price) for the three levels of task ambiguity. For all experimental conditions, the economy attained in moderate ambiguity tasks decreased from corresponding levels in tasks with low-task ambiguity. Across all conditions, economy was considerably worse for high-ambiguity tasks.

<table><tr><td colspan="13">Table 6. Descriptive Statistics: Means (and Standard Deviations)</td></tr><tr><td rowspan="3">Type of Agent Support</td><td colspan="12">Task (Procurement Item)</td></tr><tr><td colspan="4">Low Ambiguity</td><td colspan="4">Moderate Ambiguity</td><td colspan="4">High Ambiguity</td></tr><tr><td>Latitude</td><td>Win98</td><td>123456: Office Desk</td><td>987654: Office Chair</td><td>Exec Desk</td><td>Exec Chair</td><td>Mac</td><td>Shake</td><td>Burger</td><td>Cola</td><td>PC</td><td>PC OS</td></tr><tr><td colspan="13">Dependent Variable: Economy</td></tr><tr><td>No support</td><td>25.20(3.499)</td><td>24.59(2.442)</td><td>22.17(2.278)</td><td>24.04(3.667)</td><td>28.08(3.667)</td><td>33.12(4.056)</td><td>24.70(2.529)</td><td>24.4(2.484)</td><td>41.64(3.499)</td><td>38.73(1.839)</td><td>58.12(3.134)</td><td>53.51(5.657)</td></tr><tr><td>Information Retrieval</td><td>13.01(3.667)</td><td>13.21(3.125)</td><td>9.29(2.759)</td><td>8.49(2.620)</td><td>18.28(2.491)</td><td>21.10(3.009)</td><td>17.10(2.923)</td><td>15.52(3.206)</td><td>42.99(2.548)</td><td>55.31(3.566)</td><td>68.21(2.952)</td><td>65.49(4.829)</td></tr><tr><td>Advisory</td><td>11.84(3.163)</td><td>11.19(2.818)</td><td>7.26(3.373)</td><td>5.71(2.373)</td><td>17.64(3.341)</td><td>18.63(2.466)</td><td>11.32(2.952)</td><td>12.41(3.446)</td><td>63.07(1.550)</td><td>52.49(3.158)</td><td>78.15(3.388)</td><td>74.29(5.333)</td></tr><tr><td>Performative</td><td>6.62(3.523)</td><td>7.28(3.341)</td><td>5.28(2.675)</td><td>4.82(2.698)</td><td>8.16(3.185)</td><td>9.72(3.610)</td><td>7.39(2.414)</td><td>6.73(3.388)</td><td>74.26(1.891)</td><td>65.34(2.234)</td><td>88.12(3.446)</td><td>84.28(4.667)</td></tr><tr><td colspan="13">Dependent Variable: Accuracy</td></tr><tr><td>No support</td><td>0.85(0.060)</td><td>0.87(0.049)</td><td>0.91(0.035)</td><td>0.89(0.066)</td><td>0.82(0.071)</td><td>0.79(0.074)</td><td>0.85(0.047)</td><td>0.86(0.027)</td><td>0.79(0.025)</td><td>0.84(0.043)</td><td>0.74(0.023)</td><td>0.76(0.040)</td></tr><tr><td>Info. Retrieval</td><td>0.88(0.051)</td><td>0.89(0.088)</td><td>0.90(0.070)</td><td>0.93(0.048)</td><td>0.89(0.068)</td><td>0.874(0.061)</td><td>0.849(0.073)</td><td>0.827(0.025)</td><td>0.82(0.044)</td><td>0.792(0.037)</td><td>0.74(0.050)</td><td>0.69(0.050)</td></tr><tr><td>Advisory</td><td>0.94(0.031)</td><td>0.93(0.048)</td><td>0.95(0.029)</td><td>0.97(0.040)</td><td>0.836(0.085)</td><td>0.873(0.041)</td><td>0.931(0.050)</td><td>0.920(0.047)</td><td>0.77(0.051)</td><td>0.74(0.050)</td><td>0.68(0.073)</td><td>0.652(0.085)</td></tr><tr><td>Performative</td><td>0.99(0.047)</td><td>0.99(0.027)</td><td>0.98(0.057)</td><td>0.99(0.014)</td><td>0.92(0.066)</td><td>0.89(0.077)</td><td>0.96(0.057)</td><td>0.95(0.029)</td><td>0.69(0.067)</td><td>0.68(0.045)</td><td>0.63(0.059)</td><td>0.60(0.080)</td></tr></table>

<table><tr><td colspan="6">Table 7. Statistical Summary (F Value and Degrees of Freedom)</td></tr><tr><td colspan="2">Analysis</td><td>Agent Support</td><td>Task Ambiguity</td><td>Support × Task</td><td>Covariate (Experience)</td></tr><tr><td>Multivariate</td><td>MANCOVA</td><td>14.31**(6, 470)</td><td>37.06***(4, 470)</td><td>8.39**(12, 470)</td><td>5.01**(2, 235)</td></tr><tr><td>Univariate</td><td>Economy</td><td>7.02**(3, 236)</td><td>14.26***(2, 236)</td><td>10.36**(6, 236)</td><td>7.85**(1, 236)</td></tr><tr><td></td><td>Accuracy</td><td>5.32**(3, 236)</td><td>10.56***(2, 236)</td><td>5.39**(6, 236)</td><td>3.15*(1, 236)</td></tr></table>

\* significant at 0.05    \*\*significant at 0.01    \*\*\*significant at 0.001

<table><tr><td colspan="5">Table 8. Pairwise Comparisons of Significant Agent Performance Effects</td></tr><tr><td rowspan="2" colspan="2">Dependent Variable</td><td colspan="3">Task Ambiguity</td></tr><tr><td>Low</td><td>Moderate</td><td>High</td></tr><tr><td rowspan="3">Economy</td><td>No support vs. agent support conditions</td><td>NS &lt; IR; NS &lt; A; NS &lt; P</td><td>NS &lt; IR; NS &lt; A; NS &lt; P</td><td>NS &gt; IR; NS &gt; A; NS &gt; P</td></tr><tr><td>Agent support conditions</td><td>None</td><td>P &gt; IR; P &gt; A</td><td>A &lt; IR; P &lt; IR; P &lt; A</td></tr><tr><td>Support for hypotheses</td><td>+H1a-c; -H1d</td><td>+H2a-d</td><td>+H3a-d</td></tr><tr><td rowspan="3">Accuracy</td><td>No support vs. agent support conditions</td><td>NS &lt; A; NS &lt; P</td><td>NS &lt; A; NS &lt; P</td><td>NS &gt; A; NS &gt; P</td></tr><tr><td>Agent support conditions</td><td>P &gt; IR; P &gt; A</td><td>P &gt; IR; P &gt; A</td><td>P &lt; IR; P &lt; A</td></tr><tr><td>Support for hypotheses</td><td>+H1b-d; -H1a</td><td>+H2b-d; -H2a</td><td>+H3b-d; -H3a</td></tr></table>

NS = No support; IR = information retrieval support; A = advisory support; P = performative support.  
The comparisons > and < indicate significantly better or worse performance at p < 0.05.

![](/api/attachments/F45SR9AG/fulltext/images/c9f14c2d7748af8296e79fa2ee5f272e86d93ed0fa5b4682dc69e451b5eb8ed7.jpg)  
Figure 3. Economy Versus Task Ambiguity

![](/api/attachments/F45SR9AG/fulltext/images/d131a2172c1e09d21111efa9ae068114f7c6a8a844bab32ee018bcce76c37a08.jpg)

Referring also to the procurement economy rows in Table 8, notice that all types of agent support improved performance significantly over the no support condition for tasks with low ambiguity, thus providing support for hypotheses H1a, b, and c. This occurred for moderate ambiguity tasks as well, supporting H2a, b, and c. For high ambiguity tasks, all types of agent support produced significantly inferior results than the no support condition. This supports the predictions of H3a, b, and c.

In comparing means across agent-supported conditions, we find from Table 8 that they were not significantly different for low ambiguity tasks. There is, thus, no support for H1d in terms of economy. For moderate ambiguity tasks, the performative condition had a significantly better mean than did either the information retrieval or advisory condition. This supports the prediction of H2d. For high ambiguity tasks, the mean for the performative condition was significantly worse than either the information retrieval or advisory condition, thus providing support for H3d.

## Procurement Accuracy

Figure 4 shows how subjects performed with regard to procurement accuracy. For all conditions, the accuracy attained in the moderate ambiguity tasks decreased from corresponding levels in low-ambiguity tasks. Across all conditions, accuracy was considerably worse for high-ambiguity tasks.

Referring to the procurement accuracy rows in Table 8, notice that for low ambiguity tasks, advisory and performative (but not information retrieval) agent support improved performance significantly over the no support condition. The results provide support for H1b and c, but not H1a. Except for the information retrieval condition, performance gains were also significant for moderate ambiguity tasks, thus supporting H2b and c (but not H2a). For high ambiguity tasks, agent-supported performance (apart from the information retrieval condition) was significantly worse than that of the no support condition. Hypotheses H3b and c are supported, but not H3a.

Referring now to differences across agent-supported conditions, we find from Table 8 that in low ambiguity tasks, the performative condition returned significantly higher accuracy than did either the information retrieval or advisory condition. This confirms the prediction of H1d. A very similar trend was observed for moderate ambiguity tasks, thus supporting H2d. For high ambiguity tasks, the performative condition performed significantly worse than did either the information retrieval or advisory condition, thereby supporting H3d.

## Summary of Results

The analyses point to three specific findings. First, performance in procurement tasks is dependent upon the type of agent support. Indeed, the mere presence of software agent support affected task performance significantly. The effect of the type of agent support was also significant; hence not all software agents can be expected to have equivalent performance impacts on the procurement process. Second, the study also provides evidence that benefits from such support are bounded sharply by the extent of specification ambiguity. A core result of the study can be characterized as a discontinuity in decision quality that occurs when different levels of specification ambiguity interact with different types of agent support. Finally, the level of supply chain experience represents a positive contributor to procurement task performance. However, experience alone is insufficient to overcome performance degradation stemming from high levels of specification ambiguity.

<table><tr><td>Table 9. Noteworthy Conclusions</td></tr><tr><td>1. IT shifts from role of decision support to decision maker.2. Agent support and specification ambiguity create performance inversions.3. Agents create the need for human decision assistants.4. Software and human roles may shift dynamically.5. Address ambiguity at agent run time versus design time.</td></tr></table>

## Discussion and Conclusion

Intelligent software agents have the potential for effecting sharp improvements in performance in domains such as procurement. They also hold much promise for enabling management and decision making in modes not supported previously by IT. And they are pushing the person-system boundary of computer-based decision support. The impact of such technologies on decision making in organizational contexts has not been reported previously in the IS literature.

The stream of research associated with this article contributes to the literature by investigating the capabilities, limitations, and boundaries of agent technology for computer-based decision support in the procurement domain. By investigating the comparative performance of human and software agents across varying levels of specification ambiguity in the procurement domain, the experimentation described in this article helps to elucidate some new boundaries of computer-based decision making quite broadly. We seek in particular to learn from this domain and to help inform computer-based decision making, agent technological design, and IS research more generally. The five noteworthy conclusions summarized in Table 9 follow.

## IT Shifts from Role of Decision Support to Decision Maker

We learn through this study how software agents can be developed to exhibit qualitatively different and progressively subsuming capabilities (e.g., information retrieval, advisory, performative) in terms of supporting and automating the kinds of knowledge and information work performed historically by people. As agents are delegated correspondingly progressive autonomy in the organization, the roles of people in processes such as procurement diminish accordingly. In the extreme case of performative software agents, people are needed for just a peripheral role. Here the role of IT shifts from computer-based decision support to computer-based decision maker.

## Agent Support and Specification Ambiguity Create Performance Inversions

Our study shows that specification ambiguity exerts complex, nonlinear effects on procurement performance in an agent-supported task environment. The interaction of ambiguity and agent support creates a discontinuity (i.e., performance inversion) in processes that utilize both human and software agents for decision making. In the context of procurement, the results imply that conditions of low and moderate ambiguity warrant agent support, but in conditions of high ambiguity, procurement tasks should be performed manually. From here, finer gradations of specification ambiguity need to be defined and operationalized, so they can be gauged across different kinds of tasks and task environments.

## Agents Create the Need for Human Decision Assistants

With autonomous software agents capable of making decisions at runtime without people in the loop, the influence, judgment, and experience of human decision makers must be integrated through some process other than decision making itself (especially agent design). Traditionally, where people with organizational responsibilities faced simple, repetitious or low-risk decisions, for example, they would rely upon their cognitive capabilities for decision analysis and choice. Computer-based decision aids would be employed where decisions became particularly complex, novel, or risky. Here we suggest something of a role reversal between human and software agents. Where software agents with organizational responsibilities face simple, repetitious, or low-risk decisions, for example, they may rely upon their processing capabilities for decision analysis and choice. Symmetrically, human decision assistants can be employed where decisions become particularly complex, novel, or risky. This suggests a new line of research to study the reversal of human and computer roles in decision-support task environments.

## Software and Human Roles Shift Dynamically

Where computer-based decision aids and computer-based decision makers operate in environments of unknown or variable ambiguity, the complementary roles of people and machines remain indeterminate and may have to shift dynamically from one step in a process to another. For instance, the concept role may itself have to shift from a static to a dynamic one. This suggests that an important aspect in computer-based decision making will center on how to recognize when human and machine roles need to switch. Perhaps agents can be redesigned to recognize better the edges of their knowledge bases and to find a knowledgeable person to ask for assistance. Notwithstanding advancing work in artificial intelligence that has addressed meta-knowledge for some time (e.g., rules about rules to help control inference in expert systems), however, at this point implementing meta-cognition through the design of software agents remains a research agenda that is restricted to the most-advanced technologists' laboratories.

## Address Ambiguity at Agent Run Time Versus Design Time

To some extent the sophistication of agents can be increased by integrating more-complete supply chain ontologies and specialized product knowledge (see Fox and Barbuceanu 2003), by expanding inference beyond simple symbolic matching (e.g., predicate calculus, Bayesian networks), and by incorporating other, more-advanced design approaches. But so long as an agent's environment remains dynamic, no static ontology can ever hope to remain complete over time.

Unsupervised agent learning appears to represent a promising approach to handling ambiguity (see Shavlik and Dietterich 1990). Here the software developer is not designing in—at design time—how to address ambiguity autonomously. Rather, s/he is designing in how to learn—at run time—how to address ambiguity autonomously. This is more like growing software agents than building them. Indeed, information technologists may find traditional terms such as specify, design, and build giving way to a novel set including create, grow, and coach. Little of our extensive IS literature is able to shed much light on growing software agents, however. This study points to an emerging new direction for research on computer-based decision making.

## References

Alba, J., and Hutchinson, W. “Dimensions of Consumer Expertise,” Journal of Consumer Research 13 (1987), pp. 411-454.

Bakos, Y. “The Emerging Role of Electronic Marketplaces on the Internet,” Communications of the ACM (41:8), 1998, pp. 35-42.

Boy, G. A. “Software Agents for Cooperative Learning,” in Software Agents, J. Bradshaw (ed.), AAAI Press, Menlo Park, CA, 1997.

Bui, T. “Intelligent Negotiation Agents for Supporting Internet-Based Competitive Procurement,” Working Paper, Department of Information Sciences, Naval Postgraduate School, 1996.

Burke, R. D., Hammond, K. J., and Young, B. C. “The FindMe Approach to Assisted Browsing,” IEEE Expert (12:4), July/August 1997, pp. 32-40.

Camerer, C., and Johnson, E. “The Process-Performance Paradox in Expert Judgment: How Can Experts Know So Much and Predict So Badly?” in Research on Judgment and Decision Making: Currents, Connections, and Controversies, W. Goldstein and R. Hogarth (eds.), Cambridge University Press, Cambridge, UK, 1997, pp. 342-364.

Camerer, C., and Weber, M. “Recent Developments in Modeling Preferences: Uncertainty and Ambiguity,” Journal of Risk and Uncertainty (5:4), 1992, pp. 325-370.

Chavez, A., and Maes, P. “Kasbah: An Agent Marketplace for Buying and Selling Goods,” in Proceedings of the First International Conference on the Practical Application of Intelligent Agents and Multi-Agent Technology, London, April 1996.

Chen, R. S., Chen, C. C., and Lin, H. M. "Design an Agent-Based Framework for Processes Collaboration in Electronic Marketplace," International Journal of Computer Applications in Technology (16:4), 2003, pp. 154-166.

Chen, H., Chung, Y. M., Ramsey, M., and Yang, C. C. “A Smart Itsy Bitsy Spider for the Web,” Journal of the American Society for Information Science and Technology (49:7), 1998, pp. 604-618.

Clemons, E. K., and Row, M. C. “Sustaining IT Advantage: The Role of Structural Differences,” MIS Quarterly (15:3), 1991, pp. 275-292.

Collins, J., Youngdahl, B., Jamison, S., Mobasher, B., and Gini, M. "A Market Architecture for Multi-Agent Contracting," in Proceedings of the Second International Conference on Autonomous Agents, K. Sycara and M. Wooldridge (eds.), Minneapolis, MN, 1998, pp. 285-292.

Creyer, E., Bettman, J., and Payne, J. “The Impact of Accuracy and Effort Feedback on Adaptive Decision Behavior,” Journal of Behavioral Decision Making (3:1), 1990, pp. 1-16.

Desai, K., and Hoyer, W. “Descriptive Characteristics of Memory-Based Consideration Sets: Influence of Usage Occasion Frequency and Usage Location Familiarity,” Journal of Consumer Research (27:3), 2000, pp. 309-323

Einhorn, H., and Hogarth, R. “Ambiguity and Uncertainty in Probabilistic Inference,” Psychological Review (92:4), 1985, pp. 433-461.

Ellsberg, D. “Risk, Ambiguity and Savage Axioms,” Quarterly Journal of Economics (75), 1961, pp. 643-669.

Etzioni, O., and Weld, D. S. “Intelligent Agents on the Internet: Fact, Fiction, and Forecast,” IEEE Expert (10:4), August 1995, pp. 44-49.

Fox, M., and Barbuceanu, M. “The Integrated Supply Chain Management Project,” Enterprise Integration Laboratory, Department of Industrial Engineering, University of Toronto, 2003 (available online at http://www.eil.utoronto.ca/iscm-descr.html).

Franklin, S., and Graesser, A. “Is It an Agent or Just a Program? A Taxonomy for Autonomous Agents,” in Proceedings of the Third International Workshop on Agent Theories, Architectures, and Languages, Springer-Verlag, New York, 1996.

Frisch, D., and Baron, J. “Ambiguity and Rationality,” Journal of Behavioral Decision Making (1), 1988, pp. 149-157.

Gebauer, J., Beam, C., and Segev, A. “Impact of the Internet on Procurement,” Acquisition Review Quarterly, Special Issue on Managing Radical Change (5:2), 1998, pp. 167-184.

Gensch, D. “A Two-Stage Disaggregate Attribute Choice Model,” Marketing Science (6), 1987, pp. 223-239.

Gini, M., and Boddy, M. “Workshop on Agent-Based Manufacturing,” conducted at the Autonomous Agents ’98 Conference, Minneapolis, MN, 1998.

Glover, S., Prawitt, D., Spilker, B. “The Influence of Decision Aids on User Behavior: Implications for Knowledge Acquisition and Inappropriate Reliance,” Organizational Behavior and Human Decision Processes (72:2), 1997, pp. 232-255.

Goodhue, D., and Thompson, R. “Task-Technology Fit and Individual Performance,” MIS Quarterly (19:2), 1995, pp. 213-236.

Hammond, K., and Summers, D. “Cognitive Control,” Psychological Review (79:1), 1972, 58-67.

Hauser, J. R., and Wernerfelt, B. “An Evaluation Cost Model of Consideration Sets,” Journal of Consumer Research (16:4), 1990, pp. 393-408.

Heath, C., and Tversky, A. “Preference and Belief: Ambiguity and Competence in Choice Under Uncertainty,” Journal of Risk and Uncertainty (4), 1991, pp. 5-28.

Hess, C., and Kemerer, C. “Computerized Loan Origination Systems: An Industry Case Study of Electronic Markets Hypothesis,” MIS Quarterly (18:3), 1994, pp. 251-276.

Hoch, S. and Ha, Y. “Consumer Learning: Advertising and the Ambiguity of Product Experience,” Journal of Consumer Research (13:2), 1986, pp. 221-233.

Hu, J., Reeves, D., and Wong, H. S. “Agent Service for Online Auctions,” in Proceedings of the Workshop on AI for Electronic Commerce, T. Finin and B. Grosof (eds.), American Association for Artificial Intelligence, Orlando, FL, July 1999.

Hu, J., Yen, J., and Chung, A. “A Virtual Property Agency: Electronic Market with Support of Negotiation,” in Proceedings of the Workshop on AI for Electronic Commerce, T. Finin and B. Grosof (eds.), American Association for Artificial Intelligence, Orlando, FL, July 1999.

Huber, J., and Klein, N. “Adapting Cutoffs to the Choice Environment: The Effects of Attribute Correlation and Reliability,” Journal of Consumer Research (18:3), 1991, pp. 346-357.

Jennings, N. R., Sycara, K., and Wooldridge, M. “A Roadmap of Agent Research and Development,” Autonomous Agents and Multi-Agent Systems (1:1), 1998, pp. 7-38.

Johnston, H. R., and Carrico, S. R. “Developing Capabilities to Use Information Strategically,” MIS Quarterly (12:1), 1988, pp. 37-47.

Kardes, F., Kalyanaram, G., Chandrasekaran, M., and Dornoff, R. "Brand Retrieval, Consideration Set Composition, Consumer Choice, and the Pioneering Advantage," Journal of Consumer Research (20:1), 1993, pp. 62-75.

Kasturi, R. "E-Procurement: Ariba! Ariba!" Intelligent Enterprise, May 15, 2000 (available online at http://www.intelligenterp.com).

Kimbrough, S. O., Wu, D. J., and Zhong, F. “Computers Play the Beer Game: Can Artificial Agents Manage Supply Chains?,” Decision Support Systems (33:3), 2002, pp. 323-333.

Kirk, R. Experimental Design: Procedures for the Behavioral Sciences ( $2^{nd}$ ed.), Brooks-Cole Publishing, Pacific Grove, CA, 1982.

Knowles, A. “InterAp Assigns Intelligent Agents to the Web,” PC Week, June 12, 1995, p. 42.

Kruwich, D. An Agent of Change, Andersen Consulting Center for Strategic Technology Research, 1996.

Kumar, K., and van Dissel, H. G. “Sustainable Collaboration: Managing Conflict and Cooperation in Interorganizational Systems,” MIS Quarterly (20:3), 1996, pp. 279-301.

Lee, H. L., and Billington, C. “The Evolution of Supply Chain Management Models and Practice at Hewlett-Packard,” Interfaces (25:5), 1995, pp. 42-63.

Levin, I., Huneke, M., and Jasper, J. “Information Processing at Successive Stages of Decision Making: Need for Cognition and Inclusion-Exclusion Effects,” Organizational Behavior and Human Decision Processes (82:2), 2000, pp. 171-193.

Lowe, D., Reckers, P., and Whitecotton, S. “The Effects of Decision-Aid Use and Reliability on Jurors’ Evaluations of Auditor Liability,” Accounting Review (77:1), 2002, pp. 185-202.

Mabert, V. A., and Venkataramanan, M. A. “Special Research Focus on Supply Chain Linkages: Challenges for Design and Management in the 21 $^{st}$ Century,” Decision Sciences (29:3), Summer 1998, pp. 537-552.

Maes, P. “Pattie Maes on Software Agents: Humanizing the Global Computer,” Internet Computing (1:4), July-August 1997, pp. 10-19.

March, S., Hevner, A., and Ram, S. “Research Commentary: An Agenda for Information Technology Research in Heterogeneous and Distributed Environments,” Information Systems Research (11:4), 2000, pp. 327-341.

Maturana, F. P., and Norrie, D. H. “Distributed Decision Making Using the Contract Net Within a Mediator Architecture,” Decision Support Systems (20:1), 1997, pp. 53-64.

Meehl, P. Clinical Versus Statistical Prediction: A Theoretical Analysis and a Review of the Evidence, University of Minnesota Press, Minneapolis, MN, 1954.

Mehra, A., and Nissen, M. “Case Study: Intelligent Software Supply Chain Agents Using ADE,” in Proceedings of the Workshop on Software Tools for Developing Agents, J. Baxter and B. Logan (eds.), American Association for Artificial Intelligence, Madison, WI, 1998, pp. 53-62.

Monczka, R. M. Petersen, K. J., Handfield, R. B., and Ragatz, G. L. "Success Factors in Strategic Supplier Alliances: The Buying Company Perspective," Decision Sciences (29:3), Summer 1998, pp. 553-577.

Mukhopadhyay, T., Kekre, S., and Kalathur, S. “Business Value of Information Technology: A Study of Electronic Data Interchange,” MIS Quarterly (19:2), 1995, pp. 137-156.

Mullen, T., and Wellman, M. P. “Market-Based Negotiation for Digital Library Services,” in Proceedings of the Second USENIX Workshop on Electronic Commerce, Oakland, CA, November 1996.

Muthukrishnan, A. V. “Decision Ambiguity and Incumbent Brand Advantage,” Journal of Consumer Research (22:1), 1995, pp. 98-109.

Nedungadi, P. “Recall and Consumer Consideration Sets: Influencing Choice Without Altering Brand Evaluations” Journal of Consumer Research (17:3), 1990, pp. 263-276.

Nissen, M. E. “Agent-Based Supply Chain Disintermediation vs. Re-intermediation: Economic and Technological Perspectives,” International Journal of Intelligent Systems in Accounting, Finance & Management (9:4), 2000, pp. 237-256.

Nissen, M. E. “Agent-Based Supply Chain Integration,” Journal of Information Technology & Management, Special Issue, Electronic Commerce in Procurement and the Supply Chain (2:3), 2001, pp. 289-312.

Nissen, M. E. “The Commerce Model for Electronic Redesign,” Journal of Internet Purchasing WWW, July 1997 (available online at http://www.arraydev.com/commerce/JIP/9702-01.htm).

Nissen, M. E., and Mehra, A. “Redesigning Software Procurement through Intelligent Agents,” in Proceedings of the Workshop on Using AI for Knowledge Management and Business Process Reengineering, American Association for Artificial Intelligence, Madison, WI, 1998, pp. 1-10..

O'Hare, G., and O'Grady, M. "Gulliver's Genie: A Multi-Agent System for Ubiquitous and Intelligent Content Delivery," Computer Communications (26:11), 2003, pp. 1177-1187.

Payne, J., Bettman, J., and Johnson, E. The Adaptive Decision Maker, Cambridge University Press, New York, 1993.

Preece, A., Hui, K., and Gray, P. “KRAFT: Supporting Virtual Organizations through Knowledge Fusion,” in Proceedings of the Worksohp on AI for Electronic Commerce, T. Finin and B. Grosof (eds.), American Association for Artificial Intelligence, Orlando, FL, July 1999.

Ratneshwar, S., Pechmann, C., and Shocker, A. “Goal-Derived Categories and the Antecedents of Across-Category Consideration,” Journal of Consumer Research (23:3), 1996, pp. 240-250.

Redmond, W. H. “The Potential Impact of Artificial Shopping Agents in e-Commerce Markets,” Journal of Interactive Marketing (16:1), 2002, pp. 56-66.

Roberts, J., and Lattin, J. “Consideration: Review of Research and Prospects for Future Insights,” Journal of Marketing Research (34:3), 1997, pp. 406-410.

Roberts, J., and Lattin, J. “Development and Testing of a Model of Consideration Set Composition,” Journal of Marketing Research (28:4), 1991, pp. 429-440.

Rodriguez-Aguilar, J. A., Martin, F. J., Noriega, P., Garcia, P., and Sierra, C. “Competitive Scenarios for Heterogeneous Trading Agents,” in Proceedings of the Second International Conference on Autonomous Agents, K. Sycara and M. Wooldridge (eds.), Minneapolis, MN, 1998, pp. 293-300.

SAS/STAT Guide for Personal Computers, Version 6, SAS, Cary, NC, 1987.

Sen, S. “Developing an Automated Distributed Meeting Scheduler,” IEEE Expert (12:4), July/August 1997, pp. 41-45.

Shavlik, J. W., and Dietterich, T. G. Readings in Machine Learning, Morgan-Kauffman, San Mateo, CA, 1990.

Shocker, A., Ben-Akiva, M., Boccaro, B., and Nedungadi, P. "Consideration Set Influences on Consumer Decision Making and Choice: Issues, Models and Suggestions," Marketing Letters (2:3), 1991, pp. 181-197.

Stevens, J. Applied Multivariate Statistics for the Social Sciences, Lawrence Erlbaum Associates, Mahwah, NJ, 1992.

Swaminathan, J. M., Smith, S. F., and Sadeh, N. M. “Modeling Supply Chain Dynamics: A Multiagent Approach,” Decision Sciences (29:3), Summer 1998, pp. 607-632.

Todd, P., and Benbasat, I. “Evaluating the Impact of DSS, Cognitive Effort, and Incentives on Strategy Selection,” Information Systems Research (10:4), 1999, pp. 356-374.

Todd, P., and Benbasat, I. “The Influence of DSS on Choice Strategies: An Experimental Analysis of the Role of Cognitive Effort,” Organizational Behavior and Human Decision Processes (60:1), 1994, pp. 36-74.

Todd, P., and Benbasat, I. “The Use of Information in Decision Making: An Experimental Investigation of the Impact of Computer-Based Decision Aids,” MIS Quarterly (16:3), 1992, pp. 373-393.

Wallace, D. J. “She’s Only Code and Pixels, But She Can Help You Shop,” New York Times, September 20, 2000, p. H-8.

West, P. “Predicting Preferences: An Examination of Agent Learning,” Journal of Consumer Research (23:1), 1996, pp. 68-80.

Wood, R. “Task Complexity: Definition of the Construct,” Organizational Behavior and Human Decision Processes (37:1), 1986, pp. 60-82.

Wright, A., and Lynch, J. “Communication Effects of Advertising Versus Direct Experience when Both Search and Experience Attributes are Present,” Journal of Consumer Research (21:4), 1995, pp. 708-718.

Wurman, P. R., Wellman, M. P., and Walsh, W. E. “The Michigan Internet AuctionBot: A Configurable Auction Server for Human

and Software Agents," in Proceedings of the Second International Conference on Autonomous Agents, K. Sycara and M. Wooldridge (eds.), Minneapolis, MN, 1998, pp. 301-308.

Zeng, D., Sheng, O., and Wilson, B. "The Design and Experimentation of Agent-Based Procurement Systems," in Proceedings of the Third International Conference on Telecommunications and Electronic Commerce, Dallas, TX, November 2000.

Zeng, D., and Sycara, K. “Cooperative Intelligent Software Agents,” Carnegie Mellon University Robotics Institute Technical Report No. CMU-RI-TR-95-14, March 1995.

## About the Authors

Mark Nissen is an associate professor of Information Science and Management at the Naval Postgraduate School. His research focuses on knowledge dynamics. He views work, organization, and technology as an integrated design problem, with recent research concentrating on the phenomenology of knowledge flows. Mark's publications span information systems, project management, knowledge management, organization studies, and related fields. In

2000, he received the Menneken Faculty Award for Excellence in Scientific Research, the top research award available to faculty at the Naval Postgraduate School. In 2001, he won a prestigious Young Investigator Award from the Office of Naval Research. In 2002–2003, he spent a sabbatical year in the Stanford Engineering School. Mark serves currently as Regional Editor (Americas) for the journal Knowledge Management Research & Practice. Before his information systems doctoral work at the University of Southern California, he acquired over a dozen years' management experience in the aerospace and electronics industry.

Kishore Sengupta is an associate professor of Information Systems at INSEAD in Fontainebleau, France. His research interests are in management and business value of information technology, software project management, and knowledge management. Prior to INSEAD, he was on the faculty at the Naval Postgraduate School, Monterey, California. Kishore was a visiting scholar at the Hong Kong University of Science and Technology in 1996-1997. He has also worked at the AT&T Network Software Center (now Lucent Technologies) and Ernst and Young. His published research appears in journals such as Management Science, MIS Quarterly, IEEE Transactions on Software Engineering, IEEE Transactions on Systems, Man, and Cybernetics, and IEEE Transactions on Engineering Management.

## Appendix A

## Procurement Rules

The following six procurement rules were presented for adherence in the experiment.

1. Specific procurement forms (e.g., Request for Quotation or RFQ, Purchase Order or PO) must be completed for each purchase. All instructions contained on each form must be followed.

2. Items must be purchased in the order received as part of the experiment.

3. An RFQ must be sent to every vendor that offers each particular item for sale.

4. The lowest-price item must be selected when multiple vendor products can satisfy the purchase requirement.

5. Specific enterprise procedures for conducting business with particular vendors apply (e.g., a unique contractual annotation must be made to POs).

6. Specific customs must be observed when conducting business with particular vendors (e.g., a unique manner of preparing POs).

Additionally, subjects were instructed to purchase the 12 purchase items listed above according to the procedure below.

1. Review purchase requirements.

2. Conduct market survey.

3. Send one RFQ to each vendor offering items for sale that can satisfy the requirement.

4. Analyze vendor quotations in response to RFQs.

5. Select the preferred source, based on quotations and procurement rules.

6. Issue one PO to each vendor selected in Step Five.
