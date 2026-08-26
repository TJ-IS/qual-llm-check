---
otero_id: 25898
otero_key: "PYCU2552"
title: "A method to help end‐users validate the functional specification for a computer system"
authors: "T. Moynihan; N. O'Connor"
year: "1991"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1991.tb00036.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A method to help end-users validate the functional specification for a computer system

T. Moynihan and N. O'Connor

School of Computer Applications, Dublin City University, Glasnevin, Dublin 9, Ireland

Abstract. Described is a method to help users for a proposed computer system validate the functional specification for that system. Users construct an object-oriented model of the proposed functionality from the specification. The process of building the model improves users' understanding of the system and helps them identify any deficiencies in the specification. The method is applied to a real specification and a number of serious anomalies are found which would probably have been missed by a traditional review or walk-through. It is concluded that the method is probably helpful, robust and reproducible for 'transformational' computer systems of low or moderate complexity.

Keywords: functional specification, requirements analysis.

## INTRODUCTION

The established waterfall model of the system-development lifecycle is gradually being replaced by paradigms which emphasize the use of techniques such as prototyping and incremental delivery (Weinberger & Freedman, 1984). A major goal of these new approaches is to make the functionality in a proposed system 'visible' in a concrete way to end-users at an early stage in the development process. Despite these trends, most systems are still developed using the traditional, developmental lifecycle, thus the familiar paper-based 'functional specification' has not yet lost its importance. In most development projects, it is still the 'baseline' for the agreement between the developer and the user and frequently has a legal/contractual significance.

By its nature, a paper-based functional specification is an abstract, 'life-less' representation of a proposed system. If written in natural language as most still are despite the existence of formal methods, the specification will probably suffer from weaknesses such as ambiguity and inconsistency. Thus, for other than the simplest of systems, the task of understanding precisely what is being proposed can be a difficult one for users.

In this paper we describe a method to help the end-users of a proposed computer system, critically assess the functional specification of the system. The method involves the construction, by users, of a rigorous model of the functionality described in the specification. The process of building the model raises the users' level of understanding of the specification and helps users spot possible problems or anomalies in the document. We do not lay claim to the idea of 'reverse-engineering' a rigorous description of the functionality of a piece of software from its informal specification. For example, Sufrin (1989) describes the use of z to construct a model of the functionality of the UNIX utility MAKE from its supplied user-documentation. The act of building the rigorous model helped resolve a number of apparent 'enigmas' which users had found in the documentation.

In what follows, we illustrate the approach by applying it to an early draft of the functional specification for a PC-based system which we will call 'TANGO'. The system was intended to support the operation and management of a health-screening clinic. The authors of this paper had the task of working with the clinic's staff to help them assess the degree to which the specification met their requirements. Thus the analysis described below was largely a collaborative, group effort. Functions to be provided by the proposed system included patient-appointment scheduling, medical test-data storage and retrieval and patient-billing. The draft functional-specification, which was prepared by a systems analyst in a local software house, comprised 30 pages of text and a number of diagrams showing screen and report layouts. We found it to be well written and presented. The Flesch–Kincaid Readability Index (Guillemette, 1989) was well within the acceptable range for the target readership (medical doctors, nurses and administrators). As will be seen, our analysis identified some serious problems in the specification and led to its revision. The system was subsequently developed and is now working successfully at a number of user-sites.

The approach we describe is 'object-oriented' to the extent that it makes use of the notions of object, object-class and inheritance. In particular, we have drawn on the ideas of Booch (1986), Meyer (1988) and Coad & Yourdon (1990) as these relate to 'object-oriented' systems analysis. We also use the concept of pre- and post-conditions on an operation, which derives from the field of formal specification (see Woodcock & Loomes (1988) and Jones (1990)).

## THE 'TANGO' EXAMPLE

## Step 1: identify candidate objects

The first step was to identify from the specification, the application-domain objects and object-classes which appeared to be explicitly 'recognized' by the proposed system, i.e. clinic-related objects referenced in the inputs and outputs from the system. Excluded were objects mentioned in the specification which were part of the external context of the system.

