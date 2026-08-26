---
otero_id: 27041
otero_key: "KUNT9CR5"
title: "Mapping Chargeback Systems to Organizational Environments"
authors: "William P. McKinnon; Ernest A. Kailman"
year: "1987"
journal: "MIS Quarterly"
doi: "10.2307/248820"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Mapping Chargeback Systems to Organizational Environments
Author(s): William P. McKinnon and Ernest A. Kallman
Source: MIS Quarterly, Vol. 11, No. 1 (Mar., 1987), pp. 5-20
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248820
Accessed: 10-01-2016 03:33 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Mapping Chargeback Systems to Organizational Environments

By: William P. McKinnon, Supervisor Administration & Planning, I.S.S. Public Service of New Hampshire Manchester, New Hampshire

By: Ernest A. Kallman, Ph.D.
Professor Computer Information Systems
Bentley College
Waltham, Massachusetts

## Abstract

A critical problem facing information systems management is what kind of chargeback system to install and will it be appropriate in the future? The solution is to map the chargeback system to the organizational environment. This organizational environment can be described by: 1) the use to which the information technology is put, 2) the maturity of the information systems function, and 3) the level of development of the information systems managerial function. The authors have developed a model that defines the organizational environments according to these three dimensions, giving management an organizational definition by which to choose the chargeback system that best accommodates the organization's accountability needs. This paper describes characteristics of chargeback systems, major chargeback methods and the authors' model. Then the impact of the model and the extent of its implementation are displayed through two case analyses.

Keywords: Chargeback systems, chargeout systems, installation management, pricing, resource allocation

ACM Category: K.6.2

## Introduction

Although three recent empirical studies have examined chargeback effectiveness and the role of the user $[1, 2, 9]$ , much of what has been written on chargeback systems has concentrated on their benefits and weaknesses or their structure. However this article is concerned with choosing the chargeback method which provides the kind of information and control most useful to the organization at each stage of its existence. The intent of the paper is not to define proper management practices, but rather to show that, as Nolan $[7]$ contends, chargeback systems bring management into control of computer resources and fulfill more than the narrow function of simply allocating computer costs.

## Characteristics of Chargeback Systems

Chargeback systems are generally used for two major processes: 1) measurement of the resources consumed by users, and 2) determination of a dollar value for that quantity. More simply, a chargeback system is an accounting process to monitor resources and a pricing process to interface with users.

## The accounting process

A complete chargeback accounting system should do the following:

1) Record usage at a level of detail that identifies all resources consumed. This includes resources consumed by support software as well as other application overhead software.

2) Identify the individual performing the work as well as the department receiving benefit, if they differ, such as a centralized accounting staff producing district or branch reports for distribution.

3) Summarize usage based on classifications that impart the greatest amount of information. The focus need not be only on dollars expended, but also the type of resource consumed and the level of service provided.

4) Report the summarized usage at regular intervals to identify significant trends and characteristics.

While performing these specific functions, accounting systems should also demonstrate, over the course of several accounting periods, consistency in job charging, equity in cost distribution, and simplicity of approach from the user's viewpoint.

Accounting systems provide a secondary benefit to MIS management in that they measure base data for capacity planning. Hardware, software and network usage trends, peak periods of processing, application growth areas, required service levels, equipment bottlenecks, and recurring problems are examples of what can be derived from the same base data that needs to be collected to identify end user consumption of resources. Accurate capacity planning increases the effectiveness and benefit of charge-back systems by providing management with the ability to identify specific resources which should be used or supported differently. Although recent developments have allowed users to acquire small increments of capacity at reasonable rates (such as PCs and minis), in the shared mainframe environment three cost characteristics that mainframe computer systems have historically demonstrated must be taken into account [4].

1) Capacity is acquired in large blocks which cannot smoothly accommodate linear growth in demand.

2) There are significant economies of scale. When operated at capacity, the per unit job cost to the user is lower on larger systems.

3) The cost of incremental work up to full capacity is very low. However, as full capacity is approached, determining which new demand should replace existing demand is costly and difficult.

Equipped with a knowledge of what resources are nearing capacity and the cost characteristics to upgrade them, along with an understanding of which user areas are consuming the resources, management has the ability to set priorities. Once priorities have been set, two different but interrelated courses of action are possible. The first is to increase the computing resources targeted for high priorities and the second is to modify user resource consumption behavior.

## The pricing process

Management can modify user behavior and resource consumption, without playing a centralized/directive role, by adjusting pricing through the chargeback system. User behavior based on targeted pricing can extend intervals between upgrades, reduce levels of non-priority processing during peak demand periods, and encourage adoption of more efficient products.

A fundamental analysis of computing costs must be made to provide a basis for selecting a pricing strategy that identifies target priorities and defines desired user resource consumption behavior. Howard [3] suggests that each data processing resource category or "load center" be individually costed and charged out in order to allow user management to associate charges with the value of services delivered through those load centers. For example, the cost of storing data on tape versus disk, or the differences in putting output data to paper versus microfiche, should be discernable to the user. The costs within each load center should be classified as direct (such as hardware, software, materials and some labor), or indirect (such as overhead and shared expenses). The purpose of identifying costs as direct and indirect is to allow users to understand what costs they can control as opposed to those costs that are allocated or assigned.

Olson and Ives [9] refer to the pricing process as the “user interface” of a chargeback system and agree with Nolan [7] that its effectiveness can be measured on four criteria:

1) the degree to which users understand the charges,

2) the amount of control or influence users have over their use of computing resources,

3) the degree to which the user receives the chargeout bill (billing incidence), and

4) the degree to which users are held accountable by their own managers for costs incurred by using information services.

Synnott and Gruber [10] elaborate on the need for stating prices in units that are more understandable to users rather than traditional units such as CPU hours, tape and disk I/O's, lines printed and terminal connect hours. They suggest costs be expressed in user transactions such as cost per check, cost per item of inventory processed, cost per report printed. Developing costs based on transactions allows users to better budget computer expenses and to associate the value and cost of information. There is a hidden benefit to MIS management from this transaction-based costing. User estimates of future MIS support and resources will be more accurate and will result in more reliable future capacity planning. For example, users can more easily describe new product lines in terms of target sales projections, test market locations, employees required, budgeted expenses, materials required, competition expected and manufacturing locations, than they can estimate the additional direct access storage needed in branch offices, or the impact of CICS transaction times as additional sales offices are opened.

The last function of the pricing process is transferring the actual resource costs once they have been properly measured and meaningfully expressed. Though chargeback systems can be developed to recover costs or to generate profits the focus in this article is on cost-oriented chargeback systems. The next section discusses the four types of cost-based chargeback systems.

## Types of Chargeback Systems

Lin [5] distinguishes between chargeback systems based on the type of budgetary practice used within the company: allocation chargebacks use the soft-money concept in which costs are only stated in memo form; direct chargeback systems use the hard-money concept to transfer costs through the general ledger.

## Allocation chargeback

Lin [5] explains allocation chargeback as directed at upper level managers in memo form, summarizing past MIS expenses. They are categorized as uncontrollable expenses from the perspective of the operating budget and are treated as overhead, being assigned or allocated from MIS to major user groups. Allocation chargeback provides the lowest level of user accountability/control as costs are not budgeted by or transferred to user departments. This type of chargeback requires the least amount of user involvement/input to the planning process. Primarily, allocation chargeback serves to educate both corporate and MIS management by detailing the types and costs of resources consumed by major user areas.

## Direct chargeback

Lin discribes three types of direct chargeback systems: 1) average cost, 2) standard cost, and 3) resource allocation which we prefer to call flexible pricing. Under any one of these direct chargebacks, users have put computer costs in their operating budgets on the same basis as other major controllable expenses, such as salaries and supplies. This process requires a chargeback system that reports costs in such a way that the user can associate the value of the activity and its information with the cost to achieve it.

## Average cost method

Average cost chargeback is based on incurred costs and actual usage from the preceding chargeback period, or a weighted moving average of several prior periods. The focus is on past processing and usage. Total costs are divided by recorded usage within each load center and assigned by percentages to end users. This method is easy to implement, recovers all MIS costs, and is easily explained and audited. However, charges for the same amount of resource consumption may vary from period to period depending on total system activity. A job may cost more one month, simply because total usage was lower, while costs were essentially fixed. Users are unable to accurately budget and have a reduced level of accountability and control. From the MIS perspective, this chargeback method does not address or help to manage periodic workloads because there is no price differential with respect to the time the resources are used. Longer term demands are also hard to control as prices, rather than need, can influence demand. High prices decrease usage which, in turn, drives up the per unit cost of usage. Similarly, low per unit prices caused by high usage levels increase resource consumption, creating higher peak loads $[5]$ .

## Standard cost method

Standard cost chargeback is based on established prices for computer usage for future accounting periods, usually the coming year. The main objectives are to provide fixed rates for user budgeting prior to consumption and to help MIS anticipate workloads and required resource capacity. Users are able to increase their control over information expenditures by associating future costs with required or desired information. Repetitious jobs incur similar costs from period to period, regardless of other system activity. This chargeback system requires reliable forecasts of usage levels and future costs based on an exchange of MIS and user plans, as well as an understanding of computer vendor and industry costs and trends. This increased need for information exchange and industry tracking requires more time than did the administration of the average cost chargeback system. Users must better understand their own information and service level requirements as MIS budget are derived from them. This chargeback method requires more maturity in the MIS user relationship. Standard costing does not ensure full cost recovery. Negative variances occur when fixed costs and usage are too low to cover MIS expenses and, conversely, positive variances occur if higher than expected usage occurs. Balancing usage patterns to minimize peaks in processing is difficult since there is no price differential based on time of use.

## Flexible pricing method

Flexible pricing chargebacks are based on “economic prices” rather than actual costs, although cost recovery is still a goal. Higher prices are charged for “scarce” resources as defined by management. This requires management to identify and be actively involved in prioritizing the value of work that is run during peak usage periods for each of the resource load centers in the MIS function. Differential pricing that is pre-established and understood by mature users will regulate demand and level off resource utilization as users decide on less costly means of achieving their information needs, such as processing overnight rather than immediately or developing microcomputer-oriented decision support applications rather than submitting work requests to a central programming staff. Budgeting becomes more sophisticated as users have to estimate their workload's value and priority and determine the level of service (which varies in cost) that is required to meet their informational needs. With such a method MIS is better able to utilize its current capacity and prolong upgrades. Management has the ability to influence not only conservation, but also adoption and experimentation. By underpricing a product to specifically targeted users, management can encourage them to learn new and more efficient packages, or to be innovative with current resources to allow these resources to be used in ways that would be difficult to justify in a traditional operating budget. An example would be to encourage standalone micro-computer users to access centralized databases by offering subsidized communication rates and training for a six-month period to users in remote locations.

