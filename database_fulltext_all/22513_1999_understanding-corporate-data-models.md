---
otero_id: 22513
otero_key: "4GNFNRTM"
title: "Understanding corporate data models"
authors: "Graeme Shanks; Peta Darke"
year: "1999"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00078-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Understanding corporate data models

Graeme Shanks $^{*}$ , Peta Darke

School of Information Management and Systems, Monash University, Melbourne, Australia

Received 25 November 1997; accepted 23 July 1998

## Abstract

Corporate data models are widely used to support data management within organisations. However, both IS professionals and business users find them difficult to understand. This paper describes a methodology for designing and representing corporate data models that uses explanation and visualisation mechanisms to improve understanding, and reports a case study of the use of the methodology in the development of a data warehouse. The methodology was shown to be effective in that a high quality corporate data model was designed and then understood and utilised by all the participants. The model was used as an active, hypertext interface to the first prototype of the data warehouse. The case study findings indicated that: scenarios are useful for eliciting information requirements and explaining abstract concepts in the model to business users; graphical icons and subject area partitions are effective means of visualising the model and lead to improved understanding of the model by business users; and design rationale is an effective means of explaining the evolution of concepts in the model for specialist data modellers. © 1999 Elsevier Science B.V. All rights reserved

Keywords: Data management; Data administration; Data warehousing; Corporate data models; Information systems methodologies

## 1. Introduction

Data are often duplicated throughout organisations, resulting in potentially inconsistent data that may be stored in different formats and are difficult to consolidate. The corporate data model has been proposed as a tool to support the management of data at the corporate level. It is an abstract representation of the information requirements of all or part of an organisation and is independent of functional boundaries within an organisation and of implementation technology $[1]$ .

Despite strong arguments supporting data management $[2]$ , the use of corporate data models has been problematic in practice $[3, 4, 5, 6]$ . Empirical studies report that corporate data models are too complex $[7]$ , too conceptual, bulky and inflexible $[8]$ , subject to complex political and organisational problems $[9, 10]$ , and considered irrelevant for strategic planning by senior management $[11]$ . However, corporate data models are required when designing cross-functional IS that need to integrate information from a number of sources. In particular, the emergence of data warehousing and of IS that support re-engineered business processes have again motivated interest in corporate data models $[12]$ .

A major problem with corporate data models is that they are difficult to understand. Their abstract, generic concepts are unfamiliar to both business users and IS professionals, and remote from their local organisational contexts $[13]$ . This paper discusses a methodology for designing and representing corporate data models that makes explicit use of mechanisms for explaining and visualising them in order to facilitate stakeholder understanding. The methodology incorporates argumentation-based design rationale and scenarios as explanation mechanisms. Visualisation mechanisms include identification of subject area clusters to structure the models and the use of graphical icons to represent the subject areas. The methodology, ViewCon (Viewpoint Consolidator), supports the evolutionary development of a corporate data model by providing for the design and consolidation of separate business user views of data requirements. A case study of the use of ViewCon in the development of a data warehouse has demonstrated the value of the methodology in practice.

## 2. Understanding corporate data models

A corporate data model (or data architecture) is a high-level model of information requirements within an organisation. The model is usually represented using a conceptual data modelling notation, such as the entity relationship model $[14]$ , and should not reflect particular personnel, organisational structures, or technology. Corporate data models are frequently justified on the basis that they will help improve the quality of poor or inconsistent data, assist with the integration of information, and help gain control of data redundancy $[15]$ . They span functional areas within an organisation, providing a common view of data.

The purposes for corporate data models identified in the literature include support for the implementation of a set of integrated systems, a data architecture to provide a stable base for planning and prioritising the development of new application systems, a basis for education and communication about information in an organisation, and a framework for developing an inventory of data in legacy systems $[4, 16]$ . The sourcing of data for a data warehouse depends on the availability of a data inventory $[17]$ .

Empirical studies indicate that many organisations have encountered significant problems in building and using a corporate data model $[9, 13]$ . A number of these studies have identified the difficulties experienced by both business users and IS professionals in understanding corporate data models as a barrier to their effective use. A corporate data model is a conceptual data model, that is, an abstract representation of information requirements. However, corporate data models often have generic and abstract concepts that are not easily related to the actual terminology used within particular business areas. This limits the usefulness of the model, as communication about the model is difficult and a shared understanding of the model is not developed. An important dimension identified in frameworks for evaluating quality in conceptual data models is stakeholder understanding $[18, 19, 20]$ . Explanation and visualisation are two means for improving stakeholder understanding of conceptual data models.

