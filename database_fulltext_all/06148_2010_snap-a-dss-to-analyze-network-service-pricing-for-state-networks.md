---
otero_id: 6148
otero_key: "E587KNW2"
title: "SNAP: A DSS to analyze network service pricing for state networks"
authors: "Jongsawas Chongwatpol; Ramesh Sharda"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.05.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# SNAP: A DSS to analyze network service pricing for state networks

Jongsawas Chongwatpol, Ramesh Sharda ⁎

Institute for Research in Information Systems, Spears School of Business, Oklahoma State University, Stillwater, OK 74078, USA

## a r t i c l e i n f o

Article history: Received 30 December 2008 Received in revised form 1 November 2009 Accepted 19 May 2010 Available online 18 June 2010

Keyword: Telecommunications Spreadsheet modeling Decision support systems

## a b s t r a c t

This study describes the implementation of a spreadsheet-oriented Decision Support System (DSS) that helps in making telecommunications pricing decisions. The system, SNAP-DSS or Service Network Application and Pricing (SNAP)-based DSS, is developed using Microsoft Excel 2007 that also incorporates VBA programming language. We present this research within the context of OneNet, a non-pro<sup>fi</sup>t state telecommunications service agency. The SNAP-DSS offers the ability to select the rate card options that best <sup>fi</sup>t the preferred pricing strategies by providing a real-time, user-friendly, graphical user interface. The DSS not only captures the effect of changes in the pricing factors on each rate card option, but also allows the user to analyze various rate card options in different scenarios using different parameters. The paper includes some lessons learned for the DSS community.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Telecommunications network services to educational institutions and government entities are typically provided by a mix of private and public organizations. Many states in the United States and indeed around the world have one or more state agencies that are responsible for providing network services to schools, colleges, and other state agencies. One example of such an agency is OneNet, a division of the Oklahoma State Regents for Higher Education. It was established in 1995 with the initial goals not only of providing cost-effective, equalized access to advanced network and telecommunications services to educational, governmental, and health care entities, but also of advocating, supporting, and facilitating the integration of advanced technologies. The main clients served by OneNet are K-12 schools, colleges and universities, career technology centers, courts, libraries, state and federal agencies, and hospitals and clinics.

Usually agencies such as OneNet operate as an enterprise-type fund. They must recover their costs through billing their clients and/or by justifying appropriations directly from the state legislatures. Rapid changes in the economic environment, client utilization, and technologies have increased pressures on the network's infrastructure, client connection policies, and the operating budget, raising the question as to whether the current rates are adequate to recover its cost of operation. Moreover, dependence on state appropriations and federal reimbursements creates <sup>fi</sup>scal vulnerability in terms of network technology innovations and cash <sup>fl</sup>ow. As a result, these agencies face a need to reassess the revenues generated under the current pricing policy to ensure that they at least recover cost, while providing quality telecommunications services over the long term in an ef<sup>fi</sup>cient manner.

State network agencies have adopted different pricing methodologies to bill their clients or to justify funding from their sponsoring state legislatures. However, no comprehensive decision support mechanism is in place to allow these agencies to develop and justify their pricing methods. Thus, the purpose of this study is to describe the implementation of a Services Network Application and Pricing (SNAP) spreadsheet-based Decision Support System (DSS), also called “SNAP-DSS,” that helps in making telecommunications pricing decisions for state network organizations. Although we present this research in the context of OneNet, it is equally applicable to other providers of telecommunications services.

This paper is organized as follows. First, Section 2 contains a brief literature review of the constructs in SNAP-DSS development. OneNet's current rate structure and associated issues are then analyzed in Section 3. Section 4 presents the SNAP-DSS implementation, which includes the overall SNAP-DSS system architecture and the proposed rate card options. Finally, the managerial analyses, system use, evaluation and feedback, and DSS lessons learned from this study are discussed, in Sections 5–8, respectively.

## 2. Brief literature review

This section introduces the literature on telecommunications pricing and decision support systems, speci<sup>fi</sup>cally spreadsheet-based DSS, highlighting related key advances. Additional literature is cited in describing the pricing policies implemented in the DSS.

## 2.1. Telecommunications pricing models

Many pricing schemes have been proposed for pricing telecommunications networks. These pricing schemes can be classi<sup>fi</sup>ed into three main categories: cost-based pricing, pricing for best-effort services, and pricing with Quality of Service (QoS) guarantees.

Cost-based pricing refers to a pricing structure that is directly related to costs. Examples of cost-based pricing are Fully Distributed Cost (FDC) pricing, <sup>fl</sup>at rate pricing, and Ramsey pricing [4] (p. 161). FDC pricing is widely used due to its simplicity and the ability to audit the price construct. The primary concept of FDC pricing involves allocation among its clients of the total common and shared costs that the agency incurs for the services provided. Flat rate pricing, also commonly used by service providers, is based on the concept that customers are charged the average costs of providing services to all customers in the same customer group. A customer pays a <sup>fi</sup>xed amount for a service instead of for the actual usage [4] (p. 181). Ramsey pricing is another linear pricing scheme designed for monopolistic environments. It can be used to maximize social welfare and minimize economic misallocation under the constraint of recovering costs [4] (p. 131), [15]. Many service providers have adopted a cost-based pricing scheme not only because such schemes are simple and easy to implement without requiring any additional accounting architecture, but also because this gives the service providers an accurate way to predict and control costs as well as revenues. However, the issues of fairness to customers and resource utilization arise when some customers tend to overuse the resources, resulting in penalizing light users as compared to heavy ones. One way to overcome these issues is to employ best-effort pricing schemes.

“Best effort” refers to a network service that treats all types of traf<sup>fi</sup>c indifferently, with no delivery guarantee and with the possibility of traf<sup>fi</sup>c loss [18]. Best-effort pricing schemes in the literature include Smart Market [12], Paris Metro Pricing [17], Congestion Discount pricing [4] (p.219), [9], usage-based pricing, charging <sup>fl</sup>exible contract, Shadow Pricing, Edge pricing, Zone-based pricing, Priority pricing, and the Game theory models. (For a technical summary, see, [4] (p.235), [10,16]). Of these best-effort schemes, the focus in this study is on usage-based pricing, employed by many service providers, as well as charging <sup>fl</sup>exible contract scheme. The basic idea of usagebased pricing is to charge the customers for what they actually consume. This pricing scheme can be used to allocate service classes to different uses, to prioritize usage of a congested resource so that customers who value the access the most will get the highest priority, and to recover the costs of providing services [4] (p. 17), [13]. The charging <sup>fl</sup>exible contract pricing scheme can also bene<sup>fi</sup>t both service providers and customers. Customers can vary the amount of bandwidth by changing their contract without the need to predict and reserve maximum resource requirements, while the service providers can provide more services to customers, with or without the need to reserve the resources [4] (p. 235).

Lastly, QoS pricing schemes serve customers who are willing to pay more for services that ensure no traf<sup>fi</sup>c loss and provide timely delivery guarantees along with high performance data and video capabilities. QoS pricing involves technological enhancements such as Integrated Service (IntServ), Resource Reservation Protocol (RSVP), Multi-Protocol Label Switching (MPLS), and Differentiated Service (DiffServ) architectures [18]. Thus, QoS pricing schemes introduced in the literature are related to these network architecture issues. For instance, Karsten et al. [8] have proposed an embedded charging model in the RSVP architecture for an integrated services network. Fankhauser et al. [6] included the RSVP charging and accounting in the IntServ network. Additionally, Bouras and Sevasti [1] presented a model for the service provisioning procedure for the deployment of DiffServ-based Service Level Agreements (SLAs) in a bilateral fashion.

This brief literature review of network services pricing schemes is not intended to be comprehensive, but it does illustrate the large number of choices available to decision makers in agencies to select and implement pricing models. In our work, we adopt a decision support system framework for providing such support. The next section brie<sup>fl</sup>y introduces DSS concepts.

## 2.2. Decision Support Systems (DSS)

Turban et al. identify four fundamental components of a DSS: (1) data management subsystem, normally including the database management system (DBMS), (2) model management subsystem, a software package that provides the system's analytical capabilities, (3) user interface subsystem such as the Web browser, which provides a familiar, consistent graphical user interface (GUI) structure, and (4) knowledge-based management subsystem, which provides intelligence to support any decision [19] (p. 92). Even though many DSS applications have been introduced in the literature over the last decade, the following six DSS types are commonly observed: text-oriented DSS, database-oriented DSS, spreadsheetoriented DSS, solver-oriented DSS, rule-oriented DSS, and compound DSS [7]. The DSS built for this study is a spreadsheet-oriented DSS. Spreadsheet software packages are widely used because of their strength, <sup>fl</sup>exibility, and easy implementation. In this study, Microsoft Excel, including the Visual Basic for Application (VBA) programming language, is used to develop a spreadsheet application that provides a real-time, user-friendly, graphical user interface (GUI) for OneNet's pricing decisions.

## 3. OneNet's decision problem