Each object was given a unique name, generally the name by which it was most frequently referred to in the specification. Also noted were any apparent synonyms for the same object. Nouns were judged to be possible synonyms if they appeared to be used interchangably in the specification or if they 'sounded' the same at a common-sense level. Further confirmation that two or more nouns really were synonyms for the one object was obtained if the same user-operations seemed to be applicable to both nouns and if they appeared to share the same attributes.

The task took about 3 hours. The candidate objects found are shown in Table 1. Most of the objects were very familiar to the users and were unambiguously identified. There was however, a significant number of 'mystery' objects which were not readily recognizable by the users (e.g. MEDICAL FORMULA). The high frequency of apparent synonyms used in the specification made the task difficult and represented a serious flaw in the specification.

## Step 2: identify object-class and assembly-structure hierarchies

The object-types shown in Table 1 are highly interrelated. Some object-types denote a super-class or sub-class of other object-types. For example, TEST is a super-class which includes DOCTORS TEST, NURSES TEST and LABORATORY TEST as sub-classes. Some object-types are assembly structures built from two or more other object-types. For example, PATIENT TEST RESULTS is the aggregate of DOCTORS TEST RESULTS, NURSES TEST RESULTS and LABORATORY TEST RESULTS. Table 1 also includes 'objects' which are actually individual instances of an object-class. For example CROWN CRISP TEST is an instance of DOCTORS TEST.

An attempt was made to identify such object structures from the specification but it proved to be considerably difficult. Only one hierarchy was explicitly described as such in the specification. Other hierarchies were implied by the author of the specification but were not made explicit. These implied hierarchies were pieced-together and made explicit only after painstaking study of the document. The task took about 3 hours. Figure 1 shows the provisional object-structures we found. The notation used to represent the structures and the semantics of this notation are those of Coad & Yourdon (1990). The ISA relationship represents total, disjoint specialization. The 'part of' relationship in an assembly-structure is represented with a triangle pointing to the aggregate object. The semantics of the 'part of' relationship as used by Coad & Yourdon, does not distinguish between logical and physical aggregation. In the particular example of aggregation shown in Figure 1, as the aggregate object is PATIENT TEST RESULTS, the aggregation is logical.

This exercise was found to be very valuable. It greatly added to the understanding of the scope and static structure of TANGO and is a nice example of abstraction in action!

## Step 3: identify attributes and user-operations for each object

The next step was to identify the attributes of each candidate object and the user-operations which could be applied to that object. It was found that a number of user-operations automatically triggered-off a series of 'side-effect' operations on other objects. For example, the specification states that when the user attempts to add an appointment for a new patient, the personal details of the new patient are automatically requested and a record for that patient automatically added to the patient details file, before the appointment is processed. Some of these automatically invoked operations may also be invoked directly by the user whilst others may not. To document this automatic triggering of one operation by another either above or below it in the same hierarchy or in another hierarchy, we developed a simple notation, examples of which

Table 1: Candidate objects found

