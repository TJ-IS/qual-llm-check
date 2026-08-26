---
otero_id: 17708
otero_key: "RGBK5JSQ"
title: "Supporting cognitive feedback using system dynamics: A demand model of the global system of mobile telecommunication"
authors: "Tung Bui; Claudia Loebbecke"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00017-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supporting cognitive feedback using system dynamics: A demand model of the Global System of Mobile telecommunication

Tung Bui $^{a,*}$ , Claudia Loebbecke $^{b}$

$^{a}$ Department of Information and Systems Management, The Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong

$^{b}$ University of Cologne, Wilh.-Backhaus-Str. 23, 50931 Köln, Germany

Received 1 December 1994; revised 1 July 1995

## Abstract

Cognitive feedback has been known to be useful in providing decision makers with insights for enhancement of the modeling process. This paper proposes a design methodology to embed functionalities that integrate cognitive feedback in a computer-based decision support environment. From a system dynamics perspective, this paper proposes five types of information cues capable of providing cognitive feedback support at the individual, interpersonal and collective levels. DSS tools are also identified to deliver these information cues to the users. The proposed approach has been successfully applied in the construction of a decision model using system dynamics to forecast the demand for cellular telecommunications up to the year 2005 for Vietnam. Lessons learned from our model suggest that cognitive feedback is an appropriate approach to building a computer-based cognitive aid.

Keywords: Cognitive modeling; Problem solving by feedback analysis; System dynamics and simulation; Telecommunications forecasting

## 1. Introduction

For an organization, a comprehensive and robust strategic business plan is crucial to its long term survival. Modeling business situations and corresponding strategies is, however, not an easy process, especially in a complex and dynamic environment. Unfortunately, this process can rarely be supported by historical data that do not reflect well future trends. To alleviate this problem, experts with good modeling skills are often solicited [15,16]. While experts have proved to be a valuable source of information, their performance in dynamic modeling has been rather weak (e.g., [53]). According to Kleinmuntz and Thomas [29], decision makers who lack an adequate model of the dynamics of a problem cannot apprehend the shortcomings of their actions, and run the risk of propagating and perpetuating flawed decisions.

A growing body of research evidence from cognitive science suggests that cognitive feedback can be used to enhance the quality of decision outcomes as well as decision processes (e.g., [4,38,48,49]).

This paper proposes a design methodology to embed functionalities that integrate cognitive feedback in a computer-based decision support environment. Our focus is different from that of Boland et al. [5] who look at information technology as a potential enabler that facilitates and enhances dialogue and understanding in an organization with a distributed structure. We focus on identification of information cues, within which a DSS equipped with tools to support users' cognitive feedback would further enhance its effectiveness. Embedded in our design is a strong concept of the user as a learner. To operationalize our design method, we adopt system dynamics [12] as a modeling and simulation tool, and supplement it with cognitive support functions. The proposed methodology has been applied to construct a decision model to help senior executives of the Vietnam Postal and Telegraph Services construct a strategic planning model for the national demand for cellular telecommunications.

## 2. Cognitive feedback in the organizational decision environment

## 2.1. Feedback and its impacts on decision processes and performance

According to Simon [50], cognitive science is the study of intelligence and intelligent systems. Intelligence is closely related to adaptivity – in terms of problem solving, learning, and evolution. As intelligence is bounded by limits of human short-term memory and processing capacity, a good intelligent system is one that can adapt to new contexts as it evolves with its users over time. Hence, cognitive feedback can be defined as information provided to decision makers to offer them to a better understanding of decision processes. This information includes relations in the decision environment, relations perceived by the decision maker about that environment, and relations between the environment and the decision maker [4]. This feedback has been found to help the decision maker better understand the task structure, his own cognitive system, and the mapping and fit between the two (e.g., [19,20]).

Feedback occurs at two levels in the modeling cycle. First, feedback about the outcome of the decision provides insights regarding how accurate the decision was $[54]$ . Decision makers rely on outcome feedback to adjust their judgment $[22]$ . Second, cognitive feedback focuses on awareness of how well the decision maker did in terms of decision processes. Recent empirical studies suggest that outcome feedback in dynamic environments does not lead to improved decision performance (e.g., $[6,53]$ ). However, according to Doherty and Balzer $[9]$ , cognitive feedback is effective in improving the quality of the decision processes by clarifying the decision maker's intentions and controlling their implementation. Furthermore, in a dynamic environment, Newell et al. $[37]$ argue that providing cognitive feedback to decision makers should help them:

\- construct an appropriate model of the reality,

\- operate in a real-time, rich and complex environment requiring a vast amount of knowledge,

\- learn from the environment and from experience by simulation, thus enhancing the ability of the decision makers to comprehend dynamic changes in the underlying assumptions, and

\- adapt quickly to changes dictated by the users as the environment changes over time.

## 2.2. Three levels of organizational feedback

An organization is driven by its people. The use of skillful experts within an organization has proven to be an effective means for problem solving (e.g., [17,50,51]). Based on the assumption that “two experts are better than one”, researchers (e.g., [26,47]) recommend that opinions from more than one expert, whenever possible, should be considered. The use of multiple opinions not only helps reveal different views of a given problem, but can eventually consolidate expert consensus. Together, the views could provide a comprehensive and holistic description of the problem. Consensus among experts is a central assumption of a decisional context because most experts know how to solve problems, but they, as individuals, cannot explicitly specify the holistic view of the problem. It is assumed that the pooling of experts' opinions could offer enough clues to build a comprehensive theory. The argument here is germane to the concept of shared mental model discussed in the Computer-Supported-Cooperative-Work literature [7]. In this paper, we use the words "opinions", "assessment" and "judgment" interchangeably because they are part of the knowledge required for problem formulation and decision making.

