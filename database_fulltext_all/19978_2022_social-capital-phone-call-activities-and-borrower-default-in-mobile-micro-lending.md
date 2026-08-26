---
otero_id: 19978
otero_key: "JKBYRCZ4"
title: "Social capital, phone call activities and borrower default in mobile micro-lending"
authors: "Weihe Gao; Yong Liu; Hua Yin; Yiwei Zhang"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113802"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Social capital, phone call activities and borrower default in mobile micro-lending

![](/api/attachments/JKBYRCZ4/fulltext/images/ed3a7f2dea51c9bfd46b534024de1659469e8f78e0f665403f7cfa2653086677.jpg)

Weihe Gao <sup>a</sup>, Yong Liu <sup>b</sup>, Hua Yin <sup>c,\*</sup>, Yiwei Zhang

<sup>a</sup> College of Business, Shanghai University of Finance and Economics, Shanghai 200433, China

<sup>b</sup> Eller College of Management, University of Arizona, Tucson, AZ 85721, USA

<sup>c</sup> Research Institute for the Development of Shanghai, Shanghai University of Finance and Economics, Shanghai 200433, China

<sup>d</sup> School of Management, Shanghai Sanda University, Shanghai 201209, China

## A R T I C L E I N F O

Keywords: Credit worthiness Loan default Fintech Mobile micro-lending Social capital

## A B S T R A C T

This study examines how the social capital of borrowers affects loan defaults in the burgeoning mobile microlending market. We analyze the individual-level transaction data provided by one of the world’s largest mo bile lending platforms. Focusing on identifying behavior-based predictors of financial transactions, we propose that mobile phone calling activities constitute a valuable measure of social capital. Drawing on the theoretica foundation of social capital theory, we identify and study two types of calling activities: incoming calls and outgoing calls, strong ties and weak ties. Our analysis shows that the more incoming calls a borrower usually receives, the less likely he or she is to default on a loan. However, the more outgoing calls a borrower makes, the more likely default will occur. We further find that calling activities associated with stronger social ties have greater predictive power for loan defaults than those associated with weaker ties. These findings demonstrate the relevance of phone call activities in consumers’ financial decisions. They provide micro-lending companies with valuable alternatives for assessing borrower creditworthiness bevond “hard information", such as credit scores and income, and further help them make more effective loan decisions

## 1. Introduction

As a key component of Fintech applications, micro-lending has emerged in recent years as a popular funding channel for consumers [21,39,55,56,62]. Micro-lending enables individuals to borrow directly, often in relatively small amounts, from lenders via the internet or mobile platforms without traditional financial institutions acting as in termediaries [55,62]. It is expected that the loan origination of this market in the United States will soon amount to \$90 billion and the global market value will reach \$290 billion.<sup>1</sup>

Predicting consumer credit risk is a crucial task for financial institutions when making decisions regarding loans and other transactions in the traditional credit market, P2P lending, and online consumer credit service markets [48]. It has further attracted substantial attention in decision support systems. This is particularly true for micro-lending because customers on these platforms often lack credit history and belong to low-income groups that are vulnerable to credit risks [14]. In fact, the default rate is much higher in micro-lending than in the con ventional credit market, where borrowers are often required to provide collateral [18,20]. The default rate on Prosper.com, the largest microlending platform in the United States, is over 8.48% on average and can reach 30% if the economy experiences a recession.<sup>2</sup> In contrast, the default rate of consumer loans by commercial banks in the United States is, on average, 2.79%.<sup>3</sup> If not managed properly, a high default rate has the potential to hamper and severely damage the micro-lending market, which benefits millions of consumers.

Financial institutions generally use “hard information” such as in come, assets, and debt history to verify borrowers’ creditworthiness. For example, the Fair Isaac Corporation (FICO) combines a borrower’s credit history and debt level to determine his or her credit score, which subsequently influences the provision of credit [60]. However, bor rowers in the micro-lending market vary widely in terms of their back ground and credit history. Further, micro-lending companies often have very limited information about borrowers, and it is well known that hard information does not always provide a full picture of creditworthiness, especially for prediction purposes [45]. These realities have prompted lenders in these markets to increasingly turn to “soft information” to better understand borrowers [38].<sup>4</sup> Existing research suggests that gathering soft information is crucial for limiting lending risk when hard information is insufficient [50]. Various aspects of “soft information”, such as descriptive loan texts, lender-borrower communication, and social connections, can be extracted to predict a borrower’s credit risk [58,61]. For example, the micro-lending company Lenddo uses social network data (i.e., the number of followers a borrower has and with whom they are friends) to evaluate loan applicants.

Previous studies have increasingly focused on the role of another source of soft information, that is, calling activities, in predicting default probability in online micro-lending platforms (e.g., [42,63]). This study aims to identify common behavior-based soft information as a predictor of loan default, establish a causal link between calling activities and borrower default, and look deeper into the heterogeneous effects of calling activities. Our study is situated in mobile micro-lending, a fastgrowing segment of micro-lending that enables borrowers to initiate and finalize transactions on mobile devices such as smartphones and tablets. Theoretically, we propose that as a source of soft information, the social capital of borrowers can be measured through daily user be haviors that occur routinely on mobile devices. These measurements, together with the information traditionally used in borrower assess ment, can then be utilized to predict default risk.

Specifically, we focus on the connection between mobile phone calling activities and the likelihood of default on mobile microloans. The core argument is that social capital comes from social connections [40.51]. which prior research has demonstrated as a typical example of soft information (e.g., [39]). Calling activities on mobile phones, which have become a hub that facilitates social connections, constitute key indicators of resources and social capital [8,32]. By leveraging bor rowers’ calling activities to measure their social capital, we discern the different types of calling activities and elucidate their heterogeneous effects on borrower default. In a nutshell, our study uniquely links financial behavior on mobile devices (i.e., mobile loan default) to the primary function of these devices (i.e., phone calls).

Our results show that with any sensitive information of users pro tected, the pure patterns of incoming versus outgoing calls on mobile phones in the past are strongly correlated with the likelihood of borrower default in the future. Before borrowers sign up as users on the mobile micro-lending platform, those who receive more incoming calls in their daily lives are less likely to default in future transactions than those who make more outgoing calls. We also find that mobile phone calling activities associated with strong ties, measured by connections with people who are on the borrower’s contact list, are a more powerful predictor of default than calling activities with weak ties (i.e., people who are not on the borrower’s contact list).

This study has important theoretical contributions and practical implications. First, by advancing the knowledge of common and easily accessible behavior-based predictors of financial activities, we provide evidence for the efficacy of “soft information” in explaining and pre dicting borrower default. Most previous research relies on hard infor mation, such as demographic data or credit history, to analyze borrower defaults in the context of traditional lending. However, mobile microlending customers tend not to provide adequate hard information because of insufficient credit records and low income [14]. Fintech applications can obtain more soft information [56], especially con cerning borrowers’ social connections. In the context of mobile microlending, this study identifies a novel measure of soft informa tion—mobile phone calling activity—and demonstrates how it is con nected to borrower default.

Second, our study extends the literature on soft information augmentation to provide more accurate credit risk predictions. Drawing on social capital theory, our study establishes the causal connection between soft information and the behavior of borrowers through empirical design, in addition to revealing the role of social capital in explaining how different types of phone calls are connected to borrower default. Previous studies investigated the correlation and predictive power of soft information, and mostly adopted a data-driven approach without providing a theoretical underpin when modeling the credit risk of consumers.

Third, our study adds to the social capital literature on microlending. A small but growing body of research exploits the role of so cial capital in online micro-lending platforms such as Prosper.com (e.g., [20,39]). In contrast to these platforms where the social network of a user can be traced based on his or her user groups, mobile micro-lending platforms do not provide users with tools to socialize with each other; Therefore, it is important to identify individual behaviors that provide insights into social capital. Furthermore, we explore heterogeneities in the impact of social capital on borrower default in terms of social tie strength.

In conclusion, this study provides decision support for risk man agement. Using available and valuable information from phone calls helps lenders distinguish the risk level of the borrower through a more fine-grained partitioning of different types of phone calls, and conse quently make more effective loan decisions, which further helps them improve the quality of loan approval and reduce loan default and costs.

The remainder of this paper is organized as follows. In the next section, we discuss the related literature and provide theoretical argu ments that relate mobile calling activities to the likelihood of loan default. Next, we introduce the data, variables, and the empirical model. We then present and discuss our results. The paper concludes with theoretical and managerial implications, as well as several directions for future research.

## 2. Theoretical development

## 2.1. Research background

According to World Bank statistics, only 12% of borrowers globally can borrow money from traditional financial institutions.<sup>6</sup> There are two main reasons for this finding. First, it is often difficult to evaluate the creditworthiness of many “thin file” customers who do not have the background information typically used in loan assessments. Second, loans to these borrowers are typically small and do not compensate for the requisite transaction costs. However, the total volume of these po tential loans is substantial. Taken together, these small loans represent a large market worth of serving.

