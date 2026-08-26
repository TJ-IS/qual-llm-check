---
otero_id: 24727
otero_key: "SJBYQVGH"
title: "Procurement Strategies for Information Systems"
authors: "Timo Saarinen; Ari P.J. Vepsäläinen"
year: "1994"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1994.11518045"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Procurement Strategies for Information Systems

Timo Saarinen & Ari P.J. Vepsäläinen

To cite this article: Timo Saarinen & Ari P.J. Vepsäläinen (1994) Procurement Strategies for Information Systems, Journal of Management Information Systems, 11:2, 187-208, DOI: 10.1080/07421222.1994.11518045

To link to this article: http://dx.doi.org/10.1080/07421222.1994.11518045

![](/api/attachments/SJBYQVGH/fulltext/images/e6bd777f2f3ef7b2f3c03eabced456f0aff5888a19da241ffc58ac84171a235a.jpg)

Published online: 14 Dec 2015.

![](/api/attachments/SJBYQVGH/fulltext/images/d94547a803fba02cd4759e6cf1cecab47e76c5d6ec0b4c8ef97c590a56ca5785.jpg)

Submit your article to this journal ↗

![](/api/attachments/SJBYQVGH/fulltext/images/cb255087ce91fe46aacaf80bd1ed3b6c74b10e1efe90d543d51efcf51a8007b7.jpg)

View related articles ↗

![](/api/attachments/SJBYQVGH/fulltext/images/9f2e12ce037bc627a761fbc09837b8687e2a53098fa83570c82905dbf6b7e89c.jpg)

Citing articles: 21 View citing articles ↗

# Procurement Strategies for Information Systems

TIMO SAARINEN AND ARI P.J. VEPSÄLÄINEN

TIMO SAARINEN is Acting Associate Professor of Business Information Systems at the Helsinki School of Economics. His research interests include the economics and management of information systems with an emphasis on organization, competitive evaluation and risk management of systems development. He received his Ph.D. in economics (information systems) from the Helsinki School of Economics. He has published articles in Information & Management, European Journal of Information Systems, Behaviour and Information Technology, Journal of Strategic Information Systems, Journal of Systems Management, and Scandinavian Journal of Information Systems.

ARI P.J. VEPSÄLÄINEN is currently Professor of Logistics at the Helsinki School of Economics and principal of HM&V Research Oy, a consulting company specializing in information technology for the service sector. His research interests include operations management, logistics, and information systems development. He received M.Sc. and Tech.Lic. degrees in operations research from Helsinki University of Technology, and a Ph.D. in systems sciences from Carnegie-Mellon University. Previously, Dr. Vepsäläinen has been Assistant Professor at Carnegie-Mellon University and at The Wharton School, University of Pennsylvania. He has published several books as well as articles in Management Science, Strategic Management Journal, Journal of Manufacturing and Operations Management, Decision Support Systems, IEEE Transactions on Engineering Management, and other journals.

ABSTRACT: A general framework of different procurement strategies is introduced to help managers review their project portfolio to find more effective ways of using both internal and market resources in information systems development. Major decision criteria—the specificity of system design and the uncertainty involved in requirements specification—are adopted from transaction cost economics to determine what procurement strategies should be used in different situations. According to our Procurement Principle, systems that are company-specific and involve high uncertainty have to be internally developed because they require both the specific knowledge and intensive interaction between developers and users. More standard requirements indicate the use of outside consultants or software contractors who have experience and knowledge about a similar type of systems. For routine systems common in many

Acknowledgments: The authors thank Professor Markku Sääksjärvi of the Helsinki School of Economics, Professor Jonathan Miller of the University of Cape Town, Professor Juhani Iivari of the University of Jyväskylä, and the two anonymous referees for comments and support. Mary Peffers is acknowledged for her help with editing the final version of the paper. This research was finished while Timo Saarinen was a Research Fellow for the Academy of Finland and a visiting scholar at the Rutgers University School of Business in Camden, New Jersey.

organizations, acquisition and tailoring of a software package provides the most efficient procurement strategy. The Procurement Principle is also empirically tested with data from recent system development projects in major Finnish companies. Partial support was gained for the framework, but some interesting deviations were also detected, such as a tendency to rely on in-house development of even routine systems.

KEY WORDS AND PHRASES: contingency approach, information systems procurement, outsourcing.

## 1. Introduction

INFORMATION SYSTEM (IS) MANAGERS TODAY ARE FACED WITH MANY REQUESTS for developing new applications, and enhancing or replacing existing ones. At the same time, however, recession and financial austerity call for critical review of IS budgets, and cutbacks of funds and personnel. The traditional question of how IS managers are to satisfy the increasing demands of users and business strategies with their limited resources is now more important than ever before.

One conventional solution is to obtain new methods and tools, increasing the productivity of system development, thus managing the projects with the resources available. The other possibility—the one advocated here—is to utilize markets more effectively and focus in-house development on the most critical applications. However, no matter how attractive market procurement may seem, its limitations should be correctly understood to maximize its advantages. To get the full benefit from using a package, the procurement decision has to be made early in the investment process, when uncertainty of the requirements may still be high. Furthermore, many promising systems are novel and innovative, and packages will be available in the marketplace only after considerable delay. To rely on the market also means a long-lasting commitment to the selected application packages, the software vendors, and the contracting companies.

Even though many situational approaches have been developed for choosing between IS development strategies $[4, 5, 10, 11, 15]$ , specialized theories, models or frameworks for IS procurement are scarce. Some guidelines for the make-or-buy decisions can be found in Gremillion and Pyburn $[6]$ , who see the use of software packages as a viable strategy for well-structured systems that are common in many companies. Iivari $[7]$ analyzes situations in which development is based on the existing applications or on development of new unique systems. He concludes that despite the cost-efficiency and technological ease of package acquisition, organizational problems often arise in implementation. Whang $[18]$ deals with software contracting issues by modeling product definition, payment schedules, and incentive mechanisms to derive optimal contracts performing up to comparable internal development. Loh and Venkatraman $[9]$ recognize such issues as development of a competitive advantage and core capabilities as possible reasons for using either market resources or internal development strategies.

