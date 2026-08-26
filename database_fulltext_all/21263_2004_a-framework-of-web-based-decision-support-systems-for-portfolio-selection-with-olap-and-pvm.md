---
otero_id: 21263
otero_key: "PNJAZZKP"
title: "A framework of Web-based Decision Support Systems for portfolio selection with OLAP and PVM"
authors: "Jichang Dong; Helen S. Du; Shouyang Wang; Kang Chen; Xiaotie Deng"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00034-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A framework of Web-based Decision Support Systems for portfolio selection with OLAP and PVM

Jichang Dong<sup>a</sup>, Helen S. Du<sup>b</sup>, Shouyang Wang<sup>a,</sup>\*<sup>,1</sup>, Kang Chen<sup>c</sup>, Xiaotie Deng<sup>b</sup>

<sup>a</sup> Institute of Systems Science, Academy of Mathematics and Systems Sciences, Chinese Academy of Sciences, Beijing 100080, China <sup>b</sup> Department of Computer Science, City University of Hong Kong, Hong Kong, China <sup>c</sup> Department of Computer Science, Tsinghua University, Beijing, China

Received 20 February 2002; accepted 5 January 2003

Available online 26 March 2003

## Abstract

In this paper, we provide an integrated framework for portfolio selection, which is adaptable to the needs of financial organizations and individual investors, and as an organized approach of selecting efficient portfolios for investments. We focus our discussion on the implementation of this framework for a Web-based Decision Support System (DSS) based on our prototype named WPSS—A Web-based Portfolio Selection System for Chinese financial markets. In this system, we adopt technologies such as online analytical processing as an add-on tool for analytical purpose, as well as using Parallel Virtual Machine (PVM) to improve overall performance. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Web technology; Portfolio selection; DSS; OLAP; Parallel computing

## 1. Introduction

Modern portfolio theory stems from Markowitz’s [19] great insights of the Mean–Variance model which states that the key information of a portfolio can be derived from three measurements: expected returns (taken as the arithmetic mean), standard deviations and correlations among those returns. Basically, portfolio selection is a bi-criteria optimization problem where a reasonable trade-off between return and risk is considered—minimizing risk for a given level of expected return and maximizing expected return for a given level of risk. In the financial industry, investors often have to face such difficult decisions that can be provided by computer-based portfolio selection systems fast and efficiently. In general, portfolio selection systems consist of two main processes: asset selection and portfolio optimization. In our design, an efficient portfolio selection system should first be able to determine the best mix of assets based on the investment profile provided by the investor. Then the expected values of the expected rate of return of all assets, corresponding risk and the correlation of an asset’s returns with other assets, should be taken into consideration. Finally, the system should be able to allocate the investment proportions of all assets, and rebalance the assets to achieve efficient portfolio performance.

Studies show that there are many methodologies and models for portfolio selection [8], but does not exist an integrated framework that organizes the choice and implementation of these methodologies and models to support portfolio selection logically. Other attempts to develop a framework for portfolio selection [2,9,28] have failed at important issues such as flexibility, and a managerially oriented decision support for portfolio selection.

In the last few years, many PC-based Mean – Variance Optimization software packages become available to support portfolio selection. Rapid advance in the Web technologies and the emergence of the e-Business strongly influence the design and implementation of the financial Decision Support Systems [5,10], DSS in short. As a result, improvement in global accessibility in terms of integration and share of information [17,25] means that obtaining datum of assets from the Internet becomes more convenient nowadays. Growing demand in fast and accurate information sharing increases the need in developing Web-based information systems [11,26]. Some scientists and financial institutions have carried out research in portfolio selection and have made some progress in this area [14,21].

In this paper, we propose a framework, which addresses some issues of the existing Web DSS. It is a computer implementation that can be used by individual investors or financial organization to support portfolio selection. Our portfolio selection system based on the framework aimed at integrating user activities including asset allocation, portfolio optimization and asset rebalance and yet allows independent access of each module.

