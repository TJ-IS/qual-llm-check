---
otero_id: 21981
otero_key: "FMP76M4M"
title: "Business data mining — a machine learning perspective"
authors: "Indranil Bose; Radha K. Mahapatra"
year: "2001"
journal: "Information & Management"
doi: "10.1016/s0378-7206(01)00091-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Business data mining — a machine learning perspective

Indranil Bose $^{a,1}$ , Radha K. Mahapatra $^{b,*}$

$^{a}$ Department of Decision and Information Sciences, Warrington College of Business Administration,

University of Florida, 351 Stuzin Hall, P.O. Box 117169, Gainesville, FL 32611, USA

$^{b}$ Department of Information Systems and Management Sciences, College of Business Administration, University of Texas at Arlington, P.O. Box 19437, Arlington, TX 76019-0437, USA

Received 29 November 1999; received in revised form 5 February 2001; accepted 12 February 2001

## Abstract

The objective of this paper is to inform the information systems (IS) manager and business analyst about the role of machine learning techniques in business data mining. Data mining is a fast growing application area in business. Machine learning techniques are used for data analysis and pattern discovery and thus can play a key role in the development of data mining applications. Understanding the strengths and weaknesses of these techniques in the context of business is useful in selecting an appropriate method for a specific application. The paper, therefore, provides an overview of machine learning techniques and discusses their strengths and weaknesses in the context of mining business data. A survey of data mining applications in business is provided to investigate the use of learning techniques. Rule induction (RI) was found to be most popular, followed by neural networks (NNs) and case-based reasoning (CBR). Most applications were found in financial areas, where prediction of the future was a dominant task category. © 2001 Elsevier Science B.V. All rights reserved.

Keywords: Business applications; Data mining; Machine learning

## 1. Introduction

Data mining, also known as “knowledge discovery in databases” [23], is the process of discovering interesting patterns in databases that are useful in decision making. Data mining is a discipline of growing interest and importance, and an application area that can provide significant competitive advantage to an organization by exploiting the potential of large data warehouses.

The task of finding patterns in business data is not new. Traditionally, it was the responsibility of business analysts, who generally use statistical techniques. The scope of this activity, however, has recently changed. Widespread use of computers and networking technologies has created large electronic databases that store business transactions. Retailers, like Wal-Mart Stores, capture millions of sales transactions through their point-of-sale terminals. Transactions can be analyzed to identify buying patterns of individual customers as well as customer groups, and sales patterns of different stores.

Intense competition is forcing companies to identify innovative ways to capture and enhance market shares while reducing cost. A better appreciation of the buying behavior of customers can enhance the effectiveness of target marketing practices. Data warehousing technology has enabled companies to organize and store large volumes of business data in a form that can be analyzed and a maturing of the “artificial intelligence” field has created a set of techniques of “machine learning” that are useful in automating tedious but crucial activities of discovering patterns in databases. These factors have changed the way that business data are analyzed and given rise to data mining, which integrates machine learning, statistical analysis and visualization techniques, with the intuition and knowledge of the business analyst, to discover meaningful and interesting patterns in business data.

Data mining is a complex process involving multiple iterative steps. Fig. 1 gives an overview of this process. The first step is the selection of data for analysis. Normally, historical data is used. The data set may be retrieved from a single source, such as a data warehouse, or may be extracted from several operational databases. The selected data set then undergoes cleaning and preprocessing. Lack of consistency across databases creates serious problem when data is extracted from multiple databases. The cleaning operation removes discrepancies and inconsistencies. Some mining techniques require data to be preprocessed to improve its quality. Examples include transformation of data from one scale to another, identification of predictive attributes in the data set, and reduction of the dimension of the data set through recomposition.

![](/api/attachments/FMP76M4M/fulltext/images/3adb8e80d21cd5a38dd8700fe60228768fb7675ff580f867e31430a0c18b7960.jpg)  
Fig. 1. An overview of the data mining process (adapted from Fig. 1 in [23]).

The data set is analyzed next to identify patterns, i.e. models that represent relationships among data. The model is then validated with new data sets to ensure its generalizability. It should be possible to translate the model into actionable business plans that are likely to help the organization achieve its goals. A model or pattern that satisfies these conditions becomes business knowledge. The steps in the mining process are performed iteratively until meaningful business knowledge is extracted.

A number of algorithms have been developed in domains, such as machine learning, statistics, and visualization, to identify patterns in data. Of these, statistical modeling approaches are the oldest. The data set must conform to rigid distribution criteria to employ statistical modeling methods. Pattern discovery algorithms based on machine learning techniques, however, impose fewer restrictions and produce patterns that are easy to understand. They are, therefore, finding wide popularity in data mining applications. Each technique has its own strengths and weaknesses. Understanding these in the context of business data mining is very useful in selecting an appropriate technique for a specific application. The objective of this paper is to inform the information systems (IS) manager and the business analyst about the role of machine learning techniques in business data mining.

## 2. An overview of machine learning techniques

Machine learning is the study of computational methods to automate the process of knowledge acquisition from examples $[34]$ . This discipline evolved to eliminate the laborious and expensive knowledge engineering process involved in developing knowledge-based systems. A common strategy used is to discover a pattern in a training data set. This pattern is then used to classify and/or predict the behavior of new examples. Major categories of machine learning techniques are

\- rule induction,

\- neural networks,

\- case-based reasoning,

• genetic algorithms, and

\- inductive logic programming,

Rule induction (RI) creates a decision tree or a set of decision rules from training examples with a known classification $[5]$ . The root node of a decision tree represents all examples in the training set. If these examples belong to two or more classes, then the most discriminating attribute is selected and the set is split into multiple classes. This process of attribute selection and splitting is continued until each terminal node represents a different class of examples. The resulting decision tree is then applied to a test data set to evaluate its accuracy in classifying new examples. When a decision tree is overfitted to a training data set, its classification accuracy with new data may diminish. The tree must then be pruned to eliminate overfitting before it is deployed in a real life application. Consider, for example, a bank trying to model delinquency in loan repayment. The training data set for such a problem would include records of customers previously granted loans. Each customer record is labeled as delinquent or not, based on the customer's repayment behavior. Fig. 2 shows a hypothetical decision tree for this problem. The data set is split into two groups based on the credit rating attribute. Those with poor credit rating are found to belong to the delinquent category. The customers with good credit rating constitute a mixed group. This latter group is further divided into three sub groups based on the indebtedness attribute. This process of attribute selection and splitting continues until each leaf node holds a single class of customers. The resultant tree can be used to classify new customers. C4.5 [42] is a popular algorithm for creating decision trees.

