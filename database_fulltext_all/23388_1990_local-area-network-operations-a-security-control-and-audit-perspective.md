---
otero_id: 23388
otero_key: "CZEJQQHM"
title: "Local area network operations: a security, control and audit perspective"
authors: "Rodger Jamieson; Graham Low"
year: "1990"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1990.15"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Local area network operations: a security, control and audit perspective\*

RODGER JAMIESON and GRAHAM LOW

School of Information Systems, University of New South Wales, Australia

Abstract: This paper provides a framework for the review of security and control within a local area network environment. Network operations are subdivided into several functional areas or components for further review. Each component or area is briefly explained and the security risks, issues and concerns highlighted. Controls and security measures are proposed as guidelines to counter these threats. An approach to the audit of each major area of network operations is proposed.

This suggested framework provides guidance to information system security officers, auditors, communications and network administrators, consultants and information systems management for the review of local area network security during network operations.

## Introduction

Information is today one of the most valuable assets in an organization. Its most vital requirement is that it must be communicated to the right decision maker at the right time. Timely communications between decision makers and all strata in an organization are no longer a luxury but a necessity. Three prime instigators providing for effective communication are the personal computer, good software and local area networks (LAN).

Personal computers provide users with the ability to perform many different functions (such as data synthesis) necessary to make effective use of the information. LANs make it possible to communicate information in a fast, reliable and cost-efficient way.

A LAN is defined by Jamieson and Low (1989) as 'a high speed communications path between computers and associated equipment within a limited geographical area that provides resource sharing as well as data and program sharing and exchange'. LANs are typically high speed (Oritz, 1986). The issues associated with network selection and design are discussed by Low (1988a), Low (1988b) and Jamieson and Low (1989).

The LAN environment consists of network personnel and management, hardware such as cable plant, network software, file servers acting as information data stores, and network users. Complexities arising from the introduction of a LAN into an organization may be compounded by distributed data-base management software, network security and encryption software/hardware, varying standards for data communications, and the need to deal with multiple vendors for both network hardware and software. In addition legal issues such as breach of copyright resulting from the use of single version software of a LAN are a concern (Jamieson, Bergman and Levine, 1987).

Oritz (1986) states that the office of the future will be full of LANs with security problems. The challenge to management is to ensure the security and continued availability of information and computing resources necessary for business survival and competitive advantage. This risk management process includes the provision of adequate security and control in the LAN environment (Schaefer, 1985). Weighted against this challenge are the many risks inherent in the LAN environment. Risks (Fisher, 1984) appear in various forms ranging from natural disasters to accidental or intentional damage, loss, modification, disruption, and use. Kak (1983) provides some prominent examples of these threats, namely, spurious message interjection, message interception by unauthorized receivers, transmission disruption, and rerouting data transmissions to fake nodes.

The potential loss to an organisation may be higher in a LAN since the value of information found in the nodes tends to be greater than that found in the main computer (Oritz, 1986). This is because the information in the nodes has most likely been analysed and synthesized to arrive at a decision. This ‘decision form’ information may indicate a strategic direction, product development, or critical organizational intelligence and is therefore more valuable.

Table 1. Risks in the LAN environment

<table><tr><td>* Accidental or Intentional</td></tr><tr><td>- damage</td></tr><tr><td>- loss</td></tr><tr><td>- modification</td></tr><tr><td>- destruction</td></tr><tr><td>- use</td></tr><tr><td>to network hardware, network software, cable plant, personnel as well as programs and data files held on network computers and file servers.</td></tr><tr><td>* Computer Abuse</td></tr><tr><td>- spurious message interjection</td></tr><tr><td>- message interception</td></tr><tr><td>- transmission disruption/destruction</td></tr><tr><td>- rerouting data transmission to fake nodes</td></tr><tr><td>- unauthorized network file access</td></tr><tr><td>* Natural Disasters</td></tr><tr><td>* Other Exposures</td></tr><tr><td>- inability of network software to restart/recover</td></tr><tr><td>- network software failure</td></tr><tr><td>- lack of audit trails</td></tr><tr><td>- lack of network file integrity/correctness</td></tr><tr><td>- poor quantity or quality of network personnel</td></tr><tr><td>- inadequate training and supervision of network personnel</td></tr><tr><td>- inadequate network hardware/software maintenance</td></tr><tr><td>- inadequate network documentation</td></tr></table>

