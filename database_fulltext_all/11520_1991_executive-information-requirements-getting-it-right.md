---
otero_id: 11520
otero_key: "87MTRRB5"
title: "Executive Information Requirements: Getting it Right"
authors: "James Wetherbe"
year: "1991"
journal: "MIS Quarterly"
doi: "10.2307/249435"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Executive Information Requirements: Getting It Right

By: James C. Wetherbe
MIS Research Center
Carlson School of Management
University of Minnesota
271 19th Avenue South
Minneapolis, Minnesota 55455

## Abstract

Most managers spend half their time trying to get the information they need, whether it be informally through meetings, phone conversations, or reading, or formally through organizational computer-based information. During this process they have to sift through a great deal of useless information, a situation commonly referred to as "information overload." With the proliferating capabilities and plummeting cost of computers, it seems relief should be in sight for weary executives. Unfortunately, most information systems—formal or informal—do not meet executive needs. Indeed, most new systems require extensive revision (after they are supposedly completed) to even partially fulfill needs. This is a terrible loss. Most systems are expensive enough to develop. They are even more expensive to revise. As the pace of business accelerates, decisions that could wait for weeks must now be made in days, hours, or even minutes. Failure to get executives the information they need in a timely manner can result in lost opportunities or in a problem not being solved in time. Increasingly, executives have little reaction time to make decisions on pricing, product introduction, resource allocation, media inquiries, response to competition, and mergers. They need access to information without waiting several weeks or months for a computer project. Why can't executives and system designers work together to more correctly anticipate and determine information requirements? In this article, four reasons information requirements are not met are discussed, and four straightforward solutions executives can use to solve this problem are offered.

Keywords: Information requirements determination, prototyping, joint application design, cross functional design

ACM Categories: D.2, H.2, H.4

## Introduction

The new vice president of engineering for an aerospace company noticed that he automatically received 32 computer-generated reports each month. He was having difficulty determining what to do with most of them. Convinced his predecessor received these reports for a good reason and reluctant to admit his inability to find meaning for them, he had an idea. If he found out who the other managers were who also received copies of these reports, he could subtly inquire what they used them for and thereby determine what he was “missing.”

He asked his assistant to get distribution lists for all 32 reports. Within a week, the assistant returned with the distribution lists.

"So who gets copies?" the vice president inquired

"Two people, you and me," the assistant replied.

Startled, the vice president asked, "What do you do with your copies?"

"They are just backup copies in case you lose one of yours."

By paying close attention during the next year, the vice president determined that he only needed four of the 32 reports. He also determined there was some very important information he was not getting. He discontinued the unneeded 28 reports, which resulted in immense appreciation from those who had to provide data to generate them. He then began to focus on getting the information he really needed. Over the next year he became frustrated with the inability of the information system department to meet his requirements. The information system department in turn became frustrated with his inability to “make up his mind” about the information he needed. Because his requirements were in a constant state of flux, the department had to continually revise the systems.

The preceding example is all too common and represents a major cause for lost productivity among executives and their computer people.

The most important task of an executive is decision making. Outside of his or her intellect, the most important resource an executive uses is information. Yet time and again, executives complain they are overloaded with irrelevant, useless information, and they are unable to obtain the information they need promptly.

The cost and time required to remedy a system that fails to meet management's needs can often exceed the cost and time required to develop the initial system. High as it might be, the revision cost might only be a fraction of the opportunity cost of management making a bad decision because it could not get needed information. Consider the claims manager who cancelled the insurance of a teenager because of a bad driving record. Unknown to the claims manager, the teenager was the son of the president of a large corporate account. You can guess the rest of the story.

Fortunately, executives can play a positive role in ensuring that a new system meets their information requirements. By understanding why systems fail to meet requirements and the remedial actions required, an executive can work with systems analysts to get the system right.

This article covers the causes and solutions for this problem. Discussed first are some fundamentals of information and decision making. Next, a review is provided of the four common mistakes that are made both by executives and system designers when information systems are designed. Finally, four techniques—cross-functional systems, joint application design, structured interviewing, and prototyping—are presented as pragmatic, easy-to-implement solutions for correctly determining executive information requirements.

## Managers and Information

One of the most important revelations about managers and information that has come from research and practice is that managers don't know what information they need. $^{1}$ In a study coordinated by the MIS Research Center at the University of Minnesota, we found that 76 information systems developed in 26 organizations all required minor to major revisions after they were completed to even approximate management's information requirements (Jenkins, et al., 1984). The systems development process can be broadly categorized into designing the right system and implementing it right. Given an appropriate design, most information systems departments can successfully implement a system. The big problem is correctly determining information requirements and designing the right system.

