---
otero_id: 2538
otero_key: "4HR5GPP6"
title: "Simulating Internet-based collaboration: A cost-benefit case study using a multi-agent model"
authors: "Te-Wei Wang; Suresh K. Tadisina"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.020"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Simulating Internet-based collaboration: A cost-benefit case study using a multi-agent model

Te-Wei Wang<sup>a,\*</sup>, Suresh K. Tadisina<sup>b,1</sup>

<sup>a</sup>Department of Decision Science and Information Systems, Florida International University, 11200 SW 8th Street RB254B, Miami, FL 33199, USA <sup>b</sup>Department of Management, Southern Illinois University at Carbondale, USA

Available online 12 July 2005

## Abstract

The relationship between the adoption of Internet-based communication technology (ICT) and coordination performance has not been explored in sufficient depth in the literature. We argue that the impact of ICT on a coordination system typically needs to be studied on a case-by-case basis. A case study utilizing multi-agent simulation to support decision-making is described. We built the simulation system based on a theoretical model and a real world case. Through a proper verification process, we demonstrate that a multi-agent simulation experiment is a valid decision support tool for IT investment decisions. From the particular context of our case, we observe that the adoption of ICT is not a determinant of productivity. To save time and to cut cost, decision makers should focus more on technology utilization and business process redesign. <sup>D</sup> 2005 Elsevier B.V. All rights reserved

Keywords: Multi-agent simulation; Simulation experiment; IT investment; Heterogeneous group; Internet communication; Plastic tooling; Process reengineering

## 1. Introduction

In today’s competitive environment, it is tempting and sometimes necessary to invest in information technology (IT). However, many firms have felt that the promised cost saving and productivity gain from IT can seldom be realized. This phenomenon has been observed by many researchers and is referred to as the

IT productivity paradox [6,15]. Recent research suggests that the causal relationship between IT investment and productivity gain is indirect and complex. It is moderated by many factors. These factors include the fit between IT and business process [15], managerial performance [35], lack of performance metrics [50], and many other complementary factors [13,22]. Indeed, assessing return on IT investment is intrinsically difficult. Nonetheless, business owners and managers still need recommendations to justify their IT spending. We believe that the best way to provide guidance to decision makers is by offering powerful decision support tools and methods. Analogous to the practice of weather forecasting, if our method can provide reasonable estimates of relevant performance measures, decision makers can use the results to justify IT spending.

In this study, we develop a multi-agent simulation method to simulate heterogeneous project-team coordination. The simulation model is based on a theoretical framework. We use a real world case from the plastic-tooling industry to build and to verify the simulation program. With a designed simulation experiment, this paper describes how to use multi-agent simulation as a decision support tool.

## 2. Case description

Our simulation study is based on operational data obtained from CMT International, Inc., an international plastic-tooling supplier. A typical plastic-tooling supplier usually deals with multiple manufacturers. Each manufacturer may engage in multiple projects with the same supplier. The operational objectives for suppliers include cutting cost, satisfying certain performance criteria, and meeting project deadlines. To remain competitive, plastic-tooling suppliers need to use every opportunity to cut costs and to reduce project delivery time (the time required from product design to product delivery). In addition, plastic-tooling suppliers are subject to many constraints. For instance, capacity is one major problem. Due to the highly technical nature of tooling projects, experienced engineers are scarce resources.

CMT is actually a branch office in the US. Its parent company is based in Taiwan. CMT’s main role is to maintain effective communication with its customers. In fact, the internal structure of CMT is a project team consisting of engineers and marketing personnel traveling across the globe (especially in the US). The major communication methods for this team included face-to-face communication, telephone conversation, and postal mailing (or similar physical delivery) systems. In year 2001, several of its major customers were pushing the firm to use Internet as a communication and document exchange tool. The director of this company was evaluating alternatives for investing in ICT.

At the time of our study, CMT was using narrowbandwidth Internet connection for basic communication (E-mail, file transfer, etc.). CMT’s director was considering whether to invest in the new broad-bandwidth Internet connection (such as Digital Subscriber’s Line, DSL, and/or Satellite Internet Connection), and whether to use Business-to-Business market transaction and payment tracking services. The company hoped that broad-bandwidth connection could greatly reduce their communication cost. It also expected that the payment tracking service could help the company reduce delivery lead-time. To justify the company’s investment decision, the director decided to use results from this simulation study to evaluate each of the alternatives.

## 3. Research model and theoretical background

Internet technologies have been considered as valid communication media for both document exchange and communication [24]. Using Internet as communication media, without doubt, can provide an alternative way for group communication. The question is whether the benefits justify the investment in Internet technology, especially economic benefits [44]. Thus, building a decision support tool to facilitate the above decision-making process is logical.

## 3.1. Research model and dependent variables

A research model illustrated in Fig. 1 is the foundation of our simulation method. This research model follows McGrath and Hollingshead’s [29] conceptual framework that uses an input–process–output mapping to study technology management. There are four major conceptual components in the model: technological factors, social factors, coordination systems, and performance. In this study, the inputs are the technological factors that relate to Internet facilitated communication. The outputs are the performance measures of a coordination system. Lastly, social factors are considered as environmental or moderating factors, which may change the behaviors of participating companies and the coordination system design.

The first challenge in using this research model in simulation is selecting the output measurements. The performance of an IT-based coordination system can be measured from many different perspectives and at different levels [4,11,12,37]. In the case of coordination between business partners, at least two perspectives and three levels are relevant. The two perspectives are economic perspective and social perspective [14,18,23]. The three levels are individual level, firm level, and supply chain level [7,23].

![](/api/attachments/4HR5GPP6/fulltext/images/c9e98ffe26c1b43999890ea65a5cc0bf50e3f2acf91d4be80a808eee38eb635d.jpg)  
Fig. 1. Research model.

The economic perspective defines performance primarily in terms of time and cost related measures. In contrast, the definitions of performance from a social perspective can range from user satisfaction, non-economic organizational goals, to partnership quality (see Table 1). In the present study, we define performance from an economic perspective.

Among the three possible levels of performance measures, firm level and supply chain level are most relevant for managers in making investment decisions. In the present study, measurements at the individual level are considered less significant. From the supplying companies’ perspective, firm level performance should be measured over a specific time frame. Depending on the need of a particular company, the cost and time savings can be evaluated over a month, a quarter, a year, or throughout the life cycle of the adopted technology. Therefore, a time frame needs to be specified. In addition, the newly adopted technology may not be used for all projects. Some customers may not be able to utilize the new technologies. Thus, supply chain level performance can refer to one project, a set of projects, or all projects.

## 3.2. Coordination systems and process reengineering

In the research model, the system that our simulation model attempts to imitate is called a coordination system. A coordination system is designed to facilitate coordination between system components. In supply chain management, coordination systems facilitate business partners to work together. In this paper, we adopted Malone and Crowson’s [26] suggestions and define a coordination system as follows:

A coordination system is the arrangement of system components, the sequence of activities (or tasks) and the interactions between system components and their activities in a system.

Two dimensions of performance measurement of a coordination system

<table><tr><td></td><td>Economic perspective</td><td>Social perspective</td></tr><tr><td>Individual level</td><td>Personal time saving</td><td>User satisfactionSocial presenceCommunication-effectiveness</td></tr><tr><td>Firm level</td><td>Cost savingTime saving</td><td>Non-economical goalsCompetitive advantagesFirm reputationOther organizational goal</td></tr><tr><td>Supply chain level</td><td>Meeting deadlineReduce project completion timeSupply chain coordination costs</td><td>Partnership qualityTrustCommitmentBusiness understandingBenefit and risk sharing</td></tr></table>

The performance of a coordination system depends largely on system design as opposed to the use of IT. Business process design and coordination theory literature suggest that to design a social coordination system, at least five different elements should be specified [49]. The five elements are: system components [26], system component structure [25], required tasks [25,26], task precedence relationships [27], and task assignments between system components and required tasks [3,27]. Fig. 2 depicts the five elements graphically.

IT, including the ICT studied in this paper, can be considered as one type of system component. In a coordination system such as engineering project coordination, IT may induce several generic system redesigns. We describe these design ideas and their potential benefits into three propositions.

Proposition 1. Replacement of system components: ICT can replace existing system components and provide time and cost advantages to a coordination system.

