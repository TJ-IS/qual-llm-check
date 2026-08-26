---
otero_id: 15626
otero_key: "D2AKQUSF"
title: "A multidimensional analysis of data quality for credit risk management: New insights and challenges"
authors: "Helen-Tadesse Moges; Karel Dejaeger; Wilfried Lemahieu; Bart Baesens"
year: "2013"
journal: "Information & Management"
doi: "10.1016/j.im.2012.10.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A multidimensional analysis of data quality for credit risk management: New insights and challenges

Helen-Tadesse Moges <sup>a</sup>, Karel Dejaeger <sup>a</sup>, Wilfried Lemahieu <sup>a</sup>, Bart Baesens <sup>a,b,c,</sup>\*

<sup>a</sup> Department of Decision Sciences and Information Management, Katholieke Universiteit Leuven, Naamsestraat 69, B-3000 Leuven, Belgium <sup>b</sup> School of Management, University of Southampton, Southampton, SO17 1BJ, United Kingdom

<sup>c</sup> Vlerick Leuven Gent Management School, Leuven, Belgium

## A R T I C L E I N F O

Article history: Received 18 January 2012 Received in revised form 9 September 2012 Accepted 29 October 2012 Available online 16 November 2012

Keywords: Data quality Information quality Credit risk Data definition

## A B S T R A C T

Recent studies have indicated that companies are increasingly experiencing Data Quality (DQ) related problems as more complex data are being collected. To address such problems, the literature suggests the implementation of a Total Data Quality Management Program (TDQM) that should consist of the following phases: DQ definition, measurement, analysis and improvement. As such, this paper performs an empirical study using a questionnaire that was distributed to financial institutions worldwide to identify the most important DQ dimensions, to assess the DQ level of credit risk databases using the identified DQ dimensions, to analyze DQ issues and to suggest improvement actions in a credit risk assessment context. This questionnaire is structured according to the framework of Wang and Strong and incorporates three additional DQ dimensions that were found to be important to the current context (i.e., actionable, alignment and traceable). Additionally, this paper contributes to the literature by developing a scorecard index to assess the DQ level of credit risk databases using the DQ dimensions that were identified as most important. Finally, this study explores the key DQ challenges and causes of DQ problems and suggests improvement actions. The findings from the statistical analysis of the empirical study delineate the nine most important DQ dimensions, which include accuracy and security for assessing the DQ level.

\- 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The risk of poor Data Quality (DQ) increases as larger and more complex information resources are collected and maintained [27,23]. Because most modern companies tend to collect increasing amounts of data, good data management is becoming increasingly important. In response, in the previous two decades, the aspect of DQ has received a lot of attention by both organizations worldwide and in academic literature. Several studies have explored DQ challenges and have focused on DQ measurement and improvement [3–11,19–27,30,32–34,39, 37,40,41,43–48]. Fig. 1 illustrates this focus by plotting the increasing number of DQ related publications over the past ten years as reported by ISI Web of Knowledge.

In practice, decision makers differentiate information from data intuitively and describe information as data that has been processed. Unless otherwise specified, this paper uses data interchangeably with information.

DQ is often defined by ‘fitness for use’ which implies the relative nature of the concept [30,21,4]. Quality data for one use may not be appropriate for other uses. For instance, the extent to which data are required to be complete for accounting tasks may not be required for sales prediction tasks. Accounting tasks typically require the availability of all cash balances, e.g., when making up a balance sheet. Conversely, sales prediction tasks will always be possible irrespective of missing cash balances [30,37]. In addition to the task type, the contextuality of DQ can also be explained by the trade-offs between DQ dimensions where one dimension can be favored over other dimensions for a specific task. Data quality dimensions are not independent but are, in fact, correlated [22]. Moreover, if one dimension is considered more important than other dimensions for a specific application, then the choice of favoring this dimension may negatively affect other dimensions. For example, having accurate data may require checks that could negatively affect timeliness. Conversely, having timely data may result in less accuracy, completeness or consistency. A typical situation in which timeliness can be preferred to accuracy, completeness, or consistency is given by most web applications. As time constraints are often very stringent for web data, it is possible that such data are deficient with respect to other quality dimensions. For instance, a list of courses published on a university web site must be timely though there could be accuracy or consistency errors, and some fields specifying additional course details could be missing. Conversely, when considering administrative applications, accuracy, consistency and completeness requirements are more essential than timeliness, and therefore, delays are mostly permissible. Another example can be a trade-off between completeness and consistency. A statistical data analysis typically requires a significant and representative set of data, and in this case, the approach will be to favor completeness while tolerating inconsistencies or adopting techniques to address these inconsistencies. Conversely, when publishing a list of student scores on an exam, it is crucial to check the list for consistency, which may possibly defer the publication of the complete list [30,4]. Accordingly, studying the DQ in the context of a specific task is a recognized method [11,25–27,30,47,48].

![](/api/attachments/D2AKQUSF/fulltext/images/7bf4e623753615bf847c86cac19fd41e3b80655ecbff7d2560e703cfcaace15f.jpg)  
Fig. 1. Journal and conference proceedings from ISI web of knowledge

## 1.1. Credit risk assessment task

DQ is of special interest and relevance in a credit risk setting because of the introduction of compliance guidelines, such as Basel II and Basel III [2,15]. Because the latter has a direct impact on the capital buffers and, hence, on the safety of financial institutions, special regulatory attention is being given to addressing DQ issues and concerns in this context. Therefore, given its immediate strategic impact, DQ in a credit risk setting is more closely monitored than in most other settings and/or business units [42,34].

The credit risk assessment task is primarily concerned with quantifying the risk of the loss of principal or interest stemming from a borrower’s failure to repay a loan or meet a contractual obligation. Therefore, financial institutions are obliged to assess the credit risk that may arise from their investment. These institutions may estimate this risk by taking into account information concerning the loan and the loan applicant.

The quality of the credit approval process from a risk perspective is determined by the best possible identification and evaluation of the credit risk that results from a possible default on a loan. Credit risk can be decomposed into four risk parameters as described in the Basel II documentation [42]. These parameters are the Probability of Default (PD), the Loss Given Default (LGD), the Exposure at Default (EaD) and the Maturity (M). These parameters are used to calculate the Buffer Capital (BC), which also referred to as regulatory capital and is the money set aside to anticipate future unexpected losses due to loan defaults.

$$
\mathrm{BC} = f (\mathrm{PD}, \mathrm{LGD}, \mathrm{EaD}, \mathrm{M})
$$

The correct estimation of these parameters and the appropriateness of the function or algorithm used to calculate the risk concentration are crucial because incorrect parameters or inappropriate algorithms may result in a loss or even bankruptcy of the institution. The Risk Concentration (RC) refers to an exposure with the potential to produce losses large enough to threaten a financial institution’s health or ability to maintain its core operations [1]. Improving the quality of the data used for calculating these parameters is one way of improving the precision of the parameter estimates and, consequently, of improving the correctness of the credit approval decisions [2,14].

## 1.2. Total Data Quality Management Program

Poor DQ impacts organizations in many ways. At the operational level, poor DQ has an impact on customer satisfaction, increases operational expenses and can lead to lowered employee job satisfaction. Similarly, at the strategic level, poor DQ affects the quality of the decision making process. An enterprise may experience various DQ problems [21,34]. However, no improvement can be made without knowing and measuring the problems. It is argued in the literature that organizations should implement a Total Data Quality Management (TDQM) program that includes DQ definition, measurement, analysis and improvement. This enables them to achieve a suitable DQ level [39,28].

The DQ definition phase is the starting point for a TDQM program. In this phase, all the necessary DQ dimensions to be measured, evaluated and analyzed are identified. Next, the measurement process is implemented. The results from the measurement process are analyzed, and DQ issues are detected. These issues will be taken into account during the improvement phase. In this phase, the collection of poor quality data cases is thoroughly investigated, and improvement actions are suggested. The four phases are iterated in this order over time, as shown in Fig. 2. In fact, the primary goal of DQ assurance is the continuous control of data values and possibly their improvement [44,4].

The identification of DQ dimensions from a user perspective defines the list of important DQ dimensions for a specific task that need to be assessed, analyzed and improved [44,4]. Therefore, the first aim of this paper is to identify the DQ dimensions that are considered relevant to assess the DQ in the context of credit risk assessment. Second, the paper investigates the impact of different factors, such as the existence of DQ teams and the size of financial institutions, on the importance of DQ dimensions. Third, the DQ level of a credit risk databases is assessed by incorporating the DQ dimensions categorized as relevant, and finally, frequent recurring DQ challenges and their causes in a credit risk assessment context are also explored.

The remainder of the paper is structured as follows. The next section explores the related literature, while the third section explains our research methodology. The fourth section elaborates on the key findings, while the final section presents the conclusions and lists topics for further research.

## 2. Related research

## 2.1. Identification and definition of DQ dimensions

DQ problems cannot be addressed effectively without identify ing the relevant DQ dimensions. Therefore, the first objective of DQ research is to determine the characteristics of the data that are important to or suitable for data consumers [46]. While fitness for use captures the essence of the DQ, it is difficult to measure the DQ using this broad definition [3,20]. Therefore, it has long been acknowledged that the data are best described or analyzed using multiple attributes or dimensions [24,37,41]. However, despite broad discussions in the DQ literature, there is no single, precisely defined set of DQ dimensions because DQ is context dependent (see, e.g., the studies presented in Table 1).

![](/api/attachments/D2AKQUSF/fulltext/images/bad33893966168a71a995b56f631a090702558eaf74d2383e6b35b4ad4e5ef65.jpg)  
Fig. 2. A schematic overview of the TDQM methodology, adopted from Massachusetts Institute of Technology (MIT) [44].

Different studies have analyzed DQ from a task-specific perspective. For example, Zhu and Gauch [53] assessed the DQ of a web page in terms of a DQ framework comprising six DQ dimensions, which were, namely, currency, availability, information-to-noise ratio, authority, popularity, and cohesiveness. They measured these dimensions using the properties of web pages. Similarly, Chien et al. [5] assessed different DQ dimensions to evaluate the quality of online product reviewing by customers. Of course, they adopted some sort of definitions of the different DQ dimensions for the quality analysis of the online product reviews. For example, they defined objectivity as the extent to which an information item is biased. They defined the appropriate amount of data as the extent to which the volume of information in a review is sufficient for decision making. Additionally, they defined completeness as the extent to which the information in a review is complete and covers various aspects of a product. Furthermore, they defined objectivity and the appropriate amount of information as the effective DQ dimensions used to identify product review quality but assessed completeness as a very ineffective DQ dimension to measure the quality of a product review by customers or other parties.

Conversely, there are a number of studies that identify and define DQ dimensions regardless of the use of the data to facilitate the general applicability and comparability of their DQ dimensions. In this regard, Wand and Wang [43] based their definition of