We develop a general model of make-or-buy decisions for information systems procurement based on Williamson's transaction cost economics [19]. Beath [3] has made headway in applying transaction cost approach to the choice of development strategies. Apte and Vepsäläinen [1, 16] found some criteria for efficient design of delivery channels in financial services, and, in a more general context, Mäkelin and Vepsäläinen [12] used the theory to derive effective architectures for information systems based on the type of service. Koskela and Vepsäläinen [8] applied the results to the choice of management strategy for a construction project. In this paper we build on transaction cost economics and the above frameworks in analyzing efficient procurement strategies for IS investments. We also use the model to empirically study strategy choices of 48 IS development projects in major Finnish companies.

Section 2 describes our framework for efficient procurement of information systems. An empirical investigation is reported in section 3 and section 4 presents some discussion and conclusions.

## 2. A Model for IS Procurement—A Transaction Cost Approach

PROCUREMENT MEANS THE CHOICE AMONG SUPPLIERS (in-house personnel, outside experts, consultants, software contractors, or package dealers) and contracting forms (salary, project contract, package price, lease or rent) for acquiring an asset. It addresses issues that are broader than those dealt with in the conventional literature on information systems development. It deals with institutional make-or-buy decisions for which transaction cost economics [19] offers a general theory.

In neoclassical economic theory, companies are assumed to minimize production costs to compete in the marketplace. Institutional economics recognizes another class of costs equally important for the efficiency of organizations and structure of the industry. Williamson [19], following Arrow [2] and others, calls these costs transaction costs, which constitute the “friction of running the economic system.” Characteristics of transactions, together with production costs, determine whether it is effective for the company to produce certain products or services in-house, purchase them, or use subcontractors. These are seen as the alternative governance structures for the transactions. Often markets are more effective governance structures than corporate hierarchy due to the economies of scale and market feedback mechanism. Economies of scale guarantee cost-effective production and the market feedback mechanism guarantees appropriate quality and low prices. Despite the superiority of markets, however, some situations call for many products and services to be supplied from inside the company because of company-specific assets and resources that have low value in alternative uses in the marketplace. Also, any substantial uncertainty surrounding the ability of the supplier to perform up to the contract, or, under unforeseen scenarios, the tendency of the contracting parties to behave opportunistically may cause the markets to fail, leaving internal procurement—the hierarchy—as the only practical alternative.

In applying transaction cost economics to the procurement methods of information systems, we first identify the most important characteristics of the desired transactions (information systems projects) and alternative governance structures (project organization) in order to find the effective strategies. We argue that, in practice, the main problem faced in fact is choosing the correct strategy so that the most appropriate developer team is assigned for each project.

## 2.1. Types of System Specifications

The systems proposed for procurement can be characterized by two factors inherent in the transaction cost approach: specificity of system design and uncertainty of requirements. The specificity of system designs varies from common in many organizations to highly specific and contingent to one organization. The estimation of the specificity of a system may be based, for example, on management opinion or comparisons with other companies. Similarly, the uncertainty varies from situations of certain and simple requirements to risky and complex requirements. Estimates may be derived, for example, on the basis of clarity and stability of requirements.

In principle, investments with high specificity and low uncertainty are likely to offer high payoff and would be preferred by most managers. Investments with common requirements but high uncertainty are likely to result in low payoff and would usually be avoided. The economics of competition, however, ascertains that neither of these types of investments is common in practice. Specific systems often have high expected payoff, but they also have high development cost and high uncertainty. Routine systems with common requirements across organizations can be provided at a low cost and at a low risk, but accordingly, the payoff potential is usually low. Figure 1 illustrates the expected trade-offs in a matrix that locates the generic types of systems on the diagonal. The generic systems are as follows:

1. Routine systems are common to many organizations with rather stable requirements and low uncertainty about their functionality. Payroll and accounting applications are examples of this type.

2. Standard applications meet the needs of a group of organizations with some variety and dynamics of requirements. Industry-specific applications such as manufacturing and marketing systems are examples of this type.

3. Speculative investments are highly specific to one company and involve high uncertainty in terms of functionality, user interfaces, and the competitiveness of the business supported. Examples may include decision support, customer-oriented systems, and computer integrated operations support.

Proposed systems not on the diagonal, when they occur, may be difficult to deal with in the procurement process. In the case where specificity is high but uncertainty low, one can choose to rely on a system designed from scratch and accept the high development costs. In many cases these kinds of systems are profitable, but not always. An example is a highly specific production line for which management feels quite certain about the requirements of production control. If internally developed, the system would probably be costly; hence, one may want to bring the specification more in line with some standard solution or even acquire a package. The stability of requirements would be maintained but functionality would be compromised and business benefits diminished. The advantage, however, would be lower development costs. Often the problems with these kinds of systems can be avoided by decomposing the proposed project into appropriate speculative and routine subsystems.

![](/api/attachments/SJBYQVGH/fulltext/images/e10f42afe7a7a50b8b18ba7d66d05112f7550fd25d8552376f27c2154fa258c3.jpg)  
Figure 1. Generic Types of System Projects Matching the Specificity of Design and Uncertainty of Requirements

In the case of high requirement uncertainty but common nature of design, there are users who do not know that the desired functionality of the proposed system or its benefits are jeopardized due to changes in application environment. This kind of situation may occur, for example, when personnel turnover is high or competitive conditions are turbulent. Pursuing the development is likely to result in failure unless the objectives of the system are refined. Either the system would have to be fitted to the company's operations more closely, thus creating a competitive advantage corresponding to the risks taken, or the problems of turbulent requirements could be dealt with at a low cost by acquiring a package or sharing a project with other potential user organizations. In any case, the whole proposal should be scrutinized and postponement of the project considered until the user environment settles down.

## 2.2. Characteristics of the Development Team

