---
otero_id: 10142
otero_key: "Z9TF3PMD"
title: "FinPathlight: Framework for an multiagent recommender system designed to increase consumer financial capability"
authors: "Lawrence Bunnell; Kweku-Muata Osei-Bryson; Victoria Y. Yoon"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113306"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# FinPathlight: Framework for an multiagent recommender system designed to increase consumer financial capability

Lawrence Bunnell, Kweku-Muata Osei-Bryson, Victoria Y. Yoon

Department of Information Systems, Virginia Commonwealth University, 301 W Main St., Richmond, VA 23284, United States of America

## A R T I C L E I N F O

Keywords: Knowledge-based recommender systems Ontology-based recommendation agents Multiagent systems Financial capability Consumer finance Financial planning

## A B S T R A C T

In consideration of the general lack of trust in human professional financial advisors due to conflicts of interest, and given inadequacies in terms of the utility of FinTech alternatives for financial goal recommendations, this study establishes a framework for an ontology-based, multiagent recommender system designed to improve financial capability through the recommendation of financial goals, called FinPathlight. The FinPathlight framework provides an architecture for a personal financial recommender system designed to identify and recommend specific, achievable financial goals appropriate to a wide range of financially situated users. This framework contributes principles of implementation for a novel financial technology (FinTech) application aimed at addressing a pervasive lack of trust surrounding traditional financial advisory services, as well as utility inadequacies within the current landscape for FinTech applications, providing a comprehensive set of practical and explicit financial goal recommendations. Considering the importance of users' adoption of an innovation, this study empirically tests its utility in terms of trust and perceived usefulness. The experimental evaluation results show that an application built using this framework would likely be perceived as trustworthy and useful to users for identification and selection of financial capability enhancing objectives.

## 1. Introduction

In spite of increased consumer protection regulations in the wake of the Great Recession of 2008, conflicts of interest between human fi nancial advisors and consumers remain pervasive in the industry: with traditional financial advisory firms consistently found to be placing their own interests ahead of their clients [1–5]. With the "trust" bar being set so low by human advisors, FinTech recommendation methods, which may be objectively reviewed and evaluated, may provide a means for a more trusted method of providing financial advisory services than their incumbent human counterparts [6].

Further, within the current landscape of financial technology (FinTech), the usefulness of applications designed to provide consumer financial decision support with financial goal recommendations are limited in scope; mainly to recommendation assistance with basic and limited, generic goals of increasing savings. To our best knowledge, no current FinTech application exists to specifically provide the re commendation of a comprehensive set of useful financial goals designed for wide range of users from a variety of financial backgrounds and situations. The need for this type of financial recommender system is evidenced by a recent ongoing survey by the National Financial Education Council (NFEC), which indicates that 70% of consumers do not understand how to set personal financial goals [7]. Numerous studies indicate that, for a significant number of U.S. households, traditional financial goal recommendations such as “buying a home”, “saving for retirement” or “investing for college education”, are beyond their current level of financial capability. To wit, the results of a 2015 FDIC survey categorized approximately 9.0 million households, or 7% of the U.S. population, as “unbanked”; meaning that they do not even have a savings or checking account [8]. Another approximately 24.5 million U.S. households, or 20% of the population, were deemed ‘underbanked’; meaning that, although they may have a savings or checking account, they still utilize alternative financial services (AFS), such as payday loans, refund anticipation loans, rent-to-own services, pawn shop loans, or auto title loans (often characterized as ‘predatory’ due to their rela tively high interest rates and repayment terms) [8]. For these consumers, a more useful recommender system might include recommendations for an array of specific, achievable financial goals such as how to efectively “make ends meet”, or the “appropriate utilization and management of financial products”; financial capability enhancing objectives typically eschewed by professional financial advisory services.

In consideration of the pervasive mistrust of human professional financial advisors and, given the inadequacies in terms of utility of

Table 1 Research questions.

<table><tr><td></td><td>Research questions</td></tr><tr><td>RQ1</td><td>How can we develop a framework for a personal financial recommender system (PFRS) designed to engender trust and provide useful recommendations for improving user financial capability through the identification, recommendation, and tracking of a comprehensive set of specific financial goals for a wide range of financially situated users?</td></tr><tr><td>RQ2</td><td>What architecture would be most suitable as a framework for a personal financial recommender system (PFRS) designed to improve user financial capability?</td></tr><tr><td>RQ3</td><td>How can we demonstrate that an application built using this PFRS framework would be perceived as more useful than current FinTech offerings for recommendation of financial capability enhancing goals?</td></tr><tr><td>RQ4</td><td>How can we demonstrate that an application built using this PFRS framework provides a trusted alternative to human financial advisors for financial goal identification and setting?</td></tr><tr><td>RQ5</td><td>How can we bridge the gap between design science and behavioral science research for the development of a design artifact and the evaluation of its utility to provide ex ante evidence that a future, fully functioning prototype application using the PFRS framework has potential for future user adoption?</td></tr></table>

FinTech alternatives for financial goal recommendation, this research addresses a current gap in the landscape of financial recommender systems. To address these gaps in the trustworthiness and utility of current recommendation systems, we specifically aim to address five research questions (RQ) (Table 1).

In answering these research questions, we develop a framework, called FinPathlight, for a FinTech application designed to provide financial goal recommendations for a wide range of consumers with varying levels of financial capability. In order to assess the viability of an application built using the FinPathlight framework in this study, we evaluate the framework in terms of ‘trust’ and ‘perceived usefulness’; constructs adopted from a conceptual model for the evaluation of re commender systems [9]. In doing so, this study provides three primary research contributions (RC) (Table 2).

The remainder of this paper will be organized as follows: Section 2 provides a review of relevant literature and the current FinTech land scape related to this study. Section 3 discusses the design science research methodology applied to this study. In Section 4, we discuss the theoretical foundations of the study. Section 5 elaborates the implemented components of a multiagent architecture for a PFRS designed to increase consumer financial capability. Section 6 provides an experimental evaluation of the FinPathlight framework. Finally, Section 7 presents this study's contributions, limitations and future research.

## 2. Review of related literature

## 2.1. Recommender systems for financial planning

Within the area of Financial Planning, a subdomain of the domain of Finance, the majority of the extant recommender systems literature has focused on systems for providing suitable financial services or invest ment portfolio recommendations for professional financial advisors [10–13]. For direct-to-consumer financial planning, the recommender systems literature is relatively sparse. Research on a “personal financial planning tool”, for personal allocation of resources, was introduced by Fano and Kurth [14]. Their research develops a system to assist con sumers in facing multiple lifestyle choices with recommendations using a goals trade-of algorithm to maximize user satisfaction. A “pricing personalization” recommender system was proposed by Kamishima and Akaho [15], using a multi-stage process for identifying customer types. Their work focuses on detecting diferences between customer types for the purpose of determining which customers to ofer product discounts. The term “multi-stage” in their work is used to describe a phased population selection strategy, rather than a multiple stage recommendation process. Taghavi, et al. [16] presents a preliminary design for a hybrid recommender system to assist users in providing personalized decision support for the specific financial objective of equities selection recommendations. A financial planning recommendation system using content-based, collaborative, and demographic filtering for assisting users in finding financial planning recommendations is developed and evaluated [17]. The research addressed development and evaluation of a hybrid recommender system for financial investments to satisfy two specific financial objectives: 1) protecting income, and 2) saving for the future. Jung, et al. [18] was a design science research aimed at deriving and evaluating principles for a FinTech application to provide investment decision support specifically for risk-averse, low-budget consumers. However, their research did not provide an architecture for such a system nor did it address decision support for a comprehensive set of financial goals for a wide range of financially situated users. To the best of our knowledge, no recommender system research currently exists which addresses development of an application framework to provide trusted financial goal recommendations from a comprehensive set of specific, useful financial objectives designed for improving financial capability for a wide range of financially situated consumers.

## 2.2. FinTech

In common usage, the term ‘FinTech’ most often refers to recent disruptive digital technologies aimed at addressing existing customercentric deficiencies in traditional Financial Services Institutions' (FSI's) product oferings [19]. A number of FinTech alternatives to traditional FSI oferings have emerged to address various aspects of consumer financial behavior (Table 3). Though some overlap exists within the services provided by these FinTech's, the categories listed describe the primary focus of the examples provided. It should be noted that several of these oferings, such as ‘MINT®’, one of the more popular FinTech applications [20,21], include, as an add-on to their core ofering, goal recommendation and tracking functionality for a relatively small number of generic financial goals (e.g. saving for a home, retirement or college).

Table 2

<table><tr><td></td><td>Research gap</td><td>Research contribution</td><td>Research question addressed</td></tr><tr><td>RC1</td><td>Lack of a trusted financial recommender system designed to provide users with useful financial goal recommendations.</td><td>Guidelines for development of useful and trustworthy ontology-based, multiagent personal financial recommender system.</td><td>RQ1, RQ2</td></tr><tr><td>RC2</td><td>Research incorporating an empirical evaluation in terms of trust and perceived usefulness of a financial goal setting recommender system</td><td>Rigorous empirical evaluation of the proposed artifact with human subjects through development of a behavioral research model which evaluates the artifact from a user perspective.</td><td>RQ3, RQ4</td></tr><tr><td>RC3</td><td>Integration of design science and behavioral science research paradigms for development and evaluation of design artifacts.</td><td>Articulation of how the research methods of both design science and behavioral research can be integrated for the development of a design artifact and the evaluation of its utility.</td><td>RQ5</td></tr></table>

Table 4  
Table 3  
Examples of current FSI alternative Fintech categories, applications and characteristics.

