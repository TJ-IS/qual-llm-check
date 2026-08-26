---
otero_id: 19064
otero_key: "3FFYP564"
title: "Managing organizational DSS development in small manufacturing enterprise"
authors: "M.M.C. Tam; W.W.C. Chung; K.L. Yung; A.K. David; K.B.C. Saxena"
year: "1994"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)90005-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Case Study

# Managing organizational DSS development in small manufacturing enterprise

M.M.C. Tam, W.W.C. Chung, K.L. Yung and A.K. David

Hong Kong Polytechnic, Hong Kong

K.B.C. Saxena

Erasmus University, Rotterdam, The Netherlands

A number of Hong Kong manufacturing companies have moved their production to the People's Republic of China while retaining their supporting functions (such as marketing, distribution, etc.) in Hong Kong. As a consequence, their mode of operation has become more complex and demands better production planning and control (PPC). One solution is to use an information system in which all factory resources are integrated within a single framework for PPC. The main instrument of this strategy is an Organizational DSS (ODSS). This paper presents a case study of development and adoption of an ODSS in a small manufacturing enterprise. Analysis of the findings highlights the cultural as well as organizational underpinnings and the need for effective intervention before and throughout the computerization. The implementation strategies are described, with emphasis on prerequisite infrastructural developments, showing how they provide opportunities and constraints.

Keywords: Organizational decision support system (ODSS); Small manufacturing enterprise; Case study; Information systems development; Technology adoption; Production planning and control (PPC); Industrial collaboration; Technology transfer.

## 1. Introduction

The Hong Kong manufacturing industry has always been export-oriented, and its success has been attributed to its flexibility and adaptability to frequent changes of market demands, its versatility, and industrious human resources. However, there are threats to its competitive edge due to competition from other South East Asian countries and more fragmented and volatile market demands, accompanied by technology advancements. In response, a number of Hong Kong-based manufacturing companies have moved (or in the process of moving) their production facili-

![](/api/attachments/3FFYP564/fulltext/images/a29b5f5f5daa038b4209c75d1360f9795d26c17dd8117243b457ebdbb83e3297.jpg)

Migar Tam is a graduate in Manufacturing Engineering and is currently a doctoral candidate working on Decision Support Systems (DSS) in manufacturing management at Hong Kong Polytechnic. His research interests are in Organizational DSS, small manufacturing enterprises, and system development case studies; and he has published several papers in these areas.

![](/api/attachments/3FFYP564/fulltext/images/9e1550f0e3413b2d643b4f99989caac5969cf7202efd25df25ec4ed93163c19a.jpg)

K.B.C. Saxena is an Assistant Professor of Information Systems at the Rotterdam School of Management, Erasmus University, Rotterdam, Netherlands since July 1992. Prior to this he was a Reader in the Department of Computing at the Hong Kong Polytechnic. He received a B.Sc. and an M.Sc. from Lucknow University, India and a Ph.D. in Management from Gujarat University, India. He has more than 22 years of research, teaching and industrial experience in

The field of information systems and has published more than 50 papers on management support systems and information systems management. He is a member of the British Computer Society, Association of Computing Machinery (USA), Society for Information Management (USA), Information Resources Management Association (USA), The Institute of Management Sciences (USA) and the International Society for Decision Support Systems (USA).

ties to the People's Republic of China (PRC) and other South East Asian countries to take advantage of abundant and relatively cheap labour force, etc. [9]. However, they are still Hong Kong-based in their support functions, such as

![](/api/attachments/3FFYP564/fulltext/images/1f696ec71dc796fe2c1fe0f146774974a83c79c8fd5012fd643657402b169d24.jpg)

W.W.C. Chung is a Lecturer of the Department of Manufacturing Engineering, Hong Kong Polytechnic. He has over 20 years of experience in consulting, research and teaching a wide range of topics in the general areas of project management. He graduated Honours Class One in Industrial Engineering and obtained a Master's Degree in Business Administration from the University of New South Wales, Australia. He had Industrial Engineering experience be fore returning to Hong Kong and took up his present position. Mr. Chung has assisted over 30 Hong Kong companies in the concurrent design, development and implementation of manufacturing information systems. He is involved in systems integration consultancy assignments. At present, he is both an academic research supervisor and a Project Director in charge of consultancy contracts in managing emerging technologies for organizational innovation of two companies. He is a corporate member of the Institution of Engineers, Australia, a member of the Institute of Management Services, U.K. and also a member of the Institute of Logistics and Distribution Management, U.K.

![](/api/attachments/3FFYP564/fulltext/images/c8c32ae0bd05089e04b8d7b7da22c834e2459e5448c8a21129ff2cd45bc9a807.jpg)

K.L. Yung had graduated from Hong Kong Technical College (now converted to Hong Kong Polytechnic) in Mechanical Engineering and worked for two years in oil hydraulics. In 1972 he went to the United Kingdom to study for B.Sc. (Hons.) in Electronics and then continued on to M.Sc. in Control Systems and Ph.D. in Microprocessor Applications. After graduation, he has been working in the U.K. for firms such as B.O.C. Advanced Welding Ltd., Ceramic Engineering

Co. Ltd. (British Ever Ready Electric Group) and CUPE at Cranfield Institute of Technology. In 1986, he went back to Hong Kong and worked briefly for the Hong Kong Productivity Council as Consultant before joining the Hong Kong Polytechnic as Senior Lecturer. His experience and research interest include precision engineering, information technology and automation. He is the supervisor of several collaborative M.Ph. and Ph.D. programs with industry in the automation of information exchange and manufacturing management using computers.

![](/api/attachments/3FFYP564/fulltext/images/ae5eed9c4984023e5091e9b3b32a5e6027c14a95e48903105d3764364b8422e2.jpg)

