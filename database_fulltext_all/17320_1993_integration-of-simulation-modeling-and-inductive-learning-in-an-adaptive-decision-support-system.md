---
otero_id: 17320
otero_key: "W5AMHWRM"
title: "Integration of simulation modeling and inductive learning in an adaptive decision support system"
authors: "Selwyn Piramuthu; Narayan Raman; Michael J. Shaw; Sang Chan Park"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90027-z"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integration of simulation modeling and inductive learning in an adaptive decision support system

Selwyn Piramuthu, Narayan Raman and Michael J. Shaw

University of Illinois, Urbana, IL 61801, USA

Sang Chan Park

University of Wisconsin, Madison, WI, USA

This paper presents a decision support system (DSS) with inductive learning capability for model management. Simulation is used as the primary environment for modeling manufacturing systems and their processes. We propose an adaptive DSS framework for incorporating machine learning into the real time scheduling of a flexible manufacturing system and flexible flow system. The resulting DSS, referred to as pattern directed scheduling (PDS) system, has the unique characteristic of being an adaptive scheduler. While the bulk of previous research on dynamic machine scheduling deals with the relative effectiveness of a single scheduling rule, the approach presented in this study provides a mechanism for the state-dependent selection of one from among several rules. We address the PDS approach in the context of a model management system (MMS), with built-in simulation and inductive learning modules for heuristic acquisition and refinement. These modules complement each other in performing the decision support functions. Computational results show that such a pattern directed scheduling approach leads to superior system performance. It also provides a new framework for developing adaptive DSS.

Keywords: Adaptive decision support systems, Pattern-directed scheduling, Inductive learning, Model management

![](/api/attachments/W5AMHWRM/fulltext/images/8178e2b1ed53db518b4520078d39b2c371745b5626148e0f02b1dac85dcde7d0.jpg)

Selwyn Piramuthu is an Assistant Professor of Decision and Information Sciences at the University of Florida. He earned his Ph.D. in MIS at the University of Illinois at Urbana-Champaign in 1992. He holds a B.Tech. from the Indian Institute of Technology, Madras, India, and an M.S. from the University of Arizona. His research and teaching interests are in Machine Learning, AI, Human-Computer Interaction, Database Management, and Simulation.

Correspondence to: Michael J. Shaw, 2115 Beckman Institute, University of Illinois, Urbana, IL 61801, USA.

1. Introduction

1.1. Knowledge-based model management

Information as input is of vital importance during a decision making process. The primary source of information is raw data, which is processed for information by utilizing relevant mod-

![](/api/attachments/W5AMHWRM/fulltext/images/771eeb81c444f08b2b367e1111ce278f204ee172492e829c1d73be4ddf670542.jpg)

Narayan Raman is an Assistant Professor of Business Administration at the University of Illinois at Urbana-Champaign. He holds a B.Tech degree from the Indian Institute of Technology, a PGDM. from Indian Institute of Management and a PhD from the University of Michigan. Dr. Raman's research and publications are in the areas of operation scheduling, line balancing and flexible manufacturing systems. He is a member of ORSA, TIMS and POMS.

![](/api/attachments/W5AMHWRM/fulltext/images/9328680ca0b99ae5043c4df80e6883a66adc5f787852b7ce4d373efc1bd3855c.jpg)

Michael J. Shaw is an Associate Professor of Information Systems at the Department of Business Administration, University of Illinois at Urbana-Champaign. He has also been a research faculty member at the Beckman Institute for Advanced Science and Technology, a research center on the same campus for the study of intelligence, where he is currently coordinating the research program in decision support systems. His research interests include machine learning, intelligent manufacturing, distributed artificial intelligence, and knowledge-based decision support applications.

![](/api/attachments/W5AMHWRM/fulltext/images/41356bd0a427d1d88a485d98f62e7917e381993bd062e994342764560128e4fc.jpg)

Sang Chan Park is an Assistant Professor of Information Systems Design and Analysis, School of Business at the University of Wisconsin, Madison. He received his BBA (1984) from Seoul National University, Korea, and his MBA in MIS (1985) from the University of Minnesota, Minneapolis. His Ph.D. in MIS is from University of Illinois, Urbana-Champaign. His research interest includes the application of Machine Learning in Artificial Intelligence to the design of Knowl edge-Based DSS for such diversified areas as Option Investment, Flexible Manufacturing System Scheduling, Cellular Manufacturing Cell Formation, and Process Planning. He has published several articles in the areas of intelligent process planning and knowledge-based scheduling.

![](/api/attachments/W5AMHWRM/fulltext/images/5d1e3db0bc704a362c867c0ac920d0dac6a3ccb7a806a1daaca007b843a40e27.jpg)  
Fig. 1. DSS framework.

eling techniques. The modeling techniques thus take part implicitly in a decision making process by providing the decision maker with information which is derived from raw data. Models could be decomposed by organizational function, organizational level, model solution techniques, or a combination of these [5]. Both data and models are necessary resources which need to be managed efficiently for effective performance of the overall decision making process. The proliferation of modeling techniques necessitates a structured methodology to store, retrieve, and to utilize appropriate models along with data. A solution to this is to use model management systems (MMSs) to manipulate data and models.

We adapt and add additional capabilities to the MMS framework (fig. 1) as proposed in Bonczek, Holsapple, and Whinston (1983). Their DSS framework has 3 modules (components): (1) language system (LS);(2) knowledge system (KS); and (3) problem processing system (PPS). The LS module acts as an interface between the user and the PPS by including syntactic and semantic rules for determining legal problem statements. The PPS gathers input from users through the LS interface, and knowledge from the KS in transforming problem statements into appropriate executable plans of action. Both data and models belong to the KS, which is a representation system.

In this paper, we consider simulation as the primary modeling environment in the DSS. The simulation model is used to capture the characteristics of the system—a flexible manufacturing system (FMS)—in this study. The simulation model incorporates an array of parameters such as the number of machines, type of jobs, and utilization levels, among others, in simulating different scenarios in the FMS. An FMS is chosen as the example system because scheduling an FMS is known to be a hard problem, and because efficient optimum seeking solution methods are unlikely to exist for the same.

