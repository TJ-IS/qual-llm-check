---
otero_id: 17836
otero_key: "Q6NDHQRC"
title: "An on-line customer information system at a gas-utility company"
authors: "Hirohide Hinomoto"
year: "1979"
journal: "Information & Management"
doi: "10.1016/0378-7206(79)90007-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An On-Line Customer Information System at a Gas-Utility Company

Hirohide Hinomoto

Department of Business Administration, University of Illinois, Urbana, Illinois 61801. USA

Since about 1970, there has been a significant trend among large organizations in moving from a manua' system or semiautomatic system that first prepares source data and then processes it in a batch environment to an online automatic system that receives and processes data entered directly at the office. This paper describes the course of events during the development of such an on-line system that processes customer orders at a large gas utility company. One significant outcome of the conversion from the previous manual system to the on-line system was a large reduction in the work force required for processing customer orders; this resulted in great savings in labor and material costs.

Keywords: System Planning, Conversion to an On-Line System, Customer Order Processing, Organizational Effects of Computing.

![](/api/attachments/Q6NDHQRC/fulltext/images/453c3e2b15955293af3463fce3e5d10796fb602a6ccc4a6f91d7cdb20fae1a78.jpg)

Hirohide Hinomoto is Associate Professor of Business Administration at the University of Illinois, Urbana-Champaign, Illinois 61801. He has received a Ph.D. in Industrial Engineering from the University of Michigan in 1963. His current research interest is in capital capacity analysis, long-range planning, analysis and design of a management information system, and effects of an informaty system on an organization.

## 1. Introduction

The first wave of office automation was caused by the introduction of the first generation of commercial computers in the mid-1950s. It consisted of conversion of repetitive clerical work to computerized systems operating in a batch processing environment, eliminating much of the clerical personnel engaged in simple calculations and report production [10,15,16]. In the computerized environment, most clerical personnel engaged in the preparation of source documents that were later converted to punched cards used as computer inputs. A few studies documented in detail the impact of such conversion on an organization [7,9].

In the early 1960s such authors as Malcolm [8] and Sprague [14] predicted the practicality of an online real-time system for organizational information processing that would allow office personnel directly to put transactions into the computer files through an on-line terminal. Later, when several such systems for special purposes were actually developed, their characteristics were more specifically described [2,4], and case studies describing detailed accounts of their development became available (see, for example, [3 (150-17t),11,12,16]).

Since the late sixties, many large organizations have been engulfed in what may be called the second wave of office automation, this time, converting existing batch processing systems to on-line real-time systems for organization-wide purposes. The conversion efforts have been stimulated by the advent of generalized data base management systems (DBMSs) that allow the concurrent use of common data bases by different applications. Papers describing the technical aspects of a system with a DBMS are numerous, but detailed case studies on the development of such a system are limited (see, for example, [1,5,6,13]).

This paper discusses the impact of conversion from a batch-oriented system to an on-line system with a DBMS on a large gas utility company. The company serves approximately one million families in a very large city. The system involves the Customer Relations Department of the Sales Division and the Field Service Department of the Service Division. The main functions of Customer Relations include receiving customer orders for regular or emergency field service, answering customer inquiries about monthly bills, and listening to customer complaints about services. Regular field service (about 85% of the work) includes meter connections and disconnections usually performed on the day following the receipt of an order unless a later date is specified, whereas emergency field service involves the same day work on disclosure of gas leaks and poor supply. Customer requests are normally initiated through the telephone, and received and processed by “business representatives” in the downtown main office.

Towards the end of the sixties, top management was considering a major improvement in the existing customer order processing system. Top management felt that the system was too slow in processing customer calls. Though the number of business representatives had steadily increased, they could not satisfy the company's goal of answering 90% of the calls within 20 seconds.

## 2. The existing system

In 1970, the existing system was staffed by 154 business representatives who processed about, 6,500 customer calls per day. These people were divided into 22 groups of seven who sat around a circular work station with a rotating file of 5" × 8" cards that contained customer information. A tape file containing current information was updated daily and used to print out new customer master cards (one station per night), taking about a month to update all the cards. In addition, each station was given a listing of daily changes in customer premise information.

