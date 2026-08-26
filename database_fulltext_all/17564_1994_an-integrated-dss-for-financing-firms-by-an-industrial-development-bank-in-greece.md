---
otero_id: 17564
otero_key: "E87UU8WP"
title: "An integrated DSS for financing firms by an industrial development bank in Greece"
authors: "Y. Siskos; C. Zopounidis; A. Pouliezos"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90013-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An integrated DSS for financing firms by an industrial development bank in Greece

Y. Siskos, C. Zopounidis and A. Pouliezos
Technical University of Crete, 73100 Chania, Greece

This paper presents an integrated DSS for the analysis and financing of firms by an industrial development bank in Greece. Firstly, the system evaluates the financial performance of firms (financial ratios of profitability, managerial performance, solvency) during a 5-year period and allows inferences about their development tendencies. Furthermore, multivariate statistical techniques (discriminant analysis, principal components analysis) are available to aid in the identification of the most significant financial ratios and in the grouping of the firms in coherent categories. Finally, a multicriteria method is used, which ranks the firms from the most dynamic to the bankrupt and in this way dynamic to the bank to select the less risky for financing. The capabilities of the system are illustrated with actual data provided by the bank.

Keywords: Financial analysis; Corporate risk assessment; Multivariate statistical methods; MCDM methods, DSS.

![](/api/attachments/E87UU8WP/fulltext/images/3cd3613048d84997e9189d21111cbcb5e94ef40b5732a59603cc01daac154b66.jpg)

Yannis Siskos received his Doctorat d'Etat (1984) in management science from the University "Paris-Dauphine", a Diploma in Mathematics from the University of Athens (1973), a D.E.A. (1977) and a Doctorat 3 $^{e}$ Cycle (1979) in computer science and operations research from the University "Pierre et Marie Curie" in France. He is Professor of operations research at the Technical University of Crete and the director of the Decision Support Systems Lab-

oratory at the Department of Production Engineering and Management. He was Maitre-Assistant at the University Paris-Dauphine, 1982–84. His research interests are in the area of multiple criteria decision making and the design and development of decision support systems for large scale managerial tasks. He is the author of over 40 articles in refereed journals.

Correspondence to: Y. Siskos, Technical University of Crete, Decision Support Systems Laboratory, 73100 Chania, Greece.

## 1. Introduction

Deciding to finance viable firms is today a major problem for financial organisations (credit institutions, banks). These organisations, whose basic limitation is the lack of enough funds, must invest their capital in best possible way.

For a financial organisation, the primary element in the assessment of a firm is to evaluate the risk that is involved. According to Chevalier, Hirsch (1982), there are four main components of corporate risk: commercial, financial, managerial and industrial.

In recent years, new methods of assessing a firm's risk were developed, which thanks to the advancements of computer and information science, offer the financial organisations' top personnel significant aid in the selection of the best firms

![](/api/attachments/E87UU8WP/fulltext/images/c49c2b547fc59d8f081344da7ee5dcd05f70511e5e5cd81085c713825b812d26.jpg)

Constantin Zopounidis received his Doctorat d'Etat (1986) in management science, a D.E.A. (1982) in financial management from the University of Paris-IX Dauphine and a B.A. in Business Administration from the Macedonian University of Thessaloniki. He is Assistant Professor of financial management at the Technical University of Crete and a member of the Decision Support Systems Laboratory at the Department of Production Engineering and Management.

He has over 20 published articles appearing in European Journal of Operational Research, Global Finance Journal, Computer Science in Economics and Management, Foundations of Computing and Decision Sciences, among others. His current research interests are in the area of financial management and the design/development of multicriteria decision support systems for financial analysis and planning.

![](/api/attachments/E87UU8WP/fulltext/images/c6852465c09d7f230b59de3d8ef834ebf2f9b0de716ef13d797e47ddcc40dc7b.jpg)

Dr. A. Pouliczos is an Assistant Professor in the Dept. of Production Engineering and Management at the Technical University of Crete, Chania. His research interests include applications of computer science in finance, stochastic systems, fault diagnosis in dynamical systems and neural networks applications. He received his BSc. degree from the Polytechnic of N. London in Mathematics and Computing in 1975, his MSc. degree in Control Systems from Imperial Col lege in 1976 and his PhD. from Brunel University in 1980.

for financing. Firstly, there were developed statistical tools based on multivariate statistical methods (e.g. discriminant analysis, cluster analysis) which rank companies in levels of risk, and/or calculate a score representing the degree of risk using those financial ratios which are considered as significant. The commonest methods are those of “credit scoring”, which establish a discriminant function using some of the company's financial ratios, and rank them in high-risk or low-risk groups (Altman, 1983, 1984). Later, tools developed which based on multicriteria decision making methods (MCDM) also rank companies in levels of risk (Brans, Maréchal, 1990; CNME, 1973; Zollinger, 1982; Zopounidis, 1987) using criteria considered as significant. The use of multicriteria decision making methods in the assessment of a firm's risk circumvents many of the problems that exist by using discriminant analysis (Eisenbeis, 1977). Finally, tools based on artificial intelligence were developed which were originally called expert systems, then expert support systems or knowledge-based decision support systems and which were constructed for the company assessment and business loan evaluation, for the financial diagnosis of the company and for analyzing corporate creation projects (Bouwman, 1983; Duchessi, Belardo, 1987; Klein, Methlic, 1990; Shaw and Gentry, 1988; Srinivasan, Kim, 1988; Srinivasan, Ruparel, 1990). The development of neural networks based on this philosophy seems to be an interesting alternative to discriminant analysis (cf. Dutta and Shekhar, 1992; Tam and Kiang, 1992).

