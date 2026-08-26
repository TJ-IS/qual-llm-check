---
otero_id: 17236
otero_key: "KSJYY2GQ"
title: "Decision support for exception handling and quality control in office operations"
authors: "Diane M. Strong"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90016-i"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for exception handling and quality control in office operations

Diane M. Strong \*

Boston University, Boston, MA, USA

This paper compares and contrasts the approaches of two companies to providing decision support within their office information systems. The offices examined in both companies perform order fulfillment functions. Examples from the companies are presented to illustrate options for providing decision support and the difficulties of matching computer-based support to an underlying office decision process. Three design options, the level of decision automation, the level of decision support, and the accessibility of information for decision making, are evaluated in the context of the examples.

Keywords: Decision support, Exception handling, Quality control, Order fulfillment

![](/api/attachments/KSJYY2GQ/fulltext/images/3d590f2a07e69c12a11914e08c14dae0c84983d12dd0b7fa301aadd92bb81038.jpg)

Diane M. Strong is an Assistant Professor of Management Information Systems in the School of Management at Boston University. She holds a Ph.D. in Information Systems from Carnegie Mellon University, an M.S. in Computer and Information Systems from New Jersey Institute of Technology, and a B.S. in Computer Science and Mathematics from the University of South Dakota. Dr. Strong's research interests focus on information quality including quality control in business information processes, methods for producing and maintaining high quality software, and impacts of advanced information technologies on information quality. Her publications have appeared in Expert Systems and Production / Operations Management, the Proceedings of the International Conference on Information Systems, and Management Information Systems Quarterly. She is a member of ACM and TIMS.

Correspondence to: Diane M. Strong, Boston University, School of Management, 704 Commonwealth Avenue, Boston, MA 02215, USA. smg97mn@buacca.bu.edu.

## 1. Decision support in office information systems

Much of the time of office workers is spent performing exception handling activities. These exception handling activities are necessary to handle special cases and to ensure that the information produced by offices is of acceptable quality [9]. Since exception handling often has a major decision component, performing exception handling well requires good decision making skills [10].

To support office operations, office information systems must be capable of performing normal office transactions and supporting decisions required for exception handling. Decision support capabilities are often excluded from office information systems under the assumption that the many special cases are difficult to anticipate. However, the significant human resources devoted to exception handling indicate that provision of decision support capabilities in office information systems should be examined further. To provide additional decision support, we must answer the following question: Where and how should decision support capabilities be provided in office information systems?

Our investigation of this question focuses on decision support capabilities for high volume operational level processes. Offices performing these functions are classified as Type 1/Flow offices by Panko [5]. The goals of office information systems and decision support in these offices are to ensure that: (1) correct and accurate information is produced from the process, (2) good decisions are made during the process, (3) information can be retrieved on request, and (4) the entire process operates in an efficient and timely manner. Complex “what if” analyses available in many decision support systems are generally not required to support decision making in these operational level high volume processes.

We examine offices that perform various order fulfillment functions at two companies. Order fulfillment is a high volume process with many routine, yet complex decisions. The decisions are routine in the sense that they are made frequently and they are made by clerks. The decisions vary from simple decisions to complex decisions including credit approval and scheduling of orders.

Section 2 describes our research approach. Section 3 presents examples of decision support at the offices we studied. These examples illustrate decision support capabilities that match the process they are supporting well and others that do not seem to consider the underlying decision process. Section 4 discusses the observations from the two companies and what can be learned from the examples about providing decision support in operational level office processes.

## 2. Research approach

## 2.1. Introduction

Our approach to understanding decision support needs in office processes is to study the decision making in several offices at two companies and the computer-based support provided for these decisions. Since the observed computer-based decision support is not necessarily appropriate for the decision task, we also discuss possible alternative approaches to providing support. At both companies we study order fulfillment, so that there is some common base for comparing and contrasting the support provided in the offices.

Section 2.2 briefly discusses order fulfillment and gives examples of the decisions needed during order fulfillment. Section 2.3 describes the office and decision making views and the methods used during data collection at the offices. Section 2.4 describes the two companies and the offices we studied. Section 2.5 describes how these data were analyzed for this paper.

## 2.2. Order fulfillment

