---
otero_id: 22420
otero_key: "NYFZE9QW"
title: "Process reverse engineering for BPR: A form-based approach"
authors: "K.-H. Kim; Y.-G. Kim"
year: "1998"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00027-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Process reverse engineering for BPR: A form-based approach

K.-H. Kim $^{1}$ , Y.-G. Kim $^{*}$

Graduate School of Management, Korea Advanced Institute of Science and Technology, 207-43 Cheonryang, Dongdaemoon, Seoul 130-012, South Korea

Received 14 July 1997; accepted 13 December 1997

## Abstract

Firms spend significant efforts identifying and representing their current business processes for business process redesign (BPR) projects. Despite the efforts, due to the lack of proper tools and methodologies, they find it difficult to decide which process to redesign and how. Considering the effort spent in the process analysis phase and limited support in the process redesign phase, we find a need for a better process modeling and redesign method. This article introduces the enterprise process reverse engineering (EPRE) method for analyzing business processes and supporting process redesign tasks. By analyzing common business forms, the method provides designers and users with guidance for process redesign as well as in generating the current process model. Working procedures are described using a sample hospital case and a set of the EPRE prototype screens. For validation purpose, we applied the method to a real BPR project for an advertising agency and report on its outcome. © 1998 Elsevier Science B.V.

Keywords: Reverse engineering; BPR; Process modeling; Form; Field type

## 1. Introduction

Relentless changes and competitive pressures in the 1990s have placed new strains on organizations and made business process redesign (BPR) a major subject of attention in academia and industry [12, 19, 34]. BPR is offered as an enabler of organizational transformation, and many organizations have embraced the BPR approach for radical performance improvement. Currently, however, there are two major challenges facing BPR implementations.

First, existing business processes have to be understood to enable the BPR team to identify the potential problem areas before creating a new process or redesigning the existing ones $[11, 17]$ . However, it is not a trivial task to identify and represent existing processes in a formal, yet easy to understand, process model $[15]$ . Most BPR methodologies rely on labor intensive approaches for capturing and modeling business processes $[4]$ . We also suffer from the relative lack of documentation compared to the elaborate and structured documentation found in systems development projects. For example, there is seldom a trace of the initial or intermediate process models when the BPR team directly translates its interview results into the new process model or shuffles hundreds of Post-It notes during the analysis phase [5].

Second, support for the process redesign should involve top management buy-in. Many process modeling formalisms originate mostly from the application development perspective $[1, 20]$ , which cannot satisfy the cross-functional, customer-oriented process nature of BPR. Accordingly, methodologies that depend on such process modeling formalisms tend to lack the necessary diagnostic mechanism. Thus, after the current processes are modeled, the question of which process to redesign and how to redesign them still remains unanswered. This explains why most of the BPR literature is restricted to descriptions of the ‘situation before’ and the ‘situation after’, giving very little information on the redesign process itself $[16]$ .

The time-consuming efforts spent in the process analysis phase and the limitations of the current methodologies in supporting the redesign phase have motivated us to develop a new method called enterprise process reverse engineering (EPRE). The EPRE method can be used in producing current process models and suggesting process redesign guidelines based on the analysis of business forms. It will facilitate the interaction among BPR managers, IS personnel, and end-users in the analysis and redesign phases of the BPR implementation process.

## 2. Literature review

## 2.1. BPR and process modeling

Despite the explosive growth of organizations implementing enterprise-wide BPR projects, there has been a disappointing track record; Hall et al. [18] estimate that between 50 and 70 percent of the firms fail to capture the expected ‘dramatic’ gains from BPR. One of the BPR implementation problems is that the firms do not have a proper method supporting systematic redesign [10, 26].

Before BPR, process modeling was mainly the task of graphically modeling the way users process their data, using techniques such as data flow diagram (DFD) [13, 14] to support the development of IS applications for functional area users. Modeling orientations were toward internal employees and the goal of the operation was to improve productivity by automating routine tasks. With BPR, process modeling takes an entirely different perspective. Instead of focusing on developing IS applications for functional areas, process modeling aims at modeling the cross-functional business processes of the entire organization. Frequently, these processes are initiated by customers and the modeling orientation reflects a strong customer perspective. BPR support tools that are application development oriented have inherent limitations to satisfy the customer orientation of BPR [22]. In this study, we adopted the event-process chain (EPC) diagram [23] since it reinforces BPR's cross-functional and customer orientation while preserving the modeling depth and abstraction mechanism.

## 2.2. Reverse engineering: Form-driven approach

Reverse engineering in the IS field involves extracting design artifacts such as program structure or data schema from the existing system $[3, 8]$ . Its main objective is to increase the overall comprehensibility of the system for maintenance and new development. Thus, reverse engineering focuses on how to extract correct and complete target objects more efficiently. Business forms, databases, data models, and program codes are the frequently adopted source objects $[7, 27, 28, 32]$ .

