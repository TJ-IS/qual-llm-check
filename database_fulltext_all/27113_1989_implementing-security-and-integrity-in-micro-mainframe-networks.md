---
otero_id: 27113
otero_key: "8XFUXBRB"
title: "Implementing Security and Integrity in Micro-Mainframe Networks"
authors: "J.L. Boockholdt"
year: "1989"
journal: "MIS Quarterly"
doi: "10.2307/248920"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Implementing Security and Integrity in Micro-Mainframe Networks
Author(s): J. L. Boockholdt

Source: MIS Quarterly, Vol. 13, No. 2 (Jun., 1989), pp. 135-144

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/248920

Accessed: 09/05/2014 18:59

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Implementing Security and Integrity in Micro-Mainframe Networks

By: J.L. Boockholdt
Department of Accountancy & Taxation
College of Business Administration
University of Houston
Houston, Texas 77204-6283

## Abstract

This article examines the impact on computer security and data integrity of linking personal computers in user departments with the corporate mainframe computer. It describes the results of a survey of experts in computer security and integrity. In this survey, participants identified those security and integrity controls that become critical because of the micro-mainframe link. The risks associated with three ways of implementing the link are evaluated and procedures for controlling these risks are suggested.

Keywords: Data security, data integrity, micro-computers, personal computers, internal controls

ACM Categories: H.2.0, C.5.3

## Introduction

As MIS users have increasingly incorporated personal computers into their day-to-day activities, they have expanded their expectations of these systems. Many now recognize the value of linking personal computers with a mainframe computer in order to access the organization's database. This creates a micro-mainframe network (Nestor, 1989).

As user requests for micro-mainframe networks increase, MIS managers must address the issues raised concerning data security and integrity. Some organizations have begun to implement appropriate procedures over their micro-mainframe networks that have been described in professional literature (Cook, 1988; DiPerna, 1985; Lehman, 1986; Leitheiser and Wetherbe, 1986; Mills and Viggiano, 1986; Opliger, 1985; Parker 1988; Schultz, 1985; Schultz and Redding, 1985; Skinner, 1986). However, no systematic study has examined the effects of this new technology on computer system security and data integrity.

This article describes a survey undertaken to address these concerns. It attempts to answer three related questions. First, what methods of achieving data security and integrity are critical when a personal computer replaces a terminal in a network? Second, what forms of micromainframe network create the greatest threats to data security and integrity? Finally, what procedures are available for implementing the critical methods?

## The Survey

In this study, 85 Certified Information Systems Auditors were surveyed about their views on security and integrity in micro-mainframe networks. The Certified Information Systems Auditor (CISA) designation is awarded after an individual attains a minimum amount of related work experience and passes the CISA examination. This exam was established by the EDP Auditors Foundation to measure knowledge in auditing computer-based information systems. Approximately 58 percent of the questions on the examination concern computer controls, data integrity, and computer security (EDP Auditors Foundation, 1981). Thus, all participants in the survey had demonstrated an expertise in these subjects.

The questionnaire was developed from the security and integrity guidelines described in the most recent edition of Control Objectives, published by the EDP Auditors Foundation (Li, 1983). Thirty-one of these consisted of those guidelines that, in my opinion, are likely to be affected by the link's existence. One additional guideline, which should not be affected by the link, was included as a validator. These control objectives and guidelines are listed in the Appendix.

Respondents were asked to evaluate the criticality of each of the 32 guidelines in four different cases. Case A consisted of a typical teleprocessing environment, with a host mainframe computer connected to multiple local and remote terminals. It was used as a reference for comparison to the other cases involving micromainframe links. In Case B, the respondents were asked to assume that each terminal in Case A was replaced by a personal computer (PC) with access privileges identical to the terminal's. In Case C, each terminal was replaced by a PC that provided its user with file download, but not upload, capability. In Case D, PCs replaced terminals, and the links provided both download and upload capability. Table 1 summarizes these four cases.