![](/api/attachments/E87UU8WP/fulltext/images/fd0b7441342c393ddd56073d3f294eeb8726be7e1d6a3ba1014770558d90c9a6.jpg)  
Fig. 1. The components of the DSS.

In this paper is presented an integrated Decision Support System (DSS) for the analysis, evaluation and final selection of firms for financing. The DSS is based on two types of methods: (1) multivariate statistical methods, as principal components analysis and discriminant analysis, and (2) MCDM methods, as the MINORA system (Multicriteria INteractive Ordinal Regression Analysis). It aims at, (1) the forecasting and prevention of difficulties that firms face and consequently, the elimination of high risks in financing operations such as participation in capital (venture capital); (2) the upgrading of financial art and (3) supporting the managerial personnel of firms. Specifically, this DSS was developed for a Greek Industrial Development Bank (ETEVA), which finances industrial and commercial firms in Greece. The financing that was done by this bank from 1964 to 1990 is the following (in million drs): 1964–73: 7502; 1974–78: 12945; 1979–83: 21450; 1984: 5134; 1985: 3403; 1986: 6950; 1987: 10429; 1988: 11231; 1989: 15948; 1990: 16658. Specifically, for 1990 ETEVA financed 56 firms with average financing capital of 297 million drs. Today, ETEVA apart from the classical activity of financing firms, is involved in new financial activities such as underwriting of stock issues, mergers and acquisitions and financial advisory services, treasury services, bond issues and syndicated loans and fund management services.

The basic advantages, which differentiate this system from the aforementioned ones are the following: (1) it is used, either for a simple description of the firms' characteristics or for the classification of firms in risk groups or for the ranking of the firms from the most promising to the most risky and untrustworthy; (2) qualitative criteria are used such as commercial, managerial and production for a concrete analysis of corporate risk and (3) there is complete interaction amongst all the subsystems of the DSS.

In section 2 the guidelines for DSS development are given. Section 3 gives the description of the DSS. Section 4 presents some experience with the system and, in conclusion, the merits of this system and possible future research directions in the field of corporate assessment are discussed.

## 2. Guidelines for DSS designing

The theoretical framework for designing a DSS for banks was developed for the first time by Sprague and Watson (1976). The authors distinguish three types of models: strategic, tactical and operational and in every type of model, corresponds the relevant data. The corporate risk assessment models belong to the operational models category and need historical data (balance sheet and income statement) for the analysis and assessment of firms. The basic components of the proposed system are presented in Figure 1.

The analysis of a firm requires the basic financial statements, i.e. balance sheet and income statement. In order to perform a reliable and complete study of a firm, consecutive basic financial statements for at least three years for every company must be available. A number of consecutive basic financial statements help the decision maker to verify the conditions under which the company has grown and to form important trends for certain classes of accounts of the balance sheet, and/or of the income statement.

Apart from the financial data that are contained in the basic financial statements, the decision maker ought to possess additional information of a more general character, so that his evaluation would be as objective and complete as possible. Such information about a company may be: its size, industrial sector, structure of shareholder's capital, personnel, market, market share, quality of management, etc. This qualitative information is sometimes more important than the financial, because if, for example, the company does not have good managers, its financial results (sales, net income) will not be satisfactory. This information will be used as evaluation criteria in the MCDM method.

The model base of the system must include the following models:

\- financial analysis;

\- multivariate statistical methods: principal components analysis and discriminant analysis;

• corporate risk models (credit scoring models);

\- multicriteria decision-aid models.

Financial analysis performs a detailed study of the companies, based on their financial statements. More specifically it determines: common-size statements (or common-size ratios), financial ratios and graphs of the evolution of the ratios. The common-size statements provide a quick and effective method for developing a system of very useful financial ratios (common-size ratios). To calculate these ratios, the components of the balance sheet are expressed as a percentage of total assets (liabilities + equity) and the components of the income statement as a percentage of total revenues (sales).

Financial ratios have become an accepted evaluative technique of financial analysis. They offer a quantitative view of every element that concerns the internal operation of a firm as well as its relations with the outer world, and permit fast processing of a large volume of financial data. In the literature one can find various methodologies for the classification of financial ratios in predetermined classes. Financial ratios have already been used in many fields of financial management. Lee (1985) has grouped every financial ratio that has been used in the forecasting of firm failure, bond rating, market return and mergers. In the proposed financial analysis, the classification methodology developed basically by Courtis (1978) is adopted. That is, ratios are classified into three basic classes: profitability, managerial performance and solvency.

The next step in the procedure of corporate evaluation risk is the global evaluation of the companies by using multivariate statistical methods (with the corporate risk models) and multicriteria decision-aid models.

Multivariate statistical models include principal components analysis, discriminant analysis and corporate risk models, based on the results of discriminant analysis. These data analysis techniques are widely used in problems of corporate financial management (Altman et al., 1981; Altman, 1983; Lee, 1985).

The principal components analysis is a factor method of descriptive character. In the case of corporate assessment, the principal components analysis shows initially the financial ratios which are the most important and which best describe the behaviour of the firms and then groups these firms in relevant categories, signifying in this way that firms which belong to the same group have similar characteristics and behaviour.

The discriminant analysis is a factor method of analytical character. In the case of corporate risk assessment, discriminant analysis shows initially those financial ratios that best contribute to the separation of the firms in groups (discriminant power of the variables) and then repositions in its original group a firm for which there are known the value of every financial ratio and that it belongs to one of the two groups (bankrupt firms and non-bankrupt firms). The repositioning of the firm in its original group is done using a geometric or economic criterion. This type of discriminant analysis is called “with decisive aim” (Altman et al., 1981; Altman, 1983).

