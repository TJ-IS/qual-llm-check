---
otero_id: 17263
otero_key: "YT6UXEHS"
title: "Self-organizing executive information networks"
authors: "James Christopher Westland"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90036-o"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Self-organizing executive information networks

James Christopher Westland

School of Business Administration, University of Southern California, Los Angeles, CA 90089-1421, USA

Organizations acquire decision support systems in order to deliver the information needed for decision making. But at executive levels, rapid changes in organizational structure or executive decision making can quickly obsolete an existing information dissemination structure. Insights gained from prior research in executive activities, executive support systems and neural networks are used in this research to design an adaptive, self-organizing system for the dissemination of information to executives. These self-organizing executive information networks are able to learn from the changing needs of their executive constituency. A neural network based executive information system incorporates a system for responding to organizational changes in responsibilities and information flows as an integral part of the information dissemination system. Extensive research in neural network based computer systems and in studies of biological systems have shown the practicality of this approach.

Keywords: Executive support systems, Neural networks, Information systems architecture, Self-organizing systems.

![](/api/attachments/YT6UXEHS/fulltext/images/44a3479f583653e8934f63182fc5860f9b304066a7b1d4022d07a8cba69ab133.jpg)

J. Christopher Westland is currently Assistant Professor of Information Systems at the University of Southern California. He received his Ph.D. in Information Systems from the University of Michigan; he previously received an MBA in Accounting and BA in Mathematics from Indiana University. He worked in industry during the eight years prior to his doctoral program, first as a Certified Public Accountant for Touche Ross in Chicago, and later as Database Ad ministrator and Computer Security Analyst for Rockwell International. He is a member of the Western Economic Association, The American Statistical Association, the American Institute of Certified Public Accountants, and The Institute of Management Science. He is also a member of the Business Honorary Fraternity Beta Gamma Sigma, with biographies listed in various Who's Who publications. While at the University of Michigan, he was awarded a Dykstra Fellowship for Teaching Excellence, an Arthur Andersen & Co. Foundation Dissertation Fellowship, a Foreign Language & Area Studies Fellowship by the U.S. Department of Education, and several Paton Fellowships. His current research focuses on the economic analysis of information technologies and on new technologies for software engineering.

## 1. Executive Support Systems

Rapid changes in organizational structure and in executive decision making can quickly obsolete an existing information system. Around 50% of total implemented program code is unused, “dead” code, and an estimated 50% of all periodic reports produced in an organization are obsolete at any one time. The U.S. spends over \$100 billion annually for program coding and maintenance [31]; most of this is required to manage “dead” code and changed information needs [32]. In the past, rapid organizational and environmental change, the major reason for “dead” code and useless reports, has posed significant problems for the design of executive support systems. Executive support systems (ESS) may be compromised by information overload, information that is unavailable when needed, dissemination of useless or irrelevant information, and reporting of important information after it has become obsolete.

Information needed for clerical tasks and middle management decisions are typically well defined and stable, even in the face of employee turnover. The same is not true of information needed by executive management. This information is often loosely defined, subject to radical changes influenced by the organization's business environment, and affected by changes in executives' responsibilities and positions in the organization. Executive support systems must acquire, record, store, process and disseminate information from both internal and external sources. The benefits from these systems, and the primary justifications for systems expenditures, lie in the timely dissemination of useful information to executive decision makers.

This research constructs an algorithm for computer implementation, which allows the beneficiaries of an information dissemination system to define dynamically the information that is important to them. This algorithm could be incorporated into many existing executive support systems via message routing and information retrieval subsystems. The algorithm may be used to disseminate organizational information internal to the firm, such as electronic mail or financial reports; and may also be used to disseminate information originating outside of the firm, such as up-to-the-minute news reports from electronic news services, securities prices, and so forth. A self-organizing ESS can respond to most sources of ESS failure and stimulate better executive communication.

Swanson [32] proposed that the information systems that survive in an organization must occupy an available niche in both the organizational and technological environments; they must continually evolve, through maintenance, in order to adapt to changes in both environments. Swanson's evolution is Lamarckian rather than Darwinian – systems evolve by responding creatively to their needs. To succeed, this sort of evolution requires intense outside management by systems analysts, programmers and end users; in the process, there is interpretation, information loss, and error in the maintenance and design of new systems.

Huber [15] suggested that post-industrial organizational environments are turbulent at the executive level and that executives need to be supported with robust, risk-managed information systems. Both evolutionary and risk-managed approaches are appropriate where turbulence in the organizational environment is the product of uncertain outcomes of resource allocation decisions.

Where turbulence is the product of rapid structural or personnel changes, risk assessment must be based on unknown executive management talents in unknown organization structures. Stability of the organizational command, communication and control structure will be in question. Executive responsibility and position changes affect not only the information flow around the executive whose responsibilities change, but also affect the executive's superiors, peers and subordinates. Required changes in information flows will increase exponentially with changes in organizational structure, causing predefined information flows to become obsolete.

This research develops a self-organizing network which allows an executive profile of index terms to evolve as the information system is used, and as information is disseminated throughout the organization. Much of this evolution involves trial and error learning. Accuracy of routing, and relevance of information will improve over time if a system can resolve its own errors. This provides an important economic justification for self-organization, since no outside control mechanism is required to assure accuracy.

Much of the literature on executive management and executive support systems indicates that turbulence resulting from structural or personnel changes is common. Nash [23], Rockart and De-Long [27], Rockart and Treacy [28], and Houdeshel and Watson [13] have discussed the manner in which executive information systems might adapt to this sort of turbulence. In organizations experiencing rapid structural or personnel changes, systems that can modify themselves, and quickly “learn” from environmental cues will be superior to static rule-based systems. The self-organizing systems presented here are intended to address problems arising from this type of turbulence.

Mintzberg [20], [21] categorized executive activities into ten distinct roles – interpersonal roles of figurehead, leader and liaison; informational roles of monitor, disseminator and spokesman; and decisional roles of entrepreneur, disturbance handler, resource allocator and negotiator. Communicating, scanning, and delegating are central to the informational roles, but are also important in the performance of other roles. Mintzberg [20], [22] found that executives performed their roles under severe time constraints; generally only allowing five to ten minutes per problem or issue addressed. Mintzberg's conclusions imply that both information scanning, and information dissemination over very short time periods are important to successful management. This suggests that obsolescence of information is a problem that must be controlled in executive information systems, and traditional paper based reporting is inadequate for executive needs. This is one reason that most executive support systems are on-line systems.