Obviously, using ICT to replace traditional communication technologies such as telephone system or postal system can save time used for communication. Earlier studies on EDI technology support this proposition [28,32].

Proposition 2. Change of task requirements and change of task precedence relationships: ICT can eliminate or change some tasks required when it replaces older methods of communication. Consequently, cost and time advantages may be observed.

When a new technology replaces an older technology, not only the system component is replaced but also results in a new coordination process. That is, with the new technology, some steps may be skipped and the coordination system can still achieve the same objective [49]. Communication research has provided substantial support for this proposition [7,10]. However, several studies suggest that this proposition is moderated by behavioral factors. For instance, Ozawa and Fisher [34] described a communication overkill problem, which involves redundancy of using multiple channels to deliver a simple message. Walther suggest that with proper training, a leaner media may outperform a richer counterpart [47,48]. Burke and Chidambaram’s study [7] also suggests that the fit between the technology characteristics and human behavior patterns does change technology’s performance. These human behaviors may impede the effectiveness of the new communication technology.

Proposition 3. Change of coordination system component structure and task assignments: ICT can change both the coordination system structure and task assignments. The new system structure and the new roles of system components, over time, may provide both cost and time advantages.

Research on IT-enabled organizational transformation suggests that unveiling the potential benefits of a new technology usually requires corresponding organizational changes [30,36]. Nonetheless, a successful fusion between an organization and its adopted technology requires a time-consuming organizational learning process [1]. In fact, the organizational transformation and the adoption of IT may be a mutual adjustment process. Therefore, we assume that ITrelated benefits cannot be realized in a relatively short time frame.

![](/api/attachments/4HR5GPP6/fulltext/images/d94c1339f73e479a4ea5adabf911fb1db84ecbae539e9783c2c136f86b3e9246.jpg)  
Fig. 2. The five elements of a coordination system.

## 3.3. Moderator variable: contextual and behavioral factors

Many contextual, social and behavioral factors may complicate the relationship between the adoption of ICT and coordination performance. We included one such factor in this study: technology utilization.

Literature in IT diffusion suggests that technology utilization is most pertinent to economic performance [7,28]. The rationale is very simple. Investment in ICT is usually a capital expenditure for most companies. Whether the new technology can be fully utilized is an important factor to justify the investment. If the newly invested technologies are not fully utilized, all the cost and time benefits cannot be realized. As observed from historical patterns of other communication technologies, utilization does play an important role in determining the associated costs and benefits [2].

## 3.4. Use of multi-agent simulation

In the context of IT investment decisions, prior research suggests that a simulation model built on a sound analytical framework is potentially an excellent tool to facilitate such decision-making [42,45]. In this study, we adopt a multi-agent simulation method to perform a similar task. Our study can be characterized as a project-oriented supply chain coordination study. In this study, a multi-agent simulation approach is justified as an appropriate method due to the following reasons.

1. Project coordination in a supply chain is usually loosely coupled because the coordination involves more than one business unit. The autonomous behavior of each unit is difficult (but not impossible) to model in traditional (deterministic) simulation models [43,46]. An agent-based model provides an easier alternative [5,8,9].

2. In a social system, policies, decision rules, and priorities are based either on analytical models or on human intuitions. Multi-agent simulation integrates the strengths of both analytical models and personal judgments through modeling individual agent behavior. The result is a simpler model [43].

3. The coordination projects studied in this paper are events driven. Using the state-transition model in multi-agent simulation simplifies the model building effort [46].

4. In general, a deterministic simulation model can usually be used to model coordination systems [9]. Although it may provide a more stable model, a deterministic model is less flexible and less realistic [43].

An agent is an autonomous or semi-autonomous entity identified in a problem domain. Each agent specializes in different activities, has its goals, knowledge base, and behavior [43]. Agent intelligence in a simulation model is determined by the algorithms used to simulate knowledge, beliefs, and even desires and intentions [19]. To effectively simulate a coordination system, the minimal intelligence that should be assigned to agents are agent’s awareness of its current state and an event handling mechanism [19,39]. Swaminathan et al. [43] suggested a generic agent architecture to satisfy the minimal requirements to simulate supply chain coordination. We adopt this architecture as the foundation to build our agent model (see Fig. 3).

![](/api/attachments/4HR5GPP6/fulltext/images/e2b7e59e3f0b1d223edd901a5769081eedd26c5ad4a7554e019abfb7197b7fc0.jpg)  
Fig. 3. Generic agent architecture.

## 4. Model building process

The multi-agent program used in this study is constructed through the following processes.

## 4.1. Step 1: process specification

Fig. 4 illustrates briefly CMT’s project management process at the time of study. The general process is defined under the assumption that there is no subcontractor and no material supplier involved in the supply chain. The coordination process, therefore, involves only interactions between customers and one single plastic-mold supplier. The description of the existing project management process provides a baseline comparison to other reconfigured (reengineered) processes. It is also the process knowledge that is possessed by the agents in our simulation model.

## 4.2. Step 2: agent identification and definition

Identifying potential <sup>b</sup>agents,<sup>Q</sup> defining agent attributes, and defining agent behaviors in multi-agent simulation models, requires detailed descriptions about the coordination process [43]. We adopted a business-level use-case analysis (a requirement analysis method used by software engineers) for this purpose. A complete use-case documentation is available from the authors. From the use-case analysis, we identified a list of potential agents that could be used in our simulation model. Then, a filtering process was used to select agents that appear in the final model. Based on Kinny et al.’s [19] recommendation, our filtering process used the following rules.

1. In multi-agent simulation, variables under examination are embedded in agent attributes. Therefore, for every variable of interest, there must be an agent containing such an attribute.

2. Data are stored within an agent. Therefore, an agent has to be created if it contains an important piece of data that cannot be represented otherwise.

3. Agents are required to perform tasks. Once a task is identified, there must be a corresponding set of agents created.

4. In a multi-agent simulation, decision algorithms are created within an agent. Therefore, when a decision has to be made, a corresponding agent has to be created.

Following the above guidelines, a list of agents was generated as shown in Table 2.

4.3. Step 3: component structure, model variation and process control

The component structure, which is later used as the architecture for our simulation program, is illustrated in Fig. 5. This model assumes that all coordination tasks, including both communication and non-communication tasks, need to go through a certain technology (as a message or physical goods carrier). Each non-technological agent has the knowledge (defined in agent behavior) of how to select appropriate tools (technology agents) to perform their tasks.

![](/api/attachments/4HR5GPP6/fulltext/images/55e5a794b1fd4dd4688dd901b96bd4f50e61a7aea326b1897fe0b43e6d3438e0.jpg)  
Fig. 4. CMT’s project management process.

<table><tr><td colspan="2">Agents used in the simulation model</td></tr><tr><td colspan="2">Organizational agents (non-technological agents)</td></tr><tr><td>MFGF</td><td>MFGF stands for “manufacturing firm.” Manufacturing firm agents represent the “customers.”</td></tr><tr><td>PRJT</td><td>PRJT stands for “project.” A project agent represents a project from a manufacturing firm.</td></tr><tr><td>ENGT</td><td>ENGT stands for “engineering team.” The engineering team agent is the supplier’s engineering team.</td></tr><tr><td>ACCT</td><td>ACCT stands for “accounting department.” It is the supplier’s accounting department.</td></tr><tr><td>MFGD</td><td>MFGD stands for “manufacturing department.” It is the supplier’s manufacturing department.</td></tr><tr><td colspan="2">Technological agents</td></tr><tr><td>PHS</td><td>PHS stands for “phone agent.” It carries out the communication task through public phone line.</td></tr><tr><td>MAIL</td><td>MAIL stands for “mail agent.” Mail agent delivers physical mail and packages.</td></tr><tr><td>TRAV</td><td>TRAV stands for “travel agent.” Travel agent moves people from one place to another to establish face-to-face communication.</td></tr><tr><td>EMAIL</td><td>EMAIL stands for “e-mail agent.” An e-mail agent is a general representation of “narrow-bandwidth” internet communication technologies (such as e-mail and FTP).</td></tr><tr><td>TCONF</td><td>TCONF stands for “teleconference.” It is a general representation of “broad-bandwidth” Internet communication technologies.</td></tr><tr><td>3RDS</td><td>3RDS stands for “third-party service.” 3RDS agents represent Internet-based business service such as transaction handling and payment tracking.</td></tr></table>

