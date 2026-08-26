---
otero_id: 21673
otero_key: "NKEGJSR7"
title: "Load-frequency control service in a deregulated environment"
authors: "A.P.Sakis Meliopoulos; George J. Cokkinides; A.G. Bakirtzis"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00078-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Load-frequency control service in a deregulated environment

A.P. Sakis Meliopoulos <sup>a,)</sup>, George J. Cokkinides <sup>b,1</sup>, A.G. Bakirtzis <sup>c,2</sup>

<sup>a</sup> School of Electrical and Computer Engineering, Georgia Institute of Technology, Atlanta, GA 30332-0250, USA

Department of Electrical and Computer Engineering, UniÕersity of South Carolina, Columbia, SC 29208, USA

<sup>c</sup> Department of Electrical and Computer Engineering, Aristotle UniÕersity of Thesssaloniki, Thessaloniki, Greece

## Abstract

In a deregulated environment, independent generators and utility generators may or may not participate in the load-frequency control of the system. For the purpose of evaluating the performance of such a system, a flexible method has been developed and implemented. The method assumes that load frequency control is performed by an ISO based on parameters defined by the participating generating units. The participating units comprise utility generators and independent power producers. The utilities define the units, which will be under load-frequency control, while the independent power producers may or may not participate in the load frequency control. For all the units, which participate in the load-frequency control, the generator owner defines a generation limits, b rate of change and c economic participation factor. ThisŽ . Ž . Ž . information is transmitted to the ISO. This scheme allows the utilities to economically dispatch their own system, while at the same time permit the ISO to control the interconnected system operation. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Frequency regulation; Area control error; Load-frequency control; Deregulation; System AGC factor

## 1. Introduction

The operation of the interconnected electric power system has evolved over the years. Few years ago, it appeared to have settled into a system characterized with self-discipline and mutual assistance. An important aspect of system operation is the load-frequency control problem. The load-frequency control is a technical requirement for the proper operation of an interconnected power system. Fig. 1 illustrates the mechanism of the traditional load-frequency control of a system that is part of an interconnected power system. The ability of the system to control and balance the load-generation-and-frequency is measured with the area control error ACE 1 . TheŽ . <sup>w</sup> <sup>x</sup> generating units of the system are controlled on the basis of the ACE value. Utilities have been operated in such a way that at least once every 10 min, each utility zeros the area control error, meaning that at least once every 10 min the load and generation is balanced and the frequency is equal to the nominal.

![](/api/attachments/NKEGJSR7/fulltext/images/9672fb3391ca0ec2a722f04e03c7b152ea2ceb6731a663ba986b8e94b674681c.jpg)  
Fig. 1. Automatic generation control or load-frequency control in a modern electric power system.

This operation is costly requiring an infrastructure for the feedback control loop as shown in Fig. 1 and wear and tear on the power plant equipment from the frequent control action 2,3 . Operating history sug- <sup>w</sup> <sup>x</sup> gests that as long as all utilities are participating in the load-frequency control problem, the performance of the system is excellent. This cost of load-frequency control is justifiable on the basis of the excellent performance.

Recent trends toward deregulation and competition have promised to alter the traditional operating practices of load-frequency control. In a deregulated and open competition environment, load-frequency control becomes a commodity that can be traded. Generating units participating in the load-frequency control provide a service for which they must be compensated. Alternatively, a generating unit utilityŽ or independent producer may elect not to participate . in the load-frequency control in which case it must be penalized or compensate the rest of the system for the service it receives. Conceptually, load-frequency control may be offered or received by any generating unit in the system. Units may make the choice in real time. In this case, the total generating capacity participating in the load frequency control may vary in real time. What will be the implications of such an operating environment? One can project that the performance of the system in terms of maintaining near constant frequency and closely tracking load and interchanges may be different than past experiences. For example, it may be expected that the frequency deviations may be large at times when the portion of generating capacity on load-frequency control is low compared to the total load.

