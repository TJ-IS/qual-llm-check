---
otero_id: 26321
otero_key: "6WPWFBWF"
title: "Designing Workflow Coordination: Centralized Versus Market-Based Mechanisms"
authors: "Jui Chiew (J. C.) Tan; Patrick T. Harker"
year: "1999"
journal: "Information Systems Research"
doi: "10.1287/isre.10.4.328"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/6WPWFBWF/fulltext/images/e63c05d631b5e4713eeb4d565e366de33dab0aadf5bf6824365395618e62ae92.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Designing Workflow Coordination: Centralized Versus Market-Based Mechanisms

Jui Chiew (J. C.) Tan, Patrick T. Harker,

## To cite this article:

Jui Chiew (J. C.) Tan, Patrick T. Harker, (1999) Designing Workflow Coordination: Centralized Versus Market-Based Mechanisms. Information Systems Research 10(4):328-342. http://dx.doi.org/10.1287/isre.10.4.328

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1999 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/6WPWFBWF/fulltext/images/42d3a231732bb9ddb8a4ff7607c9b9949f2ab3f625e72f6c391d357d158e5855.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Designing Workflow Coordination: Centralized Versus Market-Based Mechanisms

Jui Chiew (J. C.) Tan • Patrick T. Harker

Department of Systems Engineering, University of Pennsylvania, Philadelphia, Pennsylvania 19104-6315 juichiew@seas.upenn.edu

Department of Operations and Information Management, University of Pennsylvania, Philadelphia, Pennsylvania 19104-6366 harker@wharton.upenn.edu

s a result of the increasing diffusion of decision-making within and between organizations, distributed scheduling methods have been proposed as alternatives to centralized, hierarchical, top-down production control schemes. While distributed scheduling methodologies are appealing, one must first address the fundamental questions of when and where such methods are appropriate. This paper seeks to provide answers to these questions. Using a generalized workflow framework, this paper models and compares the total expected costs of using decentralized and centralized organizational designs to coordinate the flows of information and work. This comparison allows one to define the characteristics of work environments where distributed scheduling methods are more suitable than hierarchical, top-down production approaches. Finally, from this analysis, one can conclude that distributed scheduling methods work well for systems where information technology is inexpensive relative to production cost, processing times are relatively long, and where the number of agents in the system is not too large.

(Distributed Work; Organizational Design; Organizational Structures; Workflow Coordination; Distributed Scheduling; Intelligent Agent; Market Mechanisms Auction; Bidding)

## 1. Introduction

Information technologies continue to enable the decentralization of business and production processes. For example, Bankers Trust uses groupware (a client/ server application such as Lotus Notes) to coordinate business processes in the asset management department, enabling physically distributed account administrators, record keepers, and their supervisors to work together (Kirkpatrick 1993). At Tandy Electronics Design, workflow software facilitates research and development teams in Texas and Tokyo, separated by a 14-hour time difference, to concurrently collaborate in their design efforts (Radding 1994). COMPAQ employs a build-to-order automatic replenishment system, instead of making computers based on speculated demand, to electronically link some of its 31,000 distributors, wholesalers, and retailers in its global supply chain (Henkoff 1994). These distributed organizations are characterized by their spatial and temporal separation and divergence in the goals of business units involved in the production and business processes. As such, organizations are forced to deal with operational issues as well as issues arising from distributed work environments.

In contrast, scheduling methodologies in Operations

Management (OM) tend to have centralized, topdown, sequential/hierarchical designs, and rely on various optimization approaches. They require workers in production systems to be obedient and simply follow global and local rules (Upton et al 1991); mathematical programming algorithms and heuristics are the main tools used to derive these rules. While these tools have sound theoretical underpinnings, they are cumbersome to use because of the extraordinary computational power and informational accuracy needed in the models they employ. Given these limitations, are such scheduling methodologies adequate to deal with issues arising from distributed work environments? How can supervisors in these centralized planning environments effectively enforce rules and encourage obedience in distributed work environments? Can the information accuracy required in optimization models be ensured in decentralized organizations?

Distributed scheduling methods (DSMs) have been proposed as a new class of methodologies to deal with issues arising from distributed work environments. These methods have been employed in diverse areas such as computer integrated cellular manufacturing (Shaw 1987), supply chain management (Hinkkanen et al 1997), temperature control (Clearwater and Huberman 1994), vehicle routing (Sandholm 1993), and manufacturing production planning (Baker 1996). These methodologies specifically tackle structural concerns in organizations, such as:

(1) the decentralized nature of the work environment (i.e., it involves solving many small problems, one problem for each worker or business unit who considers only local conditions in making decisions);

(2) opportunistic workers who are actively involved in seeking work through the auction mechanism, thus making a DSM a “pull” system for scheduling; and

(3) work environments where the conditions associated with business and production processes change frequently.

Our interest in centralized planning and DSM as two distinct classes of methodologies comes from recognizing that current research emphasizes methodological development and ignores the questions of when and where such methods are most applicable. In this paper, we compare these two classes of methodologies to define when and where to implement either a centralized planning method or a DSM. Though our model is similar to Malone and Smith (1988) and Deskmukh et al (1993), we differ in our definition of the cost components used in the comparisons. Specifically, our cost comparison includes monitoring costs (i.e., the costs associated with assessing the availability of workers/ machines to perform tasks) not considered by previous authors. In recognition of increasingly distributed work systems, we also want to know how changes in system characteristics will impact and sustain the implementations of these two classes of methodologies. This comparative statics analysis allows one to derive conditions describing the system parameter ranges where a distributed scheduling method is preferred to a centralized approach.

The use of a DSM raises issues related to the coordination of information flow because of the decentralized nature of this methodology. Similarly, the topdown delegation of work in centralized planning also has information flow concerns. We define this coordination issue as a workflow coordination problem. In general, workflow coordination refers to the performance of methodologies and their mechanisms to find the best candidate(s) to perform tasks through direct or indirect information gathering, and the subsequent delivery of work to workers. Thus, workflow coordination manages information flow along the production and/or service supply chain (Rathnam et al 1995), implying that it is also a logistics coordination problem. In fact, workflow coordination parallels supply chain management, but they differ only in what they manage, information or materials. Henkoff (1994, p. 64) states that there is greater opportunity for cost saving in managing supply chain coordination than in improving production processes. Premised within the context of organizational design and work environments, efficiencies of the supply chain’s controller and workers are the primary concerns in workflow coordination.

The goal of this paper is to present an analysis of the characteristics of a system that would favor a DSM over a more traditional top-down approach. From the outset, it should be noted that this analysis does not capture all of the details involved in implementing a DSM such as the specific design of an agent in the DSM, the details of the auction system employed, etc.

These issues are clearly important in the design of a DSM; however, we have chosen to simplify these issues in order to maintain analytical tractability of our model. Furthermore, the question of uncertainty in coordination systems is quite important: How does a system respond to disruptions? For this paper, we have chosen to present a deterministic model; the analysis of uncertainty is left for future research. Thus, this paper can be viewed as an initial attempt to discover the key characteristics of coordination problems that will favor a DSM over traditional methods.