In addition, we adopt On-line Analytical Processing (OLAP) tools to handle multidimensional data structures for analytic purpose [4,23], as well as using parallel computation for fast and efficient optimization of portfolio. We use Parallel Virtual Machine (PVM) as a single computational resource from a collection of heterogeneous computers, when dealing with multiple concurrent users and large-scale computations in the case of portfolio optimization.

Based on these technologies and our proposed integrated framework, we built a prototype system named WPSS designed primarily for the Chinese financial markets. In the following sections, we give a brief introduction to the framework. Then we describe how a Web-based DSS can be built around the framework with the support for portfolio selection. We provide a brief description of the prototype system WPSS, and show the main features of this system, some of which may differ from other existing optimizers.

## 2. Proposed framework for portfolio selection

Portfolio selection process should be considered as a series of tasks, rather than just solving an optimization problem. The framework we proposed contains five main stages as shown in Fig. 1 below: asset allocation, securities analysis, securities selection, portfolio optimization, and rebalancing. We provide automatic support for portfolio selection in every stage of the framework, but decision-makers may apply their knowledge and experience to adjust the result anytime. We do not have to follow the sequence of this process, and each module can be used respectively. For example, asset analysis and selection, as a separate module, can be used to analyze and select securities, and does not need to be used with other modules together. Activities in each of these stages during the selection process are described below.

![](/api/attachments/PNJAZZKP/fulltext/images/6ea1685892076998d1dcfdc7abc3748f6faf6be8aa732d9f43bfc8bd95d4f77c.jpg)  
Fig. 1. Portfolio selection framework.

Asset allocation. This is the first stage. The system determines an optimal mix of assets, such as Large Cap stocks, Small Cap stocks, International stocks, Bonds and Cash, based on the investment profile provided by the investor. We take the investor’s preference and selection criteria into consideration, and determine his/her risk/return profile after running a strategic asset allocation analysis process. As a result, an optimal mix of assets is presented to the investor which reflects his/her financial ‘‘big picture’’, investment time horizon, and risk tolerance. At this point, the investor may interactively change his/her investment allocation, time horizon, yearly contribution, tax impact, and the amount of risk he/she is willing to take, etc.

Securities analysis. This is an important stage, which enables the investor to conduct an analysis of securities that may be considered for inclusion in a portfolio. Highlighted characteristics include price, average return, return volatility, and Sharpe Ratio for each specified securities, as well as co-relations between all specified securities. The output from this stage is a common set of parameters for each security, which can be used for comparison and analysis in subsequent stages.

Securities selection. This stage uses profiling techniques where security attributes from the previous stage are examined in advance of the regular selection process. Any security, which does not meet the predetermined criteria, such as average return, return volatility, and Sharpe Ratio, will be eliminated. The intent here is to remove any nonstarters and reduce the number of securities to be considered simultaneously in the portfolio optimization stage.

Portfolio optimization. As the main stage of the framework, portfolio optimization is to ensure optimal risk-adjusted returns by analyzing the portfolio and managing the assets. The output of this stage is an efficient frontier, and the investors can have the optimal result on the efficient frontier according to their own risk preferences. There are many comparative optimization models to be considered in this stage, such as Mean –Variance Optimization (MVO) model [16,24] that takes transaction cost (not fixed) into consideration. In the system, decision-makers can select different models according to their own preferences. Management for optimization models is discussed in Section 3.2 later. This stage can be further break down into the following five steps.

1. Asset constraints—Present asset constraints, and allows investors to set individual or group constraints on assets.

2. Asset return—Shows the portfolio’s return profile, and explains how the investor can use that information.

3. Asset volatility—Shows the portfolio’s volatility profile, and explains how the investor can use that information.

4. Asset correlation—Shows how are the portfolio’s assets correlate with others, and explains how the investor can use that information.

