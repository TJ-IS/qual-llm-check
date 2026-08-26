---
otero_id: 19070
otero_key: "Q89PC95E"
title: "Expert systems shell benchmarks: The missing comparison factor"
authors: "Robert T. Plant; Juan P. Salinas"
year: "1994"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)90009-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Research

# Expert systems shell benchmarks: The missing comparison factor

Robert T. Plant \*, Juan P. Salinas 1

Department of Computer Information Systems, University of Miami, Coral Gables, FL 33124, USA

## Abstract

This paper develops a methodology for benchmarking knowledge-based systems that practitioners may use to perform a comparative analysis of expert system shells. A program utilizing a deliberate instructional mix was found to be the most suitable and accurate way to measure the value of shells. The benchmark is intended for rule-based shells, such as CLIPS, VP-Expert and Ibis. The methodology for the approach is a generic rule-based algorithm that is easily adaptable to meet the language requirements of individual shells. We present results for three shells.

Key words: Benchmarking; Expert system shells; Expert systems; System performance

## 1. Introduction

The concept of expert systems $[12]$ has existed since the mid-sixties, however it was not until the eighties, when the microcomputer revolution occurred, that this technology was made easily accessible in a business environment $[14]$ . Expert system technology has two levels application programs (e.g., MYCIN $[13]$ ) and tools (the “shells”, by which applications are developed and run e.g. EMYCIN $[15]$ ). Though there are many expert system shells available, there is no measurement technique that is generally used to compare their performance. We can find out if one expert system shell offers more capabilities than another, but we cannot determine from the packaging that comes with the system how well any given shell could process a standardized problem. Inability to judge the performance of a shell can prove very frustrating, especially to those people who are first time purchasers/users of this software and have no alternative system with which to make a comparison, or for users such as NASA who run a large number of systems upon their shells, and therefore where a saving in processing speed over all systems could be advantageous. It is the intent of this paper to fill this gap by developing a methodology to benchmark expert system shells.

## 2. Expert systems shells' benchmark strategy

The following seven step procedure is used to create a benchmark system for expert system shells. First, the target area is defined, this is the environment in which the benchmark is to be utilized. The constraints for the benchmark are then laid down; these are the “benchmark goals,” which cover aspects such as accuracy, sensitivity, etc. Having determined these parameters, the techniques by which the benchmark is to be constructed is selected, along with the statistical approach that will be used to analyze the results of performing the experiments. Having determined the framework in which the benchmark is examined, the standardized benchmark program is designed and implemented. Finally, the benchmark programs are run and the analysis performed.

## 2.1. Target area definition

The benchmark will be designed to measure the execution speed of development tools under the workload imposed by a typical business expert system. The shell will be running on an IBM PC or compatible machine with a version of the MS-DOS operating system and a hard disk drive. In order to measure the performance of our target area, we must first determine its relationship to the other components of the system. We also need to understand the effect that other factors have on the target area [9]. Obviously, the benchmark will be influenced by the speed of the compiler or interpreter; in our case this is the shell program. In turn, the compiler or interpreter's performance is influenced by the operating system. The operating system (MS-DOS) and the machine (IBM PC) remain constant throughout the experiment for all shells in order to minimize test variance. The benchmark program design is standardized, such that all shells use as small a set of operating system features as possible, minimizing bias. However, without access to the shells' source code, a complete determination of the operating system shell dependence cannot be made. In turn, we note that software performance is influenced by hardware performance, which in turn, is composed of processing speed and input/output performance. The benchmark may be run on different types of PC compatible computers. So, we must provide a way to assess the differences in processing speed and hard disk performance produced by the differences in hardware characteristics. We need this assessment to relate the results of running the benchmark programs on different computers.

Here, we discuss the effect of running the benchmark programs on three different machines: a 10 MHz XT compatible, an 80386SX 16 MHz AT compatible, and an 80386DX 25 MHz AT compatible machine. Future shell benchmark programs may be written for new development tools, using the specifications produced here; these new programs may be run on different machines. The hardware benchmark programs will provide a way of relating future results to those discussed here, since hardware characteristics may be compared using the results of the commercial hardware benchmark programs.

## 2.2. Goals of the expert system shell benchmarks

After defining the target area, the goals of the benchmark must be set in terms of accuracy, sensitivity, portability, and effort [3][4]. We begin with accuracy. A goal of the benchmark is to provide sufficient accuracy to guarantee that if it takes a shell less time to execute the benchmark than another, it is because that shell is faster for many business applications. However, there may be expert systems that, due to the nature of their algorithms, run faster on the shell though the benchmark program ran slower. This is because the benchmark is based on an estimated average of the typical business expert system's workload. In order to obtain the desired level of accuracy, we must be careful in applying five points. First, select the contents of the benchmark programs carefully, so that it represents the work load imposed by a typical business expert system. Second, be clear and concise in preparing the benchmark specifications to avoid any programmers' interpretations and abilities that produce inaccuracies. Third, analyze and standardize the contents of the system files of the machines (e.g., possibly empty all other directories) used to run the benchmarks; system files are invoked in all operations. Fourth, to guarantee the desired level of accuracy, consider problems introduced by any lack of compatibility among different development tools. For example, differences in language semantics can be a source of inaccuracies. Most development tools provide a syntax to create production systems; the production rules should follow a standard structure, as depicted in Fig. 1. To avoid possible implementation inaccuracies, the benchmark only includes production rules.

