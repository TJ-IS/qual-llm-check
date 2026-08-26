---
otero_id: 11580
otero_key: "KU8G676F"
title: "The Use of Cognitive Maps and Case-Based Reasoning for B2B Negotiation"
authors: "KUN-CHANG LEE; SOON-JAE KWON"
year: "2006"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222220412"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/KU8G676F/fulltext/images/8fa10702eaac0cf4e8a3abdb978a1c7aeaf4118534f441ab241ab32aa98b54e6.jpg)

## Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# The Use of Cognitive Maps and Case-Based Reasoning for B2B Negotiation

KUN-CHANG LEE <sup>a</sup> & SOON-JAE KWON <sup>a</sup>

<sup>a</sup> Sungkyunkwan University, Seoul, Korea Published online: 08 Dec 2014.

To cite this article: KUN-CHANG LEE & SOON-JAE KWON (2006) The Use of Cognitive Maps and Case-Based Reasoning for B2B Negotiation, Journal of Management Information Systems, 22:4, 337-376

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222220412

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http:// www.tandfonline.com/page/terms-and-conditions

# The Use of Cognitive Maps and Case-Based Reasoning for B2B Negotiation

KUN-CHANG LEE AND SOON-JAE KWON

KUN-CHANG LEE is a Professor of MIS and AIS at Sungkyunkwan University in Seoul, Korea. He received his Ph.D. in MIS from Korea Advanced Institute of Science and Technology (KAIST), an M.S. in MIS from KAIST, and a B.A. in Business Administration from Sungkyunkwan University. His recent research interests lie in cognitive map analysis of electronic commerce issues. He is currently developing several working papers specializing in multiagent cognitive map, knowledge management, and ubiquitous computing with applications to B2B and B2C problems. His research findings have been published in the Journal of Management Information Systems, Decision Support Systems, International Journal of Production Research, Expert Systems with Applications, Fuzzy Sets and Systems, Intelligent Systems in Accounting Finance and Management, Computers & Operations Research, Computers & Industrial Engineering, Simulation, Expert Systems, Computers in Human Behavior, among others.

SOON-JAE KWON is a Lecturer of MIS at Sungkyunkwan University in Seoul, Korea. He received his Ph.D. in MIS, an M.S. in Business Administration, and a B.A. in Accounting, all from Sungkyunkwan University. His research focuses on decision analysis in electronic commerce issues. He is currently preparing working papers about recommendation systems, social network analysis, and ubiquitous commerce. His research works have appeared in Journal of Management Information Systems and Expert Systems with Applications.

ABSTRACT: Conventional approaches to business-to-business (B2B) negotiation use primary negotiation terms (PNTs) such as price or order quantity for modeling and analysis, but pay little attention to such secondary negotiation terms (SNTs) as resource availability and corporate culture. This paper argues that SNTs also contribute to good negotiation decisions because PNTs and SNTs are closely interlinked in the form of causal relationships. Moreover, B2B negotiation demands a practical and useful framework that can reuse past negotiation knowledge and perform “what-if” analysis. This paper proposes a framework that consists of formalization, reuse, and problem-solving phases. The framework first formalizes TAKBN (tacit knowledge about B2B negotiation) with both PNTs and SNTs using a cognitive map and casebased reasoning, then stores them in case bases as cases that can be retrieved for later use and problem solving. This framework provides a platform with which decision makers can study past B2B negotiation cases, apply them to current B2B negotiation problems, and simulate different negotiation situations before making decisions. The framework has been tested using two practical scenarios. A structured, 13-item questionnaire was rigorously developed and applied to evaluate the validity of the proposed framework based on 16 B2B negotiation experts’ judgments. Statistical tests proved that the proposed framework could improve decision performance significantly in B2B negotiations.

KEY WORDS AND PHRASES: B2B negotiation, case-based reasoning, causal relationship, cognitive map, primary negotiation terms, secondary negotiation terms, tacit knowledge.

AS THE PHRASE DIGITAL ECONOMY SUGGESTS [77], the Internet era has opened up immense electronic commerce opportunities for many companies [5]. However, the advance of Internet technology also has profound implications for both consumers [33, 61] and businesses [36]. As the Internet has been used more and more widely by modern firms in order to gain competitive advantages, business-to-business (B2B) electronic commerce has emerged as one of the more viable alternatives for achieving these advantages [31]. Although negotiation support is highly important to the ultimate success of B2B negotiation, the subject has not been adequately dealt with in the current information systems literature [82].

Kersten [39] defines negotiation as a process of social interaction and communication about distribution and redistribution of power, resources, and commitments. It involves two or more people or firms who make decisions and engage in an exchange of information in order to determine a compromise. Each participant is an independent decision maker, but the different parties are interdependent because none can achieve its goals unilaterally. While some common issues of B2B negotiation (including logrolling [12], a priori agreement [74], and imprecise information [47]) have been addressed in the literature, no study has addressed the issue of harmonizing two kinds of negotiation terms—primary negotiation terms (PNTs) and secondary negotiation terms (SNTs). In traditional B2B negotiation, a final deal is reached after many rounds of information exchange among the involved firms. The information being exchanged usually refers to common trading terms (PNTs) such as price, order quantity, payment conditions, delivery time, refunds, and discount rate. However, other terms (SNTs) such as resource availability, cooperation of labor unions, CEO leadership style, bargaining power with vendors, and corporate culture, which are useful reference information for B2B players, are not explicitly stated in the course of traditional B2B negotiation. It is generally believed that PNTs are the primary concerns of most B2B players, but SNTs contain essential supporting information about the deal(s) being negotiated.

This paper argues that B2B players should also consider SNTs and investigate their influences on the final agreement from collective viewpoints. Although SNTs in B2B negotiation have not been dealt with explicitly in previous studies, it is clear that they have a significant impact on the final deal, which is traditionally composed of a set of PNTs. A systematic framework is proposed here that models and analyzes causal relationships among PNTs and SNTs, and highlights their influences on B2B negotiation.

The basic premise of this study is that PNTs and SNTs are closely interlinked in the form of causal relationships because changes in a given SNT may cause corresponding changes in a given PNT or multiple PNTs, and vice versa. With this awareness of the causal relationship between PNTs and SNTs in mind, we propose to model and analyze B2B negotiations using a cognitive map (CM) and case-based reasoning (CBR). The CM can illustrate causal relationships among the factors describing a given object or problem, and it can also describe experts’ tacit knowledge about a certain object [19, 57]. In most companies, B2B negotiation history is generally stored in a separate case base in which the appropriate attributes, values, and causality coefficients are assigned to each B2B negotiation case. Because CBR provides an embedded means of finding similar cases that can be compared to a new negotiation case, decision makers can select those that are most appropriate and refer to the corresponding CM using the appropriate causality coefficients. The proposed framework consists of the following three phases:

1. formalization: apply a CM to formalize tacit knowledge about B2B negotiation and store it into a case base;

2. reuse: use the CBR approach to reuse B2B negotiation-related tacit knowledge; and

3. problem solving: solve a new case of B2B negotiation by retrieving an appropriate similar CM from the case base (application of CBR) and drawing inferences.

## Background

## B2B Negotiation

AFTER THE BURST OF THE BUSINESS-TO-CUSTOMER (B2C) bubble in the late 1990s, the B2B sector has emerged as one of the electronic markets on which the major impact of electronic commerce is expected. BusinessWeek has published several articles discussing issues relating to the shift of electronic markets to B2B since 1998 [13]. It is usual in B2B transactions that its size in terms of quantity and money is relatively larger in comparison with B2C, causing the process of negotiation to become an essential part in B2B transactions. In this regard, business negotiations were modeled as a form suitable for electronic commerce [41], and the Web-based negotiation support system was proposed based on this modeling [40]. B2B negotiation requires more relaxed and realistic assumptions. In line with this need, some artificial intelligence (AI) models have proven to help the negotiation players locate an approximate solution strategy according to bounded rationality principles by utilizing heuristic search, heuristic evaluation, and learning techniques [66]. Sycara [75] proposed a more enriched negotiation model by integrating AI planning, CBR, and other decision-theoretic techniques. A multiagent negotiation framework has been extensively developed by several researchers [4, 70, 71]. In the context of several settings, distributed AI models based on multiagents have been suggested for more robust and effective negotiation models [28, 56].

Walton and McKersie [80] proposed classification of negotiations into the integrative and distributive types. Distributive negotiation predicts that one party can increase its own value only at the other party’s expense. Through a process of offer and counteroffer exchanges, the parties compete to gain as much value as possible [32]. In contrast, integrative negotiation is based on the premise that solutions can be found during the negotiation process, which reconcile the parties’ interests [59]. The two types of negotiations represent two extremes of a spectrum of mixed negotiations involving a significant element of conflict and a considerable potential for cooperation [80]. Mixed negotiations are more common; negotiators commit themselves to firm positions (distributive attitude), yet explore options (integrative), make threats (distributive), and yet trust the other negotiator (integrative) [27]. In order to build systems capable of conducting or supporting mixed negotiations, one needs to understand the requirements for the two extreme types. B2B negotiation discussed in this paper is also related to the mixed type of negotiations because a company engaged in B2B negotiation may want to keep its position (distributive) but update it in accordance with some information, such as counteroffer or environment (integrative).

## Cognitive Maps for Formalizing Tacit Knowledge About B2B Negotiation

B2B negotiation requires tacit knowledge since it deals with not only objective and rational PNTs but also subjective and firm-specific SNTs. Therefore, to successfully accomplish our research premise, we propose tacit knowledge about B2B negotiation (abbreviated as TAKBN) to handle tacit knowledge in B2B negotiation. Tacit knowledge is personal knowledge embedded in individual experience and is shared and exchanged through direct, face-to-face contact [19]. Tacit knowledge can be communicated in a direct and effective way. Typically, tacit knowledge is usually scattered across management activities and is hard to represent and store in an explicit form. This paper proposes to use a CM to define and formalize TAKBN for reuse. Tacit knowledge is often elicited by means of figurative language and symbolism to express the inexpressible [63]. Using CMs is well known as a highly promising technique for capturing tacit knowledge [52]. Lee and Courtney [50] have also suggested a CM as a means for constructing organizational memory and claimed that a CM is superior to common knowledge representation schemes such as rule and frame. Therefore, CMs can be used effectively for making tacit knowledge such as TAKBN explicable.

CMs have been found especially useful in solving unstructured problems dealing with many variables and their causal relationships [22, 23, 44, 57, 85, 87]. For example, CM was an effective problem-solving technique in the field of administrative sciences [23], where many decision variables and uncontrollable variables are causally interrelated with each other [22]. CMs have been used for distributed decision process modeling on the network [87], geographical information systems [55, 67, 68], the design of electronic commerce Web sites [49], knowledge management [62], bosphorus crossing problems [78], wayfinding processes [11], decision analysis [86], business process redesign [48], complex war games [44], strategic planning problems [65, 81], and information retrieval [35]. The primary concern of a CM is to see whether the state of one element is perceived to have an influence on the state of the other. In addition, several researchers proved that CM is a technically and methodologically mature technique to solve a wide variety of unstructured decision problems [55, 64, 68, 83, 86, 87]. Therefore, a CM can represent experts’ beliefs and cognition about ill-structured social relationships [34]. A CM is composed of concept nodes (or nodes) of a target problem, signed directed arrows, and causality value between the nodes. Concept nodes represent concepts consisting of a given target problem, signed directed arrows, and causal relations between two concept nodes. Causality value means “+” and “–.” The causality coefficient can be fuzzified into a real value between –1 and +1 [42, 51]. Axelrod [3] stated that the simple CM with a causality coefficient “+” and “–” is sufficient for replicating human cognition, because decision makers typically do not use a more complicated set of relationships. We adopt this simple CM to show that our CM-driven approach can be used effectively for formalizing TAKBN in an organization. Figure 1 shows an example of a negotiation process where the buyer is a manufacturing company that purchases raw materials from suppliers via B2B negotiation to produce products. The CM in Figure 1, in which each node represents a certain negotiation term (whether PNT or SNT), depicts a part of an expert’s tacit knowledge to analyze a buyer’s B2B negotiation process.

## CBR for Knowledge Reuse and B2B Negotiation

As discussed in the B2B Negotiation section, this paper focuses on the mixed type of B2B negotiation. When a firm proceeds to purchase from a B2B site, a B2B negotiation will be initiated. The negotiation process always requires a form of tacit knowledge to interpret the meaning of counteroffers and to consider unanticipated or anticipated effects from accepting offers or generating offers. To accept an offer in the course of a B2B negotiation requires an integrative consideration of PNTs and SNTs, with an anticipation to improve performance.

This paper applies CBR for negotiation. We propose that a TAKBN can be stored into a case base so that it can be reused for future B2B negotiation cases. CBR is a problem-solving paradigm in the field of AI, in which previous similar situations are retrieved and used to resolve new problems. An important argument for CBR is that situations recur with regularity. It is likely that the decision made for one case is applicable to another similar case. CBR allows businesses to treat past cases as a corporate resource and reuse them in future decision making [45]. This motivated us to use CBR as a key method for storing and reusing TAKBN for other B2B negotiation cases. Applying CBR to B2B negotiation is rather unique. Wong et al. [84] utilized CBR for developing an automated negotiation engine for used car trading, considering only PNTs. CBR was also used in an electronic commerce task of selecting a product from a list of alternatives most appropriate for the customer’s demands [7, 16]. CBR was also integrated with collaborative filtering techniques to provide product personalization in an electronic shop [73]. The TAKBN is represented by a set of CMs. It can be retrieved and reused when similar B2B negotiation situations sharing similar characteristics take place. There are several advantages of using CBR for TAKBN.

