---
otero_id: 21703
otero_key: "MCEH9CNM"
title: "Supporting business process redesign using cognitive maps"
authors: "Kee-Young Kwahk; Young-Gul Kim"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00003-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supporting business process redesign using cognitive maps

Kee-Young Kwahk <sup>1</sup>, Young-Gul Kim )

Graduate School of Management, Korea AdÕanced Institute of Science and Technology, 207-43 Cheongryangri-Dong, Dongdaemoon-Gu, Seoul 130-012, South Korea

Accepted 18 December 1998

## Abstract

Turbulent changes and competitive pressures have forced organizations to constantly change. Business process redesign Ž . BPR has been widely adopted as an organizational change method in the 1990s. Although BPR projects provide the possibility of dramatic performance improvement, many organizations have encountered serious problems due to the lack of commitment to such projects and the difficulty of systematic targeting of critical processes. By identifying the cause–effect relationships within an organization, we try to address these issues. We propose a cognitive map based method, called two-phase cognitive modeling TCM , to help organizational members identify potential organizational conflicts, captureŽ . core business activities, and suggest ways to support the necessary organizational change. To apply the method in the real world context, we developed a prototype modeling tool, called two-phase cognitive modeling facility TCMF . WorkingŽ . procedures of the TCM method and TCMF features are illustrated with their application to the real BPR project of a dairy company. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Business process redesign BPR ; Modeling; Core business activity; Conflict; Cognitive map Ž .

## 1. Introduction

In a world characterized by rapid and turbulent changes, the ability of an organization to correctly interpret and rapidly respond to internal and external changes is of considerable academic and practical interest. Business process redesign BPR , also calledŽ . business reengineering BR , has been proposed as Ž . an organizational change method in the early 1990s <sup>w</sup> <sup>x</sup> 6,8,21,22 . Although BPR provides the possibility of dramatic improvement in performance and has been widely promoted as an enabler of organizational change, a BPR project is considered as a high risk due to its high management complexity, enterprisewide impact, and steeper project cost 26 . Many <sup>w</sup> <sup>x</sup> organizations have encountered serious problems during their BPR implementations with widely mixed results 17,37 . Regarding the challenges facing the <sup>w</sup> <sup>x</sup> organizational change implementations, there have been two major concerns.

First, despite the massive resource investment and enterprise-wide impact, many organizations attempt to redesign their major business processes without thorough consideration for commitment to changes <sup>w x</sup> <sup>w x</sup> <sup>w x</sup> 17 . Based on Kling’s 30 work, Markus 35 explains the resistance to change and implementation difficulties in terms of the conflicts among participants. Managers or change agents spend a substantial proportion of their time and energy dealing with conflict situations 16 . Such efforts are necessary <sup>w</sup> <sup>x</sup> because any type of change in an organization tends to generate conflicts. Their effectiveness in conflict management depends on how well they understand the underlying dynamics of the conflict 39 . Without <sup>w</sup> <sup>x</sup> commitment to change, a BPR project will suffer from resistance of the participants, in particular, those belonging to the process es to be redesigned.Ž .

Secondly, the business context has to be understood to enable the BPR team to identify the potential problem or opportunity activities before creating a new process or redesigning the existing ones <sup>w</sup> <sup>x</sup> 7,15,17,18,28,38 . However, it is not a trivial task to identify and capture these activities systematically. As Barua et al. 2 notes, many BPR projects have<sup>w</sup> <sup>x</sup> been frequently targeted toward inappropriate variables which have little or no impact on the organizational payoff. Most BPR methods tend to rely on the intuitive judgment of the analyst in capturing core business activities, by and large, based on the interviews or documents without thoroughly considering how functional units interact each other.

To address the above concerns—lack of understanding for potential organizational conflicts and improper targeting of critical processes in the initial stage of BPR, we propose a method, called two-phase cognitive modeling TCM . The TCM method helpsŽ . to support the organizational change project such as BPR, based on the analysis of cognitive maps. It is expected to facilitate consensus elicitation toward common organizational goal and core business activities among BPR managers, IS staffs, and organizational members in the initial stage of a BPR project. To apply the method in the real world context, we developed a prototype modeling tool, called twophase cognitive modeling facility TCMF . This sys- Ž . tem enhances applicability of the TCM method. The rest of the paper proceeds as follows. Section 2 deals with the literature review relevant to our study. Sections 3 and 4 introduce the proposed method and the prototype system, respectively. Section 5 describes the real-world application of the TCM method with the TCMF features. Section 6 discusses implications and future directions of this research.

## 2. Literature review

## 2.1. BPR

Although many organizations have striven to achieve dramatic performance improvement through BPR, there have been unsatisfactory results. As Bashein et al. 3 notes, while some organizations<sup>w</sup> <sup>x</sup> have been satisfied with reengineering results, 70% of projects have ended in failure. According to Hall et al. 19 , between 50 and 70% of the organizations<sup>w</sup> <sup>x</sup> failed to capture the expected ‘dramatic’ gains from BPR. While several reasons for the mixed results have been proposed by BPR experts, most of them have been concerned with human-involved problems not technology-involved problems: e.g., too much expectation to the reengineering result, lack of senior management leadership, lack of IS<sup>r</sup>business partnership, lack of commitment to changes, failure to consider politics of the BR efforts, and difficulty in cross-functional cooperation 8,17,19,22,36 . A study<sup>w</sup> <sup>x</sup> on potential problems in BPR by Grover et al. 17<sup>w</sup> <sup>x</sup> reports that only eight among the 64 problems are related with technological competence and four of the top five most severe problems concern change management which entails human interaction such as communicating reengineering rationale to employees, politics of reengineering efforts, and commitment to new values.

One of the problems frequently occurring in BPR without considering human factors is various conflicts between functional units. These conflicts affect BPR in the form of resistance of the participants who belong to the functional area to be redesigned and come to undermine the corporate synergy. Identification of these factors is more important in the earlier stage of BPR than in the later stages because the target area is usually selected in the earlier stage and the opportunity cost may be relatively minimal. Despite the growth of interests for the human-involved issues, however, existing BPR researches have focused on modeling the cross-functional business process of an entire organization in terms of performance based measurements such as cycle time. Along with this effort, however, it is necessary to consider modeling qualitative factors such as perceived cause–effect or explanation–consequence relation-Ž . ship and interaction between functional units.

## 2.2. CognitiÕe modeling

Models are useful because they can be used to abstract from and simplify complex systems. We construct models to highlight or emphasize certain critical features of a system, while simultaneously de-emphasizing other less important aspects of the system 47 . The key issue in modeling, then, is the <sup>w</sup> <sup>x</sup> choice of which aspects of the observed phenomena to include and which to omit. Process modeling emphasizes process and data modeling focuses on data, whereas cognitive modeling based on causal maps deals with cause–effect relationships among causal concepts. Understanding of causal relationships permits one to explain and to predict events and is critical to environmental understanding. Eden <sup>w x</sup> <sup>w x</sup> 10 and Eden and Ackermann 11 have established a theoretical groundwork for cognitive modeling from Kelly’s 25 theory of personal constructs. The the-<sup>w</sup> <sup>x</sup> ory implies that people make sense of the world in order to predict how the world will be in the future, and to decide how they might act in order to achieve what they prefer within that world. Cognitive modeling has the following features: understanding and capturing cause–effect relationships, facilitating identification of problem and opportunity, and facilitating systems thinking in an organization.

Among the techniques for cognitive modeling, the cognitive map method has been widely used <sup>w</sup> <sup>x</sup> 11,24,33,40,49 . It is a technique used to structure, analyze, and make sense of accounts of problems <sup>w</sup> <sup>x</sup> 10 . An individual’s perception and understanding of a problem can be captured in a cognitive map which consists of interconnected sets of elements representing implicit views of one’s own interests, concerns and tasks 34 . According to Zhang et al.<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 48 , a cognitive map is ‘a representation of relationships that are perceived to exist among the attributes and<sup>r</sup>or concepts of a given environment’. Eden et al. <sup>w</sup> <sup>x</sup> 12 defined the cognitive map as ‘a directed graph characterized by an hierarchical structure which is most often in the form of a means<sup>r</sup>ends graph’. Various researchers have named it differently under different contexts: cognitive map 1,24,29,31,33,48,<sup>w</sup> 49 , cause map 11,20 , and influence diagram 9,40 . <sup>x</sup> <sup>w</sup> <sup>x</sup> <sup>w x</sup> In this study, the cognitive map is represented in matrix as well as diagram. Diagram representation is used for capturing cause–effect relationships in an organization because it is relatively easy to see how each of the concepts relate to each other, while matrix representation is used for identifying the most effective causal path because it is convenient to apply a mathematical algorithm.