The DSS frameworks (e.g., [11]) that are being used currently are static in the sense that the decision making process is either a one-shot effort, or an iterative effort where no attempt is made to learn from past experience. We present a MMS framework that not only learns from its own experience, but also adaptively reacts to the needs of the environment. A learning and refinement module is added to the framework presented in [11], to enhance the MMS. The MMS discussed in this paper is also knowledge-based, with heuristic rules for selecting the dispatching rules as the domain knowledge. These heuristics are updated dynamically as the system evolves, as learning takes place, to be adaptive to varying environment. Problem-solving knowledge, in the form of heuristics, are accumulated and evaluated by a critic, and refined in the process through feedback.

The framework proposed also can be considered as an approach to incorporate deep reasoning into the DSS by having an embedded simulation model, instead of just using heuristics for shallow reasoning. Such a model not only provides a deep structure of the problem domain (i.e., the FMS environment), but it also provides a tool for testing different scenarios of the system, hence guiding the learning process. In the rest of this section, we briefly introduce the methodology of interest in this study using scheduling in an FMS as an example.

## 1.2 Pattern-directed scheduling as adaptive decision support

We consider an FMS environment to develop the proposed adaptive model management system. This study has two-fold research aims: It enhances the capabilities of a MMS by incorporating learning and adaptability, and also suggests a methodology for dynamically scheduling machines in a FMS.

FMSs have routing flexibility which enables them to adapt easily to changes in the operations that need to be done on consecutive jobs. FMSs also have buffer-size limitations which avoids build-up of incomplete jobs in the system. Most FMS studies that incorporate routing flexibility consider machine assignment at the system setup stage only, and could be considered to be static. During operation in real time, only one route is used. Such static schedules do not, however, consider the need for various scheduling decisions to be made in real time as production proceeds. As Buzacott [13] notes, permitting machine assignment capability in real time can improve overall system performance.

In this study, we permit both machine assignment and operations scheduling in real time, thus leading to real-time dynamic scheduling. Furthermore, in comparison to previous studies, we consider a wider range of system characteristics. The control variables used in this study are overall system utilization level, tightness and variability of due dates, relative machine workload balance, actual buffer size and the degree of routing flexibility.

More importantly, however, this research focuses on the application of model management techniques using a pattern directed heuristic scheduling process. The relative effectiveness of a given scheduling rule likely depends upon the system characteristics. In a dynamic system, these characteristics change over time. Therefore, it appears conceptually appealing to adopt an approach which employs appropriate and possibly different scheduling rules at various points in time. In order to do so, however, we need a mechanism which can distinguish different combinations of system characteristics, or patterns, from one another.

We propose a systematic methodology which provides a pattern directed scheduling (PDS) with machine learning capabilities in order to extract patterns from the dominant characteristics of a given scheduling environment. These patterns are subsequently incorporated into a set of heuristic rules which guide the selection of scheduling rules in real time. We employ the ID3 [28] algorithm to help PDS recognize patterns comprising of the manufacturing system and job characteristics. These patterns are then used to specify the conditions which trigger the use of a given scheduling rule. These hybrids, which are basically heuristics in the form of patterns as preconditions and the assignments of scheduling rules as the resulting actions, are then added to the PDS's knowledge base in the course of learning. The organization of the PDS is shown in fig. 2.

We also suggest an approach for applying the developed PDS framework for dynamic scheduling in a flexible flow system (FFS). The extension to flexible flow shop $[36]$ scheduling involves two sets of heuristics, which need to be controlled in turn by meta-level heuristic rules to maintain the integrity of the FFS system.

The advantages of the framework proposed in this study are: (1) a DSS with model management techniques incorporating learning abilities; (2) capability of the DSS to be adaptive to changes in the environment of interest; (3) incorporating learning through deep reasoning in a DSS; and (4) automated knowledge acquisition through inductive learning.

The rest of this paper is organized as follows. Machine learning as applicable to model management is briefly discussed in Section 2. Section 3 presents some basic concepts of inductive learning and discussion on how inductive learning can be applied to operation scheduling. In Section 4, we describe the application of PDS to the FMS.

![](/api/attachments/W5AMHWRM/fulltext/images/0e0786c4ceb8af1d5f4987f4c6959f83f991d57ee2b647773c8954af560632c5.jpg)  
Fig. 2. Framework for pattern-directed scheduling.

Dynamic scheduling in a flexible flow system is next discussed in Section 5. Section 6 deals with the advantages of integrating machine learning and simulation. In Section 7, we discuss the addition of a learning module to the traditional DSS, and how this aids in learning and knowledge refinement. We conclude in Section 8 with a summary discussion.

## 2. Review on machine learning and model management

The need for model management arises primarily due to the fact that there is no single model which can be applied for all the decision problems. This leads to a need to select model(s) from among many (most of which might be irrelevant) models that are deemed to be able to solve the decision problem at hand. Support tools which aid in modeling such techniques as simulation, linear programming, regression analysis, among others, can be used to form composite models in response to a given decision problem. This would involve dynamically selecting the appropriate models, along with necessary input, in order to solve the decision problem $[35]$ . Shaw et al. $[35]$ classify the two major issues which research on model management systems have been concerned with: model representation, and model manipulation. In this paper, however, we are primarily concerned with the issue of model refinement and the use of simulation models for domain knowledge. Therefore, the issue of interaction between multiple models is avoided and the only model considered is the simulation model.

Models are treated similar to data $[17]$ to enable models as well as data to be integrated in a single system. Some of the commonly used model representations include predicate calculus within production system $[8–10]$ , graphs $[22]$ , semantic networks $[16]$ , frames $[15]$ , and relational database theory $[7]$ .

In the traditional model management literature, problem solving knowledge is acquired from domain experts through interviewing. Machine learning can be used for knowledge acquisition to automate the process, as well as to integrate the knowledge acquisition process into the overall model management system. Machine learning can be used to incrementally learn modeling knowledge through experience. Knowledge is stored in the knowledge-base in the form of production rules that increases in number as learned knowledge increases. This should be checked periodically since some of the rules are bound to become obsolete or the marginal contribution of some of the rules could become negligible. There is a need to weed out the production rules which do not (or negligibly) contribute in the problem-solving process. The knowledge thus learned over time needs to be refined as per predefined criteria that are executed by a critic (fig. 3), resulting in a compact, and informative knowledge-base.