How do most system analysts go about determining what information managers want from their computer system? They do the obvious and the logical. They ask, "What information do you want from the new order processing (or whatever) system?"

Unfortunately, managers usually do no know what information they need. They give it their best attempt, assuming these brilliant computer wizards will sort things out. Several months and millions of dollars later when the system is delivered, managers quickly discover the system does not give them the information they need.

Managers ask for changes, and the system analyst goes into shock. Costs and time to change the design of a system after it is complete are 50 to 100 times higher than making those same changes during systems design. This sounds like an exaggeration, but it is not. If you have had a custom-built house (or know someone who has), you may be familiar with these dynamics. For example, consider the cost of adding a bathroom after the house is complete versus the cost of adding a bathroom during the blueprint or design stage. This explains why so many needed revisions are never implemented. Consequently, the resulting systems are a disappointment. A disappointing system can range from a system that partially fulfills management's requirements (with or without expensive revisions) to one that is totally abandoned, resulting in a million dollar write-off.

For example, a major bank recently completed a multimillion dollar project that tracked all of its customers' financial relationships with the institution. After the system was completed, it was demonstrated to various management teams who asked if the system would be able to provide information it was not designed to provide. In other words, managers wanted information that had not been requested when the system was designed the previous year. Though it would not have been difficult to add the reporting capabilities requested had they been identified before systems development, to add them now would delay the project more than a year and double the cost of the system. Management was so furious that the project, which at this point represented over \$40 million, was cancelled, with many people losing their jobs.

Having been victims of managers' inability to properly define their information requirements, most systems analysts go to Plan B—the "user signoff." This approach involves asking managers what information they want from a system and then requiring them to sign a document aimed at contractually obligating them to accept the system when they get it. User signoffs have marginal political value when systems analysts are battling with management about system revisions, but they do not solve the functional problem, which is that managers do no know what information they need.

For example, in the banking example discussed above, the managers signed off on the design. However, once they realized the system would not satisfy them, they blamed the responsible system analysts for misleading them. Top management legitimately claimed: "You technical people should have protected us from our lack of expertise in this area." A user signoff is a powerless piece of paper when matched against the fury of top management.

Plan C, commonly used by systems analysts, is to use the “catalog” approach to information requirements determination. This approach involves showing a manager a wide variety of reports, perhaps requested by other managers or available from a commercially available software package. As the manager reviews these reports he or she selects the ones believed to be needed. This may seem like a good idea, but it does not work. When you offer managers a lot of reports, they request them whether they need them or not.

In research projects we have offered cosmetically impressive, but useless reports to managers and have found that they have a high propensity to take them (Benbasat, et al., 1977; Judd, et al., 1981). For example, in one study, production managers were offered 20 different reports. Eight of these reports were deemed useful by a panel of production experts. The remaining 12 reports were useless, thrown in with the eight reports to see if anyone would take them. Most managers took all 20 reports. What they are generally doing is playing it safe. Uncertain as to whether they could use the information, they played it safe and requested it. In practice, although the manager requesting the information does not use it, the manager who replaces him or her years later may assume the information has some value. Consequently, he or she may often be found staying late at work, sifting through the useless reports, asking the compelling question: "I wonder what my predecessor was doing with this information that I am missing?"

Years of this phenomenon results in information overload episodes similar to the one described in the beginning of this article.

Four fundamental mistakes have historically been made in the process of determining what information executives need. These mistakes are viewing systems as functional instead of cross-functional, interviewing managers individually instead of jointly, asking the wrong questions during the interview, and not allowing trial-and-error in the detail design process.

## Cross-Functional Systems

The first mistake that has historically been made in determining information requirements for information systems is that most systems are viewed as being functional as opposed to cross-functional (Wetherbe, 1988). This perspective is too narrow. For example, when developing a new budgeting system, we tend to focus on what information is needed by the budget managers or budgeting staff members. The problem is that people other than budgeting staff make use of budgeting information.

Virtually all managers need access to budget information. Unfortunately, if the budget department is designing the system, the system carries a very strong control orientation as opposed to a general management reporting orientation. This results in budgeting systems that end up much like a banking statement. Most people use a banking statement to simply reconcile whatever they are using to track their personal finances, whether they be on paper or a personal computer. Similarly, many managers keep their departmental budgets on a departmental computer and simply reconcile them with the "control" statement they receive from the budget department. Due to this phenomenon, up to 60 percent of the data entered into personal computers are keyed from reports generated from other computers in the same organization.