The corporate risk models or credit scoring models result from the discriminant analysis and constitute until today accepted bankruptcy risk evaluation models. It is possible to state that every country has today a credit scoring model (Altman, 1984). Some well known models to use are: Altman (1968); Altman et al. (1974); Altman, Lavalee (1981); Banque de France (1983).

A contemporary philosophy for approaching decision problems of multidimensional character is multicriteria analysis (Roy, 1985; Zeleny, 1982). The MINORA decision-aid system used in the DSS is a trial and error procedure allowing the user to assess its own preference model. It has been successfully applied to some real-world managerial decision-making problems (see for instance Siskos, 1986; Siskos and Zopounidis, 1987 and Cosset et al., 1992).

MINORA uses the UTA ordinal regression model of Jacquet-Lagrèze and Siskos (1982) which estimates an additive value or utility function of the form:

$$
u (g) = u _ {1} \left(g _ {1}\right) + u _ {2} \left(g _ {2}\right) + \dots + u _ {n} \left(g _ {n}\right),
$$

where $g=(g_{1},g_{2},\ldots,g_{n})$ is the vector of performances of a firm and $u_{1},u_{2},\ldots,u_{n}$ are the estimated marginal utilities normalized between 0 and 1. UTA requires a ranking (preordering) of some reference firms (past choices,...); the utility is estimated in such a way as to give a ranking as consistent as possible with the subjective one. This ordinal regression is performed using a linear programming formulation. The MINORA system allows the user to analyse and correct the eventual inconsistencies between the two rankings by means of a ranking versus utility diagram (see section 4, Figure 19). Two consistency measures are used: (1) the F indicator, which is the sum of the positive and negative horizontal deviations from the regression curve of the diagram. In the optimal case, F = 0. (2) Kendall's $\tau$ , measuring from -1 to +1 the goodness of fit in terms of distance between the user's ranking and that resulting from the utility.

![](/api/attachments/E87UU8WP/fulltext/images/7d8b78e86708c1f951a463e6f35b263bb6e3f7af4a571756826ea800683a42f9.jpg)  
Fig. 2. The model selection menu.

## 3. Description of the DSS

It is well accepted that certain requirements (end-user usage, interactivity, reliability, ...) have to be fulfilled by DSS software (Klein and Methlie, 1990). Following Bonczek et al. (1981), if the system is to be called a DSS it will have to provide at least some sort of support for the task of problem structuring or modeling. Therefore the minimum functions a DSS should provide are the following:

\- data management,

\- display,

\- problem analysis and structuring (modeling),

• statistical or other analytical techniques.

## 3.1. The system environment

The overall architecture is seen in Figure 2. The main modules or subsystems are the following:

\- a database management system

\- a modeling subsystem

\- a display subsystem

\- a dialogue system

The implemented system has many features which are very important in a well designed software package:

\- it is device independent. It automatically selects the best (highest resolution) graphics mode to display charts and other relevant information. If desired graphics screen dumping to printers is also available.

\- there is no limit to problem dimensions other than the computer's physical memory.

\- it can be very easily converted to an other language version (including graphics text output) by a simple translation of a text file.

\- it has context-sensitive on-line help.

\- it has full-screen editors in all stages of problem development.

The package runs on IBM compatible machines

![](/api/attachments/E87UU8WP/fulltext/images/712f946c74a9364602479fb517bf86474060073a575f7c1d964aa2f2d5bffbeb.jpg)  
Fig. 3. The DBMS.

equipped with a graphics card. A mathcoprocessor, though not necessary, greatly speeds up portions of the systems. The software has been written using Microsoft's Professional Development System 7.0, which is a Quickbasic environment with support toolboxes for graphics and user ininterface. The Hammerly Probas library has also been used, providing fast assembly code routines for fast execution.

![](/api/attachments/E87UU8WP/fulltext/images/31cf98ca5055c0b2ec39f39f574613f58bb13c946689ed4e9e3b870d3febdade.jpg)  
Fig. 4. The MINORA flow chart.

The system is currently single-user. Multi-user versions can easily be developed if required.

## 3.2. The DBMS subsystem

The data handling is based on established methods of data management and their storing and retrieval are performed easily through the guidance of context sensitive help screens at every step of the procedure. One important feature of the subsystem is the use of dynamic array indices which permit the full exploitation of the computer's memory. Thus, no dimension limitations are externally imposed (i.e. from software) other than those of hardware.

The data base management system is two dimensional and the user is working with tables that have lines and columns like a spreadsheet. The user can easily travel through the data by the use of full-screen editor that permits him to scroll the data in all directions either by single steps or pages.

There are basically two data bases: (1) the main data base generated by the firms financial support system containing basic financial figures for every firm in the data base, such as net income, selling expenses etc. (for a full list see Figures 9, 10) and criteria of two types: financial ratios calculated from the financial statements and qualitative criteria supplied by the user. These data are spread over time in yearly intervals, and (2) a data base, generated from the sub-base of criteria, for the multicriteria decision model with firms as rows and criteria as columns. The user can choose which year's data are used to form this data base. Additional features of this data base include characterisation of active and non-active criteria and preference order. The data base interaction is shown in Figure 3.

Table 1  
The model base

<table><tr><td>Reasoning</td><td>Model</td></tr><tr><td>Graphical representation of firms/criteria</td><td>Histograms, Principal Components analysis</td></tr><tr><td>Grouping of firms</td><td>Discriminant analysis</td></tr><tr><td>Ranking of firms</td><td>MINORA, scoring</td></tr></table>

## 3.3. Modeling subsystem

In this subsystem there are the following models:

\- a multicriteria interactive ordinal regression analysis model (MINORA system)

\- a discriminant analysis model