![](/api/attachments/W5AMHWRM/fulltext/images/aeca4b26b22e2df6772b54543b6d693edc1fdf90f65970ef9e2141b9920a0bb1.jpg)  
Fig. 3. Control flow in a learning-augmented MMS.

The control flow in a generic learning-augmented DSS, such as one proposed in this study, is given in fig. 3. The learning module is the focal point of control in this framework since it serves the purpose of utilizing previous experience for problem-solving in future. Information for the learning module are from the data-, knowledge-, and model-bases which are repositories of problem-solving data, knowledge in the form of heuristic rules, and models, respectively. The instance selector gets its input from the learning module and acts as an interface between the problem solver and the learning module. Performance results from the problem solver are passed on to the critic that utilizes information from the learning module to analyze the performance of the problem solver.

Figure 4 illustrates the mapping of the generic control given in fig. 3 onto the FMS scheduling problem. The data-base consists of data resulting from the FMS environment through simulation modeling. Heuristic rules for scheduling are stored in the knowledge-base, and the model-base consists of the simulator, the modeling environment. The heuristic rules generated by the inductive learner are used by the instance selector for generating training examples for PDS module.

In this study, simulation is used as a modeling tool for representing the world from the decision making perspective. Simulation provides the necessary mapping from models as input to performance as output. The performance of the models are then utilized to learn, and to adaptively modify the knowledge-base.

As in discrete-event simulation, a major disadvantage with this method, however, is that it does not eliminate the need for the decision maker to select the initial set of variables that are included in the model. The performance of the final model depends, to a large extent, on the input information as per the variables that are used in the system. In some cases, inductive learning can be used to signal a deficit in the variables that are used. This happens when, at a leaf node, values of all the variables are the same for more than one example, although they belong to different classes. This signals a deficit of variable(s) that need to be included in the model to distinguish between the classes of interest. As is the case with most of the DSSs, the proposed framework also supports what-if queries to aid in sensitivity analyses. Thus, in addition to the standard features of a model management system, the proposed methodology also is adaptive to its environment, and has the ability to learn from past experience.

![](/api/attachments/W5AMHWRM/fulltext/images/6dc80f5a3f0e26c8cefc164af39cffea97cddae7b313e81d8565001e2e20635f.jpg)  
Fig. 4. Control flow in a learning augmented MMS for FMS scheduling.

![](/api/attachments/W5AMHWRM/fulltext/images/fc9d6607db6402714611250de38f6da9819f9df9699131bd3db06193cd32b72e.jpg)  
Fig. 5. A DSS for production scheduling.

## 3. A DSS for production scheduling

## 3.1. A new framework for adaptive decision support

We develop a modified DSS framework as in [11] for adaptive model management with the ability to learn. The framework as in [11] for the FMS scheduling problem is given in fig. 5, and the modified framework with an additional LRS module is shown in figure 6. The four components that form the modified framework are: (1)

LS (language system); (2) PPS (problem processing system); (3) KS (knowledge system), and (4) LRS (learning and refining system). In the framework discussed in this paper, the LS, a representation system, consists of process and production plans, and acts as an interface between the user and the system. The PPS has extensive problem solving abilities as represented by sub-modules, the pattern-directed scheduler (PDS) and simulation unit, to be able to gather and manipulate information from LS and manipulate data from KS, and indirectly from LRS. These capabilities of PPS entail not just information collection and problem recognition, but also to adaptively apply appropriate heuristic rules as and when it is deemed necessary. Data collection is done through the simulation unit, which is the model management tool being used in this study. The PDS reacts to changing scenarios (problem recognition) when a heuristic rule is triggered as the system evolves. The change in various parameters in the system is transformed by the PPS and mapped onto corresponding rules.

![](/api/attachments/W5AMHWRM/fulltext/images/c5c026e0e188a07ed447fc37b2674f4ab505c76448aec7a6104fa82bee2a115a.jpg)  
Fig. 6. A learning-integrated DSS for pattern directed scheduling.

The KS acts as an intermediary between PPS and LRS by acting as a store-house for heuristics and scheduling rules, which are learned and updated by LRS, and used by PPS for dynamic scheduling. The LRS module has the ability to learn concepts in terms of heuristic rules for scheduling. Learning in the LRS module takes place in the learning unit sub-module, using the inductive learner. The rules thus learned are inspected periodically by the critic sub-module to detect any deficiencies that might be present in the knowledge-base. The critic sub-module helps in maintaining a good current set of heuristic rules as per pre-specified criteria. Thus the integrated framework incorporating inductive learning and simulation as the modeling tool learns through experimentation, and adaptively applies the learned heuristic rules as per the patterns in the system.

## 3.2 Adaptive production scheduling

Scheduling jobs in manufacturing systems has to take into consideration various events (e.g., machine breakdowns) that might occur in the system randomly. This creates an instability in the modeled system if appropriate heuristics are not used as and when such situations arise. The performance of the entire system is improved by dynamically using heuristics consistent with the pattern which is exhibited in the system. The adaptive scheduling based on current patterns in the system helps take advantage of various heuristics when they are at their best in terms of performance. In this section, we discuss one such system, which combines adaptive application of heuristics with learning. We give a brief discussion of inductive learning, and then present its application in the pattern directed scheduler (PDS).

Inductive learning can be defined as the process of inferring the description (that is, the concept) of a class from the description of individual objects of the class [33]. A concept is a symbolic description that is true when applied to a data case describing the class correctly, and false otherwise. The concept to be learned in FMS scheduling, for example, can be a correct description of manufacturing environments suitable for applying a given scheduling rule (a class).

A set of training examples are provided as input for learning the concept representing each class. A given training example consists of a vector of attribute values and the corresponding class. A concept learned can be described by a rule determined by inductive learning. If a new input data case satisfies the conditions of this rule, then it belongs to the corresponding class. For example, a rule defining a concept can be the following.

$$
\text { Rule } _ {i}: \text { if } (b _ {i 1} \geqslant a _ {i 1} \geqslant c _ {i 1}) \text { and } \dots \text { and }
$$

$$
\left(b _ {i m} \geqslant a _ {i m} \geqslant c _ {i m}\right) t h e n \tau ,
$$

where $a_{ij}$ represents the jth attribute in Rule $_{i}$ , and $b_{ij}$ and $c_{ij}$ define the range for $a_{ij}$ .

