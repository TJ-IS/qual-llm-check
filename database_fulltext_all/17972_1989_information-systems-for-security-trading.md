---
otero_id: 17972
otero_key: "8CENHU8U"
title: "Information systems for security trading"
authors: "Kar Yan Tam"
year: "1989"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90076-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems for Security Trading

Kar Yan Tam

Department of Management Science and Information Systems, College and Graduate School of Business CBA 5.202, University of Texas, Austin, Texas 78712-1175, USA

Deregulation of financial markets has created a volatile and competitive environment for companies engaged in security trading. In order to stay competitive, security firms have to rely more on their information systems (IS) to increase their responsiveness to market conditions. As the strategic value and the cost of such systems increase, extreme care must be exercised in their design. In this paper, issues pertaining to the design of IS for security trading are addressed. Four major issues are discussed: (1) Segmentation of the trading process, (2) Identification of trading objectives, (3) Technological requirements, and (4) Management support, planning, and control.

Keywords: Financial Instruments, Trading Objectives, Security Trading Automation, Order Processing, Fund Investment, Arbitrage, Program Trading.

![](/api/attachments/8CENHU8U/fulltext/images/f056fe869288f244f1e69bb65e8279c7664329ef1bc99027fb3267079a4062a2.jpg)

Kar Yan Tam is currently an Assistant Professor of Information Systems at the University of Texas at Austin. Professor Tam holds a B.S. in Mathematics and Computer Science from University of Illinois at Urbana, a M.S. in Computer Science and a Ph.D. in Management Information Systems, both from Purdue University. His teaching at the University of Texas includes Data Communication, Database Administration and Decision Support Systems. Professor Tam's major research interests focus on the applications of Artificial Intelligence in finance and manufacturing.

## 1. Introduction

The world economy has experienced a proliferation of financial instruments during the last decade. These, such as financial indexes, options, mutual funds, mortgage-backed securities, interest rate and currency swaps have significantly increased the number of alternatives to investing, raising funds, hedging against risk, and carrying out arbitrage activities. The impact to the financial services industry is indeed significant. Yet this financial bonanza shows no sign of ending. Instead, more innovative products are expected to appear in future. These products will probably be geared towards institutional investors, as their stakes in the security markets have been increasing in recent years.

The driving force behind this bonanza is primarily the deregulation of financial markets on a world wide basis – The “Big Bang” in U.K. and the opening of the Japanese financial market and to keen competition among exchanges. Deregulation has been fueling the proliferation of financial products by eliminating fixed commissions charged by brokers and by allowing banks and insurance companies to participate in the brokerage business. In order to obtain the necessary capital to adjust to a more competitive environment, the industry is reorganizing itself, and this has resulted in a series of mergers and consolidations.

Proliferation of financial instruments has rendered the formulation and implementation of trading strategies a laborious task. The complexity involved in selecting which security to establish (or liquidate) has gone beyond human comprehension because the time constraints imposed on these decision processes fall within fractions of a second, and this is common in arbitrage. Substantial losses, either in real monetary terms or opportunity costs, would be incurred if any changes in the market are not quickly identified, interpreted, and acted on.

In order to increase the responsiveness of their trading operations to market information, security firms have been investing heavily in computerized trading systems [6]. The trend towards security trading automation has become apparent in recent years. First, computers were installed to automate the clerical work, such as maintaining account positions and conducting the settlement process. Then computers were integrated with the communication network to facilitate prompt access to financial data from the market. Nowadays, program trading, portfolio insurance, and similar concepts could never be materialized without computers.

A major concern shared by companies engaged in security trading is how to face the structural changes of the environment and to stay competitive. In particular, how do we process the tremendous amount of financial data in real time, and what is needed to achieve that? Here, we address these questions from an information system point of view. Our intent is to point out the essential attributes of an information system for security trading and to address issues pertaining to its design.

## 2. Segmentation of the Trading Process

A Security Trading System in its broadest sense refers to an organized entity designed to carry out trading operations. In [29], Strahm has defined the term “trading systems” as:

(1) A trading advisor who handles managed accounts, private pools, or public funds;

(2) A portfolio of several advisors;

(3) A set of trading rules (“technical trading systems”) using specific parameter values applied to a single market;

(4) A technical trading system simultaneously trading with several distinct sets of such parameter values;

(5) A technical trading system simultaneously applied to a wide variety of markets; and

