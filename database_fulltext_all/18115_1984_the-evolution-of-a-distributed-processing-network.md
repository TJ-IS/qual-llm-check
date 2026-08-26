---
otero_id: 18115
otero_key: "FS87YE92"
title: "The evolution of a distributed processing network"
authors: "Lori Franz; Arun Sen; Terry Rakes"
year: "1984"
journal: "Information & Management"
doi: "10.1016/0378-7206(84)90050-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Evolution of a Distributed Processing Network

Lori Franz, Arun Sen, and Terry Rakes
College of Business Administration University of South Carolina,
The H. William Close Building, Columbia, SC 29208, USA: tel:
(803) 777-2787

Current trends in information systems technology increase the advantages of developing an increasingly complex distributed processing capacity. Distributed processing networks (DPNs) are expected to evolve gradually from centralized systems into more complex configurations. The introduction of major changes in organizational structure, such as those precipitated by mergers or acquisitions, also require rapid changes to the DPN. This paper describes four distributed processing configurations. It then presents a case: the evolution of the DPN in a large corporate bank and holding company. This case illustrates configuration changes over the life cycle of the DPN of the bank and provides insight into the process of planning for DPN change. A tendency to return toward centralization is noted in this case; this may cause practitioners to rethink their own DPN growth plans.

Keywords: MIS Management, Distributed Processing, Networking, Configuration Planning

![](/api/attachments/FS87YE92/fulltext/images/8880779a6d8711db5fc48fa25e927edf7aab73855502254b08a53d86fe3cc280.jpg)

Lori Sharp Franz is an Assistant Professor of Management Science at the University of South Carolina. She received a Ph.D. in Management Science in 1980 from the University of Nebraska. Her work experience has included industrial programming and systems analysis as well as the development of models to assist in personnel scheduling and mental health planning. Her published papers include articles in the Journal of the Operational Research Society, Computers and OR, Decision Sciences and numerous conference proceedings. She is a member of AIDS and ORSA. Her current research interests are in the area of multiple criteria decision making and decision support systems, with a focus on applications in the public sector.

## 1. Introduction

A distributed processing network (DPN) can be defined as a system where various data processing elements are partitioned into well-defined units that may be located at various logical sites and linked by appropriate protocols [5]. A protocol is a scheme that regulates the transmission of messages by controlling the access that each data source (computer or terminal) has to the communication medium, such as a simple random access scheme that allows terminals to transmit at their discretion but provides randomization of retransmission when messages collide. The elements of the DPN include hardware components, data, applications software,

![](/api/attachments/FS87YE92/fulltext/images/b8067b844344f80abe8fa45874a278e3d71e60c120447387f019204b54a60b65.jpg)

Terry R. Rakes is an Assistant Professor of Management Science at the University of South Carolina. He received his Ph.D. in Management Science from Virginia Polytechnic Institute and State University. He is a member of AIDS and TIMS. His current research interests include simulation, multiple criteria decision making, management science applications in distributed processing, and modeling in the public sector

![](/api/attachments/FS87YE92/fulltext/images/2d890f9237ca7eea5b6d3617195b6b4828be983802fc36046dbdaf19c7a6be21.jpg)

Arun Sen is an Assistant Professor of Management Science at the University of South Carolina. He received a BS in Physics from Bhagalpur University, a M. Tech. in Electronics from Calcutta University, a MS in Computer Science from the Pennsylvania State University, and a Ph.D. in Business Administration from the Pennsylvania State University. His teaching and research interests are decision support systems, expert systems, office information systems, information resource management, management information systems, data base systems, distributed processing and data base, applied operations research, and management science. He is a member of ACM, TIMS, and AIDS.

and various systems software. If data processing staff is also dispersed, then the system is said to be decentralized as well.

Very little has been written to describe the evolutionary development of DPNs. Unfortunately, in a rapidly changing area such as computer processing, in which technological innovations and user demands are in constant flux, there may be little time for introspection as data processing management strives to keep up with their expanding needs and the exploding technology. However, as more and more organizations develop mature DPNs, the question of the appropriateness of the configuration and its potential impact become more salient. While many computer professionals are extremely optimistic that the appropriate configuration will involve ever increasing degrees of distribution of computing power via sophisticated networks $[1,4,7]$ , the observer who remembers past responses to growing computer technologies may be less optimistic. For example, the prediction of the all-encompassing corporate MIS has never come to pass $[2]$ . It is possible that the development of completely distributed systems may be an equally illusive goal – one in which the benefits do not necessarily outweigh the costs in resources and corporate energy.

