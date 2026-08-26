---
otero_id: 18839
otero_key: "QPB3S4D5"
title: "Computer infectors"
authors: "Gilbert W. Joseph; J.Ellis Blanton"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90045-h"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Computer infectors Prevention, detection, and recovery

Gilbert W. Joseph

University of Tampa, Tampa, FL, USA

J. Ellis Blanton

University of South Florida, Tampa, FL, USA

Computer infectors (such as logic bombs, worms, and viruses) represent a growing concern among information system (IS) professionals. Infectors may be introduced to systems intentionally by employees or by an unknown assailant under the guise of a Trojan horse or through more direct infection means. This paper identifies the organizational and technical aspects of a total infector control program. Since eradication and recovery controls cannot guarantee total damage removal, the primary objective of an infector control program is generally identified as preventing an infection. However, whether an organization should properly emphasize prevention/detection or recovery depends on the organization's appraisal of infector threats and risks.

Keywords: Computer infector, Logic bomb, Worm, Virus, Boot infector, System infector, General executable program infector, Trojan horse, Prevention, Detection, Recovery, Organizational controls, Technical controls, Infector planning emphasis, Infector threats, Infector risks.

## 1. Introduction

The end user computing (EUC) era has brought many benefits to organizations, such as: Increased employee productivity and learning; competitive advantage through new product/market opportunities; and improved internal organization effectiveness [7]. Unfortunately, with EUC also come many organizational risks that must be met through appropriate control programs [1].

An area of concern in any EUC environment is the protection of application and data files from accidental or intentional damage. A threat to file integrity that has received a significant amount of recent press are computer infectors: Programs or series of programs that affect, inhibit, interfere, corrupt and/or obstruct the normal operation and performance of a computer and its operating system $[16]$ . An estimated 250 000 outbreaks of computer infectors have occurred, affecting over 40% of large US companies $[8]$ . As EUC environments become more integrated through local area networks and linkages to mainframes, the vulnerability of EUC application and data files and the resulting consequence of damage are expected to increase.

![](/api/attachments/QPB3S4D5/fulltext/images/33c80bb1988215071c8dd0d95df9a8b0de045801f8101c63e8535a78c6bcd0ed.jpg)

Gilbert W. Joseph is Assistant Professor of accounting at The University of Tampa, Tampa, FL. He spent over twenty years with the United States Federal Government working in computer systems analysis, systems design, computer performance evaluation, system planning, application programming, and database development. Professor Joseph teaches computer science, accounting, statistics, EDP auditing, and a disaster planning course.

Correspondence to: Gilbert W. Joseph, Box 1F, College of Business, University of Tampa, 401 West Kennedy Blvd., Tampa, FL 33606-1409, USA

![](/api/attachments/QPB3S4D5/fulltext/images/601f9df8ab18dac92ee3cacac5b7027e2dd30995092f68822a9b92f348fbbcce.jpg)

J. Ellis Blanton is Assistant Professor of MIS in the College of Business Administration at the University of South Florida, Tampa, FL. He received his Ph.D. in MIS from The University of Georgia, Athens, GA and has published articles in banking and MIS journals, and has presented papers at national professional conferences. His primary research interests are the organizational impacts of information systems and the development and implementation of information systems for competitive purposes.

To date, academic research has only examined computer infectors from a technical perspective and has not addressed the need for a total control program for: First, preventing infections and second, detecting and recovering if infection should occur. The objectives of a total computer infector control program should be based on an analysis of the threat (degree of vulnerability) and the risks (potential for loss). Not all EUC environments possess either the same threat of infection or the same risk of loss and, therefore, they should not have a control program with the same objectives or components.

## 2. Background

Computer infectors can occur in any computer environment, from standalone microcomputers to host-based wide-area networks. This article, however, focuses on prevention, detection, and recovery controls appropriate for microcomputer environments, because they typically do not possess the internal hardware and software controls found in multi-user minicomputers or mainframe computers. People with even limited programming skills can often circumvent the simple controls that are built into micros. With the increase in home computers and computer training in schools and the workplace, more people now possess the skills needed to construct infectors. Additionally, micros tend to be less well managed or controlled within organizations: Software may be acquired from many sources and transferred between computers in an uncontrolled manner. Although many of the examples and recommendations here relate to IBM microcomputers running DOS operating systems, many of the controls that are discussed are just as appropriate in non-IBM environments using other operating systems.

