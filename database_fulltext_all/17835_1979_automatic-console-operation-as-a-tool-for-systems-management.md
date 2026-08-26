---
otero_id: 17835
otero_key: "9JD5SA5Z"
title: "Automatic console operation as a tool for systems management"
authors: "Reinhard Posch"
year: "1979"
journal: "Information & Management"
doi: "10.1016/0378-7206(79)90006-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Automatic Console Operation as a Tool for Systems Management

Reinhard Posch

Institute for Information Processing, Technical University of Graz, A - 8010 Steyrergasse 17, Austria

This paper presents a method for the modification of some built-in strategies of operating systems. The method is constructed to meet the special needs of a computer installation. Such needs are considered from the viewpoint of the site management and especially the problem of distributing existing computer power is looked at. The tool, which is mainly based on automatic operator intervention, is discussed together with other ways of meeting the given goal!. Two special examples are given to show the feasibility and to study the overall effect on the whole system. Attention is paid to the question of how much power is consumed by an implementation of such strategy modifying modules.

Keywords: Automatic operating, strategy modification, console simulation, resource partitioning

![](/api/attachments/9JD5SA5Z/fulltext/images/f1de0c8ee908a0b52496de083d0b9e1cc6da4aeaffd9c7c88e1c9ea74efb62b9.jpg)

Reinhard Posch received his masters degree in Technical Mathematics (Information Processing) at the Faculty of Science of the Technical University of Graz, Austria. There he received also his PHD in 1976. He is engaged now at the Institute for Information Processing where his main aim is operating system development and lecturing Operating Systems. He is also one of the leaders of the project group 'Performance Evaluation and System Partitioning' which is a common research project of the Institute for Information Processing and the Research Center Graz. Besides this he is working in terminal handling and telecommunications.

## 1. Introduction

The work of an operator at the central console of a computer can be split into two classes.

First: actions which are demanded by the system. Typical examples are: changing forms on a print station, tape- or disc-mounting, etc. In all such cases the system is in a situation, where an action is needed because of lack of automation. Such actions can be viewed as external processes which are initiated and synchronized via the console. But because the processor is the operator, the processing times vary wildly, so that a planning for such actions by the operating system is very difficult (as far as timing is concerned). Thus the type, number, and frequency of such operator interventions should be as low as possible; e.g., output spoolers that sort the printouts according to forms, printer positioning and systems that recognize premounted tapes, and automatic tape reel searching and mounting improve the situation substantially.

Second: actions are necessary at most installations to manage the overall work that special rights of some groups of users are preserved while maximum of throughput is achieved [1]. The action of the operator will not result from an understanding of the situation but will be given by the management or by the operating systems manager and will be executed in a given way. As an example, the priority of a group of users will be raised whenever they are not granted resources for a long time during processing. Such requirements cannot be performed by an operator without machine aids.

Whereas the first group of operator interventions is necessary due to technological limits, the second group of actions is caused by systems philosophy. Built-in strategies often do not meet the expectations of management.

The work presented here takes a first step towards this coordination of system strategies and management. The method consists in adding — logically, but not in the sense of coding — a module to the operating system. This module behaves like an operator; it reacts quickly according to given built-in strategies of the system that can be tailored to any special needs. Physically, the module runs as a separate job and is separate from the operating system so that all warranty of the manufacturer remain untouched.

An application of the method has been implemented for interactive processing using an operating system that was not designed to support timesharing or interactive processing [3]. In this application, the goal of using standard supervisor calls and instruction repertoire could only be partially reached, because it was necessary to use system tables to obtain status information quickly; however, a second example shows that influence on system strategies is possible for an ordinary user program.

## 2. Modifying strategies

The operating system and application software are usually configured at each site, thus the system is not the same at each site and depends on the hardware and workload. This adjustment of the operating system is done by a system generation procedure (see fig. 1). The manufacturer delivers a general system of all possible parts that can be selected or modified.

![](/api/attachments/9JD5SA5Z/fulltext/images/ff9dbd374f19c1b039f97a5c480fb7aff366967c8e91f6739dde1e7718c0c980.jpg)  
Fig. 1.

![](/api/attachments/9JD5SA5Z/fulltext/images/f8ef3d908bf73bc6f4c562cef9f8e613203c4c5841dea5ec94173231cda28a9b.jpg)  
Fig. 2.