A.K. David is a Reader in the Department of Electrical Engineering, Hong Kong Polytechnic. He graduated with a First Class Honours Degree in Electrical Engineering from the University of Ceylon and obtained a Ph.D. from Imperial College, University of London. He has taught and researched in four continents and has been a part time Director of the Ceylon Electricity Board. His principal research interests are in Electrical Power Engineering and computer applications in power systems. He has over 75 papers in journals and conferences and has co-edited a book.

marketing, purchasing, distribution and engineering. This mode of operation is complex and demands the local manufacturing office to liaise with their remote production plants in production planning and control (PPC). For example, there are problems related to the planning of materials, dispatching jobs for production, and quality assurance. In fact, the rationalization of the whole PPC function can be troublesome and time consuming.

Confronting with these challenges, the manufacturing executives call for the use of a Decision Support System (DSS) to assist timely decision making in response to the fast-changing market. A DSS is an interactive Information Technology-based system. It is designed to make adequate provisions for effective decision making. If a DSS is in place, these manufacturing executives would use it as a vehicle to “supply the relevant information to offer guides to a decision that commits peoples at the various levels of a manufacturing operation in providing resources to do work” [7].

Table 1 highlights the typical uses of DSS in PPC. These DSS applications are not limited to individual uses. As recent advances in Information Technology have made it possible to broaden the scope of a DSS to include support for group decisions, and even organizational decisions, organizational DSS (ODSS) begins to draw contemporary research interest $[5,13,22,33]$ . In order to better relate the conceptualization of ODSS to PPC, some examples in PPC that match with the scholarly definitions of ODSS are identified and they are summarized in Table 2.

Our past attempts to conceptualize ODSS in the above PPC context teach us that an ODSS can be characterized by the followings: (1) its support orientation towards distributed decision making, coordination and cooperative work; (2) its development process which capitalises on state-of-art Information Technology; (3) and the requirement for effective intervention for its institutionalization [30]. These characteristics can be used as guidelines in making adequate provision for effective organizational decision making in PPC.

Table 1  
Typical use of DSS in production planning and control (PPC).

<table><tr><td>Department</td><td>Example use of DSS</td></tr><tr><td>Engineering</td><td>Product configuration management</td></tr><tr><td>Production Planning</td><td>Plan the physical manufacturing</td></tr><tr><td>Production Control</td><td>Plan materials supply and processing</td></tr><tr><td>Purchasing</td><td>ABC analysis</td></tr><tr><td>Shop Floor Control</td><td>Execute production control plan</td></tr><tr><td>Inventory Control</td><td>Control and monitor materials</td></tr><tr><td>Marketing</td><td>Sales forecast</td></tr></table>

Table 2  
Some scholarly definitions of ODSS and corresponding examples in manufacturing management, extracted from [31].

<table><tr><td>Extracted similarities of scholarly definitions</td><td>Examples in manufacturing</td></tr><tr><td>People from different groups enter into an activity or decision process, i.e. the range of decision makers exceeds any specific group.</td><td>Production Planning and Control, New product development, etc.</td></tr><tr><td>The focus of an ODSS is an organizational task or activity or a decision that affects several organizational units.</td><td>Marketing, Purchasing, Production, Engineering, etc.</td></tr><tr><td>The ODSS supports people from different groups and provides information which is used across multiple independent activities or decisions, i.e. the range of users exceeds any specific group.</td><td>Production scheduler, work order dispatcher, shop floor supervisor, etc.</td></tr></table>

Firstly, distributed decision making, coordination and cooperative work are of paramount importance in PPC. In production management domain, distributed decision making is often required where a set of related decisions is distributed among a set of organizational decision makers and needed to be coordinated. Coordination will mean the act of managing interdependence between various decision making activities of various decision makers. This interdependence may be of various types $[19]$ such as Prerequisite, Shared Resources, Simultaneity. Some examples are shown in Table 3.

Secondly, building an ODSS and getting it implemented are challenging tasks as these involve a range of technologies $[5,26]$ (e.g., data base, model base, user interface, communication technology, etc.). Large multinational organizations are more likely to have a sophisticated Information Technology infrastructure and the expertise needed to develop their own ODSS and use it effectively. However, most organizations in Hong Kong are small and may not have such expertise [7,29].

Thirdly, institutionalization of an ODSS may present another kind of challenge in terms of infrastructural development and management of organizational change. Some considerations relevant to infrastructural aspects are listed below:

\- The development of ODSS can be based on personal computer technology. It is well within the budget of even a small manufacturing enterprise (SME).

\- There are a number of techniques encouraging end user participation and design [11,35], production staff may use these techniques to develop their own ODSS prototypes. By doing so, they are able to adapt, in-time, to handle new procedures and especially to changes brought about by new orders. They may also rely on their own user-oriented DSS [32] to update the information and maintain system integrity.

Table 3  
Examples of distributed decision making and the nature of decision support in manufacturing, adapted from [31].

<table><tr><td></td><td>Prerequisite</td><td>Shared resources</td><td>Simultaneity</td></tr><tr><td>Operational definition</td><td>Output of one activity is required by the next activity.</td><td>Resources required by occur at the same time.</td><td>More than one activity must occur at the same time.</td></tr><tr><td>Examples in manufacturing</td><td>Parts must be delivered in time to be used.</td><td>Two parts made of the same material.</td><td>Line balancing.</td></tr><tr><td>Example of coordination</td><td>Moving information from one activity to another, JIT.</td><td>Allocate resources.</td><td>Synchronizing the activities of preceding work stations.</td></tr><tr><td>Nature of decision support</td><td>Ordering decisions, information sharing.</td><td>Negotiated Choice.</td><td>Synchronous information sharing.</td></tr></table>

