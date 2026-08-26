---
otero_id: 18772
otero_key: "TSRTJ2XH"
title: "Information as inventory"
authors: "Boaz Ronen; Israel Spiegler"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90069-e"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
gement Systems, Artificial Intelligence, Information Systems Analysis and Design, and Human Machine Interface, areas in which he published extensively.

SOS

# Information as inventory A new conceptual view

Boaz Ronen and Israel Spiegler \*

Faculty of Management, The Leon Recanati Graduate School of Business Administration, Tel Aviv University, Tel Aviv 69978, Israel

A new approach to viewing and handling information in the organization is presented. Information is treated as inventory in its three stages: raw materials (data to be processed), work in process (data being converted into information), and finished goods (information being stored). In line with modern inventory management methods, such as Just In Time, we introduce the concept of Information In Process (IIP). We show that IIP is costly, hard to control, and hinders the decision-making ability of those for whom information is gathered and processed in the first place – the users. Mismanaging the information resource by stocking IIP is suggested to be a cause of many system failures and malfunctions as is the case with production systems accumulating inventories. A methodology for applying inventory control techniques to the area of information systems is outlined aiming at the reduction of IIP.

Keywords: Database, OPT, Management by constraints, Work-in-Process, Inventory control, Just In Time, Data integrity.

![](/api/attachments/TSRTJ2XH/fulltext/images/731e736bd71f7514e587b49cc0121416d2f3711a6e49529a107ab5a66774c961.jpg)

Boaz Ronen is a senior lecturer at Tel Aviv University, Faculty of Management. He holds a B.Sc in electronics engineering from Technion, Haifa and an M.Sc and Ph.D from Tel Aviv University, The Leon Recanati Graduate School of business Administration. He was a visiting professor at New York University, the Stern School of Business, Information Systems Area, and in Columbia University, Graduate Business School with the Operations Management Area. Prior to his academic career he worked for ten years in the hi-tech electronics industry. His main research, teaching and consulting areas are information economics, MIS in operations management, as well as the implementation of JIT, TQM and TOC in service and industrial organizations. His papers were published in journals such as CACM, Operations Research, Decision Sciences, Datamation, and Production and Inventory Management.

Visiting Associate Professor, Information Science, The Claremont Graduate School, Claremont, CA 91711, USA. This work was supported in part by the Marcel and Annie Adams Institute of Management Information System, Tel Aviv University.

## Introduction

The past decade and a half of developments in MIS has seen many papers extolling the virtues of information produced from new database storage technology and techniques. Phrases such as “information is power” and “data is a key resource” became common slogans in such publications. Those are aimed at promoting and encouraging the use of the new techniques and ideas to better manage the organization’s ever-growing bases of information.

But in the midst of the euphoria surrounding these new developments in data and information storage, we are beginning to sense some dissatisfaction and problems. Despite the large databases and vast “information” content, we find managers spurning the firm’s data processing function and seeking refuge in the comfort of their own personal databases which indeed support their immediate decision-making needs. Thus, information, particularly the abundance of it, can be a hindrance, a bewildering and costly venture, and even a deterrent to the organization’s decision makers.

Taking a different view of something we are familiar with is one way of gaining new insight into a problematic situation. This is certainly the case of information due to its abstract and intangible nature. We suggest that information, as a resource, should be viewed and treated as inventory, in line with modern production and manufacturing concepts. Such a view of information is, in fact, consistent with the original analogy of data processing and production management, whereby both are seen as having the phases of input, processing, and output (see Ronen and Palley, 1987). The idea is to use the newer inventory management techniques and concepts such as cutting lead time, using small lots, Drum-Buffer Rope (DBR), Optimized Production Technology (OPT), Just In Time (JIT), and Management By Constraints (MBC), and apply them to the information system area. Those techniques have been practiced in a large number of plants all over the US, Japan and Western Europe (Schonberger, 1986, Goldratt, 1986, Ronen and Starr, 1989) and applied recently also to service organizations (Feather and Cross, 1988, Eden and Ronen, 1989) and to office automation (Floyd and Ronen, 1989).

![](/api/attachments/TSRTJ2XH/fulltext/images/fb90e710599470c135d929643bcf4b79ecf03a60f1fec75f364116e008962336.jpg)

