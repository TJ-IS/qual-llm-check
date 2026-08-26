---
otero_id: 794
otero_key: "GEZRUB9Z"
title: "Managing the Internet Payment Platform project"
authors: "Janis L Gogan; Ulric J Gelinas"
year: "2007"
journal: "Journal of Information Technology"
doi: "10.1057/palgrave.jit.2000110"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Teaching case

# Managing the Internet Payment Platform project

Janis L Gogan<sup>1</sup>, Ulric J Gelinas Jr<sup>2</sup>

<sup>1</sup>Department of Information and Process Management, Bentley College, Waltham, MA, USA; <sup>2</sup>Department of Accountancy, Bentley College, Waltham, MA, USA

Correspondence:

JL Gogan, Department of Information and Process Management, 175 Forest Street, Waltham, MA 02452-4705, USA.

Tel: þ 1 781 891 2098;

Fax: þ 1 781 891 2949;

E-mail: jgogan@bentley.edu

## Abstract

This case examines issues in the assessment and adoption of Internet technologies in a federal US government context, and describes in detail a pilot project to determine the feasibility of adopting an application service provider solution to support procurement by multiple federal agencies using a variety of different legacy transaction systems. The pilot test of the Internet Payment Platform (IPP) by the eMoney group of the United States Treasury’s Financial Management Service involved three federal agencies and subsets of their suppliers. Participants saw many benefits from their use of the IPP, but agreed that for full-scale operation it needed to be modified to better fit the government procurement context. The project manager is weighing the pros and cons of conducting another pilot test using the same commercial software as before, or obtaining and customizing a new commercial package, or building a new system from scratch.

Journal of Information Technology (2007) 22, 410–419. doi:10.1057/palgrave.jit.2000110 Keywords: emerging technologies; IT project management; pilot test; eProcurement

## Managing the Internet Payment Platform project

n May 2004 Brett Smith, Program Manager for the United States Department of the Treasury’s eMoney projects, was preparing for a conference call to talk with several managers from Xign, Inc., whose software had been adapted for use in a pilot test of the Internet Payment Platform (IPP), which was scheduled to end in a few weeks.<sup>1</sup> The pilot test had run for 18 months. Three participating federal agencies – Treasury’s Bureau of Engraving and Printing (BEP), the Denali Commission, and the United States Department of Labor (DOL) – had processed nearly \$45 million payments, representing 1822 purchase orders, over Xign’s software, which supported four steps in the agency/supplier procurement process (see Table 1)

The project demonstrated that these steps in the procurement process could be supported via an Internetbased service, with appropriately strict role-based access controls that assured tight security. An ‘appreciating database’<sup>2</sup> captured purchase order, invoice, and payment information associated with each transaction, and made the information available (also subject to access controls) to participants at any time in the transaction cycle. As Smith had explained in many presentations, the IPP system was similar to Federal Express’ package tracking system – only in this case, POs, invoices, approvals, and payments could be tracked, instead of packages.

Coordinators at the participating federal agencies had expressed a willingness to participate in future pilot tests. Of course, there had been plenty of challenges during the past 18 months. Xign’s online service did not include the full range of features that were needed in government procurement operations, and it took a little longer than expected to create the middleware<sup>3</sup> that translated data from agencies’ enterprise systems for use in the IPP because some agencies used old hardware, software, and database technologies that Xign’s out-of-the box translators could not handle. However, except for several functionality gaps, the system did perform very well.

Now that this pilot test was nearly over, Smith was starting to think about how to proceed next. Before running another pilot test, a decision needed to be made about the software. Should Treasury enter into a new contractual relationship with Xign, specifying that, for another pilot test Xign’s software needed to be adapted to fit the unique needs of federal procurement processes? Smith anticipated that Xign would charge a steep fee to make those changes to the software, and he did not know whether the value-added would be commensurate with their price. Should he thank this vendor for their participation in this pilot, end that relationship, and move on? It was not clear whether some other software vendor could offer a more flexible and robust eProcurement system that could be better adapted to the unique needs of government agencies. Should he recommend that Treasury ‘bite the bullet’ and build a completely new system from scratch? Smith understood that a choice to build a new system would entail a lot of uncertainty, since IT development projects often run overtime and over-budget.

Table 1 Agency/supplier procurement process

<table><tr><td>Agency</td><td>Agency</td><td>Agency</td><td>Agency</td><td>Agency</td><td></td><td>Agency</td><td>Agency</td></tr><tr><td>Search</td><td>Qualify supplier</td><td>Negotiate termsVendor</td><td>Issue PO</td><td>Receive goods</td><td>Create invoiceVendor</td><td>Receive invoice</td><td>Approve payment</td></tr></table>

Note: items in bold represent steps supported by the Internet Payment Platform.

## Background: US treasury FMS eMoney group