In the FMS scheduling problem described in this paper, $Rule_{i}$ is treated as a selection heuristic with a conjunction of attribute conditions collectively defining the pattern, and $\tau$ represents the best scheduling rule for that pattern.

An instance that satisfies the definition of a given concept is called a positive example of that concept; whereas an instance that does not do so is a negative example of that concept. In the dynamic scheduling problem, since there are several scheduling rules which can potentially be selected, multiple concepts need to be learned. In this situation, the training examples supporting the use of a scheduling rule are treated as positive examples of that rule, whereas training examples supporting all the other scheduling rules are treated as negative examples.

A generalization of an example is a concept definition which describes a set containing that example. For a set of training examples, the generalization process identifies the common features of these examples and formulates a concept definition describing these features. Thus, inductive learning can be viewed as the process of repetitively generalizing the descriptions observed from examples until the inductive concept definition is found. Such a concept definition must be consistent with all the examples generated.

The input to an inductive learning algorithm consists of three parts: (1) a set of positive and negative examples; (2) a set of generalization and other transformation rules, and (3) criteria for a successful inference. Each training example consists of two components: A data case consisting of set of attributes, each with an assigned value, and the classification decision made by a domain expert according to the given data case. The output generated by this inductive learning algorithm is a set of decision rules consisting of inductive concept definition for each of the asses. Learning programs falling into this category include AQ15 [20], PLS [29], and ID3 [28]. These programs are sometimes referred to as similarity-based" methods, as opposed to "explanation-based" methods [23].

In this section, we give an overview of the proposed methodology for incorporating inductive learning into the dynamic scheduling process. The details of this procedure follow in Section 3. Our approach integrates simulation, inductive learning and pattern directed scheduling. It consists of the following three steps: (1) generating training examples; (2) learning rules from examples; and (3) executing pattern directed scheduling. Detailed descriptions of these steps are in order.

## 3. Generating training examples

The major objective of generating training examples is to provide the correct characterization of the manufacturing environments suitable for various scheduling rules. We use simulation experiments to generate a variety of such environments. The relevant design issues which need to be addressed are:

(1) Criteria for performance evaluation. These could be stated as scheduling objectives such as minimizing mean tardiness, minimizing mean flow me, etc;

(2) Set of scheduling rules to be considered. In order for the learning process to be comprehensive, we need to identify all scheduling rules which can potentially be appropriate for the scheduling objective studied;

(3) Specification of control attributes. We need to determine the control attributes which are likely to be dominant for the purpose of describing a pattern, and which can, therefore, affect the election of a given scheduling rule. These control attributes include both system and job characteristics. Examples of control attributes are the physical aspects of the manufacturing system (such as the number of machines, buffer sizes, etc) the material flow pattern, overall system utilization level, relative machine workloads, job due date tightness, etc. In an FMS, it may also be important to consider contention factor $[26,31]$ which refers to the average number of machines available for processing an operation, and therefore is a measure of the routing flexibility.

(4) Measurement of control attributes. There are several possible ways in which the control attributes discussed above can be measured in training examples for providing descriptions of the scheduling environment at various points in time. If the decision (the selection of a given scheduling rule) is based upon the cumulative average measure (that is, from time zero to the current time $T_{now}$ ), training examples must be expressed in terms of cumulative average values. However, if the decision is made on the basis of the anticipated values (projection at time k through time $k + \delta$ ), training examples must do likewise. The cumulative average converges to the experimental design parameters, hence, its value is stable in the steady state. On the other hand, anticipated values show wide fluctuations and greater “lumpiness”.

Training examples are generated by simulating the system performance for the desired scheduling objective under a variety of patterns. For a given pattern, the simulation runs are replicated for each scheduling rule considered. The one rule which results in the best performance yields the positive example for that pattern. In this manner, we are able to establish a one to one correspondence between a manufacturing pattern and the scheduling rule appropriate for that pattern.

## 3.4. Learning rules from examples

The inductive learning mechanism is used to establish formally the correspondence between the manufacturing patterns and the best scheduling rule for each pattern, as observed from the training examples. Using an automated inductive learner has several advantages: (1) qualitative information with nominal values can be analyzed together with quantitative information; (2) hypotheses can be conditionally accepted; (3) the dominant aspects of design alternatives are systematically detected which can be used iteratively for redesigning the experiment; and (4) new concepts or knowledge in the form of heuristics can be created. This enables the computer to be a knowledge generator instead of being merely an information collector.

Moreover, the simulation mechanism complements the inductive learner during the process of heuristic modification. Inductive learning mechanisms, used in the literature, passively analyze given training example(s); they cannot control these training examples by themselves. Similarly, simulation has been used primarily for evaluation rather than for learning. By incorporating the simulation mechanism with the learning process in our methodology, the inductive learner can determine the number and the nature of training examples studied since it actively controls the generation of future training examples which are critically important for further performance of the system. Because of this feedback, the inductive learner is transformed from being purely data-driven to being model-driven. Therefore, not only is the burden of collecting off-line training examples greatly alleviated, but the time required to collect examples is shortened. More importantly, this approach automates the acquisition of knowledge for the manufacturing knowledge base. This integration of inductive learning and simulation provides an appealing framework for automated manufacturing decision support which learns through experimentation.

## 3.5. Executing pattern directed scheduling

Pattern directed scheduling employs the learned heuristics for scheduling in real time $[31,32]$ . Whenever a scheduling decision is to be made, the pattern of the current state is observed. Once the pattern is recognized, it is compared with the preconditions of the developed heuristics. The matching heuristic is initiated and its resulting action (the appropriate scheduling rule) is used for assigning priorities to the waiting jobs.

PDS employs a filtering mechanism to prevent overreaction to changes in the scheduling environment. This mechanism maintains a cumulative score of the number of times a given scheduling rule is favored by the current pattern. A switch to this rule occurs only when this score exceeds a pre-specified threshold. In the following section, we discuss the various filtering mechanisms and their impact on the performance of PDS. (For further details, the reader is referred to [34]).

## 4. Dynamic FMS scheduling