Although microcomputer environments are particularly vulnerable to computer infectors $[6]$ , unprotected host and large area network environments are also susceptible. Organizations often expand by internetting micros, and even in organizations with centralized computer resources, micros may be installed as intelligent terminals. Thus, the logical extension is that computer infectors may migrate from micros to larger computers and that the physical connections currently exist to permit this migration $[2]$ .

## 2.1. Types of infectors

There are several different types of computer infectors that can threaten EUC files. Although most people refer to them as viruses, in fact, only one variation is classified here as a virus.

A logic bomb is the least sophisticated type of infector. It may simply be a poorly written program that causes unintentional damage when executed. However, it may also have been designed by a disgruntled programmer to cause damage. Sometimes a logic bomb is introduced to a system in the guise of an application which overtly appears desirable (this is known as a trojan horse). A logic bomb does not spread by replicating itself and the source of the damage remains within the operational domain of a single program.

A worm, on the other hand, replicates itself, filling-up computer memory or increasingly demanding system resources until the computer becomes overtaxed. Often, copies of the worm must continue to communicate with the original worm segment [18].

A virus also replicates itself; however, each copy is independently capable of the intended damage. Viruses usually infect a 'host' program and require the 'host', to execute before the virus is capable of assuming control. Several different types of virus exist [19,22]:

(1) A boot infector moves the DOS programs from the 'boot' sector (usually the first sector on a disk) and takes control when the system first starts;

(2) A system infector attaches itself to or replaces selected memory-resident operating system commands, such as the directory listing command, the copy command, or the erase command;

(3) A general executable program infector is the most dangerous because it can spread itself to any executable program file (files which end in .COM or .EXE). With a general executable program infector, the degree to which the virus has spread may not be known.

Two attributes of computer infectors are of particular concern when designing an effective control program. First, because they can cause the same type of damage, it is often not possible to distinguish between types of infectors based upon their symptoms. Recovery controls, therefore, cannot be limited to a specific type of infector. Second, some of the newer, more sophisticated viruses may combine features and capabilities of different computer infectors, e.g., house one infector inside another or mutate from one type of infector to another. If risks warrant, it may be prudent to assume the worst case scenario; this may significantly increase the extent of detection and recovery controls needed. Fortunately, prevention controls are often the same, regardless of the type of infector.

## 2.2. Threats of infection

Table 1 identifies the various threats from computer infectors. Threats range from annoyance to death, depending on the destruction intended by the creator of the computer infector and the system which happens to become infected. Regardless of the specific symptoms, the original intent of the programmer may be to wreak havoc on a possibly unknown system with little regard for the consequences. A good example is the “AIDS information” diskette, distributed by a fictitious medical information service, containing an infector which destroyed medical files [23].

Table 1
Possible impacts of infectors

<table><tr><td>Impact</td><td>Example</td></tr><tr><td>Annoyance or harassment</td><td>New or altered messages;Unusual graphics;Changed monitor colors;Locked shift key</td></tr><tr><td>Random havoc</td><td>Keyboard changes;Move data to/from peripherals;Random change of data and filenames</td></tr><tr><td>Saturation</td><td>Fill memory;Overwrite and/or fill disks;Perform unnecessary I/Os;Perform unnecessary computations;Insert delays in processing</td></tr><tr><td>Modification</td><td>Selective destruction;Mark disk tracks as unusable (“bad”);Data alteration</td></tr><tr><td>Destruction</td><td>Complete erasure;Disk reformatting;Physical damage;Make commercial software inoperable</td></tr><tr><td>Interrupted operations</td><td>Lost productivity due to recovery efforts;Lost confidence by outsiders requires management time and distractions;Lost sales opportunity costs</td></tr><tr><td>Corruption of financial data</td><td>Transactions lost;Decision making impaired;Financial statements misstated</td></tr><tr><td>Data theft</td><td>Copy or transmit data;Destroy data so it is unusable;Reveal user IDs, passwords</td></tr><tr><td>Loss of money</td><td>Costs associated with recovery;Costs associated with auditing;Extortion (blackmail)</td></tr><tr><td>Injury/death</td><td>Disrupt real-time process control systems;Disrupt medical systems</td></tr></table>

## 3. Infector controls

