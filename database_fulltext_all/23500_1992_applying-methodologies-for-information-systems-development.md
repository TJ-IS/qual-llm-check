---
otero_id: 23500
otero_key: "3SFK472V"
title: "Applying methodologies for information systems development"
authors: "D E Avison; H U Shah; R S Powell; P S Uppal"
year: "1992"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1992.19"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applying methodologies for information systems development

D.E. AVISON

Southampton University, Southampton SO9 5NH, UK

H.U. SHAH

Aston University, Birmingham B4 7ET, UK

R.S. POWELL and P.S. UPPAL
BT Fulcrum, Birmingham, B9 5LD, UK

Many organizations develop their information systems without the use of any information systems development methodology. However, even when organizations identify the need for the use of such methodologies, it is not always obvious which to use, or whether a blended combination might be appropriate. Further, in using either stand-alone or blended information systems development methodologies in practice, a number of difficulties are encountered. This paper discusses the use of an information systems development methodology which consisted of a blend of other methodologies in a real-world situation (a large telecommunications company) where no formal methodology had been used previously. A number of difficulties arose in practice, some of which were not anticipated. Examples are given of the types of difficulty encountered, and these fell into three broad categories: those related to the deficiencies in the design techniques and tools themselves; those related to implementing the system from the design; and those related to the particular environment.

## Introduction

This paper describes our experiences of applying information systems development methods to an application in an environment where a methodology had not been used previously. No one standard methodology proved appropriate for the application and organization, and a blended method was designed. Even so, a number of problems were encountered and these are discussed in this paper. In the next section, we describe the problem situation and then the blended methodology that was used. The problems encountered with this approach are then discussed. There were three major types of problem: those which related to the deficiencies in the design techniques and tools themselves; those which related to implementing the system from the design; and those which related to the particular environment. The first of these is stressed in this paper because these problems proved to be the most difficult in this case. In the section preceding the conclusion we look at the positive experiences in using the methodology for information systems development in the particular problem situation, and the final section draws on lessons learnt.

## The problem situation

BT Fulcrum (now Fulcrum Communications) was at the time of the work described in this paper (1989–1990) a wholly owned subsidiary of British Telecom which designed and manufactured telecommunications products. Aspects of the organization described in this paper may well have changed considerably in the time since the work was carried out.

The initial terms of reference concerned the possibility of developing an interface between two successful products. The first of these is SCOUR, which is a night surveillance system for testing telephone lines and aims to detect faults before they affect customer service. Each SCOUR system tests up to 180 000 telephone lines every night. The results produced are analysed and a report is output listing any faulty lines. The second product is the M6000 computer system. This is UNIX-based, having communications software and the Informix relational database management system.

The prime objective was to migrate SCOUR facilities onto a modern platform and enhance these facilities where practical. As well as assessing the feasibility of designing the interface, the project team was asked to address a number of other connected issues. Although the user documentation was available, the technical documentation for maintaining the system was neither comprehensive nor up-to-date. Further, since the original design of the system, a number of development tools had become available which could be incorporated into the system. The original development team was widely dispersed and not available and this had also caused maintenance problems.

By migrating the SCOUR functions onto the M6000 platform, management hoped that a number of objectives (discussed below) would be achieved.

## An improved reporting system

The new platform can use a database management system for recording the test results. New reports can be readily produced in this environment, whereas the old SCOUR system was written in C and was not readily modifiable. It was particularly desirable that the reports produced did not restrict themselves to the operations-level data, as is the case in the present system, but would produce strategic management reports which would show district-wide trends (amongst other useful information). It is possible to link several of the SCOUR application systems into a central database and thereby provide management with information coming from a wider geographical area. Further, there were identified opportunities for more sophisticated fault analysis, such as the identification of lines which are frequently faulty and therefore indicate the need for cable replacement.

## Improved fault diagnosis

In the present system the analysis of test results is embedded in the code and cannot be readily modified. With the new platform and its database management system, the opportunity to enhance these facilities by providing more flexible diagnosis of the parametric results becomes apparent. For example, the diagnosis could analyse the fault and assign the necessary repair work to the relevant type of engineer. On the basis of experience, the algorithms for assigning repair work can be adapted by the user. At present, the process of assigning repairs by the system is unsatisfactory because it requires manual intervention and verification.

## Addressing the application backlog

Because of the difficulty of modifying the present code, there are now many improvements which have been requested by the users but not implemented. This has caused some user dissatisfaction. By migrating the applications onto a more flexible and faster development environment, it is to be hoped that many of these needs would be satisfied. Furthermore, there are development tools available on the system which will facilitate development by the users themselves.

## Wider access capability