![](/api/attachments/KU8G676F/fulltext/images/73b83add5a559a1b8eb9d9af709f0e839eb05f5669a4bd39f9d04c3d83f85b48.jpg)  
Figure 1. Buyer’s Cognitive Map

1. CBR allows B2B negotiators to quickly propose new offers without deriving them from scratch. This provides organizational memory-based intuition for a given B2B negotiation problem to avoid any inconsistent problem-solving process.

2. CBR provides a systematic mechanism for storing TAKBN as cases and reusing them according to the characteristics of B2B negotiation situations.

3. CBR alerts B2B negotiators to avoid repeating past mistakes because those mistakes are already captured in CBR.

4. CBR helps B2B negotiators to analyze the importance of features and issues of B2B negotiation, thus leading to better future deals.

## Methodology

THE NOVEL FRAMEWORK FOR MANAGING TAKBN that we propose consists of three phases—formalization, reuse, and problem solving. In the formalization phase, CMs that graphically show the relationships among multiple concept nodes and appropriate causality coefficients formalize TAKBN. On completing the formalization phase, TAKBN is stored into a case base with a frame as shown in Figure 2, where the CM depicted in Figure 1 is decomposed into a set of attributes and values representing concept nodes and the related causal relationships between them. The specifics will be discussed in the next subsection. The stored TAKBN is retrieved based on the characteristics of B2B negotiation. When decision makers are required to resolve B2B negotiation problems, TAKBN can be reused. To facilitate the reuse process of TAKBN, two newly proposed algorithms—retrieval and adaptation algorithms—are developed. The retrieval algorithm can choose the most appropriate TAKBN from the case base, while the adaptation algorithm allows TAKBN to be properly updated to the track changes of a B2B negotiation environment to ensure the quality of TAKBN. With these two algorithms, the reuse phase generates the most valuable TAKBN that best fits the B2B negotiation problem. The problem-solving phase intelligently solves a given B2B negotiation problem based on the results from the reuse phase. The proposed framework is presented in Figure 3. For details about how to prepare cases for the experiment, refer to Appendix A. The details of each phase will be addressed in the following subsections.

![](/api/attachments/KU8G676F/fulltext/images/f84159b61ef3f7b9d001ddc492bd83d3626e9b3c90a59c325a5d85fdcbea422a.jpg)  
Figure 2. Frame-Typed Representation of TAKBN

![](/api/attachments/KU8G676F/fulltext/images/4e83846230eab259ae0b4ff40900a8a4b1cd1dd741ef21e5e304c3acee373277.jpg)  
Figure 3. Proposed Framework

## Formalization Phase

In the formalization phase, TAKBN is formalized with the aid of a CM. TAKBN is created when a new B2B negotiation problem is handled by decision makers. Managing TAKBN is a problem for decision makers because they need to memorize TAKBN or document TAKBN in files, which are difficult to retrieve for future use. In the proposed framework, there is a formalized way of managing TAKBN. A CM is used to more explicitly formalize TAKBN, as it is simpler and more convenient to handle TAKBN in the form of a set of causal relationships.

In our framework, when multiple CMs are retrieved for a given B2B negotiation problem, those CMs will be integrated into a single CM representing a consensus CM for the given problem. The integration issue is addressed in the adaptation procedure of the reuse phase. The unified CM is represented in a frame-typed case and stored in a case base. Therefore, the frame-typed case includes all the information about the components of a CM and the corresponding specific situations.

Figure 2 shows an example of the frame representing TAKBN. As shown in Figure 2, each TAKBN consists of a frame name, situations, concept nodes, and causal relationships among the nodes. For example, TAKBN#1 indicates a frame name, IS-A “B2B negotiation with Company XYZ,” where IS-A is a reserved word denoting “is an instance of.” The frame named “TAKBN#1” has seven concept nodes used in the CM of Figure 1, such as Intention to Order, Favorableness of Payment Condition, and so on. The frame TAKBN#1 includes several reserved words, such as PART-

OF, PREDECESSORS, and SUCCESSORS, all of which have a straightforward interpretation.

Situations for each negotiation partner are also addressed in Table 1 to provide basic information about the identity of the negotiation partner and which economic and management conditions the negotiation partner is facing.

## Reuse Phase

The reuse phase is composed of two subphases—retrieval and integration. The retrieval subphase aims at searching for those TAKBNs represented in CMs relevant to the B2B negotiation problem under consideration. For this purpose, we propose two CBR parameters—fitting ratio and garbage ratio—to determine the degree of relevance of candidate TAKBNs. The retrieved and relevant candidate TAKBNs are then integrated into a unified one in the integration subphase. The integration subphase also determines core nodes, supplementary nodes, and appropriate causality coefficients.

## Retrieval Subphase

To reuse TAKBN stored in the case base in a form of CMs, we must retrieve appropriate CMs or cases from the case base based on a predefined retrieval procedure. As past studies revealed that a single CM is confined to representing a limited number of nodes relevant to a specific B2B negotiation problem, it is almost impossible that a single CM can handle several situations at a time [50]. Therefore, we propose to retrieve several candidate CMs (or TAKBNs) from the case base first and then integrate them into a unified, single CM. In line with this argument, the basic idea of our proposed retrieval procedure is, under the assumption that the case base is complete, to retrieve a few highly relevant and representative CMs to a specific B2B negotiation problem.

Two measures were developed for this purpose—fitting and garbage ratios [62]. First, a fitting ratio measures the degree of coverage of the cases stored in the case base. A particular B2B negotiation problem is usually described by situation information or a set of situation-specific factors. The more the situation information of the new B2B negotiation problem is covered by the case, the higher will be the value of the fitting ratio. Hence, the fitting ratio can determine the relevance of a case and the new B2B negotiation problem. On the other hand, the garbage ratio is used to measure the degree of dissimilarity between the new B2B negotiation problem and the case. The higher mismatch between the situation information of the new B2B negotiation problem and the case, the higher will be the garbage ratio. Therefore, a high garbage ratio indicates that the new B2B negotiation problem and the case are dissimilar. Therefore, the garbage ratio measures how much situation information of the cases does not match with that of the new B2B negotiation problem. The fitting ratio is used in a cumulative way—if the retrieved cases cannot provide sufficient information for explaining the characteristics of the new B2B negotiation problem, more cases will be selected depending on the fitting ratio value. The necessary condition for fully covering the new B2B negotiation problem is that all the situations of the new B2B negotiation problem can be explained by those retrieved cases. Details about how the fitting ratio and garbage ratio are used in the proposed CBR mechanism are addressed fully in Appendix B, using the example in Table 2 or the Retrieval Phase section for the sake of clarity.

Table 1. Situation Information for B2B Negotiation Problem Analysis

<table><tr><td></td><td>Factors</td><td>Values</td></tr><tr><td rowspan="8">Seller company&#x27;s firm characteristics</td><td>Size of corporation (SC)</td><td>Large (LG)/medium (MM)/small (SM)</td></tr><tr><td>Type of industry (TI)</td><td>Textile and wearing apparel (AP)/chemical and chemical product (CH)/metal (ML)/machinery (MA)/ electronic (EC)/transport equipment (TE)/construction (CO)Wholesale trade (WT)/communication (CT)Financial institution (FI)</td></tr><tr><td>Type of corporation (TC)</td><td>Public (PU)/nonpublic (NP)</td></tr><tr><td>Right of management (RM)</td><td>Family owned (FO)/nonfamily owned (NF)</td></tr><tr><td>Number of subsidiaries (NS)</td><td>Above average (AA)/below average (BA)</td></tr><tr><td>Major market (MM)</td><td>Domestic (DO)/overseas (OS)</td></tr><tr><td>Business strategy (BS)</td><td>Specialization (SP)/related diversification (RD)/unrelated diversification (UD)</td></tr><tr><td>Business experience (BE)</td><td>Long (LN)/medium (ME)/short (SH)</td></tr><tr><td rowspan="7">Buyer company&#x27;s environment characteristics</td><td>Domestic economy (DE)</td><td>Recession (RC)/prosperity (PR)</td></tr><tr><td>World economy (WE)</td><td>Recession (RC)/prosperity (PR)</td></tr><tr><td>Government&#x27;s policy for interest rate (PIR)</td><td>High (HG)/low (LO)</td></tr><tr><td>Exchange rate trend (ERT)</td><td>Stable (SB)/unstable (US)</td></tr><tr><td>OPEC policy (OP)</td><td>Increasing production (IP)/decreasing production (DP)</td></tr><tr><td>Labor union movement (LUM)</td><td>Radical (RA)/compliant (CP)</td></tr><tr><td>Competition strength (CS)</td><td>Strong (SG)/weak (WK)</td></tr></table>

<sub>ion</sub> <sub>Process</sub> <sub>of</sub> <sub>Candidate</sub> C<sup>ase</sup> <sup>Based</sup> <sup>on</sup> <sup>Fitting</sup> <sup>Ratio</sup> <sup>and</sup>

<table><tr><td>Iteration</td><td> $F_1$ </td><td> $F_2$ </td><td> $F_3$ </td><td> $F_4$ </td><td> $F_5$ </td><td> $F_6$ </td><td> $F_7$ ,</td><td>...,</td><td> $F_{15}$ </td><td> $R$ </td><td> $n(\bar{R})$ </td><td> $T$ </td><td> $G$ </td></tr><tr><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)</td><td>15</td><td> $\{S_1, S_2, S_3, S_4, S_5, S_6, S_7, ..., S_{15}\}$ </td><td></td></tr><tr><td>1</td><td>0.60</td><td>0.73</td><td>0.67</td><td>0.20</td><td>0.40</td><td>0.40</td><td>0.47,</td><td>...,</td><td>0.40</td><td>(1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1)</td><td>4</td><td> $\{S_1, S_3, S_4, S_5, S_6, S_7, ..., S_{15}\}$ </td><td> $G_2 = 0.27$ </td></tr><tr><td>2</td><td>0.75</td><td>—</td><td>0.75</td><td>0.25</td><td>0.75</td><td>0.50</td><td>0.50</td><td>...</td><td>0.50</td><td>(1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)</td><td>1</td><td> $\{S_1, S_4, S_5, S_6, S_7, ..., S_{15}\}$ </td><td> $G_1 = 0.40$  $G_3 = 0.33$  $G_5 = 0.60$ </td></tr><tr><td>3</td><td>1.0</td><td>—</td><td>—</td><td>1.0</td><td>1.0</td><td>0</td><td>0</td><td>...</td><td>0</td><td>(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)</td><td>0</td><td> $\{S_4, S_5, S_6, S_7, ..., S_{15}\}$ </td><td> $G_1 = 0.40$  $G_4 = 0.80$  $G_5 = 0.60$ </td></tr><tr><td colspan="14">Note: The boldface means a value corresponding to cases of CMs selected in each iteration, and the variables are defined in Appendix B.</td></tr></table>

## Integration Phase

Given a new B2B negotiation problem, suppose that candidate CMs (or TAKBNs) are retrieved with the use of the retrieval subphase. Often, multiple candidate CMs are retrieved with respect to a B2B negotiation problem. There is a need to integrate these candidate CMs into a single unified CM in order to solve the incumbent problem. Multiple and different CMs can be aggregated into a single consensus CM through systematic and sound theoretical steps as proven in the literature [9, 10, 19, 20, 21, 22, 23, 24, 25, 48, 85, 86, 87]. For this purpose, the terms core CM, super CM, and supplementary subdiagram are derived. A core CM is defined as a minimal CM intersecting the candidate CMs selected from the case base using both fitting and garbage ratios. A super CM is defined as a maximal CM that unites the candidate CMs. A supplementary subdiagram is the part of the CM that belongs to the super CM but does not belong to the core CM. In line with Smith [72], a core CM represents a common part of tacit knowledge or beliefs that the retrieved multiple CMs possess, whereas a super CM denotes maximal tacit knowledge or beliefs that unites all retrieved multiple CMs.

To integrate multiple candidate CMs into a single unified one, two procedures are needed—aggregation and modification. The aggregation procedure generates a super CM from the retrieved candidate cases and defines a core CM and a supplementary subdiagram. The modification procedure starts from a node in the supplementary subdiagram and its directly related nodes of the super CM. Based on the domainspecific knowledge and the characteristics of a given B2B negotiation problem, the decision maker decides on whether a supplementary node is necessary. Therefore, the integration phase can be formalized as follows.

## The Integration phase

Step0: Define the super CM, core CM, and supplementary subdiagram.

Step1: Select a supplementary node from the supplementary subdiagram. If there are too many supplementary nodes, choose one node arbitrarily.

Step2: Decide whether the decision maker accepts the node, considering the level of analysis, the availability of information, and the characteristics of given problems.