In group decision making, Sengupta and Te'eni [49] show that cognitive feedback is useful in helping team members understand decision processes of themselves as well as those of others. They distinguish three levels on which cognitive feedback could affect group decision making. At the individual level, as discussed earlier, the group members could search for feedback cues that could shed light on the way they make decisions. Doherty and Balzer [9] demonstrated that cognitive feedback could enhance the quality of the decision by providing the decision maker with continuing consistency analyses of the performance of the decision making processes and outcomes. Such feedback was found to increase the cognitive control of the decision maker [20].

At the interpersonal level, analyses from others are taken into consideration to help the group members' decision making. Cognitive feedback can be measured by the extent to which members are made aware of the agreement or disagreement among themselves on the problem at hand. In interacting with others, the modelers become observers of their own thinking. As Senge [47] pointed out, learning the models of others compels rethinking of one's own model, either by adaptation (i.e., revision of existing model) or by generation (i.e., creation of a new model).

At the collective level, cognitive feedback seeks to foster team learning to help build a shared vision. A shared vision is one that each member can identify with and is committed to. Team learning starts with dialogue, during which members stop making assumptions and engage in a collective thinking mode [47]. This effort of thinking together involves learning how to recognize the patterns of interactions in teams. Multiple individual models bring multiple perspectives to bear, and more important, bring a holistic view.

Since it takes time for a shared vision to emerge, cognitive feedback at the collective level can help build this vision faster.

## 3. Design considerations for supporting cognitive feedback

## 3.1. Goals

Kersten and Cray [28] propose the term cognitive support systems (CSS) to describe systems that seek to help users in structuring knowledge-based systems using generalization and analogy as two basic approaches to decision making. However, lacking in their definition of CSS is the intrinsically dynamic feedback of decision making in which decision makers constantly search for cues in their own decision processes. The purpose of providing cognitive support is to offer decision makers information that allows them to learn more about the problem and its environment so that an appropriate model can be designed and used. During this modeling process, support should be provided to reduce the amount of modeling effort required and increase the accuracy of the thought process [25].

Cognitive feedback varies as to whether it is targeted at the individual, interpersonal, or collective level. Individuals seek feedback to gain more insight into their own decision processes and to understand better the outcomes. Boland et al. [5] note that individuals exhibit a sense of ownership of their mental models and attempt to link them to the outside world. While enhancement of personal cognitive control is the goal at the individual level, team members attempt to reach strategy convergence at the interpersonal level. Information related to individual differences and interest differentials are examples of feedback that could help members learn about their counterparts' knowledge and judgments. At the group level, Senge [47] argues, cognitive feedback should facilitate mutual understanding by encouraging exchange of personal opinions.

## 3.2. Information cues for cognitive feedback

Zachary [58] identifies five general human information processing limitations:

\- Working memory: Decision makers can handle only limited amounts of information at the same time. Memory decays rapidly if not actively used or reinforced.

\- Speed of cognitive operations: Decision makers often do not have enough time to perform complex thought processes involving a series of elementary reasoning steps.

\- Retrieval of information: A decision maker's memory is often not reliable. Recently learned or rehearsed information can be more easily recalled than older information.

\- Numerical operations: Decision makers tend to avoid complex thought processes that require many calculations.

\- Projection in time and space: Decisions makers do not project very accurately problems elements in time and space. In time, they tend to either underestimate or overestimate the speed of events. In space, they tend to have very rough perception of distance.

The underlying assumption here is that modeling skills can be improved by using feedback as an interactive and accelerated mechanism for reflective thought ([5,8,46]). A number of researchers (e.g., [13,34,36,38,47]) recognize several information cues that could be used as feedback. These cues are classified into five types:

![](/api/attachments/RGBK5JSQ/fulltext/images/2bbe4a3a1464ffaa50ae4a4ee5adcb8cc3c7c6bb8f830552f2a79e9f99baa55d.jpg)  
Fig. 1. Cognitive feedback and its information cues.

\- Time: Feedback implies judgment over time. As time can span an extended horizon, the possibility of navigating through time – either by speeding it up or slowing it down, including the possibility of freezing the time – offers pauses for reflection.

\- Space: Complex dynamic problems often embrace decisions that impact, or are impacted by, different geographical and/or functional areas. As each area is dictated by its local determinants, lessons learned from one area can bring valuable experience to another area.

\- Problem determinants: Prior work has shown that decision makers' mental models generally function poorly in a dynamic environment. Hence, variables must be isolated in order to fully evaluate the causes and impacts that drive decision makers' behavior.

\- View: While problem decomposition helps reduce complexity, the ability to capture a holistic view of the problem helps uncover possible inconsistencies, incompleteness and deficiencies of the mental model. It permits the development of systemic hypotheses to enhance the understanding of the real world.

\- Memory: The older an organization is, the more firmly entrenched its institutional procedures and mechanism become. Change is increasingly difficult. At the same time, age represents a wealth of experience across functional and geographical areas. Whether age inhibits or encourages change depends on how memory can be timely recalled.

Fig. 1 outlines these dimensions together with their attributes and associated actions or values. These dimensions should provide decision makers with the ability to identify gaps between their mental model and the real world. Roberts [43] argues that a model is not, and may not need to be, a perfectly accurate representation of reality. Rather, it is a flexible tool for reflection. With these five information cues, evaluation can be executed in an accelerated yet systematic fashion to enhance the representational quality of the model.