Because of the network capability, it is possible for a user in one locality to access information on any M6000 and any SCOUR system on the network. It gives the user who has access privileges to interrogate a specific SCOUR system and retrieve test information relevant to that system. The present SCOUR system does not have the same network capability.

## The information systems methodology

At the time of the project, there was no standard adopted for information systems development at BT Fulcrum. The general trend was for the project leader to decide on an ad hoc basis how the project work was to be developed and controlled. The project leader assigned to this project had previously taken a course in information systems and wished to incorporate the appropriate methods learnt at that time in this project.

An information systems development methodology is defined by Avison and Fitzgerald (1988) as 'a collection of procedures, techniques, tools and documentation aids which will help the systems developers in their efforts to implement a new information system. It will consist of phases, themselves consisting of sub-phases, which will guide the systems developers in their choice of the techniques that might be appropriate at each stage of the project and also help them plan, manage, control and evaluate information systems projects'.

In choosing a methodology for a particular application we need to select an approach which identifies and satisfies the requirements of the users. The explicit and implicit assumptions about the factors involved in systems development inherent in the proposed framework and the set of techniques and tools recommended need to be identified and recognized as appropriate for the problem situation.

There were evidently two main aspects to the application. The first concerned data modelling, that is the analysis of the data relating to the telephone network system. The second concerns process modelling and the flow of data through the system. These two aspects could be dealt with independently. However, there was no one methodology that could be said to be ideal for this situation.

In this particular application, the factors seen as important were the need for structured data and the prominence of data flows. The Yourdon approach (DeMarco, 1979) was considered appropriate for the analysis of the component processes and their data requirements. Although it is a well accepted approach and it models the processes and data flows, it is inadequate in the data modelling aspects because it only considers data which is relevant to those processes analysed. It was therefore decided to combine this with a data-oriented approach such as that found in Avison (1985).

Davis (1982) advocates a contingency approach to information systems development. In his view, a particular methodology (from a set of approved approaches) should be chosen depending on the particular circumstances where it is to be applied. In other words, different methodologies will be used for different situations, a kind of 'horses-for-courses' approach. Another contingency approach proposed by Avison and Wood-Harper (1990, 1991) suggests a very flexible contingency approach whereby phases, techniques and tools within one methodology framework (Multiview) are chosen according to the application domain. An unstructured approach to information systems development is suggested by Benyon and Skidmore (1987). They suggest information systems development through choosing techniques and tools from a 'tool-kit'. Avison et al. (1988) argue that there needs to be some sort of framework even in approaches which follow the contingency ideals.

In the project at BT Fulcrum, we have extended Davis' ideas on contingency by suggesting that for the particular problem situation a combination, or blend, of methodologies is appropriate because no one methodology suited out needs. On the other hand, Multiview was not chosen because of the view that the specific combination

![](/api/attachments/3SFK472V/fulltext/images/d5786bcecf97f318f5ee09bb5ab1ec3edfc9a2f4719fda6420032600dea9fb22.jpg)  
Figure 1 Overall approach

![](/api/attachments/3SFK472V/fulltext/images/5f6a69bd1cf93287a212c27502a59ebd841f1a5eee06d4c280cc501d54fe820c.jpg)  
Figure 2 Data-oriented approach

of the data-oriented and process-oriented approaches of Yourdon and Avison were particularly appropriate in this situation and the extra flexibility provided by Multiview was not needed. Further, a formal approach of some sort, with standards and defined phases with deliverables, was chosen as preferable to a tool-kit view of information systems development.

We will look at each of the two approaches which were blended in turn. However, an intermediary phase was added to the two approaches. This intermediate phase looked at some key low-level requirements, essentially concerning design issues related to the choice of database management system and hardware linkages, which was necessitated by the environment. Figure 1 shows the overall approach taken. Later in this paper we discuss the problems encountered in our use of this blend.

## The data-oriented approach

The approach found in Avison (1985) is summarized in Figure 2.

## Business and conceptual models

The first part is business analysis. As described in the text, this phase concerns finding out what are the goals of the organization, company structure and roles of key personnel and deciding on a strategy for information systems development. Some of these were appropriate to the particular problem situation. For example, an attempt was made to establish the company structure and the roles of the key personnel. But this was not as easy as described in the book. It was difficult, for example, to establish who to ask about what (problems of 'ownership'), and even in the situations where this was established there was often restricted access to the relevant people (mainly for political reasons). Furthermore, difficulties were found in boundary definition and in clarifying roles. Other techniques and ideas were added to this phase, because appropriate help was not found in the original text used. For example, the participants in this study widened the scope of this analysis to include the roles of other major players, in particular its competitors and customers. On the other hand, the strategy for information systems development was not included. This part of business analysis involves the identification of business information systems needs and organizing their development, priorities, resources needed, and so on. In this situation, the need had already been established, and the application was developed on the non-competitive basis that resources 'would be found'.