The rest of this paper is organized as follows. Section 2 presents the foundations and issues arising from the implementations of distributed scheduling methods within the context of distributed work environments. In § 3, we present a framework for workflow coordination in different organizational structures. We will then quantify and compare implementations of a DSM in decentralized organizations and top-down, hierarchical planning in centralized organizations in § 4; conclusions are drawn in § 5.

## 2. Literature Review

There is a wealth of literature on centralized, hierarchical, and top-down production control schemes. We will omit the review of this literature; interested readers are referred to Graves (1981) and Lawler et al (1993) for comprehensive discussions of this approach. In this section, the literature related to the implementation of distributed scheduling methods is emphasized. A DSM is usually implemented as intelligent, softwarebased applications where messaging protocols enable automated negotiations and auctions. Since such negotiations generate bids as sets of information, the management and coordination of information flows are critical to the implementation of a DSM. As such, our discussion on workflow coordination will center on messaging protocols for managing the flow of information, mechanisms for handling divergent interests of business units, and implementations of DSMs.

Davis and Smith (1983) provide one of the first protocols for automated negotiation, the Contract Net Protocol (CNP). Since CNP, several negotiation protocol designs have been proposed in the literature.

Sandholm (1993) provides a protocol for vehicle routing problems (TRACONET) based on bounded rational self-interested agents. Stonebraker et al (1995a, 1995b) present another protocol (Mariposa) based on a bidding mechanism. In contrast to TRACONET, Mariposa is a budget constrained database search execution system. Zlotkin and Rosenschein (1990) present yet another alternative for general negotiation domains, the Unified Negotiation Protocol (UNP), where agents have goals and strategic plans.

The use of economic paradigms is not restricted to auctions and negotiations. Varian (1995) advocates the use of economic mechanisms in automated negotiations and intelligent software-based applications. In fact, TRACONET’s bounded rational self-interested agents, Mariposa’s budget constraint, and UNP’s goaloriented strategic agents show that price theory and game theory provide good starting points for designing negotiations. While price theory provides discrete actions or bids for auctions, game theory provides strategic plans (i.e., a sequence of actions) for agents to use in negotiations. On using price theory, Mackie-Mason and Varian (1994) suggest an affine pricing scheme (connect fee plus usage price) to manage congested network resources to maximize social benefits. Varian (1994) prices externalities to encourage desired behaviors from agents. On making strategic choices, the budget constraints used in Mariposa (Stonebraker et al. 1995c) can be viewed as query search plans. Gametheoretic mixed strategies are used for negotiations in UNP (Rosenschein and Zlotkin 1994), where autonomous agents make strategic choices in developing their goals and plans.

However, the application of these economic paradigms gives rise to computational problems when a DSM is used to allocate resources. The first computational issue that arises is the generation of bids or sets of information. As negotiations are carried out between two agents (Zlotkin and Rosenschein 1990), possible solutions could grow exponentially if there are numerous agents in the system. More critically, Upton et al. (1991) report the occurrence of bid traffic explosion when the work arrival rate is close to its processing rate. Usage charges (Sandholm and Lesser 1995), connect fees (MacKie-Mason and Varian 1994), and tol policies (Nagurney 1993) have been suggested to resolve the congestion problem arising from managing the number of bids and information. The second issue related to computational complexity deals with the calculation of economic measures such as marginal costs (Sandholm 1993) and equilibria (Huberman and Hogg 1995). In TRACONET, the calculation of bid prices using marginal costs is discretized, resulting in either potentially suboptimal contracts or slow estimation processes (Sandholm 1993). Huberman and Hogg (1995) observe that imperfect knowledge (a result of selfinterested agents) and information delays (a result of bounded rationality) can lead to oscillatory and chaotic solutions.

Distributed scheduling methods (DSMs) have been proposed as alternatives to classical cost reduction methods in centralized control schemes. Bertsekas (1992) states that his auction algorithm (an example of a simple DSM) is at least as competitive and often far superior to cost reduction methods that form the basis of primal simplex and dual descent methods from linear programming. Despite Bertsekas’ assertion, industrial implementations of DSMs using auction-based mechanisms are scarce. In the production literature, Upton et al. (1991) provide a general discussion on DSM methodologies and computer architectures for flexible manufacturing systems. Their initial empirical insights include bid traffic explosion when processing and arrival rates are close. However, Shaw (1987) finds encouraging results in terms of system performance measures such as tardiness and mean system waiting time when using a DSM. Lin and Solberg (1992) show that a distributed scheduling method using a marketlike model enables adaptive and real-time shop floor control. Baker and Merchant (1993) implemented a DSM to simulate an agile manufacturing system using data from a General Electric plant. In the area of business processes arising in white-collar work, Graves et al. (1993) show that DSMs are a very powerful tool for resolving a large number of scheduling conflicts. Malone et al. (1988) show that incremental benefits in task pooling among resources are realized in an environment with a relative small number of resources, and adding more resources has very little incremental benefits.

DSMs using auction-based mechanisms are robust in resolving conflicts (Graves et al. 1993), are efficient in allocating scarce resources such as heat (Clearwater and Huberman 1994) and ATM network bandwidth (Miller et al. 1996), and have an adaptive design (Lin and Solberg, 1992). However, such research only deals with the development of new methodologies, and ignores the questions of when and where a DSM can be implemented. This paper will directly answer these neglected questions by comparing the implementation of a DSM in a decentralized organization to top-down hierarchical planning in a centralized organization. Specifically, we will incorporate the costs of workflow coordination (i.e., the management of information and work flows) and actual production costs.

Deshmukh et al. (1993) and Malone and Smith (1988) have also looked into workflow coordination in centralized and decentralized organizational structures. However, they miss several central issues in organizational design. First, a centralized system is a hierarchical, top-down design using a push mechanism (e.g., an MRP-like system). Thus, only one central queue is necessary to model production activities because there is only one central controller. On the other hand, a decentralized system has a distributed decision making process. Thus, the appropriate model in the case of a DSM involves decoupled, independent queues for different business units. Our model will reflect this distinction to represent the dependence or independence of business units from a central controller. Second, real production systems involve failures (machine breakdowns, workers not completing tasks, etc.). Deshmukh et al. (1993) ignore workers’ failures, and Malone and Smith (1988) model work failures without salvage values. We will formulate failures as correcting such unexpected events (i.e., rework), thereby allowing our model to provide a more realistic representation of production and business processes. Third, Deshmukh et al. (1993) only consider expected system waiting times; coordination issues are ignored. Though our model and analysis are similar to that of Malone and Smith (1988), the method of comparison is different. Malone and Smith (1988) estimate different costs of production and compare each separately. In contrast, we compare the total expected cost. Fourth, Malone and Smith’s (1988) and the models used by Deskmukh et al. do not address several issues arising from distributed work environments. For example, Malone and Smith (1988) assume that the controller knows with certainty when workers are available to perform tasks. This is a poor assumption in many situations, especially those arising in white-collar work systems.

