---
otero_id: 24290
otero_key: "2A7FG66Z"
title: "An investigation of client/server application development methodologies"
authors: "Graham Low; Richard Looi"
year: "1997"
journal: "Journal of Information Technology"
doi: "10.1080/026839697345053"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Journal of Information Technology (1997) 12, 187–196

# An investigation of client/server application development methodologies

GRAHAM LOW

Centre for Advanced Empirical Software Research (CAESAR), School of Information Systems, University of New South Wales, Sydney, Australia 2052

RICHARD LOOI

Rothschild Australia, Sydney, Australia 2000

Client/server application development is becoming increasingly popular in commercial organizations. However, previous research has found that current application development methodologies provide little or no support for client/server computing possibly due to the relative newness of the technology in commercial environments. This research is the first step in demonstrating the applicability of the client/server methodology enhancements proposed in a commercial Management Information System (MIS) environment. It examines the application of traditional development methodologies to the client/server environment, the problems associated in using these methodologies and the respondent's rating of the importance of the various client/server application development issues included in the proposed methodology.

## Introduction

Client/server application development is becoming increasingly popular in commercial organizations. A survey of information systems executives by Cowan and Company in 1996 found that the annual growth rate of total Information Systems budgets in the next three to five years is expected to be 7-8% for organizations with client/server computing, compared with an average figure of 6-8%. Organizations are considering client/server computing as an alternative to traditional, centralized mainframe computing. This is because of the promise of better control of corporate data and higher efficiency from client/server information systems (Low and Russell, 1993).

The momentum to client/server computing is largely fuelled by the desire to downsize and the shift towards open systems technology. There are many benefits expected with client/server computing. In a survey of Australian organizations, Low and Russell (1993) reported that Australian organizations found that downsizing (application executed on the most appropriate platform) an improved network performance and transparent access to shared data were the main benefits. Other benefits included system scalability, lower software maintenance costs, graphical user interfaces, fault tolerances and parallel processing. Better response times are often achievable with client/server applications than with traditional applications because scalability gives the option of splitting the server load between two or more computers and the design of client/server systems can often reduce the amount of network traffic. For instance, some banks have developed client software that inputs customer loan details and gives an initial assessment of the likelihood that the customer will be able to get a loan. Only when the customer agrees are their details sent to the server for the final approval process.

A particular benefit of client/server software is the relative ease of integrating new technology in both new and existing client/server applications. For instance, only the client application requires modification to implement a World Wide Web Java interface or alter the data entry method from key punching to imaging.

Philipson (1993) noted that rarely has a new technology arrived with such force as client/server computing and with so little understanding of the underlying issues. He also noted that application development, systems management and network operation systems are the areas of greatest immaturity for client/server computing. Low and Russell (1993) found that the major concerns were (1) the complexity and risk of client/server development, (2) increased network traffic due to inappropriate splitting of the application between client and server(s), (3) inadequate fault tolerance (i.e. reliability), (4) inadequate hardware due to poor design and an understanding of its impact on client and server hardware, (5) security, (6) developers not being sure how to develop client/server applications and (7) system administration. Particular project management challenges include the incompatibility of client operation systems such as OS/2 and Windows and managing a distributed environment.

Low et al. (1995) found that current application development methodologies provide little or no support for client/server computing possibly due to the relative newness of the technology in commercial environments. They conducted a preliminary multiple case study of 18 Australian organizations undertaking client/server development. They studied a subset of the distributed application design issues presented in the literature (e.g. Gomaa, 1984, 1989; Shatz and Wang, 1987, 1989; Jain and Purao, 1991). The same distributed systems issues appeared to be important for both Object Orientated (OO) and non-OO client/server development. Low (1997) proposed methodology enhancements to support client/server development.

This research examines the application of traditional application development methodologies to the client/server environment, the problems associated in using these methodologies and the respondent's rating of the importance of a comprehensive set of client/server application development techniques included in the proposed methodology enhancements. It is the first step in demonstrating the applicability of the proposed client/server methodology enhancements (Low, 1997) in a commercial MIS environment. The use of this methodology would assist in identifying likely risks and ensure they are addressed during the design and implementation of client/server systems. One risk is poor performance which can be reduced by appropriate partitioning and allocation of the application (Anon, 1995). Low (1997) provided guidance in this process, suggesting a very simple approach and two more rigorous approaches.