The United States Treasury was one of the major departments within the US government’s executive branch. Figure 1 depicts the three major divisions of the US government and some of the major departments of the executive branch. The Treasury Department included the Internal Revenue Service, US Mint, BEP, and the Financial Management Service (FMS). FMS collected payments made to the US government, including income tax payments, and disbursed nearly one billion payments on behalf of federal agencies, amounting to more than \$1 trillion. As such, FMS was similar to a treasury function in a commercial organization, in that they did not decide what to purchase or to whom to sell products; their role was to receive payments and disburse funds as required by federal agencies. With 2100 employees located in the nation’s capital as well as four regional financial centers (Austin, Kansas City, Philadelphia, and San Francisco) and one debt collection center in Birmingham, Alabama, FMS was headed by Commissioner Richard Gregg.

FMS’s eMoney group had been formed in response to the rise of commerce on the Internet and various federal initiatives. For example, the Debt Collection Improvement Act specified (starting in 1999) that all federal payments except tax refunds should be provided electronically; FMS aimed to make 90% of Treasury Payments electronically by 2010. The Government Paperwork Elimination Act of 1998 further encouraged federal agencies to automate their business processes, and President George W. Bush added another push in ‘The President’s Management Agenda’ for his administration, which included ‘Expanded Electronic Government’ as one of five government-wide initiatives. This document stated (p. 24): ‘The Administration will advance eGovernment strategy by supporting projects that offer performance gains across agency boundaries, such as eProcurement, eGrants, eRegulation, and eSignatures.’

Smith worked in the eMoney group and reported to Gary Grippo, the FMS Chief Architect for Electronic Commerce. The eMoney group conducted various R&D Payment Application Modernization projects to assess the potential of emerging Internet technologies and to learn how these technologies could affect the banking system and government fiscal operations. Grippo summed up the eMoney group’s mission: ‘We’re trying to come up with the next generation federal disbursement system.’ While some initiatives were small-scale explorations, others evolved into full-production systems. For example, one successful eMoney project, Pay.Gov, resulted in the development of a government-wide transaction portal that provided several services: collections, acceptance of completed forms, submission of bills, authentication of end-users and authorization of transactions that they may execute, and reporting to Treasury, agencies and the public about transactions.

![](/api/attachments/GEZRUB9Z/fulltext/images/987fd780c38e3012817ea9be0f8fd63a4a9d6e3d27503b0d5af3002c4656087e.jpg)  
Figure 1 Selected elements of the US government.  
Note: This figure only depicts selected elements of the US Government.

## The proposed IPP

Smith had been Treasury’s coordinator for another eMoney project the 1998–2001 pilot test of eCheck, a web-based payment mechanism<sup>4</sup> that was the first digitally signed Internet payment. The scope of eCheck was to replace paper checks for payments between individuals, between businesses or government entities, and between individuals and businesses or government entities. The eCheck design included the ability to attach documents, such as remittance information, to a payment. The system was developed by the Financial Services Technology Consortium.<sup>5</sup> In that pilot test, payments to a few Department of Defense vendors were made via the Internet, with help from Smith’s group, working in collaboration with an R&D group at the Federal Reserve Bank of Boston. There had been some frustrating moments in that project, in part because of the large number of participants. Twenty-five FSTC member organizations were involved in designing eCheck, and 12 participated in the pilot test, with sometimes conflicting objectives.<sup>6</sup> Also, the eCheck team had attempted to propose both eCheck and the Financial Services Markup Language as Internet payments standards, but neither attempt had succeeded, largely because standards-setting organizations considered the more general-purpose Extensible Markup Language (XML) to be a superior approach.<sup>8</sup>

When the eCheck pilot test drew to a close in summer 2001, several individuals from participating banks formed two for-profit entities – Clareon and Xign – to commercialize the eCheck technology. At Treasury, Smith was asked to lead the planning for a new technology pilot test, dubbed the IPP. In fall 2001, when Smith first started to prepare a Concept of Operations (Con Ops) document, as required in the FMS planning process, Grippo specified that the IPP pilot should be narrower in scope and shorter than the eCheck pilot. He explained:

We started out y with a ten-year time horizon, trying to figure out how the payment system and government fiscal operations may change over the long-term. What we’re doing now is taking a lot of the lessons we learned from those experiences. We’re not using as much cuttingedge technology, but we’re building real systems that agencies across the government can use.

Our approach now is to do limited, achievable implementations of the technology, and take things in small bites, allow them to grow over time, and perhaps adjust our approach to improve security or flexibility as we go along. And, this time we’re not going to make any bets on a standard, since we don’t yet know what standards will ultimately win out.

Grippo also specified that no more than three Federal agencies were to participate in the IPP pilot test. If this initial pilot test worked out well, then another test could be proposed and participation at that time could be expanded.

