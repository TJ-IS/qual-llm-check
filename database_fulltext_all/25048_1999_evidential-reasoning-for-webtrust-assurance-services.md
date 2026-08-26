---
otero_id: 25048
otero_key: "XY4QTN4B"
title: "Evidential Reasoning for WebTrust Assurance Services"
authors: "Rajendra P. Srivastava; Theodore J. Mock"
year: "1999"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1999.11518254"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evidential Reasoning for WebTrust Assurance Services

Rajendra P. Srivastava & Theodore J. Mock

To cite this article: Rajendra P. Srivastava & Theodore J. Mock (1999) Evidential Reasoning for WebTrust Assurance Services, Journal of Management Information Systems, 16:3, 11-32, DOI: 10.1080/07421222.1999.11518254

To link to this article: http://dx.doi.org/10.1080/07421222.1999.11518254

![](/api/attachments/XY4QTN4B/fulltext/images/70363bedf972410fabc53d71d8e0e5c21b257f2eb9c8ee54ea25d6d1dc8459dd.jpg)

Published online: 02 Dec 2015.

![](/api/attachments/XY4QTN4B/fulltext/images/cc78f269d88c9704b66939429ab603ac40153955263c9d16835004eb293951ae.jpg)

Submit your article to this journal ↗

Article views: 1

![](/api/attachments/XY4QTN4B/fulltext/images/088d61fb4e5beccd55830373c8e56e2d64fdd7a9700cd90c3ef4b3fb05a38922.jpg)

View related articles ↗

# Evidential Reasoning for WebTrust Assurance Services

RAJENDRA P. SRIVASTAVA AND THEODORE J. MOCK

RAJENDRA P. SRIVASTAVA is Ernst & Young Distinguished Professor of Accounting and Director of the Ernst & Young Center for Auditing Research and Advanced Technology at the School of Business, University of Kansas. He holds a Ph.D. in accounting from the University of Oklahoma, Norman, and a Ph.D. in physics from Oregon State University, Corvallis. Dr. Srivastava's publications have appeared in The Accounting Review, Journal of Accounting Research, Auditing: A Journal of Practice and Theory, and International Journal of Intelligent Systems. He received the 1996 Award for Notable Contribution to AI & Expert Systems Research in Accounting from the AI/Expert Systems Section of the American Accounting Association. He is or has been a member of the Editorial and Review Board of several journals, including The Accounting Review and Auditing: A Journal of Practice and Theory.

THEODORE J. MOCK is the Arthur Andersen Alumni Professor of Accounting at the University of Southern California and professor of auditing research at Maastricht University in the Netherlands. His research interests lie primarily in the areas of audit, assurance, and accounting information systems. His AICPA research monograph on internal control evaluation was awarded the American Accounting Association Wildman Award and he was a coauthor of the AICPA monograph on collaborative audit research that received the 1998 Joint AICPA/AAA Collaboration Award. Professor Mock's training includes degrees in mathematics and finance from the Ohio State University and a doctorate in business administration from the University of California at Berkeley. He has held academic appointments at the University of California–Los Angeles, Ohio State University, the Norwegian School of Economics and Business, Bond, Griffiths and Southern Cross Universities in Australia, the University of Otago in New Zealand, Maastricht University in the Netherlands, City University of Hong Kong, and Nanyang Technological University in Singapore. Professor Mock has served in many positions within the American Accounting Association (AAA), including the editorship of Auditing: A Journal of Practice & Theory, AAA Director of Research, and President of the Auditing Section.

ABSTRACT: We study two aspects of assurance services in electronic commerce. The first deals with the type(s) of evidential networks that will allow a professional accountant to provide assurance. Here, we develop an evidential network model for "WebTrust Assurance," a service being provided by the American Institute of Certified Public Accountants (AICPA) and the Canadian Institute of Chartered Accountants (CICA). Our model augments the AICPA/CICA approach and provides goals, subgoals and evidence relevant to the overall assurance to be provided. The aggregation of evidence and the resolution of uncertainties follow the belief-function approach.

Next we develop a decision-theoretic model for the assurance-planning problem. Our approach is based on estimating the expected value of providing various levels of assurance and is illustrated with several different scenarios that may be faced in practice. We also consider the role of ambiguity in decision situations such as planning WebTrust engagements and calculate bounds in expected value based on whether auditors are conservative or not in their approach to risk.

KEY WORDS AND PHRASES: assurance services, decision theory, electronic commerce, risk management, WebTrust.

THE CHALLENGE FOR THE ACADEMIC ARM OF THE AUDITING PROFESSION brought about by the “Third Wave” may not be the effects of information technology itself, but rather the changes brought about by the broadening of professional services into “assurance services.” One such change relating to the provision of assurance services, and of particular interest to this paper, is the provision of WebTrust assurance related to electronic commerce: “According to the AICPA special committee on assurance services, the e-commerce assurance market for CPAs could grow to between \$2 billion and \$11 billion annually over the next few years” (www.aicpa.org/assurance/index.html) [10, p. 32].

The demands for services of this nature are not only growing, $^{1}$ but they relate to critical market impediments. As noted by the Grant Thornton accounting firm [9], “A recent study by the AICPA reveals that security fears prevent 85 percent of consumers from providing their credit card number when shopping on-line.” Allaying such fears is an important contribution that the audit profession may be able to provide.

