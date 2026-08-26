---
otero_id: 18288
otero_key: "Y93439UX"
title: "Blueprints: Adopting a construction trade approach in designing large scale management information systems"
authors: "Robert S. Tripp; Mark C. Filteau"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90010-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Blueprints: Adopting a Construction Trade Approach in Designing Large Scale Management Information Systems

Dr. Robert S. Tripp

Anderson Graduate School of Management, University of New Mexico, Albuquerque, New Mexico 87131, USA

and

Mark C. Filteau

Vice President for Information Systems, The BDM Corporation, Dayton Regional Headquarters, 1900 Founders Drive, Kettering, Ohio 45420, USA

In building large scale MIS, it is not only necessary to employ a rigorous development methodology, but it is essential that the material recorded and used at each step in the design process be effectively communicated between users and developers. This paper describes a "new" method for facilitating effective communication between users and developers in the process. The method literally adapts construction blueprints to the MIS design process. The intent of these blueprints is to capture the essence of the design and facilitate communication with the users without the bulk verbiage that it takes to provide traditional written specifications. The paper shows how blueprints were used in the development and implementation of the Air Force's largest distributed processing MIS – The Requirements Data Bank (RDB) to aid in effective communication and reduce critical design errors.

Keywords: MIS development methodologies, MIS design methodologies, MIS prototype methodologies, MIS communication methodologies.

## 1. Introduction

Development methodologies for Management Information Systems (MIS) are constantly being enhanced. Information Engineering (IE) is the term being used to describe the latest set of methodologies. A significant portion of the IE literature describes a rigorous framework and associated techniques that can be employed to insure that sound technical design principles are introduced

![](/api/attachments/Y93439UX/fulltext/images/5a3be88c5db8c6fef63db8b39ed5039f4c5fa2d745b2f74b7f4566a71da4f0e0.jpg)

Dr Robert S. Tripp is an Associate Professor of Management in the Robert O. Anderson Graduate School of Management at the University of New Mexico. Before joining the University of New Mexico, he was the Program Director for the Air Force Requirements Data Bank (RDB) System Program Office (SPO). His responsibilities included the design, development, and implementation of the RDB System. He has also directed the successful development of two other large scale

MIS developments - The AFLC Command, Control, Communications, and Intelligence (C{3}I) System, and the Weapon System Management Information System (WSMIS) at Headquarters Air Force Logistics Command (AFLC). He has published numerous logistics related articles in several leading journals. He holds a Ph.D. from the University of Minnesota.

![](/api/attachments/Y93439UX/fulltext/images/3b8071e44778e6582d8d597eb41c966f925957a18c40caa6533fca0452ddbd17.jpg)

Mark C. Filteau is Vice President of Information Systems and Technical Director of the RDB program for BDM Corporation. Prior to the RDB program, Mr Filteau managed development of information systems for NASA, the U.S. Naval Air Test Center, the U.S. Department of State, AT & T Technologies, Citibank, the World Bank, and the International Finance Corporation. The NASA Space Telescope Decision Support System (STDSS) received a NASA Achievement Award in October, 1985 and has been the subject of articles on decision support system design in Federal Computer News and Washington Technology magazine. Mark C. Filteau holds a M.S. from Florida State University and a B.A. from the University of Massachusetts.

in each step of the MIS development process. In building large scale MIS, it is not only necessary to employ a rigorous approach, but it is essential that the material recorded and used at each step in the design process be effectively communicated between users and developers. The purpose of this paper is to present a “new” method for facilitating effective communication between users and developers in the process. The method literally adapts construction blueprints to the MIS design process. Thus, much as a prospective custom home buyer would “look at” and modify several iterations of a new home design on blueprints, before ground is broken, this concept involves the MIS user in looking at several iterations of the MIS design blueprint before coding is started. This approach was developed and used in the implementation of the Air Force’s largest distributed processing MIS – “The Requirements Data Bank” (RDB). The paper shows how blueprints were used in the development of RDB to aid in effective communication and reduce critical design errors.