The three constructs of a cognitive map are ‘node’, called causal concept, $\cdot _ { \mathrm { i n k } } ,$ , representing causal connection among causal concepts, and ‘strength’, specifying causal Õalue of a causal connection. There are three kinds of cognitive maps depending on the representation method of the causal value: the simplest form which has either $\cdot + \cdot \mathrm { o r } \cdot - \cdot$ , a weighted map which has a value in the interval <sup>w</sup> <sup>x</sup> <sup>y</sup>1,1 , and a fuzzy map which employs a fuzzy value such as ‘more’ or ‘some’ 33 . We adopted the weighted <sup>w</sup> <sup>x</sup> map representation because it can express the relative strength of a causality unlike the simplest mapŽ . and is convenient to manipulate unlike the fuzzyŽ map . Causal values in the weighted map are to . quantify the perceived strengths of relationships between causal concepts 40 . For example, ‘<sup>w</sup> <sup>x</sup> <sup>y</sup>1’ means very strongly negative relationship, whereas ‘<sup>q</sup>1’ means very strongly positive relationship. Fig. 1 illustrates the constructs of the cognitive map.

## 2.3. PreÕious research using cognitiÕe map

Several cognitive modeling methods and tools using the cognitive map have been developed in

![](/api/attachments/MCEH9CNM/fulltext/images/90d81019ddd4a4e914abc91d0db32ff8b8efba93c2b00f7d2340ba618b7ed255.jpg)

Causal concept: node i, node $j ,$ node k Causal connection: link $( i , j )$ , link $( j , k )$ , link (i, k) Causal value: strength $\nu _ { i { \dot { p } } }$ strength $\nu _ { j k } ,$ strength $\nu _ { i k }$

Fig. 1. Constructs of the cognitive map.

T<sub>a</sub>bl<sub>e</sub> 1 A<sub>na</sub>l<sub>ys</sub>i<sub>s o</sub>f <sub>cogn</sub>iti<sub>ve map</sub> b<sub>ase</sub>d <sub>researc</sub>h