Executives benefit from an executive support system's ability to scan and route massive amounts of information to them through a communication network. Information received by an executive must be categorized, e.g. via an index such as a set of keywords, so that the executive support system is able to surmise whether or not a particular piece of information is relevant or not to the executive's information needs. Categorization involves matching the descriptors of an electronic message with those of an executive profile – i.e. a list of categories in which the executive has an interest. Categories may be based on combinations of topics or subject-headings, and additionally should consider authors whose output may be of interest, criteria of quality (e.g., source reliability), currency of information, completeness, length, and prior accuracy. Categories and indices in most database systems are determined by specialists who are neither users nor beneficiaries of a system; in self-organizing networks, executives themselves should be able to determine categories and indices.

The usefulness or relevance of information to an executive's decision making needs is determined by comparison of the index associated with an electronic message, with an information needs profile of the executive. In a self-organizing system, the profile is intrinsic in the network's connection matrix. This allows the executive to maximize the amount of relevant information that he consumes, to minimize the amount of irrelevant information that he consumes, and to guard against overload. In high velocity [5] or turbulent environments [15] it is doubtful whether indexers can ever provide a static prediction of executive information needs. Thus self-organizing systems are a viable alternative to indexers in turbulent environments.

Executive support systems are distinguished by the large scope and breadth of information sources available to them. In environmental scanning subsystems, or subsystems for reporting from large commercial databases, information sources are external to the firm, and information is acquired via monetary transactions in an open market. In online reporting and electronic mail subsystems, information may become obsolete quickly; e.g. with program trading in the stock exchanges, stock bid and ask information may be come obsolete in milliseconds. In electronic mail subsystems, other individuals are the source of personalized electronic messages. In these cases, hardware and software must be designed to alert the executive of the existence of messages and information, through paging, printouts, and so forth. Despite their instantaneous transmission of messages, existing electronic mail systems are often ineffective because they allow a message to languish in electronic storage for days when its recipient fails to turn on his terminal.

Executives often do not know that they want a piece of information until they receive it, or are unable to access, in real time, relevant information that they exists; such information may be designated “fugitive” information. Conversely, they may not know that it exists until they receive it; such information may be designated “serendipitous” information. Both fugitive information and serendipitous information pose significant problems in information dissemination. Blair’s [3] empirical study of full-text indexing on a large legal database indicated that most systems have a wealth of information that is potentially “serendipitous,” but that at least 80%, and perhaps as much as 99.99% of this serendipitous information never reaches the individuals that would find the information useful [4]. Westland [34], [35] showed that this problem results from the manner in which information overload is managed in very large database systems. Full-text indexing is often used to increase the amount of serendipitous information received; but this is only possible in automated systems with either very high throughput, or very small databases.

Information is “fugitive” because of time constraints in decision making. If executives had unlimited time to make a decision, then they could peruse every available piece of information that might even be remotely relevant to their decision. But with limited time, they are forced to cull a small subset of information, perhaps missing most of the information that is relevant to their decision making. The ability to quickly route needed information to an executive within given decision making time constraints is perhaps the salient feature of computer based executive support systems. The automated capability to access and report large amounts of relevant information in very short time periods will minimize the level of fugitive information the executive needs suffer. The optimal approach to minimizing fugitive information is to develop better algorithms for finding and reporting relevant information to the appropriate executive.

A self-organizing executive information network patterned upon a neural network provides four advantages in maximizing serendipitous information and minimizing fugitive information.

First, the neural model provides a good representation of the command, communication and control network in an organization. The neurons in a neural network both produce information bearing signals and are influenced by the information in the signals that delineate the channels through which information is disseminated. Similarly in the organizational network, executives are producers and consumers of information as well as delineators of the channels through which this information is disseminated. In contrast, rule-based executive support system models require the separation of these functions.

Second, neural networks are self-organizing $[14]$ ; they have intrinsic processing paths that learn from feedback. They do not need an external subsystem for formatting, delivering and responding to external feedback, such as is found in traditional computer information systems. This feature eliminates the need to externally manage the information channels in a self-organizing system, and assures that the system will adapt to organizational changes rapidly. Self-organizing, neural network based systems solve some of the problems of “dead” code and useless reports by providing the ability to reflect changes in the organizational environment rapidly.

Third, research has been conducted on the capabilities of neural networks in medicine and biology [7], and in artificial intelligence in computers [26]. Much is known from simulations and from the study of biological systems, about convergence speeds and effects of various types of learning on the self-organization of neural networks. Convergence to useful solutions in neural networks is generally faster than in rule-based and statistical systems. This latter feature has made neural networks a successful technology for such diverse applications as explosives detection systems in airports, for the system based on a Hitachi chip that manages the routes for the Japanese bullet train, and various other systems requiring a fast, optimal response to feedback. Executive information systems patterned on neural networks would gain from the study of existing implementation successes in this field. In addition, basic problems in architecture, memory management, and processing in neural networks have already been solved. There are several successful neural network software packages for von Neumann computers, as well as customized neural network VLSI chips. For example, at the time of this writing, California Scientific Software's BrainMaker neural network software package runs at 260 thousand operations (connections) per second on a 16 MHz i386 based microcomputer, and is priced at \$100 [40]. Texas Instruments sells their TMS32020 SRAM neural chip for \$125; this chip is typically configured in an eight device module that can store 84 KBytes of patterns, and deliver 2.5 billion operations per second [41].

Finally, neural networks offer a distinct advantage over the “rule-based” or “procedural” processing alternatives that are used in existing executive information systems. In rule-based systems, human decision making activities are explicitly interpreted into computer language. Two kinds of “rules” are used in corporate dissemination of information: first, corporate policy; “need to know” constraints, and so forth, determine who may access and receive certain information. Second, the decisions of authors of electronic messages determine who receives the information by specifying the recipients of their work. The translation of organizational rules to computer-based rules is a labor intensive, highly subjective, and error-prone process. Rule-based systems are generally not capable of adapting to situations not foreseen during the rule translation process.

