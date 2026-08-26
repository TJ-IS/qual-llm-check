---
otero_id: 20907
otero_key: "QVRN4RQU"
title: "Trends in power system protection and control"
authors: "Miroslav Begovic; Damir Novosel; Mile Milisavljevic"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00104-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Trends in power system protection and control

Miroslav Begovic <sup>a,)</sup>, Damir Novosel <sup>b</sup>, Mile Milisavljevic <sup>a</sup>

School of Electrical and Computer Engineering, Georgia Institute of Technology, Atlanta, GA 30332-0250, USA b ETS Institute, ABB Power T&D, Raleigh, NC 27606, USA

## Abstract

As a consequence of deregulation, competition and problems in securing capital outlays for expansion of the infrastructure, modern power systems are operating at ever-smaller capacity and stability margins. Traditional entities involved in securing adequate protection and control for the system may soon become inadequate, and the emergence of the new participants non-utility generation, transmission and distribution companies requires coordinated approach and careful Ž . coordination of the new operating conditions. The paper reviews the key issues and design considerations for the present and new generation of SPS and emergency control schemes, and evaluates the strategies for their implementation. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Wide area protection; Power system blackouts; Phasor measurements; Voltage stability; Angular stability; Out-of-step relaying

## 1. Introduction

System-wide disturbances in power systems are a challenging problem for the utility industry because of the large scale and the complexity of the power system. When a major power system disturbance occurs, protection and control actions are required to stop the power system degradation, restore the system to a normal state and minimize the impact of the disturbance. The present control actions are not designed for a fast-developing disturbance and may be too slow. Further, dynamic simulation software is applicable only for off-line analysis. The operator must, therefore, deal with a very complex situation and rely on heuristic solutions and policies. Today, local automatic actions protect the system from the propagation of the fast-developing emergencies.

However, local protection systems are not able to consider the overall system, which may be affected by the disturbance.

The trend in power system planning utilizes tight operating margins with less redundancy, because of new constraints placed by economical and environmental factors. At the same time, addition of nonutility generators and independent power producers, an interchange increase, an increasingly competitive environment and introduction of FACTS devices make the power system more complex to operate and to control and, thus, more vulnerable to a disturbance. On the other hand, the advanced measurement and communication technology in wide-area monitoring and control, FACTS devices better tools toŽ control the disturbance and new paradigms fuzzy . Ž logic and neural networks may provide better ways . to detect and control an emergency.

Better detection and control strategies through the concept of wide-area disturbance protection offer a better management of the disturbances and significant opportunity for higher power transfers and operating economies 2,4 . Wide area disturbance protec-<sup>w</sup> <sup>x</sup> tion is a concept of using system-wide information and sending selected local information to a remote location to counteract propagation of the major disturbances in the power system. With the increased availability of sophisticated computer, communication and measurement technologies, a more AintelligentB equipment can be used at the local level to improve the overall emergency response.

Decentralized subsystems, that can make local decisions based on local measurements and remote information system-wide data and emergency con- Ž trol policies and. <sup>r</sup>or send preprocessed information to higher hierarchical levels are an economical solution to the problem. A major component of the system-wide disturbance protection is the ability to receive system-wide information and commands via the data communication system and to send selected local information to the supervisory control and data acquisition SCADA center. This information should Ž . reflect the prevailing state of the power system.

## 2. Types of disturbances and remedial measures

The phenomena that create the power system disturbance are divided into the following categories: angular stability, voltage stability, overload and power system cascading.

## 2.1. Angular stability

The objective of out-of-step protection as it is applied to generators and systems is to eliminate the possibility of damage to generators as a result of an out-of-step condition. In the case where the power system separation is imminent, it should take place along boundaries, which will form islands with matching load and generation. Distance relays are often used to provide an out-of-step protection function, whereby they are called upon to provide blocking or tripping signals upon detecting an out-of-step condition.

The most common predictive scheme to combat loss of synchronism is the equal-area criterion and its variations. This method assumes that the power system behaves like a two-machine model where one area oscillates against the rest of the system. Whenever the underlying assumption holds true, the method has potential for fast detection.

## 2.2. Voltage stability

Voltage stability is defined by the System Dynamic Performance Subcommittee of the IEEE Power System Engineering Committee 9 as being the ability of a system to maintain voltage such that when load admittance is increased, load power will increase, and so that both power and voltage are controllable. Also, voltage collapse is defined as being the process by which voltage instability leads to a very low voltage profile in a significant part of the system.