\- Inevitably, technology awareness is necessary for its adoption. It can be transferred from a Higher Educational Institution to a collaborative organization [6], thereby ensuring the technical competence of the design and on-going development of the ODSS.

These considerations are conducive to management of technological change. However, recognition of a technology as beneficial does not guarantee its adoption [34]:

\- the potential adopters may not see a need for the technology;

\- the contextual factors may not require the technology;

\- potential adopters may not know how to realize the promise.

Further, organizational members at different levels, may perceive different needs. Technology adoption is therefore more difficult if the technology requires organization-wide commitment, and ODSS is one such example. The potential adopters' concern such as need, wish, aim, interest and necessity, are all action-directed measures that reflect the attitude towards adoption and implementation of a technology. An understanding of these factors is required to enhance the impact of the technology on its target adopters [16].

## 2. The organization under study

## 2.1. Company background

The company used in this case study was established in 1960. Its major products are home electrical appliances; its markets are in the U.S.A. and Europe. The customers are mainly large buying houses and hollow manufacturers, therefore their stock policy is largely customer-order-driven.

The company is a family business characterized by Chinese style management, involving: internal harmony preserving, conflict avoidance, and emphasis on cooperation and synergy, etc. [8]. It has been enjoying a relatively stable work force (most employees have been with the company over 10 years). The company was one of the manufacturers that moved their production base to China and run their operations by remote control mode. All production units (e.g. fabrication shop and assembly line) except the mould making function, are now in China. All non-production functions (e.g. Marketing, Engineering, Purchasing, Production Planning and Control and Accounting) remained in Hong Kong. Now, they are about 50 staff in the Hong Kong office, while the plants in China employ more than 2000 workers in peak seasons.

![](/api/attachments/3FFYP564/fulltext/images/c42cf025188e46e22ab09260558872a71e15e0f5cf7ed4efbdbc16047ca18a0e.jpg)  
Fig. 1a. A schematic diagram of project control in PPC operations.

![](/api/attachments/3FFYP564/fulltext/images/1fb011964ad83a87edf2494c97b4421844619442eb09664a9107ff58f58d260f.jpg)  
Fig. 1b. PPC control mechanism (simplified) involved in the remote plants.

The company had tried to implement company-wide computerization (mainly personal computers) but this was not successful. The production dropped to one fourth during that period. The project was abandoned after six months and the electronic data processing department was closed. Only a few modules for production control, and Bill-of-Material (BOM) processing were still used. Because of this, a very conservative approach towards computerization was taken in subsequent attempts.

## 2.2. Scope of the study

The operations of the company were dependent on three factors:

\- Remote control

\- Vertical manufacturing

\- Original equipment manufacturing

Because of these factors, the management of the company was intertwined with considerations of its financial situations, project control, order control and material control. But project control was most important, as it could affect customer service. In spite of this, each project was considered generically similar, see Figure 1a.

The identification of project control points followed the order cycle. It was realized that every production unit (i.e., remote plant) was regarded as a black box, while stock control points were monitored before and after each box (see Figure 1b). Such decomposition of the overall PPC structure was based on the assumption that complexity could be reduced by self-contained sub-systems with clear and well defined operational characteristics [4]. Operational planning and control were achieved by work order release functions and inventory controls that were to be supported by other related work documents (e.g., materials list and manufacturing instruction). Project control was achieved at higher aggregated levels: typically at the final assembly schedule. The scope of our study was limited to the manufacturing operations (mainly PPC) in Hong Kong. Even though shop floor decisions and activities are excluded, the activities are still very complex. They are summarized in Table 4. The interdependence of the activities highlights the need for coordinating decision-making in different departments.

## 2.3. Problems in the operations

As a consequence of the relocation of plants to China, the staff in the PPC had to monitor a wider span of activities in geographically separated plants. Therefore, both focus of control and field of actions had diverged. The planning for day-to-day production was not easy. The PPC function was consistently criticized as the bottleneck that hampered production. This could partly be attributed to the increase in work load. But the management's main concern was frequent stoppage in the production plants in China due to lack of materials supply. The apparent reason was either a delay in material delivery, or a tendency for one or two items missing in the delivery. However this only became apparent after production began. On the other side, the PPC staff complained that information for decision making did not reflect the real production situation. Some apparent reasons were:

Table 4  
PPC operations in the case organization, an activity based summary.

<table><tr><td>Production control</td><td>Stock control</td><td>Purchasing</td></tr><tr><td>- evaluate production capacity</td><td>- ensure parts availability</td><td>- place purchase orders</td></tr><tr><td>- prepare production schedule</td><td>- execute ordering rules</td><td>- progress purchase orders</td></tr><tr><td>- release work order</td><td>- vet parts and materials</td><td>- expedite deliveries</td></tr><tr><td>- report production status</td><td>- report parts shortage</td><td>- vendor analysis</td></tr></table>

(a) Data discrepancy. Inventory data kept in the warehouse was different from that in production planning. This was also different from that in the production plants in China. No one set of data was complete, and no one set of data could be trusted for purpose of planning and control. Similar problems were found in the data on work-in-progress, material-in-transit, conversion factor, consumption rate, etc.

(b) Staggered production. Production managers claimed that the production plants in China were about to stop because of material shortage and requested the PPC in Hong Kong for immediate release of materials and arrangements for urgent delivery of materials to plants in China. There was no way to verify such requests and assess the impact of a “considered” response.

(c) Difficulties in tracking material progress. PPC staff had to keep track of all materials movement (routed from Hong Kong to China and back); the corresponding work documents needed to be cross checked. The documents for status reporting contained information that were neither complete nor up-to-date. Lengthy turn around time was required to locate the responsible person(s) to clarify the situations and to cross check the data. By the time that data were updated, it would be again out-of-date.

