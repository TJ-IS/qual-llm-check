---
otero_id: 17723
otero_key: "9C62NAGA"
title: "Using query-driven simulations for querying outcomes of business processes"
authors: "P. Balasubramanian; Alexander Tuzhilin"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00025-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using query-driven simulations for querying outcomes of business processes

P. Balasubramanian $^{a,1}$ , Alexander Tuzhilin $^{b}$

$^{a}$ Management Information Systems Department, School of Management, Boston University, Boston, MA 02215, USA $^{b}$ Information Systems Department, Leonard N. Stern School of Business, New York University, New York, USA

## Abstract

When decision makers want to know outcomes of business processes in their organizations, they often use simulations to do this. Traditionally, this is achieved by running simulations, collecting statistics and answering questions of interests to the decision makers based on the collected statistics. This paper describes an alternative approach to simulations, called the Query-Driven Simulations (QDS) approach, in which the user first asks the queries of interest and then, depending on the query asked, appropriate simulations are run to answer that query. The QDS approach empowers the end-user by making it easier, faster, and more reliable to ask ad-hoc questions about outcomes of business processes than what is done in traditional simulations. To substantiate this point, the paper describes the types of questions decision makers ask about outcomes of business processes and studies how easy it is to express these questions in terms of an SQL-like query language SimQL designed for Query-Driven Simulations. In addition, a case study of using the QDS approach in a manufacturing application developed by a major management consulting company is presented and the QDS approach is tested on that application.

Keywords: Decision support; Query-driven simulations; Discrete-event simulations; Databases; Query languages; Modeling lifecycle

## 1. Introduction

Throughout their daily activities, decision makers ask different questions about future outcomes of business processes running within their organizations. The information they obtain by asking these questions helps them make planning, control, and staffing decisions. For example, a foreman in a manufacturing facility may want to know how many parts will be produced within the next shift, so that he or she can notify the distribution department beforehand, and the distribution department can determine how many trucks will be needed to carry these parts. In a mail order company, a salesperson may want to know if it is possible to deliver a customer order within 2 weeks. The salesperson can use this information to promise the customer the delivery date that is earlier than the regular delivery date under the current 3-to-4 weeks delivery policy. In the banking industry, a manager may want to know how many tellers will the new branch need so that appropriate hiring decisions can be made.

The problem of predicting the future outcomes of business processes has certainly been addressed before, mainly within the framework of Operations Research and Management Science. In particular, mathematical models of business processes are built by model developers who also try to find analytical solutions to these models. If an analytical solution can be found, then the behavior of the model is well understood. However, in complex industrial and organizational settings it is often difficult to find analytical solutions to these models. Hence we have to resort to techniques like simulation to capture the inherent complexity of such systems $[32]$ .

To answer questions such as the ones presented above about simulation models, these models are executed many times and summary statistics about individual runs are collected in one of the following two ways. In the first approach, summary statistics are computed inside the simulation program, and the program produces the final results to the user. In the second approach, various simulated events are recorded in the trace files $^{2}$ , and then statistics are collected from these trace files by either writing programs in one of the programming languages, such as Fortran or C, or by using one of the statistical packages, such as SAS [31]. In both cases, if a user wants to find some additional summary statistics about the model not a priori produced by the model, he or she has to know simulation languages, programming languages and/or statistical packages in order to make appropriate changes to the programs and be able to gather statistics.

Since most of the people who ask questions about future outcomes of business processes in their organizations, such as a foreman, a salesman, or a bank manager, do not know much about simulations, programming languages, or statistical packages, they cannot ask ad-hoc questions about future outcomes of their business processes as the questions arise “on-the-fly”. Instead, they have to rely on the systems developed by their information systems departments that support a fixed set of “canned” questions. Clearly, this situation is unsatisfactory in many organizations, such as manufacturing, transportation, or in the military, where various users want to ask many different questions about simulation outcomes of various models.

In this paper, we describe the Query Driven Simulations (QDS) approach that addresses this problem. In the QDS approach the user first asks a query about outcomes of simulations expressed in a declarative query language, and then, depending on the query asked, different simulations are run in order to answer it. After simulations are finished, the query specified by the user is evaluated on the trace files generated by simulations. Simulations are query-driven because the QDS system traces only those events that are necessary to answer the query. For example, assume a foreman wants to know who many parts will be manufactured within the next 8 hours based on the model Manufacturing-Model-2 that simulates manufacturing processes in the plant where the foreman works. According to the QDS approach, it should be determined first what events in the Manufacturing-Model-2 should be traced and for how long in order to answer the query (i.e., the event Finished (Part, Time), specifying which parts are finished and when, should be traced for 8 hours of simulated time). Then simulations are run for that amount of time and designated events (i.e., Finished (Part, Time)) are recorded in the trace files that are stored in a temporal database $^{3}$ [37]. The query is then evaluated on these trace files.

Besides describing the QDS approach, we also explain in which applications, how, and by whom the QDS approach can be used and also explain its advantages. In particular, we argue that the QDS approach provides a more declarative, flexible and interactive way for asking questions about simulation outcomes than the more traditional approaches. For these reasons, the QDS approach allows organizations to bring simulations from the “back office” of the simulation specialist to the “front office” of the end-user. To illustrate how the QDS approach works in practice, we also present a case study where QDS was successfully used in a manufacturing application developed by the management consulting company of Booz-Allen and Hamilton.

Query languages in the context of simulations were studied before. In [40,41], the idea of asking queries on simulation traces was proposed, and a SimTL language was presented. SimTL consists of the simulation and the querying components. The simulation component is based on a temporal logic programming language, and the querying component is based on temporal logic [26]. The queries about simulation outcomes expressed in temporal logic are asked about simulations generated by temporal logic programs. This means that SimTL is a tightly coupled simulation and querying system, in which both components depend on the formalism of temporal logic. Using temporal logic in querying and simulation components makes this approach to asking queries on simulation outcomes very declarative. However, it is also important to be able to ask questions on simulation models written in simulation languages other than the ones based on temporal logic. In addition, it is important to incorporate stochasticity into Sim TL. Therefore, we address these two issues in the QDS approach.

In [27], Miller and Weyrich developed the SIMODULA system that has its own SQL-like query language (with object-oriented features added to it) for asking questions about simulations. Each model has a relation of input parameters and outcomes of previously executed simulations associated with that model. For example, a banking model may have a BankScenario relation associated with it that has input parameters, such as number of tellers, mean interarrival rate, mean service time, and the output parameters, such as throughput and the service time, as its attributes. If the user wants to ask a question about throughput and average waiting time for the banking model with input parameters mean interarrival rate being 4.0, mean service time being 6.0 and the number of tellers equal to 2, then SIMODULA checks in the BankScenario relation if this model has been run before. If it has, it retrieves the answer from relation BankScenario (values of attributes Throughput and AverageWaitingTime). Otherwise, SIMODULA launches the simulation with the input parameters retrieved from the query and the rest of them set to defaults.

In this paper we present a more extensive approach to Query-Driven Simulations by allowing SimQL queries to drive simulations (trace only the necessary events) and not just launch (trace all events) them. We also allow the user to query simulation traces in an ad-hoc manner instead of letting him/her ask a fixed set of questions on summary statistics. Finally, we allow a loose coupling between various database query languages and simulation languages as long as trace files generated by simulation programs conform to a certain standard.

In [35], Snodgrass presents a relational approach to monitoring performance of complex systems. The user monitors performance of such systems by asking questions expressed in a temporal query language TQuel [34]. Since the approach presented in [35] is mainly targeted to the monitoring of operating systems and since all the events that can possibly occur in such a system are not known in advance, [35] proposes to restrict the monitoring process to only those events that the user specifies in advance before the monitoring activities start. This is accomplished in [35] by using sensors. A sensor is a piece of code written in the specification language developed by Snodgrass [35], and it is embedded by the user inside the system being monitored to keep track of one specific type of event.