<table><tr><td>Category</td><td>FinTech examples</td><td>Characteristics</td></tr><tr><td>Automated savings/investment</td><td>Acorns, Bumped, Qapital, Digit, Evati, SavedPlus, Stash, Clarity Money, Saverlife, Coinout, WinWin</td><td>Electronic automated savings programs</td></tr><tr><td>Blockchain/digital currency</td><td>Bitcoin, Binance, Coinbase, Ripple, Kyber, Tron, Bifinex, Kraken, Monero, Bitstamp</td><td>Use of distributed ledger technologies in payment, clearing and settlement</td></tr><tr><td>Credit monitoring</td><td>CreditKarma, WalletHub, CreditWise, MyFICO, CreditWorks</td><td>Cloud-based credit reporting and tracking</td></tr><tr><td>Digital payments</td><td>Paypal, Venmo, SquareCash, GooglePay, Zelle, ApplePay</td><td>Online payment and money transfer</td></tr><tr><td>Investment advisory</td><td>Wealthfront, Betterment, Robinhood, PersonalCapital,</td><td>Alternative electronic investment advisory services</td></tr><tr><td>Money management</td><td>Goodbudget, You Need A Budget (Ynab), Toshl, BudgetSimple, Level, Budgt</td><td>Cloud-based budgeting and financial planning tools</td></tr><tr><td>Neobanks</td><td>Chime, Varo, Aspiration, Ally, Salem Five Direct, Radius, iGoBanking</td><td>Digital only banking services</td></tr><tr><td>Peer-to-Peer Lending</td><td>Sofi, Prosper, Upstart, Lending Club,</td><td>Crowd-sourced and online-only lending platforms</td></tr><tr><td>Crowd funding</td><td>GoFundMe, KickStarter, IndieGoGo</td><td>Crowd-sourced online funding platforms</td></tr><tr><td>Tracking spending habits</td><td>Wally, MINT, PocketGuard, Spendee, Joy, LearnVest</td><td>Digital tracking and categorization of expenses</td></tr><tr><td>Financial goal recommendation</td><td>{FinPathlight}</td><td>Recommendation and tracking of financial goals</td></tr></table>

However, the usefulness of these applications for improving consumer financial capability through goal recommendation is limited by oferings which contain only a minimal set of financial goal recommendations designed for consumers who are already, at least, moderately financially capable. To the best of our knowledge, no existing FinTech applications specifically address the recommendation and tracking of financial goals. This may be in part due to the lack of a comprehensive trusted ontology of specific, useful financial recommendation objectives and tasks related to the concept of improving financial capability. The FinTech companies listed here exclude traditional FSI's oferings. While many FSI's have now integrated technological products into their core oferings and, a number have purchased or partnered with FinTech startups [22], none, that we are aware of, ofer a product specifically aimed at providing a comprehensive set of recommendation objectives suitable to a wide range of financially si tuated users.

## 3. Design Science Research (DSR) methodology

Within the field of IS, Design Science Research (DSR) is a paradigm for the conceptualization, design, evaluation, and communication of the development of technology-based artifacts that solve real-world problems, while providing contributions to the existing body of knowledge. The DSR approach communicated within this research incorporates the work of Hevner [23] and Pefers [24], along with the Information Systems Design Theory (ISDT) suggested by Gregor and Jones [25]. The ISDT identifies eight components of DS research: 1) purpose and scope; 2) constructs; 3) the principle of form and function; 4) artifact mutability; 5) testable propositions; 6) justificatory knowledge; 7) principles of implementation; and 8) expository instantiation. The purpose and scope component specifies “meta-requirements or goals” for a design artifact. Constructs refer to the building blocks of a design. The principle of form and function are the principles that specify the structure, organization, and functioning of the design product and/ or design method. The artifact mutability component refers to the gen eralizability of a design as it works with its potential, alternative applications. The fifth component of an ISDT suggests that design science research be guided by testable propositions or hypotheses about design artifacts to be developed. These propositions or hypotheses posit that instantiated design artifacts would produce certain outcomes if the principles are followed. The justificatory knowledge (a.k.a., kernel theory) component explains why a design artifact is developed as it is and why it works. Principles of implementation refers to the manner in which the design is brought into material being by human actors who wish to use it for its stated purposes. Finally, expository instantiation covers the manner in which a design is materialized. Expository instantiation enables for a rigorous evaluation of the design output with respect to its purpose and scope. Table 4 summarizes our study along the eight components of the ISDT.

<table><tr><td colspan="2">FinPathlight recommender system information systems design science components</td></tr><tr><td>Purpose and scope</td><td>The purpose of this research is to develop a framework for an ontology-based, multiagent personal financial recommender systems (PFRS) for decision support through recommendations of financial goals designed to enhance financial capability.</td></tr><tr><td>Constructs</td><td>This study utilizes previously identified evaluation constructs germane to the evaluation of recommendation agents from a user perspective: 1) ‘Trust’, and 2) ‘Perceived Usefulness’. [9].</td></tr><tr><td>Principle of form and function</td><td>The artifact developed by this research is a framework which functions as a recommendation agent for a PFRS utilizing the principles of recommender systems technologies. The FinPathlight framework consists of seven agents: User Interface Agent, Financial Data Import Agent, Search Engine Agent, Recommendation Agent, Storage Agent, Ontology Agent, and Learning Agent.</td></tr><tr><td>Artifact mutability</td><td>The artifact in this research study has been developed with an eye to generalizability, adaptability and future modification. For example, the proposed framework might be applied to other consumer objectives-based recommendation applications requiring a ontology-based, multi-agent approach such as health and fitness or career goals.</td></tr><tr><td>Testable proposition</td><td>Six theoretically motivated hypotheses have been developed to evaluate the framework artifact (Table 7).</td></tr><tr><td>Justificatory knowledge</td><td>The design of the FinPathlight framework is informed by two major kernel theories: Financial Capability [26,27], and Multiagent Systems [28] with Role-Based Agent Design [29]. Additionally, the evaluation of the PFRS framework utilizes constructs from the Technology Acceptance Model (TAM) [30] incorporating the conceptual model of Xiao and Benbassat [9] regarding evaluations of recommender systems from a user perspective.</td></tr><tr><td>Principles of implementation</td><td>Guidelines are provided for development of an ontology-based, multiagent PFRS. These guidelines provide the architecture for development of a mobile application for improving financial capability through financial goal setting.</td></tr><tr><td>Expository instantiation</td><td>In this research we utilize a simulated artifact in the form of a high-fidelity wire-frame prototype to instantiate a framework for a multiagent PFRS incorporating an ontological knowledgebase for evaluation purposes.</td></tr></table>

## 4. Theoretical framework

In developing the framework, the two major kernel theories which have informed us are: 1) the Financial Capability Model and 2) Multiagent System with Role-Based Agent Design.

## 4.1. Financial capability model

In order to integrate the concepts of trustworthiness and utility within our framework, we incorporate the Financial Capability model as justificatory knowledge in the design of our PFRS. Utilizing the Financial Capability model assists in aligning our framework with previously peer-reviewed studies by researchers and trusted regulatory entities on constructs shown to provide utility for improving consumer financial capability. The term ‘financial capability’ describes people's financial knowledge, confidence and motivation to manage personal finances [26]. According to a study by the U.S. Consumer Financial Protection Bureau (CFPB), financial capability is comprised of 1) financial skill, 2) financial behavior, 3) financial situation, and 4) fi nancial well-being (Fig. 1) [27,31]. A critical skill and behavior associated with financial well-being is appropriate financial goal setting [32]. Consumers with higher confidence in achieving financial goals have higher levels of financial well-being [33].

A number of constructs associated with financial capability have been referenced in the literature [26,27,34–37]. The 2015 National Financial Capability Study (NFCS) provides the following components of financial capability: 1) ‘Making Ends Meet’- consumers ability to pay their bills and manage their income and expenses, 2) ‘Managing Financial Products’- the efective use and management of financial products, 3) ‘Planning Ahead’- financial appropriation for the future, and 4) ‘Financial Knowledge and Decision Making’- incorporates information about financial education, attitudes and behaviors [36].

## 4.2. Multiagent system and role-based agent design method

Frameworks are conceptual models for organizing ideas and facilitating discussions about information systems [38]. For practitioners, frameworks provide the structural foundation, functionalities and principles of implementation of IT project solutions. As conceptual models, they provide a means of communication between designers and developers and assist in early detection and correction of errors [39]. In designing a conceptual model for a practical application, we have adopted a multiagent systems approach to the development of the FinPathlight framework.

The term multiagent systems (MAS) in IS literature refers to distributed computer systems that are composed of two or more agents that are capable of autonomous action and environmental interaction with other agents [29]. MAS are ideally suited for complex problem solving, such as recommendation activities which involve user classification and item selection [40].

The role-based agent architecture has been one of the most widely studied approaches for the design of multiagent systems. Role-based approaches include Gaia [29], Multiagent Systems Engineering (MaSE) [41], ALAADIN framework [42], role-based collaboration mechanisms [43,44], and others. A role is defined as an abstract description of a system's expected function [29]. An agent can be viewed as an actor who performs a role or a set of roles. This role-based approach has been used in the design of numerous multiagent systems [45–47].

A multiagent architecture was selected for the FinPathlight framework because MAS provide a number of unique attributes that make them particularly suitable for domains requiring multiple role-based tasks. Specifically, for the development a personal financial recommendation system, the role-based modeling approach guides us in identifying a variety of roles necessary to perform the designated task required of human users for the recommendation, selection and tracking of useful financial goals, and assigning specific roles to be performed by certain agents for each of those tasks.

## 5. FinPathlight: multiagent recommender systems framework

Following the widely adopted role-based agent design method, we have first analyzed the requirements and identified a variety of roles necessary for the framework to perform. During the design phase, we have assigned a number of closely related roles to the same agent in order to reduce communication overhead. Table 5 shows a set of roles identified for the framework and the agents which are assigned to perform those roles.

Our role-based agent analysis and design have developed the FinPathlight framework which consists of: 1) User Interface Agent (UIA), 2) Financial Data Import Agent (FDIA), 3) Search Engine Agent (SEA), 4) Recommendation Agent (RA), 5) Storage Agent (SA), 6) Ontology Agent (OA), and 7) Learning Agent (LA) (Fig. 2). In the following sections, we discuss the agents UIA and OA implemented and evaluated within this study.

## 5.1. User Interface Agent (UIA)

In multiagent systems, a user interface agent provides the role of user interaction directly through the inputs and outputs of a user interface and allows the system to take actions by invoking commands provided by the interface [48–50]. The FinPathlight User Interface Agent (UIA) provides a familiar interface for satisfying system requirements of: 1) creating and modifying a user account, 2) logging in/out, 3) capturing information about the user, 4) importing and updating financial data (FDIA), 5) allowing financial goal search, 6) displaying financial goal recommendations from the ontology agent (OA), 7) user entry and modification of inputs, 8) tracking of financial goals, and 9) obtaining feedback from the user. The FinPathlight UIA provides a means of conveying to users what information is captured and utilized by the recommendation agent (RA) and for displaying explanations of recommendation results; thereby afording the user recommendation logic transparency and results scrutability. In recommender systems research, interface familiarity, transparency and results scrutability are key issues associated with ‘trust’ and ‘perceived usefulness’ [9,51,52]. Within the FinPathlight PFRS, the UIA displays financial recommendations based on knowledge classification provided through an Ontology Agent (OA).