For example, a marketing vice president for a manufacturing company wanted to categorize costs and revenue by salesperson, customer, and product. The budgeting system only allocated costs by project account number. A project could involve more than one salesperson, more than one customer, and more than one product. Only through extensive data collecting from the sales force and the use of spreadsheet software could the information needed be obtained.

Some would argue that the budgeting department should go ahead and incorporate the reporting needs of functional managers in the development of a new budgeting system. But the common argument against this would be that it would increase the cost of developing the system. The flaw in this logic is that the increase in costs exists anyway because these functional managers have to develop their own systems. In the end, this costs more than if the systems were developed across the board and shared.

As this marketing vice president said, “The accounting department adds so much overhead to marketing by wanting more and more data categorized in ways to allow them to control and audit us. I need information categorized in ways to help us sell effectively and efficiently. The systems designed by budgeting are not responsive to my needs. Have you ever heard of a company that was successful because it had the best accounting in the world?”

To illustrate the need to develop systems cross-functionally, consider a business process such as order processing. To process orders, sales people have to decide which customers to call on, what to sell them, and what is available to sell. Credit must decide which customers can have credit and how much, which customers need past-due notices, and which customers' credit should be discontinued. The warehouse must decide what and how much inventory to stock, when to reorder, when to unload slow-moving inventory, and which customers to allocate limited inventory to. Shipping must decide such things as what merchandise to send to which customers, what orders can be shipped together to save delivery costs, and when trucks should depart. These decisions are summarized in Table 1. In developing a new system, we should provide information so that all decisions can be improved.

For example, consider the last decision listed for the warehouse department in Table 1—which customers to allocate available inventory to. If the warehouse has five orders but only enough inventory to fill three, it must make a resource allocation decision. Typically, this decision would be made on a first-in/first-out (FIFO) basis. That seems equitable and fair, given the information they have available to them.

This could result in a terrible decision. What if a customer who does a lot of business with the company really needs this shipment promptly, recently received an order late and was furious about it, is paying a high profit margin on the order, pays bills promptly, and a truck is routed to deliver a shipment to another customer nearby the same afternoon. But because a FIFO decision was made, the inventory is allocated to someone who hardly ever does business with the company, to whom the order is not urgent, who yields a low profit margin, does not pay bills on time, and a truck is not going into the vicinity for the next three weeks, during which time inventory could have been re-stocked anyway.

In trying to improve the quality of the decision, factors that should be considered include:

\- How important is each customer to the business?

\- How promptly does each customer need delivery of the order?

• What is the profitability of each order?

• What is the credit status of each customer?

\- What is the shipping schedule for delivery to each customer?

\- Has the customer recently been upset because a previous order was late?

Note that the information needed to improve the decision making in the warehouse comes from outside the warehouse. For example, customer need, importance, and profitability would come from sales, credit worthiness would come from credit, and shipping schedule would come from shipping.

Table 1. Decision Centers Involved In Order Processing

<table><tr><td>Decision Center</td><td>Activity</td><td>Examples of Major Decisions</td></tr><tr><td>Salespersons</td><td>Selling Merchandise</td><td>Which major customers to callWhat to sell customersWhat is available to sell</td></tr><tr><td>Credit Department</td><td>AccountsReceivableManagement</td><td>Which customers to allow creditHow much credit to allowWhich customers need past-due noticesWhich customers&#x27; credit should be discontinued</td></tr><tr><td>Warehouse</td><td>InventoryManagement</td><td>What inventory to stockHow much inventory to stockWhen to reorder stockWhen to unload slow-movingWhich customers to allocate available inventory</td></tr><tr><td>ShippingDepartment</td><td>Packing and Shipping Orders</td><td>What merchandise to sell to what customersWhat orders can be shipped together to save delivery costWhen trucks should depart</td></tr></table>

A very important concept of information management, therefore, is that most of the information needed to improve the decision making within a function will come from outside of the function. This is why it is so important for an organization to share information if it wants to improve productivity. When an organization learns to share information cross-functionally, employees are empowered to make better and more productive decisions for the organization.

The bottom line is that in order to develop a new information system, it is necessary to be aware of all functions that are touched by the information system and be sensitive to their decision-making requirements. Then a system can be developed that allows information to flow cross-functionally to improve decision making.

As straightforward as the concept of cross-function systems is, most system analysts attempting to develop them complain that employees are very proprietary about their "functional" information and are often unwilling to participate in a system that will "share" information. Recognizing that information is power, employees are not interested in sharing power.

For example, sales representatives for a manufacturing company were not allowed to access customer credit status. Consequently they would occasionally invest substantial effort into landing a large order for a client only to have it rejected because of credit/financing conditions. Customer relations were damaged and sales morale suffered as the sales force began to refer to credit as the “sales prevention department.”