In spite of the severe operational threats from computer infectors, there are many practical and sometimes simple controls that can be implemented to prevent and detect infection. Once an infection occurs, however, recovery controls can be complex. And they cannot guarantee that no reinfection will occur or that damage to files, programs, and hardware can be totally reversed.

Many control programs are designed on the assumption that infectors can be stopped solely by technical controls involving hardware and software. However, prevention and detection controls must also involve employees, making them aware of the risks and symptoms of computer infectors and instilling a desire to support the total control program.

Infector controls fall into two major categories: Organizational, and technical. Each is now discussed in greater detail. See Figures 1 and 2.

## 3.1. Organizational controls

These are aimed at building a strong infector awareness: A perception by end users that management is serious about infectors, and that there is an organizational mechanism to deal with prevention, detection, and recovery controls. Establishing organizational controls is primarily the responsibility of management.

## 3.1.1. Infector threat appraisal

This involves analyzing the vulnerability of the business to a potential computer infection; it is preventive in orientation. The threat from each of the different types of potential infectors should be evaluated. A particular organization may be vulnerable to different infectors in varying degrees. It is necessary to identify all critical data files, application programs, and software packages whose loss or damage would severely impact computer system operation, business decision making, accounting transaction processing, or cost/financial reporting.

## 3.1.2. Infector risk appraisal

This measures the potential loss to the organization if an infection occurs; it has a recovery perspective. Often, losses are not easily quantified, since they include such intangibles as lost customer confidence or perceived service quality.

If possible, the risk appraisal should be stated in terms of impact on the resources of the organization. This appraisal will provide a measure of the magnitude of the problem should an infection occur and it will guide many steps that follow. A clear assessment of potential dollar losses permits the computation of an annual loss expectation, which can be compared to the cost of infector recovery controls.

## 3.1.3. Plan the infector control program

Management should develop a formal plan and milestone schedule for the development of the control program. It should be treated as any other major project undertaking. The formal plan should identify how the program will be developed, maintained, evaluated, and updated and should identify the significant program products including guidelines, policies, procedures, and the specific objectives of the infector protection program. Measurable objectives are particularly important, since without them success or failure of the program could not be determined.

![](/api/attachments/QPB3S4D5/fulltext/images/2c6177142467c10268312be3fdc74d7d9315e70237b920d67c39864788dcd091.jpg)  
Fig. 1. Organizational infector controls.

From a prevention/detection perspective, control objectives might include: (1) the types of infectors perceived as the greatest threats; (2) the desired degree (completeness) of prevention; (3) the desired limitations on infector spread; and (4) the systems and/or files which should be afforded the greatest protection.

From a recovery perspective, control objectives might include: (1) the desired speed of the recovery process; (2) the desired limits on the extent of damage; and (3) the maximum tolerable costs associated with lost or damaged files.

Based on the threat analysis, it may be necessary to develop separate sub-plans for each type of infector, perhaps dealing with one sub-plan at a time. For example, management may find it more important to deal first with in-house developed logic bombs, or perhaps to concentrate first on externally introduced viruses. The infector risk appraisal will guide the priorities for the control program – whether it should have a prevention/detection or recovery emphasis.

## 3.1.4. Budgetary support

Once the costs of the business risks have been assessed and the related control objectives have been developed, management can determine the appropriate continuing budget line item that will be necessary to fulfill the objectives. Failure by management to commit to the necessary control program resources will hinder the development of an effective program.

![](/api/attachments/QPB3S4D5/fulltext/images/bc00f53cb80773565c79dcd89c001fe78229001fa34bd0b7bfb62c3d9ba6c802.jpg)  
Fig. 2. Technical infector controls.

In general, budgets for the control program should include the costs for employee hiring, special training, and conference attendance. Budgets for prevention/detection controls should consider the purchase of commercial infector prevention/detection software packages, a quarantine computer system to screen new or transferred software, system vendor assistance, and independent auditor or outside contractor assistance. Budgets for recovery controls might include the purchase of special software utilities, spare hardware components which an infector might damage, an isolated infector training computer, and disk inventory software. Also, additional system vendor, independent auditor, or outside contractor assistance may be required to help with infector planning or to perform searches for existing infectors.

## 3.1.5. Assign infector responsibilities