This paper proposes a model for evaluating the performance of the load-frequency control problem in an environment where units may elect to offer or receive the service. In this case, an important parameter is the total generation on load-frequency control as a percentage of the total system load. We shall refer to this parameter as the System AGC Factor. First, we present the model. Then typical results are given parametrically in terms of the System AGC factor.

NET - Network System Editor V 1.00 Case: Investigation of Load-Frequency Date:10/06/97 Time: 08:23:21.00

## 2. Method description

The proposed method has been implemented within the Virtual Power System VPS . The VPSŽ .

![](/api/attachments/NKEGJSR7/fulltext/images/5cf6ac0e170b2db140078d59469566fc039d09142606d8d4f916cc4b3679771f.jpg)  
Fig. 2. An example of a four-control area system.

engine consists of a time-domain simulation engine and a CAD-like user interface. The VPS permits construction of flexible control loops such as those needed for the simulation of the operation of the system as described above. Two specific control loops have been implemented: a the utility controlŽ . loop which performs economic dispatch and provides the parameters to the ISO for load-frequency control, and b the ISO control loop which performsŽ . the load-frequency control. The load frequency control is based on the parameters it receives for the utilities and the independent power producers IPP .Ž . The model computes the frequency response of the system for specific conditions. System performance is measured with two indices: a utility control errorŽ . and b independent unit-load balance index. TheseŽ . two indices are correlated with the traditional area control error. It is shown that in order to have acceptable performance, a certain percentage of the generating system must participate in the load frequency control.

Fig. 2 illustrates the system used for the study. This system is a simplification of an interconnected power system. The model consists of four interconnected power systems and three independent power producers. The location of the independent power producers is shown at the buses IPP1, IPP2 and IPP3. Power system 1 has two generating plants at busses A1GEN1 and A1GEN2 and it is interconnected with five tie lines to power systems 2, 3 and 4. Power system 2 has one generating plant at bus A2GEN1 and it is interconnected to power systems 1 and 3 with three tie lines. Similarly, power system 3 has one generating plant at bus A3GEN1 and it is interconnected with two tie lines to power systems 1 and 2. Finally, power system 4 is interconnected with power system 1 only with two tie lines and has one generating plant at bus A4GEN1. Equivalent generating units and location of electric loads is shown in Fig. 2. The figure also illustrates the location of power meters. The output of the power meters is utilized in the load-frequency control loop.

The model of each generator is important for the proposed model. It is described in this section in detail. The generator is represented with its classical model. The pertinent equations are given in Table 1. Note that the model incorporates the electrical circuit of the generator together with the dynamics of the

Table 1 Mathematical model of a synchronous machine

$$
v _ {\mathrm{abc}} (t) = e _ {\mathrm{abc}} (t) + \left(R + L \frac {\mathrm{d}}{\mathrm{d} t}\right) i _ {\mathrm{abc}} (t)
$$

$$
i _ {\mathrm{a}} (t) + i _ {\mathrm{b}} (t) + i _ {\mathrm{c}} (t) + i _ {\mathrm{n}} (t) = 0
$$

$$
\frac {\mathrm{d} y _ {1}}{\mathrm{d} t} = y _ {2} (t)
$$

$$
\frac {\mathrm{d} y _ {2}}{\mathrm{d} t} = \frac {\omega}{2 H} \left(y _ {3} (t) + e _ {\mathrm{abc}} ^ {\mathrm{T}} (t) i _ {\mathrm{abc}} (t)\right)
$$

$$
\frac {\mathrm{d} y _ {3}}{\mathrm{d} t} = - k y _ {2} (t)
$$

where:

$$
v _ {\mathrm{abc}} (t) = \left[ \begin{array}{c} v _ {\mathrm{a}} (t) - v _ {\mathrm{n}} (t) \\ v _ {\mathrm{b}} (t) - v _ {\mathrm{n}} (t) \\ v _ {\mathrm{c}} (t) - v _ {\mathrm{n}} (t) \end{array} \right]
$$

