---
otero_id: 18099
otero_key: "E4T8SQ8H"
title: "Microcomputer selection process for organizational information management"
authors: "Abraham Seidmann; Ami Arbel"
year: "1984"
journal: "Information & Management"
doi: "10.1016/0378-7206(84)90027-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Microcomputer Selection Process for Organizational Information Management

Abraham Seidmann and Ami Arbel

Department of Industrial Engineering, Faculty of Engineering, Tel-Aviv University, Tel-Aviv 69978, Israel

This paper presents a selection model based on the Analytic Hierarchy Process (AHP). The methodology uses relevant organizational needs, required operational support categories, and respective attributes of the proposed systems in a selection hierarchy. Deriving a priority structure associated with this hierarchy permits the systematic comparison of candidate systems, and thereby selecting the one that best suits the organization. The application of this model to the selection of an accounting information system is described. The methodology outlined in this paper has been used in several large organizations (insurance and industrial corporations) for selection of their “standard micro” (or mini) computer systems. These systems were installed for various decentralized applications.

Keywords: Accounting Information Systems, performance Evaluation, Microcomputer Selection, Analytic Hierarchy Process, Decision Theory, MIS design.

## 1. Introduction

The on-going computer revolution, driven primarily by the dramatic improvements in the price/performance ratio of processors and memories, has led to microcomputer business systems whose capabilities match those of previous generation minicomputers. These developments have resulted in new viable information processing and decision aids.

However, the benefits offered by the new generation of microcomputers present management with problems in their selection. The problem is particularly acute when none of the systems under consideration exhibits a clear dominance over its competitors. Possibly one system emphasizes technological capabilities, while another emphasizes software performance, and yet a third emphasizes service and reliability; obviously one should not judge the relative importance of those factors by measures devoid of projected organizational needs [8].

Many acquisitions of microcomputers are directed at "turn-key" systems (as oopsed to custom design at increased cost), where the complete installation is backed by one responsible vendor. In such cases, one has to evaluate several configurations proposed by various vendors [19]. While the direct acquisition costs of modern microcomputer systems may not be excessive, one should still exercise prudence, since installing and running an inappropriate management information system may have adverse results [6,14]. Systematic selection methodologies should, therefore, be developed and applied to these selection problems [18].

![](/api/attachments/E4T8SQ8H/fulltext/images/88c5f2764a1c9a76c078ca59475a336af892bab5db2233ac26031d1305bb9d08.jpg)  
Abraham Seidmann is a lecturer of Industrial Engineering at Tel-Aviv University, Tel-Aviv, Israel. He holds B.Sc and M.Sc degrees from Technion-Israel Institute of Technology and Ph.D in Industrial Engineering from Texas Tech University. He has published numerous papers on mathematical modelling, robotics and computerized production management.

![](/api/attachments/E4T8SQ8H/fulltext/images/773ac23ef30d7cdded6c6df9d81f05258832d21f3973636ae0ffc9d297763193.jpg)  
theory, optimization methods, decision analysis and strategic studies. He is a member of TIMS, ORSA & IEEE.

Recent publications treating the selection procedures of computers, and in particular of microcomputers, reveal the active interest in this problem $[5,9,25]$ . Early studies pointed to measurement of average execution time for several combinations of operations as a good indicator of the Central Processor speed $[20]$ . More recent research pointed out to other methods such as standard benchmark (sample) problems $[2]$ , analytic workload models and simulation techniques $[4,16]$ . These methods predict the anticipated system productivity over a wide range of workload parameters. In order to define performance, some attempts at formal, functional, analysis of information systems have also been made $[1]$ . Various arbitrary scaling or weighted factor methods have been used in computing a composite scale for computer system parameters $[10]$ . Other authors center on providing checklists and questionnaires as aids for the evaluation process $[9,20]$ . Organizational models treating the selection problem in the context of corporate planning are discussed in $[13]$ .

While many papers are treating the issue, no particular model has emerged as capable of dealing with the organizational, functional and technical facets of this diverse and complicated decision problem. This paper describes a decision framework for selecting a microcomputer system and, in particular, an accounting information system $[3,7]$ .

The selection procedure is based on the Analytic Hierarchy Process (AHP) developed by T.L. Saaty [15,17,23]. This particular methodology is used because one is basically interested in a value assessment of the deterministic decision factors rather than their utility. The latter can be provided, of course, through a multiattribute utility approach which accounts for risk attitude in decisions under uncertainty. The deterministic nature of the problem under consideration does not warrant the use of the utility approach. (For a recent comparison of these methodologies please consult [11] and [17]).

## 2. The Evaluation and Selection Model

A major problem in the selection of microcomputers is the assessment of tangible and intangible factors affecting their overall performance; these include such issues as vendor reputation, specific accounting needs, and information integrity. Microcomputer-based accounting information systems are characterized by a number of parameters describing performance levels and requirements for these systems. These parameters make up a checklist that prospective buyers should follow in arriving at an acquisition decision $[7,9,19]$ . Such a list is given in Table 1.

```csv
CPU & Main Memory
-Word size
-Basic Clock Frequency
-Add Time
-Operating System
-Memory Size
-Maximal Memory
Application Packages
-Operational Fit
-Software Versatility
-Required Memory
-Statistical Recordings
-Integrity
-Security Features
Diskette Subsystem
-Average Access Time
-Formatted Capacity
-Data Transfer Rate
Vendor's Support
-Software Maintenance
-Technical Trouble-Shooting
-Training
-Documentation
-General Reputation
-Implementation Assistance
Compatibility
-Hardware
-Software
Printer
-Technology
-Speed
-Quality
-Print Columns
-Ledger Cards
Special Features
-Wordprocessing
-Financial Spreadsheet
-Concurrent Printing
Production Measures
-Total Throughput
-Transaction Volume Load
-Peak Load Handling
-Benchmark Results
Data Channels
-Number of Channels
-Transfer Rate
-Type
Hard Disk Subsystems
-Type
-Average Access time
-Formatted Capacity
-Data Transfer Rate
```