The work presented in $[35]$ is one of the first works on querying the data that is not explicitly stored in a database and had a profound influence both in the monitoring and in the temporal database literature. However, this work has been primarily targeted towards operating systems, and therefore it has to be extended in the following three ways in order to be applied to simulations. First of all, it does not support stochasticity and therefore has to be extended in this respect. Secondly, the approach in $[35]$ is not completely query-driven because the user has to place sensors manually inside the program. In contrast to this, the QDS approach is completely query-driven and does not require any user intervention. Finally, the approach presented in $[35]$ is tightly coupled since it supports only TQuel queries on outputs generated only by sensors specified only in the specification language of Snodgrass. In this paper, we will show how the QDS approach eliminates all these three restrictions.

The rest of the paper is organized as follows. We will start with the analysis of the types of questions decision makers typically ask about outcomes of business processes in Section 2. In Section 3, we explain the very idea of QDS and compare it with the traditional approach. To demonstrate how the QDS approach works in practice, we implemented a QDS system Cassandra $^{+}$ . We describe the architecture and the implementation of Cassandra $^{+}$ in a separate paper [3]. However, to make this paper self-contained, we briefly describe Cassandra $^{+}$ in Section 4. In Section 5, we present a case study of using the QDS approach in a manufacturing application developed by the management consulting company of Booz-Allen and Hamilton. The different ways that can be used to translate an end-user query into SimQL queries are described in Section 6. Finally, in Section 7 we describe the Query-Driven Modeling Lifecycle that specifies the process of development, installation, usage, and modification of simulation models based on the QDS approach.

## 2. Types of questions decision makers ask about outcomes of business processes

The types of questions decision makers ask about outcomes of business processes vary significantly across different industries, organizations within an industry, functional units within an organization, and levels of management within a functional unit. These questions also vary depending on whether the question is about possible outcomes of business processes that are currently running in real-time (e.g., how many parts will be manufactured in the next shift?) or about some hypothetical business process (e.g., what will the average cost of producing new product be?). We will call the first type of questions on-line or real-time, and the second one we will call off-line. Furthermore, questions can vary depending on whether they are asked about the present state of the system, about the past, or about the future state of the system. Questions about the future, can be of predictive or evaluative nature (e.g., could we fulfill Order-5 (assuming it was not) if we use FIFO queuing discipline as opposed to the LIFO discipline we used over the last month).

In this section, we consider a manufacturing organization and describe the types of questions decision makers within such an organization may want to ask about the future outcomes of various processes in this organization. We choose a manufacturing example for the following reasons. First, there has been much interest developed in the last several years in applying information technologies for solving manufacturing problems $[30,2,29]$ . Second, simulations are widely used in manufacturing $[23,10,24]$ thus making it a good application for testing our ideas. Finally, as we show later in this section, various people in a manufacturing organization want to ask many different questions about future outcomes of manufacturing processes. Also, we decided to consider questions only about the future because these questions are of great interest to decision makers and because answering these questions requires running simulations.

We divide the questions manufacturing people want to ask about outcomes of manufacturing activities into several groups according to the standard classification of $[17]$ as presented in Fig. 1. As Fig. 1 shows, the decision makers are grouped based on the functional units they belong to and based on the level in the organizational structure to which they belong.

For each group of people in Fig. 1, we describe the kinds of questions about outcomes of business processes in which they are mostly interested. Because of the space limitation, we provide examples of questions only to some of the cells in Fig. 1. Additional questions for each category can be found in [4]. These questions were obtained from the literature [8,38,33,39], and through extensive discussions with manufacturing professionals [14,43,28,20]. We assume that the questions presented below are real-time predictive questions, unless stated otherwise.

![](/api/attachments/9C62NAGA/fulltext/images/ee7d03bb26e49b903a3f6aa03eb778e2a53fb79cd16f3c7f53a4dfb8c8484522.jpg)  
Fig. 1. A classification of questions arising within organizations.

Cell-1 (Production department — Operational level): In this class of queries, decision makers are interested in asking questions about production targets, quality assurance, job priority assignment, machine utilizations, raw-material availability, set-up time, work-flow co-ordination, and so on. Below, we provide examples of some of the typical questions different operations people may want to ask.

Foreman — How many jobs will be produced in the next shift?

Foreman — Which machines will have an utilization ratio of more than 90% during the next shift?

Manager — When should component-1 be delivered to station-A so as to complete assembly of unit PJ-352 on time?

Foreman — Where will Job-5 be 5 hours from now?

Manager — Will Job-5 be completed on time if we give it the highest priority?

Quality Control Engineer — How many jobs will be rejected in the next batch?

Manager — Could we have fulfilled Order-5 (assuming it was not) if we had used FIFO queuing discipline instead of LIFO discipline that we used over the last month? (evaluative)

Cell-2 (Finance/Accounting department — Operational level): These queries are asked to help decision makers in finance department manage their cash flow and for accountants to see if the manufacturing costs are under control and to ascertain costs of manufacturing new products.

Cell-3 (Sales / Marketing department — Operations level): Queries in this class are used to help the salesman to answer questions about customer order processing, delivery speed-up, etc. These questions will also help a salesman determine if a particular customer request can be met on time, track the status of a customer order and to see which customer requests can be met. The marketing manager at the operations level is interested in manufacturing and delivery times of products and flexibility in delivery schedules. Some typical questions sales and marketing managers may want to ask are:

Salesman — Is it possible to complete Job-5 in 8 hours?

Salesman — What will be the cost of fulfilling the Order-5 if it is completed using the least priority?

Salesman — How long will it take to complete Order-5 if we add optional Feature-1?

Brand manager — If the actual demand for 1 liter bottles of the soft drink A is 7% larger than the forecasted demand for these bottles, then how fast will the manufacturing department be able to meet this increased demand?

Cell-4 (Human Resources department — Operations level): The queries that can be listed in this cell help human resources department make staffing decisions. This will ensure that manpower is available to meet order requirements.

Cell-5 (Production department — Tactical level): Production middle managers may want to ask questions about future outcomes of manufacturing processes to make better production planning decisions. These questions help to ensure that production, utilization and various other targets are met. Capacity planning, workflow redesign and coordination decisions are also addressed by these questions. Some typical questions production middle managers may want to ask are:

Manager — What will be the machine utilization ratios for the various plants for the next shift?

Manager — What should the lot size be to satisfy our future demand profile at the minimum cost? (optimization)

Manager — Which of the four scheduling heuristics will help meet the target production of 100 jobs in 8 hours?

Plant Manager — How will throughput be affected if I rearrange my factory?

Plant Manager — Can I reduce my Work-In-Process (WIP) by reducing set-up times?

Manager — Among the four workshop configurations which one delivers the maximum through-put? (off-line)

Cell-6 (Finance/Accounting department — Tactical level): Financial and accounting middle managers ask the questions in this group in order to make budgeting decisions and ensuring that production costs are under control. They can also be used for performing sensitivity analysis of costs.

Cell-7 (Sales / Marketing department — Tactical level): Marketing managers are interested to know how much time it will take to manufacture new products or modify existing products to meet customer demand. They are also interested in the promotion planning questions.

Cell-8 (Human Resources department — Tactical level): As in Cell-4 such questions are helpful in making staffing and training decisions. In this case however, equipment purchase decisions are made along with staffing decisions. This quadrant should also handle questions that help negotiate pay scales with unions.

Manager — Is our manpower sufficient to meet the production schedule for the next quarter?

Manager — How many employees have to be trained in the new methodology?

Manager — If we had fixed the pay rates of Class A employees at \$X per hour for 2 years and new recruits at \$Y per hour, would we have made better return on investment for plant A? (evaluative)

Manager — How many people experienced in programming CNC machines have to be recruited?

Cell-9 (Production department — Strategic level): Senior management in operations typically asks questions about operations that have a long-term impact on the company, such as business process re-engineering or make-versus-buy questions.

