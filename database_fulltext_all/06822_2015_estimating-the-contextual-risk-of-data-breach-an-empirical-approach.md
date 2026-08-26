---
otero_id: 6822
otero_key: "TGCD98NK"
title: "Estimating the Contextual Risk of Data Breach: An Empirical Approach"
authors: "Ravi Sen; Sharad Borle"
year: "2015"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2015.1063315"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Estimating the Contextual Risk of Data Breach: An Empirical Approach

Ravi Sen & Sharad Borle

To cite this article: Ravi Sen & Sharad Borle (2015) Estimating the Contextual Risk of Data Breach: An Empirical Approach, Journal of Management Information Systems, 32:2, 314-341, DOI: 10.1080/07421222.2015.1063315

To link to this article: http://dx.doi.org/10.1080/07421222.2015.1063315

![](/api/attachments/TGCD98NK/fulltext/images/2bde40f26f89cf1e92c5acdc2a11321794eb92509dfe217d012e3943d97a1e1c.jpg)

Published online: 28 Aug 2015.

![](/api/attachments/TGCD98NK/fulltext/images/a4da1c5992d831c32c4eb9939f4eed011f6094f29938356b75701064e1b9c8f7.jpg)

Submit your article to this journal

![](/api/attachments/TGCD98NK/fulltext/images/8778baddb4326d944e8cb5af4f7d690db1819bb681e18ccc7a248c6c3c612500.jpg)

Article views: 30

![](/api/attachments/TGCD98NK/fulltext/images/676562491275aed4b48dbc4c0881f24661687b30b209d78ebd9f015f29756d1b.jpg)

View related articles

![](/api/attachments/TGCD98NK/fulltext/images/9cdaf0ab88701ec2d12e393a9100012894857ab974680cb95943814a5a26a6fe.jpg)

View Crossmark data

# Estimating the Contextual Risk of Data Breach: An Empirical Approach

RAVI SEN AND SHARAD BORLE

RAVI SEN is an associate professor in the Department of Information and Operations Management at the Mays Business School, Texas A&M University. He received his Ph.D. in business administration from the University of Illinois at Urbana– Champaign. His research interests include economics of electronic commerce, open source software, and software security. He has published in the Journal of Management Information Systems, Decision Support Systems, International Journal of Electronic Commerce, Communications of the AIS, Electronic Markets, Journal of Electronic Commerce Research, and other venues.

SHARAD BORLE is an associate professor at the Jones Graduate School of Business, Rice University. He received his Ph.D. from Carnegie Mellon University. His research interests include application of Bayesian econometrics and data analytics in marketing and information science. He has published in various marketing, management, and statistics journals.

ABSTRACT: Data breach incidents are on the rise, and have resulted in severe financial and legal implications for the affected organizations. We apply the opportunity theory of crime, the institutional anomie theory, and institutional theory to identify factors that could increase or decrease the contextual risk of data breach. We investigate the risk of data breach in the context of an organization’s physical location, its primary industry, and the type of data breach that it may have suffered in the past. Given the location of an organization, the study finds support for application of the opportunity theory of crime and the institutional anomie theory in estimating the risk of data breach incidents within a state. In the context of the primary industry in which an organization operates, we find support for the institutional theory and the opportunity theory of crime in estimating risk of data breach incidents within an industry. Interestingly though, support for the opportunity theory of crime is partial. We find that investment in information technology (IT) security corresponds to a higher risk of data breach incidents within both a state and an industry, a result contrary to the one predicted by the opportunity theory of crime. A possible explanation for the contradiction is that investments in IT security are not being spent on the right kind of data security controls, a fact supported by evidence from the industry. The work has theoretical and practical implications. Theories from criminology are used to identify the risk factors of data breach incidents and the magnitude of their impact on the risk of data breach. Insights from the study can help IT security practitioners to assess the risk environment of their firm (in terms of data breaches) based on the firm’s location, its industry sector, and the kind of breaches that the firm may typically be prone to.

KEY WORDS AND PHRASES: computer crime, computer security, data breach, data theft, information security, IT security risks.

A data breach incident involves unauthorized access to sensitive, protected, or confidential data resulting in the compromise or potential compromise of confidentiality, integrity, and availability of the affected data. Sensitive, protected, or confidential data may include personal health information, personal identifiable information, trade secrets or intellectual property, and/or personal financial data. The impact of data breach incidents is significant for both the targeted organizations and the affected individuals. In a recent study by Ponemon Institute released in May $2 0 1 4 , ^ { 1 }$ the average cost per incident was estimated to be approximately \$5.9 million for organizations in the United States. For individuals, the most severe impact of data breach is identity theft, resulting in approximately \$16 billion stolen from 12.7 million identity fraud victims in 2014 [46]. An earlier study [50] estimated that the combined financial impact of identity theft was \$56 billion in 2005. A 2014 report by the Congressional Research Service estimated that 12.6 million Americans were victims of identity fraud [19]. The same report names identity theft as the dominant consumer fraud complaint to the Federal trade Commission (FTC).

Despite preventive measures taken by organizations (e.g., allocating higher budgets for IT security), laws enacted by several state governments (e.g.. state data breach notification laws), and data breach notification requirements in federal laws in the United States (e.g., Privacy Act, the Federal Information Security Management Act) to protect an individual’s personal, financial, and health data, data breach incidents continue to happen in the United States (see Figure 1).