Business forms, due to their simplicity and availability, have long been used for recovering process and data models. Since business forms implicitly provide process information, early methods adopted them to represent process flows with form-related organizational activities $[25, 33, 35]$ . With growing interest in workflow management and groupware system, form procedures have been investigated further $[6]$ . Researchers have also adopted business forms for recovering data models such as entity relationship (ER) diagrams $[2, 24]$ . Mapping the characteristics of a form to a data schema is a relatively straightforward process, since the business form's layout and fields generally correspond to the attributes of the data model. To extract entities and their relationships, heuristics on field positioning or form hierarchy have been suggested. Table 1 analyzes the previous form-driven research in terms of purpose, target object, field type, use of field layout, and constructs.

Table 1
Analysis of form-driven research

<table><tr><td>Research criteria</td><td>Batini et al. [2]</td><td>Choobineh et al. [9]</td><td>Larson [24]</td><td>Lee [25]</td><td>Shu et al. [33]</td><td>Tsichritzis [35]</td></tr><tr><td>Purpose</td><td>Data modeling</td><td>Data modeling</td><td>Database design</td><td>Form procedure modeling</td><td>Business procedure specification</td><td>Form procedure management</td></tr><tr><td>Target object</td><td>Extended entity relationship model</td><td>Extended entity relationship model</td><td>Database view/query</td><td>Documentary procedure</td><td>Process model and specification</td><td>Form flow</td></tr><tr><td>Field type</td><td>—</td><td>6 kinds (S,U,C,F,V,FV)</td><td>—</td><td>—</td><td>9 kinds</td><td>—</td></tr><tr><td>Use of field layout</td><td>Yes</td><td>Yes</td><td>Yes</td><td>—</td><td>Yes</td><td>—</td></tr><tr><td>Constructs</td><td>Form glossary</td><td>Field clustering</td><td>Form template</td><td>Document interaction</td><td>Forms processing language</td><td>Form abstraction</td></tr><tr><td></td><td>Form hierarchy</td><td>Field hierarchy</td><td>Nested form</td><td>Procedure constraints</td><td>Process qualification</td><td>Form operation</td></tr></table>

## 3. EPRE

## 3.1. Components

Forms are generally developed to achieve local standardization and facilitate communication in business activities. Accordingly, they provide rich information on business tasks, conditions, and workflows regarding organizational behaviors $[31]$ . These characteristics led us to adopt the form as a source object for process model generation. We adopt the Choobineh et al.'s $[9]$ definition of the form as “a structured collection of variables (that is, form fields) that are appropriately formatted for data entry and display”, since this description involves the purpose, function, and components succinctly and applies to both electronic and traditional paper forms.

For the target process model, we adopt the EPC model, since it satisfies both the cross-functional and customer-oriented nature of BPR. Unlike the other internal processing-oriented modeling methods, it starts by modeling the target process from the external customer's point of view [21]. By targeting the customer-initiated processing activities, it facilitates the identification of process bottlenecks that may result in the lengthy process cycle and loss of customer satisfaction.

We categorize business activities into three types: information handling; physical and information handling; and physical. The first consists of pure information processing, for example, the determination of a shipping date for a customer order. Physical and information handling consists of actions in which information handling is a required component, for example, warehouse inventory checking. Finally, physical activity deals with actions not needing information handling, for example, part assembly operations in factories.

## 3.2. EPRE stages

The EPRE process modeling and redesign method consists of the three stages shown in Fig. 1. First, form and form field information is defined. Then, field processing activities are identified with their field types. In the second stage, initial process models, in the form of EPC diagrams, are generated. Finally, field types are examined to find opportunities for process redesign.

![](/api/attachments/NYFZE9QW/fulltext/images/6729d54c42e659bb4c91ab8819b3e193848356cfd0cd7ef055c630bdd92aeea0.jpg)  
Fig. 1. EPRE steps.

This section uses a hypothetical hospital scenario to explain the concepts of the method. The following describes the hospital's outpatient visit process.

“A patient, Tom, arrives at the hospital. He first goes to the registration’s desk in the lobby area to register for a doctor consultation. After paying the doctor’s fee, he receives a consultation slip from the registration desk. Arriving at the nurse station, he submits his slip to a nurse and waits his turn. During the consultation, the doctor prescribes medicine for him. With his prescription, Tom returns to the cashier’s desk in the lobby area to pay for the prescription. After this, he goes to the pharmacy and submits his receipt to the receptionist to obtain his medicine. Inside the pharmacy, responding to the prescription, a clerk retrieves the requested medicine from the shelf, then another clerk bottles or boxes it. Finally, a third clerk packages the medicine and sends it to the receptionist. As soon as the packaged medicine arrives, Tom receives it and leaves the hospital.”

## 3.2.1. Stage 1: Form analysis

In the first stage, the process- and form-related information is identified.

## 3.2.2. Step 1: Define forms and form fields

