---
otero_id: 17288
otero_key: "UW6CM8N6"
title: "A dedicated shell for designing expert credit support systems"
authors: "Bharat Ruparel; Venkat Srinivasan"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90055-t"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A dedicated shell for designing expert credit support systems

Bharat Ruparel and Venkat Srinivasan

College of Business Administration, Northeastern University, Boston, MA 02115, USA

There is evidence of widespread interest on the part of industrial corporations to develop knowledge based systems for corporate financial applications. This paper describes a successful dedicated shell developed for designing expert support systems for the corporate credit granting process. The shell represents an elegant implementation of knowledge representation in relational databases.

Keywords: Expert systems, Expert databases, Knowledge-based systems, Decision support systems, Relational databases, Credit granting.

## 1. Introduction $^{1}$

There is increasing recognition among academics and practitioners that knowledge-based or expert support systems have the potential to substantially improve managerial decision making and affect significant improvements in productivity. Expert support systems seem to have grown out of the need for decision support on the one hand and the desire to create intelligent systems on the other. Thus, these

![](/api/attachments/UW6CM8N6/fulltext/images/a6333fdfe9dc80fade8bc0e85749a3b3935cc371a9920cb146de11f91d1abc14.jpg)

![](/api/attachments/UW6CM8N6/fulltext/images/9375fec5be9a25c774b0fd29e785762c48ab9c94f7b99e081af8cb3c054c11e7.jpg)

Venkatesan Srinivasan is currently serving as co-editor for Advances in Working Capital Management, a series of research annuals to be published by JAI Press Inc. Professor Srinivasan has published numerous articles in such journals as the Journal of Finance, Management Science, Decision Support Systems, and Financial Management. His current research interest include working capital management, financial expert support systems and financial strategy. He is a member of the Research Committee of the Credit Research Foundation, Inc., and is also a consultant to Apple Computer, Inc.

systems are viewed to be capable of performing not only storage, retrieval, computational and analytical tasks, but inferential tasks as well.

Expert systems for corporate financial decisions, such as credit granting, are likely to differ from conventional expert systems in at least three important ways. First, historically, expert systems have been designed to be consultative in nature. Such systems prompt the user with a series of questions in the process of evaluating rules and stop when the facts supplied by the user satisfy a rule. However, in the context of financial expert systems, it is likely that a large amount of data will be repeatedly analyzed. This will make a sequential question-and-answer form very slow, tedious, expensive and impractical. A better approach in these cases is to design the expert system around an efficient data base where all the relevant data can be stored and the rules can be automatically applied to the relevant set of data.

Second, most financial expert systems will require a large amount of recursive computations on the data. This makes it desirable to store the data efficiently and in a readily accessible mode so that extensive computations can be performed effortlessly. Third, in the case of corporate financial applications, the developer has broader objectives than just developing an expert system to support a specific aspect of the process. Usually, the developer desires to support an entire process through improved systems capabilities, where certain aspects of the process may lend themselves to knowledge acquisition. For example, in the case of credit granting, the system has to support the collection process which is not directly a part of the credit granting decision and also involves negligible knowledge acquisition.

The data intensive nature of financial expert systems also imposes constraints on the type of expert system tools that are most suited. While many commercial shells are available, financial systems will require the capability to seemlessly interface stored knowledge with relevant data bases. One alternative is to use shells like 1st-Class Fusion $^{2}$ not only allow the developer to create knowledge bases that rely on extracted rules and facts but also allow easy interface with popular data base packages like DBASE IV $^{3}$ . A second alternative is to use a relational data base manager for both data and rules (i.e., represent rules as data), use a fourth generation language to design an inference engine and adopt an object oriented design philosophy. Other alternatives include the use of languages like LISP $^{4}$ and PROLOG $^{5}$ instead of ready-made shells. Here again, the connectivity with data bases is likely to be a crucial issue. Of the three alternatives, we suggest that the second alternative best allows the developer to address the three distinct dissimilarities identified with corporate financial applications. $^{6}$

This paper describes a dedicated shell for designing expert support systems for the credit granting process in industrial corporations. The shell uses the relational data model for knowledge representation. Given the increasing interest in integrating expert systems functionality in databases, such a knowledge representation scheme has considerable appeal. The paper is divided into four sections. The next section describes the corporate credit decision process. Section 3 describes the shell. The paper concludes with a summary and identifies work in progress.

## 2. The corporate credit decision process

The corporate credit decision process can be split into several categories: (i) evaluating customers' creditworthiness and determining credit limits; (ii) enforcing credit terms (collection policy); (iii) transaction processing (order processing and cash application); (iv) monitoring aggregate accounts receivable investments; (v) strategic support of the marketing and sales functions; and (vi) cash flow forecasting. While the ultimate objective is to develop an integrated expert support system for the entire process covering all the five categories, the primary focus of the system was defined to be the first two categories which are intimately related.

## 2.1. Evaluating creditworthiness and determining credit limits $^{7}$