Infector program responsibilities need to be assigned to several distinct persons or groups $[1,12]$ and some authors propose formal infector committees $[21]$ . First, technically competent, trained employees must be assigned responsibility to develop the infector control program itself. The internal auditors, EDP auditors, or external auditors should evaluate the progress made in planning for it. Finally, management must assume the responsibility to appraise progress with regard to the original planning documents and milestone schedules, to insist on periodic progress reports, and to determine whether original objectives are being met.

The responsibility should be designated for providing user education concerning the risks, effect, and impact of infectors, and deciding on proper procedures to follow or persons to notify if an infector is suspected. Those persons who will implement the recovery procedures should be preassigned authority to act immediately upon suspicion of an infection. Auditors should also initiate unannounced infector recovery exercises to test the state of the recovery capability.

## 3.1.6. Employee training

Training will probably be needed for infector control program planners and implementors. However, it might also be required for internal or

EDP auditors in order for them to assess the success of program progress or the design or operational effectiveness of the specific control and recovery procedures.

Users of the systems might also require training, since they will be expected to recognize and announce the likelihood of an infection. Also, the users and certain levels of management should be made aware of the severity of possible infector impacts and how to cooperate with recovery personnel once an infection is confirmed.

## 3.1.7. Operational management policies

For any infector prevention program to succeed, several key management policies will need to be developed and made known to all employees. To support prevention/detection, management should forbid employees to develop, transfer, install, or operate unapproved new software on the organization's computers. This will be particularly difficult in the arena of end-user programming and because of easy access to 'freeware', but it is essential to provide controls for a strong infector prevention program. This policy is particularly important when programs will be available across a local area network (LAN) over which some infectors could spread extremely rapidly. A centralized quarantine/isolation computer should be designated to test and inspect all new software, as well as programs or data files being transferred between computers. Policies should require employees to be especially diligent for and to report unusual/inconsistent operational effects or computer-generated results.

To support recovery, policies should require end users to shutdown the computer (including removing on-board batteries that would normally keep portions of memory alive when the power is turned-off) [24]. End users should then notify infector recovery employees, comply with recovery procedures (and exercises), provide uninhibited access to all systems and disks that have potentially been exposed to the infector and not restart computer operation until complete infector eradication has occurred and the system has recovered.

## 3.1.8. Obtain outside assistance

If management feels that in-house technical abilities are lacking, then a concerted effort should be made to obtain help from outside.

External auditors may be able to assist by performing the actual infector control program development and training, by reviewing program planning and progress, or by performing a search for existing infections $[17]$ . Separate independent contractors may be available if the external auditor is not sufficiently qualified $[3]$ .

Since some infectors are computer system or software package specific, the hardware or software vendors for such products should be required to provide notice of infections identified at other customer sites and to recommend protection or recovery procedures. Vendors may also be able to provide hardware or software tools to prevent/detect infections or to help in recovery from infections. The efforts by IBM to make available a low cost filter for the “Columbus Day” virus is a good example.

Common hardware or software user groups may prove invaluable as media of information exchange on prevention, detection, or recovery experience. Also user groups can exert pressure on reluctant vendors to cooperate with infector program efforts.

Finally, organizations may have to acquire special EDP insurance coverage to reimburse losses associated with business interruption or loss of use of the computer $[5]$ . Insurance companies may be able to make recommendations for prevention, detection, and recovery, or even perform risk evaluations.

## 3.2. Technical controls

Technical controls tend to be infector or computer system specific. These would be carried out by technically competent non-management personnel. They include installing appropriate software safeguards, developing protection-oriented computer operational procedures, regularly reviewing the content of disks, procuring necessary infector isolation computer systems, testing software for evidence of an infection, stocking backup hardware components, preparing the facility for the eventuality of an infection, and building/exercising plans for system recovery.

## 3.2.1. Install software safeguards

Software safeguards generally relate to prevention/detection objectives. The most obvious software safeguard is to run operational systems under the protection of a commercial infector prevention/detection package. However, there is no single commercial package that can prevent every infector variation from damaging systems, although some packages are capable of protecting systems from several different types of infectors or detecting system events common to different infectors. However, packages may erroneously interpret legitimate system events as the effect of a potential infector. This type of error may be better than not noticing a real infection; however, some sites have been ‘burned’ unnecessarily and ceased using such packages [20].

