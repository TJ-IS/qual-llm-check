---
otero_id: 17292
otero_key: "NH4ANU7Q"
title: "Connectionist approaches to inexact reasoning and learning systems for executive and decision support"
authors: "Donggill Jung; James R. Burns"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90004-m"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Connectionist approaches to inexact reasoning and learning systems for executive and decision support Conceptual design

Donggill Jung and James R. Burns
Texas Tech University, Lubbock, TX, USA

Connectionist approaches to the representation and reasoning about problems addressed by executive and decision support systems are described. It is shown that analog object structures coupled with learning produce mechanisms for managerial problem diagnoses. These mechanisms are neural models with multiple-layer structures that support continuous input/output. Because a connectionist architecture is assumed, the prototype system is called the Connectionist Inexact Reasoning System or CIROS. Although uncharacteristic of neural architectures, an explanation capability is developed within CIROS and described herein. The primary contribution of CIROS is that it provides principles for design of inexact reasoning systems for managerial problem diagnosis.

Keywords: Backward propagation (chaining); Causal model; Connectionist system; Knowledge-based system; Learning system; Neural network; Semantic network; Signed digraph.

Donggil Jung graduated from Seoul National University with M.A. Degree in Economics, 1977. He finished his graduate school at Korea Advanced Institute of Science and Technology with M.S. of Management Science, 1981. After 5 years of work, he started Ph.D study at Texas Tech University and finished it in 1990. He is now Research Coordinator of the National Computerization Agency of Korea and is working towards standardization of computer communication and information processing technologies for Korean Government. His research interests include knowledge-based systems for managerial problem-solving and neural networks. He is particularly interested in the nature of information imperfection and its impacts on human decision making to design intelligent decision support systems.

## 1. Introduction

Human decision-making in complex environments is, in general, not a well-understood process $[57,4,$ and 77]. It is, however, precisely this ill-understood process that needs support by intelligent computer systems. Although there is no comprehensive understanding of this process, it is

![](/api/attachments/NH4ANU7Q/fulltext/images/ed58d036002509aca50c883507dab1b48adc995640ba741166aae859185719bc.jpg)

James R. Burns is currently Area Coordinator of the Department of Information Systems and Quantitative Sciences and Professor of Information Systems in the College of Business Administration at Texas Tech University. Dr. Burns received his B.S. degree from the University of Colorado and his M.S. and Ph.D. degrees from Purdue University in 1966, 1967 and 1973, respectively. From 1967 to 1970 he was a research engineer with The Boeing Company in Seattle. Dr. Burns

is the author or co-author of over fifty journal articles and publications on subjects as diverse as concentrating photovoltaics to design of decision support systems. Much of his published research is concerned with methodology for modeling continuous, lumped dynamic processes. He has also published several methods for automating the process of knowledge acquisition for causal systems. He is the author or coauthor of the following texts: Management Science: An Aid for Managerial Decision Making, published by Macmillan in 1985, Management Science Models and the Microcomputer, also published by Macmillan in 1985, and Microcomputers: Business and Personal Applications, published by West in 1988. Dr. Burns has continuing interests in mathematical programming, in simulation, and in knowledge representation and processing. One specific focus is the integration of these various modeling constructs into systems for decision support. He is a member of the IEEE SMC Society, The Institute for Management Science, the Operations Research Society of America, American Production and Inventory Control Society, the Data Processing Management Association and Phi Kappa Phi.

known that human reasoning lies at the heart of any decision-making and problem-solving activity [57]. In this regard, a primary function of an intelligent computer system should be that of providing an extension of the reasoning capabilities of the human [55,56].

Humans making decisions face, in reality, a less-than-ideal environment. They have to work with less-than-perfect information. One pervasive characteristic of the real world environment is the presence of information imperfection $[62,83,11,72$ and 77]. Data are often missing or unreliable, decision rules are not well-tested or in some cases not known at all $[11,78]$ . Confronted with this situation, human reasoning processes tend to be increasingly more heuristic as data and domain knowledge become more fragmented and imperfect $[26,77]$ .

Sometimes humans cope with this situation quite effectively. In most cases, however, they are not so successful because of the limited capability of their reasoning systems $[57,51,7,$ and 11]. In this regard, there is a strong need to support human decision making in such an imperfect reasoning environment.

Fortunately, there has been a considerable amount of research done both in academia and industry to understand the human decision process in imperfect reasoning environments, and intelligent computer systems have been developed that can support the process $[73,11,$ and 44].

Attempts to design reasoning systems that try to handle human/expert decision-making with such information imperfection have not achieved fully satisfactory results in the sense that their solutions are partial and not efficient enough to work for situations that require timely decisions. These systems lack “robustness” and “efficiency” [42,30].

Robustness is a characteristic of a reasoning system such that it works in diverse situations:

(1) where some of the input data are missing, unreliable, coming from multiple sources, and sometimes combinations of these;

(2) where reasoning rules are unreliable, sometimes missing, and moreover, inexactness from these are aggregated as a result of chaining of these rules; and

(3) where data and knowledge inherently involve vagueness.

Traditional inexact reasoning systems are lacking this characteristic. For example, both MYCIN and PROSPECTOR can handle uncertain information only when the degree of uncertainty for an evidence fragment or rule is provided from outside (human experts). In other words, when an inexact reasoning system needs to acquire knowledge from the outside or to interact with human experts, human experts must express their uncertain knowledge in a way that is often unnatural (e.g., identifying numeric values that the experts are not aware of in their normal reasoning) [43,81,30]. Also these traditional systems have weak facilities for explaining the outputs of reasoning.

Another major type of flaw in most inexact reasoning systems is the problem of efficiency – specifically, computational efficiency [32,46,21]. Expert systems or decision support systems that involve inexact reasoning require much more computation than those involving deterministic situations, thus result in intolerably slow computational speed [46,21].

In short, as stated above, existing inexact reasoning systems lack the two characteristics, robustness and efficiency, to a considerable degree, that are most important and required. In this regard, there is a substantial need for reasoning systems that possess both of the two characteristics.

## 2. Problem domain and applications

## 2.1. Problem domain

The problem domain of interest in this research is managerial problem diagnosis. Problem diagnosis refers to hypothesizing about causal relationships among variables believed to be associated with the problem at hand [20]. Problem diagnosis is a critical aspect of managerial decision makings, but one in which not much progress has been made [56,36,69].

From a managerial perspective, problem diagnosis may range from the operational decision level through the strategic decision level and from well-structured problems through ill-structured ones [24]. In this research, the diagnosis problem will be further confined to strategic, semi-structured and ill-structured managerial decision situ ations. The reason for this focus is that these situations are more typical for the decision situations and it is desirable to support these decisions with inexact reasoning systems, which can result in achieving a greater increase in effectiveness than structured decision situations.

One implication of approaching managerial problem diagnosis from the perspective of strategic and ill-structured decision situations is that it is necessary to represent these decision problems in terms of a global problem domain, i.e., in structural terms involving the whole organization $[20,5]$ . Therefore, the problem and knowledge representation requires appropriate schemes for that domain. The matter of representation will be discussed in more detail later.

From the viewpoint of the managerial decision process, problem diagnosis usually takes place as a subphase of problem finding $[53,69]$ . There are a number of models that describe managerial decision-making processes $[75,53,36,1]$ , and different authors use different terms for similar concepts. The one that is used here is from Ackoff $[1]$ , and the schematic representation of Ackoff's model is given in fig. 1.

In the literature, the terms such as “problem structuring” [60], “problem formulation” [2], and “problem diagnosis” [53] represent very similar concepts that indicate the step that takes place after locating a problem (or monitoring, in terms of fig. 1) which is the first step of the whole decision process. These terms are similar in the sense that each involves the specification of causal relationships among variables. In fact, hypothesizing about cause-effect relationships among variables corresponds to hypothesizing about the structure of the problem at hand [31,54,87].

![](/api/attachments/NH4ANU7Q/fulltext/images/4fd2a202f40c894e2fa3eab3a23aa38bfb84fd3d221a81e8836655a770a07727.jpg)  
Fig. 1. A managerial decision process [Ackoff, 1981].

From an artificial intelligence (Al) point of view, problem diagnosis is one of the areas for which intensive research has been done for a wide variety of applications $[76,50]$ . In particular, medical diagnosis is one for which many expert systems have been developed with a variety of techniques to handle medical diagnostic situations. Some of these techniques are not limited to medical diagnosis but can be applied to other areas including managerial problem diagnosis $[50]$ .

The crux of diagnostic activity is the ability to infer system malfunctions from observed activities/symptoms and to relate the observed effects to underlying causes [50]. Key issues in practical problem diagnoses are:

(1) the problem usually involves very complicated relationships. In other words, a symptom may be caused by different diseases and a disease may cause different symptoms;

(2) the data about the causes/effects are missing or unreliable;

(3) the knowledge about the relationships does not exist or is unreliable;

(4) the definitions of variables are inherently ambiguous or involve fuzzy expressions.

Thus, managerial problem diagnosis is an activity that, by and large, is ill-structured and complex enough to be a good candidate for being supported by computer-based inexact reasoning systems.

## 2.2. Digraph representation of qualitative reasoning

According to the study of managerial decision making, managers are more likely to resort to qualitative reasoning, i.e., reasoning in qualitative terms for problem diagnosis when they are in ill-structured decision situations (frequently, at a strategic level) [53,10]. Although the diagnosticians are faced with largely quantitative data, they do not deal with the data in that manner.

![](/api/attachments/NH4ANU7Q/fulltext/images/adbc52748a49d7d5ad520833de6adfa9d4d01f8960ff4eb655e62ba25fae9477.jpg)  
Fig. 2. A hypothetical marketing knowledge represented in a digraph.

Instead, they translate the series of figures into qualitative terms $[10]$ . Therefore, one premise for the inexact reasoning system that is developed in this research is that it needs to work with qualitative terms. In the following, it is discussed how the causal relationships based on the qualitative terms can be represented using a directed graph (digraph). This is shown with a simple hypothetical case for a marketing strategy of a business firm.

As an example, a deliberately restricted piece of knowledge on “marketing strategy” is considered, which is expressed in English sentences as follows: “Advertizing costs $(X_{1})$ and Size of sales force $(X_{2})$ influence Marketing costs $(C_{5})$ . Size of sales force $(X_{2})$ also influences Sales volume $(X_{6})$ . Sales volume $(X_{6})$ is also influenced by Price $(X_{3})$ and Economic conditions $(X_{4})$ . Finally, Marketing costs $(X_{5})$ and Sales volume $(X_{6})$ determine Net sales revenue $(X_{7})$ .”