<table><tr><td>Characteristics</td><td>A-Pool</td><td>COCOMAP</td><td>MIND</td><td>SODA</td><td>TCM</td></tr><tr><td>Model type</td><td>Cognitive map/algorithm</td><td>Cognitive map</td><td>Cognitive map/algorithm</td><td>Cognitive map</td><td>Cognitive map/algorithm</td></tr><tr><td>Map integration</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Discrepancy resolution</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Causal value elicitation</td><td>Direct assignment</td><td>No</td><td>Direct assignment</td><td>No</td><td>Eigenvector assignment</td></tr><tr><td>Measurement</td><td>The most effective paths and values</td><td>No</td><td>The total number of paths and strength</td><td>No</td><td>The most effective paths and values</td></tr><tr><td>Guideline suggestion</td><td>Decision making based on the criteria</td><td>Map analysis (conceptual centrality, loops, etc.)</td><td>Map analysis (elements&#x27; nature, multi-order consequences, loops, cycles, etc.)</td><td>Map analysis (band, central, cluster, loop, collapse, etc.)</td><td>Potential conflict/core business activity</td></tr><tr><td>Application</td><td>Distributed decision making</td><td>Organizational learning</td><td>Strategic planning problem</td><td>GDSS</td><td>BPR</td></tr></table>

various domains: A-Pool 49 , COCOMAP collec-<sup>w</sup> <sup>x</sup> Ž tive cognitive mapping 33 , MIND mapping and . <sup>w</sup> <sup>x</sup> Ž interpreting influence diagrams 40 , SODA stra-. <sup>w</sup> <sup>x</sup> Ž tegic options development and analysis 11 , and so. <sup>w</sup> <sup>x</sup> forth. While some methods emphasize map representation and analysis using cognitive maps, others include an evaluation algorithm based on strength of causality for the maps as well. Map integration and discrepancy resolution between maps along with causal value elicitation deal with the richness of the model, while measurement and guideline suggestion represent the problem solving orientation of the model. Table 1 shows a comparison of five cognitive modeling methods.

A-Pool is a distributed decision process model based on cognitive maps in the Internet domain. Although it suggests guidelines for decision making according to some criteria, causal values used for the criteria are assumed to be given by the analysts. COCOMAP supports group cognitive processes and organizational learning via cognitive mapping. It emphasizes the use of signed cognitive maps as a knowledge representation scheme, not as a problem solving tool. MIND is a technique designed for supporting the complex business policy and planning problem using influence diagram or cognitive map .Ž . Although it evaluates and analyzes the paths between elements based on some measurements, it does not provide guidelines for solving a specific problem and it uses direct scale values. SODA aims to encourage organizational members to actively define their own strategy. It uses the COPE software or Decision Ž Explorer to capture and manage data within the. setting of group decision support. It has many application domains such as strategy development, organizational learning, and requirements capture and is used extensively by practitioners and academics for the analysis of qualitative research data and for the computer based group support. Although it provides the advanced map analysis, it does not present the problem solving guidelines based on measurements. On the other hand, the proposed TCM method provides guidelines for supporting the initial stage of BPR, based on the analysis of the most effective paths and values. It tries to elicit causal values systematically using an eigenvector approach through the pairwise comparison, while supporting the discrepancy resolution and automatic map integration.

## 3. The TCM method

The TCM method has three components as shown in Fig. 2. It proceeds in two phases. The first phase identifies cause–effect relationships in an organization through cognitive mapping. The second phase evaluates each relationship to identify the most effective causal path. By integrating these two phases, the method helps to capture potential organizational conflicts and identify core business activities.

## 3.1. CognitiÕe model

The method begins with the assumption that organizational members or their groups participate in creating their own cognitive maps which appropriately reflect the cause–effect relationships in their organization. In our method, two types of cognitive models are generated through cognitive mapping: local cognitive model and global cognitive model. Each model is represented by a cognitive map along with a relevant set of goals.

## 3.1.1. Local cognitiÕe model

Local cognitive models are generated for diverse functional operating or product units in an organi- Ž . zation. These units can be teams, departments or divisions depending on the level of analysis. The cognitive model generation process includes the four steps as shown in Table 2. The first step facilitates the generation of a robust cognitive map from the second step through the fourth step. Organizations exit for a purpose, and goals define and state that purpose 5 . Goals also serve as guides to action 43 .<sup>w x</sup> <sup>w</sup> <sup>x</sup> Hence, clarifying the goal of each functional unit helps to capture the cause–effect relationships among cognitive elements.

![](/api/attachments/MCEH9CNM/fulltext/images/f59ec7693d8e1756acb153253a59476caf8e08fdcafb2adce91294c06263361a.jpg)  
Fig. 2. The TCM method components.

The cognitive map plays a key role in the process and is a main component of our method. Since basic information used in the method is mainly derived from the cognitive map, whether the method is well applied to the real context or not depends on the capability to generate a robust cognitive map. A number of techniques can be used to generate and validate the organizational cognitive maps: interview, observation, group discussion, questionnaire, document analysis, and so forth. As mentioned in Section 2, a cognitive map is composed of three components: causal concept, causal value, and causal connection. The main difficulty lies in determining the ‘causal value’ component. Specification of the causal value is the most challenging problem in generating a cognitive map because it has a qualitative property reflecting people’s cognitive status which cannot be directly measured. Besides, human perception is often inconsistent. Direct scale values have been used by most of the methods and systems for cognitive modeling 11,24,33,40,49 . However,<sup>w</sup> <sup>x</sup> this direct assignment approach has limitations in that the procedure is not systematic and the result heavily depends on the analysts’ or participants subjective judgment. For the TCM method, an eigenvector approach through pairwise comparison was chosen for more systematic determination of causal values. This approach is based on the analytic hierarchy process AHP method developed in the 1970sŽ . 41 . Strength of the AHP method lies in its ability to structure a complex problem hierarchically and to evaluate the relationships between entities systematically. If structural equation modeling technique such as Lisrel is used in eliciting causality, more valid causality may be obtained. As Axelrod 1 notes,<sup>w</sup> <sup>x</sup> however, using a statistical technique to estimate the parameters is a long way from the purpose of cognitive mapping, which is to represent what people actually say about causal relationships.

## 3.1.2. Global cognitiÕe model

Local reasoning is done by each functional oper- Ž ating or product unit to produce its own local . cognitive model. However, global reasoning is necessary to combine local cognitive models into a global cognitive model. Because cognitive maps tend to impose structure on a vague situation, group members can gain a clearer understanding of problems and opportunities 46 . In order to combine the <sup>w</sup> <sup>x</sup> local cognitive maps, we first identify common causal concepts between any two local cognitive maps, and link the maps based on these concepts. Each common causal concept plays the role of a coupling device. In turn, the next local cognitive map is joined with the previous result. This way, the combination process continues until all local cognitive maps are exhausted. While the local cognitive maps are being combined into a global cognitive map, various discrepancies between the maps might arise. Discrepancies may occur in all three constructs of the cognitive map. These discrepancies should be detected and resolved in order to create a complete global cognitive map.

Table 2  
Cognitive model generation process

<table><tr><td colspan="2">Steps/tasks</td><td>Outputs</td><td>Means</td></tr><tr><td>1</td><td>Specify the goal</td><td>Goal statement</td><td>Brainstorming, interview, and document analysis</td></tr><tr><td>2</td><td>Identify causal concepts-List all the causal concepts-Cluster the causal concepts</td><td>Causal concept list</td><td></td></tr><tr><td>3</td><td>Identify causal connections-Identify the relationships between clusters-Identify the relationships between causal concepts</td><td>Cluster relationship diagram</td><td></td></tr><tr><td>4</td><td>Specify causal values-Conduct pairwise comparison-Compute eigenvectors</td><td>Pairwise comparison matrix Causal values</td><td>Questionnaire Eigenvector algorithm</td></tr></table>

First, causal concept naming discrepancies occur when different functional units use different terms for the same concept or for describing the same phenomenon. Therefore, a thesaurus is needed to designate a single term for multiple synonyms. Second, causal connection discrepancies occur when different functional units have different causal connections for the same link between two concepts. This can be classified into two types: existence and direction discrepancy. The existence discrepancy does not lead to a problem in generating a global cognitive map because identifying the existence of a connection means adding new information to the global cognitive map. However, a direction discrepancy must be resolved through coordination among the conflicting units. If this discrepancy is not detected and properly resolved, it may result in the overall misunderstanding of the organizational behavior. Third, causal value discrepancies occur when different functional units assign different causal values to the same connection between two concepts. For resolution of this type of discrepancy, we can adopt a knowledge combination technique which combines individual units’ causal values on each connection and generates a weighted value. We adopted the Kosko’s fuzzy knowledge combination formula 32 because it is theoretically sound and<sup>w</sup> <sup>x</sup> rests entirely on uncertainty fuzzy or random intu- Ž . itions which reflect the cognitive model of an organization closely. The Kosko’s knowledge combination formula is as follows.

$$
k = \operatorname{Min} (m, 1 - m + l)
$$

where k: Kosko’s knowledge combination value; m: Max $X _ { i } ( v ) ; l \colon$ Min $X _ { i } ( v ) ; X _ { i } ( v )$ : causal connection value by individual unit i.

During the combination process, new causal concepts and causal connections may be introduced into the global cognitive map along with appropriate causal values assigned. The cognitive model generation process shown in Table 2 is also applied to creating the global cognitive model.

## 3.2. Causal path

The completed global cognitive map is analyzed in terms of the strength of the impact between causal concepts. The global cognitive map includes the indirect causal paths as well as the direct causal paths. The direct causal paths can be easily identified from the map, while it is difficult to identity the indirect causal paths. Besides, the indirect causal paths are usually multiple. Our concern is to identify the causal paths with the maximum causal impact among all causal paths regardless of the direct or indirect impact. These causal paths take negative or positive path values, depending on their causal values. In order to identify the causal path s with theŽ . maximum causal impact, we adopted the algorithm proposed by Zhang et al. 48 and extended it to find<sup>w</sup> <sup>x</sup> the paths and values simultaneously. By applying the algorithm to the global cognitive map, we produce an $n \times n$ matrix called causal impact path and value matrix consisting of $X _ { i j } ,$ where $X _ { i j }$ is the set of $\{ + p _ { i j } , - p _ { i j } , + v _ { i j } , - v _ { i j } \}$ . Each element of the set is as follows: $+ p _ { i j } / - p _ { i j }$ is the maximum positive<sup>r</sup>negative causal impact path from causal concept i to j and $+ v _ { i j } / - v _ { i j }$ is the maximum positive<sup>r</sup>negative causal impact value from causal concept i to j. The main procedure loop of the algorithm is applied iteratively while either maximum positive value $( + v _ { i j } )$ or maximum negative value $( - v _ { i j } )$ can be improved—in other words, until new dominant values cannot be identified. The simplified algorithm is as follows:

Initialization

$$
\begin{array}{l} \text {Set X_{ij} such as} \\ \quad + p _ {i j} = \{i, j \}, \quad - p _ {i j} = \{\phi \}, \quad + v _ {i j} = u _ {i j}, \\ \quad - v _ {i j} = 0, \quad \text {If} u _ {i j} > 0 \\ \quad + p _ {i j} = \{\phi \}, \quad - p _ {i j} = \{i, j \}, \quad + v _ {i j} = 0, \\ \quad - v _ {i j} = u _ {i j}, \quad \text {If} u _ {i j} <   0 \\ \quad + p _ {i j} = \{\phi \}, \quad - p _ {i j} = \{\phi \}, \quad + v _ {i j} = 0, \\ \quad - v _ {i j} = 0, \quad \text {If} u _ {i j} = 0 \end{array}
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Main procedure
Do While Being Improvement
For i = 1 To n
    For j = 1 To n
    For k = 1 To n
    Read  $-v_{ij}, +v_{ij}, -v_{ik}, +v_{ik}, -v_{kj}, +v_{kj}$ 
    If  $-v_{ij} &gt; (-v_{ik}) \cdot (+v_{kj})$ 
    Set  $-v_{ij} = (-v_{ik}) \cdot (+v_{kj})$ 
    Set  $-p_{ij} = (-p_{ik}) \cup (+p_{kj})$ 
End If
    If  $-v_{ij} &gt; (+v_{ik}) \cdot (-v_{kj})$ 
    Set  $-v_{ij} = (+v_{ik}) \cdot (-v_{kj})$ 
    Set  $-p_{ij} = (+p_{ik}) \cup (-p_{kj})$ 
End If
    If  $+v_{ij} &lt; (+v_{ik}) \cdot (+v_{kj})$ 
    Set  $+v_{ij} = (+v_{ik}) \cdot (+v_{kj})$ 
    Set  $+p_{ij} = (+p_{ik}) \cup (+p_{kj})$ 
End If
    If  $+v_{ij} &lt; (-v_{ik}) \cdot (-v_{kj})$ 
    Set  $+v_{ij} = (-v_{ik}) \cdot (-v_{kj})$ 
    Set  $+p_{ij} = (-p_{ik}) \cup (-p_{kj})$ 
End If
Next k
Next j
Next i
Loop
</div>

## 3.3. Action guidelines

The method suggests two types of guidelines in the view of the organizational goal, based on the cognitive model and causal path analysis: organizational conflict resolution and core business activity identification. These guidelines provide a solid starting point in the initial stage of a BPR project.

## 3.3.1. Guideline for organizational conflict resolution

Organizations have multiple goals, which are often in conflict with one another. Success in one goal may mean compromise in others as in the case of increasing market share and maximizing profits. Organizational conflict is described as the inter-departmental behavior that occurs when one department perceives that other departments are blocking its goal achievement or expectation 38,42,44 . Organiza-<sup>w</sup> <sup>x</sup> tional conflicts within an organization can occur in both horizontal and vertical direction. The horizontal conflict occurs between individual departments, while the vertical conflict occurs between the organization itself and individual departments.

Organizational conflict is similar to the agency problem that arises when two parties have different goals and it is difficult or expensive for one party to verify what the other party is actually doing 13 .<sup>w</sup> <sup>x</sup> The problem lies in the fact that one party may take actions conflicting with the other party because of different goals. Different actions within the organization due to a goal conflict among multiple departments may lead to the overall organizational ineffec tiveness. When an organizational conflict occurs, there can be three possible strategies: concession, compromise, and intervention. Concession and compromise are defensive strategies which alleviate organizational conflicts by giving up one’s goal or adjusting its level, while intervention is an aggressive strategy which reduces organizational conflicts by weakening the conflict factor without changing goal status. Concession and compromise strategies are appropriate when the organizational policy or priority for the conflict resolution has been already established. If not, an intervention strategy is desirable in terms of organizational effectiveness because the goal status is not changed. Intervention represents a strategy which attempts to achieve both parties’ goal. The conflicting parties are intervened through a resolution scheme, which does not change their goal status. It is concerned with problem solv ing which may lead to an effective solution acceptable to both parties. For intervention to be a $\mathbf { \hat { W } i n } / \mathbf { W } \mathbf { i n } ^ { \prime }$ strategy, however, it is required to identify the conflict and intervention drivers. From the cognitive model and the causal impact path and value matrix, these drivers are identified. Through the process of identifying the conflict and intervention drivers in a potential conflict situation, organizational members come to understand each other better and become more willing to transform their ideas into a unified action. Consensus toward an organizational goal will reduce the resistance to the project and promote commitment to the change. The analy sis procedure is summarized in Fig. 3.

![](/api/attachments/MCEH9CNM/fulltext/images/df3fa65b7f82253ae2d4f8f44c3a9ab1661cb0eb392dfe5587781125f9797785.jpg)  
Fig. 3. Organizational conflict analysis.

## 3.3.2. Guideline for core business actiÕity identification

An organizational goal is a desired future state of affairs that the organization attempts to realize 14 .<sup>w</sup> <sup>x</sup> Goal pertains to the future, but it influences current activities. Goal is important because organizations are goal-attainment devices. Goal plays a role of direction setting for people’s activities and lead their thoughts and actions to a specific result 23 . There-<sup>w</sup> <sup>x</sup> fore, we can identify core business activities by analyzing people’s thoughts and actions toward their organizational goal—thus, identify the opportunity for redesigning the existing organizational processes.

We first focus on the most effective causal concept in achieving the goal regardless of the sign of the impact. It can be an opportunity if it has a positive impact, but it can be a problem if it has a negative impact. Then, we identify the relevant feedback loop paths which make the positive impact stronger and the negative impact weaker. For the positive impact causal concept, this means making its own positive loop more positive and making its own negative loop less negative. For the negative impact causal concept, this means making its own positive loop less positive and making its own negative loop more negative. We consider these activities as the core business activities for accomplishing the organizational goal and redesigning the relevant processes. The analysis procedure is summarized in Fig. 4.

## 4. The TCMF

TCMF has been developed to support the group cognitive processes through cognitive mapping as suggested by the TCM method. The TCM method can be used manually in a simple situation. As the number of causal concepts grows and the number of causal connections increases, however, it becomes almost impossible to compute the casual impact paths and values by hand. An intelligent system for automatic construction of the cognitive map and efficient computation of the casual impact paths and values is desired. This is why TCMF has been implemented. TCMF enhances the applicability of the TCM method. TCMF has been implemented using the Microsoft Visual Basic version 4.0 in the Windows 95 environment. The overall architecture of TCMF is depicted in Fig. 5.

## 4.1. Subsystems of TCMF

## 4.1.1. Local cognitiÕe map manager

The local cognitive map manager plays a basic role in TCMF. It stores functional units’ cognitive maps in the form of a diagram. A thesaurus is used to determine the causal concept name and avoid the causal concept naming discrepancy. Local goals are set through the goal setting window.

![](/api/attachments/MCEH9CNM/fulltext/images/7e836bf695e67e0b26f3be46407844b747b34a58d0045c3ab4be52578c7d8506.jpg)  
Fig. 4. Core business activity analysis.

![](/api/attachments/MCEH9CNM/fulltext/images/aef3f8e4d527c6c18153d428b51bd37e6d5a00e93498769ae6f82d7db21a7469.jpg)  
Fig. 5. Overall architecture of TCMF.

## 4.1.2. Global cognitiÕe map manager

The global cognitive map manager provides a synthesized map by combining local cognitive maps. A global cognitive map is automatically constructed through the synthesis process. Local goals are automatically extracted from the local cognitive models. Discrepancies between local cognitive maps are handled by the discrepancy manager.

## 4.1.3. Causal Õalue generator

The causal value generator specifies causal values to causal connections in the interval of <sup>w</sup> <sup>x</sup> <sup>y</sup>1,1 . Causal values are generated according to the pairwise comparison technique. The causal value generator supports the function of pairwise comparison and eigenvector computation. The causal value generator is used by both the local cognitive map manager and the global cognitive map manager.

## 4.1.4. Discrepancy manager

The discrepancy manager interacts with the global cognitive map manager. When discrepancies between the local cognitive maps occur during the generation of a global cognitive map, the discrepancy manager returns a solution or an alternative to the global cognitive map manager.

## 4.1.5. Causal impact path and Õalue generator

The causal impact path and value generator provides a matrix which describes the causal impact paths and values between causal concepts. It stores the causal paths with values in a matrix form. The matrix is used by the conflict and activity analyzer.

## 4.1.6. Conflict and actiÕity analyzer

The conflict and activity analyzer analyzes the potential organizational conflict and the core business activity based on information from the cognitive model and causal impact path and value matrix. It provides two types of guidelines on potential organizational conflict and core business activity, in the view of the organizational goal.

## 4.2. Relationship between TCM and TCMF

In this subsection, we describe the relationship between the TCM method and the TCMF system.

Table 3  
Tasks assigned to the user and the system for the method phase

<table><tr><td>Method phase</td><td>Tasks assigned to the user</td><td>Tasks assigned to the system</td></tr><tr><td colspan="3">(1) Cognitive model</td></tr><tr><td>(A) Specify the goal</td><td>Identify the goal</td><td>Store the goal in the model (cognitive map manager)</td></tr><tr><td>(B) Identify causal concepts</td><td>Identify causal concepts</td><td>Draw the map (cognitive map manager)</td></tr><tr><td>(C) Identify causal connections</td><td>Identify causal connections</td><td>Draw the map (cognitive map manager)</td></tr><tr><td>(D) Specify causal values</td><td>Prepare pairwise comparison matrix</td><td>Compute eigenvectors (causal value generator)</td></tr><tr><td> $^a$ Combine local cognitive maps</td><td>-</td><td>Combine local cognitive maps (cognitive map manager/discrepancy manager)</td></tr><tr><td>(2) Causal path</td><td>-</td><td>Compute causal paths (CIP/V generator)</td></tr><tr><td colspan="3">(3) Action guidelines</td></tr><tr><td>(A) Organizational conflict</td><td>Analyze organizational conflict</td><td>Compute conflict paths and values (conflict and activity analyzer)</td></tr><tr><td>(B) Core business activity</td><td>Analyze core business activity</td><td>Elicit core concepts (conflict and activity analyzer)</td></tr></table>

<sup>a</sup> Do during the process of global cognitive map generation.

Table 3 presents the tasks assigned to the user and the system for each phase of the method.

## 5. Application case

In this section, we describe a real-world application of the TCM method, which was conducted as part of the BPR project for a large dairy company with an annual sales volume of about US\$400 million in 1997. The main function of the firm consists of raw material milk collection, production man-Ž . agement, inventory control, order management, and delivery. It has three factories and various sales organizations composed of branches and agencies. Branches take orders from over 800 agencies nationwide and aggregate them on the daily basis. The ordered quantities are classified by product and by agency and are notified to the head office for accounting and to the factories for production. The factory produces the assigned quantity and delivers it to each agency according to the daily delivery schedule.

## 5.1. CognitiÕe model

Among the several candidate departments, we decided to select the marketing department and the production department to apply the TCM method because they are in charge of core functions such as order processing, marketing, production, and delivery and their interaction is very frequent. Each department deals with various sorts of products such as milk, powdered milk, cheese, yogurt, and so forth. In this application, we focused on the milk related business functions because their contribution to the total sales is the highest and their interactions are most frequent.

In order to generate the local cognitive maps for the marketing department and the production department, we first had a brainstorming session and interviews with the participants from each department. The cognitive model generation process included the following activities: 1 to identify the goal of each Ž . department, 2 to identify and cluster causal con- Ž . cepts, 3 to identify the relationships between clus- Ž . ters and between causal concepts, and 4 to collectŽ . data for a pairwise comparison between the extracted causal concepts.

Through the discussion and the interviews, the causal concept relationship diagrams were generated along with the relevant goals see Fig. 6 . TheŽ . marketing department’s goal was set as ‘increase of sales amount’, while the production department’s goals was set as ‘improvement of productivity’. Based on these diagrams, we created a pairwise comparison questionnaire to elicit the casual strength of relationships. Completed questionnaires were transformed into a pairwise comparison matrix form

![](/api/attachments/MCEH9CNM/fulltext/images/e712515c2de27011e72d7f873a994a706987a3caa1d58b7cafadd9d05c669046.jpg)  
Fig. 6. Causal concept relationship diagram for local cognitive map.

to compute the weighted causal value. Appendix A shows an example of the causal impact questionnaire and pairwise comparison matrix. The weighted causal value computation was performed by the causal value generator of TCMF. The completed local cognitive maps and the causal value generation process by TCMF are shown in Appendix B.

The global cognitive map was generated by combining the two local cognitive maps, based on the common causal concepts of the two maps. The global cognitive map manager of TCMF identified five common causal concepts: ‘market share’, ‘market size’, ‘ordering time’, ‘adjustment time’, and ‘delivery time’. After the synthesized process, a new causal concept, ‘profit’, was introduced. This causal concept was initially ignored by the two departments, but after some discussion, they agreed that it is necessary to describe the overall organizational behavior appropriately. The organizational goal was set as ‘profit increase’. A new clustering which was not considered in each local cognitive map was introduced into the global cognitive map. Causal concepts, ‘sales’ and ‘productivity’ were grouped into a new cluster: ‘profit factor’. The causal concept relationship diagram for the global cognitive map is shown in Fig. 7. In order to complete the global cognitive map, a new pairwise comparison questionnaire for the newly introduced causal concept and cluster was administered. The completed global cognitive map by TCMF is shown in Appendix B.

## 5.2. Causal path

The causal impact paths and values among the causal concepts were computed based on the pairwise comparison matrix by the causal impact path and value generator of TCMF. The derived matrix includes the negative path and value as well as the positive path and value for each relationship among the causal concepts. Fig. 8 shows the matrix derived from TCMF.

## 5.3. Action guidelines

The TCM method suggested two types of action guidelines in terms of the organizational goal. Fig. 9 shows the analysis result on organizational conflict and core business activity suggested by TCMF.

## 5.3.1. Guideline for organizational conflict resolution

TCMF identifies several potential organizational conflicts from the computed causal impact paths and values, vertically between organization itself andŽ individual departments and horizontally between. Ž individual departments as seen in Table 4 also in. Ž Fig. 9 . For the marketing department, efforts for. accomplishing the goal of the marketing department Ž . increasing sales amount may lead to a failure of the organizational goal increasing profit because of theŽ . negative impact via increase of market share–in-  crease of ordering time path. That is, various activi- 4

![](/api/attachments/MCEH9CNM/fulltext/images/625b6ebcce9f4de994589c5a310c29c2f488e4108d85feb14c613fd7fb94c225.jpg)  
Fig. 7. Causal concept relationship diagram for global cognitive map.

![](/api/attachments/MCEH9CNM/fulltext/images/35367201f775edc71ff486765c6abdf96ed689f5847dd1514795fec799314043.jpg)  
Fig. 8. Causal impact path and value matrix.

ties for increasing sales amount eventually may lead to profit decrease although the goal of the marketing department is accomplished. Therefore, the marketing department come to have a conflict with the organizational goal in this case. Likewise, the production department has a conflict with the organizational goal through increase of market share–in-  crease of ordering time–decrease of productivity4 path.

![](/api/attachments/MCEH9CNM/fulltext/images/552f0686219747d683fa08e56fcefc374860ad582fa527abf83eaa5713e9e467.jpg)  
Fig. 9. Organizational conflict and core business activity.

Table 4  
Analysis on organizational conflicts

<table><tr><td>Conflicts department</td><td></td><td>Conflict paths (values)</td></tr><tr><td rowspan="2">Marketing</td><td>Group</td><td>Sales-market share-ordering time-productivity-profit (-0.26)</td></tr><tr><td>Production</td><td>Sales-market share-ordering time-productivity (-0.39)</td></tr><tr><td rowspan="2">Production</td><td>Group</td><td>Productivity-market share-ordering time-productivity-profit (-0.13)</td></tr><tr><td>Marketing</td><td>Productivity-market share-advertising-sales (-0.17)</td></tr><tr><td rowspan="2">Group</td><td>Marketing</td><td>Profit-information system-ordering time-sales-market share-advertising-sales (-0.15)</td></tr><tr><td>Production</td><td>Profit-information system-ordering time-sales-market share-ordering time-productivity (-0.17)</td></tr></table>

After we detected the organizational conflict, our next concern was how to resolve it systematically without sacrificing the local goals. We tried to identify the conflict drivers and intervention drivers for the conflict. We first identified the conflict drivers based on the cognitive model and the causal impact path and value matrix from TCMF. Among the causal concepts consisting of the conflict paths, the ‘ordering time’ concept was identified as the conflict driver which has the most negative impact on the paths. After identifying conflict driver, we identified the intervention driver which has the most negative impact to the conflict drivers. From the causal impact path and value matrix, ‘information system concept was identified as the intervention driver which affects the conflict driver the most. The project team came to recognize the ordering time related activity as a potential problem area. Information system was also considered to be the most effective means for attaining the organizational goal and conducting the project without sacrificing local goals.

## 5.3.2. Guideline for core business actiÕity identification

TCMF identifies core business activities from the causal impact paths and values matrix as seen in Table 5 also in Fig. 9 . Considering the profit Ž . increase as a target goal, the system identifies two most effective causal concepts from the causal impact paths and values matrix refer to Table 6 . OneŽ . is the ‘productivity’ which is the most positive causal concept, and can be considered as an opportunity for accomplishing the goal since productivity enhancement contributes most to increasing the corporate profit. The other is the ‘ordering time’ which is the most negative causal concept, and can be viewed as a problem to the goal since the increase of ordering time prevents the profit from increasing. Our objective is to make the positive causal concept, ‘productivity’, stronger and to make the negative casual concept, ‘ordering time’, weaker. As seen in Table 5

Table 5  
Analysis on core business activities

<table><tr><td>Causal concept</td><td></td><td>Feedback loops</td></tr><tr><td rowspan="2">The most positive impact concept: productivity</td><td>Positive</td><td>Path = {productivity-profit-information system-productivity}Value = +0.52</td></tr><tr><td>Negative</td><td>Path = {productivity-market share-ordering time-productivity}Value = -0.19</td></tr><tr><td rowspan="2">The most negative impact concept: ordering time</td><td>Positive</td><td>Path = {ordering time-productivity-profit-information system-ordering time}Value = +0.36</td></tr><tr><td>Negative</td><td>Path = {ordering time-sales-market share-ordering time}Value = -0.32</td></tr></table>

Table 6  
Part of causal impact paths and values matrix causal concept ‘profit’ columnŽ .

<table><tr><td rowspan="2">Cell</td><td colspan="2">Positive</td><td colspan="2">Negative</td></tr><tr><td>Value</td><td>Path</td><td>Value</td><td>Path</td></tr><tr><td>(01, 01)</td><td>+0.516</td><td>1-14-11-1</td><td>-0.114</td><td>1-14-15-2-19-15-11-1</td></tr><tr><td>(02, 01)</td><td>+0.330</td><td>2-1</td><td>-0.261</td><td>2-19-15-11-1</td></tr><tr><td>(03, 01)</td><td>+0.026</td><td>3-2-1</td><td>-0.021</td><td>3-2-19-15-11-1</td></tr><tr><td>(04, 01)</td><td>+0.198</td><td>4-2-1</td><td>-0.156</td><td>4-2-19-15-11-1</td></tr><tr><td>(05, 01)</td><td>+0.160</td><td>5-7-9-2-1</td><td>-0.159</td><td>5-6-2-1</td></tr><tr><td>(06, 01)</td><td>+0.175</td><td>6-2-19-15-11-1</td><td>-0.221</td><td>6-2-1</td></tr><tr><td>(07, 01)</td><td>+0.211</td><td>7-9-2-1</td><td>-0.167</td><td>7-9-2-19-15-11-1</td></tr><tr><td>(08, 01)</td><td>+0.056</td><td>8-2-1</td><td>-0.044</td><td>8-2-19-15-11-1</td></tr><tr><td>(09, 01)</td><td>+0.254</td><td>9-2-1</td><td>-0.201</td><td>9-2-19-15-11-1</td></tr><tr><td>(10, 01)</td><td>+0.020</td><td>10-2-1</td><td>-0.016</td><td>10-2-19-15-11-1</td></tr><tr><td>(11, 01)</td><td>+0.670</td><td>11-1</td><td>-0.128</td><td>11-19-15-11-1</td></tr><tr><td>(12, 01)</td><td>+0.114</td><td>12-11-1</td><td>-0.022</td><td>12-11-19-15-11-1</td></tr><tr><td>(13, 01)</td><td>+0.080</td><td>13-15-11-1</td><td>-0.025</td><td>13-15-2-19-15-11-1</td></tr><tr><td>(14, 01)</td><td>+0.516</td><td>14-11-1</td><td>-0.114</td><td>14-15-2-19-15-11-1</td></tr><tr><td>(15, 01)</td><td>+0.149</td><td>15-2-19-15-11-1</td><td>-0.469</td><td>15-11-1</td></tr><tr><td>(16, 01)</td><td>+0.026</td><td>16-2-19-15-11-1</td><td>-0.040</td><td>16-11-1</td></tr><tr><td>(17, 01)</td><td>+0.086</td><td>17-2-19-15-11-1</td><td>-0.161</td><td>17-11-1</td></tr><tr><td>(18, 01)</td><td>+0.025</td><td>18-15-2-19-15-11-1</td><td>-0.080</td><td>18-15-11-1</td></tr><tr><td>(19, 01)</td><td>+0.138</td><td>19-5-6-2-1</td><td>-0.389</td><td>19-15-11-1</td></tr></table>

Legend: 1 profit, 2 sales amount, 3 DM, 4 advertising, 5 price down, 6 domestic competition, 7 foreign competition, 8 product Ž . Ž . Ž . Ž . Ž . Ž . Ž . Ž . differentiation, 9 product quality, 10 product diversity, 11 productivity, 12 facility, 13 manpower, 14 information system, 15Ž . Ž . Ž . Ž . Ž . Ž . Ž . ordering time, 16 delivery time, 17 adjustment time, 18 market size, 19 market share.Ž . Ž . Ž . Ž .

and Fig. 10, the causal concepts ‘productivity’ and ‘ordering time’ have the positive feedback loops of productivity–profit–information system–productivity and ordering time–productivity–profit–informa- 4  tion system–ordering time , respectively. In addition4 to that, the above two concepts have the negative feedback loops of productivity–market share–order-  ing time–productivity and ordering time–sales– 4  market share–ordering time , respectively. It seems4 clear that the paths productivity–profit–information  system and ordering time–productivity are the 4  4 main drivers that accelerate the improvement of productivity and the decrease of ordering time. Thus, by designating the above two paths related activities as core business activities, we can focus on how to use information technologies in redesigning the productivity and ordering time related processes.

![](/api/attachments/MCEH9CNM/fulltext/images/20e67c345257046a593de3989457fdd3586c4abe6f9b1beff864c800a6b4dfb3.jpg)  
Fig. 10. Feedback loops of the most effective concepts for the target goal.

![](/api/attachments/MCEH9CNM/fulltext/images/6f4e27ea4d9631a43831c91236342a1922230c598fd73e2749d5f73c4a67eabb.jpg)  
Fig. 11. EPC diagram before redesign: order processing.

Based on the above information and consensus, we identified the order process as a candidate target process and attempted to redesign it. The current order process heavily depends on manual handling which results in the long ordering time and less efficient production and delivery. In addition, it has burdened the sales branch personnel with heavy workload by forcing them to take the agencies’ order quantities and retype them into the host computers. By introducing a new client–server system for the redesigned order process, they could reduce the total ordering time significantly. In the newly redesigned order process, every agency directly sends its order to the factory through the network without intervention of the branches. Branches just confirm the ordered quantity from the agencies and adjust the quantity if necessary. Reduction of the branch’s intervention in order taking is expected to result in the decreased ordering time, which leads to the efficiency of production and delivery and, in the long run, contributes to profit. Figs. 11 and 12 show the order process before and after the process redesign, represented in the event–process chain EPC dia-Ž . gram format 27 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/MCEH9CNM/fulltext/images/94dc268064236ef1010f7c2e526ad81366756340d7978ad085e84dbb98f505c2.jpg)  
Fig. 12. EPC diagram after redesign: order processing.