The fifth consideration, involves the method of measuring the execution time of the benchmark programs.

We also have to define goals in terms of sensitivity. The benchmark must be able to show major differences in execution speed of the shells. It must be sensitive to those instructions most commonly used by business expert systems. To guarantee this, we perform a thorough statistical analysis of the selected variety of expert systems.

Because of the differences in syntax of the development tools, portability is an important issue. By using only production rule systems, the syntax becomes almost standard with a few variations due to wording and termination characters. This makes the benchmark portable; translating the benchmark involves modifying the syntax only slightly.

It is also important to provide for variety in control commands. An expert system may be modelled in two portions: control code and rules. The control code tends to be different from one shell to another. For this reason, we try to keep the control architecture of the benchmark as small as possible, while attempting not to bias the experiments in any way.

The effort can be subdivided into two parts:

(i) The design and statistical analysis that produces the benchmark specifications, and

(ii) Translation of the benchmark into actual tests.

We try to minimize the second by producing a clear specification and minimizing the control code. In addition, we reduced the translation effort by developing a rule generator program that can alter the code of the program to comply with the system under test.

## 2.3. Benchmark technique selection

The third step in developing a benchmark is to select a technique and methodology applicable to the considered target. Several benchmarking techniques are available, each having its own advantages and disadvantages. Instruction mix, arbitrary program, artificial workloads and application program [1][5][17] are amongst the best known.

After analyzing the targets characteristics, we found that the instructional mix technique best met the parameters of our benchmark requirements in terms of accuracy, sensitivity, portability, and effort.

## 2.4. Statistical analysis

Statistical analysis is a crucial component of benchmark design. Results establish the link between the benchmark and the target application. We attempted to ascertain the internal composition of several business expert systems and to determine what was a “typical business expert system”. The design of our statistical analysis involves selecting the type and focus of these statistics.

## 2.5. Type of statistics

Two statistical analysis options need to be considered: dynamic and static. Static analysis produces a statistical perspective of the components of a system, such as the number of assignment statements, operations, loop control statements, and other instructions contained in the code of the program. Dynamic analysis reflects the actual behavior of the program, achieved through counting the number of times each type of instruction is executed rather than just counting the number of occurrences, in the program.

<table><tr><td>IF conditionTHEN action_a[ELSE action_b].</td></tr><tr><td>The condition is also known as the left hand side of the rule (LHS);action_a and action_b are known as the right hand side (RHS).The ELSE clause is optional.</td></tr></table>

Fig. 1. Syntax of IF/THEN/ELSE rules.

To obtain accurate profiles of the business systems that we were using as the basis of our benchmark programs, we performed both dynamic and static analysis, through a technique called Real Problem Execution Simulation (REPROES), in which a manual procedure was performed to execute a series of case studies on actual business expert systems.

## 2.6. Shell internal functioning

After determining the type of statistics desired and the method to compile them, we had to define those characteristics of expert systems we wished to study. Every characteristic examined must have an impact on the execution speed of expert systems and must represent the vast majority of the running time of the programs. The two key components in the inferencing procedure are the chaining mechanism and pattern matching.

## 2.7. Focus of the statistical analysis

Pattern matching is a key element for both forward and backward chaining methods. Thus, composition of patterns is a major element in the systems performance. However, the literature covering the relationships of performance to pattern composition or size is weak.

The importance of this can be seen by running several tests on VP-Expert, Ibis, and CLIPS [it should be noted that these shells were selected arbitrarily and the benchmarks produced are not intended to be a reflection of the commercial suitability of the products. The paper present a benchmark methodology and uses these shells only to demonstrate the technique]. The tests were to determine if the length of the patterns made any difference in the execution time. Pattern length refers to the number of ASCII characters composing each pattern. The knowledge bases of these tests did not include any rules. Their only function was to assert 200 facts to the cache memory; that is, to relate one pattern to another. The syntax of Ibis and VP-Expert's assertions are very similar: pattern\_a = pattern\_b.

The syntax of CLIPS is different: DEFFACTS (assertion\_name(pattern\_apattern\_b)).

Although both instructions may seem different, they have the same purpose: to make a logical connection between the two patterns. Fig. 2 contains the results of these tests.

Pattern Assertions