The next phase of the data-oriented approach is data analysis: the creation of an entity-relationship model, including the identification of entities, attributes and relationships, the process of normalizing relations and producing the documentation. In the application, the obvious entities were listed, and for each of these the attributes were named. This was iterative in that there were checks to see if other entities were later identified. The entity-relationship diagram was drawn in rough to illustrate the relationship between entities. Normalization was carried out and this included changing each many-to-many relationship to a series of one-to-many relationships by adding new entities. An example of this is given in Figure 3, where 'Test Selectors' are pieces of equipment which provide access to 'Units'. A 'Unit' is a rack of switching equipment. After the normalization process, the extra entity 'TA Unit Link' was created which provided the information identifying which 'Unit' connected to which 'Test Selector'. The result of this phase was an E-R model of normalized relations, along with data dictionary entries. This phase of the data-oriented approach was followed closely in this project and it was found to be appropriate. Carrying out the data modelling first provided a model of the organization independent of the applications (Robinson, 1989). In comparison to processes, data was considered to be relatively static in structure and therefore this was a useful way to model the organization. Further, because the organization would be modelled using a database management system, it was anticipated that the applications would be easier and quicker to develop when required.

## Logical and physical models

Phase three concerns the mapping of the data model onto a database management system (DBMS). The DBMS chosen was Informix, a relational system widely available on Unix computers. Mapping onto a DBMS provided an environment to test potential application prototypes. There is a further mapping (phase 4 of the approach) relating to the best way in which to store the data on the database. However, for the particular problem situation it was not appropriate at this stage to work on performance tuning, indexing and so on. This would occur at a later stage.

## Applications development

The final phase of this approach is ‘applications development’. This was considered to be insufficiently defined in Avison (1985) and therefore an alternative approach was sought (as a result of these and similar experiences, these issues amongst others have been addressed in Avison (1992)). It was considered that to move immediately to the development of applications would be unwise as it had not yet been established that the key detailed requirements could be met. This prompted us to add a step in our development cycle which has been called the ‘intermediate phase’ in this paper.

![](/api/attachments/3SFK472V/fulltext/images/add78671e8e299116cc373de18753e1e702cf499299bfc4be4843a95d55b56ee.jpg)  
Figure 3 Removing many-to-many relationships.

## Intermediate phase

At the end of the data-oriented stage, we knew the overall context of the application including an overview of the requirements as well as data models. From these requirements it was necessary to pick out key detailed requirements before attempting the next stage which consists of developing the applications. This involved consideration of the physical devices. For example, in the application it was necessary to interface the DBMS with the test-head, which is the hardware that tests the lines. If this could not have been achieved it would have been necessary to review the practicability of the previously imposed hardware and software, which were constraints on our design.

This phase was necessary in the context of our problem situation as it would have been inappropriate to progress with the application if these key requirements could not be met. It would in this case have been necessary to backtrack and review the logical model, amending as necessary. By identifying the key requirements and ensuring that they could be met, we are ensuring that the data model and its implications are appropriate for the application. This helped to avoid the possible situation where the total model is developed only to find that it is inappropriate.

## Subsystems development

The Yourdon approach (DeMarco, 1979) was considered to be suitable for the development of applications, as it concentrates on processes and their data flows. This approach involves the use of a number of techniques and tools – data flow diagrams (DFDs), data dictionary, structured English, decision tables and decision trees – to produce the ‘target document’ which is a structured specification of the requirements. This incorporates the data dictionary, the data flow diagrams and mini-specs. The latter are descriptions of the rules governing the transformation of data flows.

This approach was felt to be suitable for us to develop these applications as it allowed a large problem to be decomposed into smaller units which could then be understood and manipulated more easily. Further, the data-oriented approach does not help in defining applications rigorously. The reason for using the two approaches in combination was that the first, the data-oriented approach, helps to define the data structures while the second approach is more process-oriented. This meant the combined approach would result in the definition of the data of interest and the processes which used that data. It also enabled the use of associated tools.

The six phases of the DeMarco approach are:

(1) Study the current physical environment.

(2) Derive the logical equivalent of the current environment.

(3) Derive the new logical environment.

(4) Establish the human-computer boundary.

(5) Quantify options.

(6) Select options.

## Study the current physical environment

Phase one of the DeMarco approach involves carrying out a study of the physical environment. In our case this meant identifying what SCOUR currently does. This was only a limited investigation and drew upon the findings of the business analysis stage of the data-oriented approach. It involved investigating how SCOUR worked, what files it created and for what they were used. Figure 4 shows a simplified model of part of this analysis phase.