Note, however, that the appearance of the various parameters in Table 1 does not indicate that they are all of equal importance in the overall selection. The relative importance of each element is dependent on the system's function it supports and it may vary from one category to another. These system functions include the accounting, operator, and data processing functions. Their relative importance is affected by the organizational structure and the specific needs. Therefore, one has first to identify and prioritize these needs. Next, one has to identify and prioritize the system function supporting these specific organizational needs. Only then, can one prioritize all the selection parameters of Table 1, based on their contributions to the system functions. After these selection parameters have been prioritized, a systematic comparison of candidate systems can be made leading to the selection of a system which dominates all the others in the weighted priority elements. The process is shown in Figure 1.

![](/api/attachments/E4T8SQ8H/fulltext/images/27bab9204c742f0d82679220e46e3d26ae8528c14e01e718c92552e7eb6bb25f.jpg)  
Figure 1: The Four Levels in the Selection Process.

The first level considers idiosyncratic organizational needs for accounting information system. Seven major system duties can be identified in Table 2. Accounts Receivable serves as the primary cash receipts system. The Accounts Payable and Payroll represent the major mean for cash disbursement in the organization. General Ledger forms the accounting, cost allocation, budget allocation and profitability control functions. The production management system is represented by the Inventory Control function. two other elements dealt with at this level are Income Tax Returns and Fixed Assets Accounting.

Level 2 deals with the System Functions Categories of Table 3. They are partitioned into three basic sets of functions. The applications of management controls, system development controls, hardware and software controls in the Accounting functions. They include various ways for transactions validation, report editing and balancing, along with the application and audit of controls. The Operator's functions include three major subsets; the first subset is the operational savings which stem from time savings and reduced clerical effort; the second subset includes improved customer service due to better reporting timeliness, enhanced account monitoring, and report quality; the third subset focuses on user-friendliness and ease of operation. The user's consideration and human factors engineering (ergonomics) aspects are grouped under relevant hardware and software aspects. The electronic data processing elements of data collection, classification, manipulation, reduction, storage etc., are all included in the final set of functions in the system functions. The Data Processing functions refer to data entry, masterfiles update, the generation of periodic reports, management reports such as income statements and statements of financial position, checks and queries.

<table><tr><td>Table 2Relevant Organizational Needs</td></tr><tr><td>Accounts ReceivableAccounts PayablePayrollGeneral LedgerInventory ControlIncome Tax ReturnsFixed Assets Accounting</td></tr></table>

Table 3  
The System Functions Categories

<table><tr><td>Accounting Functions</td><td>Operators Functions</td></tr><tr><td>- Transactions validation</td><td>- Operational Savings</td></tr><tr><td>- Editing &amp; Balancing</td><td>... Time Savings</td></tr><tr><td>- Controls &amp; Auditability</td><td>... Clerical Effort</td></tr><tr><td></td><td>- Customer Service</td></tr><tr><td></td><td>... Timeliness</td></tr><tr><td>Data Processing Functions</td><td>... Account Monitoring</td></tr><tr><td>- Data Entry</td><td>... report Quality</td></tr><tr><td>- report Generation</td><td>- User Friendliness</td></tr><tr><td>... Periodic Reports</td><td>... Hardware Aspects</td></tr><tr><td>... Management Reports</td><td>... Software Aspects</td></tr><tr><td>... Checks</td><td></td></tr><tr><td>... Queries</td><td></td></tr><tr><td>- Masterfiles Update</td><td></td></tr></table>

Next, at the third level of the model, the system attributes are separated into specific elements or forms.

The first system attribute to be considered in the evaluation of a business microcomputer is the Central Processing Unit (CPU) and the Main Memory. The relative capability of the CPU & Main Memory is related to the word size, the basic clock frequency (processing speed) and the add time for the summation of one byte in memory to a CPU register. The availability of industry-standard operating systems as well as the current and future capacity of the primary-storage, strongly affect the applicability of the system. Application Packages are the actual program that handle the specific business functions. The primary concerns here are the operational fit, software versatility, required storage space, statistical recording for costing and monitoring, integrity and security features. Security has two aspects: one is the protection of data integrity by limiting access to authorized personnel and the other is the protection of user privacy by prohibiting unauthorized access to personal data. The Diskette Subsystem consists of floppy disk drivers for the storage of the software packages, small files, and transaction data. In general, the average access time to a record the formatted capacity and transfer rate of data from amin memory to the disk are the important characteristics of these subsystems.

Vendor Support contributes to the operation of the business microcomputer in several ways, including technical trouble-shooting, software support and maintenance, user training, documentation, installation, and implementation assistance. In addition, the reputation of the vendor on both national and local levels should be considered. compatibility of hardware allows the users to consider additional sources for particular components; compatibility of software refers to the degree to which programs must be modified in order to be executed on other (larger) microcomputer systems, both from other brands and from the proposed brand. The Printer is used to produce hard-copy output. Printers vary in their technology: the character printing element, the nominal printing speed, quality (sharpness) of the output, and the number of print columns in a line. Some are equipped with a ledger card feeder system which prints details of specific accounts in a chronological fashion. The Special Features refer to added system capability which may be helpful but are not mandatory. These include such options as wordprocessing, spreadsheet for financial planning, and concurrent printing (where the system can simultaneously operate the printer and the keyboard).

System performance can be expressed in terms of several approximated Production Measures. The total throughput and the transaction volume load delineate the expected capacity of the system to handle the anticipated average workload. Peak load handling refers to the system's response to temporary added load and benchmark results indicate the actual performance characteristic of executing sample programs. Data Channels are required for communication with peripheral devices and with other computers, [22]. Their parameters are: the number of channels, the transfer rate per channel and their type of data transmission scheme (protocol). The final system attribute is the Hard Disk Subsystem. It includes the type of disks and disk drivers, average access time to a record, storage capacity, and data transfer rate.

