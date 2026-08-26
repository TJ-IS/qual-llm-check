---
otero_id: 7996
otero_key: "FB9QWBFG"
title: "IPManager: a microcomputer-based DSS for intellectual property management"
authors: "Chuda Basnet; L.R. Foulds; Warren Parker"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.05.014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# IPManager: a microcomputer-based DSS for intellectual property management

Chuda Basnet<sup>a,\*</sup>, L.R. Foulds<sup>a</sup>, Warren Parker<sup>b</sup>

<sup>a</sup>Department of Management Systems, University of Waikato, Private Bag 3105, Hamilton, New Zealand <sup>b</sup>AgResearch, Ruakura Research Centre, Hamilton, New Zealand

Received 1 April 2003; accepted 1 May 2004 Available online 27 September 2004

## Abstract

We describe a decision support system (DSS) that was developed for the management of the costs associated with the payment of fees to protect the intellectual property (IP) of organizations involved in research and development. IPManager is a decision support system that the authors developed to aid managers of IP in creating or improving IP registration and maintenance strategies and to enable them to use their experience and preferences. The system is currently in use at AgResearch, which is a New Zealand-based institute conducting research into agriculture. A case study is reported discussing the decision environment that motivated the development of the system. <sup>D</sup> 2004 Elsevier B.V. All rights reserved

Keywords: Intellectual property management; Decision support; Prototyping

## 1. Introduction

As the largest Crown Research Institute in New Zealand, AgResearch provides knowledge and best practice technology to pastoral agricultural industries. A strong focus on biotechnology and ecotechnology seeks to provide integrated life science solutions that create value for stakeholders and customers, wealth for New Zealand, and better health for all. At the beginning of 2000, 835 permanent staff operated from the

Ruakura (Hamilton), Grasslands (Palmerston North), Wallaceville (Upper Hutt), Lincoln (Christchurch), and Invermay (Dunedin) campuses of AgResearch. Revenue for the year to June 2000 was \$106 million. While contract research and development remains the cornerstone of AgResearch’s business, a major imperative is to evolve into a life sciences company providing valueadded high margin products and subsequent greater returns to New Zealand. This is to be achieved by increasing revenue through the acquisition or development and delivery of new products and technologies.

This strategy necessitates the creation of new agricultural products whose related intellectual property (IP) ownership by AgResearch must be protected by patents, trademarks (TMs), and plant variety rights (PVRs).

AgResearch (Ruakura) required a decision support system that would improve the organization’s management of the costs it periodically incurs in maintaining its IP rights. We describe here the decision environment involved and also the development and use of the DSS, called IPManager, that was constructed for this purpose. A literature review of current research into the management of intellectual property is provided in the next section. In Section 3, we discuss the use of the DSS as an operations research (OR) tool. In Sections 4 and 5, we discuss the decision environment at AgResearch and IPManager. In Section $^ { 6 , }$ a description of the development process and a discussion of the impact of the DSS is presented. We end the paper with some overall conclusions and a summary in Section 7.

## 2. Literature on intellectual property management research

Recently the World Intellectual Property Organization agreed to decrease patent registration fees [12]. The decreases were approved unanimously by all 171 member countries. Zarocostas [12] provides details on the amount the fees were decreased, including information on discounts for electronic applications. On a worldwide basis this news, along with the growing privatisation of research and development, has been a factor in the increasing number of patent registration applications. As research into the IP registration process is scarce, we provide only a brief overview of current research in this area. Beggs [2] explains the use of royalty payments, rather than fixed fees, in the licensing of patents in the presence of asymmetric information. Bousquet et al. [4] made the first formal study of risk sharing as a major rationale for the financial arrangements between a patentee and a licensee. The authors examine a particular, but empirically meaningful, class of license contracts consisting of a fixed fee, a per unit royalty, and an ad valorem royalty. The analysis proceeds by simulation in order to characterize the optimal license contracts. Lanjouw [9] has derived empirical estimates of the private value of patent protection for four technologies: computers, textiles, combustion engines, and pharmaceuticals; using new patent data for Germany. It is assumed that patent-owners must pay renewal fees to keep their patents in force, as well as legal expenses in order to enforce them. We now go on to discuss the DSS approach to management issues, of which IP fee management is an example.