Important knowledge about design decisions, assumptions, and argumentation, and about the details of how particular stakeholders intend to use the data represented in the conceptual data model is gained during the data modelling process. Although this may remain in the memories of those who participated in the modelling process, it is usually not recorded. This knowledge can be captured and used to assist with explanation of the model. Argumentation-based design rationale and scenario-based analysis are mechanisms for capturing and retaining knowledge.

Empirical studies indicate that the entity relationship modelling notation is difficult to teach $[21]$ and that practitioners find some abstractions difficult to understand $[22]$ . Visualisation of conceptual data models using appropriate representations can facilitate stakeholder understanding. The structuring of entity relationship models into subject areas together with the use of graphical icons as subject area representations has been proposed as a means of visualising the models in order to facilitate both data modellers' and business users' understanding of the model concepts $[23, 24]$ .

Previous methodologies have recognised the need to capture and integrate multiple viewpoints from a number of stakeholder groups $[25]$ . However, these focus on the consolidation of representations rather than on capturing the underlying meanings of the concepts included in the model [26]. The mechanisms of argumentation-based design rationale, scenario-based analysis, and structured representation of the corporate data model using graphical icons can be used to enhance the capture and integration of stakeholder viewpoints.

## 2.1. Capturing design discussions using argumentation-based design rationale

A number of partial and alternative data models are generated, discussed, and evaluated during conceptual data modelling which can, therefore, be considered a creative design process. The models and associated discussions and design decisions constitute the design reasoning or argumentation. Design rationales are typically represented as explicitly structured discussions about the design artefact and are “... representations of the reasoning behind the design of an artefact” [27]. They support the building of cumulative design knowledge and aid reasoning, communication, and critical reflection about the process and the design, and they are an important resource for reuse and redesign processes [28, 29].

Structure-oriented and process-oriented techniques constitute the two main categories of design rationale $[30]$ . Structure-oriented techniques are intended to be used after the design process. They focus on the logical structure of the space of all design alternatives. Process-oriented design rationale techniques focus on maintaining an historical record of design decisions and are intended to be used during the design process. The Issue-Based Information System (IBIS) and its descendants are examples of process-oriented design rationale techniques $[31]$ . There are two types of process-oriented design rationale approaches: those that represent the design discussion only, and those in which the design rationale is integrated with the artefact itself as it evolves. The latter type of approaches have been used to capture and model IS requirements $[32, 33]$ . Design rationale is used to explain the evolution of the artefact. Empirical studies suggest that integration of the design discussion with the artefact is preferable as the design is focused to the task at hand and large and unusable documentation is avoided. Simple design rationale notations are preferred, as the more expressive notations with sophisticated computer support are not as easy to use.

## 2.2. Capturing and explaining information requirements using scenario-based analysis

A scenario is “… a concrete description of an activity that the user engages in when performing a specific task” [34]. Scenarios are informal representations of specific instances of work-driven tasks. These may be in various forms (e.g. text descriptions, cartoons, videos) at any level of detail. They are useful for relating abstract, generic concepts to the everyday activities with which the user is familiar.

Scenarios may take either the envisioner role or the evaluator role [35]. In their envisioner role, scenarios can be used during requirements acquisition to drive the design process. They can be informal, vague, open and inconsistent in order to support development of an understanding of the business area and the relevant users' requirements. In their evaluator role, scenarios can be used to assist the evaluation of requirements models and to help explain their meaning to all potential stakeholders. These scenarios need to be clearly and carefully grounded in the detail of the requirements models. They are an important component of the documentation of the models and of the training programs that explain them.

Both, requirements capture and the explanation of conceptual models of requirements, have been shown to benefit from the use of scenarios. Potts et al. used scenarios to help capture requirements for a meeting scheduling system. In their study, over half the questions raised in requirements meetings related to scenarios. They found that some questions concerning requirements could not be easily answered without the use of scenario analysis. Scenarios facilitated the elaboration of requirements, and analysis of scenarios led to about half of the improvements to the set of requirements.

## 2.3. Use of visualisation to assist understanding of conceptual data models

Large numbers, even hundreds, of entity- and relationship-types may be found in corporate data models designed using the entity relationship notation. Groups of entity- and relationship-types may be clustered into high-level subject areas for ease of representation in situations where these large models are developed [36]. The subject areas are, in effect, linked by shared entity-types, and may overlap. Subject areas allow for structuring of corporate data models to improve their accessibility. A number of high-level subject areas may be used to represent a corporate data model, each of which may be expanded into a more detailed model.

