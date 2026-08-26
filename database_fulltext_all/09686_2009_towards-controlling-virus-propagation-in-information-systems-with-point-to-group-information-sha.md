---
otero_id: 9686
otero_key: "XGPV2B6K"
title: "Towards controlling virus propagation in information systems with point-to-group information sharing"
authors: "Hua Yuan; Guoqing Chen; Junjie Wu; Hui Xiong"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.05.014"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards controlling virus propagation in information systems with point-to-group information sharing

Hua Yuan <sup>a,</sup>⁎, Guoqing Chen <sup>a</sup>, Junjie Wu <sup>b</sup>, Hui Xiong <sup>c</sup>

<sup>a</sup> Department of Management Science and Engineering, Tsinghua University, China

<sup>b</sup> School of Economics and Management, Beihang University, China

<sup>c</sup> Management Science and Information Systems Department, Rutgers University, USA

## a r t i c l e i n f o

Article history: Received 14 May 2008 Received in revised form 7 April 2009 Accepted 20 May 2009 Available online 23 June 2009

Keywords: Information security Virus propagation Antivirus countermeasures E-SEIR model Point-to-group information sharing

## a b s t r a c t

Nowadays, for information systems at organizational and interorganizational levels, information sharing is essential for business operations and strategic decision-making. As a mixed blessing, however, the information sharing process also exposes information systems to more severe virus attacks. In light of this, research efforts on virus propagation and virus control have drawn increasing interests in both the academic and industrial domains. This paper thus presents a virus propagation model, namely E-SEIR, to gain insights of virus propagation in networks with Point-to-Group (P2G) information sharing patterns. Unlike most existing virus propagation models, E-SEIR has three important characteristics. First, an additional exposed state is integrated into the model to describe the latent period of computer viruses. Second, a P2G infection function is introduced to the model to characterize the real-world networks, which consist of many information-sharing sub-networks. Third, E-SEIR takes various antivirus countermeasures into consideration, which provides unique opportunities for studying the behaviors of virus propagation with the presence of antivirus activities. Based on this E-SEIR model, we have studied the possibility of short-term virus outbreaks and long-term network survivability, and the results revealed some key managerial insights that are helpful for the practice of virus propagation control in information sharing networks.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Recent years have witnessed the explosion of attacks on information resources in worldwide organizations. Among all these attacks, computer virus poses a major threat to the information security for business effectiveness and continuity [38]. For instance, the Computer Security Institute (CSI) report [8] shows that virus caused the biggest <sup>fi</sup>nancial loss among all computer security incidents in organizations. Therefore, there is a critical need to understand and control virus propagations in organizations' information systems.

Along this line, an increasing effort has been made to adopt biological epidemic models for understanding virus propagations in computer networks. Indeed, biological analogy allows security researchers to better understand the threat posed by virus propagation. As an example, in biological propagation models, one fundamental insight is that there is an epidemic threshold above which a virus may spread, and below which it cannot [25,30].

In computer network scenarios, researchers obtained theoretical results which are similar to those of the classic biological propagation theories [6,39,40]. Previous studies based on biological epidemic models have shown that the spread of computer viruses is dramatically affected by the characteristics of the underlying computer networks [10,23,26,29,33,34]. However, few studies address the impact of user behaviors, such as frequent information sharing in a workgroup [22,45], on the virus propagation. So there is a critical need to study virus propagation from a managerial perspective. This paper thus <sup>fi</sup>lls this crucial void by modeling the virus propagation in an organization level network with information sharing subgroups. Various antivirus countermeasures and strategies are also extensively studied based on that model.

Speci<sup>fi</sup>cally, based on the traditional SEIR model, we <sup>fi</sup>rst present a virus propagation model named E-SEIR for gaining managerial insights of computer virus propagation in information sharing networks. The E-SEIR model has four states: susceptible, exposed, infective, and recovered as well as seven state transition paths, which enable it to better capture the behaviors of virus propagation in realworld information systems. In fact, the E-SEIR model has three important characteristics. First, an additional exposed state has been integrated into the E-SEIR model. The use of the exposed state well describes the existence of the latent period of many viruses before triggered automatically or by the users. Second, real-world networks usually include many information-sharing sub-networks, for example, the logical network de<sup>fi</sup>ned by an e-mail address relationship [49]. To model this information sharing pattern, a point-to-group infection function has been included in the E-SEIR model. Third, based on the established multi-paths for state transitions, E-SEIR can take various antivirus countermeasures into consideration. This provides an opportunity for studying the behaviors of virus propagation with the presence of antivirus activities.

Finally, based on this E-SEIR model, we have studied the possibility of short-term virus outbreaks and long-term network survivability. The results reveal four key managerial insights: 1) If there are few antivirus countermeasures deployed in the system, the system will be evolved into a non-healthy stage of virus spread. However, before the system reaches this stage, there are several short-term virus outbreaks; 2) It is more dif<sup>fi</sup>cult to control short-term virus outbreaks than the prevention of long-term virus existing in the system; 3) Immunization cannot completely prevent short-term virus outbreaks, but can save the costs caused by virus outbreaks; 4) We can effectively reduce the risk of virus outbreaks by deploying antivirus countermeasures for information nodes at the exposed state.

The remainder of this paper is organized as follows. Section 2 describes related work in the literature. In Section 3, we introduce a new infection function and construct the virus propagation model named E-SEIR. Section 4 analyzes the virus propagation with the longterm stability of the E-SEIR system. In Section 5, we provide the parameter $C _ { S }$ that is critical for the control of short-term virus infection outbreaks. Section 6 provides a C -based antivirus strategy to realize the virus propagation control in practice. In Section 7, we present experimental results. Finally, Section 8 concludes this paper.

## 2. Related work

Computer virology was established as an emerging discipline in late 1980s [11,31]. Since then, there have been growing interests in using biological models to gain insights of computer virus propagations.

People have observed that there are signi<sup>fi</sup>cant similarities between the spread of computer viruses and biological epidemics [9]. Based on this observation, some biological epidemic models, such as the Susceptible-Infected-Susceptible (SIS) model and Susceptible-Infected-Recovered (SIR) model [1], have been adopted for studying the spread of computer viruses [12,17–20,30,42,46,48]. In the SIS model, each individual in the network is either infected or susceptible to infection, and the state transition is immediate. However, SIS cannot re<sup>fl</sup>ect the effect of virus immunizations, which motivates the so-called SIR model. In the SIR model, the infected individuals can be recovered and further obtain immunity. Nevertheless, the SIR model cannot model the scenario that some viruses go through a latent period before the host becomes infectious. Also, there are some other models, such as SIRS [21], SIDR [43], and SAIR [35], which have the same problem as the SIR model. To address this challenge, one way is to introduce the “exposed” state into the model which takes the latent period into consideration. This leads to the use of the Susceptible-Exposed-Infective-Recovered (SEIR) model developed in biological epidemics [1]. [44] studied the merits of the use of the “exposed” state in characterizing computer virus propagation by comparing the SEIR model with the SIR model in the stability of the state transition parameter.

In addition, people have deployed various antivirus countermeasures to <sup>fi</sup>ght with computer viruses. For instance, the measures such as early monitoring and alarming [7,48], immunization [2,4,20,24,26,34,49], end-user security education and antivirus training [3,13,14,37,41], infected individuals recovery, and equipment quarantine or replacement [5,28,47], have received enormous attention. Recently, Chen and Carley [4] studied the countermeasure competing (CMC) strategy for immunization. However, the studies on these measures are usually qualitative, which cannot provide us with quanti<sup>fi</sup>ed antivirus solutions. In recent years, some researchers found that the combination of virus propagation models and antivirus countermeasures is bene<sup>fi</sup>cial; that is, we can observe the antivirus effect of different measures precisely through the quantitative analysis. Some representative work along this line includes the studies on the impact of immunization [20,24,26,34] and quarantine [5,28,47] based on the SIS/SIR model. Again, these efforts have been limited by the intrinsic problem with the SIS/SIR model.

Indeed, our study is to develop a virus propagation model that can better re<sup>fl</sup>ect virus propagation in information-sharing networks. Our model, named E-SEIR, is a natural extension of the traditional SEIR model. E-SEIR differs from SEIR in three aspects: 1) More state transition paths have been set up to represent the impact of various antivirus countermeasures; 2) the information sharing pattern we consider is “point to group” (P2G) which re<sup>fl</sup>ects the fact that a network usually consists of many information-sharing sub-networks; and 3) the infection mode in our model takes the ineffective infections into consideration which is closer to the real-world scenarios. Then, based on this model, we investigate the strategies to control long-term and short-term virus propagations. For instance, the proposed novel $^ { \mathfrak { n } } C _ { S ^ { - } } \mathrm { c o n t r } 0 ^ { \mathfrak { l } ^ { \prime } }$ strategy will show its appealing merits on the virus propagation control.

## 3. The E-SEIR model

In this section, we describe the E-SEIR model — an extended version of the traditional SEIR model developed in the <sup>fi</sup>eld of epidemiology [1]. Specially, we <sup>fi</sup>rst introduce the four states and seven state transitions in the E-SEIR model. Then, we derive a new infection function for E-SEIR based on the notion of P2G information sharing. Finally, we establish the set of differential equations to characterize the E-SEIR model.

## 3.1. The states and state transitions in E-SEIR

Networks can usually be viewed as graphs with nodes and the links between the nodes. A node in networks can be a PC, a server, a mobile phone or a computerized business unit. These nodes can be the hosts of viruses. In a virus propagation process, these nodes may take any of the following four states:

1. S (susceptible): In this state, the node contains no virus code and can process information normally, but it has no ability in detecting, preventing or cleaning a virus.

2. E (exposed): In this state, the node has been the host of virus, but the virus code has not been activated. In other words, the node can still function normally, but has no intention to detect, recover or clean the virus.

3. I (infective): In this state, the node has been the host of the virus and the virus code has been activated. So the node is infectious and may not function normally.

4. R (recovered): In this state, the node contains no virus code and can function normally, and it has the ability in detecting, preventing, and cleaning the virus.

Initially, all the information nodes in the network are in S-state. Once a virus intrudes into the system, they may change their states according to the rules as follows:

1. For the node in state S, 1) if it can obtain immunity via the antivirus countermeasures, e.g., patching, it will go directly into state R; but 2) if it is infected by a nearby I-state node, it will then go into state E.

2. For the node in state E, 1) if the virus code in it can be cleaned up before loaded, it will return to state S; 2) if it can further obtain immunity via the antivirus countermeasures, it will go directly into state R; however, 3) if the virus code has been loaded into the RAM and triggered by CPU, then it has to go into state I.

3. For the node in state I, it returns to state S if the virus code can be cleaned up, or goes into state R by further obtaining immunity via the antivirus countermeasures.

Fig. 1 shows four states and state transitions in E-SEIR. In the <sup>fi</sup>gure, each circle represents a state and the information nodes that belong to this state. And the directed lines denote the potential transition paths from one state to the another states. The mathematical symbols near the directed lines denote the corresponding transition rates. Note that a transition rate from state A to state B is computed as the ratio of the nodes in A that go into B in a unit time. Also, we assume that our network is in a dynamic equilibrium. This implies that the nodes increase and decrease in a same rate $\mu ,$ as shown by the dash lines in Fig. 1.