Pricing models for OneNet's services were <sup>fi</sup>rst developed in 1995. The initial rate structure established in 1995 encompassed both onetime and on-going charges. The one-time charge was a service set-up charge for new customers, while the on-going charge was associated with continuing network services and was billed to clients on a monthly basis. The monthly network charge was equalized for all clients and for all connection types at a stated bandwidth in order to simplify the rate structure and billing process. It was also a directive of the legislature to ensure rural areas were not disenfranchised. In 2003, OneNet established a new cost-based pricing rate structure by focusing on the allocation of the costs of serving different types of clients and of different bandwidth offerings. Table 1 presents OneNet's current rate charges to clients with seven bandwidth-based tier charges. These rates were recommended by a consultant.

This rate structure has remained unchanged since 2003. As presented in Eq. (1), the rate charged for bandwidth level $" \mathrm { k } '$ is derived from the allocation of various types of costs associated with bandwidth level “k”. These costs include operations cost or infrastructure charge (O), transport charge (T), internet charge (I), and Last Mile or tail circuit charge (L). W refers to the weighting factor assigned to the bandwidth level “k”. This weighting factor was determined based on the historical data of the overall costs related to each bandwidth level. Note that this is the current method of pricing services that was recommended by a consultant but is not one of the new pricing models implemented in SNAP-DSS.

$$
R _ {k} = W _ {k} (O + T + I + L)\tag{1}
$$

The infrastructure charge or operations cost (O) refers to the cost of equipping and operating OneNet's hub sites. The transport charge (T) is the cost of circuits, either leased from vendors or state-owned <sup>fi</sup>bers that connect OneNet's hub sites. The Internet charge (I) is the amount paid to vendors for access to the Internet. The Last Mile or tail circuit charge (L) refers to the vendor's charge to connect OneNet's hub sites to a client's location. Portions of these cost components are combined into one rate charge for each level of bandwidth service as presented in Table 1.

Table 1  
OneNet's current monthly and annual rates.

<table><tr><td>Bandwidth level (k)</td><td>Baseline bandwidth</td><td>Infrastructure charge (per port)</td><td>Transport charge (bandwidth)</td><td>Internet charge (bandwidth)</td><td>Tail circuit charge (average)</td><td>Monthly rate</td><td>Annual rate</td></tr><tr><td>1</td><td>56 kb</td><td>$76</td><td>$13</td><td>$17</td><td>$157</td><td>$263</td><td>$3156</td></tr><tr><td>2</td><td>T-1</td><td>$132</td><td>$27</td><td>$34</td><td>$321</td><td>$514</td><td>$6168</td></tr><tr><td>3</td><td>Ethernet</td><td>$1719</td><td>$53</td><td>$67</td><td>$194</td><td>$2033</td><td>$24,396</td></tr><tr><td>4</td><td>DS-3</td><td>$1719</td><td>$133</td><td>$168</td><td>$1490</td><td>$3510</td><td>$42,120</td></tr><tr><td>5</td><td>Fast Ethernet</td><td>$1719</td><td>$199</td><td>$251</td><td>$131</td><td>$2300</td><td>$27,600</td></tr><tr><td>6</td><td>OC-3 (2)</td><td>$1719</td><td>$239</td><td>$302</td><td>ICB</td><td>ICB</td><td>ICB</td></tr><tr><td>7</td><td>GigaBit (3)</td><td>$1719</td><td>$531</td><td>$670</td><td>ICB</td><td>ICB</td><td>ICB</td></tr></table>

ICB: individual case basis.

The distribution of both the transport charge and the Internet access is based on the amount of bandwidth consumed: the higher the level of bandwidth services, the higher the proportion of allocated transport charges and Internet charges. The infrastructure charge consists of two main components: hub equipment costs and network operations and support costs. The distribution of this infrastructure charge is based on the number of physical ports consumed and the number of connections the client subscribes to. Lastly, the distribution of the tail circuit charge is based on the average actual fee paid to local telecommunications providers for all customers at a given bandwidth rate.

## 3.1. The problem

The rates OneNet currently charges for its services are straightforward, following a simple cost-based pricing model that averages all cost components for all clients at a given bandwidth rate as presented in Table 1. A variety of assumptions have been made based on the current network infrastructure, types of customers, and integration of new technologies and service offerings. For instance, the current rate structure is based on the assumption that even though differences in service costs exist among client groups, the equalized rate structure at a given bandwidth promotes customer acceptance of OneNet's rates and ef<sup>fi</sup>ciency in the billing and cost recovery processes. However, the current rate structure creates two major problems.

– First, the current rates are based on the estimated costs of operations and funding support in 2003 when they were last adjusted. As a result, the current rate structure does not re<sup>fl</sup>ect any changes in <sup>fi</sup>nancial support (State Appropriations, State Universal Service, and private funding) or the operating budget. For instance, if funding support is cut, the revenue generated from these <sup>fi</sup>xed rates will not cover OneNet's cost of operations. In addition, the current rate structure does not re<sup>fl</sup>ect the changes in E-Rate, funds from the Universal Service Fund to assist K-12 schools in obtaining affordable telecommunications and internet access.

– Second, the total number of clients subscribing to the services has been gradually decreasing for several years. While OneNet is the only of<sup>fi</sup>cial representative of the State Regents of Oklahoma to provide services to academic and governmental entities, many Internet Service Providers (ISPs) can provide the same services with the same or even lower rates, simply because OneNet rates are <sup>fi</sup>xed based on the bandwidth subscription, not on an individual case basis. By targeting the lower-cost circuits, other ISPs can offer clients attractive rates that OneNet cannot compete with in some speci<sup>fi</sup>c areas, similar to the “cherry picking” in the healthcare industry, for instance.

Beyond the two major problems stated above, other factors such as the high costs of new technology investments and upgrades, the costs to provide additional value-added services, or the cost associated with new bandwidth offerings generate the need to reassess whether OneNet's rates recover its costs of operations. The SNAP-DSS was developed to address these issues. Decision makers at OneNet also wanted to be able to evaluate different options and scenarios, so a DSS was the best framework to adopt for this problem.

## 4. SNAP-DSS implementation

One of the early steps in developing the DSS was to identify best practices in place for such pricing decisions. To acquire this information, we conducted an analysis of pricing practices in place at other states agencies. This process is described in the next section.

## 4.1. StateNet, The Quilt, and state network organizations

Like OneNet, most states in the United States have at least one nonpro<sup>fi</sup>t organization that was established to support the telecommunications needs of public institutions and higher education. Most of these state network organizations are members of the StateNets and The Quilt group. StateNets is a Net@EDU working group, operating under the program EDUCAUSE, a non-pro<sup>fi</sup>t association providing services for public sector organizations by promoting the intelligent use of information technology. The Quilt is another coalition of advanced regional network organizations aimed at promoting advanced networking services throughout the research and education network community. The mission of both StateNets and The Quilt is similar: to operate statewide networks that mainly serve a substantial portion of states' K-20 schools, higher education institutions, libraries, and state and municipal governments. In spring 2007, StateNets and The Quilt began a collaborative project to document business models through surveys with regard to these state network organizations' business and <sup>fi</sup>nancial plans, services and pricing strategies, funding sources, revenues, and expenditures. We used data from their surveys for this research.

Eighteen state network organizations from 50 states provided pricing information. The information was obtained from phone interviews, email, and especially from the StateNets and The Quilt surveys. 18 state network organizations from 50 states were involved in providing pricing information, among which seven were from the Midwest, four were from the Northeast, <sup>fi</sup>ve are from the South, and two were from the West. The participated state network organizations include Kan-ed (Kansas), KanREN (Kansas), OSCNet (Ohio), WisNet (Wisconsin), MoreNet (Missouri), MeritNet (Michigan), ICN (Illinois), NYSERNet (New York), OSHEAN (Rhode Island), NEREN (Northeast), Njedge.net (New Jersey), SLR/Sox (Georgia), OneNet (Oklahoma), FLR (Florida), LEARN (Texas), NCREN/MCNC (North Carolina), CENIC (California), and UEN (Utah). Even though the states have different ways of charging their clients, all pricing strategies from these 18 state network organizations can be categorized into the three main pricing schemes presented in the literature: cost-based pricing, pricing for best-effort services, and QoS pricing. These state network organizations' pricing strategies along with the pricing schemes from the literature were used as the best practices in order to provide various pricing options for OneNet. A detailed comparison of these pricing practices is reported in [3].

## 4.2. SNAP-DSS's overall system architecture

The core of the SNAP-DSS was developed and implemented in Microsoft Excel including VBA programming language. Figs. 1 and 2 provide an overview of the SNAP-DSS architecture and its user interface. All data input, all model parameters, and the data output are implemented on separate worksheets in Microsoft Excel.

## 4.2.1. Data input

