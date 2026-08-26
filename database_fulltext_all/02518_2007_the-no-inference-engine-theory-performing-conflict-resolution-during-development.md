---
otero_id: 2518
otero_key: "FKG2E8DW"
title: "The no inference engine theory — Performing conflict resolution during development"
authors: "Richard C. Hicks"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.11.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# The no inference engine theory — Performing conflict resolution during development

Richard C. Hicks

Department of MIS and Decision Science, Texas A and M International University, 5201 University Blvd., Laredo, Texas 78041, United States

Received 7 March 2005; received in revised form 8 February 2006; accepted 5 November 2006 Available online 19 December 2006

## Abstract

In many rule-based systems, an inference engine is a software component which reasons over rules when the application is executed. The major task performed by the inference engine is conflict resolution, which determines the sequence of the consultation. We describe a theory and the resulting development environment for performing conflict resolution during development to eliminate the inference engine for systems using propositional logic.

Using verification criteria and solution strategies, we derive four classes of rules and their rule ordering strategies, allowing conflict resolution to be performed during development. The resultant procedural implementations demonstrate dramatic performance improvements for some classes of rules, testing over 20,000 rules per s on a PC. © 2006 Elsevier B.V. All rights reserved.

Keywords: Expert systems; Inference engine; Rule order; Verification

## 1. Introduction

Most rule-based implementations consist of a rule base, an interface, and an inference engine. The inference engine reasons over the rules at run-time. Significant limitations of inference engine technology include the use of a proprietary language, the difficulty of creating and maintaining a rule base, performance, and cost [4]. For example, inference engines from the four largest inference engine companies cost between \$10,000 and \$35,000 per CPU, and an inference engine must reside on every computer that runs the resulting application.

There has been little significant research into the basic concepts of the inference engine since Forgy's seminal paper describing the RETE algorithm in 1981 [2]. Research into the inference engine has focused on extensions to the basic concepts, such as fuzzy logic [3], real-time systems [14], and additional data sources such as XML [18]. Other research has focused on modifications to the RETE algorithm such as the RETE II implemented in the commercial and public domain CLIPS and algorithms such as TREAT [8].

The reason for the popularity of the RETE implementations is their speed in performing the many pattern/ many match problems supported by first order logic. The approach we will describe is designed for propositional logic systems, which are limited to single pattern/many match problems, and is applicable to propositional logic systems and to the propositional logic components of systems.

The inference engine executes a recognize-act cycle [5]. The recognize step determines which rules in the rule base may fire (the conflict set) using conflict resolution and the act step executes the conclusion of the rule. In some cases, over 90% of the execution time is spent performing conflict resolution [2].

Conflict resolution is especially important when solving for single-valued conclusions because it can affect the accuracy and efficiency of the solution. The inference engine will test these rules only until one rule fires, and will not test any remaining rules. We will use the term First Rule Satisfied (FRS) to refer to these rules.

Previous research into FRS conflict resolution strategies has focused on situations where accuracy is a problem because the same set of inputs reaches different conclusions in different rules. We will refer to these rules later as Exceptions. The classic example from Winston [19] is the “bartender” problem, which may be expressed in two rules and two facts.

Facts: guest is a health nut, carrots are not served with the meal.

(r-1) If guest is a health nut, then drink = glop.

(r-2) If guest is health nut and carrots are not served with the meal then drink = carrot juice.

In an FRS implementation without conflict resolution, rule r-2 would never fire, although it is considered more desirable because it is more specific [11]. If it is known that the customer is a health nut and carrots were not served, the first rule, r-1, would always fire (from the knowledge that the customer is a health nut), the inference engine would stop testing rules for drink, and rule r-2 would never even be tested. In this example, the physical sequencing of the rules and the characteristics of a FRS implementation would keep the most desirable rule from being tested.

O'Leary approached the “bartender” problem from the perspective of verification and suboptimality in greedy inference engine implementations [11]. The problem of suboptimality is that the most desirable rule (r-2) was not tested and therefore the best solution was not reached. He then derives a rule ordering strategy for these rule clusters in which the most specific rules are ordered first. In the “bartender” problem, rule r-2 is ordered before rule r-1. In this case, a conflict resolution strategy which tested the most specific rule (r-2) first would be accurate, where a conflict resolution of firing the most general rule (r-1) first would be inaccurate.

The conflict resolution strategy of testing the most specific rules first is common in the expert systems industry, and is the default for most products. This strategy is also recommended in the manual for other expert systems shells, such as M.4 and CLIPS [5].