Compared with the traditional SEIR model, E-SEIR has more transition paths, which can better capture the impacts of various realworld antivirus countermeasures on the virus propagation:

$\rho _ { S \mathrm { R } }$ describes the impact of implementing real-time immunization;

• ρ describes the impact of cleaning the virus only for the information nodes in the latent period;

• ρ<sub>IS</sub> describes the impact of cleaning the virus only for the information nodes in the infective status;

• ρ<sub>ER</sub> describes the impact of cleaning the virus and immunizing the information nodes in the latent period.

• γ describes the impact of recovering the infective information nodes.

Indeed, we can show in the following sections that ρ<sub>SR</sub>, ρ<sub>ES</sub>, ρ<sub>IS</sub> and ρ play important roles in demonstrating the effectiveness of some speci<sup>fi</sup>c antivirus strategies. In general, higher values of these transition rates indicate better abilities in dealing with viruses.

## 3.2. The infection function

Here we consider the parameters in the E-SEIR model. In Fig. 1, α, γ, ρ , ρ , ρ , ρ and ν(t) are the state transition rates, N is the volume of information nodes in the network, and μ is the replacement rate for the disfunctioned nodes. Note that all these parameters are assumed to be constants except for ν(t), i.e., the infection function which is the key factor characterizing the virus propagation ability in the network.

To characterize the infection function, let us consider a real-world medium-sized network — the information sharing network within an enterprise, a university or a government agency. This network has a distinct property as follows.

P2G propagation: In this network, the information sharing pattern is “point to group”; that is, each node likes to share information with the nodes in the same group. This is noteworthy, since nowadays there exist many small groups in an organization which may be formed around a project, within a functional department, or even by private social relationships. Members within a group communicate with each other frequently, but members in different groups seldom contact each other. So we can expect that the virus propagation is more smooth within a group than across different groups. This is what we call the “P2G propagation” pattern of viruses.

For simplicity, we call such a network the P2G network, as shown in Fig. 2. In essence, the P2G network is not the physical computer network but the information transition network, e.g., the email communication network. Therefore, physically connected two nodes, e.g., A and B in Fig. 2, indeed have no chance to infect each other directly but through the inter-nodes of different groups, such as C, D, E and F in Fig. 2. In general, the P2G network widely exists within realworld organizations, and the P2G propagation notion can facilitate the analysis of virus propagation from a managerial perspective. Accordingly we restrict our study on the P2G network and P2G propagation. Next, we derive the infection function based on the P2G propagation notion.

![](/api/attachments/XGPV2B6K/fulltext/images/0e4c47f80d58c27ccf6fb75bd4678e9ba62a39b6d7842337a88ebadde101bed3.jpg)  
Fig. 1. The states and state transitions in E-SEIR.

![](/api/attachments/XGPV2B6K/fulltext/images/706807387192d41eb8d7590e3c71b042c898c3159545a2bc24d0a6d4611c2f24.jpg)  
Fig. 2. An example of P2G networks.

Given that: 1) the information sharing group is homogeneous, i.e., an infected individual is equally likely to infect its neighbors in the same group, 2) the network is symmetric, which means that there is no privileged direction of transmission of the virus among different groups, and 3) the distribution of S-state nodes in the network is homogeneous, the increased number of E-state nodes transited from state S in a very short period Δt can be estimated as

$$
\Delta \mathrm{SE} = \widetilde {I} r \rho \Delta t,\tag{1}
$$

where I<sup>\~</sup> is the increased number of I-state nodes per unit time which can make effective infections (the concept of effective infections will be discussed below), r is the averaged number of group members around each node, and ρ is the averaged ratio of the S-state nodes among all nodes. Note that the value of r is computed averagely over all the groups in the network and is used as a prior knowledge in our study.

Then we can re<sup>fi</sup>ne Eq. (1) by further exploring the properties of the P2G network. Actually, one phenomenon should be further addressed in the P2G network; that is, there exist ineffective infections from nodes in state I. As can be seen from Fig. 3(a) and (b), there are two centric nodes which are both in state I; however, their infection results are entirely different. In Fig. 3(a), since all other nodes are in S-state, the centric node in I-state can make effective infections, as shown by the directed solid lines. But for the centric node in Fig. 3(b), it actually cannot infect any other node, since its group members are all in state E, I or R. This is what we called the “ineffective infections”. In most cases, the infectious node is surrounded by the nodes with a small portion of S-state ones, as shown in Fig. 3(c). In this way, the “I<sup>\~</sup>” in Eq. (1) is the number of nodes in I-state that can make effective infections. To re<sup>fi</sup>ne “I ”, note that the centric node in Fig. 3(c) must be a new I-state node; that is, at time t, it just completed the state transition from E to I, so its group members have not been infected heavily. So we can replace “I<sup>\~</sup>” in Eq. (1) by “αE”, where α is the transition rate from state E to I, and E is the number of nodes in E-state.

![](/api/attachments/XGPV2B6K/fulltext/images/804f00c811df395b22c0d92b0c4b9db7baad33921ee01a9ed00226588cc3edbe.jpg)  
(a) The Extreme Case of Effective Infections

![](/api/attachments/XGPV2B6K/fulltext/images/eed2e6721dc45d4b5df3a14abe25b1c718ebd3174d4e9ceb5f704e10a8997361.jpg)  
(b) The Extreme Case of Ineffective Infections

![](/api/attachments/XGPV2B6K/fulltext/images/85eb841ece91f572453f0825cc6c7e8745a2ad47f631f764e792edc4d6b62153.jpg)  
Fig. 3. Effective vs. ineffective infections within the P2G network

Moreover, it is noteworthy that NOT all the group members are online when the centric node is in state I. We use θ to denote the averaged online ratio of the nodes in the network. That means the $" r "$ in Eq. (1) should be replaced by $" r \theta " .$ Finally, the $" \rho '$ can be approximated by $^ { * } S / N ^ { * }$ , where S is the number of nodes in S-state, and N is the number of total nodes. Therefore, we have

$$
\Delta S E = \frac {\alpha E (t) r \theta S (t)}{N} \Delta t.\tag{2}
$$

On the other hand, in terms of time span Δt, the number of nodes in transition from S to E can also be formulated as $\Delta S E = \nu ( t ) S ( t ) \Delta t ,$ where $\nu ( t )$ is the transition rate from state S to E, i.e., the infection function. With a trivial transformation, we have

$$
\nu (t) = \frac {\Delta S E}{S (t) \Delta t} = \frac {\alpha r \theta}{N} E (t).\tag{3}
$$

Compared with the traditional infection functions [1,15] such as the bi-linear contact term, our new function can take into consideration the E-state and the ineffective infections, which is meant to more suitably re<sup>fl</sup>ect the real-world P2G network environment.

## 3.3. The anti-virus level for E-state nodes

Suppose that the average duration for a node staying in state E is t . Then the state transition rate of E-state nodes is $1 / t _ { E } .$ In the E-SEIR model we have

$$
\frac {1}{t _ {E}} = \alpha + \rho_ {\mathrm{ES}} + \rho_ {\mathrm{ER}} + \mu .\tag{4}
$$

Further, from an antivirus viewpoint, the transition paths from state E to other states can be divided into two categories, one is the group of “bad” paths heading to state I, and the other is the group of “not bad” paths heading to other states. Then the numbers of “bad” and “not bad” transitions can show a negative relationship, as indicated by Fig. 4.

Let

$$
\frac {1}{t _ {E}} = m _ {E} \alpha ,\tag{5}
$$

by Eqs. (4) and (5), we have

$$
m _ {E} = 1 + \frac {\rho_ {\mathrm{ES}} + \rho_ {\mathrm{ER}} + \mu}{\alpha}.\tag{6}
$$

Apparently, $m _ { E } \in [ 1 , \infty )$ . As $m _ { E }$ goes up, α will go down, given that 1/t is stable in a certain network environment. That is to say, to reduce $\alpha _ { \ast }$ we must try to increase $m _ { E } ,$ i.e., $\rho _ { \tt E S } + \rho _ { \tt E R }$ in $\operatorname { E q . }$ (6). So $m _ { E }$ indeed characterizes our antivirus level for E-state nodes. We will refer to m frequently in the following discussions.

## 3.4. The E-SEIR model

Here we represent the E-SEIR model in a more formal manner. Based on the compartment model presented in Fig. (1), E-SEIR can be formulated by a set of partial differential equations as follows:

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} S (t)}{\mathrm{d} t} = \mu N - v (t) S (t) - \rho_ {\mathrm{SR}} S (t) + \rho_ {\mathrm{ES}} E (t) + \rho_ {\mathrm{IS}} I (t) - \mu S (t) \\ \frac {\mathrm{d} E (t)}{\mathrm{d} t} = v (t) S (t) - m _ {E} \alpha E (t) \\ \frac {\mathrm{d} I (t)}{\mathrm{d} t} = \alpha E (t) - (\gamma + \rho_ {\mathrm{IS}}) I (t) - \mu I (t) \\ \frac {\mathrm{d} R (t)}{\mathrm{d} t} = \rho_ {\mathrm{SR}} S (t) + \gamma I (t) + \rho_ {\mathrm{ER}} E (t) - \mu R (t) \end{array} \right.\tag{7}
$$

where α, γ, ρ , ρ , ρ , ρ and $\nu ( t )$ are the state transition rates, μ is the replacement rate of nodes, and N is the total number of nodes in the network which satis<sup>fi</sup>es

$$
S (t) + E (t) + I (t) + R (t) = N.\tag{8}
$$

## 4. Virus propagation analysis: long-term behaviors

In this section, we will study the long-term behaviors of virus propagation in P2G information sharing networks using the E-SEIR model.

![](/api/attachments/XGPV2B6K/fulltext/images/4a1731ec3635fadae5cd3522c533a597f69688b4c09d0e6de7b0e127d6f53e91.jpg)  
Fig. 4. The relationship of the “bad” and “not bad” transitions.

## 4.1. The long-term equilibriums

Given Formulation $( 7 ) ,$ , we compute the <sup>fi</sup>xed points of the system. Let $\mathrm { d } E ( t ) / \mathrm { d } t = 0$ , and substitute $\ " \boldsymbol { \nu } ( t ) \ "$ by $^ { * } \alpha r \theta E ( t ) / N ^ { * }$ , we have

$$
E ^ {*} = 0 \quad \text { or } \quad E ^ {*} > 0 \text { and } S ^ {*} = \frac {m _ {E} N}{r \theta}
$$

For the case of $\boldsymbol { E } ^ { * } = \boldsymbol { 0 } ,$ , let $\mathsf { d } S ( t ) / \mathsf { d } t { = } 0 , \mathsf { d } I ( t ) / \mathsf { d } t { = } 0 ,$ and $\boldsymbol { S } ^ { * } + \boldsymbol { E } ^ { * } +$ $\boldsymbol { I } ^ { * } + \boldsymbol { R } ^ { * } = \boldsymbol { N } ,$ , we have the following virus-free equilibrium

$$
\mathrm{EQ} _ {\mathrm{vf}} = \left(S _ {1} ^ {*}, E _ {1} ^ {*}, I _ {1} ^ {*}, R _ {1} ^ {*}\right) = \left(\frac {\mu}{\rho_ {\mathrm{SR}} + \mu} N, 0, 0, \frac {\rho_ {\mathrm{SR}}}{\rho_ {\mathrm{SR}} + \mu} N\right).\tag{9}
$$

