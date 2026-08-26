---
otero_id: 21477
otero_key: "TJFA5CGT"
title: "Internet-based EDI strategy"
authors: "Arie Segev; Jaana Porra; Malu Roldan"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00026-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Internet-based EDI strategy

Arie Segev $^{*}$ , Jaana Porra $^{1}$ , Malu Roldan

The Fisher Center for Information Technology and Management, Walter A. Haas School of Business, University of California, Berkeley, USA

## Abstract

The Internet appears to be a cheap, efficient, and ubiquitous channel for transmitting Electronic Data Interchange (EDI) transactions. This paper contrasts two strategies for implementing Internet-EDI systems. McKesson treated its Internet-EDI system as a traditional information systems development project while Bank of America built its Internet-EDI system with a prototyping approach. The paper discusses the conditions in which either approach may be appropriate in terms of project goals, time constraints, environmental uncertainty; and organizational structures employed. It also suggests that emerging Internet-EDI applications could transform trading partners relationships by reducing the import of EDI-capability as a competitive asset. © 1997 Elsevier Science B.V.

Keywords: Electronic data interchange; Internet; Electronic commerce; Interorganizational systems; Systems development

## 1. Electronic commerce and EDI

According to a KPMG survey of 100 United Kingdom companies with revenues of £200 million or over, companies expect £170 billion in sales over the Internet within the next five years [1]. This means that direct sales over the public network would grow from the current 2% or 3% to 17% of total sales. A similar optimism about the growth of electronic commerce is taking place in the United States. This positive outlook is most often attributed to the favorable demographics of computer-savvy

U.S. consumers [2]. But, the current discourse is seldom influenced by those who warn that the current investments in Internet-based commerce by large corporations do not match their growth expectations [1]. More importantly, the current electronic commerce projections do not clearly distinguish between expectations for business-to-business and business-to-consumer segments of the market. The emerging Internet retail systems are based on an individual with a web browser making a single purchase. But business-to-business transactions have traditionally involved sophisticated mainframe and EDI-based systems designed for batch processing of large transaction volumes. It is this business-to-business marketplace that is often omitted or misunderstood in the myriad discussions about the future of the electronic revolution.

Traditionally, EDI is a synonym for standardized inter-organizational data exchange [3]. It has been used for more than 20 years in automating the interchange of business transactions between large corporations and their trading partners—suppliers and customers—to create a paperless flow of administrative, pre-purchasing, purchasing, shipping, receiving, warehouse, customs, billing and payment information [4]. Despite its long tenure and potential benefits, EDI adoption has been slow. Forrester Research estimates that today only 5%—120,000 out of 2 million—of the companies that could be using EDI are actually doing so [5].

One of the most often cited reasons for limiting the adoption of EDI is the prohibitive cost of its implementation. Traditionally, these EDI implementation costs have included the cost of purchasing or developing the EDI translator, the cost of integrating the EDI translator with the corporate information system, and the cost of establishing a communications network among trading partners. These costs along with the major effort and expense involved in making disparate corporate systems communicate seamlessly within EDI standards, means that the spread of EDI has largely been fueled by pressure and/or subsidies from large manufacturers to their suppliers $[6–9]$ . Value Added Network providers play an essential role in providing expertise for translating, tracking and conveying EDI transactions among trading partners $[10–12]$ . Still, Forrester Research estimates that this situation excludes up to 60% of the vendor marketplace, or 1.9 million companies from current EDI networks $[13]$ . A large part of the interest in using the Internet as a channel for EDI transactions is the potential for facilitating the entry of more suppliers in such networks—both by lowering set-up costs and by being a readily available network providing ubiquitous access $[14]$ . This paper presents an assessment of the impact that the Internet might have on the growth of EDI networks, based on the results of two efforts at the early application of the technology and a preview of upcoming applications.

## 2. Evolving potential: internet-based EDI

The Internet seems to present a cost-effective transmission medium for EDI transactions [15-23]. However, the decision to move EDI to the Internet is not a forgone conclusion. Contrary to initial notions, the Internet is not always the cheaper alternative for three reasons. First, to maintain their customer base, current transport medium carriers—e.g. value added networks (VANs)—are lowering their rates to stay competitive as an increasing number of firms consider moving their EDI transactions to the Internet. Moreover, since many VANs are now offering Internet-based services, organizations need not switch to an Internet Service Provider (ISP) to obtain Internet access or capability $[15,24,10,18,25–27,12,28]$ . Second, the cross-platform, user-friendly nature of web technologies is fueling the growth of computer-based inter-organizational services at many corporations. As EDI-aware corporations are beginning to realize, the web paradigm facilitates inter-organizational transactions that need not be based on EDI standards. For example, firms specialized in the transportation of goods and information—e.g., Federal Express (FEDEX)—offer full service logistics support without using EDI forms and standards for communications and tracking among trading partners $[29]$ . Third, concerns over the security and reliability of public networks like the Internet means that porting EDI to the Internet requires additional procedures to insure the security and reliability of EDI transactions $[16,17,30,18,21,31,5]$ . Any savings on the transport medium could easily be cancelled out by the investment in developing and implementing such procedures and the risks and costs of a large security violation or reduced service quality due to delay or the loss of EDI forms sent over the Internet. For companies with high levels of security requirements (e.g. banks, research laboratories and agencies of the US government), using the Internet as an EDI transaction carrier is a complex strategic decision, given existing security solutions and infrastructure.

As with most information systems projects, companies have had two traditional development options for achieving this Internet enhancement—make it or buy it. For either option, development entails more than just building the capability to send secured EDI transaction information over the Internet. Any company building an Internet-EDI capability from the ground up faces the more formidable task of building the translators that allow information to flow seamlessly between transmission and security systems, and the back-end systems that ultimately process EDI instructions.