Full Model of Financial Capability  
Fig. 1. Full model of financial capability.  
![](/api/attachments/Z9TF3PMD/fulltext/images/fcea4723bdde4560ce821d0ca62c1d6870a8382718762de74cccf9e403cb6e5c.jpg)

Table 5  
Roles and corresponding agents.

<table><tr><td>Role</td><td>Corresponding agent</td></tr><tr><td>Interacting with users</td><td>User Interface Agent</td></tr><tr><td>Data import, data export</td><td>Financial Data Import Agent</td></tr><tr><td>Item search</td><td>Search Engine Agent</td></tr><tr><td>Make recommendation</td><td>Recommendation Agent</td></tr><tr><td>Store user profile, history</td><td>Storage Agent</td></tr><tr><td>Working with ontology</td><td>Ontology Agent</td></tr><tr><td>Learning</td><td>Learning Agent</td></tr></table>

## 5.2. Ontology Agent (OA)

Ontology agents in multiagent systems (MAS) conduct the role of working with an ontological knowledgebase and enable the query of knowledge in distributed artificial intelligence applications [53]. An ontology agent provides an interface between the system and an ontology, allowing it to interact and share resources with other agents [50,54]. Use of semantic knowledge structures, such as ontologies, can help facilitate recommendations through the following methods: 1) contextualization of a users' situation, 2) guaranteeing of inter-operability with system resources, and 3) allowing inferences where users profiles are incomplete [55]. Drawing upon the representation model of representation theory [56], we have developed a Consumer Financial Goals Ontology (CFGO) [57]. Within the FinPathlight framework, the OA manages, searches, and returns items contained within CFGO in accordance with the specific ontology language utilized for its encoding, OWL/XML. Using an ontology agent in conjunction with the FinPath light RA allows for improved recommendation quality through access to the formal representation of domain knowledge, along with reasoning, to enhance recommendation quality. In order to ensure the usefulnes of recommendations to particular user classifications, a knowledge based assignment of recommendation items from the Consumer Financial Goals Ontology to user classification categories was developed utilizing a popular method of developing a consensus opinion, known as the Delphi Method [58–60] (Table 6).

During this assignment process, semi-structured interviews were held between the authors and financial domain experts; a group of six (6) senior and mid-level executives from several consumer finance segments including consumer mortgage, banking and credit within a large, super-regional FSI in order to assist in determining which financial goal recommendations would be most useful to users at various stages of financial capability. Through this socialization to the model, user classification designations for the FinPathlight framework were categorized within the Consumer Financial Goals Ontology's top-level classes. These ontological top-level classes have been based on the previously referenced financial capability constructs derived from the literature [36,37]. Within the FinPathlight framework, these designations represent the various stages of financial capability through which users advance by completion of financial objectives associated with the categories. For example, the financial capability construct of ‘Making Ends Meet’, a top-level class in the ontology, has been designated a representative of an individual working towards financial stability; marked by establishment and strengthening of foundational financial capabilities. “Making Ends Meet” recommendation goals are associated with fundamental financial objectives such as ‘Establishing and Maintaining Credit,’ ‘Budgeting’, and ‘Managing Debt’. The financial capability construct of “Managing Financial Products” represents recommendations for users working towards financial independence; a stage where foundational financial goals have largely been met. Recommendations at this level of financial capability include financial goals designed for cultivating awareness and appropriate utilization of financial products such as various types of ‘Financial Accounts’, ‘Leases’, and ‘Loans & Credit’. For the FinPathlight RA, ‘Planning Ahead’ refers to a category of financial goals designed for individuals who have achieved a relatively

![](/api/attachments/Z9TF3PMD/fulltext/images/84ffab5546c424744eca97f928b111e8bda0d60001d9f97a187c7f6b0c80898f.jpg)  
Fig. 2. FinPathlight role-based, multiagent recommender system architecture.

FinPathlight user classification alignment with financial capability goals ontology constructs, themes and goals.

<table><tr><td>Financial capability constructs</td><td>Broad financial goals themes</td><td>Specific financial goals</td></tr><tr><td rowspan="8">Making Ends Meet</td><td>Managing Debt</td><td>Paying Down Debt, Debt Settlement, Renegotiating Debt Terms, Bankruptcy, Consumer Rights, Medical Debt, Debt Consolidation, Tax Debt, Debt Collectors, Disputing Debt, Lawsuits/Garnishments, Student Loan Debt</td></tr><tr><td>Establishing and Maintaining Credit</td><td>Understanding Credit, Credit Limits, Credit Terms, Credit Fees, Credit Grace Periods, Credit Interest Rates, Credit Laws &amp; Regulations, Credit Finance Charges, Credit Minimum Monthly Payments</td></tr><tr><td>Budgeting</td><td>Cash Flow Management, Budget Tracking, Budget Setting, Budgeting Tips, Emergency Fund</td></tr><tr><td>Transportation</td><td>Public Transportation, Private Transportation</td></tr><tr><td>Income</td><td>Employment, Non-Profit Jobs, Public Company Jobs, Private Company Jobs, Government Jobs, Job Search, Internships, Networking, Placement Agencies, Job Boards, Resume Building, Criminal Record, Increase Income, Education, Career-Vocational Training, Colleges/Universities, Work-Study Programs, College Grants, College Scholarships, Part-Time Job, Small Business, Online Income, Event Hosting, Home-Based Business, Knowledge Sharing, Asset Sharing</td></tr><tr><td>Expenses</td><td>Expense Reduction, Avoiding Fees, Insurance Reductions, Home Services, Miscellaneous Expenses, Utilities, Transportation, Health Expenses, Savings &amp; Investments, Loans &amp; Credit</td></tr><tr><td>Housing</td><td>Home Selling, For Sale by Owner, Real Estate Auction, Fair Housing, Home Search, Home Rental, Home Purchase, Mortgage Refinancing</td></tr><tr><td>Benefits Screening</td><td>Child Care Support, Health Benefits, Disability Support, Counseling Assistance, Military Benefits, Social Security Benefits, Educational Benefits, Income Assistance</td></tr><tr><td rowspan="5">Managing Financial Products</td><td>Financial Accounts</td><td>Investments, Equities, Bonds, Options, ETFs, ETNs, Mutual Funds, Derivatives, Commodities, Warrants, Hedge Funds, Investment Real Estate, Banking, Checking Accounts, Money Market Accounts, Certificates of Deposit,</td></tr><tr><td>Leases</td><td>Auto Leasing, Personal Property Leasing, Equipment Leasing, Rent-to-Own, Real Property Leases</td></tr><tr><td>Loans &amp; Credit</td><td>Secured Loans, Mortgage Loans, Pre-paid Credit Cards, Bridge Loans, Title Loans, Auto Loans, Asset Secured Loans, Pawnbroker Loans, Unsecured Loans, Term Loans, Credit Cards, Cash Advances, Veteran Loans, Peer-to-Peer Lending, PayDay Loans, Signature Loans, Lines of Credit, Student Loans</td></tr><tr><td>Identity Protection</td><td>Credit Monitoring, Identity Theft, Identity Protection Monitoring, Identity Recovery, Identity Theft Insurance</td></tr><tr><td>Money Transfers</td><td>Wire Services, e-Transfers, Bank Transfers</td></tr><tr><td rowspan="5">Financial Planning</td><td>Estate Planning</td><td>Estate Planning, Estate Planning Trusts, Wills &amp; Testaments</td></tr><tr><td>Financial Charity</td><td>Charitable Trusts, Charitable Insurance Policies, Estate Planning Gifts, Charitable Foundations</td></tr><tr><td>Retirement Planning</td><td>SSA Retirement Account, Government Retirement Accounts, Pensions, Retirement Accounts, Health Savings Accounts, 401 k, Deferred Annuities</td></tr><tr><td>College Savings</td><td>College Savings Accounts, Prepaid Tuition Plans</td></tr><tr><td>Taxes</td><td>Income Tax, Property Tax, Real Estate Tax, Personal Property Tax, State &amp; Local Tax, Other Taxes</td></tr><tr><td rowspan="3">Financial Knowledge and Decision Making</td><td>Financial Behaviors</td><td>Saving, Investing, Spending</td></tr><tr><td>Financial Attitudes</td><td>Financial Well-Being, Financial Confidence</td></tr><tr><td>Financial Education</td><td>Financial Literacy, Financial Skills, Financial Numeracy</td></tr></table>

high measure of financial capability, wherein the main financial concern is for the proper planning, use, and redistribution of their wealth. For ‘Planning Ahead’ goal recommendations, the user will generally have acquired a relatively high level of financial stability and, at least, some degree of financial independence. This category provides goal recommendations for broad financial legacy objectives such as ‘Retirement Planning’, ‘Financial Charity’, and ‘Estate Planning’. Rather than forming a separate classification, the financial goals associated with the financial capability construct of “Financial Knowledge and Decision Making” were associated with the themes of ‘Financial Education’, ‘Financial Attitudes’, and ‘Financial Behaviors’, which were deemed logi cally compatible for user recommendations at all levels of financial capability and, therefore, within the FinPathlight RA, are designated as supplementary recommendations; informative and supportive to users for certain goals as they progress towards increased levels of financial capability.

## 6. Evaluation of the FinPathlight framework

Xiao and Benbasat [9] have created a conceptual model for the evaluation of recommendation agents. Based on the aim of our research, which is to produce a useful artifact to make an intervening change in the world through the application of constructive knowledge, in this evaluation we focus on a portion of Xiao and Benbasat's model; specifically, the constructs contained within the ‘User Evaluation of Recommendation Systems’ box highlighted in yellow (Fig. 3): 1) ‘Trust’, and 2) ‘Perceived Usefulness’ (PU).

Design science artifacts are assessed against criteria of value or utility – “does it work?” [61]. In their classification of DSR evaluation methods, Pefers, et al. [62] cite prototyping, simulations, scenarios, experiments, and expert evaluation as established methods of evaluating design science research, which are utilized within this study. Prototyping is a critical tool for evaluating design concepts, early detection of errors, and providing feedback and insights for minimal viable design leading to an improved solution [63].