McGuniness suggested that graphical icons should be used in modelling notations within CASE tools for ease of use. Moody used graphical icons to represent subject areas in order to enhance understanding of corporate data models and to improve communication about them, and provide some anecdotal evidence of their usefulness. However, there has been no systematic, empirical research into the effectiveness of the use of graphical icons to represent subject areas in practice.

## 3. Research approach

There were two phases in the research project described in this study. In the first phase, the ViewCon methodology was developed by synthesising concepts from viewpoint integration approaches, argumentation-based design rationale, scenario-based analysis, and the use of subject areas and graphical icons to structure the representation of data models. ViewCon extends the existing approaches to data model design by capturing design decisions during the design process and documenting them using a design rationale notation, and by using scenarios to capture requirements and explain the data model. It was developed using Avison and Fitzgerald's [37] framework for comparing IS methodologies.

The use of the ViewCon methodology in practice was examined in the second phase using a single case study. A single case design should be adopted when the case is considered critical, extreme or unique, or revelatory $[38]$ . The case described in this study is both unique and revelatory, as the ViewCon methodology is new and was being applied in an organisational setting for the first time. A data warehouse was required by a large department in an Australian university, and a corporate data model was considered to be an essential input to the development process. The case participants included five key senior staff members from within the department and two experienced data modelling practitioners who were motivated by the opportunity to learn about and use the ViewCon methodology to design the corporate data model. Each of the five senior staff members had their own perspective of their particular information requirements.

The team involved in the task of building the corporate data model using the ViewCon methodology formed the unit of analysis in the case study. An initial briefing and training session in the use of the methodology was followed by several sessions in which the case participants carried out the activities specified in the methodology. These sessions included interviews with the senior staff, the design of data models for each of their perspectives, the integration of the various data models into a corporate data model, and a quality review with all participants present. The case study procedure concluded with a debriefing session in which the two data modelling practitioners provided further information about their use of the ViewCon methodology. All sessions were conducted in a meeting room equipped with videotaping facilities. Case study data collection was by observation (video-tapes), interviews, and examination of existing documents. Qualitative techniques were used to analyse the case study data.

## 4. The ViewCon methodology

ViewCon focuses on the acquisition and modelling of data requirements for a corporate data model. It consists of two main activities with two tasks within each activity. The first activity, requirements description, involves acquiring user data requirements and designing a data model for each user group. During the second activity, model consolidation, these models are consolidated to form the corporate data model. View-Con is an evolutionary methodology, with ongoing refinement and extension of both the user data requirements and the corporate data model.

ViewCon is not intended to be a detailed prescription of how to design a corporate data model. Details of entity relationship modelling notations and prescriptions for integrating data models are well understood and described elsewhere. The contribution of ViewCon is in the recognition that designing a corporate data model is a creative and opportunistic process. ViewCon is a descriptive methodology which provides mechanisms for capturing and structuring information used in the design process, and for using this information to help explain the meaning of the concepts in the model. The structure of the ViewCon methodology is shown in Fig. 1.

![](/api/attachments/4GNFNRTM/fulltext/images/b148010f6fbdbf92e6ee55ff60bcdbc076c60a2140e1e6367b0983b20259b865.jpg)  
Fig. 1. The ViewCon methodology.

## 4.1. Requirements acquisition

Specialist data modellers first elicit and accumulate information about the data requirements of the business users from interviews with stakeholders, existing information systems, knowledge of the application domain, and other documentation. During requirements acquisition an understanding of the domain of the IS is developed. In order to facilitate communication, requirements should be represented in the language and terminology of the business users. Requirements are represented using informal representations, including text narrative, rich pictures, and envisioner scenarios. Informal representations are readily understood by business users and allow for requirements freedoms, as described by Feather: incompleteness, complexities, ambiguities, non-uniformity of abstraction, and heterogeneity of expression [39].

A number of separate requirements acquisition sessions may be held for each business user. Discussions about each data requirement are analysed and documented using the design rationale notation of Potts et al. after each session, and structured into sets of questions, answers, and reasons. Each design rationale fragment is related to a particular requirement. Building the design rationale after each requirements acquisition session avoids the problem of distracting stakeholders from the task at hand during the session.

The requirements acquisition activity produces a requirements document containing a set of informal requirements (text narrative, rich pictures, and envisioner scenarios) together with related design rationale fragments for each business user. The quality of the requirements document is largely determined by the skills of the data modellers in eliciting and representing the data requirements of the business users. Using informal representations encourages active user participation in the requirements acquisition process.

## 4.2. Requirements modelling