## 2. Background: The Requirements Data Bank

The Air Force Logistics Command's (AFLC) primary mission is to insure that materiel resources are available to support Air Force weapon systems throughout a variety of scenarios.

The accomplishment of this mission is dependent to a great extent on the AFLC “Materiel Requirements Planning” (MRP) Process. This involves forecasting the acquisition and repair requirements of approximately 900,000 spares, repair parts, and equipment items worth nearly 28 billion dollars [1]. It involves predicting the need for about 15 to 17 billion dollars annually for acquisition and maintenance of these items [2].

Beginning in the mid 1970s, the materiel requirements process was criticized as being inundated with many problems and inefficiencies. There are currently 22 data systems being employed by AFLC to manage this enormous task. These systems were developed in the 1950s and 60s and are antiquated. AFLC realized that to meet their logistics objectives and technological needs, certain changes, modifications, and enhancements must be applied to the existing MRP process. Through systematic analysis and design, a major developmental program known as the “Requirements Data Bank" (RDB) was established to develop and implement the needed improvements.

The RDB involves an enormous development effort. For example, it will completely handle both the automated and manual areas involved in the materiel requirements process. It will involve development of nearly 3.7 million lines of code to replace the primarily batch oriented 22 main data systems. There will be over 5,600 users involved with the RDB, using smart terminal interfaces on several geographically dispersed distributed processing sites within the United States. This major program will cost nearly 300 million dollars to develop and operate over the next ten years.

The RDB data environment is estimated to include over 9000 unique data elements and an intermix of two data distribution schemes. The first partitions the data value to each of the distributed sites and thus ensures fast response, immediate data currency, and basically “puts only the data needed where it’s needed”. The second scheme replicates a minimum essential set of core data across all sites and consequently allows site data visibility, quick response, and minimization of network overhead. A complete copy of all RDB databases is also held at two sites.

The reader will appreciate the complexity of the synchronization and communications of databases. It has been estimated that it will have over 60 billion bytes of data at four sites and 90 billion at two others having complete copies of the entire database. It is estimated that 90 percent of the operations will be on-line and 10 percent batch.

When AFLC top management made the commitment to develop RDB, a cadre of top functional people began a seven year planning effort which lead to the selection of a professional services contractor to develop RDB and made financial resources available for the ten year development. Following contract award, AFLC assigned its top systems people to staff a System Program Office (SPO) to manage the efforts of the contractor and colocated the best functional specialists with the SPO and contractor for the life of the development. The functional specialists were assigned from the headquarters but had the authority to “order” functional specialists in each area from the decentralized operational sites of AFLC to the development site whenever their expertise was needed.

To accomplish a task this large, a sound IE approach had to be developed and implemented. Several formal and popular approaches were reviewed and studied before a hybrid IE approach was selected.

## 3. Information Engineering: The RDB Approach

The ultimate goal of information engineering is to build a set of requirements that form a sound foundation for the design of an organization's data structures and associated application software. There are a number of techniques, methods, and rules that can be followed in the engineering of information. The set of methods which are currently being used is an eclectic blend of approaches which have borrowed heavily from Martin's work on strategic data planning [3,4]; Howe's work on data analysis techniques [5]; and Inmon's work on information systems architecture [6]. While the RDB IE methodology is largely derived, some additions and innovations have been developed which expand on the methods discussed in the literature.

Like the approach suggested by Martin, the RDB application of IE principles was performed in three steps. In step one, the focus was on developing enterprise and associated conceptual data models. Step two involved refining the conceptual model and developing the physical models. During this step, program modules were related to their appropriate data tables. In step three, the physical implementation activities took place.

