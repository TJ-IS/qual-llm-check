---
otero_id: 26984
otero_key: "4MKGET59"
title: "Control and Audit of Electronic Data Interchange"
authors: "James V. Hansen; Ned C. Hill"
year: "1989"
journal: "MIS Quarterly"
doi: "10.2307/248724"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Control and Audit of Electronic Data Interchange
Author(s): James V. Hansen and Ned C. Hill
Source: MIS Quarterly, Vol. 13, No. 4 (Dec., 1989), pp. 403-413
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248724

Accessed: 08/05/2014 20:25

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Control and Audit of Electronic Data Interchange

By: James V. Hansen
Ned C. Hill

Marriott School of Management
Brigham Young University
Provo, Utah 84602

## Abstract

Electronic data interchange (EDI) is the movement of information electronically between a buyer and seller for purposes of facilitating a business transaction. EDI represents a powerful application of computer-communications technology. Its value includes such benefits as reduced paperwork, elimination of data entry overheads, improved accuracy, timely information receipt, accelerated cash flow, and reduced inventories.

EDI brings with it, however, new and important control considerations. This article discusses, in a non-technical fashion, the control architectures and concerns associated with EDI. Audit considerations in the EDI environment, as well as related audit tools, are also outlined.

Keywords: Data communications, control and audit, electronic data interchange

ACM Categories: H.4.3, K.6.4

## Introduction

Many firms in a number of industries are adopting business strategies based upon electronic data interchange (EDI). Documented benefits accruing from EDI include reduced order lead times; higher customer service level; fewer out-of-stock situations; improved communication about promotions, price changes, and product availability; lower inventory costs; better accuracy in ordering, shipping, and receiving; and reductions in labor costs (Stern and Kaufman, 1985).

Survey results summarized in the next section show that EDI is increasing steadily as a means of conducting business. The thesis of this article is that EDI changes the control and audit environment, but that methods and procedures exist that are responsive to those changes. Our objective is to increase the reader's understanding of both areas. To that end, the discussion centers on the following areas: The first part of the article presents some relevant results from a recent survey, establishes fundamentals and terminology, and provides an overview of some of the control issues associated with EDI. The next part of the article outlines a suggested EDI control architecture, discusses some of the more frequently raised concerns by firms considering EDI, and suggests how those concerns may be addressed. The last part of the article discusses audit considerations and tools appropriate to EDI, notes a change in audit boundaries, and finally, offers some concluding remarks.

## Recent Survey Findings

It may be of interest to briefly consider some recent survey findings related to perceived EDI benefits among the business community. The most comprehensive and current survey of EDI use was completed by EDI Research, Inc. $^{1}$ (EDI Research, 1988). The second author of this article played a major role in this survey. Respondents who were currently using, or planning to use, EDI were asked why. The question was presented in open-ended form, and responses were grouped to represent, as nearly as possible, the words of the respondents (see Table 1). The most frequently mentioned benefit, “quick response and access to information,” was mentioned nearly twice as often as any other reason. The second most frequently mentioned benefit was “cost efficiency,” followed closely by “customer request.” The “effect of EDI on paperwork” was noted by 12.4 percent of the respondents and “accuracy” by 9.8 percent.

It should be noted that some of the purported advantages of EDI were not perceived as particularly important by respondents. For instance, EDI typically reduces labor costs, yet this advantage was mentioned by less than 4 percent of the respondents. Inventory savings was also rated relatively low.

The results of a question similar to the one above, but not open ended, gave a slightly different perspective. Respondents were asked to rate various possible EDI benefits on a 5-point scale, with “5” being the most important and “1” being the least important. These results are summarized in Table 2. As the table shows, the benefit rated the highest is “improved customer service.” However, customer service was not mentioned at all in Table 1. A possible reason is that every benefit mentioned in Table 1 is directly or indirectly related to customer service. Rapid processing of information, cost efficiency, response to customer request, and accuracy all influence the relationship between the firm employing EDI and its customers.

Table 1. Reasons for Using EDI