For the case of $\begin{array} { r } { { \cal E } ^ { * } > 0 , { \cal S } ^ { * } = \frac { m _ { E } N } { r \theta } , } \end{array}$ , we can similarly get the virusepidemic equilibrium as follows:

$$
\begin{array}{l} \mathrm{EQ} _ {\mathrm{ve}} = \left(S _ {2} ^ {*}, E _ {2} ^ {*}, I _ {2} ^ {*}, R _ {2} ^ {*}\right) \\ = \left(\frac {m _ {E}}{r \theta} N, \frac {\mu - \frac {m _ {E} (\rho_ {\mathrm{SE}} + \mu)}{r \theta}}{m _ {E} \alpha - \rho_ {\mathrm{ES}} - \frac {\rho_ {\mathrm{IS}} \alpha}{\gamma + \rho_ {\mathrm{IS}} + \mu}} N, \frac {\alpha}{\gamma + \rho_ {\mathrm{IS}} + \mu} E _ {2} ^ {*}, N - S _ {2} ^ {*} - E _ {2} ^ {*} - I _ {2} ^ {*}\right). \end{array}\tag{10}
$$

Notably, the <sup>fi</sup>x point $\mathrm { E Q } _ { \mathrm { v e } }$ is meaningful only if $E _ { 2 } ^ { * } { > } 0$ . It is easy to show the denominator of $\begin{array} { r } { ^ { \cdot } E _ { 2 } ^ { * } , \mathrm { i . e . , } m _ { E } \alpha - \rho _ { \mathrm { E S } } - \frac { \rho _ { \mathrm { l S } } \alpha } { \gamma + \rho _ { \mathrm { l S } } + \mu } } \end{array}$ is greater than $m _ { E } \alpha - \rho _ { \mathrm { E S } } - \alpha .$ . Then, according to Eqs. (4) and $( 5 )$ , this denominator is greater than 0. So, we only need to show the numerator

$$
\mu - \frac {m _ {E} (\rho_ {\mathrm{SR}} + \mu)}{r \theta} > 0 \iff \frac {r \theta \mu}{m _ {E} (\rho_ {\mathrm{SR}} + \mu)} > 1.\tag{11}
$$

This implies that if we decrease the antivirus level for the E-state nodes $( m _ { E } \downarrow )$ , take less efforts on immunizing the S-state nodes $( \rho _ { S R } \downarrow )$ or increase the average on-line group members $( r \theta \uparrow )$ , then the system tends to reach the virus-epidemic equilibrium in the long run.

In what follows, we present two lemmas for the virus-free equilibrium $\mathtt { E Q } _ { \mathrm { v e } }$ and virus-epidemic equilibrium $\mathrm { E Q } _ { \mathrm { v e } } ,$ respectively.

## Lemma 1. If

$$
\frac {r \theta \mu}{m _ {E} (\rho_ {\mathrm{SR}} + \mu)} <   1,
$$

then the virus-free equilibrium $E Q _ { v f }$ is asymptotically stable.

## Lemma 2. If

$$
\frac {r \theta \mu}{m _ {E} (\rho_ {\mathrm{SR}} + \mu)} > 1,
$$

then the virus-epidemic equilibrium $E Q _ { v e }$ is asymptotically stable.

For clarity, the proofs of Lemma 1 and 2 are given in Appendix A.

## 4.2. The control parameter $C _ { L }$

Here we explore how to control the long-term equilibriums in our system. With

$$
C _ {L} = \frac {r \theta \mu}{m _ {E} (\rho_ {\mathrm{SR}} + \mu)},\tag{12}
$$

and let $D = \{ ( S , E , I , R ) | S + E + I + R = N ; S , E , I , R \in R _ { + } ^ { 4 } \}$ be the domain of the system state parameters. Then we have the following theorems.

Theorem 1. $I f C _ { L } < 1 ,$ the virus-free equilibrium $E Q _ { v f }$ is asymptotically stable in D. Whereas $i f C _ { L } { > } 1 , E Q _ { v f }$ is unstable.

Proof. Given $C _ { \mathrm { L } } { < } 1$ , by Lemma $1 , ~ \mathrm { E Q } _ { \mathrm { v f } }$ is asymptotically stable. However, when $C _ { \mathrm { L } } { > } 1 ,$ , one of the eigenvalues of the system at $\mathrm { E Q } _ { \mathrm { v f } }$ $\mathrm { i } . \mathrm { e } . , \lambda _ { 2 } \mathrm { > } 0 ,$ , which implies that the system is unstable.

Theorem 2. $I f C _ { L } \leq 1 ,$ the virus-epidemic equilibrium $E Q _ { v e }$ does not exist in D. Whereas $i f C _ { L } { > } 1 , E Q _ { v e }$ is asymptotically stable.

Proof. By Lemma 2, this theorem holds.

□

Corollary 1. For $S _ { 1 } ^ { * }$ and $S _ { 2 } ^ { * }$ in $E Q _ { v f }$ and $E Q _ { v e }$ respectively, $i f S _ { 1 } ^ { * } { < } S _ { 2 } ^ { * } ,$ there exists only virus-free equilibrium $E Q _ { v f }$ which is asymptotically stable; whereas $\dot { \boldsymbol { i } } f { \boldsymbol { S } _ { 1 } ^ { * } } { > } { \boldsymbol { S } _ { 2 } ^ { * } }$ , only the virus-epidemic equilibrium $E Q _ { v e }$ is asymptotically stable.

Proof. It is easy to show that $S _ { 1 } ^ { * } { < } S _ { 2 } ^ { * } \Leftrightarrow C _ { \mathrm { L } } { < } 1 ,$ , and $S _ { 1 } ^ { * } { > } S _ { 2 } ^ { * }  C _ { \mathrm { L } } { > } 1 .$ . So we complete the proof by the above theorems. □

Thus, $C _ { \mathrm { { L } } }$ is the key parameter that controls the long-term behaviors of the virus propagation in the system. Actually, a well-known concept in the epidemiology literature [1] — basal reproduction rate, denoted by ${ \hat { R } } _ { 0 } ,$ shows a very similar property to $C _ { \mathrm { { L } } } .$ People can also view $C _ { \mathrm { L } }$ as the basal reproduction rate for the E-SEIR model.

In summary, our system described by equations in Formulation (7) has two long-term equilibriums, i.e., the virus-free equilibrium $\mathtt { E Q } _ { \mathrm { v f } }$ and the virus-epidemic equilibrium $\mathrm { E Q } _ { \mathrm { v e } } .$ When $C _ { \mathrm { L } } { \le } 1$ , there exists only one equilibrium, i.e., the virus-free equilibrium $\operatorname { E Q } _ { \operatorname { V f s } }$ Further, if $C _ { \mathrm { L } } { < } 1$ , then $\mathrm { E Q } _ { \mathrm { v f } }$ is an asymptotically stable point. On the other hand, when $C _ { \mathrm { { L } } } { > } 1$ , both of the two equilibriums can appear. However, only the virus-epidemic equilibrium $\mathrm { E Q } _ { \mathrm { v e } }$ can be asymptotically stable.

## 5. Virus propagation analysis: short-term behaviors

In the previous section, we studied the long-term behaviors of the virus propagation. Its short-term behaviors, however, have not been well discussed yet. To this end, in this section, we try to understand the rapid and extensive outbreaks of virus propagation in short periods. This is noteworthy, since even if the virus propagation can be stabilized at a very low level after a long time, we may still suffer from a vast loss during the converging process because of some wave of emergent virus infection outbreaks [32]. Indeed, regarding the antivirus practice, in many cases the control of short-term behaviors is often deemed to be more important than the control of long-term behaviors.

Since an effective antivirus activity is usually to prevent the information nodes from getting into the I-state, we aim at the control on the volume of the E-state nodes. We call the rapid increase of the number of E-state nodes the “virus infection outbreak”. Therefore, in an information-sharing network, to slow down or even stop a (potential) virus infection outbreak, we should guarantee that the number of E-state nodes is non-increasing, i.e., $\mathrm { d } E / \mathrm { d } t \leq 0 .$ . Let $\mathrm { d } E / \mathrm { d } t \leq 0 ,$ by the second equation in (7) and the computations of $\nu ( t )$ and 1/t<sub>E</sub> in Eqs. (3) and (5) respectively, we have

$$
\frac {\mathrm{d} E}{\mathrm{d} t} \leq 0 \iff f _ {m _ {E}} (S (t)) = \frac {r \theta}{m _ {E}} \left(\frac {S (t)}{N}\right) \leq 1,\tag{13}
$$

where $r \theta$ is the average online group members for an information node in network, $m _ { E }$ is the antivirus level for E-state nodes with m<sup>0</sup> being the basic level, N is the volume of nodes in the network, and S(t) is the number of S-state nodes at time t. Since rθ is decided by the habits of network users. We can reasonably assume that it is constant. Therefore, to control virus infection outbreaks, the key factors are the antivirus level $m _ { E }$ and the dynamic number of S-state nodes S(t). It is easy to know, $f _ { m _ { F } } ( S _ { 1 } ^ { * } ) = C _ { \mathrm { I } }$ , and $f _ { m _ { F } } ( S _ { 2 } ^ { * } ) = 1$ , where $S _ { 1 } ^ { * }$ and $S _ { 2 } ^ { * }$ are the numbers of S-state nodes in virus-free and virus-epidemic equilibriums, respectively.

## 5.1. The critical point $S _ { c r }$

When $C _ { \mathrm { L } } { < } 1 ,$ , there is a critical point $S _ { \mathrm { c r } }$ for $S ( t )$ at time $t = 0$ such that: for $S ( 0 ) { \leq } S _ { \mathrm { c r } }$ no virus infection outbreak will take place even if we do not improve our antivirus level m<sup>0</sup>; but for ${ \mathsf { S } } ( 0 ) . S _ { \mathrm { c r } } ,$ one outbreak will be launched. As to the case of $C _ { \mathrm { L } } { > } 1$ , the critical point does not exist any more, and we will face multiple virus infection outbreaks.

Case 1. $C _ { \mathrm { { L } } } { < } 1 .$

According to Corollary $1 , C _ { \mathrm { L } } { < } 1$ implies $S _ { 1 } ^ { * } { < } S _ { 2 } ^ { * }$ , where $S _ { 1 } ^ { * }$ and $S _ { 2 } ^ { * }$ are the numbers of S-state nodes in virus-free and virus-epidemic equilibriums, respectively.<sup>1</sup>

$$
\bullet \text {   If   } S (0) \leq S _ {2} ^ {*},
$$

$$
\forall t, S (t) \leq \max _ {t} S (t) \stackrel {(a)} {\leq} S _ {2} ^ {*}.
$$

The reason for (a) is due to the observation that $S ( t )$ converges quickly to $S _ { 1 } ^ { * }$ of the virus-free equilibrium in the case of $S _ { 1 } ^ { * } { < } \bar { S } _ { 2 } ^ { * }$ Extensive simulation results are presented in the experimental part to further verify this observation. Therefore,

$$
\max _ {t} f _ {m _ {E} ^ {0}} (S (t)) \leq f _ {m _ {E} ^ {0}} \left(S _ {2} ^ {*}\right) = 1,
$$