Because of its tremendous size and scope, it was recognized early-on that it was highly unlikely that a single global logical and physical model could be built. It was not possible to determine whether the IE concepts outlined above had ever been applied to an undertaking as large as RDB. In addition, most Air Force functional experts had “stove pipe” knowledge of the systems that were part of the integration effort. As such, it was decided to partition RDB into sixteen segments with clearly identifiable boundaries. Each segment would develop a local information model and concentrate on that segment’s “scope of integration,” as Inmon might suggest. Each local model was then combined to form an integrated global model as shown in Fig. 1.

The development of the RDB conceptual model involved four major phases. Phase 1 entailed de-

![](/api/attachments/Y93439UX/fulltext/images/7cc3ca5c4a16dadd7eafb719170637f8d834c0a14733b45d41ffa46d35f8f9c6.jpg)  
veloping a concept of operations to guide the RDB development and insure that top management goals for RDB were incorporated in the design. Phase 2 involved developing product definitions, including the logical data model, program functional hierarchy, screen designs, and implementation plans for each major RDB segment. Phase 3 involved creating blueprints for each major segment. Phase 4 involved populating the database for that segment, coding the application software, testing and installation. Fig. 2 shows a schematic of this process.

## 3.1 Phase 1: Developing a Top-Down Concept of Operations and Conceptual Architecture

The intent and objectives of the RDB were captured through a top down analysis of its proposed operations. This analysis led to the publishing of a concept of operations which was jointly developed by the SPO and the users. It functionally described the “new world” that the RDB was expected to achieve and showed how it would change current operations. In addition, the RDB process functional descriptions (PFDs) that defined the detailed requirements of its sixteen segments had to be shown consistent with the concept of operations. This check for consistency was done to insure that the PFDs were supportive of the direction that top management wanted to pursue in the future and not just an on-line version of the current systems and methods of doing business.

![](/api/attachments/Y93439UX/fulltext/images/ef478dd77704583a9d8c3142f6263c9e3104e2ec4b0a3ea0e0125c6a5bb7617c.jpg)

The portfolio of completed PFDs included over 6500 pages that describe more than 2200 processes that were to be automated. The PFDs were developed using computer automated software developed by several vendors. The tools which were used to produce these deliverable documents included: engineering tools developed by Intech Corporation called Excelerator and Customizer; Samna Word Processing System; R:Base 5000; and the Ventura Publisher [8,10–13]. These tools were integrated into a “design factory” as shown in Fig. 3. The principle benefit of the design factory approach is to provide for smoother integration of design information from multiple sources into a deliverable document.

As shown in Fig. 3, Excelerator was used primarily to graphically describe the functional aspects of the requirement. Customizer was used to format Excelerator files for use by the Ventura Publisher. R:Base 5000 was used to develop information on database elements. Narrative text, which is a major component of the PFDs, was produced using the Samna Word Processing System. The resulting narrative, graphic elements, and database elements of the PFDs were then merged using the Ventura Publisher to produce the deliverable document.

These PFDs have been completed and took over two years to develop, and involved the participation of hundreds of people from all sites in AFLC. The PFDs not only spelled out the functional requirements, but offered details of all the process activities.

To insure that effective communication was taking place between the users, SPO, and the development contractor, design teams composed of members from all these groups held weekly meetings to review incremental progress towards completion of the PFDs.

![](/api/attachments/Y93439UX/fulltext/images/20ae8702743110de7f533c9a6245ea795960294e9fe3f3af5f4f6bfee0c4087d.jpg)  
Fig. 3. The “Design Factory” approach.

## 3.2 Phase 2: Developing Product Definitions

The conceptual design for each segment was then made. This involved several steps performed for each PFD, once it was baselined. A majority of the phase two design that was visible to the users dealt with “outside-in” design; this included the identification of each process that was to be automated and the construction of a cross reference or traceability matrix for the appropriate PFD description. The purpose of this matrix was to show the users that each process identified in the PFD was being integrated into the design phase. In addition, visual representations of the displays and reports were developed on paper or simulated (on a CRT) for user acceptance. During this step, the source for every data element was identified. If the data came from the database directly, that was noted. If the data element appearing on a screen was derived or computed, its algorithm was identified and referenced. This screen simulation process proved that every data element that was to be used in a screen or report was identified early and helped reduce the possibility of omission at this stage in the design process.