An example of FMS scheduling, using the PDS framework discussed in the previous section, is discussed in this section. FMS environment, with its ever changing scenarios, is an excellent domain for the application of adaptive model management techniques. Since the jobs coming into the system have disparate routings, there is a definite need to apply appropriate scheduling heuristics as per the current status of the system. In this section, we discuss a model management system (MMS), specifically the application of PDS, in a FMS environment.

## 4.1 Problem specification

\- Scheduling criterion. The scheduling objectives considered in this study are minimizing mean flow time and mean tardiness. These objectives were selected primarily because they have been studied extensively, and various scheduling rules have been found to perform well under different scheduling environments. This provides a strong benchmark for testing the effectiveness of the pattern directed scheduling approach.

\- Set of scheduling rules considered. The scheduling rules used for the purpose of generating the PDS for the minimum tardiness objective are: (1) earliest due date (EDD) rule; (2) shortest imminent processing time (SIPT) rule; (3) modified job due date (MDD) rule; (4) modified operation due date (MOD) rule; and (5) critical ratio (CR) rule. For the minimum flow time criterion, we used SIPT, least work remaining (LWKR), and the anticipated work in next queue (AWINQ) rules. These scheduling rules rank the various jobs competing for the use of a given machine at any point in time according to different priority schemes. They compute priority indexes for individual jobs; the job with the smallest index value is selected first. The priority index corresponding to each rule is given as follows:

$$
\begin{array}{l l} \text {EDD} & d _ {j}, \\ \text {SIPT} & p _ {i j}, \\ \text {MDD} & \max \{t + P _ {i j}, d _ {j} \}, \\ \text {MOD} & \max \{t + p _ {i j}, d _ {i j} \}, \\ \text {CR} & (d _ {j} - t) / P _ {i j}, \\ \text {LWKR} & P _ {i j}, \end{array}
$$

where $d_{j}$ is the due date of job j, $p_{ij}$ and $d_{ij}$ are, respectively, the processing time and due date of operation i in job j; $P_{ij}$ is the processing time remaining in job j at the start of operation i, and t is the time at which the scheduling decision is to be made. The AWINQ rule favors a job which is processed next on the machine which has a queue with the least anticipated work waiting. These rules have been found to be effective for the objective of minimizing mean tardiness or mean flow-time in the past (see, for example, [2]).

\- Control attributes considered. We addressed an FMS which permitted random, job shop-like flow of parts through the system. For generating training examples, eight control attributes were considered: (1) number of machines; (2) buffer size; (3) machine homogeneity;(4) relative machine workload; (5) blocking status; (6) contention factor; (7) flow allowance factor; and (8) overall system utilization. Machine homogeneity refers to the similarity among machines. It is expressed as the ratio of the standard deviation of the number of operations that each machine can process to the average number of operations that a machine can process. Relative machine workload is expressed as the ratio of the standard deviation of the machine utilizations to the average machine utilization. Blocking status is a logical yes-no variable which indicates whether any machine in the system is being blocked at a given point in time. Flow allowance factor controls the tightness of job due dates. We used the following expression to determine job due dates:

$$
d _ {j} = a _ {j} + F \cdot p _ {j},
$$

where $a_{j}$ and $p_{j}$ denote, respectively, the arrival time and processing time of job j, and F is the flow allowance factor. In the simulation study testing PDS, in the learning phase, 26 different scenarios with varying combinations of attribute values were simulated to generate 130 training examples. From among these examples, the instances in which a given scheduling rule performed the best were selected as positive examples for generating the heuristic.

## 4.2. Rule induction

Based on the training examples, an inductive learning program, ID3 [28], was employed to describe the patterns for selecting each scheduling rule. The rule induction process carried out by ID3 results in the decision tree which was subsequently translated into a set of pattern directed heuristics for controlling the pattern directed scheduler.

The decision tree generated highlights the relative importance of the various attributes in characterizing the manufacturing environment; that is, it helps determine the set of most relevant attributes that comprise the patterns of the rules. Moreover, ID3 selects the attributes to be included in the rules in such a fashion that the earlier an attribute is selected, the more important that attribute is in describing the patterns of the rule. An example of a typical decision tree generated for the minimizing mean flowtime criterion, and the heuristic rules derived from this decision tree are given in fig. 7 and table 1. Based on the learning results shown, the attributes that need to be considered for selecting scheduling rules can be ordered by their relative importance as follows: (1) NSDRL; (2) CFACT; and (3) TBF.

The decision tree thus derived is very informative. In fig. 7, NSDRL, which is the standard deviation of relative loading measuring the degree of balance of the system, is closer to 1 if the system is balanced, is chosen as the most important attribute based on its information content used to distinguish between the different dispatching heuristics. SIPT, which is a myopic heuristic, consistently appears on the balanced side of the tree confirming the fact that SIPT performs well when the system is balanced than otherwise. Similarly, AWINQ, which is a global heuristic since it takes into account work in the next queue also, performs better when the system is relatively unbalanced.

![](/api/attachments/W5AMHWRM/fulltext/images/97ce99d93d4c3805993155b43ae5440384f3b23e3e7a9c415fbee99363dcfa49.jpg)  
Fig. 7. Decision tree under min mean flowtime objective.

<table><tr><td>Table 1Heuristic rules derived from fig. 7.</td></tr><tr><td>if (NSDRL &lt; 1.2) &amp; (CFACT &lt; 4) &amp; (CFACT &lt; 3) then SIPT</td></tr><tr><td>if (NSDRL &lt; 1.2) &amp; (CFACT &lt; 4) &amp; (CFACT ≥ 3) &amp; (TBF &lt; 14) then SIPT</td></tr><tr><td>if (NSDRL &lt; 1.2) &amp; (CFACT &lt; 4) &amp; (CFACT ≥ 3) &amp; (TBF ≥ 14) then LWKR</td></tr><tr><td>if (NSDRL &lt; 1.2) &amp; (CFACT ≥ 4) then LWKR</td></tr><tr><td>if (NSDRL ≥ 1.2) &amp; (NSDRL &lt; 1.4) then AWINQ</td></tr><tr><td>if (NSDRL ≥ 1.2) &amp; (NSDRL ≥ 1.4) &amp; (TBF &lt; 178) then LWKR</td></tr><tr><td>if (NSDRL ≥ 1.2) &amp; (NSDRL ≥ 1.4) &amp; (TBF ≥ 178) then AW-ING</td></tr></table>