Paich and Sterman [38] suggest that, in teamwork, computer-based interactive modeling tools should allow representation of feedback structures to make it possible for modelers to engage in an iterative learning cycle of observation, reflection, design and action. Similarly, Boland et al. [5] view an organization as a group of autonomous agents who work together for a specific purpose. In this context, they advocate the use of information technology to support distributed cognition, stressing the importance of individual interpretation and group dialogue. Supporting cognition implies keeping decision makers abreast of the dynamic structure of the problem, their own problem assessment and decisions, and more important, the discrepancies between the two. Furthermore, we contend that feedback provided by the computerized modeling tool can help DSS users explore available information cues better, and consequently, perform more consistently in a dynamic environment.

Table 1  
DSS functional requirements for supporting cognitive feedback

<table><tr><td>Information cues for feedback</td><td>Data sources</td><td>Analysis tools</td><td>Interface</td></tr><tr><td>Time navigation</td><td>Historical data; Research data about future development</td><td>Project; Compress; Freeze; Select time intervals for calculation</td><td>Chronological plots; Tables</td></tr><tr><td>Space navigation</td><td>Data from different locations; data about different locations</td><td>Combine; Compare; Cluster</td><td>3-D Graphical display; Plots and tables</td></tr><tr><td>Problem determinants</td><td>Data on selected problem areas</td><td>Isolate variables; Generate scenarios; Perform sensitivity analysis; Analyze discrepancies; Feedback loops</td><td>Filters; Plots</td></tr><tr><td>Holistic view</td><td>Information about relationships between data sets</td><td>Generate scenarios; Decompose and aggregate subproblems; Feedback loops</td><td>Causal loop diagrams; Plots; Superposed graphs and plots</td></tr><tr><td>Institutional memory</td><td>Documentation; Publications; Personal and anecdotal memory</td><td>Document; Retrieve; Evaluate; Disseminate historical knowledge</td><td>Hypertext; Multimedia; Electronic imaging</td></tr></table>

As discussed in Section 4, information cues can be used as a means of information exchange and communication between team modelers to support construction of individual mental models, inter-model comparisons, and resolution of conflict between them.

## 3.3. Design requirements

In this section, we identify the functionalities that a DSS should have in order to provide cognitive feedback support to its users. For this purpose, Boland et al. [5] define three elements of a cognition system: actors, interpretations and actions. The actors represent the group members engaged in a continuous search for self-reflection, in reflection on others' analyses, and in dialogue to inform action. Boland et al. [5] contend that information cues must contain mixed forms of visual representation, be made available whenever they are needed, and be packaged in a fashion conducive to induction, synthesis, and innovative inquiry. We have compiled a list of characteristics and functions for the five types of information cues described previously (Table 1). These characteristics and functions are classified along the three main components of a DSS, i.e., database, analytical tools and man-machine interface. The tools listed in Table 1 resemble the ones that are typically prescribed for a DSS (e.g., [52]). However, they are particularly relevant for cognitive feedback to the DSS user. Common to the elements listed in Table 1 is our central requirement to provide users with feedback about gaps and dynamic feedback loops. The issue here is that information cues should be presented, not as a mere collection of facts, but as a means to provide feedback for acting purposefully.

## 4. Design of cognitive feedback support with system dynamics

In principle, the design requirements presented earlier can be implemented for all DSS that need a strong cognitive feedback component. In this section, we discuss the use of system dynamics $[12]$ as a modeling and simulation tool implemented in our design principles.

System dynamics provides an integrated dynamic modeling approach combining quantitative and qualitative aspects to simulate a phenomenon over time ([14,32]). It is based on some basic principles of cybernetics according to which the behavior of the system elements is endogenous and necessarily dependent on that of other elements [43]. System dynamics can be considered as a framework for understanding the dynamic interrelationships between the system elements rather than the static snapshots of elements [47]. From that perspective, models are considered as a tool conducive to support thinking, group discussion and learning in management teams [36].

System dynamics seems to be appropriate for developing information cues that support cognitive feedback. First, the system dynamics paradigm emphasizes intuitive understanding of the complex structure underlying dynamic systems [41]. Modeling the world is visualizing the relationships between the elements that compose it [18]. The behavior of a world is regarded as a consequence of the developments of the causal relationships between the elements over time. Second, the goal of a model is not to make precise quantitative predictions of the future (outcome and feedback on this outcome), but rather to uncover the trends of key decision elements where many of them are interrelated in complex fashions (functional validity feedback)

[56]. By conducting what-if analyses, decision modelers can progressively reinforce their understanding about the world [39]. Richmond [42] defines this reinforcement process as being characterized by a dual activity: generation of understanding and retardation of forgetting. Last, as the modeler develops a better understanding of the problem being analyzed, he can strengthen his “thinking” capacity. This capacity can be defined as the ability to build a mental model, compare on between models, and, if necessary, resolve the differences between them. Thus, cognitive feedback can be supported by providing information cues to facilitate these three basic thinking activities [21].

System dynamics has been successfully applied in a broad variety of economic and social settings. Due to its main characteristics and strengths, it has proven to be especially appropriate for modeling problems driven by a high degree of feedback loops between intervening forces ([2,23,35]).

## 5. Modeling the cellular telecommunication demand for Vietnam with cognitive feedback - a case study

This section provides an example derived from a real life study that illustrates the dynamics of cognitive feedback and how it can be supported. Our goal is to observe how cognition support tools interact with decision modelers.

## 5.1. Modeling the cellular telecommunication demand