As SCOUR was an existing computer system, we were unable to sensibly decompose it into its levelled subsystems. Further, as the aim of the project was to interface SCOUR to the M6000 in order to produce strategic information and reports, it was inappropriate to decompose SCOUR. There were no existing physical procedures for the production of management level reports. It was one of the aims of the project to try to provide this.

## Derive the logical equivalent of the current environment

Phase two in this approach is essentially a clean-up task, to remove physical checkpoint items and replace with logical equivalents (see Figure 5). Up to this point, existing practices and procedures had been modelled and no attempt was made to incorporate the new requirements. The next phase addresses this aspect of the design.

## Derive the new logical environment

Phase three of the DeMarco approach concerns modelling the new logical system. It involves incorporating the changes stated in the 'Feasibility Document' which in this case consisted of the requirements document that had been produced to initiate the project. The new top-level DFDs had already been developed before talking to users as it was already known that the overall requirement was to interface the products and produce strategic level reports (see Figure 6). This involved going to user sites and talking to users to find out what type of management level reports were required. The groups of people involved were strategic management, operational management and operational staff. As well as identifying what information and reports were required, it also involved identifying what improvements could be made to the operational level information. As stated earlier, this was not a simple task. The information gathered was documented on the data flow diagrams in the form of reports required. These were shown to the users in order to get their agreement. DFDs were felt to be the appropriate notation to use in discussions with users since they are comparatively simple, and easily understood and modified.

![](/api/attachments/3SFK472V/fulltext/images/4840749cc7ab0d362422ec15ab69f332fcef0e33fec3760fc4fee5a7eb37edf7.jpg)  
Figure 4 Data flow diagram of the physical environment

Each of the processes was decomposed, taking into account the users' requirements as established in the various interviews and investigations. Normally at this stage, the lowest level data flows would be decomposed into their constituent attributes, but as a data model already existed (from an earlier phase of our blended approach), the attributes which made up each data flow were taken from the data dictionary instead of the other way around. This helped to avoid giving the same attribute several different names (or aliases). Many of the data flows turned out to be complete entities rather than subsets of their attributes.

Each bottom level process on the data flow diagram was

![](/api/attachments/3SFK472V/fulltext/images/1117533fdd9679cdf5e5d02bbcf40323c8fdd1a64b5328de4a55788653555aaf.jpg)  
Figure 5 Data flow diagram of the logical equivalents

![](/api/attachments/3SFK472V/fulltext/images/ada71aa3452cdd695d523095a4a31275f4f9f0880f00f573a8616e9b8cb31398.jpg)  
Figure 6 Top level DFD of the new logical system

described using a mini-spec. The mini-specs were not necessarily in structured English, since many of the processes were reports. It was more appropriate to describe these with examples and general comments. For example, a report to list exchanges with the most faults per exchange connection in each month along with an example format was felt to be the most appropriate description of the process. To express this in structured English would go unnecessarily to a lower level than the eventual implementation code itself (especially where 4GLs were to be used).

## Establish the human-computer boundary

Phase four concerns establishing the human-computer boundary. This was a relatively straightforward phase as it was felt that the boundary was well defined from the beginning of the project. Although DeMarco recommends that several alternative human-computer boundaries be identified, this was not practical in this application because the actual project requirement was for a computerized system to produce the high level strategic reports. There was also a well defined machine-machine boundary which was clearly specified (see Figure 6).

## Quantify options

Phase five involves quantifying options in terms of costs and benefits. The options available were either (a) to have this machine-machine boundary or (b) to remove this boundary by linking the M6000 directly to the test heads rather than via the SCOUR system. The former option (a) was selected. It did provide a migration path to the latter (b) which was taken to be a long term objective. DeMarco suggests that it is too early to select hardware in this stage. However, in real world applications such as this, hardware and some software details had been specified long before this stage. For this reason we incorporated an intermediate stage in our hybrid methodology. Such 'real world' factors may be due to political pressures, which may also include a preference for products supplied by the organization. All processes on the data flow diagrams were not necessarily developed into applications. These processes may or may not be developed at some future stage. This implies that for any undeveloped process the human-computer boundary was moved.

## Select options

Phase six involves the selection of options and in our case the option (a) described above was selected. By the end of this stage the output consisted of data flow diagrams, a data dictionary and the relevant transform descriptions (mini-specs). Of these, the data flow diagrams were in the form described by DeMarco. However, the data dictionary now consisted of two parts: a main part, as obtained from the data-oriented approach, and a second part defining the composition of the data flows in terms of entries from the data dictionary, for example, that shown in Figure 7.