In summary, chargeback systems differ in the amount of control, accountability and benefit they provide to both users and MIS staff. They also vary in the degree of administrative support, management participation, user maturity and communications that they require to successfully allocate computer resources. Having reviewed the four types of non-profit chargeback systems, it is now appropriate to discuss the organizational perspectives of Synnott and Gruber, McFarlan, and Nolan. These approaches can be used to establish the position and role that information technology has within a company and the degree to which management must be accountable for its use.

## Assessing Information Technology Within the Organization

The model proposed in this article suggests that certain characteristics of the use of information technology in an organization determine the appropriate chargeback system. It is IS management's responsibility to assess this use in their organization and invoke the chargeback system which best supports it. The characteristics to be assessed were extracted from three models, Synnott and Gruber [10], McFarlan, McKenney and Pyburn [6], and Nolan [8] which were chosen because they each focus on the need for senior levels of management to recognize information as a fundamental corporate asset that can have significant impact on the future options available to the organization.

At the same time each author has a unique approach or frame of reference in describing the role, use and management of information. The broadest perspective of management's responsibility for directing information resources is from the industry level. This is the primary focus of McFarlan, et al., [6]. They take an empirical view of the role of information technology, defining its real or potential impact based on the characteristics of the industry and its products. The degree of impact of information technology then determines the relationship between the MIS department and company management. McFarlan, et al., go as far as to say that there are companies where the impact of information technology has so little strategic potential that management properly should not focus on it.

Nolan's [8] primary focus is on management dynamics at the company level and is more limited than the industry view. He suggests the long-term emergence of the mature user who, based on years of experience gained through identifiable stages, rightfully assumes responsibility for making strategic decisions on the use of information.

Synnott and Gruber [10] take a different view from Nolan's. Rather than focusing on the user, they define the rise and development of a new corporate office, the CIO or Chief Information Officer. This CIO develops widespread influence and becomes responsible for guiding, not only information as an asset, but also the strategic direction of the corporation. Their focus is primarily from the department level, with MIS's influence growing as it moves from being reactive to becoming proactive. In summary, management's accountability for information technology is viewed from three different yet complementary levels: industry, company, and department. The following sections describe each of these in detail.

## Impact of information technology: the industry perspective

McFarlan, McKenney and Pyburn [6] suggest that technology is assimilated into a firm through an evolutionary process of four general phases: 1) identification and investment, 2) experimentation and learning, 3) control and, 4) widespread technology transfer. They focus on the importance of information technology to corporate strategy as influenced by such dimensions as company size, complexity of product lines, and how information technology can build barriers to entry or change the basis of competition between firms. In view of this, they define the firm's use of information technology as being in one of four environments depending on the degree to which it supports corporate strategy and the consequent vulnerability of the organization to interruptions in information processing.

Strategic: Companies such as banks and large insurance groups are extremely dependent on information technology for both daily operations and for future applications critical to competitiveness. Senior management and MIS executives need to plan together to identify future opportunities.

Turnaround: Companies in this category receive operational IS support but are not dependent on it for long- or short-term goal achievement. However, the new systems under development are focused on the firm's strategic objectives. Companies in this group could be medium-sized grocery chains or an expanding manufacturer. User management should participate in steering committees and help establish priorities in this environment.

Factory: Information processing is critical for continued operation. Future applications are maintenance oriented and do not provide new ways to compete. Planning deals with service, cost and efficiency. Examples of such companies include airlines, retailers and some manufacturers.

Support: Disruptions in current systems have only limited impact on operations. Current applications and those under development stress efficiency at lower organizational levels and do not address strategic competitiveness. Companies in this category could include large chemical firms, power generating utilities and large process industry manufacturers.

## Stages of growth:

## the company perspective

Nolan [7, 8] describes information technology as being comprised of four separate areas or growth processes:

1. System Resources: includes hardware, system software, telecommunication developments and data processing personnel.

2. Application Software: includes business-oriented packages, user friendly languages, graphics, decision support systems and in-house developed programs.

3. User Awareness and Maturity: user's capability, experience, needs, plans and understanding with regard to using information technology.

4. Organizational Planning and Control Procedures: volumes of growth, logical flows of data, security concerns and procedures, redundancies in effort, system efficiencies, resource acquisition, project selection and funding.

Each of the four areas develops through its own life cycle. Ideally, these life cycles progress at the same rate so that technology, software, maturity, and control are always in balance. A life cycle is defined by Nolan [8] as having six stages:

1. Initiation: automation is introduced and highly structured business functions are performed, such as general accounting.

2. Contagion: Based on early successes, users request additional projects and costs grow rapidly.

3. Control: User management develops controls to set priorities and track MIS projects in an effort to control costs and focus investments.

4. Integration: New technologies and systems are incorporated into the firm and growth again occurs. However, the focus is on building a cohesive information system that can address less structured business functions.

5. Data Administration: Information is viewed as an asset and databases are established that allow integration of most business functions.

## 6. Maturity: Users are in control of information with an understanding of its value and uses.

