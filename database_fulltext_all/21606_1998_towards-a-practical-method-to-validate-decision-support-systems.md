---
otero_id: 21606
otero_key: "4QQCSHJ3"
title: "Towards a practical method to validate decision support systems"
authors: "Denis Borenstein"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00046-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards a practical method to validate decision support systems

Denis Borenstein )

Escola de Administrac¸ao, Uni ˜ ˜Õersidade Federal do Rio Grande do Sul, AÕ. Joao Pessoa, 52-sala 11, Porto Alegre, RS, CEP 90040-000, Brazil

Accepted 29 July 1998

## Abstract

Validation is important to the decision-making success and to the continued use of a Decision Support System DSS .Ž . Without proper validation, DSSs may cause costly errors. However, little is known about available effective methods to validate such computer-based systems. In this paper a new method to validate DSS is presented. The approach combines several validation methods developed to validate Operations Research<sup>r</sup>Management Science ORŽ .<sup>r</sup>MS models and expert systems validation frameworks to define a practical guidance for the validation stage of the DSS development. A case study illustrates the effectiveness of the developed method. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Assessment; Decision support systems; Evaluation; Validation

## 1. Introduction

There is a general agreement in the literature about the need to validate complex model-based systems in order to ascertain what a system knows, knows incorrectly, or does not know 20 . Validation<sup>w</sup> <sup>x</sup> can be considered as a fundamental step for more scientific and effective computer based systems <sup>w</sup> <sup>x</sup> <sup>w x</sup> 18,19,22 . In the DSS field, Finlay 5 demonstrated the importance of validating DSS.

Validation of a DSS is defined by Finlay 5 as <sup>w</sup> <sup>x</sup> ‘‘the process of testing the agreements between behaviour of the DSS and that of the real world system being modeled.’’ As pointed out by Finlay, DSS validation is not concerned with proving that a DSS is a truthful representation of the real world—since this is impossible—but with demonstrating that the

DSS has appropriate underlying relationships to permit an acceptable representation.

Unfortunately, the literature on DSS validation is still scarce, possibly reflecting the difficulty of the issue. Very few model-based DSSs have been validated 6 . Much of the research focuses on DSS<sup>w</sup> <sup>x</sup> evaluation 7,13,28 . From this perspective, it is nec-<sup>w</sup> <sup>x</sup> essary to distinguish between the concepts Õalidation and eÕaluation. Validation is the process of defining whether the model behaviour represents the real world system in a particular problem domain. Validation has two dimensions—verification and substantiation 22 . Verification is defined as the ‘‘pro-<sup>w</sup> <sup>x</sup> cess of testing the extent to which a model has been faithful to its conception, whether or not it and its conception are valid’’ 18 . Substantiation is defined <sup>w</sup> <sup>x</sup> as ‘‘the demonstration that a computer model, within its domain of applicability, possesses a satisfactory range of accuracy consistent with the intended application of the model’’ 2 . Evaluation is defined as the<sup>w</sup> <sup>x</sup> process of assessing a software systems’ overall value 19 . Evaluation includes 9 : 1 verification,<sup>w</sup> <sup>x</sup> <sup>w x</sup> Ž . validation, and quality control of the usability of the model and its readiness for use; and 2 investiga-Ž . tions into the assumptions and limitations of the model, its appropriate uses, and why it produces the results it does. The focus of evaluation is on the software and the real-world. Thus, there is insufficient available experience and critical appraisal of experience to establish practical methods concerning DSS validation. However, as DSSs are computer systems, validation methods and techniques developed to other related computer-based models might logically supply a framework for DSS validation.

According to Finlay’s 5 definition, DSS valida-<sup>w</sup> <sup>x</sup> tion presents similar characteristics to validation of analytical and simulation models. As a consequence, software engineering and validation methods and techniques applied to OR<sup>r</sup>MS models 16 might<sup>w</sup> <sup>x</sup> offer frameworks for DSS validation. However, OR<sup>r</sup>MS validation methods provide very descriptive approaches of how to validate a computer based model 5,19 . Practical aspects involved in <sup>w</sup> <sup>x</sup> particular validation such as constraints cost and time andŽ . conditions are neglected. Consequently, it is very difficult to apply this or similar processes to complex and multi-model systems such as DSS.

The synergy between Expert Systems ES andŽ . DSS 1,12 suggests that the concepts and methods<sup>w</sup> <sup>x</sup> used to validate ES are useful to establish some possible practical approach for DSS validation. ES validation has been receiving a lot of attention in the literature, and several researchers have developed methods to validate such a technology 11,14,27 . <sup>w</sup> <sup>x</sup> However, despite the existence of a strong synergy, it is not possible to apply ES validation methods directly to DSS, since they have different objectives. ESs directly influence or make decisions while DSSs simply support decision making or have an indirect impact on decisions 20 .<sup>w</sup> <sup>x</sup>

While several proposals for validating OR<sup>r</sup>MS computer-based models and ESs have been published, none are targeted at the issues of developing a formal method to validate DSSs. The main objective of this work is to describe a practical and effective method to validate DSSs. It combines several OR<sup>r</sup>MS and ES formal validation methods described in the literature into the DSS development life cycle taking into account important practical aspects in any real world DSS validation—time and costs. Since a ‘good’ decision does not always result in ‘good’ consequences 21 , due to the dynamics of<sup>w</sup> <sup>x</sup> the real world, the main focus of the method is in the process of decision making rather than in the decision derived.

This paper does not intend to present a generic method that can be used in any DSS validation—that at the moment, due to the lack of experience on the subject, is nothing but a dream—but rather to present a possible path in the development of more formal and effective methods that can be applied by developers during DSS design and implementation.