## 5.4. Discussion

The application of the TCM method to a dairy company mainly focused on validating its feasibility. Currently, we are also applying it to other BPR projects in cable-TV and engineering industries. Up to date, the tentative result of such applications convinced us that the method can contribute to effective and efficient conflict detection and provide an opportunity of process redesign based on it.

The TCM method can complement the existing BPR methodologies because the redesign opportunities identified by the TCM method can be used. However, not all BPR projects seem to benefit equally from the application of the TCM method. The cognitive map approach identifying cause–effect relationships works well with organizations where frequent interactions among functional units are required and cooperation with each other in executing a cross-functional business process is critical.

## 6. Summary and implications

We proposed the TCM method to support the initial stage of BPR based on the analysis of cognitive maps. The supporting process proceeds in two phases: cognitive model generation and causal path computation. By integrating the two phases, the method helps to capture potential conflicts and identify core business activities. To facilitate the TCM method, we developed the TCMF which consists of six subsystems. Finally, to validate the TCM method and the TCMF system, we applied them to a realworld company. The working procedure was described with the TCMF screens.

The TCM method has several implications for an organization which is planning an organizational change project at the enterprise level. First, the method facilitates the identification of the interactions among functional units. The identified interactions might lead to revealing the most effective communication paths, over the existing formal communication paths. Such communication paths play an important role in a potential conflict situation. Second, the method helps to identify core business activities by looking into people’s thoughts and actions for the organizational goal. The ability of capturing core business activities relieves the efforts in the initial stage of the enterprise level project and provides a good starting point for the project. Third, consensus drawing among various functional units can be facilitated by the method. Without commitment to changes, projects suffer from resistance of the participants, in particular, who belong to the functional area s to be redesigned. By the process of Ž . identifying the cause–effect relationships, organizational members come to understand each other better, and they become willing to transform their ideas into corporate synergy. Such a consensus will promote the commitment of the participants to the project. Fourth, the method provides an opportunity to reduce organizational equivocality. Equivocality is the ambiguity based on the existence of multiple and conflicting interpretations about an organizational situation 45 . As Daft and Huber 4 notes, equivo-<sup>w</sup> <sup>x</sup> <sup>w x</sup> cality can be reduced through the exchange of opinions, perceptions of relevant managers, construction of a joint cognitive map, and rapid feedback.

