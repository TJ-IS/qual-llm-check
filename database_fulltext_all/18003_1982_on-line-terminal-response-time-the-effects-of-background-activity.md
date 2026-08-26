---
otero_id: 18003
otero_key: "2QYHFRHY"
title: "On-line terminal response time: The effects of background activity"
authors: "James H. Conklin; Malcolm H. Gotterer; Jon Rickman"
year: "1982"
journal: "Information & Management"
doi: "10.1016/0378-7206(82)90023-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On-Line Terminal Response Time: The Effects of Background Activity

James H. Conklin
15 Olden Street, Princeton, NJ 08540, USA

Dr. Malcolm H. Gotterer

Florida International University, College of Arts & Sciences
Department of Mathematical Sciences, Tamiami Campus, Miami,
Florida 33199, USA

![](/api/attachments/2QYHFRHY/fulltext/images/4415e4a901daf59bfcfd15e2572d6ac1325b7d6056a7acad5a12c3fe3edfaff8.jpg)

and

James H. Conklin is currently a consultant to Bell Laboratories and to Southern Bell. His assignments at Bell Laboratories have included extensive research and development in the area of programmer productivity, man-machine interface using screen based interactive terminals, and advanced systems architectures to support distributed office automation systems.

Dr. Jon Rickman

He has also been a systems programmer for the International Ladies Garment Workers Union where he was

Computer Science Dept., University of Missouri, Maryville, MO 64469, USA

This paper reports on a set of experiments to determine the effects on the response time of an on-line system when different types of jobs run in the background partition. Since many applications may be better served by an on-line system but do not justify a dedicated system, it is frequently necessary to run batch jobs in the background partition of a computer supporting an on-line system. Substantial differences in terminal response time were observed depending on what jobs were scheduled in the background partitions. The computer manager should be aware of these factors when scheduling such batch work.

Keywords: Response Time, On-line System, Background Activity, Batch Processing.

responsible for bringing up and tuning the performance of an online financial transaction system. His responsibilities also included the human engineering of the displayed information presented to their terminal operators.

![](/api/attachments/2QYHFRHY/fulltext/images/71924dfe6e1350c96364b9e4d012df4404802af547353f7936d6c116a05c7430.jpg)

Dr. Malcolm H. Gotterer is presently Professor of Computer Science at Florida International University. He has previously taught at Pennsylvania State University, Georgia Institute of Technology, University of California, and Berkeley. During the year 1964 he was Post-doctoral Institute Fellow at IBM Systems Research Institute, and in 1968-69 he was Fellow in Computer Science, The John Hopkins University. He is a member of the AFIPS Pro-

He is a member of the AFIPS Professional Certification Committee,

AFIPS Committee to the IFIP Administrative Data Processing Group, a member of the Editorial Board of Management Informatics (?) and also the Editorial Board of Computers and People. He has been Chairman of the ACM Special Interest Group on Computer Personnel Research (SIG CPR), and has been active in the Association for Computing Machinery, IFIP Administrative Data Processing Group, and the IEEE Computer Group. Dr. Gotterer has served as a National Lecturer for the Association for Computing Machinery and Data Processing Management Association. He is a consultant to various U.S. Government agencies, private businesses, and non-profit organizations. Dr. Gotterer is on the Board of Directors of EDP Update, Inc. and Vanda Corporation.

He has published widely in the areas of computers and computational problems. His papers have been published in over twenty journals and books; he is also author, co-author, or editor of six books. He has presented papers at technical conferences in many parts of the world.

Dr. Gotterer received his D.B.A. from Harvard University in 1960 and is listed in Who's Who in the East, Vol. 11, 1968-69, Vol. 12, 1970-71; American Men and Women of Science, 14th Edition, 1979; and Leaders in American Science, Vol. VIII, 1968.

![](/api/attachments/2QYHFRHY/fulltext/images/cd51d943e1843741b0f48762a933c9d2499515c639709003a32d7033a1f538e4.jpg)

Dr. Jon Todd Rickman has been actively involved in the field of information management for nineteen years. His experiences include management with the Southwestern Bell Telephone Company, university instruction, research, and managing computing resources at three universities. He received his Ph.D. in Computer Science from Washington State University in 1971. He is currently the Director of Computing Services at Northwest Missouri State University where he has developed a sophisticated network of micro, mini, and mainframe computing systems.

## 1. Introduction

This study of terminal response was conducted to determine the impact of background jobs on response times. In many cases it is not economically feasible to dedicate a computer system to an on-line system. Rather it is necessary to use the background partition for batch processing while the on-line system is in operation.

A common assumption of computer managers new to an on-line environment is that jobs run in background will have a small effect on the on-line system. In light of the need for good response time for the on-line system this assumption is worth investigating.

This study measures on-line/background interactions. Actual measurements were taken from the small system described below.

## 2. The Hardware Environment

The hardware consisted of:

1. An IBM 370/125II with 256K bytes of main memory and one multiplexer channel;

2. Six 3340 winchester disk drives with 70 mega-bytes of storage each;

3. An IBM 3704 communications controller;

