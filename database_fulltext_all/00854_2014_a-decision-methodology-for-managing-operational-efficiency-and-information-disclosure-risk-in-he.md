---
otero_id: 854
otero_key: "JJUK3BBA"
title: "A decision methodology for managing operational efficiency and information disclosure risk in healthcare processes"
authors: "Xue Bai; Ram Gopal; Manuel Nunez; Dmitry Zhdanov"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.046"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision methodology for managing operational ef<sup>fi</sup>ciency and information disclosure risk in healthcare processes

Xue Bai ⁎, Ram Gopal, Manuel Nunez, Dmitry Zhdanov

Department of Operations and Information Management, School of Business, University of Connecticut, Storrs, CT 06269, USA

a r t i c l e i n f o

Available online 5 November 2012

Keywords: Information disclosure Risk Work<sup>fl</sup>ow ef<sup>fi</sup>ciency Control Healthcare processes Optimization

## a b s t r a c t

This paper addresses two critical challenges faced by healthcare organizations: signi<sup>fi</sup>cant personnel shortages and mandates to safeguard patient safety and information security. We develop a two-stage decision making methodology to optimize the healthcare work<sup>fl</sup>ow task assignments and mitigate information disclosure risks. While the <sup>fi</sup>rst stage throughput optimization formulation maximizes operational ef<sup>fi</sup>ciencies, it can expose organizations to information disclosure risks that can be exploited to violate patient safety and information security. To address the ensuing privacy and fraud concerns we de<sup>fi</sup>ne task-based con<sup>fl</sup>ict sets to assess disclosure risks with optimal task assignments. In the second stage of the solution methodology, various security control strategies – task based and employee based – are incorporated into a decision support model to help decision makers to effectively manage and achieve work<sup>fl</sup>ow ef<sup>fi</sup>ciency and meet information security requirements. For practical settings where certain parameters are not obtainable or the problem is computationally intractable, we provide a sequential-decision approach that could yield approximate partial solutions. We conduct an extensive computational analysis of a clinical work<sup>fl</sup>ow process to illustrate th practical bene<sup>fi</sup>ts of the proposed methodology.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

As healthcare costs continue to skyrocket, healthcare organizations are faced with the constant challenge of operating at reduced costs while delivering good quality of care and protecting patient privacy [1,30,31]. However, the ability of these organizations to deliver effective and ef<sup>fi</sup>cient patient care is currently hindered by two major factors: the current and growing shortage of healthcare professionals and the patient privacy concerns. On the one hand, staf<sup>fi</sup>ng shortages across healthcare job types have caused emergency department overcrowding, reduced number of staffed beds to serve patients, delayed discharge and increased length of stay for patients, and decreased staff and patient satisfaction [1]. On the other hand, organizations are mandated to comply with a plethora of rules and regulations to ensure patient privacy [30,31]. Such rules and regulations are a natural consequence of concerns about healthcare organizations that routinely collect, manage and use sensitive personal, medical, and <sup>fi</sup>nancial data on patients. While access to such data is crucial to deliver quality care and conduct clinical research, they may also be exploited for pro<sup>fi</sup>t and enable a variety of criminal activities. For example, a former UCLA employee pleaded guilty to selling medical data of celebrities to tabloids [39]. In a series of related investigations, it was discovered that records of over 1000 patients were accessed inappropriately since 2003; 165 hospital employees were disciplined. Motivations for private data snooping may go beyond mere curiosity or selling data to tabloids. By collecting pieces of information about a person, a potential attacker can create a comprehensive pro<sup>fi</sup>le of the target and use it later for identity theft, blackmail or other adverse activities.

Regulations such as HIPAA (2002) [30] and HITECH (2009) [31] require healthcare organizations to implement policies and procedures to prevent and detect security violations related to patient safety and privacy. Such initiatives are in themselves not revenue generating activities but rather an additional cost for organizations. In light of staf<sup>fi</sup>ng shortage, budget constraints, and an avalanche of evolving regulatory compliance requirements, healthcare organizations are driven to design and improve the operation ef<sup>fi</sup>ciency and information security in their work<sup>fl</sup>ow systems.

Despite large and diverse research on healthcare processes and information security, there is dearth of research addressing healthcare processes with the objective of achieving both the operational ef<sup>fi</sup>- ciency and meeting information security requirements. Research in healthcare informatics has focused on developing security mechanisms for electronic clinical record systems, while research in information security has focused on developing various technologies at microdata level or database access mechanisms to limit the disclosure of sensitive data [9,14–16,18,21,25,40]. One of the key challenges in the design of healthcare processes and other service-oriented environments is to achieve the goal of both providing ef<sup>fi</sup>cient care and securing privacy information adequately [38,55]. We recognize this challenge and explicitly address it in our work.

In this paper, we propose a decision methodology that minimizes the disclosure risk via a work<sup>fl</sup>ow system with optimal ef<sup>fi</sup>ciency and a viable and effective control scheme for preventing information disclosure. This methodology encompasses a two-stage optimization formulation. At the <sup>fi</sup>rst stage, it <sup>fi</sup>nds optimal staf<sup>fi</sup>ng solutions for a work<sup>fl</sup>ow, in terms of minimum throughput time. At the second stage, it then selects the best combination of task and employee control placements for each of the optimal staf<sup>fi</sup>ng assignments obtained from the <sup>fi</sup>rst stage, in terms of acceptable control cost. We show that solving the two-stage problem results in an ef<sup>fi</sup>cient and reasonably secure staff strategy. For applications where model parameterization is practically infeasible or the problem is computationally intractable, we provide a sequential-decision methodology that could yield ef<sup>fi</sup>- cient staf<sup>fi</sup>ng solutions with minimum disclosure risk. We use a clinical work<sup>fl</sup>ow process to illustrate our methodology.

## 2. Literature review

There is a general understanding that delivering quality health care is a complex endeavor which is highly dependent on utilizing information effectively [7]. Information systems that can help in medi cal and clinical decision making have been available for over three decades. While the usefulness of these systems is well understood, security concerns have been cited as one of the major barriers to their widespread adoption [36,37].

Research from health care informatics has focused on the development of sophisticated information and computer security mechanisms for electronic medical record systems (EMRS). Most commonly used technology in EMRS is the implementation of access management mechanisms such as role based access control [44]. However, role based access control has not been successful in complex environments like hospitals. As de<sup>fi</sup>ning discreet and universal access roles is extremely dif<sup>fi</sup>cult, hospital administrators rely on audit trails to detect intrusions of patient privacy [6]. Gallagher et al. [19] demonstrated one audit system for EHRs. This system partially reduced the burden on auditing personnel by giving users the ability to inspect the access data for their own record. Asaro and Ries [3] did a study to analyze the distribution of EHRs accessed by users. In this work, we provide a control strategy using the combinations of task monitoring and personnel monitoring control placements to reduce or completely prevent unauthorized data access.

The issue of providing proper information security con<sup>fi</sup>guration is a dif<sup>fi</sup>cult one, since consequences of inadequate use of information or system failure can lead to severe, if not lethal, consequences. Several approaches are proposed to deal with this issue. A general set of guidelines are listed in the NIST 800-14 publication that specify eight generally acceptable principles and fourteen common IT security practices [26]. Some of the key principles are that computer security must support the mission of the organization, be cost-effective and be constrained by societal factors. All of these are true in the healthcare work<sup>fl</sup>ow environment and serve as the foundation for our analysis. In the healthcare setting, Gritzalis [23] provides a broad approach to the security of healthcare information systems by creating a baseline security policy. This policy is built based on the information system security pro<sup>fi</sup>le including attitudes and awareness; experience; organizational environment; education and research; and mode of processing of the medical data. The healthcare <sup>fi</sup>eld may be characterized by a distributed information processing environment utilizing heterogeneous systems. It is important to understand the information <sup>fl</sup>ows and protect the data at every step of the process. Common approaches used for data protection in the healthcare <sup>fi</sup>eld include mobile agents [48,50] and middleware systems for ubiquitous data integration [41]. However, even with automated tasks, concerns over the exposure of private information still remain. Often, patient data is used in clinical research where knowledge of individual information is not essential for the research project, thus allowing for some sort of data distortion or access restriction mechanism to be enabled [9,11]. However, in the clinical work<sup>fl</sup>ow context where the individual data needs to be accessed, such solutions are not applicable. In our work, we propose a method for evaluating and mitigating information disclosure risk via placement of monitoring controls.

In this context, monitoring controls can be assigned either at the task level (all instances of data access in a speci<sup>fi</sup>c task are recorded, regardless of the employee) or at the employee level (speci<sup>fi</sup>c employees are monitored in all of their tasks). While both of these approaches are possible, they are not devoid of some problems. In case of employee monitoring, while organizations may expect bene-<sup>fi</sup>ts such as prevention of resource misuse and reduction of corporate liability due to misbehavior of its employees [2], there may also be substantial drawbacks to it. For instance, employee monitoring may have a negative impact on morale, encourage a negative management style, and even cause economic loss due to decreased productivity of employees and managers alike [2]. In addition, there is a variety of employee behaviors with regard to information security that may be hard to categorize before those become manageable [47]. These and other concerns prompt researchers to question the effectiveness of employee audit as a viable tool for behavioral compliance with information security requirements [51].