Currently, however, there are several limitations in the method. First, the method begins with the assumption that organizational members or their groups participate in creating their own cognitive maps which appropriately reflect cause–effect relationships in an organization. Strictly speaking, however, it is not easy to produce a theoretically robust and valid causal model. Second, it is hard to obtain causal values which are agreeable to everyone. Although this research suggested a pairwise comparison based technique, this issue still remains to be further examined. Third, the method does not consider the cause–effect relationships with time delay among causal concepts. A causal concept may affect the other one with time delay. Fourth, our approach may be well suited for strategic problems, not BPR. The causal impact paths do not imply the business processes directly. The focus on the constructs and relationships is not per se a process perspective. The interpretation of the analysts is required for capturing the corresponding business processes appropriately.

One of the future directions of this research is to include the time dimension in the method. For more realistic modeling, it is necessary to represent the time delay effect among the interrelated causal concepts. Another direction is to extend our modeling method into the areas of integrated process and data modeling since cognitive modeling can complement the other two enterprise modeling activities.

## Acknowledgements

The authors wish to thank the editor-in-chief, Professor Andrew B. Whinston, for his kind and thoughtful editorial help for this paper.

## Appendix A. Example of causal impact questionnaire and pairwise comparison matrix

## A.1. Causal impact questionnaire