The development of Fintech has lowered the credit access barrier for riskier consumers [6] and fostered the development of micro-lending as a new industry. The key enabler of this development is that nearly 80% of people globally had a mobile phone in 2021.<sup>7</sup> In the United States, nearly 90% of people without a bank account have a mobile phone, which is also a primary tool for them to access the Internet.<sup>8</sup> Thus, it is not surprising that a growing number of companies are providing microloan services through mobile phone apps to attract more con sumers. Examples include Ledge in the United States, Paipai Dai in China, and Money Tap in India.

Providing many borrowers with convenient access to much-needed credit services, mobile micro-lending as an industry has surged in the past several years, especially in emerging markets. For example, in China, there were only ten mobile micro-lending platforms in 2010. By 2014, the number of platforms had grown to 1575 with loan origination reaching \$9 billion.

Prior research has investigated borrowers’ relationships in online communities provided on micro-lending websites (e.g., friendship net works and group memberships) to elucidate their social behaviors and default risks [20,21,39,60]. With the development of the mobile Internet, research on mobile finance has increased. However, much of this research is directed at banking and mobile payments [36,47], not mobile lending services.

The emergence and development of mobile micro-lending provide another channel for studying borrowers’ default behavior and their relationship with social capital. Consequently, new insights can be gained regarding the effect of social capital on consumers’ financial decision making. Table 1 provides a summary of related research to illustrate how our study deviates from prior work.

## 2.2. Mobile phones and social capital

In 2021, the number of mobile phone users reached 6.2 billion globally, with a penetration rate of nearly 80%.<sup>9</sup> Mobile phone data reveal rich patterns of users’ daily behavior not only on the frequency of communication but also on the intricate structure of an individual’s social network [4,53]. As a result of their prevalence, mobile phones have become an extension of consumers’ “self” [44]. They transcend the threshold of communication, improve the flexibility of interactions, and help users maintain personal relationships [8,22]. Mobile phones also facilitate access to social networks that bring about social capital (i.e., the resources embedded in social networks) [7,40]. Examining the im plications of mobile phones for people and society, Ingrams [32] pro poses that mobile phones improve an individual’s social capital in two ways: (1) as a device to increase information and communication access, including sharing information, providing advice, learning, building technical knowledge, and so on; and (2) as a facilitator of social con nectivity, including building support networks, creating social familiarity, narrowing social degrees of distance, building economic networking, enabling emotional security, and building diversity of connections.

Social capital is based on social connection [7,23,31]. Through frequent connections and communications, mobile phones are an essential tool for people to build social capital. First, mobile phones facilitate contact with others and enhance mutual affection, so that people can obtain more support and opportunities from their social networks [11,32]. Second, mobile phones not only enhance strong ties with friends and family, but also foster weak ties and expand people’s social networks and diversity, which may bring more information and new resources [24,25,32].

The unique feature of mobile phones in terms of social capital has attracted a lot of attention from researchers. For example, Stachl et al. [53] document that information about individuals’ everyday behaviors collected from smartphone data can be used to infer their Big Five personality traits, and that communication and social behavior (e.g., number of outgoing calls per day) are the most significant predictors. Harari et al. [29] use conversations, phone calls, text messages, and app use based on smartphone data to characterize the differences in social behavior.

## 2.3. Incoming versus outgoing calls

Social capital provides resources, either tangible (e.g., money and objects) or intangible (e.g., information and relationships), embedded in social networks [7,40]. We argue that different patterns of mobile phone calling activities reflect different types of social capital. The amount of incoming calls initiated by others indicates the degree of acceptance of a person in his or her social network. One major reason is socioeconomic status, which is a key resource of social capital due to reciprocity [43]. Ample evidence indicates that people with low status are more likely to make friendly overtures to those with high status [43]. Blumenstock et al. [3] argue that people with higher socioeconomic status have larger social networks and are more likely to be at the center of these networks, which enables them to receive more transfers (including financial transfers) from others than those with lower socioeconomic status.

In the context of mobile micro-lending, these insights imply that a borrower who receives more incoming calls in his or her daily life is less likely to default on loans because he or she is more likely to have his or her own resources for timely repayment. Moreover, if the loan is at maturity and the borrower does not have the funds to repay it, such a borrower (i.e., with more incoming calls than outgoing calls, and thus greater social resources) is more capable of receiving assistance from social connections for repayment. It is important to note that, in this argument, phone calls are not for particular borrowing and repaying activities. They reflect the patterns of a person’s routine communication activities. As discussed in the empirical section, the phone call activities we measure are those that occur before a user registers on a mobile platform, preceding any future transactions that may include borrowing, repaying, or default. Through these routine communication activities, phone call activities can reflect social capital in general.

## 2.4. Strong versus weak ties

Social connections can be categorized into strong ties and weak ties [2,24]. Strong ties bond relationships with spouses, parents, relatives, and friends. Weak ties bridge relationships with acquaintances, business partners, former coworkers, and employees [7]. In the context of calling activities, people on a borrower’s contact list are usually those with whom he or she often communicates and has an intimate relationship. Compared to people who are not on the contact list, people on the contact list tend to have stronger ties.

The social network literature suggests that strong ties are more accessible and can provide more support including financial assistance [59,64]. By contrast, weak ties are more effective in bringing about new and external information [24,25]. Weber and Hsee [59] point out that a person’s social network of families and friends can provide material support during economically difficult times. The literature also indicates that economically insecure people rely more on strong ties to obtain financial support and attenuate economic pressure [25]. In another study, Dufhues et al. [16] examine 41 villages in Thailand and find that strong ties had a significant and positive influence on repayment per formance. However, weak ties have no such effect. Finally, supporting the financial roles of strong ties, Zhu et al. [64] find that strong ties make people more risk-seeking because they believe they could obtain financial support if needed. Recent research suggests that firms can utilize borrowers’ social tie information to predict their default behavior [60].

Table 1  
Related research on the effects of social capital on default in financial transactions.

<table><tr><td>Paper</td><td>Context</td><td>Data source</td><td>Measurement</td><td>Method</td><td>Findings</td></tr><tr><td>Agarwal et al. [1]</td><td>Credit card</td><td>Financial institution</td><td>Demographics (age, marriage, home, mobility, etc.)</td><td>Transaction data</td><td>Default risk is lower if the borrower has greater incentive to invest social capital.</td></tr><tr><td>Dufhues et al. [16]</td><td>Formal or semiformal loans</td><td>Households</td><td>Personal network</td><td>Survey</td><td>Bonding social capital has a positive influence on repayment performance.</td></tr><tr><td>Karlan [34]</td><td>Group lending</td><td>A non-profit “village banking” organization in Ayacucho, Peru</td><td>Trust and trustworthiness</td><td>Survey</td><td>Trustworthy individuals have lower default rate.</td></tr><tr><td>Cassar et al. [10]</td><td>Group lending</td><td>Artig Business Company</td><td>Trust, helpfulness, fairness</td><td>Survey</td><td>The trust between group members helps improve repayment performance.</td></tr><tr><td>Lin et al. [39]</td><td>Online micro-lending</td><td>Prosper.com</td><td>Friendship network</td><td>Transaction data</td><td>Friendships are associated with lower default rates.</td></tr><tr><td>Freedman and Jin [20]</td><td>Online micro-lending</td><td>Prosper.com</td><td>Group membership</td><td>Transaction data</td><td>Social ties result in higher default rate except when the loan is endorsed and bid on by friends.</td></tr><tr><td>Our study</td><td>Mobile micro-lending</td><td>Mobile micro-lending company</td><td>Mobile phone calling activities</td><td>Transaction data</td><td>Social capital has both negative and positive effects on default risk.</td></tr></table>

In summary, we expect that mobile phone calling activities associ ated with strong ties (i.e., people on the borrower’s contact list versus those not on the list) have a more significant influence on borrowers default behavior than those associated with weak ties.

## 3. Data, variables, and econometric model

## 3.1. Data

One of the largest mobile micro-lending companies provided data fo our empirical analysis.<sup>10</sup> This micro-lending company, which was founded in 2013, was the first platform in China to provide micro-loan products through mobile devices, such as mobile phones and tablets. The target consumers of the micro-lending company are diverse and include many low-income and younger consumers. Following the prevalence of the use of mobile phones, the features of small amounts, low barriers and easy access attract an increasing number of consumers, making the company one of the largest mobile micro-lending companies in China. Headquartered in China, the company had nearly 25 million registered users, 18 million active users with transactions, and a total volume of 50 billion RMB (approximately \$700 million) in transactions by 2018. Borrowers access the company’s loan services through a mobile phone application. To be eligible for transactions with the company, consumers need to first download and install the app on their mobile phones and register for an account. The company had no strict appli cation requirements for borrowers’ qualifications. During registration, borrowers only need to provide several pieces of personal information, including the national identification card number, gender, education level, income, number of credit cards, and employer’s name and address (if employed). When the user applies for a loan later, the system auto matically reviews and evaluates the personal information and decides whether to grant the loan. If the loan is approved, the company normally issues it within 30 min (sometimes as fast as three minutes). Money is transferred directly to the bank account provided by the borrower. Typical loans range from 1000 RMB (approximately \$160) to 4000 RMB (\$600), with a repayment period of seven to 30 days. Repayment is a single payment.