Neural networks, on the other hand, allow adaptive learning to occur via dynamic feedback of information directly from information users, modulators, and authors. This avoids the error-prone translation process that is inherent in rule-based systems. Neural networks are also able to respond to minimal, subjective, sometimes incorrect, and sometimes incomplete information from their own components, whereas rules must be constructed with rigid formality. A corporate information system patterned on neural networks would be able to adapt rapidly, with a minimum of informational feedback to external marketing and financial environments in the same fashion that a biological system adapts to its external environment. Conversely in traditional rule based information systems, feedback for modification of the executive's information channels itself needs to be communicated, interpreted, formalized, and passed through several hands prior to being implemented in an information system. This process makes rule based systems development and modification inefficient, error prone and time consuming. Selforganizing networks do not require these intermediate formalizations in order to adapt to changes in their environment.

## 2. Linguistics and Message Indexing

The model of a computer based executive support system adopted here assumes that information of relevance to executives: (1) may be succinctly described and categorized by some indexing system, or system of signs, based on the executives' business language; (2) arrives asynchronously into a central computer based repository such as a database, library or file; and (3) has a specific, generally short, useful life after which it becomes obsolete, and during which it must be disseminated to the appropriate recipients.

Information of importance to executives is expected to be ill-structured, and much less amenable to maintenance in a structured database than is the information processed in traditional MIS. For example, [6] described a number of cases where even the structured data of traditional computer based accounting and statistical reporting systems was too ill-structured for even flexible structures such as provided by IBM's AD/Cycle Repository, and other CASE dictionaries. This suggests that the categorization and indexing problem is endemic and widespread. Ill-structured information, such as the information expected to be of interest to executives, is probably best categorized and indexed using the executive's own business language, or "jargon."

The linguistic study of signs and sign-systems is called semiotics. In semiotics, the vehicle of categorization is the sign. Peirce [24] defined a sign as “something which stands to somebody for something in some respect or capacity”; and Eco [8] defined semiotics as “the discipline studying everything which can be used in order to lie.” Signs refer us to a relation between a signifier and the signified; in Eco’s terminology, this is the relation between “expression” used in communication and “content” which somehow embodies what is really meant when the sign is used. A sign system is a set of relations and expressions for the content of a body of knowledge, belief system, or set of objectives and conjectures. Only the sign is communicated, but the sign system assumes an underlying system of shared experiences between communicators which generates the relations - e.g. schooling, corporate culture, nationality, and so forth. The expression is generally a very terse statement of the content. An example of this sort of signification may be found in print; the typical compression ratio for a New York Times article to its headline is between $10^{2}$ and $10^{3}$ to 1 (measured by character count). Greater compression may result in excessive equivocality; less may result in an unwillingness of the reader to expend the effort in comprehending the headline. The process of constructing expressions and relations describing a particular content is called signification. Equivocality arises in signification as a result of noisy, inadequate or unshared relations, as well as the inherent compression of the issue content in an expression.

Semiotic models are appropriate for this research because they focus upon the transfer of information between individuals via abbreviated messages composed of expressions. Information routing decisions in this research are based upon the characteristics of these abbreviated expressions, or indices associated with a particular message content. There is considerable analytical, anecdotal and empirical evidence in support of a semiotic description of the underlying organization of individual executive perception and communication via a specialized business language.

Research by Kotter [17], Isenberg [16] and Pounds [25] suggests that executives manage a prioritized agenda of issues, and that this agenda defines the scope of their activities. Mintzberg [19], [21] noted that “the manager adsorbs information that continually bombards him and forms it into a series of mental models.” The effectiveness of the executive is largely dependent upon the quality of his models since these mental models form the content of his perception of an issue. Kotter perceived the agenda as a mental model consisting of interconnected facts, strategies and plans grouped around various issues and objectives. This research similarly makes the assumption that executive communication is issue based.

Issue based categorization serves several functions. It allows clusters of facts, new items, and opinions to be specified and retrieved without overloading the executive with useless topical information. The electronic messages comprising a cluster will tend to be completely relevant to a specific executive's responsibilities, or completely irrelevant. Issue based categorization also assures that the executive will expend considerably less effort defining information channels than he will benefit upon dissemination of information to himself.

In the model presented here, executives communicate via a vocabulary of expressions that constitute a business language or “jargon” used in discussion of issues. It is the product of signification where a large number of perspectives, experiences, activities and other “relationship generating” circumstances are shared between communicating executives. Executive information dissemination may occur via face to face meetings, but it also takes place through personal letters, memoranda, electronic mail, journal clippings, computer reports, and so forth. The next section describes an executive support system supporting the latter types of activities.

## 3. Self-Organizing Executive Information Network Design

The self-organizing executive information network provides a set of communication channels from authors and senders of information, who may or may not be executives, to consumers of information, who presumably are executives [36], [37], [38], [39]. Information of interest to executives is expressed in terms of issues and authors; and there is associated with each electronic message an index, which will include the author as well as other information. The author categorization is especially important when an author is another executive; for example, everyone may want to know what the president of the corporation has to say.

A self-organizing executive information network contains an interconnected set of “processing units” modulating a flow of “electronic messages” through specific “information channels.” Input processing units provide business language expressions for information, and output processing units provide executive’s information reporting hardware, such as video display terminals, that also serve as vehicles for the executive’s feedback of teaching signals into the system. This section describes these processing units and the nature of their interconnections in a self-organizing executive information network, following [30].

Systems Stimulus: In the selective dissemination of information, the arrival of information stimulates the system to deliver. Assume that a time-sequenced stream of electronic messages, $\Psi(t)$ , arrive sequentially and asynchronously to the executive information system; thus arrival time t uniquely defines each packet. Each packet has an associated topic-author descriptor set; i.e. an executive summary, headline, keyword list, and so forth.

Input and Output Processing Units: Processing units are denoted $v_{i}$ , and are dichotomized into input (index descriptor) and output (executive) units. Let the input subscripts run from 1 to $v_{\delta}$ ; where $v_{\delta}$ is the number of index descriptors in the vocabulary set that is available to describe electronic messages; and the output subscripts run from $v_{\delta} + 1$ to $v_{\epsilon}$ , where $v_{\epsilon} - v_{\delta}$ is the number of executives to which information may be routed. The subscripts $\delta$ and $\epsilon$ are presumed to reference specific descriptors and executives; they are expected to change dynamically over time, as discussed below.

