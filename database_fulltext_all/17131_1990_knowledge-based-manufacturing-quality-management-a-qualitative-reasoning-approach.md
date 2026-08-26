---
otero_id: 17131
otero_key: "4ZFHEVSQ"
title: "Knowledge-based manufacturing quality management: A qualitative reasoning approach"
authors: "Michael J. Shaw; Uday Menon"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90014-i"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge-based Manufacturing Quality Management: A Qualitative Reasoning Approach

Michael J. SHAW and Uday MENON

Department of Business Administration and Beckman Institute for Advanced Science and Technology, University of Illinois at Urbana-Champaign, Champaign, IL 61820, USA

Manufacturing fault diagnosis is the problem of determining the manufacturing fault(s) responsible for any critical dimensions or performance tests of the final assembly that fall outside their tolerance limits, as measured by on-line probes inserted at several chosen points of the assembly. An effective means for manufacturing fault diagnosis is crucial for controlling the quality of products rolling out of the manufacturing system. The current practice of this fault diagnosis process is to employ a computer-based information system to monitor the in-line testing results and have a diagnostic expert interpret the data when problematic measurements or performances are observed, so that any aberrations of the manufacturing system can be corrected. However, such an approach usually creates information overload and production-line disruptions, making the diagnostic task burdensome and prone to judgmental errors. The objective of this research is to automate the diagnostic process by an artificial intelligence (AI) approach. The approach is characterized as qualitative reasoning; it makes diagnostic decisions by “explaining” the undesirable test measurements and building causal links based on the qualitative model of the product assembly. We illustrate the fault-diagnosis approach by studying the quality management decision process of a torque-converter manufacturing system. Empirical manufacturing data is used to illustrate the procedure for validating the model.

Keywords: Qualitative Reasoning, An Expert System for Manufacturing Diagnosis, Inductive Learning for Model Validation, Manufacturing Quality Management.

## 1. Introduction

Manufacturing fault diagnosis is an integral part of the quality control process which ensures that product assemblies rolling out of the shop-floor meet design and performance standards. Even though individual parts that go into an assembly are subjected to in-line quality control and testing during the manufacturing process, performance testing on the final assembly is still required to ensure that the components are put together properly and that the final assembly meets the design specifications (Garvin [1988]).

Fault diagnosis in a mechanical assembly is constrained by the fact that relatively few components comprising the assembly are amenable to

![](/api/attachments/4ZFHEVSQ/fulltext/images/14f06a7d4f23e72d22ab0d1cfc42f115d576397d38355245305282e51c5e5e54.jpg)

Michael J. Shaw is an Associate Professor of Business Administration at the University of Illinois, Urbana-Champaign. He is also a faculty member of the Beckman Institute, a research center for the study of intelligence. His Ph.D. in Information Systems is from Purdue University. His current research interests are concerned with the applications of artificial intelligence to designing decision support and manufacturing information systems. He has published in the areas of knowledge-based scheduling, information systems, machine learning, distributed artificial intelligence, and intelligent manufacturing. A winner of Texas Instruments AAAI-87 and AAAI-88 paper competitions on advanced AI applications, Dr. Shaw is also a recipient of the Amoco Foundation Professorship (1985-88) and a Lilly Foundation Fellowship.

![](/api/attachments/4ZFHEVSQ/fulltext/images/01bb6195d25db436aa52dd2d56333ac3c55ed315bd4e6b08e8c583356f419e0f.jpg)

Uday Menon is currently a doctoral candidate in the Department of Business Administration at the University of Illinois at Urbana-Champaign. He received his B. Tech. in Mechanical Engineering (1977) from the Indian Institute of Technology, Kanpur, and his PGDM (1981) from the Indian Institute of Management, Calcutta. He worked in the production and machine tool maintenance divisions of a leading automobile manufacturer (TELCO, India) before taking up

product management and sales responsibilities (1981–86) at Grindwell Norton and Network respectively. Mr. Menon's research interests include the application of AI techniques to decision support systems and computer-integrated manufacturing.

performance monitoring, since most of the assembly is enclosed in some sort of housing, rendering the enclosed components inaccessible. Measurement probes are inserted at several chosen points which are accessible, and performance of the assembly is deemed satisfactory if the measurements recorded by these probes fall within specified tolerance limits. When an observed test parameter falls outside its tolerance limits, the observation is treated as a “symptom” of the possible manufacturing fault. The goal of the fault-diagnosis problem is to determine the faults responsible for a set of symptoms observed, so that any aberrations of the manufacturing system that cause the faults can be detected and corrected as soon as possible (Groover [1980], Pau [1986], Ranky [1986]).

The current practice of this fault diagnosis process in the manufacturing industry is to employ a computer-based information system to monitor the in-line testing results and have an expert make diagnostic decisions when undesirable measurements are found. In manufacturing systems producing a large volume of the final assembly, such an approach may create information overload, making the diagnostic task burdensome and prone to errors.

This paper describes an artificial intelligence method for automating manufacturing fault diagnosis. The major task of this method is to reason from behavior to structure. That is, given testing results observed from measurement probes, the method is aimed at determining the structural defect(s) responsible for the abnormal testing results.

The diagnostic method is characterized as qualitative reasoning because it reasons and explains the behavior of mechanical assemblies in qualitative terms, without invoking the mathematics of continuously varying quantities and differential equations in modeling the dynamic processes linking the faults to the symptoms. It can produce causal accounts of the underlying physical mechanisms within the assembly, thus providing an effective diagnostic tool.

The qualitative reasoning approach is based on a deep reasoning model: it incorporates a structural description of the mechanical assembly. By contrast, expert systems incorporating only shallow models make decisions directly from observed features of the presented situations without an understanding of the underlying structure. The expert systems surveyed in Pau [1986] are of this type. In performing manufacturing fault diagnosis, reasoning with deep models has these advantages: (1) The diagnosis system with deep models is capable of dealing with novel faults. Expert systems with shallow models can only handle anticipated faults with the heuristics incorporated; deep reasoning models explicitly represent the whole scope of the system under study, and are thus capable of reasoning with every type of problem scenario, including those not encountered before. (2) The diagnosis system with a deep model is easier to migrate from one manufacturing environment to another without the need for major modification. This is possible because of the separation of the causal model – the structural and behavioral descriptions of the assembly – from the diagnostic process. (3) It is easier to maintain since any changes in the design of the assembly can be made by simply modifying the structural description; by contrast, systems with shallow models need to re-examine all the diagnostic heuristics to accommodate the changes. (4) The diagnostic process can be more efficient when deep reasoning models are used because the system can use causal propagation to save searching time. Finally, (5) it is easier to validate the completeness and correctness of the diagnosis system with a deep model because of the modular representation of the structural and behavioral descriptions (table 1).

Comparisons Between Expert Systems for Manufacturing Fault Diagnosis Using Qualitative Reasoning (“Deep Model”) and Expert Systems with “Shallow Model.”

<table><tr><td></td><td>Qualitative Reasoning with Deep Models</td><td>Expert Systems with Shallow Models</td></tr><tr><td>Ability to Handle Novel Faults</td><td>Yes</td><td>No</td></tr><tr><td>System Independence &amp; Portability</td><td>Yes</td><td>No</td></tr><tr><td>Changing Designs</td><td>relatively easy</td><td>may involve significant amount of rule changes</td></tr><tr><td>Primary Reasoning Activities</td><td>causal propagation (envisionment)</td><td>searching for applicable rules</td></tr><tr><td>Representation Completeness</td><td>the complete scope of the model is explicit</td><td>difficult to test whether the rules are complete</td></tr></table>

The remaining part of this paper is organized as follows: Section 2 defines the qualitative reasoning approach to manufacturing fault diagnosis, introducing the step-by-step procedure; section 3 describes the torque-converter system as an example, formulating the qualitative causal model for the torque-converter assemblies; in section 4, the qualitative process is applied to a diagnostic example; finally, section 5 shows an empirical validation procedure using inductive learning to generate diagnostic rules from test data.

## 2. A Qualitative Reasoning Approach to Manufacturing Fault Diagnosis

## 2.1. Qualitative Physics

The study on qualitative reasoning to problem solving originates from the AI research work on qualitative physics (de Kleer and Brown [1985]), which aims at formalizing the common sense knowledge about the everyday physical world. This branch of AI research is motivated by man's ability to use intuition to reason about common physical processes without intensive mathematical calculations (Larkin et al. [1980]). By the same token, the researchers reasoned, it would be handy if an intelligent system could be equipped with the same type of capability for understanding physical processes. The understanding may be just qualitative, not as sophisticated as the solutions obtained from intensive calculations based on laws of physics. But the important point is that through such qualitative reasoning the intelligent system can obtain a useful estimation of the behavior of the physical process under study with relatively simple computation or reasoning. Such qualitative reasoning capability has been pointed out as an important design criterion for the next generation of expert systems (Bobrow [1985]).

The concept of “paths of causal interaction” is central to reasoning from structure and behavior of a physical system (Kuiper [1985], Iwasaki and Simon [1985]). Thus an effect that originates at some location in a device is transmitted through one or more paths of causal interaction, possibly undergoing a change of form in the process, before manifesting itself as a different effect at some other (physically or functionally removed) location.

The qualitative reasoning approaches developed to date have all assumed compositionality: the system under study is broken down into components. Each component has certain specified behavior, and the behavior of the system as a whole can be explained by each component's behavioral characteristics as well as the connections between the components. That is, the behavior of the system is derivable from the structure of the system. A physical process in this context is perceived as the aggregation of interactions between individual components, each with its own distinct behavior, that propagate in a cause-and-effect chain (Rieger and Grinsberg [1978]).

There have been a number of studies applying qualitative reasoning to diagnostic tasks, mostly in electrical circuit analysis (Davis [1985], Genesereth [1985], de Kleer [1985], Hofmann et al. [1986]). Our approach takes the view that a mechanical device or a manufacturing assembly, such as a torque converter, can be modeled as an interconnection of “components” and “conduits” through which “materials” flow. The corollary to this is that an effect originating at some part A in the device cannot manifest as an effect at some other part B in the assembly if there is no connecting path of interaction between A and B.

Fault diagnosis thus follows a causal reasoning process which essentially crosses previously built cause-and-effect bridges between the various parts in the assembly (Reiter [1987]). The aggregate behavior of the assembly can be described by tracing the behavior of individual parts through the cause-and-effect bridges or paths of causal interaction. Thus by observing local behavior at a preselected set of points in the assembly, it should be possible to make reasonable judgments of how the assembly as a whole is functioning. If the assembly is malfunctioning, one or more of the set of local behaviors that are being monitored must exhibit behavior that is symptomatic of the malfunction. Having detected a symptom (deviation from norm in local behavior at one or more of the preselected points), the causal reasoning process should be able to trace the symptom back to the source of the malfunction.

Unlike fault diagnosis in electrical circuits where testing of the output of individual components is possible even after they are assembled into the circuit (on a board), mechanical assemblies typically do not permit such unlimited component access, being enclosed in a housing that renders these components invisible to the outside. The behavior of individual components can therefore only be inferred from observing the overall behavior of the assembly, which is a set of measurements obtained from probes inserted at select accessible points in the assembly, and knowledge of the manner in which individual components interact with each other to influence this overall behavior (Becker and Bartlett [1988], Fink and Lusth [1987], Herbert and Williams [1987]).

Our approach bases the structural description of the assembly on the notion of paths of causal interaction which we call a schematic. The schematic of a mechanical assembly is a network representation of the interconnections between its parts (Murakami and Nakajima [1988]). Similar to the current flow in an electric circuit, one or more “materials” such as a fluid (characterized by its velocity of flow or pressure), a force, or torque, flow through the elements in the schematic. The structure of an individual part is described by a set of structural variables which characterize the part, i.e., they physically affect the material that flows through the part, possibly causing it to change in magnitude or form. The behavioral description of a part is encoded in a set of behavioral rules involving its structural variables and the material flowing through it. These rules specify how the mapping of input material to output takes place for various qualitative values of the structural variables. A step-by-step approach to building the requisite qualitative reasoning framework for manufacturing fault diagnosis is given in the following section.