This paper is organized as follows: firstly, the method developed is presented in detail. Next, a case study illustrates the effectiveness of the method, showing its strengths and weakness when applied in the validation of a particular DSS.

## 2. DSS validation method

The method developed in this work is based on past work presented both in OR<sup>r</sup>MS modeling validation approaches and ES validation frameworks. The approach is mainly based on O’Leary et al. 22<sup>w</sup> <sup>x</sup> and Preece’s 24 formal paradigm to validate Expert<sup>w</sup> <sup>x</sup> Systems, and directly applies several validation techniques developed to validate OR<sup>r</sup>MS models.

The validation method is by itself an evolutionary process based on three main principles as follows.

Ž . 1 Formal validation. The validation occurs within the DSS development life cycle.

Ž . 2 Prescriptive validation process. The validation process is designed to be performed under research constraints—namely cost and time.

Ž . 3 Qualitative-based validation. The process is mainly based on qualitative approaches to validation. Qualitative validation involves the subjective comparisons of performance. It is important to notice that this does not imply that such approaches are informal. It is possible to design highly formal qualitative validation 19 . Quantitative methods, despite their<sup>w</sup> <sup>x</sup> importance, are used at a lower scale. Quantitative tests require a number of observation and controlled data procedures that are beyond the time and cost constraints involved in the development of a multimodel DSS prototype. O’Leary et al. 22 and Preece<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 24 assert that the use of qualitative methods is more effective during a prototype development—where time and costs are more important factors than detailed data collection and analysis.

The validation process is explicitly incorporated into the development life-cycle of the DSS prototype under constrained resources—time and costs. A DSS is evaluated through a two-stage procedure—laboratory testing ensuring face validity, subsystems Ž ‘verification and validation’, and predictive validation , and field testing 22 . Fig. 1 shows the DSS. life-cycle model, with an emphasis on the validation process.

The validation process follows the cyclic strategy of prototyping methodology development. The twostage validation occurs iteratively throughout the system development. The results from any stage or Ž substage may require changes reformulations, re- . Ž design, and refinements in the prototype. Also, . whenever the prototype is modified or expanded the system must be re-evaluated.

The validation methodology can be further described as follows.

Laboratory testing. It involves the execution of laboratory experiments through the prototype development. These laboratory experiments take place in settings constructed by the development team for evaluating the DSS. Generally, these settings have no prior existence independent of the DSS’ validation. Some of these tests may involve potential users that will contribute to the validation through questionnaires and interviews. The following laboratory tests are specified in the validation approach.

Ž . A Face validation. The main objective of a face validation is to achieve consistency between the designer’s view and the potential user’s view of the problem in a timely and cost-effective way. More specifically, face validation ensures that ‘the formulated problem contains the entire actual problem and is sufficiently well structured that a credible solution can be derived before extensive and detailed software development proceeds’ 22 . The face valida-<sup>w</sup> <sup>x</sup> tion acts in the approach as a feedback mechanism for prototype refinement, reformulation, and revision.

Ž . ŽB Subsystem ‘Verification and Validation’ V& V . It consists of testing, verifying, and . <sup>r</sup>or validating the DSS modules one at a time as they are developed. The main objective is to guarantee the quality of each model in the sub-model component of the DSS. Like face validation, this step is concerned with the internal validity of the system. However, subsystem ‘V&V’ is much more focused on prototype’s details and specifics than face validation, and therefore has as its main function the identification of areas where the prototype needs further detailed development and<sup>r</sup>or revision. The first step of this subprocess is to divide the DSS into independent modules. Each module can be viewed as an input– output transformation device. Next, the performance of each subsystem is observed for a certain set of input data. As pointed out by O’Leary et al. 22 the<sup>w</sup> <sup>x</sup> module inputs should be typical of the subsystem domain, and the module outputs should be compared to actual data.

Ž . C Predictive validation. It consists of validating systems using laboratory test cases in which the results are known. A DSS is driven by past input data from the test cases, and its results are compared with corresponding known results.

![](/api/attachments/4QQCSHJ3/fulltext/images/c8021f24825b87b411752097d8b2cfd7fee17bfa97a5ff0cdae35e4a2a37027a.jpg)  
Fig. 1. IDSS life-cycle with emphasis on the validation process.

Ž . D User assessment. It can be defined as ‘the process by which interested parties who were not Ž involved in a model’s origins, development, and implementation can determine, with some level of . confidence, whether or not the model’s results can be used in decision-making’ 9 . The main objectives of<sup>w</sup> <sup>x</sup> the user assessment testing are as follows: 1 ToŽ . obtain a statement of the applicability of the system by possible users; 2 To assess the impact of the Ž . computational system’s assumptions, simplifications, methods, and generic structure from an independent source.

Field tests Õalidation. Field tests place a DSS in the field, and then seek to identify those performance errors that occur 19 . The advantages of the use of <sup>w</sup> <sup>x</sup> this kind of validation are well described in the literature see Gaschnig et al. 8 , O’Keefe et al. 19 ,Ž <sup>w x</sup> <sup>w</sup> <sup>x</sup> and Preece 24 . Miser and Quade 18 state that<sup>w</sup> <sup>x</sup>. <sup>w</sup> <sup>x</sup> field experiments are the most effective of all validity tests if a situation makes it possible field testsŽ can be quite expensive in some cases . In summary,. if a situation permits, a field testing validation of a computer based system is a very desirable step to take before a full implementation 18 .<sup>w</sup> <sup>x</sup>