DQ on the internal view of information systems (data production and system design processes) because this view is context independent. This approach allows for the definition of a set of DQ dimensions that are comparable across applications. First, they identified different criteria for a real-world system to be properly represented by an information system. Based on these criteria, they defined four deficiencies that were, namely, ambiguous representation, incomplete representation, meaningless states, and operation deficiencies. Based on these deficiencies, they summarized different DQ aspects into complete, unambiguous, meaningful, and correct DQ dimensions. Additionally, in the same study, they categorized different DQ dimensions from the literature as internal view (design or operation related) and external view (use or value related), whereby both views were further refined as either system- or data-related DQ dimensions. Within the internal view, the accuracy or precision, the timeliness or currency, the reliability, the completeness and the consistency are defined as data-related, and the reliability is defined as a system-related DQ dimension. Conversely, in the external view, the timeliness, the relevance, the content, the importance and the sufficiency are defined as data-related, and the timeliness, the flexibility, the format and the efficiency are defined as systemrelated DQ dimensions.

Similarly, Wang and Strong [46] analyzed the various DQ dimensions from end user’s perspectives but did not take into account the use of the data. They conducted a large-scale survey to determine and categorize the DQ dimensions. Their analysis began by collecting information from users regarding various DQ descriptors that resulted in over 100 items that were grouped into 20 categories. These were further aggregated into four broad DQ categories: intrinsic (the extent to which data values conform to the actual or true values), contextual (the extent to which data are applicable to the task of the data user), representational (the extent to which data are presented in an intelligible and clear manner), and accessibility (the extent to which data are available or obtainable). Table 1 illustrates the framework of Wang and Strong by classifying the DQ dimensions used in different studies according to this framework [46].

A waterfall-based literature survey was adopted to identify the most often recurring DQ dimensions and their definitions. As such, only dimensions adopted in three or more papers were retained and were used together with the DQ dimensions from our own pilot survey, see Section 3.2.1. In fact, we adopted the DQ framework of Wang and Strong to classify the DQ dimensions [46]. This framework is recognized as the only framework that attempts to strike a balance between theoretical consistency and practicability. Furthermore, the framework has been found to be applicable to various domains [10]. The structure of the framework is hierarchical and organizes DQ aspects along fifteen DQ dimensions to comprehend the four broad DQ categories. Table 2 provides an overview of the DQ dimensions considered in this study. We believe that these DQ dimensions provide a comprehensive coverage of the multi-dimensional nature of DQ. Therefore, in this paper, we used this summary to measure the applicability of the DQ dimensions for the credit risk assessment task.

DQ dimensions from the literature ordered according to the framework of Wang and Strong [48].

<table><tr><td>Ref.</td><td>Intrinsic DQ</td><td>Contextual DQ</td><td>Representational DQ</td><td>Accessibility DQ</td></tr><tr><td rowspan="2">[48]</td><td>Accuracy, completeness, consistency, validity</td><td>Timeliness</td><td>Uniqueness</td><td></td></tr><tr><td>Accuracy, believability, reputation, objectivity</td><td>Value-added, relevancy, completeness, timeliness, appropriate amount</td><td>Understandability, interpretability, concise and consistent representation</td><td>Accessibility, ease of operations, security</td></tr><tr><td>[45]</td><td>Correctness, unambiguous</td><td>Completeness</td><td>Meaningfulness</td><td></td></tr><tr><td>[9]</td><td>Accuracy, precision, reliability, freedom from bias</td><td>Importance, relevance, usefulness, informativeness, content, sufficiency, completeness, currency, timeliness</td><td>Understandability, readability, clarity, format, appearance, conciseness, uniqueness, comparability</td><td>Usableness, quantitativeness</td></tr></table>

Table 2  
Most recurring DQ dimensions in literature and their definitions.

<table><tr><td>Cat.</td><td>DQ dimensions</td><td>Definitions</td><td>References</td></tr><tr><td rowspan="3">Intrinsic</td><td>Accuracy (AC)</td><td>The extent to which data are certified, error-free, correct, flawless and reliable</td><td>[1,3,5,8,20,22,26,28,31,33,35,38,41-43,45,46,48,50]</td></tr><tr><td>Objectivity (OBJ)</td><td>The extent to which data are unbiased, unprejudiced, based on facts and impartial</td><td>[1,5,8,20,22,26,31,42,46,48]</td></tr><tr><td>Reputation (REP)</td><td>The extent to which data are highly regarded in terms of its sources or content</td><td>[3,5,20,22,26,31,42,48]</td></tr><tr><td rowspan="6">Contextual</td><td>Completeness (COM)</td><td>The extent to which data are not missing and covers the needs of the tasks and is of sufficient breadth and depth to the task at hand</td><td>[1,4,5,8,20,22,26-28,31,35,38,42,45,46,48,50]</td></tr><tr><td>Appropriate amount (APM)</td><td>The extent to which the volume of information is appropriate for the task at hand</td><td>[5,20,22,26,28,42,46,48]</td></tr><tr><td>Value-added (VAD)</td><td>The extent to which data are beneficial and provides advantages from its use</td><td>[5,20,22,26,28,42,46,48]</td></tr><tr><td>Relevance (REL)</td><td>The extent to which data are applicable and helpful for the task at hand</td><td>[5,20,22,26,28,42,45,46,48]</td></tr><tr><td>Timeliness (TIM)</td><td>The extent to which data are sufficiently up-to-date for the task at hand</td><td>[5,8,20,22,26,31,38,42,45,46,48,50]</td></tr><tr><td>Actionable (ACT)</td><td>The extent to which data is ready for use</td><td>Pilot survey</td></tr><tr><td rowspan="4">Representation</td><td>Interpretable (INT)</td><td>The extent to which data are in appropriate languages, symbols, and the definitions are clear</td><td>[5,20,22,26,31,46,48]</td></tr><tr><td>Easily understandable (EU)</td><td>The extent to which data are easily comprehended</td><td>[5,20,22,26,31,42,46,48]</td></tr><tr><td>Representational consistent (RC)</td><td>The extent to which data are continuously presented in same format</td><td>[5,20,22,26,31,35,42,43,45,46,48]</td></tr><tr><td>Concisely represented (CR)</td><td>The extent to which data is compactly represented, well presented, well-organized, and well-formatted</td><td>[5,20,22,26,31,35,42,43,45,46,48]</td></tr><tr><td rowspan="4">Access</td><td>Alignment (AL)</td><td>The extent to which data is reconcilable (compatible)</td><td>Pilot survey</td></tr><tr><td>Accessibility (ACC)</td><td>The extent to which data is available, or easily and swiftly retrievable</td><td>[5,20,22,26,31,42,46,48]</td></tr><tr><td>Security (SEC)</td><td>The extent to which access to data is restricted appropriately to maintain its security</td><td>[5,20,22,26,31,42,46,48]</td></tr><tr><td>Traceability(TRA)</td><td>The extent to which data is traceable to the source</td><td>Pilot survey and [24]</td></tr></table>

## 2.2. Data quality: intrinsic and contextual

DQ can be measured by many dimensions, such as accuracy, completeness, timeliness, relevance, objectivity, believability and others [44,10]. Some of these dimensions (e.g., accuracy and objectivity) lend themselves to objective measurement that is intrinsic to the data itself and is independent from the context in which the data are used. There are, however, DQ dimensions that cannot be measured objectively. For example, the two recognized DQ dimensions, relevance and believability [49,11], tend to vary with the usage context. Data relevance mostly depends on the task, because data that are highly relevant for one task may be irrelevant for another; for example, data on depreciation of stocks are required when creating a balance sheet, but these data are irrelevant for marketing tasks. To understand the contextual effects of DQ, it is important to take factors that pertain to the use of data into account. In this regard, factors, such as the relevance of the data to the task, the ability of the user to understand the data, and the clarity of the task, affect the usability of that data [48]. From this usage perspective, DQ assessment tends to be contextual. Furthermore, users that suppose data to be of poor quality are unlikely to weigh the data heavily in their decisionmaking tasks even if it is objectively of high quality. Many researchers, such as Fisher and Ballau [11] and Shankaranarayanan and Zhu [38], identified the impact of experience, task type and time constraints on the possible use of DQ information. Their results indicated that when experience level increases and task complexity decreases, information about the specific quality of the data is more often used in decision-making tasks. Likewise, other researchers, such as Price and Shanks [31], investigated the impact of decision-making strategies on the use of DQ-related information. In general, these studies illustrate the existence of factors that can affect DQ assessment and encourage us to investigate whether other factors, such as the existence of DQ teams and the size of organizations, would impact DQ assessment.

## 2.3. Data quality: representation and access

The most frequently mentioned DQ dimensions in the representation and access DQ categories are representationalconsistency, easily-understandable, accessibility and security. The representational-consistency and easily-understandable DQ dimensions assess the representation and understandability of data, respectively. Typical issues, such as using different currencies, different formats and different names for similar columns or rows, are addressed by the representational-consistency DQ dimension. Conversely, the latter two DQ dimensions assess the easiness of accessing data and its security, respectively. The accessibility DQ dimension, for example, deals with the request and delivery time of the output. For example, data can be classified as inaccessible if the gap between input and delivery time of output is too large [40].

## 2.4. DQ assessment

The level of DQ can be assessed using a questionnaire or metrics. Lee et al. [22] developed a methodology to assess DQ level using questionnaires. This methodology is called ‘A Methodology for Information Quality Assessment’ (AIMQ). The foundation of this methodology is a 2 - 2 table, called the PSP/IQ model, that classifies DQ dimensions according to their importance from both the user’s and the manager’s perspectives. The axes of the table are conformity to specifications and conformity to user expectations. Accordingly, four DQ categories are distinguished (sound, dependable, useful and usable), and the DQ dimensions identified in Wang and Strong’s framework [46] are classified according to these categories. The sound DQ category relates to the intrinsic value of DQ and, in particular, addresses DQ dimensions such as lack of errors (accuracy), concise representation and completeness. The useful DQ category deals with the contextdependent nature of DQ. This category includes aspects such as appropriate amount, relevancy, interpretability and understandability of the information. The dependable DQ category revolves around the timeliness and security of data, while the usable DQ category is concerned with the accessibility, the reputation and the believability of the data. The PSP/IQ model is used to aggregate scores of the DQ dimensions. Therefore, two gap analysis techniques (IQ benchmark and role gap) are used to analyze the results from this model. IQ benchmark gap analysis is compared with the best performing organizations for the four DQ categories. The role gap technique is used to investigate the differences in the DQ level assessment among different roles in the organizations. For example, DQ assessments performed by information professionals and data users are compared.