A decision tree may be translated into a set of rules. The classification rules are normally stated in disjunctive normal form. It is also possible to derive rules directly from a training data set. The model developed by RI is very attractive because it is easy to understand. A limitation of a decision tree-based model is that it creates only mutually exclusive classes; a RI algorithm can overcome this by creating rules for overlapping classes.

![](/api/attachments/FMP76M4M/fulltext/images/c7c54500d2b80c8deb667528f905bf39b6e4f457dfb83ae5373fd990ce319738.jpg)  
Fig. 2. A decision tree.

A typical neural network (NN) consists of a set of input nodes that are connected to a set of output nodes through a set of hidden nodes, thus forming a multilayered network $[45]$ . Each node is associated with a bias value and an output function. The NN receives input signals through input connections, computes an output, and transmits it to other nodes. Each connection has an associated weight that modifies the incoming signal before it is passed on to the node attached to that connection. Thus, the input signal to a node is the weighted sum of all the signals reaching it through its input connections. A sigmoidal function is often used as the output function. An NN is trained by using examples of known classification. The network learns the classification function by iteratively adjusting the weights associated with the network connections. The trained network is pruned to reduce the effect of overfitting. The strength of an NN is that it can learn any classification function. Training a network, however, is time consuming requiring several passes through the training set. The classification function in an NN is buried within the network topology and the connection weights. Thus, the classification logic is not obvious to the end-user. Researchers are developing strategies to extract symbolic rules from NNs $[18,51]$ .

The case-based reasoning (CBR) approach stores examples in a case-base and uses them in the machine learning task $[31]$ . A case stores a problem description and its solution, which could be a process description or a classification. Given a new problem, a CBR system tries to find a matching case. A nearest neighbor matching algorithm is often used for this purpose. The matching case provides a solution. Domain knowledge is captured in the indexing scheme and the concept hierarchies associated with the case-base. The advantage of using a CBR approach is that domain knowledge is easily used to enhance the effectiveness of the system; the system is also very robust. Its performance degrades gracefully with noisy or missing data, but maintenance of a large case-base can be difficult due to a lack of tool support.

Genetic algorithms (GAs) are a family of search procedures based on the theory of natural selection and evolution $[26]$ . They have been used in classification and prediction tasks. The three basic operations in a GA are selection, crossover, and mutation. The selection operator takes the items from a population, based on certain fitness criteria. The better items have a higher probability of being selected, due to their higher value of fitness. The selected items form the mating pool. The crossover operator swaps a part of an item with the corresponding part of another in the mating pool to create new items that are added to the population. The search for some optima proceeds through successive applications of the selection and crossover operators. The mutation operator randomly changes a part of an item to create a new one. Mutation thus adds diversity to the population and is used sparingly.

GAs work well with noisy data. Since they use very little domain knowledge, they can be easily connected to other systems and other machine learning approaches to create hybrid systems. However, translating the data mining problem into a model that can be represented by a GA usually takes some effort. This is so because the available data may need to go through transformations so that it will be meaningful to perform GA operations like reproduction, crossover, and mutation on it. This needs some additional work on behalf of the data miner.

Inductive logic programming (ILP) uses first order predicate logic to define a concept by using a set of positive and negative examples $[8]$ . This logic program is then used to classify new examples. Predicate logic, which is used as the modeling language in ILP systems, provides a powerful mechanism for concept description and endows ILP with two advantages over attribute-based learning techniques. First, complex relationships among components can be easily expressed, thus improving the expressive power of the model. Second, domain knowledge can be easily represented in an ILP system. This improves the effectiveness of the system. The model expressed in predicate logic is also easy to understand. ILP systems tend to have low predictive accuracy with new examples and are very sensitive to noise. Their performance deteriorates rapidly in the presence of spurious data.

## 3. A characterization of machine learning techniques for mining business data

Data mining applications in business have certain characteristics that affect the performance of machine learning techniques. Understanding these characteristics and their impacts on machine learning is useful in selecting an appropriate technique for an application.

They are distinguished as data characteristics and operational characteristics.

Business databases often contain noise in the form of inaccuracies and inconsistencies. Inadequate data validation procedures may allow the user to enter incorrect data. It can also become corrupt during migration from one system to another. Missing data is another common problem in business databases, especially when data is collected from many different sources. All attributes required for analysis may not be available because of differences in data coding standards and aggregation strategies in different parts of the organization. For example, customer data in one division may include age and education level, whereas another may not have this information available in its database. This often happens due to uncoordinated database design efforts. In business data mining, the data sets may range in size from several gigabytes to a few terabytes. These data sets are also characterized by a large number of features or attributes. Scalability of the data mining technique, therefore, becomes an important issue. Business databases contain data of various types: numeric, ordinal, and nominal etc. If a machine learning technique can handle different data types, it will be more useful for business data mining.

The predictive accuracy of a data mining technique strongly influences its effectiveness. Machine learning systems that follow a supervised learning process are first trained. However, the predictive accuracy of the system with real data is often lower than that achieved with the training data. Higher predictive accuracy with actual data is an obviously desirable feature. A business manager, on the other hand, is more likely to accept the recommendations if the results are explainable in business terms. The ability to explain the results, therefore, is an important factor. Business applications rarely operate as standalone systems. A data mining application, therefore, is likely to be integrated with other DSS or DBMS in the organization. Ease of integration with other IS is, therefore, a desirable characteristic of a data mining application. Different machine learning techniques require varying levels of tool-related expertise and knowledge on the part of the end-user before he/she can effectively use a specific technique. Some techniques also mandate extensive preprocessing activities for preparing the data set before analysis. A technique that is easy to understand and that requires fewer preprocessing activities is more useful to an end user.

The behaviors of machine learning techniques vary with variations in data and operational characteristics of data mining applications. Table 1 provides a comparison of machine learning techniques with respect to data and operational characteristics.

## 4. Data mining applications in business

Data mining applications were identified by reviewing a large number of IS and computer science journals and conference proceedings related to data mining. These journals and conference proceedings are listed in Appendix A. We first identified those articles that used the term data mining either in the title of the article or in the list of keywords. From among these we selected those related to business applications. While we used the Web as a resource, due to its reference unreliability, we did not include any application that was not published in a journal or the proceedings of a conference.

Table 1  
Characteristics of machine learning techniques

