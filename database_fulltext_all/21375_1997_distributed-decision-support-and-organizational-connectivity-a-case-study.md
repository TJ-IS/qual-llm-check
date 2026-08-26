---
otero_id: 21375
otero_key: "8M8AZR65"
title: "Distributed decision support and organizational connectivity: A case study"
authors: "Manfred A. Jeusfeld; Tung X. Bui"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00057-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Distributed decision support and organizational connectivity: A case study

Manfred A. Jeusfeld $^{a,1}$ , Tung X. Bui $^{b,*}$

$^{a}$ Aachen University of Technology, Achen, Germany

$^{b}$ The U.S. Naval Postgraduate School, Department of Systems Management, Monterey, CA 93943, USA

Received 30 August 1995; revised 2 February 1996

## Abstract

While the Internet has been grabbing most of the attention of the information systems researchers and practitioners, online transaction processing systems still take the lion's share of business information systems. Although many Decision Support Systems (DSS) have been developed, they failed to become mainstream products due to their limited availability, applicability, and interoperability. In this paper, we propose a script language to make use of the vast resource of the Internet as a means (i) to better make DSS known to potential users, and (ii) to allow construction of DSS from DSS components stored on various Internet sites. With the proposed script language, we contend that DSS would have a greater potential of gaining a larger share of use among the business community. Contrasting to other approaches that advocate for a central clearinghouse of DSS components, we propose a bottom-up strategy, i.e., users and developers of DSS's cooperate in weaving a web of distributed DSS components to form a federated network of on-line DSS repositories. The purpose of the proposed script language is to ensure effective search of DSS components and rapid development and deployment of application-specific DSS. The proposed method is scalable to support distributed platforms using multiple processors and/or application domains. A case study derived from a real life application in a multi-national company is discussed to illustrate the proposed approach.

Keywords: Decision support system; Distributed processing; Internet/Intranet; Data and model repository; World-Wide-Web

## 1. Introduction

According to surveys by PCWeek (December 1994) and the Financial Times (April 1996), the deployment of Decision Support Systems (DSS) across organizations is rather limited. There are at least three reasons that explain this poor distribution of DSS:

\- Difficulty in matching problems to appropriate DSS: Decision makers often experience difficulties in finding available analytical models suitable to their decision problems.

\- Up-to-date DSS are not easily accessible: A comprehensive model-base is hard to maintain as models and tools are continuously updated or introduced.

\- DSS are often too application-specific: Models have different assumptions about the input/output formats; some of these assumptions are implicit, i.e., not visible in the declared format.

With the explosion of Internet use, and recently with the Intranet phenomenon, many academic institutions have started making their DSS components available to potentially interested decisions makers. Bhargava et al. [3] cite three factors contributing to this trend. They argue that, due to the currently limited size of the market for decision support technologies, there is a market potential for DSS deployment on the World Wide Web (WWW). More important, DSS availability on the WWW could eliminate, or at least reduce, the costs and problems related to the issue of “re-inventing the wheel” and version management. Goul et al. [8] view DSS deployment on the Internet as an innovative means to (i) help discover opportunities for using newly developed DSS, (ii) validate DSS, including continuous feedback on their usefulness and performance, and (iii) promote wider dissemination of DSS via training.

From an operational point of view, the goal is to match the demand and the service of DSS with much lower overhead costs than those of a more conventional method of DSS distribution. Ideally, a decision maker should be able to combine suitable DSS components in the same way that he/she builds and uses functions in a spreadsheet, without having to be concerned with installation of the components in his/her computer environment. An Internet-based usable system must provide answers to the following questions:

\- How can a complex decision problem be planned using distributed DSS components as an Internet-based approach to model integration? Our answer is a script language with a graphical and a textual representation.

\- How can users access appropriate DSS components dispersed in the potentially unlimited Internet search space? Here, we suggest the adoption of Uniform Resource Locators (URL) known from the World Wide Web to allow identification of DSS data, scripts, models, and programs.

\- How can data objects be transformed into the format expected by a DSS component? We propose a version of the uniform data exchange to minimize the handshaking between sender and receiver of DSS data, and to allow a data item be stored independently from its originator.

\- How can the Internet traffic be minimized when data/script objects are at distant nodes? Here, thanks to the simplicity of our script language, optimization techniques can be applied to use the Internet traffic effectively.