Our simulation model uses a <sup>b</sup>message pool<sup>Q</sup> mechanism to simulate the real world communication process. The process of message exchange through technology can be best described using an example (see Fig. 6). Let us assume that a PRJT agent (PRJT n) in Fig. 5 needs to talk to the ENGT agent over the phone. The process is described as follows. First, at

![](/api/attachments/4HR5GPP6/fulltext/images/5776d7121906d1e534be8d9dcf441a0dd102abf9a9389b83e07b074399337ddb.jpg)  
Fig. 5. Component structure model for CMT International Inc.

![](/api/attachments/4HR5GPP6/fulltext/images/0803db22a77480f3c2cd7723731f7cd93884746f0036d0a57d0be76509bf19d4.jpg)  
Fig. 6. A message pool communication example.

time t in the simulation run, PRJT n creates a message containing message source (the PRJT n agent), message destination (the ENGT agent) and message carrier (the PHS agent). This message is added to the message pool. At time t + 1, the PHS agent scans the message pool and identifies any message that needs to be processed. The PHS agent picks up the message from the message pool and generates a random number, <sup>b</sup>L<sup>Q</sup>, to represent the length of a phone call. Then, the PHS agent holds the message for <sup>b</sup>L<sup>Q</sup> units of time. At time t + L + 1, the PHS agent releases the message to the ENGT agent. Finally, the ENGT agent picks up the message released by PHS agent at time t +L + 2 and the whole phone conversation is completed. This <sup>b</sup>message pool<sup>Q</sup> simulation process is also known as session-mediated negotiation (SMN) in the literature [41]. SMN can be used to simulate both synchronous as well as asynchronous communication [41].

An essential component in building a simulated world (the virtual universe where agents can interact) is the time-advancing mechanism. This study uses minutes as the smallest time measurement unit because the smallest unit used to calculate cost is minutes (as used in a phone bill). All time measures smaller than a minute are rounded to the nearest minute.

## 5. Simulation experiment design

## 5.1. Dependent variables

Based on the research model, the following four dependent (performance) variables are specifically defined.

PC = Total coordination cost for a project (Project Cost, defined as an attribute in PRJT agent).

PT = Total time used for coordination for a project (Project Elapsed Time, defined as an attribute in the PRJT agent).

SC = Total coordination cost assigned to a supplier in a period of time (Supplier Cost, a summation of cost reported from all participating technology agents).

ST = Total coordination time required for a supplier during the time interval of interest (Supplier’s Total Coordination Time, a summation of all project elapse times that can be attributed to the supplier).

## 5.2. Independent variables

Based on the specifics of our study, two types of independent variables were considered. They are the type of ICT technology selected and system design configuration. On the selection of ICT, two dimensions were considered relevant: the bandwidth of Internet connection and the use of third-party support.

As for the ICT-enabled system changes, we derived two different system designs from our propositions. The first design assumed that ICT was used only as a replacement for older technologies. In other words, the first configuration did not change the existing coordination process. The two important components in system configuration, the task precedence relationship and responsibility assignment (see Fig. 3), remained the same. The second design was a reengineered system process. Theoretically, reengineered design could refer to any possible change in task precedence and responsibility assignment. It is difficult to enumerate every possible way of reengineering a system. In addition, identifying an optimal reengineering design is also a near impossible task. Therefore, for the purpose of choosing a reengineered system design for comparison, we focused on a process design based on functional outsourcing. Functional outsourcing is a common manufacturing strategy in the plastic-tooling industry with the basic idea of maintaining competitiveness by focusing on a firm’s core operation [16]. All non-core operations are either eliminated or sub-contracted to a third-party service. Based on this concept, the reengineered system design was defined as an ICT-enabled new process design (compared to the system before using ICT) that replaced all possible transportation tasks and structured communication tasks (that is, transaction handling tasks such as tracking payment).

To reiterate the independent variables defined above, a list is provided here.

1. ICT Bandwidth (Narrow or Broad): The bandwidth used for ICT application.

2. Third-Party Service (With or Without): If any thirdparty service was used.

3. Process Changes (Minimal or Reengineered): ICTenabled process change could be minimal (Simple Replacement) or involve major process changes (Reengineered Processes).

To study the main effects and interactions between the four dependent variables and three independent variables, we used a modified three-way $( 2 \times 2 \times 2 )$ factorial design. The factorial design is laid out in Table 3. The values of the four dependent variables for each simulation run are represented using four subscripts in the form of $\mathrm { P C } _ { i j k m } , \ \mathrm { P T } _ { i j k m } ,$ $\mathrm { S C } _ { i j k m } ,$ , and $\mathrm { S T } _ { i j k m }$ . The details of each subscript are given below.

i =0, 1, 2 where 0= No-ICT, 1=Narrow-Bandwidth, 2=Broad-Bandwidth  
Table 3  
Experimental design

<table><tr><td></td><td>No ICT related system change (NC)</td><td>Simple “Replacement” system design (REP)</td><td>Reengineered system design (REN)</td></tr><tr><td>No ICT (NI)</td><td> $PC_{000m}$ ,  $PT_{000m}$ , $SC_{000m}$ ,  $ST_{000m}$ </td><td>N/A</td><td>N/A</td></tr><tr><td rowspan="2">Narrow–Bandwidth wo/3rd party service (LO)</td><td rowspan="2">N/A</td><td> $PC_{111m}$ ,  $PT_{111m}$ </td><td> $PC_{112m}$ ,  $PT_{112m}$ </td></tr><tr><td> $SC_{111m}$ ,  $ST_{111m}$ </td><td> $SC_{112m}$ ,  $ST_{112m}$ </td></tr><tr><td rowspan="2">Narrow–Bandwidth w/3rd party service (LW)</td><td rowspan="2">N/A</td><td> $PC_{121m}$ ,  $PT_{121m}$ </td><td> $PC_{122m}$ ,  $PT_{122m}$ </td></tr><tr><td> $SC_{121m}$ ,  $ST_{121m}$ </td><td> $SC_{122m}$ ,  $ST_{122m}$ </td></tr><tr><td rowspan="2">Broad–Bandwidth wo/3rd party service (HO)</td><td rowspan="2">N/A</td><td> $PC_{211m}$ ,  $PT_{211m}$ </td><td> $PC_{212m}$ ,  $PT_{212m}$ </td></tr><tr><td> $SC_{211m}$ ,  $ST_{211m}$ </td><td> $SC_{212m}$ ,  $ST_{212m}$ </td></tr><tr><td rowspan="2">Broad–Bandwidth w/3rd party service (HW)</td><td rowspan="2">N/A</td><td> $PC_{221m}$ ,  $PT_{221m}$ </td><td> $PC_{222m}$ ,  $PT_{222m}$ </td></tr><tr><td> $SC_{221m}$ ,  $ST_{221m}$ </td><td> $SC_{222m}$ ,  $ST_{222m}$ </td></tr></table>

H<sub>0</sub>.

sab = interaction effect among the three factors.

$$
k = 0, 1, 2
$$

$$
m = 1, 2, \dots , n
$$

In Table 3, No-System-Change and No-ICT represents the case where no ICT technology was used to design the coordination system. It is used as a baseline for comparison to assess the effects of ICT over other communication technologies.

Each of these four outcomes or performance variables can be written as a linear statistical model.