The basic goal of the industrial credit granting process is to balance the potential risk of loss against the probability of profits from granting credit. Other than the choice of a classificatory model to separate customer groups on the basis of creditworthiness, the prescriptions of normative theory in credit granting can be summarized as follows [10]:

(i) Credit granting is a multiperiod problem implying that granting credit may not only enable the firm to make the current sale but also sell in the future to the same customer.

(ii) The extent of credit investigation must be determined by the tradeoff between the incremental costs of investigation, the amount of credit involved and the likelihood of creditworthiness at each stage.

(iii) Estimate the present value of benefits and losses from granting credit for all the periods in the planning horizon.

(iv) Integrate probabilities of collection and default with benefits and losses, each period to compute the net present value from each period.

(v) Grant credit, if computed net present value is positive and reject full credit, otherwise.

Note that where computed net present value is negative and credit for the requested amount is rejected, the customer may need to be reevaluated for a lower credit amount (if feasible) and the whole process repeated again. This is because the probabilities of default and collection may be a function of the size of the credit request.

The assessment of default risk probabilities of customers is typically based on an evaluation of several customer attributes, financial and non-financial, that are perceived/found to reflect customer creditworthiness. Two basic approaches have evolved to facilitate such assessment of customer attributes: Judgemental and statistical. All credit analysis, irrespective of the approach used, operate on similar principles. The basic premise in both sets of systems is that past experience can be used as a guide in predicting the creditworthiness of future customers or existing customers in the future.

The credit granting process typically consists of two related segments: setting credit limits and reviewing them once a year, and dealing with exceptions on a daily basis. All major credit lines are reviewed at least once a year. Current credit limits are reviewed to reflect updated information on the customers. On the other hand, exceptions refer to new customers or customers who will exceed their current limits if their orders are approved or customers who have payments past due and need their orders approved. Order processing systems typically have built-in checks that determine whether there are exceptions on any given day. Exceptions are then flagged and credit analysts having responsibility for the customers review the customers' files and decide on credit extension.

Based on an analysis of the costs of investigation and obtaining information and the expected gain in terms of reduced probability of bad debts, firms establish a credit investigation sequence. The sequence is an increasing function of the size of the credit requested and at each successive stage, the amount of information and the level of investigation increases. Typically, at the lowest level, customer background is the primary focus of attention. In the next level, the credit analyst may obtain financial information and letters from bank references. In some cases, subject to the discretion of the credit analyst, Dun and Bradstreet (D&B) reports on these customers may be obtained on a one-time basis. Higher levels of exposure will trigger in-depth analysis of the customers' financial statements, D&B reports and bank references. D&B reports for such customers are almost always ordered on a continuous basis.

Analysis of the creditworthiness of customers can be synthesized in terms of five broad categories. Within each of the categories, a variety of variables are assessed. An illustrative list of such variables is:

(a) Financial strength:
audited or unaudited statements;
proforma or actual statements;
profitability;
debt management
secured or unsecured
off-balance sheet liabilities;
liquidity;
intangibles.

(b) Customer background:
number of years in business;
number of years of relationship with the PC,
perceived management quality;
recent filing of bankruptcy/liquidation;
nature of bank references.

(c) Payment record:
past payment record (with the PC);
past payment record (trade);
internal or cash how problems.

(d) Business potential and frequency: growth potential; customer's market position; market for firm's other products; order frequency.

(e) Geographical location:
perceived economic climate in customer location;
past experience in customer location.

The relative importance of the above factors and the degree of investigation by the credit analyst, of course, differs depending upon the level in which the customer falls. Further, credit investigation proceeds hierarchically with the order of investigation depending on the level of credit investigation and information available and the likelihood of creditworthiness at each stage. Most often, credit limits are set judgementally by linking the results of the customer evaluation process and the benefits and losses from the credit granting decision.

## 2.2. Obtaining timely information

Even though the credit granting decision is an expectational one, firms obviously have to rely on past data to evaluate customers. However, it is important that the information obtained is timely and as recent as possible. Most credit departments spend a considerable amount of time and effort trying to obtain timely information and following up for such information. This aspect of the process is structured to a large extent and can be automated to a significant degree.

## 2.3. Enforcing credit terms

Once a customer has been granted credit, the credit department has the responsibility of enforcing the credit terms extended to the customer. The ability of the firm to enforce its terms depends on both internal and external factors. Internal factors relate to the efficiency of the in-house monitoring system and collection personnel. External factors relate mainly to the competitive climate in the industry and to a lesser extent on the general economic climate. Most credit managers and their staff spend a significant portion of their time following up payments due from customers. The typical process is for designated personnel to place collection calls (in some cases, preceded by collection letters) and to create a log of their conversation and action taken.

## 2.4. Monitoring the quality of receivables

