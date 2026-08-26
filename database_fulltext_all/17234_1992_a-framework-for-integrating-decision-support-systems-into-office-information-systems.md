---
otero_id: 17234
otero_key: "QRFRUJH6"
title: "A framework for integrating decision support systems into office information systems"
authors: "Samo Bobek"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90015-h"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A framework for integrating decision support systems into office information systems

Samo Bobek

University of Maribor, Maribor, Slovenia

Office information system is presented as a network of decision support systems where the basis of linking decision support systems between them are decision making situations. After introducing concept of the network, basic components of it are briefly described. According to this context a model of decision support system which allows integration of different today known types of decision support systems is derived. Proposed network and model could be used as a framework for researching office information systems from a decision support systems view.

Keywords: Decision support, Group support, Knowledge based systems, Learning, Office information systems, Self-adaptivenes.

![](/api/attachments/QRFRUJH6/fulltext/images/631f6eedd8cc8d605da56be76128cc49d4c1b7581fe55bf8830252fc40cc3e04.jpg)

Samo Bobek is an Assistant Professor who teaches information systems courses. He has a bachelor degree in business Administration (1981), a masters degree (1986) and a doctorate (1989) in Management Information Systems from the University of Maribor (Yugoslavia). Dr. Bobek has participated in several research projects sponsored by the Slovenian Research Foundation. He also served as a consultant in information systems planning, executive support projects and strategic management in several leading firms in Slovenia. He has been a member of the organizing committees and has conducted several workshops and congresses for industrial managers. His research areas are executive information systems, impact of information technology in organizations, strategic and project management. He has published several articles in journals and reviews.

Correspondence to: dr. Samo BOBEK, School of Business Economics, University of Maribor, Maribor 62000, Razlagova 14, Slovenia.

## 1. Introduction

Since the term Decision Support Systems was introduced by Gorry and Scott Morton (1971) a huge body of knowledge has emerged in the literature. Yet, despite the high level of interest and activity, only a few authors try to research decision support systems in the context of office information systems (Hirscheim, 1986).

A computerized office is a phenomenon which should be discussed from a technological, organizational, sociological and some other viewpoints as well. It represents a new office space based on computer communication between people which changes working attitudes to provide greater flexibility. It enhances a new concept of management (why, what, when, how and where individuals work) especially its rationalization. Word processing was the first and for a long time the only step in the direction of office automation. The second step, electronic mail, still does not mean a computerized office. The computerized office represents a new way of communicating between people, a support for cooperation between them (i.e. making group decisions etc.), that is usually referred to as computer mediated or computer supported cooperative work.

The objective of this paper is to integrate the diffuse concepts of the decision support systems so that they can be viewed from an office information system context as a system of well defined, distinct, interrelated components (decision support systems).

The synthesis of different concepts is presented as an architectural framework that could facilitate further research and integration of decision support systems into office information systems.

## 2. Informed office

Emerging information technologies open up new possibilities for restructuring processes in which we use them. Keen's findings (1985) show that information technology influence people's habits and change management processes. Magee (1984) fortells changes in the working style of individuals and the course of processes as a whole due to the use of information technology. Changes in managing and doing business will show a great diversity; many of them we can not fortell. The computer becomes more and more an indispensable resource of the modern office.

The use of information technology will increase individual efficiency and effectiveness and further more efficiency and effectiveness of the organization. In the context of office information systems organization could be interpreted as office. It is known that in most cases we succeed in increasing the efficiency (at the individual or organization level) but seldom we have increased effectiveness (Porter, 1986).

A higher individual efficiency is in the most cases a result of change from pencil and paper, calculator or typing-machine to a computer. We try to automate individual work as much as possible. We do not try to change work in itself. The increase in efficiency of the organization is similar. We try to automate certain groups of repeating tasks. The organization remains basically the same. With the usage of information technology we do not try to change it essentially. Some process tasks are left to the computer which elaborates them easier and quicker.