Each block of customer account numbers was handled by a specific station having a unique telephone number. An incoming call was picked up by any free business representatives, but about half the customers dialed a wrong number. Misdialed calls were transferred by three switchboard operators.

On picking up a correct call, the business representative asked for name and account number, located the customer's master card and flagged its location. The business representative then processed the customer order by writing the customer name, address, and account number from the master card, the type of order, and the date and time on the appropriate form: a white form was used for regular orders, red for emergency.

Completed forms were placed on a conveyor to a station where a clerk separated them. Originals of emergency orders went to teletype operators who transmitted orders to field service shops. Originals of regular orders were accumulated until the end of the business, when they were sorted and forwarded to field service shops by messengers. Copies were sent to the computer center; these were keypunched and the cards batch processed daily to update the current order file.

## 3. Preliminary investigation

In 1970, a task force was staffed from members of the Customer Relations, Service, and System Development Departments. Its first task was to determine the extent of future computerization. It considered two approaches: first, to store the archival file of 7-year customer's history on microfiche and keep this file in a cabinet in the Customer Relations Department; second, to install online files. However, the task force was skeptical of the efficiency of a microfiche file because of slow retrieval of customer records.

During late 1970, the members of the taks force visited eight major gas and electric utility companies, four of whom had been utilizing an online customer order processing system for one to three years; the others were in various stages of operation, or conversion. However, none of these companies used a microfich file.

In early 1971, the task force submitted a report to the top management, recommending a detailed study on an online customer order processing system with the following requirements:

1. It should be capable of processing 400 customer

calls in a 15-minute peak-load period.

2. The response time from keyboard request to display should be 5 seconds or less under normal conditions.

Subsequently, the system study group was organized from managers of the Information Systems. Customer Relations, and Field Service Departments.

## 4. Analysis of call load

The systems study group first requested the Systems and Procedure Section to conduct a call load study to estimate the personnel required for the new system.

As the first step of this study, telephone call statistics for 1970 were obtained and charted daily. On average, the number of calls was greatest on Monday, dropped about 15% on Tuesday, and then gradually decreased through the week as follows: Monday (6590), Tuesday (5560), Wednesday (5410), Thursday (5390), Friday (5090). The daily call load varied substantially from month to month, e.g., see Figure 1. April was selected as an average month to be satisfied in designing the system.

As the second step, statistics were obtained on the number of calls in 15-minute intervals from 8:15 a.m. to 5:00 p.m. during 12 consecutive working days in the later part of April. Since only two of the 12 days being studied had a call load in excess of 7,000, it was concluded that a capacity of 7,000 calls a day would be satisfactory. Although the call load in 15-minute interval fluctuated, the business hours of the two days could be divided into three periods according to the average call load: the morning period (8:15 a.m.—12:00 noon) with about 250 calls per interval, the early afternoon period (12:00 noon—2:00 p.m.) with 220 calls or less, and the late afternoon period (2:00 p.m.—4:30 p.m.) with 190 calls or less.

As the third step, a time and motion study was performed. It found that an average time of 3 minutes was needed to process a call. This meant that a call load of 250, 220, or 190 calls per 15-minute interval needed a staff of 50, 44, or 38 business representatives. Main factors taken into consideration were: (1) the number of absentees (estimated as 10%), (2) the number of business representatives under a supervisor, and (3) the schedule for coffee and lunch breaks.

The total work force was to be divided into groups of from 15 to 25 people. Two 15-minute coffee breaks, in the morning and afternoon, and a 45-minute lunch break would be available as previously. One lunch period for a group would be in the morning peak period and two lunch periods for the remaining groups in the afternoon before 2 p.m. There would be a 15-minute overlap between consecutive breaks.

![](/api/attachments/Q6NDHQRC/fulltext/images/0ebb75df7b426e5aa717a73a730700b3ed10bcc0f8f01516f8962e277dcb3f62.jpg)  
Fig. 1. Daily Call Load on Mondays during 1970.

in the morning, peak-load period, no more than one group would be permitted to have a break at any time. The remaining personnel must satisfy the required number of 50. This is written as:

$$
E (n - 1) (1 - 0. 1) \geqslant 5 0,\tag{1}
$$

where E and n are the number of employees in each group and the number of such groups, respectively.

The personnel remaining at their stations in the early afternoon must be equal or greater than 44:

$$
\{E + \frac {1}{2} E (n - 1) \} (1 - 0. 1) \geqslant 4 4.\tag{2}
$$

The above conditions (1) and (2) were satisfied by an n of 4, and an E of 20. In this case, each group would have 18 people available for work, which would provide expected work force of 54 at work stations in the morning and 45 in the early afternoon period. The detailed schedule of breaks for four groups of 20 people are shown in Figure 2.

Thus, a total work force of 80 business representatives equipped with 68 CRT terminals could easily handle a call load of 7,000 requests a day. When the call load exceeds 250 calls per 15 minutes, the 20 CRT terminals provided for other departments of the Sales Division could be mobilized to assist the 68 CRT terminals in the Customer Relations Department. The total of 88 terminals thus available might easily handle a load in excess of 400 calls per 15 minutes, equivalent to a total load of 10,000 calls a day.

## 5. A proposed system

The proposed system was to be designed to enhance the efficiency of processing a customer call and to satisfy the previous requirements, incorporating the following new features:

![](/api/attachments/Q6NDHQRC/fulltext/images/0690872a181fb48cfd3d485ffda1bdf962814895a09e7f0b0532b15c062d457d.jpg)  
Fig. 2. Call Load, Work Force, and Schedule of Breaks.

1. One phone number was to be assigned to all business representatives independent of the customer and service.

2. The business representative was to have direct access to customer premise and account data from an online file.

3. The business representative was to enter the order directly into the information system.

The business representative was to have direct access to current customer payment data via two files; one containing payment data for the past 12 months, the other for the past seven years.

In the new system, all incoming calls will be received by an automatic call distributor with a queue of 100 slots. By entering new data, automatic validity checks could be made, and errors displayed on the screen for immediate correction by the business representative. By entering customer orders directly into the online file, time and costs would be reduced. Further, by providing more ways to identify the customer than the account number, the retrieval of a record could be faster.

## 6. Economic feasibility of the proposed system

Clerical efficiency as well as labor saving was the primary objective of office automation. Other objectives included equipment saving, space saving, time saving, greater accuracy, and new information [15]. As objectives of the current office automation, various authors cite fast response to an inquiry, data integrity, operational efficiency due to the elimination of data redundancies in different files, etc. However, many business firms including the gas company still insist on seeing tangible cost savings, whether it is in batch processing or on-line real-time processing.

The system study group made a detailed study on the economic feasibility of the new system. The summary costs of the proposed system are given in Table 1, whereas Table 2 gives a more detailed cost/benefit analysis of the system.

Of the capitalized costs, the purchase price of computer equipment was the price of the RCA SPECTRA 70 Model 6, representing the present value of an annual lease expense of \$484,200, discounted at a rate of 8%, under a full-payout lease for a period of 6 years (after which the firm would have ownership). Thereafter, the company would have a significant additional savings. The RCA computer was selected to duplicate current hardware and to facilitate backing up the on-line system in case of emergency. Ironically, however, RCA announced its withdrawal from general purpose computer business a few months after the feasibility study was submitted.

The system development cost consisted mostly of

## Table 1

<table><tr><td colspan="2">1. Capitalized Costs</td></tr><tr><td colspan="2">(1) Capital Equipment and Installation Costs:</td></tr><tr><td>a. Computer equipment</td><td>$ 2 258 400</td></tr><tr><td>b. Computer equipment installation</td><td>122 000</td></tr><tr><td>c. Office room renovation</td><td>574 000</td></tr><tr><td>d. Furniture and training equipment</td><td>65 000</td></tr><tr><td>Total Capitalized Cost</td><td>$ 3 019 400</td></tr><tr><td colspan="2">(2) System Analysis and Development Costs:</td></tr><tr><td>Salaries of programmers and systems analysts</td><td>1 215 000</td></tr><tr><td>Total Initial Investment Cost</td><td>$ 4 234 400</td></tr><tr><td colspan="2">2. Annual Operating Expenses:</td></tr><tr><td>(1) Decrease in labor expenses (94 employees)</td><td>$ 1 186 000CR</td></tr><tr><td>(2) Decrease in supplies expenses</td><td>104 000CR</td></tr><tr><td>(3) Increase in computer expenses</td><td>123 192</td></tr><tr><td>Net Decrease in Operating Expenses</td><td>$ 1 166 808CR</td></tr></table>