## 3. Work and Information Flows in Organizational Structures

In this section, we are interested in the use of scheduling mechanisms to coordinate work and information flows in centralized and decentralized organizations. In particular, we emphasize techniques of indirect information gathering in a centralized organizational design and direct information gathering in a decentralized organizational design. Figure 1 illustrates the flow of tasks associated with a job in these organizational structures.

The distinguishing structural characteristic between a centralized and a decentralized organizational structure is the make up of the work system. A centralized organizational structure is made up of a product manager, several functional managers, and several sets of workers. However, a decentralized organizational structure does not have a middle hierarchy (i.e., functional managers). Section 3.1 will illustrate how workflow coordination is derived in Figure 1 using the example of processing small business loans (SBLs).

Figure 1 Organizational Structures for Workflow Coordination  
![](/api/attachments/6WPWFBWF/fulltext/images/0ca6ad0ab1baa238a73bc7a0ae9048151cb57252128831f6ebb15785de483ece.jpg)

## 3.1. Example: Small Business Loan Processing

To illustrate the design of a DSM, consider the case of small business lending (SBL). In the SBL example, there are four processes: application (the gathering of relevant information from the applicant), underwriting (the process of determining the applicant’s risk level and, subsequently, the lending interest rate), regulatory filing (registering the loan application with the government), and satisfaction (the final check of ensuring adequate service delivery). In this work system, distributed branch managers are the product managers of SBL who are responsible for the whole process. Centrally located area supervisors of underwriting and records filing are functional managers who decide who will perform tasks and when they will be completed; i.e., they perform the detailed scheduling functions for these tasks. Underwriters and filing clerks are the actual processors of tasks.

3.1.1. SBL Using a Centralized Organizational Design. A centralized organizational design is a push system where the product manager acts as coordinator of the whole process, and the functional managers act as central controllers of task scheduling. Thus, it is hierarchical, top-down, and anticipatory by design. Consider a centralized production planning system in the context of processing small business loans. Since the underwriting and regulatory filing processes are internal to the SBL process, the centralized organizational design in Figure 1 is used twice to construct the complete workflow depicted in Figure 2. In this figure, arrows represent the information flow, bold arrows represent the final schedule, - represents a product manager, ● represents a functional manager, and  represents a working agent. Members of the work system include of one customer, one product manager, two functional managers, one pool of underwriters, and one pool of filing clerks.

When a completed SBL application arrives, the branch manager triggers the start of the business process. The branch manager delegates the application to the underwriting area supervisor using one message.

Figure 2 Centralized Organizational Design for the Small Business Loan Example  
![](/api/attachments/6WPWFBWF/fulltext/images/a8f66dd0ef87af390e150707ccadb6a5850eb002e781bbce0388cb0744e2cecf.jpg)

The supervisor will sample a group of underwriters to derive their availability information through a set of indirect messages. Using a message, the supervisor assigns credit analysis and risk assessment work to an underwriter. After the underwriting process is completed, the selected underwriter returns the application to the supervisor using yet another message. The supervisor then informs the branch manager of completed work using a message. The branch manager decides if the loan application is approved or rejected based on the credit analysis work, and informs the applicant/customer. The branch manager then pushes the process along to regulatory filing where messaging and sampling are repeated. Once the loan is filed, the branch manager closes the whole process.

In summary, the product manager triggers/pushes work and information flows for the underwriting and regulatory filing processes using a centralized mechanism. The functional managers use sampling to derive workers’ availability information to determine the final schedule sequence. The functional managers also act as intermediaries between the workers and the branch manager. However, workers in both underwriting and regulatory filing areas are shielded from determining what kind of work they prefer; they are asked to follow a schedule and perform work as assigned to them. For underwriting and regulatory tasks, the centralized mechanism uses four messages and sampling to completely schedule a task. In Figure 2, bold arrows represent information and work flows for the entire process. Directed arrows from the functional mangers to her workers in Figure 2 depict the sampling.

3.1.2. SBL Using a Decentralized Organizational Design. A DSM using an auction-based mechanism has a decentralized organizational design because agents (i.e., workers) use only local conditions to bid for future work. Because of the auction mechanism, this decentralized organizational design is a pull system. Thus, DSM’s using auction-based mechanisms are reactionary by design; i.e., product managers and decentralized workers simultaneously react to incoming demands. A make-to-order replenishment system is a good example.

Consider a DSM using an auction-based mechanism in the context of processing small business loans described above. In Figure 3, there is again one customer, one product manager, one pool of underwriters, and one pool of filing clerks in the work system. Again, arrows represent the information flow, bold arrows represent the final schedule, - represents a product manager, and  represents a working agent.

The loan applicant initiates the dynamics of processing a SBL. When a completed SBL application is received, the branch manager will request bids for underwriting work directly from a pool of qualified underwriters (or their intelligent software agents). In turn, these underwriters will respond with bids, implicitly revealing their availability information to the branch manager. Then, the branch manager will use an auction to determine the most suitable underwriter to perform the task. The branch manager will route work to the winner of the auction using a message. This underwriter will inform the branch manager upon work completion using another message. At this point, the branch manager informs the customer if the loan application is approved or not. The process proceeds to regulatory filing as required by law. Again, the branch manager requests bids from a pool of qualified clerks or their intelligent agents to perform this mandatory work to close the loan application process.

Figure 3 Decentralized Organizational Design for the Small Business Loan Example  
![](/api/attachments/6WPWFBWF/fulltext/images/1336eb5831175ab60024d7786091c816e06d645a62cca362fea0222a92586b3b.jpg)

In summary, the customer first triggers workflow dynamics in a decentralized organization. Then, the product manager creates two “markets” to find the most suitable agents: one for underwriting and another for regulatory filing work. Thus, for a DSM using an auction-based mechanism to work effectively, the product manager must rely on opportunistic behaviors from agents. At the same time, it must be able to manage bid traffic; i.e., information flow. In fact, agents opportunistic behaviors enable dynamic scheduling because the agents’ bids for future work are based on changing local conditions. In each of the two markets, there is a set of information in the form of request for bids, and another set in the form of bids. In Figure 3, two-way arrows represent requests for bids and bids in the auction. In addition, there are two messages passed for the actual scheduling of work. In Figure 3, the bold arrows are the actual flows of work and information.

## 4. Comparing Workflow Structures

In this section, we will quantify the organizational structures described above and compare their total expected costs. One sees that top-down, hierarchical production planning has a centralized organizational design because the decision making processes are in the hands of a central coordinator (product manager) and controllers (functional managers). In contrast, a DSM using an auction-based mechanism has a decentralized organizational design because workers use their local conditions to make individual decisions.

Since a job has the same set of tasks for both organizational structures, the unit of comparison can be based on either a task or an entire job. For simplicity, we will choose tasks as our unit of analysis. Our framework in § 3 includes work and information flows. This is in accordance with Henkoff’s (1994) view that proper management of logistics can be significant with respect to cost saving. This inclusion also allows us to define the total expected costs of using these organizational designs. In contrast, Deskmukh et al. (1993) compare organizational structures based solely on average system waiting time. Malone and Smith (1988) compare organizational structures by comparing cost on a component-by-component basis; i.e., they ignore the trade offs of these components. In the case of presenting decentralized organizational designs as alternatives to centralized ones, a system-wide or total cost comparison is clearly desired.