Cell-10 (Finance / Accounting — Strategic level): Senior management in Finance and Accounting asks budgeting and process redesign questions having long-term impact on the organization.

Accountant — What does my invoicing process really look like, and where can improvements be made to minimize processing delays in our new plant?

Accountant — What will the break-up of expenses be when our new plant is opened in Latin America in 6 months?

Finance Manager — In which plants can budget cuts be enforced to reduce total production cost by 10%?

Finance Manager — How will NAFTA affect our revenues and profits?

Cell-11 (Sales / Marketing — Strategic level): Examples of questions asked by senior sales and marketing managers are long term budget allocation and market share estimation questions.

Cell-12 (Human Resources — Strategic level): A Senior Human Resources Manager asks questions that help him or her make long-term staffing, training, and promotion decisions.

Human Resource Director — How drastically will the shortage of qualified personnel affect the output in our Latin American Plant?

Human Resource Director — What will be the total training cost for running the Mexican Plant?

Human Resource Director — What should the hiring pattern be for next year?

To answer questions such as the ones presented above simulations are often used. By repeatedly running simulations of the manufacturing processes, summary statistics are collected that help answering questions that the user has about the system. These summary statistics are usually collected in one of the following two ways. In the first approach, summary statistics are computed inside the simulation program, and the program presents these statistics to the user. The main problem with this approach is that the end-user has to modify the program if he or she wants to ask a question about simulation outcomes that goes beyond the set of statistics generated by the program $^{4}$ . For example a simulation program may output the total time spent in the system (makespan) for a job but the user may want a breakup of the time spent in the queue, in transit and in process. In order to get this information, the user has to change the simulation program to collect different statistics. In the second approach, various simulated events are recorded in the trace files, and then statistics are collected from these trace files by either writing programs in a programming language, such as Fortran or C, or by using a statistical package, such as SAS [31]. We will call this traditional approach to simulations, encompassing the two described methods, simulate-and-gather-statistics (SAGS) approach.

Since most of the people who ask questions about future outcomes of business processes in their organizations, such as a foreman, a salesman, or a bank manager, do not know much about simulations, programming languages, or statistical packages, it is hard for them to use the SAGS approach to obtain answers to the ad-hoc questions as they arise in user's minds "on-the-fly". Instead, the users have to rely on the simulation specialists for providing answers to their questions. In the next section, we present an alternative approach to simulations that makes it easier for the users to get answers to their questions.

## 3. Query-Driven Simulations

Query-Driven Simulations (QDS) is an approach to simulations in which the user first asks queries about outcomes of simulations using a query language and then, depending on the query being asked, appropriate simulations are run, and only the events necessary to answer the query are recorded in the trace files. After the simulation runs are completed, the query expressed by the user is evaluated on the trace files(s) being generated by simulations. To illustrate how the QDS approach works, consider the following example.

Example 1. Assume that a foreman wants to know how many parts the manufacturing facility modeled with a simulation model M will produce within the next 8 hours (we denote this query as Q). Also, assume that the foreman wants to have an error of estimation of the answer to be within 10% of the mean and have this answer with confidence 95%. Since query Q deals with time, it can be expressed in some temporal query language, such as TQuel [34], TSQL2 [36], temporal logic [22,42], or SQL with timestamps [12]. For example, it can be expressed in temporal logic as

## $\{COUNT(Part)|within-time(8) Finished(Part)\}$

where Finished(Part) is a temporal predicate specifying events “part is finished” and within-time $(T)P$ is a bounded temporal operator [21,40] specifying that predicate P is sometimes true between now and now + T.

To evaluate query Q, one has to determine the number of simulation runs N necessary to answer the query within the bounds specified by the user (i.e., error of estimation being 10% and confidence 95%). Techniques for estimating this number in the context of the Cassandra $^{+}$ system are described in Section 4.

To answer the query for a single simulation run, we have to determine which events the simulation model M has to record in the trace file and for how long. In our case, model M has to trace all the events “part finished” generated for the next 8 hours of simulation time. Once this information (which events to trace and for how long) is passed to the simulation model M, the control is transferred to M and simulation starts (model M is being executed for 8 hours of simulation time). As a result of this execution, model M generates a trace file Tr containing all the events corresponding to the parts being finished. Then this trace file is converted into the database format and query Q is evaluated on this trace file.

To determine the answer to query Q in statistical terms, this process has to be repeated N times so that the answer would fall within the estimation parameters specified by the foreman. For example, the answer to this query could be

The average number of parts produced within the next 8 hours is $32 \pm 3$ , and we can make this statement with confidence 95%.

The process of evaluating query Q, as described in this example, is summarized in Fig. 2.

Note that in the QDS approach, a query is asked against some simulation model. This means that there should be a modelbase of the models against which queries can be asked. We describe issues such as the structure, content, and functionalities of the modelbase in [3]. Also note that in the QDS approach a query is expressed in some temporal query language and is evaluated against a temporal database containing the trace file(s) of event(s) generated by the simulation model.

The QDS system, just like traditional simulations, can be used by the decision maker for a wide variety of tasks, such as planning, design and control. In addition, the QDS approach is well-suited for answering real-time questions that deal with future outcomes of business processes that are currently running (e.g., to which machine should we send the next part?). This is achieved by integrating the past and present data collected from the actual physical processes occurring in real-time with the future data generated by simulations. Hence the QDS approach enables us to seamlessly integrate real-time data with the data generated by simulation models.

The QDS approach has the following advantages over the traditional simulate-and-gather-statistics (SAGS) approach. First, it provides a more declarative way of asking questions about outcomes of simulations than the SAGS approach. The user formulates questions in a declarative general-purpose query language that tells the QDS system what the user wants to know. If the user uses this language he/she does not have to specify how the system has to obtain the answer. In particular, the user does not have to know any simulation and statistical packages, or write any programs. Second, the QDS approach gives the user extra flexibility. The user can ask any query expressible in the query language of the QDS system (e.g., TQuel or TSQL2). This flexibility makes the end-users less dependent on the MIS department since they do not have to rely on a simulation specialist when they want to ask additional questions not supported by the information systems installed by the MIS department. Third, QDS approach is more interactive than the traditional SAGS approach. The user of the QDS system can ask queries “on-the-fly” as they arise without any help from the simulation specialist. Finally, as Example 1 illustrates, the QDS approach automatically provides statistical answers to the questions asked by the user without any extra work on his/her part. Unlike the SAGS approach, in which the user has to determine how many simulation runs are needed in order to obtain the answer within the user-specified constraints, the QDS approach does all this work for the user.

![](/api/attachments/9C62NAGA/fulltext/images/04b22fc48d0f4ae50cb469350db38c38396cdcb5f5026e987c90ae7989985a89.jpg)  
Fig. 2. Query processing in the QDS approach.

However, the QDS approach has certain limitations in comparison to the traditional SAGS approach. First of all, some of the questions expressible in the SAGS approach cannot be expressed as QDS queries. To explain why this is the case, consider a temporal query language such as TQuel, or TSQL2, or SQL with timestamps. It is well-known that SQL (and its temporal extensions) has a limited expressive power $[1]^{5}$ , and therefore, SQL queries in complex applications have to be embedded $[13]$ in some general-purpose programming languages, such as C or Cobol, in order to express complex questions. In contrast to this, the SAGS approach uses general purpose simulation languages, such as MODSIM $[6]$ , SIMSCRIPT $[9]$ , GPSS $[19]$ , and thus is more expressive than SQL and its temporal extensions, such as TQuel or TSQL2 (because these general purpose simulation languages are

Turing-complete). To solve the problem of the limited expressive power of the QDS approach, we propose the same strategy as used in SQL applications by embedding SimQL queries in a general-purpose programming language.

