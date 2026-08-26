---
otero_id: 13752
otero_key: "7UXEDW9K"
title: "Consensus-based intelligent group decision-making model for the selection of advanced technology"
authors: "A.K. Choudhury; Ravi Shankar; M.K. Tiwari"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Consensus-based intelligent group decision-making model for the selection of advanced technology

A.K. Choudhury<sup>a</sup>, Ravi Shankar<sup>b,\*</sup>, M.K. Tiwari<sup>a</sup>

<sup>a</sup>Department of Manufacturing Engineering, National Institute of Foundry and Forge Technology, Hatia, Ranchi, 834 003, India

<sup>b</sup>Department of Management Studies, Indian Institute of Technology Delhi, Hauz Khas New Delhi, 110 016, India

Received 2 June 2004; received in revised form 21 January 2005; accepted 5 May 2005 Available online 11 July 2005

## Abstract

Consensus forming is a critical process in the present day computer assisted group decision-making (GDM) scenario. Most of the GDM problems are of strategic dimensions and get complicated due to their multi-criteria framework involving many subjective and quantitative factors. In this research, a technology selection problem has been considered for a manufacturing company. The problem has been modeled into a multi-person, multi-criteria and multi-preference scenario. Various preference modes have been transformed into Fuzzy Preference Relations. A soft consensus based group decision-making under linguistic assessments has been adopted here to eliminate the role of a moderator. To incorporate the offline/online characteristics in the re-evaluation phase of the discussion, a multi-agent system (MAS) based negotiation model is proposed to resolve a technology selection problem.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Soft consensus; Proximity measure; Consensus measure; Negotiation; Multi-agent structure

## 1. Introduction

A firm’s ability to make good decisions is particularly important in the face of increasing global competition, and the greater uncertainty from exposure to more number of competitors. Hence, quality and timely decision-making is essential for the success of any firm. In order to do so, today’s organizations prefer groups or teams to take part in the key decisionmaking process. Better cooperation and collaboration among the groups drives an organization towards perfection. Further, working in a group provides a wide range of advantages by sharing information, generating ideas, making decisions, and reviewing the effects of the decisions. Ideally, the group will reach a <sup>b</sup>better<sup>Q</sup> decision than an individual because the collective knowledge and skill of the group is greater than an individual. Individual accountability is also dispersed in a group-decision-making scenario. Optimal utilization of the time and resources is a key element sought by any decision-making group. Various researchers have focused their attention on increasing the ability of the group to make the quality decisions [3,4,7,15,16,22–24,27,33].

Traditional face-to-face discussion suffers from a number of disadvantages such as slower group activities, less satisfying, and ultimately poorer decisions. Today’s communication software meant for aiding the group discussion process tend to decrease the aforementioned demerits. With the exponential growth in the Internet, the present day computer-supported asynchronous meetings are increasingly used to complement or replace the traditional group meetings in both corporate and educational environments. These systems can help conflicting groups move from disagreement to consensus. Also, a group member can opine whenever s/he is physically present or has a useful input. Hence, the participation is not limited to specific times and places. In addition, the Decision Makers are free from temporal and geographical constraints as they do not have to be on the system simultaneously to send or receive the messages.

The quest for lower operating costs and better manufacturing efficiency have forced large number of manufacturing firms to embark on Advanced Manufacturing Technology (AMT) projects. The recent developments in AMT at various organizational levels can be attributed to numerous benefits that improve the competitive position of the adopting companies. This has led to increase in the demand for computerized automation of production systems. A natural outcome of this phenomenon is evident from the fact that mass production has been replaced in some cases by low volume, and high-variety production. Therefore, AMTs have a profound effect on the organization, its infrastructure, functional relationships, and business strategies [2,6,9,8,29,32,36,38,39,49].

However, some AMT acquisition proposals are rejected as a result of failing to satisfy financial justification measures. As acquisition and naturalization of AMT involve a very high level of investment, its payback period is longer than that for a traditional manufacturing technology. This leads to the possible rejection of the project by the various Decision Makers, as they tend to become conservative in nature. In this connection, Decision Makers at the strategic level generally hesitate from investing in AMT because of the existing difficulties in justification of the investment by means of just traditional economic analysis. To overcome this dilemma, an adequate evaluation method which can assist decision-makers in selecting a technology best suited to their operations and business objectives, needs to be employed. Therefore, to map the complexities involved in the organizational decision-making in selecting the AMT, there is a need for a proper decision-making framework so that it encompasses the nature of the planning involved and responsiveness towards the requisite modifications in an existing system.

Keeping in view, the strategic nature of the selection of Advanced Manufacturing Technology (AMT) in any manufacturing organization, there arises a need to develop a model that involves the top management of the company. Taking cue from the aforementioned advantages of the asynchronous group decision-making arrangement, a framework has been developed to incorporate a multi-person decision-making scenario in the AMT selection.

The general ignorance regarding the introduction and implementation of AMT leads to the decisions purely based on the economic analysis [40,42,43]. As a result, many new projects have been curtailed [42]. Under these circumstances, an analytic evaluation method such as Analytical Hierarchy Process (AHP) could be applied to assess the non-financial or intangible aspects of AMT [35]. The main reason for the wide application of AHP lies in its ability to capture more intangible information, and its capability to handle other measures and effects. Through analytic evaluation, the company’s situation can be reflected realistically, more factors and subjective judgments can be taken into account, and hence the situation can be fully understood by knowledge managers or decision makers [34]. However, AHP also has several shortcomings. The major criticisms being (i) lack of theoretical framework to model decision problems into a hierarchy; (ii) use of subjective judgments in making pair wise comparisons; (iii) use of the Eigen Vectors method for estimating relative weights, and (iv) lack of formal treatment of risks.

In this paper, a multi-criteria, multi-person, multipreference consensus based methodology has been adopted to select the appropriate AMT for the business organization. Here, various factors (viz. strategic, technological, and social) having long-term impact on the organization as a whole are considered by the corporate level in the company for the selection of appropriate AMT.

Although, asynchronous group decision-making (GDM) process has several advantages associated with them, they face an inherent difficulty in consensus forming among the solution alternatives provided by the various Decision Makers (DMs). In this regard, a novel approach has been proposed by Herrera et al. [17]. They have introduced the concept of soft consensus measure to incorporate the dynamic and iterative group decision discussion process and also have substituted the role of a moderator. Thus, it paves the way to map the human effects in the computerized decision support systems.

In the proposed approach, different preference structures (viz. Multiplicative Preference Structures, Fuzzy Preference Relations, Utility Functions, and Preference Ordering of the alternatives) have been taken into consideration by the various DMs. However, Fuzzy Preference Relationships have been utilized for homogenizing the various preferences. The reason for using the fuzzy relationships in the subjective evaluation is to incorporate the uncertainty in the decision opined by a particular decision maker [26,53]. Also, decision-making becomes difficult when the available information is incomplete or imprecise. The decision mechanism is also constrained by the uncertainty inherent in the determination of the relative importance of each sub-criterion.

Owing to the proliferation of Internet and e-commerce, offline/online characteristics have also been considered in the proposed methodology. This caters the need for developing an effective methodology for the Decision Makers situated at the geographically sparse locations. Further, these Decision Makers may have conflicting views regarding the selection of AMT [26,45]. Therefore, there arises the need for an intelligent opinion correcting mechanism, which will not only drive the discussion phase towards consensus but will also consider the fact that in the re-evaluation phase of the discussion, the Decision Makers can join at any point of time. Hence, there arises a need to implement a negotiation based methodology in the re-evaluation phase.

To incorporate the above-mentioned features, an agent based framework has been developed to facilitate the negotiation based consensus forming among the group of decision makers having different preference structures [18,25]. Agents based systems have proved as a helpful mechanism for the coordination of people who are performing a given task. Agent interaction protocols govern the exchange of a series of messages among agents (a conversation) [1]. Here, each DM’s opinion is transmitted by an agent. Therefore, these agents are autonomous in nature, and work in a negotiation atmosphere. In order to cater to the above situation, a negotiation based model has been adopted in this paper to reach consensus in the selection of AMT.

This paper investigates the feasibility of applying a multi-preference consensus based methodology in the AMT selection for a manufacturing company and to introduce the group decision-making in tune with the recent analytical approach. In Section 2, the problem environment has been addressed. The various criteria and sub-criteria significant in the selection of AMTs have been identified and explained. A background to the solution methodology has been given in the Section 3. Here, we have given the justification and explained the implementation of Multi-agent Systems (MAS). In Section 4, we have elicited the methodology and represented it in the form of an algorithm. Section 5, incorporates a numerical example from the original problem for explaining the solution methodology. In the last section, we conclude our results and identify the technology selected.

In the next section, we elicit the various factors affecting the selection of AMT.

## 2. Problem environment

Adoption of advanced manufacturing technology (AMT) involves a major investment and a high degree of uncertainty and, hence, warrants considerable attention within a manufacturing firm at the strategic level [6,15]. Therefore, process involving selection and implementation assumes greater importance. Various researchers reported the guidelines for the selection and implementation of the AMT and identified the key issues like technical problems, market dynamics, insufficient knowledge and attention from organization in not getting the benefits from the adoption of the same [9,8,29,35,36,38]. The crux of the problem lies not so much on the level of technology, but rather in its implementation [42]. They also state that, instead of rushing to invest in AMT, a manufacturing company must reassess its direction, strengths and weakness, and then develop a strategy for its successful implementation [32]. Thus, there arises a need for the identification of the factors affecting the selection and also thorough understanding of the various issues required for the implementation of AMT. Various factors have been identified and are classified as strategic factors, technological factors and social factors. They are elicited as follows:

## 2.1. Strategic factors

These factors have long-term impacts on the organization as a whole. The effects of the AMT on the manufacturing strategy for a company are reflected in decisions such as replacement with improved technology, plant expansion, plant modernization, etc. A comprehensive list of the various criteria that falls under strategic factors have been dealt with and given in Table 1. We view strategic effects as the significant repercussions of the AMT on different functional areas of the organization.

## 2.2. Technological factors

These factors are not as wide as strategic factors, but are limited to the capabilities of the AMT to improve the manufacturing performances. Flexibility and quality are the critical sub aspects under this category. Table 2 lists the criteria contributing to technological factors that are used in the problem.

Table 1  
Indicators of the various sub-factors of the <sup>b</sup>strategic factor<sup>Q</sup>

<table><tr><td>Strategic factors</td><td>Indicators</td></tr><tr><td>Financial position</td><td>Required finance, available finance, methods of finance</td></tr><tr><td>Infrastructural position</td><td>Improvement, modernization, expansion</td></tr><tr><td>Market position</td><td>Market share, new products/markets</td></tr><tr><td>Human resource management</td><td>Management development, training and education, job placements programme, manpower planning</td></tr></table>

Table 2  
Indicators of the various sub factors of the <sup>b</sup>Technological factor<sup>Q</sup>

<table><tr><td>Technological factors</td><td>Indicators</td></tr><tr><td>R &amp; D</td><td>Product design and development</td></tr><tr><td>Manufacturing engineering and planning</td><td>Process design, improvement, scheduling</td></tr><tr><td>Flexibility</td><td>Adaptive ability</td></tr><tr><td>Reliability</td><td>Failure, downtime</td></tr><tr><td>Maintainability</td><td>Number of suppliers, supplier Support, availability of technology</td></tr></table>

## 2.3. Social factors

Automated technologies are associated with job losses in the minds of workers and are assumed to cause a large-scale unemployment. Even though this effect is true to some extent, especially where there is a large degree of automation, automated technologies also offer newer job opportunities. They offer better working conditions with respect to safety, hygiene, and ergonomics. The criteria contributing to social factors that have been used to illustrate the model are summarized in Table 3. Fig. 1 shows the hierarchy for the AMT selection problem. The first level of the hierarchy shows that the overall goal is to select the best AMT. At the second level, we observe the three factors (strategic, technological and social) which would contribute to the achievement of the overall goal. At the third level, we have sub criteria that play a vital role in the contribution of each factor. Finally, at the fourth level, we have the three decision alternatives (CAD, CAD–CAM, CAD-FMM) that can contribute to each criterion in a unique way. On the basis of their characteristics, they have been short listed by the Decision Makers. Few of the attributes pertaining to each of the considered AMT are as follows:

## 2.4. CAD (Computer aided design)

This alternative can improve the speed of design and drawing processes.

<sup>!</sup> It can support and aid in performing electromagnetic analysis and mechanical design and engineering analysis.

Table 3  
Indicators of the various sub factors of the <sup>b</sup>Social factor<sup>Q</sup>

<table><tr><td>Social factors</td><td>Indicators</td></tr><tr><td>Personnel policies for employees</td><td>Training and education, deployment</td></tr><tr><td>Working environment</td><td>Safety, hygiene, ergonomics</td></tr><tr><td>Environmental</td><td>Pollution, depletion of natural resources, deterioration with time</td></tr></table>

## 2.5. CAD-CAM (Computer aided design–Computer aided Manufacturing)

<sup>!</sup> This alternative consists of the CAD system which performs all the functions described earlier and in addition it performs NC part programming.

<sup>!</sup> CAM replaces 90% of the operations in the machine shop by NC machine tools.

<sup>!</sup> The alternative demands huge investment and rigorous training to the operators.

## 2.6. CAD-FMM (Computer aided design-Flexible manufacturing modules)