In this paper, we propose the No Inference Engine Theory (NIET) for rule-based systems. We propose that, for rules using propositional logic, conflict resolution can be performed during the development of the system. This transposes the declarative inference engine solution into a procedural solution containing little more than a sophisticated sequence of IF statements to implement the rules and inputs to instantiate conditions. Inference is still being performed, but the components are now distributed between the development environment and the delivery environment. In the conventional technology, all of the inference components are performed at run-time, where an NEIT system performs only inputs and logic at run-time and not conflict resolution. We theorize that this simplification of the run-time task will result in significant performance improvements.

To test this theory, we have constructed a research prototype IDE that generates complete, ready to run rule-based systems into procedural languages such as C++ and VisualBasic. Testing for raw speed indicates that the resulting implementations execute at least an order of magnitude faster than that of a very fast inference engine.

Before we describe the NIET, we must have a deeper understanding of conflict resolution. We have seen an example of how rule ordering and conflict resolution strategies affect accuracy in rule clusters containing exceptions. Next, we present an overview of traditional conflict resolution.

## 2. Traditional conflict resolution

At any time, a large number of rules may potentially fire. Conflict resolution determines the most desirable rule to test based on one of many criteria. As extensive documentation is available and the same strategy is used in most commercial inference engines, consider the public domain implementation of CLIPS. The main factor in rule selection is salience, which is a priority value assigned by the developer to each rule. For rules of equal salience, CLIPS provides seven conflict resolution strategies [5].

In the depth strategy, newly activated rules are placed above all rules of the same salience. In breadth, newly activated rules are placed below all rules of the same salience. Among rules of the same salience, newly activated rules are placed above all activations of rules with equal or higher specificity in the simplicity strategy. The complexity strategy places newly activated rules above all activations of rules with equal or lower specificity among rules of the same salience. The LEX and MEA strategies order rules of the same salience by the recency of the pattern activations in the rules. The random strategy uses a random number to determine the order among rules with the same salience [5]. The CLIPS manual recommends specificity, which tests the most specific rules first.

If a different salience is assigned to each rule, the conflict resolution strategy is disregarded. If the same salience, or no salience, is assigned to one or more rules, the conflict resolution strategy will determine the rule orderings.

It is important to consider the granularity of these conflict resolution strategies. For example, specificity and generality are determined by the number of conditions in a rule. In all but the smallest of rule sets, there will be many rules with the same number of conditions. When the conflict resolution strategy cannot order rules, as when several rules have the same number of conditions, the physical ordering in the rule base is used. This conflict resolution strategy implies that the developer will manually order every rule by encoding a salience, or will manually order the rules in each cluster as appropriate for the run-time conflict resolution strategy and the state of the consultation. Any errors in the rule orderings coded by the developer may cause inaccuracies or poor performance.

Conflict resolution determines the sequence in which rules fire, and is a major determinant in the accuracy and speed of an expert system. However, the strategies described above, excepting salience, are heuristic in nature. In addition, there is little guidance about the relationships between rule ordering, rule types, and conflict resolution strategies; the three volume CLIPS manual does not address this topic [5].

We contend that this approach to conflict resolution is theoretically weak, insufficiently granular, and incomplete for propositional logic systems. A significant omission of these conflict resolution strategies is that none consider the belief in the accuracy of the rule, often expressed in confidence factors (CNF). In many domains, the most desirable answer is the one in which the developer has the highest confidence.

Additionally, we contend that the conflict resolution strategies outlined above are biased toward solving the many pattern/many match problem and are not optimized for propositional systems. The emphasis on activation sequence is very significant in a many pattern/ many match problem, but we argue that it is not as relevant as other factors, such as cost or confidence, to propositional logic systems.

In order to make the conflict resolution process more theoretically sound, we will use verification criteria to classify rules and determine appropriate conflict resolution strategies. Toward this goal, we will next present a brief overview of expert systems verification.

## 3. Rules and rule base verification

Rule bases may contain several types of rules, which we will now classify by the verification criteria met by each type. There have been several major verification efforts, beginning in 1976 with TEIRESIAS [1], which was built by Shortliffe's team to facilitate the development of MYCIN [15]. TIERESIAS built a rule model from the completed rule base and suggested improvements when modifications were made. ONCOCIN contains a tool developed by Suwa, Scott, and Shortliffe to be used during development [17]. ONCOCIN examined the rule base for conflicts, subsumption, redundancy, and missing rules (completeness). Nyugen developed CHECK [10] as an extension of the ONCOCIN project. CHECK takes a global view of the rule base, not a rule cluster view. This effort added the criteria of unreferenced attribute values, dead-end Ifs and goals, illegal conclusions, and illegal attribute values. The next major effort came from the Lockheed Corporation's EVA project, lead by Stachowitz [16]. Stachowitz further refined our definition of verification to include 28 criteria. In addition to the criteria mentioned above, EVA includes specializations of several criteria. For example, where others discuss inconsistency, EVA defines inconsistency under generalization, incompatability, or synonomy. The COVER system developed by Preece [12] adopted a strategy of testing overlapping subsets of the rule base for completeness, allowing testing for completeness. In a 1997 survey of 40 verification tools, Murrell [9] concludes “The paper provides... areas in which the researcher can provide practitioners with valuable tools for the verification and validation of knowledge-based systems, where currently there are none…”