The user is required to provide up-to-date information on budget and client information. For the budget information, various types of expenditures and funding sources are the main data input for this SNAP-DSS. These expenditures are distributed to individual clients based on assumptions and factors intended to <sup>fi</sup>nd out the total cost to provide services to individual clients (see Section 4.3.1). Additionally, client information such as Last Mile costs, Full Time Enrollment (FTE), actual bandwidth usage, value-added services, current bandwidth subscription, and current rate charged are used for further pricing analysis.

## 4.2.2. Model parameters

Once all data inputs have been provided, the next step is to select model parameters that best <sup>fi</sup>t preferred pricing strategies. These model parameters include (1) database selection, (2) weighting factor, (3) actual bandwidth usage, (4) percent surcharge for over bandwidth usage, (5) percent overall pro<sup>fi</sup>t, (6) multiple-year discount, (7) percent discount, (8) estimated total annual disconnection fees, and (9) percent surcharge for early disconnection. By adjusting these model parameters, the user can determine the appropriate rates. Details on how to select model parameters are discussed in Section 5.

## 4.2.3. Data output

After all input data have been entered and model parameters have been adjusted, the SNAP-DSS will automatically produce three major outcomes: (1) ten rate card options as alternatives for OneNet to charge its clients for the services, (2) baseline revenue comparisons among those proposed rate card options for an individual client, and (3) overall cost–revenue analyses to determine which rate card options provide the most value for both OneNet and its clients. When a new set of data has been provided or the model parameters have been readjusted, these outcomes are automatically regenerated and used for further pricing analysis.

## 4.3. The proposed rate card options

SNAP-DSS is able to generate various rate card options that a state telecommunication agency can use in charging its clients. In this study, ten rate card options are proposed as presented in Fig. 3. Even though three main pricing schemes are presented in the literature, these ten rate card options are based only on cost-based pricing and best-effort pricing schemes, as currently OneNet's network architecture does not support billing on the basis of a choice of Quality of Service. Six rate card options are proposed under the cost-based pricing schemes, three rate card options follow the best-effort pricing schemes and the last rate card option is derived from the average rate from all nine proposed rate card options. Some of these rate cards options are discussed as follows.

## 4.3.1. Option 1: Individual cost-based rate

In developing the new rate structure, the <sup>fi</sup>rst task begins with the distribution of all costs from the natural expenditure classi<sup>fi</sup>cations de<sup>fi</sup>ned in the <sup>fi</sup>scal year budget to nine functional expenditure categories: Last Mile costs (L), administrative costs (A), operations costs (O), equipment costs (E), channelized costs (C), V-lan costs (V), <sup>fi</sup>xed costs (F), hub costs (H), and network costs (N).

– Last Mile costs refers to the fees paid to vendors to connect OneNet hub sites to client locations.

– Administrative costs refers to the costs of salaries, wages, insurance premiums, retirement contributions, temporary employees, and workers' compensation.

– Operations costs refers to the costs of operating hub sites including rent expenses, freight expenses, information services, Library database subscriptions, and Internet2 membership fees

– Equipment costs refers to the costs of equipping the hub sites, including tower utilities; supplies, materials, and other furniture; and vehicles

– Channelized costs refers to the special costs to provide T1- bandwidth services

– V-lan costs refers to the special costs to provide Ethernet, Fast Ethernet, Gigabit and 10 Gigabit Ethernet services

– Fixed costs refers to the costs of core <sup>fi</sup>ber, optronics, and ampli<sup>fi</sup>ers invested over 20 years and the maintenance costs of the <sup>fi</sup>ber – Hub costs refers to the fees paid to vendors to operate hub sites

– Network costs refers directly to the costs of operating networks, including circuit costs, NLR cost, <sup>fi</sup>ber relocation costs, network equipment, bond indebtedness and expenses, refunds, and restitutions.

![](/api/attachments/E587KNW2/fulltext/images/5531973aceb3eebd217073857fab333c9a1e7573bbd3a99e1ce186fe4617dc59.jpg)  
Fig. 1. SNAP-DSS architecture.

![](/api/attachments/E587KNW2/fulltext/images/117cc24bfa287e8a8071eb2fff6bb9a091d1e958c4e1abfe99b7de38bc075686.jpg)  
Fig. 2. SNAP-DSS user interface.

After all costs de<sup>fi</sup>ned in the <sup>fi</sup>scal year budget are distributed into the functional expenditure classi<sup>fi</sup>cations rede<sup>fi</sup>ned in the SNAP-DSS, the next step is to distribute these functional costs to individual clients based on bandwidth subscriptions and the member groups.

OneNet is a non-pro<sup>fi</sup>t organization, meaning that the total cost of operations $\left( \mathsf { C } _ { \mathrm { T O T A L } } \right)$ is recovered by funding support (F) and revenue (R) from clients, with the goal of zero pro<sup>fi</sup>t as presented in Eq. (2), where “T” refers to the total number of OneNet clients and $" \mathrm { n } "$ refers to the total number of funding sources. The sum of all functional costs allocated to each client represents the rate OneNet should bill the clients.

![](/api/attachments/E587KNW2/fulltext/images/d24017947a6ac17a197cc2a3ebfcff148427775b274312d2f33258b6eb27feae.jpg)  
Fig. 3. Rate card structure.

$$
C _ {\mathrm{TOTAL}} = \sum_ {i = 1} ^ {T} R _ {i} + \sum_ {i = 1} ^ {n} F _ {i}\tag{2}
$$

Eq. (4) presents the monthly cost-based rate Option 1, which is adapted from the Fully Distributed Cost (FDC) pricing from [4] (p. 181) and from the cost allocation methods adopted by many state network organizations. The rate charged to client ${ \bf \bar { \Psi } } _ { \bf i ^ { \prime } \Psi } ( \bf R _ { 1 , i } )$ who is in the member class $" \boldsymbol { { \mathrm { c } } } "$ and subscribes to the bandwidth $" s "$ is derived from the allocation of all functional costs using a group weighting factor (G<sub>i</sub>) and a bandwidth scaling factor (B<sub>i</sub>).

$$
R _ {1, i} (c, s) = \left(\frac {G _ {c , i}}{\sum_ {1} ^ {T} G _ {c , i}} (A + E + C + V)\right) + \left(\frac {B _ {s , i}}{\sum_ {1} ^ {T} B _ {s , i}} (O + F + H + N)\right) + L _ {i}\tag{3}
$$

When $\mathtt { R } _ { 1 , \mathrm { i } } { \in } \mathtt { c }$ where $" \mathrm { c } "$ refers to the class of members, ${ \mathfrak { c } } = 1$ to 5. $\mathtt { R } _ { 1 . \mathrm { i } } \in s$ where $" s "$ refers to the class of bandwidth subscription, $s = 1$ to 12.

The term $\frac { G _ { c . i } } { \sum _ { 1 } ^ { T } G _ { c . i } }$ provides a weighted average of class-based weight factors for a particular client in class $" \mathrm { c } "$ . Similarly $\frac { B _ { s . i } } { \sum _ { 1 } ^ { T } B _ { s . i } }$ provides a weighted average of bandwidth-based weight factors for a particular client subscribing to bandwidth level $" s " .$ . By summing the factors across all clients, the denominator becomes a weighted sum of the factors based on number of clients in each category. These terms allow the relevant costs to be allocated to a speci<sup>fi</sup>c client based on the clients' member class $" \boldsymbol { { \mathrm { c } } } "$ and bandwidth level “s”. These are described further in the next few paragraphs.

Table 2 presents the bandwidth scaling factor for different types of bandwidth offerings. Generally, the idea of the bandwidth scaling factor is that clients who subscribe to higher bandwidths (Mbps) should be more responsible for the higher cost than those subscribing to lower bandwidths (Mbps). This bandwidth scaling factor begins with the calculation of the ratio of bandwidth represented by each bandwidth category. However, if ratios are based on the pure bandwidth speed, the result is an unreasonable range of bandwidth ratios. For instance, using T1 (1.5 Mbps) as the baseline ratio, the bandwidth scaling factor for T1 is equal to 1 and the bandwidth scaling factor for 10 Gigabit Ethernet (10,000 Mbps) is equal to 6666.67. Because the bandwidth ratio has a great impact on the allocation of functional costs, the range of rates is unreasonable. Accordingly, the square root of the bandwidth ratio is used instead of using pure bandwidth ratios in order to reduce the range. The adjusted bandwidth scaling factor (see Table 2) is then used as part of the cost allocation method throughout this study.

Bandwidth scaling factors (B ).