\- various credit scoring models for assessing the corporate risk

\- a principal components analysis model
In Table 1 the reasoning behind each model is summarized.

![](/api/attachments/E87UU8WP/fulltext/images/5909917114445b7fa7461cd61e60bd3a4836afe3399162722480664aa99ff049.jpg)  
Fig. 5. The Principal Components Analysis Flow Chart.

As explained previously all models have access to the two data bases and the movement from one model to the other is instantaneous and is activated through menu keys. The modular architecture of the system permits the easy addition of new model subsystems. Briefly the functions of each subsystem are:

MINORA: This subsystem utilizes the data-base consisting of firms and criteria. The user can easily scroll through the spreadsheet and can easily view the results of various preordering scenarios. Each preordering scenario is solved and the solution is stored in separate files for easy comparison. This tree structure is shown in Figure 4. Each scenario's solution is then passed to the graphical module of the subsystem which depicts the results graphically. Based on the results (model and decision maker agreement or not) the user may then change various aspects of the decision making process such as the preordering of the firms or marginal value functions on the criteria (utilities), and repeat the whole process. Finally, if the user is satisfied with the results, the suggested model is extrapolated to the full set of firms. At every stage context-sensitive help is instantly available. Printer output is also activated through the function keys.

Principal Components analysis / Discriminant analysis: These two subsystems accept data from the main firm data base and perform various advanced statistical operations. The user may select any combination of firms and firm attributes (criteria, financial ratios etc.) through an interactive selection procedure. The various statistical aids offered by this modeling subsystem (Figures 5, 6) are:

Principal Components analysis;

\- eigenvalues, percentage, cumulative percentage (selection of most significant principal axes)

\- correlation matrix (correlation between financial ratios)

\- coordinates of individuals (table of similarly behaved firms)

\- coordinates of characters (table of most significant financial ratios)

\- scattering diagram (positioning of firms and financial ratios in relation to the principal axes)

Discriminant analysis;

\- Covariance matrices (intra-and inter-class correlation of financial ratios of bankrupt and non-bankrupt firms)

\- Partial F-Processing (selection of most significant financial ratios at a 5% significance level)

![](/api/attachments/E87UU8WP/fulltext/images/8dc77fb1cf99da519e5092e079af9acf54c408001ee5d839b6ac08bd93b841a5.jpg)  
Fig. 6. The Discriminant Analysis flow chart.

![](/api/attachments/E87UU8WP/fulltext/images/d9aee5567badad5b0eeca881608cfcb2329dff5e4e8a10dbfa70e68219b31607.jpg)  
Fig. 7. The Corporate risk model flow chart.

\- Discriminant function (Z-score of firms using most significant financial ratios)

\- Significance Tests (D $^{2}$ -Mahalanobis, Student's t, Fisher-Snedecor F-Statistic).

Corporate risk models: The corporate risk models are used to separate the firms in two groups, bankrupt and non-bankrupt, according to a credit score which is calculated by a discriminant function. In this DSS seven discriminant functions have been included, chosen amongst well accepted models, and shown in Figure 7.

![](/api/attachments/E87UU8WP/fulltext/images/4f6a4c73c62b21ea65e75fff0df74f27447cc74526980c5389633c57ed447e95.jpg)  
Fig. 9. Balance sheet data.

## 4. A navigation through the DSS

## 4.1. Using the data base management system

Using the data base management system the top executives of the ETEVA industrial development bank (financial managers, financial analysts) can analyse, evaluate and finally select the most promising firms. The main menu for starting the system is presented in Figure 8.

The data base contains the financial data (balance sheet and income statement) and the qualitative criteria of 39 firms for the five-year period 1985–1989. Qualitative criteria are modeled according to the preferences of each user (financial manager) with the aid of an ordinal scale (3 better than 2 and 2 better than 1).

For example, the criterion management educational background is modeled as follows: Primary education 1; Secondary education 2; Higher education 3; Graduate work 4; Post graduate work 5.

![](/api/attachments/E87UU8WP/fulltext/images/52951b73157674ce157f42b2a65999341793e1323f48c97a0277e955a913df56.jpg)  
Fig. 10. Income statement data.

![](/api/attachments/E87UU8WP/fulltext/images/849ab8a57e2d03ea47ad582af9b795d7089a10e11c48bed67be94e17c77dfd0d.jpg)  
Fig. 11. Qualitative criteria.

Figures 9–11 present the financial data and qualitative criteria for a single firm (firm F23).

Instructions that appear on the top part of the screen help the user to a logical and quick orientation. Based on the financial data, the DSS performs a financial analysis whose results are shown for firm F23 in Figures 12–16.

## 4.2. Using the MINORA system

The MINORA system is used for the ranking of the firms from the most promising to the most risky and untrustworthy. Input data range from quantitative criteria (i.e. financial ratios originating from financial analysis) to qualitative ones coming directly from the data base. In this case study of MINORA that follows the user has selected a set of twenty reference firms from the initial sample of 39 firms and fifteen criteria on which he desires to base his decision.

Figure 17 shows in detail the input data to MINORA (i.e. multicriteria table, preordering of firms, evaluation scales,...).

The use of the UTA method provides two basic results: the criteria graphics (i.e. marginal utilities, Figure 18), and the ordinal regression curve (ranking versus global utility, Figure 19).

The restitution of the user's ranking by UTA seems to be good (Kendal's $\tau = 0.9$ , $F^{*} = 0.0.13$ ); however there are some inconsistencies. A certain number of firms such as F7, F33, F34,... appear as ill-ranked. For the analysis of these inconsistencies, MINORA submitted a series of questions about each ill-ranked firm. Let's give here an example about the ill-ranked firm F7 which is considered as underestimated by the user.