Table 2. Cost/Benefit Analysis of the Proposed Online System

<table><tr><td colspan="3">I. Capitalized Facility Costs</td></tr><tr><td colspan="3">1. Computer Equipment Costs</td></tr><tr><td>a. Computer Mainframe1</td><td>$ 2 238 400</td><td></td></tr><tr><td>b. Disk Packs</td><td>20 000</td><td></td></tr><tr><td>Total Computer Equipment Cost</td><td></td><td>$ 2 258 400</td></tr><tr><td colspan="3">2. Installation Costs</td></tr><tr><td>a. Telephone Equipment</td><td>$ 20 000</td><td></td></tr><tr><td>b. Terminal Equipment</td><td>40 000</td><td></td></tr><tr><td>c. Computer Mainframe</td><td>18 000</td><td></td></tr><tr><td>d. Conduit and Electrical Wiring</td><td>44 000</td><td></td></tr><tr><td>Total Installation Cost</td><td></td><td>$ 112 000</td></tr><tr><td colspan="3">3. Remodelling Costs</td></tr><tr><td>a. Customer Service Department</td><td>$ 74 000</td><td></td></tr><tr><td>b. Data Processing Center</td><td>500 000</td><td></td></tr><tr><td>Total Remodelling Cost</td><td></td><td>$ 574 000</td></tr><tr><td colspan="3">4. Other Capital Costs (Customer Service Department)</td></tr><tr><td>a. Furniture</td><td>$ 55 000</td><td></td></tr><tr><td>b. Training Equipment</td><td>10 000</td><td></td></tr><tr><td>Total Other Costs</td><td></td><td>$ 65 000</td></tr><tr><td>Total Capitalized Cost</td><td></td><td>$ 3 019 400</td></tr><tr><td colspan="3">II. System Development and Implementation Labor Costs</td></tr><tr><td colspan="3">1. Customer Service Department</td></tr><tr><td>a. System Design, Documentation and Testing</td><td>$ 160 000</td><td></td></tr><tr><td>b. Training (180 Employees at 60 hours each)</td><td>70 000</td><td></td></tr><tr><td>Total Customer Service Department Labor</td><td></td><td>$ 230 000</td></tr><tr><td colspan="3">2. Information Systems Department</td></tr><tr><td>a. System Analysis and Design</td><td>$ 419 000</td><td></td></tr><tr><td>b. Program Development</td><td>358 000</td><td></td></tr><tr><td>c. Keypunch and Clerical</td><td>43 000</td><td></td></tr><tr><td>d. Conversion and Implementation</td><td>87 000</td><td></td></tr><tr><td>e. Testing</td><td>12 000</td><td></td></tr><tr><td>f. Past Implementation Study</td><td>43 000</td><td></td></tr><tr><td>Total Information Systems Department</td><td></td><td>$ 962 000</td></tr><tr><td colspan="3">3. Field Service Department</td></tr><tr><td>a. Training</td><td></td><td>23 000</td></tr><tr><td>Total System Development and Implementation Cost</td><td></td><td>$ 1 215 000</td></tr><tr><td colspan="3">III. Annual Operating Costs</td></tr><tr><td colspan="3">1. Decrease in Labor Costs</td></tr><tr><td>a. Customer Service Department</td><td>$ 1 053 000CR</td><td></td></tr><tr><td>b. Data Processinf Center</td><td>113 000CR</td><td></td></tr><tr><td>Total Decrease in Labor Costs</td><td></td><td>$ 1 186 000CR</td></tr><tr><td colspan="3">2. Decrease in Supplies and Equipment Costs</td></tr><tr><td>a. Forms Costs</td><td>$ 43 000CR</td><td></td></tr><tr><td>b. Telephone Costs</td><td>58 000CR</td><td></td></tr><tr><td>c. Teletype Costs</td><td>5 000CR</td><td></td></tr><tr><td>d. Keypunch Rental Costs</td><td>12 000CR</td><td></td></tr><tr><td>e. Microfilm Costs (COM)</td><td>14 000</td><td></td></tr><tr><td>Total Decrease in Supplies Costs</td><td></td><td>$ 104 000CR</td></tr><tr><td colspan="3">3. Increase in Computer Costs</td></tr><tr><td>a. Computer Maintenance Costs</td><td>$ 79 692</td><td></td></tr><tr><td>b. Sales and Personal Property Taxes $^{2}$ </td><td>43 500</td><td></td></tr><tr><td>Total Increase in Computer Costs</td><td></td><td>$ 123 192</td></tr><tr><td>Net Decrease in Annual Operating Costs</td><td></td><td>$ 1 166 808CR</td></tr></table>

