---
otero_id: 17007
otero_key: "38KCC29A"
title: "Applying machine learning to model management in decision support systems"
authors: "Michael J. Shaw; Pei-Lei Tu; Prabuddha De"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90017-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applying Machine Learning to Model Management in Decision Support Systems \*

Michael J. SHAW, Pei-Lei TU

Decision and Information Sciences Group, Department of Business Administration, University of Illinois at Champaign-Urbana, IL 61820, USA

Prabuddha DE

Department of Decision Sciences, University of Dayton, OH 45469, USA

Model management systems have become increasingly important in handling complicated decision problems in decision support systems (DSS). Aiming at overcoming the weaknesses of currently used model management systems, we present a new framework of model management system which is capable of performing model manipulation more effectively. The new approach incorporates machine learning to acquire model manipulation knowledge, stored in the form of schemata, and to refine these acquired schemata. In addition, we also address two issues that have so far been overlooked in the DSS literature: (1) to refine existing model representations as more experiences are accumulated and (2) to create model selection heuristics adaptive to the DSS environment.

Keywords: Model Management, Machine Learning, Intelligent Decision Support.

\* The first author gratefully acknowledges the grants from the Office for Information Management, the Herbert V. Prochnow Foundation and the Research Board of the University of Illinois for supporting this research.

![](/api/attachments/38KCC29A/fulltext/images/69caf28a43a6a5bb63c1dfc03d218de98ad5edbaaefa04d0fe566f175e0f9b79.jpg)

Michael J. Shaw is an Assistant Professor of Business Administration at the University of Illinois, Urbana-Champaign. His PhD in Information Systems is from Purdue University. His current research interests are concerned with the applications of artificial intelligence to designing decision support and manufacturing information systems. He has published in the areas of information systems, machine learning, distributed AI, and intelligent manufacturing. A winner of Texas

Instruments AAAI-87 and AAAI-88 paper competitions on advanced AI applications, Dr Shaw is also a recipient of the Amoco Foundation Professorship (1985–88) and is currently a Lilly Foundation Fellow.

## 1. Introduction

Recently model management has become an important aspect in decision support systems. Individual models performing stand-alone computation (e.g., time-series, simulation, regression analysis, etc.) often need to be combined with one another to generate a composite model in response to a given decision problem. The construction of such a composite model involves dynamically selecting the necessary constituent models, imposing an appropriate sequence, and determining the correspondence of each model to different decision problems. These tasks are known as model manipulation. Model manipulation is typically the most difficult task that a model management system faces, in addition to its other tasks such as maintaining a large model bank and interacting with databases and system users.

![](/api/attachments/38KCC29A/fulltext/images/8aa3ad95d330bc3d286fd0bb666f97423dc4896bc050ac8c7028a75607636c7d.jpg)

Pei-Lei Tu is a graduate student in the Department of Business Administration, University of Illinois at Urbana-Champaign. She received a B.A. in Accountancy from National Taiwan University, Taiwan. She worked as a graduate assistant in this project.

![](/api/attachments/38KCC29A/fulltext/images/07971b126897e7e75bc7ec6e8d231e3b186e3cabf68ac62f1dc3a40448c2b3f0.jpg)

Prabuddha De is Distinguished Professor of MIS at the University of Dayton. He is also Professor of Accounting and MIS at Ohio State University (on leave of absence during 1987–89). His earned degrees include a B.Sc. (Honors) in Physics from the University of Calcutta, India, an M.S. in Computer Science from Pennsylvania State University, and a Ph.D. in Industrial Administration from Carnegie-Mellon University. He has published in Operations Research, Decision

Sciences, Computers and Operations Research, Information Systems, Journal of MIS, MIS Quarterly, IEEE Transactions on Communications and a number of other journals.

Prior research in model management has attempted to design a model management system which can automate model manipulation dynamically in response to different problems presented by decision makers (Bonczek et al 1983; Dutta and Basu 1984; Blanning 1984a; Dolk and Konsynski et al 1984). But these systems show several weaknesses: (1) the performance of the DSS relies heavily on a predetermined collection of problem solving heuristics acquired from domain experts; (2) similar problem solving heuristics are defined individually and independently; and (3) past problem solving experiences are ignored in solving subsequent problems. These systems ignore the fact that problem-solving knowledge and modeling information provided by human experts may not be complete and perfect initially, and that even a commonly used solution may change over time.

This paper presents a new framework for model management which is able to automate model manipulation more effectively. Machine learning, an evolving technique in artificial intelligence (AI), is applied here to construct such a model management system. We will describe a new approach developed to enable a model management system to generate and modify model manipulation knowledge in a self-learning fashion; that is, the system not only can generate the problem solving process intelligently but can also accumulate generated problem solving knowledge and refine/modify it through domain-specific knowledge and subsequent problems.

In addition to the generation/modification of model manipulation knowledge, two other important issues in model management – the refinement of model representation and the creation of heuristics for model selection – will also be addressed. The former is to enhance the model representation without unrealistically assuming that, once a piece of model manipulation knowledge is created, it is complete and fixed thereafter. The latter is to create heuristics accumulated from experiences of model selection among alternatives. We shall discuss machine learning techniques which can incrementally modify model representation by identifying current insufficiency through experimentation; the heuristics can be intelligently created by dynamically refining the evaluation function.

The remainder of this paper is organized as follows. Section 2 reviews problem solving as it is accomplished by current model management systems. Section 3 introduces machine learning techniques with its major applications to model management systems. Section 4 discusses the methodologies developed for learning model manipulation knowledge. Section 5 provides a brief summary of the work.

## 2. Model Management as Problem Solving

Over the past decade, research on model management systems has focused on two major issues: model representation and model manipulation (Sprague 1980; Hwang 1985).

Model representation involves representing each model with its input and output conditions. As indicated in (Elam and Henderson 1983; Dolk and Konsynski 1984; Applegate et al. 1986; Fedorowicz and Williams 1986), the representational approaches developed so far include predicate calculus within production systems (Bonczek et al. 1980, 1981a, 1981b), graphs (Liang 1987), semantic networks (Elam et al. 1980), frames (Dolk and Konsynski 1984), deep reasoning models based on qualitative physics (Menon and Shaw 1988) and relational database theory (Blanning 1984b). All these systems basically treat models as data so that the user can easily query the system without the burden of programming details and the model management subsystem can be easily integrated into the decision support system (Geoffrion 1987).

Model manipulation involves selecting, retrieving, and activating models to solve problems (Blanning 1984a; Dutta and Basu 1984). The issue of model manipulation has gained more attention recently. Each of the model representation approaches discussed above can satisfactorily represent models, and interact with the database management system. The essential problem solving task, however, lies in model manipulation (Dolk 1986). The current systems may correctly select, retrieve, sequence, and activate the right models from a model base for any particular problem. But no matter which of the above representational schemes is used, these model manipulations are not sufficient to handle increasingly complicated decision problems due to the above-mentioned weaknesses inherent in the existing practice of model-base management.

The major objective of this paper is to construct a model management system with enhanced problem-solving capabilities. The underlying representational system adopted in the paper for facilitating model manipulation is higher order predicate calculus (outlined in Appendix A) and production rules (illustrated in Appendix B).

To that end, we consider improving the abilities of a model management system by embodying it with a domain-independent problem solving strategy, i.e., a general problem solving strategy which can be applied to a number of domains. This general problem solving strategy is a learning strategy that enables the system to accumulate problem solving experiences and to improve its current knowledge incrementally as more and more problems are solved. Hence, the system can improve its performance over time.