Order fulfillment is the tasks performed to accept orders from customers and to fill, ship, and invoice these orders. Orders flow from customers to sales, then to manufacturing and distribution, and then back to customers in the form of an invoice and the product the customer ordered. Order fulfillment is a conceptually simple, operational level process, yet, in practice, many complexities are involved. The process spans organizational boundaries between sales and manufacturing, often involves a financial office for credit checking, and may involve engineering for product specifications. Information flows through many offices in a company during order fulfillment. This research is primarily concerned with the information flow required to move an order through the process. We do not consider the actual manufacturing or distribution procedures.

Routine, yet complex, decisions are involved in order fulfillment. These include deciding:

\- whether to give a customer priority treatment,

\- whether orders are complete and correct,

\- whether to approve credit,

\- which delivery date to specify to the customer,

\- which plants and warehouses will supply the product,

\- when the product will be produced and shipped.

Because order fulfillment is a high volume, operational level process, computer systems are generally employed. Since complex decisions are required, decision support capabilities are needed.

The decision making, information systems, and decision support in the two order fulfillment processes discussed in this paper demonstrate some of the options available for providing decision support within office information systems. Comparison of the two processes shows some of the difficulties of providing an appropriate level of office automation and decision support to match the underlying complexities of the process.

## 2.3. Data collection

Our data collection in offices necessarily takes a priori views of offices and of decisions and decision support [3]. These views will be briefly explained before discussing the methods used to collect data from the offices.

Newman [4] lists five types of office models: information flow, procedural, decision-making, database, and behavioral. Bracchi and Pernici [1] classify office conceptual models into four main categories: data-based, process-based, agent-based, and mixed. Our research primarily takes a process-based view since we focus on the order fulfillment process and how orders move through this process. Within this general process-based view, we focus on information flow in the process and on the decisions made during the process. This focus matches the goals of Type 1/Flow offices.

As part of our attention to information flow and decision making, we explicitly study the quality of information and how exception handling activities affect the quality of information. Decision making is an important component of exception handling. Our view of an office is derived from observations of the importance of information quality control and exception handling in offices performing order fulfillment functions $[8]$ .

Consistent with our focus on information flow, our view of decision making focuses on the information needed to make a decision. We study the decisions made during order fulfillment, the information needed to make these decisions, and the process employed to acquire the needed information. In this context, decision support is better if the needed information is readily available. Conversely, decision support does not match the order fulfillment process well if extra steps are needed to search for the information needed to make a decision. We do not ignore the rules for making decisions given the information, but this is not our primary focus

Data collection at the two companies generally followed the Office Analysis Methodology guidelines $[6,7]$ . This methodology suggests a top-down approach starting with managerial personnel to identify the organizational context and major functions of the office. Then focus shifts to a detailed analysis of the procedures performed in the office. Data collection at the two companies involved the following steps:

1. Interview managers about order fulfillment functions.

2. Interview people performing order fulfillment functions.

3. Observe people performing order fulfillment functions.

The steps were iteratively performed to resolve differences in the data collected from managers and from people doing order fulfillment tasks and differences between data collected by interview and data collected by observing the work process.

## 2.4. Field sites

Both companies have order fulfillment processes, but there are some differences. One order fulfillment process is a complex process involving engineering specifications and manufacturing to a customer order. The other is a simpler process involving standard off-the-shelf products. Both companies use office systems that have been either developed internally or substantially tailored to the company's offices. This tailoring is necessary because current office systems cannot yet provide generic tools and still fit the process well [2].

To maintain the confidentiality of the companies, they will be referred to as companies SFI (ship-from-inventory) and BTO (build-to-order). Characteristics of the two companies and their order fulfillment processes are discussed below.

## SFI Company

SFI Company is a medium-sized healthcare products company. The company manufactures and distributes healthcare products primarily to distributors who, in turn, sell the products to hospitals and health care centers. They manufacture or purchase their products and inventory them at several warehouses throughout the country.

Orders are processed at a central location. Distributors submit orders by telephone, fax, mail, or EDI. After orders are entered into a computer system, inventory is allocated to them. If inventory is available, picking and shipping tickets are electronically transmitted to the warehouses the next morning. The warehouses pick and ship the items to the distributor. The order information also becomes input to the MRP system for production and purchasing decisions.