The vocabulary set defines the language in which the executives perceive and respond to information – an automated system may coach executives in appropriate terminology. The vocabulary size $v_{\delta}$ corresponds to the number of inputs available to the executive information system, i.e. the number of ways that information may be categorized for dissemination throughout the system. $v_{\delta}$ is allowed to change as a result of feedback from executives and as a result of new developments in the environment.

Dynamic Changes in Message Indexing Vocabulary Descriptors $v_{\delta}$ : $v_{\delta}$ is the number of descriptors in the vocabulary set that is available to describe electronic messages; and the output subscripts run from $v_{\delta} + 1$ to $v_{\epsilon}$ , where $v_{\epsilon} - v_{\delta}$ is the number of executives to which information may be rerouted; $\delta$ and $\epsilon$ may change in value dynamically over time. Two processes are affected by the dynamic change in either $\delta$ and $\epsilon$ : (1) the process required to incorporate new information concerning changes in either indexing vocabulary descriptors $\delta$ or executive organizational structure $\epsilon$ , and (2) the process with allows the connection matrix $\{\omega_{ij}\}$ , the activation vector $\{\alpha_{i}\}$ , and the output vector $\{\theta_{i}\}$ to be dynamically restated, without running out of computing resources.

The first aspect could be addressed by assigning responsibility for network administration to some individual, and making that individual responsible for updates to the representation of indexing vocabulary or organizational structure in the system. Then dynamic changes in $\delta$ are not necessary in the system. The system would be more appealing if there were no requirement for human intervention or administration outside of that associated with communications terminals directly accessed by executives or executives staff.

Conversely, executive users may be allowed to suggest their own index categorizations, perhaps as a result of reviewing serendipitous information and deciding to route that information to themselves and others in the future. In this case, information about new index terms may be polled from the user's terminal as a cost of system's use. The problem is one of changing the dimension of a matrix. In fact, this problem is handled very efficiently by existing compilers and operating systems. There are two approaches - static, where memory space is allocated by the programmer in advance of any calculation using the matrix; and dynamic where memory management routines based on heaps, stacks, reference counts or garbage collection algorithms are used to allocate memory space at run time (these still assume a maximum space, and there is always, still, the possibility of running out of memory). If prior executive information systems may serve as a guide, as in [13], then the number of executives benefiting from the system $v_{\epsilon} - v_{\delta}$ is probably not more than several hundred in most organizations, and memory limitations are not a problem.

Dynamic Changes in Organization Structure $v_{\epsilon}$ : $v_{\epsilon} - v_{\delta}$ is the number of executives to which information may be routed. The method of addressing this component was considered under the previous heading. Changes in organization structure could be obtained by requiring users to describe their immediate superior and subordinates as a prerequisite for using the system.

State of Activation: An input unit $v_{i}$ , that corresponds to a particular author-topic descriptor, receives an activation level $0 < \alpha_{i}(t) < 1$ corresponding to its descriptiveness of, or relevance to, the electronic message $\Psi(t)$ . Output unit j receives an activation level $0 < \alpha_{j}(t) < 1$ corresponding to the usefulness of a set of electronic messages to executive j.

Output of the Units: Units interact by transmitting messages to their neighbors. The routing of these messages, and therefore the effect they have on their neighbors is determined by their degree of activation $\alpha_{i}$ . Associated with each unit $v_{i}$ , there is an output function, $\theta_{i}(t)$ . Sometimes $\theta_{i}(t)=\alpha_{i}(t)$ , but neural network studies have shown that when $\theta_{i}$ is a threshold function, i.e. when $\theta_{i}$ is zero below a certain level of activation, the system tends to suppress “noise” more effectively. Uncertainty and incorrect information, i.e. “noise”, fed back by executives may be more effectively handled via a threshold function.

Pattern of Connectivity and Message Propagation: Processing units are connected to each other via a connection matrix; the strength of the message propagation from the output of $v_{i}$ to the input of $v_{j}$ is given by $\omega_{ij}\in\Omega$ ; where

$$
\Omega = \left[ \begin{array}{c c c} \omega_ {1 1} & \dots & \omega_ {1 v _ {\epsilon}} \\ \dots & \ddots & \dots \\ \omega_ {v _ {\epsilon} 1} & \dots & \omega_ {v _ {\epsilon} v _ {\epsilon}} \end{array} \right].\tag{1}
$$

Ω is called the connection matrix since it determines the strength of connection between units. Connections from input to output units represent the degree to which information referenced by the specific input unit (index descriptor) may be useful to the output unit (executive); connections from output to input represent executive defined teaching signals that allow the network to “learn” by adjusting the activation levels of its input units. This latter set of connections imbues the executive information network with its “self-organizing” capabilities. Negative values of $\omega_{ij}$ are inhibitory connections, and positive values are excitatory. Connections between input units (index descriptors) all have $\omega_{ij}=0$ ; but $\omega_{ij}$ may be greater than zero between output units, representing the influence that one recipient of information may have on another.

Teaching signals in self-organizing networks are not messages from recipients to originators of information. Rather, the information system itself requests a teaching signal as a part of its operation. The teaching signals themselves are not sent to the authors of messages, rather they are used to calculate the new connection matrix for the system.

Activation Rule: The activation rule determines how the output of units connected into a particular unit are combined with one another to produce a new state of activation. Research in neural networks has generated many activation rules; [26] defined over 80 for a particular system. Only a few, though, have consistently allowed fast and robust learning by the neural network. The simplest activation rule is one in which the new activation state is given by the connection weighted outputs, i.e. $\alpha(t+1)=\Omega\theta(t)$ where $\alpha=\alpha_{1}(t+1),\ldots,\alpha_{v_{i}}(t+1)]^{T}$ and $\theta=[\theta_{1}(t),\ldots,\theta_{v_{i}}(t)]^{T}$ . This type of linear activation function tends to be impractical because it is extremely sensitive to “noise”; i.e. incorrect or incomplete feedback from executives; and to the initial weight $\omega_{ij}$ in the system. A practical way to eliminate noise is to allow no change to the state of a unit if the incoming message is below a certain level – this is the “threshold” approach taken by biological nervous systems. The most common class of “threshold” approach activation functions is the quasi-linear activation function