<table><tr><td colspan="5">Average Execution Time Expressed in Seconds (a)</td></tr><tr><td>Pattern Lengths</td><td>25 x 25</td><td>25 x 2</td><td>2 x 25</td><td>2 x 2</td></tr><tr><td>CLIPS</td><td>1.1515</td><td>0.9075</td><td>0.9095</td><td>0.6645</td></tr><tr><td>VP-Expert</td><td>9.5665</td><td>9.5675</td><td>1.9625</td><td>1.9485</td></tr><tr><td>Ibis</td><td>3.9610</td><td>3.9570</td><td>1.4470(b)</td><td>1.4340(b)</td></tr></table>

(a) These times are the average of 20 executions running on a 803860X 25 MHz.  
(b) Ibis requires variable names to be at least 3 characters long

<table><tr><td colspan="5">Percentage Changes From Results of 25 X 25</td></tr><tr><td>Pattern Lengths</td><td>25 X 25</td><td>25 X 2</td><td>2 X 25</td><td>2 X 2</td></tr><tr><td>CLIPS</td><td>0.00%</td><td>-21.19%</td><td>-21.02%</td><td>-42.29%</td></tr><tr><td>VP-Expert</td><td>0.00%</td><td>0.01%</td><td>-79.49%</td><td>-79.63%</td></tr><tr><td>Ibis</td><td>0.00%</td><td>-0.10%</td><td>-63.47%</td><td>-63.80%</td></tr></table>

Fig. 2. Pattern assertion execution times.

Although the number of assertions was kept constant, decreasing the size of the patterns produces reductions in run-time of up to 80%. Though the programs only tested assertion efficiency, they proved that number of instructions executed is not the only factor to be observed. The length of the patterns used by business expert systems must also be examined, allowing us to determine the average length of the patterns used by most business expert systems. The shell's efficiency in pattern matching and the size of these patterns will have a tremendous effect on the execution speed of expert systems.

It is important to note that the tests mentioned above are not benchmark programs. They are intended to demonstrate the differences in execution times produced by variations in patterns' lengths, rather than demonstrating the speed of the shells. These tests were performed by creating sample knowledge bases through program generators.

Rules stored in the knowledge base is the next issue. First, the total number of rules must be counted. The more rules, the greater the search space for the inference engine. We also must count how many of these rules were actually executed. In backward chaining, we count rules that fail as fired rules. That is, if the inference engine fails in an attempt to fire a rule, it will have to perform a second search for another rule.

The final factor to observe is the composition of the rules fired. The rule components are divided into those included in the LHS and those in the RHS. In the rules that fail, we will record those elements of the RHS that were executed as the only components of that rule. This must be done because our benchmark will run using both forward and backward chaining. The workload must be identical for both methodologies. Instead of having rules that fail, we increase the number of rules to be executed. This produces a similar effect on the benchmark's workload. To emphasize, it is critical to note the characteristics of the patterns used, particularly because this will have a great impact on the speed of the conflict resolution process. All types of comparisons and assertions must be recorded, including the type and size of the elements being compared or stored. Although development tools offer many other functions such as I/O, graphics and spreadsheet interfaces, these tend to be nonstandard from shell to shell. We therefore concentrate on the real burden of expert system processing: conflict resolution and inference.

![](/api/attachments/Q89PC95E/fulltext/images/092667be6de97d7cdbd5153e7329f15943df58489781e8424b19d20e22598f0d.jpg)  
Fig. 3. Resulting data from the statistical analysis.

We next examined six business expert systems in operation through the REPROES technique. The results of this systematic study are compiled in Fig. 3, where the letters between brackets refer to the following:

(a) The results of this data may vary from execution to execution, since they are based on actual behavior of the programs tested. The path followed to reach a solution changes with the problem presented to the expert system. This produces a different program behavior for each different problem solved. The results are the averages obtained by running each expert system several times, following the REPROES technique.

(b) This result includes partially fired rules of the backward chaining expert systems tested.

(c) This result counts for the rules that are not fired from the control architecture but from within another rule, either by a FIND statement or during the inference process.

(d) An intermediate chain occurs when a rule calls another rule. The second rule calls a third rule, and so on. This result measures the average number of rules called.

(e) The RHS of the rules fired may contain additional statements not considered here. These numbers only represent the data considered relevant to the benchmark design.

(f, g) Multiple operator statements count as multiple statements. For example, the statement pattern = A × B + C counts as two statements, one multiplication and one addition.

## 2.8. Benchmark design

After determining the actual behavior of a typical business expert system, we proceed to the design stage of the benchmark. This step produces the program specifications. These are based on the dynamic statistics. Fig. 4 includes the benchmark program specifications. The implementation of the benchmark programs must follow these specifications closely.

![](/api/attachments/Q89PC95E/fulltext/images/fdc84791340b1564b01a737d9622288d795db9a0b4b1fc53bc6d2911d914e68b.jpg)  
Fig. 4. Benchmark program specifications.

