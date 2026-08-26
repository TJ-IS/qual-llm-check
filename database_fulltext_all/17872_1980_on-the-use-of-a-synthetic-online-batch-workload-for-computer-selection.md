---
otero_id: 17872
otero_key: "WG9G6M9H"
title: "On the use of a synthetic online/batch workload for computer selection"
authors: "Guenter Haring; Reinhard Posch"
year: "1980"
journal: "Information & Management"
doi: "10.1016/0378-7206(80)90008-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the Use of a Synthetic Online/Batch Workload for Computer Selection

Guenter Haring and Reinhard Posch
Institute for Information Processing, Technical University
Graz, Steyrergasse 17/4, A-8010 Graz - Austria

The overall evaluation and decision process for the selection of a new computer system for the universities at Graz using a mixed synthetic online/batch workload is described. In particular the method for defining this workload for the evaluation process is explained. Furthermore the possibility of constructing assessment functions, that can be used for the comparison of different systems, is discussed.

Keywords: Computer system selection, online/batch workload, assessment functions, computer system ranking, computer system performance.

## 1. Introduction

The universities at Graz have been going through the process of selecting a new computer system by a method involving assessment of the mixed online/batch workload. This paper focusses on the description of the expected workload and its role in the evaluation process. Thus it is necessary to explain all phases of the decision process. Though the rough procedure for such a process is well established, it is important to see how each step was realized and how it depended on the previous work environment.

![](/api/attachments/WG9G6M9H/fulltext/images/77b70b30d5d88ee0f1c796c1fea2dbe2c233861e9282a22dfd361e69f30ae55d.jpg)

Günther Haring received his master degree in Technical Physics at the Faculty of Science of the Technical University of Graz, Austria in 1967. There he received also his PhD in 1970 and his "venia docendi" in Computer Science in 1975. He is engaged now at the Institute for Information Processing where he is working in the field of performance evaluation of computer systems and lecturing Principles of High-Level

Programming Languages, Software-Engineering and Computer Systems. He is also one of the leaders of the project team on "Performance Evaluation and System Partitioning" which is a common research project of the Institute for Information Processing and the Research Center Graz.

![](/api/attachments/WG9G6M9H/fulltext/images/29921447e9c96aef3437728c31f824af0a18d0b049c3218f047f7bcc8a5de4bd.jpg)

Reinhard Posch received his masters degree in Technical Mathematics (Information Processing) at the Faculty of Science of the Technical University of Graz, Austria. There he received also his PhD in 1976. He is engaged now at the Institute for Information Processing where his main aim is operating system development and lecturing Operating Systems. He is also one of the leaders of the project group "Performance

Evaluation and System Partitioning" which is a common research project of the Institute for Information Processing and the Research Center Graz. Besides this he is working in terminal handling and telecommunications. On this behalf he worked with the Research and Development group of Sperry Univac, Roseville MN during summer 1979.

## 2. Previous environment and the boundary conditions

Since user behaviour does not change rapidly, some of the usage of EDP-resources in the old system must be considered during the decision process of evaluating the new system. The old system consisting of a UNIVAC 494 running the OMEGA operating system was installed in October 1969. Only onsite and remote batch operation were available. The main applications were in research, teaching and administration (including information systems) with percentage breakdowns of CPU usage during the first six months of 1976 of 75:10:15. Due to software restrictions on the old system, about 70% of the programs were written in FORTRAN. The non-FORTRAN programs (assembler, COBOL and a special version of ALGOL) were the result of the use of those languages in introductory courses. It could therefore be assumed that the existing programs would be easily transferrable to the new system, since the FORTRAN IV compiler of the old system did not have many nonstandard (additional) features.

An essential restriction was the fact that the total cost of hardware, software and maintenance of the new system was fixed. Also, the communication net consisted of a few private telephone lines with a relatively high capacity (19.2 Kbits/sec). The different terminal points of the data net are contained in a circle of about 5 kilometers in diameter.

## 3. The overall strategy