$$
\alpha_ {i} (t + 1) = F \left(\omega_ {i 1} \theta_ {1} + \dots + \omega_ {i k} \theta_ {k}\right),\tag{2}
$$

where F is a non-decreasing function of a single type of input.

## 4. Teaching Signals and Learning Rules in Single and Multi-Level Networks

The network developed to this point provides a vehicle for learning through the connection matrix $\Omega$ . By modifying the strengths of connections $\omega_{ij}\epsilon\Omega$ , the network is able to alter the routing of electronic messages. Ideally, we would like $\Omega$ to converge to a set of values that provide the maximum relevance of information presented to the consuming executives. Previous research in parallel processing provides a guide for the sort of learning rules that possess the desirable characteristics of (1) fast convergence, (2) sensitivity to new information and new information needs, and (3) insensitivity to errors, incomplete information or other “noise.” Particular learning rules have been shown to successfully exhibit these characteristics in previous neural network research.

The simplest approach to implementation of a self-organizing executive information network utilizes Hebbian learning. Hebb [11] suggested a learning rule appropriate in neural networks where if a unit $v_{i}$ receives an input from another unit $v_{j}$ , then if both are highly active, the weight $\omega_{ij}$ from $v_{i}$ to $v_{j}$ should be strengthened. In simple form, this is

$$
\omega_ {i j} (t + 1) = \omega_ {i j} (t) + \kappa \alpha_ {i} \theta_ {j},\tag{3}
$$

where $\kappa$ is proportional to the learning rate. Grossberg [10] proposed a modification of Hebbian learning that dampens the output message in order to make the network less sensitive to “noise”. In simple form, Grossberg’s rule is

$$
\omega_ {i j} (t + 1) = \omega_ {i j} (t) + \kappa \alpha_ {i} (t) [ \theta_ {j} (t) - \omega_ {i j} (t) ].\tag{4}
$$

where $\kappa$ is proportional to the learning rate. Hebbian rules would tend to reinforce existing routings in an executive information network. Hebbian learning might be perceived as a “supply side” approach to network learning in that the authors will tend to determine the routing of electronic messages out of habit. This is probably a good approximation of the information network that arises in the normal course of business, where authors tend to route their memoranda, and so forth to particular executives, because that is the way they have previously routed them. For example, computer printouts are often disseminated according to well-entrenched routing schedules that survive long after organizational changes have made much of the delivered information irrelevant. Hebbian learning is “unmanaged” executive information system learning. The subsequent learning rules may be considered to “manage” the routings through executive feedback.

Barto and Sutton [2] describe a general version of Rosenblatt's [29] perceptron learning rule for which the perceptron convergence theorem has been proven. A “managed” approach to learning in a self-organizing network is embodied in generalized perceptron learning. Perceptron learning modifies the basic Hebbian learning in a network via a teaching message, $\eta_{ij}(t)$ . After reviewing an electronic message $\Psi(t)$ delivered by the executive information system, the jth executive generates teaching message, $\eta_{ij}(t)$ that is an opinion concerning the relevance of this packet to information referenced by the ith descriptor. In simple form, this is

$$
\begin{array}{l} \omega_ {i j} (t + 1) \\ = \omega_ {i j} (t) + \kappa [ \eta_ {i j} (t) - \alpha_ {i} (t) ] \theta_ {j} (\alpha_ {i} (t) \omega_ {i j} (t)), \end{array}\tag{5}
$$

where $\kappa$ is proportional to the learning rate; i.e. the rate at which the self-organizing executive information network adapts to changes in the responsibilities and preferences of the executives of the organization. Similar rules presented in [1] and [26] exhibit the desired properties of convergence, responsiveness and noise suppression. In this rule, large differences between an executive's utility for the information referenced by a particular descriptor, and the current activation level of that descriptor will tend to greatly modify the connection weight in the appropriate direction.

The models defined to this point operate by recognizing descriptors. It would be difficult to use such systems to identify information whose description involved more than a minimum level of semantic complexity. Neural network research has responded to this inability of single level networks to handle complex and subtle interrelationships via multi-level linkage structures, i.e. in which the output from one level provides the input stimulus to the next level. Multi-level schemes have been devised that lead to stable classifications of complex phenomena and that converge quickly to equilibrium solutions. Extension of the current multi-layer executive information networks may be premature at this point, but they demonstrate the richness and depth of neural network solutions for the design of self-organizing executive information systems. Certain specific problems can be addressed via multi-level networks.

The most successful of the multi-layer networks is a competitive learning approach defined in [9], [10] and [33]. In competitive learning, the various teaching signals, or sources of information concerning network structure, indexing $\delta$ and organization structure $\epsilon$ , are assumed to conflict at times. Such a situation may arise for two reasons. First, when a new index or topic area for categorization of information is proposed, it should only be added to the network if there is a significant amount of information that may be classified under this index, and if there are executives who would benefit from information in this topic area. Competitive learning offers an information aggregation feature that will insure that both of these objectives are met. Second, when organization structure changes, if the source of structural information is the executive user of the network, then errors may occur. Competitive learning in the network provides a voting mechanism with which to control errors in specification of the structure. In both cases, competitive learning provides a control over accuracy of information, and satisfaction of users with the system. Where the issues involved require semantic complexity of expression, accuracy and error control will be necessary to control the resulting communications ambiguity.

Competitive learning could be implemented in a self-organizing information network in the following manner, following $[10]$ which specifies a simple circuit for competitive learning. A network similar to the one defined previously is stacked on top of that network. The network defined previously, i.e. the first layer, is segregated into groups of executives, based on affiliation with organizational division, and the outputs of these groups are pooled and directed toward the inputs of the secondary layer. A unit in the secondary layer receives inputs from all of the units in the primary layer. Connections between layers are excitatory and connections within layers are inhibitory. Each layer consists of a set of clusters of mutually inhibitory units. The units within a cluster inhibit one another in such a way that only one unit per cluster may be active. The configuration of active units on the primary layer represents the input patterns for the secondary layer.

## 5. Implementation