<table><tr><td>Advantages*</td><td>Percentage of Respondents</td></tr><tr><td>Quick response and access to information</td><td>47.1%</td></tr><tr><td>Cost efficiency</td><td>20.4%</td></tr><tr><td>Customer&#x27;s request</td><td>19.2%</td></tr><tr><td>Effect of EDI on paperwork</td><td>12.4%</td></tr><tr><td>Accuracy</td><td>9.8%</td></tr><tr><td>Better communications</td><td>5.7%</td></tr><tr><td>Ease processing for order entry</td><td>5.5%</td></tr><tr><td>Aids in accounting, billing, etc.</td><td>5.5%</td></tr><tr><td>Better customer service</td><td>5.5%</td></tr><tr><td>Tracing shipments</td><td>4.9%</td></tr><tr><td>Remain competitive</td><td>4.9%</td></tr><tr><td>Industry standards</td><td>4.0%</td></tr><tr><td>Increase productivity</td><td>4.0%</td></tr><tr><td>Convenience</td><td>4.0%</td></tr><tr><td>Reduce manpower</td><td>3.7%</td></tr><tr><td>Inventory control-reduct.</td><td>3.2%</td></tr></table>

\* (Table does not include responses mentioned 10 or less times.)

Table 2. Rating Factors Important to EDI

<table><tr><td>Benefit Factor</td><td>Average Rating</td></tr><tr><td>Improved customer service</td><td>4.29</td></tr><tr><td>Improved control of data</td><td>4.14</td></tr><tr><td>Reduced clerical error</td><td>3.97</td></tr><tr><td>Decreased administrative cost</td><td>3.71</td></tr><tr><td>Decreased inventory cost</td><td>3.35</td></tr><tr><td>Increased sales</td><td>3.25</td></tr><tr><td>Decreased manufacturing cost</td><td>2.75</td></tr></table>

Peters (1987) cites a number of compelling reasons why firms are finding it necessary to utilize EDI in order to remain competitive, both domestically and internationally. He notes that EDI links foster the exchange of a wider range of electronic documents such as purchase orders, material releases, advance shipping notices, freight bills, receiving discrepancy reports, invoices, and remittance advices among trading partners. In addition, several banks are also participating in manufacturers' efforts to integrate electronic funds transfer (EFT) with EDI.

One measure of the strength of the EDI marketplace is the anticipated growth in the number of future EDI trading partners. In the EDI Research survey referred to earlier (EDI Research, 1988), respondents were asked to indicate the number of new trading partners they expected to add in 1988 and 1989. Table 3a shows that two-thirds of the respondents planned to add trading partners. The remaining one-third did not intend to add any. Fifteen percent planned to add more than 21 new partners, and 6.5 percent planned to add more than 50.

For the following year (1989), expected growth in the number of trading partners accelerated (Table 3b). Over 83 percent of the respondents intend to add new EDI partners, compared to 66.5 percent in 1988. Only 17 percent do not plan to add partners during 1989. Sixteen percent plan to add more than 50 partners, while only 6.5 percent planned to add that many in 1988.

The addition of trading partners alone may not be the most compelling measure of growth in the EDI marketplace. The addition of trading partners that have already implemented EDI may not expand the business base as much as adding trading partners that are initiating EDI. Moreover, adding new trading partners does not necessarily translate into major increases in EDI volume. Perhaps a more important measure is the expected growth in EDI document volume.

Table 3a. Intended Addition of EDI Trading Partners in 1988

<table><tr><td>Number of Additions</td><td>Percentage of Respondents</td></tr><tr><td>None</td><td>33.5%</td></tr><tr><td>1 to 10</td><td>41.8%</td></tr><tr><td>11 to 20</td><td>9.9%</td></tr><tr><td>21 to 50</td><td>8.4%</td></tr><tr><td>&gt;50</td><td>6.5%</td></tr><tr><td>Don&#x27;t know</td><td></td></tr><tr><td></td><td>100.0%</td></tr><tr><td colspan="2">Median = 4.6 new partners</td></tr></table>

Table 3b. Intended Addition of EDI Trading Partners in 1989