After the data requirements of business users are elicited, they are modelled by specialist data modellers in a semi-formal or formal notation in order to facilitate analysis and comparison. Although semi-formal notations have well-defined constructs which support model analysis, they allow some requirements freedoms, for example ambiguity, incompleteness and inconsistency $[26]$ . They are more widely used in practice than formal representations (e.g. Z) $[26]$ . Entity relationship notation is the semi-formal language used in ViewCon.

Specialist data modellers analyse the informal requirements, rich pictures, envisioner scenarios and design rationale fragments during the requirements modelling task. An entity relationship model is designed for each separate business user viewpoint. When designing data models, specialist data modellers reuse generic data model patterns and application area data models learned from previous experience, in addition to using information from the requirements document $[40]$ . The design process involves iteratively exploring alternative representations and selecting the most appropriate. After each requirements modelling session, discussions about components of the entity relationship model are documented using questions, answers and reasons. Each design rationale fragment relates to a particular entity relationship model component. The requirements modelling activity produces an entity relationship model for each business user together with related design rationale fragments.

## 4.3. Model integration

The specialist data modellers then integrate the various business user requirements models into a corporate data model. In the database literature, entity relationship models are typically integrated using a three-step process: conflict analysis, conflict resolution, and view merging $[25]$ . A weakness of this approach is that it focuses on the analysis and merging of the representations rather than on understanding the underlying perceptions of users and the meaning of the concepts in the models. It also ignores the opportunity to re-conceptualise important concepts in the data model using concepts from generic data model patterns and abstraction mechanisms.

In ViewCon, model integration is seen as a creative design process involving the exploration of alternative representations for concepts in the various business user requirements models. This process is supported by use of the design rationale fragments documented in the requirements modelling task. Design discussions between the specialist data modellers during model integration contain useful information about the process of model development and explanations of concepts in the resulting data model. After each model integration session, discussions about the design of the corporate data model are documented using questions, answers, and reasons. Each design rationale fragment relates to a particular component of the corporate data model. The model integration activity produces a corporate data model represented using the entity relationship notation together with related design rationale.

## 4.4. Model validation

Model validation consists of two processes: explanation of the model to business users and quality checking. Two mechanisms are used to explain the corporate data model to users. The first involves structuring the corporate data model into subject areas and representing each subject area using a graphical icon. This enables business users to understand the concepts in the model. Each subject area is related to an entity relationship model that is a partition of the complete corporate data model. The second involves the creation of evaluator scenarios for each user. These are based on the envisioner scenarios. Evaluator scenarios are more detailed and specific than envisioner scenarios and consist of a sequence of steps that refer directly to the subject areas in the corporate data model. In this way, abstract concepts in the corporate data model are related to familiar work-driven tasks of the business user. The corporate data model is explained to business users in a workshop.

Quality checking involves reviewing the corporate data model using a set of conceptual data modelling quality factors including correctness, completeness, understandability, flexibility and simplicity. Quality is defined as fitness for purpose and it is important to have the active participation of both business users and data modelling specialists in quality checking. Feedback from the validation workshop is used to refine and improve the model.

## 5. Using the ViewCon methodology in practice: A case study

A case study was conducted between April 1996 and October 1997 in order to examine the use of ViewCon in practice. In the case study, ViewCon was used to develop a corporate data model for a large department in an Australian university. The corporate data model was subsequently used in the development of a data warehouse. The four ViewCon tasks are described and analysed and use of the corporate data model in providing a hypertext, model-based interface to the data warehouse is discussed.

## 5.1. Requirements acquisition

The two specialist data modellers used interviews to elicit data requirements for each of the five business users. The interviews were conducted separately; requirements were documented using informal narrative description and envisioner scenarios. Each interview lasted approximately one hour and resulted in an average of 11 informal requirements and seven envisioner scenarios. There was little variation in the number of requirements between the business users. Analysis of the design discussions in the interviews by one of the authors identified an average of 30 design rationale fragments for each business user. Approximately four hours were required to identify and document the design rationale fragments for each interview.

All the participants readily understood the informal requirements and envisioner scenarios. They helped the business users structure their thoughts and supported communication between the data modellers and business users. Business users found envisioner scenarios particularly useful when checking requirements for completeness after the interviews, and resulted in the identification of additional requirements.

The design rationale fragments identified and documented were of little value as they were mostly concerned with requests for additional requirements or scenarios, and did not help to explain and clarify the requirements statements. They were not used in later tasks.

## 5.2. Requirements modelling

