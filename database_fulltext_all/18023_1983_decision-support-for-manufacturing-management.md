---
otero_id: 18023
otero_key: "QKRY3F55"
title: "Decision support for manufacturing management"
authors: "Adam D. Crescenzi; Gary K. Gulden"
year: "1983"
journal: "Information & Management"
doi: "10.1016/0378-7206(83)90001-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision Support for Manufacturing Management

Adam D. Crescenzi and Gary K. Gulden

Index Systems, Inc., Five Cambridge Center, Cambridge, MA 02142, USA

Historically, information systems have been used to improve efficiency through such means as clerical automation, inventory status reporting and transactional processing systems. Today, however, to reduce costs, increase return on investments, and achieve competitive advantage, businesses need to have information systems that support managerial decision-making and result in improved effectiveness. To meet this requirement, new approaches are needed in order to define the right problem and work the problem right. By using such techniques as critical success factor analysis followed by a top down system development approach, developing systems through prototyping and using end-user oriented software, these needs can be met.

This article describes several company experiences of using a management systems planning and development process. This process in one company presented an opportunity to test the feasibility of developing an alignment between business goals and events critical to the success of the business. Management believed that to succeed in the future they must be forward thinking in their identification and use of information systems to improve managerial effectiveness. Their questions were "What should we do?" and "How should we do it?" By applying these techniques they were able to achieve outstanding results in a very short period of time.

Keywords: Decision Support Systems, Manufacturing Management, Critical Success Factor Analysis, Top-Down Development, Prototyping, End-User Oriented Software.

![](/api/attachments/QKRY3F55/fulltext/images/125311cf73283d259d5370e1f34c730f474b0aa107dcaf4ccb68b83fa4a02aa3.jpg)

Mr. Crescenzi is responsible for all business operations of Index's Management Systems Group. The activities of this group include Management Support Systems (MSS) consulting and development, and functionally oriented applications consulting across industries with particular emphasis on high technology, consumer products, energy-related, and service organizations. Mr. Crescenzi is also a member of the firm's Policy Committee.

Mr. Crescenzi has managed the successful planning and implementation of information systems in a number of manufacturing organizations. Before joining Index, Mr. Crescenzi served as the director of material and business analysis for Honeywell Information Systems' nationwide Logistics operation. In this position, he managed line operations including material control, inventory, purchasing, and strategic planning for spare parts inventory. As a systems manager with Honeywell, Mr. Crescenzi was one of the original developers and managers of the Honeywell "COSMIC" system, an online database-oriented system to support material control and purchasing.

Other previous positions include assistant data processing manager for the Bedford Labs operation of Raytheon; director of systems development for Transystems International; and management consultant for Corporate-Tech Planning.

![](/api/attachments/QKRY3F55/fulltext/images/5e3ee2b4e3fc7b8205d752130383930b0f68d91f47727b16ba05c22db822bb8a.jpg)

Mr. Gulden is the officer responsible for Index's practice in Management Support Systems (MSS). The MSS practice provides consulting, definition, planning, and implementation services for organizations that seek to improve management effectiveness through decision support systems, executive information systems, and end-user computing technology.

Before joining Index, Mr. Gulden had over 12 years of line and staff managerial experience at Exxon Corporation and Rensselaer Polytechnic Institute, in the areas of marketing and sales management, strategic planning, energy supply/demand forecasting, operations, troubleshooting, and the management of analytical staff organizations.

Mr. Gulden is a director and member of the Executive Committee of W.J. Cowee, Inc., a manufacturing and forest management company in upstate New York.

© Copyright. 1982 Index Systems, Inc.

## 1. Introduction

The increasingly volatile manufacturing environment of the 1980's is stimulating a demand among manufacturing managers for better information to support customer service, productivity, and cost control. As a result of this demand, the Decision Support System (DSS) has emerged from the ashes of Management Information System (MIS) failures to support decision-making by management in a business which finds itself "data rich" but "information poor."

In a typical multimillion dollar manufacturing firm today, annual data processing expenditures run between \$5 million and \$15 million. Of this amount, approximately 20% is spent on administration of the data processing department itself, 20% on developing new systems, and 60% on maintaining and enhancing existing systems. In most companies, systems that were installed in the past - production scheduling, MRP (Materials Requirement Planning), and inventory control - continue to use the largest percentage of the data processing resources. Most organizations feel the need to either improve, add to, or replace these basic systems due to technological advances in hardware and/or software.

In the past twenty years, there has been considerable investment in transaction processing systems designed primarily to perform clerical tasks more efficiently. As more and more data has been captured in the computer, managers have wondered, with increasing frustration, why it seems so difficult to access that data in a timely way to support managerial decision-making. The first attempts to satisfy this need were the so-called “Management Information Systems” (MIS) of the seventies. MIS often failed to satisfy the need because the MIS was often based on providing volumes of data that provided management with a “damage assessment of the operations” instead of information that would help him prevent the damage. The management information was a by-product, constrained by data which came out of the structured clerical tasks that had been automated.