We were faced with the goal of selecting a modern general purpose computer system with extensive software support that could be accessed in a decentralized way. These goals are typical of the general problem: the new system should eliminate those deficiencies of the existing one that are reasonable within the financial and technical constraints. Thus the deficiencies must first be listed and suitable methods found for their elimination. One method of classifying deficiencies is according to their measurability: they may be objectively measurable or structural. An example of the first is in throughput under a well defined workload. An example of the second is the non-existence of a particular compiler. Another way to classify deficiencies is by the person they affect; there are subjective flaws (felt only by some users) and there are objective ones (evident to everybody). An example of both can be found in the operation of a remote batch station, where some users want to operate the station themselves (for reasons of accessibility) and yet it is necessary to have it operated by professional personnel (for reasons of privacy).

The overall strategy must, as a first step, give a functional description of the new system, and then assure that its realization is possible. Since neither the users nor their applications will change immediately, the functional description of the new system will start without perceptible change from the present situation. Both the current situation (computer system and user community) and the future situation must be structured according to the types of deficiencies. This structuring guarantees that the objectively definable flaws as well as the personal feelings of the users will be taken into account. To determine the load, we first analysed the system logs to find the consumption of resources, and held extensive interviews with the users. For the structural component, sufficiently comparable computer centers were visited and interviewed.

Under the OMEGA operating system, system logging is structured according to single jobsteps. For each job-step, the usage and activity times as well as the type of activity are recorded for the central processor and the different peripherals. Thus for a card-reader, the number of program requests, the number of transfers, the error rate, the total number of transferred characters, the mean block size per transfer and request, and the duration of assignment are recorded. It was then assumed that an extrapolation of the recent values of resource consumption would be valid. This is discussed more explicitly in [4].

Applying this method to the single components of the system, lower bounds of the necessary performance could be obtained. The way in which users would want to consume the processing power of the new system (batch/onsite/remote, TS) and proposals for structural improvements were determined by inquiry.

Therefore the experience of other computer centers was considered by planning personnel, who also asked the users for their opinion. The inquiry therefore provided a transition from the global performance values of the peripherals to exact specifications of the devices in the terminal points of the data net. Thus we had defined:

(a) the properties of the software, and the volume of system and application oriented software;

(b) the models of operation (batch onsite/remote, TS) and their portion of the total power of the new system;

(c) the number and characteristics of tape and mass storage devices;

(d) the characteristics of the paper peripherals in the different terminal points;

(e) the kind and location of special peripherals (e.g., OC-reader);

(f) the capacity and number of transmission lines and the location of publicly accessible CRTs.

Based on these results, which fixed the configuration - at least as far as peripherals are concerned - a market analysis was performed. Offers which met the financial constraints were solicited. We believe that hardware and software compatibility will be guaranteed because all manufacturers have been required to integrate existing devices (from other manufacturers) into their system.

Systems which met these rough demands could next be evaluated. Under the aspects of measurability of the performance, this evaluation uses a run-stream which corresponds to the real application (i.e. its job profile). The aim of such a testrun is to evaluate those measurable factors which cannot be derived immediately from the technical description of the whole computer system. To prevent duplication of effort in the evaluation, only those things must be evaluated in the remainder of the process which are neither represented by the testrun nor requested in the rough configuration. Further details of this point are given in [9].

## 4. The construction of the testrun

The testrun consisted of three parts. The first one, a pure batch run, was executed in order to obtain the relation between the new and old system. This is necessary to decide how well the new system meets the extrapolated requirements. The results of this run should be representative of the real life situation during the night hours. The batch testrun was made

through onsite peripherals.

In the second test, a timesharing load was added to the previous batch load. This was done in order to estimate the influence of the additional TS-load. This run was constructed in such a way that it would be representative of the real life situation during the weekend and the evening hours when no remote batch stations are accessible.

The third test was like the second, but with about one third of the batch jobs coming from remote batch stations. This test was to correspond to the expected real life situation during the day and was intended to show any problems in remote batch operation of the system. The batch load of the test-run was constructed so as to represent the batch portion of the current workload. Since there was no TS-experience at the installation, neither information about the users' behaviour nor about the pattern of resource consumption was available. Therefore an artificial load was designed based on experience on terminals in other university environments.