It is accepted that this instability is caused by the load characteristics, as opposed to the angular instability, which is caused by the rotor dynamics of generators.

The risk of voltage instability increases as the transmission system becomes more heavily loaded. The typical scenario of these instabilities starts with a high system loading, followed by a relay action either due to a fault, a line overload or hitting an excitation limit 5,6 .<sup>w</sup> <sup>x</sup>

Voltage instability can be alleviated by a combination of the following remedial measures means: adding reactive compensation near load centers, strengthening the transmission lines, varying the operating conditions, such as voltage profile and generation dispatch, coordinating relays and controls, and load shedding. Most utilities rely on planning and operation studies to guard against voltage instability. Many utilities utilize localized voltage measurements in order to achieve load shedding as a measure against incipient voltage instability 8 .<sup>w</sup> <sup>x</sup>

## 2.3. OÕerload and power system cascading

Outage of one or more power system elements due to the overload may result in overload of other elements in the system. If the overload is not alleviated in time, the process of power system cascading may start, leading to power system separation. When a power system separates, islands with an imbalance between generation and load are formed with a consequence of frequency deviation from the nominal value. If the imbalance cannot be handled by the generators, a load or generation shedding is necessary. The separation can also be started by a special protection system or out-of-step relaying.

A quick, simple and reliable way to reestablish active power balance is to shed load by underfrequency relays. There are a large variety of practices in designing load-shedding schemes based on the characteristics of a particular system and the utility practices 3,7 .<sup>w</sup> <sup>x</sup>

While the system frequency is a final result of the power deficiency, the rate of change of frequency is an instantaneous indicator of power deficiency and can enable incipient recognition of the power imbalance. However, change of the machine speed is oscillatory by nature, due to the interaction among generators. These oscillations depend on location of the sensors in the island and the response of the generators. The problems regarding the rate of change of frequency function are the following 1 .<sup>w</sup> <sup>x</sup>

v A smaller system inertia causes a larger peakto-peak value for oscillations. For the larger peakto-peak values, enough time must be allowed for the relay to calculate the actual rate of change of frequency reliably. Measurements at load buses close to the electrical center of the system are less susceptible to oscillations smaller peak-to-peak values and can Ž . be used in practical applications. A smaller system inertia causes a higher frequency of oscillations, which enables faster calculation of the actual rate of change of frequency. However, it causes faster rate of change of frequency, and, consequently, a larger frequency drop.

v Even if the rate of change of frequency relays measures the average value throughout the network, it is difficult to set them properly, unless typical system boundaries and imbalance can be predicted. If this is the case e.g. industrial and urban systems ,Ž . the rate of change of frequency relays may improve a load-shedding scheme scheme can be more selec-Ž tive and<sup>r</sup>or faster ..

v Adaptive settings of frequency and frequency derivative relays may enable implementation of a frequency derivative function more effectively and reliably. This will be discussed later.

## 3. Possible improvements in control and protection

Existing protection<sup>r</sup>control systems may be improved and new protection<sup>r</sup>control systems may be developed to better adapt to prevailing system conditions during system-wide disturbance. While improvements in the existing systems are mostly achieved through advancement in local measurements and development of better algorithms, improvements in new systems are based on remote communications. However, even if communication links exist, systems with only local information may still need improvement since they are envisioned as fallback positions.

The modern energy management system EMSŽ . can provide system-wide information for the network control and protection. The EMS is supported by SCADA software and various power system analysis tools. The increased functions and communication ability in today’s SCADA systems provide the opportunity for an intelligent and adaptive control and protection system for system-wide disturbance. This, in turn, can make possible full utilization of the network, which will be less vulnerable to a major disturbance.

## 3.1. Angular stability

Out-of-step relays have to be fast and reliable. The increased utilization of transmission and generation capacity, as well as the increased distance of power transmission, are some of the factors that cause an out-of-step situation to develop rapidly. The interconnected nature of power systems cause large geographic areas to be affected by an out-of-step condition. The present technology of out-of-step tripping or blocking distance relays is not capable of fully dealing with the control and protection requirements of power systems.