<table><tr><td>Bandwidth class (s)</td><td>Circuit speed</td><td>Mbps ( $B_s$ )</td><td>Bandwidth scaling factor</td><td>Adjusted bandwidth scaling factor ( $B_i$ )</td></tr><tr><td>1</td><td>56K</td><td>0.056</td><td>0.04</td><td>0.19</td></tr><tr><td>2</td><td>T1</td><td>1.5</td><td>1.00</td><td>1.00</td></tr><tr><td>3</td><td>Ethernet</td><td>10</td><td>6.67</td><td>2.58</td></tr><tr><td>4</td><td>DS3</td><td>44.736</td><td>29.82</td><td>5.46</td></tr><tr><td>5</td><td>Fast Ethernet</td><td>100</td><td>66.67</td><td>8.16</td></tr><tr><td>6</td><td>OC-3</td><td>155</td><td>103.33</td><td>10.17</td></tr><tr><td>7</td><td>OC-12</td><td>622</td><td>414.67</td><td>20.36</td></tr><tr><td>8</td><td>Gigabit Ethernet</td><td>1000</td><td>666.67</td><td>25.82</td></tr><tr><td>9</td><td>10 Gigabit Ethernet</td><td>10,000</td><td>6666.67</td><td>81.65</td></tr><tr><td>10</td><td>Lan 1 Mb</td><td>1</td><td>0.67</td><td>0.82</td></tr><tr><td>11</td><td>Lan 3 Mb</td><td>3</td><td>2.00</td><td>1.41</td></tr><tr><td>12</td><td>Lan 5 Mb</td><td>5</td><td>3.33</td><td>1.83</td></tr></table>

The group weighting factor is also important in this cost allocation method. As OneNet receives funding support from the government for the research and academic institutions group, the costs allocated to this group should be matched with the funding support. As a result, OneNet sets a high weighting factor for the research and academic institutions group, meaning that these groups will be responsible for higher networks and operations costs, while the non-academic group, with a low weighting factor, will receive a secondary bene<sup>fi</sup>t by having access to network services at the lower costs of providing services. As presented in Table 3, OneNet's clients can be classi<sup>fi</sup>ed into <sup>fi</sup>ve primary groups based on funding support and billing systems. Group 1 refers to higher education clients including two-year and four-year public and private universities and community colleges. Group 2 refers to public and private K-12s and libraries. Group 3 refers to hospitals, healthcares, and clinics. Group 4 refers to state or local government agencies. Group 5 refers to any af<sup>fi</sup>liate: army national guard, court, federal, law enforcement, and municipality clients. In this study, the weighting factor for group 1, higher education, and group 2, K-12, are set at 2.00 and that for the other groups is set at 0.5, meaning that if the cost to operate OneNet's networks, for instance, is \$55,000 per month, groups 1 and 2 will be responsible for \$20,000 each, while groups 3, 4, and 5 will be responsible for \$5000 each.

However, there are two main assumptions in allocating these functional costs. First, unlike other functional costs that are allocated to each client, Last Mile $\left( \mathrm { L } _ { \mathrm { i } } \right)$ in Eq. (4) is the actual cost paid to vendors to connect OneNet hub sites to client locations. Thus, Last Mile is the primary factor that differentiates rates charged to clients who are in the same group category and subscribe to the same bandwidth, as the Last Mile cost varies depending on clients' business location, bandwidth, and the rate offered by vendors. Second, clients whose business locations are connected directly to OneNet's hub sites through its owned <sup>fi</sup>ber networks will not be responsible for any Last Mile charges but only for the shared <sup>fi</sup>xed costs, de<sup>fi</sup>ned as the cost of the core <sup>fi</sup>ber, optronics, and ampli<sup>fi</sup>ers OneNet invests in to provide services. In contrast, clients whose business locations are connected to OneNet's hub sites via third party vendors will be responsible for Last Mile charges but not for any <sup>fi</sup>xed costs.

## 4.3.2. Option 2: Linear regression-based pricing

Eq. (4) presents another rate structure that is formulated as a linear regression model to recover all functional costs. The regression equation is derived using SAS, the statistical analysis software. The data used in this regression analysis are from the allocation of all functional costs in Section 4.3.1. Note that for a non-pro<sup>fi</sup>t organization, the primary goal is cost recovery; therefore, the values of dependent variables for calibrating models are from the actual cost allocated to individual clients, de<sup>fi</sup>ned as Rate $( \mathrm { R } _ { 1 . \mathrm { i } } )$ . The associated independent variables are Last Mile costs (L), administrative costs (A), operations costs (O), equipment costs (E), channelized costs (C), Vlan costs (V), <sup>fi</sup>xed costs (F), hub costs (H), and network costs (N). In this analysis, we split the data at random into two sets (estimation and validation data), build the regression model on the estimation data, apply this regression model on the validation data, and then compare predictive <sup>fi</sup>t and regression estimates between the estimation sample data and validation sample data. We also perform stepwise regression on these independent variables to simplify the model and to determine which variables are among the highest correlation with the dependent variables.

Group weighting factors (G ).

<table><tr><td>Member class (c)</td><td>Client type</td><td>Weight ( $G_i$ )</td></tr><tr><td>1</td><td>Group1—higher education</td><td>2.00</td></tr><tr><td>2</td><td>Group2—K12 and library</td><td>2.00</td></tr><tr><td>3</td><td>Group3—hospital and clinic</td><td>0.50</td></tr><tr><td>4</td><td>Group4—state agency</td><td>0.50</td></tr><tr><td>5</td><td>Group5—others</td><td>0.50</td></tr></table>

The coef<sup>fi</sup>cient of determination (R<sup>2</sup>) with these nine variables is about 80% on both estimation and validation sample data. However, after running the stepwise regression analysis, the selected independent variables (Last Mile, bandwidth, and member class) are simple and reasonable to explain and predict with less error the rates charged to individual clients $( \mathrm { R } ^ { 2 } = 7 \bar { 5 } \% )$ . Thus, the linear regression rate charged to individual client “i” $\left( \mathrm { R } _ { 2 . \mathrm { i } } \right)$ is a function of the baseline bandwidth subscription $( \mathtt { B } _ { \mathrm { s , i } } ) ,$ , the member class (c ), and the Last Mile (L ) cost. Clients within the same group subscribing to the same bandwidth are responsible for the same underlying costs. Again, the Last Mile is the only factor that differentiates the rates charged to speci<sup>fi</sup>c clients.

$$
R _ {2. i} (c, s) = 1 0 2 6. 0 6 4 7 4 + 2. 5 7 9 9 8 \left(B _ {s. i}\right) - 1 5 5. 5 7 4 6 2 \left(c _ {i}\right) + 1. 0 8 6 0 9 \left(L _ {i}\right)\tag{4}
$$

## 4.3.3. Option 3: Non-linear regression-based pricing

Adapted from a state network organization (Merit)'s pricing structure, Eq. (5) presents a non-linear regression rate structure as another alternative for determining the rates charged to individual clients. By following the same regression analysis as in Section 4.3.2, the <sup>fi</sup>nal rate charged to individual client $\ " \mathrm { ~  ~ } ^ { \ast } \mathrm { ~ \ ' ~ } ( \mathrm { R } _ { 3 . \mathrm { i } } )$ is reformulated as the function of the baseline bandwidth subscription $\left( \mathtt { B } _ { \mathrm { { s } , i } } \right)$ in the form of an exponential function.

$$
R _ {3. i} (s) = - 1 8. 6 2 0 5 + 5 5 6. 3 (B _ {s. i} ^ {0. 4 2 3 9})\tag{5}
$$

The rate derived from the non-linear regression is based on the direct variation in bandwidth subscriptions. The higher the bandwidth clients subscribe to, the higher the rate charged to clients. In contrast, the rates derived from the linear regression vary not only depending mainly on the Last Mile, but also on the direct variation of bandwidth subscription and the reverse variation of the client group.

## 4.3.4. Option 4: Twelve-tier bandwidth-based rate

The <sup>fi</sup>rst three rate structures are analyzed on an individual case basis: clients are charged based on the actual functional cost allocated to each client. However, charging clients on an individual case basis might not be achievable. Thus, the bandwidth-based rate option is introduced and analyzed with the concept that all clients subscribing to the same bandwidth are responsible for sharing the same underlying costs. After the actual functional costs are allocated to each client, the next step is to average those cost components for all clients at the same bandwidth rate. Eq. (6) presents the bandwidthbased rate for bandwidth $" s " \left( \mathrm { R } _ { 4 . s } \right)$ , which is derived from the total costs of providing services to all clients who subscribe to bandwidth $\begin{array} { r } { { ^ { u } S ^ { \prime \prime } } \left( \sum _ { i = 1 } ^ { \hat { T } _ { S } } ( R _ { 1 . i } ) _ { S } \right) } \end{array}$ divided by the total number of clients in each bandwidth class (T ). This bandwidth-based rate card option is adapted from OneNet's current pricing structure and from other state network organizations such as OSCNet, FLR, LEARN, NCREN, and OSHEAN.

$$
R _ {4. s} = \frac {\sum_ {i = 1} ^ {T _ {s}} (R _ {1 . i}) _ {s}}{T _ {s}}\tag{6}
$$

## 4.3.5. Option 7: Individual usage-based pricing option 1