## 3. The decision support system as an aid to OR practice

The decision support system (DSS) has emerged as a computer-based approach to assisting decision makers to address semi-structured problems by allowing them to access and use data and analytic models [11]. DSSs are interactive computer-based systems aimed at semi-structured problems, utilising models with internal and external databases, and emphasising flexibility, effectiveness, and adaptability. These characteristics have guided much of the research in the DSS area, but the potential benefits of the DSS in the business environment are yet to be fully realized. Nevertheless, many successful DSS applications have been reported in the literature [1,5,10] Most of these applications are either large-scale systems built to facilitate well-defined and repetitive decision tasks, or else they are small PC-based systems offering quick and economic routines to support one-time decision making [7]. Although the definition of the DSS concept has been elusive [3,6], the field has flourished with the development of computer technology. Keen [8] reviewed a decade of DSS development and concluded that there is a need for a balance between each of the three DSS elements: decision, support, and systems. He felt that more research effort on the decision component was required to restore this balance, as the technology for the system component was no longer a bottleneck. To achieve <sup>b</sup>the mission of the DSS- to help people to make better decisions<sup>Q</sup>, Keen stressed the need for an active supporting role for <sup>b</sup>decisions that really matter<sup>Q</sup>. We now focus on the decision component of the DSS.

Many DSSs have the basic structure that is illustrated in Fig. 1. The model and solution technique bases are included to incorporate mathematical programming (MP) techniques. Clearly, they could include all appropriate models and their companion solution techniques that may be useful in order to gain insight into the scenario for which the particular DSS is designed. These models and techniques may not necessarily be confined to the classical deterministic models such as linear, integer, nonlinear, and dynamic programming, but also those from areas such as queuing, scheduling, inventory, and others. The models and techniques bases are included in order to be used, as necessary, to solve certain sub-issues or precise questions that arise during the overall analysis of the main scenario. They can be invoked to answer <sup>b</sup>what if? <sup>Q</sup> questions, to perform sensitivity analysis, and to provide precise solutions to sub-problems that can be modelled exactly. For example within a vehicle routing DSS, a travelling salesman problem (TSP) model and various TSP solution techniques could be included. Then, if it has been established that a given vehicle will visit an identified list of clients, the TSP model and a TSP solution technique could be invoked to establish a least-distance tour.

![](/api/attachments/FB9QWBFG/fulltext/images/91cb6f130f3dc705296813730240f1dcffd69e1f45b1d9887825e6ccf619a404.jpg)  
Fig. 1. The structure of a decision support system.

However it must be stressed that any DSS should be much more than just a mere collection of models and solution techniques. Although these can be quite valuable aids to the implementation of MP in terms of user friendliness and convenience, these should be only a small part of any DSS. The essence of the DSS is the user-system interface that allows the planners to: experiment, input local knowledge and inspiration, deal with unstructured situations, be flexible, allow for multiple objectives, and soft (violatable to some degree) constraints. As an example, the primary purpose of an educational course timetabling DSS may be the identification of a feasible timetable without the optimization of any objective functions. The timetablers will <sup>b</sup>play<sup>Q</sup> with the DSS inputting various course-room-teacher-time slot combinations noting various statistics that the DSS displays. Judgments as to the worth of various combinations are often made on grounds that are difficult to quantify and virtually impossible to model. Nevertheless, suggestions can be made by the DSS based on various assignment, matching, and allocation models and solution techniques from the bases in Fig. 1.

In this section we have described the basic elements of any DSS and how appropriate OR models and solution techniques can be incorporated into it. We now go on to outline the DSS environment at AgResearch.