## Literature review

## Client/server model

The client/server model is an architecture for distributed processing. The objective of the model is 'to make a collection of (possibly replicated) distributed services available on a network of computers' (Levy and Tempero, 1991, p. 79). The exact definition of the client/server model varies between users with surveys often producing different definitions from every respondent (Davis, 1991).

A server is a logical process, providing a service to any other process that requests it. A client is another logical process, which requests services from a server (Levy and Silberschatz, 1990; McGoveran and White,

1990; Levy and Tempero, 1991). A client/server relationship exists when a client requests a service from the server. While it is always the client that requests the service from the server (Gomaa, 1989), the client and server may later reverse roles. In this situation, the server process becomes the client and requests a service from another server (which might previously have been a client) (McGoveran and White, 1990). An example is a workstation in a secure network establishing a World Wide Web session to a server in an untrusted network. First, the local workstation acts as a client in establishing a session with the proxy server. The proxy server then acts as a client in establishing the remainder of the connection with the remote World Wide Web server.

The interaction of the client and server should be completely transparent resulting in the user of the application not being aware that it is a client/server application (Colony, 1990). There is nothing in these definitions that limits where the client and server processes execute. They may even execute on the same computer (Svobodova, 1984; Levy and Silberschatz, 1990; McGoveran and White, 1990). In this case it is a logical separation of client and server processes.

Buzzard (1990) stated that ‘true client/server processing requires’ the following.

(1) Communication between the client and the servers.

(2) Client-initiated interaction with the server.

(3) Restriction by the server over conflicting requests from multiple clients.

(4) Arbitration by the server over conflicting requests from multiple clients.

(5) Division of the application between the client and the server.

Buzzard (1990) also noted that the first four of these requirements are present in most network operating systems and that it is only the fifth requirement that truly separates client/server computing from network computing.

The Gartner Group (Philipson, 1993) suggested five classifications for the division of the application between the client and the server (Figure 1).

(1) Distributed presentation. This involves adding presentation logic to the client (e.g. PC) while keeping the existing presentation logic at the server (typically a mainframe).

(2) Remote presentation. Presentation logic is implemented at the client only. The server is not concerned with presentation and only sends data to the client when requested.

(3) Distributed function. Both business logic and presentation logic are implemented at the client.

<table><tr><td colspan="3">Application Components</td></tr><tr><td>Presentation</td><td>Business Logic</td><td>Data Management</td></tr></table>

![](/api/attachments/2A7FG66Z/fulltext/images/9ecd54e7c694ca8c21ac1018e4b255d03fda35fa6134165e3221b95fdc4235c8.jpg)  
Figure 1 Classifications for the division of the application between client and server

(4) Remote data management. All business logic is implemented at the client while the server acts as a database manager.

(5) Distributed data management. Data is stored at the client as well as the server.

The manner in which an application is divided may span a number of the preceding classifications. For instance, an application may have the characteristics of distributed function and remote data management (Figure 2).

The definition of client/server adopted in this paper will be that proposed by Buzzard (1990) together with the five classifications relating to the division of an application between client and server proposed by the Gartner Group (Philipson, 1993).

## Distributed application development

Unfortunately there are no comprehensive client/server development methodologies available in the literature. Tools are available that assist in the development of client/server applications. However, these tools provide little support for the partitioning and allocation of components in a client/server system that authors such as Wadhwa (1995) and Low et al. (1996) consider as important design considerations.

![](/api/attachments/2A7FG66Z/fulltext/images/376b6b3c599040a3f59b54e211d3ac19110a6054d20c5ece696f38e3f0b0ace4.jpg)  
Figure 2 Typical client/server application

Fortunately client/server computing is a form of distributed computing. Thus, many of the application development techniques for distributed computing (e.g. Gomaa, 1984, 1989; Shatz and Wang, 1987, 1989; Jain and Purao, 1991; Low et al., 1996; Low, 1997) should be applicable to client/server computing. The development techniques are briefly compared in Tables 1 and 2. The commonality of the Low (1997) approach to the other three techniques is not accidental since they were influential in its development.

