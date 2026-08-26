---
otero_id: 16887
otero_key: "STRSPE8B"
title: "Decision support for integrated cash management"
authors: "Venkat Srinivasan; Yong H. Kim"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90005-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision Support for Integrated Cash Management

Venkat SRINIVASAN \* and Yong H. KIM $^{+}$ \* Northeastern University, Boston, MA 02115, USA, $^{+}$ University of Cincinnati, Cincinnati, OH 45221, USA

Cash management has attracted the increasing attention of both academicians and practitioners in recent time. The expanding role and responsibilities of cash managers and corporate treasurers is likely to increase the focus on cash management as a vital organizational function. Academic research, however, has primarily focused on providing analytical tools to solve well structured problems that are relatively isolated in nature. Conspicuously, no attempt has been made to integrate the various sub-problems of cash management explicitly recognizing interrelationships among the sub-problems as well as between the sub-problems and other financial decisions. More importantly, there is an even greater need to provide a framework that in addition to recognizing the above interrelationships will enable the cash manager to recognize a more inclusive set of dependencies that exist in practice.

Decision support systems have the potential to overcome the above deficiencies to a significant extent. This paper is aimed at providing a conceptual framework for designing an effective model-based decision support system (DSS) for integrated cash management. The framework should form a useful basis for any attempts at designing computer-based support systems for cash management.

Keywords: Decision support systems: model-based, financial, working capital, Cash management: cash balance, cash gathering, cash mobilization, cash concentration, cash disbursement, infrastructural decisions, operational decisions.

![](/api/attachments/STRSPE8B/fulltext/images/95ba023624c18e3d5d609ca98bd9c0c75b9231c92620ac83373324b04e0bc401.jpg)

Venkat Srinivasan, Ph.D., is an Assistant Professor of Finance at Northeastern University. His primary research interests are in the area of integrating artificial intelligence, expert systems, and decision support concepts with normative financial theories. He is now working with several Fortune 500 corporations to design expert systems for various facets of working capital management. Dr. Srinivasan received his B. Com degree at the University of Delhi in 1975, his

C.A. degree from the Institute of Chartered Accountants of India in 1981 and his MBA and Ph.D. degrees in Finance from the University of Cincinnati in 1985. His recent publications have appeared in OMEGA, Journal of International Business, Studies, Computers and Operations Research, among others. Dr.

## 1. Introduction

Cash management has increasingly begun to attract the attention of both academicians and practitioners in recent time. On the academic side, the most significant recent events have been the establishment of a research annual [46] and the organization of a Symposium on Cash, Treasury and Working Capital Management [121] as a forum to foster research in the area. On the practical side the increasing interest and awareness of the importance of cash management has led to the formation of National Corporate Cash Management Association (NCCMA) in 1980, which now has reportedly over 2,800 members and sponsors a widely read journal, the Journal of Cash Management. Further, the expanding role and responsibilities of cash managers and corporate treasurers is likely to increase the focus on cash management as a vital organizational function. Evidence toward this trend lies in the current debate on whether cash management should be treated as a profit center [22].

A review of the academic literature on cash management reveals that academic research has primarily focused on providing sophisticated analytical tools to solve problems that are for the most part well structured and relatively isolated in nature. Numerous cash flow planning models have evolved, ranging from inventory-type models [4,7], to linear, mixed-integer linear and dynamic programming formulations and control-limit models (see, e.g., [13,26,56,72,76,83,108]), and finally, some recent approaches suggest the use of network flow programming [35,67,92,93]. $^{1}$ Almost all these models are attempts to apply computing techniques to isolated sub-problems of cash management, e.g., lockbox locations, transfer scheduling, etc., and implicitly assume that the development of an appropriate solution procedure is all that a cash manager needs to resolve the issues faced in practice. $^{2}$

![](/api/attachments/STRSPE8B/fulltext/images/2c1b950e0434cdb5d0c42c29d63fe7c825e49dbdb044c780f8dacfaebab3a587.jpg)  
Soong Jun University, two graduate degrees, respectively, in Operations from Seoul National University and in Finance from Virginia Polytechnic Institute, and his doctoral degree in Finance from the Pennsylvania State University. Dr. Kim is also the editor of Advances in Working Capital Management, a research annual series published by JAI Press.

Conspicuously, no attempt has been made to integrate the various sub-problems recognizing interrelationships among the sub-problems as well as between the sub-problems of cash management and other financial decisions, both short- and long-term. More importantly, there is an even greater need to provide a framework that in addition to allowing for interrelationships will enable the cash manager to recognize a more inclusive set of dependencies that exist in practice. These may include organizational constraints, formal and informal information flows, and the firm's strategies and policies.

Indeed one of the most conspicuous weaknesses of normative financial theory is the absence of a linkage between normative prescriptions and the firm's strategic focus. There is a need to provide a modeling framework that will facilitate proactive modeling by managers. Additionally, approaches to model building and problem solving in financial management in general appear to have remained as predominantly academic exercises perhaps mainly due to their inherent complexity and difficulty of usage. $^{3}$

The tremendous progress in micro-computer technology has changed this situation rather dramatically. It is now possible to design decision support systems that will not only allow the evaluation of the numerous decisions involved in cash management but also provide for the recognition of interrelationships among the decision variables. Further, the system can also be designed so that the manager could recognize various constraints and policies as well as desired strategies and objectives. Additionally, by making the system conversational and interactive, the system can enable the manager to easily design strategies, thus, lending a proactive element to the system. The system can also help to narrow the gap between theory and practice by hiding the complexity and eliminating the difficulty of using normative models.

The purpose of this paper is to conceptualize and illustrate an approach to the design of an effective model-based DSS for cash management. $^{4,5}$ The remainder of this paper is organized as follows. The next section attempts to define a framework for designing an effective DSS for the purposes of this paper. The definition is based on an exhaustive review of the DSS literature. The framework is then specifically related to cash management in section 3. $^{6}$ Section 4 integrates the decision process, models and information needs identified in section 3 to provide a normative model-based approach for the design of a cash management DSS. The paper concludes with a summary.

## 2. Decision Support Systems

## 2.1. What is a DSS?

Scott Morton [81] first articulated the concepts involved in what has since come to be designated as 'Decision Support Systems'. A DSS is defined as a computer-based system designed to support and improve the effectiveness of managerial decision making. Evidence indicates that there is a growing interest among corporations to understand and develop DSS for supporting decision making. The increasing popularity of DSS can be ascribed to developments in interactive graphic terminals, on-line direct access systems, time-sharing and mini- and microcomputers, and software developments in data base management systems (DBMS).