There are two clear orders involved in the validation approach: 1 An internal order within the labo-Ž . ratory tests where predictive validation should only be executed after face validation and subsystems V&V have already been successfully carried out. Face validation and subsystems V&V can be applied without a specific order. User assessment must be carried out at last, after a successful predictive validation. 2 Only when the DSS has been internally Ž . verified by laboratory experiments should extensive field tests be carried out.

This order reflects cost and technical efficiencies. There is no sense in applying a field test, extremely expensive in terms of human and organizational resources, upon a system that has not already been at least internally verified.

## 3. A case study

This section describes the tests carried out to validate IDSSFLEX, a prototype Intelligent DSS for the evaluation and analysis of flexible manufacturing system FMS design configurations, developed by Ž . the author 4 . For more details about FMS see<sup>w</sup> <sup>x</sup> Grenwood 10 . The main objective of the computer<sup>w</sup> <sup>x</sup> system is to select a suitable FMS design alternative for a particular situation in the light of a variety of criteria, including tangible e.g., costs, lead-time Ž . and intangible e.g., manufacturing flexibility, manu-Ž facturing quality, technical and financial risks . In. addition to this main purpose the system has the following generic objectives:

<sup>Ø</sup> To help users understand the concepts involved in FMS, assisting them in assessing the effects of implementing such systems.

<sup>Ø</sup> To provide an instrument for the measurement of performance parameters, including strategic, financial and operational ones.

<sup>Ø</sup> To consider and evaluate the impact of several design criteria in a specific FMS design.

<sup>Ø</sup> To provide a common language for engineers and managers to use in the FMS design decision process.

<sup>Ø</sup> To allow design teams to examine the sensitivity of internal and external changes e.g., the intro- Ž duction of new products, increase in the capacity of a workstation, etc. ..

IDSSFLEX has the three common basic components found in DSS frameworks: User–System Interface, Data Subsystem and Model Subsystem. However, the computational implementation of the system is divided into six different modules. The decision to divide the system into six modules allows each module to be used in an individual way. In this sense, each module is a complete system by itself, and its use will only require the necessary input. Fig. 2 presents the architecture of IDSSFLEX.

User-interface module OODŽ . ESIGNFLEX . It is responsible for the definition of FMS scenarios. The module has graphical and interactive facilities, and menu-data driven dialogues that offer a friendly environment for the user to define all needed data to run the models currently existing in the DSS. This module is also responsible for the overall control of the DSS, accessing and changing information with other modules within the DSS.

The model subsystem. Composed of four models as follows: a A simulation model, called OOSŽ . IM-FLEX, in order to capture the nature of each FMS design configuration to be evaluated. b A strategicŽ . and financial performance measurement set of models for quantifying tangible and intangible aspects involved with FMS configurations. This module is a combination of different analytical models for the quantification of manufacturing costs and intangible factors, such as manufacturing flexibility and manufacturing quality, embedded in the simulation model. Ž . Ž . c A knowledge-based system KBS , called EX-PERTFLEX, to verify whether a specific FMS scenario meets the design requirements defined by the design team. If a problem is found, the system starts an ‘analysis–diagnosis–recommendation cycle’ in order to isolate the possible cause s of the design defi- Ž . ciency as well as propose changes to improve the performance of the FMS scenario. Briefly, this knowledge can be described as a set of facts, heuristics and assumptions applied by experienced FMS designers. d A multiple criteria decision model Ž . Ž . MCDM , called SCOREFLEX, in order to evaluate the verified FMS design configurations, defined as alternatives, using several criteria such as manufacturing costs, flexibility, quality, etc.

![](/api/attachments/4QQCSHJ3/fulltext/images/75afe571be9d6393272c3904c6d26dde3fe5521835719b40d0b1d639c9f7c49b.jpg)  
Fig. 2. IDSSFLEX architecture.

Data subsystem. This module contains all the information necessary to execute all submodels within IDSSFLEX as well as to store the results computed by them. The information is divided into two basic files: ‘Scenario Files’, which stores information related to any FMS scenario, and ‘Alternative File’, which store information related to FMS scenarios that have satisfied minimum design objectives defined by the design team.

Next, the validation process of IDSSFLEX is discussed in detail. The emphasis is on the tests carried out to determine the potential value of the proposed method.

## 3.1. Face Õalidation

The face validation of IDSSFLEX was carried out through workshops with the participation of Brazilian practitioners and academics involved in the design of FMS. The main objective of the workshops was to ensure that the FMS design problem was correctly identified and that the essential concepts were properly included.

In total, four two-fullday workshops were carried out. The total participation on these workshops was quite diverse with practitioners from more than six different firms, mainly from the batch engineering sector and academics from several research institutes, including universities and a technical institute. Additionally, the author had the opportunity to extend IDSSFLEX’s demonstration to two firms that apply advanced manufacturing technologies. The workshops had the following program: 1 FlexibleŽ . Manufacturing Systems: definition, principles, and examples; 2 FMS practical considerations: design,Ž . implementation and operation; 3 Current perfor- Ž . mance of implemented FMSs; 4 Presentation of theŽ . methodology developed to improve FMS Design; 5Ž . IDSSFLEX presentation; 6 IDSSF Ž . LEX demonstration —use of the system with a simple example. In this demonstration section of the workshop, the participants could navigate through the system without the author’s intervention in order to discover by themselves what is the set of functions available in the IDSS; 7 Discussions.Ž .

With the exception of the Knowledge-Based System see Fig. 2 , all modules were operational at theŽ . time of the workshops. Thus, the participants had a good perspective of IDSSFLEX as regards of its objective, its organization, and its functionality.

At the end of the workshops, questionnaires were administered to the participants in order to collect data to support the validation. The questionnaire acted as a formal instrument to measure the validity of the system. Appendix A presents the main concerns addressed by the questionnaire designed for IDSSFLEX validation. In total, 27 questionnaires were filled in by an estimated 50 participants.