<table><tr><td>Object</td><td>Synonym(s)</td><td>Object</td><td>Synonym(s)</td></tr><tr><td>Admission</td><td></td><td>Mammogram text</td><td></td></tr><tr><td>Admission notification</td><td></td><td>Medical formula</td><td></td></tr><tr><td>Admissions list</td><td>Record book</td><td>New patient</td><td></td></tr><tr><td>Appointment schedule list</td><td>Day-sheet</td><td>New patient appointment</td><td></td></tr><tr><td>Biochemistry result</td><td></td><td>Nurses test results</td><td></td></tr><tr><td>Biochemistry test</td><td></td><td>Nurses test</td><td></td></tr><tr><td>Blood data result</td><td></td><td>Output</td><td></td></tr><tr><td>Blood data test</td><td></td><td>Past history test</td><td></td></tr><tr><td>Blood pressure result</td><td></td><td>Past history test result</td><td></td></tr><tr><td>Blood pressure test</td><td></td><td>Pathology result</td><td></td></tr><tr><td>Chest X-ray result</td><td></td><td>Pathology test</td><td>Additional pathology</td></tr><tr><td>Chest X-ray test</td><td></td><td>Pathology text</td><td></td></tr><tr><td>Configuration parameter</td><td></td><td>Patient</td><td></td></tr><tr><td>Constant</td><td></td><td>Patient address label</td><td></td></tr><tr><td>Crown crisp test</td><td></td><td>Patient appointment</td><td>Visit</td></tr><tr><td>Crown crisp test result</td><td></td><td>Patient confirmation letter</td><td>Confirmation letter</td></tr><tr><td>Cytology result</td><td></td><td>Patient follow-up report</td><td></td></tr><tr><td>Cytology test</td><td></td><td>Patient letter</td><td></td></tr><tr><td>Cytology text</td><td></td><td>Patient medical report</td><td>Medical report</td></tr><tr><td>Doctor examination</td><td>Physical examination</td><td>Patient recall label</td><td></td></tr><tr><td>Doctor examination code</td><td></td><td>Patient recall letter</td><td>Recall letter</td></tr><tr><td>Doctor examination result</td><td></td><td>Patient test results</td><td></td></tr><tr><td>Doctor examination text</td><td></td><td>Personal details result</td><td></td></tr><tr><td>Doctors test</td><td></td><td>Personal details test</td><td></td></tr><tr><td>Doctors test results</td><td></td><td>Physical examination</td><td></td></tr><tr><td>ECG test</td><td></td><td>default text</td><td>Standard text</td></tr><tr><td>ECG test result</td><td></td><td>Previous visit summary</td><td></td></tr><tr><td>ECG text</td><td></td><td>medical report</td><td>Patient summary medical report</td></tr><tr><td>Family history test</td><td></td><td></td><td></td></tr><tr><td>Family history test</td><td></td><td>Printer parameter</td><td></td></tr><tr><td>Family history test result</td><td></td><td>Report</td><td></td></tr><tr><td>GP Letter</td><td>Doctors letter</td><td>Report parameter</td><td></td></tr><tr><td>Haemocult test</td><td></td><td>Returning patient</td><td></td></tr><tr><td>Haemocult test result</td><td></td><td>Returning patient appoint-ment</td><td></td></tr><tr><td>Haematology result</td><td></td><td>Sample identification label</td><td></td></tr><tr><td>Haematology test</td><td></td><td>Screening doctor</td><td>Doctor</td></tr><tr><td>Haematology text</td><td></td><td>Screening nurse</td><td>Nurse</td></tr><tr><td>Hearing test</td><td>Audiometry test</td><td>Screening type</td><td></td></tr><tr><td>Hearing test result</td><td></td><td>Social habits test</td><td></td></tr><tr><td>Height and weight result</td><td></td><td>Social habits test result</td><td></td></tr><tr><td>Height and weight test</td><td></td><td>Test</td><td></td></tr><tr><td>Invoice</td><td></td><td>Test result code</td><td></td></tr><tr><td>Label</td><td></td><td>Test result ideal range</td><td></td></tr><tr><td>Laboratory test</td><td></td><td>Urinanalysis result</td><td></td></tr><tr><td>Laboratory test results</td><td></td><td>Urinanalysis test</td><td></td></tr><tr><td>Letter</td><td></td><td>Vision result</td><td></td></tr><tr><td>Lung function result</td><td></td><td>Vision test</td><td></td></tr><tr><td>Lung function test</td><td></td><td>X-ray text</td><td></td></tr><tr><td>Mammogram result</td><td></td><td></td><td></td></tr><tr><td>Mammogram test</td><td></td><td></td><td></td></tr></table>

![](/api/attachments/PYCU2552/fulltext/images/bf6e6245f6549897d3091de1ec81b5271198fff1442fafe1062518b32fa5fc9c.jpg)  
Figure 1. The object class hierarchies.

Table 2. Candidate objects for which no operations and no attributes could be found

<table><tr><td>Admission</td><td>Medical formula</td></tr><tr><td>Admission notification</td><td>Doctor examination code</td></tr><tr><td>Mammogram text</td><td>ECG text</td></tr><tr><td>Test result ideal range</td><td>Haemotology text</td></tr><tr><td>Test result code</td><td>Pathology text</td></tr><tr><td>Doctor examination result</td><td>X-ray text</td></tr><tr><td>Doctor examination</td><td>Cytology text</td></tr><tr><td>Physical examination default text</td><td>Doctor examination text</td></tr></table>