The concept of rule base partitioning was taken a step further with the Two-Tier Verification (TTV) [6] approach implemented in the development tool EZ-Xpert. TTV partitions both the rule base and 23 verification criteria to achieve computationally tractable tests. Each rule cluster is tested individually for local criteria, while the connections between the rule clusters are tested at a global level. The classes of criteria in TTV are:

Local Verification Criteria

Completeness, Consistency, Conciseness, Domain and Host Language Constraints

Global Verification Criteria

Reachability, Domain and Host Language Constraints

As each set of rules may have different characteristics, we will use the Local Verification criteria to classify sets of rules. Conciseness is optional for all rules, and Host Language Constraints are mandatory for all rules, so they are irrelevant to our classifications.

The criteria of Completeness and Consistency are the factors that differentiate between rule sets. The verification criteria of Completeness is satisfied if the rule cluster contains at least one rule that is satisfied by any combination of condition values. Consistency is satisfied when every set of condition values reaches the same conclusion for every rule that is satisfied by the set [6].

The first question is when is conflict resolution needed? It is not needed when the rule conclusion is multi-valued. In these rules, all possible solutions are required. All conditions must be instantiated and all rules must be tested, making ordering and conflict resolution irrelevant. It is possible for these rules to be complete and/or consistent, but this has no impact on the solution strategy. Many best answer strategies, such as highest CNF, will require that all rules be tested in order to determine the best solution.

In propositional logic systems, conflict resolution is relevant only to FRS rules. The Local Verification Criteria of Completeness and Consistency, combined with solution strategy, may be used to classify four classes of FRS rules.

We will begin with Consistent rules. In these rules, rule ordering does not affect accuracy as in the bartender example. The first class of rules enforces both the Complete and Consistency criteria.

## 3.1. Deterministic rules

Rules that satisfy every combination of condition values exist. Every combination of condition values reaches the same conclusion for every rule. Confidence is usually assigned with the maximum value.

The second class of rules is Consistent, but is Incomplete.

## 3.2. Incomplete rules

Incomplete rules meet the criteria of Consistency, but are Incomplete because not all combinations of condition values will satisfy a rule. Every rule triggered by a set of condition values reaches the same conclusion.

Next, we evaluate the Incomplete and Inconsistent rules. Rules do not cover all combinations of condition values, and the same set of condition values may reach different conclusions in different rules. To differentiate between them, we examine their desired outcomes. One class of these rules is solved to return the solution with the highest belief. The other class of rules that are Incomplete and Inconsistent, the Exception, was introduced in the bartender example.

## 3.3. Belief rules

The most desirable solution is the one with the highest confidence, or CNF. Traditionally, the inference engine instantiates all conditions, tests all rules, and calculates the run-time confidence in all of the fired rules to determine the solution with the highest CNF based on both the user's and developer's CNFs.

## 3.4. Exception

In these rules, more specific rules are the most desirable solutions because they represent exceptions to more general rules, as in the “bartender” example [11].

The verification criteria met by each rule cluster type is shown in Table 1.

We now have derived four classes of FRS rules. Deterministic rules are Complete and Consistent. Incomplete rules are Incomplete but Consistent. Exception rules are Inconsistent and Incomplete, as are Belief rules. All-rule solutions do not need conflict resolution, as all rules must be fired and their sequence is irrelevant. The current IDE and theory do not support many pattern/many match rules, which are best solved by a RETE algorithm.

Next, we consider conflict resolution strategies for these rule types.

## 4. Conflict resolution during development

Traditional inference engines perform conflict resolution at run-time. By adopting an implementation strategy that tests FRS rules in the sequence that they occur, and performing conflict resolution through rule ordering during development, we move the computational burden of conflict resolution from the run-time environment to the development environment. Removing conflict resolution from the run-time environment simplifies the application into a sequence of IF statements and inputs, and allows the implementation to use compiled procedural logic instead of declarative inference.

Table 1  
Verification classes and rule types