We claim that those operations management concepts have their parallels and can be applied to the information system area. For example, lead and cycle time refer to the time that elapses between placement of an order and the actual delivery of the finished goods. This concept is directly related to the timeliness aspect of information systems discussed by Ahituv and Neumann (1986). If too much time elapses between the event which triggers the data flow and the actual receipt of information by the manager, the data may turn to be useless. Or, if the time between recording the information and reporting it to management is long, the “time window” for action may have expired.

Granted, the manufacturing analogy has its limitations. Raw material is difficult and expensive to duplicate whereas data can be copied many times without too much effort. But this makes our case even stronger. Since information is elusive, it is easily polluted and over collected, processed, and duplicated. Viewing it as inventory may help contain some of the problems such a practice may cause.

If information is to be treated as inventory, then having too much of it may be as bad as having too little, and in some cases even worse. But while the manufacturing world increasingly realizes that large inventories and Work In Process (WIP) are costly evils to the organization, the MIS world continues to accumulate more and more data, viewing the database as a bottomless repository of facts. And the exponentially growing databases inevitably increase the demand for newer storage technologies and media. In short, Information In Process (IIP) not only costs money but may inhibit and at times disrupt the purpose for which it was produced in the first place – managerial decision making.

The benefits of taking a new approach to information will bring about the introduction of inventory management concepts to be added to the data administration function of the organization. The Data Base Administrator (DBA), often called the data custodian of the firm, will indeed begin to treat information as a resource. Among such benefits is to outline a methodology and a set of evaluation measures by which the organization can make intelligent decisions on the issue of “to store or not to store”, that is, to determine whether new facts are to enter the database or be kept out.

The paper surveys some of the ills and problems of WIP. We present ideas which are the basis for a methodology of information as inventory. A summary of the managerial and organizational implications of the proposed methodology is given together with directions for further study and research.

## The Ills of Work in Process

It has been shown over and over again (Schonberger, 1982, 1986, Goldratt and Fox, 1986, Suzuki, 1987) that work in process is the cause of many problems and evils in the production of physical goods in the modern factory. Among the problems are longer cycle times, waist in the use of labor and materials, loss of production control, slow response to engineering changes, expensive holding costs, and maintenance difficulties. All these cost money, bring down the quality of products, and result in longer lead times. Thus, the cumulative monetary value of holding inventories may exceed 50% of the overall cost of materials manufactured annually. Obviously, these increases in production costs arising from the “unproductive” factors mentioned above increase considerably the overall manufacturing cost, which in turn affects the firm's competitiveness in the market. In an environment where the need is for better quality, shorter time to market, and low cost, high WIP may result in losses and even shutdown of plants and companies.

Several methods have been used to tackle the WIP problem. These are surveyed by Ronen and Pass, 1989, and are briefly mentioned here. Perhaps the better known today, stemming from the Japanese production methods is the Just In Time (JIT). This method comes in two forms: a philosophy and strategy, and a scheduling and control mechanism (Ronen and Starr, 1989). The strategy, or the large JIT, contains three parts: Total Quality Control, Total Preventive Maintenance, and JIT production principles. The first part requires the direct involvement and responsibility of employees for the quality of the product they produce. The second draws up principles for better maintenance policy. The third part deals with waste avoidance, problem solving, reduction of WIP, and increasing throughput rate. For more information the reader is referred to Schonberger (1986).

Suzaki (1987) emphasizes the JIT aspect of eliminating waste. He relates to the Japanese “seven wastes” which result from: overproduction, waiting time, transportation, processing, inventory, motion, and product defects. Overproduction, for example, was found by Toyota to be one of the worst forms of waste commonly found in factories. By producing goods over and above the amount required by the market, and by getting too far ahead of the work flow, raw materials are consumed, wages are paid and resources are operated unnecessarily, sometimes at the expense of work that is needed. This gives rise to what is known in industry as the “40-20-40” syndrome: 40% of the work is done ahead of time, 20% done in time, and 40% of the work is overdue. Moreover, overproduction waste requires additional handling of materials, additional space to hold inventories and so on.

Group Technology (GT) is a deviation from the traditional organization of production by process into an organization by product. That is, lines are dedicated to the production of families of products, each line being equipped with all the machines and facilities needed for the products in question. This simplifies the plant and allows for faster flow and easier control and management (see Burbridge, 1988).

World Class Manufacturing (WCM) is a combination of JIT and GT (Schonberger, 1986, 1987). It aims at keeping things as simple as possible, shortening lead times and improving quality.