The informal requirements and envisioner scenarios were used by the two specialist data modellers to design an entity relationship model for each of the business users. Requirements modelling took place 6 weeks after requirements acquisition was completed, and consisted of two sessions. The first was of two hours duration and the second of three hours. Each entity relationship model took an average of one hour to design and contained on an average 16 entity-types and 15 relationship-types. The data modellers were readily able to understand the informal requirements and envisioner scenarios, which provided them with sufficient information to design the data models.

Analysis of the design discussions in the modelling sessions by one of the authors identified the rationale fragments for each data model. Approximately four hours were required to identify and document the design rationale fragments for each hour of data modelling. The design rationale fragments identified and documented were mainly concerned with the justification for using particular modelling abstractions and for choosing from alternative representations for the same underlying concept. The design process followed was opportunistic $[40]$ , rather than systematic. There was no evidence that the use of design rationale constrained the design discussions, as some previous empirical studies have shown. A simple example of a design rationale fragment explains how a new, generic entity-type, activity, is created. The fragment is structured as questions (Q), answers (A), and reasons (R).

Q: How are administration tasks represented?
A: Use a ADMINISTRATION ACTIVITY entity-type.

This should be a sub-type of a more generic type called ACTIVITY.

Other sub-types will be TEACHING ACTIVITY, RESEARCH ACTIVITY and COMMUNITY SERVICE.

R: This allows all types of activities to share a common relationship with the other entity type STAFF.

## 5.3. Model integration

In order to integrate the data models for each of the five business users, copies of each of the data models and associated informal requirements, envisioner scenarios, and design rationale were provided to the two specialist data modellers. Model integration took place 5 weeks after the requirements modelling task and consisted of one 3-hour session. The five data models and their associated documentation were reviewed in the first 30 minutes of the model integration session. The design rationale fragments were particularly useful in reviewing and understanding the design of each data model, and the contexts for data modelling design decisions.

Model integration was achieved by selecting the model that contained many of the core concepts required in the corporate data model, and the other data models were sequentially integrated into the selected model. This was a creative and opportunistic design activity that involved much discussion about alternative abstractions. Several new, generic concepts were introduced: the most important were Product and Product Offering. These concepts were used to represent any formal course or subject, short course, seminar or other kind of product that the department had defined and scheduled.

Analysis of the design discussions in the model integration session by one of the authors identified the rationale fragments for the corporate data model. Approximately 4 hours were required to identify and document the design rationale fragments for each hour of model integration. A simple example explaining how the Product Offering concept is related to staff and students is shown below:

Q: Are PRODUCT OFFERINGs related to staff and students?

A: Yes, ACTIVITY (TEACHING ACTIVITY) relates to PRODUCT OFFERING in several ways; for example, examiner, lecturer, tutor, course coordinator.

Students relate to PRODUCT OFFERING via the ENROLMENT entity-type.

## 5.4. Model validation

Two sessions were required for model validation. In the first, which was of 2-hours duration, the two data modellers structured the model into subject areas represented by graphical icons, prepared several evaluator scenarios for explaining the model to business users, and reviewed the quality of the model. In the second session, which was of 2-hours duration, the model was explained to the business users, and the quality of the model was reviewed again. Model validation took place 4 weeks after model integration.

The model was structured using two heuristics: key concepts in the model must be represented as subject areas, and there should be about seven subject areas so that it is neither too complex nor too simple. Graphical icons were then selected to represent the subject areas. Evaluator scenarios were then prepared for each of the envisioner scenarios for each business user. The quality review of the corporate data model involved an informal discussion about each of the five quality factors. The model was deemed to be of high quality and no changes were made in it. The high-level consolidated data model is shown in Fig. 2 together with an example evaluator scenario, which refers to subject areas in the model.

When explaining the corporate data model, graphical icons were readily understood by all the business users, and helped communication between the data modellers and the business users. Evaluator scenarios enabled the business users to relate subject areas in the corporate data model to familiar, everyday activities. The data modellers chose not to use the design rationale during the presentation as they considered it inappropriate for communication with business users. However, they believed it would be very useful for other data modellers trying to understand and extend the data model at a later time. The model was informally reviewed and found to be complete and readily understood.

## 5.5. Developing the prototype data warehouse

The corporate data model provided the overall architecture for the subsequent design of the prototype data warehouse. Three high priority business area partitions were initially identified as candidates for data warehouse development. These were student enrolments, staff activities and finance. Each consisted of several subject areas. For example, student enrolments consisted of the student, enrolment and product offering subject areas. Student enrolments was selected for implementation in the first prototype data warehouse.