While a high degree of distribution certainly should not be a foregone conclusion, the evolution in this direction is a fact for many organizations. DPN evolution includes changes in both network size and complexity. Most growth or evolution paradigms, such as Nolan's six stages of growth [6], offer little help to the practitioner or researcher in either characterizing or prescribing the degree of decentralization during an organization's transition to distributed processing. Thus a more relevant characterization of the evolution of DPNs is required; such a characterization would permit the investigation of the premise that DPNs tend to grow increasingly large and complex.

This paper has two purposes. First it presents a method for classifying any organization's DPN by configuration type and illustrates it via a case study. DP management can use this categorization procedure for describing their current network configuration as well as proposed network designs. The process provides the practitioner with a systematic view of the current status of DPN in the organization. Additionally it provides insight into potential problems which accompany certain stages of evolution and the necessary management considerations which enable smooth transitions as DPN changes are implemented. Secondly, the case provides an example of a company that experiences growth then contraction of its DPN.

## 2. Describing the Evolution of the DPN

The evolutionary process of DPNs typically develops in one of four readily identifiable configurations: 1) centralized, 2) star, 3) fully connected, and 4) hybrid. The configurations are primarily used to denote a growing complexity of hardware architecture but may also serve as indicators of parallel decentralization of data and management control.

The advantage of using these hardware-based classifications is that: 1) they can be shown to describe all possible networks [3], 2) unique cost structures and operational properties can be described for each structure; this permits comparisons of potential configurations as well as precise descriptions of existing ones, and 3) since the configuration is a surrogate measure of the complexity of the DPN, the evolution of any stage of the DPN can be tracked by describing the network and noting the structures.

The various configurations are:

Centralization: The initial phase of DPN development is centralized. A centralized configuration includes a mainframe computer and may include remote terminals (see Fig. 1a).

Star: This structure of DPN involves the addition of intelligent hardware to the centralized configuration. It may include intelligent terminals, switches, or additional computers (mini, micro, and mainframe) operating in communication. The Star network is characterized by some node, frequently the central computer, which acts as a switch through which all data flowing between intelligent hardware is controlled (Fig. 1b).

Fully Connected: In the fully connected structure each node with intelligent hardware has a dedicated link to every other node in the network (Fig. 1c). The ability to route communications may be resident in any or all of the network nodes. That is, each node may act as a network switch.

Hybrid: The hybrid DPN structure is a general interconnection, it can evolve from a star or a fully connected network architecture. For example, both networks in Fig. 1d may have evolved from the star of 1b or from the fully connected structure of 1c, where at least one of its nodes has a dedicated link to another node without going through the central switch. Or they can have resulted from dropping one or more links in 1c.

![](/api/attachments/FS87YE92/fulltext/images/b93921ed68a9bc17809e9dcb4dab7869a3359f4cc150c689b4f7aa3f4b1e609a.jpg)  
Fig. 1d. Hybrid structure.  
Fig. 1. Examples of Four Structures.

In many instances, the evolution of the DPN begins with a centralized configuration and moves slowly through the star structure to a hybrid. The hybrid and fully connected may not be attractive configurations in those organizations wishing to maintain a centralized control of their data processing and therefore may never be utilized. The hybrid may also be only a transitory stage culminating in the implementation of a fully connected configuration. In a complex and expanding network the structure may oscillate between fully connected and hybrid as changes in hardware or addition of a communication linkage alter the classification.

With this classification scheme, a graph can be drawn to represent the DPN at each point where a technological change of hardware or communications is made. By assembling a chronological ordering of these graphs, the evolution of the DPN can be described. Frequently, change in the DPN embodies growth, as when hardware and/or communication links are added to the system. However, it is also possible that the DPN might contract due to:

\- elimination of service to a given node or nodes.
- the removal or downgrading of hardware or terminals at a node.

\- elimination of communication links.

The following case is such an example. Its DPN has grown in size and complexity, maturing over time, and will eventually return to a simpler configuration. The forces and motivations that brought about these changes are similar to those of many organizations; consequently they provide insight into the DPN evolution process.