If the (causal) relationships between the variables expressed in the above paragraph are represented as a directed graph, it looks like fig. 2.

This is a simple example for exhibition. In the real world, it is much more complicated. A typical example is shown in fig. 3.

Directed graphs have a long history in science and engineering, and are widely used as a major tool in diverse situations. For an introduction to the subject, refer to [31,15].

The digraph representation of knowledge and reasoning process has become very popular in AI field since Quillian first introduced semantic nets [61]. One extension of semantic nets was incorporation of inexactness into them. That has resulted in slightly different names from different authors, but representation of underlying structures is almost the same. Examples are “Inference Nets” in PROSPECTOR [25], “Bayesian Networks (or Belief Networks)” by Pearl [59], “Influence Diagrams” by Shachter [70,63], and so forth.

In brief, a digraph consists of only two types of symbols, nodes and links (directed lines are arcs). A node represents a random variable or an ambiguous entity/object or an uncertain event. A link between two nodes represents a causal relationship. A causal relationship may be uncertain, reflecting an expert's degree of confidence in that relationship. In the digraph representation of management decision problems, frequently the digraph contains no directed cycles.

## 2.3. Fundamental focus of the research

The directed links of the digraph are intended to represent any natural cognitive ordering that will allow assessment of any reasonable confidence measure. Although there are many other schemes for knowledge representation, network and digraph representations will be the fundamental focus of this article.

![](/api/attachments/NH4ANU7Q/fulltext/images/451d543fd4b2cff5d1e6c8c90f3438bcac55f6a138d50ebc77868c927cd470f7.jpg)  
Fig. 3. A strategic model for corporate marketing [Rosenkranz, 1979].

Moreover, support of management-oriented decision making $[24,33]$ is the primary goal of this research. As was discussed in the previous section, managerial problem diagnosis is a critical aspect of managerial problem solving. Also it was seen that the state-of-the-technology in inexact reasoning systems is not satisfactory in performance and acceptability, particularly in terms of robustness and computational efficiency $[42]$ . To mitigate this, a new inexact reasoning system is developed herein, which is based on design principles distinct from traditional ones.

## 2.4. Applications of inexact reasoning systems

Although it is difficult to quantitatively estimate all the improvements that may be expected as a result of supporting human reasoning processes, support of human reasoning activities can potentially result in enormous benefits, above and beyond those accruing from the support of knowledge access and computational activity $[7,43]$ . As Simon ponted out, imperfect information is one of the major factors that lead to a human being's “bounded rationality” in his/her decision making, and one of the roles of a computer is to help human beings reduce the limitations $[74]$ .

There are a variety of ways to support human reasoning activities using inexact reasoning systems. Since the environment described in the previous part is a very general one for most human decision makers, basic design principles of various inexact reasoning systems could have many commonalities, and it should be possible to use any inexact reasoning system for a variety of application areas.

However, most existing inexact reasoning systems were developed to support solving domain-specific problems. For example, MYCIN and INTERNIST were developed for medical diagnosis $[73]$ , PROSPECTOR for mineral exploration, and there are many systems in the area of business (FOLIO for portfolio management, LOAN RISK ADVISOR for loan management decisions, and CORP for strategic management of technology, etc. $[47,49]$ ). For damage assessments of existing structures, SPERIL was developed $[86]$ . For general probabilistic inferencing tasks, there are a number reasoning systems, including CONVINCE [40].

## 3. Knowledge representation requirements

Although there is much interest in the application of Al technology to management decision-making, very few management-oriented Al applications exist $[6,24]$ . Baldwin and Kasper discussed matching knowledge representation techniques to organizational domains. For “coordinative” and “strategic” decision categories, they suggest frames and semantic nets. The choice should depend on the characteristics of a specific task the system is to perform, such as learning versus non-learning, expert advice versus data retrieval and the type of explanation capability needed.

Dutta suggests some desirable capabilities of a representation and manipulation method to aid human reasoning under uncertain and inexact reasoning environments [26]. The method should possess the capability of inexact reasoning, which is inherent in the problem domain (managerial problem diagnosis). However, there are other capabilities that are desirable. In the following, each of these capabilities will be presented and discussed in a detailed manner to deduce requirements for inexact reasoning systems:

(1) the method should be capable of organizing the human's expertise into a knowledge structure that is easily manipulable on computers;

(2) the method should represent an uncertainty measure associated with each entity/object/event and an inexactness measure associated with the (domain) knowledge about the relationships between these entities/objects/events involved in the diagnostic situation in a natural way. Here, “natural way” means the way humans prefer in estimating and expressing the degree of uncertainty [38,48];

(3) the method should be able to recognize situations where it has insufficient or partial information;

(4) the method should be able to justify the reasoning process in any specific problem instance. It should also entail the explanation of choices of different rules, statements of alternative lines of reasoning for the same conclusion;

(5) the method should be able to acquire new knowledge and improve its reasoning ability over time as it aids in more and more decision-making instances.

In the following, each of these desirable capabilities is transformed into a substantial set of requirements for the inexact reasoning system in the context of managerial problem diagnosis.

It is known that expertise in managerial problem domains, in general, is rather ill-structured, implicit, and ambiguous $[74,1,26,24]$ . Managerial knowledge with this characteristic does not help managers to solve their problems $[10]$ . Humans' managerial knowledge should be organized and restructured so that computers can manipulate it and aid humans' problem-solving $[24]$ . Therefore, one of the requirements is that the prototype reasoning system should have the function of organizing humans' unstructured or ill-structured managerial knowledge into more structured forms.

The second issue of the desirable capabilities list above requires considerable discussion, because it involves the essential ingredients of inexact reasoning systems.

In general, it can be said that there are three different types of inexactness involved in managerial problem diagnosis. These are weight, probability, and fuzziness/certainty factor $[26,8]$ . Weights are used for measuring the degree of confidence or the strength of connection between variables that represent classes of entities/objects/events. Probabilities are used for measuring the uncertainty of a random variable or event in nature. The purpose of introducing the concept of fuzziness (or certainty factor) is that the concept is needed for represent of human experts' uncertain belief or inexact knowledge of the values of the variables involved in their decision problems. In the following, each concept is discussed in detail.

(1) By weight, we mean the strength of connection of the degree of belief in the (causal) relationship between two variables that is represented as a link in network representation of knowledge. In managerial problem diagnosis, it represents highly subjective and judgmental knowledge, which is usually acquired by experience. If enough statistical data are available for both variables, then we could calculate the correlation coefficient between the two variables and use it as the weight.

Weight, in the sense discussed above, must play a critical role in the inexact reasoning systems. It connects two uncertain variables and enables the system to compute the propagation of uncertainty (measured by probability or certainty factor) from one variable to another. And in this way uncertainty of a variable propagates to the uncertainty of the other variable that is connected by a path in the network. Another very important role of weight, particularly for a problem diagnosis, is the combination of two or more uncertainty numbers into a single uncertainty number as the process of pooling multiple evidences (effects) pertaining to the same hypothetical cause. Currently, a specific inexact reasoning system adopts a different mechanism for that purpose [42].

In addition, adaptation of the knowledge structure of a reasoning system to changes in relative connection between variables is desirable and sometimes strongly required, particularly in a long-term problem-solving environment. In this regard, it is desirable for the inference system to be fully intelligent enough to have a learning capability so that it can adjust the knowledge structure to the changing environment.

(2) For probability, there have been many controversies about its appropriateness for representing all kinds of inexactness and uncertainty, including the human's subjective judgment [14,9,84]. In contemporary expert systems, the main reason for using probability is to represent the degree of natural randomness of a variable or an event, and the people who advocate “fuzzy reasoning” believe that this characteristic of randomness should be separated from the subjective and cognitive uncertainty [8,26,84].

(3) For fuzziness and certainty factor, both concepts were created mainly to represent the uncertainty and inexactness pertaining to the human's subjective judgment and cognitive process. The concept of fuzziness is mainly for representing linguistic expressions of the definitions of variables or events. The concept of certainty factor is useful for representing the confidence degree for the existence or truth of an entity/object/event.

In a typical managerial problem diagnosis, the type of uncertainty (or inexactness) is mostly judgmental and subjective, thus it can be more appropriately represented by certainty factor or fuzzy set theoretic concepts $[26,77,8]$ . In summary of the representation of inexact knowledge, two of the inexactness measures, weight and certainty factor, seem more appropriate for the problem domain (managerial problem diagnosis). Hence, these two types of inexactness measure are adopted for the design of CIROS.

The rest of the (capability) issues are straightforward. In conclusion, the following set of requirements is provided for design of the prototype inexact reasoning system. Because a connectionist architecture is assumed, the prototype system shall be called the connectionist inexact reasoning system or CIROS, which should be able to:

(1) reorganize a human's expertise from a messy network structure into a form, say a layered, hierarchical structure that facilitates sound and efficient reasoning on computers;

(2) represent two types of inexact knowledge: Uncertain relationships between variables with their inexactness measure, weight, and uncertain entities/objects/events that are represented by variables with their inexactness measure, certainty factor;

(3) find unknown (or missing) but important variables in a particular diagnostic reasoning session and ask human users (or experts) to provide the values of those missing (but important) variables;

(4) produce justifications/explanations for its diagnostic conclusions upon request from human users;

(5) modify its knowledge structure and improve its reasoning ability over time by learning as it aids in more and more decision makings, assuming the same managerial problem domain.

![](/api/attachments/NH4ANU7Q/fulltext/images/dba34e6c38e0241d9c463511f99f5cb9f13ac655e04c4485954e8fc969738c36.jpg)  
Fig. 4. A fundamental structure of CIROS. In this figure there are L layers (excluding the input layer), numbered 1 through L. Except the layer L, all the layers are considered to be intermediate or hidden, in terms of connectionists. The number of variables in each layer varies over different layers. For example, variables in the output layer (Layer L) are numbered 1, 2, ..., $\mathbf{N}_{\mathbf{L}}$ . Notice that this numbering scheme does not mean that the number of variables in a layer should be equal to the layer number itself, i.e., $\mathbf{L}! = \mathbf{N}_{\mathbf{L}}$ .

## 4. Connectionist computational architecture

Connectionists take a totally different approach to computing. In this section, it is discussed how the connectionist approach is relevant to the computing task for the problem at hand (managerial problem diagnosis) and why it is chosen over other possible computing approaches.

To see how the connectionist approach is relevant to the computing task for managerial problem diagnosis, let us look at the managerial knowledge structure depicted in fig. 4. It involves tens or hundreds of variables and possibly hundreds or thousands of relationships between the variables. Some of these variables represent symptoms of a given diagnostic problem and others represent causes for the symptoms. Managerial problem diagnosis is nothing but a managerial problem-solving task of finding the causes for the symptoms.