Our approach is germane to the framework of the “enterprise information bus” by Ba et al. [1], yet avoiding the requirement of having a central agent. To allow distributed management of all resources (DSS script and data objects), we present two design principles: A uniform data representation as a prerequisite for exchanging information between heterogeneous systems; and uniform naming for identifying input/output data as well as the DSS components that participate in a decision process. In addition, we advocate the implementation of repository systems to provide DSS users with the knowledge to design distributed decision support scripts, and to aid the installation of DSS components across the Internet.

Felter [6] proposes a Decision Support Assistant (DSA) for local area networks (LANs). As an intelligent assistant, DSA helps a decision maker invoke DSS components from a model base. Felter studies interference of concurrent tool invocations and notices the limited processing time resources. In our approach, the control of the DSS components is more complex than that in a LAN. The main difference is the degree of distribution. In Felter's approach, all DSS components are controlled by a central DSA. In ours, we contend that a central control is neither practical nor desirable. In that regard, we depart from the “brokers-agent” concept proposed by Bhargava et al. [4]. Potential DSS users do not need to buy the service of a broker to make use of distributed computational resources on the Internet.

## 2. A Corporate-wide financial application example

To illustrate the approach set forth in this study, a case study adapted from a real-life application is presented. Rubber International (RI) (this is an altered name) is a multinational company with its headquarters located in North America. With annual sales reaching \$1.5 billion, RI has its operation worldwide. With a variety of products offered, RI seeks to constantly monitor its markets regionally. To align with its geographically distributed sales, RI information systems architecture is also distributed with major computing hubs located in Montreal, Canada, Strassbourg, France, and at various regional computing centers, e.g., in Fribourg, Switzerland.

As part of its decision support and executive information systems, RI has developed a financial planning system using a well-known software for financial planning that runs on both the mainframe and the PCs. The purpose of the system is to help management establish annual and 5-year budgeting. In particular, the DSS focuses on three main functions:

\- short term and long term strategic planning

\- cash flow management, and

• routine and ad hoc data analysis and reporting.

Fig. 1 shows an excerpt from the current federated DSS architecture of RI. The European headquarters in Strassbourg maintain financial data and models for the company's operations in Europe. Regional centers, such as the one in Fribourg, Switzerland, feed the headquarters with their operational data. In return, they also download central data for their local decision making. Some financial data and models are kept locally at the regional centers. Both the headquarters and the regional computer centers possess their own DSS components for evaluating the financial models on the financial data. Spreadsheet programs running on personal computers serve for visualizing results of the analysis. The networking of RI's federated DSS architecture has been implemented by leased data communication lines and ded icated communication protocols. The location of the financial data and models were determined in group meetings between the headquarters staff and the regional centers staff.

![](/api/attachments/8M8AZR65/fulltext/images/1e1f34b59e1e20eb0fcf24583cdd37dd7dc649a5093b82e2c3e77ed1ce92da85.jpg)  
Fig. 1. Architecture of an existing federated DSS.

![](/api/attachments/8M8AZR65/fulltext/images/d6eae4e19cf505962d06e17402004b3e15af0b42e0c8544d1a900ac6b794ce5d.jpg)  
Fig. 2. A script for financial analysis (from RI).

Scripts for computing an analysis were specified by semi-formal data flow diagrams (see Fig. 2), and then implemented by a 4GL language. The boxes on the left-hand side represent financial data (i.e., data regarding exchange rates for currencies, and worldwide financial data of the corporation), the boxes in the middle of the figure represent financial models that define how to extract relevant information from the data (i.e., model to compute profits based on sales volume, break-even analysis, conversion of currencies, forecasting models), and finally the box “PRINT” defines output formats. RI also has developed scripts with loops, allowing monthly use of models for the fiscal year.

The example shows that knowledge about the DSS is spread in heterogeneous documents (i.e., data, models, scripts). Interoperability, i.e., the ability to pass data between systems without information loss, is ensured by using the same software packages and by dedicated transformation routines (wrappers). Scripts have a Janus nature: on the one side, they can be viewed as a high level programming language; on the other side, they define a semantic relationship between data and models.

## 3. Overview of the proposed federated system

We use the setting of RI as a running example for our method of integrating DSS components on the Internet. Our goal is to provide a saleable method where data, models and processors may be located anywhere on the network. Users (decision makers, analysts, DSS software providers, etc.) of the proposed federated architecture should be able to exchange information after an agreement on location, representation and interpretation of the information has been reached. The users may be in different departments of the same company but may also be from different cooperating companies.