Based on a comparison of these methodologies, a number of distributed design issues have been selected for study in this research (Table 3).

## Research method

## Research questions

This research examines the application of traditional application development methodologies to the client/server environment, the problems associated in using these methodologies and the respondent's rating of the importance of the various client/server application development issues are outlined in Table 3. This practical assessment of the application of various distributed application design techniques in a client/server environment provides support or otherwise for the techniques described earlier and, in particular, the applicability of the Low (1997) methodology to client/server development in a non-OO environment.

## Research instrument

The exploratory nature of this research influenced the choice of research instruments employed. A combination of structured interview and questionnaire was employed. The questionnaire allowed the collection of quantitative data, while the interview allowed clarification and the collection of ‘softer’ qualitative data. The combination increased the explanatory power of this work.

Personal interviews were conducted with representatives from each of the organizations selected. Each representative was initially interviewed once. Where clarification was required, additional interview(s) and/or telephone conversations were conducted. All of the organizations had developed client/server applications. The interviews were semi-structured in nature. The interviewees were asked to describe the state of client/server development within their organization. Any important issues relating to client/server development were then discussed with the interviewees. Questions from the survey were then asked and areas not previously covered by the interviewees were investigated in more detail.

Table 1 Comparison of distributed development techniques (user requirements and logical design)

<table><tr><td></td><td>Shatz and Wang (1987; 1989) approach</td><td>Gomaa (1984; 1989) approach</td><td>Jain and Purao (1991) approach</td><td>Low (1997) approach</td></tr><tr><td>User requirements</td><td>Include additional information such as performance, reliability, growth and the potential for concurrency</td><td>N/A</td><td>Include location-specific information</td><td>Include additional information such as performance, scalability, transparency and reliability</td></tr><tr><td>Application analysis</td><td></td><td>N/A</td><td>Include location details in DFDs and process descriptions</td><td>Include location details in DFDs and process descriptions (if required)</td></tr></table>

N/A, not applicable.

Table 2 Comparison of distributed development techniques (physical design)

<table><tr><td></td><td>Shatz and Wang(1987; 1989) approach</td><td>Gomaa (1984; 1989) approach</td><td>Jain and Purao (1991) approach</td><td>Low (1997) approach</td></tr><tr><td>Application design</td><td>Split the proposed applications into a number of software processes and data files. Allocate these processes and files within the system using task partitioning and task allocationKey partitioning considerationsStructure chart analysis used to perform functional partitioning Grouping of functional modules to minimize intermodule communications and exploit concurrencyKey task allocation considerationsAllocation metrics:interprocess communications,interprocessor communications and execution cost,load balancing,completion time and reliabilityAllocation constraints:processing capacity,number of processors and memory</td><td>Use Design Approach for Real Time Systems (DARTS) approach1. Perform data flow analysis2. Structure the system into distributed subsystems3. Define interfaces between subsystems4. Structure each subsystem into concurrent tasks5. Define interfaces between tasks6. Design each task using structured design</td><td>Allocate data within the systemAllocate processes.IssuesType of processing requiredAvailability of required dataInterprocessor communicationsProcessing capacity</td><td>Three approachesTemplate approachDivide system into presentation logic,business logic and data management layers.Place the different layers on either client or server using standard templatesTheoretical approachPartition the system into cohesive independent components based on the requirements for concurrency and (inter-module) communications.Allocate the components based on interprocessor communications cost,interprocessor communications and execution cost, load balancing, reliability and scalabilitySubsystem approachForm subsystems and allocate these subsystems based on interprocessor communications cost,interprocessor communications and execution cost, load balancing, reliability and scalability</td></tr></table>

Table 3 Selected key distributed design issues