While the majority of users were concentrating on the “outside-in” design, a logical data model was created for that segment, and data elements were assigned to their proper tables. This database design was performed by a small group of database specialists. These local segment data models were integrated to form the global RDB logical data model, as previously discussed. It is through the integration of these local models that the real integration activities of RDB took place. Most of this was transparent to the users, since they were primarily concerned with the automation of their particular functions.

The process used to integrate local data models into global models is summarized in Fig. 4. The principle tools used to accomplish the integration were Data Designer and the ADR DATACOM Data Element Dictionary System [7,9]. The basic process can best be described as bottom up incremental normalization. Local information models were developed by individual product teams which were staffed with functional specialists and representatives from the database administration group. As these teams completed the initial design of their local information models, the results were transferred from Data Designer to the Data Element Dictionary. During this process, any conflicts or duplication with data elements produced by other local information modeling teams were resolved by the database administrator's office working in conjunction with the product teams. Since each of the local information models is itself a significant design undertaking, the process actually occurred in a step-wise fashion with some teams completing local information models ahead of others. Unless a global design problem was induced by conflicting needs between local information modeling groups, the general rule was that the first local model completed would dominate the global design process.

![](/api/attachments/Y93439UX/fulltext/images/7dc715a9c19996fd80fd4b08c4e32a67ed8bffbd7aaa9cd9c1ec62358a4f11b2.jpg)  
Fig. 4. Database integration process.

Finally, the software unit structure, program hierarchy, and job control procedures were identified. The steps that were used are depicted in Fig. 5.

## 3.3 Phase 3: Prototyping the Design

During the product definition phase, horizontal paper prototypes, or blueprints, were put together to show the users' visual representations of the entire segment. The intent of these blueprints was to capture the essence of the design and facilitate communication with the users without the bulk verbiage that it takes to provide traditional written specifications. By using the “design factory” mentioned earlier, these paper prototypes were relatively inexpensive to generate and change. No design progressed until the blueprints were baselined. It should be emphasized that developing the blueprints did not require “extra” time in the development process. Each of the displays used in the blueprints found their way into the system specifications and helped the users in their review.

## 3.4 Phase 4: Coding, Testing, and Installing the Product

The fourth phase involved the population of the database, coding the application software, testing the product, and installing it for use. Although none of these activities was trivial, no further discussion of these topics is included here. It should be pointed out, however, that over 1.3 million lines of code, of the projected 3.7 million, have been developed, tested, and implemented to date. The current size of the operational database is over 40 gigabytes. In addition, over 4500 users have been trained on the operational components of the system.

![](/api/attachments/Y93439UX/fulltext/images/b3b0024157d0dd3839c7c18eeaa05db44070459f64653a5405e18d234fa6ccb0.jpg)  
Fig. 5. Key components of the blueprints.

## 4. The Use of Blueprints in the RDB Development

The illustrations used to describe the blueprint content are selected from one of the major RDB segments. As their name implies, blueprints consist of blue ink printed on off-white paper, which allow for easy visual review. When completed, they were stapled and bound in the same manner as construction blueprints. The individual pages of the blueprints were reviewed and baselined at a weekly meeting during the week that they were produced. In this manner, progress toward the overall design could be assessed and monitored incrementally.

All blueprints have the same format. They contain: a traceability matrix, screen hierarchy and menu navigation charts, screen snapshots, report snapshots, program hierarchy charts, batch summary charts, job sequencing charts, batch job snapshots, structure charts, global and local logical data models, and normalized data tables for that particular segment.