![](/api/attachments/8M8AZR65/fulltext/images/3f46acb9cf05b1d1d3f23b7d90f72fecd9a382c8439967673c214d8265efeae7.jpg)  
Fig. 3. Overall architecture of the proposed federated DSS, (Selling-Data-1995, Selling-Vector, ((Q-1, K-CAN\$, 1033), (Q-2, K-CAN\$, 948), (Q-3, K-CAN\$, 1018), (Q-4, K-CAN\$, 316))).

Fig. 3 shows a simplified view of a network of DSS processors and repository systems (labeled “Can” and “Eu” in the Figure) connected by the Internet (visualized by the thick lines). The rectangular nodes represent DSS processors, i.e., programs that process information relevant for some decision. The cylindrical nodes (here “Can” and “Eu”) are examples of repository systems. The repositories constitute the foundation of the overall system in that they serve as the main information resource to support discovery and composition of Internet-based DSS components. The repositories can be implemented by a standard database application program, or by knowledge-based systems, each dedicated to a specific application domain or purpose (e.g., repository of financial applications, repository for statistical procedures, etc.).

Each repository creates its own name space, i.e., the set of stored uniform names for script and data objects. Specialized name spaces are justified for several reasons. First, different groups of decision makers are interested in different DSS components. Second, and more importantly, distributed repositories create a higher degree of security because script and data objects are known only to those users who have access to the repository.

One of our goals is to help DSS providers promote the access and use of their systems. The overall system can be continually updated by installing new DSS processors:

1. A user (system administrator or even decision maker) browses a repository, looking for DSS processors suitable to her problem definition, and selects one.

2. The repository is queried for the installation procedure of the selected DSS processor(s).

3. The installation procedure is downloaded to the local system and executed, provided the features of the procedure conforms to the local system configuration.

4. At the end of a successful installation, script objects for calling the new copy of the DSS processor have to be inserted in the local repository (uniform name, input/output types, etc.).

As more and more copies of the same DSS package are spread over the network, redundancy can be exploited for optimizing the load balance of the system (see Section 5). A DSS provider “publishes” a new DSS component by inserting its features in the repository system known to him. This can include a test installation at the local site of the DSS provider to help potential users test the component(s).

## 4. Interoperability techniques

Let's consider the following generic scenario. A DSS component P1 produces a data object O1 which is later used by DSS component P2 as input. The DSS components are autonomously developed and the data exchange via O1 may not have been planned at the time P1 and P2 were designed. The traditional approach is to store data in a (central) database for later processing (e.g., [12]). For this purpose, the schema of the database must be known in advance and is relatively fixed. In our approach, data as well as script objects are assumed to be distributed and no common type system is enforced.

Remember two principles for distributed processing: first, data can be packaged into a transferable exchange format similar to IDL [9]; second, Uniform Resource Locators (URL) [2] can be used to identify DSS components installed on the Internet.

## 4.1. Uniform data representation

We regard any data as a string of bytes to be received and interpreted by the DSS9 component which processes it. This option requires external knowledge about the kind of data, and is therefore not suitable in distributed environments where data and script objects evolve without central control.

There are several similar approaches from the areas of distributed systems, heterogeneous databases, and distributed artificial intelligence coping with the problem of data exchange. We adopt the OEM format [10] which incorporates the type information within each data object, i.e., the data structure can be retrieved from the object representation. Objects are represented as terms (n, t, v) where “n” is the name of the object, “t” is its type and “v” is its value. The value is either a constant of a base type or a term. As an example, consider the definition of a vector of currency units in Fig. 4. The building principle of OEM objects are triplets “(instance-name, type, value)”. The first component identifies the object, the second is the name of the type of the object, and the last is the value. OEM objects may be arbitrarily nested. Nested objects can be identified by a path expression, e.g., “Selling-Data-1995.Q-2” identifies the Canadian dollar amount 948 (in thousand). Such a representation makes a data object independent from type systems of programming languages: it simply carries its type definition with it. A system that reads such a term can extract the type information and match it against its own type system.

## 4.2. Uniform naming

The input of DSS scripts are data objects that may reside on one or more (remote) locations. Therefore,

