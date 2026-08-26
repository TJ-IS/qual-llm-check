---
otero_id: 21373
otero_key: "CYZ369KH"
title: "Decision support on demand: Emerging electronic markets for decision technologies"
authors: "Hemant K. Bhargava; Ramayya Krishnan; Rudolf Müller"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00056-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support on demand: Emerging electronic markets for decision technologies

Hemant K. Bhargava ${}^{a,*}$ , Ramayya Krishnan ${}^{b}$ , Rudolf Müller ${}^{c}$

$^{a}$ Code SM-BH, Naval Postgraduate School, 555 Dyer Road, Room 214, Monterey, CA 93943, USA $^{b}$ The Heinz School, Carnegie Mellon University, Pittsburgh, PA 15213, USA $^{c}$ Institut für Wirtschaftsinformatik, Humboldt-Universität zu Berlin, 10178 Berlin, Germany

Received January 1996; revised June 1996; accepted July 1996

## Abstract

For the individual or organization wishing to employ a scientific approach in solving decision problems, there is a plethora of relevant concepts, methods, models, and software. Yet, relative to their potential or to peer software such as database technologies, decision technologies are little used in real-world decision making. We argue that at least some of the problems that restrict the use of decision technologies are rooted in the use of conventional market mechanisms to distribute them. We propose the development of electronic markets for decision technologies, and explain how features of modern information networks offer a solution to these problems. We present a framework for comparing alternative electronic markets for decision technologies, survey and analyze several such emerging markets, and present some details on our own research initiative – DecisionNet. A distinctive feature of DecisionNet is that it consists of software agents that perform – at the market level – functions (such as user accounting, billing and setting up the interface to a decision technology) that would otherwise need to be developed for each consumer, provider, or technology.

## 1. Introduction

Research in the decision sciences, including operations research and decision analysis, has resulted in the development of a variety of scientific problem-solving and model-based methods for many decision problems faced by individuals and organizations (for standard references, see $[8,9,17,20,22]$ ; for a survey of software for mathematical programming, see $[23]$ ). Further, research in model management (see $[18]$ for a survey, and $[14]$ for a bibliography) and modeling environments (see $[13]$ for a good statement of purpose) has resulted in the development of better modeling principles $[12]$ , formal executable modeling languages (e.g., GAMS $[6]$ and AMPL $[11]$ ) and computer-based systems (see $[15]$ for a survey) that facilitate the use of scientific methods in decision making.

A number of computer-based decision technologies $^{1}$ are now available both in the academic, research and commercial environments. In fact, purely in terms of the technical know-how required to develop decision technologies, there is an enormous breadth in the range of products, from highly specialized technologies – e.g., to support vehicle routing in a trucking firm – to general purpose modeling systems such as GAMS.

However, despite the availability of a broad range of scientific methods and computer-based modeling tools, usage of these decision technologies is far below potential. Why is this the case? The answer may lie in the reliance on traditional software distribution strategies (e.g., value-added retailers of shrink wrapped software) that are not particularly suited to the small and specialized nature of the decision technology marketplace. Given the digital nature of decision technologies, we propose that they be considered as information products or services. In this paper, we explore how electronic markets can facilitate exchanges between consumers and providers of decision technologies.

In Section 2, we begin with a simple example to motivate the problems encountered by both consumers and developers of decision technologies (Section 2.1) and also to indicate opportunities made possible by modern information networks for addressing these problems (Section 2.2). Then we define a framework (Section 3) for describing various electronic markets for decision technologies, and follow up with a survey of representative efforts at developing such markets (Section 4). Current research involves two kinds of markets: information markets, which use networks to inform a consumer about available decision technologies, and execution markets, which let the user execute decision technologies over a network. We also present, in Section 4.6, our solution – DecisionNet – which combines elements of the aforementioned markets. We conclude with a summary and analysis of our study (Section 5).

## 2. Motivating example and market mechanisms: Problems and opportunities

Consider a small freight-hauling concern, ACME Trucking, which has just received a contract with a manufacturer, Apex Beverages. The manufacturer maintains three factories, and wishes to distribute its products to three different retail outlets. All six Apex locations are in different cities, and ACME must decide how to move the correct quantities from one place to another while minimizing its costs. In short, Apex needs a distribution plan. In simplified form, Table 1 illustrates the problem that ACME faces. A solution to the problem might look something like shown in Table 2.

How might ACME develop a solution to its distribution planning problem? If it recognized that its problem could be formulated as an optimization model (e.g., the formulation given in Appendix A, stated in the GAMS modeling language), then it would seek out the various components required to implement such a decision technology-based solution. These include

1. computational platform (hardware and operating system),

2. modeling system (e.g., GAMS, AMPL),

3. model statement in the modeling language (GAMS or AMPL),

4. data pertinent to the problem.

## 2.1. Problems with current market mechanisms

Traditional mechanisms for distribution of decision support software (such as the GAMS modeling environment) and scientific expertise (such as the model schema) require each component of the solution package to be acquired, installed and executed on the users's computational platform. This raises a series of problems for both consumers and providers; we summarize and illustrate – using ACME – these problems below.

Table 1  
Inputs to the distribution problem

<table><tr><td>Factory</td><td>Production volume</td><td>Retail store</td><td>Sales volume</td></tr><tr><td>Akron</td><td>100 tons</td><td>Philadelphia</td><td>250 tons</td></tr><tr><td>Canton</td><td>200 tons</td><td>Newark</td><td>150 tons</td></tr><tr><td>Pittsburgh</td><td>150 tons</td><td>Batavia</td><td>50 tons</td></tr></table>

The problems discussed below are indeed characteristic of most software, particularly other specialized and scientific software which does not have a “mass market.” Much of the discussion and proposed solutions should also apply to software other than decision technologies, but it is not the purpose of this paper to examine the applicability of our ideas beyond the domain of decision technologies.

## 2.1.1. Problems encountered by consumers of decision technologies

Consumers such as ACME are faced with a series of obstacles; the ones that are relevant to the underlying market mechanisms are summarized below.

1. The “awareness” problem: Potential users are not always aware of relevant technologies.

In the example, ACME has to know that its distribution planning problem can be formulated as an optimization model. Further, it also needs to know that modeling languages and modeling environments are the preferred alternative to formulate and implement such models quickly.

2. The “accessibility” problem: Often, potential users do not have access to, or own a copy of, technologies that might benefit them.

To translate awareness into action, ACME has to obtain access to the decision technology components (i.e., model, modeling environment, data). Under the current system, ACME would need to identify the software publisher or vendor of each relevant technology. In contrast to mass marketed software, the search costs associated with identifying how to obtain access to specialized decision technologies are high.

3. The “compatibility” problem: Most technologies require specific hardware and software configurations, and many potential users may not possess a suitable platform.