Program flow monitors (PFM) have been employed as watchdog co-processors to look for unexpected program behavior $[13]$ . Such approaches require modification of compilers and linkage editors to compute primitive polynomial signature values for program code sections between points in a program where branching operations occur. If the program branches early or late (perhaps due to an infector), the polynomial signature will differ from a stored signature value and execution can be aborted.

In concert with protection packages, it is recommended that other software safeguards be used. First, for program and data files which should not normally be altered during processing, the file attributes should be set to “read only”. On removable disks, the write-protect tab should be used. For hard disks, a utility such as WPHD.COM should be used to write-protect critical disk areas. Using add-in boards to prevent an application program direct access to hard disks is another good practice $[10]$ .

The strongest (and most expensive) protection is to place executable programs and read-only files in read-only memory. This would include ROM semiconductor devices or optical, laser written disks (write-once/read-many disks) [4].

## 3.2.2. Computer operational procedures

Standardizing certain operational procedures will prevent further spread of an infector and facilitate its detection. For routine operations, such as FORMAT or COPY, end users should not key the system commands directly. Instead, batch files can be built to include system commands and also check disk (CHKDSK) and file compare (COMP) commands that will reveal hidden files; these can ensure that files are copied exactly onto the destination disk as read. Similar batch files containing CHKDSK and COMP could be used for system start-up (AUTOEXEC.BAT).

Besides making program files read-only, end users should have no filenames with the extensions .COM or .EXE on their disks (in an attempt to fool general executable program infectors). Instead, when a program is executed, it should be invoked via a batch file that contains commands to rename the program files before and after they are executed.

## 3.2.3. Periodic reviews of operational systems

One strong detection control is to develop a regular schedule that investigates changes in operational systems. Standardized procedures can be built to create routine listings of the contents of disks. These should provide a variety of reports sorted by filenames, filename extensions, file creation dates, file sizes, subdirectories, and other parameters. They would reveal new files, deleted files, changed filenames, duplicate files with different extensions, unusual new filenames, changed file sizes, changed/illogical dates, and other characteristics that might indicate the presence or the effect of a computer infector.

Checkdisk programs can also be used to reveal hidden files or unexpected new 'bad' tracks on disks (infectors sometimes hide in tracks that have been marked as "bad" in the disk directory). Reviews of every computer system could be made on a rotation basis and all software being transferred between computers should be inspected.

Some infectors will not alter the host program file's size or date/time of last update, even though the content of the program file has been altered due to the placement of the infector code inside the host program. Two means are available to discover such infections and both require the organization to program or acquire specific utility software. First, a utility program can compare the executable program file byte-by-byte against a write-protected copy and signal if any difference exists. A slightly different (and faster) approach is suggested by Davis: Before being introduced into production, a utility program scans every byte of the executable program file, inspecting one bit of each byte. If the bit is “1”, the utility program increments a counter. The counter becomes a checksum and such checksums for all program files are retained on a write-protected disk. If an infector invades a program, it will change some of the bytes and, therefore, change the bit patterns. On a rotation basis, or before a program is executed, the utility program compares a newly computed checksum against the write-protected checksum, announcing any difference.

## 3.2.4. Isolate / identify infectors

Such a checksum program will not support recovery, since it only indicates that changes have occurred in a program. On the other hand, the byte-by-byte comparison program may help isolate where the infector has been placed within the 'host' program and aid in its removal.

Another approach to isolating illicit code to facilitate recovery is to use Garnett's selective disassembly. Most infectors perform two functions involving a conditional test to determine if: (1) conditions warrant performing the damage – a trigger; and (2) a potential 'host' program has already been infected or not – a decision to spread the infection. Once a program has been found to be infected, a specially written program can search the executable program for conditional statements and selectively disassemble (decompile) surrounding executable code back to source code. This code can then be analyzed to help isolate, identify, and remove the infector.

Finally, if an infector is known to exist or has been announced to activate at a specific date/time (as with several infectors), often the actual code and placement within the host program is known in advance. The site can test for the possible infector by: Manually inspecting the code, performing selective disassembly, isolating and running suspicious 'host' programs with an accelerated system clock, or installing vendor packages directed at removing that infector.

## 3.2.5.Quarantine system