In 2002 Smith consulted with various individuals who previously participated on the eCheck project, including people from FMS, the Federal Reserve Bank of Boston, and other organizations. An early version of the Concept for Operations document was created and vetted among various FMS offices, and by spring it was nearly completed.

## Vendor selection

During the spring 2002 planning, the IPP team discussed whether to collaborate with one or both of the two companies, Clareon and Xign, which had spun off from the eCheck project. Xign had created a system that offered a lot of potential for federal procurements processes, but Clareon’s narrow scope did not quite fit with what the team hoped to accomplish. Several other services and software products were also examined, but none were considered to be a good fit, and ultimately, the decision was made: Xign’s software would be licensed and adapted for use in the IPP pilot test, and Xign would host the service.<sup>9</sup>

Participating agencies would utilize Xign’s system to issue POs, receive invoices, and approve payments. Participating supplies would receive purchase orders in electronic form, create invoices, and track the status of their orders and payments. Suppliers did not pay for using the Xign system during the pilot. A spokesperson from Xign explained the business problem that the company was trying to solve with their ‘ePayables’ solution:

In the enterprise world today, 80–90 percent of purchase orders, invoices, and payment transactions are paper based. Handling paper purchase orders, generating paper invoices and sending those invoices to be processed and handled by a buyer and subsequently turned into a paper check that goes back to a supplier – those costs are enormous. And, an invoice floats around in mail for some period of time before it eventually lands on somebody’s desk in the buyer organization. It may or may not be the right person. Once they ultimately open the invoice and take a look at it, it may or may not refer to the purchase order associated with the invoice. It might have the wrong unit costs. All sorts of things can go wrong. In industry, up to 40% of all invoice transactions have some form of exception or invalidation associated with them.’

Xign already had several prominent commercial clients such as Bristol-Myers Squibb, Charles Schwab, Pacific Gas and Electric, Sprint Corporation, and the Tribune Company. Xign proposed to host the IPP website and appreciating database using the Xign Payment Services Network (XPSN), the software that executed each step in the procurement process. Mark Worsey, Xign’s Vice President for Client Services, told Smith that Xign’s middleware ‘Enterprise Adapter’ could easily receive data from leading software packages such as SAP and PeopleSoft, and translate it into XML format for use in Xign’s ePayables solution. Where older accounting software was utilized, as would be the case for some federal agencies, Xign would create a customized Enterprise Adapter, but this would cost a little extra.

## The Con Ops document, dated 18 June 2002 stated:

The goal of the Internet Payment Platform pilot is to continue where the eCheck pilot left off. The program is y focused on y accumulating all data involved in the entire life cycle of a transaction in a centralized database y The IPP is designed to provide web-based access for payees and payers to view data in the centralized database, manage the workflow associated with that data, verify the identity and authenticity of users and accounts, settle credit ACH transactions, and provide robust reporting and access to the database. The key is that the database continually receives and aggregates data throughout the lifecycle because it is the hub to the entire transaction exchange.

Xign agreed to provide access to their service at a substantially reduced price for the duration of the pilot test, provided that Xign would not have to make significant modifications to their software during the test. ‘The United States Treasury would be a very useful reference account for us,’ Worsey remarked. He added:

The participants will undoubtedly suggest additions to the functionality of our software, but it would not be costeffective to make those changes during a pilot test. Once the test is over and an evaluation has been conducted, that would be the time to discuss the cost of adapting the software to meet government requirements if you decide that there is a good fit for ongoing operational use.

As it happened, Xign did make some modifications, in order to accommodate how agencies and finance centers within Treasury approve payments for distribution, and how payment instructions are routed to banks. The Xign system normally routed payment instructions for each customer to their individual bank, to be settled through the ACH network. For the IPP pilot test, payment instructions went directly to the Federal Reserve Bank of Boston.

## Planned project milestones and governance

Project approval did not come quite as quickly as Smith hoped; some senior managers argued that IPP would not integrate well with existing FMS payment systems. Eventually the go/no-go decision was elevated to Commissioner Gregg, who said ‘Listen, IPP does not have to connect with every mainframe system. Let’s pilot this approach and see if it works. Let’s do no more than is necessary to test the basic concept.’ The project received formal approval in June 2002, and it was hoped that by summer’s end Smith would be able to choose three federal agencies to participate in the pilot test. In a summer 2002 presentation Smith laid out a timeline of key deliverables:

August 2002: Three agencies committed to pilot

October 2002: IPP conditionally certified and ‘ready’ for payments

December 2002: Agencies IPP-enabled

January 2003: Live transactions

January 2004: Pilot evaluation

The governance structure for the IPP project was much simpler than was in place for the eCheck project, since neither the Financial Services Technology Consortium nor commercial banks were involved. Xign provided the software and hosting hardware, and Biometrics Associates, Inc. and VeriSign collaborated to provide the technology for biometric authentication, which was used to digitally sign payments issued through the IPP.<sup>10</sup> The Con Ops document specified the project organization structure:

1. Project Executive Sponsor Dick Gregg, FMS Commissioner

2. Project Sponsor: Gary Grippo, FMS Chief Architect for Electronic Commerce

3. Project Director: Brett Smith, FMS Program Manager for FMS eMoney Projects

4. Steering Committee members: Smith, agency coordinators, and Mark Worsey, Xign Vice president for Client Services.

5. Project Manager: Bill Todd (FMS)

6. Project team members: Smith, Todd, Worsey, Holly Robedeau (FMS Business Coordinator), David Burns (Xign Director of Professional Services) and Bob King (Xign Manager, Professional Services)

The Con Ops document also specified that the project team would meet once a week, usually via conference call.

## Recruiting agencies to participate

Even before the Con Ops document was signed, Smith held informal discussions with managers at various federal agencies, such as Treasury’s BEP and the US Departments of Labor, Education, Veterans Affairs, and Transportation. He wanted the pilot test to involve agencies of different sizes and varied requirements. In particular, he wanted to have at least one agency that used standard ERP software, such as SAP or PeopleSoft. This had been Grippo’s suggestion. When Smith told Grippo that BEP was willing to participate in the pilot test, Grippo had said,

You will be tackling a difficult case with BEP, since their non-standard accounting package creates an integration challenge. I want to learn how rapidly a system such as IPP could be rolled out across many agencies. By focusing on users of standard ERP software, we’ll get a better idea of scalability.

In 2002 and 2003 Smith gave at least 20 presentations about IPP, at various federal conferences and in meetings that he set up within agencies. Figure 2(a–f) contains excerpts from his presentation. All told, he talked to about 200 people about IPP. ‘Selling is an under-appreciated art,’ he remarked to a colleague.

What’s challenging about these presentations is this: I have to connect with multiple audiences simultaneously. At any given meeting with an agency, there will be an attendee from procurement, somebody from the CIO’s shop, people from finance, and some accountants. Each has their own concerns and they speak different languages, in a way. We need them all to participate in this, since it’s a process redesign exercise, but they may have never even met each other before, because they haven’t previously had to collaborate. So, my job is to speak to each of them on their terms, and try to persuade them that this IPP project is a great opportunity.

Many people applauded the ‘appreciating database’ concept. However, once negotiations began in earnest, Smith found that enthusiasm did not necessarily lead to participation. Many different reasons were offered for holding back. One large federal agency, the Internal Revenue Service, stated that they were not interested in committing resources to a small, limited-scope pilot test. ‘Call us when you are ready to do something large-scale,’ was their comment. Other agencies noted that while interested, they were constrained by the federal budgeting cycle. ‘We are already committed for the remainder of this fiscal year, as well as for the next one, but we could look into it and consider adding it to our priorities for 2004,’ they stated. Some agencies had more latitude in their budgeting requirements, but were busy with other IT projects, including large-scale ERP deployments. ‘We just don’t have the resources to manage yet another risky IT project,’ was one agency’s response.

The August 2002 agency sign-up milestone was missed. An official project ‘kickoff’ took place in October, with much-publicized demonstrations and presentations about IPP, attended by many agency representatives.

a  
![](/api/attachments/GEZRUB9Z/fulltext/images/e8d4974a5dbc8d6d193108656f75aa7e250197b9f7401d11dcc0ce9b63e82ec8.jpg)  
Problem: Data Degradation and Solution: Data Aggregation

![](/api/attachments/GEZRUB9Z/fulltext/images/afd166f77a66d3506d6f431a719294cf15a13c123c4273577f4c02eb98859e96.jpg)

## b Echeck II is the Internet Payment Platform

• Internet Payment Platform is…

– Electronic payments infrastructure

– Central Internet service operated by Treasury

– Portal model: consolidated, integrated service

– Built in conjunction with Federal Reserve

## • Centralized mode

– Economies of scale and scope

– Unified security architecture

– Avoid duplication of investment

• Scope: limited, achievable pilot: 12 months, up to 3 agencies

c  
![](/api/attachments/GEZRUB9Z/fulltext/images/c64ed1c258d9cc055d4f1ebf181ed024b0e9fa872f5ef151f92366109349550c.jpg)

![](/api/attachments/GEZRUB9Z/fulltext/images/575a01a6da9c685022e7d0a194553744ef232016ab31fa55ac6ff243c0626541.jpg)  
e

![](/api/attachments/GEZRUB9Z/fulltext/images/0b6c06daaee42ac952b06f12c2155067cca7777801873675c36d7b9256f652d7.jpg)  
Figure 2 Excerpts from Brett Smith’s IPP presentation to federal agencies: (a) Problem: data degradation and Solution: data aggregation; (b) Echeck II is the Internet Payment Platform; (c) IPP interfaces and architecture; (d) Enterprise adapter; (e) Vendor view: PO inbox; (f) Vendor view: PO flip and Agency view: invoices pending.