Thus, problem diagnosis is, in a sense, very similar to pattern-matching and classification $[16,17]$ . There are differences between them. One difference between the two classes of tasks is that diagnosis usually requires building cause–symptom paths to explain and justify the diagnostic solutions $[50]$ .

A typical managerial problem diagnosis may involve tens or hundreds of pieces of symptom/evidence that should be processed simultaneously. It is known that conventional computing technologies are weak in this type of problem solving that requires massively parallel and distributed computation $[27,45]$ .

## 5. Design principles for CIROS

The fundamental structure of CIROS will look like the fig. 4. It is basically a layered, acyclic network. At the bottom is the input layer that represents the collection of symptom variables. The top layer is the output layer that represents the collection of eventual causes for symptom variables. Between the two layers are one or more intermediate layers that represent various classes of intervening variables. To capture and represent knowledge about managerial problem diagnosis, the following assumptions are made for CIROS.

(1) The domain knowledge (K) consists of two components, the set (V) of variables and the set (R) of relationships among the variables. Mathematically, K is a diad of V and $R(K = \langle V, R \rangle)$ . (2) The variables set consists of three different subsets. Input variables re considered to represent manifested symptoms or instances of the managerial problem under diagnosis. Part or all of these symptom variables are (continuously or periodically) monitored by a monitoring system, which could be another part of a whole diagnostic system. The set of output variables are considered to be a collection of all possible ultimate causes of the symptoms or the superset of the instances manifested (this is sometimes called “the frame of discernment” in Dempster–Shafer’s evidential reasoning theory [71]). Intervening variables lie between the manifested symptoms and the ultimate causes, and connect those two classes of variables to result in paths between the two classes. This is illustrated in fig. 4.

(3) The relationships set also consists of three different types: IS\_CAUSED\_BY, IS\_A, and IS\_PART\_OF. These three types of relationship have important common properties for the representation in CIROS. The common properties are: (i) transitivity; (ii) anti-symmetry; and (iii) irreflexiveness. Therefore, each relationship type constitutes its own partial ordering. This partial ordering enables the relationship structure to be built as hierarchical. Because of these common properties, CIROS does not differentiate the three types of relationship for its theoretical development (although, they are different in semantics).

Based on the fundamental assumptions about the knowledge of managerial problem diagnosis, CIROS represents its knowledge as follows (design constructs of CIROS).

## 5.1. Network representation of knowledge

In this study, all the knowledge about a managerial problem is represented in a network of cells (sometimes called nodes) and directed links (sometimes called arcs or connections or edges).

Each cell simply represents a variable and each directed link represents a relationship between two variables.

5.2. Embedded knowledge base in the reasoning system

In conventional expert systems, they usually have three separate major components: User interface, knowledge-base, and reasoning component (or inference engine). However, the connectionist takes a different approach to building knowledge-based systems. The most important single difference is that knowledge and reasoning (inferencing) are entangled into a single component [66,29].

## 5.3. Representation of uncertainty and inexactness

Associated with each cell is its value from the continuous range of $[-1, 1]$ , which represents the degree of truth, where the value 1 means a perfect (100% confidence in) truth, -1 means perfect (100% confidence in) falsity, and 0 means perfectly neutral or unknown (0% confidence in truth or falsity). This number will be called the certainty factor (of an entity/object/event) from now on. Associated with each link is its value from the continuous range of $[-1, 1]$ , called weight. The value 1 means a perfect (positive) correlation between the two variables that are connected by a link and -1 means a perfect (negative) correlation between the two variables. Zero weight means no correlation (or independence) between the two variables.

## 5.4. One-cell-one-concept representation (non-distributed representation)

Each node or cell in CIROS represents a single concept or variable. It does not incorporate distributed representations. One possible implication of this principle is that, by adopting this principle, CIROS can be applied to the problem-solving tasks that involve highly abstract and qualitative concepts or variables. The reader who has an interest in the differences between distributed representations versus non-distributed representations may consult Hinton and Sejnowski [34].

## 5.5. Acyclic layered network

The original knowledge structured (of a manager), if represented in a network, might involve loops or cycles. In CIROS, it is restructured to resolve the abstraction level imbalances of the variables that are represented by cycles or other contradictions to the assumptions before it performs any inference or learning process. The restructured knowledge, balanced in the abstraction level of the variables, will be represented as a hierarchical, layered network.

## 5.6. Knowledge update by inferencing (update of fact-type knowledge)

CIROS changes (or updates) its knowledge basically in two ways. One way is by inferencing, and the other is by learning. Knowledge updates by inferencing in CIROS mean changing (or updating) the values of its cells (variables). It is assumed that updating of cell values occurs simultaneously within a layer, but it occurs serially across the different layers (top-to-bottom or bottom-to-top).

5.7. Knowledge update by learning (update of rule-type knowledge).

CIROS can modify its pattern of connectivity as a part of the learning process. Modifying the pattern of connectivity (thus learning) means changing (or updating) the weight that is associated with each link in CIROS. However, it is assumed that inference and learning are separate processes in CIROS.

The overall architecture of CIROS that is constructed based on the design principles closely resembles causal diagrams used in system dynamics or causal models used in other causal modeling methodologies such as KSIM [39]. However, there are a number of important differences between CIROS and the causal models:

(1) the main purpose of building CIROS is to represent the domain knowledge (that is heuristic and experiential) and subsequent inferential computation. On the other hand, the principal purpose of causal models is to model and analyze causal systems;

(2) CIROS is designed to handle a large number of relevant variables, and more importantly the relationships between these variables need not be limited to causal relationships, while those in causal models are;

(3) CIROS assumes hierarchical, layered, and acyclic network structures with synchronous timing in updating their status. On the other hand, causal models assume general network structures with asynchronous timing in updating their status;

(4) CIROS supports weighted relationships (representing degree of influence) whereas the signed digraphs utilized in causal models do not.

In table 1 a summary of two terminologies is given contrasting between the one for CIROS or connectionist paradigm and the other for usual managerial thought.

## 6. Architectural design of CIROS

Based on the principles described in the previous section, CIROS works in three stages: (i) network structuring; (ii) learning; and (iii) infer-

![](/api/attachments/NH4ANU7Q/fulltext/images/7ae02abbbfb90aae98879f906958790512750603b2a98a98d8cd21e14143ede3.jpg)  
Fig. 5. An initial managerial knowledge network with initial weight values.

Table 1  
A comparison of terminologies.

<table><tr><td>CIROS/Connectionist terminology</td><td>Managerial problem diagnostic interpretation</td></tr><tr><td>Cell (Node)</td><td>Variable (symptoms, causes, intervening variables)</td></tr><tr><td>Link (Arc/Connection)</td><td>Relationship</td></tr><tr><td>Layer</td><td>Class of variables</td></tr><tr><td>Output layer</td><td>Set of ultimate causes (Frame of discernment)</td></tr><tr><td>Input layer</td><td>Set of symptoms</td></tr><tr><td>Cell output</td><td>Value of variable</td></tr><tr><td>Cell activation</td><td>Net influence from related variables</td></tr><tr><td>Weight</td><td>Degree of influence</td></tr></table>

encing. However, these three stages do not necessarily take place in sequence, although network structuring stage should take place before any process for inferencing or learning takes place. In the following, each stage is discussed from an architectural viewpoint.

## 6.1. Network structuring

This phase is basically a process of initializing knowledge structure for inference and learning of CIROS.

The input for this process is a raw form (network) of an expert's knowledge structure, which is simply the set of relevant variables $(V)$ for the given problem and the set of relationships between the variables $(R)$ ( $K = \langle V, R \rangle$ ). The output of the process is a reformed knowledge structure, which is free of loops/cycles and is a layered network. The network structuring basically consists of three tasks: Structuring the initial network, removing all loops/cycles in the initial network, and layering the cycle-free network. In the following, each task is discussed.

## 6.2. Structuring the initial knowledge network

This subtask involves structuring a raw from network of an expert's knowledge, labelling each component of the network, and specifying initial relationship (or dependency) information between cells (initializing weight for each link).

Structuring a raw form network in CIROS is, in general, what is called knowledge acquisition and elicitation in Al and expert systems. Knowledge acquisition and elicitation from human experts is, in general, known as a very complex and poorly-understood task [28]. Interpretive structural modeling (ISM) [81] is just one of several approaches to knowledge acquisition and elicitation. ISM can be used to create the required analog object structure. ISM supports the construction of digraph representations of a contextual relation among a set of elements. ISM's purpose and function is to extract from an individual or group the essential structure of a problem, process, situation, or system. The process begins by enumerating a set of variables (called "elements") and a contextual relation by which the elements will be interacted. The end result is a digraph like that in fig. 5; the required steps of the process are summarized in table 2.

Although knowledge acquisition and elicitation has much significance, it is not a main task of CIROS. Instead, CIROS starts with a given raw from knowledge network much like the raw form networks that can be created using ISM. A hypothetical, but realistic, diagnostic example of a managerial knowledge network is given in fig. 5. For illustration, all variables and the causal relationships among them are already given (in the figure).

When CIROS starts to operate initially, there is no information on weights that play a critical role in its inferencing tasks. In CIROS, initialization of weights can be done by directly accepting values from the managers (human experts). However, as CIROS performs learning in the later learning stage, these initial weights are supposed to change. The purpose of specifying the initial weights is to expedite the learning process (later) by directly exploiting human experts' knowledge, and to make easier the process of removing cycles and layering the network.

Table 2  
Steps of the ISM process.

<table><tr><td>Phase 1</td><td>Preconditioning guidelines (computer and participants)Theme: (purposes and objectives)Perspective: (whose?)Mode: (descriptive or prescriptive)Primitives: s, the element set; R, the contextual relation</td></tr><tr><td>Phase 2</td><td>Fill the reachability matrix (computer and participants)a. Partition the element set s and fill subsystem matricesb. Fill the interconnection matrices</td></tr><tr><td>Phase 3</td><td>Extract a hierarchical ordering (computer only)</td></tr><tr><td>Phase 4</td><td>Determine a minimum edge digraph (computer only)</td></tr><tr><td>Phase 5</td><td>Make adjustments as necessary (participants)a. Revise digraphb. Replace element numbers with names and redraw the digraph</td></tr></table>