$$
\begin{array}{r l} & {\mathrm{PC} _ {i j k m} = \mu_ {P C} + \tau_ {\mathrm{PC} i} + \alpha_ {\mathrm{PC} j} + \beta_ {\mathrm{PC} k} + (\tau \alpha) _ {\mathrm{PC} i j}} \\ & {\qquad + (\tau \beta) _ {\mathrm{PC} i k} + (\alpha \beta) _ {\mathrm{PC} j k} + (\tau \alpha \beta) _ {\mathrm{PC} i j k} + \varepsilon_ {\mathrm{PC} i j k m}} \\ & {\mathrm{PT} _ {i j k m} = \mu_ {\mathrm{PT}} + \tau_ {\mathrm{PT} i} + \alpha_ {\mathrm{PT} j} + \beta_ {\mathrm{PT} k} + (\tau \alpha) _ {\mathrm{PT} i j}} \\ & {\qquad + (\tau \beta) _ {\mathrm{PT} i k} + (\alpha \beta) _ {\mathrm{PT} j k} + (\tau \alpha \beta) _ {\mathrm{PT} i j k} + \varepsilon_ {\mathrm{PT} i j k m}} \\ & {\mathrm{SC} _ {i j k m} = \mu_ {\mathrm{PC}} + \tau_ {\mathrm{SC} i} + \alpha_ {\mathrm{SC} j} + \beta_ {\mathrm{SC} k} + (\tau \alpha) _ {\mathrm{SC} i j}} \\ & {\qquad + (\tau \beta) _ {\mathrm{SC} i k} + (\alpha \beta) _ {\mathrm{SC} j k} + (\tau \alpha \beta) _ {\mathrm{SC} i j k} + \varepsilon_ {\mathrm{SC} i j k m}} \\ & {\mathrm{ST} _ {i j k m} = \mu_ {\mathrm{ST}} + \tau_ {\mathrm{ST} i} + \alpha_ {\mathrm{ST} j} + \beta_ {\mathrm{ST} k} + (\tau \alpha) _ {\mathrm{ST} i j}} \\ & {\qquad + (\tau \beta) _ {\mathrm{ST} i k} + (\alpha \beta) _ {\mathrm{ST} j k} + (\tau \alpha \beta) _ {\mathrm{ST} i j k} + \varepsilon_ {\mathrm{ST} i j k m}} \end{array}
$$

where

l = mean value for all observations.

s = main effect for the first factor (type of ICT).

a = main effect for the second factor (use of third-party service).

b = main effect for the third factor (system design).

sa = interaction effect between the first and the second factors.

sb = interaction effect between the first and the third factors.

e = random error.

## 5.3. Hypotheses and hypotheses testing

The hypotheses to be tested can be divided into two parts. The first part relates to the mean value comparison between the baseline case and every other non-empty cell in Table 3. That is, we expect that at least one type of ICT use would likely have an impact on coordination system performance. In math-

ematical terms, this set of null hypotheses can be written as

<table><tr><td> $H_{0}.$ </td></tr><tr><td> $\mu_{PC000} = \mu_{PC_{ijk}}$ </td></tr><tr><td> $\mu_{PT000} = \mu_{PT_{ijk}}$ </td></tr><tr><td> $\mu_{SC000} = \mu_{SCijk}$ </td></tr><tr><td> $\mu_{ST000} = \mu_{STijk}$ </td></tr><tr><td>for every  $i, j$ , and  $k$ .</td></tr></table>

The second set of hypotheses relates to the effects of the different factors and their interactions. That is, we want to know if there are any significant main effects or interaction effects for the three treatments. In mathematical terms, the relevant null hypotheses can be written as

<table><tr><td> $\tau_{PCi}=0$  for all  $j,k$ </td><td> $(\tau\alpha)_{PCij}=0$  for all  $k$ </td></tr><tr><td> $\tau_{PTi}=0$  for all  $j,k$ </td><td> $(\tau\alpha)_{PTij}=0$  for all  $k$ </td></tr><tr><td> $\tau_{SCi}=0$  for all  $j,k$ </td><td> $(\tau\alpha)_{SCij}=0$  for all  $k$ </td></tr><tr><td> $\tau_{STi}=0$  for all  $j,k$ </td><td> $(\tau\alpha)_{STij}=0$  for all  $k$ </td></tr><tr><td> $\alpha_{PCj}=0$  for all  $i,k$ </td><td> $(\tau\beta)_{PCik}=0$  for all  $j$ </td></tr><tr><td> $\alpha_{PTj}=0$  for all  $i,k$ </td><td> $(\tau\beta)_{PTik}=0$  for all  $j$ </td></tr><tr><td> $\alpha_{SCj}=0$  for all  $i,k$ </td><td> $(\tau\beta)_{SCik}=0$  for all  $j$ </td></tr><tr><td> $\alpha_{STj}=0$  for all  $i,k$ </td><td> $(\tau\beta)_{STik}=0$  for all  $j$ </td></tr><tr><td> $\beta_{PCk}=0$  for all  $i,j$ </td><td> $(\alpha\beta)_{PCjk}=0$  for all  $i$ </td></tr><tr><td> $\beta_{PTk}=0$  for all  $i,j$ </td><td> $(\alpha\beta)_{PCjk}=0$  for all  $i$ </td></tr><tr><td> $\beta_{SCk}=0$  for all  $i,j$ </td><td> $(\alpha\beta)_{PCjk}=0$  for all  $i$ </td></tr><tr><td> $\beta_{STk}=0$  for all  $i,j$ </td><td> $(\alpha\beta)_{PCjk}=0$  for all  $i$ </td></tr><tr><td> $(\tau\alpha\beta)_{PCijk}=0$ </td><td> $(\tau\alpha\beta)_{SCijk}=0$ </td></tr><tr><td> $(\tau\alpha\beta)_{PTijk}=0$ </td><td> $(\tau\alpha\beta)_{STijk}=0$ </td></tr></table>

Hypotheses testing were performed in two phases. The first phase examined the difference between No-ICT and all other cells in Table 3 except for the shaded cells. A t-test for group mean comparison was adequate for this purpose. In the second phase, an analysis of variance (ANOVA) for a three-way factorial design was conducted.

## 5.4. Treatment manipulation

From the hypotheses developed in Table 3, we know that there are nine different coordination systems to be compared. Referring to Fig. 5, different treatment combinations for each cell were manipulated through different compositions of available technology agents.

Table 4 presents how the independent variables were manipulated through adding or subtracting both technology and supplier agents from the baseline (0,0,0) model. When <sup>b</sup>EMAIL<sup>Q</sup> agent is used, narrowbandwidth Internet technology is available and is used to replace traditional phone and mail communication whenever possible. When <sup>b</sup>TCONF<sup>Q</sup> agent is used, broad-bandwidth Internet technology is available and is used to replace face-to-face communication whenever possible. When <sup>b</sup>3RDS<sup>Q</sup> agent is used, a third-party payment tracking service is available. Thus, the payment tracking tasks performed by the accounting department (ACCT) is replaced. Note that cell (1,1,2) and cell (2,1,2) are left blank. These two cells represent the <sup>b</sup>reengineering<sup>Q</sup> (or second-order) effects triggered by the technologies. We assume that only one reengineered process (replacing the payment tracking tasks with a third-party service) is to be tested. Since this reengineering effect has no relationship with the <sup>b</sup>bandwidth effect,<sup>Q</sup> Cell (1,1,2) and Cell (2,1,2) are not feasible cells. In other words, we only tested reengineering effects triggered by adopting third-party Internet service in this paper.

## 5.5. Additional analyses

In addition to the hypotheses listed above, the trade-offs between time and cost, as well as between supplier performance and project performance were also considered worthwhile investigating. In fact, we suspect there is a strong (maybe negative) correlation between cost and time. To identify such a relationship, a correlation matrix was generated for all dependent variables within each cell of Table 3.

Table 4  
Treatment manipulation used in simulation experiment

<table><tr><td>Cell #</td><td>Available technology agents</td><td>Available supplier agents</td></tr><tr><td>0,0,0</td><td>PHS, MAIL, TRAV</td><td>ENGT, ACCT, MFGD</td></tr><tr><td>1,1,1</td><td>PHS, MAIL, TRAV, EMAIL</td><td>ENGT, ACCT, MFGD</td></tr><tr><td>1,2,1</td><td>PHS, MAIL, TRAV, EMAIL, 3RDS</td><td>ENGT, ACCT, MFGD</td></tr><tr><td>2,1,1</td><td>PHS, MAIL, TRAV, EMAIL, TCONF</td><td>ENGT, ACCT, MFGD</td></tr><tr><td>2,2,1</td><td>PHS, MAIL, TRAV, EMAIL, TCONF, 3RDS</td><td>ENGT, ACCT, MFGD</td></tr><tr><td>1,1,2</td><td>N/A</td><td>N/A</td></tr><tr><td>1,2,2</td><td>PHS, MAIL, TRAV, EMAIL, 3RDS</td><td>ENGT, MFGD</td></tr><tr><td>2,1,2</td><td>N/A</td><td>N/A</td></tr><tr><td>2,2,2</td><td>PHS, MAIL, TRAV, EMAIL, TCONF, 3RDS</td><td>ENGT, MFGD</td></tr></table>