Step3: If the node is accepted, then the node and the arrows directly related with the core CM are added to the core CM and removed from the supplementary subdiagram. Otherwise, the node is removed from the supplementary subdiagram.

Step4: If another supplementary node exists, then go to Step 1. Otherwise, stop.

## Problem-Solving Phase

Figure 1 shows that if trust of the seller increases, the intention to order raw materials improves accordingly and that it, in turn, prompts production activities. However, trust of the seller positively influences the raw materials order quantity from that seller, and the increase of the order quantity will contribute to the lowering of the seller’s price. Thus, a CM can be used to investigate the causal chain of influence between related concept nodes or factors, thereby finally concluding what kind of results would be expected from an initial change in some factors [46, 57, 83]. The CM used in this paper has the following preconditions for the sake of making our logic work in a simpler, but clearer way:

• the input node always has positive values within an interval [0, 1];

• the causality value consists of –1, 0, and +1; and

• a 0.5 threshold value is used for driving the inference process to converge within a finite number of iterations [46, 83].

In the investigation of the ways of applying such characteristics of causal links in the decision-making process, we propose three possible ways of using a CM in decision making. The first way of using a CM is that irrelevant factors can be detected as those having no effect on the target decision outcome. By analyzing the connectivity between factors depicted in a CM, one can easily determine whether a particular factor is relevant to a given decision. Figure 4 shows an example with causal links between six factors. Suppose that one is concerned with the state of F because it will affect a target decision to be made. Figure 4 shows us that both A and D influence F directly, and C has an indirect influence on F through D. On the other hand, neither B nor E influences F indirectly or directly. Both B and E are therefore “irrelevant” in light of the outcome F. This example demonstrates that such a difficult decisionmaking problem can be simplified by means of a CM.

The second way of using a CM is to evaluate the performance of causal knowledge embedded in a CM regardless of its potential to produce the expected output. Assume that one finds that the value of F is relatively high, while the values of A and D are relatively low. The CM suggests, however, that a low A and low D would lead to a low F. Thus, one knows that this is not the expected case. The reason may be attributed to other unknown factors that might be affecting F in this particular situation. Also, some factors, which were not originally perceived to be relevant, may be influencing F. If so, then our effort should focus on identifying such factors implicitly affecting F so that the performance of causal knowledge represented by a CM does not seriously degrade under turbulent decision-making situations.

The third way of using a CM is to support a “what-if” analysis. As revealed in previous studies, CMs must be further improved to deal with uncertainty and vagueness regarding the decision environments so that they may be used as a knowledge engineering tool to extract causal knowledge from factors representing environments [76]. For this purpose, a CM is organized as a matrix, in which it contains some specific inputs (or stimulus vectors) and produces outputs (or consequence vectors). The “what-if” analysis can be easily performed on this matrix representation. The aim of the problem-solving phase in our framework is particularly centered on the third way of using a CM. With a final CM being produced, it is regarded as TAKBN and used in a simulation to induce the most promising negotiation offer. After a final

![](/api/attachments/KU8G676F/fulltext/images/18678ba65cb3132b3931fba35b480dbab5b72f9a1e5985037e4e659f9ba3d69f.jpg)  
Figure 4. Illustrative Cognitive Map

CM is organized through the retrieval phase, the decision maker may want to investigate the anticipated results from it. CMs allow experts to freely draw causal pictures of their problems. We view CMs as a dynamic system that settles down to specific stable states as time evolves. Therefore, the causal dynamic system represented by a CM responds to an external stimulus, and we take its equilibrium behavior as a forward-evolved inference. The proposed problem-solving phase is based on the forward-evolved inference by a CM. For details about the inference process, refer to Appendix C.

Another point worth discussing is that throughout the CM-based, forward-evolved inference process, possible interrelationships among PNTs and SNTs can be clarified systematically, showing the chain of causal influences among PNTs and SNTs, which is very difficult to identify. Therefore, the main contribution of this paper is to suggest using CMs as a vehicle for identifying causal interrelationships among PNTs and SNTs to induce a better negotiation deal. In this problem-solving phase, therefore, the final CM obtained in the retrieval phase is used for solving a new B2B negotiation problem. As a CM is viewed as a dynamic system that settles down to a specific stable state as time evolves, the dynamic system represented by a CM responds to an external stimulus, and we take its equilibrium behavior as a forward-evolved inference result. The detailed explanation about drawing inference using a CM has been presented in the literature [43]. As the CM used for solving a new B2B negotiation problem is stored in a case base, it is possible for organizations or decision makers to accumulate and update TAKBN.

## Experiment and Discussion

## B2B Negotiation Problem

A B2B NEGOTIATION PROBLEM OCCURS when an organization attempts to procure raw materials. The paper focuses on a scenario in which a manufacturing company (or buyer) tries to purchase raw materials from a seller using B2B negotiation. The B2B negotiation problem requires a great deal of know-how knowledge—mainly tacit knowledge. For instance, the procurement department of the buyer company has to make a procurement decision under the potential risk of high cost and poor quality. To avoid such a procurement risk, the buyer company must rely on their procurement know-how knowledge, which has been accumulated through experience. Valuable know-how knowledge in B2B negotiation achieves and maintains high-quality B2B negotiations by understanding the minds of the other B2B players and making appropriate counteroffers with the right timing.

However, such know-how knowledge is mainly tacit knowledge acquired only through experience over years. Accordingly, such tacit knowledge should be treated as a core invisible asset in B2B negotiation. Hence, such tacit knowledge or TAKBN is recommended to be formalized into CMs and stored into a case base as cases in order to be shared with other decision makers in the same company and reused for similar B2B negotiation problems. Then, decision makers in the same company can be more successful in B2B negotiation. Also, the TAKBN management framework becomes the contingency plan for the retirement or turnover of B2B negotiation specialists as well as training materials for new employees.

After interviewing five B2B experts from two famous B2B players in South Korea—KTNet (www.ktnet.com) and EC Plaza (www.ecplaza.net)—we identified a representative B2B negotiation problem as well as some key SNTs and PNTs necessary for analyzing the identified B2B negotiation problem. As shown in Table 1, the diverse situation information explaining a certain B2B negotiation problem is classified into two parts, including the seller company’s firm characteristics and the buyer company’s environment characteristics. A B2B negotiation requires two parties—a buyer and a seller. Table 3 shows situation information pertinent to a new B2B negotiation problem, as well as related cases stored in the case base.

In Table $3 , S _ { 1 } , S _ { 2 } , . . . . S _ { 1 5 }$ are situation frame sets of the cases stored in the case base. $S _ { 0 }$ denotes the situation of the new B2B negotiation problem. To understand the characteristics of the situation of the new B2B negotiation problem, let us first study the seller company’s characteristics by checking the company’s firm characteristics. In this new B2B negotiation problem or $S _ { 0 } ,$ the firm size of the possible seller company is large $\left( \mathrm { S C } = \mathrm { \ddot { \Omega } L G ^ { \prime \prime } } \right)$ with its industry type being electronic $( \mathrm { T I } = \mathrm { \mathrm { \Omega } } ^ {  } \mathrm { E C } ^ {  } )$ , having a large number of subsidiaries $( \mathrm { N S } = \mathrm { \ddot { \varepsilon } A A } ^ { \prime \prime } )$ and long business experience $\mathrm { ( B E = ^ { \circ } L N ^ { \circ } ) }$ . Therefore, it means that the buyer company is now trying to purchase electronic components from the possible seller to manufacture some products. The possible seller’s stock is listed in the stock exchange market $( \mathrm { T C } = \mathrm { \ddot { \Omega } P U ^ { \mit , \mit } } )$ with the governance structure being family owned $( \mathrm { R M } = \mathrm { \ddot { \prime } F O \vec { \ } } )$ . Its major market lies overseas $( \mathrm { M M } = \mathrm { \ddot { \Omega } O S ^ { \prime \prime } } )$ and the business strategy is to diversify into related areas $( \mathrm { B S } = \mathrm { \ " R D ^ { \prime \prime } } )$ . Second, we should investigate the environmental characteristics facing the buyer company. The current domestic economic situation it is experiencing is a recession $\mathrm { ( D E = ^ { \circ } R C ^ { \circ } ) }$ 4 whereas the world economy is enjoying prosperity $( \mathrm { W E } = ^ { \ast } \mathrm { P R } ^ { \prime \prime } )$ since the Organization of the Petroleum Exporting Countries (OPEC) is increasing oil production $\mathrm { ( O P = }$ $^ { \ast } \mathrm { I P ^ { \ast } } )$ . The government regulates the interest rate as low $( \mathrm { P I R } = \mathrm { \ " { L O } } ^ { \prime \prime } )$ and the ex-

<table><tr><td rowspan="2">Case</td><td colspan="15">Situations</td><td rowspan="2">Appropriate $CM_n$ </td></tr><tr><td>SC</td><td>TI</td><td>TC</td><td>RM</td><td>NS</td><td>MM</td><td>BS</td><td>BE</td><td>DE</td><td>WE</td><td>PIR</td><td>ERT</td><td>OP</td><td>LUM</td><td>CS</td></tr><tr><td> $S_0$ (new case)</td><td>LG</td><td>EC</td><td>PU</td><td>FO</td><td>AA</td><td>OS</td><td>RD</td><td>LN</td><td>RC</td><td>PR</td><td>LO</td><td>SB</td><td>IP</td><td>RA</td><td>SG</td><td>?*</td></tr><tr><td> $S_1$ </td><td>LG</td><td>MA</td><td>PU</td><td>FO</td><td>BA</td><td>DO</td><td>RD</td><td>ME</td><td>RC</td><td>RC</td><td>LO</td><td>SB</td><td>IP</td><td>CP</td><td>SG</td><td> $CM_1$ </td></tr><tr><td> $S_2$ </td><td>LG</td><td>EC</td><td>PU</td><td>NF</td><td>AA</td><td>OS</td><td>RD</td><td>ME</td><td>PR</td><td>PR</td><td>HG</td><td>SB</td><td>IP</td><td>RA</td><td>SG</td><td> $CM_2$ </td></tr><tr><td> $S_3$ </td><td>MM</td><td>MA</td><td>PU</td><td>NF</td><td>BA</td><td>OS</td><td>RD</td><td>LN</td><td>RC</td><td>PR</td><td>LO</td><td>SB</td><td>DP</td><td>RA</td><td>SG</td><td> $CM_3$ </td></tr><tr><td> $S_4$ </td><td>MM</td><td>FI</td><td>NP</td><td>FO</td><td>AA</td><td>DO</td><td>SP</td><td>SH</td><td>PR</td><td>RC</td><td>HG</td><td>US</td><td>DP</td><td>RA</td><td>WK</td><td> $CM_4$ </td></tr><tr><td> $S_5$ </td><td>MM</td><td>MA</td><td>PU</td><td>FO</td><td>BA</td><td>OS</td><td>UD</td><td>LN</td><td>RC</td><td>RC</td><td>HG</td><td>SB</td><td>DP</td><td>CP</td><td>WK</td><td> $CM_5$ </td></tr><tr><td> $S_6$ </td><td>SM</td><td>CO</td><td>NP</td><td>NF</td><td>AA</td><td>DO</td><td>SP</td><td>LN</td><td>PR</td><td>PR</td><td>LO</td><td>US</td><td>DP</td><td>RA</td><td>SG</td><td> $CM_6$ </td></tr><tr><td> $S_7$ </td><td>SM</td><td>MA</td><td>PU</td><td>NF</td><td>AA</td><td>OS</td><td>UD</td><td>SH</td><td>RC</td><td>PR</td><td>LO</td><td>US</td><td>IP</td><td>CP</td><td>WK</td><td> $CM_7$ </td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td> $S_{15}$ </td><td>SM</td><td>AP</td><td>NP</td><td>NF</td><td>BA</td><td>OS</td><td>UD</td><td>SH</td><td>RC</td><td>PR</td><td>LO</td><td>US</td><td>IP</td><td>CP</td><td>SG</td><td> $CM_{15}$ </td></tr><tr><td colspan="17">* ? indicates “to be determined.”</td></tr></table>

<sub>.</sub> <sub>Case</sub> <sub>Base</sub> <sub>for</sub> <sub>B2B</sub> N<sup>ego</sup>

![](/api/attachments/KU8G676F/fulltext/images/23a8c6d0262bfd23f06e8d5ce5b7f29318008363885c088d198a874d2d661aee.jpg)  
Figure 5. Candidate CM  
change rate as stable $( \mathrm { E R T } = ^ { \ast } \mathrm { S B } ^ { \prime \prime } )$ . Although the labor union is getting radical (LUM $= \mathrm { \^ { 6 } R A } ^ { \prime 3 } )$ , the buyer company’s competition strength is believed to be strong $( \mathbf { C } \mathbf { S } =$ $^ { 6 6 } \mathrm { S G } ^ { \prime 3 } )$ due to exogenous variables such as a prosperous world economy and low oil prices, and so on.

## Retrieval Phase