Synchronized Manufacturing (SM) focuses on bottlenecks of the shop floor. The idea is to run the plant as a series of buffers in front of bottlenecks by separating the scheduling and deciding on the optimal size of transfer and processing lots. This is the basis for the Optimized Production Technology (OPT) software package (see Lundrigen, 1986).

Management By Constraints (MBC), also known as Theory of Constraints (TOC), is an enhancement of SM and was developed by Goldratt (1985). It focuses on additional constraints of the manufacturing operations such as market situation, components, and raw materials. For more details see Schragenheim and Ronen (1989).

It is about time the information systems and information processing areas begin to look seriously at new avenues which will not only improve the technology of data storage or yield faster retrieval, but also improve the effectiveness of computer-based information. Maintaining a data philosophy that “more is better”, is one reason why many systems do not reach beyond the mundane data processing operations. If data are the raw materials, then information produced from data is the inventory which is the basis for managerial decision making. Our goal can thus be stated clearly: to shorten as much as possible the cycle time that starts from the moment an event triggers a new piece of information, and ends when a managerial decision that relies on that information can be made. One factor that can help achieve that goal is the reduction and elimination, if possible, of information in process. Information in process (IIP), in our view, is basically a negative factor that too often impairs the proper functioning of an information system.

Aside from its actual cost and the associated direct storage and media costs, IIP is a source of other evils:

1. Information in process lengthens the cycle time needed for decision making. That is, decisions made by managers are less responsive to the actual events which they are to affect due to the lag in time needed to search for and process volumes of data. In the manufacturing area it was found, to the surprise of many, that more than 95% of the cycle time parts are in waiting state rather being in a process state. In information processing we expect the proportions to be quite high, though not of the same order as in manufacturing.

2. The quality of the information produced from a voluminous database is likely to be lower since the system must process unneeded or irrelevant facts, instead of concentrating solely on the information it has to produce. Heavy printouts or overloaded screens affect negatively the quality of information and are very often a disadvantage, and even a source of disinformation, to decision makers. We refer to two types of quality errors: (1) low quality information such as wrong or outdated information given to the decision maker due to an overloaded database; and (2) wrong or low quality decisions made as a result of the length of time it takes to get the information. The damage to information quality depends on the type of product and on the time it stays in the system. This may be measured in weeks for production of physical parts; days in the food industry; hours in microelectronics; and even minutes in medical or other vital applications (see Ahituv and Neumann, 1986, on the timeliness factor).

3. The “aging” of data is often ignored when the policy is to collect everything. Older facts not only take up storage space but also slow down the system and may in the final analysis adversely affect the information needed.

4. Information system management and control becomes harder the more data and storage media there is to handle. The complexity of the system rises as new data need to be linked to existing data structure, requiring constant effort and decisions regarding the location and access paths which will be needed if and when such data are retrieved in the future.

5. With data for storage growing exponentially, maintenance of the system becomes a problem. This means not only the maintenance of the hardware and software, tuning the database, updating and preserving the integrity of data, but also assigning people to such tasks and basically working with data that may never be accessed.

6. Data entry becomes a problem and is done automatically without any discrimination as to the real or expected value of facts collected. In many organizations entering and storing data concerning a small bolt requires about the same effort as storing the data on a rare and expensive part. Both are treated as a record in the inventory file of the firm.

Only a very small portion of the data so laboriously collected and processed are actually used by decision makers. Most facts are routinely processed by the transaction processing system and then rarely accessed again.

## Contributors to the Evils of IIP

In many organizations the trap of perceived lower storage cost basically postpones or avoids the decision on selecting what goes into the database. The default is usually to accumulate. We claim that this eventually begins to work against the information systems' goals, costs the organization money beyond holding and storage costs, and does a disservice if not harm to the user community which needs timely and accurate information. This may happen because of the use of improper measures, or the misuse of proper ones. Such measure are:

1. Common Use of the Cost per Unit of Data. This is a local measure, showing that the cost of storage per megabyte is dropping. However, the organization is not interested in such local measure. The cost of MIS includes the total storage cost, which is increasing, since IIP increases more rapidly than the decrease in storage cost. Such suboptimization results in higher total costs. The same phenomenon has been detected in the production industry, causing misleading decisions and irrelevant costing (see Goldratt, 1985, Kaplan, 1987).

