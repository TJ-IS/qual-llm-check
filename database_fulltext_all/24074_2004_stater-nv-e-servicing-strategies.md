---
otero_id: 24074
otero_key: "K695TBG5"
title: "Stater NV: E-Servicing Strategies"
authors: "Scott L Schneberger"
year: "2004"
journal: "Journal of Information Technology"
doi: "10.1057/palgrave.jit.2000014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Teaching case

# STATER NV: e-Servicing strategies

Scott L Schneberger

Georgia State University, GA, USA

Correspondence:

SL Schneberger, 5175 Ivy Green Way, Mableton, USA.

Tel: þ 1 404 651 3826;

Fax: þ 1 404 651 3842;

E-mail: scott@schne.org

## Abstract

After 2 years of on-line experiments, Tom van Vianen, CEO, felt certain it was time to fully implement STATER NV’s new ‘e-servicing’ concept with a cohesive strategy. Established in 1997 in The Netherlands and headquartered in Amersfoort, STATER had 27 business clients and serviced over 80 different mortgage portfolios of more than 450,000 mainly residential loans in the Netherlands, Belgium, and Germany. Their mortgage service operations and information systems were considered state-of-the-art in 2002, but they were moving business on-line while simultaneously increasing the types of services provided and expanding operations into Spain, France, and Italy — within the next five years. In a land known for taming the forces of the sea, Tom faced what seemed like a sea of ‘e-uncertainty.’ What exact roles should STATER play in an on-line loan market? How should they position themselves to lead in those roles? The E-Servicing Steering Committee looked to Tom to direct them, and he knew he needed a clear vision for the next Steering Committee meeting in 2 months, in May 2002.

Journal of Information Technology (2004) 19, 108–116. doi:10.1057/palgrave.jit.2000014 Published online 20 July 2004

Keywords: e-services; e-commerce; banking; Europe; mortgages; information systems; strategy

## STATER NV

S <sup>TATER</sup> <sup>NV</sup> <sup>was</sup> <sup>the</sup> <sup>leading</sup> <sup>provider</sup> <sup>of</sup> <sup>independent,</sup>third-party residential mortgage servicing in conti- third-party residential mortgage servicing in continental Europe in 2001. It was focused on managing all payment and ancillary back-office functions–streamlining the origination, servicing, and securitization of residential mortgage loans in a completely automated and paperless format.

STATER was established in 1997 as a spin-off of the mortgage business unit of Bouwfonds Nederlandse Gemeenten, one of the largest mortgage lenders in The Netherlands. Bouwfonds was established in 1946 by the Dutch municipalities to rebuild Holland after World War II by providing low-cost housing and financing. Bouwfonds’ residential mortgage subsidiary, Bouwfonds Hypotheken, eventually became the fifth largest lender in the Dutch market. In 1997, Bouwfonds launched an effort to ‘unbundle’ the residential mortgage business by creating STATER NV. In 1999, STATER opened its first office abroad in Bonn, Germany – a country with a residential loan market five times the Dutch market. In 2001, ABN-AMRO (the eighth largest bank in Europe and the 17th in the world with over 3400 branches in more than 60 countries) acquired the leading share of STATER. STATER in turn acquired the back office of CBHK in Belgium, thereby establishing its second international office. In April

2001, US-based General Motors Acceptance Corporation (GMAC) began originating mortgages in The Netherlands through STATER NV. By the end of 2001, STATER had 435 employees, 27 business clients, serviced over 80 different mortgage portfolios with more than 450,000 loans, and gained revenue of more than US\$49million (\$55.4 M Euros at 1 January 2002 exchange rates). The STATER corporate organization chart is shown in Appendix A.

## STATER information system

The STATER mortgage information system (SHS, for Stater Hypotheek Systeem) was the very heart of the business and was considered to be state-of-the-art in the mortgage servicing business. The SHS supported the complete mortgage process from loan origination to servicing (the primary market) to securitizing (a secondary market). While the mortgage system was developed during 1994– 1997 for Bouwfonds to support a single mortgage lender, it was subsequently adapted to service multiple lenders. In 1999, STATER developed a German version of the SHS for its German operations based on a copy of the Dutch system. Not only was system text translated into German, but system functions were also adapted to the requirements of the German mortgage market.