Respondents evaluated the criticality of 32 guidelines in each of the four cases. This produced a relatively long, although simple, questionnaire consisting of 128 evaluations. Statistical techniques were used to analyze these responses and identify those guidelines that respondents considered critical in micro-mainframe networks. $^{1}$

## Results

Table 2 summarizes the results of the statistical analysis to determine the critical security and integrity features in a micro-mainframe network. $^{2}$

Eighty-five useful responses were obtained from a randomly chosen sample of 414 CISAs. These were analyzed using multivariate statistical methods and the F statistic. Significance was determined at the $\alpha = .05$ level.

Of the 32 features, or guidelines, in the survey, 20 had statistically significant differences in criticality. In other words, these features were more critical in a micro-mainframe-link environment than in a teleprocessing environment using only terminals. The Appendix provides a more thorough description of these guidelines.

## Critical guidelines

Variable number 1, which was Control Guideline N in the EDPAF study (Li, 1983), states that adequate resources should be planned and managed. There is no reason a priori to expect resource planning and management to be more critical in a micro-mainframe network than in a teleprocessing one. This guideline was included on the questionnaire as a validator; if a statistically significant difference between environments was found on it, one might question the validity of all the results of the survey. Fortunately, the survey results indicated that no such difference exists. The rest of this section discusses the critical guidelines that have been categorized into four objectives (see Table 2): effective management of resources, access and physical security, backup and recovery plans, and control of PCs in database systems.

The study identified three critical guidelines associated with the management of resources. CISAs felt that periodic equipment maintenance, inventory logs for computer files, and standardized file identification methods were each more critical in a micro-mainframe network than in a teleprocessing one. Equipment maintenance becomes important because PCs, with memory and disk drives, are more complex than terminals. In a micro-mainframe network, files are stored at user locations as well as on the mainframe. Thus, methods of identifying and controlling these files become important.

Eight access and physical security guidelines were identified as more critical when PCs are used. Participants perhaps concluded that a PC's programmability enables its user to circumvent security methods that might be sufficient in a teleprocessing network. Therefore, more controls would be needed to prevent physical access to equipment or to limit access to data on the mainframe.

Another objective concerns backup and recovery plans. The study identified three associated guidelines as critical in a micro-mainframe network. Backup plans and procedures are critical because users maintain their own files at the PC site. These files may not be subject to the routine backup procedures employed on a mainframe, so a backup plan must prescribe appropriate procedures for the PC. A periodic test of backup plans can determine if users are implementing the plan.

Table 1. Network Environments Used for Evaluation

<table><tr><td>Case A:</td><td>A host mainframe is linked to intelligent terminals using standard teleprocessing software such as CICS.</td></tr><tr><td>Case B:</td><td>A host mainframe is linked to personal computers using a software link. The link provides online access, with access privileges identical to the terminal that the PC replaced.</td></tr><tr><td>Case C:</td><td>A host mainframe is linked to personal computers using a software link that provides download capability only. That is, files may be transferred from the mainframe to a PC, but may not be transferred from the PC to the mainframe.</td></tr><tr><td>Case D:</td><td>A host mainframe is linked to personal computers using a software link that provides both download and upload capability. Files may be transferred from the mainframe to a PC, changed by the PC, and transferred back to the mainframe.</td></tr></table>

Other guidelines evaluated in the study provide integrity and security in database supported systems. Respondents identified all five related guidelines as critical in a micro-mainframe network. In these networks, users access mainframe data and use it for applications on the PC. Thus, procedures for data changes and the maintenance of a data dictionary should be written and communicated clearly to all users. When mainframe data are used at a PC, they can be printed or copied to a floppy disk. Controls over access to sensitive data at the mainframe level thus become more important than when the user employs a terminal. Procedures for database recovery and data integrity are more critical because a PC user may make changes to a mainframe database that are not documented by an audit trail on the mainframe.

Table 2. Critical Security and Integrity Guidelines in a Micro-Mainframe Network