The installation manager defines, via parameters, those installation dependent needs. If necessary, local corrections are also embedded at this step. A special software processor (the 'system generator') produces an executable (bootable) system from these three components (the general system, the hardware and software parameters, and the local corrections).

The system generator is generally, however, limited in scope, allowing only certain strategic decisions. Let us suppose we wish to introduce a quick-job-queue with a very high priority for jobs with resource consumption below some limit. There are two ways. The first way involves enhancing the parameter set and adding management definitions. But this parameter set is no longer processable during system generation. Therefore either system generation has to be modified or a preliminary pregeneration phase must be installed to transform the management definitions into local corrections. This separation from the system generation is very useful because it is not then necessary to modify the system generation procedure and the processor, and thus the manufacturer delivered system is not altered (see fig. 2).

Such a method unfortunately cannot lead to a location independent procedure for the pregeneration phase since local corrections of the coding of the operating system have to be generated. This means substantial expandeture of effort.

![](/api/attachments/9JD5SA5Z/fulltext/images/8008425c5d1cb59d99605eaa85c9c9e069c44a9cab99b48bb80fb59952056885.jpg)  
Fig. 3.

The second way of modifying system strategies is to leave the system unchanged and correct the actions of the operating system online. Such a method is, however, only feasible for minor corrections. This procedure requires the operator to look what the system is doing and then to correct if necessary.

In the work discussed here, an attempt was made to find a method where the operator did not need much knowledge of the code and where the method was independent of the level. Possibly a very quick and clever operator on the console could do this work by following rules. This leads to the idea of using the console interface of the operating system for initiating the correction module: a module is created which simulates console keyins and accepts parameters and management definition.

Such an organisation is shown in fig. 3, but this console interface is strongly system dependent. Two special examples are discussed to show the principle.

Our first application was on a UNIVAC 494 using the OMEGA operating system; simple interactive processing was needed. Here the console interface had to create a systems process (this operating system has a well defined way [4]) and had to generate a request packet which contained the input text as it would be keyed on a console; this input packet then had to be submitted via a special request. Of course, any such procedure should be secure, and this is its major drawback.

Our second application involved the UNIVAC 1100/81 using the OS1100 Level 35 operating system. We wished to partition resources between two user groups. It involved the simulation of a console as a device. OS1100 allows an arbitrary number of consoles which are equivalent to timesharing terminals or other devices. Via a security processor, such devices must be declared to be consoles (via the TSS timesharing security processor [4] by the system manager). However a master console must exist and must be defined at system generation time. These console devices are meant to be manually operated and connected via some dataline. One way to provide an automatic console is to have a minicomputer which behaves like a timesharing terminal and is dedicated for this type of 'operator', but this requires additional hardware. Another possibility is to connect an output line of the computer to an input line and to simulate the terminal at the UNIVAC 1100 itself, however this would again call for additional hardware. A third way is to simulate a timesharing terminal internally. The operating system on the 1100 allows communication between the remote batch and timesharing interface (RSI) and a normal user program. Thus one must define console capability for a terminal which does not really exist via TSS and simulate a terminal with this identification (see fig. 4). In this way one can use manufacturer software without modification.

![](/api/attachments/9JD5SA5Z/fulltext/images/57a043582b615fcbf16b5dbd17ff4e439432bbd1d65c05020d44848a0b60e825.jpg)  
Fig. 4.

First, using the Remote Symbiont Interface (RSI) a terminal is defined and activated using a supervisor call. This terminal may or may not exist within the system, and therefore no additional hardware is needed to limit the use of the console interface (not the use of the terminal simulation interface) by informing the Terminal Security System which user may use a special terminal as a so called 'Remote Console'. Since both the TSS and the user access to a terminal are protected by password, a security procedure results.

To obtain status information, output and feedback by the operating system is needed. This may be achieved by using the same interface the console — for system output. This, however, presents a problem, because the information must be available rapidly via this communication link, but the consol interface is built for human and not program reaction time. Thus one has to check whether the interface is capable of fast reaction and if the overhead is too large. Correction of such problems involves code modification and leads to system level dependence.

## 3. Two special applications

Here we discuss the implementation of strategy modifying modules for the two examples. The second example is more or less temporary.