The process to select candidate CMs from the case base is illustrated in Table 2. In the first iteration, case $C M _ { 2 }$ is selected because the fitting ratio of the situation frame set $S _ { 2 }$ is the largest. S is, therefore, said to match with $S _ { 0 } ,$ although there are four mismatched situations. Therefore, the fitting ratio of $S _ { 2 }$ is 11/15 (= 0.73), and the garbage ratio is $4 / 1 5 \ ( = 0 . 2 7 )$ . We used the threshold value θ of 0.5 in this problem. In the second iteration, case $C M _ { 3 }$ is selected because the garbage ratio of the situation set $S _ { 3 }$ is the smallest among $S _ { 1 } , S _ { 3 } ,$ and $S _ { 5 } ,$ of which the fitting ratios are the same. In iteration 3, the situation frame that is not covered by $S _ { 2 }$ and $S _ { 3 }$ are covered by $S _ { 1 }$ , which has the smallest garbage ratio. All the situation information of the new B2B negotiation problem is covered by $S _ { 1 } , S _ { 2 } ,$ and $S _ { 3 }$ through this process. Therefore, three candidate CMs are retrieved from the case base using the situation information so far. Figure 5 illustrates a candidate $C M _ { 1 }$

![](/api/attachments/KU8G676F/fulltext/images/b2c7f8e8ff01f3e417082aa5eb0c3c5af330853f16afc6db669f87ce8c62e3fa.jpg)  
Figure 6. Core CM and Super CM

## Integration Phase

Figure 6 presents both the core CM and the super CM. The core CM is highlighted with a thicker line, and the super CM is drawn with a thinner line. The super CM consists of eight supplementary nodes. To adapt the super CM to the new B2B negotiation problem, we first selected a supplementary node “Labor Union’s Cooperation” arbitrarily. The decision maker in the buyer company must decide whether to accept the SNT node. Assume that the decision maker thinks that the SNT node is important in this B2B negotiation situation because the labor union’s cooperation is crucial to meeting a rather tight production schedule. Thus, arrows related to the node, “Labor Union’s Cooperation,” are also accepted. Thus, some supplementary nodes representing SNTs such as “Interest Rate,” “Labor Dispute,” “Wages,” and “Support to Subsidiary” are accepted, whereas other nodes such as “Inventory,” “Duration of Recession,” and “Oil Price” are rejected. Therefore, the final CM is generated as shown in Figure 7, which is believed to represent the characteristics of the new B2B negotiation problem.

## Problem-Solving Phase

With the final CM as depicted in Figure 7, we conclude that the new B2B negotiation problem can be described by cause–effect relationships between the four PNTs and 11 SNTs. To perform what-if analysis with the final CM, we organize Figure 7 into the adjacency matrix E as follows.

$$
\begin{array}{c c} \text {FP} & \left( \begin{array}{c c c c c c c c c c c c c c c} 0 & 0 & 1 & 0 & 1 & - 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & - 1 & 0 & 0 & 0 & - 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & - 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & - 1 & - 1 \\ W A & - 1 \\ L D & - 1 \\ C A \\ T B \\ I R \\ S S \\ B E \end{array} \right) \end{array}
$$

For the sake of brevity, we use acronyms to represent original names of nodes. The B2B negotiation problem was constructed based on the information from experts of the interviewing companies. Figure 7 shows a CM or TAKBN, which is used to describe how a group of PNTs and SNTs are interrelated and result in final negotiation terms. Our goal is to determine the combination of PNTs that will give the highest intention to order (IO). Moreover, the effects created by SNTs are also considered. The PNTs shown in Figure 7 are OQ, SP, FP, and TD. We now elaborate on the detailed negotiation terms for each PNT so that we can describe the problem-solving phase more practically.

![](/api/attachments/KU8G676F/fulltext/images/6f3758f428332e5251eb1ef381324e4520c8f9f61e816ff1e91e097e288d2fb8.jpg)  
Figure 7. Final CM for Given B2B Negotiation

Table 4 shows the PNTs, OQ, SP, FP, and TD, and their corresponding node values that the buyer company thinks reasonable and practical for B2B negotiation.<sup>1</sup> The node values of SP indicate that the buyer company will be more satisfied when the seller’s prices per unit are lower. However, the node value of OQ is different from SP’s. From the viewpoint of the buyer company, OQ = 3,000 units is preferable because quality control and process control are at a manageable level. Therefore, the node value of OQ at 3,000 units is 0.6, which is the greatest among the three. The greatest node value of TD is 0.8. It occurs when the delivery date is set to three days after order placement because it is tightest compared to the other delivery dates. Table 4 also shows that the buyer company favors a payment term of 50 percent cash and 50 percent credit card payment on delivery, as the corresponding node value of 0.8 is the greatest among the three. Although many scenarios can be derived from the data in Tables 4 and 5, two typical scenes were chosen for illustrative purpose.

<table><tr><td colspan="8">Table 4. PNTs and Their Node Values (Buyer Company)</td></tr><tr><td>Seller&#x27;s price (SP)</td><td>Node value</td><td>Order quantity (OQ)</td><td>Node value</td><td>Tightness of delivery date (TD)</td><td>Node value</td><td>Favorableness of payment condition (FP)</td><td>Node value</td></tr><tr><td>$30 per unit</td><td>0.9</td><td>1,000 units</td><td>0.2</td><td>Three days after order placement</td><td>0.8</td><td>Full payment by cash on delivery</td><td>0.3</td></tr><tr><td>$40 per unit</td><td>0.8</td><td>3,000 units</td><td>0.6</td><td>Seven days after order placement</td><td>0.5</td><td>50 percent cash and 50 percent credit card payment on delivery</td><td>0.8</td></tr><tr><td>$50 per unit</td><td>0.2</td><td>5,000 units</td><td>0.3</td><td>Fifteen days after order placement</td><td>0.2</td><td>80 percent cash and 20 percent credit card payment on delivery</td><td>0.5</td></tr></table>

Scenario 1

Given

PNTs: SP = \$30 per unit (0.9), OQ = 1,000 units (0.2), TD = three days after order placement (0.8), FP = full payment by cash on delivery (0.3)

$$
\text { SNTs:   } \mathrm{LU} = \text { good   (0.7) }, \mathrm{IR} = \text { increase   (0.3) }, \mathrm{PR} = \text { increase   (0.8) }.
$$

We start our discussion with PNTs. The buyer company is cornered by a delayed production schedule, so that it needs raw materials to be delivered as quickly as possible (TD = three days after order placement). Also, the order quantity is rather small (OQ = 1,000 units). The buyer company may be confident in its negotiation power, so the seller’s price is set to \$30 per unit. The seller company, however, is demanding full payment by cash on delivery. Under this circumstance, the buyer company needs to compute the intention to place the order. If the result is higher than the given threshold, then the buyer will go ahead with the order. Otherwise, the order will not be placed. Considering the SNTs, the labor union’s cooperation is good $( \mathrm { L U } = 0 . 7 )$ and the interest rate is low $( \mathrm { I R } = 0 . 3 )$ . However, production activity is very active (PR = 0.8). Considering this circumstance, the first concept vector $\pmb { C } _ { 1 } = ( 0 . 3 , 0 . 8 , 0 . 2 , 0 . 9 , 0 ,$ $0 , 0 . 8 , 0 . 7 , 0 , 0 , 0 , 0 , 0 . 3 , 0 , 0 )$ is created. We perform the CM-based reasoning process as follows: the first concept vector $C _ { 1 }$ is adjusted based on the information of Scenario 1. Applying a 0.5 threshold for a convergence check [46], we computed the following reasoning processes to ensure that convergence can happen within a finite number of iterations. The CM-reasoning result is labeled as “inference,” and the values inside the bracket can be either 0 or 1. The value will be 1 when the result is greater than the threshold, otherwise, it will be 0. Inference 1 refers to the result after the first iteration, while inferences 2 and 3 are generated after the second and third iterations.

<table><tr><td></td><td></td><td>FP</td><td>TD</td><td>OQ</td><td>SP</td><td>IO</td><td>CF</td><td>PR</td><td>LU</td><td>WA</td><td>LD</td><td>CA</td><td>TB</td><td>IR</td><td>SS</td><td>BE</td></tr><tr><td> $C_1$ </td><td>=</td><td>(0.3</td><td>0.8</td><td>0.2</td><td>0.9</td><td>0</td><td>0</td><td>0.8</td><td>0.7</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.3</td><td>0</td><td>0)</td></tr><tr><td> $C_1 \times E$ </td><td>=</td><td>(0.8</td><td>0</td><td>-1</td><td>0.8</td><td>0.5</td><td>0.5</td><td>-0.2</td><td>0</td><td>0</td><td>0</td><td>0.4</td><td>0</td><td>0</td><td>0</td><td>0)</td></tr><tr><td>→</td><td></td><td>(1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0) inference 1</td></tr><tr><td> $C_2$ </td><td>=</td><td>(0.3</td><td>0.8</td><td>0.2</td><td>0.9</td><td>1</td><td>1</td><td>0.8</td><td>0.7</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.3</td><td>0</td><td>0)</td></tr><tr><td> $C_2 \times E$ </td><td>=</td><td>(0.8</td><td>0</td><td>0.1</td><td>0.8</td><td>1.5</td><td>0.5</td><td>0.8</td><td>0</td><td>0</td><td>0</td><td>0.4</td><td>-1</td><td>0</td><td>0</td><td>0)</td></tr><tr><td>→</td><td></td><td>(1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0) inference 2</td></tr><tr><td> $C_3$ </td><td>=</td><td>(0.3</td><td>0.8</td><td>0.2</td><td>0.9</td><td>1</td><td>1</td><td>0.8</td><td>0.7</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.3</td><td>0</td><td>0)</td></tr><tr><td> $C_3 \times E$ </td><td>=</td><td>(0.8</td><td>0</td><td>0.1</td><td>0.8</td><td>1.5</td><td>0.5</td><td>0.8</td><td>0</td><td>0</td><td>0</td><td>0.4</td><td>-1</td><td>0</td><td>0</td><td>0) inference 3</td></tr><tr><td>→</td><td></td><td>(1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0)</td></tr></table>

The equilibrium state is reached when two consecutive inference results are identical. In this scenario, the equilibrium state occurs after two iterations (as can be seen with inference 2 equaling inference 3). By referencing the inference results of $C _ { 3 } \times E$ and considering both SNTs and PNTs, the buyer company knows that a value of IO of 1.5 is quite high because the total debts are very low (TB = –1) and cash flow improves $\left( \mathrm { C F } = 0 . 5 \right)$ . Ultimately, the competitive advantage becomes more marginally acceptable with the value of 0.4 (CA = 0.4). An interesting finding from Scenario 1 is that the buyer company may have a higher IO with the SNTs of $\mathrm { L U } = 0 . 7 , \mathrm { I R } = 0 . 3$ and $\mathrm { P R } = 0 . 8 .$ . This finding has not been addressed or reported in prior research of B2B negotiations.

<table><tr><td colspan="8">Table 5. SNTs and Their Node Values (Buyer Company)</td></tr><tr><td>Interest rate (IR)</td><td>Node value</td><td>Labor dispute (LD)</td><td>Node value</td><td>Oil price (OP)</td><td>Node value</td><td>Labor union&#x27;s cooperation (LU)</td><td>Node value</td></tr><tr><td>Increase</td><td>0.3</td><td>Three times over</td><td>0.9</td><td>Rising</td><td>0.2</td><td>Good</td><td>0.7</td></tr><tr><td>Constancy</td><td>0.7</td><td>1~2 times</td><td>0.7</td><td>Constancy</td><td>0.6</td><td>Middle</td><td>0.5</td></tr><tr><td>Decrease</td><td>0.9</td><td>None</td><td>0.1</td><td>Dropping</td><td>0.8</td><td>Bad</td><td>0.2</td></tr><tr><td>Inventory (IN)</td><td>Node value</td><td>Business expansion (BE)</td><td>Node value</td><td>Support to subsidiary (SS)</td><td>Node value</td><td>Cash flow (CF)</td><td>Node value</td></tr><tr><td>Increase</td><td>0.1</td><td>Extension</td><td>0.8</td><td>Increase</td><td>0.3</td><td>20 percent above</td><td>0.9</td></tr><tr><td>Constancy</td><td>0.4</td><td>Constancy</td><td>0.5</td><td>Constancy</td><td>0.6</td><td>5–20 percent</td><td>0.6</td></tr><tr><td>Decrease</td><td>0.8</td><td>Reduction</td><td>0.2</td><td>Decrease</td><td>0.8</td><td>5 percent below</td><td>0.3</td></tr><tr><td>Total debts (TB)</td><td>Node value</td><td>Wages (WA)</td><td>Node value</td><td>Duration of recession (DR)</td><td>Node value</td><td>Production (PR)</td><td>Node value</td></tr><tr><td>Increase</td><td>0.3</td><td>Increase</td><td>0.4</td><td>One year above</td><td>0.7</td><td>Increase</td><td>0.8</td></tr><tr><td>Decrease</td><td>0.8</td><td>Decrease</td><td>0.9</td><td>One year below</td><td>0.3</td><td>Decrease</td><td>0.3</td></tr></table>

## Scenario 2

Given

PNTs: SP = \$50 per unit (0.2), OQ = 3,000 units (0.6), TD = 15 days

after order placement (0.2), FP = 80 percent cash and

20 percent credit card payment (0.5)

$$
\text { SNTs:   } \mathrm{LD} = \text { good   (0.7) }, \mathrm{BE} = \text { extension   (0.8) }, \mathrm{CF} = 5 \text { percent   below   (0.3) }.
$$