<table><tr><td></td><td>Completeness</td><td>Consistency</td></tr><tr><td>Deterministic</td><td>Yes</td><td>Yes</td></tr><tr><td>Incomplete</td><td>No</td><td>Yes</td></tr><tr><td>Belief</td><td>No</td><td>No</td></tr><tr><td>Exceptions</td><td>No</td><td>No</td></tr><tr><td>Multi-rule</td><td>Optional</td><td>Optional</td></tr><tr><td>Many pattern</td><td>No</td><td>No</td></tr></table>

An IDE for the development of intelligent applications, EZ-Xpert, is described in [7]. The research prototype described in that paper performs verification testing for 23 criteria, performs algorithmic refinement, and generates code for ten expert system shells. The prototype has been extended to support rule types and generation of code into traditional procedural development languages such as C++, VisualBasic, and Java. Additional information about the IDE and samples can be found at www.ez-xpert.com.

The first question that we must ask concerns the choices of conflict resolution strategies. All of the existing strategies are heuristic. Are these the most appropriate conflict resolution mechanisms for propositional logic systems? Are there not other techniques that are more appropriate? Additionally, none of these strategies consider the confidence in the accuracy of a rule, which is often expressed in Confidence Factors.

## 4.1. Exception rules

The specificity strategy, which is the traditional default, is the correct solution for Exception rules but is not suited to all rule types. It is the default because Exceptions will be tested before the more general rules, therefore enhancing accuracy in inconsistent rule clusters. It also negatively affects solution efficiency without improving accuracy in consistent rules. For example, the generality strategy, which fires the most general rules first, will tend to lower the cost of solving consistent rule clusters without sacrificing accuracy. Examine the deterministic rule cluster for determining a patient's Contact Lens in Fig. 1.

If these rules are solved by a specificity strategy, three conditions will be elicited before any rules can be tested. The conflict resolution mechanism would determine that rules two through nine have the same specificity. It will therefore test those rules in the order in which they occur, starting with rule two.

If the same rules are solved by generality, only one condition, TearProduction, is needed to test the first rule. It should be noted that the probability of a more general rule firing is high, as they cover a large percentage of the search space.

## 4.2. Consistent rules

Generality by itself is not the most accurate determinant for solving consistent rules, especially when considering backward chaining environments. Generality implies lower costs because fewer conditions are contained in a rule, but this is not always true. When a condition obtains a value from other rules, the cost for instantiating the conditions in subordinate rules may be very high. Additionally, all conditions are not equivalent in financial or computational cost. For example, if determining TearProduction required a \$1,000,000 test and the other attributes could be determined by asking the patient, it would be given a very high cost and would be elicited only when other options have failed. A condition value may be obtained by selecting an answer from a listbox, but it may also require processes that are computationally or financially expensive. In the IDE, each condition (that does not get its value from other rules) in the rule base is assigned a value corresponding to the relative cost of obtaining the value. To lower the cost of the consultation without adversely affecting accuracy, consistent rule clusters will be ordered by incremental cost, then CNF, then generality. Costs for conditions determined by rules include the costs of any necessary conditions in subordinate rule clusters. The least expensive rule is tested first, lowering solution costs and usually raising computational efficiency.

<table><tr><td></td><td>Age</td><td>Prescription</td><td>Astigmatism</td><td>TearProduction</td><td>Lens</td><td>CNF</td></tr><tr><td>1</td><td></td><td></td><td></td><td>Reduced</td><td>None</td><td>100</td></tr><tr><td>2</td><td></td><td>FALSE</td><td>Hypermetrope</td><td>Normal</td><td>Soft</td><td>100</td></tr><tr><td>3</td><td></td><td>TRUE</td><td>Myope</td><td>Normal</td><td>Hard</td><td>100</td></tr><tr><td>4</td><td>Pre_Presbyopic</td><td>FALSE</td><td></td><td>Normal</td><td>Soft</td><td>100</td></tr><tr><td>5</td><td>Young</td><td>FALSE</td><td></td><td>Normal</td><td>Soft</td><td>100</td></tr><tr><td>6</td><td>Young</td><td>TRUE</td><td></td><td>Normal</td><td>Hard</td><td>100</td></tr><tr><td>7</td><td>Pre_Presbyopic</td><td>TRUE</td><td>Hypermetrope</td><td></td><td>None</td><td>100</td></tr><tr><td>8</td><td>Presbyopic</td><td>FALSE</td><td>Myope</td><td></td><td>None</td><td>100</td></tr><tr><td>9</td><td>Presbyopic</td><td>TRUE</td><td>Hypermetrope</td><td></td><td>None</td><td>100</td></tr></table>