## 3.1. Implementing Interactive Processing on the UNIVAC 494

There are two main problems: first, the I/O interface is not capable of interaction (the system uses spooling); second, the allocation strategies are in no way flexible, so that interactive processing is only sensible with high priority core resident programs. The first problem is discussed in [3]. Since priorities and reactions of the operating system to such priorities had to be considered of importance, the strategy modifying module had to be designed to take account of the system state i.e. its current storage assignment and processor allocation. Memory allocation was the module with most influence; it happens that CPU capacity is not a critical resource. This simplifies the priority system, so that CPU priority could be left unchanged. This is particularly important because no information is available on memory usage at the console interface the interface could not receive output. Therefore it was necessary to use internal tables of the operating system.

Here, memory allocation strategies were influenced by the deactivation and reactivation (suspension and resumption) of jobs. These commands are available via console interface by:

## SP jobnumber J RS jobnumber J.

However, one could imagine a similar dynamic adjustment of job priorities: a concept that has been tried, but with no effect on memory allocation resulting. SP and RS had an effect which was not superposed. In addition, this interface influences not only the memory allocation but also the processor allocation, in the negative sense, since a job which has not all its facilities (including memory) assigned is not ready for processing. The reaction of the system on SP keyin is immediately swapping out the named job (i.e. as soon as possible). A RS keyin forces the reactivation (roll-in) of the named job, as soon as memory is available, according to its priority in the memory wait queue.

In special cases, a round-robin strategy with K active (memory granted) jobs should be implemented. To obtain the necessary information, internal tables were read. The algorithm was designed so that a change of contents of these tables during the processing period of the algorithm did not disturb the function (it would recover the table access). This is important, since the module could only be activated in a periodic way but not when the contents of the tables had changed. To be able to work in spite of that, the module has a pointer which is updated after each action. As also shown in fig. 5 one action consists of bypassing all the batch jobs and activating the next K remote jobs (in direction of the links) starting at the slice pointer. This is done if necessary by a RS jobnumber J keyin. The rest of the jobs are scanned and all further remote jobs are suspended. Due to the fact that the module runs outside the operating system and not within it, an error could occur if the slice pointer points to a non existant job. This error may occur but is detectable. The cyclic list must terminate after at most N steps where N is the number of active jobs. If not so the algorithm starts as if the slice pointer had pointed to the root. This means that the round-robin philosophy of the algorithm is slightly influenced if a job disappears during processing. At the end of the action the pointer is updated by a value of L. It turned out that this value should not exceed 1 because of systems overhead.

Possible intervals of strategy modification (as shown in fig. 6) are given by the system reaction time on console keyin. This reaction time on suspend request may in a multiactivity system cause lots of effort since many activities belonging to one task may have to be delayed. A request may (at worst) last 1.8 sec. Therefore the time between two actions of the strategy modifying module should exceed 3.6 sec. In practice an interval of 5 seconds causes insignificant measurable overhead.

![](/api/attachments/9JD5SA5Z/fulltext/images/68427ba6010de4c5f827d675e023fdb46fd6fa98123752c9b89289c059471861.jpg)  
Fig. 5.

## 3.2. Resource Sharing under OS 1100

The background of this work lies in the use of the UNIVAC 1100/81 in Graz. One machine serves two very different classes of users: the University and customers of Rechenzentrum Graz, a private association. A design decision was made to develop a partition so that each partner seemed to have a separate machine.

This general partitioning was to be implemented in the operating system. But in the meantime, some control was necessary; an example of this control shown in here is the assignment of tape-units. Similar strategies may be formulated for other resources.

Before starting, the power of the console interface and the resulting overhead had to be studied. First upper bounds were evaluated. A console was simulated to keyin as fast as the system could accept data. The frequency was therefore limited by the capability of the system to respond; between 18.000 and 20.000 requests could be processed per minute. The requests were those used to obtain information of the system:

![](/api/attachments/9JD5SA5Z/fulltext/images/e3b94a89e31c0ebdc2ba151f77517f4cf2086aec7b5ae14f466d5742f4fb32b0.jpg)  
Fig. 6.

system state

tape usage

memory usage

specific run information.