Typical task-centered controls include technical solutions such as access control, audit tools and intrusion detection systems. Access control tools are preventative solutions that are designed to stop unauthorized access and data disclosure before it happens. There are multiple solutions such as access control lists (ACL) and role-based access control (RBAC), among others (please see [49] for a detailed review). However in many cases these controls are too rigid for modern day clinical work<sup>fl</sup>ows and can be effective only in relatively simple scenarios [10]. In addition, in some circumstances, such as medical emergencies, these controls may have to be overridden, leaving open opportunities for the malicious activities.

One of the prominent ways to make RBAC useful in practice is known as role engineering [12,13,46]. The process of role engineering is essentially requirement engineering and has important concepts such as static and dynamic separation of duties. Static separation of duties implies hard restrictions of data access by a role at the design level, while dynamic separation of duties is enforced at runtime and is based on the particular data instances. In our work, we explore the effects of these principles via authorization rules and con<sup>fl</sup>ict sets.

Role engineering is a broad and active area of research and the reader can <sup>fi</sup>nd many details in [22]. Our focus here is on the ideas of role engineering with regard to security and privacy. While traditional RBAC approach is built around the basic elements of the users, roles and permissions, these elements are not necessary to represent privacy authorization rules. They need to be amended with the elements of purposes, conditions and obligations of using private data [29,34]. We implicitly address these issues via the analysis of risk exposure of private data. Speci<sup>fi</sup>cally in healthcare, role engineering started with the de<sup>fi</sup>nitions of basic roles – such as patient, doctor, researcher – by Barkley [5]. Subsequent work explored many modi<sup>fi</sup>- cations of RBAC based on the authentication context [32], doctor location [27], principle of explicit denial of access to some patient data [45] and inter-organizational differences in RBAC structure [33]. These works exemplify the broad scope of issues with what healthcare role engineering is dealing, and we think that our method can provide a solid decision support tool in making choices about healthcare roles. Even if the roles are well de<sup>fi</sup>ned, there may be a need to override those constraints — such as in “controlled overriding” [52] or “break the glass” policy [17]. While these overrides trigger additional logging and audit routines, the risks of resulting privacy exposures are not discussed. Zhao and Johnson [54] provide a game theoretic analysis of escalation cases, but it is not work<sup>fl</sup>ow speci<sup>fi</sup>c. Our approach uses both the risk management view that relates to the top-level corporate policies and the work<sup>fl</sup>ow speci<sup>fi</sup>c analytical structure that supports decision making in a detail-oriented view.

The next line of defense is represented by the detection tools such as audit solutions and intrusion detection systems [28]. Audit systems produce activity logs (audit trails) that can be used for identifying instances of data misuse that would be missed otherwise. While they are a valuable tool, their major downside is the post factum nature of detection: damage may be long done and irrevocable before the misuse is identi<sup>fi</sup>ed. The problem is further compounded by the substantial volume of data produced by the audit systems, rendering substantial human review impractical, if not impossible [43]. On another hand, intrusion detection systems produce alerts of suspicious activity on the <sup>fl</sup>y thus resulting in quicker detection of misuse. However, they also produce a lot of information to review and in many cases generate false positives where a legitimate activity raises an alert [53]. Intrusion detection systems can be calibrated to reduce the false positive rates, but it necessarily results in the decrease of overall detection rates [42]. It is clear that both employee and task monitoring controls can potentially be used to prevent information disclosure in clinical work<sup>fl</sup>ows. However, their bene<sup>fi</sup>ts and costs are speci<sup>fi</sup>c to each individual situation and no universal solution will work in all circumstances. Therefore, we present a methodology to evaluate the con<sup>fi</sup>guration of controls based on the desired personnel assignment in a clinical work<sup>fl</sup>ow environment.

## 3. Security con<sup>fl</sup>ict and control

In this section, we use an example of a patient visit at the physician's of<sup>fi</sup>ce to introduce the key concepts: security con<sup>fl</sup>ict, disclosure risk, and control, in our model.

Consider a simple clinical work<sup>fl</sup>ow process [8] as shown in Fig. 1. The process starts with a patient making an appointment and ends with an accountant updating accounting ledgers. Upon the receptionist at the clinic receiving an appointment request, the request is entered into the system (T1). Once the appointment information is recorded, the patient demographic information, current illness symptoms, and payment information are documented (T2), and medical records are retrieved (T3). At the time of the visit, all the relevant information about the patient is gathered. The nurse then examines the patient's current health condition, records the patient's vitals, and hands the patient over to a physician (T4). The physician examines the patient and develops the treatment plan (T5). The plan may involve one or both of the following, lab tests (T6) and medical procedures such as vaccinations and X-rays (T7). Meanwhile, the physician prescribes medication for the patient (T8). Upon receiving the diagnostic results, the physician reviews the results (T9), and communicates with the patient (T10). If necessary, the patient schedules a follow-up appointment (T11). When the visit is complete, bills are sent out (T12) and the accounting ledgers are updated (T13). There are a total of thirteen tasks in this work<sup>fl</sup>ow process. Table 1 presents a brief description for each task that is involved in the process.

The entire process in Fig. 1 requires <sup>fi</sup>ve different quali<sup>fi</sup>cation pro<sup>fi</sup>les representing <sup>fi</sup>ve skill levels of employees: staff member (S), nurse (N), physician (P), lab technician (T), and accountant (A). A staff member can complete basic tasks that do not require special skills quali<sup>fi</sup>cation. Tasks T1, T2, T3, T11, and T12 can be performed by a staff member. Other tasks require professional training or special certi<sup>fi</sup>cation. For example, T4 involves examining patients that requires medical training and credentials to operate medical devices. The same is true for the lab tests at T6 and other medical procedures at T7, where speci<sup>fi</sup>c technique quali<sup>fi</sup>cations are required and can only be performed by specialized lab technicians. Tasks 5, 8, and 10 may be completed by a nurse or a physician. Only accountants are able to update the ledgers. Technically, a physician can complete any tasks except for updating the ledgers and sophisticated lab procedures. A nurse can perform part of the physician's tasks, and in some cases, simple lab tests, and all the tasks of a staff member. A lab technician or a nurse can be used as a staff member. A lab technician or a nurse can also be used to substitute each other. Accountants can update ledgers and have quali<sup>fi</sup>cation levels equivalent to staff members with respect to other operations. In addition to the differences in the skill levels, each employee is associated with a speci<sup>fi</sup>c cost of labor, and for each task, a speci<sup>fi</sup>c service ef<sup>fi</sup>ciency or service rate. For example, the salary for a physician is higher than a nurse while a nurse may be more ef<sup>fi</sup>cient at conducting basic examinations.

## 3.1. Security conflict

In execution of each task, employees obtain access to various types of patient information. The types of patient information that are involved in the clinical process include patient demographical informa tion, such as the name, date of birth, gender, and address, patient medication information, such as the name, dosage, and frequency of the prescribed medication, patient medication history, such as the medical records for previous visits, lab test and diagnostic results, billing information, and credit history. If too much information is collected by a malicious employee, it can be exploited in a variety of ways — a condition that can be termed disclosure risk. For disclosure risk to exist, it is necessary that certain pieces of information are available to the same employee during the work<sup>fl</sup>ow execution — a situation that we term security conflict. The disclosure risk in our problem setting may be measured in terms of the number of the compromised security con<sup>fl</sup>icts, which indicates the amount of potentially exposed information elements, severity of disclosure consequences, or the size of a compromised con<sup>fl</sup>ict, which re<sup>fl</sup>ects the dif<sup>fi</sup>culty of obtaining all the required information within a security con<sup>fl</sup>ict. Next, we discuss the types of security con<sup>fl</sup>icts that can arise in a clinical process.

![](/api/attachments/JJUK3BBA/fulltext/images/a27e283a435b93a57adb4d24a99fc0f685ae240a2b6314783dad22816fe85cc4.jpg)  
Fig. 1. A clinical work<sup>fl</sup>ow process diagram, adopted from [8].

Table 1  
Description of tasks in the clinical work<sup>fl</sup>ow process diagram in Fig. 1.

<table><tr><td>Task</td><td>Description</td></tr><tr><td>T1</td><td>Schedule appointment</td></tr><tr><td>T2</td><td>Document patient information</td></tr><tr><td>T3</td><td>Retrieve patient medical records</td></tr><tr><td>T4</td><td>Examine and assess patient</td></tr><tr><td>T5</td><td>Develop treatment plans</td></tr><tr><td>T6</td><td>Conduct lab tests</td></tr><tr><td>T7</td><td>Undergo medical procedures</td></tr><tr><td>T8</td><td>Prescribe medication</td></tr><tr><td>T9</td><td>Review diagnostic results</td></tr><tr><td>T10</td><td>Communicate with patient</td></tr><tr><td>T11</td><td>Schedule follow-up appointment</td></tr><tr><td>T12</td><td>Billing</td></tr><tr><td>T13</td><td>Update accounting ledgers</td></tr></table>

As described in [4], security con<sup>fl</sup>icts arise if the data is accessed by an unauthorized or unquali<sup>fi</sup>ed employee. Access to different pieces of data at multiple tasks of the work<sup>fl</sup>ow also leads to the vulnerability of privacy disclosure or fraud. In the example of the clinical work<sup>fl</sup>ow, only certi<sup>fi</sup>ed nurses and physicians are quali<sup>fi</sup>ed for prescribing medication. Therefore, a prescription by a staff member or a lab technician constitutes a security con<sup>fl</sup>ict. We encode this quali-<sup>fi</sup>cation requirement as a restriction “T8 not performed by A, T, S” as shown in Table 2. Similarly, results of a lab test performed by any employee other than a lab technician results in a security con<sup>fl</sup>ict. We encode this skills requirement as a restriction “T6 not performed by A, N, P, S” as shown in Table 2.