Auditors are prime security and control experts and audit both the network environment and the applications that use the network. Consequently they should be involved in the discussion of security, control and audit issues prior to commissioning and during operations. The audit approach to network operations includes: identification of risks; review and suggestion of appropriate security and controls to include in or around network components or functions; and ensuring the auditability of the network.

This paper addresses this challenge by providing a framework for the security and control review of the LAN environment from an operations perspective. For each main component of the network a brief explanation is provided and the security and control operational issues are considered. The components include cable plant, network hardware, network software, network management centre, computers and file servers, external connections, data and programs, and human resources. An audit plan to aid management, security officers, and auditors in the review of network operations is also provided.

## Security and control measures

Table 2 summarizes the security and control measures that should be considered in the operations of a Local Area Network.

These issues are considered in detail under the various component parts.

## Cable plant

The cable plant consists of the actual cable plus ancillary equipment such as star couplers and head-ends.

Network cables may be inadvertently damaged in the absence of up-to-date documentation. Delays may also occur in repairing faulty cable plant due to an inability to locate the faulty sections. Pre-installation review of network cabling and inspections following cable laying can often detect problems. Lack of up-to-date documentation may also affect the interpretation of LAN performance measurements. The performance of the network is dependent on the performance of ancillary equipment such as RF modems. Drift in these components can be determined by periodic testing. The results obtained are compared with previous network certification results to determine any change in network characteristics.

In addition to component drift, changed network performance may be due to electrical noise, power surges and drops, and changed environmental conditions such as lightning and floods. Abnormal network conditions should be investigated immediately. An increase in the number of network errors is an indication of potential problems. Power regulators and backup power sources for LANs are also effective preventative and corrective controls.

Rogue network devices can monitor traffic on the network. Securing all known network devices still leaves the network vulnerable to tapping. Since the ability to tap most LAN copper based cabling is high, access should be restricted to the LAN cable plant and all access points. Periodic inspections should be performed to ensure that security has not been breached.

## Network hardware

The incidence of theft in the general community is on the increase. Network hardware is no exception and is often costly to replace. Theft can be reduced by maintaining adequate physical controls over access to equipment. Two techniques often employed are semi-permanent attachment of hardware to the building and locating equipment in locked rooms where access is restricted to authorized users. Regular audits of

Table 2. Security and control measures

Cable plant

Restrict physical access

Up-to-date documentation

Investigate abnormal network conditions

Backup

Environmental conditions

\- lightning

\- floods

## Network hardware

Sensitive data access

\- key locked equipment

• restricted bootup procedures

• inbuilt chip identification

• dynamic signature verification

\- data encryption

\- authentication between devices

Up-to-date documentation

Regular audits of equipment

Logging and follow-up of all reported faults

Backup

\- strategy

\- equipment

Maintenance

\- diagnostic aids

\- test equipment

\- documentation

Limit and monitor usage of network monitoring devices Environmental considerations:

\- uninterruptable power supplies or voltage regulators

\- opto-isolating equipment

\- air conditioners

• physical protection barriers

## Network software

Automated procedures

Software licensing agreements

Physical controls to reduce theft

Up-to-date documentation

Operational software integrity

Appropriate maintenance strategy

Software upgrade controls

Logging and follow-up of all reported faults

## Network management centre

Access control

\- user ID and password

\- restrict network resources

\- inactivity

\- auto-disconnect terminal circuits after:

\- number of failed logins

• time of day restrictions

\- restrict network supervisory functions

Network monitoring

• time stamped audit trail

• network configuration alteration recording

• network error and performance recording

• alarming for preset events

\- message tracing and audit trails

Remote configuration

Remote diagnostics

Remote logins

## Computers and file servers

Security ultimately rests with the destination computer or file server

## External connections

Encryption

Automatic dial-back modems

Avoid publication of numbers and change regularly Inhibit:

\- reverse charging

\- message and vendor provided facilities

\- external connections for externally connected users