The reality of the 1980's is that the areas of system technology and application software are developed to such a degree that their capability far surpasses the ability of most organizations and users to properly apply and control them. The implication is that management must focus on developing user maturity and organizational planning and control procedures to correct this imbalance. This is consistent with the stage model which shows an evolutionary shift of control from technical data processing professionals in the first three stages to user and corporate management in the last three stages. [8] The role of the data processing group should shift from that of technical leader to educator to facilitator to consultant and finally to a role of sub-contractor. Key to this evolution is the increasing control that users must develop in planning, directing and controlling information resources.

## The chief information office (CIO): the department perspective

Synnott and Gruber [10] see the 1980's as a transition decade. Most firms will advance from using computer technology for operational systems which address highly structured, repetitive tasks, have a short-time horizon, and are organizationally isolated, to applications that require the integration of business and system planning and insure that information is available to top management levels for less structured, longer term tasks that define the company and its future direction. They explain this transition through an evolutionary model for MIS executives. Initial systems don't require corporate management, user management and MIS management to integrate. Corporate management sets strategic directions. User management identifies and defines areas that need to be addressed and then request that their view of the solution be developed and implemented by the MIS group. MIS management focuses on providing efficient systems and has little knowledge of the company or industry as a whole. This traditional relationship puts MIS executives in a "reactive" role to user needs. But as new systems and technology address company-wide issues and information needs, a “natural coalescence” occurs among organizational groups. MIS managers must prepare for this coalescence in order to take greatest advantage of it. This coalescence planning, according to Synnott and Gruber:

"involves bringing together the diverse information resources of the firm so that they can be used when and if needed by all levels of management and staff. This requires identifying these resources, building the technical delivery systems . . . and putting together organizational structures designed to permit better information flow in the organization" [10, pg. 56].

During this period of coalescence, the MIS executive develops a knowledge of the firm and also consolidates previously separate information functions, such as records management, data processing, word processing, mail services, printing, libraries, telecommunications, micrographics, office automation, information center and administrative services. The key result of this phase is that the MIS executive is the integrator of information flow between corporate management, user management and the MIS function.

From this foundation emerges the CIO. Knowledgeable about opportunities for use of information technology in the industry, the CIO not only sets MIS planning objectives consistent with the firm's overall objectives, but is also able to influence the future strategic direction and opportunities the firm pursues. Synnott and Gruber call this the “proactive” role of the CIO.

A major implication drawn from these models is that senior management must plan for the information resource. Computer chargeback systems relate to management's need to plan by providing the costs that serve as a basis for evaluating the worth of information. They provide a means of estimating future projects by subjecting them to the same analysis used to evaluate more traditional investments.

## Selecting and Implementing a Chargeback System

Once the current and potential uses of information technology in the organization have been asessed, the next concern is to choose a chargeback system that provides controls appropriate for the level of accountability to which management ought to be held. This requires a three-step process of: 1) assessing the current environment based on the three organizational assessment techniques previously described, 2) selecting a chargeback system that provides control to meet management's needs in the assessed environment, and 3) developing an action plan based on the results of the first and second steps to move from the current chargeback system to the desired one.

## Assessing the organization

McFarlan, et al., Nolan and Synnott and Gruber each have developed an assessment approach focused on an aspect of information technology: the impact of technology, the growth of user responsibility and the role of the CIO, respectively. These translate into an industry, a company and a departmental perspective. Therein lies the weakness of each. Similar to the story of the three blind men, each describing the same elephant as either a tree, an enormous leaf or as a hose, depending on whether they touched the leg, the ear or the trunk; these three assessment approaches can be faulted, not for what they observe, but rather for what they don't observe and their inability to present a full picture.

Clarification of this observation and support for the contention that different organizations need different chargeback systems is appropriate here. Nolan [7] describes the need in mature organizations for chargeback systems that, according to his four criteria: 1) state costs understandably, 2) are user controllable, 3) are part of the performance review process of the user, and 4) are sent directly to users at low organizational levels. If this is done, the expected results are more efficient use of resources and better relations between MIS and the user. However, Olson and Ives' [9] empirical research concludes:

“ . . . there is some evidence that the type of charging scheme is negatively related to user perception of system efficiency . . . users may become more frustrated with information services they receive if they see the costs.

It must also be noted that the type of charging scheme did not appear to affect the degree to which users become involved in development and use of information services . . . "

An explanation for this contradiction between Olson and Ives' research and Nolan's theory may be found in the firms sampled by Olson and Ives—manufacturing companies. By applying McFarlan's four categories framework, we see that large manufacturers use information technology largely in a support role where both current and future applications are focused on smooth operations, not strategic objectives and opportunities. In this support role close communications between organizational and MIS management is not needed and has negligible impact on the company as a whole. In this environment, the information provided by a mature chargeback system is not only expensive to produce in terms of the accounting systems required to collect it, but also dysfunctional to use, creating user friction.

Olson and Ives' [9] research also concludes:

"The typical user/managers who are charged for information services receive a bill and, even though they may understand the charges, they do not know how to affect those charges through usage."

Based on Synnott and Gruber's approach, it can be argued that without a CIO in the coalescence or proactive stages, users have few alternatives in the way they consume existing information resources. The CIO is responsible for generating new uses of existing resources that offer improved efficiency to the user, as well as identifying and introducing technologies not currently available to the user. Again, the point being made is that the information provided by a mature chargeback system can be dysfunctional if the organizational environment is not appropriate.