Typically, most firms evaluate customers on an individual basis and have no mechanisms to evaluate the quality of their receivables investments as a portfolio of risks apart from the periodic monitoring of such things as aging reports, etc. A more explicit examination of the portfolio risks is appropriate to ensure that, on the whole, the quality of receivables is consistent with top management's risk preferences. Thus, an individual customer may be an unacceptable risk at the micro-level and yet, the dynamics of the portfolio may allow the firm to accept the risk-return tradeoff. This may happen due to lower perceived risks of other customers.

## 3. The dedicated shell

The shell is aimed at supporting the processes outlined in the previous section in an intelligent manner. A major objective in the design of the shell was to ensure that the system allowed a user to incorporate his/her expertise and therefore be able to easy customize the knowledge base. The development of the shell initially began as a specific system in 1985 with one Fortune 500 corporation serving as the development laboratory. In extending beyond the development laboratory, we observed a significant degree of commonality in the process that formed the motivation for designing a dedicated shell. The shell relies on a relational database manager for data storage as well as knowledge representation.

## 3.1. Rule representation as relational tables in the shell

A rule is essentially a meta-object, i.e., it can be thought of as a composite of smaller objects. It can be created, updated, and deleted just like any entity in a database. We employ a scheme of successive and stepwise refinements to decompose the rule into its smaller objects down to the atomic level, i.e., until each of the decomposed objects is an independent object that cannot be decomposed any further in the context of the application being modeled. We then work backwards to create a scheme of relational tables to store and implement a rule. This is described in more detail in the following paragraphs.

A rule is quite similar to an IF ...condition... THEN ...results... statement in conventional programming language environments. It essentially consists of two components: A condition component and a result component. In this system, the condition component can consist of a simple condition or a number of simple conditions connected by the logical 'AND' operator. (We describe a scheme to implement rules with disjunctive conditions later in the section). The result component, a score, a weight or a probability, is atomic or monotonic. However, in general, it can also be an action, e.g., update certain portions of the database.

Since the action component is simpler for this system, we will deal with it first. An atomic object, i.e., the score here, can be stored in a table. This table has a rule-identifier field, a score or weight field and a note or memo field for expert comments. If the condition component consists of multiple conditions, it can be broken down into smaller or simple conditions. These simple conditions share a common structure. They define a range for a continuous state variable or a point value for a discrete state variable. These state variables are stored in the database. The range is defined by upper and lower limit (UL and LL) parameters which will have the same value (a point) for a discrete variable. Note that a qualitative attribute can be mapped to a discrete numeric variable and stored as such. For output, this mapping can be reversed to obtain the qualitative attributes value.

Essentially four tables can be created to hold a set of rules (e.g. rules to evaluate customer background). Using this scheme, the rulebase can be completely normalized $^{8}$ . Table 1 is really a look-up table which holds the factor domain, i.e., all possible factors which can be used to create rules, factor description for user interface and output purposes and a flag indicating whether that factor is being currently used for condition definitions or not. Table 1 illustrates the factor domain for background rules. Three of the four factors have currently been selected for defining rules.

Table 1  
Factor domain.

<table><tr><td>Factor</td><td>Description</td><td>Selected</td></tr><tr><td>IEXP</td><td>Number of years the customer has been doing business with the firm</td><td>YES</td></tr><tr><td>TEXP</td><td>Number of years customer has been in business</td><td>YES</td></tr><tr><td>MQ</td><td>Management Quality</td><td>YES</td></tr><tr><td>BL</td><td>Bankruptcy filing within last four years</td><td>NO</td></tr></table>

Table 2  
Factor range definitions (for size category 1).

<table><tr><td>Factor</td><td>Lower (years)</td><td>Upper (years)</td></tr><tr><td>IEXP</td><td>0</td><td>2</td></tr><tr><td>IEXP</td><td>2</td><td>4</td></tr><tr><td>IEXP</td><td>4</td><td>7</td></tr><tr><td>IEXP</td><td>7</td><td>∞</td></tr><tr><td>TEXP</td><td>0</td><td>2</td></tr><tr><td>TEXP</td><td>2</td><td>5</td></tr><tr><td>TEXP</td><td>5</td><td>7</td></tr><tr><td>TEXP</td><td>7</td><td>∞</td></tr></table>

Table 3  
Rule condition.

<table><tr><td>Factor</td><td>Lower</td><td>Upper</td><td>Rule ID</td></tr><tr><td>IEXP</td><td>2</td><td>4</td><td>10</td></tr><tr><td>TEXP</td><td>5</td><td>7</td><td>10</td></tr><tr><td>MQ</td><td>1</td><td>1</td><td>10</td></tr></table>

Table 2 holds the user-defined ranges on continuous factors and point values for discrete factors. The user in this instance will most likely be the knowledge engineer working with the experts. These ranges or point values should be mutually exclusive and collectively exhaustive. Any number of ranges or values can be defined. For example, table 2 presents ranges for the IEXP factor in table 1. Note that ranges may be different for customers of different sizes or be a function of such variables as industry grouping. Size here is proxied by the amount of credit sought by the customer.