The dictionary entry for this data flow would be:

```shell
customers_lpr =
exchange +
pcp +
dp +
phone_route....
```

where exchange, pcp, dp, phone\_route... are all entries in the main part of the data dictionary and customers\_lpr is the data flow label for this group of entities.

At this point it was found to be necessary to extend DeMarco's approach to include an extra step involving the definition of data flows across the machine-machine boundary. It was necessary to define not only the data content but also the control protocol for this boundary. The data flow shown in Figure 6 which crossed the machine-machine boundary required an associated protocol to be defined. This was an additional output.

![](/api/attachments/3SFK472V/fulltext/images/74b098ae2e0b653076dbdb2cd305a1313dac22714b922e16f21579d78f3aed37.jpg)  
Figure 7 Data flow 'customers\_lpr'

The development of the design consisted of implementing the mini-specs in the available environment. The transformation of the design into actual code required the selection of the best language for each process. In this project various processes were implemented in different languages, including C, Unix shell scripts, Informix ACE reports and Informix 4GL.

## Problems encountered

The problems encountered could be divided into two main areas: firstly, those which related to the deficiencies in the design techniques and tools themselves, and secondly, those which related to the environment into which the techniques were being introduced. We concentrate on the first of these as it had greater impact in this application.

## Problems with the methods and tools

Problems were encountered within various stages of our blended methodology. This section outlines the major problems encountered and the steps taken to overcome these problems. Some were not strictly ‘problems’ but areas where there was felt to be scope for improvements in the methods. The difficulties are related to the various stages of our blended methodology.

## Data-oriented approach

There were several problems encountered during this stage of the overall approach. Each of these is described below.

E-R diagrams were found to be an excellent tool for representing entities and their relationships, but they omitted features for what we term 'limited selective relationships'. These occur where the relationship between entities A and B may vary depending on a key attribute of A. For example, consider the relationship between the two entities cable\_pair and phone\_connection as shown in Figure 8. This relationship can vary depending on the attribute of phone\_connection called class\_of\_service. In most cases the class\_of\_service is 'Normal' and the relationship is one-to-one, as one phone is connected to one cable pair. However, two other situations may exist. When the class\_of\_service is 'Shared Service' there may be two phone\_connections on a single cable\_pair thus giving a two-to-one relationship. Finally the class\_of\_service may be 'PBX' where several cable\_pairs may go to a single phone\_connection hence giving a (d) When class\_of\_service = 'PBX'

(a) Relationship from E-R diagram  
![](/api/attachments/3SFK472V/fulltext/images/01fe35007b3071b37f90a731c6276ab9276fda964e832c54981273d872b99e1d.jpg)

![](/api/attachments/3SFK472V/fulltext/images/b0d73ae567dbfb7a4a4c43e950c6223d873fb1172aaafa6c6abc68d770521cd6.jpg)

![](/api/attachments/3SFK472V/fulltext/images/c4db7a5f42c46f235ba67be3ffbfdf040b453370096bef717b7a11331013729c.jpg)

![](/api/attachments/3SFK472V/fulltext/images/2a43e8480bb4ff50f693bf4446c5aebbf7d04ee8dc1b2c11a89e957c8f94d999.jpg)  
Figure 8 An example of a 'limited selective relationship'

one-to-many relationship. This may be depicted as a many-to-many relationship on an E-R diagram, but this is an inadequate description of the actual relationship.

Another aspect of entities is that they have features which are useful in sizing a system. For instance, a feature of employee could be that there are up to 10 000 employees, depending on the target user. Another example of such a feature could be that there are over 1 000 000 telephone lines in a district. Features such as these could, for example, give an indication of the type of DBMS that might be required. This also ties in with the key requirements evaluation phase that was described earlier. The data-oriented approach does not suggest that such features be recorded in the data dictionary.

In addition, the Avison text did not provide any detailed data dictionary definition conventions and so those specified by DeMarco (1979, p133) were used. It was felt that these conventions could be improved by including data types as part of the notation. For example, 'date' is a commonly used type. In our application 'measurements' was also an important type. For example, each time 'capacitance' was referred to, its format had to be specified. There is no notion of a common data type in

DeMarco for data dictionary entries. This leads to redundancy and means that a change to the format of the capacitance value would require that the entire data dictionary be searched and all occurrences of capacitance changed to the new format.

The final problem in this stage of the blended methodology was that the transition from conceptual to logical was not a simple step, as implied in the text. There may be no one-to-one correspondence of entities to tables. For example, one entity in the conceptual model, Test\_Results, is split into three tables in the logical model. This could be due to performance reasons. Figure 9 shows how three logical entities (Today's\_Results, Yesterday's\_Results and Historic\_Test\_Results) come from the one conceptual model entity Test\_Results. We needed to provide fast access to the entity Today's\_Results, a requirement established during the intermediate phase.