Table 3  
DQ metrics from literature conotations for task independent metrics: f denotes ‘function of’ $\mathrm { Q _ { c u r r } } \mathrm { : }$ : is the currency level of the data, A is an attribute, W is an attribute value, age refers to the difference between the moment when DQ is assessed and the moment of data acquisition and decline refers to the average decline rate of the shelf life of attribute values of the attribute under consideration. Conotations for task dependent metrics: currency = (delivery time  input time) þ age, volatility refers to the length of time over which the data remains valid, delivery time refers to the time at which the data was delivered to the user, input time refers to the time at which the data was received by the system, age refers to the age of the data when it was first received by the system and the exponent s is task dependent and used to control the sensitivity of timeliness.

<table><tr><td>DQ dimension</td><td>DQ metric</td><td></td><td>Ref.</td></tr><tr><td rowspan="2">Accuracy</td><td rowspan="2">Task independent $1 - \frac{\text{Number of data units inerror}}{\text{Total number of data units}}$  $f$  (accuracy percentage; L-Z randomness measurement; probability distribution)Bayesian Network Approach</td><td rowspan="2">Task dependent</td><td>[21,31]</td></tr><tr><td>[12][37]</td></tr><tr><td>Appropriate amount</td><td> $\min(\frac{\text{Number of data units provided}}{\text{Number of data units needed}}; \frac{\text{Number of data units needed}}{\text{Number of data units provided}})$ </td><td></td><td>[21,31]</td></tr><tr><td>Timeliness</td><td> $Q_{\text{curr}} = e^{-\text{decline}(A) \cdot \text{age}(W:A)}$ </td><td> $\max(1 - \frac{\text{currency}}{\text{volatility}}, 0)^s$ </td><td>[21,31]</td></tr></table>

Conversely, DQ metrics are being developed to assess the DQ level in organizations. Table 3 shows a number of exemplary DQ metrics proposed by different authors. Pipino et al. [30] developed DQ metrics based on three functional forms, such as simple ratio, min/max operation, and weighted average. The simple ratio is used to create DQ metrics for the accuracy, completeness and consistency DQ dimensions. The metric for the accuracy DQ dimension is given in Table 3. Metrics for the completeness and consistency DQ dimensions are defined analogously. Conversely, metrics for the believability, the appropriate-amount, the timeliness and the accessibility DQ dimensions are developed using min/ max operations. Metrics quantifying the appropriate-amount and the timeliness DQ dimensions are given in Table 3 as examples. The appropriate-amount metric is based on the most recognized definition, which is, namely, that there should be neither too few or too many data [3]. Conversely, a metric for the timeliness DQ dimension is defined as the maximum of one minus the ratio of the currency and the volatility and 0 [21], see Table 3.

More recently, Fisher et al. [12] proposed an accuracy metric by changing the simple ratio scale to a vector approach that includes percentages, a randomness measure, and a probability distribution. The metric combines a simple ratio, which is the ratio of the number of cells in error to the total number of cells, with a randomness measure computed using the Lempel–Ziv complexity measure algorithm.<sup>2</sup> This algorithm is used to differentiate whether the errors in a database are random or systematic in nature. Once the randomness of the errors is determined, a probability distribution is used to help address various managerial questions. The metric is based on the assumption that the value corresponds to the possible validity range.

Similarly, Sessions and Valtorta [36] suggested a measuring approach for accuracy using Bayesian networks.<sup>3</sup>

The metrics discussed earlier are task independent. However, a task-dependent metric is formulated for currency, which is one aspect of the timeliness DQ dimension, by Heinrich and Klier [17], as shown in Table 3. This metric is based on the quality of conformance, which is primarily related to data values and more independent of a particular user’s demand in a specific business situation. The metric is defined as the probability that an attribute value stored in a database still corresponds to the current state of its real world counterpart at the moment when the DQ level is assessed. This metric depends on the context in which it will be applied. If the timeliness dimension is not critical to the task at hand, then a more relaxed sensitivity measure can be applied. Conversely, if the dimension is very critical, a conservative sensitivity measure is suggested.

Many metrics are being developed by different DQ researchers and organizations to assess the DQ level in organizations using the DQ dimensions. Many of the dimensions are multivariate in nature; the variables/components of the metrics that are important to the organization must be clearly identified and defined. Choosing the specific variables or components to measure can be much more difficult than defining the general metric, which is often reduced to a ratio form. Although it may fall within a specific dimensional category, the measure to assess a specific dimension will vary from organization to organization [21]. Therefore, though a comparison of the objective and subjective assessment of the DQ level may indicate the actual DQ level and define the gap between objective and subjective DQ level assessments, the focus of this paper is only DQ assessment using a questionnaire.

## 2.5. DQ challenges

As more data are collected and maintained, the risk of poor DQ increases. Multiple data sources, subjective judgment in data production, security/accessibility trade-off, and changing data needs are often cited challenges [21]. For example, multiple sources of the same data produce different values for that data. For instance, similar accounting data held in different files are very likely to differ from each other, as updating or changing all the files at the same time is not always possible. This is also illustrated by the tendency of system designers to avoid having similar data in different files or, in other cases, to enforce transactional consistency among replicated data. Similarly, using several different processes is also likely to produce different values for the same information [24]. Like multiple sources of data, subjective judgment of data is also a challenge for DQ. Information production using subjective judgment often produces biased information. Data stored in an organization’s database is considered to be a set of facts. However, the process by which these ‘facts’ are collected may involve subjective judgments. For example, the expense codes assigned to indicate different allowances paid to employees by an accountant can be biased by the accountant’s knowledge. The security/accessibility trade-off is also a challenge for DQ. Easy access to information may conflict with requirements for security, privacy, and confidentiality. For data consumers, high-quality data must be easily accessible. However, ensuring privacy, confidentiality, and security of information requires barriers to access. The other most recognized challenge is changing data needs. As information consumers’ tasks and the organizational environment change, the data that used to be relevant and useful may become obsolete [3].

![](/api/attachments/D2AKQUSF/fulltext/images/8479c03e58a1a43cf1f0b57d7688d849cb6361c0304a64af9246fd3b66d797ae.jpg)  
Fig. 3. Different data inputting and manipulating processes, adopted from Maydanchik [24].

In fact, DQ improvement actions require the identification of the causes of data errors and their permanent elimination through an observation of the whole process where data are involved [3,4,24]. Data are impacted by many processes, most of which affect their quality to a certain degree. Fig. 3 shows different data inputting and manipulation processes as identified by Maydanchik [24]. Measuring the impacts of data inputting and manipulation processes on DQ is necessary for proper DQ-improving activities. In this paper, we identify different DQ challenges and their main causes in financial institutions.

## 3. Research methodology

The research methodology is developed alongside four research aims. Fig. 4 shows the four aims of the study.

## 3.1. Research aims

Data of sufficient quality that are considered appropriate for one task may not be of sufficient quality for another task [41]. Therefore, identifying and defining DQ dimensions that are relevant to assess the DQ of one specific task is a recognized approach [53,5]. Therefore, the first aim of this paper is to identify the most important and relevant DQ dimensions for the credit risk assessment task to assess the DQ level.

![](/api/attachments/D2AKQUSF/fulltext/images/7ecb2f7fbcfa2f5b106b8b0e12c60d58563258cf27c69e898bf0c1bf45fef975.jpg)  
Fig. 4. The aims of the study.

As we discussed in Sections 2.1 and 2.2, the task type (simple or complex) and the user experience (beginner or domain expert) are found to have an impact on the DQ assessment [4]. Therefore, these two factors are controlled in this study. The study subjects have similar experience with respect to the credit risk assessment task. However, the impact of various DQ enhancing activities, such as the implementation of DQ teams and the impact of the size of the financial institutions on DQ assessment by the decision makers, remains, to the best of our knowledge, unexplored until now. Therefore, taking these aspects into account, the second aim of this paper is to test whether the importance of the DQ dimensions in Table 2 differs depending on the existence of DQ teams, the size of financial institutions and the differences between financial institutions and other companies.

Assessing the DQ level is a crucial step for DQ improvement actions because it indicates the DQ problem areas [22]. Therefore, the third aim of this paper is to assess the DQ level of credit risk databases by considering the degree of importance of each of the DQ dimensions identified in the first aim of the study. Assessing the DQ level using the most important DQ dimensions helps to identify the most critical DQ problem areas. Additionally, this assessment indicates potential DQ improvement actions.

Finally, the common DQ challenges and their causes, the DQ improving activities and the motivation for DQ improvement activities in the context of credit risk assessment are investigated. Identifying frequent DQ challenges and sources of these challenges leads to sustainable DQ improvement actions because DQ problems can be mitigated from their source.

## 3.2. Empirical study

The data for this empirical study are collected in the form of a survey taken from financial institutions worldwide. The advantage of adopting an empirical approach is that it captures task specific user requirements [46]. Furthermore, it may reveal characteristics that researchers have not defined as part of a general DQ definition.

## 3.2.1. Pilot study

To verify the setup and the clarity of the questions/items in the survey, a pilot study was conducted. The pilot and final study questionnaires are based on Lee et al. [21] and Wang et al. [46]. The pilot study, which has 21 questions (see Appendix A), was organized using an online survey tool. The link to the pilot study questionnaire was sent to three respondents (two males and one female), who can be considered experts in this research area. The respondents’ minimum educational level is a master’s degree, and they have all previously participated in data governance activities. Overall, they have 6–10 years of managerial experience in the risk department of financial institutions. They took an average answer time of 30 min to complete the questionnaire.

The pilot study also helped to identify DQ dimensions important to the credit risk assessment task but not shown in Wang and Strong’s IQ framework [46]. Subjects were asked to list as many DQ dimensions as they found relevant for their task in addition to the given framework (see Question 1, 2 and 3 of part I). As a result, ‘actionable’, ‘alignment’ and ‘traceability’ DQ dimensions were identified. The categories and definitions of these three dimensions were also determined by the subjects (see Table 2). These three DQ dimensions are included in the full study.

Actionable means that data do not require additional manipulation and are readily usable. This dimension is related to the ‘relevant’ dimension in the sense that the former is dependent on the latter; the actionability of the data should be investigated once its relevancy is established.

The alignment DQ dimension is defined as ‘the extent to which data are well-matched or compatible’. If two similar data elements from different data sources contain similar attributes, it may very well be that the data elements are still very differently structured and/or formatted. If, despite these differences, it is possible to integrate both data elements, these elements are said to be reconcilable or compatible.

Traceability refers to the extent to which data are traceable to their sources.

The pilot study provided feedback as to the usability and the clarity of the study instruments and the clarity and consistency of the procedures.

## 3.2.2. Final study