This attitude is totally dysfunctional. Since information is power, the idea is to empower decision makers by giving them the best information to make these type of decisions. An organization that does not share information cross-functionally ends up with the left hand not knowing what the right hand is doing.

To solve the problem, top management needs to use its leadership and influence to achieve cross-functional design. When a new system is being undertaken, those functions that are transcended by the new system must have management participation in the design.

## Joint Application Design

The second mistake commonly made in the determination of information requirements is that the system design team usually interviews managers individually instead of using a group process, also known as joint application design. The individual interveiwing process places cognitive stress on a manager, stress that hinders his or her ability to respond adequately to questions.

Consider this scenario: A group of strangers come into your office and ask you to tell 10 jokes. Even though you probably know 10 good jokes, you might have difficulty recalling them. Most people would. Let's change this scenario. What if a group of you and your fellow managers within the company are put together in a room and asked to generate some good jokes. Very likely you and your colleagues could generate 80, 90 maybe 100 jokes. Each manager would be familiar with perhaps 80-90 percent of them. In other words, each manager really knows a great deal of jokes, but when asked to come up with them off the top of one's head, one would have difficulty recalling them. The moral is that group or collective experiences and memory are essential in recalling information. When people are asked to tell a joke, they generally tell ones they have heard recently. By themselves they cannot remember many from the past. Similarly, when managers are asked what information they need, they generally mention things they needed recently, not everything they need. Therefore, one reason that we want the requirements determination to be done as a group or joint process is so the memory of each manager can be pooled to do a more thorough job of recalling key requirements.

A second reason for a joint application design is that different functional areas of an organization have different agendas when it comes to developing a new information system. For example, considering the order processing system portrayed in Table 1, each decision center would likely emphasize different design criteria. Sales may view the primary importance of order processing as ensuring prompt and correct delivery of orders to customers. Credit, on the other hand, may view the agenda as primarily ensuring that the company gets full payment for all orders. Those responsible for inventory management are, of course, interested in facilitating good inventory management, reducing inventory costs, etc., while those responsible for shipping are interested in ensuring good routing of trucks to minimize delivery costs. So if we were to think of the purpose of order processing from a group perspective, we would likely end up with a design criteria that would focus on improving prompt, correct delivery of orders to customers while ensuring credit integrity and facilitating good inventory management, and good routing and scheduling of shipments.

It is difficult to achieve this overall perspective if each manager is interviewed individually. A case study illustrates the need for joint application design from a cross-functional perspective. A direct mail catalogue company was revising its information systems. Prior to the cross-functional design, the credit department viewed its primary goal as ensuring payment from customers. Ideal performance would be for all customers to make all payments—that is, no credit losses. In an effort to increase its performance in this area, the credit department had continually requested more and more information about customers, i.e., credit references, credit bureau checks, etc., to the point that credit costs were becoming excessive.

Two mistakes can be committed in making a credit decision. The first is to give credit to people who will not pay their bills, and the second is not to give credit to people who would pay their bills. After looking at the problem cross-functionally with joint application design, the organization determined that it was better off not doing any credit checks at all. This rather counter-intuitive conclusion was based upon two key understandings that were generated from the joint application design. First, the company could send catalogues of only low-priced items to first-time customers. Customers who paid for what they ordered could be upgraded to more expensive catalogues. Those customers who did not pay would, of course, be dropped from any future mailings.

In this way, the company was not inferring whether customers would pay from credit reference material; they knew for a fact, based on their own experience, which customers would and would not pay. It turns out that their losses from not receiving payment were less than what doing all the credit checks were costing them. In other words, the cost of merchandise not paid for was the cost of determining whether someone would pay. This information was not only more accurate, but it was also less costly than doing the traditional credit reference checking. If credit information requirements had been determined without considering the context of sales management, this insight would not likely have been achieved.

Furthermore, it turns out that people who would generally be categorized as higher credit risks have a greater propensity to purchase this company's catalogues. Conversely, people who would be considered excellent credit risks tend not to buy anything from their catalogues. This means the company could send out a lot of catalogues to people with excellent credit ratings and seldom make a sale. Therefore, it would be losing money by shipping catalogues that never generate any revenue. The company would be better off marketing to those people who would be higher credit risks but not letting them buy anything expensive until it was established that the customer would, in fact, pay for things ordered.

Without the perspective provided by a joint application design, it would have been difficult for credit to accept that credit checks were not functional to the overall process of making sales and processing orders. Therefore, when determining information requirements, all affected functions should be represented in the same room at the same time.

## Structured Interview

