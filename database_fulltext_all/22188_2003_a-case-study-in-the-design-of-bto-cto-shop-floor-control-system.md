---
otero_id: 22188
otero_key: "TCQXWG8W"
title: "A case study in the design of BTO/CTO shop floor control system"
authors: "Ruey-Shun Chen; Kun-Yung Lu; Shien-Chiang Yu; Hong-Wei Tzeng; C.C. Chang"
year: "2003"
journal: "Information & Management"
doi: "10.1016/s0378-7206(03)00003-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A case study in the design of BTO/CTO shop floor control system

Ruey-Shun Chen<sup>a</sup>, Kun-Yung Lu<sup>a,b,\*</sup>, Shien-Chiang Yu<sup>a</sup>, Hong-Wei Tzeng<sup>a</sup>, C.C. Chang<sup>a</sup>

<sup>a</sup>Institute of Information Management, National Chiao Tung University, 1001 Ta Hsueh Road, Hsin-Chu, Taiwan, ROC <sup>b</sup>National Lien-Ho Institute of Technology, 1 Lien Kung, Kung-Ching Li, Miao-Li, Taiwan, ROC

## Abstract

Although computerized information systems are conventionally used to control production, applying a manual approach and improper logistical assignments typically reduces operating efficiency and increases customer service response time. Satisfying the requirements of remaining competitiveness in the current marketplace, such as offering build-to-order (BTO) or configuration-to-order (CTO) services is difficult. This study presents an integrated information system for use in shop floor controlling systems (SFCS) for kitting parts, producing goods, packing finished goods and distributing them, to enhance the performance of the BTO/CTO production system. Several information technologies and devices, such as barcode system, the electronic pick-to-light picking system, electronic Kanban (eKanban), and others are adopted to support the relevant logistics. A personal computer (PC) manufacturer is used to demonstrate the proposed system. The findings of the study reveal that the proposed information system can respond to the status of the production line in real time. This responsiveness can help the production controller to make a suitable decision and quickly meet the requirements of the BTO/CTO production system. <sup>#</sup> 2003 Elsevier Science B.V. All rights reserved.

Keywords: BTO/CTO; Shop floor control system; Reengineering; Just-in-time/kanban; Warehousing; Logistics

## 1. Introduction

The globalization and strong competition in current marketplaces have forced companies to change their ways of doing business. Shocked by the shortening life cycle of information technology products, many Taiwanese PC manufacturers have been compelled to alter their production strategy from build-to-forecast (BTF) to BTO or CTO to reduce inventories and obtain a beneficial position in a global supply chain [17]. However, the limitations of short lead times, many product types and small lot sizes of orders have raised serious control and logistics problems in BTO/CTO production systems.

Presently, high productivity and a quick response to customers are essential for most producers [18]. Reducing the processing time and inventories are objectives in managing production systems. Although computerized information systems are typically used to control production, applying a manual approach and assigning improper logistics normally reduce operating efficiency and increase customer service response time. The common problems are that the information flow and material flow are separated, production messages are not transferred in real time, and working states are governed visually but do not depend on the exchange of information, among others. Furthermore, these information systems are typically designed for a BTF system but not for BTO/CTO systems.

Following the successful implementation of just-intime (JIT) systems by many Japanese manufacturers beginning in the 1950s, JIT began to attract the interest of the professional and popular press in North America during the 1980s [19]. According to related studies [3,7], JIT production systems are associated with greater plant productivity, improved processes and products, lower costs, and higher profits. The key success factor of a JIT system is that all production actions are triggered by the demands of customers (pull-type production). This situation is similar to that of demands on the BTO/CTO system. This study presents an integrated information system for shop floor control to simulate a JIT production system and smoothly operate it according to BTO/CTO strategies. Several information technologies and devices, including the barcode system, electronic pick-to-light picking system, electronic Kanban (eKanban), and others are adopted to support the relevant logistics. A PC manufacturer is considered to demonstrate the proposed system. The findings of this study case reveal that the proposed information system can respond to the status of the production line in real time. The system can help the production controller to make a suitable decision and respond to the working status in real-time.

The rest of this paper is organized as follows: Section 2 describes related problems. Section 3 outlines the framework of the proposed system. Section 4 describes the implementation and evaluation of the proposed system. Finally, Section 5 draws conclusions.

## 2. Problem statements