<table><tr><td>Guideline Number</td><td>Guideline Description</td></tr><tr><td colspan="2">Control Objective O: Effectively Manage Resources</td></tr><tr><td>03</td><td>Periodic equipment maintenance</td></tr><tr><td>05</td><td>Inventory logs for all computer files</td></tr><tr><td>06</td><td>Standardized file identification</td></tr><tr><td colspan="2">Control Objective Q: Access and Physical Security</td></tr><tr><td>08</td><td>Protect against unauthorized access</td></tr><tr><td>09</td><td>Assign responsibility for access and security</td></tr><tr><td>11</td><td>Control access to terminals or PCs</td></tr><tr><td>12</td><td>Record and review terminal or PC access data</td></tr><tr><td>14</td><td>Security control based on classification of data</td></tr><tr><td>15</td><td>Do not publicly identify IS facilities</td></tr><tr><td>16</td><td>Protect files from destruction &amp; unauthorized use</td></tr><tr><td>18</td><td>Train mainframe operators in security procedures</td></tr><tr><td>19</td><td>Periodically test security plans</td></tr><tr><td colspan="2">Control Objective R: Backup and Recovery Plans</td></tr><tr><td>25</td><td>Backup CPU and other hardware</td></tr><tr><td>26</td><td>Backup procedures to minimize recovery requirements</td></tr><tr><td>27</td><td>Periodic test of the backup plan</td></tr><tr><td colspan="2">Control Objective W: Control in database systems</td></tr><tr><td>28</td><td>Consideration of integrity &amp; security of shared data</td></tr><tr><td>29</td><td>Written procedures for data dictionary changes</td></tr><tr><td>30</td><td>Access to sensitive data, concurrent access controls</td></tr><tr><td>31</td><td>Sufficient written data recovery procedures</td></tr><tr><td>32</td><td>Adequate procedures for database integrity</td></tr></table>

Statistical analysis identified those teleprocessing security and integrity features that are most critical in a micro-mainframe network. However, features in certain forms of the network are likely to be more critical than in other forms. In the survey, respondents were asked to evaluate three of them. Further analysis then investigated the effect of the form of network on the criticality of those control objectives and guidelines.

## Form of micro-mainframe network

The questionnaire asked respondents to evaluate security and integrity features in networks using three different micro-mainframe links. These were identified as Cases B, C, and D. Statistical methods then compared the criticality of features in these networks to the same ones in Case A, a teleprocessing system using only terminals. $^{3}$ Table 3 summarizes the results of these comparisons. It identifies the forms of micro-mainframe networks that are most vulnerable.

## Record or Field Level Access

Case B contains PCs with access privileges identical to those of the terminals in the teleprocessing system. In most systems, this provides access at the record or field level to data stored on the mainframe. Comparing Case B with Case A shows whether network vulnerability is increased simply because of the existence at user locations of the greater memory, local storage, and printing capability of the PC.

Table 3 shows that three guidelines are more critical in a micro-mainframe system providing record or field level access. These are the variables numbered 3, 12, and 25 in the Appendix. Because PCs have more mechanical parts than terminals, regular maintenance and backup hardware are more important. The respondents also felt that recording and reviewing terminal (or PC) access records on the mainframe is more critical in this form of network. Perhaps they were suggesting that, because of the PCs' greater capability for circumventing mainframe security features, more reliance should be placed on detecting unauthorized access after it has occurred than on preventing unauthorized access.

## File Download Capability

Cases C and D describe networks providing access to entire mainframe data files. The network in Case C provides only download capability — the ability to transfer files from the mainframe to the PC. In Case D, the PC user has both download and upload capability; that is, files can be transferred from mainframe to PC, altered at the PC, and then transferred back to the mainframe.

The guidelines considered more critical in the download only case are: restricted access to terminals, security classifications for data, scheduled hours of operation for terminals connected to sensitive data, and avoiding public disclosure of the location of computer facilities. Thus, the respondents considered this form of network more vulnerable than the teleprocessing network because of the ability of PCs to download greater quantities of data.

## File Download and Upload