<table><tr><td></td><td>RI</td><td>NN</td><td>CBR</td><td>GA</td><td>ILP</td></tr><tr><td>Ability to handle noisy data</td><td>Good</td><td>Very good</td><td>Good</td><td>Very good</td><td>Poor</td></tr><tr><td>Ability to handle missing data</td><td>Good</td><td>Good</td><td>Very good</td><td>Good</td><td>Poor</td></tr><tr><td>Process large data sets</td><td>Very good</td><td>Poor</td><td>Good</td><td>Good</td><td>Poor</td></tr><tr><td>Process different data types</td><td>Good</td><td>Requires transformation to numeric type</td><td>Very good</td><td>Requires data transformation</td><td>Difficulty in handling numeric data</td></tr><tr><td>Predictive accuracy</td><td>High</td><td>Very high</td><td>High</td><td>High</td><td>Domain dependent</td></tr><tr><td>Explanation capability</td><td>Very good</td><td>Poor</td><td>Very good</td><td>Good</td><td>Very good</td></tr><tr><td>Ease of integration</td><td>Good</td><td>Good</td><td>Good</td><td>Very good</td><td>Very good</td></tr><tr><td>Ease of operation</td><td>Easy</td><td>Difficult</td><td>Easy</td><td>Difficult</td><td>Difficult</td></tr></table>

Table 2 lists these applications by functional area and identifies the techniques used and the type of data mining problem addressed. This is, however, not meant to be exhaustive. Some of the applications in our survey address more than one problem category. We categorized such applications by their dominant categories, depending on the problem context. Data mining applications included in our survey addressed the following problem types: classification, prediction, association, and detection.

Table 2  
List of Data mining applications

<table><tr><td>Area</td><td>Application</td><td>Technique(s) used</td><td>Problem type</td></tr><tr><td rowspan="14">Finance</td><td>Forecasting bankruptcies [62,57]</td><td>NN [62]; RI [57]</td><td>Prediction</td></tr><tr><td>Forecasting defaulting loans [40]</td><td>RI [40]</td><td>Prediction</td></tr><tr><td>Forecasting stock price [6]</td><td>NN [6]</td><td>Prediction</td></tr><tr><td>Credit assessment [14]</td><td>RI [14]</td><td>Prediction</td></tr><tr><td>Portfolio management [27]</td><td>RI [27]</td><td>Prediction</td></tr><tr><td>Forecasting interest rates [29]</td><td>NN and CBR [29]</td><td>Prediction</td></tr><tr><td>Forecasting price of index futures [58]</td><td>RI and NN [58]</td><td>Prediction</td></tr><tr><td>Corporate bond rating [13]</td><td>CBR and RI [13]</td><td>Prediction</td></tr><tr><td>Loan approval [7]</td><td>RI and visualization [7]</td><td>Prediction</td></tr><tr><td>Risk classification [52]</td><td>RI [52]</td><td>Classification</td></tr><tr><td>Financial customer classification [43]</td><td>RI [43]</td><td>Classification</td></tr><tr><td>Detecting delinquent bank loans [28]</td><td>NN and visualization [28]</td><td>Detection</td></tr><tr><td>Identifying suspicious transactions [12,30,50]</td><td>NN [12]; RI [30,50]</td><td>Detection</td></tr><tr><td>Risk management [25]</td><td>Visualization [25]</td><td>Detection</td></tr><tr><td rowspan="4">Telecom</td><td>Forecasting network behavior [38,46]</td><td>RI [38]; NN and RI [46];</td><td>Prediction</td></tr><tr><td>Call tracking [1]</td><td>CBR [1]</td><td>Classification</td></tr><tr><td>Churn management [9]</td><td>RI [9]</td><td>Classification</td></tr><tr><td>Fraud detection [12,47,53]</td><td>RI [12]; Visualization [47,53]</td><td>Detection</td></tr><tr><td rowspan="8">Marketing</td><td>Market segmentation [53]</td><td>RI [53]</td><td>Classification</td></tr><tr><td>Lifestyle behavior analysis [36]</td><td>Visualization and RI [36]</td><td>Classification</td></tr><tr><td>Online sales support [61]</td><td>CBR [61]</td><td>Classification</td></tr><tr><td>New opportunity analysis [48]</td><td>Visualization [48]</td><td>Prediction</td></tr><tr><td>Customer reaction to promotions [11,49]</td><td>GA [11]; RI and visualization [49]</td><td>Prediction</td></tr><tr><td>Improvement of cross sales [2]</td><td>RI [2]</td><td>Association</td></tr><tr><td>Product performance analysis [3,4,25]</td><td>RI [3,4]; Visualization [25]</td><td>Association</td></tr><tr><td>Market basket analysis [7,12]</td><td>Visualization [7,12]</td><td>Association</td></tr><tr><td rowspan="5">Web analysis</td><td>Similarity assessment of user browsing patterns [16,17,63]</td><td>RI [16]; RI and visualization [17];Rule-based heuristics [63]</td><td>Classificationand association</td></tr><tr><td>Identification of Web pages that are viewed together [63]</td><td>Rule-based heuristics [63]</td><td>Association</td></tr><tr><td>Similarity assessment of Web page contents [19,56]</td><td>ILP [19]; rule-based heuristics [56]</td><td>Association</td></tr><tr><td>Categorization of Web pages based on content [15,60]</td><td>Rule-based heuristics [15]; RI [60]</td><td>Classification</td></tr><tr><td>Searching for specific Web pages [44]</td><td>Visualization [44]</td><td>Detection</td></tr><tr><td rowspan="12">Others</td><td>Litigation assessment [21,47]</td><td>RI [21]; NN and RI [47]</td><td>Prediction</td></tr><tr><td>Political conflict resolution [24]</td><td>CBR and RI [24]</td><td>Prediction</td></tr><tr><td>Insurance claim estimation [20]</td><td>CBR and statistics [20]</td><td>Prediction</td></tr><tr><td>Detecting insurance claims fraud [37]</td><td>RI and statistics [37]</td><td>Detection</td></tr><tr><td>Exception reporting in healthcare [39]</td><td>RI [39]</td><td>Detection</td></tr><tr><td>Software cost estimation [35]</td><td>NN [35]</td><td>Detection</td></tr><tr><td>Customer technical support [33,54]</td><td>RI and CBR [33]; CBR [54]</td><td>Classification</td></tr><tr><td>Hypothesis formulation about illness [10]</td><td>GA [10]</td><td>Classification</td></tr><tr><td>Mapping patient symptoms to surgical procedures [55]</td><td>RI and NN [55]</td><td>Classification</td></tr><tr><td>Scheduling [32,59]</td><td>GA [32,59]</td><td>Classification</td></tr><tr><td>Expenditure of allocated budget [41]</td><td>GA [41]</td><td>Classification</td></tr><tr><td>Software quality control [1]</td><td>CBR [1]</td><td>Classification</td></tr></table>

Classification: A training data set is used to identify the maximally distinguishing attributes associated with classes or clusters of data. Once the classes are identified, new examples can be analyzed and appropriately categorized. Examples of classification tasks include categorizing the risk-return characteristics of stocks, bonds and mutual funds, and determining the creditworthiness of a credit application.