The majority of the surveyed participants Ž . 88.99% reported that IDSSFLEX has a great potential as an effective prescriptive tool in real world FMS designs, due to the following aspects: a the Ž . ability of the system to capture different criteria involved in FMS design; b its integrated and sys-Ž . temic approach to FMS design; c the ‘user-Ž . centered’ perspective; d its didactic potential as aŽ . learning tool for FMS and application of OR<sup>r</sup>MS methods and techniques to the manufacturing area; and e its advanced modeling approach. The remain- Ž . ing participants believed that the system can be applicable but a more complete version and more user time is needed for a better idea of the abilities and limitations of the system. Nevertheless, all participants recognized the necessity of the use of a such prescriptive decision aid during the design stage of an FMS in order to avoid irrecoverable investments.

The participants also highlighted factors that should be addressed to increase the applicability of IDSSFLEX as follows: a The high cost of utilizationŽ . both in computer and designer team time; b TheŽ . extensive number of input data rendered some of them difficult to collect; and c A well-documentedŽ . on-line aid to assist users in the efficient utilization of the computational system.

In addition to the information gathered by the questionnaires a series of discussions took place during IDSSFLEX demonstration in certain cases,Ž the author had the opportunity to return to some companies to demonstrate the software for a group of engineers that have implemented small flexible manufacturing systems . During the software naviga- . tion, the participants were able to independently evaluate the consistency of the software. Thus, the participants were able to pinpoint inconsistencies and initiate dialogue concerning prototype revisions.

In summary, face validation permitted software system modification and expansion to better reflect experts’ solution procedures. Some of the revisions dealt with reformulating system concepts. For example, additional code was added to model different material handling systems, such as automated guided vehicles AGV and conveyors. Some revisions dealtŽ . with redesigning the user interface of the system. Some revisions dealt with expanding the problem domain. For example, the system was reformulated to include the modeling of assembly operations. Dialogue and revisions continued in this phase until it was generally agreed that the prototype was sufficiently well structured to permit a credible solution derivation.

## 3.2. Subsystem ‘Verification and Validation’ V&V( )

In order to verify the internal system structure and to guarantee subsystem accuracy, a subsystem V&V was carried out for each model module in the system. This validation process occurred in parallel with the development of each model within the IDSSFLEX development cycle. As soon as the model was sufficiently developed to be considered as an input–output device this validation took part. Just after being satisfactorily verified and validated, the model was integrated to IDSSFLEX.

The subdivision of the DSS into modules was immediate since IDSSFLEX has a highly modular architecture. Four basic modules were identified for subsystem V&V, as follows: simulation model, strategic and financial estimation models, decision analysis model and knowledge-based representation module. The verification and<sup>r</sup>or validation procedures used varied with the nature and objectives of each module. For the simulation module, a paired t-test was applied while for the remaining three modules predictive tests were used.

Table 1 presents an example of the comparison of the results obtained by OOSIMFLEX and SIMAN <sup>w</sup> <sup>x</sup> 23 , a well-known commercial simulation package, for one of the several manufacturing system examples analyzed. In total, five different manufacturing systems were used for the V&V of the simulation model 4 .<sup>w</sup> <sup>x</sup>

The computational implementation of the flexibility estimation model, cost estimation model and quality estimation model were verified—referring to build the system ‘right’—by running test cases and comparing the modules’ output with the output provided by Kochikar and Narendran 15 , Son 25 , and<sup>w x</sup> <sup>w x</sup> Son and Hsu 26 , respectively. So far, only minor discrepancies were identified for the computation of manufacturing quality, as a consequence of the use of different methods to generate normal random variables. As the differences were inferior to 5%, they were considered acceptable. In addition, for each module sensitivity analysis was performed by systematically changing the input variable values and parameters over a large range of interest and observing the effect upon module’s performance. This was done by running the models with extreme values of the parameters and comparing the solution set of decision variables and their values with the recommended solutions by theoretical issues and experts’ recommendations. Such analysis led to a better understanding of the model’s structure with respect to the real system.

Table 1  
Comparison general results SIMAN–OOSIMFLEX for an example

<table><tr><td>Performance measure</td><td>SIMAN</td><td>OOSIMFLEX</td></tr><tr><td>Lead-time</td><td>44.95 ± 1.75</td><td>42.82 ± 2.57</td></tr><tr><td>Total average in queue</td><td>43.85 ± 2.35</td><td>39.8 ± 2.00</td></tr><tr><td>Forklift moving loaded</td><td>0.75 ± 0.01</td><td>0.75 ± 0.03</td></tr><tr><td>Forklift moving empty</td><td>0.24 ± 0.02</td><td>0.23 ± 0.03</td></tr><tr><td>Average daily throughput</td><td>91.60 ± 1.89</td><td>91.40 ± 1.53</td></tr></table>

In order to validate SCOREFLEX, the MCDM model, the software was run with the decision problem ‘which car to buy’ considered in VISA’s 3<sup>w</sup> <sup>x</sup> manual. The results obtained with SCOREFLEX were identical to the ones obtained using VISA. Furthermore, during this validation it was possible to check the ability of SCOREFLEX to offer a good repertoire of facilities for a visual interactive analysis.

Extensive validation tests were carried out to insure EXPERTFLEX’s effectiveness. The system was validated in various ways. The content was validated by direct examination of the knowledge base by Brazilian manufacturing experts during the development of the system. Further, a series of test examples was created in order to validate and adjust the performance of the system. The models used varied greatly in size and complexity. After carrying out this validation process it was possible to affirm that EXPERTFLEX as it currently stands is a fairly robust system. Taking into account the scope of action of the prototype, the system presented a current level of expertise that is equivalent to an experienced human designer.

