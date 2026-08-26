---
otero_id: 17880
otero_key: "TB64RM6Y"
title: "Transystem tracing arrays: A macroflow analysis technique"
authors: "Lebert R. Alley"
year: "1980"
journal: "Information & Management"
doi: "10.1016/0378-7206(80)90013-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Transystem Tracing Arrays: A Macroflow Analysis Technique

Lebert R. Alley

Texas Tech University, Industrial Engineering, Texas Tech University, Lubbock, P.O. Box 4130, TX 79409, USA

The transystem tracing array (TTA) is the basic building block for a transystem flow analysis technique. It helps analyse and document the flow through a processing system. The TTA technique has helped improve the handling of system changes, diagnosis of data errors and system bugs, and user-analyst communication. It has provided a simple and clear method for obtaining a brief and unambiguous overview of the trace (flow) through an entire system. TTAs are very easy to understand; they help users and analysts avoid bogging down in numerous system details of secondary interest, while maintaining a system-wide scale of perspective. The TTA technique is well suited to both the computerized portion of information systems and to manual office tasks for forms processing. The TTA method is built on a novel technique of collapsing complex composite dimensional arrays into simple two-way arrays.

Keywords: Database, Data Flow, User-Analyst Communication, Change Control & Evaluation, Error Tracing, HIPO, User Procedures, Debugging, Documentation, Change Costs, Cost Overruns, Tertiary User Impacts, Arrays.

![](/api/attachments/TB64RM6Y/fulltext/images/11fd0e285a801cde6fe35003eee09fce7cc2f3575524a187fce647d58c2c527b.jpg)

Lebert Alley recently joined the Industrial Engineering faculty of Texas Tech University, Lubbock, Texas. Since 1964 he has been a practitioner and manager in data processing, as well as a nationally active lecturer, specializing in systems analysis and project management methodologies. He has been employed in the Information Systems area by the federal government, in state government, private business, and university administration. He has held faculty appointments at universities in Missouri, Nebraska and Texas. His Ph.D. is in Management Systems Engineering, and he holds masters degrees in Computer Science and Physics and a bachelors degree in Mathematics.

## 1. Introduction

There is a set of particularly nagging problems for practicing information systems analysts and managers (and users) that seem to never be really solved. These problems continually recur, whittling away at the effectiveness of information systems, productivity of analysts, and satisfaction of users. Within that set of problems are, typically:

\- Documentation not understandable by both analysts and users, due to jargon;

\- Analysts and users interpreting individual documentation items differently (but not knowing it until later);

\- System change costs overruning estimates;

\- Unsuspecting users disappointed by changes implemented for other users;

\- Data input errors difficult to trace backcast, and correct;

\- Second order effects of processing design changes that are difficult to foresee.

The transsystem tracing array (TTA) technique was developed to help address these specific problems while the author was Management Systems Manager for a multiple datacenter facility in a midwestern organization with 12,000 employees, 400 user departments, scores of application systems, (and numerous problems!). The technique was further refined (and streamlined) to its present form while using it in collaboration with information systems staffs at several other organizations.

The strategy for addressing the problems was based on a single unique proposition: that each problem would be significantly diminished, if not solved, by developing some extremely simple mechanism for helping users and analysts trace the macroflow of complex systems while disregarding the intricacies of processing and file manipulation algorithms.

## 2. Developing Transystem Tracing Arrays

A considerable amount of theoretical formalism has been developed to describe and to extend the basic TTA technique to cover many practical circumstances found in information systems. However, for purposes here, the essence and simplicity of the basic method are best described by a specific illustration. It should be noted that the “80/20 rule” applies to the TTA methodology. That is, in a majority of situations, a small subset of the fully generalized TTA method has been found to provide solid, practical benefits. An overview of the TTA method is illustrated in the three consecutive steps below.

## 2.1. Step 1

First, each significant information system component is classified as either a passive Object or an active Process. For this particular illustration some categories are listed in Table 1. The Objects have two roles: as the input to, or the result of, a Process.

All the elements under each category of components are listed for the particular system of concern. For example, Table 2 lists a few of the typical elements for a personnel information system. A single stage of system processing is described by identifying all input and resulting objects for each processing element, as illustrated in Figure 1. (Note the generic similarity between Figure 1 and HIPO charts. This illustrates that the TTA method is quite compatible with HIPO, but does not require or replace HIPO as a design aid).

The transystem tracing array in Figure 1 is the basic building block and starting point of the TTA method. It answers the question, "Given an individual Processing element, which resultant Object elements can be affected by each individual input Object element?" For example, in Figure 1, we can trace the effect of changes to or errors in source document D2 on data element E3. The subsequent simplification and composition of several such arrays, representing the entire scope of the system rather than just one processing stage, has proved to be surprisingly helpful.

## 2.2. Step 2

Step 1 will have yielded a separate TTA for each of the individual active Processing stages, such as were listed in Step 1-a. In our example, there would be four TTA's, (i.e., O, T, P, R).

The reason for the TTA being especially useful as a post-development tool becomes clear. If the system processing elements have been programmed and frozen (until some new system release edition), then the three-axis CTA can be collapsed into a simplified 2-axis array that omits unnecessary reference to the details of processing algorithms. In fact, it even obviates any reference whatever to these constant elements, leaving full attention to be devoted to the only system components that are subject to change during normal system operation: that is, the passive Objects directly.

Table 1. STEP 1-a. Sets of Relevant System Components are Identified