## 3. An Illustration of DPN Evolution

First Union National Bank is a large commercial and retail bank with corporate headquarters in Charlotte, North Carolina. The holding company, First Union Corporation has a computer service center, First Computer Services, Inc., which manages the computer resources and computer processing for the bank. The computer functions of an affiliate institution, a mortgage bank serving 13 states, are also managed by this computer service center. The commercial bank is one of the three largest financial institutions in the state, with over 200 branches in 70 communities. Listed on a major national stock exchange, the corporation could be best described as “growth oriented.” First Computer Services is an effective arm of this dynamic organization.

In 1968, the organization boasted two mature computer systems which fully managed the banks' transactions processing, accounting, and customer accounts. The first system was located in Charlotte and was dedicated to processing transactions for the commercial bank. The second system, located to the east in Raleigh, North Carolina, was dedicated to handling the functions of the mortgage bank (Fig. 2). These systems were two separate, centralized computer systems; there was no telecommunication between them (see Fig. 3a). The data flow for the commercial bank was very simple. Checks were transported by vehicle to the data processing center and the resultant reports were later returned to either central bank management in Charlotte or the branch bank management (or both).

Between 1968 and 1970, system development occurred at a rapid pace. By 1970, hardware at the two sites had been upgraded; the Charlotte center had an IBM 370/155, the Raleigh center an IBM 370/145. Increased computing power provided more detailed account information and faster response time. While terminals were added for credit card authorization, the systems remained batch oriented without telecommunication (Fig. 3b). Thus, the DPN remained centralized.

Over the next two years, management become aware of economic and operational factors that predicated increasing influence over the way data processing was performed: the float due to delay in the clearance of checks was more of a problem as annual check volume increased and transportation of checks to Charlotte in time to meet the Federal Reserve System clearing time was costly (both in terms of manning the fleet of vehicles and in the opportunity costs of missed clearing times). On the positive side, technological changes allowing distribution of the processing capability had made it feasible to do something about this. In 1972, the decision was made to take the first step toward a statewide, distributed processing system.

![](/api/attachments/FS87YE92/fulltext/images/d79508b95fb0ae3e09c64d1d37885e456beb42e9444a0138331fe6fe1d847372.jpg)

The state was split into four quadrants, with a data center located in each, for faster check clearance. The new sites were designed to act primarily as data centers for check and item processing. Since the headquarters of the commercial bank with its associated large processing demands was in Charlotte, the mainframe computing capability and primary data storage were kept there. Program development, maintenance, and managerial control of the commercial banking system also were still in Charlotte. The mainframe was upgraded to a multi-processor system with two IBM 370/158's. The mainframe at Raleigh was downgraded to an IBM System 3 and linked to Charlotte via telecommunication. Item processing in the Raleigh quadrant and work from the mortgage bank were performed at this site, with a data processing staff of 12 persons to develop and maintain mortgage bank systems, although processing was executed at the central node in Charlotte. Further online activity was facilitated by the addition of audio-response terminals which allowed tellers to process account inquiries and verify balances.

Minicomputers were also located in Lumberton, Greenville, and Asheville in the other three quadrants; (Fig. 2) these were connected to Charlotte via telecommunication links, primarily to facilitate more timely item processing. At this point, the logical hardware structure had become a star network (Fig. 3c). Checks were processed at the branch sites, with data files maintained only for that day's transactions. These files were transmitted at the end of the day to the Charlotte center. Reliability of the system at this time was almost entirely dependent in the availability of the mainframe in Charlotte. Data processing management attained a 98% reliability with reliability defined as “the capacity to run any job when scheduled.”

Thus, the bank and its computer service center had truly become both distributed and decentralized. Regional offices, and especially the mortgage bank in Raleigh, gained control over portions of their own processing. Programming changes were implemented to overcome interconnection problems. Distribution of regional account files was considered but rejected, as economies of scale indicated centralized data and technology. The desire to maintain equivalent services to any customer at any branch, including those outside the customer's region, supported the centralization of data decision.

The early transition period, i.e., while an organization is first attempting to distribute computing power, may present many problems. The more common are:

\- loss of central D.P. control in order to maintain continuity of operations during the implementation phase

\- lack of coordination as users assume more responsibility

\- need to make ad hoc changes to the configuration in response to user demand