As a BPR project deals with major business processes that often cut across departmental boundaries and involve various people with diverse roles, we need to define the candidate business processes and the related organizational units. To identify the candidate business processes, we start with the critical success factors (CSF) of the organization [29]. Then, we derive the candidate business processes that are responsible for creating, affecting, or monitoring the CSFs. The candidate process of our hospital scenario is the outpatient visit process, which directly affects the patient satisfaction, a major CSF of the hospital. Organizational unit information consists of roles and work places that correspond to the vertical dimension of the EPC diagrams. Organizational units related to the outpatient visit process are: the registration; consultation; and pharmacy departments.

For the candidate business process to be analyzed, every form needs to be defined with its form fields. After this, naming conflicts should be resolved; these may be homonyms or synonyms. The homonym conflict occurs when two or more form fields have the same name but different meaning (for example, date for both date of birth and date of visit), whereas the synonym conflict occurs when two or more form fields have the same meaning but different names (such as patient and person name).

## 3.2.3. Step 2: Identify field set operations with field types

Definition 1. Field set operation (FSO) is defined as “a set of activities which processes one or more form fields and is performed at a single location during a single session for a specific customer service.”

An FSO is a key EPRE construct used to model the process flows and suggest redesign opportunities. In the hospital scenario, patient registration is an FSO that satisfies the definition. Every FSO is identified from the customer (service requester)'s viewpoint. When an FSO does not deal with customers directly, as in activities performed internally, the internal service requester will take the customer's role in dealing with the server [30]. Therefore at any organizational level an FSO can be seen as sustaining the customer viewpoint. Fig. 2 shows the prototype screens for the FSO Manager and Repository Manager for specifying the registration FSO performed by a clerk at the registration desk. Components are:

## 1. Organizational Unit: Name of the organizational unit conducting the FSO.

2. FSO Name: Every FSO has a unique name, which is translated into a process or event name.

3. Description: Explanation of the FSO.

4. Customer Contact: Checked if the FSO deals directly with a customer.

5. Manipulation: The effect of the FSO on field values: create; update; query; or delete.

6. FSO Time Analysis

1. Waiting Time: Average delay before start.

2. Processing Time: Average duration for completion.

7. Field Set: Each field in the set is defined by giving its name, origin, input type, and determinant which is a field whose value is used to derive or determine the value of other form fields.

Definition 2. Origin type describes where the field value originates. The value of an origin type can be either new(N) or exist(E). The former is used when the field value has not previously existed within the organization, while the latter is used when its value can be retrieved from the existing forms or database instances.

![](/api/attachments/NYFZE9QW/fulltext/images/c4b7267aa639ba2c3dc5dd4ff3b62fd2abb192c91e9f76354238e6ff3bf676be.jpg)  
Fig. 2. FSO Manager and Repository Manager windows.

Definition 3. Input type specifies how a field value is entered on a form. The input type can be either user-input(U) or system-provided(S). It is user-input when the user enters its value, but system-provided if its value is automatically assigned by the system.

We represent the type of a field in the form of [origin type, input type]. This distinction is made because, even for the same field, multiple origin and input types may exist across different FSOs, for example, the field type of the patient number field may be [new, system-provided] in the new patient enrollment FSO, since the patient number does not exist until enrollment and is assigned by the system automatically for every new patient. However, for the consultation FSO, the patient number field is [exist, user-input], since every patient who comes to the consultation FSO must already have a patient number and the doctor enters it on the prescription form.

## 3.2.4. Stage 2: Process model generation

The second stage generates the initial EPC diagrams based on the process-related and form-related information, using some heuristics. When the target process involves physical activities, user interviews may be necessary to refine the initial EPC diagrams into the final one.

## 3.2.4.1. FSO selection for sequence determination

When multiple FSOs exist within a process, a proper FSO selection order needs to be established. The FSO selection rule determines the next FSO to be analyzed, based on the common fields, determinants, and common forms. The first of these occurs when there are multiple FSOs using or inputting the same field (common field) while a common form is found when they use the same form (common form). First, an FSO with the largest number of related FSOs through common fields, determinants, and common forms is chosen because starting with such an FSO has the potential to identify the largest number of operation sequences. Then, the FSO with the next largest number of related FSOs (except the previously analyzed FSOs) is chosen for the same reason. This rule is then iteratively applied to the remaining FSOs.

## 3.2.4.2. Operation sequence