The effectiveness of individual or organization can be significantly increased by different kinds of automatization; Zuboff (1985) describes it as "to informate". To informate means a complex process of examining information technologies and their use in such areas which will change the organization (Zuboff, 1985). Information technology is used in a way to enhance cooperation between humans and computers which gives synergical effects. This cooperation reflects in a synthesis of human intellectual activities and computer capabilities as a machine. This synthesis is known as intellectual technology (Curley, 1982). The essence of such synthesis is that the use of computer is not prescribed in advance and that humans use the computers in such a way that they become familiar to them by using them. Computer use means a continuous and intensive learning process in which humans search computers capabilities and enhance their own creative potentials.

Zuboff (1988) states that an individual in such conditions should master abstract thinking, inductive reasoning and understanding the phenomenon to which data relate. Most individual's concerns are directed toward the semantic and pragmatic dimensions of the information. Office work in an informatic society becomes more and more abstract. The nature of such work will be intellectual – individuals will master models as intellectual pictures of the real world. According to that model they will undertake actions. Individuals will become aware of facts and will influence them indirectly through models. Cooperation between man and computer becomes part of the role held by the individual in a given context of the organization (Zuboff, 1982). It gives the possibility to accept, change and mediate models to others in the organization. Computer mediated work is the opposite of direct cooperation between people (Winograd, 1986). Cooperation between people in the office of the future becomes more and more computer supported (Christie, 1986).

## 3. Architecture for decision support system viewed office information system

## 3.1. Office as a network of decision support systems

The office information system could be understood as a network of decision support systems. Every office information system is an open system. That means network (O) is as na open system composed by a set of components (HC), set of links between components (CO), relations with the surroundings which are determined by the entrance space into the system (XP), the exit space out of the system (YP) and the processes in the system which are determined by a set of transformations (DP). We can express it as follows:

$$
\mathrm{O} = (\mathrm{HC}, \mathrm{CO}, \mathrm{XP}, \mathrm{YP}, \mathrm{DP}), \quad \text { where }
$$

$$
\mathrm{HC} = \left\{\mathrm{hc} _ {\mathrm{i}}; \mathrm{i} \in \mathrm{I} \right\},\tag{1}
$$

(2)