## Intermediate stage

The main difficulty encountered during this stage was that the process of normalization had led to large numbers of tables being produced. This affected performance, especially when manipulating the database involved joins across many tables. To help reduce this effect, some of the tables were ‘denormalized’. This involved a considerable amount of work and the whole process became more ad hoc. It is important to note that having normalized first, every ‘denormalization’ identifies an area of the database which requires care when updating.

![](/api/attachments/3SFK472V/fulltext/images/15d11b3a13d5adeabe810d9a7a24bb3c6ab2777f485d2f892a247272dab152c9.jpg)  
Figure 9 Logical entity

## DeMarco's approach

There were a number of difficulties encountered using DeMarco's approach including those concerned with specification of required reports, use of the top-down approach itself and using DFDs in particular. All of these are discussed below.

In this project many of the processes produced statistical reports. There was difficulty in defining the exact requirements of the users, for example, getting managers to think about what statistics they required, particularly what would be really useful, rather than simply cosmetic. This was felt to be a deep-rooted problem in that manually produced statistics often denote trends over particular time-scales. However, such statistics often had little real value and only monitored a situation over time. If the analysis is not carried out properly there is a real danger in this area of decreasing the usefulness of the system by either choosing the ‘wrong’ reports or by producing too many reports and overloading the user. So much is possible that extreme caution is necessary and the actual reports required may only be identified when a ‘live’ system has been in use for some time.

The use of a top-down approach caused difficulties in three main areas. The first occurred when interfacing to devices for which only a low level specification was available. In this case, a bottom-up approach was necessary. In some cases the lower level DFDs had to be of a different format, for example, in the form of state diagrams for the devices. This was found to be true especially for processes which 'controlled' a device. In the approaches used, data is the dominant feature and control is an afterthought, whereas, for devices, control is the dominant feature.

The second area where the top-down approach was found to be a problem was in providing an improved fault-diagnosis algorithm. At a high level, the diagnosis function was of the form shown in Figure 10, but to decompose it any further would have been extremely difficult. It was much easier to look at the parameters, of which there were 13, and make useful building blocks (see Figure 11). From these parameters we can see that certain capacitance values can be used to deduce the class of service that is being provided on that line. By combining many such building blocks, the fault-diagnosis function was constructed. The DFD technique was still useful to document the process structure after the building blocks had been pieced together.

The third area where this was found to be a problem occurred when interfacing to undocumented software.

![](/api/attachments/3SFK472V/fulltext/images/6cc27e1b421147609c48844863a16544c0d08ef3e4315bc612a4254970607084.jpg)  
Figure 10 High-level description of ‘produce\_a\_diagnosis’ function

![](/api/attachments/3SFK472V/fulltext/images/f1ee73557c3bfd62c20081e5a90e1b4319c2097787a8f80bc253ec95d0801b83.jpg)  
Figure 11 Building block

The only description available of such software was the code itself, which tended to be of a low-level nature, and again had to be dealt with in a bottom-up manner.

As discussed earlier, one of the major tools of the DeMarco approach are DFDs. Although a feature of DFDs is that they are system independent, it would be useful if they could be used to identify critical regions in the underlying system so that effort could be concentrated on these areas. An example of this would be the provision of notation so that a particular process on the DFD could be identified to say, for example, 'this process must produce its output from its input within 10 seconds'. Factors such as these may determine hardware and software requirements and are therefore very important.

DFDs also lack a facility to indicate whether particular processes could be run concurrently and, if so, what is the maximum number of occurrences. In addition, there is no facility to indicate critical resources. It would be more useful if such details were highlighted on the DFDs rather than at a later stage in the mini-spec. If the assumption is that a DBMS is to be used, then this is less significant. However, if the underlying data is held in conventional files then this could lead to problems. For example, in a 'user data entry' process, should two users wish to use that process concurrently or both enter data for a single telephone number, then this would also result in major problems.

A further problem was encountered with DFDs when dealing with common modules. DeMarco's notation for labelling processes does not allow two separate occurrences of the same process to be identified. This means that each occurrence of the duplicated process required its own mini-spec. For example, the diagnosis algorithm was a complex process which operated on data in many parts of the system and each reference to it had to be labelled with a different process identifier according to DeMarco's notation. Perhaps a 'normalization' of processes is also necessary. In this project this difficulty was overcome by one such common module being described in mini-spec form and other occurrences referencing this mini-spec.

## Implementation from design