When the system initializes each weight, it is recommended that only one value, i.e., one number selected from $\{-1, -0.5, 0, 0.5, 1\}$ should be used. The reason is that humans are very weak in providing some specific weights from a continuous range of values ( $[-1, 1]$ ). Rather, they are more comfortable and show consistency when they are working with binary or ternary values (with direction (minus or plus sign) [38]). So, for this case, the weight 1 between two cells represents belief in a strong positive correlation between them, 0.5 represents belief in a weak or middle range influence, and 0 represents belief in no influence.

If no initial dependency information is available, all weight matrices are initialized to zero. As stated earlier, however, these will change during the (later) learning stage.

In this initial stage, CIROS may start with directional dependency information with only perfect strength for each dependency, i.e., either -1 or 1 for each link. In fig. 5, all the dependency information is given only by the existence of links and their directions with either plus or minus sign. In a sense, this is more desirable than pushing the human expert to get specific numbers for the strength of each link because it is usually expected that this initial dependency information will be changed in later processes (restructuring the knowledge network and learning). Thus, human experts will be entering 1, 0, or -1 for the strength of each link, initially. In a sense, a knowledge network with N variables can be considered to start with zero weight for all its possible $N(N-1)/2$ connections.

The knowledge network in this initial stage may contain loops/cycles and is not layered at all. In fact, there is one cycle in fig. 5 (Production rate → Inventory → Production adjustment → Production rate). These cycles should be removed and the network needs to be restructured to form a layered, hierarchical network. The reason for doing this is stated in the subtask “Layering the Knowledge Network”.

## 6.3. Removing cycles

The initial network is structured as a general network structure. Since CIROS has the function of checking the presence of any cycle in the raw form knowledge network, users do not have to worry about that in the initial stage. This is one way that CIROS provides facilities to users do not feel constrained by the underlying computational structure. The process of removing cycles consists of finding all cycles, clustering all the variables in each cycle into a clustered, larger-class variable, and restructuring the network. Some authors called this “condensation” [81,31]. In the following, this is discussed in turn.

There are a number of algorithms for finding all loops/cycles in a network [23]. However, all of them require exponential time. In fact, this graphic problem (finding all cycles in a network) is known to be a subclass of the Hamiltonian circuit problem and thus belongs to the NP-complete class [58]. The cycle detection algorithm used in CIROS is given in table 3. Using this

A cycle detection algorithm. V is the set of all nodes $(v_{1}, v_{2}, \ldots, v_{N})$ . C contains cycles. And P is the current path that is being examined. This algorithm works basically by examining the existence of a cycle recursively for every node in the digraph.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Cycle detection algorithm

Input: A directed graph G =  $\langle V, R \rangle$  for the network
K =  $\langle V, R \rangle$ 

Output: All cycles/loops in G