The company provided us with information about a sample of 36,897 unique users who borrowed money from September 2013 to July 2015.<sup>11</sup> These include the date of user registration, date of borrowing activities, status of repayment, and individual information described above. As in most app installations, the platform asks for permission to access the user’s phone book during the registration process. In a pop-up window on the phone, the app states a policy in which no identifying information is collected and consumers’ private information is fully protected by law. It is important to note that the company can only obtain these data from mobile phones with the borrowers’ full consent. Moreover, because all calling data are aggregated, there is no identifying information, such as phone numbers and individual names.

To facilitate the identification and interpretation of the effects, we focus on the first borrowing activity after registration by each user. Therefore, the calling record that we use to measure social capital is the cumulative mobile phone behavior of the user before he or she registers on the app. The calling activities relate to the user’s routine calling ac tivities but not to any specific loans that can only happen after regis tration. They do not vary with subsequent repaying activities either. This provides a clean measure of routine behavior prior to the focal transaction. There are missing data on several variables that we need to control for in the analysis as the state regulation for mandatory requirement on borrowers’ qualifications only includes the national identification card and a valid phone number when a user fills in their information. These include, for example, income, education, and num ber of credit cards. After dropping missing or invalid values in various dependent and independent variables, the dataset contains a sample of 14,715 unique users.

## 3.2. Variables

The micro-lending company records the repayment due date and the actual date on which a borrower repays the loan. The difference between the actual repayment date and due date indicates whether a default occurred. A positive value indicates default, whereas a negative or zero value indicates that the borrower repaid the loan either before it was due or on the due date. In the sample, the maximum and minimum repay ment days were 331 and − 30, respectively. A value of − 30 indicates that the borrower made repayment on the same day when a 30-day loan was initiated. To focus on borrower defaults, we treat early and on-time repayments as non-defaults.

Our focal independent variables include borrowers’ frequency of calls to/from people on/not on the borrowers’ contact lists. We measure the frequency of outgoing calls by the total number of calls to other people, and the frequency of incoming calls by the number of calls from other people. As previous research has demonstrated that borrowers default behavior is also influenced by individual demographics, we control for borrowers’ age, gender, education level, monthly income, number of credit cards, and name and location of the employer [1,15,28]. To control for industry effects, each employer is classified into industry sectors following the two-digit Chinese industry classifi cation system. We dummy code whether the employer address is pro vided by the borrower. Compared with those who do not have this information (either not employed or not providing the address), the borrowers who provided the employer address could have a more stable job. We also dummy code whether the employer address (if provided) is in the same city where the borrower was born. This variable captures the migration status of a person, which has become an important economic and social factor as the workforce in China becomes increasingly mobile. It is usually the case that due to better job opportunities, migrated workers have higher earnings than those who remain in their home towns. Finally, we control for the borrower’s geographical location to account for differences in economic environments.

For a specific loan, we control for the loan amount, the time lag between registration on the platform and when the user applies for the loan (which reflects the urgency of borrowing), and the due date of borrowers’ repayment [28]. In general, the greater the borrowed amount, the higher the risk of default [17]. Table 2 reports the defini tions and summary statistics of all variables.

## 3.3. Econometric model

We now turn to estimating the heterogeneous effects of mobile phone calling activities on borrower default. Given that the key dependent variable is a count variable with a variance more than five times larger than the mean (variance = 16.86, mean = 3.08), the negative binomial model that handles over-dispersion in the count data should be used. Although the zero-inflated count data model can also be used to account for excess zeros [41], the Vuong test [57] shows that the negative binomial model outperforms the zero-inflated negative binomial model for our data.<sup>12</sup> The negative binomial count data model is also preferred to the Poisson model when the data are over-dispersed, as is the case in our data.<sup>13</sup> We follow He et al. [30] in modeling OverdueDay<sub>it</sub>, the number of days borrower i defaulted on his or her loan, which occurred in year t, as follows:

$$
\operatorname * {P r} (O v e r d u e D a y _ {i t} = k) = \frac {\Gamma (k + 1 / \delta)}{\Gamma (k + 1) \Gamma (1 / \delta)} \left(\frac {1}{1 + \delta \mu_ {i t}}\right) ^ {1 / \delta} \left(\frac {\delta \mu_ {i t}}{1 + \delta \mu_ {i t}}\right) ^ {k}
$$

<table><tr><td>Variable</td><td>Definition</td><td>Mean</td><td>SD</td><td>Min.</td><td>Max.</td></tr><tr><td>ln(FREQin)</td><td>Natural logarithm of frequency of incoming calls</td><td>4.953</td><td>1.531</td><td>0</td><td>11.029</td></tr><tr><td>ln(FERQout)</td><td>Natural logarithm of frequency of outgoing calls</td><td>5.426</td><td>1.497</td><td>0</td><td>11.594</td></tr><tr><td>ln(FREQin0)</td><td>Natural logarithm of frequency of incoming calls from people not on the borrower&#x27;s contact list</td><td>3.991</td><td>1.615</td><td>0</td><td>11.016</td></tr><tr><td>ln(FREQin1)</td><td>Natural logarithm of frequency of incoming calls from people on the borrower&#x27;s contact list</td><td>4.104</td><td>1.752</td><td>0</td><td>10.322</td></tr><tr><td>ln(FREQout0)</td><td>Natural logarithm of frequency of outgoing calls to people not on the borrower&#x27;s contact list</td><td>4.360</td><td>1.618</td><td>0</td><td>11.475</td></tr><tr><td>ln(FREQout1)</td><td>Natural logarithm of frequency of outgoing calls to people on the borrower&#x27;s contact list</td><td>4.619</td><td>1.780</td><td>0</td><td>10.638</td></tr><tr><td>Age</td><td>Borrower&#x27;s age in years</td><td>27.848</td><td>4.759</td><td>18</td><td>58</td></tr><tr><td>Male</td><td>Dummy variable that equals 1 if the gender of a borrower is male and 0 otherwise</td><td>0.879</td><td>0.327</td><td>0</td><td>1</td></tr><tr><td>College</td><td>Dummy variable that equals 1 if a borrower&#x27;s education is a bachelor&#x27;s degree above and 0 otherwise</td><td>0.192</td><td>0.394</td><td>0</td><td>1</td></tr><tr><td>NumCards</td><td>The number of a borrower&#x27;s credit cards</td><td>1.037</td><td>0.914</td><td>0</td><td>5</td></tr><tr><td>Migrant</td><td>Dummy variable that equals 1 if a borrower works away from his or her city of birth and 0 otherwise</td><td>0.498</td><td>0.500</td><td>0</td><td>1</td></tr><tr><td>WorkEast</td><td>Dummy variable that equals 1 if a borrower works in eastern China and 0 otherwise</td><td>0.650</td><td>0.477</td><td>0</td><td>1</td></tr><tr><td>WorkWest</td><td>Dummy variable that equals 1 if a borrower works in western China and 0 otherwise</td><td>0.141</td><td>0.348</td><td>0</td><td>1</td></tr><tr><td>ln(Timelag)</td><td>Natural logarithm of time lag in minutes between the time of registration on platform and the time of the applying for the loan</td><td>7.370</td><td>3.642</td><td>1.609</td><td>13.628</td></tr><tr><td>ComAddress</td><td>Dummy variable that equals 1 if a borrower fully reported his or her employer address and 0 otherwise</td><td>0.699</td><td>0.459</td><td>0</td><td>1</td></tr><tr><td>Vacation</td><td>Dummy variable that equals 1 if the due date of a borrower&#x27;s repayment is on a holiday or a weekend and 0 otherwise</td><td>0.345</td><td>0.475</td><td>0</td><td>1</td></tr><tr><td>ln(Income)</td><td>Natural logarithm of borrower&#x27;s monthly income</td><td>8.612</td><td>0.447</td><td>7.601</td><td>9.798</td></tr><tr><td>ln(Amount)</td><td>Natural logarithm of borrowed amount</td><td>6.898</td><td>0.079</td><td>5.704</td><td>6.908</td></tr><tr><td>BorrowDay</td><td>Days that a borrower decides to borrow to indicate the expectation that he or she made on his or her repayment ability</td><td>25.481</td><td>7.988</td><td>7</td><td>30</td></tr></table>

List of variables and summary statistics. Table 2