<table><tr><td>Issue</td></tr><tr><td>Guidance in splitting the application between client and server</td></tr><tr><td>Data flow diagram support</td></tr><tr><td>Structure charts</td></tr><tr><td>Task partitioning considerations</td></tr><tr><td>Intermodule communications</td></tr><tr><td>Concurrency</td></tr><tr><td>Size of processes</td></tr><tr><td>Task allocation considerations</td></tr><tr><td>Interprocessor communications</td></tr><tr><td>Interprocessor communications and execution cost</td></tr><tr><td>Load balancing</td></tr><tr><td>Completion time</td></tr><tr><td>Reliability</td></tr><tr><td>Task allocation constraints</td></tr><tr><td>Processing capacity</td></tr><tr><td>Number of processors</td></tr><tr><td>Memory</td></tr></table>

Table 4 Research questions

<table><tr><td>Research questions</td></tr><tr><td>The extent of client/server development within the organization, the type of applications developed, the client/server configuration used and the number of users of the client/server applications within the organizations</td></tr><tr><td>Development methodology and its appropriateness</td></tr><tr><td>The importance of the methodology in providing guidance in how to divide an application between client and server</td></tr><tr><td>Task partitioning considerationsWhether task partitioning was supported by the organization&#x27;s development methodologyThe extent of use of structure charts and data flow diagramsThe relative importance of various task partitioning considerationsMinimizing intermodule communicationsExploiting concurrencyLimiting the size of processes</td></tr><tr><td>Task allocation considerationsWhether task allocation was supported by the organization&#x27;s application development methodologyThe relative importance of various approaches to task allocationInterprocessor communicationsInterprocessor communications and execution costLoad balancingCompletion timeReliabilityThe relative importance of various system constraints upon the task allocation processProcessing capacityLimited number of processesMemory size</td></tr><tr><td>What methodology would be used for future client/server development</td></tr></table>

A brief description of the survey/interview instrument is presented in Table 4. A seven-point Likert scale format was used for the questions that asked the respondent to rate the ‘importance’ of an item.

## Instrument validity

The questionnaire instrument was pilot tested by five members of faculty and two industry respondents. Discussions on the design and content of the instrument were conducted immediately after each pilot test. The reviewers' comments were considered and the necessary changes were made in order to improve readability, clarity, content and structure. The pilot phase of instrument testing allowed the reliability of the questionnaire to be established, while also checking its validity with people knowledgeable in the field.

## Data collection

Every effort was made to obtain a representative sample of Australian organizations for this research. In total 19 organizations which had all developed client/server applications participated in the research. There were approximately equal proportions of large-, medium- and small-sized organizations covering the finance and business (nine), mining (one), consultancy (three), food (three), and government (three) areas. Each of the organizations included in the research had completed at least one client/server project. In total these 19 organizations had completed 73 client/server projects with a further 23 under development and 18 under evaluation.

## Results and discussion

The results of the interviews and survey are discussed in this section in the order presented in Table 4.

## Extent of client/server development

Thirteen of the 19 organizations had completed their first project within the previous 2 years with the majority (55 out of 73 projects) of client/server development being undertaken by the information technology (IT) consultancy and finance and business services sectors. Most of the client/server projects were either transaction processing or reporting applications (Table 5). Other applications included decision support systems, executive information systems, expert systems, research database application, contacts database application, system monitoring applications, multimedia applications and utility applications providing support to office applications.

Table 5 Classification of applications completed

<table><tr><td colspan="7">Types of application</td></tr><tr><td>Industry</td><td>Transaction processing</td><td>Reporting</td><td>Decision support</td><td>Executive information system</td><td>Expert system</td><td> $Other^a$ </td></tr><tr><td>Finance and business services</td><td>12</td><td>11</td><td>2</td><td>-</td><td>-</td><td>1</td></tr><tr><td>Mining</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2</td></tr><tr><td>Government agencies</td><td>1</td><td>2</td><td>1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>IT/consultancy</td><td>11</td><td>3</td><td>1</td><td>2</td><td>1</td><td>5</td></tr><tr><td>Food</td><td>7</td><td>8</td><td>-</td><td>1</td><td>-</td><td>2</td></tr></table>

$^{a}$ Other applications: one research database application, one contacts database application, two system monitoring applications, two multimedia applications and four utility applications providing support to office applications.