Algorithm:
For every  $v_{i}$  in V (i = 1, 2, ..., N), do
1. Path ( $v_{i}$ )
1.1 Mark  $v_{i}$  visited
1.2 Set C =  $\{v_{i}\}$  and P =  $\{v_{i}\}$ 
1.3 Set S =  $\{v_{j}, \ldots, v_{k}\}$ 
(all direct successors of  $v_{i}$ )
1.4 If (S == { }, then exit Path( $v_{i}$ )
1.5 Else
1.5.1 if ( $v_{j} == vi$ ), then set C =  $\{v_{i} \rightarrow v_{j}\}$ 
and report a cycle
1.5.2 else Set P =  $\{v_{i} \rightarrow v_{j}\}$ 
1.6 Path( $v_{j}$ )
</div>

algorithm, only one cycle is found in the knowledge network of fig. 5 (Production rate → Production adjustment → Inventory → Production rate).

The next step is for CIROS to ask a user (or an expert) what shall be the name for the clustered variable. This is a process of restructuring the knowledge network into one whose variables are conceptually balanced, i.e., they are balanced in abstraction level. In fig. 6, it is assumed that the three variables in the cycle are condensed into a single variable and renamed to be “Production rate” for the variable.

## 6.4. Layering the knowledge network

This process is required because CIROS is not a feedback system and back-propagation of intermediate information is not allowed. There are three reasons for structuring the knowledge network to be a layered one in CIROS.

First and most importantly, layering the knowledge structure makes CIROS computationally efficient for learning and inference. This computational speed is needed because of the real-time characteristic of managerial decision support systems. It should be apparent that, if there are L layers each consisting of N nodes, the computational complexity is of order $O[N(L-1)]$ for unlayered knowledge networks, whereas the computational complexity is of order O[N] for layered networks.

Second, the synchronization problem (in inference and learning) can be much simpler. Asynchronous neural network systems are much more complex to design and implement, whose analyses typically involve complicated differential (or difference) equation systems. By adopting a hierarchical, layered structure, CIROS can easily assume a synchronous timing mechanism.

![](/api/attachments/NH4ANU7Q/fulltext/images/f916dc78361edb232bada5ced6ce92bf0fef05309b2c5d2ba7340484b29a2ec5.jpg)  
Fig. 6. An acyclic managerial knowledge network. In this figure, the variable Production Rate becomes a condensed one from Production Rate, Production Adjustment, and Inventory in fig. 5 to remove the cycle.

![](/api/attachments/NH4ANU7Q/fulltext/images/a15791dbbe253334d51a73c2b1905d34d91b337de41c084ffe87a4fc71f06c74.jpg)  
Fig. 7. A partially layered network.

Third, layering could give users (or experts) new insight to their old knowledge. Since each layer in CIROS could be given some meaning in the context of the whole knowledge network, users might get some new perspectives and perceptions of their problems.

A partially layered network (PLN) Algorithm developed by Jung [37] is applied to the acyclic network in fig. 6, resulting in the partially layered network shown in fig. 7.

A completely layered network is one in which no arc (or edge) extends further than a single layer. An example is shown in fig. 8. Again, Jung [37] provides formal definitions, theorems, and an algorithm (described in table 4) for conversion of a PLN to a CLN. A CLN is one that is completely consistent with conventional acyclic connectionist architectures.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
A CLN algorithm.

Input: A PLN  $G = \langle V_{L}, R_{L} \rangle$ 

Output: A CLN  $G' = \langle V_{L}', R_{L}' \rangle$ 

Algorithm:

1. Set k = 0
2. Set  $V = V_{k}$ , p = 0
3. For each member  $v_{j}$  of V
3.1 Set  $W = \{w_{i} | (w_{i} \leftarrow v_{j}) \in R_{L}\}$ 
3.2 Set d = the layer number of  $w_{i}$ 
    - the layer number of  $v_{j}$  (which is k)
3.3 For (d = 2; d &lt; L; d++)
</div>

Real-world examples of PLN and CLN networks are provided in figs. 9 and 10. In fig. 9 notice that there is some flexibility in layering the knowledge structure. For example, sales cost can be in any of layers 1–4 (in fig. 9, it is in layer 4).

![](/api/attachments/NH4ANU7Q/fulltext/images/5185a80148cd8fd4df1833670535e5ddc7db5701e4ee565f56a526ac219feb4d.jpg)  
Fig. 8. A completely layered network.

![](/api/attachments/NH4ANU7Q/fulltext/images/10bf5b9cbbbb5c66f83be6ed5e7c18e28bae51a6cf443920a313236746d0b0ff.jpg)  
Fig. 9. A partially layered knowledge network.

That kind of flexibility is always true for partially layered networks that are not completely layered. To fix the layer level for the nodes that have this flexibility (in layering), CIROS assumes that any pair of nodes that are directly connected by a link should be as far away as possible in terms of layers. The layered network in fig. 9 is structured based on this assumption.

The final step in CIROS's network structuring is to convert the partially layered (knowledge) network (PLN) into a completely layered (knowledge) network (CLN). This is done by introducing dummy cells (variables). For example, Turn-over rate and demand are directly connected to economic conditions in the PLN in fig. 9. But there is one layer gap between the layer (layer 3) where demand lies and the layer (layer 5) where economic conditions lies, and four layers gap between turn-over rate (layer 0) and economic conditions (layer 5). For these cases, CIROS needs exactly the same number of dummy cells as the number of layers gap. In fig. 10 a completely layered knowledge network that is converted from the partially layered network in fig. 9 is given as an example.

## 6.5. Inferencing

The main purpose of CIROS is to find the causes under the frame of discernment for the observed symptoms. In pursuit of this purpose, CIROS computes the certainty degree of the inferred causes based on the knowledge network structure. Therefore, inexact inferencing in CIROS is a computational process of finding the ultimate causes and generating certainty numbers for the inferred causes. Inferencing can be divided into the following subtasks:

(1) finding (ultimate) causes for the observed symptoms under the frame of discernment;

(2) computing the certainty numbers for the causes;

(3) finding unknown cells (variables) that are keys for further inferencing; and

(4) producing justifications/explanations for the conclusion.

In the following, each of these subtasks is discussed in turn.

6.6. Finding causes for the observed symptoms (forward chaining)

In CIROS, this is basically a repeating process of “generate (or find) hypotheses and test (or examine) them” to find out the eventual causes of the given symptoms. This task can be described formally as follows: Given a symptom set $S = \{s_{1}, s_{2}, \ldots, s_{s}\}$ , where $s_{i}$ is an individual symptom

![](/api/attachments/NH4ANU7Q/fulltext/images/4f7c7ec31923332b46afcc7b295c6b9d46589d3384f992080e5ca2d8af1bedab.jpg)  
Fig. 10. A completely layered knowledge network. This figure is continued on the next page. The numbers at the bottom (1 through 15) and the corresponding numbers at the top of the next page are provided to represent the continuation of the connections. In this figure, each dummy cell is named as "D" followed by its proper index. A cell's first index indicates the number to which the layer belongs.

![](/api/attachments/NH4ANU7Q/fulltext/images/d28d7c9c17fd33d62cd798f0ef4eb0656ea69ca40fa2c94ce3e6edf1a3b04117.jpg)  
Fig. 10. (continued)

$(i=1,2,\ldots,s)$ and turned out to be true or false, i.e., its value turned out to be 1 or -1, find the set of causes $C=\{c_{1},c_{2},\ldots,c_{c}\}$ , where each $c_{k}(k=1,2,\ldots,c)$ is the ultimate cause of one or more of the $s_{i}$ 's. This problem can be stated more formally as follows. In the Cartesian space $S\times C$ , where S is the set of all possible symptom elements and C is the set of all possible ultimate cause elements, find a subset of $S\times C$ that the subset is equal to the result of successive composite mappings in the given layered network.

Since CIROS is working on acyclic knowledge networks, the task can be viewed as a problem of graph search [3]. CIROS can solve the (graph search) problem by using existing algorithms. Two most widely known are the depth-first search and breadth-first search algorithms. Both have the same computational complexity [3]. It is O(max[n, e]) for a single node, where n is the total number of nodes and e is the number of edges in a digraph. For s nodes, the time complexity should be O(s max[n, e]). Both depth-first and breadth-first search can be used in CIROS. However, depth-first search was chosen for CIROS' inference task. This does not imply that CIROS cannot do multiple lines of reasoning. Rather, multiple lines of reasoning is inherently built into CIROS because of its parallel computational structure. This feature is useful for other reasoning tasks such as justifying/explaining conclusions.

In table 5, an algorithm for depth-first search is provided. This is a variation of the one in [3], adopted to fit into CIROS' problem domain (inagerial problem diagnosis). For example, consider the knowledge structure given in fig. 9. Assume that the input values are: The knowledge structure K exhibited in fig. 9 is a partially layered knowledge network; and Symptom set $S = \{s_{2} \text{ (net profit)}, s_{3} \text{ (turn-over rate)}\}$ , where the value of $s_{2} = 1$ and that of $s_{3} = -1$ .

For $s_2$ (net profit), there are sixteen possible causal paths as shown in fig. 11. For $s_{3}$ (turn-over rate), there are two possible causal paths in fig. 12.

![](/api/attachments/NH4ANU7Q/fulltext/images/f0cf17b22acdf0bcfb07a8414891a435e9ba9e66aab0694faea24824be40641b.jpg)  
Fig. 11. Casual paths for net profits.

Finding the most plausible one or, in general, ranking the possible causal paths from the most probable to the least probable can be done in two ways: One method is to use the weights information in CIROS's knowledge structure; and the other is to rely on empirical tests on all the variables on the causal paths. The second method is typically used in experimental research or medical diagnoses where precise examination for the given problem is required, and time and diagnostic resources (such as experimental resources and data) are fully available. In a managerial diagnosis, this method is difficult to adopt because it typically involves too many hypotheses to test. The first method, which is employed in CIROS, will be discussed next.

## 6.7. Computing certainty numbers for the hypothetical causes

Computing certainty numbers for the hypothetical causes is one of the major functions of CIROS and has significant implications. Computation of certainty factors should not be confused with computation of probabilities. As stated earlier in this article, a certainty factor for a confidence measure (for an entity/object/event)

![](/api/attachments/NH4ANU7Q/fulltext/images/e45b00e04a6171ee069ba22d971ef954000f667c0f42e63a66328e1d6af1ed10.jpg)  
Fig. 12. Causal paths for turn-over rate.

should be differentiated from a probability which is another type of uncertainty measure (for an entity/object/event) in other inexact reasoning systems such as PROSPECTOR, CONVINCE, etc.

For the computation of certainty factors, it is computationally more convenient and efficient to use a completely layered knowledge network such as the one shown in table 5. In the following, a mathematical formulation of the computation process is presented, followed by an example using the knowledge network in fig. 10. In fig. 13, a general case of a completely layered knowledge network is given. The computation process can be mathematically expressed as a system of equations that involve activation and output of each cell and a weight matrix for each layer (except the input layer). In CIROS, the activation level $x_{ki}$ of the ith cell in the kth layer is given as

```txt
Table 5
A depth-first search algorithm.

Input: • A partially or completely layered knowledge network K = ⟨V, R⟩
• Symptom Set S = {s₁, s₂, ..., sₛ}

Output: The set of causes C = {c₁, c₂, ..., c_c} for S

Algorithm:
1. Set S' = {s₁, s₂, ..., sₛ}
2. For each sⱼ in S', do
2.1 Set Pⱼ = { }, where Pⱼ is the set of causal paths directed from sⱼ
2.2 Set v = sⱼ, where v is the current node
2.3 Set P = { }, where P is the current causal path
2.4 Procedure Depth(v)
2.4.1 Put v in P and mark v visited (or examined)
2.4.2 Set T = {n | n is a successor of v which is not visited (examined) yet}
2.4.3 If T is empty, then exit the procedure
2.4.4 For each n in T, do
2.4.4.1 If |wvn| > δ,
    then connect n to v and
    put it in P = {n → v → · · · }
2.4.4.2 Set T = T - {n}
2.4.4.3 Set v = n
2.4.4.4 Procedure Depth(v)
2.5 Put P in Pⱼ
2.6 Goto 2.
3. Set Pₐₗₗ = {P₁, P₂, ..., Ps}.
```

$$
\begin{array}{l} x _ {k i} = \sum_ {j = 1} ^ {N _ {(k - 1)}} w _ {k i j} Y _ {(k - 1) j}, \\ k = 1, \dots , L, i = 1, \dots , N _ {k}, \end{array}\tag{1}
$$

where $w_{kij}$ is the weight from the jth cell in the $(k-1)$ th layer to the ith cell in the kth layer, and $y_{(k-1)j}$ is the output level of the jth cell in the $(k-1)$ th layer. The output $y_{ki}$ of the ith cell in the kth layer is given as

$$
y _ {k i} = f _ {\mathrm{k}} (x _ {k i}) = \tanh (x _ {k i}), \quad i = 1, \dots , N _ {k},\tag{2}
$$

where $f_{k}$ is an output function which is the same for all cells in the kth layer. If we employ vector and matrix notations, (1) becomes

$$
\boldsymbol {x} _ {k} = \boldsymbol {W} _ {k} \boldsymbol {y} _ {k - 1}, \quad k = 1, \dots , L,\tag{3}
$$

where $x_{k}$ is the activation vector of the kth layer, $W_{k}$ is the weight matrix, and $y_{k}$ is the output vector, both for the kth layer. Equations (2) become

$$
\mathbf {y} _ {k} = f _ {\mathrm{k}} (\mathbf {x} _ {k}) = \tanh (\mathbf {x} _ {k}).\tag{4}
$$

The reason for adopting the hyperbolic tangent function as the output function is as follows. In CIROS, a cell output function $f(x)$ , where x is the cell's activation level, is desired to satisfy the following criteria:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(1) $f:\mathbb{R}\to [-1, + 1]$ , continuous;   
(2) $f(x) = 0$ when $x = 0$   
(3) $f(x) = -f(-x)$ (symmetricity);   
(4) algebraic simplicity; and
</div>

![](/api/attachments/NH4ANU7Q/fulltext/images/2571d3d2532f0c08480b756670c3567df8a6e57bd31670596ba3dea0334f5f4d.jpg)  
Fig. 13. A general case of a completely layered knowledge network.

(5) uniform monotonicity (continuously differentiable and non-decreasing on the range of activation values).

For satisfying these criteria, the hyperbolic tangent function is most appropriate [41]. In fig. 14 a typical output function is presented.

![](/api/attachments/NH4ANU7Q/fulltext/images/e4ca442ee2d20c876be6b6a58905e1cf49d009c3a7858b0429f93786a97c9705.jpg)  
Fig. 14. A typical output function.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 6
A forward computation algorithm.

Input: Symptom vector  $y_{0}$ 
Output: Cause vector  $y_{L}$ 
Algorithm:
For each k = 1, 2, ..., L, compute iteratively and successively, the activation vector,
 $x_{k} = w_{k} \cdot y_{k-1}$ ,
and the output vector,
 $y_{k} = f_{k}(x_{k})$ $= \tanh(x_{k}), k = 1, \ldots, L.$
</div>

Notice how a completely layered knowledge network (CLN) allows all required computations to be performed in a simple manner. As can be seen in eqns. (3) and (4), the required computation is a simple successive and iterative process starting from $y_{0}$ (which is given) and eventually yielding $y_{L}$ . The algorithm for computation of certainty numbers is presented in table 6.

For a computational example, a small part of the knowledge network in figure 10 is given in fig. 15. In this case, the symptom set $S = \{\text{turn-over rate, demand, growth rate}\}$ . Assume that the input vector is

$$
\boldsymbol {y} _ {0} = \left[ - 1, - 1, 0 \right] ^ {\mathrm{T}}.
$$

These values connote low turn-over rate, low demand and no information about growth rate.

Then, iteratively and successively, the activation level of layer 1 is $[-1 - 10]^{T}$ . This can be interpreted as the summation of net influences of the symptom set on the two dummy variables and market share (see fig. 15).

$$
\begin{array}{r l} & y _ {1} = f (x _ {1}) = \operatorname{tanh} (x _ {1}) \\ & \quad = \left[ \begin{array}{l} \tanh (- 1) \\ \tanh (- 1) \\ \tanh (0) \end{array} \right] = \left[ \begin{array}{c} - 0. 7 6 1 6 \\ - 0. 7 6 1 6 \\ 0. 0 0 0 0 \end{array} \right]. \end{array}
$$

The certainty values for the two dummy variables and market share is -0.7616 and 0.0, respectively.

$$
\begin{array}{r l} \boldsymbol {x} _ {2} & = \boldsymbol {w} _ {2} \boldsymbol {y} _ {1} = \left[ \begin{array}{c c c} 1 & 1 & 0 \\ 0 & 0 & - 1 \end{array} \right] \left[ \begin{array}{c} - 0. 7 6 1 6 \\ - 0. 7 6 1 6 \\ 0. 0 0 0 0 \end{array} \right] \\ & = \left[ \begin{array}{c} - 1. 5 2 3 2 \\ 0. 0 0 0 0 \end{array} \right], \\ \boldsymbol {y} _ {2} & = f (\boldsymbol {x} _ {2}) = \operatorname{tanh} (X _ {2}) = \left[ \begin{array}{c} \tanh (- 1. 5 2 3 2) \\ \tanh (0. 0 0 0 0) \end{array} \right] \\ & = \left[ \begin{array}{c} - 0. 9 0 9 3 \\ 0. 0 0 0 0 \end{array} \right]. \end{array}
$$

This can be interpreted as fairly strong negative belief in (good) economic conditions and neutral effect on sales price, given low turn-over rate, low demand, and no information on growth rate.

![](/api/attachments/NH4ANU7Q/fulltext/images/0562e4def010a4b2096bc47e8b401f829d8c718e8e922142c80dc4a51a7b8a5c.jpg)  
Fig. 15. Part of a managerial knowledge network.

When CIROS performs inferencing, it is usually possible to compute the output and activation for a cell without knowing all the values of its input cells. Notice that if some of its input cell values are 0 (which means that the information on those cells is unknown or irrelevant to the target cells), then such values do not influence the activation value of the target cell (they are neutral to the target object at the particular moment). This capability of computing based on incomplete information is one of the strengths that CIROS and general connectionist models possess. Also this capability contributes to the overall system's robustness.

## 6.8. Finding unknown but important variables (backward chaining)

As was just discussed, CIROS performs its inferences even if it is provided with only partial (input) information. In this case, CIROS treats the values of non-specified variables to be zero, thus making these variables neutral in the inferential computation. However, this is not necessarily desirable from a sound reasoning viewpoint. CIROS is able to find out missing but important variables, and advise users to examine those variables and provide the values.

In CIROS, this can be done in two ways. First, if a user has weights for all final possible causes, i.e., an output vector for the output layer (top layer), which can be considered as the user's (human expert's) prior knowledge about the causes before they get any evidences, then the input vector for the input layer (bottom layer) can be computed using the composite weight matrix. The composite weight matrix can be obtained by multiplying $|W_{1}|$ and $|W_{2}|$ , then $|W_{2}|,\ldots$ , and finally $|W_{L}|$ , where $|W_{i}|$ (for $i=1,2,\ldots,L$ ) means the weight matrix that is obtained by taking the absolute value of each weight element of $W_{i}$ . This $|W_{i}|$ is called the absolute weight matrix. Finally, the input vector is computed by multiplying the output vector with the transpose of the resulting composite absolute weight matrix. Mathematically, if the output vector $u_{L}$ is given, then the input vector $u_{i}$ can be computed as follows, assuming $u_{0}$ is of appropriate dimension.