Central to the development effort of an out-of-step protection system is the investigation of the multiarea out-of-step situation. The new generation of out-of-step relays has to utilize more measurements, both local and remote, and has to produce more outputs. The structure of the overall relaying system has to be distributed and coordinated through a central control. In order for the relaying system to manage complexity, most of the decisions have to be taken locally. The relay system is preferred to be adaptive in order to cope with system changes. To deal with out-of-step prediction, it is necessary to start with a system-wide approach, find out what sets of information are crucial and how to process information with acceptable speed and accuracy.

## 3.2. Voltage instability

The protection against voltage instability should also be addressed as a part of hierarchical structure. Decentralized actions are performed at substations with local signals and signals obtained from slow communication with other substations and<sup>r</sup>or central level e.g. using SCADA data . The higher hierarchi-Ž . cal level requires more sophisticated communication of relevant system signals and coordination between the actions of the various substations.

The recommended approach for designing the new generation of voltage instability protection is to first design a voltage instability relay with only local signals 10 . The limitations of local signals should <sup>w</sup> <sup>x</sup> be identified in order to be in a position to select appropriate communicated signals. However, a minimum set of communicated signals should always be known in order to design a reliable protection, and it requires the following: a determining the algorithmŽ . for gradual reduction of the number of necessary measurement sites with minimum loss of information necessary for voltage stability monitoring, analysis and control; b development of methods i.e. sensi-Ž . Ž tivity analysis of reactive powers , which should. operate concurrent with any existing local protection techniques, and possessing superior performance, both in terms of security and dependability.

## 3.3. Power system cascading and load-shedding strategies

Conventional load-shedding schemes without communications are not adaptive to system conditions, which are different from the one used in the load-shedding design. For the relays to adapt to the prevailing system conditions, their settings should change based on the available spinning reserve, total system inertia, and load characteristics. These values may be periodically determined at the central site from SCADA data and provided to the relays using low speed communications.

In addition, the actual load, which would represent an assigned percentage for shedding at each step, may be periodically calculated at a central site based on the actual load distribution. However, the system characteristics may change depending on the separation points. If the separation is controlled from a central site or can be predicted, an algorithm may calculate the settings and assign the appropriate load in coordination with switching actions. However, high-speed communication may be required to and from the central location for fast-developing disturbances, such as multi-machine angular instability. Another aspect may be adding a correction element to a scheme. If only slow speed communications are available, a fast load-shedding scheme may be implemented to stop system degradation. When adequate information is available, corrective measures may be applied.

If the composite system inertia constant is known, the actual power imbalance may be calculated directly from the frequency. This detection should be fast to avoid a large frequency drop and done at theŽ . location close to the center of inertia. High-speed communications are required to initiate load shedding at different power system locations. Further, changes of load and generation, with frequency and in particular voltage, impact the power imbalance and calculation of the average of the frequency derivative. In addition, the power system imbalance changes after the initial disturbance due to dynamic system changes.

Thus, relay settings should be based on the spinning reserve, total system inertia, and load characteristics and distribution. In conclusion, sophisticated models and<sup>r</sup>or high-speed communication may be required for accurate estimation of the amount and distribution of the load to be shed. If communications are available, it is easier and more reliable to calculate the amount of load to shed from the switching information and the mismatch based on data onŽ load and generation before the separation in the. island.

To avoid disadvantages of the underfrequency load shedding and difficulties with implementing the rate of change of frequency function, the automated load shedding that will reduce overloading or prevent system instability before the system is isolated is proposed as an advantageous strategy.

## 4. Example: angular stability

An algorithm for predicting the location at which an out of step can take place following a disturbance in a large-scale system is shown as an example of the hierarchical protection and control strategies using communications. To implement this scheme, one needs a central computer that receives information from across the system. The sets of crucial information that require fast communications consist of generator speeds, and changes in line status. Other information needed by the algorithm are generation and load levels. Using these sets of information, a simple and quick processing method is able to tell, with a high degree of accuracy, 1 whether an out of step isŽ . imminent, and 2 the boundary across which this outŽ . of step will take place. This algorithm has been tested thoroughly using a Monte Carlo-type approach. At each test, random values are assigned to line impedances, load, generator inertias, as well as disturbance location. It is found that the algorithm is capable of making accurate prediction.

To illustrate how the algorithm works, consider the power system shown in Fig. 1. This system is a modified version of the IEEE 39-bus test system. In Fig. 1, each generator is marked with a circle, and each load with a square; the size of each symbol indicates relatively the power generated or consumed at the node. For example, generator 34 supplies more active power to the grid than does generator 38.