Monitor and assign all communications costs
Restoration facilities for disconnections

## Data and programs

Contingency and disaster recovery plan

Encryption

Backup

Uploading and downloading of data

Unauthorized copying

Valid software licence agreements

## Human resources

Management commitment

Assign responsibility for:

\- network operations

\- disaster planning

Adequate training or personnel

Information Centre

Segregation of duties

Mandatory vacations

Personnel security checks

Maintenance supplier vetting equipment will identify security breaches. Up-to-date documentation including equipment description, serial number, revision level, previous maintenance history and location will assist in the identification of equipment as well as in making insurance claims. Permanent marking or tagging of equipment inside and out is a useful aid for recovery identification of stolen equipment.

Theft is not necessarily restricted to the physical removal of equipment. For instance unauthorized access to sensitive data and restricted network resources may result from unauthorized access to network equipment. Key locking equipment and restricted bootup procedures for workstations, possibly using diskettes, may be considered. Use of diskless work stations make it more difficult to export sensitive information. Access to LAN devices such as file servers and peripheral equipment such as printers and plotters should be restricted to systems administrators and authorized users. Ideally these devices should be kept in locked rooms and regularly checked. Consideration should also be given to the use of equipment with inbuilt chip identification, dynamic signature verification (Worthington, Chainer, Williford and Gundersen, 1985), authentication between devices (Power and Wilbur, 1985) and data encryption.

Regardless of the actual functionality of the network, the user's perception is dependent on his/her ability to use it. Thus it is very important that operating manuals are current, correct and well written. LAN operating manuals are usually developed at two levels, systems administration and user levels. Simple menus and/or batch files and on-line help facilities also aid operational efficiency and control.

The functionality and performance of the network is affected by equipment failure. Backup equipment may be used to reduce the disruption to network operations. The assessment of backup requirements should be based on the cost of network disruption (particularly application based review), equipment reliability and estimated time for repair. Regardless of the provision of backup equipment, faulty equipment should be repaired as quickly as practicable. It is recommended that an appropriate maintenance strategy be developed. Considerations would include:

\- Relative disruption to the network through equipment failure

\- The expected mean time between failure (MTBF) of network equipment

\- Anticipated time for repair - Vendor and organization expertise in fault diagnosis and repair

\- Geographic location – for instance, if the LAN was installed hundreds of miles from vendor premises, the organization would probably need to become more self sufficient or require vendor personnel to be located on site; and

\- Distribution of failure over time (that is, age of the equipment).

Irrespective of the maintenance strategy adopted it is important that adequate procedures are developed and adhered to for logging network faults.

Manufacturers often recommend upgrades to equipment to overcome known faults. These upgrades should be performed as soon as practicable following notification should a cost/benefit analysis be favourable. In addition, the availability of spare parts and the vendor's willingness to enter into or renew maintenance agreements becomes more difficult as equipment ages. The situation should be monitored and appropriate action taken. It is particularly sensible to maintain critical equipment at the latest revision levels.

Network diagnostic aids and test equipment are used to ensure that changed network conditions including faults are quickly identified. They should be regularly tested and reviewed to ensure applicability. Since certain test equipment such as data analysers may be used to monitor network data, a policy should be developed and enforced for its use. Thorough and up-to-date documentation for all network equipment, test equipment and diagnostic aids will greatly assist in the speedy diagnosis and rectification of faults.

Environmental conditions can have an adverse effect on network equipment. Consequently it is essential that controls such as air conditioners be regularly maintained and checked. It is advisable to use alarms to indicate malfunction and regular reviews to ensure the applicability of current measures. Good general housekeeping of the environment is important to protect network components, for example from dust or sawdust in servers from office alterations.

## Network software

The users' perception and use of the network depends on their understanding of both the equipment and the software. Operating manuals, which are installation specific not just vendor manuals, should be regularly reviewed to ensure they are up-to-date and relevant. Certain procedures should be automated to overcome the potential lack of user sophistication in LANs. However this automation should not jeopardize network security.

While software can be purchased outright, it is often provided on the basis of an annual licence renewal. The agreements covering software should be documented and renewed when necessary.

The theft or unauthorised copying of network software is less likely to immediately affect the operations of the network than is the theft of network hardware.