## 2.9. Implementation of the benchmark programs

We attempt to benchmark three development tools: VP-Expert Version 2.1 by Paperback Software International, CLIPS version 4.2 developed at NASA/Johnson Space Center, and Ibis educational version 4.33 by Intelligence Manufacturing Company [2][8][16]. VP-Expert and Ibis use backward chaining, whereas CLIPS utilizes forward chaining.

Benchmark programs were produced through our code generator, which itself was written in Clipper Version Summer 87. However, due to the divergence in logic between forward and backward chaining, the benchmark for CLIPS varies slightly from the other two benchmark programs. The first difference is that the contents of the LHS and the RHS had to be altered. The result of running both sets of rules will be the same, and the processing requirements for both is very similar. In addition, CLIPS requires an additional rule that invokes all other rules. This rule starts the program by making the necessary pattern assertions to the cache memory required by the other rules. Even with these differences, the burden imposed by the CLIPS' benchmark program is identical to the Ibis and VP-Expert programs within our accuracy constraints.

## 2.10. Timing of the benchmark programs

Upon developing the benchmark programs, we must devise a technique that guarantees precision and fairness in measuring execution times. The first alternative is to use the internal clock of the computer. The major limitation of this approach is that the internal clock only counts in seconds, so lack of precision rules out this option. Therefore, we must use an external chronometer. The new problem is therefore: how can we start and stop the external timer? Because human response time is slow and inconsistent, manual control is not effective. We need to create an interface between the computer and the timer that is accessible from all expert system programs. In addition, portability becomes an issue.

As a result, we created a purpose built timing-device: The “Chronosound”. As its name suggests, this device is a chronometer that works with sounds. The instrument is connected to the terminals of the internal speaker of the computer. It contains an internal audio amplifier that transforms the speaker output into the necessary voltage needed to activate a micro relay. This relay, in turn, controls an external chronometer. Fig. 5 shows the circuit diagram of the Chronosound.

In testing the measuring device, we discovered that different computers send different output voltage levels to their speakers. To amend these discrepancies, we adjust the audio level through the audio gain control. The frequency and duration of the sound that starts and stops the chronometer may need adjustment and this is determined through a program that tests different frequencies and durations, so that the optimum signal for a given computer can be identified. After obtaining the frequency and duration of sound, we use a small program “START-STOP.EXE” that contains the instruction “sound-frequency, duration”, (frequency and duration contain the values obtained before). Running this program will cause the Chronosound to start or stop the chronometer, depending on its previous status.

To use the Chronosound with our benchmark

![](/api/attachments/Q89PC95E/fulltext/images/b9c89933bea06147ccc35d0271dfd18d6ec26e3fcbb72848dcb0aa9cc3483905.jpg)  
Fig. 5. Chronosound's electrical diagram.