which implies that $\forall t , \mathrm { d } E / \mathrm { d } t \leq 0 .$ So no virus infection outbreak will be launched under the basic antivirus level m<sub>E</sub><sup>0</sup>.

$$
\bullet \text {   If   } S (0) > S _ {2} ^ {*},
$$

$$
\max _ {t} f _ {m _ {E} ^ {0}} (S (t)) \geq f _ {m _ {E} ^ {0}} (S (0)) > f _ {m _ {E} ^ {0}} \left(S _ {2} ^ {*}\right) = 1,
$$

which implies that $\exists t = 0$ such that $\frac { \mathrm { d } E ( t ) } { \mathrm { d } t } \big | _ { t = 0 } > 0$ . In other words, there is at least one outbreak at the beginning of the virus infection. Indeed, as will be shown in the experiments, there is one and only one outbreak in this case. So if we want to control this outbreak, we need to raise our antivirus level m<sup>0</sup> in a short period.

From the above cases, we can draw the conclusion that the $\mathsf { \Omega } ^ { \ast } \mathrm { \nabla \psi i r t u a l { \vec { \epsilon } } \ } S _ { 2 } ^ { \ast }$ is the critical point for the virus infection outbreak given $C _ { \mathrm { L } } { < } 1 , \mathrm { i . e . , } S _ { \mathrm { c r } } { = } S _ { 2 } ^ { * }$

Case 2. $C _ { \mathrm { { L } } } { > } 1 .$

C N1 means that $S _ { 2 } ^ { * } { < } S _ { 1 } ^ { * }$ , where $S _ { 1 } ^ { * }$ is the “virtual” point here. Similar to the above case, we have

$$
\bullet \text {   If   } S (0) \leq S _ {2} ^ {*},
$$

$$
\max _ {t} S (t) ^ {(b)} > S _ {2} ^ {*}.
$$

The reason for (b) is due to the facts that: $( 1 ) S ( t )$ will converge to $S _ { 2 } ^ { * }$ , and $( 2 ) S ( t )$ tends to vibrate around $S _ { 2 } ^ { * }$ in our observations. So $\exists t , S ( t ) > S _ { 2 } ^ { * }$ . Therefore,

max $f _ { m _ { E } ^ { 0 } } ( S ( t ) ) ~ > ~ f _ { m _ { E } ^ { 0 } } \left( S _ { 2 } ^ { * } \right) = 1 .$ t

So ∃t, dE/dtN0, which means that at least one virus infection outbreak will be launched.

$\mathrm { I f } S ( 0 ) > S _ { 2 } ^ { * }$ , this case is similar to that of $S ( 0 ) { > } S _ { 2 } ^ { * }$ when $C _ { \mathrm { L } } { < } 1$ . That is, at least one outbreak will be launched at the beginning of the virus infection.

So when $C _ { \mathrm { L } } { > } 1 , S _ { 2 } ^ { * }$ is no longer the critical point for virus infection outbreaks. In other words. virus infection outbreaks are inevitable if $C _ { \mathrm { L } } { > } 1$ . Indeed, as can be seen in the experimental section, when $C _ { \mathrm { L } } { > } 1 ,$ more than one virus infection outbreak will be launched no matter what S(0) is.

## 5.2. The control parameter $C _ { S }$

Now the question is: How to control virus infection outbreaks in a short period? Since $S ( t )$ is dynamic during the infection process, one solution is to set the antivirus level m dynamically so that

$$
f _ {m (t)} (S (t)) \leq 1 \Longleftrightarrow m (t) \geq \frac {r \theta}{N} S (t).
$$

By Inequality (13), we know $\mathrm { d } E / \mathrm { d } t \leq 0$ for all t given the above m(t), which means that the virus infection outbreak can be completely avoided. However, this dynamic control is not applicable in the real-world cases, since to know the exact $S ( t )$ at any time t is dif<sup>fi</sup>cult. In the following discussion, we illustrate how to set a proper antivirus level to control the virus infection outbreak in a short period.

From the previous subsection we know that, when $C _ { \mathrm { L } } { > } 1$ or $C _ { \mathrm { L } } { < } 1$ but $S ( 0 ) { > } S _ { 2 } ^ { * }$ , under the basic antivirus level m<sup>0</sup>, there will be at least one virus infection outbreak in a short period. So we need to increase our antivirus level $m _ { E }$ from m<sup>0</sup> to a higher level, or improve the ability of real-time immunization $\rho _ { S \mathbb { R } } ,$ or both. More concretely,

Case 1. $S ( 0 ) { \leq } S _ { 1 } ^ { * }$

If $C _ { \mathrm { { L } } } { < } 1 ,$ , according to Corollary 1, we have $S ( 0 ) { \leq } S _ { 1 } ^ { * } { < } S _ { 2 } ^ { * }$ . Then by case 1 in Section 5.1, no virus infection outbreak will be launched even if we do not carry out any more antivirus effort.

For the case of $C _ { \mathrm { { L } } } { > } 1 ,$ , however, we must raise our antivirus level to avoid multiple infection outbreaks. More precisely, we must raise $m _ { E }$ or $\rho _ { S \mathrm { R } }$ to guarantee $S _ { 1 } ^ { * } { < } S _ { 2 } ^ { * }$ , or equivalently,

$$
\frac {r \theta}{m _ {E} N} \left(\frac {\mu N}{\mu + \rho_ {\mathrm{SR}}}\right) <   1.\tag{14}
$$

By doing so, we have $S ( 0 ) { \leq } S _ { 1 } ^ { * } { < } S _ { 2 } ^ { * }$ again, and the multiple outbreaks can be fully avoided.

Case $2 . \ S ( 0 ) { > } S _ { 1 } ^ { * } .$

No matter what the $C _ { \mathrm { L } }$ value ${ \mathrm { i } } s ,$ if we raise m to guarantee $S _ { 2 } ^ { * } { > } S ( 0 )$ or equivalently

$$
\frac {r \theta}{m _ {E} N} (S (0)) <   1,\tag{15}
$$

we have $S _ { 1 } ^ { * } { < } S ( 0 ) { < } S _ { 2 } ^ { * }$ . Then by case 1 in Section 5.1 again, we can also avoid any infection outbreak.

Here, we put the above two cases together. To unify Inequalitie (14) and (15), we let

$$
C _ {S} = \frac {r \theta}{m _ {E} N} \max \left(\frac {\mu N}{\mu + \rho_ {S R}}, S (0)\right).\tag{16}
$$

Then if $C _ { S } { < } 1$ , no virus infection outbreak can be launched, whereas if $C _ { S } { > } 1$ , at least one virus infection outbreak will take place. Thus $C _ { S }$ is the control parameter for the virus infection outbreak. To change the value of $C _ { S } ,$ , we can adjust the antivirus level for E-state nodes, i.e., $m _ { E } ,$ or the real-time immunization ability, i.e., ρ .

## 6. The $\mathbf { c _ { s } } .$ control strategy

In this section, we introduce an antivirus strategy based on the E-SEIR model. First, the control objective is the following:

The network system can be stabilized at the virus-free equilibrium after a long period without any virus infection outbreak during the converging process.

There are long-term and short-term interests in the above objective, therefore it might not be enough to simply keep $C _ { \mathrm { L } } { > } 1$

## 6.1. Antivirus countermeasures in E-SEIR

People have developed various antivirus countermeasures, such as early monitoring and alarming, pre-immunization, virus scanning and cleaning, real-time immunization (including patching, <sup>fi</sup>re-wall installation, etc), quarantine/replacement, and recovery. The combinations of these countermeasures constitute the bases of different antivirus strategies.

In this paper, we focus on the antivirus countermeasures for $S -$ state and E-state nodes, $\mathrm { e . g . }$ , the pre-immunizations and real-time immunizations for S-state nodes, the virus scanning and cleaning for E-state nodes, and the real-time immunizations subsequently. The reason for such consideration is that in many cases people usually seek to control the virus before the nodes getting into the I state. To this end, we set in our E-SEIR model

1. the state transition path from S to R, which represents the real-time immunization effect on S-state nodes, and the level is denoted by $\rho _ { S \mathrm { R } } ;$

2. the state transition path from E to S, which represents the virus scanning and cleaning effect on E-state nodes, and the level is denoted by $\rho _ { \mathrm { E S } } ;$

3. the state transition path from E to R, which represents the combination effect of virus cleaning and real-time immunization on E-state nodes, and the level is denoted by $\rho _ { \tt E R }$

Moreover, the number of the initial S-state nodes, i.e., $S ( 0 ) ,$ , can reveal the pre-immunization level for the network, given the numbers of E-state and I-state nodes are fairly low at the beginning. That ${ \mathrm { i } } s ,$ a higher S(0) means a lower $R ( 0 )$ , which implies a lower pre-immunization level, and vice versa.

Therefore, we can better set the target level of $m _ { E } , \rho _ { S \mathrm { R } } ,$ and S(0) to control the long-term and short-term virus propagation in our E-SEIR model. And the settings indeed indicate the antivirus strategies.

## 6.2. The $C _ { S }$ -control

We <sup>fi</sup>rst provide two notions as follows.

De<sup>fi</sup>nition 1. C<sub>L</sub>-control The C<sub>L</sub>-control on the virus propagation is to keep $C _ { \mathrm { L } } { < } 1 .$

De<sup>fi</sup>nition 2. $C _ { S } .$ -control The $C _ { S ^ { - } }$ -control on the virus propagation is to keep $C _ { S } { < } 1$

Indeed, to achieve the long-term objective, we can take $C _ { \mathrm { { L } } }$ -control. Alternatively, to achieve the short-term objective, we must take $C _ { { \sf S } ^ { - } } \mathrm { c o n t r } 0 \mathrm { l } .$ . Since

$$
C _ {L} = \frac {r \theta}{m _ {E} N} \left(\frac {\mu N}{\mu + \rho_ {S R}}\right) \leq \frac {r \theta}{m _ {E} N} \max \left(\frac {\mu N}{\mu + \rho_ {S R}}, S (0)\right) = C _ {S},
$$

we know $C _ { S } { < } 1$ implies $C _ { \mathrm { L } } { < } 1$ . In other words, to ful<sup>fi</sup>ll the longterm and short-term objectives simultaneously, we can employ the $C _ { S }$ -control. We exploit this strategy by considering two cases.

Case 1. The pre-immunization level for S-state nodes is low.

In this case, we have a large $S ( 0 )$ with $S ( 0 ) { > } S _ { 1 } ^ { * } { = } { \mu } N / ( { \mu } { + } \rho _ { \mathrm { S R } } )$ . In order to control the virus infection outbreak in short periods, we must use $C _ { { \sf S } ^ { - } } \mathrm { c o n t r } 0 \mathrm { l } .$ Let $C _ { S } { < } 1$ , which implies that

$$
m _ {E} > \frac {r \theta S (0)}{N}.
$$

This indicates that, in the case, the way to avoid the virus infection outbreak is to increase the antivirus level for E-state nodes beyond a certain level.

Case 2. The pre-immunization level for S-state nodes is high.

In this case, $S ( 0 ) { < } S _ { 1 } ^ { * }$ . So we have

$$
C _ {S} = C _ {L}.
$$