The cost-based pricing schemes (rate card options 1–6) have two major <sup>fl</sup>aws: penalizing light users with respect to heavy users and encouraging resource waste resulting in less ef<sup>fi</sup>cient resource utilization. However, by adopting best-effort pricing through usagebased pricing, OneNet can charge its clients based on their actual use of network resources. Eq. (7) presents the usage-based rate for individual client $\ " \mathrm { ~  ~ } ^ { \mathrm { ~ t ~ } } ( \mathrm { R } _ { 7 . \mathrm { i } } )$ , which is developed from the cost-based rate $( \mathrm { R } _ { 1 . \mathrm { i } } )$ , as presented in Eq. (4) by including actual bandwidth usage $\left( \mathtt { B } _ { \mathtt { A } } \right)$ , into the model. Also, a penalty charge (P) or surcharge is applied when client $" _ { 1 } "$ consumes resources above the baseline bandwidth subscription $\left( \mathtt { B } _ { \mathrm { s , i } } \right)$

$$
\begin{array}{l} R _ {7, i} (c, s) = \left(\frac {G _ {c , i}}{\sum_ {1} ^ {T} G _ {c , i}} (A + E + C + V)\right) + \left(\frac {B _ {s , i}}{\sum_ {1} ^ {T} B _ {s , i}} (O + F + H)\right) + L _ {i} \\ + \left(\left(\frac {N G _ {c , i}}{\sum_ {1} ^ {T} G _ {c , i}}\right) \left(\frac {B _ {s , i}}{\sum_ {1} ^ {T} B _ {s , i}}\right) \left(1 + \frac {P (B _ {A , i} - B _ {s , i})}{B _ {s , i}} \times 1 0 0\right)\right) \end{array}\tag{7}
$$

## 4.3.6. Option 9: Six-tier guaranteed bandwidth-based rate

The six-tier guaranteed bandwidth-based rate is adapted from the best-effort pricing scheme “charging <sup>fl</sup>exible contracts” from [4] (p. 235) and from a state network organization (Merit)'s rate card structure. Even though the baseline rates are developed under the cost-based pricing schemes, the minimum bandwidth for a particular client is speci<sup>fi</sup>ed by the contracted bandwidth fee, plus any additional charge for the actual peak bandwidth used each month. The penalty charge is determined on an individual basis. Additionally, if the client consumes resources above the baseline bandwidth subscription in three consecutive months, the highest amount used during those months will become the new baseline bandwidth.

## 4.3.7. Option 10: The average rate from all nine proposed rates

The last rate card option in this study is derived from the average rates from all nine proposed rates. This average rate is bene<sup>fi</sup>cial to OneNet in that it reduces pricing errors from all nine rate card options. These pricing errors, resulting in overcharging or undercharging, may include errors in allocating all functional costs, errors in determining bandwidth scaling factors or group weight factors, or errors in computing each rate card option.

However, in order to select the rate card option that values both OneNet and its clients the most, it is important to analyze the baseline revenue generated from those ten proposed rate card options for an individual client and to conduct an overall cost–revenue analysis to ensure the <sup>fi</sup>nancial sustainability of the organization in the future. The next section, “Managerial Analysis,” presents scenarios to show how to use this SNAP-DSS when the model parameters have been changed and how to determine the rate card that best <sup>fi</sup>ts OneNet's strategic plan.

## 5. Managerial analyses of rate card options

This SNAP-DSS enables the user to analyze various rate card options, the baseline revenue, and overall cost–revenue structure when some input data or model parameters are changed. To illustrate the SNAP-DSS capabilities, each analysis is discussed in this section. The <sup>fi</sup>rst task in utilizing this SNAP-DSS is to provide up-to-date data input. On the expenditure input worksheet (see Appendix $\mathsf { A } ) ,$ the user is required to identify “Type of Cost,” the functional expenditure categories used in the cost allocation procedure. These functional expenditure categories include Last Mile costs, administrative costs, operations costs, equipment costs, channelized costs, V-lan costs, <sup>fi</sup>xed costs, hub costs, and network costs. For instance, “Professional services” can be categorized as an administrative cost, while “Maintenance $\boldsymbol { \mathrm { C o s t s } } ^ { \nu }$ is the category for network costs. After the user provides the input data for all related expenditures, Last Mile (see Appendix B), FTE, actual bandwidth usage, value-added services, current bandwidth subscription, and current rate charged (see Fig. 4 for a summary of all functional expenditures), the user then selects the model parameters to match the preferred pricing strategies and to allocate these functional expenditures to individual clients. Section 5.1 displays a scenario in which changes in bandwidth scaling factors or group weighting factors have a great impact on the proposed rate card options.

Monthly Cost-Allocation Model  
![](/api/attachments/E587KNW2/fulltext/images/fc8bde0f18a717445d1a8b7fd8a2f5e9c5018f3e76b743b13892a1af0577be91.jpg)  
Fig. 4. The summary of all functional expenditures.

## 5.1. Changes in bandwidth scaling factors and group weighting factors

The bandwidth scaling factors and group weighting factors are the most important parameters in allocating all functional expenditures in this study (see Section 4.3.1 for greater detail on how to allocate these functional expenditures to individual clients). According to Eq. (4) in Section 4.3.1, the group weighting factors are used in the allocation of administrative costs, equipment costs, channelized costs, and V-lan costs, while the bandwidth scaling factors are used in the allocation of operations costs, <sup>fi</sup>xed costs, hub costs, and network costs. To illustrate the in<sup>fl</sup>uence of the changes in these factors, this section focuses on the allocation of administrative costs.

OneNet was established mainly to provide services to research and academic institutions, while non-academic clients receive a secondary bene<sup>fi</sup>t by having access to network services at a lower cost. With this assumption, these research and academic groups (groups 1 and 2) are responsible for higher networks and operations costs than the nonacademic groups (groups 3, 4, and 5). In this study, the weighting factors for groups 1–5 are then set as 2, 2, 0.5, 0.5, 0.5 respectively (see Fig. 5). The changes in these group weighting factors re<sup>fl</sup>ect the allocation of administrative costs for each client. The total administrative costs allocated to all clients in groups 1–5 are \$14,641, \$71,810, \$2580, \$15,443, and \$12,863, respectively. The total of the allocated administrative costs remains the same at \$117,336 (see Figs. 4 and 5 for the total administrative costs). The same procedure used for group weighting factors is applied to the bandwidth scaling factors. The total costs associated with the changes in these bandwidth scaling factors are redistributed to all clients accordingly.

## 5.2. Baseline revenue analysis

Once the model parameters in Section 5.1 are adjusted properly, the SNAP-DSS automatically produces ten rate card options. The users then evaluate which rate cards options are reasonable and feasible for

![](/api/attachments/E587KNW2/fulltext/images/e9bd1ca88dc124f31268b611aaebce36712276635332a67e543b4877906ce670.jpg)  
Monthly Cost Allocation

<table><tr><td></td><td>LAST MILE</td><td>Admin.C</td><td>Oper.C</td><td>Equip.C</td><td>Channalized</td><td>V-Lan</td><td>Fixed C</td><td>Hub Cost</td><td>Network C</td><td>Total</td></tr><tr><td>Group1</td><td>$31,797</td><td>$14,641</td><td>$4,570</td><td>$162</td><td>$1,410</td><td>$1,695</td><td>$12,542</td><td>$1,668</td><td>$35,430</td><td>$103,915</td></tr><tr><td>Group2</td><td>$178,830</td><td>$71,810</td><td>$5,392</td><td>$796</td><td>$17,921</td><td>$865</td><td>$428</td><td>$8,228</td><td>$41,799</td><td>$326,070</td></tr><tr><td>Group3</td><td>$18,821</td><td>$2,580</td><td>$722</td><td>$29</td><td>$668</td><td>$17</td><td>$268</td><td>$1,010</td><td>$5,597</td><td>$29,712</td></tr><tr><td>Group4</td><td>$223,329</td><td>$15,443</td><td>$6,097</td><td>$171</td><td>$3,636</td><td>$147</td><td>$5,760</td><td>$7,005</td><td>$47,266</td><td>$308,854</td></tr><tr><td>Group5</td><td>$94,176</td><td>$12,863</td><td>$4,530</td><td>$143</td><td>$3,033</td><td>$251</td><td>$3,373</td><td>$5,600</td><td>$35,118</td><td>$159,087</td></tr><tr><td></td><td>$546,953</td><td>$117,336</td><td>$21,312</td><td>$1,300</td><td>$26,669</td><td>$2,975</td><td>$22,372</td><td>$23,511</td><td>$165,210</td><td>$927,638</td></tr></table>

Fig. 5. Model parameters analysis: the adjusted group weighting factors.

OneNet to implement by looking at the baseline revenue comparison among those rate card options on an individual case basis. Fig. 6 presents the baseline revenue scenario analysis when the group weighting factors and bandwidth scaling factors are set as in Fig. 5. The proposed ten rate card options are ranked from 1 to 10, respectively; the last column of the baseline revenue analysis worksheet represents the current rates OneNet charges its clients for the services.