<table><tr><td>Number of Additions</td><td>Percentage of Respondents</td></tr><tr><td>None</td><td>16.9%</td></tr><tr><td>1 to 10</td><td>36.0%</td></tr><tr><td>11 to 20</td><td>17.8%</td></tr><tr><td>21 to 50</td><td>13.3%</td></tr><tr><td>&gt;50</td><td>16.0%</td></tr><tr><td>Don’t know</td><td>____</td></tr><tr><td></td><td>100.0%</td></tr><tr><td colspan="2">Median = 9.3 new partners</td></tr></table>

Another issue respondents in the EDI Research study were asked to assess was percent growth of EDI document volume within their functional areas over the next three years. Almost one-third of those answering this question expected a growth rate of over 30 percent, as shown in Table 4. Only 10 percent assessed the growth rate at less than 6 percent. The average was in excess of 22 percent annual growth in EDI volume.

One final set of survey data that may be of interest is shown in Table 5. Of the 1094 respondents, 69 percent imported or exported goods outside the U.S. Of those, 34.7 percent said they use or plan to use EDI for purposes of international trade.

Table 4. Expected Growth in EDI Document Volume

<table><tr><td>Expected Growth</td><td>Percentage of Respondents</td></tr><tr><td>&lt; 6%</td><td>10.1%</td></tr><tr><td>6 to 12%</td><td>15.8%</td></tr><tr><td>12 to 18%</td><td>11.3%</td></tr><tr><td>18 to 24%</td><td>13.8%</td></tr><tr><td>24 to 30%</td><td>18.6%</td></tr><tr><td>&gt; 30%</td><td>30.4%</td></tr><tr><td></td><td>100.0%</td></tr></table>

## EDI Fundamentals and Definitions

Electronic data interchange (EDI) is the movement of business documents electronically between or within firms (including their agents or intermediaries) in a structured, machine-retrievable, data format that permits data to be transferred, without rekeying, from a business application in one location to a business application in another location.

There are a number of ways to transmit data electronically. In general, moving electronic data between two points is called electronic messaging. The various forms of electronic messaging may be arrayed along a continuum (see Figure 1) from unstructured to highly structured. As the figure shows, EDI allows the use of generic formats (such as ANSI X12) intended for use by any of the trading partners, industry-specific formats designed to suit the needs of a particular type of business (e.g., automotive), as well as proprietary formats that may be limited to particular firms and their trading partners.

There is some tendency to confuse EDI with certain other forms of data communication, such as facsimile transmission and electronic mail.

Table 5. Planned Use of EDI for International Trade

<table><tr><td>Response</td><td>Percentage of Respondents</td></tr><tr><td>Yes</td><td>34.7%</td></tr><tr><td>No</td><td>47.8%</td></tr><tr><td>Don’t know</td><td>17.6%</td></tr><tr><td></td><td>100.0%</td></tr></table>

![](/api/attachments/4MKGET59/fulltext/images/98ca89fc03b3d29afcb1033a988bd5930f095c201592fa4a4b589a043348aed0.jpg)  
Figure 1. Electronic Messaging

EDI, however, differs in significant ways. In the case of facsimile transmission, business documents are sent electronically by converting an image of the document into digitized form. Ordinarily, the data so transmitted is not machine retrievable. Typically, the data must be rekeyed into a business application system. EDI data is machine retrievable, and the architecture of EDI avoids unnecessary re-entry of data.

Some advocates of electronic mail argue that EDI is a subfunction of electronic mail. It is true that electronic mail can move business documents electronically, but electronic mail is currently limited to the use of a free format, rather than the structured format that defines EDI. This is an important distinction because it can be difficult to design programs that can read electronic mail directly into data files that can be directly read and processed by business application programs.

Electronic payments (EP) is a subset of EDI that involves not only the transfer of payment information between two partners but also requires a financial institution for the transfer of value. The automated clearinghouse (ACH) system is an EP system that permits the electronic movement of payment and other (limited) information electronically between two partners. Fedwire is another EP system that involves a realtime transfer of value from one account to another. Fedwire is sometimes also referred to as EFT (electronic funds transfer).

Financial EDI refers to EDI messages that are connected with the payment system. It is sometimes helpful to consider invoices, payment advices, and credit and debit memos as a distinct subset of EDI transactions since these may have implications for credit terms, banking, and the payment system.