Table 6 Completed projects classified by client/server type

<table><tr><td rowspan="2">Industry</td><td colspan="2">Client/server configuration</td><td rowspan="2">Distributed logic</td><td rowspan="2">Remote data management</td><td rowspan="2">Distributed database</td></tr><tr><td>Distributed presentation</td><td>Remote presentation</td></tr><tr><td>Finance and business services</td><td>2</td><td>7</td><td>12</td><td>5</td><td>7</td></tr><tr><td>Mining</td><td>-</td><td>-</td><td>2</td><td>-</td><td>-</td></tr><tr><td>Government agencies</td><td>-</td><td>-</td><td>1</td><td>2</td><td>-</td></tr><tr><td>IT/consultancy</td><td>3</td><td>2</td><td>10</td><td>3</td><td>-</td></tr><tr><td>Food</td><td>3</td><td>11</td><td>3</td><td>-</td><td>-</td></tr></table>

In terms of the Gartner Group model, the majority of competed projects were either remote presentation or distributed function (Table 6).

Most client/server projects used the IBM PC as the client hardware platform while VAX, HP/Sun workstations an IBM PCs were most often used as servers.

The majority of the client/server projects completed by the organizations surveyed have a relatively small user base with 32% of projects having between 11 and 50 users and another 32% having between 51 and 100 users.

## Development methodology and its appropriateness

Most organizations commented that the logical design phase is independent of the type of development. Certainly no respondent raised the issue of determining the requirements for various logical sites as suggested by Jain and Purao (1991). This is not altogether surprising given the simplicity of client/server development compared with the more general distributed application design. In fact Low (1997) recognized this by noting that it would be a relatively rare requirement for most commercial organizations.

Ten organizations (52%) used their normal development methodology for client/server application development. These organizations were relatively inexperienced with client/server application development with the majority having completed their first project within the previous 2 years. These projects were mostly simple, non-critical applications aimed at pilot testing client/server development. While most organizations did not see any difference in the design of client/server applications compared with traditional applications (“there is no difference between developing a client/server application compared to a traditional time-sharing application”), two organizations indicated that they would develop new methodologies specific to client/server development. These organizations planned to address the issues of task partitioning and task allocation in their new methodologies. This should ensure that performance is not impacted on by poor task partitioning and task allocation decisions (Anon, 1995).

The remaining nine organizations fell into two groups: organizations with tailored methodologies (five)

and organizations without formal methodologies (four) which generally relied on the experience of their project development teams to build client/server applications.

Organizations with tailored methodologies have experienced two major problems during the development of client/server projects. The most common problem was the absence of any formal method for the division of the application between client and server. These organizations stated that when they first commenced client/server development, they found that there were no techniques providing guidance on how to divide an application although most have now included support for task partitioning and task allocation in their methodologies. The other major difficulty encountered was the initial weakness of the development and design tools. When the organizations began client/server development they found that the development tools available were inadequate. These tools generally offered little support for developers. Gradually, the tools have matured, to such an extent that one organization noted that 'the software tools available are now able to assist developers in fully utilizing the client/server concept'. However, not all these organizations have adopted a single integrated methodology for client/server development. In fact one organization used a variety of different 'methodologies' for building client/server applications. It stated its development methods were appropriate to client/server development, as each method selected was considered the most appropriate for that particular stage of the development life cycle.

A number of organizations with tailored methodologies noted that project management is a key issue in client/server development. 'Client/server projects have a considerable level of risk associated with them. ... a formal management system is required to coordinate the project team and end users.' Low (1997) addressed this concern in the methodology enhancements under 'activity: develop management concerns'.

## Guidance in splitting the application

Four of the six organizations that considered ‘guidance in splitting the application’ as an important issue (rating 6 or 7) did not have methodologies that supported task partitioning or task allocation. However, they were generally fairly experienced in client/server development with two organizations having developed their first client/server applications 6 and 9 years ago. Organizations whose methodology supports task partitioning and task allocations already have a formal technique of splitting the application between client and server. Hence, they are less likely to feel the need for general guidance in splitting the application.