The most vulnerable case is Case D, in which data download and upload capabilities are provided. Table 3 shows that respondents identified all but two of the guidelines as critical when the micro-mainframe network provides both download and upload capability. Critical features include all the access and physical security guidelines and all those listed for database systems. Respondents also felt that file controls and backup procedures are important in this kind of network.

The respondents' concern with data integrity appears justified. Using this form of link, a PC user can download a data file from a mainframe, make changes to all or part of the file, and replace the mainframe file with the changed one. This procedure may circumvent any validation procedures that exist in the mainframe-based application that processes the file. Two guidelines identified as critical — file identification (No. 6)

Table 3. Summary of Critical Guidelines and Forms of PC Access in a Micro-Mainframe Network

<table><tr><td>Guideline Number</td><td>Description of Critical Guideline</td><td>Record/Field Access</td><td>File Download</td><td>File Download and Upload</td></tr><tr><td colspan="5">Control Objective O: Effectively Manage Resources</td></tr><tr><td>3</td><td>Periodic equipment maintenance</td><td>X</td><td></td><td></td></tr><tr><td>5</td><td>Inventory logs for all computer files</td><td></td><td></td><td>X</td></tr><tr><td>6</td><td>Standardized file identification</td><td></td><td></td><td>X</td></tr><tr><td colspan="5">Control Objective Q: Access and Physical Security</td></tr><tr><td>8</td><td>Protect against unauthorized access</td><td></td><td></td><td>X</td></tr><tr><td>9</td><td>Assign responsibility for access and security</td><td></td><td></td><td>X</td></tr><tr><td>11</td><td>Control access to terminals or PCs</td><td></td><td>X</td><td>X</td></tr><tr><td>12</td><td>Record and review terminal or PC access data</td><td>X</td><td>X</td><td>X</td></tr><tr><td>14</td><td>Security control based on classification of data</td><td></td><td>X</td><td>X</td></tr><tr><td>15</td><td>Do not publicly identify IS facilities</td><td></td><td>X</td><td>X</td></tr><tr><td>16</td><td>Protect files from destruction &amp; unauthorized use</td><td></td><td></td><td>X</td></tr><tr><td>18</td><td>Train mainframe operators in security procedures</td><td></td><td></td><td>X</td></tr><tr><td>19</td><td>Periodically test security plans</td><td></td><td></td><td>X</td></tr><tr><td colspan="5">Control Objective R: Backup and Recovery Plans</td></tr><tr><td>25</td><td>Backup CPU and other hardware</td><td>X</td><td></td><td></td></tr><tr><td>26</td><td>Backup procedures to minimize recovery requirements</td><td></td><td></td><td>X</td></tr><tr><td>27</td><td>Periodic test of the backup plan</td><td></td><td></td><td>X</td></tr><tr><td colspan="5">Control Objective W: Control in Database Systems</td></tr><tr><td>28</td><td>Consideration of integrity &amp; security of shared data</td><td></td><td></td><td>X</td></tr><tr><td>29</td><td>Written procedures for data dictionary changes</td><td></td><td></td><td>X</td></tr><tr><td>30</td><td>Access to sensitive data, concurrent access</td><td></td><td></td><td>X</td></tr><tr><td>31</td><td>Sufficient written data recovery procedures</td><td></td><td></td><td>X</td></tr><tr><td>32</td><td>Adequate procedures for database integrity</td><td></td><td></td><td>X</td></tr></table>

and file inventory and logs (No. 5) — may be useful in detecting this process after it occurs.

Of the three micro-mainframe networks evaluated, respondents considered Case B (record and field level access) as the least vulnerable and Case D (data download and upload) as the most vulnerable. These results were expected. They demonstrate to MIS managers those features that are most critical in a specific form of network. The results also show the importance of knowing procedures for implementation. MIS managers adopt procedures that are cost-effective for the organization and its form of network.

## Implementation

This study identifies security and integrity guidelines for teleprocessing systems that are critical when PCs are used. This section of the article provides guidance concerning how to implement these guidelines. As discussed previously, they have been categorized in Tables 2 and 3 according to four objectives. They are: effective management of resources, access and physical security, backup and recovery plans, and control of PCs in database systems.