Based on the studies of Olhager and O<sup>¨</sup> stlund [15], the manufacturing continuum can be classified as Make-to-Stock, Assemble-to-Stock, Make-to-Order and Engineer-to-Order. These researchers indicated that the bottleneck in the production network is the critical decision point at which the production system is chosen. Their study claimed that the BTF is similar to the Make-to-Stock and Assemble-to-Stock; BTO is similar to Make-to-Order; and CTO is similar to Engineer-to-Stock. Many Taiwanese manufacturers are compelled to employ BTO/CTO production systems to meet quickly the diverse demands of customers. However, such a type of production system relies strongly on the tight integration of the upstream supplier of parts, the midstream manufacturer and assembler of components, and the downstream distributor of finished goods in the supply chain [4]. In this system, the shop floor control mechanism of the middle manufacturer critically determines the performance of the supply chain.

According to the classification of the studied case, the CTO production system for PC computers can be divided into five layers.

\- CTO1: This type is employed to assemble optional hardware parts, including CPU, memory, hard disk, and others. It is a fundamental form of BTO.

\- CTO2: This type integrates the components of CTO1 with some items of third party, such as the network system.

\- CTO3: This type integrates the components of CTO1 and/or CTO2 with some application programs, including Microsoft Office, Oracle Database, and others. The distributor can sometimes provide these services.

\- CTO4: This is a special case of which a product involving an enterprise application system, such as accounting application systems.

\- CTO5: This is the most complex way of meeting individual customer orders.

The customer orders in the case study are normally composed of the five layers mentioned above. The many product types and small lot sizes of an order produced in BTO/CTO systems represent a challenge to the production controller in controlling shop floor control [16].

In previous decades, many well-known studies elucidate the core elements of the shop floor control problem. Melnyk and Ragate focused on the information system required to maintain and exchange information between the work order (WO) and the work center [14]. They suggested that the effective control mechanism must include order review and release, detailed scheduling, data collection and monitoring, emergency control and feedback, and order disposition [13]. Its main functions were to determine the priority of WO, transfer messages regarding work-inprocess (WIP) and WO to the material requirement planning (MRP) layer, and supply the real-time information concerning the work center to the capacity planning layer. The key control element was the order review and release function to adjust the schedules and routes of the work order.

Daniel and Robert [6] emphasized the five functions of (1) WO reception—shifting the WO generated from the MRP into the shop floor control system; (2) capacity review—checking the available resources including stocks of materials, parts and WIP, and projected available capacity; (3) scheduling—assigning the priority of the job orders (JO) according to pre-defined schedule; (4) monitoring—following up the status of WO, WIP and out-sourcing, and (5) updating—feeding back the current messages of work centers, such as lead time, load, yield rate, and others, to the MRP layer. This system is similar to that of Melnyk and Ragate.

The system proposed by Bauer emphasized the function of factory coordination [2]. The system consisted of two parts—production environment and production control. The former was involved in program scheduling, dispatching, and monitoring. The latter controlled the information flow of material’s moving and production.

Although the SFCSs mentioned above were successfully installed into a practical pilot system, they were designed for the BTF system and based on the logic of MRP which relates to a pushing production strategy. The successful operation of this control strategy relied greatly on the assumption of actual production parameters, including fixed lead times, optimal lot sizes, and others. However, practically, especially in the job–shop environment, actual lead times and optimal lot sizes are neither known nor fixed [10]. Small changes in parameters at the final assembly level frequently cause large changes on earlier production levels. The uncertainty of production and operations, especially in an environment of many product types and small lot sizes in a computer production system, is difficult to cope with.

In summary, some difficult issues, listed further, are involved in conventional SFCS. These issues are the main motivations of this paper, which seeks to contribute to real-time production control systems.

\- The difficulty of quickly transferring production messages.

\- Costs increased by ineffective logistics (for example, of parts picking, WIP moving).

\- Inability to respond quickly to emergencies or a rushed order.

\- Ineffective information system (in manual and duplicate processing).

## 3. Demand analysis and system design

The case study, Acer Co. Ltd., is a large manufacturer of PC products in Taiwan. The manufacturer is an important OEM partner of many globally famous computer brands. Fig. 1 illustrates the main manufacturing processes. These processes can be divided into four stages. They are (1) preparation—pick parts, label lot no. on the parts, and deliver them to the corresponding assembly lines, according to the BOM of the relevant WO; (2) assembly—assemble the relevant parts and components into end products, according to the specifications; (3) testing—perform the pre-run-in and function tests, and install the system and application program software to meet customer’s requirement, and (4) packing and shipping—gather the end products and the components into cartons and ship them to the places stated on the packing lists.