Table 2 defines the domain for table 3. Table 3 holds the total condition component of the rule in the form of one or more rows. If the condition components consists of a simple condition defined as a range or a point value on a factor then that rule can be represented by only one row in table 3. In general, the number of rows required to represent a rule is the same as the number of simple conditions defined on various factors. To illustrate, table 3 presents a rule with three simple conditions. Further, the third condition relates to the management quality factor which is a discrete variable. As stated before, in the case of discrete factors, the lower and upper range parameters are the same, effectively yielding a point value. Note the implicit assumption that the simple conditions are all conjunctive, i.e., connected by the locial 'AND' operator. Therefore, if any of these conditions is not met, the rule will not be activated.

Table 4
Result table.

<table><tr><td>Rule ID</td><td>Score</td><td>Expert text</td></tr><tr><td>10</td><td>10</td><td>Customer has been in business for more than five years.We have had a business relationship with the customer for between two and four years.Customer&#x27;s management quality is perceived to be excellent.Overall, customer&#x27;s background is considered excellent</td></tr></table>

Table 4 holds the result component. As pointed out earlier, this holds the rule identifier, score and expert text. The user could associate every rule with unique expert text which comprises the reasoning component of the system. The hierarchical relationship among the four tables is shown in fig. 1. The first level of the hierarchy shows the one-to-one relationship between the condition component and the rule component. The relationship between the condition component and simple conditions forms the next level of the hierarchy. Finally, the simple conditions can be represented in terms of a factor, a lower limit and an upper limit as shown in the third level of hierarchy in fig. 1. As an illustration, consider the following rule:

![](/api/attachments/UW6CM8N6/fulltext/images/8988679eb6fdbbde78679167725997348a10545cef0bbd92d4d36b11184aa097.jpg)

<table><tr><td>If</td><td>IEXP</td><td>is between 0 and 2 years</td></tr><tr><td>AND</td><td>TEXP</td><td>is between 0 and 2 years</td></tr><tr><td>AND</td><td>MQ</td><td>is Excellent</td></tr><tr><td>Then</td><td>Background Score</td><td>is 50.</td></tr></table>

The above rule is composite condition which consists of three simple conditions connected by the 'AND' operator. The result here is the score of 50. We have two continuous factors in this rule, namely IEXP and TEXP, and and discrete factor—MQ. The continuous factors have a set of user defined ranges. The discrete factor can have any number of user defined values, e.g., Excellent, Very Good, Good, Above Average, Average, Poor, etc.

Summing up, a rule consists of a condition and a result. The condition is an aggregate of simple conditions. A simple condition is either a range on a factor defined by upper and lower limits or a point value. This completes the stepwise splitting (or refinement) process to the point where all the attributes and parameters are in atomic state.

## 3.2. Representing rules with disjunctive conditions

In the previous section, we illustrated the rule representation scheme used in the shell where the rule consisted of a number of simple conditions connected together by the conjunctive 'AND'. It is, however, possible that the user desires to represent disjunctive conditions in a rule. We will consider two distinct situations in this context. The first is where the user wishes to use a disjunctive 'OR' but still uses all the factors in the factor domain. The second is where the user does not necessarily wish to use all the factors in the factor domain in constructing a rule. In the first case, the representation scheme outlined in the previous section will still apply. As an illustration consider the following rule

<table><tr><td>If</td><td>IEXP</td><td>is between 0 and 2 years</td></tr><tr><td>OR</td><td>IEXP</td><td>is between 2 and 4 years</td></tr><tr><td>AND</td><td>TEXP</td><td>is between 0 and 2 years</td></tr><tr><td>AND</td><td>MQ</td><td>is Excellent</td></tr><tr><td>Then</td><td>Background Score</td><td>is 50.</td></tr></table>

The rule above contains a disjunctive condition for the first factor but still uses all the selected factors in the factor domain. It is easy to see that the above rule can be split into two rules as follows

<table><tr><td>If</td><td>IEXP</td><td>is between 0 and 2 years</td></tr><tr><td>AND</td><td>TEXP</td><td>is between 0 and 2 years</td></tr><tr><td>AND</td><td>MQ</td><td>is Excellent</td></tr><tr><td>Then</td><td>Background Score</td><td>is 50.</td></tr><tr><td>If</td><td>IEXP</td><td>is between 2 and 4 years</td></tr><tr><td>AND</td><td>TEXP</td><td>is between 0 and 2 years</td></tr><tr><td>AND</td><td>MQ</td><td>is Excellent</td></tr><tr><td>Then</td><td>Background Score</td><td>is 50.</td></tr></table>

Both the rules can be stored as described in the previous section. Consider as an example of the second case, the following rule

If BL is YES
Then Background Score is 0.

While this rule can be represented exactly as described above, it requires a different inferencing process for it to be activated. This is true as long as the factor domain contains factors in addition to the factor BL and these factors are selected for use in rule definition. In the shell, we refer to such rules as 'exception rules'. The inferencing process for exception rules is described in a subsequent section.

## 3.3. Shell structure

Structurally, the shell consists of three components: A customer database; a rulebase; and a financial consultant.