In summary, the process of making a V&V subsystem analysis identified only minor miscalculations in the prototype. The subsystems were then revised and corrected as appropriate. It was more important that this phase stimulated further thought about the models in development and additional refinement as necessary.

## 3.3. PredictiÕe Õalidation

The performance of IDSSFLEX was evaluated with input data from Melman and Livy 17 —a simple <sup>w</sup> <sup>x</sup> FMS design problem. The problem can be described as the selection of the ‘best’ material handling system for an initial design configuration composed of 12 cells and capable of producing three different parts. The FMS configuration selection must respect defined design objectives. As a starting point four different material handling system alternatives were proposed two having a conveyor, and two having aŽ trolley . The problem was then solved by IDSSF. LEX. IDSSFLEX successfully accomplished the task of supporting the decision process, selecting the configuration that not only met the stated production and financial objectives, but also featured the ‘best’ overall performance on a list of FMS design criteria that included flexibility, costs, technical performance and technological and operational risks. The FMS design criterion values were computed by the simulation module and the set of strategic and financial performance measurement models see Fig. 2 . TheŽ . final alternative selected by IDSSFLEX was the same defined by Melman and Livy 17 after practical<sup>w</sup> <sup>x</sup> experiments, demonstrating the ability of the DSS to produce the desired results. In the work of Borenstein 4 a complete description of the predictive <sup>w</sup> <sup>x</sup> experiment is presented.

With face validation, subsystem V&V and predictive validation, the prototype was sufficiently verified and substantiated to guarantee the DSS technical validity using concepts and terminology pre- Ž sented by Gass 9 . The DSS validation could then<sup>w</sup> <sup>x</sup>. proceed to the next step in the validation method— the user assessment.

## 3.4. User assessment

The user assessment validation consisted of a laboratory experiment in which the DSS’s output and solution process was directly compared with an expert assessor’s prediction and solution process. To simplify the experiments the same example applied in the predictive validation was used. The user assessment experiments consisted of the following steps.

Ž . 1 Problem explanation. In this step the FMS design problem analyzed in the predictive validation was set out and analyzed by the assessors’ analysis method. This step occurred at least 2 days before the remaining steps, giving the assessors time to think about the problem and solve it, applying their own solution process.

Ž . 2 IDSSFLEX demonstration. Consisted of the software system demonstration, emphasizing the prescriptive decision process. Certain individual modules received special attention during the demonstration, since not all assessors were confident of the range of models and techniques used in IDSSFLEX.

Ž . 3 Proposed problem solution using IDSSFLEX. This step was the user experiment tests core. It involved the practical use of IDSSFLEX by the assessor—with the author’s research support—in order to solve the problem proposed.

Ž .4 Assessors’ evaluation. In this step, the software evaluators and the author’s research analyzed IDSSFLEX both as a prescriptive decision aid and as a computer program. A questionnaire see AppendixŽ B was used to gather information about the asses-. sors’ evaluation.

Ten different experiments were conducted with the participation of 15 experienced manufacturing designers from industry and universities. The experiments took on average 18 h to solve the problem 10Ž of which were spent using IDSSFLEX.. In all the experiments, the experts initially picked up a different configuration applying their own design pro- Ž cess from the one selected by IDSSF. LEX. However, having explored the problem interactively with the software system, all the participants, in the 10 experiments, agreed that IDSSFLEX’s solution was the most appropriate for the proposed problem. There was a unanimous consensus of opinion that IDSS-FLEX improved the decision process for the problem by introducing ‘an FMS design method’ able to analyze and evaluate different system configurations in the light of several criteria. In addition, the assessors commented on the software system ability to stimulate, support, and suggest different courses of action in order to improve the FMS design process effectiveness. Borenstein 4 described in detail the<sup>w</sup> <sup>x</sup> experiments structure and the assessors’ impressions about the use of the system for a typical FMS design solution.

All the assessors were unanimous in recognizing IDSSFLEX as a valuable objective tool for the analysis and evaluation of FMS design. The main aspect cited by the assessors to justify this success is the introduction of a method able to capture all dimensions of FMS design problems. Additionally, the assessors have indicated the following strong points of the FMS design methodology<sup>r</sup>IDSSFLEX: a The Ž . FMS design methodology considers tangible and intangible factors such as manufacturing quality and flexibility, in an integrated perspective; b The inter-Ž . active and user-oriented way in which these factors are manipulated, as a result of a complete and complex analysis of individually complex elements; cŽ . The final decision is based upon a detailed analysis process in which the design team’s preferences and experience assume the very important role of ‘fitting’ the FMS to a certain firm’s characteristics; dŽ . The quantification of all factors involved in FMS design improves the design process, offering an objective and easily communicated language between all design team members.

This is ratified by the desire of 100% of the assessors to apply the system in future FMS design problems and<sup>r</sup>or to use IDSSFLEX as an instruction and training tool about FMS.

Notwithstanding, the assessors identified some aspects that restrict the software’s practical usefulness which deserved special as follows: i The complex-Ž . ity of the methodology and the information necessary to run the system calls for the participation of a senior designer in the design team; and ii enhance-Ž . ment of the knowledge-based system embedded in IDSSFLEX through future experimentation in order to increase the scope of utilization of the software system.

Based on the assessor’s comments and recommendations, it is possible to affirm that the IDSS-FLEX system is a practical and useful prescriptive decision aid with many desirable features to assist FMS designers in finding an overall effective design to obtain desired strategic, financial, and operational performance from an FMS.