Given the massive and quite diverse demand for, and the short lead time of, PC products, customers’ orders normally composed of several levels of CTO and BTO; much manpower is required to support the logistics, including picking parts, printing production documents, arranging the line, and collecting data in conventional BTF information systems. However, the case company adopts the push-type MRP logic to control the production system. The information system is designed for use in batch type and off-line process. These ineffective processes usually raise some problems of operation, management, and distribution as given further.

\- The method of pre-printing the label is not suitable for the production of many species and small lot sizes.

\- It is no enough times to prepare the testing program and customized software in fast changing production model.

\- It significantly lowers the performance of production by using the BTF control strategy to meet the requirements of BTO/CTO.

\- How to quickly and accurately prepare the parts and documents for assembly?

![](/api/attachments/TCQXWG8W/fulltext/images/de30cf652892125c0fcf0fe90d7ddb6980bb86fa0abcd15a8910dc71232c83e8.jpg)  
Fig. 1. The manufacturing processes of PC.

\- How to support the high turn over rate of finished goods inventory management in out-bound logistics?

## 3.1. Descriptions of proposed framework

This study presents an integrated information system (Fig. 2) used in shop floor control to enhance production and logistics and thus solve the aforementioned problems and satisfy the requirements of a BTO/CTO production strategy. The proposed systems are divided into four parts, which include several subfunctions, as shown in Fig. 3.

\- Pre-processing system: this part pre-processes the WO schedules received from the MPS (master production scheduling) system. The embedded scheduling and routing mechanisms coded by genetic algorithms (GA) can automatically arrange the optimal detailed schedules for WO, and the optimal picking routes, as new job orders are received. This information, including the time bucket, the routes, the quantity, and other data, are stored in the database to support the on-line logistics. The system can also automatically inform the purchasing mechanism to replenish the parts while the control point reaches the re-order point.

\- Kitting system: this part prints the relevant picking documents and specifies an optimal path for guiding the picker to select better picking sequences.

\- Production information system: this part dispatches the WOs, collects the production messages, monitors the working status, and provides real-time production information reports.

\- Out-bound logistics system: this part provides detailed information on packing the optional components and printing the relevant shipping documents.

## 3.2. System design

## 3.2.1. Pre-processing system

A genetic algorithm (GA) LibGA, coded in C language was employed herein to generate automatically the optimal detailed schedules and the picking routes [5]. Holland initially introduced GAs as a global search technique [9]. GAs explores the solution space by applying concepts taken from natural genetics

![](/api/attachments/TCQXWG8W/fulltext/images/aaeda6541ce1a33cb86de6f9e9f336f05b7c7a5c021d8aaa3f272b04e5f65b99.jpg)  
Fig. 2. The framework of the proposed systems.

and evolution theory. During the search, candidate solutions in the solution space are encoded as symbolic strings, known as chromosomes. According to the basic operators of the GAs—selection, crossover, mutation and reproduction—the search algorithm analyzes and extracts continually improved information from the search space, and guides the search in a pre-defined direction.

![](/api/attachments/TCQXWG8W/fulltext/images/cf5b73b6c62b1a21f2801038afa9d0f2bbac861d372883b255d7a8a476144c76.jpg)  
Fig. 3. The functions of the proposed systems.

![](/api/attachments/TCQXWG8W/fulltext/images/84520980edbbfd8b67deebe62dd14454e199c4677517e22806d3c44981c476b7.jpg)  
Fig. 4. The demonstration of kitting operations.

While the SFCS receives the job order (JO) transferred from the MPS system, the LibGA automatically transforms the JO into a piece of WOs and generates detailed schedules based on available resources. These WOs will be sent to the corresponding stations in the form of eKanban. The system can also automatically arrange the optimal picking routes according to the relationships between part location and the BOM used in the corresponding WOs. Meanwhile, the system concurrently checks the stock level of the parts used in the corresponding WOs. The system automatically triggers the purchasing mechanism to replenish the stock of parts as the control point reaches the re-order point.

## 3.2.2. Kitting system

The kitting system is a buffer system designed to accelerate the picking and reduce the error rates when picking parts. Owing to the peculiarly diverse demands in the BTO/CTO production system, one