MAKE IT: Companies can build certification and security capabilities by customizing secure public domain secure e-mail software (e.g., PGP, PEM/MIME, S/MIME, PEM/MOSS), readily and inexpensively available via traditional software distribution channels and on the Internet. This option also allows companies to leverage any existing investments in Internet connections and e-mail by using the same infrastructure for EDI transactions [32].

BUY IT: Many expect that the Internet and the WWW will increase the number of inexpensive EDI service and software packages. As large EDI based service providers hope, this event could not only solve many uncertainties but could also dramatically increase their customer base. Thus, many of the major VANs and software providers in the current EDI market have moved aggressively to provide these packages $[16–18,26,12,5]$ .

Currently, the most complete secure Internet-EDI solution available for purchase is Premenos' Templar $[33]$ . However, until the announced inter-operable version is available, using this product is a partial and expensive solution, particularly because it requires that all trading partners run Templar software $[18]$ . On the horizon are browser-based software products like those being developed by Actra Business Systems, a joint venture between Netscape and GE Information Systems. Aside from simplifying EDI transactions into forms-based interfaces, the software specifications also include tools for easing the integration of user inputs with back-end corporate systems $[34]$ . By lowering all the costs involved in building EDI capability, the combination of browser-based products, integration tools and the Internet, could fuel the mass adoption of Internet-EDI applications $[5]$ .

The intense development of software and services by major EDI suppliers augers a time when the tools for building Internet-EDI capability become commodities—increasing the appropriateness of the 'buy' strategy [35]. Nevertheless, much can be learned from the implementation experiences of early adopters of Internet-EDI capabilities. This paper reports on the efforts of two such organizations. It compares two different approaches to implementation to identify the parameters of strategies for building Internet-EDI capability. We address the implications of the two approaches for Internet-EDI imple mentation and how these approaches may affect the formation of EDI trading partners networks. Specifically, in this paper, we seek to answer two questions:

1. What are approaches for building an Internet-EDI capability, and what conditions make each approach appropriate?

2. What kind of an Internet-EDI configuration facilitates the growth in the number of EDI trading partners in a given network?