However the organization is under an obligation via its software agreement to take all measures practicable to prevent the occurrence of theft. Measures which could be undertaken to reduce the possibility of theft include the labelling and storing of non-operational copies of software in secure locations. Fortunately network software is usually keyed to specific hardware, so theft of network software without network hardware is pointless. Network software documentation including description, serial number (if appropriate), revision level, previous maintenance history and location should be maintained. This will assist in the regular audits that should be performed to check for the removal or revision of network software. In the latter case operational software integrity can be ensured by periodically downloading new versions of network software to network devices.

No software is entirely free of security loopholes. As a result all known loopholes should be documented, the degree of risk assessed and appropriate action taken. While the impact of selecting non-default options is normally fully assessed, this is not always the case for default settings. Steps should be taken to ensure that this situation does not occur.

When software is being upgraded, the normal security controls are by-passed. Strict controls should be in place during the upgrade. In the event of difficulties occurring with the upgraded software, the implementation should be performed in such a way that the network can revert to its pre-upgrade status.

The software upgrade process should be part of an overall maintenance strategy. This strategy should be reviewed at regular intervals to ensure its appropriateness. Aspects of this strategy would include maintenance agreements with the software vendor, maintaining software at the latest revision levels to take advantage of 'bug' fixes, improved functionality and continued vendor support. In addition diagnostic aids should be regularly reviewed and tested.

All reported faults should be logged. These together with network logs should be reviewed and appropriate action initiated.

## Network management centre

Among the responsibilities of the network management centre are network access and network monitoring.

## Access control

The network management centre provides the primary means of preventing unauthorised access to the network. All valid users should have appropriate user identification, passwords and privileges assigned. The effectiveness is reduced if null passwords are allowed, passwords are not changed at regular intervals or network entries are not deleted for employees that have left the organization. Network access should be denied to users following a specified number of failed login attempts.

User access lists are used by the network management centre to determine which devices a user is authorized to access. These lists should be regularly reviewed and maintained. In addition, users should be authorized access to specified devices rather than being denied access to particular devices. In this situation, there is a conscientious decision to grant access to a user.

An employee that has gained out of hours access to a building may be tempted to 'play' on the network. Time of day restrictions may be useful in limiting the use of facilities to specified times of day. These restrictions should be regularly reviewed.

Consideration should be given to denying computer provided remote login facilities in sensitive networks. Gaining access to a low security computer and then using the remote login capability to access a high security computer is a method often used by hackers to hide their identity. When remote login is enabled the computer originating the connection should record all successful and unsuccessful remote login attempts. This log should include the user identification, the destination address, the time of access and the duration.

Individuals have a tendency to leave workstations unattended and still logged onto computers or file servers at certain times of the day (such as at morning tea). During this period, anyone with physical access to the workstation has all the access privileges of the actual user. The network management centre should disconnect a workstation user after a specified period of inactivity.

## Network monitoring

The network management centre or administrator should log all successful and unsuccessful login attempts. Potential security breaches can be determined from the log of unusual or alarmed network events in conjunction with user access rights documentation (for example, user identification, access rights and time of day rights) and network configuration data. Due to its high susceptibility to hackers, accesses that result in computer pass through should be included. All events should be investigated with priority being given to alarmed events.

The network management centre can also monitor network performance. Alarm limits should be set to indicate significant variations in network performance. The variation may be due to high error rates, unusually high network utilization or altered utilization characteristics (for example, greatly increased use of graphics or critical growth of data bases). The performance results should be periodically compared with those previously obtained. Changes in network configuration, hardware and software may be responsible for any noted performance differences. Relevant documentation (such as current network configuration, recent network changes and past performance measurements) should be available to assist in the interpretation. User reports of poor network performance should also be investigated and followed up by the network management centre.

Since the network management centre is the hub of the network security, all software and hardware controls previously mentioned should be rigidly enforced. In addition all supervisory commands should be logged and subjected to periodic management review.

## Computers and file servers

Regardless of the network security installed, the prevention and detection of unauthorized access and the control of consequent financial loss should reside primarily in the computer and/or file server, (Gardner and Saunders, 1986). Reliance on network management security and the security implemented by other computer systems on the network is potentially fool-hardy.