\- difficulty in finding new or retraining existing personnel to implement the new technology

\- changeover difficulties as new technology is introduced

\- difficulty in evaluating the cost/benefit tradeoff of new technology.

These are indicative of the pressures inherent in developing and implementing any new system in a relatively short time with “great expectations.”

Although there was potential for disruption, the bank service center executed a relatively smooth, problem-free implementation because of their commitment to careful planning and management control. Over the next eight years, the banks continued growth caused an 8 to 10 percent average annual increase in transactions. Consequently the number of online systems at First Union National Bank had to grow rapidly to handle increased volume. The changes included a direct link to the regional bank credit card authorization center in St. Louis, systems for commercial and consumer lending and customer information, as well as implementation of automatic teller machines (ATMs). To facilitate these online operations, a corporate data base and data communication system were needed.

The ATMs were installed point to point to the mainframe. Distribution of ATMs was rejected in order to provide the highest possible reliability and efficient service for any customer of any ATM. At this time, the measure of reliability was re-defined in terms of endpoint availability: “the percent of time that the system is available to the customer.” The installation of ATMs changed the environment to a realtime data processing network operating continuously.

The operational complexity of the network was greatly increased, as considerations of service level, reliability, and maintenance became paramount. Prior to this time, system users had all been employees; now customers were primary users. Thus computer services' role changed from providing organizational support to an integral element of customer service.

A minimum target reliability level of 97% was set by data processing management. But in order to insure this, the mainframe in Charlotte had to attain at least a 99% operational reliability. Data processing management recognized at this time that reliability must be designed into the system. This realization brought about an operational commitment to proactive network management and planning. Procedures were implemented to track problems and forecast downtime so that preventative maintenance during nonpeak hours could be scheduled to insure high endpoint availability to consumers. Using this policy the target reliability was achieved.