Avoiding unnecessary access to private data reduces the possibility of information breach. For example, task 3 requires minimum skills while providing access to all patient information. Therefore, access should only be given to employees who have received compliance certi<sup>fi</sup>cation. Task 10 requires access to both the patient's demographic information and diagnostic results. If the patient is diagnosed with a sensitive condition, unauthorized access to this information may compromise the patient's privacy. Hence, by changing the authorization level for task 10 from all employee types to only P or N reduces security concerns. Similarly, task 9 gives access to a great amount of sensitive information, and to safe guard the patient privacy, access right should only be given to authorized individuals among P, N or S. Table 2 lists some examples of such authorization restrictions.

Authorization and quali<sup>fi</sup>cation restrictions imposed on task execution do not completely eliminate the possibility of information breach. Access to different pieces of data at multiple tasks of the work<sup>fl</sup>ow over a time period may develop the vulnerability of privacy disclosure or fraud. Following [4], we focus on two types of con<sup>fl</sup>icts: fraud concerns and privacy concerns.

In terms of fraud concerns, knowledge of a patient's personal information at task 1 or task 11, the patient's medication information at task 8, and billing information at task 12 may lead to fraudulent insurance claims. Access to a patient's personal information at task 1 or task 11, the patient's medical records at task 3, and billing records at task 12 could yield an accounts-receivable fraud in the form of generating fake invoices. Similarly, an employee who conducts lab tests at task 6 or other medical procedures at task 7 has the access to the patient's billing records at task 12 could lead to fraud in the form of asset misappropriation that can be covered up in the billing process. In terms of privacy concerns, knowledge of a patient's demographical information at task 2, diagnostic results at task 9, and the prescribed medication task 8 may reveal the patient's current medical status. Knowledge of a patient's credit information at task 2, medication history at task 3, and diagnostic results at task 9 could potentially put the patient in a disadvantageous situation in insurance premium charges. Knowledge of a patient's contact information at task 1 or task 11 and medication information at task 8 or task 10 may invite unsolicited drug marketers.

Table 2  
Examples of quali<sup>fi</sup>cation and authorization restrictions for individual tasks

<table><tr><td>Type of restrictions</td><td>Description of the restriction</td></tr><tr><td>Skill qualification</td><td>T8 not performed by A, T, ST6 not performed by A, N, P, S</td></tr><tr><td>Authorization</td><td>T10 not performed by T, S, or AT3 not performed by T or AT9 not performed by T, S or A</td></tr></table>

We represent a work<sup>fl</sup>ow-level security concern that involves a multi-task assignment with a set of con<sup>fl</sup>icting tasks. Assigning all the tasks within such a set to the same employee leads to a security con<sup>fl</sup>ict. We call such a set a conflict set. Table 3 lists some examples of the security con<sup>fl</sup>ict sets.

## 3.2. Control

Control procedures monitor process performance and provide means to mitigate risk. In auditing practice, control procedures have preventive, detective, and corrective functions. Commonly used control procedures include document sampling and audit, performance reviews, and segregation of duties [35]. A business process typically has a range of available control procedures, each of which is capable of monitoring a speci<sup>fi</sup>c set of work<sup>fl</sup>ow activities. In this paper, we consider two types of monitoring controls: task-level monitoring, or outcome monitoring, and personnel-level monitoring, or behavior monitoring.

By placing a monitoring control procedure at a task, the control is able to eliminate security threats at that task, therefore, eliminating any of the security concerns that involve the task. For example, task 12 handles patients' billing information. A monitoring control procedure deployed at task 12 is able to ensure that the billing information is properly handled and any possibility of information breach is eliminated.

Alternatively, by placing a monitoring control procedure at an employee, the control is able to eliminate security threats potentially caused by the employee. For instance, a staff member could be assigned to perform tasks 2 and 10, while access to information at these two tasks could potentially lead to privacy disclosure. Monitoring the behavior of this staff member is able to ensure that no inappropriate activities that violate the information security constraints are taking place.

## Table 3

Examples of conflict sets for multi-task assignments

<table><tr><td>Type of conflicts</td><td>Conflict sets</td></tr><tr><td rowspan="2">Fraud</td><td>{T1, T8, T12}, {T8, T11, T12}, {T6, T12}</td></tr><tr><td>{T1, T3, T12}, {T3, T11, T12}, {T7, T12}</td></tr><tr><td>Privacy</td><td>{T2, T3, T9}, {T2, T8, T9}, {T1, T8}, {T2, T8}, {T1, T10}, {T2, T10}</td></tr></table>

## 3.3. The decision problem

The staf<sup>fi</sup>ng strategies that maximize work<sup>fl</sup>ow ef<sup>fi</sup>ciency without information security constraints may put patient information at risk of disclosure. Controls are introduced at certain cost to resolve security con<sup>fl</sup>icts and hence alleviate the risk of disclosure. In order to achieve both work<sup>fl</sup>ow ef<sup>fi</sup>ciency and information security requirements, an organization <sup>fi</sup>rst wishes to <sup>fi</sup>nd the staf<sup>fi</sup>ng strategies that maximize work<sup>fl</sup>ow ef<sup>fi</sup>ciency, and then look for control placement strategies to deploy at a subset of employees and tasks to eliminate security con<sup>fl</sup>icts. We formally de<sup>fi</sup>ne this problem as a two-stage decision problem. At the <sup>fi</sup>rst stage, a throughput optimization problem is formulated to identify a set of equivalent optimal solutions; at the second stage, a control cost minimization problem is developed to <sup>fi</sup>nd optimal control placement strategies at combinations of tasks and employee to eliminate or mitigate the disclosure risk. The outcomes of the two-stage model are an optimal employee assignment and control placement strategy that achieve both ef<sup>fi</sup>- ciency and information security requirements in a work<sup>fl</sup>ow. In the next section, we formally introduce the mathematical model.

## 4. Model formulation

## 4.1. Personnel assignment for throughput optimization