The total expected cost is the sum of actual production costs, coordination costs, and disruption costs. Production cost is a measure of the efficiency of the queue design in each organizational structure. Thus, the average system waiting time is the primary driver of this cost component. Coordination cost is a measure of the efficiency of the mechanism to find a worker to perform a task through the use of information technology as a messaging tool. Thus, the total number of messages needed to find that an available and appropriate worker is the only factor of interest. Disruption cost is a measure of workers’ failure probability. The choice of rework in this model given by the cost incurred as a result of failures is deliberate. This modeling choice parallels industrial practice in that production and business processes have salvage values. The notion of rework is particularly important in service organizations since the delivery of service to a customer cannot be scrapped if a failure has occurred; i. $\mathbf { \epsilon } _ { \mathrm { e } } . ,$ the customer’s request must be fulfilled. In contrast, a product may be scrapped in a manufacturing environment (although this practice is diminishing with the advent of quality management principles).

## 4.1. Mathematical Model

Using the modeling concepts and notation from Deskmukh et al. (1993) and Malone and Smith (1988), let us begin quantifying organizational structures by formalizing the setting to provide fair treatments to both structures. We assume the following.

Assumption (A1). All costs not included in this analysis are equal in both the decentralized and centralized organizational structures.

Assumption (A2). Tasks are processed on a first-come, first-serve basis.

Assumption (A3). Tasks have exponential interarrival and service rates, where the service rate is assumed to be greater than the interarrival rate.<sup>1</sup>

Assumption (A4). Production cost can be estimated using the average wage rate and the average system waiting time.

Assumption (A5). Coordination costs can be estimated using the number of messages required for each task and the unit messaging costs.

Assumption (A6). There exists a large pool of workers.

Assumption (A7). The probability that a functional manager and a worker fail at the same time is negligible.

Assumption (A8). There are at least two workers contacted when a DSM with an auction-based mechanism is deployed.

<sup>1</sup>This assumption is made for modeling simplicity. If general distribution functions were used, we would get similar results.

Assumption (A9). A functional manager’s failure probability is small.

Assumption (A1) enables one to model the differences between these organizational designs. For example, the impacts of the product managers’ behaviors may be included in the model. However, one realizes that the inclusion will not change the result derived herein. Similar to Malone and Smith’s (1988) model, production cost can be estimated using Assumptions (A2)–(A4). Assumption (A5) is used to estimate the cost of employing coordinating mechanisms. Assumptions (A6)–(A9) are simplifications for the analysis presented in §§ 4.1 and 4.2.

There are n workers qualified to perform a class of tasks, whose interarrival rate is exponentially distributed with parameter $\lambda ;$ the service rate is also exponentially distributed with parameter $\mu .$ . The average wage rate for these n workers is $R _ { H } .$ The coordination of workflow is carried out through a decision support system where there is a unit utilization cost of $R _ { T }$ for each message. Workers’ failure probability is defined as $p _ { s } \mathrm { ; }$ on average, 100 % of work must be reworked when such a failure occurs. A functional manager fails with probability $p _ { f } ,$ on average, 100b% of work must be reworked because of a function manager’s inability to correctly determine work schedules. Note that modeling product managers’ behavior is not necessary because of Assumption (A1).

We now obtain the total expected cost for using a centralized organizational design, $C _ { c } .$ The average system time of a production process is used to estimate production cost. The queue design for centralized organizational structure is a central M/M/n queue; there is no need to maintain separate queues for each worker. This stems from the fact that functional managers act as central controllers who choose workers to perform tasks at hand. Thus, if the assigned worker processes the task successfully, using Assumption (A4) and standard results from queuing theory $( \mathrm { e . g . }$ , Gross and Harris 1985), the expected production cost can be expressed as:

$$
\Big (\frac {W _ {c}}{n \lambda} + \frac {1}{\mu} \Big) R _ {H},\tag{1}
$$

where

$$
W _ {c} = \frac {(n \lambda / \mu) ^ {n} (\lambda / \mu) P _ {0}}{n ! (1 - \lambda / \mu) ^ {2}},
$$

and

$$
\frac {1}{P _ {0}} = \sum_ {j = 0} ^ {n - 1} \left\{\frac {1}{j !} \left(\frac {n \lambda}{\mu}\right) ^ {j} \right\} + \frac {1}{n ! (1 - \lambda \mu)} \left(\frac {n \lambda}{\mu}\right) ^ {n}.
$$

The expected coordination cost can be estimated using the sum of messages for coordinating the actual information and workflow and monitoring/supervising by the functional manager. We noted in § 3.1.1 that there are four messages passed between hierarchies for the actual flow of work. One message is passed from the product manager to the functional manager; one from the functional manager to the selected worker; one from the selected worker back to the function manager when the task is completed; and another from the functional manager to the product manager. Using ${ \mathrm { A s } } -$ sumption (A5), the expected coordination cost is

$$
\Big (4 + \frac {z _ {\gamma / 2} ^ {2} p _ {f} (1 - p _ {f})}{d ^ {2}} \Big) R _ {T},\tag{2}
$$

where the second term in the parenthesis is the number of sampling messages carried out by the functional manager; this term is described below.

Malone and Smith (1988) assume that no monitoring is necessary as the functional manager can keep track of the availability of individual workers by knowing when tasks are assigned to workers and when these tasks are completed. This assumption is acceptable if there is a small pool of workers that reside at the same location. However, the associated cost of monitoring is no longer trivial when the pool of workers gets larger and the production activities are set in a distributed work environment. Our model will include monitoring by considering it as statistical sampling with a binomial distribution. Assume that there is at least one worker available to perform the task at hand; let each draw of a worker in the sampling process be independent and identically distributed. Let $Y ~ = ~ 1$ if the worker is available, and $Y ~ = ~ 0$ if the worker is not available be a random variable for the sampling experiment with a binomial distribution with parameter $( 1 ~ - ~ p _ { f } )$ . In other words, $( 1 ~ - ~ p _ { f } )$ can be taken as the probability that a functional manager selects an available worker. However, $\Sigma _ { i = 1 } ^ { N } \ Y _ { i } / N$ is the realized $( 1 ~ -$ $p _ { f } ) .$ . Defining d as the distance between the realized and true $( 1 ~ - ~ p _ { f } )$ with probability $( 1 \mathrm { ~ - ~ } \gamma ) , \mathrm { i . e . }$

$$
P \left(\left| \frac {\sum_ {i = 1} ^ {N} Y _ {i}}{N} - (1 - p _ {f}) \right| <   d\right) = 1 - \gamma ,
$$

then

$$
N = \frac {z _ {\gamma / 2} ^ {2} p _ {f} (1 - p _ {f})}{d ^ {2}},
$$