<table><tr><td rowspan="3"></td><td colspan="2">PC-XT</td><td colspan="2">80386 SX</td><td colspan="2">80386 DX</td><td rowspan="3"></td></tr><tr><td>4.77 Mhz</td><td>10 Mhz</td><td>10 Mhz</td><td>16 Mhz</td><td>8 Mhz</td><td>24 Mhz</td></tr><tr><td colspan="6">Expert Systems Benchmark Programs</td></tr><tr><td>Clips</td><td>6.396</td><td>3.006</td><td>1.454</td><td>1.130</td><td>1.639</td><td>1.187</td><td>Seconds (a)</td></tr><tr><td>Ibis</td><td>59.250</td><td>41.450</td><td>15.212</td><td>6.013</td><td>11.906</td><td>3.686</td><td>Seconds (b)</td></tr><tr><td rowspan="2">VP-Expert</td><td>11.400</td><td>5.615</td><td>2.234</td><td>1.698</td><td>2.315</td><td>0.985</td><td rowspan="2">Seconds (c)</td></tr><tr><td colspan="6">Benchmark Program V. 1.20 by Chips and Technologies Inc.</td></tr><tr><td rowspan="2">Overall Performance</td><td>0.21</td><td>0.42</td><td>1.21</td><td>1.84</td><td>1.03</td><td>3.36</td><td rowspan="2">MIPS (d)</td></tr><tr><td colspan="6">CheckIt Benchmark Programs</td></tr><tr><td>CPU Speed</td><td>344</td><td>689</td><td>1,674</td><td>3,157</td><td>1,842</td><td>6,374</td><td>Dhrystones (e)</td></tr><tr><td>Video Speed</td><td>465</td><td>762</td><td>3,543</td><td>5,212</td><td>3,277</td><td>6,995</td><td>Characteres/Second (e)</td></tr><tr><td>Math Speed</td><td>6.5</td><td>13.6</td><td>31.2</td><td>60.4</td><td>35.4</td><td>121.5</td><td>Kilo-Whetstones (e)</td></tr><tr><td>Average Seek Time</td><td>64.1</td><td>64.6</td><td>19.8</td><td>19.8</td><td>21.2</td><td>20.7</td><td>Milliseconds (f)</td></tr><tr><td>Track to Track Seek Time</td><td>8.8</td><td>8.8</td><td>6.0</td><td>6.0</td><td>1.0</td><td>1.0</td><td>Milliseconds (f)</td></tr><tr><td rowspan="2">Transfer Speed</td><td>28.2</td><td>100.1</td><td>594.3</td><td>494.3</td><td>514.0</td><td>514.0</td><td rowspan="2">Kilobytes/Second (f)</td></tr><tr><td colspan="6">CORE Disk Performance Test Program V. 2.8</td></tr><tr><td>Disk Capacity</td><td colspan="2">32.7</td><td colspan="2">80.3</td><td colspan="2">89.0</td><td>Megabytes (f) (g)</td></tr><tr><td>Number of Cylinders</td><td colspan="2">939</td><td colspan="2">922</td><td colspan="2">1,023</td><td>Cylinders (f) (g)</td></tr><tr><td>Number of Heads</td><td colspan="2">4</td><td colspan="2">5</td><td colspan="2">10</td><td>Heads (f) (g)</td></tr><tr><td>Number of Sectors per Track</td><td colspan="2">17</td><td colspan="2">34</td><td colspan="2">17</td><td>Sectors (f) (g)</td></tr><tr><td>Transfer Speed</td><td>28.1</td><td>189.1</td><td>670.5</td><td>686.2</td><td>807.0</td><td>980.0</td><td>Kilobytes/Second (g)</td></tr><tr><td>Average Seek Time</td><td>59.6</td><td>62.7</td><td>6.1</td><td>20.1</td><td>21.2</td><td>21.0</td><td>Milliseconds (g)</td></tr><tr><td>Track to Track Seek Time</td><td>16.6</td><td>17.0</td><td>6.1</td><td>6.2</td><td>1.2</td><td>1.0</td><td>Milliseconds (g)</td></tr><tr><td rowspan="2">Performance Index</td><td>1.090</td><td>2.003</td><td>6.741</td><td>6.823</td><td>7.396</td><td>8.458</td><td rowspan="2">Benchmark Units (g)</td></tr><tr><td colspan="6">Norton Utilities V.5.0 System Information Benchmarks</td></tr><tr><td>CPU Speed</td><td>1.0</td><td>2.0</td><td>4.9</td><td>8.9</td><td>5.9</td><td>22.5</td><td>Benchmark Units (h)</td></tr><tr><td>Disk Speed</td><td>0.8</td><td>1.5</td><td>6.3</td><td>6.3</td><td>6.6</td><td>7.1</td><td>Benchmark Units (i)</td></tr><tr><td>Average Seek Time</td><td>62.95</td><td>62.83</td><td>19.72</td><td>19.71</td><td>20.87</td><td>20.89</td><td>Milliseconds (i)</td></tr><tr><td>Track to TracI Seek Time</td><td>9.81</td><td>9.93</td><td>5.17</td><td>5.16</td><td>3.62</td><td>3.51</td><td>Milliseconds (i)</td></tr><tr><td>Transfer Speed</td><td>29.1</td><td>142.7</td><td>711.9</td><td>711.1</td><td>780.9</td><td>878.1</td><td>Kilobytes/Second (i)</td></tr><tr><td>Overall Performance Index</td><td>0.8</td><td>1.8</td><td>5.3</td><td>8.0</td><td>6.1</td><td>17.3</td><td>Benchmark Units (j)</td></tr></table>

Fig. 6. Benchmark results.

Shell Benchmarks' Execution Times  
![](/api/attachments/Q89PC95E/fulltext/images/d39bffeb82ce29e36970d5c0e068960a64bc31f78869178aa57565d83fd0dd65.jpg)  
Fig. 7. Execution times of the shell benchmark programs.

programs, we include two system calls within the benchmarks to the program START-STOP.EXE. The first call must be placed at the beginning of the expert system and the other at the end.

The Chronosound was used in a way to guarantee that all times are taken under the same conditions. The results produced by the Chronosound have a 0.03 seconds variance. The average

![](/api/attachments/Q89PC95E/fulltext/images/c4fce15eee3f58cee9e69ff553bb0ba325f84e25cadeac20dd2dc11e4f86e76a.jpg)  
Fig. 8. Norton's CPU benchmark results.

<table><tr><td colspan="2">Average = 7.333Standard Deviation = 7.174</td></tr><tr><td colspan="2">(1.0-7.333)/7.174) = -0.911</td></tr><tr><td colspan="2">(2.0-7.333)/7.174) = -0.771</td></tr><tr><td colspan="2">(4.9-7.333)/7.174) = -0.367</td></tr><tr><td colspan="2">(8.9-7.333)/7.174) = 0.191</td></tr><tr><td colspan="2">(5.9-7.333)/7.174) = -0.228</td></tr><tr><td colspan="2">(22.5-7.333)/7.174) = 2.086</td></tr></table>