![](/api/attachments/PYCU2552/fulltext/images/3681bbef2dbc276f5d6c3f57b62eae86b39e05d08522c32f621dbdd6b7238e9b.jpg)  
This shows that 'Add New Patient' is automatically  
triggered by Make New Appointment.

![](/api/attachments/PYCU2552/fulltext/images/19c581843484a40e209bad9029f7977adb86d85fce704695f9e7c4397301a643.jpg)  
This shows that 'Make New Patient Appointment' automatically triggers 'Add New Patient'.  
(See 'New Patient' in this figure)

Figure 2. Examples of attributes and operations.

may be found in Figure 2. The notation used, whilst adequate for TANGO, would probably need more formalization to cope with cases of complex triggering behaviour between operations. Petri-Net graphs might be a suitable basis for any needed formalization.

The analysis of TANGO's operations was restricted to those explicitly described in the specification. No attempt to 'second-guess' the author of the specification was made; if an operation or an attribute was not explicitly mentioned, its existence was not surmised. Difficulty was encountered in gathering the attributes and operations for many of the objects because these were not explicitly recorded in an 'easy to get at way' in the document. The presence of apparent synonyms for some attributes and operations added to the difficulty of the task. Typically, it took about 30 minutes to document a 'straightforward' object but it took up to 90 minutes to piece together the attributes and operations for a less explicitly described or 'scattered' object.

The process unmasked a number of apparent anomalies in the specification (or in our interpretation of it!). For some 'objects', no attributes and no operations mentioned in the specification could be found. Whilst one can accept the notion of an object having no attributes, it is hard to accept the notion that a meaningful object would have no operations associated with it. Were the omissions an oversight on the part of the specifier? Or was the problem created by the authors who may have mistakenly reified into objects some items that the specifier intended to play the role of mere attributes. Perhaps the apparently 'empty' objects were simply unrecognized synonyms for already identified non-problematic objects. These anomalous 'objects' are listed in Table 2.

In Figure 2 we show some of the attributes and all of the user-operations we identified for two of the object-class structures. For economy and clarity of presentation, we made full use of 'inheritance' in that we located each attribute and user-operation in the most general object-class to which it appeared to apply. Members of sub-classes inherit these attributes and operations from their super-classes. Figure 2 is a small example of the descriptive power of abstraction and inheritance when used in combination!

## Step 4: identify instance-connections between candidate objects

An instance-connection is a constraint in the existence of an instance of an object-class. For example, a set of test results for a patient (i.e. PATIENT TEST RESULTS) can exist only if there is a corresponding PATIENT APPOINTMENT during which the tests were administered. A PATIENT LETTER (i.e. a letter to the patient summarizing the results of his/her tests) can exist only if his/her full MEDICAL REPORT on which the summary is based, exists. Instance-connections are an important component in the description of any system.

Figure 3 shows the instance-connections we could identify from TANGO documentation. The instance-connections are drawn at the highest level of generalization at which they appear to apply. Thus lower level object-classes are shown only if they participate in instance connections in which the more general or aggregate object does not participate. The cardinality of each connection is also shown. We have used our own notation to express the cardinality of an instance connection. For example, APPLE<3:5----2:2<ORANGE shows that each instance of APPLE must be associated with exactly two instances of ORANGE and that each instance of ORANGE must be associated with three, four or five instances of APPLE. Where the cardinality of an instance-connection could not be fully determined from the specification, a '?' is shown in place of the unknown information. Unlike the relationships in an entity-relationship diagram, the instance-connections in an instance-connection diagram are not named. This is a deliberate omission. The purpose of the diagram is limited to documenting the existence of instance-connections and their cardinality.

![](/api/attachments/PYCU2552/fulltext/images/b8860a375b2d52f4968eeba31adec2b4902c0ba83ba24c17b7cc44d2e134e940.jpg)  
Figure 3. Instance connections.