## 4.3. Pattern directed scheduling

Rules similar to those in fig. 7 provide the basis for pattern directed scheduling. The left-hand-side of each rule represents the pattern for applying the scheduling rule at the right-hand-side. Thus, different scheduling rules will be selected when the manufacturing system manifests different patterns. As a result, rule selection decision can also be changed dynamically as the pattern of the system changes over time. Conceptually, this technique should be more effective than the use of a single rule throughout the process, as has been the case in most of the previous research on dynamic scheduling. We use simulation studies to provide experimental evidence in support of this conjecture for the minimum tardiness objective.

In applying PDS, the issue of how reactive the scheduling system is to pattern changes turns out to be significant. Specifically, the performance of PDS deteriorates when different rules are applied immediately upon a pattern change. This problem can be attributed to excessive system nervousness and over-reaction to patterns that are only transient. In order to mitigate this tendency, we used a threshold factor which smooths the response of PDS to pattern changes. Under this approach, we keep a cumulative score of the number of times each rule is favored. Suppose that the rule being used currently is $i^{*}$ with a cumulative score of $S_{i^{*}}$ . If a pattern change now favors the selection of rule j, $j \neq i^{*}$ , then j will be selected if and only if $S_{j} > R \cdot S_{i^{*}}$ . R is a smoothing constant which is treated as a variable. The appropriate value of R for a given pattern is determined through additional induction.

The performance of PDS depends upon: (1) the frequency of actual pattern changes that are realized in the system; (2) system size; (3) contention factor; (4) mean tardiness values; and (5) performance differences of the various dispatching rules used.

If the number of potential switches in the applicable dispatching rule is high, the frequency of actual pattern changes are regulated by the R values. The improvement ratio (between PDS and the best heuristic) decreases with an increase in the number of pattern changes $[34]$ . On the other extreme, only a few pattern switches would imply that there are a few dominant patterns that characterize the system. Hence, PDS is most effective when the number of pattern changes is from medium to reasonably high and no pattern is clearly dominant.

The differential between utilization of machines would tend to be lesser when there are more machines than are needed for jobs to be processed, and PDS would behave identically to the best dispatching rule, in the limit, as the contention factor is increased. An increase in the system size, as measured by the number of machines, generally leads to an increase in contention factor as well.

As in [2], when the mean tardiness values are small, the relative difference in the performance of PDS and best dispatching rule decreases. Under the conditions found in an FMS environment, if all the dispatching rules that are being used for PDS have similar performance, the difference between PDS and the best heuristic diminishes since, ideally, PDS can perform only as well as the best rule in a given situation.

In general, because the set of training examples is a subset of the universe of the possible scheduling environments, the learned heuristics are likely to be overgeneralized. Therefore, some prediction errors cannot be avoided. Specifically, in a situation which is not described in the set of training examples, PDS may not perform very well. However, we found that in such situations, the difference between the performance of PDS and the best rule was marginal.

Loss of information due to data compression may be another explanation for the PDS behavior. Heuristics are condensed form of data cases (or training examples). Thus, bias from either representation or learning algorithm may degrade the quality of heuristics, which, in turn, affects the PDS performance. Nonetheless, we can assert that PDS benefits from real time execution as the set of training examples becomes richer and more comprehensive because the inductive learning process employs a feedback mechanism to update the learned heuristics. Therefore, in a real system, the relative performance of the pattern directed scheduling approach should improve continually.

## 5. Dynamic flexible flow system (FFS) scheduling

Flexible flow systems have become an increasingly important manufacturing technology $[1,4,37]$ . The PDS approach proposed in this paper can be extended to scheduling a flexible flow line, an example of which would be a production process utilizing surface mount technology (SMT) for making printed circuit boards (PCBs). The types of scheduling decisions that need to be taken into account while studying the dynamics of a flexible flow system include dispatching at machines and part release. Dispatching at machines would be similar to those used for FMS scheduling, except that it would be at a local (machine) level. Part release would have to be implemented similar to dispatching, but with appropriate additional variables and constraints involving these variables.

In the course of developing the PDS system, insights into the structure and behavior of flexible flow lines, in the context of PCB fabrication, would be obtained. This is particularly true during system design. Increased understanding would be gained through abstraction of essential features in the design process to aid in the decisions involved in the system. We briefly discuss the problem specifications that should be taken into consideration while considering a flexible flow system.

## 5.1 Scheduling criteria

Because capital costs are high and variable processing costs are relatively low, high utilization of SMT equipment is a generally accepted goal in the semiconductor industry. The objective of the flexible flow system in this context would be to maximize throughput (or minimize makespan), and minimize work-in-progress (WIP).

## 5.2. Set of scheduling rules

Two different sets of scheduling rules need to be used for FFS scheduling—one for part release, and the other for dispatching. For dispatching, rules such as SIPT can be used similar to those used in FMS scheduling. Rules for part release could include selecting the part that minimizes $\max_{j}\{|x_{j}(t)|\}$ , where $x_{j}(t)$ is the difference between the total number of parts of type j produced until time t and the total number of parts required, selecting the part that minimizes machine load imbalance, or based on anticipated work in next queue (AWINQ).

Whereas scheduling rules for part release are based on a global (system) level, the rules for machine dispatching operate at a local (machine) level. Since both sets of rules pertain to the same system, and operate on overlapping objectives, they need to be controlled by meta-level heuristics similar to the hierarchical approach to production scheduling as in [1].

## 5.3. Control attributes

The control attributes for part release and machine dispatching, although mostly the same, differ in that it is at a global level for the former and at a local level for the latter. The control attributes for part release could include total WIP, relative workloads, overall system utilization, contention factor, among others, and those for machine dispatching could include local buffer space, machine utilization, and relative machine load. These attributes that are used for FFS, although the same as those used for FMS scheduling, differ in that both a global average involving all the machines and local values involving those of specific machines are used for FFS.

## 6. Integrating inductive learning and simulation

Both inductive learning and simulation, when integrated, are complementary to each other in learning by experimentation. As per the training examples generated using simulation, inductive learning is used to generate the heuristic rules which are then adaptively applied in the PDS environment. The learning module requires a source (simulation module) for training examples which exemplifies the system under consideration, and the simulation module requires a source (inductive learning module) for learning heuristics. Thus there is a feed-back between the inductive learning and simulation modules which happens to enhance the performance characteristics of both the modules by knowledge refining thus increasing the performance of the PDS.