The third mistake made in determining information requirements is that the designers usually ask the wrong question: "What information do you need from the new system?" Though this is the obvious question, it is not at all helpful to managers attempting to determine what information they need. Systems analysts assume managers surely know what information they need. The executive assumes the systems analyst knows what he or she is doing. The problem is that this technique is akin to a psychoanalyst talking to a patient lying on a couch and asking, "What type of therapy do you need?" Or a salesperson being an order taker, rather than a problem solver, who asks, "What features do you want?" If patients or customers don't know how to look out for themselves, they are unlikely to get satisfactory solutions.

A personal story illustrates this point: When I moved to Minnesota, I purchased a home in the country with sufficient land to require a tractor mower. I set out to purchase a tractor mower, not knowing much about tractor mowers, other than that I wanted a Toro. (The dean of our business school was the former chief executive officer of Toro, and I wanted a Toro in my garage—just in case.) Consider me a manager who needed to solve a problem but didn't know specifically what his requirements were.

When I went into a dealership to purchase a tractor mower, the salesperson would ask me what I was looking for. I would say I was looking for a Toro tractor mower. After that I would find myself in trouble. The next question I would typically be asked was what blade width I wanted. This was not a question I was really prepared to answer. When I told the salesperson this, I could see him roll his eyes as if to say, "I hate these idiots who don't know what they're doing."

Next he would ask how much horsepower I wanted. "How much can I get?" I would respond. He would say "five to 18," as he rolled his eyes again. Then he would ask such questions as, "Do you want wide tires, narrow tires, a rear bagger, a side bagger, manual start or electric start?" It turned out the tractor mower would cost between \$800-\$2,800, depending on how it was configured. Ideally, I would like not to over or under buy. Once the salesperson realized I did not know what I was doing, he would immediately start pushing the \$2,800 unit, suggesting I should go first class. Mowing my yard and first class are not two concepts I associate with one another. Suspecting that I was being oversold, I would go to other dealerships. Unfortunately, I encountered the same experience, time after time.

Finally, I went into a dealership where the salesperson was not an order taker but a problem solver. He did not ask what features I wanted on the lawn mower. He asked other types of questions such as, "How big is your yard?" My yard was about an acre. Next he asked, "How steep is your yard?" I told him it had a gradual slope. He next asked, "What is the terrain like?" I told him it was natural, lumpy in spots. He wanted to know if I had fences or trees. I replied yes, a fence and about 80 trees. Next he wanted to known if I wanted my wife to use the tractor mower. I said, "Are you kidding? This is her anniversary present!"

With that information, he walked over to a tractor mower unit and said, "This is the one you need." I said, "How much?" He said, "Eighteen hundred dollars." Well, that was better than \$2,800. I asked him why this particular unit. He said, "You have a large yard so you want the widest blade. You need 12 horsepower to drive the widest blade, but you do not need 18 horsepower unless your yard is both big and steep. You want wide tires to keep them from slipping into a rut, tilting the blade deck and scalping the yard; you want a rear bagger so you can mow around the trees and mow by your fences one way one time and the other way the next time so you do not pack the grass; and you want electric start because you've got delusions you are going to get your wife to use it!"

Notice that what he did was extremely simple. He asked indirect questions that backed into my requirements. He never specifically asked what features I wanted.

This use of indirect questions is the creative skill of the problem solver in sales versus the order taker. Problem solvers creatively determine how to obtain answers to requirements through less obvious, indirect questions. Those designing information systems need to do the same, and executives should request they do so.