$$
\begin{array}{l} \text {(Selling - Data - 1995, Selling - Vector,} \\ \quad (\quad (Q - 1, K - C A N , 1 0 3 3), \\ \quad (Q - 2, K - C A N , 9 4 8), \\ \quad (Q - 3, K - C A N , 1 0 1 8), \\ \quad (Q - 4, K - C A N , 3 1 6) \end{array}
$$

Fig. 4. OEM object of type matrix, (Earning–Forecast–1995, po-call, ((po-node, url, http://fribourg.rubber.ch/bin/IFPS), (arg-1, url, http://fribourg.rubber.ch/local/BUSMOD.ifps), (arg-2, url, http://strassbourg.rubber.fr/finance/Selling-Data-1995.oem), (arg-3, po-call, ((po-node, url, http://strassbourg.rubber.fr/bin/IFPS), (arg-1, url, http://strassbourg.rubber.fr/local/XSBC.ifps), (arg-2, url, http://strassbourg.rubber.fr/local/Exchange-Rate-1995.oem))))).

both data objects and script objects must be identifiable across system boundaries. Uniform resource locators (URL) [13] serve this purpose. The general format is

## protocol://node-address/path

The component “protocol” specifies the communication protocol used to transfer data or to activate a remote process. We assume the widely-used protocol “http” in the following. The “node-address” uniquely identifies the computer system which hosts the requested data or script object. Finally, the “path” identifies the object within the name space of the local computer system. For example, the URL

## http://strassbourg.rubber.fr/finance/Selling

\- Data - 1995.oemm

uniquely identifies location of the data object Selling-Data-1995 in the file system of the computer “strassbourg” of organization “rubber” in France. Via the transfer protocol “http”, it is technically accessible from any node in the network in which “strassbourg” participates. We assume that any persistent data object, i.e., a data object that exists beyond the processing time of the script objects that produced or consumed it, is represented in a file with extension “oem” indicating that its content is in OEM format.

A call to a DSS processor is also be named via URLs. The format resembles a procedure call with input parameters referenced by their URLs. For example, the URL

http://fribourg.rubber.ch/bin/IFPS?call
= http://strassbourg.rubber.fr/scripts/Earning
- Forecast - 1995.oem

invokes the DSS processor IFPS (actually a financial analysis package) at Fribourg to evaluate on the input object Earning–Forecast–1995.oem located in Strassbourg. As specified in the HTTP protocol, such an URL names the result of the evaluation. This is exploited in the definition of script objects below.

Fig. 5 shows a script object where all objects reside on different nodes in the Internet. The script object Earning–Forecast–1995.oem encodes the call of the DSS processor IFPS at Fribourg, and the arguments of the call which are either URLs of data objects or calls of component scripts. Argument arg-1 of Earning–Forecast–1995 is financial model

![](/api/attachments/8M8AZR65/fulltext/images/60b63c099ed08c9aef405e950875a8a1fc005bfd8661bf5ec06bafacfc46d6d1.jpg)  
Fig. 5. OEM representation of a script object.

BUSMOD, arg-2 is Selling-Data-1995 from Strassbourg, and arg-3 is the result of a nested call to another DSS processor IFPS at Strassbourg.

The evaluation of a script object is explained in Section 5. For the moment, it is sufficient to note that the script object encodes a data flow diagram as depicted in Fig. 6. Also note that a script object is in OEM format like the data objects! Therefore, it may be the output of a compiler script. Furthermore, it can be classified in the repository presented in Section 4.

The URL conventions are sufficient to invoke a remote DSS component with local or remote input objects and to receive the result in as a single object in OEM format. Legacy DSS components can be integrated by a transducer $[7]$ which mediates between the network and the DSS component. The transducer accepts the call in the above syntax, transforms the (input) data into the internal representation for the legacy DSS component and then invokes it.

The proposed approach is well-suited for DSS components with no user interaction, i.e., those that are linked with other DSS components. The design of local user interface should not impose principal obstacles (i.e., at the client site in a client/server framework). An elegant way is to install a specialized DSS processor on the computer system of the user. This processor accepts requests from the remote DSS component via the URL call mechanism shown above. Locally, it gathers the input from the user by an appropriate input device.

![](/api/attachments/8M8AZR65/fulltext/images/b371eb5ed5053deadad4d380502f5a2af2d5b0e9fc9d9f6db9045e9c4aa3e3d8.jpg)  
Fig. 6. Diagram denoting a distributed DSS script.

## 5. The repository

Uniform data representation and naming described above provide the basic framework for communication between distributed DSS components. We propose a repository which stores conceptual information about data objects as well as script objects and answers queries based on classification hierarchies.

## 5.1. Persistent data objects in the repository

Each data object is in OEM format. Thus, its type can be extracted from its representation and be used for classifying it in the repository. We use the statement “OBJECT x IN T” to express that an object “x” is an instance (element) of type “T”. The type is represented as a term over the type constructors and base types (given by their name). For example, the most specific type of Selling-Data-1995 is Selling-Vector(K-CAN\$,K-CAN\$,K-CAN\$,K-CAN\$). Consequently, the data object is represented in the repository as:

OBJECThttp://strassbourg.rubber.fr/finance/

$$
S e l l i n g - D a t a - 1 9 9 0. o e m \in S e l l i n g - V e c t o r
$$

$$
(K - C A N , K - C A N , K - C A N , K - C A N)
$$

Membership of the data object to more generic types like Selling-Vector(Int,Int,Int,Int) can be derived provided Int is a more generic type than K-CAN\$. We express such generalization in the repository by a statement “K-CAN\$ ISA Int”. Further classifications can be obtained when additional attributes about the data object are provided. Such attributes are highly domain-specific, especially when data objects come from different organizations. Therefore, it is difficult to prescribe a set of attributes to be used. Book-keeping features like “creator”, “creation-date”, “valid-thru”, and “comment” are reasonable first choices. Semantic information explaining the meaning of a data object, its problem class and applicable models is more useful for data classification but requires a common terminology among the users of the repository (which is beyond the scope of this paper). In our running example, the attributes could be as follows:

K - CAN\$ISA∫

...

OBJECThttp://strassbourg.rubber.fr/finance/

Selling - Data - 1995.oem

∈ Selling - Vector(K - CAN\$, K - CAN\$, K -

CAN\$,K - CAN\$)

WITH ATTRIBUTE

creator: "FrancoisNome";

creation - date: “4 - Nov - 1995”;

valid - thru: “31 - Dec - 1995”;

remark - 1: “entries correspond to quarterly selling

of Rubber - Europe";

END

## 5.2. DSS-Scripts

DSS-Scripts are special data objects that describe a computation for a certain decision problem. In the example below, the script Earning–Forecast–1995 is defined with two arguments of type IFPS-Model (a plain text) or Selling–Vector, respectively. The result is expected to be of type matrix(Int). Note that the input and output signature can be used for searching for data objects matching a script's signature and for checking type conformance.

OBJECT http://strassbourg.rubber.fr/scripts/

Earning - Forecast - 1995.oem

∈ DSS - Script

WITH ATTRIBUTE

arg -- 1: IFPS - Model;

arg -- 2: Selling - Vector( f );

arg -- 3: Exchange - Vector (pair( $\Re, \Re$ ))

result: matrix( Int )

preferred - processor: http://fribourg.rubber.ch/bin/IFPS

END

The processors of scripts (attribute preferred-processor in the example above) are DSS software packages installed on some computer in the network. It may well be that the same DSS package is installed on several nodes. Then, there is a choice for the evaluation strategy of the script. In the repository, we store a statement like:

OBJECT http://fribourg.rubber.ch/bin/IFPS

EQUIVALENT - TO http://strassbourg.rubber.fr/

software/bin/IFPS

to represent this fact. It is used for the run-time scheduling of the evaluation of a task.

Some scripts may have the only task to filter, transform or display some data objects. They constitute no special case. For example, the result of Earning–Forecast–1995 may be transformed into a spreadsheet format and then displayed by a standard spreadsheet package.

## 6. Implementation steps

To implement the proposed approach, two principle steps are required. First, the DSS components have to be connected to the Internet, and second, they must be updated in the repository for identification.

## 6.1. Connecting DSS components to the Network

Our approach relies on standard protocols and interfaces. Therefore, setting up a running system only requires a fair amount of programming. First, the DSS processors must be accessible from distant nodes. This can be achieved by installing a so-called HTTPD server [WWW-Consortium 95] on the local node. The server has the basic function of accepting calls from the Internet and returning some result (in our case data objects). It can be configured to transfer all calls with the right URL to the local DSS component. Second, a local DSS component must be able to retrieve the arguments of a call (as encoded in the script object), i.e., to call itself remote HTTPD servers. The standard-compliant library “libwww” for this script is freely available from [13]. Fig. 7 shows a schematic view of a DSS component linked to the WWW.

![](/api/attachments/8M8AZR65/fulltext/images/078849945962530f877abd1fd0021625b6f35c90fe2a81845759248e26268ec0.jpg)  
Fig. 7. Schematic architecture of a DSS processor linked to WWW.

This architecture allows a user to activate a DSS processor from a remote node with a certain script object. As third and final requirement for the connection, the arguments and the result of a call to a script are expected to be in OEM format. Therefore, the DSS processor must be able to read/write such a format and transfer the values to and from its internal format. The effort for this function is minimal once the OEM format is known. A script is invoked by submitting a call like:

## http://fribourg.rubber.ch/bin/IFPS?call = http://strassbourg.rubber.fr/scripts/Earning - Forecast - 1995.oem

to the HTTPD server of a suitable processor. The DSS processor then fetches the script object (here Earning–Forecast–1995.oem) through its libwww interface. Argument descriptions in the script object which are of type “po-call”, for example arg–3 in Fig. 5, are stored on a local file. e.g. http://fribourg.rubber.ch/temp/arg–3.oem. Thereby, the local DSS processor can issue the corresponding call, in our running example:

$$
\begin{array}{r l} & h t t p: / / s t r a s s b o u r g. r u b b e r. f r / s o f t w a r e / b i n / I F P S? \\ & \quad c a l l = h t t p: / / f r i b o u r g. r u b b e r. c h / t e m p / a r g \\ & \quad - - 3. o e m \end{array}
$$

in the same manner it was called itself. The local DSS processor at Fribourg may well deviate from the preferred processor specified in the script and call instead an equivalent processor, e.g. the IFPS package at the local site. This scheduling requires no central control and is guaranteed not to influence the result of the computation. Of course, the DSS processors must be equivalent. Finding equivalent processors is done by a query to a (local or remote) repository.

## 6.2. Searching the repository

The main functions of the repository system are to store the properties of data and script objects as shown above, and to facilitate searching for information about data and script objects. Three search strategies are discussed below.

## 6.3. Simple search for scripts

Assume a decision maker has a problem encoded by a single input data object and wants to find a suitable collection of DSS components. The solution can be determined by matching the type of the data object with the input argument types of the DSS scripts stored in the repository. The search may be limited by conditions on the features of the DSS script. The search is efficient, more exactly, it is linear in the number of objects in the repository. Indexes on the input argument feature can speed up the average case performance to constant time.

## 6.4. Chain search for scripts

Assume that the repository contains some data transformation scripts P1,...,Pk such that the input argument of P1 matches the input data object and the output for Pi (i=1,...k-1) matches the input of Pi+1. Then, suitable DSS scripts can be obtained by searching such chains and then finding a DSS scripts whose input matches the output of Pk. This search delivers more alternative solutions than the simple search depending on the number of data transformation scripts known to the repository. This search is linear in the number of matches between input and output argument types of DSS components in the repository. In the “worst” case (i.e., every output type can be transformed to every output type), it is quadratic in the number of DSS components. The quality of the search, and subsequently, the problem solution depend on the completeness of the set of transformation scripts

## 6.5. Interactive script object generation

This is both the most useful and most difficult search. It assumes that the decision maker has more than one data object as problem definition and that some goal objects have to be computed by a complex sequence of DSS scripts. Theoretically, all combinations of chains, each starting with one of the input data objects, are applicable. Indeed, the number of combinations explodes as the number of input data objects and available scripts increases. The problem of finding a suitable script object is similar to scheduling problems. Since the repository has incomplete knowledge about the available script objects (only input/output types plus some features) and about the goal of the decision maker, we propose an interactive approach to construction of the script object. The user incrementally builds the script starting from the input data objects. Simple and chain search are used as auxiliary functions which offer the decision maker a choice of possible component scripts operating on a selected data object (either input data object or output of a script object). After validation the generated script may be included in a repository for later use and re-use (then being component of other scripts).

## 6.6. Implementation Properties

The script objects encode functional expressions on data objects (OEM format). The functions are denoted by the URLs of the DSS processor, and the arguments are either functional expressions or URLs of data objects. We assume the following computational model for DSS processors:

## 6.6.1. Persistent data objects are never updated after their creation

That means that the OEM term referred to by an URL is always the same. This property is analogous to the treatment of variables in functional and logic programming languages. It is different from the destructive updates allowed in imperative programming languages. The result of a script object only depends on its input objects. As a consequence, two calls of the same DSS processor will have the same result if and only if the input objects are persistent data objects.

The computational model allows application of several heuristics for optimization of script objects.

\- Lazy evaluation lets arguments be evaluated only when actually requested. This heuristic reduces the overall load on the network. Its implementation tion is not trivial because it affects the internal routines of the DSS components.

\- Caching materializes results of sub-expressions (parts of script objects which are of type “po-call” for speeding up subsequent calls of the same sub-expression. Caching makes most sense for script objects having only persistent data objects as input since their result never changes.

\- Multi-processing allows arguments of a script object which are of type “po-call” to be called in parallel. This strategy is the opposite to lazy evaluation and will speed up response time provided the calls go to distant idle nodes in the network. A precondition for this strategy is that the parallel calls do not interfere with each other. This can be achieved by forbidding updates to persistent data objects.

\- Load balancing can be enforced to optimize network traffic. Calls to DSS processor (named by their URL in the script object) can be replaced by calls to “equivalent” script objects located elsewhere. Load balancing can be incorporated before evaluation (compile-time approach) or during evaluation (run-time approach). Since DSS processors may be installed redundantly at any time on any node in the network, the overall system is saleable to the workload. There is no need of central control. The heuristics can be applied with the (limited) knowledge of the local repository system.

Script objects are hierarchical, i.e., they do not contain loops. The evaluation of a script object will terminate if the evaluation of its components (either task objects or data objects) terminate. We conclude the following property:

## 6.6.2. The evaluation of script objects will always terminate under a sound evaluation strategy (e.g., top-down, depth-first)

This property allows DSS users not familiar with programming languages to design them without fearing to consume too much resources of the network. Indeed, the resource consumption can be estimated from a script object definition. The total processing time is the sum of the processing times of the component scripts in the script objects, i.e., it is linear in the size of the script object. The processing times of the individual calls to DSS processors are in general indefinite. Response time, i.e., the time between calling a script object and receiving its result, depends on the degree of multi-processing. The minimal response time is the processing time divided by the number of distinct nodes involved in the processing. The actual response time also depends on data dependencies and the network bandwidth. Network costs (measured in the amount of data to be transferred between distinct nodes) is also linear in the size of the script object since in the worst case only as many transfers occur as there are DSS processors referred to in the script object. Network costs are also linear in the size of the input data objects provided that the result of any call to a DSS processor is linear in the size of its inputs. This is a reasonable assumption for DSS components since their purpose is to reduce decision problems on large data sets to a small number of choices. Network costs can be reduced to zero by installing any DSS processor referred to in the script object on the local node of the Internet. This is an extreme case of load balancing whose expenses are strictly those from local resources.

## 6.7. Integrity and control

On first sight, the distributed approach on the Internet bears the danger of uncontrolled access to models which where never meant to be combined. The reader should however note, that the repositories are specifically used to define a name space of meaningful data and scripts objects for a certain group of users. In the extreme case, a repository can just cover the objects on a local computer network. On the other hand, even small organizations have worldwide connections and will need the techniques for global decision support. The repository for such an organization may and should be restricted to cover those distributed objects important for its business.

As seen for the application of electronic data interchange (EDI), distribution of information processing requires a clear understanding of the business processes of the participating organizations. We assume that this understanding has been reached prior to the exchange of models and software. The “global” DSS, i.e., the sum of all data and script objects on the Internet, can never assumed to be consistent. Instead it is the resource from which consistent subsets (maintained in the decentralized repositories) can be extracted. This global resource will increase in value when more and more data transformation scripts are published in the repositories. They are in fact the tools for enabling interoperability.

## 7. Final remarks

A combination of three elements describe our approach. Uniform naming of script and data objects allows the programs and data to be located anywhere in the Internet. A uniform data format, OEM, allows data exchange independent from the implementation language of the DSS components. Finally, decentralized repositories support the design of distributed scripts and the evolution of the overall system by providing users with semantic information.

The proposed approach relaxes the necessity of having central control of the overall system. While the lack of a central clearinghouse creates some drawbacks, e.g., problem formulation, book-keeping issues, our approach empowers an unlimited number of decision makers (users) and DSS providers to participate in the growth of the overall system. It also provides more flexibility in terms of DSS proliferation, diffusion and use. Utilizing widely accepted protocols for data exchange keeps the implementation costs reasonably low. Also, the effects of low bandwidths of existing Internet traffic can be reduced by duplicating DSS processors on the nodes (computers) where the data reside, and a large number of nodes can be exploited via multi-processing.

Future efforts should concentrate on more sophisticated search facilities for the repositories and quality control of retrieved DSS scripts. Two other research issues are the cooperation among several decision makers and guidance in long-term decision processes. The approach presented in this paper has only marginal support for several decision makers cooperating in a decision script. To extend our approach to real cooperation, one has to embed the individual script objects into complex script or process languages $[5]$ . Then, loops for scripts are likely to become an issue. We are currently investigating such limited forms of such loop concepts.

## Acknowledgements

This research was conducted while the authors were at the Hong Kong University of Science and Technology, Department of Information and Systems Management. The authors would like to thank Mr. Daniel Jorio for his contribution to the case study.

## References

[1] S. Ba, Kalakota and A.B. Whinston, Executable Documents as the Basis for DSS, Proc. of the 3rd Int. Conf. on Decision Support Systems, Hong Kong, 22–23 June 1995, pp. 373–380.

[2] T. Barners-Lee, Uniform Resource Locators, Document http://www.w3.org/hypertext/WWW/Addressing/URL/URL\_TOC.html, 1995.

[3] H. Bhargava, A. King and D. McQuay, DecisionNet: An Architecture for Modeling and Decision Support over the World Wide Web, Proc. of the 3rd Int. Conf. on Decision Support Systems, Hong Kong, 22–23 June 1995, pp. 499–505.

[4] H. Bhargava, R. Krishnan and D. Kaplan, On Generalized Access to a WWW-based Network of Decision Support Services Proc. of the 3rd Int. Conf. on Decision Support Systems, Hong Kong, 22–23 June 1995, pp. 507–515.

[5] C.A. Ellis and M. Jarke (eds.), Distributed Cooperation in Integrated Information Systems, Proc. of the 3rd Int. Workshop on Intelligent and Cooperative Information Systems, Report AIB-92-18, RWTH Aachen, Germany, 1992.

[6] R. Felter, Decision Support Assistant, Deutscher Universitätsverlag, Wiesbaden, Germany, 1989.

[7] M.R. Genesereth and S.P. Ketchpel, Software Agents, Commun. ACM, 37, 7 (1994) pp. 48–53 and 147.

[8] M. Goul, A. Philippakis, M. Kiang, D. Fernandes and B. Otondo, Towards a Client/Server Open-DSS Protocol Suite for Automating DSS Deployment on the World Wide Web, Proc. of the 3rd Int. Conf. on Decision Support Systems, Hong Kong, pp. 517–528.

[9] J.R. Nestor, J.M. Newcomer, P. Gianni and D.L. Stone: IDL —The Language and its Implementation, Prentice Hall, 1990.

[10] Y. Papakonstantinou, H. Garcia-Molina and J. Widom, Object exchange across heterogeneous information sources, Proc. of the 11th Int. Conf. on Data Engineering, Taipei, Taiwan, 6–10 March 1995, pp. 251–260.

[11] J. Rasmussen, B. Brehmer, J. Leplat, Distributed Decision Making—Cognitive Models for Cooperative Work, Wiley, 1991.

[12] R. Sprague, E. Carlson, Building Effective Decision Support Systems, Prentice Hall, 1982.

[13] WWW-Consortium, CERN Httpd, Document http://www.w3.org/hypertext/WWW/Daemon/Status.html, 1995.

![](/api/attachments/8M8AZR65/fulltext/images/9255805931c04289dabcdfa92593ba94d02221c0b2872679b1dd8751bd429dc1.jpg)

Manfred Jeusfeld is a senior researcher at the Computer Science Department of Aachen University of Technology in Germany. He received his doctoral degree from the University of Passau. Before returning to Germany, he was a visiting assistant professor with the Hong Kong University of Science and Technology. His teaching focuses on cooperative information systems, systems analysis methods, and knowledge-based systems. His research interests include

quality information systems, meta-modeling, electronic trading, and terminology services. He is a member of IEEE, ACM, GI, and EMISA.

![](/api/attachments/8M8AZR65/fulltext/images/792db6af757175567fea2e6b0a14ebdd235437f2e1ccb6b4bd198ebab1c357bb.jpg)

Tung Bui is a professor of information technology at the U.S. Naval Postgraduate School, Monterey, CA. His research interest include implementation of information systems in large organizations, group decision and negotiation support systems, and design of distributed systems for organizational decision making. He is presently serving as the department editor of the journal Group Decision and Negotiation, an INFORMS journal dedicated to the study of group decision/negotiation support systems. He is also the consortium director of PRIISM, the Pacific Rim Institute for Research in Information Systems Management.