The objective of the modeling effort is to derive an integrated market demand model for the Global System of Mobile communication (GSM) in Vietnam. The purpose of the model is twofold. First, it estimates the total demand of mobile communication measured by the number of users. Second, it predicts the relative relevance of the GSM demand driving forces.

![](/api/attachments/RGBK5JSQ/fulltext/images/b4f923d7f6070a82bb5f9f187f99e9d868d01466d2275cdb09a181ebb6227d3b.jpg)  
Fig. 2. Conceptual view of the GSM demand model.

## 5.1.1. Background

Vietnam currently has an estimated population of 72 million. In 1989, it decided to adopt a market economy yet maintaining its strong central government. Since then, the country has enjoyed unprecedented growth. Huge investments are being made in infrastructure development (e.g., roads, telephone lines, power stations). While Vietnam has one of the lowest teledensities in the world (0.4 per 100 inhabitants), it is committed to adopting the latest technology in telecommunications. The Vietnamese Postal and Telecommunication Service (VNPT) is working at full capacity to lay new telephone lines as the supply lags far behind the demand. In 1993, Vietnam implemented its first cellular phone network in Saigon, called Callink. In May 1994, VNPT adopted GSM as the standard for future nationwide cellular telecommunications [40].

## 5.1.2. Driving forces for GSM demand

In order to develop a model that captures the complex relationships among the interacting factors for GSM demand in Vietnam, we used a model developed by Loebbecke [30] to identify the basic driving forces for GSM demand. The demand model of cellular telecommunication has successfully been applied to Germany [30] and Hong Kong [31]. It considers seven main demand factors, each of which consists of several sub-factors with varying degrees of importance (Fig. 2):

\- Cost: Invariably, the cost of GSM usage is the single most important demand driver ([11,45]). It is broken down into the monthly fee and the usage cost per minute. Telecommunication analysts unanimously predict that the GSM usage fee will continue to decline due to economies of scale, maturation of the networks, and increased competition resulting from market liberalization.

\- Product quality: Product quality remains a prevalent factor in consumers' demand for information technology [1]. It consists of network quality, service quality, and terminal or handset quality. GSM is still in the growth phase; as with any new product, quality is a critical consideration for consumers [57]. Higher quality probably helps boost the demand for GSM during the introductory phase, but the boost is likely to weaken over time.

• Information about GSM: This factor is known in the marketing literature as communicability of product benefits [44]. Promotion of new telecommunication technology is often supported by advertising (including public relations), general publications introducing the new product and word-of-mouth. Advertising should convey a positive image; however, this is not necessarily true for independent publications and word-of-mouth.

\- GSM impacts on private lifestyle: Reachability also affects GSM users in their private lives. GSM brings convenience to social interaction; at the same time, in certain situations, it can become disruptive and annoying ([10,27]).

\- GSM impacts on business practices: The impact of cellular communication on business practices is in essence similar to that of the phone. GSM use is expected to have stronger, more positive externalities than other telecommunication services. As the capacity of the network increases with new GSM subscribers, its usefulness to GSM users will increase as they are able to communicate with more people [3]. With instant reachability, the most visible effect would be on continuous adaptation of work processes [33]. The new technology is expected to help foster business opportunities, although to a much lesser extent when compared to the introduction of the wired phone.

\- Alternative technologies: GSM demand depends on the development of alternative technologies [24]. While GSM brings more flexibility, wired communication is cheaper and still more reliable, particularly for large data transfer.

\- Availability of a GSM evaluation framework: The cost-effectiveness of a new technology is difficult to estimate [1]. Hence, it is argued, however, that if a solid evaluation framework exists, this evaluation would be used to support GSM adoption. This factor is particularly relevant to corporate users.

## 5.2. Modeling with cognitive feedback

Three top managers in charge of mobile and cellular telecommunications with rich industrial experience in Vietnam were invited to serve as modelers. As they are in charge of different managerial and technical aspects of GSM, and as they come from three regions of the country, their knowledge and views on the GSM market were expected to collectively embody a valuable cross-section of information. However, due to the complex and dynamic nature of the telecommunication market, it is impossible to establish a precise set of relationships among all intervening factors. Even if the experts chosen for building the system are the most knowledgeable available, their expertise is still limited by the sheer complexity and uncertainty of the demand for telecommunications in the future. This limitation is further aggravated by the lack of historical data due to the infancy of the new technology, and more important, the effects of time lags within different intervening factors.

The experts were briefed on the GSM forecasting model and its implementation of a computer using system dynamics. The interviewees were introduced to the functionalities of the simulation model. In particular, tools to support cognitive feedback were displayed to them in an interactive manner (see Table 2). Each of the experts received a two-hour tutorial on a sample simulation model. The training session stressed the utility of using the five information cues (i.e., time navigation, space navigation, problem determinants, holistic view, institutional memory).

To facilitate knowledge extraction, questions were centered around the analysis of the seven factors discussed above. Knowledge extraction was conducted by protocol analysis using Forrester's system dynamics graphical representation scheme. Due to the limited space on the computer screen, cues requested by the experts were printed. These printouts were posted on the wall to support observation, reflection, design, and action. After 47 iterations, the experts were satisfied with the outcome provided by the software. They felt confident with their market analyses and the simulation output.

The role of cognitive support in the modeling of the GSM demand is discussed in section 5.4..

Table 2  
DSS functions for supporting cognitive feedback in the GSM model