The task of constructing Figure 3 from the specification was quite difficult because few instance connections were explicitly identified. The task took about 4 hours to complete. Once again, we did not 'second-guess' the author of the specification.

A number of apparent anomalies were identified. These fall into the following two categories.

## 1 The existence of seemingly 'disconnected' objects

Despite our best efforts, we failed to identify any instance connections for 16 candidate objects (see Table 3). Maybe connections exist but they could not be deduced from the documentation. These 16 'disconnected' objects happen to be the same 16 'objects' for which no attributes and operations could be found (see Table 2).

## 2 The existence of instance connections of unspecified cardinality

The cardinality of four instance connections could not be established from the user-documentation:

```txt
PATIENT<1:1----0:?>PATIENT APPOINTMENT
NURSES TEST RESULTS<?:1----?:7>NURSES TEST
DOCTORS TEST RESULTS<?:1----?:6>DOCTORS TEST
LABORATORY TEST RESULTS<?:1----?:8>LABORATORY TEST
```

These unspecified cardinalities raise a number of questions which could be of great importance to potential users of TANGO. For example, can only one future scheduled appointment exist at any given time for a patient? Or is it possible to stack-up a number of future appointments for a patient? If some of the nurses', doctors', or laboratory tests are not administered to a patient, do the test results for the tests which are administered constitute a valid set of patient test-results?

Table 3. Candidate objects apparently participating in no-instance connections

<table><tr><td>Admission</td><td>Medical formula</td></tr><tr><td>Admission notification</td><td>Doctor examination code</td></tr><tr><td>Mammogram text</td><td>ECG text</td></tr><tr><td>Test result ideal range</td><td>Haemotology text</td></tr><tr><td>Test result code</td><td>Pathology text</td></tr><tr><td>Doctor examination result</td><td>X-ray text</td></tr><tr><td>Doctor examination</td><td>Cytology text</td></tr><tr><td>Physical examination default text</td><td>Doctor examination text</td></tr></table>

## Step 5: first review session with the specifications' author

In steps 1–4 we identified a number of 'puzzles' in TANGO's specification. Before proceeding any further with our analysis of the document, a review session was held with its author (a systems analyst in a local software house) to confirm the validity of the analysis and to sort out the 'puzzles'. The review session took about 1 hour to complete.

Table 1 was reviewed first. It was confirmed that all but one of the candidate synonyms really are synonyms. VISIT is not a synonym for PATIENT APPOINTMENT as had been thought, but is a synonym for ADMISSION.

Table 4. Pre- and Post-conditions for user operations

<table><tr><td>Object</td><td>Operation</td><td>Pre-condition</td><td>Post-condition</td></tr><tr><td rowspan="2">Patient</td><td>Display patient details</td><td>Patient present</td><td>(self evidence)</td></tr><tr><td>Amend patient details</td><td>Patient present</td><td>(self evident)</td></tr><tr><td rowspan="7">Patient appointment</td><td>Modify</td><td>state indicator = 1 or ?</td><td>state indicator unchanged</td></tr><tr><td>Cancel</td><td>state indicator = 1 or ?</td><td>state indicator = 2</td></tr><tr><td>Reinstate</td><td>state indicator = 2</td><td>state indicator = 1</td></tr><tr><td>Admit</td><td>state indicator = 1</td><td>state indicator = 3</td></tr><tr><td>Unadmit</td><td>state indicator = 3</td><td>state indicator = 1</td></tr><tr><td rowspan="2">Clearout</td><td>date of visit earlier than 3 months ago and if state indicator = 3</td><td>Patient appointment moved to archive table</td></tr><tr><td>if state indicator ≠ 3</td><td>Patient appointment deleted from system</td></tr><tr><td colspan="4">Sub-types:</td></tr><tr><td>New patient appointment</td><td>Make new patient appointment</td><td>Patient not present</td><td>Patient present and Patient Appointment present with state indicator = 1</td></tr><tr><td>Returning patient appointment</td><td>Make returning patient appointment</td><td>Patient present and no patient appointment present for this patient with statement = 1 and Patient Appointment present for this patient with state indicator = 3</td><td>Patient Appointment present with statement indicator = 1</td></tr></table>

