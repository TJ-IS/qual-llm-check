---
otero_id: 21724
otero_key: "UNEUU4Y8"
title: "Circuit diagnosis support system for electronics assembly operations"
authors: "Anantaram Balakrishnan; Thilo Semmelbauer"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00015-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Circuit diagnosis support system for electronics assembly operations

Anantaram Balakrishnan <sup>a,)</sup>, Thilo Semmelbauer <sup>b,1</sup>

<sup>a</sup> The Smeal College of Business Administration, The PennsylÕania State UniÕersity, 303 Beam Building, UniÕersity Park, PA 16802, USA Massachusetts Institute of Technology, 1 Amherst Street, Cambridge, MA 02139, USA

Accepted 11 February 1999

## Abstract

Diagnosis and repair operations are often major bottlenecks in electronics circuit assembly operations. Increasing board density and circuit complexity have made fault diagnosis difficult. But, with shrinking product life cycles and increasing competition, quick diagnosis and feedback is critical for cost control, process improvement, and timely product introduction. This paper describes a case-based diagnosis support system to improve the effectiveness and efficiency of circuit diagnosis in electronics assembly facilities. The system stores individual diagnostic instances rather than general rules and algorithmic procedures, and prioritizes the tests during the sequential testing process. Its knowledge base grows as new faults are detected and diagnosed by the analyzers. The system provides distributed access to multiple users, and incorporates on-line updating features that make it quick to adapt to changing circumstances. Because it is easy to install and update, this method is well-suited for real manufacturing applications. We have implemented a prototype version, and tested the approach in an actual electronics assembly environment. We describe the system’s underlying principles, discuss methods to improve diagnostic effectiveness through principled test selection and sequencing, and discuss managerial implications for successfu implementation. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Circuit diagnosis; Electronics assembly; Decision support system; Case-based system

## 1. Introduction

Electronic circuit diagnosis is the process of identifying the components or connections that are responsible for the malfunction of a defective printed circuit board so that corrective action can be taken both to repair the board and to improve the process.

Diagnosis and repair operations are often major bottlenecks in circuit board assembly facilities because they are labor intensive and highly variable. Annual expenses directly related to troubleshooting and rework can exceed hundreds of thousands of dollars even in a medium-sized facility. The diagnosis task has become considerably more difficult in recent years due to increasing circuit complexity, greater board density, and the introduction of new high-precision assembly processes. But, as product life cycles continue to shrink and companies attempt to capture market share early, the ability to diagnose defects quickly and provide rapid feedback for process control and improvement is critical. Reducing technician time to diagnose faults is also an important concern since trained technicians are scarce and expensive.

This paper, based on a project at a high-volume consumer electronics assembly plant, describes a case-based system to support circuit diagnosis. The plant, faced with rapid new product introductions and a shortage of skilled technicians, wanted to improve the efficiency of its circuit diagnosis operation, reduce the workload on its few expert analyzers, and develop a tool to train new technicians, without devoting significant system development resources. An informal survey of available systems and current practice revealed that, although the literature describes several rule-based and model-based systems to support diagnosis, these systems are not widely used by industry partly because they are inadequate or require considerable time and special expertise to develop and maintain.

The case-based approach offers a practical means to improve diagnosis productivity and accuracy. The method uses information about prior diagnostic instances to eliminate candidate defects during the sequential testing process. It also accumulates knowledge on-line in the form of cases, i.e., diagnostic instances and their associated test outcomes, as analyzers identify new faults. The system does not require specialized computer personnel for maintenance, and the standard format of a case promotes learning and information sharing among technicians Ž . e.g., working in different shifts or production lines . We enhanced the basic case-based approach to systematically select tests and optimize the search process. To validate the overall approach, we implemented and tested a prototype on a client–server system in a high-volume printed circuit board Ž . surface-mount assembly line producing a hybrid Ž . analog and digital circuit board for a consumer electronics product. Within five weeks of installation, the system had acquired enough diagnostic instances to correctly diagnose 90% of the defects. Based on our implementation experience, we offer suggestions to improve the management of the diagnosis function. We emphasize that this paper focuses on circuit diagnosis, i.e., isolating the component sŽ . or connection s responsible for board malfunction.Ž . The subsequent step of root cause analysis, i.e., investigating and correcting the root cause of the defect e.g., an assembly process or the product’s Ž design , is equally important but not addressed here..

The rest of this paper is organized as follows. Section 2 outlines the circuit diagnosis process, and discusses related decision support opportunities and criteria. Section 3 describes the underlying structure and operation of a basic case-based system for circuit diagnosis. Section 4 discusses how to improve diagnosis efficiency through proper sequencing of tests based upon the likelihood of different defects. We formalize the optimal test sequencing problem by formulating it as a dynamic program to minimize the expected number of tests per board, and outline some heuristic methods for on-line test selection. Section 5 describes our prototype implementation and the lessons we learned from this implementation exercise.

## 2. The circuit diagnosis process

The printed circuit board assembly process consists of solder paste application, component placement, soldering, in-line inspection, and testing operations see Ref. 23 for a detailed description of eachŽ <sup>w</sup> <sup>x</sup> processing step . If a board fails the in-line in-cir-. Ž cuit or functional tests, it goes to a rework station. for detailed off-line diagnosis and repair. EachŽ . component and connection on a circuit board is a potential defect site, and the types and causes of defects are varied. For instance, a board might malfunction because of a defective component s , place- Ž . ment of the wrong component, defect in the printed circuit board’s internal wiring, or improper out ofŽ control manufacturing process such as poor solder-. ing or component misalignment.

In a circuit board with hundreds of components, the number of defect generation possibilities is enormous. So, achieving perfect first pass yield is almost impossible even with highly capable placement and soldering operations. At the same time, higher board densities, smaller components, and fewer accessible connections and test pads have reduced the diagnostic capabilities of in-line testing and inspection operations. For instance, in-circuit testing which canŽ verify the functionality of individual components; see, for instance, Ref. 16 is infeasible or has<sup>w</sup> <sup>x</sup>. limited use for dense surface-mount boards 7 . This<sup>w</sup> <sup>x</sup> method is also prone to measurement errors 3 , and<sup>w</sup> <sup>x</sup> is uneconomical for short production runs due toŽ product-specific tooling and programming requirements . Functional testing, which measures the cir-. cuit’s response at the board’s output ports or edge connectors to different combinations of input signals, can typically only trace a board’s failure to an approximate region or block of components but not to a particular component or connection on the board. Consequently, in-line inspection and testing operations serve primarily as screening processes, i.e., to identify defective boards. Malfunctioning boards are then sent to an off-line repair station where expert technicians or analyzers perform detailed diagnosis to isolate the component or connection that is responsible for the defect. This paper focuses on providing computer-based support for this off-line diagnosis or ‘diagnosis’, in brief process.Ž .

## 2.1. Sequential testing procedure for off-line diagnosis

Diagnosing a circuit board that has failed in-line tests entails identifying the responsible components or connections on the board, so that appropriate corrective action can be taken to repair the board. We define a defect as the finest grain source of malfunction that an analyzer can be unambiguously identify. Defects are distinguished by their symptoms and the means to diagnose them, but different defects might possibly require the same corrective action.

Before the diagnosis process begins, each defective board has an associated set of possible defects, called the candidate defect set, depending on which in-line tests it failed and the failure modes. The analyzer’s task is to identify the ‘true’ defect s inŽ . this candidate set by conducting additional tests on the board, and observing the outcomes of these tests. In this context, a test is any action, either manual or using automated test equipment that provides additional information about the board’s performance. For instance, a test might consist of applying a certain set of electrical inputs, possibly adjusting some circuit elements e.g., tuning capacitors , and Ž . monitoring the board’s response by probing selected locations and measuring the voltage or viewing the signal on an oscilloscope. We refer to the set of possible results of a test as its possible outcomes.

The outcome of a test depends on the actual defect in the board. By successively applying various tests, the analyzer can progressively prune the candidate defect set.