In consideration of the purpose of the FinPathlight framework, which is to provide an architecture for the development of a FinTech application, and in order to assess the usefulness and trustworthiness of the artifact prior to the time and resource expenditure of building a fullyfunctioning prototype, we have utilized an iterative, exploratory approach through an ex ante evaluation of a potential FinTech mobile application using a series of illustrative use case scenarios within a high-fidelity wireframe prototype. High-fidelity wireframe prototyping of an interactive application allows users to examine and visualize use case scenarios, in the form of simulated process flows, as well as the look and feel of a system, prior to the large resource allocation required for the instantiation of an information technology application [64]. Evaluation through wireframe prototyping provides a formative assessment, which also serves to inform an iterative design and development process [65]. A high-fidelity wireframe prototype based on the FinPathlight framework serves to demonstrate the utility and trustworthiness of the artifact as well as how an instantiation based on the framework meets our theoretically motivated evaluation hypotheses.

## 6.1. Hypotheses for evaluation of the FinPathlight framework

The study done by Wimmer and Yoon [66] evaluates the utility of the proposed design artifact (counterfeit score of a product) in terms of its ability to increase the trustworthiness of a product and to decrease perceived risks of purchasing the product. Informed by this evaluation approach, and Xiao & Benbasat's concept model [9], we have developed six theoretically motivated hypotheses to evaluate the FinPathlight framework from a user perspective, through the constructs of ‘Trust’ and ‘Perceived Usefulness’ (Table 7). These hypotheses will help to establish whether an application based on the FinPathlight framework would be deemed as trusted and perceived as useful for the recommendation of financial goals. and whether it compares favorably. in terms of ‘trust and 'perceived usefulness', to other available sources of financial goal recommendations such as human financial advisors and currently available commercial FinTech applications.

![](/api/attachments/Z9TF3PMD/fulltext/images/6c0607adb4d07e842668524e649a0e59264d6c954e9f39b6c9bc3f0e48113156.jpg)  
Fig. 3. Conceptual Model of Evaluation Constructs for Recommender Systems (Adapted from Xiao and Benbasat 2007)

Table 7  
Theoretically motivated hypotheses for evaluation of the FinPathlight Recommender System Framework.

<table><tr><td>#</td><td>Testable hypothesis</td></tr><tr><td>H1</td><td>Users of a FinTech application based on the FinPathlight framework will deem the system to be trustworthy.</td></tr><tr><td>H2</td><td>Users of a FinTech application based on the FinPathlight framework will deem the system as being useful for recommendation of financial goals.</td></tr><tr><td>H3</td><td>Users of a FinTech application based on the FinPathlight framework will perceive the system as equivalent to human sources of financial goal recommendation in terms of trust.</td></tr><tr><td>H4</td><td>Users of a FinTech application based on the FinPathlight framework will perceive the system as equivalent to human sources of financial goal recommendation in terms of perceived usefulness.</td></tr><tr><td>H5</td><td>Users of a FinTech application based on the FinPathlight framework will perceive the system to be as trustworthy as leading commercial FinTech apps, as a source of financial goal recommendations.</td></tr><tr><td>H6</td><td>Users of a FinTech application based on the FinPathlight framework will perceive the system as more useful than leading commercial FinTech apps, as a source of financial goal recommendations.</td></tr></table>

## 6.2. FinPathlight high-fidelity wireframe prototype and process flows

In order to perform an experimental evaluation, a simulation artifact in the form of a high-fidelity wireframe prototype for a FinTech mobile application based on the FinPathlight framework was developed using Adobe XD, a vector-based tool for designing and prototyping user experiences for web and mobile apps [67] (Fig. 4).

To assess the usefulness and trustworthiness of an application based on the framework, a series of use case scenario process flows were developed using the wireframe prototype. The process flows in Table 8 were developed in order to demonstrate how issues associated with ‘Trust’ and “Perceived Usefulness” in recommender systems literature have been addressed within the FinPathlight framework, including: 1) familiarity of the user interface to other widely used applications, 2) detailed information provided, 3) user control of inputs and re commendation selection, 4) ease of use, 5) transparency into the recommendation process, and 6) appropriateness of recommendations [9,51]. For example, Process Flow #1 provides the user with a familiar mobile user interface with easy to follow, step-by-step input forms with instructions and links to help information available on each screen. It also provides the user with control over their personal and financial data inputs, as well as transparency as to what types of information about the user the system will utilize, in order to make appropriate financial goal recommendations (Fig. 5).

A survey was created and administered to a group of financial domain experts from various consumer finance segments (including executives and employees from credit, mortgage, marketing and consumer banking) within a large, super-regional FSI (89% of respondents)), along with several Ph.D. level graduate students and professors from a large public university (11% of respondents). As part of the survey, participants were provided with: 1) a description of the FinPathlight framework, 2) a link and QR code (Passcode: ‘vcu2019A’) to a high-fidelity, wire-frame prototype of an interactive application interface, and 3) a within-subjects experiment survey with measures formulated to assess the evaluation constructs of ‘Trust’ and ‘Perceived Usefulness’.

At the end of the wireframe prototype process flow review, survey participants were asked to assess the prototype in terms of the evaluation constructs of our study: 1) ‘Trust’ and 2) ‘Perceived Usefulness’ (Table 9). We adapted the previously validated measurement items from the recommender systems literature [68,69] to operationalize these evaluation constructs [9].

Participation recruitment took place through email invitation. No financial or other incentives were ofered to participate in the study. The survey was hosted by online survey provider SurveyMonkey.com. The results were gathered from participants who responded to the survey invitation and completed the survey between March 21 and April 1, 2019; a total of 118 responses were received, with 97 com pleted responses and 21 incomplete responses. Incomplete responses were ignored in our analysis. In Step 1 of the survey, a survey description was provided; Step 2 provided the survey privacy policy. In

![](/api/attachments/Z9TF3PMD/fulltext/images/1145eb6217de850eeff8dd44026c71eeca1897344fd03b43fbdd66a30edf92f2.jpg)  
Fig. 4. Sample screenshots of a high-fidelity wireframe prototype of an example mobile application based on the FinPathlight framework developed using Adobe XD.

Step 3, participants were asked a series of questions regarding their age range, occupational industry, familiarity with recommender systems, and current methods for obtaining financial goal recommendations. In Step 4 of the survey, participants were given a series of six statements (Table 9), with responses on a 5-point Likert scale to rate their agree ment with the statement (1 = “Strongly Disagree”, 2 = “Disagree”, $3 = { ^ { \circ } N e u t r a l ^ { \prime \prime } } , 4 = { ^ { \circ } A g r e e ^ { \prime \prime } }$ , and 5 = “Strongly Agree”) based on their current method of obtaining financial goal recommendations. Next, before Step 5 of the survey, participants were provided with a link and

QR code to view the set of process flows illustrated through the highfidelity, wireframe prototype of a mobile application based on the FinPathlight framework. In Step 5, after viewing the prototype, they were again asked to rate the same six statements from Table 9; this time in reference to their assessment of the FinPathlight wireframe prototype. In the final Step 6 of the survey, participants were allowed to provide any comments for improving the FinPathlight prototype application, which provided additional qualitative feedback.

Table 8  
Process flows of FinPathlight framework wire-frame prototype.

<table><tr><td>Process flow #</td><td>Description</td><td>Issue addressed</td></tr><tr><td>1</td><td>Provides example of the process for a new user registration and user-profile setup. It would allow the user to: 1) register to create an account, 2) view information about the app, 3) enter demographic, employment, education, housing and financial information (Fig. 5).</td><td>[1] Familiarity,[2] Detail,[3] User control,[4] Ease of use,[5] Transparency</td></tr><tr><td>2</td><td>Provides an example of the process for financial data imported from sources such as financial institutions and credit bureaus. This information will be utilized as part of the real-world assessment of the user&#x27;s financial capability for the purpose of personalization of financial goals</td><td>[1] Familiarity,[3] User control,[4] Ease of use</td></tr><tr><td>3</td><td>Provides illustration of an assessment designed to assess the user&#x27;s subjective financial well-being based on the CFPB&#x27;s FWBS (CFPB 2017) and the initial Financial Capability Score calculated by the system as a result of the user inputs.</td><td>[5] Transparency; [6] Appropriateness</td></tr><tr><td>4</td><td>For an illustration of a ‘Making Ends Meet’ financial goal recommendation. In this example, the user is presented with recommended financial goals and has selected “Creating a Budget” from the ‘Making Ends Meet’ category. For this process flow, only one path will be highlighted. The example demonstrates how, during the budget setting process, a user would enter budget amounts for each budget category (e.g home, auto, health, etc.), opt for budget recommendations based on their user profile information and import actual expenses from their financial services account(s).</td><td>[2] Detail,[4] Ease of use,[6] Appropriateness</td></tr><tr><td>5</td><td>This process flow demonstrates a user goal selection from the ‘Managing Financial Products’ category of “Opening a Checking Account”. In this scenario, the user would be able to a) learn about the appropriate use of various types of checking accounts (e.g. free checking, interest checking, rewards checking, etc.), b) compare rates from different financial institutions, and if deemed necessary by the user, c) open a checking account. The process flow indicates that in a working application, the FinPathlight app would connect a user to their selected financial institution&#x27;s online checking account application page in a browser window to complete the process.</td><td>[2] Detail,[4] Ease of use,[6] Appropriateness</td></tr><tr><td>6</td><td>Provides an example of a financial goal recommendation from the ‘Planning Ahead’ category. The user, in this example, has selected a financial goal of ‘Establishing an Asset Protection Trust’. The process flows demonstrate that in a functional implementation, the financial goal would include information allowing a self-assessment of the need for an asset protection trust and, if deemed appropriate by the user, recommendation of a financial advisor would correspond to the user&#x27;s answers to a series of interactive questions.</td><td>[2] Detail,[4] Ease of use,[6] Appropriateness</td></tr></table>

FinPathlight high-fidelity wireframe prototype use case scenario process flows utilized in the experimental survey associated with this research may be accessed with passcode ‘vcu2019A’.

![](/api/attachments/Z9TF3PMD/fulltext/images/ebcfca3ab49fdea023d78df3fc37ca61d900a08e27e84c60ffd4be779253f2f3.jpg)

![](/api/attachments/Z9TF3PMD/fulltext/images/7efe41754179e5383029d793d696d7d39bfcea1c7ceb971582ffdd15cad5b2bc.jpg)