![](/api/attachments/QVRN4RQU/fulltext/images/951444da90338de57daf12d3e44ad307639f5a16018e2a0d6e7363f327bbe313.jpg)  
Fig. 1. Graph of the 39-bus test system.

![](/api/attachments/QVRN4RQU/fulltext/images/f2393761c7160e9d322de7a48c59469f4d3208cdd9a3135800d9d8da288581fc.jpg)  
Fig. 2. Time domain simulation of the system.

A disturbance is introduced to the system where two lines are simultaneously removed each line isŽ marked by an ‘x’ in Fig. 1 . This information is fed. to the algorithm, which predicts that an out of step will occur across the line 2–25. Fig. 2 reveals that the two generators 37 and 38 eventually separate from the other generators. All line angles have been checked and none but line 2–25 indicate the boundary of the out of step. The angle of critical line is shown in Fig. 3. This confirms the result of the algorithm.

Such an algorithm requires a centralized scheme and high-speed communication links across the wide system. Decentralized scheme requires communications with a central location. According to this hierarchical scheme, each regional computer issues control actions to alleviate problems that are imminent

![](/api/attachments/QVRN4RQU/fulltext/images/df921c7448f5aadb17637fdadbda57e907365ba67092bd1abfef8299d27b12b7.jpg)  
Fig. 3. Angle of critical line.  
within its jurisdiction; the coordination among regions is left to the central computer.

## 5. Example: thyristor-controlled series compensator TCSC control( )

In this section, we briefly present a method for online detection of inter-area oscillations. The method does not require the topological knowledge of the system and is based on the spectral characteristics of the locally observable data. Moreover, we introduce a different approach to the power system stabilization. We apply the globally available information about the system to the adaptation of TCSC. The control we propose attempts to optimally adjust the line admittance on sample to sample basis in order to reduce the inter-area oscillations in the power systems. We explain how such approach may combine the global system information with locally observable quantities and eventually result in the damping of inter-area modes.

## 5.1. Power system modeling and spectral characteristics

We consider a generic N-machine, p-bus power system described by the following swing equation:

$$
M _ {i} \Delta \dot {\omega} _ {i} = - D _ {i} \Delta \omega_ {i} + P _ {\mathrm{a} i} (t)
$$

$$
\Delta \delta_ {i} = \omega_ {\mathrm{B}} \Delta \omega_ {i}
$$

where $\varDelta \delta _ { i }$ and $\Delta \omega _ { i }$ represent the deviation of the rotor angle and its speed relative to the synchronous reference frame, $P _ { \mathrm { a } i } ( t )$ is the accelerating power, i.e. imbalance between the mechanical and mechanical power, $M _ { i }$ is the inertia constant for machine i, $\omega _ { \mathrm { B } }$ is the synchronous angular frequency, and $D _ { i }$ is the damping factor corresponding to the machine i. Swing equation can be linearized to obtain:

$$
\Delta \dot {\boldsymbol {x}} = \mathbf {A} \Delta \boldsymbol {x} + B \Delta \boldsymbol {u}
$$

where vector x is the vector obtained by concatenating rotor angle deviation vector and rotor speed deviation vector, and u is the vector of power imbalances for each machine. Eigenanalysis of matrix A, and its participation factors can now obtain information about possible modes of the system.

This, however, is not the only way that the information on the oscillatory modes can be obtained. In a system subject to the impulse excitation, the oscillatory modes can be determined from the power spectral density of the system response. In other words, the modes would appear as peaks of the power spectral density function of state variable x calculated as:

$$
S _ {x _ {i}} (\omega) = F _ {t} \left\{\int_ {- \infty} ^ {+ \infty} x _ {i} ^ {*} (\tau) x _ {i} (t - \tau) d \tau \right\}
$$

where F represents the Fourier transformation. Peaks of the power spectral density correspond to the modes of the inter-area oscillations, and can be, therefore, determined from measurements of x over a time window, if we consider x as a time-frequency distribution.

The descriptive measurement quantity we use is Ž . the machine speed. We think of inter-area oscillations as energy exchanges between the groups of the machines. This energy exchange should be visible from the machine speed data. Moreover, the machine speed is easily measurable quantity, thus making a perfect candidate for descriptive quantity for a pattern recognition task. The algorithm we propose are the following:

v Collect machine speed data;