Access should be controlled by the mainframe security function and be subjected to all the mainframe's normal security controls for:

• Terminal/modem identification

\- User ID/password, including number of invalid attempts allowed per day, length, frequency of change, deletion on employee termination

\- Terminal logout after a period of inactivity

\- Logging and follow-up of access exceptions

\- File and directory access rights

\- Directory rights – which restricts user action and access rights in particular directories on the LAN file server and

\- File attributes – this is normally used to prevent accidental deletion of programs and data

\- Encryption of transmitted messages and files

\- Access to and use of mainframe software

\- Segregation of production and development environment.

Access to PCs can be controlled by security packages similar to those available for mainframes.

## External connections

The provision of external access exposes the network to attack from individuals outside the organization as well as unauthorized use of external facilities by internal users. The best security possible is provided by disconnecting external access to and from the network during periods when it is not required. Fortunately there are a number of measures that provide a degree of protection at other times.

Hackers (Baird, 1985) have accessed computers and networks via dial-up modem facilities and external network connections. When it is necessary to provide dial-up facilities, the modem should have call back facilities installed. This applies regardless of whether the modem is directly connected to the network, to a computer on the network or to a PABX which is connected to the network. The user identification and dial-back numbers stored in the dial-back facility should be regularly reviewed. The delay implemented before the modem commences dial back should be sufficient to accommodate all PSTN exchange types. Some newer modems provide dial-back on a new line as an additional precaution.

Security is endangered by the publication of external access numbers. Even with the best intentions, numbers may become known. Thus it is advisable to change these on a regular basis. In addition a hacker is more likely to make several attempts to access a facility if he/she is not paying. Thus it is advisable that reverse charging facilities should not be enabled. In addition many packet switched networks provide a password facility. This facility should be used as a defence against unauthorized access.

Messages and vendor provided facilities such as the ability to list network devices assist the would-be hacker. These facilities should not be implemented for external connections. In addition all network access control measures previously discussed should be implemented.

A hacker may use computer and network resources to gain access to facilities outside the organization. For instance he/she may wish to use the organization's network to gain access to other networks. This can be prevented by inhibiting access to all external facilities for externally connected users.

A member of the organization may attempt to utilize the network to gain unauthorized access to external networks and facilities. For instance he/she may send a private telex. The same controls that apply to user access to network devices should apply to external connections. In addition all communication costs should be monitored and assigned to an individual user. A monthly audit should also be conducted of all communication costs.

Number, time and date stamping of all in and out bound messages assists in ensuring their correct delivery. Wherever possible a network protocol should be used that guarantees the timely, error free delivery of messages in the correct order. The use of encryption for all messages guards against the possibility of interception. An analysis of exposure should be undertaken prior to the blanket use of encryption.

Unfortunately external connections are subject to failure or degraded performance due to high error rates and industrial disputes. Adequate procedures should be in place for such events. Line utilization and error rate statistics often give warning of impending problems. All occurrences of unacceptable error rates should be followed up immediately. In the case of a complete communications failure, communications may be switched to the backup facility if installed. If a dial-up modem facility is used as a backup for dedicated leased line links, automated procedures should check to ensure that the leased line has in fact failed before it is activated.

## Data and programs

Disruption to network operations may seriously affect the business of the organization. Reasons for this include the inability to process due to network down time and the loss of data due to hardware failure. As with any critical business operation, the organization should develop a contingency and disaster recovery plan. The ongoing stages are:

\- Analyse the organization's exposure to interruptions in processing

\- Assign responsibility for recovery coordination

\- Develop measures to reduce risks to acceptable levels

\- Test the plan

\- Update and maintain the plan.

LANs often lead to a high concentration of data particularly in PC networks. A disruption to file server operations may affect many users. The potential loss of data resulting from a hard disk failure may be catastrophic without the implementation of an appropriate back-up and recovery procedure for LAN file servers. Critical data directories requiring frequent backup should be identified. LAN users should be informed of the date and time of each back-up operation along with a list of the directories and data files included in the backup. Backup procedures may be automated using the systems clock as a trigger. However, as automated backups skip over active files, there needs to be a balance between the frequency of backup and the use and utility of data during backup. Critical data should be stored off site or in fireproof safes. The efficiency of the backup operation can be improved by the use of such systems as streaming tape units.