In evaluating the overhead of such activities, it was not possible to consider one run and take the time or system charge as a measure. This is because most actions are in the operating system and cannot be charged to the users' account. The overhead was therefore evaluated using the influencing module in parallel with a heavy loaded system. A jobmix which relates to a load in real life [5] was used and the difference in times between this jobmix and a similar run with the strategy module in parallel. No real difference could be measured because the frequency of interaction is small compared with the power of the consol interface, and the processing time was not a critical resource. The module did not cause any additional memory load because it could be embedded in another module, into which it fitted due to the block structured memory.

![](/api/attachments/9JD5SA5Z/fulltext/images/86002bc02c35fe216b8e2a1425d919122786932c4074dfb6c468202635f9ea0d.jpg)  
Fig. 7.

For reasons of readability the whole module except the immediate console interface was written in FORTRAN. The module is made up of a driver which determines the time intervals and calls subroutines. In the special case of tape unit allocation, the module is shown in fig. 7. For production usage, control involved more than tapes, and therefore the module was rewritten in assembler language, for efficiency. The tape control routine acquires the tape usage from the operating system and forms a table. This is used to determine the distribution of units among the users and if this distribution is not acceptable, one tape assignment is rejected – that having the shortest processing time. This action is only started if the system (or some user) is on hold due to the lack of tape facilities. This condition may be tested by keying in a system status request via the timing routine. Thus N keyins at the simulated consol where N is the number of runs requesting a tape +1 at each moment where the tape assignment was checked were necessary. This was checked once every five seconds.

## 4. Final comments

The examples show that it is possible to influence system strategies in a clear way without touching the operating system. The first example showed that the limits of such actions are reached very soon. However the application of minor strategy modification is legion. One useful example occurs if it is necessary to adapt the service to the batch processing as the number of timesharing users rises. The number of opened batch runs can be changed in order to get a good response time, even though many timesharing users coexist with a high throughput of pure batch processing.

## Appendix

The requests on a simulated console to control tape assignment at OS 1100

```csv
FS,ALL TC2,TC8 (tape assignment information)
T00 UP * RUNID/HUETT
T01 UP * RUNID/BOLT
T02 UP * RUNID/SAUPER
T03 UP * RUNID/COPY9
RC HUET (special run information)
HUETT ,0 F805PRA02/ OPEN/INCOR
DEMAND TIME = 06:00:00/00:00:00 PAGES 10000/1
CARDS = 5000/2 SIZE = 2
PROJECT = TAL
RC BOLT
BOLT ,0 B7240LCA0/ OPEN/INCOR
DEMAND TIME = 06:00:00/00:00:48 PAGES 10000/1
CARDS = 5000/2 SIZE = 2
PROJECT = TAL
RC SAUPER
SAUPER,0 B3260SRD01 OPEN/INCOR
DEMAND TIME = 06:00:00/0:00:48 PAGES 10000/1
CARDS = 5000/2 SIZE = 2
PROJECT = REI
RC COPY9
COPY9 ,A SYSTEM OPEN/INCOR
BATCH TIME 06:00:00/00:00:04 PAGES 10000/1
CARDS = 5000/0 SIZE = 13
PROJECT = SYS$
FS,ALL TC2,TC8
T00 UP * RUNID/LACK
T01 UP * RUNID/SOMM
T02 UP * RUNID/RAPPL
T03 UP * RUNID/CE
```

TM TPKON/R CE TERMINATED

## References

[1] G. Bayer, Transparency and Flexibility in Servicing the Users; Informatik – Fachberichte Nr. 2, Springer 1976.

[2] Sperry Univac 1100 Series: Operating System Installation Reference Manual, UP 8486, 1977.

[3] R. Posch, Analysis and Implementation of Remote Computing of a Group of Users (German). Technical University of Graz 1976, PHD.

[4] Sperry Univac 494: Operating System, Technical Documentation, System Documentation Univac 494.

[5] G. Gell, G. Haring, R. Posch, C. Leonhardt, The Use of a Synthetic Jobstream in Performance Evaluation, Accepted for publication at Computer Journal, Aug. 1979.

[6] S.W. Watkins, M.D. Abrams, Survey of Remote Terminal Emulators, NBS Special Publication 500-4, National Bureau of Standards 1977.

[7] M.M. Mano, Computer System Architecture, Prentice-Hall, Inc., 1976.