Although it is easy to identify examples of DSS in terms of their characteristics, a formal definition and uniform generalization of their capabilities have proved to be a much more difficult task. The unavoidable confusion with 'DSS' as with any new terminology is that it means different things to different people. Suggested definitions in the literature cover a very broad spectrum from a narrow to a loosely defined focus. On the narrow end of the spectrum, a DSS is defined as an interactive, computer-based system that supports managers in making unstructured decisions, i.e., decisions which have not been or are incapable of being analyzed using any type of structured approach or procedure because the decision environment is to a high degree indeterminate. On the other end of the spectrum, a DSS is very loosely defined as any system that supports a decision. Neither approaches are generalizable enough to help us in specifying and designing new systems. However, as research and practice in DSS have evolved, it is now recognized to be a system that supports all the relevant aspects of a decision process or processes. The extent of support could range from being purely descriptive in the case of unstructured aspects to being prescriptive in the case of structured aspects.

We present in exhibit 1 the framework adopted in this paper to conceptualize a cash management DSS. The framework is a result of an exhaustive review of the DSS literature. The first step is to identify the decision processes to be supported. The next step is to study the decision processes

Steps:

![](/api/attachments/STRSPE8B/fulltext/images/2dfaeb86653163e0551d188c79ab64110de62c00cc21c588caa20dddc65c24d1.jpg)  
Exhibit 1. A General Framework for Designing Effective DSS.

identified. Since the objective of the paper is to define a normative DSS, we base our identification of the decision processes on the relevant normative literature. However, the framework presented does recognize that the typical normative approach in cash management does not allow the decision maker to explicitly and systematically integrate the evaluation of strategic and other important qualitative factors. The review of the normative literature will yield modeling methodologies which will form the basis for the model support in the DSS. Simultaneously, the developer has to identify an appropriate DSS data base environment. Interface management systems and dialog system design also are accomplished in this step. The final step reflects the fact that DSS design is an iterative process. Previously unidentified needs are bound to surface during implementation and later. A successful DSS is one where the design is flexible enough to allow changes, where necessary.

Further, in exhibit 2, a structural definition of a DSS is presented. The typical DSS can be defined to consist of three sets of components: a model base, a data base, and interface management systems. Exhibit 2 indicates that the model base can be designed using a DSS generator, DSS tools or both. The data base may contain the data needed for the decision processes that the DSS is designed to support, and the sources can be broadly categorized as: transactional, internal non-transactional and external. The interface management systems are shown to comprise three sub-components: model management systems, data base management systems and dialog management systems. In the next section, we attempt to relate the stepwise DSS development process and the structural definition of DSS to cash management.

![](/api/attachments/STRSPE8B/fulltext/images/9ed9bdd9fb11e5543a39e0b2237314e690c2c627cfc50acebdeba3cfad69450f.jpg)  
Exhibit 2. Components of a Decision Support System (DSS).

## 3. Cash Management DSS (CMDSS)

The process of studying cash management could begin by seeking answers to several questions. What does the cash manager do? What kinds of decisions does the literature suggest the cash management team take? Broadly, the cash management function has the responsibility to mobilize, control and plan the firm's cash resources. The responsibilities could be viewed from strategic, tactical and/or operational perspectives. A study of the normative literature on cash management reveals that the cash management decision process can be decomposed into five major decision types: (i) cash balance management, (ii) cash gathering, (iii) cash mobilization and concentration, (iv) cash disbursement, and (v) banking system design for credit services. Within four of these major decision types, a number of subproblems can be identified:

(i) Cash balance management
- cash position management
- cash forecasting
- investment of surplus cash
- borrowing to meet cash deficit

(ii) Cash gathering
- in-house processing
- lockbox location

(iii) Cash mobilization and concentration
- design of concentration systems
- choice of fund transfer mechanisms
- cash transfer scheduling

(iv) Cash disbursement
- disbursement system
- disbursement techniques

Each of the above decision types is discussed next.

## 3.1. Cash balance management

## 3.1.1. A Study of the Decision Process

One of the primary responsibilities of the cash management function is the maintenance of what are perceived to be optimum cash balances. In any company this activity will require that the cash manager first assess the available resources at the beginning of the planning or operation horizon under consideration. This may be done with the help of balance reporting services offered by firm's bankers and internal reporting systems. Forecasts on receipts and disbursement will then have to be integrated with this assessment of available resources. The firm will typically have internal reporting systems requiring each of the collection and disbursement locations to submit forecasts of receipts and payments, respectively.

Such position management is usually done on a rolling basis. For example, estimates and forecasts may be submitted on a daily basis for the next 5 days, on a weekly basis for the next 3 weeks and may be on a monthly basis for the subsequent 2 months. These reports may be updated daily on an exception basis to allow comparison of actual with estimates as well as to revise the subsequent estimates where such revisions are indicated.

Based on approved funding requests, transfers are initiated to various locations. The cash manager now has an idea of the firm's cash position as of the end of the previous day and has estimates of the current day's cash position and the cash position of subsequent periods depending on the periodicity of the rolling budget adopted. Initiating the required transfers to locations would also signal the need to either borrow or invest. Exhibit 3 illustrates the cash balance management decision process and the interrelationships between the identified segments.

Two aspects in exhibit 3 merit additional explanation. First, exhibit 3 recognizes that strategic and policy input may necessitate a change in the minimum cash balances or other related decisions. Secondly, the cash manager needs to determine how much of the surplus (deficit) is relatively permanent and how much of it is relatively temporary. This is because while a temporary cash surplus or deficit will necessitate evaluation of short-term investment or borrowing alternatives, a permanent surplus or deficit will require that long-term financing alternatives also be explored.

Depending on the size of the firm, the cash manager may have a number of borrowing alternatives. The major types of short-term borrowing include, short-term bank loans, commercial paper, bankers' acceptances, and master notes. The cash manager has to obviously select the optimal mix of borrowings from the sources available. There is also a need to analyze and evaluate lender performance. The firm may require some routine transaction reports giving breakdown of the activities, amounts, maturity schedules, and costs of short-term borrowing activity. The firm may also desire analytical reports on lender performance to help evaluate the lender mix employed. $^{7}$

![](/api/attachments/STRSPE8B/fulltext/images/042e851f8fed886d89b31ed92e666a21379cd061c427b4767d72b6c6fdfc1b1b.jpg)  
Exhibit 3. Cash Balance Management Decision Process.

There are a number of short-term investments available to the company depending on the amount to be invested and the proposed length of the investment. $^{8}$ The major short-term investment instruments include certificates of deposits issued by major banks, commercial paper issued by major corporations and bank holding companies, U.S. government securities, and time deposits with commercial banks. A common method of completing short-term investment transactions is to execute a repurchase agreement (repo) with the other party to the transaction, usually a bank or broker. It is also possible to establish an ‘open’ repo to accommodate uncertainty with respect to the length of the temporary surplus balances.

For a firm that is active in investing in the short-term, such activity must be governed by some broad policy guidelines such as the types of investments that are not acceptable, the maximum investment in dollars that can be made in any one type of security and a periodically updated approved security list. As in the case of short-term borrowing, the cash manager may require a number of reports covering the activities, maturities and investment profiles.