Under the status quo, ACME's decision technology acquisitions must be compatible with its IT architecture. Thus, for example, a modeling environment only available on Windows NT/Intel platforms would be incompatible with a Macintosh based ACME IT architecture.

Further, platform configurations can have undesirable multiplier effects on compatibility. For instance, the model may be programmed using features available in a certain release of the modeling environment software which in turn may only be available for a certain release of the operating system.

4. The “applicability” problem: Due to the complexity – expertise, effort, and cost – of developing decision technologies, many of them exist only as broadly-applicable general solutions, needing further customization before they can be used to solve real-world problems.

Table 2  
The distribution plan

<table><tr><td></td><td>Philadelphia</td><td>Newark</td><td>Batavia</td></tr><tr><td>Akron</td><td>100</td><td>0</td><td>0</td></tr><tr><td>Canton</td><td>0</td><td>150</td><td>50</td></tr><tr><td>Pittsburgh</td><td>150</td><td>0</td><td>0</td></tr></table>

In our example, the GAMS modeling language and environment is the general solution, requiring expertise in the language, optimization models, and the application in order to implement and solve the transportation problem for ACME. Even if models are available for generic problem types, they often need to be customized before being applied. Given the small size of the market for these solutions, the cost of delivering a customized solution is high and discourages use of decision technology.

5. The “interoperability” problem: Many decision problems require a combination of multiple technologies to provide a satisfactory solution.

For example, the problem-specific data for the ACME problem may need to be extracted from a database server, cast in the format desired in the GAMS modeling language, and submitted to the GAMS modeling environment for execution. A subset of the results may need to be presented graphically (e.g., the percentage of the production of one Apex factory that is shipping product to retail stores, aggregated by region, presented as a pie chart). Since each of the technologies has its own input and output formats (SQL-90 for the database server, GAMS syntax for the GAMS environment, GIF images for the pie chart and so on), data interchange to enable interoperability is an important requirement. Under the status quo, interoperability either requires substantial human intervention or integration of a variety of tools on a single platform with the attendant compatibility problems described earlier.

## 2.1.2. Problems encountered by providers of decision technologies

Problems encountered by providers are symmetric to the problems encountered by consumers.

1. The “advertisement” problem: In general, as new decision technologies are developed, providers need proactive ways of informing potential consumers. While popular media targeted at software users serves this need well for mass marketed software such as Microsoft Word, the current system makes it difficult for specialized software (e.g., decision technologies) providers with small markets to reach consumers cost-effectively. This is the dual of the awareness and accessibility problem encountered by consumers.

2. The “heterogeneity” problem: Even within this small market, there is heterogeneity of computational platforms. For providers, this means having to support the technology on a variety of platforms. This is the dual to the compatibility problems encountered by consumers.

3. The “version management” problem: Often, a working version of a product is rendered useless due to a change in, say, operating system software, and providers must offer and maintain versions that are consistent with other combinations of hardware and software product versions. A good example is the recent shift from Windows 3.1 to Windows '95 which has resulted in the need to support multiple versions. Of course, even in the absence of shifts in the user platform, a variant of this problem is encountered as there is a need to upgrade and maintain the software over time. This is also dual to the compatibility problem encountered by consumers.

4. The “customization” problem: The cost of producing and customizing decision technology solutions using the traditional software distribution strategy is high due to the small and specialized nature of the market. This is exacerbated by the need to offer coordinated or integrated interoperable solutions. This problem is dual to the applicability and interoperability problems.

## 2.2. Opportunities for delivering decision technologies electronically

Under the current system, ACME would have to overcome all consumer problems before it could apply the decision technology based solution. This might prevent ACME, if it is only going to be an occasional user, from choosing to use this technology.

Is there an alternative to the current system? Must ACME own and install every component of the solution package? For example, could the modeling environment be accessed as a service over an information network such as the Internet? After all, ACME has the data for the problem, and another party on the network might own the optimization model which could solve the problem. If all three (ACME, the model provider, and the modeling environment service provider) could pool resources, ACME would have its solution.

Treating decision technologies as information products or services that can be accessed (e.g., executed or transported from one host to another) over an information network is the fundamental idea explored in this paper. In short, we propose the development of an electronic market (or markets) in which consumers and providers transact access to decision technologies. Several such markets are already emerging, but will they address the problems encountered by consumers and providers of decision technologies? The answer depends, naturally, on the specific functionality of the marketplace itself which, in turn, depends on the sets of features of the information network that is used to host the marketplace. All emergent markets for decision technologies that we are aware of are hosted on the Internet – in particular, on the World Wide Web [4]. Therefore, we continue our proposal by summarizing below the enabling features of the Web and the Internet and explain how they can address consumer and provider problems discussed above.

(1) Global hypermedia information system: Awareness; Accessibility; Applicability; Advertisement; Customization

The WWW offers an excellent opportunity to address, via creation of globally accessible “yellow pages,” the awareness and advertisement problems – it has enormous reach, is easy to use, and electronic search is both convenient and powerful. A yellow pages market would include a listing of, and information about, available decision technologies in particular categories. It would also have a classification scheme for technologies and features to locate, via indexed search and retrieval, suitable products or providers. The global reach of the Web also has implications for the potential number of providers and consumers that can participate; this is in contrast to markets hosted on private networks such as America Online or Compuserve. We believe this would have an indirect effect on the applicability and customization problems – by lowering advertising and distribution costs, the electronic market would encourage the development of specialized or niche products.

Further, due to its protocols for data transport between heterogeneous networks, the Internet can also address the accessibility problem; technologies on the yellow pages can be linked to the actual software that can be downloaded or distributed over the Internet. For various kinds of software – but not for decision technologies – the Internet has, for years, been used to provide low-cost access to large numbers of users.

## (2) Common Gateway Interface: Compatibility; Awareness; Heterogeneity; Version Management