The major purpose of the traceability matrix is to show the user where each function to be automated will appear in the new system design. It assigns a design number and name to each function that is to be automated. The matrix also identifies the PFD paragraph number which describes the process. The matrix also identifies the screen number that will be used to accomplish a particular function. An example of this matrix is shown in Fig. 6.

The blueprint also identifies the screen hierarchy and navigation paths to various screens which accomplish the functions identified in the traceability matrix. In the RDB design, users have access only to those screens necessary to accomplish their specific functions. As a result, the RDB has put together several user profiles which identify those screens that each user group can access. These profiles are coded into the system and may be used to control user access to designated functions. The profiles can be easily changed by controlling the screens that each user or user group can access. This aspect of RDB allows accommodation to organizational change. A screen hierarchy chart is shown in Fig. 7. Specific user profiles are shown by indicating which of the total number of screens for a given segment can be accessed by a given profile.

<table><tr><td>PFD NUMBER</td><td>PFD PROCESS NAME/SUBPROCESS</td><td>DESIGN</td><td>DESIGN NAME</td><td>SCREEN NUMBER</td></tr><tr><td rowspan="9">3.1.1.1</td><td>ON-LINE MAINTAIN PHYSICAL RELATIONSHIP DATA</td><td></td><td></td><td></td></tr><tr><td>NHA FILE MAINTENANCE</td><td>S1.1.7</td><td>F/M NHA</td><td>SS00009</td></tr><tr><td>NHA DELETE</td><td>S1.1.7</td><td>F/M NHA</td><td>SS00009</td></tr><tr><td></td><td>S1.1.11</td><td>DELETE NHA CONFIRMATION</td><td>SS00056</td></tr><tr><td></td><td>S1.1.12</td><td>DELETE NHA INFORMATION</td><td>SS00057</td></tr><tr><td></td><td>B46</td><td>PROCESS NHA DELETION</td><td></td></tr><tr><td>COMPONENT FILE MAINTENANCE</td><td>S1.1.6</td><td>F/M INDENTURE</td><td>SS00010</td></tr><tr><td>COMPONENT DELETE</td><td>S1.1.6</td><td>F/M INDENTURE</td><td>SS00010</td></tr><tr><td></td><td>B1.1.10</td><td>DELETE COMPONENT CONFIRMATION</td><td>SS00055</td></tr><tr><td rowspan="4">3.1.1.2</td><td>ON-LINE MAINTAIN PROGRAM SELECTION DATA</td><td></td><td></td><td></td></tr><tr><td>PROGRAM SELECTION</td><td>S1.1.5</td><td>F/M PROGRAM SELECTION</td><td>SS00008</td></tr><tr><td>GLOBAL CHANGE OIM</td><td>S1.1.9</td><td>CHANGE OF PROGRAM SELECT CODE</td><td>SS00051</td></tr><tr><td>ERRC CODE CHANGE PROCESSING</td><td>B21</td><td>PROCESS STOCK LIST CHANGES</td><td></td></tr><tr><td rowspan="7">3.1.1.3</td><td>ON-LINE MAINTAIN STANDARD DESIGNATOR DATA</td><td></td><td></td><td></td></tr><tr><td>STANDARD DESIGNATORS</td><td>S1.2.8</td><td>F/M STANDARD PROGRAM DESIGNATOR</td><td>SS00007</td></tr><tr><td></td><td>B44</td><td>PROCESS SPD DELETES</td><td></td></tr><tr><td>COPY/ADD STANDARD DESIGNATORS</td><td>S1.2.9</td><td>COPY/ADD PROGRAM SELECTION</td><td>SS00011</td></tr><tr><td>REDESIGNATE STANDARD PROGRAM DESIGNATORS</td><td>S1.2.10</td><td>REDESIGNATE A SPD</td><td>SS00012</td></tr><tr><td></td><td>B45</td><td>PROCESS REDESIGNATIONS</td><td></td></tr><tr><td>EQUIPMENT SEGMENT INTERFACE</td><td colspan="2">NOT IMPLEMENTED THIS RELEASE</td><td></td></tr><tr><td>3.1.1.4</td><td>ON-LINE MAINTAIN PRODUCTION HISTORY</td><td>S1.1.3</td><td>F/M PRODUCTION HISTORY</td><td>SS00006</td></tr></table>