The contents of the training examples, which are the sole input to the inductive learning module, are of prime importance. Since in discrete-event simulation, only the average of the attribute values over time are taken into consideration, variation in the training examples to a certain degree is unavoidable. The rules that are developed using the inductive learning module thus needs to be filtered to reduce any noise that might be present due to averaging.

Rule-refinement is an additional phase of learning to be used along with PDS. During this phase, performance results from the pattern-directed scheduling phase are collected, and performance of the rules are evaluated using a critic program. If a heuristic rule is proved to be causing undesirable scheduling performance, the rule-refinement module would either delete the specific rule or generate additional training examples in order to refine the rule(s). Bundy and Silver [12], Politakis and Weiss [27], and Wilkins [38] describe methods for rule refinement. The basic rule-refinement program involves iterating through the following steps: (1) obtain performance of rules; (2) analyze the ill-performing rules; and (3) revise or delete the rules. Meta-rules are used to suggest further experiments with training examples. The if part of the meta-rule contains conjunction of predicate clauses on features about ill-performing rules and the training examples resulting in these rules; the then part suggests further experiments with modified attributes for generating additional training examples and refining the rules.

As the patterns in the system varies over time, the integration of inductive learning and simulation helps in adaptively utilizing different dispatching heuristics in real-time. Unlike in static systems where extensive calculations are required whenever there is an unexpected disturbance in the system such as machine breakdowns, and large deviations in processing times, the PDS system incorporating both simulation and inductive learning adapts itself instantaneously. This is rendered possible through learning the different possible patterns that can arise in the system and their corresponding dispatching heuristics. Thus the decision support system incorporating simulation is used as a learning tool in addition to being used as an evaluating tool.

## 7. Adaptation by learning and knowledge refinement

An intelligent system needs to be adaptive to its current environment for it to perform effectively even as the environment evolves. By adapting to its current environment, the system can react to the problem solving situation by utilizing appropriate models and strategies, rather than models that are out-dated or otherwise inappropriate to the current situation.

Machine learning is used in this study as a means by which the system adapts itself to the environment. Machine learning is used to continually update and refine the knowledge-base. The critic module screens new knowledge, as and when they are formed, as to their adherence to the pre-defined criteria for being included in the knowledge-base. These updates are done incrementally through experimentation with various scenarios that are present in the MMS environment.