Table 1 Mortgage value chain

<table><tr><td>Process step</td><td>Involved parties</td></tr><tr><td>1. Marketing</td><td>Independent brokers, lenders, consumers</td></tr><tr><td>2. Origination; processing applications, generating offers, closing</td><td>Lenders, brokers, notaries, consumers</td></tr><tr><td>3. Servicing</td><td>Lenders, consumers</td></tr><tr><td>4. Funding, underwriting</td><td>Lenders, investors</td></tr><tr><td>5. Trading</td><td>Lenders, investors</td></tr></table>

Table 2 SHS process flow

<table><tr><td>Process</td><td>Functions</td></tr><tr><td>Origination</td><td>Application processing through closing</td></tr><tr><td>Servicing</td><td>Servicing until full redemption of a loan</td></tr><tr><td>Funding</td><td>Supporting lenders and investors</td></tr></table>

SHS was developed for the traditional mortgage value chain (see Appendix B) as shown in Table 1.

This process flow was reflected in the original SHS functional structure shown in Table 2.

(Appendix C gives an overview of the SHS application architecture and the main subsystems of the SHS in 2002.)

With small, competitive margins in the mortgage business, one of the most important SHS system design principles was to achieve cost efficiency in the mortgage process by taking the process flow as a starting point in the design and automating, where possible, all process steps. The workflow concept had a central role in the origination process that had a fixed sequence of steps; in the servicing module this workflow was embedded in events that triggered automated actions, both from the system and the user (based on tasks in a work list).

The most crucial subsystem of the SHS was the automated underwriting subsystem (called Capstone). This subsystem could make automated credit decisions based on rule-based and credit risk models developed using neural artificial intelligence and data mining technologies. Capstone contained the credit rules and risk models of each lender, making it possible to significantly streamline the loan origination process – tailored for each lender. When an application was entered into the system and an employee wanted to generate an offer, Capstone compared the application with the lender’s credit rules as well as performed an automated check with a credit bureau. Lender employees could see the results of the credit check on a system monitor, but the built-in rules were determinant. If the system did not approve the loan, it was impossible to generate an offer without the approval of an authorized credit officer; if the system approved the loan, it automatically generated a conditional offer. During the fulfillment process, derived customer data were compared with the submitted customer documentation. If these data were consistent, the loan received final approval and was closed.

In practice, the system automatically generated over 90% of STATER’s loan offers; lender credit officers intervened with and analyzed only 10%. This was tremendously efficient and made it possible to send an offer (or a rejection) to all consumers within 24 hours. Most importantly, however, automated underwriting created opportunities to outsource part of the loan process to brokers because the system ensured compliance with their own credit rules. STATER could capitalize on its SHS investment by providing SHS processing to brokers, on behalf of its clients, as an outsourcer. Instead of just servicing existing loans, STATER could support the entire loan process as the information processing hub for brokers and lenders.

As a loan service hub, STATER could take the lead in other, wider initiatives. In the Netherlands, STATER led lenders and brokers to develop a standard Electronic Data Interchange (EDI) format for submitting electronic mortgage applications. Loan applications in EDI format were sent over a dedicated communications network to lenders and to STATER as the third party servicer. STATER developed a subsystem that validated EDI messages and then fed them automatically into Capstone for generating offers. The success rate of these EDI-formatted applications was initially very low – due to data inconsistencies and missing fields in the messages – but it showed it was possible to fully automate the process from application through generating an offer as a third party servicer. From this to using the Internet as the communications channel seemed only natural.

## STATER and the Internet

## The EUBOS Website<sup>1</sup>