3.2.2.1. Participants. Among a set of 500 financial institutions worldwide that was determined by multiple business experts, a random subset of 150 financial institutions was selected. The study subjects are managers of the credit risk department who are responsible for developing or assessing credit risk models. The majority of subjects (48%) have more than 10 years of working experience, and most of them (64%) worked at the company where the survey was conducted for at least 1 to 5 years. Using a Friedman test at $\alpha = 5 \%$ , it was verified that no statistically significant differences exist across experience groups.

3.2.2.2. Study design and procedures. The survey was organized into two different sessions and consisted of three separate parts. The first session, which consisted of the first and second part of the survey, was sent to a sample group of 150 financial institutions. In the first part, the importance of the DQ dimensions defined in

Table 2 was measured. Subjects were provided with Table 2 and were asked to rate the importance of the DQ dimensions listed on a scale from 0 to 10 for their task (credit risk assessment), where 0 was not important at all, 5 was somewhat important and 10 indicated high importance. In the second part of the survey, subjects were asked to assess the DQ level of their own data using the same scale (0–10). They were provided with different controlling questions/items of the same DQ dimension. For example, they are asked to indicate the extent to which two analogue statements apply to their data, e.g., ‘the data are error free’ and ‘the data are accurate’. Two or three questions for each DQ dimension, totaling 31 questions, were asked. Of the 150 questionnaires mailed to financial institutions, 64 (an effective response rate of 42.67%) were returned. Similarly, of the 150 questionnaires mailed to organizations in other sectors, 30 (an effective response rate of 20%) were returned.

Next, during a follow up session, the third part of the survey was sent to those who replied in the first session. Note that this second session was also organized in the same time frame as the first session and was only conducted in financial institutions. As a result, among the 64 respondents in the first session, only 37 also participated in the second session. In the third part of the survey, the respondents were asked 6 questions to identify recurring DQ problems and their magnitude,the motivation forDQ initiatives in their departmentand if there are any DQ improving activities in place.

## 3.3. Statistical analysis

To test the significance of the obtained results, a number of statistical tests were applied according to the literature. Each of the different tests was assessed at a significance level of 5% unless stated otherwise. The following notation is adopted throughout the remainder of this paper. Financial institutions are denoted by $i = 1 \dots N ,$ , while DQ dimensions are denoted as $j = 1 \ldots P .$ N and P indicate the total number of financial institutions and DQ dimensions, respectively. $d _ { j }$ is used to indicate the jth DQ dimension.

When items are used to form a scale, they need to have internal consistency. Items measuring the same aspects should be correlated with one another. A useful coefficient for assessing the internal consistency is Cronbach’s alpha: $\alpha _ { c }$ [35]. This measure is defined as

$$
\alpha_ {c} = \frac {K}{K - 1} \left(1 - \frac {\sum s _ {l} ^ {2}}{s _ {T} ^ {2}}\right)
$$

where K is the number of items/questions under one DQ dimension, $s _ { l } ^ { 2 }$ is the variance of the lth item, and $s _ { T } ^ { 2 }$ is the variance of the total score formed by summing all the items. The reliability of the study instruments is confirmed as $\alpha _ { c }$ and was found to be 0.82 or greater for each dimension.

Before adopting specific statistical tests, the underlying assumptions made by these tests should be fulfilled. Parametric tests, such as Analysis Of Variance (ANOVA) and t-tests, assume that the data are normally distributed and IID (Independently and Identically Distributed) [16]. A Jarque–Bera test was adopted to verify the normality of the data. The Jarque–Bera test is a twosided, goodness-of-fit test used to verify the null hypothesis that the data come from a normal distribution with unknown variance and mean. It has an asymptotic $\chi ^ { 2 }$ distribution with 2 degrees of freedom. The test statistic takes the following form:

$$
J B = \frac {N}{6} \left(s ^ {2} + \frac {(k - 3) ^ {2}}{4}\right)
$$

where N represents the sample size, s represents the sample skewness, and k represents the sample kurtosis.

As the null hypothesis of normality was rejected for ten out of seventeen DQ dimensions at $\alpha = 5 \% ,$ we used non-parametric tests in the remainder of the analysis.

To compare the survey results across DQ dimensions, a Friedman test was adopted, which is a non-parametric equivalent to the well known ANOVA test [13]. This test detects differences across all DQ dimensions and is defined as

$$
\chi_ {F} ^ {2} = \frac {1 2 N}{P (P + 1)} \left[ \sum_ {j = 1} ^ {P} A R _ {j} ^ {2} - \frac {P (P + 1) ^ {2}}{4} \right]
$$

where $A R _ { j }$ is the average rank of the jth DQ dimension for N financial institutions. Under the null hypothesis, the Friedman test statistic is $\chi _ { F } ^ { 2 }$ distributed with $P - 1$ degrees of freedom, at least when N and P are large enough $( N > 1 0$ and $P > 5 )$ . In this survey, N = 64, and $P = 1 7$

Next, because the assumption of equality between all DQ dimensions is rejected, we proceed with a post-hoc Bonferroni– Dunn test. The Bonferroni–Dunn test is a non-parametric alternative to the Tukey test and compares the DQ dimensions with the dimension associated with the greatest average rank (AR). The difference between two dimensions is found to be significant if the corresponding average ranks (ARs) differ by at least the critical difference:

$$
C D = q _ {\alpha} \sqrt {\frac {P (P + 1)}{6 N}}
$$

where $q _ { \alpha }$ is drawn from a studentized range statistic divided by ${ \sqrt { 2 } } .$ . This test also incorporates an additional Bonferroni correction by dividing the confidence level a by the number of comparisons made, $P - 1$ , to control for family-wise testing, which resulted in a stronger test.

In the case of comparing the sample median between two groups, a (non-parametric) Wilcoxon ranked sum test was used. This test hypothesizes that the data comes from two unknown distributions with equal medians [50]. All statistical tests were implemented in Matlab.<sup>4</sup>

## 4. Results and discussion

In this section, we present and discuss the key findings of the study. In Section 4.1, we present the results of the statistical analysis, which define and identify the most important DQ dimensions for the credit risk assessment task. In Section 4.2, we discuss the DQ level assessment by using the outputs of Section 4.1. Finally, the results of Section 4.3 explain the key DQ challenges, the key causes of DQ problems and the motivations of DQ enhancing activities in financial institutions.

## 4.1. Aim 1: Importance of DQ dimensions

Our first research aim is addressed by analyzing the first part of the survey where the respondents were asked to rate the importance of each of the DQ dimensions given in Table 2. The overall results are presented in Table 4. All seventeen DQ dimensions in Table 2 received a score greater than 7/10, which indicates the importance of each dimension for credit risk assessment. The results in Table 4 are further analyzed by first performing a Friedman test, which detects whether there are statistically significant differences between the scores of all DQ dimensions. The null hypothesis is strongly rejected (p value <

## Table 4

Basic statistical description of DQ dimensions (mean, standard deviation (SD) and confidence interval (C.I.))

<table><tr><td>DQ dimension</td><td>Mean</td><td>SD</td><td>95% C.I.</td></tr><tr><td>Accuracy(AC)</td><td>9.08</td><td>1.54</td><td>8.69–9.46</td></tr><tr><td>0.95 Actionable(ACT)</td><td>8.53</td><td>1.63</td><td>8.12–8.94</td></tr><tr><td>Relevancy(REL)</td><td>8.52</td><td>1.53</td><td>8.13–8.9</td></tr><tr><td>0.95 Security(SEC)</td><td>8.47</td><td>2.08</td><td>7.95–8.99</td></tr><tr><td>Accessibility(ACC)</td><td>8.41</td><td>1.61</td><td>8.00–8.81</td></tr><tr><td>0.95 Timeliness(TIM)</td><td>8.28</td><td>1.79</td><td>7.83–8.73</td></tr><tr><td>Value-added(VAD)</td><td>8.27</td><td>1.94</td><td>7.78–8.75</td></tr><tr><td>0.95 Objectivity(OBJ)</td><td>8.19</td><td>2.20</td><td>7.64–8.74</td></tr><tr><td>Representational-consistent(RC)</td><td>8.13</td><td>2.22</td><td>7.57–8.68</td></tr><tr><td>0.95 Completeness(COM)</td><td>8.02</td><td>2.31</td><td>7.44–8.59</td></tr><tr><td>Reputability(REP)</td><td>7.89</td><td>1.88</td><td>7.42–8.36</td></tr><tr><td>0.95 Interpretability(INT)</td><td>7.86</td><td>2.05</td><td>7.35–8.37</td></tr><tr><td>Appropriate-amount(APM)</td><td>7.84</td><td>1.86</td><td>7.38–8.31</td></tr><tr><td>0.95 Easily-understandable(EU)</td><td>7.81</td><td>1.93</td><td>7.33–8.30</td></tr><tr><td>Alignment(AL)</td><td>7.75</td><td>2.05</td><td>7.24–8.26</td></tr><tr><td>0.95 Traceability(TRA)</td><td>7.73</td><td>2.23</td><td>7.18–8.29</td></tr><tr><td>Concisely-Represented(CR)</td><td>7.36</td><td>2.21</td><td>6.81–7.91</td></tr></table>

![](/api/attachments/D2AKQUSF/fulltext/images/6fd25b7000e3816d364e101cd0a30530e2624d4bbe117f18e46133ffdac2e62b.jpg)  
Fig. 5. Bonferroni–Dunn plot of the relative importance of the DQ dimensions for financial institutions

0.001) indicating significant differences exist in the results of the survey. Therefore, we proceeded with a Bonferroni–Dunn test. The results of the Bonferroni–Dunn test are depicted in Fig. 5. The xaxis in this figure corresponds to the average rank (AR) for each of the DQ dimensions. The DQ dimensions are represented by a horizontal line; the further this line is situated to the right, the greater the score is of the specific DQ dimension. The right end of this line depicts the average ranking, while the length of the line corresponds to the critical distance. If the difference in the average ranking between a DQ dimension and the ‘best’ DQ dimension is more than this critical distance, the difference is significant at a 99% confidence level. The ‘best’ DQ dimension is a DQ dimension that has the greatest average ranking. The dotted, dashed and full vertical lines in the figure indicate the critical difference at a 90%, 95% and 99% confidence level, respectively. The scores of a DQ dimension are significantly less than those of the ‘best’ dimension if the DQ dimension is located on the left hand side of the vertical line.

Accuracy clearly resulted in the greatest score as it is the most right-positioned DQ dimension, as shown in the results of the Bonferroni–Dunn test in Fig. 5, and consequently, accuracy is confirmed to be the most important DQ dimension. Because accuracy is found to be the best scoring dimension, it is used to compare the average scores of each of the other sixteen DQ dimensions. The scores for security, relevancy, actionability, accessibility, objectivity, timeliness, value-added

## Table 5