Fig. 9. Computations to produce Fig. 10.

time for 40 executions of the shell benchmark programs on each computer were calculated. The number of executions was chosen to obtain the execution times within 0.015 seconds with 98% confidence or better. Using the standard sample size formula the actual result calculated was 22 samples or executions; but by increasing the number of samples to 40, we also increase the confidence factor. By measuring 40 executions, we are at least 98% confident that the margin of error is not greater than 0.015 seconds.

Since the three computers used to run the benchmarks allowed is to select the processor's speed, all benchmarks were run at both speeds available on each machine. Fig. 6 contains the results obtained from all the benchmarks, including the shell and the hardware benchmarks.

With all the benchmark programs run and compiled, the results of the benchmarks can be compared to determine the fastest shell. These results are diagramed in Fig. 7.

## Combined Benchmarks Results In Number of Standard Deviations from the Mean Grouped by Benchmarks' Target Areas

<table><tr><td></td><td>XT/ 4.77Mhz</td><td>8088 10Mhz</td><td>AT/ 10Mhz</td><td>80386 SX 16Mhz</td><td>AT/ 8Mhz</td><td>80386DX 25Mhz</td></tr><tr><td>Clips (a)</td><td>2.106</td><td>0.288</td><td>-0.544</td><td>-0.718</td><td>-0.445</td><td>-0.687</td></tr><tr><td>Ibis (b)</td><td>1.780</td><td>0.908</td><td>-0.378</td><td>-0.828</td><td>-0.540</td><td>-0.942</td></tr><tr><td>VP-Expert (c)</td><td>2.045</td><td>0.437</td><td>-0.502</td><td>-0.651</td><td>-0.480</td><td>-0.849</td></tr><tr><td>Average (**)</td><td>1.977</td><td>0.544</td><td>-0.475</td><td>-0.732</td><td>-0.488</td><td>-0.826</td></tr><tr><td>CPU Speed (e)</td><td>-0.994</td><td>-0.823</td><td>-0.334</td><td>0.402</td><td>-0.251</td><td>1.999</td></tr><tr><td>CPU Speed (h)</td><td>-0.911</td><td>-0.771</td><td>-0.367</td><td>0.191</td><td>-0.228</td><td>2.086</td></tr><tr><td>CPU Speed (d)</td><td>-1.085</td><td>-0.884</td><td>-0.129</td><td>0.473</td><td>-0.301</td><td>1.926</td></tr><tr><td>Math Speed (e)</td><td>-0.997</td><td>-0.812</td><td>-0.353</td><td>0.407</td><td>-0.244</td><td>1.999</td></tr><tr><td>Average (**)</td><td>-0.997</td><td>-0.823</td><td>-0.296</td><td>0.368</td><td>-0.256</td><td>2.003</td></tr><tr><td>Transfer Speed (i)</td><td>-1.559</td><td>-1.214</td><td>0.515</td><td>0.513</td><td>0.725</td><td>1.020</td></tr><tr><td>Transfer Speed (f)</td><td>-1.555</td><td>-1.232</td><td>0.990</td><td>0.540</td><td>0.629</td><td>0.629</td></tr><tr><td>Transfer Speed (g)</td><td>-1.573</td><td>-1.097</td><td>0.326</td><td>0.373</td><td>0.730</td><td>1.242</td></tr><tr><td>Average Seek Time (*) (i)</td><td>-1.411</td><td>-1.409</td><td>0.794</td><td>0.796</td><td>0.617</td><td>0.614</td></tr><tr><td>Average Seek Time (*) (f)</td><td>-1.407</td><td>-1.414</td><td>0.792</td><td>0.792</td><td>0.582</td><td>0.654</td></tr><tr><td>Average Seek Time (*) (g)</td><td>-0.802</td><td>-0.819</td><td>2.143</td><td>-0.142</td><td>-0.194</td><td>-0.185</td></tr><tr><td>Track to Track Seek Time (*) (i)</td><td>-1.228</td><td>-1.244</td><td>0.022</td><td>0.027</td><td>1.153</td><td>1.271</td></tr><tr><td>Track to Track Seek Time (*) (f)</td><td>-0.771</td><td>-0.771</td><td>-0.641</td><td>-0.641</td><td>1.412</td><td>1.412</td></tr><tr><td>Track to Track Seek Time (*) (g)</td><td>-0.829</td><td>-0.833</td><td>-0.560</td><td>-0.567</td><td>1.178</td><td>1.611</td></tr><tr><td>Disk Speed (i)</td><td>-1.538</td><td>-1.267</td><td>0.595</td><td>0.595</td><td>0.711</td><td>0.905</td></tr><tr><td>Disk Performance Index (g)</td><td>-1.542</td><td>-1.217</td><td>0.471</td><td>0.500</td><td>0.705</td><td>1.083</td></tr><tr><td>Average (**)</td><td>-1.292</td><td>-1.138</td><td>0.495</td><td>0.253</td><td>0.750</td><td>0.932</td></tr></table>