v Perform spectrum estimation on machine speed data;

v Identify the frequencies of possible modes of inter-area oscillations;

v Perform clustering on the phases of machine spectrum data at inter-area frequencies;

![](/api/attachments/QVRN4RQU/fulltext/images/eefbc8ba49922a0c70f52f78105043dded7f74a92c77bc8e66122ba92c6f66ee.jpg)  
Fig. 4. Transient disturbance of the test system as described in the text below.

v Identify inter-area groups with clusters of phases of machine spectrum data.

We illustrate the performance of the algorithm on the following example: Fig. 4 shows the machine speeds of the 16 machine 64-bus NPCC system subject to the fault on line between busses 28 and 29. The fault is cleared by tripping the line after three cycles but still divides machines in three groups, thus producing the inter-area oscillations. In this simulation, we used the transient model for synchronous machines. It is obvious that the system is divided into three groups that oscillate against each other. In one group, we have machines 1–8, in the second group, machines 11–13 and all other machines oscillate by themselves. Modal analysis of the linearized system reveals five oscillatory modes under 1 Hz: at 0.4150, 0.5564, 0.7326, 0.8066, and one at 0.9825 Hz. Participation factor analysis indicates that machines most likely to oscillate at 0.415 Hz are machines 1–9 and 13–16. Machine 15 seems very prone to the mode at 0.5 Hz, machines 10–13 are susceptible to the mode at 0.7326 Hz, and machines 14–16 are prone to oscillatory mode at 0.8066 Hz. We use the phase angles of the power spectral density at the given mode to determine the group to which machine belongs. The phase data is summarized in Table 1. Indeed, machines 1–8 have the phase angle of approximately 118, machines 11, 12 and 13 have phase angles of approximately 38, while phase angles of speed spectra of other machines do not belong to any of the groups.

Table 1  
Phase angles of the power spectral density at the interarea oscillation mode at 0.4 Hz

<table><tr><td>Machine number</td><td>Speed PSD phase at 0.4 Hz (°)</td></tr><tr><td>1</td><td>11.6975</td></tr><tr><td>2</td><td>10.3086</td></tr><tr><td>3</td><td>10.8000</td></tr><tr><td>4</td><td>12.5058</td></tr><tr><td>5</td><td>12.1250</td></tr><tr><td>6</td><td>12.0467</td></tr><tr><td>7</td><td>12.6263</td></tr><tr><td>8</td><td>12.4726</td></tr><tr><td>9</td><td>25.6914</td></tr><tr><td>10</td><td>8.2753</td></tr><tr><td>11</td><td>3.2167</td></tr><tr><td>12</td><td>3.5110</td></tr><tr><td>13</td><td>2.7732</td></tr><tr><td>14</td><td>63.4004</td></tr><tr><td>15</td><td>144.1611</td></tr><tr><td>16</td><td>195.3319</td></tr></table>

We propose to use the information about groups of machines belonging to inter-area modes to formulate an emergency control by modulating the admittance of the TCSC. The control we propose is based on the premise that we only want to enhance the stability of the system by applying the admittance adjustment control. The main control still relies on power system stabilizers, which usually perform this task very well. We would like to use the admittance control to minimize the inter-area oscillations, which are exhibited as the flow of energy between machines or groups thereof. We use the rate of change of machine speeds as an indication of the energy change at particular machine. In that sense, we would keep the undesirable variations of the machine velocities to their minimum, reducing the energy transfers between different groups of machines. In turn, reduced energy exchange reduces the inter-area oscillations, which is the goal of our control. While this type of control does not guarantee the stability, it does guarantee that the Lyapunov exponents of a system with such control will be smaller than the ones of the system without the control. This is a result of the facts that machine states are the state variables of linearized system, and that the logarithm is a monotonous function. In that sense, the system is more stable than the system without the control.

Moreover, the proposed type of control can be computed with a cost of QR decomposition for the matrix of sensitivity coefficients and one matrix multiplication. In addition, this type of the control guarantees the minimum energy solution, i.e. minimum per-sample change of line admittances. The stability of the control computation procedure, low computational cost, and easy parallelization of the process this algorithm very appealing for the real-time applications on multiprocessor architectures.

## 5.2. Minimum energy control