The situation was further accentuated as customer order changes were frequent and they were hard to anticipate. Staff in PPC were presented with a lot of operational difficulties which came as a consequence. For example, they needed to change their order bookings as frequently as possible in order to reflect the impact of the change to the revised schedules. One strategy was to delay the issue of the final schedule as late as possible. However, it was partially effective. As decisions were interdependent, the gain in one decision maker was at the expense of others. Given little information in advance, reactive decisions are made solely based on intuition, experience, and personal judgement.

It might appear that computerization could help in these circumstances. But the staff were sceptical. Their perception was that computer systems were inflexible especially when changes would be required due to new order or order changes. They expressed their distrust by saying that they were too busy with their daily work to spare time to learn the computer systems – or else that it was too difficult for them to use.

In summary, PPC operations are intricate. It takes time, effort and cooperation to validate, prepare and update the relevant work documents. Further, there were difficulties in logistic functions, communication and coordination across the national boundary. The data discrepancy problems meant that no one set of data could be trusted for production planning.

## 3. Conceptual foundations of ODSS for PPC

Given the aforementioned PPC context, some managerial considerations were come across. These considerations, when accepted by the management and production staff, gave them insights in making better provision for effective organizational decision making. These considerations and insights are summarized in the following sub-sections with an objective that they can be used to provide cues tending to sensitize management to articulate the meanings of “adequate provision” for effective decisions in a PPC context.

## 3.1. Integrative decision support for PPC

PPC may be considered to be a series of inter-linked planning and control loops. Integration is through establishment of inter-loop linkages at various levels, e.g., the item, BOM, order, fund flow, project, and department. The generic use of an ODSS can be categorize into the methods for (1) planning future operations; (2) communicating scenarios; and (3) monitoring operations (i.e. providing information for short term decision making or special analysis). With respect to this categorization, each PPC loop could be considered to be similar to the extent that it includes the following common activities.

(a) Planning Future Operations. Production requirements and schedules are prepared for each level, based on committed or forecasted requirements. For finished products, the higher level requirement will be the customer order; however, for purchased parts, the higher level requirement will be the assembly schedule. Here, the BOM is used to explode the assembly into its subassembly or components. An important technique for constructing BOM for decision support is to embed preplanned decision points in the BOM processing. Some typical examples include: inclusion of lead time offset for time-phasing material planning, rolling up cost figures, schedule engineering changes, etc. [20].

(b) Communicating Scenarios. Next, the part requirements are processed against the stock status and each part analyzed for availability. Another kind of preplanned decision procedure can be effective at this point. One kind of preplanned decision here is to allow for order transaction and analysis; e.g., actual or logical allocation of materials or queuing of order backlog. The work or purchase request is then prepared for those parts needing to be replenished. PPC prepares the work orders and collects the relevant work documents and then releases them according to the schedule.

(c) Monitoring Operations. Data collected about the stock before and after each production unit is available to keep track of the progress of an order.

Once the activity cycles for every PPC loop and their inter-linkages have been identified, it is possible to design the necessary data models, system outputs, the control parameters, and the system inputs. Such design considerations are covered elsewhere $[2,27]$ .

![](/api/attachments/3FFYP564/fulltext/images/ef1685403e69b7ee1c978a5fa979194ccab5a7603e6ee881b76eca9384560d2f.jpg)  
Fig. 2a. A cumulative time series representation, e.g. cumulative in/out stock status.

## 3.2. Application of visual modelling

From an information processing perspective, production staff can benefit from making use of visual models and quantitative aids which aid their decision making through improvement in information aggregation, analysis, and presentation. As every order cycle involves transactions to both open and close an order, huge amount of data about the order status need to be monitored. The dynamics of the order transactions could be modelled by a linear step function where each variable of interest in the transaction is taken as a step change with respect to time. The change in the variable of interest (e.g. order status) therefore is a function of time. It is represented as a time-line to be displayed graphically.

An example is given in Figure 2a. A tabular view of the Data is shown in Figure 3.

Here, the change of incoming and outgoing quantity of any particular item are of interest for order status monitoring and tracking. The interrelationship between the two lines represents the dynamics of interdependency. The two major dynamic patterns of interest are: change in materials shortage and surplus with respect to time and change of item lead time with respect to time. The former is modelled by the vertical separation between lines (the stock on hand), while the latter is modelled by the horizontal separation between lines (the lead time relationship). Whenever these two lines cross each other, it indicates materials shortage. This concept will be clearer if the gap distance between the two lines is represented as the balance and shown on a separate graph (see Figure 2b).

The graphical modelling technique is very useful because it can be applied to a wide range of applications, for example, every stock point in the

![](/api/attachments/3FFYP564/fulltext/images/9cc3729ca57d3e5671fdc352cff120c5db2e0f284271420f77fe15bd09f9fd97.jpg)  
Fig. 2b. Differences between the two variables in Fig. 2a, e.g. stock balance.