Note: 1. This is the present values of an annual lease payment of \$ 484 200 for 6 years, discounted at a rate of 8%.  
2. The sum of an average annual sales tax and an estimated and personal property tax paid over six years is averaged over a system life of eight years.

salaries to programmers and system analysts over a two-year period. The capital equipment and installation costs of the system would be capitalized over 8 years, an estimate life of the system.

The new system was expected to realize savings by a net reduction of 79 employees with an average wage rate of \$4.74 per hour in the Customer Relations Department, 14 keypunch operators with an average rate of \$3.20 per hour, and one control clerk with a rate of \$4.97 per hour in the computer center. In general, the hourly rate was increased by 35% to cover fringe benefits. On the basis of cash flows without discounting, the initial investment was recovered by annual savings in 3.6 years. This payoff period became approximately 4.5 years when the annual cash flows were discounted at a rate of 8%, the rate used by the company to evaluate all capital projects.

In August 1971, the system study group presented their proposal. Top management was sufficiently impressed by the profitability of the proposed system, as well as the non-economic advantages associated with improvements in customer services:

1. The simpler customer procedure and quicker response due to the use of only one phone number.

2. The faster response because of the use of the online customer file and the better data due to the instant verification of keyed in data.

3. The better response to emergency orders, which are to be automatically transmitted to respective field service shops, and printed out by on-line printers.

4. The elimination of duplicate orders, which were created because it was virtually impossible to match new against previously received orders. These duplicate orders would be eliminated by having the computer match new orders against pending orders.

The breakdown of the 94 people being replaced is given in Table 3.

The reduction of 51 business representatives was expected from improved telephone call processing, reduced time in retrieving the customer records, and the elimination of the manual order form. The reduction of 25 clerks in the Sales Division was from the

## Table 3

<table><tr><td colspan="2">1. Customer Service Departments</td></tr><tr><td>a. Business Representatives</td><td>51 persons</td></tr><tr><td>b. Business Representative Trainees</td><td>3</td></tr><tr><td>c. Cler&#x27;s in Memo Group</td><td>6</td></tr><tr><td>d. Cler&#x27;s in Review and Dispatch Group</td><td>25</td></tr><tr><td>e. Clerk in Control Group</td><td>1</td></tr><tr><td>f. Telephone Switchboard Operators</td><td>3</td></tr><tr><td>g. Contingency Staff (increase)</td><td>(10)</td></tr><tr><td></td><td>79</td></tr><tr><td colspan="2">2. Computer Center</td></tr><tr><td>a. Keypunch Operators</td><td>14 persons</td></tr><tr><td>b. Control Clerk</td><td>1</td></tr><tr><td></td><td>15</td></tr></table>

elimination of manual processing of pending order forms, reviewing and batching of completed orders, processing of unposted order memos, teletyping of emergency orders, and handling of the present card file used for customer master information. The reduction of 3 telephone switchboard operators was from the reduction in telephone numbers. The contingency staff of 10 people would have to be created to fill the positions of business representatives absent or on break.

At the computer center, the existing system required 14 keypunch operators. These people would not be needed because business representatives would key in the data. The elimination of batch posting of customer orders and associated processing would also help in releasing one of the control clerks.