A computer should be designated solely for infector prevention, detection, and recovery exercise/training. Some infectors attack specific commercial vendor packages. On the quarantine system, one should install all operating systems, utilities, network software, routine business packages (spreadsheets, databases, word processors, etc.), copies of significant data files, and any files that would be at risk on operational computers. Also, it is a good idea to install an infector detection package (or packages).

To support prevention/detection, all new software, whether developed in-house or acquired from outside, should first be executed on this quarantine system, as well as test any programs or files being transferred between computers within the organization. To support recovery, the quarantine system can be used to exercise recovery plans, train recovery personnel, or develop recovery procedures by installing and activating infector simulators or actual infectors. Using an isolated quarantine system places production systems at no risk for these activities.

## 3.2.6. New software acceptance

The following procedures principally support prevention/detection objectives. The software purchasing function can be centralized and software ordered only from sources on an ‘approved’ vendor list. Purchased software should only be accepted in vendor sealed packages. When possible, pre-compiled programs should be avoided. Software should be accepted only in its source code form (eg., COBOL, FORTRAN, etc.) and then visually inspected for unusual program instructions or comments and compiled on the quarantine system. For pre-compiled programs, a commercial decompiler (disassembler) can determine if the program contains suspect DOS write calls which appear inconsistent with the program’s stated purpose.

When de-archiving (uncompressing) files received from an external source using ARC programs, special utilities can be used to trace file paths and inspect the content of a disk before the de-archival programs are executed. Files should be de-archived only after a cold boot is performed from a write-protected DOS and utility disk.

All new software should be tested repeatedly on the quarantine system in order to detect infectors which activate only after a fixed number of executions $[14]$ . Using an accelerated system clock will help detect infectors that incubate and activate only at a certain date/time or only after a time delay from first being introduced $[9,20]$ . Some infectors are publicized to activate at some future date/time; therefore, the quarantine system's clock can be adjusted accordingly. Research or training for infector control personnel will reveal the system impacts most frequently encountered.

## 3.2.7. Hardware backup components

A sufficient stock of removable disks should be available to accomplish infector recovery procedures. Infectors have been known to damage disks and disk drives physically by changing rotation speeds. For this reason, it is necessary to stock spare removable disk drives and hard disks. Some infectors damage other computer components; for example, one virus adjusted the refresh speed for the computer monitor, resulting in its overheating. It may be advisable to also stock replacement monitors and key computer boards.

## 3.2.8. Prepare the facility

To prepare for the eventuality of an infection, a series of steps must be taken to ensure that infector eradication is possible and that the system can be returned to its pre-infection state. First, the following tools should be acquired: File utilities which physically remove unwanted files versus only removing/marking file directories; a bulk degaussing (erasing) device to completely erase removable and hard disks; and special utilities to inspect disk tracks, sectors, and file allocation tables.

Next, the following documents should be established and maintained: A numbered inventory of disks given to employees; an inventory of all data files, batch files, utility programs, application programs, compilers, etc; a listing of all directories, subdirectories, and paths.