Fig. 10. Number of standard deviations away from the mean.

An analysis of the results in Fig. 7 shows us that Ibis performance is far from satisfactory. It took the shell almost a minute to run the benchmark on a 4.77 MHz PC, more than nine times CLIPS's run time, and five times VP-Expert's run time. The Ibis requires a powerful computer to provide an acceptable response time. CLIPS, on the other hand, proved to be the fastest shell. Its response time was good for almost all the machines. The only case where this execution time was not satisfactory was in the 4.77 MHz test, which took over six seconds to execute. Since this type of computer is almost extinct, this becomes less of an issue. CLIPS also produced interesting results for the 16 MHz 80386SX and the 25 MHz 80386DX. Although the first machine is faster than the second one, CLIPS runs faster on the SX. The only explanation to this phenomena is the fact that the hard disk on the SX is slightly faster than the one on the DX. Still, the difference of only five hundredths of a second is quite small, if compared to the difference obtained from the Ibis benchmarks (2.327 seconds slower on the SX than on the DX). From this one may conclude, CLIPS uses the hard disk more than

VP-Expert and Ibis, since VP-Expert and Ibis behaved as expected, running faster on the faster machine. This may make shells such as VP-Expert and Ibis more competitive with faster 80486 and subsequent generation processors.

Because the values represent different types of information and are expressed with different notations, it is difficult to infer the relationships among the different variables. We created Fig. 10 to show the relationships. The values in Fig. 11 are stated as “the number of standard deviations that each value of Fig. 6 moves away from the average computed for that benchmark”. This was achieved by determining the CPU speeds as reported by Norton Utilities CPU Speed benchmark, Fig. 8.

We calculated the average (7.333), together with the standard deviation (7.174). With these two figures, we can perform the computations shown in Fig. 9.

The numbers we calculated are the same as those of the line “CPU Speed (h)” of Fig. 10 although Fig. 10, does not provide the actual results of each test, it enables us to make comparisons among the different characteristics of the hardware and the running speed of the shell benchmark programs.

![](/api/attachments/Q89PC95E/fulltext/images/ad16266ad52a8c9de617aaa30d128348c6b32c0130d3b4313d1bf527e2aef111.jpg)  
Fig. 11. Differences in shell benchmarks' execution times.

The rows in Fig. 10 have been sorted by the target area of the benchmarks. The first section includes the expert systems' benchmarks. The second section includes the benchmarks targeted at the processing speed. The third section includes the hard disk benchmarks. The last section includes the overall hardware benchmark.

Fig. 11 provides a graphical representation of the differences in execution speed among the computer runs. The term “computer run” refers to the execution of a benchmark program on a given machine at a given speed. Because each machine allows two speeds, two runs can be obtained from each. The vertical axis indicates the “number of standard deviations away from the mean.” The three plots are the three shell benchmarks.

Fig. 12 shows that the execution times for the three benchmarks denoted almost the same pattern for all six computer runs. The three lines, representing the three benchmark programs, are almost identical because the instruction mix of each program is equivalent. If this were not the case, we would not see such even behavior among the shells' execution times when switching from one computer run to the next.

Finally, computer performance is the product of several factors and hardware processing speed will have an influence on shell performance. Fig. 12, illustrates this point and provides a graphical perspective of the influence that different hardware characteristics have upon shell performance.

Fig. 12 is based on the calculated averages obtained for the four groups of benchmarks of Fig. 11: shells, processing speed, disk speediness, and overall hardware performance. The vertical axis shows the number of standard deviations that each run is away from the computed average for that type of benchmark over all the computer runs, as calculated in Fig. 10 on the rows labeled “Average (\*\*)” and “Overall Performance Index (J)”.

The four plots represent the changes in bench-

## Relationship Between Hardware and Shell Performance

![](/api/attachments/Q89PC95E/fulltext/images/5b75461370ad4a5d1a6a08d8551829e7d1fb977df9a1d5aa9a953e5b752db683.jpg)  
Note2: 1=8088/4.77MHz, 2=8088/10MHz, 3=80386SX/10MHz, 4=80386SX/16MHz, 5=80386DX/8MHz, 6=80386DX/25MHz  
Note1: NSDFM=Number of Standard Deviations from the Mean

Fig. 12. Relationship between hardware and shell performance.