## The BEP pilot

By November one agency had committed to participate in the pilot test: the US Treasury’s BEP, which manufactures US currency. BEP’s Chief Financial Officer, Gregory Carper, felt that it was important to support its ‘sister’ organization, FMS. Numerous previous collaborations had yielded good relationships between the two organizations, so the IPP pilot test was not seen as a terribly risky endeavor – particularly as Smith had offered assurances that his office would handle much of the necessary technical work. Carper saw participation as a way to demonstrate his organization’s commitment to furthering President Bush’s Management Agenda, which called for effective use of IT to improve the timeliness and effectiveness of operations, and, a finance manager explained a helpful aspect of the Bureau’s position: ‘BEP is a revolving fund, with so-called No-Year money. We can fully fund multi-year initiatives and can change our spending plans. Unlike most agencies, we don’t depend on (yearly) appropriations from Congress for our funding.’ Since the Bureau was self-supporting and operating with a surplus from the sales of currency and stamps, they were able to commit resources to the IPP project on short notice, unlike most of the other federal agencies.

Vendor View: PO File  
![](/api/attachments/GEZRUB9Z/fulltext/images/1fc8737a227590e760726e7e77c563b308ec3d285c8d06f6800272a2b90c6279.jpg)

Agency View: Invoices Pending  
![](/api/attachments/GEZRUB9Z/fulltext/images/9d00d4b08cbd9b6ed4bcf0c77a3031836a0fb2b64fa94d90aafb57da760a9617.jpg)  
Showing 1-5 of 5  
Figure 2 Continued.

Once BEP had signed on, Bob Deans, a manager in the Bureau’s Financial Systems and Accounting Division, was appointed as the BEP coordinator for the project. The IPP team, staffed by IT professionals from FMS, BEP, and Xign, turned its attention to creating the Enterprise Adapter. This middleware would allow BEP’s legacy purchasing and accounts payable systems to export transactions to the Xign software as XML messages, and subsequently receive updates that would be translated back from XML into the format required by the legacy software. Reviewing the software and creating the middleware took longer than expected, because BEP’s software did not produce output in the form that Xign expected. Smith noted: ‘It was as if people were speaking completely different languages – but sometimes they didn’t realize it. BEP figured their software was EDI-ready, but Xign had a different idea of what ‘‘EDI-ready’’ means.’ While it was true that BEP’s accounting software could produce messages for EDI, it was still necessary to format those messages according to newer standards. BEP’s IT group worked mostly with older mainframe hardware, software, and development methodologies, while the IT professionals from Xign were well trained in XML, object-oriented languages, and opensource software.

The middleware work was well worth doing, in Smith’s opinion, since it increased the commitment level of BEP employees from IT, financial management, and procurement. It also revealed that Xign’s software, written for a commercial context, did not quite fit the government context. For example, BEP purchase orders often included large amounts of text containing stipulations and conditions required by the Federal Acquisition Regulation, but the Xign software did not accommodate this requirement. When Deans requested that Xign customize their software to fit BEP’s needs, Smith explained the conditions under which Xign was participating in the pilot test. ‘They gave us a large discount for use of their software in the test,’ he explained. ‘In return, we agreed not to request any customization.’ However, Xign did make some changes, such as an audit trail of purchase order modifications and adding an ‘Approved to Pay’ field to the payment status categories.

Once the middleware work was done, a team at BEP did extensive pre-pilot testing of the system, since management did not want to involve any suppliers until they were reasonably confident that nothing would go wrong.

By the end of February 2003, the managers, accountants, and IT security experts at BEP were satisfied that the IPP system would run securely and not adversely impact data quality. So, BEP agreed to ‘certify’ the software for approving and making payments in the pilot test. At that point the purchase order-to-invoice ‘flip’ functionality, by which data from a PO was automatically transferred into an invoice, was not yet fully debugged. So, for the time being, participating suppliers would create invoices the traditional way, but receive their payments through the IPP. BEP procurement specialists and accountants continued to grumble a bit about other missing functionality. Smith felt that these employees did not fully appreciate how different their mainframe-era accounting systems were from Xign’s newer architecture. Had BEP used a more current ERP package, such as SAP or Oracle, it would have been a much easier task to integrate with Xign’s system.

The project plan specified that up to 25 suppliers would participate per agency, but Deans told Smith, ‘My people want to proceed slowly and cautiously, because we don’t want to hurt our relationship with any of our suppliers.’ So, only two BEP suppliers were introduced to the IPP system at first. One, a small distributor, supplied large quantities of relatively small-value items such as plumbing and electrical supplies; this supplier typically issued 200 or more invoices per year, at a value of more than \$300,000. The other company was the sole supplier of the highly specialized ink that was used in US currency; BEP managers were particularly concerned that nothing go wrong with this key supplier. Conversely, managers at this supplier were also concerned that nothing go wrong, since BEP was their largest customer. Smith was pleased that the two suppliers differed greatly in the systems that they used to run their own businesses, in the number of employees dedicated to fulfilling and accounting for customers’ orders, and the characteristics of the orders themselves.