STATER’s initial leap into servicing the loan process through the Internet happened almost by accident. STATER did not have a clear Internet strategy in 1999 when the Bank of Scotland approached STATER with their intent to use STATER and the Internet as its main distribution channel in foreign markets. Aware of STATER’s SHS and its potential benefits, the Bank of Scotland wanted to create a dedicated website with STATER in the Netherlands where consumers could get information on Bank of Scotland products, use calculators and other software to determine their mortgage options, and apply online for a mortgage. Ideally, consumers would then receive a return electronic offer by e-mail or through the website within a very short period. A call center would be set up to answer customer questions or contact a customer in case of missing information or documents, or to offer personal advice. By using STATER, the Bank of Scotland could quickly establish a lender presence – albeit virtual – in The Netherlands. By eliminating human brokers in the loan process value chain, the Bank of Scotland could also avoid paying loan commissions—and could thus reduce the loan rates charged to consumers. They hoped these reduced rates would provide them a competitive advantage over other Dutch lenders. It was clear to the Bank of Scotland that the capability of STATER’s SHS to electronically process loan applications could be used with the concept of on-line webbased mortgage applications to achieve business presence, reduce costs, and hopefully offer other business opportunities.

STATER and the Bank of Scotland formed a combined project team to implement the online capability. They agreed that the Bank of Scotland would be responsible for designing the website and the web infrastructure, and that the STATER team would be responsible for receiving and processing web-based applications through SHS-Connect.<sup>2</sup> To reduce SHS-Connect software changes, they also agreed early on that the format of the web-based application would comply with the existing EDI application format. Handling the applications that did not pass the formatting validation checks or the Capstone credit checks, however, would be very different. In the EUBOS web-based model, there would be no broker involved to contact a consumer in the case of a rejected application. This would be, in essence, a direct business-to-customer (B2C) model – and such a model was totally new for STATER. Moreover, retaining potential customers was very important to the Bank of Scotland. So they decided to extend the SHS with a database of invalidly formatted and rejected applications that could then be accessed by call center personnel. The customer fulfillment personnel could work on adding or correcting data fields by contacting customers and then re-submitting the application for validation and credit check. Throughout the process, consumers could track their application in a secure part of the EUBOS site. The SHS system would send electronic status messages and – if the application was approved – a mortgage offer.

The launch of the website at the end of 1999 attracted a lot of media attention – and shocked the incumbent banks because a foreign bank had succeeded in entering ‘their’ market without having to set up a complete ‘on the ground’ operation. The Internet, a call center, and a third party servicer (STATER NV) were all the Bank of Scotland needed to enter the local residential loan market. The entry barrier to the Dutch mortgage market suddenly appeared to be disturbingly low. Willie Donald, Director of European Operations at Bank of Scotland commented:

EUBOS has proved very successful so far. The number of hits to the site has exceeded all expectations. The virtual age is truly upon us when a business can operate to such an extent, and profitably, with such a small core team of three people.<sup>3</sup>

## Application service providers

Not only did STATER want to provide consumers with fast, effective loan servicing, STATER wanted to provide clients like the Bank of Scotland with business information. As STATER’s business increased, so would the burden of implementing an increasing number of system connections with brokers, lenders, investor credit officers, and employees that worked from their homes. In the beginning, individual users had to dial in to connect, and multiple user environments used dedicated point-to-point connections. Both created an increasing burden on systems processing and information technology personnel – raising costs substantially. IT people had to install equipment and software, provide training, and in most cases give on-site technical support. Connecting through the Internet offered a much simpler and less costly communications alternative – and it allowed STATER to take advantage of application service providers.

Application service providers (or ASPs) are essentially outsourcers for information systems that ASP clients or client customers access through the Internet. ASP services ranged from complete system development, implementation, operation, and maintenance to simply hosting a website. While there were many potential benefits and risks to using ASPs, most of the benefits were tied to the benefits of the Internet as a communications channel and to ASP economies of scale. STATER thought it could take advantage of both.

It seemed possible to have an ASP host the full SHS interface (the mortgage system and electronic loan files), making SHS available to a very wide range (and reach) of potential clients. As long as a client had an Internet connection, a computer with common Internet browser software, and authorized access, the client could access the SHS at anytime and from anywhere in the world. This could quickly create enormous business value for STATER’s SHS and Capstone system – and for business clients who could use their existing Internet infrastructure to access and use STATER services. From STATER’s perspective, the Bank of Scotland could be the beginning of a wide range of loan business relations with STATER’s SHS at the core.