![](/api/attachments/Z9TF3PMD/fulltext/images/eeccbad020e839d049038823742094e3a88ba5bc584f78460a9cd0452014a48d.jpg)

![](/api/attachments/Z9TF3PMD/fulltext/images/7cbb3f68e75c514cc9b5d3a78a6f5da739dfbc89a8c7da65ed06929d4241ab3b.jpg)  
Fig. 5. FinPathlight Process Flow #1.

## 6.3. Experimental evaluation result

Raw data was downloaded from the SurveyMonkey.com website in CSV format. The survey data was uploaded into both SPSS and QlikView for analysis. To begin, a descriptive frequencies table was calculated using SPPS (Table 10). The frequencies table demonstrates favorably positive (> 3) ratings for the FinPathlight app with median scores of 4.0 (‘Agree’) for all measurement items.

In order to establish the reliability and validity of our scales, we utilized SPSS to examine the constructs of ‘Trust’ and ‘Perceived Usefulness’. Cronbach's Alpha's of 0.817 and 0.899 respectively suggest

represents:

![](/api/attachments/Z9TF3PMD/fulltext/images/3d3386b718c5489d74654621397aa27cc4c12734d1616f164819b920bf4a9535.jpg)

your current financial status and knowledge and select from personalized financial goal recommendations along with methods for obtaining your goals. You can track your progress here and get updates on your financial capability score (FCS). Over time. you'll be able to not only see your FCS improve, but will undoubtedly realize the benefits of improved financial capability ir you and your family's lives such as: financial literacy. financial independence. financial confidence and financial security

that the survey question items have a relatively high internal consistency (Table 11). Due to the relatively small sample size, we also performed a Shapiro-Wilks test of normality, which indicated a nonnormal distribution with p-value ≤ .05 (Table 12).

Studies have shown that with small sample sizes and when populations are not normally distributed, the Wilcoxon Signed-Rank Test is more eficient than a parametric t-test; has a lower likelihood for Type I errors [70,71], and is more robust to somewhat asymmetrical population shapes [72]. Therefore, in order to test our theoretical hypotheses, we first performed a non-parametric, One-Sample Wilcoxon Signed-Rank Test. In this case, the null hypothesis is that the median is equal to 3.00 (‘Neutral’), with the alternative hypothesis being that the median was > 3 on a 5-point Likert scale (i.e. ‘Agree’ or ‘Strongly Agree’ with the statement). We use the 90% confidence level because with small samples sizes, where there is low power to detect an efect, the 90% confidence level has been generally accepted as a suficient statistical measure [73,74].

![](/api/attachments/Z9TF3PMD/fulltext/images/6a549b14c6961c908279aab25198e64bf3ba870a29370fb62f6c4230137013b4.jpg)

![](/api/attachments/Z9TF3PMD/fulltext/images/b4657ed9bcfb9fe5318ab1332dd29ce7a08c52ec903acfb0f621dde0513f628e.jpg)

![](/api/attachments/Z9TF3PMD/fulltext/images/0ffec60fe8f4b7bd409612179d643bfa287b8a5ba351922150498d61a79b23bc.jpg)  
Fig. 5. (continued)

The results of this statistical analysis indicate that the sample median scores are significantly diferent than the theoretical value of 3.00 since all p-values < .10 and positive Z-Scores indicate that the median rating is greater than the hypothesized median [75] (e.g. participants “Agree” or “Strongly Agree” with the statement) (Table 13). Based on these results, our first two theoretical hypotheses, H1) “Users of a FinTech application based on the FinPathlight PFRS framework will deem the system to be trustworthy.”, and H2) “Users of a recommender system application based on the FinPathlight PFRS framework will perceive the FinPathlight system as providing utility for improving their financial capability”, are supported.

Of the 30.51% of survey participants who indicated usage of a non-FinTech or human source of financial goal recommendations, 30.5%, the largest portion, selected a ‘Financial Advisor’ (FA) as their current source of financial goal recommendations. To compare FinPathlight with these human FA's, we next performed a Related-Samples Wilcoxon Signed Rank test for these survey respondents. As illustrated by the results, there were no significant diferences between the median ratings for FinPathlight and human FA's in terms of ‘Trust’ or ‘Perceived Usefulness

Table 10  
Survey responses descriptive frequencies statistics.

<table><tr><td rowspan="2"></td><td rowspan="2">N</td><td rowspan="2">Mean</td><td rowspan="2">Median</td><td rowspan="2">SD</td><td colspan="3">Percentiles</td></tr><tr><td>25</td><td>50</td><td>75</td></tr><tr><td>Trust1</td><td>97</td><td>3.96</td><td>4.00</td><td>0.594</td><td>4.00</td><td>4.00</td><td>4.00</td></tr><tr><td>Trust2</td><td>97</td><td>3.70</td><td>4.00</td><td>0.793</td><td>3.00</td><td>4.00</td><td>4.00</td></tr><tr><td>Trust3</td><td>97</td><td>3.44</td><td>4.00</td><td>0.866</td><td>3.00</td><td>4.00</td><td>4.00</td></tr><tr><td>PU1</td><td>97</td><td>3.73</td><td>4.00</td><td>0.757</td><td>3.00</td><td>4.00</td><td>4.00</td></tr><tr><td>PU2</td><td>97</td><td>3.67</td><td>4.00</td><td>0.787</td><td>3.00</td><td>4.00</td><td>4.00</td></tr><tr><td>PU3</td><td>97</td><td>3.67</td><td>4.00</td><td>0.851</td><td>3.00</td><td>4.00</td><td>4.00</td></tr></table>

Table 11  
Reliability statistics.

<table><tr><td>Construct</td><td>N</td><td>Cronbach&#x27;s alpha</td></tr><tr><td>Trust</td><td>3</td><td>0.817</td></tr><tr><td>PU</td><td>3</td><td>0.899</td></tr></table>

with all p-values > .10 (Table 14).

The statistical analysis results support our second pair of theoretical hypotheses, H3) “Users of a FinPathlight framework-based recommender system application will perceive the system as equivalent to human sources of financial goal recommendation in terms of ‘Trust’”, and H4) “Users of a

Table 9  
Validated survey items, associated constructs, measurements and literature references for evaluation of recommendation agents from a user perspective. (Adapted from Komiak and Benbasat 2006; Pu and Chen 2010)

<table><tr><td>Item #</td><td>Construct</td><td>Survey item</td><td>Item measurement</td><td>Literature reference</td></tr><tr><td>1</td><td>Trust</td><td>This recommender has good knowledge about financial goals.</td><td>Cognitive trust in competence</td><td>Komiak and Benbasat 2006</td></tr><tr><td>2</td><td>Trust</td><td>I consider this recommender to be of integrity.</td><td>Cognitive trust in integrity</td><td>Komiak and Benbasat 2006</td></tr><tr><td>3</td><td>Trust</td><td>I feel comfortable about relying on the recommender for my financial goal decisions.</td><td>Emotional Trust</td><td>Komiak and Benbasat 2006</td></tr><tr><td>4</td><td>Perceived Usefulness</td><td>The recommended items effectively helped me to find the ideal product or method.</td><td>Perceived Usefulness</td><td>Pu and Chen 2010</td></tr><tr><td>5</td><td>Perceived Usefulness</td><td>The recommended items influence my selection of financial goals.</td><td>Perceived Usefulness</td><td>Pu and Chen 2010</td></tr><tr><td>6</td><td>Perceived Usefulness</td><td>I feel supported in selecting financial goals with the help of the recommender.</td><td>Perceived Usefulness</td><td>Pu and Chen 2010</td></tr></table>

Table 12  
Shapiro-Wilk Test of Normality.

<table><tr><td></td><td>Statistic</td><td>df</td><td>p-value</td></tr><tr><td>Trust</td><td>0.957</td><td>97</td><td>0.003</td></tr><tr><td>PU</td><td>0.922</td><td>97</td><td>0.000</td></tr></table>

FinPathlight framework-based recommender system application will perceive the system as equivalent to human sources of financial goal recommendation in terms of ‘Perceived Usefulness’”. Given the high cost of professional financial advisors [76], this result in terms of ‘Perceived Usefulness’ favors a relatively low-cost alternative of a technology based FinPathlight application for millions of consumers unable to aford human professional financial advice. Further, given the equivalence in terms of ‘Trust’, Philippon [6] infers that a FinTech application based on the FinPathlight framework may provide a comparatively more accessible and transparent alternative to human financial advisors regarding the recommendation of financial goals.

Of the 69.5% of survey participants who indicated use of a FinTech app, the largest portion of those (56%) selected MINT® as their source of financial advice for financial goal setting. We performed another Related-Samples Wilcoxon Signed Ranks Test to compare median scores of FinPathlight with the MINT® application. Test results indicate no significant diference between the FinPathlight prototype and MINT® for the construct of ‘Trust’ at the 90% confidence level (Table 15). There was, however, a significant diference in favor of FinPathlight at the 90% confidence level with p-values < .10 for ‘Perceived Usefulness’ (0.073) (Table 15).

These results indicate that, in terms of ‘Perceived Usefulness’, FinPathlight received significantly more favorable rankings that MINT®. Therefore, hypotheses H5, “Users of a FinTech application based on the FinPathlight framework will perceive the system to be as trustworthy as leading commercial FinTech apps, as a source of financial goal recommendations”, and H6, “Users of a FinTech application based on the FinPathlight framework will perceive the system as more useful than leading commercial FinTech apps, as a source of financial goal recommendations” are also supported. Given that the FinPathlight prototype is a first iteration, simulated artifact, these results indicate that FinPathlight is deemed equivalent in terms of ‘Trust’ and preferred to a widely used, commercially refined FinTech application in terms of ‘Perceived Usefulness’ for the recommendation of financial goals.

## 7. Conclusion, limitations and future research

Despite concerns with the general lack of trust in human profes sional financial advisors due to conflicts of interest, and given the inadequacies, in terms of utility, of FinTech alternatives for financial goal recommendations, no recommender systems are currently available to provide consumers with a comprehensive set of trusted and useful financial goals recommendations. As evidenced by our review of the literature, most of the existing recommender system research relating to financial planning has been directed towards professional advisory services. To fill this gap in the literature, the aim of this study has been the development of a framework for a FinTech recommender system which would provide consumers a level of trust and utility requisite to the recommendation of financial goals. We propose the framework, called FinPathlight, which can be used to build a FinTech application designed to provide financial goal recommendations for a wide range of consumers with varying levels of financial capability. In order to assess the utility of an application built using the FinPathlight framework from a user's perspective, we empirically evaluate the framework with human subjects in terms of ‘Trust’ and ‘Perceived Usefulness’. The results of our experiment indicate that, from the user's perspective, the FinPathlight framework provides for a relatively high level of recommendation trust and perceived usefulness for the task of financial goal setting.