When constructing the batch run, two major methods were available: benchmark or synthetic jobstream. In the first case, real user programs are used to build a jobstream to be executed, while in the second, a synthetic program is first built so that its resource consumption can be determined by assigning appropriate parameters, then multiple copies of this program are introduced as the batch jobstream. In both methods the jobs must be executed on the actual system to be evaluated; i.e., all important aspects of the computer system must be exactly as used and observable. The reaction of the whole system is used as a basis for the judgement.

When benchmarking it is important to select the proper jobs from the real workload (which can either be done randomly or according to a given strategy). The difficulties are legion, mainly because it is necessary to run rather a long time period to smooth seasonal fluctuations in the workload. If the benchmarks are selected by applying a selection process involving a random number generator to sequence the jobs, the selected programs may no longer be available – especially in a university environment. Other difficulties like security and privacy problems may also arise. If one takes programs based on defined problems instead of extracting jobs from the real workload, one will run the risk that the benchmark may not be typical of the real job profile.

Because of these difficulties, we used the synthetic job method for constructing our testrun. Compared with the benchmark method, this approach provides flexibility, since it is possible to design jobs to include almost any desired parameters.

During the first six months of 1976, a total of 51716 jobs were executed, 30352 of them with at least one FORTRAN task and 44837 with at least one execution task. The major part of programs having no FORTRAN task but at least one execution phase were relocatable elements resulting from a FORTRAN compilation with a following linkage editor call. Therefore it was simple to reconstruct the real batch load from synthetic FORTRAN jobs. The synthetic program was a self-developed transformation of Buchholz's PL/1 synthetic program [2]. In contrast to other transformations (e.g. as done in [10]) the kernel of our version was constructed according to Gibbson-Mix II [8] for scientific applications. An analysis in detail (i.e., the determination of the characteristic parameters of the existing workload) is necessary to obtain a testrun that represents the needed profile. As a mechanism for this, the UNIVAC 494 system logging was used, describing each job by characteristic variables. The values of these variables show the system resources required. One way of grouping this set is to use cluster methods for finding groups of jobs with special requirements of the system resources [6,7].

Another method would be to calculate the joint probability density of jobs in discrete cells of the representation space [11]. Being aware of the fact that both methods are adequate means for constructing a synthetic workload, we decided to use the second because it is less expensive in processing time. Finally the joint probability density of the synthetic workload had to match that of the real workload. In our case, the parameters were the number of words transferred between the central memory and secondary storage and vice versa, the amount of consumed CPU-time, and the maximum memory requirements within the execution phases of a job. An important change to the method of Sreenivasan was the distinction between compilation and execution in the synthetic jobstream. On the existing system, a very strong correlation between the number of statements to be compiled and the resource requirements of the compiler was observed. This suggested that we should construct the synthetic program in such a way that the number of statements was equal to average length of the source coding in the real workload (288 statements). Another difference existed in the imitation of the execution phase. Whereas Sreenivasan proposed the use of the midpoint of a cell as a representation of the resource requirements, we hoped to obtain a better representation of the jobs in each cell by using the mean value of each variable taken over the number of jobs of the real workload in this cell. In another paper [5] the imitation of the real batch workload by a synthetic one is discussed in more detail.

A comparable method could not be used to construct the TS-part of the testrun because we had no TS-experience. Till now there is no successful solution to the representation of a real TS-workload by a synthetic one. There are some basic studies of the problem (e.g. [3]), but it would be worthwhile having a closer look at this problem. It seemed reasonable to evaluate the dynamic behaviour of the system as a consequence of the additional TS-load. The estimation of the time sharing portion of the testrun was a special problem. Our first market analysis (using kernels and instruction mixes) showed that a computer system at least twice as fast as the UNIVAC 494 (if measured in pure batch) was obtainable under the price constraints. Therefore it seemed to be realistic to construct a TS-load as heavy as the constructed batch portion of the testrun. Terminal activities at a university normally load the general system and I/O management rather than the CPU. Thus the script to be performed for a terminal simulation consisted of inputting a program to solve a simple problem (quadratic equation). Furthermore the compilation and the compiler output phases, together with an extensive editing were performed. This editing phase was made up of character and line corrections, as well as saving and retrieval of the program. Finally the program was executed using some data sets. Some steps within the procedure were repeated to give a realistic distribution between generation, correction, and the execution of the program.