Relative impact strength for ‘sales amount

<table><tr><td>Column I</td><td colspan="2">Absolute</td><td colspan="2">Very strong</td><td colspan="2">Strong</td><td colspan="2">Weak</td><td>Eq</td><td colspan="2">Weak</td><td colspan="2">Strong</td><td colspan="2">Very strong</td><td colspan="2">Absolute</td><td>Column II</td></tr><tr><td>Ordering time</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Delivery time</td></tr><tr><td>Ordering time</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Adjustment time</td></tr><tr><td>Delivery time</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>Adjustment time</td></tr></table>

Relative impact strength for ‘sales amount

<table><tr><td>Column I</td><td colspan="2">Absolute</td><td colspan="2">Very strong</td><td colspan="2">Strong</td><td colspan="2">Weak</td><td>Eq</td><td colspan="2">Weak</td><td colspan="2">Strong</td><td colspan="2">Very strong</td><td colspan="2">Absolute</td><td>Column II</td></tr><tr><td>Product quality</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Product diff.</td></tr><tr><td>Product quality</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Product diversity</td></tr><tr><td>Product diff.</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Product diversity</td></tr></table>

## A.2. Pairwise comparison matrix

<table><tr><td>Sales amount</td><td>Ordering time</td><td>Delivery time</td><td>Adjustment time</td><td>Causal value</td></tr><tr><td>Ordering time</td><td>1</td><td>5</td><td>2</td><td>0.57</td></tr><tr><td>Delivery time</td><td>1/5</td><td>1</td><td>1/4</td><td>0.10</td></tr><tr><td>Adjustment time</td><td>1/2</td><td>4</td><td>1</td><td>0.33</td></tr></table>