This article has two main objectives. The first is to develop a conceptual framework for evidential reasoning for the WebTrust assurance services being provided jointly by the AICPA and CICA $[2]$ . WebTrust assurance is one of many types of assurance proposed by the AICPA Special Committee on Assurance Services $[4]$ and involves “assuring that Web sites which offer electronic commerce meet standards of consumer information protection, transaction integrity and sound business practice” (http://www.aicpa.org/webtrust/princrit/htm).

To achieve our first objective, an evidential reasoning model is developed. This model provides a structured approach for collecting, evaluating, and aggregating evidence appropriate to the assertions, objectives, and subobjectives relevant to the WebTrust service. The traditional SAS 47 audit risk model [1] for financial statement audits does not facilitate incorporation of either interrelated evidence or interrelationships among the variables: balance sheet or income statement accounts, assertions, and audit objectives.

The second objective is to develop a decision-theoretic model for determining the optimal level of assurance on important dimensions of the WebTrust assurance service. This approach will enable the assurance provider to obtain sufficient competent evidential matter to achieve an acceptable level of assurance based on a cost-benefit analysis.

One important issue to be researched is the extent to which the evidential reasoning approach for assurance is similar to that of auditing $[23]$ . Clearly, the assurance provider would have a network of variables similar to those used to model an audit. For example, we might need to specify the various assertions related to the assurance service being provided and then specify related objectives and subobjectives. Conceptually, these variables would be connected to each other through various logical relationships. In order to provide assurance, each variable ultimately would need to be connected to one or more items of (sufficient, competent) evidence. In certain situations, one piece of evidence may support more than one variable making the evidential diagram a network.

One issue that needs to be considered is the nature of the WebTrust assurance statement. In auditing, we have many variables and types of evidence leading to an essentially binary output (i.e., an unqualified or qualified opinion). But in WebTrust, we have factors that lead to an n-nary output (an opinion concerning business policies, information security, and transaction integrity). Here, the assertions are at the level of the individual assurance statements. And, as will be evident in the following models, this leads to somewhat different evidential issues than for the traditional audit.

In the present paper, we express the strength of evidence through belief functions $[16]$ . Shafer and Srivastava $[18]$ and Srivastava and Shafer $[24]$ argue that belief functions provide a better framework for representing the strength of evidence than the probability framework. Moreover, Curley and Golden $[4]$ contend “that belief functions offer promise as a language for representing degrees of belief, particularly for capturing degree of justification or support” (p. 298).

We use a computer program called Auditor's Assistant developed by Shafer, Shenoy, and Srivastava [17] to draw the evidential network and aggregate evidence. However, we make no attempt here to measure the strength of evidence.

We take the basic framework developed by the AICPA/CICA and classify their principles and controls into various assertion categories, objectives, and subobjectives. Also, we suggest some audit procedures that would provide items of evidence for corresponding assertions, objectives, and subobjectives. We also generate a new assertion category or principle in AICPA/CICA terminology (Legal Environment) that appears to be important in an international context. $^{2}$ We then provide relevant objectives and subobjectives along with appropriate procedures for collecting evidence.

This article contributes to assurance literature $^{3}$ in two significant ways. First, it is the first research that looks at assurance services, in general, and at WebTrust assurance, in particular, using an evidential reasoning approach. That is, we model how various items of evidence gathered in a given WebTrust engagement for various assurance assertions could be combined to obtain a specified assurance level for the WebTrust service. Second, it is the first study in the auditing, accounting, and information systems literature that introduces the concepts and methods for making decisions using an expected utility theory approach under conditions of ambiguity and the belief-function framework. Also, this study is the first to introduce a decision-theoretic approach of combining risks concerning the various assertions of the assurance service. Since the incremental cost in providing an assurance service depends on the individual risks associated with different assertions, it makes economic sense to combine these risks using a decision-theoretic approach. This approach is different from the traditional audit approach where the risks or assurances are combined without explicit consideration of the expected liability associated with each audit assertion or objective.

## Conceptual Framework for Evidential Reasoning

THE PROPOSED CONCEPTUAL FRAMEWORK FOR EVIDENTIAL REASONING is primarily based on the documentation provided by the AICPA/CICA [2] for WebTrust assurance services. In addition to the three assertion categories $^{4}$ described by the AICPA/CICA, we introduce one other assertion category that should be considered in providing the WebTrust assurance service. The global environment for electronic commerce is the major reason for the additional assertion category. Later in this section we discuss this addition in more detail.

## Four Assertion Categories

Table 1 describes the assertion categories along with the related objectives and subobjectives for WebTrust assurance services. The first column lists the four assertion categories that would need to be considered when providing WebTrust assurance: Business Practice, Transaction Integrity, Information Protection, and Legal Environment. According to the AICPA/CICA, the Business Practice assertion category implies that the entity will perform at some reasonable level of belief for all disclosed business practices. This includes terms and conditions of each transaction, the nature of goods and services provided, any warranty coverage, and information on customer claims. These conditions are expressed as objectives in column two of Table 1. The assurance provider will need to collect sufficient, competent evidence in support of each of these objectives. When there is competent evidence that these objectives have been met, the assertions within the Business Practice category are judged to be met. In some cases, these objectives are further divided into subobjectives that are listed in column three in Table 1. The main objectives are assumed to be related to the corresponding subobjectives through an “and” relationship. This relationship implies that the main objective is met if and only if the corresponding subobjectives are met.

## Evidential Network

We present an evidential diagram in figure 1 for the assertion category Business Practice along with all its objectives and subobjectives. Such an evidential framework provides a structured approach to evaluate all the evidence the assurance provider collects in support of the assertions. The rectangular nodes with rounded corners in figures 1–4 are known as variable nodes in an evidential diagram [24]. These variable nodes represent assertions, objectives, and subobjectives. They have values such as “true” or “false” that the assertion or objective has been met or not met. The rectangular boxes in Figures 1–4 represent evidence nodes. These evidence nodes represent the procedures preformed by the assurance provider. A node with “&” in a circle represents an “and” relationship between the variables to the right of it with the variable on its left. For example, in figure 1, the four objectives to the right of Business Practice are related to it through an “and” node. This relationship implies that the assertion that Business Practice standards have been met would be true if and only if the four objectives have been met.

Table 1. Assertion Categories and Objectives for WebTrust Services

<table><tr><td>Assertion categories</td><td>Objectives</td><td>Subobjectives</td></tr><tr><td rowspan="7">1. Business practice</td><td>1.1. E-commerce terms and conditions are disclosed.</td><td>No subobjective</td></tr><tr><td rowspan="2">1.2. Information concerning nature of goods and services is disclosed.</td><td>1.2.1. Proper disclosure.</td></tr><tr><td>1.2.2. Accurate disclosure.</td></tr><tr><td rowspan="2">1.3. Information concerning warranty, service, and support is disclosed.</td><td>1.3.1. Proper disclosure.</td></tr><tr><td>1.3.2. Accurate disclosure.</td></tr><tr><td rowspan="2">1.4. Information enabling customer claims, questions etc. is disclosed.</td><td>1.4.1. Proper disclosure.</td></tr><tr><td>1.4.2. Accurate disclosure.</td></tr><tr><td rowspan="4">2. Transaction integrity</td><td>2.1. Order accurate and complete</td><td>No subobjective.</td></tr><tr><td>2.2. Order accepted before shipment</td><td>No subobjective.</td></tr><tr><td>2.3. Proper shipping or delivery</td><td>No subobjective.</td></tr><tr><td>2.4. Proper billing</td><td>No subobjective.</td></tr><tr><td rowspan="10">3. Information protection</td><td rowspan="3">3.1. Protection from external access</td><td>3.1.1. Protection from altering files.</td></tr><tr><td>3.1.2. Protection from virus transmission.</td></tr><tr><td>3.1.3. Protection from copying private info.</td></tr><tr><td rowspan="2">3.2. Protection during transmission</td><td>3.2.1. Reliable transmission.</td></tr><tr><td>3.2.2. No interception.</td></tr><tr><td rowspan="2">3.3. Protection from internal misuse</td><td>3.3.1. No unauthorized access to cust. data</td></tr><tr><td>3.3.2. Authorized but no improper use of customer data.</td></tr><tr><td rowspan="3">3.4. Protection from improper use of customer&#x27;s computer and its files</td><td>3.4.1. Protection from altering files.</td></tr><tr><td>3.4.2. Protection from virus transmission</td></tr><tr><td>3.4.3. Protection from copying private info.</td></tr><tr><td rowspan="2">4. Legal environment</td><td>4.1. Compliant with International legal environment.</td><td>No subobjective.</td></tr><tr><td>4.2. Compliant with state and national legal environment.</td><td>No subobjective.</td></tr></table>

![](/api/attachments/XY4QTN4B/fulltext/images/dd1a4182dab372728bc9e1bccc43dbc3bd8947ff6f861d5da96a3ab9fc6d67f9.jpg)  
Figure 1. Evidential Diagram for Business Practice Assurance

![](/api/attachments/XY4QTN4B/fulltext/images/acfc33ff416fd140d3d1b42e61bd4ccec8e2510ab89937db6a84fcf3562bcc14.jpg)  
Figure 2. Evidential Diagram for Transaction Integrity Assurance

In order to determine whether the Business Practice assertion has been met, the assurance provider would perform all the procedures described in rectangular boxes (evidence nodes) in figure 1. Each procedure acts as an item of evidence providing support (or possibly nonsupport or mixed support) to the assertion or objective to which it is connected. Based on the findings on each of the procedures, the assurance provider can estimate the level of support from each item of evidence for the corresponding objectives and subobjectives [24]. The level of support can be expressed in terms of belief functions [18, 23] or some other calculus based on probabilities, fuzzy logic, and the like. We use belief functions $^{5}$ and a computer program Auditor Assistant [17] to aggregate these items of evidence. For the inputs shown in figure 1, the overall belief supporting the assertions related to Business Practice is 0.956.

The first number in a variable node is the level of support or belief in favor of the node and the second number is the level of support or belief for the negation of the node. Auditor Assistant can be used to perform sensitivity analysis on the level of support desired from various items of evidence and the overall belief desired on the node or assertion of interest.

Figure 2 represents an evidential diagram for the assertion category Transaction Integrity. The general assertion is that transactions have been properly processed and it is connected through an “and” node to four objectives: “order accurate and complete,” “order accepted before shipment,” “proper shipping or delivery,” and “proper billing." These objectives are derived from the AICPA/CICA description of Transaction Integrity. In other words, a transaction has integrity only if the customer's order is accurate, complete, accepted, shipped properly, and billed correctly.

![](/api/attachments/XY4QTN4B/fulltext/images/529fa178b93cb526cf53cf84611c62e838e8ec3e7ba1f710c1d3233bf8e1c769.jpg)  
Figure 3. Evidential Diagram for Information Protection Assurance

A possible set of audit procedures is described in the evidence nodes shown in figure 2 for this case. These procedures are not meant to be exhaustive; there could be several other procedures as described in AICPA/CICA document. Our purpose here is to demonstrate how a conceptual framework for evidential reasoning can be developed using assertions, objectives, subobjectives, relationships among the variables, and items of evidence. For the assumed input values for the level of support from each item of evidence in figure 2, the overall belief in Transaction Integrity is 0.983.

Figure 3 represents an evidential diagram for the assertion Information Protection. Information is assessed to be appropriately protected if and only if the following objectives have been met: “protection from external access,” “protection during transmission,” “protection from internal misuse,” and “protection from improper use of customer computers and its files.” As listed in Table 1 and also shown in figure 3, these objectives are further decomposed into subobjectives. For example, the objective “protection during transmission” is met if and only if the subobjectives “reliable transmission” and “no interception” are met. In other words, if the information is protected during transmission by using encryption technology or other techniques, and if the customer information is not stolen during transmission, then the objective “protection during transmission” is met. Again, some suggested procedures are represented through rectangular nodes in figure 3 for this case. For the assumed level of support from various items of evidence in figure 3, we obtain 0.99 level of support for Information Protection. Such a high level of support may be desired by the assurance provider because of high costs of liability if this assertion is not met.

Let us consider another scenario for the Information Protection assertion. Suppose the assurance provider finds that the web site does not have good control over the subobjective “No Unauthorized Access to Customer Data” and expresses a judgment with a level of support, say 0.9, for the negation of the subobjective. Even if the other items of evidence provide the specified levels of positive support to the respective variables as shown in figure 3, the overall belief that the Information Protection assertion is true is only 0.189 with a 0.730 level of belief that it is not true. Although the other objectives and subobjectives have been met with at least 0.98 level of support, the belief that Information Protection is true is now only 0.189. This is because of the “and” relationship between the assertion and its four objectives. The assertion is met if and only if all its objectives are met. Strong negative evidence that leads to a 0.9 level of belief that “No Unauthorized Access to Customer Data” is not met is the reason for the overall belief in support of the objective “Protection from Internal Misuse” to be only 0.189. The overall belief against the objective “Protection from Internal Misuse” is 0.730. This is quite strong belief that the assertion is not met. In such a situation, the assurance provider may decide either to issue a qualified opinion or withdraw from the engagement depending on the cost and benefit analysis of the engagement as presented in the next section.

![](/api/attachments/XY4QTN4B/fulltext/images/8ced6149298d6403f97a0a6109c1b968f084bc16749eaece365bcc94ca85ec5b.jpg)  
Figure 4. Evidential Diagram for "Legal Environment" Assurance

Figure 4 represents the evidential diagrams for the assertion, Legal Environment. This assertion is not discussed in any detail in the AICPA/CICA document. However, we believe that this assertion is important. First, the assertion “Legal Environment” means that the assurance provider must assess whether the entity selling the goods or providing the services is in compliance with the legal requirements of doing business. This would mean that the assurance provider would need to evaluate compliance with the rules and regulations of the state government, federal government, and appropriate international agencies. $^{6}$ Even if the other three assertions (Business Practice, Transaction Integrity, and Information Protection) are fully met, lack of compliance with applicable legal conditions would make the WebTrust assurance certification fallacious and this might result in liability to the assurance provider.

In general, dividing assertions into objectives and subobjectives provides a structured approach for the evidence gathering process to the assurance provider. Although it is an empirical question, a structured approach of identifying and collecting evidence relevant to various objectives and subobjectives of an assertion could make the evaluation of whether the assertions have been met or not met relatively more efficient and effective.

## Decision-Theoretic Approach to WebTrust Services

AS DISCUSSED IN THE PREVIOUS SECTION, IN A WEBTRUST ASSURANCE SERVICE, the assurance provider would accumulate various items of evidence pertaining to the four assertions for planning purposes: Business Practices (B), Transaction Integrity (T), Information Protection (I), and Legal Environment (L). $^{7}$

In order to give unqualified assurance, the assurance provider would like to obtain a target level of belief on each of the four assertions. However, that level may vary for each assertion because of a different loss function associated with each assertion if it is not met. $^{8}$ For example, the assurance provider may give unqualified assurance if he or she is confident with a degree of belief 0.95 that Business Practice is met ( $Bel(b)=0.95$ ), with 0.98 degree of belief that Transaction Integrity is met ( $Bel(t)=0.98$ ), with 0.99 degree of belief that Information Protection is met ( $Bel(i)=0.99$ ), and with 0.95 degree belief that Legal Environment is met ( $Bel(l)=0.95$ ). In the above example, we assume that a rational assurance provider would chose a lower threshold level of belief for an assertion that is assessed as having lower risk.

Strat [25, 26] has developed an approach for making decisions where ambiguity exits. Such a situation is best modeled using belief functions. Under the belief-function framework, uncertainties associated with each state $^{9}$ of nature in a decision problem may not add to one [18]. As a result, there would exist a certain level of ignorance or ambiguity with each state of nature. Under Strat's approach the decision maker would first resolve the ambiguities by redistributing them to various states of nature and then determine the expected value of the payoffs.

Suppose that the assurance provider gives unqualified WebTrust assurance when beliefs on the individual assertions reach the desired threshold values, say, $\operatorname{Bel}(b) = m_{\mathrm{B}}$ , $\operatorname{Bel}(t) = m_{T}$ , $\operatorname{Bel}(i) = m_{I}$ , and $\operatorname{Bel}(l) = m_{L}$ . For simplicity, we assume that the assurance provider has no evidence against the assertions, that is, $\operatorname{Bel}(\sim b) = 0$ , $\operatorname{Bel}(\sim t) = 0$ , $\operatorname{Bel}(\sim i) = 0$ , and $\operatorname{Bel}(\sim l) = 0$ . In general, the above m values would be less than 1. Thus, there would be ambiguity in each assertion as to whether it is met or not.

Ambiguity in a state is measured by the difference between the respective plausibility and belief (see note 5 for details). For example, ambiguity in b or in $\sim b$ is given by $^{10}$

$$
\text { Ambiguity } (b) = \operatorname{Pl} (b) - \operatorname{Bel} (b) = 1 - m _ {B},
$$

$$
\text { Ambiguity } (\sim b) = \operatorname{Pl} (\sim b) - \operatorname{Bel} (\sim b) = 1 - m _ {B}.
$$

In order to use decision theory, one needs to resolve the ambiguity and then determine the expected value of the payoff for the decision. Strat proposes resolving ambiguity through the use of a parameter $\rho (1 \geq \rho \geq 0)$ . A value of $\rho = 0$ means that the decision maker is most conservative and resolves the ambiguity in a risk-averse manner. A value of $\rho = 1$ , on the other hand, means that the decision maker will resolve ambiguity in a risk-seeking manner. Based on this scheme, if we resolve the ambiguity in b we obtain the following revised m-values:

$$
m ^ {\prime} _ {B} (b) = m _ {B} + \rho (1 - m _ {B}),
$$

$$
m ^ {\prime} _ {B} (\sim b) = (1 - \rho) (1 - m _ {B}),
$$

and

$$
m _ {B} ^ {\prime} (\{b, \sim b \}) = 0.
$$

We can see that in the most conservative case $(\rho=0)$ , all the ambiguity is assigned to the negation of b, which is consistent with risk-averse preferences. However, if we assume that the resolution is made in a risk-seeking manner $(\rho=1)$ , then all the ambiguity is assigned to b. We will develop the decision-theoretic approach for the general case and then use various values of the parameter $\rho$ to discuss the impact of risk attitude on various decisions.

The assurance provider faces possible liability or cost for giving unqualified WebTrust assurance when one or more assertions are not met. This cost, in general, would depend on how many assertions are not met. To make the model more general, we consider different costs or liabilities for different assertions not being met. Also, we assume that there is an additional cost if more than one assertion is not met. This assumption is made to reflect the real world. It seems logical that if only one assertion is not met, then the court may decide it to be just a case of negligence. However, if two or more assertions are not met, then the court may decide that the assurance provider was grossly negligent, resulting into a higher cost than the sum of the individual costs. In those cases where this is not true, one can always set the additional costs to zero. Table 2 provides definitions of various costs considered in the present discussion. We use symbols $C_B$ , $C_T$ , $C_P$ , and $C_L$ to represent the individual costs when the respective assertions, Business Practice (B), Transaction Integrity (T), Information Protection (I), and Legal Environment (L) are not met. We use $C_{BT}$ , $C_{BP}$ , $C_{BL}$ , $C_{TP}$ , $C_{TL}$ , $C_{IL}$ , $C_{BTP}$ , $C_{BTL}$ , $C_{BIL}$ , $C_{TIL}$ , and $C_{BTIL}$ to represent the incremental costs when the related two, three, or four assertions are not met. As an illustration, a numerical example is discussed later in this section.

Table 3 lists all the states with corresponding m-values after resolving the ambiguity in the general way and the corresponding payoffs. The expected value $^{11}$ for the decision when the assurance provider gives an unqualified assurance is given by:

$$
\begin{array}{c} E (\text {Unqualified Assurance}) = F - K _ {B} - K _ {T} - K _ {I} - K _ {L} - [ C _ {B} (1 - m ^ {\prime} _ {B}) + C _ {T} (1 - m ^ {\prime} _ {T}) \\ \qquad + C _ {I} (1 - m ^ {\prime} _ {I}) \\ \qquad + C _ {L} (1 - m ^ {\prime} _ {L}) + C _ {B T} (1 - m ^ {\prime} _ {B}) (1 - m ^ {\prime} _ {T}) m ^ {\prime} _ {I} m ^ {\prime} _ {L} + C _ {B I} (1 - m ^ {\prime} _ {B}) m \phi_ {T} (1 - m ^ {\prime} _ {I}) m ^ {\prime} _ {L} \\ \qquad + C _ {B L} (1 - m ^ {\prime} _ {B}) m ^ {\prime} _ {T} m ^ {\prime} _ {I} (1 - m ^ {\prime} _ {L}) \\ \qquad + C _ {T I} m ^ {\prime} _ {B} (1 - m ^ {\prime} _ {T}) (1 - m ^ {\prime} _ {I}) m ^ {\prime} _ {L} + C _ {T L} m ^ {\prime} _ {B} (1 - m ^ {\prime} _ {T}) m ^ {\prime} _ {I} (1 - m ^ {\prime} _ {L}) + C _ {I L} m ^ {\prime} _ {B} m ^ {\prime} _ {T} (1 - m ^ {\prime} _ {I}) (1 - m ^ {\prime} _ {L}) \\ \qquad + C _ {B T I} (1 - m ^ {\prime} _ {B}) (1 - m ^ {\prime} _ {T}) (1 - m ^ {\prime} _ {I}) m ^ {\prime} _ {L} + C _ {B T L} (1 - m ^ {\prime} _ {B}) (1 - m ^ {\prime} _ {T}) m ^ {\prime} _ {I} (1 - m ^ {\prime} _ {L}) \\ \qquad + C _ {B I L} (1 - m ^ {\prime} _ {B}) m ^ {\prime} _ {T} (1 - m ^ {\prime} _ {I}) (1 - m ^ {\prime} _ {L}) \\ \qquad + C _ {T I L} m ^ {\prime} _ {B} (1 - m ^ {\prime} _ {T}) (1 - m ^ {\prime} _ {I}) (1 - m ^ {\prime} _ {L}) + C _ {B T L} (1 - m ^ {\prime} _ {B}) (1 - m ^ {\prime} _ {T}) (1 - m ^ {\prime} _ {I}) (1 - m ^ {\prime} _ {L}) ], \end{array}\tag{1}
$$

where $m' = m + \rho(1-m)$ , and it represents the revised m-value after ambiguity is resolved. F represents the fee for the assurance service and K represents the cost of

Table 2 List of Symbols

## Symbol Description

<table><tr><td> $C_B$ </td><td>Cost incurred by the assurance provider when Business Policy assertion is not met.</td></tr><tr><td> $C_T$ </td><td>Cost incurred by the assurance provider when Transaction Integrity assertion is not met.</td></tr><tr><td> $C_I$ </td><td>Cost incurred by the assurance provider when Information Protection assertion is not met.</td></tr><tr><td> $C_L$ </td><td>Cost incurred by the assurance provider when Legal Environment assertion is not met.</td></tr><tr><td> $C_{BT}$ </td><td>Incremental cost incurred by the assurance provider when Business Policy and Transaction Integrity assertions are not met.</td></tr><tr><td> $C_{BI}$ </td><td>Incremental cost incurred by the assurance provider when Business Policy and Information Protection assertions are not met.</td></tr><tr><td> $C_{BL}$ </td><td>Incremental cost incurred by the assurance provider when Business Policy and Legal Environment assertions are not met.</td></tr><tr><td> $C_{TI}$ </td><td>Incremental cost incurred by the assurance provider when Transaction Integrity and Information Protection assertions are not met.</td></tr><tr><td> $C_{TL}$ </td><td>Incremental cost incurred by the assurance provider when Transaction Integrity and Legal Environment assertions are not met.</td></tr><tr><td> $C_{IL}$ </td><td>Incremental cost incurred by the assurance provider when Information Protection and Legal Environment assertions are not met.</td></tr><tr><td> $C_{BTI}$ </td><td>Incremental cost incurred by the assurance provider when Business Policy, Transaction Integrity, and Information Protection assertions are not met.</td></tr><tr><td> $C_{BTL}$ </td><td>Incremental cost incurred by the assurance provider when Business Policy, Transaction Integrity, and Legal Environment assertions are not met.</td></tr><tr><td> $C_{BIL}$ </td><td>Incremental cost incurred by the assurance provider when Business Policy, Information Protection, and Legal Environment assertions are not met.</td></tr><tr><td> $C_{TIL}$ </td><td>Incremental cost incurred by the assurance provider when Transaction Integrity, Information Protection, and Legal Environment assertions are not met.</td></tr><tr><td> $C_{BTIL}$ </td><td>Incremental cost incurred by the assurance provider when Business Policy, Transaction Integrity, Information Protection, and Legal Environment assertions are not met.</td></tr><tr><td>F</td><td>The assurance fee.</td></tr><tr><td> $K_B$ </td><td>Cost incurred by the assurance provider in collecting evidential matter to achieve the desired level of belief, $m_B$ , on Business Policy assertion to accept that it is met. $K_T$ Cost incurred by the assurance provider in collecting evidential matter to achieve the desired level of belief, $m_T$ , on Transaction Integrity assertion to accept that it is met.</td></tr><tr><td> $K_I$ </td><td>Cost incurred by the assurance provider in collecting evidential matter to achieve the desired level of belief, $m_P$ , on Information Protection assertion to accept that it is met.</td></tr><tr><td> $K_L$ </td><td>Cost incurred by the assurance provider in collecting evidential matter to achieve the desired level of belief, $m_B$ , on Legal Evaluation assertion to accept that it is met.</td></tr></table>

gathering evidence to obtain a level of belief equal to the desired threshold value for the assertion. The ambiguity resolution parameter $\rho$ depends on the risk attitude of the decision maker.

Table 3. Payoff Table for WebTrust Assurance Decision with m-Values

<table><tr><td rowspan="2">State</td><td rowspan="2">m-values after resolving ambiguity in accordance with Strat&#x27;s ρ*</td><td colspan="2">Payoff</td></tr><tr><td>Accept Engagement Unqualified Assurance</td><td>Do not accept</td></tr><tr><td>btil</td><td> $m'_{B} m'_{T} m'_{I} m'_{L}$ </td><td> $F - K_{B} - K_{K} - K_{I} - K_{L}$ </td><td>0</td></tr><tr><td>~btil</td><td> $(1 - m'_{B}) m'_{T} m'_{I} m'_{L}$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{B}$ </td><td>0</td></tr><tr><td>b~til</td><td> $m'_{B}(1 - m'_{T}) m'_{I} m'_{L}$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{T}$ </td><td>0</td></tr><tr><td>bt~il</td><td> $m'_{B} m'_{T}(1 - m') m'_{L}$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{I}$ </td><td>0</td></tr><tr><td>bti~l</td><td> $m'_{B} m'_{T} m'_{I}(1 - m'_{L})$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{L}$ </td><td>0</td></tr><tr><td>~b~til</td><td> $(1 - m'_{B})(1 - m'_{T}) m'_{I} m'_{L}$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{B} - CK - C_{BT}$ </td><td>0</td></tr><tr><td>~bt~il</td><td> $(1 - m'_{B}) m'_{T}(1 - m') m'_{L}$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{B} - C_{I} - C_{BI}$ </td><td>0</td></tr><tr><td>~bti~l</td><td> $(1 - m'_{B}) m'_{T} m'_{I}(1 - m'_{L})$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{B} - C_{L} - C_{BL}$ </td><td>0</td></tr><tr><td>b~t~il</td><td> $m'_{B}(1 - m'_{T})(1 - m') m'_{L}$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{T} - C_{I} - C_{KI}$ </td><td>0</td></tr><tr><td>b~ti~l</td><td> $m'_{B}(1 - m'_{T}) m'_{I}(1 - m'_{L})$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{T} - C_{L} - C_{KL}$ </td><td>0</td></tr><tr><td>bt~i~l</td><td> $m'_{B} m'_{T}(1 - m') (1 - m'_{L})$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{I} - C_{L} - C_{IL}$ </td><td>0</td></tr><tr><td>~b~t~il</td><td> $(1 - m'_{B})(1 - m'_{T})(1 - m') m'_{L}$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{B} - C_{T} - C_{I} - C_{BTI}$ </td><td>0</td></tr><tr><td>~b~ti~l</td><td> $(1 - m'_{B})(1 - m'_{T}) m'_{I}(1 - m'_{L})$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{B} - C_{T} - C_{L} - C_{BTL}$ </td><td>0</td></tr><tr><td>~bt~i~l</td><td> $(1 - m'_{B}) m'_{T}(1 - m') (1 - m'_{L})$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{B} - C_{I} - C_{L} - C_{BIL}$ </td><td>0</td></tr><tr><td>b~t~i~l</td><td> $m'_{B}(1 - m'_{T})(1 - m') (1 - m'_{L})$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{T} - C_{I} - C_{L} - C_{TIL}$ </td><td>0</td></tr><tr><td>~b~t~i~l</td><td> $(1 - m'_{B})(1 - m'_{T})(1 - m') (1 - m'_{L})$ </td><td> $F - K_{B} - K_{T} - K_{I} - K_{L} - C_{B} - C_{T} - C_{I} - C_{L} - C_{BTIL}$ </td><td>0</td></tr><tr><td colspan="4">* Where  $m' = m + r(1-m)$ .</td></tr></table>

## Discussion of Results

EQUATION (1) YIELDS RESULTS THAT MAKE LOGICAL SENSE. For example, if we assume that the assurance provider obtains 100 percent assurance that all the assertions are met (e.g., $m_B = m_T = m_I = m_L = 1.0$ ), then the expected value of the payoffs for giving an unqualified assurance is simply ( $F - K_B - K_T - K_I - K_L$ ), which is just the difference of the fee and cost $^{12}$ of providing the service. However, if there are uncertainties (risks) whether or not the assertions are met, then the expected value incorporates the liabilities or costs to the assurance provider associated with those risks. We discuss a few special cases below.

## Case 1: No Incremental Joint Costs

Under the assumption that there are no incremental joint costs or liabilities to the assurance provider (e.g., $C_{BT} = C_{BI} = C_{BL} = C_{TI} = C_{TL} = C_{IL} = C_{BTI} = C_{BTL} = C_{BIL} = C_{TIL} = C_{BTIL} = 0$ ), equation (1) yields:

$$
\begin{array}{l} E (\text {Unqualified Assurance}) = F - K _ {B} - K _ {T} - K _ {I} - K _ {L} - [ C _ {B} (1 - m _ {B}) (1 - \rho_ {B}) \\ \quad + C _ {T} (1 - m _ {T}) (1 - \rho_ {T}) + C _ {I} (1 - m _ {I}) (1 - \rho_ {I}) + C _ {L} (1 - m _ {L}) (1 - \rho_ {L}) ]. \end{array}\tag{2}
$$

In general, we use different $\rho$ 's for different assertions because the decision maker may respond differently to different assertions. In this case, the expected value is equal to the assurance fee minus the cost of providing the assurance service less the expected cost or liability associated with the risk of each assertion not being met.

## Numerical Example

Suppose that the assurance provider is a risk-averse individual and has the following cost structure for providing WebTrust assurance with the respective assurances as:

$$
K _ {B} = 2, 0 0 0, K _ {T} = 3, 0 0 0, K _ {I} = 2, 5 0 0, K _ {L} = 2, 5 0 0,
$$

and

$$
C _ {B} = 1 0 0, 0 0 0, C _ {T} = 1 5 0, 0 0 0, C _ {I} = 2 0 0, 0 0 0, \text { and } C _ {L} = 1 0 0, 0 0 0,
$$

with

$$
\operatorname{Bel} (b) = m _ {B} = 0. 9 5, \operatorname{Bel} (t) = m _ {T} = 0. 9 8, \operatorname{Bel} (i) = m _ {I} = 0. 9 9, \text { and } \operatorname{Bel} (l) = m _ {L} = 0. 9 5.
$$

From Equation (2), we obtain:

$$
\begin{array}{c} E (\text {Unqualified Assurance}) = F - 2, 0 0 0 - 3, 0 0 0 - 2, 5 0 0 - 2, 5 0 0 - 5, 0 0 0 (1 - r _ {_ B}) \\ - 3, 0 0 0 (1 - \rho_ {_ T}) - 2, 0 0 0 (1 - \rho_ {_ I}) - 5, 0 0 0 (1 - \rho_ {_ L}). \end{array}\tag{3}
$$

Most conservative resolution of ambiguity ( $\rho = 0$ ): Under this case, the decision maker assigns all the ambiguities to the negation of the respective states. Equation (3) yields: $E(\text{Unqualified Assurance}) = F - 25,000$ .

This expected value implies that \$25,000 is the minimum fee the assurance provider could charge for the above WebTrust assurance service and expect to break even. This result makes logical sense if we assume that there are no interactions among the assertions. However, it appears likely that, when more than one assertion is not met, the liability to the assurance provider will be more than the sum of the individual costs.

Least conservative resolution of ambiguity ( $\rho = 1$ ): Under this scenario, the decision maker takes the risk by resolving the ambiguities by assigning it to the respective affirmation of the states. This process yields an expected value of giving an unqualified report to be:

$$
E (\text { Unqualified   Assurance }) = F - 1 0, 0 0 0.
$$

This result shows that \$10,000 is the break-even point for the service if the service provider is a pure risk seeker. A value between \$10,000 and \$25,000 is appropriate as the break-even point for the audit fee if 1 > ρ > 0.

## Case 2: Risk of One Assertion Not Being Met

Assume that the assurance provider has given unqualified WebTrust assurance with the following level of individual beliefs: $\operatorname{Bel}(b)=m_{B}$ , $\operatorname{Bel}(t)=\operatorname{Bel}(i)=\operatorname{Bel}(l)=1.0$ . The expected value in this case will be

$$
E (\text { Unqualified   Assurance }) = \mathrm{F} - \mathrm{K} _ {\mathrm{B}} - \mathrm{K} _ {\mathrm{T}} - \mathrm{K} _ {\mathrm{I}} - \mathrm{K} _ {\mathrm{L}} - \mathrm{C} _ {\mathrm{B}} (1 - m _ {B}) (1 - \rho_ {B}).\tag{4}
$$

The term $C_{B}(1-m_{B})(1-\rho_{B})$ in the above equation represents the expected cost or liability to the assurance provider for not being 100 percent sure that the Business Policy assertion is met. This term is the product of the cost and the risk the assurance provider has about the assertion.

## Case 3: Risk of Any Two Assertions Not Being Met

Under the assumption where only two of the assertions are not met, the expected value of payoffs can be written as:

$$
\begin{array}{l} E (\text { Unqualified   Assurance }) = F - K _ {B} - K _ {T} - K _ {I} - K _ {L} - [ C _ {i} (1 - m _ {i}) (1 - \rho_ {i}) \\ \quad + C _ {j} (1 - m _ {j}) (1 - \rho_ {j}) + C _ {i j} (1 - m _ {i}) (1 - m _ {j}) (1 - \rho_ {i}) (1 - \rho_ {j}) ], \end{array}\tag{5}
$$

where $i$ and $j$ stand for different assertions.

## Case 4: Risk of Any Three Assertions Not Being Met

When three of the assertions are not met, the incremental cost could be just represented by one interaction term. For example, assume that Business Policy, Transaction Integrity, and Legal Environment are met with a belief of $m_{B}$ , $m_{T}$ , and $m_{L}$ , respectively, and Information Protection is met with 100 percent assurance. The expected payoffs in this case becomes:

$$
E (\text { Unqualified   Assurance }) = F - K _ {B} - K _ {T} - K _ {I} - K _ {L} - \left[ C _ {B} \left(1 - \mathrm{m} _ {\mathrm{B}}\right) \left(1 - \rho_ {B}\right) \right.\tag{6}
$$

$$
+ C _ {T} (1 - m _ {T}) (1 - \rho_ {T}) + C _ {L} (1 - m _ {L}) (1 - \rho_ {L}) + C _ {B T L} (1 - m _ {B}) (1 - m _ {T}) (1 - m _ {L}) (1 - \rho_ {B}) (1 - \rho_ {T}) (1 - \rho_ {L}) ].
$$

## Numerical Example

Consider the following cost structure $^{13}$ with the corresponding beliefs that the assertions are met.

$$
K _ {B} = 2, 0 0 0, K _ {T} = 3, 0 0 0, K _ {I} = 5, 0 0 0, K _ {L} = 2, 5 0 0,
$$

and

$$
\begin{array}{r l} C _ {B} = & 1 0 0, 0 0 0, C _ {T} = 1 5 0, 0 0 0, C _ {I} = 2 0 0, 0 0 0, C _ {L} = 1 0 0, 0 0 0, \text { and } C _ {B T L} \\ & = 1 0 0, 0 0 0, 0 0 0, \end{array}
$$

with

$\operatorname{Bel}(b) = m_B = 0.95$ , $\operatorname{Bel}(t) = m_T = 0.98$ , $\operatorname{Bel}(\mathrm{i}) = m_I = 1.0$ , and $\operatorname{Bel}(l) = m_L = 0.95$ . From Equation (6), we obtain:

(7)

$$
\begin{array}{c} E (\text {Unqualified Assurance}) = F - 2, 0 0 0 - 3, 0 0 0 - 5, 0 0 0 - 2, 5 0 0 - 5, 0 0 0 (1 - \rho_ {B}) \\ - 3, 0 0 0 (1 - \rho_ {T}) - 5, 0 0 0 (1 - \rho_ {L}) - 5, 0 0 0 (1 - \rho_ {B}) (1 - \rho_ {T}) (1 - \rho_ {L}). \end{array}
$$

Most conservative scenario ( $\rho = 0$ ): If the resolution of ambiguity is made in the most conservative way, the expected value of giving unqualified opinion will be (from equation [7]):

$$
E (\text { Unqualified   Assurance }) = F - 3 0, 5 0 0.
$$

This result shows that a risk-averse assurance provider should charge a minimum \$30,500 fee for the WebTrust assurance service. Even though the expected liability cost of “gross negligence” is assumed to be very high (\$100 million), the joint belief of three assertions not being met is very small and thus the net change in the expected cost is small.

Least conservative resolution of ambiguity ( $\rho = 1$ ): This is the extreme case where the decision maker is assumed to be a risk seeker and the break-even fee would be just the direct cost of conducting the assurance service, which is \$12,500 in this case.

There are many other scenarios where the assurance provider does not obtain the desired level of belief for the assertion of interest. In such situations, depending on cost-benefit analysis, the assurance provider will either issue an appropriate qualified opinion or withdraw from the engagement.

## Conclusion

THIS STUDY HAS CONSIDERED TWO THEORETICAL ASPECTS OF ASSURANCE services. The first relates to the type of evidential networks that professional accountants require in order to plan and provide assurance. To illustrate this network, we developed an evidential network model for WebTrust Assurance, a service being provided by the

AICPA and CICA [2]. Of course, the general research area to which this study relates is much broader than WebTrust itself. For example, Gray and Debreceny [10] identify a number of services such as TRUSTe and BBB OnLine, which are similar in nature to WebTrust assurance. Our model augmented the AICPA/CICA approach to providing WebTrust Assurance and presented an additional category of assertion, Legal Environment, related to providing this service. The resolution of uncertainties in the model follows the belief-function approach of Srivastava and Shafer [24]. Our evidential reasoning approach using networks is able to incorporate all potentially relevant relationships and interdependencies among variables and evidence.

Next, we developed a decision-theoretic model for the problem of whether the auditor should take on the assurance service represented by the evidential network. Our approach was based on estimating the expected value of providing various levels of assurance and was illustrated with several different scenarios that may be faced in practice. As expected, the cost factors that were important included the estimated cost of obtaining evidential matter and the incremental cost (liability) incurred when assertions are not met for clients who have obtained a “clean” WebTrust seal.

Being both a modeling paper and the first to attempt to identify some of the issues related to the provision of WebTrust assurance presents both limitations and opportunities for future research. Although the models we present in the figures offer a great deal of detail, they are far from complete models for WebTrust assurance. For example, we have only sketched a few evidential nodes that may be relevant. Future research in both academia and practice need to improve the model by, for example, delineating the specific assertions within each category and the types of evidential matter that may be relevant. Debreceny and Gray [6] and Dedreceny [5] offer some ideas for the latter issue.

The approach we took for the expected value model also involved a number of assumptions and simplifications that need further study. The empirical implications of the Strat [25] approach should also be investigated.

The cost functions we developed, although somewhat complex, are linear, and assume additive costs. In practice, it has been suggested $[2, 6]$ that information technology will facilitate collection of cost and other assurance evidence. This and many other empirical questions in this arena remain to be researched.

## Notes

Acknowledgments: We appreciate the suggestions provided by Roger Debreceny, Mike Ettredge, Wim van der Stede, and Arnold Wright during the early stages of this project. This research has been partly funded by a grant from the General Research Funds, School of Business, University of Kansas.

2. There may be additional assertion categories that need to be considered.

3. Various disciplines have considered the nature of “trust” [14] both within organizations and from the perspective of the individual.

4. We use assertion categories in place of “criteria” as used by the AICPA/CICA document.

5. In order to conserve space, we do not provide details on belief functions here. Rather, we refer readers to $[18–26$ and 28, 29]. However, we provide definitions of the following functions that are important for the current study:

m-values (the basic probability assignment function): m-values represent the uncertainties assigned to individual elements or a set of elements of a frame, Q. All these m-values add to one, i.e.,

$$
\sum_ {A \subseteq \Theta} m (A) = 1,
$$

where A represents a proper subset of Q.

Belief functions: The belief in A, a subset of elements of a frame $\Theta$ is equal to $m(A)$ plus the sum of all the m-values for the set of elements contained in A, i.e.,

$$
\operatorname{Bel} (A) = \sum_ {B \subseteq A} m (B)
$$

By definition, belief in the empty set is zero.

Plausibility functions: Plausibility in A, $\mathrm{Pl}(A)$ , represents the maximum uncertainty that could be assigned to A given the evidence available:

$$
\operatorname{Pl} (A) = \sum_ {A \cap B \neq \emptyset} m (B) = 1 - \operatorname{Bel} (\sim A).
$$

Measure of ambiguity [21, 27]: Ambiguity in $A = \operatorname{Pl}(A) - \operatorname{Bel}(A)$ .

6. Providing assurance for legal requirements that span the global market may turn out to be a daunting task to the extent that the assurance provider only provides a low level of assurance or none at all for this aspect of electronic commerce.

7. We represent assertions by upper-case letters and their values by lower-case letters. For example, the Business Policy assertion is represented by B and its values are represented by b meaning that it is met and $\sim b$ that it is not met.

8. The IFAC exposure draft Reporting on the Credibility of Information states that “The framework and general principles allow for any level of assurance to be expressed” [11].

9. By definition, these states form a mutually exclusive and exhaustive set.

10. By definition, $\operatorname{Pl}(b) = 1 - \operatorname{Bel}(\sim b)$ . Since $\operatorname{Bel}(\sim b) = 0$ , $\operatorname{Pl}(b) = 1$ . Similarly, $\operatorname{Pl}(\sim b) = 1 - \operatorname{Bel}(b) = 1 - m_B$ .

11. One could easily use the utility theory approach in the present discussion. However, for simplicity of presentation, we prefer to use expected value of payoffs rather than the utility function.

12. In general, we assume that the cost of collecting sufficient competent evidence to obtain the desired level of belief in an assertion varies with the level of belief.

13. Note a higher cost for obtaining a higher level of assurance in Information Protection assertion, e.g.,

$$
K _ {I} = 2, 5 0 0 \text {   for   } m _ {I} = 0. 9 9, \text {   and   } K _ {I} = 5, 0 0 0 \text {   for   } m _ {I} = 1. 0.
$$

## REFERENCES

1. American Institute of Certified Public Accountants. Statements on Auditing Standards, no. 47 (1983).

2. American Institute of Certified Public Accountants. AICPA/CICA WebTrust Principles and Criteria for Business-to-Consumer Electronic Commerce. http://www.aicpa.org/webtrust/princrit/htm (1997).

3. American Institute of Certified Public Accountants. Report of the Special Committee on Assurance Services. www.aicpa.org (1997).

4. Curley, S. P., and Golden, J.I. Using belief functions to represent degrees of belief. Organization Behavior and Human Decision Processes (1994), 271–303.

5. Debreceny, R. The Internet and new assurance services. Working paper, Nanyang Technological University, 1997.

6. Debreceny, R., and Gray, G.L. The impact of the Internet on traditional assurance services and opportunities for new assurance services: challenges and research opportunities. Working paper, Nanyang Technological University, 1997.

7. Einhorn, H. J., and Hogarth, R.M. Decision making under ambiguity. Journal of Business, 59 (4), part 2 (October 1986), S225–S250.

8. Einhorn, H. J., and Hogarth, R.M. Ambiguity and uncertainty in probabilistic inference. Psychological Review, 92 (1985), 433–461.

9. Grant Thornton. CPA WebTrust seal erases consumer concerns about electronic commerce. Tax & Business Advisor (1998), 7.

10. Gray, G.L., and Debreceny, R. The electronic frontier. Journal of Accountancy (May 1998), 32–38.

11. International Auditing Practices Committee. Reporting on the credibility of information. Exposure Draft, August 1997, IFAC.

and J. Kacprzyk (eds.), Advances in the Dempster-Shafer Theory of Evidence. New York: John Wiley and Sons, 1994.

13. Jaffray, J-Y. Utility theory for belief functions. Operations Research Letters, 8 (1989), 107–112.

14. Mayer, R. G.; Davis, J.H.; and Schoorman, F.D. An organizational model of organizational trust. Academy of Management Review, 20, 3 (1995), 709–734.

15. Nguyen, H.T., and Walker, E.A. On decision making using belief functions. In R.R. Yager, M. Fedrizzi, and J. Kacprzyk (eds.), Advances in the Dempster-Shafer Theory of Evidence. New York: John Wiley and Sons, 1994.

16. Shafer, G. A Mathematical Theory of Evidence. Princeton, NJ: Princeton University Press, 1976.

17. Shafer, G.; Shenoy, P.P.; and Srivastava, R.P. Auditor's Assistant: a knowledge engineering tool for audit decisions. Proceedings of the 1988 Touche Ross University of Kansas Symposium on Auditing Problems, May 1988, pp. 61–79.

18. Shafer, G., and Srivastava, R.P. The Bayesian and belief-function formalisms: a general perspective for auditing. Auditing: A Journal of Practice and Theory (Supplement) (1990), 110–148.

19. Smets, P. The combination of evidence in the transferable belief model. IEEE Transactions on Pattern Analysis and Machine Intelligence, 12, 5 (May 1990).

20. Smets, P. Constructing the Pignistic probability function in a context of uncertainty. In M. Henrion, R.D. Shachter, L.N. Kanal, and J.F. Lemmer (eds.), Uncertainty in Artificial Intelligence 5. Amsterdam: North-Holland, Elsevier Science Publishers, 1990.

21. Srivastava, R.P. Decision making under ambiguity: a belief-function perspective. Archives of Control Sciences, 6, 42 (1997), 5–27.

22. Srivastava, R.P. Belief functions and audit decisions. Auditors Report, 17, 1 (Fall 1993), 8–12.

23. Srivastava, R.P.; Dutta, S.K.; and Johns, R. An expert system approach to audit planning and evaluation in the belief-function framework. International Journal of Intelligent Systems in Accounting, Finance and Management, 5, 3 (1996), 165–183.

24. Srivastava, R.P., and Shafer, G. Belief-function formulas for audit risk. Accounting Review (April 1992), 249–283.

25. Strat, T.M. Decision analysis using belief functions. International Journal of Approximate Reasoning, 4, 5 (1990), 6.

26. Strat, T.M. Decision analysis using belief functions. In R.R. Yager, M. Fedrizzi, and J. Kacprzyk (eds.), Advances in the Dempster-Shafer Theory of Evidence. New York: John Wiley and Sons, 1994.

27. Wong, S.K.M., and Wang, Z.W. Qualitative measures of ambiguity. In D. Hackerman, and A. Mamdani (eds.), Proceedings of the Ninth Conference on Uncertainty in Artificial Intelligence. San Mateo, CA: Morgan Kaufmann, 1993, pp. 443–450.

28. Yager, R.R. Decision making under Dempster-Shafer uncertainties. Technical Report MII-915, Iona College, New Rochelle, NY, 1990.

29. Yager, R.R.; Kacprzyk, J.; and Fedrizzi, M. Advances in the Dempster-Shafer Theory of Evidence. New York: John Wiley and Sons, 1994.

## APPENDIX A: Decision Making Under Belief Functions

THE UTILITY MAXIMIZATION APPROACH HAS BEEN USED TO MAKE DECISIONS under uncertainty, especially when uncertainty is represented by probabilities. However, the traditional approach does not work when uncertainties are not represented by probabilities. In this section, $^{1}$ we illustrate Strat's approach [25, 26] of decision making when uncertainties are represented in terms of belief functions. In order to illustrate the process, we first discuss the example given by Strat using a probability framework and then change the situation and describe how the decision can be made using belief functions.

## Decision Making Using Probabilities

Consider Strat's example of Carnival Wheel no. 1 [25]. This wheel has ten equal sectors. Each sector is labeled with a dollar amount as follows: Four sectors are labeled \$1, three sectors \$5, two \$10, and one \$20. Each player can spin the wheel for a \$6 fee and receives the amount shown in the sector that stops at the top. The question is, would you spin the wheel?

In this example, there are four outcomes (\$1, \$5, \$10, \$20); the related uncertainties are represented by the following probability distribution:

$$
P (1) = 0. 4, P (5) = 0. 3, P (1 0) = 0. 2, \text { and } P (2 0) = 0. 1.
$$

The expected value of the game is:

$$
E (x) = \Sigma x P (x) = 0. 4 (1) + 0. 3 (5) + 0. 2 (1 0) + 0. 1 (2 0) = 5. 9 0.
$$

The expected utility is:

$$
E (U (x)) = \Sigma P (x) U (x) = 0. 4 U (1) + 0. 3 U (5) + 0. 2 U (1 0) + 0. 1 U (2 0).
$$

If one had to make a decision based on the expected value of the game, then one would not play the game since the expected value of the game (\$5.90) is smaller than the ticket price (\$6).

## Decision Making Using Belief Functions

Consider a situation where uncertainties related to the random events in a decision problem are not expressible in terms of probabilities but in terms of belief functions. As an example of such a situation, consider Carnival Wheel no. 2 of Strat [25]. Carnival Wheel no. 2 is divided into ten equal sectors, each labeled \$1, \$5, \$10, or

20. Four sectors are labeled \$1, two sectors \$5, two \$10, one \$20, and for one sector the label (1, 5, 10, or 20 dollars) is hidden from view. If you have to pay a \$6 fee to play the game, will you play?

Before we discuss how to make a decision under such a situation, let us first express the uncertainties in the problem by m-values in the belief-function framework:

$$
\begin{array}{c} m (1) = 0. 4, m (5) = 0. 2, m (1 0) = 0. 2, m (2 0) = 0. 1, \\ \text { and } m (\{1, 5, 1 0, 2 0 \}) = 0. 1. \end{array}
$$

This simply means that we have direct evidence that \$1 appears in four sectors out of ten on the wheel, \$5 appears in two sectors out of ten, and so on. m( $1, $5, $10, $20$ ) = 0.1 represents the basic probability assignment to the sector with the label hidden from view and thus represents the unassigned part of the probability mass. The corresponding beliefs in the four outcomes are:

$$
\text { Bel } (1) = 0. 4, \text { Bel } (5) = 0. 2, \text { Bel } (1 0) = 0. 2, \text { Bel } (2 0) = 0. 1.
$$

The plausibility for various outcomes are (see note 5 for definitions):

$$
\mathrm{Pl} (1) = 0. 5, \mathrm{Pl} (5) = 0. 3, \mathrm{Pl} (1 0) = 0. 3, \mathrm{Pl} (2 0) = 0. 2.
$$

In this case, the degree of ambiguity, $\mathrm{Pl}(A) - \mathrm{Bel}(A)$ , for each dollar amount on the wheel is 0.1.

If one has to compute the expected utility of the outcome using belief functions, one would get an interval for the expected utility instead of a single value. This is because one needs to assign the unassigned part of probability mass of 0.1 in all possible alternative ways. In the present case, we have four alternatives: We assign 0.1 to either \$1, \$5, \$10, or \$20. Each alternative will give us a different expected value and thus yield an interval for the expected value. $^{2}$ The lower end of the expected value interval for the outcomes of the game in wheel no. 2 is:

$$
E (x) _ {*} = 0. 5 (1) + 0. 2 (5) + 0. 2 (1 0) + 0. 1 (2 0) = 5. 5 0
$$

and the upper end is

$$
E (x) ^ {*} = 0. 4 (1) + 0. 2 (5) + 0. 2 (1 0) + 0. 2 (2 0) = 7. 4 0.
$$

If you had to make a decision based on the expected value, then you are in a difficult situation. The lower end of the expected value is lower than the fee of \$6 and the upper end is greater than the fee. Of course, if you were allowed to gather more evidence, then you might be able to eliminate the ambiguity by, for example, observing the label on the hidden sector. But that is not allowed and you still need to make a decision. What will you do?

As mentioned earlier, there have been several approaches for decision making using belief functions [12, 13, 15, 19, 20, 25, 26, 28]. We describe Strat's approach here because it has strong support from the empirical data of Einhorn and Hogarth [7, 8], as shown in Srivastava [21].

Strat calculates a single value for the expected value for the outcomes of the game by resolving ambiguity in the problem through the choice of a parameter, $\rho$ , that defines the probability that ambiguity will be resolved as favorably as possible. This means that $(1 - \rho)$ represents the probability that ambiguity will be resolved as unfavorably as possible. Under this consideration, the probability for each outcome will be:

$$
P (1) = 0. 4 + 0. 1 (1 - \rho), P (5) = 0. 2, P (1 0) = 0. 2, P (2 0) = 0. 1 + 0. 1 \rho ,
$$

and the expected value will be:

$$
E (x) = 5. 5 + 1. 9 0 \rho .
$$

To decide whether or not to play the game, you need to only estimate $\rho$ . Given that the labels were put there by the carnival hawker, you will probably be more in favor of choosing $\rho = 0$ . This will yield $E(x) = \$5.50$ , which is lower than the fee, and thus an expected value maximizer will not be interested in playing the game.

## Appendix Notes

1. A major portion of this section is taken from Srivastava [21].

2. The expected value interval, $[E_{*}(x), E^{*}(x)]$ , is given by (see, e.g., [25]):

$$
E _ {*} (x) = \sum_ {A _ {i} \subseteq \Theta} \inf (A _ {i}). m (A _ {i})
$$

and

$$
E ^ {*} (x) = \sum_ {A _ {i} \subseteq \Theta} \sup (A _ {i}). m (A _ {i})
$$

where $\inf(A_{i})$ represents the smallest element in the set $A_{i} \subseteq \Theta$ and $\sup(A_{i})$ represents the largest element in the set $A_{i} \subseteq \Theta$ .