$$
i _ {\mathrm{abc}} (t) = \left[ \begin{array}{c} i _ {\mathrm{a}} (t) \\ i _ {\mathrm{b}} (t) \\ i _ {\mathrm{c}} (t) \end{array} \right]
$$

$$
y _ {1} (t) = \delta (t)
$$

$$
y _ {2} (t) = \frac {\mathrm{d} \delta}{\mathrm{d} t}
$$

$$
y _ {3} (t) = P _ {\mathrm{m}} (t)
$$

$$
e _ {\mathrm{abc}} (t) = \left[ \begin{array}{c} \sqrt {2} E \cos (\omega t + \delta (t)) \\ \sqrt {2} E \cos \left(\omega t + \delta (t) - \frac {2 \pi}{3}\right) \\ \sqrt {2} E \cos \left(\omega t + \delta (t) - \frac {4 \pi}{3}\right) \end{array} \right]
$$

generator rotor. The input mechanical power to the generator is denoted with the variable $y _ { 3 } ( t )$ . The model also assumes that the voltage regulator of the generator controls the generated voltage to a constant level.

![](/api/attachments/NKEGJSR7/fulltext/images/704324e05afdf626b0b44bf1162ad1823127720c906ec979a0aeaa0c56d985fd.jpg)  
Fig. 3. Illustration of load frequency control animation using the VPS.

The model shown in Table 1 is another form of the classical generator model used for transient anal ysis studies. It has been modified to meet the requirements of the proposed method. Specifically, the available variables at the network level are the generator terminal voltages and currents, the rotor position, Ž .t , and the input mechanical power. The simulation engine of the Virtual Power System is a time-domain solution method that computes these quantities as they evolve in time with a user defined time step. As the solution progresses, the meters shown in Fig. 2 capture the real power flow in the tie lines and the frequency of the system at each generating plant. The frequency is given with:

$$
f = f _ {0} + \frac {\mathrm{d} \delta}{\mathrm{d} t}
$$

Note that each generating unit will have a different frequency at any given instance during a transient.

The tie line flows and the average of the frequency of all generators in a system are used to compute the area control error for this system. The area control error is then distributed to the generators of the system, which participate in the load-frequency control. A similar procedure is followed for the independent power producers, if they elect to participate in the load-frequency control. If not, their mechanical input power is set to a constant level. During transients they may fluctuate their real power output based on the natural response of the generator to the system transients. The overall scheme is illustrated in Fig. 3. Note that the ISO computes the area control error for each system utility or IPP and transmits Ž . the signal to the appropriate party.

## 3. System performance

System performance results have been computed for the example system of Fig. 2 using the ISO controller of Fig. 3. The performance is measured in terms of frequency deviations and net interchange deviations. The following scenarios have been evaluated.

Scenario 1: The entire interconnected system operates under steady-state conditions, all generators Ž . utilities and IPPs participate in load frequency control. Suddenly, power system 1 losses generator 1. Prior to this outage, generator 1 generates 250 MW. System performance for this scenario is illustrated in Fig. 4. Note that maximum frequency deviation is 0.238 Hz.

Scenario 2: The entire interconnected system operates under steady-state conditions, all utility generators participate in load frequency control. None of the IPPs participates in the load frequency control. Suddenly, power system 1 losses generator 1. Prior to this outage, generator 1 generates 250 MW. System performance for this scenario is illustrated in Fig. 5. Note that maximum frequency deviation is 0.74 Hz.

Scenario 3: The entire interconnected system operates under steady-state conditions. Only the generators of power systems 1 and 3 participate in load frequency control. None of the IPPs participate in load-frequency control. Suddenly, power system 1 losses generator 1. Prior to this outage, generator 1 generates 250 MW. System performance for this scenario is illustrated in Fig. 6. Note that maximum frequency deviation is 0.90 Hz.