(6) Several technical trading systems employed simultaneously.

Of course, this list is not exhaustive. Nevertheless, an invariant property of these systems is that they take in information, interpret it, and respond accordingly. The entire process is carried out in real time. In some systems, such as technical trading, responses to incoming information are prespecified in the form of trading rules. In its strictest form, a technical trading system does not involve any human intervention. It sells and buys securities according to the signals generated by the underlying trading rules, which are in turn specified by a set of parameters such as high/low prices and transaction volumes [see references 14, 15, 32]. However, most trading systems have a significant degree of trader participation. The generic structure of a trading system and its interactions with the market(s) is shown in Fig. 1. It depicts the flow of information and its transformation during the entire process. The trading process is divided into three functional segments: (1) information gathering, (2) formulation/analysis, and (3) strategy implementation. In a typical trading system, information is constantly generated from the market(s) and channeled to the trading system. The form of information collected from the market is rudimentary. It can be ask-bid prices from the exchanges, latest reports of the economy, news about incidents happening world-wide, and corporate earning reports to name a few. The volume of information is tremendous therefore a certain degree of preprocessing is required to condense the incoming information to a manageable size. Two types of preprocessing take place during the information gathering stage: filtering and updating.

Filtering. Not all information is relevant in a particular instance. That which is irrelevant with respect to the current trading strategy need not be retained. This avoids overburdening the trader with useless information. For example, a trader working on a foreign exchange hedge strategy may be interested in the spot rate and the 3-month future rate of yen and dollar only. All other information would be irrelevant at this time.

Updating. Some data have to be updated to reflect the actual situation in the market. Among these, ask-bid prices are the most important; they need to be updated whenever a new transaction has taken place. Traders are usually interested in the trend of movements in transaction volume and security prices. Thus, logs of these data are important in making decisions. Unlike some of the information that can be filtered out, information pertaining to these data has to be retained for further use.

![](/api/attachments/8CENHU8U/fulltext/images/732585be9e0bb9d739be54bcde0042c770aab3438c17d82ee1386e24249d7e34.jpg)  
Fig. 1. Segmentation of the Trading Process.

In essence, the output of the first stage is an updated description of the market(s) and the position of the firm. The outputs may be different in different trading systems because of discrepancies between the ways these two preprocessing functions operate. This partially explains why two trading systems will behave differently in the same market situation. The difference in trading behavior can also be explained by the various trading objectives with which trading systems are associated.

Once an updated description of the market is obtained, the next step is to formulate trading strategies. They are then analyzed. The complexity of these analyses varies significantly and is dependent on the system objective. No matter how complicated a trading strategy is, it can always be reduced to answering the question “When should we establish/liquidate a position of a security?”

The answer is, to a large extent, dependent on the following factors:

Actual ask/bid price;

Request ask/bid price;

Size of each contract;

Maturity date (if any);

Margin requirement;

Transaction cost;

Estimated risk;

## Estimated return;

Forecasted supply/demand; and

Tax requirement.

Added to these factors are the relationships between different yet closely bound instruments, such as between the price of a stock option and of the underlying stock. As shown in the list, the formulation/analysis stage is knowledge-intensive. It draws on information from sources in different domains. Hence, it usually takes a relatively large amount of time to arrive at a trading decision. Instead of trading a single security, an investment strategy usually includes the trading of a basket of securities. Large-scale mathematical programming is commonly used to decide the weights to be invested in an individual security. Some of these optimization techniques have proved to be extremely time-consuming (NP-hard), and the variables (e.g., expected yield and risk) that are input to these optimization programs in turn have to be estimated before by using statistical routines. These tasks take up a large amount of time, making the analysis stage the bottleneck of the entire process.

Any means that can speed up these tasks will definitely improve the position of the company with respect to its peers. A trading system capable of interpreting and responding more quickly than others will definitely gain a comparative advantage. Recently, attempts have been made to automate a subset of the analysis process by using advanced techniques of artificial intelligence and expert systems [22].

Once the trader has decided which securities to establish (or liquidate) and at what prices, the corresponding trading strategy is then implemented. This involves the actual buying and selling of securities in the market. In order to avoid opening the trader's position to potential losses, the trader must compare actual quoted prices with the calculated prices before committing to a strategy. It is very likely that the prices on which the formulation was based will have by then changed.