4. Several IBM 3601 communications controllers with 64 K bytes of main memory and a floppy disk drive each.

The 3601 controllers interfaced to the 3704 via a 1200-baud SDLC link. Each 3601 controller supported two 4800-baud SDLC local terminal loops. Each loop consisted of 8 terminals, 4 keyboard plasma screen display terminals equipped with magnetic strip readers, and four passbook printers.

## 3. The Software Environment

All system software was supplied by IBM. It consisted of the packages described in Table 1.

## 4. The On-Line Application

A widely-dispersed network of terminals was located in supervised locations with trained operators who used the terminals to complete financial transactions for individuals coming to the operators. Each individual carried a passbook with a magnetic strip attached to its cover with his or her identification number and other basic information encoded in the strip. Transactions normally followed the following sequence of steps.

1. The passbook strip was read by the terminal and status information from the host computer masterfile was shown on the plasma display screen;

2. A transaction key was depressed and a money transaction amount was entered;

3. The transaction was verified and the data was stored on the 3601 floppy disk;

4. The transaction was printed on the individual's passbook by the terminal;

5. The magnetic strip was updated and the pass-book was returned to the user;

6. A log of the transaction was sent to the host computer to be stored on a log file.

All updates to the host master file were done as a batch procedure at the end of the day using the log file.

The host master file was not distributed to the 3601 minicomputer because of the need for central management control of the database.

## 5. Communications Links

There are two communications links of concern in this system. Both use SDLC as the line control discipline. The link between the 3704 and the 3601 was initially 1200-baud and was later increased to 2400-baud. Within each local loop a 4800-baud line was used.

Table 1

<table><tr><td>Package</td><td>Name</td><td>Power</td><td>Function</td></tr><tr><td>Operating System</td><td>DOS/VS</td><td>56 K</td><td>Provides basic operating system support with paging and two batch partitions.</td></tr><tr><td>Spooling System</td><td>POWER</td><td>156 K</td><td>Provides print spooling support.</td></tr><tr><td>Terminal Applications Management</td><td>CICS</td><td>500 K</td><td>Provides terminal support to the applications for the transaction oriented terminal network.</td></tr><tr><td>Terminal Management</td><td>VTAM</td><td>0 K</td><td>Provides terminal support to CICS. This runs as part of CICS and its size estimate is included with the CICS figure.</td></tr><tr><td>File Management</td><td>VSAM</td><td>272 K</td><td>Provides indexed retrieval to the file system.</td></tr><tr><td>Network Management</td><td>NCP</td><td>0 K</td><td>Provides support for the control of the network. This package runs in the 3704, which is a separate processor with its own memory.</td></tr><tr><td>Terminal Software</td><td>TAP</td><td>64 K</td><td>This system was written in-house and runs in the 3601 controller. It manages the tellers&#x27; work stations and provides for a stand-alone transaction environment. The only work that the host system does during a normal session is to access the database once to retrieve the customer&#x27;s record from the main database.</td></tr></table>

## 6. Measurement of Response

Terminal response time was defined as the time interval from the time the operator depressed the transmit key until the first response character appeared on the screen. Measurements were taken with a stop watch. This approach is in agreement with the NBS guidelines for measurement of response time [1].

## 7. The Background Programs

The six programs used for these experiments were programs in actual use that represented the spectrum of typical activity in the system. A brief description of the programs selected follows:

1. Assembly. The assembly used was a 5000-line program for the 3601. It was unusual to the extent that each line accessed a macro stored on a disk drive.

2. Cobol Compile. The program selected was approximately 1000 lines. Its intended use was a typical file maintenance operation. The compile phase was the basis of the test.

3. Link Edit. This was the link edit phase for the Cobol program above.

4. Print. This was the output from the print queue of the POWER spool file.

5. Sort. The sort selected was a disk sort of approximately 66,000 fixed length records, 150 characters long. The system sort was used.

6. CPU Bound Loop. For experimental purposes a tight loop was written in assembler that did no input or output. This was used only for the purpose of the experiments.

## 8. The Experiments

The experiments consisted of taking 10 observations for each of the combinations studied. The 10 observations were averaged to produce an average response time which is the figure reported below unless explicitly stated otherwise. Since the experiments were being conducted in a production environment it was not possible to study all combinations of the six jobs. The experiments were run during the evening shift when the on-line system was not otherwise being used. The experiments are discussed below and are summarized in Table 2.

## 8.1. No Background Jobs

Response times were taken for an idle machine in order to determine a base line for the rest of the experiments. The average response time was 3.4 seconds for the 1200-baud link and 1.94 seconds for the 2400-baud link. This decrease of 1.5 seconds was constant over all experiments and is attributable to character transmission time over the 3704 to 3601 link.

## 8.2. One Background Job

Printing from the POWER output spool file had minimal effect on terminal performance. This is expected since POWER uses almost no system resources: the printer is relatively slow and few disk accesses and few cpu cycles are required to keep it running at speed.

When the assembly was run in background, terminal response degraded to 4.8 seconds. The assembly used a great deal of disk resources both for I/O to the macro library and for paging. Due to the large number of macroes that were required to assemble the 3601 terminal program, the assembly required a 400 K byte partition to run.