Γ[•] represents the gamma distribution, $\mu _ { i t } > 0$ is the mean of OverdueDay<sub>it</sub>, and δ is the overdispersion parameter. Eqs. (1) and (2) specify the mean of overdue days in a natural logarithmic form ac counting for different types of calling variables:

$$
\ln \mu_ {i t} = \alpha_ {0} + \alpha_ {1} \ln (F R E Q i n _ {i t}) + \alpha_ {2} \ln (F R E Q o u t _ {i t}) + \alpha_ {3} X _ {i t} + \lambda_ {t}\tag{1}
$$

the trapezoidal rule. As pointed out by Carson and Ghosh [9] and Kostov et al. [35], multicollinearity between the generated regressor and endogenous variable will arise if the assumed marginal distribution of the endogenous variable is not substantially different from its empirical distribution. To address the inefficiency problem, we follow prior research to regress the generated regressors on the respective endoge nous variables and then employ the residuals for the estimation [5].

$$
\ln \mu_ {i t} = \beta_ {0} + \beta_ {1} \ln (F R E Q i n 0 _ {i t}) + \beta_ {2} \ln (F R E Q i n 1 _ {i t}) + \beta_ {3} \ln (F R E Q o u t 0 _ {i t}) + \beta_ {4} \ln (F R E Q o u t 1 _ {i t}) + \beta_ {5} X _ {i t} + \lambda_ {t}\tag{2}
$$

We estimate Eqs. (1) and (2) by the maximum likelihood estimator. In Eq. (1), ln(FREQin ) is the natural logarithm of borrower i’s frequency of incoming calls (plus one to address the possibility of zero calls). Similarly, ln(FREQout ) measures the natural logarithm of borrower i’s frequency of outgoing calls. In $\operatorname { E q . }$ (2), l $\mathsf { n } ( F R E Q i n O _ { i t } )$ measures the nat ural logarithm of borrower i’s frequency of incoming calls from people not on his or her contact list. ln(FREQin1 ) measures the natural loga rithm of borrower i’s frequency of incoming calls from people on his or her contact list. ln(FREQout0 ) and ln(FREQout1 ) are constructed similarly for the frequency of outgoing calls. Vector $X _ { i t }$ includes the control variables. λ is the time (year) fixed effect. According to our theoretical arguments, we expect the sign of $\alpha _ { 1 }$ to be negative and the sign of $\scriptstyle \alpha _ { 2 }$ to be positive. We also expec ${ } ; { \beta } _ { 2 }$ and $\beta _ { 4 }$ to have greater effects than $\beta _ { 1 }$ and $\beta _ { 3 } ,$

## 3.4. Copula terms to control for endogeneity

As stated in Section 3.1, the calling history is the cumulative mobile phone behavior of the user before he or she registers on the app, and thus does not relate to any specific loans that can only happen after regis tration. To further eliminate the concern about reserve causality, we employ the instrument-free method introduced by Park and Gupta [49] with Gaussian copulas. Copulas are a class of functions that allow the joint distribution of endogenous variables and the error term to be constructed from the individual marginal distributions, thereby ac counting for the correlation between them. As Park and Gupta [49] suggested, the copula method provides unique advantages over the instrumental variable approach, which often suffers from validity and weak instrument issues. The instrument-free method has been increas ingly adopted in previous research [9,13,35].

Following Park and Gupta [49], we estimate the empirical distribu tion of each focal variable nonparametrically using an Epanechnikov kernel density function. We follow Silverman’s [52] suggestion to calculate the bandwidth. This results in the following regressors in Eqs. (3)–(4) and Eqs. (5)–(8) are added to Eqs. (1), (2), respectively.

$$
C _ {-} \ln (F R E Q i n _ {i t}) = \Phi^ {- 1} \left[ H _ {\ln (F R E Q i n)} \left(\ln (F R E Q i n _ {i t})\right) \right]\tag{3}
$$

$$
C _ {-} \ln (F R E Q o u t _ {i t}) = \Phi^ {- 1} \left[ H _ {\ln (F R E Q o u t)} \left(\ln \left(F R E Q o u t _ {i t}\right)\right) \right]\tag{4}
$$

$$
C _ {-} \ln (F R E Q i n 0 _ {i t}) = \Phi^ {- 1} \left[ H _ {\ln (F R E Q i n 0)} \left(\ln (F R E Q i n 0 _ {i t})\right) \right]\tag{5}
$$

$$
C _ {-} \ln (F R E Q i n 1 _ {i t}) = \Phi^ {- 1} \left[ H _ {\ln (F R E Q i n 1)} \left(\ln (F R E Q i n 1 _ {i t})\right) \right]\tag{6}
$$

$$
C _ {-} \ln (F R E Q o u t 0 _ {i t}) = \Phi^ {- 1} \left[ H _ {\ln (F R E Q o u t 0)} \left(\ln (F R E Q o u t 0 _ {i t})\right) \right]\tag{7}
$$

$$
C _ {-} \ln (F R E Q o u t 1 _ {i t}) = \Phi^ {- 1} \left[ H _ {\ln (F R E Q o u t 1)} \left(\ln (F R E Q o u t 1 _ {i t})\right) \right]\tag{8}
$$

In these equations. $\Phi ^ { - 1 }$ is the inverse of a standard normal distri: bution function. H(⋅) represents the empirical distribution function of each focal variable, which is calculated via numerical integration using

Furthermore, for identification, it is necessary that the ln(FREQin), ln (FREQout), ln(FREQin0), ln(FREQin1), ln(FREQout0) and ln(FREQout1) variables are non-normally distributed [49]. Non-normal distribution is confirmed using the Shapiro-Wilk test (ln(FREQin) = 0.939, p < 0.01; ln (FREQout) = 0.933, p < 0.01; ln(FREQin0) = 0.984, p < 0.01; ln(FRE Qin1) = 0.927, p < 0.01; ln(FREQout0) = 0.985, p < 0.01; ln(FREQ $o u t 1 ) = 0 . 9 0 9 , p < 0 . 0 1 )$

## 4. Findings

In this section, we first report the estimation results for payment overdue days using the negative binomial model, followed by the rela tive importance of social capital variables.

## 4.1. Effects of social capital on borrower default

Incoming calls vs. Outgoing calls. Table 3 presents the estimation re sults of the overdue day model defined in Eq. (1). Model 1 only accounts for the borrower’s individual characteristics and other controls related to a specific loan. In Model 2, we include two focal variables and correct for endogeneity with their respective copula terms. Chi-square test statistics provide evidence for the joint significance of the coefficients in each model.

In Model 2, the parameter estimate of the frequency of incoming calls is − 0.291, which is statistically significant at the 1% level. Thus, the frequency of incoming calls has a negative and significant effect on the number of overdue payment days. By contrast, the frequency of out going calls has a positive and significant effect on payment overdue days (with an estimated coefficient of 0.287 and a p-value less than 0.01). Calculating the incidence rate ratios of the negative binomial model, we find that, on average, a borrower with a 1% increase in the frequency of incoming calls has 25% fewer payment overdue days, while a borrower with a 1% increase in the frequency of outgoing calls has 33% more payment overdue days.

Table 3  
Effects of social capital on borrower default.

<table><tr><td>Variables</td><td>Model 1</td><td>Model 2</td></tr><tr><td>ln(FREQin)</td><td></td><td>-0.291*** (0.0717)</td></tr><tr><td>ln(FREQout)</td><td></td><td>0.287*** (0.0713)</td></tr><tr><td>Age</td><td>-0.329*** (0.00881)</td><td>-0.0302*** (0.00881)</td></tr><tr><td>Male</td><td>0.121 (0.122)</td><td>0.147 (0.122)</td></tr><tr><td>College</td><td>-0.101 (0.116)</td><td>-0.0997 (0.114)</td></tr><tr><td>NumCards</td><td>-0.152*** (0.0439)</td><td>-0.153*** (0.0438)</td></tr><tr><td>Migrant</td><td>-0.261*** (0.0868)</td><td>-0.278*** (0.0842)</td></tr><tr><td>WorkEast</td><td>-0.103 (0.108)</td><td>-0.0747 (0.104)</td></tr><tr><td>WorkWest</td><td>-0.0911 (0.134)</td><td>-0.0694 (0.128)</td></tr><tr><td>ln(Timelag)</td><td>-0.0000371 (0.0109)</td><td>-0.00199 (0.0111)</td></tr><tr><td>ComAddress</td><td>-0.0244 (0.0958)</td><td>-0.000699 (0.0927)</td></tr><tr><td>Vacation</td><td>0.239*** (0.0876)</td><td>0.242*** (0.0868)</td></tr><tr><td>ln(Income)</td><td>-0.780*** (0.0987)</td><td>-0.794*** (0.0986)</td></tr><tr><td>ln(Amount)</td><td>2.527*** (0.339)</td><td>2.530*** (0.338)</td></tr><tr><td>C_ln(FREQin)</td><td></td><td>-0.149 (0.204)</td></tr><tr><td>C_ln(FREQout)</td><td></td><td>0.349* (0.191)</td></tr><tr><td>Constant</td><td>-9.810*** (2.503)</td><td>-10.004*** (2.489)</td></tr><tr><td>Year fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Industry fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Vuong test</td><td>-4.240 (p-value = 0.990)</td><td>0.570 (p-value = 0.283)</td></tr><tr><td>Chi-square test</td><td>267.970 (p-value = 0.000)</td><td>303.170 (p-value = 0.000)</td></tr><tr><td>Observations</td><td>14,715</td><td>14,715</td></tr><tr><td>Log likelihood</td><td>-18,624.1</td><td>-18,605.4</td></tr></table>