The concentration of data on file servers and computers poses risks for data security not so apparent on single user systems. A user gaining access to an account with the appropriate privileges can view the data. This unauthorized viewing may be inhibited by storing highly sensitive information in encrypted form on the file server, or in unlisted or 'unshared' volumes. In addition, the file server normally allocates disk space as required. If a file is deleted, then this disk space is available generally. Files are usually deleted by deleting the entry in the appropriate directory table. However the contents of the file are not actually deleted. To prevent the possibility of another user viewing the contents of a deleted file, it should be overwritten by blanks, using for example the Norton wipe-file utility.

As previously discussed modern test equipment and rogue network devices can monitor network messages. To prevent the monitoring of highly sensitive data use encryption. Since encryption will reduce the performance of the network, it may be inadvisable to encrypt data that is not overly sensitive. An alternative is to encrypt the data indices only.

LANs often result in a large number of users requiring access to the same data on a mainframe. The downloading of data to an intermediate storage device such as another computer or file server may be used to isolate the mainframe from users. Procedures should be developed to ensure that the data downloaded is the correct version for the task to be undertaken. Filename, data and version identification should be clearly specified, checked and stored with the date in the intermediate computer or fileserver.

Databases are often maintained in parallel with the mainframe database. In some instances these data bases are created using data downloaded from the mainframe. This maintenance should be discouraged since it will call into question the integrity of the data.

The uploading of data to the mainframe should in general be discouraged. Mainframe data integrity controls are normally not applied to localized data. Where it is allowed, strong integrity controls should be enforced over the intermediate computer, fileserver and PC data. The use of control totals to reconcile the upload process is recommended.

The risk of unauthorized copying of application software may be reduced by:

\- Assigning appropriate file access rights on the computer and/or file server to prevent copying

\- Using the hidden files option to hide application programs

• Using diskless workstations

\- Modifying the program image when transmitting across the network such that it will only run on the destination workstation. All workstations have unique addresses

\- Ensuring adequate physical storage and security for all off-line copies of programme and data

\- Maintaining an application program inventory and conducting regular audits

\- Logging network activity.

An organization should only use software for which it has a valid application software licence agreement. It is important to review regularly these agreements to ensure that they remain valid and that the software is licensed for the computers on which it is currently running. Good documentation is essential.

## Human resources

A high level of management commitment is important to any business activity. A LAN is no exception. Management should ensure that sufficient human resources are provided to manage adequately the network and that all security controls are implemented.

Responsibility should be assigned for maintaining and monitoring the LAN to a particular person or group of individuals. Since it is inadvisable to rely entirely on a single individual, a number of staff should have adequate technical skills to perform this function. Alternatively these skills must be obtainable in a contingency situation.

The responsibility for the coordination of a disaster recovery plan should be assigned to a particular individual. This individual may also have responsibility for network management.

The network management staff have the greatest opportunity to by-pass normal security procedures. The probability of hiring staff that may commit fraud is reduced by obtaining security clearances for potential staff (Carroll, 1979; Jamieson, 1986). In addition, enforcing mandatory vacations and separation of duties (Parker, 1981) as well as the logging and checking of all situations where they could circumvent security in the performance of their duty will deter wrongful action and assist in its detection. Management should also check that staff have implemented and adhered to all required security, backup, diagnostic and test procedures. User adherence to all control procedures should also be monitored.

Since many security controls are by-passed during maintenance, vendors who perform maintenance should be checked for competence and trustworthiness.

The network is unlikely to achieve its full potential if users do not understand how to use it or receive inadequate support in the event of problems. Training in the use of the network and associated application software should be provided along with access to reliable technical support and documentation. The implementation of an Information Centre facility for network assistance may also be of benefit.

## Audit approach

Network operations should be periodically subject to audit to ensure that security, control and auditability features designed and built into the LAN are maintained and used on a day-to-day basis.

## Table 3. Audit approach or plan

## Identify and document:

• LAN threats or risks