## EDI's Impact on Internal Controls

From a control and audit standpoint, those characteristics of EDI that make it a powerful business strategy — e.g., reduction of paper and human intervention, and tighter coupling of vendors and suppliers — have a dramatic impact. The change from paper-based transaction processing systems toward a paperless transaction environment results in control evidence being found in machine-readable formats that may be distributed at locations that transcend traditional corporate boundaries. Other important consequences include these:

\- Absence of source documents — Traditional paper source documents related to transactions with outside parties bearing signatures and evidencing authorization and other information will generally not exist in the EDI environment, or may only be available for a limited period. For example, purchase orders and invoices are received from customers and vendors in a machine readable format from a central network depository.

\- Bridging applications — Transactions may be initiated automatically based upon the occurrence of some event. For example, a basic invoice may be generated, based upon the receipt of a purchase order, and determination that the customer's credit rating is satisfactory and that sufficient inventory is on hand.

\- Direct interaction with trading partners — Transactions may be initiated directly by customers and vendors. The authorization of transactions is controlled by limiting those trading partners that can gain access to the computer system.

In general, EDI can virtually eliminate paper flow in the order / delivery / invoice / payment cycle because the computer-based network enables transactions to be initiated, recorded, approved, and executed electronically. Repeated transcriptions by various parties involved in the processing cycle are eliminated because the computer is able to manipulate and exchange the data in a variety of ways after these transactions are entered into the system. Here is one example.

A major auto manufacturer has completely automated the manufacturing process with a material requirements planning (MRP) system for materials requisition, purchasing, and inventory control. The system has entirely automated the process of purchasing and disbursements and is tied into the general ledger system for accounting and financial reporting. The MRP system initiates orders and electronically transmits purchase orders to company suppliers based upon forecasted product sales and current inventory levels. All suppliers are required to be part of the company's electronic data interchange network.

When inventory is received from suppliers, the receiving department uses optical scanning equipment to identify the product. There are no paper receiving reports.

Invoices are received through the electronic data interchange network from suppliers. On a weekly basis the machine-readable database of unpaid invoices is matched against the machine-readable receiving report database. Matched items are routed into the cash disbursement system. Unmatched items on either file are written to a temporary holding file for follow-up by the user through terminals.

Payments to suppliers are initiated by the computer system and are made electronically through a wire transfer of funds at the company's central bank.

The company maintains perpetual inventory records. Because of the historical accuracy of the MRP system, annual physical inventories are not taken, although test counts are taken in conjunction with the annual audit.

There is virtually no paper for the auditor to examine in this system. The only paper is the contract between the manufacturer and its suppliers. The manufacturer has established a policy of purchasing goods only through suppliers who agree to participate in the electronic data interchange network.

Such developments immediately raise questions concerning control.

## A General EDI Control Architecture

Figure 2 illustrates the basic structure of an EDI transmission group. For economy of expression, we have called this an EDI message. The innermost boxes are comprised of electronic representations of business documents such as purchase orders, invoices, and remittance advices. In EDI parlance, an electronic business document is termed a transaction set. Transaction set control is implemented by use of transaction set header and trailer records. The headers and trailers contain control information such as destination ID, date, number of line segments, and so on. They act in a manner analogous to that of batch control tickets in routine batch processing.

All transaction sets of a similar type, e.g., purchase order, form a functional group. Functional groups are also provided with header and trailer records for control. All the functional groups taken together form an EDI message bounded by transmission group header and trailer records. This data is inserted into a transmission protocol, and transmission is initiated. Important (and similar) control information is provided in the header and trailer records at all three levels. The transaction set (or functional group, or EDI message) is uniquely identified and timestamped. Record counts and hash totals are utilized to check for completeness. Sending and receiving parties are uniquely identified in the EDI message header records.

EDI systems architectures for inbound transaction sets and outbound transaction sets are represented in Figures 3 and 4 respectively. The communications interface may be thought of as a modem. The EDI translator converts the incoming EDI format to that format required by the firm's application programs. The application interface accepts input from the EDI translator, accesses the appropriate application program, ensures that the data is complete and is in the necessary format, then feeds the data to the application program. The process is reversed for outbound transactions.