2. Use of "Efficiency" Measures. It is well known in the production and operations management area that machine utilization and "efficiency" measures result in high WIP, bad quality, and loss of control (see Goldratt, 1985, Ronen and Starr, 1989). Using utilization measures of computer hardware (e.g., CPU, printers, storage media) encourages MIS managers to justify their investments and maximize resource utilization.

3. Costing Methods. Costing methods usually allocate overhead costs to the transaction. This encourages maximizing the transactions in order to reduce “perceived costs”.

4. Justifying the Race for Newer Technology. The rapidly changing information technology is another source of IIP as its users and operators are eager to demonstrate the merits and features of the new technology in storage capacity and processing power.

The key factor to focus on is, therefore, the reduction of IIP. Following are a number of proposed steps and remedies in this direction.

## Remedies

In order to reduce IIP, improve the decision makers' response time and increase the information quality we propose to take a different approach to data collection, storage and processing. The proposed strategy consists of the following components.

## Storing Algorithms, not IIP

Rather than storing data, which quickly becomes IIP, it is preferable to recalculate or reprocess the data that is directly necessary for decision making. Thus, we believe that algorithms, programs, routines, macros and the like should be stored in the system instead of multiple and voluminous data facts. The saving resulting from sparing to store an item of data lies in bypassing the whole data processing cycle of capturing, keying, verifying, correcting, sorting, classifying, storing, updating, integrating, calculating, disseminating, and reporting.

## Using the 80:20 Pareto Rule

The Pareto rule of 80:20 is very pertinent to the area of data storage and usage as it is in other areas of information systems. We assume that about 20% of the data available to an organization are used most of the time, while 80% are hardly used at all.

The $20\%$ of data can be identified by past experience or in a logical manner, to become the actual stored data to support decision making. The rest is of archival value and hence should not be allowed to overload the organization's database.

To illustrate this point consider a bank or a department store. The information system stores every transaction, though most never get used beyond the initial update of the accounting records. While the bank is bound by law to keep records, it may be argued that the unimportant transactions of a department store could be stored according to a randomized sample rather than unselectively and in total. It may be more cost effective for a firm to recollect an item of data when needed, or even pay a penalty for not having certain information, rather than have masses of unneeded facts pollute the database waiting for the rare moment of retrieval.

## Using Relevant Information

Information produced by the transaction processing system affects, at most, the operational levels of the organization. Transaction data are hardly accessed again and are held not because of any expected future need but simply out of inertia or in line with a policy that was never put to a serious test. Managers subscribe to the notion that the medium “is already there” anyway and that storage and operating costs associated with yet another piece of data are insignificant. Yet, they cannot explain why the budget of the information system keeps rising while hardware is going down in price. The answer is simple. The volume of data collected and stored rises at a faster rate then the reduction in the cost or capacity of storage media. This ever-increasing volume brings up the cost of producing “real” information for decision making where most of the information produced hardly used at all.

Taking a different view of information, as we propose here, suggest applying new measurement tools and criteria to information. The new approach must cease looking at the “unit cost” as a standard way of evaluating the cost of information storage and processing and begin to delineate more global measuring techniques. Rather then looking at how many units of data are processed each hour the question should be what is the global contribution of collecting such data to the firm's overall decision making. A printer should not be measured by how many pages it produces per hour but how many relevant pages it generates and who is using them.

## Focusing on the Key Issues

As noted by Ronen and Pass (1989), information systems should focus on the important issues. Such issues include:

a. “A Type” Items. These are the 20% items. For example, MIS and DSS should include information on “A Type” items with regard to the firm’s inventory.

b. Constraints. The key issues may be viewed as constraints. Information on internal constraints such as bottlenecks are by far more important than information on other machines. Bottlenecks are less than 5% of a production area's resources, but still this information may be vital.

c. Critical Items. These are the key items that will support better control and decision making (i.e., critical path in a PERT network)

## Using Excess Capacity rather than Excess IIP

Excess capacity calls for using additional machines to produce items when needed, rather that produce to inventory. The analogy to information systems is clear. A system should be provided with additional processing power rather than have extra IIP. This concept requires a change in work habits and a different approach to information production. The idea is not to purchase more computing; such, without careful planning, may soon become cluttered again. Excess capacity, when used properly, is that which gives fast turnaround response to requested information needed in a hurry.

## Using Information Dimensions Properly