The detailed hierarchy discussed here is depicted in Figure 2. It shows many factors some of which are not always relevant. This allows the deletion and even the addition of elements to certain levels identified in the evaluation hierarchy.

![](/api/attachments/E4T8SQ8H/fulltext/images/82de3eeb96fc5577b0821682680e8ead34be7ef3fc85796222cdb58b68397d84.jpg)  
Figure 2: Accounting Information System Evaluation Hierarchy.

Table 4
Specifications for Candidate Configuration

<table><tr><td rowspan="2">Parameters</td><td colspan="4">Systems</td></tr><tr><td>A</td><td>B</td><td>C</td><td>D</td></tr><tr><td colspan="5">CPU &amp; Main Memory</td></tr><tr><td>Word size(1)</td><td>16</td><td>8</td><td>8</td><td>16</td></tr><tr><td>Basic clock frequency(2)</td><td>5</td><td>2.5</td><td>3.0</td><td>8</td></tr><tr><td>Add time(3)</td><td>7.45</td><td>14.0</td><td>10.20</td><td>5.60</td></tr><tr><td>Operating systems</td><td>vendor&#x27;s</td><td>vendor&#x27;s</td><td>CPM, MPM</td><td>vendor&#x27;s</td></tr><tr><td></td><td>MPM, CPM</td><td>CPM-like</td><td></td><td>UNIX-like</td></tr><tr><td>Memory size(4)</td><td>124</td><td>48</td><td>64</td><td>196</td></tr><tr><td>Maximal memory(4)</td><td>512</td><td>128</td><td>96</td><td>768</td></tr><tr><td colspan="5">Application Packages</td></tr><tr><td>Operational fit</td><td>very good</td><td>good</td><td>very good</td><td>good/fair</td></tr><tr><td>software versatility</td><td>fair</td><td>excellent</td><td>very good</td><td>good</td></tr><tr><td>Required memory(4)(minimal)</td><td>24</td><td>32</td><td>48</td><td>64</td></tr><tr><td>Statistical recording</td><td>N/A</td><td>good</td><td>fair</td><td>N/A</td></tr><tr><td>Integrity</td><td>fair</td><td>good</td><td>very good</td><td>excellent</td></tr><tr><td>Security features</td><td>excellent</td><td>good</td><td>fair</td><td>good</td></tr><tr><td colspan="5">Diskette Subsystem</td></tr><tr><td>Average access time(5)</td><td>290</td><td>264</td><td>400</td><td>364</td></tr><tr><td>Capacity(4)(Formatted)</td><td>2×280</td><td>2×148</td><td>2×216</td><td>2×450</td></tr><tr><td>Data transfer rate(6)</td><td>210</td><td>260</td><td>250</td><td>275</td></tr><tr><td colspan="5">Vendor&#x27;s Support</td></tr><tr><td>Software maintenance</td><td>very good</td><td>excellent</td><td>excellent</td><td>very good</td></tr><tr><td>Technical trouble shooting</td><td>good</td><td>very good</td><td>excellent</td><td>fair</td></tr><tr><td>Training</td><td>very good</td><td>very good</td><td>good</td><td>fair</td></tr><tr><td>Documentation</td><td>good</td><td>fair</td><td>very good</td><td>very good</td></tr><tr><td>General reputation</td><td>excellent</td><td>very good</td><td>good</td><td>good</td></tr><tr><td>Implementation assistance</td><td>fair</td><td>good</td><td>very good</td><td>good</td></tr><tr><td colspan="5">Compatibility</td></tr><tr><td>Hardware</td><td>good</td><td>good</td><td>poor</td><td>good</td></tr><tr><td>Software</td><td>poor</td><td>poor</td><td>good</td><td>good</td></tr><tr><td colspan="5">Printer</td></tr><tr><td>Technology</td><td>matrix 5×8</td><td>matrix 7×9</td><td>matrix 9×9</td><td>matrix 9×9</td></tr><tr><td>Speed(7)</td><td>30-210</td><td>25-140</td><td>160</td><td>180</td></tr><tr><td>Quality(8)</td><td>good</td><td>very good</td><td>very good</td><td>fair</td></tr><tr><td>Print columns</td><td>80,96,132</td><td>132,158</td><td>66-210</td><td>136,250</td></tr><tr><td>ledger Cards</td><td>15&quot;cards</td><td>N/A</td><td>N/A</td><td>15&quot; cards</td></tr><tr><td colspan="5">Special Features</td></tr><tr><td>Wordprocessing</td><td>N/A</td><td>good</td><td>very good</td><td>very good</td></tr><tr><td>Financial spreadsheet</td><td>fair</td><td>good</td><td>very good</td><td>fair</td></tr><tr><td>concurrent printing</td><td>good</td><td>N/A</td><td>limited</td><td>limited</td></tr><tr><td colspan="5">Production Measures</td></tr><tr><td>Total throughput(9)2.3</td><td>2.7</td><td>1.95</td><td>1.7</td><td></td></tr><tr><td>Transaction volume load</td><td>1.4</td><td>1.6</td><td>1.0</td><td>3.4</td></tr><tr><td>Peak load handling</td><td>very good</td><td>good</td><td>very good</td><td>good</td></tr><tr><td>Benchmark results</td><td>good</td><td>good</td><td>very good</td><td>good</td></tr><tr><td colspan="5">Data Channels</td></tr><tr><td>No. of Channels transfer rate(10)</td><td>5</td><td>4</td><td>3</td><td>4</td></tr><tr><td></td><td>1,200</td><td>3,600</td><td>1,200</td><td>9,600</td></tr><tr><td>Type</td><td>1 parallel</td><td>3 custom, IEEE-488</td><td>parallel, RS232-C, IEEE-488,</td><td>parallel 2 RS232-C, RS422,</td></tr><tr><td colspan="5">Hard Disk Subsystem</td></tr><tr><td>Type</td><td>8&quot; winchester</td><td>5&quot; winchester</td><td>8&quot; winchester</td><td>14&quot; winchester</td></tr><tr><td>Average ac. time(11)</td><td>140</td><td>153</td><td>110</td><td>60</td></tr><tr><td>Capacity (formatted)(12)</td><td>14</td><td>7.52</td><td>10.5</td><td>32</td></tr><tr><td>Data transfer rate(13)</td><td>4</td><td>5</td><td>6.2</td><td>7.68</td></tr></table>