Tables 2 and 3 were reviewed next. These list, respectively, objects that are apparently 'empty' (i.e. have no attributes and no operations) and objects that do not seem to participate in any instance connections. We learnt that DOCTOR EXAMINATION actually consists of 19 different tests, called PHYSICAL EXAMINATION TESTs, which involve examining some physical attribute of the patient (for example, his/her eyes). Each of these tests is identified with a unique code (DOCTOR EXAMINATION CODE synonym for which is TEST RESULT CODE) which is an attribute of the test rather than an object in its own right. The result for a test is DOCTOR EXAMINATION RESULT. Associated with each test is a paragraph of standard text (PHYSICAL EXAMINATION DEFAULT TEXT). The doctor may include this paragraph of text in the PATIENT MEDICAL REPORT if the result of the test is 'normal'. If the result is 'abnormal', the doctor may generate his/her own text (DOCTOR EXAMINATION TEXT).

We learnt that MEDICAL FORMULAs and TEST RESULT IDEAL RANGEes are algorithms and constants respectively to be used by the system when computing PATIENT TEST RESULTS. These object types appear to be 'hard-coded' into the system. The term ADMISSION NOTIFICATION was used in error in the specification. It should have read APPOINTMENT NOTIFICATION and is a further synonym for PATIENT CONFIRMATION

LETTER. The term ADMISSION refers to a PATIENT APPOINTMENT for which the PATIENT has attended and undergone tests. MAMMOGRAM TEXT, ECG TEXT, HAEMOTOLOGY TEXT, PATHOLOGY TEXT, X-RAY TEXT and CYTOLOGY TEXT refer to free text paragraphs which may be generated by staff at the clinic for inclusion in the PATIENT MEDICAL REPORT if, for example, the results of any of these tests are abnormal.