The strength of the model offered in this paper for assessing the company is that it combines all three approaches and demonstrates a need for balance in the relationship of technological potential, user maturity and MIS leadership. The intention is to demonstrate the varying levels of appropriate accountability for management based on the synergistic as well as the limiting effects these variables have on each other. Figure 1 is a cube that uses as its X axis the four dimensions McFarlan, et al., propose in their assessment model. At the origin is the support category, followed horizontally by the factory, turnaround, and strategic categories. This represents a continuum of industry level environments where the impact of information technology on the firm's ability to compete and provide service increases as the firm moves further away from the origin. As previously stated, the greater the impact of information technology on the firm's ability to compete, the greater the level of accountability for which company management must be held.

The Y axis represents Nolan's six stages of EDP growth. At the origin is the initiation stage, followed vertically by the contagion, control, integration, data administration, and maturity stages. This represents a continuum of company environments where the transition of control and use of information systems shifts from centralized technical professionals to knowledgeable end users in organizationally and administratively decentralized areas. The accountability for information resources by general management increases in the advanced stages.

The Z axis, which is the depth dimension of the cube, is a continuum of department environments reflecting the development of the CIO as expressed by Synnott and Gruber. At the origin, the role of MIS management is reactive, with little accountability to the organization beyond efficiency. Further along the axis are found the roles of coalescence planner and proactive change agent. Again, the further from the origin, the more accountability management has for the identification, selection and adoption of information technology.

This model requires that all three perspectives be measured when an organizational environment is assessed. As an example, in terms of accountability the cube shows environments that map into the front, lower left area (nearest to the origin) where applications address structured problems as having the lowest need for management accountability. Environments that map into the rear, upper right area (furthest from the origin) have the highest need for management accountability. These are complex, high cost appli-

INFORMATION TECHNOLOGY

## Lowest need for management accountability

![](/api/attachments/KUNT9CR5/fulltext/images/feb6aa41fe8a5b73d1afcc97672a40addf86a54b34566665dfa594ba2f6d66c8.jpg)

cation areas, addressing semi-structured problems. The diagonal between these two extremes represents other possible environments. The information needs of each of these environments differ and it is necessary to select a chargeback system appropriate to that need.

## Selecting a chargeback system

Each of the four types of chargeback systems has its appropriate region along the diagonal in Figure 1. Allocation chargeback systems which provide summarized financial information in memo form on historic DP costs are appropriate for environments that require little feedback for management to remain properly accountable and in control. Allocation chargeback systems map into the cube for environments that are described from the three axes as being support, initiation and reactive.

Further along the diagonal, more control is needed as the cost, use and potential for information systems increase. Average cost chargeback systems provide the additional control by using "hard money" journals that identify in more detail user groups and types and costs of resources consumed. Average cost chargeback systems map to environments that are best described as being factory, contagion-control and reactive-coalescence.

Standard chargeback systems are next on the diagonal, providing additional controls such as user driven capacity planning and full cycle accountability to the user who now has pre-set prices, repeatable charges and knowledge of and access to alternative consumption patterns. The environment that this chargeback system maps to is turnaround, integration-data administration and coalescence-proactive.

Flexible price chargebacks provide the most control, although they require advanced support systems to fully reach their objective of maximizing the use of information technology in support of strategic objectives. To do this, capacity planning must be developed to the point where alternative future usage patterns can be compared through traditional asset analysis methods considering such things as useful life and the impact of intangible benefits derived from further integration of business functions. Also, budgeting systems must be developed in terms that identify expected results as well as expenditure rates, and management systems must reward users who optimize usage. Flexible price chargeback systems map to environments that are described as strategic, mature and proactive.

Perhaps the greatest problem readers will have when using this model is that companies are not uniform internally. For instance, some user groups are more mature than others; advances in technology and software target individual groups such as engineers and financial analysts more than others; CIO's have areas of expertise where they are more likely to be proactive, and conversely, are perhaps more reactive in other areas. However, if the model is applied at lower levels, such as the divisional level, the exposure of management accountability can still be identified.

The implication of this observation is that the model should be applied at both the macro level of the firm and the micro level of the division or department. The benefit of the macro approach is that it identifies exposure, not so much in control systems, but rather in the effective application of information technology as an asset. The micro level focuses on control systems such as capacity planning, budgeting, and chargeback systems which provide the framework for efficiently managing that information asset.

## Developing an action plan

The previously described steps of assessing the current environment and selecting an appropriate chargeback system meet management's immediate needs using the controls available. To develop an appropriate chargeback system for the long-term requires an action plan and a re-examination of Figure 1. Up to this each of the three axes variables has been viewed as independent, with companies having various levels of development along the three continuums with no requirement to map on or near the diagonal of the cube. To establish an action plan the industry level assessment methodology of McFarlan, et al., must be treated as the sole independent variable in dictating appropriate levels in the other two axes, since their focus is from the narrower company and MIS department levels. This is the variable management has the least ability to change and therefore must be used as a reference point in determining an appropriate longterm chargeback system. Two examples support this definition of information technology as being the independent variable/axis. In the banking industry, information technology has a strategic role to play currently and in the future, defining products, customers and marketing channels at a minimum. This strategic role dictates that in successful companies senior management must be mature MIS users, understanding costs, benefits and uses of information services. This strategic role of information technology also dictates that the CIO role be advanced and proactive, providing new alternatives for the use of existing information as well as new technological products and assistance for senior management in establishing strategic direction for the company. An example at the other end of the spectrum is a public utility company in the electricity production industry. Information technology cannot assume a strategic role since the customers are determined by monopoly rights, the product (electric power) and the distribution system (physical lines) are all fixed. Information technology is used in a support role focused on efficient operations and cost saving. The proper focus of senior management is elsewhere. The CIO can be reactive, that is, responding to line management requests for information technology that address efficiency in operations and direct cost saving, without putting the company at strategic risk.