Initial implementations of self-organizing executive information networks would most likely be extensions of E-mail systems, given that currently sold executive information systems software often takes an extended E-mail approach. In addition to message transfer it will provide automated intermediaries to extract information items from computer databases, files, and so forth, and human intermediaries to obtain information items not on the computer. Information would be presented to the executive via a high-resolution, real-time device such as the large screen monitor, via windows in a “desktop organizer” type of software package. System’s feedback from the executive will be required as a “price” of obtaining each electronic message. Network teaching messages will be facilitated via mouse or keyboard activated responses to questions such as: (1) I want / do not want this type of information in the future; (2) send this electronic message to X (another executive); (3) do not allow access to this type of electronic message to X (another subordinate executive); (4) ask X (another executive, subordinate, or information intermediary) for information of a certain type that is not available on the database. Human engineering of the software interface can make the “price” of obtaining information feedback minimal. Research presented in [1], [10], and [12] provides additional insight to some of the technical problems and approaches associated with self-organizing information dissemination.

Minsky and Papert [18] provide an analysis of neural network models which proves that certain classes of concepts cannot be represented in neural networks, e.g. connectedness in a torus. Although these limitations are important where neural networks are being used to mimic the activities of humans, these limitations do not affect the usefulness of self-organizing executive information networks. Neural network models are adequate to address any requirement in the domain of information dissemination applications. This domain requires only that there be fast adjustment to external feedback, and rapid convergence to equilibrium when external feedback becomes stationary. Self-organizing executive information networks do not attempt to mimic biological systems; rather they use what is known about biological systems to guide the design of executive support systems.

## 6. An Example

The self-organizing network just presented provides a general description of a message routing system that reflects executive information needs. This section presents an example of such a system using two index terms and distributing to two executives. Extensions to this approach could be implemented using matrix processing software. The following six steps are assumed to occur in the information acquisition and distribution process in ESS.

Step 1: electronic messages are acquired from external news services, internal reports, executives, and so forth.

Step 2: Index terms are assigned to electronic messages.

Step 3: electronic messages are distributed to executives based on the distribution network weights $\omega_{ij}$ .

Step 4: electronic messages are consumed by executives.

Step 5: electronic messages having been consumed, are then evaluated for relevance; e.g. if information consumption is performed online, simply require an evaluation of the electronic message before going to the subsequent screen.

Step 6: The distribution network is updated to reflect the executives' current information needs.

Consider the following connection matrix initially set up to describe distribution of electronic messages to executives

$$
\Omega (t) = \{\omega_ {i j} \} = \left[ \begin{array}{c c c c} 0 & 0 & 0. 5 & 0. 5 \\ 0 & 0 & 0. 5 & 0. 5 \\ 0. 5 & 0. 5 & 0 & 0 \\ 0. 5 & 0. 5 & 0 & 0 \end{array} \right].\tag{6}
$$

The explanation of this matrix is as follows. Connection weights $\omega_{31}$ , $\omega_{32}$ , $\omega_{41}$ and $\omega_{42}$ represent index terms associated with a single specific electronic message (input) 1 and 2 respectively. Connection weights $\omega_{13}$ , $\omega_{14}$ , $\omega_{23}$ and $\omega_{24}$ represent electronic messages delivered (output) to executives 1 and 2 respectively. Assume the output function $\theta_{i}=1$ if $\omega_{ji}\alpha_{i}\geqslant\frac{1}{4}$ or $\theta_{i}=0$ if $\omega_{ji}\alpha_{i}<\frac{1}{4}$ ; i.e. for period t, i.e. the “threshold” is $\frac{1}{4}$ . Assume the activation rule “deliver packet to executive j if $\alpha_{j}\geqslant1.00$ for that executive.” Let the distribution network be designed for perceptron learning, following the rule in equation (7), a reiteration of the perceptron learning rule in equation (5). Assume that an input electronic message either gets an index $\alpha_{i}=0.5$ or it does not, $\alpha_{i}=0$ where i=1,2. Assume that time period t describes the (asynchronous) receipt of a single electronic message. Let the learning rate parameter k=1. Then the connection matrix learns from executive responses as per equation (7).

$$
\begin{array}{l} \omega_ {i j} (t + 1) \\ = \omega_ {i j} (t) + \kappa [ \eta_ {i j} (t) - \alpha_ {i} (t) ] \theta_ {j} (\alpha_ {i} (t) \omega_ {i j} (t)). \end{array}\tag{7}
$$

Now assume that a packet with index 1 is delivered; $\alpha_{1}=0.5$ and $\alpha_{2}=0$ . This packet is delivered to the first executive ( $j=3$ ) with the corresponding executive “interest level” responses $\eta_{13}=0.75$ and $\eta_{23}=1$ (i.e., assume that the executive wants no change in his activation for index 2 if a packet with index 2 is not delivered) and is delivered to the second executive (j=4) with the corresponding executive responses $\eta_{14}=0.75$ and $\eta_{24}=1$ . Then $\Omega(t+1)$ becomes

$$
\Omega (t + 1) = \{\omega_ {i j} \} = \left[ \begin{array}{c c c c} 0 & 0 & 0. 7 5 & 0. 7 5 \\ 0 & 0 & 0. 5 & 0. 5 \\ 0. 5 & 0. 5 & 0 & 0 \\ 0. 5 & 0. 5 & 0 & 0 \end{array} \right].\tag{8}
$$

Thus the new connection matrix accentuates both executives' moderate interest in electronic messages with index type 1. This accentuation lowers their probability of suffering from "fugitive" type 1 information. Prior interest in type 1 information has been noted by the network, and thus is more likely to be given all of the type 1 information arriving, despite preferences at the current point in time. If instead, the type 1 connections had remained at 0.5, rather than "adapting" to 0.75, there would be a much higher probability that newly arrived information, that the executives might be interested in reviewing, would fail to be delivered - i.e. that information would remain "fugitive." This same feature fosters the serendipitous discovery of new information when there exists a clustering of relevant information around types of information that have been relevant in the past.

Note that since $\kappa=1$ , the matrix is overly sensitive to new information; $\kappa$ will generally need to be tuned to reflect the sensitivity desired of the distribution system. Simulations and prototypes are useful in determining both the initial values for the connection matrix, and the sensitivity parameter $\kappa$ . Values in the lower left hand corner of the matrix $\omega_{31}$ , $\omega_{32}$ , $\omega_{41}$ and $\omega_{42}$ do not change, because feedback is only received from the executives, not from the indexers; their initial settings do effect the sensitivity of the learning through the activation rule $\theta_{i}$ .