## 2.2. Building the Qualitative Reasoning Framework

The qualitative reasoning approach to fault diagnosis entails the following:

(i) identifying a list of elements (parts) in the assembly that play a functional role in determining overall behavior;

(ii) categorizing these elements as Components if they change the form or magnitude of the material flowing through them, or as Conduits if they simply transfer material between

Components without changing any of its characteristics;

(iii) identifying the structural variables set for each element in (i) and their qualitative mappings. These are qualitative variables that can assume one of a usually small set of qualitative values. Each qualitative value represents a disjoint interval on the real line in that variable's quantitative space. Thus if the "normal" range (tolerance limits specified by the design) for a clearance between two adjacent parts in the device is [0.001" 0.004"], this entire interval is mapped onto a single value in qualitative space (Forbus [1985]), say [0]. Values below 0.001" could be mapped onto the value [-] while those above 0.004" onto the value [+]. In this way the entire set of possible values for this clearance are now represented by three qualitative values, [0], [-] and [+];

(iv) identifying the material(s) flowing through each element in (i) and the variable(s) characterizing this flow;

(v) linking the Components and Conduits in (ii) to form a schematic that depicts the material(s) flow through the assembly. Thus two elements in the schematic are connected, thus adjacent, only if they have a common material flowing from one to the other, i.e., the variable characterizing this flow is the same for both elements. This constitutes the structural description of the assembly;

(vi) evolving a set of behavioral rules for each element in the schematic. These rules are cast in terms of the element's structural variables set and the variables characterizing the material flowing into and out of it. Each rule describes how input material is transformed to output by that element for various qualitative value combinations of the structural and material flow variables. This constitutes the behavioral description for each element. A trace of the transformations undergone by the material(s) flowing through the different elements in the schematic constitutes aggregate behavior of the device.

Having put together an abstracted qualitative model of the mechanical device as described above, we now show how such a qualitative model can aid the reasoning process for manufacturing fault diagnosis.

![](/api/attachments/4ZFHEVSQ/fulltext/images/4a58e3cf4822a53bf71d577fce18d8919bd2299376a886b795237cbbd156bb11.jpg)  
Fig. 1. The Qualitative Reasoning Approach to Manufacturing Fault Diagnosis.

## 2.3. The Qualitative Reasoning Process for Manufacturing Fault Diagnosis

A failure in the functioning of a manufacturing assembly can manifest itself either as erroneous behavior or as a complete breakdown in function where no response to input is observed. The former is a malfunction failure type, which is more frequent and difficult to diagnose. Our concern in this paper is with addressing this problem.

The qualitative reasoning process takes observed assembly testing behavior (symptoms) as input and bases the diagnosis on this observed behavior. These symptoms are the data recorded by measurement probes inserted at accessible points in the assembly. Since these probes obtain a measure of the dynamic state of the assembly, the variables being measured are those that characterize material flow at chosen points in the assembly. The qualitative causal reasoning process for manufacturing diagnosis, summarized in fig. 1, may therefore be stated as:

## GIVEN

(i) Structural knowledge of variables that characterize the elements in a manufacturing assembly and the paths of material flow between these elements (paths of causal interaction) described by a network of interconnections called the schematic;

(ii) Behavioral knowledge of how these structural variables interact to influence the transformation of incoming material to output, for each element in the assembly;

(iii) Performance measurements, which are stated by qualitative variables characterizing material flow at several fixed points in the assembly;

DETERMINE

(i) A set of qualitative values for the structural variables that is consistent with observed values for material flow.

(ii) The malfunctioning component(s).

The source of the observed malfunction is determined by searching for the element (or elements if more than one is involved) whose struct-

![](/api/attachments/4ZFHEVSQ/fulltext/images/72d1bc64a6525c17fc50f7f3632e4d875556929b46b3b5361118dfe177cb56ed.jpg)  
Note: Given observed values for test parameters
[T1 T2 T3 T4 T5] = [0 - + + 0],
the qualitative reasoning process concludes that
Malfunction Component = { C2 }

Fig. 2. An Example of the Qualitative Reasoning Process.

ural variable(s) are assigned qualitative values that connote deviations from norm, i.e., variables which have a $[-]$ or $[+]$ value assigned by the reasoning process. The solution to the qualitative causal reasoning problem involves an envisionment process (de Kleer and Brown [1982], Forbus [1985], Kuipers [1986]) in which a qualitative simulation of the behavior of the device is carried out using the behavioral rules.

This envisionment process traces the changes that take place in material flow through the schematic. As an example, fig. 2 shows a simple graphic representation of a qualitative reasoning process, in which test parameter probes, [T1, T2, T3, T4, T5] = [0, -, +, +, 0], measure the qualitative values of material flow at certain chosen points in the assembly. Using these qualitative values for the performance measurements as input, the reasoning process attempts to inject deviations at the exit of one or more components which will explain the observed values for T1–T5 by having the envisionment process start at the origin of a deviation and end up predicting values for T1–T5 that match observed values. The system finds that a malfunction in component C2 can “explain” the observed values for T1, T2, T3, T4 and T5 since the deviations injected at the exit of C2 propagate as shown in the figure. (Note that behavior rules are omitted in this example.) The system therefore returns {C2} as the location of malfunction in the assembly. More detailed description of the reasoning process and causal propagations using the behavioral rules will be presented in Section 2.4 and 2.5.

Owing to the nature of the diagnosis problem domain, we are interested only in the steady state behavior of the assembly and do not concern ourselves with transient states that the assembly may assume in its transition to the steady state. Thus rates of change (first derivatives) of material flow variables do not enter the behavioral rules. The reasoning process is concerned with finding a set of exit flow deviations (i.e., deviations introduced to the values of flows at the exit of a set of components) that will result in values for the test parameters consistent with what is observed. The set of components thus found (this set would contain one or more elements in it) represent the source(s) of malfunction observed. Using a generate and test procedure, the reasoning process first identifies a candidate list of components which may be responsible for the observed device behavior. These candidates represent alternate hypotheses which are then tested, one at a time, using the envisionment process. A description of how hypotheses are generated and tested follows.

## 2.4. Building Dependency Lists and Generating Hypothesis

Under assumptions of normalcy, if all structural variables have design specified values, i.e., a qualitative value of [0] in our notation, it must be true that all material flow variables also have design specified values, i.e., [0]. In other words, if all elements in the assembly meet design standards, then the assembly as a whole must perform to the standards laid down. As a corollary to this, if any subset of material flow values shows deviations from normal, i.e., they have qualitative values of $[-]$ or $[+]$ , this must have been caused by $[-]$ or $[+]$ values for structural variables of one or more elements in the assembly. The space of all combinations of deviations possible in structural variables can be too large to enumerate. However at this point we resort to a heuristic for guidance in managing this space, viz. the single-fault hypothesis. Since most assembly malfunctions in practice are caused by a failure in one element, it is not unreasonable to make this assumption at the start of the diagnosis process. If no single element is found to be consistent with the observed material flow values then we can relax this assumption and look for multiple causes of malfunction.

Using the “single-fault” hypothesis as the basis, the system is run with deviations ( $[-]$ or $[+]$ ) introduced in the structural variable set of each component/conduit, one at a time. Rather than introduce deviations in all structural variables, only those that have been known to go wrong are considered. For each such run, a list of test parameters (material flow variables) which have their values affected (changed from $[0]$ to $[-]$ or $[+]$ ) is compiled. When all simulation runs are completed, separate dependency lists are created, two for each test parameter, one specifying Components/Conduits that resulted in changing the value from $[0]$ to $[+]$ , and the other for the $[0]$ to $[-]$ change. These dependency lists constitute overall behavioral knowledge about the assembly, generated by chaining through the behavioral rules of individual elements. The purpose of generating and storing these dependency lists is to minimize repetitive traversal along paths in the schematic expected to be used frequently.

Another perhaps more efficient use of these lists is in creating a shortlist of elements that are likely sources of assembly malfunctions. This is done by forming a list of those elements that are common to all dependency lists associated with observed material flow values. For example, if material flow variables V1, V3 and V4 are observed to have $[-]$ , $[+]$ and $[+]$ values respectively (all other test parameters are assumed to be normal, i.e. [0]), the dependency lists corresponding to $[-]$ value for V1, $[+]$ value for V3 and $[+]$ value for V4 are retrieved and elements common to all these three lists comprise the candidate shortlist. The underlying assumption here is again the single-fault hypothesis. This is akin to the candidate generation procedure described in Davis [1983].

## 2.5. Envisionment

Envisionment is the process of predicting overall device behavior (i.e., the operational performance of the assembly) by propagating a given set of local behaviors through the schematic with the help of behavioral rules. Envisionment is the system's way of answering what-if questions about the effect of the state of the component (local behavior) on the overall behavior of the assembly. Each component has a normal state associated with it which in structural terms implies that all the structural variables characterizing the component conform to design specifications. If however one or more of these structural variables is outside tolerance specifications, the value of the material flow at the exit of this component would no longer conform to design specifications. The envisionment process traces the effect of this deviation in value of material flow by chaining through the behavioral rules of components/conduits that lie in the path of this material flow after it leaves the component. In a sense, the envisionment process is a simulation mechanism which helps envision the effects of causal propagation.

For each candidate element in the list, a deviation is introduced in the material flow value at the output end of the element and this effect is propagated through the schematic using behavioral rules.

By creating a deviation in the material flow value at the output end, we are implicitly making the assumption that the candidate element is the source of the assembly malfunction. Propagation via behavioral rules determines a predicted value set for the material flow variables (test parameters). This predicted value set is now compared with the observed value set (obtained from probes inserted into a real physical device). If the two sets match, the candidate element is diagnosed to be the source of the assembly malfunction. If the two sets do not match, the hypothesis that the candidate element is a likely source of device malfunction is rejected and the envisionment process is repeated with the next candidate in the shortlist.

Appendix A provides a summary of the qualitative causal reasoning process in fault diagnosis.

## 3. Fault Diagnosis for a Torque Converter System: A Case Study

## 3.1. A DSS for Monitoring Manufacturing Quality

We use a manufacturing quality system at a manufacturing plant as the testing ground for our fault diagnosis approach. The facilities in the plant rely on a computerized system for quality control and testing – referred to as the quality information system (QIS) – that keeps track of in-line test data for each component as it is put through the various manufacturing processes. This QIS data is used to provide feedback for process control and also serves as a historical record of an individual component's quality information.

One of the several product lines monitored by QIS is the Torque Convertor (TC) assembly, which is part of a vehicle's power transmission system. The function of a TC is to transmit power, from the vehicle's engine to the output shaft and on to the wheels, at varying output torque levels to match load requirements. A more detailed description of the TC is contained in Appendix B.

An effective fault diagnosis method for better quality management of the TC line is important because the cost of correcting faults in an assembled TC is high, in terms of the resources required to dismantle and put together the more than 60 parts that go into a TC. Currently, QIS maintains data obtained from performance tests carried out on TC assemblies. These data are used by the

DATE RANGE: 20500 TO: 21000  
![](/api/attachments/4ZFHEVSQ/fulltext/images/5836f6498dc5924922445e3222e6e3d071bf0fa8754993f59e4ef94809af53ee.jpg)  
Fig. 3. The Quality Statistical Reports Generated.