The methods used did not provide any tools to address the problem relating to which users have access to which processes and how this access is achieved. For example, a manager may require access to all possible processes whilst a clerical officer may only require access to a subset. This involves issues such as specifying which users get particular menu options and is a necessary consideration in the design of such menus. This is relevant to security and access privileges. As these details were not catered for, they had to be considered during the implementation stage and this involved defining different menus for particular users at this late stage in the project.

A DBMS was found to be a useful tool for supporting the data-oriented approach but also causes some significant problems. For example, the version of Informix used in this application made assumptions about user requirements and organized its indices accordingly. This led to 'skew indexing', where the index becomes unbalanced because the distribution of values for a particular attribute is not even. As a result, data access was slower than expected and since a tuning facility was not provided nothing could be done about it. This problem is of significance because speed is a major feature by which systems are judged by users.

## Environment

There are a number of side-affects that arose as a result of employing a methodology-based approach. It was difficult to come to terms with the fact that a lot of time elapsed before it was seen by management and other staff to be productive. There was a tendency to view the project as over-costed. In addition, the approach was seen as 'academic', required too much effort 'up-front' and increased the danger of slippage in time-scales. From the developers' point-of-view, they had their own traditional ways of developing computer applications which often consisted of a specification in natural language which would then be transformed into code. They were resistant to the new techniques. Further they needed to be convinced that this approach was better than the approaches which were more familiar to them.

In real-world situations it is often necessary to interface the methodology to existing standards and procedures. In our case, for example, part of the contractual obligations involved adherence to BS5750 (1987) which is a British quality standard that has existed since 1979. Accreditation under this standard implies a certain level of quality in the company's products. The documentation procedures of this standard specify that as documentation changes its issue level is increased. As many of the documents are subject to change during particular stages of the development, the task of keeping these up-to-date with issue control numbers becomes a major problem. To solve this practical problem it was decided to produce one document, the 'Design Definition Document' which included mini-specs, functional hierarchies, data flow diagrams, software requirements, hardware requirements, conceptual model and data dictionary. This document was then issue controlled, that is, subjected to the issue procedures of the BS5750 standards. The problems associated with documentation are, however, greatly alleviated through the use of data dictionary systems.

## Positive experiences

This project has shown that the use of a contingency approach to information systems development can be successful if used in a disciplined way. Although this paper has concentrated on a discussion of the difficulties of using information systems development techniques in our particular environment, there were many positive aspects to using such techniques. Most of the benefits of such approaches are well documented elsewhere (Gane and Sarson, 1979; Avison and Fitzgerald, 1988; Bull, 1989) and we concur that the benefits exceeded the costs in our application. Our concentration on the costs is due to the fact that these are normally neglected in texts and in the literature of suppliers.

One of the major benefits of the database stage of the overall methodology used was that it made it very easy to maintain the data dictionary and limited scope for potential inconsistencies, both in the data dictionary and in the database itself. Further, the structured format of documentation made it relatively easy to add enhancements to the system. New processes slotted in easily and extending the data dictionary caused few problems. Through use of DFDs, discussions with both users and other developers became focussed. Areas that required modification were easily identified. They were also useful in identifying alternatives and in identifying housekeeping routines that were required. For example, Figure 12 shows two possible options for handling the data flow between two processes. If the second option is selected, some sort of archiving facility may be necessary. Organizing integrated debugging facilities is also made simpler.

The overall use of a methodology-based approach fitted in well with the aim of quality products. In terms of project management, the employment of methodologies led to much better control of the project. Firstly, this was in terms of the initial costing. The decomposition of the problem into sub-modules make it easier to cost individual modules and hence arrive at a more accurate overall cost for the project. Secondly, the monitoring of plans is now based around modules and is well-defined.

## Conclusions

It could be argued that many of the problems that were encountered would not have arisen if a single methodology has been used in its entirety. However we have attempted to describe the problems that have arisen and no one methodology was appropriate to our problem situation. In many cases a mixture of tools and techniques will always be more appropriate than using one methodology in its entirety. However, the experience at BT Fulcrum showed the necessity of using some form of methodology framework even if no ‘off the shelf’ methodology is appropriate, because of the discipline that it imposes.

Experience of this project has shown that a contingency approach can be successfully applied, but the underlying techniques and tools need to be well-understood. The developers need to be flexible and experienced, particularly as aspects of the methodology may not be well-defined and techniques need to be modified for the particular circumstances. Further, the 'philosophy' of the methodology needs to conform to the requirements of the organization and application. The assumptions about the factors which are significant need to be stated explicitly and the approach needs to be defined in detail. Without such discipline, a contingency approach may lead to misguided effort and poor results. When successfully applied, a contingency approach allows the benefits of the experience and expertise embodied in good methodologies to be focused on the particular needs of a situation, and will provide significant advantages in terms of cost, time and quality.