Now assume that a packet with both indices (a composite descriptor) arrives at the network; i.e. $\alpha_{1}=0.5$ and $\alpha_{2}=0.5$ and $\theta_{3}=1$ since $\omega_{i3}\alpha_{i}\geqslant\frac{1}{4}$ and $\theta_{4}=1$ since $\omega_{i4}\alpha_{i}\geqslant\frac{1}{4}$ for both executives, i=1, 2. Then output activation (assuming linear activation rule $\alpha=\Omega\theta$ ) is $\alpha_{3}=0.75+0.5\geqslant1.00$ for the first executive, and thus the packet is delivered; the output activation is $\alpha_{4}=0.75+0.5\geqslant1.00$ for the second executive, and thus the packet is delivered to the second executive also. Let this second packet receive executive responses $\eta_{13}=0.75$ and $\eta_{23}=0.75$ from the first executive and executive responses $\eta_{14}=0.75$ and $\eta_{24}=0.75$ from the second executive. Then $\Omega(t+2)$ becomes

$$
\Omega (t + 2) = \left\{\omega_ {i j} \right\} = \left[ \begin{array}{c c c c} 0 & 0 & 1. 0 & 1. 0 \\ 0 & 0 & 0. 7 5 & 0. 7 5 \\ 0. 5 & 0. 5 & 0 & 0 \\ 0. 5 & 0. 5 & 0 & 0 \end{array} \right].\tag{9}
$$

Next assume that a packet with both indices is delivered; i.e. $\alpha_{1}=0.5$ and $\alpha_{2}=0.5$ and $\theta_{3}=1$ since $\omega_{i3}\alpha_{i}\geqslant\frac{1}{4}$ and $\theta_{4}=1$ since $\omega_{i4}\alpha_{i}\geqslant\frac{1}{4}$ for both executives, i=1,2. Then output activation is $\alpha_{3}=1.0+0.75\geqslant1.00$ for the first executive, and thus the packet is delivered; the output activation is $\alpha_{4}=1.0+0.75\geqslant1.00$ for the second executive, and thus the packet is delivered to the second executive also.

This third packet is delivered to the first executive and receives “lukewarm” executive responses $\eta_{13}=0.50$ and $\eta_{23}=0.50$ and from the second executive, responses $\eta_{14}=0.50$ and $\eta_{24}=-0.20$ , i.e. the second executive decides that he is now uninterested in packets with index 2, and receives disutility from consuming them. Then $\Omega(t+3)$ becomes

$$
\Omega (t + 3) = \left\{\omega_ {i j} \right\} = \left[ \begin{array}{c c c c} 0 & 0 & 1. 0 & 1. 0 \\ 0 & 0 & 0. 7 5 & 0. 0 5 \\ 0. 5 & 0. 5 & 0 & 0 \\ 0. 5 & 0. 5 & 0 & 0 \end{array} \right].\tag{10}
$$

Next assume that a packet with both indices is delivered; i.e. $\alpha_{1}=0.5$ and $\alpha_{2}=0.5$ . Now $\theta_{3}=1$ since $\omega_{i3}\alpha_{i}\geqslant\frac{1}{4}$ ; but $\theta_{4}=1$ for the first executive, since $\omega_{23}\alpha_{2}\geqslant\frac{1}{4}$ , and $\theta_{2}=0$ for the second executive, since $\omega_{24}\alpha_{2}<\frac{1}{4}$ . Output activation is now $\alpha_{3}=1.0+0.75\geqslant1.00$ for the first executive, and thus the packet is delivered; the output activation is $\alpha_{4}=0.75+0.05<1.00$ for the second executive, and thus the packet is not delivered to the second executive.

The proof of perception convergence theorem [29] assures that this will converge to a stable equilibrium that reflects end-user's information needs. Simulation studies on neural networks have shown that the convergence is quick and thus useful in responding to turbulent environments.

The tunability of the system via $\kappa$ assures that adjustment will not be overly sensitive.

## 7. Discussion and Conclusion

The previous discussion has presented an approach to computer support that is central to some of the more important activities of an executive – the modulation of information dissemination. A neural network inspired approach was presented that incorporates a system for responding to organizational changes in responsibilities and information flows as an integral part of the information dissemination process. The approach is practical; the success of the information dissemination approach defined in this paper has been shown via the extensive research performed in neural network based computer systems and in studies of biological systems. The mathematics of neural networks are well defined, and thus the cost and performance of self-organized executive information networks should be easy to ascertain.

The benefits of self-organizing executive information networks are several. Executive overload due to irrelevant information may be better controlled when dissemination is determined by non-user groups such as indexers and authors. Existing executive information systems are generally conceived as online systems that disseminate information by query or by predefined profile. In these cases, the dissemination algorithms can be implemented automatically. As corporations move toward more information dissemination by query or by user profile, the usefulness of automatic, real-time control of dissemination becomes more attractive. Executive information requirement profiles may evolve as information is disseminated throughout the system. Self-organizing ESS should actually be much less expensive to operate than a traditional mainframe based, periodic, paper-based reporting system, because the executives will tend not to be overloaded by useless information.

The system described here is practical and appropriate given the current direction of computer development. Over the past five years, over 50% of corporate computing has shifted to microcomputers, many of them being workstations on networks. In a managed network environment, where processing and databases are distributed, and where there exist computing resources specifically dedicated to network management and file serving, self-organizing executive information networks fit quite naturally into the requisite operating systems.

Incorrect learning is a potential short-term problem in neural networks, as is incorrect specification in systems design, or in the design of report dissemination. But self-organizing dissemination systems can correct themselves – they are adaptable and robust. The example demonstrates a specific way of implementing the network so that the executive must specify that a particular type of information is not desired before it is dropped from distribution. The executive could also periodically review the connection matrix (or some more readable form of it than is presented in the example) in order to determine if he thinks that the dissemination routes are misspecified or otherwise odd.

The systems for information dissemination presented here are conceived in terms of corporate needs. But there are potential applications and extensions of the current research in other areas. In particular, in the “invisible colleges” of researchers in science, the ability to effectively disseminate databases, working papers, ideas, notes and so forth holds the potential of significantly improving the efficiency of research. Similarly, in police monitoring and military intelligence, self-organizing executive information networks could improve coordination and effectiveness.

