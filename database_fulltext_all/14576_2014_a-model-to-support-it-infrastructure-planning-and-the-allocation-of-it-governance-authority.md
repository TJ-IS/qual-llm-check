---
otero_id: 14576
otero_key: "VTGXZKS2"
title: "A model to support IT infrastructure planning and the allocation of IT governance authority"
authors: "Steven Thompson; Peter Ekman; Daniel Selby; Jonathan Whitaker"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.10.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A model to support IT infrastructure planning and the allocation of IT governance authority

Steven Thompson <sup>a,</sup>⁎, Peter Ekman <sup>b</sup>, Daniel Selby <sup>a</sup>, Jonathan Whitaker <sup>a</sup>

<sup>a</sup> Robins School of Business, University of Richmond, 1 Gateway Road, Richmond, VA 23173, United States <sup>b</sup> Mälardalen University, Högskoleplan 1, Västerås, Sweden

## a r t i c l e i n f o

Article history: Received 7 August 2012 Received in revised form 24 October 2013 Accepted 27 October 2013 Available online 2 November 2013

Keywords: Decision support systems IT governance Markov decision processes Case studies IT infrastructure planning Global operations

## a b s t r a c t

Information technology (IT) requires a signi<sup>fi</sup>cant investment, involving up to 10.5% of revenue for some <sup>fi</sup>rms. Managers responsible for aligning IT investments with their <sup>fi</sup>rm's strategy seek to minimize technology costs, while ensuring that the IT infrastructure can accommodate increasing utilization, new software applications, and modi<sup>fi</sup>cations to existing software applications. It becomes more challenging to align IT infrastructure and IT investments with <sup>fi</sup>rm strategy when <sup>fi</sup>rms operate in multiple geographic markets, because the <sup>fi</sup>rm faces different competitive positions and unique challenges in each market. We discussed these challenges with IT executives at four Forbes Global 2000 <sup>fi</sup>rms headquartered in Northern Europe. We build on interviews with these executives to develop a discrete-time, <sup>fi</sup>nite-horizon Markov decision model to identify the most economically-bene<sup>fi</sup>cial IT infrastructure con<sup>fi</sup>guration from a set of alternatives. While more <sup>fl</sup>exibility is always better (all else equal) and lower cost is always better (all else equal), our model helps <sup>fi</sup>rms evaluate the tradeoff between <sup>fl</sup>exibility and cost given their business strategy and corporate structure. Our model supports firms in the decision process by incorporating their data and allowing firms to include their expectations of how future business conditions may impact the need to make IT changes. Because the model is <sup>fl</sup>exible enough to accept parameters across a range of business strategies and corporate structures, the model can help inform decisions and ensure that design choices are consistent with <sup>fi</sup>rm strategy.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

To compete in a global marketplace, <sup>fi</sup>rms are increasingly building relationships and engaging in transactions with partners and customers outside their country of origin. Firms globalize their operations to reduce costs, obtain labor and expertise, and pursue growth by accessing new markets [1,6,28].

As part of their global strategy and structure, many <sup>fi</sup>rms establish subsidiaries in other countries. While corporate headquarters (HQ) emphasize <sup>fi</sup>rm-wide value creation and loss prevention, subsidiaries have a more limited scope of <sup>fi</sup>nancial performance in their respective markets [7,8]. The <sup>fi</sup>rm must de<sup>fi</sup>ne the extent to which each subsidiary is able to make decisions independently of HQ, to align subsidiary governance with <sup>fi</sup>rm-wide <sup>fi</sup>nancial performance. Financial performance improves when <sup>fi</sup>rms allow subsidiaries to react to local market conditions rather than follow globally-standardized business processes [3,14].

At the same time, granting decision authority to subsidiaries can create tension between subsidiaries and HQ, including decisions related to the governance of information technology (IT). Firms formulate their business strategy through their governance mechanisms, and then align their IT resources to support the business strategy [9,20]. Prior to the 2002 Sarbanes–Oxley Act (SOX), <sup>fi</sup>rms tended to decentralize IT governance and delegate IT investment decisions to IT professionals closest to the problem [17]. While this decentralized approach offered the advantage for <sup>fi</sup>rms to better utilize their IT resources to respond to local market conditions, it also involved the risk that IT investments may not align with the overall business strategy [29]. This lack of IT-business alignment could increase the likelihood of wasted <sup>fi</sup>nancial resources, user dissatisfaction, and security control failures, create managers who are reluctant to invest in future IT initiatives, and ultimately undermine <sup>fi</sup>nancial performance [3]. Since SOX, many <sup>fi</sup>rms globally centralized IT decision-making processes to mitigate this risk, optimize resource allocations, satisfy users, strengthen controls, and support the <sup>fi</sup>rm's strategy [17,36].

The primary argument for centralized IT governance is that in<sup>fl</sup>uential managers are involved in making IT decisions. These managers prioritize IT projects based on their relevance to the <sup>fi</sup>rm's strategy, and ensure that important IT projects receive adequate funding [34]. When decision authority is decentralized, IT professionals (while close to the problem) may not understand the negative effects of their ideal “local” solution on other areas of the <sup>fi</sup>rm.

The opposing argument is that centralized IT decision-making may limit the in<sup>fl</sup>uence of local managers in the IT decision-making process, when these managers may actually have a better understanding of the problem and their respective markets. IT professionals, closer to problems that are driven by local market conditions, may be in a better position to identify and de<sup>fi</sup>ne solution requirements and prioritize projects. Centralized IT infrastructure authority risks poor decisions due to a lack of knowledge and information overload in the face of multiple complex markets [18]. Based on this argument, many <sup>fi</sup>rms decentralize IT governance when subsidiaries offer different products/ services or operate in diverse markets [16]. When markets are more diverse and dynamic, the <sup>fi</sup>rm may receive more requests for new IT systems and changes to existing IT systems. In diverse and dynamic markets where change requests are frequent and HQ has a limited understanding of the problem, better IT investment decisions can be made more quickly if subsidiaries have decision authority to apply their knowledge of the local market, and these IT investments will lead to superior <sup>fi</sup>nancial performance [16].

We develop a model that enables <sup>fi</sup>rms with multiple subsidiaries and varying market conditions to determine the economic consequences of centralization/decentralization of IT decision authority. Our decision framework enables <sup>fi</sup>rms to evaluate costs and bene<sup>fi</sup>ts associated with various IT infrastructure designs, under varying degrees of centralized and decentralized IT control, and to evaluate IT investment risks due to uncertain future conditions.

Firms can use our model to identify whether the dynamism in different markets is suf<sup>fi</sup>ciently large to justify the higher cost and divergent systems/processes associated with decentralization. Our model supports managers and IT decision-makers in their efforts to align IT investments with the <sup>fi</sup>rm's strategic objectives. We base the model on interviews with senior managers involved in IT governance at four Forbes Global 2000 <sup>fi</sup>rms headquartered in Northern Europe. While the <sup>fi</sup>rms operate in different industries, they indicate that a better understanding of the short- and long-term economic impacts of various governance and control arrangements would be helpful in making future decisions.

The remainder of the paper is organized as follows. In Section 2, we review prior research on IT governance and IT investment decisions. In Section 3, we describe the problem setting. In Section 4, we develop a model to frame the decision of whether to centralize or decentralize IT decision authority as a discrete time, <sup>fi</sup>nite horizon, Markov decision problem (MDP). In Section 5, we present simulation results to illustrate the application of our model to IT infrastructure and governance decisions for a global <sup>fi</sup>rm under a range of business environment conditions. In Section 6, we conclude with managerial implications and directions for future research.

## 2. Literature review

Prior research has identi<sup>fi</sup>ed <sup>fi</sup>ve areas of IT governance — strategic alignment, risk management, resource management, value delivery, and performance measurement [39]. This paper focuses on the strategic alignment area of IT governance, and identi<sup>fi</sup>es the near-term and longterm costs and bene<sup>fi</sup>ts associated with centralized/decentralized IT investment decisions. Strategic alignment requires senior managers to align IT strategies with overall business strategy as the focal point of their IT infrastructure. We offer a decision support model to ensure that IT investments are aligned with <sup>fi</sup>rm strategy in terms of centralization/ decentralization, and we incorporate knowledge about future costs bene<sup>fi</sup>ts more formally into the IT decision-making process.