Sensitivity analyses were conducted to provide more insights of the simulated systems. We conducted our sensitivity analysis on the utilization factor. The utilization factor was manipulated through the mix of available technologies. During the coordination process, the utilization of a particular technology was determined by a predefined probability (based on data collected empirically from the case).

## 6. Model verification

Any simulation model for system evaluation requires certain techniques to (1) validate, (2) authenticate, and (3) collate time series data [20,21, 33,38]. Validation implies that the model adequately represents the <sup>b</sup>real world<sup>Q</sup> situation; authentication denotes the establishment of a measure of confidence in a single set of model results; collation connotes a critical comparison of two or more sets of model outputs. In general, the authentication and collation problems can be described as the level of simulator’s trust in a model’s behavior. The validation of a simulation model, on the other hand, involves using external evidence to prove the model as being a <sup>b</sup>true<sup>Q</sup> representation of reality [20]. Based on the fact that the simulation model in this study was to mimic real world problems, a classic step-bystep empirical validation procedure suggested by Naylor and Finger [33] was considered most appropriate to verify the model’s authentication and collation. However, the empirical validation process is usually not enough to establish a model to be valid [20]. To overcome the weakness of classical empirical methods in validating simulation models, Howson and Urbach [17] suggested that building a simulation model through a real world case could strengthen its validity. We adopted both Naylor and Finger and Howson and Urbach’s suggestions and designed the following three-step procedure to verify the multi-agent model.

1. Verification during problem formulation and model building: The verification is built-in when the simulation is designed. Our simulation model is based on McGrath and Hollingshead’s research framework [29]. The use of a theoretical framework provides the basic level of verification.

2. Verification during code generation: Agents behave by way of generating and receiving messages. Each agent in a multi-agent model is designed to respond to a list of predefined messages and generate a specific set of messages (triggered by either certain events or by time). A random message generator was used to test each agent by feeding predefined messages. Reactions of each agent were tested statistically to ensure that the model behaved as per design. We tested our agents’ behavior for normality, stationarity, and randomness. Different combinations of initial conditions were also tested.

3. Verification through empirical data: We used CMT International, Inc. as our verification case. Half of the operational data collected from CMT was used for building the simulation model. The other half was used for verification. Our comparison results showed that our simulation model could successfully predict project elapse time for CMT International.

## 7. Conducting the experiment

## 7.1. Choice of sample size

We adopted Montgomery’s [31] suggestion and used the Confidence Interval Estimation Method to determine sample size. From our calculations, we determined that we needed at least 50 completed projects and 50 runs of 1-year duration for each cell to generate the required observations. Therefore, the simulation programs were set to run 50 times for each cell in the experiment over the duration of 1 year to generate enough observations for generating SC.

Table 5  
Two-tail t-test results for PT comparison with baseline case (0,0,0)

<table><tr><td></td><td>(1,1,1)</td><td>(1,2,1)</td><td>(1,2,2)</td><td>(2,1,1)</td><td>(2,2,1)</td><td>(2,2,2)</td></tr><tr><td>df</td><td>98</td><td>98</td><td>98</td><td>98</td><td>98</td><td>98</td></tr><tr><td>t statistic</td><td>1.971</td><td>4.28*</td><td>4.47*</td><td>2.41*</td><td>3.55*</td><td>5.44**</td></tr><tr><td>p-value</td><td>0.051</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.00</td><td>0.00</td></tr></table>

\* Significant at 0.05 level.  
\*\* Significant at 0.01 level.

Table 6  
Two-tail t-test results for PC comparison with baseline case (0,0,0)

<table><tr><td></td><td>(1,1,1)</td><td>(1,2,1)</td><td>(1,2,2)</td><td>(2,1,1)</td><td>(2,2,1)</td><td>(2,2,2)</td></tr><tr><td>df</td><td>98</td><td>98</td><td>98</td><td>98</td><td>98</td><td>98</td></tr><tr><td>t statistic</td><td>1.039</td><td>0.856</td><td>-3.2*</td><td>-0.95</td><td>0.29</td><td>-0.03</td></tr><tr><td>p-value</td><td>0.30</td><td>0.393</td><td>0.00</td><td>0.34</td><td>0.77</td><td>0.97</td></tr></table>

\* Significant at 0.05 level.

Then, 50 projects were randomly selected from about 1500 completed projects for each cell as the observations to be tested.

## 8. Experiment results

8.1. Hypothesis testing: comparing with the baseline case

Simple t-tests (two-tailed) were used for the first phase of hypothesis testing. The first-phase of hypothesis testing compared the baseline case and every other non-empty cell in the experiment. We expected at least one pair of the comparisons to generate significant results. That is, at least one technological factor would impact the performance of the coordination system. Tables 5–8 summarize the t-test results.

The across-the-board significant results in Table 5 suggest that the use of any combination of ICT technologies does improve the average project completion time (PT). Also, the supplier’s time used in communication (ST) decreases by adopting third-party transaction support, reengineering process or a combination of both (Table 7). However, the use of Internet connection (both broad-bandwidth and narrow-bandwidth) without third-party support may not produce significant time saving. On the other hand, we found in Table 8 that the use of ICT does not reduce the coordination cost for average projects compared to traditional communication technology (i.e. public telephone systems). Although we used two-tailed t-tests that do not suggest any direction, the negative numbers still indicate that the use of certain combinations of ICT actually <sup>b</sup>increases<sup>Q</sup> the coordination cost. However, it seems that the use of broad-bandwidth Internet connection combined with certain reengineering effect may reduce the supplier’s communication cost in the long run (Table 8). To sum up the results from the first phase analysis, the use of ICT should be able to save time by improving coordination between customers and the supplier. Nonetheless, the supplier may not benefit from the low-cost communication provided by ICT.

Table 7  
Two-tail t-test results for ST comparison with baseline case (0,0,0)

<table><tr><td></td><td>(1,1,1)</td><td>(1,2,1)</td><td>(1,2,2)</td><td>(2,1,1)</td><td>(2,2,1)</td><td>(2,2,2)</td></tr><tr><td>df</td><td>98</td><td>98</td><td>98</td><td>98</td><td>98</td><td>98</td></tr><tr><td>t statistic</td><td>0.708</td><td>2.83*</td><td>5.12*</td><td>1.51</td><td>9.3*</td><td>9.4*</td></tr><tr><td>p-value</td><td>0.48</td><td>0.00</td><td>0.00</td><td>0.13</td><td>0.00</td><td>0.00</td></tr></table>

\* Significant at 0.05 level.

Table 8  
Two-tail t-test results for SC comparison with baseline case (0,0,0)  
Table 10

<table><tr><td></td><td>(1,1,1)</td><td>(1,2,1)</td><td>(1,2,2)</td><td>(2,1,1)</td><td>(2,2,1)</td><td>(2,2,2)</td></tr><tr><td>df</td><td>98</td><td>98</td><td>98</td><td>98</td><td>98</td><td>98</td></tr><tr><td>t statistic</td><td>1.703</td><td>3.56*</td><td>1.38</td><td>3.6*</td><td>2.35*</td><td>1.79</td></tr><tr><td>p-value</td><td>0.09</td><td>0.00</td><td>0.16</td><td>0.00</td><td>0.02</td><td>0.07</td></tr></table>

\* Significant at 0.05 level.

## 8.2. Hypothesis testing: technological effects

The second phase of hypothesis testing was to examine the three technological effects and their interaction effects. Considering the missing cells in this study, the original $2 ^ { 3 }$ factorial design was reduced into two $\dot { 2 } ^ { 2 }$ full factorial designs. The two resulting experiments are called two one-half fractions of the $2 ^ { 3 }$ design [31]. Tables 9 and 10 present the two fractions of the original design.

Table 9 describes the first half of the experiment. Using this design, the main effects and interaction effects generated by both Internet bandwidth and third-party support can be analyzed. Table 10 describes the second half of the experiment. Using the technique of fractional factorial design, one has to assume that high-order interactions are negligible.

Table 9  
The first fraction of the original experiment design (no reengineering effect)