Notes: The dependent variable is the number of payment overdue days. Robust standard errors are in parentheses. $^ { * } p < 0 . 1 0 ; ^ { * * } p < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1$

We also calculate the marginal effects and categorize borrowers into two groups based on the median frequency of incoming and outgoing calls. Compared with borrowers whose frequency of incoming calls is below the median, those above the median use 6.6 fewer overdue days to repay their loans $\Big ( \frac { 6 6 8 - 8 0 } { 8 0 } ^ { * } 0 . 9 0 = 6 . 6 \Big )$ . In terms of outgoing calls, borrowers whose frequency of outgoing calls is above the median use 6.3 more overdue days than those with fewer outgoing calls $\textstyle \left( { \frac { 1 0 4 8 - 1 3 3 * } { 1 3 3 } } 0 . 9 1 = 6 . 3 \right)$

Regarding the control variables, the signs of the estimated co efficients are as anticipated. Specifically, borrowers with more credit cards may care more about their creditworthiness and, thus, have fewer payment overdue days. In addition, borrowers who moved to another place to work had fewer payment overdue days than borrowers who did not move. The data show that approximately 80% of all migrants moved to eastern China, where economic development is at a relatively higher level than other parts of the country. Furthermore, the greater the amount borrowed, the greater number of payment overdue days. The higher the borrower’s income, the fewer his or her payment overdue days. If the due date of repayment falls in a vacation or weekend time period, there will be more payment overdue days. In summary, bor rowers who receive more incoming (outgoing) calls have a higher (lower) likelihood of defaulting. These results are robust to the control for borrower characteristics as well as year and industry fixed effects.

Strong ties vs. Weak ties. We now examine whether the effects of calling activities associated with strong ties and weak ties on borrowers default behaviors are different. As explained earlier, relative to people who are not on a borrower’s contact list, those on the contact list will have stronger ties with the borrower. Table 4 presents the estimation results of Eq. (2). In Model 2, we include four focal variables and the copula term of each focal variable. We find that only the copula term for ln(FREQout0) is significant, underscoring the importance of controlling for endogeneity in ln(FREQout0). However, in this case, endogeneity threats only lead to a more conservative estimate.

Table 4  
Effects of strong versus weak ties on borrower default.

<table><tr><td>Variables</td><td>Model 1</td><td>Model 2</td></tr><tr><td>ln(FREQin0)</td><td></td><td>-0.0449 (0.0615)</td></tr><tr><td>ln(FREQin1)</td><td></td><td>-0.283*** (0.0732)</td></tr><tr><td>ln(FREQout0)</td><td></td><td>0.0769 (0.0634)</td></tr><tr><td>ln(FREQout1)</td><td></td><td>0.268*** (0.0747)</td></tr><tr><td>Age</td><td>-0.329*** (0.00881)</td><td>-0.0335*** (0.00880)</td></tr><tr><td>Male</td><td>0.121 (0.122)</td><td>0.155 (0.120)</td></tr><tr><td>College</td><td>-0.101 (0.116)</td><td>-0.101 (0.115)</td></tr><tr><td>NumCards</td><td>-0.152*** (0.0439)</td><td>-0.153*** (0.0438)</td></tr><tr><td>Migrant</td><td>-0.261*** (0.0868)</td><td>-0.261*** (0.0849)</td></tr><tr><td>WorkEast</td><td>-0.103 (0.108)</td><td>-0.130 (0.103)</td></tr><tr><td>WorkWest</td><td>-0.0911 (0.134)</td><td>-0.110 (0.125)</td></tr><tr><td>ln(Timelag)</td><td>-0.0000371 (0.0109)</td><td>-0.00117 (0.0112)</td></tr><tr><td>ComAddress</td><td>-0.0244 (0.0958)</td><td>-0.0178 (0.0935)</td></tr><tr><td>Vacation</td><td>0.239*** (0.0876)</td><td>0.241*** (0.0874)</td></tr><tr><td>ln(Income)</td><td>-0.780*** (0.0987)</td><td>-0.797*** (0.0986)</td></tr><tr><td>ln(Amount)</td><td>2.527*** (0.339)</td><td>2.504*** (0.360)</td></tr><tr><td>C_ln(FREQin0)</td><td></td><td>-0.420 (0.438)</td></tr><tr><td>C_ln(FREQin1)</td><td></td><td>-0.109 (0.252)</td></tr><tr><td>C_ln(FREQout0)</td><td></td><td>1.331*** (0.443)</td></tr><tr><td>C_ln(FREQout1)</td><td></td><td>0.0122 (0.223)</td></tr><tr><td>Constant</td><td>-9.810*** (2.503)</td><td>-9.731*** (2.628)</td></tr><tr><td>Year fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Industry fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Vuong test</td><td>-4.240 (p-value = 0.990)</td><td>0.550 (p-value = 0.290)</td></tr><tr><td>Chi-square test</td><td>267.970 (p-value = 0.000)</td><td>335.590 (p-value = 0.000)</td></tr><tr><td>Observations</td><td>14,715</td><td>14,715</td></tr><tr><td>Log likelihood</td><td>-18,624.1</td><td>-18,595.9</td></tr></table>

Notes: The dependent variable is the number of payment overdue days. Robus standard errors are in parentheses. $^ { * } p < 0 . 1 0 ; ^ { * * } p < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1$

The parameter estimate of calling activities associated with strong ties is negative and statistically significant in Model 2, whereas that for calling activities with weak ties is insignificant. These results support our argument that compared with weak ties, borrowers with strong ties have more social support and are thus less likely to default on their loans. In terms of magnitude, a borrower with a 1% increase in the frequency of incoming calls from people on his or her contact list has 25% fewer payment overdue days. By contrast, a borrower with a 1% increase in the frequency of outgoing calls to people on his or her contact list has 31% more overdue days. The signs of the estimated coefficients of the frequencies of incoming and outgoing calls are the same as those shown in Table 3. The effects of the control variables are as expected.

## 4.2. Relative importance of social capital on default

Having explored the relationship between mobile phone calling ac tivities and borrower default, we now examine the relative importance of mobile phone calling activities on borrower default in contrast to other variables. In doing so, we isolate the contribution of each explanatory variable to pseudo-R<sup>2</sup> after controlling for endogeneity in each focal variable. We employ the relative importance analysis widely used in management, psychology, and sociology (e.g., [19,27,37]) to assess the relative explanatory power of mobile phone calling activities on borrower defaults.<sup>14</sup> We standardize the values of relative impor tance following the methods of LeBreton and Tonidandel [37] and Nimon and Oswald [46].<sup>15</sup>

The results are reported in Table 5 in which each factor is categorized into an effect category. The number of credit cards and income represent the income effect. Borrower characteristics, such as age and gender, are demographic effects. The loan amount is in its own group, and mobile phone calling activities represent the social capital effect. As Table 5 shows, income and demographic effects are the top influencers of borrower defaults. This is not surprising given the direct impact of in come and demographics on financial ability. Regarding the important effect of social capital, mobile phone calling activities account for

## Table 5

Relative importance of social capital on borrower default.

<table><tr><td rowspan="3">Groups</td><td colspan="2">Contribution (%)</td></tr><tr><td>Calling activities</td><td>Social connections</td></tr><tr><td>(1)</td><td>(2)</td></tr><tr><td>Income Effect</td><td>52.88</td><td>49.09</td></tr><tr><td>Demographics Effect</td><td>27.97</td><td>27.43</td></tr><tr><td>Loan Amount Effect</td><td>7.66</td><td>6.98</td></tr><tr><td>Social Capital Effect</td><td>11.49</td><td>16.50</td></tr><tr><td>Total</td><td>100.00</td><td>100.00</td></tr></table>

Notes: The relative important analyses in Columns (1) and (2) follow the spec ifications in Eqs. (1) and (2), respectively.

Table 7

11.49% and 16.50% of the variance in payment overdue days. Furthermore, social capital accounts for more of the variance in default behavior than the loan amount itself. Together, these findings provide strong evidence that social capital plays a critical role in borrower defaults.

## 4.3. Robustness checks