Related Samples Wilcoxon Signed Ranks Test FinPathlight (FPL) and Financial Advisors (FA).

<table><tr><td></td><td>Pairs</td><td>Mean</td><td>STD</td><td>Neg.</td><td>Pos.</td><td>Tie</td><td>Z</td><td>p-Value</td></tr><tr><td rowspan="2">Pair 1</td><td rowspan="2">FA_Trust - FPL_Trust</td><td>3.754</td><td>0.6835</td><td rowspan="2"> $6^a$ </td><td rowspan="2"> $5^b$ </td><td rowspan="2"> $3^c$ </td><td rowspan="2"> $-0.275^d$ </td><td rowspan="2">0.783</td></tr><tr><td>3.778</td><td>0.8632</td></tr><tr><td rowspan="3">Pair 2</td><td rowspan="3">FA_PU - FPL_PU</td><td>3.702</td><td>0.8157</td><td rowspan="3"> $5^a$ </td><td rowspan="3"> $5^b$ </td><td rowspan="3"> $4^c$ </td><td rowspan="3"> $-0.517^d$ </td><td rowspan="3">0.605</td></tr><tr><td>3.667</td><td>0.8632</td></tr><tr><td>3.722</td><td>0.7519</td></tr></table>

<sup>a</sup> FA\_{construct\_name} < FPL\_{construct\_name}.  
<sup>b</sup> FA\_{construct\_name} > FPL\_{construct\_name}.  
<sup>c</sup> FA\_{construct\_name} = FPL\_{construct\_name}.  
<sup>d</sup> Based on negative ranks.

Related samples Wilcoxon Signed Ranks Test for FinPathlight (FPL) and MINT® FinTech app.

<table><tr><td></td><td>Pairs</td><td>Mean</td><td>STD</td><td>Neg.</td><td>Pos.</td><td>Tie</td><td>Z</td><td>p-Value</td></tr><tr><td rowspan="2">PPair 1</td><td>Mint_Trust</td><td>3.726</td><td>0.7568</td><td> $7^a$ </td><td> $55^b$ </td><td> $77^c$ </td><td> $-0.241^d$ </td><td>0.810</td></tr><tr><td>FPL_Trust</td><td>3.619</td><td>0.6522</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">PPair 2</td><td>Mint_PU</td><td>3.824</td><td>0.7180</td><td> $8^a$ </td><td> $33^b$ </td><td> $611^c$ </td><td> $-1.792^d$ </td><td>0.073</td></tr><tr><td>FPL_PU</td><td>3.249</td><td>0.7922</td><td></td><td></td><td></td><td></td><td></td></tr></table>

<sup>a</sup> Mint\_{construct\_name} $< \mathrm { \nabla \ F P L }$ \_{construct\_name}.  
<sup>b</sup> Mint\_{construct\_name} > FPL\_{construct\_name}.  
<sup>c</sup> Mint\_{construct\_name} = FPL\_{construct\_name}.  
<sup>d</sup> Based on positive ranks.

The theoretical contributions of this work are three-fold. First, as suggested by the Design and Action theory type [77], we provide guidelines for developing useful and trustworthy ontology-based, multiagent personal financial recommender systems (PFRSs), thereby extending the recommender systems' body of knowledge. These guidelines also provide an architecture for development of a mobile application for improving financial capability through financial goal setting. Additionally, we suggest/envision/propose a framework that is likely to be suitable for developing other consumer objectives-based recommendation applications that require an ontology-based, multi-agent approach; such as, health & fitness, educational or career goal setting. Further, we provide a detailed method on how to integrate ontology constructs based on a trusted model within a role-based, multi-agent recommender system architecture.

Second, this work contributes to the rigorous evaluation of the utility of the proposed artifact with human subjects. We have developed a behavioral research model to evaluate the proposed artifact from a user perspective, through the constructs of ‘Trust’ and ‘Perceived Usefulness’, and thus have extended information systems theory in the context of recommender systems. The results of our testing demonstrate that our artifact compares favorably, in terms of ‘Trust’ and ‘Perceived Usefulness’, to other available sources of financial goal recommendations, such as human financial advisors and currently available commercial FinTech applications. Empirical evidence of our design artifact clearly shows that our design successfully obtains the outcome of interest.

Table 13  
One-Sample Wilcoxon Signed Rank Test.

<table><tr><td>Construct</td><td>Null hypothesis</td><td>N</td><td>p-value</td><td>Z</td><td>Observed median</td><td>Decision</td></tr><tr><td>Trust</td><td>The median of Trust equals 3.00</td><td>97</td><td>0.000</td><td>7.199</td><td>3.667</td><td>Reject the null hypothesis</td></tr><tr><td>PU</td><td>The median of Perceived Usefulness equals 3.00</td><td>97</td><td>0.000</td><td>6.831</td><td>4.000</td><td>Reject the null hypothesis</td></tr></table>

Third, this empirical evaluation bridges the gap between design science and behavioral science. Design science and behavioral science are often viewed as distinct research paradigms. However, they can be complementary; thus, researchers should draw upon the strengths of both paradigms. This study aims to provide financial goal recommendations for a wide range of consumers with varying levels of financial capability. In doing so, this work articulates how the research methods and guidelines of both design science and behavioral research can be integrated for the development of a design artifact and the rig orous evaluation of its utility.

From a practical standpoint, a FinTech application built using the FinPathlight framework would provide useful financial goal recommendations to a wide range of consumers. Such an application would aford users specific, achievable tasks for addressing the problem of financial capability through financial goal setting. Compared to professional advisory services, an application built from the framework could provide lower- and middle-income end-users with an economical alternative to high-cost human advisors, making financial advice affordably available to a larger segment of consumers. Further, since, to the best of our knowledge, there are no current FinTech applications designed solely for the recommendation of consumer financial goals, a FinPathlight based application would fill a gap in the current FinTech landscape for systems designed specifically for the recommendation of a wide array of financial goals categorized to specific user classifications. Utilization of the framework also informs the software development process for personal recommender systems by providing communication of a structural foundation along with guidelines for selection of role-based agents and the integration of domain specific ontologies. As noted within literature on recommender systems, issues such as a familiar user-interface, detailed recommendations, user control of inputs, ease of use, and transparency of recommendation results are critical factors in user adoption. In order to maximize the potential benefits of such a recommender system framework, developers should pay close attention to addressing these issues associated with ‘Trust’ and ‘Perceived Usefulness’.

There are a number of other issues for technology-based financial applications that have not been addressed in this research, as they are outside of the scope of this particular study. For example, regulation of “robo-advice” is, at the time of this writing, still in its infancy. For an indepth treatise of potential legal and regulatory issues associated with digital financial advisory services, readers are directed to Baker and Dellaert [78]. To comply with legal and regulatory issues, the Fin-Pathlight Recommendation Agent will need to ensure the competency, honesty, and suitability of recommendation ranking and matching algorithms. Additionally, as a number of authors have noted, there are a number of moral and ethical issues associated with technological systems that should be addressed, as well with recommender systems al gorithms designed to classify users [79–81]. The FinPathlight User Profile, Learning, and Recommendation Agents should address potential bias and discrimination in user classification and recommendation. Data privacy and security concerns remain an important consideration for technologies that capture and store financial information, as well [82]. The FinPathlight Financial Data Input and Storage Agents will require methods for ensuring privacy and security of personal and financial data. Evaluations through wireframe prototypes have inherent limitations. For instance, since prototypes are not complete systems, a number of system details are not included, which may limit assessment of its full functionality. These challenges would need to be addressed in a fully-functioning, commercial application. Further, although a number of methods exists for classifying users based on their financial capability, we have not at this time addressed the issue of attribute identification and selection for user classification.

Future research will include the development of classification methods for the FinPathlight User Profile Agent to identify and select an appropriate set of attributes to accurately model the financial capability of users. To address the limitations of this study, a user classification model along with the remaining role-based agents proposed with the multi-agent architecture will be developed and evaluated through a fully functional prototype utilizing more sophisticated software methods. The experimental evaluation will be expanded to include a larger, more diverse group of financial experts from several financial institutions, along with potential users of a FinPathlight based FinTech application. However, the encouraging results of our evaluation experiment provide support and direction for future stepwise, iterative improvements to the framework. Given the favorable experimental evaluation results, future research is planned towards the development of a fully functioning prototype instantiation of a FinPathlight mobile application.

## CRediT authorship contribution statement

Lawrence Bunnell:Conceptualization, Methodology, Data curation, Formal analysis, Writing - original draft, Writing - review & editing, Validation.Kweku-Muata Osei-Bryson:Conceptualization, Methodology, Formal analysis, Writing - review & editing, Validation.Victoria Y. Yoon:Conceptualization, Methodology, Formal analysis, Writing - review & editing, Validation.

## References

[1] R. Greenwood, D. Scharfstein, The growth of modern finance, J. Econ. Perspect. 27 (2) (2013) 3–28 http://www.aeaweb.org/articles?id=10.1257/jep.27.2.3.

[2] D. Bergstresser, J.M.R. Chalmers, P. Tufano, Assessing the costs and benefits of brokers in the mutual fund industry, Rev. Financ. Stud. 22 (10) (2009) 4129–4156, https://doi.org/10.1093/rfs/hhp022.

[3] J. Chalmers, J. Reuter, Is Conflicted Investment Advice Better Than No Advice?, National Bureau of Economic Research Working Paper Series, No. 18158, https:// ssrn.com/abstract= 1785833. (2012)

[4] G.L. Foà, L. Gambacorta, L. Guiso, P.E. Mistrulli, The supply side of household finance, Rev. Financ. Stud. 32 (10) (2019) 3762–3798, https://doi.org/10.1093/rfs hhz011.

[5] P. Sullivan, “Is your financial advisor working in your best interests?” the New York times, your money, https://www.nytimes.com/2017/02/10/your-money/is-yourfinancial-adviser-acting-in-your-best-interest.html, (2017) , Accessed date: 9 June 2019.