The purpose of cash forecasting is to provide estimates of future receipts and disbursements. Such information is crucial for cash balance management and helps plan short-term finances for the firm. Approaches to forecasting can be classified into two groups: traditional and statistical. The traditional approach is usually based on an aggregation of location-wise estimates whereby the individual locations generate estimates of receipts and disbursements over a planning horizon. These forecasts are then aggregated into a proforma cash budget which is a crucial input to the cash position planning process. Statistical approaches could range from the relatively simple payment pattern approach to the more sophisticated markovian chain or Box-Jenkins methodologies. $^{9}$ There is no single approach that is the best for all corporations. The most appropriate approach would depend on the particular circumstances of each case. In practice, however, many firms rely on the aggregative approach and aggregate forecasts from various locations into proforma cash budgets.

An important analytical process subsequent to forecasting is one of comparing actual performance with forecasts. This is an important but completely neglected aspect of cash balance management. Variance analysis techniques from standard costing can be relatively easily adopted for the purpose. While the only recognition of the need for variance analysis, in the literature appears in [44, p. 8], there is no mention of any specific variance that the cash manager can examine to isolate and localize the reasons for significant deviations. $^{10}$

## 3.1.2. Analysis of Information Requirements

The information requirements for cash balance management can now be identified. In determining available and required resources, the cash manager requires information on balances, forecasts of receipts and disbursements and required fund transfers. Part of this information may be provided by the banks and the remaining may have to be generated internally. Deciding on the appropriate short-term investing mix requires a host of financial market information and details of company policies. The review and analysis process leading to changes in the approved security list may in turn necessitate the procuring of a variety of information on the securities being evaluated.

Similarly, the short-term financing decision requires information on available alternatives including qualitative information such as company policies with respect to short-term borrowing. Use of statistical forecasting techniques will require historical and future information on various factors depending on the technique used. Variance analysis will require detailed information on the assumptions underlying the forecasts and the corresponding actual data. In addition, the firm's strategies and policies and other constraints that directly or indirectly have an impact on cash balance management should also be available as part of the DSS data base or some other source.

## 3.1.3. Analysis of Modeling Requirements

The cash balance management decision type may require a number of models depending on the approaches to be adopted for the underlying decision segments. The determination of optimal transfer schedules and transfer modes from both deposit banks to concentration banks and from concentration banks to disbursement banks can be determined by designing a mathematical programming model (see, e.g., [13,35,60,67,72,92]). The model can be expanded to determine the optimal investment or borrowings, as the case may be. Since the number of short-term investment alternatives are likely to be numerous, this may result in a very large mathematical program with substantial computational complexity. Besides, in the case of many firms, several strategic and qualitative factors are likely to have a substantial influence on the final decision. To overcome computational complexity, a screening process may be used to prune the lists of available alternatives to a reduced set of feasible alternatives. Further, the impact of strategic and other relevant qualitative factors can be explicitly integrated with the expected return from the alternatives by adopting a multi-attribute modeling approach (MADM), e.g., the Analytic Hierarchy Process (AHP). $^{11}$ The variance analysis component of this decision type will require a model that can identify the desired variances. Once the desired variances are identified, a variance analysis model can be implemented as a relatively simple spreadsheet. While aggregative forecasting will not need any formal models, an appropriate model will be needed if statistical approaches are used.

## 3.2. Cash Gathering

## 3.2.1. A Study of the Decision Process

Cash gathering refers to the collection of customer remittances and the movement of these remittances to some focal point, frequently called the corporate concentration center. Efficient gathering is important since it determines the amount of funds available to the firm for use in operations and additionally, any unnecessary delay also entails an opportunity cost to the firm. Large companies may have several regional concentration banks in addition to the corporate concentration bank. Two common modes exist for collection of customer remittances. The first is to have the local branch of the firm collect the check from the customer and deposit it into a local bank with instructions to transfer to a concentration bank. The second is to instruct the customer to mail the remittance to a lockbox operated by a bank offering lockbox services. While most companies use lockboxes, the mode used essentially depends upon the size of remittance and geographical location. Thus, the check collection system design revolves around lockbox locations and local branches.

The purpose of a lockbox service is to provide a mail intercept point to reduce float. The establishment of effective lockbox networks has enabled companies to greatly reduce mail time involved in remittances. The overall objective to the cash gathering decision type are to design an efficient collection system comprising lockboxes and in-house processing centers. A corollary decision involves the assignment of customers to a specific collection center. Exhibit 4 presents the cash gathering decision process. The evaluation of existing collection system design or alternative designs can be done periodically and/or when substantial changes are observed in remittance patterns. Exhibit 4 also clearly suggests that the selection of lockboxes and in-house collection centers has to be done simultaneously.

## 3.2.2. Analysis of Information Requirements

The emphasis in the literature relating to cash gathering systems has been misplaced on solution algorithms. Data requirements of such systems have not been addressed. The cash gathering decision process requires a vast amount of information. Some of the information, however, can be extracted from transactional data bases. Specifically, the following types of information will be required: (i) the mail and availability times relating to group i and collection center j for the existing system as well as alternative that are being evaluated, (ii) the total amount of incoming funds from each group i, (iii) the fixed and variable costs associated with the firm's present and proposed systems for processing group i's checks through collection center j, and (iv) the firm's cost of capital. Additionally, information will also be required on the actual mail and clearing times, actual volume and dollar amount of checks processed through various collection centers so that the effectiveness of the system can be continually evaluated.

![](/api/attachments/STRSPE8B/fulltext/images/4bdeacdc5da19e67ec07e8def48bafa864cf7223cd37c19e61f0b3366889048c.jpg)  
Exhibit 4. Cash Gathering Decision Process.

## 3.2.3. Analysis of Modeling Requirements

The problem of choosing the best set of collection alternatives has been studied extensively by management scientists. Research has produced a number of solution procedures that have in fact been used by banks in lockbox studies. $^{12}$ The mathematical programs to solve real life lockbox location problems are large combinatorial problems that are computationally complex. Many heuristic alternatives have been proposed. Typically, lockbox studies are done by banks with specialized cash management consulting staff. However, if a CMDSS is designed, such analysis can be done internally. This will require mathematical programming models. Further, customer remittance patterns can be analyzed by traditional management information reports extracted from internal transactional data.

## 3.3. Cash Mobilization and Concentration

## 3.3.1. A Study of the Decision Process

Banks at which remittances are first credited to corporate accounts are called deposit banks. For many companies, collections in deposit banks are of little value mainly because these deposits earn typically little or no interest. Therefore, companies move such funds through the banking system to more aggregate levels in the structure to banks that are known as concentration banks. Such accounts primarily exist at money center banks or banks that are part of the corporation's credit line consortium.