## 5. The execution of the testrun

The target systems for the testrun were a CDC Cyber 172, a DEC 10/90 and a UNIVAC 1100/21. For the adaption and execution of the testrun, the manufacturers were required to follow strict and predefined rules. This was intended to guarantee an exact comparison of results. As an alternative, it would have been possible to leave adaption and execution of the testrun to the manufacturer, but this would only be practicable if the set of programs and types of data to be executed are nearly fixed, which is obviously not true in a university environment.

Generally speaking, each part of the testrun started with the input of the onsite batch portion and ended with the last activity of the system resulting from batch operation. The input medium was a magnetic tape containing the batch jobstream in a predefined sequence. It was stipulated that all jobs must have the same external priority. During the testrun no operator intervention was allowed and each program had to be compiled by the same compiler with the same option set.

In order to issue the defined TS-portion the activities of 30 terminals with a transmission rate of 110 baud was simulated in parallel with the batch portion for the second and third part of the testrun [12]. The input rate from the terminal was fixed at 1.5 characters per second, and a think time of 4 seconds had to be included before the transmission of each input line image. These values were observed at comparable installations. As with the batch run, the external priorities of all TS-programs were set equal. To avoid a parallel operation of all terminals, each had to start its activity with a delay of 10 sec. The defined script was repeated until the end of the testrun. In addition, the duration of the total execution of one script should not exceed 40 minutes, even in parallel to the batch load. To obtain comparable results, the input time and job sequence for the used remote batch stations were fixed in the third part of the testrun.

To obtain a good measure of the performance of the different systems, it was necessary to measure those values of the execution of the testrun which were not too strongly related to the philosophy of any special computer system. For the batch portion of each part of the testrun, the execution time of the whole stream was measured by the wall clock time (i.e., the time interval started with the input of the first block of the magnetic tape and ended with the last batch system activity).

For the TS-part the measure was the difference between the average execution of a script in parallel to the batch load as part of the TS-load and the duration of the stand alone execution of one script at one simulated terminal. This stand alone execution guarantees the optimum response time of the system. In this way, only the response time delay caused by the total load was evaluated. This is exactly what the user understands of the behaviour of the system.

## 6. The evaluation of the testrun

The testrun was evaluated to obtain an ordering of the different offers meeting the predefined requirements. Those aspects with a special weight within the planning phase had to be adequately considered in the evaluation phase. As a result the measured values characterizing the different aspects of the performance had to be included. Since the measured values were separately gathered, this problem was not one-dimensional. The different values can be interpreted as points in a multidimensional space to which the ordering is to be applied. To meet the aims of the planning phase in an adequate way, the measured values were mapped into the closed interval $[0,1]$ using a corresponding assessment function. Any direct use of the measured values would not make sense. As an example one may consider a pure batch throughput with is less than the one on the existing system. This might lead us to consider a system weaker than the existing one.

Using this example one can see that in the first part of the testrun a lower limit for the performance of a new system was given by the batch throughput of the existing system $(1/T_{\max})$ . It is obvious that the throughput is to be represented as the reciprocal value of execution time. Taking into account the results of the extrapolation within the planning phase one obtains an upper limit $(1/T_{\mathrm{p}})$ . This upper limit should be reached.

At this point we can observe a great difference between university and commercial computing centers; in the latter case the extrapolation would lead to a lower limit. Because of the fact that nearly any available power may be consumed in a university environment, it is not reasonable to accept this as a lower limit. From such considerations, the marks for a throughput performance less than the lower limit and greater than the upper limit were 0 and 1 respectively.