We emphasize two factors describing the type of intended developers: the knowledge of the supported business and ability to specify requirements. These are considered as the means to cope with system specificity and requirements uncertainty, respectively. The level of business knowledge varies from specific knowledge about the supported business to only common knowledge about business organizations in general. Estimation of the capabilities may be rather straightforward, including the job titles and expertise evaluated by managers and clients. Similarly, ability to specify requirements varies from a developer team able to specify requirements effectively to those unable to communicate and reach agreement on the system's desired functionality. Besides formal positions in the organizations, the estimates may include the intensity of communication among the developers and users, and the opinions of managers and clients.

The expected combinations of business knowledge and specification skills are illustrated on the diagonal of the matrix of developers in figure 2. Again, we can characterize generic types of developers as follows:

1. Implementors may have high product-specific knowledge and skills relating to methods and packages but only common knowledge about user organizations. Furthermore, they are often hired by a software house or a dealer; thus they have only limited possibilities or capabilities to specify users needs and add value to the application.

2. Analysts have capabilities of solving generic problems and specifying even complex integrated systems. Commissioned by the client to help in the systems development process, they are motivated to specify users' requirements and improve the system solutions.

3. Innovators have specialized knowledge about the company, its users, and information systems, and it is assumed that they communicate easily with the users. They are able to specify and create new innovative solutions. Usually hired by the user organization, they are expected to specify and evaluate systems solutions from the perspective of the client.

The expected relationship between developers' business knowledge and specification skills is illustrated in figure 2. It is assumed that innovators have the highest specialized knowledge and that they have the ability to find the requirements that bring the highest value to the client—that is, the organization developing the system. In the other extreme, implementors may be specialized in the particular supplier's software product, and their motivation may come mainly from selling the system. Finally, analysts are usually positioned in the middle of both business knowledge and specification skills dimensions in a competitive market.

If developers' business knowledge does not match their specification skills (i.e., they are not on the diagonal in figure 2), problems may arise. If the specification skills are high but the knowledge about supported business is poor, it is likely that the developer team will have to spend a lot of time learning and communicating the required business knowledge, thus increasing time spent by management in creating a solution. This is necessary, however; otherwise, a proposed system is not likely to be the best solution for the organization. This kind of situation may occur, for example, when the organization hires young experts.

![](/api/attachments/SJBYQVGH/fulltext/images/180df8daf8ccb23454d61c5fa808e38e04cf81df18471dbfc592e212895c135e.jpg)  
Figure 2. Generic Types of System Developers Matching Specific Business Knowledge with Specification Skills

On the other hand, if developers' business knowledge is high but ability to add value to the customer by specifying his or her specific requirements is low, clients face a high risk of failure. An example of this kind of developer is a systems analyst with extensive experience and specialized knowledge about a company, who is commissioned by a systems supplier to rely mostly on the functionality of an existing solution or a package offered. This situation may lead to embarrassing results if, for example, the true motivation of the developer is revealed or some forthcoming changes in the organization undermine the seemingly rational choice that had been made prior to these changes.

To align developers' characteristics more productively, the following corrective actions can be recommended. Developers with high knowledge about supported business but low specification skills should be hired with extreme care, thus avoiding predetermined solutions and solutions that may be sophisticated but do not fit customer needs. Situations in which developers have high specification skills but low business knowledge are best avoided by not accepting final plans without ensuring critical assessment by in-house experts, demanding extensive verification of the proposed system, and, at the very least, obtaining a “second opinion” from a reliable independent consultant.

## 2.3. Efficient Procurement Strategies

The proposed information system projects may now be mapped in a matrix formed by the types of information systems and the types of prospective developers. This matrix is shown in figure 3 (see similar matrices in [12, 16]). The appropriate matching of the type of the system and the developer constitute the efficient procurement strategies, as indicated by the diagonal in figure 3. In terms of the efficient strategies, we may form the following Procurement Principle:

1. Routine systems can be best implemented by acquiring software packages from implementors.

2. Standard applications require software contracting by analysts and possibly other outside resources for implementation.

3. Speculative investments are best left for internal development by innovators.

This Procurement Principle is stated in terms of three generic strategies. In large projects, these strategies have to be combined and redefined in practice. Software packages, for instance, often have to be tailored to fit the needs of the company, thus calling for system consultants and internal developers to bring user perspectives to the project. Similarly, while using the internal development strategy for a speculative competitive application, it is possible to support the staff with consultants and other outside resources, leading to a contract management-type strategy.

The Procurement Principle states indirectly, on the basis of transaction cost economizing, that some combinations of projects and developers are inefficient. These strategies are indicated by the shadows outside the main diagonal of the procurement matrix. When innovators are used to build routine systems and relying on hierarchy in a situation favoring markets, unnecessarily high costs are incurred (the “high cost” corner). Similarly, when implementors are used to supply a package for a speculative application without support from consultants or own experts, the company is subjected to unnecessary risks of an inappropriate system or broken confidentiality (the “high risk” corner). Sometimes, for reasons of management policy, for example, companies use only internal resources, or they rely entirely on markets. According to the Procurement Principle, management has deliberately chosen to ignore the costs and risks of IS development in many typical situations.

We should note, however, that to some extent one may compensate for inefficient procurement decisions by taking corrective actions during the implementation phase $[15]$ . High cost can be reduced by using rational implementation approaches and high risk can be reduced by relying more on experimental implementation strategies. Moreover, it is possible to reduce both cost and risk simultaneously in some cases by establishing a joint project with other user companies or system providers. Earlier, during the specification phase, decomposition of the project into subprojects with distinct systems characteristics or deployment of teams from different developer groups may resolve at least some of the original procurement problems.

Type of Information System  
![](/api/attachments/SJBYQVGH/fulltext/images/186574487e58510bafb18cc861e9fbafbb9015e8ecb2c7ee969158f5b597aa33.jpg)  
Figure 3. Efficient Procurement Strategies Matching Type of Information Systems and Type of Developers