The development approach adopted for the prototype was that of Kimball $[17]$ in which a dimensional model is designed for each business area partition. A dimensional model of the student enrolments business area was readily developed from the corporate data model, and included an enrolment fact table and three-dimensional tables: student, product offering and time. The dimensional model, together with hypertext links to associated evaluator scenarios, provided an active interface to the data warehouse for business users. A set of pre-defined reports were also developed to provide standard information about enrolments to business users and an active link to an on-line analytical processing (OLAP) tool was provided to support browsing of the data warehouse. Explanations of the contents of the fact table and dimensions' tables were provided by hypertext links to evaluator scenarios.

An alternative interface to the data warehouse was developed for data modellers. This interface displayed an entity relationship model together with hypertext links to associated design rationale fragments. Details about the attributes in each entity and how they were sourced from central university systems and other data sources were provided by additional hypertext links.

The prototype was developed using Visual Basic with an Access database to load sample data as proof of concept of the use of ViewCon for the development of a data warehouse. It demonstrated the feasibility of using the visualisation and explanation mechanisms within ViewCon as an active, hypertext interface to a data warehouse. An example screen for business users is shown in Fig. 3 below.

![](/api/attachments/4GNFNRTM/fulltext/images/eefe23e99cc860204afa6fbfbbdfd19da92867a0960acf616d66b4ac7e96a1fb.jpg)

![](/api/attachments/4GNFNRTM/fulltext/images/4d5defe09887508bac07c81476b5d3ef968383725f409839b643cb3c8722b86c.jpg)  
Fig. 2. Graphical corporate data model and evaluator scenario.

## 6. Case study findings and implications for practice

ViewCon was shown to be effective in supporting the design of a high quality corporate data model which was readily understood by and communicated to all participants. The case study clarified where and how specific explanation and visualisation mechanisms could be used in the corporate data modelling process. Business user participation in the requirements acquisition and model validation tasks was facilitated by the incorporation of explanation and visualisation mechanisms into the corporate data modelling process. Data modellers found these mechanisms useful in understanding previously designed data models and in explaining the corporate data model to business users. The mechanisms were also useful in developing a model-based interface to a prototype data warehouse. Discussion of more specific case study findings follows.

![](/api/attachments/4GNFNRTM/fulltext/images/38150603dcfabde919b3e9a29522ad6712b4e6dca965c01af87209c22216fa1c.jpg)  
Fig. 3. User interface to data warehouse for business user.

## 6.1. Scenarios

Both envisioner and evaluator scenarios should be used during the corporate data modelling process for elicitation of requirements and to explain abstract concepts in the model to business users. Envisioner scenarios were particularly useful in helping participants express their information requirements and for reviewing them and detecting omissions during requirements acquisition. They also provided data modellers with knowledge about how business users would use the information in the data models. This was very useful during the model integration activity. Evaluator scenarios were readily understood by the business users and facilitated communication between them and the data modellers during the model validation activity.

## 6.2. Subject areas and graphical icons

The corporate data model should be structured using subject areas as a means of reducing the complexity of the model and providing support for business users in gaining an overall understanding of the model. Subject areas also supported partitioning of the model for evolutionary development of the data warehouse. Graphical icons were an effective means of visualising the model and presented abstract concepts as real-world, concrete objects to which the business users could readily relate. They were effective in facilitating communication about and understanding of the model by the business users.

## 6.3. Design rationale

Design rationale should be used to document the evolution of concepts in the corporate data model. Although Potts et al. argue that design rationale is useful in discovering and explaining requirements for IS during requirements acquisition, we found it to be of little benefit, as it did not clarify or explain requirements statements, but simply recorded requests for further data requirements. Design rationale was, however, found to be most useful in documenting design discussions during data modelling, both for the design of the business user data models and when consolidating these models into the corporate data model. The data modellers used the design rationale to help understand concepts in the business user data models and to determine how they could be synthesised during the model integration task.

The simple, indented text notation adopted for the design rationale was easily understood and used. This confirms the findings of previous empirical studies. Integration of the design rationale with the artefact being designed (the data model) provided a means of partitioning the design rationale according to the components in the model and simplified access to the design rationale fragments. Further studies are required to determine the effectiveness of the design rationale when other data modellers maintain and evolve the corporate data model.

## 6.4. Active hypertext interface

The explanation and visualisation mechanisms were used to provide a model-based, hypertext interface in the development of a prototype data warehouse. An important feature of the interface was the separate interface profiles provided for business users and data modellers. Business users were provided with graphical icons, scenarios, and other linked textual information in their interface. Data modellers were provided with an entity relationship model, associated design rationale fragments, and other linked textual information in their interface. The effectiveness of the interface needs to be further examined.

## 6.5. Limitations of the study