When the Cobol Compile or the Link Edit or the sort were run in the background, terminal response degraded to 4.0, 3.8 and 4.0 seconds, respectively. All three programs use about 100 K bytes of memory and as a result should cause considerably less paging than the assembly. All three programs alternate between being disk- and cpu-intensive.

When the cpu-bound job was run in background the terminal response degraded to 2.5 seconds. This job does not do disk I/O and uses almost no memory, so it should not cause paging. It is assumed that the response degradation is due to scheduling delays within the operating system. Specifically, the cpu-bound job will not be preempted until its time slice has expired.

## 8.3. Two Background Jobs

There was only the opportunity to perform two experiments using two background jobs.

When the sort was run with the cpu-bound job, the terminal response was degraded to 5.1 seconds.

Table 2  
Terminal Response Time Measurements

<table><tr><td>Program</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>Average</td></tr><tr><td>Idle</td><td>2.0</td><td>2.0</td><td>2.0</td><td>1.8</td><td>2.0</td><td>2.0</td><td>1.8</td><td>2.0</td><td>2.0</td><td>2.0</td><td>1.9</td></tr><tr><td>Assembly</td><td>6.5</td><td>6.5</td><td>6.5</td><td>2.0</td><td>6.7</td><td>4.0</td><td>2.0</td><td>3.7</td><td>4.7</td><td>6.3</td><td>4.8</td></tr><tr><td>Cobol Compile</td><td>5.0</td><td>3.7</td><td>3.5</td><td>3.0</td><td>3.0</td><td>3.2</td><td>3.0</td><td>8.3</td><td>3.5</td><td>3.7</td><td>4.0</td></tr><tr><td>Link Edit</td><td>6.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>5.5</td><td>3.3</td><td>8.3</td><td>3.7</td><td>2.0</td><td>3.1</td><td>3.8</td></tr><tr><td>Power Print</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>1.9</td><td>2.0</td><td>2.0</td><td>2.0</td><td>1.9</td><td>2.0</td></tr><tr><td>Sort</td><td>4.5</td><td>4.0</td><td>4.3</td><td>4.5</td><td>3.7</td><td>3.9</td><td>4.5</td><td>3.3</td><td>3.8</td><td>3.7</td><td>4.0</td></tr><tr><td>CPU Loop</td><td>2.0</td><td>2.5</td><td>2.0</td><td>2.8</td><td>2.5</td><td>3.2</td><td>2.0</td><td>2.3</td><td>3.1</td><td>2.0</td><td>2.5</td></tr><tr><td>Sort &amp; Compile</td><td>8.5</td><td>7.7</td><td>5.0</td><td>4.0</td><td>4.5</td><td>7.5</td><td>4.5</td><td>7.5</td><td>3.7</td><td>4.0</td><td>5.7</td></tr><tr><td>Sort &amp; CPU Loop</td><td>5.8</td><td>4.7</td><td>5.5</td><td>5.0</td><td>5.0</td><td>5.0</td><td>5.3</td><td>4.0</td><td>4.5</td><td>5.7</td><td>4.1</td></tr></table>

The worst-case response measured for this job mix was 5.8 seconds.

When the sort was run with the Cobol Compile, the terminal response was degraded to 5.7 seconds. The worst-case response measured for this job mix was 8.5 seconds.

## 9. Analysis

Our findings indicate that the response time degradation that was found when background jobs were running appears to be caused primarily by the multiplexor channel being overloaded by disk accesses.

The overloading shows up in the worst-case response time of 8.5 seconds, which occurred when a great deal of background disk I/O was in progress.

The worst-case (two background jobs both doing intensive disk I/O) scenario follows. The on-line program starts to run. It will need to do disk I/O to page itself in and to get requested data from the disk file. Everytime it does a disk access the first background job will run and do a disk access. This disk access will queue up behind the on-line program's disk-access request. At this point the first background job will stop and the second background job will run and do a disk access. This disk access will queue up behind the on-line program's disk-access request. At this point the first background job will stop and the second background job will run and do a disk access. This disk access will queue up behind the first background jobs' disk request. The on-line program will start up when its original disk access has completed and it will do another disk I/O which will be queued up after the two background jobs disk requests. Thus the on-line program's ability to access the disk is slowed by a factor of 3 even though it runs at the highest priority. Add paging contention for real memory and the response time of the on-line slows to a crawl.

One of the authors (James H. Conklin) found the same phenomenon of disk-access overload on a PDP 11/45 minicomputer running the UNIX1 \* operating system. Significant throughput improvement was gained when the swap area was moved to another device with its own controller.

## 10. Summary

What is clearly shown by this study is that for a system that has a great deal of memory contention and disk contention great care must be used if background tasks are to be run concurrently with on-line jobs.

## Reference

[1] "Guidelines for the Measurement of Interactive Computer Service Response Time and Turnaround Time." Reprint from "Federal Information Processing Standards Publication 57," dated 1978, August 1, Computer Communications Review, ACM SIGD, January 1979, Volume 9, No. 1, page 13.