![](/api/attachments/WG9G6M9H/fulltext/images/f41e70f622ce465abe6683e035298ec06e200d99f27d60d65aa25fc51da2a4fa.jpg)  
Fig. 1. Assessment function for the batch part.

Assuming an assessment function which is linear in terms of throughput between the above mentioned limits, one has a mapping shown in Fig. 1. The principal effect on this special form of the assessment function is that differences of the execution time in the critical region near 1 have greater influence than those in the lower region. This effect can even be multiplied by using an assessment function lying in area b of Fig. 1. Since this throughput measure represents the turnaround time for batch users, it is not reasonable to use a function which lies in area c of Fig. 1.

The present case showed that the extrapolated throughput would not be reached by any system matching the given price limitations. Thus the upper limit - till now derived from extrapolation - was replaced by the optimum throughput value; that is, the value of that system which had the best batch performance in each part of the testrun $(1 / T_{\mathrm{opt}})$ . The shape of the assessment function is the same as shown in Fig. 1 but the value $T_{\mathrm{p}}$ is to be replaced by the value $T_{\mathrm{opt}}$ . The lower limit must not be set to the worst case, because bad systems would influence the assessment function. This can also lead to unjustification ble strong differences between the offers though all throughput values are close together. These two methods, to set the upper limit either to the extrapolated throughput value or to fix it as the optimum throughput value, can be combined. Then an assessment function results which ascends quickly to the extrapolated throughput value and continues slowly until it reaches the optimum performance value (see Fig. 2). The mark $N_{\mathrm{p}}$ given to the throughput value $1 / T_{\mathrm{p}}$ is strongly dependent on the goals. In our case $1 / T_{\mathrm{p}}$ lay beyond $1 / T_{\mathrm{opt}}$ .

The possibility of measuring the reaction of the system to decentral TS-oriented work has already been discussed. The response time was given as the delay-time of the execution of the script, and it could therefore be evaluated independent of special features of the system. Since this component of the overall performance influences comfort with the system and does not represent the throughput, the assessment function must take account of comfort. This means that a delay time that is unacceptable to the users has to be marked as zero. On the other hand, an immediate response (i.e. zero delay time) must get the best mark - one. The "unbearable" delay time for execution of the whole script was fixed at 11 minutes. This corresponds to a mean response time of about 5 seconds. Hence it follows that an immediate answer is not much better than a response within a short interval of 1-2 seconds. This corresponds to the suggestion made in [1]. Therefore, in the special case, a linear assessment function was not applicable, since the function should be much flatter near the zero delay time. Fig. 3 shows an adequate assessment function with the shape of a parabolic function. This function fulfills the necessary criterion and evaluates also the additional power necessary to provide a rapid response. This has no immediate importance, but a very short response time means that the system could either be tuned (and thus provide a better performance elsewhere) or it could support a greater number of terminals under the restriction of comfort.

![](/api/attachments/WG9G6M9H/fulltext/images/9f4a198d4198d613c901086abd7b77a7eeaf7deff992209bd80ff60b7b865eaf.jpg)  
Fig. 2. Combined assessment function.

![](/api/attachments/WG9G6M9H/fulltext/images/c900951e384e661a4c754408797cf1163453838a2a1f6912b625bb135437982a.jpg)  
Fig. 3. Assessment function for the TS-part. ( $\Delta T_{s} = \text{Delay time of the script}$ ).

After having fixed the scales on the coordinate axes, principles of ordering must be developed. For reasons of evidence, the structuring is done in such a way that for the first stage the marks of the different components of each part of the testrun (batch, TS) are combined to get a unequivocal performance value. In the second stage the three different performance values are used to give the overall ordering rank. In the first stage this combination was done according to the structure of the components (batch, TS) and the meaning of the measured values. In the second state the influence of the different parts of the testrun on the real life situation was observed. For the first part of the testrun, the pure batch run, the performance value was immediately derived from the assessment function as shown in Fig. 1. In the second and third stages of the testrun, two components giving two marks (one for the batch portion, derived in the same way as for the first stage, and another for the TS-portion) were present. On the one hand, time sharing performance is measured by response time, but on the other hand it has great influence on the batch running in parallel, thus giving an essential delay in the batch portion. According to our inquiry, decentralized TS-operation was requested to a great extent. Therefore on the computer system that matched the price constraints, the delay of the batch portion was about as long as the execution of the pure batch run. Therefore a combination of marks (nbatch for batchpart and nts for TS-part), using the formula $n = (\text{nbatch} \times \text{nbatch} \times \text{nts}) \uparrow (1/3)$ was utilized for part two and three of the testrun. It is necessary to multiply these marks, because otherwise (even when ignoring the TS-part) a remarkable performance value could be reached. Furthermore response time and batch throughput cannot be regarded independently.