It was clear to Tom and STATER management that SHS and the Internet provided enormous business opportunities. STATER could be the hub of all the stakeholders in the mortgage value chain (Appendix B), and the Internet appeared to be the perfect way to connect STATER and the stakeholders – and give them data access to their part of the mortgage value chain. This vision became known as ‘eservicing’ and it was the umbrella for all STATER Internetrelated projects.

## e-Servicing

In 2000, STATER defined e-servicing this way:

E-servicing is to give business relations and consumers access to data and functionalities of the SHS, anytime and anywhere, provided that they have the appropriate authorization. The use of Internet technology is essential for realizing the e-servicing concept.

An e-Servicing Steering Committee was formed to guide and monitor STATER’s move into online mortgage servicing as shown in Table 3.

The committee met every 2 weeks. They decided they needed an integrated framework or e-strategy for the projects to guide project prioritization.

## e-Servicing applications

It was apparent to the Tom and the Steering Committee that business relations, or clients, could potentially use STA-TER’s information systems in three basic ways (see Table 4):

The Committee then turned their attention to developing specific applications to perform e-servicing functions, initially focused on the home market (The Netherlands). These were, in chronological order:

Table 3 e-Servicing steering committee

<table><tr><td>Name</td><td>Corporate position</td><td>Responsibilities</td></tr><tr><td>Tom van Vianen</td><td>CEO, STATER NV</td><td>Chair, corporate strategy</td></tr><tr><td>Richard Jansen</td><td>Senior VP, STATER Netherlands</td><td>Business clients</td></tr><tr><td>Harry Mulder</td><td>Senior VP, STATER Information Technology</td><td>IT strategy and implementation</td></tr><tr><td>Caroline Meyer</td><td>Director, Corporate Business Development</td><td>Corporate expansion strategies</td></tr><tr><td>Wilma Flohr</td><td>Director, Corporate Communications</td><td>Public relations</td></tr><tr><td>Johan Gessel</td><td>Program Manager, E-Servicing</td><td>Project development and implementation</td></tr></table>

Table 4 Potential e-Servicing functions

<table><tr><td>Business function</td><td>Business relation</td></tr><tr><td>Information upload to SHS</td><td>STATERBrokersLendersFront-office supportNotariesConsumers</td></tr><tr><td>Information modification in SHS</td><td>STATERBrokers (applications, offers)Front-office supportNotaries</td></tr><tr><td>Information retrieval from SHS</td><td>All business relations</td></tr></table>

\- e-Application: A simple Web page where all the necessary data for a mortgage application could be entered and validated. It was to be used by brokers and lenders to quickly enter application data using an ordinary browser communicating with the SHS. e-Application data would be processed using the same technology infrastructure used by EUBOS.

\- e-Notary: Notaries played a pivotal role in the loan process by closing the deal, and were hired by loan consumers. If the e-servicing hub could automate and improve the efficiency of the notary task, STATER could then more easily branch into the other loan process steps. The simply stated objective of this project was: ‘to optimize and speed up the information exchange between a notary and STATER using the Internet.’ Tom set out to build the capability for notaries to go to the STATER website using a browser and access a secure part of the site to see the status of all the loans the notary had been appointed to complete. When all requirements for closing were fulfilled, the notary would be able to request – on-line – release of funds for a closed mortgage. Before e-Notary, a notary had to send a fax to STATER to request disbursement; with e-Notary, a notary could directly control this part of the process. This was a benefit for the notary – more direct control over personal workloads – and for STATER in gaining a much more efficient process, speeding up loan closings, and reducing costs. STATER could also strengthen business associations with brokers, reducing broker relations with other loan servicers and thereby raising competitive barriers. After 12 months, over 50% of the notary payments were handled through e-Notary. And there was a secondary objective to this project. E-Notary was the first public, operational test of the new e-servicing applications and technical infrastructure. This not only made it a test case for the e-servicing program and the IT department, but it allowed the e-servicing team to gain experience and knowledge to apply to follow-on e-servicing projects. From STATER’s business side, however, it was a significant first step. For the first time, an external party in STATER’s mortgage process would actively gain control over their own part of that process. This brought significant opportunities and risks. The opportunities included very favorable response by the notary community, including more notaries signing up for service with STATER. There was also the favorable public relations image of being ‘the first’ with leading edge technologies applied to the everyday loan business process. On the other hand, the risks of allowing external, non-STATER employees direct access to STATER databases filled with private financial data seemed dangerous – but essential to the entire concept of e-servicing. This project helped to ‘test the waters’ of not only the technical infrastructure, but the entire virtual loan process – while limiting the scope of any damage before implementing more eservicing projects.