Five of the eight organizations (63%) that rated 'guidance in splitting the application' of little importance (rating 1 or 2) had completed their first client/server project within the previous 6–12 months and were not using a tailored methodology. These organizations had only developed reporting, research database and multimedia applications where there is less need for this guidance to ensure performance and reliability.

## Methodology's support for task partitioning

A total of nine organizations (47%) indicated that they performed task partitioning as part of their design process. Four of the organizations with tailored methodologies were included in this group. The remaining five organizations were from the normal methodology group.

Gomaa (1989) described a method a task partitioning that is based on data flow diagrams. Shatz and Yau (1986) outlined another method of task partitioning that involves the use of structure charts. The results indicate that, according to their methodology, organizations rated data flow diagrams slightly more useful in task partitioning than structure charts (Table 7).

This support for data flow diagrams is not surprising since they are generally used in industry. The three organizations that rated the use of structure charts lowest (rating 1–2) belonged to the normal methodology group. In addition these organizations had completed their first client/server project within the previous year.

Shatz and Wang (1989) suggested issues such as minimizing intermodule communication, exploiting concurrency and limiting the size of processes should be considered in task partitioning. Table 7 suggests that all three are considered relatively important although the organizations were not consistent in their ratings. For instance, one organization rated intermodule communications very important (rating of 7), exploiting concurrency very important (rating of 7) and limiting the size of processes not important (rating of 1). This difference in emphasis may be the result of the organization's environment where workstation memory has not been an issue but performance is an important concern.

Table 7 Relative importance of task partitioning issues

<table><tr><td></td><td>Median</td><td>Mode</td><td>Range</td></tr><tr><td>Data flow diagrams</td><td>5</td><td>5</td><td>4-7</td></tr><tr><td>Structure charts</td><td>4</td><td>5</td><td>1-6</td></tr><tr><td>Minimizing intermodule communications</td><td>5</td><td>6</td><td>1-6</td></tr><tr><td>Exploiting concurrency</td><td>4</td><td>6</td><td>1-7</td></tr><tr><td>Limiting the size of processes</td><td>4</td><td>4</td><td>1-6</td></tr></table>

In general the ratings were higher for organizations with tailored methodologies. Four of the five organizations that rated intermodule communications as important (rating 5–7) were using tailored methodologies. In addition, all these organizations had developed transaction processing systems. The only organizations that rated intermodule communications or exploiting concurrency of little importance (rating 1–2) were using their normal methodologies for client/server development. These results suggest that the ratings placed on various factors may be influenced by the support offered by the methodology and/or the type of applications developed. Further research should address this issue.

## Methodology's support for task allocation

A total of six organizations (31%) indicated that they currently performed task allocation as part of their development methodology. All five organizations with tailored methodologies were included in this group plus one organization from the normal methodology group. The methodologies for four of the nine organizations that supported task partitioning did not support task allocation. These four organizations were using their normal methodology for client/server application development.

The five main performance cost metrics for task allocation are interprocessor communications, interprocessor communication and execution cost, load balancing, completion time and reliability. The results are presented in Table 7. Reliability was universally regarded as the most important metric with all organizations regarding it as extremely important (rating of 7). The general importance of interprocessor communications is in line with the importance placed on intermodule communications in task partitioning. Many organizations were also concerned about the distribution of the application workload with one organization noting that it is more critical when the application has a high transaction volume.

The importance placed on the various metrics may be influenced by the type of application(s) being developed. Interestingly, the one organization that rated interprocessor communications, total interprocessor and execution cost and completion time as not important (rating of 1) had only developed multimedia systems while organizations that had implemented transaction processing systems rated the importance of these metrics much higher. It was also one of the two organizations that ranked intermodule communications in task partitioning as not important (rating of 1).

For some of the organizations, load balancing was an important consideration when performing task allocation. A possible explanation for this is that load balancing can improve the overall performance of an application (Kratzer and Hammerstrom, 1980; Chou and Abraham, 1982). One organization noted that 'load balancing appears to become more critical when an application has a high transaction volume'.