The mobilization and concentration decision type involves three aspects. The first relates to the selection of the optimal set of concentration banks. A second decision aspect of this decision process is that of selecting the appropriate transfer mechanism. This selection is based on the forecasts of inflows and outflows for the decision horizon. Typically, corporations have the choice of three transfer mechanisms: depository transfer checks (DTCs), automated clearing house (ACH) transfers, and wire transfers (WTs). $^{13}$ The typical approach to selecting the appropriate mechanism is to determine the least cost mechanism based on the size of transfer and the opportunity cost of capital.

The third related decision is that of determining the frequency of transfers for the decision horizon based on forecast data. The transfer mechanism selection and transfer scheduling decisions, even though based on forecast data for the decision horizon, are required as inputs to determine the optimum set of concentration banks. The decision process is illustrated in exhibit 5.

## 3.3.2. Analysis of Information Requirements

A non-exhaustive list of information requirements include: (i) information on deposit and disbursement banks, (ii) potential concentration banks and alternative designs, (iii) cost and benefit information on alternative designs, (iv) mail and availability times from deposit banks to concentration banks and from concentration banks to disbursement banks for each of the alternatives, (v) costs and availability times for each of the transfer mechanisms, (vi) non-financial benefits from banks and transfer mechanisms, if any, and (vi) collection and disbursement data. Further, the computation of variances will require actual information on all the above parameters.

![](/api/attachments/STRSPE8B/fulltext/images/90511a07af5d59112fb3201565a17903ee11cef49ec9106ebb174a83bbf93c69.jpg)  
Exhibit 5. Cash Mobilization and Concentration Decision Process.

## 3.3.3. Analysis of Modeling Requirements

Mathematical programming formulations have been suggested for use in selecting concentration banks and for optimal transfer scheduling $[115,116]$ . The formulations simultaneously yield an optimal set of concentration banks as well as transfer schedules. The formulations, however, suffer from one major weakness. They imply that the transfer scheduling and mechanism selection issue is static and fixed at the time of selecting concentration banks. In other words, they seem to imply that for the two sets of decisions to be optimal, they need to be determined simultaneously. But, in reality, while an optimal concentration system design cannot be determined without transfer scheduling and mechanism selection data, the converse is not true. Transfer scheduling and mechanism selection decisions can be dynamically revised as changes occur in forecasted cash flows. The concentration system design process can, therefore, be supported by a mathematical programming model that will allow the determination of optimal concentration banks, by considering the optimal transfer scheduling and mechanism selection decisions based on forecast data for a given horizon.

## 3.4. Cash Disbursement

## 3.4.1. A study of the Decision Process

We can identify the following major decision types within this decision process: (i) disbursement site selection, (ii) assignment of disbursing banks to concentration or funding banks, (iii) funding method, and (iv) transfer mechanisms. The objective of maximizing disbursing float is at the core of disbursement site selection decisions. Disbursement float is comprised of mail and presentation float. The effect of extending the mail float or presentation float can, of course, be nullified if the vendor recognizes actual receipt of funds in his bank as the date of payment. However, since not all of the vendors may be in a position to enforce such strict credit policies, attempting to maximize disbursement float may be a feasible idea for many companies.

The disbursement site selection is very similar to the lockbox location decision. From a representative sample of checks issued by the firm, the average clearing times are estimated for the existing disbursing system. Using a data base of nationwide average clearing times and using appropriate optimization or heuristic procedures, the firm can then determine a set of disbursing banks and also assign vendors to such banks. The decision process is illustrated in exhibit 6. Like lockbox studies, most disbursement studies are usually done by banks on the request of their clients.

The second related decision type within this decision process is that of choosing an appropriate funding method. There are three major funding methods: (i) staggered funding, (ii) controlled disbursing, and (iii) zero balance funding. Controlled disbursing and zero balance funding are not mutually exclusive. Staggered funding involves estimating the clearing pattern of checks issued and funding is based on the clearing time estimates. Under controlled disbursing, disbursements are not funded until the day checks are presented for payment. The drawee bank is located in such a location that the day's presentments can be funded the same day. Zero balance funding essentially refers to the collection of banking activity within the same branch such that funding for the disbursing accounts can be provided from a central funding account maintained in the bank.

![](/api/attachments/STRSPE8B/fulltext/images/8a4d9ed06dc7d030e9a2795923dd39068e1008d71812f970e862bd3ee2f60209.jpg)  
Exhibit 6. Cash Disbursement Decision Process.

## 3.4.2. Analysis of Information Requirements

The decision types detailed above will require a variety of information. Data required will be similar to the information required for lockbox studies. Data will be needed on the location of vendors or the location of banks/lockboxes to which checks have to be mailed so that homogeneous groups can be identified. The cash manager will require cost estimates of setting up and operating the disbursement system. The concentration system design must be known and data must also be available on mail times from the check issuing location to vendor groups and on presentation times from the vendor groups to drawee banks. The decision process also requires information on the estimated payments to be made to each of the vendor groups. Further, in order to support monitoring the effectiveness of disbursement sites, actual data on the parameters above must be continually updated.

## 3.4.3. Analysis of Modeling Requirements

The cash disbursement process can also be supported by a mathematical program similar to the cash gathering decision process. $^{14}$ One of the major benefits on which most disbursement studies hinged in the past was the disbursement float caused by slippage in the Federal Reserve clearing system. However, recent efforts by the Federal Reserve to reduce such slippage have been largely successful [41]. Ferguson and Maier [29] recognize the implications of this changing environment for disbursement system designs and suggest a modified programming model that considers the risk of complete elimination of Federal Reserve slippage. Thus, the decision process can be supported by a mathematical program that allows the decision maker to assign an appropriate weight to the benefits from Federal Reserve slippage in determining optimal disbursement sites.

## 3.5. Banking System Design for Credit and Other Banking Services

## 3.5.1. A Study of the Decision Process

This decision process relates to the selection of an optimal banking system for the firm's credit and other banking services excluding concentration, deposit and disbursement services. The firm's credit needs could be in the form of lines of credit and/or long-term loans. Noncredit service needs excluding deposit, disbursement and concentration services could include merger advice, specialized consulting with respect to international cash management, international borrowing, etc. The decision process is illustrated in exhibit 7.

This decision process is relatively more strategic in nature than the decision types discussed in previous sections. The decision process typically involves the evaluation of banks on several qualitative factors in addition to the evaluation of costs and benefits in financial terms. Examples of such qualitative factors include bank support during adversity, reputation of the bank among corporate circles, capacity to provide special services, financial strength of the bank, innovativeness, and operating efficiency. An additional factor that has increased in its relative importance in recent years is the bank's flexibility in accepting a mix of various forms of compensation. Traditionally, compensation for credit services was always in the form of compensating balances. During the past decade, new compensation opportunities have emerged, including the increasing use of fees, the use of non-interest bearing time deposits, and long-period averaging.