There are two limitations of this case study. First, a university department is not typical of the organisational environment in which corporate data modelling usually occurs, because the business users may have knowledge of data modelling and because commercial organisations are generally larger and more complex than the university department. Three of the business users in the study, however, were administrative staff with no experience in conceptual data modelling. Second, it is constrained in that all the sessions were conducted in the same meeting room so that the sessions could be videotaped for detailed analysis. The behaviour of the participants may have been affected, because the sessions were not held in their usual work environment. Additional case studies of the use of ViewCon in building corporate data models in different organisational settings are required to confirm and strengthen the results of this study.

## 7. Conclusions

This paper describes the ViewCon methodology for designing and representing corporate data models. Previous empirical studies have shown that corporate data models are difficult to build and use in practice, and that both information systems professionals and business users find them difficult to understand. ViewCon extends previous approaches to data model design in that it uses explanation and visualisation mechanisms to help overcome these problems. A case study of the use of ViewCon in practice has demonstrated that the use of scenarios, subject areas, graphical icons, and design rationale is effective in improving the understanding of corporate data models, and may be used to provide a hypertext, model-based interface to a prototype data warehouse.

## References

[1] J.C. Brancheau, J.C. Wetherbe, Information architectures: Method and practice, Inf. Processing and Manage. 22(6), 1986, pp. 453–464.

[2] J.C. Brancheau, B.C. Janz, S.T. March, Key issues in information systems management: 1994, 1995 SIM Delphi results, MIS Quarterly 20(2), 1996, pp. 225–242.

[3] D.L. Goodhue, J.A. Quillard, J.F. Rockart, Managing the data resource: A contingency perspective, MIS Quarterly, pp. 373–392, 1988.

[4] D.L. Goodhue, L.J. Kirsch, J.A. Quillard, M.D. Wybo, Strategic data planning: Lessons from the field, MIS Quarterly, pp. 11–34, 1992.

[5] S.T. Guynes, M.T. Vanecek, Critical success factors in data management, Inf. Manage. 30, 1996, pp. 201–209.

[6] J.A. Hoffer, S.J. Michaele, J.J. Carrol, The Pitfalls of Strategic Data and Systems Planning, in: Proc. 22nd Ann. Hawaii Int. Conf. Sys. Sci. Kona, Hawaii, January 1989.

[7] M.J. Earl, Experiences in strategic information systems planning, MIS Quarterly 17(1), 1993, pp. 1–20.

[8] Y. Kim, G.C. Everest, Building an IS architecture: Collective wisdom from the field, Inf. Manage. 26, 1994, pp. 1–11.

[9] P. Beynon-Davies, Information management in the British national health service: The pragmatics of strategic data planning, Int. J. Inf. Manage. 14, 1994, pp. 84–94.

[10] G.M. McGrath, Migrating information systems through the analysis of power, its determinants and distribution, Ph.D. dissertation, Department of Computing, Macquarie University, 1993.

[11] K.P. Periasamy, Development and usage of information architecture, Ph.D. dissertation, University of Oxford, 1994.

[12] F. McFadden, Data warehouse for EIS: Some issues and impacts, in: Proc. 29th Annual Hawaii Int. Conf. System Sciences, 1996.

[13] G. Shanks, The challenges of strategic data planning in practice: An interpretive case study, J. Strategic Inf. Sys. 6(1), 1997, pp. 69–90.

[14] P. Chen, The entity relationship model: Towards a unified view of data, ACM TODS 1(1), 1976, pp. 9–36.

[15] J. Martin, Strategic Data Planning Methodologies, Prentice-Hall, 1982.

[16] A.-W. Sheer, A. Hars, Extending data modelling to cover the whole enterprise, CACM 35(9), 1992, pp. 166–172.

[17] R. Kimball, The Data Warehouse Toolkit, Wiley, New York, 1996.

[18] J. Krogstie, O.I. Lindland, G. Sindre, Towards a Deeper Understanding of Quality in Requirements Engineering, in: Proc. 7th Int. Conf. Advanced Information Systems Engineering, Jyvaskyla, Finland, June 1995.

[19] D. Moody, G. Shanks, What makes a good data model? Evaluating the quality of entity relationship models, in: P. Loucopoulos (Eds.), Proc. 13th Int. Entity Relationship Conference, Manchester, England, 1994.

[20] G. Shanks, P. Darke, Quality in Conceptual Modelling: Linking Theory and Practice, in: Proc. Asia-Pacific Conference on Information Systems, Brisbane, 1977.