Prior research has studied the IT investment decisions of managers as a form of strategic alignment, and found that managers achieved better organizational performance when they had a strategic intent for IT investments [24]. While managers provide oversight for IT investment decisions [30], prior research has not reached a consensus on the extent of their involvement [39]. One study suggests that senior management needs to be involved, but does not go so far as to say that all decision rights should rest entirely with senior management [36]. Another study concludes that the strategic alignment decisions of IT reside on a continuum, and based on the context could be decentralized, centralized or mixed [15]. A third study surveyed 500 managers responsible for IT governance and conducted follow-up interviews with 30 CIOs [35], and <sup>fi</sup>nds that strategic alignment provides revenue growth when the environment ties accountability to business results and applications are effective, otherwise strategic alignment can lead to counterproductive IT investments.

Aligning IT investments based on business needs impacts the outcome of IT initiatives, such as ERP implementation [37]. Consistent with the arguments described above, some research supports centralization and other research supports decentralization. For example, one study found that productivity increased and loss ratios decreased as insurance <sup>fi</sup>rms used centralized IT planning and control [26], suggesting that centralized IT planning and control can improve <sup>fi</sup>nancial performance. Another study found that the distinctive characteristics of CRM data processing and localized nature of CRM efforts are best supported when CRM technologies are loosely coupled to the broader infrastructure and governed locally [33].

This study contributes to the literature on the effects of oversight on IT investment decisions and the allocation of decision authority. Our model provides a basis for <sup>fi</sup>rms to evaluate the impact of marketspeci<sup>fi</sup>c factors on the need for subsidiaries to maintain decision authority and control over local IT investment decisions. While prior research focused on process and controls, this paper incorporates the economic considerations of IT decision authority and IT investment decisions with the strategic alignment considerations of IT governance. This is an important contribution, because decision makers are not merely focused on reducing IT costs, but on ensuring that IT investments are in the economic and strategic best interests of the <sup>fi</sup>rm. This study continues research into how decision support techniques can facilitate IT decisions, building on prior work in a knowledge warehouse setting [27], electronic market setting [29], and Internet server-based setting [5]. Our use of a Markov decision problem model is consistent with recent research that uses MDP for other IT governance issues such as workforce and data management [12,21]. While these studies support improved performance of speci<sup>fi</sup>c IT infrastructure, this study broadens and extends prior research by offering a decision support model to ensure that overall IT investments are aligned with <sup>fi</sup>rm strategy.

## 3. Problem setting

For this study, we collaborated with four Forbes Global 2000 <sup>fi</sup>rms with headquarters in Northern Europe and subsidiaries on several continents. All four <sup>fi</sup>rms have revenue over US\$1 billion, with equities publicly traded on U.S. and European exchanges. Table 1 provides an overview of our case study <sup>fi</sup>rms and interviewees, including the industry, nature of product (durable vs. non-durable), and nature of customer (industrial vs. consumer) for each <sup>fi</sup>rm. To protect the con<sup>fi</sup>dentiality of our case study <sup>fi</sup>rms, we assign an anonymous name based on the <sup>fi</sup>rm's industry. For each <sup>fi</sup>rm, we collected data from European HQ and U.S. subsidiaries.

Case study <sup>fi</sup>rms and executive interviewees.

<table><tr><td rowspan="2">Firm</td><td rowspan="2">Product</td><td rowspan="2">Customer</td><td colspan="2">Executive interviewees</td></tr><tr><td>Europe</td><td>U.S.</td></tr><tr><td>Equipment Firm</td><td>Durable</td><td>Industrial</td><td>Global CIO</td><td>Regional VP/Controller Manager IT Operations</td></tr><tr><td>Parts Firm</td><td>Non-durable</td><td>Industrial</td><td>Global CIO</td><td>Regional Controller Sales Unit Controller</td></tr><tr><td rowspan="3">Household Goods Firm</td><td rowspan="3">Durable</td><td rowspan="3">Consumer</td><td>Global CIO</td><td>Regional IT VP</td></tr><tr><td>Global CTO</td><td>Regional Controller</td></tr><tr><td>Global IT Director</td><td></td></tr><tr><td rowspan="3">Consumer Products Firm</td><td rowspan="3">Non-durable</td><td rowspan="3">Consumer</td><td>Global CIO</td><td>Regional CIO</td></tr><tr><td>Deputy CIO</td><td>Regional IT Director</td></tr><tr><td></td><td>Regional Sales Director</td></tr></table>

One of our objectives in this multiple case study was to understand the perceived value and trade-offs associated with centralized/ decentralized IT planning and governance. Case studies are frequently used to understand a contemporary phenomenon when the problemboundary is unclear [10,40]. Our use of case studies to frame and provide context to a problem is consistent with recommendations to use case studies as a foundation for theory-building [11,40]. Case studies have been used in prior decision support research on IT governance, such as work to identify governance processes for high performance data warehouses [38].

Data collection took the form of interviews that were supplemented with additional archival data including internal documentation and publicly-available information. This data triangulation approach enabled us to compare responses of interviewees with public data and con<sup>fi</sup>dential internal documents [4]. The interviews were based on semi-structured questions that asked senior managers to describe their current business challenges and IT strategies (see interview guide in Appendix A). In addition, respondents were asked to describe typical IT projects, the scope of these IT projects, and their occurrence.

Most interviews were attended by multiple members of the research team, and the data for each interview was analyzed by three members of the research team [23]. The interviews are transcribed in formal interview notes and maintained in a research database. Our data enables us to identify common high-level factors that these MNCs utilize to make IT governance decisions, and these factors drove the formulation of our model. Our data con<sup>fi</sup>rms earlier research that found that MNCs were inclined to centralized IT governance to achieve lower costs, but are concerned about the impact of centralized IT governance on agility and performance of subsidiaries [13,19]. For example, the Global CIO of Equipment Firm stated that their efforts to adopt a common ERP system were hampered by the subsidiaries' reluctance to use common business processes, believing that each region “was fundamentally different.” Similarly, subsidiaries of Parts Firm were disappointed when they were forced to migrate to a common ERP system, stating that they used to “jump over backwards for the customer” but were no longer able to do so.

## 3.1. Illustrative example

As one example, consider the decision problem facing Consumer Products Firm, who shared speci<sup>fi</sup>c IT infrastructure design challenges and estimates of IT costs with our research team. Consumer Products Firm has three primary business units. In addition to the corporate HQ in Northern Europe, the <sup>fi</sup>rm has a large subsidiary in Europe and a smaller subsidiary in the U.S. The European subsidiary sells products throughout the European Union, Scandinavia, and the United Kingdom. The U.S. subsidiary sells products throughout the U.S., Canada, and Mexico. In addition to their regional customers and distributors, both subsidiaries operate within a multi-tier supply chain environment with regional and foreign suppliers. Fig. 1 illustrates the basic operating environment.

As illustrated in Fig. 1, the IT infrastructure of Consumer Products Firm consists of three separate but connected platforms, and each platform is associated with a corresponding annual cost. The annual cost re<sup>fl</sup>ects all IT expenditures including maintenance, enhancements, modi<sup>fi</sup>cations and integration. Initially, the subsidiaries maintained decision authority over IT investments, and the only information required from HQ pertained to <sup>fi</sup>nancial reporting data. Each subsidiary was free to build custom applications to improve performance. For example, the U.S. subsidiary invested signi<sup>fi</sup>cant resources to develop an application to obtain information from distributors for use by <sup>fi</sup>eld sales representatives.

Consumer Products Firm identi<sup>fi</sup>ed an opportunity to achieve substantial cost reduction by consolidating the three separate platforms into a single platform. The <sup>fi</sup>rm would be able to reduce the number of applications and consolidate hardware, and the decrease in complexity would reduce the ongoing costs associated with licenses and maintenance. The <sup>fi</sup>rm's goal was to move from the environment shown in Fig. 1 to the environment shown in Fig. 2.

