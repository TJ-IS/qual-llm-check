---
otero_id: 21327
otero_key: "QC5Y355Q"
title: "Decision station: situating decision support systems"
authors: "Rustam Vahidov; Gregory E. Kersten"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00099-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision station: situating decision support systems

Rustam Vahidov\*, Gregory E. Kersten

Department of Decision Sciences and MIS, J. Molson School of Business, Concordia University, Montreal, Canada H3G 1M8

Received 29 May 2002; received in revised form 9 June 2003; accepted 20 June 2003 Available online 6 August 2003

## Abstract

Internet facilitates access to data, information, and knowledge sources, but at the same time, it threatens to cognitively overload the decision makers. This necessitates the development of effective decision support tools to properly inform the decision process. Internet technologies require new type of decision support that provides tighter integration and higher degree of direct interaction with the problem domain. The central argument of this work is that in dynamic and highly complex electronic environments decision support systems (DSSs) should be situated in the problem domain. A generic architecture, the set of capabilities for our vision of a situated DSS is proposed, and the architecture is illustrated with a DSS for investment management. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Decision support systems; Software agents; Situated DSS; Active DSS; DSS architecture

## 1. Introduction

During the past 30 years since the conception of decision support systems (DSSs), the business environment has changed in several ways. The most significant changes include:

 Globalization of economy and the growing complexity of economic relationships;

 Flattening of organizations and growing employee empowerment;

 Increasing need for fast response in the dynamic competitive environment;

 Explosion of information accessible through electronic networks;

 Emergence and growth of electronic commerce; and

 Better-informed and empowered customers [36].

These changes contribute toward higher degree of complexity of the environment and, subsequently the number and difficulty of problems faced by the decision makers. It appears, therefore, that the need for decision support tools should be, if anything, increasing [45]. Contrary to these expectations we are not witnessing an adequate heightening of interest reflected by the limited number of recent scholarly publications on the subject of DSSs.

With the growing interconnectedness of the business environment, the ‘‘problem-solving’’ characterization of DSSs needs to be expanded and integrated. The ‘‘isolated DSS’’ view hampers their usefulness for today’s decision makers and is incompatible with such new information technologies as enterprise resource planning, supply chain management, and customer relationship management. DSSs need to be seamlessly integrated to the firm’s information environment. They also need to empower users by providing them with relevant information, inform about the decision-making process, respond to the emerging situation, and be capable of influencing the environment in the desired direction.

The main purpose of this paper is to lay a foundation for a new generation of decision support systems, the situated DSSs, which we refer to as decision stations, and propose a model and architecture for these systems. We view such DSSs as being active and closely linked to their respective problem environments. Section 2 presents the theoretical background for the proposed architecture of a situated DSS. It mainly builds upon the active DSS paradigm and research in software agents. Section 3 discusses the changing role of modern decision support, introduces the new components of situated DSS, and argues in favor of software agents as means of building such components. The architecture of a decision station, its major components and their formal representation are discussed in Section 4. Types and examples of situated DSSs are discussed in Section 5. Section 6 presents an illustration of the proposed approach using investment DSS. Section 7 presents the conclusions and future work.

## 2. Theoretical background

Our framework for situated DSS stems primarily from the developments in two disciplines: decision support systems and software agents. In this section, we will briefly discuss the relevant aspects of these fields to properly introduce our vision. We will not elaborate much on the subject of classical models for DSSs as we assume the readers to be familiar with the major contributions to the field made in the 1970s and early 1980s. Instead, we will focus on more recent developments.

## 2.1. Recent developments

It has been stressed that the need for decision support in the age of the Internet and e-business is now becoming even more critical than ever [47,49]. However, while DSSs constitute as one of the most popular areas of research in information systems in the past, a closer look reveals that lately the interest in DSS appears to be declining [8]. This somewhat paradoxical observation calls for a closer analysis of requirements for decision support tools posed by the new dynamic environment.