5. Portfolio optimization—Provides how the risk/ return profiles, correlations of portfolio assets, and any constraints the investor placed on those assets will impact the portfolio’s risk-adjusted returns; shows how to allocate the securities in order to achieve optimal portfolio.

Rebalancing. After the stage of portfolio optimization, holdings and weights of the optimal portfolio are decided, and investors may construct an optimal portfolio and make it into practice. However, rebalancing is another important part after portfolio optimization. In this stage, the investors apply their knowledge and experience to balance and make other adjustment to the portfolio by adding or deleting securities. This adjustment can help to achieve balance among the securities selected. The proportion of high-risk securities should not be too high because failure to some of these securities leads to greater danger in the overall investment. On the other hand, if the portfolio selected is too conservative, the expected return may be too low. Furthermore, balance on securities size is also important, because the commitment of high proportion of investment to a few securities can be catastrophic if more than one fails. Also, too many long-term investments may cause financing or cash flow problems.

After the portfolio has been adjusted, results can be gained by cycling back to portfolio optimization stage. Since the adjustment phase allows the consideration of issues and constrains that are new and crucial for investor, the new solution will be more satisfactory. We could say that they are ‘‘satisfying’’ rather than ‘‘optimizing’’ [1].

From previous discussion, we can see that portfolio selection process can be simplified once we break it down into several stages. Decision-makers can interactively select and change their initial investment, time horizon, yearly contribution, tax impact, and the amount of risk they are willing to take according to their own preference. Moreover, decision-makers also can use the models or methodologies or criteria in each stage, which avoids forcing the use of approaches they may not prefer. This provides more flexibility to the selection process. In the following section, we describe our prototype Web-based DSS, which supports portfolio selection based on the proposed framework.

## 3. A Web-based Portfolio Selection System (WPSS)

According to Turban [27], ‘‘A Decision Support System (DSS) is an interactive, flexible, and adaptable computer-based information system, specially developed for supporting the solution of a non-structured management problem for improved decision making. It utilizes data, provides an easy-to-use interface, and allows for the decision-maker’s own insights’’. We know that provision for continuous interaction between system and decision-makers is important [3]. On one hand, to formulate explicitly in advance all of the preferences of the decision-makers is very difficult; On the other hand, interactive decisionmaking has been accepted as the most appropriate way to obtain the correct preferences of decisionmakers [20,22]. If this interaction is to be supported by a computer-based system, then there is a need to manage the related techniques (or models), to support the data needs, and to develop an interface between the users and the system.

Fig. 2 shows a general architecture of the WPSS, and the data flow between the user interface, portfolio selection framework, optimization models and databases. Basically, this system contains the following components.

 User-friendly Interface. Used by decision-makers to input data and decision preferences, and to retrieve answers from related services. It also displays to the users and allows them to interact with the system to arrive at satisfactory solutions.

![](/api/attachments/PNJAZZKP/fulltext/images/380c346bb27528f76b26eddf32234f3b87bebe126b525bd521fd487e4e943558.jpg)  
Fig. 2. General architecture and data flow of WPSS.

 Security System. Not only used for user protection purpose, but also checks for user access levels (e. g. novice, expert, etc.) to determine the level of flexibility and interaction that the system would allow or provide.

 Portfolio Selection Framework. As described in the earlier section, it is used to aid the users along their decision-making process in a more organized fashion.

 OLAP and Multidimensional Database. Used as an add-on tool for fast user analytic purpose since Decision Support System often requires processing large amount of operational data to come up with the analytic analysis.

 Models Management Database System. Used to handle models of the many different types, which may be chosen.

 System Database. Used as a repository of historical data for all model programs and OLAP services.

## 3.1. Interaction and interface design