where $P \ ( z _ { \gamma / 2 } \leq Z ) = 1 - { \gamma } / { 2 } ,$ , and $Z$ is a standard normal random variable. That is, the functional manager must sample at least $z _ { \gamma / 2 } ^ { 2 } p _ { f } \ ( 1 \ - \ p _ { f } ) / d ^ { 2 }$ workers so that there is $( 1 ~ - ~ \gamma )$ probability that the proportion of available workers in N is within d of $1 ~ - ~ p _ { f }$ (Larsen and Marx 1986).

As stated earlier in this section, disruption costs are modeled as rework as a result of workers’ and functional managers’ failures. By figuring in potential failures by workers as well as by functional managers and using Equations (1) and (2), the total expected cost for a task using a centralized organizational structure is:

$$
\begin{array}{r l} C _ {c} = (1 + \beta p _ {f}) & \Bigg \{\bigg (4 + \frac {z _ {\gamma / 2} ^ {2} p _ {f} (1 - p _ {f})}{d ^ {2}} \bigg) R _ {T} \\ & + \Big (\frac {W _ {c}}{n \lambda} + \frac {1}{\mu} \Big) R _ {H} + p _ {s} \Big (\Big (2 + \frac {z _ {\gamma / 2} ^ {2} p _ {f} (1 - p _ {f})}{d ^ {2}} \Big) R _ {T} \\ & + \Big (\frac {W _ {c}}{n \lambda} + \frac {\alpha}{\mu} \Big) R _ {H} \Big) \Bigg \}. \end{array}
$$

Next, we obtain the total expected cost for using a decentralized organizational design, $C _ { d } .$ We will employ a DSM using an auction-based mechanism to represent a decentralized organizational design. Since workers in this organizational structure make decisions and generate bids for auctions by considering only local conditions, the queue design must be a set of decoupled independent queues. Thus, there are n $M / M / 1$ queues–one for each worker. There is no queue maintained by the product manager because workers are now responsible for their own work. If the selected worker successfully processes the assigned task, using Assumption (A4) and the standard queuing results, the expected production cost can be expressed as:

$$
\left(W _ {d} + \frac {1}{\mu}\right) R _ {H},\tag{3}
$$

where

$$
W _ {d} = \frac {\lambda}{\mu (\mu - \lambda)}.
$$

Let a be the proportion of qualified workers contacted to participate in an auction to bid for future work. The expected coordination cost for using a DSM with an auction-based mechanism is

$$
(2 + 2 a n) R _ {T}.\tag{4}
$$

Two messages account for the actual workflow between the product manager and the selected worker; there are an request-for-bid messages sent from the product manager to qualified workers and an bids messages sent from the contacted workers to the product manager.

Modeling rework as costs associated with potential failures, and using Equations (3) and (4), the total expected cost for using a decentralized organizational design is:

$$
\begin{array}{l} C _ {d} = (2 + 2 a n) R _ {T} + \bigg (W _ {d} + \frac {1}{\mu} \bigg) R _ {H} \\ \qquad + p _ {s} \left((2 + 2 a n) R _ {T} + \bigg (W _ {d} + \frac {\alpha}{\mu} \bigg) R _ {H}\right). \end{array}
$$

## 4.2. Analysis

We now compare the total expected costs for both organizational structures on a single task basis. Taking the difference between $C _ { d }$ and $C _ { c } ,$ a centralized organizational design is preferred over a decentralized organizational design if

$$
(1 + p _ {s}) (2 + 2 a n) R _ {T} - (1 + \beta p _ {f})
$$

$$
\Big (4 + \frac {z _ {\gamma / 2} ^ {2} p _ {f} (1 - p _ {f})}{d ^ {2}} \Big) R _ {T} \geq \beta p _ {f} \Big (\frac {1}{\mu - \lambda} \Big) R _ {H}\tag{5}
$$

holds. Inequality (5) is obtained by using Assumption (A7) and $W _ { d } \geq W _ { c }$ (Malone and Smith 1988).

Using (5), the following result can be established (proofs for this theorem and the subsequent corollaries can be found in the Appendix):

Theorem 1. Define $\bar { R } _ { H }$ as the upper limit of $R _ { H }$

Equation (5). If $R _ { H } \geq \bar { R } _ { H } ,$ then a decentralized organizational structure is preferred. Conversely, if $R _ { H } < \bar { R } _ { H } ,$ then a centralized organizational structure is preferred.

Corollary 1. $\partial \bar { R } _ { H } / \partial p _ { s } \geq 0 ;$ A decentralized organizational design becomes more attractive to implement if workers become less prone to failures.

This corollary states that as agents (i.e., workers) are less prone to failure, $\bar { R } _ { H }$ decreases; thus, a decentralized organizational design becomes more attractive. This result arises from the fact that a DSM using an auction-based mechanism depends heavily on its workers to reveal availability information to the product manager. Thus, the more often workers reveal their true local availability, the more likely a DSM will succeed as an automated scheduling tool.

Corollary 2. $\partial \bar { R } _ { H } / \partial a \geq 0 ; A$ decentralized organizational design becomes more attractive to implement when the auction mechanism becomes more efficient.

This corollary is very intuitive because there are less messages to coordinate in using a DSM with an efficient auction mechanism. Thus, the likelihood that a decentralized organizational design is preferred increases because the expected coordination cost is decreased. In fact, a small a is equivalent to a good auction mechanism.

Corollary 3. $\partial \bar { R } _ { H } / \partial n \geq 0 ;$ A decentralized organizational design becomes more attractive to implement when there is a decreasing number of workers involved in the auction.

At first glance, this corollary does not make sense if it is viewed only from the perspective of the coordination of information flow within a work system. However, the result becomes clear if we take the supposition that an organizational design also deals with the decision making process. For the moment, assume that workers in a decentralized organizational structure are self-interested (e.g., Sandholm, 1993) so that collusion is not possible. As the pool of workers gets larger, then the marginal contribution of each decision $( \mathrm { i . e . , }$ bids) from each individual worker on the final scheduling outcome will decrease in a decentralized organizational structure. Now, compare the effect of an equivalent increase in the pool of workers in a centralized organizational structure. Since the decision making process rests solely on the functional manager, there will not be an increase in coordination cost nor a decrease in the marginal contribution to the scheduling outcome so long as $n > z _ { \gamma / 2 } ^ { 2 } p _ { f } \ : ( 1 \ : - \ : p _ { f } ) / d ^ { 2 } $ . Consequently, in facing an increased pool of workers, the expected communication cost for using a decentralized design may be reduced by assigning the decision making power to an identified leader such as a functional manager, thereby achieving an equivalent centralized design. Thus, the implementation of a DSM using an auction-based mechanism is suited for a decentralized organization with a manageable pool of workers/ agents.

Arnold and Lippman’s (1995) work on selling mechanisms supports our finding in Corollary 3. They compare distributed selling (i.e., making sale decisions on a product by product basis) to centralized selling $( \mathrm { i . e . , }$ making sale decisions on a batch of products) of a set of homogeneous products. They show that distributed selling is preferred if there is a limited number of products. However, centralized selling is preferred if the number of products to sell is large.