According to these ten rate card options, it seems that OneNet is overcharging clients 30 and 31. The maximum rate charged for T-1 bandwidth from these proposed rate card options is \$1064 (Client 31, rate card option 2) while the current rate actually charged is \$1100. In contrast, OneNet is undercharging client 37, who subscribes to OC-3 bandwidth, as the maximum rate charged for the OC-3 bandwidth from these proposed rate card options is \$10,420, while the current rate actually charged is \$5000. The problem of undercharging or overcharging can be solved when the model parameters are adjusted appropriately. OneNet can readjust the bandwidth scaling factors to decrease the gap between the rates charged to clients subscribing to higher bandwidths and those subscribing to lower bandwidths. Additionally, in the case of an unreasonable rate issue among clients in the same group subscribing to the same bandwidth, OneNet can adjust the group weighting factors to overcome this issue.

## 5.3. Cost–revenue analysis

The baseline revenue scenario analysis in Section 5.2 can help OneNet determine whether the proposed rate card options are reasonable and are fair across its clients. The cost-revenue scenario analysis in this section provides an overview of OneNet's net surplus and helps OneNet determine the rate card option that is suitable for OneNet's pricing strategies.

As mentioned in Section 4.3.1, the proposed rate card options are derived from the concept of zero pro<sup>fi</sup>t, meaning that the rates charged to each client are equal to the functional expenditures allocated to each client. However, if OneNet needs to reserve a certain amount of budget for the next <sup>fi</sup>scal year for new technology investments and upgrades, the revenues generated from these proposed rate card options will not be adequate. Thus, this SNAP-DSS offers the users the ability to adjust another set of model parameters (see Section 4.2) that in<sup>fl</sup>uence the proposed rate card options and overall revenues: (1) overall percent pro<sup>fi</sup>t, (2) multipleyear discount, (3) percent discount, (4) percent early disconnection, and (5) estimated disconnection fees. The in<sup>fl</sup>uence of the changes in these model parameters on the overall revenue is analyzed below.

The total monthly revenues generated from the ten proposed rate card options are presented in Appendix C. The estimated monthly network and operations costs are \$1,445,647. Without adjusting any model parameters, the monthly revenues generated from the rate card options 1, 7, and 8 are \$1,447,044 with the highest overall pro<sup>fi</sup>t of \$1397. Rate card option 2 seems to be the most reasonable option as the overall pro<sup>fi</sup>t (\$2) is close to zero. The overall pro<sup>fi</sup>ts from other rate card options range from \$50 to \$850.

When the “overall percent pro<sup>fi</sup>t” is set at 5% and OneNet offers its clients a one year contract option with a 5% discount rate and a 5% (or \$5000) penalty charge for early disconnection, for instance, the overall functional expenditures are then redistributed to all clients accordingly. The proposed ten rate card options are recalculated. Without considering the revenue from clients who are penalized for early disconnection, rate card options 1, 7, and 8 seem to be the most reasonable, as the revenues generated from these options are \$1,447,416 with the highest pro<sup>fi</sup>t of \$1769. Meanwhile, the overall pro<sup>fi</sup>ts from the other rate card options are negative, ranging from − \$1474 to −\$3612. When the amount gathered from the early disconnection fees is considered, all rate card options will provide a positive overall pro<sup>fi</sup>t, depending on the number of penalized clients.

## 6. Use of SNAP-DSS at OneNet

As illustrated in Section 5, the SNAP-DSS enables OneNet to evaluate different pricing structure in different scenarios. In this section, we emphasize how OneNet actually uses this SNAP-DSS in practice (see Fig. 7). After entering all relevant data into the system, adjusting appropriated model parameters, and analyzing all rate card options including cost–revenue analysis, OneNet can determine its pricing model choice based on three-factor evaluation model: Data availability, Social impact, and Political acceptance.

– Data availability concerns the data needed to implement a pricing model. Speci<sup>fi</sup>cally, OneNet has to answer the following question “Is it possible for OneNet to compile all the information needed for implementing a particular pricing model?”

– Social impact concerns the fairness among members. Does a model distribute the cost fairly across the members based on resource usages, size of the organization, or quality of services, etc.?

<table><tr><td colspan="13">OneNet: Oklahoma&#x27;s Telecommunications Network</td></tr><tr><td colspan="6"></td><td>Individual-Based Pricing</td><td>Group-Based Pricing</td><td colspan="3">Cost-Revenue Analysis</td><td colspan="2">Home</td></tr><tr><td colspan="6">Comparison Between Current Rate and Proposed Rate Card Options</td><td colspan="7">Oklahoma State University</td></tr><tr><td colspan="2">Pricing Options Summary</td><td rowspan="2">(1) Individual Cost-Based Rate</td><td rowspan="2">(2) Linear Regression-Based Rate</td><td rowspan="2">(3) Non-Linear Regression-Based Rate</td><td rowspan="2">(4) Twelve-Tier BW-Based Rate</td><td rowspan="2">(5) Twelve-Tier BW with Group-Based Rate</td><td rowspan="2">(6) Group-FTE and BW-Based Rate</td><td rowspan="2">(7) Individual Usage-Based Rate (1)</td><td rowspan="2">(8) Individual Usage-Based Rate (2)</td><td rowspan="2">(9) Six-Tier Guarantee BW-Based Rate</td><td rowspan="2">(10) The Average Rate from Nine Rate Options</td><td rowspan="2">Current Rate Actually Charged</td></tr><tr><td>Site Name</td><td>Bandwidth</td></tr><tr><td>Client 30</td><td>T1</td><td>$465</td><td>$426</td><td>$642</td><td>$672</td><td>$540</td><td>$536</td><td>$450</td><td>$465</td><td>$685</td><td>$542</td><td>$1,100</td></tr><tr><td>Client 31</td><td>T1</td><td>$895</td><td>$1,064</td><td>$642</td><td>$672</td><td>$897</td><td>$586</td><td>$895</td><td>$895</td><td>$685</td><td>$803</td><td>$1,100</td></tr><tr><td>Client 32</td><td>Fast Ethernet</td><td>$2,345</td><td>$506</td><td>$3,900</td><td>$2,658</td><td>$2,453</td><td>$2,530</td><td>$2,345</td><td>$2,345</td><td>$2,590</td><td>$2,408</td><td>$2,300</td></tr><tr><td>Client 33</td><td>56K</td><td>$334</td><td>$871</td><td>$145</td><td>$279</td><td>$333</td><td>$317</td><td>$367</td><td>$367</td><td>$282</td><td>$366</td><td>$350</td></tr><tr><td>Client 34</td><td>DS3</td><td>$1,785</td><td>$986</td><td>$2,768</td><td>$2,310</td><td>$2,516</td><td>$2,056</td><td>$1,785</td><td>$1,785</td><td>$2,590</td><td>$2,065</td><td>$3,510</td></tr><tr><td>Client 35</td><td>Ethernet</td><td>$1,073</td><td>$896</td><td>$1,458</td><td>$1,193</td><td>$1,121</td><td>$1,221</td><td>$1,073</td><td>$1,073</td><td>$685</td><td>$1,088</td><td>$2,033</td></tr><tr><td>Client 36</td><td>OC-3</td><td>$3,746</td><td>$2,737</td><td>$4,700</td><td>$8,422</td><td>$4,689</td><td>$7,688</td><td>$3,746</td><td>$3,746</td><td>$8,422</td><td>$5,322</td><td>$5,000</td></tr><tr><td>Client 37</td><td>OC-3</td><td>$10,420</td><td>$9,090</td><td>$4,682</td><td>$8,340</td><td>$4,565</td><td>$7,688</td><td>$10,420</td><td>$10,420</td><td>$8,422</td><td>$8,122</td><td>$5,000</td></tr></table>

Fig. 6. Baseline revenue analysis.

![](/api/attachments/E587KNW2/fulltext/images/da49f0561a8d6829427a18990fe3d88396d8d3b40ee5d23b6c3141678bf72b4a.jpg)  
Fig. 7. A typical use of SNAP-DSS.

– Political acceptance concerns the organizational structure, mission and goals, or particularly funding sources. Will the members accept a particular pricing model as being fair and equitable? Can the model be justi<sup>fi</sup>ed, If a new model is proposed, those whose costs are lowered will not mind but what about those who will pay more?

Accordingly, twelve-tier bandwidth-based rate (rate card option 4), which is adapted from OneNet's current pricing structure seems to be the right pricing model choice for several reasons. First, this recommended rate leads to the minimal changes in its infrastructure, current database system, and billing system. Second, the problem of undercharging and overcharging its clients is minimized. In this case, total 1321 clients who mostly subscribe to T1 and DS3 bandwidth end up paying about 2% and 20% less, respectively. However, inevitably, a total of 196 clients subscribing to the 56K, Ethernet, Fast Ethernet, Gigabit Ethernet, and 10 Gigabit Ethernet have to pay about 4%, 36%, 74%, 20%, and 75% more, respectively. Additionally, when compared to its direct competitor such as AT&T and other state network organizations that are similar to OneNet, our analysis shows that the 56K and T1 rates are about less than 2% apart. The major discrepancies, however, are on the higher bandwidth services. OneNet can offer cheaper services, especially the Gigabit and 10 Gigabit Ethernet as OneNet utilizes Indefeasible Right of Use agreements (IRUs) to lease dark <sup>fi</sup>ber from the State of Oklahoma free of charge. The term “IRU” means a right to use <sup>fi</sup>ber, cable, or channels of a given bandwidth for a certain period of time. With this support from the government, OneNet can cut down its operations cost and provide services at rational rates.