## 3.5. Field tests

The main objective of the field tests was to simulate operational use of the system in situ. In the set of experiments performed we were attempting to test the system within a real environment, to identify needs for interface re-design, re-design of the analytical and simulation models, and additional knowledge acquisition.

IDSSFLEX was installed in two manufacturing companies in Brazil, both from the metal-mechanical sector. The computer system was undergoing in the field tests validation for around 1 year. During that time, the system was involved in the design of two flexible manufacturing cells and of an automated handing facility. Over 20 engineers and a number of specialists were exposed to it.

The first experiment—the design of a flexible manufacturing cell—led to a major redesign of the system, after which it was once again evaluated by the author. The second and third experiences were less dramatic, only minor alterations were necessary. Feedback from the users was elicited via the following methods:

<sup>Ø</sup> Comments obtained during the training period.

<sup>Ø</sup> Observations and comments on the system in use.

<sup>Ø</sup> Frequent meetings with expert designers.

<sup>Ø</sup> Application of questionnaires see Appendix C atŽ . the end of each design project.

Essentially, the field tests provided the following practical results in terms of improving IDSSFLEX as a computer system: i The ergonomic aspects of theŽ . system were greatly improved. Several problems were identified with the user interface that could be detected and corrected as several assessors used the system. ii Improvement of the analytical models ofŽ . IDSSFLEX. The quality and cost estimation models were the most benefited. The discrepancies between the practical results and the real values demanded a complete evaluation of the models. A set of experiments were then performed with the collaboration of graduate students and the companies’ engineers to define better estimations. More suitable models were then developed. iii Further knowledge about FMSŽ . design was elicited during the test cases, enhancing EXPERTFLEX’s performance.

As a whole, the users delivered an overall evaluation ‘ very positive’ for the system. The high costs involved in learning and using IDSSFLEX were counterbalanced with advantages by the reduction on the overall design costs, after the corrections resulting of the first test. The use of the system decreased the overall design time for the two subsequent tests from an average of 1 year to a 6-month period, reducing in more than 50% the design costs. In addition, the system improved the design process by introducing a complete scientific perspective to FMS design by the implementation of a methodology of analysis and evaluation. The system surmounted the limitations imposed by traditional analysis and evaluation of investment in flexible automation, based either on empiric factors or taking into consideration easily operational and financially measurable aspects.

In summary, the field tests were the most important validation experiments due to two aspects. First, the system was mainly tested without the intervention of the software developer with real cases. As a consequence, the frequent control bias exerted by developers by selecting tests cases as to guarantee good system performance was minimized. Second, the input domain of the validation process was expanded, enlarging the acceptable performance range of the prototype system to a reasonable set of application domain.

## 3.6. Conclusions from the case study

The case study revealed important information in the direction to evaluate the proposed methodology efficiency, effectiveness and usefulness. The first concern was the whole process efficiency. Considering the total time spent in a test as the sum of the time spent to elaborate the experiment, the time to collect the data the run the trials, the time spent to carry out the experiments, and the time spent to analyze the results, the time spent in validating IDSSFLEX was considerably long. The two major responsible factors in the process are as follows.

Ž . A Experiments definition. It was difficult to select suitable tests for certain validation steps. Questions such as ‘Are these tests powerful enough for my objectives?’, ‘May I replicate the experiment in order to check results?’, were important and difficult issues that make this process a very difficult task. As a result, a considerable period of time, well beyond the initial expectations, was spent in this activity.

Ž . B External assessors involvement. The difficulty to contact external assessors have created enormous time barriers in the validation process. The time needed to set up the experiments including avail-Ž ability of the assessors, the set up of the computers and the training time of the assessors , in certain. cases, was three or four times longer than the planned time. Little or nothing can be done to avoid such problems, unless the potential users are integral part of the software development. But, in this case, unwished biases can be introduced in the process of validation.

The validation process effectiveness was measured, subjectively, by the level of satisfaction of the same team of external assessors, composed of 10 experts, in the period between the face validation and the field tests in the validation process, using the same set of performance criteria for the software. Table 2 summarizes the relative effectiveness of the validation methodology based on the following software attributes: graphical modeling approach, integration of modules, presentation of results, manufacturing technology used, logical description, global efficiency and program consistency. The results show clearly how the validation method has improved the software performance and acceptability.

As expected, the most important point concerning the validation method effectiveness in the case study was the impossibility to apply extensive quantitative validation techniques. This fact reduced the significance, interpretability and testability of the measurements of the experiments. However, this limitation is typical of domains in which the outcome of the decisions supported by an DSS will not appear in 2 or 3 years.

Table 2  
Comparative assessors’ level of satisfaction with the software values in percentŽ .

<table><tr><td rowspan="2">Attribute</td><td colspan="4">After face validation</td><td colspan="4">After field tests</td></tr><tr><td>V. Good</td><td>Good</td><td>Fair</td><td>Poor</td><td>V. Good</td><td>Good</td><td>Fair</td><td>Poor</td></tr><tr><td>Graphical modeling</td><td>0</td><td>40</td><td>60</td><td>0</td><td>80</td><td>20</td><td>0</td><td>0</td></tr><tr><td>Integration of modules</td><td>0</td><td>40</td><td>40</td><td>20</td><td>60</td><td>40</td><td>0</td><td>0</td></tr><tr><td>Presentation of results</td><td>0</td><td>60</td><td>20</td><td>0</td><td>60</td><td>40</td><td>0</td><td>0</td></tr><tr><td>Manufacturing terminology</td><td>0</td><td>65</td><td>35</td><td>0</td><td>70</td><td>30</td><td>0</td><td>0</td></tr><tr><td>Logical description</td><td>0</td><td>60</td><td>40</td><td>0</td><td>50</td><td>40</td><td>10</td><td>0</td></tr><tr><td>Global efficiency</td><td>0</td><td>60</td><td>40</td><td>0</td><td>55</td><td>45</td><td>0</td><td>0</td></tr><tr><td>Program consistency</td><td>20</td><td>40</td><td>40</td><td>0</td><td>45</td><td>55</td><td>0</td><td>0</td></tr></table>