Finally, procedures should be developed to provide for adequate backup. A simple stick-on tab (or sliding the plastic switch on a 3.5" disk) will write-protect all original disks containing vendor packages, operating system software, network software, application source code programs, compilers, linkage-editors, runtime environment software, utility programs, and original test data used to accept application programs. It is advisable to maintain up-to-date write-protected copies of all batch files, encrypted user ID/password/permission files, major data files identified by the risk appraisal, and transaction files which update master data files. The facility should establish a regular pattern to refresh backup files containing data which changes and have sufficient depth to the dates of backup copies to be able to recover from an uninfected copy.

Archiving write-protected original software vendor disks obviously facilitates system recovery.

However, this practice may also provide a means to isolate the origin of an infector and provide redress through legal processes. Criminally charging someone for an infector or a computer crime is not new; however, civil suits are new and the courts have yet to really address this issue.

## 3.2.9. Build / exercise recovery plans

The final step is to write detailed recovery procedures so that personnel can accomplish recovery quickly and clearly. Separate plans may be needed for different types of computer infectors and the plans should be detailed and precise. Simply stated, recovery plans should address the following issues: (1) rebooting from write-protected, uninfected disks; (2) performing disk reformatting; (3) restructuring directories, subdirectories, and paths; (4) replacing programs and data files, including program recompiling procedures; (5) retesting programs; and (6) inspecting disks for infector copies. Plans should also be exercised in advance, so that personnel are familiar with the plan and can be assured that the procedures work properly.

4. Determining the infector control program emphasis

## 4.1. Threats versus risks

A total infector control program may appear complex. and potentially costly. Some argue (perhaps legitimately) that a single infection of an unprepared system could prove more costly, however. The unprepared organization is more likely to experience significant system down time. As a result of an attack, the organization could incur the cost of an expert brought in on an emergency basis to isolate and eradicate the infector. Even if such efforts were successful, the organization could still suffer from damage to (or irreversible loss of) important business data. It would be naive to argue that the infector problem should be ignored. This is especially true when the existence of an infection may violate statutes concerning information privacy and security. California, for example, mandates security standards for state-maintained programs and data. Also, standard EDP insurance policies may not cover losses from infectors deliberately introduced by end users or costs associated with business interruption. Losses, even if covered, may be large to an organization, but may still be less than insurance deductibles.

![](/api/attachments/QPB3S4D5/fulltext/images/4973b609bfed02f890ed1676b5d163da2b1c344715e6e18f751b9f00021e2374.jpg)  
Fig. 3. Infector threat vs risk matrix.

However, all organizations face the very real problems of scarce resources. As with other business decisions, resources should be applied in a manner which achieves the greatest benefit. Even in the area of internal controls over accounting data, auditors operate under the principle of “reasonable assurance”, that is, the cost of a control should not exceed the cost of the error or irregularity being controlled. Certainly, where no risk exists, no control is needed.

With respect to computer infectors, every system is inherently at some risk. Also, every system is threatened (vulnerable) to some degree or other. However, not all systems are equally threatened, and not all systems would suffer to the same degree if an infection occurred. See Figure 3.

## 4.2. High versus low threat

The threat of an infection reflects the ease with which it could enter the system and the speed with which it might spread. Organizations experience a greater threat if the system is primarily stand-alone microcomputer-based, there is considerable end-user programming, software can be introduced from uncontrolled sources, software can be transferred easily between computers within the organization (via shared disks or a local area network), there are multiple copies of the operating system, and 'booting' (system startup) routinely occurs from a variety of removable disks. A 'high threat', organization represents an increased potential for infection and the undiscovered spread of an infector, thus a 'high threat' organization would emphasize controls which relate to prevention and rapid detection.

A ‘low threat’ organization is one with standardized software, centralized programming with an emphasis on thorough testing, multi-user files and programs, a single operating system copy, and system ‘booting’ is confined to one computer (even if there are multiple microcomputers attached). In such systems, the chance of unapproved software entering the system are reduced. Also, organizations are at less risk when each end user has responsibility for his/her own machine and does not share computers, or where disks are seldom swapped between computers [9].

Note that no organization is at ‘no threat’ from infection. Even a ‘low threat’ organization may not be protected from intentional actions of a disgruntled programmer [15]. While Figure 3 does not stress an infector program for the ‘low threat–low risk’ quadrant, something should be installed, perhaps with an emphasis on recovery controls.

## 4.3. High versus low risk

Risk reflects the costs associated with an infection. An organization with a high risk would suffer high costs from system ‘down’ time, for alternative computer capabilities, due to loss of (or damage to) stored data and programs, and for the recovery operation. A ‘high risk’ organization reflects an increased urgency to recover from a computer infector, thus a ‘high risk’ organization would emphasize controls which relate to recovery operations.

‘High risk’ organizations are those with strategically important information systems, where ‘down’ time results in lost service to customers and reduced competitive advantage. But, strategic importance is not the only factor. If unique computer hardware requirements are involved (large systems, dedicated communications, or unusual hardware components), the organization may find it difficult to transfer operations to other locations or to other computers within the organization. ‘Low risk’ organizations exhibit the opposite characteristics. Systems are small and non-unique or sufficient redundancy exists. Little strategic importance may exist with the computer systems, thus, there is less urgency to accomplish recovery on any single infected system.

## 5. Conclusions

We have discussed the aspects of a computer infector control program that organizations may implement and have identified the control emphasis needed, depending on information system characteristics. Organizations with a serious interest in controlling infection must take steps to prevent an infector's introduction and limit its spread. They must continually prepare for recovery, should prevention fail. However, placing the emphasis on prevention or recovery is driven by a number of factors that affect the cost of the control program and, therefore, alter its objectives.

## References

[1] Alavi, M. and Weiss, I. “Managing the Risks Associated with End-User Computing”, Journal of Management Information Systems, Vol. 11, No. 3, Winter 1985–1986.

[2] Bidgoli, H. and Azarmsa, R. “Computer Security: New Managerial Concern for the 1980s and Beyond”, Journal of Systems Management, October 1989, pp. 21–27.

[3] Cullen, S.W. “The Computer Virus: Is There a Real Panacea?”, The Office, Vol. 109, No. 3, March 1989, pp. 43–46.

[4] Davis, R. “Exploring Computer Viruses”, Proceedings of the 1988 Fourth Aerospace Computer Security Conference, IEEE Computer Society Press, Washington, DC, December 12–16, 1988, pp. 7–11.

[5] Ellis, A.W. "Computer Viruses: Working Out the Bugs", Best's Review: Property / Casualty Insurance Edition, Vol. 90, No. 1, May 1989, pp. 84–88.

[6] Garnett, P.D. “Selective Disassembly: A First Step Towards Developing a Virus Filter”, Proceedings of the 1988 Fourth Aerospace Computer Security Conference, IEEE Computer Society Press, Washington, DC, December 12–16, 1988, pp. 2–6.

[7] Gerrity, T. and Rockart, J. "End-User Computing: Are You a Leader or a Laggard?", Sloan Management Review, Summer 1986.

[8] Hafner, K. “Is Your Computer Secure?”, Business Week, August 1, 1988, pp. 64–72.

[9] Herrick, E. “Computer Viruses: Prevention is Better than Cure”, The Accountant’s Magazine (UK), Vol. 93, No. 992, March 1989, pp. 24–25.

[10] Jones, L.G. “Computer Viruses: Threat or Media Hype?”, The EDP Auditor Journal, Vol. III, 1988, pp. 25–32.

[11] Joseph, G.W. “Computer Virus Prevention and Detection Planning”, Journal of Accounting and EDP, Vol. 5, No. 4, Winter 1990, pp. 4–8.

[12] Joseph, G.W. “Computer Virus Recovery Planning – An Auditor’s Concerns”, Journal of Accounting and EDP, Vol. 6, No. 1, Spring 1991, pp. 26–30.

[13] Joseph, M.K. and Avizienis, A. "A Fault Tolerance Approach to Computer Viruses", Proceedings of the 1988 IEEE Symposium on Security and Privacy IEEE Computer Society Press, Washington, DC, April 18–21, 1988, pp. 52–58.

[14] Liebman, R.H. and Walters, G.Q. “Computer Viruses: A User’s Guide”, Florida CPA Today, September 1989, pp. 40–43.

[15] Maher, J.J. and Hicks, J.O. “Computer Viruses: Controller’s Nightmare”, Management Accounting, Vol. LXXI, No. 4, October 1989, pp. 44–49.

[16] Mische, M.A. “Computer Viruses – The Problem and the Legal Implications”, Computer Litigation News, Vol. I, No. 1, April 1989, pp. 5–8.

[17] Perry, W.E. “Recognizing and Controlling Computer Viruses”, Journal of Accounting and EDP, Vol. 5, No. 1, Spring 1989, pp. 54–56.

[18] Price Waterhouse, The Computer Virus Handbook, Price Waterhouse, 1989.

[19] Roberts, R. Computer Viruses, COMPUTE! Books, Greensboro, NC, 1988.

[20] Schneider, W. "Computer Viruses: What They Are, How They Work, How They Might Get You, and How to Control Them in Academic Institutions", Behavior Research Methods, Instruments & Computers, Vol. 21, No. 3, April 1989, pp. 334–340.

[21] Spaul, B.J. “Protect and Survive”, Accountancy, Vol. 103, No. 1148, April 1989, pp. 146–147.

[22] Toigo, J.W. “An Overview of Computer Viruses”, Journal of Accounting and EDP, Vol. 5, No. 2, Summer 1989, pp. 21–29.

[23] United Press International, “AIDS Disks Hide ‘Worm’ That Eats Data”, The Tampa Tribune, December 21, 1989, p. 11-B.

[24] Zajac, B.P. “Computer Viruses Can They Be Prevented?”, Computer Law and Security Report, Vol. 5, No. 1, May–June 1989, pp. 18–21.