In March 2003, the first BEP payment using the IPP system was made to the small supplier, East Coast Sales.

Soon after, the larger supplier, SICPA, also received a payment. Over the next several weeks the BEP team reported that all was going well, and that employees at BEP and the two supplier organizations were enthusiastic about the system. ‘They can see how IPP could save time, improve efficiency, and dramatically reduce the many phone calls that we typically receive from vendors wondering when they will be paid,’ said Deans. Still, he added, BEP managers had decided that they would prefer not to recruit additional suppliers for the pilot test, until the ‘PO Flip’ feature was fully debugged and certified for use.

## Recruiting two other agencies

In April 2003, Smith had ‘serious discussions’ with managers from the DOL, who seemed to be on the verge of committing to the pilot test. DOL, with more than 17,000 employees, is comprised of multiple agencies and offices, such as OSHA and the Employment and Training Administration, which administer federal labor laws related to workers’ health and safety, wages, and employment discrimination. Like BEP, DOL used an older accounting system, a 15 year-old mainframe COBOL-based system with a hierarchical database, and a separate procurement system. In the next year or two, Labor expected to upgrade to new ERP software and a relational database. Labor’s Director of Financial Systems, Dave Sawyer, was quite interested in testing Xign’s workflow module. Sawyer, who previously worked as a consultant with Accenture, had been a government employee for just eight months, and Smith was impressed with his many ideas for improving Labor operations. Sawyer told Smith, ‘This IPP pilot looks like a great opportunity to do some streamlining of business functionality, automate some workflow and tighten down the purchasing process, with more control.’ He added that the workflow component would be especially important, both from an operational standpoint and due to the audit trail that would reside in the IPP database. ‘My boss (Labor’s Chief Financial Officer) is always talking about moving from an operational focus to a decision support focus. IPP would help us capture important information such as how long it takes for a transaction to flow through. It should be very useful.’ However, Sawyer cautioned it would take another month or two before he could make a firm commitment on behalf of the Department.

Smith was eager to get a commitment from DOL, but he told Grippo that this might take some time. ‘DOL has many different divisions, and I guess there are many layers of approval. I hope they can get on board by September.’ Several other agencies also expressed interest in the IPP pilot, but chose to remain ‘on the fence’ until this first phase was completed. ‘They indicated that they could be seriously interested once we are able to tell them how it goes with these first few agencies,’ he explained.

Smith was unhappy with the delays at DOL, but his spirits improved when in late July, the first PO-to-invoice ‘flip’ was finally conducted, to rave reviews from the owner of East Coast Sales. Shortly thereafter SICPA also did their first PO flip. They were a little less enthusiastic about this particular feature, since it required that an individual log on to IPP, review an order and manually initiate the flip. SICPA wanted to use Xign’s eFile option, a service that would translate a vendor’s invoice from the vendor’s billing system into invoice data for recording in the IPP database. However, this function was not implemented during the pilot test.

Now satisfied that IPP was working well, managers at BEP agreed to enlist additional suppliers to the pilot. Another 30 BEP vendors eventually signed up to participate and 25 actually did use the IPP during the pilot.

In July one more agency, the Denali Commission, agreed to participate. With just 19 employees, this small agency had been able to make their decision within only a few weeks of Smith’s first presentation to them. But, Denali was in the process of converting from QuickBooks to Great Plains software; that cutover date was set for 24 October. Although Great Plains was not a package typically used by federal agencies (since it is designed for smaller organizations), Xign indicated that it would not be difficult to create the necessary Enterprise Adapter.

In August, Smith got more good news: Dave Sawyer finally gave the ‘go ahead’ for Labor’s participation. The target go-live date was set for early November. Again it would be necessary to create middleware that would enable Labor to extract transactions from its legacy accounting software, and an Enterprise Adapter to translate the data into XML for use in IPP, and to return data to the legacy systems. Integration work was also needed in order to implement the workflow module.

## Re-evaluating the one-year milestone

In September, the Denali Commission enrolled 12 vendors on the IPP system, and beginning 25 September, the payment approval and remittance functions were tested with five vendors: a small local photographer, the property maintenance company for the Commission’s offices in Alaska, and lawyers and a consulting firm located in other states. The operations manager in Anchorage noted that many smaller vendors were reluctant to enter their invoices into the IPP system, but quite a few were interested in receiving payments electronically. The purchase order creation and flip-to-invoice features were not tested right away because the operations manager felt it would make more sense to try that functionality after Great Plains was installed, along with its Enterprise Adapter. And, a decision was made to temporarily suspend the IPP pilot from 2 October until the Great Plains cutover date of 24 October, in order to ensure a clean cutover.