![](/api/attachments/4MKGET59/fulltext/images/56bd9e1fa61a28dd131b947f9eecb29e55524e7478d8a1face238a7e0dc52d9d.jpg)  
Figure 2. EDI — Transmission Group Nomenclature

![](/api/attachments/4MKGET59/fulltext/images/becf79b73f282372d2ae57640e4f84786ce0fb16d4cf3cf50d5a546eb0951257.jpg)  
Figure 3. EDI Systems Architecture — Inbound Transaction Sets

![](/api/attachments/4MKGET59/fulltext/images/c7e27a912bd246dac13d2b287d968f75b25a97b2837b93409b057223352a6cb6.jpg)  
Figure 4. EDI Systems Architecture — Outbound Transaction Sets

Figure 5 illustrates the specific control functions that should be performed during inbound and outbound transaction processing. For inbound transactions the EDI translator should check the EDI formats for correctness, then translate from that format. Concurrently, a functional acknowledgement should be generated and transmitted to the transaction originator. The functional acknowledgement is an electronic analog to registered mail. It provides the sender with immediate information on whether the transaction was received, the time of its receipt, and any errors discovered at the receiving end. If errors do occur and are of sufficient severity, the functional acknowledgement will indicate that the related transactions were rejected.

The EDI translator can also check the received messages to determine that the appropriate password or authorization is included. The application interface will parse the message into the required application format, and it can perform some edit functions (e.g., field checks) on the data prior to inputting to the appropriate application program.

![](/api/attachments/4MKGET59/fulltext/images/43af414533c5d6aa358adae1b4b690633b7ea525fce9c816b6bea6a181228760.jpg)  
Figure 5. Functions Performed by EDI Interface

For outbound transactions the EDI translator accepts input from the application system, converts that data to EDI format, and adds the necessary header and trailer record information. The message is then passed to the communications processor, which provides the necessary transmission protocol information before sending the message over the transmission link. The transmission link may connect directly with the trading partner, but most often will go to a value-added network provided (VAN) such as McDonnell-Douglas or General Electric Information Systems. VANs provide a good measure of flexibility in terms of adding or deleting trading partners. They also provide an electronic mailbox service that allows a trading partner to download messages at times of convenience.

## EDI Control Concerns

The material that follows is not intended to be exhaustive, but it is representative of concerns that have been expressed by those involved with implementing or auditing EDI systems. The strategies outlined suggest that while these are important concerns, appropriate control mechanisms are available. An awareness of these mechanisms and how they apply can ensure inclusion of appropriate control strategies in EDI planning and implementation.

## Validation of payments

## Concern

In a paper-based transaction system, the standard procedures that are followed in authorizing payments include matching vendor invoices with the associated purchase orders and receiving documents. This allows the firm to verify that the goods were actually ordered, that they were received, and that the invoice includes charges for only those goods. Confirmation that this procedure has been accomplished is manifest by the signature of the person responsible for comparing document order information. In an EDI system both the document and signature may be missing.

## EDI Control Strategy

Programmed routines that match control documents (e.g., matching the purchase order, receiving report, and invoice before initiating payment) before allowing the next transaction process to begin can actually enhance the validation process, when compared to the manual procedures of a paper-based system. That is, if the procedures are properly programmed, there will be fewer errors caused by human fallibility. Such validation procedures must be developed with understanding and care, however. Efforts that slip through validation procedures can propagate loss of data integrity in a short period of time.

Codes and IDs can replace signatures. If the programmed control routine verifies that the amounts on the relevant electronic documents match, a code can be automatically applied to indicate that the appropriate procedures have been successfully completed and that evidence for payment authorization is established.

## Audit trail

## Concern

A paper-driven system naturally creates a trail of documents that allow tracking of the transaction activities. These documents are not necessary to process transactions in an EDI system. What will the external auditors say?

## EDI Control Strategy

This problem has arisen in the application of data communications in general. With EDI, data entry is usually accomplished in one of three ways:

1. Source documents are batched, then entered via direct entry terminals.

2. Source documents are entered as received.

3. Transactions are entered directly without preparation of source documents.

The first case is handled in the same manner as batched input not entered directly. The batch number serves as a batch reference.

The second and third cases can easily be handled by a programmed routine that assigns electronic documents to batches it numbers automatically. Under the second method computer-created source documents are batched and filed by entry station. The third method differs only because it requires a computer-generated substitute for a source document. Surrogate documents typically indicate the person preparing or authorizing the transactions.

## Order and payment control

## Concern

Paper-based transaction systems require signatures in order to authorize orders and payments. EDI generally removes signatory authority, and it may increase opportunities for unauthorized access. What is to prevent someone from entering an EDI system and placing an order or authorizing the payment to himself/herself or a cohort? Vindictive employees or inadequately trained users may initiate procedures that were unforeseen. In paper-based systems, the informal checking performed by human workers has served as a modest check on these contingencies.

## EDI Control Strategy

EDI can mitigate the above control problems by implementing the following procedures. A file can be created to hold purchase orders that, in fact, require managerial approval — e.g., unusually large orders, orders in excess of credit limit, and so on. Levels of password control can be implemented to restrict access to applications and data files. Encryption may be used to prevent data or password pirating. Computerized checks can emulate human judgement in detecting fraudulent activity.

Despite the lack of a paper document with an authorizing signature, some firms consider EDI orders as authentic if there is a record of subsequent payment. If production lead times or payment terms render confirmation of subsequent payment difficult, the firm may consider confirming the existence of such EDI-transmitted orders through independent confirmations. While this is not a failsafe procedure, it has been applied with some success.

Specialized approaches to data encryption and authentication have been developed that can be useful in EDI systems. A brief overview is provided in the Appendix.

## Audit Considerations

## A role for continuous auditing

Continuous process auditing offers capabilities and methodologies that are appropriate to the nature of EDI systems. They can provide evidence as well as a basis for more efficient means of transaction processing. The key characteristics of continuous process auditing are:

1. Online monitoring of the major modules of EDI processing.

2. Systems metrics for key functions of EDI processing.

3. System alarms to call attention to system problems.

4. Functional acknowledgements to capture data flows and errors within moments of their occurrence.

Functional acknowledgements were noted earlier. The discussion that follows addresses points 1-3, above.

## Online monitoring of major modules

In EDI systems the processing controls mimic to some degree the standard controls found in a batch processing system. However, in an EDI system there is necessarily an emphasis on programmed controls because of concurrent processing and increased accessibility of files and programs. The bulk of these programmed controls resides in a supervisory program, implying that substantially more effort is needed in the development of test data than in a traditional system. The implementation of EDI controls requires close monitoring to determine if those controls function as desired. A failure that goes undetected for a length of time can prove damaging. Methods such as the integrated test facility (ITF) have potential for EDI systems since they allow entry of test transactions into the system concurrent with production transactions.

## Systems metrics for key processing functions

Software monitors may be useful in collecting performance measurement data. The principal decision to be made when using a sampling software monitor is how frequently events should be inspected. Historical data on error types and rates of occurrence may assist in developing a density for particular types of control failure. This tool can be valuable in the closely coupled systems of EDI.

## Systems alarms

Embedded audit modules are typically designed to monitor all transaction activity and to notify the auditor of any activities having special audit significance, such as unauthorized attempts to access the system or dollar amounts in excess of specified limits. Typically, the module writes all relevant information concerning such events on a file called the audit log. The auditor may at his or her discretion request a printout of the audit log for inspection.

## System Boundaries and Flow of Transactions

EDI systems provide the potential for connecting different organizations into one large system. Most current applications of EDI use VANs. In such systems, the VAN can perform compliance checking on transaction formats, store data, maintain security over that data, and maintain transaction logs.

A large proportion of EDI systems use a third-party VAN to serve as an intermediate processing agent to handle such complexities as transformation of data formats and holding electronic mail until the recipient is ready to receive messages. VANs have shown some reluctance to allow auditors, other than their own, access to their facilities. However, this reluctance has been softened by a recognition that VAN clients are better served by allowing one reputable audit firm to evaluate their operations. The client's auditor (which may be a different firm) then at least has the benefit of a control evaluation that has been performed by professional computer-audit specialists.