The Procurement Principle expressed in the strategy matrix in figure 3 is sensitive to the proper classification of the projects and developers. Two types of errors can be made. First, a project may be misplaced in either dimension of the matrix by estimation error, such as taking a routine system for a standard system. Avoiding such an estimation error calls for exact measures for classifying both systems and developers. Second, a more profound error may be committed by accepting an improper system design or a developer of undesirable qualities. For example, a speculative investment is assumed above to have a company-specific design and to involve a high level of uncertainty at the same time. How, then, is a project with a company-specific design but with extremely certain requirements to be treated—as a speculative investment or as a routine system? Similarly, would the user organization have to worry about a technology-oriented developer pushing perhaps unrealistically sophisticated and expensive solutions? The first type of error is an estimation error, and it can be avoided by using relative measures or, better still, by general calibration of the dimensions for classification. The second type of error is managements' failure in system specification or sourcing of developers, or both.

## 3. Empirical Tests

THE ABOVE ANALYSES EMPHASIZE THE CHARACTERISTICS of the systems and developers—and proper matching of the two—as the foundation for effective procurement strategies. In this section, the resulting Procurement Principle is used to empirically study information system development projects carried out in major Finnish companies.

## 3.1. Data Collection Procedure

For a preliminary investigation testing whether the guidelines of efficient procurement are followed in practice, we were able to use data from a survey among major Finnish organizations concerning recently implemented development projects $[14]$ . The survey was addressed to the 200 largest companies and the 25 largest banks and insurance companies in Finland; altogether, 272 IS managers were asked to contribute to the study (some companies have an IS manager in each business unit). A short questionnaire mailed to the IS managers asked for a list of all projects finished in the last two years with a brief evaluation of their success. To enable a closer review of the two most recently implemented information systems, we requested that the IS managers name these systems as well as the project manager and the user manager responsible for the system so that we might send them another, more detailed, questionnaire.

Within one month, 102 IS managers returned the questionnaire; 47 of them, however, were either unable or unwilling to participate in the study and returned an noncompleted questionnaire. The main reasons for noncompletion were that they had not implemented new information systems in the last two years, the company had been recently reorganized, the IS manager had been recently nominated, or he or she was too busy to participate. The remaining 55 companies form a representative sample of the population in terms of industry and company size. The IS managers in these companies indicated a total of 247 information systems and selected 101 of these for a detailed evaluation. Of the indicated 101 project managers and user managers, 70 and 62, respectively, responded to the questionnaire. This response rate was achieved by reminder letters and several telephone calls. Complete responses containing evaluations from both project and user managers totaled 48 forming the database used in this study. Detailed examination of these projects confirmed that they constituted a representative sample of the 247 projects completed in large Finnish companies with regard to type of system, application area, and overall level of success assessed by IS managers [14].

## 3.2. Organizations and Systems Studied

The profile of the companies showed average annual net sales in 1988 of FIM 1,906 million (FIM 1 = U.S.\$0.25), and average employment of 2,317. Two-thirds of the companies were in manufacturing, one-fifth in retailing and wholesale, less than 10 percent in banking or insurance, and the rest in the service sector.

The average budget of the information systems studied was FIM 1.2 million, the average duration of the development project 17 months, and the average of the total effort was 41 man-months. One-third of the systems under study were designed to support accounting, one-third marketing, one-fifth manufacturing, and the rest business administration or purchasing.

## 3.3. Key Variables

Here we describe the main variables used in this study. Appendix A shows the sources, scales, and descriptive statistics for each.

## Characteristics of the System

Specificity of the system was composed of two attributes: the project managers' estimates of the specificity of the supported object system and the level of using existing systems as a basis for requirements. The specificity measure was composed as an average of these two attributes. Requirements uncertainty was measured by the characteristics of the information system that cause problems to identify user needs. The detailed questions posed to project managers measured the clarity and stability of the requirements. The composite uncertainty estimate was constructed based on an average of the answers to these two questions. Correlation between the two constructed variables, specificity of the system and requirements uncertainty, was 0.29 and significant at the 0.02 level. This means that in this sample most system specifications are of a generic type. This observation led us to combine measures of specificity and uncertainty, using an average of these two variables to identify types of systems. Based on this combined variable, we divided the projects into three groups of about equal sizes: 13 routine systems, 20 standard applications, and 15 speculative investments.

## Capabilities of Developers

The business knowledge of the developer team was measured on the basis of the evaluation given by project managers concerning both system analysts' and users' knowledge of the supported business. These two items were used to establish a composite variable of developers' business knowledge. The specifications skills of developers were measured by the evaluation of project managers concerning system analysts' ability to elicit and users' ability to specify requirements for the system. An average of these two answers was used as a composite variable for specification skills. The correlation between business knowledge and specification skills was 0.59 and significant at the 0.001 level. Therefore, we concluded that the developer teams represented the generic types specified in section 2.2. An average of business knowledge and specification skills was computed and used to divide developers into three categories: 13 implementors, 18 analysts, and 17 innovators.

## Procurement Strategy

Procurement strategies were classified by the allocation of the development effort between a company's own and its outside resources. It was known also whether the implementation was based on a software package and whether the package was extensively tailored. Based on this information, the projects were classified into five categories: 16 internally developed systems, 8 projects employing a construction management strategy, 12 projects relying on a contracting strategy, 7 projects tailoring a software package, and 5 projects implementing a software package without major modifications. The average use of outside resources in internally developed projects was 2.68 percent, in projects using contract management strategy 34.25 percent, and in projects using contracting strategy 69.41 percent.

## Success Variables

The success of the project was measured by using perceptions of project and line managers concerning different attributes of success. These perceptions were converted into a measurement instrument in four dimensions: success of the development process, success of the use process, quality of the IS product, and impact of the IS on the organization (for details, see [13]). Success of the development process is measured by the evaluation, after implementation, of the adequacy of IS staff and user abilities, success of the development phases, and controllability of the development process. Success of the use process is evaluated as the adequacy of the capabilities of IS staff and users involved in the use process, effective communication between them, and consequent responsive IS services. Quality of the IS product is measured by the quality and flexibility of user interface and format, and the reliability and relevancy of the information provided to the users. Impact of the IS on the organization is measured by the changes that occur through use of the system with positive impact on the organization's efficiency and profitability, on decision making and control, as well as on the communication processes and possible reorganization. Only the constructed summary variables are used in this study. The construction principles for them are described in more detail in appendix B and in [13].