In early November, Smith learned that Denali’s cutover to Great Plains did not go quite as smoothly as planned; additional work had to be done before they were in a position to resume their participation in the IPP pilot test. Most software cutovers entail some unexpected surprises, he figured, so this was not cause for alarm.

Unfortunately, there was also a delay in Labor’s go-live date. The IPP project plan and the contract with Xign specified that the pilot test would terminate at the end of December, so Smith had to ask both Grippo and Xign to agree to an extension of the test. He had not wanted to have these conversations until both Denali and DOL were up and running properly. Finally, in late November, Smith learned in the weekly conference call that Denali had resumed pilot testing, and the integration between IPP and Great Plains software was working beautifully. And, the DOL was also up and running.

With just one month left on the contract, an agreement had not yet been reached with Xign on whether to extend the pilot test and if so, for how long and at what price. Worsey expressed the opinion that the work with BEP had been sufficient to demonstrate the applicability of Xign’s software to government procurement, and it was clear from that experience that Xign could successfully integrate with quite old mainframe systems. He assured Smith that if a decision was made to invest in Xign for the long term, it would not be a problem to accommodate BEP’s requested changes (such as increasing the amount of allowable text appended to the PO). With each new agency, the implementation had been accomplished more quickly, and both suppliers and agency personnel were pleased with the IPP and did not want to stop using it. The time was right to talk about a long-term contract, Worsey said; he favored a pricing scheme comprised of fees for customizing the software and launching the integration, plus a small fee for every transaction processed in the IPP.

Smith talked about this with Grippo, who was not prepared to ask senior management to approve such a deal in December 2003. ‘It’s too early,’ he stated.

The BEP transactions so far are mostly with just a few vendors, and you haven’t yet had enough experience with Denali and DOL. Besides, Xign needs us a lot more than we need them. Having the US Treasury as a customer gives a company a lot of marketing credibility.

Smith phoned Worsey with the news: ‘We propose to continue the pilot for six more months, with the current three agencies. We are willing to continue paying you the same monthly amount you’ve been getting for hosting the system.’ Worsey counter-proposed that Xign could do the customization that BEP had requested for an additional fee but Smith’s answer was no. ‘Until we know what the long-term prospects are, it doesn’t make sense to do that work,’ he said. Worsey brought this news back to his colleagues at Xign, and before the end of December a new contract was signed for a six-month extension. At that time Smith explained to Worsey that consultants from McKinsey were working on a report that apparently was going to recommend major changes to the US Treasury’s overall IT architecture and IT governance processes. ‘Once the consultants’ report comes out – in February, I hope – we’ll be in a better position to continue our conversation about a longer-term relationship.’

In January and February, the IPP pilot test ran smoothly at all three agencies. Each week, new suppliers came on board, and Smith received much positive feedback about the IPP, as well as some suggestions for improvement. While awaiting the McKinsey consultants’ report, Smith worked with coordinators from the three agencies and the Boston Fed to design a formal assessment of the IPP. Questionnaires were distributed and structured telephone interviews were conducted with agency and supplier personnel. Overall, the results indicated that participants’ reactions were quite positive. Suppliers generally rated the IPP experience as ‘good’ or ‘excellent,’ and agency personnel also spoke positively about the experience. Most respondents stated that they would be happy to participate in future pilots, and many expressed the opinion that the IPP should continue to be used at their agency and should be extended to other agencies.

In May 2004, 15 additional supplier surveys were again distributed and completed, to capture the viewpoints of some IPP latecomers. Again, the results were positive and many said that they would support future eProcurement initiatives. In addition, the three agencies were asked to calculate the cost of performing the processes associated with issuing a PO, handling a vendor invoice, and generating a payment, with and without the IPP. Using Activity-Based Costing (ABC) analysis, the per-transaction savings with IPP were determined to be \$23.18 for BEP, \$50.34 for Denali, and \$11.44 for DOL.

Also in the spring the McKinsey consultants presented their report to senior management. McKinsey had been asked to recommend changes that would give FMS a more coherent, cost-effective and efficient IT architecture and governance structure. Smith had been eager to learn what McKinsey might say about the eMoney R&D programs, including IPP. He knew that some senior FMS managers held the view that greater efficiency and coherence would be achieved if the eMoney projects were managed under the CIO’s authority. Now, Smith learned that McKinsey had recommended a new IT governance structure, and it had been approved. Hereafter, new IT project proposals would be vetted in several new governing boards, representing multiple constituencies.

Not long after the release of the McKinsey report, several personnel changes at FMS were announced, including that Gary Grippo was promoted to Assistant Commissioner. Grippo now reported to FMS Commissioner Gregg. Some changes were also announced at the Boston Fed: several key individuals were retiring or otherwise leaving the Fed. So, Smith realized that future collaboration with the Boston Fed would entail a new set of personal relationships. He had greatly enjoyed working with the current team and was sorry to see them go.