\- e-Broker: A loan or mortgage broker advised customers about loan options and costs, submitted loan applications, and tracked customer delivery of required documentation. To perform these tasks, a broker needed current information on the customer application status. Before e-Broker, STATER sent brokers a weekly status report on their applications. It was, of course, often out of date the moment it arrived. With e-Broker, this status report information was not only available in detail on the STATER website from any Internet connection worldwide at any time, but was as instantaneously current as the information in STATER’s databases.

Like e-Notary, e-Broker not only helped brokers conduct business more efficiently and possibly give them a competitive edge, but e-Broker made STATER’s loan process more efficient and less costly by eliminating the reports and reducing the number of calls from brokers requesting or questioning information on a customer. And like e-Notary, it helped cement relationships with brokers; the more advantages it gave the brokers, the more dependent they became on e-Broker and STATER.

## Possible Applications

By March 2002, the e-Servicing Steering Committee was considering a number of other possible applications for the next e-servicing projects, including:

\- e-Capstone: pre-qualifying loan applications online without requiring full processing in the SHS.

\- e-Consumer: giving consumers direct access to their application data, loan data, and payment history – and perhaps calculate pre-payment penalties or provide other helpful functionality.

\- e-Advice: integrating e-Application into e-Broker for a seamless process from customer advice through mortgage offer.

## Strategic issues

The most important objective for STATER in 2002 was ‘growth in Europe’ through 2005. The volume of outstanding mortgage loans in the European Union more than doubled in the previous 10 years to over h3.9trillion in 2001 – more than 40% of Europe’s gross domestic product – and STATER wanted to be a major player. STATER intended to focus on countries with large, attractive residential loan markets – namely, Spain, Italy, and France. Within The Netherlands and Belgium, STATER intended to concentrate on improving the efficiency of existing clients and aim for significant (20% per year) growth in Germany. e-Servicing was the key part of its objectives; STATER aimed to furnish all mortgage stakeholders with the right information and services via the Internet.

But how? The profound ‘reach and range’ of the Internet seemed to offer dozens of attractive, viable opportunities where there were few players. The STATER Steering Committee recognized that a complete e-servicing strategy was necessary to help them choose appropriate projects, coordinate organizational business units, guide them through the development process, and anticipate external events – like competitive reaction. The Steering Committee saw many issues, opportunities, and risks.

## Market position

The Steering Committee felt that STATER could be positioned somewhere within three different models:

1. The ‘specialist originator’:<sup>4</sup> STATER would standardize and automate the buyer decision-making process for complex and relatively expensive products, then send transactions to an exchange for execution.

2. A complete service provider: STATER would facilitate an end-to-end mortgage process.

3. Business intelligence provider: STATER had one of the most extensive mortgage databases in the Dutch mortgage industry; they could mine that data and sell market information – although, to date, STATER’s business clients had not allowed STATER to use their data for these purposes.

STATER’s competitive advantage had been based on its operational excellence, operating at a lower cost than the back-offices of lenders. e-Servicing could allow STATER to deliver new, premium services at even lower costs. Although brokers tended to not be willing to pay for services, the Steering Committee believed they would for effective, additional value provided.

Moreover, although the concept of ‘straight-through processing’ with mortgages was first implemented by STATER, it was not invented by STATER – many service organizations and financial institutions were developing the concept with new technologies and web-based architectures. Sustaining competitive market advantage would likely be a constant issue.

The Steering Committee had many questions. What were the potential advantages and risks of each model? Should STATER try to position itself in just one, a combination, or all three? If not all three, which one or ones? If more than one, what priority should STATER assign to them? Which should it try to tackle first – the easy one, the one with the quickest payoff, or the one with the biggest payoff? Which model is the competition most and least able to react to? Which is most likely to pay off in the short run; which in the long run? Which model is the one most likely to allow STATER to defend its present strengths? Which model is the one most likely to spawn new opportunities?