The implementation must be achieved in such a way that the strategy is either totally completed or aborted. A half-way completed strategy would have unknown and probably disastrous results. There are two complications here. First, a strategy might consist of securities that are traded in different geographically located markets in different time zones; a number of securities have spot and future markets located in different parts of the world. Second, a strategy might require the simultaneous trading of a number of securities; this is very common in arbitrage and hedging strategies.

Trading strategies are manually implemented by a group of traders. The entire strategy is properly divided and synchronized among the participants. A trading group might be organized internally, in the same dealing room, or across phone lines. Communication and control during the actual buying and selling are made possible by shouting or across phone lines. In general, the objective of this stage is to check the requirements of the formulated strategies against the actual market conditions, making sure that no half-way completed trading strategy is executed. Some exchanges provide on-line buying and selling systems that will reduce the risk exposure during the implementation of a trading strategy. For example, the New York Stock Exchange (NYSE) operates a Designated Order Turnaround System (DOT) which allows its members to place selling and buying orders of a large basket of securities at the same time.

## 3. Objectives of Trading Systems

What make a trading system unique is its objective. Trading systems can be categorized according to three different objectives: order processing, arbitrage, and fund investment. Because different objectives impose different functional requirements on the information systems, an understanding of these three is essential.

## Order Processing Systems

Order processing systems are the most basic forms. In fact, to process orders is the primary functions served by a brokerage house before all others. Its objective is to carry out buying and selling orders for its customers. These systems are profit centers because the major portion of revenue is generated from commissions charged for each transaction.

## Arbitrage Systems

The objective of an arbitrage system is to detect arbitrage opportunities that lead to risk-free profits. The many ways of carrying out arbitrage activities are usually coded as mathematical expressions with prices as the determining variables. Any significant deviation from the equilibrium position as reflected by these expressions will trigger the execution of an arbitrage strategy to capitalize the profit.

For example, a simplified arbitrage strategy based on the interest rate parity relationship is stated as the following decision rules:

if $\Delta y + (1 + r_{d})^{t} < R_{0}(1 + r_{f})^{t}/R_{t}$ then at time 0, 1. borrow from the domestic bond market and invest in the foreign bond market yielding at $r_{f}$ , and simultaneously

2. purchase a future contract on domestic currency at $R_{t}$

if $(1 + r_{d})^{t} > \Delta y + R_{0}(1 + r_{f})^{t}/R_{t}$ then at time 0,
1. borrow from the foreign bond market and invest in the domestic bond market yielding $r_{d}$ , and simultaneously

2. sell a future contract on domestic currency at $R_{t}$

$r_{d}=$ current yield of the domestic bond market $r_{f}=$ current yield of the foreign bond market $R_{0}=$ spot exchange rate of the two currencies $R_{t}=$ exchange rate of the two currencies at time t, t>0

$\Delta y =$ threshold yield of the strategy, $\Delta y > 0$

Relatively less computation is required to evaluate these expressions, yet the speed with which prices are reported and buying signals are delivered directly determine the efficacy of an arbitrage system.

Program Trading systems are notable examples of arbitrage systems; they have stirred considerable controversy recently. An arbitrage strategy is coded as a computer program in program trading. The computers watches closely the spot prices of those stocks that make up a stock index (such as S&P 500), and compares them with the future stock index (S&P 500 Future Index). Any significant difference between the two implies a risk-free yield. Selling and buying are then generated automatically to capitalize the profit.

The risk-free property of arbitrage activities makes it possible to delegate a significant portion of the job to the computer. However, most trading transactions are generated by investment activities with risk as the major factor in decision making.

## Fund Investment Systems

The number of funds, especially mutual funds, has increased significantly in recent years. Under the risk/yield framework of investment theory $[20]$ , the objective of a fund investment system is to attain the maximum yield of a fund given a certain degree of risk. Instead of detecting deviations in prices as in the case of arbitrage, a complete investment strategy requires assessing the risk exposure of each strategy and its expected return. Large scale optimization techniques provide part of the solution. However, some of the parameters, such as political and social incidents which have significant impacts on the decisions, cannot be easily quantified. They are instead subject to human valuations, which are based on experience, intuition, and belief.

## 4. Mapping Trading Objectives with System Functions

Sometimes, trading systems serve more than one objective during operation. For instance, in foreign exchange dealing, orders and arbitrages are usually processed concurrently. Failing to separate these three objectives might lead to poor mapping between system functions and their intended purposes.