Prediction: This involves finding possible future values and/or distributions of attributes of interest based on the observed data. A key task is identification of attributes that most strongly influence the attributes being predicted. Example problems in this domain include forecasting faults in telecommunication networks and predicting market performance of products.

Association: This identifies rules that govern the relationships among groups of attributes and/or entities. A good example is market basket analysis, which involves identifying a group of products that tend to sell together. Associating symptoms with diseases is another example.

Detection: This includes determination of anomalous behavior, outliers, counter intuitive data values, and irregular patterns in data sets, and seeks to explain the cause of such irregularities. Churn management, which involves identifying profiles of customers that are likely to switch their telecom carriers, is an example of this.

## 4.1. Data mining applications in finance

Predicting the future is a dominant problem category in finance and banking. Wilson and Sharda [62] demonstrate the superiority of NNs over discriminant analysis method in predicting bankruptcy of a firm. Their NN-based system achieved a prediction accuracy of $97\%$ . Another application in this area [57] showed that a RI-based model could achieve higher prediction accuracy than a multivariate discriminant analysis model in predicting bankruptcy under varied economic conditions.

Messier and Hansen [40] report the use of RI to predict defaulters of loans. Their study shows that a

RI-based model can achieve superior prediction accuracy than discriminant analysis. Barr and Mani [6] report the use of NNs and RI to forecast the price of the S&P 500 Index. The NN was trained using time series data with 21 indicator variables as input and achieved a prediction accuracy of 0.92 for the change in the movement of the index. Carter and Catlett [14] describe the use of RI to assess the reliability of credit card applicants. Using a data set containing both continuous and discrete valued attributes their study showed that RI is superior to discriminant analysis and rule-based expert systems in this application. REDON [27] ranks stocks based on their risk and return performance and allows the user to create portfolios of stocks based on his/her risk tolerance level.

Some data mining applications employ more than one machine learning technique. Kim and Noh [29] report an integrated system that combines CBR with NN to forecast interest rates for corporate bonds and treasury bills. Their integrated model outperformed a random walk model in predicting US interest rates, but was not so successful in predicting Korean interest rates. Another such hybrid system uses CBR with RI to rate corporate bonds [13]. It provides superior judgment about bond rating situations by complementing knowledge gathered from rules on how to rate bonds with similarity metrics obtained from past bond rating situations. This system matched the S&P recommended ratings 90.4% of the time for companies with complete data and 84.4% of the time for companies with incomplete data. A hybrid RI–NN approach is presented in [58] for predicting the direction of the daily price changes in the S&P 500 stock index futures. The RI subsystem selects key indicator variables that are then used to train the NN subsystem, which makes recommendations on the direction of the price change.

Data visualization has been used in some data mining applications in the field of finance. MineSet [7] uses supervised and unsupervised learning for loan approval, churn management in banking, and detection of credit card frauds. It allows creation of visual decision trees for obtaining business rules. Gershon and Eick [25] discusses visualization-based data mining applications in fixed income and derivative risk management, what-if analysis for decision support, and credit application evaluation. Shaw and Gentry [52] use inductive learning for risk classification in loan evaluation and bond rating. The goal of this system is to make generalizations about outcomes in each task using a large set of variables. It demonstrates the superior performance of RI over probit and logit analysis, and discriminant analysis.

GUHA, KEX, and KnowledgeSeeker identify classes of accounts with interesting behavior patterns, such as periodically changing small credit and debit balances, from financial transaction databases $[43]$ . Intelligent miner combines the predictive features of NN with visualization, to detect delinquent bank loans $[28]$ . It uses attributes such as loan-to-value ratio, origination amount, period and type of loan, etc., to predict whether a mortgage is likely to become delinquent. FALCON $[12]$ uses an NN-based approach to identify suspicious credit card transactions whereas Kokkinaki $[30]$ proposes the use of similarity trees for a similar application. FAIS $[50]$ detects large cash transactions that indicate potential for money laundering operations.

## 4.2. Data mining applications in telecommunications

Telecommunications offers an attractive domain for data mining because of the data intensive nature of applications in this domain. One class of applications involves finding trends and patterns in operational characteristics of networks to diagnose chronic faults. Sasisekharan and Seshadri [46] combines statistical methods and machine learning techniques to identify patterns of chronic problems in network operations, and uses these patterns to predict potential faults in telecom networks. Telecommunication alarm sequence analyzer [38] identifies frequently occurring alarm episodes and encodes their predictive characteristics as rules to predict likelihood of occurrence of such episodes.

Fraud detection is another important application area in telecommunications. Data visualization has been used to detect telephone fraud involving calls to bogus premium-rate services $[47,53]$ . British Telecom uses Netmap $[47]$ to track fraudulent calls and to identify calling patterns of those callers who make such calls. An interesting feature of Netmap is that it can categorize fraudulent call makers into a hierarchy of criminals ranging from petty abusers to ringleaders. Clonedetector $[12]$ uses customer profile data to detect cellular cloning fraud.

CBR has been used for the classification and routing of incoming telex messages $[1]$ . This system determines the most appropriate recipient of a telex message by comparing the characteristics of an incoming message with those of previously routed messages. Churn management, or prevention of frequent switching of telecommunication service providers by customers, is an important application area for telecommunication companies due to its impact on their market share and growth. Various demographic attributes, type of service in use, and call patterns have been used to induce classification rules to identify customers that are most likely to switch companies within a short time period $[9]$ .

## 4.3. Data mining applications in marketing

Data mining applications in marketing include retail sales analysis, market basket analysis, product performance analysis, and market segmentation analysis. British Telecom uses RI to distinguish between users and nonusers of telecommunication products $[53]$ . This information facilitates tailoring new services to closely meet customers' needs. Cross-sales, i.e. selling a product with enhanced features to current customers, can be improved by associating customer characteristics with product features. Anand et al. $[2]$ describe a RI-based methodology for identifying target customers for a new insurance product offered by a bank from among the account holders of that bank. IDEA $[49]$ analyzes the effect of new promotions on market behavior in the telecommunications industry. It provides interactive querying and drill-down capabilities on customer characteristics. Bhattacharya $[11]$ discusses the use of GA to classify customers that are most likely to respond to a marketing campaign. This study identifies mailing depth (i.e. percentage of customers to whom the advertisement needs to be sent) required to maximize return on advertisement under a budget constraint.