## A portal for the mortgage industry

e-Notary and e-Broker raised the issue of how to position these applications in the market. They were intended to deliver value-added services to the business relations with STATER’s clients through the STATER website. One of the major discussions with their clients was whether or not a broker should be allowed to see the status of all their offers or only the ones through a particular lender. Some lenders did not want brokers to have an overview that included lender competitors; they wanted brokers to access their information through the lender’s website. Other lenders wanted to create the most efficient market and did not insist on access through lender websites.

STATER wanted to create its own mortgage portal; a oneentry point for all mortgage related services available to all mortgage participants. STATER would provide mortgage eservices on this site, but also links to other companies like auction sites. The Steering Committee wondered: would the market accept STATER as the central, driving force behind this concept? Or should STATER try to form alliances with different stakeholders to build the site – based on STATER applications?

## Client obligations

The existing e-servicing applications had created direct relationships with brokers and notaries who were participants in the process, but not employees or legal contractors with STATER. The scope of STATER’s services had increased dramatically as had its responsibility to maintain and properly operate the e-infrastructure. But what rights did these third parties have? Could they launch claims or lawsuits against STATER in case of infrastructure failures or software errors? What if STATER was successfully hacked, causing the loss of confidential financial data – or worse – loan manipulation and fraud? If STATER launched the mortgage portal, to what extent would it be responsible for all the activity that occurred through their website? Could STATER control and manage what it had created?

## Industry standard maker

In the Dutch mortgage market, STATER was the frontrunner and the first to have created an electronic infrastructure for the mortgage process. This appeared to give STATER the market power to impose their standards on this nascent market. But as the ‘service grid’ of linked mortgage players grew – each with their own technology preferences and agendas – the industry would need a leader that had the influence and the capability to create and compel industry standards. Could STATER fulfill this ambitious role? Would STATER want to fulfill this role?

## e-Business model

For e-Application, STATER charged a fee for each application; for e-broker, a fee per inquiry up to a certain limit per broker. The Committee wondered if STATER should charge an ‘admission’ fee and a monthly fee for access to the service. Charging a broker was difficult (they were used to getting everything freely), but charging a notary was possible since STATER made his work process more efficient and less costly.

## The next steering committee meeting

Tom laid out the business strategy issues – as well as the technology issues – and attempted to first plot how he would identify STATER’s alternatives and the criteria for his recommendations to the Steering Committee on an eservices strategy. He also wondered: Who should be involved in this process? Should they focus on a few areas, or attempt an overall, comprehensive strategy? How should the process occur?

As Tom looked out his office window pondering these questions, he could see fields of famous Dutch tulips beginning to bloom in swaths of primary colors. They bloom each year in spite of endangering seas and usually miserable winters, he thought, and yet they are beautiful. Perhaps they are a metaphor for the challenges, opportunities, and our own blooming in the European mortgage servicing market – starting with a good e-servicing business strategy.

## Teaching note

## Synopsis

After 2 years of on-line experiments, Tom van Vianen, CEO, felt certain it was time to fully implement STATER NV’s new ‘e-servicing’ concept with a cohesive strategy. Established in 1997 in The Netherlands and headquartered in Amersfoort, STATER had 27 business clients and serviced over 80 different mortgage portfolios of more than 450,000 mainly residential loans in the Netherlands, Belgium, and Germany. Their mortgage service operations and information systems were considered state-of-the-art in 2002, but they were moving business on-line while simultaneously increasing the types of services provided and expanding operations into Spain, France, and Italy – within the next 5 years. In a land known for taming the forces of the sea, Tom faced what seemed like a sea of ‘euncertainty.’ What exact roles should STATER play in an on-line loan market? How should they position themselves to lead in those roles? The e-Servicing Steering Committee looked to Tom to direct them, and he knew he needed a clear vision for the next Steering Committee meeting in 2 months, in May 2002.

## Intended audience