Another limitation of the QDS approach is that it requires generation of large trace files. In the worst case, the QDS system must trace every event occurring in the simulation model. In contrast to this, the SAGS approach can simply compute summary statistics inside the simulation model and thus generate no trace files at all. Furthermore, if the trace files are generated by the SAGS approach, the model developer has a control over the events he or she wants to trace. This means that only a small fraction of all the events may end up being recorded in the trace files in the SAGS approach. Since recording events in the trace files can slow performance of the QDS in comparison to the SAGS approach, it is important to develop query optimization techniques for QDS systems. These techniques would allow recording only those events that are necessary for answering the query. We discuss some of these techniques in the context of the Cassandra $^{+}$ system in [3]. To address the performance issues of the QDS approach, we did a case study, in which we measure the performance of a QDS system in a manufacturing application. We describe the results of this study in Section 5.

As we pointed out already, the QDS approach has several important advantages over the SAGS approach. However, this does not mean that the QDS approach should always be used instead of the SAGS approach in all the applications. In order to understand which applications are better suited for the QDS than the SAGS approach, consider the Logistics Modeling System (LMS) [15] that IBM uses as a dispatcher for its wafer fabrication manufacturing processes in its semiconductor facility near Burlington, VT.

The LMS system collects real-time transactional data about the processes occurring on the manufacturing floor and makes some lot routing decisions based on this information. To make good routing decisions, it sometimes has to predict the future outcomes of its manufacturing processes. However, there are only few questions about such future outcomes that are of interest to the LMS system. Therefore, the LMS designers have written programs to answer these questions, one program addressing one question.

However, as discussed in Section 2, in general, decision makers in manufacturing organizations have many questions about outcomes of manufacturing processes, and this makes the one-program-per-question approach less attractive. The situation becomes even more complex when an organization has multiple simulation models since a program has to be written for each question on each model in the worst case. For example, if decision makers want to ask 500 different questions against 20 different manufacturing models then it means that one has to write 10,000 programs that handle these questions in the worst case.

This discussion suggests the types of applications where Query-Driven Simulation (QDS) systems, are most useful. These applications can be measured in terms of the following two dimensions:

\- how many models are there in the modelbase,
- how many different questions users of a QDS system want to ask about these models.

The best types of applications are those where users want to ask many queries about various types of models since in this case the alternative program-per-question approach is the most expensive. The least interesting application is when there are few models and the users want to ask only few questions about simulation results since in this case the program-per-question approach is feasible.

In Section 2, we considered questions that decision makers in manufacturing organizations ask about outcomes of manufacturing processes, and showed that there are many questions of interest to them. Also, large manufacturing organizations typically have many different models describing various aspects of manufacturing [29]. Therefore, manufacturing applications fall into the “many-questions-many-models” category and, thus, provide a good application for Query-Driven Simulations. Besides manufacturing applications, we believe that military and transportation applications belong to the many-questions-many-mod els category and, therefore, are also well-suited for Query-Driven Simulations.

## 4. Overview of Cassandra $^{+}$

In this section, we describe a Query-Driven Simulation system $Cassandra^{+}$ that supports the QDS approach presented in Section 3. The full description of $Cassandra^{+}$ , including its architecture, the formal definition of its query language SimQL, and other software engineering aspects of $Cassandra^{+}$ , can be found in [3]. To make this paper self-contained, we briefly describe $Cassandra^{+}$ in this section.

Cassandra $^{+}$ is a QDS system that can ask questions about execution outcomes of various simulation models. Therefore, there is a need to store all these models in a modelbase [7] that serves as the central repository of all the information about all the simulation models maintained by the organization. For example, assume that a manufacturing organization has three manufacturing plants, PL1, PL2, and PL3 that have different manufacturing processes. Correspondingly, we need three different models, Manufacturing-Model-1, Manufacturing-Model-2, and Manufacturing-Model-3, that model manufacturing processes in plants PL1, PL2, and PL3 respectively. These models are stored in a modelbase that also contains some additional information about the features of these models, such as the name of the simulation language in which a model is written, default simulation parameters for the model, information needed to interface the query and simulation languages, such as the events that the model can trace, and whether real-time queries are allowed on the model.

Given the modelbase, the end-user can ask various queries against the models stored in the modelbase. These queries are expressed in the language SimQL that is formally defined in [3]. In this paper, we give a “flavor” of the language by presenting a couple of examples.

Example 2. Consider the query from Example 1, i.e., assume a foreman from plant PL-3 wants where FINISHED(PART,TIME) is a temporal relation specifying which parts are finished at what time.

to know how many parts will be manufactured within the next 8 hours at that plant. This query can be formulated in SimQL as:

<table><tr><td>Time:</td><td>8 hours</td></tr><tr><td>Answer-Semantics:</td><td>Numeric</td></tr><tr><td>Core-query:</td><td></td></tr><tr><td>SELECT</td><td>COUNT(PART)</td></tr><tr><td>FROM</td><td>FINISHED</td></tr><tr><td>Model-Name:</td><td>Manufacturing-Model-3</td></tr><tr><td>Error-of-Estimation:</td><td>10</td></tr><tr><td>Confidence-Coefficient:</td><td>95</td></tr></table>

This query consists of two parts: the core-query and the shell consisting of a set of parameters providing directives to Cassandra $^{+}$ on how the core query has to be integrated with the simulation module. The core-query expresses the actual question the end-user asks and is represented in this example with the SQL statement

## SELECT COUNT(PART)

## FROM FINISHED

The shell parameters in this example are Time, Answer-Semantics, Model-Name, Error-of-Estimation, and Confidence-Coefficient. The Model-Name parameter specifies the name of the simulation model from the modelbase against which the query is asked (Manufacturing-Model-3 in our example). The Time specifies for how long simulations have to be run (8 hours). The Answer-Semantics parameter specifies if the query returns a number as the answer (e.g., the number of parts produced) or a relation (as in Example 3). Depending on this parameter, Cassandra $^{+}$ returns different answers, as will be explained below. Finally, Error-of-Estimation and Confidence-Coefficient parameters specify the accuracy of the answer. A typical answer in case the Answer-Semantics parameter is Numeric would be:

The average number of parts produced within the next 8 hours is $32 \pm 3$ , and we can make this statement with confidence $95\%$ .

In this example, only five shell parameters are used. However, SimQL supports other parameters as well. This means that the other parameters were given default values by Cassandra $^{+}$ . The description of other SimQL parameters can be found in [3].

We illustrate how $Cassandra^{+}$ processes a SimQL query based on Example 2. When the user issues a SimQL query, $Cassandra^{+}$ parses the query and determines the simulation model to which the query refers (it is Manufacturing-Model-3 in our case). Then the system accesses the modelbase and retrieves all the information about the model Manufacturing-Model-3. Based on this information and on the values of Error-of-Estimation, and Confidence-Coefficient parameters, it determines the number of simulation runs N necessary to answer the query within the estimation bounds of these two parameters using the technique described below. After that, $Cassandra^{+}$ determines which events the simulation model Manufacturing-Model-3 should trace and for how long. In Example 2, $Cassandra^{+}$ will determine that only the event FINISHED should be traced, and this should be done for 8 hours. Then $Cassandra^{+}$ passes this information to Manufacturing-Model-3 together with the default simulation parameters and random seeds extracted from the modelbase and launches execution of Manufacturing-Model-3 for 8 hours, and this is done N times.

For each of the N simulation runs, Manufacturing-Model-3 produces the simulation trace of the event FINISHED. After each simulation run, Cassandra $^{+}$ converts the trace file containing the FINISHED events into the temporal relational database format so that the core query SELECT COUNT(PART) FROM FINISHED can be evaluated on relation FINISHED. Therefore, each simulation run of Manufacturing-Model-3 produces a single answer to the core query. After all N simulation runs are completed, we have N answers to the query. These answers are statistically analyzed, as described below, and the final (statistical) answer is presented to the user, as discussed in Example 2.