The reliability of applications is a very important consideration for all organizations. Bannister and Trivedi (1983) claimed that task allocation is optimized by balancing computational load and that in achieving a balanced load, the reliability of a distributed system is maximized. Hence, those organizations that are concerned with balancing their operational load are also helping to achieve their reliability goal.

Table 9 shows the importance to organizations of particular system constraints upon the task allocation process. Memory size appears to be a very important constraint for most organizations. This is not altogether surprising since the client platform most often used for client/server projects was a PC. The other constraints, processing capacity and number of processes, were considered slightly less important than memory capacity.

## Methodology for future client/server development

The majority of organizations reported that they will continue to use their current development methodology for future client/server development. This is not unexpected for organizations with tailored methodologies.

Table 8 Relative importance of task allocation metrics

<table><tr><td></td><td>Median</td><td>Mode</td><td>Range</td></tr><tr><td>Interprocessor communications</td><td>5</td><td>5</td><td>1-7</td></tr><tr><td>Interprocessor communications and execution cost</td><td>4</td><td>4,6</td><td>1-6</td></tr><tr><td>Load balancing</td><td>5</td><td>4,7</td><td>2-7</td></tr><tr><td>Completion time</td><td>4</td><td>1,2,4,5,6,7</td><td>1-7</td></tr><tr><td>Reliability</td><td>7</td><td>7</td><td>7-7</td></tr></table>

Table 9 Relative importance of task allocation constraints

<table><tr><td></td><td>Median</td><td>Mode</td><td>Range</td></tr><tr><td>Processing capacity</td><td>5</td><td>4,6</td><td>3-7</td></tr><tr><td>Limited number of processes</td><td>5</td><td>6</td><td>2-6</td></tr><tr><td>Memory size</td><td>6</td><td>6</td><td>37</td></tr></table>

However, a number of the organizations using their normal development methodologies have not considered issues such as how to divide the logic of an application between client and server (i.e. task partitioning and task allocation). These organizations may encounter problems with their methodologies in the future when undertaking more complex application development.

Of those organizations that planned to adopt a client/server methodology, all planned to develop it in-house. One organization commented ‘(We) intend to build up expertise in client/server development and gain a broad understanding of the options available before deciding upon two to three particular methods with which to develop applications’. The organization then planned to define and document standard methods or design templates for client/server applications. This approach is very similar to the template approach to application design suggested by Low (1997). A couple of organizations were also keen to incorporate prototyping support within the new methodology.

## Conclusion

This study provides an insight into the client/server development methodologies used by industry and the problems that organizations have experienced. It was found that over half the organizations used their normal development methodology for client/server application development. These organizations were relatively inexperienced with client/server application development, the majority having completed their first project within the previous 2 years.

The relative importance placed on the client/server application design techniques included in the methodology enhancements proposed by Low (1997) provides support for their application in a non-OO client/server commercial application development environment. All of the organizations with tailored methodologies performed task allocation. This reinforces the inclusion of this technique in both the subsystems approach and theoretical approach to application design (Table 1: see also Low, 1997). The Data Flow Diagram (DFD) approach to task partitioning outlined in the subsystems approach was slightly preferred over the structured chart approach in the theoretical approach. However, factors such as intermodule communications, exploiting concurrence and limiting the size of processes were important considerations to both groups. For those organizations requiring assistance in splitting the application between client and server but who do not want to adopt a more formal approach, the template approach to application design should be appropriate.

No organization considered determining the requirements of logical sites as suggested by Jain and Purao (1991) and incorporated by Low (1997) in activity:

user requirements and activity: application analysis in the proposed methodology enhancements. However, Low (1997) noted that this would be a relatively rare occurrence in client/server development.

These proposed methodology enhancements should assist organizations in ensuring that important design considerations are not overlooked. Unfortunately existing traditional development methodologies do not support these key distributed application design issues such as task partitioning and task allocation. The need for a methodology that supports client/server application design would appear to be particularly appropriate when organizations are relatively inexperienced in client/server development as evidenced in this study. The use of this methodology would be a major factor in identifying likely risks and ensuring they are addressed during the design and implementation of client/server systems.

## References

Anon (1995) Performance and tuning in the client/server world. Capacity Management Review, 23(5), 1–13.