Even with the subjectivity of the data described in Table 2, the validation method used was highly beneficial in terms of validating IDSSFLEX. The integration of different quantitative and qualitative validation techniques and methods into a well described and practical method offered a helpful framework to validate a complex DSS. The validation method had fulfilled its objectives, detailing in which conditions the software can be used. Also, it offered a good understanding of the strengths and weakness of the computer-based system.

## 4. Conclusion and further research

In this paper a formal, qualitative and prescriptive method to validate model-based DSS is presented. The method combines OR<sup>r</sup>MS modeling validation techniques and expert systems validation frameworks to validate DSS. It also incorporates validation into the life time cycle of the DSS development, emphasizing important practical aspects within a validation process such as costs and time, offering an effective framework to DSS validation. A case study illustrates the applicability of the methodology for a particular and complex DSS validation.

Although the validation method accomplished its objective of establishing the level of credibility of the DSS evaluated in the light of its expected uses, the author realizes that the method is still a first attempt in the right direction. The following are the two issues that were raised during the case study that require a deeper analysis.

Ž . 1 Generality. The application field of DSS technology is vast and increasing as its effectiveness is proved. As a consequence, it is possible to argue whether a single validation method is able to cover the whole range of applications and situations. The answer is obviously no. Although any computer based system validation has the same objectives, there are intrinsic factors to each area of application that make impossible to define a single validation process. Nevertheless, the developed method presents generic ideas that can be used as guidance to any DSS validation process such as the integration of different validation techniques, including qualitative and quantitative methods, into one integrated, formal and prescriptive approach.

Ž . 2 Integration of quantitative validation. Gass 9<sup>w</sup> <sup>x</sup> and O’Keefe et al. 19 have demonstrated that quan-<sup>w</sup> <sup>x</sup> titative tests are essential for a more scientific validation process. However, as quantitative tests require a great number of observation and controlled data procedures, their expenses in terms of cost andŽ time can be extremely high. Thus, how to integrate. them into a practical validation process, respecting several time and costs constraints? This integration constitutes a very difficult challenge that requires ingenious solutions. The complexity of the problem increases when the DSS to be validated is an abstract representation of a nonexistent system, in which it is impossible to make assumptions about future responses.

Both issues are currently being addressed by the author and it will constitute subject of future research.

## Acknowledgements

The author likes to acknowledge the support of CNPq, Brazil, under grant 300102<sup>r</sup>97-6, and FAPERGS, RS, Brazil, Contract 96<sup>r</sup>1602.2. The author would also like to thank the anonymous referees and the area editor for their valuable comments and useful suggestions.

## Appendix A. Face validation questionnaire main topics

Ž . 1 Considering the FMS design methodology developed, what is your opinion on the potential of IDSSFLEX as an objective analysis and evaluation tool of FMS design configurations?

Ž . 2 In your opinion which are the strong points of the methodology<sup>r</sup>IDSSFLEX?

Ž . 3 The weak points?

Ž . 4 Although the system is focused on FMS design do you think that the methodology presented can be applied to the evaluation of advanced manufacturing systems other than FMS? Please justify your answer.

Ž . 5 Please comment on the following computational aspects of IDSSFLEX Žtick the appropriate response category :.

<table><tr><td>Aspect</td><td>Very Good</td><td>Good</td><td>Fair</td><td>Poor</td></tr><tr><td>Graphical modeling approach</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Integration of modules</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Presentation of results</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Manufacturing terminology used</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Logical description</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Global efficiency</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Program consistency</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Ž . 6 Based on your previous comments, how do you think it is possible to improve the IDSSFLEX software?

## Appendix B. User assessment questionnaire main topics

Besides the questions presented above, the user assessment questionnaire has incorporated the following questions.

Ž . 7 Do you believe that IDSSFLEX facilitated the decision process in the utilization example proposed as part of the validation session? Please give reasons for your answer:

Ž . 8 Would you apply the methodology<sup>r</sup>IDSSFLEX to solve further manufacturing design problems based on the experience gained through the example?

Ž. Yes

Ž. No

Please specify your reasons:

## Appendix C. Field tests questionnaire main topics

Besides the questions presented in Appendices A and B, the field tests questionnaire has included the following additional questions.

Ž . 9 List the advantages obtained through IDSS-FLEX utilization for the manufacturing system design:

Ž . 10 List any disadvantage of using the computer system:

Ž . 11 Evaluate the following IDSSFLEX modules and models:

<table><tr><td>Aspect</td><td>Very Good</td><td>Good</td><td>Fair</td><td>Poor</td></tr><tr><td>User interface</td><td>()</td><td>()</td><td>()</td><td>()</td></tr><tr><td>Simulation model</td><td>()</td><td>()</td><td>()</td><td>()</td></tr><tr><td>Quality estimation model</td><td>()</td><td>()</td><td>()</td><td>()</td></tr><tr><td>Flexibility estimation model</td><td>()</td><td>()</td><td>()</td><td>()</td></tr><tr><td>Costs estimation model</td><td>()</td><td>()</td><td>()</td><td>()</td></tr><tr><td>Knowledge-based system</td><td>()</td><td>()</td><td>()</td><td>()</td></tr><tr><td>Decision analysis model</td><td>()</td><td>()</td><td>()</td><td>()</td></tr></table>