From the very beginning, the focus of DSS research and development has been on generic problem-solving activities, for example, Expert Choice (http://www. expertchoice.com) and Decision Explorer (http:// www.banxia.com). The sphere where actual business operations or transactions took place was often seen as a secondary concern for the adoption and implementation of DSS. While criticism of the ‘‘stand-alone’’ DSS approach and the need for closely linking DSS with business work processes have been voiced [2], this theme has not yet resulted in the introduction of new concepts, frameworks, or architectures.

The requirement of the DSS connectedness to its environment builds upon the concept of an active DSS [1,23,40]. The advocates of active DSS point out the weakness of traditional support for being passive, where the user needs to have full knowledge of the system’s capabilities and must exercise initiative to perform decision-related tasks. An active DSS need not be capable of undertaking all the tasks on its own and completely without the user’s intervention. Ideally, an active DSS would establish a two-way interaction with both the user and the environment, and would be capable of maintaining those links if any of the entities is active. Such a system would allow for the integration of decision-making and decision implementation activities.

## 2.2. Insights from the software agent research

In the last decade, a broad category of software referred to as agents, or bots, has gained tremendous popularity. Although software agents defy precise definition, several characteristics are often cited; they are proactive, reactive, exhibit social ability, intelligence, and purpose [13]. One central theme in agentbased technologies is that agents are situated in their environment; they are capable of sensing the state of the environment (e.g., load in electrical power grids, presence of e-mail messages in one’s mailbox), and of affecting the state (e.g., switching power lines, sorting e-mail messages).

One definition states that ‘‘an agent is an encapsulated computer system that is situated in some environment and that is capable of flexible, autonomous action in that environment in order to meet its design objectives’’ [24]. The emphasis here is on the existence of direct links with the problem environment.

The difference between situating a system in the environment can be illustrated with the difference between closed and open systems in artificial intelligence (AI). The situated ‘‘view’’ in AI has been gaining popularity since the late 1980s [51]. The distinguishing characteristic of this perspective, as opposed to traditional ‘‘rationalistic’’ perspective, is the focus on the system interaction with its environment [31]. If systems are to have cognitive abilities, they need to be situated, because cognition cannot be abstracted away from the environment. The behavior of a system is the combined result of its purpose and its interaction with the environment [41].

An agent can be a vehicle capable of purposeful seeking and using information sources. It can, therefore, be used as an advanced sensor with encapsulated intelligence. Agents can gather information to promote user awareness [5] and support decision-making (e.g., use airline databases to support travel planning Ref. [39]). Agents embedded in a DSS can decide on information being monitored, gathered and filtered in geographically distributed environments [6]. A cognitive agent can be used to amplify human perception and cognition in critical environments [11]. In ebusiness, agents have been used to obtain information and undertake tasks on behalf of their principals [16,34,43]. Agents are also used to maintain databases of vendors [60], and assess their reputation [62].

## 3. The changing role of decision support

## 3.1. Situating DSSs

One result of the information revolution is a very high level of connectivity that pervades multiple aspects of managing and conducting business activities. In many aspects, the network is becoming the actual place for conducting business [42]. We have been recently observing an increasing integration of information systems in business environments. e-Business and enterprise resource planning systems are just a few examples of integration of previously disparate information systems. While they provide some DSS functionality, there is a need for the development of decision support tools, which can be tightly integrated with the business environment. In particular, the phenomenon of ‘‘ubiquitous network’’ needs to remain within the focus of DSS research.

Effective linking of DSSs to their problem environments would enable the improvement of strategic capabilities of organizations through timely response to the dynamically arising challenges and management of organizations ‘‘by wire,’’ that is, combining high level decision-making with automation and IS support of various business operations [17]. The terms ‘‘cockpit of the business’’ and ‘‘cyberspace cockpit’’ have been coined to signify the new requirements for computerbased support [36]. Furthermore, we are witnessing an increased interest in real-time, more responsive breed of DSSs [56]. On the consumer side, the predictions are made about the emergence of a ‘‘new breed of consumer. . .more selective, better informed, and with a range of powerful tools at his or her disposal’’ [36].

One possible reason behind the inherent constraint in expanding traditional DSS out of the detached problem realm and into the dynamic environment comprising all business interactions has been the wide adoption of Simon’s ‘‘intelligence–design –choice’’ problem solving model. Although Simon later extended the model with monitoring, DSS research remained primarily focused on the three-phase model. Other suggestions to use alternative models that incorporate implementation and monitoring were proposed but not accepted in the mainstream of decision support research and development [4,48].

The difficulty in the design and implementation of active and connected DSSs was caused by the lack of connectivity among different information systems in an organization and between these systems and the organization’s environment. The ubiquitous network and pervasive computing demand new approaches that will allow a DSS to become a part of the information infrastructure, through interaction with its environment, and leveraging its cognitive capabilities through its connectedness to the decision problem’s environment. This would provide a DSS with means to sense the problem environment, offer decision support to a decision maker and act upon the environment to adequately respond to his/her needs that may undergo changes and refinement during the process. In other words, these systems will be the situated decision support systems.

The above discussion stresses recent trends toward the adoption of the connected and situated concepts. The relationships between AI, agents, and decision support systems are presented in Table 1. Within AI, expert systems have been proposed as means of mimicking expert decision-making. Situating these systems in the problem environments led to the development of intelligent agents. Situating DSSs within problem environments, providing them with capabilities to seek and sense the relevant data, and giving them the ability to change the environment can bring about the type of support that today’s organizations need.

The goal of a situated, connected, and active DSS is to provide all services necessary for decisionmaking and implementation. To reflect the comprehensive nature of such a system and also its integration with other systems and with the environment we call it a decision station (DS). A DS is used to perform the following: (1) sense what is going on in the problem domain; (2) utilize traditional DSS facilities to inform decisions; (3) make choices; and (4) undertake implementation and monitoring activities.

## 3.2. Active and passive components

The key components for situating DSSs are sensors and effectors. In Table 2, two types of these components, as well as their capabilities and functions, are presented. The examination of the basic capabilities of sensors and effectors reveals the fact that some of them are more ‘‘advanced’’ than the others. For example, the ability to search for new information sources (more generally, adaptive capability) is more advanced than simple connecting capability. This insight leads to a dichotomous distinction between the ‘‘active’’ and ‘‘passive’’ capabilities of sensors and effectors.

Table 1  
Comparison of DSS, expert systems, and intelligent agents

<table><tr><td></td><td>Decision support</td><td>Artificial intelligence</td></tr><tr><td rowspan="2">Traditional Situated</td><td>DSS</td><td>Expert systems</td></tr><tr><td>Situated DSS</td><td>Intelligent agents</td></tr></table>

Table 2  
Active vs. passive capabilities of sensors and effectors

<table><tr><td colspan="2">Sensors</td><td colspan="2">Effectors</td></tr><tr><td>Capabilities</td><td>Supported functions</td><td>Capabilities</td><td>Supported functions</td></tr><tr><td>Passive</td><td></td><td></td><td></td></tr><tr><td>Connecting</td><td>Importing data</td><td>Connecting</td><td>Exporting data, carrying out actions</td></tr><tr><td>Transforming</td><td>Filtering, pre-processing, noise reduction, etc.</td><td>Transforming</td><td>Converting decisions into actions</td></tr><tr><td>Alerting</td><td>Drawing user&#x27;s attention, signaling to effectors</td><td>Querying</td><td>Requesting information or authorization from user or sensors</td></tr><tr><td>Active</td><td></td><td></td><td></td></tr><tr><td>Adapting</td><td>Search for new sources, attuning transformational and alert generation logic</td><td>Adapting</td><td>Identifying alternative destinations, Adjusting transformation and alerting logic, bidding tactics, etc.</td></tr><tr><td>Planning</td><td>Determining order of actions, scheduling sensory (monitoring), and adapting actions</td><td>Planning</td><td>Determining order and scheduling of actions</td></tr></table>

Sensors have five capabilities that support their main functions. Some capabilities affect others, for example, the adapting capability can modify the connecting capability in order to reflect the identification of new information sources. The division of the basic capabilities into two categories is not completely ‘‘clear-cut’’ and is primarily determined by our perception of the level of the proactive nature present in the capabilities. To further clarify the distinction between the active and passive situating components, let us consider an example of a DSS for supply chain management.

With the growth of B2B commerce, the supply chains are expected to be more dynamic [9,38]. Assume that decisions need to be made regarding which parts to purchase from which suppliers. Consider first the case with passive components. The (passive) sensors would be able to collect the prices and other relevant information on parts from the existing vendors by consulting their databases. The decision maker could use this information to run optimization models in DSS kernel and perform sensitivity analysis in order to come up with the desired decision. The decisional output then will be given to (passive) effectors that would inject necessary information into the order forms and submit the orders to the respective vendors (e.g., through the Web, e-mail, fax).

Consider now the case with active DSS components. The sensors could monitor the prices by the vendors on a regular basis and notify about any changes in price for the timely response (a similar scenario has been described as an application of agent technologies to DSS in Ref. [19]). Moreover, the sensors would be able to look for and identify new potential vendors through consulting Yellow Pages, auctions, or crawling the Web. The sensors could also consult the auctions to see in what range the prices for the parts are. The monitor in DSS kernel could decide whether to invoke DSS functions depending on the state of the environment. The user would make a decision using the tools of DSS, possibly including ranges instead of crisp values and pass the results to the effectors. It is possible that the effectors would be able to conduct automated bidding in an auction in order to make the best deal. Upon winning the bid, they would finalize the transaction and monitor the delivery of the parts by consulting other organizational IS.

## 3.3. Agents as decision station building blocks

As we have mentioned earlier, the DSS research has stressed the importance of active and high cognitive level DSS. In this paper, we argue for a situated DSS. Ideally, a new type of DSS would be fully situated, active, and with advanced capabilities. These characteristics point toward employing agent technologies for building such systems. It is not surprising that most of the work reviewed by us relies on agent technologies, since agents have the characteristics that fit our purposes quite well. Let us review some of the important agent characteristics in light of the components of a DS.

Situatedness is the feature that helps sensors and effectors link to the respective problem environments.

The target environment could be either virtual or physical one, or it could span across both. Autonomy and proactiveness are necessary for allowing the components of a system to take initiative and execute various related tasks in an automated fashion. Intelligence may be required for performing high-level cognitive tasks, e.g., negotiations. Social ability allows the situated DSS to communicate with other systems as well as the user; and reactivity enables monitoring of the environment, or the user to signal and handle significant problem-related events.

Recent articles on the future directions of DSS research have stressed the importance of using agent technologies in DSS [7,46]. Use of agents for building active DSS has been discussed earlier. Ref. [1] proposed a vision where a decision maker is supported by a team of stimulus agents forming a virtual teamwork. Ref. [19] presented a generic architecture with DSS components (models, data, dialogue) being managed by agents. Furthermore, use of recommendation agents as the basis for DSS was proposed in Ref. [49], and use of critiquing agents within DSS was discussed in Ref. [59].

An interesting model of an agent-based distributed DSS that comes close to our notion of a decision station is given in Ref. [20]. Here, the three DSSs encapsulated in raw materials, production, and finished goods inventory agents have been described. The agents automate much of the work, enjoying limited authority in performing minor and routine tasks. They also collaborate with the decision makers when necessary. The agents obtain all necessary information from electronic sources, and their decisions are implemented electronically as well (i.e., submitting an order, communicating the results of a decision, etc.). Hence, the systems are both active and situated.

A closely related research direction focused on the supply chain management [28]. The authors discuss their work at IBM Research on ‘‘sensing and responding enterprise’’ model. Coming from Operations Research perspective, the group proposed the use of additional ‘‘sensing and responding’’ layer sandwiched between the supply chain planning and supply chain execution layers in order to deal with emerging problems and opportunities. The sensing-and-responding capability was carried out by intelligent agents. This work strengthens our belief in the appropriateness of the notion of situated decision support.

## 4. Decision station

In this section, we present the generic architecture of a DS followed by detailed capabilities and functions of its five components. In Section 5, we discuss several examples of DS functionalities in selected domains. An example of a DS is given in Section 6.

## 4.1. Generic architecture

Situating the DSS necessitates the addition of at least two key capabilities: (i) the capability to access the state of affairs, and (ii) the capability to change the state of affairs. The former is achieved with sensors and the latter with effectors. Sensors, effectors (together with the kernel), and active user interface comprise the generic DS illustrated in Fig. 1.

The kernel is composed of the DSS facilities in a traditional sense (i.e., database, models, and knowledge base) relevant to a problem domain. It includes an active component: the DSS manager. The inclusion of the manager reflects the view that the situated DSS needs to be active, irrespective of the presence of the user and capable of performing certain tasks autonomously—for example, contacting the user, preparing the system for interaction prior to the user’s request, and even making decisions when the user cannot be contacted.

The manager requires a knowledge base containing, among others, business rules, in order to be capable of performing some of the tasks autonomously. Since our primary focus in this paper is the links of a DS with the problem environment, a detailed description of functionality of the manager is not discussed here.

Sensors capture the data relevant to the problem domain from a variety of sources. The sensors, however, should not be thought of only as mere means of capturing the data. They may incorporate more advanced functions as well, i.e., search for relevant sources, filtering and pre-processing of data, alerting generation, and other useful features.

Effectors are the devices used by a decision station to send signals to the problem environment with the purpose of directly altering current state of affairs. Similarly to the sensors, the effectors are not necessarily simple vehicles of decision execution or communication, but may engage in different activities required to implement a decision (e.g., converting the decision into more detailed plans, optimizing the well structured aspects of a decision, determining sequence of actions, monitoring execution of a decision, and conducting negotiation in the course of implementing a decision). Note that the separation of sensors and effectors here is prompted by the distinct roles they play in carrying out the interactions with the problem domain. Implementation-wise, these parts can be integrated into a single module.

![](/api/attachments/QC5Y355Q/fulltext/images/756599d22cb0d6b6f6d0adee98afa174979f8e4ee27b9a85f48dad88487f175c.jpg)  
Fig. 1. Generic architecture for a decision station.

Active user interface has been included to signify new ideas and developments in facilitating human– machine dialogues. Such interfaces may incorporate synthetic characters, reside on wearable devices, and have learning capabilities. The functionalities of decision station components are discussed below.

The structure of the decision station can be described as:

$$
D S = \{S, E, N, K N \},\tag{1}
$$

where S denotes the sensors, E represents the effectors, N is the user interface, and KN indicates the DSS kernel. In the following sections, each of these constructs is described in more detail.

In Fig. 1, the information exchanged between the DS components and the user is indicated with D. X denotes the information obtained from, and Z represents information passed to the environment. Y denotes the information flow between the DS components. In the following sections, the component type is not indicated in its local inputs and outputs, unless it is necessary to avoid ambiguity.

## 4.2. DSS sensors: assessing the state of affairs

Delivering new and relevant information is an important task in all phases of decision-making, particularly in the intelligence and monitoring phases. In a DS, this task is performed by means of sensors, which are various tools used to access problem domain and assess its state of affairs. In a trivial case, the sensors import relevant information into DSS from the environment. More advanced sensors require capabilities for locating, filtering and transforming relevant information, and generating alerts. With the explosion of the information available in electronic form on the Internet, the task of finding the right sources, filtering useful information, and presenting it in a suitable way to the decision maker has become of critical importance. Hence, it is not surprising to see the growth of smarter, more advanced tools used for these functions.

The sources of information can vary. These could be embedded in physical environments, various databases, or the Internet [12,21,44]. Depending on the definition of problem domain, the DS sensors should have the means to access a variety of sources.

We propose the following set of sensor functions: accessing, filtering, conversion, and monitoring of information and generating alerts, should a critical situation arise. More advanced features, including identification of new sources of information (e.g., through interacting with search engines, or crawling the web), and fine-tuning of some of the sensing functions (e.g., adjusting thresholds that trigger alert generation) could also be provided. This leads to the following model of a generic sensor:

$$
S = \{C, G, K, R, O \},\tag{2}
$$

where C is the set of sensor capabilities, G is the set of goals, K is the knowledge base of the sensor that can schedule and direct its use of capabilities, R denotes the requests received from other parts of the system, and O denotes the operations that a sensor performs; the concrete utilization of a single capability at some point in time. Henceforth, it will be assumed that the ‘‘null’’ action—that is, ‘‘do nothing’’—is also a valid operation.

The sensor ‘‘reads’’ the state of the environment x (x<sup>a</sup> X ) and transforms it to outputs $y \left( y { \in } Y \right)$ , that is, S: X ! Y. The inputs and outputs are those of a sensor, not of the entire DS.

The five capabilities of sensor C considered here are:

$$
C = \{\text { plan }, \text { conn }, \text { trans }, \text { alert }, \text { adapt } \}.\tag{3}
$$

The key capability of an advanced sensor is the planning capability, plan, which decides on the order and time in which the other capabilities are invoked, which sources of information are sought and used, and how the sensor’s outputs are directed. For example, depending on the volatility of the market, the sensor may decide to monitor the developments with more or less frequency. In a degenerate (trivial) case, the planning capability is reduced to executing pre-specified fixed operations, such as reading certain piece of information at regular fixed intervals. This capability utilizes the sensor’s knowledge base K. In order to enable planning capability, the sensor should exhibit a goal-oriented behavior. Therefore, representation of goals is necessary.

$$
o _ {t, T} = \operatorname{plan} \left(K _ {t}, x _ {t}, g _ {t}, c _ {t}\right), \left(o _ {t, T} \in O, g _ {t} \in G, y _ {t} \in Y, c \in C\right).
$$

where $c$ is a capability defined by Eq. (3), $o _ { t , T }$ is the sequence of operations at time $t \left( 0 \leq t < T \right)$ for the next T periods (T is the planning horizon):

$$
o _ {t, T} = \left[ o _ {t + 1}, o _ {t + 2}, \dots , o _ {t + T} \right],\tag{4}
$$

and $x _ { t } , \ g _ { t }$ and $c _ { t }$ are the inputs, goals and capabilities of a sensor, respectively, at time t.

Below, we discuss the capabilities possessed by DS components in a generic form; their concrete implementations depend on the problem domain. In Section 6, we provide examples from the investment domain.

Let us assume that the environment is described by a vector $\mathbf { { \boldsymbol { x } } } \in X .$ . The connect capability conn of S allows direct access to the sources and information passing to other parts of the system without any modification, that is:

$$
\text { conn }: y = x, (\boldsymbol {x} \in X, y \in Y).
$$

In general, $Y \subset X$ because the sensor selects and passes only some environment descriptors. Information filtering, conversion, noise reduction, and other preprocessing done by the sensor is due to its transformational capability trans:

$$
y = \operatorname{trans} (x), (\boldsymbol {x} \in X, y \in Y).
$$

Note that, in this case, the number of outputs (average ranking) could be different from the number of inputs (individual rankings). The capability to generate signals that require immediate users’ attention or actions of the other parts of the system is alert.

$$
y _ {\mathrm{a}} = \operatorname{alert} (x), (\boldsymbol {x} \in X, y _ {\mathrm{a}} \in Y _ {\mathrm{a}}),
$$

where $Y _ { \mathrm { a } } , ( Y _ { \mathrm { a } } \subset Y ) _ { \cdot }$ , is a set of alert messages.

Although alert is a specialized capability of trans, it is separated here because of its impact on other parts of the system. While conn and trans produce output that is used when needed, alert’s outputs are used when they are produced. The sensor communicates directly with the user interface to alert the user, with the DSS kernel, or with the effectors (see Fig. 1). The decision regarding the invocation of the alert capability and components to which the alerting signal should be directed can be done by the plan capability.

The capability of a sensor to seek different information and to modify its own capabilities is called adapt. For example, we already mentioned a possibility of tuning a threshold for alert generation. Another example includes changing the conn capability by identifying and connecting to new sources of information. In general, the adapt capability modifies the capabilities of the sensor at time t based on s previous periods described by input –output –capability triplets:

$$
\begin{array}{l} C _ {t} = \text { adapt } \{(x _ {t - \tau}, y _ {t - \tau}, C _ {t - \tau}), \dots , (x _ {t - 1}, y _ {t - 1}, C _ {t - 1}) \}, \\ (1 <   \tau \leq T). \end{array} \tag {5}
$$

The information-gathering capabilities of a sensor could be invoked on a regular basis or in reply to the requests R from other parts of the system.

Fig. 2 illustrates the sensor’s capabilities and information flow between the environment and other DS components. To simplify the figure, we did not include the capability adapt, which affects all other capabilities and components. Information about its past states, which is used by the capabilities plan and adapt, is stored in its database (memory).

## 4.3. Effectors: changing the state of environment

The focus on the intelligence – design–choice trinity in DSS research largely led to the oversight of the implementation phase. With diminishing requirement of ‘‘switching media’’ when moving from decisionmaking to decision implementation, systems should enable the implementation as well as the monitoring of the results of decisions [36]. For example, an investor should be able to view the financial indicators, news and performance of his/her portfolio; obtain decision support in building/improving the portfolio; make buy/ sell decisions; and subsequently implement those decisions through an online system. Moreover, since 98% of the computing power is embedded in different types of devices facilitating proactive computing with humans placed ‘‘out and above the loop’’ [54], the effectors can also reach beyond the virtual world and into the physical one.

![](/api/attachments/QC5Y355Q/fulltext/images/64edab7047732c33bd9c41658eb0b76a04ba0d525700ea3d991d9a6bd320f16f.jpg)  
Fig. 2. Architecture of a sensor.

Implementation primarily involves carrying out the decisions, but it may also entail planning and optimization activities, monitoring of execution, as well as reviewing and negotiating changes, if necessary. Conduct of these activities requires that the effectors have advanced capabilities. For example, an effector with the optimization capabilities [10] may finalize the details; find the best way of carrying out actions; and overview the execution of decisions. Another possibility is to delegate the authority and capability to conduct automated negotiations within a certain range of criteria to the effectors as part of the decision implementation process. For example, production decisions may require purchase of items from suppliers with whom effectors could negotiate the purchase terms [38].

In general, effectors can be described as:

$$
E = \{C, K, G, O \},
$$

where C is the set of capabilities, K is the knowledge base of the effector that schedules and directs its use of capabilities, G denotes the goals of the effector, and O is the set of operations that effector performs. We have included the following set of effector capabilities:

$$
C = \{p l a n, c o n n, t r a n s, q u e r y, a d a p t \},
$$

As in the case with sensors, the key capability of an effector is planning and it is used to establish the order in which other capabilities are invoked in order to achieve a given goal $g \colon$

$$
o _ {t, T} = \operatorname{plan} \left(K, y _ {t}, g _ {t}, c _ {t}\right), \left(g _ {t} \in G, y _ {t} \in Y _ {\mathrm{DS}}, c _ {t} \in C\right),\tag{6}
$$

where the sequence of operations for the next T periods of time $o _ { t , T }$ is defined in Eq. (4), and $y _ { t } , g _ { t } ,$ and c<sub>t</sub> are the inputs, goals and capabilities, respectively, of a sensor at time t. $Y _ { \mathrm { D S } }$ denotes the set of the inputs from other components of DS.

The connecting capability is the ability to directly export or write the values of decision variables from a sensor or the DSS into some action variable that attempts to change the state of affairs. If we let Z represent the effector’s outputs directed to the environment, we have:

$$
\text { conn: } \quad z = y _ {\mathrm{DS}}, (z \in Z, y _ {\mathrm{DS}} \in Y _ {\mathrm{DS}}).
$$

The output vector z contains actions, e.g., the sensor sends orders to an online store.

The transformational capability requires the formulation of action $z ~ \left( z { \in } Z \right)$ in order to implement a decision generated by the DSS or a request sent from a sensor or the user (via active UI), e.g., informing prospective vendors about a request for proposals, or executing transaction:

$$
z = \operatorname{trans} (y), (z \in Z, y \in Y).
$$

The effector may also need additional information in order to implement the decision. Its output Y that is directed to other components includes querying in order to obtain additional information necessary to undertake an action:

$$
y _ {q} = \operatorname{query} \left(y _ {\mathrm{DS}}\right), \left(y _ {q} \in Y _ {\mathrm{E}}, y _ {\mathrm{DS}} \in Y _ {\mathrm{DS}}, Y _ {\mathrm{E}} \cup Y _ {\mathrm{DS}} \subset Y\right),
$$

The capability of an effector to change its own capabilities allows it to adapt over time, similar to the sensors in Eq. (4). Effectors also use their past actions—that is, they take into account previous periods described by input –output–capability–action:

$$
\begin{array}{c} C _ {t} = \text { adapt } \{(z _ {t - \tau}, y _ {t - \tau}, C _ {t - \tau}), \ldots , (z _ {t - 1}, y _ {t - 1}, C _ {t - 1}) \}, \\ (1 <   \tau \leq T). \end{array}
$$

In addition to the above capabilities, the effector may also have some capabilities of the sensor. Perhaps, the two most useful capabilities are: (1) the interactivity capability (inter) to respond to the environmental changes in an autonomous manner; and (2) the capability to generate alert signals (alert).

Fig. 3 illustrates the effector’s actions directed to the environment, capabilities and information flow between the effector and other DS components. To simplify the figure we did not include the capability adapt, which affects all other capabilities and components. The information about its past states, which is used by the capabilities plan and adapt, is stored in its database (memory).

## 4.4. Active interfaces: toward advanced collaboration

An idealistic vision for the DSS to establish synergy between people and machines had not come to fruition in the past. Because decision makers can easily be overwhelmed with the amount of information and multitude of modeling tools available through their computers, the task of designing an effective and easy-to-use user interface is as important as ever.

With the growth of the Web, one can expect more user interfaces having web browser-like characteristics that are well known and easy to use. However, while basing user interface on WWW promotes the standardization and familiarity level of users and places minimal requirements on their geographical location, a higher level of human –machine collaboration can be achieved by promoting more active interfaces. Such mixed-type interfaces could help alleviate information overload by combining direct manipulation with the automation [22]. It is predicted that: ‘‘Future human – computer interface will be rooted in delegation, not the vernacular or direct manipulation’’ [37]. These interfaces populated with personal digital assistants and virtual secretaries will be able to perform certain tasks, including scheduling, filtering information, learning user preferences, and many others in an (semi-) autonomous fashion [3,22,33].

![](/api/attachments/QC5Y355Q/fulltext/images/ed6a87d0da2a30a8109e3cadfbd6fe7d9fa66b2c1c33154613ef7ffaf7501074.jpg)  
Fig. 3. Architecture of an effector.

To advance the use of visual channels and psychologically comfort the user, new directions in the design of virtual beings can be employed [26]. In Ref. [14], the use of animation in DSS user interfaces is presented. Empirical studies suggest that people prefer more natural-like personae [35]. There is some research in the direction of designing characters with advanced psychological dialogue skills [55]. Opponents of this notion, however, warn about the possible negative legal consequences of employing such devices, particularly in e-business transactions [18]. Other more exotic directions include the virtual work environment featuring room elements and furniture [50]. In general, it is reasonable to expect a higher degree of human –machine integration through the use of such devices as wearable computers [61].

To set apart these new developments from the traditional notion of port-like user interfaces, we use the term ‘‘active interface.’’ We describe the active interfaces as follows:

$$
N = \{C, V, K, G, O \},
$$

where C is the set of capabilities of the interface, V is the set of user characteristics, (user profile), K is the knowledge base of the interface, G denotes the goals that the interface may have (e.g., the maintenance of the accurate user profile), and O is the set of operations the interface performs.

The set of capabilities, in general, includes:

$$
C = \{\text { conn }, \text { trans }, \text { alert }, \text { query }, \text { adapt }, \text { plan }, \text { profile } \},
$$

The active interface N is an intermediary between the user and the system. Therefore, its communication is two-way and it is convenient to think of separate ‘‘languages’’ used to communicate with the system and with the user. As indicated in Fig. 1, Y denotes messages used to communicate with other DS components, and D denotes dialogue elements used in communication with the user. As before, $Y _ { \mathrm { D S } }$ denotes the set of inputs to the interface from other components; $Y _ { N }$ is the set of N outputs to the components. Further, $D _ { \mathrm { U } }$ is the set of user’s inputs, $D _ { N }$ is the set of outputs to the user, and $D = D _ { \mathrm { U } } \cup D _ { N }$

The capability to connect the user with the system means N passes information received from other components to the user, that is:

$$
c o n n \colon y = d, (y \in Y _ {\mathrm{DS}}, d \in D _ {N}),
$$

$$
\text { conn: } d = y, (y \in Y _ {N}, d \in D _ {\mathrm{U}}).
$$

Interaction with the user may require transformation of inputs and undertaking actions that allow the inputs to be represented in a rich and easy to understand context. This may involve relating the activities of sensors, effectors, and the DSS in a historical perspective, and their comparison with information obtained (via the sensors) from other systems. The transformation capability can be broken into a pair of capabilities used to transform (translate) messages from the user to the system and back to the user:

$$
\begin{array}{l} y = \text { trans } (d), (y \in Y _ {N}, d \in D _ {\mathrm{U}}), \\ d = \text { trans } (y), (y \in Y _ {\mathrm{DS}}, d \in D _ {N}). \end{array}
$$

The interface may need additional information from other DS components and from the user. Its output directed to other components includes querying for additional information necessary in order for N to formulate output directed to the user:

$$
y = \operatorname{query} (d, y ^ {\prime}), (y \in Y _ {N}, y ^ {\prime} \in Y _ {\mathrm{DS}}, d \in D _ {\mathrm{U}}).
$$

Similarly, interface N queries the user when it receives ambiguous input or requires clarification to formulate requests directed to other DS components:

$$
d = q u e r y (d ^ {\prime}, y), (y \in Y _ {\mathrm{DS}}, d \in D _ {N}, d ^ {\prime} \in D _ {\mathrm{U}}),
$$

The term alert denotes the capability to generate alert signals directed to the user. If something goes wrong with the implementation (e.g., product was not delivered), these signals can be used to prompt an immediate action and to draw user’s attention:

$$
d _ {\mathrm{a}} = \operatorname{alert} (y), \left(y \in Y _ {\mathrm{DS}}, d _ {\mathrm{a}} \in D _ {\mathrm{a}}, D _ {\mathrm{a}} \subset D _ {N}\right).
$$

Adapting capability allows the interface to change its own capabilities, e.g., to alter the mode of dialogue:

$$
\begin{array}{c} C _ {t} = \text { adapt } \{(y _ {t - \tau}, d _ {t - \tau}, C _ {t - \tau}), \ldots , (y _ {t - 1}, d _ {t - 1}, C _ {t - 1}) \}, \\ (1 <   \tau \leq T, y \in Y _ {\mathrm{DS}}, d \in D _ {N}) \end{array}
$$

Planning is the capability of the interface to act and interact with a purpose. It allows the user to determine the order in which the other capabilities are invoked in order to achieve a given goal:

$$
o _ {t, T} = \operatorname{plan} (K, y, d, g _ {t}, c _ {t}), \left(g _ {t} \in G, y \in Y _ {\mathrm{DS}}, d \in D _ {\mathrm{U}}, c _ {t} \in C\right),
$$

where the sequence of operations for the next T periods of time $o _ { t , T }$ is defined by Eq. (3).

The elicitation of user profiles from the dialogues with the user is done with profiling capability:

$$
\begin{array}{c} v _ {t} = \text { profile } ((d _ {t - \tau} ^ {\prime}, d _ {t - \tau}), \ldots , (d _ {t - 1} ^ {\prime}, d _ {t - 1})), \\ (1 <   \tau \leq T, v \subseteq V, d ^ {\prime} \in D _ {N}, d \in D _ {\mathrm{U}}). \end{array}
$$

The profile is updated using information on past interactions with the user. For example, from past dialogues, the interface may infer that the user is a risk-taker. We are assuming that the user profile is implicitly present in all of the above formulas, expressing different capabilities except for the basic connecting capability. We have not explicitly included it to reduce the complexity of expressions.

## 4.5. DSS kernel

A number of representations for describing functionality of DSS kernel (i.e., traditional DSS) appeared in the past [48]. Since our primary interest here is in the relationship of DSS to its situating components, we will focus on these interactions. We describe DSS kernel as:

$$
K N = \{C, G, K \},
$$

where C is the set of capabilities of a DSS, G is the goals of a kernel, and K is the knowledge base that directs the use of it’s capabilities.

The DSS has the following capabilities:

$$
C = \{\text { query }, \text { generate }, \text { suggest }, \text { adapt }, \text { plan } \}.
$$

The term query is the capability to produce results upon input, which the DSS kernel obtains from other components, e.g., data retrieval, solution of linear programming model. The DSS may need additional information from other DS components in order to respond to the query:

$$
y = \operatorname{query} (y ^ {\prime}), (y \in Y _ {\mathrm{K}}, y ^ {\prime} \in Y _ {\mathrm{DS}}).
$$

Here, $Y _ { \mathrm { K } }$ denotes DSS kernel outputs to other components.

The term generate denotes the capability to generate, based on output from other components $( Y _ { \mathrm { D S } } )$ 2 decisional outputs directed to effectors (E):

$$
y = \operatorname{generate} (y ^ {\prime}), (y \in Y _ {\mathrm{E}}, y ^ {\prime} \in Y _ {\mathrm{DS}}),
$$

where $Y _ { \mathrm { E } }$ is the set of outputs directed to effectors. This capability also allows the DSS kernel to make autonomous decisions and react to inputs to the kernel within the pre-specified limits of its authority. It uses information obtained from sensors to generate actions to be implemented by effectors:

$$
y = \operatorname{generate} \left(y ^ {\prime}\right), \left(y \in Y _ {\mathrm{E}}, y ^ {\prime} \in Y _ {\mathrm{S}}\right),
$$

where $Y _ { \mathrm { { S } } }$ is the set of inputs from sensors.

The term suggest denotes the capability of DSS to proactively generate suggestions $y , ( y { \in } Y _ { \mathrm { K } } )$ directed to the user through the interface N, based on the current inputs from other components (Y ), goals (G ), and user profile (V):

$$
y = \operatorname{suggest} \left(y ^ {\prime}, g, v\right), \left(y \in Y _ {K}, y ^ {\prime} \in Y, g \in G, v \in V\right).
$$

The term adapt denotes the capability of a DSS kernel to change its own capabilities:

$$
\begin{array}{c} C _ {t} = \text { adapt } \{(y _ {t - \tau} ^ {\prime}, y _ {t - \tau}, C _ {t - \tau}), \ldots , (y _ {t - 1} ^ {\prime}, y _ {t - 1}, C _ {t - 1}) \}, \\ (y \in Y _ {\mathrm{K}}, y ^ {\prime} \in Y _ {\mathrm{DS}}). \end{array}
$$

Similar to effectors and other components, the DSS kernel has planning capability, plan, that allows it to determine when to invoke specific capabilities:

$$
o _ {t, T} = \operatorname{plan} \left(K _ {t}, y _ {t}, g _ {t}, c _ {t}\right), \left(g _ {t} \in G, y _ {t} \in Y _ {\mathrm{DS}}, c _ {t} \in C\right).
$$

## 5. Types of situated DSS

We are particularly interested here in the roles that sensors and effectors play in achieving tight integration between the environment and the DSS. As we already mentioned, both ‘‘situators’’ (mediators) between the DSS and the environment can be implemented as one unit. For instance, the same software can implement viewing account balance and handling withdrawal. In general, though, this is not the case. For example, in e-commerce, the sensors could be software agents used to review the prices of a certain category of products, while the effectors may be separate agents responsible for payment and delivery.

We have used the terms ‘‘problem domain’’ or ‘‘environment’’ to denote what the mediators interact with. These terms need some clarification. Consider, for example, the purchase of a good. From the buyer’s perspective, the task of carrying out a transaction and actual shipping of the product is not his/her task. The task of the buyer is to make a payment, and monitor the progress of the delivery. Therefore, those elements of the information delivery and decision implementation which are essential to the performance of the task, but would not be normally executed by the potential user of a system, belong to the environment. Hence, the system that the user uses to purchase a good would not get involved in the details of packaging, and managing the shipment of a good. In particular, the implementation of a decision can trigger decisionmaking process by other entities in a chain-like fashion.

As we have discussed, both mediators can have a range of capabilities. We can distinguish trivial and advanced capabilities, where the trivial moderator would include connecting and basic transforming capabilities. The increasingly more advanced capabilities include transforming, alerting, interacting, adapting, and planning capabilities. On the other hand, the DSS may have both mediators handling all traffic from and into the environment on one hand, and part of the traffic on the other. In the former case, we have a fully situated DSS, or a Decision Station, while the latter case can be called a ‘semi-situated’ DSS.

Consider, for example, a DS with trivial capabilities. In the simplest case, one can think of an on-line banking system. Here, the user can view balances on different accounts, do ‘‘what-if ‘‘ analysis to see how much amount he or she could transfer to a foreign currency account considering the exchange rates, and perform the transfer. The user actually accesses information, makes a decision, and implements a decision without having to change the media. A more elaborate extension of this example would be on-line trading. Many e-commerce systems fall into this category. Consider, for example purchasing an air ticket online. Here, the users can specify queries, view alternatives, modify criteria, make a purchase, receive confirmation, and even obtain an electronic ticket.

In manufacturing, it has been stressed that IS and operations should be properly integrated [15]. The range of manufacturing systems including CAD/ CAM/CAPP, CNC, AGV, and AR/AS would fit well into such an integrated system. In such an integrated system, a DSS with planning and analysis capabilities could write business decisions to the business database, which would be then used by CAD/CAM/CAPP systems as inputs to make design decisions, which, in turn will be entered into the engineering database, and later translated into actions for CNCs, robots, and other devices coming into contact with the physical world [28].

A semi-situated DSS with trivial mediators would let some of the traffic from or into the environment go through other channels, than those directly employed by DSS. Third-party comparison-shopping tools (see, e.g., Ref. [33]) and e-commerce sites that enable running queries by the buyers, but do not allow actually executing transactions, fall into this category. This approach can be justified when a value of a particular good to be sold is considered rather high. For example, while GM and Ford were trying to make an on-line sale to the customer an option, Toyota decided to refer the customer to the dealer [32]. In another example, a customer web-based DSS that enables users to view important information about providers and surgeons is described. Based on this information, the customers can make healthcare decisions, but implementation goes beyond the system. In manufacturing, Lockamy and Cox [30] argued for an integrated performance measurement system that would capture operational measures (through sensors) and describe the situation at hand at a high level.

A semi-situated DSS with advanced mediators will either have sensors or effectors with the advanced capabilities. An example is a system that monitors remote environmental data and supports human perception and cognition through its capabilities including situation assessment, and alert generation [11]. An agent-based architecture (‘‘Retsina’’) for decision support that has three layers of agents to capture data and perform different information tasks, e.g., security analysis, is described in Refs. [52,53]. A DSS with decision-centric information monitoring (with the data that could influence decisions closely monitored for changes) is proposed in Ref. [44]. A system where agents monitor supplier prices, and respond by invoking an optimization model if necessary is described in Ref. [19]. A DSS that supports the implementation and control phases of decision-making is reported in Ref. [25]. Focusing on intangible investments problem, the DSS helps to coordinate and translate goals into plans, and supports users in implementing plans, distribution of plans through network, and preparing necessary documentation. Thus, the DSS supports implementation, rather than automating it.

The situated DSSs with advanced capabilities are probably the most interesting type of those discussed here. For example, a service at http://www2.activebuyersguide.mysimon.com/ lets the buyer choose the product category, identify important features, perform tradeoffs, and offer a range of products the website thinks are attractive to the buyer. When the buyer chooses one, he or she can do comparison-shopping, and later go to the seller’s site to complete the transaction. An architecture of a geographically distributed agent-based DSS, where agents monitor the environment, assess situations, and implement actions in a semi-autonomous manner is described in Ref. [6] in the crisis management context. A semi-autonomous system for awarding contracts, where an agent composes RFQs and evaluates bids is presented in Ref. [9].

## 6. Decision station: an illustrative example

## 6.1. Architecture for an investment decision station

We present here an example of an agent-based investment Decision Station. This example can be viewed as an extension of the developed investment DSS prototype discussed in Ref. [57]. The problem is in determining the portfolio of securities, monitoring its performance, and making modifications to the portfolio, if necessary. The system architecture is shown in Fig. 4.

The sensors incorporate multiple agents that collect information from different sources. These include financial markets, historical information, analysts’ opinions, news articles, and other relevant sources. The sensors monitoring the markets collect information about overall market and specific industry performance indicators (S&P 500, DJIA, etc.), performance of individual securities from the user portfolio, and the other securities on the ‘‘watch list.’’ They can easily be configured to add new securities and alarms. They can do some basic transformations, e.g., calculating moving averages and other technical indicators. The sensors attached to the historical data retrieve historical security performance upon demand and calculate some basic indicators (e.g., historical return and standard deviation for a security). The sensors for news articles deliver the financial, economic, and political news that may have an impact on a market to the user in a timely fashion. Active sensors would be able to perform advanced tasks, e.g., based on the market volatility they could decide to monitor market more closely (planning capability) and adjust the levels at which the alert signals are generated (adaptive capability).

![](/api/attachments/QC5Y355Q/fulltext/images/cfba5c7760ef6feb5d8f381fdbfa67d8ce8ba1c6b8cd68ad65ab5486b941f321.jpg)  
Fig. 4. Decision Station for investment management.

The effectors are the means of executing the user’s investment decisions. These can be linked to various online brokerage firms as alternative outlets for the ordering. The choice of the firm can be made interactively with the user on the basis of fees charged, reputation of the firm, past experiences, and other factors. The effectors support different types of order and can monitor execution of an order to see whether it had actually gone through or not. Active effectors can take charge of re-evaluating and re-submitting an order if necessary. For example, in limit orders, it is possible that the order will never be executed, because the price surpassed the limit. The effectors can detect this situation, and re-adjust the order, if necessary, within certain limits. Table 3 describes the key capabilities of sensors and effectors embedded in the investment DS in more detail.

The DSS kernel incorporates the financial models for estimating portfolio risk and return, knowledge and formulas for conducting fundamental and technical analysis, and others. The manager decides when to update the local information, keeps track of performance of the models, translates user decisions into buy/ sell signals for the effectors and may even authorize minor buying/selling decisions without user involvement within specified limits. The active interface adapts to the user preferences using direct and indirect input from the user. It displays the stock performance indicators and news articles that fit the user profile and interests.

## 6.2. Sample scenario and a prototype

In order to provide a more concrete example of the investment DS, we present a sample scenario and a prototype, and provide examples of sensor and effector capabilities outlined earlier in the context of the scenario. A UML activity diagram summarizing the working of a DS is presented in Fig. 5.

The diagram outlines the operation of a DS for portfolio management. The scenario presented in Fig. 5 begins with activities pertaining to collection of information about the portfolio and market performance. Then, the portfolio status is assessed in order to determine a need for an intervention. The intervention decision is either made automatically or in interaction with the user. If an intervention is made, the changes are implemented using the effector capabilities of composing and executing an order defined in the intervention. The operation of different DS components is detailed below.

Capabilities of sensors and effectors in an investment decision station

<table><tr><td colspan="2">Sensors</td><td colspan="2">Effectors</td></tr><tr><td>Capabilities</td><td>Key functions</td><td>Capabilities</td><td>Key functions</td></tr><tr><td>Connecting</td><td>Accessing stock quotes, market indicators (DJIA, S&amp;P 500), news articles, firms&#x27; financial data, historical data</td><td>Connecting</td><td>Placing buy/sell orders, transferring funds between accounts</td></tr><tr><td>Transforming</td><td>Calculating moving averages, portfolio performances, speed of change in stock prices, market indices, reconciling conflicting data, extracting keywords from news articles</td><td>Transforming</td><td>Calculating total amounts to be paid, placing special orders using pre-specified rules</td></tr><tr><td>Alerting</td><td>Signaling a sharp change in stock prices, market conditions, notifying the user about key variables (price, P/E ratio) reaching pre-specified targets, signaling breaking news</td><td>Querying</td><td>Querying sensors about current prices to execute special orders, requesting additional information on order or seeking confirmation of decision from the user</td></tr><tr><td>Adapting</td><td>Finding new sources of financial information, adjusting the thresholds for alert generation (e.g., in the case of sharp changes), assessing sources&#x27; credibility and reliability</td><td>Adapting</td><td>Adjusting the rules for placing special orders, adjusting planning capabilities</td></tr><tr><td>Planning</td><td>Deciding how frequently to read the stock, firm and market data, when to search for new sources, when to adjust alert thresholds</td><td>Planning</td><td>Deciding when to query the sensors, when to execute orders</td></tr></table>

![](/api/attachments/QC5Y355Q/fulltext/images/0eea89159ea982f8e06709518a53aadbd66e411a6977566f2f6fbf67767c7253.jpg)  
Fig. 5. Investment DS activity diagram.

The sensor connects to electronic information sources and imports the relevant data about the stock performance, market, and economy according to predefined rules. The sensor also performs some calculations including portfolio performance evaluation and changes in market indicators. Periodically, the sensor will adjust its parameters, most notably the threshold for alert generation. The capabilities of the sensor defined in Eq. (3) are specified here as follows:

```txt
plan={“choose next action”};
conn={“collect relevant data (SQL querying, XML, HTML parsing, etc.)”};
trans={“process data (e.g., calculate return on portfolio)”};
alert={“send notification of the sharp change (via e-mail)”};
adapt={“adjust alert generation threshold”}.
```

For example, the alert capability is realized as:

$$
a l e r t = \left\{ \begin{array}{l l} \text { ``Sharp   Change'' } & \text { if   } \Delta \text { Index } > \theta \\ \oslash & \text { otherwise } \end{array} \right.,
$$

where DIndex is the change in a market index, such as DJIA, and e\` is a pre-defined threshold value.

The adapt capability affects the above alerting capability by adjusting the threshold according to some function of the variance of the market index:

$$
\theta_ {t} = \theta_ {t - 1} + \operatorname{adj} (\sigma^ {2} (\text { Index })),
$$

where adj(.) is a function that calculates the magnitude of adjustment.

The sensors also update the database of the DS.

The DS manager (see Fig. 4) performs a more detailed assessment of situation. A sensor’s alert prompts the DS manager to reassess the portfolio of securities using available financial models (e.g., fundamental and technical models). The manager’s authority to make modifications to the portfolio is limited. If an interference that exceeds the manager’s authority is required, the user is notified and an attempt to initiate the decision support session is made. The active interface supports the user’s decision-making process, employing alternative portfolio generation, and critiquing [58]. The resulting portfolio is passed to the effector.

The effector determines changes that have to be made to the current portfolio and fills out the necessary order forms electronically. The set of capabilities described earlier as C={plan, conn, trans, query, adapt} in this example includes:

plan={‘‘choose time for submitting order,’ ‘‘choose the time to resubmit order’’};

conn={‘‘fill out order form,’’ ‘‘execute order’’};

trans={‘‘calculate all data needed to submit an order’’};

alert={‘‘send notification if the order could not be submitted’’ (via e-mail)’’}.

For example, having been given an order to purchase shares of a certain company for a specified amount, the effector can use the trans capability to calculate the number of shares and fill out the order form: number\_of\_shares = amount/price. Subsequently, the effector executes the changes (submits the forms) and monitors their implementation.

In the DS prototype—see Fig. 6 for a screenshot— the system’s agents generate four candidate portfolios proposed by agents called: ‘‘risky fundamental,’’ ‘‘risky technical,’’ ‘‘non-risky fundamental,’’ and ‘‘non-risky technical.’’ The critiquing agents that are also part of active interfaces generate critiques of the analyzed portfolios based on user profile.

The DS prototype uses data related to the software industry stocks (coded as X1 through X50) downloaded from the sources on the web to come up with recommendations. The data is processed using ‘‘transformation’’ capability to be used by the DSS models and to inform the decision making process. More in-depth elaboration of the prototype is given elsewhere [57].

The described decision station will inform the investor about the current situation, support his/her decision process, execute and monitor execution of the orders, thus becoming an active situated system.

## 7. Discussion and conclusions

We have argued for a DSS that is situated in its environment, i.e., has the capabilities of directly sensing and acting upon it. The generic design for such a system, which we call a decision station, involves the use of sensing and effecting components as well as active user interfaces. One major concern that we have not discussed so far is the complexity of such a system. Complexity is discussed here from three different perspectives: complexity of using the system, computational complexity, and development complexity.

![](/api/attachments/QC5Y355Q/fulltext/images/142580d5ff04227e9497ddbd9603fd45f6ddbfa943df75c01e70b6973d182385.jpg)  
Fig. 6. Screenshot of the prototype.

The complexity of use is concerned with both the system’s ease of use and its effectiveness in the decision-making process. This ultimately depends on the proper design of the active interface. One approach to effectively designing such interfaces has been elaborated in Ref. [58]. The idea is to facilitate effective decision making by using DSS-user intermediaries. Although we have not directly measured the usefulness of the prototype mentioned above, the related measure of satisfaction elicited from the student subjects that used the system showed the value of 4.25 on a Likert scale of 1 to 7. While clearly more thorough and formal studies are needed, this measure provides some basis for our belief that the users will be able to make use of the system with adequately designed active interface.

The issue of computational complexity (and computational feasibility) arises because, in the proposed architecture, new components are added on top of the traditional DSS. Naturally, this would lead to the increased demand for the computational power. It is difficult to provide an accurate assessment of the computational complexity involved for all possible problem domains, since we are not proposing an algorithm, but a generic architecture. We note, however, that the use of agent technology as the basis for the DS implies the consideration of the agents’ computational complexity. This issue is addressed in Ref. [29] (p. 242), where it is shown that ‘‘the complexity of autonomy-oriented computation (agent–environment interactions) is adapted to the complexity of tasks (agent environments).’’ The tasks that an agent performs depend on its capabilities. The common capabilities that we have outlined in this manuscript include: connecting, transforming, planning, and adapting. In general, it would be reasonable to assume that the capabilities listed above are ordered by the increasing degree of computational complexity (assuming that the planning capability could also be adapted). Therefore, depending on the type of the problem domain (environment) the designer would include different types of capabilities in the system; the more active capabilities would require higher level of complexity. For a more formal treatment of the computational complexity of autonomous agents, the reader is referred to Ref. [29].

Since the basic capability enabling the situatedness of DSS is that of connecting, we will briefly discuss it here. Ideally, both sensors and effectors have access to the databases/files in order to learn about the state of environment and to communicate decisions. Then connecting can be reduced to executing SQL statements. If this is not possible, ftp, telnet, or WWW could be used. The data can be located in HTML documents and HTML parsing may be required in order to access it. Many tools exist to accomplish this task, e.g., the Network Query Language (http://www.nqltech.com/ nql.asp) provides several flexible ways that enable agents to issue web queries. However, HTML parsing has obvious disadvantages, the major one being the possible redesign of web pages. While having maintenance personnel detect such changes and rewrite the connecting code may be an option (assuming that the web-page redesign is not a very frequent activity), the current trends toward adoption of XML may alleviate this problem considerably.

Finally, the issue of the complexity (feasibility) of development concerns the question of ease of development of DSs. Clearly, developing a situated DSS considerably requires more effort than developing a traditional DSS. However, the recent trend toward component-oriented software development is encouraging, since it enables and simplifies the development of more complex software. Moreover, the increased shift toward distributed architectures would enable use of distributed components. In this regard, it is useful to mention the work reported in Ref. [27] on DSS intermediaries, which suggests using CORBA in order to assemble DSS components.

In our opinion, the revival of interest in DSS research depends on new frameworks and architectures that would extend the cognitive capacities of DSS to meet the complexities encountered by the decision makers. We hope that our work points in this direction. The work does not produce detailed specifications or comprehensive guidance on how to build a situated DSS. Instead, our objective is to provide a basis for DS, description of its components, and specification of their capabilities and functions. Much work is required. For example, incorporation of the implementation phase in the DS needs proper analysis and design of system’s effectory capabilities with the utilization of findings from the management and problem solving literature. Furthermore, future work should be done on the nature of interaction between the components of a decision station and the kernel. Development of agent-based architectures for decision stations is another possibility to explore. Development of research prototypes and their evaluation would help to test the benefits and viability of the new concept.

An important research direction that could potentially arise from the outlined concept is its application to web-based customer decision support for e-commerce applications. In a recent paper, Silverman et al. [47] have emphasized the critical importance of providing adequate DSSs capabilities for shopping decisions. The paper distinguishes the three levels of such DSSs, including access-focused (basic search, browsing, etc.), transaction-focused (shopping support, guided choices, etc.), and relationship-focused levels. The latter one represents the highest level of support and expands the temporal and scope dimensions. This is indicates situated DSSs as promising candidate for the conceptual foundation of providing such decision support in e-commerce applications.

## References

[1] A.A. Angehrn, Computers that criticize you: stimulus-based decision support systems, Interfaces 23 (3) (1993) 3 – 16.

[2] R. Balasubramaniam, M. Kannan, Integrating group decision and negotiation support systems with work processes, Proc. of the 34th Hawaii International Conference on System Sciences, IEEE, Hawaii, 2001.

[3] M. Bauer, D. Dengler, Trias: trainable information assistants for cooperative problem solving, Third International Conference on Autonomous Agents, ACM Press, Seattle, WA, 1999.

[4] C.H.P. Brookes, A framework for Dss development, in: P. Gray (Ed.), Decision Support and Executive Information Systems, Prentice-Hall, Englewood Cliffs, NJ, 1994, pp. 27 – 44.

[5] J. Budzik, et al., Supporting on-line resource discovery in the context of ongoing tasks with proactive software assistants, International Journal of Human – Computer Studies 56 (1) (2002) 47– 74.

[6] T. Bui, J. Lee, An agent-based framework for building decision support systems, Decision Support Systems 25 (1999) 225–237.

[7] C. Carlsson, E. Turban, Dss: directions for the next decade, Decision Support Systems 33 (2) (2002) 105– 110.

[8] E. Claver, R. Gonzales, J. Llopis, An analysis of research in

information systems (1981 – 1997), Information and Management 37 (2000) 181– 195.

[9] J. Collins, C. Bilot, M. Gini, Mixed-initiative decision support in agent-based automated contracting, Proc. of Fourth International Conference on Autonomous Agents, ACM Press, Barcelona, Catalonia, 2000.

[10] D.G. Conway, G.J. Koehler, Interface agents: caveat mercator in electronic commerce, Decision Support Systems [Decis. Support Syst.] 27 (4) (2000) 355 – 366.

[11] S. Das, D. Grecu, Cogent: cognitive agent to amplify human perception and cognition, Proc. of Fourth International Conference on Autonomous Agents, ACM Press, Barcelona, Catalonia, 2000.

[12] O. Etzioni, D. Weld, A softbot-based interface to the internet, in: M.N. Huhns, M.P. Singh (Eds.), Readings in Agents, Morgan Kauffmann, San Francisco, CA, 1997, pp. 77 – 81.

[13] S. Franklin, A. Graesser, Is it an agent, or just a program?: a taxonomy for autonomous agents, in: J.P. Muller, M.J. Wooldridge, N.R. Jennings (Eds.), Intelligent Agents Iii: Agent Theories, Architectures, and Languages, Springer Verlag, Berlin, 1997, pp. 21 – 36.

[14] C. Gonzalez, G.M. Kasper, Animation in user interfaces designed for decision support systems, in: K.E. Kendall (Ed.), Emerging Information Technologies: Improving Decisions, Cooperation, and Infrastructure, Sage Publications, Thousand Oaks, 1999, pp. 45– 74.

[15] V. Grover, M.K. Malhotra, A framework for examining interface between operations and information systems, Decision Sciences 30 (4) (1999) 901–920.

[16] R. Guttman, A. Moukas, P. Maes, Agent-mediated electronic commerce: a survey, Knowledge Engineering Review 13 (3) (1998).

[17] S. Haeckel, R. Nolan, Managing by wire, Harvard Business Review (1993 Sept.–Oct.) 122– 132.

[18] C.E. Heckman, J.O. Wobbrock, Put your best face forward: anthropomorphic agents, e-commerce consumers, and the law, Proc. of Fourth International Conference on Autonomous Agents, Barcelona, Catalonia, 2000.

[19] T.J. Hess, L.P. Rees, T.R. Rakes, Using autonomous software agents to create next generation of decision support systems, Decision Sciences 31 (1) (2000) 1 – 31.

[20] A. Hinkkanen, et al., Distributed decision support systems for real-time supply chain management using agent technologies, in: R. Kalakota, A. Whinston (Eds.), Readings in Electronic Commerce, Addison Wesley Longman, Reading, MA, 1997, pp. 275 – 292.

[21] T.A. Horan, The paradox of place, Communications of the ACM 44 (3) (2001) 58–60.

[22] E. Horvitz, Principles of mixed-initiative user interfaces, Human Factors in Computing Systems, CHI 99, ACM Press, New York, 1999.

[23] M.T. Jelassi, K. Williams, C.S. Fidler, The emerging role of Dss: from passive to active, Decision Support Systems 3 (4) (1987) 299–307.

[24] N.R. Jennings, On agent-based software engineering, Artificial Intelligence 117 (2) (2000) 277 – 296.

[25] H. Kilvijarvi, M. Tuominen, Computer based intelligence,

design, choice, implementation, and control of intangible investments projects, Proc. of the 32nd Hawaii International Conference on System Sciences, IEEE, Hawaii, 1999.

[26] A. Kraft, S. Pitsch, V. Michael, Agent-driven online business in virtual communities, Proceedings of the 33rd Hawaii International Conference on System Sciences, IEEE, Hawaii, 2000.

[27] K.R. Lang, A.B. Whinston, A design of a Dss intermediary for electronic markets, Decision Support Systems 25 (3) (1999) 193– 214.

[28] R.R. Levary, Computer-integrated manufacturing: a complex information system, in: H.R. Parsaei, S. Kolli, T.R. Hanley (Eds.), Manufacturing Decision Support Systems, Chapman & Hall, New York, 1997, pp. 281– 291.

[29] J. Liu, Autonomous agents and multi-agent systems: explorations in learning, Self-Organization and Adaptive Computation, World Scientific Printers, Singapore, 2001.

[30] A.I. Lockamy, J.F.I. Cox, Linking strategies to actions: integrated performance measurement systems for competitive advantage, in: H.R. Parsaei, S. Kolli, T.R. Hanley (Eds.), Manufacturing Decision Support Systems, Chapman & Hall, New York, 1997, pp. 41– 54.

[31] C. Lueg, R. Pfeifer, Cognition, situatedness, and situated design, Second International Conference on Cognitive Technology, IEEE Computer Society, Aizu, Japan, 1997.

[32] B.K. Lundegaard, E-commerce (a special report): selling strategies—changing lanes: Toyota hopes to avoid the potholes that have plagued its competitors’ online efforts, Wall Street Journal (2001 April 23).

[33] P. Maes, Modeling adaptive autonomous agents, in: C.G. Langton (Ed.), Artificial Life: An Overview, MIT Press, Cam bridge, MA, 1995, pp. 135–162.

[34] P. Maes, R.H. Guttman, A.G. Moukas, Agents that buy and sell, Communications of the ACM 42 (3) (1999) 81 – 87.

[35] H. McBreen, et al., Experimental assessment of the effectiveness of synthetic personae for multi-modal e-retail applications, Proc. Of Fourth International Conference on Autonomous Agents, ACM Press, Barcelona, Catalonia, 2000.

[36] J. McDonald, J. Tobin, Customer empowerment in the digital economy, in: A. Lowy, D. Ticoll (Eds.), Blueprint to the Digital Economy: Creating Wealth in the Era of E-Business, McGraw-Hill, New York, 1998, pp. 202 – 220.

[37] N. Negroponte, Agents: from direct manipulation to delegation, in: Bradshaw (Ed.), Software Agents, MIT Press, Cambridge, MA, 1997, pp. 57 – 66.

[38] M.E. Nissen, Supply chain process and agent design for ecommerce, 33rd Hawaii International Conference on System Sciences, 2000.

[39] J. Nunes-Suarez, et al., Experiences in the use of Fipa Agent Technologies for the development of a personal travel application, Proc. of Fourth International Conference on Autonomous Agents, ACM Press, Barcelona, Catalonia, 2000.

[40] S.A. Raghavan, Janus: a paradigm for active decision support, Decision Support Systems 7 (1991) 379 – 395.

[41] S.J. Rosenschein, L.P. Kaelbling, A situated view of representation and control, Artificial Intelligence 73 (1 – 2) (1995) 149– 173.

[42] J. Roth, The network is the business, in: A. Lowy, D. Ticoll

(Eds.), Blueprint to the Digital Economy: Creating Wealth in the Era of E-Business, McGraw-Hill, New York, 1998, pp. 283 – 297.

[43] A. Scarl, C. Bauer, M. Kaukal, Commercial scenarios of digital agent deployment, Journal of Electronic Commerce Research 1 (3) (2000).

[44] L. Seligman, et al., Decision-centric information monitoring, Journal of Intelligent Information Systems [J. Intell. Inform. Syst.] 14 (1) (2000) 29 – 50.

[45] M.J.D. Shaw, M. Gardner, H. Thomas, Research opportunities in electronic commerce, Decision Support Systems 21 (1997) 149–156.

[46] J.P. Shim, et al., Past, present, and future of decision support technology, Decision Support Systems 33 (2) (2002) 111 – 126.

[47] B.G. Silverman, M. Bachann, K. Al-Akharas, Implications of buyer decision theory for design of e-commerce websites, International Journal of Human – Computer Studies 55 (5) (2001) 815– 844.

[48] R.H.J. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[49] E.A. Stohr, S. Viswanathan, Recommendation systems: decision support for the information economy, in: K.E. Kendall (Ed.), Emerging Information Technologies, SAGE Publications, Thousand Oaks, CA, 1999, pp. 21 – 44.

[50] N.A. Streitz, et al., I-Land: an interactive landscape for creativity and innovation, Human Factors in Computing Systems, CHI 99, ACM Press, New York, 1999.

[51] L. Suchman, Plans and Situated Actions: The Problem of Human – Machine Communication, Cambridge Univ. Press, Cambridge, MA, 1987.

[52] K.P. Sycara, K. Decker, D. Zeng, Intelligent agents in portfolio management, Agent Technology: Foundations, Applications, and Markets, Springer Verlag, 1997, pp. 267 – 282.

[53] K.P. Sycara, D. Zeng, Multi-agent integration of information gathering and decision support, European Conference on Artificial Intelligence, Budapest, Hungary, John Wiley and Sons, Chichester, UK, 1996.

[54] D. Tennenhouse, Proactive computing, Communications of the ACM 43 (5) (2000) 43–50.

[55] K.R. Thorisson, Real-time decision making in multimodal face-to-face communication, Second International Conference on Autonomous Agents, ACM Press, Minneapolis/St. Paul, MN, 1998.

[56] C.-C. Tseng, P.J. Gmytrasiewicz, A real time decision support system for portfolio management, Thirty-Fifth Annual Hawaii International Conference on System Sciences, IEEE, Big Island, Hawaii, 2002.

[57] R. Vahidov, A framework for multi-agent Dss, PhD Thesis, Dept. of Decision Sciences, Georgia State University, Atlanta, GA, 2000.

[58] R. Vahidov, Intermediating user – DSS interaction with autonomous agents, Decision Sciences Institute Annual Meeting, San Diego, CA, 2002.

[59] R. Vahidov, R. Elrod, Incorporating critique and argumentation in Dss, Decision Support Systems 26 (3) (1999) 249– 258.

[60] X.F. Wang, et al., Anytime algorithm for agent-mediated merchant information gathering, Proc. of Fourth International

Conference on Autonomous Agents, ACM Press, Barcelona, Catalonia, 2000.

[61] C.K. West, Techno-Human Mesh: The Growing Power of Information Technologies, Quorum Books, Westport, CT, 2001.

[62] G. Zacharia, A. Moukas, P. Maes, Collaborative reputation mechanisms for electronic marketplaces, Decision Support Systems 29 (2000) 371–388.

![](/api/attachments/QC5Y355Q/fulltext/images/be1c05555a01f76cfca0ad6db07de9e4f5802006b6d4337dda7365bc20bdc567.jpg)

ests include: decision support systems, distributed artificial intelligence and multi-agent systems, negotiation software agents, and soft computing.

Rustam Vahidov is an Assistant Professor of MIS at the Department of Decision Sciences and MIS, John Molson School of Business, Concordia University (Montreal, Canada). He received his PhD and MBA from Georgia State University. Dr. Vahidov has published papers in a number of academic journals, including Decision Support Systems, Journal of MIS, Information and Management, Fuzzy Sets and Systems, and several others. His primary research inter-

![](/api/attachments/QC5Y355Q/fulltext/images/8f7d1bcf2b2ba7161560cb002e4552b348d57a92b890454ec2a894c909c00642.jpg)

Gregory E. Kersten is a professor of Decision Sciences and Information Systems at the John Molson School of Business, Concordia University; Paul Desmarais/Power Corporation professor at the School of Management, University of Ottawa, and an adjunct research professor at the Carleton University Sprott School of Business. He is a founding member and the first Director of the Decision Analysis Lab. (DAL), Carleton University Sprott School of Business, the

first Director of the Information Systems at the John Molson School of Business, Concordia University and a member of the Ottawa Carleton Institute for Computer Science. Dr. Kersten received his MSc in Econometrics and a PhD in Operations Research from the Warsaw School of Economics, Poland. His research interests include individual and group decision-making, negotiations, knowledgebased systems and knowledge management, decision support, web-based systems and electronic commerce.