At each stage, the analyzer has a set of aÕailable tests that can distinguish between the current candidate defects. Conceptually, the diagnosis process entails applying the following iterative procedure. Starting with the initial set of candidate defects and available tests, the analyzer: i selects and appliesŽ . one of the currently available tests, ii observes the Ž . outcome of this test, iii eliminates all candidateŽ . defects that cannot produce the observed outcome, and iv eliminates from the available test set thoseŽ . tests that cannot distinguish between the remaining defects. In the ideal situation, assuming that all defects are known a priori, the test suite is comprehensive, and measurements are error-free, this process will terminate with the candidate defect set containing only the true defect. Otherwise, the analyzer needs to take ‘extraordinary actions’ to diagnose the true defect, and augment the knowledge base. These actions might entail detailed experimentation and consultations with design engineers, production staff, and component vendors.

The time to diagnose a board depends on the number of tests that the analyzer performs. Reducing this time and improving diagnosis efficiency, therefore, requires avoiding unnecessary tests by systematically updating the sets of candidate defects and available tests, and judiciously selecting the test sequence based upon the likelihood of various defects and the outcomes observed thus far. Unfortunately, in practice, analyzers do not always follow a systematic procedure to select tests, record outcomes, and eliminate defects. Diagnosis is often considered an art, and analyzers rely largely on intuition, some circuit knowledge, memory, and experience as they perform diagnosis.

## 2.2. Diagnosis decision support requirements

A purely manual diagnosis process can be both inefficient and error-prone especially when it is not supported by clear procedures and documentation. Empirical evidence 11,26,27 suggests that humans <sup>w</sup> <sup>x</sup> are not optimal diagnosticians since they have difficulty in effectively utilizing all the available information to systematically select the test sequence. For instance, using a static fault tree i.e., a predeter-Ž mined test sequence can result in unnecessary tests. and hence long diagnosis times relative to an approach that uses recent defect history to guide the search. Also, the informal approaches found in practice are not conducive to learning, transferring knowledge to other analyzers, or generating appropriate information for quality improvement.

Computer systems can assist diagnosis in various ways. At a basic level, they can serve as the repository for the necessary background information, e.g., the list and descriptions of possible defects, and outcomes of various tests for each defect. Computer systems can also provide on-line support by recording the successive test outcomes for each board, and automatically updating the candidate defect set and the available test set at each step. Advanced support might consist of proactive assistance during the diagnosis process such as suggesting the next test to apply, and dynamically acquiring knowledge when new defects are discovered or new tests are introduced. Some of these functions, e.g., the documentation and recording functions, ensure consistency among analyzers, improve diagnosis accuracy, permit verification by engineers, and promote learning. The pruning and test selection functions can reduce diagnosis time and decrease the number of iterations.

To be feasible and effective in practice, the diagnosis support system must meet the following key requirements.

<sup>.</sup> DeÕelopment time and cost: Given the short product life cycles of electronic products, the system must become operational quickly and without significant expense.

<sup>.</sup> Flexibility: The system must adapt easily and quickly to the frequent design and process changes that characterize the electronics industry. Preferably, the users themselves should be able to update the system rather than relying on external resources e.g.,Ž software experts and knowledge engineers ..

<sup>.</sup> Compatibility: To promote widespread use by technicians rather than being viewed as a threat to creativity, the system must be compatible with current practices. It should be easy to use and provide manual override options.

<sup>.</sup> Response time: Since each board requires several test iterations to prune the candidate defect set, the system must provide quick response to inputs and queries.

<sup>.</sup> EffectiÕeness: The system should help improve diagnosis productivity by reducing the time per test, the number of tests, and errors. Reducing diagnosis time produces direct cost savings fewer analyzersŽ and test equipment, and lower work-in-process plus. potentially much larger indirect savings due to quicker feedback for process control and improvement.

Other desirable system features include its ability to interface with existing databases, prepare periodic summary reports for process improvement, highlight inconsistencies, facilitate learning, and operate in multi-user environments.

## 3. The case-based approach for circuit diagnosis

## 3.1. Knowledge base for diagnosis

Circuit diagnosis relies on three broad classes of knowledge—historical, heuristic, and fundamental knowledge. Historical data such as prior information on the likelihood of defects can help the analyzer prioritize candidate defects, thus enabling an effective choice of test sequence. Heuristic knowledge refers to an empirical association between observed symptoms and diagnostic conclusions. This category might include rules and procedure that the analyzer has found to be effective after some troubleshooting experience. Fundamental knowledge refers to an understanding of the underlying physics of circuit elements which can be used to predict circuit response. Engineers rely on this type knowledge to design electronic circuits and develop tests.

Depending on the primary source of diagnostic knowledge, we can distinguish between experiencebased empirical knowledge and model-basedŽ . Ž . fundamental knowledge systems to support circuit diagnosis. The model-based approach uses an analytical model or a circuit simulator to dynamically identify the potential causes for the observed outcomes during the sequential testing process. Ref. 5<sup>w</sup> <sup>x</sup> illustrates the three basic steps—hypothesis generation, hypothesis testing, and hypothesis discrimination—in model-based diagnosis. Refs. 6,8,9 de-<sup>w</sup> <sup>x</sup> scribe various model-based systems to diagnose digi-

tal circuits. Model-based systems offer the advantage of directly integrating design and diagnosis: ideally, when the designer changes the circuit schematic, the diagnosis model is automatically updated, permitting instantaneous troubleshooting capability without requiring any human experience with the new circuit <sup>w</sup> <sup>x</sup> 4 . However, because they are very computationally intensive, model-based diagnostic systems are not well-suited for on-line applications. Furthermore, technical difficulties still remain in building suitable diagnostic models for analog circuits see, for exam- Ž ple, Refs. 1,13,29 due to bi-directional signal prop-<sup>w</sup> <sup>x</sup>. agation, and the impact of physical layout and tolerances on the performance of high speed radiofrequency circuits. Dealing with bridge defects and improper open connections also poses problemsŽ . since the basic circuit structure itself changes 24 .<sup>w</sup> <sup>x</sup> Rule-based systems, the most common experiencebased approach, rely on expert inputs to develop if-then rules that enable the system to reason about the behavior of the malfunctioning board. One of the pioneering applications of the rule-based approach was for medical diagnosis e.g., Ref. 10 . TheŽ <sup>w</sup> <sup>x</sup>. rule-based approach can deal with some of the complexities that model-based systems cannot handle, but conventional expert systems often require special expertise e.g., knowledge engineers and long de-Ž . velopment times 24 , especially for initial knowl-<sup>w</sup> <sup>x</sup> edge acquisition 20 . Also, unlike the field of<sup>w</sup> <sup>x</sup> medicine, electronic circuits and manufacturing processes vary widely, and the technologies undergo frequent and radical changes. So, rule-based circuit diagnosis systems are likely to require more customization and maintenance effort. In general, the literature on knowledge-based diagnostic systems focuses on knowledge representation issues and inference mechanisms, but does not adequately address issues of optimizing the sequential search process.

## 3.2. Application of case-based reasoning

The goal of our project was to develop and test a diagnostic support system that is viable in a practical manufacturing environment. Two observations regarding practice motivated our case-based approach. First, the ubiquitous 80–20 law applies also to electronic circuit diagnosis, i.e., less than 20% of all possible defects occur in over 80% of the defective boards. Fig. 1, showing the cumulative distribution of defects arranged in decreasing order of occur- Ž rence observed during the first few weeks of our . prototype implementation, illustrates this phenomenon. So, a system that can operate with incomplete knowledge, progressively adding defects as they are encountered, is preferable to enumerating, a priori, all possible defects. This strategy reduces development time and effort, improves response time Ž . by focusing on the most common defects , and makes the system more flexible to changes in product design.

Second, a simple way to learn from an expert analyzer is by recording the actions—the tests performed and their respective outcomes—as the analyzer explores and identifies a new defect. The observed test outcomes characterize the new defect, and also provide a convenient knowledge representation that facilitates system maintainability and communication among analyzers and engineers.

Case-based reasoning CBR originated in the Ž . area of legal argument. An early system, HYPO, in the domain of trade-secret law combines reasoning about the statutes rules with relevant precedentsŽ . Ž . cases . Legal argument continues to dominate the most recent case-based reasoning literature see, forŽ example, Ref. 25 . Applications of CBR to fault <sup>w</sup> <sup>x</sup>. diagnosis are limited. Ref. 14 applies CBR to<sup>w</sup> <sup>x</sup> robotic assembly cell diagnosis, and Ref. 12 pre-<sup>w</sup> <sup>x</sup> sents a generalized approach to case-based diagnosis using frame theory.