For order processing systems, security prices and customers orders are the primary input. Each order received is checked against the current position of the customer and the margin requirement (if appropriate) associated with the security. A commission is calculated and the order is then sent to the market. The input prices are used to update the positions of their customers. In cases where brokerage houses offer financial services to their customers, it is essential to keep track of the status of each customer. If the current prices indicate additional funds are required to cover a losses in an account, signals are then generated to alert the trader to inform the customer. This is especially important for highly leveraged securities, such as future commodities with low margin requirements [26].

Selling and buying orders are not necessarily implemented on-line or in chronological sequence. The sequence depends on the priority set by the system. Order processing IS are supportive in nature; they support the trading operation by monitoring the status of each account in response to market conditions. Overall, the design of an order processing system is basically that of an accounting IS with some extended computational facilities $[7,11,17]$ . Thus, guidelines similar to that for an accounting IS can be followed.

The main task of an arbitrage system is to detect any price fluctuations that lead to lock-in profit. Time is critical. A fast computation unit is required to assess the arbitrage relationship in real time. The amount of data involved is relatively small, mainly quoted prices; yet that information has to be retrieved very quickly. This imposes constraints on the design of the retrieval system which would favor certain data modeling schema and file structures over others. For example, it might suggest a traditional file system over a relational DBMS simply because the former is more efficient. Because of the repetitive nature of the task, information can even be hardwired in the system. This gives the fastest arbitrage system possible. To this end, arbitrage systems are actually real-time processing systems.

Unlike arbitrage, fund investment includes risk, a factor which must be considered in analyzing fund investment strategies. The design of IS that support fund management, therefore should include facilities that support the assessment of risks. A number of pricing models have been developed to assist traders in understanding the relationship between return and risk of an investment portfolio. The Capital Asset Pricing Model (CAPM) developed by Sharpe [27], Lintner [18], and Mossin [19] has been widely used for the last two decades. A more general model based on the Arbitrage Pricing Theory (APT) proposed by Ross [23,24] has been gaining popularity in recent years. Both of these models relate the return of a security to the systematic risk associated with the security. They differ in the number of factors to which the systematic risk is related. In CAPM, the systematic risk is related to the market portfolio, whereas in APT it can be related to more than one economic factor. The parameters of these pricing models require a large amount of data to estimate. To support this, a database is essential to store the historic data for estimation purposes.

Instead of adopting a quantitative approach in risk assessment, traders may employ a qualitative approach. In this approach, the risk associated with a fund depends on a set of attributes that are defined by a trader (or a group of traders). These attributes and their values represent the trader's perception and decision model of the market situation, thus explaining why different traders will respond differently to an identical market situation. The determination of an attribute value may simply be based on previous experience or it might require the solution of a huge combinatorial problem (determining the weights of stocks comprising a fund). Usually, a fund investment strategy is the end-product of a combination of empirical and qualitative analyses. To facilitate these analyses, we need:

1. A model management system to store the analytical models. This is a piece of software that supports the definition, management, integration, and execution of models. Numerous model management schema have been proposed, ranging from first order logic predicate [4], CODASYL DBTG [16,28], relations [2,3], and structural modelling [10]. They differ in the ways models are represented at the logical level. The actual implementation of models are opaque to the users. By providing a logical view of models independent of their physical storage structures and processing procedures, traders are able to call upon the various portfolio selection and asset pricing models stored in the model base in a declarative manner. In other words, the traders only have to specify what they want without bothering with how the calculation is performed.

![](/api/attachments/8CENHU8U/fulltext/images/9855f5e6bd0c6d32a90cbc8ce9971182c965bcf7766215e6c7199c645f401277.jpg)  
Fig. 2. Integration of Models and Data in Strategy Formulation.

2. A database storing information on the fund. It serves two main purposes. First, it provides a static view of the fund at any particular point in time. Second, it stores the historic data pertaining to the fund. These data include price and volume movements of securities, economic indexes, P/E ratios, etc. Some are used to estimate the model parameters while others may be used for report generation.