Corollary 4. $\partial \bar { R } _ { H } / \partial p _ { f } \leq 0 ;$ A decentralized organizational design becomes more attractive to implement when the failure rates of functional managers in a centralized organization increase.

This corollary is obtained by using Assumption (A9). In fact, Assumption (A9) is necessary for a more practical reason. That is, if $p _ { f }$ is not small, then a decentralized organization design is always preferred because, without this assumption, the validity of a functional manger acting as a central controller is no longer true. As functional manager’s failure rate increases, both production and coordination costs increase for the centralized organizational design, causing the increased preference to use decentralized organizational design.

Corollary 5. $\partial \bar { R } _ { H } / \partial d \geq 0 ;$ A decentralized organizational design becomes more attractive to implement when workers are hard to supervise or monitor.

As a functional manager desires to monitor his/her workers more closely (d gets smaller), the functional manager must sample more workers. Similarly, a small d implies workers are harder to monitor; for example, workers are physically separated from the functional manager. Consequently, the coordination cost for using a centralized organizational design increases, making a decentralized organizational structure more attractive.

Corollary $6 . \partial \bar { R } _ { H } / \partial \mu \geq 0 ; A$ decentralized organizational design becomes more attractive to implement when the tasks take relatively long to process.

This corollary states that an increase in $\mu$ will increase the likelihood of preferring a centralized work system. That is, when the processing time of a task is relatively small, then coordination costs play a more critical role in deciding which organizational design to deploy. In the case of employing a DSM using an auction-based mechanism, the coordination cost needed to handle requests-for-bid and received bids will overwhelm the savings from reduced production costs. Thus, the implication is that work environments with simple production or business processes are not appropriate for market-based systems. (Note that, as workers become more proficient in performing tasks alone, there is no net differential in production cost between the two organizational designs.) The effect of reduced processing time requirements is that it heightens logistical issues in the coordination of work and information. Thus, a DSM using auction-based mechanisms is suitable for distributed work systems with relatively long processing times.

Corollary 7. $\partial \bar { R } _ { H } / \partial \lambda \geq 0 ;$ A decentralized organizational design becomes more attractive to implement as the tasks interarrival rate increases.

This corollary states that an increase in the tasks interarrival rate will result in an increased preference for a decentralized organizational design. This seems to be counterintuitive because an increase in k suggests the need for an “invisible hand” to clear tasks from the system; i.e., a functional manager to direct the flow of work. However, the need to have an invisible hand assumes that the functional manager is available at that time $( \mathrm { i . e . , } p _ { f } = 0 )$ , which is not always true. Assumption (A9) suggests that $p _ { f }$ is small, but not zero. That is, our framework assumes the presence of a middle hierarchy within the centralized organizational design and that there is a probability that the functional manager might fail. This possible failure creates the preference for the decentralized system.

Corollary 8. $\partial \bar { R } _ { H } / \partial R _ { T } \geq 0 ;$ A decentralized organizational design becomes more attractive to implement if the technology used to perform messaging functions becomes cheaper.

By using Assumption (A6), Corollary 8 states that there is an increase in the likelihood that a decentralized workflow system would be preferred if there is an decrease in $R _ { T } .$ Clearly, as a decentralized organizational design depends on its workers to reveal availability information using messages through information technology, a decrease in technology utilization cost increases the likelihood that a decentralized organizational design is preferred.

## 4.3. Application of Results

The above first-order comparative static analyses are summarized in Table 1. They describe a set of conditions relating changes in system characteristics to the decision on the use of centralized and decentralized organizational designs. With respect to the implementation of DSMs using auction-based mechanisms, these conditions are: (i) workers are less prone to failures; (ii) good auction mechanisms exist to create marketlike environments; (iii) smaller pool of workers; (iv) failureprone functional managers such as those arising in a distributed work systems due to temporal and spatial separation; (v) difficulty in monitoring work behaviors; (vi) longer average task processing times; (vii) faster average task interarrival rates; and (iix) inexpensive information technology to enable messaging.

As noted earlier, the comparative statics described above suggest DSMs are suitable for some production and business processes. In a manufacturing environment, a plant with several functionally equivalent production lines is the most natural area of application. Examples are manufacturing of electronic car components (ECC) and wafer fabrication lines for producing electronic chips. In the example of an ECC, the product manager will set up a competition among the most appropriate production lines (i.e., agents in § 3.2). However, Corollary 6 implies that a DSM is not a suitable mechanism for scheduling simple task such as epoxy coating in a production line. In fact, the coordinating mechanism might take longer than the actual processing time. In such a case, using a rule such as first-come-first-serve may be the most efficient scheduling method.

In a white-collar environment, the example of a small business loan processing system in § 3.1 is a prime target for a DSM; mortgage application processing is also an ideal candidate. However, consider a process like securities trading. In securities trading, the actual trade itself is very short and therefore, is not suitable for a DSM. However, if contracts must be drawn and agreed by all parties involved (i.e., it is not a simple trade), then this negotiation and contracting process is likely to consume a large amount of time compared to the actual trade. Thus, the workflow loops between the traders and contract writers are excellent opportunities for implementing DSM as an automation tool. Moreover, the parties involved in the trade are almost surely to be physically distributed.

Thus, Table 1 provides a guide for classifying what production or business processes are likely candidates for DSM implementations. Of course, the interaction between the effects listed in Table 1 (i.e., the interaction terms between these variables) is also important; the analysis of these interaction effects is left for future research.

## 5. Conclusion

Like Kanban cards, auction mechanisms are used as tools to pass workers’ availability information in distributed work environments. In fact, the auction mechanism recognizes scheduling as problems in the allocation of scarce resources; without the scarcity of resources, scheduling problems do not exit. Moreover, an auction provides a setting for finding a total solution to the scheduling problem, not only involving the scheduling of requests, but also making sure that the requestor is satisfied. Thus, a DSM using an auctionbased mechanism has a request stage, a negotiating stage, performance of task stage, and finally a satisfaction stage. These four stages are in accordance with the speech-act framework (Denning, 1992) that is implemented by Medina-Mora et al. (1993) of Action Technologies in their line of workflow software.

Table 1 Summary of the Comparative Statics Analysis

<table><tr><td></td><td>Decentralized design will become more desirable it</td><td>Centralized design will become more desirable if</td></tr><tr><td>worker/agent failure</td><td>less prone</td><td>more prone</td></tr><tr><td>auction mechanism</td><td>more efficient</td><td>less efficient</td></tr><tr><td>number of workers/agents</td><td>decreasing</td><td>increasing</td></tr><tr><td>central controller failure</td><td>increasing</td><td>decreasing</td></tr><tr><td>monitoring functions</td><td>harder</td><td>easier</td></tr><tr><td>task processing time</td><td>longer</td><td>shorter</td></tr><tr><td>tasks arrival rate</td><td>faster</td><td>slower</td></tr><tr><td>messaging technology</td><td>inexpensive</td><td>costly</td></tr></table>