Other rate card options seem to be unreasonable at this point. For instance, even though the individual cost-based pricing (options 1–3) and usage-based pricing (options 6 and 7) re<sup>fl</sup>ect actual cost allocation and provide more accurate rates to charge its clients for what they actually consume, charging its clients on an individual case basis is politically undesirable as any changes in rates must be reported to and approved by the State Regent of Oklahoma. Furthermore, they require signi<sup>fi</sup>cant changes in data gathering and monitoring of the actual bandwidth usage, database, and billing systems.

In summary, after the pricing model choice has been made, OneNet can evaluate each client's speci<sup>fi</sup>c pricing as individual case basis. Consequently, in addition to selecting the right pricing model choice for speci<sup>fi</sup>c client billing, OneNet can defend its rate decisions on a political basis.

## 7. System evaluation and feedback

The development of the SNAP-DSS started with the analysis of OneNet's overall business plan, organizational structure, and current pricing structure. Then the pricing strategies and rate card options from many state network organizations along with the pricing schemes from the literature were used as the best practices in improving this SNAP-DSS. The <sup>fi</sup>rst version of the SNAP-DSS was assessed by specialists in the organization. OneNet of<sup>fi</sup>cials were excited about the DSS and asked it to be presented at their trade meetings to share the success with the peers in other states so the model was presented at the Annual StateNets Financial Focus Group Meeting, Tempe, AZ. After receiving feedback with regard to each rate card option, the second version of the SNAP-DSS has been developed and implemented on an actual project in order to evaluate its feasibility and effectiveness. The second version of the SNAP-DSS was continuously evaluated by OneNet's specialists and was presented at the Quilt, the Annual Financial Focus Group Meeting, Newport, RI. Below are examples of feedback from specialists in the organization as the users of the system.

“The Oklahoma State Regents' of<sup>fi</sup>ce has been extremely pleased with the work done …related to a distinct pricing and cost allocation model for OneNet, Oklahoma's of<sup>fi</sup>cial telecommunications network for education and government. Speci<sup>fi</sup>cally, Dr. Sharda's current model affords the State Regents the ability to apply various cost allocation and recovery methodologies within a single architecture. This is invaluable with respect to accommodating potential changes in state policy and appropriations and assures the model is not rendered useless should changes of this nature occur.”

Kurt Snodgrass, Vice Chancellor for IT & Telecommunications, OneNet

“SNAP: DSS is a real time business management tool that determines immediate budget impact as a result of adding a single client. The DSS spreadsheet provides multiple rate cards which are derived by calculations utilizing nine business models currently used by eighteen state network organizations. These rate cards are presented in numerical and graphical formats and each one is calculated simultaneously with the change or addition of a single client. The bene<sup>fi</sup>ts of incorporating the Decision Support System include; the ability to have consistent and reliable information that can be used to justify OneNet rate structure to management and clients.”

Ken Ferguson, Director of Administration, OneNet

Additionally, the model has also been shared with other states such as North Carolina to let them customize it for their applications.

Although we also wanted to develop some quanti<sup>fi</sup>able measures of the utility of this DSS, that is not practical because the DSS is being used by only a small group of users. By the nature of the application, only the CFO, <sup>fi</sup>nance director, and technical marketing directors are involved in making the pricing decision and the use of SNAP-DSS. It is not uncommon for a DSS to have just a few users and to be successful. DSS aimed at top management are likely to fall in this category. A recent study from McGill and Klobas [14], however, indicates that the successful use of spreadsheet applications is based on suf<sup>fi</sup>cient spreadsheet knowledge of both the developer and user. Thus, the problem of successfully utilizing the SNAP-DSS and the quality of its application can be partially balanced by the knowledge of the application and contents of these users. Two similar spreadsheetbased decision support systems from Buehlmann et al. [2] and De Reyck and Degraeve [5] are developed to support decisions making in manufacturing and marketing areas, respectively. These systems including the quality of the outputs, its relevance solution, and the ease of use were also assessed by specialists and top managements in the company. Thus, evaluation of this DSS through interviews with the <sup>fi</sup>nancial and IT experts is the only feasible method at this point.

## 8. DSS—Lessons learned and conclusions

This is the <sup>fi</sup>rst DSS where many different pricing models have been incorporated in one place. This is based on the concept of data and information fusion aiming at combined information originating from different data sources for greater quality, higher accuracy, and robustness [11]. There is also a unique design for DSS that has been proposed here that allows a decision maker to start with the goal of <sup>fi</sup>nding a pricing level that achieves their objectives, then perform an analysis at the macro level (cost–revenue analysis) to see if the total costs are being covered and, and also a micro level analysis to analyze how various customers would be treated fairly under a speci<sup>fi</sup>c pricing model. This helps with the social equity analysis.

Developing an interface that permits data entry, rate card option generation, and macro–micro analysis requires some design decisions that should be of interest to other researches. The domain speci<sup>fi</sup>c application of a common tool such as a spreadsheet is unique as well.

Thus, the main contribution of this paper is addressing the decision support mechanism that allows users to practically develop and justify their pricing decisions with multiple rate card options, which are based on the cost-based pricing and best-effort pricing structure. The users can then determine their pricing model choice based on the proposed three-factor evaluation model: data availability, social impact, and political acceptance.

For the SNAP-DSS development, we started with the selection of software packages that can provide a versatile, user-friendly, Graphical User Interfaces (GUIs) that most users are comfortable with.

We began to develop the SNAP-DSS on a modeling and visualization application, Planners Lab (PL), developed by GRW studios, Inc. [20]. PL is primarily developed for modeling various <sup>fi</sup>nancial situations with an analysis of what-if and goal-seek questions. PL offers the DSS developer the features to build and simulate the model using linear algebraic equations with drag and drop visualization. Additionally, the equations designed by the DSS developer are in the English language, for example “Total Network Related Expenditures=Maintenance and Operations+Internet Circuits.” Thus, instead of de<sup>fi</sup>nitions of cell references in an Excel spreadsheet, formulas written in English are easy and understandable. We received positive feedback after introducing this PL implementation to the users, especially for the graphic representation, user interface, and the error identi<sup>fi</sup>cation. Unfortunately, developing the SNAP-DSS on PL created two major problems. First, when too many variables or conditions are involved in the model, changing or inserting variables in PL is dif<sup>fi</sup>cult for the developer due to the complexity in writing the equation. Second, PL cannot handle massive amounts of data as it is not designed to include a Database Management component. For instance, when OneNet has roughly 1500 clients subscribing to the services, all related information can be at least 1500 lines of equations in PL. The issue of organizing massive data sets can be resolved by using Microsoft Excel. As a result, we moved to Microsoft Excel 2007 as a second version of the SNAP-DSS.

Compared to Excel 2003, Excel 2007 offers a powerful and effective tool in managing and analyzing data and especially supports dual or multi-core processor platforms to speed up the calculation performance. With the new results-oriented user interface in Excel 2007, the user can even write complex formulas. Thus we realized that when a DSS application involves a signi<sup>fi</sup>cant database component, a spreadsheet might work better than a more user-friendly DSS development tool such as Planners Lab.

This project is an actual application of DSS concepts to a practical problem faced by many network operators. Although many other sophisticated methods of pricing network services have been proposed in the literature, the users favor simplicity over complex

Appendix A. Data input worksheet on various types of expenditures  
![](/api/attachments/E587KNW2/fulltext/images/39500102162468791c4bc5441319d016b1870d2037334a9e5d653fda53b58f7a.jpg)

Appendix B. Data input worksheet on Last Mile for individual clients  
![](/api/attachments/E587KNW2/fulltext/images/0e86b85d35f91ecaa1996992db13773d7bc1b3d5c53cae9708975f6113c40c08.jpg)

<table><tr><td colspan="4">Total cost paid to Telco providers</td></tr><tr><td>Telco1</td><td>Telco2</td><td>Telco3</td><td>Total</td></tr><tr><td>$523,852</td><td>$22,953</td><td>$148</td><td>$546,907</td></tr></table>