3. An interface blending the database and the model management system to support integrated problem solving, queries, and report generation. For instances, in building an investment portfolio, a trader might want to use Markowitz's model to determine the weight of each comprising security. The input of the Markowitz's model are the expected risk and expected yield of each security. In order to obtain the input, the trader may want to use another model, say the Capital Asset Pricing Model, to estimate the expected yield of each security. For the expected risk, the trader may simply calculate the variance in price movement during the past six months. For the Capital Asset Pricing model, the trader has to decide on the market portfolio in order to determine the market risk. To do this, it may be necessary to browse through the database to select the securities for the market portfolio. The data flow diagram for this example is illustrated in Fig. 2. Other traders might employ totally different strategies, requiring different models and data. As illustrated by this example, the process of strategy formulation and analysis requires integrated resources from the database, the model management system, and the trader. An interface that integrates all three components as a synergy is essential to provide fast answers to what-if questions.

## 5. Technology Requirements

Several recent technologies and their applications to security trading are now discussed.

## Communications

A fast communication network forms the core of any trading system. Furthermore, the trend toward twenty-four hour global trading necessitates a global network that connects offices in different geographical regions. This was made possible by the advent of data communication technologies, such as Integrated Services Digital Network (ISDN) and optical fibre. They have drastically increased the capacity of communication lines, allowing more data to be transmitted at a higher speed, and eventually at a lower cost. In terms of data presentation, the information vendor is shifting from video to digital feeds. This allows in-house processing of data that can be presented in any format required by the traders. The number of connecting switches can be reduced significantly by using digital feeds, making it possible to expand the dealing room with much less wiring. The use of optical fibers will significantly increase the bandwidth and the accuracy of digital transmission. Since optical fibers are smaller and easier to install, they require much less space. This can also reduce the cost of setting up a dealing operation, because dealing rooms are usually located in financial districts where the rental cost is very high.

## Data Security

Since financial data, as well as buying/selling orders, are delivered through this network, they are vulnerable to flaws, both intentional and unintentional. Information has to be properly encrypted and physically protected from outsiders. An internal security policy, specifying the access-right hierarchy and the operational procedures, has to be determined in collaboration with top management. This policy should provide a secure environment that covers all components, both hardware and software, and human users engaged in the trading operation [25]. The granularity of the security measures may range from the logical record locking mechanism of a database management system [33] up to the physical locking of a tape library. For internal control purposes, accesses to customer accounts and classified data must be placed on a log and audited periodically [9] to ensure compliance with security procedures.

## Expert Systems

There is an emerging role of expert systems in the domain of security trading. In fact, a number of brokerage houses and banks are developing expert systems to facilitate their trading activities. An expert system is a piece of software that replicates the reasoning processes of human experts [12]. In most such systems, reasoning knowledge is organized as a set of production rules with each relating a set of conditions to some actions or decisions [5,13]. Expert systems are applicable to all phases of the trading process. First, they can help to screen out irrelevant information flowing into the trading system. Second, they can assume part of the analyst's job. Third, they can coordinate and synchronize the buying and selling orders of a trading strategy, making sure that it is totally completed or else aborted. Wisely used, expert systems can reduce the time of the entire trading process, making it possible to respond more rapidly to incoming market information.

## Fault-Tolerant Computers

Fault-tolerance should be an essential property of the underlying hardware to make sure that computing resources are available when needed. Halting the trading operation is an expensive alternative. Safety is made possible by duplicating the hardware components and adding fault detection and recovery circuits to conventional computer architecture. An alternative is a backup computer, together with a set of backup procedures that specify the actions to be taken when the master computer fails.

## 6. Management Issues

The capital investment in an information system, including software, hardware, maintenance, and administration is huge. Therefore, support and understanding of top management is of prime importance in launching a project. The following is a set of typical management concerns:

## Support of Top Management Objective

Each trading system has its own objective. This, whether order processing, arbitrage or fund investment, should be set forth by top management and must be clearly defined beforehand. This is important because the objective can be articulated into the functions of the system, which in turn identify the factors related to its design. The functions performed by an arbitrage system might be very different from that by a fund investment system, with each implying a totally different capacity planning and budgeting strategy. Systems with different objectives should be based on different sets of cost and benefit. In the case of an arbitrage system, the cost and benefits of the system can be correlated with the amortized expenses and the monetary return of the system over a period of time. However, the same criteria would not be applicable to a fund investment system, where return of fund depends on factors which are exogenous to the system.

## Environmental Factors

Environmental factors are those exogenous to a company, such as government regulations/deregulations, market developments, international political situations, and technological innovations. Because of the rapid changing environment, judging from the average life time of a dealing room, the life span of a trading system is only two to three years. Therefore, in developing a trading operation, management should strive to forecast these factors and integrate the findings with the objective of the system. A carefully planned system with a provision to “expect the unexpected” is essential to keep the company at the competitive edge. To achieve this, top management should regularly interact with MIS personnel, making sure that the system is well designed to cope with environmental change.