## 3.3.1. The customer database

The Customer database contains all available data pertaining to the firm's credit customers. The database is logically divided into fourteen primary files according to the attribute group to which a specific data item might belong (fig. 2). The primary files are related to each other through appropriate key fields. Various one-to-one and many-to-many relationships were resolved through normalization. A brief description of the primary files is given below.

Basic customer info constitutes the core file containing the customer's name, address, etc., and a customer code. It is customary in most firms to identify a customer with an accounts receivable code that is unique to the customer. All the remaining primary files are linked (related) to this file through the customer code field.

Background file allows the user to manage data relating to the customer's background, such as the number of years the customer has been in business, the number of years of business relationship with the customer, management quality, etc. A separate lookup table was created for management quality. Every customer has a unique record in the background file.

Pay file. Customer's payment habits form an important input to the credit evaluation process. Pay habits are typically categorized into discrete classes which may be different from firm to firm or from one industry to another. Pay categories are housed in a separate lookup table. The shell allows users to customize the descriptions of pay categories to suit their circumstances.

Bank ref file allows the user to manage data relating to the customer's bank references. Bank reference data can be grouped into two categories (i) data that identifies the bank; and (ii) data that identifies the nature of a customer's relationship with the bank. Several lookup tables support the bank reference file. All these lookup tables are customizable by the users.

Trade ref file allows the user to manage data relating to the customer's trade references. Very similar to the bank reference file in structure.

Collateral file allows the user to manage data relating to collateral that may be furnished by individual customers. The various types of collateral typically furnished are known. Therefore, these were represented as fixed fields and the users allowed the flexibility to input two nonfixed collateral types. A customer can at most have one record in this file.

Balace sheet & income statements. These two files contain the customer's financial statements. There can he multiple records per customer in both the files. Often users will get only one of the two statements from the customer. Therefore, these two statements were into separated files. The two files are related to each other through a complex key field combining the statement year, statement period and statement type (audited, unaudited, etc.).

Financial

Non-financial

![](/api/attachments/UW6CM8N6/fulltext/images/c49a1affd43403b8c5c820fac0e2a37d2c6479a4cad445e84f6e8bdf1be62bc1.jpg)  
Fig. 2. The customer database structure.

Misc. credit file. This file contains data that cannot be logically allocated to any of the other primary files. Data in this file includes the customer's D&B rating, credit review dates, frequency of review, etc. Every customer has at most 1 record in the file.

![](/api/attachments/UW6CM8N6/fulltext/images/04ceef41f0d86001ed5f7f2053fbb8ccb39f72660b6e3933e4085dc866e89470.jpg)  
Fig. 3. Rulebase structure.

In addition to these primary files, the Customer database contains secondary files for storing some processed data. Examples are a file for storing financial ratios, another file to store trends in financial variables, a file to store results of matching rules with customers' data, etc.

## 3.3.2. The knowledge base and inferencing process

The shell's knowledge base for credit granting can be divided into two subcomponents: (i) rules for evaluation of customer creditworthiness; and (ii) model base to integrate risk and return. Evaluation of customer creditworthiness is accomplished using rules for each of the attribute categories, finding the applicable set of attribute weights, and computing a total weighted credit score. Credit limits are established by integrating these credit scores and a proxy for returns, using models available in the model base. The rulebase is completely customizable.

For the representation scheme described in the previous sections, the inferencing process is quite simple. At runtime, the shell retrieves the values for the selected factors for a specific customer, matches them against the rules and determines the result. Such a sequential process is likely to be slow in large applications. This is, because, in the worst case, the sequential process requires an exhaustive search of all the rules in the rulebase to find a matching rule. One way to improve system efficiency is to map the representation scheme described in the previous section to an index key to facilitate direct access. Essentially this means mapping or creating a many-to-one relationship between data and rules. This scheme also eliminates the need for the third table described in the previous section. $^{9}$ The resulting rulebase structure is shown in fig. 3.

The construction of the rule index key can be described in terms of the hierarchical relationships used to describe rule representation in fig. 1. This is shown in fig. 4. The first level shows the one-to-one relationship between the condition component and the result in terms of the rule index key and the result. The rule index key is an abstract representation of the condition component. It can be created by representing the simple conditions in terms of a unique identifier for the corresponding attribute value as shown in the second level of fig. 4. The unique identifier for a factor corresponds to a unique value for the factor. In the case of numeric factors, the unique identifier can correspond to a discrete range of values for the factor. Qualitative variables are by definition represented in discrete values. The final hierarchical relationship is shown in the third level of fig. 4. Thus, a rule can be stored and identified using a unique rule index key. As an illustration, consider the following rule.

![](/api/attachments/UW6CM8N6/fulltext/images/eab25e5557d41f3825bc3783a7078ca6a73d3c0c9a7f23144090da0c1a48aed4.jpg)  
Fig. 4. Rule representation using indexes.

If IEXP is between 0 and 2 years

AND TEXP is between 0 and 2 years