Data visualization has been used in conjunction with other machine learning techniques in marketing applications. WinViz [36] has been used to study transportation, food, shopping, and travel patterns for numerous households in Singapore. Visualization has also been used for analyzing the performance of consumer products and for identifying factors that affect this performance [25]. This system enables the user to interactively compare performances of different stores with the benchmark. Systems specializing in market basket analysis include Rules Visualizer of MineSet [7] and Nicheworks [12]. Both these tools use visualization to identify products that are frequently purchased together. Rules Visualizer found, for example, that grocery items like bread and dry-food condiments are usually sold together. Nicheworks discovered a strong relationship between purchase of discounted hardware items and plumbing items in hardware stores.

Spotlight [3] is an explanation-based mining system that is used for product performance analysis. It can indicate changes in a product's market share due to introduction of promotional programs and shifts among product segments. Opportunity Explorer [4], a later version of Spotlight, can be used by a sales representative to analyze his/her business with individual retailers. CoverStory [48] can process large volumes of marketing data to provide summarized information to managers on new opportunities, threats and deviations from trends. CBR is used for sales support in a novel application that involves on-line shopping [61]. This system computes similarity measures between the customer specified product and the company offered products, and provides the customer with a list of products with similar characteristics from its case-base.

## 4.4. Data mining applications in Web analysis

With the growing popularity of electronic commerce, the World Wide Web (WWW) has attracted the attention of data mining researchers. Discovering usage patterns on the WWW is an important application area in Web data mining $[22]$ . Data mining has been used to analyze log file data to understand access patterns of WWW users $[16]$ . This information is useful in improving access to Web sites. WEBMINER $[17]$ uses RI and visualization to discover association rules, classification rules, clusters, and sequential access patterns from site access data using an SQL-like query mechanism. Speedtracer $[63]$ analyzes Web usage data to generate user-based, path-based, and group-based summary reports on duration of user sessions, distribution of pages visited by users, and most frequently visited pages and paths. Multiple data mining algorithms including sequential patterns, association rules, and clustering are used in $[60]$ for categorizing HTML pages and for discovering similarities in interests among WWW users. The goal is to provide suggestions about which cluster of pages to visit to new incoming users based on their choice of preferences.

A number of data mining applications focus on Web content mining. ParaSite [56] mines information contained implicitly in the links that relate documents on the WWW. This can be used in searching for Web pages when the locations of the desired pages are not known. Examples of such applications include locating individuals' homepages, new locations of moved pages as well as any unindexed information. On a similar vein, the CLEVER system [15] mines the WWW for authorities (pages that give the best information on a topic) and hubs (pages that provide collection of links to authorities), and returns more relevant pages than most search engines. A classification-based system like Quinlan's FOIL is used in [19] for learning definitions of page classes and relationships among pages. This system improves the search time and accuracy by using the knowledge of relationships among various page classes. Rohrer and Swing [44] discuss a visualization-based method for searching the Web. It uses a content-based clustering technique to generate topic spheres that hold documents with similar contents in close proximity. Users' queries are directed at these topic spheres and then refined through additional keywords to identify target documents.

## 4.5. Other data mining applications

This section describes data mining applications that did not fit any of the categories described above. The legal domain is a growing area for data mining applications. Dale and Bench-Capon [21] identifies several applications in this area including monitoring compliance with guidelines in sentencing criminals, explaining legal decisions through established legal theories, and obtaining rules from knowledge gathered from legal experts. Some of the challenges of developing data mining applications in this domain are handling ordinal as well as continuous valued attributes, identifying threshold values for partitioning continuous attributes, large number of values for attributes, huge data sets that are difficult to partition, and presence of noise in the form of outlying cases. NNs and RI have been used to develop models to predict the results of lawsuits $[47]$ . Companies can use the insight gained from such models to evaluate the cost effectiveness of settling a lawsuit versus pursuing it. The Internal Revenue Service uses a prototype system based on KnowledgeSeeker, ModelWare and AIM for identifying income tax frauds. Furnkranz et al. $[24]$ discuss the use of CBR and nearest neighbor techniques to predict the outcomes of international conflicts. IntelligenceWare (IDIS) is used for evaluating the quality of judgements delivered by judges and for identifying dominant biases of judges.

Applications of CBR are also found in customer technical support systems $[33,54]$ . When a problem is reported to the support center the CBR system identifies the most similar problem from the case-base and suggests the solution, with modifications if necessary, to the user. Kriegsman and Barletta $[33]$ describe a customer support system that uses CBR to suggest solutions to technical problems related to computer usage. Another CBR system called CASCADE $[54]$ is used to suggest solutions to system crashes related to the VMS operating system. RICAD $[20]$ combines CBR with statistics to predict the potential of a driver making an insurance claim and the likely size of the claim. This information is useful in determining insurance premiums for drivers.

Data mining has been used in the healthcare industry to detect fraudulent health insurance claims and to identify exceptional behavior in patient populations. Electronic fraud detection (EFD) system $[37]$ uses historical claims data to identify healthcare providers that are likely to submit fraudulent insurance claims. EFD examined the records of 21786 providers in six metropolitan areas and recommended about 4% of them for further investigation. KEFIR $[39]$ analyzes performance measures in the health care industry, such as cost, price, usage, and quality, to detect deviations from the norm. It then uses rules for explaining the deviations and for recommending corrective actions. Data mining has also been used to map patient diagnosis and demographic data into surgical procedures to be performed on the patient $[55]$ . This study compared the performances of three techniques, namely NN, RI, and discriminat analysis, and found that NN- and RI-based models committed fewer overall misclassifications than the discriminant analysis-based model.

GAs have been used in manufacturing to solve scheduling problems by obtaining order permutations, process plans and allocation of resources $[59]$ . An interesting application in this area is DBMine $[32]$ , a toolkit for understanding the heuristic behavior of GAs in producing job schedules. GA has also been used to study spending patterns in government offices $[41]$ . Data on fund requests is collected from different government offices and is searched for patterns that may be useful in making budget allocation decisions. Bhargava $[10]$ reports the use of GA to help formulate hypotheses regarding causes of illnesses among Gulf War veterans. A database containing 20,000 records and 150 attributes of military personnel is searched to identify the most crucial sets of attributes that may be linked to illnesses among Gulf War veterans.

SQUAD [1] uses CBR to disseminate software quality knowledge among software developers in an organization. Experience reports on software quality problems and their resolutions are collected in a case-base to allow easy sharing of this expertise. Lee et al. [35] discuss a hybrid approach for software cost estimation. Cluster analysis is used to group similar software projects. The features of a project cluster are then used to identify an appropriate structure of the NN to be used for cost estimation. The attributes of a software project are used as the input to this NN to estimate the cost of the project.

## 5. Discussion

Table 3 shows the distribution of applications by machine learning techniques.

\- RI has many interesting characteristics that make it an appropriate technique for developing data mining applications in business. It is robust in processing large data sets with high predictive accuracy and is well suited for classification and prediction tasks. The results are easy to explain. It has been extensively studied in the literature and is supported by tools that make it easier to implement applications.