The number of simulation runs N needed to answer the query within the accuracy parameters specified by the user is determined incrementally as follows. First, an initial batch of runs is made and the query is answered with some degree of accuracy. If this accuracy is not sufficient, the number of runs is increased and the query is answered for the larger number of simulation runs. The process of increasing the number of simulation runs continues until the query is answered with the accuracy within the bounds specified by the user. If the accuracy specified by the user is never achieved, Cassandra $^{+}$ can provide partial answers to the query with the accuracy that is lower than the one specified by the user. The details of this process are presented in [3], and additional information about sequential run control procedures can be found in [18].

In Example 2, we used SQL with timestamps as a query language. However, other temporal relational query languages, such as TQuel, TSQL2, or temporal logic calculus [26,22], can be used instead of SQL as a core-query language. Furthermore, simulation models in the model-base can be written in any simulation language, as long as they generate the trace files in a certain relational form described in [3]. For example, Manufacturing-Model-1 can be written in MODSIM, Manufacturing-Model-2 in SIMSCRIPT, and Manufacturing-Model-3 in GPSS.

Example 3. Consider another question (question 2 from Cell-1 in Section 2) that a foreman from plant PL-2 may want to ask:

Which machines will have a utilization ratio of more than 90% during the next 10 hours?

Assume that the temporal relation MACHINE describes the status of the machines. It has the form MACHINE(ID,STATUS,FROM,TO) specifying that a certain machine has a certain status from time FROM until time TO. Then this query can be expressed in SimQL as $^{6}$ :

<table><tr><td>Time:</td><td>10 hours</td></tr><tr><td>Answer-Semantics:</td><td>Relational</td></tr><tr><td>Core-query:</td><td></td></tr><tr><td>SELECT</td><td>ID</td></tr><tr><td>FROM</td><td>MACHINE</td></tr><tr><td>WHERE</td><td>STATUS = ‘busy’ AND$NOW &lt; FROM ANDTO &lt; $NOW + 10hours</td></tr><tr><td>GROUP-BY</td><td>ID</td></tr><tr><td>HAVING</td><td>SUM(TO-FROM) /10hours &gt;90%</td></tr><tr><td>Model-Name:</td><td>Manufacturing-Model-2</td></tr><tr><td>Error-of-Estimation:</td><td>10</td></tr><tr><td>Confidence-Coefficient:</td><td>95</td></tr></table>

The core query in this SimQL query retrieves, for a single simulation run, those tuples from the relation MACHINE that have status busy and whose validity time interval ([FROM,TO]) lies between NOW and 10 hours from NOW. To determine the utilization of a machine between NOW and NOW + 10, we have to sum, for each machine ID, the validity intervals of all the tuples for this machine that have STATUS = busy and then divide this sum by 10 hours. This is the expression in the HAVING clause of the SQL statement (SUM(TO-FROM)/10hours). Then, we want to retrieve only those machines that have this number >90%, and we specify this condition in the HAVING clause.

Unlike the query from Example 2, this query returns a set of machine IDs (having utilizations greater than 90%). The meaning of the Relational value of Answer-Semantics parameter in the query is that we are interested in the most likely scenario as the answer to the query. For instance, if we did N simulation runs to answer the query, we want to know which answer to the core query was returned most often among these N runs. A typical answer for this query can be

The most likely answer for this query is $\{Machine-23, Machine-12, Machine-17\}$ , and it is returned with probability $36\% \pm 3\%$ and confidence level of 95%.

This means that in the most likely scenario only machines Machine-23, Machine-12, Machine-17 have utilization ratios over 90%, and the probability of this scenario is $36\% \pm 3\%$ with confidence 95%.

Alternatively, the foreman may want to have a different type of answer to the query. In particular, the foreman may want to know what is the chance that each machine has the utilization ratio of 90% or more, and he or she may want to know this answer for two most likely machines. In this case, the query should have the parameter Answer-Semantics to be set to the value Tuple, and the additional parameter Number-of-answers = 2 should be added to the query. A typical answer for this (modified) query can be

The most likely machine to have utilization more than 90% is Machine-23 (with probability $57\% \pm 3\%$ ), and the second most likely machine is Machine-17 (with probability $42\% \pm 2\%$ ).

Thus, SimQL supports Relational and Tuple semantics as answers to non-numeric queries (queries returning relations as answers), and these semantics are complimentary to each other. It is up to the user to decide which semantics he or she wants to use in the query. These two types of semantics and the differences between them are discussed further in [3].

To answer some of the SimQL queries, simulation models may have to be run forever. For example, the query “When will Job-1 be finished?” may require the corresponding simulation model to be simulated for an indefinite amount of time and, in theory, forever if Job-1 never leaves the system. Cassandra $^{+}$ prevents this situation by requiring an upper bound on the simulation time. This, essentially, means that the Cassandra $^{+}$ system processes the query that is slightly different from the core query specified by the user. For example, if the user specifies the time parameter Time = 10 hours in the previously stated query, then the modified query that Cassandra $^{+}$ processes is “When will Job-1 be finished within the next 10 hours?” This modified query requires only 10 hours of simulation time to answer it.

Among other important features of SimQL, not discussed in this paper, is the support for queries about the past, support for the off-line queries (discussed in Section 2), and the support for experimental design (when the user can ask a query about models with different values of parameters). Description of these features and their implementation in Cassandra $^{+}$ can be found in [3].

## 5. Case study: Using Cassandra $^{+}$ in a manufacturing application

As a testbed for Cassandra $^{+}$ , we used a simulation model of a manufacturing facility developed by the management consulting company of Booz-Allen and Hamilton for an aircraft manufacturer that was planning to establish an in-house surface treatment facility for the aircraft parts used in the assembly process. The objective of Booz-Allen in this engagement was to help the manufacturer design and understand such a production facility and to make sure that the facility had the necessary capacity to meet the demands of the assembly line.

To achieve this goal, two alternative manufacturing model layouts of the surface treatment facility are to be considered, a single process line model and a two process line model, and it has to be decided which layout is better than the other. In both the two process line and the one process line models, the steps involved in the surface treatment process of aircraft parts were the same and included such steps as vapor degreasing, alkaline degreasing, cold washing, demineralising, penetrant application, deoxidation, hot drying, oxidation, shot peening etc. The difference between the two models was only in the layout and the number of treatment tanks.

In this project, Booz-Allen's consultants had one major strategic question (corresponding to Cell-9 in Fig. 1): which of the two alternative layouts is better. In order to answer this question, Booz-Allen's consultants translated it into many smaller tactical and operational questions that can be classified into the following categories:

• production capacity questions

\- buffer related questions

— waiting time questions-both in front of various machines and in front of various transport vehicles— questions about queue lengths-both in front of various machines and various transport vehicles

\- makespan questions, including time spent in queues, in transport, and in processing

\- questions about the utilization ratios including machines and transport vehicles

\- questions about machine failures

\- questions about parts serviced by a resource machines/transport vehicles)

\- questions about plant layout

\- transportation questions, such as the waiting times based on machine priorities and the waiting times based on the number of transport vehicles

If it turns out that one of the layouts is better than the other one for most of these questions, then the answer to the initial strategic question is to select the layout that yields better results.

Before Cassandra $^{+}$ was installed, Booz-Allen's consultants were using the traditional simulate-and-gather-statistics approach to answer the questions listed above. More specifically, the consultants were using a simulator [5] and were running multiple simulation runs and statistically analyzing the results of these runs. For example, in order to answer a production capacity question, the user has to perform the following steps using the simulator. In step 1, the user has to load the appropriate model using the run option. In step 2, the simulator asks the user for the number of replications he or she wants (the output from each replication is stored separately) and for the length of simulation runs. After that, the actual simulations are run. When the appropriate simulation runs are finished, the user performs step 3 in which he or she has to choose any one of the simulation output files that has been created by the simulator. In step 4, after selecting an output file, the user gets a menu from which the user can select the multiple replication summary option. In step 5, the user can then select the exit buffer variable, since the outcome of interest is the throughput, from the output summary and then ask the system to perform statistical analysis on the values of this variable. The statistical summary includes the mean, variance and a 90%, 95% and 99% confidence intervals (CI). If the CI's are not within expectations the user can opt to do additional runs. However, the user has to provide the system with the value of the number of runs that are needed to get the answer within the bounds that the user wants. As we can see, this is a laborious and error-prone process, and, in the worst case, the consultants had to repeat it per each question they wanted to ask.