Ž . 12 Please specify possible improvements for each module and<sup>r</sup>or model:

Ž . 13 Overall, how do you evaluate IDSSFLEX performance? Please justify your answer.

## References

<sup>w</sup> <sup>x</sup> 1 L. Alter, Decision Support Systems: Current Practices and Continuing Challenges, Addison-Wesley Publishing, Reading, MA, 1980.

<sup>w</sup> <sup>x</sup> 2 O. Balci, R.G. Sargent, A methodology for cost–risk analysis in the statistical validation of simulation models, Commun. ACM 24 11 1981 190–197.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 V. Belton, S.P. Vickers, VISA—Visual Interactive Sensitivity Analysis for Multiple Criteria Decision Aid, ver. 2.1 Ž . IBM PC , V. Belton and SPV Software Products, July 1993.

<sup>w</sup> <sup>x</sup> 4 D. Borenstein, Integrated Decision Support System for Flexible Manufacturing Design, PhD thesis, University of Strathclyde, Glasgow, Scotland, 1995.

<sup>w</sup> <sup>x</sup> 5 P. Finlay, Introducing Decision Support Systems, NCC Blackwell, Oxford, 1989.

<sup>w</sup> <sup>x</sup> 6 P.N. Finlay, J.M. Wilson, The paucity of model validation in operational research projects, J. Opl. Res. Soc. 38 4 1987 Ž . Ž . 303–308.

<sup>w</sup> <sup>x</sup> 7 C.L. Gardner, J.R. Marsden, D.E. Pingry, The design and use of laboratory experiments for DSS evaluation, Decision Support Systems 9 4 1993 369–379.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 J. Gaschnig, P. Klarh, H. Pople, E. Shortliffe, A. Terry, Evaluation of expert systems: issues and case studies, in: F. Hayes-Roth, D.A. Waterman, D.B. Lenat, Eds. , Building Ž . Expert Systems, Chap. 8, Vol. 1, Addison-Wesley, Reading, MA, 1983, pp. 241–278.

<sup>w</sup> <sup>x</sup> 9 S.I. Gass, Decision-aiding models: validation, assessment, and related issues for policy analysis, Operations Research 31 4 1983 603–631.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 N. Grenwood, Implementing Flexible Manufacturing Systems, Wiley, London, 1989.

<sup>w</sup> <sup>x</sup> 11 P. Grogono, A. Batarekh, A. Preece, R. Shingal, C. Suen, Expert system evaluation techniques: a selected bibliography, Expert Systems 8 4 1991 227–239.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 J.C. Henderson, Finding synergy between decision support systems and expert systems research, Decision Sciences 18 Ž . Ž .3 1987 333–349.

<sup>w</sup> <sup>x</sup> 13 C.L. Holsapple, A.B. Whinston Eds. , Recent Developments Ž . in Decision Support Systems, Springer-Verlag, Berlin, 1993.

<sup>w</sup> <sup>x</sup> 14 M. King, G.J. Phythian, Validating an expert support system for tender enquiry evaluation: a case study, J. Opl. Res. Soc. 43 3 1992 203–214.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 V.P. Kochikar, T.T. Narendran, A framework for assessing the flexibility of manufacturing systems, Int. J. Prod. Res. 30 Ž . Ž . 12 1992 2873–2895.

<sup>w</sup> <sup>x</sup> 16 M. Landry, K.L. Malouin, M. Oral, Model validation in operational research models, Eur. J. Opl. Res. 14 1983Ž . 207–220.

<sup>w</sup> <sup>x</sup> 17 M. Melman, M. Livy, Distributed system simulation of a flexible manufacturing system, in: Proceedings of JSST International Conference, Osaka, Japan, 1986, pp. 61–69.

<sup>w</sup> <sup>x</sup> 18 H.J. Miser, E.S. Quade, Validation, in: H.J. Miser, E.S. Quade Eds. , Handbook of System Analysis—Craft Issues Ž . and Procedural Choices, Wiley, UK, 1988.

<sup>w</sup> <sup>x</sup> 19 R.M. O’Keefe, O. Balci, E.P. Smith, Validating expert system performance, IEEE Expert 2 4 1987 81–90.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 D.E. O’Leary, Validation of expert systems—with application to auditing and accounting expert systems, Decision Sciences 1 3 1987 468–486.Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 D.E. O’Leary, Methods of validating expert systems, Interfaces 18 6 1988 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 T.J. O’Leary, M. Goul, K.E. Moffitt, A.E. Radwan, Validating expert systems, IEEE Expert 5 3 1990 51–58.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 D. Pedge, Introduction to SIMAM, Systems Modeling, January 1989.

<sup>w</sup> <sup>x</sup> 24 A.D. Preece, Towards a methodology for evaluating expert systems, Expert Systems 7 4 1990 215–223.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 Y.K. Son, A decision support system for manufacturing automation: a case study, Int. J. Prod. Res. 29 7 1991Ž . Ž . 1461–1473.

<sup>w</sup> <sup>x</sup> 26 Y.K. Son, L.-F. Hsu, A method of measuring quality costs, Int. J. Prod. Res. 29 9 1991 1785–1794.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 M.C. Sturman, G.T. Milkovich, Validating expert systems: a demonstration using personal choice expert, a flexible employee benefit system, Decision Sciences 26 1 1996 105–Ž . Ž . 118.

<sup>w</sup> <sup>x</sup> 28 P. Todd, I. Bensabat, The use of information in decision making: an experimental investigation of the impact of computer-based decision aids, MIS Quarterly 16 3 1992 373– Ž . Ž . 393.