The structure of Browser/Server is an extension of Client/Server, and its operations adapt standard Client/Server processes. In Fig. 3, we give a threetier structure of the WPSS. At the client site, the Web browser and Java Applet handle the user interface and the presentation logic. At the server site, the Web server gets all http requests from the Web user and propagates the requests to the application server which implements the business logic of all the services for portfolio selection in this case. Communication between the Web server and the application logic can be done through CGI, ASP (used in this system) or other gateway tools. At the database server site, transactional or historical data of the day-to-day operations are stored in the system database by RDBMS. Optimization models can be maintained in a separate database. In addition, this system provides multidimensional database (MDB) for easy and fast access of summarized or analyzed data since DSS by nature requires access of large amount of operational data to find the analytic trend. Application server sends the query to the database server and gets the result set. It prepares the response after a series of processes and returns to the Web server to be propagated back to the client site.

![](/api/attachments/PNJAZZKP/fulltext/images/17165c6bc71e34ec9aba4b178bf200c2fccbc307c2630c757677aa9a7d3685f8.jpg)  
Fig. 3. Three-tier structure of WPSS.

To use this system, a new user must first register to obtain a user id and password, which will be used to authorize all further access. A registered user can log in and pick an existing session or create a new session of his/her own preference, such as level of user protection, access rights and level of complexity. User protection and session management are maintained in the security system interface level. Following with asset allocation, securities analysis, securities selection, portfolio optimization, and rebalancing modules, the system is designed in an integrated fashion and yet each module can be used independently. OLAP tool is used here as an add-on feature for user analytic purpose. In terms of system security, OLAP services add dimension-level security, so that the users could not gain any access to that dimension without security clearance. In addition, the system provides user feedback as an accessory function for the users to raise questions, have discussions, leave messages, or contact the administrators. It also provides E-mail service. We show the interface of WPSS used in the securities selection stage in Fig. 4.

![](/api/attachments/PNJAZZKP/fulltext/images/8fe0f38e933d1d8bc037d5e6f62f2954db64c660ec5a87f9e9d4e80674643ba1.jpg)  
Fig. 4. Securities selection interface.

## 3.2. Management of optimization programs

A model database is used to support variety of modeling techniques for portfolio selection optimization. Optimization programs written by us or from existing software packages can be plugged into the database for our system to use. Several popular portfolio optimization models, such as single-period MVO and multi-period MVO, are included in our model database. We also developed a model program using Java based on portfolio selection with a minimal purchase unit [12] for the Chinese financial markets. Some models in our system take transaction cost (not fixed) into consideration as well. When the users request to access the Web server, we use ASP language to manipulate database through the Open Database Connectivity (ODBC) or other special connection interfaces. Then, the system will pick an appropriate optimization program from the model database.

Fig. 5 shows a result of the portfolio optimization using single-period MVO model from an existing software package. It is generated dynamically by a Java applet from information retrieved from our system database that stores historical data. The output is an efficient frontier, and the users can have the optimal decision on the efficient frontier according to their own risk preferences.

## 3.3. An add-on tool for analytic purpose

OLAP [6,7] is an advanced information system technology for decision support. It is used to provide fast answers for dynamic analysis that aggregates large amount of data. OLAP introduces spreadsheet-like multidimensional views and graphical displays to better capture the structure of the real world data.

![](/api/attachments/PNJAZZKP/fulltext/images/c7c726ffc5847d7aaae00ef20dc805f91cf2f02f567496734093bc32cc349949.jpg)  
Fig. 5. Portfolio optimization result.

In the system, we adopt Microsoft SQL Server OLAP service 7.0 as an add-on tool to facilitate the users to make their decisions faster and easier. The system permits the users to perform complex analysis on the historical data stored in the system database. Users can read the historical data quickly and efficiently with the aid of the OLAP tool since it can provide short response time and data visualization for complex data analysis.

## 3.4. Efficient optimization via parallel computation