Fig. 1.

## 4.3. Belief rules

A major weakness in the traditional conflict resolution strategies is that none of these strategies consider solving for the highest belief. Rules express the developer's belief in the rule in the form of a CNF. High CNFs indicate high beliefs in the conclusion of the rule when the conditions are met, while low CNFs indicate lower belief. The traditional approach to computing CNF is based on the user's CNF that is input at run-time and the developer's CNF assigned to the rule. This approach requires instantiation of all conditions and testing of all rules so that the overall CNF of every fired rule can be compared.

However, in many cases the CNF for every condition is the maximum, or the system is automated and has no user to provide CNFs, or it is not desirable to ask the user to assign a CNF. For FRS rule clusters, solving for the Highest Developer CNF by testing rules ordered by the Developer CNF until one fires will be more computationally efficient than solving for the Highest Run-Time CNF, which requires instantiating every condition and solving every rule to determine the runtime CNF. The IDE supports both strategies.

## 4.4. Rule orderings

The verification criteria met for each rule cluster determine the appropriate solution strategy and therefore the appropriate rule ordering. Ties are broken for each rule type by the hierarchy of relevance of the other solution characteristics.

In the Consistent rule clusters, Deterministic and Incomplete, accuracy is not affected by rule ordering, making cost the dominant factor in solution efficiency. If two rules have the same cost, the next significant factor is confidence, which indicates the developer's relative belief in the rule. If a tie still exists, the least specific rule would be ordered first because it contains the rules covering the largest portion of the search space. If a tie still exists, the rules will be ordered in the physical order that they exist in the rule base.

In Belief rule clusters, the confidence in the rule is used to determine the “best” solution. Therefore, the dominant factor in these rules is CNF and the first ordering criteria is the developer's CNF. Accuracy is a concern in these rules, so the next factor is the most specific rules. If ties still remain, order the rules by lowest cost. If ties still exist, order the rules by the physical order in the rules.

Exception rules are more accurate when the most specific rules are tested first [11]. If two rules have the same specificity, the next factor is developer CNF to maximize accuracy. If two rules have the same CNF, the next factor is lowest cost. If two rules have the same cost, order the rules by the physical order of the rules.

Table 2 shows the types of FRS rules and the appropriate orderings. Note that this theory achieves much higher granularity than the traditional conflict resolution theory.

Ordering the rules by verification criteria and solution strategy allows the run-time rule testing of propositional logic systems to be performed in the physical sequence that the rules occur and eliminates the need for run-time conflict resolution.

In summary, during development the rule developer specifies the rule class for each set of rules. The IDE constrains the rule builders with the appropriate verification constraints. When the rules have been specified and tested in the menu-driven, fill in the blank interface, the IDE algorithmically simplifies the rules, orders each rule set, and generates ready to compile and deploy code.

## 5. Input sequencing in backward-chaining systems

The generated code takes a hybrid chaining approach to Interactive systems, while Automated and Monitoring systems depend on external sources instantiating facts and use only forward chaining. When the implementation begins, it determines if any facts have been instantiated. If so, forward chaining is performed without the instantiation of any new conditions. If new facts are instantiated by rule firings, they will simplify the consultation and potentially solve the consultation. If the consultation is not solved, the Interactive systems will then implement backward chaining and obtain inputs from the user.

The generated code contains sets of properly ordered rules, eliminating conflict resolution. The sequencing of backward chaining inputs is also performed during development. Each rule is sent sequentially to the rule solver. Inputs are instantiated by an on-demand algorithm in the rule solver component.

Table 2  
Verification criteria determine solution strategy

<table><tr><td>Strategy/rule type</td><td>Consistent</td><td>Belief</td><td>Exceptions</td></tr><tr><td>Cost/CNF/Generality</td><td>X</td><td></td><td></td></tr><tr><td>CNF/Specificity/Cost</td><td></td><td>X</td><td></td></tr><tr><td>Specificity/CNF/Cost</td><td></td><td></td><td>X</td></tr></table>

The first task that the rule solver performs is to determine if any conditions have already been instantiated. Each condition is compared to the existing facts. If the condition exists, it is tested against the operator and value specified by the rule. If the condition fails, the rule also fails, and execution is passed to the next rule. If the condition passes, it is deleted and testing of the rule continues.

If none of the conditions which have already been instantiated fail, values are solicited from the user for the remaining conditions. At this level of granularity, accuracy is unaffected by sequence. However, solution efficiency is enhanced by ordering the inputs by lowest cost in the IDE; this also allows the developer to influence the input sequence within a rule. After each condition is instantiated, it is tested against the operator and value specified by the rule. If the condition fails, the rule also fails, and execution is passed to the next rule. If the condition passes, it is deleted and testing of the rule continues.