Table 3  
Application distribution by technique

<table><tr><td>Technique</td><td>Number of applications</td><td>Percentage</td></tr><tr><td>RI</td><td>34</td><td>48.6</td></tr><tr><td>NN</td><td>10</td><td>14.3</td></tr><tr><td>CBR</td><td>9</td><td>12.9</td></tr><tr><td>GA</td><td>5</td><td>7.1</td></tr><tr><td>ILP</td><td>1</td><td>1.4</td></tr><tr><td>Visualization</td><td>11</td><td>15.7</td></tr><tr><td>Total</td><td>70</td><td>100</td></tr></table>

\- NN has poorer explanation capability, is less efficient in processing large data sets, and requires the user to possess substantial tool knowledge to set up and operate the system. This may explain why NN is less popular than RI in business data mining.

\- CBR is highly useful in a domain that has a large number of examples but may suffer from the problem of incomplete or noisy data. It is still evolving as a machine learning technique. Due to its ability to work with noisy and missing data, its use in business data mining is likely to increase as the technology matures.

\- GA and ILP are relatively new machine learning techniques that require extensive tool knowledge to set up and operate. GA works well with noisy data and is easy to integrate with other systems. Although ILP has several weaknesses, one of its strengths is its powerful modeling language that can model complex relationships.

Even though visualization is not a machine learning technique, we have listed it as a separate category because of its widespread use. Visualization plays a useful role by enabling the analyst to scan the raw data to identify patterns, detect outliers, and develop hypotheses, which are subsequently verified. Visualization also facilitates interpretation of results.

While most of the applications surveyed use a single technique, some applications complementarily combine more than one technique. A notable example in this direction uses NN, GA, and RI to mine classification rules from a database $[64]$ . GA is used to identify the most discriminating features of the data set. These features are used to train an NN. Rules are then extracted from the trained NN. Incorrect rules are revised using an explanation-based algorithm to improve the predictive accuracy of the system. This approach combines the robustness and search ability of GA with high predictive accuracy of NN and interpretability of rules to create a data mining system that outperforms systems based on a single technique. While developing such hybrid systems seem to be beneficial, more studies are required to understand the scope and limitations of these systems and to provide guidelines for developing such systems.

Table 4  
Application distribution by functional area

<table><tr><td>Functional Area</td><td>Number of applications</td><td>Percentage</td></tr><tr><td>Finance</td><td>17</td><td>28.3</td></tr><tr><td>Marketing</td><td>12</td><td>20.0</td></tr><tr><td>Web analysis</td><td>9</td><td>15.0</td></tr><tr><td>Telecom</td><td>7</td><td>11.7</td></tr><tr><td>Others</td><td>15</td><td>25.0</td></tr><tr><td>Total</td><td>60</td><td>100</td></tr></table>

Table 4 shows the distribution of data mining applications by functional area. Finance and marketing lead other areas in application count. Two characteristics of these areas may explain the widespread use of data mining. First, computerization of transaction processing activities has created large databases ready to be mined. Second, these areas offer high potential payoff for data mining applications. The latter is an important consideration in developing data mining applications because of the huge investments required for such applications. Predicting the future is a dominant application category in finance. Whether it involves predicting the ability of a loan applicant to pay back the loan or the change in the stock price, any such information that may reduce the uncertainty in a financial decision is likely to result in substantial payoff. Marketing applications mostly target the customer with a view to understanding customer needs. This information will help develop products and services that better match customer expectations.

Table 5 shows the distribution of applications by problem category and functional area. The counts in this table do not match with those in Tables 3 and 4 due to double counting of some applications that have addressed two problem categories. Classification and prediction are dominant problem categories accounting for a total of 62% of all applications. A large number of financial applications involve predicting the future. Thus, an important use of data mining applications in finance is to reduce the uncertainty in financial transactions. Association is a major problem category in marketing. Market basket analysis and product performance analysis are examples of applications in this category. These applications provide useful information for designing sales and marketing strategies. Web Mining applications seek to understand browsing behavior of net surfers. This information is useful in enhancing Web page design. Detection is a dominant application category in telecommunications. Fraudulent use of telecommunication products is a major cause of loss of revenues to telecom service providers. Detecting fraudulent users can minimize these losses.

Table 5  
Application distribution by functional area and problem category

<table><tr><td></td><td>Finance</td><td>Marketing</td><td>Web analysis</td><td>Telecom</td><td>Other</td><td>Total</td><td>Percentage</td></tr><tr><td>Classification</td><td>2</td><td>3</td><td>5</td><td>2</td><td>8</td><td>20</td><td>31.7</td></tr><tr><td>Prediction</td><td>10</td><td>3</td><td></td><td>2</td><td>4</td><td>19</td><td>30.3</td></tr><tr><td>Association</td><td></td><td>6</td><td>6</td><td></td><td></td><td>12</td><td>19.0</td></tr><tr><td>Detection</td><td>5</td><td></td><td>1</td><td>3</td><td>3</td><td>12</td><td>19.0</td></tr><tr><td>Total</td><td>17</td><td>12</td><td>12</td><td>7</td><td>15</td><td>63</td><td>100</td></tr></table>

While RI may continue to be the dominant technique in business data mining for reasons discussed earlier, other techniques, especially ILP and GA, are expected to find wider use. ILP with its powerful modeling language and GA with its robust search technique offer some unique features that are valuable in many data mining applications. Since these techniques are difficult to implement, development of user friendly tools is necessary to enhance their use. We also expect to see a growth in hybrid applications that complementarily use more than one technique. The growth of Internet commerce is likely to stimulate development of Web Mining applications.

Data mining is a fast growing application area in business organizations. IS managers are often faced with data mining tasks but are overwhelmed with a plethora of techniques and toolkits. This paper aims at helping them understand the role of machine learning techniques in mining business data. We discussed the strengths and weaknesses of each technique in terms of the data and operating characteristics. This knowledge is useful in selecting an appropriate technique(s) for a specific task. The survey of applications presented in this paper provides additional insight into the use of machine learning in business data mining. Interested readers may further explore applications in a specific area through the references listed in this paper. Understanding the scope and limitations of current data mining applications can be very useful in developing new applications.

## Acknowledgements

The authors would like to thank the anonymous reviewers for their helpful comments that have improved the readability and the overall quality of the paper to a great extent. Both authors have contributed equally in this paper and share equal responsibility for all errors and omissions.

## Appendix A