Portfolio optimization is an important part in the framework. When a large-scale investment is under process, the optimization method requires enormous computing time. Such situation becomes even worse if a multi-period MVO model is selected to use. It is obvious that a single computer cannot afford to handle such system load where multiple users and/or models are involved. Without enough computing capability, the response time to the users will not be tolerable. Parallel processing or the similar technology clustering computing has the potential power of reducing the computational load and enabling the efficient use of these models to solve a wide variety of problems. We choose the PVM [13] network computing environment as the high performance computing component in our system.

Since our system must consider the multi-model and multi-user issues, we use a cluster of computers interconnected together as a network parallel computing environment to maintain high performance. The network parallel computing technology has many virtues, such as high performance/price ratio, good scalability and easy management. Computers of heterogeneous system architectures can be used in a single supercomputing environment. Our parallel computing cluster is constructed behind the other system components. As shown in Fig. 6, it is made up of several PCs interconnected by a fast LAN. PVM software is installed in each computer. When the system load exceeds a predefined threshold, more computers will be added into the cluster. As the price of PCs becomes cheaper and the performance becomes higher, such network parallel computing system has outstanding characteristics.

![](/api/attachments/PNJAZZKP/fulltext/images/02567289e60bcfd934146b7af7fc3c8341bb970366711b37bfbdca3039c6eaa2.jpg)  
Fig. 6. Parallel computing environment.

In general, data for the optimization models can be collected from other databases, directly from the optical fiber, or other resources like Internet/Intranet. Currently, our data are collected from the historical data stored in databases. All the collected data are dispatched through a data dispatcher component (a PVM task) and it is used for the load balance purpose, i.e. to provide each computer in the cluster with almost even number of data. The optimization models have many matrix operations. PVM is suitable for these operations. When the dimensions of decision variables exceed a critical limit, such technology can greatly improve the system performance. Optimization computations are accomplished via a number of collaborated processes distributed to the different computers in the cluster. PVM is used for the interprocess communication and process control. The results of the computation are stored in the database and can be accessed by other subsystems. The multiuser problem is also handled by the PVM tasks. When the user invokes his portfolio selection, several PVM tasks will be constructed and put to the bag of tasks. They are queued and emitted one by one whenever a computer is available. Multi-server coordination and sharing of workload are other critical problems we have taken into consideration [4,28]. We setup a system management task, which takes in charge of all the working units in the system and makes them work properly.

## 4. Implementation and characteristics of WPSS

Based on a three-tier structure, our portfolio selection system can run on both the Internet and Intranet environments. The user can use a Web browser to access our Web server through HTML language and HTTP protocol. The kernel of the system is placed on the Web server. ASP and Java technologies are used extensively and well integrated in the system. Moreover, with the use of integrated Web application development tool—Interdev, network operation system—Windows 2000 and database server—MS SQL Server 7.0, the system is well developed. The software of the system is as follows:

<table><tr><td colspan="2">(1) Software in server</td></tr><tr><td>Network operation system</td><td>WINDOWS 2000 SERVER (NT 5.0)</td></tr><tr><td>Database server</td><td>MS SQL SERVER 7.0</td></tr><tr><td>Web server</td><td>MS IIS 4.0</td></tr><tr><td>Mail server</td><td>www.software.com, Post office v3.5</td></tr><tr><td colspan="2">(2) Software in client</td></tr><tr><td>Desktop OS</td><td>WINDOWS 9X</td></tr><tr><td>Browser</td><td>Internet Explorer 4.01 (or higher edition)</td></tr><tr><td colspan="2">(3) Development tools</td></tr><tr><td>Visual InterDev 6.0(Integrated Web application development tool); ASP (JavaScript and VBScript), Java</td><td></td></tr></table>