No past research has explicitly addressed this issue. The only exception is a simple learning concept described by Bonczek et al. (1980), where a learning method was used to avoid repeating the same problem solving process by recording every past solution. However, this is merely a machine memorization of possibly hundreds or thousands of problem solving approaches. The process is restricted to the exact problems solved previously and thus is inefficient.

Over the past decade, many AI programs have experienced increasing success on building a powerful problem solver with the ability to learn in such applications as board games (Waterman 1970), chemical spectroscopy (Buchanan and Mitchell 1977), symbolic integration (Mitchell 1983), and loan evaluation (Shaw 1987). They are accomplished by machine learning techniques which enable the machine itself to generate problem solving knowledge and refine the knowledge as more problems are accumulated. The knowledge generated from machine learning techniques is similar to heuristics; these heuristics are often imperfect and informal but has useful judgmental value which can be employed in problem-solving situations where precise knowledge is lacking. Each such piece of problem solving knowledge can be used alone or combined with other pieces. In the following sections, we will show how a model management system can apply similar techniques to problem solving in DSS settings; specifically, financial applications will be used to illustrate the new approach.

## 3. The Application of Machine Learning to Model Management

The major applications of machine learning to model management take place in four aspects: (1) the acquisition of model manipulation knowledge, (2) refinement of model manipulation knowledge, (3) the refinement of model representation, and (4) the creation of model selection heuristics. Among these four aspects, there are two basic processes of machine learning: the processes of generalization and refinement.

## 3.1.1. The Acquisition of Model Manipulation Knowledge

One of the deficiencies of the current model management systems is that they do not store the knowledge concerning the problem solving process for a given problem in a form which can be used for similar problems so that the system does not have to spend the same effort repetitively. In other words, the current systems do not generate model manipulation knowledge representing a common problem solving process for a given class of decision problems.

Model manipulation knowledge can be obtained from human experts based on their accumulated expertise. But sometimes it is difficult to obtain consistent and correct knowledge from human experts, causing a bottleneck to system development. A more intelligent knowledge acquisition approach would be to let machines perform this acquisition task itself through some embedded learning ability.

We use the term model manipulation schemata to describe the knowledge generated from past problem solving tasks. Every schema contains a condition part which describes a class of problems and a solution part which indicates the shared problem solving approach of every problem in this class. The problem solving process can be represented in an AND/OR tree structure, which we call the solution tree. An OR subtree in the solution tree denotes all possible alternative solution paths, and an AND subtree indicates the input requirements for a model or a set of subproblems for a decomposable problem. Each subproblem could be as simple as data retrieval from databases or information requests from users, or as complicated as executing a model which needs to further expand an AND subtree indicating its condition (a generalized problem expression)
solution

![](/api/attachments/38KCC29A/fulltext/images/9d64e9b2693f6d80671bbc9fc1922062687ef971fcc0f93299e1f42416768d91.jpg)  
Fig. 1. Model manipulation schema.

input requirements. Some of the inputs may execute other models as well. It should be noted that several models may generate similar solutions to a problem which altogether constitute an OR tree for this problem. Each subtree in the OR tree is an alternative solution path to this problem. Nodes in the bottom of the solution tree are either solvable terminal nodes which are subproblems solved by either data-retrieval or user input – marked with “\*” in the figures – or unsolvable terminal nodes which are subproblems that cannot be solved by data-retrieval, user input or models. The solution tree with at least one solution path whose terminal nodes are all solvable is complete since this solution tree can provide a solution to the problem. Otherwise, it is incomplete since it cannot provide any solution to the problem.

A general framework for such a model manipulation schema is shown in fig. 1. The solution of a stored model manipulation schema is applicable only if a new problem matches with the condition part of this schema.

As the model management system usually deals with the synthesis of two or more models in an appropriate sequence, it involves a multiple-step problem solving process where each step usually involves more than one search on either the database or the model base (see fig. 2). Instead of a blind search, a learned model manipulation schema views the entire multiple-step process as a single module that can be used either as a whole or in part for solving subsequent problems (see fig. 3).

This type of learning model manipulation schemata can be characterized as 'learning of multiple-step tasks', which is also used in (Shaw 1988), (Fikes 1972), (Korf 1982), and (DeJong 1979, 1986). Moreover, the concept of model manipulation schemata is similar to the 'macro-operators' used in (Fikes 1972) and (Korf 1982) for representing the sequence of actions learned. The macro-operators help reduce the amount of search required on the same type of problems, because they are stored in a generalized form that allows similar solutions to be applied (Fikes 1972).

![](/api/attachments/38KCC29A/fulltext/images/4af5d73191fe715dad2ec1e2513d81e9c6e8970dfca6649f8e44173e8cea7214.jpg)  
Fig. 2. A solution without using model manipulation schema.

DeJong (1979, 1986) employed ‘schemata’ to achieve the same purpose, and he also addressed an alternative machine learning approach called explanation based learning (EBL). The machine learning approach we use in this paper examines a number of examples, and constructs the generalization based on their commonalities and differences. By contrast, EBL tries to apply a significant amount of domain knowledge and constructs the generalization based on the explanation of a single example. Although EBL has been successful in several applications where the other learning approach cannot be applied effectively (DeJong 1986), (Shaw 1988), here we adopt the other approach due to several reasons. First, not only do we want the system to generate schemata knowledge through generalization, but we also want it to intelligently refine these schemata as well. EBL does not have a strong refinement ability. Second, like the robot planning problem in STRIPS (Fikes 1972), it is straightforward to construct the cause-and-effect relationships for a particular instance of problem solving. Therefore, it is not necessary to apply EBL to discover any missing intermediate relationships to construct the generalization.

![](/api/attachments/38KCC29A/fulltext/images/ebe92ffb9fa7576e9486b4837a3d2856df1ed6251c4edff56f73dcf6fd965679.jpg)  
Fig. 3. A solution using model manipulation schema.

In addition to automatically acquiring model manipulation schemata, with machine learning techniques the model management system also can learn to refine these schemata after an iterative experimentation process. We shall elaborate on this experimentation process next.

## 3.1.2. Refinement of Model Manipulation Knowledge

The model manipulation schema is a generalization of a specific problem instance and its solution. However, such a generalization may cover more than it is supposed to: it may cover some 'illegal' hypotheses, i.e., hypotheses covered by negative instances. To increase the accuracy of the initially learned schema, the model management system needs to modify the schema through a training process which contains a collection of self-created or teacher-provided experiments. The series of experiments with training instances would help the generalization process converge to the emerging concept, i.e., the learned model-manipulation knowledge.

An experiment with a training instance provides a positive, negative, or a modifiable example for the current schema, but not any combination of them. The positive or negative example is covered by the general problem expression in the condition part of an existing schema. A positive instance has a complete instantiated solution tree, while a negative instance does not. A negative instance is a problem instance which does not belong to the class under consideration. A modifiable instance is a problem instance which differs from the problem expression of the current schema slightly and has a problem solving process very similar to the one in this schema. Defined as the 'near miss instances' in (Winston 1970), modifiable instances are determined by some predefined criterion to determine how similar they should be to the current schema in order to belong to this category. Usually training instances with only one mismatched parameter are treated as modifiable instances.

Negative instances can help the system refine the model manipulation schema by constraining its over-generalized problem description. Modifiable instances can help the system refine the schema by expanding its incomplete problem solving approach.

## 3.1.3. Refinement of Model Representation