![](/api/attachments/UNEUU4Y8/fulltext/images/1af2de02bb41f7668dcc1cbba18c07e3d5478f8b70a0c3d365a1253cd7e535f9.jpg)  
Fig. 1. Distribution of actual board defects in electronics assembly plant.

For electronic circuit diagnosis, the case-based approach offers several important advantages. It requires much lower development time and effort compared to other approaches, is easy to update via incremental, on-line knowledge acquisition, and is compatible with current practices it is non-threaten-Ž ing because it relies on, rather than replaces, analyzers’ expertise for the diagnosis of new defects . We. enhance the conventional case-based approach by adding features to incorporate verification and updating steps to correct inconsistencies, distributed implementation in a client–server environment, and effective test sequencing to reduce the number of test iterations.

In the electronic circuit diagnosis context, a case is an instance of a diagnostic experience, represented by its test outcomes. A rule, by contrast, is aŽ generalization about diagnostic experience gathered over time. Each case represents a particular defect.. The case base consists of the collection of instances corresponding to different defects observed in the past. For a given defect, we refer to its set of expected outcomes for all available tests as the signature of that defect. Suppose we have identified n defect types and have available m tests to diagnose these defects. Let i<sup>s</sup>1, . . . ,n index the set of defect types, and j <sup>s</sup> 1, . . . , m index the tests. We visualize the case base as an n<sup>=</sup>m matrix all of whoseŽ elements might not be known , with row. i corresponding to defect i and column j to test j. For simplicity, we assume that each test has only two possible outcomes, which we denote as 0 and 1 Že.g., 0 might correspond to a particular voltage being less than 4.5 V, while 1 denotes a voltage greater than or equal to 4.5 V . This assumption is. valid for the particular application we studied, but the general approach applies even with more than two outcomes. We permit tests to have indeterminate Ž . or random outcomes for certain defects, e.g., for defect i, test j’s outcome might be either 0 or 1 depending on, say, the state of a flip-flop device. Furthermore, we permit incomplete knowledge, i.e., the outcome of a test for a particular defect might be unknown a priori. Accordingly, the jth element of the ith row in the case base has a 0, 1, R, or U depending on whether the expected outcome of test j for defect i is 0, 1, indeterminate, or unknown. The entire ith row represents the signature of the ith defect. As we explain later, the user can dynamically add rows cases and columns tests to the case baseŽ . Ž . as new defects are detected and diagnosed incre-Ž mental knowledge acquisition ..

## 3.3. Diagnosing a defectiÕe board: successiÕe refinement through case matching

Diagnosing a defective board corresponds to observing the board’s response to various tests while simultaneously searching the case base to identify matching cases whose test outcomes coincide with the board’s partial signature observed thus far. If no matching case is found, the board contains a new defect or the case base is inaccurate. In either situation, the case base must be updated to reflect this latest experience. The general case-based approach goes beyond case matching and database updating functions to possibly include reasoning and extrapolation. Our implementation does not exploit these additional capabilities. Fig. 2 shows the flow chart for our case-based circuit diagnosis support system Ž . CDSS . We first explain how the system operates before describing how to update the case base Sec-Ž tion 3.4 . Section 4 describes enhancements to im- . prove the system’s test sequencing capabilities.

At each stage of the search process, the system maintains: i aŽ . Ž . candidate defect set CDS consisting of all known defects whose signatures match the observed outcomes for all the tests performed thus far, and ii theŽ . Ž . aÕailable test set ATS containing all remaining tests whose outcomes differentiate one or more candidate defects from the others in the CDS. In the basic version of the case-based system, the analyzer chooses and applies a test from the ATS, observes the outcome of that test, and enters this information into the system. The system then automatically updates the CDS and ATS by:

<sup>Ø</sup> removing from the CDS all defects whose expected outcome for the latest test differs from the observed outcome. All defects whose outcome for this test is unknown or indeterminate are retained; and,

Table 1  
Complete case base for illustrative example

<table><tr><td></td><td>Test 1</td><td>Test 2</td><td>Test 3</td><td>Test 4</td></tr><tr><td>Defect 1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Defect 2</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Defect 3</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Defect 4</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Defect 5</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

<sup>Ø</sup> deleting from the ATS the test that was just performed as well as any other test whose outcome is the same or unknown or indeterminateŽ . for all the remaining defects in the updated CDS.

To illustrate this process, consider a simple circuit with five possible defect types e.g., each defect type Ž might represent a particular defect component and. four available tests that can identify these defects. Table 1 shows the case base containing the complete signatures for all five defects. This example does not have any indeterminate or unknown outcomes.

Suppose the analyzer selects tests in order of increasing index, and suppose a particular board contains defect 3. Table 2 traces the CDS and ATS at each stage.

At the end of the third iteration, the candidate defect set contains a single defect defect 3 , and theŽ . diagnosis process terminates. For this diagnostic instance, if we first applied test 2 instead of test 1, its 0 outcome automatically eliminates test 1 since all remaining candidate defects 1, 2, 3 have the same  4 outcome 0 for test 1. Applying test 3 next isolates defect 3.

This example illustrates the following characteristics of the sequential search procedure:

Ž . 1 Exploiting prior information: Suppose the likelihood of defect 3 is significantly higher than the other defects. Since tests 2 and 3 are adequate to isolate defect 3, applying these two tests first completes the diagnosis in only two iterations for our sample board. For complex circuits, this type of savings in number of tests can be significant. Section 4 discusses how to exploit historical and other prior knowledge to dynamically select an effective test sequence.

Ž . 2 Incomplete knowledge: The diagnosis process can terminate correctly even if we do not have complete knowledge about the expected outcome of each test for every defect. Consider, for instance, the incomplete case base shown in Table 3 containing several unknown outcomes U, but adequate knowledge to distinguish between the 5 defects.

Using this case base and our original test sequence, the diagnosis procedure to identify defect 3 requires four tests vs. three tests with complete Ž knowledge . Thus, although complete knowledge is. not essential for accurate diagnosis, it can accelerate the pruning process and reduce the number of tests. Also, after completing and validating the diagnosis, Ž . we can perform signature augmentation by updating some unknown entries in the case base with the actual observed outcome e.g., replaceŽ U with 0 for defect 3’s test 1 outcome ..

3.4. Updating the case base: incomplete knowledge and inaccuracies

Our discussion in Section 3.3 assumed that the case base is comprehensive i.e., it covers all possi-Ž ble defect types and accurate, the available test set. is adequate to isolate each defect, and the test outcomes are observed without error. If these conditions are not met, the testing process can terminate prematurely without a definitive diagnosis, and the analyzer needs to take some extraordinary actions such as repeating certain tests or performing additional tests. Next, we discuss possible premature stopping conditions, and the necessary follow-up actions.

Table 2  
Diagnostic process for illustrative example

<table><tr><td>Iteration number</td><td>Candidate defect set (CDS)</td><td>Available test set (ATS)</td><td>Selected test</td><td>Test outcome</td><td>Eliminated defect</td></tr><tr><td>1</td><td>{1, 2, 3, 4, 5}</td><td>{1, 2, 3, 4}</td><td>1</td><td>0</td><td>5</td></tr><tr><td>2</td><td>{1, 2, 3, 4}</td><td>{2, 3, 4}</td><td>2</td><td>0</td><td>4</td></tr><tr><td>3</td><td>{1, 2, 3}</td><td>{3, 4}</td><td>3</td><td>1</td><td>1, 2</td></tr><tr><td>4</td><td>{3} STOP</td><td></td><td></td><td></td><td></td></tr></table>

Table 3  
Incomplete case base for illustrative example

<table><tr><td></td><td>Test 1</td><td>Test 2</td><td>Test 3</td><td>Test 4</td></tr><tr><td>Defect 1</td><td>U</td><td>U</td><td>U</td><td>0</td></tr><tr><td>Defect 2</td><td>U</td><td>U</td><td>0</td><td>1</td></tr><tr><td>Defect 3</td><td>U</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Defect 4</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Defect 5</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

The regular diagnosis process might terminate abnormally for two reasons, as discussed below.

Ž .i The candidate defect set becomes empty, i.e., the observed test outcomes do not match the signature of any known defect. This situation could arise because:

Ž .a the board contains a new defect that had not occurred previously;

Ž . Ž . b a defect signature s recorded in the case base is inaccurate due to data entry errors, designŽ changes, etc. ; or, .

Ž .c one or more test measurements were erroneous.