There are three basic heuristics for determining the operation sequence between two FSOs, belonging to the same process. The first uses the origin type of a common field. Consider two FSOs, the first is the registration FSO; this includes the registration number field classified as [new] type. The second is the consultation FSO which includes the same registration number field but it is classified as an [exist] type. Then, we can infer that the registration FSO occurs before the consultation FSO. The second heuristic uses the determinant information. Assume that a field f in FSO1 is defined as a determinant of the field g in FSO2. Then, to determine the value of the field g, the value of the field f must already exist. Thus, FSO1 must take place prior to the start of FSO2. The third heuristic is based on the location of a field on a form. Suppose that there is no common field between FSO1 and FSO2 and they do not have any determinant relationship. If there exists a form, we may trace the sequence of the FSOs according to the place of each form field. We assume that, in an organization where a document or a form goes through multiple levels of management ranks for reporting or authorization purposes, an FSO that deals with a form field located closer to the upper-left (or lower-right, depending on the firm's practice) corner of the common form is likely to be manipulated before the other FSO. A document that needs signatures of multiple managers is an example. FSO1 is likely to occur prior to FSO2 when FSO1 contains a signature field for a manager placed on the left-side of or above the signature field for an executive referenced in FSO2.

We can now generate an initial EPC diagram from the customer's perspective. Each FSO is converted into a process or an event in the EPC diagram. Fig. 3 shows the initial EPC diagram generated from the scenario with ‘start event’ and ‘end event’. The place of these two events should be selected from the predefined organizational unit information. The nature of wait is revealed in the form of a lower level EPC diagram if it is determined as unacceptable to the customer. For instance, if the wait at the pharmacy (W3) is unacceptably long to the customer, it is exploded into a lower level EPC diagram where the patient's medicine request plays the role of the customer.

![](/api/attachments/NYFZE9QW/fulltext/images/93e75fb4fa89ac4248220cef8fb9c316a91ec055a9726c45d3970f7cd61b26ca.jpg)  
Fig. 3. Initial EPC: Level-1.

Since initial EPC diagrams do not consider branching or physical activities, users are expected to help the analysts complete the initial EPC diagram by providing information about branching and physical activities. The portion of the physical activities included in the target business process will affect the level of the user participation. In the hospital case, the added branching is located on the flow between the consultation and payment processes. The physical activity, slip submission, is added as an event on the flow between the registration and consultation processes. After the user input to the initial EPC diagram, the completeness of the diagram is examined. Branching without conditions or processes disconnected from the process chain need to be validated for correctness. The analysts and users finally confirm the completeness of the diagram.

## 3.2.5. Stage 3: Process redesign

The last stage of the method is the process redesign stage, which is recursive because the two steps can be repeatedly performed.

3.2.5.1. Step 1: Perform intra-FSO redesign. To identify process redesign opportunities, we rely on field type information from the process generation. Field type designation for each field is dynamic. That is, the same field can have different field types in different FSOs. Fig. 4 shows an example for the fields (patient number, patient address) which have different types in different FSOs.

Field type information provides the opportunity for process improvement from the intra-FSO perspective. First, the [exist, user-input] type fields ([E,U] quadrant in Fig. 4) reflect the hidden inefficiency of the process, since [exist, user-input] type means that users (employees) must enter the field value even though the value already exists inside the organization. If possible, fields of this type should be changed into the [exist, system-provided] type. We can also consider the opportunity cost from the customer's perspective. Assume that a customer is required to input his/her credit card and personal information for every order while that information exists in the supplier firm's database, it may be an unacceptable inconvenience.

![](/api/attachments/NYFZE9QW/fulltext/images/4befd3e402f14177f46f5d343bc2959c56cbbddfecf4c0258514dbf90f9b4974.jpg)  
Fig. 4. Examples of the dynamic aspect of field types.

We define a variable, $\alpha$ , to represent the portion of the [exist, user-input] type fields among all [exist] type fields. When an organization depends heavily on manual data handling activities, we may find many FSOs with high $\alpha$ values.

The second opportunity can be found among the [new, user-input] type fields ([N,U] quadrant in Fig. 4). We can categorize them into two groups. The first consists of the fields with determinant field(s). For this group, we may change the [new, user-input] type into the [new, system-provided] type by computerization. Assuming that the total payment amount field of the medicine payment FSO is of the [new, user-input] type field, its field type could be changed into [new, system-provided], since its value can be calculated by referencing the values of the medicine number, medicine price, and medicine quantity fields. This kind of field is often found in an FSO that handles field values manually or depends on a poorly integrated IS. The second group consists of fields whose values are generated by certain rules without any determinant; these may also be changed into [new, system-provided] using an IS. An example of this may be found in the medicine request FSO, in which a receptionist issues a sequence number, the order of medicine preparation ([new, user-input]) on the paid prescription slip at the pharmacy center. The sequence number can be automatically generated and this changes the field into a [new, system-provided] type. We define another variable, $\beta$ , to denote the portion of the fields changeable into [new, system-provided] type among all [new, user-input] type fields. When an FSO has a high $\beta$ value, the possibility of reducing the inefficiency in its information handling activities is high. We can use the $\alpha$ and $\beta$ variables as the process redesign criteria during the redesigning phase of the BPR implementation process.

3.2.5.2. Step 2: Perform inter-FSO redesign. Field type also provides the opportunity for process redesign from the inter-FSO perspective. We can determine whether there is an opportunity for reducing cycle time by moving an FSO earlier in the process. This opportunity can be identified by examining the field type information.

First, we focus on the [exist] type fields ([E,U] and [E,S] quadrants) of an FSO to decide if it is properly positioned in the overall business process. Suppose that there are time gap between the current FSO having an [exist] type field and the preceding FSOs having the same field. Then the customers of the process may be able to receive faster service. For two FSOs, FSO1 and FSO2, let FSO1 precede FSO2 and form field f, belonging to both FSO1 and FSO2. Then, before we process FSO2, we can determine the value of f while processing FSO1. For instance, the medicine payment FSO currently occurs after the doctor's consultation and prior to submitting the medicine request at the pharmacy. When the patient returns to the cashier's desk with the prescription, the cashier enters the medicine names and quantities, since their field types are [exist, user-input] types. In this case, since the medicine name(s) and quantity information are determined during the doctor's consultation, we may be able to execute part of the medicine payment FSO during the patient's consultation FSO. Then, the field type of the medicine name and quantity fields is changed from [exist, user-input] into [exist, system-provided] since their values are already defined in the consultation FSO. By eliminating unnecessary data entry, we can decrease the $\alpha$ value of the FSO.

For the [system-provided] type fields ([E,S] and [N,S] quadrants), we look for the possibility of moving them to the preceding FSO. First, determinant field(s) may be moved to the preceding FSO, from which its determinant values are provided. For example, the total payment amount field ([new, system-provided]) of the medicine payment FSO can be moved to the consultation FSO, since its determinant values are available in the consultation FSO. Secondly, the fields whose values are generated by rules without a determinant may be moved to the preceding FSOs, for example, the sequence number field for preparation of the medicine whose input type was changed into the [system-provided] type. It can be moved to the FSO where the payment is executed, since the IS can also generate the sequence number. Then, the preparation of the medicine may start as soon as the patient pays for it without waiting until the patient submits the paid prescription slip to the receptionist.

However, while the above two guidelines provide an opportunity to move processing of the [exist] and [system-provided] type fields to an early part of the business process, if there is a field of [new, user-input] type in the FSO, it may not be movable; a patient's credit card number ([new, user-input]) that is being used to pay for medicine in the medicine payment FSO. If the type may be changed to [exist, system-provided] by storing the value for repeat customers, the medicine payment may be initiated at the completion of the doctor's consultation. Here, the credit card number processing is moved to the registration FSO, where the initial contact takes place. Then, the medicine payment FSO can be merged into the doctor's consultation FSO. Table 2 summarizes opportunities and directions.

In a typical BPR project, a variety of managerial factors and business practices guide and motivate the redesign effort. However, these have limits in supporting decisions on process change and in estimating the savings. To reduce the process cycle time, we have to examine both the intra- and inter-FSO opportunities. At the pharmacy center, the medicine retrieval activity, which processes all [exist] type fields, can start as soon as the doctor enters the prescription information for the patient, further reducing the total cycle time. As a result, when a patient arrives at the pharmacy after the doctor's consultation, the medicine will be ready for pick-up. Additionally, a BPR team can perform a simulation by changing fields and their types as well as FSOs; this can lead to further opportunities not found in either intra-FSO or inter-FSO redesign steps.

## 4. Validation

A prototype version of the EPRE method has been implemented as a PC-based software tool utilizing Visual Basic 4.0 in the Windows95 environment.

## 4.1. Empirical case: Advertising agency

The advertising industry helps client firms with market analysis and advertisement creation. One of the top five advertising agencies in Korea has an annual billing of about \$250 million in 1996. Its business area consists of advertising, marketing research, sales promotion, public relations, and space development; it has about 400 employees. We select the ‘media reservation process,’ as a candidate business process for our case. When a project order (P/O) from a client is received, the ad agency puts together a team of project manager (PM), account executives (AE), and ‘creatives’ (CR) to prepare an advertising plan for the P/O. At the same time, AE starts to make commitments of time in the media (TVs, Radios, Newspapers, Magazines, etc.). After interaction between the client and AE and between the media team and KOBACO, the government media control agency that coordinates media reservation requests and provides availability information to the media team using paper forms. After the draft advertising plan is approved by the client, the P/O is officially registered using the reserved media information.

Table 2
Summary of redesign opportunities and directions

<table><tr><td></td><td>Expected result</td><td>Field type information</td><td>Redesign direction</td></tr><tr><td rowspan="2">Intra-FSO opportunity</td><td>- Processing time reduction</td><td>[exist, user-input]</td><td>[exist, system-provided]</td></tr><tr><td>- Customer satisfaction</td><td>[new, user-input] having determinant</td><td>[new, system-provided]</td></tr><tr><td rowspan="3">Inter-FSO opportunity</td><td>- Cycle time reduction</td><td>[exist, user-input]</td><td>delete delay between [new] and [exist]</td></tr><tr><td>- Customer satisfaction</td><td>[new, user-input]</td><td>obtain field value from preceding FSO distribute with the related field</td></tr><tr><td></td><td>[exist, system-provided], [new, system-provided]</td><td></td></tr></table>

![](/api/attachments/NYFZE9QW/fulltext/images/6a218f94ee53bc1d31efb557d9f394fb13a697ee3466864a27ca62fd915d6607.jpg)  
Fig. 5. Complete EPC diagram for the candidate business process.

## 4.1.1. Form analysis and process generation

We first gathered forms handled in the media reservation process. Next, their FSOs and field types were identified. Then, we extracted the initial EPC diagram for the process. After the initial diagram had been drawn, some processes, events, and branchings were added through user interviews. Fig. 5 shows the complete EPC diagram for the candidate business process. Shaded symbols and dotted arrows represent the constructs added to the initial EPC diagram.

## 4.1.2. Process redesign

4.1.2.1. Intra-FSO redesign. After constructing the complete process model, we looked for intra-FSO redesign opportunities. Fig. 6 shows the prototype screen for the changed $\alpha$ and $\beta$ values using intra-FSO redesign opportunities. FSOs with high $\alpha$ or $\beta$ values (P1, P3, E4, E5, P6, E8, E9) need IT support as they seem too dependent on manual processing and need program enhancement, for example, P3 (input media information), which is performed after receiving media information in a printed form, can be enhanced (that is, low $\alpha$ value) using EDI so that the activity of entering is unnecessary. However, $\alpha$ value could not become zero for some FSOs even after changing the field types, since it was still necessary to enter the [exist] type values for some identifier fields such as the client number field entered in the contact report generation FSO.

4.1.2.2. Inter-FSO redesign. After changing some fields from the [user-input] type to the [system-provided] type, each FSO was examined on whether it could be performed earlier at the preceding ones. Table 3 shows the result of applying the inter-FSO redesign opportunities.

Fig. 7 shows the final process flow, where the process cycle time is reduced from 12 to 9 days. We have changed one process into an event and removed one process and four events; this significantly reduced unnecessary interactions and waits.

![](/api/attachments/NYFZE9QW/fulltext/images/1376569e425f8d3bc852152af45af798085a77db0f6f907775a369744a275121.jpg)  
Fig. 6. Changed $\alpha$ or $\beta$ values from Intra-FSO opportunities.

Table 3
Inter-FSO redesign opportunities

<table><tr><td rowspan="2">FSO name</td><td colspan="3">Opportunities</td><td rowspan="2">Result</td></tr><tr><td>[E,U]</td><td>[N,U]</td><td>[E,S], [N,S]</td></tr><tr><td>Request P/O (P1)</td><td>—</td><td>—</td><td>—</td><td>remain</td></tr><tr><td>Generate contact report (P2)</td><td>move emp-no, client-employee to P1</td><td>move contact-date, contact-content to P1</td><td>move all fields to P1</td><td>perform P2 at P1</td></tr><tr><td>Input media information (P3)</td><td>NA</td><td>NA</td><td>EDI support from KOBACO</td><td>changed to event</td></tr><tr><td>Media infor. extraction (E3)</td><td>move media-no to P1</td><td>NA</td><td>move all fields to P1</td><td>perform E3 at P1</td></tr><tr><td>Media reservation request (E4)</td><td>move emp-name, media-no to P1 and P4</td><td>NA</td><td>move all fields to P1 and P4</td><td>for first discussion: perform E4 at P1 for other discussions: perform E4 at P4</td></tr><tr><td>Reservation request to KOBACO (E5)</td><td>—</td><td>—</td><td>—</td><td>remain</td></tr><tr><td>Confirm (P5)</td><td>—</td><td>—</td><td>—</td><td>remain</td></tr><tr><td>Rejection reporting (E6)</td><td>—</td><td>—</td><td>—</td><td>remain</td></tr><tr><td>Acceptance reporting and updating (E7)</td><td>—</td><td>—</td><td>—</td><td>remain</td></tr><tr><td>Review ad plan (P6)</td><td>—</td><td>—</td><td>—</td><td>remain</td></tr><tr><td>P/O registration request (E8)</td><td>—</td><td>—</td><td>—</td><td>remain</td></tr><tr><td>P/O registration (E9)</td><td>move brand-no to E8</td><td>NA</td><td>move all fields to E8</td><td>perform E9 at E8</td></tr></table>

![](/api/attachments/NYFZE9QW/fulltext/images/c85d089bd7514b83b2afcd72f0f671f3c018488d92d83f789070e87c528aa4b4.jpg)  
Fig. 7. New EPC diagram after examining inter-FSO redesign opportunities.

## 4.2. Discussion

The application of EPRE to the advertising agency mainly focused on illustrating its feasibility. We are currently also applying it to BPR projects in manufacturing, hospital, and cable-TV industries. While the validation of the method is far from over, the tentative result of its application convinced us that the EPRE method can contribute to the understanding of the ‘current’ processes more efficiently and provide process redesign.

The form-based approach adopted in EPRE does not replace existing BPR methodologies. The proposed method can complement them, since redesign opportunities identified through EPRE can be used. However, not all BPR projects seem to benefit equally from the application of EPRE. The form-based approach works well with business processes consisting mostly of information handling activities. Customer order fulfillment and invoice management processes are such processes. In many organizations, these constitute the core business processes with heavy transaction volume and non-trivial redesign impact. On the other hand, for business processes that contain mostly physical activities or do not use many business forms, the EPRE method may be of limited applicability.

## 5. Summary and conclusion

We have discussed the EPRE method and how it can be used to generate the current enterprise process model and provide process redesign guidelines by analyzing business forms. EPRE consists of three stages: (1) Form analysis; (2) Process model generation; and (3) Process redesign. In the first stage, we identify FSOs for explaining and generating the current process model. Characteristics of each process are reflected in FSOs. In the second stage, we generate the initial process model, using an EPC modeling formalism which supports BPR from the customer's perspective. To the basic model, physical activities and branchings are added. In the last stage, the method provides process redesign guidelines in terms of intra- and inter-FSO redesign opportunities based on the field type information. Intra-FSO redesign opportunities suggest field handling level improvement while inter-FSO redesign opportunities suggest FSO level improvement.

Currently, there are several limitations to be overcome in the future research. First, to cover physical activities and branchings, our method needs some level of user interaction to generate the complete process model. Second, process redesign support is restricted to information handling activities. Thus, physical activity or facility related redesign needs to be examined by users. Third, the suggested intra/inter-FSO redesign guidelines do not consider a radical redesign alternative such as removing the entire candidate business process. Rather, it suggests multiple, significant, continuous improvements. Fourth, due to the limitation in identifying field dependencies and relationships, the suggested intra/inter-FSO redesign guidelines lack field level guidelines, such as determining to which FSO the [new] type fields should be moved.

## Acknowledgements

The authors wish to thank the chairman of the editorial board, Professor Edgar H. Sibley, for his kind and thoughtful editorial help for this paper.

## References

[1] D. Barbara, S. Mehrotra, M. Rusinkiewicz, INCAs: Managing Dynamic Workflows in Distributed Environments, Journal of Database Management, (1996) 5–15.

[2] C. Batini, B. Demo, A. Di Leva, A methodology for conceptual design of office databases, Information Systems 9(3/4), 1984, pp. 251–263.

[3] A.T. Berztiss, SYSLAB, Reverse engineering, reengineering, and concurrent engineering of software, International Journal of Software Engineering and Knowledge Engineering, 5(2) (1995) 299–324.

[4] P. Calvert, An advanced BPR methodology with integrated, computer-based tools, Proceedings of the IFIP TC8 Open Conference on Business Process Re-engineering: Information Systems Opportunities and Challenges, 1994, pp. 161–170.

[5] J.R. Caron, S.L. Jarvenpaa and D.B. Stoddard, Business reengineering at CIGNA corporation: Experiences and lessons learned from the first five years, MIS Quarterly 18(3), 1994, pp. 233–250.

[6] A. Celentano, M.G. Fugini, S. Pozzi, Knowledge-based document retrieval in office environments: The Kabiria system, ACM Transactions on Information Systems 13(3), 1995, pp. 237–268.

[7] R.H.L. Chiang, T.M. Barron and V.C. Storey, Reverse engineering of relational databases: Extraction of an EER model from a relational database, Data and Knowledge Engineering 12(2), 1994, pp. 107–142.

[8] E.J. Chikofsky, J.H. Cross II, Reverse engineering and design recovery: A taxonomy, IEEE Software 7(1), 1990, pp. 13–17.

[9] J. Choobineh, M. Mannino, V. Tseng, A form-based approach for database analysis and design, Communications of the ACM 35(2), 1992, pp. 108–120.

[10] T.H. Davenport, Process Innovation: Reengineering Work Through Information Technology, Boston, Harvard Business School Press, 1993.

[11] T.H. Davenport, M.C. Beers, Managing information about processes, Journal of Management Information Systems 12(1), 1995, pp. 57–80.

[12] T.H. Davenport, J.E. Short, The new industrial engineering: Information technology and business process redesign, Sloan Management Review 31, 1990, pp. 11–27.

[13] T. DeMarco, Structured Analysis and System Specification, New York, Yourdon Press, 1978.

[14] C. Gane, T. Sarson, Structured Systems Analysis: Tools and Techniques, New York, IST, Inc., 1977.

[15] D. Georgakopoulos, M. Hornick, A. Sheth, An overview of workflow management: From process modeling to workflow automation infrastructure, Distributed and Parallel Databases 3, 1995, pp. 119–153.

[16] H. Gerrits, Business modeling based on logistics to support business process re-engineering, Proceedings of the IFIP TC8 Open Conference on Business Process Re-engineering: Information Systems Opportunities and Challenges, 1994, pp. 279–288.

[17] V. Grover, S.R. Jeong, W.J. Kettinger, J.T.C. Teng, The implementation of business process reengineering, Journal of Management Information Systems 12(1), 1995, pp. 109–144.

[18] G. Hall, J. Rosenthal, J. Wade, How to make re-engineering really work, Harvard Business Reviews 71(6), 1993, pp. 119–131.

[19] M. Hammer, Reengineering work: Don't automate, obliterate, Harvard Business Review 68(4), 1990, pp. 104–112.

[20] T. Holden, P. Wilhelmij, Improved decision making through better integration of human resource and business process factors in a hospital situation, Journal of Management Information Systems 12(3), 1996, pp. 21–41.

[21] K. Kim, Y. Kim, Form-based approach for enterprise process modeling, Proceedings of the 1st Asia Pacific Decision Science Institute Conference, Hong Kong, 1996, pp. 1087–1096.

[22] H. Kim, Y. Kim, Dynamic process modeling for BPR: A computerized simulation approach, Information and Management 32(2), 1997, pp. 1–13.

[23] Y. Kim, Process modeling for BPR – Event-process chain approach, Proceedings of the 16th International Conference on Information Systems, Amsterdam, 1995, pp. 109–121.

[24] J.A. Larson, The forms pattern language, Proceedings of International Conference on Data Engineering, Los Angeles, 1984, pp. 183–192.

[25] R.M. Lee, Dynamic modelling of documentary procedures: A case for EDI, Proceedings of the 3rd International Working Conference on Dynamic Modelling of Information Systems, Noordwijkerhout, 1992, pp. 95–123.

[26] M.G. Martinsons, Radical process innovation using information technology: The theory, the practice and the future of reengineering, International Journal of Information Management 15(4), 1995, pp. 253–269.

[27] J.Q. Ning, A. Engberts and W. Kozaczynski, Automated support for legacy code understanding, Communications of the ACM 37(5), 1994, pp. 50–57.

[28] W.J. Premerlani, M.R. Blaha, An approach for reverse engineering of relational databases, Communications of the ACM 37(5), 1994, pp. 42–49.

[29] J. Rockart, Chief executives define their own data needs, Harvard Business Review 57(2), 1979, pp. 81–91.

[30] A.L. Scherr, A new approach to business processes, IBM Systems Journal 32(1), 1993, pp. 80–98.

[31] A. Sen, L. Kerschberg, Enterprise modeling for database specification and design, Data and Knowledge Engineering 2, 1987, pp. 31–58.

[32] P. Shoval, N. Shreiber, Database reverse engineering: From the relational to the binary relationship model, Data and Knowledge Engineering 10, 1993, pp. 293–315.

[33] N.C. Shu, V.Y. Lum, F.C. Tung, C.L. Chang, Specification of forms processing and business procedures for office automation, IEEE Transactions on Software Engineering 8(5), 1982, pp. 499–512.

[34] D.B. Stoddard, S.L. Jarvenpaa, Business process redesign: Tactics for managing radical change, Journal of Management Information Systems 12(1), 1995, pp. 81–107.

[35] D. Tsichritzis, Form management, Communications of the ACM 25(7), 1982, pp. 453–478.

![](/api/attachments/NYFZE9QW/fulltext/images/ad8badfc7dee04ce75f27c5a4d026ae170adf9fbe6d6b37c85252af1998b181c.jpg)

Kyong-Ho Kim is a Ph.D. candidate at Graduate School of Management of Korea Advanced Institute of Science and Technology in Seoul. He received his B.S. degree from Seoul National University and M.S. degree in Management Science from Korea Advanced Institute of Science and Technology in Seoul. He has participated in several industrial projects for IT infrastructure

development as a senior consultant in Andersen Consulting and is now working for i2 Technologies, Inc. as a Consulting Group Leader, Korea. His active research areas are: BPR; Reverse Engineering; Data and Process Modeling; and Supply Chain Management.

![](/api/attachments/NYFZE9QW/fulltext/images/a4467931ea5c641a1f53bf3433ed7754e30d1cfb964d89f5a4ee7b7de6b4ee6b.jpg)

Young-Gul Kim is an associate professor at Graduate School of Management of Korea Advanced Institute of Science and Technology in Seoul. He received his B.S. and M.S. degrees in Industrial Engineering from Seoul National University, Korea and Ph.D. degree in MIS from University of Minnesota. His active research areas are: IS Architecture Development; Data and Process Modeling; and IT Management. He has published in

Communications of the ACM, Information and Management, Database, Journal of MIS, and Information Systems Management. Also, he presented several papers at ICIS, HICSS, and DSI conferences.