## 4. The decision environment at AgResearch

## 4.1. Overview

We first focus on the information required to manage the costs associated with the IP protection process. IP information consists of events, associated dates, and associated costs. For example, an IP examination in a specific country is one such event. Thus one needs to know what events (with dates and costs) that have occurred so far, and what events are planned in the future in order to estimate the total costs. Even though the actual occurrences of events and costs cannot be known in advance, an estimated schedule of events and costs is available for each item of IP maintained by AgResearch. The schedule is also differentiated by the particular countries in which AgResearch maintains IP rights.

A schedule for New Zealand patent registration can be represented in the following manner. The events and timing are shown in Fig. 2. In addition an annual maintenance fee is payable until the IP right is granted. Then a renewal fee is payable after 1, 4, 7, and 10 years. Obviously, the costs and timings are expectations only, but they permit future costs to be estimated. IP applications can be discontinued at any time thus avoiding any costs thereafter. There is also a statutory term limit of 20 years for the patent rights in New Zealand.

![](/api/attachments/FB9QWBFG/fulltext/images/5b2d34600cad9263d67053679d30f55a79776cbbe9a10bdbe150abe00ddf9881.jpg)  
Fig. 2. A New Zealand patent registration schedule.

Patents in foreign countries may be registered in one of two ways: (1) by applying directly to a country, based solely on the New Zealand application date, or (2) by applying to the country on the basis of the patent cooperation treaty (PCT). The second process simplifies work in foreign countries, but a prior PCT application needs to be made in New Zealand first.

## 4.2. Applying directly to a foreign country

Fig. 3 shows the events, costs, and expected timings of the process of applying for patents directly in Canada. In addition there are annual maintenance fees before the grant, and renewal fees after the grant. The events may be slightly different from country to country. Each country has its own schedule of maintenance and renewal fees. For example, renewal fees are payable 4, 8, and 12 years after the patent grant in the USA.

## 4.3. Applying via the PCT

Patent application via the PCT occurs in two stages. The PCT procedure occurs first in New Zealand. An international preliminary examination is carried out by the New Zealand Patent Office, acting as an agent for the World Intellectual Property Organisation (WIPO). Once this stage is complete, the patent application is processed in individual countries (the national phase). The PCT application, until it enters the national phase, is shown in Fig. 4.

Once the PCT application has entered the national phase, application is made in individual countries. Once again, there are maintenance and renewal fees, with their own schedules of time and amount. There are also time limits for patents specific to each country.

## 4.4. Trademarks and plant variety rights

So far the discussion has focussed on patents, but the application process for TMs and PVRs follow similar patterns. Both these processes essentially consist of application, examination, and registration. However, the events, their schedules, and their costs are different. There is no PCT application process for both trademarks and PVRs. All overseas applications have to be made directly to the individual countries. A single application suffices for PVR in the European Community. Similar to patents, there are maintenance and renewal fee schedules and time limits for trademarks and PVRs for each country.

![](/api/attachments/FB9QWBFG/fulltext/images/df4bba3a1db129345e48bcd2eb7d799496e9cbcec56a3cbfdd5bea926735b819.jpg)  
Fig. 3. Direct patent application process in a foreign country.

![](/api/attachments/FB9QWBFG/fulltext/images/7589c69cad0204e0adb66879dcb04eeec3ef8030608305aa63b3dbd9e3010eaa.jpg)  
Fig. 4. PCT application process.

In this section we have described the practical scenario for which our DSS was designed. In the following section the description of our DSS is given.

## 5. IPManager

IPManager is the name given to the DSS that was developed to aid managers in AgResearch in their decision-making. IPManager was devised to help AgResearch manage the fees that the organization pays concerning their IP rights. It provides estimates of future expenses incurred in pursuing, registering, maintaining, and renewing IP rights in various countries. These estimates incorporate prior commitments and provide decision support to AgResearch concerning desirable future courses of action to be taken with regards to IP financial strategies. In addition, IPManager maintains information on the current registration status of IP.