We conduct several additional analyses to test the robustness of our findings. These include using different model specifications, the social capital effect on defaulters only, and whether a borrower’s expectation of social capital influences the results.

Alternative model specification. In addition to the negative binomial model, the two-part model proposed by Cragg [12] is also applicable in the case when a large fraction of payment overdue days is zero. The first part of the model is a selection model that describes whether a borrower defaults. The second part, which is slightly different from Eqs. (1), (2), captures the number of default days, as shown in Eqs. (9), (10), respectively.

$$
\ln \left(\text { OverdueDay } _ {i t}\right) = \phi_ {0} + \phi_ {1} \ln \left(\text { FREQin } _ {i t}\right) + \phi_ {2} \ln \left(\text { FREQout } _ {i t}\right) + \phi_ {3} X _ {i t} + \lambda_ {t} + \varepsilon_ {i t}\tag{9}
$$

the borrower’s contact list have significant effects.

Defaulters only. Micro-lending companies often focus on defaulters. Thus, we estimated the models using only the sample of borrowers who defaulted. We employ the Heckman model to first account for sample selection, which arises from only including defaulters in the regression. The estimated results are shown in Table 7 where ComAddress is the exclusive variable. Again, for defaulters, their social capital, strong ties, and weak ties all demonstrate similar patterns of results to those ob tained for the full sample that includes both defaulters and nondefaulters.

Expectation of social capital. When a borrower decides to borrow money through mobile micro-lending, he or she should have some ex pectations about the repayment ability. This expectation arises, at least in part, from the borrowers’ social capital. Consequently, we check whether accounting for such expectation changes our main findings. We use a borrower’s decision on how many days to borrow as an indicator for the expectation of repayment ability. As described earlier, the repayment days can be either seven days or 30 days for this microlending company. We include the variable BorrowDay into Eqs. (1, 2) for estimation. The results show that a borrower’s expectation has a positive and statistically significant effect on his or her default behavior. More importantly, with the expectation controlled for, the effects of the

$$
\ln \left(\text { OverdueDay } _ {i t}\right) = \varphi_ {0} + \varphi_ {1} \ln \left(F R E Q i n 0 _ {i t}\right) + \varphi_ {2} \ln \left(F R E Q i n 1 _ {i t}\right) + \varphi_ {3} \ln \left(F R E Q o u t 0 _ {i t}\right) + \varphi_ {4} \ln \left(F R E Q o u t 1 _ {i t}\right) + \varphi_ {5} X _ {i t} + \lambda_ {t} + \varepsilon_ {i t}\tag{10}
$$

As Table 6 shows, accounting for default behavior with a two-step model does not change the findings. Incoming and outgoing calls exert contrary effects on borrower default, and only calls to/from people on frequency of incoming and outgoing calls remain similar to those re ported in Table 3. Moreover, the tie strength effects continue to exist.

Table 6  
Two-part model for effects of social capital and tie strength.

<table><tr><td>Variables</td><td>Model 1</td><td>Model 2</td></tr><tr><td>ln(FREQin)</td><td>-0.123*** (0.0455)</td><td></td></tr><tr><td>ln(FREQout)</td><td>0.103** (0.0468)</td><td></td></tr><tr><td>ln(FREQin0)</td><td></td><td>-0.0107 (0.0343)</td></tr><tr><td>ln(FREQin1)</td><td></td><td>-0.150*** (0.0419)</td></tr><tr><td>ln(FREQout0)</td><td></td><td>0.0166 (0.0345)</td></tr><tr><td>ln(FREQout1)</td><td></td><td>0.128*** (0.0409)</td></tr><tr><td>Age</td><td>-0.0113** (0.00491)</td><td>-0.0116** (0.00489)</td></tr><tr><td>Male</td><td>0.114* (0.0688)</td><td>0.114* (0.0686)</td></tr><tr><td>College</td><td>-0.0273 (0.0582)</td><td>-0.0327 (0.0583)</td></tr><tr><td>NumCards</td><td>-0.0632** (0.0255)</td><td>-0.0625** (0.0254)</td></tr><tr><td>Migrant</td><td>-0.0933** (0.0473)</td><td>-0.0974** (0.0473)</td></tr><tr><td>WorkEast</td><td>-0.0625 (0.0566)</td><td>-0.0722 (0.0566)</td></tr><tr><td>WorkWest</td><td>-0.0709 (0.0747)</td><td>-0.0671 (0.0747)</td></tr><tr><td>ln(Timelag)</td><td>0.000162 (0.00618)</td><td>-0.0000133 (0.00617)</td></tr><tr><td>ComAddress</td><td>0.0340 (0.0495)</td><td>0.0323 (0.0495)</td></tr><tr><td>Vacation</td><td>0.0422 (0.0466)</td><td>0.0427 (0.0466)</td></tr><tr><td>ln(Income)</td><td>-0.394*** (0.0525)</td><td>-0.401*** (0.0526)</td></tr><tr><td>ln(Amount)</td><td>1.272*** (0.214)</td><td>1.279*** (0.215)</td></tr><tr><td>C_ln(FREQin)</td><td>-0.211* (0.127)</td><td></td></tr><tr><td>C_ln(FREQout)</td><td>0.213* (0.121)</td><td></td></tr><tr><td>C_ln(FREQin0)</td><td></td><td>-0.366 (0.254)</td></tr><tr><td>C_ln(FREQin1)</td><td></td><td>-0.205 (0.145)</td></tr><tr><td>C_ln(FREQout0)</td><td></td><td>0.693*** (0.260)</td></tr><tr><td>C_ln(FREQout1)</td><td></td><td>0.0902 (0.130)</td></tr><tr><td>Constant</td><td>-3.119** (1.532)</td><td>-3.091** (1.539)</td></tr><tr><td>Year fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Industry fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>14,715</td><td>14,715</td></tr><tr><td>F-test</td><td>5.750 (p-value = 0.000)</td><td>5.610 (p-value = 0.000)</td></tr></table>

Notes: The dependent variable is the logarithm of the number of payment overdue days. Robust standard errors are in parentheses. Model 1 refers to the model defined in Eq. (9) and Model 2 refers to the model defined in Eq. (10). \*p $< 0 . 1 0 ; { ^ { * * } p } < 0 . 0 5 ; { ^ { * * } * p } < 0 . 0 1$

Heckman model for effects of social capital and tie strength.

<table><tr><td>Variables</td><td>Model 1</td><td>Model 2</td></tr><tr><td>ln(FREQin)</td><td>-0.118*** (0.0453)</td><td></td></tr><tr><td>ln(FREQout)</td><td>0.0975** (0.0465)</td><td></td></tr><tr><td>ln(FREQin0)</td><td></td><td>-0.00755 (0.0341)</td></tr><tr><td>ln(FREQin1)</td><td></td><td>-0.148*** (0.0417)</td></tr><tr><td>ln(FREQout0)</td><td></td><td>0.0132 (0.0343)</td></tr><tr><td>ln(FREQout1)</td><td></td><td>0.124*** (0.0407)</td></tr><tr><td>Age</td><td>-0.0108** (0.00486)</td><td>-0.0112** (0.00486)</td></tr><tr><td>Male</td><td>0.114* (0.0685)</td><td>0.115* (0.0682)</td></tr><tr><td>College</td><td>-0.0258 (0.0579)</td><td>-0.0311 (0.0580)</td></tr><tr><td>NumCards</td><td>-0.0581** (0.0254)</td><td>-0.0569** (0.0252)</td></tr><tr><td>Migrant</td><td>-0.0852* (0.0470)</td><td>-0.0887* (0.0469)</td></tr><tr><td>WorkEast</td><td>-0.0546 (0.0560)</td><td>-0.0638 (0.0560)</td></tr><tr><td>WorkWest</td><td>-0.0672 (0.0742)</td><td>-0.0633 (0.0742)</td></tr><tr><td>ln(Timelag)</td><td>0.000148 (0.00615)</td><td>-0.0000 (0.00614)</td></tr><tr><td>Vacation</td><td>0.0382 (0.0464)</td><td>0.0381 (0.0464)</td></tr><tr><td>ln(Income)</td><td>-0.376*** (0.0525)</td><td>-0.381*** (0.0525)</td></tr><tr><td>ln(Amount)</td><td>1.263*** (0.213)</td><td>1.269*** (0.214)</td></tr><tr><td>C_ln(FREQin)</td><td>-0.213* (0.126)</td><td></td></tr><tr><td>C_ln(FREQout)</td><td>0.208* (0.120)</td><td></td></tr><tr><td>C_ln(FREQin0)</td><td></td><td>-0.358 (0.253)</td></tr><tr><td>C_ln(FREQin1)</td><td></td><td>-0.210 (0.144)</td></tr><tr><td>C_ln(FREQout0)</td><td></td><td>0.658** (0.258)</td></tr><tr><td>C_ln(FREQout1)</td><td></td><td>0.0918 (0.130)</td></tr><tr><td>Constant</td><td>-3.0687** (1.526)</td><td>-3.027** (1.534)</td></tr><tr><td>Year fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Industry fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>14,715</td><td>14,715</td></tr><tr><td>Log likelihood</td><td>-13,633.7</td><td>-13,615.4</td></tr></table>