Bannister, J.A. and Trivedi, K.S. (1983) Task allocation in fault-tolerant distributed systems, Acta Information, 20, 261–81.

Buzzard, J. (1990) The client/server paradigm: making sense out of the claims. Database Advisor, 8(8), 72–80.

Chou, T.C.K. and Abraham, J.A. (1982) Load balancing in distributed systems, IEEE Transactions on Software Engineering, 8(4), 401–12.

Colony, G. (1990) President of Forrester Research Inc., reported by Mead, T. the attraction is price. Datamation, 36, 15 March, 49–51.

Davis, D. (1991) Where client/server fits. Datamation, 37, 15 July, 36–8.

Francis, B. (1990) Client/server: the model for the '90s. Datamation, 36, 15 February, 34–40.

Gomaa, H. (1984) A software design method for real-time systems. Communications of the ACM, 27(9), 938–49.

Gomaa, H. (1989) A software design method for distributed real-time applications. The Journal of Systems and Software, 9(2), 81–94.

Jain, H.K. and Purao, S. (1991) Distributed application development: SDLC revisited. Information and Management, 20, 247–55.

Kratzer, A. and Hammerstrom, D. (1980) A study of load levelling, in Proceedings of Computer Conference, pp. 647–54.

Levy, E. and Silberschatz, A. (1990) Distributed file systems: concepts and examples. ACM Computing Surveys, 22(4), 321–74.

Levy, H. and Tempero, E. (1991) Modules, objects and distributed programming: issues in RPC and remote object invocation. Software: Practice and Experience, 21(1), 77–90.

Low, G.C. (1997) Methodology Enhancements for Client/Server Development (Technical report 96/5, Centre for Advanced Empirical Software Research, University of New South Wales).

Low, G.C. and Russell, P. (1993) Application of the client/server model on LANs, in Proceedings of the Conference on The Open Systems Future: Leveraging the LAN, Perth, pp. 107–22.

Low, G.C., Henderson-Sellers, B. and Han, D. (1995) Comparison of object-oriented and traditional systems development issues in distributed environments. Information and Management, 28(5), 327–40.

Low, G.C., Rasmussen, G. and Henderson-Sellers, B. (1996) Incorporation of distributed computing concerns into object-oriented methodologies. Journal of Object Orientated Programming, 9(3), 12–20.

McGoveran, D. and White, C. (1990) Clarifying client/server.
DBMS, 3(12), November, 78–90.

Philipson, G. (1993) In search of client/server. Informatics, 1(6), August, 23–8.

Sagar, G. and Sarje, A.K. (1991) Task allocation model for distributed systems. International Journal for Systems Science, 22(9), 1671–8.

Shatz, S.M. and Wang, J.-P. (1987) Introduction to distributed software engineering. IEEE Computer, 20(10), 23–31.

Shatz, S.M. and Wang, J.-P. (1989) Tutorial: Distributed Software Engineering (Washington, DC, IEEE Computer Society Press).

Shatz, S.M. and Yau, S.S. (1986) A partitioning algorithm for distributed software systems design. Information Sciences, 38(2), 165–80.

Svobodova, L. (1984) File servers for network-based distributed systems. ACM Computing Surveys, 16(4), 353–98.

Wadhwa, V. (1995) Partitioning applications: what are the issues? Unix Review, 13(5), 35–8.

## Biographical notes

Dr Graham Low is a deputy director of the Centre for Advanced Empirical Software Research at the University of New South Wales. His main research interests are in software engineering with a particular interest in distributed application development and its enabling technologies such as object-oriented development and networking. An important part of this research programme is the conduct of empirical studies in industry. Prior to joining the university in 1987, Graham was Technical MIS Manager for the Sugar Division of CSR.

Richard Looi graduated from the University of New South Wales with a BSc degree in business information technology in 1994. He has worked for the Prince of Wales Hospital in client/server development. he is currently working for Rothschild Australia. His research interests are in client/server application development and Internet site development.

Address for correspondence: Dr Graham Low, Centre of Advanced Empirical Software Research, School of Information Systems, University of New South Wales, Sydney, Australia 2052.
