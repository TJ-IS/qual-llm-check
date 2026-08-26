---
otero_id: 26748
otero_key: "R6QPVHGB"
title: "Providing Design Assistance: A Case-Based Approach"
authors: "Atish P. Sinha; Jerrold H. May"
year: "1996"
journal: "Information Systems Research"
doi: "10.1287/isre.7.3.363"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [131.94.16.10] On: 21 September 2016, At: 00:38 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## HSR Information Systems Research

![](/api/attachments/R6QPVHGB/fulltext/images/93f0d2991404073c1af29833a9636f7035394918d9ce2ebb0f0d2462011f0763.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Providing Design Assistance: A Case-Based Approach

Atish P. Sinha, Jerrold H. May,

## To cite this article:

Atish P. Sinha, Jerrold H. May, (1996) Providing Design Assistance: A Case-Based Approach. Information Systems Research 7(3):363-387. http://dx.doi.org/10.1287/isre.7.3.363

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1996 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/R6QPVHGB/fulltext/images/37f8dac186fd3702c65db412f462a9041d79e6298f9ec6b999c99373b935f8ab.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Providing Design Assistance: A Case-Based Approach

Atish P. Sinha • Jerrold H. May

Department of MIS & Decision Sciences, University of Dayton, Dayton, Ohio 45469-2130
sinha@udayton.edu

Joseph M. Katz Graduate School of Business, University of Pittsburgh, Pittsburgh, Pennsylvania 15260 jerrymay@vms.cis.pitt.edu

This paper presents an integrated and comprehensive framework for decision support. A model integrating case-based reasoning with constraint posting and multicriteria decision making is proposed for providing effective and efficient assistance in solving routine design problems. The model is developed based on an analysis of the knowledge acquired from experts in engineering design, and is subsequently operationalized as a computer-based design assistant called IDEA. IDEA employs constraint posting to initially bound the design space and to maintain consistency of the design solutions. Case-based reasoning allows IDEA to generate new designs by retrieving, adapting, and composing from similar cases in memory. Finally, IDEA optimizes multiple objectives to identify a set of pareto-optimal designs. By organizing computer memory as a collection of cases and case snippets, and by adapting and synthesizing those cases and snippets—using techniques similar to those employed by design experts—IDEA provides valuable design assistance. In addition to providing a framework for decision support, the research makes specific contributions to case-based design. It shows how case snippets can be retrieved, adapted, and synthesized to generate multiple design solutions, whose consistency is enforced through a dynamic constraint management mechanism. The concepts and techniques developed for performing dynamic adaptation (adaptation during composition from case snippets) and for maintaining an evolving solution space (a solution space that shrinks and expands over time) contribute to the state-of-the-art in case-based design.

(Case-Based Reasoning; Constraint Posting; Decision Support; Design Assistance; Multicriteria Decision Making)

## 1. Introduction

The area of decision support systems (DSSs) has evolved over the last 20 years or so. As the field matures, some researchers feel that only two attributes are required in a basic definition of DSS: (1) the DSS should support decision making rather than replace the decision maker; and (2) the DSS should be used in semistructured or unstructured decision situations (Konsynski et al. 1992). Most DSS researchers also view these two attributes as essential (Alter 1994, Keen and Scott Morton 1978, Keen 1989, Sprague and Carlson 1982). The potential benefits of a DSS include: (1) better decisions, (2) an increase in the number of alternatives examined, (3) time and cost savings, (4) a better understanding of the business, (5) new insights and learning, and (6) better use of the data resource (Keen 1989). Given that most of the benefits provided by a DSS are qualitative, evaluating a DSS is difficult because traditional cost-benefit analysis techniques cannot be used (Keen 1989). Also, as Keen and Scott Morton (1978) point out, because there are no clear criteria for assessing performance, the effectiveness of the system largely depends on its evolving usage.

In their review and critique of DSS, Konsynski et al. (1992) identified several new research directions. They point out the need for more research in developing systems that provide support in the intelligence and design phases, because DSS research and application have primarily focused on the choice phase. Also, the research focus has been on modeling and data analysis, where the effort has been largely devoted to structuring as much as possible of the decision problem, leaving the unstructurable part unsupported. General problem-solving abilities such as reasoning by analogy have been largely neglected. This view is also shared by other researchers (Sprague et al. 1992), who cite the lack of use of case-based reasoning (CBR) as a limitation of current approaches.

CBR is a problem solving paradigm in the field of Artificial Intelligence (AI) in which past cases are retrieved from memory and are utilized to solve a new problem (Kolodner 1993, Riesbeck and Schank 1989). Cases that were successful, as well as those that were failures, are stored in a memory called case memory. The basic philosophy of CBR is that if a case has worked before, it should be used to solve similar problems in future; if a case has failed on a previous occasion, then the same mistake should not be repeated. CBR has been presented as a general paradigm for reasoning from experience (Slade 1991). It has been proposed as a methodology for solving problems in such diverse domains as legal reasoning (Ashley and Rissland 1987, Ashley 1990), diagnosis (Bareiss 1989, Koton 1988, Redmond 1989), dispute mediation (Kolodner and Simpson 1989, Simpson 1985, Sycara 1987), meal planning (Kolodner 1987), and software effort estimation (Mukhopadhyay et al. 1992). CBR seems to be especially appropriate for domains in which there does not exist a strong theory built up from first principles. Expertise then derives from experience, properly organized, rather than from knowledge of rules or factual statements.

The focus of CBR to date has been on problem solving, rather than on providing assistance in problem solving. Departing from the traditional norm, Kolodner (1991, p. 52) presents case-based decision-aiding as “a methodology for building systems in which people and machines work together to solve problems. The case-based decision-aiding system augments the person's memory by providing cases (analogues) for a person to use in solving a problem. The person does the actual decision making using these cases as guidelines." A system that provides assistance to a human user in areas where he usually has trouble—such as retrieving the right cases—while allowing him to do other things, such as making the final decision, is more likely to be adopted and relied upon than a system that simply outputs the final solution to the user, without involving him at all.

So while DSS researchers point to the need for employing techniques such as CBR for supporting the relatively unstructured part of decision making, CBR proponents argue for a stronger decision support role. Realizing that their goals are complementary, we aim to explore the feasibility of incorporating the CBR approach within a DSS framework. Our central thesis is that such an incorporation would result in a powerful decision support methodology. The thesis is tested on a Class 3 or routine design problem (Brown and Chandrasekaran 1989). In routine problems, an a priori plan of the solution exists—the decomposition of the problem is known and plans for each of the components exist. At each stage of the design process, the designer knows what the alternatives are. The solution lies in finding the appropriate alternatives for each component such that the given constraints are satisfied. Class 3 problems could then be solved by search; total enumeration would guarantee an optimal solution, were it not impractical due to the size of the design space. We believe that a DSS methodology incorporating CBR would provide valuable assistance by identifying only the best alternatives. Such a methodology can be applied to a wide range of DSS applications; however, we do not claim that the approach is going to work for more creative forms of human endeavor, such as innovative design.

We present a model that uses design knowledge, implicit in the form of existing design cases, to provide an effective and efficient medium for design assistance (Section 4 describes the effectiveness and efficiency measures used to evaluate the model). $^{1}$ The model integrates case-based reasoning with constraint posting and multi-criteria decision making to provide a comprehensive architecture for design assistance. The model is implemented as a computer-based design assistant called IDEA. CBR allows IDEA to reason from past cases, while constraint posting bounds the design space and maintains consistency. In the absence of strong causal theories of the domain, which is typical of design environments, the weak model provided by the constraint manager serves the purpose of progressively constraining and revising the design space, and of ensuring consistency of the design solutions. The case-based reasoner further reduces the design space generated by the constraint manager to one that consists of only cases from case memory.

IDEA provides design assistance by posting constraints; retrieving, adapting, and synthesizing cases; maintaining multiple solutions; and identifying attractive solutions—tasks that a human designer finds difficult and time-consuming (Kolodner 1991). Constraint posting allows IDEA to automate design calculations whose sheer volume impedes proper analysis and evaluation. Such automation is viewed as a predictor of success for a DSS (Alter 1994). By making better use of a key data resource—existing design cases—IDEA recognizes another DSS benefit (Alter 1994, Keen 1989). Also, by maintaining all feasible solutions, IDEA substantially increases the number of alternatives examined, a key benefit of a DSS (Keen and Scott Morton 1978, Keen 1989). While IDEA performs tasks that a human designer finds daunting, other tasks, such as revising specifications, selecting a solution from among multiple optimal solutions, and doing detailed design and costing, are left to the human user, because humans are good at these tasks (Kolodner 1991), and also because we wanted to avoid ineffectual efforts to automate tasks that are, given the current state of our knowledge, inherently unstructured (Bonczek et al. 1981, Keen and Scott Morton 1978, Konsynski et al. 1992). The division of responsibilities between the two, however, is an issue that can be properly resolved only with evolving usage.

Our work also makes important contributions in the areas of case adaptation and case composition. In addition to the traditional use of rules for case adaptation, the model employs two novel and attractive techniques for adapting cases. First, IDEA uses a dependency network, generated by the constraint manager, to perform constraint relaxation by recursively tracing backward through the dependency network; constraint propagation, therefore, is not unidirectional. Second, IDEA performs dynamic adaptations when two or more snippets are combined together to form a composite solution; such adaptations are needed when the snippets interact. $^{2}$

Another contribution, which arises out of the dynamic constraint revision mechanism, is the notion of an evolving solution space. IDEA maintains a solution space that consists of multiple solutions, not just one solution. Because many design constraints are dynamic, the solution space evolves over time. Dynamic constraint relaxation has the effect of expanding the solution space; some solutions that earlier were inconsistent later enter the solution space. If a dynamic constraint later becomes more restrictive, the solution space shrinks. Maintaining an evolving solution space prevents IDEA from ruling out any potentially attractive solutions. From a DSS perspective, this function is important not only because it results in a large number of alternative solutions, but also because it recognizes the iterative and dynamic nature of a complex decision making process.

This research has much broader implications, outside the realm of engineering design. The model provides an integrated and comprehensive framework for decision support. The encouraging results from IDEA's evaluation (see §4) suggest that the model is potentially applicable to stable, complex domains endowed with a rich history of cases. IDEA opens up a new and exciting area for future research: providing decision support through cases. The techniques developed in our work—for decomposing tasks, functions, and constraints; retrieving good cases; identifying local and global inconsistencies; progressively revising/relaxing functions and constraints; performing dynamic case adaptation and composition; generating and maintaining multiple solutions; and optimizing multiple conflicting criteria—could prove to be useful for future research in case-based decision support.

The outline of the paper is as follows. Section 2 reviews some prior research that provides the background for the current research. Section 3 describes the development of the case-based model. Section 4 describes the computer implementation and evaluation of the model. Section 5 describes the relationship of our work to prior work in case-based design and discusses the implications for IS/DSS research. Section 6 concludes the paper and outlines directions for future research.

## 2. Background

Mostow (1985) identified the state of the design, the goal structure of the design process, design decisions, rationales for design decisions, control of the design process, and the role of learning in design as research issues that should be considered in developing knowledge-based design models. His guidelines proved to be useful for future researchers, who used a variety of methodologies, such as the rule-based approach, decomposition, heuristic search, constraint-based approaches, plan-based approaches, and generic task approach (see Coyne et al. 1990 for a thorough discussion of the different approaches).

Recently, CBR has also been applied to design problems. Notable case-based design systems include JULIA (Hinrichs 1988, 1989, 1992; Kolodner 1987), CYCLOPS (Navinchandra 1988, 1991), KRITIK (Goel 1989, Goel and Chandrasekaran 1989), and CADET (Navinchandra et al. 1991).

The existing systems integrate CBR with other techniques. JULIA illustrates integration with constraint posting and propagation, KRITIK with model-based reasoning, CADET with qualitative reasoning, and CYCLOPS with constraint-based and multiobjective optimization techniques. It therefore appears that CBR needs to be complemented by other methods for solving design problems. In KRITIK, for example, while CBR is used to propose solutions, model-based reasoning is used to verify those solutions, to point out where adaptation is needed, and to suggest adaptations.

A variety of techniques have been employed for organizing, indexing, and retrieving design cases. KRI-TIK's organization of cases is flat; the cases are indexed by their functional specifications. Retrieval is based on a qualitative match between the functional specifications of the stored cases and those of the stored design. The organization of cases in CYCLOPS is also flat; the cases are indexed by the problem features. Rather than matching on common attributes, CYCLOPS uses common causal relationships among attributes to retrieve similar cases. In CADET, for organizing cases, directed acyclic graphs representing behaviors of devices are normalized into a relational database. Because there does not usually exist a direct, one-to-one correspondence between the desired behavior of a device and the individual component behaviors, relevant cases might not be retrieved by using behavioral features. CADET, therefore, employs behavior-preserving index transformation techniques to transform an abstract description of the desired behavior of the device into a description, via which relevant components can be retrieved. The index transformation techniques are based on qualitative reasoning about physical devices. In JULIA frames are used to structure the cases. The cases are organized as redundant discrimination nets and heuristic rules are used to find partially-matching cases as the network is traversed (Hinrichs 1992).

Large design problems cannot be usually solved by retrieving and adapting a single case. JULIA and CA-DET merge pieces of old cases to generate a solution. In JULIA, problems are decomposed into component parts, each of which is solved separately by retrieving and combining snippets of old cases. However, if a single case is available to solve the problem, JULIA prefers using the composite case to combining different snippets. When a problem is decomposed, the components could interact strongly with one another. In JULIA, such interactions are communicated by propagating constraints. JULIA also illustrates the use of CBR to achieve goals at any level of abstraction. Using composite cases to satisfy higher-level goals expedites problem solving.

When components interact, conflicts could arise as the solution is being completed. To reconcile such conflicts, JULIA tries to adapt the solution. If it fails, it attempts to adapt the problem specification by minimally relaxing some of the constraints. CYCLOPS also explores alternatives by relaxing criteria, and by using past design cases to identify additional criteria. The PO-A\* algorithm employed by CYCLOPS allows it to search for alternatives and select an optimal solution based on the criteria. For selecting from among retrieved cases, the other systems also use criteria such as ease of adaptability (KRITIK), and cost, weight, and ease of synthesis (CADET).

Different types of case adaptation are possible. JULIA can make substitutions in its ongoing solution, or it can modify the structure of its ongoing solution. KRITIK uses case-specific models to guide the adaptation process. CYCLOPS, in contrast to JULIA and KRITIK, employs CBR for adaptation. Instead of matching on common attributes, common causal relationships among attributes are used to find similar cases, identify problems, and suggest solutions to the problems. CADET avoids adaptation by synthesizing only those case snippets that are directly relevant to the given goal.

The emphasis of the systems discussed above is on solving design problems, rather than on providing the type of interactive assistance suggested by Kolodner (1991). A system that provides design assistance is more likely to be adopted and relied upon than one which attempts to function in a stand-alone fashion. Kolodner's proposal for case-based decision aiding is especially relevant from a DSS perspective, because it emphasizes the need for sharing responsibilities. Kolodner's ideas complement those of DSS researchers, who aim to support the hitherto unstructurable part of decision making by employing general problem-solving abilities such as CBR (Konsynski et al. 1992, Sprague et al. 1992). As Alter (1994, p. 12) points out, "the potential benefit of a proposed DSS is often strongly related to the extent to which it will provide additional structure or exploit whatever structure already exists." Also, augmenting the decision maker's memory with more (and better) cases would potentially result in more alternatives, better decisions, better use of the data resource, cost and time savings, and new insights—all recognized as benefits of a DSS (Keen 1989).

## 3. A Case-Based Model

The engineering firm we studied specializes in the design, supply, and installation of complete rolling mill facilities for the worldwide ferrous and nonferrous producers market. We worked closely with personnel from the firm's Process/Application Engineering department, which is responsible for the development of mill designs for unique customer requirements. Figure 1 depicts the design process, which begins with the customer's specification of the product requirements and ends with the generation of a design proposal.

We conducted interviews, spread over several sessions, with three experts involved in mechanical design and product costing. Each session lasted from one hour to three hours. The interviews were taped and later transcribed. The first two experts participated during the preliminary stage of development of the conceptual model. Identifying and conceptualizing the domain problem helped us to define an initial structure for the model, along with the relevant underlying processes. Additional domain knowledge was acquired from the third expert to fill in gaps in our knowledge and to implement the conceptual model as a computer system.

Figure 1 The Design Process  
![](/api/attachments/R6QPVHGB/fulltext/images/07edbad3b67fefba3c29933635b930924a48695a166c1bcfab09afb86f782ec0.jpg)

## 3.1. Analysis of the Design Process

Based on our analysis of the interview and protocol data, we formalized a set of principles that appear to characterize the design process. The principles under task decomposition and constraint posting describe how experts reduce the complexity of a task and maintain correctness of the design. The principles under case-based reasoning describe the process through which experts use past cases to generate new solutions. The principles under multicriteria selection identify several criteria that experts consider in selecting a solution.

3.1.1. Task Decomposition. To deal with complexity, we observed the experts decompose a design task into smaller subtasks, each of which requires significantly less resources than the original task. For example, they decompose the task of mill design into subtasks of mill stand design, tables design, auxiliary equipment design, and descale equipment design (see Figure 2). If any of the subtasks themselves are sufficiently complex, they are further decomposed into smaller subtasks. The process continues until the experts feel comfortable in dealing with the complexity of the subtasks. Based on such behavior, which appeared repeatedly in the interview and protocol data, we extracted:

PRINCIPLE 1A. Designers decompose a complex task into smaller subtasks.

PRINCIPLE 1B. Designers stop decomposing a subtask when a solution is readily available, or when the subtask involves designing a primitive object.

Principles 1A and 1B are related to task decomposition. Principle 1A implies that the model should have a task decomposition module. Principle 1B stresses the need for computational efficiency in the design search space. If the designer finds a design case or snippet with which he is satisfied, he would be reluctant to expend further resources in searching for better designs. That is, if, with minimum decomposition, he could retrieve a past design that is promising, he would be willing to terminate the search for additional solutions through decomposition. The model should also incorporate such a search minimization strategy.

3.1.2. Constraint Posting. The design task for a given object entails specifying the design parameters for that object such that it delivers all the desired functions.

Figure 2 Design Hierarchy  
![](/api/attachments/R6QPVHGB/fulltext/images/ac777f172dd46e0b5326eb2082788c60db5bc53c38b314000744fd0cae772f3e.jpg)

The functions impose a set of constraints on the design parameters. With task decomposition, a design is broken down into subdesigns, i.e., designs for each of the component objects. As part of the decomposition, the initial set of constraints is decomposed into constraints on each of the subdesigns, and design parameters are anchored to values. Anchoring in one part of the design necessitates that assignments of values be made in other parts of the design, too. Otherwise, though the individual subdesigns may be locally consistent, they may not be globally consistent, which occurs when the subdesigns cannot be combined together to form a feasible design. Global inconsistency arises because the subdesigns are not completely independent of one another—they are loosely coupled and may interact with one another in harmful ways. Subsystems are loosely coupled when the interactions between them are weak but not negligible.

To ensure global consistency, design experts formulate constraints on design parameters and propagate their effects on other parts of the design. Also, before anchoring parameters in a subdesign to values, the design experts verify whether anchoring would violate global consistency. Such behavior in dealing with constraints is similar to the constraint posting approach identified by Stefik (1981). The constraint posting approach views systems as aggregates of loosely coupled subsystems and models the design of such systems in terms of operations on constraints. The interactions between subsystems are handled through constraints.

The constraint posting approach is comprised of three operations: constraint formulation, constraint propagation, and constraint satisfaction. Constraint formulation is the process of adding new constraints as commitments in the design process. Constraint propagation provides a communication mechanism between different subsystems that are being designed—new constraints are created from old constraints as the design is refined. It adopts a least-commitment strategy of deferring decisions as long as possible. Constraint satisfaction is the operation of searching for objects that satisfy the constraints. Based on the use of constraint posting by the experts, we formulated the following principles:

PRINCIPLE 2A. Designers formulate constraints on a given subdesign to define a search space of feasible solutions.

PRINCIPLE 2B. Based on constraints formulated and commitments made in a given subdesign, designers propagate constraints to other subdesigns as a means to enforce global consistency.

PRINCIPLE 2C. For a given subdesign, designers identify a set of feasible solutions that satisfy all constraints imposed on that subdesign.

Principles 2A, 2B, and 2C stress the need for a module for managing constraints. Principle 2A implies the need for a mechanism to formulate constraints from a set of functions at any stage in the design process. Principle 2B points to the need for a mechanism to propagate constraints between different interacting subdesigns. Without such a mechanism, it would not be possible to enforce global consistency. Principle 2C implies that the model should be able to generate feasible designs from a knowledge of the constraints. The module for managing constraints, therefore, should be able to support the three operations mentioned above.

3.1.3. Case-Based Reasoning. The design environment we studied is endowed with a rich history of past design solutions, which are available in the form of proposals and contracts. Instead of starting from scratch, design experts frequently resort to those solutions (cases) to formulate new solutions. Reasoning from past cases helps them generate new solutions quickly, because it reduces the effort required to search a large space of designs. CBR is, therefore, different from other knowledge-based design approaches, such as heuristic search and the rule-based approach, which do not take advantage of past design episodes for solving new design tasks.

Human designers also frequently use snippets from different cases, and compose a design solution by combining those snippets. A snippet, being part of a case, contains design values for only that part. If any of the cases or snippets do not satisfy the target specifications, then the designer performs adaptations to make them feasible.

The use of CBR by the experts was evident throughout the knowledge acquisition process. Functions were used as indexes to retrieve cases. Based on such observations, we extracted:

PRINCIPLE 3A. Designers retrieve similar design cases, which are indexed on functions, to establish a starting point for the current design task.

PRINCIPLF 3B. For a given subdesign within a particular task, designers retrieve snippets of cases that may be different from the ones used for other subdesigns within the same task.

PRINCIPLE 3C. If some of the retrieved cases (snippets) for a design (subdesign) are not feasible, designers adapt them to make them feasible.

PRINCIPLE 3D. Designers compose from feasible snippets, which may come from different cases, to generate a set of candidate designs. If composition renders a design infeasible, designers try to restore feasibility by performing further adaptation.

Principles 3A through 3D strongly imply the need for a CBR module within the model. Principles 3A and 3B entail that the module be able to support retrieval of cases as well as snippets. Principle 3C requires that the module support case and snippet adaptation. Principle 3D requires that the model support case composition along with any necessary adaptation.

3.1.4. Multicriteria Selection. We observed that design experts, while selecting from a set of feasible solutions, use multiple criteria in making the selection. Those criteria can be treated as objectives they wish to optimize. An important objective, for example, is to minimize the adaptation that needs to be done to a design case so that it satisfies the specifications of the current task, which is equivalent to selecting the most similar design case.

Figure 3 Work Roll Design  
![](/api/attachments/R6QPVHGB/fulltext/images/b0c41c4540eac4c6c59d8c5b0dff9f722531966000b3e10654772e5dda8d4577.jpg)

OBJECTIVE 1. In selecting among alternative design cases (snippets), designers try to select the one that requires minimum adaptation (adaptation objective).

Another important objective is to minimize the cost.

OBJECTIVE 2. In selecting among alternative design cases (snippets), designers try to select the one with the minimum cost (cost objective).

We also observed the designers' tendency to refer to more detailed designs when they exist. As stated before, designs are available in two forms: proposals and contracts. Contracts typically include much more detailed information than proposals, because the design decisions were actually carried out, and the results could be used for feedback purposes. It is therefore not surprising that designers tend to rely more on contracts than on proposals when both are available. We formalize such behavior by taking into account the level of detail in a design case (a contract is always more detailed than a proposal).

OBJECTIVE 3. In selecting among alternative design cases (snippets), designers try to select the one having maximum detail (detail objective).

As described before, a design can be generated by reasoning from a single case or from snippets of different cases. A single case comprises a globally consistent set of subdesigns. Because a retrieved case is similar to the current task, there is an implicit expectation that minimal adaptation would be needed for the subdesigns to remain globally consistent. On the other hand, if an attempt is made to combine snippets of different cases, there is a good chance that the subdesigns would not be compatible, implying considerable adaptation work during composition. We observed that the design experts tend to prefer whole cases to case snippets. $^{3}$

OBJECTIVE 4. In selecting among alternative design cases (snippets), designers try to select the one that requires minimum composition (composition objective).

Objectives 1 through 4 imply the need for a module that would support multi-criteria decision making. It should be able to help the human designer focus on a small number of attractive cases, by trying to optimize the objectives of adaptation, cost, detail, and composition simultaneously.

## 3.2. Model Development

In the previous subsection, we stressed the need for developing the following modules: (1) a task decomposer, (2) a constraint manager, (3) a case-based reasoner, and (4) a multicriteria selector. We now describe the modules.

3.2.1. Task Decomposer. The task decomposer module reduces a given design task into a set of subtasks. The subtasks, in turn, may be divided into further subtasks. This recursive process continues until either a satisfactory design is found or the task is reduced to designing a primitive component.

The task decomposer uses its representation of the design hierarchy (see Figure 2) to divide a task into its constituent subtasks. Decomposition knowledge, in the form of the design hierarchy, is always available to the task decomposer module. The task decomposer does not directly formulate any constraints or generate functions for subdesigns. Instead, it consults with the constraint manager, which formulates constraints on design parameters, generates functions on subdesigns, and feeds information back to the task decomposer. The task decomposer can then concentrate on reducing the subtasks, one at a time, using the design hierarchy.

3.2.2. Constraint Manager. The constraint manager provides the backbone of the model, by continuously formulating and propagating constraints, and by checking for inconsistencies in partial designs. It supports operations on constraints through a dependency network. The portion of the network used for work roll design is shown in Figure 3.

Design parameters and design constants are enclosed in boxes with single-line borders. Functional specifications are enclosed in boxes with double-line borders. A box with curved edges encloses a function/parameter whose value can be revised dynamically during problem solving. A box with straight edges contains a function/parameter which is either a constant or whose value cannot be modified once it is specified. Dependencies are represented by directed links. The head of a link points toward the dependent function/parameter and the tail is connected to the determinant function/parameter. A conjunctive dependency, in which two or more determinants jointly determine a dependent function/parameter, is represented by drawing an arc between the links connecting the determinants to the dependent function/parameter. Any box that does not have an incoming link contains a function/parameter whose initial value has to be specified by the user. Some of the links are labeled. Three labels are used in the dependency network: approx, min, and max. The labels “min” and “max” are used to establish lower bound and upper bound constraints on dependent functions and parameters. The “approx” label specifies an approximate value for a function or parameter. Any link that does not have a label specifies an exact relationship.

Figure 4 depicts the portion of the network responsible for backup roll and housing design. The function of the backup rolls is to support the separating force developed between the work rolls during rolling. The housings house the work rolls and the backup rolls.

Figure 4 Backup Roll and Housing Design  
![](/api/attachments/R6QPVHGB/fulltext/images/8247a59178d27e79ed4d29009eaad574b215b20ceee0dcbdaf847b1707b9908d.jpg)

Because the separating force is transmitted through the work roll necks to the housing posts, the post area of the housings has to be sufficiently large to support this force. The value of maximum separating force specifies lower bounds for the backup diameter and the post area of the housings. Note that both POST-AREA and MAX-SEP-FORCE can be varied. If, for instance, none of the available housings satisfies the lower bound post area constraint, the constraint could be relaxed to determine if any of the housings could be used.

Relaxation also requires determining whether the new constraint on POST-AREA is consistent with the global design. The dependency network supports such consistency checking by recursively tracing backward to find if any of the determinants can be varied to satisfy the new constraint. If the constraint on POST-AREA has to be relaxed to a new value, MAX-SEP-FORCE has to change. The determinants of MAX-SEP-FORCE are WR-DIA, DRAFT, MAX-SLAB-WI, and K, of which only WR-DIA can be changed (see Figure 3). WR-DIA can be varied within the limits defined by the lower and upper bounds. $^{4}$ Relaxing the constraint on POST-AREA, therefore, implies finding a smaller WR-DIA that satisfies the lower bound constraint previously imposed on it. If such a WR-DIA is found, the constraint on POST-AREA can be relaxed to use an available housing.

Table 1 Case Indexes

<table><tr><td>Design Case/Snippet</td><td>Indexes</td></tr><tr><td>Housing</td><td>Max separating force</td></tr><tr><td>Work Rolls</td><td>Min gauge, Max torque</td></tr><tr><td>Backup Rolls</td><td>Max input width, Max separating force, Crown</td></tr><tr><td>Motor</td><td>Max torque</td></tr><tr><td>Pinions</td><td>Max torque, Base rpm</td></tr></table>

The power of the dependency network is evident in the way in which it formulates different types of constraints, relates functions and constraints, allows constraint relaxation, and maintains global consistency. The constraint manager, which incorporates the network, works in tandem with the case-based reasoner.

3.2.3. Case-Based Reasoner. The case-based reasoner module is responsible for case indexing and retrieval, case adaptation, and case composition.

Case Indexing and Retrieval. Cases are indexed by the functions they were designed to satisfy. Table 1 shows the indexes used for different types of cases. Cases can be indexed by more than one function.

The CBR module emulates the approximate matching techniques of experts by specifying a range of index values for each function. Based on a function value, a range of values is specified to retrieve cases similar with respect to that function.

Table 2 Range of Index Values

<table><tr><td>Function</td><td>Range</td></tr><tr><td>Max Separating Force</td><td>0.7 to 1.5</td></tr><tr><td>Max Torque</td><td>0.6 to 1.7</td></tr><tr><td>Max Horsepower</td><td>0.7 to 1.7</td></tr></table>

The constraint manager determines whether a case is feasible by checking all constraints imposed on the design. If the case is infeasible, then there is a need to check whether it could be adapted and made feasible (adaptation is discussed below); otherwise, it is discarded. The strategy adopted by the case-based reasoner is to retrieve similar cases, and then to check for feasibility and adaptability. Instead of using absolute deviations, percentage deviations (e.g., $\pm30\%$ of the target) are specified to determine the range of index values. The more critical function is, the narrower is its range of index values. Representative ranges are shown in Table 2. Retrieval rules for housings and work rolls are shown in Figure 5.

Case Adaptation. The case-based reasoner retrieves multiple cases, not all of which are even locally feasible. The issue, therefore, is to determine if some of those infeasible cases could be made feasible by adaptation.

There are two sources of adaptation knowledge. The first is the constraint manager, which maintains a dependency network. The dependency network is traced backward to identify possible adaptations. The second is the case-based reasoner, which stores adaptation knowledge in the form of production rules. The adaptation rules measure the deviation of a base (retrieved) case from the target design task and then propose ways to minimize the deviations. Deviations are measured

## Figure 5 Retrieval Rules

If the MAX-SF function is ?sf1 and there is a HOUSINGS case with MAX-SF ?sf2 and (similar-sf? ?sf1 ?sf2)

Then retrieve the HOUSINGS case.

If the MAX-TORQUE function is ?torq1 and there is a WORK-ROLLS case with MAX-TORQUE ?torq2 and (similar-torq? ?torq1 ?torq2)

Then retrieve the WORK-ROLLS case.

Table 3 Adaptation Rules

<table><tr><td>Violating Constraint</td><td>Adaptation Rule</td></tr><tr><td>window depth &gt; specified depth</td><td>If window depth &gt; specified depthThen cut shoe plates and separators down to specified depthbring housings closer togetherreplace shoe-plates and separators</td></tr><tr><td>window depth &lt; specified depth</td><td>If window depth &lt; specified depthThen remove separators and shoe platespull housings apart to specified depthattach new separators and shoe plates</td></tr><tr><td>window height &lt; specified min height</td><td>If window height &lt; specified min heightThen cut down the chucks</td></tr><tr><td>roll face &gt; specified face</td><td>If roll face - specified faceThen cut the rolls down to the specified value</td></tr><tr><td>motor HP ≪ specified min HP</td><td>If motor HP &lt; specified min HPThen couple another motor having the same ratings in series with existing motor</td></tr></table>

relative to the constraints. The case-based reasoner then has to check the adaptation rules to determine whether there is a way to reduce the deviation so that the constraint is satisfied. A representative sample of adaptation rules is shown in Table 3. After application of the adaptation rules, the set of retrieved cases consists of those that were locally feasible when retrieved, as well as those that could be adapted to be locally feasible.

Figure 6 Constraint Posting Stage  
![](/api/attachments/R6QPVHGB/fulltext/images/05285febc72f28a960718f095ec639c898328f72b16ff09315186e8850033fab.jpg)

Case Composition. More complex adaptation occurs during case composition. If a design is composed of snippets from different cases, even if the snippets are locally consistent, there is no guarantee that there will not be any harmful interactions when the snippets are combined. Providing adaptation cues is critical to the designer. The constraint manager not only helps in identifying the set of violating constraints, but also suggests adaptations, by changing the values of the determinants. Because such adaptations are done only at the time of composition, they are called dynamic adaptations.

3.2.4. Multicriteria Selector. The multicriteria selector (MCS) module identifies a pareto-optimal set of designs. $^{5}$ The process of selecting pareto-optimal designs is a nontrivial one, because a design is composed from different snippets, each of which could satisfy the objectives in different ways. We need to assign an aggregate score to a candidate design based on each ob-

Figure 7 Case-Based Reasoning Stage  
![](/api/attachments/R6QPVHGB/fulltext/images/a66359540853ae3fa82813e0aa8937a35235b8a13575f96c4f02444b15eec8de.jpg)

INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 3, September 1996

jective. This is done by scoring each primitive snippet with respect to a given objective, and combining those individual scores to generate an aggregate score.

Adaptation is scored in the following way. An adaptation can be done using an adaptation rule or by recursively tracing backward through the dependency network. Whichever method is followed, certain design parameters are adjusted. The model needs to know how easy or difficult it is to adapt each of the variable design parameters. It stores that knowledge along with each parameter; a parameter is weighted on a 1 to 3 scale depending on how easy or difficult it is to adjust the parameter. A weight of 1 indicates minimum difficulty while a weight of 3 denotes maximum difficulty. For each parameter adjustment, the model also takes into account the extent of the adjustment, which is accomplished by assigning a score to each adaptation. The model consults a lookup table which contains discrete scores, on a 0 to 5 scale, for different degrees of adaptation.

The score for the cost objective is the sum of the costs of all the equipment specified in the design. The detail objective uses a binary score of 0 or 1 for the primitive components. If the component references a contract, a score of 1 is assigned; if it references a proposal, a score of 0 is assigned. The model adds the scores to come up with an aggregate score for the detail objective. The composition objective favors minimizing the number of compositions from different cases, that is, the model prefers a more composite design to a less composite one.

## 3.3. Algorithm

The model executes in two stages: a constraint posting stage and a case-based reasoning stage. In the constraint posting stage, the constraint manager and the task decomposer work together in a top-down fashion to post relevant constraints on the design. The output from this stage is an instance of the dependency network, which bounds the search space for the given design by imposing constraints on design parameters. The output (a set of functions and constraints) becomes the input to the case-based reasoning stage. The case-based reasoner works in conjunction with the constraint manager and the multicriteria selector to generate a set of pareto-optimal designs.

3.3.1. Constraint Posting Stage. Figure 6 illustrates the steps executed by the model in the constraint posting stage. The input to the model is a set of functions specified by the designer. Based on those functions, a set of constraints is formulated by the constraint manager. Only constraints specific to the task are formulated. Formulation of other constraints, which are implied but not directly relevant to the task at hand, are deferred to a later stage.

Figure 8 System Architecture  
![](/api/attachments/R6QPVHGB/fulltext/images/bb50db21420d2fca92c40b68a5d9e2d2eba4279fcfe6b9f2ca62821ad74407fb.jpg)

The next step is to check whether the task is primitive. If not, it is divided into its component subtasks by the task decomposer. Decomposition leads to propagation of constraints related to the subtasks. Propagation could also result in derivation of additional functions for the subtask. Also, the designer can revise existing functions or specify additional ones at any stage.

The process described above iterates until there is no potential decomposition remaining, that is, all the subtasks are primitive. The flow of control is top-down and breadth-first. All subtasks at a given level are considered before going down to the next lower level. The output from the constraint posting stage is an instance of the dependency network. The network is instantiated with values for functions and constraints.

3.3.2. Case-Based Reasoning Stage. The output from the constraint posting stage provides the input to the case-based reasoning stage. The steps executed in the case-based reasoning stage are illustrated in Figure 7.

In general, more than one case is retrieved. Each such case is checked for feasibility. Feasibility is determined by checking whether all design parameters of the case—which include those in all of its snippets—satisfy the constraints in the dependency network instance. Because a retrieved case further instantiates and revises the dependency network, it maintains its own version of the dependency network. If a case is found to be infeasible, it is not discarded immediately. Rather, the case-based reasoner uses its adaptation knowledge to see whether the case can be adapted to make it feasible. Adaptation knowledge, as discussed in §3.2.3, may come from either the dependency network instance or from adaptation rules. If the case is adaptable, it is adapted and added to the set of feasible cases $C_{f}$ . If there does not exist any known way in which a case could be adapted, by using the adaptation rules or the dependency network, then the case is discarded. Each retrieved case is checked for feasibility in this fashion.

Table 4 Feasible Mill Stand Solutions

<table><tr><td>Solution (HSG-WR-BU-MTR-PIN) $^{12}$ </td><td>Adaptation Score</td><td>Cost Score $^3$ </td><td>Detail Score</td><td>Composition Score</td></tr><tr><td>1. C700-C700-C700-C800-C800</td><td>33</td><td>12</td><td>5</td><td>2</td></tr><tr><td>2. C700-C700-C1950-C800-C800</td><td>37</td><td>10</td><td>5</td><td>3</td></tr><tr><td>3. C700-C800-C700-C800-C800</td><td>39</td><td>13</td><td>5</td><td>2</td></tr><tr><td>4. C700-C800-C1950-C800-C800</td><td>43</td><td>11</td><td>5</td><td>3</td></tr><tr><td>5. C800-C700-C700-C800-C800*</td><td>29</td><td>5</td><td>5</td><td>2</td></tr><tr><td>6. C800-C700-C1950-C800-C800*</td><td>32</td><td>3</td><td>5</td><td>3</td></tr><tr><td>7. C800-C800-C1950-C800-C800*</td><td>38</td><td>4</td><td>5</td><td>2</td></tr><tr><td>8. C1950-C700-C700-C800-C800</td><td>35</td><td>8</td><td>5</td><td>3</td></tr><tr><td>9. C1950-C700-C1950-C800-C800</td><td>39</td><td>6</td><td>5</td><td>3</td></tr><tr><td>10. C1950-C800-C700-C800-C800</td><td>41</td><td>9</td><td>5</td><td>3</td></tr><tr><td>11. C1950-C800-C1950-C800-C800</td><td>45</td><td>7</td><td>5</td><td>2</td></tr><tr><td>12. P7509-C700-C700-C800-C800</td><td>25</td><td>5</td><td>4</td><td>3</td></tr><tr><td>13 P7509-C700-C1950-C800-C800</td><td>27</td><td>3</td><td>4</td><td>4</td></tr><tr><td>14. P7509-C800-C1950-C800-C800</td><td>33</td><td>4</td><td>4</td><td>3</td></tr><tr><td>15 C1700-C700-C700-C800-C800*</td><td>24</td><td>5</td><td>5</td><td>3</td></tr><tr><td>16. C1700-C700-C1950-C800-C800*</td><td>27</td><td>3</td><td>5</td><td>4</td></tr><tr><td>17. C1700-C800-C1950-C800-C800</td><td>33</td><td>4</td><td>5</td><td>3</td></tr><tr><td>18. P8009B-C700-C1950-C800-C800*</td><td>32</td><td>1</td><td>4</td><td>4</td></tr><tr><td>19. P8009B-C800-C1950-C800-C800*</td><td>38</td><td>2</td><td>4</td><td>3</td></tr></table>

\* Pareto optimal (Objectives: 1. Minimize adaptation 2 Minimize cost 3. Maximize detail 4. Minimize composition)  
$^{1}$ A solution consists of housings (HSG), work rolls (WR), backup rolls (BU), motor (MTR), and pinions (PIN) snippets.  
$^{2}$ The snippets that were finally adapted are marked in bold  
$^{3}$ To maintain confidentiality, the cost scores were assigned on an ordinal scale, with 1 representing the lowest cost.

If the user is then satisfied with the existing set of cases, he could decide not to search for additional cases, terminating the search process. In general, the feasible set includes snippets, which must be composed. Hence it is necessary to compose designs from those snippets. Composition from snippets is discussed below. If the user decides not to terminate the search for additional cases, the model selects all non-primitive objects and decomposes them in a breadth-first order. The process iterates until all objects are primitive, or until the user explicitly stops the search process. When terminated, the model includes sets of feasible cases for different objects, both primitive and composite.

The case-based reasoner composes all possible designs from such cases; those designs constitute the set D. Not all designs $d_{i}$ in D may be feasible, because the components may interact. Dysfunctional interactions are detected by the dependency network version maintained for each $d_{i}$ by the constraint manager. If a composition $d_{i}$ is infeasible, then it is the responsibility of the constraint manager and the case-based reasoner to determine whether it could be adapted to a feasible one. If such a possibility exists, then $d_{i}$ is adapted and added to the set of all feasible designs $D^{f}$ . If not, it is discarded.

The multicriteria selector applies all the objectives in ways described earlier in §3.2.4, and outputs the pareto-optimal set of designs $D''$ to the user. Each design in $D''$ is a complete structural specification. That is, it provides values for all the design parameters, along with any adaptations that may be necessary. It also specifies the set of equipment, which may be used for the current design task.

## 4. System Implementation and Evaluation

The model was operationalized as a computer-based design system called IDEA (Intelligent Design Assistant). $^{6}$ IDEA is implemented using GoldWorks II $^{TM}$ , a Golden Common LISP $^{TM}$ -based expert system development environment, and runs on a 486 PC. $^{7}$ GoldWorks supports multiple knowledge representation schemes such as rules, frames, and objects, and various control mechanisms such as forward chaining, backward chaining, and goal-directed forward chaining.

Figure 8 depicts IDEA's architecture. User interactions are through the interface. The input is a set of functional specifications from the user and the final output is a set of pareto-optimal solutions, along with any necessary adaptations. Other intermediate interactions also take place through the interface. Based on the user's specifications, the task decomposer and the constraint manager work together to generate a dependency network, which is then used by the CBR module. The CBR module performs case retrieval, adaptation, and composition, and outputs a set of feasible cases, along with the required adaptations, to the multicriteria selector. $^{8}$

The multicriteria selector identifies a pareto-optimal set of cases and outputs those cases to the user through the interface. The controller is responsible for exercising central control among the different modules. The architectural components are described in detail in Sinha (1993).

Table 4 shows the final set of feasible mill stand solutions generated by IDEA on an actual design task. $^{9}$ The “C” and “P” prefixes of the snippets constituting a solution represent contracts and proposals, respectively. Out of the nineteen feasible solutions, only seven are pareto optimal; they are solutions 5, 6, 7, 15, 16, 18, and 19. These solutions, along with the recommended adaptations, were output to the user. $^{10}$ Note that every solution required adaptation of at least one of its snippets. The recommended adaptations for solution #5, for example, include increasing the window width by 5.5" and cutting the face of each post down by 2.75". As an example of conflicting objectives, notice that while solution #15 is better than solution #16 in terms of adaptation and composition, solution #16 is better cost-wise.

IDEA's performance was evaluated using a multiattribute utility technology (MAUT) approach (see Adelman 1992). The method is designed to obtain the utility of an item that is evaluated on more than one criterion or attribute. A MAUT model combines the utility or satisfaction derived from the individual attributes into a single measure of overall utility. Because IDEA has numerous attributes of potential value to the human designer, MAUT represents an appropriate evaluation method.

To apply MAUT, a value hierarchy was created (see Figure 9), with the global criterion, “overall utility (or value) of the system,” at the top. The overall utility was decomposed into the following major criteria: case-based reasoning, task performance, management of the data resource, changes in the decision process, and changes in the user's concept. These categories were further decomposed to obtain the bottom-level attributes, which are directly measurable. The evaluation task was to assign scores to the bottom-level attributes. MAUT depends on the evaluator's ability to directly measure the ratings of each bottom-level attribute. More complex evaluations are often done using indirect tools, such as AHP (Bard 1992). IDEA supports design for artifacts which are directly comparable in physical and engineering terms, so that a human's direct responses to value questions should be sufficiently reliable for us to assess IDEA's efficiency using a technique such as MAUT.

<table><tr><td>.135</td><td>.06</td><td>.06</td><td>.045</td><td>.008</td><td>.008</td><td>.008</td><td>.02</td><td>.008</td><td>.02</td><td>.02</td><td>.008</td><td>06</td><td>.06</td><td>.08</td><td>.099</td><td>201</td><td>.067</td><td>.033</td></tr><tr><td>Case retrieval</td><td>Case composition</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>Case adaptation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Case rejection</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Ease of use</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Transparency</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Response time</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Expert judgment</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Flexibility</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Automation of manual calculations</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Quality of solutions</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Effectiveness of framework</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Expediting access to unavailable info</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Better utilization of proposals &amp; contracts</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Ability to draw inferences</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Range of alternatives</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Ranking of alternatives</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Development of new insights</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Better understanding</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Figure 9 Multiattribute Utility Analysis Hierarchy  
![](/api/attachments/R6QPVHGB/fulltext/images/f5d2c535cbe43eb6e7fc2cbdc73194afe2550a6cf01fa09534af554aa09c6c99.jpg)

A common "utility" scale was used to compare scores on one attribute with scores on another. Utility functions, which were linearly increasing or decreasing in form, were used to translate the attribute scores into utility scores. An utility score on an attribute measures the system's worth or value to the user with respect to that attribute. The utility scale ranged from 0 to 10. A score of 5 means that the system meets the performance expectations on that attribute. A score of 0 indicates that the system fails the performance expectations. A score of 10 means that the system not only fully meets the performance expectations, but it greatly exceeds them.

The individual measures of effectiveness, as well as the broader effectiveness categories, were weighted by the expert to reflect their relative importance. The relative weights are shown along the branches in Figure 9; the weights at each node sum to 1. Within the case-based reasoning category, for example, case retrieval has a weight of 0.45 and case rejection has a weight of 0.15, implying that retrieval is three times more important than rejection. Similarly, case-based reasoning, with a weight of 0.3, is three times more important than changes in the user's concept, which has a weight of 0.1. The weights on the bottom-level attributes represent their cumulative weights, which were calculated by multiplying the relative weights from the top to the bottom of the hierarchy. As can be seen, ranking of alternatives and case retrieval were considered to be the two most important attributes, accounting for roughly one-third of the importance.

A questionnaire was prepared to obtain the expert's opinion about IDEA with respect to the measures of effectiveness under the case-based reasoning category. Two items from the questionnaire, one for retrieval and the other for adaptation, are presented below:

How would you rate the HOUSINGS case retrieved for the given task?

<table><tr><td colspan="4">Totally unacceptable</td><td colspan="4">Moderately acceptable</td><td colspan="2">Highly acceptable</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr></table>

The adaptation on the window height was appropriate.

<table><tr><td colspan="5">Very Strongly Disagree</td><td colspan="4">Neither Disagreenor Agree</td><td colspan="2">Very Strongly Agree</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr></table>

The questions required the expert to respond on an eleven-point Likert scale from zero (totally unacceptable or very strongly disagree) to ten (highly acceptable or very strongly agree), with five being “moderately acceptable” or “neither disagree nor agree.” The expert evaluated a total of 12 case retrievals, 16 case rejections, 28 case adaptations, and 19 case compositions. The average utility score obtained for each of these measures is reported in the second column of Table 5.

Another questionnaire, containing 46 questions, was completed by the expert to obtain scores on the remaining effectiveness measures. Most of the measures—such as ease of use, transparency, response time, automation of manual calculations, expediting access to unavailable information, range of alternatives, and development of new insights—have been identified in the DSS literature (see, for example, Alter 1994, Keen 1989). Each attribute was measured by two or more questions in order to achieve greater confidence in the scores. Also, half the questions for each attribute were presented in each half of the questionnaire to minimize any effects of question ordering on the scores. Two questions for evaluating whether IDEA exhibits expert judgment capabilities are presented below:

In my opinion, IDEA's solutions are comparable to those generated by an expert

<table><tr><td colspan="4">Very Strongly Disagree</td><td colspan="5">Neither Disagreenor Agree</td><td colspan="2">Very Strongly Agree</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr></table>

IDEA's solutions are much better than those produced by an inexperienced designer

<table><tr><td colspan="4">Very Strongly Disagree</td><td colspan="5">Neither Disagreenor Agree</td><td colspan="2">Very Strongly Agree</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr></table>

The overall utility of IDEA was calculated by using the following formula:

$$
U = w _ {1} u (x _ {1}) + \dots + w _ {j} u (x _ {j}), \quad \text { where }
$$

$U$ is the overall utility;

there are $j$ attributes;

$w_{j}$ is the cumulative relative weight on attribute $j$ ; and $u(x_{j})$ is the utility scale value on attribute $j$ .

IDEA's overall utility was 7.467. To test whether or not IDEA's utility exceeds the user's expectations, we tested the null hypothesis that it did not ( $H_0$ : $\mu \leq 5$ ) against the alternative hypothesis that it did ( $\mu > 5$ ). Using the sample of utility ratings on the individual questions ( $n = 121$ ), a $t$ -test of those hypotheses was conducted. The $p$ -value for the $t$ -test is less than 0.01, strongly supporting the contention that, overall, IDEA exceeded the user's expectations. The mean ( $\bar{x}$ ) and standard deviation ( $s$ ) of the sample are 7.81 and 1.94, respectively. The results of the $t$ -test are reported in the last column of Table 5.

IDEA's utility scores on the individual measures of effectiveness are reported in the second column of Table

Table 5 Utility Scores

<table><tr><td>Measure of Effectiveness</td><td>Utility Score</td><td>Results of t-test† for Each Category</td><td>Contribution Toward Overall Utility</td><td>Overall Utility (t-test† Results)</td></tr><tr><td>Case retrieval</td><td>6.08</td><td></td><td></td><td></td></tr><tr><td>Case composition</td><td>6 11</td><td> $\bar{x} = 7.52, s = 172$ </td><td>Case-based reasoning</td><td></td></tr><tr><td>Case adaptation</td><td>7 75</td><td>n = 75, t = 12 69</td><td>2 097</td><td></td></tr><tr><td>Case rejection</td><td>9.88</td><td>p = 0 000</td><td></td><td></td></tr><tr><td>Ease of use</td><td>6.50</td><td></td><td></td><td></td></tr><tr><td>Transparency</td><td>10.00</td><td></td><td></td><td></td></tr><tr><td>Response time</td><td>8.50</td><td></td><td></td><td></td></tr><tr><td>Expert judgment</td><td>7.75</td><td></td><td></td><td></td></tr><tr><td>Flexibility</td><td>7 00</td><td> $\bar{x} = 846, s = 1.92$ </td><td>Task performance</td><td></td></tr><tr><td>Automation of manual calculations</td><td>8.75</td><td>n = 26, t = 9 18</td><td>0.816</td><td></td></tr><tr><td>Quality of solutions</td><td>7 50</td><td>p = 0 000</td><td></td><td></td></tr><tr><td>Effectiveness of framework</td><td>10.00</td><td></td><td></td><td>7.467</td></tr><tr><td>Expediting access to unavailable information</td><td>10.00</td><td></td><td></td><td> $\bar{x} = 781$ </td></tr><tr><td>Better utilization of proposals and contracts</td><td>9.00</td><td> $\bar{x} = 913, s = 1.81$ </td><td>Management of the data source</td><td>s = 1 94</td></tr><tr><td>Ability to draw inferences from presentation</td><td>7 50</td><td>n = 8, t = 6.45</td><td>1 740</td><td>n = 121</td></tr><tr><td></td><td></td><td>p = 0 000</td><td></td><td>t = 15.95</td></tr><tr><td></td><td></td><td></td><td></td><td>p = 0.000</td></tr><tr><td>Range of alternatives</td><td>9 50</td><td> $\bar{x} = 775, s = 328$ </td><td>Changes in the decision process</td><td></td></tr><tr><td>Ranking of alternatives</td><td>6 00</td><td>n = 8, t = 2 37</td><td>2 147</td><td></td></tr><tr><td></td><td></td><td>p = 0 025</td><td></td><td></td></tr><tr><td>Development of new insights</td><td>7.00</td><td> $\bar{x} = 6.50, s = 100$ </td><td>Changes in the user&#x27;s concept</td><td></td></tr><tr><td>Better understanding</td><td>6 00</td><td>n = 4, t = 3 00</td><td>0.667</td><td></td></tr><tr><td></td><td></td><td>p = 0 029</td><td></td><td></td></tr></table>

† IDEA exceeds user's expectations.

5. To further test IDEA's performance on each of the five categories, analogous $t$ -tests were conducted separately; the results are reported in the third column. IDEA significantly exceeded the user's expectations on all the five categories ( $p < 0.01$ for case-based reasoning, task performance, and management of the data resource; $p < 0.05$ for changes in the decision process and changes in the user's concept). The fourth column reports the contribution of each category toward the overall utility score.

In addition to the evaluation by an expert, we assessed IDEA's performance on several relevant quantitative attributes. Size of the solution space is one such performance measure for an AI method. As Buchanan (1988, p. 242) points out, “The power of a method is somehow related to its ability to find correct (or acceptable) solutions to large problems, where the size of the problem is the number of possible solutions in the search space.” Given that a solution is a combination of the solutions for five different mill objects, each of which has 14 snippets, IDEA’s solution space size is $14^{5}$ —a space of half a million. In this large space, IDEA retrieved a total of 30 snippets for the five primitive objects, performed 25 adaptations, and generated 145 compositions, all in a space of a few minutes. Due to cognitive limitations, it is unlikely that a human designer could exhaustively or implicitly perform so many retrievals, adaptations, and compositions. By allowing the user to explore all possible scenarios in a short time, IDEA provides valuable design assistance.

Another performance measure suggested by Buchanan (1988) is the way the method organizes its search of the solution space. IDEA first reduced the maximum possible of $14^{5}$ combinations to 1008 (seven housings, two work rolls, three backup rolls, four motors, and six pinions)—a reduction of $99.8\%$ —by pruning off locally infeasible solutions. Out of those 1008 solutions, IDEA actually generated 95 mill stand solutions (a reduction of $90.6\%$ ), of which 76 were discarded because of harmful interactions, reducing the number of feasible solutions to 19 (a further reduction of $80\%$ ). These figures demonstrate IDEA's power in reasoning effectively and efficiently in a large combinatorial space.

A third quantitative measure used to assess IDEA's effectiveness is the hit rate of the cases retrieved. Among the 30 primitive snippets it retrieved, 12 were part of the final feasible set, implying an impressive hit rate of $40\%$ . The hit rate is even higher $(54.5\%)$ if we take into account that eight of those snippets were discarded immediately after retrieval.

At the end of the evaluation session, the expert cited the following as major contributions of IDEA: case reference, range of alternatives, adaptation to available equipment, guide to degree of adaptation, comprehensive view, and (early) exclusion of bad choices. For future improvements, he suggested the following: incorporating additional criteria and heuristics, showing the relation of solutions to cost, allowing single screen data entry, adding lookup tables, and giving it the ability to handle ill-specified tasks. We believe that all of them, except for the last one, are implementation-level limitations that could easily be overcome in future.

We conjecture that the current size of the case memory is responsible for the relatively low utility scores on case retrieval and case composition (see Table 5). The addition of a large number of cases should improve those scores. The “ease of use” score might improve with a friendlier user interface. At present, IDEA provides a ranking of the solutions with respect to each individual criterion, and identifies the pareto-optimal solutions, but does not provide an overall rank. Expressing all the objectives in terms of cost and combining them into a linear cost optimization function to yield an overall rank is certainly appealing, but is impractical because the criteria, given the current state of our knowledge, are incommensurable. The third expert also provides an account of why combining the criteria would not be of much help:

I'd like them to be separate criteria because that's the way they think about it and that allows them on a lot of times to make discriminating judgments. As far as the company is concerned, we always want to see how it's ranked with respect to the different criteria. They don't want to see a single answer because the first thing I'll have in my mind is why? You can say that this is the best choice, all things considered, but in our world over there, there's never a best choice, there's always a forced choice. And I pick one set of choices, our cost guy picks another set of choices, people who think too much about their inventory and equipment would pick another choice. A lot of our discussion revolves around what type of choice is a better choice. Now, in effect, you are saying, well, ok, if you summarize into one criterion, you make that decision, but that's not the way it happens in the real world

To compare IDEA's performance with that of a human designer, we further evaluated IDEA on five real design tasks. The expert was asked to compare the design solutions generated using IDEA with those generated by experienced human designers not using IDEA on three measures: the time taken to generate the solutions, the number of solutions generated, and the quality of the solutions. $^{11}$ A questionnaire was designed to measure the expert's relative assessment of performance. Performance on time and number of solutions was assessed separately for each of the five tasks through the following questions:

Please rate the time taken to generate the solutions using IDEA

<table><tr><td colspan="4">Much more than w/o IDEA</td><td colspan="4">About the same as w/o IDEA</td><td colspan="3">Much less than w/o IDEA</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr></table>

$^{11}$ For two of the design tasks, IDEA did not generate any composite mill stand solutions because it could not produce any feasible drive solutions. However, it generated composite solutions by combining housings, work rolls, and backup rolls; those solutions were used for performance evaluation

INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 3, September 1996

Table 6 Performance Results

<table><tr><td></td><td>Task #1</td><td>Task #2</td><td>Task #3</td><td>Task #4</td><td>Task #5</td><td>Results of t-test†</td></tr><tr><td rowspan="2">Total # of Solutions Generated (Rating)</td><td>57</td><td>8*</td><td>55</td><td>28</td><td>153*</td><td rowspan="2"> $\bar{x} = 9.60, s = 0.89$  $n = 5, t = 11.50$  $p = 0.000$ </td></tr><tr><td>10</td><td>8</td><td>10</td><td>10</td><td>10</td></tr><tr><td rowspan="2">Time Taken to Generate Solutions (Rating)</td><td>3.50 min</td><td>2.08 min</td><td>2.00 min</td><td>2.08 min</td><td>3.25 min</td><td rowspan="2"> $\bar{x} = 10.00$ </td></tr><tr><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td></tr><tr><td>Average Quality Rating of Solutions</td><td>6.00</td><td>7 17</td><td>9 33</td><td>9.00</td><td>7 17</td><td> $\bar{x} = 7.73, s = 2.10$  $n = 30, t = 7.13$  $p = 0.000$ </td></tr></table>

\* HSG-WR-BU solutions  
† Using IDEA leads to better performance.

Please rate the total number of Mill Stand solutions generated using IDEA.

<table><tr><td colspan="4">Much less than w/o IDEA</td><td colspan="4">About the same number as w/o IDEA</td><td colspan="3">Much more than w/o IDEA</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr></table>

For each of the design tasks, six of the better solutions produced using IDEA were evaluated with respect to quality. A question for evaluating the quality of a specific solution is shown below.

Please rate the quality of the following Mill Stand solution generated using IDEA

<table><tr><td colspan="3">1 HSG: C800</td><td colspan="2">WR: C700</td><td colspan="2">BU: C700</td><td colspan="2">MTR: P800</td><td colspan="2">PIN· P800</td></tr><tr><td colspan="3">Much worsethan w/o IDEA</td><td colspan="4">About the sameas w/o IDEA</td><td colspan="4">Much betterthan w/o IDEA</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr></table>

Note that 5 on the Likert scale for each of the questions corresponds to an experienced human designer's performance without assistance from IDEA (unassisted scenario). The expert gave a time rating of 10 for all the five tasks, indicating that using IDEA resulted in much quicker solutions. The mean rating for the number of solutions generated using IDEA was 9.60 (s = 0.89), which was significantly better than that for the unassisted scenario (p < 0.01). The mean quality rating for the 30 individual solutions was 7.73 (s = 2.10), again significantly better than the solution quality for the unassisted scenario $p < 0.01$ . So on all the three measures—time, number of solutions, and quality—the use of IDEA improved the performance of the human designer significantly. The questionnaire results are summarized in Table 6, which also includes the results of t-tests similar to those reported in Table 5.

## 5. Discussion

IDEA builds upon prior research in case-based design in several ways. As discussed before, the emphasis so far has been on solving design problems, rather than on providing design support. A system that provides design assistance is more likely to be adopted and relied upon than one which attempts to function in a standalone fashion. IDEA, in addition to allowing the user to be involved in activities such as selecting the solution, requires the user to add a lot of detail to the solution before the proposal is finally ready to be sent out. Using the selected solution as a ballpark, the design engineers give final shape to the design by completing several activities, such as sizing the chucks, selecting the bearings, generating the drawings, and providing detailed cost estimates.

Like JULIA, IDEA does not require all user specifications to be input at the beginning of the problem solving session. As previously noted, for real-world design tasks, many of the constraints are not known a priori—they are progressively formulated from higher-level functions/goals as problem solving proceeds. Though CADET and

KRITIK differentiate between functions and constraints, they require that both be specified initially.

IDEA, in contrast to the other case-based designers, maintains a solution space that consists of multiple solutions, not just one solution. Because some design constraints are dynamic, the solution space evolves with time. Maintaining an evolving solution space precludes IDEA from ruling out any potentially attractive solutions.

In contrast to the other systems, the cases in IDEA are real engineering design cases. The evaluation of IDEA was also carried out with real design tasks: RFPs received from prospective customers. To the best of our knowledge, none of the other systems has been formally evaluated on real tasks, something that is imperative for the field to mature (Cohen 1989). Also, IDEA's domain knowledge, acquired from recognized design experts, gives it much more credibility than the other systems.

Except for JULIA, none of the other systems adapts cases during composition. Though CADET merges snippets of different cases to generate a solution, it does so by avoiding any adaptation. KRITIK cannot make non-local structure modifications to design cases. CYCLOPS, which does not use CBR for design synthesis, checks for consistency during synthesis, but discards the design if it is inconsistent. There is a subtle distinction between JULIA and IDEA in terms of how they adapt cases during composition. While JULIA resolves conflicts by ruling out some of the parts, IDEA actually performs adaptation on one or more of them.

Our work has important implications for Information Systems (IS) researchers. The successful incorporation of CBR within a DSS framework should encourage researchers to explore the applicability and effectiveness of the approach in other domains. That would help us develop a better understanding of the role of CBR in a decision support context. For complex and relatively unstructured tasks, such as information systems design and local area network planning, a DSS framework that integrates several techniques—such as CBR, constraint posting, and multicriteria decision making—could prove to be valuable to future researchers. In particular, we believe that many of the techniques we developed—such as those for case adaptation, case composition, and constraint management—would provide a basis for future research in case-based decision support.

For IS practitioners, our work has interesting implications. It provides a way of maintaining an organizational memory, which ensures that valuable experiences accumulated over long periods of time are not lost due to employee turnover. Companies that maintain case banks could explore a large number of solutions in a limited time. Also, using an approach similar to ours could result in significant cost savings, not only because it would reduce the time to make decisions, but also because it might obviate the need for involving highly experienced personnel in the process.

## 6. Conclusions and Future Directions

This paper described the development of a case-based model for assisting designers in routine design tasks. The model provides an integrated and comprehensive framework for decision support. The model was realized as a computer system called IDEA, whose efficacy was evaluated by a design expert. The overall positive evaluation results support our central thesis that CBR is an effective and efficient decision support methodology. Our work paves the way for future research in case-based decision support. A worthwhile future endeavor is to apply the salient concepts and techniques embedded in the model to decision support tasks in different areas, such as information systems design, audit planning, and loan approval.

An important finding of our research is that CBR is an attractive methodology for tackling the complexity inherent in real-world design tasks. The approach seems to be particularly suitable for stable design domains, which are characterized by an absence of strong causal theories, but are usually endowed with a rich history of cases. The techniques developed in our work—such as those for decomposing tasks, functions and constraints; progressively revising/relaxing functions and constraints; performing dynamic case adaptation and composition; maintaining local and global consistency; maintaining multiple solutions; and optimizing multiple conflicting objectives—and the means for integrating those techniques could be generalized across a wide range of design tasks.

An expansion of the case base should improve IDEA's performance. Several interesting research questions might explore the impacts of a more comprehensive case base on system utility. IDEA is grounded in a model of design assistance, not one of a stand-alone designer. Given that conceptualization, what are the benefits of, and trade-offs between, an encyclopedic case base and adaptation/redesign skills? From the user's perspective, how much "intelligence" is helpful in an assistant? How does that compare with the amount of intelligence desired in a human assistant? If those differ, what does that teach us about the differences between human-human and human-computer interaction?

IDEA currently does not have a learning mechanism. Given the rich history of cases in the environment, it is natural to expect that the system be able to automatically acquire knowledge on its own (Marcus 1988, 1990). At present, only successful cases are stored in memory. The immediate goal, therefore, should be to devise a mechanism that would enable IDEA to learn from positive experiences. Later, unsuccessful cases could be added to case memory so that IDEA could learn from those negative experiences and avoid similar mistakes in future (Hammond 1986).

At present, IDEA can tackle problems that are sufficiently structured, where all the input functions must be specified by the user. What would happen if some of those functions are not known? IDEA would then have to deal with an under-constrained or ill-defined problem, something it fails to do currently. An ill-defined problem implies searching a very large space for solutions. The issue is to devise clever ways or heuristics to impose sufficient structure on the problem so that the search becomes tractable (Abraham 1993, Pople 1982). Also, as new opportunities are discovered, the model should be able to perform problem reformulation by restating or recasting the problem (Sycara 1991).

At present, IDEA's processing takes place in a predetermined sequence; the flow of control is static. To improve its performance, the processes could be ordered heuristically. The order could depend on factors such as availability and cost of equipment, time to converge to a solution, effects on other parts of the design, etc.

A complex design task is usually solved by a design team, rather than by a single individual. Different design personnel—such as mechanical engineers, electrical engineers, cost engineers, and draftsmen—bring into play their own perspectives into the team. Different perspectives generate different views of the design solution. At present, perspectives are incorporated as objectives within the multi-criteria selector. But that is different from maintaining different views of the design solution; currently, the views are combined into one and do not retain their separate identities. If view integration took place in a collaborative fashion among the team members, more synergistic problem solving might result (Gray et al. 1992).

Finally, the process of reinterpreting case-based knowledge for design in rapidly changing domains, such as local area network planning, may pose a challenge even for human experts. If IDEA could be extended to incorporate such a capability, it might truly be able to function as a design partner, even to experienced human designers. $^{12}$

$^{12}$ This research was supported in part by funding from Tippins, Inc. The authors thank Ronald Gretz, Sidney Snitkin, Andrew Park, and Alfred Capnioti for their generous contributions of time and their sharing of their knowledge. Kevin Ashley, Luis Vargas, and Alexander Kott provided significant help in structuring the IDEA model and played an important role in earlier versions of the writeup. The authors also wish to thank the associate editor and three anonymous referees of ISR for their many insightful comments on previous versions of the manuscript

## References

Abraham, D. M., "A Process Model of Initial Representation Formation in a LAN Planning Problem," Ph.D. Dissertation, Joseph M Katz Graduate School of Business, University of Pittsburgh, Pittsburgh, PA, 1993

Adelman, L., Evaluating Decision Support and Expert Systems, John Wiley, New York, 1992

Alter, S., "Transforming DSS Jargon into Principles for DSS Success," in P Gray (Ed.), Decision Support and Executive Information Systems, Prentice Hall, Englewood Cliffs, NJ, 1994, 3–26

Ashley, K D and E. Rissland, "Compare and Contrast, A Test of Expertise," Proc AAAI-87, American Association for Artificial Intelligence, Seattle, WA, 1987, 31–36.

— Modeling Legal Argument, MIT Press, Cambridge, MA, 1990

Bard, J. F., "A Comparison of the Analytic Hierarchy Process with Multiattribute Utility Theory," IIE Trans., 24, 5 (1992), 111-121.

Bareiss, E. R., Exemplar-Based Knowledge Acquisition A Unified Approach to Concept Representation, Classification, and Learning, Academic Press, Boston, MA, 1989.

Bonczek, R H., C. W. Holsapple, and A B. Whinston, Foundations of Decision Support Systems, Academic Press, Orlando, FL, 1981.

Brown, D. C. and B. Chandrasekaran, Design Problem Solving Knowledge Structures and Control Strategies, Pitman, London, UK/Morgan Kaufmann, San Mateo, CA, 1989

Buchanan, B. G., "Artificial Intelligence as an Experimental Science," in J. H. Fetzer (Ed.), Aspects of Artificial Intelligence, Kluwer Academic, Dordrecht, Holland, 1988, 209–250

Cohen, P. R., "Evaluation and Case-Based Reasoning," in Proc. DARPA Workshop on Case-Based Reasoning, Pensacola Beach, FL, DARPA/ISTO, Morgan Kaufmann, San Mateo, CA, 1989, 168–172

Coyne, R D., M. A. Rosenman, A D. Radford, M. Balachandran, and J. S Gero, Knowledge-Based Design Systems, Addison-Wesley, Reading, MA, 1990.

Goel, A. K., "Integration of Case-Based Reasoning and Model-Based Reasoning for Adaptive Design Problem Solving," Ph.D Dissertation, Ohio State University, Columbus, OH, 1989

— and B. Chandrasekaran, "Use of Device Models in Adaptation of Design Cases," in Proc. DARPA Workshop on Case-Based Reasoning, Pensacola Beach, FL, DARPA/ISTO, Morgan Kaufmann, San Mateo, CA, 1989, 100–109.

Gray, P., S. L. Alter, G. DeSanctis, G. W. Dickson, R. Johansen, K. L. Kraemer, L. Olfman, and D. R. Vogel, "Group Decision Support Systems," in E. A. Stohr and B. R. Konsynski (Eds), Information Systems and Decision Processes, IEEE Computer Society Press, Los Alamitos, CA, 1992, 75–135.

Hammond, K. J., "Learning to Anticipate and Avoid Problems Through the Explanation of Failures," in Proc. AAAI-86, Philadelphia, PA, 1986.

Hinrichs, T R., "Towards an Architecture for Open World Problem Solving," in J. Kolodner (Ed.), Proc. DARPA Workshop on Case-based Reasoning, Clearwater Beach, FL, DARPA/ISTO, Morgan Kaufmann, San Mateo, CA, 1988.

—, "Strategies for Adaptation and Recovery in a Design Problem Solver," in K. Hammond (Ed.), Proc DARPA Workshop on Case-Based Reasoning, Pensacola Beach, FL, DARPA/ISTO, Morgan Kaufmann, San Mateo, CA, 1989, 115–118

—, Problem Solving in Open Worlds: A Case Study in Design, Erlbaum, Northvale, NJ, 1992.

Keen, P. G. W., "Value Analysis: Justifying Decision Support Systems," in R. H. Sprague and H. J. Watson (Eds.), Decision Support Systems: Putting Theory into Practice, Prentice-Hall, Englewood Cliffs, NJ, 1989, 65–81.

— and M. S. Scott Morton, Decision Support Systems, Addison-Wesley, Reading, MA, 1978.

Kolodner, J. L., "Extending Problem Solving Capabilities through Case-Based Inference," in Proc. Fourth Annual International

Machine Learning Workshop, Irvine, CA, Morgan Kaufmann, 1987, 167–178

—— and R L Simpson, "The MEDIATOR: Analysis of an Early Case-Based Problem Solver," Cognitive Sci, 13, 4 (1989), 507–549

——, "Improving Human Decision Making Through Case-Based Decision-Aiding," AI Magazine, 12, 2 (1991), 52–68

—, Case-Based Reasoning, Morgan Kaufmann, San Mateo, CA, 1993

Konsynski, B. R., E. A. Stohr, and J. V. McGee, "Review and Critique of DSS," in E. A. Stohr and B. R. Konsynski (Eds), Information Systems and Decision Processes, IEEE Computer Society Press, Los Alamitos, CA, 1992, 7–26.

Koton, P., "Reasoning About Evidence in Causal Explanation," in Proc. AAAI-88, St. Paul, MN, 1988, 256–261.

Marcus, S. (Ed.), Automating Knowledge Acquisition for Expert Systems, Kluwer Academic, Norwell, MA, 1988

—— (Ed.), Knowledge Acquisition. Selected Research and Commentary, Kluwer Academic, Norwell, MA, 1990

Mostow, J, "Toward Better Models of the Design Process," AI Magazine, 6, 1 (1985), 44–57.

Mukhopadhyay, T, S. S Vicinanza, and M. J Prietula, "Examining the Feasibility of a Case-Based Reasoning Model for Software Effort Estimation," MIS Quarterly, 6, 2 (1992), 155–171

Navinchandra, D., "Case-Based Reasoning in CYCLOPS, a Design Problem Solver," in J. Kolodner (Ed.), Proc DARPA Workshop on Case-based Reasoning, Clearwater Beach, FL, DARPA/ISTO, Morgan Kaufmann, San Mateo, CA, 1988, 286–301.

——, Exploration and Innovation in Design. Towards a Computational Model, Springer Verlag, New York, 1991.

——, K. P. Sycara, and S. Narasimhan, "Behavioral Synthesis in CA-DET·A Case-Based Design Tool," in Proc. Seventh Conf Artificial Intelligence Applications, Miami, FL, 1991, 217–221

Pople, H E, Jr., "Heuristic Methods for Imposing Structure on Ill-Structured Problems: The Structuring of Medical Diagnostics," in P Szolovits (Ed.), Artificial Intelligence in Medicine, Westview Press, Boulder, CO, 1982, 119–190.

Redmond, M., "Combining Case-Based Reasoning, Explanation-Based Learning, and Learning from Instruction," in A Segre (Ed.), Proc Sixth International Workshop on Machine Learning, Morgan Kaufmann, San Mateo, CA, 1989

Riesbeck, C. K. and R. C. Schank, Inside Case-Based Reasoning, Lawrence Erlbaum, Hillsdale, NJ, 1989.

Simpson, R L, "A Computer Model of Case-Based Reasoning in Problem Solving: An Investigation in the Domain of Dispute Mediation," Ph.D Dissertation, School of Information and Computer Science, Georgia Institute of Technology, Atlanta, GA, 1985

Sinha, A. P., "IDEA: A Case-Based Model of Design Assistance," Ph.D. Dissertation, Joseph M. Katz Graduate School of Business, University of Pittsburgh, Pittsburgh, PA, 1993.

Slade, S, "Case-Based Reasoning: A Research Paradigm," Al Magazine, 12, 1 (1991), 42–55

Sprague, R H and E D Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

——, I. Benbasat, O. El Sawy, D King, T. R. Hill, H G Sol, and P. A

Todd, "Technology Environments to Support Decision Processes," in E A Stohr and B R Konsynski (Eds), Information Systems and Decision Processes, IEEE Computer Society Press, Los Alamitos, CA, 1992, 167–204

Stefik, M., "Planning with Constraints (MOLGEN. Part 1)," Artificial Intelligence, 16, 2 (1981), 11–139

Sycara, K P, "Resolving Adversarial Conflicts An Approach to Integrating Case-Based and Analytic Methods," Ph D Dissertation, School of Information and Computer Science, Georgia Institute of Technology, Atlanta, GA, 1987

——, "Problem Restructuring in Negotiation," Management Sci, 37, 10 (1991), 1248–1268

Michael J Shaw, Associate Editor. This paper was received on September 8, 1993, and has been with the authors 21 months for 2 revisions