To support decisions, such as when to file applications or when to abandon an IP process, a schedule of expected events for each country is used. Even though the actual occurrences of events and costs cannot be known in advance, an estimated schedule of events and costs is available for each country. Once this is available, and a series of tentative decisions are made, one can apply the schedules to the decisions and consequent yearly costs can be estimated. This information consists of events, associated dates, and associated costs. For example, an IP examination in a specific country is one such event. Thus one needs to know what events (with dates and costs) have occurred so far, and what events are planned in the future, with respect to prior and new IP, in order to estimate the total costs. Management can thus explore different IP management scenarios to meet budget allocations and ensure current plans do not jeopardise future opportunities.

## 5.1. The DSS model

IPManager is based on a schedule of IP costs for each country. As can be expected, not all the nuances described in Section 4 are captured by this model. Based on the number of years spent for a particular IP in the patent process for a given country, the schedule of IP costs, and any future plans, the total yearly budget estimates are calculated, and compared with actual budgets.

## 5.2. The DSS facilities

IPManager provides the following facilities: updating records for each IP, deciding to abandon or continue an application path, and deciding to start or continue applications in particular countries.

The main screen of the DSS is shown in Fig. 5. There are facilities here to add/delete new IPs, add/ delete patent registration regions. Notice the annual plan roll-over button at the bottom. This permits annual updating of all the plans. The current plan is assumed to have been carried out, and the progress of the IP applications is incremented by 1 year.

Fig. 6 shows the screen reached by pressing the <sup>b</sup>Plan by IP<sup>Q</sup> button shown above (the information is disguised). This screen shows the fees to be paid this year, annual projected budget (total across all IPs, for each IP, for each IP type), lists of current IP items (patents, trademarks, PVRs), estimates of future expenses regarding IP rights.

![](/api/attachments/FB9QWBFG/fulltext/images/a3c15309e9da23ec8cd4a38dd1271c9fd254dabfb5b8e330d13069051836e163.jpg)  
Fig. 5. Main screen of IPManager.

The decision-maker can carry out <sup>b</sup>what-if?<sup>Q</sup> scenario analysis by typing x’s on the appropriate cells indicating continuance of the application process. On pressing the <sup>b</sup>update<sup>Q</sup> button, the resulting estimates of costs are shown by the DSS.

IPManager provides:

<sup>!</sup> decision support for various IP activities (continuance with certain existing IP rights, allowance of certain existing IP rights to lapse, and selection of countries for each new, or ongoing, IP item);

<sup>!</sup> yearly budget limit comparison;

<sup>!</sup> database of current IPs and costs; and

<sup>!</sup> lists of current IP according to type.

IPManager includes following characteristics of an effective DSS, as provided in the Turban’s [11] generic DSS framework:

<sup>!</sup> it supports but does not replace the decision maker, it neither tries to provide the <sup>b</sup>answers<sup>Q</sup> nor to impose a predefined sequence of analysis;

<sup>!</sup> it supports semi-structured decisions, where parts of the analysis can be systematized for the computer, but where the decision maker’s insight and judgment are needed to control the process;

<sup>!</sup> it combines modeling techniques with database and presentation techniques;

<sup>!</sup> it emphasizes ease of use, user friendliness, user control, and flexibility and adaptability; and

<sup>!</sup> it supports all phases of decision making.