$$
\boldsymbol {u} _ {i} = | \boldsymbol {W} | ^ {\mathrm{T}} \boldsymbol {u} _ {0},\tag{5}
$$

where the composite absolute weight matrix $|W|$ is computed as follows.

$$
\mid \boldsymbol {W} \mid = \mid \boldsymbol {W} _ {L} \mid \dots \mid \boldsymbol {W} _ {2} \mid \mid \boldsymbol {W} _ {1} \mid ,\tag{6}
$$

where the matrices $|W_{i}|$ are of compatible dimensions, and ordinary matrix multiplication is used. The vector $u_{i}$ for the input layer represents the collection of importance values for every input variable. If this importance value for an input variable is above some standard, say 0.5, but its certainty factor is unknown, then this input variable should be examined and provided with its value. This topic is discussed in [12]. However, this method seems more appropriate for planning tasks rather than diagnostic situations because it is not likely that human users can provide the output vector for the output layer before diagnostic reasoning.

The second method is similar to the first one, but assumes the same importance values for all the (possible) cause variables (in the top layer). This amounts to assuming the values of all the elements of the output vector are the same. Assume that these are unit values, i.e.,

$$
\boldsymbol {u} _ {0} = \left[ \begin{array}{l l l l} 1 & 1 & \dots & 1 \end{array} \right] ^ {\mathrm{T}}.\tag{7}
$$

Then, by substituting (7) into (5),

$$
\boldsymbol {u} _ {i} = | \boldsymbol {W} | ^ {\mathrm{T}} \boldsymbol {u} _ {0},
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 7
An algorithm for finding the missing but important input cells.

Input: CLN with Weight Matrices $W_1, W_2, \ldots, W_L$
Output: Composite absolute weight matrix C Missing/important input cells

Algorithm:
1. Compute the absolute weight matrices
$|W_1|, |W_2|, \ldots, |W_L|$
2. Compute $C = |W_1| \cdot |W_2| \cdot \cdots |W_L|$
3. For (j = 1; j &lt;= s; j++) /* where s is the dimension of the input vector */
3.1 Compute
$s_j = \sum_{i=1}^{c} c_{ij}$
/* where c is the dimension of the output vector */
4. For (j = 1; j &lt;= s; j++)
4.1 If ((s_j &gt;= \delta) &amp;&amp; (y_{0j} = 0))
4.2 Ask the user to provide the value of y_{0j}.
</div>

or

$$
U _ {i} = \left[ \begin{array}{c} \sum_ {j = 1} ^ {N _ {L}} | \boldsymbol {w} _ {j 1} | \\ \sum_ {j = 1} ^ {N _ {L}} | \boldsymbol {w} _ {j 2} | \\ \vdots \\ \sum_ {j = 1} ^ {N _ {L}} | \boldsymbol {w} _ {j N 0} | \end{array} \right]
$$

For each input variable $n = 1, 2, \ldots, N_{0}$ , the ith element of $u_{i}$ is read and checked to ascertain if its current value is unknown. If it is, then CIROS asks users to examine that input variable and provide its value. An algorithm to compute the composite absolute weight matrix and find the missing but important variable values using the computed matrix is presented in table 7. Notice that in this algorithm, any prior information on the importance of any variable is not assumed.

When human users are asked to answer for CIROS to obtain the values of unknown cells, it is recommended that they respond with a number from $\{-1, -0.5, 0.0, 0.5, 1\}$ instead of a number from $[-1, 1]$ , as was explained earlier.

6.9. Producing justifications / explanations for conclusions (backward chaining)

One of the essential functions that an expert system should have is the capability of justifying the conclusions and explaining the reasoning processes $[22,19]$ . As an expert system, CIROS is no exception to this.

In CIROS, this capability is obtained by backward chaining on the knowledge network. A particular conclusion in CIROS is a subset of the Cartesian product space $S \times C$ involving the set S of symptoms and the set C of final causes with certainty numbers (the certainty vector y). To justify a conclusion is to build causal paths from C (the causes set) to S (the symptoms set). Also CIROS may be asked to explain how it obtained particular certainty numbers.

In the following, the direction of all the connections and links in the knowledge network will be reversed because the justification/explanation process in CIROS is the reverse of its diagnostic reasoning processes.

There are three modes of justification/explanation for general expert systems [13]. These are: (i) the rule query, where the text of relevant rules are shown; (ii) the why query, which inspects the path of reasoning the system is currently exploring; and (iii) the how query, which presents all paths that have led to a particular goal state. All three modes are available in CIROS and each of these is explained next.

The rule query. In CIROS, the rule query is a request by the user to display in a textual format (through the user interface facility) all the connections that lead to a particular cell (variable) along with the direction and the associated weight for each connection, and the cells connected by them. For example, in fig. 12, if a user queries the rules for turn-over rate, then CIROS displays the following two rules:

Turn-over rate ← Economic conditions:

$$
\text { weight } = + 1
$$

Turn-over rate $\leftarrow$ Job satisfaction: weight $= -1$ .

The why query (explanation). In CIROS, the why query is handled by tracking the single path and thus following the single line of reasoning on which the system is currently exploring. For example, if a user asks why the turn-over rate is affected by wage rate, CIROS responds by displaying the single path between the two variables on which it is currently examining, as follows.

$$
\begin{array}{c}\text { Wage   rate } \rightarrow \text { Job   satisfaction } \rightarrow \text { Turn - over   rate }.\\(+ 1) \quad (- 1)\end{array}
$$

The how query (explanation). In general expert systems, the how query from a user is handled by explaining how the system got to a particular conclusion. In CIROS, this is done by building all cause-symptom paths for the given set of symptoms, or if it is desirable (or requested by the user), by building all cause-symptom paths for each element in the symptoms set. An algorithm for this purpose is easily made by adding a backward chaining function to create the cause-symptom paths to the DFS algorithm (in table 5). Since the DFS algorithm builds symptom-cause paths (forward chains) for a given set of symptoms, it can be easily modified to build the cause-symptom paths (backward chains) for the same set of symptoms. The algorithm, named backward chaining (BWC), is presented in table 8.

```txt
Table 8
A backward chaining algorithm.

Input: • The reverse of partially layered knowledge network
K = ⟨V, R⟩
• Symptom Set S = {s₁, s₂, ..., sₛ}
Output: The set of cause-symptom paths {P₁, P₂, ..., Pₛ}
Algorithm:
1. Set S' = {s₁, s₂, ..., sₛ}
2. For each sⱼ in S', do
2.1 Set Pⱼ = { }, where Pⱼ is the set of causal paths directed to
sⱼ
2.2 Set v = sⱼ, where v is the current node
2.3 Set P = { }, where P is the current causal path
2.4 Procedure Depth(v)
2.4.1 Put v in P and mark v visited
2.4.2 Set T = {n | n is a predecessor of v which is not visited
(examined) yet}
2.4.3 If T is empty, then exit the procedure
2.4.4 For each n in T, do
2.4.4.1 If |wₙᵥ| > δ,
then connect n to v and
put it in P = {n → v → · · · }
2.4.4.2 Set T = T - {n}
2.4.4.3 Set v = n
2.4.4.4 Procedure Depth (v)
2.5 Put P in Pⱼ
2.6 Goto 2.
3. Report {P₁, P₂, ..., Pₛ}
```

## 6.10. Learning in CIROS

Human experts learn their expertise from experience. Learning expertise means building and updating their knowledge structure. Learning in CIROS takes place in a similar manner. Because CIROS represents its knowledge structure as a network of variables and relationships between these $(K = \langle V, R \rangle)$ , its structural change assumes adjustment and update of relationships between variables. In CIROS, this is done by adjustment of weight values between cells in different layers. Therefore, learning in CIROS means update of weight matrices to enable CIROS to perform correct inferencing (to find correct causes for the given symptoms).

Learning in CIROS can take place in two ways. Once the structure of the knowledge network has been determined, a learning process is required to update the weight values because in CIROS an essential information component is the weights and the initialized values are by no means complete and correct. The other way is execution of the learning module of the CIROS in the middle of its operation. This would be required as the whole problem diagnosis system and CIROS builds up cumulative errors or there is a sudden change in the operating environment.

The learning method adopted in CIROS is the generalized delta rule or back-propagation algorithm as suggested in $[68]$ . The power of a learning method (algorithm) depends on two factors: The speed (how fast it generates rules, or more technically, how fast it converges to a learning formula (equations)) and robustness (the algorithm is not biased or does not show abrupt behavior over diverse training examples). It is known that the generalized delta rule (back-propagation method) possesses these two desirable characteristics $[45,27]$ . This algorithm was developed by $[68]$ and is better known as the back-propagation method. It is one of most popular learning algorithms for neural networks $[45]$ . This algorithm is a generalization of the famous delta rule, which was first presented in $[65]$ .

## 7. Comments, conclusion and contributions

As a summary to this article, guidelines for designing connectionist inexact reasoning systems will be presented. These were fully described from an architectural viewpoint earlier. Discussion in this section emphasizes managerial diagnostic aspects and considerations.

Major design guidelines that can be extracted from the discussion of the CIROS architecture are listed as follows:

(1) multiple-layer structure that includes one or more intermediate layer(s);

(2) continuous input/output;

(3) hyperbolic tangent output function;

(4) back-propagation learning algorithm.

Each of these guidelines has special implications for managerial problem diagnosis as well as its own implications for computational architecture. In the following, each of these is discussed in turn.