This case was written with MBA students in mind, but could be effectively used for students in other fields or majors, including Information Systems, Business Strategy, Management, Marketing, and Information Technology – and at all post-secondary school levels (undergraduate, graduate, or executive education).

## Teaching objectives

This case was intended to highlight:

\- e-servicing as a new on-line area of business (as opposed to e-products, or selling products on-line)

\- the opportunities and risks associated with online business

\- the issues surrounding an e-business strategy, and

\- the process of choosing an e-business strategy.

## Teaching discussion

This case introduces a wide range of e-business issues for online services (as opposed to products). While mainly a business and information systems strategy case, it covers almost all e–business issues including virtuality vs bricksand-mortar presence, legal responsibilities and obligations, pricing models, international cultural issues, personnel issues, marketing images, and decision-making processes. This range of issues is not uncommon for companies breaking new ground as STATER did with mortgage eservicing. The issues were even more difficult to navigate, however, because of the speed at which STATER felt it must act to seize market advantage, the speed at which the underlying technology was evolving, the potential size of the market, and how quickly customers were evolving. And perhaps as important as reaching a decision on each issue was simply being able to prioritize the issues in the beginning to help speed up their action.

To be sure, there are far more unanswered issues in this case than there is complete data for deterministically deciding each issue. There certainly is very little quantitative data for ‘doing the numbers.’ Assuming one never has all the information one needs to reach totally objective and calculated conclusions, this case will reflect e-business and information system strategic decision–making under situations that are highly ambiguous yet potentially highly rewarding (or damaging). Students will have to rely on their experience, insight, and instincts to find solutions to the questions the case raises. The challenge to the case discussion teacher will be to focus their attention on a small range of issues that can be adequately covered in the allotted class time.

## Suggested assignment questions

1. What specific roles should STATER play in the on-line loan market?

2. To what extent should STATER operate in the virtual (on-line) world and in the physical (bricks-and-mortar) world?

3. How could STATER stave off e-servicing competitors?

4. Which e-servicing business strategy should STATER pursue first?

5. What process should STATER use in determining their e-servicing business strategy?

## A teaching strategy (80 min class)

1. The mortgage process in the Netherlands, and STATER’s role prior to EUBOS (15 min)

\- Who is STATER? What were their strengths and vulnerabilities? How did their mortgage servicing operations function? Who were their customers?

\- What capabilities did SHS provide?

2. Internet e-servicing opportunities and risks (25 min)

\- What opportunities did EUBOS give them?

\- What risks did EUBOS introduce?

\- Who were their existing and potential competitors? 3. Strategic issues (25 min)

\- What role(s) should STATER play in e-servicing?

\- Which e-servicing business strategy issue should be number one priority, and why?

4. Conclusion and postscript (15 min)

\- What did they learn from the case?

\- Some STATER lessons learned (provided below), the professor’s take-aways, and the case wrap-up.

## Case analysis

The Internet, which has gone beyond the dot-com implosion of the late 1990s, still offers very attractive benefits including wider access to potential buyers and sellers, fast transaction processing, localized multimedia, greatly reduced transaction costs, and location flexibility and scalability. Which is not to say there are not attendant, super-size risks, also. But two key issues face those who would like to reap the rewards of Internet business: how, and to what extent.

STATER was an established, successful mortgage servicing company that – by its own admission – entered the Internet e-servicing world ‘almost by accident.’ STATER had developed the SHS system for automating the entire loan process from origination to servicing to securitizing, containing the all-important Capstone artificial intelligence system for making loan decisions. It was the Bank of Scotland that showed STATER the potential benefits (and risks) of connecting SHS to the Internet. From there, it took little imagination to see a wide range of opportunities for STATER to expand the range and reach of profitable services.

But how? More precisely, which of the many possible approaches should they take, and how should they decide with route(s) to take? An important decision-making step students often overlook is determining decision criteria before choosing among the alternatives. As the old saying goes, ‘Making decisions is easy if you know what’s really important to you.’ Students should recognize that decision criteria vary considerably by situation and intent. The criteria for a physical value chain service should be different than those for an online value chain; when starting a new venture than optimizing an old one; and when seeking market expansion instead of market dominance. In this case, students could consider at least the following decision criteria for STATER:

\- value proposition