<table><tr><td>Sales amount</td><td>Product quality</td><td>Product diff.</td><td>Product diverse</td><td>Causal value</td></tr><tr><td>Product quality</td><td>1</td><td>7</td><td>9</td><td>0.77</td></tr><tr><td>Product diff.</td><td>1/7</td><td>1</td><td>5</td><td>0.17</td></tr><tr><td>Product diverse</td><td>1/9</td><td>1/5</td><td>1</td><td>0.06</td></tr></table>

## Appendix B. Cognitive maps and causal value generation process

1. Marketing department cognitive map Fig. B.1. .Ž .

2. Production department cognitive map Fig. B.2. .Ž .

![](/api/attachments/MCEH9CNM/fulltext/images/76090755b1cab588454a8cb549df8fd662fef7549ca4d2e3f6284f4678a935a9.jpg)  
Fig. B.1. Marketing department cognitive map.

![](/api/attachments/MCEH9CNM/fulltext/images/4f79166510aadce92bc953d714813b34ddc070db7924cad35a79d2524fcd8c65.jpg)  
Fig. B.2. Production department cognitive map.

![](/api/attachments/MCEH9CNM/fulltext/images/40ac1d32f35af68a0164eb443247f888823d6388b28bde9b2969bca2de52fc81.jpg)  
Fig. B.3. Global cognitive map.

![](/api/attachments/MCEH9CNM/fulltext/images/71e184d814d24c61b0ebe79a20e40d1a12383797a08ef1bde1586fd3cbf947c3.jpg)  
Fig. B.4. Casual value generation.

3. Global cognitive map Fig. B.3. . Ž .

4. Causal value generation Fig. B.4. .Ž .

## References

<sup>w</sup> <sup>x</sup> 1 R. Axelrod, Structure of Decision: The Cognitive Maps of Political Elites, Princeton University Press, Princeton, NJ, 1976.

<sup>w</sup> <sup>x</sup> 2 A. Barua, C.H.S. Lee, A.B. Whinston, The calculus of reengineering, Information Systems Research 7 4 1996Ž . Ž . 409–428.

<sup>w</sup> <sup>x</sup> 3 B. Bashein, L. Markus, P. Riley, Preconditions for BPR success, Information Systems Management, Spring 1994Ž . 27–38.

<sup>w</sup> <sup>x</sup> 4 R.L. Daft, G. Huber, How organizations learn: a communication framework, in: S. Bucharach, N. Tomasso Eds. , Re-Ž . search in Sociology of Organizations, Vol. 5, JAI Press, Greenwich, CT, 1986.

<sup>w</sup> <sup>x</sup> 5 R.L. Daft, R.M. Steers, Organizations: A Micro<sup>r</sup>Macro Approach, Foresman, IL, 1986.

<sup>w</sup> <sup>x</sup> 6 T.H. Davenport, Process Innovation, Harvard Business School Press, Cambridge, 1993.

<sup>w</sup> <sup>x</sup> 7 T.H. Davenport, M.C. Beers, Managing information about processes, Journal of Management Information Systems 12 Ž . Ž . 1 1995 57–80.

<sup>w</sup> <sup>x</sup> 8 T.H. Davenport, J. Short, The new industrial engineering: information technology and business process redesign, Sloan Management Review, Summer 1990 11–27.Ž .

<sup>w</sup> <sup>x</sup> 9 J. Diffenbach, Influence diagrams for complex strategic issues, Strategic Management Journal 3 1982 133–146.Ž .

<sup>w</sup> <sup>x</sup> 10 C. Eden, Cognitive mapping, European Journal of Operational Research 36 1988 1–13.Ž .

<sup>w</sup> <sup>x</sup> 11 C. Eden, F. Ackermann, Strategic options development and analysis SODA —using a computer to help with the man- Ž . agement of strategic vision, in: G. Doukidis, F. Land, G. Miller Eds. , Knowledge-Based Management Support Sys-Ž . tems, Ellis Horwood, UK, 1989, pp. 198–207.

<sup>w</sup> <sup>x</sup> 12 C. Eden, F. Ackermann, S. Cropper, The analysis of cause maps, Journal of Management Studies 29 3 1992 309–324.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 K.M. Eisenhardt, Agency theory: an assessment and review, Academy of Management Review 14 1 1989 57–74. Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 A. Etzioni, Modern Organizations, Prentice-Hall, Englewood Cliffs, NJ, 1964.

<sup>w</sup> <sup>x</sup> 15 H. Gerrits, Business modeling based on logistics to support business process reengineering, in: Proceedings of the IFIP TC8 Open Conference on Business Process Reengineering: Information Systems Opportunities and Challenges, May, 1994, pp. 279–288.

16 L. Greenhalgh, SMR forum: managing conflict, Sloan Management Review, Summer 1986 45–51.Ž .