During this period, online systems growth was accompanied by the evolution of the network into a hybrid configuration. This happened because of the development of a mortgage information system which was designed to assist the mortgage bank in processing loan applications. The configuration changed as two IBM Series-1 computers were added at Raleigh. The first (denoted as R' in Fig. 3d) serviced as a communication link to offices in thirteen states as well as an online interface to the mainframe at Charlotte where the customer information system could be accessed. The second processor (denoted as R'') served as controller of mortgage production programs and their associated databases (Fig. 3d).

It is interesting to note that this hybrid structure was developed as a complement to the organizational structure of First Union National Bank. Since the mortgage banking operation in Raleigh is essentially a self standing entity not under the managerial control of the commercial bank in Charlotte, there was little impetus to centralize its data under Charlotte's operation. Data at this time continued to flow from the branch sites to the central node of Charlotte, with no need for direct data exchange between branches.

This was definitely a growth period in the bank DPN's evolution with service to users becoming a primary focus. The installation of IMS in 1973 marked a strong corporate commitment to database/data communication. Control and reliability in the network became a major concern of the DP department during this stage. The characteristics of a DPN typically change as an organization gains implementation and operational experience with the network. Once major user demands have been achieved, attention can be turned to improving the DPN and developing less critical extensions of the network. At this point time pressures inherent in getting sytems developed, debugged, and online within tight deadlines may be relaxed.

Characteristics of this growth period include:

\- a focus on improving service to users, as opposed to the application orientation of the earlier period

\- a functional orientation, in which the DP group attempts to standardize processes that perform functions common to all applications. A data base approach is needed

\- contingency and “disaster” plans, in case of component failure in the network

\- centralized planning, control, and project management for the DP department

\- need for careful consideration of security problems as the DPN grows more complex

\- long range planning with possible reprogramming of early applications to bring them in line with new standards.

These activities may be viewed as refinements to the DPN rather than major changes.

During 1981, a major change to the First Union National Bank network was precipitated by the acquisition of a bank in a remote county of the state. The acquired bank had assets of three hundred million dollars and a well established computer center of its own. The primary consideration was to assimilate the bank into the organization rapidly so that the services associated with First Union could be provided in the acquired bank: although service to the existing customers could easily be maintained, it was considered to be imperative that any customer could receive the same level of service at any branch throughout the state. The newly acquired customers had expectations, including addition of ATMs and the statewide banking privileges of the larger bank.

The integration of the new bank into the network was complicated because of the short lead time in which the changes had to be made. Because most acquisition and merger negotiations are kept secret until the final agreement is reached, the data processing planners were not informed and consequently were forced to respond more quickly than with most major network changes.

The computer service center began transition planning by examining existing functions of the acquired bank to see if any of these were outside their current capability and should be considered for addition to the corporate system. When no such functions were identified, the primary problem became one of updating corporate databases with the accounts and information of the newly acquired customers. The new location was then linked to the corporation mainframe computer. It was designed to function as a data center, much like the centers at Lumberton, Greenville and Asheville (Fig. 3e).

The graphs in Fig. 3 show how development closely followed the organizational structure of the bank. The graphs illustrate both the strong central control of the computer services management and the relationship between the main bank and branches. As the acquisition of the new bank changed the organizational structure, the change was reflected by the new DPN configuration.

The bank today (Fig. 3e) can still be classified as being in a growth stage of DPN evolution. They are still adapting the network to user needs and are primarily concerned with maintaining network function. Their development is maturing, however, as evidenced by the desire of management to redesign the network configuration to minimize costs while retaining its operational effectiveness.

When a DPN approaches maturity, the computer professionals and users have adapted fully to the new technology. Operational problems of distributing databases and data communication over a complex network have been met.

At this stage concerns typically focus on:

\- optimizing the DPN configuration with consideration of how best to distribute and partition the database over the network so as to minimize communication and storage costs while maximizing data availability and reliability

\- network security with predefined in-house security measures

\- carefully studied, planned change with a research and development team evaluating new technologies

\- developing an auditing function for DPN

\- development of an approach to monitor standards, disciplines and protocols, interdivisional systems concepts, designs of EDP in all units

\- interest in integrating word processing, elec-

tronic mail or other technologies into the system

As the First Union National Bank's DPN approaches maturity, the concerns of management have focused on determining configuration improvements. Future plans of the organization include major network changes to ensure the viability of the organization in the event of natural disaster and the capacity for continued high level service to customers in the case of computer malfunction. As the organization has become increasingly dependent on the computer to perform its function, it has become more vulnerable. The organization's survival and competitive posture is dependent upon the machine and its configuration.

Another motivation for these network changes is increased usage of ATMs and their resultant electronic funds transfer capabilities. This has increased usage for routine transactions, such as payments, queries, and withdrawals and resulted in a shift in the data flow pattern with projected reduction in non-ATM traffic volume. The shift in data routing directly toward the central banks and away from remote branch sites will obviously prompt management to re-evaluate the current distributed structure in light of a more centralized one.

The projected future configuration includes the consolidation of computer power and function at Raleigh into a single mainframe. Using redundant high speed communication via satellite, the site will serve a secondary function of providing backup for the essential operations of the network. Data centers will be phased out (Fig. 3f) in order to provide the necessary system reliability. It is estimated that the network will eventually support over one thousand terminals and one hundred and fifty ATMs, with all teller stations automated. Such a system will prove to be economically more attractive as the eventual volume of checks processed decreases with the increased use of electronic funds transfer.

These plans show a notable contraction of the computer network Although the organization has found many reasons for further distribution of computer resources, the strategy is one of opting for control and reliability via a more centralized position.

The First Union National Bank example supports the idea that DPNs tend to evolve incrementally. However, the idea that “distribution or decentralization is irreversible” is found to be untrue. There are two possible explanations for this. First, it might be assumed that either banks, or possibly this bank in particular have a stronger need for centralized processing than most organisations. If this were so, contraction of the network would be expected.

Another explanation is that the DPN will expand in the organization until the entire function of the organization becomes dependent on the network. As its vulnerability is assessed and as the complexity of the DPN makes it more difficult to control the computer resource, management may seek to design a configuration that minimizes these problems. A likely response might be contraction of the DPN to increase the control and decrease its vulnerability. If this is the case, it would be expected that network contraction would become a common occurrence in DPN evolution. The decision to contract the network would be contingent on the need to spend additional resources to improve reliability, thus reducing vulnerability to failure, and the success with which the organization is able to control the distributed resource.

## 4. Guidelines for Management

From the bank's experiences several guidelines can be suggested. Most notably:

1) The present and projected future data flow of the organization must be examined carefully prior to any DPN design decisions. Identify the destinations of responses and reports and the sources of transactions and queries. A diagram of data flows will suggest likely configurations. Realize that changes in data flow directions or increases or decreases in traffic volumes may precipitate alteration of the DPN at a later date. In the case of First Union National Bank, the introduction of ATMs and the resulting shift in data flow pattern was just such a change. These changes should be anticipated, if possible, to facilitate later expansions or contraction of the network.