(1) Bits, (2) Megahertz, (3) Microseconds, (4) K-Bytes, (5) Millisecond/record, (6) K-bits/second. (7) Characters/second, (8) Relative quality assessment at high speed. (9) Relative estimated performance (1.0 = minimal acceptable level) (10) Bauds (max. rate for serial line), (11) Millisecond/record, (12) M-Bites, (13) M-Bites/second

## 3. An Illustrative Example

This section gives a detailed application of the model of the previous section. The effort is directed at selecting an accounting information system that suits the organization under consideration.

The first step in the acquisition process is the determination of the organizational needs, and the translation of these needs to specific parameters. Since the selection is to be made from systems available on the market (as opposed to a custom design), candidate systems can be identified within the minimum required performance levels.

A detailed search for candidate systems yielded those systems designated as “A”–“D” in Table 4. Readers who are not familiar with contemporary information system terminology may refer to [3,5,7,21]. Examining the performance levels and capabilities of these systems reveals that no single system stands out as an obvious “winner”. All four satisfy the minimal configuration requirements of the preliminary analysis and design phase. Price differences were marginal and, therefore, ignored.

In order to prioritize the selection parameters one has to consider the complete model and prioritize all its elements. The prioritization of the model's elements is carried out through the "Analytic Hierarchy Process" (AHP). This methodology requires that first, one must prioritize the specific needs to assess those which dominate the accounting system selection. Next, the impact of the system functions on each of the organizational needs is assessed. This results in a set of local priorities reflecting the importance of each function to the specific organizational needs. Then, using the priorities of the organizational needs, one proceeds to evaluate the global priorities of the system functions. This is done by weighting each local priority by the priority of the respective organizational need, repeating this process for each organizational need, and summing all products to arrive at the global priority. This process is repeated for each level by first assessing local priorities of members of the i-th level with respect to each member of the $(i-1)$ -th level. Then, using the weighting scheme described above, one converts these local weights to global weights and proceeds down the hierarchy until the bottom level is reached, at which stage the specific candidate systems can be prioritized.

As outlined above, the first step is concerned with the assessment of the organizational needs. This is done by asking $n(n=1)/2$ pairwise comparison questions of the type “which of the following two organizational needs dominates the other, and by how much?” The first part of the question is clearly an ordinal question while the second part is a cardinal one requiring a numerical input. This input is provided by using the ratio scale described in Table 5.

The assessment of the relative importance of the organizational needs is summarized in Table 6. The information displayed in this matrix is interpreted as follows: every element, $a_{ij}$ , of this matrix A shows the relative contribution (to the subject of comparison) of the i-th element as compared to the j-th element, i.e.,

Table 5
Comparison Scale

<table><tr><td>Intensity of Importance</td><td>Definition</td><td>Explanation</td></tr><tr><td>1</td><td>Equal importance</td><td>Two activities contribute equally to the objective</td></tr><tr><td>3</td><td>Moderate importance of one over another</td><td>Experience and judgement favour one activity over another</td></tr><tr><td>5</td><td>Essential or strong importance</td><td>Experience and judgement strongly favour one activity over another</td></tr><tr><td>7</td><td>very strong or demonstrated importance</td><td>An activity is favoured very strongly over another; its dominance demonstrated in practice</td></tr><tr><td>9</td><td>Absolute importance</td><td>The evidence favouring one activity over another is of the highest possible order of affirmation</td></tr><tr><td>2,4,6,8</td><td>Intermediate values between adjacent scale values</td><td>When compromise is needed</td></tr><tr><td>Reciprocals of above nonzero</td><td colspan="2">If activity i has one of the above nonzero numbers assigned to it when when compared with activity j, then j has the reciprocal value when compared with i.</td></tr></table>

$$
a _ {i j} = w _ {i} / w _ {j}, \quad 1 \leq i \leq n, \quad 1 \leq j \leq n.\tag{1}
$$

Only the upper triangular part of this “comparison matrix” is shown since the matrix is reciprocal, i.e., $a(i, j) = 1/a(j, i)$ . The entries of this matrix are taken from the scale in Table 5. So, in comparing, for example “accounts receivable” with “general ledger” the first was judged to be more important and the strength of this dominance was judged to be between “equal” and “moderate” which is translated to the entry (2) shown circled. After all $n(n = 1)/2$ (in this case $7 \times 6/2 = 21$ ) questions have been asked, the eigenvector corresponding to the largest eigenvalue ( $\lambda_{max}$ ) is found, i.e., $Aw = \lambda_{max}w$ is solved for w. This (normalized) eigenvector provides the priorities shown in the last column. One must be concerned with the quality of the answers provided in the comparison matrix and, in particular, with the problem of consistency. This is assessed by considering whether $a(i, j) = a(i, k)a(k, j)$ holds for all triplets. The “consistency ratio” (designated C.R.) is required to be less than 0.1 for acceptable consistency.

It should be emphasized, however, that the priorities associated with the organizational needs should not be taken as general for every organization. Though the model is general enough for diverse needs, the prioritization should reflect the specific organization and its particular needs.

Next, one considers the contributions of the three sets of system functions to each of the organizational needs. This process is summarized in Tables 7–13.

These seven comparison matrices provide the local priorities of the support categories with respect to each of the organizational needs. These local priorities are depicted graphically in Figure 3, and summarized in Table 14.

Table 7  
Systems Functions vs. "Accounts Receivable"