We model a work<sup>fl</sup>ow as a queueing network consisting of N tasks (nodes), where tasks are labeled as $1 , 2 , \ldots , N .$ Orders enter through node 1 and are subsequently processed through the nodes. Upon completion of service at node j, an order moves to another node $j ^ { \prime }$ with a transition rate $r _ { j j }$ with $0 { \le } r _ { i i ^ { \prime } } { \le } 1$ . Orders exit through node N after completing their process. A node j′ is reachable from a node j if there exists as sequence of arcs $( j , i _ { 1 } ) , ( i _ { 1 } , i _ { 2 } ) , . . . , ( i _ { n } j ^ { \prime } )$ for $n { \geq } 1$ such that $r _ { j , i _ { 1 } } r _ { i _ { 1 } , i _ { 2 } } – r _ { i _ { n } , j ^ { ' } } > 0 .$ We assume that all the nodes are reachable from node 1 (entry point) and that node N (exit point) is reachable from all the nodes. Node N is an exit node, that is, $\sum { \dot { N } } _ { j = 1 } ^ { N - 1 } r _ { N j } { < } 1$ and $\begin{array} { r } { 1 - \sum _ { j = 1 } ^ { N } r _ { N j } > 0 } \end{array}$ is the probability of an order exiting from node N.

The arrival process of orders to node 1 is Poisson with intensity $\lambda > 0 .$ . Orders queue at each node according to a <sup>fi</sup>rst-in <sup>fi</sup>rst-out queueing discipline. There are M employees available who could be assigned to the tasks. Each task can only be executed by one employee, but an employee can execute multiple tasks. If employee i has the skills to do task $j ,$ then the employee's time to complete the task varies for each order according to an exponential distribution with (service) rate $\mu _ { i j } > 0$ . If employee i does not have the skills to do task j, then we set $\mu _ { i j } = 0$ . Last, we assume that the service times at each node are independent of each other and independent of the arrival process of orders.

Under the preceding conditions, the order processing system can be modeled as an open Jackson queueing network (see [24]). We denote by $\bar { \lambda } _ { j }$ the total mean <sup>fl</sup>ow rate into node j. The $\bar { \lambda } _ { j }$ rates can be obtained by solving the traf<sup>fi</sup>c equations

$$
\bar {\lambda} _ {1} = \lambda + \sum_ {i = 1} ^ {N} \bar {\lambda} _ {i} r _ {i 1}, \quad \bar {\lambda} _ {j} = \sum_ {i = 1} ^ {N} \bar {\lambda} _ {i} r _ {i j}, \text {   for   all   } j = 2,..., N,
$$

which will always have solution under the node reachability assumptions stated above.

Our goal in this system is to <sup>fi</sup>nd an assignment of personnel to tasks so as to minimize the average processing time of the orders going through the work<sup>fl</sup>ow (average throughput time). To do so, we introduce a binary 0–1 decision variable $x _ { i j } ,$ such that $x _ { i j } = 1$ if and only if we assign employee i to do task j. We denote by X the M×N-dimensional matrix of decision variables. For a given assignment matrix X, T(X) denotes the steady-state average throughput time per order, that is, the average time required for an order to pass through the work<sup>fl</sup>ow; and $\rho _ { i } ( X )$ the utilization of employee i, that is, the proportion of the employee's time used by the orders the employee processes. Some tasks might require a skill level that some of the employees do not have. We set $s _ { i j } = 1$ if employee i has the required skills to perform task j, and $s _ { i j } = 0$ otherwise. We denote by $\cdot S { = } [ s _ { i j } ]$ the M×N-dimensional skill matrix. The resulting optimization model is as follows:

$$
(\mathrm{P} _ {0}) \quad z _ {0} = m i n T (X),
$$

s.t.

$$
\sum_ {i = 1} ^ {M} x _ {i j} = 1, \forall j,\tag{1}
$$

$$
X \leq S,
$$

$$
\rho_ {i} (X) <   1, \forall i,\tag{2}
$$

$$
x _ {i j} \in \{0, 1 \}, \forall i, j.\tag{3}
$$

4

Constraint (1) indicates that each task should be performed by exactly one employee. Constraint (2) indicates that employees should only be assigned to tasks for which they have the skills to perform. Constraint (3) indicates that the utilization of employee i should be less than 100% (otherwise the work<sup>fl</sup>ow will be unstable). Finally, constraint (4) indicates that variables x<sub>ij</sub> are binary.

Using the open Jackson queueing assumptions we have (see [24]):

$$
\rho_ {i} (X) = \sum_ {j = 1} ^ {N} \frac {\bar {\lambda} _ {j}}{\mu_ {i j}} x _ {i j},
$$

for all $1 \leq i \leq M$ . Furthermore, i $\mathrm { f } \rho _ { i } ( X ) < 1$ for all $1 \leq i \leq M ,$ then the average throughput time per order is given by

$$
T (X) = \frac {1}{\lambda} \sum_ {i = 1} ^ {M} \frac {\rho_ {i} (X)}{1 - \rho_ {i} (X)}.
$$

Notice that the obiective function $T ( X )$ is a non-increasing function of the $\mu _ { i j }$ parameters, so that if two employees with indexes i and $i ^ { \prime } ,$ respectively, can perform the same task j but have different service levels $\mu _ { i j } { < } \mu _ { i j }$ , then in an optimal solution it would be less desirable to assign the less ef<sup>fi</sup>cient employee (employee i) to do such a task. Therefore, our model takes into account the variability in skills and performance quality of the employees.

## 4.2. Assessment and control of disclosure risk

We consider a collection of K nonempty subsets of $\{ 1 , . . . , N \} ,$ , namely, $A _ { 1 } , A _ { 2 } , . . . , A _ { K } ,$ which we call security con<sup>fl</sup>ict sets. The elements in one of those sets represent a minimum collection of tasks that if assigned to the same employee will create a security con<sup>fl</sup>ict. (A collection of tasks is minimum in the sense that if A is a con<sup>fl</sup>ict set, then $B \subset { \cal A } , { \cal B } \ne { \cal A } ,$ is not a con<sup>fl</sup>ict set.) As discussed in previous sections, con<sup>fl</sup>icts may arise because of the risk of identity theft, fraud, or privacy disclosure. For example, an employee assigned to do task 2 “Document patient information” has access to customer information such as name, address and maximum allowable bene<sup>fi</sup>ts. If the same employee is assigned to task 9 “Review diagnostic results,” she would have an opportunity to identify the health condition of the individual. This may give rise to harassment, extortion or other abuses of the patient's privacy.

To assess the disclosure risk arising from assigning tasks from a con<sup>fl</sup>ict set to one employee, we introduce sets $B _ { i } ( X ) \subset \{ 1 , . . . , N \} ,$ representing the tasks assigned to employee i according to

assignment matrix X, that is

$$
B _ {i} (X) = \left\{j: x _ {i j} = 1 \right\}.
$$

We say that con<sup>fl</sup>ict set $A _ { k }$ is at risk if $\cdot { A _ { k } } \subset B _ { i } ( X )$ for some $i { \in } \{ 1 , { \ldots } , M \}$ As discussed in previous sections, there are two types of controls to prevent security breaches: controls at the employee level and controls at the task level. If a control is applied at the employee level, then we assume that all the tasks assigned to the employee will be safe and in particular, it will make safe all of the con<sup>fl</sup>ict sets at risk that are assigned to the employee. If a control is applied at the task level, then the task will be safe and in particular, it will make safe all of the con<sup>fl</sup>ict sets that contain that task.

Our goal in this section is to <sup>fi</sup>nd a minimum cost assignment of controls of the two types (employee and task level) so as to ensure that all con<sup>fl</sup>ict sets are safe. We denote by g the cost of a control on employee i, and by $h _ { j }$ the cost of a control on task j. We denote by E the K×M matrix whose entries are:

$$
\begin{array}{l l} 1 & \text { if } A _ {k} \subset B _ {i} (X), \\ 0 & \text { otherwise }. \end{array}
$$

Matrix entry $E _ { k i }$ indicates whether or not the tasks in con<sup>fl</sup>ict set k have been assigned to employee i and ${ \bf { S 0 , } }$ whether or not the set is made unsafe by employee i. Similarly, we denote by F the $K \times N$ matrix whose entries are:

$$
F _ {k j} := \left\{ \begin{array}{l l} 1 & \text { if } j \in A _ {k}, \\ 0 & \text { otherwise }. \end{array} \right.
$$

Matrix entry $F _ { k j }$ indicates whether or not task j is in con<sup>fl</sup>ict set k. Finally, we introduce binary decision variables $\nu _ { i } ( \mathrm { f o r } i = 1 , . . . , M )$ and w<sub>j</sub> for $( j = 1 , . . . , N )$ to represent whether or not we place a control on employee i and task j, respectively.

The resulting optimization model is as follows:

$$
\left(\mathrm{P} _ {1}\right) \quad z _ {1} (X) = \operatorname{ming} ^ {T} v + h ^ {T} w,
$$

s.t.

$$
\begin{array}{l} E v + F w \geq \vec {1}, \\ v _ {i}, w _ {j} \in \{0, 1 \}, \forall i, j. \end{array}\tag{5}
$$

6

In this model, g represents the cost vector of the controls on employees and h represents the cost vector of the controls on tasks. The vector 1 represents the K-dimensional all-ones vector. Constraint (5) indicates that all con<sup>fl</sup>ict sets should be safe by either placing a control on at least one task in the con<sup>fl</sup>ict set or by controlling an employee that makes the set unsafe. We emphasize the dependency on X of the $z _ { 1 } ( X )$ value to indicate that the minimum value of the objective function depends on the employee assignment. Concretely, notice that the matrix E depends on the assignment matrix X. Also notice that problem $\mathrm { P _ { 1 } }$ is a set covering problem.

In formulating problem $\mathrm { P } _ { 1 }$ we have assumed that the controls (if assigned) are fully effective. Nevertheless, it is possible that some of the controls are not completely effective because of diverse reasons, such as some employees or tasks are easier to monitor than others, lack of effort, systematic errors, and so on. To account for the effectiveness of the controls, in Appendix A we provide a model extension for $\mathrm { P } _ { 1 }$ to account for the effectiveness of controls.

## 4.3. Throughput optimization and controls

By combining the throughput optimization problem and the control cost minimization problem that we have discussed in the preceding sections, we obtain an overall methodology to assign employees and controls in an ef<sup>fi</sup>cient and safe way. Namely, we <sup>fi</sup>rst solve problem $\mathrm { P } _ { 0 }$ to <sup>fi</sup>nd the most ef<sup>fi</sup>cient assignments in terms of throughput time, and then we solve problem $\mathrm { P _ { 1 } }$ to <sup>fi</sup>nd the best way to assign controls according to the optimal assignments from $\mathrm { { P _ { 0 } } . }$

We denote by $X _ { 1 } , \dots , X _ { L }$ the optimal solutions to problem $\mathrm { { P _ { 0 } } , }$ that is, each $X _ { l }$ is a feasible employee assignment satisfying $T ( X _ { l } ) = z _ { 0 } ,$ for all $l { = } 1 , . . . , L .$ . Next, for each assignment $X _ { l }$ we solve problem $\mathrm { P _ { 1 } }$ and compute $z _ { 1 } ( X _ { l } )$ . Finally, we select $X ^ { * }$ as an employee assignment that satis<sup>fi</sup>es

$$
T \left(X ^ {*}\right) = z _ {0}, z _ {1} \left(X ^ {*}\right) = \min \left\{z _ {1} \left(X _ {1}\right), \dots , z _ {1} \left(X _ {L}\right) \right\},
$$

and implement the controls found from solving $\mathrm { P _ { 1 } }$ for $X ^ { * }$ .

However, <sup>fi</sup>nding $X ^ { * }$ that satis<sup>fi</sup>es $z _ { 1 } ( X ^ { * } ) { = } m i n \{ z _ { 1 } ( X _ { 1 } ) , { \ldots } , z _ { 1 } ( X _ { L } ) \}$ can be dif<sup>fi</sup>cult to implement in practice. This is because it requires to solve several set covering problems, one for each solution to $\mathrm { { P _ { 0 } } . }$ The set-covering problem is a well-known -hard problem [20], <sup>NP</sup>and hence, there are no known ef<sup>fi</sup>cient (polynomial time) algorithms to solve it. Therefore, even if we use state-of-the-art algorithms to solve set-covering, <sup>fi</sup>nding a solution to each of the subproblems $\mathrm { P _ { 1 } }$ can take a worst-case-scenario exponential number of iterations on the number of employees, tasks, and con<sup>fl</sup>ict sets, which could be computationally impractical. More importantly, to solve problem $\mathrm { P } _ { 1 }$ it is necessary to know the cost of controlling employees and tasks, which could be dif<sup>fi</sup>cult to assess or even not possible to achieve (no all controls are available or feasible). Therefore, we consider instead a sequential-decision methodology that could yield partial but practically relevant solutions.

Fig. 2 illustrates our approach in a decision support system context. After solving problem $\mathrm { P } _ { 0 }$ and identifying all of its optimal solutions (assignments), then we <sup>fi</sup>x one of them. It could be the assignment with the least con<sup>fl</sup>icts, or the assignment with the most available controls, or some other criteria. Then we sequentially apply controls until all con<sup>fl</sup>ict sets are covered or there are no more controls left. The decision of what control to apply next can be made based on the cost of the control (greedy choice), the number of con<sup>fl</sup>ict sets that the control covers, the dif<sup>fi</sup>culty of implementing the control, the appraised risk of the con<sup>fl</sup>ict sets, organizational and managerial concerns, etc. If after applying this procedure all con<sup>fl</sup>ict sets are covered, then we have obtained a fully safe solution that minimizes average throughput time. If we run out of controls before covering all con<sup>fl</sup>ict sets, then we have obtained a partially safe solution that minimizes average throughput time but with disclosure risk due to the presence of con<sup>fl</sup>ict sets that are left uncovered.

## 5. Computational results

In this section, we illustrate how our approach can be used in a context of a decision support system for staf<sup>fi</sup>ng a healthcare work<sup>fl</sup>ow.

## 5.1. Model calibration

We use the clinical work<sup>fl</sup>ow process presented in Section 3 for our computational analysis. The work<sup>fl</sup>ow parameters are calibrated as follows. We assume a <sup>fi</sup>xed collection of employees that are available to perform these 13 tasks. The 1-Step Transition Matrix of the work<sup>fl</sup>ow is presented in Table B.11 in Appendix B. To illustrate the main concerns that surround the issue of improper information access by employees, we introduce a collection of 22 con<sup>fl</sup>ict sets, breach of which can lead to undesired exposure of private information. We vary the size of the con<sup>fl</sup>ict set between 2 and 4. We assume that there are seven employees of different skill quali<sup>fi</sup>cations available to process work<sup>fl</sup>ow tasks, and that new patients arrive at a rate of 2 per hour. The service rate and the skill levels of each employee for each task in the work<sup>fl</sup>ow are presented in Table C.12 in Appendix C.

![](/api/attachments/JJUK3BBA/fulltext/images/c9d74fa4466fcc831f52670de6a8ae27b1f4c446edfaa7dd70154a53a5722062.jpg)  
Fig. 2. Solution methodology.

## 5.2. Finding optimal personnel assignments for throughput optimization

By solving the throughput optimization model $\left( \mathrm { P _ { 0 } } \right)$ using the above model parameterization, we obtain six optimal personnel assignment solutions, $X _ { 1 } , . . . , X _ { 6 } ,$ that result in identical expected processing costs and waiting times. A summary of these solutions is presented in Table 4, where columns $X _ { 1 } - X _ { 6 }$ represent optimal assignment solutions, and each cell describes how many tasks are assigned to each individual employee. The details of the six optimal assignments $X _ { 1 } , . . . , X _ { 6 }$ are presented in Appendix D.

## 5.3. Assessing severity of disclosure risk

In terms of work<sup>fl</sup>ow ef<sup>fi</sup>ciency, all of these solutions are identical both in terms of processing cost and personnel workload. However, picking an arbitrary solution to implement would be a mistake.

Table 5  
Summary of personnel assignment for solutions $\mathrm { X } _ { 1 }$ – $\mathrm { - } \mathrm { X } _ { 6 } .$

<table><tr><td>Employee</td><td> $X_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td> $X_4$ </td><td> $X_5$ </td><td> $X_6$ </td></tr><tr><td>E1</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>E2</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>E3</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>E4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>E5</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>E6</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>E7</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></table>

Each of these solutions is associated with different degree of information disclosure risks, as illustrated in Table 5. In this table, we present the number of compromised con<sup>fl</sup>ict set, as well as maximum and average size of the compromised con<sup>fl</sup>ict sets. For example, solution $X _ { 6 }$ could potentially result in a compromise of just one con<sup>fl</sup>ict set, while other solutions are not as good with this regard. Further, solutions $X _ { 1 }$ and $X _ { 3 }$ both result in a compromise of six distinct con<sup>fl</sup>ict sets, but the average as well as maximum size of the compromised set is greater for solution $X _ { 3 } .$ Therefore, when making the decision on choosing a particular staf<sup>fi</sup>ng strategy, organizations need to estimate the magnitude of disclosure risk both in terms of the number of their potentially exposed data elements, severity of consequences, and the dif<sup>fi</sup>culty for the attacker of obtaining the required information within a con-<sup>fl</sup>ict set, i.e., the size of a con<sup>fl</sup>ict set. The full speci<sup>fi</sup>cations of the compromised sets in $X _ { 1 } , . . . , X _ { 6 }$ are detailed in Appendix D.

Another way to measure the severity of disclosure risk is by the degree of presence of a con<sup>fl</sup>ict set in the optimal personnel assignment solutions. Table 6 presents the frequency of the con<sup>fl</sup>ict sets that are present in different solutions. As one can see, the set {T2, T7} is the worst con<sup>fl</sup>ict set as it is present in all six solutions. On the other hand, 12 of 22 con<sup>fl</sup>ict sets are not exposed in any of the assignment con<sup>fi</sup>gurations. Given the fact that the probability of security breach is dif<sup>fi</sup>cult to obtain in practice, the frequency of the con<sup>fl</sup>ict sets appearing in all of the candidate solutions can well be viewed as a proxy of the breach probability. For those con<sup>fl</sup>ict sets that are never exposed, then the breach probability is zero, therefore there is no disclosure risk. In organizations where control resources are scarce, these inactive con<sup>fl</sup>icts can be safely ignored.

## 5.4. Exploring control approaches for disclosure risk mitigation

Given that all six possible solutions are drastically different in their impact on information security state, we next explore the ef<sup>fi</sup>- ciency of personnel-level and task-level monitoring tools in reducing the disclosure risk. One possible way to prevent information abuse is by monitoring employees who are involved in sensitive information processing tasks. For all of the six possible solutions, Tables 7 and 8 present an absolute number and a percentage of con<sup>fl</sup>ict sets that can be successfully protected by implementing employee monitoring. The percentage of con<sup>fl</sup>ict sets protected is calculated as the absolute number of con<sup>fl</sup>ict sets protected divided by the total number of exposed con<sup>fl</sup>ict sets. Not surprisingly, monitoring an employee who is performing a single task does not have an impact in terms of reducing information security risk since our model assumes no collusion between employees. However, monitoring multi-task employees such as E1 and E2 has different effectiveness depending on which personnel assignment scheme is implemented.

Characterization of personnel assignment solutions by the severity of disclosure risk.  
Table 6

<table><tr><td>Solution</td><td>Number of compromised sets</td><td>Max size of compromised sets</td><td>Average size of compromised sets</td></tr><tr><td> $X_1$ </td><td>6</td><td>3</td><td>2.17</td></tr><tr><td> $X_2$ </td><td>5</td><td>4</td><td>2.6</td></tr><tr><td> $X_3$ </td><td>6</td><td>4</td><td>2.5</td></tr><tr><td> $X_4$ </td><td>4</td><td>2</td><td>2</td></tr><tr><td> $X_5$ </td><td>6</td><td>3</td><td>2.17</td></tr><tr><td> $X_6$ </td><td>1</td><td>2</td><td>2</td></tr></table>

Frequency of con<sup>fl</sup>ict sets that are potentially breached in different solutions.

<table><tr><td>Conflict set</td><td>Frequency in solutions</td></tr><tr><td>{T1,T3}</td><td>4</td></tr><tr><td>{T1,T10}</td><td>3</td></tr><tr><td>{T2,T7}</td><td>6</td></tr><tr><td>{T2,T10}</td><td>3</td></tr><tr><td>{T4,T9}</td><td>3</td></tr><tr><td>{T7,T10}</td><td>3</td></tr><tr><td>{T1,T4,T10}</td><td>1</td></tr><tr><td>{T2,T7,T10}</td><td>3</td></tr><tr><td>{T1,T3,T4,T10}</td><td>1</td></tr><tr><td>{T1,T3,T5,T9}</td><td>1</td></tr><tr><td>{T1,T8,T12},{T8,T11,T12},{T1,T3,T7},{T1,T3,T12},{T3,T11,T12},{T4,T9,T12},{T2,T3,T9},{T2,T8,T9},{T1,T8},{T2,T8},{T6,T12},{T7,T12}</td><td>0</td></tr></table>

Similar to employee monitoring, task monitoring has different degree of effectiveness in different solutions. Tables 9 and 10 describe the effectiveness of task-level controls in different solutions. For example, in solution 2, monitoring task T1 can potentially prevent information disclosure for 80% of all exposed con<sup>fl</sup>ict sets, with monitoring of task T10 being a solid second option. On the contrary, in solution $^ { 3 , }$ there is no dominant location of control, with monitoring of either of the tasks T2, T7 or T10 providing 50% coverage for exposed con<sup>fl</sup>ict sets. Overall, there is no universal best placement of task monitoring controls, since they are contingent on the resultant personnel assignment solutions from $\mathrm { { P _ { 0 } } . }$

## 5.5. Control application for disclosure risk mitigation

The problem of selecting the best placement for monitoring controls cannot be optimized if the costs of controls are not known or readily available. In these situations, the organizations have to resort to the con<sup>fi</sup>guration analysis using a solution evaluation methodology presented in Fig. 2. In the following discussion, we present possible sequence of evaluation steps that can be used by an organization.

Take the solution $X _ { 1 }$ to the personnel assignment problem for example. In the case of solution $X _ { 1 }$ , there are six exposed con<sup>fl</sup>ict sets: {T1, T3}, {T4, T9}, {T2, T10}, {T2, T7}, {T7, T10}, {T2, T7, T10}. We can iterate through the solution methodology trying to place task-based and employee-based monitoring tools. If we start with the task-based monitoring tools, a good place to start would be task T2, as it will remediate 50% of exposed con<sup>fl</sup>icts. As a next step, we can enable a monitoring solution for E1, which will resolve two more con<sup>fl</sup>icts. Finally, only con<sup>fl</sup>ict set {T7, T10} is left unmitigated and this can be achieved my placing a task monitoring tool on either T7 or T10. Overall, this solution requires one deployment of personnel monitoring and two deployments of task monitoring tools.

Effectiveness of employee-focused monitoring solutions (absolute number of con<sup>fl</sup>icts addressed).

<table><tr><td>Employee</td><td> $X_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td> $X_4$ </td><td> $X_5$ </td><td> $X_6$ </td></tr><tr><td>E1</td><td>2</td><td>4</td><td>2</td><td>2</td><td>1</td><td>0</td></tr><tr><td>E2</td><td>4</td><td>1</td><td>4</td><td>2</td><td>5</td><td>1</td></tr><tr><td>E3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>E4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>E5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>E6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>E7</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Table 8  
Effectiveness of employee-focused monitoring solutions (percentage of con<sup>fl</sup>icts addressed).

<table><tr><td>Employee</td><td> $X_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td> $X_4$ </td><td> $X_5$ </td><td> $X_6$ </td></tr><tr><td>E1</td><td>33%</td><td>80%</td><td>33%</td><td>50%</td><td>17%</td><td>0%</td></tr><tr><td>E2</td><td>67%</td><td>20%</td><td>67%</td><td>50%</td><td>83%</td><td>100%</td></tr><tr><td>E3</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>E4</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>E5</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>E6</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>E7</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr></table>

Alternatively, if the starting point is to place an employee monitoring solution, it is best to enable it for E2, effectively covering 67% of the exposed con<sup>fl</sup>ict sets. Next, two additional task-level controls can be placed to mitigate {T1, T3} and {T4, T9}; ultimately resulting in the same composition of controls (2 tasks and 1 employee), but having a different control location in each case. Obviously, it is possible in principle to do task-based or employee-based controls exclusively; however the <sup>fi</sup>nal decision may rest on additional factors, such as varying costs of placing controls in different locations, availability of solutions, and employee morale.

## 6. Concluding remarks

We have presented a decision making methodology for healthcare organizations to design and improve the operational ef<sup>fi</sup>ciencies in work assignments and information security in the work<sup>fl</sup>ow systems. These are pressing challenges in the healthcare industry which is experiencing rising costs and signi<sup>fi</sup>cant shortages in human resources, and is faced with a plethora of rules and regulations to safeguard patient safety and information security. An important aspect of proposed decision making methodology is that it is practical in healthcare settings where it is often infeasible to objectively quantify the probability of information breach, precise cost implications of placing security controls, and <sup>fi</sup>nancial consequences of information disclosure.

Effectiveness of task-focused monitoring solutions (absolute number of con<sup>fl</sup>icts addressed).

<table><tr><td>Task</td><td> $X_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td> $X_4$ </td><td> $X_5$ </td><td> $X_6$ </td></tr><tr><td>1</td><td>1</td><td>4</td><td>2</td><td>2</td><td>1</td><td>0</td></tr><tr><td>2</td><td>3</td><td>1</td><td>3</td><td>1</td><td>3</td><td>1</td></tr><tr><td>3</td><td>1</td><td>2</td><td>2</td><td>1</td><td>0</td><td>0</td></tr><tr><td>4</td><td>1</td><td>2</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>5</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>7</td><td>3</td><td>1</td><td>3</td><td>1</td><td>3</td><td>1</td></tr><tr><td>8</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>9</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>10</td><td>3</td><td>3</td><td>3</td><td>1</td><td>4</td><td>0</td></tr><tr><td>11</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>12</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>13</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Table 10  
Effectiveness of task-focused monitoring solutions (percentage of con<sup>fl</sup>icts addressed).

<table><tr><td>Task</td><td> $X_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td> $X_4$ </td><td> $X_5$ </td><td> $X_6$ </td></tr><tr><td>1</td><td>17%</td><td>80%</td><td>33%</td><td>50%</td><td>17%</td><td>0%</td></tr><tr><td>2</td><td>50%</td><td>20%</td><td>50%</td><td>25%</td><td>50%</td><td>100%</td></tr><tr><td>3</td><td>17%</td><td>40%</td><td>33%</td><td>25%</td><td>0%</td><td>0%</td></tr><tr><td>4</td><td>17%</td><td>40%</td><td>0%</td><td>25%</td><td>17%</td><td>0%</td></tr><tr><td>5</td><td>0%</td><td>0%</td><td>17%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>6</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>7</td><td>50%</td><td>20%</td><td>50%</td><td>25%</td><td>50%</td><td>100%</td></tr><tr><td>8</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>9</td><td>17%</td><td>0%</td><td>17%</td><td>25%</td><td>17%</td><td>0%</td></tr><tr><td>10</td><td>50%</td><td>60%</td><td>50%</td><td>25%</td><td>67%</td><td>0%</td></tr><tr><td>11</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>12</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>13</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr></table>

The <sup>fi</sup>rst stage of the solution methodology entails maximizing the work<sup>fl</sup>ow ef<sup>fi</sup>ciency with available human resources by allocating tasks to employees with appropriate skill levels and who can execute appropriate tasks most effectively. While the <sup>fi</sup>rst stage maximizes operational ef<sup>fi</sup>ciencies, it can expose organizations to information disclosure risks that can be exploited to violate patient safety and information security. To address the ensuing privacy and fraud concerns we de<sup>fi</sup>ne task-based con<sup>fl</sup>ict sets to assess disclosure risks with optimal task assignments. In the second stage of the solution methodology, various task-based and employee-based security control strategies are incorporated into a decision support model to help decision makers to effectively manage and achieve work<sup>fl</sup>ow ef-<sup>fi</sup>ciency and meet information security requirements. An important <sup>fi</sup>nding from our extensive computational analysis is that while some security con<sup>fl</sup>icts are theoretically possible, they are not practically relevant in speci<sup>fi</sup>c work<sup>fl</sup>ow con<sup>fi</sup>gurations. Thus our proposed methodology aids decision makers in identifying and focusing on particularly problematic security issues pertinent to the organization. A logical extension of our current work would focus on developing an iterative decision making approach that accommodates changes in staf<sup>fi</sup>ng, work<sup>fl</sup>ow con<sup>fi</sup>gurations, and security requirements. Explicitly modeling the possibility of collusion among employees is also a viable avenue for future research.

## Appendix A. Control effectiveness and residual disclosure risk

To account for the effectiveness of controls, we introduce Bernoulli random variables $V _ { i }$ and $W _ { j }$ to represent whether or not a control is effective on an employee or a task. In other words, the probability that the control on employee i will be effective is

$$
\mathcal {P} \{V _ {i} = 1 \} = 1 - \mathcal {P} \{V _ {i} = 0 \} := p _ {i},
$$

where $0 { \le } p _ { i } { \le } 1$ . Similarly, the probability that the control on task j will be effective is

$$
\mathcal {P} \Bigl \{W _ {j} = 1 \Bigr \} = 1 - \mathcal {P} \Bigl \{W _ {j} = 0 \Bigr \} := q _ {j},
$$

where $0 \leq q _ { j } \leq 1$ . We also assume that the variables $V _ { i }$ and $W _ { j }$ are independent of each other. Notice that the parameters $p _ { i }$ and $q _ { j }$ can be used as a measure of the effectiveness of the controls, the closer to one the more effective is the control. Also notice that they can be estimated from statistics on the past performance of the controls.

Now, let $D _ { V } { : = } d i a g \{ V _ { 1 } { , } . . . . , V _ { M } \}$ denote the M×M-dimensional diagonal matrix with diagonal entries given by $V _ { 1 } , . . . , V _ { M } ,$ and $D _ { W } : = d i a g$ $\{ W _ { 1 } , . . . , W _ { N } \}$ be the N×N-dimensional diagonal matrix with diagonal entries given by $W _ { 1 } , . . . , W _ { N } .$ A revised optimization model to account for the effectiveness of the controls is

$$
\left(\mathrm{P} _ {2}\right) \quad z _ {2} (X) = \min \mathbf {g} ^ {T} v + h ^ {T} w,
$$

s.t.

$$
\mathcal {P} \bigg \{E D _ {V} v + F D _ {W} w \geq \stackrel {\rightarrow} {1} \bigg \} \geq 1 - \beta ,\tag{7}
$$

$$
v _ {i}, w _ {j} \in \{0, 1 \}, \forall i, j.\tag{8}
$$

In other words, we <sup>fi</sup>nd an assignment of controls to employees and tasks so as to minimize the total cost of the controls while satisfying the constraint that the residual disclosure risk is at most β, where β is a given parameter in the interval (0,1). By “residual disclosure risk” we mean the probability that at least one of the con<sup>fl</sup>ict sets is compromised.

Problem P is a stochastic program that can be approximately solved by using a Monte Carlo method. In this method, for each candidate solution (v,w), a sample of randomly generated values for Dv and Dw is used to determine the percentage of sample points for which $E D _ { V } \nu + F D _ { W } w \ge $ 1; the candidate solution is likely to be feasi-<sup>þ</sup>ble if such percentage is less than or equal to β.

## Appendix B. 1-Step Transition Matrix of the work<sup>fl</sup>ow in Fig. 1

Table B.11  
1-Step Transition Matrix

<table><tr><td></td><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td><td>T6</td><td>T7</td><td>T8</td><td>T9</td><td>T10</td><td>T11</td><td>T12</td><td>T13</td></tr><tr><td>T11</td><td>0</td><td>0.2</td><td>0.8</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T2</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T3</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.7</td><td>0.4</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T7</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T8</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>T9</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>T11</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>T12</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>T13</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Appendix C. Service rates and skills quali<sup>fi</sup>cations for each employee and each task in the work<sup>fl</sup>ow in Fig. 1

## Appendix D. Equivalent optimal solutions and the corresponding compromised con<sup>fl</sup>ict sets

Solution 1. [T1→E1, T2→E2, T3→E1, T4→E1, T5→E2, T6→E3, T7→E2, T8→E4, T9→E1, T10→E2, T11→E5, T12→E6, T13→E7]; Compromised sets: [{1 3}{4 9}{2 10}{2 7}{7 10}{2 7 10}].

Solution 2. [T1→E1, T2→E2, T3→E1, T4→E1, T5→E2, T6→E3, T7→E2, T8→E4, T9→E2, T10→E1, T11→E5, T12→E6, T13→E7]; Compromised sets: [{1 10}{1 3}{1 4 10}{1 3 4 10}{2 7}].

Solution 3. [T1→E1, T2→E2, T3→E1, T4→E2, T5→E1, T6→E3, T7→E2, T8→E4, T9→E1, T10→E2, T11→E5, T12→E6, T13→E7]; Compromised sets: [{1 3}{1 3 5 9}{2 10}{2 7}{7 10}{2 7 10}].

Solution 4. [T1→E1, T2→E2, T3→E1, T4→E2, T5→E1, T6→E3, T7→E2, T8→E4, T9→E2, T10→E1, T11→E5, T12→E6, T13→E7]; Compromised sets: [{1 10}{1 3}{2 7}{4 9}].

Solution 5. [T1→E2, T2→E2, T3→E1, T4→E1, T5→E1, T6→E3, T7→E2, T8→E4, T9→E1, T10→E2, T11→E5, T12→E6, T13→E7]; Compromised sets: [{4 9}{1 10}{2 10}{2 7}{7 10}{2 7 10}].

Solution 6. [T1→E2, T2→E2, T3→E1, T4→E1, T5→E1, T6→E3, T7→E2, T8→E4, T9→E2, T10→E1, T11→E5, T12→E6, T13→E7]; Compromised sets: [{2 7}].

## References

[1] American Hospital Association, The State of America's Hospitals — Taking the Pulse: Findings from the 2006 AHA Survey of Hospital Leaders, 2007.

[2] S. Ariss, Computer monitoring: bene<sup>fi</sup>ts and pitfalls facing management, Information Management 39 (7) (2002) 553–558.

[3] P.V. Asaro, J.E. Ries, Data mining in medical record access logs, in: 2001 American Medical Informatics Association Annual Symposium (AMIA), 2001, p. 855.

[4] X. Bai, R. Gopal, M. Nunez, D. Zhdanov, On the prevention of fraud and privacy exposure in process information <sup>fl</sup>ow, INFORMS Journal on Computing 24 (3) (2012) 416–432.

[5] J. Barkley, Application engineering in health care, in: Proceedings of the 2nd Annual CHIN Summit, 1995.

[6] R.C. Barrows, P.D. Clayton, Privacy, con<sup>fi</sup>dentiality, and electronic medical records, Journal of the American Medical Informatics Association 3 (2) (1996) 139–148.

[7] R. Bose, Knowledge management-enabled health care management systems: capabilities, infrastructure, and decision-support, Expert Systems with Applica tions 24 (1) (2003) 59–71.

[8] F.M. Bowens, P.A. Frye, W.A. Jones, Health information technology: integration of clinical work<sup>fl</sup>ow into meaningful use of electronic health records, Perspectives in Health Information Management (1–18) (Fall 2010)

[9] Claus Bovens, Ramayva Krishnan, Rema Padman, On Privacy-Preserving Access to Distributed Heterogeneous Healthcare Information, in: In Proceedings of the Proceedings of the 37th Annual Hawaii International Conference on System Sciences (HICSS'04) - Track 6 - Volume 6 (HICSS '04), Vol. 6, IEEE Computer Society, Washington, DC, USA, 2004, p. 60135.

[10] C.J. Bussler, Policy resolution in work<sup>fl</sup>ow management systems, Digital Technical Journal 6 (4) (September 1994) 26–49.

[11] C. Clifton, M. Kantarcioglu, A. Doan, G. Schadow, J. Vaidya, A. Elmagarmid, D. Suciu, Privacy-preserving data integration and sharing, in: The 9th ACM SIGMOD Workshop on Research Issues in Data Mining and Knowledge Discovery (DMKD'04), 2004, pp. 19–26.

[12] A. Colantonio, R.D. Pietro, A. Ocello, N.V. Verde, A new role mining framework to elicit business roles and to mitigate enterprise risk, Decision Support Systems 50 (4) (2011) 715–731.

[13] E.J. Coyne, Role engineering, in: C.E. Youman, R.S. Sandhu, E.J. Coyne (Eds.), Of the First ACM Workshop on Role-based Access Control (RBAC'95), Number 4, ACM, New York, NY, 1996.

[14] G.J. de Moor, B. Claerhout, F. de Meyer, Privacy enhancing technologies: the key to secure communication and management of clinical and genomic data, Methods of Information in Medicine 42 (2003) 148–153.

Table C.12  
Service rates and skill quali<sup>fi</sup>cations for each employee and each task in the work<sup>fl</sup>ow (orders/h).

<table><tr><td></td><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td><td>T6</td><td>T7</td><td>T8</td><td>T9</td><td>T10</td><td>T11</td><td>T12</td><td>T13</td><td>Skills</td></tr><tr><td>E4</td><td>14.0</td><td>9.0</td><td>9.0</td><td>3.0</td><td>4.0</td><td>0.0</td><td>0.0</td><td>15.0</td><td>10.0</td><td>9.0</td><td>11.0</td><td>0.0</td><td>0.0</td><td>P</td></tr><tr><td>E1</td><td>25.0</td><td>25.0</td><td>25.0</td><td>25.0</td><td>25.0</td><td>0.0</td><td>25.0</td><td>0.0</td><td>25.0</td><td>25.0</td><td>25.0</td><td>0.0</td><td>0.0</td><td>N</td></tr><tr><td>E3</td><td>13.0</td><td>11.0</td><td>11.0</td><td>0.0</td><td>0.0</td><td>7.0</td><td>5.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>13.0</td><td>0.0</td><td>0.0</td><td>T</td></tr><tr><td>E6</td><td>12.0</td><td>10.0</td><td>10.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>8.0</td><td>12.0</td><td>8.0</td><td>0.0</td><td>S</td></tr><tr><td>E5</td><td>18.0</td><td>9.0</td><td>9.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>8.0</td><td>18.0</td><td>8.0</td><td>0.0</td><td>S</td></tr><tr><td>E7</td><td>17.0</td><td>9.0</td><td>9.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>17.0</td><td>10.0</td><td>16.0</td><td>A</td></tr><tr><td>E2</td><td>21.0</td><td>21.0</td><td>21.0</td><td>21.0</td><td>21.0</td><td>0.0</td><td>21.0</td><td>0.0</td><td>21.0</td><td>21.0</td><td>21.0</td><td>0.0</td><td>0.0</td><td>N</td></tr></table>

[15] G.T. Duncan, D. Lambert, Disclosure-limited data dissemination (with discussion), Journal of the American Statistical Association 81 (1986) 10–28.

[16] G.T. Duncan, D. Lambert, The risk of disclosure of microdata, Journal of Business and Economic Statistics 7 (1989) 207–217.

[17] A. Ferreira, R. Cruz-Correia, L. Antunes, P. Farinha, E. Oliveira-Palhares, D.W. Chadwick, A. Costa-Pereira, How to break access control in a controlled manner, in: Proceedings of the 19th IEEE Symposium on Computer-Based Medical Systems (CBMS'06), IEEE Computer Society, Washington, DC, 2006, pp. 847–854.

[18] S.E. Fienberg, U.E. Makov, R.J. Steele, Disclosure limitation using perturbation and related methods for categorical data (with discussion), Journal of Of<sup>fi</sup>cial Statistics 14 (1998) 485–512.

[19] R.J. Gallagher, S. Sengupta, G. Hripcsak, R.C. Barrows, P.D. Clayton, An audit server for monitoring usage of clinical information systems, in: 1998 American Medical Informatics Association Annual Symposium (AMIA), 1998, p. 1002.

[20] M.R. Garey, D.S. Johnson, Computers and Intractability: A Guide to the Theory of NP-Completeness, W.H. Freeman and Company, 2002.

[21] R. Gar<sup>fi</sup>nkel, R.D. Gopal, P.B. Goes, Privacy protection of binary con<sup>fi</sup>dential data against deterministic, stochastic, and insider threat, Management Science 48 (2002) 749–764.

[22] G. Goncalves, A. Poniszewska-Maranda, Role engineering: from design to evolution of security schemes, Journal of Systems and Software 81 (8) (August 2008) 1306–1326.

[23] D. Gritzalis, A baseline security policy for distributed healthcare information systems, Computers & Security 16 (8) (1997) 709–719.

[24] D. Gross, J.F. Shortle, J.M. Thompson, C.M. Harris, Fundamentals of Queueing Theory, fourth edition John Wiley & Sons, Inc., New York, 2008.

[25] J. Gulcher, K. Kristjansson, H. Gudbjartsson, K. Stefansson, Protection of privacy by third-party encryption in genetic research, European Journal of Human Genetics 8 (2000) 739–742.

[26] B. Guttman, E.A. Roback, An Introduction to Computer Security. The Nist Handbook, Diane Pub Co., 1995.

[27] F. Hansen, V. Oleshchuk, Spatial role-based access control model for wireless networks (2003), in: Proceedings of the 58th IEEE Vehicular Technology Conference (VTC'03), volume 3, IEEE Computer Society, 2003.

[28] J.V. Hansen, P.B. Lowry, R.D. Meservy, D.M. McDonald, Genetic programming for prevention of cyberterrorism through dynamic and evolving intrusion detection, Decision Support Systems 43 (4) (2007) 1362–1374.

[29] Q. He, A.I. Antón, A framework for modeling privacy requirements in role engineering, in: International Workshop on Requirements Engineering for Software Quality (REFSQ 2003), Klagenfurt, Austria, June 16–17 2003.

[30] HIPAA, Standards for privacy of individually identi<sup>fi</sup>able health information. 45 C.F.R. Parts 160 and 164, in: Health Insurance Portability and Accountability Act (HIPAA), 2002.

[31] H.R. 1 (111th): American Recovery and Reinvestment Act of 2009. http://www. govtrack.us/congress/bills/111/hr1.

[32] J. Hu, A.C. Weaver, A dynamic, context-aware security infrastructure for distributed healthcare applications, in: Proceedings of Pervasive Security, Privacy and Trust (PSPT2004), Boston, MA, August 2004.

[33] W. Hummer, P. Gaubatz, M. Strembeck, U. Zdun, S. Dustdar, An integrated approach for identity and access management in a SOA context, in: Proceedings of the 16th ACM Symposium on Access Control Models and Technologies (SACMAT), Innsbruck, Austria, June 2011.

[34] P.C.K. Hung, Towards a privacy access control model for e-healthcare services, in: The Third Annual Conference on Privacy, Security and Trust, October, 2005.

[35] ISACA, Control Objectives for Information and Related Technology (COBIT), ISACA & IT Governance Institute, 2007.

[36] B. Kaplan, Evaluating informatics applications—clinical decision support systems literature review, International Journal of Medical Informatics 64 (1) (2001) 15–37.

[37] Y. Lu, Y. Xiao, A. Sears, J. Jacko, A review and a framework of handheld computer adoption in healthcare, International Journal of Medical Informatics 74 (5) (2005) 409–422.

[38] Y.A. Lussier, R. Williams, J. Li, S. Jalan, T. Borlawsky, E. Stern, I. Kohli, Partitioning knowledge bases between advanced noti<sup>fi</sup>cation and clinical decision support systems, Decision Support Systems 43 (4) (2007) 1274–1286

[39] S.T. Mohajer, Former UCLA Hospital Worker Admits Selling Records, Associated Press, 2008. Available at www.breitbart.com/article.php?id=D94Q8LJ80&show\_article=1.

[40] M. Nunez, R. Gar<sup>fi</sup>nkel, R.D. Gopal, Stochastic protection of con<sup>fi</sup>dential information in statistical databases: a hybrid of query restriction and data perturbation, Operations Research 55 (2007) 890–908.

[41] G. Pallapa, N. Roy, S. Das, Precision: privacy enhanced context-aware information fusion in ubiquitous healthcare, Software Engineering for Pervasive Computing Applications, Systems, and Environments 10 (2007) 20–26.

[42] L. Portnoy, E. Eskin, S. Stolfo, Intrusion detection with unlabeled data using clustering, in: Of ACM CSS Workshop on Data Mining Applied to Security (DMSA-2001), 2001.

[43] K Price. Host-based misuse detection and conventional operating systems’ audit data collection. Master's Thesis, Purdue University, 1997.

[44] S. Rehm, S. Kraft, Electronic medical records: the FPM vendor survey, Family Practice Management 8 (1) (2001) 45–54

[45] J.F. Reid, I. Cheong, M.P. Henricksen, J. Smith, A novel use of RBAC to protect privacy in distributed health care information systems, in: R. Safavi-Naini, J. Seberry

(Eds.), Proceedings of 8th Australasian Conference on Information Security and Privacy (ACISP 2003), Wollongong, July 9–11 2003.

[46] R. Sandhu, D. Ferraiolo, R. Kuhn, The NIST model for role-based access control: towards a uni<sup>fi</sup>ed standard, in: Proceedings of the Fifth ACM workshop on Role-based Access Control (RBAC '00), ACM, New York, NY, USA, 2000. pp. 47–63.

[47] J. Stanton, K. Stam, P. Mastrangelo, J. Jolton, Analysis of end user security behaviors, in: Computers & Security, 2005, pp. 124–133.

[48] M. Tentori, J. Favela, M.D. Rodriguez, Privacy-aware autonomous agents for pervasive healthcare, Intelligent Systems, IEEE 21 (6) (2006) 55–62.

[49] W. Tolone, T. Pai, G.J. Ahn, S.P. Hong, Access control in collaborative systems, ACM Computing Surveys 37 (1) (March 2005) 29–41.

[50] P.M. Vieira-Marques, S. Robles, J. Cucurull, R.J. Cruz-Correia, G. Navarro, R. Marti, Secure integration of distributed medical data using mobile agents, Intelligent Systems, IEEE 21 (6) (2006) 47–54.

[51] C. Vroom, R. von Solms, Towards information security behavioural compliance, Computers & Security 23 (3) (2004).191-198

[52] J. Wainer, P. Barthelmess, A. Kumar, W-RBAC — a work<sup>fl</sup>ow security model incorporating controlled overriding of constraints, International Journal of Cooperative Information Systems 12 (4) (2003) 455–485.

[53] W.T. Yue, M. Çakanyıldırım, A cost-based analysis of intrusion detection system con<sup>fi</sup>guration under active or passive response, Decision Support Systems 50 (1) (December 2010) 21–31.

[54] X. Zhao, M.E. Johnson, Access governance: <sup>fl</sup>exibility with escalation and audit, in: Proceedings of 43rd Hawaii International Conference on System Sciences, 2010, pp. 1–13.

[55] H. Zo, D.L. Nazareth, H.K. Jain, Security and performance in service-oriented applications: trading off competing objectives, Decision Support Systems 50 (1) (2010) 336–346.

Dr. Xue Bai is an Associate Professor of Management Information Systems in the Department of Operations and Information Management, University of Connecticut. She received her Ph.D. degree in Management Information Systems from Carnegie Mellon University. Her research interests include mathematical modeling for managing data quality and information security related risks in enterprise information systems. Another of her research interests is in the area of data mining and data analytics methods applied to business and healthcare domains. Her work has appeared in Information Systems Research, INFORMS Journal on Computing, Decision Support Systems, among others.

Dr. Ram D. Gopal is GE Capital Endowed Professor of Business and Head of the Department of Operations and Information Management. His current research interests are in the areas of business analytics, information security, privacy and valuation, intellectual property rights, online market design and business impacts of technology. His research has appeared in Management Science, Operations Research, INFORMS Journal on Computing, Information Systems Research, Journal of Business, Journal of Law and Economics, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, Journal of Management Information Systems, Decision Support Systems, and other journals and conference proceedings. He serves on the editorial board of Information Systems Research, Journal of Database Management, Information Systems Frontiers, and Journal of Management Sciences.

Dr. Manuel Nunez received a B.S. in mathematics and computer science and an M.S. in mathematics from the Universidad de Costa Rica in 1986, 1987, and 1993, respectively, an M.S. in operations research and computer science and the Engineer degree in operations research from Stanford University in 1989, 1990, and 1991, respectively, and a Ph.D. in operations research from the Massachusetts Institute of Technology in 1997. Since 2007, he has been an Associate Professor of operations management at the Department of Operations and Information, University of Connecticut. He has published for Mathematical Programming, SIAM Journal on Optimization, Operations Research INFORMS Journal on Computing, INFORMS Information Systems Research, IEEE Transactions on Systems, Man, and Cybernetics, and IEEE Transactions on Engineering Management. His primary work and research is in the application of optimization and stochastic methods in the <sup>fi</sup>elds of operations and information management.

Dr. Dmitry Zhdanov is an Assistant Professor in the Operations and Information Management Department at the School of Business, University of Connecticut. He received his Ph.D. degree from the University of Minnesota in 2007. His research has been published in leading management journals such as MIS Quarterly, Information Systems Research and INFORMS Journal on Computing. He serves as an Area Editor of Electronic Commerce Research and Applications and is also a Certi<sup>fi</sup>ed Information Systems Security Professional (CISSP). His research interests include information security and privacy, large-scale data analysis, design of intelligent agents and social impacts of information technology.