However, the system does not interact with other computer based systems, such as the mainframe

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td></tr><tr><td>1</td><td>Planning by I.P.</td><td></td><td colspan="3">G.AOKAU</td><td></td><td colspan="3">Plant Variety Rights</td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td rowspan="3" colspan="2">Update</td><td rowspan="3" colspan="3">Main Screen</td><td rowspan="3" colspan="3">Plan by Country</td><td rowspan="3" colspan="3">Help</td><td></td></tr><tr><td>4</td><td></td></tr><tr><td>5</td><td></td></tr><tr><td>6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>Country</td><td>Year 1</td><td>Year 2</td><td>Year 3</td><td>Year 4</td><td>Year 5</td><td>Year 6</td><td>Year 7</td><td>Year 8</td><td>Year 9</td><td>Year 10</td><td></td></tr><tr><td>8</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9</td><td>ARGENTINA</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>AUSTRALASIA</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11</td><td>BRAZIL</td><td>x</td><td>x</td><td>x</td><td>x</td><td>1000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12</td><td>CANADA</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td></td><td></td><td></td></tr><tr><td>13</td><td>CHINA</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td></tr><tr><td>14</td><td>EUROPE</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15</td><td>JAPAN</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>16</td><td>RUSSIA</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td></td><td></td></tr><tr><td>17</td><td>SOUTH AFRICA</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td></td><td></td></tr><tr><td>18</td><td>UK</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>19</td><td>USA</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td></tr><tr><td>20</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>21</td><td>Total this IP</td><td>113100</td><td>100400</td><td>132500</td><td>10400</td><td>91000</td><td>68600</td><td>18900</td><td>56800</td><td>10900</td><td>13000</td><td></td></tr><tr><td>22</td><td>Total all IPs</td><td>113100</td><td>100400</td><td>132500</td><td>10400</td><td>91000</td><td>68600</td><td>18900</td><td>56800</td><td>10900</td><td>13000</td><td></td></tr><tr><td>23</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>24</td><td>Budget</td><td>160000</td><td>1200000</td><td>1100000</td><td>700000</td><td>600000</td><td>600000</td><td>600000</td><td>600000</td><td>600000</td><td>600000</td><td></td></tr><tr><td>25</td><td>Surplus/Deficit</td><td>46900</td><td>1099600</td><td>967500</td><td>689600</td><td>509000</td><td>531400</td><td>581100</td><td>543200</td><td>589100</td><td>587000</td><td></td></tr><tr><td>26</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>27</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>28</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>29</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>30</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>31</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>32</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>33</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>34</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>35</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>36</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Cell E12 commented by Chuda Basnet

Fig. 6. Planning by IP.

computer of the organization to download and upload information. The stand-alone nature of the system means that updating of the system has to be done manually. This is a deficiency in the system, which was meant to be removed at a future time. This improvement has not been pursued as yet simply because the users have not felt a pressing need for this.

This section provided an overview of IPManager. In the following section we describe the development and implementation of this DSS.

## 6. The development, implementation, and impact of the DSS

## 6.1. Development