## 3.4. Findings

In this section, we first describe what procurement strategies have been used in different situations. We then analyze the implications of adhering to the Procurement Principle on the success of the studied projects.

## Use of Procurement Strategies

Use of procurement strategies for different kinds of systems is illustrated in Table 1. It seems that the Procurement Principle describes managers' choices for routine systems rather poorly. There seems to be a tendency to use an internal development strategy even when the characteristics of the situation indicate use of market resources or acquisition of a software package. Even though there seem to be some projects relying on markets for speculative investments, the Procurement Principle seems to describe strategy choices better for this kind of system.

Table 1 Procurement Strategies Used for Different Types of Systems

<table><tr><td rowspan="2">System type</td><td colspan="5">Procurement strategy</td></tr><tr><td>Internal development</td><td>Contract management</td><td>Contracting</td><td>Tailoring a package</td><td>Software package</td></tr><tr><td>Speculative investment</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td></tr><tr><td>Standard application</td><td>6</td><td>2</td><td>5</td><td>4</td><td>3</td></tr><tr><td>Routine systems</td><td>5</td><td>2</td><td>4</td><td>1</td><td>1</td></tr></table>

Table 2 Developers Assigned for Different Types of Systems

<table><tr><td rowspan="2">System type</td><td colspan="3">Developer type</td></tr><tr><td>Innovators</td><td>Analysts</td><td>Implementors</td></tr><tr><td>Speculative investment</td><td>6</td><td>5</td><td>4</td></tr><tr><td>Standard application</td><td>5</td><td>9</td><td>6</td></tr><tr><td>Routine system</td><td>6</td><td>4</td><td>3</td></tr></table>

The developers assigned for the projects are presented in Table 2. There seems to be no relationship between the characteristics of systems and developers. Developers varying in level of business knowledge and specification skills have been used to develop all kinds of systems. These initial results show that the Procurement Principle does not describe the strategies used in practice, at least not for all kinds of systems; nevertheless, whether it may indicate the strategies managers should use is an interesting question.

## Implications for Project Success

In order to see if management could do better by following the Procurement Principle more closely, we analyzed separately the implications of using different kinds of procurement strategies and developers in each of the three groups of systems.

According to the Procurement Principle, for routine systems, one should use software packages and outside resources, which are less expensive and still produce results comparable to those achieved by internal developers. Consequently, we tested if there were any differences in success between projects relying on markets compared with those that rely on internal development or contract management strategies.

Table 3 Success in projects with Routine Systems Using Internal Development and Contracting Management as Compared with Relying on Markets (Mean Ranks from Mann Whitney Tests)

<table><tr><td rowspan="2">Routine systems (n = 13)</td><td colspan="3">Procurement strategy</td></tr><tr><td>Internal development or contracting</td><td>Market-based implementation</td><td>Significance</td></tr><tr><td>Success of the development process</td><td>8.14</td><td>5.67</td><td>0.25</td></tr><tr><td>Success of the use process</td><td>6.44</td><td>7.42</td><td>0.72</td></tr><tr><td>Quality of the IS product</td><td>7.86</td><td>6.00</td><td>0.39</td></tr><tr><td>Impact of the IS on the organization</td><td>8.07</td><td>5.75</td><td>0.28</td></tr><tr><td>Number of projects</td><td>7</td><td>6</td><td></td></tr></table>

Table 3 shows the results of Mann Whitney tests. As the mean ranks in each strategy group and significance levels show, there were no differences in any of the success criteria used. Using Kruskal Wallis analyses of variance, we also analyzed if the developers with differing levels of skills had any effects on success. The mean ranks and significance levels in Table 4 show that the different kinds of developers used to produce routine systems did not influence success. These results indicate that the projects in which the procurement strategies were chosen according to the Procurement Principle may have been doing better than the other projects. The resulting systems are of comparable levels of success but presumably accrued lower development costs. In any case, these companies have been able to use their best developers—the innovators—for developing systems with more challenging requirements.

According to the Procurement Principle, standard applications are suitable for contracting and contract management strategies. When using internal development and most qualified developers, one may incur extra cost while less expensive outside resources could provide systems with similar qualities. When relying on software packages, on the other hand, it is possible that the success of the project will be low, since the functionality of the package may not satisfy the users or expensive changes may be required. Furthermore, according to the Procurement Principle, the use of developers with low skills (i.e., implementors) is risky.

Table 5 presents the results of Kruskal Wallis analyses of variance testing differences of project success when using internal development strategy, contracting or contract management strategies, or acquiring and tailoring software packages. The mean ranks and significance levels show that there were no differences between these three different procurement strategies for standard applications. We expected packages to result in lower success than other strategies, but this was not the case. However, the fact that there was no difference in success between favoring the internal strategy over the contracting or contract management strategies is more in line with the Procurement Principle.

Table 4 Success in Projects with Routine Systems Using Different Types of Developers (Mean Ranks from Kruskal Wallis Analyses of Variance)

<table><tr><td rowspan="2">Routine systems (n = 13)</td><td colspan="4">Developer type</td></tr><tr><td>Innovators</td><td>Analysts</td><td>Implementors</td><td>Significance</td></tr><tr><td>Success of the development process</td><td>7.50</td><td>5.00</td><td>8.67</td><td>0.42</td></tr><tr><td>Success of the use process</td><td>7.25</td><td>5.80</td><td>8.50</td><td>0.58</td></tr><tr><td>Quality of the IS product</td><td>5.50</td><td>8.50</td><td>8.00</td><td>0.43</td></tr><tr><td>Impact of the IS on the organization</td><td>5.67</td><td>8.38</td><td>7.83</td><td>0.51</td></tr><tr><td>Number of projects</td><td>6</td><td>4</td><td>3</td><td></td></tr></table>