Prior research on model management has always assumed that once a model is created, its inputs and outputs will never change. Usually, the most general forms of a model's inputs and outputs are believed to be sufficient to cover all problem instances and thus the model is fully determined. However, this most general model representation may cover many negative instances in addition to all positive instances. Since negative instances may lead the system to use an incorrect problem solving process, their existence significantly affects the accuracy of problem solving by model management systems. Hence, we need a training process, similar to the one in refining a model manipulation, to refine the existing over-generalized model representation.

## 3.1.4. The Creation of Model Selection Heuristics

When there are more than one way to solve a given problem (e.g., regression, moving average, exponential smoothing, and delphi models all can solve a forecasting problem), the model management system usually either can let the user select the best model, or it can choose among these alternative models based on a utility function. This evaluation function, E, is chosen based on past performances or human experts' experiences and is usually in the form of a polynomial of several important factors $f_{i}$ 's:

$$
E = \sum_ {i} w _ {i} ^ {*} f _ {i},
$$

where $w_{i}$ is the weight given to $f_{i}$ . For example, $f_{i}$ 's used in an evaluation function for scoring the performances of several forecasting models could be the accuracy/error, the operating cost, the operating time, and the difficulty of collecting data for each model, where each $f_{i}$ is characterized in a numeric scale (e.g., 0 to 10).

The coefficients of an evaluation function may be changed with different preferences of the users or with different types of problems. A marketing manager may think that the past accuracy of a forecasting mode dominates other criteria, but a bank officer may feel that the computer time of a forecasting method is as, if not more, important. Therefore, different types of problems or users may require different utility functions. Hence, the model management system should be able to self-adjust the coefficients of the evaluation function according to different users or different types of problems and to store these evaluation functions as heuristics which can be applied to similar problems.

For example, in fig. 4, to predict the inventory to assets ratio, the system determines that the RATIO model is needed, which requires the predicted values of both inventory and assets. A previously learned model selection heuristic on forecasting models can be used here to forecast these two predicted values. This heuristic would help reduce the time spent in the selection process and increase the efficiency of searching for the best solution to the problem.

Learning from Credit Assignment for Creating Model Selection Heuristics

Whenever the system selects a model, it should justify the merits of choosing this particular model, and the reasons for treating the rest as undesirable solutions. This is a learning process in that the system not only successfully selects the desirable model, but also examines the underlying reasons for making this selection, thereby improving its "skill" for solving future problems. This type of learning is achieved by applying a technique similar to the one used in the credit assignment problem (Minsky 1963; Sleeman et al. 1982; Langley 1985). The credit assignment problem is to determine which steps in the problem solving process are desirable and to be assigned credits, or undesirable and to be assigned blames. In model selection, desirable models are models which are on the chosen solution path; undesirable models are models which are not on the chosen solution path. The problem solved is a positive example to strengthen the likelihood of choosing the desirable models but a negative example to weaken the likelihood of choosing the undesirable ones.

Samuel's checker-playing (1959) and Rendell's PLS program (1983a) are two successful AI programs to discover/modify the evaluation function through a set of training examples. However, Samuel's program is too domain-dependent and is restricted to game-playing problems where the minimax method and alpha beta pruning (Nilsson 1980) can be used. Rendell's PLS program, on the other hand, is domain-independent with a general methodology which can be applied to different domains based on credit assignment. Our approach enhances the model selection ability in a model management system with the application of PLS.

Pruning Unsatisfiable Models during Model Selection

Before using the evaluation function as a heuristic to choose the best solution, the system can

![](/api/attachments/38KCC29A/fulltext/images/ad4e21d0f684e5eb35326a0d2eb98939693f5755f651de523cd65b622372079b.jpg)  
Fig. 4. An example of problems using an existing model selection heuristic on forecasting models.

![](/api/attachments/38KCC29A/fulltext/images/22f4c29deb49f8d6ee38171327b24394d4474983c8e5a3f2e45d3ce39fe2dbf7.jpg)  
- -- denotes a unsatisfiable model

Fig. 5. Pruning unsatisfiable models during model selection.

reduce the search space by pruning unsatisfiable models. The reason that a model is unsatisfiable is primarily because the current knowledge base cannot totally satisfy every precondition needed for the model to apply. For example, the task of sales forecasting of a new product causes the system to face a decision on the selection of all possible forecasting models that exist in the model base. But models, such as regression and trend analysis models, requiring historical data as preconditions cannot be satisfied since a new product does not have any historical data. Pruning these models in every problem solving step can reduce the search space significantly. In fig. 5, assume that every node, on the average, can grow two subnodes and that the problem is not solved until the third level. Before the pruning of models with incomplete solution paths, the total number of nodes in the solution tree is (4 \* 16 \* 64). After pruning three nodes in the first level and one in each of the second and third levels, the total number of nodes becomes (4 \* 2 \* 2).

## 3.2. The Generalization and the Refinement Processes

As previously explained, the basic processes of learning model manipulation knowledge and model selection heuristics are two-fold: generalization and refinement. The former refers to an inductive inference process and the latter an iterative generalizing-and-constraining process.

As we mentioned before, the model manipulation schema is acquired by generalizing the problem solved. If the system is initially restricted to only one positive instance, a typical generalization would be to change one or more (if necessary) parameters in the problem expression from the instance value to its variable form (Fikes 1972) (e.g., from 1988 to YEAR, or from SALES, to FINANCE-VARIABLE). But such a generalization denotes the maximal generalization which is often over-generalized and needs to be refined to increase its accuracy and completeness.

The refinement on the current over-generalized form contains an iterative generalization and constraining process through a collection of training examples which include both positive and negative instances. $^{1}$ If the current problem expression does not cover the encountered positive example, then it needs to be generalized. If it covers the encountered negative example, then it needs to be constrained.

Instead of the simple, but widely used, maximal generalization, here we use a generalization to a certain extent depending on the current problem expression, the positive example, and the domain knowledge. On the other hand, we impose a certain extent of constraining on the current generalization based on the current problem expression, the negative example, and the domain knowledge.

The domain knowledge here refers to the domain hierarchy and the linear character of parameters. The domain hierarchy contains a set of intermediate generalizations of a parameter between its specific instances and the variable form. From the root to the bottom nodes, the domain hierarchy describes this parameter from general to specific. In other words, it shows the extent of generalization of this parameter from maximal (top) to minimal (bottom). An example of a domain hierarchy of financial variables is shown in fig. 6.

Based on the common parameter of a set of positive instance expressions $\{E_i\}$ , the minimal generalization is performed by climbing the domain hierarchy with a node covering all occurrences of this parameter form $\{E_i\}$ . For example, the problem expression (I/S-var, ?x1, 1988, ABC) is a minimal generalization on two positive instances - (sales, ?x1, 1988, ABC) and (expenses, ?x1, 1988, ABC) - using the domain hierarchy in fig. 6.

Based on the common parameter of both a generalization and a negative instance, a minimal constraining on this generalization is accomplished by reducing this generalization in the domain hierarchy as little as possible without covering this negative instance. Sometimes, more than one common parameter exist. The overall constraining on the generalization will then be a disjunctive set of constrainings resulting from the individual common parameters.

![](/api/attachments/38KCC29A/fulltext/images/d43b9eb8968848c446dd70b25ca8f61e2c22c25a301c4fb219b877588b88e3e2.jpg)  
Fig. 6. A domain hierarchy for financial variables.

## A Version Space for Maintaining the Refined Generalization