The Common Gateway Interface (CGI) to executable programs can be used to allow users to use (i.e., remotely execute on the provider's machine) decision technologies (the executable programs) made available by providers. Remote computation can easily be launched by a user equipped with a Web browser by supplying, say via HTML forms, parameters that control the computation. For example, Goodyear Tires permit remote execution of a decision support system which helps users select a tire best suited to their needs. $^{2}$ Remote execution completely solves the compatibility problems since the user never needs to own or install a copy of the software. From a providers' point of view, it solves the heterogeneity and version management problems.

Another approach to the same set of problems uses Sun Microsystems' Java language which allows executable programs (applets) to be downloaded to users' (i.e., clients') machines and then be executed without requiring any compilation or installation. The remote execution feature is also required to support indexed search of yellow pages, which helps users locate and become aware of appropriate decision technologies.

## (3) Distributed nature: Applicability; Interoperability

The distributed nature of the Web means not only that several consumers can use products on remote machines, but also that multiple providers can enter the market supplying the same or different technologies.

Further, consumers may be able to interconnect multiple technologies – possibly from different providers – in ways that would not otherwise be possible.

For example, one might implement an application program that interoperates several technologies provided in the network [3]. This interoperation would include use of a data format conversion service if the technologies being integrated used different data formats. Assistance for this sort of technology interconnection may be offered as an infrastructural service in the marketplace. For instance, this is the approach taken in DecisionNet (see Section 4.6).

Support for interoperation in a decision technology market has implications for what it takes to participate as a provider in the market. Providers are not limited to supplying vertically integrated and complete solutions, but can offer access to small components. From a consumer perspective, one is not limited to just a single provider.

## 3. A comparison framework for electronic markets for decision technologies

The last section argued for exploiting internetworking technologies to solve consumer and provider problems in extending the usage of decision technologies. In the last few years, a few researchers and organizations have indeed begun this process, using the Internet and World Wide Web as the enabling technologies; our own research on DecisionNet falls in this category. In Section 4, we describe and compare these efforts. But, first – in Section 3.1 – we must deal with some matters of terminology. Then, in Section 3.2, we present a framework to characterize the similarities and differences between alternative electronic markets for decision technologies. As research in this area matures, we hope it will guide the development of electronic markets in a way that is consistent with criteria laid out by the developers. Although our framework is meant to compare network based usage of decision technologies, it might well apply to transactions of involving other IT products in information networks.

## 3.1. Definitions

With the increasing popularity of the Web as an instrument of commerce, terms like electronic commerce, electronic markets, and electronic shopping malls can be found in several publications. In order to compare proposed and emerging markets, it is important to have a precise understanding of the terms used to characterize the similarities and differences between markets. Some terms defined below have already been used in the previous sections, but now we require a precise definition in order to describe the framework.

Definition 1 (Decision technology). A decision technology consists of information and associated computational procedures (including data sets, model schemas, model instances, modeling environments, solvers, and decision support systems) that have the ability to support decision making and can be represented electronically.

Since our discussion is oriented on decision technologies, the term object in the rest of this paper refers to a decision technology.

Definition 2 (Consumer). A consumer of decision technologies is an individual or organization who could benefit from applying one or more types of decision technologies.

This definition is quite inclusive covering, for example, end users, researchers, model builders and algorithm developers.

Definition 3 (Provider). A provider of decision technologies is an individual or organization who creates decision technologies that address all, or parts of, a consumer's needs.

Definition 4 (Market). A decision technology market is a collection of consumers and providers of decision technologies, who conduct certain transactions involving the exchange or use of these technologies.

For the purpose of this paper, it is sufficient to focus on markets that involve consumers and providers only; in reality markets may involve various other players such as regulators, certification agencies, brokers and third-party solution providers.

Definition 5 (Electronic market). An electronic market is a market where the enabling medium for transactions between consumers, providers and services is an information network.

Definition 6 (Market infrastructure). A market infrastructure consists of computational platforms (e.g., a Web server where space may be leased) and procedures (e.g., user registration and accounting, billing, indexed search and retrieval) that are usually made available to all consumers and providers.

Each type of electronic market is characterized by the infrastructure it provides. Infrastructure functions can be thought of as being performed by agents (either software or human) on behalf of the consumers or providers interested in that functionality. In the absence of infrastructural service to support some function, that function must be performed either by providers or by consumers.

## 3.2. Dimensions in the framework

We have identified, based on our examination of alternative markets and our own efforts at developing one, four dimensions for describing electronic markets for decision technologies. Our focus in developing the framework is on the structures of these markets, rather than on implementation-specific aspects.

1. Market objective: Information; Access; Execution.

An electronic market for decision technologies can follow one or all of the following objectives.

\- It can aim to provide information such as found in the “yellow pages” of decision technologies;

\- it can support access as in providing references to anonymous FTP servers from which the technology could be downloaded;

\- it can offer executable access to decision technologies, e.g., via platform-independent applets or through the Common Gateway Interface on a WWW server.

2. Market infrastructure: Markets provide varying degrees of infrastructural services. These range from indexed search and retrieval of decision technologies to services such as billing. These infrastructural services provided to consumers and providers are itemized below.

(a) Consumer operations on the collection of objects: Browse; Keyword search; Indexed search and retrieval; Script technology interconnection.

Even a simple electronic market would allow users to browse through the collection. More advanced markets would allow search using keywords, retrieving information about a subset of the collection that is of interest. If the collection is organized as a taxonomy or an index, further operations – specific to the organizing scheme may be supported.

Similarly, the consumer may be able to script the execution of a series of operations on a collection of decision technologies (e.g., in the ACME example, format the problem specific data in GAMS format, use anonymous FTP to copy over the model, concatenate the data and the model and submit it using anonymous telnet to a GAMS modeling environment).

(b) Provider operations on objects: Register; Change; Withdraw; Support for getting connected.

A market that provides services, e.g., yellow pages, may dictate policies for allowing providers to manipulate objects in the collection that are administered by these services. If the market permits an open registration process, providers may be allowed to register objects, and to change and withdraw their previous entries. In cases where the organization that provides the services wants to control contents in the collection, add and delete operations are not made available to all providers. Control is exercised using access control mechanisms or by requiring providers to work market administrators.

Given the overhead associated with offering decision technologies in the electronic marketplace, an infrastructural service may facilitate this process. Support may, for example, consist of a specific toolbox to set up CGI access to a technology, a language by which the provider describes feasible sequences of interactions with a technology on a telnet port [21], or a parameterizable transaction model (i.e., a transaction model that is automatically created using parameters supplied by the technology provider) [5].

## 3. Technologies provided to consumers:

(a) Types of objects: Data sets; Model instances; Model schemas; Solvers; Modeling languages and systems; Modeling environments; Decision support systems; Computational platforms.
Providers in an electronic market can provide any of the listed types of decision technology objects.

(b) Consumer operations on objects: Query; Download; Use.

Providers and/or market services can allow specific operations on provided objects. By query it is meant that the consumer can obtain information about a specific technology. Download is the operation made possible by the file transfer protocol such that usage of the technology may require an installation on the user's machine. By use it is meant that the consumer can execute immediately the decision technology, either on their client platform or on a platform offered in the market.

## 4. Technology required to participate:

(a) As consumer: Usually a Web browser is the technology required by a consumer, causing only minor compatibility problems since browsers are available for almost all platforms. In other cases, specialized software may be required – for example, only Sun's HotJava, Netscape's Navigator 2.0, Microsoft's Explorer and Spry's Mosaic browsers for 32 bit operating systems have the capability to work with Java applets. Note, that the technology to interact with a service of the market may differ from what is necessary to interact with a provider's technology, for example if yellow pages list only an e-mail address of the provider.

(b) As provider: This depends on the type of decision technology being provided and the types of operations that are allowed on objects residing at the provider's platform. Technologies that are executable – such as modeling environments, solvers and visualization tools – require the use of WWW features such as HTTP / CGI, Java or anonymous telnet servers. On the other hand, data set providers or model schema providers need only FTP servers to make their technology accessible.

## 4. Emerging electronic markets for decision technologies

In this section, we list and briefly describe a selection of efforts in creating electronic markets. Our description follows the framework presented in Section 3, and we follow on with an analysis of each market in terms of the problems discussed in Section 2.1.

A few notes of caution are in order at this point. The examples described in this section are considered “markets” in a broad sense; even though they do not currently have mechanisms for user accounting, pricing and billing, they certainly could in the future. Since none of the markets yet have features of electronic commerce, we have entirely ignored this aspect throughout the paper. Further, most of the examples presented here involve decision technologies based on operations research (specifically, mathematical programming) paradigms; this is so partly because of the relevance of these methods to decision analysis, but also due to the authors' own bias and experiences in the area of decision support. Finally, this list is representative of the significant approaches in this area, rather than an exhaustive survey of emerging electronic markets for decision technologies.

## 4.1. OR-Library: A library of problem sets for optimization models

In the OR area, there are several efforts to share problem instances over the Internet and Web. An early implementation is described in [1] and is now available on the Web, allowing researchers to download datasets [2]; however, the library itself is not distributed – it is a collection at a single location.

The information about the data sets is restricted to the format, some information about the source, and, as far as it is known, the optimal solution value for the corresponding optimization problem.

## 4.1.1. Analysis

In terms of our framework, the OR-Library may be described as follows.

1. Market objective: To provide information about, and access to, data sets of typical OR problem classes for which researchers need to develop and test algorithms.

2. Market infrastructure: The infrastructure consists of HTTP and FTP servers at Imperial College Management School, London.

(a) Consumer operations on the collection of objects: The consumer can browse the collection of data sets. The provider of the data set is not involved in transactions with a consumer. Consumers can register their electronic mail address in order to be informed about changes.

(b) Provider operations on objects: A provider transfers data sets to administrators which are then manually integrated in the collection. There is no assistance to providers.

3. Technologies provided to consumers:

(a) Types of objects: Data sets.

(b) Consumer operations on objects: Query; Download; Use.

4. Technology required to participate:

(a) As consumer: Electronic Mail, FTP, Web browser.

(b) As provider: none.

Data libraries such as the OR-Library are important to researchers, both as consumers and as providers of data sets. The data sets provide a common testbed – a benchmark set of problems – on which algorithms can be compared and improved. Such libraries only address the awareness and advertising problems of this narrow segment of the consumers and providers.

A useful functionality in such libraries is a reference list, for each dataset, to research papers in which the data set was used for experimental studies. Such a system has been implemented for time series analysis (see $[16]$ ) using the Harvest software $[7]$ . The Harvest agents regularly visit FTP sites of research groups involved in time series analysis. Preprints at these sites are downloaded and heuristic programs try, using full-text search, to find out whether the data-set is cited.

## 4.2. Netlib: A library of optimization solvers

Netlib is a repository of mathematical software (e.g., approximation algorithms, optimization software) and other non-computational items. $^{3}$ Originally developed to distribute software via electronic mail [10], it is now

lib: lp (tar)
for: linear programming test problems
editor: David Gay
master: netlib.att.com

for: linear equations and linear least squares problems linear systems whose matrices are general, banded, symmetric indefinite, symmetric positive definite, triangular, and tridiagonal square. In addition, the package computes the QR and singular value decompositions of rectangular matrices and applies them to least squares problems.

![](/api/attachments/CYZ369KH/fulltext/images/a554d67bcfbd4cab315f5aaf30d837e99857c48e7a3785d6114c66e3cbd1c803.jpg)

ref: J. Bunch, J. Dongarra, C. Moler, and G.W. Stewart. LINPACK User's Guide. SIAM, Philadelphia, PA, 1979.

Fig. 1. Netlib objects: Two examples.

available on the World Wide Web. $^{4}$ Most of the objects in this library are “designed for use by professional numerical analysts” and are unlikely to directly be useful to other consumers of decision technologies. Nevertheless, Netlib contains components that are required in solving decision problems, and is a useful step towards an electronic market for decision technologies.

Netlib is organized as a collection of chapters, each of which has a collection of relevant objects (specifically, code “libraries”). Going down this hierarchy, users find information about mathematical software; this information is illustrated in Fig. 1 which displays details on two Netlib objects. Users can find suitable objects via keyword search and download them via the Internet to the user’s machine.

## 4.2.1. Analysis

In terms of our framework, Netlib is described as follows.

1. Market objective: To provide information about and access to mathematical programming algorithms.

2. Market infrastructure: The infrastructure consists of HTTP and FTP servers, mirrored at several organizations world-wide.

(a) Consumer operations on the collection of objects: Consumers can browse and do keyword and index search. Providers are not involved in consumer transactions.

(b) Provider operations on objects: A provider transfers data sets to administrators which are then manually integrated in the collection. There is no assistance to providers.

3. Technologies provided to consumers:

(a) Types of objects: Models; Solvers/algorithms.

(b) Consumer operations on objects: Query; Download.

G. Optimization (search also classes K, L8)
...
G2. Constrained
G2a. Linear programming
G2a1. Dense matrix of constraints
G2a2. Sparse matrix of constraints
G2b. Transportation and assignments problem
G2c. Integer programming
G2c1. Zero/one
G2c2. Covering and packing problems
G2c3. Knapsack problems

Fig. 2. Fragment of the GAMS classification tree.

4. Technology required to participate:

(a) As consumer: FTP, Web browser.

(b) As provider: none.

Netlib solves the awareness and the accessibility problems of consumers. Consumers can benefit from Netlib as long as they have an IT environment that meets the requirements of the downloaded objects (compatibility problem). Applicability and interoperability have to be solved by the consumers.

For the provider Netlib offers a medium for advertisement. Netlib does not support solutions for the other three provider problems. So the number of consumers that can benefit from the providers technology is still restricted by heterogeneity and version management problems.

## 4.3. Guide to available mathematical software (GAMS)

An excellent example of an electronic yellow pages service for decision technologies is the GAMS $^{5}$ (Guide to Available Mathematical Software) library maintained by the National Institute for Standards and Technology. GAMS catalogs several hundred models and algorithms, classified along a well-defined taxonomy which is organized as a tree (see Fig. 2 for a fragment of this tree). Users of this library are able to locate suitable products by navigating around this taxonomy until, eventually, they arrive at one of its leaf nodes (e.g., transportation and assignments problems). Once a user selects a particular leaf node, the GAMS system determines a list of products corresponding to that node (see Fig. 3 for an example). For each product in the list, the user can obtain certain meta-information, including the location of the software, the kind of platform it executes on and, possibly, how to access the software (see Fig. 4 for an example). In most cases, the ability to use the software is limited to authorized organizational users.

## 4.3.1. Analysis

In terms of our framework, GAMS is described as follows.

1. Market objective: To provide information (including how to access) about mathematical software.

2. Market infrastructure: The infrastructure consists of HTTP and FTP servers at the National Institute for Standards and Technology.

(a) Consumer operations on the collection of objects: The consumer can browse the entries and get by that references of provider. Keyword search and index search is supported.

(b) Provider operations on objects: As with Netlib, but GAMS editors of new sites support open registration.

## Modules for class G2b

Package NAG at GRANTA

H03ABE Solves the classical Transportation (Hitchcock) problem.
H03ABF Solves the classical Transportation (Hitchcock) problem.

Package TOMS at NETLIB

548 ASSCT: a Fortran subroutine for solving the square assignment problem. (See G. C ...
608 HGW: A Fortran subprogram to compute an approximate solution to the extended ...

Fig. 3. List of objects under a leaf node of the GAMS taxonomy. Underlined items are hyperlinks.

## Module H03ABE in NAG

\- Module Abstract (portion attached)

• Package Information

\- Components Example from GRANTA

H03ABE
Solves the classical Transportation (Hitchcock) problem.

Classes: G2b. Transportation and assignments problem

Type: Fortran subroutine in NAG library (H sublibrary).

Access: Proprietary. Many implementations available.

Precision: Single.

Usage: CALL H03ABE (KOST, MMM, MA, MB, M, K15, ... K8, K11, K12, Z, IFAIL)

Details: Example

Sites: (1) GRANTA

Fig. 4. A GAMS object. Underlined items are hyperlinks. Display has been formatted for this paper.

3. Technologies provided to consumers:

(a) Types of objects: Solvers/algorithms.

(b) Consumer operations on objects: The consumer can query meta-information about objects. Further operations as download or use depend on the technology provider and are not part of the market.

4. Technology required to participate:

(a) As consumer: Web browser.

(b) As provider: none.

The advantage of GAMS in comparison to Netlib is its improved index and that the objects itself are decentralized. Thus also commercial providers can use the GAMS index to advertise their technologies, improving the grade of awareness for the consumer. All other issues, for example accessibility, depend on the technology by which the provider is present in the network. Aside from a reference by a URL, the chosen technology is not a part of the GAMS market.

## 4.4. Optimization technology center (OTC)

The optimization technology center, $^{6}$ a joint enterprise of Argonne National Laboratory and Northwestern University, is a comprehensive collection of computational resources pertaining to mathematical programming

Optimization
Discrete
Integer Programming
Stochastic Programming
Continuous
Unconstrained
Nonlinear Equations
Nonlinear Least Squares
Global Optimization
Nondifferentiable Optimization
Constrained
Linear Programming
Semidefinite Programming
Nonlinearly Constrained
Bound Constrained
Quadratic Programming
Network Programming
Stochastic Programming

Fig. 5. Taxonomy of optimization problems in the NEOS guide.

(Fig. 5). The objective of the center is to inform users in industry, government and academia about the potential of mathematical programming techniques and to make sophistical mathematical programming software available for execution over the Internet. The center consists of the following resources:

1. The NEOS guide: An organized and searchable collection of information about mathematical programming;  
2. A library of advanced software for certain types of mathematical programming problems (see Fig. 6), with supporting material to inform potential users about required data formats and ways of accessing the solvers;

3. A computational platform – the NEOS (network enabled optimization system) server – that permits users to execute the software in the library. The NEOS server [19] provides the hardware platform as well as the middleware required to access and execute the solvers. The middleware is used to implement both e-mail and online HTML form-based access to the software. In addition, it is used to handle special types of “data” submitted by users such as Fortran routines to evaluate objective functions in unconstrained optimization.

## 4.4.1. Analysis

In terms of our framework, the OTC can be characterized as shown below.

1. Market objective: To provide information about, access to, and ability to execute on the server side, mathematical programming algorithms and model schemas.

2. Market infrastructure: The infrastructure consists of HTTP servers giving CGI access to services at OTC.
(a) Consumer operations on the collection of objects: The consumer can browse the collection. The provider of the technology is not involved in transactions with a consumer.

(b) Provider operations on objects: A provider allows the administrators to integrate their technology in the collection. The provider is not allowed to do any operations.

Linear Programming

Unconstrained Minimization

Stochastic Linear Programming

Bound Constrained Minimization

Linear Network Optimization

Fig. 6. Problems that can be solved using NEOS software.

3. Technologies provided to consumers:

(a) Types of objects: Model schemas; Data sets; Solvers/algorithms.

(b) Consumer operations on objects: Query; Use.

4. Technology required to participate:

(a) As consumer: Electronic Mail, Web browser.

(b) As provider: not applicable.

From the perspective of a consumer, the OTC addresses awareness, accessibility, and compatibility problems. The NEOS guide provides comprehensive information about mathematical programming and its applications. Accessibility is addressed at two levels – (a) vendors of relevant optimization software that is commercially available (and not available at the OTC) are hyperlinked to the NEOS guide, (b) direct computational access is provided to the solvers available at the OTC. The latter case – supporting remote execution at OTC – addresses the compatibility problem encountered by consumers. Apart from solvers, the OTC provides access to libraries, such as the Netlib library of linear programming test problems. These are made available both in the MPS format as well as in AMPL. However, these objects, which are stored in a compressed (zip) format can only be downloaded to a consumer site. They cannot be used directly in an interoperable manner with the solvers available at the NEOS site. Thus, a consumer cannot instruct the NEOS server to accept a test problem data set as input to the NEOS linear programming solver. In general, NEOS provides computational access to a single solver and does not address the interoperability problem.

From the perspective of a technology provider, the OTC does not provide any automated means to register or submit their decision technologies. This applies both to solvers, the predominant technology featured at the OTC, as well as applications (e.g., the diet problem) which feature integration of multiple technologies (e.g., linear programming and a graph-drawing program). All technologies on the NEOS server are made available through the direct intervention of the OTC which, presumably, makes them Web accessible and implements any of the required integration. For featured providers, of course, this OTC strategy solves many problems. The technology resides on the NEOS server and is integrated into NEOS by the OTC. The NEOS guide addresses advertising; execution on NEOS servers addresses both the version management and heterogeneity problems.

It is important to note two characteristics of the OTC market. First, the control exercised by the OTC over which technologies are featured in the market; this is in contrast to an “open” registration where any providers technology may be featured. Second, technology execution occurs on servers owned by the OTC; contrast this with a situation where execution takes place on a server owned and maintained by the technology provider. These, as we shall see, are important differences between the DecisionNet market and the OTC. The implications of these differences are discussed in Section 5.

## 4.5. Repositories of Java applets for decision support

The Java $^{7}$ language was originally designed as a secure, robust, object-oriented language to implement distributed applications. Since compiled Java programs can be executed on any platform as long as it has an installed Java environment, it has quickly become the standard language to provide downloadable software for client-side computing in the World Wide Web. This is made possible using a Web browser that integrates a Java interpreter required to execute the Java programs (called applets). The applets are downloaded either by resolving links in usual HTML documents, or during the execution of a Java applet. The latter is supported by Java built-in functions that can cope with FTP and HTTP servers.

Individual applications exist that employ the Java language in the decision support context. For example, Jones $^{8}$ offers an implementation of a traveling salesman algorithm as well as animation of a linear programming algorithm $^{9}$ in Java; Bradley $^{10}$ provides a graph coloring algorithm for a final exam scheduling problem. However, we are not aware of Java repositories of decision technologies, but our discussion is in the context of a hypothetical repository.

## 4.5.1. Analysis

In terms of our framework, Java is described as follows.

1. Market objective: To provide access to, and ability to execute algorithms (on the client side).

2. Market infrastructure: There is no market infrastructure besides Web browsers and servers.

(a) Consumer operations on the collection of objects: Web navigation.

(b) Provider operations on objects: not applicable.

3. Technologies provided to consumers:

(a) Types of objects: Model schemas; Solvers/algorithms.

(b) Consumer operations on objects: Download; Use.

4. Technology required:

(a) As consumer: Java-compatible browser.

(b) As provider: an environment for Java development.

In principle, Java repositories could replace software repositories like the Netlib, solving awareness and advertisement problems, and adding the advantage that access goes one-in-one with usage. This solves the compatibility problem for the user and the heterogeneity and version management problems of the provider. Furthermore applicability and interoperability can be achieved by implementing Java applets that combine Java applets from other providers. Currently this requires that all applets are downloaded from the same Internet site. This enforces a single provider of all components in one solution, or that the provider mirrors applets from other providers.

The big drawback of Java is that it enforces all technology to be implemented in the same language. Given the variety of high-level, specialized languages used to implement mathematics, it cannot be assumed that a significant amount of Java applets for decision support will be available in the next years. It is more likely that environments for mathematical modeling and implementations, like Mathematica, open a gate to the Internet, such that they can integrate on the fly native scripts for client-side computing. But, in this case, interoperability remains an issue.

## 4.6. DecisionNet

DecisionNet $^{11}$ aims to establish a marketplace which implements features of both information and execution markets. In contrast to other emerging markets, all types of decision technologies may be registered and made available to consumers in DecisionNet. Listings of registered technologies are organized into yellow pages which can be searched. The entries in the yellow pages are hyperlinks to the technologies and encode the appropriate access semantics (e.g., FTP for download, telnet for execution). These entries are created as part of a technology registration process which also automates much of the overhead of creating a Web-accessible technology. We list four key features of DecisionNet which differentiate it from other markets, and in particular OTC, the most well developed of them all.

![](/api/attachments/CYZ369KH/fulltext/images/8df091e8c384f9eba54a9cf3fb9886ba6c3c9dd5faec18975c3f44c46abf3d28.jpg)  
Fig. 7. Input dependency graph for PV model. The nodes are input data elements in the model. An edge, for example from X and Tflow to V, means that the name of the item (X) and the time of the cash flow (Tflow) must be determined before its value (V) can be defined.

\- DecisionNet features all types of decision technologies from data sets to modeling environments. Each of these technologies may be made available by a provider. This permits providers who develop models and data sets to participate in the market on an equal footing with providers who own high-end computational platforms and modeling environments.

\- In DecisionNet, a technology provider is given access to an intelligent registration agent [5] which leads the provider through a series of steps resulting in both a listing in the DecisionNet yellow pages and in the automated creation of a Web-based user interface to the technology. This agent-based assistance to providers considerably lowers the barrier to entry into DecisionNet. For example, Bhargava et al. [5] describe an example where a DecisionNet agent obtains from the provider of a financial present value (PV) model the input dependency graph (Fig. 7) for the model. Using this graph, and certain other generalized procedures, the agent is able to develop a technology execution graph (Fig. 9) that directs a consumer's interaction with the model – it would be useful for the reader to locate the structure of the input graph inside the technology graph. The nodes in this graph represent tasks that the agent needs to perform, and edges represent prerequisites for the tasks. For example, the ask tasks result in the creation of an input form such as shown in Fig. 8. Execution of this graph results in the interaction depicted in the vertical time sequence diagram depicted on the right half of Fig. 9.

\- Consumers in DecisionNet can use the services of an intelligent agent to cobble together a solution using available decision technologies. Thus, in the ACME example, data supplied by ACME is formatted in the GAMS syntax using a formatting service, combined with the transportation model supplied by an independent provider, and executed at the modeling environment owned by yet another provider. This support for interoperability has benefits potentially for both consumers and providers. Providers can participate in the market even if they only provide a piece of the solution (e.g., a model). Consumers can flexibly design their own solutions and are not limited to specific applications designed and made available in the market.

![](/api/attachments/CYZ369KH/fulltext/images/694c533a02e0cc140068a9ecfedfaf62191baaa63dd509db4e952ae4d2158317.jpg)  
Fig. 8. DecisionNet “Tell” form. This asks the user to enter values for variables X and T flow of the PV model.

![](/api/attachments/CYZ369KH/fulltext/images/670c9f7c78088ddda62dbd7522e24ef531c32d33636348c1f8f003a0f6e069d4.jpg)  
Fig. 9. PV technology graph (left) and communication diagram (right): In the graph, details are shown only for a few tasks; shaded ellipses represent elementary tasks, and empty ellipses represent composite tasks. In the vertical time sequence communication diagram (right), time is on the vertical axis, increasing as we go down.

DecisionNet does not require a provider to supply their technologies on a platform owned by DecisionNet (as is the case with the OTC). Providers may maintain their own servers and simply register with the agent the appropriate protocol to be used to invoke their technology (e.g., anonymous telnet or the POST method of the HTTP protocol). As needed, data or models are transported to appropriate computational servers, leveraging the distributed nature of the Web, and permitting scalability.

## 4.6.1. Analysis

In terms of the framework, DecisionNet may be characterized as follows.

1. Market objective: To provide information, access, and remote execution of decision technologies.

2. Market infrastructure: Services (agents) running at Naval Postgraduate School, Carnegie Mellon University, and Humboldt University support transactions between consumers and providers. Consumers contact services via HTTP/CGI.

(a) Consumer operations on objects: Browse; Indexed search and retrieval; Interoperable execution of technologies.

(b) Provider operations on objects: Register; Withdraw. Providers can also register partial solutions. These are upgraded by agents to full services for consumers.

## 3. Technologies provided to consumers:

(a) Types of objects: Data sets; Model instances; Model schemas; Solvers; Modeling languages and systems; Computational Platforms.

Future versions of DecisionNet are expected to support providers of modeling environments and decision support systems as well.

(b) Consumer operations on objects: Query; Use.

4. Technology required to participate:

(a) As consumer: Web browser.

(b) As provider: Web browser and FTP servers for data and model providers, telnet and other TCP/IP based services for algorithm/solver and modeling environment providers.

From the perspective of a consumer, DecisionNet addresses awareness, accessibility, compatibility and the interoperability problems. The yellow pages is a resource that can be used by consumers to become aware of the capabilities of available decision technologies. This awareness also benefits from the types of access supported in DecisionNet. For instance, trial runs or example runs of solvers and models are made available by a provider and can be accessed by following a hyperlink. In addition, access, both to download a technology or to execute a technology over the network are also supported. Support for remote execution of technology (e.g., a modeling environment) at a provider's server addresses the compatibility problem and the agent mediated support for cobbling together decision technologies permits interoperable execution. These features also address the applicability problem in that the low cost of setting up and disseminating a decision technology may make it feasible for providers to supply custom solutions to meet the needs of a small group of providers. Finally, since consumers can access all DecisionNet services using only a Web browser, the barrier to entry is very low.

From the perspective of a provider, DecisionNet addresses advertising, heterogeneity, and version management problems. While the yellow pages address the advertising problem, hosting decision technologies on the providers platform addresses the version management and heterogeneity problems. Further, all types of decision technologies are featured and even a provider of a single model schema can participate on an equal footing with larger providers supplying an integrated collection of decision technologies. While technology providers are generally required to maintain their own computational platforms and support appropriate Internet protocols (e.g., FTP by model and data set providers), the agent assisted DecisionNet registration process considerably lowers the barriers to entry into the DecisionNet market.

## 5. Summary and conclusions

We have presented a framework for describing electronic markets for decision technologies, and surveyed and compared six different efforts towards developing such markets. The OR data library provides information about and access to data sets for various classes of optimization problems; as such it is most useful for those involved in developing and testing algorithms. Netlib and GAMS are examples of information-oriented libraries of mathematical software; these systems also provide information on how to access the software and, in some cases, also allow the user to download the software via the Internet. The Java approach allows platform-independent applets to be downloaded to the user's machine; however, these applets can be executed without requiring further installation or configuration. NEOS and DecisionNet are examples of execution-oriented libraries of decision technologies; users interact and exchange data with the technology over the World Wide Web, but do not have to obtain a copy of the software since execution occurs on the provider's platform.

To what extent do these markets address the problems listed in Section 2.1? Clearly, all of them contribute to solving the awareness and advertising problems; the ones with well-designed taxonomies and search features particularly so (GAMS, DecisionNet – in progress). Similarly, accessibility is also addressed – Netlib and GAMS do not ensure access in all cases but the other approaches do. The OTC market, DecisionNet and Java-based repositories also address the compatibility, heterogeneity, and version management problems – OTC and DecisionNet do so by requiring consumers to send their data (to the model provider) and/or model (to the solver provider); Java involves the download of an executable program to the user's machine, but current implementations, for security reasons, limit the ability of users to execute these programs with their own data sets. We believe the availability of such electronic markets will also indirectly solve the applicability and customization problems, by lowering costs and by facilitating the development of niche products. Finally, DecisionNet aims to address the interoperability problem at the market level by offering general facilities for format translation and scripting the interconnection; other solutions aim to do so at the application level by providing integrated technologies.

In conclusion, we believe the intersection of modern information networking technologies and computer-based decision technologies creates exciting new opportunities for the increased use of scientific methods in decision making. Modern networking technologies allow us to think of decision technologies as usage-based services rather than as products. This conceptual shift, we believe, has the potential to revolutionize the real-world application of decision support systems. The concepts of decision support have been around for over 25 years – longer than the time it took for database systems to become a foundation of organizational information systems – but decision support systems have yet to gain a permanent and indispensable place in today's organizations. We hope that this paper will create further excitement in the decision support community and catalyze the creation of electronic markets for decision support.

## Acknowledgements

The authors acknowledge funding by the National Science Foundation (grant IRI-9312143), the U.S. Army Artificial Intelligence Center (grant MIPR6GNGS00087), U.S. Army Research Office (grant DAAH04-94-G-0239), the Institute for Joint Warfare Analysis at the Naval Postgraduate School, and the National Research Center SFB 373 of the Deutsche Forschungsgemeinschaft. We also acknowledge the effort of several of our students in implementing DecisionNet: Andrew King and Dan S. McQuay (Naval Postgraduate School) for the earliest prototype, Patrick Protacio, Patricia Rogers, and Steven Earley (Naval Postgraduate School) for the current implementation, and David Kaplan, Nancy Sawan, and Paul Varley (Carnegie Mellon University) for the GAMS registration and execution agent. We are also grateful to Gordon Bradley, Art Geoffrion, and Ted Lewis for useful comments during our research and on earlier drafts.

## Appendix A. An optimization model for ACME's distribution problem, stated in GAMS

\$TITLE A TRANSPORTATION PROBLEM (TRANSPORT, SEQ=1)

\$OFFUPPER

\* This problem finds a least cost shipping schedule that meets

\* requirements at markets and supplies at factories.

\* References: G.B. Dantzig, Linear Programming and Extensions

\* (Princeton University Press, Princeton, New Jersey, 1963) Chapter 3-3.

\* This formulation is described in GAMS: A Users 'Guide (Chapter 2 by R.E. Rosenthal).

\* (A. Brooke, D. Kendrick and A. Meeraus (Scientific Press, Redwood City, CA, 1988.)

SETS

I canning plants / SEATTLE, SAN-DIEGO /

J markets / NEW-YORK, CHICAGO, TOPEKA /;

## PARAMETERS

```txt
A(I) capacity of plant i in cases
/ SEATTLE 350
SAN-DIEGO600 /
```

```txt
B(J) demand at market j in cases
/ NEW-YORK 325
CHICAGO 300
TOPEKA 275 /;
```

TABLE D(I,J) distance in thousands of miles

```txt
NEW-YORKCHICAGOTOPEKA
SEATTLE 2.5 1.7 1.8
SAN-DIEGO 2.5 1.8 1.4;
```

```txt
SCALAR F freight in dollars per case per thousand miles /90/;  
PARAMETER C(I,J) transport cost in thousands of dollars per case;  
C(I,J)=F*D(I,J)/1000;
```

## VARIABLES

```txt
X(I,J) shipment quantities in cases
z total transportation costs in thousands of dollars;
```

POSITIVE VARIABLE X;

```sql
EQUATIONS
COST define objective function
SUPPLY(I) observe supply limit at plant i
DEMAND(J) satisfy demand at market j;
```

```matlab
COST.. Z = E = SUM((I, J), C(I, J) * X(I, J));
SUPPLY(I).. SUM(J, X(I, J)) = L = A(I);
DEMAND(J).. SUM(I, X(I, J)) = G = B(J);
MODEL TRANSPORT /ALL/;
option lp = sciconic;
SOLVE TRANSPORT USING LP MINIMIZING Z;
DISPLAY X.L, X.M;
```

## References

[1] J.E. Beasley, OR-Library: Distributing Test Problems by Electronic Mail, Journal of the Operational Research Society 41, No. 11 (1990) 1069–1072.

[2] J.E. Beasley, Imperial College – OR Data Library, http://mscmga.ms.ic.ac.uk/info.html (June 1994).

[3] P. Becker, An Embeddable and Extendable Language for Large-Scale Programming on the Internet, to appear in: Proceedings of the 16th International Conference on Distributed Computing Systems (ICDCS'96) (1996).

[4] Tim Berners-Lee, R. Cailliau, A. Luotonen, H.F. Nielsen and A. Secret, The World-Wide Web, Communications of the ACM 37, No. 8 (1994) 76–82.

[5] H.K. Bhargava, R. Krishnan and R. Müller, On Parameterized Transaction Models for Agents in Electronic Markets for Decision Technologies, in: Proceedings of the Fifth Workshop on Information Technologies and Systems, Amsterdam, Holland (December 1995) 218–227.

[6] Johannes Bisscop and Alexander Meeraus, On the Development of a General Algebraic Modeling System in a Strategic Planning Environment, Mathematical Programming Society (1982) 1–29.

[7] C. Mic Bowman, Peter B. Danzig, Darren R. Hardy, U. Manber and M.F. Schwartz, The Harvest Information Discovery and Access System, in: Proceedings of the Second International World Wide Web Conference, Chicago, Illinois (October 1994) 763–771.

[8] Stephen P. Bradley, Arnoldo C. Hax and Thomas L. Magnanti, Applied Mathematical Programming (Addison-Wesley Publishing Co., Menlo Park, 1977).

[9] Michael W. Davis, Applied Decision Support (Prentice-Hall, Inc., Englewood Cliffs, 1988).

[10] Jack J. Dongarra and Eric Grosse, Distribution of Mathematical Software via Electronic Mail, Communications of the ACM 30 (1987) 403–407.

[11] Robert Fourer, David M. Gay and Brian W. Kernighan, A Modeling Language for Mathematical Programming, Management Science 36, No. 5 (1990) 519–554.

[12] Arthur M. Geoffrion, An Introduction to Structured Modeling, Management Science 33, No. 5 (1987) 547–588.

[13] Arthur M. Geoffrion, Computer-Based Modeling Environments, European Journal of Operations Research 41, No. 1 (1988) 33–43.

[14] Harvey Greenberg, A Bibliography for the Development of an Intelligent Mathematical Programming System, ORSA CSTS Newsletter 5, No. 1 (1994) 21–38.

[15] Harvey J. Greenberg and Frederick H. Murphy, A Comparison of Mathematical Programming Modeling Systems, Annals of Operations Research 38 (1992) 177–238.

[16] Oliver Güther, Rudolf Müller and Andreas S. Weigend, The Design of MMM: A Model Management System for Time Series Analysis, in: James Ford, Fillia Makedon and Samuel A. Rebelsky, Eds., Electronic Publishing and the Information Superhighway (DAGS95), Boston, Basel, Berlin (1995) 223–233. Birkhäuser, On-line conference proceedings: Addison-Wesley Interactive http://www.aw.com/awi.html.

[17] Daniel P. Heyman and Matthew J. Sobel, Stochastic Models in Operations Research, Vol. 1 (McGraw-Hill, New York, 1982).

[18] R. Krishnan, Model Management: Survey, Future Research Directions and a Bibliography, ORSA CSTS Newsletter 14, No. 1 (1993).

[19] Michael P. Messnier, The Network-Enabled Optimization System Server, Technical Report ANL/MCS-TM-210, Argonne National Laboratory, Mathematical and Computer Sciences Division (August 1995).

[20] Stuart S. Nagel, Computer-Aided Decision Analysis: Theory and Applications (Quorum Books, Westport, 1993).

[21] L. Perrochon and R. Fisher, IDLE: Unified W3-Access to Interactive Information Servers, Computer Networks and ISDN Systems 27 (1995) 927–938.

[22] Thomas L. Saaty and Joyce M. Alexander, Thinking with Models: Mathematical Models in the Physical, Biological and Social Sciences, 1st Edition (Pergamon Press, Oxford, 1981).

[23] Ramesh Sharda, Linear Programming Solver Software for Personal Computers: 1995 Report, OR/MS Today 22, No. 5 (1995) 49–57.

![](/api/attachments/CYZ369KH/fulltext/images/7843694b84e1a18d47b7d9611e8928d8f02a7701d0c84796b54b0a8f41241eef.jpg)  
Hemant K. Bhargava is Associate Professor of Information Technology at the Naval Postgraduate School. He received his Ph.D. and M.S. in Decision Sciences from the University of Pennsylvania, and an MBA from the Indian Institute of Management. His research focus is in the decision sciences, and involves computer-aided mathematical modeling, logic modeling, and artificial intelligence. His current work develops methods for using the Internet for global sharing of computer-based decision technologies. Dr. Bhargava's research has been applied in organizations, such as the U.S. Coast Guard, Army and Navy, and to such problems as fleet mix planning, the "Persian Gulf War syndrome", force sourcing, flight scheduling, radar coverage optimization, and watchbill scheduling.

![](/api/attachments/CYZ369KH/fulltext/images/c7d6c148c5ff0c9cc55830e0fbaecccdf0b7cbc88b2b60bd07cc4b04e726b484.jpg)

Ramayya Krishnan is Associate Professor of Information Systems at the H. John Heinz School of Public Policy and Management at Carnegie Mellon University. He has a Ph.D. in Management Science and Information Systems, a M.S. in Industrial Engineering from the University of Texas at Austin and a B.Tech. in Mechanical Engineering from the Indian Institute of Technology, Madras. His current research interests are in electronic commerce, the interface between information networking and decision support systems and in data privacy and confidentially issues. His research on these topics has been funded by the NSF, the US Army and DARPA. He is an associate editor for Decision Support Systems and INFORMS Journal on Computing.

![](/api/attachments/CYZ369KH/fulltext/images/38e170318af3bf48ee5d03f2bd6d8ba72666f8f40f84b45a7b5bca468406e36a.jpg)

Rudolf Müller is a Research Professor of Information Systems at the Humboldt-University at Berlin. He is there a member of the National Research Center SFB 373 “Quantification and Simulation of Economic Processes”. He has a diploma in Pure Mathematics from the University of Bonn ad a Ph.D. in Applied Mathematics from the Technical University of Berlin. His research interests are in combinatorial optimization, information networks and software engineering. His current work focuses on the design of computational services in the Internet, investigating applications for combinatorial optimization, decision support and statistical data analysis. Dr. Müller’s research is funded by the Deutsche Forschungsgemeinschaft.