![](/api/attachments/D2AKQUSF/fulltext/images/a7c90cbaea5aed82e3e16496bda2e7bb8bbf10eccfe8911cc9e3f5c09d99065b.jpg)  
Fig. 6. Bonferroni–Dunn plot of the relative importance of the DQ dimensions as assessed by other sectors.

![](/api/attachments/D2AKQUSF/fulltext/images/18dcb3b643c25b5e4a956fb7c642fcff6a78abb597b916b89633da7f1a696c48.jpg)  
Fig. 7. The results of the Wilcoxon ranked sum test, comparing the medians of the DQ dimensions for financial institutions with and without DQ teams; p values are indicated between brackets.

and representational-consistency are not found to be significantly different at a 99% confidence level. Based on these results, we can conclude that accuracy and those dimensions with a less significant AR are the most important DQ dimensions for assessing the DQ level for the credit risk assessment task. Conversely, the completeness, interpretability, reputability, traceability, easilyunderstandable, appropriate-amount, alignment and conciserepresentation DQ dimensions are found to be significantly less important (see Fig. 5).

A Bonferroni–Dunn test was also performed on the other sector data, and the results are depicted in Fig. 6. These sectors include telecommunication, retail, food, pharmaceutical, chemical and health care industries. From the results shown in Fig. 6, we can see that all the DQ dimensions are suggested to be very important, unlike in the financial sector. Additionally, the relative importance of the DQ dimensions are very different compared to Fig. 5. For the financial sector, accuracy is the crucial DQ dimension, while in the other sectors, appropriate-amount is found to be the most important DQ dimension. However, none of the 16 other dimensions are significantly less important. In general, we established that there is a difference between the DQ assessment in the financial sector and other sectors. This result confirms that DQ depends on the context of the intended use [29,5].

Finally, a non-parametric Wilcoxon signed-rank test was performed to test whether there is a difference in the relative importance of the DQ dimensions between financial institutions with and without DQ teams, as well as between large and small and medium (SME) financial institutions. The results are shown in Fig. 7 and Fig. 8. Both figures (Fig. 7 and 8) show that there are no significant differences in the relative importance of DQ dimensions between financial institutions with and without DQ teams and between large and SME financial institutions, respectively. This result confirms that DQ depends greatly on the characteristics of the task [52]. Therefore, we can conclude that the results in Fig. 5 are applicable to all financial institutions irrespective of the presence or absence of DQ teams and the size of the financial institution.

![](/api/attachments/D2AKQUSF/fulltext/images/9865944c5f89eaabcc349e5428801ae8bd6ab6295972485f04e1bce99f623f90.jpg)  
Fig. 8. The results of the Wilcoxon ranked sum test, comparing the medians of the DQ dimensions for large and SME financial institutions; p values are indicated between brackets.

For the financial institutions’ data, the correlation between the DQ dimensions is also investigated using the Spearman’s rank correlation, $\rho .$ This is a non-parametric correlation measure that investigates the monotonic relationship between any two DQ dimensions. $\rho$ is defined as

$$
\rho = 1 - \frac {6 \sum_ {i = 1} ^ {N} r _ {i} ^ {2}}{N (N ^ {2} - 1)}
$$

where N is the sample size and r the difference between the ordinal ranks assigned to each of the observations. The significance of the Spearman’s rank correlation measure is given in Table 5.

![](/api/attachments/D2AKQUSF/fulltext/images/21696f5292270f47e005a900046be96272f6b099496c893ca72f4f66ed89decf.jpg)

These results show that most of the DQ dimensions are correlated with each other. The black and grey cells show the significance of the correlation between the DQ dimensions at a 99% and 95% confidence level, respectively, while the white cell indicates no correlation between two DQ dimensions.

As the results in Table 5 indicate, the majority of the DQ dimensions are positively correlated with each other. Accuracy is correlated with the majority of the other DQ dimensions, which clearly illustrates the business analyst’s tendency to equate accuracy with the total DQ requirements. In fact, the problem of inaccuracy can be related to many of the DQ dimensions. For example, a null value for the age of a customer can be both associated to the completeness and accuracy DQ dimensions. Accuracy can also relate to the representational-consistency DQ dimension. For example, a birthdate value of a person represented in DDMMYY and MMDDYY format can indicate both inaccuracy and inconsistency problems. Easily-understandable, interpretability and actionability DQ dimensions are also highly correlated to each other. As a rule of thumb, a person that understands the data is able to interpret the data. Likewise, if a decision maker understands the data, it is more likely that he/she will use the data, thereby enhancing the data’s actionability.

![](/api/attachments/D2AKQUSF/fulltext/images/eb89a37368abc5a79794e476a5864a9b2f2eba5b2bc7351521cef2656852f503.jpg)  
(a) x distribution of DQ levels for the intrinsic DQ category

The strong positive correlation observed in the results shown in Table 5 are also supported by the literature. Lee et al. also found a strong correlation between a number of DQ dimensions. These authors reported a significant correlation at a 95% confidence level between the accessibility DQ dimension and the appropriateamount, believability, completeness, concise-representation, consistent-representation, free-of-error, interpretability, relevance, reputation, security, timeliness and easily-understandable DQ dimensions [22]. Therefore, it can be concluded that action to improve one DQ dimension will have a positive effect on the other DQ dimensions.

## 4.2. Aim 2: Scorecard index

The second research aim of the study is investigated by analyzing the second part of the survey where the DQ levels of credit risk databases are assessed using the DQ dimensions in Table 2. For this analysis, we aggregated the DQ dimensions into Wang and Strong’s DQ categories [46]. The value of each DQ category is computed as the weighted average of the values of its constituting DQ dimensions using their degrees of importance. The degree of importance of each DQ dimension is assessed in the first phase of the study. The weights (), which indicate the degrees of importance, are computed using the average ranks () shown in Fig. 5. A simple-average model was also investigated. However, the equal weight of 0.25 for each of the four DQ categories is different from the range of weights (0.183–0.366) computed. Therefore, we only used the weighted average model in our analysis. The weighted average distribution of the DQ level for each DQ category for each financial institution is given in Fig. 9. In line with the previously introduced notation, let $d _ { i j }$ be the score attributed by the ith financial institutions to the jth DQ dimension. Then, in the rest of the analysis, we use $\overline { { x } } _ { i } , \overline { { x } }$ and s to indicate the weighted average for individual financial institution i, the sector weighted average and the sector standard deviation, respectively. We calculate ${ \overline { { x } } } _ { i } ,$ x and s for each of the four DQ categories. The weight for each DQ dimension is computed as

![](/api/attachments/D2AKQUSF/fulltext/images/bc5721da7985ec60b9f4579a01c95d90d69775ab286d5a4f408e68ef5cf6bca8.jpg)

![](/api/attachments/D2AKQUSF/fulltext/images/7978dfa48f77658f7e3f9579bd3c96d6e79d1148e35a681f0cf9fc0f43fd56ca.jpg)  
(b) x distribution of DQ levels for the contextual DQ category

(c) x distribution of DQ levels for the representation DQ category  
![](/api/attachments/D2AKQUSF/fulltext/images/e5d142c5e2937ac3ad27c49c11b82a63bbc98639985266c78c97bb63afa3a9b8.jpg)  
(d) x distribution of DQ levels for the accessibility DQ category  
Fig. 9. DQ levels for the financial institutions for the four DQ categories.

$$
w _ {j} = \frac {A R _ {j}}{\sum_ {j = 1} ^ {P} A R _ {j}}
$$

where $w _ { j }$ is the weight of each DQ dimension as per its degree of importance in assessing the DQ level. $A R _ { j }$ is the average rank of each DQ dimension, as shown in the Bonferroni–Dunn results in Fig. 5. The weighted average is computed as

$$
\overline {{x}} = \frac {1}{N} \sum_ {i = 1} ^ {N} \left[ \frac {\sum_ {j = 1} ^ {P} w _ {j} d _ {i j}}{\sum_ {j = 1} ^ {P} w _ {j}} \right]
$$

where x is the sector weighted average of the DQ level for each DQ category and $d _ { i j }$ is the DQ level score of each DQ dimension from the second part of the survey for each DQ category for each financial institution. The summation across the DQ dimensions is particular for each DQ category. Therefore, the summation only includes the DQ dimensions for a specific DQ category.

The DQ level distribution (Fig. 9) is used to indicate the performance of the sector for the four DQ categories. Therefore, best practices and areas for improvement can easily be identified. Consequently, this result helps an individual financial institution to focus improvement activities. The four categories can be compared to detect common patterns or to focus on the category that needs to be improved the most.

A common concern in organizations is how well they are performing relative to other organizations in the sector. The scorecard index addresses this concern. It is defined as a managerial system that can motivate breakthrough improvements by indicating critical areas, such as product, process, customer, and market development [42]. Additionally, this index is a measurement of products, services, or practices against tough competitors, industry leaders, or other sources or best practices. These best practices form the benchmark against which performance is measured. The scorecard index is used to benchmark the DQ level of an individual financial institution.

The distribution in Fig. 9 provides a method to establish the state of DQ benchmarks. Therefore, financial institutions can assess their DQ level using the best practice institutions in the sector. To identify the best practice institutions, we defined four limits in the distributions. These limits are above upper limit $\left( \overline { { x } } _ { i } > \left( \overline { { x } } + s \right) \right)$ , between the upper limit and the sector weighted average $( { \overline { { x } } } < { \overline { { x } } } _ { i } < ( { \overline { { x } } } + s ) )$ , between the sector weighted average and the lower limit $\left( \left( \overline { { \pmb { x } } } - \pmb { s } \right) < \overline { { \pmb { x } } } _ { i } < \overline { { \pmb { x } } } \right)$ and less than the lower limit $( \overline { { x } } _ { i } < ( \overline { { x } } - s ) ) .$ . If the weighted average for an individual financial institution $\left( \overline { { \boldsymbol { x } } } _ { i } \right)$ falls above the upper limit, between the upper limit and the sector weighted average, between the sector weighted average and the lower limit, or below the lower limit for the specific DQ category, then the DQ level is assessed to be very good, good, below average or worst, respectively. In general, if the DQ level is assessed to be below average, the institution is in a poor DQ state. Therefore, an improvement action should be taken. This is illustrated by an example in the following section.

The columns indicate the mean, the average rank (AR ) and the weight $( w _ { j } )$ from the first part of the study and the DQ level assessment scores $( d _ { f j } )$ of one fictitious financial institution (f) from the second part of the study for each DQ dimension.