In this paper, we compare decentralized and centralized organizational structures by comparing their total expected costs. Theorem 1 and Equation (5) establish the trade off between having functional managers acting as controllers in centralized organizational structures and private information problems in decentralized organizational structures. Conditions (i)-(xii) suggest that a DSM using an auction-based mechanism would work well for a distributed work system where information technology is cheap, processing time is relative long, and the pool of agents is not large. In addition, the success of a decentralized organizational design depends on its auction mechanism to create marketlike environments that encourage truthful bidding, in contrast to a centralized organizational design’s dependence on the functional manager’s reliability.

However, our model does not address learning possibilities in bidding. For example, the product manager might learn workers’ behaviors from the auction, and devise incentive compatible contracts to deal with the inherent computational complexity of the methodology. In so doing, incentive compatible contracts encourage workers to be truth revealing. Truthrevelation mechanisms in the context of DSMs are another area of future research.

Acknowledgment This work was supported by the National Science Foundation under grants SBR 96- 02053 and DMI-9634808. The comments of Lyle Ungar and the Agent-Auction Research Workshop at the University of Pennsylvania are warmly acknowledged.

## Appendix: Proofs

Proof of Theorem 1. Consider $C _ { d } - C _ { c } \geq 0$ . Our goal is to find an upper bound for $\bar { R } _ { H }$ so that a centralized organizational design is preferred over a decentralized organizational design.

$$
\begin{array}{l} 0 \leq \Bigg [ (2 + 2 a n) R _ {T} + \Big (W _ {d} + \frac {1}{\mu} \Big) R _ {H} + p _ {s} \Big ((2 + 2 a n) R _ {T} \\ \quad + \Big (W _ {d} + \frac {\alpha}{\mu} \Big) R _ {H} \Big) \Bigg ] - \Bigg [ (1 + \beta p _ {f}) \left\{\Big (2 + \frac {z _ {\gamma / 2} p _ {f} (1 - p _ {f})}{d ^ {2}} \Big) R _ {T} \right. \\ \quad + \Big (\frac {W _ {c}}{n \lambda} + \frac {1}{\mu} \Big) R _ {H} + p _ {s} \Big (2 + \frac {z _ {\gamma / 2} p _ {f} (1 - p _ {f})}{d ^ {2}} R _ {T} + \Big (\frac {W _ {c}}{n \lambda} + \frac {\alpha}{\mu} \Big) R _ {H} \Big) \Bigg \} \Bigg ] \end{array}
$$

Using the fact that $W _ { d } > W _ { c } / ( n \lambda )$ (Malone and Smith 1988), Assumption (A7), and Assumption (9) which implies that $p _ { f } ^ { 2 } \approx 0 ,$ one obtains

$$
\begin{array}{l} (1 + p _ {s}) (2 + 2 a n) R _ {T} - (1 + \beta p _ {f}) \\ \left(4 + \frac {z _ {\gamma / 2} ^ {2} p _ {f} (1 - p _ {f})}{d ^ {2}}\right) R _ {T} \geq \frac {\beta p _ {f} R _ {H}}{\mu - \lambda} \end{array}
$$

Rearranging the last equation, putting it in terms of $R _ { H } ,$ and denoting the upper bound as ${ \bar { R } } _ { H } ,$ one obtains

$$
\bar {R} _ {H} = \frac {(1 + p _ {s}) (2 + 2 a n) R _ {T} - (1 + \beta p _ {f}) \frac {z _ {\gamma / 2} ^ {2} p _ {f} (1 - p _ {f})}{d ^ {2}}}{\beta p _ {f} \left(\frac {1}{\mu - \lambda}\right)} R _ {T}.\tag{6}
$$

Proofs of Corollary 1, 2, and 3. By the stability criterion of Assumption (A3),

$$
\frac {\partial \bar {R} _ {H}}{\partial p _ {s}} = \frac {(2 + 2 a n) (\mu - \lambda)}{\beta p _ {f}} R _ {T} > 0
$$

$$
\frac {\partial \bar {R} _ {H}}{\partial a} = \frac {(1 + p _ {s}) (\mu - \lambda) 2 n}{\beta p _ {f}} R _ {T} > 0
$$

$$
\frac {\partial \bar {R} _ {H}}{\partial n} = \frac {(1 + p _ {s}) (\mu - \lambda) 2 a}{\beta p _ {f}} R _ {T} > 0
$$

Proof of Corollary 4.

$$
\begin{array}{l} \frac {\partial \bar {q}}{\partial p _ {f}} = \frac {2 \beta R _ {T} \left[ (1 + p _ {s}) (2 a n + 2) R _ {T} - 2 R _ {T} (1 + \beta p _ {f}) - \frac {\beta p _ {f} R _ {H}}{\mu - \lambda} \right]}{\left[ (1 + p _ {s}) (2 + 2 a n) R _ {T} - 2 (1 + \beta p _ {f}) R _ {T} - \beta p _ {f} \left(\frac {1}{\mu - \lambda}\right) R _ {H} \right] ^ {2}} \\ - \frac {2 R _ {T} (1 + \beta p _ {f} + p _ {s}) \left(- 2 R _ {T} \beta - \frac {\beta R _ {H}}{\mu - \lambda}\right)}{\left[ (1 + p _ {s}) (2 + 2 a n) R _ {T} - 2 (1 + \beta p _ {f}) R _ {T} - \beta p _ {f} \left(\frac {1}{\mu - \lambda} R _ {H} \right. \right] ^ {2}} \\ = \frac {2 R _ {T} \beta \left\{(1 + p _ {s}) (2 + 2 a n) R _ {T} + \frac {R _ {H}}{\mu - \lambda} + 2 R _ {T} p _ {s} + \frac {R _ {H} p _ {s}}{\mu - \lambda} \right\}}{\left[ (1 + p _ {s}) (2 + 2 a n) R _ {T} - 2 (1 + \beta p _ {f}) R _ {T} \beta p _ {f} \left(\frac {1}{\mu - \lambda}\right) R _ {H} \right] ^ {2}} \\ > 0. \end{array}
$$

Proof of Corollary 5.

$$
\begin{array}{l} \frac {\partial \bar {R} _ {H}}{\partial d} = - \frac {(1 + \beta p _ {f}) z _ {\gamma / 2} ^ {2} p _ {f} (1 - p _ {f}) (- 2) d ^ {- 3}}{\beta p _ {f} \Big (\frac {1}{\mu - \lambda} \Big)} \\ = \frac {2 (1 + \beta p _ {f}) z _ {\gamma / 2} ^ {2} p _ {f} (1 - p _ {f})}{\beta p _ {f} \Big (\frac {1}{\mu - \lambda} \Big) d ^ {3}} \\ \geq 0. \end{array}
$$

Proofs of Corollary 6 and 7. They are straightforward conclusions from Equation (6).

Proof of Corollary 8.

$$
\frac {\partial R _ {H}}{\partial R _ {T}} = \frac {(1 + p _ {s}) (2 + 2 a n) R _ {T} - (1 + \beta p _ {f}) \frac {z _ {\gamma / 2} p _ {f} (1 - p _ {f})}{d ^ {2}})}{\beta p _ {f} \left(\frac {1}{\mu - \lambda}\right)}
$$