<sup>w</sup> <sup>x</sup> 17 V. Grover, S.R. Jeong, W.J. Kettinger, J.T.C. Teng, The implementation of business process reengineering, Journal of Management Information Systems 12 1 1995 109–144.Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 S. Guha, W.J. Kettinger, J.T.C. Teng, Business process reengineering, Information Systems Management 10 3Ž . Ž . 1993 13–22.

<sup>w</sup> <sup>x</sup> 19 G. Hall, J. Rosenthal, J. Wade, How to make reengineering really work, Harvard Business Review 71 6 1993 119–Ž . Ž . 131.

<sup>w</sup> <sup>x</sup> 20 R. Hall, The natural logic of management policy making: its implications for the survival of an organization, Management Science 30 8 1984 905–927.Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 M. Hammer, Reengineering work: don’t automate, obliterate, Harvard Business Review, July–August 1990 104–112.Ž .

<sup>w</sup> <sup>x</sup> 22 M. Hammer, J. Champy, Reengineering the Corporation: A Manifesto for Business Revolution, Harper-Collins Publishers, New York, 1993.

<sup>w</sup> <sup>x</sup> 23 W.C. Hamner, J. Ross, B.M. Staw, Motivation in organizations: the need for a new direction, in: R.M. Steers, L.W. Porter Eds. , Motivation and Work Behavior, McGraw-Hill,Ž . 1983, pp. 52–72.

<sup>w</sup> <sup>x</sup> 24 R.J. Johnson, R.O. Briggs, A model of cognitive information retrieval for ill-structured managerial problems and its benefits for knowledge acquisition, in: Proceeding of the 27th Annual Hawaii International Conference on System Sciences, 1994, pp. 191–200.

<sup>w</sup> <sup>x</sup> 25 G. Kelly, The Psychology of Personal Constructs: A Theory of Personality, Norton, New York, 1955.

<sup>w</sup> <sup>x</sup> 26 H.W. Kim, Y.G. Kim, Dynamic process modeling for BPR: a computerized simulation approach, Information and Management 32 1 1997 1–13.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 Y.G. Kim, Process modeling for BPR—event process chain approach, in: Proceedings of International Conference on Information Systems, 1995, pp. 109–121.

<sup>w</sup> <sup>x</sup> 28 Y.G. Kim, H.W. Kim, J.W. Yoon, H.S. Ryu, Building an organizational decision support system for Korea Telecom: a process redesign approach, Decision Support Systems 19 Ž .1997 255–269.

<sup>w</sup> <sup>x</sup> 29 J.H. Klein, D.F. Cooper, Cognitive maps of decision-makers in a complex game, Journal of Operational Research Societ 33 1982 63–71.Ž .

<sup>w</sup> <sup>x</sup> 30 R. Kling, Social analysis of computing: theoretical perspectives in recent empirical research, Computing Surveys 12 1Ž . Ž .1980 61–110.

<sup>w</sup> <sup>x</sup> 31 B. Kosko, Fuzzy cognitive maps, International Journal of Man–Machine Studies 24 1986 65–75.Ž .

<sup>w</sup> <sup>x</sup> 32 B. Kosko, Fuzzy knowledge combination, International Journal of Intelligent Systems 1 1986 293–320.Ž .

<sup>w</sup> <sup>x</sup> 33 S. Lee, J.F. Courtney, R.M. O’Keefe, A system for organizational learning using cognitive maps, Omega 20 1 1992 Ž . Ž . 23–36.

<sup>w</sup> <sup>x</sup> 34 R.T. Lenz, J.L. Engledow, Environmental analysis: the appli cability of current theory, Strategic Management Journal 17 Ž . Ž .4 1986 329–346.

<sup>w</sup> <sup>x</sup> 35 M.L. Markus, Power, politics, and MIS implementation, Communications of the ACM 26 6 1983 430–444.Ž . Ž .

<sup>w</sup> <sup>x</sup> 36 E.V. Martinez, Successful reengineering demands IS<sup>r</sup>business partnership, Sloan Management Review, Summer 1995 Ž . 51–60.

<sup>w</sup> <sup>x</sup> 37 M.G. Martinsons, Radical process innovation using information technology: the theory, the practice, and the future of reengineering, International Journal of Information Management 15 4 1995 253–269.Ž . Ž .

<sup>w</sup> <sup>x</sup> 38 S. Pfreniziner, Reengineering goals shift toward analysis, transition, Software Managing 12 14 1992 50–58.Ž . Ž .

<sup>w</sup> <sup>x</sup> 39 M.A. Rahim, A strategy for managing conflict in complex organizations, Human Relations 38 1985 81–89.Ž .

<sup>w</sup> <sup>x</sup> 40 A. Ramaprasad, E.A. Poon, A computerized interactive technique for mapping influence diagrams MIND , Strategic Ž . Management Journal 6 1985 377–392.Ž .

<sup>w</sup> <sup>x</sup> 41 T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

<sup>w</sup> <sup>x</sup> 42 S.M. Schmidt, T.A. Kochan, Conflict: toward conceptual clarity, Administrative Science Quarterly 17 1972 359–370.Ž .

<sup>w</sup> <sup>x</sup> 43 H.A. Simon, On the concept of organizational goals, Administrative Science Quarterly 9 1964 1–22.Ž .

<sup>w</sup> <sup>x</sup>44 K. Thomas, Conflict and conflict management, in: M.D. Dunnette Ed. , Handbook of Industrial and OrganizationalŽ . Psychology, Rand McNally, Chicago, 1976.

<sup>w</sup> <sup>x</sup> 45 K.E. Weick, The Social Psychology of Organizing, Addison-Wesley, Reading, MA, 1979.

<sup>w</sup> <sup>x</sup> 46 K.E. Weick, M.G. Bougon, Organizations as cognitive maps, in: H.P. Sims, D.A. Gioia Eds. , The Thinking Organization:Ž . Dynamics of Organizational Social Cognition, Jossey-Bass, San Francisco, CA, 1986, pp. 103–135.

<sup>w</sup> <sup>x</sup> 47 E. Yourdon, Modern Structured Analysis, Yourdon, Englewood Cliffs, NJ, 1989.

<sup>w</sup> <sup>x</sup> 48 W.R. Zhang, S.S. Chen, J.C. Bezdek, Pool2: a generic system for cognitive map development and decision analysis, IEEE Transactions on Systems, Man, and Cybernetics 19 1Ž . Ž . 1989 31–39.

<sup>w</sup> <sup>x</sup> 49 W.R. Zhang, W. Wang, R.S. King, A-Pool: an agent-oriented open system shell for distributed decision process modeling, Journal of Organizational Computing 4 2 1994 127–154.Ž . Ž .

![](/api/attachments/MCEH9CNM/fulltext/images/f07c1a94224f48b03d580ce01699de63da755f5eb3ec01713767ebf42209bc82.jpg)

Kee-Young Kwahk has worked with Samsung SDS as a senior consultant for IS planning, BPR, and IT infrastructure development. He received his BA degree in Business Administration from Seoul National University, his MS and PhD degree in MIS from the Graduate School of Management of the Korea Advanced Institute of Science and Technology KAIST in Seoul, Korea. HisŽ . research interests are: process and cognitive modeling, organizational learning

and knowledge management system, coordination science, IS architecture development, and BPR. He has published in International Journal of Information Management, Decision Support Systems, and Korean Management Science Review. He also presented a paper at the international DSI conference.

![](/api/attachments/MCEH9CNM/fulltext/images/da9775544b65527f3e088d2a95f5c7da688cda0eec4519e7a4736c11662599d0.jpg)

Young-Gul Kim is an associate professor of MIS at the Graduate School of Management of the Korea Advanced Institute of Science and Technology Ž .KAIST in Seoul, Korea. He received his PhD degree in MIS from the Carlson School of Management, University of Minnesota, USA, and taught at the Katz Graduate School of Business, University of Pittsburgh, USA, from 1990 to 1993. His research interests are: data and process modeling, IS architecture develop-

ment, knowledge management system, business process redesign, and customer information system. He has published in Communications of the ACM, Journal of MIS, Decision Support Systems Information and Management, Database, and Information Systems Management. He also presented several papers at DSI, HICSS, and ICIS conferences.