If none of the conditions in the rule fails, the rule itself passes. The activities in the Then portion of the rule are executed. If the rule is FRS, testing of the rule set is complete. If the rule seeks all possible values, execution passes to the next rule until all are tested. When testing is complete, execution returns to the calling code.

The elimination of conflict resolution from the runtime implementation transposes a declarative implementation into a procedural one and eliminates the need for a physical inference engine.

## 6. Benefits of eliminating the inference engine

A significant benefit of eliminating the physical inference engine is the speed of the resulting applications. As conflict resolution has been performed during development, the run-time task is less complex that the task of an inference engine implementation. In addition, inference engine latency – the time necessary to read the inference engine from disk and initialize it, read the knowledge base from disk, parse it, and determine the initial rule to test – is almost eliminated.

No standard speed tests exist for propositional systems, such as the Manners or Waltz [8] tests derived for RETE systems by Miranker's group at the University of Texas. To test speed, several rule bases were constructed using variations of the Chess End Game Test Set [13] used for testing induction algorithms. This test set is deterministic and consists of 648 rules with seven conditions in each rule for a total of 4,536 conditions. Larger rule sets are created by duplicating the original rules and modifying the 648th rule so that it occurs only at the end of the rule base. Each rule base was tested by supplying the facts necessary to fire the last rule in the rule base.

On a 2.4 GHz PC, a rule base containing 19,440 rules was solved in .812 s, which equates to 23,940 rules per s. A rule base containing 12,960 rules was solved in .563 s, which equates to 23,019 rules per s, and a rule base containing 648 rules was solved in .031 s for a rate of 20,645 rules per s. All of these examples test over 20,000 rules per s. It should also be noted that the number of rules tested per s actually increases very slightly as rule base size increases, in vivid contrast to other approaches. These samples are not optimized for speed, but contain full functionality such as explanations, confidence factor calculations, and tests for non-monotonicity.

Large rule bases could not be tested because of limitations in CLIPS 6.21, which contains the updated RETE algorithm and is considered to be one of the fastest inference engines, but a shortened version of the same rule base containing 90 rules took .046 s, or 1956 rules per s. The NEIT solution took .031 s to test 648 rules, so it is over an order of magnitude faster while performing a task over seven times as large. This comparison overstates the performance of CLIPS, as the number of rules has a dramatic impact on the performance of traditional inference engines. CLIPS R/2 benchmarks of the Manners test set (www.pst.com/benchcr2.htm) performed on a Sun workstation show a speed of 325 rules fired per s when 624 rules are fired, and a speed of 104 rules per s when 4944 rules are fired. In the same benchmarks, NASA CLIPS, with the original RETE algorithm, took 2.13 h to fire 4944 rules. As the NIET implementations consistently test over 20,000 rules per s independent of rule base size, and the CLIPS test returns under 2000 rules per s on a rule base with only 90 rules, speed increases of over an order of magnitude have been achieved. Considering the performance profiles of traditional systems and the linear speed of the NEIT implementations, it is expected that the larger the rule base, the larger the performance improvement can be expected.

Others have compiled expert systems for performance advantages, although these approaches all start with the knowledge captured in an appropriate language. Miranker created C++ RETE systems, and stated that typically, performance is between 10 to 20 times faster [8]. In US Patent #5,442,792, Chun describes a system that transposed an expert system from declarative to procedural and the resulting system improved speed by 132 times and the system ran in 1/16th of the memory of the declarative solution. However, it is hard to derive any substance from these figures until a common test set is accepted.

It should be noted that the Chess example described above would not actually be implemented. The IDE algorithmically simplifies consistent rule clusters prior to generating code [7]. Simplification of the Chess example results in 12 rules with 38 conditions. Simplification makes the knowledge in the system more accessible; for example, the fact that people with poor tear production don't get contact lenses is obvious in Fig. 1, but is lost in the most specific representation of this knowledge in 24 rules, half of which represent the knowledge in this single rule. The IDE has an Explode button that expands a rule to its most specific representation and an incremental simplification algorithm for maintenance.

The IDE generates code into the firm's normal programming language, such as C++, Java, or VisualBasic, so there is no new language to learn and support. The cost of the inference engine is eliminated. The generated code is simply included and compiled as a component of the host application, eliminating the need for any implementation support. In addition, the intelligent components can be transparently embedded in commercial software.