• LAN security, control and audit facilities

## Review:

\- management structure and resources for LAN operations

\- human resource staffing of LAN operations • prospective packaged network software - audit trail facilities namely journal logs, event logs, exception logs, error logs and special audit monitor logs

\- network monitoring facilities and network log design

• and document external connections to the LAN

\- program, data and data storage protection afforded by the network software and hardware

• network contingency plan design

## Obtain:

\- management commitment to an audit review of the network environment and operations

## Establish:

\- an audit plan for the LAN operations review and testing

## Review:

\- the division of duties between network operations and application message entries

\- documentation for all network component parts

• physical security network component parts

● network systems access and resource allocation security

\- encryption facilities

• key management

• key file encryption facilities

• network technical control procedures • network log analyser and reports - network contingency plans, procedures and documentation

## Conduct:

\- inventory audit

A suggested approach to the audit of network operations is provided below:

\- Obtain management commitment to an audit review of the network environment and operations

\- Establish an audit plan for the LAN operations review and testing. This should involve setting appropriate control objectives based on the eight major areas previously covered, namely cable plant, network hardware, network software, network management centre, connected computers and file servers, external connections, data and programs and human resources. The individual controls mentioned in these sections provide a comprehensive guide to measure security and control in the LAN environment and may assist the formulation of your audit approach.

\- Review the division of duties between network operations and application message entries. Also ensure separation of functions within network operations, namely key distribution, network maintenance, identification/password control, and network log review, approval and follow up. Supervision by the network manager or network operations supervisor is also essential and should be reviewed.

\- Review documentation for network cable plant, hardware, software and operations to ensure adequacy and currency.

\- Check physical security surrounding cable plant and network hardware at both the master terminal operator centre and network nodes.

\- Conduct a regular inventory audit of all network components including cable plant, network hardware and software and ensure inventory registers are regularly maintained.

\- Review network systems access and resource allocation security by examination and verification of network allocation/access tables. Also ensure that non-existent terminals are not predefined in the host tables. If they are defined, ensure that these terminals are cut off from operational use either by hardware protocol verification (electronic terminal ID check to the address chip), password control or by being by-passed in the polling list

\- Review encryption facilities for both hardware and software and ensure that encryption boxes are intact (not tampered with), and that encryption is operating as stated in the design document.

\- Review key management, that is the process of creation, assignment, distribution, storage and cancellation of keys as this area is often the most exposed part of the encryption process (Fidlow, 1985; Power and Wilbur, 1985). If key management is manual, review key delivery arrangements to remote nodes (for example, certified mail or hand/courier delivery). Usually when the required frequency of key change is high and/or a large number of nodes require servicing then key management should be automatic. Automatic key management involves cryptors controlling the functions of key generation and distribution, although originally initiated by the network manager or by a more secure design which replaces the operator-initiated key change with downloaded instructions from the host. Frequency of key change is variable by time, per connection or per session. If key management is automatic, review the method for generating and distributing the keys and ensure frequency of change is appropriate to the organization.

\- Review key file encryption facilities and ensure that a selection of files which should be encrypted are in fact encrypted, for example host network/terminal tables, central password/login identification files, file directories and network logs. Ensure that only one way encryption (clear text to encrypted form) is used for password entry validation.