![](/api/attachments/STRSPE8B/fulltext/images/142053e2d6fbcfc1d18d2889d47656feba60e3f8a731ebe90cf4c9e025529453.jpg)  
Exhibit 7. Banking System Design for Credit Services.

## 3.5.2. Analysis of Information and Modeling Requirements

The banking system design for credit services will mainly require comparative cost and benefit information on the alternative banks being evaluated. Detailed information will be needed on acceptable compensation mix for various banks. Forecast information on expected cash flows will also be required. The ranking of the alternative banks on the qualitative and strategic factors forms a crucial input to the selection process and, therefore, information will be needed on the qualitative characteristic of banks.

Strategic considerations weigh heavily in a firm's decision to select credit line banks. Thus, a straightforward mathematical program to evaluate costs and benefits will not suffice for supporting this decision process. An alternative framework that can be adopted is the framework suggested by Srinivasan, Kim and Stone [98]. The suggested framework combines the Analytic Hierarchy Process (AHP) and mathematical programming to integrate evaluation of strategic factors and financial benefits and losses.

## 4. An Integrated Design of a CMDSS

## 4.1. A Revised Taxonomy of Cash Management Decisions

The previous section has attempted to describe the decision processes underlying cash management decisions and to identify the associated information and modeling requirements for each of the decision types. The decision processes were identified according to the taxonomy of cash management decisions that has implicitly or explicitly evolved in the literature. However, the existing taxonomy of cash management decision types, in our opinion, does not facilitate the recognition of important interrelationships that exist between the decision types and make the conceptualization of an integrated cash management DSS unnecessarily complex.

To motivate a revised taxonomy, let us examine the lockbox location problem. An important assumption in a typical formulation of the lockbox problem is that the concentration system design is known (see, e.g., [30]). On the other hand, consider a typical formulation to evaluate concentration system design [116]. It is assumed in this case that the set of optimal lockbox locations are known. Obviously, both decisions are dependent on each other since the mail and availability times that form a crucial input to both decisions are jointly determined by the two sets of banks. In fact, lockbox location, deposit bank selection, concentration system design, disbursement site selection and allocation of credit services to banks are inseparably related, at least conceptually. This points to an underlying character of these decision processes. All of them are infrastructural in nature. They relate to the establishment of an infrastructural system through which the company's cash resources are channeled, mobilized and optimally utilized. It should also be noted that these infrastructural decisions are not typically taken every day or very frequently. They are infrequent and conducted periodically, when and if, financial managers feel that the existing system is inappropriate.

An additional motivation for recognizing infrastructural dependencies stems from the recent trends in cash management environment: potential for increased adoption of electronic funds transfer systems (EFTS), possibility of nation-wide banking, and the advances in computer and information technologies. These trends have far reaching implications for the design and formulation of normative models for bank selection decisions relating to both credit and noncredit services. The introduction of EFTS on a wider scale and its acceptance for corporate payments will eventually result in far less importance being assigned to exploiting float opportunities. Moreover, the introduction of inter-state banking, will remove the need to maintain credit and banking relationship with a multiplicity of banks. A large national bank will have branches all over the country, and, thus, will be able to provide the entire range of cash management services required by corporations. In fact, it may become a competitive necessity for banks to integrate their existing services with the services currently being provided by deposit and disbursement banks. Such backward integration implies that national banks will be required to offer an integrated optimal banking system instead of advising separately on components of such a system.

On the other hand, cash balance management, cash forecasting, transfer mechanism and scheduling of transfers have to be revised and planned every day as fresh information becomes available. Indeed, these set of decisions are different in character and frequency from infrastructural decisions and can be designated as ‘operational decisions’. All of these decision types are interrelated to a high degree. Further, cash forecasting forms a crucial and continuous input to the cash position planning process and can, therefore, be properly grouped under operational decisions. Similarly, variance analysis for both infrastructural and operational decisions is also a continuous process and should form part of ‘operational decisions’.

The above decisions lead us to suggest a revised taxonomy of cash management decisions that should be the basis for systems design. We suggest that cash management decisions be grouped as operational and infrastructural decisions. The two groups of decisions are not independent but there is a certain degree of autonomy between the two processes due to the frequency with which they are taken. In fact, it is possible to specifically identify the dependencies between the two sets of decision processes. First, evaluation of the banking system for tangible services (deposit,-disbursement and concentration) will obviously require information on the funds to be moved through each potential location in the system. The costs and benefits of the system and each of the potential bank locations are directly dependent on the amount of funds and the frequency of transfers. Secondly, the infrastructural component for credit services will require information on the type and extent of credit required. This information forms a crucial input to the design of this component and emanates from the cash budgeting process. New compensation opportunities like long-run averaging form another source of dependency between operational and infrastructural decisions.

![](/api/attachments/STRSPE8B/fulltext/images/e559e3cc89944838eaafeea8dbb9d6ea217eb84d903f9b8b1d1d205b02bc5978.jpg)  
Exhibit 8. Conceptual Partitioning of Information Needs for Corporate Level Cash Management.

There is an important distinction in the dependencies between operational and infrastructural decisions as compared to the dependencies among the decision types within each of two groups. Dependencies within each of the groups are direct and necessitate simultaneous determination to obtain globally optimum solutions, i.e., are inseparable. However, dependencies across the two groups are only indirect and, therefore, the two groups of decisions are separable. The selection of the banking infrastructure is necessarily based on forecast data over a fairly long horizon since it is infeasible to alter the banking system design very frequently. Operational cash management, however, is dynamic and will depend on revised information as the horizon unfolds.

## 4.2. Effective Organization of Information

In the preceding section, we have identified the information needs of each decision type. However, they were presented in an ad hoc manner without any form of stratification or organization. From the point of efficiently organizing the DSS data base, information needs have to be stratified and grouped systematically to facilitate easy identification and retrieval. The literature on information characteristics (see, e.g., [20,32,38,49]) suggests that information can be grouped according to the following major characteristics: (i) financial vs. nonfinancial, (ii) ex post vs. ex ante, (iii) internal vs. external. These groupings yield eight possible combinations of information types. In addition, the data can also be stratified along the decision type dimension. The resulting conceptual partitioning of information is illustrated in exhibit 8. A review of the various alternative data models suggests that the relational data model would be the most suitable representation for the CMDSS data base.

![](/api/attachments/STRSPE8B/fulltext/images/a4310fdef675f0cbb7affe63603c9b34f55ca500d97eeb575ba5c6d9f94cbd2b.jpg)  
Exhibit 9. Integrated CMDSS Model Base Design.

## 4.3. An Illustrative Model Base Design

We summarize in exhibit 9 an illustrative design for the CMDSS model base. As evident from exhibit 9, we suggest that specific DSSs be built to deal with operational decisions, infrastructural decisions and variance analysis. It is also necessary to point out that to obtain a globally optimum banking system design, the DSS will require a computationally complex mathematical program. If the complexity of the resulting program is deemed unacceptable, or infeasible, the relationships can be examined through descriptive linkages. In such a case, separate models within the infrastructural DSS could support the credit line, concentration, deposit and disbursement bank selection process with the built in ability in the model management systems and models to effectively examine the dependencies descriptively.