![](/api/attachments/TGCD98NK/fulltext/images/9ad59e40c8622c920a5b61c0d4f53ff95285cfeeddb2a80309733945017d9d04.jpg)  
Figure 1. Data Breach Incidents Between 2005 and 2012  
Source: Figure was generated based on data of the Privacy Right Clearinghouse (http://www. privacyrights.org).

![](/api/attachments/TGCD98NK/fulltext/images/adfda4e6f79e61697162ffa0f397e4c3aa96df55ff8022527334cf5eeb8e6cba.jpg)  
Figure 2. Distribution of Data Breach Incidents Across Types of Target Organizations  
Source: Figure was generated based on data of the Privacy Right Clearinghouse (http://www. privacyrights.org).

These incidents are not confined to one type of data or organization. For instance, in the data breach incidents (for the United States) publicly disclosed between 2005 and 2012, personal medical data were potentially compromised in 22 percent of the cases, personal identifiable data were potentially compromised in 74 percent of the cases, and personal financial data were compromised in 22 percent of the cases.<sup>2</sup> The types of organizations targeted and the frequency of data breach incidents in such organizations during this same period are shown in Figure 2. Given the frequency of data breach incidents and their financial impact, we need to improve our understanding of the risk of such incidents.

## Motivation for the Study

The current literature in the area of computer security has predominantly focused on the financial impact of public disclosure of computer security vulnerabilities and breaches. Cavusoglu et al. [12] found that the public disclosure of computer security breach resulted in a loss of 2.1 percent of market value of the victim organization within two days of the announcement. Another study [9] investigated the impact of computer security breaches on market performance and found that firms that experience a breach of confidential information saw a 5 percent drop in their stock price whereas firms suffering a nonconfidential breach saw no such effect. Acquisti et al. [1] found that data privacy breach has a negative impact on the affected software vendors’ stock prices. More recently, Goel and Shawky [20] found that, on average, the announcement of a corporate security breach had a negative impact of about 1 percent of market value of the firm during the days surrounding the event. Hovav and D’Arcy [28, 29] examined the impact of security breaches for a limited subset of computer security incidents (viruses, worms, and denial of service). They concluded that the relative impact of different types of breaches was not clear. Telang and Wattal [55] investigated the impact of vulnerabilities disclosure and found that firms lose around 0.6 percent of their market value when the vulnerability is reported; this is equivalent to a loss of about \$0.86 billion per firm for each vulnerability disclosure. In short, the existing research on computer security breaches has predominantly focused on the impact of public disclosure of such incidents on the affected firm’s market valuation. Some studies [50] have investigated the impact of data breach disclosure laws in reducing the number of incidents of identity theft; however, these studies while providing empirical support for investment in computer security, make a limited contribution to our theoretical understanding of the risks of data breach, and provide limited insights to IT practitioners who want to prepare for future data breach incidents. More specifically, research is needed to investigate the determinants of risk of data breach incident. This study is an attempt to address this gap in information security research. We use information on data breach incidents that occurred between 2005 and 2012 in the United States to investigate the risks of these incidents. Further, we look at these risks by categorizing them across three different contexts, by industry, geography, and type of data breach. As per Gartner, a leading technology research company, the use of supplemental or contextual information (e.g., location and time) “improves security decisions at the time they are made, resulting in more accurate security decisions capable of supporting dynamic business and IT environments” (http://www.gartner.com/it-glossary/contextaware-security). To make a decision on context-aware security, a firm must understand contextual risk. This study investigates the risk of data breach for a firm in the context of it's primary industry, geographical location, and the type of data breach it may have suffered from in the past. An understanding of these risks should help IT security professionals implement controls that are tailored to a particular type of data breach, location (i.e., state) of data, and primary industry of the organization that collects and stores data.

In the following section we present the theoretical research framework, followed by the statistical model, results, and discussion of results.

## Determinants of Risk of Data Breach Incident: Relevant Theories

Before we can estimate the risk of data breach incidents we must identify the determinants of this risk. A data breach incident that results in the compromise of personal, financial, or health data is considered a crime under the existing computer security laws. Therefore, we use theories from criminology to identify the determinants of risk of data breach incidents. Specifically, we use the opportunity theory of crime and the institutional anomie theory to identify factors that could increase or decrease the risk of data breach. We also apply institutional theory to identify factors that could reduce the risk of data breach incidents.

## Opportunity Theory of Crime

Hannon [25] states that a criminal requires more than an initial motivation and lack of restraints to commit a crime. It also requires a vulnerable victim. The central assumption of this theory is that, much like other social behavior, criminal behavior is motivated by human rationality. Everything else being equal, a criminal is more likely to behave opportunistically. In the case of crimes resulting in data breach, vulnerabilities in information systems, software, and firmware provide the opportunity that potential data thieves are looking for. The following is a fairly common definition of the term “vulnerability” used in information security literature:

A universal vulnerability is a state in a computing system (or set of systems) that either (a) allows an attacker to execute commands as another user, or (b) allows an attacker to access data that are contrary to the specified access restrictions for these data, or (c) allows an attacker to pose as another entity, or (d) allows an attacker to conduct a denial of service.

As we can see from the definition, unauthorized access to data (i.e., data breach) can be caused by software vulnerabilities. For instance, in our empirical application approximately 22 percent of the data breach incidents that occurred between 2005 and 2012 were caused by outsiders through the use of malware that was introduced into the victim’s system by exploiting vulnerabilities that were present in the system. In fact, existing research has found an increase in the frequency of attacks on vulnerable systems after public disclosure of the relevant vulnerability [7]. In accordance with the opportunity theory of crime, the higher the numbers of vulnerabilities the more the opportunities for data thieves, which results in a higher risk of data breach. Conversely, fewer vulnerabilities should provide fewer opportunities to data thieves, and result in a lower risk of data breach incidents. Organizations can reduce the number of vulnerabilities in their systems by planning and managing IT security [2, 38, 45, 53, 54] and by investing in IT security [10, 14, 16, 21]. For example, investment in technical security controls (e.g., firewalls, intrusion detection systems, cryptographic systems, identity management systems, etc.) reduces the risk due to vulnerabilities as well as losses from security breaches [11, 59]. Therefore, we hypothesize that investment in IT security should reduce the risk of data breach.

## Institutional Anomie Theory

Institutional anomie theory (IAT) is a macro-level perspective on the social determinants of crime [41, 42]. IAT argues that advanced societies that assign higher priority to economic institutions (i.e., markets) than they do to other institutions (e.g., family and legal) are more conducive to crime. A basic premise of the theory is that dominance of market mechanisms encourages a materialistic goal-orientated behavior among individuals and organizations. This promotes a calculating, utilitarian orientation toward social relationships [27]. In extreme cases, this could result in the weakening of social normative controls and is likely to lead to high levels of deviant behavior such as crime. This theory has found some empirical support [51]. When applied to estimate the risk of data breach, IAT would suggest that the strength of market institutions should impact the risk of data breach. Measures of the strength of economic institutions are economic performance indicators (e.g., gross domestic product [GDP]) for any society. In fact, economic measures are commonly used in crime analysis [17, 39, 58]. Therefore, based on IAT, we can hypothesize that the economic performance indicators (i.e., measures of strength of markets) should impact criminal activities (such as data breach incidents). This could be because greater potential riches for hackers in materialistically stronger societies leads to wealthier states (within the United States) that are likely to have a greater incidence of data breaches.

While the markets dominate in United States, other institutions do have some influence on the behavior of individuals and organizations. More specifically, legal restraints are applied when any criminal activity becomes highly prevalent or has a significant impact on citizens. Data breach incidents have severe financial implications for victim organizations and could result in identity theft of U.S. residents. Therefore, laws mandating the disclosure of such incidents have been enacted by several states. These disclosure laws result in transparency, which in turn forces organizations to improve their controls for data security. This relationship between transparency and organizational behavior is explained through the prism of institutional theory.

## Institutional Theory

Transparency can be defined as timely disclosure of information [40], as the level of clarity of information [8], or as the level of accuracy of information [22]. In short, transparency is the degree to which information is disclosed, clear, and accurate. Transparency can result from voluntary action on the part of organizations or it can be mandated by law, as is the case with data breach disclosure laws. What is undisputed is that transparency can result in product quality improvements [32] and in service quality improvements [33]. Several studies have concluded that government-mandated disclosure of performance information has spurred companies to improve environmental performance [5, 26, 34, 48], food and water safety [3, 32], and surgical outcomes [13, 24, 47]. So the obvious question is why do these improvements happen? We will focus our analysis on cases in which transparency is mandated because in cases of data breach incidents, the disclosure of such incidents is mandated by law.

The rationale for mandatory information disclosure programs is to provide better information to firms’ stakeholders, including customers, investors, employees, government agencies, and interest groups. The rationale for such policies, regulations, and/or laws is that forcing organizations to reveal information to stakeholders can induce these stakeholders to bring pressure on the organizations, which in turn prompts the organizations to change their behavior [56]. Institutional theory provides a basis for studying how external pressures affect organizational behavior. For example, disclosure of a data breach incident can result in a loss of investor confidence in a firm, or a loss of reputation among customers. Such actions constitute a form of institutional pressure that can motivate some firms to improve along the metrics of information disclosed. In case of data breach disclosure, victim firms should strengthen their data security controls because such disclosure forces IT managers to focus on data security, thereby reducing their risk of a data breach incident.

Risks of data breach are likely to be different for various industries because different federal and state laws govern data protection in different industries. For example, HIPPA applies predominantly to the health-care industry, while GLB applies mostly to the financial industry. These laws require levels of transparency from firms that experience data breach incidents. According to the institutional theory, these different levels of transparency requirements result in different institutional pressures on victim organization, depending on their core industry. Therefore, the security controls implemented by organizations are likely to differ from industry to industry, thus resulting in different risks of data breach in different industries.

Laws requiring mandatory disclosure of data breach force organizations to inform law enforcement agencies about data breach incidents. The resulting investigation could lead to the arrest and prosecution of the individuals responsible for the breach. This could act as a deterrent to crimes that can cause data breach. Many criminologists have studied the deterrence effects of law in general [6, 37, 44, 49], and others have focused specifically on the deterrent effects of gun laws and crime [4, 18, 39] and capital punishment [43, 58]. While there appears to be no conclusive evidence to overwhelmingly support deterrence policies, Romanosky et al. [50] did find a significant relationship between state data breach disclosure laws and resulting incidents of identity theft.

In summary, laws requiring mandatory disclosure of data breach incidents: (a) force transparency on organizations, which prompts them to improve their data security controls, and (b) potentially deter individuals from conducting data breach. Therefore, we hypothesize that the existence of such laws should reduce the risk of data breach.

Table 1 summarizes the theoretical foundations of this study.

An important characteristic of the state laws on data breach disclosure is that residency of the consumer rather than location of the breach drive disclosure of the incident to affected individuals. Therefore, a firm that incurs a data breach must comply with the state laws of each of their affected consumers. Since the firms have to comply with state data breach disclosure laws, we will use statelevel data on the economic indicators for states and various industries within the state. However, we will use software vulnerability numbers for the entire United States since it provides opportunities to data thieves irrespective of their location. Furthermore, we will use the aggregate value for investment in IT security for all firms in the United States because this aggregate investment should reduce the number of vulnerabilities, and therefore opportunity for data theft, for all firms in the country. Figure 3 shows the conceptual model that we use to investigate the risks of data breach incidents by industry, geography, and type of breach. More specifically, the research questions addressed by this conceptual model are as follows:

Table 1. Theories Relevant to This Study

<table><tr><td>Relevant theory</td><td>Variable of interest</td><td>Impact on the risk of data breach</td></tr><tr><td rowspan="2">Opportunity theory of crime</td><td>Number of vulnerabilities discovered</td><td>Increase in the number of vulnerabilities should increase the risk of data breach</td></tr><tr><td>Investment in IT security</td><td>Reduces vulnerabilities and therefore should reduce the risk of data breach</td></tr><tr><td>Institutional anomie theory</td><td>Economic indicators</td><td>Higher value of economic indicators is correlated with higher risk of data breach</td></tr><tr><td>Institutional theory</td><td>Existence of law requiring mandatory disclosure of data breach incident</td><td>The law deters potential data thieves and requires greater transparency on the part of the organization, thereby reducing risk of data breach</td></tr></table>

![](/api/attachments/TGCD98NK/fulltext/images/f3df089b2cf9cc523bcc0b11c6705f64d5da630978f915c4eef3f1068afcfcbf.jpg)  
Figure 3. Conceptual Model: Determinants of the Risk of Data Breach Incidents

1. What is the impact of the number of publicly disclosed vulnerabilities, investment in IT security, state economic indicators, and state data breach disclosure laws on the risk of data breach incidents for a state?

2. What is the impact of the number of publicly disclosed vulnerabilities, investment in IT security, state economic indicators, and state data breach disclosure laws on the risk of data breach incident for organizations within an industry?

3. What is the impact of the number of publicly disclosed vulnerabilities, investment in IT security, state economic indicators, and state data breach disclosure laws on the risk of certain types of data breach incidents (e.g., caused by an insider)?

The next section provides details of the data used in the study.

## Data Sources and Summary Statistics

The secondary data used in the study were collected from multiple sources, described as follows.

## Privacy Rights Clearinghouse

Established in 1992, the Privacy Rights Clearinghouse in San Diego, California, is a nonprofit organization. It works as an advocacy group for consumers’ privacy rights at the local, state, and federal levels. It works to raise consumers’ awareness about the impact of technology and personal privacy, advises them on privacy protection, helps them redress their privacy-related grievances and concerns, and documents “the nature of consumers’ complaints and questions about privacy in reports, testimony, and speeches and make[s] them available to policy makers, industry representatives, consumer advocates, and the media.” Among various services that it offers, it maintains a database of data breach incidents within the United States. The details about these incidents were obtained from the Open Security Foundation (www.datalossdb.org) list-serve. Since January 2010, the source for these data breach incidents also includes Databreaches.net (www. databreaches.net), Personal Health Information Privacy (www.phiprivacy.net/), and the National Association for Information Destruction, Inc. (www.naidonline. org). In March 2012, the organization also began using the California attorney general’s list of data breach incidents.

## U.S. Bureau of Economic Analysis

The Bureau of Economic Analysis (BEA) (http://www.bea.gov/), one of the world’s leading statistical agencies, is part of the U.S. Department of Commerce, which provides economic data and produces economic statistics that enable government and business decision makers, researchers, and the U.S. public to follow and understand the performance of the country’s economy. Among the main economic data produced by the BEA is the national income and product accounts (NIPAs), which feature the estimates of GDP and related measures. We obtained the state-level economic indicators from the BEA.

## Commercial Law League of America

According to the Commercial Law League of America (CLLA) Web site (http:// www.clla.org/), “Since 1895, the CLLA has brought experienced attorneys together with credit grantors, lending institutions and other members of the commercial credit, bankruptcy and general finance industries, providing new business opportunities through networking, education, legislative advocacy and highly effective specialized legal services.” The CLLA maintains information on U.S. state laws related to data breach incident notification (www.clla.org/docu ments/breach.xls). This database was used to extract information on which U.S. states have such laws, the date these laws became effective, and the details of the laws.

## Secunia

Founded in 2002, and privately held, based in Copenhagen, Denmark, Secunia (www.secunia.com) is one of the leading IT security consulting organizations. Its expertise lies in the area of software vulnerability management. It provides its clients with services and products such as vulnerability intelligence, vulnerability assessment, and patch management. Its client list includes Fortune 500 and Global 2000 businesses, and government agencies worldwide. As a part of its product/ service portfolio, it maintains a database of software vulnerabilities announced for all types of software applications and operating systems. It continuously updates advisories to reflect new data whenever they become available. This database was used to extract information on the number of vulnerabilities discovered each year between 2005 and 2012.

## Ponemon Institute IT Security Tracking

The Ponemon Institute (www.ponemon.org) was founded in 2002 by Larry Ponemon. Headquartered in Michigan, the Ponemon Institute is a leading research center dedicated to privacy, data protection, and information security policy. Its annual consumer studies on privacy trust are widely quoted in the media and its research quantifying the cost of a data breach has become valuable to organizations seeking to understand the business impact of lost or stolen data. Its services include helping companies to meet data privacy compliance and regulatory requirements in the United States and abroad. The 2010 report from Ponemon was used to extract data on the annual IT security expenditure by U.S. firms from 2006 to 2011.

![](/api/attachments/TGCD98NK/fulltext/images/fb90bd05cbf39060c52b4f6fed24dc7afc6577d38ef50d0e8b2f85727eaa0322.jpg)  
Figure 4. Sources of Data Used to Estimate the Statistical Models

All of the data sources used in the study and the relationships between them are shown in Figure 4.

Appendix A provides a summary of data (and their corresponding variable names) extracted from the aforementioned data sources (Table A1) and the summary statistics for the variables used in the study (Table A2). For the purposes of estimation we meancenter all the variables (except the indicator variables) in our analysis.

## Statistical Models and Coefficient Estimates

## Statistical Models

The focus of this study is to investigate the risk of data breach incidents. More specifically, once a data breach incident occurs, we are interested in estimating the risk of the next such incident. Thus the dependent variable in our analysis is the time elapsed between two consecutive breaches (inter-breach-time). We investigate this inter-breach-time within a state, within an industry, and for the same type of data attacks.

## Risk of Breaches at the State Level

We model inter-breach-times at the state level using a negative binomial distribution as follows:

$$
t \_ s t a t e _ {k i} \sim N B D (\lambda_ {k i}, v),\tag{1a}
$$

where $t \_ s t a t e _ { k i }$ is the ith inter-breach-time (in days) for state $k ; \lambda _ { k i }$ is defined over the positive real line and is the mean of the negative binomial distribution (NBD); and ν is defined over the positive real line and is the dispersion parameter of the NBD distribution.

The pdf of the NBD is as follows:

$$
\operatorname * {P r} (t \_ s t a t e _ {k i}) = \frac {\Gamma (v + t \_ s t a t e _ {k i})}{\Gamma (v) \Gamma (t \_ s t a t e _ {k i} + 1)} \left(\frac {v}{v + \lambda_ {k i}}\right) ^ {v} \left(\frac {\lambda_ {k i}}{v + \lambda_ {k i}}\right) ^ {t \_ s t a t e _ {k i}},\tag{1b}
$$

where the mean of the distribution $= \lambda _ { k i }$ and variance $\begin{array} { r } { \mathbf { \lambda } = \lambda _ { k i } + \frac { \lambda _ { k i } ^ { 2 } } { \nu } } \end{array}$ . The parameter $\lambda _ { k i }$ varies across states as well as incidence of breaches and is further specified as follows:

$$
\begin{array}{l} \lambda_ {k i} = e ^ {(\lambda_ {k} + \lambda_ {1} L a w S t r i c t _ {k i} + \lambda_ {2} S e v e r i t y _ {k i} + \lambda_ {3} H o s p i t a l s _ {k} + \lambda_ {4} S T G D P _ {k i})} \\ \times e ^ {(\lambda_ {5} V U L N _ {i} + \lambda_ {6} E x p I n f o _ {i} + \lambda_ {7} l a g I T S e c _ {i} + \lambda_ {8} S T I n t e r n e t _ {k i} + \lambda_ {9} S T E d u _ {k i}).} \end{array}\tag{1c}
$$

The various explanatory variables used are described in Table A1 in Appendix A. The NBD is a flexible distribution and has found multiple applications in the social and medical sciences. The specification we use in this study has the added advantage that the parameters can be directly interpreted in terms of percentage impact on the “average” inter-breach-time, which in turn can be interpreted as the “risk” of a breach (greater inter-breach-times imply reduced risk whereas shorter inter-breach-times imply greater risk). For example, in Equation (1c), every \$1 billion increase in the state GDP (variable $S T G D P _ { k i } )$ corresponds to the interbreach-time in that state increasing by $e ^ { \lambda _ { 4 } }$ , that is, if the estimated value of the parameter $\lambda _ { 4 }$ is equal to 0.0953 then for every \$1 billion increase in the state GDP, the inter-breach-time increases by $e ^ { 0 . 0 9 5 3 } = 1 . 1$ , or 10 percent. On the other hand if the estimated value of $\lambda _ { 4 }$ is equal to –0.1054 then for every \$1 billion increase in the state GDP, the inter-breach-time increases by $e ^ { - 0 . 1 0 5 4 } = 0 . 9$ , or in other words a decrease of 10 percent.

Note that the model also has individual state-specific intercepts (the parameters $\lambda _ { k } , k = 1 , 2 , \ldots , 5 0 )$ in Equation (1c). These state specific parameters capture the impact of various unobserved factors that affect risk of data breach in a particular state. These $\lambda _ { k } \mathbf { s }$ are further “shrunk” using a Bayesian hierarchical model:

$$
\lambda_ {k} \sim N o r m a l (\alpha , \beta),\tag{1d}
$$

where the mean of the distribution = α and the variance = β. Also, because we are using the explanatory variables in their mean-centered formats, these $\lambda _ { k }$ scan be directly interpreted as the average risk of data breaches in the corresponding state.

To complete the Bayesian specification of the model (Equations [1a] through [1d]), we need to specify “priors” to various estimable parameters (ν, $\lambda _ { 1 } \mathrm { t h r o u g h } \lambda _ { 1 0 } , \alpha , \beta )$ . We specify relatively diffuse priors for all these parameters indicating a lack of sharp prior beliefs over the magnitude of the parameters. The model is estimated using an Markov chain Monte Carlo (MCMC) algorithm, which results in posterior distributions of all parameters that can then be summarized by the posterior means and posterior standard deviations.

## Risk of Breaches Within an Industry

In line with the model for risk of breach at the state level, we formulate the model to investigate risk of breaches within an industry. We use a total of seven industry sectors (as categorized by the Privacy Rights): (1) Financial and Insurance; (2) Retail & Merchant; (3) Education; (4) Government; (5) Medical and Health Care; (6) Nongovernmental organizations (NGOs); and (7) Others.

The model is specified as follows:

$$
t \_ i n d _ {k i} \sim N B D (\lambda_ {k i}, v _ {k}),\tag{2a}
$$

where $t \lrcorner n d _ { k i }$ is the ith inter-breach-time in days for industry k (a total of 7 industry sectors, $k = 1 , 2 , . . . , 7 )$ .

Further, the parameter $\lambda _ { k i }$ varies across industries as well as incidence of breaches and is specified as follows:

$$
\begin{array}{c} \lambda_ {k i} = e ^ {(\lambda_ {0 k} + \lambda_ {1 k} L a w S t r i c t _ {k i} + \lambda_ {2 k} S e v e r i t y _ {k i} + \lambda_ {3 k} S T G D P _ {k i} + \lambda_ {4 k} V U L N _ {i})} \\ \times e ^ {(\lambda_ {5 k} E x p I n f o _ {i} + \lambda_ {6 k} l a g I T S e c _ {i} + \lambda_ {7 k} S T I n t e r n e t _ {k i} + \lambda_ {8 k} S T E d u _ {k i}).} \end{array}\tag{2b}
$$

The parameter $\nu _ { k }$ also varies across industries $( k = 1 , 2 , . . . , 7 )$ . Also notice that one of the control variables Hospitals is dropped from the analysis in this model.

The interpretations from this model remain similar to those of the earlier model (in the previous section), where every unit increase in the explanatory variable corresponds to a proportional increase/decrease in the average inter-breach-time in that particular industry, as specified by exponential of the corresponding coefficient.

## Risk of Types of Data Breach Incident

As with the models in previous sections, the model to investigate the risk of types of data breach incident is specified as an NBD model. Eight types of data breach incidents (as categorized by the Privacy Rights on the basis of the cause of data breach) are considered: (1) sensitive information posted publicly (e.g., on a website), mishandled, or sent to the wrong party (e.g., via e-mail, fax, or mail); (2) electronic entry by an outside party (e.g., hacker), or malicious software (e.g., malware, spyware); (3) fraud involving debit and credit cards that is not accomplished via hacking (e.g., skimming devices at point-of-service terminals); (4) caused by an insider, that is, someone with legitimate access intentionally breaches information (e.g., an employee or contractor); (5) lost, discarded, or stolen nonelectronic records (e.g., paper documents); (6) lost, discarded or stolen mobile device (e.g., laptop, PDA, smartphone, portable memory device, CD, hard drive, data tape, etc.); (7) lost, discarded, or stolen stationary electronic device (e.g., a computer or server not designed for mobility); and (8) cause of data breach unknown.

The model is specified as follows:

$$
t \_ t y p e _ {k i} \sim N B D (\lambda_ {k i}, v _ {k}),\tag{3a}
$$

where $t \_ t y p e _ { k i }$ is the ith inter-breach-time in days for breach type k (a total of 8 types, $k = 1 , 2 , . . . , 8 )$ . The parameter $\lambda _ { k i }$ varies across types of breach as well as incidence of breach and is specified as follows:

$$
\begin{array}{c} \lambda_ {k i} = e ^ {(\lambda_ {0 k} + \lambda_ {1 k} L a w S t r i c t _ {k i} + \lambda_ {2 k} S e v e r i t y _ {k i} + \lambda_ {3 k} S T G D P _ {k i} + \lambda_ {4 k} V U L N _ {i})} \\ \times e ^ {(\lambda_ {5 k} E x p I n f o _ {i} + \lambda_ {6 k} l a g I T S e c _ {i} + \lambda_ {7 k} S T I n t e r n e t _ {k i} + \lambda_ {8 k} S T E d u _ {k i}).} \end{array}\tag{2b}
$$

The parameter $\nu _ { k }$ also varies across the types of breach $( k = 1 , 2 , . . . , 8 )$

## Coefficient Estimates

As mentioned earlier, the various models are estimated using an MCMC algorithm. The result of the estimation is a set of posterior distributions for all parameters. These posterior distributions are summarized by their means and standard deviations in Appendix B, Tables B1, B2, and B3 for the inter-breach-times at the state level, industry, and type of breaches, respectively.

## Estimation Results

## Risk of Data Breach for a State

The estimated coefficients from the model for risk of data breach for a state are provided in Table B1, Appendix B.

The institutional theory suggests that stricter laws would motivate organizations to have better data security controls in place, thereby discouraging potential data thieves. This should reduce the risk of data breach (i.e., increasing the interbreach-time). However, the coefficient $\lambda _ { 1 }$ (corresponding to the variable LawStrict) in Table B1 is not significant, which implies that we fail to find any impact of the strictness of law on risk of data breach at the state level. This could be because of aggregation when we are considering data breaches at the state level, that is, when looking at the risk of breaches at the state level we are not segregating the breaches based on the industry they target or the type of breaches they are. We do so in the subsequent models when we look at the risk of breaches by different industry classifications and type of breach. Aggregation can mask effects and this is perhaps what we are witnessing here. This is reinforced by the fact that in later models we do notice an impact of stricter laws in line with the institutional theory.

On the other hand, we find mixed support for the predictions from the opportunity theory of crime, in that the risk of data breach increases with increase in total vulnerabilities; the estimated value of $\lambda _ { 5 }$ implies that for every increase of 100 vulnerabilities (variable VULN) the inter-breach-time decreases by 7.28 percent $( 1 . 0 \mathrm { ~ - ~ } 0 . 9 2 7 2 \mathrm { ~ = ~ } 0 . 0 7 2 8 )$ , implying an increased risk of data breach. However, this impact is tempered by any increases in vulnerabilities that can be exploited to expose information (variable ExpInfo, coefficient $\lambda _ { 6 } )$ . Such vulnerabilities (ExpInfo) are typically about 20 percent of the total vulnerabilities (VULN ) in our data and this implies that the decrease of 7.28 percent in the interbreach-time because of a 100 unit increase in VULN is tempered by a corresponding increase in the inter-breach-time by $e ^ { \circ } . ^ { 0 9 4 4 / 5 } - 1 = 1 . 9$ percent because of ExpInfo.

One would also expect based on the predictions of the opportunity theory of crime that investments in IT would correspond to a decrease in risk of data breaches. However, our results show the reverse (parameter $\lambda _ { 7 } )$ , for every \$1 billion increase in the annual IT expenditure across the United States we notice an increased risk of data breach, the inter-breach-time decreases by 5.11 percent $( 1 . 0 - 0 . 9 4 8 9 = 0 . 0 5 1 1 ) .$ 3 Finally, we find support for the institutional anomie theory, which suggests that a higher value of economic indicators is correlated with a high risk of data breach. The coefficient on STGDP (parameter $\lambda _ { 4 } )$ has a negative value (–0.0013), implying that a \$1 billion increase in state GDP corresponds to a decrease of inter-breach-time by $e ^ { - 0 . 0 0 1 3 } = 0 . 9 9 8 7 _ { \cdot }$ , in other words a decrease in inter-breach-time by 0.13 percent. The other variables in the model (Severit, Hospitals; STInternet; STEdu) are primarily used as control variables.

The parameters $\lambda _ { k } , k = 1 , 2 , \ldots , 5 0$ are the state-specific intercepts and capture the impact of various unobserved factors that affect risk of data breach in a particular state. Since all other variables are mean–centered, these parameters can be interpreted as the “average” risk of data breach in that particular state. In particular, $e ^ { \lambda _ { k } }$ gives the “average” inter-breach-time in these states (when all other variables are at their mean values). Based on these calculations, Table 2 lists the states in increasing order of inter-breach-times (i.e., in decreasing order of risk of breach).

The state ranked 1 faces the highest risk and the state ranked 50 faces the lowest risk. All the ranks are given in Table 2.

<sub>tes</sub> <sub>Ranked</sub> <sub>According</sub> <sub>to</sub> <sub>T</sub><sup>heir</sup> <sup>Inherent</sup> <sup>Risk</sup> <sup>of</sup> <sup>Data</sup> <sup>Breach</sup> <sup>(av</sup>

<table><tr><td>Rank</td><td>State</td><td>Days until next breach</td><td>Rank</td><td>State</td><td>Days until next breach</td><td>Rank</td><td>State</td><td>Days until next breach</td><td>Rank</td><td>State</td><td>Days until next breach</td><td>Rank</td><td>State</td><td>Days until next breach</td></tr><tr><td>1</td><td>IN</td><td>11.8</td><td>11</td><td>NV</td><td>16.9</td><td>21</td><td>IA</td><td>20.2</td><td>31</td><td>OK</td><td>24.5</td><td>41</td><td>AR</td><td>34.0</td></tr><tr><td>2</td><td>WA</td><td>12.8</td><td>12</td><td>CO</td><td>17.0</td><td>22</td><td>VA</td><td>20.3</td><td>32</td><td>SC</td><td>26.1</td><td>42</td><td>AK</td><td>35.4</td></tr><tr><td>3</td><td>OR</td><td>13.4</td><td>13</td><td>TN</td><td>17.2</td><td>23</td><td>WI</td><td>20.8</td><td>33</td><td>RI</td><td>26.9</td><td>43</td><td>MT</td><td>35.7</td></tr><tr><td>4</td><td>OH</td><td>14.1</td><td>14</td><td>IL</td><td>17.9</td><td>24</td><td>UT</td><td>21.5</td><td>34</td><td>NE</td><td>27.0</td><td>44</td><td>ID</td><td>36.9</td></tr><tr><td>5</td><td>CT</td><td>14.7</td><td>15</td><td>MN</td><td>18.2</td><td>25</td><td>NH</td><td>21.7</td><td>35</td><td>DC</td><td>27.1</td><td>45</td><td>VT</td><td>37.1</td></tr><tr><td>6</td><td>NC</td><td>15.6</td><td>16</td><td>NY</td><td>19.0</td><td>26</td><td>LA</td><td>21.9</td><td>36</td><td>KS</td><td>28.4</td><td>46</td><td>MS</td><td>38.5</td></tr><tr><td>7</td><td>KY</td><td>15.8</td><td>17</td><td>PA</td><td>19.1</td><td>27</td><td>MO</td><td>23.1</td><td>37</td><td>WY</td><td>29.1</td><td>47</td><td>DE</td><td>40.3</td></tr><tr><td>8</td><td>GA</td><td>15.9</td><td>18</td><td>AZ</td><td>19.2</td><td>28</td><td>AL</td><td>23.7</td><td>38</td><td>NM</td><td>29.4</td><td>48</td><td>TX</td><td>58.6</td></tr><tr><td>9</td><td>FL</td><td>16.1</td><td>19</td><td>MI</td><td>19.5</td><td>29</td><td>NJ</td><td>24.1</td><td>39</td><td>ME</td><td>29.9</td><td>49</td><td>CA</td><td>60.8</td></tr><tr><td>10</td><td>MA</td><td>16.4</td><td>20</td><td>MD</td><td>19.7</td><td>30</td><td>WV</td><td>24.2</td><td>40</td><td>HI</td><td>33.1</td><td>50</td><td>SD</td><td>67.3</td></tr></table>

## Risk of Data Breach Within an Industry

The estimated coefficients from the model for risk of data breach within an industry are given in Table B2, Appendix B. We have a total of seven industry classifications (1) Financial and Insurance, (2) Retail & Merchant, (3) Education, (4) Government, (5) Medical and Health Care, (6) Nongovernmental organizations (NGOs), and (7) Others. Table B2 contains the results across these industry classifications. For the sake of easier interpretation, rather than reporting the coefficients themselves we report the impact of the coefficients $( e ^ { c o e f f } )$ in Table B2.

The coefficients $\lambda _ { 0 k } , k = 1 , 2 , \ldots , 7$ specify the inter-breach-times across various industries when all other covariates are at their “average” values. The value $e ^ { \lambda _ { 0 k } }$ gives this inter-breach-time across industries. NGOs have the highest value of this inter-breach-time (27.71 days), implying that they are the least at risk among the various industry classifications. This is understandable given that potential monetary gains from a breach at an NGO are likely to be smaller as compared to the remaining industry classifications.

The strictness of law (parameters $\lambda _ { 1 k } , k = 1 , 2 , \ldots , 7 )$ has a positive impact on the inter-breach-times (i.e., the risk reduces or the inter-breach-time increases). Though the effect is significant across four industries (and nonsignificant across the remaining three), the direction of the impact is the same across all seven industries. NGOs and medical providers tend to gain the maximum by stricter laws; stricter laws are related to an increase of 84.49 percent in the inter-breachtimes among “Medical providers” while it is related to an increase of 93.21 percent in the inter-breach-times among the NGOs. Breaches in the medical provider industry and NGOs are looked at as particularly intrusive by consumers, and stricter laws are likely to impel such medical providers to institute mechanisms to minimize the risk of breaches.

A good sign from these estimates is that more severe breaches across all these industries tend to happen with less frequency as evidenced by the coefficients $\lambda _ { 2 k }$ (the value $e ^ { \lambda _ { 2 k } }$ is greater than 1.0 across all industries). That is, the more severe breaches tend to have greater inter-breach-times.

Across these industries, the relationship of total vulnerabilities (VULN ) and vulnerabilities that can be exploited to expose information (ExpInfo) with interbreach-times is similar to that observed for the inter-breach-times within a state. Increase in total vulnerabilities increases the risk of breach across industries; however, this increased risk is mitigated by increases in ExpInfo vulnerabilities. This could be because system administrators, while prioritizing vulnerabilities that they need to address, give more attention to those vulnerabilities that could result in information exposure. As a result, these vulnerabilities are patched faster, thereby reducing their risk of exploitation by data thieves.

Another interesting aspect of the results is that all seven industries see an increased risk of breach with increased investments in IT (NGOs have an insignificant effect, but the direction of the effect is in line with other industries). This reinforces the result we obtained earlier for the risk of data breach within a state.

## Risk of Types of Data Breach Incident

The estimated coefficients from this model for risk of data breach by “types of data breach” are given in Table B3, Appendix B. A total of eight types of data breaches are considered.<sup>5</sup> As with the earlier models, for ease of interpretation we report the exponential of the lambda coefficients, which can in turn be directly interpreted as the percentage change in the inter-breach-times with every unit change in the corresponding covariate.

The $\lambda _ { 0 k } , k = 1 , 2 , \ldots , 8$ parameters indicate that the greatest risk exists for the type of breach “Lost, discarded, or stolen mobile device” [PORT] and the least risk exists for “Debit and credit card fraud that is not accomplished via hacking” [CARD], the corresponding inter-breach-times for these two types considering all other covariates at their average levels is 3.0 days and 75.3 days, respectively. The high risk of data breach due to lost, discarded, or stolen mobile devices should not surprise anyone. A recent report by the Pew Research Center finds that a majority of Americans have smartphones and almost half own tablets (http://www.pewinternet.org/fact-sheets/ mobile-technology-fact-sheet/). Furthermore, there is evidence of increasing incidents of loss of these devices due to theft [e.g., 52]. Therefore, risk of data breach due to these stolen or lost devices should be a frequent occurrence. The lowest risk of data breach is associated with debit/credit card fraud not accomplished via hacking. One possible explanation is that such incidents generally affect a few cards. For example, a lost/stolen credit or debit card will affect the primary card holder and any supplemental card holders (e.g., spouse and children). Furthermore, the affected individuals are very likely to inform the credit card company about the lost card, thereby limiting any opportunity for anyone to fraudulently use the card. Therefore, data thieves are not likely to focus on debit/credit card fraud when they can get a higher payoff by hacking into credit card databases and stealing account information in bulk, which can later be sold in the hacker underground or black markets for credit card numbers [23].

As seen in the risk of breach across industries, here too we notice a positive result that more severe breaches occur less frequently (have a greater inter-breachtime). This is because $e ^ { \lambda _ { 2 k } }$ is greater than 1.0 (wherever $\lambda _ { 2 k }$ is significant, which is for breaches of the type “Electronic entry by an outside party or malicious software” [HACK] and “Debit and credit card fraud that is not accomplished via hacking”[CARD]). Interestingly, looking at the parameters $\lambda _ { 1 k } \mathrm { w e }$ notice that “strictness of law” has a positive relationship with reducing the risk of “Sensitive information posted publicly, mishandled, or sent to the wrong party” [DISC] (the corresponding $e ^ { \lambda _ { 1 k } } = 1 . 3 5 3 9 , \mathrm { i . e . }$ , an increase in inter-breach-times of 35.39 percent); however, “strictness of law” has an opposite relationship with inter-breach-times for breaches of the type “Lost, discarded, or stolen nonelectronic records” [PHYS]. In such breaches the “stricter law” has a negative correlation with inter-breach-times (the inter-breach-time decreases by 27.72 percent). Strictness of laws would goad firms to incorporate stricter controls and this may be the reason we see a decrease in risk of DISC types of breaches. However breach of the PHYS type is primarily driven by laxity on the part of the consumer and thus is unlikely to be diminished by stricter laws; on the other hand, we may argue that with stricter laws this particular kind of breach is likely to increase in risk relative to the other types of breaches.

The impact of vulnerabilities (VULN as well as ExpInfo) is in line with the effect observed in earlier models. The risk of breach increases with increase in total vulnerabilities (VULN ), but this impact is tempered by the decrease in risk due to increases in vulnerabilities that can be exploited to expose information (ExpInfo).

As consistently seen across various models, we again see an increased risk of breach with increased investments in IT, the parameters $\lambda _ { 6 k }$ are significant across all but one type of breach, and the values $e ^ { \lambda _ { 6 k } }$ are all less than 1.

## Discussion and Conclusion

Data breach incidents have significant financial implications for the affected organizations. Therefore, it is important for organizations to understand their risk of such incidents. This study investigates the effect of state-level economic indicators, the existence of state data breach disclosure laws, software security factors, and investment in IT security on:

1. The risk of data breach incident for a state.

2. The risk of data breach incident for organizations within an industry sector.

3. The risk of data breach incident for organizations that have recently suffered from a certain type of data breach incident.

We find that the strictness of state-level data breach disclosure laws, while having a insignificant impact on the risk of data breach within a state, have a significant impact on the risk of data breach within the financial, educational, and medical industries and for the nongovernmental organization sector. In the affected industries, the strictness of state-level data breach disclosure laws is directly correlated with the reduced risk of data breach within these industries. One conclusion that public policymakers can draw from this result is that stricter laws on data breach notifications benefit consumers because they lead to reduced risk of data breach. However, before jumping to this conclusion, policymakers should be warned of some unintended consequences of such a move. Data disclosure laws mandate a minimal security requirement. As a result, to meet these security requirements, organizations may be motivated to outsource security protections to managed security service providers (MSSPs) to benefit from the security expertise of the MSSP and to reduce their cost of complying with the stricter laws. This adds another risk to the organizations’ data, that is, system interdependency risk [30]. The greaer the number of clients an MSSP serves, the greater the system interdependency risk, which results in overall reduced social welfare [30]. Furthermore, stricter legal security requirements can also cause “security-related stress” to the employees of the affected organizations [15], which could have an adverse impact on data security. Finally, existing studies have found that operationally mature organizations are more likely to be motivated by actual security considerations than by compliance with the legal requirements, and operationally immature firms are primarily motivated by compliance [36]. Therefore, if public policy requires strict laws to improve data security, the laws should be targeted at operationally immature firms.

Another key result from this study is that investment in IT security is correlated with a higher risk of data breach within both a state and industry sectors. This result is counter to what is expected according to the opportunity theory of crime. One explanation for this result could be that firms are investing inefficiently in information security management [60]. For instance, firms could be investing a major part of their IT budget on technical controls (e.g., firewalls, antivirus software, intrusion detection systems, etc.), at the expense of administrative and physical controls. This assertion is supported by a survey of 1,500 companies by Gartner, which found that 45 percent of the IT security budget is spent on hardware and software [35]. These additional technical security controls are not necessarily more secure than the underlying systems that they are protecting. In fact, several of these security software applications may themselves have vulnerabilities (http://www.ivizsecurity.com/blog/penetration-testing/vulnerabil ities-in-security-products-increasing-at-37-cagr/), which would increase the opportunities available to data thieves. Finally, the companies are not spending the IT security budget on the right technical controls that protect primarily against data breach [31]. In short, just investing in IT security does not guarantee reduced risk of data breach, unless the expenditure is on the right type of security controls, that is, administrative, technical, and physical. This kind of analysis becomes important given the fact that recent data breach incidents at Target and Neiman Marcus seem to have motivated companies to spend more on IT security [57].

For IT security practitioners, this research and the insights offered by the study allow an organization to assess the risk environment (in terms of data breaches) based on its location (i.e., state in which it is located), its industry sector, and the kind of breaches that the firm may typically be prone to. Based on these risk assessments and the factors contributing to the risks, it can decide on its investment in preventive controls that would minimize such risks. An organization thinking of outsourcing its data center or investing in its own data center can estimate the risk of data breach in various states; it could also focus specifically on data breach caused by hackers to decide on its investments in preventive measures. Figure 5a provides the survival curves based on model estimates for the risk of data breaches across three states. The vertical axis is the probability of the next data breach and the horizontal axis is the number of days until the next data breach in that state.

Figure 5b provides similar survival curves but for the risks associated across various industry classifications. Notice that there is considerable heterogeneity across states and industry classifications and this can be informative to a firm doing business in a particular state in a particular industry.

![](/api/attachments/TGCD98NK/fulltext/images/3ea1bb526d6a32fb195559202045138593a3e733dbfa5647ad12de187b5b158a.jpg)  
Figure 5a. Survival Estimates for the Risk of Data Breach for a State

![](/api/attachments/TGCD98NK/fulltext/images/d8bd4909c5775129a18f5e52d0e5b1b4c81d2e0413df49f6e6d86b36f82303ef.jpg)  
Figure 5b. Survival Estimates for the Risk of Data Breach for Different Industry Classifications

Finally, the study contributes to our theoretical understanding of: (a) the deterrence impact of data breach disclosure laws on the risk of data breach; (b) the determinants of data breach; and (c) the impact of vulnerability disclosure on the risk of data breach.

We also put our study results in the context of a theoretical research framework; specifically, we use theories from criminology to identify the determinants of risk of data breach incidents and find some support for these theories. More research is required to explore these theories and their relevance to risk of data breaches.

The empirical study in our work is based on secondary data. Although in the model we control for various unobserved factors by way of fixed effects, one should be careful regarding a strict casual interpretation of our results in various contexts. It is necessary to replicate more such studies in different contexts so as to make more robust inferences.

## NOTES

1. The 2014 Cost of Data Breach Study: United States, Ponemon Institute, May 2014.

2. The percentage of cases for the type of data compromised adds up to more than 100 percent because in some incidents two or more types of data were compromised

3. We also ran an estimation with the current values of IT investments rather than lagged values. The direction of results was the same.

4. We also ran the estimation with current values of IT investments. The direction of results was the same.

5. These eight types are listed in the section on “Risk of Types of Data Breach Incident.”

## REFERENCES

1. Acquisti, A.; Friedman, A.; and Telang, R. Is there a cost to privacy breaches? An event study. Fifth Workshop on the Economics of Information Security. Cambridge, June 26–28, 2006.

2. Beattie, S.; Cowan, C.; Wagle, P.; and Wright C. Timing the application of security patches for optimal uptime. Proceedings of LISA 2002: 16th Systems Administration Conference. Philadelphia, 2002, pp. 101–110.

3. Bennear L.S.; Olmstead S.M. The impacts of the “right to know”: Information disclosure and the violation of drinking water standards. Journal of Environmental Economics and Management, 56, 2 (2008), 117–130.

4. Black, D.A., and Nagin, D.S. Do right-to-carry laws deter violent crime? National Consortium on Violence Research. Carnegie Mellon University, 1996.

5. Blackman A.: Afsah, S.; and Ratunanda D. How do public disclosure pollution control programs work? Evidence from Indonesia. Human Ecology Review, 11, 3 (2004), 235–246.

6. Blumstein, A.; Cohen, J.; and Nagin, D. Deterrence and incapacitation: Estimating the effects of criminal sanctions on crime rates, report of the panel of deterrence and incapacitation. National Academy of Sciences, Washington, DC, 1978.

7. Browne, H.K.; Arbaugh, W. A.; McHugh, J.; and Fithern, W.L. A trend analysis of exploitations. University of Maryland CMU Technical Reports, 2000.

8. Bushman, R.; Piotroski, J.; and Smith, A. What determines corporate Transparency? Journal of Accounting Research, 42, 2 (2004), 207–252.

9. Campbell, K.; Gordon, L.A.; Loeb, M.; and Zhaou, L. The economic cost of publicly announced information security breaches: Empirical evidence from the stock market. Journal of Computer Security, 11, 3 (2003), 431–448.

10. Cavusoglu, H.; Mishra, B.; and Raghunathan S. A framework for evaluating IT security investments. Communications of the ACM, 47, 7 (2004), 87–92.

11. Cavusoglu, H; Mishra, B.; and Raghunathan S. The value of intrusion detection systems (IDSs) in information technology (IT) security. Information Systems Research, 16, 1 (2005), 28–46.

12. Cavusoglu, H.; Mishra, B.; and Raghunathan, S. The effect of Internet security breach announcements on market value: Capital market reactions for breached firms and

Internet security developers. International Journal of Electronic Commerce, 9, 1 (2004), 70–104.

13. Cutler, D.M.; Huckman, R.S.; Landrum, M.B. The role of information in medical markets: An analysis of publicly reported outcomes in cardiac surgery. American Economic Review, 94, 2 (2004), 342–346.

14. D’Aqostino, D. Insuring security. CIO Insight, July 31, 2013. www.cioinsight.com/c/a/ Past-News/Insuring-Security/ (accessed June 20, 2015).

15. D’Arcy, J.; Herath, T.; and Shoss, M.K. Understanding employee responses to stressful information security requirements: A coping perspective. Journal of Management Information Systems, 31, 2 (2014), 285–318.

16. Doll, M. Security & Technology Solutions: The 2002 Ernst & Young Digital Security Overview: An Executive Guide and Diagnostic. Dover, DE: Ernst & Young LLP, 2002.

17. Donohue, J., and Ayres, I. Shooting down the “More guns, less crime” hypothesis. Stanford Law Review, 51, 4 (2003), 1194–1312.

18. Donohue, J. Guns, crime, and the impact of state right-to-carry laws. Fordham Law Review, 73 (2004), 622–652.

19. Finklea, K. Identity theft: Trends and issues. Congressional Research Service, January 16, 2014.

20. Goel, S., and Shawky, H.A. Estimating the market impact of security breach announcements on firm values. Information and Management, 46, 7 (2009), 404–410.

21. Gordon, L.A., and Loeb, M.P. The economics of information security investment. ACM Transactions on Information and System Security, 5, 4 (November 2002), 438–457.

22. Granados, N.; Gupta, A.; and Kauffman, R. 2006. The impact of IT on market information and transparency: A unified theoretical framework. Journal of the Association for Information Systems, 7, 3 (2006) 148–178.

23. Hackett, R. Online, a bazaar bursting with stolen credit card information. Fortune, September 21, 2014.

24. Hannan, E. L.; Kilburn, H., Jr.; Racz, M.; Shields, E.; and Chassin, M.R. Improving the outcomes of coronary artery bypass surgery in New York State. Journal of the American Medical Association, 271, 10 (1994), 761–766.

25. Hannon, L. Criminal opportunity theory and the relationship between poverty and property crime. Sociological Spectrum, 22, 3 (2002), 363–381.

26. Henriques, I., and Sadorsky, P. The determinants of an environmentally responsive firm: An empirical approach. Journal of Environmental Economics and Management, 30, 3 (1996), 381–395.

27. Hirschman, A.O. Rival Views of Market Society and Other Recent Essays. Cambridge, MA: Harvard University Press, 1992.

28. Hovav, A., and D’Arcy, J. Capital market reaction to defective IT products: The case of computer viruses. Computers and Security, 24, 5 (2005), 409–424.

29. Hovav, A., and D’Arcy, J. The impact of virus attack announcements on the market value of firms. Information Systems Security, 13, 3 (2004), 32–40.

30. Hui, K.; Hui, W.; and Yue, W.T. Information security outsourcing with system interdependency and mandatory security requirement. Journal of Management Information Systems, 29, 3 (Winter 2012), 117–156.

31. Hulme, V.G. Security budgets are on the rise, yet secure results aren’t: It’s time for security teams to change that for the better. CSO Online, May 12, 2014. www.csoonline.com/article 2153713/security-leadership/how-to-optimize-your-security-budget.html (accessed June 20, 2015).

32. Jin, G., and P. Leslie. The effect of information on product quality: Evidence from restaurant hygiene grade cards. Quarterly Journal of Economics, 118, 2 (2003), 409–451.

33. Jung, K. The impact of information disclosure on quality of care in HMO markets. International Journal of Quality Health Care, 22, 6 (December 2010), 461–468.

34. Khanna M., and Anton W.Q. Corporate environmental management: Regulatory and market-based pressures. Land Economics, 78, 4 (2002), 539–558.

35. Kirk, J. How much should you spend on IT security? IDG News Service, September 22, 2010. www.infoworld.com/article/2626219/security/how-much-should-you-spend-on-itsecurity-.html (accessed June 20, 2015).

36. Kwon, J., and Johnson, M.E. Health-care security strategies for data protection and regulatory compliance. Journal of Management Information Systems, 30, 2 (Fall 2013), 41–66.

37. Levitt, S.D. Why do increased arrest rates appear to reduce crime: Deterrence, incapacitation, or measurement error? NBER Working Paper no. W5268, September 1995.

38. Loch, K.D.; Carr, H.C.; and Warkentin, M.E. Threats to information Systems: Today’s reality, yesterday’s understanding. MIS Quarterly, 16, 2 (June 1992), 173–186.

39. Lott, J.R., Jr. and Mustard, D.B. Crime, deterrence and the right-to-carry concealed handguns. University of Chicago: Journal of Legal Studies, 26, 1 (January 1997), 1–68.

40. Madhavan, A.; Porter, D.; and Weaver, D. Should securities markets be transparent? Journal of Financial Markets, 8, 3 (2005), 265–287.

41. Messner, S.F., and Rosenfeld, R. Crime and the American Dream. 4th ed. Belmont, CA: Thomson Wadsworth, 2007.

42. Messner, S.F.; Thome, H.; and Rosenfeld, R.Institutions, anomie, and violent crime: Clarifying and elaborating institutional-anomie theory. International Journal of Conflict and Violence, 2, 2 (2008), 163–181

43. Mocan, H.N., and Gittings, K. Getting off death row: Commuted sentences and the deterrent effect of capital punishment. Journal of Law and Economics, 46, 2 (October 2003), 453–478.

44. Nagin, D. Criminal deterrence research at the outset of the twenty-first century. Crime and Justice, 23 (1998), 1–42.

45. Niederman, F.; Brancheau, J.C.; and Wetherbe,J.C. Information systems management issues for the 1990s. MIS Quarterly, 15, 4 (December 1991), 475–500.

46. Pascual, A., and Miller, S. Identity fraud report protecting vulnerable populations. Javelin Strategy and Research, March 2015. http://securityaffairs.co/wordpress/34449/cybercrime/javelin-study-2015-identity-fraud.html (accessed June 30, 2015).

47. Peterson, E.D.; DeLong, E.R.; Jollis, J.G.; Muhlbaier, L.H.; and Mark, D.B. The effects of New York’s bypass surgery provider profiling on access to care and patient outcomes in the elderly. Journal of the American College of Cardiology, 32, 4 (October 1998), 993–999.

48. Reid, E.M., and Toffel, M.W. Responding to public and private politics: Corporate disclosure of climate change strategies. Strategic Management Journal, 30, 11 (2009), 1157–1178.

49. Robinson, P.H., and Darley, J.M. The role of deterrence in the formulation of criminal law rules: At its worst when doing its best. Georgetown Law Journal, 91, 2003, 949–1002.

50. Romanosky, S.; Telang, R.; and Acquisti, A. Do data breach disclosure laws reduce identity theft? Journal of Policy Analysis and Management, 30, 2 (2011), 256–286.

51. Savolainen, J. Inequality, welfare state, and homicide: Further support for the institutional anomie theory. Criminology, 38, 4 (2000), 1021–1042.

52. Scherer, M. Law enforcement sounds alarm on cell-phone-theft epidemic. TIME, March 25, 2013.

53. Straub, D.W. Effective IS security: An empirical study. Information Systems Research, 1, 3 (1990), 255–276.

54. Straub, D.W., and Welke, R.J. Coping with systems risk: Security planning models for managerial decision making. MIS Quarterly, 22, 4 (December 1998), 441–469.

55. Telang, R., and Wattal, S. An empirical analysis of the impact of software vulnerability announcements on firm stock price. IEEE Transactions on Software Engineering, 33, 8 (2007), 544–557.

56. Weil D.; Fung, A.; Graham, M.; and Fagotto E. The effectiveness of regulatory disclosure. Journal of Policy Analysis and Management, 26, 1 (2006), 155–181.

57. Wheeler, J.A. IT security budgets rise as data breach fear spreads. Gartner Blog Network, February 28, 2014. blogs.gartner.com/john-wheeler/it-security-budgets-rise-as-databreach-fear-spreads/ (accessed June 20, 2015).

58. Wolfers, J., and Donohue, J.J. Uses and abuses of empirical evidence in the death penalty debate. CEPR Discussion Paper no. 5493, February 2006.

59. Yeh, Q., and Chang, A.J. Threats and countermeasures for information system security: A cross-industry study. Information and Management, 44, 5 (2007), 480–491.

60. Zhao, Xia; Xue, L.; and Whinston, A.B. Managing interdependent information security risks: Cyberinsurance, managed security services, and risk pooling arrangements. Journal of Management Information Systems, 30, 1 (Summer 2013), 123–152.

## Appendix A: Data and Variables

<table><tr><td colspan="3">Table A1. Data used in the Study</td></tr><tr><td>Variable name</td><td>Data description</td><td>Variable coding</td></tr><tr><td colspan="3">Data Breach Disclosure Law</td></tr><tr><td>LawStrict</td><td>Whether a state has a strict data breach disclosure law on the date of the data breach incident</td><td>1 for a strict law, 0 otherwise</td></tr><tr><td colspan="3">State-level economic indicators</td></tr><tr><td>STGDP</td><td>State GDP (in $billions)</td><td>In $billions</td></tr><tr><td colspan="3">Software security</td></tr><tr><td>VULN</td><td>Number of total new vulnerabilities publicly disclosed per year</td><td>Actual vulnerability count in hundreds</td></tr><tr><td>ExpInfo</td><td>Number of new vulnerabilities that can be exploited to expose information per year</td><td>Actual vulnerability count in hundreds</td></tr><tr><td colspan="3">IT management</td></tr><tr><td>lagITSec</td><td>Lag of annual expenditure on information/computer/IT security</td><td>Actual dollar amount in $millions</td></tr><tr><td colspan="3">Control variables</td></tr><tr><td>Severity</td><td>This is a proxy variable we create to capture how severe the data breach is. This variable takes a value 0, 1, 2, or 3 depending on whether none, one, two, or all three types of data (medical, personal, financial) have been breached</td><td>0, 1, 2, or 3 depending on whether none, one, two or all three types of data (medical, personal, financial) have been breached</td></tr><tr><td>Hospitals</td><td>Total number of hospitals in the state</td><td>Actual number of hospitals</td></tr><tr><td>STInternet</td><td>Internet penetration in a state</td><td>0 to 100%</td></tr><tr><td>STEdu</td><td>Percentage of &gt;25-year-olds with a college degree or higher in the state</td><td>0 to 100%</td></tr><tr><td colspan="3">Sources: For software security—Secunia Advisory and Vulnerability Database; for IT management —Ponemon Institute IT Security Tracking;</td></tr></table>

<table><tr><td>Variable name</td><td colspan="4">Summary statistics</td></tr><tr><td colspan="5">Data Breach Disclosure Law</td></tr><tr><td>LawStrict</td><td colspan="4">20 percent of all data breach incidents across states happened with a strict data breach disclosure law in place in the state on the date of data breach incident</td></tr><tr><td colspan="5">State-level economic indicators</td></tr><tr><td></td><td>Mean</td><td>Std. dev.</td><td>Minimum</td><td>Maximum</td></tr><tr><td>STGDP in $billions</td><td>670.75</td><td>584.18</td><td>23.61</td><td>2,009.94</td></tr><tr><td colspan="5">Software security</td></tr><tr><td>VULN in hundreds</td><td>51.50</td><td>7.46</td><td>40.07</td><td>61.95</td></tr><tr><td>ExpInfo in hundreds</td><td>10.17</td><td>1.90</td><td>6.93</td><td>14.69</td></tr><tr><td colspan="5">IT management</td></tr><tr><td>lagITSec in $ millions</td><td>54.38</td><td>13.82</td><td>36</td><td>76</td></tr><tr><td colspan="5">Control variables</td></tr><tr><td>Severity</td><td>1.18</td><td>0.68</td><td>0</td><td>3</td></tr><tr><td>Hospitals</td><td>172.6</td><td>118.4</td><td>9</td><td>420</td></tr><tr><td>STInternet</td><td>74.2%</td><td>6.5%</td><td>52.8%</td><td>87.9%</td></tr><tr><td>STEdu</td><td>29.3%</td><td>5.5%</td><td>16.5%</td><td>53%</td></tr></table>

Table A2. Summary Statistics for the Variables Used in the Study

## Appendix B: Coefficient Estimates

Table B1. Risk of Breaches at the “State” Level

<table><tr><td>Variables</td><td>Coefficient</td><td>Estimate</td><td>exp (estimate)</td></tr><tr><td> $LawStrict_{ki}$ </td><td> $\lambda_1$ </td><td>0.0453(0.402)</td><td>1.0463</td></tr><tr><td> $Severity_{ki}$ </td><td> $\lambda_2$ </td><td>0.0269(0.163)</td><td>1.0273</td></tr><tr><td> $Hospitals_k$ </td><td> $\lambda_3$ </td><td>-0.0037(0.018)</td><td>0.9963</td></tr><tr><td> $STGDP_{ki}$ </td><td> $\lambda_4$ </td><td>-0.0013(0.000)</td><td>0.9987</td></tr><tr><td> $VULN_i$ </td><td> $\lambda_5$ </td><td>-0.0756(0.000)</td><td>0.9272</td></tr><tr><td> $ExpInfo_i$ </td><td> $\lambda_6$ </td><td>0.0944(0.000)</td><td>1.0990</td></tr><tr><td> $lagITSec_i$ </td><td> $\lambda_7$ </td><td>-0.0524(0.000)</td><td>0.9489</td></tr><tr><td> $STInternet_{ki}$ </td><td> $\lambda_8$ </td><td>0.0298(0.001)</td><td>1.0302</td></tr><tr><td> $STEdu_{ki}$ </td><td> $\lambda_9$ </td><td>-0.0552(0.000)</td><td>0.9463</td></tr></table>

Note: Equivalent p-values given in parentheses. Italicized values represent significant results.

<table><tr><td rowspan="2">Variables</td><td rowspan="2">Coeff.</td><td>Other businesses</td><td>Financial and Insurance services</td><td>Retail merchants</td><td>Educational institutions</td><td>Government and military</td><td>Medical providers</td><td>NGOs and nonprofit organizations</td></tr><tr><td>Exp (coeff.)</td><td>Exp (coeff.)</td><td>Exp (coeff.)</td><td>Exp (coeff.)</td><td>Exp (coeff.)</td><td>Exp (coeff.)</td><td>Exp (coeff.)</td></tr><tr><td rowspan="2"> $LawStrict_{ki}$ </td><td> $e^{\lambda_{0k}}$ </td><td>5.9868(0.000)</td><td>5.4447(0.000)</td><td>6.8738(0.000)</td><td>4.2105(0.000)</td><td>4.4161(0.000)</td><td>2.9103(0.000)</td><td>27.7136(0.000)</td></tr><tr><td> $e^{\lambda_{1k}}$ </td><td>1.1331(0.242)</td><td>1.3230(0.033)</td><td>1.0641(0.394)</td><td>1.2486(0.072)</td><td>1.1684(0.162)</td><td>1.8449(0.000)</td><td>1.9321(0.053)</td></tr><tr><td> $Severity_{ki}$ </td><td> $e^{\lambda_{2k}}$ </td><td>1.1784(0.037)</td><td>1.0301(0.359)</td><td>1.1335(0.091)</td><td>1.1375(0.036)</td><td>1.0196(0.372)</td><td>1.2216(0.001)</td><td>1.1133(0.326)</td></tr><tr><td> $STGDP_{ki}$ </td><td> $e^{\lambda_{3k}}$ </td><td>0.9999(0.326)</td><td>0.9999(0.255)</td><td>1.0001(0.355)</td><td>1.0000(0.471)</td><td>1.0000(0.409)</td><td>0.9998(0.026)</td><td>0.9998(0.211)</td></tr><tr><td> $VULN_{i}$ </td><td> $e^{\lambda_{4k}}$ </td><td>0.9019(0.000)</td><td>0.8694(0.000)</td><td>0.9178(0.002)</td><td>0.9607(0.005)</td><td>0.8748(0.000)</td><td>0.9407(0.014)</td><td>0.9529(0.282)</td></tr><tr><td> $ExpInfo_{i}$ </td><td> $e^{\lambda_{5k}}$ </td><td>1.1120(0.006)</td><td>1.2427(0.000)</td><td>1.1099(0.032)</td><td>1.0473(0.084)</td><td>1.1757(0.000)</td><td>1.0165(0.327)</td><td>1.0507(0.328)</td></tr><tr><td> $lagITSec_{i}$ </td><td> $e^{\lambda_{6k}}$ </td><td>0.9333(0.000)</td><td>0.9272(0.000)</td><td>0.9240(0.000)</td><td>0.9828(0.031)</td><td>0.9361(0.000)</td><td>0.9236(0.000)</td><td>0.9638(0.189)</td></tr><tr><td> $STInternet_{ki}$ </td><td> $e^{\lambda_{7k}}$ </td><td>1.0237(0.087)</td><td>1.0377(0.010)</td><td>1.0085(0.334)</td><td>1.0083(0.239)</td><td>1.0027(0.374)</td><td>1.0037(0.373)</td><td>0.9721(0.196)</td></tr><tr><td> $STEdu_{ki}$ </td><td> $e^{\lambda_{8k}}$ </td><td>0.9806(0.137)</td><td>0.9878(0.202)</td><td>1.0083(0.333)</td><td>1.0096(0.227)</td><td>1.0110(0.042)</td><td>0.9966(0.384)</td><td>1.0098(0.311)</td></tr><tr><td colspan="9">Note: Equivalent p-values given in parentheses. Italicized values represent significant results.</td></tr></table>

<sub>2.</sub> <sub>Risk</sub> <sub>of</sub> <sub>B</sub><sup>reaches</sup> <sup>within</sup> <sup>an</sup> <sup>I</sup>

<sub>device;</sub> <sub>???</sub> <sub>=</sub> C<sup>ause</sup> <sup>of</sup> <sup>data</sup> <sup>breach</sup> <sup>u</sup> <sub>discarded,</sub> <sub>or</sub> <sub>stolen</sub> <sub>nonelectronic</sub> <sub>records;</sub> <sub>PORT</sub> <sub>=</sub> <sub>Lost,</sub> <sub>discarded,</sub> <sub>or</sub> <sub>stolen</sub> <sub>mobile</sub> <sub>de</sub><sup>vice;</sup> <sup>STAT</sup> <sup>=</sup> <sup>Lost,</sup> <sup>dis</sup> <sub>ntry</sub> <sub>by</sub> <sub>an</sub> <sub>outside</sub> <sub>party</sub> <sub>or</sub> <sub>malicious</sub> <sub>software</sub><sup>;</sup> <sup>CARD</sup> <sup>=</sup> <sup>Debit</sup> <sup>and</sup> <sup>credit</sup> <sup>card</sup> <sup>fraud</sup> <sup>that</sup> <sup>is</sup> <sup>not</sup> <sup>accomplished</sup> <sup>v</sup> <sub>sent</sub> <sub>significant</sub> <sub>results</sub>. <sub>The</sub> <sub>eight</sub> <sub>kinds</sub> <sub>of</sub> <sub>breaches</sub> <sub>are</sub>: <sub>DISC</sub> <sub>=</sub> <sub>Sensitive</sub> <sub>information</sub> <sub>poste</sub><sup>d</sup> <sup>publicly,</sup> <sup>misha</sup>

<table><tr><td rowspan="2">Variables</td><td rowspan="2">Coeff.</td><td>DISC</td><td>Other businesses HACK</td><td>Financial and Insurance services CARD</td><td>Retail merchants INSD</td><td>Educational institutionsHY</td><td>Government and military ORT</td><td>Medical providers STAT</td><td>NGOs and nonprofit organizations</td></tr><tr><td>Exp (coeff.)</td><td>Exp (coeff.)</td><td>Exp (coeff.)</td><td>Exp (coeff.)</td><td>Exp (coeff.)</td><td>Exp (coeff.)</td><td>Exp (coeff.)</td><td>Exp (coeff.)</td></tr><tr><td rowspan="2"> $LawStrict_{ki}$ </td><td> $e^{\lambda_{0k}}$ </td><td>4.1894(0.000)</td><td>3.6274(0.000)</td><td>75.2829(0.000)</td><td>7.2801(0.000)</td><td>6.4819(0.000)</td><td>2.9974(0.000)</td><td>13.7021(0.000)</td><td>22.5007(0.000)</td></tr><tr><td> $e^{\lambda_{1k}}$ </td><td>1.3539(0.013)</td><td>1.1725(0.152)</td><td>0.6617(0.210)</td><td>1.0014(0.494)</td><td>0.7228(0.020)</td><td>1.1524(0.117)</td><td>0.7479(0.125)</td><td>1.3157(0.209)</td></tr><tr><td> $Severity_{ki}$ </td><td> $e^{\lambda_{2k}}$ </td><td>0.9646(0.318)</td><td>1.1203(0.023)</td><td>2.0237(0.015)</td><td>0.9294(0.178)</td><td>1.0232(0.386)</td><td>1.0312(0.286)</td><td>1.0331(0.411)</td><td>0.8416(0.139)</td></tr><tr><td> $STGDP_{ki}$ </td><td> $e^{\lambda_{3k}}$ </td><td>0.9999(0.166)</td><td>1.0001(0.240)</td><td>0.9996(0.219)</td><td>1.0001(0.174)</td><td>1.0002(0.040)</td><td>1.0001(0.147)</td><td>1.0002(0.192)</td><td>1.0004(0.062)</td></tr><tr><td> $VULN_{i}$ </td><td> $e^{\lambda_{4k}}$ </td><td>0.9118(0.000)</td><td>0.9452(0.002)</td><td>0.8419(0.200)</td><td>0.9760(0.238)</td><td>0.9661(0.130)</td><td>0.8749(0.000)</td><td>0.8763(0.000)</td><td>0.8337(0.002)</td></tr><tr><td> $ExpInfo_{i}$ </td><td> $e^{\lambda_{5k}}$ </td><td>1.0862(0.007)</td><td>1.1658(0.000)</td><td>1.6490(0.077)</td><td>0.9809(0.374)</td><td>0.9615(0.218)</td><td>1.1786(0.000)</td><td>1.1759(0.001)</td><td>1.2785(0.004)</td></tr><tr><td> $lagITSec_{i}$ </td><td> $e^{\lambda_{6k}}$ </td><td>0.9426(0.000)</td><td>0.9449(0.000)</td><td>0.9886(0.452)</td><td>0.9504(0.000)</td><td>0.9537(0.001)</td><td>0.9398(0.000)</td><td>0.9396(0.001)</td><td>0.8994(0.002)</td></tr><tr><td> $STInternet_{ki}$ </td><td> $e^{\lambda_{7k}}$ </td><td>1.0210(0.024)</td><td>1.0010(0.461)</td><td>0.7661(0.000)</td><td>0.9874(0.186)</td><td>1.0175(0.105)</td><td>1.0147(0.055)</td><td>1.0418(0.050)</td><td>0.9821(0.260)</td></tr><tr><td> $STEdu_{ki}$ </td><td> $e^{\lambda_{8k}}$ </td><td>1.0108(0.099)</td><td>0.9864(0.051)</td><td>1.1971(0.007)</td><td>1.0168(0.108)</td><td>0.9687(0.024)</td><td>0.9994(0.465)</td><td>0.9206(0.014)</td><td>1.0271(0.119)</td></tr></table>

<sub>.</sub> <sub>Risk</sub> <sub>of</sub> <sub>T</sub><sup>ypes</sup> <sup>of</sup> <sup>Data</sup> <sup>Breach</sup>