AND MQ is Excellent

Then Background Score is 50.

It is clear from table 1 and the rule shown above that three out of four factors have been selected for this rule. Any unselected factor can be represented by a predefined symbol or character (e.g. letter Z for instance). Therefore factor BL will be represented by the letter Z in this rule's index key. Table 2 shows that for both the continuous factors, IEXP and TEXP, the first user defined range is applicable. Therefore they will be represented by the character 1 in the rule's index key. Lastly, the discrete factor MQ has a user defined value of Excellent which is obtained from a separate lookup table for this factor. Since Excellent, is the very first user defined value for this factor, it will also be represented by the character 1. Maintaining the ordering of factors shown in table 1 (i.e. IEXP first, TEXP second, MQ third, and BL fourth), the value of index key will be 111Z. This key is maintained dynamically. Key values are updated whenever existing user defined ranges are deleted. Merely editing the lower and upper limits of a range, or creating additional ranges will not affect the key value. Also, the key is expanded or shrunk as factors are added or deleted in the factor domain table shown in table 1.

![](/api/attachments/UW6CM8N6/fulltext/images/4142be3e5c48e0db71c81143807bc4ea9cf0985817b952f1d748e30ee263a0c9.jpg)  
Fig. 5. Attribute weight rule file structure.

With the index key, the processing of individual customer data is done as follows. The shell uses rule file 1 (fig. 3) and finds the customer value for each factor that has its flag 'ON'. As the values are found, the corresponding range numbers are found by searching rule file 2. The rule index key for the customer is built recursively. After this process is complete, the system searches for a matching rule in rule file 3. If a matching rule is found, the result is stored in an intermediate file. The process is repeated for all attributes. Once scores have been determined, the system searches for the appropriate attribute weights in the weight rule file. The weight rule file also has a structure identical to that of the attributes (fig. 5). Currently, the weight rule file 1 has six factors corresponding to the five attributes (background, bank reference, trade reference, pay and financials) and a size factor. All the factors are restricted to two discrete values in rule file 2: Yes and No. 'Yes' indicates that the database has information available to evaluate the customer on the relevant attribute, e.g., 'Yes' for financials indicates that the customer database has customer financials that can be evaluated. The weight rule file 3 contains the appropriate weights to be used corresponding to a range combination (rule index key). Thus, this scheme allows users to de- with incomplete information to a large extent.

The above inferencing scheme is very much like a forward chaining process, where the system processes the attributes in some predetermined order and the results of each attribute chain forward to yield the final result. It is dissimilar to the conventional forward chaining process in the sense that the conventional expert system environments do not try to ‘factor’ out the commonality in the domain expertise as we have attempted to in the shell. This will become clear as we compare the inferencing process that the shell uses for ‘exception’ rules.

As stated earlier, exception rules are stored in the same way that stable rules are. However, the exception rule file 1 has an additional field to indicate the data file that the factor is drawn from. This is because exception rules could use any factor across the factor domains for the attributes. For example, the exception rule file 1 could have factors from the bank rule file 1, background rule file 1, financial rule file 1, etc. Exception rules are processed sequentially. However, users indicate the importance of various factors in the exception rule domain. At runtime, the system creates a new rule index key by ordering the exception rule file 1 according to the importance of the factors. This ensures that the most important rule is the first one to be checked.

While the unique rule index key allows the system to access matching rules very quickly (instantaneously in most cases), the processing speed for exception rules is slower because of the sequential nature of such processing. However, we have so far found that the number of exception rules are so small that this is really not an issue in this decision process. $^{10}$

The model base currently houses two types of models: (i) an explicit risk-return model; and (ii) an implicit risk-return model. The explicit risk-return model interprets the total credit score as the expert's subjective prior probability of payment. These probabilities are then integrated in a simple expected value framework to yield the expected net present value and the recommendation is based on the conventional net present value rule. Users have the option to define returns in terms of product contribution margin, account profitability, or opportunity cost of capital. Such a model obviously assumes that managers are willing to assume greater risks (without limit, theoretically) for greater returns. If this is not desired, the returns can be held constant to reflect a truncated risk preference function. In practice, many credit managers relate the maximum amount of desired exposure to the customer's net worth. We interpret this as an implicit mechanism for integrating risk and return and allow users to set maximum limit to networth ratios for various classes of customers. Appendix A displays sample output from the system.

## 3.4. Supporting other segments of the credit decision process

The shell, as described in the previous section, focuses on only one major aspect of the credit decision process. From an implementational perspective, a better approach is to increase the functionality of the system to also intelligently support other aspects of the credit decision process. Accordingly, a variety of options and features were added to the shell to significantly increase its functionality. Among the major additional support features are:

(1) Tickler sub-system. The credit decision process has a number of related tasks that need periodic monitoring, e.g., customer credit evaluation, collateral expiry, bank reference updates, trade reference updates, financial statement updates, Dun & Bradstreet report updates, etc. The database structures were expanded to store user-defined tickler frequencies for a variety of action variables. The tickler sub-system can be invoked by the user with a listing of tickler actions that are due. The user has the option to execute some of the actions directly from the tickler sub-system. The user can also suspend the tickler operation to perform actions that cannot be performed from within the tickler sub-system and resume tickler processing where suspended.