[6] T. Philippon, The FinTech Opportunity, National Bureau of Economic Research 2016 Working Paper 22476 http://www.nber.org/papers/w22476.

[7] NFEC, Top 3 Most Missed Questions, National Financial Educators Council National Financial Literacy Test Results. https://www,financialeducatorscouncil.org national-financial-literacy-test . Accessed date: 1 January 2019

[8] FDIC, FDIC National Survey of Unbanked and Underbanked Households, Federal Deposit Insurance Corporation. 2015. https://www.fdic,goy/householdsurvey/ 2015/index,html (accessed 9 September 2019)

[9] D. Xiao, I. Benbasat, E-commerce product recommendation agents: use, characteristics, and impact, MIS O. 31 (1) (2007) 137–209, https://doi,org/10.2307/ 25148784.

[10] E. Aïmeur, K. Boudina, FIPS: A Financial Planification System by Case Based Reasoning, Proceedings of the AAAI-99, Workshop on Exploring Synergies of Knowledge Management and Case Based Reasoning, AAAI, 1999, pp. 1–5.

[11] A. Felfernig, A. Kiener, Knowledge-based interactive selling of financial service with FSAdvisor, Proceedings of the 17th Innovative Applications of Artificial Intelligence Conference (IAAI’05), 2005, pp. 1475–1482.

[12] D.G. Vico, G. Huecas, J.S. Rodrıguez, Generating context-aware recommendations using banking data in a mobile recommender system. Proceedings ICDS 2012: The Sixth International Conference on Digital Society. 2012

[13] C. Musto, G. Semeraro, P. Lops, M. de Gemmis, G. Lekkas, Personalized finance advisory through case-based recommender systems and diversification strategies, Decis. Support. Syst. 77 (2015) 100–111, https://doi.org/10.1016/j.dss.2015.06. 001.

[14] A. Fano, S.W. Kurth, Personal choice point: helping users visualize what it means to buy a BMW, IUI 03: Proceedings of the Eighth International Conference on Intelligent User Interfaces, 2003, pp. 46–52, , https://doi.org/10.1145/604045. 604057.

[15] T. Kamishima, S. Akaho, Personalized pricing recommender system: multi-stage epsilon-greedy approach. HetRec 11: Proceedings of the 2nd International Workshop on Information Heterogeneity and Fusion in Recommender Systems, 2011, pp. 57–64., https://doi.org/10.1145/2039320.2039329.

[16] M. Taghavi, K. Bakhtiyari, E. Scavino, Agent-based computational investing recommender system. RecSys 13: Proceedings of the 7th ACM Conference on

Recommender Systems, 2013, pp. 455–458, , https://doi.org/10.1145/2507157. 2508072.

[17] N. Pereira, S.L. Varma, Financial planning recommendation system using content based collaborative and demographic filtering, in: B. Panigrahi, M. Trivedi, K. Mishra, S. Tiwari, P. Singh (Eds.), Smart Innovations in Communication and Computational Sciences. Advances in Intelligent Systems and Computing, 669 Springer, Singapore, 2019, p. 2019, , https://doi.org/10.1007/978-981-10-8968- 8\_12.

[18] D. Jung, V. Domer, C. Weinhart, H. Pusmaz, Designing a robo-advisor for riskaverse, low-budget consumers, Electron. Mark. 28 (2017) 367–380, https://doi. org/10.1007/s12525-017-0279-9.

[19] R. Alt, T. Puschmann, The rise of customer-oriented banking - electronic markets are paving the way for change in the financial industry, Electron. Mark. 22 (3) (2012) 203–215 https://ssrn.com/abstract=2509134

[20] K.T. Prince, Mint by the Numbers: Which User Are You? Intuit MintLife Blog, https://blog.mint.com/credit/mint-by-the-numbers-which-user-are-you-040616/, (2016) , Accessed date: 4 March 2019.

[21] N. Lusinksi, 11 Financial Experts Reveal Their Favorite Money Apps, Business Insider. 2018. https://www.businessinsider.com/financial-experts-reveal-bestmoney-apps-2018-10 , Accessed date: 29 March 2020.

[22] R. Van Loo, Making innovation more competitive: the case of FinTech, 65 UCLA Law Review (2018) 232 https://ssrn.com/abstract=2966890.

[23] A.R. Hevner, A three cycle view of design science research, Scandinavian Journal of Information Systems Research 19 (2) (2007) 87–92.

[24] K. Pefers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A design science research methodology for information systems research, J. Manag. Inf. Syst. 23 (3) (2007) 45–78. https://doi.org/10.2753/MIS0742-1222240302.

[25] S. Gregor, D. Jones, The anatomy of a design theory, J. Assoc. Inf. Syst. 8 (5) (2007) 312–335.

[26] M.S. Sherraden, Financial capability: What is it, and how can it be created? CSD Working Papers 10–17, Washington University Center for Social Development, St Louis, 2010. , https://doi.org/10.7936/K7SX6COX

[27] CFPB, Pathways to Financial Well-being: The Role of Financial Capability, Consumer Financial Protection Bureau Research Brief, 2018, https://www. consumerfinance.gov/data-research/research-reports/pathways-financial-well being/ , Accessed date: 5 May 2019.

[28] M.J. Woolridge, An Introduction to Multiagent Systems, John Wiley and Sons, New York, 2002

[29] M. Wooldridge, N.R. Jennings, D. Kinny, The GAIA methodology for agent-oriented analysis and design, Journal of Autonomous Agents and Multi-Agent Systems 3 (2000).285–312.https://doi org/10.1023/A:1010071910869

[30] F.D. Davis, R.P. Bagozzi, P.R. Warshaw, User acceptance of computer technology: a comparison of two theoretical models, Manag. Sci. 35 (8) (1989) 982–1003, https://doi.org/10.1287/mnsc.35.8.982.

[31] Abt Associates, Understanding the pathways to financial well-being, National Financial Well-being Survey: report 2, https://www.abtassociates.com financialpathways. (2018) . Accessed date: 7 June 2019.

[32] CFPB, Financial Well-being: The Goal of Financial Education, Consumer Financial Protection Bureau, 2015, https://files.consumerfinance.gov/f/201501\_cfpb\_report financial-well-being.pdf , Accessed date: 30 August 2019.

[33] CFPB, CFPB Financial Well-being Scale: Scale Development Technical Report, Consumer Financial Protection Bureau. 2017. https://www.consumerfinance,goy data-research/research-reports/financial-well-being-technical-report/. Accessed date: 30 August 2018.

[34] A. Atkinson, S. McKay. E. Kempson, S. Collard. Levels of Financial Capability in the UK: Results of a Baseline Survey, FSA Consumer Research Paper 47, http://www. pfrc.bris.ac.uk/publications/Reports/Fincap\_baseline\_results\_06.pdf, (2006) , Accessed date: 12 June 2017.

[35] J. Serido, S. Shim, C. Tang, A developmental model of financial capability: a framework for promoting financial knowledge and skills during the transition to adulthood, Int. J. Behay. Dey, 37 (4) (2013) 287–297, https://doi.org/10.1177/ 0165025413479476.

[36] J.T. Lin, C. Bumcrot, T. Ulicny, A. Lusardi, G. Mottola, C. Kiefer, G. Walsh, Financial Capability in the United States. FINRA Investor Education Foundation 2016, http://www.usfinancialcapability.org/downloads/NFCS 2015 Report Natl Findings pdf Accessed date: 6 June 2017

[37] G.R. Motolla, C.N. Kiefer, Understanding and using data from the National Financial Capability Study, Fam. Consum. Sci. Res. J. 46 (1) (2017) 31–39, https:/ doi.org/10.1111/fcsr.12227.

[38] G.A. Gorry, M.A. Scott-Morton, A framework for management information systems, Sloan Management review, Cambridge 13 (1) (1971)

[39] H.C. Lucas, K.W. Clowes, R.B. Kaplan, Frameworks in information systems, Information Systems and Operational Research 12 (3) (1974) 245–260, https://doi. org/10.1080/03155986.1974.11731579.

[40] G. Weiss, S. Sen, Adaptation and Learning in Multi-Agent Systems, IJCAI 95: Lecture Notes in Artificial Intelligence, 1042 Springer-Verlag, Berlin, 1996, pp. 1–21.

[41] S.A. DeLoach, M.F. Wood, C.H. Sparkman, Multiagent systems engineering, The International Journal of Software Engineering and Knowledge Engineering 11 (2001) 231–258, https://doi.org/10.1142/S0218194001000542.

[42] J. Ferber, O. Gutknecht, M.M. Fabien, From agents to organizations: an organizational view of multi-agent systems. in: P. Giorgini. J.P. Müller. J Odell (Eds.). Agent-Oriented Software Engineering IV. AOSE 2003. Lecture Notes in Computer Science 2935, Springer, Berlin, Heidelberg, 2004, pp. 214–230, , https://doi.org/ 10.1007/978-3-540-24620-615

[43] H. Zhu, Role mechanisms in collaborative systems, Int. J. Prod. Res. 44 (1) (2006) 181–193, https://doi.org/10.1080/00207540500247495.

[44] H. Zhu, M.C. Zhou, Role-based collaboration and its kernel mechanisms, IEEE Trans. on Systems, Man and Cybernetics, Part C 36 (4) (2006) 578–589, https://doi. org/10.1109/TSMCC.2006.875726

[45] O. Kazik, Role-based Approaches to Development of Multi-Agent Systems: A Survey. WDS'10 Proceedings of Contributed Papers, Part I, (2010), pp. 19–24.

[46] H. Wimmer, V. Yoon, V. Sugumaran, A multi-agent system to support evidence based medicine and clinical decision making via data sharing and data privacy, Decis. Support. Syst. 88 (2016) 51–66, https://doi.org/10.1016/j.dss.2016.05.008.

[47] H. Xu, X. Zhang, R.J. Patel, Developing role-based open multi-agent software systems, International Journal of Computational Intelligence Theory and Practice 2 (1) (2007) 39–56.

[48] H. Lieberman, T. Selker, Agents for the user interface, handbook of software agents, in: J.M. Bradshaw (Ed.), Handbook of Software Agents, AAAI Press/The MIT Press, Cambridge, 2003.