<table><tr><td></td><td>DQ dimension</td><td>Mean</td><td> $AR_j$ </td><td> $w_j$ </td><td> $d_{fj}$ </td></tr><tr><td rowspan="3">Intrinsic</td><td>Accuracy(AC)</td><td>9.08</td><td>12.10</td><td>0.079</td><td>3</td></tr><tr><td>Objectivity(OBJ)</td><td>8.19</td><td>9.61</td><td>0.063</td><td>2</td></tr><tr><td>Reputability(REP)</td><td>7.89</td><td>8.02</td><td>0.052</td><td>9</td></tr><tr><td rowspan="6">Contextual</td><td>Completeness(COM)</td><td>8.02</td><td>8.78</td><td>0.057</td><td>8</td></tr><tr><td>Appropriate-amount(APM)</td><td>7.84</td><td>7.71</td><td>0.050</td><td>7</td></tr><tr><td>Value-added(VAD)</td><td>8.27</td><td>9.40</td><td>0.061</td><td>4</td></tr><tr><td>Relevancy(REL)</td><td>8.52</td><td>10.39</td><td>0.068</td><td>7</td></tr><tr><td>Timeliness(TIM)</td><td>8.28</td><td>9.45</td><td>0.062</td><td>3</td></tr><tr><td>Actionable(ACT)</td><td>8.53</td><td>10.37</td><td>0.068</td><td>1</td></tr><tr><td rowspan="5">Representation</td><td>Interpretability(INT)</td><td>7.86</td><td>8.13</td><td>0.053</td><td>8</td></tr><tr><td>Easily-understandable(EU)</td><td>7.81</td><td>7.73</td><td>0.051</td><td>8</td></tr><tr><td>Representational-consistent(RC)</td><td>8.13</td><td>9.21</td><td>0.060</td><td>3</td></tr><tr><td>Concisely-Represented(CR)</td><td>7.36</td><td>6.52</td><td>0.043</td><td>3</td></tr><tr><td>Alignment(AL)</td><td>7.75</td><td>7.51</td><td>0.049</td><td>3</td></tr><tr><td rowspan="3">Access</td><td>Security(SEC)</td><td>8.47</td><td>10.45</td><td>0.068</td><td>3</td></tr><tr><td>Accessibility(ACC)</td><td>8.41</td><td>9.74</td><td>0.064</td><td>3</td></tr><tr><td>Traceability(TRA)</td><td>7.73</td><td>7.88</td><td>0.051</td><td>4</td></tr></table>

Scorecard index for one fictitious financial institution’s DQ level for each DQ category, where x is the weighted average for the DQ level of the institution for each DQ category, x is the sector weighted average and s is the sector standard deviation.

<table><tr><td>Limits</td><td>Color index</td><td colspan="2">DQ scorecard for XYZ</td></tr><tr><td> $\overline{x}_{i} > (\overline{x} + s)$ </td><td></td><td>Intrinsic</td><td>Contextual</td></tr><tr><td> $\overline{x} < \overline{x}_{i} < (\overline{x} + s)$ </td><td></td><td> $\overline{x}_{i} = 4.28$ </td><td> $\overline{x}_{i} = 4.86$ </td></tr><tr><td> $(\overline{x} - s) < \overline{x}_{i} < \overline{x}$ </td><td></td><td>Representation</td><td>Access</td></tr><tr><td> $\overline{x}_{i} < (\overline{x} - s)$ </td><td></td><td> $\overline{x}_{i} = 5.03$ </td><td> $\overline{x}_{i} = 3.28$ </td></tr></table>

Scorecard index illustration The scorecard index is illustrated using a fictitious financial institution. The mean, the average rank $( A R _ { j } )$ and the weight $( w _ { j } )$ from the first part of the study, and the DQ level assessment scores from the second part of the study for each of the DQ dimensions are given in Table 6. The weighted average for each DQ category is computed using the $( w _ { j } )$ and the score, and the results are given in Table 7. The colors of the cells indicate the DQ level of each DQ category. The black, dark grey, light grey and white cells indicate very good, good, below average and worst DQ levels, respectively. The DQ level for the three DQ categories (intrinsic, contextual and access) are categorized as worst, and the DQ level for the representation DQ category is below average for the financial institution. This scorecard allows financial institutions to directly locate potential areas for improvement and guide their improvement actions.

## 4.3. Aims 3 and 4: DQ issues for credit risk management

In this section, the third and fourth research aims of the study are discussed based on the third part of the survey. Note that among the 64 financial institutions, only 37 participated in the third part of the survey. The 37 institutions are, in fact, a subset of the 64 institutions that participated in the first part of the survey. We used a Friedman test to determine if there were significant institutional (size and geographical area) and background (education level and experience) differences between the 37 and 27 institutions and subjects, respectively, at $\alpha = 5 \%$ . The results indicated there were no statistically significant differences, and therefore, the results of this section can also be considered as equally valid as sections 4.1 & 4.2.

![](/api/attachments/D2AKQUSF/fulltext/images/96ecb81a50b27dda5edff1ff27857845cec9d627351ec0e1aafab0aa52e87359.jpg)

(a) Major data quality issues in financial institutions  
![](/api/attachments/D2AKQUSF/fulltext/images/31c846ae39d4cde869b1af89447491485e11b6d2b6522fe5a64b96f4e1cae862.jpg)  
(b) Major Data quality initiative motivations in inancial institutions  
Fig. 10. The major DQ problems and reasons for improvement actions.

## 4.3.1. Different DQ problems and their causes

In this third part, the respondents were asked to indicate the major DQ challenges or problems that they encounter on a daily basis. The results are shown in Fig. 10a. Inconsistency (value and format) and diversity of data sources were indicated by 63% of the respondents as the main recurring DQ challenges. This result indicates that there are many similar data that are maintained in different files. Because these data may not be updated or changed at the same time, it is very likely that the data can be different from each other. As a result, decision makers either must rely on their own DQ assessment to select the data source most suited for their decision tasks or must reconcile the different data sources to obtain one reliable data source. However, we can infer from the results that neither process is easy. In line with the results from Fig. 10a, Cappiello et al. [4] indicated that mismatches among sources of the same data are a common cause of intrinsic DQ concerns. In their study, these authors identified that mismatches among sources of the same data encourage a subjective DQ assessment by the decision makers, which gradually affects the intrinsic or objective DQ dimensions. Initially, data consumers do not know the source to which DQ problems should be attributed; they only know that data are conflicting. These concerns initially appear as believability problems. Over time, data users assess the accuracy of the data by the sources based on experience and personal preferences, which leads to a poor reputation for sources considered inaccurate. Therefore, less reputable sources are viewed as having little added value for the task, which results in reduced use [4,40]. However, these less reputable data sources may be of high quality.

In addition to the inconsistency and diversity of data sources, the results in Fig. 10a show that data collection problems and the high costs associated with these problems are recurring DQ challenges. Data are often produced or maintained by different departments and by different data producers. However, these data are typically also needed by other departments, which are not responsible for the production and maintenance of the data. Although cross departmental data access is typically facilitated by enterprise-wide information systems, collecting all the necessary data is still a common challenge that consumes an important share of decision makers’ time. Another reported DQ related problem in the results shown in Fig. 10a are difficulties when making use of the available data. This is related to the relevancy and timeliness DQ dimensions. Decision makers will discard irrelevant data because they have no added value in a particular context; the decision makers may also opt not to use outdated data. Unfortunately, in many cases, assessing whether data are relevant and/or timely will again consume a fair amount of decision makers’ valuable time.

![](/api/attachments/D2AKQUSF/fulltext/images/2e5342d81c332d2601d378268a58a0d91e48ff3ceee67e27f220d990ef354784.jpg)  
Fig. 11. Different causes of DQ problems in financial institutions.

4.3.1.1. Data processes as causes of DQ problems. The impact of different data-related processes on DQ has been assessed previously [24,21]. The third part of the survey further investigates these processes and quantifies their impact on DQ in financial institutions. The results are shown in Fig. 11. These results indicate that although to a different degree, all data-related processes have caused DQ problems.

Manual data entry processes are predominantly confirmed to be a major DQ problem source. This indicates that despite high automation, a lot of data are manually entered into databases, which induce an increased risk of faults. One example could be confusing the age of two customers or not entering any data at all, which results in inconsistent data. This can create a DQ problem that cannot be easily identified or explained. These different human manual data entry process problems, however, can be mitigated by well-designed data entry processes and accompanying instructions [24].

The system consolidation and the initial data conversion are also confirmed to cause database impurity. The main common problem in system consolidation is data duplication. Previous research also acknowledges that the data in the consolidated systems often overlap [3]. Similarly, when data are transferred from previous/old systems or paper documents to a new system, data may be lost in the process. This is exacerbated by the fact that there is typically no well-recorded metadata [3,24,21]. In addition to the above identified causes of DQ problems, data mutations taking place internally without being captured by the system and losses of expertise are also indicated as common DQ problem causes, as shown in the results in Fig. 11. The changes are known only by those who made the changes, and whenever those employees leave the institution, these changes may be lost. This clearly indicates that a majority of the information that is essential for the appropriate use of the data exists as tacit knowledge rather than in a metadata format. Though very rarely, the respondents also admitted that processes meant to clean impure data in fact caused DQ problems. Wang and Strong [46] reported that every database has impurities; thus, trying to fix one problem may create another problem. This finding warns that to ensure DQ, the effects of all data-related processes need to be taken into account as well.

Table 8  
Cause–effect relationship between DQ problems and different data processes [22].

<table><tr><td></td><td>Processes bringing data from outside</td><td>Processes changing data within</td><td>Processes causing data decay</td></tr><tr><td>Inconsistent data representation</td><td>Large</td><td>Medium</td><td>Small</td></tr><tr><td>Inconsistent copies of data</td><td>Large</td><td>Medium</td><td>Small</td></tr><tr><td>Data collection and its costs</td><td>Large</td><td>Medium</td><td>Small</td></tr><tr><td>Diversity of data sources</td><td>Large</td><td>Medium</td><td>Small</td></tr><tr><td>Making use of the available data</td><td>Small</td><td>Medium</td><td>Large</td></tr></table>

The data processes in Fig. 11 can also be cataloged as processes bringing data from the outside, processes changing data within the company, and processes causing data decay, as seen Fig. 3 [24]. In Table 8, we have summarized the cause– effect relationship between the DQ problems reported in Fig. 10a and the different data processes reported as causes of the problems in Fig. 11. Initial data conversion, system consolidation, manual data entry, batch feeds and real-time interfaces are processes bringing data from the outside into databases and are confirmed to be major causes of most DQ problems reported in a context of credit risk management. Consequently, many DQ problems, such as inaccuracy, incompleteness and inconsistency, can be traced back to these processes. For example, during initial data conversion, the data may not enter into new databases simply because the new databases are not prepared to accept those data. Similarly, the person who manually enters data can make different mistakes, such as entering the wrong data or leaving the cell/column empty where there is supposed to be a value. Likewise, DQ can be impacted by data processing, data cleansing and data purging, which are processes that change data inside the databases. If there is a bug in the program responsible for data processing, this bug can create different DQ problems, such as inaccuracy, inconsistency and incompleteness. Similarly, as there are always DQ problems in databases, data cleansing and purging may impact DQ. For instance, the wrong data in a database can accidentally be cleaned or purged because the data fit the cleansing or purging criteria [21]. Changes not captured, system upgrades, new data uses, loss of expertise and process automation are processes that can cause data decay. Sometimes physical changes that happen in organizations may not be recorded into the systems. For example, a married employee may be recorded as a single. In organizations, there are many daily changes. New production methods can be created, or new methods of sales can be proposed, but the data previously collected may not be useful for these new tasks.