<table><tr><td></td><td>Data Sources</td><td>Analysis Tool</td><td>Interface</td></tr><tr><td>Time navigation</td><td>Research data about additional licenses to be granted in the future</td><td>Project current cost decline over a ten year time frame</td><td>Various plots showing the number of users over time</td></tr><tr><td>Space navigation</td><td>Data regarding GSM user numbers from Hanoi and Saigon</td><td>Compare cost developments and their impact in Hanoi and Saigon</td><td>3-D graphical display regarding the user numbers in several cities and regions over time</td></tr><tr><td>Problem Determinants</td><td>Data regarding use of GSM by different user groups (government, bus., private)</td><td>Perform sensitivity analysis regarding the availability of a nation-wide infrastructure and its impact on GSMdemand</td><td>Filtering the developments that have more than a 20% increase or decrease in a certain quarter</td></tr><tr><td>View</td><td>Data about the dependence of private use and technology maturity</td><td>Generate scenarios regarding the development of alternative technologies and their respective impact</td><td>Displaying causal loop diagrams regarding the interdependence of the seven main factors and their sub-factors</td></tr><tr><td>Memory</td><td>Data about Callink (analog network) development</td><td>Retrieve Callink database</td><td>Hypertext-based display of various telecommunication developments in Vietnam and regarding GSM usage in other countries (as far as accessible)</td></tr></table>

The discussion is preceded by a short presentation of the simulation results.

## 5.3. Simulation results

As illustrated in Figs. 3 and 4, the simulation results of the Vietnam GSM model are briefly described below. The evolution of the GSM demand measured by the number of users (Curve 1 in Fig. 3), the minute cost (Curve 2 in Fig. 3), and the monthly cost (Curve 3 in Fig. 3), are plotted on a time horizon divided into 44 quarters representing the period from January 1994 to December 2005. The numbers attached to the vertical axis show the minimum, maximum and mid-point values for each curve. For example, the minute cost would fall from a maximum of US\$ 0.18 to a minimum of US\$ 0.09 (actual selling cost) over the ten-year time span.

![](/api/attachments/RGBK5JSQ/fulltext/images/b9a048777bee2044f2ac6b493c234da3ef7c80dbe72df1ac24c36db50d85f51d.jpg)  
Fig. 3. Simulation results (I) of the GSM demand model.

![](/api/attachments/RGBK5JSQ/fulltext/images/4b51e2ccca623ab5eec1d016e1758ff94bc7d839408f75060730e9540a7b4872.jpg)  
Fig. 4. Simulation results (II) of the GSM demand model.

While the cost per minute of consumption is predicted to reach its minimum in the 17th quarter (i.e., in October 1999), the monthly cost would reach its minimum only in the 30th quarter (i.e., US\$ 14 in April 2002). Both cost minima equal 50% of the current cost, which has been stable since the introduction of GSM in 1994. The cascaded shape of both cost curves can be explained by the cost policy of the network operator (VNPT) which declared it would lower the prices according to infrastructure availability and for market pressure.

Interestingly, the predicted number of users does not follow the cascaded shape of the cost curves. While it is expected that the cost reduction will lead to an increase in GSM demand, Curve 1 shows that the number of users increases to a maximum (6 million users) in the 31st quarter (July 2002) when a slight decline starts. The number of users shows, however, little direct correlation with the GSM cost. This means that the cost does not play as dominant a role for GSM demand in Vietnam as has been observed and predicted in other countries (e.g., Germany, Loebbecke 1994). As demand will remain higher than the ability of the VNPT to offer new services, users whose business needs critically depend on telecommunication means are willing to pay more to subscribe to the service. Consequently, demand drivers other than cost contribute to the increase in GSM demand (see Fig. 4).

The impact of product quality increases steadily over time mainly reflecting the improved national coverage of the GSM network. As the second most important demand driver, the information volume available to customers shows a sharp increase in the early years, and then stabilizes at a value of 1.38 (Fig. 4). Information volume mainly consists of advertising and word-of-mouth. Vietnam has been investing heavily in GSM commercials, which led to a fast increase of awareness about the new technology. Over time, the impact of advertisements will be increasingly replaced by word of mouth because (i) the number of users spreading the word increases, and (ii)

advertisements for high-technology products have proved to be most effective during the early years immediately after a product launch. The positive impact GSM has on business practices will also continuously push the demand. Since GSM is currently the most convenient way to provide communication services, many companies, private and public alike, are willing to pay almost any price to subscribe to this service. GSM represents virtually the only opportunity to communicate in real time outside the company building.

Remarkable also is the curve representing the impact of alternative technologies. In Vietnam, the most important alternative technology is the fixed network. As the infrastructure is built, and the number of subscribers to fixed networks increases, cost-conscious customers will abandon GSM for a cheaper technology. In Fig. 4, advancements in alternative technologies are depicted by Curve 4 which slopes downward. As modeled in the system, the closer the value of the curve is to 1.00, the less the impacts alternative technologies have on the demand. Conversely, as the value drops to 0.50 in the year 2005, this suggests that alternative technologies will negatively affect the demand in a significant fashion. This prediction is remarkable if one compares this trend to that of other more advanced countries. In developed countries, such as Germany and Hong Kong, alternative technologies are more complementary than substitutable. Fixed networks have long been used before the introduction of GSM. With their stable demand, they have less significant impact on the GSM demand.

## 5.4. The role of cognitive support in modeling the GSM demand

During the model building process, the system dynamics software provided the executives with feedback in various forms (see Table 2). For each level of cognitive support, the actual frequency of use of cognitive feedback cues according to the five types of feedback is given in Table 3. Fig. 5 depicts the total frequency of use of the information cues for the three levels of organizational feedback. Furthermore, it indicates the sequence of information searches. $^{1}$