<sup>!</sup> The CAD system has an additional feature of database access through GT codes.

<sup>!</sup> This alternative greatly improves the flexibility of the manufacturing process.

<sup>!</sup> The machines are linked by management controlled computer, thus greatly improving the adaptability of the manufacturing operations.

![](/api/attachments/7UXEDW9K/fulltext/images/e146d54cb274cf1f85ddd99ad40c38264340e331ceeafa45c1f5139e30e23a73.jpg)  
Fig. 1. Represents the hierarchy for the technology selection problem.

The aforementioned underscored factors are now captured to draft the various criteria and sub-criteria and are used to formulate an appropriate model for selecting the desired AMT for a manufacturing company. Fig. 1 represents the model depicting the hierarchy identified by the experts for the selection of the technology for their company.

In the next section, we elicit the background of our proposed methodology.

## 3. Background of solution methodology

In this section, we propose a framework of the multiagent system (MAS) to map the consensus group decision-making (GDM) model for selecting the AMT of a manufacturing company. Prior to introducing MAS in the GDM, we present the background of the consensus based multi-person, multi-preference and multi-criteria group decision-making model [3,4,16,17,19–21]. Here, we have incorporated the concept of soft consensus measure, owing to its closer resemblance to real life. GDM is a dynamic and iterative process in nature and is coordinated with the help of a moderator. The moderator helps the experts to readjust their opinions so as to reach an accepted level of consensus. In the proposed work, an intelligent Negotiator agent has replaced the role of a human moderator.