Fig. 6. PFD traceability matrix.

![](/api/attachments/Y93439UX/fulltext/images/78e71662f137a4680ce8ba141054d9ec83a640cfbc550f0fd268a44f0752576e.jpg)  
Fig. 7. Screen hierarchy chart.

The blueprint also shows a copy of the global logical data model and indicates the portions used in the segment of interest. An example is shown in Fig. 8.

The blueprints also contain screen snapshots; an example is shown in Fig. 9. The screen snapshots show a “mock-up” of the proposed screen; these are produced for user review (and modification, if necessary) before coding is started to provide the screen. The mock-up shows examples of the positioning of data on the screen as well as its contents. Every screen proposed for a given segment was reviewed, and each screen was identified by the number in the traceability matrix.

In addition to the screen layout, the screen snapshot showed the navigation path to access the screen. The snapshot also showed the portion of the logical data model that held the data being used in the screen.

A screen matrix on the snapshot showed the data element dictionary name associated with every field name on the screen. It also showed the source of the data. If the data element was derived (i.e. not input directly from the user or obtained directly from the database), the algorithm used to calculate the element was identified in the matrix. If the screen was used for file maintenance actions, access methods and edit criteria were identified.

![](/api/attachments/Y93439UX/fulltext/images/313c34917c195690e54feca1f08a053f9eb110a7a6e5a3f7df5e9d3f0c3eb5e0.jpg)  
Fig. 8. Global logical model (RID, C017, applications).

RECORD NAME: FIELD NAME

![](/api/attachments/Y93439UX/fulltext/images/4b3b8cdba8a9017dde46e473b2f8aeea969cfebd1cdaad630bb688b544502717.jpg)  
Fig. 9. Screen snapshots.

RECORD NAME: FIELD NAME

![](/api/attachments/Y93439UX/fulltext/images/b567b65fbf72a53287f85d0b9306a81674e61fbc8536ccf83a90dfc6fed6fcc7.jpg)  
Fig. 10. Report snapshots.

![](/api/attachments/Y93439UX/fulltext/images/50968dc54fa79479125138414d824b696847ce64cdd9ef13e2d32e823499dc14.jpg)  
Fig. 11. On-line program.

![](/api/attachments/Y93439UX/fulltext/images/0fb6b5cb3505dd8e54b9549cca0723363491c0a01830152c1cf6b1445c773733.jpg)  
Fig. 12. File maintenance indenture/applications.

<table><tr><td>BATCH JOB NAMES-MISCELLANEOUS</td><td>DAILY</td><td>WEEKLY</td><td>MONTHLY</td><td>QUARTERLY</td><td>ANNUALLY</td><td>AS REQ MANUALLY INVOKED</td><td>AS REQ ON-LINE INVOKED</td></tr><tr><td>PROCESS STOCK LIST CHANGES (B21)</td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PURGE RDB PRODUCTION/CONSUMPTION (B5)</td><td></td><td></td><td></td><td>●</td><td></td><td></td><td></td></tr><tr><td>PURGE SUSPENDED CONSUMPTION HISTORY (B6)</td><td></td><td></td><td></td><td>●</td><td></td><td></td><td></td></tr><tr><td>DETERMINE ITEMS TO DERIVE (B30)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td></tr><tr><td>DERIVE APPLICATION MIEC (B28)</td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DERIEVE ITEM MIEC (B29)</td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DERIVE ITEM DISPOSAL DEFERRED CODE (B32)</td><td>●</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SHIFT CONTROL PROCESSING (B11)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td></tr><tr><td>INITIAL LOAD (B0)</td><td></td><td></td><td></td><td></td><td></td><td>ONE TIME</td><td></td></tr><tr><td>PROCESS SPD DELETE (B44)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td></tr><tr><td>PROCESS REDESIGNATION (B45)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td></tr><tr><td>PROCESS NHA DELETE (B46)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>●</td></tr><tr><td>RETAIN HISTORICAL DATA (B23)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 13. Batch summary.