<table><tr><td>No.</td><td>Site Name</td><td>Department Name</td><td>Circuit Speed</td><td>Telco1</td><td>Telco1 ($)</td><td>Telco2</td><td>Telco2 ($)</td><td>Telco3</td><td>Telco</td></tr><tr><td>1</td><td>Client 1</td><td>Affiliates</td><td>T1</td><td>Southwestern Bell Telephone Company</td><td>$160</td><td></td><td>$0</td><td></td><td></td></tr><tr><td>2</td><td>Client 2</td><td>Affiliates</td><td>T1</td><td>Southwestern Bell Telephone Company</td><td>$84</td><td></td><td>$0</td><td></td><td></td></tr><tr><td>3</td><td>Client 3</td><td>Affiliates</td><td>T1</td><td>Southwestern Bell Telephone Company</td><td>$238</td><td></td><td>$0</td><td></td><td></td></tr><tr><td>4</td><td>Client 4</td><td>Army National Guard</td><td>Fast Ethernet</td><td>OneNet</td><td>$0</td><td></td><td>$0</td><td></td><td></td></tr><tr><td>5</td><td>Client 5</td><td>Army National Guard</td><td>T1</td><td>Southwestern Bell Telephone Company</td><td>$368</td><td></td><td>$0</td><td></td><td></td></tr><tr><td>6</td><td>Client 6</td><td>Army National Guard</td><td>T1</td><td>AT&amp;T</td><td>$84</td><td></td><td>$0</td><td></td><td></td></tr><tr><td>7</td><td>Client 7</td><td>Army National Guard</td><td>T1</td><td>AT&amp;T</td><td>$84</td><td></td><td>$0</td><td></td><td></td></tr><tr><td>8</td><td>Client 8</td><td>Army National Guard</td><td>T1</td><td>Southwestern Bell Telephone Company</td><td>$84</td><td></td><td>$0</td><td></td><td></td></tr><tr><td>9</td><td>Client 9</td><td>Army National Guard</td><td>T1</td><td>Southwestern Bell Telephone Company</td><td>$110</td><td></td><td>$0</td><td></td><td></td></tr></table>

Appendix C. Baseline cost–revenue analysis  
![](/api/attachments/E587KNW2/fulltext/images/1817e60f8db581ac16290aaa8a34737199c77bcd7c04fc27c26dc6d0222ee106.jpg)

<table><tr><td>Cost-Revenue Analysis</td><td colspan="3">Baseline Analysis (Monthly)</td></tr><tr><td>Rate Card Options</td><td>Revenue ($)</td><td>Cost ($)</td><td>Profit ($)</td></tr><tr><td>1. Cost-Based Pricing (Individual)</td><td>$1,447,044</td><td>$1,445,647</td><td>$1,397</td></tr><tr><td>2. Linear Regression Analysis</td><td>$1,445,649</td><td>$1,445,647</td><td>$2</td></tr><tr><td>3. Non-Linear Regression Analysis (3)</td><td>$1,445,697</td><td>$1,445,647</td><td>$50</td></tr><tr><td>4. Cost-Based Pricing (13 Tier BW)</td><td>$1,446,258</td><td>$1,445,647</td><td>$611</td></tr><tr><td>5. Cost-Based Pricing (13 Tier - Group)</td><td>$1,446,401</td><td>$1,445,647</td><td>$754</td></tr><tr><td>6. Cost-Based Pricing (FTE)</td><td>$1,446,501</td><td>$1,445,647</td><td>$854</td></tr><tr><td>7. Usage-Based Pricing (1)</td><td>$1,447,044</td><td>$1,445,647</td><td>$1,397</td></tr><tr><td>8. Usage-Based Pricing (2)</td><td>$1,447,044</td><td>$1,445,647</td><td>$1,397</td></tr><tr><td>9. Cost-Based Pricing 6-Tier BW</td><td>$1,446,495</td><td>$1,445,647</td><td>$848</td></tr><tr><td>10. Average Pricing from all Options</td><td>$1,446,459</td><td>$1,445,647</td><td>$812</td></tr></table>

modeling. Copies of the DSS have already been requested by other states to customize it for their own applications.

## References

[1] C. Bouras, A. Sevasti, Service level agreements for DiffServ-based services provisioning, Journal of Network and Computer Applications 28 (4) (2005) 285–302.

[2] U. Buehlmann, R. Ragsdale, B. Gfeller, A spreadsheet-based decision support system for wood panel manufacturing, Decision Support Systems 29 (3) (2000) 207.

[3] I Chongwatpol R. Sharda Pricing Telecommunications Network Services in Practice: A Case Study of State Network Organizations Working Paper Oklahoma State University, Institute for Research in Information System (IRIS), Spears School of Business, Stillwater, 2008.

[4] C. Courcoubetis, R. Weber, Pricing Communication Networks: Economics, Technology and Modelling John Wiley & Sons Inc, Hoboken, NI 2003

[5] B. De Reyck, Z. Degraeve, MABS: spreadsheet-based decision support for precision marketing, European Journal of Operational Research 171 (3) (2006) 935.

[6] G. Fankhauser, B. Stiller, V. Christoph, B. Plattner, Reservation-based Charging in an Integrated Services Network, 4th INFORMS Telecommunications Conference. Boca Raton, FL. 1998

[7] C.W. Holsapple, A.B. Whinston, Decision Support Systems: A Knowledge-based Approach West Publishing, St. Paul MN 1996

[8] M. Karsten, J. Schmitt, L. Wolf, R. Steinmetz, An Embedded Charging Approach for RSVP. Proc, Ouality of Service. 1998. (IWOoS 98) 1998 Sixth International Workshop on, 1998, pp. 91–100.

[9] N.J. Keon, G.A. Anandalingam, A new pricing model for competitive telecommunications services using congestion discounts, INFORMS Journal on Computing 17 (2) (2005) 248.

[10] N.J. Keon, G.A. Anandalingam, Optimal pricing for multiple services in telecommunications networks offering quality-of-service guarantees, IEEE/ACM Transactions on Networking 11 (1) (2003) 66–80.

[11] W. Lucien, Some terms of reference in data fusion, IEEE Transactions on Geoscience and Remote Sensing 37 (3) (1999) 1190–1193.

[12] J. K. MacKie-Mason and H. R. Varian, “Pricing the Internet,” Public Access to the Internet, JFK School of Government, 1993.

[13] J.K. MacKie-Mason, H.R. Varian, Some FAQs about usage-based pricing, Computer Networks and ISDN Systems 28 (1–2) (1995) 257–265.

[14] T.J. McGill, J.E. Klobas, The role of spreadsheet knowledge in user-developed application success, Decision Support Systems 39 (2005) 355

[15] B.M. Mitchell, I. Vogelsang, Telecommunications Pricing: Theory and Practice, The Press Syndicate of the University of Cambridge, New York, NY, 1991.

[16] T.T.T. Nguyen, G.J. Armitage, Evaluating Internet pricing schemes: a threedimensional visual model, ETRI Journal 27 (2005) 64–74.

[17] A. Odlyzko, Paris metro pricing for the Internet, Proceedings of the 1st ACM conference on Electronic commerce ACM, Denver, Colorado, 1999, pp. 140–147.

[18] S. Shin, R.I.F. Cope, R.F. Cope, J. Tucci, E., Internet pricing: best effort versus quality of service, Academy of Information and Management Sciences Journal 9 (2) (2006) 1.

[19] E. Turban, E.J. Aronson, T.P. Liang, R. Sharda, Decision Support and Business Intelligence Systems, Eighth edPearson Education, Inc, Upper Saddle River, New Jersey, 2007.

[20] J. Wagner, “Planners Lab software,” July 20, 2008, bhttp://www.plannerslab.com site/plannerslab.php?site=teradata&section=overviewN.

![](/api/attachments/E587KNW2/fulltext/images/cbc3f927ad00fdaf1d716929682b2504c5ab1d697741e1ce6ea2d0913f41687d.jpg)

Jongsawas Chongwatpol is a Ph. D. student in Manage ment Science and Information Systems in the Spears School of Business at Oklahoma State University. He received his B.E. in Industrial Engineering from Thammasat University, Bangkok, Thailand and M.S. in Risk Control Management, and M.S. in Management Technology from University of Wisconsin-Stout. His major research interests include decision support systems, RFID, manufacturing management, and supply chain management.

![](/api/attachments/E587KNW2/fulltext/images/33ac03030a7b020e9239b6a84e2af906955e9e9fd47f4e991b00b3e17bb46343.jpg)

Ramesh Sharda is Director of the Institute for Research in Information Systems (IRIS), ConocoPhillips Chair of Management of Technology, and a Regents Professor of Management Science and Information Systems in the Spears School of Business at Oklahoma State University. He received his B. Eng. degree from University of Udaipur, M.S. from The Ohio State University and an MBA and Ph. D. from the University of Wisconsin-Madison. His research has been published in major journals in management science and information systems including Management Science, Information Systems Research, Decision Support Systems, Interfaces, INFORMS Journal on Computing, Computers and Operations Research, and many others. He serves on the editorial boards of journals such as the

INFORMS Journal on Computing, Decision Support Systems, Information Systems Frontiers, and OR/MS Today. His research interests are in decision support systems, especially neural network applications, and technologies for managing information overload. His team's work on forecasting box of<sup>fi</sup>ce revenue of movies has received a lot of press. Defense Ammunitions Center, NSF, the US Department of Education, Marketing Science Institute, and other organizations have funded his research. Ramesh is also a cofounder of a company that produces virtual trade fairs, iTradeFair.com.