<table><tr><td colspan="5">Inventory File View</td></tr><tr><td colspan="5">PART: 900-100-10-XX10DESP: SWITCH-SWIVEL CONTACT DISC SUB-ASSEMBLYDATE: 91.10.15 -&gt; 91.11.15</td></tr><tr><td>Date</td><td>In</td><td>Out</td><td>Balance</td><td>Reference</td></tr><tr><td>91.10.14</td><td>10,000.00</td><td></td><td>51,200.00</td><td>4678</td></tr><tr><td>91.10.16</td><td>16,000.00</td><td></td><td>67,200.00</td><td>4681</td></tr><tr><td>91.10.18</td><td>8,000.00</td><td></td><td>75,200.00</td><td>4684</td></tr><tr><td>91.10.21</td><td>14,000.00</td><td></td><td>89,200.00</td><td>4685</td></tr><tr><td>91.10.21</td><td></td><td>67,200.00</td><td>22,000.00</td><td>8097</td></tr><tr><td>91.10.23</td><td>16,000.00</td><td></td><td>38,000.00</td><td>4687</td></tr><tr><td>91.10.25</td><td>14,000.00</td><td></td><td>52,000.00</td><td>4689</td></tr><tr><td>91.10.28</td><td>18,000.00</td><td></td><td>70,000.00</td><td>4691</td></tr><tr><td>91.10.30</td><td>15,200.00</td><td></td><td>85,200.00</td><td>4694</td></tr><tr><td>91.11.01</td><td>14,000.00</td><td></td><td>99,200.00</td><td>4696</td></tr><tr><td>91.11.05</td><td></td><td>99,200.00</td><td>0.00</td><td>8280</td></tr><tr><td>91.11.11</td><td>15,200.00</td><td></td><td>15,200.00</td><td>4706</td></tr><tr><td>91.11.13</td><td>16,800.00</td><td></td><td>32,000.00</td><td>4708</td></tr><tr><td>91.11.14</td><td>16,000.00</td><td></td><td>48,000.00</td><td>4698</td></tr><tr><td>91.11.14</td><td>12,000.00</td><td></td><td>60,000.00</td><td>4709</td></tr><tr><td>91.11.14</td><td></td><td>31,200.00</td><td>28,800.00</td><td>8205</td></tr><tr><td>91.11.15</td><td></td><td>28,800.00</td><td>0.00</td><td>8211</td></tr><tr><td colspan="5">Rec no.: 1/17 &lt; &gt;</td></tr></table>

Fig. 3. Tabular view of Fig. 2a and 2b (a sample output of the text display).

order cycle could make use of graphics to avoid information overload of the stock keeper. Provided that the order booking is available, this tool could also be used to project order bookings to visualize future requirements. It constitutes an early warning window for anticipating materials shortage in advance.

## 3.3. User-oriented DSS development

The manufacturing business is required to respond to a changing market, therefore production staff require timely operational data to make informed decisions in a responsive manner. Such decisions could be guided, to a limited extent, through planned intervention and supplemented by human intelligence. It is essential that operational decision makers are made responsible for solving problems in the complex business environment and making continual adaptations to the system.

As the change is frequent and rapid that software for production planning and control has to be maintained to meet the changing circumstances. Rigid program structures are one of the most significant limitations in using computers for live applications $[7]$ . Every change (e.g. product structure re-configuration or material substitution) requires modelling before putting into operation. In extreme cases, manufacturing might begin even though the product had not been thoroughly prototyped. With such (little) information, hardly anything could be modelled.

With the development of more sophisticated user-oriented system development tools, the skill required for system development is lowered, at least for less complicated applications. Some end users (in this case, the production staff) begin to develop applications for their own specific needs. Staff can be encouraged to use the opportunities.

## 3.4. ODSS technology adoption and diffusion

The fundamental improvements of adopting ODSS in manufacturing stem from structural reform in the organization [7]: i.e., reviews of operating procedures, revising standards to meet the current needs, user training and management commitment in providing resources, etc. Production staff's prior experience, perception, and expectation inevitably affect the nature of the system requirements. Therefore, in organizing a system development project, it is necessary to extend it to cover preparatory works needed for making changes, such as revision of policy or renewing obsolete procedure. Similarly, it is desirable to consider these in the ODSS design. The changes will inevitably be regarded as process innovations. Their adoption process in general consists of the following stages:

i. acquiring knowledge of ODSS technology;

ii. persuading relevant people of its viability;

iii. deciding to adopt it;

iv. converting the old system by ODSS development;

v. confirming that it is appropriate.

Provided that the ODSS is an integral approach to support decision making, it should be supported. Based on this, the design of the ODSS needs to consider its innovation attributes $[24]$ , such as its Relative Advantage, Compatibility, Complexity, Trialability and Observability in the context. In addition, it is necessary to consider the innovation diffusion strategies $[17]$ such as Transferability, Divisibility, and Implementation Complexity. DSS designers must consider the social implications of their technology innovations as early as possible and keep these considerations parallel with the technological constraints in every stages of the project. This is “Innovation in Situ” for management of change in the organization $[14]$ .

Further, some western decision technology does not fit into the oriental culture. Typical problems include, cultural clash $[36]$ and difference in collective decision making behaviour $[23]$ , etc. Consider brainstorming, which is typically used as a fact finding or knowledge elicitation techniques in group settings. One of the underlying assumptions is that open confrontation help to reveal underlying assumptions. However, in an organization that emphasizes harmony preserving, open confrontations are avoided.

Nevertheless, early diagnosis to reveal cultural clash is required to avoid problems in later stages of the development [25]. Evolutionary or participatory development making use of prototyping [1,15] techniques seem useful.

## 4. Managing ODSS development in the organization

## 4.1. Ready decision makers

The efforts in the earlier stages of development were centred around opportunity finding. Opportunity for ODSS development were sought. At this early stage, they were limited to some readily available and ease-to-use applications. Some applications identified and implemented included:

\- a word processing program to issue purchasing contracts,

\- a graphics program to present engineering test data,

– data base applications for storage and retrieval of outstanding purchase orders,

\- spreadsheet applications for analysis of final assembly schedule,

\- Chinese part-description-label printing.

Initial successes motivated the production staff to participate by forming informal groups to explore further opportunities for improvement. They began to team up for ODSS developments. Interest groups and project teams were formed for joint application developments. This suggested that consensus was being formed between organizational members in resolving conflicts and realizing the challenges of ODSS development.