Initially, a team of developers and the proposed users of the system (which included the authors of this paper—two of the authors are the developers, and the other is now one of the actual endusers) was formed. The team had a number of preliminary meetings to clarify the issues at hand. Once the team had achieved a consensus on the IP scenario, a prototype was created in ExcelR, featuring the proposed system functions. The development process thus followed a prototyping approach. (<sup>b</sup>The iterative, prototyping approach is most common in DSS development when the information requirements are not known precisely<sup>Q</sup> [[11], p. 304]. The core of the DSS was developed as an ad hoc system from the ground up, using Visual BasicR extensions in an ExcelR spreadsheet application. This development did not require any structured analysis tools such as data flow diagrams or data dictionaries. Systematic testing assured that each process was error-free before the next layer of complexity was added. Pilot implementation enabled the team to work on both the model building and the interface between other components of the systems, allowing for the periodic testing of added enhancements and for checking on the performance of the whole system. The need for involvement and participation of the proposed users was recognized right from the beginning of the development phase. Version 1.0 of IPManager was used to obtain users’ feedback and reactions. At this time an expanded team (of the developers, high- and mid-level managers, and IP specialists) met many times to discuss the utility of the prototype and improvements that the developers made to it. As a result the system was refined, expanded and modified.

## 6.2. Implementation and current use

The distinction between the development and the hand-over of the system was quite blurred. No training was required as the endusers are very knowledgeable of the related decision environment. They became fully familiar with the use of IPManager during the development meetings mentioned in the previous section, and are proficient in the use of spreadsheets and databases. The system is currently used by the IP administrator at the user organisaton, who uses it to estimate the effects of IP decisions and to provide these estimates to managers. The system is also used by the general manager, the chief financial officer, and accountants. The developers (the first two authors) are contacted from time to time concerning the use and possible extensions to the system.

## 6.3. The impact of the DSS

Any DSS needs to conform to the hierarchical nature of decision making: compared to lower level decisions the top level decisions are made with a longer planning horizon and the amount of detail is lesser at the higher echelons of decision making. As decisions are made further down the hierarchy, the lower level decisions are subservient to the higher level decisions. In considering the impact of IPManager, it is important to realise that the system was designed for use by the upper levels of management. At this level the planning was done on an aggregated basis—the costs for the different types of IPs were aggregated into one, the unit of the planning horizon was aggregated to 1 year. For this reason, it is not designed for some uses—it does not help in planning month by month, for example. This level of aggregation suited the users well and the system provided acceptable results for the general manager, the chief financial officer, and accountants.

The IP administrator, who is the primary user of this system, said that before the implementation of this system, the organisation depended on outside patent attorneys for planning all IP-related activities. After the implementation, they still needed to consult with the attorneys about the detailed plans and costs, but the DSS provided a rough-cut estimate of the yearly costs. The variance between the actual costs in a recent financial year (July 2002 to June 2003) and the estimates forecasted by the system was only 8%, which was considered satisfactory by the IP manager.

Another benefit cited by the user was that before the implementation of the system the organisation simply responded to notices from patent attorneys, as the attorneys progressed through various stages of the IP process. With the new system in place, the user can make plans on a more proactive basis, by working through various <sup>b</sup>what-if<sup>Q</sup> scenarios. In one decision cited by the user, one option was to start the IP process in 3 PCT and 3 non-PCT countries; the other option was to file for the IP in New Zealand only. After examining the projection of costs, it was decided to pursue the IP in New Zealand only. It was felt that at the aggregate level the system was sufficient for decision making by the high-level management, but some stake-holders, such as business managers felt that they needed more specific detailed information to do their planning.

In general, DSS benefits are often uncertain and are difficult to assess. This is especially the case with the prototyping approach, where development is evolutionary. The ongoing schedule changes and changing environments make it even more so. The true value of a DSS is whether it improves a manager’s decision making, which is not easily measured. Therefore, the traditional cost benefit analysis will not be able to capture all DSS benefits [8,11]. Actually in some cases, it may not be well suited to the DSS. However, some of the benefits in our case can be measured, such as a reduction in fee payment administrative costs and time. The system also has intangible benefits, such as enabling: the fine tuning of existing fee payment schedules, the creation of entirely new schedules, strategic planning, efficient IP utilization, and the flexibility to plan for and cope with unexpected situations. The DSS allows the users to carry out ad hoc analysis through <sup>b</sup>what if? <sup>Q</sup> queries. It also provides users with a better understanding of the IP fee management process, such as highlighting seemingly illogical decisions.

IPManager has been able to improve the visibility of IP plans and their associated future costs to the decision makers, which was formerly obscured by the interactions needed with the attorneys. It provides a quick and effective assessment of the decisions that are under consideration. The bottom line is that the users of IPManager have expressed satisfaction at the decision support provided by the DSS.

## 7. Conclusions and summary

We introduced a DSS, called IPManager, which is designed to address issues concerning the management of the events and fees that are incurred in the process of protecting intellectual property rights. IPManager seeks to assist financial planners and controllers at every step of this process. It does not automate the decision making process but helps planners by providing tools to create schedules, choose between plans, generate alternative plans, and to assess alternative plans with respect to given criteria.

In summary, this paper shows that IP protection and the resulting fee payment management is a complex process, involving large amounts of subjective and objective information and requiring expert judgment. IPManager is designed to support research managers in coping with such complex situations.

## References

[1] B. Arinze, M. Igbaria, L.F. Young, A knowledge based decision support system for computer performance management, Decision Support Systems 8 (1992) 501– 515.

[2] A.W. Beggs, The licensing of patents under asymmetric information, International Journal of Industrial Organization 10 (1992) 171– 191.

[3] R.H. Bonczek, C.W. Holsapple, A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, 1981.

[4] A. Bousquet, H. Cremer, M. Ivaldi, M. Wolkowicz, Patent licensing and risk sharing-simulation results, Annales Des Telecommunications 50 (1995) 297 – 305.

[5] J. Couillard, A decision support system for vehicle fleet planning, Decision Support Systems 9 (1993) 149 – 159.

[6] M.C. Er, Decision support systems: a summary, problems, and future trends, Decision Support Systems 4 (1988) 355– 363.

[7] G. Islei, G. Lockett, B. Cox, S. Gisbourne, M. Stratford, Modelling strategic decision-making and performance measurement at ICI Pharmaceuticals, Interfaces 21 (1991) 4 – 22.

[8] P.G.W. Keen, Decision support systems: the next decade, Decision Support Systems 3 (1988) 253– 265.

[9] J.E. Lanjouw, Patent protection in the shadow of infringements: simulation estimations of patent value, Review of Economic Studies 65 (1998) 671– 710.

[10] W.J. Parker, A.E. Dooley, C.K. Dake, Decision support for farm business strategy: an example for sheep breeding, in: L. Oxley, F. Scrimgeour (Eds.), Proceedings of the International Congress on Modelling and Simulation, 1999, Hamilton, New Zealand.

[11] E. Turban, Decision support and expert systems: management support systems, 3rd ed., Macmillan, New York, 1993.

[12] J. Zarocostas, Patent fees are cut again, National Law Journal 21 (1998) A13.

![](/api/attachments/FB9QWBFG/fulltext/images/e02413acc34d2a7bcc9fb46759ad0d980ff98b06906f2479a5843123a21294fe.jpg)  
Chuda Basnet is a Senior Lecturer at the Waikato Management School, New Zealand. He has received a Bachelor’s degree in Mechanical Engineering, a Master’s degree in Industrial and Management Engineering, and a PhD in Industrial Engineering and Management. His research interests are in the areas of manufacturing modeling, supply chain management, and decision support systems. He has previously published in Decision Support Systems, the

Journal of the Operational Research Society, and the Annals of Operations Research.

![](/api/attachments/FB9QWBFG/fulltext/images/bd6427e18ffe15b3c9a981de3345860047487c568abfe24e81cfc2c92f202b3c.jpg)

Les Foulds is a Professor of Manufacturing Management at the Waikato Management School, New Zealand. He received his BSc in Mathematics in 1970 and his MSc with honours in Mathematics in 1972, both from The University Auckland, and his PhD in Operations Research in 1974 from Virginia Polytechnic Institute. His main areas of research are in manufacturing management and the applications of graph theory and integer programming to traffic

planning, facilities layout and scheduling. He has published numerous articles on these topics in journals such as: Nature, Operations Research, Management Science, the European Journal of Operational Research, Journal of the Operational Research Society, and the Annals of Operations Research.

![](/api/attachments/FB9QWBFG/fulltext/images/7c44e6f371bb755755a52ef284ce5a46d3cffb813b598c8333978f24a6199dee.jpg)

Warren Parker is Chief Operating Officer, AgResearch Science, New Zealand. Prior to joining AgResearch in 1998, he was Professor of Farm Management and Agricultural Systems at Massey University where he completed a MAgrSc (Hons I) in Farm Management (1984) and PhD in Animal Science (1990). A Director of several research companies, his research interests span agribusiness, pastoral farming systems and farm management. He has

published on these topics in journals such as: Dairy Science, Agricultural Science (Cambridge), Animal Science and New Zealand Agricultural Research.