\- Review network technical control procedures to ensure that network logs or built-in alarm software reporting to a dedicated ‘alarms’ printer, are being continually reviewed during the day and that abnormalities (carrier failing/restoring, terminals not responding to polls and selects or being logically disabled, file server failures, build up of delivery queues (Fidlow, 1985) are detected and followed up

\- Review network log analyser and reports to ensure that appropriate reviews and follow up action is taken on exceptions detailed on the logs.

\- Review network contingency plans, procedures and documentation for completeness and adequacy. Ensure that regular walk-throughs and tests of these plans are performed and that appropriate personnel are responsible for maintenance and update of the contingency plans.

The audit approach should not only involve discussions and review of the points raised above but also involve tests such as examination, verification and performance. An audit testing environment, similar to an integrated testing facility, may be constructed on the network to allow the auditors to perform on-line testing of the network and facilities.

## Conclusion

With the increasing reliance by organization on a LANs environment, due regard must be paid by management to the security and control issues discussed. It is vital that information systems security officers or auditors be involved in performing periodic reviews of network operations. This approach or framework to LAN security may serve as a basis for inclusion into the corporate Information Systems Security Plan.

## References

Baird, L.L. (1985) Sensible Network Security. Datamation, pp. 22–28

Carroll, J.M. (1979) Computer Security. Butterworth, Boston

Caelli, W.J. (ed.) (1989) Computer security in the

age of information: Proceedings of the 5th International Conference on Computer Security, IFIP/Sec '88, Elsevier North Holland. pp 439–469.

Fidlow, D. (1985) A comprehensive approach to network Security, Data Communications, April.

Fisher, R.P. (1984) Information Systems Security. Prentice-Hall, New Jersey.

Gardner, J.A. and Saunders, P.A. (1986) Security Risks in Data Communications. EDPAC.

Jamieson, R. (1986) Impact of Audit Involvement on Systems Development. Information Systems Research Report No. 14, University of New South Wales.

Jamieson, R. and Low, G.C. (1989) Security, control and audit issues in local area network design. Computers and Security, 8, 4, June.

Jamieson, R., Bergman, J. and Levine, J. (1987) Computer security: what every executive should know. Self Study Audio Package and Study Guide, Continuing Education University of New South Wales.

Kak, S.C. (1983) Data security in computer networks. Computer, February.

Low, G.C. and Hunt, D.C. (1986) Multi-vendor Local Area Networks: Some Technological Issues. Aust. Comp. Journal 20, 3, pp. 138–144.

Low, G.C. and Hunt, D.C. (1988b) A successful local area network project, Aust Comp. Conf., Sydney, Sep. 21–23, 1988, pp. 499–510.

Oritz, J. (1986) Security and local area networking. Information Age, 8, 1.

Parker, D.B. (1981) Computer Security Management.
Reston Publishing Co Inc., Reston.

Power, J.M. and Wilbur, S.R. (1985) Authentication in a heterogeneous environment. Proceedings of the Third IFIP International Conference on Computer Security, Dublin.

Schaefer, M. (1985) Security vulnerabilities in the automated Office. Proceedings of the Third IFIP International Conference on Computer Security, Dublin.

Wing, P. and Jones, M. (1986) How secure is your PC. Notes for a proposed seminar on PC security.

Worthington, T., Chainer, T.J., Willingford, J.D. and Gundersen, S.C. (1985) IBM Dynamic Signature Verification. Proceedings of the third ITIP International Conference on Computer Security, Dublin, August.

## Biographical notes

Graham Low is a senior lecturer in the School of Information Systems, University of New South Wales. He holds BE (Chem) and PhD degrees from the University of Queensland and is a Member of the Institution of Chemical Engineers and a Chartered Engineer (UK). He lectures externally to organizations such as the Australian Computer Society, in communications, communications security and software engineering.

He also acts as a consultant to universities for the design and installation of both campus-wide networks and smaller PC networks. Prior to joining the School of Information Systems, he was Head of the User Services Unit for the Computer Services Department. As Technical MIS Manager at CSR Ltd, he was responsible for data communications planning and installation. Other positions he held with CSR include Systems Engineer and Shift Chemist.

Rodger Jamieson is a director of the centre for Information Technology Research in the School of Information Systems at the University of New South Wales. He holds honours degrees at both Bachelor and Master of Commerce levels from the University of New South Wales, is a qualified Chartered Accountant, member of the Australian Computer Society and a Certified Information Systems Auditor from the EDP Auditors Association (USA). His prior experience included computer security and audit consulting for Touche Ross and Coopers & Lybrand, as well as commercial experience with the AMP Society and Honeywell.

Mr Jamieson is involved in applied research in the fields of EDP security and audit, and expert systems. He has presented and published his research findings, and has designed and presented a range of computer audit seminars and courses to auditors, data processing professionals, management and consultants in Australia and overseas. In addition, he has lectured widely to professional bodies, tertiary education institutions, government and the federal police in this area.

Address for correspondence: School of Information Systems, University of New South Wales, P.O. Box 1, Kensington, NSW 2033, Australia.