\- competition

\- profitability

\- information systems

\- technology opportunities and constraints

\- customers and their knowledge, skills

\- future maneuverability and scalability.

Question 1: ‘What specific roles should STATER play in the online loan market?’ There are so many opportunities, risks, possible criteria, and possible outcomes to this new business venture, that the best answer may simply be ‘the most they can possibly do very well, especially in areas with the greatest potential return.’

Question 2: ‘To what extent should STATER operate in the virtual (online) world and in the physical (bricksand-mortar) world?’ Here the article by Sviokla and Rayport (1995) about virtual value chains can be enlightening. Most importantly, STATER does not have to operate in one or the other; indeed, the optimum is likely to have some portions of STATER’s value chain in the virtual world to take advantage of its strengths, and some parts of STATER’s value chain in the physical world for the same reason. Much of this will revolve around whether the value chain part is a physical object or virtual. Loan approval based on applicant data can be entirely virtual; filing official papers with local officials may be entirely physical.

Question 3: ‘How could STATER stave off e-servicing competitors?’ Students may apply what they already know about competitive strategy: STATER can get out ahead and stay ahead of competitors in what and how they offer their services, they can offer more or better services for the same prices, they can be the low-cost leader, they can maintain a market image of the leader, they can form alliances, and they can forge buy-ins with customers to make the cost of customer switches to competitors appear greater than the benefits.

Question 4: ‘Which e-servicing business strategy should STATER pursue first?’ Their most important objective, as stated in the case, was ‘growth in Europe.’ Of the three market strategies (specialist originator, complete provider, and business intelligence provider), they appear to have little to lose and everything to gain by embracing the complete provider strategy. While stumbles and mistakes are likely, the potential to very quickly spread across Europe (breadth) while simultaneously automating the entire loan process (depth) would seem enormous and too big not to try – especially since the loan process automation part was almost entirely complete and operational. The field seemed wide open for innovation, and it would be easier to back off from the complete provider approach than to move toward it in the face of competition.

Question 5: ‘What process should STATER use in determining their e-servicing business strategy?’ One of the strengths of the teaching case method of learning is that the case evaluating process is more important than the case particulars – that a student is unlikely to be faced with exactly the same situation after class but can use the methodical evaluation process in almost any situation. In this case, the basic method of identifying the opportunities, the alternatives, and the criteria is sound and could be applied to choosing the best strategy. The students should be aware of the relevant issues to consider, however – such as Internet and systems technology, sound business principles and practices, the market and its players, customers and their use of technology, differing mortgage loan regulations and regulators (especially across different countries if not standardized within the European Union), European cultural differences, privacy issues, and competition. The students may well suggest STATER should ‘try, evaluate, make adjustments, and try again.’

## Notes

1 The name was changed in 2002 for commercial reasons to www.bankofscotland.nl.

2 SHS-Connect was the subsystem that processed the electronic applications and performed validity checks. The credit check was performed in the next stage by Capstone.

3 Wednesday, 12 January 2000. Press release, Bank of Scotland. http://www.hbosplc.com/media/pressreleases/articles/bos/2000/ eubos.doc

4 Described in Richard Wise and David Morrison (2000).

## References

Sviokla, J.J. and Rayport, J.F. (1995). Exploiting The Virtual Value Chain, Harvard Business Review November, (Article 95610), 75–85.

Wise, R. and Morrison, D. (2000). Beyond the Exchange: The future of B2B, Harvard Business Review November–December: 86–96.

Appendix A. STATER NV organization  
![](/api/attachments/K695TBG5/fulltext/images/eb357b5c0dff7ee062500f64c2e9d31d4af0aaee5be5fc670fc56926e6ac596b.jpg)

Appendix B. The mortgage process  
![](/api/attachments/K695TBG5/fulltext/images/dc91743927aa6beb6a0cac9b3226fb3cf3e4b27adb0f26b92f59145e10f61105.jpg)  
Appendix C. The SHS architecture

## System: Mortgage processing support

![](/api/attachments/K695TBG5/fulltext/images/49d9a9c30155d3984079fc6b134941200128081041942f637e7bbd9f1ac0058b.jpg)