This indicates that the long-term and short-term controls have been nicely integrated together. In other words, the $C _ { S ^ { - } }$ -control reduces to the $C _ { \mathrm { { L } } }$ -control. Therefore, we only need to make sure that

$$
m _ {E} > \frac {r \theta \mu}{\mu + \rho_ {\mathrm{SR}}}.
$$

Note that, if we cannot guarantee that $C _ { \mathrm { L } } { = } C _ { S } { < } 1 ,$ , we will have the worst result — more than one virus infection outbreak plus the virusepidemic equilibrium. As a result, a low S(0), i.e., a high pre-immunization level, does not necessarily prevent the network from virus outbreaks. This also agrees with the real-world situations. Both CSI/FBI and ICSA report [8,16] that although most organizations have installed antivirus software in their information systems, virus infections can still manage to prevail and survive in the networks, and caused server down time, loss of productivity and loss of data for these organizations.

In summary, C -control can help to achieve our antivirus objective. However, the cost of this control is relatively high, especially for a high S(0) value when the pre-immunization level is low. To this end, we propose a multi-stage $C _ { S }$ -control strategy which can lower the required $m _ { E }$ level stage by stage and <sup>fi</sup>nally reduce $C _ { S }$ -control to $C _ { \mathrm { { L } } }$ -control. Further details are illustrated in Section 7.4.

## 6.3. Some managerial insights

For real-world applications, we have some interesting observations from the managerial perspective.

• First, the control of the short-term virus infection outbreak is more dif<sup>fi</sup>cult than the control of the long-term virus propagation equilibrium. This is straightforward since $C _ { S }$ -control is more strict than $C _ { \mathrm { L } ^ { - } } \mathrm { c o n t r o l }$

• Second, a high pre-immunization level does not prevent the system from the virus outbreaks. We should further guarantee the $C _ { \mathrm { L } ^ { - } } \mathrm { c o n t r } 0 \mathsf { l } .$ . Nevertheless, a high pre-immunization level can stillmitigate the required antivirus efforts. This is noteworthy, since the real-world antivirus activities always have resource constraints.

• Finally, the real-time immunization on S-state nodes is of no use to the control of the virus infection outbreaks given a low preimmunization level. An effective way to control the outbreaks is to improve our antivirus level on E-state nodes, i.e., $m _ { E } .$

## 7. Numeric results

## 7.1. The experimental setup

We <sup>fi</sup>rst describe the parameters used in our experiments. As shown in Table 1, we have three types of parameters: the system parameters, the state transition parameters, and the initial parameters.

Generally, the values of the system parameters are <sup>fi</sup>xed in all the experiments unless we explicitly specify the changes. Also, these parameters are carefully selected so as to better simulate the realworld situations. For instance, we assume that the replacement cycle for each information node is approximately $1 / 2 \ y e a r = 4 3 8 0 \ { \mathrm { h } } ,$ , so we set $\mu { = } 1 / 4 3 8 0$ correspondingly. This is reasonable, since in information systems the “replacement” includes not only the real replacements of old nodes (machines) but also the virtual replacements — the node lost its immunity due to the system reinstallation or the software problem is regarded as the replacement of its own.

There are ten state-transition related parameters. Among these parameters, $t _ { E }$ and $t _ { I }$ are the two important ones which are strongly related to the information network, the network users and the speci<sup>fi</sup>c virus. In our experiments, we <sup>fi</sup>xed $t _ { I } = 1 2$ and set the values of $t _ { E } ,$ m and $\rho _ { S \mathrm { R } }$ orderly, then the rest parameters can be computed by the relationships shown in Table 1. Note that $\nu ( t )$ is computed dynamically according to the value of E(t).

Table 2  
Table 1  
Parameters used in experiments.

<table><tr><td>Type</td><td>Parameter</td><td>Value</td><td>Note</td></tr><tr><td>The system</td><td> $N$ </td><td>100,000</td><td>Total number of information nodes.</td></tr><tr><td rowspan="3">Parameters</td><td> $\mu$ </td><td>1/4380</td><td>Replacement rate of nodes.</td></tr><tr><td> $r$ </td><td>30</td><td>Average number of group members.</td></tr><tr><td> $\theta$ </td><td>1.0</td><td>Average on-line ratio of the nodes.</td></tr><tr><td>The state</td><td> $t_{E}$ </td><td>Not fixed</td><td>Average duration for exposed nodes.</td></tr><tr><td>Transition</td><td> $m_{E}$ </td><td>Not fixed</td><td>Antivirus effort on E-state.</td></tr><tr><td rowspan="8">Parameters</td><td> $\rho_{\text{SR}}$ </td><td>Not fixed</td><td>State transition rate from S to R.</td></tr><tr><td> $t_{I}$ </td><td>12</td><td>Average duration for infectious nodes.</td></tr><tr><td> $\alpha$ </td><td> $1/(t_{E}m_{E})$ </td><td>State transition rate from E to I.</td></tr><tr><td> $\rho_{\text{ES}}$ </td><td> $1/(300t_{E})$ </td><td>State transition rate from E to S.</td></tr><tr><td> $\rho_{\text{ER}}$ </td><td> $1/t_{E}-\alpha-\rho_{\text{ES}}-\mu$ </td><td>State transition rate from E to R.</td></tr><tr><td> $\rho_{\text{IS}}$ </td><td> $1/(400t_{I})$ </td><td>State transition rate from I to S.</td></tr><tr><td> $\gamma$ </td><td> $1/t_{I}-\rho_{\text{IS}}-\mu$ </td><td>State transition rate from I to R.</td></tr><tr><td> $\nu(t)$ </td><td> $\alpha r\theta E(t)/N$ </td><td>State transition rate from S to E.</td></tr><tr><td>The initial</td><td> $S(0)$ </td><td>Not fixed</td><td>Initial number of nodes in state S.</td></tr><tr><td rowspan="3">Parameters</td><td> $E(0)$ </td><td>Not fixed</td><td>Initial number of nodes in state E.</td></tr><tr><td> $I(0)$ </td><td>0</td><td>Initial number of nodes in state I.</td></tr><tr><td> $R(0)$ </td><td> $N-S(0)-E(0)-I(0)$ </td><td>Initial number of nodes in state R.</td></tr><tr><td>Other</td><td> $S_{1}^{*}$ </td><td> $\mu N/(\mu+\rho_{\text{SR}})$ </td><td>Number of nodes in S-state at virus-free equilibrium.</td></tr><tr><td>Important</td><td> $S_{2}^{*}$ </td><td> $m_{E}N/(r\theta)$ </td><td>Number of nodes in S-state at virus-epidemic equilibrium.</td></tr><tr><td rowspan="2">Parameters</td><td> $C_{L}$ </td><td>See Eq. (12)</td><td>Parameter for long-term virus propagation control.</td></tr><tr><td> $C_{S}$ </td><td>See Eq. (16)</td><td>Parameter for short-term virus propagation control.</td></tr></table>

Moreover, the initial state of the system, i.e., (S(0), E(0), I(0), R(0)), can make great impact on the virus propagation. So we need to set the initial parameters carefully. Typically, we assume that E(t) is relatively low at the beginning of the virus propagation, i.e., E(0) is small. As to S(0) and R(0), they re<sup>fl</sup>ect the pre-immunization level of the network; that is, a high pre-immunization level indicates a high R(0) and a small S(0), and vice versa.

Finally, to facilitate the computations, we also list some important computational parameters in the table. These parameters can be easily calculated by the above three types of parameters. Indeed, Table 2 shows all the real parameter values we used in the experiments.

## 7.2. The long-term equilibriums

In this subsection, we verify the two long-term equilibriums of the E-SEIR model. As can be seen in Fig. 5(a), the numbers of nodes in four states tend to be stable after 200 units of time. Speci<sup>fi</sup>cally, the levels of the E-state and I-state nodes are both zeros at the equilibrium. This implies a virus-free equilibrium when $C _ { \mathrm { L } } { = } 0 . 7 7 .$ If we change the initial parameters and the state transition parameters simultaneously while keeping $C _ { \mathrm { L } } { < } 1 ,$ as indicated by Fig. 5(b), we can <sup>fi</sup>nd that the virus-free equilibrium still holds since $\bar { E } _ { 1 } ^ { * } { = } I _ { 1 } ^ { * } { = } 0$ , while $S _ { 1 } ^ { * }$ and $\boldsymbol { R } _ { 1 } ^ { * }$ might be different.

The settings of the parameters.

<table><tr><td></td><td> $t_{E}$ </td><td> $m_{E}$ </td><td> $ρ_{SR}$ </td><td>S(0)</td><td>E(0)</td></tr><tr><td>Fig. 5(a)</td><td>24</td><td>4.0</td><td>1/650</td><td>98,990</td><td>10</td></tr><tr><td>Fig. 5(b)</td><td>24</td><td>5.0</td><td>1/650</td><td>990</td><td>1000</td></tr><tr><td>Fig. 6(a)</td><td>24</td><td>4.0</td><td>1/2500</td><td>98,990</td><td>10</td></tr><tr><td>Fig. 6(b)</td><td>24</td><td>4.0</td><td>1/2500</td><td>990</td><td>1000</td></tr><tr><td>Fig. 7(a)</td><td>24</td><td>6.0</td><td>1/650</td><td>-</td><td>100</td></tr><tr><td>Fig. 7(b)</td><td>24</td><td>4.0</td><td>1/2500</td><td>-</td><td>100</td></tr><tr><td>Fig. 8</td><td>4</td><td>-</td><td>1/2500</td><td>-</td><td>10</td></tr><tr><td>Fig. 9(a)</td><td>4</td><td>2</td><td>1/650</td><td>10,000</td><td>1000</td></tr><tr><td>Fig. 9(b)</td><td>4</td><td>4</td><td>1/650</td><td>10,000</td><td>1000</td></tr><tr><td>Fig. 10(a)</td><td>4</td><td>2</td><td>1/650</td><td>70,000</td><td>1000</td></tr><tr><td>Fig. 10(b)</td><td>4</td><td>4</td><td>1/650</td><td>70,000</td><td>1000</td></tr><tr><td>Fig. 10(c)</td><td>4</td><td>22</td><td>1/650</td><td>70,000</td><td>1000</td></tr><tr><td>Fig. 10(d)</td><td>4</td><td>-</td><td>-</td><td>70,000</td><td>1000</td></tr></table>

Note: “–” means the parameter takes several values.

(a) CL=0.77.  
![](/api/attachments/XGPV2B6K/fulltext/images/dcfb47130c1485c060f1e991cd67cd6a478f7c4d9df88a58d4ddfc32e8450421.jpg)

(b) $C _ { L } { = } 0 . 9 6 .$  
![](/api/attachments/XGPV2B6K/fulltext/images/32ce316c9377365a31930d427e93dcc193a794c73be62c6f9f4e716915a1ee3c.jpg)  
Fig. 5. The virus-free equilibrium.

Fig. 6 shows the virus-epidemic equilibrium when $C _ { \mathrm { L } } { = } 2 . 7 1$ Although we change the initial parameters dramatically as shown in Fig. 6(a) and (b), we can observe that the equilibriums in the two <sup>fi</sup>gures are the same. This observation agrees with the theoretical results in Eqs. (9) and (10), which indicate that it is the state transition parameter rather than the initial parameter that determines the equilibriums.