Compared to other existing portfolio selection systems, such as http://www.morningstar.com and http://www.effisols.com, our system is integrated, high performance and user-oriented. It differs from the others mainly in the following areas.

 We provide an integrated framework for portfolio selection that is adaptable to the needs of financial organizations and individual investors. Other attempts to develop a framework for portfolio selection, have failed at important issues such as flexibility, and a managerially oriented decision support for portfolio selection.

 The system is easy to be expanded. Since the criterion concluded in the asset analysis and selection module may not be adequate or typical, advanced users are also given the right to modify them. Because modification is done directly to the server database, after refreshing, the on-line user can see the updated items. The advantage is that modification of the system no longer depends on the source code by programmer, and maintenance of the system can be done from remote place. Hence, meets the expectation of the investor much better.

 The system is modularized. For example, asset analysis and portfolio optimization in this prototype can be used separately. Problems to be solved in each module can be chopped smaller.

 We provide some portfolio optimization models in our system, and decision-makers can select the model according to their own preferences. This system also allows models to be selected from simple to complex.

 As the portfolio optimization stage is an important part in the framework and it will cost a lot of computational resources and times, we apply parallel computing technology to achieve fast optimization.

 We also adopt OLAP services as an add-on feature in this system to provide multidimensional analysis to the users.

 The system is mainly designed for Chinese financial organizations and individual investors. Some methods and models are suitable only to Chinese financial markets.

## 5. Discussions and conclusions

This paper briefly introduced an integrated framework for portfolio selection and implementation of the framework for Web-based DSS. Based on the proposed framework and the technologies of OLAP and PVM, we construct a prototype Web-based Portfolio Selection System, which not only integrates asset allocation, portfolio optimization, and asset rebalancing, but also improves the overall performance of the optimization process as well as providing a more organized and user-friendly interface particularly oriented for decision making of financial market investments. Our approach is not intend to prescribe certain portfolio, but rather to assist decision-makers to find an efficient portfolio, which is close to optimal, and at the same time satisfies any constraints that have been imposed.

In the process of selecting an efficient portfolio, the optimization model plays an important role. Portfolio theory has been developed rapidly since Markowitz introduced his pioneering work on portfolio selection in the 1950s, and many optimization models have been developed since. However, lots of problems remain to be solved, such as, the problems with transaction cost, multi-period, and incomplete information. Moreover, some of the existing methodologies and models are not widely used because they are too complex and require lots of input data, they may be too difficult for decision-makers to understand and use, or they may not be used in an integrated fashion. Among all of the processes of portfolio selection, optimization techniques are the most fundamental tool for portfolio selection. However, they have failed to gain user acceptance mainly due to the fact that they prescribe solutions to portfolio selection problems without allowing interactive and flexible operations from the decision-maker.

WPSS is based on our proposed framework, which supports the flexible and interactive approach in system design and implementation since users can choose their own methodologies or optimization models according to their own requirements, and expand the system to meet their own needs. The system provides ease of use as well as fast response time, which we believe is critical to all users especially executive decision-makers. Since portfolio optimization is a very important part of the system, when dealing with concurrent multi-user and large-scale computation, the system users PVM to handle the situation more efficiently. We also adopt OLAP service as an add-on feature to provide multidimensional data view and graphical display for user analytic purpose.

Although lots of tests show that WPSS is a useful tool, problems must also not to be ignored. A major issue for most optimizers on the Internet is selecting historical data as input data. The simplest way to convert N years of historical data into MVO inputs is to make the hypothesis that the upcoming period will resemble one of the N previous periods, with a probability 1/N assigned to each. When we use historical data to provide the MVO inputs, we implicitly assume that:

 the returns in the different periods are independent;

 the returns in the different periods are drawn from the same statistical distribution;

 the N periods of available data provide a sample of this distribution.

However, these hypotheses may simply be false. The most serious inaccuracies arise from a phenomenon called mean reversion, in which a period, or periods, of superior (inferior) performance of a particular asset tend to be followed by a period, or periods, of inferior (superior) performance. Suppose, for example, we have used 5 years of historical data as MVO inputs for the upcoming year, the outputs of the algorithm will favor those assets performed well over the past 5 years with highly expected return. Yet if mean reversion is in effect, these assets may well turn out to be those that perform most poorly in the upcoming year.