Notes: The dependent variable is the logarithm of the number of payment overdue days. Robust standard errors are in parentheses. ComAddress is the exclusive variable. The LR test shows that there exists the sample selection problem after considering only the defaulter’s sample at the 5% level. \*p < 0.10; $^ { * * } p < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1$

## 5. Conclusions

Predicting borrower defaults is an important yet difficult task for financial service providers [33]. Prior research on traditional financial markets concentrates on hard information to predict borrowers’ default risks. In the emerging field of micro-lending, however, and especially in mobile micro-lending, the use of soft information in predicting bor rowers’ default risk has been increasingly prevalent. Against this back drop, we examine the relationship between mobile phone calling activities and borrowers’ default risk in the mobile micro-lending mar ket. In addition, based on the theoretical perspective of social capital, we ascertain the effects of different types of mobile phone calling activities on the default risk of borrowers, which helps lenders distinguish the risk level of the borrower and make more effective loan decisions.

This study provides strong evidence for the efficacy of soft infor mation in explaining and predicting borrowers’ default risk and expands the sparse research on the relationship between social capital and credit scoring. In particular, it extends traditional studies that rely on hard information to predict borrowers’ default risk. As one of the most important types of soft information, it is difficult to infer social capital from financial data alone. Owing to the development of Fintech appli cations, networks have been created that can reveal people’s social and economic relationships [54]. We suggest that borrowers’ social capital can be reflected by information from their mobile phone calling activities.

Our research provides new evidence on how social capital affects borrowers’ default risk, a question of growing interest in the fields of information systems, economics, and management. Thus far, identifying social relationships formed outside the economic context being inves tigated remains a key challenge [26]. Mobile micro-lending, however, offers well-defined, objective measures of social capital through mobile phone calling activities that are formed outside of the lending context. We further explore the heterogeneous effects of social capital in view of different types of mobile phone calling activities.

Furthermore, our research extends the literature on social ties (e.g., [2,24]). We identify people who are or are not on the borrower’s phone contact list and distinguish the effects of these two types of people on the borrower’s default. Compared to weak ties, the relationship between strong ties is much more robust. This suggests that, although weak ties can bring new knowledge [7,24,25], financial support comes primarily from strong ties.

Micro-lending provides access to loans to people with low incomes o insufficient credit records. However, lending to the poor always suffers from high default risk [34], especially in micro-lending. Thus, control ling default risk is the primary focus of micro-lending management. Beyond the traditional practice of using hard information, an increasing number of start-up firms are attempting to use soft information to pre dict borrowers’ creditworthiness. For example, with the full consent of consumers, the Hong Kong micro-lending company Lenddo mines bor rowers’ mobile phone records and online social behavior data to eval uate their credit.

Our study demonstrates the efficacy of soft information revealed through social capital in predicting borrower defaults. We show that mobile phone calling activities can be a valuable addition to relying on hard information. To cope with fierce competition, micro-lenders must improve their loan application and approval processes. Some lenders provide loans to borrowers within just 30 min. The process of applying for loans has become much simpler than before. For example, borrowers no longer need to provide thick files to prove their creditworthiness, but are only required to fill in some basic personal information on a mobile app. While speeding up transactions, a less elaborate approval process also increases default risk. Our study suggests that lenders can benefit from utilizing readily available information about borrowers’ daily activities to help improve the quality of loan approval and reduce loan defaults and costs.

In closing, we highlight two areas that can be particularly fruitful for future research. First, this study only considers mobile phone calling activities as an indicator of borrowers’ social interactions, but ignores other mobile phone modalities in text messaging, microblogging, and social networks. To the extent that consumer privacy is protected, microlenders can identify ways to productively utilize this information. Sec ond, owing to data limitations, we could not analyze borrowers’ overall social networks in terms of structure and density. Research addressing additional indicators of social capital could deepen our ability to predict borrowers’ default risk.

## CRediT authorship contribution statement

Weihe Gao: Conceptualization, Methodology, Supervision, Writing – review & editing. Yong Liu: Conceptualization, Methodology, Su pervision, Writing – review & editing. Hua Yin: Methodology, Formal analysis, Writing – Original Draft. Yiwei Zhang: Methodology, Writing – Original Draft..

## Acknowledgement

The authors thank the Editor and reviewers for their insightful comments and suggestions, which improved the quality of this paper significantly. This work is supported by the National Natural Science Foundation of China [Grants 71872106 and 71728007] and the Key Project of the National Social Science Fund of China [Grant AZD057]. The authors are listed alphabetically and contributed equally to the paper. Corresponding author: Hua Yin, yin.hua@mail.shufe.edu.cn.

## References

[1] S. Agarwal, S. Chomsisengphet, C. Liu, Consumer bankruptcy and default: the role of individual social capital, J. Econ. Psychol, 32 (4) (2011) 632–650.

[2] Y. Bian, Bringing strong ties back in: indirect ties, network bridges, and job searches in China, Am, Sociol, Rev, 62 (3) (1997) 366–385

[3] J.E. Blumenstock, N. Eagle, M. Fafchamps, Airtime transfers and mobile communications: evidence in the aftermath of natural disasters, J. Dey. Econ. 120 (2016) 157-181.

[4] J. Blumenstock, G. Cadamuro, R. On, Predicting poverty and wealth from mobile phone metadata, Science 350 (6264) (2015) 1073–1076.

[5] P.A. Bottomley, S. Holden. Do we really know how consumers evaluate brand extensions? Empirical generalizations based on secondary analysis of eight studies. J. Mark, Res. 38 (2001) 494–500.

[6] G. Buchak, G. Matyos, T. Piskorski, A. Seru, Fintech, regulatory arbitrage, and the rise of shadow banks, J. Financ. Econ, 130 (3) (2018) 453–483.

[7] R.S. Burt, The network structure of social capital, Res. Organ. Behav. 22 (2000) 345-423.

[8] S.W. Campbell, N. Kwak, Mobile communication and social capital: an analysis of geographically differentiated usage patterns, New Media Soc. 12 (3) (2010) 435-451.

[9] S.J. Carson, M. Ghosh, An integrated power and efficiency model of contractua channel governance: theory and empirical evidence, J. Mark. 83 (4) (2019) 101–120.

[10] A. Cassar, L. Crowley, B. Wydick, The effect of social capital on group loan repayment: Evidence from field experiments, Econ. J. 117 (517) (2007) 85–106.

[11] M. Chan, Mobile phones and the good life: examining the relationships among mobile use, social capital and subjective well-being, New Media Soc. 17 (1) (2015) 96–113.

[12] J.G. Cragg, Some statistical models for limited dependent variables with application to the demand for durable goods. Econometrica 39 (1971) 829–844

[13] H. Datta, B. Foubert, H.J. Van Heerde, The challenge of retaining customers

[14] B.W. Dobbie, P.M. Skiba, Information asymmetries in consumer credit markets:

[15] J. Duarte, S. Siegel, L. Young, Trust and credit: the role of appearance in peer-topeer lending, Rev. Financ. Stud. 25 (8) (2012) 2455–2483.

[16]. T. Dufhues. G. Buchenrieder, D.G. Euler. N. Munkung. Network based social capital and individual loan repayment performance, J. Dev. Stud. 47 (8) (2011)

[17] L. Einav, M. Jenkins, J. Levin, The impact of credit scoring on consumer lending, RAND J. Econ, 44 (2) (2013) 249–274.

[18] R. Emekter, Y. Tu, B. Jirasakuldech, M. Lu, Evaluating credit risk and loan performance in online peer-to-peer (P2P) lending, Appl. Econ. 47 (1) (2015) 54–70.

[19] N. Fortin, T. Lemieux, S. Firpo, Chapter 1-decomposition methods in economics, in: A. Orley, C. David (Eds.), Handbook of Labor Economics, Elsevier, New York, 2011, pp. 1–102.

[20] S. Freedman, G.Z. Jin, The information value of online social networks, Int. J. Ind. Organ, 51 (2017) 185–222

[21] R. Ge, J. Feng, B. Gu, P. Zhang, Predicting and deterring default with social media information in peer-to-peer lending, J. Manag. Inf. Syst. 34 (2) (2017) 401–424.

[22] A. Ghose. A. Goldfarb. S.P. Han. How is the mobile internet different? Inf, Syst. Res 24 (3) (2013) 613–631.

[23] E.L. Glaeser, D. Laibson, B. Sacerdote, An economic approach to social capital, Econ. J. 112 (2002) 437–458.

[24] M. Granovetter, The strength of weak ties, Am. J. Sociol. 78 (6) (1973) 1360–1380.