Contrary to Scenario 1, the buyer company is experiencing a labor dispute $( \mathrm { L D } = 0 . 7 )$ and the cash flow is pitched $\left( \mathrm { C F } = 0 . 3 \right)$ due to the business expansion into a new market $( \mathrm { B E } = 0 . 8 )$ . These terms, however, are not negotiable with the sellers because they are SNTs. The buyer company wants to order 3,000 units of raw materials (OQ = 0.6). However, the delivery date that the seller company imposes is quite loose with 15 days after order placement $( \mathrm { T D } = 0 . 2 )$ , and the unit price that the seller offers is \$50, which is expensive $( \mathrm { S P } = 0 . 2 )$ . In addition, the payment condition that the seller suggests is 80 percent cash and 20 percent credit card payment (0.5). In this circumstance, we perform the following what-if simulation. After two iterations, the state of equilibrium is reached with $( 0 . 2 , 0 , 0 . 6 , 0 . 2 , 0 . 4 , - 1 . 3 , - 1 . 2 , 0 , 0 . 7 , 0 , - 1 . 7 , 0 . 5 , 0 , 0 ,$ 0). The results show that the intention to place an order is rather low with 0.4 (IO = 0.4) because the production activity is extremely low $( \mathrm { P R } = - 1 . 2 )$ , which is caused by lack of cooperation by the labor union (LU = 0) and high wages $( \mathrm { W A } = 0 . 7 )$ . All these negative factors push the buyer company’s competitive advantage to a very low level (CA = –1.7). Therefore, in Scenario 2, the buyer company cannot afford to accept the offer from the seller company. Since $\mathrm { I O } = 0 . 4$ is relatively low, the buyer company needs to modify its offers or PNTs so as to increase the IO.

$$
\begin{array}{r l r l r l r l r l r l r l r l r l}&&\text {FP}&\text {TD}&\text {OQ}&\text {SP}&\text {IO}&\text {CF}&\text {PR}&\text {LU}&\text {WA}&\text {LD}&\text {CA}&\text {TB}&\text {IR}&\text {SS}&\text {BE}\\C _ {1}&=&(0. 5&0. 2&0. 6&0. 2&0&0. 3&0&0&0&0. 7&0&0&0&0&0. 8)\\C _ {1} \times E&=&(0. 2&0&0. 6&0. 2&1. 4&- 1. 3&- 0. 2&0&0. 7&0&- 0. 7&0. 5&0&0&0)\\\rightarrow&&(0&0&1&0&1&0&0&0&1&0&0&1&0&0&0)\\C _ {2}&=&(0. 5&0. 2&0. 6&0. 2&1&0. 3&0&0&1&0. 7&0&1&0&0&0. 8)\\C _ {2} \times E&=&(0. 2&0&0. 6&0. 2&0. 4&- 1. 3&- 0. 2&0. 0&0. 7&0&- 1. 7&0. 5&0&0&0)\\\rightarrow&&(0&0&1&0&0&0&0&0&1&0&0&1&0&0&0)\\C _ {3}&=&(0. 5&0. 2&0. 6&0. 2&0&0. 3&0&0&1&0. 7&0&1&0&0&0. 8)\\C _ {3} \times E&=&(0. 2&0&0. 6&0. 2&0. 4&- 1. 3&- 1. 2&0&0. 7&0&- 1. 7&0. 5&0&0&0)\\\rightarrow&&(0&0&1&0&0&0&0&0&1&0&0&1&0&0&0)\end{array}
$$

For this purpose, let us revisit the original PNTs: $\mathrm { S P } = \$ 50$ per units (0.2), OQ = 3,000 units (0.6), TD = 15 days (0.2), and $\mathrm { F P = 8 0 }$ percent cash + 20 percent credit card payment (0.5). The buyer company remembers that the seller’s price is comparatively high $( \mathrm { S P } = \$ 50$ per units) considering its considerably large order quantity, ${ \mathrm { O Q } } = 3 { , } 0 0 0$ units. Therefore, the buyer company suggests counteroffers by lowering the unit price to \$40 $( \mathrm { S P } = \$ 40$ per units (0.8)), reducing the delivery date to seven days after order placement (TD = 7 days (0.5)), but keeping both the OQ and FP unchanged. Then the buyer company would like to know the expected IO if these modified PNTs are approved into the TAKBNs. After three iterations, the IO is still computed as 0.4. However, even after the what-if analysis with other modified SNTs such as $\mathrm { O Q } = 5 { , } 0 0 0$ units (0.3), FP = 50 percent cash and 50 percent credit card payment (0.8), and modified SNTs such as $\mathrm { L D } = + 0 . 2$ , which means that the LD is stabilized, the computed IO still remains 0.4. With this result, we conclude that the buyer company cannot upgrade its IO even with changes in the above SNTs.

## Discussion

Considering both PNTs and SNTs simultaneously presents a real challenge for B2B negotiators because it is difficult to compute the chain of influences accurately in light of the large number of cause–effect relationships among them. An incorrect decision may result in a huge loss in B2B revenue; the proposed framework therefore provides a mechanism with which decision makers can consider both PNTs and SNTs while making more attractive decisions. To organize this discussion more systematically, we will focus on two main issues—reconciliation and evaluation.

## Reconciliation

The reconciliation issue occurs when both buyer and seller are in conflict over one or more PNTs. In general, each B2B player, linked to the others via the Internet, possesses some number of SNTs. Earlier researchers made no attempt to study the influence of SNTs on PNTs. However, even if B2B players had wanted to study this influence, it would have been difficult for them to evaluate it without the proper mechanism. In this paper, we propose a mechanism to take SNTs and PNTs into TAKBNs. The use of CBR also enables us to solve new B2B negotiation problems more effectively. Reconciliation should be made on a systematic negotiation basis, not an arbitrary one. Considering that most TAKBNs are concerned with understanding the possible influences SNTs may have on PNTs (or offers from counterplayers), and vice versa, this framework systematically analyzes both SNTs and PNTs on a cause– effect relationship basis and then derives their computational results. This is an effective reconciliation vehicle that enables B2B players to introduce more desirable negotiation terms. With the illustrative example in the Problem-Solving Phase subsection, we show that such reconciliation is possible using two scenarios in which hidden causal relationships among several PNTs and SNTs are analyzed successfully with a simple matrix multiplication.

## Evaluation

Nelson et al. [60] proposed seven steps for evaluating CM-related methodology. Of these, the last step, “validity of findings,” indicates that decision makers should determine whether the CM findings actually make sense. In accordance with this criterion, we asked five experts who were originally invited to help us perform member checks [54, p. 357] to see whether the results of the two scenarios properly solved the concerns that domain experts usually feel when engaged in the B2B negotiation. Member checks are done by going back to the original expert respondents and asking their opinion about the proposed methodology. The process and purpose of this is to test for factual and interpretive accuracy, and to provide evidence of credibility and trustworthiness similar to internal validity in confirmatory studies [54]. The results of member checks are as follows. First, regarding excellence of inference, the experts agreed that the proposed methodology is unique in examining both PNTs and SNTs within a logical and systematic CM framework; something that was not possible in more traditional approaches. Second, regarding ease of application, the experts all suggested that the proposed methodology would be very easy for decision makers to use in a real work environment because the inference process can be performed simply on spreadsheet programs such as Excel.

To add more quantitative rigor to the results of the member checks, we performed a prioritization experiment and Wilcoxon test [1] based on a structured questionnaire survey completed by another group of 16 B2B negotiation experts who have worked in four B2B companies for six to 15 years. Since decision performance in the proposed framework should be tested statistically, our first job was to configure the questionnaire to evaluate the decision makers’ psychological attitudes toward the framework as well as its quantitative aspects. Before proceeding further, it seems necessary to consider the meaning of decision performance. Decision performance is “to evaluate the outcomes generated by individuals or groups in accomplishing their task” [26, p. 7]. Such evaluation measures fall into four general categories [17, 69]: (1) quality or effectiveness, focusing on tangible results of the decision or problem solution; (2) satisfaction or confidence, focusing on the attitude of group members regarding these outcomes; (3) economic value, referring to net profit, increased revenue, or decreased expenses to the organization resulting from introducing and using the DSS; and (4) efficiency, concerned primarily with time to make the decision or complete the task. Aldag and Power [2] also suggested seven constructs of assessing decision makers attitudes toward decision-making processes: (1) confidence in decision quality, (2) enhancement of problem-solving ability, (3) satisfaction with resource expenditure, (4) perceived acceptability of solution, (5) perceived process structure, (6) perceived process adequacy, and (7) positive affect toward process. Montazemi and Gupta [58] have used the four constructs among the above seven constructs [2] by organizing them into two categories: (1) quantitative measures of decision quality or effectiveness that focus on the tangible results of the decision process, and (2) qualitative measures of the decision process. Aldag and Power’s constructs were adopted to organize our questionnaire, which consisted of 13 items (see Appendix D for details).

Using the questionnaire, the 16 domain experts’ attitudes toward solving the two scenarios based on the proposed framework were rigorously assessed.

For our objective experiments, a prototype system, written in Excel VBA macro, was implemented to help B2B negotiation domain experts experience solving the two scenarios. Experiments were then performed in two ways: (1) through prioritization of the 13 items regarding decision performance and (2) through the answers on the questionnaire.

Prioritization of the 13 Items Regarding Decision Performance. The 16 domain experts were first given cards containing the description of two scenarios and asked to read them. They were then asked to “rank” the 13 items on the questionnaire in order of how important each statement’s meaning was to solving the scenarios. In other words, they were asked to place the statement that was most important at the top of the deck of cards and the statement that was least important at the bottom. A ranking matrix was used to derive a priority index for each item, and the median rank was used as the basis for establishing item priority. The median was chosen over the mean because of its robustness in light of the skewed distribution of the priority ratings, while the mean was used to break ties. This methodology has previously been used to evaluate the importance of variables in the fields of psychology and management information systems (MIS) [1, 8]. In this study, the 16 domain experts ranked 13 items according to their relative importance (see summary in Table 6). A nonparametric test was used to assess interrater reliability since variables can be categorical and normal distribution assumptions are not met. A Kendall test was therefore used to measure agreement among the 16 experts’ ordering of the 13 items [30]. A test statistic $W = 0 . 6 6 2$ was calculated, indicating the 16 experts’ significant agreement on the relative importance ratings of the 13 items $( \chi ^ { 2 } = 1 2 7 . 0 1 , p < 0 . 0 0 1 )$ . Table 6 shows the medians, means, and resulting priorities for the perceived relative importance of the 13 items, where (R) denotes a reverse item. The most important item is DP10, followed by DP12, DP13, DP3, DP4, DP11, DP7(R), DP6(R), DP1(R), DP2(R), DP8(R), DP5(R), and DP9(R) in descending order of relative importance. To put this order using the construct name, the two constructs, “perceived acceptability of solution” and “perceived process structure,” were seen as relatively more important than the other three constructs, “perceived adequacy of the decision process,” “confidence in decision quality,” and “perceived satisfaction with expenditure of time and effort,” all of which are made up of reverse items. It is noteworthy that the reverse items have a low level of relative importance, meaning that the 16 experts were originally satisfied with the decision performance suggested by the proposed framework as well as with the low expenditure of time and effort. These results have something in common with the results of member checks.

The Answers on the Questionnaire. For the two kinds of TAKBN (individual CM and final CM), the 16 experts were asked to answer by circling a number from one to seven, arranged horizontally beneath anchor point descriptions “strongly disagree (1),” “neutral (4),” and “strongly agree (7)” (see Appendix D). Because each expert was asked to evaluate the questionnaire for the two kinds of TAKBN, response results were analyzed statistically using the Wilcoxon matched-pairs test [29, 53]. The Wilcoxon test, a nonparametric approach, can be used to compare two variables within one group [1] and has been used broadly in the field of MIS research [6]. Because the Wilcoxon test does not require a hypothesis about the form of distribution, it was suitable for our case, in which the sample numbered fewer than 30. Table 7 shows the Wilcoxon test results and illustrates that for 11 of the 13 items (not including DP3 and DP8), the domain experts perceived a significant difference between the two kinds of TAKBN. The other two items, DP3 and DP8, illustrate that the domain experts did not perceive a difference in interest and time spent between the two kinds of TAKBN, meaning that they felt the proposed framework was both interesting (DP3) and time well spent (DP8), regardless of the TAKBN they used to solve the scenarios. For the final CM, all other decision performance measures showed higher means or improved values when compared to the individual CM, indicating that how different experts’ tacit knowledge is integrated into a final CM could upgrade decision performance. In a nutshell, Table 7 reveals that using the framework based on the final CM could provide a better decision performance for the two scenarios than the individual CM.

Table 6. Prioritization of Items