## 4.2. Preparing for operational rationalization

A properly designed and structured BOM is extremely important for management of production and product information (especially in a vertical manufacturer). Any discrepancy in its structuring or processing logic could be regarded as a form of structural weakness in the design.

In this case study, as the manufacturing staff learnt about the concepts of embedding pre-planned decision procedures in the BOM processing, they began to realize that there were a lot of structural weaknesses in their existing BOM structure that prevented them from reaping the potential benefits for integrated production planning and control. Before specifying any Information Technology solution, method and process were redesigned with an objective of turning structural weaknesses into preplanned decision procedures and building them into the BOM processing. These tasks at background were requisites to supporting the subsequent ODSS design and development. They were regarded as custodial or administrative developments. In fact, these are another kind of administrative innovation to the organization. Some typical examples are given in Table 5.

## 4.3. On-going improvement

A strategic plan for the next three years was developed. The goal was to create an early warning window that would highlight further material shortage. The essence is to project the order bookings into the future and shown the impact on the graphic window using the visual modelling techniques outlined in section 3.2.

The pilot project was selected because it was a major component in over 70% of the finished goods. It helped the PPC to avoid materials shortages. The early success motivated both the management team and user group to increase the project to cover a wider span. Therefore, it involved the full sub-assembly of parts, and subsequently all sub-assemblies and finished goods as well. The scope of the project was also extended to include every order booking; this typically consisted of materials allocation, materials onorder, and outstanding orders.

The structuring of preplanned decision into the BOM processing was decomposed into a series of tactical plans. They are complementary to the development of the warning window project. Typical examples include: rationalization of the part number system and restructuring of the BOM system. These plans were organized as user-oriented projects. For example, one major project was in tracking of material progress and arranging order bookings. The staff from Stock Control, Purchasing, and Production Control developed their individual DSS to keep track of individual records of materials booking using a shared relational data base.

Table 5  
Example custodial projects with objectives to overcome structural weaknesses.

<table><tr><td>Project</td><td>Prime objective</td><td>Targeted structural weakness</td></tr><tr><td>Variety reduction (group tech.)</td><td>To design a generic BOM so that it is applicable to all order types, whether it is make-to-stock, make-to-order or assemble-to-order.</td><td>exception handlings related to option items, substitute items, mock up, customer order changes, etc.</td></tr><tr><td>Part master with bi-lingual display</td><td>To rationalize the coding system, and also ensure that staff who find difficulty in reading English can also use the system</td><td>Coding discrepancy: no Chinese part description, different code with same description whether English or Chinese, description too long</td></tr><tr><td>Conversion factor</td><td>To capture the conversion factor in every shop, every production line, and every process; and safeguard its consistency</td><td>variability in process yield, multiple measuring units (e.g. kg, lb, ctw, pcs, roll, etc.)</td></tr><tr><td>Consumption factor</td><td>Similar to the conversion factor project</td><td>Excessive wastage, lost, excessive work-in-progress</td></tr></table>

Shortly after execution of several projects, the management and some of the production staff realized that the ODSS project was not a single project, but it was a series of on-going projects. Matrix project organization has been set up, see Figure 4. In fact, the way that identification of DSS along the business cycle (i.e. order cycle) was found to be instrumental in achieving seamless integration of these various projects. The primary projects are:

(a) Extended Part Master Project.

(b) Generic BOM Project.

(c) Inventory Control Project.

(d) Material Allocation Project.

(e) Scheduling \ Rescheduling Project.

## 4.4. Setting-up an IT infrastructure

A new design, namely Throughput Material Requirement Planning (T-MRP) [31], was proposed as a distributed resources management tool for logistics support for remote plants in PRC. The major functionalities of T-MRP included: keep active account of Input/Ouput material status and provide timely report of them; synchronize the material movement on order basis; detect bottleneck and perform material shortage analysis based on order bookings. T-MRP was developed using a system development software (which usually known as software development environment) that consisted of relational database, software modules libraries, graphic generator, report writer and other software utilities including a Chinese User Interface development tool kit. The software platform was chosen in consideration for ease of promoting user participation in their user-oriented development. The existing system infrastructure was stretched: stand-alone personal computers were re-configured into a Local Area Network (LAN) and equipped with additional Office Automation facilities; applications whether newly acquired or originally run on stand-alone personal computers were upgraded to be Local Area Network (LAN)-based; system architecture was redesigned to be a Client-Server based; data capture terminals were set-up in the PRC plants and connected to the host systems in Hong Kong through modem. These system changes not only facilitated integration of T-MRP with the existing system but also reserved much flexibility for further system enhancements.

![](/api/attachments/3FFYP564/fulltext/images/9d1c444f5fd2071e21b4039d032764fefe84ac6d1fc7f3a9662f46bd95449881.jpg)  
Fig. 4. Project matrix of the ODSS development in the case organization.

## 4.5. Implications to management

The company wide implications of the ODSS development were apparent to management and production staff: The structural weakness in the BOM structure and inconsistent data were improved; staff in various departments began to integrate their order bookings, and project them into aggregated demand and supply at various levels of control; the evaluation function offered by the warning window helps to assess materials shortage in advance; and there was a behavioural change in the organization associated with the ODSS development; the decision making style changed from confrontative to collaborative.

The staff in the PPC began to try more peripheral ODSS developments. These eventually turned into incentives that motivated both management and staff to sustain the ODSS development. As a result the management team decided to consider a new strategic plan for the next three years. The previous work laid the foundation towards integrated manufacturing, and encouraged management to include other areas in future ODSS development, e.g. Engineering Design, Shop Floor Order Dispatching.