Journal list
ACM Transactions on Database Systems
ACM Transactions on Information Systems
AI Expert
AI Magazine
Artificial Intelligence
Communications of the ACM
Computer Networks and ISDN Systems
Database
Decision Support Systems
Information & Management
IBM Systems Journal
IEEE Computer
IEEE Computer Graphics and Applications
IEEE Expert (now IEEE Intelligent Systems)
IEEE Internet Computing
IEEE Transactions on Knowledge and Data Engineering
IEEE Transactions on Systems, Man and Cybernetics

IEEE Transactions on Pattern Analysis and Machine Intelligence
INFORMS Journal on Computing
International Journal of Intelligent Systems
Information Systems Research
Journal of Management Information Systems
Knowledge-Based Systems
Machine Learning
Management Science
MIS Quarterly
Conferences
Knowledge Discovery and Data Mining
SIGMOD Record

## References

[1] B. Allen, Case-based reasoning: business applications, Communications of the ACM 37 (3), 1994, pp. 40–42.

[2] S.S. Anand, A.R. Patrick, J.G. Hughes, D.A. Bell, A data mining methodology for cross-sales, Knowledge-Based Systems 10, 1998, pp. 449–461.

[3] T. Anand, G. Kahn, Focusing knowledge-based techniques on market analysis, IEEE Expert (1993), pp. 19–24.

[4] T. Anand, Opportunity Explorer: navigating large databases using knowledge discovery templates, Journal of Intelligent Information Systems 4 (1), 1995, pp. 27–38.

[5] C. Apte, S. Weiss, Data mining with decision trees and decision rules, Future Generation Computer Systems 13, 1997, pp. 197–210.

[6] D.S. Barr, G. Mani, Using neural nets to manage investments, AI Expert (1994), pp. 16–21.

[7] B.G. Becker, Using MineSet for knowledge discovery, IEEE Computer Graphics and Application (1997), pp. 75–78.

[8] F. Bergadano, D. Gunetti, Inductive Logic Programming, The MIT Press, Cambridge, MA, 1996.

[9] A. Berson, S.J. Smith, Data Warehousing, Data Mining and OLAP, McGraw-Hill, New York, 1997.

[10] H.K. Bhargava, Data mining by decomposition, INFORMS Journal on Computing 11 (3), 1999, pp. 239–247.

[11] S. Bhattacharya, Direct marketing performance modeling using genetic algorithms, INFORMS Journal on Computing 11 (3), 1999, pp. 248–257.

[12] R.J. Brachman, T. Khabaza, W. Kloesgen, G. Piatetsky-Shapiro, E. Simoudis, Mining business databases, Communications of the ACM 39 (11), 1996, pp. 42–48.

[13] P. Buta, Mining for financial knowledge with CBR, AI Expert (1994), pp. 34–41.

[14] C. Carter, J. Catlett, Assessing credit card applications using machine learning, IEEE Expert Fall (1987), pp. 71–79.

[15] S. Chakrabarti, B.E. Dom, S.R. Kumar, P. Raghavan, S. Rajagopalan, A. Tomkins, D. Gibson, J. Kleinberg, Mining the Web's link structure, IEEE Computer (1999), pp. 60–67.

[16] M.S. Chen, J.S. Park, P.S. Yu, Data mining for path traversal patterns in a Web environment, in: Proceedings of the Sixteenth International Conference on Distributed Computing Systems, 1996, pp. 385–392.

[17] R. Cooley, B. Mobasher, J. Srivastava, Web Mining: information and pattern discovery on the World Wide Web, in: Proceedings of the Ninth IEEE International Conference on Tools with Artificial Intelligence, 1997, pp. 558–567.

[18] M.W. Craven, J.W. Shavlik, Using neural networks for data mining, Future Generation Computer Systems 13, 1997, pp. 211–229.

[19] M. Craven, S. Slattery, K. Nigam, First-order learning for Web Mining, in: Proceedings of the Tenth European Conference on Machine Learning, Chemnitz, 1998, pp. 250–255.

[20] J. Daengdej, D. Lukose, R. Murison, Using statistical models and case-based reasoning in claims prediction: experience from a real-world problem, Knowledge-Based Systems 12, 1999, pp. 239–245.

[21] S.L. Dale, T. Bench-Capon, Data mining tool for producing characteristic classifications in the legal domain, in: Proceedings of the International Conference on Database and Expert Systems Applications, 1997, pp. 186–191.

[22] O. Etzioni, The World Wide Web: Quagmire or Gold Mine? Communications of the ACM 39 (11), 1996, pp. 65–68.

[23] U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, From data mining to knowledge discovery in databases, AI Magazine (1996), pp. 37–53.

[24] J. Furnkranz, J. Petrak, R. Trappl, Knowledge discovery in international conflict databases, Applied Artificial Intelligence 11, 1997, pp. 91–118.

[25] N. Gershon, S.G. Eick, Information visualization applications in the real world, IEEE Computer Graphics and Application (1997), pp. 66–70.

[26] D.E. Goldberg, Genetic and evolutionary algorithms come of age, Communications of the ACM 37 (3), 1994, pp. 113–119.

[27] G.H. John, P. Miller, R. Kerber, Stock selection using rule induction, IEEE Expert (1996), pp. 52–58.

[28] G.H. John, Y. Zhao, Mortgage data mining, in: Proceedings of the IEEE/IAFE Conference on Computational Intelligence for Financial Engineering, 1997, pp. 232–236.

[29] S.H. Kim, H.J. Noh, Predictability of interest rates using data mining tools: a comparative analysis of Korea and the US, Expert Systems with Applications 13 (2), 1997, pp. 85–95.

[30] A.I. Kokkinaki, On atypical database transactions: identification of probable frauds using machine learning for user profiling, in: Proceedings of the IEEE Knowledge and Data Engineering Exchange Workshop, Newport Beach, CA, 1997, pp. 107–113.

[31] J. Kolodner, Case-Based Reasoning, Morgan Kaufmann, San Mateo, CA, 1993.

[32] D.A. Koonce, C.-H. Fang, S.-C. Tsai, A data mining tool for learning from manufacturing processes, Computers and Industrial Engineering 33 (1/2), 1997, pp. 27–30.

[33] M. Kriegsman, R. Barletta, Building a case-based help desk application, IEEE Expert (1993), pp. 18–26.

[34] P. Langley, H.A. Simon, Applications of machine learning and rule induction, Communications of the ACM 38 (11), 1995, pp. 55–64.

[35] A. Lee, C.H. Cheng, J. Balakrishnan, Software development cost estimation: integrating neural network with cluster analysis, Information and Management 34, 1998, pp. 1–9.

[36] H.-Y. Lee, H.-L. Ong, Visualization support for data mining, IEEE Expert (1996) 69–75.