<table><tr><td>Accounts Receivable</td><td>1</td><td>2</td><td>3</td><td>Priorities</td></tr><tr><td>1) Accounting</td><td>1</td><td>3</td><td>3</td><td>0.59</td></tr><tr><td>2) Operator</td><td></td><td>1</td><td>2</td><td>0.25</td></tr><tr><td>3) Data Processing</td><td></td><td></td><td>1</td><td>0.16</td></tr><tr><td></td><td colspan="3">C.R. = 0.046</td><td>1.00</td></tr></table>

Table 8  
System Functions vs. "Accounts Payable"

<table><tr><td>Accounts Payable</td><td>1</td><td>2</td><td>3</td><td>Priorities</td></tr><tr><td>1) Accounting</td><td>1</td><td>3</td><td>3</td><td>0.59</td></tr><tr><td>2) Operator</td><td></td><td>1</td><td>2</td><td>0.25</td></tr><tr><td>3) Data Processing</td><td></td><td></td><td>1</td><td>0.16</td></tr><tr><td></td><td colspan="3">C.R. = 0.046</td><td>1.00</td></tr></table>

Table 9  
System Functions vs. "General Ledger"

<table><tr><td>General Ledger</td><td>1</td><td>2</td><td>3</td><td>Priorities</td></tr><tr><td>1) Accounting</td><td>1</td><td>1</td><td>2</td><td>0.49</td></tr><tr><td>2) Operator</td><td></td><td>1</td><td> $1/2$ </td><td>0.20</td></tr><tr><td>3) Data Processing</td><td></td><td></td><td>1</td><td>0.31</td></tr><tr><td></td><td colspan="3">C.R. = 0.046</td><td>1.00</td></tr></table>

Table 10  
System Functions vs. "Payroll"

<table><tr><td>Payroll</td><td>1</td><td>2</td><td>3</td><td>Priorities</td></tr><tr><td>1) Accounting</td><td>1</td><td> $1/3$ </td><td> $1/3$ </td><td>0.14</td></tr><tr><td>2) Operator</td><td></td><td>1</td><td>1</td><td>0.43</td></tr><tr><td>3) Data Processing</td><td></td><td></td><td>1</td><td>0.43</td></tr><tr><td></td><td colspan="3">C.R. = 0.00</td><td>1.00</td></tr></table>

Table 6  
Organizational Needs

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>Priorities</td></tr><tr><td>1) Accounts Receivable</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>0.22</td></tr><tr><td>2) Accounts Payable</td><td></td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>0.22</td></tr><tr><td>3) General Ledger</td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0.11</td></tr><tr><td>4) Payroll</td><td></td><td></td><td></td><td>1</td><td>2</td><td>1</td><td>1</td><td>0.12</td></tr><tr><td>5) Inventory</td><td></td><td></td><td></td><td></td><td>1</td><td> $1/2$ </td><td>1</td><td>0.09</td></tr><tr><td>6) Fixed Asset</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td> $1/2$ </td><td>0.11</td></tr><tr><td>7) Tax Return</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>0.13</td></tr><tr><td></td><td colspan="7">C.R. = 0.019</td><td>1.00</td></tr></table>

Table 11  
System Functions vs. "Inventory"

<table><tr><td>Inventory</td><td>1</td><td>2</td><td>3</td><td>Priorities</td></tr><tr><td>1) Accounting</td><td>1</td><td>2</td><td>1</td><td>0.40</td></tr><tr><td>2) Operator</td><td></td><td>1</td><td> $1/2$ </td><td>0.20</td></tr><tr><td>3) Data Processing</td><td></td><td></td><td>1</td><td>0.40</td></tr><tr><td></td><td colspan="3">C.R. = 0.00</td><td>1.00</td></tr></table>

Table 12  
System Functions vs. "Fixed Assets"

<table><tr><td>Fixed Asset</td><td>1</td><td>2</td><td>3</td><td>Priorities</td></tr><tr><td>1) Accounting</td><td>1</td><td>3</td><td>2</td><td>0.54</td></tr><tr><td>2) Operator</td><td></td><td>1</td><td> $1/2$ </td><td>0.16</td></tr><tr><td>3) Data Processing</td><td></td><td></td><td></td><td>0.30</td></tr><tr><td></td><td colspan="3">C.R. = 0.008</td><td>1.00</td></tr></table>

Table 13  
System Functions vs. "Tax Return"

<table><tr><td>Tax Return</td><td>1</td><td>2</td><td>3</td><td>Priorities</td></tr><tr><td>1) Accounting</td><td>1</td><td>4</td><td>2</td><td>0.57</td></tr><tr><td>2) Operator</td><td></td><td>1</td><td> $1/2$ </td><td>0.14</td></tr><tr><td>3) Data Processing</td><td></td><td></td><td>1</td><td>0.29</td></tr><tr><td></td><td colspan="3">C.R. = 0.00</td><td>1.00</td></tr></table>

Using the priorities derived for the organizational needs to weight each column of local priorities of Table 14, one derives the global priorities for the operational support categories, as shown in Figure 4.

Each of the system function categories is subdivided into more specific functional categories as shown in Figure 2. Deriving the local priorities of these specific categories with respect to their “host” categories, and weighting them by the priorities of the “host” categories yields the global priorities of all the (specific) system function categories. These are given in Table 15.

Now that the global priorities of all the elements in the system functions categories have been established, we proceed at level 3 to describe the system attributes. Not all attributes listed at in this level are relevant to each system functions categories, so the analysis considers only those relevant attributes in each case. For example, in considering contributions to the “transactions” category, only “cpu & memory”, “application packages”, “diskette subsystems”, “printers” and “special features” are relevant.

The assessment of the importance of these attributes to the “transaction” category is summarized in Table 16.

This process is repeated for each of the system functions categories and its relevant attributes. Once the local priorities with respect to each of these categories is derived, we weight them by the respective global priorities of the system functions to obtain the global priorities of the system attributes; these are summarized in Table 17.