## 5. Lessons learned

## 5.1. Collaborative team work

The case study highlights the need for preparatory work before computerization. It involves tasks that typically relate to data capture, work simplification and networking staff across functional boundaries in collaborating teamwork. ODSS development would inevitably accompany with behavioural change in the organization. A form of cooperative on-the-job improvement, if successfully cultivated, would be conducive to support and reinforce the ODSS development. In essence, this team collaborative approach emphasizes the need for pre-implementation efforts in data capture, in-house training of production staff, simplifying working procedures and elimination of structural weakness in the operations.

## 5.2. Parallel organizational development and adoption of technology

The logical steps involved: Identification of the user-oriented DSSs (usually simple applications) and identification of structural weakness in the operations. Insights are learnt on-the-job when incremental improvement projects are implemented. The detailed procedures could be gradually rationalized along the business cycle during successive development and improvement throughout the ODSS implementation. Therefore the management team should however, be encouraged to become involved in the development process to enable them to cultivate and foster insights in situations that must ultimately be included.

This pattern of steps in summary is not an isolated incidence. Review of past successful projects $[6]$ of the same nature shown similar patterns: “simple DSS, procedure rationalization, management vision to formulate incremental improvement into projects, technology adoption, incremental but continuous improvement”. The logical and tactical steps involved may not be linear. However, it seems that simple rather than sophisticated ODSS is required to start up the process.

## 5.3. Information systems research challenge

With an ODSS, the user and their systems capabilities are constantly pursuing forthcoming challenge; but there will never be a complete solution. There is a consistent criticism $[3,10,21,28]$ about research on complex real world problems: model is usually simplified in order to obtain results in a relatively short time. Such artificial conditions limit the research design and conflict with reality. As illustrated in this study, such weakness can be overcome if the research is conducted in real life setting. In case that technology transfer is required, it can be done in collaboration with Higher Educational Institutions [6].

## 6. Conclusion

In this paper, a case study of development and adoption of an ODSS in a small manufacturing enterprise is described showing the value in paying attention and supporting the design process as well as users' social process of learning and innovation. The mechanism that provides opportunity and constraint is discussed illustrating the adoption and implementation strategies to address these issues. The technical system was institutionalized in the case organization. Further ODSS development will hinge on parallel development and adoption of technology as an effective strategy for continuous operational improvement; and the extension of the experience to an ODSS for integrated logistic management is under discussion.

The study is aimed to assess the need of development and enrichment of ODSS as primary component of strategic IT platform in general and for small manufacturing enterprise in particular. At the same time the development of such system has to be concerned jointly with the need to manage technological innovation with organizational change and human resources development. One condition that improves the chance of creating a success out of a new market niche would depend on the presence of a co-design process which brings out the best from the people. The DSS is employed to channel the creativity of these highly competent people in a responsive manner for the parallel process of design, development, testing, implementation and institutionalization of ideas so that the business continues to offer a product or service of “value” to the customers.

The challenge in adopting a DSS is to convince the organization the need to acquire a new mental set while the transformation of the organization is taking place with the use of the DSS.

Persuading the organization a need to change its management style is more than an announcement for the adoption of a new organizational structure. Once again, human creativity holds the key in which an infrastructure of competent people could be strategically located to maintain business continuity. If the teams of competent people are developed over time internally, this reduces the need to take excessive risks which otherwise might threaten business continuity. The ODSS is the state-of-the-art managerial perspective found useful in the case study to develop these teams of competent people. The ODSS also guides the formulation of a framework for using DSS in manufacturing management.

Given an organization has acquired this managerial perspective of using ODSS, one might venture to say that the teams of competent people are better equipped to drive the organization faster than competitors could in anticipating and managing emerging technologies for organizational innovation. The business would prosper with these talents operating and creating new market niches.

Project of the nature as described in the case study requires extensive technology transfer. Industrial collaboration between Higher Educational Institutions and Industry help to bridge such a technological gap. Perhaps it is pertinent to point out that although Hong Kong may be lagging behind in advanced science and technology $[12]$ , it excels in mid-level manufacturing technology which is what China needs so much $[18]$ . If technology is interpreted in a broad sense to include management information systems, integrated planning and control and flexible incentive schemes for the promotion of manufacturing, South China can benefit from such technology transfer.

## References

[1] S.L. Alter, Decision Support Systems: Current Practices and Continuing Challenge, Addison-Wesley, 1980.

[2] M. Baudin, Manufacturing Systems Analysis, Yourdon Press, 1990.

[3] I. Benbasat, D.K. Goldstein and M. Mead, “The case research strategy in studies of Information Systems,” MIS Quarterly, Vol. 11, No. 3, 1987, pp. 368–386.

[4] J.W.M. Bertrand and J. Wijngaard, “The structuring of Production Control Systems,” Report ARW03/BDK/

ORS / 84 / 10, Eindhoven University of Technology, Netherlands.

[5] G.M. Carter, M.P. Murray, R.G. Walker and W.E. Walker, Building Organizational Decision Support Systems, Academic Press, 1992.

[6] W.W.C. Chung and M.M.C. Tam, “Empirical-based Manufacturing Research Paradigm,” Proc. Australian Conference on Manufacturing Engineering ACME'93, 22–24 November, 1993, The Institution of Engineers, Australia.

[7] W.W.C. Chung, M.M.C. Tam, K.B.C. Saxena, and K.L. Yung, “Evaluation of DSS use in Hong Kong manufacturing industries,” Computers in Industry, Vol. 21, No. 3, 1993, pp. 307–324.