By automating verification, conflict resolution, and code generation, this approach allows end users to become developers who create and maintain rule-based systems. It is unrealistic to expect any end user to create and maintain a substantial rule based system using an inference engine because of the requirements for verification and conflict resolution. As Gill [4] observes, systems that depend on end user maintenance have a high failure rate. However, the NEIT IDE dramatically reduces the time and cost required. The 648 rule Chess example was created in less than 6 h. While no published metrics establish the throughput of the traditional Knowledge Engineer approach, informal conversations estimate a rate of between one and 20 rules per man/day. In addition, 20% of the Knowledge Engineers time is spent with the firm's expert.

NEIT also makes the inference process transparent to the developer by making run-time execution predictable. Using the IDE, the inference path through the rule base can be seen in the rule browser. The rules are tested from top to bottom, and the conditions are elicited from left to right. In contrast, the current technology is a black box, where it is very difficult to predict the sequence of rules that will be tested.

In summary, this theory allows typical end users to quickly develop verified, high performance rule-based systems that dramatically out perform their inference engine equivalents.

## 7. Conclusions

The current inference engine theory and technology have many drawbacks, including poor computational performance, cost, and the difficulty of coding an accurate intelligent application. The most complex task performed by the inference engine is conflict resolution, which directs the sequence of execution. With the current technology, it is the developer's responsibility to manually code virtually every rule in accordance with the conflict resolution strategy adopted at run-time by the inference engine. Errors may cause inaccuracies or poorer computational performance, necessitating highly specialized personnel for both development and maintenance.

In contrast, the NEIT performs conflict resolution in the development IDE. Rule based systems using FRS rules contain four classes of rules — Deterministic, Incomplete, Exception, and Belief. The class of rule is used by the IDE to implement the appropriate conflict resolution strategy during development, eliminating the need for run-time conflict resolution and therefore eliminating the need for a physical inference engine.

The elimination of the need for run-time conflict resolution simplifies the run-time code to a sequence of IF statements and inputs, allowing the IDE to generate procedural code that performs with the same logic as the inference engine implementation. The procedural implementation is far faster, testing over 20,000 rules per s. Memory requirements are also much lower.

Eliminating the inference engine has many other benefits. The cost of the inference engine, which can be up to \$35,000 per CPU, is eliminated. The need to learn and support a new language is eliminated, although the IDE must be learned. The need for additional skills in knowledge engineering and expert systems implementations is dramatically lowered. As the IDE generates code into the developer's desired language, customization and extension are much easier than in a proprietary language.

By performing conflict resolution and verification algorithmically in the IDE, the task of the rule base developer is greatly simplified, increasing the speed of development and lowering the necessary skill level to that of a typical end user. This dramatically lowers the cost and time to market for a project. The prototype IDE developed the 648 rule Chess End Game test set in less than 6 h, and developers can be trained in 2 h. The IDE contains extensive Wizard support and a project debugger to assist the developer.

The highest levels of accuracy are ensured by the IDE, which tests the knowledge for 23 criteria. The IDE also algorithmically refines the knowledge, orders the rules, and generates code that is ready to compile and deploy. Most testing is done algorithmically, lowering the time needed for testing, so that the only tests that the developer needs to run are to determine if the knowledge was entered correctly into the IDE.

All of these factors should lower the cost of an expert systems implementation and raise the accuracy of the implementation. In some cases, the domain expert can learn the IDE and produce the NEIT implementation is less time than it would take to initially educate the knowledge engineer, producing a final system before a knowledge engineer would write a line of code, and would then be able to maintain the system. The prototype IDE has produced over 100 rules per h in informal testing compared to the industry metric of 1 to 20 rules per man/ day. Development times drop from months to days while eliminating the need for expensive specialists such as knowledge engineers and lowering the time demands on the domain expert by eliminating the interview process. A simple 500 rule system would traditionally take 25 knowledge engineer man/days to implement and cost \$25,000 in knowledge engineer fees. A NEIT system could be implemented by the domain expert in two days, including the training for the IDE. In addition, the domain expert would be involved with the development of the NEIT system for two days, where he would be expect to involved for five days in the traditional approach.

Additionally, the performance advantages allow the creation of very large rule bases and cooperative rule bases that are beyond the capabilities of current technology, expanding the possibilities for rule based implementations. Although most current rule bases are fairly small, it is not obvious if this is because the knowledge needs are small or that the technology is not able to support larger problems. NASA CLIPS took over 2 h to seat 96 people at a Manners party, which would certainly limit the uses for the technology. Because the NEIT implementations run much faster in a smaller memory space, the implementation hardware can sometimes be downsized from a mini computer to a PC. Alternatively, many more operations can be performed with the same implementation hardware.