## Effective management of resources

The survey identified several critical practices associated with the effective management of resources. These include standardized file identification, an inventory of files, scheduled periodic maintenance, a smooth production schedule, input/output controls, reasonable chargeout rates, and safe storage for data files.

## Risks

Effective management of a network that provides both file download and file upload is especially important because of risks introduced by file upload capability. Changes can be made to the file at the PC level, producing data on the mainframe that are incorrect or subject to misinterpretation. For example, a clerk can create a data file at a PC and upload it to the mainframe without its undergoing adequate validation. Or a manager may download a file for analysis, make any changes needed for his or her purpose, and then upload the file for later use. Another employee may produce reports from the file without understanding the assumptions made in the analysis.

## Establish Policies

Appropriate management policies can substantially reduce the risks of file uploading. All production data files stored on a mainframe should go through a validation program on the mainframe, whether the data originate from a mainframe application or from a PC. PC users may be allowed to store PC files on the mainframe, but these should never be used as inputs to production programs. No report should ever be produced from data derived from a non-mainframe source. If all data are validated when uploaded and then downloaded only when needed, no data used in a report are ever more than one generation removed from validated data.

An alternative policy is to mark all mainframe data with the date and time of their creation. Any report produced on a micro must show this date and time or identify any external information sources used. If this information is missing from a report, a reader is alerted to the possibility of corrupted data.

## Access and physical security

Other objectives in teleprocessing systems are to limit access to computer resources and to provide physical security against unauthorized use, damage, loss, or modification. Survey respondents identified several practices for these objectives that were critical in PC networks. They included designating a security manager, classifying security for data, limiting and logging access to PCs, and protecting computer files and facilities.

## Data Classifications

All PC and mainframe data files should be categorized by security classification, and different protection policies should be implemented for each classification. In many organizations, the use of two data security classifications is adequate: non-critical and critical. Others may establish a third for sensitive data.

Non-critical data include memos, analyses, and newsletters for which neither security nor integrity are a major concern. Critical data are the records that are essential to the operations of the organization. They include accounting, statistical, and inventory data. The major concern with critical data is preserving their integrity. Sensitive data includes personnel salaries, private personal data, and proprietary information for which very limited access is desired. Because it is subject to theft, controls over sensitive data should provide both integrity and security.

## Controlled Access

In order to implement any security classification method, an organization must identify individuals who have a need to access each data set. Employees should justify their requests for upload or download capability in writing, and this request should be approved by management. Then procedures should be put in place to restrict access to only those individuals.

For example, user profiles, in the form of passwords and user ids, are stored on the mainframe. These profiles specify which parts of the mainframe database are accessible to each PC user and are maintained by the security manager.

One respondent to the survey stated that, in many organizations, application of security on an individual basis creates an undesirable amount of overhead. This has led these organizations to broaden access categories to include heterogeneous groups rather than individuals. Such a compromise, although easier to implement, increases the risks to data security and integrity.

Survey participants felt that access to terminals or PCs should be controlled, and those connected to sensitive data should have specifically scheduled hours of operation. One respondent suggested that restricting physical access to PCs is not practical in a micro-mainframe network.

These physical limits must be replaced by individual user profiles, accompanied by preprogrammed days and hours of authorized mainframe access. In this way, the PCs are functional at all times. The mainframe is accessible to individuals only in their predetermined periods and modes of operation.

## Protect Files

Controlled access should be accompanied by routine logging and monitoring of attempts to gain unauthorized access to files. The mainframe operating system should log any attempt by an unauthorized person to access data files, execute sensitive programs, or access system utilities that enable the user to copy, modify, or access files. The security manager should investigate all such attempts.

File protection at the mainframe level is implemented with appropriate data security software. At the PC level, it is dependent on user training and discipline. More restrictive protection policies should be established for sensitive data. For example, sensitive PC files can be stored only on specially colored floppy disks and locked up when not in use. These files should always be encrypted before storing them on a mainframe or a PC hard disk, and preferably, a removable hard disk should be used.