WO may include several types of products/components. This system employs a batch picking strategy that allows several WOs to be combined as a picking batch, to improve the picking. When the picking tasks are completed, the relevant parts are labeled with the number of the corresponding WO and placed on the assigned shelf of the kitting warehouse. Fig. 4 shows the layout and operation of the kitting system.

The picking system includes two sub-systems—online printing and electronic pick-to-light. The on-line printing system prints picking lists, working labels, packing labels, and other documents. The barcode system is used to label tasks and contents to enable quick exchange and accurate collection of information. The traditional (one-dimensional (1D)) barcode only identifies the number of the WO. In the case that a message must be displayed, a two-dimensional (2D) barcode system, PDF417 [11] is used here. Fig. 5 presents an example of a 2D barcode for designating a WO.

<table><tr><td>Job No:</td><td>#3148</td><td>Part No:</td><td>21-21486-1</td><td>Qty:</td><td>1500pcs</td></tr><tr><td>WC-fm:</td><td colspan="2">103</td><td>WC-to:</td><td colspan="2">213</td></tr><tr><td>ST-early:</td><td colspan="2">2001/11/9, AM 10:00</td><td>ST-late:</td><td colspan="2">2001/11/9, AM 10:15</td></tr><tr><td>Controller:</td><td colspan="2">#2114</td><td>2D Barcode</td><td colspan="2"></td></tr></table>

Fig. 5. An example of 2D Barcode of WO.

![](/api/attachments/TCQXWG8W/fulltext/images/2dd6cab5caf3c8df3efed766a0fd8322467cf7fdf8aa6a5fff26b7d41851e096.jpg)  
Fig. 6. The structures of ABLEPICK.

The main benefits of applying the 2D barcode system are that one piece of 2D barcode can contain more messages than 1D does, and that the 2D barcode can continuously transfer the information to the next station while the network system being interrupted.

The electronic pick-to-light system guides pickers quickly and accurately to the locations of the picked parts. The system automatically lights up and displays messages that state the picking sequences, WO no. and quantity, while a picking task is performed. This capacity effectively improves the performance and reduces the error of the picking tasks. ABLEPICK, a Q-Way pick-to-light system, is adopted in the case study. Fig. 6 depicts the structures of ABLEPICK. The ABLEPICK applies the RS485 and the SDLC protocol to communicating data between database and parts location. The system is flexible, scalable, support long distance communication, and has many connecting points (1 PC can control 160,000 units).

## 3.2.3. Production information system

The information generated in the preceding two stages, concerning detailed schedules, WO no., the series no. of product label, and other BOMs, is stored in backend databases. When the assembly controller (agent or supervisor) receives notification of production, the production information system (PIS) integrates this information with the eSOP (electronic standard operation procedure, offered by the industrial engineering department, IE) to generate a configuration table to guide the assembly operations. The Lan/Pre-load system (a sub-system of PIS) automatically unloads the testing program and the application software (provided by the test engineering department, TE) from the file server to the testing stations.

Barcode-reading systems are established in the loading and unloading stations of every assembly line. Such a system is a basic element of a flow control system (FCS). The barcode reader can automatically scan the label pasted on a working component to verify the accuracy of the parts inputs to the loading station and monitor the speed of assembly in the unloading station. The information collected by the loading station and the testing station is transferred into the daily production database and printed as a daily production report. This information can be used in performance analysis and control.

While finishing the test tasks in the assembly line, the finished goods are mounted on a pallet and the series no. of the pallet is input to the PIS to locate the stock. Then, this information, including sales order no., WO and pallet series no., is transferred to the database of out-bound logistics system. The inventory control system changes the control status from a WIP to a stock of finished goods, and then closes this WO.

## 3.2.4. Out-bound logistics system

This system consists of three sub-systems—storing, picking and shipping—and is controlled by an RF (radio frequency) controller. Fig. 7 depicts the structure of the out-bound logistics control system. When storing finished goods, the warehouse controller must input the relevant pallet no. to the logistics control system via the RF devices. Then, the AS/RS (automatic store/receive system) system will automatically store the pallet to the assigned locations of the warehouse.