By Assumption (A6), n is large and thus, $\bar { \partial } { R _ { H } } / \partial { R _ { T } } \geq 0 .$

## References

Arnold, M. A., S. A. Lippman. 1995. Selecting a selling institution: Auctions versus sequential search. Econom. Inquiry 33(1) 1–23.

Baker, A. D., M. E. Merchant. 1993. Automatic factories: How will they be controlled. IEEE Potentials 12(4) 15–20.

——. 1996. Metaphor or reality: A case study where agents bid with actual costs to schedule a factory. S. H. Clearwater, Market-Based Control: A Paradigm for Distributed Resource Allocation. Addison-Wesley, Reading, MA.

Bertsekas, D. P. 1992. Auction algorithms for network flow problems: A tutorial introduction. Comput. Optimization Appl. 1 7– 66.

Clearwater, S. H., B. A. Huberman. 1994. Thermal markets for controlling building environments. Energy Engn. 91(3) 26–56.

Davis, R., R. G. Smith. 1983. Negotiation as a metaphor for distributed problem solving. Artificial Intelligence 20 63–109.

Denning, P. J. 1992. Work is a closed-loop process. Amer. Sci. 80 (July-August) 314–317.

Deshmukh, A. V., S. Benjaafar, J. J. Talavage, M. M. Barash. 1993. Comparison of centralized and distributed control policies for manufacturing systems. Institute of Indust. Engnr., 2nd Indust. Engnrg. Res. Conf. Proc.

Graves, R. L., L. Schrage, J. Sankaran. 1993. An auction method for course registration. Interfaces 23(5) 81–92.

Graves, S. C. 1981. A review of production planning. Oper. Res. 29(4) 647–675.

Gross, D., C. M. Harris. 1985. Fundamentals of Queuing Theory, 2nd ed. John Wiley, New York.

Henkoff, R. 1994. Delivering the goods. Fortune November 28. 64– 78.

Hinkkanen, A., R. Kalakota, P. Saengcharoenrat, J. Stallaert, A. B. Whinston. 1997. Distributed decision support systems for realtime supply chain management using agent technologies. R. Kalakota, A. B. Whinston, eds. Readings in Electronic Commerce. Chapter 12. Addison-Wesley, Reading, MA.

Huberman, B. A., T. Hogg. 1995. Distributed computation as an economic system. J. Econom. Perspectives 9(1) 141–152.

Kirkpatrick, D. 1993. Groupware goes boom. Fortune December 27. 99–106.

Larsen, R. J., M. L. Marx. 1986. An Introduction to Mathematical Statistics and Its Applications, 2nd ed. Prentice-Hill, Englewood Cliffs, NJ.

Lawler, E. L., L. K. Lenstra, K. Rinnooy, D. B. Shmoys. 1993. Sequencing and scheduling: Algorithms and complexity. S. C. Graves, et al., eds. Handbooks in OR & MS. Vol. 4 445–521.

Lin, G. Y. J., J. J. Solberg. 1992. Integrated shop floor control using autonomous agents. IIE Trans. 24(3) 57–71.

MacKie-Mason, J. K., H. R. Varian. 1994. Pricing congestible network resources. Working Paper, Department of Economics, University of Michigan, Ann Arbor, MI.

Malone, T. W., R. E. Fikes, K. R. Grant, M. T. Howard. 1988. Enterprise: A market-like task scheduler for distributed computing environments. B. A. Huberman, ed. The Ecology of Computation. Elsevier Science Publishers, Amsterdam, The Netherlands 177– 205.

——, S. A. Smith. 1988. Modeling the performance of organizational structures. Oper. Res. 36(3) 421–436.

Medina-Mora, R., T. Winograd, R. Flores, F. Flores. 1993. The Action Workflow approach to workflow management technology. Inform. Soc. 9. 391–404.

Miller, M. S., D. Krieger, N. Hardy, C. Hibbert, D. Tribble. 1996. An automated auction in ATM network bandwidth. S. H. Clearwater, ed. Market-based Control: A Paradigm for Distributed Resource Allocation, Chapter 5. Addition-Wesley, Reading, MA.

Nagurney, A. 1993. Traffic network equilibrium. Network Economics: A Variational Inequality Approach. Kluwer Academic Publishers, Boston, MA.

Radding, A. 1994. Stopping the bottlenecks with workflow analysis. Info World 16 (5)

Rathnam, S., V. Mahajan, A. B. Whinston. 1995. Facilitating coordination in customer support teams: A framework and its implications for the design of information technology. Management Sci. 41(12) 1900–1921.

Rosenschein, J. S., G. Zlotkin. 1994. Rules of Encounter: Designing Conventions for Automated Negotiation Among Computers. MIT Press, Cambridge, MA.

Sandholm, T. 1993. An implementation of the Contract Net Protocol based on marginal cost calculations. Proc. Eleventh National Conf. Artificial Intelligence AAAI/The MIT Press, Menlo Park, CA. Washington, D.C.

——. V. Lesser. 1995. Issues in automated negotiation and electronic commerce: Extending the Contract Net framework. Proc. First Internat. Conf. Multiagent Systems June.

Shaw, M. J. 1987. A distributed scheduling method for computer integrated manufacturing: the use of local area networks in cellular systems. Internat. J. Production Res. 25(9) 1285–1303.

Spearman, M. L., M. A. Zazanis. 1992. Push and pull production systems: Issues and comparisons. Oper. Res. 40 (3) 521–532.

Stonebraker, M., P. M. Aoki, R. Devine, W. Litwin, M. Olson. 1995a.

Mariposa: A new architecture for distributed data. Working Paper, Department of Computer Science, University of California, Berkeley, CA.

——, A. Pfeffer, A. Sah, J. Sidell, C. Staelin. A. Yu. 1995b. Mariposa: A wide-area distributed database system. Working Paper, Department of Computer Science, University of California, Berkeley, CA.

, R. Devine, M. Nornacker, W. Litwin, A. Pfeffer, A. Sah, C. Staelin. 1995c. An economic paradigm for query processing and data migration in Mariposa. Working Paper, Department of Computer Science, University of California, Berkeley, CA.

Upton, D. M., M. M. Barash, A. M. Matheson. 1991. Architecture and auctions in manufacturing. Internat. J. Comput. Integrated Manufacturing 4 (1) 23–33.

Varian, H. R. 1997. A solution to the problem of externalities when agents are well-informed . Amer. Econom. Rev. 84 (5) 1278–1293. . 1995. Economic mechanism design for computerized agents. Working Paper, Department of Economics, University of Michigan, Ann Arbor, MI.

Zlotkin, G., J. S. Rosenschein. 1990. Negotiation and conflict resolution in non-cooperative domains. Proc. National Conf. AI Boston, MA. August 100–105.

Andrew B. Whinston, Associate Editor. This paper was received on May 13, 1997 and has been with the authors 10 months for 1 revision.