<table><tr><td>Construct</td><td>Item number</td><td>Median rank</td><td>Mean rank</td><td>Priority</td></tr><tr><td rowspan="2">Confidence in decision quality</td><td>DP1(R)</td><td>8</td><td>7.2</td><td>9</td></tr><tr><td>DP2(R)</td><td>9</td><td>8.6</td><td>10</td></tr><tr><td rowspan="3">Positive affect toward the decision process</td><td>DP3</td><td>5</td><td>5.7</td><td>4</td></tr><tr><td>DP4</td><td>6</td><td>6.0</td><td>5</td></tr><tr><td>DP5(R)</td><td>12</td><td>10.8</td><td>12</td></tr><tr><td rowspan="2">Perceived adequacy of the decision process</td><td>DP6(R)</td><td>8</td><td>6.8</td><td>8</td></tr><tr><td>DP7(R)</td><td>7</td><td>6.8</td><td>7</td></tr><tr><td rowspan="2">Perceived satisfaction with expenditure of time and effort</td><td>DP8(R)</td><td>10</td><td>9.5</td><td>11</td></tr><tr><td>DP9(R)</td><td>13</td><td>5.7</td><td>13</td></tr><tr><td rowspan="2">Perceived acceptability of solution</td><td>DP10</td><td>4</td><td>4.2</td><td>1</td></tr><tr><td>DP11</td><td>7</td><td>6.1</td><td>6</td></tr><tr><td rowspan="2">Perceived process structure</td><td>DP12</td><td>4</td><td>5.3</td><td>2</td></tr><tr><td>DP13</td><td>5</td><td>5.5</td><td>3</td></tr><tr><td colspan="5">(R) denotes a reverse item.</td></tr></table>

## Concluding Remarks

B2B NEGOTIATION HAS CAPTURED THE ATTENTION of game theorists, computer scientists, and economists in the past decade [15, 38]. From the technology perspective, intelligent agent has been a promising technology toward B2B negotiation [14, 37].

Table 7. Wilcoxon Test Results

<table><tr><td rowspan="2">Item number</td><td colspan="2">Individual CM (n = 16)</td><td colspan="2">Final CM (n = 16)</td><td rowspan="2">t-value for difference</td><td rowspan="2">p-value</td></tr><tr><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>DP1(R)</td><td>5.75</td><td>1.00</td><td>6.50</td><td>0.52</td><td>-2.24</td><td>0.03*</td></tr><tr><td>DP2(R)</td><td>6.06</td><td>0.85</td><td>6.63</td><td>0.50</td><td>-2.01</td><td>0.04*</td></tr><tr><td>DP3</td><td>6.25</td><td>0.68</td><td>6.44</td><td>0.73</td><td>-1.13</td><td>0.26</td></tr><tr><td>DP4</td><td>6.31</td><td>0.79</td><td>6.75</td><td>0.45</td><td>-2.11</td><td>0.03*</td></tr><tr><td>DP5(R)</td><td>5.75</td><td>0.45</td><td>6.31</td><td>0.70</td><td>-2.50</td><td>0.01**</td></tr><tr><td>DP6(R)</td><td>5.81</td><td>0.83</td><td>6.75</td><td>0.45</td><td>-2.83</td><td>0.00***</td></tr><tr><td>DP7(R)</td><td>4.06</td><td>1.18</td><td>5.69</td><td>1.08</td><td>-2.76</td><td>0.01**</td></tr><tr><td>DP8(R)</td><td>6.31</td><td>0.70</td><td>6.13</td><td>0.81</td><td>-0.47</td><td>0.64</td></tr><tr><td>DP9(R)</td><td>5.88</td><td>0.81</td><td>6.63</td><td>0.50</td><td>-2.55</td><td>0.01**</td></tr><tr><td>DP10</td><td>4.00</td><td>1.15</td><td>5.56</td><td>1.26</td><td>-3.10</td><td>0.00***</td></tr><tr><td>DP11</td><td>4.06</td><td>1.18</td><td>5.69</td><td>1.08</td><td>-2.76</td><td>0.01**</td></tr><tr><td>DP12</td><td>6.31</td><td>0.79</td><td>6.81</td><td>0.40</td><td>-2.31</td><td>0.02*</td></tr><tr><td>DP13</td><td>5.75</td><td>0.45</td><td>6.44</td><td>0.81</td><td>-2.84</td><td>0.00***</td></tr><tr><td colspan="7">*p&lt;0.05, **p&lt;0.01, ***p&lt;0.001.</td></tr></table>

However, research in B2B negotiation from more practical and easy-to-understand viewpoints is scarce. This paper contributes to the understanding of B2B negotiation by proposing a framework using both a CM and CBR to tackle the problem of B2B negotiation. The proposed framework encompasses all negotiation terms related to B2B negotiation, PNTs and SNTs, as it is believed that they critically influence the performance of B2B negotiation. The proposed framework relates negotiation activities with PNTs and SNTs. Unlike prior research, this paper emphasizes the combination of both PNTs and SNTs in modeling and analyzing B2B negotiation. As tacit knowledge is required in handling these negotiation terms, TAKBN was introduced to capture cause–effect knowledge among PNTs and SNTs in B2B negotiation. The proposed framework consists of three major phases—formalization, reuse, and problem solving. In the formalization phase, it is responsible for generating TAKBNs— for modeling the B2B negotiation problem being solved and past B2B negotiation cases. CMs and CBR are the core methods in this phase. Keeping past cases for reference can help retain a long-term cooperation in a win–win spirit with particular companies. Such long-term cooperation is known as a key factor for success in negotiation [18, 79]. In the reuse phase, related TAKBNs will be retrieved and compared with the TAKBNs of the new B2B problems. B2B decision makers may draw references to past cases and study their strategies in handling similar B2B negotiation situations. Also, new players may gain experience by studying past cases. The problem-solving phase provides a useful, practical, and necessary what-if tool for decision makers to consider B2B negotiation problems from various perspectives. The decision makers may adjust the concerning parameters and simulate a different situation to predict possible outcomes.

With the support of two well-known B2B players in South Korea, we compiled two realistic B2B negotiation scenarios and tested the proposed B2B negotiation framework with them. We demonstrate that the proposed framework is practical and easy to use in B2B negotiation. The invited experts verified that with the use of both PNTs and SNTs in our model, the proposed framework represents a very useful and effective what-if tool for B2B negotiation, and the solutions are far more realistic and practical. The overall experimental results are very positive. We believe that the proposed framework also provides a foundation for other related research in the field of negotiation, behavioral study, and pricing strategy. We hope that more studies will be suggested where the proposed framework is tested against cases from various industries and businesses to prove its applicability and extensibility.

Acknowledgment: This research project was supported by Korea Research Foundation Grant KRF-2001–041-C00339.

## NOTE

1. It is worth noting that node values in Tables 4 and 5 were extracted from the focus group interview with five experts working for two famous B2B companies in Korea. They considered a number of real B2B negotiation instances gathered in the two companies. Combination of each node value would lead to a great deal of B2B negotiation cases. However, we consider typical cases for illustration of the performance of the proposed methodology.

## REFERENCES

1. Alavi, M. An assessment of the concept of decision support systems as viewed by seniorlevel executives. MIS Quarterly, 6, 4 (1982), 1–9.

2. Aldag, R.J., and Power, D.J. An empirical assessment of computer-assisted decision analysis. Decision Science, 17, 4 (1986), 572–588.

3. Axelrod, R. Structure of Decision: The Cognitive Maps of Political Elites. Princeton: Princeton University Press, 1976.

4. Bailin, S.C., and Truszkowski, W. Ontology negotiation between intelligent information agents. Knowledge Engineering Review, 17, 1 (2002), 7–19.

5. Bakos, Y. The emerging role of electronic marketplaces on the Internet. Communications of the ACM, 41, 8 (1998), 35–42.

6. Baroudi, J.J., and Orlikowski, W.J. The problem of statistical power in MIS research. MIS Quarterly, 13, 1 (1989), 87–106.

7. Bergmann, R., and Cunningham, P. Acquiring customers’ requirements in electronic commerce. Artificial Intelligence Review, 18, 3–4 (2002), 163–193.

8. Bohrnstedt, G.W. Reliability and validity assessment in attitude measurement. In G.F. Summers (ed.), Attitude Measurement. Chicago: Rand McNally, 1970, pp. 80–99.

9. Bougon, M. Congregate cognitive maps: A unified dynamic theory of organization and strategy. Journal of Management Studies, 29, 3 (1992), 369–389.

10. Bougon, M.; Weick, K.E.; and Binkhorst, D. Cognition in organizations: An analysis of the Utrecht Jazz Orchestra. Administrative Science Quarterly, 22, 4 (1977), 606–636.

11. Chen, J.L., and Stanney, K.M. A theoretical model of way finding in virtual environments: Proposed strategies for navigational aiding. Presence: Teleoperators & Virtual Environments, 8, 6 (1999), 671–685.

12. Cheung, S.C.; Hung, P.C.K.; and Chiu, D.K.W. On the e-negotiation of unmatched logrolling views. In R.H. Sprague Jr. (ed.), Proceedings of the Thirty-Sixth Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 2003, pp. 29–38 (available at www.hicss.hawaii.edu/hicss36).

13. Cohn, L.; Brady, D.; and Welch, D. B2B: The hottest net bet yet? BusinessWeek (January 17, 2000), 36–37.

14. Collins, J.; Bilot, C.; Gini, M.; and Mobasher, B. Decision processes in agent-based automated contracting. IEEE Internet Computing, 5, 2 (2001), 61–72.

15. Conry, S.E.; Kuwabara, K.; Lesser, V.R.; and Meyer, R.A. Multistage negotiation for distributed constraint satisfaction. IEEE Transactions on Systems, Man & Cybernetics, 21, 6 (1991), 1462–1477.

16. Cunningham, P.; Bergmann, R.; Schmitt, S.; Traphöner, R.; Breen, S.; and Smyth, B. Intelligent support for online sales: The WEBSELL experience. In R. Weber and C.G. Wangenheim (eds.), Proceedings of the Fourth International Conference on Case-Based Reasoning. Vancouver: Springer, 2001, pp. 87–93.

17. DeSanctis, G. Computer graphics as decision aids: Direction for research. Decision Sciences, 15, 4 (1984), 463–487.

18. Donnellon, A. Team Talk: The Power of Language in Team Dynamics. Boston: Harvard Business School Press, 1996.

19. Eden, C. Cognitive mapping: A review. European Journal of Operational Research, 36, 1 (1988), 1–13.

20. Eden, C. Strategic options development and analysis—SODA. In J. Rosenhead (ed.), Rational Analysis in a Problematic World. London: Wiley, 1989, pp. 21–42.

21. Eden, C. Strategic thinking with computers. Long Range Planning, 23, 6 (1990), 35–43.

Using a computer to help with the management of strategic vision. In G. Miller (ed.), Knowledge-Based Management Support Systems. New York: Ellis Horwood, 1989, pp. 198–207.

23. Eden, C.; Jones, S.; and Sims, D. Thinking in Organizations. London: Macmillan Press, 1979.

24. Eden, C.; Jones, S.; and Sims, D. Messing About in Problems. Oxford: Pergamon, 1983. 25. Eden, C.; Jones, S.; Sims, D.; and Smithin, T. The intersubjective of issues and issues of intersubjectivity. Journal of Management Studies, 18, 1 (1981), 37–47.

26. Eierman, M.A.; Niederman, F.; Adams, C. DSS theory: A model of constructs and relationships. Decision Support Systems, 14, 1 (1995), 1–26.

27. Fells, R.E. Overcoming the dilemmas in Walton and McKersie’s mixed bargaining strategy. Industrial Relations, 53, 2 (1998), 300–325.

28. Fischer, K.; Chaib-draa, B.; Muller, J.P.; Pischel, M.; and Gerber, C. A simulation approach based on negotiation and cooperation between agents: A case study. IEEE Transactions on Systems, Man & Cybernetics, Part C: Applications & Reviews, 29, 4 (1999), 531–545.

29. Gibbons, J.D. Nonparametric Statistical Inference, 2d ed. New York: Marcel Dekker, 1985.

30. Goodman, P.S., and Darr, E.D. Computer-aided systems and communities: Mechanisms for organizational learning in distributed environments. MIS Quarterly, 22, 4 (1998), 417–440.

31. Grewal, R.; Comer, J.M.; and Mehta, R. An investigation into the antecedents of organizational participation in business-to-business electronic markets. Journal of Marketing, 65, 3 (2001), 17–33.

32. Heiskanen, F. Generating pareto-optimal boundary points in multiparty negotiations using constraint proposal method. Naval Research Logistics, 48, 3 (2001), 210–225.

33. Hoffman, D.L., and Novak, T.P. Marketing in hypermedia computer-mediated environments: Conceptual foundations. Journal of Marketing, 60, 3 (1996), 50–68.

34. Huff, A.S. Mapping Strategic Thought. New York: Wiley, 1990.

35. Johnson, R.J., and Briggs, R.O. A model of cognitive information retrieval for ill-structured managerial problems and its benefits for knowledge acquisition. In R.H. Sprague Jr. (ed.), Proceedings of the Twenty-Seventh Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 1994, pp. 191–200.

36. Kaplan, S., and Sawhney, M. E-hubs: The new B2B marketplace. Harvard Business Review, 78, 3 (May–June 2000), 97–103.

54. Lincoln, L.S., and Guba. E.G. Naturalistic Inquiry. Thousand Oaks, CA: Sage, 1985. 54. Lincoln, L.S., and Guba. E.G. Naturalistic Inquiry. Thousand Oaks, CA: Sage, 1985. 55. Liu, Z.Q., and Satur, R. Contextual fuzzy cognitive map for decision support in geographic information systems. IEEE Transactions on Fuzzy Systems, 7, 5 (1999), 495–507.