[49] H.-C. Tu, J. Hsiang, An architecture and category knowledge for intelligent information retrieval agents, Decis. Support. Syst. 28 (2000) 255–268, https://doi. org/10.1109/HICSS.1998.655297.

[50] H. Zhang, R. Kishore, R. Sharman, R. Ramesh, Agile Integration Modeling Language (AIML): a conceptual modeling grammar for agile integrative business information systems, Decis. Support. Syst. 44 (1) (2007) 266–284, https://doi.org/10.1016/j. dss,2007.04.009

[51] M. Kaminskas, D. Bridge, Diversity, serendipity, novelty, and coverage: a survey and empirical analysis of beyond-accuracy objectives in recommender systems, ACM Transactions on Interactive Intelligent Systems (TiiS) 7 (1) (2017) 1–42, https://doi.org/10.1145/2926720.

[52] N. Tintarey, J. Masthoff, Survey of explanations in recommender systems, IEEE 23rd International Conference on Data Engineering Workshop, Istanbul, 2007, 2007, pp. 801–810, , https://doi.org/10.1109/ICDEW.2007.4401070.

[53] A.P. Peña-Ayala, Ontology agents and their applications in the web-based education systems: towards an adaptive and intelligent service, in: N.T. Nguyen, L.C. Jain (Eds.), Intelligent Agents in the Evolution of Web and Applications, Studies in Computational Intelligence 167, Springer, Berlin, Heidelberg, 2009, , https://doi. org/10.1007/978-3-540-88071-4\_11.

[54] S.-Y. Yang, Developing of an ontological interface agent with template-based lin guistic processing technique for FAQ services, Expert Syst. Appl. 36 (2–2) (2009) 4049–4060, https://doi.org/10.1016/j.eswa.2008.03.011.

[55] V. Codina, L. Ceccaroni, Taking advantage of semantics in recommendation systems, in: R. Alquezar, A. Moreno, J. Aguilar (Eds.). Proceedings of the 13th International Conference of the Catalan Association for Artificial Intelligence. CCIA 2010, IOS Press, Espluga de Francolí, Catalunya, 2010, pp. 163–172, , https://doi. org/10.3233/978-1-60750-643-0-163.

[56] Y. Wand, R. Weber, Toward a theory of the deep structure of information systems, Proceedings 3: ICIS, 1990 https://aisel.aisnet.org/icis1990/3.

[57] L. Bunnell, K.-.M. Osei-Bryson, V.Y. Yoon, Development of an Ontology of Consumer Financial Goals Designed for Improving Financial Capability. Submission, Working Paper, Consumer Financial Goals Ontology, 2019 available online http://www.finpathlight.com/Ontologies/index.html

[58] N. Dalkey, O. Helmer, An experimental application of the Delphi method to the use of experts, Manag. Sci. (3) (1963) 458–467, https://doi.org/10.1287/mnsc.9.3.458.

[59] C.-C. Hsu, B.A. Sandford, The Delphi technique: making sense of consensus, Pract. Assess, Res, Eval. 12 (10) (2007). http://pareonline,net/pdf/v12n10.pdf , Accessed date: 12 January 2019.

[60] W. Hui, S.M. Lui, W.K. Lau, A reporting guideline for IS survey research. Decis Support. Syst. 126 (2019) 113–136, https://doi.org/10.1016/j.dss.2019.113136.

[61] S.T. March, G.F. Smith, Design & natural science research on information technology, Decis. Support. Syst. 15 (1995) 251–266, https://doi.org/10.1016/0167- 9236(94)00041-2.

[62] K. Peffers, M. Rothenberger, T. Tuunanen, R. Vaezi, Design science research evaluation, in: K. Peffers, M. Rothenberger. B. Kuechler (Eds.). Design Science Research in Information Systems. Advances in Theory and Practice, DESRIST 2012, Lecture Notes in Computer Science, 7286 Springer, Berlin Heidelberg, 2012 pp 398–410

[63] Y.-K. Lim, A. Pangam, S.A. Perivasami, Comparative analysis of high- and low-fi. delity prototypes for more valid usability evaluations of mobile devices, Proceedings of the 4th Nordic Conference on Human-Computer Interaction, 2006, pp. 291–300, , https://doi.org/10.1145/1182475.1182506.

[64] T.R. Silva, J.-L. Hak, M. Winckler, O. Nicolas, A comparative study of milestones for featuring GUI prototyping tools, J. Softw. Eng. Appl. 10 (6) (2017) 564–589.

[65] K.-C. Hamborg, J. Hulsmann, K. Kaspar, The interplay between usability and aesthetics: more evidence for the “what is usable is beautiful” notion, Advances in Human-Computer Interaction, Hindawi, 2014, , https://doi.org/10.1155/2014/ 946239 Article 15.

[66] H. Wimmer, V. Yoon, Counterfeit product detection: bridging the gap between design science and behavioral science in information systems research, Decis. Support. Syst. 104 (2017) 1–12, https://doi.org/10.1016/j.dss.2017.09.005.

[67] Adobe, Adobe XD Release Notes. Adobe Inc., https://helpx.adobe.com/xd/releasenotes. html. (accessed September 9. 2019)

[68] S.Y.K. Komiak, I. Benbasat, The efects of personalization and familiarity on trust and adoption of recommendation agents, MIS Q. 30 (4) (2006) 941–960, https:// doi.org/10.2307/25148760.

[69] P. Pu, L. Chen, R. Hu, A user-centric evaluation framework for recommender systems. Proceedings of the fifth ACM conference on Recommender systems (2010) 157–164. https://doi.org/10.1145/2043932,2043962

[7o] S. Siegel, Nonparametric Statistics for the Behavioral Sciences, McGraw-Hill, New York, NY, 1956.

[71] G.E. Meek, C. Ozgur, K. Dunning, Comparison of the t vs. Wilcoxon Signed-Rank Test for Likert scale data and small samples, J. Mod. Appl. Stat. Methods 6 (1)

(2007) 90–106, https://doi.org/10.22237/jmasm/1177992540.

[72] D. Doane, L. Seward, Applied Statistics in Business and Economics, McGraw-Hill Irwin, New York, 2007.

[73] J.F. Hair Jr., W.C. Black, B.J. Babin, R.E. Anderson, Multivariate Data Analysis, 7th edition, Prentice Hall, Upper Saddle River, NJ, 2009.

[74] J. Sauro, J.R. Lewis, Quantifying the User Experience, 2nd edition, Morgan Kaufman, Boston, MA, 2016.

[75] A. Field, Discovering Statistics Using IBM SPSS, Sage Publications, Los Angeles, 2013.

[76] A. Eneriz, Can you aford a financial advisor, Investopedia, 2016, http://www. investopedia.com/articles/personal-finance/021216/can-you-aford-financialadvisor.asp, (2016) , Accessed date: 28 March 2017.

[77] S. Gregor, The nature of theory in information systems, MIS Q. 30 (3) (2006) 611–642.

[78] T. Baker, B.G.C. Dellaert, Regulating Robo Advice Across the Financial Services Industry, Faculty Scholarship, 2018, p. 1740 http://scholarship.law.upenn.edu/ faculty\_scholarship/1740 , Accessed date: 5 September 2019.

[79] W. Wallach, C. Allen, Moral Machines: Teaching Robots Right from Wrong, Oxford University Press. 2009. https://www.oxfordscholarship.com/view/10.1093/ acprof:oso/9780195374049.001.0001/acprof-9780195374049 , Accessed date: 23 August 2019.

[80] S. Barocas, A.D. Selbst, Big Data's disparate impact, 104 California Law Review 671 (2016), https://doi.org/10.2139/ssrn.2477899.

[81] K. Crawford, Artificial Intelligence’s White Guy Problem, N.Y. Times, 2016, http:/ www.nytimes.com/2016/06/26/opinion/sundav/artificial-intelligences-whiteguv-problem.html , Accessed date: 23 August 2019.

[82] R. Swedlof, Risk classification's Big Data (R)evolution, Connecticut Insurance Law Journal 21 (2014), https://ssrn.com/abstract=2566594.

Lawrence Bunnell holds a PhD in Information Systems as well as a Master of Science in Information Systems and MBA from Virginia Commonwealth University. He is currently working as a business intelligence and data analytics executive within the financial services industry. As part of his PhD work, he developed a framework as part of a design science research for an ontology-based, multiagent, hybrid-methods recommender sys tems FinTech application designed to increase consumer financial capability. His current research focus is on knowledge classification, data analytics and machine learning. Professional experience includes data analytics high-level code development and data visualizations, as well as having directed digital development and marketing strategy for several fast growth and start-up e-commerce companies. He can be reached at bunnelll@ vcu.edu.

Kweku-Muata Osei-Bryson is Professor of Information Systems at Virginia Commonwealth University in Richmond. VA. He is also currently a Visiting Professor of Computing at the University of the West Indies at Mona, and has also been Visiting Professor of Information Systems at the Ghana Institute of Management & Public Administration. Previously he was Professor of Information Systems & Decision Sciences at Howard University in Washington, DC. He has also worked as an Information Systems practitioner in industry and government in the USA and Jamaica. He holds a Ph.D. in Applied Mathematics (Management Science & Information Systems) from the University of Maryland at College Park; a M.S. in Systems Engineering from Howard University; and a B.Sc. in Natural Sciences from the University of the West Indies at Mona.

His research areas include: Analytics & Data Science, Knowledge Management, Expert & Decision Support Systems, ICT for Development, Cyber-Security, e-Commerce, and Multi-Criteria Decision Making. His research has been published in various leading research journals, and he is author or editor of 5 books. Currently he serves as a Senior Editor of Information Technology for Development, an Associate Editor of the European Journal of Information Systems, a member of the Editorial Board of Computers & Operations Research, and a member of the International Advisory Board of the Journal of the Operational Research Society.

Victoria Y. Yoon is Professor in the Department of Information Systems at Virginia Commonwealth University (VCU). She received her M.S. from the University of Pittsburgh and her Ph.D. from the University of Texas at Arlington. Her primary research interests have been in the application of Artificial Intelligence (AI) to support the complex decision- making process and the managerial issues of such technology. She has published in MIS Quarterly, Decision Support Systems, Communications of the ACM, Journal of Management Information Systems, Journal of Operation Research Society, and other journals. She is the recipient of the VCU School of Business 2016 Faculty Award of Excellence. In 2018 she is named as a Dean's Scholar Professor at the VCU School of Business. She is a senior editor of Decision Support Systems.