![](/api/attachments/D2AKQUSF/fulltext/images/d9296a7cd053a27a4d150a79f472038ffd9d0cabffd341518c8ceaf2e769c569.jpg)  
Fig. 12. Magnitude of poor DQ problems measured in financial institutions.

## 4.3.2. Magnitude of DQ problems

To properly manage DQ, one should know the challenges and the causes of DQ problems. However, an important step is the ability to measure the DQ of the data stores [22]. In the third part of the survey, the respondents were also asked to indicate the magnitude of the DQ problems. The results in Fig. 12 depict the observed magnitude of poor DQ. More than 10% of the data in credit risk management databases are estimated to be of poor quality. The majority of the institutions estimated that between 10 and 20% of the data is subject to errors. However, 19% of the questioned institutions are unaware of the magnitude of their DQ problems. This result indicates that most financial institutions are still unable to develop comprehensive measures and are unable to assess the magnitude of DQ problems. As a consequence, the impact of the existing poor DQ on the decision tasks is hard to assess as well. However, it is clear that addressing the reported 10–20% of DQ problems may take more than 50% of an employee’s time [18].

Additionally, the inherent difficulty of accurately measuring DQ might discourage any initiative to improve the DQ. This is confirmed by the results shown in Fig. 10b, which indicate that regulatory requirements (e.g., Basel I and II) are cited as the main reason for many DQ enhancing projects. The Basel Accord requires the calculation of detailed loss modeling factors to determine the capital requirement as explained previously. Accurate quantitative modeling of PD, LGD, EaD and M is not only required by this regulation but can become a competitive advantage leading to superior credit performance [2]. However, a competitive advantage is considered to be less important when initiating DQ enhancing activities. Because of these regulatory compliance requirements, financial institutions are organizing DQ teams to improve DQ and cross-functional efforts to improve the comparability and applicability of data sources across different business units. However, such efforts are not yet mature.

Generally, these key findings show that although poor DQ appears to be the norm rather than the exception, DQ is not given much attention in financial institutions.

Every data-related process has an impact on the quality of the data. However, the DQ problem(s) that can be caused by one datarelated process may be very different to the problems induced by other processes. This statement also holds for processes meant to improve data quality.

## 5. Conclusion and future research

This paper explored the important DQ dimensions and assessed the DQ level using a scorecard index. Additionally, this study identified different DQ challenges and their possible causes. In general, this study demonstrated a TDQM effort in a financial setting. In the definition phase, the identification of various DQ dimensions relevant to credit risk assessment is considered. Similarly, in the measurement phase, the DQ level in credit risk databases is assessed, and DQ issues are analyzed. The results of the analysis help to identify the problem areas and to focus improvement actions, which completes the TDQM cycle.

We began with a literature overview of the different DQ dimensions and focused on the framework of Wang and Strong [46]. Based on the results of the pilot survey, this framework was extended with three additional DQ dimensions (i.e., ‘alignment’, ‘actionability’ and ‘traceability’), which resulted in seventeen total DQ dimensions. The importance of this extended framework has been assessed by credit risk managers. These decision makers rated the DQ dimensions on a scale from 0 to 10. The results were analyzed using a Friedman test, which indicated a significant difference between the scores of the DQ dimensions. The results of the post-hoc Bonferroni–Dunn test confirmed that accuracy is the most important DQ dimension. Additionally, security, relevancy, actionability, accessibility, objectivity, timeliness, value-added and representational-consistency are found to be important DQ dimensions. The Wilcoxon ranked sum tests confirmed that the most important DQ dimensions identified are valid irrespective of the size of the financial institution and the presence of DQ teams. A Bonferroni–Dunn test was also performed on data from other sectors. The results indicate that there is a difference between financial and other sectors in assessing the importance of DQ dimensions. This result also confirmed the contextual behavior of DQ. The correlation between DQ dimensions has also been assessed, and the majority of DQ dimensions were found to be correlated, which implies that DQ, although intrinsically a multidimensional concept, is often perceived from a single perspective.

Second, the DQ levels in the credit risk databases are assessed using the weighted average model. The distributions of the weighted average of each DQ category were used to benchmark the DQ level as very good, good, below average and worst. The scorecard index is used to assess the DQ level and to indicate problem areas.

Finally, the paper identified different DQ challenges and their causes in financial institutions. The results indicated that inconsistency and diversity of data sources are among the most recurring challenges. Likewise, manual data entry processes are found to cause the majority of the DQ problems. Although DQ problems are endangering the effectiveness of the task, only a few DQ enhancement activities are currently in place. Moreover, these activities are mostly instigated by regulatory authorities rather than by internal considerations. Surprisingly, creating a competitive advantage was not found to be an important stimulus in any DQ improving activity.

It is confirmed in this paper that the majority of financial institutions are unaware of the magnitude of their DQ problems, which stops them from taking holistic measures to address these issues. This is a clear indication of the need for comprehensive DQ metrics.

Although DQ is contextual and should be addressed with respect to the task at hand, DQ also has intrinsic characteristics that can be valuable to other tasks. Because credit risk assessment involves primarily analytical tasks, DQ requirements and findings of this study can be extended towards different tasks and organizations of a similar nature. The empirical validation of this conjecture is considered to be an interesting topic for future research.

Finally, the sensitivity analysis of the parameters (PD, LGD, EaD and M) performed to understand the possible impact of DQ on risk concentration as well as the relative importance of individual DQ dimensions on these parameters are both considered to be interesting topics for future research.

## Acknowledgement

This research was supported by the Odysseus program (Flemish Government, FWO) under grant G.0915.09.

## Appendix

The questionnaire used in this study is included below. As there is considerable overlap between the pilot and the final study questionnaires, only the final study questionnaire is presented. The questions unique to the pilot study are indicated each time.

## Final study questionnaire

## General questions

1. The sector in which your company operates?—-

2. The country in which your company is?—

3. The primary type of data you are reporting in this questionnaire are? a. Financial or Accounting Data b. Credit Risk Management Data c. Marketing or Sales Data d. Human Resource Data e. Patient, Clinical Data f. Other (Please specify)

4. Your main role relative to these data; do you primarily: a. Collect these data b. Use these data in tasks c. Work as an information systems professional d. Manage those who collect these data e. Manage those who use these data in tasks f. Manage information systems professionals g. Other (Please specify)

5. Your department is: a. Financial, Accounting b. Risk management c. Production, Manufacturing d. Marketing, Sales e. Human Resource f. Information Systems (MIS) g. Legal h. Senior Executive i. Other (Please specify)

6. How long have you worked for this company? a. Less than 1 year b. 1 to 5 years c. 6 to 10 years d. More than 10 years

7. How many years of experience do you have?

8. How long have you held your current job? a. Less than 1 year b. 1 to 5 years c. 6 to 10 years d. More than 10 years

9. What is your current job title?

10. Highest educational level or degree that you hold? a. High school b. College degree c. Graduate Degree d. Other (Please specify) 11. Gender a. Female b. Male

## Part I of the study

1. When you think of data quality, what attributes/dimensions other than accuracy that are necessary for your task come to mind? Please list as many as possible with their meaning?—-(Note: this question was only asked in the pilot study)

2. After reviewing the following list, do any other data quality attributes or dimensions that are necessary for your task come to mind? If so, please list them with their meaning. The definitions of all the listed DQ dimensions are given in Question No.3 (Note: this question was only asked in the pilot study)

 Accuracy, Relevance, Objectivity,

 Reputation, Completeness, Appropriate-amount,

 Value-added, Timeliness, Interpretable,

 Easily-understandable, Representational-consistency,

 Concisely-represented, Accessibility, Security

3 If you are given the following four DQ categories, in which category you will place the newly identified DQ dimensions? (Note: this question was only asked in the pilot study)

a. Access: The extent to which data are available or obtainable.

b. Contextual: The extent to which data are applicable to the task of the data user.

c. Intrinsic: The extent to which data values are in conformance with the actual or true values.

e. Representation: The extent to which data are presented in an intelligible and clear manner.

## 3. How important is it to your task that the data you reported

<table><tr><td></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td colspan="12">accurate: data are certified, error-free, correct, flawless, reliable,</td></tr><tr><td colspan="12">complete: data are not missing and cover the needs of tasks</td></tr><tr><td colspan="12">value-added: data give you a competitive edge, add value to your operations</td></tr><tr><td colspan="12">Timeliness: data are sufficiently up-to-date</td></tr><tr><td colspan="12">Interpretable: data are in appropriate language and symbols and the definitions are clear</td></tr><tr><td>.</td><td colspan="11">.</td></tr><tr><td>.</td><td colspan="11">.</td></tr><tr><td>.</td><td colspan="11">.</td></tr><tr><td colspan="12">Note: the importance rate increases from 0 to 10Note: this question is asked for all DQ dimensions in Table 2</td></tr></table>

## Part II of the study

Part II of the questionnaire includes controlling questions for each DQ dimension. Each DQ dimension has three or four controlling questions. Therefore the consistency of the answers for the controlling questions has been verified using Cronbach’s alpha measure.

## 1. For each statement, indicate the extent to which it is true for the data

```txt
that you reported in Question No. 3 in the General Questions section.
0 1 2 3 4 5 6 7 8 9 10
The sources of these data are possible to trace.
These data are accurate.
Access to these data is sufficiently restricted.
These data are formatted compactly.
The amount of the data is neither too much nor too little.
These data come from good sources.
These data are consistently presented in the same format.
It is easy to interpret what these data mean.
These data are complete.
These data are objectively collected.
.
.
.
Note: 0 is not at all and 10 is completely true
Note: this question is asked for all DQ dimensions in Table 2
```

## Part III of the study

1. Why is data quality a concern for your task?

a. Because of regulatory compliance (e.g., Basel II, Solvency II)

b. Because data quality is becoming a bottleneck for my operational analysis

c. Because data quality is becoming a bottleneck for my strategic decisions

d. In order to get a competitive advantage over other competitors e. Other (Please specify)

2. What are the major data quality problems for your data?

a. Getting data consistently represented across business departments