By comparing a company's current position as mapped in the model (step 1), with the company's desired long-term position (step 3), management can measure its degree of exposure. Exposure includes both “under-management” and “over-management.” Under-management occurs for points below the diagonal where neither end users (company management) nor MIS leadership are ready to use information technology competitively. In addition, control systems that provide feedback, such as advanced budgeting, accounting, capacity planning and chargeback systems, all require further development. Over-management occurs for points above the diagonal where additional information on expenses and uses of information technology is unable to return a benefit equal to the cost of maintaining the management support systems that produce information. The risks/exposures of being strategically under-managed are more severe than being inefficiently over-managed.

## Case Studies

The model described in this article has been used to select chargeback systems for two major user groups of the same data center. One is Public Service of New Hampshire (PSNH), an electric utility supplying power to 80% of the state from 19 generating stations through 17 business offices. The other is New Hampshire Yankee, a business entity jointly owned by 16 regional power utilities, that is responsible for the construction and future operation of Seabrook Station, a twin reactor nuclear generating site. At PSNH the primary focus of the 250 terminal network is providing online customer information statewide, as well as more traditional business applications for finance, engineering, accounting and materials management. Applications at Seabrook address both current construction management for the nine billion dollar project and future management systems for operation of the station. Seabrook's applications are supported by a 100 terminal network connected to an IBM 3081 CPU.

The Seabrook station case traces the migration from an average cost to a standard cost chargeback system and shows the value of the model as a planning tool. The Public Service case demonstrates how an allocation chargeback successfully communicates the cost and value of a major systems upgrade to senior management.

By 1982, the construction of Seabrook Station was already entering its ninth year. Due to its scale, Seabrook Station was jointly owned by sixteen regional utility companies, with PSNH having the largest share and responsibility for construction and operation. Computer-based information systems addressed three aspects of the project: process control of the physical plant centralized in a large control room, construction management of the nine billion dollar project, and plant management to supervise station procedures/operations when completed. Process control systems were being addressed primarily by the equipment vendors such as Westinghouse and General Electric. Construction management was done by United Engineers and Constructors (UE&C), the project's general contractor. Plant management, the focus of this case study, was the responsibility of PSNH through two groups. The Nuclear Information Systems Group (NISG), physically at the site, defined system requirements. The second group, at PSNH's corporate data center, did database design and programming from those requirements. The second group also included the technical support and operations departments which were responsible for the system hardware, software and network.

The initial request to charge the joint owners for computer services came from PSNH corporate management in mid-1982. Initial response was pragmatic and timely. An average cost direct chargeback system was started. Expenses were grouped into six load centers: CPU, disk, tape, print, telecommunications and database. Updates to load center costs were performed every three months by reviewing vendor contracts, invoices and general ledger expense reports. Job tracking and reporting was first done through a package called “JARS” from Johnson Job Accounting. This resulted in a chargeback journal that stated costs in terms of general ledger accounts, rather than in units of use such as CPU hours, lines printed, disk I/O’s, etc. The immediate goal of cost recovery was accomplished.

Many items needed refinement in the chargeback process, such as enforcement of consistent naming standards for jobs, logon ID's and data files, as well as the need to increase the auditability of algorithms developed by system programmers for started tasks and online software products. These products, such as IBM's TSO and CICS, Cullinet's IDMS and Interact, UCCel's UCC7 and UCC11, SAS, and Infodata's Inquire, accounted for nearly half of CPU consumption. In an effort to see what benefits could be derived beyond cost recovery, the vice president of IS requested a chargeback review at the end of 1982. Although not fully developed at the time, the model proposed in this article was used as a framework in the preparation of this review. It required an examination of the role of information technology within Seabrook Station and the nuclear industry, the maturity of computer usage at Seabrook, and the development of the CIO role within the company. This was done to assess the type of chargeback that would match the needs and also provide cost controls.

## Information technology at Seabrook

The plant management applications being developed by PSNH for Seabrook are unique to the industry. Called “FINIS” (Fully Integrated Nuclear Information Systems), these five large database applications provide complete and timely online information for management action during normal operations, preventive maintenance and problem situations. Since the mid 1970's, no new nuclear plants have been started in the U.S. Combining this fact with the accident at Three Mile Island, which was aggravated by poor management procedures, the emphasis of regulatory bodies such as the Nuclear Regulatory Commission (NRC) is understandably shifting from construction to the control of plant operations.

Since FINIS is such a comprehensive plant management system, directly addressing the emerging nuclear regulatory issues, it has the potential to be a system which the NRC might require of all nuclear operating plants. This has led to the classification of Seabrook's information technology as being turnaround, meaning that it was not strategic for current operations but would be for future operations. The future strategic importance of the system meant that corporate and Seabrook management, rather than just low level users and MIS managers, needed to be involved in the decisions affecting FINIS. The chargeback method would need to summarize past expenses and provide a basis for projecting future costs. Additionally, the chargeback system would need to convey the value of the information, along with its costs, so that management would be informed of the risks and benefits of this multiple year, multi-million dollar project. Put more directly, the chargeback system needed to provide a basis from which alternatives could be generated and evaluated by management, in addition to transferring costs.