<table><tr><td></td><td>No 3rd-party support</td><td>With 3rd-party support</td></tr><tr><td>Narrow-bandwidth</td><td> $PC_{111m}$ ,  $PT_{111m}$ , $SC_{111m}$ ,  $ST_{111m}$ </td><td> $PC_{121m}$ ,  $PT_{121m}$ , $SC_{121m}$ ,  $ST_{121m}$ </td></tr><tr><td>Broad-bandwidth</td><td> $PC_{211m}$ ,  $PT_{211m}$ , $SC_{211m}$ ,  $ST_{211m}$ </td><td> $PC_{221m}$ ,  $PT_{221m}$ , $SC_{221m}$ ,  $ST_{221m}$ </td></tr></table>

The second fraction of the original experiment design (no thirdparty support effect)

<table><tr><td></td><td>No process change(replacement)</td><td>Process change(reengineering)</td></tr><tr><td>Narrow-bandwidth</td><td> $\text{PC}_{121m}, \text{PT}_{121m},$  $\text{SC}_{121m}, \text{ST}_{111m}$ </td><td> $\text{PC}_{122m}, \text{PT}_{122m},$  $\text{SC}_{122m}, \text{ST}_{122m}$ </td></tr><tr><td>Broad-bandwidth</td><td> $\text{PC}_{221m}, \text{PT}_{221m},$  $\text{SC}_{221m}, \text{ST}_{221m}$ </td><td> $\text{PC}_{222m}, \text{PT}_{222m},$  $\text{SC}_{222m}, \text{ST}_{222m}$ </td></tr></table>

In other words, we have to sacrifice the explanatory power of a complete random design to obtain more reliable results for easier interpretation. Any interactions involving both the reengineering <sup>b</sup> treatment<sup>Q</sup> and the third-party support <sup>b</sup>treatment<sup>Q</sup> were ignored.

To conduct the two-part experiment using our simulation model, an additional 50 simulation runs were conducted to generate enough replications for the overlapped portion of the experimental design. That ${ \mathrm { i s } } ,$ cell (1,2,1) and cell (2,2,1) were simulated 100 times for 1-year durations. To analyze the results, eight two-way ANOVA tests were conducted (the ANOVA tables and detailed interpretation is available from the authors). By examining the significant results from our ANOVA analysis, we have the following observations.

<sup>!</sup> The adoption of a third-party Internet transaction service was likely to reduce the average project completion time (PT) for CMT under its current project management process. Calculated from the average numbers in Table 1, the saving was about 11 working days per project.

<sup>!</sup> The adoption of a third-party Internet transaction service was likely to reduce the time used for coordination (ST) in CMT. The saving was about 15 working days.

<sup>!</sup> The adoption of broad-bandwidth Internet connection reduced the time used for project coordination in CMT. The average saving was about 9 working days per project.

<sup>!</sup> The adoption of both the third-party Internet transaction service and broad-bandwidth technology significantly improved CMT’s coordination performance by reducing the time used in coordination. The additional saving from the reengineering effect was about 5 working days per project.

<sup>!</sup> As seen in Fig. 7, the significant interaction effect indicates that the use of a third-party transaction service may have had a synergetic effect in reducing coordination time when used with broad-bandwidth technology.

<sup>!</sup> Process reengineering triggered by the adoption of third-party Internet transaction service could had a significant impact on CMT’s coordination performance. However, the interaction effects between the reengineering process and the adoption of broad-bandwidth were not clear.

<sup>!</sup> The cost of coordination increased significantly if both broad-bandwidth Internet connection and a third-party transaction service were adopted. The average increase was hard to tease out from the ANOVA results.

<sup>!</sup> The adoption of third-party transaction service may reduce the time required for coordination but would increase the overall coordination cost for CMT. The cost increase is about \$3700 per year.

## 8.3. Sensitivity and other analysis

Sensitivity analysis in this study focused on the utilization factor. Also, sensitivity analysis only makes sense when the main experiment has significant results. Therefore, the sensitivity analysis was done only on the time-based performance measures (PT and ST). In addition to analyzing the utilization factor, a correlation analysis was also performed to identify possible relationships among dependent variables. However, no significant results were found in the correlation analysis.

Utilization analysis for cell (1,2,1), t-test, assuming equal means between two samples: baseline case and cell (1,2,1)

<table><tr><td></td><td>Utilization (%)</td><td>df</td><td>Mean (min)</td><td>t-statistic</td><td>p-value</td></tr><tr><td rowspan="6">PT—project elapsed time</td><td>100</td><td>98</td><td>34449.91</td><td>4.28*</td><td>0.00</td></tr><tr><td>95</td><td>98</td><td>33521.21</td><td>5.1*</td><td>0.00</td></tr><tr><td>90</td><td>98</td><td>39782.34</td><td>2.78*</td><td>0.00</td></tr><tr><td>85</td><td>98</td><td>42009.00</td><td>2.01*</td><td>0.00</td></tr><tr><td>80</td><td>98</td><td>46523.08</td><td>1.75</td><td>0.103</td></tr><tr><td>75</td><td>98</td><td>45395.75</td><td>1.79</td><td>0.087</td></tr><tr><td rowspan="6">ST—supplier&#x27;s coordination time</td><td>100</td><td>98</td><td>16264.72</td><td>2.83*</td><td>0.00</td></tr><tr><td>95</td><td>98</td><td>15789.61</td><td>2.95*</td><td>0.00</td></tr><tr><td>90</td><td>98</td><td>17982.06</td><td>1.99*</td><td>0.01</td></tr><tr><td>85</td><td>98</td><td>22136.66</td><td>1.78</td><td>0.09</td></tr><tr><td>80</td><td>98</td><td>21395.95</td><td>1.98*</td><td>0.04</td></tr><tr><td>75</td><td>98</td><td>23001.84</td><td>0.96</td><td>0.33</td></tr></table>

\* Significant at 0.05 level.

## 8.4. The utilization factor

In this study, sensitivity analysis could have been conducted for both phases of hypothesis testing: phase one, the comparison between each cell with the baseline case and phase two, the ANOVA analysis on the two fractional experiments. However, the interpretation of sensitivity analysis for the second phase would have been difficult due to the fact that utilization factors in these experimental setups contain complicated interaction effects. Therefore, testing on the utilization factor was performed only for phase one.

In the CMT case, the utilization of three different technologies was of interest. They are: the use of Email (narrow-bandwidth), the use of third-party service, and the use of teleconferencing technology (broad-bandwidth). However, the t-test that compared cell (1,1,1) with the baseline case did not generate any significant results (see Table 5). Therefore, the sensitivity analysis was conducted only on the use of third-party service (1,2,1) and the use of broad-bandwidth Internet connection (2,1,1). The common assumption for the two sensitivity analyses was that the E-mail function was fully utilized in both situations.

![](/api/attachments/4HR5GPP6/fulltext/images/ff26d66b8866b066bb617a5dba86906b0c28c09ff587925c4ccb055d72aaf158.jpg)  
Fig. 7. The interaction effect between Internet bandwidth and the use of third-party service on ST.

The utilization of an ICT was manipulated by adjusting the probability of an agent choosing a particular message <sup>b</sup>carrier.<sup>Q</sup> In the original experiment setup, all utilization probability was set to 100%. In other words, once a technology exists in the simulation model, it was available to other agents all the time. In this analysis, we changed the utilization probability in decrements of 5%. For every utilization level, the program was set to run 50 times for 1-year duration. Then, 50 completed projects were selected from the data set for examining differences using ttests. The sensitivity analysis for the two cells generated two tables (Tables 11 and 12) listing the relationships between utilization level and test statistics.

For cell (1,2,1), where the third-party transaction service is used, t-test results dropped out of significance between 80% (ST in Table 11) to 85% (PT in Table 11) utilization. For cell (2,1,1), where teleconferencing technology is used, t-test results become insignificant very quickly after the utilization dropped below 90% for both PT and ST. These results indicate that the time saving effects brought upon by ICT are very sensitive to utilization, and only near-full utilization of newly adopted technology can guarantee overall performance improvement.

Table 12  
Utilization analysis for cell (2,1,1), t-test, assuming same mean value between two samples: baseline case and cell (2,1,1)