Order fulfillment functions at the central location are supported by one large minicomputer system. This is a new system, developed and implemented within the last year. Approximately 20 people work at the central location performing order fulfillment functions. Of these, 3 are managers, 14 are customer service representatives (CSR's) who take the orders and enter them into the computer system, and 3 are planners that ensure that orders are shipped from warehouses and that manufacturing plants receive new demand information. All three managers were interviewed, but the detailed study focused more on customer service than on the planners. These people handle approximately 800 orders per day or approximately 200,000 orders per year.

Exceptions occur in the order fulfillment process. These exceptions include backorders and special processing for government orders, for priority treatment (e.g. faster shipment, no partial shipment), and for credit holds. Salespeople or customers may request information about products specifications, product availability, product delivery dates, and information about the status of specific orders. People may call and order products that do not have a contract with the company. In addition, errors can occur when the products sent to a customer do not match the products ordered, when the invoice sent to a customer is incorrect, e.g., because of incorrect pricing, or when there are quality problems with the received products. Many of these exceptions require information retrieval and decision making by the customer service representatives.

## BTO Company

BTO Company is a Fortune 100 electronics manufacturing firm with sales and manufacturing facilities in many countries. They manufacture large, expensive electronics systems that are sold to other firms for their use. Customers select from many options when specifying the product they want. These options are configured into a complete product and the product is then manufactured according to these specifications.

Orders are collected world-wide, entered into computer systems, and forwarded to centralized computer systems for processing. Centralized processing of orders includes configuring the product, scheduling it for production, and selecting one or more plants to manufacture components of the product. Orders are then electronically distributed to the various plants for production. When production at a plant is complete, the centralized computer system is notified. When all components are produced, the order is authorized for shipment. This entire process takes one or more months.

Several large minicomputers support the centralized order fulfillment functions. Much of the software was developed years ago when the business was smaller and the decision rules for scheduling and plant selection were different. These systems are gradually being updated. Sometimes they are replaced or augmented by expert systems to make some of the more complex decisions, such as configuration and plant selection. Approximately 100 people work in the centralized locations performing order fulfillment functions. These people handle approximately 100,000 orders per year.

Our study of this order fulfillment process focused on the centralized functions. We did not study order entry, operations in sales, or operations in the plants, except to investigate the quality of the order information arriving from sales and the quality of the information sent to the manufacturing plants. The centralized functions and the people performing them are sub-divided by major product categories. We studied the offices performing the centralized functions for one product category, the mid-range systems.

A number of exceptions occur during centralized order fulfillment processing at BTO. These exceptions include incorrect and incomplete order information, customer requested changes to orders, requests for priority treatment, incorrect plant selection, incorrect scheduled ship date, and components that cannot be configured.

## 2.5. Data analysis

We take a data driven approach to considering the role of decision support in office systems. First, we consider the decisions made in order fulfillment offices. The interview and work observation data from the two companies were reviewed to find the decisions made during the process. Requests for assistance or information from people external to the office, such as from customers, were also included in the list of decisions. These were included because of our focus on exception handling, which usually requires decision making, but also includes some problems resolved by information retrieval only. This decision information provides the baseline for considering what could be done to support these decisions.

The support for these decisions was then considered. For each decision, we examined the information acquired to make the decision and how this information was obtained. The role of computer systems in providing information and assisting in decision making was reviewed. We also studied interview data about additional support that could or should be provided. Thus, we have data on both the support of decisions in the process and on possibilities for better support.

This information about decisions, decision support, and possibilities for better support is the basis for the examples and the discussion presented in this paper. The results of our analyses are presented in the form of examples of decisions and how they are supported. The examples were selected to cover the types of decisions we observed and to illustrate difficulties of providing support that matches the underlying decision process. Examples of both good support and poor support are included.

## 3. Decision support examples

The decision support examples are grouped into six categories, order taking, customer problems, manual decision making, quality control, exception handling, and management decisions. These groups represent different decision making purposes and are approximately ordered by decision complexity. Except for the first category, order taking, all the categories are some form of exception handling.

## 3.1. Support for order taking

At the SFI company, approximately 70% of orders arrive via telephone. The customer service representative (CSR) asks the customer questions, enters the responses into a computer system, and provides the customer with delivery date feedback. The computer system responds quickly and provides the information needed to support order taking. However, the process of accessing information does not always match the order taking process.

For example, providing delivery date information to customers is an extra step in the order entry process. Inventory availability determines delivery date, but order entry and inventory status are different menu selections. When taking a telephone order, the CSR writes the product numbers and quantities on a sheet of paper and then enters these as an order. After entering the order, the CSR ends order entry and selects inventory status. She re-enters the product numbers to check inventory status and reports this information to the customer in the form of an approximate delivery date. The CSR performs extra work by selecting a different menu option, re-entering product numbers, and translating inventory availability to expected delivery date. The computer system could more directly support the process employed by the CSR if inventory status was automatically checked at order entry time and translated into an expected delivery date.

Support for customer address information is much better than the support for delivery date information. When a CSR starts to enter an order, she first enters the customer number provided by the customer. The computer system then lists the possible shipping addresses for that customer and the CSR selects the appropriate one based on feedback from the customer. The CSR does not have to obtain the entire address from the customer. If the customer does not remember their number, customer information can also be obtained by zip code. This process works for SFI because all customers must have a contract with SFI before they place any orders. When the contract is agreed to, customer information, such as addresses, is entered into the computer system.

## 3.2. Support for researching customer problems

At SFI company, customers request information about orders, especially when an expected order has not arrived or when the products that were delivered do not match what the customer thought they ordered. At BTO company, sales often requests information about the status of orders or puts through changes to orders after orders have submitted, but before they are shipped. Therefore, both companies must provide ways of looking up information about customer orders.

Neither company's computer systems adequately support the people who must retrieve and report the requested information. As orders move through steps in the order fulfillment process and through offices in the organization, the order information is moved. In both companies, the person attempting to retrieve information about a customer order must know the stage of the process that the order is in. At SFI company, an order may be mailed in and not yet in the computer system, in the computer system but not yet allocated for distribution, in the computer system and already allocated for distribution, or archived in hardcopy form. Each of these four places in the process requires a different procedure for retrieving order information. The CSR attempts to get information from the customer about when the order was placed so she can start searching at the most likely place. At BTO company, orders move through four computer systems as they move from sales to a production plant. To find information about an order, the order processor must know which system contains the order. The order processor starts at the most likely place based on what they know about the order.

The difficulty lies in providing this retrieval support on top of a transaction oriented system. The transaction system moves orders through the process. Providing people needing order information with retrieval access to all the stages in the process is relatively easy, but does not directly support the information needs of order processors or CSR's.

## 3.3. Support for manual decision making

Neither SFI's nor BTO's order fulfillment process is completely automated. There are points in each process where manual intervention is required to initiate the next step in the process.

For example, at BTO the scheduling computer system assigns a ship date to each order. This date is the last day of a month. The order processor manually assigns a weekly date to the order and tells the computer system when to release the order to manufacturing plants. Thus, release to manufacturing and selection of a weekly schedule date are manual decisions. The computer system stores these dates and transmits orders to the production computer system on the release date, but it does not provide any assistance in selecting these dates beyond selecting the monthly schedule date.

At SFI, the planners decide what products will be packed into each truck going from the central warehouse to restock the regional warehouses. The computer system provides information about the urgency of the inventory requirements at the regional warehouse. It also provides shipping volume information for the products and sums these. Thus, the computer system provides the information needed by the planner to make the decision. The planner is deciding whether to ship partial trucks, to delay products that only partially fill a truck, or to fill a truck with products that will be needed later. He can also override some of the information if he has more recent information than the computer system has, e.g., a telephoned in emergency request.

In both companies, credit approval requires some manual decision making. At SFI, since customers are required to have contracts with the company, some companies are pre-approved in the computer system. The computer system sends orders to credit only if they do not have approval already. In both companies some manual intervention is required to give customers priority treatment. Requests for priority treatment are more common at BTO because order fulfillment can take more than a month. At BTO, there is essentially no computer-based support for deciding to give priority treatment or in giving that treatment. Order processors know from experience whether they should grant a priority request. At SFI, the order is shipped the next day so there is less need for priority treatment. On request, the orders may be shipped the same day. The computer system provides support for this by immediately allocating inventory to the order and transmitting a pick and ship ticket to the warehouse.

## 3.4. Support for quality control

Many of the office activities in the order fulfillment process at BTO involve checking the order information for acceptable quality and fixing any detected problems. A person decides whether various pieces of order information are of acceptable quality. Computer systems can support these decisions by detecting problems automatically, by focusing attention on possible problems, or by providing explanations of computer-generated information.

The complexity of automatically detecting quality problems by computer ranges from flagging missing fields to expert systems that indicate the cases they cannot solve. For example, at BTO an expert system generates a product configuration from the product options ordered. This expert system indicates when it cannot successfully generate a configuration.

If a computer system cannot automatically detect problems, a person searching for problems could be assisted if the computer system indicated likely problems. Since order fulfillment and other office processes are often high volume, methods for focusing people's attention on problems is important. However, we did not observe this in our offices. For computer systems that do not automatically detect problems, people had to scan all of the outputs searching for problems. From experience, order processors learned which cases were likely to have problems and they focused their attention on these cases. More decision support is needed to assist people in cases where the computer system cannot automatically detect problems.

If the information is computer-generated, a person may have difficulty deciding whether the information is correct. For example, a system at BTO selects build sites for components of the product. This system can usually select a site, but it is not always a correct site. However, the decision rules for selecting the appropriate site are complex and are based on the particular combination of options ordered. A person reviewing the output of this system could be assisted if the system explained why it selected a particular build site.

## 3.5. Support for exception handling

If information is detected as missing or incorrect by a computer system or a person, someone must decide what the correct information is. Computer systems can provide support for this exception handling task. When computer systems detect exceptions, they can provide exception handling assistance by indicating possible solutions or by indicating causes of the problem. At BTO, the configuration expert system indicates the components that is could not successfully configure. This provides information to a person who decides whether the expert system did not have sufficient knowledge to do a complete configuration or whether the components ordered cannot be configured. The system also provides some indication of why it could not configure, e.g., unrecognized component, incompatible components, or missing connecting components.

In our observations, support for exception handling is often related to support for quality control. That is, if a computer system provides support for finding quality problems, it is also likely to provide at least some support for handling the exceptions found. The configuration expert system at BTO is an example of this.

In addition to instances in which exception handling was not supported by a computer system, we observed cases in which computer system controls made exception handling difficult. For example at BTO, computer system controls prevented changes to build sites for orders after production had started and any site had confirmed that it had completed building its part of the order. However, because of inventory shortages or build site selection errors, build sites sometimes needed to be changed when the order was almost complete. The change process involved de-confirming any completed build of components, de-allocating inventory, making the change, re-confirming builds, and reallocating inventory. Since one person does not have the authority to make all these changes, any change requires the coordination of multiple people at multiple plant locations.

There are also examples at SFI company where computer system controls make it difficult to make necessary changes. After inventory is allocated to an order, changes cannot be made without involving people at the distribution site. Another example at SFI involves orders from salespeople for product samples. If an order is entered incorrectly, the data entry person must contact a manager to have the entry backed out.

## 3.6. Support for management decisions

In addition to supporting routine decisions made during office processes, office information systems can provide information for management. Typically, management receives information about outcomes of the order fulfillment process, e.g., the number and dollar volume of orders shipped and backordered. This information helps in monitoring the performance of the business.

These outcome measures provide little information about how well the order fulfillment process is working. Companies may not know that information processing is not working well until orders fail to be delivered to manufacturing or

Table 1
Decision automation and decision support distribution. For example, BTO experienced problems with order flow that severely affected company revenues. In addition, knowing that the process is not working well does not necessarily provide information about why the process is not functioning well.

Neither company provides management with measures of the process; they only receive measures of the outcomes of the process. It would be helpful if office systems provided diagnostic measures of the process that could be used to detect problems before the outcomes of the process are adversely affected.

## 4. Discussion

These decision support examples show that office information systems can take different approaches to the presence of decision making in office environments. Designers of office information systems must consider several design choices, including how automated systems should be, what support should be provided for decision making, and what information should be available. The examples presented in this paper indicate the difficulties of making these design decisions. In both companies, improvement could be made in the decision support capabilities provided in their office systems.

Although our field study has a small sample size, we can make some preliminary recommendations about the provision of decision support capabilities in systems in Type I/Flow offices. The decision support capabilities in any office information system should match or fit the underlying decision process. For these offices, the fit to the process must be considered relative to their performance measures, specifically the quality of the information produced and the efficiency of the process. Because of the efficiency requirements, a good fit to the office process is important.

Our discussion of decision support capabilities in these office systems will focus on three dimensions: how automated decision making is, how much decision support is provided, and how accessible information for decision making is. These three dimensions capture support problems common to several decision support examples.

<table><tr><td rowspan="2">Decision automation</td><td colspan="2">Decision support</td></tr><tr><td>High</td><td>Low</td></tr><tr><td>High</td><td>Easy to monitor, control, and change computer decisions.</td><td>Difficult to override computer decisions.</td></tr><tr><td>Low</td><td>Easy to obtain information and support for decision making.</td><td>Difficult to find information for decision making.</td></tr></table>

## 4.1. Decision automation and decision support

Two design dimensions, level of automation and support for decision making, were apparent in several of the examples. Level of automation denotes whether the decision maker is a computer system (high automation) or whether the decision maker is a person (low automation). For either of these cases, the support provided to a person making, monitoring, or overriding a decision may be high or low. This framework, shown in Table 1, provides a structure for discussing these design choices in office information systems.

Each of the four cells in Table 1 may be appropriate for some decisions in some office processes. None of the combinations is inherently a poor or a good design. Whether a particular combination of automation and support is appropriate depends on the decision process.

## High automation, high support

In this combination, the computer system makes the decision, but there is sufficient support for people to easily evaluate the computer system results and change them as needed. An example is the configuration expert system at BTO. This combination is good when a computer system can automatically make many decisions, but there are known difficult cases that a person must decide. In these difficult cases, the computer system switches from an automated decision mode to a decision support mode to aid a decision maker. This combination may also be good in changing environments where the computer system can make a good initial decision, but due to a changing environment a person may need to override this decision. Build site selection at BTO is an example of this. However, the build site selection computer does not provide a high level of support, so making the necessary overrides is difficult.

This combination can be poor when the decision is complex and the computer system generally makes better decisions than the people overriding the computer decisions. In this case, less support could be better. That is, management may decide to make it difficult to override computer decisions. This can be done by including controls so that computer decisions will not be changed unless necessary. Less decision support in a system is also likely to yield an office system that runs faster and needs less maintenance.

This combination can also be poor if the decision is too complex to be automated. In this case, decisions must be frequently overridden. Less automation may make the decision process more efficient. Instead of deciding whether the computer output is good, the person can make the decision.

## High automation, low support

In this combination, the computer system makes the decision and little support is provided for evaluating or changing the decision. This combination is good if the decision quality is generally better without overrides, but it is inefficient if overrides are commonly required. If overrides are commonly needed, it may be better to allocate more resources to providing high support, rather than to providing high automation.

Unfortunately, the need for overrides is often not a stable condition. When an expert system is first installed, especially if it is a prototype, overrides may frequently be needed. As the system's expertise is developed, the system may reach a point at which it generally makes better decisions than the people. Then low support may be appropriate. Alternatively, high support may be provided as with the configuration expert system, but the person only makes a decision when the system fails to make a decision. With conventional systems the opposite direction of change may occur. The system may adequately handle all cases when it is first installed, but as the organization changes and maintenance lags, the system may need more overrides.

## Low automation, high support

This case represents a typical decision support system – the computer system does not make the decision, but it provides good support to a person making the decision. The decisions made by the planners at SFI about truckloads are an example of this. In general, this combination is good when the information required to make the decision is known, but all the rules for making the decision are not known. It is also a good starting point in a prototype that will eventually provide automated decision making.

For many decisions in high volume offices, a low automation, high support combination indicates insufficient automation. It is likely that more of the decisions of the planners at SFI could be automated now that the system has been operating for some time. However, there are some complex, somewhat subjective decisions that legitimately belong in this category. Examples include credit decisions and scheduling decisions.

## Low automation, low support

This combination is appropriate for decisions that are difficult to automate and for which computerized support is difficult to provide. These decisions are best made by experienced people. Examples are highly subjective decisions such as the decision at BTO to provide priority treatment to a customer.

In high volume office processes, decisions of this type cause problems because they require significant time from experienced people. For these cases, it is important to investigate whether better support can be provided to make the decision process more efficient.

## 4.2. Information accessibility

The accessibility of the information needed to make a decision was important in several of the decision support examples. Accessibility is affected by the organization of the information and whether the information is maintained on-line.

Both SFI and BTO organized their on-line information primarily by the stage in the process rather than an organization that more closely matched the process of requesting this information. This created inefficiencies in both organizations. The organization by process stages resulted from using the organization of the underlying information flow system rather than providing additional support for ad hoc retrieval requests.

SFI has an additional accessibility problem. Order fulfillment at SFI is a higher volume process than at BTO (twice as many orders per year) and they have smaller computer systems. The result is that SFI cannot maintain much history on-line. CSR's frequently must go to archival hard copy to look up customer's orders. SFI must explicitly decide which information should be kept on-line to produce the most efficient information retrieval.

## 4.3. Conclusion

Based on the above discussion, we can summarize the different approaches taken at SFI and BTO to providing decision support capabilities in their office systems. SFI is a much simpler process than BTO with higher volume, but its decision support facilities generally fall in the low automation category. SFI could consider automating more of its decision making. The simpler process makes automation easier and the high volume makes it worth investigating.

BTO's more complex process employs higher automation, but they experience problems with frequent needs to override computer systems. Since BTO has some old computer systems and some expert systems in prototype stage, further computer system maintenance may allow them to continue with high automation. Because many of BTO's decisions are complex, they want to maintain automation to produce high quality information from the process. However, in some cases, BTO may need more decision support capabilities to support its automation of complex decisions.

The analyses of the order fulfillment processes at SFI and BTO presented in this paper provide an example of how other office processes could be analyzed for decision support opportunities. The analysis procedure is to find the decision points in the process and study how the decisions are made and the information accessed. The information from the study provides the basis for evaluating the support provided and investigating possible choices of technology to support decision making and information retrieval.

There are several possibilities for extending this study. This research studied offices of one of six types of offices $[5]$ . Further research is needed to test whether this analysis and these results apply to other types of offices. They are more likely to apply to other forms of Type I offices (operational level offices) than to forms of Type II offices (managerial offices). In addition, this study could be extended to study Type I/Flow offices that do something other than order fulfillment.

In general, more research is needed to determine how best to incorporate decision support capabilities into office information systems. Research similar to $[2]$ , which studies possibilities for providing general office functions that can be tailored to individual offices, may be able to find ways of incorporating general decision support facilities into office systems so that these facilities can be tailored to support specific decision processes. As can be seen from the offices we studied, more decision support capabilities are needed in office systems.

## References

[1] Bracchi, G. and B. Pernici, “The Design Requirements of Office Information Systems” ACM Transactions on Office Information Systems 2, 3 (April 1984) 151–170.

[2] Croft, W.B. and L.S. Lefkowitz, “Task Support in an Office System” ACM Transactions on Office Information Systems 2, 3 (July 1984) 197–212.

[3] Hirschheim, R.A., “The Effect of A Priori Views on the Social Implications of Computing: The Case of Office Automation” Computing Surveys 18, 2 (June 1986) 165–195.

[4] Newman, W., “Office Models and Office System Design” in Naffah, N. (ed) Integrated Office Systems – Burotics North-Holland (1980) 3–10.

[5] Panko, R.R., “38 Offices: Analyzing Needs in Individual Offices” ACM Transactions on Office Information Systems 2, 3 (July 1984) 226–234.

[6] Sirbu, Jr., M.A., S.R. Schoichet, J.S. Kunin, M.M. Hammer, and J.B. Sutherland, "OAM: An Office Analysis Methodology" in Office Automation Conference Digest AFIPS (April 1982) 317–330.

[7] Sirbu, Jr., M.A., S.R. Schoichet, J.S. Kunin, M.M. Hammer, J.B. Sutherland, and C.L. Zarmer, Office Analysis: Methodology and Case Studies Technical Report MIT/LCS/TR-289, Laboratory for Computer Science, Massachusetts Institute of Technology (March 1983).

[8] Strong, D.M., “Design and Evaluation of Information

Handling Processes" Ph.D. Dissertation, Carnegie Mellon University (1988).

[9] Strong, D.M. and S.M. Miller, “Exception Handling and Quality Control in Office Operations” Working Paper 89-16, Boston University, School of Management (September 1989).

[10] Suchman, L.A., “Office Procedure as Practical Action: Models of Work and System Design” ACM Transactions on Office Information Systems 1, 4 (October 1983) 320–328.