## 5. Summary

In summary, this paper suggests that the analytical approaches advanced in the literature ignore the broader set of constraints that the cash managers face in practice. The problem of optimally utilizing cash resources is not well structured. Some aspects of the problem are more structured that others. The paper conceptualizes an effective approach to a DSS for cash management based on a revised taxonomy of cash management decision making. The framework provided should form the conceptual basis for both theoretical research in the area and development of DSS for use by cash managers. Implementational issues will have to be considered on a situation-specific basis and the DSS modified, if necessary.

Neither the informational needs nor the decision types can be expected to be completely specified a priori. Various needs in the design of a CMDSS that were not previously identified are bound to come up during and after implementation. Modifying the DSS for such needs will pave the way for creating an effective DSS for cash management.

## References

[1] Alter, S. Decision Support Systems: Current Trends and Continuing Challenges Addison-Wesley, Reading, MA (1980).

[2] Ang, J., J.H. Chua and R. Sellers, Generating Cash Flow Estimates: An Actual Study Using the Delphi Technique, Financial Management 9 (1) (1980).

[3] Anthony, R.N., Planning and Control Systems: A Framework for Analysis, Studies in Management Control, Harvard University Graduate School of Business Administration, Cambridge, MA (1965).

[4] Anvari, M. An Application of Inventory Theoretical Models to Cash Collection, Decision Sciences 12 (1981) 126–133.

[5] Austin, J., S.F. Maier and J.H. Vander Weide, General Telephone's Experience with a Short-Run Financial Planning Model, Cash Management Forum (June, 1980) 3–6.

[6] Baker, K.R., S.F. Maier and J.H. Vander Weide, Heuristic Methods for Solving the Lockbox Location Problem and Related Location-Allocation Problems, Working paper, Graduate School of Business Administration, Duke University (September, 1975).

[7] Baumol, W.J., The Transaction Demand for Cash: An Inventory Theoretic Approach, Quarterly Journal of Economics 66 (November, 1952) 545–556.

[8] Beehler, P.J., Contemporary Cash Mangement, Wiley, New York (1983).

[9] Bennett, J., User-Oriented Graphics, Systems for Decision Support in Unstructured Tasks, in: S. Treu, ed., User-Oriented Design of Interactive Graphics System, Association of Computing Machinery, New York (1977) 3–11.

[10] Bonczek, R.H., C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York (1981).

[11] Boyd, K. and V.A. Mabert, A Two-Stage Forecasting Approach at Chemical Bank of New York for Check Processing, Journal of Bank Research (Summer, 1977) 101–107.

[12] Brandon, B.M., Contemporary Disbursing Practices and Products: A Survey, Journal of Cash Management (March, 1982) 26–39.

[13] Calman, R.F., Linear Programming and Cash Management: CASHALPHA, The MIT Press, Cambridge, MA (1968).

[14] Cash Management: The New Art of Wringing More Profit from Corporate Funds, Business Week (March 13, 1978) 62–68.

[15] Churchill, M. and B. Ward, How BMW Computerised Cash Planning, Accountancy (June, 1976) 26–29.

[16] Constantinides, G.M., Stochastic Cash management with Fixed and proportional Transaction Costs, Management Science 22 (August, 1976) 1320–1331.

[17] Cox, G.E.P. and G.M. Jenkins, Time Series Analysis, Forecasting and Control, Holden Day, San Francisco (1970).

[18] Dallenbach, H.G., Are Cash Management Models Worthwhile? Journal of Financial and Quatitative Analysis (September, 1974) 607–626.

[19] Date, C.J., An Introduction to Data Base Systems, 2nd ed. Addison-Wesley, Reading, MA (1977).

[20] Dermer, J.D., Cognitive Characteristica and the Perceived Importance of Information, The Accounting Review (July, 1973) 511–519.

[21] Edick, T.B., The Credit Executive's Role in Cash Management, Credit and Financial Management (October, 1975) 16–33.

[22] Editorial, The Expanding Role of the Corporate Cash Manager, Journal of Cash Management, (July–August, 1984) 12–13.

[23] Elton, E.J. and M.J. Gruber, On the Cash Balance Problem, Operational Research Quarterly 25 (4) (1979) 553–572.

[24] Emery, G., Some Empirical Evidence on the Properties of Daily Cash Flow, Financial Management (Spring, 1981) 21–28.

[25] Emery, G., Discussion: The Design of a Company's Banking System, Journal of Finance (May, 1983) 387–389.

[26] Eppen, G.D. and E.F. Fama, Three Asset Cash Balance and Dynamic Portfolio Problems, Management Science (January, 1971) 311–319.

[27] Ferguson, D.M. and S.F. Maier, Finding the Real Float – A New Standard for Lockbox Studies, CASHFLOW (September/October, 1980) 55–59.

[28] Ferguson, D.M. and S.F. Maier, By Any Other Name..... Controlled Disbursement in the New Environment, CASHFLOW (May, 1981) 31–35.

[29] Ferguson, D.M. and S.F. Maier, Disbursement System for the 1980s, Journal of Cash Management (November, 1982) 56–69.

[30] Fielitz, B.D. and D.I. White, A Two-Stage Solution Procedure for the Lockbox Problem, Management Science (August, 1981) 881–886.

[31] Gerrity, Jr., T.P., Design of Man–Machine Decision Systems: An Application to Portfolio Management, Sloan Management Review (Winter, 1971) 59–75.

[32] Ghymn, K.I. and W.R. King, Design of a Strategic Management Information System, OMEGA (1976) 595–607.

[33] Gitman, L.J., D.K. Forrester and J.R. Forrester, Jr., Maximizing Cash Disbursement Float, Financial Management (Summer, 1975) 15–24.

[34] Gitman, L.J., An Assessment of Marketable Securities Management Practices, Journal of Financial Research (Fall, 1979) 161–169.

[35] Golden, B., M. Liberatore and C. Lieberman, Models and Solution Techniques for Cash Flow Management, Computers & Operations Research (1979) 13–20.

[36] Golden, B. and K. Keating, On Simplifying a Network Model for Cash Flow Management, in: T. Rakes and E. Hickman, eds., Proceedings of the 17th Annual Southwest TIMS Conference, Atlanta (1982) 226–230.

[37] Gordon, L.A., and G.A. Pinches, Improving Capital Budgeting: A Decision Support System Approach, Addison-Wesley, Reading, MA (1984).

[38] Gordon, L.A., D.F. Larcker and F.D. Tuggle, Strategic Decision Processes and the Design of Accounting Information Systems: Conceptual Linkages, Accounting, Organizations and Society (1978) 203–213.