The version space approach developed by Buchanan and Mitchell (1977), and Mitchell (1978) can be used to keep track of both the upper bound and the lower bound of a generalization through an incremental training process. We apply the version space approach here to utilize the previously encountered training instances in order to construct a more accurate and more meaningful generalization of a model manipulation schema. To generalize a model manipulation schema, the problem description is characterized by an upper-bound set G and a lower-bound set S. G initially contains all instances covered by the maximal generalization and S initially contains a particular training instance. However, after a series of experimentation, G is constrained to avoid covering negative examples and S is expanded to cover more positive examples encountered. G and S will eventually be equal as more and more training instances are learned. A schema with the highest accuracy is then found.

## 4. Methodologies for Learning Model Manipulation Knowledge

A learning procedure in model management system that not only acquires model manipulation schemata but also improves their problem solving performances is presented in this section. Such a learning procedure consists of four distinct processes: (1) generating/accepting training problems; (2) solving the problems; (3) evaluating the solutions; and (4) generating/refining model manipulation schemata. These four processes can be achieved by four corresponding learning components: the Instance Selector, the Problem Solver, the Critic, and Learning Module, respectively. The Instance Selector produces training problem instances. It accepts new training instances externally or generates them itself as a consequence of previous training processes. The Problem Solver generates the solutions to new instances either by applying existing model manipulation schemata or by employing the embedded deductive inference mechanisms. The resulting solution is then evaluated by the Critic. The Critic examines the solution and classifies a training instance as a positive or a negative example in relation to a certain model manipulation schema. In response to the evaluation made by the Critic, the Learning Module either refines the existing schemata or hypothesizes new schemata.

![](/api/attachments/38KCC29A/fulltext/images/f3a7b40efea9fa1f020f029fc37786330b1e7ee6152e1448f1e2c3a1802b6d3d.jpg)  
Fig. 7. The control flow and data flow in the learning procedure of a DSS.

This learning procedure and the four learning components are integrated into a decision support system with a typical data and control flow diagram as illustrated in fig. 7. In addition to the basic information flows among the learning components, model bases and data bases are incorporated to supply the necessary information; the user interacts with the procedure to start a new problem solving session or to provide additional information; a collection of learned model manipulation schemata and model selection heuristics are maintained by the interaction among the four learning components; the domain hierarchy provides more domain-dependent knowledge; a trainer (usually a domain expert) interacts with the system to assist in the learning procedure.

A detailed learning procedure to build model manipulation knowledge through various learning situations is described below.

## (I) Acquisition of Model Manipulation Knowledge

In the initial model manipulation knowledge acquisition, the learning system accepts a new problem externally, creates its solution path, generalizes it and stores it in the knowledge base as a model manipulation schema. This process is described by the following procedure (shown in fig. 8.a):

(1) The Instance Selector accepts a new problem instance from the external trainer and passes it to the Problem Solver.

(2) The Problem Solver generates its solution tree by using the backward chaining inference process. It first decomposes the problem into subproblems solved by data retrieval or user input. However, for subproblems which are solved by a model, the Problem Solver expands the solution tree by adding the model's preconditions (inputs) which then may be a leaf node by itself; otherwise, further propagations into more subproblems would be necessary.

(3) The Critic evaluates the solution tree.

If there exists at least one solution path whose terminal nodes are all solvable (i.e., the solution

![](/api/attachments/38KCC29A/fulltext/images/98591bcba88cb63072f6b5ee1dea69c3655b2e253da7c75080c6e8c84ad3c4af.jpg)  
Fig. 8.a. The learning procedure in the acquisition of model manipulation knowledge.

![](/api/attachments/38KCC29A/fulltext/images/5e77e2ce6c0224dd4b28cd7660ef0a4b10d62d1e503e7a1288319cdbfad4efdc.jpg)  
Fig. 8.b. An example in the learning procedure in the acquisition of model manipulation knowledge.

path is complete), then this problem is treated as the initial positive example, which could cause the Learning Module to create a new model manipulation schema; otherwise, the problem is failed and the procedure stops.

(4) The Learning Module generates a new model manipulation schema.

Based on this problem instance and its solution tree, the Learning Module can generate a new model manipulation schema with the condition part same as the maximal generalization of this problem expression and the solution part identical to the maximally generated solution tree.

(5) If more knowledge acquisition is needed, go to step 1; otherwise, stop.

An example showing the learning procedure of generating a new model manipulation schema is shown in fig. 8.b. First, the Instance Selector accepts the problem, 'what is the sales figure of ABC company in 1988', (sales, ?x1, 1988, ABC) in (i). Then the Problem Solver generates the solution tree in (ii). Since two solution paths, rooting from PREDICT and TREND, are complete, the Critic classifies this problem as a positive example. The Learning Module creates a new model manipulation schema by generalizing the solution tree in (ii) and the version space with G: (var, ?x1, yr, fn) and S: (sales, ?x1, 1988, ABC) in (iii).

(II) Learning to Refine Model Manipulation Knowledge

A newly created model manipulation schema is usually not accurate enough because of its likely over-generalization. An additional learning procedure is used to refine the schema. This learning procedure (see fig. 9.a) includes generating training examples for modifying the schema representation based on positive, negative, and modifiable examples.

(1) The Instance Selector accepts a new training instance from an external source, or creates a new training example which is covered in the current problem description of the schema and is as close to the previously encountered problem as possible (see the Instance Generator Procedure described below). In the former case, a new training instance could be further classified as a positive, negative, or a modifiable example, but in the latter, it is either a positive or a negative example.

The new training example is created by the following instance generation procedure. A similar procedure under the first order predicate calculus system has been presented by Mitchell (1983).

Instance Generator Procedure

Input: (1) a domain hierarchy structure

(2) a model manipulation schema

Output: a new training example for this schema.
Procedure:

a. Select an element, $s_1$ , from $S$ and an element $g_1$ , from $G$ .

Choose a single parameter (term or predicate) to be substituted.

b. If only one parameter in $s_{1}$ is different from the corresponding one in $g_{1}$ , choose this parameter to be substituted and go to step d; otherwise, go to step c.

c. When more than one such parameter exist in $s_{1}$ , a lowest order parameter (usually a first order parameter) is chosen. If still more than one parameter satisfy this condition and they include a predicate, then select this predicate. Otherwise, randomly choose one.

Choose a new parameter to substitute.

d. Find the corresponding parameter in $g_{1}$ .

e. Examine the domain hierarchy to determine a sibling of the parameter from $s_{1}$ , which is more specific, according to the hierarchy, than the corresponding parameter from $g_{1}$ .

f. If a sibling in the domain hierarchy contains more than one level of nodes, select one of the instances from the lowest level.

g. Substitute the selected instance into $s_{1}$ to form a new training example which is different from $s_{1}$ but is still covered by $g_{1}$ .

(2) The Problem Solver instantiates the model manipulation schema under consideration to create the solution tree in response to this new training example. The instantiation of an existing model manipulation schema in response to the new training example is to pattern match corresponding parameters. Here, the pattern-matching is restricted to an instance matching with its variable form, or a parameter matching with another parameter of the same order. For example, a second order parameter cannot match with a first order parameter.

(3) The Critic examines the instantiated solution tree to determine whether this new training in-

![](/api/attachments/38KCC29A/fulltext/images/e80ee71e3239779fffe731f70e24a1e5637487128210210bdee5a0134de9e5fb.jpg)  
Fig. 9.a. The learning procedure in the refinement of model manipulation knowledge.

![](/api/attachments/38KCC29A/fulltext/images/be1f9a178fdc39119f84241d9f93d1830c3a52fde3d0b1edb0c0f1f36f062fec.jpg)  
Fig. 9.b. An example in the learning procedure in the refinement of model manipulation knowledge.