Each of these “system attributes” is made up of a number of more specific elements; e.g., “cpu & memory” is comprised of: word size (bits), clock frequency, add time, operating system, memory size, and maximal memory. Evaluating the relative importance of these parameters leads to the comparison matrix shown in Table 18. The last column is obtained by multiplying the local priorities with the global priority of “Cpu & memory” (0.130).

![](/api/attachments/E4T8SQ8H/fulltext/images/e628b805ac713bddc5118b511d8f0d0018407b748546aa8c14f769b22cfd9a7b.jpg)  
Figure 3: Local Priorities of Operational Support Categories.

Table 14  
Local Priorities of System Functions Categories (level 2)

<table><tr><td rowspan="2">Support Category</td><td colspan="7">Organizational Need</td></tr><tr><td>Accounts</td><td>Accounts</td><td>General</td><td>Payroll</td><td>Inventory</td><td>Fixed</td><td>Tax</td></tr><tr><td></td><td>Receivable</td><td>Payable</td><td>Ledger</td><td></td><td></td><td>Asset</td><td>Return</td></tr><tr><td>Accounting</td><td>0.59</td><td>0.59</td><td>0.49</td><td>0.14</td><td>0.40</td><td>0.54</td><td>0.57</td></tr><tr><td>Operator</td><td>0.25</td><td>0.25</td><td>0.20</td><td>0.43</td><td>0.20</td><td>0.16</td><td>0.14</td></tr><tr><td>Data Processing</td><td>0.16</td><td>0.16</td><td>0.31</td><td>0.43</td><td>0.40</td><td>0.30</td><td>0.29</td></tr></table>

Table 15  
Global Priorities of System Functions Categories

<table><tr><td>Category</td><td>Global Priority</td></tr><tr><td>Transactions</td><td>0.270</td></tr><tr><td>Editing &amp; Balancing</td><td>0.082</td></tr><tr><td>Controls</td><td>0.149</td></tr><tr><td>Time Saving</td><td>0.084</td></tr><tr><td>Clerical Effort</td><td>0.021</td></tr><tr><td>Timliness</td><td>0.022</td></tr><tr><td>Account Monitoring</td><td>0.008</td></tr><tr><td>Report Quality</td><td>0.010</td></tr><tr><td>Hardware Aspects</td><td>0.018</td></tr><tr><td>Software Aspects</td><td>0.074</td></tr><tr><td>Data Entry</td><td>0.036</td></tr><tr><td>Periodic Reports</td><td>0.045</td></tr><tr><td>Management Reports</td><td>0.061</td></tr><tr><td>Checks</td><td>0.024</td></tr><tr><td>Queries</td><td>0.033</td></tr><tr><td>Masterfile Update</td><td>0.063</td></tr><tr><td>Total</td><td>1.000</td></tr></table>

![](/api/attachments/E4T8SQ8H/fulltext/images/4cf512b662119a8796469d609eb178c7a4be773a12c13f446d991e39ffb5e285.jpg)  
Figure 4: Global Priorities of Operational Support Categories.  
Table 17

Again, we repeat this process for all the elements of the “system attributes” level until the global priorities for all the elements are derived. This is summarized in Table 19.

Global Priorities of System Attributes

<table><tr><td>Attribute</td><td>Priority</td></tr><tr><td>Cpu &amp; Memory</td><td>0.130</td></tr><tr><td>Application packages</td><td>0.356</td></tr><tr><td>Diskette subsystem</td><td>0.101</td></tr><tr><td>Vendor&#x27;s Support</td><td>0.064</td></tr><tr><td>Compatibility</td><td>0.006</td></tr><tr><td>Printers</td><td>0.098</td></tr><tr><td>Special features</td><td>0.063</td></tr><tr><td>Production measures</td><td>0.112</td></tr><tr><td>Data Channels</td><td>0.002</td></tr><tr><td>Hard-disk subsystem</td><td>0.068</td></tr><tr><td>Total</td><td>1.000</td></tr></table>

Table 16  
Attributes vs. "transactions"

<table><tr><td>Transactions</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>Priorities</td></tr><tr><td>1) Cpu &amp; memory</td><td>1</td><td> $1/3$ </td><td>4</td><td>2</td><td>3</td><td>0.26</td></tr><tr><td>2) Application packages</td><td></td><td>1</td><td>3</td><td>3</td><td>3</td><td>0.41</td></tr><tr><td>3) Diskette subsystem</td><td></td><td></td><td>1</td><td>1</td><td> $1/2$ </td><td>0.09</td></tr><tr><td>4) Printers</td><td></td><td></td><td></td><td>1</td><td>2</td><td>0.12</td></tr><tr><td>5) Special features</td><td></td><td></td><td></td><td></td><td>1</td><td>0.12</td></tr><tr><td></td><td colspan="5">C.R. = 0.066</td><td>1.00</td></tr></table>

Table 18  
"CPU & Memory" attributes

<table><tr><td>CPU &amp; memory</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>local priority</td><td>global priority</td></tr><tr><td>1) word size</td><td>1</td><td>4</td><td>3</td><td>2</td><td>1/3</td><td>1/2</td><td>0.19</td><td>0.025</td></tr><tr><td>2) clock frequency</td><td></td><td>1</td><td>1</td><td>1/2</td><td>1/3</td><td>1/2</td><td>0.08</td><td>0.010</td></tr><tr><td>3) add time</td><td></td><td></td><td>1</td><td>1/2</td><td>1/2</td><td>1/3</td><td>0.08</td><td>0.010</td></tr><tr><td>4) Operating system</td><td></td><td></td><td></td><td>1</td><td>1/2</td><td>1/2</td><td>0.13</td><td>0.017</td></tr><tr><td>5) memory size</td><td></td><td></td><td></td><td></td><td>1</td><td>2</td><td>0.31</td><td>0.040</td></tr><tr><td>6) maximal memory</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>0.21</td><td>0.028</td></tr><tr><td>C.R. = 0.054</td><td></td><td>total</td><td></td><td></td><td></td><td></td><td>1.00</td><td>0.130</td></tr></table>