During the shipping stage, the logistics control system prints out a 2D barcode type of picking list, and guides the AS/RS system to unload the assigned pallets. The picked pallets are gathered in the staging area. The shipping operator must verify the packing contents using a hand-held barcode reader, before loading the packs onto trucks. This confirmatory information will be returned to the ERP system to close the corresponding job orders and working orders. The complexity of the BTO/CTO production system is such that a packing error can easily be made during the shipping stage. Applying the 2D barcode system can help an operator to verify the packing contents.

![](/api/attachments/TCQXWG8W/fulltext/images/fd848d20f6da7657f0b70d83b6c80f8b32155234e22fbde622fa4c9b9e72a101.jpg)  
Fig. 7. The structure of the out-bound logistics control system.

## 4. Implementations

## 4.1. Information infrastructure

This study constructs the information infrastructure of the SFCS as a client–server structure under an Internet/Intranet network system to generate a realtime information transaction environment. Fig. 8 depicts the architecture of the proposed approach. The architecture consists of three layers—the presentation layer to display the relevant working assignments and print the required documents; the application layer to provide services and system control, and the data layer to provide enterprise resources and the job orders. Section 3 describes the main components of the SFCS.

## 4.2. System developing environment

The development environment of the SFCS is described as given further.

\- OS: server: NT5.0, client: Win98.

\- Database: Oracle 8i.

\- Application program: VB 6.0 used for AP, Delphi 5.0 used for RF control interface program, Cþþ used for genetic algorithms, and SQL used for database transactions.

\- 1D and 2D barcode systems are employed to identify the relevant working orders and parts. Barcodereading devices are used to collect data automatically.

\- ABLEPICK pick-to-light system is used to pick parts. RF control system is used to guide and search among finished goods.

## 4.3. System operations

The proposed system simulates the SFCS as a JIT production control system with a pulling strategy. When a customer order is received from the Internet or a conventional channel, the ERP system (not described here) automatically generates a corresponding job order and transfers it to the SFCS. Then, the SFCS transforms the job order into working orders (WOs), which it issues to the pre-assigned stations (via the Intranet system) in eKanban. The manufacturing processes are initiated in the pre-processing stage; the corresponding working labels are printed, and the required parts prepared. While the assembly, testing, and packing procedures proceed, the material and informational flows are tied by identifying labels so that the production status can be recorded in real-time using a barcode-reading system, which is also a supplementary monitoring system. Collection devices, such as barcode readers, pick-to-light picking devices, RF controllers, and others, automatically collect the production information, significantly improving the performance and accuracy of the data transactions. Fig. 9 depicts the data flow of the proposed system.

![](/api/attachments/TCQXWG8W/fulltext/images/01996df4951bf2b5b3f298b9636e7f5b4b0af0186fce4ca181cd7951af219a5b.jpg)  
Fig. 8. The information infrastructures of the proposed system.

## 4.4. System installation and performance evaluation

The production manager accepts the authors’ suggestions that the study case should be divided into four phases to smoothly transform the proposed SFCS controlling system into a BTO/CTO system, because the primary production control system is of the BTF type.

\- Primary phase: reserve the primary control method to collect the detailed production data for future comparison.

\- Pilot phase: pre-test the proposed system with minor assembly changes.

\- Modify phase: modify the production line to the BTO/CTO type and apply the parallel testing strategy to launch the proposed control system.

\- Formal running phase: regularly perform the proposed control system.

Four months of hard work were spent to pilot test the proposed system and realize major changes in the production line to fit it to the BTO/CTO type. The new control system worked successfully. Following 6 months of observation, the production manager was satisfied with the control. Daily production reports and the authors’ observations of the pilot system established that the proposed approach was superior to the conventional BTF control strategy.

The following criteria were applied to compare the performance of the BTF and BTO/CTO systems.

\- Throughput time in hours.

\- Shipment hit rate as a percentage.

\- Productivity in man–hours per unit.

\- Quality failure rate in FQC.

![](/api/attachments/TCQXWG8W/fulltext/images/ba49cf4e07c5cfd1403af408428d1cdcde5427b1210712e5a5192689a530cf28.jpg)  
Fig. 9. The diagram of data flow of the proposed system.

![](/api/attachments/TCQXWG8W/fulltext/images/4d7d4173ed0cdbdeae2c1362026eccb4e4c66031a3aa989de7360b1da33f4abb.jpg)  
Fig. 10. The comparison effects in four phases (1).

