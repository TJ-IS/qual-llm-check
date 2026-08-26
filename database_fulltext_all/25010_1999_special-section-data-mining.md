---
otero_id: 25010
otero_key: "KQ27H79M"
title: "Special Section: Data Mining"
authors: "H. Michael Chung; Paul Gray"
year: "1999"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1999.11518231"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Special Section: Data Mining

## H. Michael Chung & Paul Gray

To cite this article: H. Michael Chung & Paul Gray (1999) Special Section: Data Mining, Journal of Management Information Systems, 16:1, 11-16, DOI: 10.1080/07421222.1999.11518231

To link to this article: http://dx.doi.org/10.1080/07421222.1999.11518231

![](/api/attachments/KQ27H79M/fulltext/images/3cc478d1ed1a77f4b0a453ce9b139132f9de59502cd1ba5be56109f6107a9785.jpg)

Published online: 02 Dec 2015.

![](/api/attachments/KQ27H79M/fulltext/images/52df362b281cfcf3213a4897d06eb0a6588e156c1091a2875803c34c0bbf3748.jpg)

Submit your article to this journal ↗

![](/api/attachments/KQ27H79M/fulltext/images/05e14cf1b39ae10a4486f0eb9f384f75a07ea4241304ca13ac5993a8ad9af197.jpg)

Article views: 7

![](/api/attachments/KQ27H79M/fulltext/images/708d3be4c6e827262287b14218bb84691a4e6b4da702234cc41677f55840c366.jpg)

View related articles ↗

![](/api/attachments/KQ27H79M/fulltext/images/3c252fe4e3add7414ec94066532e5d43291ed90e1ce67c8e8ba0594ca435c69b.jpg)

Citing articles: 5 View citing articles ↗

# Special Section: Data Mining

H. MICHAEL CHUNG AND PAUL GRAY, Guest Editors

H. MICHAEL CHUNG is Professor in the Department of Information Systems at California State University, Long Beach. He is also Director of the Center for Information Systems Technologies. He was previously on the faculty at Texas A&M University. He received both his Ph.D. and M.B.A. from UCLA. His industry experience includes systems engineering at IBM. He received the Edward W. Carter Award and SIM Award.

Dr. Chung's current research interests include decision modeling by applying machine learning, data mining and telecommunications and networks, including capacity planning and system security and control. His recent publications appear in Decision Sciences, Review of Communications, International Journal of Intelligent Systems, International Journal of Computer and Engineering Management, Journal of Knowledge Engineering, and Decision Support Systems, among others. He is coauthor of the forthcoming book, Electronic Commerce. Dr. Chung has been guest editor of the International Journal of Decision Support Systems. He is the organizer of the Data Mining and Knowledge Discovery minitrack at the Hawaii International Conference on System Sciences. His latest funded research projects deal with the national information infrastructure, neural network applications, and a wireless system.

PAUL GRAY is Professor of Information Science at Claremont Graduate University and founding chair of its Program in Information Science. He specializes in decision support systems, data warehousing, and knowledge management. He worked for eighteen years in research and development organizations, including nine years at SRI. He was previously a faculty member at Stanford University, the Georgia Institute of Technology, the University of Southern California, and Southern Methodist University, and was President of the Institute of Management Sciences for 1992–93 and formerly president-elect, vice-president, and secretary of the institute. He is Editor of the Communications of the Association for Information Systems and is on the editorial board of several journals. He is the author of over 110 journal articles and author or editor of thirteen books. He received his Ph.D. from Stanford University.

THREE NEW INTERRELATED TOPICS HAVE APPEARED IN INFORMATION SYSTEMS in the last several years: data mining, $^{1}$ data warehousing, and knowledge management. All three are related to obtaining more return from the information gathered by an organization. This Special Section concentrates on data mining.

The objective of data mining is to identify valid, novel, potentially useful, and understandable correlations and patterns in existing data. In the popular mind, data mining refers to finding answers from a company's data that an analyst or an executive has not thought to ask. The reality is not quite that grand, though data mining does create both data and insights that add to the organization's knowledge.

Data mining can proceed from the bottom up (explore raw facts to find connections) or from the top down (search to test hypotheses). Bottom-up data mining tries to find hypotheses that can then be tested. This approach differs from that used in most information systems studies, where the investigator states the hypothesis and then tests it with t-tests or other statistical techniques.

Every new field has its initial successes that intrigue others to investigate it further. Early results from data mining indicate, for example:

\- That people who buy scuba gear take Australian vacations,

\- That men who buy diapers on Friday night also tend to buy beer,

• Who is likely to repay a loan,

\- Appropriate play selection and matchups in National Basketball Association games.

These results are extreme cases. Usually, data mining leads to steady incremental changes rather than major transformations. It leads to small advantages each year with each customer and each project. Over time, these changes accumulate like compound interest. Although breakthroughs occur from time to time, they cannot be counted on to happen on a regular basis.

## Steps in Data Mining

THE FOLLOWING STEPS ARE USUALLY FOLLOWED IN DATA MINING. These steps are iterative, with the process moving backward whenever needed.

1. Develop an understanding of the application, of the relevant prior knowledge, and of the end user's goals.

2. Create a target data set to be used for discovery.

3. Clean and preprocess data (including handling missing data fields, noise in the data, accounting for time series, and known changes).

4. Reduce the number of variables and find invariant representations of data if possible.

5. Choose the data-mining task (classification, regression, clustering, etc.).

6. Choose the data-mining algorithm.

7. Search for patterns of interest (this is the actual data mining).

8. Interpret the pattern mined. If necessary, iterate through any of steps 1 through 7.

9. Consolidate knowledge discovered and prepare a report.

The first two steps—understanding the application and determining the target data to be used for discovery—are common to all forms of data analysis. These steps include knowing what relevant prior knowledge exists, the goals of the project, and what data exist. If a data warehouse is available, its metadata help in pinpointing what data exist. The third step—cleaning and preprocessing the data—is the usual one used in preparing data for warehousing. Organizational data are cleaned and validated before being put in the warehouse. For knowledge discovery, further preprocessing is used to remove outliers and noise in the data.

The fourth and fifth steps involve reducing the number of variables and choosing the data classification task. With too many variables, it becomes difficult to make sense of the results. Therefore, the analyst applies dimensionality reduction or transformation techniques and tries to find representations of the data that are invariant.

KDD involves looking in the data for such factors as:

\- Associations: things done together (e.g., buying groceries).

\- Sequences: events occurring over time (e.g., house, refrigerator).

\- Classifications: rules for recognizing patterns (e.g., days on which restaurant customers arrive and what they order).

\- Clusters: defining new groups (e.g., market segments).

\- Forecasting: predictions from time series (e.g., stock market fluctuation).

The sixth and seventh steps (choosing the data-mining algorithm and searching for patterns) are the heart of the KDD process. The algorithm selected depends on the task to be performed. It is in these steps that the actual mining is done. They involve fitting models or determining patterns from the warehouse data. Patterns are represented according to classification rules or trees, regression functions, or other knowledge or model representation methods, clustering, and sequences.

The specific models come from a variety of fields including:

• Statistical analysis of data.

\- Neural networks.

\- Expert systems.

\- Fuzzy logic.

\- Intelligent agents.

• Multidimensional analysis.

\- Data visualization.

\- Decision trees.

The software associated with these steps is called “sftware.” As used in sftware, data-mining algorithms consist of three components:

\- The model,

• The preference criterion, and

• The search algorithm.

The parameters of the model are determined from the data. The preference for a particular model depends on the data available. Usually, some form of “goodness-of-fit” criterion is used. Care has to be taken that the model does not try to infer too much (overfitting) or too little (too many degrees of freedom) from the data. The search algorithm is selected based on the model and the preference criterion being used. The selection of these three components is still an art.

The eighth step introduces the human back into the picture. The results of the data-mining operation of step 7 are examined by an analyst who judges whether the outcomes are possible, internally consistent, and plausible. “Possible” implies that the result is physically possible (e.g., does not exceed the speed of light); “internal consistency” implies that the result does not contradict itself; and “plausible” means that the association found is believable, that is, it could happen.

If the analyst is dissatisfied with the outcome, he or she can rerun the case with revised or refined queries and conditions. That is, the process is iterative, with the analyst asking questions after each new set of computer results. Once the analyst is satisfied with the output, the results are interpreted (step 8) and the findings are reported (step 9). These steps involve presenting the results in a form that is more understandable to decision makers. Such approaches as representing patterns graphically, structuring rules based on the patterns, resolving redundancy and conflicts with previous results, and explaining findings in natural language are all involved here. Finally, actions are based on the findings.