![](/api/attachments/RGBK5JSQ/fulltext/images/2476a7886e0f7a441cff2762ec0c1c95477de41e3887e222df53f1fa610e1128.jpg)  
Fig. 5. Actual frequency and sequence of use of information cues totaled for all three levels of organizational feedback.

As the modeling task involved long-term forecasting, time navigation was heavily sought at all three levels of cognitive support, namely individual, interpersonal and collective (Table 3). Simulation outputs regarding the number of users and the impact of the GSM cost (Fig. 3) and quality (Fig. 4) for the entire forecasting period were the first ones required by the decision makers. When doubts were cast regarding certain segments of the output curves (i.e., the sharp increase in the number of users in the 30th quarter, Fig. 3), the time span was reduced to allow for more detailed analysis on that shortened period. Thanks to computer visualization, it was discovered that the demand increase was caused by the sudden drop in monthly cost.

Screening of problem determinants was the most frequent activity as the three experts explored, weighed and adjusted the sub-factors of the demand forces (Table 3). The executives often referred to the relationships between stocks and flows $^{2}$ to differentiate between the development of the quality of GSM and its impact on demand (Fig. 2).

Observed frequencies of use of cognitive feedback in modeling the GSM demand for Vietnam

<table><tr><td rowspan="2"></td><td colspan="3">Levels of cognitive support</td></tr><tr><td>Individual</td><td>Interpersonal</td><td>Collective</td></tr><tr><td>Time navigation</td><td>**</td><td>**</td><td>**</td></tr><tr><td>Space navigation</td><td>n.a.</td><td>**</td><td>**</td></tr><tr><td>Screening of problem determinants</td><td>***</td><td>***</td><td>**</td></tr><tr><td>View</td><td>*</td><td>**</td><td>***</td></tr><tr><td>Institutional memory</td><td>**</td><td>*</td><td>**</td></tr></table>

The frequent display of causal loop diagrams enhanced the executives' understanding of the interdependencies of the subfactors involved in each driving force, and the holistic view of the problem. In particular, the circular loop between the number of users and the quality of the network caught the attention of the decision makers in the adjustment process. When the number of users increases, the quality of the networks decreases due to traffic congestion. The visual display of the simulation helped the modeler uncover the fact that VNPT must increase network capacity to improve quality.

Institutional memory was not supported by the simulation software. However, textual information regarding the history of mobile communications (e.g., the Vietnamese analog system) was often retrieved from a separate database for comparison purposes.

Visual examination of sensitivity analyses performed by peers was the most frequent activity during the initial phase of the modeling process. Discussion and arguments among group members were so intense yet interrupted by moments of reflection. As one member became quickly familiar with the forecasting model, he numbered the screen displays as he fine-tuned his model. As soon as the other two officials understood their colleague's modeling assumptions, they started to build their own. The structures of the three models were in essence similar. However, the three executives had different views regarding the evolution of GSM demand, costs of telecommunications, and the extent of GSM impacts on consumers. When there is a significant discrepancy in forecasting outcomes, executives sought to understand the points of views of their colleagues and re-examined their own thinking. They often ended up to adjust their model after discussion. Frequent search for information cues regarding holistic view, time navigation and problem determinants was requested by the group to progressively move toward a shared vision. Multiple adjustments were negotiated between the three executives as they cross-examined various chronological plots (see Table 3).

## 6. Concluding remarks

The purpose of this paper is to show that it is possible to design a DSS equipped with tools to support cognitive feedback. The proposed approach has been successfully used for modeling the future national demand for GSM services in Vietnam. The lessons learned from our model suggest that cognitive feedback is an appropriate approach to building a computer-based cognitive aid. The benefits of our approach are to (i) capture qualitative knowledge from a group of experts, and (ii) derive an operational model for decision support.

Feedback has been known to be useful in providing decision makers with insights for correction and enhancement of the modeling process. We have proposed five types of information cues that have proved able to provide cognitive feedback support at the individual, interpersonal and collective levels. DSS tools are also identified to deliver these information cues to the users. At the individual level, the GSM modeling example suggests that our design expectations are consistent with previous work in that cognitive control can be increased with feedback ([9,20]). Furthermore, it suggests that information cues can be used to reduce the modeling effort and enhance modeling accuracy [55].

More important, our study shows that cognitive feedback can serve as an effective means for dialogue and discussion among decision makers. Thus, our result confirms observations made by Sengupta and Te'eni [49] and Boland et al. [5]. Finally, the analyses provided by system dynamics can be used as a shared mental model for the group to collectively enhance its modeling perceptions of the problem at hand through an accelerated and iterative process [51]. A difficulty when modeling problems in a dynamic environment lies in the modelers' inability to infer sufficient operational knowledge. With the built-in simulation capability, system dynamics has the potential for responding in new contexts that may help experts refine their view of the problem. As such, the output of a simulation run becomes the input to another one until a satisfactory model is achieved.

This paper suggests a number of significant research possibilities. More research is needed to understand the relative importance of the five information cues (i.e., time, space, problem determinants, holistic view, and institutional memory). The GSM model is a long-range planning model. Here time navigation was the most frequently sought tool to support cognitive feedback. This might not be the case in other decision situations. With regard to the three levels of cognitive feedback (i.e., individual, interpersonal, and collective) the pattern of information sharing for cognitive feedback was not clear: what information can best serve the three levels of cognitive support, how frequently should these be triggered, and in what sequence are questions which remain unanswered? Moreover, the tools proposed in this paper (Table 2) were tested in a stand-alone computer environment. More design work is required if these tools are to be implemented in a distributed network: we need to know how decision makers interpret information cues in a distributed environment. Finally, it is important to investigate the role and effect of cognitive feedback tools in various cultural and inter-cultural settings. Answers to these research questions would help fine-tune the design principles outlined in this paper.