## MIS maturity at Seabrook

To determine the degree of MIS maturity at Seabrook each of Nolan's four areas of development was examined. System resources were well utilized including use of current hardware and system software for CPU, disk, tape and print functions through a well maintained and responsive network. Application software included a database management system equipped with a screen development and prototyping utility. Fourth generation software aimed at end-user computing was available for statistical modeling, database queries, report writing, word processing and personal computing. All of these were supported through an information center that provided training and assistance on request. User awareness and maturity had grown throughout the project's nine-year life to the point where there were selected areas with their own user analysts defining and designing application requirements for mainframe systems and actively using the fourth generation software through the information center. Organizational planning and control procedures experienced the most change. With the construction project several billion dollars over budget and years behind schedule, it was clear that cost control procedures for all aspects of Seabrook would need to be enhanced, including information systems. Taking all four areas as a whole and placing them into one of Nolan's six stages, Seabrook's maturity in the usage of information technology was evaluated to be in the control stage moving toward integration. This implies that user management was mature enough for additional control reports and that the information from the chargeback system would not be dysfunctional and frustrating. Rather the chargeback information would serve as a basis for associating the value of information services with their cost and generating alternatives to maximize MIS expenditures.

## CIO role at Seabrook

The last dimension to be analyzed was the role of the chief information officer. The CIO role had developed within PSNH to where the IS chief was a vice president. Within the IS budget were all hardware, software, telecommunication equipment and development and technical labor. Additionally, the budget included the company mailroom, duplicating equipment, word processing equipment, office automation, the corporate library, records management and storage, and the information center. Personal computers were budgeted by users, but had to be approved and supported by the information center. Normally such an organization would lead to the classification of the CIO's role as proactive, but because of the unique organizational structure presented by Seabrook (sixteen co-owners) the CIO's ability to set future directions and priorities for implementing information technology at Seabrook was significantly reduced. Thus a classification of coalescence was more appropriate. By late 1984, this organizational structure had evolved to the point where Seabrook Station had become the responsibility of New Hampshire Yankee, a unique division within PSNH with its own president accountable directly to the sixteen joint owners. In terms of the chargeback system, the impact of having an advanced CIO role was that the IS group was developed enough to be able to anticipate and plan alternatives for future usage of information technology rather than simply responding to request for services as efficiently as possible.

## Impact on IS management

The result of mapping Seabrook into the model (Figure 1) showed that for its environment (turnaround, integration, coalescence), the best type of chargeback system would be standard cost, rather than the current average cost system.

The initial value of using the framework presented in the model was that both the IS administration department and the vice president focused not on the detailed process of transferring expenses, but rather on the issue of the level that would allow project management and the corporation to associate the cost of services with the value of the information? Once this decision was made, the degree of detail and types of administrative systems needed to support a standard cost chargeback system were identified and an action plan established.

The primary difference between the two chargeback methods was that standard costing required the forecasting of system capacity, utilization levels and IS expenses in order to establish fixed rates for future periods. To facilitate this, four major changes were made. First, PSNH decided to change system accounting packages in 1983 from JARS to a Morino Associates' product, MICS, to collect greater detail on standard tasks and online products.

The second change was occasioned by the need to enforce and standardize reporting on naming conventions used for file, logon's and programs. To address this, PSNH installed a security package from SKK called ACF2.

Disk storage was growing at forty percent a year, increasing from twenty gigabytes to forty-five. System accounting packages such as JARS and

MICS only measured I/O activity, not actual track space used. PSNH's third change was the installation of UCCel's UCC3 disk management package. It identified growth areas and file sizes by user groups, providing the basis needed to project future use and costs, and also reviewed storage alternatives, such as tape, from a cost perspective.

The fourth change was organizational and procedural, rather than product related. A centralized invoice management function was established within the IS administration department. Previously, IS-related invoices went directly to one of as many as eight department managers for verification prior to being sent to corporate accounts payable. This change provided a basis for building cost pools that were accurate and timely.

These four changes (MICS, ACF2, UCC3, invoice management) were fundamental in establishing the basis of the standard cost chargeback system. However, it is important to emphasize that sufficient lead-time was critical to Seabrook having the basic information for a standard cost chargeback system. Each element took twelve to fifteen months to select, implement and test and no amount of management pressure or additional resources could have shortened this process.

## Corporate PSNH

The initiation of a chargeback system for corporate PSNH came about under different circumstances. In December of 1983, it became apparent that a \$1 million CPU upgrade from an IBM 3083 to an IBM 3081 was required. This change attracted top management attention for three reasons: 1) it came about unexpectedly, 2) the company's credit rating did not permit long-term lease or third party financing, which meant a painful cash outlay, and 3) no assurances could be given that future upgrades would not be required. To aid the IS steering committee to understand the importance of this upgrade, an allocation chargeback memo was prepared, summarizing what IS costs were incurred by the major functional areas of the company. The report indicated that the major benefits of the upgrade accrued not to the IS division, but to other corporate areas and were essential and justified.

The corporate allocation chargeback has been formalized and is done on a quarterly basis. AIthough the IS department is capable of administering an average cost or a standard cost system, a decision was made in early 1985 to keep the corporate chargeback on an allocation basis.