Fig. 6 also shows that some viruses cannot be cleaned up in the network but keep propagating in a relatively small scale. This result agrees with our intuitions on real-world scenarios. And the reasons may be 1) a high replacement rate for information nodes (μ<sup>↑</sup>), 2) a frequent communication level for group members (rθ<sup>↑</sup>), and 3) a low antivirus level of webmasters and web users (m <sup>↓</sup>, ρ<sup>↓</sup> ). These factors can be uni<sup>fi</sup>ed by the single parameter $- \ C _ { \mathrm { L } }$ as indicated in Eq. (12).

## 7.3. The virus infection outbreaks

Here, we investigate the important factors for virus infection outbreaks. First, compared with Fig. 7(a) and (b), we can <sup>fi</sup>nd that the virus infection outbreak patterns are different for different $C _ { \mathrm { L } }$ values. For the case of $C _ { \mathrm { L } } { < } 1$ in Fig. 7(a), there is only one virus infection outbreak at most before the network goes into the virus-free equilibrium. For the case of $C _ { \mathrm { L } } { > } 1$ in Fig. 7(b), however, more than one virus infection outbreak are to be launched before the virusepidemic equilibrium. And the peaks in the latter <sup>fi</sup>gure are higher than the peaks in the former one. This implies that we will face much more serious virus infection outbreaks in the second scenario. Therefore, C might be the <sup>fi</sup>rst important factor for virus infection outbreaks; that is, if we can keep $C _ { \mathrm { L } } { < } 1$ , we may reduce multiple outbreaks to at most one outbreak, and the scale of the outbreak can be much smaller.

(a) $C _ { L } \mathrm { = } 2 . 7 1 , \mathrm { S } ( 0 ) \mathrm { = } 9 8 9 9 0 , \mathrm { E } ( 0 ) \mathrm { = } 1 0 0 0 , \mathrm { I } ( 0 ) \mathrm { = } 0 .$  
![](/api/attachments/XGPV2B6K/fulltext/images/79bc1e5ec95c34def94584d5d1e2b6b467409ba0f47124a55dc85381cca44553.jpg)

(b) CL=2.71, S(0)=990, E(0)=1000, I(0)=0  
![](/api/attachments/XGPV2B6K/fulltext/images/57883749fcb7e1155acc06d145cb4ce6c068f6de4e3283eeaab1945a04501e48.jpg)  
Fig. 6. The virus-epidemic equilibrium.

Nevertheless, $C _ { \mathrm { L } }$ is not the only factor for virus infection outbreaks. In fact, in our experiments, we found that the initial level of the $S \cdot$ -state node is also a key factor that can make impact on virus infection outbreaks. As can be seen in Fig. $^ { 7 ( \mathsf { a } ) , }$ , when $S ( 0 ) = 2 2 , 0 0 0 , 2 4 , 0 0 0$ or 26,000, exactly one outbreak is launched; but for $S ( 0 ) = 1 8 , 0 0 0$ or 8000, there is no outbreak at all. This implies that, if $C _ { \mathrm { L } } { < } 1$ , there is a critical point for S(0) which determines the existence of virus infection outbreaks. Indeed, we can have the empirical critical point $S _ { \mathrm { c r } } { = } 2 0 { , } 0 0 0$ , which is the value of $S _ { 2 } ^ { * }$ , given the parameters in Table 2. This result justi<sup>fi</sup>es our analysis in Section 5.1. However, for the case $C _ { \mathrm { L } } { > } 1$ in Fig. 7(b), the critical point disappeared. In other words, no matter what the S(0) value is, more than one virus infection outbreak will take place, although the peaks can be different for different S(0) values.

(a) CL=0.64.  
![](/api/attachments/XGPV2B6K/fulltext/images/4bca35ad3068a0d7d20d6b2889149c3b9892290dfa07ce8b0f09ca4d7507a0f4.jpg)  
(b) $C _ { L } { = } 5 . 4 2 .$

![](/api/attachments/XGPV2B6K/fulltext/images/62b90836d5e29e087b034a5c1b67c2e74ce65a8fca8b5b60f98f168a38081fdb.jpg)  
Fig. 7. The impact of $C _ { \mathrm { { L } } }$ and S(0) on virus infection outbreaks.

![](/api/attachments/XGPV2B6K/fulltext/images/71f03a44482f9703931963ab0c6c53c3661305bd14744f38ce9ce16a4f7a6a9e.jpg)  
Fig. 8. The max<sub>t</sub> S(t).

Next, let us take a look at the above result from a different perspective. As indicated in Section 5, to avoid virus infection outbreaks, we should guarantee that $\mathrm { d } E / \mathrm { d } t \leq 0$ for all t, which is equivalent to

$$
\max _ {t} f _ {m _ {E}} (S (t)) = \frac {r \theta}{m _ {E}} \left(\frac {\max _ {t} S (t)}{N}\right) \leq 1.
$$

Then, we observe the relationship between max $\cdot f _ { m _ { E } } ( S ( t ) )$ and S(0) at different $C _ { \mathrm { { L } } }$ values (adjusted by $m _ { E } )$ . As shown in Fig. 8, there are two types of relationships between max $f _ { m _ { E } } ( S ( t ) )$ ) and $S ( 0 ) { \mathrm { ; } }$

• When $C _ { \mathrm { { L } } } { > } 1 ,$ i.e., m b10.9, line “max $f _ { m _ { E } } ( S ( t ) ) ^ { \prime }$ consists of two pieces with $( S _ { 2 } ^ { * } , 1 )$ as the turning point. In other words, max $f _ { m _ { F } } ( S$ $\mathbf { \tau } ( t ) ) \geq 1$ , and the equality holds if and only $\mathrm { i f } S ( 0 ) = S _ { 2 } ^ { * }$ (note that ${ \bar { S } } _ { 2 } ^ { * }$ is different for different $m _ { E } )$ . This means that there will be at least one virus infection outbreak given $C _ { \mathrm { { L } } } { > } 1$ for any $S ( 0 )$ level, since the probability that $S ( 0 ) = S _ { 2 } ^ { * }$ is close to 0. This agrees with Fig. 7(b). Also, it is interesting to show that a smaller S(0) might result in a more serious outbreak, since max $f _ { m _ { E } } ( S ( t ) )$ goes up as $S ( 0 )$ goes down in the left piece of the line. Fig. 7(b) also shows that the peak of line $\ " S ( 0 ) = 2 0 0 0 "$ is higher than the peak of line $\ " S ( 0 ) = 8 0 0 0 "$ • When $C _ { \mathrm { L } } { \leq } 1 , \mathrm { i . e . , } m _ { E } { \geq } 1 0 . 9$ , line “max $f _ { m _ { E } } ( S ( t ) ) ^ { \prime }$ consists of two pieces with $( S _ { 1 } ^ { * } , C _ { \mathrm { L } } )$ as the turning point. When $S ( 0 ) = S _ { 1 } ^ { * }$ , max $f _ { m _ { F } } ( S ( t ) ) =$ $C _ { \mathrm { L } } { \le } 1 .$ . If we further increase S(0) but keep $S _ { 1 } ^ { * } { < } S ( 0 ) { \le } S _ { 2 } ^ { * }$ , we still have max<sub>t</sub> $f _ { m _ { E } } \ ( S ( t ) ) { \leq } 1$ , although the value of max $f _ { m _ { E } } \ ( S ( t ) )$ increases linearly. This means that for $S ( 0 ) { \leq } S _ { 2 } ^ { * } ,$ , no virus infection outbreak can happen. However, if the level of $S ( 0 )$ is beyond $S _ { 2 } ^ { * }$ , there is at least one virus infection outbreak since max $f _ { m _ { F } } ( S ( t ) ) { > } 1$ . This is consistent with Fig. $7 ( \mathtt { a } ) . \mathsf { S o } S _ { 2 } ^ { * }$ is the critical point for virus infection outbreaks if $\mathrm { \Delta } C _ { \mathrm { L } } { < } 1$

In summary, virus infection outbreaks are strongly related to the two parameters: $C _ { \mathrm { L } }$ and S(0). If $C _ { \mathrm { L } } { > } 1$ , multiple virus infection outbreaks will be launched. Otherwise, if $C _ { \mathrm { L } } { < } 1$ , one and only one outbreak will be launched for $S ( 0 ) { > } S _ { 2 } ^ { * }$ . For the rest, there will be no outbreak at all.

## 7.4. The effect of $C _ { S }$ -control and multi-stage control strategy

In this subsection, we evaluate the antivirus strategy $- C _ { S }$ -control. We aim to use $C _ { S } .$ -control to ful<sup>fi</sup>ll the antivirus objectives established in Section 6.2.

![](/api/attachments/XGPV2B6K/fulltext/images/02ac05f8672f5d710f348158f3d22c4b51dec76b0f3f8d989120eab36521b478.jpg)

(b) Case1: $C _ { S ^ { - } } \mathrm { C o n t r o l } .$  
![](/api/attachments/XGPV2B6K/fulltext/images/04800eaffaa511e0a1b00191b1e847b927320c7c637e0800553a8103139280a9.jpg)  
Fig. 9. The C<sub>S</sub>-control effect for Case 1.

We <sup>fi</sup>rst consider a simple case. In this case, we assume that we have had excellent pre-immunization work before we <sup>fi</sup>nd some Estate nodes. In other words, we have a low $S ( 0 ) _ { \ O }$ , say 10,000, but a high $R ( 0 ) = 8 9 , 0 0 0$ . However, we may still suffer from the virus since we have a low antivirus level for E-state nodes, i.e., $m _ { E } = 2 . 0 $ . Other parameters can be found in Table 2 (denoted by $\ " \mathrm { F i g . } 9 ( \mathsf { a } ) \ " )$ . According to Eq. (16), $C _ { S } { < } 1$ is equivalent to

![](/api/attachments/XGPV2B6K/fulltext/images/0fb74840234f89fe966fa90f2e87e952c83837a4a37ad7c2184d9b4376991656.jpg)

![](/api/attachments/XGPV2B6K/fulltext/images/21d76a766bc72afec4a4f7f7f3628824d75ef08562a7655075eb35b35757a8b4.jpg)  
(c) Case 2: Cs-Control.  
(a) Case 2: No Control.

$$
m _ {E} > r \theta \max \left(\frac {S (0)}{N}, \frac {\mu}{\mu + \rho_ {\mathrm{SR}}}\right) = 3. 8 8.
$$

So we simply increase the m level to $m _ { E } = 4 ,$ , then we can realize the C -control. Fig. 9(a) and (b) show the situations before and after employing $C _ { S }$ -control respectively. As can be seen in the <sup>fi</sup>gures, we avoid virus infection outbreaks and drive the system into the virusfree equilibrium with $C _ { S }$ -control. Actually, in this case, $C _ { S }$ -control reduces to the C -control due to the low S(0) value.

Next, we consider a more complicated case. In this case, we assume that we have a poor pre-immunization level with $S ( 0 ) = 7 0 { , } 0 0 0$ and $R ( 0 ) = 2 9 , 0 0 0 ,$ and other parameters are exactly the same as the previous case. As can be seen in Fig. 10(a), multiple virus infection outbreaks occur before the system goes into the virus-epidemic equilibrium, and the peaks are much higher than the ones in the former case.