The elimination of these posts was the greatest concern of top management. The task force estimated that the main part of the reduction would be absorbed by natural attrition during the system development phase of two years. Further, early retirements and reassignments of employees could accelerate the phasing out process. Thus, the reduction was considered to pose no particular personnel problem to the company.

## 7. Implementation of the new system

In the fall of 1971, the proposal was accepted and a system planning team was organized to analyze the existing system and design a new one. This team consisted of:

7 programmer/analysts,

1 method and procedure specialist,

6 members of Customer Relations Department,

1 member of Field Service Department.

About the same time, RCA announced that it was leaving the general purpose computer business. The sudden development forced the system study group to select alternatives to replace the two RCA computers. Subsequently, decisions were made to go to an IBM 370/155 in the following spring and to add an IBM 370/145 when the on-line system became operational. It was planned that the 155 would be used for the on-line system, and the 145 would be used for batch processing (but be switched in order to back-up the 155 in emergency). To control messages using common data bases, two IBM data base management systems were compared; these were IMS and CICS. CICS appeared to be much simpler to use and meet most requirements of the on-line system while IMS seemed to offer many unneeded features and required a higher memory overhead. The group chose CICS.

The development work lasted a little over two years, during which various modifications were made in the original design. In the summer of 1972, management made a formal announcement to the employees about the on-line customer service system. They then held a special meeting of the Sales Division employees to emphasize that the new system was essential for the improvement in processing customer calls and that no employee would be fired or laid off because of system conversion.

From the fall of 1972 through the spring of 1973, the training materials and standard procedures of the new system were developed. In the summer of 1973, the first group of 20 business representatives was placed in the two-month training program, this was followed by three more groups during the ensuing months lasting through the spring of 1974. Meanwhile, arrangements were made for voluntary early retirements and the transfers of some of the older business representatives to other jobs in the same division or other divisions.

By the early summer of 1974, the installation of new hardware and the development of new programs were completed. Subsequently, the new system, staffed by 20 business representatives, was placed in test operation in parallel with the old system for three months, during which a number of errors were corrected. In October 1974, the nuw system was placed in full operation, replacing the old.

In the new arrangement, business representatives were divided into four groups of 20 people each under one supervisor. These groups occupied an L-shaped floor space with a glass-peneled section in the corner. Each wing of the L-shaped floor was occupied by two groups in tandem. Members of each group sat in five rows of four people facing abreast the glass-peneled section. The glass peneled section, called the "control room", contained a machine that monitored telephne calls and indicated (through the light bulbs on its console) the number of customer calls in queue to be processed, the number of calls currently being processed, and the status of each station (whether it was switched on and processing a call, or waiting for a new call, or not switched on).

## 8. Post implementation observations

By July 1975, the on-line order processing system had been operating nearly nine months and new application modules had been added. The number of daily calls processed by the system had gradually increased from 7,000, to as many as 8,500 in May. To the bewilderment of everyone concerned, this increase seemed to have little effect on the number of telephone calls waiting in queue. A rationale given to the unchanged length of the queue was that a greater number of customers became impatient with a longer waiting time and left the queue.

Towards the end of June 1975, there was a surge in number of customer calls. As a result, almost 10,000 calls were processed daily. The surge was caused by a large number of inquiries about June bills that were received by customers who had elected a budget payment plan. These bills changed from the normal rate to compensate for the accumulated credits or deficits in payments. They tended to be high deficits because of two unforeseen events: (1) the spring of 1975 had been exceptionally cold, forcing most families to consume more gas than they had realized, and (2) the substantial rate increase approved by the state a few months earlier had affected the expected rate of original billing average. The sudden increase also contributed to a surge of delinquent accounts that had hirherto been slowly, but steadily, increasing because of the economic recession that started 1974. Almost 15% of the total customer calls were inquiries about bills or requests for an extension in payment date.

In July 1975, a survey was conducted to find the attitudes of business representatives toward the new system. Most of them had a stronger sense of accomplishment under the new system, because of their ability to handle as many as 10,000 calls a day. But they felt a strong psychological pressure to keep up with customer calls because of machine paced processing. Because of this, they thought that the on-line system was much more tiring than the manual system.