(2) Industry patterns. Comparison of customers implies the existence of a standard. Frequently, experts would desire to examine aggregate industry patterns before deciding on standards. A common practice is to look up published industry average data by the Standard Industrial Classification (SIC) code. In the shell, the users have additional options to examine the aggregate behavior of the customers in the customer database. Further, customers in the customer database can be identified by several industry affiliation variables effectively allowing users to examine micro-segments of the industry as portrayed by the firm's customers. For example, in one implementation in the computer industry, there were 3 industry related variables that allowed the users to examine customer data according to business focus, class of trade, market segment and any combination thereof.

(3) Sensitivity analyses. Often, the information on customers is received late and, thus, the credit manager has to form expectations about future behavior based on outdated data. Under such circumstances, sensitivity analyses obviously becomes crucial. However, instead of the user having to modify customer data in the database, a number of different 'What If' options were added to facilitate easy sensitivity analysis. This set of options also includes the ability to forecast customer financial statements so that the user can evaluate the customer based on forecasted financial statements.

(4) Special management reports. Aside from the operational aspect of the credit granting process, there is also the need to support a number of tactical dimensions of the process including an aggregate evaluation of the quality of the firm's receivables, internal control reports, etc. Receivables quality can be proxied by computing dollar-weighted credit scores and monitoring such scores over time. A number of other reporting options were added to generate reports typically required by higher level managers.

(5) Form letters. The most common mode for updating customer data is to mail standardized letters to various constituencies requesting for updates. Since these letters are mostly standard, their processing can be automated by storing standard letters and using user-defined tickler conditions to mail them. Accordingly, 2 sets of capabilities were added to the shell: (i) the ability to design and store standard letters requesting information from Dun & Bradstreet, bank references, trade references, and the customer; and (ii) the ability to automatically generate these letters for mailing.

(6) Collection log. A major task of credit managers is to follow up on payments from customers. This aspect of the process consumes a significant amount of time and effort and also lends itself to analytical support. The database and rulebase were expanded to allow the credit managers to create and maintain a collection log and to perform a variety of operations on the log.

(7) Portfolio diversification. The accounts receivable investments for any corporation really represents a portfolio of risks which are constantly changing over time. Viewed with such a perspective, the credit managers may desire to analyze their accounts receivable investments in the aggregate as a portfolio and manage the portfolio such that the implicit risk distribution in the portfolio is consistent with their risk preferences. The shell allows credit managers to apply portfolio risk diversification concepts by tracking aggregate risk behavior of various customer groups and using aggregate constraints to ensure that total portfolio risk is in line with managerial risk preferences.

The above enhancements to the shell transform it from being a narrowly defined expert system to a more complete expert support system for all aspects of the credit granting process.

## 4. Summary and extensions

There is a significant amount of interest in industrial nonfinancial corporations to exploit advances in artificial intelligence technology by creating expert systems. This paper has suggested that the relational databases coupled with fourth generation procedural languages provide an attractive environment for designing such systems. Such a knowledge representation scheme has been applied to the corporate credit granting process with considerable success. The resulting shell enables the corporate credit manager to create an expert support system for the credit granting process.

In the seven Fortune 500 corporations, knowledge engineering itself was done outside the shell using a variety of different processes. Once the initial knowledge was defined, the users used the shell to store, update and manage their knowledge base. We are now extending the shell in several directions. One is to explicitly incorporate induction capabilities within the shell to enable the users to structure initial knowledge within the shell, as much as possible. Another area of future research is to improve the inferencing process for sequential rules.

## References

[1] Athena Group, Portfolio Management Advisor Application Note (New York, NY, 1986).

[2] M.R. Blaha, W.J. Premerlani and J.E. Rumbaugh, Relational Database Design Using an Object-Oriented Methodology, ACM Computing Practices (1988).

[3] B.G. Buchanan and E.H. Shortcliffe, Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project (Addison-Wesley, Reading, MA, 1984).

[4] CCGX Beta User's Manual, Version 0.01 (©SR Research, Boston, 1988).

[5] C.W. Holsapple, K.Y. Tam and A.B. Whinston, Adapting Expert System Technology to Financial Management, Financial Management, 12–22 (Autumn 1988).

[6] C.W. Holsapple and A.B. Whinston, Business Expert Systems (Irwin, Homewood, IL, 1987).

[7] K. Parsaye and M. Chignell, Expert Systems for Experts (Wiley, New York, 1988).

[8] T. Risch, R. Reboh, P. Hart and R. Duda, A Functional Approach to Integrating Database and Expert Systems, Communications of the ACM, 31(12), 1424–1437 (1988).