In order to answer these questions, the two approaches to developing an Internet-EDI capability are illustrated using two case studies. The first case describes McKesson's quick development of an Internet-EDI application to meet the requirements of a major contract. The second case describes Bank of America's (BofA's) incremental approach to building its EDI capability (for full reports, cf., [22,32,36]). Contrasting the two cases in terms of mode of experimentation, mode of collaboration, skill requirements and cost offers insight on the appropriate application of each approach.

## 3. Two approaches for building Internet-EDI capability

The cases of BofA and McKesson were selected from a wider set of current Fisher Center for Information Technology and Management cases. To ensure comparability of answers for the two case studies, a fixed list of semi-structured questions was used for interviews with executives, managers, and project team members at each organization. Additionally, support material, in the form of project reports, articles and other material provided by the organizations was used to profile the cases. It is suggested that the two cases demonstrate two contrasting—but equally appropriate—approaches to implementing an Internet strategy.

## 3.1. McKesson's traditional information systems design approach

## 3.1.1. McKesson and EDI

With 13 billion in revenues, McKesson is the leading wholesaler in the pharmaceutical industry. Maintaining this leadership in an industry where average net profits hover around 2%, requires constant innovation. McKesson has achieved continued leadership by growing its generic drug inventories, providing value added services and improving the efficiency of its own operations [37]. Key acquisitions and its own internal development have made Mckesson a leader in the provision of value added services to many segments of the health care industry. Many of these services involve the application of information technology to rationalize and improve the efficiency of distributing pharmaceuticals and of managed care compliance. Its proprietary Economost product—ordering system, originally developed in the 1970s, today supports 6600 trading partners [38]. It has recently developed a suite of financial and managed care applications to complement the backend services it provides to a group of individual retail pharmacies that McKesson helps operate as a virtual pharmacy chain.

## 3.1.2. Background and objectives

Recently, the Internet-EDI involvement of the company was hastened by efforts to win a major contract that included requirements for Internet-based access to McKesson's product inventory and ordering systems. The specific requirements of the contract were direct FTP access into McKesson's systems for price checks and product availability, two-hour quantity and pricing confirmation on orders, and emergency ordering capabilities. Additionally, McKesson needed to build this functionality within 90 days in order to win the contract. Because of the security risks associated with providing such access, McKesson negotiated to meet the contract requirements using two systems: a browser-based system for emergency inventory checking and ordering of single items, and an Internet-EDI system for routine ordering, invoicing and other transactions [38].

In addition to meeting the requirements of the customer contract, any solution chosen by McKesson had to meet the high access and security standards of the company. Due to its long history with mainframe-based computing, McKesson's managers were accustomed to the operation of critical systems on a 24-hour-per-day, seven-days-a-week basis. The mainframe era security standards and the critical nature of the data stored and processed by McKesson's systems dictated rigorous security measures for the proposed system.

## 3.1.3. Implementation

To respond to these requirements, McKesson established two systems: a browser-based system for emergency orders and an Internet-EDI system for routine orders and related transactions. To build the two systems, McKesson built a multi-disciplinary team, headed by the Vice President for Information Delivery. The team was composed of two project managers, programmers from the EDI area, five architects from the applications area, a web developer, network engineers, UNIX engineers, and customer integration staff. The new system had to be integrated with legacy systems in the order processing, distribution, receiving and accounting areas. The team had to knock down many organizational obstacles to meet its aggressive deadline and its additional goal of enhancing existing applications in the process $[38]$ . The magnitude of the contract associated with this development effort supported a strong case for obtaining resources and convincing various organization members to break from traditional organizational practices. The size of the contract was also instrumental in justifying the half million spent in building the infrastructure and developing the software necessary to meet the customer requirements and McKesson's own high standards of security and availability. To meet these standards, McKesson purchased redundant web servers and built a double firewall.

The browser-based system for emergency ordering was built using HTML and PERL on the Netscape platform. The use of these tools greatly reduced the development time for the emergency ordering application. The system is in effect an Extranet that allows password-enabled access into McKesson's inventory and ordering systems. Authorized representatives of the customer can access the Extranet using a web browser. The system allows authorized users to check on inventory levels and order individual products.

McKesson contracted with EDS to build its Internet-EDI system. The company purchased Premenos' Templar software for both its own system and a hub at its customer's facility that could be used to support 18 ordering sites. At the time, Templar was the only product that provided complete, secure Internet-EDI capability using the Simple Mail Transfer Protocol (SMTP) messaging standard [38]. Despite being limited to one package, McKesson could be reassured by successful applications and testing of the Templar product [39]. This software package interfaced with the company's existing EDI software and added software level security and authentication procedures, including the encryption and signing of any EDI documents that were sent over the Internet. The package includes key management capabilities that would be especially useful as McKesson increases the number of trading partners it conducts EDI with over the Internet.

## 3.1.4. Results

Benefiting from the use of a full featured Internet-EDI application, the expertise of EDS and the motivation of a large government contract, McKesson was able to complete development of its Internet-EDI capability in only 90 days. Key to achieving this quick turnaround was the willingness of McKesson management to invest heavily in hardware, software and information systems development consulting in order to quickly develop the infrastructure for a highly-secure and highly-available system tailored to a single customer.

McKesson chose the information systems development life cycle model approach to solve the problem. Of the two traditional options (make or buy), McKesson chose to buy as much of the system as possible. This strategy emphasized producing a finished system as quickly as possible. This meant that a robust production level system must fulfill their customer's specific requirements with precision. While McKesson's approach achieved the delivery and functionality goals, it represents an expensive option that may not be feasible in all organizational settings. Furthermore, the decision to build its solution around a single product (Premenos's Templar) limits McKesson's ability to expand the network of trading partners on the Internet. Though a complete solution, the system requires Templar to operate on the machines of both trading partners. Since Templar is relatively expensive, trading partners have to make a considerable initial investment in order to become part of McKesson's Internet-EDI network. As a result, almost six months after the system was finished, McKesson was still conducting EDI with only one trading partner. By utilizing the traditional information systems design approach for Internet-EDI,

McKesson may have limited its ability to exploit the Internet's potential for a wide range of trading partners. Thus, the high cost of tailoring of the system for one customer may reduce the flexibility needed to achieve the full benefits of the Internet's customer base. Ironically, a software package that was inherently designed to handle a large network of trading partners, ends up limiting the size of this network because of the high cost of expanding it.

## 3.2. Bank of America's proof of concept approach

## 3.2.1. Bank of America and FEDI

As one of the largest banking companies, with assets of more than US\$227 billion, BofA offers diversified global financial services to individuals, businesses, government agencies, and other financial institutions in the United States and in 36 other countries [22]. With its large corporate customers, BofA has used Financial EDI (FEDI) based systems for years. FEDI refers to the processing of a payment from payer to payee through electronic channels using standard EDI formats. The bank's approach has always been customer driven. In terms of FEDI based applications, this has meant accommodating multiple access methods and two different transport mechanisms: value added network (VAN) providers; and private lines. Because the initial investment in EDI systems and their operating costs when using either VANs or private lines have traditionally been high, BofA's EDI customer base is limited to corporations with continuous and significant transaction volumes.

By widening the customer base to smaller businesses and firms with temporary and small volume FEDI transaction needs, BofA could utilize its existing EDI applications more efficiently and serve all of its customer segments more effectively. With this goal in mind, in 1994 BofA began to examine strategies which would: (1) consider the Internet as an alternative transport medium to VANs and private networks; and (2) consider the vast marketplace of the Internet and WWW for its EDI market potential.

## 3.2.2. Background and objectives

The BofA Internet based FEDI pilot project started as a ‘grass-roots joint venture’. At an annual CommerceNet meeting in 1994, the bank’s representatives teamed up with its customer (the Lawrence Livermore National Laboratories or LLNL) to answer a mutually interesting question: Could critical business transactions be transmitted over the Internet in a secure, reliable and fast manner? If the answer to the conceptual level question was in the affirmative, the two organizations could both expand the solution to new business applications and to other relationships. While the bank's interest was to widen both its FEDI based services and its customer base, LLNL wanted to use Internet-based EDI with its suppliers as well as internally for purposes such as travel reimbursements for its employees.

The bank garnered support for its strategy by anticipating the inexpensive Internet-EDI software packages. The project group believed, WWW-based packages had the potential to expand BofA's EDI-based market place. If the WWW-software package approach was valid, then small enterprises and businesses with temporary and small volume EDI needs could inexpensively access the array of BofA's EDI-based business services on demand. For LLNL, Internet-based EDI had potential to support the organization's efforts in cost containment through reengineering people- and paper-intense processes.

The BofA–LLNL project team chose a prototyping approach to developing the information system. The rationale behind the approach was that in order to gain management acceptance, it was necessary to first address some common negative perceptions about the feasibility of the Internet as a critical business transaction carrier before implementing production applications. In the project team's opinion, the best way to prove the solution was to conduct an experiment under real circumstances. Exchanging actual business data over the Internet between BofA and LLNL for a period of 12 months should provide adequate support for pursuing Internet-based EDI.

## 3.2.3. Implementation

During the following six months, the project group researched several available Internet-based security products. A satisfactory solution was designed around Privacy Enhanced Mail (PEM) and the multipurpose Internet mail extension (MIME). The project team implemented an inter-organizational FEDI system with the Internet as the transport mechanism. In this pilot system, payment instructions and remittance information flowed from BofA's mainframe-based EDI system via the corporate network to an e-mail gateway and a firewall, then over the Internet to LLNL's comparable system and back again.

The project consisted of two phases. The purpose of the first phase was to gain confidence with the initial implementation by exchanging a small volume of transactions of US\$10,000 or less per supplier per day between BofA and LLNL. The purpose of the second phase was volume testing using actual transactions and dummy files of up to 1000 transactions amounting to not more than US\$100,000 per vendor per day. During both phases, the security, reliability and speed of the system was monitored by automated e-mail-based control procedures and a rigorous, human monitoring system implemented by both organizations. Each transaction was monitored by groups of individuals assigned from all participating units and levels of organizations. In addition to e-mail, a system of telephones, faxes, and beepers was used to complement the e-mail-based FEDI system. Recurring problems were resolved in weekly meetings which sometimes consisted of more than twenty people from the two organizations. The project organization was aided by the existing security units of both organizations who conducted their own tests on the system and made recommendations for improvements. Finally, the firewall team of BofA conducted their own routine tests of the firewall.

## 3.2.4. Results

The results of the pilot project where encouraging. During the 12 months of the two phase pilot project, no security violations were encountered. Throughout the project, the speed and reliability of the system remained high. No transactions were lost and no transaction took more than two days from its initiation to completion at the supplier's bank. Moreover, delays were mainly caused by coordination problems between the two organizations and by the EDI applications—not by the Internet. Summarizing the problems which were encountered during the project:

\- 49% of the problems stemmed from systems being down or off-line

• 24% were transaction delivery problems

\- 17% were application/operating system incompatibilities

• 5% were message delivery problems

• 5% were decryption problems.

The error rate per month averaged 24% and did not exceed 50% during the test period. The total number of problems each month did not exceed 22. More importantly, the error rate showed a decreasing trend over time. Thus, the organizations learned quickly about the adequacy of both Internet transport and the Internet-based security packages for EDI.

Instead of adopting the information systems life cycle model, BofA approached the Internet-EDI system as an evolutionary prototyping process aimed at no particular immediate end product. The prototype was successful. It demonstrated that it was possible to transmit critical business transactions over the Internet with security, reliability and speed. Today, both parties are comfortable exchanging FEDI data using the Internet. This means that this inexpensive technical implementation of the pilot project has served its purpose as a proof-of-concept. The success of the pilot resulted in the purchase of the hardware to build a production-level system that is now fully operational. BofA has gained Internet-EDI partners since the pilot project. The prototype system also helped in identifying the open issues for the future production system. Some of the open issues include scalability of the system from both the technical and the security management viewpoints. In particular, the pilot project systems did not include the capability to handle public key management given a growing customer base and did not have a system for generating documents that automatically acknowledge receipt of an EDI transmission. While products such as Templar provide limited solutions to these issues, full resolution cannot be achieved without the establishment of a public key infrastructure and legally binding protocols for EDI receipts.

## 4. Analysis: contrasting the Mckesson and BofA-LLNL approaches

The McKesson and BofA cases differ fundamentally in their approach to information systems development. McKesson viewed the Internet-EDI system as an end product, a production level system. This end product is an outcome of a technical task analysis and an information systems design process patterned after the traditional information systems life cycle model. BofA approached its Internet-EDI system as an open ended organization-level learning process which was not (possibly ever) to produce an end product but a sequence of temporary software and hardware configurations to solve current business needs. We suggest that the two cases show that the meaningful difference between the two implementation strategies is not in whether the system is bought or made. Rather, the different outcomes of the two cases is a result of two different ways of applying technology. In this section, we contrast the two approaches in terms of mode of experimentation, mode of collaboration, skills issues and cost issues.

## 4.1. Mode of experimentation

Because of the time constraints in their contract, choosing an experimental Internet-EDI strategy was not possible for McKesson. To avoid spending time to learn the technology, the company purchased the technical expertise and a turn-key system. Based on the McKesson case, it can be demonstrated that the state-of-the-art in Internet EDI is mature enough so that it can be acquired on short notice. However, it is rare enough to be expensive in today's marketplace. In McKesson's case, the Internet-based EDI system was considered a traditional outsourced information systems design project. Whether the system had been developed with internal or external expertise, the degree of specificity in the contract requirements, the high standards of reliability and security required, and time constraints made the costs unavoidable.

BofA had no time-critical reasons for a rapid Internet-EDI implementation. From the beginning, BofA's purpose was to test Internet-EDI security solutions to gain confidence in the technology. During the pilot project, no permanent FEDI/Internet solutions were intended or implemented between the bank and LLNL or between the bank and any other customer. Although the technical implementation was functional, it was never considered as the final version of the system. A list of potential problems and improvement propositions were carefully recorded during the pilot project in order to benefit any future production version. Moreover, rather than spending time and money on making the pilot system robust, the project group continued to evaluate other options (such as Templar from Premenos) during the project. The consensus of the team was that, at this early stage, no Internet-FEDI implementation can be considered permanent. As the products for Internet security continue to evolve, the systems will change.

The project group's Internet-EDI system development method is a natural outgrowth of BofA's policy of offering a variety of system options for diverse customer needs and technical circumstances. The project did not consider the Internet-FEDI system as a large scale development project requiring advanced technical expertise and established information systems design methodologies. Instead, implementing the system translated into integrating existing and new software and hardware into an inter-organizational assembly line for marketable business applications. In this modular system, each technical component temporarily fulfills its purpose and may be replaced with more contemporary solutions as they become available. The resulting Internet-EDI system is a collection of existing and new corporate software and hardware for integration. This approach limited investments in new information technology. For example, should Internet-based FEDI turn out to be premature, the borrowed modules and people could be returned to their original uses in the line organization. It also ensured that before the final investments are made in production systems, Internet-based EDI makes business sense.

From the organizational perspective, BofA's conceptual level information systems prototyping approach is a part of a larger process called 'punctuated prototyping'—prototyping organizational units with the intention of replacing them with newer structures when the environment changes [40–42]. The approach assumes that there will be periods of stasis (where the environment is constant) and punctuations (where there are radical shifts in the environment) [43,44]. Instead of forming a permanent organizational unit with permanent personnel (or permanent information systems), BofA loaned employees from existing functional units to participate in the virtual business unit for the duration of the project. Thus, the pilot project was a 'company inside a company'—without formal changes in the line organization or its processes. Punctuated prototyping protected both the parent organization and those participating in the project. If the virtual enterprise turns out to be unsatisfactory, it can be modified by changing the composition of its participants or its technical systems to respond to environmental change. In the event of catastrophes, it can be terminated and the people returned to their normal positions without the cost of reorganizing.

It is likely that as the Internet-EDI infrastructure matures and cheaper software becomes more readily available, Internet-EDI capability will be a commodity which can be acquired on demand. In effect, companies planning to enter the Internet-EDI arena in 1997 are mid-cycle adopters. Thus, they will be able to benefit from the experimentation done by early adopters like BofA, LLNL, McKesson, and its major customer.

## 4.2. Mode of collaboration

Because of their significant time constraints, McKesson's Internet-EDI team had to quickly identify and bring together experts from outside and inside the firm. In selecting outside collaborators the company was encouraged to work with EDS by their target customer. McKesson's development options were narrowed by the goal of the project to provide a final, production-grade solution in a short time frame. They chose to use Premenos as the software vendor simply because no other applicable Internet EDI packages were available at the time. The time constraint also prevented any attempt to customize other software solutions. The importance of the project helped the McKesson team gain the support of managers who controlled key resources and internal experts needed for the project. These included individuals with expertise in UNIX, hardware and networking, as well as the corporate databases and information systems. The collaboration in the McKesson Internet-EDI project was motivated by necessity and driven by technical expertise.

Free from imposed performance pressure, BofA and LLNL started the FEDI/Internet pilot project as peers. Both parties were equally interested in adopting the Internet—but for different reasons. BofA would get the opportunity to expand its FEDI customer base and LLNL could streamline its own operations. In both organizations, the project champions were the business and information systems professionals—not the management. In both cases, management was supportive of the experiment but not ready to commit completely to the Internet strategy. All units had a role to fill in the project. It was not lead by the technical experts or by the business managers. Rather, all parties joined the project to learn about the Internet novelty and to contribute their applicable expertise to the project.

As a result, the atmosphere of the pilot project was entrepreneurial. Commitment to the success of the project was personal at all levels of project in both organizations. The participants volunteered their time because they had personal stakes in the project success. Likewise their enthusiasm and commitment was predicated on building a successful solution. The termination of the pilot project was emotional for all the parties. The central participants on both sides believed their work would make a meaningful difference in the way their organization does business.

## 4.3. Skills issues

Since at McKesson, the Internet-EDI systems design skills were purchased from outside vendors—e.g. EDS and Premenos—the primary future issue for McKesson was to find the expertise to maintain the Internet-EDI production system after it was finished. Since the company relied on external experts to build their Internet-EDI capability, the task was to identify individuals from within the company who would possess the needed skills. Facing this expertise problem, the project group automated as many of the key processes as possible. Additionally, internal consultants were paired with external experts during the development of the system. As the system was being built, the internal consultant learned about the software being developed and the basic technical skills needed to maintain and enhance the final system.

At BofA, the Internet was familiar to the pilot project participants with technical backgrounds, but it was a novelty for those less familiar with computer technology. Among the non-technical project participants, questions of security and reliability of the Internet were real: What if we lose transactions completely? Who guarantees an acceptable time frame for a transmission? While the business units and marketing groups learned about public networks in the course of the project, the technical staff learned about the existing and potential customers and their business needs. For BofA, the project served as an unusual organizational learning experience. It crossed functional lines, organizational levels, professional and educational backgrounds. The technical novelty of the Internet served as a uniting force.

## 4.4. Cost issues

In order to quickly implement their Internet EDI system which met both McKesson's and its customer's requirements, McKesson invested half a million dollars. This investment covered the purchase of the Templar software as well as the development of the interfaces with the corporate information system. It also included hardware and network purchases. Two servers were acquired to run the Templar system and software allowing one server to act as a backup. Additionally, the company built a double firewall to protect the corporate information system from intruders via EDI channels. Lastly, the investment covered the consulting fees for EDS.

Since the champions of the Internet/FEDI pilot project of BofA and LLNL used existing resources of the participating organizations, on BofA's side, investments in equipment and software totaled less than US\$80,000 and consisted of an existing Sun work station and some operating systems software. At LLNL, the project team used existing hardware and software exclusively. Most technical work on both sides, consisted primarily of integrating existing EDI systems with the systems required to secure EDI transmissions being sent out over the Internet. Additional work was done to build systems to track the progress of transactions between the two organizations. The work was done by the organization's experts as part of their organization duties.

Because Internet-based FEDI was a novelty for both BofA and LLNL, the premise in forming a project team was to include all necessary expertise in the two organizations to effectively tackle any technical or operational question inside the project group without relying on outside consultants. Since the expertise of the related business areas and technology was distributed and no unit was an expert on secure EDI transactions over the Internet or their business applications, the project group grew large. At BofA, the project organization consisted of representatives from Global Payment Services business unit, project management, telecommunications, information systems support, security, and marketing. Moreover, during the project, a new business unit called Interactive Banking was formed. Because the purpose of this unit was to design and market Internet-based banking services, its representatives were also included on the project team. At LLNL, the project group consisted of representatives from the Electronic Commerce Applications and Finance departments. However, no human resources were assigned to the project full time. The participants provided their time to the project in addition to their normal organization duties.

## 5. Discussion

5.1. Assessing the conditions leading to contrasting systems development methods and their implications for building an EDI network

## 5.1.1. Contextualizing development approaches

This paper has presented two successful Internet-EDI implementation strategies. Clearly, differences in the system development methods chosen for the solutions can be attributed to differences in: (1) the project goals; (2) development time constraints; (3) environmental uncertainty; and (4) the organizational structures employed.

With respect to project goals, McKesson and BofA had different motives for building their Internet-EDI capabilities. McKesson's project goal was based on the objective of being the successful bidder on a large contract. In contrast, BofA and its customer were interested in Internet-based EDI in a more general sense. The BofA project had no specific Internet-EDI business applications to build or customers to satisfy. Moreover, in the BofA case, the management was not pressuring the participants nor were they completely committed to the project. Rather the employees themselves decided that it would be beneficial to learn more about the technology to prepare for the uncertain future of the Internet-EDI market place. Additionally, the differences in goals can be seen in the degree of rigor in the customer requirements. While LLNL was open to an experimental system with some expectation of security flaws, McKesson's customer demanded high security from the outset. One interpretation of the two cases is that providing high-level security under actual circumstances can only be justified by implementations such as that provided by McKesson.

With respect to completion objectives, McKesson operated under the considerable time constraints of a pending contract. Conversely, having no fixed target, BofA had the opportunity to spend time learning about the technology in a leisurely fashion. But waiting until a potential customer is interested in novel technologies may turn out to be too-little-to-olate for comprehensive Internet-based business strategy.

The circumstances of the cases differed in terms of perceived certainty of the environment. While McKesson approached its Internet-EDI project under certainty, trusting that they could win the contract, BofA's pilot project considered its environment to be uncertain. For BofA the outcome depended on the near term technological developments and the forecast for the Internet-EDI business services to be offered by the bank. These outcomes could vary from non-existent Internet markets to explosive customer growth. Since there were no current customer relationships directly dependent on the bank's near term implementations, BofA's experimental strategy was acceptable.

For the first three issues, the reasons for the different paths chosen by McKesson and BofA are relatively apparent. But in their chosen organizational forms, the two cases were significantly different. This may be attributable to the three differences in goals, time constraints and uncertainty. However, organizational form in and of itself may be the central lesson provided by the Internet and its revolution in technology and users and its potential for collaboration.

For the greater part of the computer industry's history, most systems have followed the traditional life cycle development methodology just as McKesson did for its EDI application. These solutions tended to be rigid and expensive and have a limited productive life. Yet at the edges of the industry, proponents of open systems touted the coming revolution of full inter-operability and inter-connectivity. These promises of open systems architectures have failed to materialize in the past 25 years of open systems discussions. Though open standards do exist, most of them are still product based and proprietary and do not fulfill the original objectives of the open systems movement. The Internet, however, appears to provide all of the promised interoperability without utilizing the slow standardization bodies and cumbersome standards documents. At its very core, imprinted upon its birth, the Internet has an emphasis on cross-platform applications and interoperability that now flavors most development efforts.

How then can organizations begin to respond to Internet-based activities when technologies are evolving quickly and markets are in a state of constant flux? The answer lies in the use of entrepreneurial organizations which are able to assemble solutions quickly to respond to rapid changes in the marketplace. Such organizational forms are like the BofA approach where resources are gathered with the intention of building prototypes and then reorganized to effect production level implementations. This building-for-change is the central premise of punctuated prototyping. Solutions can be expected to be temporary and flexible so that they can enjoy a limited period of operation (stasis) before the dynamics of the market change them (punctuation). While McKesson approached the Internet-EDI projects from the technical requirements standpoint, the priority for BofA was to involve the business units which would be in the position to decide the immediate applicability of the technology in their business areas. Thus, the technical solution was not driven by direct customer requirements but by the entrepreneurial visions of the BofA business units. The result for BofA was not just another system designed by user specification—but a new organizational unit designed to anticipate the inevitable changes in the marketplace.

We suggest that the Internet and the WWW-based technologies are changing the way large corporations can develop their information systems. The traditional life cycle methodologies driven by the technical aspects of the system will undoubtedly continue to prevail in cases such as McKesson's where the goal was to produce a specific system for a specific long term customer relationship. But BofA's approach of prototyping for change may be more appropriate in the new Internet marketplace characterized by large customer bases, rapidly changing technologies and entrepreneurial opportunity.

Successful prototype projects will eventually cause an organizational change (comparable to the creation of BofA's Interactive Banking unit) or develop into a spin-off corporation. This development emphasizes that the rapid prototyping of computer supported concepts is an area of corporate computing which deserves attention. While the current development paradigms are based on a product analogy (such as the McKesson case), the more modern approaches (such as the BofA case) are likely to emphasize intra- and inter-organizational collaboration and cooperation between organizational units, levels and professional backgrounds to rapidly learn and assimilate new technology applications.

## 5.1.2. Implications for trading partner networks

Ultimately, the goal of any EDI effort is to expand the network of trading partners transacting business using its standards. The BofA–LLNL approach, based on an inexpensive, published standard (PEM/MIME) resulted in faster growth of its EDI network. Costs of entry into the BofA–FEDI network were very low, particularly since new trading partners could benefit from the standards, code, and procedural refinements resulting from the BofA–LLNL pilot. The McKesson approach, on the other hand, resulted in little growth in its Internet-EDI network. Arguably, growth of the network was not a primary aim of the McKesson implementation. Yet, an organization using the McKesson approach would have to be cognizant of the high cost of entry into its Internet-EDI network.

As often pointed out in this paper, Internet-EDI applications are rapidly evolving. In the coming months new products are expected to greatly reduce the cost of entry into EDI networks. An emphasis on interoperability and facilitation of set-up using browser-based applications could result in a situation where even small companies and occasional EDI users can quickly and inexpensively acquire the capability to handle EDI transactions. At that point, being EDI-capable would cease to be a competitive advantage for suppliers. Buyers need not be locked in to suppliers solely because they are EDI-capable and suppliers who are not EDI-capable need not be locked out of a trading networks. Such a scenario portends a transformation of the competitive landscape within such networks. Buyers can place less emphasis on pressuring suppliers to build up EDI-capabilities and more on other aspects of buyer-supplier relationships—cost, trust, product quality, co-development. Ideally, this could result in improvements in product quality, as organizations are no longer limited to EDI-capable firms in their search for suppliers. Ultimately, the winners may be the EDI infrastructure providers, as widespread adoption translates into major increases in EDI transactions. Albeit, the potential windfall for EDI providers is somewhat mediated by the potential competition from non-EDI based inter-organizational systems solutions—e.g., logistics services provided by FEDEX, Extranets.

## 6. Conclusion

This paper has illustrated two approaches to building an Internet-EDI capability. The approaches reflect the contrasting conditions in which they were applied—BofA/LLNL started developing their pilot in mid-1994 during the early days of Internet-EDI evolution while McKesson started its implementation in early 1996. When BofA started its pilot, the design of Internet-EDI systems was still being worked out, indeed, Premenos' Templar was still being tested and, with co-sponsorship of CommerceNet, the BofA–LLNL pilot was seen as part of the effort of refining Internet-EDI specifications. When McKesson attempted its own implementation, the technology had matured to a point where production grade systems could be purchased, albeit at an imposing price that limited the size of the trading network that could be built. At this juncture, the state of Internet-EDI technology suggests that McKesson's quandary is a temporary one and that soon the cost of ramping up to EDI capability may be low enough to promote its widespread adoption.

We suggest that McKesson's approach may be suitable for stable, long term EDI relationships under relatively predictable, yet high risk circumstances while BofA's approach potentially helps to cope with uncertain, unpredictable or temporary relationships and/or unpredictable market conditions. The BofA-LLNL teams benefited from extraordinary conditions that shielded them from constant oversight, and allowed them to experiment with the new technology for almost 2 years. Paramount among these conditions were the uncertainty over the ultimate application of a newly and enthusiastically appropriated technology (the Internet), the presence of well-recognized EDI and Security experts at both organizations, and the relatively low cost of the entire experiment (US\$80,000). In essence, the pilot, was sustained in a pocket of ambiguity and slack resources [45]—similar to many organization's initial forays into Internet application. The proliferation of experimentation by commercial firms on the Internet underscores the tenet that while circumstances exist in which accurate, detailed information systems requirements are essential for a successful information system—the opposite is also true. In some cases, conceptual level information systems design such as BofA's is not only necessary but appropriate.

## References

[1] Management Accounting-London L170bn, Sales expected to come via the Internet in five years, Management Accounting-London 74, No. 10, Nov. 1996.

[2] D.L. Hoffman, W.D. Kalsbeek, T.P. Novak, Internet and web use in the U.S., Commun. ACM 39 (12) (1996).

[3] R. Kalakota, A.B. Whinston, Frontiers of Electronic Commerce, Addison-Wesley Publishing, New York, 1996.

[4] P.K. Sokol, From EDI to Electronic Commerce: A Business Initiative, McGraw-Hill, New York, 1995.

[5] J. Smith Bers, Diving into Internet EDI, Bank Syst. Technol. 33 (3) (1996).

[6] C. Iacovou, I. Benbasat, A. Dexter, Electronic data interchange and small organizations: adoption and impact of technology, Manage. Info. Syst. Q. 19 (4) (1995).

[7] T. Mukhopadhyay, S. Kekre, S. Kalathur, Business value of information technology: a study of electronic data interchange, Manage. Info. Syst. Q. 19 (2) (1995).

[8] G. Premkumar, K. Ramamurthy, The role of interorganizational and organizational factors on the decision mode for adoption of interorganizational systems, Decision Sci. 26 (3) (1995).

[9] E. Wang, A. Seidmann, Electronic data interchange: competitive externalities and strategic implementation policies, Manage. Sci. 41 (3) (1995).

[10] B. Fox, Internet: bane or boom for EDI VANs, Chain Store Age 72 (6) (1996).

[11] Hitchcock Publishing, Is the Internet a better way?, Manufacturing Systems: Master the Supply-Chain Challenge, Supplement, 1995.

[12] J. Ross, Retailers explore EDI on the Internet, Stores 78 (7) (1996).

[13] Hitchcock Publishing, Internet breaks price barriers for small and mid-size companies, Manufacturing Systems, 14 (8) 1996.

[14] J. Gebauer, Internet-Based EDI, Fisher Center For Information Technology and Management Briefings Paper 96-BP-001, 1996.

[15] C. Curtis, EDI over the Internet: let the games begin, Commun. Week 627 (59) (1996).

[16] C. Frye, EDI users explore Internet as tool of trade, Software Mag. 15 (13) (1995).

[17] P. Gill, Manufacturers cautious on the Internet, Software Mag. 16 (5) (1996).

[18] C. Harler, Logistics on the Internet: freeway or dead end?, Transport. Distr. 37 (4) (1996).

[19] E. Messmer, Chase Manhattan parks VAN, drives up to Internet, Network World 13 (37) (1996).

[20] E. Messmer, The Internet rocks EDI boat, Network World 13 (18) (1996).

[21] K. Nash, Internet EDI on horizon, Computerworld 30 (5) (1996).

[22] A. Segev, D. Wan, C. Beam, B. Toma, D. Weinrot, Internet-based financial EDI: a case study, The Fisher Center for Management and Information Technology Working Paper CITM-95-WP-1006, 1995.

[23] K. Weisul, Heavy hitters open doors to EDI over the Internet, Invest. Dealers Digest 62 (46) (1996).

[24] J. Davis, M. Parsons, EDI vendors adjust strategies in face of growing Internet, InfoWorld 17/18 (52) (1996).

[25] D. Kilbane, Services enable EDI exchanges by Internet, Automatic I.D. News 12 (9) (1996).

[26] E. Messmer, Harbinger gives EDI an Internet twist, Network World 13 (15) (1996).

[27] J. Minkoff, Internet appeal to business, Discount Merchandiser 36 (3) (1996).

[28] G. Socka, EDI meets the Internet, CMA Mag. 70 (5) (1996).

[29] T. Lappin, The airline of the Internet, Wired 4 (12) (1996).

[30] J. Gould, EDI Over the Internet, ec.com.3, No. 1 (Jan., 1997).

[31] A. Reinbach, Internet commerce slow, but moving forward, Bank Syst. Technol. 33 (10) (1996).

[32] A. Segev, J. Porra., M. Roldan, Internet-based financial EDI: the case of the Bank of America and Lawrence Livermore National Laboratory Pilot, The Fisher Center for Management and Information Technology Working Paper CITM-95-WP-1018, 1996.

[33] Premenos, templar software and services—secure, reliable, standards-based EDI over the Internet, http://www.templar.net/, 1996.

[34] Actra Business Systems, Actra business document gateway: Internet-centric electronic commerce messaging software, http://www.actracorp.com/002\_ind.html, 1996.

[35] M. Turner, The make/buy decision: getting it right, Network World 9 (17) (1992).

[36] Lawrence Livermore National Laboratory, Financial Electronic Data Interchange Pilot Project, UCRL-AR-1241103, 1996.

[37] S.L. Oswald, W.R. Boulton, Obtaining industry control: the case of the pharmaceutical distribution industry, California Manage. Rev. 38 (1) (1995).

[38] V. Wheatman, EDI over the Internet: McKesson case study, The Gartner Group Electronic Commerce Strategies Research Note, 1996.

[39] S. Gore, Electronic data interchange (EDI) over the Internet, National Information Infrastructure Testbed, http://www.infotest.com, 1996.

[40] A. Meyer, Adapting to environmental jolts, Admin. Sci. Q. 27 (4) (1982).

[41] A. Meyer, J. Goes, G. Brooks, Organizations reacting to hyperturbulence, in: G.P. Huber, W.H. Glick (Eds.), Organizational Change and Redesign: Ideas and Insights for Improving Performance, Oxford Univ. Press, New York, 1993.

[42] J. Porra, Colonial Systems, Information Colonies and Punctuated Prototyping, Jyvaskyla Univ. Press, Jyvaskyla, Finland, 1996.

[43] C. Gersick, Revolutionary change theories: a multilevel exploration of the punctuated equilibrium paradigm, Acad. Manage. Rev. 16 (1) (1991).

[44] E. Romanelli, M. Tushman, Organizational transformation as punctuated equilibrium: an empirical test, Acad. Manage. J. 37 (5) (1994).

[45] J. March, Footnotes to organizational change. Admin. Sci. Q. 26 (1981)

![](/api/attachments/TJFA5CGT/fulltext/images/e9866026576424e8e240ffeca299ec6052a272d28d40d4d2f39adb7fc8558d12.jpg)

Arie Segev is a professor at the Haas School of Business and the Director at the Fisher Center of Management & Information Technology, at University of California, Berkeley, where he has been responsible for a variety of industry-oriented research and out-reach activities. He also has an affiliate faculty position with the Computer Science Research & Development of Lawrence Berkeley National Laboratory. Professor Segev's research has dealt with various issues re-

lated to Electronic Commerce, Information Management technologies, techniques and methodologies, including temporal data management, data quality, the integration of AI and Database technologies, semantic data integration, information modelling and its relation to business process re-engineering, and financial and manufacturing information systems. More recently, he has been leading projects on business and technology issues in electronic commerce, including CommerceNet sponsored projects on Designing Electronic Catalogs for Business Value and Internet-Based Financial Electronic Data Interchange (EDI). Professor Segev has published over 70 papers on the above topics in leading journals and conferences, consulted government and industry, and has been the recipient of major research grants. He has been the Editor-in-Chief of ACM SIGMOD RECORD for seven years, and is on the editorial board of IEEE Transactions of Knowledge & Data Engineering, Information System Research, INFORMS Journal on Computing, and the Journal of Internet Purchasing. He is a member of ACM, INFORMS, the IEEE Computer Society, and the San Francisco Bay Area CIO Forum. He received his PhD from the University or Rochester in 1984.

![](/api/attachments/TJFA5CGT/fulltext/images/1243438e80eddcae2365a7a159ab24b5caf58738c5b3fbda7f2b7f37ebc03aa0.jpg)

At the time of the article, Jaana Porra, PhD, was a Research Fellow at the Fisher Center for Information Technology and Management at the Haas School of Business, University of California, Berkeley. At Berkeley, Jaana's research interests include social, organizational and business impacts and electronic commerce and the Internet. Jaana Porra has over a decade long consulting career in designing large scale open system networks for corporations and government offices in Europe. Jaana Porra's current academic affiliation is with the University of Houston, College of Business and Administration as a Visiting Assistant Professor. In Houston, Jaana works on developing theoretical and conceptual foundations for studying the long term impact of global computer networks on homo sapiens based on species level evolution in nature.

![](/api/attachments/TJFA5CGT/fulltext/images/b2bbb01e85f73811344acbba26109f43b9c9d6e84ce4dfd427712daa8d83b9bd.jpg)

Malu Roldan is a lecturer at the Haas School of Business and Research Fellow at the school's Fisher Center for Information Technology and Management. She has more than ten years experience with management education and research. She recently completed PhD Studies at UCLA's Anderson School, studying the change processes of hospital displaying different patterns of success and flexibility. Her current research focuses on change management issues

associated with the rapid deployment and evolution of web technologies. During her management studies, Malu worked on special projects and developed computer training programs at the Anderson School. Previously, she held staff positions at Citibank, Hughes Aircraft and Grace Restaurant.