![](/api/attachments/TCQXWG8W/fulltext/images/d3d6dea9c9583945d06627e10822704a88cab039030e652b9772c7b1f93668a4.jpg)  
Fig. 11. The comparison effects in four phases (2).

\- Required production space in m<sup>2</sup>.

\- Capacity in units per hour.

Figs. 10 and 11 compare the results generated from the four phases of the systems. The comparisons reveal that the total production performance was significantly improved in the fourth phase. The throughput time was reduced from 36.8 to 7.8 h (79% decrease); the shipment hit rate increased from 40 to 95% (138% increase); the productivity (man–hours per unit)) increased from 2.1 to 0.8 (62% increase); the quality failure rate was reduced from 20 to 1% (95% decrease);

Comparison of business processes between two different strategies

<table><tr><td>Items</td><td>Primary strategy (BTF)</td><td>Proposed strategy (BTO/CTO)</td></tr><tr><td>Label Printing</td><td>Off line</td><td>On line</td></tr><tr><td>Parts shortage</td><td>Inspection by human</td><td>On-line display by electronic pick-to-light system</td></tr><tr><td>Parts picking</td><td>Search by human</td><td>Automatic guide by pick-to-light system</td></tr><tr><td>SOP documents</td><td>Paper type</td><td>Electronic type, on-line printing</td></tr><tr><td>Testing program</td><td>Loading by disk, test by human</td><td>Automatic load from network and test</td></tr><tr><td>Production control</td><td>Collecting production data by manual</td><td>Real-time holding the production status based on barcode-reading system</td></tr><tr><td>Finished goods (FG) storage</td><td>FG store &amp; data transaction by manual</td><td>FG store by AS/RS system, on-line data transaction</td></tr><tr><td>FG retrieving</td><td>Search by human</td><td>Automatic retrieve by AS/RS system based on the packing list</td></tr><tr><td>Shipping</td><td>Off line printing the shipping label, data key-in by manual</td><td>On-line printing the shipping label, automatic data transaction</td></tr></table>

the production space was reduced from 2300 to 1560 $\mathrm { m } ^ { 2 }$ (32% (reduction OR saved)); and the capacity was increased from 150 to 350 units/h (133% increase).

In summary, the overall manufacturing process was improved by the application of new information technology. Table 1 presents the differences of business processes between the strategies of BTF and BTO/CTO.

## 5. Discussions and conclusions

This study has presented an integrated information technology in the shop floor control system for use in a BTO/CTO production system. A information-control system, combined with several information technologies, including a barcode system, electronic pick-tolight picking system, eKanban, and others, is developed and suggested to control a production system with many product types and small lot sizes. A PC manufacturer is considered to demonstrate the proposed system. The findings of the study reveal that the proposed information system can significantly improve the performance of the production system and respond to the status of the production line in real time, helping the production controller to make a suitable decision and be aware of the work status just-in-time. Importantly, the proposed system can immediately respond to the customer, using the BTO/CTO production system.

Computerized information systems have been proven to be effective in controlling production systems [1,12]. However, a traditional, manual information system cannot meet the requirements of a quickresponse environment. Such a system depends on other supplementary devices to facilitate the automation of data transactions. The data retrieval devices used in this study increase not only the efficiency of data transaction but also the accuracy of information. Besides, applying appropriate business process reengineering (BPR) is another key success factor [8]. For example, applying superior manufacturing practices in the form of JIT and continuous process improvements (CPI) strengthen companies on the Pacific Rim where fewer natural resources are available than in other parts of the world [7]. Indeed, combining IT with a BPR strategy represents a main trend to increase competitiveness in the current marketplace.

## Acknowledgements

The authors would like to thank Dr. E.H. Sibley, and anonymous referees whose insights improved the content of the manuscript.

## References

[1] T.J. Andersen, A.H. Segars, The Impact of IT on decision structure and firm performance: evidence from the textile and apparel industry, Information and Management 39, 2001, pp. 85–100.

[2] A. Bauer, Shop Floor Control: From Design to Implementation, Champan & Hall, New York, 1991.

[3] W.C. Benton, H. Shin, Manufacturing planning and control: the evolution of MRP and JIT integration, European Journal of Operational Research 110, 1998, pp. 411–440.

[4] S.W. Changchien, H.Y. Shen, Supply chain reengineering using a core process analysis matrix and object-oriented simulation, Information and Management 39, 2002, pp. 345– 358.