![](/api/attachments/VTGXZKS2/fulltext/images/f80e37f6bc0df3410c16179d900ebd61c716b4a0d2bf04c21ecc7b5f69af40ef.jpg)  
Notes:  
1. In boxes, 'S' indicates supplier, and 'D' indicates distributor.  
2. Amounts represent the firm's estimates of total 2009 system costs for three platforms.

Fig. 1. Current operating environment of Consumer Products Firm.

![](/api/attachments/VTGXZKS2/fulltext/images/c4cf85fb6890e5d1c1d96029a3eb905ddb9ef847a39e731399845f95e11e3712.jpg)

Notes:

1. In boxes, 'S' indicates supplier, and 'D' indicates distributor.

2. Amount represents the firm's estimate of total system costs for a combined platform.

Fig. 2. Future operating environment for Consumer Products Firm.

While HQ was committed to ensuring that new IT infrastructure would continue to support all functionality currently in use, the subsidiaries had reservations about the plan. The overall goal, part of an “administrative excellence” initiative, was to centralize the IT function to achieve greater ef<sup>fi</sup>ciency and stability while retaining “some degree” of <sup>fl</sup>exibility. The Global CIO believed that the transition would bene<sup>fi</sup>t the overall performance of the <sup>fi</sup>rm, stating “If we are going to do something it needs to be under one umbrella.” In contrast, the Deputy (European) CIO thought change should be gradual and that when it came to IT, the <sup>fi</sup>rm should strive for “good enough” rather than excellence. The U.S. Regional CIO was also skeptical, stating “The wrong IT [investments] might compromise business opportunities.” The U.S. Sales Director was concerned that the ERP system and associated modules that formed the foundation of the new global platform were not well-suited to support many of the U.S. IT initiatives in place or planned for the near future. While it would still be technically possible for the U.S. subsidiary to move forward with those initiatives, the cost would be higher. The result would be a reduction in project return on investment (ROI) that would be large enough to scuttle some initiatives and reduce the attractiveness of the others.

There was an additional concern that subsequent IT budgets for each subsidiary would have to be increased to accommodate requests for system enhancements, such as integration with suppliers and distributors. Absent a higher budget allocation for system enhancements, even good projects with strong ROI would begin to backlog. Further, U.S. subsidiary managers worried that their estimates regarding the need for future system enhancements (derived from previous experience) may not re<sup>fl</sup>ect future needs in the new environment.

This example illustrates the fundamental challenge of determining how to allocate IT decision authority and control. On one hand, the <sup>fi</sup>rm must consider the potential bene<sup>fi</sup>ts of centralization. On the other hand, the <sup>fi</sup>rm must also consider the potential economic and competitive impact of decisions that hinder the ability of subsidiaries to respond to local market conditions. The <sup>fi</sup>rm faces a decision environment where several alternative IT infrastructure plans are under consideration. Each plan speci<sup>fi</sup>es the substrate hardware, enterprise systems and modules that the <sup>fi</sup>rm will support. We use the term platform to describe an enterprise system and its corresponding modules. The <sup>fi</sup>rm would like to identify the platform, or set of platforms, that maximizes the expected ROI, yet is robust in the face of variability in the extent to which system enhancements are required. Our model enables <sup>fi</sup>rms to evaluate the short-, intermediate- and long-term <sup>fi</sup>nancial implications of platform decisions on the costs and bene<sup>fi</sup>ts associated with future IT initiatives. This helps to ensure that IT investment decisions are aligned with the <sup>fi</sup>rm's strategic goals by ensuring that the need for adaptability/local autonomy and the bene<sup>fi</sup>ts of economies of scale/standard business processes are explicitly considered.

## 4. Valuation model for IT infrastructure con<sup>fi</sup>guration

Our model uses available data to estimate short- and long-term costs and bene<sup>fi</sup>ts of alternative IT infrastructure designs that use one or more different platforms under consideration. Our model assumes that IT governance should mirror the IT infrastructure design. This assumption is supported by prior research discussed in Section 2, and by our case study <sup>fi</sup>rms including Consumer Products Firm that serves as an example in this paper.

The model incorporates current data regarding the cost and bene<sup>fi</sup>ts of migrating to a new platform con<sup>fi</sup>guration (including the cost of “reconnecting” to systems of business partners), future expectations of cost/bene<sup>fi</sup>ts of IT change requests across a range of project categories, and historical data from IT project proposals to estimate the rate of change requests across project categories from each subsidiary. We model the decision problem as a discrete time, <sup>fi</sup>nite horizon, Markov decision process (MDP). Time is split into <sup>fi</sup>xed-length intervals (periods). The process state is observed at the beginning of a period, and a decision is chosen from a <sup>fi</sup>nite set of possible decisions. Immediate costs and bene<sup>fi</sup>ts are incurred depending on the state and the decision, which determines transition probabilities for the next state. That state is realized at the end of the period, the process state is updated, and the process repeats. This model seems appropriate for this setting because IT strategic plans typically involve a <sup>fi</sup>nite time horizon. According to our interviews, the CIOs expect to revisit and likely replace enterprise platforms every seven to ten years. The episodic nature of IT decision-making is conducive to the discretization of time intervals where decisions can be modeled as occurring on a periodic basis.

## 4.1. Notation summary

The essential notation for the description of the MDP is given below:

## Parameters

Q index set of subsidiaries $( Q = \{ 1 , . . . , q \} ) ;$

s subsidiary index (s ∈ Q);

$P$ index set of IT platforms $( P = \{ 1 , . . . , p \} ) ;$

$j$ IT platform index (j ∈ P);

$M$ index set of time periods (M = {1, …, m});

$b _ { t }$ IT budget for new projects at time t (does not include ongoing maintenance);

$R$ index set of request categories (R = {1, …, l});

$r$ category index for change requests (r ∈ R);

$\nu _ { s j }$ cost of migrating subsidiary s to platform j, including all costs associated with hardware, software, integration, and implementation;

$a _ { r j s }$ cost of completing a category r change request on platform j at subsidiary s;

$b _ { r j s }$ bene<sup>fi</sup>t of completing a category r change request on platform j at subsidiary s (we allow for the fact that not all change requests will have a measureable bene<sup>fi</sup>t);

$\lambda$ discount rate of return (per period cost of capital).

## State space

$x _ { r s }$ number of category r change requests not yet completed for subsidiary s;

$z _ { s j }$ current platform of subsidiary s;

$t$ time period index (t ∈ M);

$X$ matrix of $\dot { x } _ { r s }$ values;