## Market Integration

Most trading operations of securities firms are segmented into markets. Operations are managed individually as loosely connected subdivisions. This segmentation of trading operations into different markets makes it difficult to implement strategies that span different markets in a timely fashion. Hedging strategies, for example, usually involve two or more markets. To facilitate cross-market trading $[1,8]$ , information systems of different trading operations should be function as a single system in implementing cross-market trading strategies.

## Responsibility for Computer-Generated Decisions

A trading decision today is not just the end product of a mental process but is an interactive process between a trader and the decision support aids. This semi-automatic decision making process renders it very difficult to define the responsibility of traders. Nevertheless, management should provide guidelines that define the scope of responsibility and the role of a trader engaged in the process.

But, computers cannot be held responsibility for their decisions, therefore top management has to decide what kinds of decisions can be made by the computer and who should be responsible for them. In a real-time arbitrage system, selling and buying signals are generated by computers once arbitrage opportunities are detected. Should these signals be automatically sent to the market or should they just alert the traders who are the final decision makers? An arbitrage opportunity might last only for fractions of a second. Any delay will probably impair the possibility of making a risk-free profit. In this case, top management has to compromise between the time gained in a fully automatic trading system and the likelihood of a computer generated error.

## 7. Concluding Remarks

The recent price volatility on the exchanges in New York and Chicago are attributed to computer monitored arbitrage activities, commonly known as Program Trading. It is an arbitrage strategy that uses computer to keep track of the deviation between a stock index future and the spot prices of the composing stocks. Any significant difference between the two results in a risk free yield. Selling and buying signals are then generated to capitalize the profit.

Perceptions of automated security trading are mixed. Public reactions to Program Trading illustrates some of these views. Practitioners in the securities industry have voiced their concerns, and the positions they take depend on the size and the financial capacity of their firms. Critics of Program Trading blame it for the unnecessary volatility of the market. Prices of stocks, at least in the short run, no longer reflect the underlying value and the earning power of the firm. Critics argue that the fundamental purpose of stock trading, which is capital formation, is distorted in the hands of Program Trading. Furthermore, funds from other markets (e.g., bond markets) are likely to be attracted and channeled into the stock market in the hope of arbitrage opportunities. This adversely affects the capital formation process of other markets, thus causing the cost of capital to rise and prices to become unpredictable in those markets.

On the other hand, some big brokerage firms are positive towards Program Trading. Their arguments are based on increase in markets efficiency caused by Program Trading, and they claim that price volatility is merely an adjustment of the market to incoming information. Whether computers are used or not, the market will still adjust to this information. The only difference is that electronic speeds make it possible to shorten the entire process to seconds. From an economical point of view, any arbitrage opportunity will be quickly detected and eliminated by the market. The increase in responsiveness to incoming information, as reflected by the rapid changes in price, is the property of a more efficient market.

Regardless of options, the trend to automation in security trading is underway, and its impact on the financial markets is definitely high. Since the first step in automation has already had a subtle impact on the security market, one would expect structural change to occur in the entire security industry in the months and years ahead. Small brokerage firms are likely to be taken over or go out of business, because of their lack of capital to invest in developing new trading systems. Companies in the brokerage business have to rely more than ever on their computers to increase their responsiveness. The automated information system is becoming the nucleus of the entire trading operation. As pointed out by McFarlan and McKenney [21], the strategic value of information systems in the financial service industry is increasing as more profitable financial products are directly supported by these systems, as illustrated by the increasing budget allocated for technological development in many large banks. According to recent studies [30,31], seven U.S. banks spent more than \$200 millions per year in technology, with Citicorp topping the group by investing \$850-900 millions annually in developing technologies to increase its competitiveness.

An information system plays a strategic role in a financial company, any flaws in the final system because of an improper design are intolerable and a failure of a strategic nature. Extreme care must be exercised in planning and design. The four major issues, (1) Segmentation of the trading process, (2) Identification of trading objectives, (3) Technological requirements, and (4) Management support, planning and control, attempt to identify the essential attributes and to offer design guidelines in building these systems.

## References

[1] Anderson, R. and Danthine, J., Cross Hedging, Journal of Political Economy 89 (6) 1981.