Table 6 gives results from Kruskal Wallis analyses of variance testing differences of success in projects with different types of developers. The mean ranks and significance levels show that there was a significant difference in the impact of the IS on the organization: implementors produced lowest levels of impact and innovators were the most successful developers. This finding clearly supports the Procurement Principle.

When the system is specified as speculative, it is unlikely that one could succeed by acquiring a software package and fitting it to the specifications. Such extensive tailoring would require a lot of extra effort, and the supplier would be reluctant to expend such effort, at least not at a competitive price just for one customer. Speculative systems have to be specially made by the most qualified developers—the innovators—as indicated in the Procurement Principle.

Table 7 shows results from Mann Whitney tests comparing the differences in success of the projects developing specially made systems with those relying on package solutions for speculative system investments. Only three projects out of fifteen were based on software packages. Furthermore, those using packages produced systems with a significantly lower quality than the specially made systems. These findings support the Procurement Principle, which prescribes the strategy choices in the case of speculative systems rather well.

Using Kruskal Wallis analyses of variance for each of the four success criteria, the success of speculative projects employing high-quality developers (i.e., innovators) was compared with the success of projects using other types of developers. The mean ranks and significance levels in Table 8 show no differences in success between the three groups of development teams, thereby indicating a deviation from prescription of the Procurement Principle.

Table 5 Success in Projects with Standard Application Using Internal Development Strategy, Contracting and Contract Management Strategies, or Software Packages (Mean ranks from Kruskal Wallis Analyses of Variance)

<table><tr><td rowspan="2">Standard applications (n = 20)</td><td colspan="4">Procurement strategy</td></tr><tr><td>Internal development</td><td>Contracting of contracting management</td><td>Software packages</td><td>Significance</td></tr><tr><td>Success of the development process</td><td>10.42</td><td>12.43</td><td>8.64</td><td>0.48</td></tr><tr><td>Success of the use process</td><td>7.83</td><td>13.43</td><td>9.86</td><td>0.22</td></tr><tr><td>Quality of the IS product</td><td>12.83</td><td>11.57</td><td>7.43</td><td>0.21</td></tr><tr><td>Impact of the IS on the organization</td><td>8.83</td><td>12.79</td><td>9.64</td><td>0.43</td></tr><tr><td>Number of projects</td><td>6</td><td>7</td><td>7</td><td></td></tr></table>

Table 6 Success in Projects with Standard Applications Using Different Types of Developers (Mean ranks from Kruskal Wallis Analyses of Variance)

<table><tr><td rowspan="2">Standard applications (n = 20)</td><td colspan="4">Developer type</td></tr><tr><td>Innovators</td><td>Analysts</td><td>Implementors</td><td>Significance</td></tr><tr><td>Success of the development process</td><td>11.50</td><td>12.44</td><td>6.75</td><td>0.17</td></tr><tr><td>Success of the use process</td><td>12.80</td><td>11.06</td><td>7.75</td><td>0.34</td></tr><tr><td>Quality of the IS product</td><td>9.10</td><td>11.67</td><td>9.92</td><td>0.70</td></tr><tr><td>Impact of the IS on the organization</td><td>14.50</td><td>11.00</td><td>6.42</td><td>0.07</td></tr><tr><td>Number of projects</td><td>5</td><td>9</td><td>6</td><td></td></tr></table>

Table 7 Success in Projects with Speculative Investments Relying on Specially Made Systems or Software Packages (Mean Ranks from Mann Whitney Tests)

<table><tr><td rowspan="2">Speculative investments (n = 15)</td><td colspan="3">Procurement strategy</td></tr><tr><td>Specially made systems</td><td>Software packages</td><td>Significance</td></tr><tr><td>Success of the development process</td><td>8.58</td><td>5.17</td><td>0.31</td></tr><tr><td>Success of the use process</td><td>8.83</td><td>6.67</td><td>0.56</td></tr><tr><td>Quality of the IS product</td><td>9.29</td><td>2.83</td><td>0.02</td></tr><tr><td>Impact of the IS on the organization</td><td>8.54</td><td>5.43</td><td>0.34</td></tr><tr><td>Number of projects</td><td>12</td><td>3</td><td></td></tr></table>

In conclusion, even though some support was found for the Procurement Principle, it was not fully confirmed in our empirical investigation. In many cases managers were behaving according to the predictions of the Procurement Principle, and, if not, it had implications on project success. But the few deviations from the model clearly call for further empirical studies to learn more about the actual practices of organizing and managing the procurement of information systems.

## 3.5. Limitations of the Study

There are some limitations in the empirical tests reported here. The data were initially collected for another study, and, consequently, we felt that some of the variables might not be best suited for operationalizing the main concepts of the Procurement Principle. The sample size was rather small and we used nonparametric statistical analyses. Hence, the results are tentative and should be regarded as an initial test of the framework in an attempt to interpret the procurement decisions and their implications in the organizations studied.

Other potential problems in our data collection include: First, the splitting of the sample on the basis of relative measures into groups of approximately equal size may not have been an adequate technique: some projects classified as speculative may have been just a little bit more specific and uncertain than the other projects in the sample, but not necessarily speculative in any absolute sense. A similar error may have occurred when classifying the developers. This sort of estimation error in using the relative measures may have affected our results. Second, the sample may be biased toward major development projects in large companies. These projects involved a thorough specification of requirements, and the solutions consequently tend to become specially made or tailored to meet the company's needs. Furthermore, it is well known that, unlike many other countries, Finland has a tradition of relying more on internal development. The special laws and accounting and labor regulations of a small country, along with a less widely spoken language, substantially limit the number of suitable packages and other alternatives available in the marketplace. While this cultural bias may help explain some of the anomalies of the data, it also makes a case for conducting a comparative study in a country with a more active market for software packages and development services.