## Acknowledgements

This research was funded by the 1995 HKUST Direct Allocation Grant, DAG93/94.BM40/ISMT.

## References

[1] Bacon, J., The Use of Decision Criteria in Selecting Information Systems/Technology Investments, Management Information Systems Quarterly 16, No. 39 (1992) 35–360.

[2] Baills, G.; Olivier, C., MIRZA: Un Modèle Dynamique du Marché de l'Automobile, Presentation to the Congrès AFCET (Association Française pour la Cybernétique Economique et Technique, 1993).

[3] Bental, B., Consumption Externalities in Telecommunication Services, in: de Fontenay, A. et al., Eds., Telecommunication Demand Modeling (Amsterdam, 1990).

[4] Balzer, W. et al., Effects of Cognitive Feedback on Performance, Psychological Bulletin 106, No. 3 (1989) 410–433.

[5] Boland, R.J., Jr. et al., Designing Information Technology to Support Distributed Cognition, Organization Science 5, No. 3 (1994) 456–475.

[6] Brehmer, B., Systems Design and the Psychology of Complex Systems, in: Hogarth, R., Ed., Insights in Decision Making: A Tribute to Lillel J. Einhorn (University of Chicago Press, Chicago, 1990).

[7] Bui, T., Towards a Theory of Shared Mental Model in CSCW, Proceedings of the 1992 IFIP Workshop on CSCW (Germany, May 1992).

[8] Davis, H. and Hogarth, R., Rethinking Managerial Education: A View from Chicago, Selected Paper 72, University of Chicago, Graduate School of Business (1992).

[9] Doherty, M. and W. Balzer, Cognitive Feedback, in: Brehmer, B. and Joyce, C., Eds., Human Judgment: The SJT View, North-Holland (Amsterdam, 1988) 163–197.

[10] Dordick, H.S., The Social Uses of the Telephone, in: Forschungsgruppe Telekommunikation, Ed., Telefon und Gesellschaft 1 (Berlin, 1989) 221–238.

[11] Eutelis Consult, Scenario Mobile Communications 2010: Study on the Forecast Development and Future Trends in Technical Development and Commercial Provision up to the Year 2010 – Report to the Commission of the European Communities, CEC Contract Number 48, No. 166 (October 1993).

[12] Forrester, J., Industrial Dynamics, 6th ed. (Cambridge, Massachusetts, 1969).

[13] Forrester, J., Lessons from System Dynamics Modeling, System Dynamics Review 3, No. 2 (1987) 136–149.

[14] Forrester, J., Urban Dynamics, 3rd ed. (Cambridge, Massachusetts, 1970).

[15] Forrester, J., World Dynamics (Cambridge, Massachusetts, 1971).

[16] Forrester, J., The System Dynamics National Model: Macrobehavior from Infrastructure in Computer-Based Management of Complex Systems, Proceedings of the 1989 International Conference of the System Dynamics Society, Stuttgart, Germany (July 10–14 1989).

[17] Freiling, M. et al., Start a Knowledge Engineering Project: A Step by Step Approach, AI Magazine (Fall, 1985).

[18] Greene, W.H., Econometric Analysis (MacMillan Publishing Co., 2nd ed., 1993).

[19] Hammond, K., New Directions in Research on Conflict Resolution, Journal of Social Issues 21 (1965) 44–66.

[20] Hammond, K. and D.A. Summers, Cognitive Control, Psychological Review 79, No. 1 (1972) 58–67.

[21] Heilbroner, R.L., The Worldly Philosophers, Fifth Edition (Simon & Schuster, New York, 1980).

[22] Hogarth, R., On the Surprise and Delight of Inconsistent Responses, in: Hogarth, R., Ed., Question Framing and Response Consistency (Josey Bass, San Francisco, 1982).

[23] Homer, J.B., A Diffusion Model with Application to Evolving Medical Technical Technologies, Technological Forecasting and Social Change 31 (1987) 197–218.

[24] Jarratt, J. and J.F. Coates, Future Use of Cellular Technology – Some Social Implications, in: Telecommunications Policy (Feb. 1990) 78–84.

[25] Johnson, E. and J. Payne, Effort and Accuracy in Choice, Management Science 31 (1985) 395–415.

[26] Kaplan, R.S., and D.P. Norton, The Balanced Scorecard D Measures that drive Performance, Harvard Business Review 70, No. 1 (1992) 71–79.

[27] Katz, J.E., US Telecommunications Privacy Policy, in: Telecommunications Policy (December 1988) 353–368.

[28] Kersten, G.E. and D. Cray, Perspectives on Representation and Analysis of Negotiations: Towards Cognitive Support Systems (Carleton University, 1994).

[29] Kleinmuntz, D. and J. Thomas, The Value of Action and Inference in Dynamic Decision Making, Organizational Behavior and Human Decision Processes 39, No. 3 (1987) 341–364.

[30] Loebbecke, C., Marktentstehung Innovativer Infrastrukturen – Dynamische Simulation der Nachfrageentwicklung des Digitalen Zellularen Mobilfunks in Deutschland, PhD Thesis (University of Cologne, Germany, forthcoming).

[31] Loebbecke, C. and T. Bui, A Comparative Study of GSM Demand for Germany, Hong Kong, and Vietnam, Working Paper (The Hong Kong University of Science and Technology, 1994).