In contrast to this, each of the questions listed above was formulated as a SimQL query when $Cassandra^{+}$ was installed. For example, the capacity planning question for the 2-process line model operating 2 shifts (16 hours) is formulated in SimQL as

<table><tr><td>Type:</td><td>Event-based</td></tr><tr><td>Time:</td><td>16 hours</td></tr><tr><td>Answer-Semantics:</td><td>Numeric</td></tr><tr><td>Core-query:</td><td></td></tr><tr><td>SELECT</td><td>Count(Job-Id)</td></tr><tr><td>FROM</td><td>2lmodel-departure</td></tr><tr><td>WHERE</td><td>predicate-name = &#x27;exit&#x27;;</td></tr><tr><td>Model-Name:</td><td>2lmodel</td></tr><tr><td>Error-of-estimation:</td><td>10</td></tr></table>

The answer to this query was 8.5 racks, and it took Cassandra $^{+}$ 10 simulation runs to obtain this answer. Although during the simulation process thousands of events occur, the trace file contained only 89 records. This was the case because the query-driven simulation approach records only the events necessary to answer the query (all the exit events). Overall response time for this query, on a Sun SPARCstation 1 (under SunOS UNIX operating system), was 20 seconds.

To answer one of the major tactical questions that the Booz-Allen's consultants had about the two alternative layouts, i.e., which layout is better in terms of capacities, this question was translated into four SimQL queries that were run, one query per each model (2-process line and 1-process line) and per each shift (2 shifts and 3 shifts). The answers to these four queries are summarized in Table 1.

As it follows from this analysis, the 2-process line provides greater throughput than the 1-process line.

Similar types of analysis was done for other questions of interest to the company (makespan, waiting time, utilization and other questions). Since these questions could not be directly expressed in SimQL, all of them had to be translated into several SimQL queries in a way that is similar to the capacity question. Based on this analysis, it was concluded by the company that the 2-process line was better than the 1-process line.

Table 1  
Throughput summary statistics

<table><tr><td rowspan="2"></td><td colspan="2">Throughput</td></tr><tr><td>Two shifts (16 hrs.)</td><td>Three shifts (24 hrs.)</td></tr><tr><td rowspan="3">Two process line</td><td>8.5</td><td>18.4</td></tr><tr><td>CI: 8.3-9.4</td><td>CI: 17-19.5</td></tr><tr><td>number of runs: 10</td><td>number of runs: 10</td></tr><tr><td rowspan="3">One process line</td><td>6.9</td><td>15.2</td></tr><tr><td>CI: 6.14-7.66</td><td>CI: 14.37-16.83</td></tr><tr><td>number of runs: 20</td><td>number of runs: 10</td></tr></table>

In summary, the major strategic question, which layout is better, was translated into several tactical and operational questions, and these questions were translated into one or more SimQL queries that were evaluated using the Cassandra $^{+}$ system. The answers to the SimQL queries were used to answer the main strategic question.

If we compare the QDS approach to answering questions that the consulting company had about the surface treatment facility with the traditional approach that the company adopted before Cassandra $^{+}$ was used, we see that the QDS approach provides the following advantages:

\- Ease of use, reliability, speed. The user can formulate a SimQL query in a declarative fashion and does not have to know any simulation and statistical packages. In contrast to this, before Cassandra $^{+}$ was implemented, the consultants had to put together all the necessary ingredients to run a simulation from various sources for the various scenarios that they wanted to consider, determine number of runs and then run simulations. This was a time consuming, error-prone and slow process.

\- Empowering the end-users. Before Cassandra $^{+}$ was used, questions about the surface treatment facilities could be handled only by simulation specialists familiar with the simulator used in this case. After Cassandra $^{+}$ was installed, these questions can be asked by the end-users familiar with SimQL $^{7}$ . Thus, query-driven simulations allow us to move simulations from the “back-office” of simulation specialists to the “front-office” of the end-users.

## 6. How end-user questions are mapped into SimQL queries

In Section 2, we presented various questions different people in a manufacturing organization want to ask about outcomes of their business processes, and in Section 5 we described some of these questions in the context of the Booz-Allen's case. Although some of these questions could be asked directly in SimQL as Examples 2 and 3 show, other questions cannot be directly expressed in SimQL. For example, the strategic Booz-Allen's question, which plant layout is better, cannot be expressed directly in SimQL for the reasons explained in Section 3.

Since not all questions of interest to the end-user can be expressed in SimQL, this means that there should be a mapping (translation) from the high-level end-user questions into SimQL queries. For example, the strategic Booz-Allen's question, which plant layout is better, had to be translated into several tactical and operational questions (i.e., questions about capacities, makespans, utilizations, and so on).

Fig. 3 summarizes the distinction between the user queries directly expressible in SimQL and those that need translation. The translation can be achieved by building various tools on top of SimQL queries $^{8}$ that translate high-level end-user questions into SimQL queries in one of the following ways:

![](/api/attachments/9C62NAGA/fulltext/images/b90d1bbaf724a901ef6b1afa676ff90f4db0b4fa329078724d7770c10a17d2f3.jpg)  
Fig. 3. Translation of user questions into SimQL.

Manually. In this case the user does the translation by him- or herself by formulating a set of SimQL queries and then analyzing the results. For example, the strategic Booz-Allen's question which plant layout is better is manually translated into the questions about capacities, makespans, utilization rates, and so on, and the latter questions are further translated into SimQL queries.

Using Conventional PL's. The user can embed SimQL queries into conventional programming languages (e.g., C, COBOL, Assembler, etc.), as is typically done with conventional database query languages. For example, in large data-intensive applications, SQL queries are embedded into conventional programming languages, such as C, COBOL, or ASSEMBLER, each language requiring a separate interface [11]. Therefore, if we want to embed SimQL queries into a programming language, we have to provide an interface between this programming language and SimQL, as is done in the classic database case.

Using 4GL's. The 4th Generation Language built “on top” of Cassandra $^{+}$ provides for the processing of some high-level queries.

Using Expert Systems. An expert system can be built "on top" of SimQL. This expert system will reason about outcomes of various SimQL queries thus answering high-level questions asked by the end-user.

Using Optimization Modules. While dealing with optimization queries, a single query can spawn off several queries. For example in determining the optimum lot size, the optimizer will start with a particular lot size value and keep changing the size until an optimum is obtained. Each such size value will result in a different query and a different set of simulation runs.

One does not have to develop any translation tools for the manual translation method since the translation is done by the human. Translation using conventional programming languages also does not require the development of any special tools. One only has to adopt the programming interface used in relational databases to the SimQL query language and incorporate it into Cassandra $^{+}$ . In contrast to this, one needs more work to develop the translation tools based on 4GLs, expert systems, and optimization modules.

As the sample of questions presented in Section 2 shows, translation of end-user questions into SimQL queries becomes progressively more difficult as we move up the management hierarchy as shown in Fig. 1. For example, the tactical question from the Booz-Allen's case, i.e., which plant layout is better in terms of capacities, was mapped into four SimQL queries in Section 5. In contrast to this, the strategic question, i.e., which plant layout is better, was mapped into many tactical and operational questions in Section 5, and some of these questions had to be mapped even further to SimQL queries.

To illustrate this point further, consider some more examples from Section 2. At the operational level of management, most of the questions in Cells 1 through 4 can be expressed directly in SimQL. Some of the examples of such questions are “where will Job-5 be 5 hours from now?”, “how many jobs will be produced in the next shift?”, “what will the material costs for Order-5 be?”, or “to complete Order-20 in a week, how much overtime should be granted?” Furthermore, those queries that cannot be expressed in SimQL directly can be easily translated into SimQL queries.