If, after investigating this situation, the board is found to contain a known defect and the initial test measurements were re-validated, then this defect’s signature in the case base must be corrected Ž signature correction.. On the other hand, if the board contains a new defect, we must add a new case Žcase addition. containing the defect’s expected test outcomes, and some auxiliary information such as the name of the defect, who identified or approved the case, the corrective repair action required, and whoŽ . to notify for defect prevention. Although the existing tests might suffice to distinguish the new defect from previously known defects, the analyzer might also wish to add one or more new tests that can quickly isolate this defect.

![](/api/attachments/UNEUU4Y8/fulltext/images/1c8e8ce6a185d87c4a3aee9d2407b1a9aa28bede5ca25142c90c392789f15111.jpg)  
Fig. 2. Flow chart for case-based circuit diagnosis.

Ž . ii The aÕailable test set becomes empty, but the candidate defect set contains more than one possible defect. This stopping condition might arise due to erroneous test measurements, inaccurate defect signatures, or inadequate tests or known outcomes. Again, the analyzer must take extraordinary actions to verify the test measurements, check the defect signatures stored in the case base, complete the partial signatures of the remaining candidate defects, or add new tests Žtest addition) that distinguish between these defects.

Fig. 2 contains a flow chart summarizing the case matching and updating process. This process might include a defect Õerification step e.g., confirming Ž observed outcomes, applying additional confirmatory tests at the end of a successful diagnosis exercise.. This optional step is especially important after design changes and during production ramp-up when many new cases are added to the case base. During normal operation, defects are automatically verified if, after repairing the identified defect, the board passes the functional test; otherwise, more investigation is needed.

In summary, the case-based approach to support circuit diagnosis permits incremental, robust, and distributed knowledge acquisition. All cases have the same format, and contain information on the symptoms that the user identifies to be relevant in defining and distinguishing between defects. Because of this standardized format, the case base is easy to understand and update. The system begins with incomplete knowledge and sparse defect coverage, but each unsuccessful diagnosis initiates a process of case-building to ensure subsequent coverage of the same defect. The various correction and updating steps—signature augmentation, signature correction, case addition, and test addition—make the knowledge acquisition process robust and adaptive. The case-based system can be implemented using a shared relational database in a multi-user computing environment, thus providing wide access to analyzers, design and process engineers, and production supervisors possibly at different locations . IntegratingŽ . this system with other factory information systems facilitates communicating current production problems to the diagnosis operation, and feeding back defect information for quality improvement. The system can also keep track of cumulative defect frequencies that, as we discuss next, can serve to guide and optimize the sequential testing process.

## 4. Effective test sequencing

By systematically recording the outcomes and automating the updating functions, the basic circuit diagnosis support system CDSS reduces errors asŽ . well as the time to complete each test iteration e.g.,Ž to update the CDS and ATS . Decreasing the . number of test iterations provides another means to significantly reduce the total diagnosis time per board. As our example of Section 3 illustrates, the expected number of iterations depends on the test sequence. A principled test selection policy to decide, at each stage, which available test to apply next Ž . based on the observed outcomes thus far can reduce test iterations considerably. To formally define and understand the issues in test selection, we first present a dynamic programming formulation for the optimal test selection problem. We then outline some on-line heuristic rules that the CDSS can incorporate to reduce the expected number of tests. These rules rely on prior information concerning the likelihood of different defect types, estimated from historical yield data or based upon information about vendor or assembly problems, inputs from design engineers, and so on.

## 4.1. Optimal test selection

The test selection problem seeks an optimal or near-optimal testing policy that minimizes the expected number of test iterations to diagnose a malfunctioning board. More generally, we can associate a ‘cost’ for each test that can vary by test , andŽ . minimize the total expected cost to complete the diagnosis. We distinguish between dynamic and static policies. A dynamic policy selects the next test based on the previously observed test outcomes for the board currently being tested, while a static policy uses the same test sequence for all boards. Dynamic policies perform better i.e., they require fewer tests Ž on average since they use more information. The. optimization of sequential search processes has been previously modeled e.g., Ref. 18 , and applied to Ž <sup>w</sup> <sup>x</sup>. many domains e.g., to computer file search by Ref. Ž <sup>w</sup> <sup>x</sup> 17 . The reliability literature has also addressed. optimal sequencing issues, but only for certain special circuit and test structures e.g., Refs. 2,19 study Ž <sup>w</sup> <sup>x</sup> series systems with special test structures . This. stream of literature often assumes that all defect types and their probabilities are known and the requisite tests are available, without provisions for unknown or indeterminate outcomes. The knowledgebased diagnosis systems described in the literature do not appear to incorporate optimal search principles.

## 4.1.1. Dynamic programming formulation

This section presents a dynamic programming formulation to clarify the ingredients and tradeoffs in test selection during circuit diagnosis. As before, let n denote the number of candidate defect types, indexed from $i = 1 , \ldots , n ,$ , and let m denote the number of available tests, indexed from $j = 1 , \ldots , m$ . Let $c _ { j }$ be the cost of performing test $j .$ Setting this cost to the same value say, 1 for all tests corresponds to Ž . minimizing the expected number of tests. We assume, without loss of generality, that the case base contains all possible defect types. Otherwise, we can introduce a dummy defect type and a fictitious test with a 1 outcome if the board has this unidentified defect, and a 0 outcome for all other known defect types. We perform this fictitious test only when the set of known candidate defects is empty. For the discussion in this section, we assume that test outcomes are observed correctly, and the available tests can uniquely identify each defect.

Let B be the $n \times m$ matrix representing the case base, with elements $b _ { i j } = O , I ,$ R, or U, respectively, if the outcome of test j for defect i is $\theta , \ l ,$ indeterminate, or unknown. At any intermediate iteration of diagnosis process for a particular board, the state of knowledge about the board is characterized by the observed outcomes for the tests performed thus far. This knowledge is represented by a state Õector X whose elements $x _ { j } ,$ for $j = 1 , \ldots , m$ , are 0 or 1 if test $j$ has already been performed and its observed outcome was 0 or 1, or if test j has not yet been applied. Let DŽ . Ž . X and T X denote, respectively, the CDS and ATS corresponding to state X , i.e.,

$$
\begin{array}{l} \mathbf {D} (X) = \left\{i = 1, \dots , n: b _ {i j} = x _ {j} \text { or } R \text { or } U \text { for all } j \right. \\ \qquad \qquad \qquad \text { with } x _ {j} \neq \phi \}, \\ \text { and } \\ \mathbf {T} (X) = \left\{j = 1, \dots , m: b _ {i j} = 1 \text { and } b _ {i ^ {\prime} j} = 0 \text { for some } \right. \\ \qquad \qquad \qquad i, i ^ {\prime} \in \mathbf {D} (X) \} \end{array}
$$

Note that we delete from the CDS only those defects whose definite and known outcomes differ with the observed outcomes, i.e., defects with indeterminate or unknown outcomes for the applied test are retained in the CDS regardless of the actual outcome of that test.

The initial state vector $X ^ { 0 }$ has elements $x _ { j } ^ { 0 } = \phi$ for all $j = 1 , \ldots , m$ , with $\mathbf { D } ( X ) ^ { 0 } = \left\{ 1 , \ldots , n \right\}$ and $\mathbf { T } ( X ^ { 0 } ) = \left\{ 1 , \ldots , m \right\}$ . Starting with this initial state, the iterations of the diagnosis process correspond to moving from one state to the next until we reach a terminal state $X ^ { * }$ whose candidate defect set $\mathbf { D } ( X ^ { * } )$ contains only one defect. At any intermediate state $X .$ , we select and apply a test $j \in \mathbf { T } ( X )$ , observe its outcome $O _ { j } ~ ( = O ~ \mathrm { o r } ~ I )$ , and update the state vector $( \mathrm { i . e . }$ ., change $x _ { j }$ from to $O _ { j } )$

The expected number of tests to complete the diagnosis of a defective board depends on the probability of different defects and the testing policy we choose. Let $p _ { i } ^ { 0 } \geq 0$ denote the prior probability Žat the start of the diagnosis process that the board . contains defect i. As we apply tests and eliminate defects from the CDS, we must update the defect probabilities to reflect the observed test outcomes. Let $p _ { i } ( X )$ represent the conditional probability that the board contains defect i given that we are currently in state X. This value is given by:

$$
p _ {i} (\boldsymbol {X}) = 0 \quad \text { if } i \notin \mathbf {D} (\boldsymbol {X}), \text { and }
$$

$$
p _ {i} (\boldsymbol {X}) = \frac {p _ {i} ^ {0}}{\sum_ {h \in \mathbf {D} (\boldsymbol {X})} p _ {h} ^ {0}} \quad \text { if } i \in \mathbf {D} (\boldsymbol {X}).\tag{4.1}
$$

If we are currently in state X, the optimal test selection policy must choose the test $j \in \mathbf { T } ( X )$ that minimizes the expected cost-to-go of subsequent tests until the diagnosis process terminates. Suppose we apply test j next, and let D0, D1, DU, and DI represent the respective subsets of defects in DŽ . X whose anticipated outcomes for test j are 0, 1, indeterminate, or unknown these subsets depend onŽ the current state X and the test j, but we omit the arguments X and j for simplicity in notation . As- . sume for convenience that any defect whose outcome for test j is unknown or indeterminate is equally likely to give a 0 or 1 outcome we canŽ incorporate other probability values, if known . If. $q ( \mathbf { \boldsymbol { X } } , \mathbf { \boldsymbol { O } } _ { i } )$ denotes the probability that applying test j at state X results in outcome ${ \cal O } _ { j } \left( = 0 \ \mathrm { o r } \ I \right) .$ , then,

$$
\begin{array}{l} q \big (\boldsymbol {X}, O _ {j} = 0 \big) = \sum_ {i \in \mathrm{D} 0} p _ {i} (\boldsymbol {X}) \\ \qquad + \left\{0. 5 \sum_ {i \in \mathrm{DI} \cup \mathrm{DU}} p _ {i} (\boldsymbol {X}) \right\}, \end{array}\tag{4.2}
$$

and

$$
\begin{array}{l} q (X, O _ {j} = 1) = \sum_ {i \in \mathrm{D} 1} p _ {i} (X) \\ \qquad + \left\{0. 5 \sum_ {i \in \mathrm{DI} \cup \mathrm{DU}} p _ {i} (X) \right\}. \end{array}\tag{4.3}
$$

Using these probabilities, we can compute the expected cost-to-go from the current state X if we perform test j next, denoted as $C (  { \boldsymbol { X } } , j )$ , as follows:

$$
\begin{array}{c} C (\boldsymbol {X}, j) = c _ {j} + q \big (\boldsymbol {X}, O _ {j} = 0 \big) C ^ {*} \big (\boldsymbol {X} _ {j, 0} ^ {+} \big) \\ + q \big (\boldsymbol {X}, O _ {j} = 1 \big) C ^ {*} \big (\boldsymbol {X} _ {j, 1} ^ {+} \big) \end{array}\tag{4.4}
$$

where $X _ { j , 0 } ^ { + }$ and $X _ { j , l } ^ { + }$ denote, respectively, the next state withŽ $x _ { j } = 0$ .or 1 when the outcome $O _ { j }$ of test j is 0 or 1. Then, the minimum expected cost-to-go $C ^ { * } ( X )$ from state X is:

$$
C ^ {*} (X) = \min \left\{C (X, j): j \in \mathbf {T} (X) \right\}.\tag{4.5}
$$

Correspondingly, the best test to apply at state X is

$$
j ^ {*} (\boldsymbol {X}) = \arg \min \left\{C (\boldsymbol {X}, j): j \in \mathbf {T} (\boldsymbol {X}) \right\}.
$$

If X is a terminal state, i.e., DŽ . X contains exactly one defect, then we do not require any additional tests; hence, $C ^ { * } ( X ) = O \ \mathrm { i f } \ \left| \mathbf { D } ( X ) \right| = I ,$ where <sup><</sup> <sup><</sup> S represents the number of elements in set S. Eq. 4.5 with these initial conditions provide the Ž . dynamic programming recursion to compute the minimum cost-to-go and the optimal decision for every state X. This dynamic programming formulation of the sequential test selection problem can also accommodate precedence constraints e.g., testŽ j must precede test $j ^ { \prime }$ due to technological or operational constraints and probabilistic test outcomes..

The optimal testing policy found by the dynamic programming algorithm can be represented as a look-up table that specifies the best next test $j ^ { * } ( X )$ for every possible state X. In general, finding the optimal policy by solving the dynamic program can become very computationally intensive it is expo- Ž nential in the number of tests for complex circuits. . However, for certain special cases, the optimal testing strategy is easy to identify. For instance, suppose each defect i has a corresponding ‘focused’ test $j ( i )$ that produces a 1 outcome for that defect alone, and a 0 outcome for all other defects, i.e., the case base B is an identity matrix. Thus, applying test $\mathbf { \chi } _ { j } ( \mathbf { \chi } _ { i } )$ is necessary and sufficient to verify whether or not the board contains defect i. In this special case, the optimal testing strategy to minimize the expectedŽ number of tests consists of sorting the defects in. decreasing probability order, and applying the corresponding focused tests in this sequence. For more general cases, we next consider some on-line rules to heuristically select the test sequence.

## 4.2. Heuristic test selection rules

Easiest to implement are on-line rules that dynamically select the next test at each stage based on simple computations using information about the current state. Intuitively, the on-line rule must select a test that can rapidly prune the candidate defect set. We list below three illustrative rules that attempt to achieve this objective. We focus on minimizing the expected number of tests, but extensions to test-dependent costs are easy.

Highest failure rule: At each state X, this rule selects the test with the highest probability of failure, i.e., if outcome 1 denotes failure, select the test $j ( X ) = \arg$ max $\{ j \in \mathbf { { T } } ( X ) { : } q ( X , O _ { i } = 1 ) \}$ as the next test to apply. For the special case discussed in Ž Section 4.1 in which each defect. i has a corresponding focused test, this rule provides the highest optimal testing sequence.

Most known outcomes rule: A test that has unknown or indeterminate outcomes for many defects is relatively ineffective since these defects remain in the candidate set regardless of the test’s actual outcome. Hence, to rapidly eliminate candidate defects, the ‘most known outcomes’ rule selects the available test with the largest number of known outcomes for Ž the remaining candidate defects . To incorporate de- . fect probabilities, we might modify the rule to select the test with the lowest total probability of unknown and indeterminate outcomes.

Smallest expected remaining defects rule: To quickly prune the CDS, this rule selects the available test j with the smallest expected number of remaining defects, defined as the sum over the two outcomes $O _ { j } = O$ and 1 of the probability of obtaining outcome $O _ { j }$ times the number of remaining defects in the CDS if we observe outcome $O _ { j }$ . Observe that a test that with many unknown or indeterminate outcomes will have a large number of remaining defects for either outcome.

We might enhance these myopic rules to incorporate look-ahead features, accounting for the likely states two or more iterations hence. Alternatively, we might consider static rules that prioritize the tests before starting the diagnosis process; at every stage, the available test with the highest priority is applied next. Unlike the dynamic programming procedure, these heuristic rules do not guarantee optimality, i.e., in the long run, they might require more tests on average than the optimal policy. Their relative effectiveness depends on the nature and probability distribution of various defects, the test characteristics Ž . e.g., focused vs. joint tests , and the level of knowledge regarding test outcomes.

To assess the potential benefits of systematic test sequencing, we applied the three dynamic test selection rules and a static version of the third rule to a series of randomly-generated problem instances. The relative performance of these rules might be sensitive to various problem parameters such as the probabilities of different failures. To study these effects, we considered different scenarios by varying the following problem characteristics.

Ž .i the number of possible defect types,

Ž . ii the number of available tests,

Ž . Ž iii the density of the case base i.e., the fraction of known test results , and.

Ž . iv the shape of the defect probability distribution Že.g., a skewed distribution represents situations with a few commonly occurring defects and many rare defects; see Ref. 28 for more details .<sup>w</sup> <sup>x</sup> .

The values of these four parameters were chosen based on characteristics of real circuits. For each combination of parameters, we implemented a simulator that generates a random sequence of defective boards with the specified characteristics, and records the number of tests required to complete the diagnosis using each heuristic rule. The average number of tests over these problem instances estimates the expected number of tests required under each rule. A naive rule that randomly selects the next test at each stage provides a benchmark for comparison. We emphasize that this study was not meant to identify the best rule or evaluate the intuitive and informal rules that analyzers might already employ; rather, the main purpose was to verify the potential benefits of investigating and implementing principled test selection rules. Table 4 shows the various combinations of problem parameters we tested and the results of our computational experiments.