[37] J.A. Major, D.R. Riedinger, EFD: a hybrid knowledge/statistical-based system for the detection of fraud, International Journal of Intelligent Systems 7, 1992, pp. 687–703.

[38] H. Mannila, H. Toivonen, A.J. Verkamo, Discovering frequent episodes in sequences, in: Proceedings of First International Conference on Knowledge Discovery and Data Mining, Montreal, Canada, AAAI Press, Menlo Park, CA, 1995, pp. 210–215.

[39] C.J. Matheus, G. Piatetsky-Shapiro, Selecting and reporting what is interesting, in: U.M. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthuruswamy (Eds.), Advances in Knowledge Discovery and Data Mining, AAAI Press/MIT Press, Cambridge, MA, 1996, pp. 495–515.

[40] W.F. Messier Jr., J.V. Hansen, Inducing rules for expert system development: an example using default and bankruptcy data, Management Science 34 (2), 1988, pp. 1403–1415.

[41] N.H. Packard, A genetic learning algorithm for the analysis of complex data, Complex Systems 4, 1990, pp. 543–572.

[42] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, San Mateo, CA, 1993.

[43] J. Rauch, P. Berka, Knowledge discovery in financial data — a case study, Neural Network World 4 (5), 1997, pp. 427–437.

[44] R.M. Rohrer, E. Swing, Web-based information visualization, IEEE Computer Graphics and Applications (1997), pp. 52–59.

[45] D.E. Rumelhart, B. Widrow, M.A. Lehr, The basic ideas in neural networks, Communications of the ACM 37 (3), 1994, pp. 87–92.

[46] R. Sasisekharan, V. Seshadri, Data Mining and forecasting in large-scale telecommunication networks, IEEE Expert (1996), pp. 37–43.

[47] R.T. Scarfe, R. J. Shortland, Data mining applications in BT, IEE Colloquium (Digest) (1995) 5/1–5/4, pp.

[48] J.D. Schmitz, G.D. Armstrong, J.D.C. Little, CoverStory — automated news finding in marketing, Interfaces 20 (6), 1990, pp. 29–38.

[49] P.G. Selfridge, D. Srivastava, L.O. Wilson, IDEA: interactive data exploration and analysis, in: Proceedings of SIGMOD '96, Montreal, Canada, ACM Press, New York, 1996, pp. 24–34.

[50] T.E. Senator, H.G. Goldberg, J. Wooton, M.A. Cottini, A.F. Umar Khan, C.D. Klinger, W.M. Llamas, M.P. Marrone, R.W.H. Wong, The financial crimes enforcement network AI system (FAIS) identifying potential money laundering from reports of large cash transactions, AI Magazine (1995), pp. 21–39.

[51] R. Setiono, J.Y.L. Thong, C.-S. Yap, Symbolic rule extraction from neural networks, Information and Management 34 (2), 1998, pp. 33–40.

[52] M.J. Shaw, J.A. Gentry, Inductive learning for risk classification, IEEE Expert (1990), pp. 47–53.

[53] R. Shortland, R. Scarfe, Digging for gold, IEE Review 41 (5), 1995, pp. 213–217.

[54] E. Simoudis, Using case-based retrieval for customer technical support, IEEE Expert (1992), pp. 7–12.

[55] W. Spangler, J.H. May, L.G. Vargas, Choosing data-mining methods for multiple classification: representational and performance measurement implications for decision support, Journal of Management Information Systems 16 (1), 1999, pp. 47–62.

[56] E. Spartus, ParaSite: mining structural information on the Web, Computer Networks and ISDN Systems 29, 1997, pp. 1205–1215.

[57] T.K. Sung, N. Chang, G. Lee, Dynamics of modeling in data mining: interpretive approach to bankruptcy prediction, Journal of Management Information Systems 16 (1), 1999, pp. 63–85.

[58] R. Tsaih, Y. Hsu, C.C. Lai, Forecasting S(P 500 stock index futures with a hybrid AI system, Decision Support Systems 23, 1998, pp. 161–174.

[59] S. Uckun, S. Bagchi, K. Kawamura, Y. Miyabe, Managing genetic search in job shop scheduling, IEEE Expert (1993), pp. 15–24.

[60] M.S. Viveros, S. Elo-Dean, M.A. Wright, S.S. Duri, Visitors' behavior: mining Web servers, in: Proceedings of First International Conference on the Practical Applications of Knowledge Discovery and Data Mining, London, UK, 1997, pp. 257–269.

[61] I. Vollrath, W. Wilke, R. Bergmann, Case-based reasoning support for online catalog sales, IEEE Internet Computing (1998), pp. 47–54.

[62] R.L. Wilson, R. Sharda, Bankruptcy prediction using neural networks, Decision Support Systems 11, 1994, pp. 545–557.

[63] K.-L. Wu, P.S. Yu, A. Ballman, SpeedTracer: a Web usage mining and analysis tool, IBM Systems Journal 37 (1), 1998, pp. 89–105.

[64] Z. Yuanhui, L. Yuchang, S. Chunyi, Combining neural network, genetic algorithm and symbolic learning approach to discover knowledge from databases, in: Proceedings of the IEEE International Conference on Systems, Man and Cybernetics, Vol. 5, Orlando, FL, 1997, pp. 4338–4393.

![](/api/attachments/FMP76M4M/fulltext/images/ce10be203e04df516df39edfb726093b93c0730a63c8e0a4b0409ab06f1a73c6.jpg)  
Indranil Bose is Assistant Professor of Decision and Information Sciences at the University of Florida. He holds a BTech (Hons) in Electrical Engineering from the Indian Institute of Technology, Kharagpur, an MS in Electrical and Computer Engineering from the University of Iowa, an MS in Industrial Engineering and a PhD in Management from Purdue University. His publications have appeared in Computers and

Operations Research, Decision Support Systems and Ergonomics. His research interests are in the areas of design and pricing issues in telecommunications, data mining, and applied operations research. His teaching interests are telecommunications and networking, database management systems, systems analysis and design and knowledge-based systems.

![](/api/attachments/FMP76M4M/fulltext/images/c87ac5f0ffa50d3e103ca48f0e5b01b217ecff5ef3196ef20b9804ab5919c2eb.jpg)

Radha K. Mahapatra is Assistant Professor of Information Systems at the University of Texas at Arlington. He holds a BSc (Hons) degree in Electrical

Engineering from Regional Engineering College, Rourkela, India, a PGDM from the Indian Institute of Management, Ahmedabad, India, and a PhD in Information Systems from Texas A&M University. His research interests are in the areas of physical database design, data mining, case-based reasoning, systems analysis and design, software reuse and knowledge management. His research publications have appeared in Decision Support Systems, Information & Management, Data Base and other journals.