If we only use $C _ { \mathrm { { L } } }$ -control in this case, as shown in Fig. 10(b), the peaks of $E ( t )$ and I(t) are still very high (max $I ( t ) { > } 1 0 { , } 0 0 0 )$ . This can cause a fatal damage to the system, although the number of peaks has been reduced to one.

Instead, we can use $C _ { S }$ -control in this case. Similar to the former case we have $m _ { E } { > } 2 1 . 0 .$ Then, we can set $m _ { E } = 2 2 . 0 ,$ , and the control effect can be seen in Fig. 10(c). As can be seen, we achieve a similar effect as Fig. 9(b). However, it takes more than 2500 units of time for the system to go into the equilibrium. Also, it is often not practical to maintain C -control for such a long period, since we have limited antivirus resources.

Finally, we can also use multi-stage $C _ { S ^ { - } }$ control. That means we lower the $m _ { E }$ level step by step according to the $S ( t )$ level as well as the $C _ { S ^ { - } }$ control requirements. When the system reaches the equilibrium eventually, $C _ { S ^ { - } } \mathrm { c o n t r } 0 1$ then reduces to $C _ { \mathrm { L } ^ { - } } \mathrm { c o n t r } 0 \mathsf { l } .$ . Fig. 10(d) shows the effect of three-stage $C _ { S }$ -control. In the <sup>fi</sup>rst stage, $S _ { I } ( 0 ) =$

(b) Case 2: CL-Control.  
![](/api/attachments/XGPV2B6K/fulltext/images/9d03f3a9f7bc91a870ca52dd561bc4320579cbfb30b75e5981c89a1c2c046d29.jpg)

(d) Case 2: Multi-stage Cs-Control.  
![](/api/attachments/XGPV2B6K/fulltext/images/ca68623f669aba3d959bd2104dabf4b030d8e5a86abf31c5ec183c15a112005d.jpg)  
Fig. 10. The C -control effects for Case 2.

70,000, so we have to increase m to 22.0. And $E ( t )$ goes down rapidly in this stage. Then after 1.5 months≈1090 units of time, we enter the second stage. In this stage, the initial number of S-state nodes $S _ { I I } ( 0 ) =$ $S _ { I } ( 1 , 0 9 0 ) = 3 0 , 0 0 7 ,$ , and to keep $C _ { S } { < } 1$ we should guarantee $m _ { E } { > } 9 . 0$ Thus we can reduce $m _ { E }$ from 22.0 to 10.0 and still ensure no virus infection outbreak. After 3.5 months≈2530 units of time, there comes the <sup>fi</sup>nal stage. Similarly, we have $S _ { I I I } ( 0 ) = S _ { I I } ( 2 , 5 3 0 ) = 1 7 , 1 7 1$ , and the m can be further reduced to 5.5. Then we keep m on this level until the system goes into the virus-free equilibrium. During this threestage process, no virus infection outbreak can happen, and the control effect (refer to E(t) in Fig. 10(d)) is very similar to the one in Fig. 10(c). Meanwhile, we avoid a great waste of resources by steadily reducing the $m _ { E }$ level. Note that the relative changes of $\rho _ { S \mathrm { R } }$ and $m _ { E }$ values in Fig. 10(d) well illustrated the resource competitions for different antivirus countermeasures.

## 7.4.1. Discussion

It is worthwhile to make a brief comparison among the $C _ { \mathrm { L } } , C _ { S }$ and multi-stage $C _ { S }$ -control strategies as follows:

• Without any control, the economic costs due to the virus infection can be extremely high, since the peak of the E-state nodes is sharp, as illustrated in Fig. 10(a). Moreover, the convergence time for the number of E-state nodes is also very long, say, over 3000 in Fig. 10(a) with multiple virus infection outbreaks.

• While $C _ { \mathrm { L } ^ { - } } \mathrm { c o n t r } 0 \vert$ has a fast convergence for the number of E-state nodes, and takes lower antivirus costs than $C _ { S ^ { - } }$ and multi-stage $C _ { S ^ { - } }$ control, the system still suffers from the great economic costs with a sharp peak of the E-state nodes, as illustrated in Fig. 10(a).

• The greatest strength of C -control is to prevent virus infection outbreaks so that the economic costs can be minimized. Also, the convergence time for the number of E-state nodes is modest, as illustrated in Fig. 10(c). Nevertheless, the weakness of $C _ { S }$ -control is also noteworthy. That is, it needs much higher antivirus efforts than $C _ { \mathrm { { L } ^ { - } } }$ -control, which increases the managerial costs dramatically. In some cases, the costs are just too high to meet given the limited antivirus resources.

• Multi-stage C -control is the re<sup>fi</sup>ned version of $C _ { { \sf S } ^ { - } } \mathrm { c o n t r } 0 \mathrm { l } .$ . It inherits the merits of $C _ { S ^ { - } }$ control, and lowers the antivirus costs substantially by a stepwise strategy, as illustrated in Fig. 10(d). To lower both the economic costs and managerial costs in antivirus activities, the multi-stage $C _ { S ^ { - } }$ -control is a good choice.

## 8. Concluding remarks

In this paper, we have proposed a virus propagation model named E-SEIR to study the computer virus prevalence in P2G information sharing networks. This model is a natural extension of the traditional SEIR model in biological epidemics. However, E-SEIR differs from SEIR and other existing models in taking multiple state transition paths, which enable it to better capture the behaviors of virus prevalence in real-world information systems. Also, since information systems usually consist of many information-sharing sub-groups, a P2G infection function has been integrated into E-SEIR to model this information sharing pattern. Furthermore, the E-SEIR model can take various antivirus countermeasures into consideration, and thus has the ability to study the behaviors of virus propagation at the presence of antivirus activities.

Moreover, we have exploited the E-SEIR model for investigating short-term and long-term virus propagations. The analysis and experiments have highlighted four managerial insights. First, if there are few antivirus countermeasures deployed in the system, the system will be evolved into a non-healthy stage of virus spread. However, before the system reaches this stage, there will be several short-term virus outbreaks. Second, it is relatively dif<sup>fi</sup>cult to control short-term virus outbreaks compared with the prevention of long-term virus existing in the system. Third, although pre-immunization cannot completely prevent short-term virus outbreaks, it can at least save the costs caused by them. Finally, we can effectively reduce the risk of virus outbreaks by deploying antivirus countermeasures for the Estate information nodes.

## Acknowledgements

The work was partly supported by the National Natural Science Foundation of China (No.70890080/70621061), the Ph.D. Programs Foundation of Ministry of Education of China (No.200800060031), the Lan Tian Xin Xiu Seed Funding of Beihang University, the Research Center for Contemporary Management at Tsinghua University, and the National Science Foundation (NSF) of USA via grant number CNS 0831186.

## Appendix A. The proof of Lemma 1

Let $\begin{array} { r } { { \hat { \boldsymbol { \beta } } } = \alpha r { \boldsymbol { \theta } } / N . } \end{array}$ The Jacobian matrix of the system described by Formulation (7) can be computed as follows:

$$
J = \left[ \begin{array}{c c c} - \big (\hat {\beta} E + \rho_ {\mathrm{SR}} + \mu \big) & - \hat {\beta} S + \rho_ {\mathrm{ES}} & \rho_ {\mathrm{IS}} \\ \hat {\beta} E & \hat {\beta} S - m _ {E} \alpha & 0 \\ 0 & \alpha & - (\gamma + \rho_ {\mathrm{IS}} + \mu) \end{array} \right].\tag{17}
$$

Therefore, according to Eq. (9), the Jacobian matrix at the virusfree equilibrium $\mathtt { E Q } _ { \mathrm { v f } }$ is

$$
J (\mathrm{EQ} _ {\mathrm{vf}}) = \left[ \begin{array}{c c c} - (\rho_ {\mathrm{SR}} + \mu) & - \hat {\beta} S _ {1} ^ {*} + \rho_ {\mathrm{ES}} & \rho_ {\mathrm{IS}} \\ 0 & \hat {\beta} S _ {1} ^ {*} - m _ {E} \alpha & 0 \\ 0 & \alpha & - (\gamma + \rho_ {\mathrm{IS}} + \mu) \end{array} \right].\tag{18}
$$

The corresponding eigenvalues of $J ( \mathrm { E Q } _ { \mathrm { v f } } )$ are