diagnostic experts in deciding the location and nature of faults in "failed" TC's. QIS can provide statistical data on a variety of test parameters such as torque absorption (input torque), stall torque ratio (ratio of input torque to output torque at stall), and efficiency (output horsepower/input horsepower) for torque converters. QIS passes or fails torque converters based on established maximum or minimum values for these test parameters. Currently curves and data are reviewed on a regular basis to determine if there has been a significant shift in the data from the established nominal curve. If the shift is proved to be detrimental to the use of the torque converter then the problem area must be determined online. This is the fault-diagnosis problem dealt with in this paper.

Fig. 3 and 4 show examples of the kinds of statistical reports and curves generated by QIS on such test parameters as Input Torque and Leak (the amount of fluid escaping the main fluid circuit). When a significant shift in the data is detected, the line operator first makes sure it is not a measurement error; the diagnostic expert is then called upon to pinpoint the source of the malfunction based on the test data.

![](/api/attachments/4ZFHEVSQ/fulltext/images/6f05815a843dc4649b2dea9d34ffc0a9f0738d5ffcc3c3027008c3c2bbdf7157.jpg)

![](/api/attachments/4ZFHEVSQ/fulltext/images/9e0d5aa15fb1a20eeb6a1298c69ecd46f63ac02b15b8689cc50198f6d1f1b293.jpg)

![](/api/attachments/4ZFHEVSQ/fulltext/images/af5ea438f334534727e8f291a41c6bf505ccd3e8688e18bfd807420c81397d04.jpg)  
Fig. 4. The Sample Data Curves Displayed by QIS.

This diagnostic process can be improved by an AI-based expert system. Instead of calling upon the diagnostic expert, the line operator can key in the performance data of the problematic assembly and then through a sequence of question-and-answer interactions referred to as the consultation process, the expert system will make a diagnosis about the likely source of malfunction. Appendix C shows examples of diagnoses made by a prototype expert system that we have built for the TC. In contrast with the statistical data (Figs. 3 and 4) currently generated by QIS, the information provided by such a diagnostic expert system is clearly less susceptible to judgmental errors.

The qualitative reasoning approach described in section 2 is applied to incorporate a deep model in the expert system. This requires building a qualitative causal model that includes the structure and behavior descriptions of the torque converter assembly, as explained in the following section.

## 3.2. A Qualitative Causal Model for the Torque Converter

Ignoring the bolts, washers and other relatively unimportant items in the parts list that accompanies the TC sectional view, fig. 5 illustrates the schematic showing interconnections between these elements and the material(s) flowing through the schematic. The corresponding parts are explained in table 2.

The torque converter is characterized by a complex set of quantitative equations (for details see Larew [1968]) specifying fluid flow velocities at the entrance and exit points of the impeller, turbine and stator. These velocities are functions of blade angles, clearances between impeller, turbine and stator, the cross-sectional areas of flow compartments formed by the vanes, and the geometry of the flow path (radii of the core and shell). These flow velocities determine how much input torque is required to run the impeller and turbine at a fixed speed ratio for a given load (output torque requirement).

Standards are established for the test parameters at specific speed ratios. Thus for each of the four output to input shaft speed ratios - stall (output shaft stationary), 90 percent, 75 percent and 50 percent - the optimum range (min. and max. values) for input torque (IT), output torque

![](/api/attachments/4ZFHEVSQ/fulltext/images/f7fee0f003db903faae96e25988b2ada21c5f86ec3af5a11de4d4efa3b9f2dd2.jpg)  
Fig. 5. The Schematic Representation of the Torque Convertor.

Table 2  
The Components in the Schematic.

<table><tr><td>S No.</td><td>Part Name</td><td>Part Type</td></tr><tr><td>1</td><td>Input Shaft</td><td>Conduit</td></tr><tr><td>2</td><td>Housing Assembly</td><td>Conduit</td></tr><tr><td>3</td><td>Impeller (I)</td><td>Component</td></tr><tr><td>4</td><td>Turbine (T)</td><td>Component</td></tr><tr><td>5</td><td>Clearance between I&amp;T</td><td>Conduit</td></tr><tr><td>6</td><td>Stator (S)</td><td>Component</td></tr><tr><td>7</td><td>Clearance between T&amp;S</td><td>Conduit</td></tr><tr><td>8</td><td>Clearance between S&amp;I</td><td>Conduit</td></tr><tr><td>9</td><td>Stator Shaft</td><td>Conduit</td></tr><tr><td>10</td><td>Output Shaft</td><td>Conduit</td></tr><tr><td>11</td><td>Bearing (B1)</td><td>Component</td></tr><tr><td>12</td><td>Bearing (B2)</td><td>Component</td></tr><tr><td>13</td><td>Hub</td><td>Conduit</td></tr></table>

(OT), torque ratio (TR), input flow (IFLOW), output flow (OFLOW), inlet pressure (IPSI), outlet pressure (OPSI), inlet temperature (ITEMP), outlet temperature (OTEMP), and leakage (LEAK) are known. These values are based on efficiency and other performance considerations. Note that each of these test parameters is a variable characterizing material flow in the TC schematic.

From the design specifications for the TC geometry (blade angles, clearance and radii of core and shell), the desired flow velocities at the entrance and exit points of our three main Components can be determined using the set of quantitative equations. This gives a complete description of optima for all variables at each speed ratio. Note that these optima are really ranges of values (intervals) that constitute tolerance limits.  
Next, these intervals are mapped onto their qualitative equivalents such that each interval is mapped onto a single qualitative value. We use three qualitative values to represent the entire real line in a variable's quantitative space.

<table><tr><td>Quantitative Value</td><td>Qualitative Value</td></tr><tr><td>[A B] = interval of optimum values</td><td>[0]</td></tr><tr><td>values &lt; A</td><td>[-]</td></tr><tr><td>values &gt; B</td><td>[+]</td></tr></table>

Fault diagnosis in the TC involves tracing a symptom (deviation in one or more test parameters) back to a Component or Conduit. While in principle, the diagnosis should be able to trace the exact location and nature of the fault within the Component/Conduit, this is impractical in a manufacturing scenario for productivity reasons. It is much cheaper to simply replace a Component/Conduit that is identified as the source of the fault than to rework the faulty part and bring it within tolerance limits. Rework, when possible, is best done offline so that no production bottlenecks are created (as a result of diverting production resources to rework) that could result in starving downstream manufacturing operations and reducing throughput. The exception to this is when the faulty element cannot be replaced, as for example, in the case of the fault being traced to a clearance (a Conduit in our representation), or when rework is easily done, as is the case when a missing washer or spacer is the source of the problem.

Thus an intelligent diagnostic system should be able to trace a symptom back to a deviation in fluid flow velocity (since this is the main material type in the physical device) at the entrance or exit of some Component/Conduit in the schematic. Whether such a deviation was caused by an incorrect blade angle, variation in cross-sectional area or surface defects on the blades is not of consequence to the diagnosis process. This has the effect of making lesser demands on the diagnostic system by cutting short its backtracking process.

Accordingly, our system is equipped with a set of behavioral rules that specify how different (qualitative) values of entrance velocity/torque into a Component/Conduit are transformed to exit values, together with any other effects this may have on observed test parameters. These effects on test parameters are those that occur as a direct result of the corresponding Component/Conduit's transformation process. Thus if Component A causes a deviation in exit fluid flow velocity which in turn causes Component B to affect a test parameter then this effect will be described in Component B's rules not in A's. This preserves the spirit of the principle of adjacency (Davis [1985]) by allowing elements to affect only their neighbors and not be able to act at a distance except by the propagation of interaction effects.

## Descriptions of Structure and Behavior

For each Component/Conduit in the TC (see table 2), the structural variables set together with the behavioral rules that govern mapping of entrance flow velocity and entrance torque to exit flow velocity and exit torque are given below.

Note: Variables that do not appear in a behavior rule are assumed to have a value of [0], i.e., normal.

Input shaft

Variables

$T_{i} =$ input torque from the engine

$T_{out,is}$ = torque transmitted from input shaft to housing assembly

$T_{out,bl}$ = torque transmitted from bearing B1 to input shaft

$V_{\mathrm{is}} = \mathrm{rpm}$ of input shaft

Behavioral Rules

(1) $\{T_{\mathrm{i}} = [ + ]\}$ and $\{V_{\mathrm{is}} = [ + ]\} \dashrightarrow \{T_{\mathrm{out,is}} = [ + ]\}$

(2) $\{T_{\mathrm{i}} = [-]\}$ and $\{V_{\mathrm{is}} = [-]\} \dashrightarrow \{T_{\mathrm{out,is}} = [-]\}$

(3) $\{T_{\mathrm{out,bl}} = [ + ]\} \dashrightarrow \{T_{\mathrm{out,is}} = [ + ]\}$

Rule (1) and (2) specify the torque-speed characteristics of the engine. In order to generate a higher input torque $T_{i}$ the engine must revolve faster, i.e., $V_{is}$ (this is the same as the engine rpm since input shaft is directly coupled) must increase. (Note that beyond a certain speed, torque put out by the engine will begin to drop. For the purposes of this analysis this is omitted.)

Rule (3) says that if the bearing is “sticking” and thereby transmitting some torque from the output shaft, this gets added on to the input torque from the engine. In effect, the load capacity on the output shaft decreases because of this dissipation.

## Housing Assembly

Variables

$T_{out,is}$ = torque transmitted from input shaft to housing assembly

$T_{out,ha}$ = torque transmitted from housing assembly to impeller

$V_{ha} = rpm$ of housing assembly (this is equal to $V_{is}$ )

Behavioral Rules

(1) $\{T_{\mathrm{out,ha}} = [0]\} \dashrightarrow \{T_{\mathrm{out,is}} = [0]\}$

(2) $\{T_{\mathrm{out,ha}} = [-]\} \rightarrow \{T_{\mathrm{out,is}} = [-]\}$

(3) $\{T_{\mathrm{out,ha}} = [ + ]\} \dashrightarrow \{T_{\mathrm{out,is}} = [ + ]\}$

The housing assembly merely transmits the torque it receives from the input shaft. None of its own variables can ever change this.

Impeller

Variables

$R_{in,i}$ = distance from axis of TC at impeller entrance

$R_{out,i}$ = distance from axis of TC at impeller exit $V_{i}$ = radial velocity of impeller vanes (rpm)

$T_{out,ha}$ = torque transmitted from housing assembly to impeller

$V_{in,i}$ = radial velocity of fluid at impeller entrance $V_{out,i}$ = radial velocity of fluid at impeller exit

## Behavioral Rules