We summarize below some important conclusions from these simulations.

<sup>.</sup> Principled test sequencing can provide significant savings: even relatively simple dynamic test selection rules reduce the number of tests by 50% on average relative to random test sequencing, and 41% on average relative to the static rule.

<sup>.</sup> For the problem scenarios we tested, the dynamic rule D3 seems to be the most effective, although rule D2 performs better in some cases. Heuristics D1 and S1 performed uniformly worse. Additional development and more experimentation is needed to identify the best rule for each scenario.

<sup>.</sup> The number of tests performed decreases as the density of the case base increases. A denser case base i.e., fewer unknown and indeterminate out-Ž comes eliminates more defects at each stage since it. contains more information.

Table 4  
Comparison of test sequencing heuristics

<table><tr><td rowspan="2">No. of candidate defects</td><td rowspan="2">No. of available tests</td><td rowspan="2">Density of case base</td><td rowspan="2">Skewness of defect prob. distribution</td><td colspan="5"> $Average^a$ number of tests required using  $heuristic^b$ </td></tr><tr><td>D1</td><td>D2</td><td>D3</td><td>S1</td><td>R</td></tr><tr><td>40</td><td>20</td><td>0.3</td><td>High</td><td>19.23</td><td>18.36</td><td>18.31</td><td>19.38</td><td>19.47</td></tr><tr><td>40</td><td>20</td><td>0.6</td><td>High</td><td>10.41</td><td>8.83</td><td>8.90</td><td>11.68</td><td>12.73</td></tr><tr><td>40</td><td>20</td><td>0.9</td><td>High</td><td>8.06</td><td>6.66</td><td>4.78</td><td>7.34</td><td>7.73</td></tr><tr><td>40</td><td>20</td><td>0.3</td><td>Low</td><td>19.08</td><td>18.42</td><td>18.25</td><td>19.23</td><td>19.51</td></tr><tr><td>40</td><td>20</td><td>0.6</td><td>Low</td><td>10.39</td><td>9.08</td><td>8.15</td><td>11.12</td><td>12.53</td></tr><tr><td>40</td><td>20</td><td>0.9</td><td>Low</td><td>7.84</td><td>6.61</td><td>5.34</td><td>7.21</td><td>7.79</td></tr><tr><td>60</td><td>30</td><td>0.3</td><td>High</td><td>23.49</td><td>19.78</td><td>21.56</td><td>25.85</td><td>27.09</td></tr><tr><td>60</td><td>30</td><td>0.6</td><td>High</td><td>11.97</td><td>9.25</td><td>8.19</td><td>13.15</td><td>13.29</td></tr><tr><td>60</td><td>30</td><td>0.9</td><td>High</td><td>10.11</td><td>7.33</td><td>5.32</td><td>8.17</td><td>8.43</td></tr><tr><td>60</td><td>30</td><td>0.3</td><td>Low</td><td>24.64</td><td>21.99</td><td>22.13</td><td>25.87</td><td>26.90</td></tr><tr><td>60</td><td>30</td><td>0.6</td><td>Low</td><td>11.41</td><td>9.31</td><td>7.90</td><td>12.55</td><td>13.93</td></tr><tr><td>60</td><td>30</td><td>0.9</td><td>Low</td><td>12.28</td><td>6.19</td><td>4.84</td><td>6.33</td><td>7.07</td></tr><tr><td>100</td><td>50</td><td>0.3</td><td>High</td><td>23.58</td><td>19.19</td><td>20.96</td><td>30.57</td><td>32.59</td></tr><tr><td>100</td><td>50</td><td>0.6</td><td>High</td><td>15.05</td><td>9.96</td><td>8.59</td><td>14.63</td><td>15.00</td></tr><tr><td>100</td><td>50</td><td>0.9</td><td>High</td><td>13.18</td><td>8.32</td><td>5.97</td><td>8.82</td><td>9.39</td></tr><tr><td>100</td><td>50</td><td>0.3</td><td>Low</td><td>23.41</td><td>19.06</td><td>18.83</td><td>29.08</td><td>31.95</td></tr><tr><td>100</td><td>50</td><td>0.6</td><td>Low</td><td>13.83</td><td>9.93</td><td>8.64</td><td>13.87</td><td>15.01</td></tr><tr><td>100</td><td>50</td><td>0.9</td><td>Low</td><td>12.74</td><td>8.08</td><td>6.66</td><td>8.87</td><td>8.95</td></tr></table>

Averaged over 10 random problem instances.  
Numbers in bold represent lowest average number of tests among all methods.  
<sup>b</sup> Heuristics D1, D2, and D3 are dynamic test selection rules, Heuristic S1 is a static version of D3, and R is the random test selection rule.

<sup>.</sup> Problem size number of defect types and theŽ . skewness of the distribution of defect probabilities do not appear to have a significant impact on the relative performance of different heuristics.

## 5. Prototype system implementation and future directions

## 5.1. Features of CDSS prototype

We implemented and tested a prototype of the Circuit Diagnosis Support System CDSS in a pro-Ž . duction environment to diagnose actual printed circuit boards that failed in-line tests. The primary purpose of the implementation was to establish the viability of this concept, and understand human issues associated with introducing computer support tools in a predominantly manual diagnosis environment. The prototype was written in Omnis 5 for the Macintosh computers that the technicians use; these terminals use touch-screens, bar-code readers, mice, and keyboards as input devices. The Omnis program communicates via an SQL Standard Query Lan-Ž guage interface with a relational database. Ž . ORACLE on a central UNIX machine serving the facility. This central database stores and manipulates the case base, permitting multi-user access via a local network. The prototype system used only a simple decision rule the ‘most known outcomes’Ž rule to select the next test at each stage, and did not. incorporate the signature augmentation feature described in Section 3.

Observations and feedback from users over a five-week period led to several system improvements. The final version of the system employs a user-friendly interface that displays matching cases Ž . the candidate defect set and the outcomes of previous tests, and permits technicians to assess the usefulness of each available test in pruning the candidate defect set. Fig. 3 shows select screen displays for our prototype system—as the user initiates diagnosis of a new board Fig. 3a , reviews results duringŽ . an intermediate stage of testing Fig. 3b , and addsŽ . new cases Fig. 3c and tests Fig. 3d . Ž . Ž .

The system permits the user to override the automatic test selection procedure. The simplicity of the case-based approach, its transparent logic and operation, and the manual override option greatly facilitated the introduction and acceptance of the system in the existing environment.

The system was tested on a double-sided printed circuit board containing approximately 400 components, half analog radio frequency and half digital. Ž . Only part of the board was supported by the CDSS; the test circuit contains approximately 70 analog components. Over the course of five weeks, 467 boards were diagnosed using the prototype system; these boards had 87 different defect types involvingŽ 54 components, some of which had multiple defect types . We estimate that the average time to diagnose .

(a)  
![](/api/attachments/UNEUU4Y8/fulltext/images/7b86a9add835a3f94f41a0fd37a27ae700495558a8c285c950a03de110f12307.jpg)

(b)  
![](/api/attachments/UNEUU4Y8/fulltext/images/e9e8c6aa8bc4add332edf569fdb698620d6c63ab64535816804a10e5d9794861.jpg)  
The questions (tests) are listed in decreasing order of known outcomes. The notation “3/8" next to matching case 17 means that 3 out of the 8 known test outcomes for this defect match currently.  
Fig. 3. Sample screens from CDSS prototype. a Initiating diagnosis for a new board. b Intermediate stage of diagnosis process. c Ž . Ž . Ž . Adding a new case. d Adding a new test. Ž .

(c)  
![](/api/attachments/UNEUU4Y8/fulltext/images/a41ea73fbb05c312ab084e4eb36dd1eee4d404916e586a5699ea98dda254ae19.jpg)

(d)  
![](/api/attachments/UNEUU4Y8/fulltext/images/9c8a9230d97cfab51ad502e80c99471f1a72944a58fee85c71e00ca5cdea2d6c.jpg)  
Fig. 3 continued . Ž .

