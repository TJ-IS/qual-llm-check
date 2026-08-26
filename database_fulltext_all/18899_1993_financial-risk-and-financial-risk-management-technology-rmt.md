---
otero_id: 18899
otero_key: "J5VCY7CG"
title: "Financial risk and financial risk management technology (RMT)"
authors: "Arun Bansal; Robert J. Kauffman; Robert M. Mark; Edward Peters"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90004-d"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Applications

# Financial risk and financial Risk Management Technology (RMT) \*

# Issues and advances

Arun Bansal

Bear Stearns & Co., Inc., New York, NY, USA

Robert J. Kauffman

Stern School of Business, New York, NY, USA

Robert M. Mark

Chemical Banking Corporation, New York, NY, USA

Edward Peters

The HAY Group Inc., Washington, DC, USA

Methods for sound risk management are of increasing interest among Wall Street investment banking and brokerage firms in the aftermath of the October 1987 crash of the stock market. As the knowledge of advanced technology applications in risk management increases, financial firms are finding innovative ways to use them practically, in order to insulate themselves. The recent development in models, the software and hardware, and the market data to track risk are all considered advances in Risk Management Technology (RMT). These advances have affected all three stages of risk management: the identification, the measurement, and the formulation of strategies to control financial risk. This article discusses the advances made in five areas of RMT: communication software, object-oriented programming, parallel processing, neural nets and artificial intelligence. Systems based on

Correspondence to: Arun Bansal, Information Services, Bear Stearns & Co., Inc., 245 Park Avenue, New York, NY 10167, USA.

any of these areas may be used to add value to the business of a firm. A business value linkage analysis shows how the utility of advanced systems can be measured to justify their costs.

Keywords: Risk management; Object-oriented; Neural nets; Artificial intelligence; Business value; Clientserver; Distributed database; Parallel processing; Pattern recognition; Data quality

## 1. Introduction

Over the last ten years, major securities firms, money center banks and other commercial and

![](/api/attachments/J5VCY7CG/fulltext/images/38716fc8dd11f4312554d1c0f32661fa7814238de3309497dba547c04f89496f.jpg)

Arun Bansal is completing his Ph.D. in IS at the Stern School of Business, New York University. He is currently working as an analyst at Bear, Stearns and Company, Inc. in New York City. Mr. Bansal held a visiting position at the University of Connecticut, Storrs for one year. He recently completed a multi-year research project on information technology applied to financial risk management in the Capital Markets Sector of Manufacturers Hanover Trust Company. His research interests include information economics, data quality analysis and control, and the application of neural nets and artificial intelligence models in financial forecasting.

![](/api/attachments/J5VCY7CG/fulltext/images/a721c3b79ade97db6dede94e2c290de821e949232b935fd512c3bb3b6f0fa4a5.jpg)

Robert J. Kauffman is Associate Professor of IS at the Stern School of Business, New York University. Prior to pursuing a Ph.D. at the Graduate School of Industrial Administration, Carnegie Mellon University, he was an international lending officer at a large money center bank in New York. His research focuses on developing new methods for measuring the business value of information technology, using techniques from finance and economics. He has published articles

in MISQ, JMIS, IEEE Transactions on Software Engineering, and elsewhere, and recently edited a refereed research volume entitled Perspectives on the Strategic and Economic Value of IT Investment (Idea Group Publishing, Middletown, Pennsylvania, 1992).

\* The authors would like to thank the editor and reviewers for their helpful suggestions. They also thank Brian Fitzpatrick, Joonkee Hong, Jonathan Lomartire, Bruce Hannan for generously sharing their time and knowledge of risk management in the investment banking industry. Finally, the authors appreciated valuable advice from Ted Stohr, Bruce Weber and Rob Weitz on various aspects of this project.