$\{V_{\mathrm{in,i}} = [0]\} \dashrightarrow \{V_{\mathrm{out,i}} = [0]\}$ and $\{T_{\mathrm{out,ha}} = [0]\}$

) $\{V_{\mathrm{in,i}} = [-]\} \dashrightarrow \{V_{\mathrm{out,i}} = [0]\}$ and $\{T_{\mathrm{out,ha}} =$

(3) $\{V_{\mathrm{in},i} = [ + ]\} \dashrightarrow \{V_{\mathrm{out},i} = [0]\}$ and $\{T_{\mathrm{out,ha}} = [-]\}$

(4) $\{V_{i} = [-]\} \rightarrow \{V_{\mathrm{out},i} = [-]\}$

(5) $\{R_{\mathrm{out},i} = [ + ]\} \dashrightarrow \{V_{\mathrm{out},i} = [ + ]\}$

(6) $\{R_{\mathrm{out,i}} = [-]\} \rightarrow \{V_{\mathrm{out,i}} = [-]\}$

Rules (2) and (3) have the entrance variable $T_{out,ha}$ on the right-hand side of the rule. This is because the impeller draws input torque depending on the load attached to the output shaft and thus in a sense determines how much torque is put out by the engine.

## Clearance Between Impeller and Turbine (CI) Variables

$V_{\mathrm{out,i}} =$ radial velocity of fluid at impeller exit $V_{\mathrm{in,t}} =$ radial velocity of fluid at turbine entrance $C_\mathrm{it} =$ clearance between impeller and turbine

Behavioral Rules

(1) $\{V_{\mathrm{out,i}} = [0]\} \dashrightarrow \{V_{\mathrm{in,t}} = [0]\}$

(2) $\{C_{\mathrm{it}} = [-]\} \rightarrow \{V_{\mathrm{in},\mathrm{t}} = [-]\}$

(3) $\{V_{\mathrm{out},i} = [ + ]\} \dashrightarrow \{V_{\mathrm{in},t} = [ + ]\}$

Rule (2) says that too low a clearance results in reduction of entrance velocity at the turbine due to losses caused by turbulence.

## Turbine

Variables

$R_{in,t}$ = distance from axis of TC at turbine entrance

$R_{\mathrm{out,t}} =$ distance from axis of TC at turbine exit

$V_{\mathrm{in},\mathrm{t}} =$ radial velocity of fluid at turbine entrance

$V_{\mathrm{out,t}} =$ velocity of fluid at turbine exit

$V_{t}$ = radial velocity of turbine vanes (rpm)

$m_{\mathrm{t}} =$ blade angle at turbine entrance

$T_{out,t}$ = output torque transmitted by turbine to hub

Behavioral Rules

(1) $\{V_{\mathrm{in,t}} = [0]\} \dashrightarrow \{V_{\mathrm{out,t}} = [0]\}$ and $\{T_{\mathrm{out,t}} = [0]\}$ (2) $\{V_{\mathrm{in,t}} = [-]\} \dashrightarrow \{V_{\mathrm{out,t}} = [-]\}$ and $\{T_{\mathrm{out,t}} = [-]\}$

(3) $\{V_{\mathrm{in,t}} = [ + ]\} \dashrightarrow \{V_{\mathrm{out,t}} = [ + ]\}$ and $\{T_{\mathrm{out,t}} = [ + ]\}$ and $\{V_{\mathrm{t}} = [ + ]\}$

(4) $\{m_{t} = [ + ]\} \dashrightarrow \{T_{\mathrm{out},t} = [-]\}$ and $\{V_t = [-]\}$

$$
\{R _ {\text { out,t }} = [ - ] \} \rightarrow \{V _ {\text { out,t }} = [ - ] \}
$$

Hub

Variables

$T_{out,t}$ = output torque transmitted by turbine to hub

$T_{\mathrm{out,h}} =$ torque transmitted to output shaft

## Behavioral Rules

(1) $\{T_{\mathrm{out,t}} = [0]\} \dashrightarrow \{T_{\mathrm{out,h}} = [0]\}$

(2) $\{T_{\mathrm{out,t}} = [-]\} \rightarrow \{T_{\mathrm{out,h}} = [-]\}$

(3) $\{T_{\mathrm{out},\mathrm{t}} = [ + ]\} \dashrightarrow \{T_{\mathrm{out},\mathrm{h}} = [ + ]\}$

## Clearance Between Turbine and Stator (C2)

$V_{\mathrm{out,t}} =$ velocity of fluid at turbine exit

$V_{in,st}$ = radial velocity of fluid at stator entrance

$C_{\mathrm{ts}} =$ clearance between turbine and stator

## Behavioral Rules

(1) $\{V_{\mathrm{out},t} = [0]\} \dashrightarrow \{V_{\mathrm{in,st}} = [0]\}$

(2) $\{C_{\mathrm{ts}} = [-]\} \rightarrow \{V_{\mathrm{in,st}} = [-]\}$

(3) $\{V_{\mathrm{out,t}} = [-]\} \rightarrow \{V_{\mathrm{in,st}} = [-]\}$

(4) $\{V_{\mathrm{out},\mathrm{t}} = [ + ]\} \rightarrow \{V_{\mathrm{in},\mathrm{st}} = [ + ]\}$

Stator

Variables

$V_{\mathrm{in,st}} =$ radial velocity of fluid at stator entrance

$V_{\mathrm{out,st}} =$ velocity of fluid at stator exit

$T_{\mathrm{out,st}} =$ torque transmitted to stator shaft

$n_{st} =$ blade angle at stator exit

## Behavioral Rules

(1) $\{V_{\mathrm{in,st}} = [0]\} \dashrightarrow \{V_{\mathrm{out,st}} = [0]\}$ and $\{T_{\mathrm{out,st}} = [0]\}$

(2) $\{V_{\mathrm{in,st}} = [-]\} \dashrightarrow \{V_{\mathrm{out,st}} = [-]\}$ and $\{T_{\mathrm{out,st}} =$

(3) $[V_{\mathrm{in,st}} = [ + ]\} \dashrightarrow \{V_{\mathrm{out,st}} = [ + ]\}$ and $\{T_{\mathrm{out,st}} =$

(4) $\{n_{\mathrm{st}} = [ + ]\} \dashrightarrow \{V_{\mathrm{out,st}} = [-]\}$ and $\{T_{\mathrm{out,st}} = [-]\}$

## Clearance Between Stator and Impeller (C3)

$V_{\mathrm{out,st}} =$ velocity of fluid at stator exit

$C_{\mathrm{si}} =$ clearance between stator and impeller

## Behavioral Rules

(1) $\{V_{\mathrm{out,st}} = [0]\} \dashrightarrow \{V_{\mathrm{in,i}} = [0]\}$

(2) $\{C_{\mathrm{si}} = [-]\} \rightarrow \{V_{\mathrm{in,i}} = [-]\}$

(3) $\{V_{\mathrm{out,st}} = [-]\} \rightarrow \{V_{\mathrm{in,i}} = [-]\}$

(4) $\{V_{\mathrm{out,st}} = [ + ]\} \rightarrow \{V_{\mathrm{in,i}} = [ + ]\}$

## Stator Shaft

Variables

$T_{\mathrm{out,st}} =$ torque transmitted to stator shaft

$T_{\mathrm{out,sl}} =$ reaction torque transmitted to stator

$T_{\mathrm{out,s2}} =$ torque transmitted to bearing B2

## Behavioral Rules

(1) $\{T_{\mathrm{out,st}} = [-]\} \dashrightarrow \{T_{\mathrm{out,sl}} = [-]\}$

(2) $\{T_{\mathrm{out,st}} = [ + ]\} \dashrightarrow \{T_{\mathrm{out,sl}} = [ + ]\}$

Bearing B2 (Between Stator Shaft and Output Shaft) Variables

$TEMP_{\mathrm{b2}} =$ temperature of bearing

$T_{\mathrm{out,s2}} =$ torque transmitted to bearing B2

$T_{out,b2}=$ torque transmitted to output shaft

## Behavioral Rules

(1) $\{TEMP_{b2} = [0]\} \dashrightarrow \{T_{\mathrm{out},b2} = [0]\}$

(2) $\{TEMP_{b2} = [ + ]\} \dashrightarrow \{T_{out,b2} = [ + ]\}$

If the bearing gets overheated it implies that it is not running freely and thereby transmitting some torque to output shaft.

## Output Shaft

Variables

$T_{\mathrm{out,h}} =$ torque transmitted to output shaft

$T_{\mathrm{out,b2}} =$ torque transmitted to output shaft

$T_{\mathrm{out,os1}} =$ torque transmitted to bearing B1

$T_{\mathrm{out,os2}} =$ torque transmitted to load

Behavioral Rules

(1) $\{T_{\mathrm{out,h}} = [0]\} \dashrightarrow \{T_{\mathrm{out,os2}} = [0]\}$

(2) $\{T_{\mathrm{out,h}} = [-]\} \rightarrow \{T_{\mathrm{out,os2}} = [-]\}$

(3) $\{T_{\mathrm{out,h}} = [ + ]\} \rightarrow \{T_{\mathrm{out,os2}} = [ + ]\}$

(4) $\{T_{\mathrm{out,b2}} = [ + ]\} \rightarrow \{T_{\mathrm{out,os2}} = [-]\}$

(5) $\{T_{\mathrm{out,os1}} = [ + ]\} \dashrightarrow \{T_{\mathrm{out,os2}} = [-]\}$

Rule (4) says that when bearing B2 transmits torque from the stator shaft it has the effect of reducing the torque from the output shaft since the stator shaft is applying a torque in the opposite direction. Rule (5) says that if bearing B1 is "sticking" and thereby drawing some torque $(T_{\mathrm{out,os1}})$ , the net torque available to drive the attached load $(T_{\mathrm{out,os2}})$ will decrease as a result of this dissipation.

## Bearing B1 (Between Output Shaft and Input Shaft) Variables

$T_{\mathrm{out,os1}} =$ torque transmitted to bearing B1

$T_{\mathrm{out,b1}} =$ torque transmitted to input shaft

$TEMP_{\mathrm{b1}} =$ temperature of bearing

Behavioral Rules

(1) $\{TEMP_{b1} = [0]\} \dashrightarrow \{T_{\mathrm{out},b1} = [0]\}$ and $\{T_{\mathrm{out},\mathrm{os1}} = [0]\}$

(2) $\{TEMP_{b1} = [ + ]\} \dashrightarrow \{T_{out,b1} = [ + ]\}$ and $\{T_{out,os1} = [ + ]\}$

Rule (2) says that if the bearing does not run smoothly (gets overheated), it draws torque $T_{\mathrm{out,osl}}$ from the output shaft and transmits this back to the input shaft $T_{\mathrm{out,bl}}$ .

This completes the qualitative causal model building stage for the TC.

## 4. An Example of the Qualitative Reasoning Process

When a TC fails on the testbed, the observed values for the test parameters together with the input values for torque $T_{i}$ , speed $V_{is}$ (input shaft rpm), and speed $V_{t}$ (turbine rpm) are read off the gauges on the testbed. The system first retrieves the dependency lists for each test parameter that has a $[+]$ or $[-]$ value and finds those components/conduits that are common to all these dependency lists. This corresponds to (i) and (ii) of Hypothesis Generation (Step 2) in the Qualitative Reasoning Process (see Appendix A). Note that the Dependency Lists are assumed to already exist so the system skips Step 1.

For the purposes of this example, let us assume that the output torque $T_{out,os2}$ put out by the output shaft is below the tolerance range, i.e., it has a value of $[-]$ . All other test parameters have normal values, i.e., [0].

The diagnostic system initializes the qualitative model of the TC by setting the output torque (OT) test parameter value to $[-]$ , and all other test parameter values to [0]. The system first retrieves the dependency list of components/conduits that could cause a $[-]$ value for the OT test parameter. Only one dependency list is retrieved because only one test parameter deviation was observed. The dependency list corresponding to a $[-]$ value for the OT component (in terms of the schematic what this really means is that $T_{out,os2} = [-]$ ) is {B2, C1}, say. (There may be other components/conduits in this list but for the purposes of illustrating the qualitative reasoning mechanism in operation we consider the two most common causes of failure associated with this symptom.) The system now proceeds to examine each of these in turn, in an attempt at uncovering more corroborative evidence with the help of the behavioral rules.

Following (i) of Step 3 of the Qualitative Reasoning Process, B2 is made the current hypothesis (location of fault) and the system finds that rule (2) of bearing B2 maps a problem in the bearing (overheating) to a deviation in the value of torque transmitted by the bearing (normally no torque is transmitted) to the output shaft:

$$
\{T E M P _ {\mathrm{b} 2} = [ + ] \} \rightarrow \{T _ {\text { out,b } 2} = [ + ] \}. \tag {2}
$$

Propagating this deviation forward through the network, it determines that this leads to a deviation in torque transmitted from the output shaft:

$$
\{T _ {\text { out,b2 }} = [ + ] \} \rightarrow \{T _ {\text { out,os2 }} = [ - ] \}. \tag {4}
$$

Since no other test parameter deviation was concluded in this propagation process, B2 overheating is consistent with all other test parameters having a [0] value. The system therefore puts B2 in a confirmed list and sets C1 as the new current hypothesis. (Repetition of (i) of Step 3 of the QR process with the second element in the candidate list.)

Rule (2) of C1 is used as the starting point of the propagation:

$$
\{C _ {\mathrm{it}} = [ - ] \} \dots \rightarrow \{V _ {\mathrm{in}, \mathrm{t}} = [ - ] \}. \tag {2}
$$

Then rule (2) of the Turbine asserts:

$$
\begin{array}{l} (2) \left\{V _ {\text { in,t }} = [ - ] \right\} \dashrightarrow \left\{V _ {\text { out,t }} = [ - ] \right\} \quad \text { and } \quad \left\{T _ {\text { out,t }} = [ - ] \right\}. \end{array}
$$

Since this rule describes two deviations a branching occurs in the propagation process. Following the second conjunct of the RHS of the above rule through rule (2) of the Hub and rule (2) of the Output Shaft, the system asserts:

$$
\begin{array}{l} \text {(2)} \left\{T _ {\mathrm{out,t}} = [ - ] \right\} \dashrightarrow \left\{T _ {\mathrm{out,h}} = [ - ] \right\} \text { and } \\ \text {(2)} \left\{T _ {\mathrm{out,h}} = [ - ] \right\} \dashrightarrow \left\{T _ {\mathrm{out,os2}} = [ - ] \right\}. \end{array}
$$

This branch of the propagation process is thus consistent with observed data. However when the first conjunct is propagated forward through rule (3) of C2 and rule (2) of Stator the system asserts:

$$
\begin{array}{l} \text {(3)} \quad \left\{V _ {\mathrm{out}, \mathrm{t}} = [ - ] \right\} \dashrightarrow \left\{V _ {\mathrm{in}, \mathrm{st}} = [ - ] \right\} \text { and } \\ \text {(2)} \quad \left\{V _ {\mathrm{in}, \mathrm{st}} = [ - ] \right\} \dashrightarrow \left\{V _ {\mathrm{out}, \mathrm{st}} = [ - ] \right\} \text { and } \quad \left\{T _ {\mathrm{out}, \mathrm{st}} = [ - ] \right\}. \end{array}
$$

Following the branching along the first conjunct and propagating through rule (3) and C3 and rule (2) of Impeller the system asserts:

$$
\begin{array}{l} \text {(3)} \quad \left\{V _ {\mathrm{out,st}} = [ - ] \right\} \dashrightarrow \left\{V _ {\mathrm{in,i}} = [ - ] \right\} \text { and } \\ \text {(2)} \quad \left\{V _ {\mathrm{in,i}} = [ - ] \right\} \dashrightarrow \left\{V _ {\mathrm{out,i}} = [ 0 ] \right\} \text { and } \quad \left\{T _ {\mathrm{out,ha}} = [ + ] \right\}. \end{array}
$$

But if $\{T_{\mathrm{out,ha}} = [ + ]\}$ then $\{T_{\mathrm{out,is}} = [ + ]\}$ as specified by rule (3) of Housing Assembly:

$$
\{T _ {\text { out,ha }} = [ + ] \} \rightarrow \{T _ {\text { out,is }} = [ + ] \} \tag {3}
$$

Note that since Housing Assembly is a conduit, it merely transfers its input material as output without altering its value. The input and output variables are strictly equal.

By a similar argument, rule (1) of Input Shaft asserts:

$$
\{T _ {i} = [ + ] \} \rightarrow \{T _ {\text { out,is }} = [ + ] \} \text {   and   } \{V _ {i s} = [ + ] \}. \tag {1}
$$

Thus it must be true that $\{T_{i}=[+]$ . But this contradicts the observed value for input torque which is normal, i.e., $\{T_{i}=[0]\}$ . At this point the system rejects the hypothesis since a conjunct of an assertion is found to lead to a contradiction. Note that the reasoning process terminates with one propagation path still unexplored. The final diagnosis of location of fault is thus determined to be B2 since it is the only candidate in the confirmed list ((ii) of Step 3). In the event of more than one candidate making the confirmed list, the system resorts to the expert's judgemental heuristics and returns the most likely candidate from the confirmed list. Fig. 6 summarizes the causal explanation as a result of the qualitative reasoning process for this example.

A prototype of this system is being implemented on a TI Explorer machine using the KEE (Knowledge Engineering Environment) expert system shell. Each component, conduit and test parameter is represented as a frame with slots for the variables that characterize it. The behavioral rules are stored as a method in another slot. This method looks at the value of the entrance fluid velocity/torque and computes the exit fluid velocity/torque, putting this value in the appropriate slot and passing a message (exit velocity/torque value) to the adjacent frame (as specified in the schematic). The name of the adjacent frame is also included in a slot in this frame.

```txt
1 Tout,os2 = [-] Given
2 Candidate elements = {B2, Cl} Dependency list of Tout,os2
3 Current hypothesis = B2 Premise
4 (Tout,b2 = [+]) (2) of B2
5 (Tout,os2 = [-]) (4) of Output shaft
6 Confirmed list = {B2} Consistent with observed value
7 Current hypothesis = Cl Premise
8 (Vin,t = [-]) (2) of Cl
9 (Vin,t = [-]) & (Tout,t = [-]) (2) of Turbine
10 (Tout,t = [-]) (2) of Hub
11 (Tout,h = [-]) (2) of Output Shaft
12 (Vout,os2 = [-]) (3) of C2
13 (Vout,st = [-]) & (Tout,st = [-]) (2) of Stator
14 (Vin,i = [-]) (3) of C3
15 (Vin,i = [0]) & (Tout,ha = [+]) (2) of Impeller
16 (Tout,i = [+]) (3) of Housing Assy
17 (Ti = [+]) (1) of Input Shaft
18 (Ti = [0] Given
19 Current Hypothesis Cl rejected 17 & 18 lead to Contradiction
20 Source of Malfunction = B2 Confirmed list
```  
Fig. 6. The Causal Explanation for a Fault Diagnosis Example.

In the frame-based system, a simulation run of the TC is achieved by message passing between component and conduit frames. Given an impeller velocity, input torque, and speed ratio combination as input, the system completes one run in which it puts entrance and exit velocity/torque values in the component and conduit frames and the value of each test parameter in its frame.

## 5. Empirical Validation By Inductive Learning

Given a product assembly, the qualitative causal model is used to capture the desired structure and behavior of the assembly. The qualitative reasoning process can propagate the effects among components and derive the diagnosis for manufacturing faults based on the observed aberrations i.e., symptoms. However, this qualitative model needs to be properly validated in order to ensure its correctness as well as the effectiveness of the diagnostic process based on the model. The problem of validation is to ascertain that a particular qualitative model demonstrates a composite behavior matching the behavior of the system under study and the diagnostic reasoning process performed by the expert.

To achieve such validation for the qualitative causal model of the torque converter, we developed a procedure using the manufacturing test data such as those collected from a torque-converter Quality Information System. Each of these cases was classified by detected location malfunction (obtained from QIS records).

Putting the tested data cases corresponding to problematic torque converter and the diagnosis

<table><tr><td>SNO</td><td>TC</td><td>IRPH</td><td>ORPH</td><td>IT</td><td>OT</td><td>TR</td><td>IPSI</td><td>OPSI</td><td>IFLOW</td><td>OPLOW</td><td>LEAK</td><td>ITEMP</td><td>OTEMP</td><td>CLPSI</td><td>CLEAK</td><td>CLASS</td><td>LOCATION OF PAULT</td></tr><tr><td>1</td><td>594</td><td>1701</td><td>1</td><td>784</td><td>1615</td><td>2.06</td><td>69</td><td>39</td><td>35.8</td><td>30.8</td><td>5</td><td>178</td><td>254</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>2</td><td>624</td><td>1701</td><td>1</td><td>774</td><td>1588</td><td>2.05</td><td>67</td><td>37</td><td>35.2</td><td>30.4</td><td>4.8</td><td>178</td><td>260</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>3</td><td>631</td><td>1701</td><td>0</td><td>797</td><td>1641</td><td>2.06</td><td>69</td><td>39</td><td>36.3</td><td>31.9</td><td>4.4</td><td>179</td><td>265</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>4</td><td>680</td><td>1701</td><td>1</td><td>784</td><td>1598</td><td>2.04</td><td>65</td><td>38</td><td>35.8</td><td>31.4</td><td>4.4</td><td>177</td><td>261</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>5</td><td>798</td><td>1701</td><td>2</td><td>794</td><td>1629</td><td>2.05</td><td>66</td><td>38</td><td>35.8</td><td>31.4</td><td>4.4</td><td>180</td><td>258</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>6</td><td>803</td><td>1701</td><td>1</td><td>797</td><td>1638</td><td>2.06</td><td>65</td><td>39</td><td>35.8</td><td>30.4</td><td>5.4</td><td>178</td><td>260</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>7</td><td>804</td><td>1701</td><td>1</td><td>764</td><td>1564</td><td>2.05</td><td>56</td><td>37</td><td>35.8</td><td>28.9</td><td>6.9</td><td>178</td><td>258</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>8</td><td>805</td><td>1701</td><td>1</td><td>785</td><td>1607</td><td>2.05</td><td>59</td><td>39</td><td>35.2</td><td>30.3</td><td>4.9</td><td>177</td><td>260</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>9</td><td>810</td><td>1701</td><td>1</td><td>771</td><td>1570</td><td>2.04</td><td>57</td><td>38</td><td>36.3</td><td>30.4</td><td>5.9</td><td>178</td><td>258</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>10</td><td>813</td><td>1699</td><td>1</td><td>775</td><td>1582</td><td>2.04</td><td>57</td><td>38</td><td>35.8</td><td>31.4</td><td>4.4</td><td>179</td><td>259</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>11</td><td>828</td><td>1701</td><td>1</td><td>777</td><td>1585</td><td>2.04</td><td>58</td><td>39</td><td>35.8</td><td>27.4</td><td>8.4</td><td>179</td><td>257</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>12</td><td>830</td><td>1699</td><td>1</td><td>785</td><td>1614</td><td>2.06</td><td>61</td><td>40</td><td>35.8</td><td>31.4</td><td>4.4</td><td>180</td><td>261</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>13</td><td>857</td><td>1701</td><td>1</td><td>787</td><td>1624</td><td>2.06</td><td>61</td><td>40</td><td>35.8</td><td>29.8</td><td>6</td><td>166</td><td>247</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>14</td><td>1142</td><td>1701</td><td>0</td><td>772</td><td>1580</td><td>2.05</td><td>60</td><td>38</td><td>35.8</td><td>30.4</td><td>5.4</td><td>179</td><td>256</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>15</td><td>5748</td><td>2001</td><td>1</td><td>680</td><td>1455</td><td>2.14</td><td>84</td><td>38</td><td>50.9</td><td>45.7</td><td>5.2</td><td>179</td><td>234</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>16</td><td>5859</td><td>2000</td><td>1</td><td>673</td><td>1453</td><td>2.16</td><td>86</td><td>38</td><td>50.9</td><td>45.7</td><td>5.2</td><td>180</td><td>240</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>17</td><td>5872</td><td>2001</td><td>1</td><td>670</td><td>1442</td><td>2.15</td><td>85</td><td>39</td><td>50.9</td><td>46.1</td><td>4.8</td><td>178</td><td>237</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>18</td><td>5904</td><td>2001</td><td>1</td><td>668</td><td>1454</td><td>2.18</td><td>88</td><td>39</td><td>50.9</td><td>46.1</td><td>4.8</td><td>179</td><td>242</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>19</td><td>5905</td><td>2001</td><td>1</td><td>665</td><td>1445</td><td>2.17</td><td>88</td><td>39</td><td>50.9</td><td>46.1</td><td>4.8</td><td>180</td><td>244</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>20</td><td>5923</td><td>2001</td><td>0</td><td>675</td><td>1448</td><td>2.15</td><td>85</td><td>37</td><td>50.9</td><td>46.2</td><td>4.7</td><td>180</td><td>239</td><td>0</td><td>0</td><td>A1</td><td>CARRIER</td></tr><tr><td>21</td><td>4058</td><td>1402</td><td>1404</td><td>1005</td><td>987</td><td>0.98</td><td>103</td><td>59</td><td>60.1</td><td>57.9</td><td>2.9</td><td>178</td><td>179</td><td>187</td><td>2.2</td><td>A1'</td><td>CARRIER ASSEMBLY</td></tr><tr><td>22</td><td>4141</td><td>1404</td><td>1405</td><td>997</td><td>979</td><td>0.98</td><td>106</td><td>61</td><td>60.1</td><td>57.9</td><td>2.6</td><td>179</td><td>180</td><td>185</td><td>1.4</td><td>A1'</td><td>CARRIER ASSEMBLY</td></tr><tr><td>23</td><td>4286</td><td>1400</td><td>1400</td><td>1005</td><td>986</td><td>0.98</td><td>106</td><td>59</td><td>60.5</td><td>58.4</td><td>2.5</td><td>180</td><td>181</td><td>188</td><td>1.4</td><td>A1'</td><td>CARRIER ASSEMBLY</td></tr><tr><td>24</td><td>5767</td><td>2001</td><td>0</td><td>772</td><td>1545</td><td>2</td><td>85</td><td>38</td><td>49.8</td><td>46.6</td><td>3.2</td><td>177</td><td>241</td><td>0</td><td>0</td><td>A2</td><td>IMPELLER</td></tr><tr><td>25</td><td>5821</td><td>2000</td><td>1</td><td>693</td><td>1456</td><td>2.1</td><td>86</td><td>39</td><td>50.4</td><td>48.2</td><td>2.2</td><td>179</td><td>238</td><td>0</td><td>0</td><td>A2</td><td>IMPELLER</td></tr><tr><td>26</td><td>5938</td><td>1999</td><td>1</td><td>693</td><td>1432</td><td>2.07</td><td>73</td><td>39</td><td>40.3</td><td>37.2</td><td>3.1</td><td>179</td><td>251</td><td>0</td><td>0</td><td>A2</td><td>IMPELLER</td></tr><tr><td>55</td><td>78</td><td>2100</td><td>0</td><td>697</td><td>1491</td><td>2.14</td><td>76</td><td>40</td><td>40.8</td><td>38.1</td><td>2.7</td><td>180</td><td>254</td><td>0</td><td>0</td><td>E1</td><td>CLUTCH</td></tr><tr><td>27</td><td>63</td><td>1401</td><td>1401</td><td>501</td><td>489</td><td>0.98</td><td>81</td><td>42</td><td>40.3</td><td>40.3</td><td>0.7</td><td>180</td><td>183</td><td>283</td><td>2.1</td><td>B1</td><td>SHAFT</td></tr><tr><td>28</td><td>67</td><td>1401</td><td>1400</td><td>496</td><td>501</td><td>1.01</td><td>80</td><td>41</td><td>40.8</td><td>39.8</td><td>1.7</td><td>180</td><td>187</td><td>281</td><td>2.3</td><td>B1</td><td>SHAFT</td></tr><tr><td>29</td><td>69</td><td>1401</td><td>1399</td><td>492</td><td>501</td><td>1.02</td><td>80</td><td>41</td><td>40.3</td><td>40.2</td><td>0.9</td><td>179</td><td>183</td><td>282</td><td>2.4</td><td>B1</td><td>SHAFT</td></tr><tr><td>30</td><td>96</td><td>1401</td><td>1401</td><td>503</td><td>493</td><td>0.98</td><td>78</td><td>41</td><td>39.7</td><td>39.2</td><td>1.2</td><td>182</td><td>185</td><td>284</td><td>2.1</td><td>B1</td><td>SHAFT</td></tr><tr><td>31</td><td>97</td><td>1401</td><td>1399</td><td>500</td><td>505</td><td>1.01</td><td>78</td><td>41</td><td>40.3</td><td>39.3</td><td>1.7</td><td>182</td><td>184</td><td>279</td><td>2.1</td><td>B1</td><td>SHAFT</td></tr><tr><td>32</td><td>4277</td><td>1400</td><td>1401</td><td>1001</td><td>979</td><td>0.98</td><td>106</td><td>59</td><td>59.9</td><td>57.7</td><td>2.7</td><td>180</td><td>179</td><td>187</td><td>1.7</td><td>B1'</td><td>HUB</td></tr><tr><td>33</td><td>4278</td><td>1402</td><td>1403</td><td>1003</td><td>984</td><td>0.98</td><td>106</td><td>59</td><td>59.8</td><td>58.8</td><td>1.4</td><td>180</td><td>180</td><td>186</td><td>1.4</td><td>B1'</td><td>HUB</td></tr><tr><td>34</td><td>4286</td><td>1400</td><td>1400</td><td>1005</td><td>986</td><td>0.98</td><td>106</td><td>59</td><td>60.5</td><td>58.4</td><td>2.5</td><td>180</td><td>181</td><td>188</td><td>1.4</td><td>B1'</td><td>HUB</td></tr><tr><td>35</td><td>4368</td><td>1402</td><td>1402</td><td>1003</td><td>983</td><td>0.98</td><td>100</td><td>60</td><td>60.4</td><td>58.6</td><td>2.3</td><td>180</td><td>180</td><td>189</td><td>1.5</td><td>B1'</td><td>HUB</td></tr><tr><td>36</td><td>4381</td><td>1403</td><td>1403</td><td>1005</td><td>984</td><td>0.98</td><td>100</td><td>59</td><td>60.4</td><td>58.4</td><td>2.5</td><td>180</td><td>179</td><td>190</td><td>1.5</td><td>B1'</td><td>HUB</td></tr><tr><td>37</td><td>4397</td><td>1402</td><td>1404</td><td>1002</td><td>982</td><td>0.98</td><td>100</td><td>61</td><td>60.1</td><td>58.3</td><td>2.4</td><td>180</td><td>181</td><td>188</td><td>1.8</td><td>B1'</td><td>HUB</td></tr><tr><td>38</td><td>4400</td><td>1401</td><td>1401</td><td>1002</td><td>982</td><td>0.98</td><td>101</td><td>61</td><td>60.1</td><td>58.6</td><td>1.9</td><td>181</td><td>180</td><td>187</td><td>1.4</td><td>B1'</td><td>HUB</td></tr><tr><td>39</td><td>7338</td><td>2099</td><td>1</td><td>607</td><td>1689</td><td>2.78</td><td>84</td><td>60</td><td>40.8</td><td>31</td><td>9.8</td><td>181</td><td>238</td><td>0</td><td>0</td><td>C1''</td><td>TURBINE</td></tr><tr><td>40</td><td>7377</td><td>2100</td><td>0</td><td>610</td><td>1686</td><td>2.76</td><td>84</td><td>57</td><td>41.4</td><td>34.4</td><td>7</td><td>181</td><td>241</td><td>0</td><td>0</td><td>C1''</td><td>TURBINE</td></tr><tr><td>41</td><td>7615</td><td>2100</td><td>1</td><td>611</td><td>1688</td><td>2.76</td><td>85</td><td>59</td><td>40.8</td><td>33.8</td><td>7</td><td>178</td><td>238</td><td>0</td><td>0</td><td>C1''</td><td>TURBINE</td></tr><tr><td>42</td><td>7616</td><td>2101</td><td>1</td><td>609</td><td>1694</td><td>2.78</td><td>83</td><td>60</td><td>40.8</td><td>33.8</td><td>7</td><td>179</td><td>240</td><td>0</td><td>0</td><td>C1''</td><td>TURBINE</td></tr><tr><td>43</td><td>7666</td><td>2101</td><td>1</td><td>616</td><td>1687</td><td>2.74</td><td>82</td><td>57</td><td>40.8</td><td>33.9</td><td>6.9</td><td>180</td><td>243</td><td>0</td><td>0</td><td>C1''</td><td>TURBINE</td></tr><tr><td>44</td><td>7692</td><td>2101</td><td>0</td><td>613</td><td>1704</td><td>2.78</td><td>84</td><td>57</td><td>40.8</td><td>33.4</td><td>7.4</td><td>179</td><td>237</td><td>0</td><td>0</td><td>C1''</td><td>TURBINE</td></tr><tr><td>45</td><td>2209</td><td>2001</td><td>0</td><td>913</td><td>2363</td><td>2.59</td><td>94</td><td>59</td><td>50.9</td><td>45.7</td><td>5.2</td><td>172</td><td>252</td><td>0</td><td>0</td><td>C2'</td><td>SUPPORT</td></tr><tr><td>46</td><td>2225</td><td>2001</td><td>1</td><td>919</td><td>2374</td><td>2.58</td><td>92</td><td>58</td><td>50.9</td><td>46.3</td><td>4.6</td><td>180</td><td>258</td><td>0</td><td>0</td><td>C2'</td><td>SUPPORT</td></tr><tr><td>47</td><td>8876</td><td>2001</td><td>1499</td><td>286</td><td>324</td><td>1.13</td><td>66</td><td>41</td><td>22.3</td><td>22.3</td><td>0</td><td>180</td><td>192</td><td>0</td><td>0</td><td>D1</td><td>STATOR</td></tr><tr><td>48</td><td>8878</td><td>2001</td><td>1501</td><td>286</td><td>324</td><td>1.13</td><td>66</td><td>41</td><td>22.3</td><td>21.8</td><td>0.5</td><td>179</td><td>191</td><td>0</td><td>0</td><td>D1</td><td>STATOR</td></tr><tr><td>49</td><td>8883</td><td>1999</td><td>1499</td><td>286</td><td>325</td><td>1.13</td><td>67</td><td>41</td><td>22.3</td><td>21.8</td><td>0.5</td><td>180</td><td>192</td><td>0</td><td>0</td><td>D1</td><td>STATOR</td></tr><tr><td>50</td><td>8884</td><td>2001</td><td>1499</td><td>285</td><td>325</td><td>1.13</td><td>67</td><td>41</td><td>23.4</td><td>22.2</td><td>1.2</td><td>179</td><td>192</td><td>0</td><td>0</td><td>D1</td><td>STATOR</td></tr><tr><td>51</td><td>8886</td><td>1999</td><td>1501</td><td>285</td><td>322</td><td>1.13</td><td>66</td><td>41</td><td>23.4</td><td>22.3</td><td>1.1</td><td>180</td><td>191</td><td>0</td><td>0</td><td>D1</td><td>STATOR</td></tr><tr><td>52</td><td>8895</td><td>1999</td><td>1501</td><td>285</td><td>325</td><td>1.13</td><td>66</td><td>40</td><td>21.7</td><td>21.2</td><td>0.5</td><td>180</td><td>194</td><td>0</td><td>0</td><td>D1</td><td>STATOR</td></tr><tr><td>53</td><td>8896</td><td>2001</td><td>1500</td><td>285</td><td>325</td><td>1.13</td><td>66</td><td>41</td><td>22.3</td><td>21.2</td><td>1.1</td><td>178</td><td>191</td><td>0</td><td>0</td><td>D1</td><td>STATOR</td></tr><tr><td>54</td><td>74</td><td>2100</td><td>0</td><td>679</td><td>1481</td><td>2.18</td><td>75</td><td>40</td><td>40.3</td><td>38.2</td><td>2.1</td><td>180</td><td>250</td><td>0</td><td>0</td><td>E1</td><td>CLUTCH</td></tr></table>

Fig. 7. (continued).

given by the expert together, we have a set of data cases in the following form:

$\left( \begin{array}{c}\text {test data for the problem-}\\ \text {matic torque converter} \end{array} \right)\longrightarrow \left( \begin{array}{c}\text {detected location}\\ \text {of malfunction} \end{array} \right)$

These data cases gathered from the outputs of QIS are shown in fig. 7. The basic idea of the validation process is to derive rules that can link a subset of the 13 test parameters to each location of malfunction. These rules are then tested against the qualitative causal model for validation. As shown in the conceptual procedure depicted in fig. 8, the rules can be generated by inductive learning.

![](/api/attachments/4ZFHEVSQ/fulltext/images/9ba34bba103e6b8c037beafaa70a987f848d731de332960ef89df3a83f3b2ce6.jpg)  
Fig. 8. The Use of Inductive Learning for Deriving Diagnostic Rules.

Inductive learning can be defined as the process of inferring the description of a decision - i.e., a concept - based on the description of examples for that concept. In our case, the data in fig. 7 can be used as such “training examples” for learning diagnostic rules.

There are a variety of computer algorithms developed for inductive learning (Michalski [1983]). The one we used is a program called ACLS (Analogue Concept Learning System) which is in the ID3 family described in (Quinlan [1986]).

Inductive learning algorithms such as ACLS use a decision-theoretic approach to form homogenous clusters of the given set of objects such that objects in each cluster have similar values for some group of attributes. Each example (object) is represented as a conjunction of attribute-value pairs. The induction algorithm takes such object descriptions as input together with a classification label for each object, and returns a description for each of the classification labels, expressed as a conjunction of attribute value pairs, such that the attributes in the classification description form a subset of the total set of attributes used to describe each object. This classification description is in effect a generalized description of all objects in the example set that were tagged with the same label.

In our application, each TC test (only “failed” TC’s are considered) represents one object. The object description is the conjunction of the test parameter and observed value pairs (thus each test parameter is an attribute) and the classification is the location of fault that was determined on the shop floor. ACLS derives a classification rule (a generalized description for each location of fault expressed in terms of the observed values for a subset of test parameters) which for the purposes of display is cast in the form of a decision tree, branching according to the values of the attributes.

By running the training examples shown in fig. 7 through the inductive learning program ACLS, we obtained a set of diagnostic rules; some of the sample diagnostic rules are illustrated in fig. 9. Consider, for example, a diagnostic rule $R_{i}$ obtained by induction, of the following form:

$$
\begin{array}{l} R _ {i}: \text { IF } (| T _ {i _ {1}} - a _ {i _ {1}} | > e _ {i _ {1}}) \& (| T _ {i _ {2}} - a _ {i _ {2}} | \\ > e _ {i _ {2}}) \& \dots . \\ \dots . \& (| T _ {i _ {k}} - a _ {i _ {k}} | > e _ {i _ {k}}) \\ \text { then   fault - location   is   i } \end{array}
$$

The validation of the model using this rule would proceed as below:

STEP 1 Introduce a qualitative deviation $d_{i}$ to the flow at the exit of the component/conduit associated with location $i$ . For $d_{i} = [+]$ and $[-]$ respectively, do Step 2 and Step 3.

STEP 2 Propagate the deviation through the schematic using the behavioral rules of the components/conduits that lie in the causal path; determine the values predicted for the set of test parameters $\{T_i, i = 1, \ldots, n\}$ .

STEP 3 Compare the predicted test values obtained in Step 2 with the value specified in the antecedent of $R_{i}$ . If the two sets of conditions match, then $R_{i}$ is consistent with the qualitative model. Exit.

(4) IF (INPUT-RPM >= 1552) & (LEAKAGE >= 3.8) & (OUTPUT-TORQUE >= 1664) THEN (FAULT-LOCATION IS TURBINE)

![](/api/attachments/4ZFHEVSQ/fulltext/images/12fa0a0788cc0f491c4f67e148eeea89e46a4a545422ea455ac2f4193ccacd1b.jpg)  
Fig. 9. (a). The Diagnostic Decision Tree Generated by the Learning Program.

STEP 4 Otherwise $R_{i}$ is not consistent with the qualitative model, a modification routine is called upon to check the source of the discrepancies.

(i)

(ii)

To illustrate the validation process consider the following rule:

(iii)

IF (Input-Torque (IT) = [-]) and (Inlet-Flow (IFLOW) = [ + ]) and (Output-Torque (OT) = [ + ]) and (Input-Speed (IRPM) = [-])

(iv)

(v)

THEN Fault-Location is IMPELLER.

(vi)

(In terms of the TC schematic these test parameter symbols translate as: IT = $T_{i}$ , IFLOW = $V_{in,t}$ , OT = $T_{out,Os2}$ & PM = $V_{is}$ .)

The validation of the model would appear as below:

STEP 1 The system introduces a $[+]$ deviation to the flow at the exit of the IMPELLER. Thus it sets $V_{\mathrm{out},i} = [+]$ .

STEP 2 Propagating this through the schematic yields the following:

## Diagnostic Rules

(3) IF (INPUT-RPM < 1552) & (INPUT-TORQUE >= 749) & (OUTPUT-TORQUE >= 985)
THEN (FAULT-LOCATION IS CARRIER ASSEMBLY)

(5) IF (INPUT-RPM >= 1552) & (LEAKAGE >= 3.8) & (OUTPUT-TORQUE < 1664) THEN (FAULT-LOCATION IS CARRIER)

(6) IF (INPUT-RPM >= 1552) & (LEAKAGE < 3.8) & (OUTPUT-RPM >= 750)
THEN (FAULT-LOCATION IS STATOR)

(7) IF (INPUT-RPM >= 1552) & (LEAKAGE < 3.8) & (OUTPUT-RPM < 750) THEN (FAULT-LOCATION IS IMPELLER)

Fig. 9. (b). Sample Diagnostic Rules Learned from the Empirical Data.

$\{V_{\mathrm{out,i}} = [ + ]\} \dashrightarrow \{V_{\mathrm{in,t}} = [ + ]\}$ by rule 3 of C1

$\{V_{\mathrm{in,t}} = [ + ]\} \dashrightarrow \{V_{\mathrm{out,t}} = [ + ]\}$ and $\{T_{\mathrm{out,t}} = [ + ]\}$ by rule 3 of TURBINE

$\{T_{\mathrm{out,t}} = [ + ]\} \dashrightarrow \{T_{\mathrm{out,h}} = [ + ]\}$ by rule 3 of HUB

$\{T_{\mathrm{out,h}} = [ + ]\} \dashrightarrow \{T_{\mathrm{out,Os2}} = [ + ]\}$ by rule 3 of OUTPUT SHAFT

$\{V_{\mathrm{out,t}} = [ + ]\} \dashrightarrow \{V_{\mathrm{in,st}} = [ + ]\}$ by rule 4 of C2

$$
\{V _ {\text { in,st }} = [ + ] \} \rightarrow \{V _ {\text { out,st }} = [ + ] \} \quad \text { and }
$$

$$
\left\{T _ {\text { out,st }} = [ + ] \right\}
$$

(vii) $\{V_{\mathrm{out},\mathrm{st}} = [ + ]\} \dashrightarrow \{V_{\mathrm{in,i}} = [ + ]\}$ by rule 4 of C3

(viii) $\{V_{\mathrm{in,i}} = [ + ]\} \dashrightarrow \{T_{\mathrm{out,ha}} = [-]\}$ by rule 3 of IMPELLER

(ix) $\{T_{\mathrm{out,ha}} = [-]\} \dashrightarrow \{T_{\mathrm{out,is}} = [-]\}$ by rule 2 of HOUSING ASSEMBLY

(x) $\{T_{\mathrm{i}} = [-]\}$ and $\{V_{\mathrm{is}} = [-]\} \dashrightarrow \{T_{\mathrm{out.is}} = [-]\}$ by rule 2 of INPUT SHAFT

Thus the $[+]$ deviation at IMPELLER exit has predicted

$$
\begin{array}{l} \left\{V _ {\mathrm{in,t}} = [ + ] \right\} \text { by (ii)} \\ \left\{T _ {\mathrm{out.Os2}} = [ - ] \right\} \text { by (iv)} \\ \left\{T _ {\mathrm{i}} = [ - ] \right\} \text { and } \left\{V _ {\mathrm{is}} = [ - ] \right\} \text { by (x)} \end{array}
$$

STEP 3 Comparing these predicted values with the antecedent of induction rule $R_{i}$ yields a perfect match. Thus the system concludes that the induction rule $R_{i}$ is consistent with the qualitative model.

In the event of a perfect match not being obtained, intervention by a domain expert is required to reconcile the discrepancies between predicted and observed values for the test parameters in question. The expert must make a judgment about the validity of the data used to induce the rule on the one hand (data may have been corrupted by noise), and the validity of the qualitative model on the other. As shown in fig. 8, this reconciliation between the deep reasoning of the model and the shallow reasoning represented by induction rules is brought about by comparing the predictions made by each with the expert's own heuristics.

In a sense, the inductive learning process can be viewed as data compression since the rules derived contain all the relevant knowledge described by the training examples. We can then use these rules to validate the qualitative causal model. Besides serving as a validation tool during the initial model building stage, induction can be useful in carrying out periodic reviews of the model, modifying its behavioral rules when necessary.

## 6. Summary

We have shown how fault diagnosis of a mechanical assembly can be performed using a qualitative reasoning model representing the mechanism of the assembly. Starting with the classification of the assembly's parts into two generic types called components and conduits, a structural description consisting of a schematic, which is a circuit diagram-like representation of the interconnections between parts, and the variables that characterize the parts, is built. A description of the assembly's behavior is contained in a set of behavioral rules (derived from the quantitative equations that describe the physical system), that specify mapping of the entrance values of "material flow variables" to their exit values. The physical system's behavior is simulated by a causal reasoning approach that uses these behavioral rules to determine the effects that are passed between the system's elements. Induction is used as a mechanism for abstracting generalizations from raw performance data, which is then used to validate the qualitative causal reasoning model as well as the domain expert's diagnostic heuristics.

Although the qualitative reasoning approach with causal models is applied only to fault diagnosis in this paper, the approach has broader implications to integrated manufacturing. Using the manufacturing fault diagnosis of the torque converter as an example, the causal model for the assembly can be used by the design engineer to test if the underlying design for the torque converter assembly meets the functional specifications (Murakami and Nakajima [1988]); the process engineer can use the model of the assembly for process planning (Shaw, Menon, and Park [1988]); and the quality control engineer can use it for fault diagnosis as described in this paper. Such an approach unifies the representation of the assembly in different phases of the manufacturing process and enforces the coordination among these manufacturing activities.

Acknowledgement. This research is supported in part by the Office for Information Management, the Research Board of the University of Illinois, Texas Instruments, and IntelliCorp. Texas Instruments and IntelliCorp also provided the LISP machine and the knowledge engineering environment (KEE) software for implementing the prototype. The help we obtained from the Quality Control Department in Caterpillar Inc. is greatly appreciated. Prakash B. Babu contributed greatly to the success of this project and provided many insightful suggestions. Marvin Blunier and John Shorty are the diagnostic experts who helped us on many technical aspects of the research. We learned a great deal from them on the quality control decision process.

## References

Becker, L.A. and Bartlett, R. (1988). Compiling Diagnostic Rules from a Manufacturing Process Representation, in Artificial Intelligence in Engineering: Diagnosis and Learning, J.S. Gero (Ed.), Elsevier, Amsterdam, pp. 285–304.

Bobrow, D.G. (1985). Qualitative Reasoning About Physical Systems (Ed.), MIT Press, Cambridge, MA.

Davis, R. (1984). Diagnostic Reasoning Based on Structure and Behavior, Artificial Intelligence 24, no. 1–3, pp. 347–410.

De Kleer, J. and Brown, J.S. (1984). A Qualitative Physics Based on Confluences, Artificial Intelligence 24, no. 1–3, pp. 7–83.

De Kleer, J. and Brown, J.S. (1985). Qualitative Physics Based On Confluence. In Qualitative Reasoning About Physical Systems, D. Bobrow (Ed.), MIT Press.

Fink, P.K. and Lusth, J.C. (1987). Expert Systems and Diagnostic Expertise in the Mechanical and Electrical Domains, IEEE Transactions on Systems, Man, and Cybernetics, V. 17, No. 3, pp. 340–349.

Forbus, K.D. (1984). Qualitative Process Theory, Artificial Intelligence, V. 24.

Garvin, D.A. (1988). Managing Quality, Macmillan Publishers, New York.

Genesereth, M.R. (1984). The Use of Design Descriptions in Automated Diagnosis, Artificial Intelligence, V. 24.

Groover, M.P. (1980). Automation, Production Systems, and Computer-Aided Manufacturing, Prentice-Hall Inc., Englewood Cliffs, N.J.

Herbert, M.R. and Williams, G.H. (1987). An Initial Evolution of the Detection and Diagnosis of Power Plant Faults using a Deep knowledge Representation of Physical Behavior, Expert Systems, vol. 4, no. 2, pp 90–99.

Hofmann, M., Caviedes, J., Bourne, J., Beale, G., and Brodersen, A. (1986). Building Expert Systems for Repair Domains, Expert Systems, Vol. 3, no. 1, pp 4–12.

Iwasaki, Y. and Simon, H.A. (1986). Causality in Device Behavior, Artificial Intelligence, V. 29.

Kuipers, B. (1984). Commerce Sense Reasoning About Causality: Deriving Behavior from Structure, Artificial Intelligence, V. 24.

Kuipers, B. (1986). Qualitative Simulation, Artificial Intelligence, V. 29, pp. 289–338.

Larew, W.B. (1968). Fluid Clutches and Torque Convertors. Chilton Book Company.

Larkin, J., McDermott, J., Simon, D. and Simon, H. (1980). Expert and Novice Performance in Solving Physics Problems, Science, V. 208, pp. 1335–1342.

Michalski, R.S. (1983). A Theory and Methodology of Inductive Learning, in Machine Learning, Michalski, Carbonell, and Mitchell (eds.), Tioga Publishing Co., Palo Alto, CA.

Murakami, T. and Nakajima (1988). Computer-Aided Design Diagnosis Using Feature Description, in Artificial Intelligence in Engineering: Diagnosis and Learning, J.S. Gero (Ed.), Elsevier, Amsterdam, pp. 199–226.

Pan, L.F. (1986). Survey of Expert Systems for Fault Detection, Test Generation and Maintenance, Expert Systems, vol. 3, no. 2, pp 100–111.

Quinlan, J.R. (1979). Discovering Rules from Large Collections of Examples: A Case Study. In Expert Systems in the Microelectronic Age, D. Mitchie (Ed.), Edinburgh University Press.

Quinlan, J.R. (1986). Induction of Decision Trees. In Machine Learning, Vol. 1, pp. 81–106, 1986.

Ranky, P.G. (1986). Computer-Integrated Manufacturing, Prentice-Hall International, Englewood Cliffs, N.J.

Reiter, R. (1987). A Theory of Diagnosis From First Principles, Artificial Intelligence, V: 32 (1), pp. 57–96.

Rieger, C. and Grinberg, M. (1978). A System of Cause-Effect Representation and Simulation for Computer-Aided Design, in Artificial Intelligence and Pattern Recognition in Computer Aided Design, Latombe (ed.), North-Holland Pub. Co., Amsterdam, pp. 299–334.

Shaw, M., Menon, U., and Park, S.C. (1988). An Explanation-Based Learning Approach to Intelligent Process Planning, in Expert Systems, A. Kusiak (Ed.), Society of Manufacturing Engineers Press, Dearborn, MI.

## Appendix A - Qualitative Reasoning Process

STEP 1: Build Dependency Lists \*

(i) Identify the set of elements $\{E_i\}$ that have been known to cause a device malfunction

(ii) For each $E_{i}$ introduce a $[+]$ deviation for material flow variable $Mv_{i}$ at this element's exit

(iii) Propagate this deviation through the schematic, following the path of $Mv_{i}$ , updating the qualitative values of material flow variables at the inlet and exit points of all elements in the schematic

(iv) Form a list $L_{i+}$ of all test parameters (subset of material flow variables) whose values show $[+]$ deviation and list $L_{i-}$ for all test parameters that show $[-]$ deviation

(v) Repeat steps (ii)-(iv) with $[-]$ deviation for $M_{vi}$ and update lists $L_{i+} \& L_{i-}$

(vi) From the lists $L_{i+}$ and $L_{i-}$ , compile dependency lists $D_{j+}$ and $D_{j-}$ for the $j$ th test parameter such that $D_{j+}$ contains all those elements that caused a $[+]$ deviation in $j$ 's value, and $D_{j-}$ contains those elements that caused a $[-]$ deviation in $j$ 's value.

\* This is a one time activity that helps save diagnosis time.

## STEP 2: Hypothesis Generation

(i) Given an observed set of test parameter values $\{O_j\}$ , retrieve the corresponding dependency list for each $O_j$ that has a $[+]$ or $[-]$ value.

(ii) Form a candidate element list $\{C_{i}\}$ above that is the intersection of all dependency lists in (i) above. This is the list of likely sources of device malfunction.

## STEP 3: Envisionment

(i) For each candidate element in $\{C_i\}$ , introduce a deviation for material flow variable at exit of element and propagate this through the schematic updating all material flow variables. Compare the predicted values of test parameters with $\{O_j\}$ . If a perfect match is obtained, this element is confirmed as a source of device malfunction otherwise this element is removed from the list $\{C_i\}$ .

(ii) Return the elements remaining in $\{C_i\}$ after (i) and terminate procedure.

(iii) If after (i) $\{C_{i}\}$ has no elements, start with each of the remaining elements not in $\{E_{i}\}$ and propagate deviations introduced at the exit of the element updating material flow variables as before. Compare predicted test parameter values with $\{O_{i}\}$ and stop when a perfect match is found. \*\*

\*\* The system could be directed to search the remaining elements in some prespecified order so that it works its way down the list beginning with the most probable element.

## Appendix B - The Torque Converter

The torque converter is a device used in automobile transmissions. Its function is similar to that of a gear-box in conventional transmissions; it takes the engine torque as input and delivers a higher torque as output to the propeller shaft. Ignoring losses in transmission, it transfers the power generated by the engine, unchanged to the wheels of the vehicle, but at an increased torque level.

## power = torque × rpm

Since power transmitted remains the same, an increase in torque implies that the rotational speed (rpm) must decrease proportionately. When the vehicle starts from rest, its wheels are stationary, i.e., rpm = 0. Initial torque required to move the vehicle from rest is high, with a steady reduction in torque requirement as the vehicle picks up momentum. In contrast to this desired profile, the engine is running at a constant rpm (the optimum speed specified for maximum efficiency), and thereby producing a constant torque. The torque converter acts as an interface between the engine and the rest of the power transmission unit, facilitating generation of maximum power by the engine at constant rpm (and thereby constant torque) while providing a varying torque as dictated by the vehicle's dynamics.

The principal elements of a torque converter include an input shaft, impeller, turbine, stator, and output shaft. Power is transmitted from the engine to the input shaft which is directly coupled and thus rotating at the same speed (rpm). The impeller, which has a fan-like construction composed of several vanes that project radially outward from a core, is fixed to the input shaft and therefore rotates at the same speed. The outer ends of the radially projecting vanes are attached to a shell which together with the core divide the space within them into compartments resembling distorted doughnuts. The turbine resembles the impeller except for the curvature of its vanes. The turbine core is fixed to a hub mounted on the output shaft. The impeller and turbine are enclosed in a housing containing fluid. Wedged between the turbine and impeller is the stator which is similar to them in construction.

When the impeller attached to the input shaft rotates, it sets the fluid inside the housing in rotation with it. Centrifugal forces acting on this rotting fluid cause it to move from the core (which is at a radially smaller distance from the axis of rotation of the shaft) towards the shell. Thus the velocity of the fluid particles has two components; a tangential component provided by the impeller vanes causing the fluid to rotate with them, and a radial component imparted by the centrifugal forces causing the fluid to move along the length of the vane from core to shell. Having reached the (radially) outermost point along the vane, the fluid particles are prevented from any further displacement radially by the shell. This causes them to enter the spaces between the vanes of the turbine, driving the (initially) stationary fluid there radially inward towards the core. This sets up a circulatory flow in a plane perpendicular to the plane of rotation of the impeller. The curvature of the turbine vanes changes the direction of circulatory flow so that fluid particles leaving the turbine vanes (at a radial distance near the core) now flow toward the impeller. This change in velocity produces a reaction on the turbine vanes, forcing them to rotate in the same direction as the impeller. Before the fluid particles re-enter the impeller vane passages, they pass through the spaces between the stator vanes. Since the stator is mounted on a fixed shaft (it does not rotate unlike the turbine and impeller), it reduces the rotational component of the fluid particles to zero, thus leaving them with only a circulatory flow component as they re-enter the impeller. The impeller vanes again impart a rotational velocity component to the entering particles and a new (circulatory) cycle begins.

With every circulatory cycle of fluid flow energy is transmitted from the impeller to the turbine which in turn drives the output shaft. The difference in rotational speeds between the impeller and turbine is proportional to the percentage increase of output torque over input torque. As the output shaft picks up speed (the vehicle gains in momentum) the difference between input and output shaft speeds decreases, reducing the output to input torque ratio, until it reaches a ratio of one. This corresponds to directly coupling the two shafts, bypassing the torque converter. This is achieved by a clutch, a detail that we need not concern ourselves with in this paper beyond noting its presence as one element in the torque converter assembly.

## Appendix C - Sample Displays of the Expert System Prototype

## Consultation for: TORQUE CONVERTER DECISION SYSTEM"

"the test results for input torque, 1...::YES"

"the input torque at STALL ::1200"

"the torque ratio at STALL :: unknown"

"the leakage at STALL :: unknown"

"the tests for input torque, efficien... :: NO"

"the tests for input torque, efficien... :: NO"

"the test for efficiency and leakage...::NO"

## TORQUE-CONVERTER-1 CONCLUSIONS:

The name of the part which could be causing the failure is as follows:

## IMPELLER (75%) STATOR (25%)

## Test for stall input torque high with small difference

"the test results for input torque, 1...::YES"

"the input torque at STALL :: 1080"

"the torque ratio at STALL :: unknown"

"the leakage at STALL :: unknown"

"the tests for input torque, efficien... :: NO"

"the tests for input torque, efficien... :: NO"

"the test for efficiency and leakage....:NO"

## TORQUE-CONVERTER-1 CONCLUSIONS:

The name of the part which could be causing the failure is as follows:

## IMPELLER CF (8%) HOUSING CF (8%) BEARING CF (8%) CARRIER (75%)

## Consultation for: TORQUE CONVERTER DECISION SYSTEM

"the test results for input torque, 1...::YES"

"the input torque at STALL ::800"

"the torque ratio at STALL :: unknown"

"the leakage at STALL :: unknown"

"the tests for input torque, efficien... :: NO"

"the tests for input torque, efficien... :: NO"

"the test for efficiency and leakage...::No"

## TORQUE-CONVERTER-1 CONCLUSIONS:

The name of the part which could be causing the failure is as follows:

IMPELLER (75%) STATOR (25%)

## Test for stall input torque low with small difference

"the test results for input torque, 1...::YES"

"the input torque at STALL ::950"

"the torque ratio at STALL :: unknown"

"the leakage at STALL :: unknown"

"the tests for input torque, efficien... :: NO"

"the test for efficiency and leakage...::NO"

## TORQUE-CONVERTER-1 CONCLUSIONS:

The name of the part which could be causing the failure is as follows: Inlet or outlet oil flow problems - blocked passage.