More recently, a different approach has been used to satisfy management's need for information. The Decision Support System (DSS) differs from the Management Information System (MIS) in many ways, but the principal difference is that the design of DSS starts with the problem to be solved, while the design of MIS starts with the data available from the transaction processing system. The DSS approach is thus “top-down”; it starts with the decision maker and ends with the computer and data base.

Decision Support Systems are designed to support managers in making decisions in “semi-structured” tasks. Early work in the 1960’s by Michael S. Scott Morton [1], of M.I.T. Sloan School of Management and Thomas P. Gerrity [2], President of Index Systems, showed how computer systems could be designed to support those decisions where neither managerial judgment (because of the size of the problem or the computational complexity in solving it) nor a model (because the solution involves some judgment and subjective analysis) are adequate. They suggested that the area where most managers make decisions lay between the structured tasks (which could be solved by models – no judgment required) and the unstructured decisions, for which both judgment and data are needed. To support judgment, one needs information presented in a form relevant to the decision maker. That is the role of a Decision Support System (DSS).

A DSS design focuses on the creation of a tool for managers, retained under their control, that does not attempt to automate the decision process, predefine objectives, or impose solutions. DSS represents a natural evolution in computer applications, building on the mistakes of MIS and taking advantage of new technology.

## 2. Formulating a DSS Strategy

To satisfy management requirements for better information – rather than just more data – traditional investments in transaction processing and information systems must be redirected to develop and implement Decision Support Systems. Most industrial organizations have made their investments in inventory control, procurement, materials, and manufacturing systems. While operational personnel are well supported today by automation, managers are not. But the foundation upon which to build automated support for managers is in place. With good management systems definition and prototyping planning, companies can both improve existing information systems and benefit from investments in new systems. The following three steps have proven to be highly successful in determining future needs of management information systems; these can then be used to develop an action plan for the introduction of Decision Support Systems.

## 2.1. Assess Current Systems

An understanding of the strengths and weaknesses of present systems is the starting point for identifying where and how a DSS can utilize the current systems, and where systems must be replaced. In an EDP assessment, an evaluation is made of the characteristics and efficiency of all EDP activities, along with a review of the effectiveness of the company investment in these activities. Two things are notable:

First, the assessment should show what parts are working well and can be copied elsewhere. This assessment will also identify what is not working, so that it can be fixed – but it is better to concentrate on the winners than look for the losers.

Second, generalizations about user needs across multidivisional companies are usually dangerous. Most companies are in several “different businessess,” each of which has different needs for information systems. Inventory control is quite different in a growth-oriented customer service division than in a control-oriented profit maximizing division.

## 2.2. Look for New DSS Opportunities

In planning for management systems, a key is the prioritization of the areas where management needs support. Critical Success Factors (CSF) analysis, developed by John R. Rockart of MIT's Sloan School of Management [3], has proven to be a particularly effective tool for uncovering upper management information requirements. The methodology is based on interviews with managers to establish what factors they consider to be “critical” to the success of the business. Examples of Critical Success Factors are: product reliability, asset control, material procurement, delivery lead time, maintenance support, and pricing tactics. Identifying these factors is the first step in determining DSS opportunities. Often the existing information systems do not provide management with information needed to monitor these critical success factors. In many instances, there is no plan to provide such support, because the project backlog was derived by extrapolating from the past rather than forcing managers to work through what would really support their decision-making.

## 2.3. Develop The Information Systems Plan

Based on the assessment of current systems and the management information needs derived from the Critical Success Factors analysis, an information systems plan can be developed which will align management needs to future systems investments. There will be a reorientation of budget allocation toward DSS that may necessitate a reallocation of investments in the maintenance and replacements of transaction and operational systems to the management systems.

## 3. Example of Inventory Control

Using this strategy, one company developed and installed a DSS in six months. It is in an industry where the timely buying of materials from its suppliers and the alternate uses of its inventory are critical to the success of the business. All day long, suppliers and customers are calling the Vice President merchandising and the Vice President operations with orders for new goods, changes to existing orders, or offerings of materials to be bought at “bargain prices.” The key operational decision that must be made is: Should we buy this new material and can we use or reshape it for current or future customers’ needs?

The nature of the business requires that its top management remain current and fully abreast of the day-to-day details, with online interactive information on the following:

● Market environment business upturns and downturns

\- Quotation trends

● Daily sales

● Individual pricing decisions

● Deliveries and production schedules

A Decision Support System was implemented for these managers; it gave them access to information to answer the following (typical) questions:

● What did we last pay for this material?

\- Do we have inventory?

● What is the scrap factor?

● What has been paid in the past?

\- At what price have we sold this to any customer in the last few weeks?

● What are current inventory levels?

● Are we low in this type of material?

● Have we been high in the past? When? Why?

● What demand do we predict for the next two months?

● What is the current order demand?