$Z$ array of $\left[ z _ { s j } \right.$ values;

S process state $( S : = [ X , Z , t ] ) .$

## Random variables

g<sub>rst</sub> number of new category r change requests from subsidiary s at time t;

G array of $g _ { r s t }$ variables.

Decision variables

y<sub>rst</sub> number of category r change requests to complete for subsidiary s at time t;

$l _ { s j t }$ whether subsidiary s is transitioned to platform j at time t; $\dot { Y }$ array of decision variables;

Ƒ(S) set of feasible decisions for a given state S;

C(Y) total bene<sup>fi</sup>t associated with decision Y.

Objective value

$V _ { n } ( S )$ maximum expected n-stage value in state S.

## 4.2. Process state

Based on our interviews, none of the CIOs or IT Directors expected any enterprise system that they selected to be in use for more than ten years. In the case of Household Goods Firm, the CIO expected the system to be in use for only <sup>fi</sup>ve to seven years. Given that IT strategic plans and system life expectancy are <sup>fi</sup>nite with respect to time, we consider a decision process with a <sup>fi</sup>nite time horizon divided into m periods of constant length. The transition probability from state A to state B is constant from one period to the next. However, since the IT project budget can vary over the planning horizon, we include time in the state de<sup>fi</sup>nition. We therefore have a stationary MDP where the process state is de<sup>fi</sup>ned by the following:

• Current IT platform of each subsidiary

• Number of change requests for each project category for each subsidiary that have not been completed

• Time period.

## 4.3. Constraints on decision variables

For a state S := [X, Z, t], decision variables in Y must satisfy:

• Budget:

$$
\sum_ {s} \sum_ {j} v _ {s j} l _ {s j t} + \sum_ {r} \sum_ {s} a _ {r j s} y _ {r s t} \leq b _ {t}\tag{1}
$$

• Project volume:

$$
y _ {r s t} \leq x _ {r s}, \forall r, \forall s\tag{2}
$$

• Platform requirements:

$$
\sum_ {j} l _ {s j t} = 1, \forall s\tag{3}
$$

• Non-negativity:

$$
y _ {r s t} \geq 0, \text { integer }.\tag{4}
$$

All decisions Y that satisfy (1)–(4) for a state S are denoted by Ƒ(S). Additional constraints can be added. For example, there may be projects that must be completed to maintain system integrity and security. While these projects may not have a direct measureable ROI, they must be completed to ensure the ongoing reliability of the IT infrastructure.

## 4.4. Stage reward

Once a feasible decision Y has been made at the beginning of a period, there are a number of immediate expected costs and rewards. First, there is the expected positive reward $b _ { r s }$ to the <sup>fi</sup>rm from completing a change request of category r for subsidiary s. The <sup>fi</sup>rm also incurs a <sup>fi</sup>nancial cost $a _ { r s }$ associated with completing the change request. In addition to costs and bene<sup>fi</sup>ts associated with individual change requests, there could also be a cost $\nu _ { s j }$ associated with migrating subsidiary s to platform j. The stage reward associated with Y is:

$$
C (Y) = \sum_ {r} \sum_ {s} b _ {r s} y _ {r s t} - \sum_ {s} \sum_ {j} v _ {s j} l _ {s j t} - \sum_ {r} \sum_ {s} a _ {r s} y _ {r s t}.\tag{5}
$$

Table 2

C(Y) can be positive or negative. If $\begin{array} { r } { \sum _ { r } \sum _ { s } b _ { r s } y _ { r s t } > \sum _ { s } \sum _ { j } \nu _ { s j } l _ { s j t } + } \end{array}$ $\textstyle \sum _ { r } \sum _ { s } a _ { r s } y _ { r s t } ,$ then the bene<sup>fi</sup>ts associated with selected projects, represented by the <sup>fi</sup>rst term in the stage reward function, outweigh the costs associated with those projects, and vice versa.

## 4.5. Transition probabilities

Uncertainty in the problem is related to the frequency of each category of change request from each subsidiary. We assume that the entries of $G : = [ g _ { r s t } ]$ are statistically independent of each other. Let $S : =$ [X], [Z] be the current state, $Y \in { \mathsf { F } } ( S )$ the chosen decision array, and $\hat { S } : =$ $\big [ \hat { X } \big ] , \big [ \hat { Z } \big ]$ after existing change requests are completed and new project requests arrive. State <sup>^</sup>S is updated as follows:

$$
\hat {x} _ {r s} = x _ {r s} - y _ {r s t} + g _ {r s t}\tag{6}
$$

$$
\hat {z} _ {s j} = l _ {s j t}\tag{7}
$$

$$
\hat {t} = t + 1.\tag{8}
$$

The transition probability from S to ${ \hat { S } } ,$ given decision Y, is

$$
P _ {\hat {S S} (Y)} = \prod_ {s \in Q} \prod_ {r \in R} \mathcal {P} \left\{\boldsymbol {g} _ {r s t} \mid z _ {s j} = \hat {x} _ {r s} - x _ {r s} + y _ {r s t} \right\}.\tag{9}
$$

## 4.6. Objective function

$$
V _ {1} (S) = \max _ {Y \in \mathcal {F} (S)} C (Y),\tag{10}
$$

$$
V _ {n} (S) = \max _ {Y \in \mathcal {F} (S)} \left\{C (Y) + \sum_ {\hat {S}} \lambda P _ {S \hat {S}} (Y) V _ {n - 1} (\hat {S}) \right\}, n > 1.\tag{11}
$$

The complexity of computing $V _ { n } ( S )$ for n N 1 depends on the size of the decision space $\mathsf { F } ( S )$ . For most real-world scenarios involving up to 10 subsidiaries, 50 change request categories, and a 10-year planning horizon, computing $V _ { n } ( S )$ is computationally tractable. The simulation and analysis of Consumer Products Firm in the next section included three subsidiaries, 15 project categories, and the MDP coded on a Lenovo T510 laptop with 2.53 GHz Intel Core i5 processor and 4 GB RAM, which arrived at a solution using value iteration, a backward recursive technique in less than 1 min per iteration (see Appendix C for the pseudo code of the value iteration algorithm).

## 5. Simulation and analysis

The simulation is based on the decision problem facing Consumer Products Firm illustrated in Figs. 1 and 2, in which Consumer Products Firm is trying to decide which business units to place on Platform 1 and which to place on Platform 2.

In essence, IT decision makers were trying to decide whether to migrate all business units to the lower cost platform (Platform 1) where system modi<sup>fi</sup>cations are more costly (where $\nu _ { s j }$ parameter values are lower and $a _ { r j s }$ parameter values are higher), or to allow the U.S. subsidiary to remain on the more expensive Platform 2 that is more <sup>fl</sup>exible and less costly to modify. As suggested in Table 2, if data is available our decision support model can enable decision makers to evaluate the potential bene<sup>fi</sup>t of a large number of design alternatives.

Consumer Products Firm did have good estimates of the expected cost of placing each business unit on either Platform 1 or Platform 2. The impact of change requests and ongoing system enhancements was not as clear. We base the project categories on <sup>fi</sup>ve areas shown in Table 3, identi<sup>fi</sup>ed in prior research [22] to help Consumer Products Firm better estimate the types of potential projects and the <sup>fi</sup>nancial impact of those projects. While we found this framework to be helpful, our model allows IT decision-makers to de<sup>fi</sup>ne their own categories.

IT con<sup>fi</sup>guration options for Consumer Products Firm.

<table><tr><td>Configuration</td><td>Headquarters</td><td>European subsidiary</td><td>U.S. subsidiary</td></tr><tr><td>1</td><td>Platform 1</td><td>Platform 1</td><td>Platform 1</td></tr><tr><td>2</td><td>Platform 1</td><td>Platform 1</td><td>Platform 2</td></tr><tr><td>3</td><td>Platform 1</td><td>Platform 2</td><td>Platform 1</td></tr><tr><td>4</td><td>Platform 2</td><td>Platform 1</td><td>Platform 1</td></tr><tr><td>5</td><td>Platform 1</td><td>Platform 2</td><td>Platform 2</td></tr><tr><td>6</td><td>Platform 2</td><td>Platform 2</td><td>Platform 1</td></tr><tr><td>7</td><td>Platform 2</td><td>Platform 2</td><td>Platform 2</td></tr></table>

Note: While Consumer Products <sup>fi</sup>rm was seriously considering only the <sup>fi</sup>rst two option (shaded), our simulation would enable the <sup>fi</sup>rm to consider all seven options.

We further divided each type of event in Table 3 into categories based on the size and scope of requested changes, and estimates of corresponding cost/bene<sup>fi</sup>ts provided by Consumer Products Firm. Table 4 illustrates the change request data structure used in the simulation.

The cost parameters shown in Table 4 are expected values provided by the U.S. subsidiary of Consumer Products Firm, based on historical observations working with Platform 2 and estimates of what costs would be on Platform 1 (see Appendix B for estimates for HQ and European subsidiary). Ideally, costs would be exact rather than estimates, but in reality estimated costs often represent the best information <sup>fi</sup>rms have available when making decisions. Since there is uncertainty in cost estimates, we conduct simulations to test the robustness of a decision to variation in the cost, bene<sup>fi</sup>t and frequency of different types of change requests. Most importantly, our model is <sup>fl</sup>exible to accommodate any set of parameter values or project categorization schema. This allows for sensitivity analyses to evaluate the impact of variation in parameter values on infrastructure con<sup>fi</sup>guration decisions.

## 5.1. Simulation details

In this simulation we compare economic bene<sup>fi</sup>ts derived from the recommendations provided by our comprehensive MDP model that considers costs and bene<sup>fi</sup>ts simultaneously, with more limited recommendations that would result from a heuristic focusing primarily on IT cost (Heuristic A described below), or a heuristic focusing primarily on IT strategy (Heuristic B also described below).

In Heuristic A, IT is a cost center [17] and the objective is to minimize expenditure by simultaneously minimizing cost and deviations from de<sup>fi</sup>ned work <sup>fl</sup>ows that would require future system changes. This logic assumes that best practices have been identi<sup>fi</sup>ed and incorporated into existing systems (though the assumption was rarely tested). In our case study, we observed this heuristic at Equipment Firm and to a lesser extent at Parts Firm, where the CIOs believed that heavy investment in long-term infrastructure and tightly-integrated supply chains made frequent process changes undesirable.

In Heuristic B, IT is an enabler of value creation and the objective is to invest in systems that enable the <sup>fi</sup>rm to respond to rapidly evolving market conditions [32]. We observed this heuristic at the U.S. subsidiaries of Consumer Products Firm and Household Goods Firm. Firms with this mindset view IT investments as opportunities to create new processes and recon<sup>fi</sup>gure existing processes. While simplistic, these decision heuristics re<sup>fl</sup>ect views about the future business environment of the <sup>fi</sup>rm. Our simulation makes signi<sup>fi</sup>cant progress by simultaneously considering cost and value [31], in the same way that the supply chain ef<sup>fi</sup>ciency curve considers both ef<sup>fi</sup>ciency and responsiveness [2], and <sup>fi</sup>nancial portfolio theory considers both risk and return [25].

Table 3  
Events that can motivate changes to IT platforms.

<table><tr><td>Event type</td><td>Example</td><td>Source of benefit</td><td>Source of cost</td></tr><tr><td>New application</td><td>Installation of new application due to business or IT changes.</td><td>Value generated by new application.</td><td>Cost of installing new application on IT infrastructure.</td></tr><tr><td>Scaling</td><td>Increase in number of transactions due to changes in business conditions or extension into new markets.</td><td>Value generated by new transactions.</td><td>Cost of scaling IT infrastructure.</td></tr><tr><td>Integration</td><td>Need to integrate applications due to mergers, supply chain management initiatives, etc.</td><td>Value generated by improved information flow.</td><td>Cost of required integration.</td></tr><tr><td>System modification</td><td>Need to combine data from multiple formats as decision aids.</td><td>Value of improved decision-making.</td><td>Cost of modifying application to produce data in required format.</td></tr><tr><td>Security</td><td>Hacker attempts necessitate more robust firewall.</td><td>Potential negative impact on transaction volume and potential loss of valuable data.</td><td>Cost of procedures required to address threat and restore the IT infrastructure.</td></tr></table>

Note: Event types based on prior research [22].

## 5.2. Simulation and analysis

We compare the three decision rules described in Section 5.1 which we will refer to as minimum cost (Heuristic A), maximum responsiveness (Heuristic B), and MDP respectively. We assume that the actual number of change requests for each subsidiary in a given period (g ) follows a Poisson distribution with parameter λ. Baseline λ is set to the expected number of change requests given by Consumer Products Firm for each business unit. The value of λ is varied from 25% to 200% of the baseline value in 5% increments (36 design points). We further analyze the impact of changes in distribution of change requests across subsidiaries on the platform recommendation. The baseline distribution of change requests is set to the actual distribution of change requests based on information provided by Consumer Products Firm (25% from HQ, 30% from the European subsidiary, and 45% from the U.S. subsidiary). For ease of exposition, we hold the proportion of change requests from HQ constant and vary the distribution of the remaining 75% of change requests from 0% Europe/75% U.S. to 75% Europe/0% U.S. in 5% increments (15 design points). This yields 540 simulation design points. Assigning an expected cost and bene<sup>fi</sup>t to each change request was a two-stage process. First, the total number of change requests for each subsidiary is determined. Second, change requests are allocated proportionally to categories based on their relative frequency and then assigned a corresponding cost and bene<sup>fi</sup>t. Fig. 3 shows the recommendations (from the seven possible con<sup>fi</sup>gurations listed in Table 2) provided by the MDP for the different simulation design points.

Based on the expected rate and distribution of change requests (illustrated by the ‘bulls eye’ in Fig. 3), Consumer Products Firm is economically better off adopting Con<sup>fi</sup>guration 4, which allows the

U.S. subsidiary to remain on Platform 2. This decision would not change without a signi<sup>fi</sup>cant decrease in either the rate of change requests or in the distribution of change requests. Fig. 4 provides a more detailed look at the relative cost of following the cost minimization approach (Heuristic A) and the maximum responsiveness approach (Heuristic B), relative to recommendations provided by the MDP.

The costs shown in Fig. 4 represent the additional IT expense that Consumer Products Firm would incur as the volume of change requests varied from the current baseline level and the proportion of requests from each business unit remained constant at the current baseline level. For the cost minimization approach (Heuristic A) to be the most effective, total expected change requests would have to fall to less than 78% of current levels. For the maximum responsiveness approach (Heuristic B) to be the most effective, total change requests would have to increase to more than 165% of current levels. These thresholds coincide with instances where the minimum cost approach and the maximum responsiveness approach yield the same recommendation as the MDP approach

## 6. Managerial implications and future research

While senior managers are motivated to contain IT costs, they are also tasked to deploy IT to support the business in the various markets in which it competes. Our model enables <sup>fi</sup>rms to evaluate the <sup>fi</sup>nancial implications of alternative IT infrastructure con<sup>fi</sup>guration plans. In addition to identifying the best course of action for a set of circumstances, our model enables IT decision makers to identify the breakpoints that de<sup>fi</sup>ne when an alternate course of action should be taken. This is an important contribution because while prior research has shown that <sup>fi</sup>rms are motivated to either centralize or decentralize IT, the cost of making the wrong decision is high. Our model supports <sup>fi</sup>rms in the decision process by incorporating their own data and allowing them to include their own expectations of how future business conditions may impact the need to make IT changes.

Table 4  
Cost/bene<sup>fi</sup>t data structure for Consumer Products Firm U.S. subsidiary

<table><tr><td rowspan="2">Category index</td><td rowspan="2">Main category</td><td rowspan="2">Request size</td><td rowspan="2">Expected frequency (annually)</td><td colspan="2">Platform 1</td><td colspan="2">Platform 2</td></tr><tr><td>Expected cost ($k)</td><td>Expected benefit ($k)</td><td>Expected cost ($k)</td><td>Expected benefit ($k)</td></tr><tr><td>1</td><td>New application</td><td>Small</td><td>160</td><td>20</td><td>25</td><td>15</td><td>25</td></tr><tr><td>2</td><td>New application</td><td>Medium</td><td>40</td><td>80</td><td>100</td><td>50</td><td>100</td></tr><tr><td>3</td><td>New application</td><td>Large</td><td>8</td><td>300</td><td>400</td><td>150</td><td>400</td></tr><tr><td>4</td><td>Scaling</td><td>Small</td><td>40</td><td>15</td><td>25</td><td>15</td><td>25</td></tr><tr><td>5</td><td>Scaling</td><td>Medium</td><td>20</td><td>60</td><td>90</td><td>60</td><td>90</td></tr><tr><td>6</td><td>Scaling</td><td>Large</td><td>8</td><td>200</td><td>400</td><td>200</td><td>400</td></tr><tr><td>7</td><td>Integration</td><td>Small</td><td>120</td><td>10</td><td>15</td><td>5</td><td>15</td></tr><tr><td>8</td><td>Integration</td><td>Medium</td><td>20</td><td>80</td><td>150</td><td>30</td><td>150</td></tr><tr><td>9</td><td>Integration</td><td>Large</td><td>4</td><td>400</td><td>650</td><td>200</td><td>650</td></tr><tr><td>10</td><td>System modification</td><td>Small</td><td>120</td><td>10</td><td>15</td><td>5</td><td>15</td></tr><tr><td>11</td><td>System modification</td><td>Medium</td><td>40</td><td>15</td><td>20</td><td>10</td><td>20</td></tr><tr><td>12</td><td>System modification</td><td>Large</td><td>12</td><td>100</td><td>200</td><td>50</td><td>200</td></tr><tr><td>13</td><td>Security</td><td>Small</td><td>200</td><td>5</td><td>10</td><td>5</td><td>10</td></tr><tr><td>14</td><td>Security</td><td>Medium</td><td>24</td><td>20</td><td>45</td><td>20</td><td>45</td></tr><tr><td>15</td><td>Security</td><td>Large</td><td>4</td><td>110</td><td>280</td><td>110</td><td>280</td></tr></table>

![](/api/attachments/VTGXZKS2/fulltext/images/0094e30feae55b924ba5c8121863f047c7292f9ff426fcdcd3bd6e26db8a35d5.jpg)  
Fig. 3. MDP recommendations

Our model can also help <sup>fi</sup>rms to prepare long-range budgets. By having a better understanding of the rate of change requests across subsidiaries, and matching the IT infrastructure to re<sup>fl</sup>ect those requests, <sup>fi</sup>rms will have a better understanding of how to allocate resources to each subsidiary for future projects. For example, a <sup>fi</sup>rm may be better off with a centralized common infrastructure across all subsidiaries. However, one subsidiary might compete in a more dynamic environment, but not suf<sup>fi</sup>ciently dynamic to justify a decentralized IT infrastructure. As an alternative, that subsidiary would require a change request budget that is disproportionately large compared with its overall IT budget to accommodate the level of local responsiveness and innovation that it needs to succeed.

Our model is not without limitations in terms of implementation and external validation of recommendations. While an MDP approach ensures internal validity with respect to input parameters, the external validity of the model is dependent on whether future costs, bene<sup>fi</sup>ts and frequency of various change requests are consistent with historical and/or expected values. While decision-makers can conduct sensitivity analyses, our model can only provide an optimal investment policy based on available information, and the <sup>fi</sup>nal recommendation cannot be guaranteed optimal in the face of unknown future conditions. In addition, our MDP model assumes a stationary stochastic process over time. Even if costs, bene<sup>fi</sup>ts and frequency of change requests are consistent with expectations, an environmental shift to a nonstationary stochastic process would violate the assumptions of our model and justify the need for alternate solution methodologies.

However, an MDP approach does offer some advantages over other stochastic modeling techniques such as discrete event simulation and Markov Chains. First, while other techniques can evaluate the consequences of a fully speci<sup>fi</sup>ed model, they do not enable the optimization of that model because they evaluate one policy at a time. While many instances of the problem addressed in this manuscript could be addressed one policy at a time, testing every policy seems unnecessarily cumbersome. Second, the basic MDP approach is <sup>fl</sup>exible in that it can be easily modi<sup>fi</sup>ed to re<sup>fl</sup>ect in<sup>fi</sup>nite (or unknown) time horizons. While the actual solution algorithm would have to be changed, the overall model would not.

While our model provides useful information, there are opportunities for future research to make improvements on this model. For example, once one subsidiary is on a given platform, the incremental cost of placing another subsidiary on the same platform may decrease due to lower licensing fees, shared hardware, and shared expertise. A decision model that captures these non-linear costs would be very useful. In addition, our model assumes one-year time periods and that projects/programs are completed during each time period. In fact, many of the largest IT projects span multiple years, which can impact budget allocations and recognition of bene<sup>fi</sup>ts. Incorporating projects spanning multiple time-periods into a framework for valuing IT infrastructure <sup>fl</sup>exibility would also be a useful topic for future research.

In conclusion, executives responsible for IT governance seek to minimize technology costs, while ensuring that the infrastructure can accommodate increasing utilization, new software applications, and modi<sup>fi</sup>cations to existing software applications. To address this challenge, we used interviews with executives from four Fortune 200 Global <sup>fi</sup>rms to develop a discrete-time, <sup>fi</sup>nite-horizon Markov decision model to identify the most economically-bene<sup>fi</sup>cial IT infrastructure con<sup>fi</sup>guration from a set of alternatives. Our decision model enables <sup>fi</sup>rms to evaluate the costs and bene<sup>fi</sup>ts associated with alternative IT infrastructure designs, under varying degrees of centralized/decentralized IT control. Our model and <sup>fi</sup>ndings will be useful as <sup>fi</sup>rms continue to expand their operations to compete in the global marketplace.

![](/api/attachments/VTGXZKS2/fulltext/images/f91b6ac20e3c3fbc23c3adbfe55c339c075d4beb1b4dffa8c75750fd2347164e.jpg)  
Change request volume relative to expectations  
Fig. 4. Additional seven year cost of alternate decision rules relative to MDP.

## Acknowledgments

We thank the participating executives for the insights and details on their <sup>fi</sup>rms and IT decision-making processes. We thank Mälardalen University in Västerås, Sweden for its hospitality during data collection in Northern Europe. Financial support was provided in part by the Handelsbanken Foundation and the University of Richmond Robins School of Business.

## Appendix A. Sample questions for semi-structured interviews

## A.1. Headquarters questions

1. What are the strategy and goals for the company as a multi-national corporation (MNC)?

2. What challenges does the company face in achieving its strategy and goals?

3. How does the company work to address these challenges [using organizational structure, IT systems, and/or business process changes]?

4. How does the company evaluate the success/failure of its initiatives [organizational, IT, business process]?

5. From the perspective of the <sup>fi</sup>rm, what is the desired relationship between headquarters and subsidiaries?

6. What type of information needs to be exchanged between headquarters and subsidiaries to establish and maintain this relationship?

7. Do headquarters and subsidiaries share a common view on the desired relationship and the need for information exchange?

8. Are there barriers to a common view and/or information exchange? If so, what are the barriers? How is the company working to overcome the barriers?

## A.2. Subsidiary questions

1. Which of the functions listed below are performed at the subsidiary level? Are the associated business processes unique to the subsidiary, or are the processes based on headquarters directives?

## Appendix B. Cost, bene<sup>fi</sup>t, and project frequency parameter

a. R&D/product design

b. Procurement

c. Production/manufacturing

d. Marketing/advertising

e. Sales/service

f. IT/IS

g. Finance/accounting

h. HR

i. Other

2. Please brie<sup>fl</sup>y describe the current IT/IS at the subsidiary level:

a. Network/intranet

b. Data center

c. ERP

d. Procurement

e. Supply chain management

g. CRM

f. Warehousing/distribution

h. Electronic commerce

i. Major initiatives underway

j. Other

3. What are the general strategy and goals for the subsidiary? How are these related to the <sup>fi</sup>rm's global strategy? How does the IT/IS function support the subsidiary's goals?

4. From the subsidiary's perspective, what is the desired relationship between the subsidiary and headquarters?

5. What type of information is exchanged with headquarters? What type of information is exchanged with other subsidiaries? Are there any barriers to information exchange, and if so, how does the subsidiary work to overcome these barriers?

6. Are there any local market aspects that have had a great impact on the current IT/IS state? Are there any corporate functions (see list under subsidiary question 1 above) that present unique requirements for the current IT/IS state?

7. Where are the major of high-level IT/IS decisions made — at the subsidiary or at headquarters? What role does your position play to de<sup>fi</sup>ne the information and application architecture? To what extent do IT/IS and executive leadership in other areas collaborate to de<sup>fi</sup>ne architecture and application strategy and implementation?

Table B1  
Cost/bene<sup>fi</sup>t data structure for Consumer Products Firm HQ.

<table><tr><td rowspan="2">Category index</td><td rowspan="2">Main category</td><td rowspan="2">Request size</td><td rowspan="2">Expected frequency (annually)</td><td colspan="2">Platform 1</td><td colspan="2">Platform 2</td></tr><tr><td>Expected cost ($k)</td><td>Expected benefit ($k)</td><td>Expected cost ($k)</td><td>Expected benefit ($k)</td></tr><tr><td>1</td><td>New application</td><td>Small</td><td>80</td><td>20</td><td>25</td><td>15</td><td>25</td></tr><tr><td>2</td><td>New application</td><td>Medium</td><td>20</td><td>80</td><td>100</td><td>50</td><td>100</td></tr><tr><td>3</td><td>New application</td><td>Large</td><td>5</td><td>300</td><td>400</td><td>150</td><td>400</td></tr><tr><td>4</td><td>Scaling</td><td>Small</td><td>24</td><td>15</td><td>25</td><td>15</td><td>25</td></tr><tr><td>5</td><td>Scaling</td><td>Medium</td><td>12</td><td>60</td><td>90</td><td>60</td><td>90</td></tr><tr><td>6</td><td>Scaling</td><td>Large</td><td>4</td><td>200</td><td>400</td><td>200</td><td>400</td></tr><tr><td>7</td><td>Integration</td><td>Small</td><td>80</td><td>10</td><td>15</td><td>5</td><td>15</td></tr><tr><td>8</td><td>Integration</td><td>Medium</td><td>10</td><td>80</td><td>150</td><td>30</td><td>150</td></tr><tr><td>9</td><td>Integration</td><td>Large</td><td>4</td><td>400</td><td>650</td><td>200</td><td>650</td></tr><tr><td>10</td><td>System modification</td><td>Small</td><td>60</td><td>10</td><td>15</td><td>5</td><td>15</td></tr><tr><td>11</td><td>System modification</td><td>Medium</td><td>20</td><td>15</td><td>20</td><td>10</td><td>20</td></tr><tr><td>12</td><td>System modification</td><td>Large</td><td>5</td><td>100</td><td>200</td><td>50</td><td>200</td></tr><tr><td>13</td><td>Security</td><td>Small</td><td>200</td><td>5</td><td>10</td><td>5</td><td>10</td></tr><tr><td>14</td><td>Security</td><td>Medium</td><td>24</td><td>20</td><td>45</td><td>20</td><td>45</td></tr><tr><td>15</td><td>Security</td><td>Large</td><td>4</td><td>110</td><td>280</td><td>110</td><td>280</td></tr></table>

Cost/bene<sup>fi</sup>t data structure for Consumer Products Firm European subsidiary.

<table><tr><td rowspan="2">Category index</td><td rowspan="2">Main category</td><td rowspan="2">Request size</td><td rowspan="2">Expected frequency (annually)</td><td colspan="2">Platform 1</td><td colspan="2">Platform 2</td></tr><tr><td>Expected cost ($k)</td><td>Expected benefit ($k)</td><td>Expected cost ($k)</td><td>Expected benefit ($k)</td></tr><tr><td>1</td><td>New application</td><td>Small</td><td>80</td><td>30</td><td>40</td><td>25</td><td>40</td></tr><tr><td>2</td><td>New application</td><td>Medium</td><td>20</td><td>125</td><td>150</td><td>125</td><td>150</td></tr><tr><td>3</td><td>New application</td><td>Large</td><td>4</td><td>450</td><td>600</td><td>225</td><td>600</td></tr><tr><td>4</td><td>Scaling</td><td>Small</td><td>12</td><td>25</td><td>40</td><td>25</td><td>40</td></tr><tr><td>5</td><td>Scaling</td><td>Medium</td><td>6</td><td>90</td><td>135</td><td>100</td><td>135</td></tr><tr><td>6</td><td>Scaling</td><td>Large</td><td>4</td><td>300</td><td>600</td><td>300</td><td>600</td></tr><tr><td>7</td><td>Integration</td><td>Small</td><td>50</td><td>15</td><td>25</td><td>5</td><td>25</td></tr><tr><td>8</td><td>Integration</td><td>Medium</td><td>6</td><td>120</td><td>225</td><td>50</td><td>225</td></tr><tr><td>9</td><td>Integration</td><td>Large</td><td>4</td><td>600</td><td>1000</td><td>300</td><td>1000</td></tr><tr><td>10</td><td>System modification</td><td>Small</td><td>60</td><td>15</td><td>25</td><td>5</td><td>25</td></tr><tr><td>11</td><td>System modification</td><td>Medium</td><td>40</td><td>25</td><td>30</td><td>25</td><td>30</td></tr><tr><td>12</td><td>System modification</td><td>Large</td><td>4</td><td>150</td><td>300</td><td>75</td><td>300</td></tr><tr><td>13</td><td>Security</td><td>Small</td><td>200</td><td>10</td><td>15</td><td>10</td><td>15</td></tr><tr><td>14</td><td>Security</td><td>Medium</td><td>24</td><td>30</td><td>75</td><td>30</td><td>75</td></tr><tr><td>15</td><td>Security</td><td>Large</td><td>4</td><td>175</td><td>400</td><td>175</td><td>400</td></tr></table>

## Appendix C. Value iteration algorithm

There are many algorithms that are used to arrive at solutions to MDPs, and the speci<sup>fi</sup>c algorithm chosen often depends on the nature and size of the problem. Two common methods are value iteration and policy iteration. Value iteration is the procedure that evaluates the utility of each state by using the utilities of the adjacent states,

$$
\operatorname{Max} _ {S ^ {i}} \left| U (S ^ {i}) - U ^ {\prime} (S ^ {i}) \right| <   \varepsilon
$$

where ε is a predetermined threshold value. As the threshold value is decreased, the algorithm becomes more precise but solution time increases. Given a utility matrix, value iteration identi<sup>fi</sup>es a corresponding policy based on maximum expected utility (i.e. there is no guarantee that the actual outcome equate to the maximum expected utility). The basic structure of the value iteration algorithm is:

Function: Value iteration (P, R) returns a utility matrix

Inputs: P (a transition probability matrix)

R (a reward matrix)

Variables: U (initially equal to R), U′ (initially equal to R)

For each state i, do:

$$
U ^ {\prime} (S ^ {i}) \leftarrow R \left(S _ {i} + \max _ {a} \sum_ {j} P _ {i j} ^ {a} U (S _ {j}) \right.
$$

$$
\begin{array}{c} \text {End} \\ \text {Until} \\ \operatorname * {M a x} _ {S ^ {i}} \left| U (S ^ {i}) - U ^ {\prime} (S ^ {i}) \right| <   \varepsilon \\ \text {Return} U. \end{array}
$$

In contrast to value iteration, policy iteration is generally used to solve in<sup>fi</sup>nite horizon MDPs with <sup>fi</sup>nite state and action sets. Policy iteration was not used because it is not an ef<sup>fi</sup>cient approach to solving <sup>fi</sup>nite horizon MDPs. However, the fundamental problem in this paper might change to re<sup>fl</sup>ect an unknown time horizon (i.e. not arbitrarily capped at something “reasonable”), in which case a decision analyst would have to change to a policy iteration algorithm in order to <sup>fi</sup>nd a solution. Readers interested in learning more about Markov Decision Processes and solution algorithms are encouraged to begin with the seminal work of Martin Puterman whose 1994 book titled “Markov

Decision Processes: Discrete Stochastic Dynamic Programming” provided the basis for the solution algorithm described above.

## References

[1] C.A. Bartlett, S. Ghoshal, Managing Across Borders: The Transnational Solution, Harvard Business School Publishing, Boston, MA, 1989.

[2] B.M. Beamon, Measuring supply chain performance, International Journal of Operations & Production Management 19 (3) (1999) 275–292.

[3] M.-C. Boudreau, K.D. Loch, D. Robey, D. Straub, Going global: using information technology to advance the competitiveness of the virtual transnational organization, Academy of Management Executive 12 (4) (1998) 120–128.

[4] R.G. Burgess, In the Field: An Introduction to Field Research, Routledge, New York, 1984.

[5] S. Casolari, M. Colajanni, Short-term prediction models for server management in Internet-based contexts, Decision Support Systems 48 (1) (2009) 212–226.

[6] R.E. Caves, Multinational Enterprise and Economic Analysis, Cambridge University Press, Cambridge, UK, 2007.

[7] A.D. Chandler, The functions of the HQ unit in the multibusiness <sup>fi</sup>rm, Strategic Management Journal 12 (1) (1991) 31–50.

[8] D. Collis, D. Young, M. Goold, The size, structure, and performance of corporate headquarters, Strategic Management Journal 28 (4) (2007) 383–405.

[9] P. Cragg, M. King, H. Husnayati, IT alignment and <sup>fi</sup>rm performance in small manufacturing <sup>fi</sup>rms, Journal of Strategic Information Systems 11 (2) (2002) 109–132.

[10] L. Dubé, G. Paré, Rigor in information systems positivist case research: current practices, trends and recommendations, MIS Quarterly 27 (4) (2003) 597–635.

[11] K.M. Eisenhardt, M.E. Graebner, Theory building from case studies: opportunities and challenges, Academy of Management Journal 50 (1) (2007) 25–32.

[12] X. Fang, O. Sheng, R. Liu, P. Goes, When is the right time to refresh knowledge discovered from data? Operations Research 61 (1) (2013) 32–44.

[13] P. Finnegan, S.N. Longaigh, Examining the effects of information technology on control and coordination relationships: an exploratory study in subsidiaries of pannational corporations, Journal of Information Technology 17 (3) (2002) 149–163.

[14] P. Ghemawat, Managing differences: the central challenge of global strategy, Harvard Business Review 85 (3) (2007) 58–68.

[15] V. Grover, R.M. Henry, J.B. Thatcher, Fix IT–business relationships through better decision rights, Communications of the ACM 50 (12) (2007) 80–86.

[16] B. Gu, L. Xue, G. Ray, IT infrastructure governance and IT investment performance: an empirical analysis, Proceedings of the International Conference on Information Systems, (Paris, France, 2008), 2008

[17] J.C. Henderson, N. Venkatraman, Strategic alignment: leveraging information technology for transforming organizations, IBM Systems Journal 32 (1) (1993) 472–484.

[18] L.M. Hitt, E. Brynjolfsson, Information technology and internal <sup>fi</sup>rm organization: an exploratory analysis, Journal of Management Information Systems 14 (2) (1997) 81–101.

[19] S. Jarvenpaa, B. Ives, Organizing for global competition: the <sup>fi</sup>t of information technology, Decision Sciences 24 (3) (1993) 547–580.

[20] G.S. Kearns, R. Sabherwal, Strategic alignment between business and information technology: a knowledge-based view of behaviors, outcome, and consequences, Journal of Management Information Systems 23 (3) (2006) 129–162.

[21] J.Y. Kim, K. Altinkemer, A. Bibi, Yield management of workforce for IT service workers Decision Support Systems 53 (1) (2012) 23-33

[22] R.L. Kumar, A framework for assessing the business value of information technology infrastructures, Journal of Management Information Systems 21 (2) (2004) 11–32.

[23] A. Langley, Strategies for theorizing from process data, Academy of Management Review 24 (4)(1999) 691–710

[24] C.C.H. Law, E.W.T. Ngai, ERP systems adoption: an exploratory study of the organizational factors and impacts of ERP success, Information & Management 44 (4) (2007) 418–432.

[25] H.M. Markowitz, Portfolio selection, Journal of Finance 7 (1) (1952) 77–91.

[26] P. Neirotti, E. Paolucci, Assessing the strategic value of information technology: an analysis on the insurance sector, Information & Management 44 (6) (2007) 568–582.

[27] D. Nemati, D.M. Steiger, L.H. Iyer, R.T. Herschel, Knowledge warehouse: an architectural integration of knowledge management, decision support, arti<sup>fi</sup>cial intelligence and data warehousing, Decision Support Systems 33 (2) (2002) 143–161.

[28] N. Nohria, S. Ghosal, The Differentiated Network — Organizing Multinational Corporations for Value Creation, Jossey-Bass, San Francisco, 1997.

[29] A.W. Rohm, G. Pernul, COPS: a model and infrastructure for secure and fair electronic markets, Decision Support Systems 29 (4) (2000) 343–355.

[30] J.W. Ross, P. Weill, Six decisions your IT people shouldn't make, Harvard Business Review 80 (11) (2002) 84–95.

[31] R.T. Rust, C. Moorman, P.R. Dickson, Getting return on quality: revenue expansion, cost reduction, or both? Journal of Marketing 66 (4) (2002) 7–24.

[32] V. Sambamurthy, A. Bharadwaj, V. Grover, Shaping agility through digital options: reconceptualizing the role of information technology in contemporary <sup>fi</sup>rms, MI Quarterly 27 (2) (2003) 237–263.

[33] A. Sen, A.P. Sinha, IT alignment strategies for customer relationship management, Decision Support Systems 51 (3) (2011) 609–619.

[34] S. Senft, F. Gallegos, in: Taylor & Francis (Ed.), Information Technology Control and Audit, Third edition, 2009, (London).

[35] D. Shpilberg, S. Berez, R. Puryear, S. Shah, Avoiding the alignment trap in information technology, MIT Sloan Management Review 49 (1) (2007) 51–58.

[36] J. Simonsen, Involving top management in IT projects, Communications of the ACM 50 (8) (2007) 53–58.

[37] E.T.G. Wang, J.H.F. Chen, The in<sup>fl</sup>uence of governance equilibrium on ERP project success, Decision Support Systems 41 (4) (2006) 708–727.

[38] H.J. Watson, C. Fuller, T. Ariyachandra, Data warehouse governance: best practices at Blue Cross and Blue Shield of North Carolina, Decision Support Systems 38 (3) (2004) 435–450.

[39] C.L. Wilkin, R.H. Chenhall, A review of IT governance: a taxonomy to information accounting information systems, Journal of Information Systems 24 (2) (2010) 107–146.

[40] R.K. Yin, Case Study Research: Design and Methods, Fourth Edition ed. Sage Publications, Thousand Oaks, CA, 2009.

Steven Thompson is a faculty in the Management Department of the Robins School of Business at the University of Richmond. Prior to his academic career he worked 10 years in the healthcare industry. His current research is focused on health care information technology, health care systems engineering, and the use of information technology to coordinate inter-organizational operations. His research has been published in leading academic journals such as Operations Research, Information Systems Research, Communications of the ACM, Decision Sciences, and Decision Support Systems Journal. Steven earned a PhD, MBA, and B.S.N. from the University of Connecticut.

Peter Ekman is an Assistant Professor at Mälardalen University. He earned his master's degree at Stockholm University and his Doctoral degree at Mälardalen University in cooperation with the Swedish Research School of Management and Information Technology. Prior to his academic career, Peter worked for several years in technical manufacturing and consulting. His research is focused on the intersection of marketing, international business, and information systems

Daniel Selby is an assistant accounting professor in the Robins School of Business at the University of Richmond. Daniel holds a current Certi<sup>fi</sup>ed Information Systems Auditor license and active Certi<sup>fi</sup>ed Public Accountant licenses in California and Florida. He has more than 11 years of corporate accounting, public accounting and corporate information systems practice experience. He has published and presented the results of his research domestically and internationally. Daniel earned a PhD and Master's degree in Accounting Information Systems from Florida State University and a BS degree in Accounting from Norfolk State University.

Jonathan Whitaker is a faculty in the Management Department of the Robins School of Business at the University of Richmond. Prior to his academic career, he worked 10 years in consulting and professional services with A.T. Kearney and Price Waterhouse, including project work in North America, Europe and Asia. Jonathan earned a PhD from the University of Michigan, an MBA from the University of Chicago, and a BA from the University of Southern California. His academic research has been published in leading academic journals such as Information Systems Research, Journal of Management Information Systems, and Production and Operations Management, and pro<sup>fi</sup>led in the Wall Street Journal and MIT Sloan Management Review.