<table><tr><td></td><td>Utilization (%)</td><td>df</td><td>Mean (min)</td><td>t-statistic</td><td>p-value</td></tr><tr><td rowspan="6">PT—project elapsed time</td><td>100</td><td>98</td><td>40924.74</td><td>2.41*</td><td>0.00</td></tr><tr><td>95</td><td>98</td><td>39989.03</td><td>2.68*</td><td>0.00</td></tr><tr><td>90</td><td>98</td><td>42348.25</td><td>1.87</td><td>0.07</td></tr><tr><td>85</td><td>98</td><td>48935.38</td><td>0.70</td><td>0.49</td></tr><tr><td>80</td><td>98</td><td>46523.08</td><td>1.75</td><td>0.103</td></tr><tr><td>75</td><td>98</td><td>45395.75</td><td>1.79</td><td>0.087</td></tr><tr><td rowspan="6">ST—supplier&#x27;s coordination time</td><td>100</td><td>98</td><td>9908.66</td><td>2.83*</td><td>0.00</td></tr><tr><td>95</td><td>98</td><td>11232.75</td><td>2.95*</td><td>0.00</td></tr><tr><td>90</td><td>98</td><td>15897.31</td><td>2.06*</td><td>0.00</td></tr><tr><td>85</td><td>98</td><td>19987.85</td><td>1.77</td><td>0.101</td></tr><tr><td>80</td><td>98</td><td>21052.62</td><td>1.33</td><td>0.24</td></tr><tr><td>75</td><td>98</td><td>21282.27</td><td>0.96</td><td>0.33</td></tr></table>

## 8.5. Correlation among dependent variables

To identify possible trade-offs between time and cost, a correlation matrix was generated for every cell in the experimental design. From the eight correlation matrices and the corresponding scatter plot, we found positive relationships between PT and ST and between PC and SC in every cell. However, we did not find any noticeable relationship between PT, ST (time) and PC, SC (cost) pairs. In other word, the trade-off between time and cost was not identifiable.

## 9. Implications and conclusion

The main contribution of this paper is not the findings from our simulation experiment. It is the methodology used to conduct a multi-agent simulation study. We have described in depth three key aspects of multi-agent simulation.

1. Some important considerations in building a multiagent system are identified. These considerations include agent identification criteria, component structure design and simulation process control.

2. Explanations of how to design a simulation experiment using multi-agent systems are provided. Specifically, how treatments are manipulated in multiagent simulation is explained.

3. A verification process is proposed to verify multiagent simulation models. Our verification further assures the applicability of the multi-agent method in social system simulation.

In the particular context of our case, we find four major results from the simulation experiment. First, the use of Internet-based communication technology (ICT) can significantly shorten the time required for project coordination. However, cost saving was not significant. In some situations, the adoption of ICT had an adverse effect on cost saving. Second, technology utilization plays an important role in performance improvement. The performance gains from the technology diminish very quickly as the utilization level drops. Third, process reengineering provides additional benefits in using Internet technology. Using new technology without reconfiguring the business process may result in wasted resources. Fourth, it was found that the utilization level is a major determinant in realizing Internet technology’s time saving benefits.

A number of limitations are identified in this study. First, the simulation model is built on a case study. The results from our analysis can only be used as a decision support tool, they cannot be used to verify theories. In other words, the results cannot be generalized to other coordination systems. This, in fact, is a common limitation for any case-based simulation study [43].

Also related to the real world case is the choice of experiment design. In this study, empty cells showing up in the experiment design forced the reduction of a complete random factorial design to two onehalf fraction experiments. Two adverse effects result from this reduction. First, the explanatory power of ANOVA was reduced. High-level interactions (some two-way and the three-way interactions) among treatments (the technology factors) could not be examined. Second, additional samples needed to be collected.

Another limitation concerns the current simulation model. Many assumptions made in the simulation model were based on the then <sup>b</sup>current<sup>Q</sup> situation (year 2001). These assumptions more than likely change over time. Once these assumptions change, the experiment results might change as well. Therefore, constant correction is necessary to ensure that the simulation model can generate current, and reliable information for decision-making.

In fact, a multi-agent simulation model has the capability to overcome the limitation of changing assumptions. The solution is building more <sup>b</sup> intelligence<sup>Q</sup> into every agent. The current model allows two types of very primitive intelligence. One is that the agents have knowledge about their current status (the process intelligence). The other one is that the agents have certain decision rules (either a deterministic or probability-based) guiding their behavior (the rule-based intelligence). These agents lack the capability of learning. That is, they do not know how to modify their knowledge about process and their decision rules. In the artificial intelligent (AI)

professional’s terms, these agents possess only <sup>b</sup>beliefs<sup>Q</sup> for them to make decisions [39,40]. They do not have the <sup>b</sup>desire<sup>Q</sup> and <sup>b</sup>intention<sup>Q</sup> to scan the environment and to change their own <sup>b</sup>beliefs.<sup>Q</sup> This so called <sup>b</sup>BDI<sup>Q</sup> (belief, desire, and intention) model for building intelligent agents was not used in this simulation.

Also inherited from the multi-agent simulation approach is the question of model instability. Multiagent simulation has been demonstrated to be very sensitive to parameter changes [40,46]. Without careful control of agent’s behaviors, the simulation model can quickly turn into a chaotic system. This fact can be observed from the quick performance degradation in the sensitivity analysis. Although we have concluded that the system is very sensitive to utilization, however, knowing the characteristics of multi-agent simulation suggest that we need to be cautious in stating our conclusions.

We identified the following research directions for the future. First, although the simulation model was verified through the three-step verification process, we can provide more support by seeking external verification sources. One of the common practices in verifying multi-agent simulation models is building an equivalent equation-based model. If the agents in the multi-agent simulation model do not possess a highlevel of intelligence, the simulation model can be duplicated using an equation-based model [40,46]. Comparing the results generated from the equationbased model with the multi-agent model would give us more confidence in our model. Similarly model instability issues can be addressed.

Second, the same simulation model can be applied to other cases in different industries. Replicated case studies and similar findings could give us some basis for theory verification. Therefore, extending the experiment to at least one other tooling/equipment supply chain is suggested.

Third, the experiment design provides comparison for only eight different technology configurations. In the real world, the process variations resulting from new technologies are typically more complicated. Applying the same simulation model to different experiment designs is also a feasible future research project.

Finally, we only considered one contextual factor in this study. Many contextual factors such as partnership quality, Internet stability, project types, etc., are all important factors in determining coordination performance. Close examination of these factors, either empirically or through simulation, can provide fruitful research opportunities.

## References

[1] M. Alavi, D.E. Leidner, Review: knowledge management and knowledge management systems: conceptual foundations and research issues, MIS Quarterly 25 (1) (2001) 107 – 136.

[2] C. Antonelli, Investment, productivity growth and key-technologies: the case of advanced telecommunications, Manchester School of Economic and Social Studies 61 (4) (1993) 386– 398.

[3] A.B. Badiru, Project Management in Manufacturing and High Technology Operations, John Wiley and Sons, New York, 1988.

[4] J. Ballantine, M. Bonner, M. Levy, A. Martin, The 3-D model of information systems success: the search for the dependent variable continues, Information Resources Management Journal 9 (4) (1996) 5– 15.

[5] A.H. Bond, L. Gasser, An Analysis of Problems and Research in DAI. Readings in Distributed Artificial Intelligence, Morgan Kaufman, San Mateo, CA, 1988.

[6] E. Brynjolfsson, L.M. Hitt, Beyond the productivity Paradox, Communications of the ACM 41 (8) (1998) 49– 55.

[7] K. Burke, L. Chidambaram, How much bandwidth is enough? A longitudinal examination of media characteristics and group outcomes, MIS Quarterly 23 (4) (1999) 79–112.

[8] P. Coad, E. Yourdon, Object-Oriented Design, Yourdon Press, Englewood Cliffs, NJ, 1991.

[9] R. Conte, N. Gilbert, S. Sichman, MAS and social simulation: a suitable commitment, Conference Proceedings, Multi-agent Systems and Agent Based Simulation, First International Workshop MABS ’98, Paris, France, 1998.

[10] R.L. Daft, R.H. Lengel, Organizational information requirements, media richness, and structure design, Management Science 32 (5) (1986) 554–571.

[11] W.H. DeLone, Determinants of success for computer usage in small business, MIS Quarterly 12 (1) (1998) 51 – 62.

[12] W.H. DeLone, E.R. McLean, Information system success: the quest for the dependent variable, Information System Research 3 (2) (1992) 157– 179.

[13] S. Dewan, L. Kennneth, International dimensions of the productivity paradox, Communications of the ACM 41 (8) (1998) 56–62.

