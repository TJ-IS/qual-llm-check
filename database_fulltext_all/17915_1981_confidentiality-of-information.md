---
otero_id: 17915
otero_key: "TW7WYC68"
title: "Confidentiality of information"
authors: "H. Roos"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90021-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Confidentiality of Information

H. Roos

Klynveld Kraayenhof & Co., Prinses Irenestraat 5 $^{0}$ , 1077 WV Amsterdam, the Netherlands

The relationship between organization structure, the supporting information systems and the confidentiality issue, defines the end user's responsibility for information control. In a data sharing environment end users must agree upon their mutual responsibility for shared data. The database administrator is the natural authority to control the execution of that agreement. Any departure from strictly preventive control weakens data sharing control.

On-line end user access control by means of security tables may be compromised by the current privileged state machine architecture. Resulting control weaknesses should be compensated by procedural and organizational means.

Keywords: Privacy, security, data sharing control, database administration.

![](/api/attachments/TW7WYC68/fulltext/images/ab26c8e7dae688e25042e427c8f2e6aff95cee087c96d1e503f1e5b03579a933.jpg)

H. Roos is partner of the Dutch auditing firm Klynveld (Krayenhof & Co., which is a founding member firm of KMG (Klynveld Main Goerdeler). After obtaining the Dutch professional qualification of register-accountant (RA) he moved to Spain where he worked in the financial audit field. Confrontation with computerized information systems provoked his interest in EDP and EDP audit. After his return to the Netherlands in 1974 he joined the EDP audit department of the firm and started specialising on audit of databases. In 1980 he became one of the five partners that manage the EDP audit department. His actual research interest is in the audit and control aspects of cooperating operating systems, TP-monitors and DBMS's.

## 1. Confidentiality of Information in a Business Environment

A general principle used in organizing business is to allocate all identifiable tasks to functions and to assign those functions to people. The resulting pattern is a set of functions coupled by hierarchical and lateral relationships. Hierarchical relationships represent delegation of authority, which by nature demands control [1]. Any function processes information during the performance of its tasks. The function is triggered by incoming information and is guided by general instructions describing the duties of the function in the context of the overall business goals. It uses stored information consisting of status-information about objects managed by the function, and event-information already collected, while producing decisions represented as the emission of messages and by the addition to or changes in the stored information belonging to the function. A function is accountable to its superior authority and may itself delegate authority. Incoming messages may consist of event-information, information modifying its instructions, and accounting or control information about the performance of delegated tasks. Outgoing messages will contain similar information, plus decisions on events for transmittal to lateral operations.

Any function that can be held responsible for the performance of the tasks delegated to it obviously has a strong interest in the integrity of all information used in its decision making and reporting processes. This integrity demand implies a need for control over that information which implies the need for control of usage of that information by lateral and by hierarchically superior and subordinate functions. This is the basic requirement for information. Information local to a function may consist of or contain sensitive information that is subject to strict usage rules, e.g., privacy. Control of the latter type of confidentiality presupposes control of the former. This paper deals with the former.

![](/api/attachments/TW7WYC68/fulltext/images/9df841dff64326c012fb7098b85566566fad49c18ca194246153d702c0cf0f3a.jpg)  
Fig. 1. Delegation of Information Processing Control.

Delegation of information processing is a two-step process consisting of the delegation of the construction of programs to a systems development function and delegation of the custodianship of the programs and the stored data and of the program execution to the information processing function (Figure 1). Each step demands control. If the system is an integrated database/data communication system characterized by data sharing among different user functions and by direct data access by users via work stations, need for data sharing control and data access control is obvious.

## 2. Preventive Control of Confidentiality

In a direct data access/data sharing environment, confidentiality of information can easily be compromised. To prevent this, a very clear set of agreements will have to be made about data usage authority. These agreements must be enforced during systems development and operation. This might be done by automating this enforcement using an active integrated Data Dictionary/Data Directory system (DD/DS) complemented by the use of database procedures within the Database Management System (DBMS) both controlled by Database Administration (DBA). Data sharing control and data access control by the DD/DS covers the definitional level, database procedures provide for data occurrence control. Controls may even be carried out down to field type (Figure 2). This type of control can only be realized, however, if the data structure provided during database design is compatible with the confidentiality demanded in the data sharing agreement.

![](/api/attachments/TW7WYC68/fulltext/images/520fedb65e97e6636d2b31543041f5baefda2335acbe8dae78e05f1904b5e289.jpg)  
Fig. 2. Preventive Control of Confidentiality of Data Usage.

If, for performance reasons or due to irreparable design errors, the definitional type of control is not assigned to the DD/DS function and occurrence level controls are not assigned to database procedures, centralized active control by the DBA is sacrificed and must be substituted by control over program construction and usage.

## 3. Confidentiality Control Supplemented by Audits

Controlling program construction means checking whether the program reliably reflects the users' intentions, as described in the user approved functional specifications. The only way to perform this check is by user testing. But the user cannot verify compliance with the data sharing agreement. In order to be able to do that, it is necessary to verify whether all other operational programs behave as agreed with respect to his data.

![](/api/attachments/TW7WYC68/fulltext/images/5582f84d10485a9737e1f292fd2c894e439aa25595765157f0bdb03e65a06717.jpg)  
Fig. 3. Audit Based Control of Confidentiality.

Knowledge about programs might be provided by the DBA, but the user cannot obtain knowledge about input, functions, and output of all those programs. Even if the user has knowledge about all operational programs, it is physically impossible to obtain all necessary knowledge in time to perform those tests.

An integrated fully coordinated test environment containing a complete and up-to-date set of tests covering all applications programs and all data of the shared database, might perhaps provide some evidence about the reliable implementation of the data sharing agreement through the complex of programs and database. And even this statement only holds if testing is executed in a highly disciplined way, in conformity with the state-of-the-art. In practice, it is impossible to comply with those conditions. The inherent weakness of controls, performed primarily on a test basis, must obviously be complemented with confidentiality audits on a regular basis.

## 4. Confidentiality Control on an Audit Basis

One way for a user to check for compliance with the data sharing agreement is by performing an audit of the actual usage of shared data or by delegating this activity to an audit function. Such an audit can only be carried out if a complete audit trail, containing all necessary information is available [2]. The reliability of the audit trail depends on its control. If no preventive data sharing control exists (i.e. one or more programmer views of the database contain access rights to data of more than one user function), the best way to effect data sharing control is via centralized control of the logging facility producing the audit trail (Figure 3). Completeness of logging can be controlled via the DBMS by the DBA. Completeness of each log-record can more easily be tested than the overall functioning of all programs. Production and management of log-files should be integrated in the dp-center organization to prevent inadvertent loss of logging information. It should be stressed, however, that control of confidentiality of information entirely and only based on audits can only uncover violations that have occurred and can never prevent them.

![](/api/attachments/TW7WYC68/fulltext/images/4212b7d2a8c8d493889a3f4b0285cc8b28f6b02e6eaea98d81fd14bfebf7d444.jpg)  
Fig. 4. General Model for Data Sharing Control.

## 5. Theory and Use of Actual Tools

A general model for data sharing control consists of a set of user interfaces, one of which is the security officer's interface: a set of programs, one of which is the security controller, and a set of databases, one of which contains the security tables defining the access and execution rights of all authorized users and their indentifications (Figure 4). Users may comprise humans as well as programs. Mapping of access and execution rights to physical resources should preserve the boundaries of those rights. The physical resources (e.g. workstations and physical data files) sensitive to the security system should be controlled by the security controller.

Actual available tools comprise operating systems and several operating systems extensions (like

DBMS's, TP-monitors, DD/DS's and system monitors). An observable tendency to integrate DD/DS, DBMS, and TP-monitor may result in a tool that provides for integrated and active control of data sharing and data access, comparable to a generalized security controller. The security boundaries of each user (the user's security domain) during actual system execution are preserved however to a limited extent only. The vast majority of actual systems are so-called privileged-state machines. On such machines, a module operating as part of a larger program might access all resources available to the entire program, and those modules running in privileged mode might access all resources available on the machine [3]. A direct consequence of this is that all actually available security additions to an operating system can, in fact, be bypassed using a program running in a privileged mode.

Depending on the degree of flexibility and sophistication of the operating system, this can be a simple or a very complicate operation. Review of a security system should identify which system information might be used to circumvent the security system. This information must be the subject of special security measures of a procedural and organizational nature.

## References

[1] J.G. March and H.A. Simon, Organizations (John Wiley and Sons, Inc. 1958).

[2] L.A. Bjork Jr., Generalized audit trail requirements and concepts for data base applications, IBM Systems Journal (1975), nr. 3, reprint form G321-5012.

[3] T.A. Linden, Operating system structures to support security and reliable software. ACM Computing Surveys, Vol. 8, nr. 4 (December 1976).