[25] M. Granovetter, The strength of weak ties: a network theory revisited, Sociol. Theor, 1 (1983) 201–233.

[26] M. Granovetter, The impact of social structure on economic outcomes social networks and economic outcomes, J. Econ. Perspect. 19 (1) (2005) 33–50.

[27] U. Gromping, ¨ Estimators of relative importance in linear regression based on variance decomposition, Am. Stat, 61 (2007) 139–147.

[28] D.B. Gross, N.S. Souleles, An empirical analysis of personal bankruptcy and delinquency, Rev. Financ. Stud. 15 (1) (2002) 319–347.

[29] G.M. Harari, S.R. Müller, C. Stachl, R. Wang, W.C. Wang, M. Bühner, P.J. Rentfrow, A.T. Campbell, S.D. Gosling, Sensing sociability: individual differences in young adults’ conversation, calling, texting, and app use behaviors in daily life, J. Pers. Soc. Psychol. 119 (1) (2019) 204–208.

[30] S. He, H. Rui, A.B. Whinston, Social media strategies in product-harm crises, Inf. Syst. Res. 29 (2) (2018) 362–380.

[31] O. Hinz, M. Spann, I.H. Hann, Can’t buy me love…or can I? Social capita attainment through conspicuous consumption in virtual environments, Inf. Syst. Res. 26 (4) (2015) 859–870.

[32] A. Ingrams, Mobile phones, smartphones, and the transformation of civic behavior through mobile information and connectivity, Gov, Inf, O. 32 (4) (2015) 506–515.

[33] R. Iyer, A.I. Khwaja, E.F.P. Luttmer, K. Shue, Screening peers softly: inferring the quality of small borrowers, Manag. Sci. 62 (6) (2016) 1554–1577.

[34] D.S. Karlan, Social connections and group banking, Econ. J. 117 (2007) 52–84.

[35] P. Kostov, S. Davidova, A. Bailey, E. Gjokaj, K. Halimi, Can direct payments facilitate agricultural commercialization: evidence from a transition country, J. Agric. Econ. 72 (1) (2021) 72–96.

[36] T. Laukkanen, Consumer adoption versus rejection decisions in seemingly similar service innovations: the case of the internet and mobile banking, J. Bus. Res. 69 (7) (2016) 2432–2439.

[37] J.M. LeBreton, S. Tonidandel, Multivariate relative importance: extending relative weight analysis to multivariate criterion spaces. J. Appl. Psychol. 93 (2) (2008 329-345.

[38] J.M. Liberti, M.A. Petersen. Information: hard and soft. Rey. Corp. Financ. Stud, 8

[39] M. Lin, N.R. Prabhala, S. Viswanathan, Judging borrowers by the company they keep: friendship networks and information asymmetry in online peer-to-peer lending, Manag, Sci, 59 (1) (2013) 17–35

[40] N. Lin, Building a network theory of social capital, Connections 22 (1) (1999) 28–51.

[41] S. Long, J. Freese, Regression Models for Categorical Dependent Variables Using Data, Stata press, College Stations, 2003.

[42] L. Ma, X. Zhao, Z.L. Zhou, Y.Y. Liu, A mew aspect on P2P online lending default prediction using meta-level phone usage data in China, Decis. Support. Syst. 11 (2018) 60–71.

[43] D. Marmaros, B. Sacerdote, How do friendships form? Q. J. Econ. 121 (1) (2006) 79–119.

[44] M. McLuhan, Understanding Media: The Extensions of Man, Gingko Press, Berkeley, 2003.

[45] O. Netzer, A. Lemaire, M. Herzenstein, When words sweat: identifying signals for loan default in the text of loan application, J. Mark. Res. 56 (6) (2019) 960–980.

[46] K.F. Nimon, F.L. Oswald, Understanding the results of multiple linear regression: beyond standardized regression coefficients, Organ. Res. Methods 16 (4) (2013) 650–674.

[47] T. Oliveira, M. Thomas, G. Baptista, F. Campos, Mobile payment: understanding the determinants of customer adoption and intention to recommend the technology, Comput. Hum. Behav. 61 (2016) 404–414.

[48] M. Papouskova, P. Hajek, Two-stage consumer credit risk modelling using heterogeneous ensemble learning, Decis. Support. Syst. 118 (2019) 33–45.

[49] S. Park, S. Gupta, Handling endogenous regressors by joint estimation using copulas, Mark. Sci. 31 (4) (2012) 567–586.

[50] M.A. Petersen, R.G. Rajan, Does distance still matter? The information revolution in small business lending, J. Financ. 57 (6) (2002) 2533–2570.

[51] R.D. Putnam, Bowling alone: America’s declining social capital, J. Democr. 6 (1) (1995) 65–78.

[52] B.W. Silverman, Density Estimation for Statistics and Data Analysis, Chapman & Hall. London. 1986.

[53] C. Stachl, Q. Au, R. Schoedel, S.D. Gosling, G.M. Harari, D. Buschek, S.T. Volkel,¨ T. Schuwerk, M. Oldemeier, T. Ullmann, H. Hussmann, B. Bischl, M. Bühner, Predicting personality from patterns of behavior collected with smartphones, Proc Natl, Acad, Sci, U. S. A, 117 (2020) 17680–17687.

[54] A. Sundararajan, F. Provost, G. Oestreicher-Singer, S. Aral, Information in digital, economic, and social networks, Inf. Syst. Res. 24 (4) (2013) 883–905.

[55] H. Tang, Peer-to-peer lenders versus banks: substitutes or complements? Rev. Financ. Stud. 32 (5) (2019) 1900–1938.

[56] B. Vall´ee, Y. Zeng, Marketplace lending: a new banking paradigm? Rev. Financ. Stud, 32 (5) (2019) 1939–1982

[57] Q. Vuong, Likelihood ratio tests for model selection and non-nested hypotheses, Econometrica 57 (1989) 307–334.

[58] Z. Wang, C.Q. Jiang, H.M. Zhao, Y. Ding, Mining semantic soft factors for credit risk evaluation in peer-to-peer lending, J. Manag. Inf. Syst. 37 (1) (2020) 282–308.

[59] E.U. Weber, C. Hsee, Cross-cultural differences in risk perception, but cross-cultura similarities in attitudes towards perceived risk, Manag. Sci. 44 (9) (1998) 1205–1217.

[60] Y. Wei, P. Yildirim, C. den Bulte, C. Dellarocas, Credit scoring with social network data, Mark. Sci. 35 (2) (2016) 234–258.

[61] J.J. Xu, M. Chau, Cheap talk? The impact of lender-borrower communication on peer-to-peer lending outcomes, J. Manag. Inf. Syst. 35 (1) (2018) 53–85.

[62] J. Zhang, P. Liu, Rational herding in microloan markets, Manag. Sci. 58 (5) (2012) 892–912.

[63] J.L. Zhou, C. Wang, F. Ren, G.Q. Chen, Inferring multi-stage risk for online consumer credit services: an integrated scheme using data augmentation and model enhancement, Decis. Support. Syst. 149 (2021), 113611.

[64] R. Zhu, U.M. Dholakia, X. Chen, R. Algesheimer, Does online community participation foster risky financial behavior? J. Mark. Res. 49 (3) (2012) 394–407.

Weihe Gao (gao.weihe@mail.shufe.edu.cn) is a Professor at the College of Business, Shanghai University of Finance and Economics. He received his PhD degree in Manage ment from Shanghai Jiaotong University. His research interests include new media mar keting, marketing strategy, and innovation and business models. He has published in journals such as Journal of Marketing, Industrial Marketing Management, Asia Pacific Journa of Manggement, and others.

Yong Liu (yoliu@eller.arizona.edu) is a Professor and Robert A. Eckert Endowed Chair at the Eller College of Management, University of Arizona. He received his PhD degree in Marketing from the University of British Columbia. His research interests include inno vation and business models, media strategies and cultural product marketing, and social interactions on the internet and mobile device. He has published in journals such as Journal of Marketing, Journal of Marketing Research, Marketing Science, Management Science, and others. He is an Associate Editor of Journal of Retailing and serves on the editorial boards of Journal of Marketing, Marketing Science, and Journal of the Academy of Marketin Science.

Hua Yin (yin.hua@mail.shufe.edu.cn) is an Assistant Professor at the Research Institute for the Development of Shanghai, Shanghai University of Finance and Economics. He received his PhD degree in Economics from Southwestern University of Finance and Economics. His research interests include econometric model. consumer finance. and program evaluation. He has published in such journals as Economic Modelling, World Economy. Journal of Environmental Management. and others

Yiwei Zhang (zhangyw@sandau.edu.cn) is an Associate Professor at the School of Management, Shanghai Sanda University. He received his PhD degree in Marketing from Shanghai University of Finance and Economics. His research interests include online finance, service marketing, and consumer behavior