In this paper, group decision makers are free to express their preferences in four different ways. We have considered here Decision Makers having sizeable experience in the field of AMT selection. Each one expresses his preferences in a unique way. Various ways of expressing the opinions are: Preference Ordering of the alternatives, Fuzzy Preference Relation, Multiplicative Preference Relation and Utility Functions. Thus, a need arises for different preference structures to be standardized in a single preference structure [10–12]. We have considered the fuzzy preference as our base to uniform the information as it incorporates the uncertainty in the decision by the particular decision maker. It is rather a powerful tool if we want to aggregate the individual expert’s opinion into group preferences. The information is smoothened out utilizing the various transformation functions [13]. Once the information has been homogenized, then we apply a selection process that includes: i) aggregation and ii) exploitation. In the aggregation phase, a collective fuzzy preference relationship is calculated by incorporating the individual fuzzy preference relations and it indicates the global/consensus preference between every ordered pair of alternatives according to the majority of experts’ opinion in one round of discussion. The aggregation operation is carried out by means of an OWA operator. Details related to the OWA operator has been dealt with in Appendix A. The same can be done using other aggregation techniques. However, considering the inherent advantages associated with the OWA operators, we have utilized it to carry out the job. A detailed comparison of the operators vis-a\`-vis to the OWA operators is given in Appendix B.

The concept of fuzzy linguistic quantifiers that represents the concept of fuzzy majority, is used to calculate the weighting vector to facilitate the aggregation process. Linguistic quantifiers are defined as Q and their range is given symbolically by (a,b). The most common linguistic fuzzy quantifiers used are <sup>b</sup>most<sup>Q</sup>, <sup>b</sup>at least half<sup>Q</sup>, and <sup>b</sup>as many as possible<sup>Q</sup>. Their ranges are given as (.3,.8), (0,.5) and (.5,1), respectively.

In the exploitation phase, we transform the global/ consensus information about the alternatives into global/consensus ranking, from which the set of solution alternatives are obtained for a particular round of discussion. The same is done with the individual fuzzy preference relations of the various Decision Makers. In this case, we have applied the <sup>b</sup>Quantifier Guided Dominance Degree<sup>Q</sup> (QGDD) that quantifies the dominance the individual alternative has over all others in a fuzzy majority sense. This QGDD can easily replace the Eigen vectors calculated in the method of AHP. The details related to the QGDD are given in Appendix A.

Now, we present an overview of the Consensus model for the Multiperson Decision Making (MPDM) problems with different preference structures based on two soft consensus criteria: 1) Consensus Measure, which indicates the agreement among the experts opinions. It is calculated by comparing the individual solutions with the collective solution, where comparison is done on the basis of positions of the alternatives in the aforementioned solutions. Neat OWA is utilized to calculate the same [31,50]. Details related to Neat OWA are given in Appendix C. 2) a measure of the proximity, to find out how far the individual opinions are from the group opinion. The Measure of

Proximity is also calculated by comparing the individual solutions with the global/consensus solution. Here also, the comparison is done on the basis of positions of the alternatives in the individual as well as collective solution.

In the proposed system, consensus building process is supervised by the Consensus Measure until the end solution is obtained, whereas the Proximity Measure is employed to support the discussion phase of the consensus process. The group decision makers determine the consensus level (CL), required for the solution in advance. When the consensus measure reaches this level, the decision-making session is finished and the solutions are obtained [4]. If that is not the case, the DMs lying below a prefixed proximity level will be asked to change their views. To do this, a feedback mechanism has been applied. We propose that these re-evaluations would be resolved via negotiations. The processes of buying and selling goods have inspired us to incorporate an agent-based negotiation model in the feedback mechanism [18,28,37,1]. A concept of maximum number of rounds called MC (Maximum Cycle) is also incorporated in the consensus model to avoid the delayed convergence of collective solution after several rounds of discussion. To further clarify this point, maximum cycle concept prevents endless rounds of discussion to reach the consensus [4]. In reality, this process is similar to the one used in qualitative forecasting models such as Delphi Method and Executive Consensus Committee. The Fig. 2 elicits the consensus model discussed above.

In Fig. 3, we have described the negotiation mechanism in the reevaluation phase of the process.

After developing the consensus model for the various levels of criteria in Fig. 1 (i.e., strategic factors, technical factors, social factors), we consider a problem of selecting an advanced technology in a manufacturing company. Three potential manufacturing technologies were short listed for the evaluation and subsequently one of these would be selected to meet the company’s objective. In the next subsection, we put forth the MAS in the aforementioned GDM model.

![](/api/attachments/7UXEDW9K/fulltext/images/d90395775a08e8412797e96398c23803333d3e65b4d1e2df5adb0766f2b83a4b.jpg)  
Fig. 2. The schematic illustration of the consensus process.

![](/api/attachments/7UXEDW9K/fulltext/images/1de443d2db47436c8164628cf822db0d1315d12dd5484e844226920e0b09c542.jpg)  
Fig. 3. Diagrammatic representation of the consensus reaching process in an agent based group decision-making.

## 3.1. MAS Architecture

The MAS consists of heterogeneous types of agent, which implement some functionality of the consensus-based group decision-making for a multi-person, multi-preference and multi-criteria scenario. All of these heterogeneous agents have some understanding of the system ontology and use Agent Communication Language (ACL) to establish a conversation. Proposed work has been implemented in Knowledge Query and Knowledge Language (KQKL), which was first proposed by the Foundation for Intelligent Physical Agents/Agent Communication Language (FIPAACL) [28].

To emulate the realistic situations, we have introduced the negotiation model in the feedback mechanism. We have assumed that each expert is not aware of the individual solution set of other experts and is also unaware of the temporary Consensus Solution generated in each round. In addition, we have also used the fact that <sup>b</sup>models with complete information have difficulty explaining strikes or wars, but with passage of time an uninformed player can learn the type of the informed player by observing what offers are made or rejected<sup>Q</sup>. Here, each player is the DM and the prices offered in each round of discussions are the solution sets offered to the DMs lying below a fixed priori. In order to get close to the negotiation model, various solution sets are presented before the concerned DM. If he accepts it, then his solution set is the same as what he accepts, otherwise negotiation fails. The same process shifts to other DMs lying below the fixed priori. After the negotiation is over, again the Consensus Measure and Proximity Measure are enumerated. On the basis of prefixed conditions, it is judged whether to initiate the re-evaluation phase or not.

The agents presented in our model are heterogeneous in nature and posses varied interests and goals. It consists of a society of intermediary agents viz. DM agents, Consensus agent, Negotiator agent and Manager agent. They use a blackboard database as a central repository. The feature and function of the test bed include enabling the Decision Makers to post decisions according to their choice based on their ideas, attitude, motivations and personality. It also:

<sup>!</sup> Provides the framework to calculate Consensus Measure and Proximity Measure in a round of discussion and post it on the blackboard for the further use of the Negotiator agent.

<sup>!</sup> Facilitates the Consensus agent to post the consensus preference pertaining to one round and the Proximity Measure of the various DM agents on the blackboard.

<sup>!</sup> Enables the Negotiator agent to identify the Decision Makers for the process of re-evaluation.

<sup>!</sup> Offers the ground to post the final weights calculated related to each of the alternatives by the Manager agent.

The aforementioned features are bolstered by a society of heterogeneous agents described below:

Decision Maker Agent—Decision Maker agents provide the user interface for the decision makers to the aforementioned test bed. They can post/ change the preferences with the decision makers consent on the blackboard. They are also responsible to inform their respective DMs about the likely negotiation process with the Negotiator agent.

Consensus Agent—This agent calculates the Consensus Measure, Degree of Proximity, and the Proximity Measure in a round of discussion. It posts the order of the DMs based on the Proximity Measure of that round on the test bed. When the required consensus is reached, it calculates the consensus solution and informs the DM agents about the final solution and the end of the discussion phase.

Negotiator Agent— This agent identifies the Decision Maker agent for the negotiation process on the basis of a fixed proximity level. It starts the negotiation with the DMs having Proximity Measure lying just below the fixed priori. The Negotiator agent informs the DM agent just below the fixed level about the review of their opinions. In turn, the DM agent informs the concerned DM, if he/she is present. Otherwise, it informs when he/she would be present. Negotiator agent offers three prices (solution alternatives) to the DMs lying below the fixed priori. They are as follows:

<sup>!</sup> As the first price, it offers the temporary collective solution of that round to the underscored DMs.

<sup>!</sup> Next, it offers the solution alternative of the DM lying just below the consensus solution.

<sup>!</sup> Then Negotiator agent proposes the solution alternative of the DM lying just above the fixed priori.

It depends on the DMs whether to accept the three prices offered by the Negotiator agent, otherwise the negotiation ends after the three prices are offered. On completion of the negotiation process with the concerned DM Negotiator agents proceeds to the next underscored DM and thus the process goes on. Manager Agent: The rounds of discussion concerning each level of hierarchy is initiated by the Manager agent. It informs the DM agents to ask their respective DMs to post their opinions. As the consensus is reached in a level of hierarchy, it initiates the discussion for the next level. After all the rounds have been discussed, it finally incorporates the QGDD associated with each sub-criteria and calculates the final weights intended for each AMT and informs the decision makers about the final outcome. Black Board Database: The blackboard accepts 1) opinions from the DM agents before fresh round of discussion and after the negotiation phase 2) the Con.- sensus Measure and the ascending order of the DMs based on the Proximity Measure. It is also used to provide the position of the various DMs on the basis of the Proximity Measure to the Negotiator agent.

## 3.2. Protocol for various agents

While the test bed provides an electronic infrastructure for the DM agents, Consensus agent, Negotiator agent and Manager agent, the protocol specifies the interactions and negotiations between the negotiation agent and DMs. The protocol specifies the interactions and negotiations between the Negotiator agent and the DMs. The protocol for the society of agents is as follows:

1) DM agents put forward the opinions of the various DMs on the test bed. When the Negotiator agent contacts any one of them to reevaluate their respective DMs’ opinion, then in turn it informs its respective DM. If the DM is present, it informs the Negotiator agent about his/her presence; otherwise, system allows for waiting period till his/her availability. After the negotiation process is over, it again posts the opinion presented by the DM on the test bed for the consideration in the next round of discussion.

2) The Consensus agent homogenizes all the preference structure into a fuzzy preference relation and calculates the Consensus Measure and the Proximity measure. It also posts the order of the various DMs on the basis of their Proximity Measure. Later, when the Consensus Measure reaches or exceeds the desired level, then it informs the Manager agent to convey about the completion of the discussion and put forward the consensus solution of the discussion.

3) Negotiator agent identifies the DM agents lying below the fixed level. It asks the concerned DM agents to inform their respective DMs. When the respective DM agents inform the availability of their respective DMs to the Negotiator agent, it initiates the negotiation process. It offers the various prices (stands) to the DMs as the negotiation price. In any adverse case, the concerned DM may opt out of the negotiation process.

4) After the negotiation process is over and the underscored agents have posted their preference on the test bed, the Negotiator agent informs the Consensus agent to calculate the Consensus Measure and Proximity Measure again. If the Consensus Measure satisfies the fixed level, it informs the Manager agent about the completion of the discussion and the consensus preferences of that round is presented to the Manager agent, who in turn informs the various DMs. Otherwise, the same process is repeated. The final QGDD (after consensus is reached) associated to one level of hierarchy is captured by the Manager agent for the calculation of final weights related to each AMT.

5) Manager agent informs the respective DMs via their agents to express their opinions about the next level of hierarchy after the consensus has been reached for one level of hierarchy. Finally, when the consensus is reached among all levels of hierarchy, the weights of each AMT is calculated. The AMT garnering the highest weight is selected and the chosen alternative is informed to each DM via their agents.

A framework developed to model the interaction of the various agents is given in Fig. 4.

We consider here a problem regarding the selection of AMT of a manufacturing company and demonstrate how the proposed model can be applied. Three potential technologies are short listed for the evaluation process and subsequently one of them would be selected by the company. In the next section, we elicit the solution methodology in an algorithmic form and assign the various steps of the algorithm to the responsible agents.

## 4. Solution methodology

The solution methodology of the proposed model has been described in the algorithmic form to lay down the steps involved in the consensus based decision-making process. The algorithm explaining the solution methodology is as follows:

## 4.1. Algorithm

## 4.1.1. Work envelope for DM agent

1) Generate the different preference structures of the respective Decision Makers i.e. (Preference Ordering of the alternatives, Fuzzy Preference Relations, Multiplicative Preference Relation and Utility Functions). They are represented as follows: Preference Ordering of alternatives as $\mathrm { O } ^ { i }$ , Fuzzy preference Relation as ${ \mathrm { K } } ^ { i } { \mathrm { , } }$ , where $K ^ { i } \subset X \times X$ with membership function $\mu _ { \mathrm { k i } } \colon { \cal X } \times { \cal X } { \longrightarrow } [ 0 , 1 ]$ , and $\mu _ { \mathrm { k i } } ( x _ { \mathrm { s } } , x _ { \mathrm { m } } ) { = } k _ { \mathrm { s m } } ^ { \mathrm { i } }$ where $X = \{ x _ { 1 } , \ldots , x _ { \mathrm { n } } \}$ be a finite set of alternatives: Multiplicative Preference Relation as $A ^ { i } ,$ , where $A ^ { i } \subset \bar { X } \times X , A ^ { i } = a _ { \mathrm { s m } } ^ { i } )$ , where $a _ { \mathrm { s m } } ^ { i }$ indicates a ratio of the preference intensity of alternative $x _ { \mathrm { s } }$ to $x _ { \mathrm { m } } .$ . It is rated in a 1 to 9 scale, Utility functions are represented as $U ^ { i }$ where DM<sup>i</sup> (ith Decision Maker) represents his preferences on X as set of n utility values $U ^ { i } = \{ U _ { \mathrm { s } } ^ { i } , $ $s = 1 , . . . , n ) , \ U _ { \mathrm { s } } ^ { i } \varepsilon [ 0 , 1 ]$ . The opinions given by the respective DMs in the abovementioned ways are passed on to the DM agent.

## 4.1.2. Work envelope for Consensus Agent

2) Available information is transformed into fuzzy preference relationship by different transformation functions. The transformation functions are given in Appendix D.

3) Aggregate the individual fuzzy relations using the OWA operator $\phi _ { \mathrm { Q } }$ for getting the collective preference relationship.

$$
k _ {\mathrm{sm}} ^ {i} = \phi_ {\mathrm{Q}} \big (k _ {\mathrm{sm}} ^ {l}, \ldots , k _ {\mathrm{sm}} ^ {l} \big) = \sum_ {i = 1} ^ {\mathrm{m}} W _ {i} \cdot k _ {\mathrm{sm}} ^ {i}\tag{1}
$$

where Q is fuzzy linguistic quantifier that represents the concept of fuzzy majority and it is used to calculate the weighting vector of $\phi _ { \mathrm { Q } }$ 4 $W { = } ( w _ { 1 } , . . . . , w _ { n } )$ such that $w _ { j } \mathrm { ~ \varepsilon ~ } [ 0 , 1 ]$ and $\textstyle \sum _ { j = 1 } ^ { n } W _ { j } = { \hat { 1 } }$ . We have utilized the <sup>b</sup>most<sup>Q</sup> linguistic quantifier, defined by parameters $^ { ( \mathrm { a } , \mathrm { b } ) }$ as $( . 3 , ~ . 8 )$ . A background related to OWA is detailed in Appendix B.

$$
Q (r) = \left\{ \begin{array}{l} 0, i f r <   a \\ (r - a) / (b - a), i f a \leq r \leq b \\ 1, i f r > b \end{array} \right.\tag{2}
$$

(4) Calculate Quantifier guided dominance degree (QGDD) of the alternative $x _ { \mathrm { s } }$ to quantify the dominance of the alternative $x _ { \mathrm { s } }$ over others for the individual DM solutions as well as collective solution in a round of discussion.

$$
\mathrm{QGDD} _ {s} = \phi_ {\mathrm{Q}} \left(k _ {\mathrm{sm}} ^ {c}, s = 1, \dots , n\right)\tag{3}
$$

(5) Enumerate $Z ^ { c }$ (position of alternatives in the collective solution) and $Z ^ { s }$ (position of alternatives in the individual solutions) based on the QGDD calculated.

(6) Estimate the degree of proximity of each DM with respect to each sub-criteria, called $k _ { \mathrm { s } } ~ ( x _ { \mathrm { m } } )$ by comparing the position of that sub-criteria in the Decision Maker’s individual solution and the collective solution set by using a function.

![](/api/attachments/7UXEDW9K/fulltext/images/8a49add3a6a7514abc9b9a765c2411b0184e59d55069507a0de55c72e5e21e5f.jpg)  
Fig. 4. Agent architecture.

$$
k ^ {i} (x _ {\mathrm{m}}) = \left[ | Z _ {\mathrm{m}} ^ {c} - Z _ {\mathrm{m}} ^ {s} | / (n - 1) \right] ^ {b}\tag{4}
$$

where $b \in ( 0 , 1 )$

Here b controls the rigorousness of the consensus process. We have selected b = 1 in this model.

(7) Calculate the degree of consensus of all Decision Maker’s on each alternative $x _ { \mathrm { m } }$ using the following expression:

$$
R (x _ {\mathrm{m}}) = 1 - \sum_ {i = 1} ^ {m} k ^ {i} (x _ {\mathrm{m}}) / m\tag{5}
$$

(8) Estimate the Consensus Measure $R _ { X }$ using the neat OWA.

$$
R _ {X} = \text { neat   OWA } \left\{R (x _ {j}) \right\}\tag{6}
$$

$$
w _ {s} = \frac {x _ {s} ^ {\alpha}}{\sum_ {s} x _ {s} ^ {\alpha}}, \text { where } \sum_ {s = 1} ^ {n} w _ {s} = 1
$$

(9) Calculate the Proximity Measure of sth Decision Maker’s (DM) using the neat OWA, and is symbolized as $Y _ { X } ^ { S }$

$$
Y _ {X} ^ {S} = 1 - \text {   neat   OWA } (\{K _ {s} (x _ {m}) \})\tag{7}
$$

(10) If $R _ { X } { > } \mathrm { C L }$ , tabulate the QGDD linked to the various criteria and sub-criteria. Otherwise, go to Step 11.

(11) Pick the Decision Makers (DMs) below a fixed level g and pass the information to the Negotiator agent regarding the negotiation based feedback mechanism.

## 4.1.3. Working envelope of negotiation agent

12) Incorporate the aforementioned negotiation model.

## 4.1.4. Working envelope of manager agent

(13) If number of rounds of discussion<sup>N</sup>MC (Maximum Cycle), stop.

Tabulate the QGDD of all the sub-criteria and criteria.

(14) Calculate the priority weights for each subcriteria.

(15) Append all the final priority weights with respect to each alternative manufacturing system and inform the DM agents about the selected alternative.

Now, we present a numerical example eliciting the details of the solution methodology to explain the working of our model. We have applied the same to other criteria affecting the selection of the AMT.

## 5. Numerical example

To bring forth the multi-person scenario, six DMs have been considered for the selection of AMT in our proposed model. Here, we have picked up a small portion of the hierarchy to explain the model and the same has been done with the other criteria and sub-criteria, the results have been captured and have been further used to enumerate the final calculations. The global weights of the various attributes are tabulated in Table 8. Based on these global weights the alternative AMT securing the highest weights is being selected.

The DMs present their views on the various criteria and sub-criteria in four different ways. $\mathrm { D M } ^ { 1 }$ presents his view in Multiplicative Preference Relation on a scale of 1 to 9 as discussed in the algorithm; $\mathrm { D M } ^ { 2 }$ expresses his view in Fuzzy Preference Relation, $\mathrm { D M } ^ { 3 }$ puts across his views in Utility functions, $\mathrm { { ^ { D M } } ^ { 4 } }$ presents his views in Preference Ordering of the alternatives, $\mathrm { D M } ^ { 5 }$ opines also in Preference Ordering of the alternatives and $\mathrm { D M } ^ { 6 }$ puts forward his opinions in Utility functions. Their preferences are given as:

<table><tr><td rowspan="13"> $DM^1$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td></td></tr><tr><td>1</td><td>1</td><td>0.25</td><td>0.33</td><td>0.42</td><td>5.08</td><td>5.08</td><td>1.00</td><td>0.14</td><td>0.13</td><td>5.08</td><td>6.06</td><td>9.00</td></tr><tr><td>2</td><td>4</td><td>1.00</td><td>2.02</td><td>5.08</td><td>3.00</td><td>2.02</td><td>0.20</td><td>0.11</td><td>0.11</td><td>6.06</td><td>5.08</td><td>6.91</td></tr><tr><td>3</td><td>3</td><td>0.42</td><td>1.00</td><td>3.00</td><td>0.33</td><td>0.20</td><td>0.17</td><td>0.14</td><td>0.13</td><td>5.08</td><td>3.00</td><td>6.91</td></tr><tr><td>4</td><td>2</td><td>0.20</td><td>0.33</td><td>1.00</td><td>3.00</td><td>1.00</td><td>0.20</td><td>0.17</td><td>0.14</td><td>1.00</td><td>2.02</td><td>0.20</td></tr><tr><td>5</td><td>0</td><td>0.33</td><td>3.00</td><td>0.33</td><td>1.00</td><td>0.20</td><td>0.25</td><td>0.14</td><td>0.11</td><td>0.33</td><td>0.20</td><td>1.00</td></tr><tr><td>6</td><td>0</td><td>0.42</td><td>5.08</td><td>1.00</td><td>5.08</td><td>1.00</td><td>3.00</td><td>0.33</td><td>0.20</td><td>3.00</td><td>2.02</td><td>6.91</td></tr><tr><td>7</td><td>1</td><td>5.08</td><td>6.06</td><td>5.08</td><td>4.08</td><td>0.33</td><td>1.00</td><td>0.33</td><td>0.14</td><td>2.02</td><td>1.00</td><td>5.08</td></tr><tr><td>8</td><td>6</td><td>9.00</td><td>6.91</td><td>6.06</td><td>6.91</td><td>3.00</td><td>3.00</td><td>1.00</td><td>0.20</td><td>7.89</td><td>5.08</td><td>9.00</td></tr><tr><td>9</td><td>7</td><td>9.00</td><td>7.89</td><td>6.91</td><td>9.00</td><td>5.08</td><td>6.91</td><td>5.08</td><td>1.00</td><td>5.08</td><td>6.06</td><td>7.89</td></tr><tr><td>10</td><td>0</td><td>0.17</td><td>0.20</td><td>1.00</td><td>3.00</td><td>0.33</td><td>0.42</td><td>0.13</td><td>0.20</td><td>1.00</td><td>4.08</td><td>6.06</td></tr><tr><td>11</td><td>0</td><td>0.20</td><td>0.33</td><td>0.42</td><td>5.08</td><td>0.42</td><td>1.00</td><td>0.20</td><td>0.17</td><td>0.25</td><td>1.00</td><td>6.91</td></tr><tr><td>12</td><td>0</td><td>0.14</td><td>0.14</td><td>0.17</td><td>1.00</td><td>0.14</td><td>0.20</td><td>0.11</td><td>0.13</td><td>0.17</td><td>0.14</td><td>1.00</td></tr></table>

<table><tr><td rowspan="13"> $DM^{2}$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>1</td><td>.5</td><td>.18</td><td>.25</td><td>.3</td><td>.87</td><td>.87</td><td>.5</td><td>.05</td><td>.03</td><td>.87</td><td>.91</td></tr><tr><td>2</td><td>.82</td><td>.5</td><td>.66</td><td>.87</td><td>.75</td><td>.66</td><td>.13</td><td>0</td><td>0</td><td>.91</td><td>.87</td></tr><tr><td>3</td><td>.75</td><td>.3</td><td>.5</td><td>.75</td><td>.25</td><td>.13</td><td>.09</td><td>.05</td><td>.03</td><td>.87</td><td>.75</td></tr><tr><td>4</td><td>.66</td><td>.13</td><td>.25</td><td>.5</td><td>.75</td><td>.5</td><td>.13</td><td>.09</td><td>.05</td><td>.5</td><td>.66</td></tr><tr><td>5</td><td>.13</td><td>.25</td><td>.75</td><td>.25</td><td>.5</td><td>.13</td><td>.18</td><td>.05</td><td>0</td><td>.25</td><td>.13</td></tr><tr><td>6</td><td>.13</td><td>.3</td><td>.87</td><td>.5</td><td>.87</td><td>.5</td><td>.75</td><td>.25</td><td>.13</td><td>.75</td><td>.66</td></tr><tr><td>7</td><td>.5</td><td>.87</td><td>.91</td><td>.87</td><td>.82</td><td>.25</td><td>.5</td><td>.25</td><td>.05</td><td>.66</td><td>.5</td></tr><tr><td>8</td><td>.94</td><td>1</td><td>.94</td><td>.91</td><td>.94</td><td>.75</td><td>.75</td><td>.5</td><td>.13</td><td>.97</td><td>.87</td></tr><tr><td>9</td><td>.97</td><td>1</td><td>.97</td><td>.94</td><td>1</td><td>.87</td><td>.94</td><td>.87</td><td>.5</td><td>.87</td><td>.91</td></tr><tr><td>10</td><td>.13</td><td>.09</td><td>.13</td><td>.5</td><td>.75</td><td>.25</td><td>.3</td><td>.03</td><td>.13</td><td>.5</td><td>.82</td></tr><tr><td>11</td><td>.09</td><td>.13</td><td>.25</td><td>.3</td><td>.87</td><td>.3</td><td>.5</td><td>.13</td><td>.09</td><td>.18</td><td>.5</td></tr><tr><td>12</td><td>0</td><td>.05</td><td>.05</td><td>.09</td><td>.5</td><td>.05</td><td>.13</td><td>0</td><td>.03</td><td>.09</td><td>.05</td></tr></table>

DM<sup>3</sup> [.45, .536, .363, .369, .238, .545, .587, .77, .896, .349, .339, .121].  
DM<sup>4</sup> [5, 6, 8, 7, 11, 4, 2, 3, 1, 9, 10, 12].  
DM<sup>5</sup> [8, 9, 6, 7, 11, 4, 10, 12, 1, 5, 2, 3].  
DM<sup>6</sup> [.66, .7, .6, .4, .238, .545, .75, .77, .896, .349, .339, .121].  
The Consensus Agent transforms the various forms of opinion into Fuzzy Preference Relation using the transformation functions given in Appendix D. The transformed value for the above tables is as follows:

<table><tr><td rowspan="13"> $DM^{1}$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>1</td><td>.5</td><td>.18</td><td>.25</td><td>.3</td><td>.87</td><td>.87</td><td>.5</td><td>.05</td><td>.03</td><td>.87</td><td>.91</td></tr><tr><td>2</td><td>.82</td><td>.5</td><td>.66</td><td>.87</td><td>.75</td><td>.66</td><td>.13</td><td>0</td><td>0</td><td>.91</td><td>.87</td></tr><tr><td>3</td><td>.75</td><td>.3</td><td>.5</td><td>.75</td><td>.25</td><td>.13</td><td>.09</td><td>.05</td><td>.03</td><td>.87</td><td>.75</td></tr><tr><td>4</td><td>.66</td><td>.13</td><td>.25</td><td>.5</td><td>.75</td><td>.5</td><td>.13</td><td>.09</td><td>.05</td><td>.5</td><td>.66</td></tr><tr><td>5</td><td>.13</td><td>.25</td><td>.75</td><td>.25</td><td>.5</td><td>.13</td><td>.18</td><td>.05</td><td>0</td><td>.25</td><td>.13</td></tr><tr><td>6</td><td>.13</td><td>.3</td><td>.87</td><td>.5</td><td>.87</td><td>.5</td><td>.75</td><td>.25</td><td>.13</td><td>.75</td><td>.66</td></tr><tr><td>7</td><td>.5</td><td>.87</td><td>.91</td><td>.87</td><td>.82</td><td>.25</td><td>.5</td><td>.25</td><td>.05</td><td>.66</td><td>.5</td></tr><tr><td>8</td><td>.94</td><td>1</td><td>.94</td><td>.91</td><td>.94</td><td>.75</td><td>.75</td><td>.5</td><td>.13</td><td>.97</td><td>.87</td></tr><tr><td>9</td><td>.97</td><td>1</td><td>.97</td><td>.94</td><td>1</td><td>.87</td><td>.94</td><td>.87</td><td>.5</td><td>.87</td><td>.91</td></tr><tr><td>10</td><td>.13</td><td>.09</td><td>.13</td><td>.5</td><td>.75</td><td>.25</td><td>.3</td><td>.03</td><td>.13</td><td>.5</td><td>.82</td></tr><tr><td>11</td><td>.09</td><td>.13</td><td>.25</td><td>.3</td><td>.87</td><td>.3</td><td>.5</td><td>.13</td><td>.09</td><td>.18</td><td>.5</td></tr><tr><td>12</td><td>0</td><td>.05</td><td>.05</td><td>.09</td><td>.5</td><td>.05</td><td>.13</td><td>0</td><td>.03</td><td>.09</td><td>.05</td></tr><tr><td rowspan="14"> $DM^{2}$ </td><td colspan="12"></td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>1</td><td>.5</td><td>.18</td><td>.25</td><td>.3</td><td>.87</td><td>.87</td><td>.5</td><td>.05</td><td>.03</td><td>.87</td><td>.91</td></tr><tr><td>2</td><td>.82</td><td>.5</td><td>.66</td><td>.87</td><td>.75</td><td>.5</td><td>.66</td><td>.13</td><td>0</td><td>.91</td><td>.87</td></tr><tr><td>3</td><td>.75</td><td>.3</td><td>.5</td><td>.75</td><td>.25</td><td>.13</td><td>.09</td><td>.05</td><td>.03</td><td>.87</td><td>.75</td></tr><tr><td>4</td><td>.66</td><td>.13</td><td>.25</td><td>.5</td><td>.75</td><td>.5</td><td>.13</td><td>.09</td><td>.05</td><td>.5</td><td></td></tr><tr><td>5</td><td>.13</td><td>.25</td><td>.75</td><td>.25</td><td>.5</td><td>.13</td><td>.18</td><td>.05</td><td>0</td><td>.25</td><td>.13</td></tr><tr><td>6</td><td>.13</td><td>.3</td><td>.87</td><td>.5</td><td>.87</td><td>.5</td><td>.75</td><td>.25</td><td>.13</td><td>.75</td><td>.66</td></tr><tr><td>7</td><td>.4</td><td>.87</td><td>.91</td><td>.87</td><td>.82</td><td>.25</td><td>.5</td><td>.25</td><td>.05</td><td>.66</td><td>.5</td></tr><tr><td>8</td><td>.94</td><td>1</td><td>.94</td><td>.91</td><td>.94</td><td>.75</td><td>.75</td><td>.5</td><td>.13</td><td>.97</td><td>.87</td></tr><tr><td>9</td><td>.97</td><td>1</td><td>.97</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>.13</td><td>.09</td><td>.13</td><td>.5</td><td>.75</td><td>.25</td><td>.3</td><td>.03</td><td>.13</td><td>.5</td><td>.82</td></tr><tr><td>11</td><td>.09</td><td>.13</td><td>.25</td><td>.3</td><td>.87</td><td>.3</td><td>.5</td><td>.13</td><td>.09</td><td>.18</td><td>.5</td></tr><tr><td>12</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan="13"> $DM^3$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td></td></tr><tr><td>1</td><td>0.50</td><td>0.41</td><td>0.61</td><td>0.60</td><td>0.78</td><td>0.41</td><td>0.37</td><td>0.25</td><td>0.20</td><td>0.62</td><td>0.64</td><td>0.93</td></tr><tr><td>2</td><td>0.59</td><td>0.50</td><td>0.69</td><td>0.68</td><td>0.84</td><td>0.49</td><td>0.45</td><td>0.33</td><td>0.26</td><td>0.70</td><td>0.71</td><td>0.95</td></tr><tr><td>3</td><td>0.39</td><td>0.31</td><td>0.50</td><td>0.49</td><td>0.70</td><td>0.31</td><td>0.28</td><td>0.18</td><td>0.14</td><td>0.52</td><td>0.53</td><td>0.90</td></tr><tr><td>4</td><td>0.40</td><td>0.32</td><td>0.51</td><td>0.50</td><td>0.71</td><td>0.31</td><td>0.28</td><td>0.19</td><td>0.15</td><td>0.53</td><td>0.54</td><td>0.90</td></tr><tr><td>5</td><td>0.22</td><td>0.16</td><td>0.30</td><td>0.29</td><td>0.50</td><td>0.16</td><td>0.14</td><td>0.09</td><td>0.07</td><td>0.32</td><td>0.33</td><td>0.79</td></tr><tr><td>6</td><td>0.59</td><td>0.51</td><td>0.69</td><td>0.69</td><td>0.84</td><td>0.50</td><td>0.46</td><td>0.33</td><td>0.27</td><td>0.71</td><td>0.72</td><td>0.95</td></tr><tr><td>7</td><td>0.63</td><td>0.55</td><td>0.72</td><td>0.72</td><td>0.86</td><td>0.54</td><td>0.50</td><td>0.37</td><td>0.30</td><td>0.74</td><td>0.75</td><td>0.96</td></tr><tr><td>8</td><td>0.75</td><td>0.67</td><td>0.82</td><td>0.81</td><td>0.91</td><td>0.67</td><td>0.63</td><td>0.50</td><td>0.42</td><td>0.83</td><td>0.84</td><td>0.98</td></tr><tr><td>9</td><td>0.80</td><td>0.74</td><td>0.86</td><td>0.85</td><td>0.93</td><td>0.73</td><td>0.70</td><td>0.58</td><td>0.50</td><td>0.87</td><td>0.87</td><td>0.98</td></tr><tr><td>10</td><td>0.38</td><td>0.30</td><td>0.48</td><td>0.47</td><td>0.68</td><td>0.29</td><td>0.26</td><td>0.17</td><td>0.13</td><td>0.50</td><td>0.51</td><td>0.89</td></tr><tr><td>11</td><td>0.36</td><td>0.29</td><td>0.47</td><td>0.46</td><td>0.67</td><td>0.28</td><td>0.25</td><td>0.16</td><td>0.13</td><td>0.49</td><td>0.50</td><td>0.89</td></tr><tr><td>12</td><td>0.07</td><td>0.05</td><td>0.10</td><td>0.10</td><td>0.21</td><td>0.05</td><td>0.04</td><td>0.02</td><td>0.02</td><td>0.11</td><td>0.11</td><td>0.50</td></tr><tr><td rowspan="13"> $DM^4$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td></td></tr><tr><td>1</td><td>0.50</td><td>0.55</td><td>0.64</td><td>0.59</td><td>0.77</td><td>0.45</td><td>0.36</td><td>0.41</td><td>0.32</td><td>0.68</td><td>0.73</td><td>0.82</td></tr><tr><td>2</td><td>0.45</td><td>0.50</td><td>0.59</td><td>0.55</td><td>0.73</td><td>0.41</td><td>0.32</td><td>0.36</td><td>0.27</td><td>0.64</td><td>0.68</td><td>0.77</td></tr><tr><td>3</td><td>0.36</td><td>0.41</td><td>0.50</td><td>0.45</td><td>0.64</td><td>0.32</td><td>0.23</td><td>0.27</td><td>0.18</td><td>0.55</td><td>0.59</td><td>0.68</td></tr><tr><td>4</td><td>0.41</td><td>0.45</td><td>0.55</td><td>0.50</td><td>0.68</td><td>0.36</td><td>0.27</td><td>0.32</td><td>0.23</td><td>0.59</td><td>0.64</td><td>0.73</td></tr><tr><td>5</td><td>0.23</td><td>0.27</td><td>0.36</td><td>0.32</td><td>0.50</td><td>0.18</td><td>0.09</td><td>0.14</td><td>0.05</td><td>0.41</td><td>0.45</td><td>0.55</td></tr><tr><td>6</td><td>0.55</td><td>0.59</td><td>0.68</td><td>0.64</td><td>0.82</td><td>0.50</td><td>0.41</td><td>0.45</td><td>0.36</td><td>0.73</td><td>0.77</td><td>0.86</td></tr><tr><td>7</td><td>0.64</td><td>0.68</td><td>0.77</td><td>0.73</td><td>0.91</td><td>0.59</td><td>0.50</td><td>0.55</td><td>0.45</td><td>0.82</td><td>0.86</td><td>0.95</td></tr><tr><td>8</td><td>0.59</td><td>0.64</td><td>0.73</td><td>0.68</td><td>0.86</td><td>0.55</td><td>0.45</td><td>0.50</td><td>0.41</td><td>0.77</td><td>0.82</td><td>0.91</td></tr><tr><td>9</td><td>0.68</td><td>0.73</td><td>0.82</td><td>0.77</td><td>0.95</td><td>0.64</td><td>0.55</td><td>0.59</td><td>0.50</td><td>0.86</td><td>0.91</td><td>1.00</td></tr><tr><td>10</td><td>0.32</td><td>0.36</td><td>0.45</td><td>0.41</td><td>0.59</td><td>0.27</td><td>0.18</td><td>0.23</td><td>0.14</td><td>0.50</td><td>0.55</td><td>0.64</td></tr><tr><td>11</td><td>0.27</td><td>0.32</td><td>0.41</td><td>0.36</td><td>0.55</td><td>0.23</td><td>0.14</td><td>0.18</td><td>0.09</td><td>0.45</td><td>0.50</td><td>0.59</td></tr><tr><td>12</td><td>0.18</td><td>0.23</td><td>0.32</td><td>0.27</td><td>0.45</td><td>0.14</td><td>0.05</td><td>0.09</td><td>0.00</td><td>0.36</td><td>0.41</td><td>0.50</td></tr><tr><td rowspan="13"> $DM^5$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td></td></tr><tr><td>1</td><td>0.50</td><td>0.55</td><td>0.41</td><td>0.45</td><td>0.64</td><td>0.32</td><td>0.59</td><td>0.68</td><td>0.18</td><td>0.36</td><td>0.23</td><td>0.27</td></tr><tr><td>2</td><td>0.45</td><td>0.50</td><td>0.36</td><td>0.41</td><td>0.59</td><td>0.27</td><td>0.55</td><td>0.64</td><td>0.14</td><td>0.32</td><td>0.18</td><td>0.23</td></tr><tr><td>3</td><td>0.59</td><td>0.64</td><td>0.50</td><td>0.55</td><td>0.73</td><td>0.41</td><td>0.68</td><td>0.77</td><td>0.27</td><td>0.45</td><td>0.32</td><td>0.36</td></tr><tr><td>4</td><td>0.55</td><td>0.59</td><td>0.45</td><td>0.50</td><td>0.68</td><td>0.36</td><td>0.64</td><td>0.73</td><td>0.23</td><td>0.41</td><td>0.27</td><td>0.32</td></tr><tr><td>5</td><td>0.36</td><td>0.41</td><td>0.27</td><td>0.32</td><td>0.50</td><td>0.18</td><td>0.45</td><td>0.55</td><td>0.05</td><td>0.23</td><td>0.09</td><td>0.14</td></tr><tr><td>6</td><td>0.68</td><td>0.73</td><td>0.59</td><td>0.64</td><td>0.82</td><td>0.50</td><td>0.77</td><td>0.86</td><td>0.36</td><td>0.55</td><td>0.41</td><td>0.45</td></tr><tr><td>7</td><td>0.41</td><td>0.45</td><td>0.32</td><td>0.36</td><td>0.55</td><td>0.23</td><td>0.50</td><td>0.59</td><td>0.09</td><td>0.27</td><td>0.14</td><td>0.18</td></tr><tr><td>8</td><td>0.32</td><td>0.36</td><td>0.23</td><td>0.27</td><td>0.45</td><td>0.14</td><td>0.41</td><td>0.50</td><td>0.00</td><td>0.18</td><td>0.05</td><td>0.09</td></tr><tr><td>9</td><td>0.82</td><td>0.86</td><td>0.73</td><td>0.77</td><td>0.95</td><td>0.64</td><td>0.91</td><td>1.00</td><td>0.50</td><td>0.68</td><td>0.55</td><td>0.59</td></tr><tr><td>10</td><td>0.64</td><td>0.68</td><td>0.55</td><td>0.59</td><td>0.77</td><td>0.45</td><td>0.73</td><td>0.82</td><td>0.32</td><td>0.50</td><td>0.36</td><td>0.41</td></tr><tr><td>11</td><td>0.77</td><td>0.82</td><td>0.68</td><td>0.73</td><td>0.91</td><td>0.59</td><td>0.86</td><td>0.95</td><td>0.45</td><td>0.64</td><td>0.50</td><td>0.55</td></tr><tr><td>12</td><td>0.73</td><td>0.77</td><td>0.64</td><td>0.68</td><td>0.86</td><td>0.55</td><td>0.82</td><td>0.91</td><td>0.41</td><td>0.59</td><td>0.45</td><td>0.50</td></tr><tr><td rowspan="13"> $DM^{6}$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>1</td><td>0.50</td><td>0.47</td><td>0.55</td><td>0.73</td><td>0.88</td><td>0.59</td><td>0.44</td><td>0.42</td><td>0.35</td><td>0.78</td><td colspan="2">0.79</td></tr><tr><td>2</td><td>0.53</td><td>0.50</td><td>0.58</td><td>0.75</td><td>0.90</td><td>0.62</td><td>0.47</td><td>0.45</td><td>0.38</td><td>0.80</td><td colspan="2">0.81</td></tr><tr><td>3</td><td>0.45</td><td>0.42</td><td>0.50</td><td>0.69</td><td>0.86</td><td>0.55</td><td>0.39</td><td>0.38</td><td>0.31</td><td>0.75</td><td colspan="2">0.76</td></tr><tr><td>4</td><td>0.27</td><td>0.25</td><td>0.31</td><td>0.50</td><td>0.74</td><td>0.35</td><td>0.22</td><td>0.21</td><td>0.17</td><td>0.57</td><td colspan="2">0.58</td></tr><tr><td>5</td><td>0.12</td><td>0.10</td><td>0.14</td><td>0.26</td><td>0.50</td><td>0.16</td><td>0.09</td><td>0.09</td><td>0.07</td><td>0.32</td><td colspan="2">0.33</td></tr><tr><td>6</td><td>0.41</td><td>0.38</td><td>0.45</td><td>0.65</td><td>0.84</td><td>0.50</td><td>0.35</td><td>0.33</td><td>0.27</td><td>0.71</td><td colspan="2">0.72</td></tr><tr><td>7</td><td>0.56</td><td>0.53</td><td>0.61</td><td>0.78</td><td>0.91</td><td>0.65</td><td>0.50</td><td>0.49</td><td>0.41</td><td>0.82</td><td colspan="2">0.83</td></tr><tr><td>8</td><td>0.58</td><td>0.55</td><td>0.62</td><td>0.79</td><td>0.91</td><td>0.67</td><td>0.51</td><td>0.50</td><td>0.42</td><td>0.83</td><td colspan="2">0.84</td></tr><tr><td>9</td><td>0.65</td><td>0.62</td><td>0.69</td><td>0.83</td><td>0.93</td><td>0.73</td><td>0.59</td><td>0.58</td><td>0.50</td><td>0.87</td><td colspan="2">0.87</td></tr><tr><td>10</td><td>0.22</td><td>0.20</td><td>0.25</td><td>0.43</td><td>0.68</td><td>0.29</td><td>0.18</td><td>0.17</td><td>0.13</td><td>0.50</td><td colspan="2">0.51</td></tr><tr><td>11</td><td>0.21</td><td>0.19</td><td>0.24</td><td>0.42</td><td>0.67</td><td>0.28</td><td>0.17</td><td>0.16</td><td>0.13</td><td>0.49</td><td colspan="2">0.50</td></tr><tr><td>12</td><td>0.03</td><td>0.03</td><td>0.04</td><td>0.08</td><td>0.21</td><td>0.05</td><td>0.03</td><td>0.02</td><td>0.02</td><td>0.11</td><td colspan="2">0.11</td></tr></table>

Now, the collective Fuzzy Preference Relation to the above homogenized and transformed information is found out. The collective Fuzzy Preference is calculated using OWA operator. The weights used in the aggregation process are (0, 0.07, 0.36, 0.33, 0.27, 0)

<table><tr><td rowspan="13">Collective solution</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td></td></tr><tr><td>1</td><td>0.52</td><td>0.42</td><td>0.53</td><td>0.52</td><td>0.82</td><td>0.55</td><td>0.43</td><td>0.29</td><td>0.20</td><td>0.71</td><td>0.73</td><td>0.89</td></tr><tr><td>2</td><td>0.61</td><td>0.52</td><td>0.64</td><td>0.68</td><td>0.78</td><td>0.51</td><td>0.34</td><td>0.28</td><td>0.19</td><td>0.73</td><td>0.73</td><td>0.86</td></tr><tr><td>3</td><td>0.50</td><td>0.38</td><td>0.52</td><td>0.57</td><td>0.58</td><td>0.28</td><td>0.25</td><td>0.23</td><td>0.14</td><td>0.63</td><td>0.61</td><td>0.82</td></tr><tr><td>4</td><td>0.50</td><td>0.35</td><td>0.46</td><td>0.52</td><td>0.73</td><td>0.40</td><td>0.27</td><td>0.25</td><td>0.16</td><td>0.55</td><td>0.61</td><td>0.62</td></tr><tr><td>5</td><td>0.21</td><td>0.25</td><td>0.45</td><td>0.30</td><td>0.52</td><td>0.17</td><td>0.16</td><td>0.13</td><td>0.04</td><td>0.34</td><td>0.31</td><td>0.60</td></tr><tr><td>6</td><td>0.48</td><td>0.51</td><td>0.75</td><td>0.63</td><td>0.86</td><td>0.52</td><td>0.56</td><td>0.40</td><td>0.28</td><td>0.74</td><td>0.72</td><td>0.91</td></tr><tr><td>7</td><td>0.60</td><td>0.69</td><td>0.78</td><td>0.76</td><td>0.87</td><td>0.47</td><td>0.52</td><td>0.43</td><td>0.28</td><td>0.74</td><td>0.70</td><td>0.91</td></tr><tr><td>8</td><td>0.73</td><td>0.75</td><td>0.80</td><td>0.78</td><td>0.90</td><td>0.63</td><td>0.60</td><td>0.52</td><td>0.32</td><td>0.83</td><td>0.81</td><td>0.93</td></tr><tr><td>9</td><td>0.83</td><td>0.84</td><td>0.89</td><td>0.87</td><td>0.99</td><td>0.75</td><td>0.74</td><td>0.71</td><td>0.52</td><td>0.88</td><td>0.90</td><td>0.99</td></tr><tr><td>10</td><td>0.32</td><td>0.30</td><td>0.40</td><td>0.48</td><td>0.69</td><td>0.29</td><td>0.28</td><td>0.20</td><td>0.15</td><td>0.52</td><td>0.61</td><td>0.80</td></tr><tr><td>11</td><td>0.30</td><td>0.30</td><td>0.42</td><td>0.41</td><td>0.72</td><td>0.30</td><td>0.33</td><td>0.22</td><td>0.13</td><td>0.42</td><td>0.52</td><td>0.80</td></tr><tr><td>12</td><td>0.14</td><td>0.17</td><td>0.21</td><td>0.20</td><td>0.43</td><td>0.12</td><td>0.12</td><td>0.10</td><td>0.04</td><td>0.23</td><td>0.23</td><td>0.52</td></tr></table>

As referred in Step 4 of the Algorithm, <sup>b</sup>Consensus agent<sup>Q</sup> calculated the QGDD concerning all the individual and collective solution sets. We have adopted fuzzy quantifier as many as possible with the pair (.5, 1), and the corresponding OWA operator with the weighting vector is:

W =(0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.17, 0.16, 0.17, 0.17, 0.16, 0.17). <sup>b</sup>Manufacturing engineering and planning<sup>Q</sup> is given the highest consensus priority among the six Decision Makers.

<table><tr><td>DM $^{1}$  [1.07, 1.13, 0.91, 0.73, 0.49, 1.13, 0, 0, 0, 0, 0, 0]</td></tr><tr><td>DM $^{2}$  [1.07, 1.13, 0.91, 0.73, 0.49, 1.13, 0, 0, 0, 0, 0, 0]</td></tr><tr><td>DM $^{3}$  [1.07, 1.15, 0.89, 0.90, 0.53, 1.23, 0, 0, 0, 0, 0, 0]</td></tr><tr><td>DM $^{4}$  [1.16, 1.00, 0.88, 0.97, 0.57, 1.25, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]</td></tr><tr><td>DM $^{5}$  [0.88, 0.74, 1.07, 0.97, 0.57, 1.25, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]</td></tr><tr><td>DM $^{6}$  [1.27, 1.24, 1.19, 0.86, 0.47, 1.11, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]</td></tr><tr><td>Collective Solution [1.12, 1.10, 0.93, 0.91, 0.55, 1.25, 0, 0, 0, 0, 0, 0]</td></tr></table>

DM<sup>6</sup> [1, 2, 3, 5, 6, 4, 7, 7, 7, 7, 7, 7]

DM<sup>5</sup> [4, 5, 2, 3, 6, 1, 7, 7, 7, 7, 7, 7]

Table 4  
Ranking difference of different DMs with respect to the consensus solution

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td> $DM^1$ </td><td>-1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $DM^2$ </td><td>-1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $DM^3$ </td><td>-1</td><td>1</td><td>-1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $DM^4$ </td><td>0</td><td>0</td><td>-1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $DM^5$ </td><td>-2</td><td>-2</td><td>2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $DM^6$ </td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>-3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Table 5  
Proximity measure of the various sub criteria for different DM

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td> $DM^{1}$ </td><td>0.091</td><td>0.091</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td> $DM^{2}$ </td><td>0.091</td><td>0.091</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td> $DM^{3}$ </td><td>0.091</td><td>0.091</td><td>0.091</td><td>0.091</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td> $DM^{4}$ </td><td>0.000</td><td>0.000</td><td>0.091</td><td>0.091</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td> $DM^{5}$ </td><td>0.182</td><td>0.182</td><td>0.182</td><td>0.182</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td> $DM^{6}$ </td><td>0.091</td><td>0.091</td><td>0.091</td><td>0.000</td><td>0.000</td><td>0.273</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr></table>

Now the enumerated positions of the alternatives on the basis of the QGDD are given as follows:

Collective Solution [2, 3, 4, 5, 6, 1, 7, 7, 7, 7, 7, 7]

The Proximity table calculated on the basis of rank difference is given in Table 4 and Table 5.

The degree of consensus related to all experts is calculated using Step 7 in the Algorithm and the results are given in the Table 6.

The Proximity Measure of each expert is calculated using the degree of proximity given in Table 5. The aggregation is carried out with the help of neat OWA. The enumerated results are given in the Table 7.

The Consensus Measure is calculated by using the degree of consensus with the help of neat OWA. The a parameter used here has a value of 0.98. The Consensus Measure of the present round is calculated as 0.97. Since the soft consensus measure is below the company’s fixed level of 0.98, hence there is a need to change the opinions of the Decision Makers lying below a fixed level. The fixed priori set by the model is 0.5. Now the Consensus agent informs the Negotiator agent to start its process of correcting the erroneous DM. Therefore, on the basis of results calculated in Table 7, Negotiator agent identifies $\mathrm { D M } ^ { 5 }$ and $\mathrm { D M } ^ { 6 }$ to change his/her opinion. Negotiator agent first picks $\mathrm { D M } ^ { 6 }$ for the negotiation process. It offers the collective solution of that round to the decision maker, which he doesn’t accepts. Next, the solution alternative of the $\mathrm { D M } ^ { \mathrm { 1 } }$ is presented, which he accepts:

DM<sup>6</sup>: [3, 2, 4, 5, 6, 1, 7, 7, 7, 7, 7, 7].

Table 6  
Degree of consensus of the various sub-criteria

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>0.891</td><td>0.891</td><td>0.909</td><td>0.927</td><td>1.000</td><td>0.945</td><td>1.000</td><td>1.000</td><td>1.000</td><td>1.000</td><td>1.000</td><td>1.000</td></tr></table>

Table 7  
Proximity measure for different decision makers

<table><tr><td> $DM^{1}$ </td><td> $DM^{2}$ </td><td> $DM^{3}$ </td><td> $DM^{4}$ </td><td> $DM^{5}$ </td><td> $DM^{6}$ </td></tr><tr><td>0.58</td><td>0.58</td><td>0.58</td><td>0.58</td><td>0.46</td><td>0.45</td></tr></table>

Table 8  
Final weights for the selection of Advanced Manufacturing Technology

<table><tr><td>Strategic factors</td><td>Strategic factor&#x27;s weight</td><td>CAD</td><td>CAD-CAM</td><td>CAD-FMM</td></tr><tr><td>Financial position</td><td>1.12</td><td>0.37</td><td>0.63</td><td>0.5</td></tr><tr><td>Infrastructural position</td><td>1.10</td><td>0.55</td><td>0.34</td><td>0.55</td></tr><tr><td>Market position</td><td>0.94</td><td>0.275</td><td>0.725</td><td>0.895</td></tr><tr><td>Human resource Management</td><td>0.92</td><td>0.5</td><td>0.5</td><td>0.29</td></tr><tr><td>R &amp; D</td><td>0.56</td><td>0.315</td><td>0.68</td><td>0.58</td></tr><tr><td>Manufacturing engineering and planning</td><td>1.25</td><td>0.315</td><td>0.46</td><td>0.985</td></tr><tr><td>Flexibility</td><td>0.00</td><td>0.3</td><td>0.475</td><td>0.97</td></tr><tr><td>Reliability</td><td>0.00</td><td>0.38</td><td>0.62</td><td>0.765</td></tr><tr><td>Maintainability</td><td>0.00</td><td>0.66</td><td>0.39</td><td>0.18</td></tr><tr><td>Personnel policies for employees</td><td>0.00</td><td>0.42</td><td>0.58</td><td>0.7</td></tr><tr><td>Working environment</td><td>0.00</td><td>0.31</td><td>0.68</td><td>0.6</td></tr><tr><td>Environmental factors</td><td>0.00</td><td>0.31</td><td>0.68</td><td>0.84</td></tr><tr><td>Final Score</td><td></td><td>2.31</td><td>3.17</td><td>3.83</td></tr></table>

Negotiator agent then picks $\mathrm { D M } ^ { 5 }$ for the discussion; it offers the collective solution of that round to the decision maker, which he refuses to accept. Like the case of $\mathrm { D M } ^ { 6 } , ~ \mathrm { D M } ^ { 5 }$ also accepts the solution of $\mathrm { D M } ^ { \mathrm { 1 } }$ . Thus his alternative is: [3, 2, 4, 5, 6, 1, 7, 7, 7, 7, 7, 7].

Further, the Consensus agent again calculates the degree of proximity after the revised preferences is posted and consequently degree of consensus is calculated on the basis of degree of proximity. The consensus measure is calculated for the new round and it is found out to be 0.98. Since this consensus measure is above the fixed level, the discussion would be stopped and this temporary collective solution would be the final consensual solution. The Consensus agent informs the Manager agent about reaching of the consensus. The Manager agent incorporates the QGDD calculated for each sub-criteria and informs the DMs to present their views about other levels of hierarchy. The final consensus solution for the <sup>b</sup>pair wise comparisons of the criteria<sup>Q</sup> is: [2, 3, 4, 5, 6, 1, 7, 7, 7, 7, 7, 7] with a QGDD of [1.12, 1.10, 0.93, 0.91, 0.55, 1.25, 0, 0, 0, 0, 0, 0]. The same has been applied to calculate the impact of different sub-factors on AMTs. Owing to the large number of preference tables involved we have only incorporated the $\mathrm { Q G D D _ { s } }$ related to various sub factors affecting the AMTs. As mentioned in Step 14 of the algorithm, the $\mathrm { Q G D D _ { s } }$ for the comparison of three AMT alternatives with respect to each criterion is incorporated by the Manager agent. The final priority weight of each AMT with respect to each sub-criterion is calculated and given in Table 8.

CAD-FMM is selected and the Manager agent informs the DMs via DM agent about the end of the discussion process and the selection of the technology. In the next section, we conclude our discussion.

## 6. Conclusion

Technology selection in a manufacturing system is an important problem. We first identified three alternatives and then defined several criteria and sub-criteria pertaining to the AMT selection. A multi-criteria, multi-person and multi-preference scenario was modeled for the above system.

The consensus model adopted here presents a decision support system to incorporate offline and online characteristics while the discussion phase. To do ${ \bf s o , }$ this system is based on two soft consensus criteria: 1) a consensus measure and 2) a proximity measure. Consensus measure evaluates the consensus situation at each moment and it is used to guide the consensus process. The proximity measure evaluates how far the individual expert’s opinions are from the collective opinion and it is used to design the feedback mechanism. An agent framework has been incorporated to present the offline/online characteristic as well as the negotiation model in the re-evaluation phase of the discussion.

The methodology presented here, is an intelligent decision support system in the multi-person, multi-criteria and multi-preference scenario. We have incorporated the fuzzy preference relation based approach to handle the uncertainty inherent in the technology selection problem. The model presented here, effectively negotiates the drawback associated with the AHP model.

## Acknowledgement

The Authors wish to express their most sincere thanks to the learned referees for their constructive criticisms that led to considerable improvement in the earlier version of the paper.

## Appendix A. OWA operators

The OWA operator was proposed by Yager [50]. The OWA operators are the special case of the Choquet Integral. They are a family of aggregation operators which have the <sup>b</sup>and<sup>Q</sup> operator at one and the $\ " { } _ { 0 1 } \overrightarrow { } \overrightarrow { } \mathrm { ~ }$ operator at the other extreme.

The OWA operator of dimension n is a function $\phi ,$ $\phi \colon [ 0 , 1 ] ^ { \mathrm { n } } { \longrightarrow } [ 0 , 1 ]$ , that has associated with a set of weights. Let $\{ a _ { 1 } , \ldots . . , a _ { \mathrm { n } } \}$ be a list of values to aggregate, then the OWA operator $\phi$ is defined as

$$
\varphi (a _ {1}, \dots , a _ {m}) = W \times B ^ {T} = \sum_ {j = 1} ^ {m} w _ {j} \cdot b _ {j}\tag{A1}
$$

where $W { = } \left\{ w _ { 1 } , . . . , w _ { n } \right\}$ is a weighting vector, such that $w _ { i } , \varepsilon \left[ 0 , 1 \right]$ and $\textstyle \sum _ { i } W _ { i } = 1$ and B is the associated ordered value vector. Each element $b _ { i } \ \varepsilon \ B$ is the ith largest value in the collection $( a _ { 1 } , . . . , a _ { m } )$

The OWA operators fill the gap between the operators Min and Max. They are commutative, increasing monotonous and idempotent in nature.

A natural question in the definition of the OWA operator is how to obtain the associated weighting vector. There are two approaches to deal with this kind of situation. The first approach is to use some kind of learning mechanism by exploiting the sample data; and the second approach is to try to give some semantics or meaning to the weights.

We are interested in the area of quantifier guided aggregations. Our idea is to calculate the weights for the aggregation operations (made by means of the OWA operator) using linguistic quantifiers that represent the concept of fuzzy majority. In [21] Yager, suggested an interesting way to compute the weights of the OWA aggregation operator using fuzzy quantifiers, which, in the case of a non-decreasing proportional quantifier $\mathcal { Q } ,$ it is given by the expression:

$$
w _ {i} = Q (i / n) - Q ((i - 1) / n), i = 1, \dots , n\tag{A2}
$$

When a fuzzy quantifier $\mathcal { Q }$ is used to compute the weights of the OWA operator $\phi _ { ; }$ , it is symbolized by $\phi _ { Q }$

Now, we discuss the operator used in giving the idea of dominance of the various alternatives, i.e. $\mathrm { Q G D D _ { s } } .$

In order to select the alternatives <sup>b</sup>best<sup>Q</sup> acceptable to the group of individuals as a whole, we will use quantifier guided choice degrees of alternatives, based on the concept of fuzzy majority: a dominance degree. Both of them are based on the concept of OWA operator.

Quantifier Guided Dominance DegreeYFor the alternative $x _ { i } ,$ we compute the quantifier-guided dominance degree $\mathrm { Q G D D _ { s } }$ used to quantify the dominance that one alternative has over all the others in a fuzzy majority senses as follows:

$$
\mathrm{QGDD} _ {s} = \phi_ {Q} \left(p _ {i i} ^ {c}, j = 1, \dots , n, j \neq i\right).\tag{A3}
$$

In the next Appendix, we detail the various aggregation operators and their comparisons with the OWA.

## Appendix B

The choice of the aggregation operator is a tailorcut approach to suit the various situations in which it is applied. Here, we have considered Quasi arithmetic means [5,30], Weighted Median Aggregation [51], Sugeno Integral [30,46] and Leximin Ordering [14,52] in the GDM scenario. The applications and the properties of the various operators vis-a\`-vis OWA operator are given as follows:

<sup>!</sup> Weighted Median OperatorsYThey are less flexible in satisfying various criteria in comparison to the OWA operator. An OWA operator can be determined analytically but they are calculated numerically. Due to non-linearity, it is sometimes difficult to determine the weights to meet the global weights.

<sup>!</sup> Quasi Arithmetic MeansYThese weights are also somewhat problematic in nature, as the obtained weights are decreasing and or like, however an and like operator is obtained from OWA. Although, they are easy to compute and can express global goals, they cannot adequately model interactions (positive or negative) between the criteria. However, the OWA operators are flexible in nature and have the ability to trade-offs between conflicting goals.

<sup>!</sup> Sugeno IntegralY Sugeno integrals are useful to aggregate non-cardinal data, including ordered scores and rankings. They are also easy to compute when a fuzzy measure can be assigned to each rating. However, it is often difficult to determine the measure based on the global goals. They also possess non-linear characteristics.

<sup>!</sup> Leximin OrderingYLeximin ordering can be used in multi-stage problem where the <sup>b</sup>best<sup>Q</sup> scores are obtained from previous stages. Occasionally, the Leximin scores are different from the numerically highest scores.

In the next Appendix, we detail the background related to the neat OWA, which is used to calculate the Consensus Measure and the Proximity Measure.

## Appendix C

For aggregating the preferences, the neat OWA aggregation operator has been used [31]. The operator allows one to aggregate unordered preference values into a value lying between an and and or operators. This operator is more appropriate, since the type of aggregation implicitly desired by the decision maker is neither the pure or nor an and operator.

In this operator, one is allowed to assign a weight which is not fixed, but is as the function of the values to be aggregated. The parameter that corresponds to the weight function, i.e. a´, is a decision parameter. It can be determined based on the experiment and the intended degree of orness or andness of the operator. In our case, we use the weight function that corresponds to the andlike like operator. The neat OWA operator, for X with associated weight $w _ { i } = x _ { i } ^ { \alpha } / \textstyle \sum _ { i } x _ { i } ^ { \alpha }$ , is defined as $\begin{array} { r } { \mathrm { F } \bigl ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } \bigr ) = \sum _ { i } x _ { i } ^ { \alpha + 1 } / \sum _ { i } x _ { i } ^ { \alpha } . } \end{array}$ ; a<sub>z</sub>0 . Thus, by using this kind of weight function, the weights are directly deduced from the values to be aggregated. When a = 0.0 we get a simple average operator. As the a approach infinity, we get a maximum operator.

Next, we detail the various transformation functions used to even the opinions into Fuzzy Preference Relationships.

## Appendix D

As each Decision Maker is characterized by their own ideas, attitudes, motivations and personality, it is quite natural to think that different experts will provide their preferences in different ways. The DMs will provide their preferences in Utility Functions, Preference Ordering of the alternatives, Fuzzy Preference Relation, and Multiplicative Preference Relation [11,12,48,41,44]. The use of Fuzzy Preference Relations in representing an expert’s opinion about set of the alternatives, appears to be a useful tool in modeling decision processes, and is easy to aggregate as far as group preferences are considered. The justification of the various transformation functions utilized for homogenizing the various modes of information into Fuzzy Preference Relationships are as follows:

1. Utility Functions: Here, the DM presents his preferences on X as a set of n utility values $U ^ { i } = \{ u _ { s } ^ { i } ,$ $s = l , . . . , n \} , u _ { s } ^ { i } \varepsilon [ 0 , 1 ] .$ , where $u _ { s } ^ { i }$ represents the utility evaluation given by Decision Maker $\mathrm { D M } ^ { \mathrm { i } }$ to the alternative $x _ { \mathrm { s } } .$ Therefore, the higher the evaluation the better the alternative satisfies the Decision Maker. Any Transformation function must satisfy the following properties [12]:

(i) The transformation function h relating the fuzzy preference relation with the Utility Function for DM<sup>i</sup>, $K _ { \mathrm { s m } } ^ { i } { = } h ( u _ { s } ^ { i } , u _ { m } ^ { i } ) .$ , should depend only on the values of $u _ { s } ^ { i }$ and $u _ { m } ^ { i }$ . This transformation function must satisfy the fact that the more the value of $\dot { u } _ { s } ^ { i }$ the more the $K _ { \mathrm { s m } } ^ { i } ,$ and the more the value of $u _ { m } ^ { i }$ the less the value of $K _ { \mathrm { s m } } ^ { i }$ [11,12,48].

Proof. Function h should obtain the preference of any alternative over any other alternative depending on the value of the quotient between the respective utility values of the alternatives. i.e.

$$
h \left(u _ {s} ^ {i}, u _ {m} ^ {i}\right) = \eta \left(u _ {s} ^ {i} / u _ {m} ^ {i}\right)\tag{A4}
$$

where is a non-decreasing function. This type of transformation function $\eta$ have been studied and further developed by Chiclana et. al. [12]. Here, $u _ { s } ^ { i } / u _ { m } ^ { i }$ is interpreted as a ratio of the preference intensity for $x _ { s }$ to that of $x _ { m } ~ ( i . e . ~ x _ { s } ~ i s ~ u _ { s } ^ { i } / u _ { m } ^ { i }$ times as good as $x _ { m } ,$ , and assuming a reciprocal fuzzy preference relation, a possible transformation function to obtain the intensity of preference of the alternativex $x _ { s }$ over alternative $x _ { m }$ for DM<sup>i</sup>, $K _ { \mathrm { s m } } ^ { i }$ may be defined as

$$
\begin{array}{r l} K _ {\mathrm{sm}} ^ {i} & = \eta^ {1} \left(u _ {s} ^ {i} / u _ {m} ^ {i}\right) = \left(u _ {s} ^ {i} / u _ {m} ^ {i}\right) / \left\{\left(u _ {s} ^ {i} / u _ {m} ^ {i}\right) + \left(u _ {v} ^ {i} / u _ {s} ^ {i}\right) \right\} \\ & = \left(u _ {s} ^ {i}\right) ^ {2} / \left\{\left(u _ {s} ^ {i}\right) ^ {2} + \left(u _ {m} ^ {i}\right) ^ {2} \right\}, s \neq m. \end{array} \tag {A5}
$$

In addition to the above discussion, the Transfor mation function must satisfy certain other properties. They are as follows:

$$
\mathbf {a} h \left(u _ {m} ^ {i}, u _ {s} ^ {i}\right) + h \left(u _ {s} ^ {i}, u _ {m} ^ {i}\right) = 1 \forall u _ {s} ^ {i}, u _ {m} ^ {i} \varepsilon [ 0, 1 ];\tag{A6}
$$

This property deals with the reciprocity condition. [47,48,12].

$$
\mathbf {b} h \left(u _ {s} ^ {i}, u _ {s} ^ {i}\right) = 1 / 2 \forall u _ {s} ^ {i} \varepsilon [ 0, 1 ]\tag{A7}
$$

indicates the indifference of an expert between two alternatives verifying his criterion with the same intensity.

$$
\mathbf {c} h \left(u _ {m} ^ {i}, 0\right) = 1 \forall u _ {m} ^ {i} \varepsilon [ 0, 1 ]\tag{A8}
$$

implies that if Decision Maker has a prior knowledge that an alternative does not satisfy his criterion, then any alternative satisfying his criterion with a positive value should be preferred with the maximum degree of preference, i.e. Unity.

$$
\mathbf {d} h \left(u _ {s} ^ {i}, u _ {m} ^ {i}\right) > 1 / 2 \text {   if   } u _ {s} ^ {i} > u _ {m} ^ {i}. \forall u _ {s} ^ {i}, u _ {m} ^ {i} \varepsilon [ 0, 1 ].\tag{A9}
$$

Finally, property d indicates that between two alternatives, the expert gives a definite preference to the alternative with the higher evaluations over the other.

(ii) As per the need of the utility functions, h(.) has to be non-decreasing in the first and non-increasing in the second argument. A theoretical proof pertaining to the above statement is given as follows:

We assume that

$$
h \left(u _ {s} ^ {i}, u _ {m} ^ {i}\right) = 1 / 1 + d \left(u _ {s} ^ {i}, u _ {m} ^ {i}\right)\tag{A10}
$$

where, d: $[ 0 \times 1 ] \times [ 0 \times 1 ] { \longrightarrow }  { R ^ { + } }$ is a function of same nature as h.(i.e. is non-decreasing in the first, and nondecreasing in the second argument). We express that d is a separable function and the assumption is also based on the fact that the set of utility values are given on the basis of a positive ratio scale. We then have

$$
h \left(u _ {s} ^ {i}, u _ {m} ^ {i}\right) = 1 / \left\{1 + t ^ {\prime} \left(u _ {s} ^ {i}, u _ {m} ^ {i}\right) \times t ^ {\prime \prime} \left(u _ {s} ^ {i}, u _ {m} ^ {i}\right) \right\}\tag{A11}
$$

where $t ^ { \prime }$ and $t ^ { \prime \prime } \ i s \ \varepsilon \ [ 0 , 1 ]$ and have same sign but $t ^ { \prime }$ is non-increasing in the first domain and non-decreasing in the second one and the reverse is true for $t ^ { \prime \prime }$ . Now, from the earlier discussion, we have

$$
t ^ {\prime} \left(u _ {s} ^ {i}\right) \times t ^ {\prime \prime} \left(u _ {m} ^ {i}\right) = 1, \forall u _ {s} ^ {i} \varepsilon [ 0, 1 ]\tag{A12}
$$

Therefore, $t ^ { \prime } = 1 / t ^ { \prime \prime }$ , with $t ^ { \prime \prime } ( t ) { \neq } 0$ for any t belonging to the domain of definition of $t ^ { \prime \prime }$ . But, we also have from property $\mathbf { c } , t ^ { \prime \prime } ( 0 ) { = } 0 ,$ , so that $t ^ { \prime \prime } \colon [ 0 , 1 ] { \longrightarrow } R ^ { + }$ and for $\eta = 0 , \ t ^ { \prime } \left( . \right)$ is not defined, therefore, the expression h transforms into

$$
h \left(u _ {s} ^ {i}, u _ {m} ^ {i}\right) = t ^ {\prime \prime} \left(u _ {m} ^ {i}\right) / \left\{t ^ {\prime \prime} \left(u _ {m} ^ {i}\right) + t ^ {\prime \prime} \left(u _ {s} ^ {i}\right) \right\}\tag{A13}
$$

(iii) The function h(.) should be continuous in nature as it must reflect the changes in the utility valuations $u _ { s } ^ { i } , \ u _ { m } ^ { i } .$ . To validate the above-mentioned propositions, let us consider the following.

$$
h \left(u _ {s} ^ {i}, u _ {m} ^ {i}\right) = \left[ r ^ {\prime} \left(u _ {s} ^ {i}, u _ {m} ^ {i}\right) \right] ^ {2}, \forall u _ {s} ^ {i}, u _ {m} ^ {i} \varepsilon [ 0, 1 ]\tag{A14}
$$

where $r ^ { \prime } ( u _ { s } ^ { i } , u _ { m } ^ { i } ) \varepsilon [ 0 , 1 ]$ . Considering Eq. (A6), we can have the following transformation.

$$
\left[ r ^ {\prime} \left(u _ {s} ^ {i}, u _ {m} ^ {i}\right) \right] ^ {2} + \left[ r ^ {\prime} \left(u _ {m} ^ {i}, u _ {s} ^ {i}\right) \right] ^ {2} = 1, \forall u _ {s} ^ {i}, u _ {m} ^ {i} \varepsilon [ 0, 1 ].\tag{A15}
$$

Since, the above equation can be converted into a parametric equation of two continuous functions (i.e. sine and cosine), hence, the transforming function must be continuous in nature.

2. Preference Ordering of the alternatives: Here, Decision Maker DM<sup>i</sup> provides his preferences on X as an individual preference ordering, $\mathbf { \bar { \boldsymbol { O } } } ^ { \mathrm { i } } = \{ \boldsymbol { o } ^ { \mathrm { i } } \ . . . , \boldsymbol { o } ^ { \mathrm { i } } \ ( \boldsymbol { n } ) \}$ , where $\partial ^ { \mathrm { i } } \left( . \right)$ is a permutation function over the index set $\scriptstyle \{ 1 , \ldots , n \}$ for the DM<sup>i</sup> [10,44,12–14], n is the maximum number of alternatives. Therefore, according to the view point of each DM, an ordered vector of alternatives, from the best one to the worst one is given in the form of Preference Ordering of alternatives. Various theoretical justifications for the properties associated with the transformation function are as follows:

The transformation function must only depend on the values of $o ^ { \mathrm { i } } ( \mathrm { s } )$ and $o ^ { \mathrm { i } } ( \mathrm { m } )$ , i.e.

$$
k _ {\mathrm{sm}} ^ {i} = f \big (o ^ {i} (s), o ^ {i} (m) \big).\tag{A16}
$$

It must be the non-increasing function of the first argument and a non-decreasing function of the second argument. To satisfy, the above conditions of the function f should depend on the difference between the alternatives’ positions. It should give a value of importance or utility to each alternative, in such a way that the lower the position of an alternative, the higher the utility. The preference of the best alternative over the worst alternative is the maximum preference and has a value of unity.

Therefore, the utility associated with an alternative is

$$
u _ {s} ^ {i} = v \big (n - o ^ {i} (s) \big)\tag{A17}
$$

where v is a non-decreasing function. Thus, for

$$
u _ {s} ^ {i} = v \big (n - o ^ {i} (s) \big) = \big (n - o ^ {i} (s) \big) / (n - 1).\tag{A18}
$$

Several researchers like [47,48] have done a considerable work in this regard. However, we have utilized the transformation function adopted by Chiclana et al. [12] to even the rank ordering of the alternatives into fuzzy preference relation.

$$
\begin{array}{l} k _ {\mathrm{sm}} ^ {i} = g ^ {\prime} \left(o ^ {i} (s) - o ^ {i} (m)\right) \\ \qquad = 1 / 2 \bigl \{1 + \bigl (o ^ {i} (m) - o ^ {i} (s) \bigr) / (n - 1) \bigr \}. \end{array}\tag{A19}
$$

Thus, by adopting the above transformation function all the requisite properties are met. Such as: 1: f o<sup>i</sup>ð Þs ; o<sup>i</sup>ð Þ m e ½  0; 1 ; 8 s; m: ðA20Þ

$$
\begin{array}{l} 2. f \big (o ^ {i} (s), o ^ {i} (m) \big) + f \big (o ^ {i} (m), o ^ {i} (s) \big) \\ = 1 ], \forall s, m. \end{array}\tag{A21}
$$

$$
\begin{array}{l} 3. f \big (o ^ {i} (s), o ^ {i} (m) \big) = 1 / 2 i f o ^ {i} (m) \\ = o ^ {i} (s), \forall s, m. \end{array}\tag{A22}
$$

$$
4. f \left(o ^ {i} (s) - o ^ {i} (m)\right) <   1 / 2 \text {   if   } o ^ {i} (s) > o ^ {i} (m), \forall s, m.\tag{A23}
$$

3. Multiplicative Preference Relations: The relationship between multiplicative and fuzzy preference relations is analyzed assuming that a DM provides his preference on X by means of Multiplicative Preference Relation [41], $A ^ { i } { = } [ a _ { \mathrm { s m } } ^ { i } ]$

In general, if

$$
A ^ {\prime} = \left\{A ^ {i} = \left[ a _ {s m} ^ {i} \right] | a _ {\mathrm{sm}} ^ {i} \times a _ {\mathrm{ms}} ^ {i} = 1, a _ {\mathrm{sm}} ^ {i} \varepsilon [ 1 / 9, 9 ] \right\}\tag{A24}
$$

is the set of multiplicative preference relations in Saaty’s sense, and

$$
K ^ {\prime} = \left\{K ^ {i} = \left[ k _ {s m} ^ {i} \right] | k _ {\mathrm{sm}} ^ {i} + k _ {\mathrm{ms}} ^ {i} = 1, k _ {\mathrm{sm}} ^ {i} \varepsilon [ 0, 1 ] \right\}\tag{A25}
$$

is the additive fuzzy preference relations, then we are looking for a continuous function

$$
N: A ^ {\prime} \rightarrow K ^ {\prime}, | F (A ^ {i}) = K ^ {i}, \forall i.\tag{A26}
$$

This class of functions is equivalent to the class of functions verifying

$$
\left. \begin{array}{c} f: [ 1 / 9, 9 ] [ 0, 1 ] \\ f (x) + f (1 / x) = 1 \\ f (9) = 1 \end{array} \right\}\tag{A27}
$$

Function f can be rewritten in the following way: $f ( \mathbf { x } ) { = } 1 / 2 + \mathbf { h } ( \mathbf { x } )$ , which implies that $\operatorname { h } ( \mathbf { x } ) + \operatorname { h } ( 1 / \mathbf { x } ) =$ $0 , \mathrm { h } ( 9 ) { = } 1 / 2$

On the other hand, it is well known that the general solution of functional equation

$$
l (x \times y) = l (x) + l (y) \text {   is   in } [ 1, + \alpha ];\tag{A28}
$$

$$
l (z) = C. \ln z, C \varepsilon R.\tag{A29}
$$

In our situation, the following relationship holds, i.e. $y = 1 / x ,$ , and making $x = 1$ , we have $0 = h \ ( 1 ) + h$ $( 1 ) = 2 \times h ( 1 ) = 2 \times h ( x \times y )$ and therefore, function h verifies $h ( x ) + h ( y ) = h ( x \times y )$ and thus matches the generic equation, Eq. (A24)

$$
h (z) = C \times \ln z, C \varepsilon R
$$

Since $h ( 9 ) = 1 / 2$ , then $\mathrm { C } = 1 / ( 2 \times \ln { 9 } )$ , and therefore $h ( z ) = 1 / 2 \ ( \mathrm { l n } z / \mathrm { l n } 9 )$

## References

[1] Rina Azoulay-Schwartz, Sarit Kraus Negotiation on data allocation in multi-agent Environments, (available at) www. google.com, 1999.

[2] H. Boer, W.E. During, Management of process innovation— the case of FMS: a systems approach, International Journal of Operations and Production Management 25 (4) (1985) 671– 682.

[3] G. Bordogna, M. Fedrizzi, G. Pasi, A linguistic modeling of consensus in group decision-making based on OWA operators, IEEE Transactions on Systems, Man and Cybernetics: Part A. Systems and Humans 27 (1997) 126– 132.

[4] N. Bryson, Group decision-making and the analytic hierarchy process: exploring the consensus-relevant information content, Computers & Operations Research (23) (1996) 27– 35.

[5] P.S. Bullen, D.S. Mitrinovic, P.M. Vasic, Means and Their Inequalities, D. Reidel Publishing Company, Dordrecht, 1988.

[6] J.S. Busby, C.G.C. Pitts, Real options in practice: an exploratory survey of how finance officers deal with flexibility in capital appraisal, Management Accounting Research 40 (13) (1997) 169–186.

[7] C. Carlsson, D. Ehrenburg, P. Eklund, M. Fedrizzi, P. Gustafsson, P. Lindholm, G. Merkuryeva, T. Riissanen, A.G.S. Ventre, Consensus in distributed soft environments, European Journal of Operational Research 61 (1992) 165–185.

[8] N. Chaidmong, C.O’. Brien, Decision support tool for justifying alternative manufacturing and production control systems, International Journal of Production Economics 60–61 (1999) 177– 186.

[9] F.T.S. Chan, M.H. Chan, H. Lau, R.W.L. Ip, Investment appraisal techniques for advanced manufacturing technology (AMT): a literature review, International Journal of Manufacturing Technology and Management 21 (1) (2001) 35–47.

[10] F. Chiclana, F. Herrera, E. Herrera-Viedma, M.C. Payotos, A classification method of alternatives for multiple preference

ordering criteria based on fuzzy majority, Journal of Fuzzy Mathematics (1996) 4.

[11] F. Chiclana, F. Herrera, E. Herrera-Viedma, Preference Relations as the Information Representation Base in Multiperson Decision-Making, Proc. 6th International Conference on Information Processing and Management of Uncertainty in Knowledge Based Systems, vol. 1, Granada, 1996, pp. 459 – 464.

[12] F. Chiclana, F. Herrera, E. Herrera-Viedma, Integrating three representative models in fuzzy multipurpose decision-making based on fuzzy preference relations, Fuzzy Sets and Systems 97 (1998) 277– 291.

[13] G.B. Devedzie, E. Pap, Multi-criteria-multistages linguistic evaluation and ranking of machine tools, Fuzzy Sets and Systems 102 (1999) 451 – 461.

[14] D. Dubois, H. Fargier, H. Prade, Refinements of the maximin approach to decision-making in a fuzzy environment, Fuzzy Sets and Systems 81 (1996) 103–122.

[15] A. Efstathiadsea, S. Tassoub, A. Antoniouc, Strategic planning, transfer and implementation of advanced manufacturing technologies (AMT), Technovation 22 (4) (2002) 210– 212.

[16] F. Herrera, E. Herrera-Viedma, J.L. Verdegray, A model of consensus in group decision-making under linguistic assessments, Fuzzy Sets and Systems 78 (1996) 73– 87.

[17] E. Herrera-Viedma, F. Herrera, F. Chiclana, A consensus model for multiperson decision-making with different preference structures, IEEE Transactions on Systems, Man and Cybernetics 32 (2002) 394– 402.

[18] M. Jarke, Knowledge sharing and negotiation support in multiperson decision support systems, Decision Support Systems 2 (1) (1986) 93– 102.

[19] J. Kacprzyk, Group decision-making with a fuzzy linguistic majority, Fuzzy Sets and Systems (18) (1986) 105–118.

[20] J. Kacprzyk, On some fuzzy cores and soft consensus measures in group decision-making, in: J. Bezdek (Ed.), The Analysis of Fuzzy Information, CRC Press, Boca Raton, FL, 1987, pp. 119– 130.

[21] J. Kacprzyk, M. Fedrizzi, A <sup>d</sup>soft<sup>T</sup> measure of consensus in the setting of partial (fuzzy) preferences, European Journal of Operational Research (34) (1988) 316–325.

[22] J. Kacprzyk, M. Fedrizzi, Multiperson Decision-Making Models Using Fuzzy Sets and Possibility Theory, Kluwer Academic Publishers, Dordrecht, 1993.

[23] J. Kacprzyk, M. Fedrizzi, H. Nurmi, Consensus Under Fuzziness, Kluwer, Norwell, MA, 1997.

[24] E.E. Karsak, Distance-based fuzzy MCDM approach for evaluating flexible manufacturing system alternatives, International Journal of Production Research 40 (13) (2002) 3167– 3181.

[25] G.E. Kersten, A procedure for negotiating efficient and nonefficient compromises, Decision Support Systems 4 (2) (1988) 167– 177.

[26] S. Kotha, P.M. Swamidass, Advanced manufacturing technology use: exploring the effect of the nationality variable, International Journal of Production Research 36 (11) (1998) 3135– 3146.

[27] L.I. Kuncheva, Five measures of consensus in group decisionmaking using fuzzy sets, Proceedings IFSA, 1991, pp. 141– 144.

[28] Sim Kwang Mong, Chan Raymond, A brokering protocol for agent-based e-commerce, IEEE Transactions on Systems, Man and Cybernetics 4 (30) (2000) 473– 474.

[29] S.L. MacDougall, R.H. Pike, Consider your options: changes to strategic value during implementation of advanced manufacturing technology, Omega 31 (1) (2003) 1 – 15.

[30] J.L. Marichal, Aggregation operators for multicriteria decision and PhD Dissertation, University de Liege, 1999.

[31] M. Marimin, M. Umano, I. Hatono, H. Tamura, Hierarchical semi-numeric method for pairwise fuzzy group decision-making, IEEE Transactions on Systems, Man and Cybernetics 5 (32) (2002) 691– 700.

[32] J.R. Meredith, Implementing the automated factory, Journal of Manufacturing Systems (1) (1987) 1 – 13.

[33] L. Mich, L. Gaio, M. Fedrizzi, On fuzzy logic-based consensus in group decision, Proceedings IFSA, 1993, pp. 698–700.

[34] R.P. Mohanty, Analysis of justification problems in CIMS: review and project evaluation, International Journal of Production Planning and Control 4 (3) (1992) 26– 37.

[35] R.P. Mohanty, Sitalakshmi Venkataramen use of the analytic hierarchy process for selecting automated manufacturing systems, International Journal of Operations and Production Man agement 13 (8) (1993) 45–57.

[36] R.P. Mohanty, S.G. Dehmukh, Advanced manufacturing technology selection: a strategic model for learning and evaluation, International Journal of Production Economics 55 (3) (1998) 295–307.

[37] J.F. Nunamaker, A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Electronic meeting systems to support group work: theory and practice at Arizona, Communications of the ACM 34 (7) (1991) 40–61.

[38] S.M. Ordoobadi, N.J. Mulvaney, Development of a justification tool for advanced manufacturing technologies: systemwide benefits value analysis, Journal of Engineering and Technology Management 18 (2) (2001) 157–184.

[39] E. Persentili, S.E. Alptekin, Product flexibility in selecting manufacturing planning and control strategy, International Journal of Production Research 38 (9) (2000) 2011– 2021.

[40] M. Punniyamoorthy, P.V. Ragavan, A strategic decision model for the justification of technology selection, International Journa of Advanced Manufacturing Technology 21 (1) (2003) 72–78.

[41] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[42] B. Saleh, M. Hacker, S. Randhawa, Factors in capital decisions involved in manufacturing technologies, International Journal of Operations and Production Management 21 (10) (2001) 1265–1288.

[43] K.V. Sambasivarao, S.G. Deshmukh, Selection and implementation of advanced manufacturing technologies: Classification and literature review issues, International Journal of Opera tions and Production Management (4) (1995) 47– 62.

[44] F. Seo, M. Sakawa, Fuzzy multi attribute utility analysis for collective choice, IEEE Transactions on Systems, Man and Cybernetics SMC 15 (1985) 45– 53.

[45] S. Sohal, R. Schroder, E. Uliana, W. Maguire, Adoption of AMT by South African manufacturers, Integrated Manufacturing Systems 12 (1) (2001) 15–34.

[46] M. Sugeno. Theory of Fuzzy Integrals and its Applications, PhD thesis, Tokyo Institute of Technology, Tokyo, 1974.

[47] T. Tanino, Fuzzy preference relations in group decision-making, in: J. Kacprzyk, M. Roubens (Eds.), Non-Conventional Preference Relations in Decision-Making, Springer, Berlin, 1988, pp. 54– 71.

[48] T. Tanino, On group decision-making under fuzzy preferences. Multiperson decision-making using fuzzy sets and possibility theory, Kluwer, Norwell, MA, 1990.

[49] J.W. Troxler, L.M. Blank, Decision support system for value analysis of integrated manufacturing technology, in: H. Parsaei, T. Ward, W. Karwoski (Eds.), Justification Methods for Integrated Manufacturing Systems, Elsevier, New York, NY, 1990, pp. 19– 30.

[50] R.R. Yager, On ordered weighted averaging aggregation operators in multi criteria decision-making, IEEE Transactions on Systems, Man and Cybernetics: Part A. Systems and Humans 18 (1988) 183– 190.

[51] R.R. Yager, On weighted median aggregation, International Journal of Uncertainty, Fuzziness and Knowledge-based Systems 2 (1994) 101– 113.

[52] R.R. Yager, On the analytic representation of the Leximin ordering and its application to flexible constraint propagation, European Journal of Operational Research 102 (1997) 129–145.

[53] S. Zadrozny, An Approach to the Consensus Reaching Support in Fuzzy Environment. Consensus Under Fuzziness, Kluwer, Norwell, MA, 1997.

![](/api/attachments/7UXEDW9K/fulltext/images/98489d15d3203ad6ac74ba4a3a56f5d1a9051765d8453bd6527b87977c04afc0.jpg)

A. K. Choudhury is a final year Bachelor student of Manufacturing Engineering, NIFFT. He has developed various algorithms by applying the concepts of Multi-Criteria, Multi-person scenario to solve the problems of Vendor Selection, Technology Selection, etc. He is presently working on Sustainable Product Design, building Decision Support Systems to resolve disassembly line balancing problems, and design of Auction systems for telecommu-

nication market. He has published his article in PPC.

![](/api/attachments/7UXEDW9K/fulltext/images/0bddaf2147b369b767c1c0e71e6ca576b3a903588c8f52ba004f274d0e05a258.jpg)

Dr. Ravi Shankar is Assistant Professor of Operations and Information Technology Management at the Department of Management Studies at Indian Institute of Technology Delhi, India. He has nearly 23 years of teaching and research experience. His areas of interest are Supply Chain Management, Knowledge Management, Flexible Manufacturing Systems, TQM, etc. His publications have appeared in various journals including the European Journal of Opera-

tional Research, International Journal of Production Research, Computers and Industrial Engineering, International Journal of Production Economics, Computers and Operations Research, International Journal of Supply Chain Management, etc. He is the executive editor of Journal of Advances in Management Research.

![](/api/attachments/7UXEDW9K/fulltext/images/86ad74b45542028ad127b240a706418a66f10e9327f84e63fb045124e4bbddae.jpg)  
Dr. M. K. Tiwari has been pursuing research in the broad area of Soft Computing Applications in Solving Planning, Scheduling, and Control Problems of Automated Manufacturing Systems. He has extensively contributed articles in reputed journals like EJOR, International Journal of Production Research, IJCIM, R and CIM, PPC etc. He is also acting as a referee for 16 International Journals and also in the list of Editorial board members of 2 Journals.