## Protect Facilities

Survey participants indicated that the locations of information system facilities should not be identified publicly. However, most organizations have PCs located throughout the organization. When this is true, the location of those PCs linked to the mainframe should not be publicly disclosed. Furthermore, non-user employees in the same work area should not know the access privileges of any linked PC. This limits the ability of an unauthorized person to use the PC to gain unauthorized access to the mainframe. PC keyboards should be equipped with locking switches to prevent their use when unattended.

## Backup and recovery plans

The survey identified three critical guidelines associated with file backup and recovery plans. They concerned backup hardware, backup procedures, and a periodic test of the backup plan.

## Backup Hardware

A backup plan should provide for backup CPU and other hardware resources. In a teleprocessing environment, this is frequently provided by an identical mainframe at a different location. In a micro-mainframe network, backup hardware is necessary for PCs as well. The relatively low cost of a PC enables an organization to maintain spares for use as replacements. To maintain software compatibility, spares should be identical to those PCs in daily use. If the technical expertise is available, spare components such as motherboards, power supplies, and hard disks can be maintained.

One respondent to the survey stated that having available “hot recovery” facilities, which allow immediate resumption of vital processing, is the critical form of hardware backup. It is impractical to have on hand facilities to completely restore permanent facilities following their destruction.

## Backup Procedures

Backup procedures that minimize recovery requirements should be established. Procedures should allow a user to easily recover files that have been lost or damaged.

At the PC level, users may lack the training or discipline to employ procedures that are routine on a mainframe. One survey participant stated that most backup and recovery plans focus on disaster at the data center and ignore the potential for disaster at the user site. At the PC level, he suggested, a greater and more costly exposure may exist. An effective recovery plan recognizes the entire data flow, from information origin through processing and data center backup and recovery.

In this regard, the ability to upload files, identified by this study as a source of risk in a network, also provides an advantage. Data files created and used at a PC can be uploaded to the mainframe by communications software. Standard file backup procedures that exist for the mainframe then protect the PC user from lost programs and data.

## Test the Backup Plan

Not only should the backup and recovery plan consider the entire data flow, but it should also be tested periodically to ensure that it functions properly. PC users who have never experienced a major data loss are frequently unaware of the importance of routine backups. They become careless about making them, even when management policy requires them. A periodic test of the backup plan in user departments, perhaps conducted by internal auditors, serves as a reminder.

## Security and integrity in database-supported systems

The study identified five critical topics in dealing with database-supported systems. Three topics (access to sensitive data, database recovery, and database integrity) have already been discussed; the two remaining ones are data dictionary maintenance and concurrent access to data.

## Data Dictionary Maintenance

In a micro-mainframe network, procedures related to data description, data changes, and data dictionary maintenance should be established and stated in writing. When a network allows data file upload, individual PCs may create data sets for processing by a mainframe. The data dictionary designates standard data names and formats required by the application. Written procedures prevent an individual PC user from developing data sets that are incompatible with those of another user. They also prevent one user from making changes that would affect another.

## Concurrent Access

A database-supported system should provide features that address problems created by concurrent access. Such a system can produce conflicting information if one user accesses a data item or file while another is making a change to it.

Concurrent access can be prevented by certain software packages that implement the micro-mainframe link. These packages provide a "check-in check-out" facility that is similar to a record lockout in a teleprocessing system. Whenever a file has been downloaded to a PC, it is designated as checked out. It cannot be accessed by anyone else until it is checked in.

These suggestions provide ways of implementing improved security and data integrity in micro-ainframe networks. However, before attempting to implement them, MIS managers must evaluate the tradeoff between the costs of a feature and the benefits it provides at the managers' own installations. If the benefits are small, or if the likelihood or a security or integrity failure are remote, some features may not be worthwhile. MIS managers must exercise judgement in evaluating them.

## Conclusion

This article describes a survey of persons knowledgeable in computer security and data integrity. The survey was undertaken to summarize their opinions concerning the impact in these areas of the use of PCs in computer networks. Statistical methods were used to identify those features that the survey population considered critical. Three different kinds of micro-mainframe networks were considered.