The various dimensions of information were outlined by Ahituv and Neumann (1986). Among them are accuracy, timeliness, detail, and scope. There is a pervasive “culture” of treating information at the lowest level in each dimension. Thus, with regard to accuracy, most detailed data are collected and supplied to the user community in a uniform and standard manner. This may not be needed, except when legal obligations make it imperative. Similarly, timeliness depends on the decision maker who receives the information. Some may not need the most up-to-date status of a transaction. In short, information is hardly a uniform entity; its dimensions should be carefully handled rather than automatically taken at the lowest level.

## Methodology

The methodology proposed here is based on similar methods that have been developed in related areas, mostly in operations and production management systems. They are relevant to the present context, since our basic premise is that information is to be treated as inventory.

The methodology consists of the following six stages:

1. Assess the real cost of storing IIP. This stage requires a careful examination of the cost of IIP by methods similar to those used for evaluating physical goods. That is, the fixed and variable costs of IIP are estimated for all the parameters in the categories of manpower, hardware, and software. There are costs other than those associated with the usual items of disks, terminals, communications link, which are relatively easy to get. Capturing, verifying, maintaining, or disseminating are some examples of costs often overlooked.

2. Assess System's Required Response Time. This stage attempts to outline the responsiveness of the information system with respect to its users and decision makers. This, again, is not uniformly distributed over the user community. For some users a relatively slow response may suffice, while others require a fast response. Those needing a faster response are really the bottleneck of the system and should be served accordingly-by using excess capacity, for example.

3. Assess Required Levels of Accuracy. Similar to response time, the level of accuracy needed by the various users determines the effectiveness of the system. Assessing the required accuracy level will give an indication of the IIP, help reduce it and have the system focus on the relevant information.

4. Identify System Constraint(s). The system's constraint(s) can be any of the following: a user (department or person), hardware (CPU, channel, storage media, I/O device), software (old program, package, routine), or procedure (method of data collection, verification process). Each of the constraints mentioned is associated with some information processed or produced. Such constraints are the bottleneck of the system and should be handled first in any effort to reduce IIP and improve the system's effectiveness.

5. Replace Stored Data with Algorithms. This phase calls for evaluating the firm's data stores in order to determine which data can be discarded or replaced with algorithms or other processing means. There are instances when multiple copies of a file are stored, each reflecting a parametric change. Such copies can be eliminated and the routine that processes the file kept together with the desired changes. When, and if, needed, the original data should be processed again. This will help also in preserving data integrity and consistency. The idea is to store items, if at all, concisely with preference to formulas, aggregations, or even data sampling.

6. Determine Relevant Measures of Performance. Information systems generally lack measures of performance. This may be due to the fact that such systems are conceptual in nature and do not deal with physical things. Since lack of performance measure is a general problem in MIS, we elaborate on this issue and offer some relevant measures.

Goldratt and Fox (1986) proposed three measures of performance for a production system: throughput, inventory, and operating expenses. These are equally relevant as measures of performance of an information system.

Throughput: This is a measure of the relevant output to the user rather than the total number of units that a system produces. In the factory this measures how many units are actually sold or meet a customer's order in terms of dollar value rather than the total units that a machine makes, many of which may go into inventory and never be sold.

Inventory: Raw material or work in process that has to be processed to create the throughput.

Operating Expense: This is a measure of performance which takes into account all the costs of labor, equipment, storage, and other factors that are needed to operate a certain department. It is the cost to convert inventory into throughput. These global costs are compared with the contribution a department makes to the overall profitability of the production line. The analogy to information processing is to measure the various units, i.e., data entry, information center, etc., in terms of their operation cost and contribution to the information they produce. Care has to be taken not to overlook qualitative variables such as information quality or customer support.

Eden and Ronen (1989) propose two additional measures of performance: lead time and quality measures.

Lead Time: This is also called response time and it measures the time taken by the information system to produce a typical throughput unit (e.g., a typical report). The measurement of lead time is important as it is an indication of the responsiveness of the system to its user community. If a report takes days or weeks to produce, and this is not uncommon, then the relevance to a decision maker of the information it contains approaches zero when the report is finally delivered.

The claim that overabundance of information/inventory makes for a decrease in lead time and responsiveness of the system has to be tested empirically but at this stage we propose it as an intuitive hypothesis.