Table 8 Success in Projects with Speculative Investments Using Different Types of Developers (Mean Ranks from Kruskal Wallis Analyses of Variance)

<table><tr><td rowspan="2">Speculative investments (n = 15)</td><td colspan="4">Developer type</td></tr><tr><td>Innovators</td><td>Analysts</td><td>Implementors</td><td>Significance</td></tr><tr><td>Success of the development process</td><td>7.77</td><td>7.00</td><td>10.50</td><td>0.42</td></tr><tr><td>Success of the use process</td><td>7.67</td><td>7.70</td><td>8.88</td><td>0.90</td></tr><tr><td>Quality of the IS product</td><td>7.88</td><td>7.70</td><td>9.81</td><td>0.59</td></tr><tr><td>Impact of the IS on the organization</td><td>6.92</td><td>6.90</td><td>11.00</td><td>0.29</td></tr><tr><td>Number of projects</td><td>6</td><td>5</td><td>4</td><td></td></tr></table>

## 4. Conclusions

WE HAVE DEVELOPED A PRESCRIPTIVE MODEL OF MAKE-OR-BUY decisions for information system investments. The main idea is to assign appropriate developers to different systems to yield efficient procurement strategies. Some preliminary tests of the model with empirical data on management choices in major Finnish companies indicated that the actual behavior, especially in the case of speculative investments, can be explained relatively well. Furthermore, it was found that the recommendations, expressed as the Procurement Principle, have some potential to explain success of development projects as well. Although the principle can assist practicing managers in their decisions on procurement strategies, deviations from the Procurement Principle were detected, and these deviations call for more empirical evidence to fully confirm the recommendations.

The proposed approach to information systems procurement extends the conventional development principles by bringing markets and outside resources as potential alternatives to internal development even in large and sophisticated projects. This may require decomposition of an in-house project into subprojects, some of which could be contracted out to suppliers while others may be bought off-the-shelf. In some cases, joint projects among several companies may allow sharing of costs and risks of systems.

Further studies will be directed toward confirming our preliminary results and elaboration of the model by including, for example, interorganizational systems, network infrastructures, and end-user computing to allow the analysis of complete systems portfolios.

## REFERENCES

1. Apte, U.M., and Vepsäläinen. A.P.J. High tech or high touch? efficient channel strategies for delivering financial services. Journal of Strategic Information Systems, 2, 1, (March 1993), 39–54.

2. Arrow, K. The organization of economic activity: issues pertinent to the choice of market versus nonmarket allocation. The Analysis and Evaluation of Public Expenditure: The PPB System, Vol.1. U.S. Joint Economic Committee, 91st Congress, 1st Session, Washington, DC: U.S. Government Printing Office, 1969, pp. 59–73.

3. Beath, C. Strategies for managing MIS projects: a transaction cost approach. In C.A. Ross and E.B. Swanson (eds.), The Proceedings of the Eighth International Conference on Information Systems. December 6–9, 1987, Pittsburgh, PA, pp. 415–427.

4. Burns, R.N., and Dennis, A.R. Selecting an appropriate application development methodology. DATA BASE (Fall 1985), 19–23.

5. Davis, G.B. Strategies for information requirements determination. IBM Systems Journal, 21, 1 (1982), 4–29.

6. Gremillion, L.L., and Pyburn, P. Breaking the systems development bottleneck. Harvard Business Review (March–April 1983), 130–137.

7. Iivari, J. Implementability of in-house vs. application package based information systems. In L. Maggi, R. Zmud, and J. Wetherbe (eds.), Proceedings of the Seventh International Conference on Information Systems. December 15–17, 1986, San Diego, pp. 67–80.

8. Koskela, L. and Vepsäläinen, A. A model of procurement services for construction projects. The Fourth Yugoslav Symposium on Organization and Management in Construction. Dubrovnik, Yugoslavia: 1991.

9. Loh, L., and Venkatraman, N. Determinants of information technology outsourcing: a cross sectional analysis. Journal of Management Information Systems, 9, 1, (Summer 1992), 7–24.

10. Mathiassen, L., and Stage, J. Complexity and uncertainty in software design. Proceedings of the IEEE (1990), 482–489.

11. Cash, J.I., Jr.; McFarlan, F.W.; McKenny, J.L.; and Vitale, R.V. Corporate Information Systems Management—Text and Cases, 2d ed. Homewood, IL: Irwin, 1988.

12. Mäkelin, M., and Vepsäläinen, A. Service Strategies: Services, Distribution Channels and Information Technology [in Finnish]. Espoo Finland: HM&V Research Oy, 1991.

13. Saarinen, T. Perceived success of an information system investment. Working Paper F-292, Helsinki School of Economics, 1991.

14. Saarinen, T., and Sääksjärvi, M. Success of information systems in large Finnish organizations. Helsinki School of Economics, Series D:116, 1989.

15. Saarinen, T., and Vepsäläinen, A. Managing the risks information of information system implementation. European Journal of Information Systems, 2, 4 (October 1993), 283–295.

16. Vepsäläinen, A., and Apte, U. The impact of information technology on financial services delivery. Working paper #12-01-87, Department of Decision Sciences, University of Pennsylvania, 1987.

17. Vepsäläinen, A., and Koskela, L. Normative guidelines for procuring a construction

project. Unpublished Working Paper, Helsinki School of Economics, 1989.

18. Whang, S. Contracting for software development. Management Science, 38, 3 (1991), 307–324.

19. Williamson, O.E. The Economic Institutions of Capitalism. New York: The Free Press, 1985.

Appendix A: Key Variables Used in the Study