![](/api/attachments/3SFK472V/fulltext/images/07918cdf097aaecf090ed58e499c9af438c168492fb0671cc41bf5c774d56f4a.jpg)  
Figure 12 Options available

The use of methodology-based approaches make it easier to extend and add applications and to help in identifying possible alternatives. Further, of especial interest in this particular environment, it ties in well with the concept of quality products. This enables much better control of the project and conformity to a particular standard, in this case BS5750.

Both the data-oriented and the process-oriented structured analysis approaches which made up the blended methodology used had particular problems, some of which were overcome by blending them. While this overcame some of the incompleteness of the individual approaches, there were still many problems remaining. These problems have been detailed in this paper and possible solutions suggested.

Our experiences lead us to conclude that methodologies for information systems development should not be treated as a series of strict rules that must be adhered to in all situations, but as a framework containing tools and techniques which can be drawn upon as and when required. Further it is considered perfectly valid to refine and adjust any tools to suit a particular situation.

Management and systems development staff at BT Fulcrum were more disposed towards the use of a systems development methodology at the end of the project despite a number of problems which have been identified in this paper. This suggests that the use of the blended methodology in our situation was successful.

## Acknowledgements

The authors wish to thank one of the referees, Gill Smith of Oracle, for very valuable and constructive criticism of the original draft submitted. Many of the suggestions made by her have been incorporated into this final manuscript. We also wish to thank Tom Brassil of

Fulcrum Communications for permission to publish our findings.

## References

Avison, D.E. (1985) Information Systems Development: A Data Base Approach (Blackwell Scientific, Oxford).

Avison, D.E. and Fitzgerald, G. (1988) Information Systems Development: Methodologies, Techniques and Tools (Blackwell Scientific, Oxford).

Avison, D.E., Fitzgerald, G. and Wood-Harper, A.T. (1988) Information systems development: a tool-kit is not enough. Computer Journal, 31, 379–380.

Avison, D.E. and Wood-Harper, A.T. (1990) Multiview: An Exploration in Information Systems Development (Blackwell Scientific, Oxford).

Avison, D.E. and Wood-Harper, A.T. (1991) Information systems development research: a pragmatic view. Computer Journal, 34, 98–112.

Avison, D.E. (1992) Information Systems Development: A Database Approach, 2nd edition (Blackwell Scientific, Oxford).

Benyon, D. and Skidmore, S. (1987) Towards a tool-kit for the systems analyst. Computer Journal, 30, 2–7.

BS5750 (1987) BS5750 Quality Systems Manual (British Standards Institute, HMSO, London).

Bull, M. (1989) Systems Development using Structured Techniques (Chapman & Hall, London).

Davis, G.B. (1982) Strategies for information requirements determination IBM Systems Journal, 21, 4–30.

DeMarco, T. (1978) Structured Analysis and System Specification (Prentice-Hall, New Jersey).

Gane, C. and Sarson, T. (1979) Structured Systems Analysis: Tools and Techniques (Prentice Hall, New Jersey).

Robinson, H. (1989) Database Analysis and Design, 2nd ed. (Chartwell-Bratt, Bromley).

## Biographical notes

David Avison, PhD has recently taken up the post of Professor of Information Systems in the Department of Accounting and Management Science, University of Southampton. He was previously Senior Lecturer at Aston University's Department of Computer Science. He has also worked for a number of companies as chief programmer, systems analyst and project leader, and as an independent consultant. He has had two visiting fellowships in Australia and has also lectured widely in the United States. He has published several research papers as well as 11 books on information systems. In addition to being joint editor of the Journal of Information Systems, he is joint consulting editor of Blackwell Scientific's series of texts on information systems.

Hanifa Shah, PhD is a lecturer in the Department of Computer Science and Applied Mathematics at Aston

University. She has worked as a programmer, systems analyst and senior software engineer in industry and also as an independent consultant. Her research interests are in information systems and databases. She is currently supervising several doctoral students in these areas, some of whose research projects are industry based.

Richard Powell, MEng has a background in electronic systems engineering. He has worked for a number of companies as a design development engineer, systems support consultant and also as an independent consultant. His interests are in information systems development and database design and in investigating the practicality of theoretical issues in these areas.

Pala Uppal, MSc has had experience in the design and development of computer systems ranging from microprocessors to large distributed information systems. His interests include database approaches to information systems development, communications and connectivity of distributed systems and software design technologies.

Address for correspondence: David Avison, Professor of Information Systems, University of Southampton, Highfield, Southampton SO9 5NH, UK.