each board dropped from about 25 min per board for purely manual diagnosis to approximately 10 min with CDSS assistance. This estimate is based on anŽ informal observation for random boards rather than a rigorous time study. The system’s response time . was not adversely affected even after five weeks of case addition. For assembly contexts that require a significantly higher number of cases, we might consider limiting the number of cases that are stored; when the case base reaches this limit, an old case Ž . with the smallest current probability of occurrence must be discarded in order to add a new case. This strategy trades off the gain in response time per test iteration against the additional effort needed to relearn and update the case base if an old defect occurs again.

To evaluate the system’s learning rate, we measured the coÕerage of the system during each week of the trial period. Coverage is defined as the proportion of defects that is correctly diagnosed in a given Ž week using the current information in the case base.. Fig. 4 shows how the system’s coverage increased during the first five weeks of its operation. The case base initially contained cases corresponding to defects that the technicians felt were most likely or significant based on their experience . As Fig. 4Ž . shows, after 3 weeks of using the CDSS, 85% coverage was achieved for the test circuit; by the fifth week, coverage increased to 90%. Interestingly, during the first week of operation, the system could only diagnose about 17% of the defect types, suggesting that initial knowledge can be quite inadequate for this application. The CDSS’s rapid learning rate makes it especially attractive in today’s dynamic electronics assembly environment.

## 5.2. Managing the diagnosis function

Although the CDSS is effective and easy to use, exploiting its full potential requires appropriate management support. To rapidly develop full defect coverage, the system relies on its regular use by experienced technicians as they detect and diagnose new defects. However, as with many knowledge-based systems, experienced technicians are less likely to use the system because they might feel that they have less to learn and benefit from the system. Changing this behavior requires some fundamental changes in the way the diagnosis function is managed.

Technicians at the plant have traditionally been managed as hourly production workers despite their important role in the quality improvement loop and their high skill level. Emphasizing their contributions to defect prevention and process improvement, rather than viewing diagnosis as their sole function, can produce rapid progress towards world-class manufacturing standards. This shift in emphasis from fault finding to proactive process improvement requires changing the technicians’ performance evaluation metrics, providing appropriate incentives, and creating an environment that is conducive to learning and information sharing. Based on our experience with the prototype system, we suggest the following managerial changes to exploit the technicians’ skills.

Ž . 1 Redefine the technician’s job description and expectations: Technicians’ first priority must be defect prevention and process improvement. They are among the most skilled workers on the line, and are often the first to identify defects. Thus, they are better suited than design or process engineers whoŽ are typically less concerned with day-to-day operations to respond quickly to production problems..

Ž . 2 Measure quality as well as quantity: Traditional productivity metrics such as the number of boards diagnosed per month often produce adverse overall performance. For instance, technicians might tend to work on the ‘easy’ boards first, delaying attention to more critical quality problems. By emphasizing the quality of diagnosis the consequent process improvements can create a productive culture.

![](/api/attachments/UNEUU4Y8/fulltext/images/3dee8452df8d724dfaffc10869dd671faed52bfa6d277a7d9b9074c0d36ebadb.jpg)  
Fig. 4. Defect coverage and growth of CDSS during actual test.

Ž . 3 Introduce technical supervision through Master Technician. Traditionally, technicians report to the production supervisor who often does not have detailed technical knowledge about circuit behavior. Appointing a Master Technician to supervise the diagnosis<sup>r</sup>repair operations of multiple lines, if Ž available and provide consulting help to the techni-. cians can greatly improve productivity and professional satisfaction.

Ž . 4 Interact closely with product development. Closer cooperation with product development might be encouraged, for instance, through a rotation program or a career path from technician to development engineer.

We believe that electronics companies will be naturally driven towards these changes in order to cope with increasing product diversity and small-lot production.

## 5.3. Future directions

Our prototype implementation demonstrates that the case-based CDSS can be a very useful decision support tool for electronic board assembly operations. The prototype incorporates only certain basic features, but can be enhanced quite easily to incorporate more advanced capabilities. Potential enhance ments include: i permitting tests to have more thanŽ . two outcomes, ii providing defect validation andŽ . verification as an explicit feature, iii incorporatingŽ . automatic case base updating mechanisms such as signature augmentation, iv translating actual testŽ . measurements continuous values to corresponding Ž . discretized test outcomes, v minimizing the ex- Ž . pected testing cost per board when tests have different costs, vi accounting for precedence constraints Ž . and sequence-dependency among tests, and vii in-Ž . corporating more sophisticated test sequencing methods based on defect probabilities. These and other enhancements are possible even with current hardware, software, and development tools. Furthermore, the case-based approach offers two very promising possibilities in the future—integrating with a model-based approach, and adding automated probing capabilities.

Although the model-based approach can potentially provide seamless and instantaneous integration of the circuit design and diagnosis functions, the method is not suitable for real-time applications because of its extensive computational requirements. One promising approach is to combine the modelbased and case-based approaches in a hybrid system that captures the automatic reasoning capabilities of diagnostic models with the quick response of a case base that stores only the most important and relevant defects. The model-based approach can complement the case-based system in two ways: i whenever aŽ . new defect or new test is added to the case base, we can use the circuit model to verify the correctness of the partial signature specified by the analyzer orŽ obtained by recording the test outcomes which led to the new defect and even augment it i.e., replace. Ž unknown values in the case base with model-based predictions of test outcomes ; and, ii when the . Ž . case-based approach terminates with an empty candidate defect set, the circuit model can generate hypotheses regarding the new defect, and propose appropriate tests to isolate it. We can also apply the model-based system off-line to initialize the case base. Note that these schemes apply the circuit model only to resolve exceptions; hence, they do not degrade the average response time of the system during regular diagnosis. The hybrid approach decomposes the diagnosis function into its short-term and longterm components, thus permitting independent development of the case-based and model-based subsystems.

The second promising direction concerns the addition of automated probing capabilities to the CDSS. As printed circuit assemblies become smaller and more dense, automatic testing and probing will become a necessity. Most test equipment, such as power supplies, signal generators, and frequency analyzers, are already computer-controllable, but most diagnosis operations currently use manual probing. With the emergence of new high-precision robotic technologies incorporating vision and feedback con-Ž trol , automated flexible probing might become fea-. sible in regular manufacturing environments. A case-based system controlling the automatic circuit probing and measurement equipment can reduce diagnosis time by performing routine and repetitive diagnosis functions without human intervention; analyzers would still be required to troubleshoot new defects and resolve inconclusive diagnoses.

Computer assisted diagnosis is, of course, just one element of the overall testing and repair strategy. Formulating an effective test strategy requires considering many other tradeoffs and decisions, as enumerated below.

<sup>.</sup> How to incorporate diagnosis and testability issues in the product design process? Ref. 30 pre-<sup>w</sup> <sup>x</sup> sents a comprehensive survey of issues and methods relating to design for testability.

<sup>.</sup> Where to locate in-line test stations, and what tests to perform at each station? Ref. 22 discusses <sup>w</sup> <sup>x</sup> this issue in a generic production line setting, and Ref. 3 considers alternative in-line testing strategies <sup>w</sup> <sup>x</sup> for printed circuit board assembly operations.

<sup>.</sup> Whether to perform detailed, diagnostic tests in-line or off-line? This decision depends on the tradeoff between higher cycle times and test capacity requirements on the main assembly line vs. greater off-line effort.

<sup>.</sup> What tests to include in the test set for off-line diagnosis? Different tests partition the state space in different ways. The number and type of diagnostic tests that test engineers choose to implement influences the structure of the case base and hence the expected number of iterations to complete the diagnosis.

<sup>.</sup> When to stop the testing process for a board? For some defects, the cost to diagnose and repair the board might exceed the value of the board. When boards contain multiple defects, a common policy is to discard any board that goes through the diagnosis–repair loop more than a certain prespecified number of times. Conversely, analyzers might sometimes terminate the diagnosis process prematurely Ž . before conclusively proving a defect , and recommend repairing the most likely cause of the problem.

<sup>.</sup> How to screen boards that enter diagnosis? Refs. 15,21 discuss screening strategies to discard <sup>w</sup> <sup>x</sup> semiconductor wafers with low yield in order to avoid wasteful usage of the subsequent detailed wafer-probing capacity. Similar screening strategies might alleviate diagnosis bottlenecks in printed circuit board assembly.

As these issues illustrate, testing and diagnosis in printed circuit board assembly operations continues to offer many important and challenging research opportunities. Furthermore, the increasing volume of process data generated by placement, reflow, inspection, testing, diagnosis, and repair stations in today’s high volume electronics assembly environment presents fertile ground for developing proactive systems that systematically monitor and screen the process signals, recognize patterns, and anticipate problems.