## Next steps

On a Monday morning in May 2004, Smith met with Gary Grippo. After congratulating him on being promoted to Assistant Commissioner, Smith de-briefed him on the project, the survey results, and the ABC analysis. Smith added, ‘I’m very pleased. There were no lost payments, no security breaches. IPP performed well. And, nobody wants us to pull the plug on it!’ Grippo thanked him for this work and then stated:

FMS builds mission-critical systems that every agency relies on. So, what I really wanted to learn was: organizationally and procedurally how do you roll out a new piece of enterprise software like this that will touch every agency? What are effective strategies and mechanisms for rolling something like this out? I wasn’t particularly worried about the technology aspects.

Smith had an answer for that:

We learned a lot about rolling out new software. We got better over time: our deployment with BEP took six months, Denali took four and a half, and Labor took three months. We were able to grab that experience curve and ride it; we executed faster with each deployment.

Now Smith needed advice. He explained that Xign wanted to retain control over its source code. Smith felt FMS should own the code and do their own upgrades. Grippo did not share this concern, but he did have questions about Xign’s pricing model for ongoing use beyond a pilot test. Smith explained that Xign saw each federal agency as a separate customer, whereas in Smith’s view, Treasury was one customer. ‘So, Xign sees a \$10 million opportunity here. I’m not comfortable with a price in that range, nor am I comfortable with a per-transaction model; we are currently very far apart in these negotiations.’

Grippo encouraged Smith to consider multiple options. ‘You chose this provider because you were comfortable with some aspects of their platform, which grew out of the eCheck project,’ he stated. ‘You don’t necessarily have to live forever with that choice. Maybe you’ll want to move to our production environment with different software, maybe not.’ After further discussion, Smith promised Grippo that by the end of the week, he’d lay out the pros and cons of several courses of action, and offer his own recommendation. As he walked back to his office, Brett Smith was not at all sure about the pros and cons of writing a new contract with Xign, selecting another software vendor or perhaps building a new procurement system that would be tailored to the needs of Treasury and federal agencies. Each choice entailed risks. Certainly, building new software would take a long time and involve a lot of uncertainty, and buying or licensing software or services from a vendor other than Xign would also bring new challenges.

Whatever choice he recommended – stay with Xign, build a new system, buy another one – by the end of the week Smith would need a plan of action that would address both this question and other concerns related to eProcurement. And, thanks to the McKinsey consultants’ report, Smith’s recommendations would be aired in a whole new governance structure, with multiple boards and multiple kill points. ‘This is brand new territory,’ he mused.

## Acknowledgements

We thank Brett Smith, Dick Gregg, Gary Grippo, and numerous employees at Xign Inc., the Federal Reserve Bank of Boston, the US DOL, the Denali Commission, and the US Department of the Treasury’s BEP for giving their time and thoughts during this study. Thanks also to Christine Williams, who participated in this research but opted out of this paper, and to other members of the Bentley College Invision Project, who participated in analyzing data from this study and comparisons with other case studies of inter-organizational information sharing: Jane Fedorowicz, Lynne Markus, Amy Ray, and Catherine Usoff. Lastly, we thank Bentley College for providing funding and release time in support of this work.

## Notes

1 This case study was prepared by Janis L Gogan and Ulric J Gelinas of Bentley College as the basis for class discussion. The case is not intended to serve as an endorsement, source of data, or an illustration of effective or ineffective management.

2 ‘Appreciating database’ was the term used by Smith to describe the ‘data aggregation,’ vs ‘data degradation’ that would take place as the procurement process progressed from PO through payment. See Figure 2 for slides depicting these concepts.

3 Middleware refers to the software that connects two or more separate applications or software modules. Middleware might be used to stitch together a number of legacy systems, an ERP system, best-of-breed applications, and Web-based applications.

4 See Gogan, J.L. and Gelinas, U.J. The FSTC Electronic Check Project. Case no. 96-10, American Institute of Certified Public Accountants Academic and Career Development Division Case Development Program, January 1997. Online at http:// www.aicpa.org/members/div/career/edu/caselist.htm

5 See www.fstc.org

6 See Gogan, J.L., Gelinas, U.J. and Rao, A (2004). Is This Pilot Test Over? Annals of Cases on Information Technology 6: 22–40. 7 For example, www Consortium and IEEE.

8 See Gogan, J.L (November 2005). Punctuation and Path Dependence: Examining a vertical IT standard-setting process.Electronic Markets 15(4): 344–354.

9 By hosting the IPP and providing the software, Xign was an application service provider (ASP), an organization that provides computer-based services over the Internet.

10 A smartcard stored fingerprint templates and digital certificates for those authorized to approve payments allowing these individuals to authorize payments, in a completely secure manner, from any computer communicating with the IPP server.