It was stipulated that the changes in machine speeds are an indicator of inter-area oscillations. Moreover, the change of machine speeds indicates the direction of the energy fluctuations. The reduction of machine speed changes does, therefore, reduce the inter-area oscillations. Per-sample machine speed change can be written in the following form:

$$
\Delta \dot {\omega} _ {k} \mathrm{d} t = \Delta \omega_ {k + 1} - \Delta \omega_ {k} = \mathbf {A ^ {\prime}} \left[ \begin{array}{l} \Delta \delta_ {k} \\ \Delta \omega_ {k} \end{array} \right] + P \Delta y
$$

where P is the sensitivity of the machine speed changes with respect to the line admittance. By setting $\begin{array} { r } { \varDelta \omega _ { k } \mathrm { d } t = 0 , } \end{array}$ , the control is computed as the solution of following equation:

$$
P \Delta y = \mathbf {A} ^ {\prime} \left[ \begin{array}{c} \Delta \delta_ {k} \\ \Delta \omega_ {k} \end{array} \right]
$$

In contrast to this optimization, control of system modes would imply the minimization of . Since TCSC devices present a permanent change in the topology of a power network, their location needs to be determined before the fault has occurred. Having this in mind, TCSC selection process has to consider several criteria.

v Various and possibly multiple faults may happen.

v All machines need to be controlled at the same time to insure the control of all inter-area modes Žthis condition may be relaxed by adaptive tracking of the inter-area groups ..

v Since all machines participating in a certain interarea mode will have similar angles and rates of change of angles speeds , it is technically possibleŽ . to use just a representative machine from a group. This may be useful in speeding up the control processing to enable real-time control.

v The above two tasks have to be performed with minimum change of the line admittances since the TCSC devices have range typically limited to a certain percentage of the nominal line admittance, for a variety of reasons.

v The above considerations exclude the a priori knowledge of the fault location.

Taking into account the above consideration, selection process may be based on an extensive sensitivity analysis spanning a large number of situations, either by using some form of a composite objective function, or by applying some effective means of combinatorial optimization, such as genetic algorithms. The end result is the allocation of a limited number of TCSC controllers, which perform reasonably well over a finite set of different disturbance scenarios.

![](/api/attachments/QVRN4RQU/fulltext/images/415a0f1e5629426de38a781be19725bf79015dcc8bb184c504c10ced01def26b.jpg)  
Fig. 5. Comparison of the machine a16 speeds fault as per Fig. 4 : - - -, Original speed in center of inertia reference frame. No control isŽ . applied. . . . , Machine a 16 speed with TCSC modulation control. -<sup>P</sup>-<sup>P</sup>-, Machine a 16 speed with power system stabilizer control. —, Machine a 16 speed with both PSS and TCSC controls applied.

The results of some comparative tests, obtained by time-domain simulation on the system and fault used in, are shown in Fig. 5. The presented scenarios involve situations when no control was applied to the system under disturbance, and when group of five optimally selected and tuned PSS and five TCSC was applied, both separately and altogether.

The opportunity to speed up processing in power system stabilizing devices to enable real-time control is in the inclusion of the distributed architectures, which combine low per-unit cost with high efficiency. The control algorithm we have described in the previous section can be easily implemented in the parallel architecture with great reduction of complexity and large parallel efficiency.

## 6. Conclusion

A large disturbance, such as a sudden outage of a transmission line, may trigger a sequence of events leading to machine swings, voltage problem and eventually power outage in a large area of the system. The role of a protection and control system is to timely predict the system instability, to perform actions to restore the system to a normal state and to minimize the impact of the disturbance.

As the communications and computer technology continue to improve, and protection and control becomes more integrated, an application of adaptive system-wide protection is becoming more feasible. Since any improvement in system-wide protection and control products provides significant savings to utility, the decentralized systems that provide improved and economical solution for the system-wide disturbance problems are very attractive.

Automated load shedding that will reduce overloading before the system is isolated is an improved solution in comparison to underfrequency load shedding. Although local measurements may suffice if tasks are simple e.g. protection against few contin- Ž gencies only , information communicated either from . central location or from remote substation seems necessary for more sophisticated requirements.

Microprocessor-based coordinated protection, monitoring and control systems are the key to innovations in power system operating philosophy. The coordinated system is clearly the future of relaying technology.