Moreover, standard deviation as an estimation of risk is not completely appropriated [18], which limit the potential of lots of optimization models because of the deficiency of themselves. Other decision-making models may be good alternatives [15].

Portfolio selection system has been used in some countries, and has been proven to make great profits for investors. However, it is still a new research area in China, full of questions, full of challenges. With the fast expansion of the Internet, developing on-line portfolio selection system has gained more and more interests from researchers all over the world.

## Acknowledgements

Supported by a joint research grant from RGC of Hong Kong and NSFC (Grant #N\_CityU 102/01), and a research grant from City University of Hong Kong (Grant #7001040), NSFC and MADIS. The authors are grateful to the two referees for their very valuable comments and suggestions.

## References

[1] N.P. Archer, F. Hasemzadeh, Project portfolio selection through decision support, Decision Support Systems 29 (2000) 73 – 88.

[2] W.J. Bernstein, D. Wilkinson, Diversification, Rebalancing and the Geometric Mean Frontier, Research manuscript (1997).

[3] R.O. Briggs, J.F. Nunamaker, R.H. Sprague, 1001 Unanswered research questions in GSS, Journal of Management Information Systems 14 (1997) 3 – 21.

[4] S. Chaudhuri, U. Dayal, V. Ganti, Database technology for decision support systems, Computer, January (2001) 48 – 55.

[5] S.C.T. Chou, Migrating to the web: a web financial information system server, Decision Support Systems 23 (1998) 29 – 40.

[6] E.F. Codd, S.B. Codd, C.T. Salley, Providing On-line Analytical Processing to User-Analysts: An IT Mandate, E.F. Codd and Association, 1993.

[7] E.F. Codd, S.B. Codd, OLAP with TM/1, E.F. Codd and Association, 1994.

[8] X. Deng, S.Y. Wang, Y.S. Xia, Criteria, models and strategies in portfolio selection, Advanced Modeling and Optimization 2 (2000) 79–104.

[9] J.C. Dong, X. Deng, S.Y. Wang, Y. Nakamori, Portfolio selection based on the internet, System Engineering: Theory and Practice 12 (2002) 73–80.

[10] M. Fan, J. Stallaert, A.B. Whinston, Implementing a financial market using Java and Web-based distributed computing, IEEE Computer 32 (1999) 64 – 70.

[11] M. Fan, J. Stallaert, A.B. Whinston, The internet and the future of financial markets, Communications of the ACM 43 (2000) 82 – 88.

[12] Y. Fang, S.Y. Wang, K.K. Lai, Portfolio Rebalance with Transaction Costs and A Minimal Purchase Unit, MADIS working paper, MSPS-E-01-07, CAS, Beijing (2001).

[13] A. Geist, A. Beguelin, J. Dongarra, W. Jiang, R. Manchek, V. Sunderam, PVM: Parallel Virtual Machine A Users’ Guide and Tutorial for Networked Parallel Computing, MIT Press, Cambridge, MA, USA, 1994.

[14] M. Hirschey, V.J. Richardson, S. Scholz, Stock-price effects of internet buy – sell recommendations: the Motley Fool Case, The Financial Review 35 (2000) 147 – 174.

[15] H. Latane, Criteria for choice among risky ventures, Journal of Political Economy 67 (1959) 144 – 155.

[16] Z.F. Li, Z.X. Li, S.Y. Wang, X.T. Deng, Optimal portfolio selection of asset with transaction costs and no short sales, International Journal of Systems Science 32 (2001) 599 – 607.

[17] Z.M. Li, Internet/Intranet technology and its development, Transaction of Computer and Communication 8 (1998) 73– 78.

[18] J.C.T. Mao, Survey of capital budgeting: theory and practice, Journal of Finance 25 (1970) 349– 360.

[19] H.M. Markowitz, Portfolio selection, Journal of Finance 7 (1952) 77–91; Mean – Variance Analysis in Portfolio Choice and Capita Markets, Basil Blackwell, New York, 1987.

[20] R.G. Mathieu, J.E. Gibson, A methodology for large scale R&D planning based on cluster analysis, IEEE Transactions on Engineering Management 30 (1993) 283 – 291.

[21] R.Z. Mehdi, R.S. Mohammad, A web-based information system for stock election and evaluation, Proceedings of the International Workshop on Advance Issues of E-Commerce and Web-Based Information Systems, 1998.

[22] K. Mukherjee, Application of an interactive method for MO-LIP in project selection decision: a case from Indian coal mining industry, International Journal of Production Economics 36 (1994) 203 – 211.

[23] T.B. Pedersen, C.S. Jensen, Multidimensional database tech nology, Computer (January 2001) 40 – 46.

[24] A.F. Perold, Large-scale portfolio optimization, Management Science 30 (1984) 1143– 1160.

[25] M.S. Ralph, W.R. George, Principles of Information System, A Managerial Approach, China Machine Press, Beijing, China, 2000.

[26] K. Saatcioglu, J. Stallaert, A.B. Whinston, Design of a financial portal, Communications of the ACM 44 (2001) 33– 38.

[27] E. Turban, Decision Support and Expert Systems, 4th ed., Prentice-Hall, Englewood Cliffs, NJ, 1995.

[28] D.A. Wood, Three-stage approach proposed for managing risk in exploration and production portfolios, Oil & Gas Journal 23 (2000) 69–72.

![](/api/attachments/PNJAZZKP/fulltext/images/ecf7baa105c40cba68fd3e468f6a68f18c72510b8ee1a3dce7051eb327b97bcd.jpg)  
Jichang Dong is a PhD student at Institute of Systems Science, Chinese Academy of Sciences (CAS). His current research interests include financial engineering and decision support systems.

![](/api/attachments/PNJAZZKP/fulltext/images/6401467d9770c8dfa2ed76c6fee4b7a758f81e2e4719a1b8ce2c841f4b104708.jpg)

Du Helen Songhua is currently a Master of Philosophy student at Department of Computer Science, City University of Hong Kong. She received her Bachelor of Arts Honors degree major in Computer Science from York University, Canada. Her research interests include distributed computing technologies and their applications on the Web, heterogeneous system or data Integration and Interoperation, and intelligent decision support systems.

Shouyang Wang received the PhD degree in Operations Research from Institute of Systems Science, Chinese Academy of Sciences (CAS), Beijing in 1986. He is currently a Bairen distinguished professor of Management Science at Academy of Mathematics and Systems Sciences of CAS and a Lotus chair professor of Hunan University, Changsha. He is the editor-inchief or a co-editor of 12 journals. He has published 18 books and over 120 journal

![](/api/attachments/PNJAZZKP/fulltext/images/15414ff699cd0842b3a8dfbb4ccb425cff3da0856088c62c2dc91d17a97b2331.jpg)

papers. His current research interests include financial engineering, e-auctions and decision support systems.

![](/api/attachments/PNJAZZKP/fulltext/images/ccc90a77d36b3914552d017c7f9a13d6ddd0fd75b59a752b87af505667ba4e38.jpg)

![](/api/attachments/PNJAZZKP/fulltext/images/cf5451fce590d9b185f84b95824f2a455df91bd45a55a5b0b84afebec5a7edc9.jpg)

Chen Kang is a PhD candidate at Department of Computer Science and Technology of Tsinghua University in Beijing, China. He received his Bachelor’s degree in 1999 at Tsinghua University.

Xiaotie Deng received his Bachelor’s degree from Tsinghua University and Master’s degree from Chinese Academy of Sciences, both in Beijing China. He received his PhD from Stanford University in 1989. Since then, he worked at Simon Fraser University and York University, Canada. He is now professor in computer science at City University of Hong Kong. His current research interests are in algorithms and application systems associated with internet economics, finance and E-commerce.