A company should consider seeking the auditor's report from the VAN. This practice is not yet commonplace, but should become so as EDI becomes more pervasive.

## Concluding Remarks

Our message has been two-fold:

1. EDI systems change the control and audit environment. They introduce additional complexities in initiating, recording, and executing transactions by various participants in EDI networks. Hard copy evidence is replaced with electronic documents maintained on computer-readable media. EDI systems also transcend the boundaries of an entity, thus changing the evaluation of general controls that deal with the organization and operation of controls. Where third-party VANs are used, auditors need to evaluate network application features — either directly or through the VAN's auditor.

2. There are means available for maintaining adequate control and auditability in this environment. Managers and systems designers need to be aware of these methods and procedures so that they are provided for in the EDI implementation. We have attempted to outline some of these methods and procedures.

If EDI is to attain its potential as a business strategy, its control issues must be addressed by knowledgeable planning and implementation.

## References

EDI Research, Inc. The State of EDI: 1988, EDI Research, Inc., 1988.

Hoffman, L. Modern Methods for Computer Security and Privacy, Prentice-Hall, Englewood Cliffs, NJ, 1977.

Peters, T. Thriving on Chaos, Alfred A. Knopf, Inc., New York, NY, 1987.

Stern, L. and Kaufman, P. "EDI in Selected Consumer Goods Industries: An Interorganizational Perspective," Marketing in an Electronic Age, Harvard Business School Press, Boston, MA, 1985.

## About the Authors

Ned C. Hill holds the Joel C. Peterson Professorship in Business Administration at Brigham Young University and is one of the principals in EDI Group Limited in Oak Park, Illinois. He is editor of EDI Forum: The Journal of Electronic Data Interchange. He co-authored Short-Term Financial Management, published in 1988 by Macmillan and Essentials of Cash Management: A Study Guide, published by the National Corporate Cash Management Association in 1985. He has authored more than 50 articles in the areas of cash management, electronic data interchange, credit policy, and corporate finance. He received his undergraduate training at the University of Utah and MS and Ph.D. degrees from Cornell University.

James V. Hansen is professor of computer and information systems in the Marriott School of Management at Brigham Young University. He received a BS in mathematics from Brigham Young University and earned his Ph.D. at the University of Washington, Seattle. He was formerly a faculty member at Indiana University and a senior research scientist at Battelle Institute. His research interests focus on the use of artificial intelligence methods in decision making, data modeling, and electronic data interchange.

# Appendix

Data encryption is the process of converting a normal message (plaintext) into a non-legible message (ciphertext) that cannot be read until it is decoded (decrypted) into the original plaintext form. There are a large number of encrypting schemes that have been proposed (Hoffman, 1977).

The Data Encryption Standard (DES) is an ANSI-supported cryptographic algorithm widely used in EDI applications. DES allows for $10^{17}$ possible keys for producing cipher code from plaintext. The only party that can decrypt the data is someone who has the same key that was used for the encryption. It would be unlikely for the fastest computer to be able to discover the specific key used for encryption in any reasonable time period. Thus, key control is critical.

Authentication builds upon encryption methods. The purpose of authentication is not to provide for secrecy of data, however, but to ensure that data is not altered during transmission or storage (bank account numbers, dollar amounts, quantities order, etc.). The way in which this works is summarized below:

Examine Figure A. A plaintext message is encrypted to form the ciphertext version of the message. Then a message authentication code termed MAC-1 is formed by subtracting the key from the ciphertext. The ciphertext message and MAC-1 are sent to the receiving party. The plaintext is then encrypted with the same key, and MAC-2 is formed in the same manner as MAC-1. If MAC-1 and MAC-2 match, then the plaintext received must be the same as the plaintext sent.

![](/api/attachments/4MKGET59/fulltext/images/2935b084066549b09c1f7252af5b81c3c06919e3aa2221e8b342ed74c7a830cc.jpg)  
Figure A. Data Authentication Example