[39] Gorry, G.A., and M.S. Scott Morton, A Framework for Management Information Systems, Sloan Management Review (Fall, 1971) 55–70.

[40] Gregory, G., Cash Flow Models; A Review, OMEGA (1976) 643–656.

[41] High Group Sort Program, The Federal Reserve Bank of St. Louis (February 24, 1984).

[42] Hill, N.C., W. Sartoris and D.M. Ferguson, Corporate Credit Policies and Corporate Payment Policies: Results of Two Surveys, Journal of Cash Management.

[43] Jaffe, R.S., A Singular Cash Management Problem, Financial Executive (May, 1978) 44–46.

[44] Kallberg, J.G. and K. Parkinson, Current Asset Management, John Wiley, New York, (1984).

[45] Keen, P.G.W. and M.S. Scott Morton, Decision Support System: An Organizational Perspective, Addison-Wesley, Reading, MA (1978).

[46] Kim, Y.H., Ed., Advances in Working Capital Management, Research Annual, Vol. 1, forthcoming (1987) JAI Press, Greenwich, CT.

[47] Kramer, R.L., Feedback: The Lockbox Location Problem, Journal of Bank Research (Springer, 1971).

[48] Kraus, A., C. Janssen and A.K. McAdams, The Lockbox Location Problems, Journal of Bank Research (Autumn, 1970) 51–58.

[49] Larcker, D.F., The Perceived Importance of Selected Information Characteristics for Capital Budgeting Decisions, Accounting Review (July, 1981) 195–206.

[50] Lerner, E.M., Simulating the Cash Budget, California Management Review (Winter, 1968) 78–87.

[51] Levy, F.K., An Application of Heuristic Problem Solving to Accounts Receivable Management, Management Science (February, 1966) B236–B244.

[52] Lewellen, W. and R.O. Edmister, A General Method for Accounts Receivable Analysis and Control, Journal of Financial and Quantitative Analysis (March, 1973) 195–206.

[53] Lockyer, K.G., Cash as an Item of Stock, Journal of Business Finance (1973) 44–51.

[54] Loscaljo, W., Cash Forecasting, McGraw-Hill, New York (1982).

[55] Maier, S.F. and J.M. Vander Weide, The Lockbox Problem: A Practical Reformulation, Journal of Bank Research, (Summer, 1974) 92–95.

[56] Maier, S.F. and J.M. Vander Weide, A Unified Model for Cash Disbursement and Lockbox Collections, Journal of Bank Research (1976) 166–172.

[57] Maier, S.F. and J.M. Vander Weide, A Decision Support System for Managing a Short-Term Financial Instrument Portfolio, Journal of Cash Management (March, 1982) 20–25.

[58] Maier, S.F. and J.M. Vander Weide, What Lockbox and Disbursement Models Really Do, Journal of Finance (May, 1983) 361–371.

[59] Maier, S.F., D.W. Robinson and J.M. Vander Weide, A Short-Term Disbursement Forecasting Model, Financial Management (Spring, 1981) 9–20.

[60] Mao, J.C.T., Application of Linear Programming to the Short-Term Financing Decision, The Engineering Economist (July, 1968) 221–241.

[61] Mavrides, L.P., An Indirect Method for the Generalized

k-Median Problem Applied to Lockbox Location, Management Science (October, 1979) 990–996.

[62] McAdams, A.K., Critique of: A Lockbox Model, Management Science (October, 1968) B88–B90.

[63] Miller, M. and D. Orr, A Model of the Demand for Money by Firms, Quarterly Journal of Economics (August, 1966) 413–435.

[64] Miller, T.W., A Systems View of Short-Term Investment Management, in: Y.H. Kim, (ed.), Advances in Working Capital Management, Vol. 1 forthcoming (1986).

[65] Miller, T.W. and B.K. Stone, Daily Cash Forecasting and Seasonal Resolution: Alternative Models and Techniques for Using the Distribution Approach, Journal of Financial and Quantitative Analysis (September, 1985) 335–378.

[66] Mullins, D. and R. Homonoff, Applications of Inventory Cash Management Models, in: S.C. Myers (ed.), Modern Developments in Financial Management, Praeger, New York (1976).

[67] Mulvey, J.M., A Network Flow Approach for Cash Flow Management, Journal of Cash Management (January, February, 1984) 46–48.

[68] Nauss, R. and R.E. Markland, Solving the Lockbox Location Problem, Financial Management (Spring, 1979) 21–31.

[69] Nauss, R.M. and R.E. Markland, Theory and Application of an Optimizing Procedure for Lockbox Location Analysis, Management Science (August, 1981) 855–865.

[70] Nelson, C.R., Applied Time Series Analysis, Holden Day, San Francisco (1973).

[71] Orgler, Y., Cash Management: Methods and Models, California, Belmont (1970).

[72] Orgler, Y., An Unequal Period Model for Cash Management Decisions, Management Science (1974) 1350–1363.

[73] Osteryoung, J.S., G.S. Roberts and D.E. McCarty, Riding the Yield Curve – A Useful Technique for Short-Term Investment of Idle Funds in Treasury Bills? in Keith V. Smith, ed., Readings in the Management of Working Capital, 2nd Ed. West Publishing, St. Paul, MN (1980).

[74] Petty, J.W. and O.D. Bowling, The Financial Manager and Quantitative Decision Models, Financial Management (Winter, 1976) 32–41.

[75] Pogue, G.A., R.B. Faucett and R.N. Bussard, Cash Management: A Systems Approach, Industrial Management Review (1970) 55–74.

[76] Robichek, A.A., D. Teichroew and J.M. Jones, Optimal Short-Term Financing Decisions, Management Science (September, 1965) 1–36.

[77] Saaty, T.L., The Analytic Hierarchy Process, McGraw-Hill, New York (1980).

[78] Saaty, T.L. and L.G. Vargas, The Logic of Priorities, Kluwer-Nijhoff, Boston (1982).

[79] Scott, D.F. L.J. Moore, A. Saint-Oenis, E. Archer and B.W. Taylor, Implementation of a Cash Budget Simulator at Air Canada, Financial Management (Summer, 1979) 46–52.

[80] Scott, D.F. and L.J. Moore, Simulation of Cash Budgets, Journal of Systems Management (November, 1973) 28–33.

[81] Scott Morton, M.S., Management Decision Support Systems: Computer Based Support for Decision Making,

Division of Research, Harvard University, Cambridge, MA (1971).

[82] Searby, F.W., Use Your Hidden Cash Reserves, Harvard Business Review (March-April, 1980) 71–80.

[83] Sethi, S.P. and G.L. Thompson, Application of Mathematical Control Theory to Finance: Modeling Simple Dynamic Cash Balance Problems, Journal of Financial and Quantitative Analysis (December, 1970) 381–394.

[84] Sethi, S.P. and G.L. Thompson, A Note on Modeling Simple Dynamic Cash Balance Problems, Journal of Financial and Quantitative Analysis (September, 1973) 685–687.