[21] R.C. Goldstein, V.C. Storey, Some findings on the intuitiveness of entity-relationship constructs in: F.H. Lochovsky (Ed.), Entity-Relationship Approach to Database Design and Querying, Elsevier, Amsterdam, The Netherlands, 1990.

[22] S. Hitchman, Practitioner perceptions on the use of some concepts in the entity-relationship model, European J. Inf. Sys. 4, 1995, pp. 31–40.

[23] S. McGuiness, CASE support for collaborative modelling: Re-engineering conceptual modelling techniques to exploit the potential of CASE tools, Software Eng. J., pp. 183-189, 1994.

[24] D. Moody, A Graphical Representation of Entity Relationship Models in: B. Thalheim (Ed.), Proc. 15th Int. Entity Relationship Conference, Cottbus, Germany, 1996.

[25] C. Batini, M. Lenzerini, S.B. Navathe, Comparison of methodologies for database schema integration, ACM Computing Surveys 18(4), 1986, pp. 232–364.

[26] P. Darke, G. Shanks, Stakeholder viewpoints in requirements definition: A framework for understanding viewpoint development approaches, Requirements Eng. 1, 1996, pp. 88–105.

[27] S. Buckingham Shum, N. Hammond, Argumentation-based design rationale: What use at what cost, Int. J. Human-Computer Studies 40, 1994, pp. 603–652.

[28] G. Fischer, A. Lemke, A.C. McCall, A.I. Morch, Making argumentation serve design, Human-Computer Interaction 6, 1991, pp. 393–419.

[29] A. MacLean, R.M. Young, V.M.E. Bellotti, T.P. Moran, Questions, options and criteria: Elements of design space analysis, Human-Computer Interaction 6, 1991, pp. 210–250.

[30] A. Dix, J. Finlay, G. Abowd, R. Beale, R. Human-Computer Interaction, Prentice-Hall, 1993.

[31] J. Conklin, K.C. Burgess Yakemovic, A process-oriented approach to design rationale, Human-Computer Interaction, 6(3–4) (1991) 357–391.

[32] C. Potts, G. Bruns, G, Recording the Reasons for Design Decisions, Proc. 10th Int. Conf. Software Engineering, pp. 418-427, 1988.

[33] C. Potts, K. Takahashi, A.I. Anton, Inquiry-Based Requirements Analysis, IEEE Software, March 1994, pp. 21–32.

[34] J.M. Carrol, Introduction: The scenario perspective on systems development, in: J.M. Carrol (Eds.) Scenario-Based Design, Wiley, New York, 1995, pp. 1–17.

[35] A MacLean, D. McKerlie, Design space analysis and use representations, in: J.M. Carrol (Ed.) Scenario-Based Design, Wiley, New York, pp. 183–207, 1995.

[36] P. Feldman, D. Miller, Entity model clustering: Structuring a data model by abstraction, The Computer J. 29(4), 1986, pp. 348–360.

[37] D. Avison, G. Fitzgerald, Information Systems Development: Methodologies, Techniques and Tools, 2nd edn., McGraw-Hill, London, 1995.

[38] R.K. Yin, Case Study Research: Design and Methods, 2nd edn., Sage Publications, San Fransisco, 1989.

[39] M. Feather, Requirements engineering – getting right from wrong, in: Proc. 3rd European Conf. Software Engineering, Milan, 1993.

[40] R. Guindon, Knowledge exploited by experts during software system design, Int. J. Man-Machine Studies 33, 1990, pp. 279–304.

![](/api/attachments/4GNFNRTM/fulltext/images/1c2eed0346f01e613c8caf770c0f25c4fbb4d5fc5ad08e588c7b5448aaafd21b.jpg)

Graeme Shanks is a senior lecturer in the School of Information Management and Systems at Monash University, Melbourne, Australia. He holds a B.Sc. and a Ph.D. in information systems from Monash University. His research interests include data warehousing, data quality, quality in conceptual modelling, and requirements definition. He has published articles in Information Systems Journal, Journal of Strategic Information

Systems, Requirements Engineering, Australian Computer Journal, and Australian Journal of Information Systems.

![](/api/attachments/4GNFNRTM/fulltext/images/9bfabc159629f40ef15911b5f2835738c4b741ae97031518daf57b960d063387.jpg)

Peta Darke is a lecturer in the School of Information Management and Systems at Monash University, Melbourne, Australia. She holds a B.A. (Hons.) and a Ph.D. in information systems from Monash University. Her research interests include requirements definition, data quality, data warehousing and quality in conceptual modelling. She has published articles in Information Systems Journal, Requirements Engineering, Australian

Computer Journal, and Australian Journal of Information Systems.