[8] C.K. Farn and K. Sung, “Collaborative decision making behaviour in the Chinese society and its implication in Group Decision Support Systems,” in Group Decision Support Systems in Pacific Rim Nations, Joey F. George, Jay F. Nuanmaker (eds.), PRIISM monograph, Nov. 1988, Pacific Research Institute of Information Systems and Management.

[9] Federation of Hong Kong Industry 1990, Hong Kong's Offshore Investment, 1990.

[10] B.B. Flynn, A. Sakibara, R.G. Schroeder, K.A. Bates and E.J. Flynn, “Empirical research methods in operations management,” Journal of Operations Management, Vol. 9, No. 2, 1990, pp. 250–274.

[11] J.C. Henderson and M.E. Treacy, “Managing End-User Computing for competitive advantage,” Sloan Management Review, Winter 1986, pp. 3–14.

[12] D. Henton, Building Prosperity: a fore-part economic strategic for Hong Kong's future, SRI International, 1989.

[13] V.S. Jacob and H. Pirkul, “Organizational decision support systems,” Int. J. Man-Machine Studies, 36, 1992, pp. 817–832.

[14] R.S. Kanter, The Change Masters, Hazell Watson & Viney Ltd., 1983.

[15] P.G.W. Keen, “Adaptive design for DSS,” Data Base, 12(1), Fall 1982.

[16] P.G.W. Keen, “Relevance and rigor in information system research: improving quality, confidence, cohesion and impact,” in Information System Research: Contemporary Approaches and Emergent Traditions, H.E. Nissen, H.K. Klein, R. Hirschheim (eds.), Elsevier Science Publishers B.V. (North Holland), IFIP, 1991, pp. 27–49.

[17] D. Leonard-Barton, “Implementation characteristics of organizational innovations: Limits and opportunities for management strategies,” Communication Research, October, 1988, pp. 603–631.

[18] T.P. Leung, “Technology transfer and development between China and Hong Kong,” Proc. Technology Transfer and Implementation TTI'93, Vol. 1., Teaching Company, U.K., 1993, pp. 139–142.

[19] T.W. Malone and K. Crowson, “What is Coordination Theory and How can it help design Cooperative Work Systems?”, Proc. Conf on Computer-Supported Cooperative Work, Los Angels, October, ACM press, pp. 357–370.

[20] H.M. Mather, \*Bills of Materials\*, the Dow Jones-Irwin/APICS series in Production Management, APICS, 1987.

[21] J.F. Nunamaker, M. Chen and T.D.M. Purdin, "Systems

development in information systems research," Journal of Management Information Systems, Vol.7, No.3, (Winter 1990–91), pp. 89–106.

[22] J.F. Nunamaker et al, “Organizational Decision Support Systems (ODSS)”, in Information Systems and Decision Processes, E.A. Stohr and B.R. Konsynski (eds.), IEEE Computer Society Press, 1992, pp. 137–166.

[23] K.S. Raman, E.K. Rao, “Group decision Support systems for public bodies: A modest proposal,” in Group Decision Support Systems in Pacific Rim Nations, Joey F. George, Jay F. Nunamaker (eds.), PRIISM monograph, Nov. 1988, Pacific Research Institute of Information Systems and Management.

[24] E.M. Rogers, \*Diffusion of Innovations\*, The Free Press, third edition, 1983.

[25] T. Romm, N. Pliskin, Y. Weber and A.S. Lee, “Identifying organizational culture clash in MIS implementation: When is it worth the effort,” Information & Management, 21, 1991, pp. 99–109.

[26] K.B.C. Saxena, “Computer-aided Decision Support Engineering,” in Recent Developments in Decision Support Systems, Clyde W. Holsapple and Andrew B. Whinston (eds.), Springer-Verlag, 1993, pp. 313–335.

[27] J.A. Senn, Analysis and Design of Information Systems, McGraw-Hill, 1989.

[28] P.M. Swamidass, “Empirical science: New frontier in operations management research,” Academy of Management Review, Vol. 16, No. 4, 1991, pp. 793–814.

[29] M.M.C. Tam, K.B.C. Saxena, W.W.C. Chung, and K.L. Yung, “Decision Support Systems (DSS) in Manufacturing: Cross comparison of surveys from United Kingdom, Singapore and Hong Kong,” Proc. Intl. Manufacturing Conf. with China IMCC'93, Vol. II, Hong Kong, 1993, pp. 521–526.

[30] M.M.C. Tam, K.B.C. Saxena, W.W.C. Chung, K.L. Yung and A.K. David, “Organizational Decision Support Systems (ODSS) for Small Manufacturing Enterprises (SME) in Hong Kong,” in Advances in Production Management Systems (APMS'93), Ioannis A. Pappas (eds.), Elsevier Science Publishers (North Holland), IFIP, 1994.

[31] M.M.C. Tam, W.W.C. Chung, K.B.C. Saxena, K.L. Yung, and A.K. David, “Theory and Practice of Throughput Materials Requirement Planning (T-MRP) in repetitive manufacturing,” Proc. Australian Conference on Manufacturing Engineering ACME'93, The Institution of Engineers, Australia, 1993.

[32] R.J. Thierauf, User-Oriented Decision Support Systems: Accent on Problem Finding, Prentice-Hall Int. Eds., 1988.

[33] E. Turban, Decision Support and Expert Systems: Management Support Systems, Macmillan, 1993.

[34] F.W. Wolek, “Implementation and the process of adopting managerial technology,” Interfaces, Vol. 5, No. 3, 1975, pp. 38–46.

[35] L.F. Young, “Decision Support Systems for workers: A bridge to advance productivity,” Information & Management, 16, 1989, pp. 131–140.

[36] B. Zhang and O.A. Ian, Decision Support Systems in China: A clash of cultures," Information Technology for Development, Vol. 5, No. 2, 1990, pp. 137–154.