There are several side effects to NEIT that users should consider. Small rule bases will show less benefit from the performance advantages, but will still benefit from the verification testing done by the IDE. Rules with multi-valued conclusions may receive little benefit, as conflict resolution is irrelevant in these rules. Additionally, the current implementation must be recompiled each time the rules are modified, which may be problematic in dynamic environments.

There are several areas that will benefit from additional research. There has been little empirical research into the cost and effort of creating and maintaining rule based systems, as well as their performance and accuracy, using various methodologies such as the knowledge engineer vs. the end user vs. an end user with an IDE. Another area for research is the development of a speed test for propositional systems. The 648 rule test set used in this article is sufficiently large, but is flat and does not chain to other sets of rules. Finally, NIET does not support first order logic, and a logical extension of this research would be to consider a NEIT solution to first order logic problems, as well as to research other domains that would benefit from additional rule classes and solution strategies.

This paper describes the NIET for solving FRS rules. It is hoped that this research will assist practitioners in developing fast, accurate, intelligent systems.

An earlier version of this paper was presented at the 35th Annual Meeting of the Decision Sciences Institute in Boston, MA, November 2004.

## References

[1] Davis, R. Applications of Meta-Level Knowledge to the Construction, Maintenance, and Use of Large Knowledge Bases, Ph.D. Dissertation, Stanford Univ., 1976.

[2] Charles L. Forgy, RETE: a fast algorithm for the many pattern/ many object pattern match problem, Artificial Intelligence 19 (1) (1982).

[3] G. Gerla, Inferences in probability logic, Artificial Intelligence 70 (1–2) (1994)

[4] T. Grandon Gill, Early expert systems: where are they now? Management Information Systems Quarterly 19 (1) (1995).

[5] Joseph C. Giarratano, CLIPS 6.21 User's Guide, International Thompson Publishing, 2003.

[6] Richard C. Hicks, Two-Tier verification of rule-based expert systems, Journal of Computer Information Systems 37 (1) (1996).

[7] R.C. Hicks, Knowledge base management systems-tools for creating verified intelligent systems, Knowledge-Based Systems, 2003.

[8] D.P. Miranker, B. Lofaso, The organization and performance of a treat-based production system compiler, IEEE Transactions on Knowledge and Data Engineering 3 (1) (1991).

[9] Steven Murrell, Robert T. Plant, A survey of tools for the validation and verification of knowledge-based systems: 1985-1995, Decision Support Systems 21 (1997).

[10] T.A. Nyugen, W.A. Perkins, T.J. Laffey, D. Pedora, Knowledge base verification, Artificial Intelligence 8 (2) (1987).

[11] Daniel E. O'Leary, Inference engine greediness: subsumption and suboptimality, Decision Support 21 (1997)

[12] A.D. Preece, A new approach to detecting missing knowledge in expert system rule bases, International Journal of Man-Machine Studies 38 (1993).

[13] J.R. Quinlan, Simplifying decision trees, knowledge acquisition for knowledge-based systems, in: B. Gaines, J. Boose (Eds.), Academic Press, 1988.

[14] M. Shimbo, T. Ishida, Controlling the learning process of realtime heuristic search, Artificial Intelligence 146 (1) (2003).

[15] E.H. Shortliffe, Computer-based medical consultations: MYCIN, Elsivier Publishing, New York, NY, 1976.

[16] R. Stachowitz, Validation of knowledge-based systems, Tutorial at the Hawaii International Conference on System Sciences, Kona, Hawaii, Jan. 1990.

[17] M. Suwa, A.C. Scott, E.H. Shortliffe, An approach to verifying completeness and consistency in a rule-based expert system, AI Magazine 3 (4) (1982).

[18] S. Swamynathan, A. Kannan, T.V. Geetha, Composite event monitoring in XML repositories using generic rule framework for providing reactive e-services. Decision Support Systems, to appear.

[19] P. Winston, Artificial intelligence, Addison-Wesley, Reading, MA, 1993.

![](/api/attachments/FKG2E8DW/fulltext/images/a5b6879e67353f9b6be5eaa939fde889efcfc2c42156e9a2535d270aec78c7b2.jpg)

Richard Hicks is an Associate Professor of Information Technology at Texas A and M International University, where he teaches in the Ph.D. program. He holds a Ph.D. from the University of Texas at Austin. His research has appeared in academic journals such as Journal of Computer Information Systems and Information and Management. He is the designer and developer of the artificial intelligence RAD development environment EZ-Xpert, and is currently researching inference without the inference engine.