As the communications and computer technology continue to improve, and protection and control become more integrated, the application of the adaptive wide-area disturbance protection concept is becoming more feasible. Since any improvement in the wide-area protection and control strategy provides significant savings to the utility, the intelligent systems that provide improved and economical solution for the wide-area disturbance problems are very attractive. Intelligent emergency control systems i.e. Ž systems described in the paper provide more secure . operation and better emergency responses, allowing utilities to operate at closer transmission and generation margins.

## Acknowledgements

Part of the work presented in this paper was funded by the National Science Foundation under Grant aECS-9404895. We gratefully acknowledge this assistance.

## References

<sup>w</sup> <sup>x</sup> 1 A. Apostolov, D. Novosel, D.G. Hart, Intelligent protection and control during power system disturbance, 56th Annual APC, Chicago, April, 1994.

<sup>w</sup> <sup>x</sup> 2 L. Cederblad, T. Cegrell, A new approach to security control of power systems-local protection coordinated with systemwide operation, IFAC Symposium, Brussels, September, 1988.

<sup>w</sup> <sup>x</sup> 3 L.H. Fink et al., Emergency control practices, IEEE Trans. Power Appar. Syst. 104 1985 2336–2441, September. Ž .

<sup>w</sup> <sup>x</sup> 4 A.P.J. Malt et al., Computer based supervisory control and energy management system for the city of Cape Town, IEE Proc. 135 1988 41–50, January.Ž .

<sup>w</sup> <sup>x</sup> 5 NERC Planning Standards and Guides, ASystem Protection and ControlB, Draft, North American Electric Reliability Council, Interconnection Dynamics Working Group of the NERC Engineering Committee, 1997.

<sup>w</sup> <sup>x</sup> 6 Proceedings of Bulk Power System Voltage Phenomena: III. Voltage Stability, Security and Control. Davos, Switzerland, August, 1994.

7 System Disturbances: 1986–1997 North American Electric Reliability Council, NERC Reports.

<sup>w</sup> <sup>x</sup> 8 System Protection and Voltage Stability, IEEE Power System

Relaying Committee, IEEE Publication, 93THO596-7 PWR, 1993.

<sup>w</sup> <sup>x</sup> 9 Voltage Stability of Power Systems: Concepts, Analytical Tools, and Industry Experience, IEEE Publication, 90TH-0358-2-PWR, 1990.

<sup>w</sup> <sup>x</sup> 10 K. Vu, M. Begovic, D. Novosel, M. Saha, Use of local measurements to estimate voltage-stability margin, Proceedings of the PICA 1997 Conference, May 11–16, 1997.

![](/api/attachments/QVRN4RQU/fulltext/images/a509fe0413408422ddd342da6f6e63bf2ea3a128b68f85f02e1f5ab400136c82.jpg)

Miroslav Begovic is an Associate Professor of Electrical Engineering at the Georgia Institute of Technology in Atlanta, GA. He obtained his PhD degree in Electrical Engineering from Virginia Polytechnic Institute and State University, following which he accepted a faculty position at Georgia Tech. His area of research is application of real-time monitoring and control in power systems. He chairs a Working Group on Wide Area Protection and Control within

the IEEE PES Power System Relaying Committee. Dr. Begovic is a Senior Member of IEEE, and a member of Sigma Xi, Tau Beta Pi, Eta Kappa NU, and Phi Kappa Phi.

![](/api/attachments/QVRN4RQU/fulltext/images/d39b3f8c24098aed2d4532b2546ebbe7598a248063be404259537af4202050e3.jpg)

Damir Novosel is the R&D Technology Manager for Applications<sup>r</sup>Products in Substation Automation within ABB T& D Technology in Baden, Switzerland, and the R&D Manager in Electric Systems Technology Institute of ABB Power T&D in Raleigh, NC. Dr. Novosel obtained his PhD degree in Electrical Engineering from the Mississippi State University, and has held a variety of research and managerial positions after that. His research has been centered

around applications of advanced protection and control technology in power systems. Dr. Novosel is the Vice-Chairman of the System Protection Subcommittee of the IEEE PES Power Systems Relaying Committee, and a Senior Member of the IEEE.

![](/api/attachments/QVRN4RQU/fulltext/images/e4eac96e9dae88179d6a73a212c7345b92946faa6b0bb453f2da1be85ded5ba2.jpg)

Mile Milisavljevic is a graduate student of Electrical Engineering in the School of Electrical and Computer Engineering at Georgia Institute of Technology. His research interests are in applications of modern control theory to large-scale systems.