stance is a positive or a negative example. If a complete solution path exists, the training instance is a positive example; otherwise, it is a negative example.

If this new training example is accepted externally and it is only slightly mismatched with the current problem description of the schema, it is classified as a modifiable example for this schema by the Critic.

(4) The Learning Module refines this model manipulation schema in response to the information sent by the Critic on the nature of the example, viz., positive, negative or modifiable.

(5) If either G and S are equal or if some predetermined resource limits (e.g., processing time) are exceeded, stop; otherwise, go to step 1.

For example, consider the learned scheme in fig. 8.b. Under the instance generation procedure, the Instance Selector selects $s_1$ and $g_1$ as:

$$
\begin{array}{l} s _ {1}: (\text { sales,   ?x1,   1988,   ABC }) \\ g _ {1}: (\text { var,   ?x1,   yr,   fn }). \end{array}
$$

Sales in $s_{1}$ is chosen for substitution, since it is the only predicate among the parameters of $s_{1}$ and $g_{1}$ . With the domain hierarchy of the financial variable (fig. 7), $s_{1}$ can be substituted by any of the following siblings of sales: expense, income tax, etc. Assume that the Instance Selector chooses to substitute sales by expense, generating a new training instance (expense, ?x1, 1988, ABC). The refinement of the schema by a training process using this new instance is shown in fig. 9.b.

Since the instantiated solution tree of fig. 9.b (ii) is complete, this new training instance is classified as a positive example by the Critic. The Learning Module therefore refines the schema by minimally generalizing S to incorporate this positive example. G is not changed, since it already covers this example. The new version space generated by the Learning Module is given by:

G: (var, ?x1, yr, fn)

of sales and expense based on the domain hierarchy.

The modification procedure conducted by the Learning Module according to the three different types of training examples is summarized below.

S: (I/S-var, ?x1, 1988, ABC)

where S is expanded by a minimal generalization

Modification Procedure According to a Positive Example

Input: (1) a positive training example

(2) the model manipulation schema to be modified

![](/api/attachments/38KCC29A/fulltext/images/32faf3d179eaf94018fa8f43b09a018d06c275c788d8e0d81cd86471f3718e3e.jpg)

An example, (percentile, (ratio, asset, liab.), ?x1, 1986, ABC) with the pattern-matching, {assets/var1, liab/var2, 1986/yr, ABC/fn}, has the following instantiated solution:

![](/api/attachments/38KCC29A/fulltext/images/9d386760ee95e3fe3a7032430152de04e3c379b130f0039332f09b4bd0066253.jpg)

solvable, It modifies the condition of this schema as follows:

G: (percentile, (ratio, var1, var2), ?x1, yr, fn)

Fig. 10.a. A positive example of a model manipulation schema.

S: (percentile, (ratio, asset, B/S-var), ?x1, 1986, ABC)

An example, (percentile, (ratio, profits, assets), ?x1, 1988, ABC), with the pattern-matching, {profits/var1, assets/var2, 1988/yr, ABC/fn} has the following instantiated solution.

![](/api/attachments/38KCC29A/fulltext/images/576ecde702f6a107aa618544c5bc2073c6b712e98ea1868b05d75fe6615ac76f.jpg)

Since all terminal nodes are unsolvable, this example is treated as a negative example. It modifies the condition of the schema as follows:

```txt
G: (percentile, (ratio, B/S-var, var2), yr, fn), or (percentile, (ratio, var1, I/S-var), yr, fn), or (percentile, (ratio, var1, var2), yr, fn)^(yr<1988).
S: (percentile, (ratio, assets, B/S-var), 1986, ABC)
```

Fig. 10.b. A negative example of a model manipulation schema.

Output: the refined model manipulation schema Procedure:

1. Minimally generalize $S$ in order to cover this positive example.

2. Remove from $G$ all elements that do not cover the example.

Modification Procedure According to a Negative Example

Input: (1) a negative training example (2) the model manipulation schema to be modified

Output: the refined model manipulation schema Procedure:

1. Remove from $S$ all elements that cover the example.

2. Update G, as little as possible, so that its elements would not cover the negative example.

Modification Procedure According to a Modifiable Example

Input: (1) a modifiable training example

(2) the model manipulation schema to be modified

Output: the refined model manipulation schema Procedure:

1. Locate the unsolvable nodes in the instantiated solution tree.

2. Find the solution for each unsolvable node.

3. Modify the current solution tree in the schema by adding these new solutions.

4. Incorporate this modifiable example into $S$ and add its maximally general form to $G$ .

Fig. 10 illustrates the refinement on an existing model manipulation schema according to a positive example (fig. 10.a), a negative example (fig. 10.b), and a modifiable example (fig. 10.c).

In fig. 10.a, a model manipulation schema created from an initial positive instance, (percentile, (ratio, A/R, inv), x1?, 1986, ABC) $^{2}$ has a version space where the G set is maximally generalized from this instance as (percentile, (ratio, var1, var2), ?x1, yr, fn) and the set is minimally generalized from this instance as itself. An example, (percentile, (ratio, asset, liab), ?x1, 1986, ABC), with a complete instantiated solution tree is classified as a positive example. It modifies the current version space by minimally generating the S set with its common parameters of this positive instance, which then is (percentile, (ratio, asset,

A modifiable example, (percentile, (ratio, inv, (avg, inv)), ?x1, 1986, ABC), with the partial pattern-matching, (inv/var1, 1986/yr, ABC/fn), has the following instantiated solution:

![](/api/attachments/38KCC29A/fulltext/images/7adb6609be07cb2e1848a07f1e4414b3dcfaf2486040e746a85e52af50f51d7a.jpg)  
Fig. 10.c. A modifiable example of a model manipulation schema.

B/S-var), ?x1, 1986, ABC) with asset being the minimal generalization of asset and accounts-receivable, and B/S-var being the minimal generalization of liability and inventory.