The single parts of the testrun correspond to the way the system is operated at different times of day. According to this partitioning, and considering the fact that time at night is not considered as valuable, a combination of the above mentioned performance figures was chosen with weights of 0.15, 0.30, 0.55. The weighted sum was formed and gave the overall measure of performance of the system. Since the weight of the first part was fairly small (0.15) it was not necessary to use a multiplicative combination with exponential weights in order to avoid a pure batch machine.

## 7. Conclusions

An important point on performing testruns is the necessary work. This work can be partitioned between the planning team and the manufacturers. Whereas the effort of the planning team was quite extensive, the expense to the manufacturer was very small due to restrictive definitions. With the batch part only the replacement of the job control statements was necessary. Due to the lack of standard time sharing system (i.e., a standardized command language) more feedback to the planning group was necessary. The only tuning done by the manufacturer would be to the operating system being used.

The work in the planning phase -- especially the exact analysis of the existing workload -- was confirmed by the execution of the testrun. Differences concerning the mode of operation (batch, TS) were observed, but even in the use of programming languages. This could be seen especially when executing a jobstream corresponding to a different profile [9].

Finally a short statement of the result obtained might be of interest. Starting with the first part of the testrun, CDC and DEC were close, with a slight advantage for the CYBER-system. The second part was clearly won by the DEC-system followed by CDC. The final decision was made by the third part of the testrun, where the CYBER-system was much better, both in the TS and batch portion.

## References

[1] M.D. Abrams, I.W. Cotton, The Service Concept Applied to Computer Networks (NBS Techn. Note 880, August 1975).

[2] W. Buchholz, A Synthetic Job for Measuring System Performance, IBM Systems Journal Vol. 8, Nr. 4 (1969) 304–318.

[3] C.G. Crothers, Workload Determination and Representation for On-line Computer Systems (The Mitre Corp. F 19628-73-C-0001, Nov. 1973).

[4] G. Gell et al., Entscheidungskriterien und Ergebnisse des Auswahlverfahrens bei der Planung eines Universitätsrechenzentrums, Angew. inform. 21.Jg.H.4 (April 1979) 158–162.

[5] G. Haring et al., The Use of a Synthetic Jobstream in Performance Evaluation, Comp. Journal Vol. 22, Nr. 3 (Aug. 1979) 209–219.

[6] E. Hunt et al., Who are the Users? An Analysis of Computer Use in an University Computer Center, AFIPS Conf. Proc. Vol. 38 (1971) 231–238.

[7] K. Landau, Cluster Analysis for Computer Workload Evaluation (in German), Elektron. Rechenanlagen 18, H 6 (1976) 273–277.

[8] B. Oswald, Leistungsvermoegensanalyse von Datenverarbeitungsanlagen (S. Toeche-Mitter, Darmstadt 1973).

[9] R. Posch et al., Ein leistungsorientiertes Bewertungsverfahren zur Auswahl von Grossrechnern, Angew. Inform: 21.Jg. H.2 (Feb. 1979) 47–52.

[10] A.C. Sketler, T.E. Bell, Computer Performance Analysis Controlled Testing (Rand Corp. R-1436-DCA, April 1974).

[11] K. Sreenivasan et al., On the Construction of a Representative Synthetic Workload, CACM Vol. 17 (March 1974) 127–133.

[12] S.W. Watkins, M.D. Abrams, Survey of Remote Terminal Emulators (NBS Spec. Publ. 500-4, April 1977).