mark results from one computer run to the next for each of the four benchmark groups. We can see how the shell's benchmarks ran faster, thus taking less time to execute on faster machines that obtained higher ratings on the hardware benchmarks. Note that, the shell benchmarks' results are given in seconds, whereas the commercial hardware benchmarks produce ratings. The faster the hardware, the higher the ratings of the hardware benchmarks; the faster the shell benchmarks executed, the less time to run them.

A final observation is that differences in Disk, CPU and Overall Hardware Speed produce changes in the execution speed of the benchmarks to different degrees. As noted earlier when selecting goals, the shell benchmarks are not hardware insensitive. The results of the hardware benchmarks allow the reader to relate possible future benchmarks of other shells run on different hardware.

## 3. Conclusion

We attempted to develop a benchmark for shells or development tools. These benchmark programs allow for comparison of different shells based on their execution speed. In the past, such comparisons could only be made based on the features and capabilities of the different programs available. After implementing the benchmark programs, we see that CLIPS is faster than Ibis, for business applications. If we only look at the features and capabilities of the programs, Ibis would probably be the winner, because it provides excellent development and user interfaces. In addition, Ibis offers both forward and backward chaining, while CLIPS only permits forward chaining.

In the past, researchers have attempted to develop benchmark programs for expert systems. Their major flaw was that they did not establish the link between their benchmark programs and the real world. People developed expert systems to compare different tools, but only to a certain degree. Although we can use an expert system that solves the “monkey and the bananas” problem to compare shells [6], we cannot conclude that a shell that runs this program in less time will also run business applications faster. The second error was that they did not utilize the fact that expert system performance is strongly related to its pattern matching capability. Developing a set of rules that call each other and count the number of rules fired does not tell us anything about the shell unless we know the contents of the rules and base those contents on some logical criteria.

This paper summarizes the efforts of many people, who for over 20 years, have studied benchmarks. Only a few researchers have attempted to develop a benchmark program for expert systems, and their efforts tended to be “one-off” attempts; e.g., [7][10][11].

## References

[1] Bell, A.G., Hallowell, and Long, D.H., Software-Practice and Experience, “A Universal Benchmark?” October 1973, P. 355

[2] CLIPS Version 4.2 (NASA-Johnson Space Center)

[3] Conte, Thomas M. and Hwu, Wen-mei, Computer, "Benchmark Characterization," January 1991, P. 49.

[4] Curnow, H.J. and Wichmann, B.A., The Computer Journal, "A Synthetic Benchmark," February 1976, P. 43

[5] Ferrari, Domenico, Computer, “Workload Characterization and Selection in Computer Performance Measurement,” August 1972, P. 20

[6] Giarratano, Joseph and Riley, Gary, Expert Systems: Principles and Programming (Boston-Massachusetts: PWS-KENT Publishing Co., 1989), P. 160.

[7] Gilbreath, Jim, BYTE, “A High-Level Language Benchmark,” September 1981, P. 180

[8] Ibis Educational Version 4.33 (West Sacramento-California: Intelligence Manufacturing Company)

[9] Levy, Henry M. and Clark, Douglas W., Computer Architecture News, "On the Use of Benchmarks for Measuring System Performance," December 1982, P. 5

[10] Press, Larry, AI Expert, “Eight-Product Wrap-Up,” September 1988, P. 64.

[11] Press, Larry, IEEE Expert, “Expert Systems Benchmarks,” Spring 1989, P. 37–44.

[12] Rich, E., Artificial Intelligence, 1983. McGraw Hill, New York.

[13] Shortliffe, E.H. Computer-based Medical Consultations: MYCIN, Elsivier, New York.

[14] Silverman, B.G., 1987. Addison-Wesley, Reading, MA.

[15] van Melle, W., Scott, A.C., Bennett, J.S., & Peairs, M.A., The EMYCIN Manual. Technical Report, Heuristic Programming Project, Stanford University, 1981

[16] VP-Expert Version 2.1 (Oakland-California: Paperback Software International)

[17] Walters, R.E., The Computer Journal, “Benchmark techniques: a constructive approach.” February 1976, P. 50

ods, Software Economics and Metrics. Dr Plant is also a Chartered Engineer and a Senior Member of the American Institute of Aeronautics.

![](/api/attachments/Q89PC95E/fulltext/images/03f7371fad818fc0ed20223ae2cc5b10a3713e75dd08dbcb542d5c63b8b3d79e.jpg)

Robert T. Plant, is an Assistant Professor in Computer information Systems Department, School of Business Administration, at The University of Miami, Coral Gables, Florida. Dr Plant obtained his Ph.D in Computer Science at The University of Liverpool, England. Previously having studied at The Programming Research Group, Oxford University, England. His research interests are in Software Methodology, Formal Meth

Juan Salinas is a Systems Consultant in Costa Rica, Central America. He has a Master of Science Degree from the School of Business Administration at The University of Miami, Florida in Computer Information Systems and a Bachelor of Science in Computer Information Systems from Bentley College, Waltham, Massachusetts.