<table><tr><td>Passive Objects</td><td>Active Processes</td></tr><tr><td>D. Source documents</td><td>O. Office Tasks (originating)</td></tr><tr><td rowspan="2">E. Data elements in a data base or file</td><td>T. Update transactions</td></tr><tr><td>P. Computer System process</td></tr><tr><td>R. Printed reports</td><td>R. Office Tasks (reacting)</td></tr></table>

Table 2. Specific System Entities Listed as Elements Within Each Category

<table><tr><td>Source Documents</td><td>Update Transactions</td><td>Data Elements on Data File</td></tr><tr><td>D1. New Employee Form</td><td>T1. Add record to fill</td><td>E1. I.D. Number</td></tr><tr><td>D2. Employee Status Changes</td><td>T2. Change Job Location</td><td>E2. Dept. Number</td></tr><tr><td></td><td>T3. Change Status</td><td>E3. Marital Status</td></tr><tr><td></td><td></td><td>E4. Residence Status</td></tr><tr><td></td><td></td><td>E5. Vacation Status</td></tr></table>

![](/api/attachments/TB64RM6Y/fulltext/images/9ae6ae5520caf73230c40cca5484e59a5d4b24ff3dd81d3d1d6f1b27e283351e.jpg)  
Fig. 1. The Basic Consequence Tracing Array (CTA).

The collapsed version of the TTA in Figure 1 is illustrated in Figure 2. The collapsed TTA answers such questions as, "For which source documents might we require changes in user procedure manual instructions if we change the definition of data element E4?"

No major new benefits are provided by the collapsed TTA over existing alternative analytic techniques. Still, there has been some preference shown in practice for their stand-alone utility, even apart from the context of the overall TTA method which subsequently uses them.

## 2.3. Step 3

It is clear that most of the elemental Objects in a system will serve as both inputs to some processing stages, yet the result of other stages. And in fact many elements, especially data elements, will serve in both input and resultant roles within a single processing stage (e.g., updating a year-to-date total payroll). Ultimately, these circumstances catenate to form a multistage chain of consequences spanning the full scope of system processing operations. The cumulative result is that the chain of processing stages manifests a dependence of any final report upon a specific set of original, input source documents. The TTA method provides for a catenation of several collapsed TTA's, to form a simple composite array of any number of stages, spanning either the entire system or any part of it.

![](/api/attachments/TB64RM6Y/fulltext/images/1d2a4cb8fc1ccd8a4af0649626b9c7d53879eec4bee35de5d11c3c4b151ac764.jpg)  
Fig. 2. Collapsed CTA.

![](/api/attachments/TB64RM6Y/fulltext/images/31a0997eb029d78b215753e426b4bc1cd28163a72097903b9750d09ab7c76fb5.jpg)  
Fig. 3. Composition of Collapsed CTA's.

Figure 3 illustrates the composition of two chronologically sequential arrays. This figure corresponds to having collapsed the update Transaction (T) and System Processing (P) stage from the earlier example. Figure 4 illustrates how the two-stage span of Figure 3 is collapsed to provide a very clear and simple single-stage equivalent representation. In a similar manner, a single-stage equivalent for an entire system or subsystem can be constructed. The use of such single-stage equivalents for complex subsystems has alone proven to be very helpful in improving user-analyst communication, and user understanding of the systems.

![](/api/attachments/TB64RM6Y/fulltext/images/029c661c23abab27d5a5d0fb4a1b156f7282ebe928cb0e45e7252d895be643dd.jpg)  
Fig. 4. Collapse Composite CTA's to form a Single-Stage Equivalent System.

## 3. Other Considerations

The simplified illustration described above gives a good characterization of the salient features of the fully generalized and theoretically formalized TTA method. Certainly, the interested analyst (or user) will be able to adopt the basic 3-step method described here.

It should be noted that several special cases and variations of practical importance in real systems have been accommodated by the general TTA methodology. These are merely mentioned here to give readers some ideas how to expand or adapt the TTA method to their own needs. All deal with configuration of the chain formed by multistage catenation, in Step 3.

Cycling is the multistage effect of an active processing stage operating recursively on its own output categories, to form tertiary consequences. In addition to such single stage cycling is the broader concept of multistage cycling. For example, in the system processing stage (P) of the illustration, a chained serial relationship between the three data elements, employee gross pay, employee year-to-date gross pay, and company year-to-date gross pay expense could be established by separate processing elements. In this instance, all elemental objects, both input and resulting, are data elements.

Within a data base environment, especially where data elements and segments are not application-specific, the potentially complicating aspects of divergent and convergent branching in the TTA chain are actually handled quite simply. Multiple applications or systems (active Processing stages) "feeding" into or out of a set of passive Objects are simply listed, as shown in Figure 1.

Extensions of the above branching concepts leads to the identification criteria for parallel independence and closed sets of active processing algorithms. In some instances, this leads to improved job scheduling.

The TTA technique has a much higher potential benefit in a well-designed data management environment. For example, the promulgation of system change evaluation procedures and specific assignment of data quality assurance responsibilities go hand in hand with the success of this (and most any other) systems analysis tool.

## 4. Conclusion

Reflection on the historical evolution of systems science exposes the important roles of both new concepts and the new techniques for proceduralization of the new concepts. The transystem tracing array technique described here presents some new contributions in each of these areas. Certainly, no major new discoveries in systems theory are unveiled. Nor has yet another intricate and complex new systems analytic procedure been unfolded. However, we have outlined a simple and easy to understand analysis and communication aid which has achieved solid results. It may well help the readers solve some of the nagging, recurrent problems in their own organization.