Multiple-layer with one or more intermediate layer(s). For design of connectionist inexact reasoning systems, multiple-layer architecture with intermediate layer(s) is more appropriate for the problem area (managerial problem diagnosis) than single layer architectures with single input layer-output layer structure. The latter architectures do not exhibit the variety of behaviors required for inherently nonlinear managerial problems.

In the history of connectionist/neural nets theories, the limited capability of single-layer neural net once banned further study of the artificial computing systems (neural network systems) [67,45,52]. The limited reasoning capability of the single-layer neural networks was fully studied and demonstrated by Minsky and Papert [52].

An implication for managerial problem diagnosis is that a single-layer connectionist architecture can never produce a correct diagnosis when the frame of discernment (the output cause layer) includes mutually exclusive final causes. However, this can be easily cured by introducing one or more intermediate layers. For a more thorough discussion about this matter, see [66].

Another important implication of the single layer connectionist architecture for managerial problem diagnosis is that it can be interpreted as shallow knowledge versus the deep domain knowledge structure of a multiple-layer network $[50,35,17]$ . In medical and engineering systems diagnosis, it is known that in general, deep knowledge is more desirable than surface knowledge $[50,35]$ . In managerial problem diagnosis, the argument is still true because deep knowledge in the above sense corresponds more faithfully to robust knowledge modeling as discussed in the DSS literature $[20,8]$ .

In general, what is the appropriate number of intermediate layers for a given diagnostic problem? This can be answered by the knowledge structuring task of CIROS that was discussed previously. The number of intermediate layers should be determined by the PLN algorithm. Therefore, it depends on the specific diagnostic situation and the expert knowledge structure. Although, a multiple-layer structure with at least three layers should be preferable, the number of intermediate layers can vary in designing a specific CIROS.

Continuous input and output (cell) value. Another important design decision for CIROS is continuous versus discrete cell value range. In CIROS, each cell value represents the degree of truth (or falsity) or certainty degree. Although it is well known that human experts are poor in identifying a specific number from a continuous range such as $[-1, 1]$ , it is believed that the human's internal representation of degree of uncertainty about an entity/object/event is based on a rather continuous value range $[80,48]$ . Because one of the design criteria for CIROS is to make it closely resemble the reasoning process of human experts, adopting a continuous cell-value range is recommended.

The shape of the output function. The requirements for the shape of the output function were discussed in section 7. As a first requirement, the range of output values should be $[-1, 1]$ as just discussed. Second, it should be differentiable and non-decreasing on the range of (net) activation values of a cell to satisfy one of the conditions for applying the Back-propagation learning algorithm. Third, the shape of the output function should be symmetric so that it can better incorporate the tendency of symmetry in the human experts' uncertainty evaluation [48]. And finally, it should be simple and easy to manipulate mathematically. To satisfy the requirements presented, the hyperbolic tangent function (tanh) is believed to be the most appropriate one [41].

Back-propagation learning algorithm. For implementation of the learning function in CIROS, the Back-propagation method, originally named as generalized delta rule [68], is recommended as preferable to other neural net learning algorithms.

The primary contribution of CIROS is that it provides principles for design of inexact reasoning systems for managerial problem diagnosis. The design principles were derived by merging the technologies and principles of two contemporary computing fields: Expert systems/knowledge representation and the connectionist computational architectures. Although there are many inexact reasoning architectures whose design principles are based on a single traditional AI or expert systems technology (such as rule-based inexact reasoning systems), it is believed that the design of CIROS is the first attempt to utilize and synthesize two fields of computing technologies for managerial problem-solving.

The synthesis of the two computing technologies is significant in the following sense:

(1) In the real world, most managerial decision problems are very complex and ill-structured. And these problems become more complicated if they are associated with information imperfection. The result is severe degradation of the quality of the managers' decision.

Information imperfection in managerial decision-making is very diverse. For handling such diverse information imperfection, more conventional inexact reasoning systems such as rule-based systems are not very effective because they are based on declarative, explicit representation of (imperfect) information and knowledge. On the other hand, the knowledge representation in CIROS does not need to be declarative. The imperfection and inexactness are merged into the knowledge structure and inferencing is performed on the knowledge structure in a procedural (non-declarative) manner.

(2) More conventional inexact reasoning systems such as rule-based inexact reasoning systems do not attempt to organize the knowledge base. In contrast, CIROS performs restructuring of the knowledge base (knowledge network) as its first stage of operation. An important implication of this is that as the size of the knowledge base becomes larger, the reasoning of the rule-based systems on their knowledge base becomes unwieldy. The result of this may be a severe degradation in performance of these systems. Moreover, opportunities for inconsistency and incompleteness creep in.

On the other hand, CIROS reorganizes the knowledge structure into a hierarchical, layered form. The hierarchical, layered structure seems very natural to humans, and it is known to be very efficient for computation [79].

An implication of the reorganized knowledge structure for managerial decisionmaking is that CIROS can be very effective for aiding human managers to understand and solve the managerial decision problems in the real world that are typically very complex.

(3) The hierarchical, layered architecture of CIROS makes the formulation of a justification/explanation subsystem for connectionist models straight forward. One of the biggest criticisms levied against the connectionist models is the absence of a justification/explanation mechanism. The CIROS architecture obviates that criticism.

(4) The use of certainty factors in conjunction with a connectionist architecture has not been previously considered. It is believed that CIROS is the first inexact reasoning architecture that combines certainty factors with the connectionist computational architecture. Certainty factors have traditionally been adopted only in rule-based reasoning systems. Certainty factors enable CIROS to represent certainty in a non-declarative way and to make the computation of them hidden. This implies that the human users (or experts) do not have to be bothered to determine and provide precise (or exact) certainty numbers, that are very imprecise in human minds.

(5) Although it is frequently pointed out that a learning capability is very much desirable in managerial decision aiding systems, there are, to the authors' knowledge, very few systems with that capability (particularly, decision aiding systems for strategic management decision making). This article suggests a learning architecture that is suitable to the knowledge structure for managerial problem diagnosis.

In other words, when the knowledge network derived from the learning phase differs significantly from the user's belief structure, the user is challenged to reevaluate and reconcile his/her own belief structure in relation to the learned knowledge structure of CIROS. This reconciliation may result in additional learning experiments applied to the knowledge network. Ultimately, improvements to the user's own belief structure will accrue as a learning effect on the user.

## Acknowledgement

The authors are indebted to the referees for many helpful suggestions regarding appropriate revision of the article.

## References

[1] R.L. Ackoff, Creating the Corporate Future (Wiley, New York, 1981).

[2] R.L. Ackoff and M.W. Sasieni, Fundamentals of Operations Research (Wiley, New York, 1968).

[3] A.V. Aho, J.E. Hopcraft and J.D. Ullman, Data Structure and Algorithm (Addison-Wesley, Reading, MA, 1983).

[4] J. Anderson and G. Bower, Human Associative Memory (Winston, Washington, DC, 1973).

[5] N.H. Ata Mohammed, J.F. Courtney, Jr. and D.B. Paradice, A Prototype DSS for Structuring and Diagnosing Managerial Problems, IEEE Trans. on Systems, Man, and Cybernetics 18, No. 6 (1988) 899–907.

[6] D. Baldwin and G. Kasper, Toward Representing Management-domain Knowledge, Decision Support Systems 2, No. 2 (1986) 159–172.

[7] A. Barr and E.A. Feigenbaum, The Handbook of Artificial Intelligence, Vol. 1 (Addison-Wesley, Reading, MA, 1981).

[8] A. Basu and A. Dutta, Reasoning with Imprecise Knowledge to Enhance Intelligent Decision Support, IEEE Trans. on Systems, Man, and Cybernetics 19, No. 4 (1989) 756–770.

[9] P.P. Bonissone and R.M. Tong, Editorial: Reasoning with Uncertainty in Expert Systems, International Journal of Man-Machine Studies, 22 (1985) 241–250.

[10] M.J. Bouwman, Human Diagnostic Reasoning by Computer: An Illustration from Financial Analysis, Management Science 29, No. 6 (June, 1983) 653–672.

[11] B.G. Buchanan and R.O. Duda, Principles of Rule-Based Expert Systems, in: M.C. Yovits, Ed., Advances in Computers (Academic Press, New York, 1982) 164–216.

[12] J.R. Burns and M. Mahmood, Design and Development of a Decision Support System for Curriculum Design, Policy and Information 9, No. 2 (Dec. 1985) 77–94.

[13] C.W. Butler, E.D. Holdi and G.L. Richardson, Building Knowledge-Based Systems with Procedural Languages, IEEE Expert (Summer, 1988) 47–59.

[14] R. Carnap, Logical Foundations of Probability, 2nd ed. (University of Chicago Press, Chicago, IL, 1962).

[15] B. Carre, Graphs and Networks (Clarendon Press, Oxford, 1979).

[16] B. Chandrasekaren, Towards a Taxonomy of Problem-Solving Types, Al Magazine 4, No. 1 (1983) 9–17.

[17] B. Chandrasekaren and A. Goel, From Numbers to Knowledge Structures: Artificial Intelligence Perspective on the Classification Task, IEEE Trans. on Systems, Man, and Cybernetics 18, No. 3 (May/June 1988) 415-424.

[18] B. Chandrasekaren, A. Hoel, and D. Allemang, Connectionism and Information-Processing Abstractions, Al Magazine (Winter 1988) 24–34.

[19] W.J. Clancey, Viewing Knowledge Bases as Qualitative Models, IEEE Expert (Summer 1989) 9–23.

[20] J.F. Courtney, Jr., D.B. Paradice and N.H. Ata Mohammed, A Knowledge-Based DSS for Managerial Problem Diagnosis, Decision Science 18 (1987) 373–399.

[21] A.M. Darwish and A.K. Jain, A Rule Based Approach

for Visual Pattern Inspection, IEEE Trans. on Pattern Analysis and Machine Intelligence 10, No. 1 (Jan./Feb. 1986) 56–68.

[22] R. Davis, Expert Systems: Where are we? And where do we go from here? Al Magazine 3, No. 2 (1982) 3–22.

[23] R. Deo, Graph Theory with Applications in Engineering and Computer Science (Prentice-Hall, Englewood Cliffs, NJ, 1974).

[24] V. Dhar, On the Plausibility and Scope of Expert Systems in Management, Journal of Management Information Systems 4, No. 1 (1987) 25–40.

[25] R.O. Duda, P.E. Hart and N.J. Nilsson, Subjective Bayesian Methods for Rule-Based Inference Systems, Proceedings of National Computer Conference (1976) 1075–1082.

[26] A. Dutta, The Explicit Support of Human Reasoning in Decision Support Systems, in: M.C. Yovits, Ed., by Advances in Computers, Vol. 26 (Academic Press, New York, 1987) 1–45.