![](/api/attachments/Y93439UX/fulltext/images/e10b7c4a75a54b0df28e2e60380e2f0321fb45e229d3888e5758d4f5394e2c6c.jpg)  
Fig. 14. Batch job name programs (B13).

![](/api/attachments/Y93439UX/fulltext/images/5f6acd41d344844dbe0727257272d6bcb64eca8f9f2e452cffa3b6afb8f67287.jpg)  
Fig. 15. Job sequencing charts.

The blueprints also included report snapshots for information that could be printed on specified media. As shown in Fig. 10, the report snapshot is very similar to the screen snapshot.

Also included in the blueprints are displays of overview (Fig. 11) and detailed (Fig. 12) on-line program hierarchy charts. Similar displays are included for batch processing activities in the blueprints (Figs. 13 and 14); the appropriate job sequencing charts, as shown in Fig. 15, were also provided.

## 5. Summary: The RDB Blueprint Experience

The importance of applying correct design methodologies cannot be overemphasized, especially in an extremely complex and large information system like RDB. Sometimes the size makes it difficult to communicate the basic principles which guide systems development. To avoid costly mistakes and those design errors that result from poor communications between developers and users, blueprints were used in the RDB development. In the time since the RDB implemented the blueprint idea the cost of associated baseline change requests has dropped dramatically.

The user can plainly see “where RDB is going and how it will get there”. A large part of the success will be directly attributable to the visual constructs for the future RDB system and the way that these were stated and modified before code was built.

It is absolutely necessary to keep users involved in the MIS development sequence. In the RDB program, the use of blueprints aided the user in reviewing the system and insured they would be satisfied with the results once they could appreciate what they were going to get. Without the use of blueprints, building a system as large and complex as RDB in an incremental fashion would have been much more difficult and time consuming.

## References

[1] The Air Force Requirements Data Bank Master Functional Description (MFD), Revision B, BDM Corporation, December 12, 1986.

[2] The Air Force Requirements Data Bank (RDB) Economic Analysis, HQ AFLC/LO(RDB), Wright-Patterson AFB, Ohio, October 29, 1982.

[3] Martin, James: Managing The Database Environment, Prentice-Hall, Englewood Cliffs, New Jersey, 1987.

[4] Martin, James: Stategic Data-Planning Methodologies, Prentice-Hall, Englewood Cliffs, New Jersey, 1982.

[5] Howe, D.R.: Data Analysis for Database Design, Edward Arnold, London, Great Britain, 1985.

[6] Inmon, W.H.: Information Systems Architecture, Prentice-Hall, Englewood Cliffs, New Jersey, 1986.

[7] “ADR DATACOM/DB and the ADR/DATACOM Environment Video (DB401)”, Applied Data Research Corp., Princeton N.J., Copyright 1986.

[8] Excelerator User Guide, Index Technology Corp., Cambridge, Mass., Copyright 1984.

[9] Data Designer User Guide, Database Desing Inc., Ann Arbor, Mich., Copyright 1985.

[10] Customizer User Guide, Index Technology Corp., Cambridge, Mass., Copyright 1984.

[11] Samna Word IV User Manual, The Samna Corporation, Atlanta, Ga., Copyright 1986.

[12] R:Base 5000 User Manual, Microrim Corporation, Redman, Washington, Copyright 1986.

[13] Ventura Desktop Publishing Series Reference Guide, Xerox Corporation, Lewisville, Texas, Copyright Xerox Corp. 1986, 1987, Ventura Software, Inc., 1986, 1987.