\- When can we ship? Schedule? Test?

\- Which customer buys these materials?

● What is the price range?

● What customers look for bargains?

\- At what prices have we sold this item?

● What is the overall profitability of this product?

● What impact will the buy/sell have on sales volume? Gross margin? New margin?

Benefits of DSS at this company have been:

● Improved ability to evaluate purchases

● Improved ability to move inventory

\- Improved ability to cope with changes in orders and opportunities to buy

● Enhanced communication between senior management in the buying and selling function.

## 4. Other Examples

Another manufacturing company developed and installed a Decision Support System in less than four months. By evaluating product inventory and sales contract obligations, the system determined the optimum product output mix with the highest profit under the constraints of existing cost structures.

A major division of a leading multinational manufacturer developed a Decision Support System for the master scheduling function. As a result, the master scheduling meetings progressed from “gladiator warfare” to an environment where marketing, materials management, and production management personnel could model the implications of various alternatives and easily come to an agreement on the approach.

A multibillion dollar manufacturer of glass fiber products had attained the dominant position in its continually expanding market. While its sales and profits had increased annually in excess of twenty-five percent, the cost of goods sold cut into the profit increase by expanding at an even higher rate. Raw material costs as a portion of cost of good sold had risen disproportionately, inflating even more rapidly than other associated product costs. Recognizing the need to control these raw material purchasing costs efficiently, management focused on well-designed decision support tools for the purchasing managers to leverage the firm's fixed investment in data resources and information processing equipment. This Decision Support System was designed and implemented within an extremely tight timeframe and was expected to save the corporation in excess of \$1 million in its first-year of operation.

## 5. Decision Support Systems Design and Implementation

Decision Support Systems cannot be designed and implemented utilizing the traditional approaches to data processing and information systems. The people, the technology, the models, and design and implementation process must all be different. In particular, the manager must be personally active in the design of the system since it will be tailored to meet the unique information requirements.

A Decision Support System is as much a process as it is a product. Its purpose is to enable managers to explore various alternatives through an interactive personal dialogue with the computer, and users will invariably think of improvements as they gain experience with the system. For this reason, it is important to approach the development knowing that whatever is initially implemented will be changed. The objective is to put something in the manager's hands as soon as possible, so that management will realize the benefits of a support system long before it would under traditional system development methods. Then, as the manager gains experience with the system, changes can be made. In fact, our experience with these systems is that the tool shapes the user as much as the user shapes the tool.

Only in rare circumstances is it necessary to replace present systems to provide decision-support capabilities. Usually, DSS can be built in the "air space" on top of current systems, making use of the data, procedures, and tools that already exist. It is usually better to duplicate data or provide an alternative procedure for collecting the data necessary for the DSS than to risk the rebuilding of all the company's operational and transaction processing systems.

The implementation of the DSS should evolve by first constructing a prototype. The evolution of the system accomplished through a series of working prototypes, rather than through the extensive written specifications typical of traditional information systems implementation, has proven to be more meaningful to managers. This can usually be accomplished in less than six months which enables managers to evaluate feedback under actual operating conditions so that changes and improvements can be made before the system is finalized. The Critical Success Factors analysis results should be utilized to limit the scope of the model so that designers will not be tempted to create an overload of information.

## 5.1. Keys to Success

The four keys to success for Decision Support Systems in manufacturing are:

1. Defining the "right problem" for manufacturing decision support; i.e. the problem that has relevance and visibility for the manager.

2. The right participants are the persons who stand the most to gain from having the problems solved - i.e. the "owners" of the problem, and hence of its solution.

3. The right process is based on using prototyping and evolving the system at the pace of the "owner". Because decision support systems are really "mind support systems the pace of growth of the decision support system must be in sync with the owner's understanding.

4. The right tools in the form of end-user computing software and hardware. Fitting the right tool to the right problem is a crucially important task.

## 6. Summary

The specific contributions of a DSS will differ from company to company, but the common fundamental benefits are:

\- More effective managers who can spend more time in the evaluation, judgment, and intuitive processes, and less time gathering data.

\- More effective control of the changing business environment by enabling the company to operate in a proactive, rather than a reactive, mode.

Although successful managers may feel that they have identified their CSF's, established the measures to monitor those factors, and provided themselves with information systems to support their decision making, they have seldom adopted the notion of providing automated information systems directly to the decision-makers. There is a growing consensus that information resources will play a pivotal role in determining which manufacturing firms hold a competitive advantage in meeting the more intense challenges of the future. The key benefit from Decision Support Systems will be improved management effectiveness, the Critical Success Factor for manufacturing firms in the 1980's.

## References

[1] Peter G.W. Keen, Michael S. Scott Morton. "Decision Support Systems, An Organizational Perspective".

[2] T.P. Gerrity, "The Design of Man-Machine Decision Systems: An Application to Portfolio Management".

[3] John F. Rockart, "Chief Executive Define Their Own Data Need", Harvard Business Review (1979).