Table 2  
Translation difficulty for various user queries

<table><tr><td>Levels of management</td><td>Translation from end-user to SimQL queries</td></tr><tr><td>Strategic</td><td>Moderate to hard</td></tr><tr><td>Tactical</td><td>Easy to moderate</td></tr><tr><td>Operational</td><td>Direct to easy</td></tr></table>

At the tactical level of management, some of the questions in Section 2 are directly expressible in SimQL, whereas others are not. For example, such questions as “what will be the yield per plant for the next quarter for manufacturing Product-C?” or “what will be the average cost of producing product-A for the next quarter?” can be directly expressed in SimQL. On the other hand, such questions as “What should the lot size be to satisfy our current demand profile at the minimum cost?” or “Can I reduce my Work-In-Process (WIP) by reducing set-up times?” cannot be directly expressed in SimQL and require translation into SimQL queries. Nevertheless, the translation of these questions into SimQL queries is feasible. For example, the first query requires the solution of an optimization problem using one of the Operations Research methods. The translation of the second query requires changing set-up times and asking by how much work-in-progress will be reduced for various set-up times.

At the strategic level, most of the queries cannot be expressed directly in SimQL. For example, questions such as “is it better to make a new microprocessor in-house for our new line of PCs, or is it better to buy it from the leading manufacturer of microprocessors?” or “what will the benefits of re-engineering of my business processes be?” that are of interest to the senior management, cannot be directly expressed in SimQL. Furthermore, it is difficult to translate these questions into SimQL queries.

In summary, most of the questions at the operational level of management can be directly expressed in SimQL or it is easy to translate them into SimQL queries. Although some of the questions at the tactical level can be directly expressed in SimQL, others require translation, which is typically not hard to do. Most of the queries at the strategic level of management require translation into SimQL queries, and it is often difficult to come up with this translation. This discussion is summarized in Table 2. This means that Query-Driven Simulations, and Cassandra $^{+}$ in particular, should be used primarily by operational and tactical management in organizations.

## 7. Query-driven modeling lifecycle

We identify the following major tasks in building, running, and maintaining a Query-Driven Simulation system:

1. Model Development. This task requires writing simulation models using one of the simulation languages, such as Simscript, Modsim, etc. These simulation models are developed by the model developer.

2. Model Administration. A group of simulation models are stored in the modelbase $^{9}$ . The modelbase also stores additional information about these models, such as the language in which the simulation model is written, default simulation parameters, the list of events traced by the model, and various other information needed for asking queries on that model. The modelbase is maintained by a model administrator, who is responsible for adding new, removing old, and updating existing models. In addition, this person grants access privileges to various users of the models in the modelbase.

3. Model Querying. This task is the major purpose of Query-Driven Simulation systems, and we described it at length in the paper. The end-users usually perform this task. To ask a query on a simulation model, the end-user has to make sure that the model exists in the modelbase. The end-user should also know the names of the temporal relations associated with the model that he or she intends to query. Finally, the end-user should know the names of the attributes in these temporal relations. All this information is contained in the modelbase. To retrieve this information from the modelbase, we propose to develop a browser based on a graphical user interface. For example, this browser should support the retrieval of information such as “which simulation language is used to write model Manufacturing-Model-4,” or “find the names of relations that can be queried for model Manufacturing-Model-5.” To answer such questions, languages have been proposed before $[25,16]$ , and we plan to build a graphical front end for one such language.

![](/api/attachments/9C62NAGA/fulltext/images/b02dc95b9acb1f575b309084626538ca70e3b17f1db6adfc45b2a11f4fca301e.jpg)  
Fig. 4. Query-driven modeling lifecycle.

All the tasks described above are related to each other in the way shown in Fig. 4. As Fig. 4 shows, the model developer initially designs one or several working simulation models of an enterprise and delivers them to the model administrator who installs them into the modelbase. After the model administrator installs the model in the modelbase, end-users can start using it by issuing queries about simulation outcomes expressed in SimQL.

At this point, either the user is satisfied with the model and keeps using it, or he/she might experience some problems. There are two types of problems the user can face. First, the information, as specified in the modelbase, does not satisfy user's needs. For example, it may turn out that the user wants to ask a query about a relation that does not appear in the modelbase but can be easily computed from the events that the simulation model traces. Note that this problem can be solved by the model administrator who makes appropriate administrative changes to the modelbase. Note that this simulation model itself is not changed for this type of a problem. Second, the user may want to ask a query that the simulation model cannot handle. For example, the user may want to know how many parts will be painted in red color within the next 10 hours, and the simulation model does not keep track of the colors of different parts and the painting information. In this case, the model developer must make changes to the simulation model itself.

In both cases, Query-Driven Simulations provide a feedback loop in the process of model development and model administration: the models are modified based on the feedback coming from the user after the user asks various questions about these models. The process of development, installation, usage, and feedback represents a Query-Driven Modeling Lifecycle of a model. The model development process can go through several iterations before it converges to a stable simulation model satisfying end-user's needs.

We have described in this section the simulation modeling issues that arise while doing Query-Driven Simulations. A QDS system, as any other software system, also requires system administration. The system administration functions include setting resource quotas, assigning privileges, configuring the system, and so on. All these tasks should be performed by the system administrator.

## 8. Conclusions

In this paper, we introduced the concept of Query-Driven Simulations (QDS) and described how QDS can be used by different people in various organizations for asking questions about future outcomes of business processes. The information provided by a QDS system can help managers make better planning, control, and staffing decisions.

In particular, we considered a manufacturing organization and described the types of questions decision makers across different functional units and levels of management ask about outcomes of manufacturing processes. In addition, we considered a specific manufacturing application developed by the management consulting company of Booz-Allen and Hamilton and studied the questions of interest to their consultants. We argued that it is easier, faster, and more reliable for the end-user to ask these questions using the QDS than the traditional SAGS approach. Moreover, the end-user can express his/her questions in various temporal relational query languages and direct them against the simulation models written in any simulation language as long as the simulation traces generated by the model follow a certain format. Thus, the QDS approach empowers the end-user by bringing simulations from the “back office” of the simulation specialist to the “front office” of the end-user.

Despite its clear advantages, the QDS approach also has some limitations in comparison to the SAGS approach. In particular, it is impossible to express some end-user questions in the query language of the QDS system and, thus, they have to be translated into the lower-level questions directly expressible as QDS queries. We considered this translation process and concluded that the higher the person is in the management hierarchy, the more difficult it is to translate his/her questions into QDS queries. Another limitation of the QDS approach is that it requires generation of large trace files which can impede the performance of the QDS systems. However, our experience with the Booz-Allen's case showed that the Cassandra $^{+}$ system handled all of the Booz-Allen's queries with ease and performance was not an issue in that case. In general, the QDS approach is best suited for asking queries that require short to medium simulation time to answer them and the medium degree of precision for the answer, and Booz-Allen's queries fell into this category $^{10}$ .

## Acknowledgements

The authors wish to thank Jim Kwon from Booz-Allen for helping them with the case study presented in Section 5.

## References

[1] A. Aho and J. Ullman, Optimal Partial Match Retrieval when Fields are Independently Specified, ACM Transactions On Database Systems 4, No. 2 (1979) 168–179.

[2] R. Askin and C. Standridge, Modeling and Analysis of Manufacturing Systems, 1st ed. (Wiley, NY, 1993).

[3] P. Balasubramanian and A. Tuzhilin, Cassandra $^{+}$ : A System for Doing Query Driven Simulation, Working Paper IS-93-40, Leonard N. Stern School of Business, NYU, 1993.

[4] P. Balasubramanian and A. Tuzhilin, Using Query-Driven Simulations for Querying Outcomes of Business Processes, Working Paper IS-93-38, Leonard N. Stern School of Business, NYU, 1993.