[9] V. Srinivasan and Y.H. Kim, Financial Applications of the Analytic Hierarchy Process. TIMS XXVII International Meetings, Gold Coast, Australia, July.

[10] V. Srinivasan and Y.H. Kim, Credit Granting: A Comparative Analysis of Classification Procedures, Journal of Finance, 661–680 (July 1987a).

[11] V. Srinivasan and Y.H. Kim, The Bierman–Hausman Credit Granting Model: A Note, Management Science, 1361–1362 (Oct. 1987b).

[12] V. Srinivasan and Y.H. Kim, Designing Expert Financial Systems: A Case Study of Corporate Credit Management, Financial Management, 32–44 (Autumn, 1988).

[13] V. Srinivasan and B. Ruparel, Designing an Expert Support System for Credit Granting, European Journal of Operations Research, 45, 293–308 (1990).

# Appendix A Sample output from the shell

Credit analysis for: SR Research Inc.
30 Silver Hill, No. 8
Natick, MA 01760

<table><tr><td>Credit need</td><td>$30,000</td></tr><tr><td>Existing line</td><td>$ 0</td></tr><tr><td>Suggested line</td><td>$ 0</td></tr></table>

Overall conclusions:

Pay experience Good
Background Good
Bank Good
Financials Poor

## Narrative:

Pay. Customer pay habits are good. Pay from SR Research has been mostly within terms and pay to trade is excellent. Focus on collection efforts to bring pay from SR Research up to par with trade pay.

Background. Customer background is considered good. Customer has been doing business with us for over five years and has been in business for more than eight years. Customer's management capabilities are generally considered to be good. No indication of customer having filed any bankruptcy papers within the last four years.

Bank. Customer's major bank indicates relationship as satisfactory. Minor banks also report satisfactory relationship. Balance details with major banks are as follows:

Current account. Medium Six Figures
Unsecured loan-high high seven Figures
Unsecured loan-present medium six figures
Secured loan-high high eight Figures
Secured loan-present medium eight Figures

Financials. Customer's financials are considered to be poor. The conclusion was drawn based on three years' audited financial statements. The latest financial statement is four months old as of review date.

Summary. Customer's financial strength is judged to be poor. This conclusion has been reached after finding that customer's basic earning power is poor, total asset turnover is high, and the customer is not significantly levered financially. Negative net profit margins have thus been compounded by the high asset multiplier significantly worsening the situation Restructuring is recommended with a view to improving profitability and improving the total asset turnover. In the short run, more equity is required to reduce the fixed financial costs and/or improve cash flow. Revenues declined sharply in the most recent period. Customer's revenue base and future prospects need careful attention. Based on the adjusted Z-score, the customer is beyond the critical range.

Profitability. Customer's basic earning power is quite poor, Major efforts should be directed to improve all dimensions of profitability-pricing, focus, service revenues, fixed and variable operating expenses, financial costs and nonoperating items. Gross margin in the most recent period (16.5%), is marginal. Compounding the already low gross profits is an above average operating expense ratio. Net profit margin (-1.1%) is poor with respect to standards. It has been worsened to a degree of nonoperating items. In terms of the comparison groups, customer is in the 20–40% range with respect to gross profits and net profit margins and in 60–80% with respect to operating expense ratio. Sales were sharply lower (-13.8%) in the most recent period compared to the immediately prior period. This calls for an examination of the fixed costs and breakeven levels in the customer's operations. Gross margins show a significantly declining trend. Customer has, however reduced operating expenses significantly and more than offset the worsening trend in gross margins at the operating level. There is probably substantial competitive pressure on price, and/or a significant reduction in service revenues. Nonoperating income provided a significant boost to net profit margin for this period.

Asset management. Total asset turnover is in the above median range relative to standards. Customer's level of asset utilization is good. Given that the turnover is already at a high level, focus should be on turning net profit margins around if necessary by reducing the scale of operations. Current asset turnover appears relatively higher than noncurrent asset turnover. Total asset turnover increased to 5.295 in the most recent period further compounding the deteriorating trend in net profit margin. The multiplier effect yielded a return on assets of -5.9% compared to -0.3% in the immediately prior period. Receivable turnover is in the 20–40% and has decreased significantly.

Debt management. Customer's financing strategy is quite conservative. Financing requirements have been primarily met through equity. Reliance on short-term debt and supplier financing has been low. No appreciable change was observed in the relative levels of supplier financing. There has been a considerable decrease in the overall proportion of the amount of long-term debt as a percent of total debt and equity. Even though the overall level of debt as a proportion of total assets is low, customer's debt service levels are poor. If operating margins are not expected to increase significantly, customer needs to infuse equity into the business.

Liquidity. Current ratio is in the top $20\%$ and quick ratio is in the above median range with respect to the standards. Customer exhibits a relatively long net operating cycle. Customer's cash flow from operations are negative and a cause for serious concern in light of the sharp decline in sales revenues and negative net profit margins. Long run solvency is questionable. Customer needs to find strategies to break even including a critical review of existing revenue base and judiciously manage liquidity pressures.