The study found that few differences exist whenever the PC simply replaces the terminal. In this case, however, a PC can be programmed to bypass mainframe security features. Thus, logging and reviewing attempted file accesses become critical. Because of a PCs mechanical parts, maintenance and hardware backup are also more important.

Whenever the PC is able to download entire files, three additional access and physical security controls become critical. Security classifications for data should be established and different access restrictions implemented for each classification. Locations of PCs with access to a mainframe should not be publicly disclosed, and their access should be restricted by software and user profiles.

The most vulnerable form of a micro-mainframe network allows file transfer both from the mainframe to the PC and also from the PC to the mainframe. The study identified eighteen guidelines that are significantly more critical in a network of this kind. These existed in four areas: effective management of resources, access and physical security, backup and recovery plans, and control in database-supported systems. Methods of implementing these guidelines were suggested.

As more users acquire PCs and as current PC users become more sophisticated in their use, requests from them for a micro-mainframe link will increase. MIS managers cannot afford to implement such a link without first evaluating its impact on computer security and data integrity. This study identifies the security and integrity features that are critical in micro-mainframe networks.

## Acknowledgement

The aid of the EDP Auditors Foundation and the financial support from the University of Houston are gratefully acknowledged.

## References

Cook, M.G. "Unravelling PC Data-Security Confusion," Internal Auditor, December 1988, pp. 49-53.

DiPerna, M. "Auditing a PC — It's Not So Difficult," EDP Auditor (I), 1985, pp. 23-25.

EDP Auditors Foundation. "Certified Information Systems Auditor Study Guide," January 1981, p. 3.

Lehman, J.A. "Microcomputer Use of Mainframe Databases," Journal of Systems Management, January 1986, pp. 18-22.

Leitheiser, R.L. and Wetherbe, J.C. "Approaches to End-User Computing: Service May Spell Success," Journal of Information Systems Management, Winter 1986, pp. 9-14.

Li, D.H. Control Objectives, Control in a Computerized Environment: Objectives, Guide-

lines, and Audit Procedures, EDP Auditors Foundation, Carol Stream, IL, 1983.

Mills, V. and Viggiano, W. "Do You Have to be a Whiz Kid to Audit Data Security?" EDP Auditor (II), 1986, pp. 39-45.

Nestor, J.H. "An Introduction to the Micro-to-Mainframe Connection," Journal of Accounting and EDP, Winter 1989, pp. 4-9.

Opliger, E.B. "Identifying Microcomputer Concerns," EDP Auditor (I), 1985, p. 43.

Parker, R.G. "Microcomputer Security and Control," EDP Auditor (I), 1988, pp. 13-20.

Schultz, N.O. "Microcomputer Control Strategy: An Empirical Study of Its Development," EDP Auditor (II), 1985, p. 5.

Schultz, N.O. and Redding, R.J. "A Survey of Microcomputer Control and Support Policies," EDP Auditor (I), 1985, p. 5.

Skinner, B.F. "Technology: How Is It Changing the CFO's Job?" FE Magazine, May 1986, p. 23.

## About the Author

J.L. Boockholdt is an associate professor in the Department of Accountancy and Taxation, University of Houston. A former systems employee of a major accounting firm, Dr. Boockholdt has earned degrees from Rice University, the University of Pennsylvania, and the University of Alabama. He has authored several articles in professional journals on the subjects of information systems, auditing, and controls of computerized systems.

## Appendix Guidelines Selected for CISA Evaluation