[5] J. Banks, E. Aviles, J. McLaughlin and R. Yuan, The Simulator: New Member of the Simulation Family, Interfaces 21, No. 2 (1991) 76–86.

[6] R. Belanger, B. Donovan, K. Morse and D. Rockower, MODSIM II Reference Manual, CACI (1990).

[7] R. Blanning, A. Whinston, M. Ai-Chang, V. Dhar, C. Holsapple, M. Jarke, S. Kimbrough, J. Lerch and M. Prietula, Model Management Systems, in: Edward A. Stohr and Benn R. Konsynski (eds.), Information Systems and Decision Processes (IEEE Computer Society Press, 1992).

[8] CACI, A quick look at SIMFACTORY II.5/SIMPROCESS: Manufacturing and Business Modelling (1993).

[9] Consolidated Analysis Centers, Inc., UNIX SIMSCRIPT II.5 User's Manual (1987).

[10] R. Conway, W. Maxwell, J. McClain and S. Worona, User's Guide To XCELL+ Factory Modeling System, Release 4.0 (The Scientific Press, 1990).

[11] C.J. Date, An Introduction to Database Systems, 4th ed. (Addison-Wesley, 1986).

[12] C.J. Date, A Guide to the SQL Standard, 1st ed. (Addison-Wesley, 1989).

[13] R. Elmasri and S. Navathe, Fundamental of Database Systems, 2nd ed. (The Benjamin/Cummings Publishing Company, 1990).

[14] Jim Fidele, Manager of Manufacturing & Logistics, DEC, Personal Communications, Spring 1993.

[15] K. Fordyce, R. Dunki-Jacobs, B. Gerard, R. Sell and G. Sullivan, Logistics Management System (LMS): An Advanced Decision Support System for Dispatch or Short Interval Scheduling, Production and Operations Management 1, No. 1 (1992) 70–86.

[16] A.M. Geoffrion, An Introduction to Structured Modeling, Management Science 33, No. 5 (1987) 547–588.

[17] R. Head, Management Information Systems: A Critical Appraisal, Datamation 13, No. 5 (1967) 22–28.

[18] P. Heidelberger and P.D. Welch, Simulation Run Length Control in the Presence of an Initial Transient, Operations Research 31, No. 6 (1983).

[19] IBM, General Purpose Simulation System/360 User's Manual (1970).

[20] S. Kotha, Leonard N. Stern School of Business, New York University, Personal Communications, Spring 1993.

[21] R. Koymans, Specifying Real-Time Properties with Metric Temporal Logic, Journal of Real-Time Systems 2 (1990).

[22] F. Kroger, Temporal Logic of Programs, Vol. 8, EATCS Monographs on Theoretical Computer Science (Springer-Verlag, Berlin, 1987).

[23] A.M. Law and D.W. Kelton, Simulation Modeling and Analysis, 2nd ed. (McGraw-Hill, NY, 1991) Ch. 13.

[24] A.M. Law and M.G. McComas, How Simulation Pays Off. Manufacturing Engineering (1988) 37–39.

[25] M.L. Lenard, A Prototype Implementation of a Model Management System for Discrete-Event Simulation Models, in: Proceedings of the 1993 Winter Simulation Conference (1993) pp. 33–39.

[26] Z. Manna and A. Pnueli, The Temporal Logic of Reactive and Concurrent Systems (Springer-Verlag, Berlin, 1992).

[27] J.A. Miller and O.R. Weyrich, Query Driven Simulation Using SIMODULA, in: Proceedings of the 22nd Annual Simulation Symposium (1989).

[28] Praveen Nayyar, Leonard N. Stern School of Business, New York University, Personal Communications, Spring 1993.

[29] J. Pruett and V. Vasudev, MOSES: Manufacturing Organization Simulation and Evaluation System, Simulation (1990) 37–45.

[30] P.G. Ranky, Computer Integrated Manufacturing (Prentice-Hall, NY, 1986) Ch. 6–8.

[31] SAS Institute, Raleigh, NC, SAS User's Guide, 1989.

[32] H.A. Simon, Artificial Intelligence, Simulation, and Modeling, Interfaces 17, No. 5 (1987) 11–31.

[33] M.R. Smith and J.M. Kay, A Case Study on the Applica-

tion of Simulation to a Car Assembly Line, Proceeding of the 3rd International Conference in Manufacturing (1987) 207–234.

[34] R. Snodgrass, The Temporal Query Language TQuel, ACM Transactions On Database Systems 12, No. 2 (1987) 247–298.

[35] R. Snodgrass, A Relational Approach to Monitoring Complex Systems, ACM Transactions On Computer Systems 6, No. 2 (1988) 157–196.

[36] R.T. Snodgrass, I. Ahn, G. Ariav, D.S. Batory, J. Clifford, C.E. Dyreson, R. Elmasri, F. Grandi, C.S. Jensen, W. Káfer, N. Kline, K. Kulkarni, T.Y.C. Leung, N. Lorentzos, J.F. Roddick, A. Segev, M.D. Soo and S.M. Sripada, TSQL2 Language Specification, ACM SIGMOD Record 23, No. 1 (1994) 65–86.

[37] A. Tansel, J. Clifford, S. Gadia, S. Jajodia, A. Segev and R. Snodgrass, Temporal Databases (Benjamin/Cummings, 1993).

[38] L. Joseph Thomas, John O. McClain and David B. Edwards, Cases in Operations Management: Using the XCELL Factory Modeling System (The Scientific Press, 1989).

[39] H.G. Thome, Planning and Monitoring of FMS by Simulation, Proceeding of the 7th International Conference on Flexible Manufacturing Systems (1988) 137–149.

[40] A. Tuzhilin, Sim T.L.: A Simulation Language Based on Temporal Logic, TRANSACTIONS of The Society for Computer Simulation 9, No. 2 (1992) 87–100.

[41] A. Tuzhilin, Applications of Temporal Databases to Knowledge-Based Simulations, in: A. Tansel, J. Clifford, S. Gadia, S. Jajodia, A. Segev and R. Snodgrass (eds.), Temporal Databases (Benjamin Cummings, 1993).

[42] A. Tuzhilin and J. Clifford, A Temporal Relational Algebra as a Basis for Temporal Relational Completeness, in: Conference on Very Large Databases (1990) 13–23.

[43] S. Walsh, Operations Manager in Manufacturing & Logistics, DEC, Personal Communications, September 1993.

![](/api/attachments/9C62NAGA/fulltext/images/31ff2c0dcea28d9538d30899afc6e59dc7cb149eb8d08d13d0f03ea84fd1043b.jpg)

Alexander Tuzhilin is an Assistant Professor of Information Systems at Stern School of Business, New York University. He holds a Ph.D. in Computer Science from the Courant Institute of Mathematical Sciences, NYU. His research interests include temporal databases, query-driven and knowledge-based simulations, knowledge discovery in databases, and conceptual modeling of information systems. His research has been spon-

sored by the NSF and he has published papers in ACM Transactions on Database Systems, ACM Transactions on Information Systems, ACM Transactions on Modeling and Computer Simulation, IEEE Transactions on Knowledge and Data Engineering, Acta Informatica, and other journals. He is a co-editor of the book Recent Advances in Temporal Databases published by Springer-Verlag.

![](/api/attachments/9C62NAGA/fulltext/images/cd968adae216f78b6d6dd32c51a1be7579471b4d4b9059f6e5d7e24cfe2c343f.jpg)

P. Balasubramanian is an assistant professor of Management Information Systems in the department of management information systems, Boston University. Professor Balasubramanian received his Ph.D. from New York University in MIS with a minor in computer science. His current research interests include query-driven simulation and its applications in manufacturing, hypermedia design and development, model manage-

ment systems, and modeling and simulation of office workflows. He has published papers in the Communications of the ACM, in The Model Management and Hypertext Mini Track at HICSS and in the Proceedings of AI Applications on Wall Street.