The primary purpose of knowledge-base refinement is to discover, test, and incorporate modifications to the rules in the knowledge-base, with a view towards improving the empirical adequacy of the knowledge-base [18]. Detecting deficiencies in the knowledge-base is a prerequisite to refining the same. Wilkins [38] lists six of the common performance standards that are used by machine learning programs to detect deficiencies. They are: (1) problem solution (e.g., SEEK2 [19]); (2) problem solution steps (e.g., ARMS [30] taken to arrive at a correct solution; (3) environmental feedback (e.g., HACKER) (4) oracle (e.g., LEAP [24]); (5) efficiency, by having an internal standard of performance (e.g., LEX [25]); and (6) correctness (e.g., AM [21]).

Once deficiencies are detected, the knowledge-base of interest needs to be refined. Blanning [6] considers knowledge-based refinement in terms of optimization in knowledge-base space. The knowledge base is refined in the direction which optimizes the contents of the same. The goal of this search is to maximize the objective function which measures the knowledge-base performance over the example space. In an ideal situation, a convergence criterion could be such that the refined knowledge-base will never have to be changed, which could be attained only after necessary examples which cover the space of the decision process sufficiently are used during the learning phase of the model management system. This would imply that no future scenarios would be misdiagnosed, assuming that the environment of interest remains constant without any new ramifications in the attribute space or the values the attributes can assume. This continual refinement can be executed until stopping criteria are reached. The stopping criteria could be based on the performance standards as mentioned above [38], or could be based on the size of the individual rules in the knowledge-base.

![](/api/attachments/W5AMHWRM/fulltext/images/2a1edff92f50fa9343bc57e48e6205a57a19f01be8d4541520c835426f63f84a.jpg)  
Fig. 8. Learning-augmented DSS framework.

In concluding, we have developed a modified DSS framework as in Bonczek, Holsapple, and Whinston for adaptive model management with the ability to learn (fig. 8).

In addition to LS, PPS, and KS, an additional module, learning and refining system (LRS) has been added to the framework. The LRS module interacts with the knowledge system (KS), which could consist of data, knowledge, and model bases. The knowledge learned and refined incrementally by the LRS are stored in the KS for further processing by PPS. The LRS module thus adds incremental learning facility to the proposed adaptive DSS framework.

## 8. Concluding remarks

We have developed a modified model management system framework with learning capabilities using inductive learning, an artificial intelligence methodology, for decision support. The MMS learns from past experience through experimentation in the domain of interest. The learning process also endows the system with automated knowledge acquisition capability, thus avoiding the hard task of manually acquiring problem-related knowledge. Knowledge thus acquired is also refined through feed-back from a critic module utilizing pre-specified performance criteria.

This paper has established the following results which we think are significant from a model management perspective: (1) It is desirable to apply appropriate models adaptively as per the needs of the problem-solving system; (2) the heuristics for selecting models can be generated by the inductive learning process; (3) learning through experimentation leads to an effective management of data, knowledge, and model resources; (4) deep reasoning can be incorporated into the DSS for structured analyses; and (5) a new methodology for improving the performance of the system by integrating simulation and inductive learning, resulting in an adaptive model management system which learns and evolves over time through experimentation.

We used the problem of scheduling in a FMS to illustrate the proposed framework. The side-effect due to this framework resulted in the PDS approach for intelligent scheduling. By utilizing the PDS approach, scheduling in an FMS and an FFS environment could be done adaptively as per the dynamics of the system.

## References

[1] R. Akella, Y. Choong and S.B. Gershwin, Performance of Hierarchical Production Scheduling Policy, IEEE Transactions on Components, Hybrids, and Manufacturing Technology vol. CHMT-7, no. 3, pp. 225–240 (Sep. 1984).

[2] K.R. Baker, Sequencing Rules and Due-Date Assignments in a Job Shop, Management Science 30, No. 9, pp. 1093–1104 (Sep. 1984).

[3] K.R. Baker, Introduction to Sequencing and Scheduling (Wiley, New York, 1974).

[4] M.O. Ball and M.J. Magazine, Sequencing of Insertions in Printed Circuit Board Assembly, Operations Research 36, pp. 192–201 (1988).

[5] R.W. Blanning, Issues in the Design of Expert Systems for Management, Proceedings of the 1984 National Computer Conference (1984a).

[6] R.W. Blanning, Expert Systems for Management: Possible Application Areas, DSS-84 Transactions, W. Zmud (ed.), pp. 69–77 (1984b).

[7] R.W. Blanning, A Relational Framework for Join Implementation in Model Management Systems, Decision Support Systems 1, pp. 69–82 (1985).

[8] R.H. Bonczek. C.W. Holsapple and A.B. Whinston, Future Directions for Developing Decision Support Systems, Decision Science 11, pp. 616–631 (1980).

[9] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems (Academic Press 1981a).

[10] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management, Operations Research 29, 2 (March–April 1981b).

[11] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Specification of Modeling Knowledge in Decision Support Systems, in H.G. Sol (ed.), Processes and Tools for Decision Support, pp. 65–78 (North-Holland 1983).

[12] A. Bundy and B. Silver, A Critical Survey of Rule Learning Programs, in Proceedings of the European Conference on Artificial Intelligence, Orsay, France (1982).

[13] J. Buzacott, Optimal Operating Rules for Automated Manufacturing Systems, IEEE Transactions on Automatic Control AC-27, 80–86 (1982).

[14] R.W. Conway, W.L. Maxwell and L.W. Miller, Theory of Scheduling (Addison-Wesley, Reading MA, 1967).

[15] D.R. Dolk and B. Konsynski, Knowledge representation for Model Management Systems, IEEE Transactions on Software Engineering 10, 6, pp. 619–628 (November 1984).

[16] J.J. Elam, J.C. Henderson and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proceedings of the First Conference on Information Systems (1980).

[17] A.M. Geoffrion, An Introduction to Structured Modeling, Management Science, 33, 5, pp. 547–588 (1987).

[18] A. Ginsberg, Automatic Refinement of Expert System Knowledge Bases (Pitman, London 1988).

[19] A. Ginsberg, S. Weiss and P. Politakis, SEEK2: A Generalized Approach to Automatic Knowledge base Refinement, Proceedings of the 1985 IJCAI, pp. 367–374 (1985).

[20] J. Hong, I. Mozetic and R.S. Michalski, AQ15: Incremental Learning of Attribute-Based Descriptions from Examples, Technical Report No. UIUCDCS-F-86-1949, Dept. of Computer Science, University of Illinois at Urbana-Champaign (July 1986).

[21] D.B. Lenat, AM: An Artificial Intelligence Approach to Discovery in Mathematics as Heuristic Search, PhD Thesis, Stanford University (1976).

[22] T.P. Liang, Development of a Knowledge-Based Model Management System, Operations Research 36, 6, November–December, pp. 849–863 (1988).

[23] T.M. Mitchell, R.M. Keller and S.T. Kedar–Cabelli, Explanation Based Learning: A Unifying View, Machine Learning 1, pp. 47–80 (1986).

[24] T.M. Mitchell, S. Mahadevan and L.I. Steinberg, LEAP: A Learning Apprentice for VLSI design, Proceedings of the 1985 IJCAI, pp. 573–580 (1985).

[25] T.M. Mitchell, P.E. Utgoff and R.S. Banerji, Learning by Experimentation: Acquiring and Refining Problem-Solving Heuristics, in R.S. Michalski, J.G. Carbonell and T.M. Mitchell (eds.), Machine Learning: An Artificial Intelligence Approach, pp. 163–190 (Tioga. Palo Alto, 1983).

[26] S. Park, N. Raman and M.J. Shaw, Heuristic Learning in Pattern-Directed Scheduling, in Proceedings of the Third ORSA/TIMS Conference on Flexible Manufacturing Systems (Elsevier Science Publishers, Amsterdam, The Netherlands, 1989).

[27] P. Politakis and S.M. Weiss, Using Empirical Analysis to Refine Expert System Knowledge Bases, Artificial Intelligence 22, pp. 23–48 (1984).

[28] J.R. Quinlan, Induction of decision Trees, Machine Learning 1, pp. 81–106 (1986).

[29] L. Rendell, Induction, of and by Probability, in Kanal and Lemmar (Eds), Uncertainty in AI, pp. 429–443 (North Holland 1986).

[30] A.M. Segre, Explanation-Based Learning of Generalized Robot Assembly Plans, PhD Thesis, University of Illinois at Urbana-Champaign (1979).

[31] M.J. Shaw, Knowledge-Based Scheduling in Flexible Manufacturing Systems: An Integration of Pattern-Directed Inference and Heuristic Search, International Journal of Production Research 15, No. 5, pp. 353–376 (1988).

[32] M.J. Shaw, A Pattern-Directed Approach to Flexible Manufacturing: A Framework for Intelligent Scheduling, Learning, and Control, International Journal of Flexible Manufacturing Systems 2, pp. 121–144 (1989).

[33] Shaw, M.J., Applying Inductive Learning to Enhance Knowledge-Based Expert Systems, Decision Support Systems 3, pp. 319–332 (1987).

[34] M.J. Shaw, S.C. Park and N. Raman, Intelligent Scheduling with Machine Learning Capabilities: The Induction of Scheduling Knowledge, IIE Transactions (1992).

[35] M.J. Shaw, P-L. Tu and P. De, Applying Machine Learning to Model Management in Decision Support Systems, Decision Support Systems 4, pp. 285–305 (1988).

[36] R.J. Wittrock, Scheduling Algorithms for Flexible Flow Lines, IBM Journal of Research and Development 29, No. 4, pp. 401–412 (July 1985).

[37] R.J. Wittrock, An Adaptive Scheduling Algorithm for

Flexible Flow Lines, Operations Research 36, No. 3, pp. 445–453 (1988).

[38] D.C. Wilkins, Apprenticeship Learning Techniques for Knowledge Based Systems, Report No. STAN-CS-88-1242, Department of Computer Science, Stanford University, Stanford, CA (December 1988).