$$
\mathrm{CO} = \left\{\left(\mathrm{hc} _ {\mathrm{p}}; \mathrm{hc} _ {\mathrm{q}}\right); \mathrm{hc} _ {\mathrm{p}} \in \mathrm{HC} \& \mathrm{hc} _ {\mathrm{q}} \right.
$$

$$
\in \mathrm{HC} \& \left. \operatorname{hc} _ {\mathrm{p}} \mathrm{COhc} _ {\mathrm{q}} \right\rbrace \mathrm{p}, \mathrm{q} \in \mathrm{I},\tag{3}
$$

$$
\mathrm{XP} = \left\{\mathrm{x} _ {\mathrm{j}}; \mathrm{j} \in \mathrm{J} \right\},\tag{4}
$$

$$
\mathrm{YP} = \left\{\mathrm{y} _ {\mathrm{k}}; \mathrm{k} \in \mathrm{K} \right\},\tag{5}
$$

$$
\mathrm{DP}: \mathrm{XP} \rightarrow \mathrm{YP}.\tag{6}
$$

The set HC includes decision support systems of an office information system, the set CO which represents the communication net (infrastructure) are links between them and the set of transformations (T) which have the character of decision making and other processes in the office.

The linking of decision support systems has to be dynamic and dependent on decision making situations as they occur. It has to be established as nonformal communication between decision makers and their computers. The result of connecting decision makers and their computers are groups of decision support systems which we will indicate as OG. Above mentioned linking can be expressed as follows:

$$
\mathrm{OG} _ {\mathrm{n}} = \mathrm{K} _ {\mathrm{n}} \mathrm{hc} _ {\mathrm{m}}, \quad \text { where }\tag{7}
$$

$$
\mathbf {m} \in \mathbf {M},\tag{8}
$$

$$
\mathbf {M} \in \mathbf {I},\tag{9}
$$

$$
\mathbf {n} \in \mathbf {N},\tag{10}
$$

If needed we have to be able for example, to link decision support systems for solving different problems. Groups of systems could be composed by one or more decision support systems. A decision support system could, for instance, belong to different problem solving groups (for example to the groups solving the problem 1 and to the group solving the problem 2). When the problem is solved current links between systems break off especially within temporary groups.

Groups OG are systems of the office system O. So we can on the basis of (1) and (7) represent this as follows:

$$
\mathrm{OG} _ {\mathrm{n}} = \left(\mathrm{HC} _ {\mathrm{n}}, \mathrm{CO} _ {\mathrm{n}}, \mathrm{XP} _ {\mathrm{n}}, \mathrm{YP} _ {\mathrm{n}}, \mathrm{DP} _ {\mathrm{n}}\right).\tag{11}
$$

For the group of decision support systems we can conclude as follows:

\- because decision support systems which belong to the set HC are linked into the group we can say

$$
\mathrm{HC} _ {\mathrm{n}} \subseteq \mathrm{HC},\tag{12}
$$

– within the group part of the existing communication net (infrastructure) activates:

$$
\mathrm{CO} _ {\mathrm{n}} \subseteq \mathrm{CO},\tag{13}
$$

\- the way of combining decision support systems into a group is influenced by management technology (MT) and decision making methods (DM):

$$
\mathrm{CO} _ {\mathrm{n}} = \mathrm{f} (\mathrm{MT}, \mathrm{DM}),\tag{14}
$$

\- entrance space into the group can be describe as follows:

$$
\begin{array}{r l} \mathrm{XP} _ {\mathrm{n}} = & \left\{\left(\mathrm{hc} _ {\mathrm{s}}, \mathrm{hc} _ {\mathrm{n}}\right); \mathrm{hc} _ {\mathrm{s}} \in \overline {{\mathrm{HC}}} _ {\mathrm{n}} \& \mathrm{hc} _ {\mathrm{n}} \right. \\ & \left. \in \mathrm{HC} _ {\mathrm{n}} \& \mathrm{hc} _ {\mathrm{s}} \mathrm{Kh} \mathrm{c} _ {\mathrm{n}} \right\}, \end{array}\tag{15}
$$

\- exit space out of the group is

$$
\begin{array}{r l} \mathrm{YP} _ {\mathrm{n}} = & \left\{\left(\mathrm{hc} _ {\mathrm{n}}, \mathrm{hc} _ {\mathrm{v}}\right); \mathrm{hc} _ {\mathrm{n}} \in \mathrm{HC} _ {\mathrm{n}} \& \mathrm{hc} _ {\mathrm{v}} \right. \\ & \left. \in \overline {{\mathrm{HC}}} _ {\mathrm{n}} \& \mathrm{hc} _ {\mathrm{n}} \mathrm{Kkc} _ {\mathrm{v}} \right\}, \end{array}
$$

$$
\overline {{{\mathrm{HC}}}} = \mathrm{HC} \backslash \mathrm{HC} _ {\mathrm{n}}.\tag{16}
$$

(17)

The groups formed can be smaller or bigger, concentrated or disperse. Experiments dealing with the computer supported cooperation within groups are directed mostly at the smaller groups workink together in the same rooms (DeSanctis, 1987). Despite this, one of the many characteristics of the decision making in the post-industrial society will be decision making in bigger and disperse groups (Huber, 1984) for which an adequate cooperation support will be needed. This support are office information systems. Computer supported cooperation will be, on the other hand, heavily influenced by new emerging management technologies and decision making methods.

The office information system has to be very adaptable, functioning as an autopoietic system. There is a need for self-organization of such networks of decision support systems. During researching and solving problems humans and computers expand their knowledge and the knowledge of the organization. The cooperation between the people goes on as a set of (decision making) processes. These processes are simultaneous. In them individuals deal with inconsistent and incomplete knowledge (informations) (Mazer, 1987); therefore individuals must cooperate to attain such knowledge enabling them to solve the problems. The knowledge individuals have about events, other peoples knowledge about the same events, the cooperation between people and the purpose for such cooperation are very confined.

3.2. Decision support system as a building block of the office

The decision support system is like every system with certain components, internal links between components and the external links with the surroundings, composed as follows:

\- the components are defined with a set of humans (people) and a set of computers,

\- the links between humans and computers (internal links of the system) are expressed by a process which determines the “rules” of cooperation between components,

\- the boundary links (between the system and the surroundings) are expressed by data as a picture of reality which is the entrance into the system and the decisions as the exit from it.

Deriving from the common expression of the system (1) we can express the basic building block of the office system – decision support system as follows:

$$
\mathrm{hc} = (\mathrm{h}, \mathrm{c}, \mathrm{Qhc}, \mathrm{Xhc}, \mathrm{Yhc}, \mathrm{Phc}), \quad \text { where }\tag{18}
$$

\- human (h) is an element of the set of humans (H):

$$
\mathrm{h} \in \mathrm{H},\tag{19}
$$

\- computer (C) belongs to information technology of the organization (C):

$$
c \in C,\tag{20}
$$

\- Qhr is a set of (possible) links between human and computer which can be expressed by

$$
\mathrm{Qhc} = \left\{\mathrm{q} _ {\mathrm{m}}; \mathrm{m} \in \mathrm{M} \right\}, \quad \text { where }\tag{21}
$$

$$
q _ {m} \in (H \times C \cup C \times H),\tag{22}
$$

\- Xhr is the entrance space representing messages (data) from other decision support systems,

\- Yhr is the exit space representing the transmission of data (information) to other decision support systems,

\- Phc is the process of computer supported decision making (we distinguish between four different generic ways of computer supported problem solving – knowledge renewal, learning the problem domain, learning the procedure of problem solving and researching):

$$
\operatorname{Phc} = \left\{\mathrm{P} _ {\mathrm{v}}; \mathrm{v} \in \mathrm{V} \right\}.\tag{23}
$$

Each element h from the set H is itself a system $h = (z, j, Dh, Xh, Yh, Ph)$ , where (24)

\- z corresponds to knowledge,

\- j is the language of the individual,

\- Dh corresponds to representation of the knowledge by the language,

\- Xh represents the individual's entrance space,

\- Yh represents the individual's exit space,

\- Ph are the individual's mental processes.

Each element c from the set C is itself a system too:

$$
\mathrm{c} = (\mathrm{bz}, \mathrm{sj}, \mathrm{Dc}, \mathrm{Xc}, \mathrm{Yc}, \mathrm{Pc}), \quad \text { where } \tag {25}
$$

\- bz is a knowledge base representing knowledge stored in the computer,

\- sj a system of computer language,

\- Dr a linkage between knowledge base and language system,

\- Xc a computer entrance space,

\- Yr a computer exit space and

\- Pr a set of processes done by the computer during supporting the decision making.

Human and computer cooperate during decision making, therefore:

\- there must be a cross-section between language (j) and the language system (sj),

\- cross section between Xh and Yc should not be empty,

\- cross section between Xc and Yr should not be empty neither,

\- both input and output spaces form messages which are interchanged between human and computer; the messages in the input space of an individual (Xh) and in the output space of the computer or in the input space of the computer (Xc) and in the output space of an individual (Yh) do not differ on the semantic and pragmatic level, they differ on the syntactic level.

The functioning of a decision support system could be described as follows. Human describe the problem which will be solved using the computer in a language familiar to the computer. Syntactic rules determine the correct description of the problem while semantic rules describe the context of the description. When describing a problem human uses knowledge he/she has about the problem domain. The description of the problem therefore reflects someones knowledge about the problem domain. A clear description of the problem enables the human to search for knowledge stored in the computer by himself or someone else. This enables the human to complete his/her knowledge. Human interacts with computer in exchanging knowledge by using the language system of the computer. We tried to illustrate this interaction in Figure 1.

![](/api/attachments/QRFRUJH6/fulltext/images/5d1a8a4ec68391ee83d019fb9092b85931af2860f412bdd352c11c6831d071a7.jpg)  
Fig. 1. A problem solving system of the network.

The decision support system which enables an exchange of knowledge in the process of problem solving is a problem solving system. It is also an autopoietic system. Since we have defined the network of decision support systems as an autopoietic system and because the decision support system is an element of such a network, this characteristic holds on for it too. The decision maker enlarges his/her knowledge by researching and solving of problems which is also true for the computer.

![](/api/attachments/QRFRUJH6/fulltext/images/5af69207e45eef7aaff22baa04a008874d256f6efe151019e1f0b6795544101f.jpg)  
Fig. 2. Typology of decision support technologies.

## 4. Typology of decision support systems in the office information system context

Considering decision support systems from an office information system viewpoint, four types of decision support systems could be identified. Criteria for distinguishing between them are:

\- individual decision making versus group decision making,

\- quantitative knowledge base versus qualitative knowledge base,

\- structured decision situations support versus illstructured decision situations support.

According to these criteria we distinguish between:

\- Structured decision support systems; structured decision situation support for individual decision making with knowledge expressed in a quantitative way.

\- Illstructured decision support systems; illstructured decision support for individual decision making with knowledge expressed in a quantitative way.

\- Expert systems; structured decision situation support for individual decision making with knowledge expressed in a qualitative way.

\- Expert support systems; illstructured decision situation support for individual decision making with knowledge expressed in a qualitative way.

\- Structured group decision support systems; structured decision situation support for group decision making with knowledge expressed in a quantitative way.

\- Illstructured group decision support systems; illstructured decision support for individual decision making with knowledge expressed in a quantitative way.

\- Group expert systems; structured decision situation support for individual decision making with knowledge expressed in a qualitative way.

\- Group expert support systems; illstructured decision situation support for individual decision making with knowledge expressed in a qualitative way.

The majority of them are well documented in the literature. For the others intensive research is in progress. Main directions in research efforts are toward expert support systems and in integrating artificial intelligence technologies in the group support systems. We will be able to integrate them into office information systems, beyond communications problems, when we will overcome different ways of expressing knowledge in computers and with usage of compatible language systems.

## 5. Conclusions

Office is for the knowledge workers the arena for performing everyday tasks. The computer should be an effective tool to human's intellectual activities. There is a demand for finding the ways how to support human's cognitive processes and how to support connecting individuals whose function is cooperation in the organization. We propose studying and researching of office information systems as a network of decision support systems.

Our framework regards linking of the decision support systems dynamically and depending on decision situations. When problems arise, decision support systems organize themselves into groups in an autopoietic manner. During cooperating in solving of problems, individuals exchange and expand their knowledge and knowledge of the organization. The crucial point in office information systems are therefore knowledge representation and language usage.

Both the underlying framework and the actual implementation are in the process of empirical validation in laboratory and field studies. We try to build a consistent approach for implementing different information technologies for supporting knowledge workers in the office.

## References

Christie, B. (1986). Human Factors of Information Technology in the Office. Wiley & Sons, New York 1986.

Curley, K.F. and P.J. Pyburn (1982). “Intelectual” technologies: The Key to Improving White Collar Productivity. Sloan Management Review, Vol. 24, No. 3, 1982, pp. 31–41.

DeSanctis, G. and R.B. Gallupe (1987). A Foundation for Study of Group Decision Support Systems. Management Science, Vol. 33 No. 5, 1987, pp. 589–609.

Gorry, G.A. and M.S. Scott Morton (1971). A Framework for Management Information Systems. Sloan Management Review, Vol. 13, No. 1, 1971, pp. 55–70.

Hirscheim, R.A. (1986). Office Automation: A Social and Organizational Perspective. Wiley & Sons, New York 1986.

Huber, P.G. (1984). The Nature and Design of Post-Industrial Organizations. Management Science, Vol. 30, No. 8., 1984, pp. 928–951.

Keen, P.G.W. (1985). Computers and Managerial Choice. Organizational Dynamics, Vol. 14, No. 2, 1985, pp. 35–50.

Magee, J.F. (1984). What Information Technology Has in Store for Management. Sloan Management Review, Vol. 25, No. 1, 1984, pp. 17–31.

Mazer, M.S. (1987). Exploring the use of distributed problem solving in office support systems. IEEE 1987 Office Automation Symposium, pp. 217–225.

Porter, I.R. (1986). Managing the Diffusion of End-User-Computing Technologies: A Fifties Mindset with Eighties Tools. In: Jarke M. Eds: Managers, Micros and Mainframes. Wiley & Sons, New York 1986, pp. 55–72.

Winograd, T. (1986). Understanding Computers and Cognition. Ablex Norwood, NY, 1986.

Zuboff, S. (1985): Automate/Informate: The Two Faces of Intelligent Technology. Organizational Dynamics, Vol. 14, No. 3, 1985, pp. 5–18.

Zuboff, S. (1982). New Worlds of Computer Mediated Work. Harvard Business Review, Vol. 60, No. 5, 1982 pp. 142–153.

Zuboff, S. (1988). In the Age of the Smart Machine: The Future of Work and Power. Basic Books, New York 1988.