There are limits to data mining. Data mining is still an art, requiring skillful analysis and choice of methodology. It requires subject area expertise, experience with large databases, and skills with data-mining algorithms. As indicated by the list above, the techniques being used come from existing classical statistics or artificial intelligence techniques. Problems encountered with data, including overfitting existing data, missing and noisy data, and dealing with very large databases and very high dimensionality, need to be resolved. Furthermore, for large-scale, real-world tasks, high performing algorithms (such as neural networks and genetic algorithms) must cope with long computation times and difficulties in making interpretations. Techniques associated with probabilistic learning need to be improved.

## Research Issues

MANY ISSUES STILL NEED TO BE ADDRESSED to reap quality knowledge from the sophisticated algorithms available for data mining. For example:

• How good is the quality of discovered knowledge?

\- Does the same method always produce the same results?

\- Are different tools required for different application domains?

• What factors affect tool performance?

• How do human cognitive factors affect the results?

Primary research issues include:

1. Methodological issues in applying the tools,

2. Performance improvement through the integration of tools and techniques,

3. Exogenous factors to consider in modeling,

4. Interdisciplinary perspectives, and

5. The economics of data mining.

Data are an important issue. Dealing with incomplete raw data or erroneous input is not a trivial task. The size of the data set needed to apply an algorithm, duplicate data, and temporal data, as well as multimedia representation of data are concerns. How a data-mining technique can learn to improve itself through experience is another interesting issue.

Algorithms differ in the ways models are generated. How the quality of an algorithm is assessed, its robustness, scalability, preprocessing, generalizability, and reliability are critical issues. The way model performance is measured is an important consideration. The same model performs differently in different domains because of the quality of the data, normative criteria, and the decision-maker factors involved. Noise tolerance and sensitivity analysis are also of interest.

Scalability is particularly significant. This refers to the ability to maintain performance as the size of the database being mined increases. Scalable mining tools take advantage of parallel computing. Therefore, better parallel algorithms as well as direct access to parallel database management systems are research topics. When human decision makers are involved, decision-making modeling as well as the database often have to consider cognitive factors. In addition, domain task characteristics affect model performance. Nonlinearity and nonmonotonicity issues can be addressed by data visualization.

In summary, in generating a data-mining model and in selecting the appropriate model assessment method, data-mining research needs to incorporate the characteristics of a given task domain, quality and composition of a dataset that represents a domain, the decision-making environment, the human factors, and potential interaction among them. Figure 1 is a simple framework that incorporates these ideas.

## Papers in the Special Section

IT IS CLEAR THAT DATA MINING IS STILL IN ITS INFANCY and therefore offers great research opportunities. It is a multidisciplinary field, using inputs from statisticians who deal with data, computer scientists and operations researchers creating new algorithms, and information systems people looking at how to cope with the systemic and human limitations that exist. The three papers in this Special Section present results that address some of the current limitations of data mining.

The first paper describes a conceptual development and an implementation for exploring hypothesis space in data mining. The problem faced by data miners is that the information obtained is very difficult to understand and hence to represent because of high dimensionality. Steven O. Kimbrough and his colleagues present a clever way of creating simple visualizations that make this task manageable.

William E. Spangler, Jerrold H. May, and Luis G. Vargas discuss the effects of errors, data representation, and assessment approach in data mining. Data-mining techniques designed for classification problems usually assume that each observation is a member of only one category. The authors extend these methods to the case in which observations may be full members of multiple categories. They evaluate three of the popular methods (decision tree induction, linear discriminant analysis, and neural networks) and explore representational and performance measurement perspectives.

![](/api/attachments/KQ27H79M/fulltext/images/97a6c3c63335922eabc99aec50986a04c830c31c89f5a464450a18a538ce2664.jpg)  
Figure 1. Data-Mining Research Framework

Tae Kyung Sung, Namsik Chang, and Gunhee Lee apply data mining to predicting bankruptcy. They show that different parameters for forecasting bankruptcy are obtained when economic conditions are normal and when countries are operating in crisis mode, as has been the case recently in parts of Asia. Consideration of the influence of exogenous factors on the performance of a data-mining model is noteworthy in this paper.

It is clear from these papers, and from the many that were submitted, that much still needs to be done. Data mining is a rich research field that deserves the attention of the information systems research community.

## NOTE

1. Data mining is also known as knowledge discovery in databases (KDD). The term data mining is usually applied to the operational procedure for obtaining new insights, whereas KDD is used by the research community developing new techniques. We use the terms interchangeably.