Figure 3 (Instance Connections) was reviewed next. It was confirmed that the analysis was correct. The four instance connections for which cardinalities could not be found were examined in particular. It was established that the system will allow only one future, scheduled PATIENT APPOINTMENT to exist for any PATIENT (i.e. future appointments can't be 'stacked up' for a patient). Also a partial set of test results does constitute a valid set of PATIENT TEST RESULTS (i.e. not all tests must be administered to a patient).

Following the review, the various diagrams were amended as necessary. The revised diagrams are not shown in this paper.

## Step 6: extract the pre- and post-conditions for each operation

Next, an attempt to identify the pre- and post-conditions for each user-operation was made. This was found to be a difficult task as few of the conditions were made explicit in the specification. It required careful 'reading-between-the-lines' to construct them. Because of this the analysis may have been inaccurate and incomplete. Table 4 shows an extract from the 'best shot'. As in earlier analyses, each operation was attached to the most general object-class to which it appeared to apply. Where the pre- or post-conditions seemed to differ for a sub-class, this was made explicit in the diagrams. This use of abstraction greatly simplified the presentation.

The notation used for recording the conditions is fairly informal, but it was adequate for this purpose. Had the complexity of the application been greater, we would have been forced to use a more formal and elaborate notation such as that used in VDM (Jones, 1990) or Z (Woodcock & Loomes, 1988) would have been necessary. In some of the conditions, a 'state-indicator' (Skidmore et al., 1990) was introduced. The use of the state-indicator helped us express constraints on the sequences of operations which could be validly applied to an instance of an object-class, and helped us express alternative post-conditions where the effect of an operation was contingent on the internal state of the object.

In addition to a general feeling of unease about the accuracy and completeness of the analysis of pre- and post-conditions, a number of specific ambiguities in the documentation were identified. For example, can the details of a PATIENT APPOINTMENT be modified after the PATIENT has been admitted? Can a PATIENT APPOINTMENT which has not resulted in an ADMISSION but which is less than 3-months-old (and thus not removable by 'clearout') be cancelled? To make a RETURNING PATIENT APPOINTMENT must there exist an instance of a previous, admitted PATIENT APPOINTMENT for this PATIENT?

## Step 7: confirm the existence of operations to add, modify and remove instances of each object-type

By its nature, one would expect any information system to provide user-operations to add and delete instances of persistent objects and operations to modify the values of their attributes. An exception to this generalization would be an object, such as a table of 'hardwired' constants, which by design the user is not allowed to change. In step 7, an instance of each object-class was walked-through its lifecycle was explored and the presence of these basic operations was confirmed or otherwise. If these operations are missed from the specification, it may signal an inadvertent omission from the specification — or a deliberate design decision which may have important implications for the user. Table 5 shows those object-classes for which one or more of the basic operations could not be found. Once again, full use was made of abstraction in presenting the results.

Table 5. Persistent objects for which no Create, Amend or Remove user-operations could be found

<table><tr><td>Object</td><td>Create operations</td><td>Amend operations</td><td>Remove operations</td></tr><tr><td>Patient</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Test</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Medical formula</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Test result ideal range</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Physical examination default text</td><td>No</td><td>No</td><td>No</td></tr></table>

Table 5 presents a number of puzzles. While a new instance of PATIENT is automatically created when a NEW PATIENT APPOINTMENT is made, there appeared to be no operation which allows the user to directly create a new instance of PATIENT. Can a new patient be added only in the context of that patient making his/her first appointment?

It appeared that instances of the following objects were to be 'hard-wired' into the system and could not be added, changed or removed by the user: TEST, MEDICAL FORMULA, TEST RESULT IDEAL RANGE and PHYSICAL EXAMINATION DEFAULT TEXT. The first three of these object-classes specify the various tests to be applied to patients and contain parameters and algorithms for processing test results. Thus they are very central to the operation of the system. Perhaps user operations for their maintenance were intended but they did not appear in the specification.

## Step 8: second review session with the specification's author

The purpose of this step was to confirm the validity of the analysis in steps 6 and 7 and to feed back the new 'puzzles' encountered in the specification. The review session lasted about 30 minutes and the objectives were achieved. The specification was subsequently revised.

## CONCLUSIONS

In an ideal world, systems would be formally specified and users would be able to read and understand formal specifications. In practice, this is not the case! For the foreseeable future, most users will expect functional specifications to use natural language and understandable diagrams. But natural language lacks precision. So functional specifications can be ambiguous and may contain errors and anomalies which are hard to spot. In this paper we have described some ideas to help end-users validate a functional specification. In terms of degree of rigour, the ideas seem to occupy the middle ground between traditional structured systems analysis and design representations (e.g. data-flow diagrams, entity-relation diagrams) and formal representations such as z or vDM.

Does the particular process described here work? Is it cost-effective? Is there any alternative approach with which this approach can be compared? Let us address the last of these questions first. We believe the approach is fairly novel. The idea of having users work together to construct a rigorous model from a traditional functional-specification does not appear to have been tried before. Perhaps the most comparable method is the traditional walk-through (Weinberger & Freedman, 1984). In a walk-through, the author of the specification leads a group of users through the document and answers queries and notes problems. The process of a walk-through is far more passive and unstructured than the process we propose. In the case of TANGO, we are confident that our process uncovered problems in the specification, which a walk-through would have missed. To date, three groups of end-users have used the process on three different specifications to good effect. They had no difficulty understanding the techniques. We believe this is because the constructs in the object-oriented approach closely match those in the typical user's 'mental model' (Carroll & Olson, 1988) of an information system and thus have intuitive appeal. A further advantage of the representations used is their similarity to those emerging from object-oriented approaches to systems analysis, design and implementation (Korson & McGregor, 1990). Thus, familiarity with the ideas will probably benefit users in the longer term.

Obviously there is a cost associated with using the process. For example, the analysis of the TANGO specification and the review sessions with the specification writer took about 3 man-days of users' time. To finish on the theme of the cost-effectiveness of the proposed approach, we must admit that we cannot yet provide hard evidence to demonstrate that our approach is more cost-effective than the traditional walk-through. Substantial empirical research would be needed to resolve this question.

Why did we choose the particular techniques we used? Would other techniques have been more effective? In addressing this question, it is important to note that we are proposing a PROCESS in which a number of techniques are used in sequence. So the question of the appropriateness of the choice of any individual technique cannot be answered independently of the choice of the other techniques used. Also, the process is designed for use by end-users who cannot afford to spend significant time on special training. This imposes constraints on the formality and complexity of the techniques used. Then there is the question of the effectiveness of the 'shape' of the overall process, i.e. the particular sequence of steps chosen and the goals set for each step. Is there a better overall process? These questions cannot be answered with confidence without empirical research.

What are the limitations of the approach? In the process we have described, the focus of attention is on the functionality actually proposed in the specification, not on the functionality that should be in the specification. The question of the completeness and the appropriateness of the functionality specified is not directly addressed. The assumption we make is that the users involved in the process understand the problem domain and the 'real' requirements. The purpose of the process is confined to giving users a good understanding of what is being proposed. Clearly, though, this understanding is a good basis for subsequent judgements on completeness and appropriateness. The process and the techniques used seem to be adequate for specifications of information systems of low or moderate complexity. More elaborate techniques, with tool support, would certainly be required for complex systems. But a caveat must be entered in this regard. A major attraction of the process, as illustrated through TANGO, is its intuitive appeal to users and its perceived simplicity. If the level of formality or complexity of the techniques used were raised significantly, it is likely that users would reject the process. So, our whole approach is probably unsuited to specifications of very complex systems (but then so too is a traditional text-based functional specification!) To-date, our experience with the approach is limited to specifications for 'transformational' systems (e.g. data-processing/MIS systems which do not interact with objects in their environment in a time-dependent way). The method is probably unsuited to specifications for 'reactive' systems (e.g. real-time control systems).

How reproducible is the process? If two groups of users independently analysed the same specification, would they come-up with identical models? Would they find the same 'problems'? Again, this question can only be answered by further research. In the case of TANGO, the authors of this paper each worked with a separate group of clinic-staff on most steps of the analysis. The two groups, working independently, almost invariably found the same problems and puzzles. This is encouraging.

Finally, if the approach is helpful, why not structure the specification in this way to begin with? Why put users to the bother of building the model? It is our view that the process of building the model is the key to the success of the review. The process forces users to play an active role and results in a deeper understanding of the specification.

## ACKNOWLEDGEMENTS

This work is partially supported by the EC through the ESPRIT2 Project 'SCOPE'.

## REFERENCES

Booch, G. (1986) Object-oriented development. IEEE Transactions on software engineering, 12, 211–221.

Carroll, J.M. & Olson, J.R. (1988) Mental models in human computer interaction. In: Handbook of Human-Computer Interaction, Helander, M. (ed.), pp. 45–65. Elsevier Science Publishers.

Coad, P. & Yourdon, E. (1990) Object-oriented analysis. Yourdon Press, New Jersey.

Guillemette, R.A. (1989) The CLOZE Procedure: An Assessment of the Unerstandability of Data Processing Texts, Information and management, 17, 143–155.

Jones, C.B. (1990) Systematic software development using VDM. Prentice Hall, New Jersey.

Korson, T. & McGregor J.D. (1990) Understanding Object-Oriented: A Unifying Paradigm, Communications of the ACM, 33, 40–60.

Meyer, B. (1988) Object-oriented software construction. Prentice Hall, New Jersey.

Skidmore, S., Farmer, R. & Mill, G. (1990) Ssadm models and methods, National Computing Centre of Great Britain, Manchester.

Sufrin, B. (1989) Effective industrial application of formal methods. In: Information Processing 89 — Proceedings of the IFIM 11th World Computer Congress, Ritter, G.X. (ed.), pp. 61–69. North-Holland.

Weinberger, G. & Freedman, D. (1984) Reviews, Walkthroughs and Inspections. IEEE Transactions on software engineering, 10, 68–72.

Woodcock, J. & Loomes, M. (1988) Software engineering mathematics. Pitman, London.

## Biographies

Tony Moynihan is a professor in the School of Computer Applications at Dublin City University. He is working in the area of user-requirements capture and validation. Noel O'Connor is a graduate student in the same school and he is particularly interested in using the model generated by the process described in this paper to generate test scripts for functional testing of the implemented system.