Quality: This is a measure of the value of the data stored in terms of their quality and not mere quantity. Each unit in the organization should define its quality measure of information stored and produced. For instance, error ratio can be a measure of the data collection function; the integrity of data should be a measure of the data base administration function in the organization; the accuracy of the reports and their timeliness can be the measure of the output of an information system.

These measures of performance can be further broken down into specific criteria which may in turn be applied to various functions in the organization for evaluation. List of criteria and the score given by users and system people are suggested as a tool and method for testing one important and crucial factor that relates to information as inventory: to store or not to store.

Such measures are global in nature and give an overall picture of the status of information use in a typical organization. In a sense we may get a “profile” of information as a resource in the organization, not only in terms of its quantity and space, but also in terms of quality and potential usage in managerial decision making.

## Summary and Conclusions

The paper proposes the application of inventory management concepts to the way information should be treated in the organization. This, we claim, will prevent and remedy information system failures in the same manner done in inventory control systems. Significant benefits have been achieved in the production and manufacturing fields by using concepts such as Just In Time, total quality control, and reduction of work in process. Such techniques are relevant and applicable to the MIS field as well.

A review of the many ills of work in process is given and the operations management techniques to remedy them discussed. The analogy to information systems is made by analyzing the problems that may result from information in process (IIP).

A proposed methodology is then outlined for the reduction of IIP in the firm's information system. Among the suggestions are: storing algorithms rather than IIP, using Pareto's 80:20 rule, focusing on relevant information, and using excess capacity.

Avenues for additional study in this new area of information as inventory are many. First, there has to be a way to assess the real cost of IIP. This may be done by a cost/benefit model that evaluates the expected value of a new item of data before it enters the database. Second, a study on the aging affect of data in the firm's databases should be undertaken. This will shed new light on the potential value of the information contained in the database. Third, a better assessment of the response times and the required levels of accuracy of an information system will contribute to an understanding of the real information needed by the decision maker. And finally, an extended set of performance measures should be defined for the firm's information system. Having these will lead to the development of tools and techniques to improve the effectiveness of information use.

## References

Ahituv, N. and Neumann, S., Principles of Information Systems for Management, 2nd Ed., Dubuque, Iowa W.C Brown, 1986.

Burbridge, J.L., “Operations Scheduling with GT and PBC”, International Journal of Production Research, Vol 26, 3, 1988, pp. 429–442.

Feather, J.J., and Cross, K.F., “Workflow Analysis, JIT Techniques Simplify Administrative Process”, Industrial Engineering, Jan. 1988, pp. 32–42.

Eden, Y. and Ronen, B., "Service Organization Costing: A Synchronized Manufacturing Approach", Industrial Management, September-October 1990, pp. 24–26.

Floyd, B., and Ronen, B., “Where Best to System Invest”, Datamation, November 15, 1989.

Floyd, B. and Ronen, B., "Office Automation: A Management by Constraints Approach", Working Paper, GBA New York University, 1989.

Goldratt, E.M. and Cox, J., The Goal, North River Press, Crotton on Hudson, New York, 1986.

Goldratt, E.M., and Fox, R.E., The Race, North River Press, Crotton on Hudson, New York, 1986.

Kaplan, Relevance Lost-The Rise and Fall of Cost Accounting, Harvard Business Press, 1987.

Lundrigen, R., "What is This Thing Called OPT", Production and Inventory Management, 1986, 2nd quarter, pp. 2–11.

Ronen, B. and Palley, M.A., "A Topology of Financial versus Manufacturing Management Information Systems", Human Systems Management, vol 7, 4 1987, pp. 291–298.

Ronen, B. and Pass, S., “MMIS: Manufacturing Management Information Systems”, Working Paper 1/89, Faculty of Management, Tel Aviv University 1989.

Ronen, B. and Starr, M.K., "Synchronized Manufacturing as

in OPT: From Practice to Theory", Computers and Industrial Engineering, August 1990, pp. 585–600.

Schonberger, R.J., Japanese Manufacturing Techniques, The Free Press, New York 1982.

Schonberger, R.J., World Class Manufacturing, The Free Press, New York 1986.

Schonberger, R.J., "Frugal Manufacturing", Harvard Business Review, Sept-Oct 1987, pp. 95–100.

Schragenheim, E., and Ronen, B., “The Drum-Buffer Shop Floor Control”, Production and Inventory Management, Third Quarter 1990, pp. 18–23.

Suzaki, K., The New Manufacturing Challenge, The Free Press, New York 1987.