b. Incomplete data

c. Wrong values

d. Diversity of data sources

e. Making use of available data

f. Outdated data

g. Insecurity of the data

h. Inconsistencies between different copies of the same data i. Other (Please specify)

3. What portion of the database where your primary data comes from suffers from data quality problems? a. Less than 5% b. Between 5 and 10% c. Between 10 and 20% d. Greater than 20% e. Not applicable (Specify the reason) f. Other (Please specify)

4. Does your organization have a cross-functional data management effort in place? a. Yes, Please describe the activities of this cross-functional data management effort b. No

5. Do you have a data quality team in your department?

a. Yes, Please specify the activities and the number of employees working on this team

b. No

<table><tr><td colspan="4">of the data quality problems you reported in Question No. 2 from the data processes listed below?</td></tr><tr><td></td><td>Major Cause</td><td>Minor Cause</td><td>NA</td></tr><tr><td>Initial data conversion: Data conversion from a previously existing old system to the new databases.</td><td>-</td><td>-</td><td>-</td></tr><tr><td>System consolidation: Database consolidations after corporate mergers.</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Manual data entry: Entering data into a system manually.</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Batch feeds: Regular data exchange between systems through batch interfaces.</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Real-time interfaces: Data exchanged between the systems through real-time interfaces.</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Data Processing: The change in the programs responsible for regular data processing.</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Data cleansing: Using automated data cleansing rules to make corrections in mass</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Data purging: Deleting old data routinely from the system to make way for more new data.</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Changes not captured: Different organizational changes not captured in the system.</td><td>-</td><td>-</td><td>-</td></tr><tr><td>System upgrades: Systems software are often upgraded every few years.</td><td>-</td><td>-</td><td>-</td></tr><tr><td>New data uses: The data may be good enough for one purpose but inadequate for another.</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Loss of expertise: Much of the data knowledge exists in people&#x27;s minds rather than in metadata documents.</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Process automation: With the progress of technology, more and more tasks are automated.</td><td>-</td><td>-</td><td>-</td></tr></table>

## References

[1] B. Baesens, C. Mues, D. Martens, J. Vanthienen, 50 years of data mining and OR: upcoming trends and challenges, Journal of the Operational Research Society 60, 2009, pp. 16–23.

[2] Basel Committee on Banking Supervision, International convergence of capital measurement and capital standards, Technical report, Bank of international settlements. 2006

[3] C. Batini, M. Scannapieco, Data Quality: Concepts, Methodologies and Techniques New York, Springer, 2006, pp. 20–50.

[4] C. Cappiello, P. Giciaro, B. Pernici, HIQM: a methodology for information quality monitoring, measurement, and improvement, ER Workshops, LNCS 4231, 2006, pp. 339–351.

[5] C.C. Chen, Y.D. Tseng, Quality evaluation of product reviews using an information quality framework, Decision Support Systems 50 (4), 2011, pp. 755–768.

[6] I.N. Chengalur-smith, D.P. Ballou, H.L. Pazer, The impact of data quality information on decision making: an exploratory analysis JEEE Transactions of Knowledge and Data Engineering 11 (6). 1999, pp. 853–864.

[7] P. Cykana, A. Paul, M. Stern, DoD guidelines on data quality management, in: Proceedings of the Conference on Information Quality, Cambridge, MA, 1996, pp. 154–171.

[8] K. Dejaeger, B. Hamers, J. Poelmans, B. Baesens, A novel approach to the evaluation and improvement of data quality in the financial sector, in: Proceedings of the 15th International Conference on Information Quality, Little Rock, USA, 2010.

[9] W.H. Delone, E.R. McLean, Information systems success: the quest for the dependant variables, Information Systems Research 3 (1), 1992, pp. 60–95.

[10] M.J. Eppler, D. Wittig, Conceptualizing information quality: a review of information quality frameworks from the last ten years, in: Proceedings of the 2000 Conference on Information Ouality, 2000

[11] C.W. Fisher, D.P. Ballou, The impact of experience and time on use of data quality information in decision making, Information Systems Research 14 (2), 2003, pp. 170–188.

[12] C.W. Fisher, E.J.M. Lauria, C.C. Matheus, An accuracy metric: percentages, randomness, and probabilities, Journal of Data and Information Quality (JDIQ) 1 (3), 2009, p. 16.

[13] M. Friedman, A comparison of alternative tests of significance for the problem of m rankings, Annals of Mathematical Statistics 11, 1940, pp. 86–92.

[14] M.B. Gordy, A comparative anatomy of credit risk models, Journal of Banking and Finance 24, 2000, pp. 119–149.

[15] H. Hannoun, The Basel III Capital Framework: a decisive breakthrough, Discurso pronunciado en el seminario de alto nivel BoJ-BIS Financial Regulatory Reform:

Implications for Asia and the Pacific, www.bis.org/speeches/sp101125a.pdf 2010.

[16] T. Hastie, R. Tibshirani, J. Friedman, The Elements of Statistical Learning, Data Mining, Inference, and Prediction, Springer, New York, 2001.

[17] B. Heinrich, M. Klier, Assessing data currency a probabilistic approach, Journal of Information Science 37 (1), 2011, p. 86.

[18] H. Interactive, Information workers beware: Your business data can’t be trusted, 2006.

[19] M. Jarke, Y. Vassiliou, Data warehouse quality: a review of the DWQ project, in: Proceedings of the Confrenece on Information Quality, Cambridge, MA, 1997, pp. 299–313.

[20] B.K. Kahn, D.M. Strong, R.Y. Wang, Information quality benchmarks: product and service performance, Communications of the ACM 45 (4), 2002, pp. 184–192.

[21] Y.W. Lee, L.L. Pipino, J.D. Funk, R.Y. Wang, Journey to Data Quality, The MIT Press, London, 2006, pp. 67–108.

[22] Y.W. Lee, D.M. Strong, B.K. Kahn, R.Y. Wang, A methodology for information quality assessment, Information & Management 40, 2002, pp. 133–146.

[23] S. Madnick, H. Zhu, Improving data quality through effective use of data semantics, Data & Knowledge Engineering 59, 2006, pp. 460–475.

[24] A. Maydanchik, Data Quality Assesment, Technics publications, LLC, post office Box 161,Bradley Beach, NJ, 2007, pp. 5–30.

[25] C. Moraga, M.A. Moraga, C. Calero, A. Caro, Towards the discovery of data quality attributes for web portals, ICWE, LNCS 5648, 2009, pp. 251–259.

[26] F. Panse, N. Ritter, Completeness in databases with maybe tuples, ER workshops 20, 2009, pp. 2–211.

[27] A. Parssian, V.S. Jacob, Assessing data quality for information products: impact of selection, projection, and cartesian product, Management Science 50 (7), 2004, pp. 967–982.

[28] J.M. Pearson, C.S. McCahon, R.T. Hightower, Total quality management. Are information systems managers ready? Information & Management 29 (5), 1995, pp. 251–263.

[29] M. Pinto, Data representation factors and dimensions from the quality function deployment (QFD) perspective, Journal of information science 32 (2), 2006, pp. 116-130.

[30] L.L. Pipino, Y.W. Lee, R.Y. Wang, Data quality assessment, Communications of the ACM 45 (4), 2002, pp. 211–218.

[31] R. Price, G. Shanks, The impact of data quality tags on decision-making outcomes and process, Journal of the Association for Information Systems 12 (4), 2011, p. 1.

[32] S. Raghunathan, Impact of information quality and decision-maker quality on decision quality: a theoretical model and simulation analysis, Decision Support Systems 26, 1999, pp. 275–286

[33] E. Rahm, H.H. Do, Data cleaning: problems and current approaches, Bulletin of the IEEEComputerSocietyTechnicalCommitteeonDataEngineering23,2000,pp.3–13.

[34] T.C. Redman, The impact of poor data quality on the typical enterprise, Communications of the ACM 41, 1998, pp. 79–82.

[35] J.R.A. Santos, Cronbach’s alpha: a tool for assessing the reliability of scales, Journal of Extension 37 (2), 1999, pp. 1–5.

[36] V. Sessions, M. Valtorta, Towards a method for data accuracy assessment utilizing a Bayesian network learning algorithm, Journal of Data and Information Quality (JDIQ) 1 (3), 2009, p. 14.

[37] G. Shankaranarayanan, Y. Cai, Supporting data quality management in decisionmaking, Decision Support Systems 42, 2006, pp. 302–317.

[38] G. Shankaranarayanan, B. Zhu, Data quality metadata and decision making, The 45th Hawaii International Conference on System Science, IEEE, 20121434–1443.

[39] G. Shankaranarayanan, M. Ziad, R.Y. Wang, Managing data quality in dynamic decision environments: an information product approach, Journal of Database Management 14 (4), 2003, pp. 14–32.

[40] D.M. Strong, Y.W. Lee, R.Y. Wang, Data quality in context, Communications of the ACM 40 (5), 1997, pp. 103–110.

[41] G.K. Tayi, D.P. Ballou, Examining data quality, Communications of the ACM 41 (2), 1998, pp. 54–57.

[42] T. Van Gestel, B. Baesens, Credit Risk Management, Oxford University Press Inc, New York 2009

[43] Y. Wand, R.Y. Wang, Anchoring data quality dimensions in ontological foundations, Communications of the ACM 39 (11), 1996, pp. 86–95.

[44] R.Y. Wang, A product perspective on data quality management, Communications of the ACM 2, 1998, pp. 58–65.

[45] R.Y. Wang, V.C. Storey, C.P. Firth, A framework for analysis of data quality research, IEEE Transactions on Knowledge and Data Engineering 7 (4), 1995, pp. 623–640.

[46] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4), 1996, pp. 5–34.

[47] J.E. Ware, B. Gandek, Methods for testing data quality, scaling assumptions, and reliability, Journal of Clinical Epidemiology 51 (11), 1998, pp. 945–952.

[48] S. Watts, G. Shankaranarayanan, A. Even, Data quality assessment in context: a cognitive perspective, Decision Support Systems 48, 2009, pp. 202–211.

[49] S. Watts, W. Zhang, Knowledge adoption in online communities of practice, System d’Information et Management 1 (9), 2004, p. 9

[50] F. Wilcoxon, Individual comparisons by ranking methods, Biometrics 1, 1945, pp. 80-83.

[51] C. Zeeh, The Lempel Ziv Algorithm, Technical report, University of Munich, 2003.

[52] H. Zhu, R.Y. Wang, Information quality framework for verifiable intelligence products, Data Engineering 31, 2010, pp. 5–333.

[53] X. Zhu, S. Gauch, Incorporating quality metrics in centralized/distributed information retrieval on the world wide web, in:Proceedings ofthe 3rd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, 2000, pp. 288–295.