Assessing the appropriateness of this charge-back method requires a review of the company from an internal point of view. Using the information technology dimension of the model, computers at PSNH provide a support role in most areas such as personnel, accounting, materials, rates, purchasing, billing, etc. In selected areas, such as district operations, computer usage performed factory role. The customer information system is an online, state-wide, network application which provides information to consumers about usage, rates, balance and location changes. Also, it helps schedule lineman work assignments in response to customer requests. These functions provide a direct interface to the public. This is extremely important during the final years of construction on Seabrook when political/public support for the company is strategic to survival. More control is required for these services in terms of capacity planning for terminals, lines, controllers and response time. The completion of Seabrook will increase the need for better and more flexible consumer support systems as prices rise and rate structures become more complex.

In terms of Nolan's maturity dimension, PSNH is nearing the end of the control stage and entering the integration stage similar to Seabrook. Examples of controls and maturity include: end user departments having full-time analysts, a steering committee that reviews all projects in reference to the five-year ISS plan, user group meetings, internal standards having been developed, and the existence of a formal database administration group.

The CIO role is fully developed and proactive. The vice president is responsible for IS functions and other support departments. Within the IS budget are all hardware, software, telecommunication equipment and development labor. Additionally, the budget includes company mailroom, duplicating equipment, word processing equipment, office automation, library, records management/storage, and information center costs.

The difficulty of mapping PSNH to the cube is that the proactive CIO role, along with the wide range in user maturity, appears inconsistent within a company where information technology is primarily support in nature. IS management recognized this variance and chose the following solution. An allocation chargeback would be used company-wide as long as the focus of most applications remained support in nature, and at the same time IS would provide advanced user departments or feasibility study teams with the cost information they desire on an informal basis. This approach provides selective cost information without creating friction in other parts of the company. The implication is that, on an informal level, an advanced chargeback system has to be maintained. For PSNH, however, this is not a problem since a standard cost chargeback effort is underway at Seabrook and most of the necessary data is available.

## Summary and Conclusion

The thesis of the article is that a model could be developed that would define the controls required by management to ensure that a proper level of accountability was being maintained for information technology uses and expenditures. Further, it was proposed that the model could identify management exposures and provide insights for management action. To that end, four chargeback systems have been described, each with increasing management feedback and support costs. Three assessment theories for managing information technology were reviewed. A model interfacing the theories was developed and the four chargeback systems mapped into environments within that model. Finally, the process of developing a successful action plan to match control systems with management accountability was discussed. Two case studies were used to display the applicability of the model. Further research should focus on empirical application of the model on both a micro and macro level and in the development of criteria to enable management to properly assess their organizational status on each axis.

## References

[1] Bergeron, F. Conditions of Effectiveness for Data-Processing Charge-Back Systems. Doctoral dissertation, University of California, Los Angeles, 1984, No. 20147.

[2] Drury, D. "Conditions Affecting Chargeback Effectiveness," Information & Management, Volume 5, Number 1, May 1982, pp. 31–36.

[3] Howard, P. "Standard Costing in Data Processing," EDP Performance Review, Volume 9, Number 6, June 1981, pp. 1–6.

[4] Joy, J. "Pricing DP Services," Journal of Systems Management, Volume 28, Number 11, November 1977, pp. 36–41.

[5] Lin, C. "System for Charging Computer Services," Journal of Systems Management, Volume 34, Number 11, November 1983, pp. 6–10.

[6] McFarlan, F., McKenney J. and Pyburn P. "The Information Archipelago—Plotting a Course," Harvard Business Review, Volume 61, Number 1, January/February 1983, pp. 145–156.

[7] Nolan, R. "Controlling the Costs of Data Services," Harvard Business Review, Volume 55, Number 4, July/August 1977, pp. 114–124.

[8] Nolan, R. “Managing the Crises in Data Processing,” Harvard Business Review, Volume 57, Number 2, March/April 1979, pp. 115–126.

[9] Olson, M. and Ives, B. "Chargeback Systems and User Involvement in Information Systems—An Empirical Investigation," MIS Quarterly, Volume 6, Number 2, June 1982, pp. 47–60.

[10] Synnott, W. and Gruber W. Information Resource Management, John Wiley & Sons, New York, New York, 1981.

## About the Authors

Dr. Kallman received his B.S. in Economics from St. Peters College (Jersey City) and both the M.B.A. and Ph.D. degrees from the City University of New York. He is currently Professor of Computer Information Systems at Bentley College, Waltham, Massachusetts. He has published a number of articles in such journals as Long Range Planning, Managerial Planning, and Planning Review, and is co-author of The Practice of

Planning: Strategic, Administrative, and Operational (Van Nostrand Reinhold, New York, 1981) and Information Systems for Planning and Decision Making (Van Nostrand Reinhold, New York, 1984).

William P. McKinnon is currently Supervisor of Administration and Planning within the Information Systems and Services Division of Public Service Company of New Hampshire. He received his M.B.A. with a concentration in management information systems from Bentley College, Waltham, MA in 1984, and his BS in Accounting from New Hampshire College in 1981. He chairs the computer committee for the town of Goffstown, NH and consults with gasoline retailers on business automation systems. His experience includes three years as a business analyst/programmer in the insurance industry and three years as an analyst with Public Service.