[5] A.L. Corcoran, R.L. Wainwright, LibGa: source codes and technical notes, Department of Mathematical and Computer Sciences, The University of Tulsa, 1993.

[6] S. Daniel, L.B. Robert, Production: planning, control, and integration, McGraw-Hill, New York, 1997.

[7] R.R. Fullerton, C.S. McWatters, The production performance benefits from JIT implementation, Journal of Operations Management 19, 2001, pp. 81–96.

[8] V. Grover, J. Teng, A.H. Segars, K. Fiedler, The influence of information technology diffusion and business change on perceived productivity: the IS executive’s perspective, Information and Management 34, 1998, pp. 141–159.

[9] J.H. Holland, Adaptation in Natural and Artificial Systems, Ann Arbor, MI, The University of Michigan Press, 1975.

[10] Z. Huq, F. Huq, Embedding JIT in MRP: the case of job shops, Journal of Manufacturing Systems 13 (3), 1994, pp. 153–164.

[11] M. Marriott, PDF417 portable data files, Sensor Review 15 (1), 1995, pp. 33–35.

[12] K.N. McKay, J.A. Buzacott, The application of computerized production control system in job shop environments, Computers in Industry 42, 2000, pp. 79–97.

[13] S.A. Melnyk, P.L. Carter, Production Activity Control, Homewood, IL, Business One Irwin, 1987.

[14] S.A. Melnyk, G.L. Ragate, Order review/release: research issue and perspectives, International Journal of Production Research 27, 1989, pp. 1081–1096.

[15] J. Olhager, B. O<sup>¨</sup> stlund, An integrated push-pull manufacturing strategy, European Journal of Operational Research 45, 1990, pp. 135–142.

[16] P.J.P. Slater, Pconfig: a web-based configuration tool for Configure-To-Order Products, Knowledge-Based Systems 12, 1999, pp. 223–230.

[17] S.S. Wang, The Impact of BTO and Adaptation in Taiwan Information Business, Marketing Reports, CETRA Publications, Taiwan, 1998.

[18] J.D. Wells, W.L. Fuerst, J. Choobineh, Managing information technology (IT) for one-to-one customer interaction, Information and Management 35, 1999, pp. 53–62.

[19] R.E. White, J.N. Pearson, J.R. Wilson, JIT manufacturing: a survey of implementations in small and large US manufacturers, Management Science 45 (1), 1999, pp. 1–15.

![](/api/attachments/TCQXWG8W/fulltext/images/b3d7c0524b57eb43d346f05589b7b7d75412cd0a3261046264c8e5380ead8bd7.jpg)  
Shien-Chiang Yu is a candidate for doctorate degree in the Institute of Information Management at National Chiao-Tung University. His research interests are that spatial database, electronic commerce, information retrieval and metadata.

![](/api/attachments/TCQXWG8W/fulltext/images/58884bcd7491fa2c38d1c7e27e29decb67b93839d22b4789eafe8dc8935f883a.jpg)  
Ruey-Shun Chen is an associate professor in the Institute of Information Management at National Chiao-Tung University, Taiwan. He received his PhD from the Department of Computer Science and Information Engineering, National Chiao-Tung University. His research interests are that genetic algorithm, relia bility, performance evaluation, business networks and distributed systems.

![](/api/attachments/TCQXWG8W/fulltext/images/509fadec46e3976eb6a8529bbdc806a852acd18c8e156d17843d2cb329282067.jpg)  
Hong-Wei Tzeng received his MS degree in 2001 with major in information management from National Chiao-Tung University. His research interests are that production control system, database management and electronic commerce.

![](/api/attachments/TCQXWG8W/fulltext/images/8844529bce2689f11b192cb6f1877d72b9ad2e9e09bae75b0e42be9ff346f43a.jpg)  
Kun-Yung Lu is a candidate for doctorate degree in the Institute of Information Management at National Chiao-Tung University. He is also a lecturer of National Lien-Ho Institute of Technology in computer science. His research interests are that production information system, product data management, optimization, and artificial intelligence.

![](/api/attachments/TCQXWG8W/fulltext/images/f3ad6f34d32a7397395c2a6e61a7e6920ee5a6dd726f8201ed97ca223c3f10dd.jpg)  
C.C. Chang is a student of doctorate degree in the Institute of Information Management at National Chiao-Tung University. His research interests are that enterprise information system, internet security control, optimization, and artificial intelligence.