In fig. 10.b., the training instance, (percentile, (ratio, profits, assets, ?x1, 1988), has an incomplete solution tree. Consequently, this instance is classified as a negative example for the current schema. It modifies the current version space by constraining the G set to be (percentile, (ratio,

B/S-var, var2), yr, fn), (percentile, (ratio, var1, I/S-var), yr, fn), or (percentile, (ratio, var1, var2), yr, fn) (yr < 1988).

In fig. 10.c, a modifiable example expands the insufficiency of the current problem solving scheme (or the solution tree) by adding one more precondition of the RATIO model, (avg, var1, ?x5, yr, fn). The G and S sets in the current version space are also expanded to include the maximal and minimal generalizations of this example.

(III) Learning to Refine Model Representation

The learning procedure for refining model representation is similar to the aforementioned generalization procedure.

A general regression model, for example, could be represented by the following primitive form: $^{3}$

(var1, ?x1, yr1, fn) & (var2, ?x2, yr1, fn)

& (GT, yr2, yr1)

& (REGRESSION, ?x1, ?x2, ?x3, yr, fn)

$\Rightarrow (\mathrm{var1},? \mathrm{x3}, \mathrm{yr2}, \mathrm{fn})$

This REGRESSION model analyzes the past dependency between var1 and var2 to predict the future value of var1. A query, such as, 'what is the sales figure of ABC firm in 1983', matches with the consequence of the REGRESSION model, (var1, ?x3, yr2, fn). But actually this query cannot be answered by the REGRESSION model since it asks for the past value of sales, a data retrieval operation, instead of the output of the REGRESSION model. This shows that the current representation of the REGRESSION model is too general to cover such a query. Therefore, this problem instance (the query) can be used as a negative example to constrain the current over-generalized representation of the REGRESSION model through a refinement process. During the refinement process, the Learning Module prescribes that the condition, (GT, yr1, 1983) or (LT, yr1, 1983), needs to be added to the current consequence of the REGRESSION model (GT stands for 'greater than' and LT stands for 'less than').

## (IV) Learning Model Selection Heuristics

Instead of the traditional model selection approach using a static evaluation function, we adopt a machine learning technique which can dynamically refine the evaluation function of model selection based on the idea of credit assignment mentioned earlier. The objective is to make model selection adaptive to the user's preference. Based on the concepts articulated in Rendell's probabilistic learning system (PLS) (1983, 1985, 1986), we use feature space, utilities (probabilities), errors, and layered knowledge structures to develop a dynamic evaluation function which can be incrementally modified. As such, the performance evaluation is represented in the form of a region defined as follows:

$$
P = (r, u, e),
$$

where r is a rectangular region in the feature space, u is the probability given by the ratio of the positive instances to the total observed instances in this region, and e is the error rate allowed in this region. This PLS framework can be applied to generate heuristics for model selection, as shown in fig. 11. The models can be classified based on two criteria: (1) quality of solution and (2) time complexity, which comprise the two dimensions of the feature space. The feature space is classified into regions. Each region represents a combination of quality of solution and time complexity of the same utility. For a given model, the corresponding utility – which represents the model selection heuristics – can be determined by mapping it into the feature space. This approach progressively refines the heuristics assigned to each region by splitting a region into smaller regions. In addition, unlike some of the other learning system (e.g., errors in the training set or noisy data by considering the error term of each region, i.e., the allowable rate for misclassifying a model.

For example, in fig. 11.a, the three problems – 'the sales next year', 'the inventory three years later', and 'the interest expense next year' – all face the decision of choosing the best forecasting model. For the sake of simplicity, as in the figures, we use the two more important criteria – quality of solution and time complexity – for evaluating alternative models. Based on past experiences, some predefined evaluation function, or the user's preference, the Problem Solver may choose different forecasting models (e.g., the regression model for the first problem, the moving-average model for the second one, and again the regression model for the third one) for solving these problems. The chosen model for each problem is then treated as a positive instance, and the rest are treated as negative instances by the Critic.

Using each model's quality of solution and time complexity, the Learning Module can localize the model in the feature space (fig. 11.b). In order to predict the performance of model selection on the same set of forecasting models for subsequent

(a)  
![](/api/attachments/38KCC29A/fulltext/images/fbacf0e32d86e05fbe048b93bd673a78963ddef87ecc0ffac6c38a9cafea4c53.jpg)

F1: REGRESSION
F2: MOVING AVERAGE
F3: EXPONENTIAL SMOOTHING
F4: DELPHI

P1: THE SALES NEXT YEAR
P2: THE INVENTORY THREE YEARS LATEI
P3: THE INTEREST EXPENSE NEXT YEAR

(b)  
(c)  
![](/api/attachments/38KCC29A/fulltext/images/81ee636c761616786452eb4dc6cf3f9e2e39eb76e2a04c799072668f162e1192.jpg)  
o -- denotes a positive instance  
- -- denotes a negative instance

Fig. 11. An example of learning model selection heuristics using Rendell's PLS program.

problems, the Learning Module further divides the feature space into several utility classes using the following procedure. Initially, it arbitrarily splits the feature space into two regions, and calculates the success probability, $u$ , in each of these regions. In fig. 11.b, an arbitrary splitting generates the regions, $r_1$ and $r_2$ , which initially have the utilities (probabilities) $u_1 = 2/7$ , and $u_2 = 1.5$ , respectively. Each region is then refined by a further splitting, where the best splitting is measured by the largest dissimilarity $d$ among all possible dichotomies which horizontally or vertically divide the region at each integer point of the axes. A dissimilarity measure $d$ for each splitting is defined as $(|\log u_1 - \log u_2| - \log (e_1 / e_2))$ , where $u_1, u_2$ , and $e_1, e_2$ , are the utility and error rates for the two regions after the splitting. The splitting process is repeated until $d \leq 0$ for every region, which results in the division shown in fig. 11.c. Now every region is a utility class which has similar utility for every occurrence in the same region but is as dissimilar as possible to every occurrence in any other region.

Using the region representation, the system is able to predict the success probability of each new alternative model by using the utility class a model belongs to, which has the same effect as that of an evaluation function. But this approach can incrementally refine the region's representation through more training instances; thus it provides a way to make the heuristic adaptive. Moreover, the error allowance can be changed arbitrarily.

## Pruning Unsatisfiable Models

When multiple models are possible solutions, some of them may not be applicable, since they may not have a complete solution path. Before evaluating any model the system needs to examine whether there exist models with incomplete solution paths. For example, there are four possible solution paths generated by the Problem Solver under REGRESSION, EXPONENTIAL

SMOOTHING, MOVING AVERAGE, and DELPHI models to the problem, (sales, new-product-name, ?x, ABC, 1988), since all these forecasting models have the output matching with this problem. But the solution paths of REGRESSION, EXPONENTIAL SMOOTHING, and MOVING AVERAGE models are not complete, because these models require some historical data as input which cannot be obtained for a new product. Only the DELPHI model, which does not require historical data, has a complete solution path for this problem. Therefore, the Critic classifies the DELPHI model as a positive example and the rest of the models as negative examples. The Learning Module can then modify the preconditions of these four models in light of this information.

## 5. Summary

In this paper, we present a new design for model management systems that can automatically generate model manipulation knowledge, incrementally refine the acquired knowledge and model representation, and intelligently adjust the utility function used to select the best solution. This new design is constructed under a general framework with four learning components – the Instance Selector, the Problem Solver, the Critic, and the Learning Module. The methodology presented not only overcomes several weaknesses exhibited in most model management systems currently available in the literature but also introduces a more intelligent framework for designing decision support systems (Shaw 1988).

## Appendix A

## Predicate Calculus Language

The basic elements in the predicate calculus language are:

1. constants - the objects in the domain of discourse,

2. variable - individual variables range over objects,

3. functions - matching from a sets of variables (or constants) to a set of variables (or constants), which is a special kind of relation,

4. relations - e.g., an example of relations between variables is $x > y$ .

The language basically consists of two categories of syntactic entities: a term and a predicate.

We can define a term recursively as

(1) a constant;

(2) a variable;

(3) an $n$ -ary function, $(f, t_1, \ldots, t_n)$ , where $f$ is the function symbol and each $t_i$ is a term. Examples of terms are 17, $x$ , $(2 + 5)$ , $-7$ , $x^3$ .

A predicate expresses properties or relations on a fixed domain of discourse. An n-ary predicate will be defined as a list of $n+1$ elements, $(p, t_{1}, \ldots, t_{n})$ , where p represents the predicate symbol and each $t_{i}$ is a term. A first order predicate has terms as arguments, but a higher order predicate (second order, third order, ..., etc.) may have lower order predicates as arguments in addition to terms.

## Appendix B

Production Rules for Applying Models in Loan Evaluation

In a DSS, production rules can be used to represent model knowledge. The application of each model is directed by an if-then rule and interpreted as 'if the input requirements are satisfied and the model thus becomes executable, then the output value is...' In the model predicates, we use the upper case to specify the model, underlines to represent the input values, and the rest to represent the output values. Some of the rules directing model applications in a loan-evaluation DSS are listed here. Machine learning techniques can be used to learn additional rules or to refine existing rules.

(1) (var1, ?x1, yr1, fn) & (var2, ?x2, yr1, fn) & (REGRESS, ?x1, ?x2, ?x3, ?x4, yr, fn) $\Rightarrow (\beta, \text{var1}, \text{var2}, ?x3, \text{yr}, \text{fn})$ & $(R^2, \text{var1}, \text{var2}, ?x4, \text{yr}, \text{fn})$ With the input values, ?x1 and ?x2, of var1 and var2 in a given year for a particular firm, the REGRESS model outputs values, ?x3 and ?x4, of $\beta$ and $R^2$ between the two input variables.

(2) (var1, ?x1, yr, fn) & (var2, ?x2, yr, fn) & (RATIO, ?x1, ?x2, ?x3, yr, fn)
⇒ (ratio, var1, var2, ?x3, yr, fn)
Using the input values, ?x1 and ?x2, of var1 and var2 in a given year for a given firm, the

Ratio model calculates the value of their ratio, ?x3.

(3) (var, ?x1, yr, fn) & (var, ?x2, (-yr 1), fn) & (var, ?x3, (-yr 2) & (AVG, ?x1, ?x2, ?x3, ?x4, yr, fn)
⇒ (avg, var, ?x4, yr, fn)
Using the input values, ?x1, ?x2, and ?x3, of var from three consecutive years, the AVERAGE model calculates their average value, ?x4.

(4) (var, ?x1, yr, fn) & (industry-type, ?x2, yr, fn) & (PERCENTILE, ?x1, ?x2, ?x3, yr, fn) $\Rightarrow$ (percentile, var, ?x3, yr, fn, ?x2) Using the value of var and the industry type of this firm, the PERCENTILE model calculates its percentile value of var in its industry.

(5) (var, ?x1, yr, fn) & (industry-type, ?x2, yr, fn) & (MEDIAN, ?x1, ?x2, ?x3, yr, fn)
⇒ (median, var, ?x3, yr, fn, ?x2)
Using the value of var and the industry type of this firm, the MEDIAN model calculates its median value of var in its industry.

(6) (var, ?x1, yr, fn) & (tax-type, ?x2, yr, fn) & (TAX, ?x1, ?x2, ?x3, yr, fn)
⇒ (after-tax, var, ?x3, yr, fn)
Using the value of var and the tax-type of this firm, the TAX model calculates the after-tax value of var.

(7) (var, ?x1, yr, fn) & (var, ?x2, (-, yr, 1), fn) & (var, ?x3, (-, yr, 2), fn) & (TREND, ?x1, ?x2, ?x3, ?x4, yr, fn)
⇒ (trend, var, ?x4, yr, fn)
Using the value of var from three consequentively value years, the TREND model calculates the trend of var.

(8) (ratio, (+, long-term-debt, curr-liab, ?x1, yr, fn), total-assets, ?x2, yr, fn) & (ratio, funds-from-op, (+, interest, (avg, debt-maturity, ?x4, yr, fn) & (trend, sales, ?x5, yr, fn) & (RISK-SCORE, ?x1, ?x2, ?x3, ?x4, ?x5, ?x6, yr, fn)
⇒ (risk-score, ?x6, yr, fn)
Using (long-term-debt + current-liabilities) to total-assets ratio, and funds-from-operation to (interest + the-average-debt-maturity) ratio, the RISK-SCORE model calculates the risk score of this firm.

(9) (interest-income, ?x1, yr, fn) & (cost-of-handling-deposit, ?x2, yr, fn) & (avg, loan-volume, ?x3, yr, fn) & (avg, collected-balance, ?x4, yr, fn) & (risk-score, ?x5, yr, fn) & (LT, ?x5, 0) & (LOAN-YIELD-I, ?x1, ?x2, ?x3, ?x4, ?x5, ?x6, yr, fn)
⇒ (loan-yield, ?x6, yr, fn)
Using the interest-income, cost-of-handling-deposit, three year average loan-volume and collected-balance, and the risk-score, under the condition that the risk score is less than 0, the LOAN-YIELD-I model calculates the loan-yield of this firm.

(10) (interest-income, ?x1, yr, fn) & (cost-of-handling-deposit, ?x2, yr, fn) & (avg, loan-volume, ?x3, yr, fn) & (avg, collected-balance, ?x4, yr, fn) & (risk-score, ?x5, yr, fn) & (GT, ?x5, 0) & (LCAN-YIELD-II, ?x1, ?x2, ?x3, ?x4, ?x5, ?x6, yr, fn)
⇒ (loan-yield, ?x6, yr, fn)
Using the interest-income, cost-of-handling-deposit, three year average loan-volume and collected-balance, and the risk-score, under the condition that the risk score is greater than 0, the LOAN-YIELD-II model calculates the loan-yield of this firm.

(11) (interest-income, ?x1, yr, fn) & (cost-of-handling-deposit, ?x2, yr, fn) & (avg, loan-volume, ?x3, yr, fn) & (avg, collected-balance, ?x4, yr, fn) & (risk-score, ?x5, yr, fn) & (GT, ?x5, 1.255) & (LOAN-YIELD-III, ?x1, ?x2, ?x3, ?x4, ?x5, ?x6, yr, fn)  
⇒ (loan-yield, ?x6, yr, fn)  
Using the interest-income, cost-of-handling-deposit, three year average loan-volume and collected-balance and the risk score, under the condition that the risk-score is greater than 1.255, the LOAN-YIELD III model calculates the loan-yield of this firm.

(12) (interest-income, ?x1, yr, fn) & (cost-of-handling-deposit, ?x2, yr, fn) & (avg, loan-volume, ?x3, yr, fn) & (avg, collected-balance, ?x4, yr, fn) & (risk-score, ?x5, yr, fn) & (GT, ?x5, 2.79) & (LOAN-YIELD-IV, ?x1, ?x2, ?tx3, ?x4, ?x5, ?x6, yr, fn)
⇒ (loan-yield, ?x6, yr, fn)
Using the interest-income, cost-of-handling-deposit, three year average loan-volume and collected-balance, and the risk-score, under

the condition that the risk score is greater than 2.79, the LOAN-YIELD-IV model calculates the loan-yield of this firm.

(13) (trend, interest-rate, ?x1, yr, fn) & (interest-rate, ?x2, yr, fn) & (loan-period, ?x3, yr, fn) & (GT, ?x3, 3, 12) & (ST-LOAN-RATE, ?x1, ?x2, ?x3, ?x4, yr, fn)
⇒ (st-loan-rate, ?x4, yr, fn)
Using the trend of interest-rate, interest-rate, and the loan-period, under the condition that the loan-period is between 3 to 12 months, the ST-LOAN-RATE model calculates the short term loan rate of this firm.

(14) (trend, interest-rate, ?x1, yr, fn) & (interest-rate, ?x2, yr, fn) & (loan-period, ?x3, yr, fn) & (GT, ?x3, 12) & (LT-LOAN-RATE, ?x1, ?x2, ?x3, ?x4, yr, fn)
⇒ (lt-loan rate, ?x4, yr, fn)
Using the trend of interest-rate, interest-rate, and the loan-period, under the condition that the loan-period is greater than 12 months, the LT-LOAN-RATE model calculates the long term loan rate of this firm.

(15) (interest-cost, ?x1, yr, fn) & (operating-cost, ?x2, yr, fn) &
(avg-assets, ?x3, yr, fn) & (reserve-requirements, ?x4, yr, fn) &
(COST-OF-FUNDS, ?x1, ?x2, ?x3, ?x4, ?x5, yr, fn)
⇒ (cost-of-funds, ?x5, yr, fn)
Using the interest-cost, operating-cost, three year average assets, and the reserve-requirements, the COST-OF-FUND model calculates the cost-of-fund of this firm.

(16) (costs-of-funds, ?x1, yr, fn) & (loan-yield, ?x2, yr, fn) & (COMPENSATING-BALANCE, ?x1, ?x2, ?x3, yr, fn) $\Rightarrow$ (compensating-balance, ?x3, yr, fn) using the cost-of-funds, and the loan-yield, the COMPENSATING-BALANCE model calculates the compensating-balance of this firm.

## References

Applegate, L.M., Konsynski, B.R., and Nunamaker, J.F., Model Management Systems: Design for Decision Support, Decision Support Systems, vol. 2, 81–91, 1986.

Blanning, R.W., Issues in the Design of Expert Systems for Management, Proc. of the 1984 National Computer Conference, 1984a.

Blanning, R.W., Expert Systems for Management: Possible Application Areas, DSS-84 Transactions, W. Zmud (ed.), 69–77, 1984b.

Bonczek, R.H., C.W. Holsapple, and A.B. Whinston, Future Directions for Developing Decision Support Systems, Decision Science, Vol. 11, pp. 616–631, 1980.

Bonczek, R.H., C.W. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, 1981a.

Bonczek, R.H., C.W. Holsapple, and A.B. Whinston, A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management, Operations Research, Vol. 29, No. 2, March–April 1981b.

Bonczek, R.H., C.W. Holsapple, and A.B. Whinston, Specification of Modeling and Knowledge in Decision Support Systemis, in H.G. Sol. (ed.) Processes and Tools for Decision Support, North Holland: Amsterdam, 1983.

Buchanan, B.G., T.M. Mitchell, R.G. Smith, and C.R. Johnson, Jr., Models of Learning Systems, Encyclopedia of Computer Science and Technology, Dekker, Vol. 11, 1978.

Buchanan, B.G., and T.M. Mitchell, Model-Direct Learning of Production Rules, Proceedings of the Workshop on Pattern-Directed Inference Systems, Honolulu, Hawaii, May 1977.

DeJong, G., Prediction and Substantiation: A New Approach to Natural Language Processing, Cognitive Science 3, pp. 251–273, 1979.

DeJong, G., An Approach to Learning from Observation, in Machine Learning: An Artificial Intelligence Approach, Vol. II, R.S. Michalski, J.G. Carbonell, and T.M. Mitchell (Eds.), Morgan Kaufman, Los Altos, California, 1986.

Dolk, D.R., and B. Konsynski, Knowledge Representations for Model Management Systems, IEEE Transactions on Software Engineering, Vol. 10(6): 619–628, November 1984.

Dolk, R.D., Data as Models: An Approach to Implementing Model Management, Decision Support Systems 2, 73–80, 1986.

Dutta, A. and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support System, IEEE Computer, 89–97, September 1984.

Elam, J.J., J.C. Henderson and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proceedings of the First Conference on Information Systems, 1980.

Elam, J.J., and Henderson, J.C., Knowledge Engineering Concepts for Decision Support System Design and Implementation, Information & Management 6, 109–114, 1983.

Elam, J.J., and Konsynski, B., Using Artificial Intelligence Techniques to Enhance the Capabilities of Model Management Systems, Decision Sciences, vol. 18, 487–502, 1987.

Fedorowicz, J., and Williams, G.B., Representing Modeling Knowledge in an Intelligent Decision Support System, Decision Support Systems 2, 3–14, 1986.

Fikes, R.E., P.E. Hart, and N.J. Nilsson, Learning and Executing Generalized Robot Plans, Artificial Intelligence 3:251–288, 1972.

Geoffrion, A.M., An Introduction to Structured Modeling, Management Science, vol. 33, No. 5, 547–589, May 1987.

Konsynski, B., and Sprague, R.H., Jr. Future Research Direc-

tions in Model Management, Decision Support Systems 2, 103–109, 1986.

Korf, R.E., Learning to Solve Problems by Searching for Macro-Operators, Ph.D. thesis, Department of Computer Science, Carnegie-Mellon University, July 1983.

Hwang, S., Automatic Model Building Systems: A Survey, DSS-85, Transactions, San Francisco, California, 22–32, 1985.

Langley, P., Learning to Search: From Weak Methods to Domain-Specific Heuristics, Cognitive science 9, 217–260, 1985.

Liang, T.P., Development of a Knowledge-Based Model Management System, BEBR Report No. 1364, Dept. of Accountancy, University of Illinois, Champaign, 1987.

Menon, U. and Shaw, M.J., Qualitative Reasoning and Modeling for Decision Support, Technical Report, Dept. of Business Administration, University of Illinois, 1988.

Michalski, R.S., J.G. Carbonell, and T.M. Mitchell (eds.), Machine Learning: An Artificial Intelligence Approach, Tioga Publishing Co., Palo Alto, California, 1983.

Minsky, M., Steps towards Artificial Intelligence, in E.A. Feigenbaum and H. Feldman (Eds.), Computers and Thought, McGraw-Hill, New York, 406–450, 1963.

Mitchell, T.M., P.E. Utgoff, and R. Banerji, Learning by Experimentation: Acquiring and Refining Problem-Solving Heuristic, in Machine Learning: An Artificial Intelligence Approach, R.S. Michalski, J.G. Carbonell, and T.M. Mitchell (eds.), Tioga Publishing Co., Palo Alto, California, 1983.

Nilsson, N.J., Principles of Artificial Intelligence, Tioga, Palo Alto, 1980.

Rendell, L.A., A New Basis for State-Space Learning Systems and a Successful Implementation, Artificial Intelligence 20, 369–392, 1983.

Rendell, L.A., Utility Patterns as Criteria for Efficient Generalization Learning, Proceedings on Intelligent Systems and Machines, 1985.

Rendell, L.A., Induction, of and by Probability, Uncertainty in AI, L. Kanal and J. Lemmer (Eds.), North Holland, 1986.

Samuel, A.L., Some Studies in Machine Learning Using the Game of Checkers, IBM Journal of Research and Development, 3, 210–229, 1959.

Shaw, M., Applying Inductive Learning to Enhance Knowledge-Based Expert Systems, Decision Support Systems, Vol. 4, No. 4, 1987, pp. 319–332.

Shaw, M.J., Gentry, J., Incorporating Inductive Learning in a Loan Evaluation DSS, Journal of Financial Management, v. 17, Fall 1988.

Shaw, M.J., Learning Model Management Knowledge in Intelligent DSS, BEBR Report No. 1483, Dept. of Business Administration, University of Illinois, 1988.

Shaw, M.J., An Integrated Framework for Applying Machine Learning to Intelligent Decision Support Systems, BEBR Report No. 1485, Dept. of Business Administration University of Illinois, 1988.

Sleeman, D., T.M. Mitchell, and P. Langley, Learning from Solution Paths: An Approach to the Credit Assignment Problem, The AI Magazine, Spring 1982.

Sprague, R.H., Jr., A Framework for the Development of Decision Support Systems, MIS Quarterly, 1–26, December 1980.

Waterman, D.A., Generalization Learning Techniques for Automating the Learning of Heuristics, Artificial Intelligence 1, 121–170, 1970.

Winston, P.H., Learning Structural Description from Examples, Ph.D. thesis, Massachusetts Institute of Technology, Cambridge, Massachusetts, 1970.