<table><tr><td>Procurement strategy</td><td>Scale</td><td>Source</td><td>Mean</td><td>Std. dev.</td></tr><tr><td>Internal:</td><td></td><td></td><td></td><td></td></tr><tr><td>Internally developed</td><td>0/1</td><td>PM</td><td>0.33</td><td>—</td></tr><tr><td>Contract management:</td><td></td><td></td><td></td><td></td></tr><tr><td>Developed together by internal and outside resources</td><td>0/1</td><td>PM</td><td>0.17</td><td>—</td></tr><tr><td>Contracting:</td><td></td><td></td><td></td><td></td></tr><tr><td>Developed mainly by outside resources</td><td>0/1</td><td>PM</td><td>0.25</td><td>—</td></tr><tr><td>Tailored package:</td><td></td><td></td><td></td><td></td></tr><tr><td>Software package that was modified extensively</td><td>0/1</td><td>PM</td><td>0.15</td><td>—</td></tr><tr><td>Package:</td><td></td><td></td><td></td><td></td></tr><tr><td>Software package</td><td>0/1</td><td>PM</td><td>0.10</td><td>—</td></tr><tr><td>System type</td><td></td><td></td><td></td><td></td></tr><tr><td>Uncertainty of requirements</td><td>1-7</td><td>Constructed</td><td>3.08</td><td>1.15</td></tr><tr><td>Composite of the following variables:</td><td></td><td></td><td></td><td></td></tr><tr><td>Clarity of requirements</td><td>1-7 R</td><td>PM</td><td>4.85</td><td>1.30</td></tr><tr><td>Stability of requirements</td><td>1-7 R</td><td>PM</td><td>4.98</td><td>1.41</td></tr><tr><td>Specificity of system</td><td>1-7</td><td>Constructed</td><td>3.81</td><td>1.18</td></tr><tr><td>Composite of the following variables:</td><td></td><td></td><td></td><td></td></tr><tr><td>Specificity of object system</td><td>1-7 R</td><td>PM</td><td>3.85</td><td>1.59</td></tr><tr><td>Extent of having existing systems as a basis for requirements</td><td>1-7</td><td>PM</td><td>4.52</td><td>1.59</td></tr><tr><td>Developer type</td><td></td><td></td><td></td><td></td></tr><tr><td>Business knowledge</td><td>1-7</td><td>Constructed</td><td>5.15</td><td>1.05</td></tr><tr><td>Composite of the following variables:</td><td></td><td></td><td></td><td></td></tr><tr><td>System analysts' object system knowledge</td><td>1-7</td><td>PM</td><td>4.35</td><td>1.62</td></tr><tr><td>Users' object system knowledge</td><td>1-7</td><td>PM</td><td>5.94</td><td>1.10</td></tr><tr><td>Specification skills</td><td>1-7</td><td>Constructed</td><td>4.52</td><td>1.04</td></tr><tr><td colspan="5">Composite of the following variables:</td></tr><tr><td>System analysts' ability to elicit user requirements</td><td>1-7</td><td>PM</td><td>4.81</td><td>1.44</td></tr><tr><td>Users' ability to specify requirements</td><td>1-7</td><td>PM</td><td>4.23</td><td>1.39</td></tr><tr><td colspan="5">Success of the project—summary variables</td></tr><tr><td>Success of the development process</td><td>1-7</td><td>Constructed</td><td>4.70</td><td>0.74</td></tr><tr><td>Success of the use processes</td><td>1-7</td><td>Constructed</td><td>5.01</td><td>0.83</td></tr><tr><td>Success of the IS product</td><td>1-7</td><td>Constructed</td><td>4.32</td><td>0.80</td></tr><tr><td>Impact of the IS on the organization</td><td>1-7</td><td>Constructed</td><td>4.42</td><td>0.78</td></tr><tr><td colspan="5">PM = Project manager responsible of the development project; R = reverse scale. Appendix B describes construction principles for success variables in more detail.</td></tr></table>

## Appendix B: Dependent Variables

## Success of the Development Process

Success of the development process is constructed as an average of the users' and system analysts' abilities (after the implementation), success of the development phases, and controllability of the project. Users' abilities is an average of the DP knowledge, knowledge about supported business, ability to communicate and commitment to the project (including management commitment) assessed by the project manager, except the knowledge about the supported business by the line manager. System analysts' abilities is an average of the DP knowledge, knowledge about supported business, ability to communicate, and commitment to the project assessed by the line manager except DP knowledge by the project manager. Success of development phases is an average of the success of requirement specification, analysis and design, technical implementation, and installation and startup phases evaluated by the project manager. Controllability of the project is an average of the adherence to development schedule and development budget evaluated by the line manager. All questions apply seven-point scales.

## Success of the Use Process

Success of the use process is constructed as an average of the user knowledge and involvement, abilities of the IS staff, and responsive IS services. User knowledge and involvement is an average of the training provided to users, users' knowledge about systems, and user participation in development projects. Abilities of the IS staff is an average of their attitude toward the users, relationships with the users, and communication capabilities. Responsive IS services is an average of the flexibility to change existing systems and time needed for new development. All questions are answered by the line manager in seven-point scales.

## Quality of the IS Product

Quality of the IS product is constructed as an average of the quality of user interface, flexibility of the system and quality, contents, and format of output information provided by the system. Quality of user interface is an average of the systems performance, response times, user friendliness, and ease of use. Flexibility of the system is an average of the flexibility to change the existing functions and add new functions to the system. Information quality is an average of the precision, accuracy, and reliability of output information provided by the system. Information contents is an average of the completeness, relevance, timeliness, and up-to-datedness of output information provided by the system. Information format is an average of the format and clarity of output information provided by the system. All questions are answered by the line manager in seven-point scales.

## Impact of the IS on the Organization

Impact of the IS on the organization is an average of the use and consequent changes, improved efficiency and profitability, improved decision making and control, and improved communication and restructuring of the organization. Use and changes is an average of the extent of using the system and extent of improvements due to introduction of the system. Efficiency and profitability is an average of the profitability, price performance ratio, improved work processes, cost savings, and improved efficiency. Decision making and control is an average of the improved decision making, improved organizational control, and improved effectiveness. Communication and reorganization is an average of the improved internal communication, improved interorganizational communication, improved organization structure, and improved data processing. All questions are answered by the line manager in seven-point scales.