A straightforward, useful approach to interviewing executives (instead of simply saying “what information do you need?") to determine information requirements has been developed through research done at the MIS Research Center at the University of Minnesota (Wetherbe, 1988). The technique is based upon three different requirement/determination methodologies, defined in Table 2. By combining questions from these three different methodologies, a comprehensive, reliable determination of conceptual information requirements can be achieved.

Before conducting the interview, an agreement of the overall purpose of the business activity must be established in a joint application design fashion. For example, for the order processing system discussed earlier, the objective of the system could be to ensure prompt, correct delivery of orders to customers, maintain credit integrity, facilitate inventory management, and ensure good shipment routing and scheduling. Once this has been established, questions can be asked that determine what information is needed to ensure those objectives are accomplished. A basic model for the information requirements interview is portrayed in Figure 1. The notion is to focus on issues that “back into” information requirements. The specific questions asked are as follows:

## Business systems planning (BSP)

(Source: IBM Corporation, 1984)

1. a. What are the major problems encountered in accomplishing the purposes of the organizational unit you manage?

For example, in an order processing system, problems include being out of stock too often, allocating limited inventory to the wrong customers, and sending off trucks unaware that another order going to the same destination will be arriving at the dock within an hour.

Table 2. Comprehensive Interview Approaches, Implementations, and Developers

<table><tr><td>Comprehensive Approach</td><td>Information System Implementation</td><td>Developers</td></tr><tr><td>Specify problems and decisions</td><td>The executive interview portion of Business Systems Planning (BSP)</td><td>IBM</td></tr><tr><td>Specify critical factors</td><td>Critical Success Factors (CSF)</td><td>Rockart</td></tr><tr><td>Specify effectiveness criteria for outputs and efficiency criteria for processes used to generate outputs</td><td>Ends/Means Analysis (E/M analysis)</td><td>Wetherbe and Davis</td></tr></table>

![](/api/attachments/87MTRRB5/fulltext/images/516f13dc65d3f9f72de91c69bc512a2c8cfd9e5dbc2b370c45aade3b6dcd98ff.jpg)  
Figure 1. Framework for Information Requirements Interview

## b. What are good solutions to those problems?

For example, to solve the problem of being out of stock too often requires better inventory management. To solve the problem of incorrectly allocating orders requires letting the warehouse know the importance of customers and the importance of orders to specific customers. It would also be helpful to know customer credit status. To solve the scheduling of truck departure problems requires letting shipping know the destination of orders that are being processed but have not yet arrived at the shipping dock.

## c. How can information play a role in any of those solutions?

For example, to improve inventory management, out-of-stock and below-minimum reporting could be provided electronically. Also, an automatic reordering system could be implemented. Electronic access to customer importance, importance of order, and credit status could allow the warehouse to make appropriate allocation decisions when inventory is limited. If the shipping department has access to orders received and in process, it can make better decisions over routing and scheduling trucks.

Table 3a provides an illustration of a structured interview using the problem/solution/information interview format.

## 2. a. What are the major decisions associated with your management responsibilities?

Major decisions for order processing include: which customers to call on and what to sell them? Credit for whom? How much? When to discontinue credit? What and how much inventory to stock? When to reorder? How to allocate limited inventory? How to schedule and route trucks?

## b. What improvements in information could result in better decisions?

Table 3b provides an illustration of a structured interview using the decision/information interview format.

## Critical success factors (CSF)

(Source: Rockart, 1979)

## 3. a. What are the critical success factors of the organizational unit you manage? Most managers have four to eight of these.

Table 3a. Requirements Interview for Order-Processing System: BSP

<table><tr><td>Problems</td><td>Solution</td><td>Information</td></tr><tr><td>Out of stock too often</td><td>Better inventory management</td><td>Out-of-sotck, below-minimum report; automatic reordering of inventory</td></tr><tr><td>Ordering department often allocates limited inventory to the least important customers and/or customers who have credit problems</td><td>Let warehouse department know relative importance and credit status of different customers</td><td>Customer-importance rating and credit rating</td></tr><tr><td>Shipping department often sends off a truck, unaware that another order going to the same destination will be coming to the dock within an hour</td><td>Let shipping department know the destination of orders that are being processed through credit and warehouse</td><td>Shipping destination of orders provided when orders received from customers</td></tr></table>

Table 3b. Requirements Interview for Order-Processing System: BSP

<table><tr><td>Decision</td><td>Information</td></tr><tr><td>Which customers to call on and what to sell them?</td><td>Customer-order history; inventory available</td></tr><tr><td>Credit for whom? How much? When to discontinue?</td><td>Credit rating; current status of account, payment history</td></tr><tr><td>What and how much inventory to stock?</td><td>Inventory on hand; sales trends on inventory items; market forecasts</td></tr><tr><td>When to reorder?</td><td rowspan="2">Priority of order; importance of customer; credit status of customer; shipping schedule</td></tr><tr><td>How to allocate limited inventory?</td></tr><tr><td>When to unload slow-moving inventory?</td><td>Sales trends</td></tr><tr><td>Destination of ordered inventory?</td><td>Customers&#x27; addresses</td></tr><tr><td>What orders can be shipped together to save delivery costs?</td><td>Shipping schedule and customers&#x27; destination for orders awaiting shipment</td></tr></table>

For example, critical success factors for order processing include: adequate inventory to fill customer orders, prompt shipment of orders, high percentage of customer payments made, and vendors (suppliers) promptly filling reorders.

b. What information is needed to ensure that critical success factors are under control? For example, to determine if adequate inventory is available, management would need summary and exception reports on percentage of orders filled on time. In addition to overall reports, they should also be categorized by customer and product. To determine if orders are being shipped promptly, management would need to have summary and exception reports on delivery time—both overall reports and reports categorized by customers.

Table 4 provides an illustration of the critical success factor/information interview format.

Table 4. Requirements Interview for Order-Processing System: CSF

<table><tr><td>Critical Success Factor</td><td>Information</td></tr><tr><td>Adequate inventory to fill customer orders</td><td>Percentage of orders filled on time—overall and also categorized by customer and product</td></tr><tr><td>Prompt shipment of orders</td><td>Delivery time—overall and also categorized by customer</td></tr><tr><td>High percentage of customer payments</td><td>Delinquency report on non-paying customers</td></tr><tr><td>Vendors (suppliers) promptly fill reorders</td><td>Exception report of vendor reorders not filled on time</td></tr></table>

## Ends/means (E/M) analysis

(Source: Wetherbe, 1988)

4. a. What is the end or good or service provided by the business process?

b. What makes these goods or services effective to recipients or customers?

c. What information is needed to evaluate that effectiveness?

Table 5a provides an illustration of the ends/effective/information interview format.

5. a. What are the key means or processes used to generate or provide goods or services?

For example, means for order processing include processing orders, processing credit requests, and making shipments.

b. What constitutes efficiency in the providing of these goods or services?

For example, efficiency for order processing pertains to achieving low transaction costs for orders and credit checks. It would also pertain to minimizing shipment costs.

c. What information is needed to evaluate that efficiency?

Examples of information needed to assess efficiency include cost per transaction with historical trends, cost per credit transaction with historical trends, and shipment cost categorized by order, customer, region, and revenue generated.

Table 5b provides an illustration of the means/efficiency/information format.

The method of using these three methodologies as a basis for indirect questions for obtaining a reasonably correct and complete set of information requirements is both simple and powerful. It is simple because it consists of simple components that can be learned by an analyst and a manager in a relatively short time. It is powerful because it is based on fundamental theories of human information processing and human strengths and limitations. It provides a comprehensive set of approaches that are additive in their results.

The interview has a redundant “safety net” built into it. For example, note that a problem identified in the first set of questions in the example pertains to poor allocation of limited inventory to customers (see Table 3a). The need to allocate limited inventory was also identified as a decision that must be made (see Table 3b). In other words, if the concept of allocating limited inventory was not recalled as a problem, it can still be identified as a decision, and vice versa. This “safety net” effect greatly increases the reliability of the structured interview.

Note that what is generated from the interview is a profile of conceptual types of information necessary to support an order processing system. For example, the first item in the information column in Table 3a says "Out-of-stock, below minimum report." This could be the title of a screen or report. The next item in Table 3a is "automatic reordering of inventory," which is a function needed from a new system.

At this point, we need to take these conceptual ideas and progress to the stage of detail design.

Table 5a. Requirements Interview for Order-Processing System: E/M Analysis

<table><tr><td>Ends</td><td>Effective</td><td>Information</td></tr><tr><td>Fill customer orders</td><td>Customer orders delivered as ordered, when expected, and as soon or sooner than competition</td><td>Summary and exception reports on customer deliveries; number of order corrections made; comparative statistics on delivery service vs. competition&#x27;s</td></tr><tr><td rowspan="3">Provide customer service</td><td>Promptly provide credit to qualified customers</td><td>Customer credit status and payment history</td></tr><tr><td>Quick response to and reduction of customer complaints</td><td>Report of number and type of complaints by customers and average time to resolve complaint</td></tr><tr><td>Customers are satisfied</td><td>Customer attitudes toward services perhaps determined by customer surveys</td></tr></table>

Table 5b. Requirements Interview for Order-Processing System: E/M Analysis

<table><tr><td>Means</td><td>Efficiency</td><td>Information</td></tr><tr><td>Process orders</td><td>Low transaction cost</td><td>Cost per transaction with historical trends</td></tr><tr><td>Process credit request</td><td>Low transaction cost</td><td>Cost per transaction with historical trends</td></tr><tr><td>Make shipments</td><td>Minimize shipment costs</td><td>Ship cost categorized by order, customer, region, and revenue generated</td></tr></table>

This is where mistake number four is normally made.

## Prototyping

The fourth mistake that is typically made in requirements determination is that managers are not allowed to determine and refine their conceptual requirements into detail information requirements through trial and error. Detail requirements refer to the specific screens or reports that are generated by a system, as illustrated in Figure 2.

Trial and error, or experiential learning, is an important part of problem solving. For example, people are using trial and error when they

\- Try on clothes before they purchase them

\- Test-drive cars

\- Change their college major after a few courses

\- Have several relationships before marriage

\- Rearrange furniture several times when decorating a room

\- Put more than one nail hole in a wall when hanging a picture

Trial and error is also a part of determining detail information requirements. It can be incorporated into the system design process through the use of a prototype or mock-up of the system. Using state-of-the-art technology, a prototype of a new system can usually be constructed in a day to a couple of weeks, depending on the complexity of the system (Wetherbe, 1988). As in manufacturing, much can be learned about final requirements through a prototype before “building the new factory.” A model of prototyping is provided in Figure 3.

![](/api/attachments/87MTRRB5/fulltext/images/c55f783382e6163322e2ff381547f9ea1bfadd24d06d6769b66076149f5f75ce.jpg)  
Figure 2. From Conceptual to Detail Reporting Specification

Conceptual analysis through a structured interview prior to the trial-and-error process can substantially reduce the amount of time expended to resolve the solution. For example, in the five preceding situations, the following analysis, prior to trial and error, could save time:

1. A fashion consultant could narrow the trial-and-error search for a new wardrobe by asking questions about career, lifestyle, budget, and taste, and by observing physical characteristics. Stores and designs could be suggested based upon the answers to these questions, thereby saving search time.

2. A well-trained car salesperson could ask qualifying questions (similar to those of the fashion designer) to better suggest automotive alternatives.

3. A career counselor, based upon interviewing, could suggest majors for students.

4. A marriage counselor could use personality and interest profiles to assist in determining the compatibility of potential marriage partners.

5. Interior decorators could use their analysis techniques to approach a decorating solution that could be refined by trial and error.

As in these examples, the structured interview prior to a trial-and-error process reduces the time necessary to determine detailed requirements.

Unfortunately, over the years, systems analyses have not incorporated a learning, trial-and-error process into systems design. Equally as troublesome is that they either agree to or have imposed upon them by management a budget and schedule for a new system before there is a prototype. This is naive. If the schedule and budget are set, the only thing left to maneuver around is the content of the deliverable. Accordingly, systems analyses often leave useful or even critical functionality out of a system in an effort to stay within budget and on schedule.

![](/api/attachments/87MTRRB5/fulltext/images/dbbc17becb4d00601733618ef930c68dffd45ae6e976b9d8d2315a82207e12da.jpg)  
Figure 3. Model of Prototyping

Consider this analogy: Have you ever moved to a new city where you had to purchase a new home? Did you have a price in mind and a desired date to move in before you began your search? Were you able to keep to the original price and schedule or did you need to adjust to meet your requirements? Often you looked at houses (prototyped) and saw the ones you really wanted. What would have happened had you forced someone to meet your housing requirements within the original price and schedule you started with?

Management should not let systems analysts disappear after the initial concept for the system is established. Management should be able to observe and experience a prototype within two to five days after being interviewed. This prototype can then be shaped into a final design within a few weeks.

Once management accepts the prototype, a realistic schedule and budget can be established for building the system. Although systems must evolve over time and should be built with evolution in mind, a system that is initially “right” will not need substantial immediate modifications. Evolutionary change of such a system is therefore much more manageable.

## Conclusion

More correctly determining information requirements is a key productivity issue, both for systems and for managers who need better information for decision making. Failure to get the requirements “right the first time” wastes human and economic resources. Management can greatly enhance the correct determination of information requirements by encouraging their systems designers to use a cross-functional, joint application design that involves input from all key decision makers involved in the business process. The conceptual requirements for a new system can be determined by a structured interview. Detail requirements can then be identified through prototyping. Then the best source of information—be it formal or informal—can be determined.

## References

Ackoff, R.L. "Management Misinformation Systems," Management Science, December 1967, pp. 147-56.

Benbasat, I. and Schroeder, R. G. "An Experimental Investigation of Some MIS Design Variables," MIS Quarterly (1:1), March 1977, pp. 37-47.

IBM Corporation. Business Systems Planning, Publication No. GE20-527, Revision 4, July 1984.

Jenkins, A., Naumann, D., and Wetherbe, J. C. "Empirical Investigation: Systems Development Practices and Results," Information and Management (7:2), April 1984, pp. 73-82.

Judd, P., Paddock, C., and Wetherbe, J.C. "Decision Impelling Differences: An Investigation of Management by Exception Reporting," Information and Management (4:5), November 1981, pp. 259-267.

Rockart, J.F. "Chief Executives Define Their Own Information Needs," Harvard Business Review, March-April 1979, pp. 81–93.

Weatherbe, J.C. Systems Analysis and Design, West Publishing Company, St. Paul, MN, 1988.

## About the Author

James C. Wetherbe is professor of management information systems and director of the MIS Research Center of the Carlson School of Management at the University of Minnesota. He is the author of 12 books in information management and systems design. He has completed extensive research and consulting in the area of information systems development.