[32] Lyneis, J.M., Corporate Planning and Policy Design: A System Dynamics Approach (Massachusetts, 1980).

[33] Malone, T. and J. Rockart, How will Information Technology Reshape Organizations? Computers as Coordination Technology, in: Bradley, S. et al., Eds., Globalization Technology and Competition: the Fusion of Computers and Telecommunication in the 1990s (Harvard Business School, 1993).

[34] Milling, P., Time - A Key Factor in Corporate Strategy, in: Andersen, D. et al., Eds., System Dynamics '90, Proceedings of the 1990 International System Dynamics Conference (1990).

[35] Morecroft, J.D W., The Dynamics of a Fledging High-Technology Growth Market: Understanding and Managing Growth Cycles, System Dynamics Review 2, No. 1 (1986) 36–61.

[36] Morecroft, J.D.W., Executive Knowledge, Models and

Learning, European Journal of Operational Research 59 (1992) 9–27.

[37] Newell, A. et al., Symbolic Architectures for Cognition, in: Posner, E.D., Ed., Foundation of Cognitive Science (MIT Press, 1989).

[38] Paich, M. and J.D. Sterman, Boom, Bust, and Failures to Learn in Experimental Markets, Management Science 39, No. 12 (1993) 1439–1458.

[39] Payne, J.W., J. Bettman, E.J. Johnson and E. Coupey, Understanding Contingent Choice: A Computer Simulation Approach, IEEE Transactions on Systems, Man and Cybernetics 20, No. 12 (1990) 296–309.

[40] Petrazzini, B, T. Bui, Vietnam: On the Road to Reform (Telecommunications, May 1995).

[41] Radzicki, M.J., Dyadic Processes, Tempestuous Relationships, and System Dynamics, System Dynamics Review 9, No. 1 (1993) 79–94.

[42] Richmond, B., Stella II, An Introduction to System Thinking (High Performance Systems Inc., Hanover, NH, 1994).

[43] Roberts, E.B., System Dynamics – An Introduction in Managerial Applications of System Dynamics, Roberts, E.B., Ed. (Cambridge, 1978).

[44] Rogers, E.M., Diffusion of Innovations, 3rd Ed. (London, 1983).

[45] Ross, M., Marketing Strategies: Are the Customers Getting What They Expect?, in: FIBA, Ed., Europäischer Mobilfunk, 4th Annual Congress (Düsseldorf, 1992).

[46] Schoen, D., The Reflective Practitioner (Basic Books, New York).

[47] Senge, P.M.: The Fifth Discipline, The Art and Practice of the Learning Organization (New York, 1990).

[48] Sengupta, K. and T. Abdel-Hamid, Alternative Conceptions of Feedback in Dynamic Decision Environments: An Experimental Investigation, Management Science 39, No. 4 (1993) 411–428.

[49] Sengupta, K. and D. Te'eni, Cognitive Feedback in Group Decision Support Systems, MIS Quarterly (March, 1993) 87–113.

[50] Simon, H., Models of Thought (Yale University, 1979).

[51] Simon, H. and K.A. Ericsson, Protocol Analysis (MIT Press, 1986).

[52] Sprague, R. and E. Carlson, Building Effective Decision Support Systems (Prentice Hall, 1982).

[53] Sterman, J.D., Modeling Managerial Behavior: Misperceptions of feedback in a Dynamic Decision Making Experiment, Management Science 35, No. 3 (1989) 321–339.

[54] Tindale, R.S., Group vs. Individual Information Processing: The Effects of Outcome Feedback on Decision Making, Organizational Behavior and Human Decision Processes 44, No. 3 (1989) 454–473.

[55] Todd P., and I. Benbasat, The Influence of Decision Aids on Choice Strategies: An Experimental Analysis of the Role of Cognitive Effort, Organizational Behavior and Human Decision Processes 60 (1994) 36–74.

[56] Veit, K.P., System Dynamics and Corporate Long Range

Planning in Managerial Applications of System Dynamics, Roberts, E.B., Ed. (Cambridge, 1978).

[57] Weizsäcker von, C., The Economics of Value Added Network Services (Cologne, Germany, 1987).

[58] Zachary, W.W., Decision Support Systems: Designing to Extend the Cognitive Limits, in: Helander, Ed., Human Computer Interaction, Chapter 47 (1988) 99–1030.

![](/api/attachments/RGBK5JSQ/fulltext/images/cece44cb1fdda3cada1cd2366b706303f0bcf6f6456c29290f5c6a3ecb4a63a5.jpg)

Tung Bui is an associate professor of Information Technology at the U.S. Naval Postgraduate School, Monterey, California. His research interests include implementation of information systems in large organizations, group decision and negotiation support systems, and design of distributed knowledge-bases for organizational decision making. Dr. Bui is presently serving as the department editor of the journal Group Decision

and Negotiation, an INFORMS journal dedicated to the study of group decision/negotiation support systems.

![](/api/attachments/RGBK5JSQ/fulltext/images/e91676311b449ed6700b3f2a8d5b4b0787cf7e44723aa656d43e34f4d54c7b27.jpg)

Claudia Loebbecke received a Master in Business from the University of Cologne, Germany, and M.B.A. from Indiana University, and a Ph.D. in Business from the University of Cologne. She was an Associate Consultant with McKinsey & Co. in Duesseldorf, Germany, and a Research Assistant at the European Institute for Business Administration (INSEAD) in Fontainebleau, France, and at the Hong Kong University of Sci

ence and Technology. This work was done at the Hong Kong University of Science and Technology, Department of Information and Systems Management, Clear Water Bay, Hong Kong.