![](/api/attachments/E87UU8WP/fulltext/images/c1ab8738ec208431c262b8ca9b9f7cd4e041cdfab7ba262d5af8de58adedbc28.jpg)  
Fig. 12. Common-size statements (common-size ratios).

<table><tr><td colspan="6">&lt;Ctrl+&gt; &lt;PgUp&gt; &lt;PgDn&gt; &lt;↑&gt;&lt;↓&gt;&lt;(•)&lt;→Moving &lt;F1&gt; &lt;Esc&gt; &lt;F5&gt;&lt;F6&gt;Graphics &lt;F7&gt;</td></tr><tr><td colspan="6">Title: F23 28-09-1992</td></tr><tr><td>......PROFITABILITY RATIOS......</td><td>1985</td><td>1986</td><td>1987</td><td>1988</td><td>1989</td></tr><tr><td>(Sales-Cost of goods sold)/Sales</td><td>26.3</td><td>25.1</td><td>25.9</td><td>24.8</td><td>27.2</td></tr><tr><td>Net income / Sales</td><td>0.5</td><td>1.8</td><td>3.8</td><td>3.2</td><td>5.8</td></tr><tr><td>EBIT / Total assets</td><td>9.4</td><td>17.2</td><td>18.4</td><td>18.9</td><td>28.2</td></tr><tr><td>Net income / Net worth</td><td>2.1</td><td>18.2</td><td>13.7</td><td>13.5</td><td>16.9</td></tr><tr><td>(Sales(t)-Sales(t-1))/Sales(t-1)</td><td></td><td>6.6</td><td>-2.6</td><td>39.8</td><td>38.4</td></tr><tr><td>Net inc.t-Net inc.t-1/Net inc.t-1</td><td></td><td>265.7</td><td>59.9</td><td>49.8</td><td>149.2</td></tr><tr><td>Gross profit / Total assets</td><td>28.8</td><td>27.9</td><td>25.9</td><td>28.0</td><td>38.3</td></tr></table>

Fig. 13. Profitability ratios.

<table><tr><td colspan="6">&lt;Ctrl+&gt; &lt;PgUp&gt; &lt;PgDn&gt; &lt;↑&gt;(↓)&lt;(•)+Moving &lt;F1&gt; &lt;Esc&gt; &lt;F5&gt;&lt;F6&gt;Graphics &lt;F7&gt;</td></tr><tr><td colspan="6">Title: F23 28-09-1992</td></tr><tr><td>..MANAGERIAL PERFORMANCE RATIOS..</td><td>1985</td><td>1986</td><td>1987</td><td>1988</td><td>1989</td></tr><tr><td>General &amp; administr.expen./Sales</td><td>2.8</td><td>2.8</td><td>2.2</td><td>2.4</td><td>2.5</td></tr><tr><td>Selling expences / Sales</td><td>9.2</td><td>7.4</td><td>7.8</td><td>7.7</td><td>8.0</td></tr><tr><td>Interest expences / Sales</td><td>7.7</td><td>13.2</td><td>14.7</td><td>12.0</td><td>10.9</td></tr><tr><td>Gen.&amp; adm.+Sell.exp./Total assets</td><td>12.2</td><td>10.4</td><td>10.0</td><td>11.5</td><td>11.7</td></tr><tr><td>Cost of goods sold / Sales</td><td>73.7</td><td>74.9</td><td>74.1</td><td>75.2</td><td>72.8</td></tr><tr><td>Sales / Accounts receivable</td><td>3.3</td><td>2.7</td><td>2.9</td><td>3.0</td><td>2.0</td></tr><tr><td>Net worth / Total assets</td><td>27.4</td><td>20.0</td><td>22.0</td><td>27.0</td><td>38.3</td></tr><tr><td>Total liabilities/Working capital</td><td>295.9</td><td>212.7</td><td>203.5</td><td>231.4</td><td>152.0</td></tr></table>

Fig. 14. Managerial performance ratios.