## Acknowledgements

We are grateful to Brian Santoro, Thomas Babin, and Dennis Miller for initiating this project and providing constant support and encouragement. We thank the analyzers, especially Zakiuddin Mashood and Karl Browder, and members of the DOC team for sharing their insights on circuit diagnosis.

## References

<sup>w</sup> <sup>x</sup> 1 R.G. Bennetts, Introduction to Digital Board Testing, Crane Russak, 1981.

<sup>w</sup> <sup>x</sup> 2 D.A. Butler, G.J. Lieberman, Inspection policies for fault location, Operations Research 32 3 1984 566–574.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 P. Chevalier, Optimal inspection for circuit board assembly, Part II of PhD Thesis, Operations Research Center, Massachusetts Institute of Technology, Cambridge, MA, 1992.

<sup>w</sup> <sup>x</sup> 4 R. Davis, Diagnostic reasoning based on structure and behavior, Artificial Intelligence 24 1984 347–410.Ž .

<sup>w</sup> <sup>x</sup> 5 R. Davis, W.C. Hamscher, Model-based reasoning: troubleshooting, A.I. Memo No. 1059, Artificial Intelligence Laboratory, Massachusetts Institute of Technology, Cambridge, MA, 1988.

<sup>w</sup> <sup>x</sup> 6 J. de Kleer, B.C. Williams, Diagnosing multiple faults, Artificial Intelligence 32 1987 97–130.Ž .

<sup>w</sup> <sup>x</sup> 7 M. Garcia-Rubio, Key problems and solutions in electronics testing, in: J.A. Edosomwan, A. Ballakur Eds. , ProductivityŽ . and Quality Improvements in Electronics Assembly, Mc-Graw-Hill, New York, 1988.

<sup>w</sup> <sup>x</sup> 8 M.R. Gensereth, The use of design descriptions in automated diagnosis, Artificial Intelligence 24 1984 411–436.Ž .

<sup>w</sup> <sup>x</sup> 9 W.C. Hamscher, Model-based troubleshooting of digital systems, A.I. Technical Report No. 1074, Artificial Intelligence Laboratory, Massachusetts Institute of Technology, Cambridge, MA, 1988.

<sup>w</sup> <sup>x</sup> 10 P. Harmon, D. King, Artificial Intelligence in Business: Expert Systems, Wiley, New York, 1985.

<sup>w</sup> <sup>x</sup> 11 Henneman, Rouse, Measures of human problem solving performance in fault diagnosis tasks, IEEE Transactions on Systems, Man, Cybernetics SMC 14 1984 99–112.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 Y. Ishida, H. Tokumaru, A framework for case-based diagnosis—dynamic frame and reasoning on the representation, Transactions of the Society of Instrument and Control Engineers, Japan, 1990.

<sup>w</sup> <sup>x</sup> 13 J. Kritz, H. Sugaya, Knowledge-based testing and diagnosis of analog circuit boards, FTCS Digest of Papers, 16th Annual International Symposium on Fault-Tolerant Computing Systems, 1986, pp. 378–383.

<sup>w</sup> <sup>x</sup> 14 C.N. Lee, P. Liu, Case-based reasoning for robotic assembly cell diagnosis, Proceedings of the SPIE—The International Society for Optical Engineering, SPIE 1008 1988 241–246.Ž .

<sup>w</sup> <sup>x</sup> 15 M. Longtin, L.M. Wein, R. Welsch, Sequential screening in semiconductor manufacturing: II. Exploiting spatial dependence, Working Paper, Sloan School of Management, Massachusetts Institute of Technology, Cambridge, MA, 1992.

<sup>w</sup> <sup>x</sup> 16 C.M. Maunder, R.E. Tulloss, The Test Access Port and Boundary-Scan Architecture, IEEE Computer Society Press Tutorial, 1990.

<sup>w</sup> <sup>x</sup>17 J.C. Moore, W.B. Richmond, A.B. Whinston, A decision theoretic approach to file search, Computer Science in Economics and Management 1 1988 3–19. Ž .

<sup>w</sup> <sup>x</sup> 18 J.C. Moore, A.B. Whinston, A model of decision-making with sequential information-acquisition, Decision Support Systems 2 1986 285–307.Ž .

<sup>w</sup> <sup>x</sup> 19 J.A. Nachlas, S.R. Loney, B.A. Binney, Diagnostic-strategy selection for series systems, IEEE Transactions on Reliability 39 3 1990 273–279.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 M.A. Newstead, R. Pettipher, Knowledge acquisition for expert systems, Electrical Communication 60 1986 115–Ž . 121.

<sup>w</sup> <sup>x</sup> 21 J. Ou, L.M. Wein, Sequential screening in semiconductor manufacturing: I. Exploiting lot-to-lot variability, Working Paper, Sloan School of Management, Massachusetts Institute of Technology, Cambridge, MA, 1992.

<sup>w</sup> <sup>x</sup> 22 S. Pappu, S.C. Graves, A dual-ascent algorithm for determining the optimal testing strategy, unpublished manuscript, Massachusetts Institute of Technology, Cambridge, MA, 1992.

<sup>w</sup> <sup>x</sup> 23 R.P. Prasad, Surface mount technology: principles and practice, Van Nostrand-Reinhold, New York, 1989.

<sup>w</sup> <sup>x</sup> 24 C. Preist, B. Welham, Modelling bridge faults for diagnosis in electronic circuits, Working Notes of First International Workshop on Principles of Diagnosis, unpublished, Stanford University, Stanford, CA, 1990.

<sup>w</sup> <sup>x</sup> 25 E.L. Rissland, D.B. Skalak, Case-based reasoning in a rulegoverned domain, Proceedings—Fifth Conference on Artificial Intelligence Applications, IEEE, 1988.

<sup>w</sup> <sup>x</sup> 26 W.B. Rouse, N.M. Morris, Review and evaluation of empirical research in troubleshooting, Journal of the Human Factors Society 27 5 1985 1.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 W.B. Rouse, R.M. Hunt, Human problem solving in fault diagnosis tasks, Research Note 86-33, US Army Research Institute for the Behavioral and Social Sciences, 1986.

<sup>w</sup> <sup>x</sup> 28 T. Semmelbauer, A case-based approach for diagnosing failed printed circuit boards in manufacturing, unpublished thesis, Massachusetts Institute of Technology, Cambridge, MA, 1992.

<sup>w</sup> <sup>x</sup> 29 D.W. Tong, E. Walther, K.C. Zalondek, Diagnosing an analog feedback system using model-based reasoning, Artificial Intelligent Systems in Government, Proceedings of the IEEE, 1989.

<sup>w</sup> <sup>x</sup> 30 T.W. Williams, K.P. Parker, Design for testability—a survey, Proceedings of the IEEE 71 1 1983 98–112.Ž . Ž .

![](/api/attachments/UNEUU4Y8/fulltext/images/08ee15ae4a055c6afc2842cb50aaca9c77faf627352a96288bf4ab21d1abd1ed.jpg)

Dr. Anantaram Balakrishnan is the Mary Jean and Frank P. Smeal Professor of Management Science and Information Systems at Penn State University’s Smeal College of Business Administration. Dr. Balakrishnan has previously held faculty appointments at the Sloan School of Management, MIT and the Krannert Graduate School of Management, Purdue University. His research interests span operations research, manufacturing, information systems, and

telecommunications. He has worked closely with several manufacturing firms particularly in the electronics industry, and often collaborates on research with colleagues in other disciplines. One of his current interests is exploiting information technology to monitor, manage, and plan supply chain operations.

![](/api/attachments/UNEUU4Y8/fulltext/images/b960f462c02d5452ff515e3c76704201ffb15cc7b057bf38c62058da86cbeb35.jpg)

Mr. Thilo Semmelbauer graduated summa cum laude with a BA in computer science and electrical engineering from Dartmouth College, and earned Master of Science degrees in management and in electrical engineering as a graduate of MIT’s Leaders for Manufacturing Program. Mr. Semmelbauer is currently a manager at The Boston Consulting Group where he is involved in the firm’s high technology and e-commerce practices in the US and in Europe. Prior to 1996, Mr. Semmelbauer was involved in the launch of wireless data and cable data modem products at Motorola.