[85] Sethi, S.P. and G.L. Thompson, A Note on Modeling Simple Dynamic Cash Balance Problems," Journal of Financial and Quantitative Analysis (September, 1978) 585–586.

[86] Shanker, R.J. and A.A. Zoltners, An Extension of the Lockbox Location Problems, Journal of Bank Research (Winter, 1972).

[87] Shanker, R.J. and A.A. Zoltners, The Corporate Payments Problem, Journal of Bank Research (Spring, 1972) 47–53.

[88] Shim, J.K., Estimating Cash Collection Rates from Credit Sales: A Lagged Regression Approach, Financial Management (Winter, 1981) 28–30.

[89] Simon, H.A. The New Science of Management Decision, Harper and Row, New York (1960).

[90] Sprague, Jr., R.H. and E.D. Carlson, Building Effective Decision Support Systems, Prentice Hall, Englewood Cliffs, NJ (1982).

[91] Sprague, Jr., R.H., A Framework for the Development of Decision Support Systems, in: W.C. House ed., Decision Support Systems, Petrocelli Books, New York (1983) 85–123.

[92] Srinivasan V., A Transshipment Model for Cash Management Decisions, Management Science Research Report no. 243, Graduate School of Industrial Administration, Carnegie-Mellon University, Pittsburg, PA (1971).

[93] Srinivasan V., A Transshipment Model for Cash Management Decisions, Management Science (1974) 1350-1363.

[94] Srinivasan, V. and Y.H. Kim, Cash Flow Management: A Decision Support System Approach, Journal of Cash Management (November/December, 1984) 72–80.

[95] Srinivasan, V. and Y.H. Kim, Decision Support for Credit Management: A Conceptual Framework, Paper presented at the Cash, Treasury and Working Capital Symposium, Montreal, Canada, (July, 1985).

[96] Srinivasan, V. and Y.H. Kim, A Network Optimization Approach to Efficient Cash Management in India, Asia-Pacific Journal of Operations Research 2 (1985) 54–65.

[97] Srinivasan, V. and Y.H. Kim, Deterministic Cash Flow Models: State-of-the-Art and Research Directions, OMEGA 14 (2) (1986) 145–166.

[98] Srinivasan, V., Y.H. Kim and B.K. Stone, Banking System Design: The State of the Art, Working paper, CBA, Northeastern University (1986).

[99] Srinivasan, V. and Y.H. Kim, Designing a DSS for Working Capital Management, in: Y.H. Kim, ed., Advances in Working Capital Management, Vol. 1, forthcoming (1987).

[100] Srinivasan V. and Y.H. Kim, Payments Netting in International Cash Management: A Network Optimization Approach, Journal of International Business Studies 17(2) Summer, 1986 1–20.

[101] Srinivasan, V. and Y.H. Kim, Financial Applications of the Analytic Hierarchy Process, Paper presented at the TIMS XXVII Gold Coast, Australia (July, 1986).

[102] Srinivasan, V. and Y.H. Kim, International Cash Management: A Systems Approach (under revision), University of Cincinnati (January, 1985).

[103] Srinivasan, V. and Y.H. Kim, Variance Analysis for Effective Cash Management, Working paper, University of Cincinnati (March, 1985).

[104] Srinivasan V. and Y.H. Kim, The Role of Expert Systems and AI Technology in Cash Management, Working paper (under revision), Northeastern University.

[105] Stancill, J.M., A Decision Rule for the Establishment of a Lockbox, Management Science (October, 1968) 884–887.

[106] Stone, B.K., The Use of Forecasts and Smoothing in Control Limit Models for Cash Management, Financial Management (Spring, 1972) 72–84.

[107] Stone, B.K., Cash Planning and Credit Line Determination with a Financial Statement Simulator: A Case Report on Short-Term Financial Planning, Journal of Financial and Quantitative Analysis (December, 1973) 711–729.

[108] Stone, B.K., Allocating Credit Lines, Planned Borrowing, and Tangible Services Over a Company's Banking Design, Financial Management (Summer, 1975) 65–78.

[109] Stone, B.K., The Payments Pattern Approach to the Forecasting and Control of Accounts Receivable, Financial Management (Autumn, 1976) 65–82.

[110] Stone, B.K., Break-even Receivables Size and the Allocation of Receivables to Lockboxes, Working paper no. MS-78-1, College of Industrial Management, Georgia Institute of Technology.

[111] Stone, B.K. Zero-Balance Banking and Collection System Design in a Divisionalized Firm, Working paper no. 79–2, College of Industrial Management, Georgia Institute of Technology.

[112] Stone, B.K., Lockbox Selection and Collection Systems

Design: Objective Function Validity, Journal of Bank Research (Winter, 1980) 251–254.

[113] Stone, B.K. Design of a Receivable Collection System: Sequential Building Heuristics, Management Science (August, 1981) 886–880.

[114] Stone, B.K., The Design of a Company's Banking System, Journal of Finance (May, 1983) 373–385.

[115] Stone, B.K. and N.C. Hill, Cash Transfer Scheduling for Efficient Cash Concentration, Financial Management (Autumn, 1980) 35–43.

[116] Stone, B.K. and N.C. Hill, The Design of a Cash Concentration System, Journal of Financial and Quantitative Analysis (September, 1981) 301–322.

[117] Stone, B.K. and N.C. Hill, Alternative Cash Transfer Mechanisms and Methods: Evaluation Frameworks, Journal of Bank Research (Springer, 1982) 7–16.

[118] Stone, B.K., D.M. Ferguson and N.C. Hill, Cash Transfer Scheduling and Overview, The Cash Manager (March, 1980) 3–8.

[119] Stone, B.K. and R.A. Wood, Daily Cash Forecasting: A Simple Method for Implementing the Distribution Approach, Financial Management (Fall, 1977) 40–50.

[120] Stone, B.K. and T.W. Miller, Daily Cash Forecasting with Dummy Variable Regression using Multiplicative and Mixed-Effects Models for Measuring Cash Flow Cycles, Working paper no. 79–18, College of Industrial Management, Georgia Institute of Technology.

[121] Symposium on Cash, Treasury and Working Capital Management, Montreal, Canada, (1985, 1986).

[122] Truenkle, J.W., E.B. Cox and J.A. Bullard, Jr., The Use of Financial Models in Business, The Financial Executive Research Foundation, New York (1975).

[123] Vandaele, W., Applied Time Series and Box-Jenkins Models, Academic Press, New York (1983).

[124] Vander Weide, J. and S.F. Maier, Managing Corporate Liquidity, John Wiley, New York (1985).

[125] Winters, P.R., Forecasting Models by Exponentially Weighted Moving Averages, Management Science (1960).

[126] Zionts, S., A Deterministic Cash Management Problem, Working paper no. 75–2, European Institute for Advanced Studies in Management (January, 1975).