Some of the business representatives were critical of the new system; they felt that they were completely dependent on the automatic system and that the response time to an inquiry was too sensitive to the current workload. The response to a request at the terminal was about 5 second in normal periods, but it deteriorated with an increasing load, taking as long as 30 seconds in busy periods when a call load of around 10,000 was experienced. Such long response was too long a time to look at a blank CRT in anticipation of a message. As a result, some business representatives considered a system with a slow but predictable response time more desirable than a system with a fast but unpredictable response time, and thought the old manual system much more attractive!

To alleviate some of the above problems, management took a few measures in the fall of 1975. Against the original estimates shown in Figure 2, the call load in the morning period persisted through the early afternoon period perhaps because working customers called the gas company during their lunch time. Some ten students from a nearby college were hired on a part-time basis to staff the stations vacated by business representatives in lunch break between noon and 2:00 p.m. Since customer complaints or inquiries about bills usually lasted several times longer than service related calls, special business representatives without terminal were created to handle them exclusively. As a long-run measure of reducing work monotony, a job rotation program was instituted in which interested business representatives could perform clerical jobs for one week in each month. On the technical side, the area of main memory allocated to message processing was increased in order to enhance the number of messages simultaneously processed.

## Acknowledgement

The author wishes to acknowledge Dr. F.H. Sibley and referees for their helpful comments.

## References

[1] J.S. Blanchard, We Bet Our Company on Data Base agreement, Datamation, (Sept. 1974) 61–65.

[2] D.C. Carroll, Implication of On-Line Real-Time Systems

for Managerial Decision Making, in C.A. Myers, ed., The Impact of Computers on Management (MIT Press, Cambridge, 1967) 140–167.

[3] J.D. Gallagher, Management Information Systems and the Computer (American Management Association, New York, 1961).

[4] M. Greenberger, The Computer in Organizations, in C.A. Walker, ed., Technology, Industry and Man (McGraw-Hill, New York, 1968) 302–324.

[5] G. Hanish, The Introduction of IMS at Bayer's, GK10-600-0 (IBM World Trade Corporation, New York, (1973).

[6] G.E. Huhn, The Data Base in a Critical On-Line Business Environment, Datamation (Sept. 1974) 52–56.

[7] E.F. Huse, The Impact of Computerized Programs on Managers and Organizations: A Case Study in an Integrated Manufacturing Company, in C.A. Myers, ed., The Impact of Computers on Management, 282–302.

[8] D.R. Malcolm, Real-Time Management Control in a Large-Scale Man-Machine System, Industrial Engineering, (11) 2 (1960) 103–110.

[9] F.C. Mann and L.K. Williams, Observations of the Dynamics of a Change to Electronic Data-Processing Equipment, Adm. Sci. Q. (5) 2 (Sept. 1960) 217–256.

[10] W.R. Riche and W.E. Allen, Office Automation in the

Federal Government, Monthly Labor Statistics (83) 9 (Sept. 1960) 933–938.

[11] H. Sackman, Evolution of SAGE as a Prototype Man-Machine Digital System, in H. Sackman, ed., Computers, System Science, and Evolving Society (John Wiley & Sons, New York, 1967) 91–119.

[12] M. Sanders, Telefile—A Case Study of an Online Saving Bank Application, Communications of ACM (6) 12 (Dec. 1963) 708–712.

[13] Sandvik AB, A Tube Mill Production Control Information System Using IMS, GE15-6048-0 (IBM World Trade Corporation, New York, 1975).

[14] R.E. Sprague, Electronic Business Systems (Ronald Press, New York, 1962) 155–162.

[15] U.S. Bureau of Labor Statistics, Adjustments to the Introduction of Office Automation: A Study of Some Implications of the Installation of Electronic Data Processing in 20 Offices in Private Industry, with Special Reference to Older Workers, Bulletin No. 1276 (Govt. Print. Office, Washington, 1960).

[16] E. Weinberger, Experience With Introduction of Office Automation, Monthly Labor Statistics (83) 4 (April 1960) 376–380.

[17] E. Yourdon, Design of On-Line Computer Systems (Prentice-Hall, New York, 1972) 95–123.