[14] V. Grover, M.J. Cheon, J.T.C. Teng, The effect of service quality and partnership on the outsourcing of information systems functions, Journal of Management Information Systems 12 (4) (1996) 89– 116.

[15] V. Grover, J. Teng, A.H. Segars, K. Fiedler, The influence of information technology diffusion and business process change on perceived productivity: the IS executive’s perspective, Information & Management 3 (1998) 141– 159.

[16] T. Hill, Manufacturing Strategy: Text and Cases, 3rd ed., McGraw-Hill/Irwin, 1999.

[17] C. Howson, P. Urbach, Scientific Reasoning: The Bayesian Approach, Open Court, La Salle, IL, USA, 1989.

[18] S.S. Kahai, R.B. Cooper, The effect of computer-mediated communication on agreement and acceptance, Journal of Management Information Systems 1 (1999) 165– 188.

[19] D. Kinny, M. Georgeff, A. Rao, A methodology and modeling technique for systems of BDI agents, Presented at Agent Breaking Away: 7th European Workshop on Modeling Autonomous Agents in a Multi-Agent World, MAAMAW ’96, Einhoven, The Netherlands, 1996.

[20] G.B. Kleindorfer, L. O’Neill, R. Ganeshan, Validation in simulation: various positions in the philosophy of science, Management Science 44 (8) (1998) 1087 – 1099.

[21] A.M. Law, W.D. Kelton, Simulation Modeling, 2nd ed., McGraw Hill, New York, 1991.

[22] C.S. Lee, Modeling the business value of information technology, Information and Management 39 (3) (2001) 191– 210.

[23] J.N. Lee, Y.G. Kim, Effect of partnership quality on IS outsourcing success: conceptual framework and empirical validation, Journal of Management Information Systems 15 (4) (1999) 29– 61.

[24] V.A. Mabert, M.A. Venkataramanan, Special research focus on supply chain linkages: challenges for design and management in the 21st century, Decision Sciences 29 (3) (1998) 537 – 551.

[25] K.D. Mackenzie, Processes and their framework, Management Science 46 (1) (2000) 110– 125.

[26] T.W. Malone, K. Crowston, The interdisciplinary study of coordination, ACM Computing Surveys 26 (1) (1994) 87– 95.

[27] T.W. Malone, K. Crowston, J. Lee, B. Pentland, C. Dellarocas, G. Wyner, J. Quimby, C.S. Osborn, A. Bernstein, G. Herman, M. Klein, E. O’Donnell, Tools for inventing organizations: toward a handbook of organizational processes, Management Science 45 (3) (1999) 425– 443.

[28] B. Masseti, R.W. Zmud, Measuring the extent of EDI usage in complex organizations: strategies and illustrative examples, MIS Quarterly 20 (3) (1996) 331– 345.

[29] J.E. McGrath, A.B. Hollingshead, Groups Interacting with Technology: Ideas, Evidence, Issues, and an Agenda, Sage Publication, Thousand Oaks, CA, 1994.

[30] I. McKeown, G. Philip, Business transformation, information technology and competitive strategies: learning to fly, International Journal of Information Management 23 (1) (2003) 3– 24.

[31] D.C. Montgomery, Design and Analysis of Experiments, 3rd ed., John Wiley & Sons, New York, 1991.

[32] T. Mukhopadhyay, S. Kekre, S. Kalathur, Business value of information technology: a study of electronic data interchange, MIS Quarterly 19 (2) (1995) 137– 156.

[33] T.H. Naylor, J.M. Finger, Verification of computer simulation models, Management Science 14 (1) (1967) B92 –B101.

[34] N. Ozawa, M. Fisher, The complexity of office communications, Ten-Year Forecast: Institute For The Future (IFTF), 1998, pp. 187–195.

[35] A. Pinsonneault, S. Rivard, Information technology and the nature of managerial work: from the productivity paradox to the icarus paradox? MIS Quarterly 22 (3) (1998) 287–311.

[36] J.B. Quinn, J.J. Baruch, K.A. Zien, Software-based innovation, Sloan Management Review 37 (4) (1996) 11– 20.

[37] A. Rai, S.S. Lang, R.B. Welker, Assessing the validity of IS success models: an empirical test and theoretical analysis, Information Systems Research 1 (2002) 50– 69.

[38] A. Ravindran, D.T. Phillips, J.J. Solberg, Operations Research: Principles and Practice, 2nd ed., John Wiley & Sons, 1987.

[39] J. Rouchier, F. Bousquet, Non-merchant economy and multi agent system: an analysis of structuring exchanges, Conference Proceedings, Multi-agent Systems and Agent Based Sim ulation, First International Workshop, MABS ’98, Paris, France, 1998.

[40] M. Scott, Social simulation models and reality: three approaches, in multi-agent systems and agent based simulation, Conference Proceedings, Multi-agent Systems and Agen Based Simulation, First International Workshop, MABS ’98, Paris, France, 1998.

[41] E. Steinmetz, J. Collins, S. Jamison, R. Sundareswara, Bid evaluation and selection in the magnet automated contracting system, and in agent mediated electronic commerce, Conference Proceedings, First International Workshop on Agent Mediated Electronic Trading AMET-98, Minneapolis, MN USA, 1998.

[42] J.M. Swaminathan, S.F. Smith, M. Sadeh, Information exchange in supply chains, Technical Report, CMU-RI-TR-95- 36. Pittsburgh, PA: Carnegie Mellon University, 1995.

[43] J.M. Swaminathan, F. Smith, M.N. Sadeh, Modeling supply chain dynamics: a multi-agent approach, Decision Sciences 29 (3) (1998) 607–632.

[44] R. Tadjer, Too much tech? Small Business Computing & Communications 4 (10) (1999) 58– 62.

[45] S. Tzafestas, G. Kapsiotis, Coordinated control of manufacturing/supply chain using multi-level techniques, Computer Integrated Manufacturing Systems 7 (3) (1994) 206–212.

[46] H. Van Dyke Parunak, R. Savit, R.L. Riolo, Agent-based modeling vs. equation-based modeling: a case study and users’ guide, Conference Proceedings, Multi-agent Systems and Agent Based Simulation, First International Workshop MABS ’98, Paris France, 1998.

[47] J.B. Walther, Interpersonal effects in computer mediated com munication: a relational perspective, Communication Research 19 (1) (1992) 52–90.

[48] J.B. Walther, Computer-mediated communication: impersonal, interpersonal and hyperpersonal interaction, Communication Research 23 (1) (1996) 3– 43.

[49] T.-W. Wang, S.K. Tadisina, The impact of internet communication on coordination performance in tooling projects: a literature review, Conference Proceedings, 32nd Annual Meeting of the Decision Sciences Institute, San Francisco, California USA, 2001.

[50] L.P. Willcocks, S. Lester, In search of information technology productivity: assessment issues, Journal of the Operational Research Society 48 (11) (1997) 1082 – 1094.

![](/api/attachments/4HR5GPP6/fulltext/images/776f5c8422f52d118404c6f8382e9b0d7c3d6e7294e677c4a40afa509af6f8c8.jpg)

Te-Wei Wang is an assistant professor in the Department of Decision Sciences and Information Systems at Florida International University. He received his Ph.D. in business administration from the Southern Illinois University at Carbondale. He holds a Master of Sciences in mechanical engineering from University of Missouri-Rolla. His research interests include e-commerce assurance service, information systems analysis and design, requirement engineer-

ing and enterprise resource planning. His publications can be found in several IS journals such as Journal of Database Management and Review of Business Information Systems.

![](/api/attachments/4HR5GPP6/fulltext/images/48b4b3f48ab97a241d236d9134caa953c035e7f388041adc2b8dbcd8fe701862.jpg)

Suresh K. Tadisina is an associate professor and former chairperson of the Department of Management at Southern Illinois University at Carbondale. Suresh holds a B.E. (Mech.) and an M.B.A. from Osmania University in India and an M.B.A. and Ph.D. in Quantitative Analysis and Operations Management from the University of Cincinnati. His current research interests include decision support/expert systems, management of technology, service opera-

tions management, supply chain management, and IS agility. His publications have appeared in journals such as Annals of Operations Research, Computers and Operations Research, Decision Support Systems, European Journal of Operations Research, IIE Transactions, Interfaces, Journal of the Operational Research Society, OMEGA, Project Management Journal, among others.