Table 19  
Global priorities of system attributes

<table><tr><td>Word Size</td><td>= 0.002</td></tr><tr><td>Basic Clock Frequency</td><td>= 0.01</td></tr><tr><td>Add Time</td><td>= 0.01</td></tr><tr><td>Operating System</td><td>= 0.02</td></tr><tr><td>Memory Size</td><td>= 0.04</td></tr><tr><td>Maximal Memory</td><td>= 0.03</td></tr><tr><td>Operational Fit</td><td>= 0.11</td></tr><tr><td>Software Versatility</td><td>= 0.03</td></tr><tr><td>Required Memory</td><td>= 0.08</td></tr><tr><td>Statistical Recording</td><td>= 0.04</td></tr><tr><td>Integrity</td><td>= 0.04</td></tr><tr><td>Security Features</td><td>= 0.05</td></tr><tr><td>Average Access Time</td><td>= 0.02</td></tr><tr><td>Formatted Capacity</td><td>= 0.06</td></tr><tr><td>Data Transfer Rate</td><td>= 0.03</td></tr><tr><td>Software Maintenance</td><td>= 0.02</td></tr><tr><td>Technical Trouble-Shooting</td><td>= 0.01</td></tr><tr><td>Training</td><td>= 0.01</td></tr><tr><td>Documentation</td><td>= 0.01</td></tr><tr><td>General Reputation</td><td>= 0.01</td></tr><tr><td>Implementation Assistance</td><td>= 0.005</td></tr><tr><td>Hardware Compatibility</td><td>= 0.001</td></tr><tr><td>Software Compatibility</td><td>= 0.001</td></tr><tr><td>Printer Technology</td><td>= 0.01</td></tr><tr><td>Printed Speed</td><td>= 0.04</td></tr><tr><td>Printer Quality</td><td>= 0.002</td></tr><tr><td>Print Columns</td><td>= 0.02</td></tr><tr><td>Wordprocessing</td><td>= 0.01</td></tr><tr><td>Financial Spreadsheet</td><td>= 0.02</td></tr><tr><td>Concurrent Printing</td><td>= 0.02</td></tr><tr><td>Total Throughput</td><td>= 0.04</td></tr><tr><td>Transaction Volume Load</td><td>= 0.02</td></tr><tr><td>Peak Load Handling</td><td>= 0.04</td></tr><tr><td>Benchmark Results</td><td>= 0.015</td></tr><tr><td>Number of Channels</td><td>= 0.05</td></tr><tr><td>Transfer Rate</td><td>= 0.002</td></tr><tr><td>Type</td><td>= 0.004</td></tr><tr><td>Hard Disk Type</td><td>= 0.01</td></tr><tr><td>Average Access Time</td><td>= 0.015</td></tr><tr><td>Formatted Capacity</td><td>= 0.03</td></tr><tr><td>Data Transfer Rate</td><td>= 0.01</td></tr><tr><td>Total</td><td>= 1.000</td></tr></table>

Now, finally, one is in a position to assess the priorities of the candidate systems. This is done by comparing the four systems relative to each of the prioritized system attributes. In comparing the four systems relative to “word size” Table 20 is obtained.

Note that the entries in the matrix were not taken as simply the ratio between the respective attributes (8 vs. 16 bits) but rather, the 16 bit system was judged to be of considerable dominance relative to the 8 bit system (the entry 4 corresponds to a scale value between moderate" and "strong" dominance). Those systems who do not share a given property (e.g., statistical recording is not available with systems A) are not compared with respect to it.

Table 20  
Systems vs. "word size"

<table><tr><td>word size</td><td>1</td><td>2</td><td>3</td><td>4</td><td>priorities</td></tr><tr><td>1) system A</td><td>1</td><td> $-4$ </td><td>4</td><td>1</td><td>0.40</td></tr><tr><td>2) system B</td><td></td><td>1</td><td>1</td><td> $1/4$ </td><td>0.10</td></tr><tr><td>3) system C</td><td></td><td></td><td>1</td><td> $1/4$ </td><td>0.10</td></tr><tr><td>4) system D</td><td></td><td></td><td></td><td>1</td><td>0.40</td></tr><tr><td></td><td colspan="3">C.R. = 0.00</td><td></td><td>1.00</td></tr></table>

Table 21  
Global Priorities of Candidate Systems

<table><tr><td>System</td><td>Priority</td></tr><tr><td>System A</td><td>0.331</td></tr><tr><td>System B</td><td>0.205</td></tr><tr><td>System C</td><td>0.228</td></tr><tr><td>System D</td><td>0.236</td></tr></table>

Repeating this process of comparing the four systems relative to all attributes and weighting their local priorities by the global priorities of the attributes yields the global priorities for the systems given by Table 21.

These global priorities reveal that system A clearly dominates its competitors and, therefore, is the system to be selected.

Note: The conclusion in favour of system A was reached based on the assumption that all systems are of relatively equal cost. If this assumption is not justified, one derives cost priorities for these systems depicting their relative cost and then makes the choice using a benefit/cost approach $[12,20]$ with the benefit priorities taken from Table 21.

## 4. Sensitivity Analysis

The analysis presented thus far has resulted with the conclusion that system A is the one to be selected. This conclusion is affected by the priorities associated with the particular organizational needs. Would a slight shift in these priorities alter our decision?

Let us denote by $W(i+1,i)$ the matrix of local weights relating level $(i+1)$ to level i. That is, each column of this matrix, say $w_{j}$ , provides the local weights of elements in level $(i+1)$ with respect to the j-th element in level i. The global priorities of elements in level $(i+1)$ are given,

therefore, by

$$
p (i + 1) = W (i + 1, i) p (i),\tag{2}
$$

where $p(i)$ is the vector of global priorities of elements in level i. If the hierarchy has n levels, then the global priorities of elements in the n-th level are given by