The simulations illustrate that as the number of generators participating in the load-frequency control problem decreases, the frequency deviations under transients increase and last longer. Of course such

![](/api/attachments/NKEGJSR7/fulltext/images/0d087c811643d30dd5c09fad502e0243845589d22b0ca99f1c3a12f640f4bdbc.jpg)  
Fig. 4. System performance during Scenario 1.

![](/api/attachments/NKEGJSR7/fulltext/images/1c6818e947c66785fedfd355308d82b4d8a0acbb81a0e233fde789c9cec00f2c.jpg)  
Fig. 5. System performance during Scenario 2.

system response may trigger under-frequency relays and additional oscillations.

## 4. Conclusions

Load-frequency control in a deregulated environment may result in free choice by units to participate or not in this operation. It is shown that if the percentage of the units participating in this control action is very small, system performance deteriorates to a point that is unacceptable. It is therefore recommended that minimum requirements be established. The minimum requirements are system-dependent. Extensive studies may be needed to establish acceptable limits of nonparticipation to the load-frequency control problem.

## Acknowledgements

This research has been supported by ONR Grant No. N00014-96-1-0926 and by NATO Collaborative Research Grant CRG.960101.

## References

<sup>w</sup> <sup>x</sup> 1 IEEE Std 95, Definitions for Terminology for Automatic Generation Control on Electric Power Systems.

<sup>w</sup> <sup>x</sup> 2 F.P. DeMello, R.J. Mills, W.F. B’Rells, Automatic Generation Control: Part I. Process Modelling, Paper T72 598-1, 1972 IEEE-PES Summer Meeting, San Francisco, CA, July 19972.

<sup>w</sup> <sup>x</sup> 3 F.P. DeMello, R.J. Mills, W.F. B’Rells, Automatic Generation Control: Part II. Digital Control Techniques, Paper T72 487-7, 1972 IEEE-PES Summer Meeting, San Francisco, CA, July 1972.

![](/api/attachments/NKEGJSR7/fulltext/images/4d28a1df3e7c3a64d19650a0759dc4e5038d81aa5171d83148c34521c7afec89.jpg)  
Fig. 6. System performance during Scenario 3.

A.P. Sakis Meliopoulos M ’76, SM ’83, F ’93 was born inŽ . Katerini, Greece, in 1949. He received the ME and EE diploma from the National Technical University of Athens, Greece, in 1972; the MSEE and PhD degrees from the Georgia Institute of Technology in 1974 and 1976, respectively. In 1971, he worked for Western Electric in Atlanta, Georgia. In 1976, he joined the Faculty of Electrical Engineering, Georgia Institute of Technology, where he is presently a professor. He is active in teaching and research in the general areas of modeling, analysis, and control of power systems. He has made significant contributions to power system grounding, harmonics, and reliability assessmen of power systems. He is the author of the books, Power Systems Grounding and Transients, Marcel Dekker, June 1988, Lightning and OÕerÕoltage Protection, Section 27, Standard Handbook for Electrical Engineers, McGraw-Hill, 1993, and the monograph, Numerical Solution Methods of Algebraic Equations, EPRI monograph series. Dr. Meliopoulos is a member of the Hellenic Society of Professional Engineering and the Sigma Xi.

George Cokkinides M ’85 was born in Athens, Greece, in 1955.Ž . He obtained his BS, MS, and PhD degrees from the Georgia Institute of Technology in 1978, 1980, and 1985, respectively. From 1983 to 1985, he was a research engineering at the Georgia Tech Research Institute. Since 1985, he has been with the University of South Carolina where he is presently an Associate Professor of Electrical Engineering. His research interests include power system modeling and simulation, power electronics applications, power system harmonics, and measurement instrumentation. Dr. Cokkinides is a member of the IEEE<sup>r</sup>PES and the Sigma Xi.