2) The desire to distribute is closely tied with the organizational structure. Just as changes in data flows must be anticipated, so must changes in organizational structure. Acquisitions such as the First Union merger and other structural changes may precipitate DPN reconfiguration.

3) The external environment may also dictate changes in the DPN configuration. In the case of First Union National Bank, alterations in the Federal Reserve check clearing policies had great impact on the attractiveness of certain configurations. Networks which are sensitive to pressure from the outside should be designed to simplify any likely alterations in DPN configuration which might occur. Again, anticipation of possible change is a key to DPN planning.

4) Reliability of the network is critical. Network designers must define this meaning of “reliability” and decide on the level of reliability appropriate to their operations. Reliability must then be built into the network, with the configuration choices and systems programming designed to meet this goal.

5) The decision to distribute processing must be made for three functional areas with a separate distribution decision for each. The areas are:

\- management – can the managerial function be distributed or is central control desirable?

\- operations – can the operations of the network be distributed or is centralized processing necessary?

\- development and maintenance – can the development and maintenance of the system software be handled better centrally or at user sites?

Cost considerations, reliability of the system and the need for control dictate whether distribution occurs in one, two or three of these areas.

6) A proactive style of DPN management is preferable to reactive style. Network decision makers must continually plan for the future, forecasting changes that will impact on the DPN. Continual review of network operations and alternate configurations, including those involving contraction of the DPN, will provide the best, most effect DPN.

The focus on the DPN can be expected to change as the organization gains experience with the distributed network. Anticipation of the problems during early development and an awareness of the characteristics of a growing and maturing network can help minimize the problems associated with the changing DPN environment. By realizing that the current configuration may require modification, and by continually evaluating alternative network configurations, changes can be made with little or no disruption to the organization.

## 5. Conclusions

The case study chronicles the evolution of the DPN of the holding company of First Union National Bank, a large southeastern bank, using graphs to represent various stages in its evolution. Banks are a particularly interesting setting for study because they have developed mature data processing systems over the last two decades. In an attempt to improve service, banks with branches at remote sites are moved toward distributed systems by competitive pressures and by users' requests for improved information services. As competitive pressures have increased, acquisition and merger are more frequently seen as remedies for both the smaller bank struggling to remain competitive and the larger bank wishing to achieve growth or economy of scale. Such organizational changes have further amplified the demands for changes in the DPN.

In one sense, banks, with mature DPNs, may be considered models of evolution that other organizations may follow. If so, this case disproves the popular notion that DPNs will inevitably evolve toward more distributed and complex configurations. Further study is needed of the phenomenon of contraction of the DPN (to ascertain whether the observations of this case are unique to banking).

Papers discussing the phased implementation of sophisticated DPNs in organizations are rare to non-existent. Consequently, this case provides valuable insight for DP managers; they can compare their own DPN's developmental stages and growth characteristics to this case to aid them in planning changes in their own organizations. Practitioners who identify a need for strong control and reliability, as found in this case, may wish to evaluate the need for recentralization.

## References

[1] G.M. Booth, “Distributed Information Systems,” Proc. AFIDS (1976) 786-794.

[2] G.B. Davis, Management Information Systems: Conceptual Foundations, Structure and Development, McGraw-Hill Book Company, New York, 1974.

[3] L. Franz, A Sen and T. Rakes, “Managing the Evolution of Distributed Processing Networks: A Framework,” Proceedings of the Southeast AIDS Meeting (1982) 34-36.

[4] E.C. Joseph, “Distributed Function Computer Systems: Innovative Trends,” Digest of Papers, COMPCON 1974 (Spring 1974).

[5] H. Lorin, Aspects of Distributed Computer Systems, John Wiley and Sons, New York, 1980.

[6] R. Nolan, “Managing the Crisis in Data Processing,” Harvard Business Review (March-April 1979) 115-126.

[7] S.E. Scripski, “Distributed Processing Grows as its Hardware and Software Develop”, Electronics (May 1976) 91-97.