$$
\begin{array}{c} p (n) = W (n, n - 1) W (n - 1, n - 2) \dots \\ \times W (2, 1) p (1) = W (n, 1) p (1), \end{array}
$$

where

(3)

$$
W (n, 1) = W (n, n - 1) W (n - 1, n - 2) \dots W (2, 1).\tag{4}
$$

Now, if the priorities of the first level, $p(1)$ , are changed to $\hat{p}(1)$ , the new global priorities of the n-th level, $\hat{p}(n)$ , are given simply by

$$
\hat {p} (n) = W (n, 1) \hat {p} (1).\tag{5}
$$

Referring to Table 4, we note that system A is dominated by other systems in a number of categories. However, changing the priorities of the organizational needs resulted in no shift in our preference for system A. This becomes quite clear upon consulting Fig. 5 where systems' priorities relative to organizational needs are depicted. The sensitivity analysis summarized in that figure shows that system A dominates all the others with respect to each organizational need (in spite of several inferiorities with respect to specific attributes of Table 4) and, therefore, no change in p(1)

![](/api/attachments/E4T8SQ8H/fulltext/images/ca0247a943cbd50c9c108c8d65d240c13113eee988eaf712a35a5fd99562228b.jpg)  
Figure 5: Sensitivity Analysis With Respect to Relevant Organizational Needs.

will result in a shift to a different system.

The insensitivity displayed in this example is not necessarily the common rule for these selection problems but the availability of sensitivity analysis should be exploited before arriving at a final acquisition. Note, that in spite of the fact that system B has some strong attributes (cf. Table 4) it is quite inferior to the other systems with respect to most organizational needs. This stems from the fact its specific strong attributes support relatively unimportant issues.

## 5. Summary and Conclusions

A methodology of selecting a microcomputer system for a particular organizational application has been presented. The selection problem is partitioned into two major steps. At the first step one constructs a four level hierarchical model of all relevant factors identifying critical categories at each level and their interrelationships. At the second step, the managers and their staff go through the hierarchical structure and derive a priority structure associated with the various factors at each level.

The application described in this paper was carried out with the aid of an interactive computer program that computed the priority vectors and the consistency ratios. Major conclusions from few similar applications of the model were that it was found to be valid, flexible, easy to apply and did not overlook any significant factor. Management viewed this model as a good vehicle for communicating their concerns and influencing the search in a technical area, while information and computer experts viewed the model as a vehicle for interfacing all technical aspects with the required management priorities.

## References

[1] G.M. Booth, Functional Analysis of Information Processing, Wiley, New York, 1973.

[2] I. Borovits, and Neumann, S., Computer Systems Performance Evaluation, Lexington Book, New York, 1979.

[3] B.E. Cushing, Accounting Information Systems and Business Organizations, Addison-Wesley, Reading, Mass., 1978.

[4] D. Ferrari, Computer Systems Performance Evaluation, Prentice-Hall, Englewood Cliffs, N.J., 1978.

[5] J.P. Frankenhuis, "HOW to Get a Good Mini", Harvard Business Review, Vol. 60 (May-June 1982), pp. 139–149.

[6] M.J. Ginzberg, “Early Diagnosis of MIS Implementation Failure: Promising Results and Unanswered Questions”, Management Science, Vol. 27 (1981), pp. 459–478.

[7] J.O. Hicks, and W.E. Leininger, Accounting Information Systems, West Publishing, St. Paul, Minn., 1981.

[8] G. Huber, “Organizational Information Systems: Determinants of Their Performance and Behavior”, Management Science, Vol. 28 (February 1982), pp. 138–155.

[9] K.R. Isshiki, Small Business Computers: A Guide to Evaluation and Selection, Prentice-Hall, Englewood Cliffs, N.J., 1982.

[10] E.O. Joslin, Analysis, Design and Selection of Computer Systems, College Readings, Arlington, Va., 1974.

[11] R.D. Kamenetzky, “The Relationship Between the Analytic Hierarchy Process and the Additive Value Function”, Decision Science, Vol. 13 (October 1982), pp. 702–713.

[12] J.L. King and E.L. Schrems, “Cost-Benefit Analysis in Information Systems Development and Operation”, ACM Computing Surveys, Vol. 10 (March 1978), pp. 19–34.

[13] C. Mader and R. Hagin, Information Systems: Technology, Economics and Applications, SRA, Chicago, IL., 1974.

[14] R.L. Patrick, “The Other Side of the Small Computer Picture”, Datamation, Vol. 24 (August 1978), pp. 132–135.

[15] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1981.

[16] C. Sauer and K.M. Chandy, Computer Systems Performance Modeling, Prentice-Hall, Englewood Cliffs, N.J., 1981.

[17] P.J.H. Schoemaker and C.C. Waid, "An Experimental Comparison of Different Approaches to Determining Weights in Additive Utility Models", Management Science, Vol. 28 (February 1982), pp. 182–196.

[18] J. Schwartz and W.P. Melling, “Sharing Work and Logic”, Datamation, Vol. 28 (November 1982), pp. 113–120.

[19] S. Stibbens, "Buying a Desk Top Computer", Infosystems, Vol. 29, (December 1982), pp. 40–44.

[20] E.M Timmreck, “Computer Selection Methodology”, ACM Computing Surveys, Vol. 5, (1973), pp. 199–222.

[21] M.E. Walsh, Understanding Computers, Wiley, New York, 1981.

[22] C. Weitzman, Distributed Micro/Minicomputer Systems, Prentice-Hall, Englewood Cliffs, N.J., 1980.

[23] Y. Wind and t.L. Saaty, “Marketing Applications of the Analytic Hierarchy Process”, Management Science, Vol. 26 (July 1980), pp. 641–658.

[24] R.C. Wynne and A. Frotman, "Microcomputers: Helping Make Practice Perfect", The Journal of Accountancy, Vol. 152 (December 1081), pp. 34–39.