37. Karageorgos, A.; Thompson, S.; and Mehandjiev, N. Agent-based system design for B2B electronic commerce. International Journal of Electronic Commerce, 7, 1 (Fall 2002), 59–90.

38. Kauffman, R.J., and Walden, E.A. Economics and electronic commerce: Survey and directions for research. International Journal of Electronic Commerce, 5, 4 (Summer 2001), 5–116.

39. Kersten, G.E. The science and engineering of e-negotiation: An introduction. In Ralph H. Sprague Jr. (ed.), Proceedings of the Thirty-Sixth Annual Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 2003, pp. 27–36 (available at www.hicss.hawaii.edu/hicss36).

40. Kersten, G.E., and Noronha, S.J. WWW-based negotiation support: Design, implementation, and use. Decision Support Systems, 25, 2 (1999), 135–154.

41. Kersten, G.E., and Szpakowicz, S. Modeling business negotiations for electronic commerce. In K. Komunikat (ed.), Proceedings of the Seventh Workshop on Intelligent Information Systems. Warsaw: Malbork, 1998, pp. 17–28.

42. Kim, H.S., and Lee, K.C. Fuzzy implications of fuzzy cognitive map with emphasis on fuzzy causal relationship and fuzzy partially causal relationship. Fuzzy Sets & Systems, 97, 3 (1998), 303–313.

43. Kim, J.H., and Pearl, J. CONVINCE: A conversational inference consolidation engine. IEEE Transactions on Systems, Man & Cybernetics, 17, 2 (1987), 120–132.

44. Klein, J.H., and Cooper, D.F. Cognitive maps of decision-makers in a complex game. Journal of the Operational Research Society, 33, 1 (1982), 63–71.

45. Kolodner, J. Case-Based Reasoning. San Mateo, CA: Morgan Kaufmann, 1993.

46. Kosko, B. Neural Networks and Fuzzy Systems: A Dynamical Systems Approach to Machine Intelligence. Upper Saddle River, NJ: Prentice Hall, 1992.

47. Kowalczyk, R. Fuzzy e-negotiation agents. Soft Computing, 6, 5 (2002), 337–347.

48. Kwahk, K.Y., and Kim, Y.G. Supporting business process redesign using cognitive maps. Decision Support Systems, 25, 2 (1999), 155–178.

49. Lee, K.C., and Lee, S. A cognitive map simulation approach to adjusting the design factors of the electronic commerce Web sites. Expert Systems with Applications, 24, 1 (2003), 1–11.

50. Lee, S., and Courtney, J.F., Jr. Organizational learning system. In R.H. Sprague Jr. (ed.), Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 1989, pp. 492–503.

51. Lee, S.; Courtney, J.F., Jr.; and O’Keefe, R.M. A system for organizational learning using cognitive maps. Omega, 20, 1 (1992), 23–36.

52. Lenz, R.T., and Engledow, J.L. Environmental analysis: The applicability of current theory. Strategic Management Journal, 17, 4 (1986), 329–346.

53. Levin, R.I., and David, S.R. Statistics for Management, 7th ed. Upper Saddle River, NJ: Prentice Hall, 1998.

56. Mazer, M.S. Reasoning about knowledge to understand distributed AI systems. IEEE Transactions on Systems, Man & Cybernetics, 21, 6 (1991), 1333–1346.

57. Montazemi, A.R., and Conrath, D.W. The use of cognitive mapping for information requirements analysis. MIS Quarterly, 10, 1 (1986), 45–56.

58. Montazemi, A.R., and Gupta, K. On the effectiveness of cognitive feedback from an interface agent. Omega: International Management Science, 25, 6 (1997), 643–658.

59. Moukas, A.; Zacharia, G.; Guttman, R.; and Maes, P. Agent-mediated electronic commerce: An MIT media laboratory perspective. International Journal of Electronic Commerce, 4, 3 (Spring 2000), 5–21.

60. Nelson, K.M.; Nadkarni, S.; Narayanan, V.K.; and Ghods, M. Understanding software operations support expertise: A revealed causal mapping approach. MIS Quarterly, 24, 3 (2000), 475–507.

61. Ngai, E.W.T. Internet marketing research (1987–2000): A literature review and classification. European Journal of Marketing, 37, 1–2 (2003), 24–49.

62. Noh, J.B.; Lee, K.C.; Kim, J.K.; Lee, J.K.; and Kim, S.H. A case-based reasoning approach to cognitive map–driven tacit knowledge management. Expert Systems with Applications, 19, 4 (2000), 249–259.

63. Numata, J.; Hane, K.; Bangyu, L.; and Iwashita, Y. Knowledge discovery and sharing in an information system. In D.F. Kocaoglu and T.R. Anderson (eds.), Proceedings of Portland International Conference on Management of Engineering Technology. Los Alamitos, CA: IEEE Computer Society Press, 1997, pp. 713–716.

64. Park, K.S., and Kim, S.H. Fuzzy cognitive maps considering time relationships. International Journal of Human–Computer Studies, 42, 2 (1995), 157–168.

65. Ramaprasad, A., and Poon, E. A computerized interactive technique for mapping influence diagrams (MIND). Strategic Management Journal, 6, 4 (1985), 377–392.

66. Rich, E., and Knight, K. Artificial Intelligence. New York: McGraw-Hill, 1991.

67. Satur, R., and Liu, Z.Q. A context driven intelligent database processing system using object-oriented fuzzy cognitive maps. International Journal of Intelligent Systems, 11, 9 (1996), 671–689.

68. Satur, R., and Liu, Z.Q. A contextual fuzzy cognitive map framework for geographic information systems. IEEE Transactions on Fuzzy Systems, 7, 5 (1999), 481–494.

69. Schroeder, R.G., and Benbasat, I. An experimental evaluation of the relationship of uncertainty in the environment to information used by decision makers. Decision Science, 6, 3 (1975), 556–567.

70. Sim, K.M. A market driven model for designing negotiation agents. Computational Intelligence, 18, 4 (2002), 618–637.

71. Sim, K.M., and Choi, C.Y. Agents that react to changing market situations. IEEE Transactions on Systems, Man & Cybernetics, Part B: Cybernetics, 33, 2 (2003), 188–201.

72. Smith, K.L. Exploring the need for a shared cognitive map. Journal of Management Studies, 29, 3 (1992), 349–368.

73. Stahl, A., and Bergmann, R. Applying recursive CBR for the customization of structured products in an electronic shop. In E. Blanzieri and L. Protinale (eds.), Proceedings of the Fifth European Workshop on Case-Based Reasoning. Trento, Italy: Springer-Verlag, 2000, pp. 297–308.

74. Strobel, M. Design of roles and protocols for electronic negotiations. Electronic Commerce Research, 1, 3 (2001), 335–353.

75. Sycara, K.P. Negotiation planning: An AI approach. European Journal of Operational Research, 46, 2 (1990), 216–234.

76. Taber, R. Knowledge processing with fuzzy cognitive maps. Expert Systems with Applications, 2, 1 (1991), 83–87.

77. Tapscott, D. Digital Economy. New York: McGraw-Hill, 1996.

78. Ulengin, F.; Topcu, Y.I.; and Sahin, S.O. An integrated decision aid system for bosphorus water-crossing problem. European Journal of Operational Research, 134, 1 (2001), 179–192.

79. Ulijn, J.M.; Lincke, A.; and Karakaya, Y. Non–face-to-face international business negotiation: How is national culture reflected in this medium. IEEE Transactions on Professional Communication, 44, 2 (2001), 126–137.

80. Walton, R.E., and McKersie, R.B. A Behavioral Theory of Labor Negotiations. New York: McGraw-Hill, 1965.

81. Warren, K. Exploring competitive futures using cognitive mapping. Long Range Planning, 28, 5 (1995), 10–21.

82. Weigand, H.; Schoop, M.; Moor, A.D.; and Dignum, F. B2B negotiation support: The need for a communication perspective. Group Decision and Negotiation, 12, 1 (2003), 3–29.

83. Wellman, M. Inference in cognitive maps. Mathematics and Computers in Simulation, 36, 2 (1994), 137–148.

84. Wong, W.Y.; Zhang, D.M.; and Kara-Ali, M. Negotiating with experience. In T. Finin and B. Grosof (eds.), Proceedings of the American Association for Artificial Intelligence (AAAI) Workshop on Knowledge-Based Electronic Markets. Menlo Park, CA: AAAI Press, 2000, pp. 85–90.

85. Zhang, W.R. Pool: A semantic model for approximate reasoning and its application in decision support. Journal of Management Information Systems, 3, 4 (Spring 1987), 65–78.

86. Zhang, W.R.; Chen, S.S.; and Bezdek, J.C. P0012: A generic system for cognitive map development and decision analysis. IEEE Transactions on Systems, Man & Cybernetics, 19, 1 (1989), 31–39.

87. Zhang, W.R.; Wang, W.; and King, R.S. A-Pool: An agent-oriented open system shell for distributed decision process modeling. Journal of Organizational Computing, 4, 2 (1994), 127–154.

## Appendix A. Preparation of Cases for the Experiment

AS DESCRIBED ABOVE, FIVE B2B EXPERTS working for two famous B2B players in Korea—KTNet and EC Plaza—were invited to the principal author’s office for a focus group interview, the purpose for which was to specify appropriate B2B negotiation cases for our study, related contents such as PNTs and SNTs, and situation information. Details on the experiment and cases are as follows.

First, among the number of B2B transactions cases performed on the two B2B players, 15 cases were selected for our study, and related PNTs and SNTs were also determined for each case. The reason only 15 cases were selected is because they represent typical situations for B2B negotiation that seemed sufficient for our research purpose, and we did not need to risk a computational burden by incorporating a large number of excessive cases beyond our original research purpose. To determine the cases necessary for our research purpose, we asked experts the following two questions.

Question 1: How many cases would be required to fulfill our research purpose? Of course, the principal author explained the intrinsic nature of our research purpose, which is to use CMs and CBR for B2B negotiation problems. The experts suggested that it was unnecessary to develop a huge number of cases for our research and thereby risk a computational burden. Therefore, experts and the principal author agreed to select typical B2B negotiation cases from the database of two B2B companies. The experts first consumed about 30 minutes to select approximately 50 cases. After reviewing them, the principal author proposed that it might be appropriate to include 20 cases considering the size of company (abbreviated as SC in Table 3). Then, the experts suggested deleting five cases due to their redundancy. Thus, 15 cases were selected for our research.

Question 2: Which factors should be considered in each case? The experts first suggested considering this question from the perspective of the buyer company because most of the cases in their database were focused on the buyer company, which wants to conduct B2B negotiations with potential seller companies. In response, the principal author offered that the information regarding the buyer company should include environment characteristics while information regarding the seller company should be focused on firm characteristics, because our research purpose requires the CM to include a set of causal relationships between the environment factors and firmrelated factors to give the inference process a more complicated and reality-based flavor. A set of factors and related values are summarized in Table 1.

Second, the situation information for the 15 cases was collected by the five experts and summarized in Table 1. Our assumption was that a buyer company intended to negotiate with the possible seller company before making a decision to purchase specific products or services from the seller.

Third, the 15 cases with their PNTs and SNTs were distributed to the five experts so that they could draw an appropriate CM for each case by using both PNTs and SNTs as well as the related situation information of Table 1.

Fourth, the principal author gave the five experts a brief, but intensive, introduction about how to draw a CM and interpret it for the B2B negotiation problem. Then, each expert was given a maximum of 30 minutes to draw an individual CM for each case so that five individual CMs were prepared for each case.

Fifth, the experts discussed with each other to determine an appropriate consensus CM for each case, taking about one hour to come up with final consensus CMs for the 15 cases. Those CMs were stored into a case base for further use. The full contents of each case are depicted in Table 3. It is worth noticing that an appropriate consensus (or integrated) CM is attached to each case at the utmost right column of Table 3.

## Appendix B. Fitting Ratio and Garbage Ratio

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
IN THE PROPOSED CBR APPROACH to the reuse phase, both the fitting ratio and garbage ratio are defined mathematically as follows:

N: the number of cases.

 $X_{1}, X_{2}, \ldots, X_{N}$ : cases in case base.

 $T = \{S_{1}, S_{2}, \ldots, S_{N}\}$ : situation frame set, where  $S_{k}$  is the situation frame of  $X_{k}, k = 1, \ldots, N$ .

m: the number of situation information of each case.

 $S_{k} = (e_{k1}, e_{k2}, \ldots, e_{km})$ : the value of situation frame of case  $X_{k}, k = 1, \ldots, N$ .

 $S_{0} = (e_{01}, e_{02}, \ldots, e_{0m})$ : the value of situation frame of the new B2B negotiation problem.

 $R = (r_{1}, r_{2}, \ldots, r_{m})$ : R is an indicator representing whether each situation frame of the new B2B negotiation problem is covered. Hence,

 $r_{j} = \begin{cases} 1 &amp; e_{oj} \text{ is covered} \\ 0 &amp; e_{oj} \text{ is not covered.} \end{cases}$ 