[2] Blanning, R.W., A Relational Framework for Model management in Decision Support Systems, Transactions of International Conference on Decision Support Systems, DSS-82, 1982.

[3] Blanning, R.W., A Relational Framework for Model Bank Organization, Proceedings of the IEEE Workshop on Languages for Automation, November, 1984.

[4] Bonczek, R.H., Holsapple, C.W., and Whinston, A. B., The Evolving Roles of Models in Decision Support Systems, Decision Sciences 11 (2) 1980.

[5] Davis, R., Buchanan, B.G. and Shortliffe, E.H. Production Rules as a Representation for a knowledge-based Consultation Program, Artificial Intelligence 8 (1) 1977.

[6] Duffy, F., Dealing Rooms, The Banker, September 1986.

[7] Everest, G.C. and Weber, R., A Relational Approach to Accounting Models, Accounting Review 52 (2) 1977.

[8] Figlewski, S., Hedging with Stock Index Futures: Theory and Application in a New Market, Journal of Future Markets 5 (2) 1985.

[9] Florentin, J.J., Consistency Auditing of Databases, The Computer Journal 17 (2) 1974.

[10] Geoffrion. A.M., Structured Modelling, Working Monograph, Western Management Science Institute, UCLA 1985.

[11] Haseman, W.D. and Whinston, A.B., Design of a multidimensional Accounting System, Accounting Review 51 (1) 1976

[12] Holsapple, C.W. and Whinston, A.B., Manager Guide to Expert Systems using Guru, Dow-Jones Irwin: Illinois, 1986.

[13] Holsapple, C.W., Tam, K.Y., Whinston, A.B., Inductive Approaches to Acquire Trading Rules, Proceeding of the First Conference on Expert Systems in Business and Finance, New York, New York, November 1987.

[14] Kaufman, P.J., Commodity Trading Systems and Methods, Wiley: New York, 1978.

[15] Kaufman, P.J., Technical Analysis in Commodities, Wiley: New York, 1980.

[16] Konsynski, B.R., On the Structure of a Generalized Model Management System, Proceedings of the Fourteenth Hawaii International Conference on System Sciences Vol. 1., 1980.

[17] Lieberman, A.Z. and Whinston, A.B., A Structuring of an Event-accounting Information Systems, Accounting Review 50 (2) 1975.

[18] Lintnet, J., The Valuation of Risk Assets and the selection of Risky Investments in Stock Portfolios and Captial Budgets, Review of Economics and Statistics 47 (1) 1965.

[19] Mossin, J., Equilibrium in a Captial Asset Market, Econometrica 24 (4) 1966.

[20] Markowitz, H.M., Portfolio Selection, Journal of Finance 7 (1) 1952.

[21] McFarlan, F.W. and McKenney, J.L., Corporate Information Systems Management: The issue Facing Senior Executives, Dow Jones Irwin: Illinois 1983.

[22] Reid, I., Artificial Intelligence in the Market, The Banker June 1986.

[23] Ross, S.A., The Arbitrage Theory of Capital Asset Pricing, Journal of Economic Theory 13 (3) 1976.

[24] Ross, S.A., Return, Risk, and Arbitrage in Risk and Return in Finance I (Friend, I. and Bicksler, J.L. eds.), Ballinger: Mass 1977.

[25] Saltzer, J.H. and Schroeder, M.D., The Protection of Information in Computer Systems, Proceeding of IEEE 63 (9) 1975.

[26] Schwager, J.D., A Complete Guide to the Future Markets, Wiley: New York 1984.

[27] Sharpe, W., Capital Asset Prices: A Theory of Market Equilibrium Under Conditions of Risk, Journal of Finance 19 (3) 1964.

[28] Stohr, E.A. and Tanniru, M., A Database for Operations Research Models, International Journal of Policy Analysis and Information Systems 4 (1) 1980.

[29] Strahm, D.N., Preference Space Evaluation of Trading System Performance, The Journal of Future Markets 3 (3) 1983.

[30] McKinsey & Co., System Technology and the U.S. Commercial Banking Industry, New York and Chicago 1987.

[31] Salomon Brothers Stock Research, Technology and Banking: The Implication of Strategic Expenditures, New York 1987.

[32] Wilder, J.W., New Concept of Technical Trading Systems, NC: Trend Research 1978.

[33] Wood, C., Summers, R.C., and Fernandez, F.B., Authorization in Multilevel Database Models, Information Systems 4 (2) 1979.