<table><tr><td colspan="6">&lt;Ctrl-&gt;&gt; &lt;PgUp&gt; &lt;PgDn&gt; &lt;↑&gt;&lt;↓&gt;&lt;+&gt;&lt;-&gt;Moving &lt;F1&gt; &lt;Esc&gt; &lt;F5&gt;&lt;F6&gt;Graphics &lt;F7&gt;</td></tr><tr><td colspan="6">Title: F23 28-09-1992</td></tr><tr><td>......SOLUENCY RATIOS......</td><td>1985</td><td>1986</td><td>1987</td><td>1988</td><td>1989</td></tr><tr><td rowspan="2">Long term liab+Stockhold.eq./Net(Curr.assets-Invent.)/Curr.liab.</td><td>3.6</td><td>4.9</td><td>4.9</td><td>3.2</td><td>4.8</td></tr><tr><td>1.1</td><td>1.5</td><td>1.6</td><td>1.5</td><td>1.7</td></tr><tr><td>Total liabilities/Net worth</td><td>267.8</td><td>481.6</td><td>358.1</td><td>275.8</td><td>161.7</td></tr><tr><td>Total liabilities / Total assets</td><td>73.1</td><td>88.4</td><td>78.8</td><td>74.5</td><td>61.9</td></tr><tr><td>L.term liab/(L.term l.+Stockhold.</td><td>28.2</td><td>57.9</td><td>54.8</td><td>42.1</td><td>29.3</td></tr><tr><td>Current assets / Current liabilit</td><td>1.1</td><td>1.6</td><td>1.6</td><td>1.5</td><td>1.8</td></tr><tr><td>Total liabilities / Cash flow</td><td>14.5</td><td>18.5</td><td>15.2</td><td>18.8</td><td>6.3</td></tr><tr><td>Working capital / Total assets</td><td>24.7</td><td>37.8</td><td>38.7</td><td>32.2</td><td>48.7</td></tr><tr><td>Cash / Total assets</td><td>4.7</td><td>2.4</td><td>4.4</td><td>1.8</td><td>3.8</td></tr></table>

Fig. 15. Solvency ratios.

<Enter>Continue <F1>Help <F2> <End> <Esc>  
![](/api/attachments/E87UU8WP/fulltext/images/f8de927f9a50a4e8d6eebbda01a785ddcf96ef25d9e79d2d2b4440ce5d1be554.jpg)  
Fig. 16. Total liabilities to cash flow ratio evolution for firm F23.

![](/api/attachments/E87UU8WP/fulltext/images/4d9352df42250d8a3e935618c52a79d6dccbecfa2126abf8614e4cfbcabe2640.jpg)  
Interest expences √ Sales  
Fig. 17. A part of data input for MINORA.

<PgDn>Continue<FD>Instruct.><F2>Print<End>Exit<Eso>  
![](/api/attachments/E87UU8WP/fulltext/images/f63e14dfa5337b23ca19247f31dfb1158a35ac2276b4fac8b0da339c925f0e27.jpg)  
Fig. 18. Marginal utility of the criterion succession scheme for management.

3.96414  
![](/api/attachments/E87UU8WP/fulltext/images/b84f6d6027c3e6fc7a7ec9476fbdda9c5be6572b0b956664d116585dc1d8ff91.jpg)  
Fig. 19. Firm ranking versus global utility.

<PyDn>Continue<F1><Instruct.><F2>Print<End>Exit<Esc>  
![](/api/attachments/E87UU8WP/fulltext/images/620d01e282112c2f55403e051f9db2a409dbcc5e9d42e20e040efc17271c20fe.jpg)  
Fig. 20. Pairwise comparison of firms on the evaluation criteria.

<1><↓><->Moving <F5><F6><F7>Graphics <F1><F8><Instruct,><Esc><END>

<table><tr><td></td><td>R/U</td><td>R/M</td><td>(Sales -</td><td>M.U.</td><td>EBIT / T</td><td>M.U.</td><td>Interest</td><td>M.U.</td><td>G.U.</td></tr><tr><td>88-F6</td><td>1</td><td>1</td><td>30.7109</td><td>0.003</td><td>16.4315</td><td>0.064</td><td>-7.58755</td><td>0.064</td><td>0.003</td></tr><tr><td>88-F25</td><td>1</td><td>1</td><td>28.9497</td><td>0.003</td><td>35.8143</td><td>0.064</td><td>-2.06308</td><td>0.064</td><td>0.003</td></tr><tr><td>88-F31</td><td>1</td><td>1</td><td>39.8632</td><td>0.003</td><td>28.6139</td><td>0.064</td><td>-3.64879</td><td>0.064</td><td>0.003</td></tr><tr><td>88-F13</td><td>1</td><td>1</td><td>44.5948</td><td>0.003</td><td>11.5213</td><td>0.064</td><td>-4.19464</td><td>0.064</td><td>0.003</td></tr><tr><td>88-F1</td><td>5</td><td>5</td><td>45.5835</td><td>0.003</td><td>11.6597</td><td>0.064</td><td>-12.1830</td><td>0.064</td><td>0.670</td></tr><tr><td>88-F22</td><td>5</td><td>5</td><td>29.7501</td><td>0.003</td><td>25.7219</td><td>0.064</td><td>-4.55107</td><td>0.064</td><td>0.670</td></tr><tr><td>88-F2</td><td>5</td><td>5</td><td>24.8941</td><td>0.003</td><td>8.67828</td><td>0.064</td><td>-4.58951</td><td>0.064</td><td>0.670</td></tr><tr><td>88-F11</td><td>5</td><td>5</td><td>45.2438</td><td>0.003</td><td>29.7233</td><td>0.064</td><td>-2.18398</td><td>0.064</td><td>0.670</td></tr><tr><td>88-F5</td><td>5</td><td>5</td><td>24.7022</td><td>0.003</td><td>18.3812</td><td>0.064</td><td>-2.82148</td><td>0.064</td><td>0.670</td></tr><tr><td>88-F35</td><td>5</td><td>5</td><td>31.8177</td><td>0.003</td><td>21.1721</td><td>0.064</td><td>-3.57425</td><td>0.064</td><td>0.670</td></tr><tr><td>88-F7</td><td>11</td><td>5</td><td>29.4452</td><td>0.003</td><td>24.4823</td><td>0.064</td><td>-3.26154</td><td>0.064</td><td>0.670</td></tr><tr><td>88-F9</td><td>11</td><td>13</td><td>24.8778</td><td>0.003</td><td>13.1564</td><td>0.064</td><td>-6.43413</td><td>0.064</td><td>0.666</td></tr><tr><td>88-F33</td><td>11</td><td>12</td><td>22.5736</td><td>0.003</td><td>16.8835</td><td>0.064</td><td>-5.56226</td><td>0.064</td><td>0.669</td></tr><tr><td>88-F23</td><td>11</td><td>13</td><td>24.8155</td><td>0.003</td><td>18.9121</td><td>0.064</td><td>-11.9548</td><td>0.064</td><td>0.666</td></tr><tr><td>88-F38</td><td>11</td><td>13</td><td>42.3955</td><td>0.003</td><td>16.6562</td><td>0.064</td><td>-11.8682</td><td>0.064</td><td>0.666</td></tr><tr><td>88-F34</td><td>16</td><td>13</td><td>38.8792</td><td>0.003</td><td>29.6048</td><td>0.064</td><td>-5.17908</td><td>0.064</td><td>0.666</td></tr><tr><td>88-F39</td><td>16</td><td>17</td><td>18.5809</td><td>0.002</td><td>14.6126</td><td>0.064</td><td>-6.68914</td><td>0.064</td><td>0.661</td></tr><tr><td colspan="10">Trade off analysis.With the middle solution</td></tr></table>

Fig. 21. Trade off analysis.

<table><tr><td colspan="12">The Global Utility of all the possible Alternative Solutions</td></tr><tr><td>Ran.</td><td>Name</td><td>Util</td><td>Ran.</td><td>Name</td><td>Util</td><td>Ran.</td><td>Name</td><td>Util</td><td>Ran.</td><td>Name</td><td>Util</td></tr><tr><td>1</td><td>88-F6</td><td>.803</td><td>4</td><td>88-F2</td><td>.670</td><td>16</td><td>88-F24</td><td>.598</td><td></td><td></td><td></td></tr><tr><td>1</td><td>88-F25</td><td>.803</td><td>5</td><td>88-F26</td><td>.669</td><td>17</td><td>88-F37</td><td>.401</td><td></td><td></td><td></td></tr><tr><td>1</td><td>88-F31</td><td>.803</td><td>6</td><td>88-F33</td><td>.669</td><td>18</td><td>88-F36</td><td>.305</td><td></td><td></td><td></td></tr><tr><td>1</td><td>88-F13</td><td>.803</td><td>7</td><td>88-F23</td><td>.666</td><td>18</td><td>88-F18</td><td>.305</td><td></td><td></td><td></td></tr><tr><td>1</td><td>88-F29</td><td>.803</td><td>7</td><td>88-F32</td><td>.666</td><td>19</td><td>88-F16</td><td>.290</td><td></td><td></td><td></td></tr><tr><td>2</td><td>88-F12</td><td>.802</td><td>7</td><td>88-F17</td><td>.666</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>88-F10</td><td>.670</td><td>7</td><td>88-F34</td><td>.666</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>88-F22</td><td>.670</td><td>7</td><td>88-F3</td><td>.666</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>88-F5</td><td>.670</td><td>7</td><td>88-F30</td><td>.666</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>88-F11</td><td>.670</td><td>8</td><td>88-F9</td><td>.666</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>88-F7</td><td>.670</td><td>9</td><td>88-F8</td><td>.666</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>88-F15</td><td>.670</td><td>10</td><td>88-F39</td><td>.661</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>88-F20</td><td>.670</td><td>11</td><td>88-F20</td><td>.660</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>88-F14</td><td>.670</td><td>12</td><td>88-F21</td><td>.660</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>88-F1</td><td>.670</td><td>13</td><td>88-F27</td><td>.659</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>88-F4</td><td>.670</td><td>14</td><td>88-F30</td><td>.630</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>88-F35</td><td>.670</td><td>15</td><td>88-F19</td><td>.598</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 22. Final ranking of firms.

The system proposes to compare firm F7 to the firms belonging to the same equivalent class: F9, F33, F23 and F30. Figure 20 shows the graphical pairwise comparison between the firm F7 and the firm F23, which is correctly ranked. The comparison shows that firm F7 is clearly better than the rest of its equivalent class and consequently the user must upgrade.

The user can also correct some inconsistencies by modifying the marginal utilities.

In Figure 21, the system prompts the decision maker to subtract the amount of 0.064 from the marginal utility of the criterion EBIT/Total Assets where F7 is superior to other firms of its equivalent class.

After the acceptance of the evaluation model the user may obtain the ranking of other firms of the portfolio of the ETEVA industrial development bank (extrapolation phase, Figure 22).

<Enter>Continue <F1>Hello <F2> <End> <Ero>  
![](/api/attachments/E87UU8WP/fulltext/images/62db1c0e88924bfd2a36e3461d503e73163c7f8cd6ea4803d0515cead1a2ddcc.jpg)  
Fig. 23. The Altman's corporate risk model.

<table><tr><td rowspan="4"></td><td colspan="2">Scattering Diagram</td></tr><tr><td>Number of rows : 39</td><td>Number of cols : 24</td></tr><tr><td colspan="2">Horizontal Axis : Axis 1Vertical Axis : Axis 2Cum. Percentage : 40.87%</td></tr><tr><td>FirmsVariables</td><td></td></tr></table>

Fig. 24. The scattering diagram of principal components analysis.

## 4.3. Using corporate risk models

The utilization of Altman's model (1968) who was the first to apply the technique of discriminant analysis to the failure classification problem is shown in Figure 23. Firm F23 scores, for the whole period of the study lower than the cut off score of Altman's model which means that this firm is considered as bankrupt (Figure 23).

Similarities between firms can be analysed by means of principal components analysis factorial diagrams (see Figure 24). Finally, the user can classify the firms in two classes (bankrupt firms and no bankrupt firms) using the discriminant analysis model of the DSS.

## 5. Conclusion

A DSS for financing firms by a Greek industrial development bank was developed in this paper. The system is a new supportive tool in the evaluation of a portfolio of firms and in the financing decision making. Specifically, the DSS allows to manage financial information as balance sheet and income statement as well as qualitative information. The models included are used to describe, discriminate and rank the firms. This triple analysis of firms is a major advantage over previous methodologies. An important characteristic of the proposed DSS for corporate assessment is its ability to show their competitiveness level, the viability and the financial performance of the firms. Finally, the DSS gives important information on the criteria that the ETEVA bank is using for evaluating firms and on their relative significance in the decision making process (i.e. marginal utility for every criterion). Apart from the supporting role in the corporate assessment process, the proposed DSS innovates in some other areas as well:

\- The complex problem of corporate risk assessment is structured.

\- The time and cost for the study of the firms' dossiers are minimized, since this is now computerized.

\- The competitiveness and effectiveness of the ETEVA industrial development bank are increased, through the learning of scientific methods and models by their personnel.

\- Since more reliable data is needed for a computerized system, this is sought after more keenly.

\- The financial art is upgraded by the use of even more sophisticated methods (multivariate statistical data methods, MCDM methods).

\- The computerized system offers transparency in the selection of the firms to be financed, since every decision can be argued on solid scientific grounds.

The field of applications of the system is very broad. It can be used for the appreciation of industrial clients of banks, industrial clients of insurance companies, clients of venture capital firms or of firms of particular industrial sectors (motor car industry, agriculture, chemistry, electrical equipment and appliance industries, hardware industries, distribution, etc.).

## References

Alter, S.L., Decision support systems: Current practice and continuing challenges (1982) (Addison Wesley, Reading, Mass).

Altman, E.I., Financial ratios, discriminant analysis and the prevision of corporate bankruptcy (1968), The Journal of Finance 23, 589–609.

Altman, E.I., Corporate financial distress (1983) (John Wiley and Sons, New York).

Altman, E.I., Introduction: Company and country risk models (1984), Journal of Banking and Finance 8, no 2, 171–198.

Altman, E.I., M. Margaine, M. Schlosser and P. Vernimmen, Statistical credit analysis in the textile industry: A French experience (1974), Journal of Financial and Quantitative Analysis 9, no 2, 195–211.

Altman, E.J. and M. Lavalee, Business failure classification in Canada (1981), Journal of Business Administration, Summer, 147–164.

Altman, E.I., R.B. Avery, R.A. Eisenbeis and J.F. Sinkey Jr., Application of classification techniques in business, banking and finance (1981) (JAI Press Inc., Greenwich).

Banque de France, L' analyse des défaillances d'entreprises (1983), Rapport présenté à la IXème Journée d'Etude des Centrales de Bilan, Paris.

Bonczek, R., C. Holsapple and A. Whinston, Foundation of Decision Support Systems (1981) (Academic Press, London).

Bouwman, M.J., Human diagnostic reasoning by computer: An illustration from financial analysis (1983), Management Science 29, no 6, 653–672.

Brans, J.P. and B. Maréchal, The PROMETHEE methods for MCDM; The PROMCALC, GAIA and BANKADVISER software, in C.A. Bana e Costa (ed.) (1990) (Springer-Verlag, Berlin Heidelberg), 216–252.

Chevalier, A. and R. Hirsch, Le Risk Management (1982) (Entreprise Moderne d'Edition, Paris).

CNME, Méthode de décision multicritère appliquée à l'évaluation de l'entreprise (1973), 58,1-27.

Cosset, J.C., Y. Siskos and C. Zopounidis, Evaluating country risk: A decision support approach (1992), Global Finance Journal, vol. 3, no 1, 79–95.

Courtis, J.K., Modelling a financial ratios categoric framework (1978), Journal of Business Finance and Accounting, vol. 5, no 4, 371–386.

Duchessi, P. and S. Belardo, Lending analysis support system (LASS): An application of a knowledge-based system to support commercial loan analysis (1987), IEEE Transactions on Systems, Man, and Cybernetics, vol. SMC-17, no 4, 608–616.

Dutta, S. and S. Shekhar, Generalization with neural networks: An application in the financial domain (1992), Journal of Information Science and Technology, vol. 1, no 4, 309–330.

Eisenbeis, R., Pitfalls in the application of discriminant analysis in business, finance and economics (1977), The Journal of Finance 32, no 3, 723–739.

Jacquet-Lagrèze, E. and J. Siskos, Assessing a set of additive utility functions for multicriteria decision making: The UTA method (1982), European Journal of Operational Research 10, 151–164.

Klein, M. and L.B. Methlie, Expert systems: A decision support approach with applications in management and finance (1990) (Addison-Wesley, Reading, Mass).

Lee, C.F., Financial analysis and planning: Theory and applications (1985) (Addison-Wesley, Reading, Mass).

Roy, B., Méthodologie multicritère d'aide à la décision (1985) (Economica, Paris).

Shaw, M.J. and J.A. Gentry, Using an expert system with inductive learning to evaluate business loans (1988), Financial Management, Autumn, 45–56.

Siskos, J., Evaluating a system of furniture retail outlet using an interactive ordinal regression method (1986), European Journal of Operational Research 23, 179–193.

Siskos, J. and C. Zopounidis, The evaluation criteria of the venture capital investment activity: An interactive assessment (1987), European Journal of Operational Research 31, 304–313.

Sprague, R.H., Jr. and H.J. Watson, A decision support system for banks (1976), OMEGA, vol. 4, no 6, 657–671.

Srinivasan, V. and Y.H. Kim, Designing expert financial systems: A case study of corporate credit management (1988), Financial Management, Autumn, 32–44.

Srinivasan, V. and B. Ruparel, CGX: An expert support system for credit granting (1990), European Journal of Operational Research 45, 293–308.

Tam K.Y. and M.Y. Kiang, Managerial applications of neural networks: The case of bank failure predictions (1992), Management Science, vol. 38, no 7, 926–947.

Zeleny, M., Multiple criteria decision making (1982) (McGraw-Hill, New York).

Zollinger, M., L'analyse multicritère et le risque de crédit aux entreprises (1982), Revue Française de Gestion, 56–66.

Zopounidis, C., A multicriteria decision-making methodology for the evaluation of the risk of failure and an application (1987), Foundations of Control Engineering, vol. 12, no 1, 45–67.