n(R): the number of situation information of R, which has the value 1 in this paper.

Definition
</div>

The fitting ratio $F _ { k }$ is the degree that the current situation information of a new problem is to be covered when $X _ { k }$ is selected as a next retrieved case. $F _ { k }$ is defined as

$$
F _ {k} = \frac {n (\overline {{R}} \otimes (S _ {0} \cdot S _ {k}))}{n (\overline {{R}})}.
$$

The garbage ratio $G _ { k }$ is the number of situation information of $X _ { k }$ that does not match with those of a new problem. $G _ { k }$ can be defined as

$$
G _ {k} = \frac {m - n (S _ {0} \cdot S _ {k})}{m}.
$$

The fitting ratio is calculated between the situation information of the new B2B negotiation problem and those of the cases stored in the case base. The number of candidate cases may be predefined or may be larger than a predefined threshold value, $\theta _ { G } . \mathrm { A }$ case becomes a candidate case if the garbage ratio is less than the predefined threshold value $\theta _ { G } ( 0 \leq \theta _ { G } \leq 1 )$ . If a larger $\theta _ { G }$ is used, more cases will be selected as candidate cases, but the risk is to have more inappropriate cases accepted as candidate cases. In the CBR experiment performed in the Reuse Phase section, 0.5 was used as threshold value $\theta _ { G } .$ . We defined two functions, MAX(T) and MIN(T), where MAX(T) returns the element that has the largest fitting ratio, while MIN(T) returns the element that has the smallest garbage ratio. To illustrate the use of the fitting ratio and garbage ratio, let us suppose that a new B2B case $S _ { 0 }$ arises as shown in the first row in Table 3. Its situations are depicted in the first row with $\mathrm { S C } = \mathrm { \mathrm { ^ { 4 } L G , ^ { 9 , } T I } } = \mathrm { ^ { 4 } E C , ^ { 9 } }$ and $\mathrm { C S } = { } ^ { 6 6 } \mathrm { S G } . { } ^ { 7 }$ We do not know, however, which CM seems appropriate for this new B2B case $S _ { 0 } .$ (Note that the cell at the utmost right under the title $C M _ { n }$ is given as $\mathbf { \Psi } ^ { 6 6 9 } ? _ { 9 } ^ { 9 9 }$ which means that it is to be determined through CBR experiments using a fitting ratio and garbage ratio.) To determine the appropriate CM for a new B2B case $S _ { 0 } ,$ we perform the following iteration as shown in Table 2.

## Iteration 1

Since we have 15 cases in the case base, 15 fitting ratios should be calculated respectively for them in line with the definitions above. Results are $F _ { _ { 1 } } = 0 . 6 0 , F _ { _ { 2 } } = 0 . 7 3 , F _ { _ { 3 } } =$ 0.67, $F _ { 4 } = 0 . 2 0 , F _ { 5 } = 0 . 4 0 , F _ { 6 } = 0 . 4 0 , F _ { 7 } = 0 . 4 7 , . . . , F _ { 1 5 } = 0 . 4 0 . F _ { 2 }$ has the largest fitting ratio, 0.73. Its garbage ratio $G _ { 2 }$ is also calculated as 0.27 in accordance with the definition, though it is not necessary to compute it in actuality because there is only one fitting ratio. Therefore, CM is chosen as a candidate TAKBN for a new B2B negotiation case $S _ { 0 } .$ Since we are using 0.5 as a threshold value, those fitting ratios over 0.5 will be denoted as 1 in R. Therefore, we have R as $( 1 , 1 , 1 , 0 , 1 , 1 , 1 , 0 , 0 , 1$ 2 0, 1, 1, 1, 1). Since four 0s exist in $R , n ( \bar { R } ) = 4$ . Since $n ( { \bar { R } } )$ is not 0, the iteration must continue further until $n ( { \bar { R } } )$ becomes 0.

## Iteration 2

Fourteen fitting ratios are calculated for the remaining 14 cases. Results are shown in the third row at iteration 2 in Table 2. Since there exist three largest fitting ratios, 0.75 for $F _ { 1 } , F _ { 3 } ,$ and $F _ { 5 } ,$ their garbage ratios should be considered further to select the one with least garbage ratio value: $G _ { 1 } = 0 . 4 0 , G _ { 3 } = 0 . 3 3$ , and $G _ { 5 } = 0 . 6 0$ . Therefore, $C M _ { 3 }$ is selected because its garbage ratio is 0.33. Since $n ( { \bar { R } } ) = 1$ , another round of iteration is needed.

## Iteration 3

As we did in iterations 1 and 2, three fitting ratio values, $F _ { 1 } , F _ { 4 } , F _ { 5 } ( = 1 . 0 )$ , are found to be the largest. Therefore, the garbage ratio values are further calculated to choose only one candidate. $G _ { \mathrm { 1 } } ( = 0 . 4 0 )$ is the least among the other garbage ratios. In conclusion, $C M _ { 1 }$ is selected as a candidate and $n ( { \bar { R } } ) = 0 ;$ , indicating that further iteration is not necessary.

Integrating the results so far, final CM candidates for $S _ { \mathrm { 0 } } \mathrm { a r e } C M _ { \mathrm { 2 } } , C M _ { \mathrm { 3 } } , C M _ { \mathrm { 1 } }$

## Appendix C. Forward-Evolved Inference

CONSIDER THE FORWARD-EVOLVED INFERENCE using the causal knowledge in Figure 1. We first assume a concept node vector, which is defined as a vector showing a set of input or output values that each concept node can have through inference. There are seven concept nodes in Figure 1, where there are four PNTs and three SNTs. We can define a concept node vector C accordingly as follows: $\begin{array} { r } { { \cal C } = ( C _ { 1 } , C _ { 2 } , C _ { 3 } , } \end{array}$ $C _ { 4 } , C _ { 5 } , C _ { 6 } , C _ { 7 } )$ , where $C _ { 1 }$ represents Intention to Order, $C _ { 2 }$ for production, $C _ { 3 }$ for trust for seller, $C _ { 4 }$ for order quantity, $C _ { 5 }$ for favorableness of payment condition, $C _ { 6 }$ for seller’s price, and $C _ { 7 }$ for tightness of delivery date. $C _ { 1 } , C _ { 2 } , C _ { 3 }$ are SNTs, and $C _ { 4 }$ through $C _ { 7 }$ are PNTs. In Figure 1, both PNTs and SNTs are interrelated with appropriate causality values +1 $\mathrm { o r } - 1$ . By referring to Figure 1, the adjacency matrix E is derived as follows:

$$
\boldsymbol {E} = \left( \begin{array}{c c c c c c c} C _ {1} & 0 & 1 & 0 & 0 & 0 & 0 \\ C _ {2} & 0 & 0 & 0 & 1 & 0 & 0 \\ C _ {3} & 1 & 0 & 0 & 1 & 1 & 0 \\ C _ {4} & 1 & 0 & 0 & 0 & 1 & - 1 \\ C _ {5} & 1 & 0 & 0 & 0 & 0 & 0 \\ C _ {6} & - 1 & - 1 & 0 & 0 & 0 & 0 \\ C _ {7} & 0 & 0 & 0 & - 1 & 0 & 1 \end{array} \right)
$$

With this adjacency matrix, we can test the effect of “order quantity” $( C _ { 4 } )$ on all the other concepts in a CM by setting the fourth concept node of the first concept node vector $C _ { 1 }$ to be 1 as follows:

$$
\boldsymbol {C} _ {1} = \left( \begin{array}{c c c c c c c} 0 & 0 & 0 & 1 & 0 & 0 & 0 \end{array} \right).
$$

Multiplying this by E, we get the second concept node vector $C _ { 2 }$

$$
\begin{array}{r l}\boldsymbol {C} _ {1} \times \boldsymbol {E}&= (1 0 0 0 1 - 1 0) \rightarrow (1 0 0 0 1 0 0) \text {   inference   } 1\\&(1 0 0 1 1 0 0) = C _ {2}\end{array}
$$

The arrow indicates the threshold operation using 0.5 as a threshold value [38, 70], which is the most popular in the CM-based inference process [34, 70]. We can use different values for a threshold instead of 0.5, but the same results with the same meaning will be derived unless the threshold values lie in the interval [–1,1]. Under the 0.5 threshold, if a causality coefficient is less than 0.5, then it becomes 0, otherwise, it is equal to 1. Applying 0.5 threshold to the result of $C _ { 1 } \times E$ yields inference result 1, which is not the same as $C _ { 1 }$ . Therefore, we need to design the second concept node vector $C _ { 2 } ,$ which contains $C _ { 4 } = 1$ because we are testing the effect of “order quantity” $\ ' ( C _ { 4 } )$ . Then the inference results 2 and 3 are derived as follows:

$$
\begin{array}{r l}\boldsymbol {C} _ {2} \times \boldsymbol {E}&= (2 1 0 0 1 - 1 0) \rightarrow (1 1 0 0 1 0 0) \text {   inference   } 2\\&(1 1 0 1 1 0 0) = C _ {3}\end{array}
$$

$$
\begin{array}{c}\boldsymbol {C} _ {3} \times \boldsymbol {E} = (2 1 0 0 1 - 1 1) \rightarrow (1 1 0 0 1 0 1) \text { inference } 3\\(1 1 0 1 1 0 1) = C _ {4}.\end{array}
$$

Still, inference result 3 is not identical with inference result 2, so that we have to compute $C _ { 4 }$ by inserting $C _ { 4 } = 1$

$$
\boldsymbol {C} _ {4} \times \boldsymbol {E} = (2 1 0 0 1 0 1) \rightarrow (1 1 0 0 1 0 1) \text { inference } 4
$$

Finally, we reach the state of equilibrium where inference 4 equals inference 3. As a result, the inference result 4 or $( 1 , 1 , 0 , 0 , 1 , 0 , 1 )$ is a fixed point of the CM dynamic system described in Figure 1, with respect to a given stimulus “order quantity $( C _ { 4 } ) =$ $1 . ^ { \circ }$ The CM (or TAKBN) depicted in Figure 1 can be used to perform reasoning jobs such as this. The final concept node vector of the inference result $^ { 4 , }$ an equilibrium state of the CM (or TAKBN) depicted in Figure 1 with respect to a given question “What if order quantity $( C _ { 4 } )$ increases with causality $+ 1 ? { } ^ { , }$ contains additional information about four concept nodes such as intention to order $\left( \mathbf { C } _ { 1 } \right)$ , production $( \mathbf { C } _ { 2 } ) ,$ favorableness of payment condition $( \mathbf { C } _ { 5 } ) _ { : }$ , and tightness of delivery date $( C _ { 7 } )$ , all of which have value 1 in the inference result 4. The result may be well interpreted in this way: An increase of order quantity $( C _ { 4 } )$ contributes to improving payment condition from the seller (favorableness of payment condition $\displaystyle [ C _ { 5 } ] )$ because the increased amount of order quantity allows the seller to give the buyer some discount or more generous payment terms, and in turn buyer’s intention to order from that seller (intention to order $\left[ C _ { 1 } \right] )$ will also improve. Production activity will also be motivated (production $\left[ C _ { 2 } \right] )$ because more raw materials are procured from that seller due to the increased intention to order. However, the activated production activity requires more raw materials on time, which will make the delivery date much tighter (tightness of delivery date $\lbrack C _ { 7 } ] )$ . After all, we can identify the composite effects of order quantity $( C _ { 4 } )$ on the other possibly related factors including intention to order $( C _ { 1 } )$ through the forward-evolved inference.

## Appendix D. Questionnaire for Assessment of Decision Performance

WE WOULD LIKE TO REQUEST YOUR voluntary participation in this brief survey, the purpose of which is to test and assess decision performance using the proposed framework in this study. Your responses will remain completely anonymous, and will be used only for the sake of academic purpose. Thank you for your participation.

(ex) How to use rating scales:

<table><tr><td>Strongly disagree</td><td></td><td></td><td>Neutral</td><td></td><td></td><td>Strongly agree</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr></table>

By circling the 6, you would be saying that you agree quite a lot with the given statement.

## Confidence in Decision Quality

DP1: I am not confident about my solution regarding the new B2B negotiation problem. (R)

DP2: I am not sure my solution to the new B2B negotiation problem was appropriate. (R)

## Positive Affect Toward the Decision Process

DP3: Solving the new B2B negotiation problem was interesting.

DP4: I am pleased with the approach used to solve the new B2B negotiation problem.

DP5: Solving the new B2B negotiation problem was frustrating. (R)

## Perceived Adequacy of the Decision Process

DP6: I may have missed important things in the new B2B negotiation problem. (R)

DP7: I really felt lost in trying to solve the new B2B negotiation problem. (R)

## Perceived Satisfaction with Expenditure of Time and Effort

DP8: It took too much time to solve the new B2B negotiation problem. (R)

DP9: The approach used to solve the new B2B negotiation problem was not worth the effort. (R)

## Perceived Acceptability of Solution

DP10: People in the new B2B negotiation problem who would be affected by my solution would probably be satisfied with it.

DP11: I could easily justify my solution.

## Perceived Process Structure

DP12: The approach taken to solving the new B2B negotiation problem was very structured.

DP13: My analysis of the new B2B negotiation problem was systematic.