[27] S.E. Fahlman and G.E. Hinton, Connectionist Architectures for Artificial Intelligence, IEEE Computer (Jan. 1987) 100–108.

[28] B. Gaines, Foundations of Uncertain Reasoning, International Journal of Man-Machine Studies 22 (1976) 312–355.

[29] S.I. Gallant, Connectionist Expert Systems, Communications of the ACM 31, No. 2 (1988) 152–169.

[30] B.N. Grosof, An Inequality Paradigm for Probabilistic Knowledge: The Logic of Conditional Probability Intervals, in: L.N. Kanal and J.F. Lemmer, Eds., Uncertainty in Artificial Intelligence (North-Holland, New York, 1986) 259–275.

[31] F. Harary, R.Z. Norman and D. Cartwright, Structural Models: An Introduction to the Theory of Directed Graphs (Wiley, New York, 1965).

[32] Havens and Mackworth, A Computational Model of 3-D Pattern Recognition, IEEE Trans. on Pattern Analysis and Machine Intelligence 13, No. 2 (1983) 235–247.

[33] D.E. Heckerman and E.J. Horvitz, On the Expressiveness of Rule-Based Systems for Reasoning with Uncertainty, Proceedings of the Sixth National Conference on AI (July 1987) 121–126.

[34] G.E. Hinton and T.J. Sejnowski, Learning and Relearning in Boltzmann Machines, in: D.E. Rumelhart, J.L. McClelland and PDP Research Group, Eds., Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Vol. I: Foundations (MIT Press, Cambridge, MA, 1986) 282–317.

[35] E. Hollnagel, Commentary: Issues in Knowledge-Based Decision Support, International Journal of Man-Machine Studies 27, No. 2 (1987) 743–751.

[36] I.L. Jannis and L. Mann, Decision-making: A Psychological Analysis of Conflict, Choice, and Commitment (Free Press, New York, 1977).

[37] D.G. Jung, Design of Inexact Reasoning Systems for Managerial Problem Diagnosis, Ph.D. Dissertation (Texas Tech University, Lubbock, TX, 1990).

[38] D. Kahneman, P. Slovic and A. Tversky, Judgment under Uncertainty: Heuristics and Biases (Cambridge University Press, New York, 1982).

[39] J. Kane, A Primer for a New Cross-Impact Language-KSiM, Technological Forecasting and Social Change 4 (1972) 129–142.

[40] J.H. Kim and J. Pearl, CONVINCE: A Conversational Inference Consolidation Engine, IEEE Trans. on System, Man, and Cybernetics 17, No. 2 (Mar./Apr. 1987) 470–474.

[41] E. Kreyszig, Advanced Engineering Mathematics, 5th ed. (Wiley, New York, 1983).

[42] L. Lesmo, L. Saitta and P. Torasso, Evidence Combination in Expert Systems, International Journal of Man-Machine Studies 22 (1985) 307–326.

[43] H.J. Levesque, Knowledge Representation and Reasoning, Annual Review of Computer Science 1 (1986) 255-287.

[44] T.S. Levitt, Uncertainty in Artificial Intelligence (Workshop Report), Al Magazine (Winter 1988) 77–78.

[45] R.P. Lippmann, An Introduction to Computing with Neural Nets, IEEE ASSP Magazine (April 1987) 4–22.

[46] J. Martin and S. Oxman, Building Expert Systems: A Tutorial (Prentice-Hall, Englewood Cliffs, NJ, 1988).

[47] J. Maiers and Y.S. Sherif, Application of Fuzzy Set Theory, IEEE Trans. on Systems Man, and Cybernetics 15, No. 1 (Jan./Feb. 1985) 175–189.

[48] M.W. Merkhofer, Quantifying Judgmental Uncertainty: Methodology, Experiences, and Insights, IEEE Trans. on Systems, Man, and Cybernetics 17, No. 5 (Sep./Oct. 1987) 741–752.

[49] R.K. Miller and T.C. Walker, Artificial Intelligence Applications for Business Management, 2nd ed. (Prentice-Hall, Englewood Cliffs, NJ, 1988).

[50] R. Milne, Strategies for Diagnosis, IEEE Trans. on Systems, Man, and Cybernetics 17, No. 3 (May/June 1987) 333–339.

[51] M. Minsky, A Framework for Representing Knowledge, in: P. Winston, Ed., The Psychology of Computer Vision (McGraw-Hill, New York, 1975) 211–277.

[52] M. Minsky and S. Papert, Perceptron (MIT Press, Cambridge, MA, 1969).

[53] H. Mintzberg, D. Raisinghani and A. Theoret, The Structure of Unstructured Decision Process, Administrative Science Quarterly 21 (1976) 246–275.

[54] C.V. Negoita, Management Applications of System Theory (Springer-Verlag, New York, 1979).

[55] A. Newell and H.A. Simon, GPS: A Program that Simulates Human Thought, in: E. Feigenbaum and J. Feldman, Eds., Computers and Thought (McGraw-Hill, New York, 1963) 279–293.

[56] A. Newell and H.A. Simon, Human Problem Solving (Prentice-Hall, Englewood Cliffs, NJ, 1972).

[57] A. Newell and H.A. Simon, Computer Science as Empirical Inquiry: Symbols and Search, Communications of ACM 19, No. 3 (March 1976) 113–126.

[58] C.H. Papadimitriou and K. Steiglitz, Combinatorial Optimization: Algorithms and Complexity (Prentice-Hall, Englewood Cliffs, NJ, 1982).

[59] J. Pearl, Fusion, Propagation, and Structuring in Belief Networks, Artificial Intelligence 29 (1986) 241–288.

[60] W.E. Pracht, GISMO: A Visual Problem-Structuring and Knowledge-Organization Too, IEEE Trans. on Systems,

Man, and Cybernetics 16, No. 2 (Mar./Apr. 1986) 265–270.

[61] M. Quillian, Semantic Memory, in: M. Minsky, Ed., Semantic Information Processing (MIT Press, Cambridge, MA, 1968) 216–270.

[62] H. Raiffa, Decision Analysis (Addison-Wesley, Reading, MA, 1968).

[63] A. Rege and A.M. Agogino, Topological Framework for Representing and Solving Probabilistic Inference Problems in Expert Systems, IEEE Trans. on Systems, Man, and Cybernetics 18, No. 3 (May/June 1988) 402–414.

[64] R. Reiter, A Logic of Default Reasoning, Artificial Intelligence 13 (1980) 81–132.

[65] F. Rosenblatt, Principles of Neurodynamics (Spartan, New York, 1962).

[66] D.E. Rumelhart, G.E. Hinton and J.L. McClelland, A General Framework for Parallel Distributed Processing, in: D.E. Rumelhart, J.L. McClelland and PDP Research Group, Eds., Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Vol. I: Foundations (MIT Press, Cambridge, MA, 1986) 46–76.

[67] D.E. Rumelhart, G.E. Hinton, and R.J. Williams, Learning Internal Representation by Error Propagation, in: D.E. Rumelhart, J.L. McClelland and PDP Research Group, Eds., Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Vol. I: Foundations (MIT Press, Cambridge, MA, 1986) 318–362.

[68] D.E. Rumelhart, J.L. McClelland and PDP Research Group, Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Vol I: Foundations (MIT Press, Cambridge, MA, 1986).

[69] A.W.W. Schoennauer, Problem Finding and Problem Solving (Nelson-Hall, Chicago, IL, 1981).

[70] R.D. Schachter, Probabilistic Inference and Influence Diagrams, Operations Research 36, No. 4 (July/Aug. 1988) 589–604.

[71] G. Shafer, A Mathematical Theory of Evidence (Princeton University Press, Princeton, NJ, 1976).

[72] G. Shafer, Probability Judgment in Artificial Intelligence, in: L.N. Kanal and J.F. Lemmer, Eds., Uncertainty in Artificial Intelligence (North-Holland, New York, 1986) 127–136.

[73] E.H. Shortliffe, B. Buchanan and E.A. Feigenbaum, Knowledge Engineering for Medical Decision-Making: A Review of Computer-Based Clinical Decision Aids, Proceedings of IEEE 67, No. 9 (Sept. 1979) 1207–1224.

[74] H.A. Simon, New Science of Management Decision (Harper & Row, New York, 1960).

[75] H.A. Simon, Administrative Behavior, 3rd ed. (Macmillan, New York, 1974).

[76] M. Stefik, J. Balzer, J. Benoit, L. Birnbaum, F. Hayes-Roth and E. Sacerdoti, The Organization of Expert Systems: A Tutorial, Artificial Intelligence 18 (1982) 135-174.

[77] H.E. Stephanou and A.P. Sage, Perspectives on Imperfect Information Processing, IEEE Trans. on Systems, Man, and Cybernetics 17, No. 5 (Jan./Feb. 1987) 780–798.

[78] R.M. Tong and D.G. Shapiro, Experimental Investigation of Uncertainty in a Rule-Based System for Information

tion Retrieval, International Journal of Man-Machine Studies 22 (1985) 265–282.

[79] D.C. Tsichritzis and F.H. Lochovsky, Data Models (Prentice-Hall, Englewood Cliffs, NJ, 1982).

[80] A. Tversky and D. Kahneman, Judgment under Uncertainty: Heuristics and Biases, Science 185 (1974) 1124–1131.

[81] J.N. Warfield, Developing Subsystem Matrices in Structural Modeling, IEEE Trans. on Systems, Man, and Cybernetics 4, No. 1 (Jan./Feb. 1976) 74–81.

[82] B. Wise and M. Henrion, A Framework for Comparing Uncertain Inference Systems to Probability, in: L.N. Kanal and J.F. Lemmer, Eds., Uncertainty in Artificial Intelligence (North-Holland, New York) 69–84.

[83] L.A. Zadeh, Fuzzy Logic and Approximate Reasoning, Synthese 30 (1975) 407–428.

[84] L.A. Zadeh, The Role of Logic in Management of Uncertainty in Expert Systems, Fuzzy Sets and Systems 2, No. 2 (1983) 199–228.

[85] L.A. Zadeh, A Simple View of the Dempster-Shafer Theory of Evidence and its Implication for the Rule of Combination, Al Magazine 7, No. 2 (1986) 85–90.

[86] H.J. Zimmermann, Fuzzy Set Theory and its Applications (Kluwer-Nijhoff Publishing, Boston, MA, 1985).

[87] H.J. Zimmermann, Fuzzy Sets, Decision-Making, and Expert Systems (Kluwer-Nijhoff Publishing, Boston, MA, 1987).