savings banks have undertaken financial commitments involving risks they did not fully understand, resulting in major losses and unexpected write offs. As a result, senior managers are seeking new ways to identify, evaluate, and predict changes in financial risks. Investing in information technologies (IT's) that improve the control of risk – a new area which we term risk management technology (RMT) – is one approach that is increasingly viewed as being able to affect the strategic and competitive position of financial firms.

In 1990 a joint project was initiated between the Stem School of Business, New York University and Manufacturers Hanover Trust Company (now known as Chemical Banking Corporation) in New York City to study the use of RMT in financial firms in the United States. The present article summarizes our findings and suggests a number of ways in which the use of RMT can be made efficient.

![](/api/attachments/J5VCY7CG/fulltext/images/6aa5200defcf26916c752b9dae4a85c0f3a9a634c4b46cfea8bb670772ace34a.jpg)

Bob Mark is a managing director in the Asia, Europe, Capital Markets and Treasury (AECM & T) group and teaches as an adjunct professor at the Stern School of Business. New York University. His responsibilities within AECM encompass risk management research (quantitative analysis), planning and business analysis. He joined the bank in November 1988. He is also a chairperson of the National Asset Liability Management Association. He holds a Ph.D. from the

Graduate School of Engineering and Science, New York University. He subsequently received an Advanced Professional Certificate in Accounting from New York University also. Prior to his current position, he was a senior officer at Marine Midland Bank/Hong Kong Shanghai Bank group where he headed the technical analysis group within the Capital Markets sector. Earlier, he was a Director of a systems profit center at American Express, USA.

![](/api/attachments/J5VCY7CG/fulltext/images/83be3439c6db1d6d98284dbd6d0526ca1a9e0ddc9e85856e4cd011ca0caa6541.jpg)

Edward Peters is Vice President, Information Technology for the Hay Group, Inc., Washington, DC. He is responsible for the management and application of information technologies relating to Hay's worldwide business needs. Prior to joining Hay, Mr. Peters was Vice President, Strategic Technology and Research at Manufacturers Hanover Trust, New York, NY. He was also the Chairman of the ADJP, an international task force of IBM customers that defined the product specifications for AD/Cycle. He has also held various academic appointments, most recently as Visiting Lecturer in Informatics at Katholieke Universiteit, Leuven, Belgium. Mr. Peters holds a B.A. and an M.S.I.E. from Lehigh University and is a Ph.D. candidate at the Universiteit van Amsterdam. His current research interests focus on use of information technology and its relationship to organizational effectiveness.

## 1.1. Financial risk management

Risk is defined by Doherty [13] as 'the lack of predictability of outcomes.' It covers both pleasant surprises and adverse business outcomes. Since prediction is facilitated by the availability of information, RMT can be used to gauge risk in financial operations, where the outcomes of regional lending operations, involvement in selected financial markets and instruments and positions taken by traders are uncertain and may change from day to day. Risk management, on the other hand, is the management of the resources and commitments of a firm so as to maximize its value, taking into account the impact that unpredictable outcomes or events can have.

Risk management activities normally involve three basic steps:

(1) exhaustive identification and classification of the risks that can impact business outcomes;

(2) measurement of the risk associated with a set of events that affect the value of the firm, in terms of the likelihood of their occurrence and magnitude of expected losses;

(3) timely formulation of the actions required to bring business risks within acceptable bounds.

The sources of risk are varied and depend on the business area. For example, a financial firm involved in trading financial instruments will face a market risk associated with unpredictable price changes. Interest rate risk arises from interest rate fluctuations that render the return on financial assets uncertain. This also poses significant financial uncertainty when there are gaps in value between the set of claims made on a firm's assets and the assets' value when the claims are due. With a substantial gap between these values, it may become necessary for the firm to purchase funds at an unexpectedly high cost. Exchange rate risk arises from fluctuations in the value of foreign currency. Credit risk is associated with defaults in repayment of loans and operating risk stems from frequent changes in or discontinuance of a revenue stream against a continuing level of fixed cost expenditures.

Being able to obtain accurate, up-to-date information is crucial in such contexts. For example, interest rate risk is normally measured by identifying fluctuations in interest rates and the manner in which such changes influence asset values, and market risk is measured by tracking the volatilities (i.e., overnight price changes in an asset's value) of financial instruments and currencies. Examination of such data enables the loss or gain in a portfolio to be measured quite objectively. Timely and accurate information about interest rate fluctuations enables risk managers to gauge the risks of maintaining funding gaps. Because senior managers usually draw the line on the maximum risk of the firm, risk managers and operations managers have similar incentives to use RMT to eliminate excess risk.

## 1.2. The role of information technology in risk management

Information technology has been used pervasively to automate trading activities. Systems that report information about market conditions and market changes, such as Merrill Lynch – Bloomberg for the fixed income market, are also being used to assist traders and portfolio managers. Although a variety of traditional ITs and approaches, including mainframe databases and non-automated tracking of basic market indicators, are still in use, there has been a major move on the part of Wall Street firms towards more sophisticated, state-of-the-art technologies, such as parallel processing, artificial intelligence, and neural nets. These ITs are being used by major investment banks to gain competitive advantage in strategic cost management.

There also has been substantial growth in the availability of highly specialized commercial databases, including those from firms such as Reuters/I.P. Sharp and Loanet, that support the tracking of securitized lending portfolios. Apart from supporting the routine activities, commercial databases and computerized financial modeling systems help a trader to manage a portfolio and ward off excess risk by the implementation of hedging strategies that neutralize risk. For example, mortgage loans can be securitized on the basis of the risk involved in their prepayment and their expected return. These mortgage-backed securities can then be freely traded in the market.

At the heart of these developments is the realization that IT is crucial in defining the basis of a set of new approaches to conducting money market trading operations. Engineering new financial products that possess attractive risk characteristics for the parties in a transaction, as well as the intermediaries to the transaction, is only limited by willingness of the firm to explore the capabilities of the technologies that support such innovations. Another aspect is the growth in the ability to manage risks associated with global investments on a real-time basis from a centralized location.

## 2. Information technology applied to risk management problems

RMT has three primary components:

(1) analytic models implemented using computer software;

(2) computer hardware for capturing, consolidating, and evaluation new information about changing risk; and

(3) data describing the current and prior states of the market.

## 2.1. Identification of risky events

Many organizations today use IT to detect events that can increase their exposure to market risk in their investments. For example, databases of financial information are used to detect changing risks in investment positions. A key element is early identification of crucial changes that will affect this business. This is often accomplished with the help of trading platform automation that pulls in digital signals on market indicators, and then scans them to determine if they change the risk profile of current or contemplated investments [24].

For investment in specific financial instruments, most investment banks today use risk calculators for financial instruments, such as treasury bonds, mortgage-backed securities, and options and foreign exchange (FX) trading. Most of them have a simple spreadsheet-type format for carrying out sensitivity analysis, however, a few are more sophisticated. In-house consulting groups in major investment banking institutions also produce highly specialized tools to discern variation in risk associated with specific financial instruments. For example, the Strategic Technology and Research Group of Manufacturers Hanover Trust was instrumental in the design and development of an expert system (ES) called Trading and Risk Assistant (TARA) that identified risky transactions in the FX market. Another expert system, developed at Morgan Stanley, is called the GNMA Trading Assistant [19], a rule-based ES that helps traders identify risks associated with mortgage-backed securities.

## 2.2. Categorizing and measuring financial risk

Well-defined measures of financial risk are important to allow senior management to devise strategies to monitor and evaluate risk. Such measures will enable them to make policies to help departmental traders, operating divisions and the firm as a whole to keep within the acceptable, pre-determined limits. The first step is to develop an understanding of the factors that affect risk (for example, the historical prices of the financial instruments for market risk, and the probability of default for credit risk). Next, the range of fluctuations from their mean values and the overnight price volatility can be calculated. The measurement of volatility determines the riskiness of the financial instrument during the period of observation.

Credit risk is generally measured by tracking information on the credit quality of the parties involved in a credit transaction. This requires the firm to establish a consistent measure of credit exposure as a common denominator. For this purpose, all balance sheet items (notes receivable, terms loans and so on), off-balance sheet items (e.g., standby letters of credit or pending legal commitments), and interest rate and exchange rate contracts (foreign exchange spot and forward trades, interest rate and currency swaps) are converted into a loan equivalent exposure amount. An equity factor is then assigned to each grade of credit risk. This is used to adjust balance sheet and off-balance sheet exposure to yield equity at risk.

IT plays an important role in this measurement. Banks usually subscribe to real-time databases that supply information on the credit quality of corporations. The advantage of a real-time system for monitoring credits is that credit quality updates are instantly available. For example, Manufacturers Hanover Trust employed a Global Exposure System (GES) that tracks the equity factors assigned to each grade of credit risk, and provides updated risk calculations.

Market risk is measured by the fluctuation in prices of instruments due to underlying change in the market. Adverse movements in FX rates, interest rates, and the extent of the volatility of price of financial instruments are the most common determinants of market risk. FX positions are exposed to movements in exchange and interest rates. Measurement of interest rates fluctuations is important to match the cash flows associated with assets and liabilities that are expected to become due at some future date.

For example, suppose a one-year working capital loan is created against a one-month certificate of deposit of similar amount. In this situation, eleven months of additional funding must be generated to match the asset the firm will carry until the expiration of the liability in the twelfth month. The value to the firm of the one-year loan would decrease (or increase) at the end of the first month if the interest rates are higher (lower), forcing (enabling) the firm to purchase relatively more (less) expensive funds from certificates of deposit or in the form of overnight U.S. Federal Reserve Bank funds. Clearly, prevailing interest rates would determine whether the firm is profitable in this kind of lending.

The set of activities involved in ensuring that risk is controlled in such circumstances is called gap management. It involves devising strategies and tactics to deal with interest rate risk so that cash flows representing both assets and liabilities are matched. Effective gap management enables a financial institution to protect itself from unexpected and costly borrowing when assets exceed liabilities at some point in time, or eliminates the need for seeking investment opportunities from excess cash balances that arise when liabilities exceed assets.

Operating risk is measured by two factors: the scale of operations and the flexibility with which the current investments in an operating unit can be used elsewhere if the unit is shut down. IT assists measurement of operating risk by providing advanced applications of database management systems that can gauge the flexibility with which resources can be reallocated within a firm, if reorganization should occur.

## 2.3. Formulation of strategies to control risk

Once the risks have been measured correctly, they can be compared using common units. A recent proposal, espoused by Mark [23], recommends that risk be measured in dollars at risk. This indicates the amount of money at risk in a transaction, based on its face value and the probability of the occurrence of a loss. So, for example, if an investment of \$1 million is exposed to a 1% risk of loss, then \$10,000 is the expected value of dollars at risk.

Most financial instruments exhibit variation in value with change in the factors that affect risk. So, it is possible to combine investments in multiple instruments in such a way that the losses due to adverse changes in risk factors can be set against the gains due to favorable changes. This strategy is widely known as hedging and the combination of investments selected for this purpose is called a portfolio. Typically, the objective is to keep overall exposure within certain predetermined risk limits while maximizing expected returns.

IT plays an important role in the creation of efficient hedges. By definition, efficient hedges are those that produce maximum returns on investment for some specified level of risk $[31]$ . Although the ratio of investments in different financial instruments can be varied to produce several different portfolios, only a few will be used in efficient hedges. To create efficient hedges, the correlations between prices of each instrument in a portfolio must be calculated, and this is normally done through statistical analysis of large financial databases. Common factors that affect risk of multiple financial instruments must also be determined through statistical analysis. The power of IT in this application is to sample the permutations and combinations of instruments to provide new and hybrid hedges that were not easily found with manual analysis.

## 3. Technological improvements in risk management

The potential benefits of risk management activities conducted by investment banking and brokerage firms are increasing due to continuing developments in the market for new IT s. We consider five of the most important ones:

\- communication software;

\- object-oriented programming and distributed programming;

\- parallel processing and supercomputing;

\- artificial intelligence; and

\- neural nets.

These ITs have been of significant interest to the major accounting firms dealing with risk management in financial auditing [26,18].

## 3.1. Communication software advances

Attempting to calculate and manage risk on a global basis requires centralized control of algorithms and immediate access to large amounts of data, both historical statistics and current risk characteristics for each instrument in every portfolio kept by a trading unit of the institution. The problem increases in complexity when one considers that the trading units may be dispersed among markets in multiple time zones. Centralizing risk calculation and providing immediate access to data means that an organization must develop an enabling architecture made up of database and communication technologies. The two main technological approaches are client-server architectures and distributed databases.

In a client-server architecture, workstations are linked together via a local area network (LAN) with one workstation acting as the database handler (server) for other workstations that request and process information (clients). In this manner, a group of traders can access risk calculations sent to the local network from a centralized mainframe controlled by the headquarters' risk management group. All data necessary for local risk calculation and processing can be staged on the server with "end-of-day" calculations being sent back to the central mainframe. In implementing this approach to “passing the book” as each office closes, an organization can review “end-of-day” risk calculations from each overseas trading office, review the overall dollars at risk, make adjustments to the risk calculation algorithms (if required), and send the new requirements to each node (server) in the system for use beginning on the next trading day (see Figure 1). This would allow a form of centralized control with distributed decisionmaking facilitated via the communications technology.

![](/api/attachments/J5VCY7CG/fulltext/images/0c308bc60e0a3f36dc52f7948fc5d8062850630735d60afbfcbb610b214cca48.jpg)  
Fig. 1. Client-server architecture.

Distributed databases also promote distribution of data and decisionmaking to regional sites, yet take a different technological approach (see Figure 2). Whereas client-server architectures allow users at workstations to see remote access as local access to a single database, distributed databases allow concurrent access to two or more remote databases. This enables an organization to store data on the network wherever it is most economical. It also avoids having to stage the data at each remote database server, which is the case in client-server architectures. Thus an overseas office can request information on any financial instrument from other sites and need not know about all global portfolios that the firm maintains. This location transparency enables an organization to adopt a low cost solution to providing data for risk decisionmaking.

We recently have seen an application of these concepts at work at the First Boston Corporation, a large investment bank in New York City [3]. In the late 1980s, the firm invested in computer aided software engineering (CASE) technology to defray the long-term costs of creating a new architecture of trading and investment banking software applications. The architecture provided distributed processing among large IBM mainframes, fault-tolerant minicomputers and high-end workstations running Microsoft Windows and specialized software to support trading. A key enabling technology was called “middleware,” a set of ready-to-use software routines that could be used to develop complex communication capabilities in a trading system at a low cost.

![](/api/attachments/J5VCY7CG/fulltext/images/ce764465eb178278d6a5d00757cd736087a9c587e518eb2d4e5e39f9baf261dd.jpg)  
Fig. 2. Distributed database technology with interconnected servers.

This architecture also delivered “economic MIPs”, by ensuring that the appropriate processes were run on the appropriate computer resources across the three processing levels. By distributing the databases that supported trading decisions, a trader would be able to work with a “high functionality” workstation that delivered the combined power of the firm’s entire computer architecture. This allowed workstation graphics, models and databases; digital feeds from a minicomputer to update current prices; and mainframe-based mathematical models and databases to be available to a trader up to the second, to support profitable trading.

## 3.2. Object-oriented databases and programming systems

Object-oriented programming languages, such as C++, are rapidly gaining acceptance for software development in the financial world. An object is defined as an entity that encapsulates some private state information or data, with a set of associated operations or procedures that manipulate the data. For example, generic financial instruments such as options, bonds, and stocks can all be classified as objects. Object-oriented programming languages use the concept of class and instance. A class is a template from which objects may be created. Every object is an instance of some class, and a group of objects that have the same set of operations and the same state representations are considered to be of the same class. Inheritance is a mechanism that allows new classes to be derived (called subclasses or derived classes) from existing ones when the two classes share a set of common properties. For example, each of the two types of options, American and European, can be constructed as derived classes from the class “option”. As a result, each of them will inherit some common properties from the class. The class from which another class is derived is called a superclass for the derived class. For example, the class “options will be a superclass for the class “American Option”. A database is object-oriented if it supports objects and the mechanism of inheritance between objects [9]. To communicate with other objects, an object sends messages to them. Upon receiving a message, the receiver checks to see if the request can be satisfied by using information available within it. If not, the request is forwarded to others that may be able to provide the information.

Different financial instruments fall naturally into different classes: fixed income investments, options, futures, FX, etc. Under each of these classes, several subclasses may be specified. For example, fixed income investments may further be categorized into the subclasses “bonds” and “mortgages.” And, each class and subclass can have several instances, which will be the names of actual financial instruments. Thus, a “5% coupon Government National Mortgage Association (GNMA) instrument” will be an instance of a mortgage instrument. Another example is bond and mortgages. Both exist for a certain period of time called their “time to maturity”. It helps in the calculation of profitability from investments in these financial instruments. Thus, the formula to determine whether an investment in bonds or mortgages is profitable can be put in the “fixed income instruments” class and inherited by the subclasses, “bonds” and “mortgages.” Messages can be passed from one object to another to gather information pertaining to the current investments in a firm’s portfolio. In fact, information that frequently changes, such as FX rates and interest rates, can be combined to form a separate object with the other objects sending messages to it object if they need updated information.

The nature of risk of investment in a financial instrument changes with its type. For example, while investments in options usually face market risk, an investment in treasury bonds bears interest rate risk. With the development of an object-oriented system, financial instruments bearing the same type of risk can be easily grouped under one class to make it convenient for a portfolio manager to identify alternative investments that reduce a particular risk. With the addition of an inheritance mechanism, modifications to any class of instruments will only be needed in one place.

Another application area for object-oriented systems in the future may be that of distributed databases. Invalid or corrupt data is a very serious problem that portfolio managers face in global portfolios, since the data are gathered from all around the world. Using distributed object-oriented databases, a class of portfolios and inherited classes of individual financial instruments can be created at a centralized location. This ensures that data for individual financial instruments and the corresponding operations permitted on the instruments are consistent with permissible operations on the firm's portfolio, an important factor when data can be provided at any of several remote offices of a financial institution. One remote office can usually provide updated information on several financial instruments. With the help of a distributed object-oriented system, the updated objects can be shipped to a centralized location, thereby automatically detecting data inconsistencies by checking to see if the transmitted objects exhibit undesirable properties (see Figure 3 and Table 1). The system can be used to hide sensitive information by making a limited number of required objects accessible only at specific locations within the firm.

Among the other advantages of a distributed object-oriented system is better robustness in case of a local hardware failure. Since each node has the responsibility of updating only a part of the system, the failure of a single node restricts the loss to only a few objects and not the complete system. In this case, when the node is restored, the affected objects are updated locally and the entire database is then updated. Failure of local hardware is not uncommon in the foreign operations of large financial institutions. For global risk management, local offices can be asked to maintain only those financial instruments that originate in their markets. Every time an object instance – a financial instrument in this case – is updated by the local office, the updated information can be passed to a centralized location and checked for errors there. This updated information on the object can be passed to other offices that require it. In case of a local failure, only some of the information will be lost. If the node went down after the message was sent out to update remote locations, it can be easily recovered by contacting either the centralized location or other locations where the most recent information is available. However, if the node went down before the message was sent, local update of the affected objects will have to done.

Table 1  
![](/api/attachments/J5VCY7CG/fulltext/images/48435b8d12356f9af8ab0f8873926d2f8a2439d9e40fa22cb816099916c233ff.jpg)  
Fig. 3. An example of a distributed object-oriented database.

3.3. Optimization and parallel processing for financial risk management

During the 1970s, significant progress was made on developing sophisticated management science models to solve a variety of financial problems, including asset and liability matching, cash flow and position forecasting, float optimization, etc. Many industry observers, however, have argued that the application of such models to real problems in large financial firms – especially where uncertainty about cash flows and interest rates was involved – required a level of computing power that had not yet become widely available.

Today, the situation has changed. Computing power has increased by several orders of magnitude and is now readily available in the form of 486-PCs and RISC-based (reduced instruction set computing) engineering workstations. In addition, parallel processing and supercomputing capabilities have fundamentally changed the scope of the models that can be solved. As Stavros Zenios, director of the HERMES Laboratory for Financial Modeling and Simulation at the Wharton School has pointed out: "Financial optimization in the 1990s promises to be an area of applications comparable to the use of management science models in logistics, transportation and manufacturing" [33].

The use of mathematical programming is a logical choice: it enables the analyst to “optimize” the risk profile associated with a portfolio. Mathematical programming also enables the analyst to represent institutional requirements or limitations placed on investors and their portfolios. Finally, it provides a ready mechanism to formulate a clear objective function for financial risk management, to identify the set of financial instruments m which portfolio selection occurs, and to carry out structured analysis of the relationship between risk and reward.

Characteristics of the superclass and the derived classes in the example shown in Figure 3.

<table><tr><td colspan="2">Property</td><td>Superclass</td><td>Derived class</td></tr><tr><td rowspan="2">Inheritance</td><td>Operations</td><td>Buy/Sell operations permitted to be inherited. Operations on non-local financial instruments not permitted to be inherited for modifications.</td><td>Buy/Sell inherited from the class.</td></tr><tr><td>Properties</td><td>Correlation among instruments permitted to be inherited.</td><td>Price correlation inherited.</td></tr><tr><td>Private operations</td><td></td><td>Portfolio risk and reward calculations.Range-checks for portfolio risk.</td><td>Country-specific risk calculations.Error-checks for specific financial indicators.</td></tr><tr><td>Private properties</td><td></td><td>Portfolio specific properties, such as the upper limit on portfolio risk and the type of portfolio: short-term or long-term.</td><td>Individual instrument properties, such as maturity, coupon and volatility.</td></tr></table>

Such techniques have been successfully applied to a wide variety of financial optimization problems involving risk. These include:

\- bond portfolio immunization [6,15,16,29];

\- bond “factor” immunization (which alters the assumption in bond portfolio immunization that the term structure of interest rates is flat and shifts in parallel);

\- bond dedication modeling (which alters immunization models to match cash flows “on average” [34];

\- downside risk control in option positions;

\- Markowitz models representing the mean and variance of non-systematic risk in portfolios [17,25]; and,

\- multi-period stochastic planning models involving uncertainty [7,11,20,28].

Areas that have especially benefitted from major advances in risk management include mortgage-backed securities (MBS) and their derivatives, collateralized mortgage obligations (CMO), and other financial instruments that are highly sensitive to interest rates and that involve many cash flows over time. Portfolios can be built well on analysis of the instruments only if the analysis can be carried out in real-time, prior to the expiration of the opportunity or changes in the underlying conditions of the market. Mortgage-backed security portfolio risk management involves modeling mortgage holder behavior as a call option (since a mortgage holder can select to prepay if interest rates drop substantially). The financial optimization problem is to determine what securities to include in an MBS pool with a selected risk profile, and the related lending and borrowing decisions associated with MBS cash flows that either lead or lag the expected cash flow schedule at the time the portfolio was created. Zenios [33] reports on the use of a Thinking Machines Inc. "Connection Machine CM-2" parallel computing architecture (32,000 processing elements) that takes advantage of recent advances in algorithms for stochastic programming to solve this problem in real-time. In this case, computing power not only supports a business, it enables it.

3.4. Artificial intelligence (AI) and the recognition of patterns associated with risk

While the majority of corporate information processing expenditures are in the area of traditional information systems, some organizations have begun to develop expert systems. This technology goes beyond the normal approach of collecting, storing and retrieving data to one of defining human decisionmaking rules (or expertise) and storing them with the data. These systems tend to act as an aid to decision making through the use of stored “knowledge resources rather than attempt to replace humans with computer automation [30].

Expert systems can be classified as to use of knowledge and technological complexity. An expert systems rises on the scale of knowledge complexity as the number of different fields of information required in the decision analysis increases or as the uncertainty of the information, or its completeness, increases. Similarly, an expert system is considered technologically complex if the diversity of platforms (hardware and system software) used for implementing the system is high (see Figure 4). A PC-based personal time management program written using an AI shell is an example of an expert system exhibiting low knowledge complexity and low technological complexity. A global risk management system that includes credit, market and operational risk measurement utilizing mainframe distributed databases linked to workstations located around the globe would be one that exhibits both high knowledge and high technological complexity [27]. An example of the latter is the Life Underwriting System by Lincoln National Reinsurance Company, whose goal is to improve organizational profitability through better underwriting risk management. This system includes in-depth knowledge from both the medical and underwriting domains and is supported by multiple technologies and databases.

![](/api/attachments/J5VCY7CG/fulltext/images/2023b15c0485382a2c6fd7e9e8dbb38c8a83d520583f99a4cd4a4afc0a9a812b.jpg)  
Technological Complexity (Number of Software Packages/Platforms Used)  
Fig. 4. Knowledge and technological complexity framework: a few examples.

The uses of AI in financial risk management are numerous:

\- Manufacturers Hanover Trust in New York City successfully installed an expert system called TARA (Technical Analysis and Reasoning Assistant) to assist traders who deal in foreign exchange. The system helped identify patterns associated with foreign exchange rate movements, improving management's ability to identify changing market risk. The flexibility and capability of TARA to explain its reasoning, along with senior management support, were important to its success at Manufacturers Hanover. Manufacturers Hanover Trust recently implemented an expert system called Inspector that monitors worldwide foreign exchange trading in order to detect irregular activity. The system is considered extremely cost-effective and fits well with existing technologies in the organization, two factors considered important for its success [8].

\- The American Stock Exchange is currently experimenting with an expert system, $MESS$ (Market Expert Surveillance System), to detect cases of insider trading. $MESS$ scans thousands of trade transactions daily and is able to shortlist a few of these that it considers may involve insider trading frauds [22].

\- Chase Lincoln Bank developed a planning expert system, the Chase Personal Financial Planning System. The system provides financial planning advice to investors and can be used to produce output tailored to specific user interests [19].

\- RESRA (Residential Real Estate Appraiser) used by all Security Pacific appraisers in California was designed to remove appraisers' biases in deciding whether real estate loans should be approved. This made an objective measurement of credit risk possible [19].

\- Citibank makes use of an expert system DOLS to issue thousand of checks to retirees, and also to make suitable deductions for taxes and pension amounts [19].

Another area where AI systems have proved themselves for financial risk management is pattern recognition. This involves analysis of current or historical data on prices, yields or other measures related to specific financial instruments or the market at large to detect patterns for predictive models. The ability of these systems to process and store data for comparison purposes has given them a competitive edge over humans in recognizing trends that are useful to control risk. An expert's knowledge can now be coded in a system to infer meaningful predictions from the patterns detected. One example of such a system is PRISM (Pattern Recognition Information Synthesis Modeling) developed by the Raden Research Group. The system has been successfully used to predict changes in the Dow Jones Industrial Average [1].

In cases where structured knowledge is available (for example, in programmed trading activities involving cross-market interest rate or market index arbitrage), traditional procedural programming methods can be used to provide fully automated decision support and trade transaction capabilities. AI models seem to work best in situations where semi-structured knowledge is available to make decisions, a characteristic that fits many financial risk management situations quite well. Most of the rules used in expert systems can be extracted from one or more experts in the trading and treasury domain. In some cases, however, structured knowledge, similar to that presented in finance textbooks, may be hard to elicit. In others, it may be easy to elicit, but harder to apply.

## 3.5. Neural nets and the prediction of changing risk

Neural network technology is another innovation that is being explored for use in the risk management domain [14,32]. Neural networks are computer systems whose internal architectures are designed to imitate real neural systems. Two objectives of present-day neural net research are: to duplicate adaptive behavior of humans and to duplicate their capacity to learn new things quickly. Neural nets are now being tested in the financial services industry in numerous contexts, including: bankruptcy and asset price prediction, mortgage-backed securities (MBS) portfolio pre-payment rate forecasting, and classification of customers to improve targeting of new services. In contrast to expert systems neural nets are used where problems cannot be readily represented by explicit analytic models, and where the process of reasoning to obtain a result may be fuzzy. For example, neural nets may prove to be useful for forecasting financial indicators where no universally acceptable forecasting model exists.

Neural nets model massive parallelism and high interconnectivity among a large number of processing units called neurons. Each of these can have multiple inputs and outputs. Generally, they are arranged in three layers: input, output, and hidden. Input neurons act as sensors and accept all incoming signals. Output neurons act as motoring units generating the results for a classification scheme. The hidden layer comprises neurons that together imitate the complex phenomenon of learning from mistakes and fine-tuning the network so that the predictions achieve more accuracy.

Neural networks usually have two stages: a learning and a performing stage [21]. During the learning phase, the neural net is trained on a part of the data (e.g., price changes, defaults, etc.). This subset (inputs) is supplied to the network and a set of predicted values (outputs) is predicted from the network. These are compared with the actual values. Depending on the difference between predicted and actual values, the network is iteratively fine-tuned to reduce this difference. This process is repeated for all observations from the training data set. The resulting neural net can then be used to predict values for unknown classification variables.

Neural nets have been shown to perform better than conventional classification techniques (such as regression) in cases where the classification scheme does not have a well-defined model. For example, Dutta and Shekhar [14] showed that a neural network consistently outperformed a regression model in predicting bond ratings. Cosset and Roy [10] also showed that neural networks had a higher predictive accuracy than comparable logistic regressions in predicting country risk ratings. Although the technology is promising for forecasting financial indicators, one should be cautious in suggesting use of expensive neural net systems when the problem is well-structured enough to permit conventional classification approaches.

Reports of successful neural net applications in industry have sparked rapid growth in their use. Some examples are:

\- Chase Manhattan Bank of New York City developed a neural network application, ADAM, in collaboration with Inductive Inference. ADAM extracts a collection of Boolean formulas from historical data to determine the borrower's credit-worthiness [26].

\- In the United States Standard and Poor's successfully used NeuralWorks Professional to predict bond price swings [26].

\- The Nestor Character Learning System is being successfully used in some banks in the United States to interpret the dollar amounts scribbled on the face of a check [18].

## 4. Risk management systems: Cost-benefit implications for implementing firms

Risk management systems (RMS) based on RMT are generally expensive. Sophisticated, large-scale risk management tools can cost anywhere from a few thousand to millions of dollars. Given the high costs, senior management is faced with the difficult question of their payback. To justify investments, management needs to tie all the benefits of a risk management system to its costs and then evaluate the cost-benefit ratio. The usual discounted cash flow analysis fails to measure the real benefits of such a system, as most benefits are intangible or uncertain, and thus difficult to convert into cash flows.

For example, it is hard to evaluate the benefits of a system which assesses the credit risk of a borrower more accurately than a credit analyst, who may be conservative in approving loans and, as a result, may reject some loan applications that might not have been refused by the system. However, because the loan was not approved, data on the expected returns of lost business will not be available when the bank evaluates benefits of the system. Another example is in systems that provide graphical displays. These are used to inform a trader how the market is expected to behave during the course of the day. Although graphics may make it easy for a trader to analyze incoming information, it is very hard to measure the actual benefits of such a system. Even when the overall profits are believed to have increased after the use of a system, it is not easy to determine what part of them is attributable to system use. (See [12] for additional details.)

## 4.1. Risk management systems: Benefits

Recent advances in IT value research have shown that creation of a business value linkage may be useful in understanding the scope of indirect benefits. Business value is defined as the economic contribution that IT can make to firm profitability. A linkage formalizes the relationships between IT investment and business value. For risk management systems, it involves three primary features:

\- identifying all input costs or investments needed to install and maintain the system;

\- understanding all intermediate production processes, both inside and outside the firm, that are affected by the use of the system; and

\- identifying all business value outputs whose variations can be attributed to the investments.

Figure 5 provides an illustration of a linkage for a distributed object-oriented database system for managing global portfolios. The system has four possible intermediate production processes from which business value can be realized indirectly. These four production processes are: data hiding control operations, data integrity control operations, portfolio management operations, and data mailing operations. By providing limited data access to users, the system will be able to save losses that may result from inappropriate sharing or leakage of information. The system should also be able to reduce operating costs by taking care of data integrity problems. Because the system will obtain updated information in a very short time on all worldwide financial instruments, the firm will be able to control portfolio risk and increase returns from investments. Finally, in the long run the system should be able to control data mailing costs.

![](/api/attachments/J5VCY7CG/fulltext/images/8fc20acf2eff8552c3aed830fdc12377b3f35aea810dfbe882a02319f6d5ea5d.jpg)  
Fig. 5. Business value linkages for a distributed database system.

## 4.2. Risk management systems: Cost

To manage risk, a firm typically has to incur several types of costs, including fixed, variable and opportunity costs. Fixed costs include investments in systems. If a new risk management system involves complete replacement of existing hardware, it may not be preferred over one which uses existing equipment, even if the latter system does not provide as good performance. Variable costs include costs of periodic input data feeds, preventive and break-down maintenance, and of software updates, etc. Variable cost is dependent on the amount of service requested. For example, data feeds may be available in several forms: on-line reports; batch reports; daily reports; and monthly or quarterly reports. The actual cost of the data will usually vary.

Another dimension of cost in a risk management system is the opportunity cost of losing business to competitors. Opportunity costs arise when profitable risks are not properly identified due to the inadequate performance. Opportunity costs are important here for two reasons. First, they form a basis for comparison of performances of different systems. Second, unlike other costs, opportunity costs in not using a particular system vary for different firms, depending on the nature of their businesses and their current investments. For example, if an investor has not invested in fixed income assets, a risk management system providing in-depth analysis of them will be worth less to him than to an investor who has diversified investments in the whole range of products, including fixed income assets.

## 4.3. Data quality: Its importance in risk management system design

The performance of a system depends on the quality of the data feeds that it utilizes. Very often, data that are updated at more frequent intervals will aid in obtaining a more accurate reading of the financial risks. Similarly, if the data are accurate and made available with a minimum delay, it is likely that the RMS will provide more value to the user. Work that is underway, however, suggests that some tradeoffs are inevitable, for example, in terms of frequency, response time or accuracy and even the models on which these systems are based, assuming there is a limited budget $[4,5]$ .

To evaluate the impacts of variations in quality of data feeds, it is necessary to state all possible forms of data feeds used as inputs to the particular risk management system. Next, all data quality attributes of these data feeds, such as frequency, response time and accuracy, should be listed. By simulating the variations in data quality using a sample data set, the decision maker can determine how a particular risk management model will perform, and examine how far its performance deviates from the best observed performance when the highest quality data are used [2]. Performance is treated as an objective measure in terms of the specifics of a particular risk management problem. For example, the utility of a well-hedged portfolio may be one measure of system's performance. In this case, a measure of utility can be used to gauge the objective effectiveness of the hedges. The difference in performance of two systems distinguished by different data quality designs gives the difference between the opportunity costs. The corresponding cost of each data feed should be included with the opportunity cost for each RMS. The total costs can then be used in the optimization problem for selecting the appropriate data quality levels that will match the firm's risk management requirements.

## 4.4. Risk management systems: How should they be selected?

As a first step towards evaluating risk management systems, managers need to state their requirements and estimate future needs. Knowing these, a cost-benefit analysis can be carried out for alternative tools and the data feeds they require.

We recommend the following steps:

1. Identify the types of risk the business faces. Identification of business risk is important to verify if the RMS being considered will help manage the business risk.

2. List all objectives in using an RMS: Management usually opts for an RMS with certain objectives in mind. It is essential that all such objectives be listed to make comparison easier. Possible objectives of a RMS may be: forecasting foreign exchange patterns, detecting errors in international data entries, checking for trading frauds, etc.

3. Compile the list of alternative RMSs that can do the job: This involves shortlisting those RMSs that satisfy the management's objectives enumerated in Step 2.

4. Gather all costs associated with an RMS: For each, calculate the fixed and the variable costs.

5. Sketch a business value linkage diagram for identifying the impacts of the RMS: For each RMS, identify all intermediate production processes that will be affected by the use of the system. This will help to determine hidden or less tangible benefits.

6. Estimate all direct and indirect business value outputs of the RMS: The individual intermediate production managers must provide an estimate of business value outputs, e.g., savings in operating costs, value-added by better risk management control, etc. Also estimate the direct revenues that might result from the use of the system. The sum of these direct and indirect benefits also provides a measure of opportunity costs of not using the RMS.

7. Select the system that has the highest expected benefit to cost ratio.

## 5. Conclusions

Advanced information technologies can help in identifying, measuring and monitoring financial risk. With the advent of sophisticated computing technology, investments in foreign countries are becoming more easy-to-track and easier to monitor. Artificial intelligence has been used with success in many financial applications, and it is now being used to assist risk managers in identifying risky events. Measurement of financial risk under alternative investment scenarios can now be carried out in seconds using parallel computing architectures. Monitoring of global investment portfolios is now made simpler by distributing the task at a number of worldwide locations and integrating the results using advanced communication technology and object-oriented database systems. Finally, neural networks have been shown to be useful to identify the extent to which risky events can affect forecasted outcomes.

The benefits of RMT are obvious, but in many cases these benefits are intangible or probabilistic. Thus, justification of significant investments in such systems is difficult, and the appropriate strategies for justification still need to be established. We suggested the use of a business value linkage to identify direct and indirect benefits of RMT investments in the intermediate production processes of a financial firm, and also suggested the use of an economics-based approach to selecting the design of risk management systems in terms of the data, the modeling, and the hardware component. In particular, data quality optimization can enhance the benefits of a risk management system while adding relatively few additional costs.

All firms are subject to operating risks. In addition, market and credit risk can be readily adapted to reflect the content of different kinds of business scenarios. Market risk, as an example, may arise from competitor pricing strategies, the entry of new market competitors, and a variety of other factors that are beyond management's control. In software development projects, volatility of returns is an important consideration, especially as the mission of the organization changes or the underlying software development methods evolve. Finally, successful marketing strategies generally evolve after a careful study of credit risk. Thus, the discussion provided here applies to a number of businesses across different industries. By identifying the types of risk an industry faces, one should be able to select a suitable RMT to monitor these risks.

## References

[1] Aronson, D.R. "Artificial Intelligence/Pattern Recognition Applied to Forecasting Financial Market Trends," MTA Journal, May 1985, pp. 91–132.

[2] Ballou, D.P., and Pazer, H.L. "Modeling Data and Process Quality in Multi-Input, Multi-Output Information Systems," Management Science, Vol. 31, No. 2, February 1985, pp. 152–162

[3] Banker, R.D., Kauffman, R.J. "Reuse and Productivity: An Empirical Study of Computer Aided Software Engineering at the First Boston Corporation," MIS Quarterly, Vol. 15, No. 3, September 1991, 375–401.

[4] Bansal, A., and Kauffman, R.J. "Risk Management and Data Quality: An Information Economics Approach." Working paper, Center for Research in Information Systems, Stern School of Business, New York University, November 1991.

[5] Bansal, A., Kauffman, R.J., and Weitz, R. "Comparing the Forecasting Performance of Regression and Neural Nets When Data Quality Varies." Working paper, Center for Research in Information Systems, Stern School of Business, New York University, September 1992.

[6] Beirwag, G. Duration Analysis, Ballinger Publishing Company, Cambridge, Massachusetts, 1987.

[7] Bradley, S.P., and Crane, D.B. "A Dynamic Model for Bond Portfolio Management," Management Science, Vol. 19, No. 2, 1972, pp. 139–151.

[8] Byrnes, E., Campfield, T., Henry, N. and Waldman, S. "Inspector: An Expert System for Monitoring Worldwide Trading Activities in Foreign Exchange." In Proceedings of the Second Annual Conference on Innovative Applications of Artificial Intelligence, Georgetown University, Washington, DC, May 1990.

[9] Chin, R.S., and Chanson, S.T. "Distributed Object-Based Programming Systems," Computing Surveys, Vol. 23, No. 1, March 1991, pp. 91–124.

[10] Cosset, J.C., and Roy J. "Forecasting Country Risk Ratings Using a Neural Network." In Proceedings of the Twenty-Third Annual Hawaii Conference on System Sciences, Kailua-Kona, Hawaii, 4: 327–334, IEEE Press, January 1990.

[11] Dahl, H., Meerus, A., and Zenios, S.A. "Some Financial Optimization Models: I. Risk Management," Report 89-12-01, Decision Sciences Department, The Wharton School, University of Pennsylvania, December 1989.

[12] Diamond, L., and Kauffman, R.J. "The Business Value Effects of Cognitive Biases in Trading Workstation Window Design." In Proceedings of the 1990 Hawaii International Conference on Systems Science, IEEE Press, January 1990.

[13] Doherty, N.A. Corporate Risk Management, McGraw-Hill Inc., New York, NY, 1985.

[14] Dutta, S., and Shekhar, S. "Bond Rating: A Non-Conservative Application of Neural Networks," In Proceedings of the Second International Conference on Neural Networks, IEEE, 1988, pp. 443–450.

[15] Fabozzi, F.J., editor. The Handbook of Fixed Income Options: Pricing, Strategies, and Applications, Probus Publishing Company, Illinois, 1989.

[16] Granito, M.R. Bond Portfolio Immunization, Lexington Books, D.C. Heath and Company, Lexington, Massachusetts, 1984.

[17] Ingersoll, J.E., Jr. Theory of Financial Decision Making, Rowman and Littlefield, Totowa, New Jersey, 1987.

[18] Keyes, J. "AI in the Big Six," AI Expert, Vol. 5, No. 5, May 1990, pp. 36A3.

[19] Keyes, J. The New Intelligence: Artificial Intelligence Ideas and Applications in Financial Services, Harper Business, New York, 1990.

[20] Kusy, M.I., and Ziemba, W.T. "A Bank Asset and Liability Management Model," Operations Research, Vol. 34, No. 3, 1986, pp. 356–376.

[21] Lippmann, R.P. “An Introduction to Computing with Neural Nets,” IEEE ASSP Magazine, April 1987, pp. 4–22.

[22] Lucas, H. "Market Expert Surveillance System," Working Paper, Center for Research on Information Systems, Information Systems Department, Stern School of Business, New York University, 1990.

[23] Mark, R.M. “Techniques for Addressing Market and Other Trading Risks.” Presented at the Global Trading Technology Conference, New York, May 1990.

[24] Mark, R.M., and Roth, S. "Automated Decision Support in the Trading Room." Presented at the Fourth Annual Conference on Integrating Trading Technologies, New York, February 1990.

[25] Markowitz, H. "Portfolio Selection," Journal of Finance, Vol. 7, 1952, pp. 77–91.

[26] Marose, Robert A. "A Financial Neural-Network Application," Al Expert, Vol. 5, No. 5, May 1990, pp. 50–54.

[27] Meyer, M.H., and Curley, K.F. "Putting Expert Systems Technology to Work," Sloan Management Review, Winter 1991, pp. 21–31.

[28] Mulvey, J.M., and Vladimirou, H. "Stochastic Network Optimization for Investment Planning," Report SOR-88-2, Department of Civil Engineering and Operations Research, Princeton University, 1988.

[29] Platt, R.B., editor. Controlling Interest Rate Risk: New Techniques and Applications for Money Management. John Wiley and Sons, New York, 1986.

[30] Prietula, M.J., and Simon, H.A. "The Experts in Your Midst," Harvard Business Review, January–February 1989, pp. 120–124.

[31] Weston, J.F., and Copeland, T.E. Managerial Finance, The Dryden Press, New York, 1986.

[32] White, H. "Economic Prediction Using Neural Networks: The Case of IBM Daily Stock Returns." In Proceedings of Second IEEE International Conference on Neural Nets, 1988, San Diego, pp. II-451-458.

[33] Zenios, S.A. "Massively Parallel Computations for Financial Planning Under Uncertainty," Report 90-11-10, HERMES Laboratory for Financial Modeling and Simulation, Decision Sciences Department, The Wharton School, University of Pennsylvania, November 1990.

[34] Zipkin, P. "The Structure of Structured Bond Portfolios," Technical Report, Columbia University, Graduate School of Business, 1989.