<table><tr><td>Guideline Number</td><td>EDPAF Control4</td><td>Description</td></tr><tr><td>1</td><td>N</td><td>Resources adequate to support the IS objectives should be planned and managed.</td></tr><tr><td>2</td><td>O</td><td>Computer resources in the IS function should be utilized effectively by maintaining a smooth production schedule, providing adequate input/output controls, allowing reasonable chargeout rates, and keeping data files in safe storage.</td></tr><tr><td>3</td><td>O3</td><td>Periodic equipment maintenance should be included in the overall schedule.</td></tr><tr><td>4</td><td>O8</td><td>Responsibilities for data storage should be assigned, and housekeeping procedures to protect library contents should be established.</td></tr><tr><td>5</td><td>O9</td><td>All computer files should be inventoried and controlled by appropriate logs.</td></tr><tr><td>6</td><td>O10</td><td>Computer files should be uniquely identified according to installation standards.</td></tr><tr><td>7</td><td>P</td><td>Systematic procedures should be followed to identify, select, program, implement, maintain, and control systems software acquisition and usage.</td></tr><tr><td>8</td><td>Q</td><td>Access to computer resources should be controlled, and physical security should be provided to protect them against unauthorized use, damage, loss, or modification.</td></tr><tr><td>9</td><td>Q1</td><td>Responsibility for access control and physical security should be assigned. A security manager should be appointed where appropriate.</td></tr><tr><td>10</td><td>Q2</td><td>Access to the mainframe computer room should be restricted to authorized personnel.</td></tr><tr><td>11</td><td>Q4</td><td>Access to terminals should be controlled. Access to terminals connected to sensitive data should have specifically scheduled hours of operation.</td></tr><tr><td>12</td><td>Q5</td><td>Terminal access data should be recorded and reports of terminal activity should be reviewed periodically.</td></tr><tr><td>13</td><td>Q6</td><td>Access to the library should be restricted to authorized personnel.</td></tr><tr><td>14</td><td>Q7</td><td>There should be access security control based on classification of file data.</td></tr><tr><td>15</td><td>Q8</td><td>The location of IS facilities should not be identified publicly.</td></tr><tr><td>16</td><td>Q10</td><td>Computer files should be protected against destruction and unauthorized use.</td></tr><tr><td>17</td><td>Q11</td><td>Security measures should be provided for source documents and forms to ensure privacy, confidentiality, retention, and availability for backup.</td></tr><tr><td>18</td><td>Q12</td><td>Mainframe computer operations personnel should be trained in the application of security controls and procedures for mainframe computer operations.</td></tr><tr><td>19</td><td>Q13</td><td>Security plans should be tested periodically.</td></tr><tr><td>20</td><td>R</td><td>Adequate plans should exist for the backup of critical computer resources and for the recovery of IS services following unanticipated interruptions.</td></tr><tr><td>21</td><td>R1</td><td>There should be a documented backup plan for processing critical jobs in the event of a major hardware or software failure or destruction of mainframe facilities.</td></tr><tr><td>22</td><td>R2</td><td>The backup plan should contain a predetermined priority for application processing.</td></tr><tr><td>23</td><td>R4</td><td>The backup plan should identify critical production and operating systems and the files needed for recovery.</td></tr><tr><td>24</td><td>R5</td><td>The backup plan should contain instructions for re-establishing communications.</td></tr><tr><td>25</td><td>R6</td><td>The backup plan should provide for backup CPU and other hardware resources.</td></tr><tr><td>26</td><td>R8</td><td>Procedures for backup files to minimize recovery requirements should be established.</td></tr><tr><td>27</td><td>R10</td><td>The backup plan should be tested periodically to ensure its workability.</td></tr><tr><td>28</td><td>W</td><td>In the development of database-supported systems, the control, integrity, and security of data shared by multiple users should be considered. All components making up a database environment should be addressed.</td></tr><tr><td>29</td><td>W3</td><td>Procedures related to data description, data changes, and data dictionary maintenance should be established and stated in writing.</td></tr><tr><td>30</td><td>W4</td><td>Procedures related to access to sensitive data and control over concurrent access to data, should be addressed by the DBMS.</td></tr><tr><td>31</td><td>W5</td><td>Recovery procedures for the database should be sufficient to minimize failures and recover the database to the point of failure. Procedures should be written.</td></tr><tr><td>32</td><td>W6</td><td>Procedures should be adequate to ensure the integrity of data maintained within the databases.</td></tr></table>