## References

[1] S-I Amari, 1983, Field Theory of Self-Organizing Neural Nets, IEEE Transactions on Systems, Man and Cybernetics SMC-13, no. 5, Sept./Oct.

[2] A.G. Barto and R.S. Sutton, 1981, Landmark Learning: An illustration of associative search, Biological Cybernetics 42, 1–8.

[3] D.C. Blair and M.E. Maron, 1985, An evaluation of retrieval effectiveness for a full-text document retrieval system, Communications of the ACM 28(3), 289–97.

[4] D.C. Blair, 1980, Searching Biases in Large, Interactive Document Retrieval Systems, Journal of the American Society for Information Science 31(4), 271–277.

[5] L.J. Bourgeois III and K.M. Eisenhardt, 1988, Strategic Decision Processes in High Velocity Environments: Four Cases in the Microcomputer Industry, Management Science 34(7).

[6] R. Carlyle, 1990, Is Your Data Ready for the Repository? Datamation, January 1.

[7] F. Crick and C. Asanuma, 1987, Certain Aspects of the Anatomy and Physiology of the Cerebral Cortex, in J.L. McClelland, D.E. Rumelhart and the PDP Research Group (1987) Parallel Distributed Processing, Cambridge: MIT Press.

[8] U. Eco, 1976, A Theory of Semiotics, Bloomington: Indiana University Press.

[9] K. Fukushima, 1975, Cognitron: A self-organizing neural network model for a mechanism of pattern recognition unaffected by shift in position, Biological Cybernetics 36, 193–202.

[10] S. Grossberg, 1976, Adaptive pattern classification and universal recoding: Part I. Parallel development and coding of neural feature detectors, Biological Cybernetics 23, 121–134.

[11] D.O. Hebb, 1949, The Organization of Behavior, New York: Wiley.

[12] J.H. Hester and D.S. Hirschberg, 1987, Self-Organizing Search Lists Using Probabilistic Back-Pointers, Communications of the ACM 30, no. 12, 1074–1079.

[13] Houdeshel, G. and H.J. Watson, 1987, The Management Information and Decision Support (MIDS) System at Lockheed-Georgia, MIS Quarterly 11, no. 1, 127–140.

[14] J. Hopfield, 1982, Neural networks and physical systems with emergent collective computational abilities, Proceedings of the National Academy of Sciences: USA 79, 2554–8.

[15] Huber, G.P., 1984, The Nature and Design of Post-Industrial Organizations, Management Science 30(8), 928–51.

[16] D.J. Isenberg, 1988, Managerial Thinking: An Inquiry Into How Senior Managers Think.

[17] Kotter, J.P., 1982, What Effective General Managers Really Do, Harvard Business Review, Nov.-Dec., 161.

[18] M. Minsky and S. Papert, 1988, Perceptrons (expanded edition) Cambridge: MIT Press.

[19] H. Mintzberg, 1976, Planning on the Left Side and Managing on the Right, Harvard Business Review, July-Aug., 49.

[20] H. Mintzberg, 1973, The Nature of Managerial Work, New York: Harper & Row.

[21] H. Mintzberg, 1980, Structure in 5's: A Synthesis of the Research on Organization Design, Management Science 26, no. 3, 322–341.

[22] H. Mintzberg, 1967, The Science of Strategy-Making, Sloan Management Review 8, no. 2, 71–81.

[23] D.R. Nash, 1977, Building EIS, A Utility for Decisions, Data Base 8, no. 3, 43–45.

[24] C.S. Peirce, 1955, Logic as Semiotic: The Theory of Signs, in Philosophical Writings of Peirce, Justus Buchler (ed) New York: Dover, p. 99.

[25] W.F. Pounds, 1969, The Process of Problem Finding, Sloan Management Review, 1–19.

[26] G.N. Reeke Jr. and G.M. Edelman, 1984, Selective Networks and Recognition Automata, Annals of the New York Academy of Sciences 426, 181–201.

[27] J.F. Rockart and D.W. DeLong, 1988, Executive Support Systems, New York: Dow Jones-Irwin.

[28] J.F. Rockart and M.E. Treacy, 1982. "The CEO Goes On-Line", Harvard Business Review, Jan.-Feb., 82.

[29] F. Rosenblatt, 1962, Principles of Neurodynamics, New York: Spartan.

[30] D.E. Rumelhart, G.E. Hinton and J.L. McClelland, 1987, A General Framework for Parallel Distributed Processing, in Parallel Distributed Processing, vol. 1, D.E. Rumelhart, J.L. McClelland, and the PDP Research Group (eds.), Cambridge: MIT.

[31] B.R. Schlender, 1989, How to Break the Software Logjam, Fortune, September 25, 1989, 100–112.

[32] E.B. Swanson, 1988, Information Systems Implementation, Homewood IL: Irwin.

[33] C. von der Malsburg, 1973, Self-organizing of orientation sensitive cells in the striate cortex, Kybernetic 14, 85–100.

[34] J.C. Westland, 1989a, A Net Benefits Approach to Measuring Retrieval Performance, Information Processing and Management 25(5), 579–581.

[35] J.C. Westland, 1990a, Scaling Up Output Volumes Predicted by Information Systems Prototypes, ACM Transactions on Database Systems, Sept., 15 (3), 341–358.

[36] J.C. Westland, 1990b, Economic Constraints in Hypertext. Journal of the American Society of Information Science, 42 (3), 178–184.

[37] J.C. Westland, 1990c, Topic Specific Monopolies in the Information Services Industry: Evidence from the DIALOG Group of Databases, The Information Society 6, 127–138.

[38] J.C. Westland, 1990d, Assessing the Economic Benefits of Information Systems Auditing, Information Systems Research 1(3), 309–324.

[39] J.C. Westland and M. Kochen, 1989, Parallel Renaissance in Neural Networks: A Bayesian Approach to Neural Learning, Behavioral and Brain Science 12, 1989, 121–179.

[40] “The Fastest Software-Only Neural Net,” Electronic Engineering Times, September 15, 1988, 53(2).

[41] “Building Neuro Computers,” Electronic Engineering Times, March 20, 1989, 12(2).