$$
\left\{ \begin{array}{l c l} \lambda_ {1} & = & - (\rho_ {S R} + \mu), \\ \lambda_ {2} & = & \hat {\beta} S _ {1} ^ {*} - m _ {E} \alpha , \\ \lambda_ {3} & = & - (\gamma + \rho_ {\mathrm{IS}} + \mu). \end{array} \right.
$$

By the stability theory [27,36], the suf<sup>fi</sup>cient condition for the three-dimension system to be asymptotically stable is that $\lambda _ { i } { < } 0 ,$ , for $i = 1 , 2 , 3 ,$ . It is easy to show $\lambda _ { 1 } { < } 0$ and $\lambda _ { 3 } < 0$ in our system. As to $\lambda _ { 2 } , \lambda _ { 2 } { < } 0$ is equal to $S _ { 1 } ^ { * } { < } m _ { E } \alpha / \beta .$ If we substitute $\boldsymbol { S _ { 1 } ^ { * } } { = } \mu \boldsymbol { N } /$ $( \rho _ { S R } + \mu )$ and $\beta { = } \alpha r \theta / N$ into the above inequality, we have $\frac { r \theta \mu } { m _ { E } ( \rho _ { \ S R } + \mu ) } { < } 1$ which is exactly the suf<sup>fi</sup>cient condition in the lemma.

## Appendix B. The proof of Lemma 2

For the case of the virus-epidemic equilibrium $\mathrm { E Q } _ { \mathrm { v e } }$ in Eq. (10), however, things are more complicated. The Jacobian matrix at $\mathrm { E Q } _ { \mathrm { v e } }$ is

$$
J (\mathrm{EQ} _ {\mathrm{ve}}) = \left[ \begin{array}{c c c} - \left(\hat {\beta} E _ {2} ^ {*} + \rho_ {\mathrm{SR}} + \mu\right) & - m _ {E} \alpha + \rho_ {\mathrm{ES}} & \rho_ {\mathrm{IS}} \\ \hat {\beta} E _ {2} ^ {*} & 0 & 0 \\ 0 & \alpha & - (\gamma + \rho_ {\mathrm{IS}} + \mu) \end{array} \right].\tag{19}
$$

Apparently the trace is non-positive, and we can show that the determinant is also negative. The eigenfunction of $J ( \mathrm { E Q } _ { \mathrm { v e } } )$ is

$$
f (\lambda) = a _ {3} \lambda^ {3} + a _ {2} \lambda^ {2} + a _ {1} \lambda + a _ {0},
$$

where

$$
\left\{ \begin{array}{l l l} a _ {3} & = & 1, \\ a _ {2} & = & (\gamma + \rho_ {\mathrm{IS}} + \mu) + \big (\hat {\beta} E _ {2} ^ {*} + \rho_ {\mathrm{SR}} + \mu \big), \\ a _ {1} & = & (\gamma + \rho_ {\mathrm{IS}} + \mu) \big (\hat {\beta} E _ {2} ^ {*} + \rho_ {\mathrm{SR}} + \mu \big) + \hat {\beta} E _ {2} ^ {*} (m _ {E} \alpha - \rho_ {\mathrm{ES}}), \\ a _ {0} & = & (\gamma + \rho_ {\mathrm{IS}} + \mu) \hat {\beta} E _ {2} ^ {*} (m _ {E} \alpha - \rho_ {\mathrm{ES}}) - \alpha \hat {\beta} E _ {2} ^ {*} \rho_ {\mathrm{IS}}. \end{array} \right.
$$

As pointed out in Eq. (11), the virus-epidemic equilibrium exist only $\mathrm { i f } \frac { r \theta \mu } { m _ { E } ( \rho _ { \mathrm { S R } } + \mu ) } > 1$ . Then by the Routh–Hurwitz criterion, the Routh– Hurwitz array for $\mathrm { E Q } _ { \mathrm { v e } }$ is as follows:

$$
\left[ \begin{array}{c c} a _ {3} & a _ {1} \\ a _ {2} & a _ {0} \\ (a _ {1} a _ {2} - a _ {0} a _ {3}) / a _ {2} & 0 \\ a _ {0} & 0 \end{array} \right]
$$

Therefore, if we can verify that $( a _ { 1 } a _ { 2 } - a _ { 0 } a _ { 3 } ) / a _ { 2 }$ has the same sign with $a _ { 1 } ,$ then the three eigenvalues all have negative real parts. Obviously $a _ { 1 } > 0 .$ . Also, $( a _ { 1 } a _ { 2 } - a _ { 0 } a _ { 3 } ) / a _ { 2 } > 0 \iff a _ { 1 } a _ { 2 } - a _ { 0 } > 0$ , and the latter holds by the computations of $a _ { 0 } , \ a _ { 1 }$ and a . So the three eigenvalues all have negative real parts, which implies that the virusepidemic equilibrium is asymptotically stable.

## References

[1] R.M. Anderson, R.M. May, Infectious Diseases of Humans: Dynamics and Control, Oxford University Press, USA, 1992.

[2] J. Balthrop, S. Forrest, M.E.J. Newman, M.M. Williamson, Technological networks and the spread of computer viruses, Science 304 (April 2004) 527–529.

[3] Elisa Bertino, L.R. Khan, Ravi S. Sandhu, Bhavani M. Thuraisingham, Secure knowledge management: con<sup>fi</sup>dentiality, trust, and privacy, IEEE Transactions on Systems, Man, and Cybernetics, Part A 36 (3) (2006) 429–438.

[4] Li-Chiou Chen, Kathleen M. Carley, The impact of countermeasure propagation on the prevalence of computer viruses, IEEE Transactions on Systems, Man and Cybernetics, Part B 34 (2) (2004) 823–833.

[5] T. Chen, N. Jamil, Effectiveness of quarantine in worm epidemics, IEEE International Conference on Communications 2006, IEEE, June 2006, pp. 2142–2147.

[6] D.M. Chess, The future of viruses on the internet, Virus Bulletin International Conference, 1997.

[7] Symantec Corp. Symantec early warning solutions. In http://enterprisesecurity. symantec.com/.

[8] CSI/FBI. ’2004 CSI/FBI computer crime and security survey’ and ’2005 CSI/FBI computer crime and security survey’. www.gocsi.com.

[9] S. Datta, H. Wang, The effectiveness of vaccinations on the spread of email-borne computer viruses, IEEE CCECE/CCGEI, IEEE, May 2005, pp. 219–223.

[10] M. Garetto, W.B. Gong, D. Towsley, Modeling malware spreading dynamics, IEEE INFOCOM, IEEE, 2003, pp. 1869–1879.

[11] W. Gleissner, A mathematical theory for the spread of computer viruses, Computers & Security 8 (1989) 35–41.

[12] C. Grif<sup>fi</sup>n, R. Brooks, A note on the spread of worms in scale–free networks, IEEE Transactions on Systems, Man and Cybernetics, Part B 36 (1) (2006) 198–202.

[13] S. Groves, The unlikely heroes of cyber security, Information Management Journal 37 (3) (May/June 2003) 34–40.

[14] A.W. Harrison, R.K. Rainer, The in<sup>fl</sup>uence of individual differences on skill in enduser computing, Journal of Management Information Systems 9 (1992) 93–111.

[15] H.W. Hethcote, The mathematics of infectious diseases, SIAM REVIEW 42 (4) (October 2000) 599–653.

[16] ICSA. Annual computer virus prevalence survey. ICSA Labs, TruSecure Corporation, www.icsalabs.com/icsa/docs/.

[17] J.O. Kephart, G.B. Sorkin, D.M. Chess, S.R. White, Fighting computer viruses Sienti<sup>fi</sup>c American (1997) 88–93.

[18] J.O. Kephart, S.R. White, D.M. Chess, Computers and epidemiology, IEEE Spectrum 30 (1993) 20-26.

[19] J.O. Kephart, S.R. White, Directed-graph epidemiological models of computer viruses, IEEE Symposium on Security and Privacy, 1991, pp. 343–361.

[20] J.O. Kephart, S.R. White, Measuring and modeling computer virus prevalence, IEEE Computer Security Symposium on Research in Security and Privacy, IEEE, 1993, pp. 2–15.

[21] M. Kuperman, G. Abramson, Small world effect in an epidemiological model, Physical Review Letters 86 (13) (2001) 2909–2912.

[22] J.-Q. Lia, R. Sikorab, M.J. Shawa, G.-W. Tan, A strategic analysis of inter organizational information sharing, Decision Support Systems 42 (1) (2006) 251–266.

[23] A.L. Lloyd, R.M. May, How viruses spread among computers and people, Science 292 (5520) (May 2001) 1316–1317.

[24] N. Madar, T. Kalisky, R. Cohen, D. ben Avraham, S. Havlin, Immunization and epidemic dynamics in complex networks, European Physical Journal B 38 (2004) 269–276.

[25] J. Marro, R. Dickman, Nonequilibrium Phase Transitions in Lattice Models, Cambridge University Press, Cambridge, 1999.

[26] R.M. May, A.L. Lloyd, Infection dynamics on scale-free networks, Physical Review E 64 (066112) (2001) 1–3

[27] Merkin, D. Rakhmilevich, Introduction to the theory of stability, Springer, New York, 1997.

[28] D. Moore, C. Shannon, G.M. Voelker, S. Savage, Internet quarantine: requirements for containing self-propagating code, Proceedings of IEEE INFOCOM2003, IEEE, April 2003.

[29] Y. Moreno, R. Pastor-Satorras, A. Vespignani, Epidemic outbreaks in complex heterogeneous networks, European Physical Journal B 26 (2002) 521–529.

[30] J.D. Murray. Mathematical Biology. I, Introduction. Springer, New York, 2002.

[31] W. Murray, The application of epidemiology to computer viruses, Computers & Security 7 (1988) 35–41.

[32] Insu Park, R. Sharman, H.R. Rao, S. Upadhyaya, Short term and total life impact analysis of email worms in computer systems, Decision Support Systems 43 (3) (2007) 827–841.

[33] R. Pastor-Satorras, A. Vespignani, Epidemic dynamics and endemic states in complex networks, Physical Review E 63 (066117) (2001) 1–8.

[34] R. Pastor-Satorras, A. Vespignani, Epidemics and Immunization in Scale-free Networks in, Handbook of Graphs and Networks: From the Genome to the Internet, Wiley-VCH, Berlin, 2002.

[35] J.R.C. Piqueira, B.F. Navarro, L.H.A. Monteiro, Epidemiological models applied to viruses in computer networks, Journal of Computer Science 1 (1) (2005) 31–34.

[36] R.C. Robinson, An introduction to Dynamical System: Continuous and Discrete, Prentice Hall, USA, 2004.

[37] C.D. Schou, K.J. Trimmer, Editorial preface: information assurance and security, Journal of Organizational and End User Computing 16 (3) (July–September 2004) I–VII.

[38] Bhavani M. Thuraisingham, Chris Clifton, Amar Gupta, Elisa Bertino, Elena Ferrari, Directions for Web and E-commerce Applications Security, 2001, pp. 200–204, WETICE.

[39] S.R. White, Open problems in computer virus research, Virus Bulletin Conference, 1998.

[40] Steve R. White, Jeffrey O. Kephart, David M. Chess, Computer viruses: a global perspective, In Proceedings of the 5th Virus Bulletin International Conference, Virus Bulletin Ltd, September 1995, pp. 165–181.

[41] M.E. Whitman, H.J. Mattord, Making users mindful of it security: awareness training is vital to keeping the idea of it security uppermost in employees' minds, Security Management 48 (11) (November 2004) 32–34.

[42] J.C. Wierman, Probabilistic analysis of a computer virus epidemic model, Proceedings of the Workshop on Statistical and Machine Learning Techniques in Computer Intrusion Detection, 2002.

[43] Ma.M. Williamson, J. Leill, An epidemiological model of virus spread and cleanup, 2003, In http://www.hpl.hp.com/techreports/.

[44] Hua Yuan, Junjie Wu, Guoqing Chen, Adapting the right infection functions for virus propagation in computer networks, Proceedings of AMIGE 2008 IEEE Symposium, IEEE, 2008, pp. 1–5.

[45] Hai Zhuge, Knowledge <sup>fl</sup>ow network planning and simulation, Decision Support Systems 42 (2) (2006) 571-592.

[46] C. Zou, W. Gong, D. Towsley, Code red worm propagation modeling and analysis, Proceedings of CSS02, 2002.

[47] C. Zou, W. Gong, D. Towsley, Worm propagation modeling and analysis under dynamic quarantine defense, Proceedings of the ACM CCS Workshop on Rapid Malcode, ACM, October 2003, pp. 51–60.

[48] C. Zou, W.B. Gong, D. Towsley, L.X. Gao, The monitoring and early detection of internet worms, IEEE/ACM Transactions on Networking 13 (5) (October 2005) 961-974.

[49] C. Zou, D. Towsley, W.B. Gong, Modeling and simulation study of the propagation and defense of internet e-mail worms, IEEE Transactions on Dependable and Secure Computing 4 (2) (April–June 2007) 105–118.

Hua Yuan has received his master’s degree in Management Information Systems from the School of Economics and Management (SEM), Tsinghua University. He is a PhD candidate student in Management Science and Engineering Department at SEM. His research interests focus on information system management and information security data mining, system modeling and system simulation.

Guoqing Chen received his PhD from the Catholic University of Leuven (K.U. Leuven, Belgium) and now is Professor of Information Systems at School of Economics and Management, Tsinghua University (Beijing, China). His research interests include Information Systems Management, Business Intelligence and Decision Support, and Soft Computing. Dr. Chen is member of ACM (SIGMOD and SIGKDD) and AIS and has wide publications internationally including a monographic book on data modeling published by Kluwer Academic Publishers (Boston, 1998).

Junjie Wu is currently an Assistant Professor in the Information Systems Department, School of Economics and Management, Beihang University, China. He received the B.E. degree in Civil Engineering and the Ph.D. degree in Management from Tsinghua University, China. His general research area is data mining and business intelligence, with a special interest on clustering, rare class analysis and information security. He has published near 10 technical papers in peer-reviewed journals and conference proceedings including SIGKDD and ICDM. He is a member of AIS.
