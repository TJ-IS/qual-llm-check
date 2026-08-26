---
otero_id: 6858
otero_key: "AGT2V4QF"
title: "Do phishing alerts impact global corporations? A firm value analysis"
authors: "Indranil Bose; Alvin Chung Man Leung"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.04.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Do phishing alerts impact global corporations? A <sup>fi</sup>rm value analysis

Indranil Bose <sup>a,</sup>⁎, Alvin Chung Man Leung <sup>b,1</sup>

<sup>a</sup> Indian Institute of Management Calcutta, Diamond Harbour Road, Joka, Kolkata 700104, India

<sup>b</sup> Department of Information Systems, City University of Hong Kong, Tat Chee Avenue, Kowloon, Hong Kong

## a r t i c l e i n f o

Article history: Received 1 May 2013 Received in revised form 15 April 2014 Accepted 22 April 2014 Available online xxxx

Keywords: Abnormal returns Event study Financial holding companies Firm value Phishing Trading volume

## a b s t r a c t

Phishing is a form of online identity theft that is increasingly becoming a global menace. In this research, we analyze the impact of phishing alerts released in public databases on the market value of global <sup>fi</sup>rms. Using a sample of 1942 phishing alerts related to 259 <sup>fi</sup>rms in 32 countries, we show that the release of each phishing alert leads to a statistically signi<sup>fi</sup>cant loss of market capitalization that is at least US\$ 411 million for a <sup>fi</sup>rm. We propose a theoretical framework for analyzing the impact of threats on <sup>fi</sup>rm value, and determine that the negative investor reaction is strongly signi<sup>fi</sup>cant for alerts released in 2006–2007 and for those targeted to <sup>fi</sup>nancial holding companies, and weakly signi<sup>fi</sup>cant for <sup>fi</sup>rms listed in the US. We derive and validate these results using a combination of event study, subsampling analysis, and cross-sectional regression analysis. Our research makes a contribution by providing a new model for conducting multi-country event studies. We also contribute to the information systems literature by quantifying the loss in market value caused by phishing, and provide compelling evidence to information security administrators of <sup>fi</sup>rms that urge them to adopt adequate countermeasures to prevent phishing attacks

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

“Cyber-crime has become a \$105 billion business that now surpasses the value of the illegal drug trade worldwide.” — David DeWalt, CEO of McAfee [67]

With an increasing number of Internet crimes, online security has become a major concern for the general public. Among various online frauds, phishing, “a form of social engineering in which an attacker attempts to fraudulently retrieve legitimate users' con<sup>fi</sup>dential or sensitive credentials by mimicking electronic communications from a trustworthy or public organization”, is one of the biggest threats to the online community [50]. This online crime has grown tremendously in recent years. According to the Anti-Phishing Working Group (APWG) the number of phishing incidents has increased from 47,324 in the <sup>fi</sup>rst half of 2008 to 126,697 in the second half of December 2009. Since its <sup>fi</sup>rst appearance around 1995, phishing has spread all over the world affecting millions of customers and numerous <sup>fi</sup>rms. Fig. 1 shows how phishing attacks take place and various associated <sup>fi</sup>nancial losses. The actual <sup>fi</sup>nancial loss due to phishing attacks may be ten times more than the estimated numbers for direct loss due to the indirect and the opportunity loss in<sup>fl</sup>icted by phishing — an estimate of which is unavailable in literature [41]. Indirect losses take the form of increased customer support to phishing victims as well as efforts of customers to deal with credit-rating agencies to prevent themselves from being blacklisted due to the attacks. According to Meg Whitman, the former CEO of eBay, phishing has caused deterioration of trust of online customers and impaired e-commerce [10]. Her concern about opportunity loss is supported by the fact that the rate of opening of legitimate emails has dropped by 20% [9], and in a survey 89% of the respondents expressed concern about phishing attacks [79].

Motivated by the lack of research on the indirect and opportunity loss of phishing and particularly the lack of analysis of the impact of phishing on a worldwide basis, we embarked on analyzing the impact of phishing on the market value of <sup>fi</sup>rms. We collected data on phishing alerts targeted to global <sup>fi</sup>rms that were released by anti-phishing organizations. These alerts either included emails that were being sent to customers of public companies or noti<sup>fi</sup>cations about fake websites that were being set up to lure customers. Using the event study method, we determined the impact of such alerts on the market value of global public <sup>fi</sup>rms by evaluating the change in their stock prices and trading volume after the release of the alerts. We also determined the various factors that in<sup>fl</sup>uenced the impact.

Phishing has been a subject of intense research recently. The social and legal responsibilities of phishing were studied by researchers [7,88]. Technical research on phishing included development of antiphishing tools such as AntiPhish, which is a browser extension that generates warning messages when users give away personal information to fake websites [58], and BogusBiter, which is a browser extension that feeds fake user information to phishing websites [89]. In business focused research on phishing, researchers analyzed anti-phishing preparedness of Hong Kong banks [8] and identi<sup>fi</sup>ed antecedents for the severity of phishing attacks [20]. Experimental studies discovered that user related behavioral and dispositional factors and phisher related social relationship mining skills led to success of phishing [49]. In summary, phishing has spurred enormous interest in academia and many anti-phishing tools and behavioral studies were conducted. Nevertheless, do industrial practitioners believe that the bene<sup>fi</sup>ts of antiphishing products justify the cost of adoption? This paper aims at providing a reasonable estimation of the loss in market value due to phishing. Through this study, we hope to arouse the awareness of managers to phishing and encourage them to adopt appropriate antiphishing tools.

![](/api/attachments/AGT2V4QF/fulltext/images/22750aa6ea8a263df0d28c63e591dc164e573830ca8041a296769dab5298e56d.jpg)  
Fig. 1. Phishing attacks and their impacts on <sup>fi</sup>rms and individuals.

Our research is similar to past research conducted on information security breaches and their market impact. Using an event study, researchers showed that mishandling of con<sup>fi</sup>dential information [12], unauthorized access, hacking, denial of service (DoS), website vandalism [14], online credit cards thefts, website defacements [35], data breaches [36], and security breaches related to loss of integrity [52] caused a signi<sup>fi</sup>cant negative impact. The online nature of <sup>fi</sup>rms and tools used for attacks in<sup>fl</sup>uenced the impact on <sup>fi</sup>rm value [2]. Prior research also reported negative but insigni<sup>fi</sup>cant market reaction to DoS attacks [45]. Virus attacks resulted in contradictory positive and insigni<sup>fi</sup>cant returns [46] as well as negative and insigni<sup>fi</sup>cant returns [47] when different datasets were used.

The past research on the impact of security breaches examined only US <sup>fi</sup>rms. But there is no denying that security breaches in general and phishing attacks in particular are a global phenomenon. The insigni<sup>fi</sup>- cant market reaction observed in some prior studies could be due to the non-global nature of the research. Past research focused on discovering the link between security attacks and <sup>fi</sup>nancial loss has often grouped various types of security breaches together [12,52]. Although DoS attacks and virus attacks have been studied separately [35,45,46], the impact of phishing on market value has not caught the attention of researchers. Phishing is a menace in its own right, and is different from other security breaches such as vandalism, DoS, and hacking. Those attacks are company oriented, and reveal the weakness of corporate security. On the contrary, phishing is customer oriented, and affects the perception of the customers about the targeted <sup>fi</sup>rm. This unique nature of phishing as a security breach motivates us to study its impact on global <sup>fi</sup>rms using 1942 alerts from 259 <sup>fi</sup>rms belonging to 32 countries. We also observe the lack of a theoretical framework in extant literature for studying the consequences of security breaches like phishing. We propose a risk-components based framework that explains why phishing causes a negative impact on <sup>fi</sup>rm value, and identi<sup>fi</sup>es factors at the <sup>fi</sup>rm, industry, country, and temporal levels that moderate the impact. Since our research involves <sup>fi</sup>rms from multiple countries, we improve on the traditional Capital Asset Pricing Model (CAPM) based event study method commonly used in Information Systems (IS) research, by proposing a re<sup>fi</sup>ned asset pricing model that combines the Fama–French three factor model with the Fama–French international model, and is able to explain the risk in the cross-sectional abnormal return of global <sup>fi</sup>rms better. We conduct subsampling and cross-sectional regression to identify the signi<sup>fi</sup>cant moderating factors. Our results show that phishing alerts create statistically signi<sup>fi</sup>cant negative impact on stock prices and trading volume and lead to a loss of market capitalization that is at least US\$ 411 million per alert. The market reaction becomes more pronounced for phishing alerts released in 2006–07 and for alerts targeted to <sup>fi</sup>nancial holding companies. This research contributes to the literature on information security by quantifying the loss in market value caused by phishing, and providing hard evidence to security administrators to encourage adoption of adequate countermeasures to prevent phishing.

## 2. Theoretical framework

Our proposed framework for assessing the impact of security risks on market value of <sup>fi</sup>rms is shown in Fig. 2. According to Drucker, “risk is inherent to the commitment of present resources to future expectations” [27]. To model risk for a <sup>fi</sup>rm, we adapt the idea of risk-components proposed by Crockford [22]. The <sup>fi</sup>rst component of risk is threats that can disrupt the functioning of an organization.

![](/api/attachments/AGT2V4QF/fulltext/images/8dcb68e91fda5388dae0c550f4093f08a5dceed8a2ab2a7916090f37efb4e98d.jpg)  
Fig. 2. Framework for analyzing the impact of indirect threats on <sup>fi</sup>rm value.

These can include direct or indirect “natural forces, human error, deliberate damage, and progressive deterioration” [22]. Phishing is an indirect security threat that manifests itself in the form of fake websites and spam emails and causes customers to give away their personal data.

Any threats acting on a <sup>fi</sup>rm can impact the tangible resources of the <sup>fi</sup>rm, such as physical properties, <sup>fi</sup>nances, and personnel, and intangible resources, such as reputation of <sup>fi</sup>rms, know-how of employees, and intellectual property rights of patents and designs [18,42]. In the case of phishing, the resources that are affected are the intangible resources of the <sup>fi</sup>rm such as reputation and brand name. Phishing is different from other forms of security breaches in that it is not targeted to a <sup>fi</sup>rm's computer system but to its potential customers. Despite the indirect nature, phishing can affect resources in the form of disrupted operations, loss of earnings, or deterioration of reputation. Although <sup>fi</sup>rms, whose customers are targeted through phishing, are considered to be victims in the eyes of law, most <sup>fi</sup>rms eventually compensate customers on a voluntary basis [50]. As a result, a phishing attack signals the message of potential future earnings loss for the targeted <sup>fi</sup>rm, that may be re<sup>fl</sup>ected in the stock price or trading volume.

The next important component of risk is the moderating factors that may be internal or external to the <sup>fi</sup>rms' resources, and can moderate the consequences of threats on the <sup>fi</sup>rm [86]. Since phishing is a global phenomenon and affects <sup>fi</sup>rms in multiple industries over time, four factors at the <sup>fi</sup>rm, industry, country, and temporal levels respectively are likely to determine the severity of impact of phishing. Phishers tend to attack as many customers of a <sup>fi</sup>rm as possible to improve their chances of success, and do not discriminate between customers of holding or subsidiary companies. However, the market reaction may be different for the different types of <sup>fi</sup>rm ownership, and this prompts us to list <sup>fi</sup>rm ownership as a moderating <sup>fi</sup>rm level factor. The type of industry can be quite relevant as phishing is mostly directed towards industries with the highest payoff [5]. Furthermore, the country of listing for <sup>fi</sup>rms in<sup>fl</sup>uences the consequences of security threats due to a variety of reasons that include regulation, education, popularity of e-commerce, and awareness about security among the general public. Time plays an important role in in<sup>fl</sup>uencing the impact of negative events such as security breaches [2,14,36] as concern about information security heightens as users become more knowledgeable about the crimes [63].

## 3. Hypothesis development

The consequences of phishing affect not only individual customers, but also corporate owners. To an extent, companies that are targeted by phishers are responsible for <sup>fi</sup>nancial loss under speci<sup>fi</sup>c ordinances. The US Truth in Lending Act requires companies to bear most of the losses due to unauthorized purchases [64]. The cost of lawsuits and potential compensation to customers may also drive down future pro<sup>fi</sup>ts of the companies. Furthermore, phishing incidents may undermine the con<sup>fi</sup>dence of consumers in using e-commerce services offered to them. Customers are sensitive to privacy issues and are concerned about trustworthiness of <sup>fi</sup>rms [28]. Prior research on information security has shown that customers' concern about security has driven down market value, and security breaches have given rise to a negative stock price return of 0.6% [1] and even an average loss in market capitalization of \$1.65 billion per breach [14]. It is also known that con<sup>fi</sup>dentiality related security breaches [35], unauthorized access of con<sup>fi</sup>dential data [12], and software vulnerabilities associated with con<sup>fi</sup>dentiality breaches [84] have had a stronger impact on market value than other non-con<sup>fi</sup>dentiality related infringements. As phishing belongs to the class of con<sup>fi</sup>dentiality infringements, it poses a similar negative impact. This leads to:

H1. Phishing alerts cause a negative impact on return of stock price of targeted <sup>fi</sup>rms.

Phishing alerts may reduce the con<sup>fi</sup>dence of security conscious investors about the future prospect of targeted <sup>fi</sup>rms and in<sup>fl</sup>uence them to sell their shares. The large amount of sell-off may cause significant changes in trading volume. Prior literature in <sup>fi</sup>nance has stated that while abnormal return of stock prices indicated the overall market expectations about an announcement, abnormal trading volume signi-<sup>fi</sup>ed the change in the expectation of individual investors [15,54,57]. A joint test of both return of stock price and change in trading volume could enhance the power of the result generated from an event study [55]. e-Commerce investments [23], IT infrastructure investments [15], and IT investments from 1991 to 1996 [48] have generated significant positive increase in trading volume. At the same time, major negative events, such as the crash of the space shuttle Challenger, have triggered signi<sup>fi</sup>cant positive trading volume on the announcement day [66]. Phishing alerts will send a signal to investors to sell off shares of affected <sup>fi</sup>rms. This leads to:

## H2. Phishing alerts cause positive abnormal change in trading volume.

In addition to studying the impact of phishing alerts on <sup>fi</sup>rm value, we also assess the moderating factors at the <sup>fi</sup>rm, industry, country, and temporal levels.

Please cite this article as: I. Bose, A.C.M. Leung, Do phishing alerts impact global corporations? A <sup>fi</sup>rm value analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.006

## 3.1. Firm ownership

Conglomerates with subsidiary <sup>fi</sup>rms are more likely to diversify their risks. Phishing as a risk may have less impact if it targets a subsidiary of a conglomerate. Prior studies have shown that the subsidiary status has a mitigating impact in case of data breach announcements [37] and DoS attack announcements [46]. The primary reason is that investors pay more attention to news that in<sup>fl</sup>uences the overall pro<sup>fi</sup>tability of a conglomerate and less attention to events related to a single subsidiary of a conglomerate. Though phishing may pose a negative impact on a targeted <sup>fi</sup>rm, its impact is less pronounced when targeted to a subsidiary of a conglomerate due to diversi<sup>fi</sup>cation of risk. This leads to:

H3. Phishing alerts targeting a subsidiary <sup>fi</sup>rm are likely to have less negative impact on the market value of the listed conglomerate which owns the <sup>fi</sup>rm than when it targets the conglomerate directly.

## 3.2. Type of industry

Dependency on IT varies from one industry to another. The <sup>fi</sup>nancial services industry has higher requirements for IT infrastructure capabilities, IT management, and security services than production-based industries (e.g., manufacturing) [11]. Therefore, it is more sensitive to announcements related to IT, e-commerce, or outsourcing investments [23,26,48]. Phishers target industries with a heavy volume of monetary transactions, and over 90% of the reported phishing incidents are targeted to the <sup>fi</sup>nancial services industry followed by the IT and telecom industry and the retail industry respectively [4]. Attacks targeted to credit unions experienced a tremendous year-to-year growth rate of 584%, followed by that of banks (325%) in the <sup>fi</sup>rst two months of 2007 [37]. Firms that provide <sup>fi</sup>nancial services are more concerned about legal, <sup>fi</sup>nancial, and client risks in comparison to IT related and publishing related industries [80]. When faced with cyber attacks, the <sup>fi</sup>nancial services industry may show a severe reaction because such attacks diminish the trust of customers and may even lead to legal proceedings from customers and regulators [76]. This leads to:

H4. Firms in the <sup>fi</sup>nancial services industry are more negatively affected by phishing alerts than those belonging to other industries.

## 3.3. Country of listing

Due to its superb technological infrastructure, the US leads the world in the diffusion of e-commerce [38], and is also “the largest source of information security attacks” [77]. Online <sup>fi</sup>nancial transaction is one of the key segments of B2C e-commerce in the US that has witnessed signi<sup>fi</sup>cant growth in recent years. Since more than 53 million people in the US conducted online banking around 2004–05 compared with about 15 million in the UK in 2007, people in the US tend to be more aware of phishing [29]. In a survey conducted by RSA, 83% of US bank account holders claimed to be familiar with phishing, whereas less than 70% of the interviewed bank customers in countries like Australia, the UK, and India made a similar claim [78]. Also, according to the APWG, most web-based phishing attacks are launched in the US and account for 37.25% of all attacks in January 2008, more than nearly three times the number of such attacks (11.66%) launched in the second highest ranking country [4]. Therefore, people in the US are more knowledgeable about the negative impact of phishing. Furthermore, the US has enacted speci<sup>fi</sup>c laws against phishing. Federal laws include Identity Theft and Assumption Deterrence Act of 1998 and Social Security Number Privacy and Identity Theft Prevention Act of 2003 [50-51] and state laws include Anti-Phishing Act of 2005 in California and other similar laws in Texas and Arkansas [51]. By November 2008, the US Federal Government even mandated all banks to implement ‘Red Flag Rules’ to take a proactive role in detecting possible identity theft [7]. The strict anti-phishing laws may have heightened the awareness of the US investors about the negative impact of phishing.<sup>2</sup> Therefore, we posit:

H5. Companies listed in the US are more negatively affected by phish ing alerts.

## 3.4. Time of release

Perception and awareness of the general public towards technology and its associated threats change over time [43,56]. In prior event studies, Im et al. found that recent IT investments resulted in more signi<sup>fi</sup>- cant returns when compared with older investments [48]. Chatterjee et al. showed that recently announced new CIO positions resulted in a more statistically signi<sup>fi</sup>cant impact on <sup>fi</sup>rm value [16]. Benbunan-Fich and Fich demonstrated that the announcements related to traf<sup>fi</sup>c on websites created signi<sup>fi</sup>cant positive <sup>fi</sup>rm value in the pre-dotcom bubble period [6]. People's perception about security also changes over time. In the early 80s, people were more concerned about technical aspects of information security and in the late 90s, people focused on corporate best practices in information security management [85]. When analyzing the impact of security breaches on <sup>fi</sup>rm value, the reaction became more negative as time progressed [14]. Time also played a role in phishing. The number of individuals who received phishing emails increased from 57 million in 2004 to 124 million in 2007 [61]. With more frequent exposure to the news of phishing, the perception and knowledge of people also changed over time. This leads to:

H6. The negative impact of phishing alerts on <sup>fi</sup>rm value increases over time.

## 4. Research method and data analysis

According to McWilliams and Siegel, “an event is anything that results in new relevant information”, and events in this research are phishing alerts released on public databases [68]. We collected data primarily from Millersmiles — the largest phishing alert database in the world with over 7000 announcements at the time of research. Since phishing alerts collected from a single database could be potentially biased and incomplete [70], we also collected alerts from alternative repositories such as Websense and from the websites of other region speci<sup>fi</sup>c anti-phishing organizations, such as the Hong Kong Monetary Authority and Antiphishing Group Japan. Factiva, which is an international news database, was also used to cross-check and retrieve any remaining phishing alerts. Keywords such as phishing, fraudulent/bogus/ fake email, fraudulent/bogus/fake websites, online identity theft, and scam were used. Appendix A shows some examples of phishing alerts retrieved from Millersmiles, Websense, and Factiva.

The data were collected from January 2003 to December 2007. We eliminated alerts related to private and non-listed public companies, duplicate alerts and alerts affected by confounding news about mergers/acquisitions, announcements of dividends/pro<sup>fi</sup>ts, change of management, new company development, and evaluation by external entities. We chose a confounding window of 5 days (2 days before, on, and 2 days after the date of phishing alert). The length of the confounding window was the longest among those used in prior event studies.<sup>3</sup>

Appendix B shows the breakdown of data collected from different sources before and after <sup>fi</sup>ltering. If a phishing alert recurred on a database or appeared on more than one database on different dates, only the earliest one was retained. We also ensured that each unique phishing alert for the same company was separated by at least three days.<sup>4</sup> A careful comparison of the description and snapshot of phishing emails, as well as address of websites available on phishing databases, was made to determine whether a phishing alert was unique. Furthermore, if the average stock price of a <sup>fi</sup>rm was less than US\$ 1, or the average daily trading volume was less than 50,000 shares in the estimation period, then the corresponding alerts were eliminated [82]. We started with the retrieval of 9395 phishing alerts, and our cleaned dataset consisted of 1942 usable phishing alerts.<sup>5</sup>

## 4.1. Methods for event study

For determination of cumulative abnormal returns (CAR) of stock prices, the CAPM assumes linear relationship between the rate of return and the rate of market return, and is represented as:

$$
R _ {i t} = \alpha_ {i} + \beta_ {i} R _ {m t} + \varepsilon_ {i t}. 6\tag{1}
$$

We used stock price data for 200 trading days that ended one month prior to the event announcement date, and built the regression models. In prior research, only one market index, such as S&P 500 index or CRSP Value Weighted Index was used. As our data involved <sup>fi</sup>rms from different countries, we considered multiple stock indices (including specialized indexes like the S&P banking index) for a particular stock, and chose the market index that resulted in the best adjusted $R ^ { 2 }$ for the regression model.

In past research, it was reported that the CAPM, which included only the market factor, resulted in miscalculation of abnormal market returns [32]. Fama and French determined that apart from the market factor, it was necessary to include two other factors that could explain the abnormal returns better [32,33]. They reasoned that there was a value premium in the average returns of stocks as analysts overvalued ‘growth’ (low book-to-market ratio and low earnings) stocks and undervalued ‘value’ (high book-to-market ratio and high earnings). Therefore, a risk factor (HML), that represented the difference between the high and low book-to-market ratio stocks in a value-weighted portfolio of stocks, should be added to the CAPM to compensate for the risk missed by that model. Similarly, when the book-to-market ratio was controlled, small <sup>fi</sup>rms generally had lower earnings than big <sup>fi</sup>rms. A second risk factor (SMB) was added to the CAPM, and represented the difference in the rate of returns between small and big <sup>fi</sup>rms in a value-weighted portfolio. Eq. (2) represents the Fama–French three factor model (FF):

$$
R _ {i t} - R _ {f t} = \alpha_ {i} + \beta_ {i} \left(R _ {m _ {i} t} - R _ {f t}\right) + \gamma_ {i} S M B _ {t} + \delta_ {i} H M L _ {t} + \varepsilon_ {i t}. ^ {7}\tag{2}
$$

Besides <sup>fi</sup>nance, the FF model has been used to study the impact of branding [65], new product announcements [81], marketing alliances [83], and security breaches announcements [39] on market value.

However, it was not suf<sup>fi</sup>cient for us to use the FF model as is because the data consisted of several non-US <sup>fi</sup>rms. Past research on non-US markets had shown that when an international book-to-market correction factor (IHML) was added to the model, it could explain the returns generated from global value and global growth portfolios. The addition of one factor rather than two was done for simplicity, and Fama and French remarked that “we ignore other risk factors that might affect expected returns … our simple approach provides a reasonably adequate story for average returns” [34]. Such an international model was used to study the performance of hedge funds [13], but is yet to make its appearance in IS literature. We combined the three factor FF model for US data with the international FF model to develop the merged FF model (FFM) as shown in Eq. (3):

$$
\begin{array}{c} R _ {i t} - R _ {f t} = \alpha_ {i} + \beta_ {i} = \left(R _ {m _ {i} t} - R _ {f t}\right) + D _ {i} (\gamma_ {i} S M B _ {t} + \delta_ {i} H M L _ {t}) ^ {8} \\ + (1 - D _ {i}) \phi_ {i} I H M L _ {i t} + \varepsilon_ {i t}. \end{array}\tag{3}
$$

In this research, all stock prices and trading volume data were retrieved from Thomson Reuters. Daily data related to $R _ { f t } , S M B _ { t } , H M L _ { t } ,$ and $I H M L _ { i t }$ were retrieved from Professor Kenneth French's website. Since the website listed $I H M L _ { i t }$ for only 21 countries, 50 alerts from 11 countries not listed in that website were not analyzed.

We chose an event window of 3 days (one day before to one day after the release date of the phishing alert). The event window was kept short to conform with the assumption of ef<sup>fi</sup>cient market, allow better power for the test statistics, and enable precise determination of confounding events [68]. Prior event studies have also chosen an event window of 3 days [2,12]. An impact on the day before the event was analyzed because there might be leakage about the phishing incident in online electronic media before it appeared in the database. For computation of the cumulative abnormal trading volume (CAV), the market adjusted model was chosen.<sup>9</sup> Our approach of choosing a mixed model for stock price and trading volume was similar to a prior study [15]. To test the statistical signi<sup>fi</sup>cance of the abnormal returns of stock prices and trading volume, a parametric Z test was used [26]. To further establish the robustness of results, we used non-parametric tests that are better in controlling “nonnormal distributions crosssectional dependence and increases in the variance of abnormal returns during the event window” [15]. We used the sign Z test [19] and the Corrado's rank test [21].

## 4.2. Subsampling and cross-sectional regression

Similar to the composition of the reported phishing incidents of APWG, our sample data were primarily from US listed companies (64.4% of the total sample) and from the <sup>fi</sup>nancial services sector (79.1% of the total sample). In order to minimize the potential sampling bias, we split the data into subsamples based on various moderating factors such as <sup>fi</sup>rm ownership (holding and subsidiary), country of listing (US and non-US), type of industry (<sup>fi</sup>nancial services <sup>fi</sup>rms and others), and time of release (pre-2006 and 2006–07). These subsamples corresponded to hypotheses H3 to H6. We computed the CAR for all subsamples, and used parametric and non-parametric tests on them to test the hypotheses. As a post-hoc analysis, we built regression models, where control variables and hypothesized variables acted as the independent variables, and the CAR for the most signi<sup>fi</sup>cant event window was the dependent variable. The three unrelated control variables included <sup>fi</sup>rm size, history of prior phishing alerts, and riskiness of phishing alerts. Firm size was studied in extant literature [1,2,14,36, 52,84], and measured as natural logarithm of total assets reported in the last month of the year before the release of the phishing alert. The attack history of the <sup>fi</sup>rm was similar to frequency of incidents that was studied in past event studies [3,36,84]. It is represented as ln(n + 0.5), where n was the number of occurrences of phishing alerts in the past [72]. This variable was chosen to control the impact of repeated phishing alerts. The severity of the phishing alert, similar to severity of a security breach, software vulnerability, web outage, or virus attack [3,14,40,47,84], was the third control variable. It was represented by a dummy variable, where 1 indicated a sophisticated phishing alert with risk level above medium, and 0 otherwise.<sup>10</sup> The sample size for cross-sectional regression analysis was 1865 because the total assets for some companies with delisted tickers were not available. All hypothesized variables were dummy variables.<sup>11</sup> The descriptive statistics for these alerts and the correlations are shown in Table 1. The correlations were found to be less than ±0.65. We used quantile regression instead of OLS because it was robust to departure from non-normality of error terms, presence of outliers, and minimized cross-sectional and cross-correlational heteroskedasticity<sup>12</sup> [59].

## 5. Research <sup>fi</sup>ndings

The average adjusted $R ^ { 2 }$ for the CAPM for the entire sample was 0.465, and that for the FFM was 0.483. With the inclusion of additional risk factors, the explanatory power of the model increased. Panel A of Table 2 shows that the impact was the most signi<sup>fi</sup>cant one day after the alert was released. The event window [−1] did not show a signi<sup>fi</sup>- cant result, implying no serious news leakage. Multiple day event windows, like [0,1] and [ 1,1], showed signi<sup>fi</sup>cant results at the 5% level for all tests. The loss in market capitalization was at least US\$ 411 million.<sup>13</sup> Therefore, H1 is strongly supported. With regard to the impact on trading volume, both parametric and non-parametric tests showed signi<sup>fi</sup>cant negative change. Panel B shows that, except event window [1] that was barely signi<sup>fi</sup>cant at the 10% level in the sign test, all other event windows showed signi<sup>fi</sup>cant negative change at the 1% level. The volume of shares traded in all event windows was lower than usual, implying a general lack of con<sup>fi</sup>dence among investors. However, the change in the CAV was signi<sup>fi</sup>cant negative rather than positive. Therefore, H2 is rejected.

## 5.1. Subsampling analysis (SA)

The impact of the moderating factors for event window [−1,1] is shown in Table 3. As shown in Panel A, all tests for FFM indicated subsidiaries were signi<sup>fi</sup>cantly affected but the Z test for the CAPM did not indicate the same. Therefore, H3 is rejected. Panel B shows the industry effect. The p-values for the <sup>fi</sup>nancial services <sup>fi</sup>rms in both tests were less than or equal to 0.05 for the CAPM and the FFM but were mostly insigni<sup>fi</sup>cant for the non-<sup>fi</sup>nancial services <sup>fi</sup>rms.<sup>14</sup> Therefore, H4 is supported. Panel C shows the country effect. US <sup>fi</sup>rms showed signi<sup>fi</sup>cant negative CAR at the 10% level for the tests used on both models. The mean CARs of alerts associated with US <sup>fi</sup>rms were more negative than those associated with <sup>fi</sup>rms in other countries. Therefore, H5 is supported. The time period of announcement was classi<sup>fi</sup>ed as early or late depending on the year of the announcement. Several countries made it compulsory for <sup>fi</sup>rms to adopt two-factor authentication by 2005, and this led to our choice of 2005 as the cutoff year. Panel D shows that the impact of phishing increased over time. The announcements made in 2006 and 2007 resulted in signi<sup>fi</sup>cant negative CAR for <sup>fi</sup>rms in both parametric and non-parametric tests conducted on both models. In the pre-2006 period, the mean and median CARs were positive in some models in sharp contrast to the observation in the later period. This indicated a change in perception of investors about phishing alerts over time. Therefore, H6 is supported. We conduct further robustness checks by breaking down industry, country of listing, and year of announcements into more precise levels. The results obtained are consistent with the reported <sup>fi</sup>ndings.<sup>15</sup>

## 5.2. Interaction analysis

Since the nature of ownership of <sup>fi</sup>rm turned out to be insigni<sup>fi</sup>cant in SA, we decided to explore it more fully in association with another hypothesized variable. This is in agreement with Oh et al. who remarked that “a lack of attention to interaction terms might account for the inconsistent results found in conventional event studies that have considered only the main effects” [73]. The statistically signi<sup>fi</sup>cant interaction results are shown in Table 4.<sup>16</sup> As shown in Panel A, holding companies in the <sup>fi</sup>nancial services sector were signi<sup>fi</sup>cantly negatively affected by phishing alerts with p-values less than 0.1 for both models. The interaction variable consisting of the Holding and Recent factors showed a signi<sup>fi</sup>cant and negative coef<sup>fi</sup>cient, with p-values less than or equal to 0.02 as shown in Panel B. This showed that while Holding by itself was not a signi<sup>fi</sup>cant factor, it became so in the presence of the <sup>fi</sup>nancial services factor or the recent time factor. Finance and Recent were both signi<sup>fi</sup>- cant factors in determining negative market impact. Hence, it was not surprising to observe that their interaction also gave rise to signi<sup>fi</sup>cant negative reaction as shown in Panel C. Similarly, Panel D shows that the interaction of US and Recent also resulted in signi<sup>fi</sup>cant negative impact. Interestingly, although US and Finance were independently signi<sup>fi</sup>cant factors, their interaction turned out to be insigni<sup>fi</sup>cant.

## 5.3. Cross-sectional regression analysis (CSRA)

To validate the findings in the SA. we conducted CSRA using data from the event window [ 1,1] that showed the most signi<sup>fi</sup>cant negative CAR at the 5% level. In the QR results shown in Table 5, the control variables were insigni<sup>fi</sup>cant for all models. Similar to a prior study [15], an OLS regression model constructed using all variables except the interaction terms showed that the variance in<sup>fl</sup>ation factor (VIF) was less than 3 for all variables. As VIF was less than 10, this indicated that little multicollinearity between the variables and the models was valid. The low $R ^ { 2 }$ reported in Table 5 did not imply poor accuracy because low $R ^ { 2 }$ (often less than 3%) was common in prior event studies and other <sup>fi</sup>nancial studies using daily stock data [16,24,25].<sup>17</sup>

Table 2  
Table 1  
Descriptive statistics and correlations between hypothesized and control variables.

<table><tr><td>Sample size = 1942</td><td>Min</td><td>Max</td><td>Mean</td><td>Std. dev.</td><td>Firm size</td><td>Attack history</td><td>Risk level</td><td>Holding</td><td>US</td><td>Finance</td><td>Recent</td></tr><tr><td> $Firm size^a$ </td><td>19.23</td><td>33.02</td><td>25.60</td><td>1.94</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $Attack history^b$ </td><td>-0.69</td><td>7.34</td><td>3.32</td><td>2.01</td><td>0.09</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Risk level</td><td>0</td><td>1</td><td>0.09</td><td>0.29</td><td>0.01</td><td>0.04</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>Holding</td><td>0</td><td>1</td><td>0.47</td><td>0.50</td><td>-0.12</td><td>0.03</td><td>-0.02</td><td>1</td><td></td><td></td><td></td></tr><tr><td>US</td><td>0</td><td>1</td><td>0.63</td><td>0.48</td><td>-0.45</td><td>0.21</td><td>0.07</td><td>0.01</td><td>1</td><td></td><td></td></tr><tr><td>Finance</td><td>0</td><td>1</td><td>0.78</td><td>0.41</td><td>0.63</td><td>-0.29</td><td>-0.01</td><td>-0.30</td><td>-0.33</td><td>1</td><td></td></tr><tr><td>Recent</td><td>0</td><td>1</td><td>0.62</td><td>0.49</td><td>0.19</td><td>0.28</td><td>-0.07</td><td>0.00</td><td>-0.12</td><td>0.14</td><td>1</td></tr></table>

<sup>a</sup> Size of the <sup>fi</sup>rm is calculated as ln(total assets) and is represented in US\$.  
<sup>b</sup> Attack history is calculated as ln(number of prior phishing alerts + 0.5).

Stock price and trading volume reaction.

<table><tr><td colspan="13">Panel A: reaction of stock price</td></tr><tr><td>Event windows</td><td>[-1]</td><td></td><td>[0]</td><td></td><td>[1]</td><td></td><td>[-1,0]</td><td></td><td>[0,1]</td><td></td><td>[-1,1]</td><td></td></tr><tr><td>Models</td><td>CAPM</td><td>FFM</td><td>CAPM</td><td>FFM</td><td>CAPM</td><td>FFM</td><td>CAPM</td><td>FFM</td><td>CAPM</td><td>FFM</td><td>CAPM</td><td>FFM</td></tr><tr><td>Sample size</td><td>1942</td><td>1892</td><td>1942</td><td>1892</td><td>1942</td><td>1892</td><td>1942</td><td>1892</td><td>1942</td><td>1892</td><td>1942</td><td>1892</td></tr><tr><td>Mean CAR</td><td>0.00%</td><td>-0.01%</td><td>-0.01%</td><td>-0.01%</td><td>-0.03%</td><td>-0.04%</td><td>-0.01%</td><td>-0.02%</td><td>-0.05%</td><td>-0.05%</td><td>-0.05%</td><td>-0.06%</td></tr><tr><td>Z test p-value</td><td>0.39</td><td>0.28</td><td>0.08</td><td>0.14</td><td>0.03</td><td>0.01</td><td>0.12</td><td>0.12</td><td>0.01</td><td>0.01</td><td>0.02</td><td>0.01</td></tr><tr><td>Median CAR</td><td>-0.04%</td><td>-0.03%</td><td>-0.03%</td><td>-0.04%</td><td>-0.04%</td><td>-0.04%</td><td>-0.08%</td><td>-0.06%</td><td>-0.07%</td><td>-0.06%</td><td>-0.09%</td><td>-0.10%</td></tr><tr><td>Sign test p-value</td><td>0.13</td><td>0.14</td><td>0.22</td><td>0.13</td><td>0.08</td><td>0.05</td><td>0.08</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.03</td></tr><tr><td>Corrado&#x27;s rank test p-value</td><td>0.34</td><td>0.18</td><td>0.11</td><td>0.14</td><td>0.06</td><td>0.02</td><td>0.12</td><td>0.08</td><td>0.03</td><td>0.01</td><td>0.03</td><td>0.01</td></tr><tr><td colspan="13">Panel B: reaction of trading volume</td></tr><tr><td>Event windows</td><td></td><td>[-1]</td><td></td><td>[0]</td><td></td><td>[1]</td><td></td><td>[-1,0]</td><td></td><td>[0,1]</td><td></td><td>[-1,1]</td></tr><tr><td>Sample size</td><td></td><td>1942</td><td></td><td>1942</td><td></td><td>1942</td><td></td><td>1942</td><td></td><td>1942</td><td></td><td>1942</td></tr><tr><td>Mean CAV</td><td></td><td>-6.25%</td><td></td><td>-8.21%</td><td></td><td>-5.31%</td><td></td><td>-14.46%</td><td></td><td>-13.52%</td><td></td><td>-19.77%</td></tr><tr><td>Z test p-value</td><td></td><td>0.00</td><td></td><td>0.00</td><td></td><td>0.00</td><td></td><td>0.00</td><td></td><td>0.00</td><td></td><td>0.00</td></tr><tr><td>Median CAV</td><td></td><td>-7.86%</td><td></td><td>-9.23%</td><td></td><td>-3.41%</td><td></td><td>-17.20%</td><td></td><td>-12.60%</td><td></td><td>-18.80%</td></tr><tr><td>Sign test p-value</td><td></td><td>0.00</td><td></td><td>0.00</td><td></td><td>0.10</td><td></td><td>0.00</td><td></td><td>0.00</td><td></td><td>0.00</td></tr><tr><td>Corrado&#x27;s rank test p-value</td><td></td><td>0.00</td><td></td><td>0.00</td><td></td><td>0.03</td><td></td><td>0.00</td><td></td><td>0.00</td><td></td><td>0.00</td></tr></table>

Models C1 and F1 (Table 5), that studied the impact of control and hypothesized variables on the CAR, showed that Recent was signi<sup>fi</sup>cant and negative.<sup>18</sup> Since four interaction terms of the hypothesized variables showed statistical signi<sup>fi</sup>cance in the SA, we exhaustively experimented with them in CSRA.<sup>19</sup> Models C2 and F2 studied the impact of inclusion of the interaction term Holding ∗ Finance. Apart from Recent, Holding, Finance, and Holding ∗ Finance were all signi<sup>fi</sup>- cant in these models. However, only the coef<sup>fi</sup>cients for Recent and Holding ∗ Finance were negative. In models C3 and F3, we added two interaction terms, Holding ∗ Finance and Finance ∗ Recent. Similar results were observed for both models and the coef<sup>fi</sup>cients for Recent and Holding ∗ Finance were consistently negative and signi<sup>fi</sup>cant. Surprisingly, the coef<sup>fi</sup>cient for Finance ∗ Recent was signi<sup>fi</sup>cant and positive. In models C4 and F4, we replaced Finance ∗ Recent with Holding Recent. Holding Finance again had the most signi<sup>fi</sup>cant negative coef<sup>fi</sup>cient, but the coef<sup>fi</sup>cient of Recent was negative and marginally insigni<sup>fi</sup>cant with p-value equal to 0.19 in the CAPM and 0.16 in the FFM. The coef<sup>fi</sup>cient for Holding ∗ Recent was negative but insigni<sup>fi</sup>cant. In models C5 and F5, when we replaced Holding ∗ Recent with US ∗ Recent, the coef<sup>fi</sup>cients of Holding ∗ Finance were negative and significant for both models, and those for Recent were negative and signi<sup>fi</sup>cant only for the CAPM. The impact of US ∗ Recent in C5 and F5 was insigni<sup>fi</sup>cant in both models, but it was positive for C5 and negative for F5.

The CSRA con<sup>fi</sup>rmed that Recent played a signi<sup>fi</sup>cant role in driving down <sup>fi</sup>rm value and gave strong support for H6. With regard to <sup>fi</sup>rm ownership, we could conclude from the SA and the CSRA that it had no signi<sup>fi</sup>cant impact and thus, H3 was rejected. As for industry and country effects, though the SA showed that both signi<sup>fi</sup>cantly impacted abnormal returns, the CSRA showed that the impact was not strong, and it lost its signi<sup>fi</sup>cance in the presence of other hypothesized variables. Hence, H4 and H5 were partially supported. An important <sup>fi</sup>nding was that the interaction of Holding and Finance was strongly signi<sup>fi</sup>cant in driving the negative reaction of <sup>fi</sup>rms, and this was consistent for both the CAPM and the FFM.

## 6. Discussion

This research provided evidence that phishing alerts caused negative abnormal returns of stock prices and negative abnormal changes in trading volume. The mean CAR was low when compared to event studies related to catastrophes, where the CAR ranged from −2.48% to −11.86% on the event day [66]. The trading volume reaction of phishing alerts was different when compared to that of catastrophes. The low trading volume in the event windows showed that investors became indecisive about the future performance of the targeted companies, and preferred to hold rather than sell or buy stocks [87].

We found that <sup>fi</sup>rm ownership was an insigni<sup>fi</sup>cant factor, whereas the industry and the country of listing were weak moderating factors. The time of occurrence of alerts, and speci<sup>fi</sup>cally if the alerts were

<table><tr><td colspan="5">Panel A: moderating effect of firm ownership</td><td colspan="5">Panel B: moderating effect of type of industry</td></tr><tr><td>Models</td><td>CAPM</td><td></td><td>FFM</td><td></td><td>Models</td><td>CAPM</td><td></td><td>FFM</td><td></td></tr><tr><td>Firm ownership</td><td>H</td><td>S</td><td>H</td><td>S</td><td>Type of industry</td><td>F</td><td>N</td><td>F</td><td>N</td></tr><tr><td>Sample size</td><td>889</td><td>1053</td><td>853</td><td>1039</td><td>Sample size</td><td>1536</td><td>406</td><td>1486</td><td>406</td></tr><tr><td>Mean CAR</td><td>-0.04%</td><td>-0.05%</td><td>-0.04%</td><td>-0.07%</td><td>Mean CAR</td><td>-0.03%</td><td>-0.11%</td><td>-0.06%</td><td>-0.05%</td></tr><tr><td>Z test p-value</td><td>0.04</td><td>0.12</td><td>0.03</td><td>0.09</td><td>Z test p-value</td><td>0.05</td><td>0.09</td><td>0.02</td><td>0.15</td></tr><tr><td>Median CAR</td><td>-0.10%</td><td>-0.08%</td><td>-0.04%</td><td>-0.15%</td><td>Median CAR</td><td>-0.08%</td><td>-0.21%</td><td>-0.12%</td><td>0.00%</td></tr><tr><td>Sign test p-value</td><td>0.05</td><td>0.05</td><td>0.45</td><td>0.01</td><td>Sign test p-value</td><td>0.01</td><td>0.20</td><td>0.01</td><td>0.22</td></tr><tr><td>Corrado&#x27;s rank test p-value</td><td>0.13</td><td>0.08</td><td>0.12</td><td>0.03</td><td>Corrado&#x27;s rank test p-value</td><td>0.04</td><td>0.26</td><td>0.01</td><td>0.46</td></tr><tr><td colspan="5">Panel C: moderating effect of country of listing</td><td colspan="5">Panel D: moderating effect of time of release</td></tr><tr><td>Country of listing</td><td>US</td><td>OC</td><td>US</td><td>OC</td><td>Time of release</td><td>O</td><td>R</td><td>O</td><td>R</td></tr><tr><td>Sample size</td><td>1250</td><td>692</td><td>1250</td><td>642</td><td>Sample size</td><td>751</td><td>1191</td><td>736</td><td>1156</td></tr><tr><td>Mean CAR</td><td>-0.07%</td><td>-0.01%</td><td>-0.08%</td><td>0.00%</td><td>Mean CAR</td><td>0.03%</td><td>-0.09%</td><td>-0.02%</td><td>-0.08%</td></tr><tr><td>Z test p-value</td><td>0.06</td><td>0.09</td><td>0.01</td><td>0.25</td><td>Z test p-value</td><td>0.36</td><td>0.01</td><td>0.22</td><td>0.01</td></tr><tr><td>Median CAR</td><td>-0.08%</td><td>-0.11%</td><td>-0.11%</td><td>-0.10%</td><td>Median CAR</td><td>-0.01%</td><td>-0.14%</td><td>0.01%</td><td>-0.15%</td></tr><tr><td>Sign test p-value</td><td>0.05</td><td>0.04</td><td>0.05</td><td>0.19</td><td>Sign test p-value</td><td>0.47</td><td>0.00</td><td>0.28</td><td>0.00</td></tr><tr><td>Corrado&#x27;s rank test p-value</td><td>0.08</td><td>0.11</td><td>0.01</td><td>0.25</td><td>Corrado&#x27;s rank test p-value</td><td>0.34</td><td>0.01</td><td>0.35</td><td>0.00</td></tr></table>

H: Holding, S: Subsidiary, F: Finance, N: Non-<sup>fi</sup>nance, US: US listed <sup>fi</sup>rms, OC: <sup>fi</sup>rms listed in other countries, O: Old period (i.e., before 2006), R: Recent period (2006–07).

released in 2006 and 2007, showed a signi<sup>fi</sup>cantly strong negative impact on market returns. Undoubtedly, the perception of investors towards phishing alerts evolved over time and with the availability of more knowledge about phishing alerts, investors realized the serious nature of such incidents. Any <sup>fi</sup>rms targeted after 2005 gave rise to the perception that they were not well equipped or were not doing enough to handle this type of event. This <sup>fi</sup>nding is similar to that of Kannan et al. who reported that the impact of security breaches was signi<sup>fi</sup>cantly more negative in the period following the dot-com bust [52] and that of Cavusoglu et al. who determined that “investors reacted more harshly to the recent attacks” [14]. The US as a country of listing, turned out to be a weak moderating factor as its coef<sup>fi</sup>cient was insigni<sup>fi</sup>cant and sometimes even positive in the CSRA. A probable explanation for this observation is that due to frequent exposure to phishing incidents, investors in the US may have become inert to phishing alerts and do not take them as a surprise any more. Financial services as a moderating factor showed a weak negative in<sup>fl</sup>uence. This was in line with existing literature, where researchers did not <sup>fi</sup>nd the <sup>fi</sup>nancial services sector to be signi<sup>fi</sup>cantly impacted by privacy or security breaches [1,52]. However, the interaction term of Holding and Finance showed a consistently strong and statistically signi<sup>fi</sup>cant negative reaction in the SA and the CSRA. This is an interesting result because it showed that the combined effect of the two factors was signi<sup>fi</sup>cant in determining the negative impact of phishing alerts on <sup>fi</sup>rm value.

It is known that sometimes the latent relationship between variables was not additive but multiplicative in nature [177], and this turned out to be true in this case. The signi<sup>fi</sup>cance of the interaction terms highlighted the importance of studying interaction variables. This is an important theoretical <sup>fi</sup>nding which may be useful in guiding IT <sup>fi</sup>rm value research in the future.

We used two different models for conducting the event study in this research. To the best of our knowledge, this is the <sup>fi</sup>rst time the FFM model is used in IS. Though the FFM is a more conservative model than the CAPM, it was a preferred approach as it allowed us to study global <sup>fi</sup>rms and “compensate for risk missed by the CAPM” [31]. Although the loss in market capitalization due to phishing alerts computed by the CAPM was higher than that obtained using the FFM, we found strong consistency in the results generated using both models.

## 6.1. Managerial implications

Through this research, we demonstrated that phishing had a signif icant negative impact on market value of global <sup>fi</sup>rms. In more recent years, the impact became more signi<sup>fi</sup>cant because investors

Table 4 Impact of interaction factors.

<table><tr><td colspan="5">Panel A: interaction effect of Holding * Finance</td><td colspan="5">Panel B: interaction effect of Holding * Recent</td></tr><tr><td>Models</td><td>CAPM</td><td></td><td>FFM</td><td></td><td>Models</td><td>CAPM</td><td></td><td>FFM</td><td></td></tr><tr><td>Firm ownership</td><td>HF</td><td>NHF</td><td>HF</td><td>NHF</td><td>Type of industry</td><td>HR</td><td>NHR</td><td>HR</td><td>NHR</td></tr><tr><td>Sample size</td><td>582</td><td>1360</td><td>546</td><td>1346</td><td>Sample size</td><td>552</td><td>1390</td><td>525</td><td>1367</td></tr><tr><td>Mean CAR</td><td>-0.02%</td><td>-0.06%</td><td>-0.02%</td><td>-0.05%</td><td>Mean CAR</td><td>-0.14%</td><td>-0.01%</td><td>-15.66%</td><td>-0.31%</td></tr><tr><td>Z test p-value</td><td>0.05</td><td>0.08</td><td>0.07</td><td>0.14</td><td>Z test p-value</td><td>0.01</td><td>0.17</td><td>0.01</td><td>0.30</td></tr><tr><td>Median CAR</td><td>-0.09%</td><td>-0.08%</td><td>-0.06%</td><td>-0.05%</td><td>Median CAR</td><td>-0.19%</td><td>-0.05%</td><td>-14.92%</td><td>-3.00%</td></tr><tr><td>Sign test p-value</td><td>0.02</td><td>0.06</td><td>0.05</td><td>0.18</td><td>Sign test p-value</td><td>0.00</td><td>0.16</td><td>0.01</td><td>0.30</td></tr><tr><td>Corrado&#x27;s rank test p-value</td><td>0.07</td><td>0.11</td><td>0.06</td><td>0.18</td><td>Corrado&#x27;s rank test p-value</td><td>0.02</td><td>0.22</td><td>0.01</td><td>0.35</td></tr><tr><td colspan="5">Panel C: interaction effect of Finance * Recent</td><td colspan="5">Panel D: interaction effect of US * Recent</td></tr><tr><td>Country of listing</td><td>US</td><td>OC</td><td>US</td><td>OC</td><td>Time of release</td><td>O</td><td>R</td><td>O</td><td>R</td></tr><tr><td>Sample size</td><td>993</td><td>949</td><td>958</td><td>934</td><td>Sample size</td><td>706</td><td>1236</td><td>706</td><td>1186</td></tr><tr><td>Mean CAR</td><td>-0.07%</td><td>-0.02%</td><td>-5.14%</td><td>-3.98%</td><td>Mean CAR</td><td>-0.14%</td><td>0.01%</td><td>-0.14%</td><td>0.01%</td></tr><tr><td>Z test p-value</td><td>0.04</td><td>0.13</td><td>0.06</td><td>0.20</td><td>Z test p-value</td><td>0.04</td><td>0.10</td><td>0.06</td><td>0.17</td></tr><tr><td>Median CAR</td><td>-0.11%</td><td>-0.08%</td><td>-8.00%</td><td>-3.75%</td><td>Median CAR</td><td>-0.11%</td><td>-0.08%</td><td>-0.10%</td><td>-0.05%</td></tr><tr><td>Sign test p-value</td><td>0.00</td><td>0.25</td><td>0.02</td><td>0.34</td><td>Sign test p-value</td><td>0.02</td><td>0.09</td><td>0.08</td><td>0.15</td></tr><tr><td>Corrado&#x27;s rank test p-value</td><td>0.02</td><td>0.35</td><td>0.02</td><td>0.36</td><td>Corrado&#x27;s rank test p-value</td><td>0.03</td><td>0.20</td><td>0.02</td><td>0.29</td></tr></table>

HF: holding <sup>fi</sup>rms in <sup>fi</sup>nancial services industry, NHF: <sup>fi</sup>rms other than HF, HR: holding <sup>fi</sup>rms with phishing alerts released in 2006–07, NHR: <sup>fi</sup>rms other than HR, FR: <sup>fi</sup>nancial services <sup>fi</sup>rms with phishing alerts released in 2006–07, NFR: <sup>fi</sup>rms other than FR, UR: US listed <sup>fi</sup>rms with phishing alerts released in 2006–07, NUR: <sup>fi</sup>rms other than UR.

Please cite this article as: I. Bose, A.C.M. Leung, Do phishing alerts impact global corporations? A <sup>fi</sup>rm value analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.006

Cross-sectional quantile regression results. Table 5

<table><tr><td colspan="5">Panel A: CAPM</td><td colspan="6">Panel B: FFM</td></tr><tr><td>Models</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>F1</td><td>F2</td><td>F3</td><td>F4</td><td>F5</td></tr><tr><td>Size</td><td>0.0002 (0.0003)</td><td>0.0003 (0.0003)</td><td>0.0003 (0.0003)</td><td>0.0003 (0.0003)</td><td>0.0003 (0.0003)</td><td>0.0001 (0.0003)</td><td>0.0002 (0.0003)</td><td>0.0002 (0.0003)</td><td>0.0003 (0.0003)</td><td>0.0002 (0.0003)</td></tr><tr><td>Attack history</td><td>0.0001 (0.0002)</td><td>0.0001 (0.0002)</td><td>0.0002 (0.0002)</td><td>0.0001 (0.0002)</td><td>0.0001 (0.0002)</td><td>0.0002 (0.0002)</td><td>0.0002 (0.0002)</td><td>0.0002 (0.0002)</td><td>0.0001 (0.0002)</td><td>0.0002 (0.0002)</td></tr><tr><td>Risk level</td><td>-0.0012 (0.0012)</td><td>-0.0009 (0.0011)</td><td>-0.0008 (0.0012)</td><td>-0.0009 (0.0011)</td><td>-0.0008 (0.0011)</td><td>-0.0008 (0.0012)</td><td>-0.0009 (0.0012)</td><td>-0.0010 (0.0012)</td><td>-0.0006 (0.0011)</td><td>-0.0008 (0.0012)</td></tr><tr><td>Holding</td><td>0.0004 (0.0007)</td><td> $0.0041^{***}$ (0.0016)</td><td> $0.0051^{***}$ (0.0017)</td><td> $0.0049^{***}$ (0.0018)</td><td> $0.0041^{***}$ (0.0016)</td><td>0.0005 (0.0007)</td><td> $0.0037^{**}$ (0.0017)</td><td> $0.0037^{**}$ (0.0018)</td><td> $0.0044^{**}$ (0.0017)</td><td> $0.0038^{**}$ (0.0017)</td></tr><tr><td>Finance</td><td>0.0013 (0.0013)</td><td> $0.0041^{***}$ (0.0015)</td><td> $0.0035^{*}$ (0.0019)</td><td> $0.0038^{**}$ (0.0016)</td><td> $0.0038^{**}$ (0.0016)</td><td>0.0019 (0.0013)</td><td> $0.0042^{**}$ (0.0017)</td><td>0.0022 (0.0020)</td><td> $0.0039^{**}$ (0.0016)</td><td> $0.0043^{***}$ (0.0017)</td></tr><tr><td>US</td><td>0.0009 (0.0008)</td><td>0.0009 (0.0008)</td><td>0.0008 (0.0009)</td><td>0.0009 (0.0008)</td><td>0.0004 (0.0012)</td><td>0.0008 (0.0008)</td><td>0.0008 (0.0008)</td><td>0.0006 (0.0009)</td><td>0.0008 (0.0008)</td><td>0.0010 (0.0013)</td></tr><tr><td>Recent</td><td> $-0.0018^{**}$ (0.0008)</td><td> $-0.0018^{**}$ (0.0007)</td><td> $-0.0055^{***}$ (0.0015)</td><td>-0.0013 (0.0010)</td><td> $-0.0020^{*}$ (0.0012)</td><td>-</td><td> $-0.0022^{***}$ (0.0008)</td><td> $-0.0057^{***}$ (0.0015)</td><td>-0.0013 (0.0009)</td><td>-0.0017 (0.0013)</td></tr><tr><td>Holding * Finance</td><td></td><td> $-0.0042^{**}$ (0.0018)</td><td> $-0.0051^{***}$ (0.0020)</td><td> $-0.0036^{*}$ (0.0019)</td><td> $-0.0042^{**}$ (0.0018)</td><td></td><td> $-0.0037^{*}$ (0.0019)</td><td> $-0.0040^{**}$ (0.0020)</td><td> $-0.0033^{*}$ (0.0018)</td><td> $-0.0037^{**}$ (0.0019)</td></tr><tr><td>Finance * Recent</td><td></td><td></td><td> $0.0041^{**}$ (0.0017)</td><td></td><td></td><td></td><td></td><td> $0.0045^{***}$ (0.0017)</td><td></td><td></td></tr><tr><td>Holding * Recent</td><td></td><td></td><td></td><td>-0.0019 (0.0014)</td><td></td><td></td><td></td><td></td><td>-0.0015 (0.0013)</td><td></td></tr><tr><td>US * Recent</td><td></td><td></td><td></td><td></td><td>0.0008 (0.0014)</td><td></td><td></td><td></td><td></td><td>-0.0004 (0.0015)</td></tr><tr><td>Constant</td><td>-0.0082 (0.0063)</td><td> $-0.0132^{**}$ (0.0062)</td><td> $-0.0120^{*}$ (0.0069)</td><td> $-0.0132^{**}$ (0.0065)</td><td> $-0.0127^{**}$ (0.0064)</td><td>-0.0041 (0.0064)</td><td>-0.0099 (0.0069)</td><td>-0.0076 (0.0072)</td><td> $-0.0111^{*}$ (0.0065)</td><td>-0.0100 (0.0070)</td></tr><tr><td>Sample size</td><td>1863</td><td>1863</td><td>1863</td><td>1863</td><td>1863</td><td>1815</td><td>1815</td><td>1815</td><td>1815</td><td>1815</td></tr><tr><td>Pseudo  $R^2$ </td><td>0.0026</td><td>0.0041</td><td>0.0051</td><td>0.0047</td><td>0.0041</td><td>0.0032</td><td>0.0042</td><td>0.0059</td><td>0.0047</td><td>0.0042</td></tr></table>

⁎⁎⁎ Significant at the 1% level. <sub>⁎</sub><sup>⁎</sup> ⁎⁎ Significant at the 5% level. ⁎ Significant at the 10% level. 关

increasingly expected <sup>fi</sup>rms to be well-prepared to face off phishing. Financial services <sup>fi</sup>rms were commonly targeted by phishers, and such <sup>fi</sup>rms had negative market returns. However, such a factor alone was not signi<sup>fi</sup>cant enough in determining the market reaction. The interaction analysis showed that holding companies in the <sup>fi</sup>nancial services sector received the most signi<sup>fi</sup>cant negative impact when phishing alerts were released. At the same time, while Litan reported that the number of phishing attacks in the US rose by nearly 40% in 2008 [62], the impact of phishing alerts on the US listed <sup>fi</sup>rms was surprisingly not so signi<sup>fi</sup>cant. Alerts that were released after 2005 created a strong negative impact on <sup>fi</sup>rm value. This meant that <sup>fi</sup>rms that had not taken any steps to prevent phishing needed to do so immediately. The loss of market capitalization of the order of several hundred million US dollars, as estimated in this research, should be a clarion call to <sup>fi</sup>rms to improve on their anti-phishing countermeasures. Firms could adopt technologies that prevented cloning of websites or caused poorer quality to the cloned websites. Existing technologies include content encryption and digital watermarking. Interested readers may also refer to [7] for more details about other technologies (e.g., traf<sup>fi</sup>c <sup>fl</sup>ow monitoring and proactive website scanning) to detect web cloning and fraudulent websites. Furthermore, <sup>fi</sup>rms could collaborate with anti-phishing organizations and Internet service providers in identifying and taking down of phishing websites.

## 6.2. Academic implications

Our research enriched existing academic literature in information security. We revisited the risk-components model proposed by Crockford and used it to study the impact of a security threat like phishing on <sup>fi</sup>rm value. We demonstrated the importance of considering moderating factors, and also the interactions between these factors to determine the impact on <sup>fi</sup>rm value. Past research had shown that security breaches that directly affect a <sup>fi</sup>rm's computer systems, such as virus, worms, and DoS attacks, caused a negative reaction. Phishing is a security breach that indirectly impacted the <sup>fi</sup>rms by targeting their customers and tarnishing their intangible resources like reputation and brand name. Yet its impact on <sup>fi</sup>rm value was strongly statistically signi<sup>fi</sup>cant as well. This implied that this indirect online criminal activity should not be ignored.

Another important contribution was the use of the FFM in conducting the event study. Phishing is a global phenomenon, and a study of phishing cannot be complete by considering only US companies. In fact, the negative impact of phishing is strongly statistically signi<sup>fi</sup>cant for all global <sup>fi</sup>rms, but is weakly signi<sup>fi</sup>cant for US <sup>fi</sup>rms only. This demonstrates the importance of considering non-US <sup>fi</sup>rms for studying a global phenomenon like phishing.

Finally, we showed that to appropriately analyze the impact of events on <sup>fi</sup>rm value, it was important to conduct the event study using stock prices and trading volume together with the SA and the CSRA on the same data. Most past event studies in IS have sought validation from some of these methods, but not all. Kaplan and Duchon have favored an approach where “using multiple methods increases the robustness of results because <sup>fi</sup>ndings can be strengthened through triangulation” [53]. The consistency in the results obtained using multiple methods in our research improved the validity of the analysis and strengthened the <sup>fi</sup>ndings.

## 6.3. Limitations of the study

We were not able to study the impact of phishing alerts for private <sup>fi</sup>rms and government organizations, although a number of phishing alerts were targeted to them. This was due to the limitation of the event study because it only allowed us to study publicly listed <sup>fi</sup>rms. Firms listed in countries, which did not make the phishing alerts publicly available, could not be studied as well. This research also suffered from the typical limitation of an event study — the assumption about ef<sup>fi</sup>cient markets. Some deviation from this assumption was possible, and that could affect the results. Finally, there is no denying that phishing alerts are an indirect measure of phishing attacks. Moore and Clayton have rightly lamented that the best approach to estimate “phishing activity would be to measure the number of emails delivered into inboxes and subsequently read by individuals” and yet “this email data are not available” [71]. We used the date of release of the alert as the event day. However, it is possible that there was a delay in the release of the alert. Although we used a large window of confounding events to overcome this, still there could be inaccuracies in the data that we couldn't control.

## 7. Conclusion and future research

Using a framework grounded on risk-components, we showed that phishing alerts led to statistically signi<sup>fi</sup>cant decrease in stock prices and trading volume of <sup>fi</sup>rms from 32 countries. The decrease in <sup>fi</sup>rm value was strongly signi<sup>fi</sup>cant for <sup>fi</sup>nancial holding companies, and for alerts released after 2005, and weakly signi<sup>fi</sup>cant for all <sup>fi</sup>rms listed in the US. We found that the release of each phishing alert could cause a loss of at least US\$ 411 million in market capitalization for a <sup>fi</sup>rm.

Future researchers can include alerts from more countries and propose alternative metrics for analyzing private <sup>fi</sup>rms. It will be interesting to categorize phishing attacks based on their nature, such as pharming, spear phishing, vishing, and smishing, and study their impact. Alternative event study models such as the multiple index model can be used to control for <sup>fi</sup>rm heterogeneity [44]. Park has used such a model by adding the currency exchange rate factor and a global stock index factor to the CAPM for studying international alliances [75]. Furthermore, it will be interesting to study whether voluntary disclosures made by <sup>fi</sup>rms about phishing attacks and announcements about adoption of anti-phishing measures lead to positive changes in their <sup>fi</sup>rm value. Finally, we encourage future researchers to continue to use data on global <sup>fi</sup>rms to overcome the “paucity of IT business value research in this area” [69], and provide better validation to <sup>fi</sup>rm value analysis.

## Acknowledgements

The authors thank Professor John Bacon-Shone, Director of Social Science Research Centre, The University of Hong Kong, for statistics advice and Thomson Reuters for retrieval of some delisted stock data. The second author also thank the generous <sup>fi</sup>nancial support of Swire Group to sponsor his trip to attend International Conference on Information Systems (ICIS) 2008 and valuable feedback received from the conference.

## Appendix A. Examples of typical phishing alerts

## Phishing alert from Millersmiles about Barclays

Barclays Message ID 79673 — Barclays Account Expire Noti<sup>fi</sup>cation

Date Reported: 23rd October 2005

Risk Level: MEDIUM

Apparent Sender: Barclays

Return Address: baccounts@barclays.co.ukN

Email Format: HTML

URL of Web Content: http://www.ctpacket.com/securesuite/olb/p LoginMember.do/BarclaysIBank.htm

Location: CT, US

Detailed server information: www.ctpacket.com detailed server information

Comments:

Email asks you to con<sup>fi</sup>rm/update/verify your account data at Barclays by visiting the given link. You will be taken to a spoof website where your details will be captured for the phishers.

\* Barclays never send their users' emails requesting personal details in this way.

\* The REAL URL of the spoof website is disguised as “https://ibank. barclays.co.uk/olb/p/LoginMember.do”.

\* The REAL URL of the spoof website looks nothing like the actual Barclays URL.

Content Email:

“We have noticed that you haven't used our online service recently, and we don't want you to miss out on the fantastic services available to you.”

## Phishing alert from Websense about Monster.com

Date: 03.28.2005

Threat Type: Phishing Alert

Websense® Security Labs™ has received reports of a new phishing attack that targets customers of Monster.com.

Users receive a spoofed email from the Monster Customer Support department saying that their account has been suspended, and they need to login to check their information.

This attack appears to be targeting companies who use the Monster. com Employers section. Employer users of Monster.com can post jobs on behalf of their company, and can search resumes in the Monsters database.

The phishing site is hosted in Korea and was up at the time of this alert.

Phishing email body:

Subject: Monster.com information

Dear Monster Customer,

We were unable to process the account is not suspended, please check your information by clicking here.

b URL REMOVED N

Monster Network b URL REMOVED N Customer Service

Phishing site screenshot

## Phishing alert from Factiva about Wing Lung Bank

Title: Hong Kong: HKMA alerts members of fraudulent website

Date: 15 September 2006

Publication: The Asian Banker Interactive

The Hong Kong Monetary Authority (HKMA) wishes to alert members of the public in Hong Kong to a fraudulent website with the domain name “www.winglungservice.com”. The website looks similar to the of<sup>fi</sup>cial website of Wing Lung Bank Ltd. (Wing Lung Bank). Wing Lung Bank has clari<sup>fi</sup>ed that it has no connection with the fraudulent website.

Wing Lung Bank has reported the case to the Hong Kong Police Force for further investigation. Anyone who has provided his or her personal information to the website or has conducted any <sup>fi</sup>nancial transactions through the website should contact Wing Lung Bank at 2770 2112 and any local Police Station or the Commercial Crime Bureau of the Hong Kong Police Force at 2860 5012.

## Appendix B. Sources of phishing alerts

<table><tr><td>Source</td><td>Before filtering of confounding news</td><td>After filtering of confounding news</td></tr><tr><td>Millersmiles</td><td>7407</td><td>1655</td></tr><tr><td>Websense</td><td>582</td><td>160</td></tr><tr><td>APWG JP</td><td>32</td><td>15</td></tr><tr><td>HKMA</td><td>113</td><td>30</td></tr><tr><td>MyCERT</td><td>24</td><td>8</td></tr><tr><td>Factiva</td><td>1207</td><td>67</td></tr><tr><td>Others</td><td>30</td><td>7</td></tr><tr><td>Total</td><td>9395</td><td>1942</td></tr></table>

Please cite this article as: I. Bose, A.C.M. Leung, Do phishing alerts impact global corporations? A <sup>fi</sup>rm value analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.006

Appendix C. Industry classi<sup>fi</sup>cation of sample data

<table><tr><td>Industries</td><td>Global Industry Classification Standard (GICS)</td></tr><tr><td>Financial services</td><td>Banking related GICSAsset management &amp; custody banks, diversified banks, investment banking &amp; brokerage, and regional banksFinance related GICSCansumer finance, diversified capital markets, other diversified financial services, specialized finance, and thrifts and mortgage financeInsurance related GICSLife &amp; health insurance, multi-line insurance, and property &amp; casualty insurance</td></tr><tr><td>IT &amp; Telecom</td><td>Application software, communications equipment, computer hardware, data processing &amp; outsourced services, diversified commercial &amp; professional services, electronic equipment manufacturers, integrated telecommunication services, internet software &amp; services, systems software, and wireless telecommunication services</td></tr><tr><td>Others</td><td>Broadcasting &amp; cable TV, building products, casinos &amp; gaming, food retail, human resource &amp; employment services, hypermarkets and supercenters, internet retail, IT consulting &amp; other services, movies &amp; entertainment, multi-utilities, publishing, railroads, real estate management &amp; development, semiconductors, and trading companies &amp; distributors</td></tr></table>

## Appendix D. Supplementary data

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2014.04.006.

## References

[1] A. Acquisti, A. Friedman, R. Telang, Is there a cost to privacy breaches? An event study, Proceedings of Twenty-seventh International Conference on Information Systems, 2006, pp. 1563–1580.

[2] F.K. Andoh-Baidoo, K.-M. Osei-Bryson, Exploring the characteristics of Internet security breaches that impact the market value of breached <sup>fi</sup>rms, Expert Systems with Applications 32 (3) (2007) 703–725.

[3] J.H. Anthony, W. Choi, S. Grabski, Market reaction to e-commerce impairments evidenced by website outages. International Journal of Accounting Information Systems 7 (2) (2006) 60–78.

[4] APWG, Phishing Activity Trends Report: Report for the Month of January, 2008, Anti-Phishing Working Group, 2008. 1–9.

[5] APWG, Global Phishing Survey: Trends and Domain Name Use in 2H2009, Anti-Phishing Working Group, 2010. 1-33.

[6] R. Benbunan-Fich, E.M. Fich, Effects of web traf<sup>fi</sup>c announcements on <sup>fi</sup>rm value, International Iournal of Electronic Commerce 8 (4) (2004) 161–181.

[7] I. Bose, A.C.M. Leung, Unveiling the mask of phishing: threats, preventive measures and responsibilities, Communications of the Association for Information Systems 19 (24) (2007) 544–566.

[8] I. Bose, A.C.M. Leung, Assessing anti-phishing preparedness: a study of online banks in Hong Kong, Decision Support Systems 45 (4) (2008) 897–912.

[9] A. Brandt, Phishing anxiety may make you miss messages, PC World 23 (10) (2005) 34.

[10] A. Broache, Ebay CEO: Phishers Threaten User Trust, ZDNet News, March 8th, 2007, http://news.zdnet.com/2100-1009\_22-6165628.html.

[11] M. Broadbent, P. Weill, B.S. Neo, Strategic context and patterns of IT infrastructure capability, The Journal of Strategic Information Systems 8 (2) (1999) 157–187.

[12] K. Campbell, L.A. Gordon, M.P. Loeb, L. Zhou, The economic cost of publicly announced information security breaches: empirical evidence from the stock market, Journal of Computer Security 11 (3) (2003) 431–448.

[13] D. Capocci, G. Hubner, Analysis of hedge fund performance, Journal of Empirical Finance 11 (1) (2004) 55–89.

[14] H. Cavusoglu, B. Mishra, S. Raghunathan, The effect of Internet security breach announcements on market value: capital market reactions for breached <sup>fi</sup>rms and Internet security developers, International Journal of Electronic Commerce 9 (1) (2004) 69–104.

[15] D. Chatterjee, C. Pacini, V. Sambamurthy, The shareholder-wealth and tradingvolume effects of information-technology infrastructure investments Journal of Management Information Systems 19 (2) (2002) 7–42

[16] D. Chatterjee, V.J. Richardson, R.W. Zmud, Examining the shareholder wealth effects of announcements of newly created CIO positions, MIS Quarterly 25 (1) (2001) 43–70.

[17] S. Chatterjee, A.S. Hadi, Regression Analysis by Example, 4th ed. Wiley-Interscience, Hoboken, N.J., 2006

[18] S. Chatterjee, B. Wernerfelt, The link between resources and type of diversi<sup>fi</sup>cation: theory and evidence, Strategic Management Journal 12 (1) (1991) 33–48.

[19] H. Chen, M.Y. Hu, J.C.P. Shieh, The wealth effect of international joint ventures: the case of U.S. investment in China, Financial Management 20 (4) (1991) 31–41.

[20] X. Chen, I. Bose, A.C.M. Leung, C. Guo, Assessing the severity of phishing attacks: a hybrid data mining approach, Decision Support Systems 50 (4) (2011) 662–672.

[21] C.J. Corrado, A nonparametric test for abnormal security price performance in event studies Journal of Financial Economics 23 (2) (1989) 385–396

[22] N. Crockford, An Introduction to Risk Management, Woodhead-Faulkner, Cambridge, 1986.

[23] M. Dardan, A. Stylianou, S. Dardan, The valuation of ecommerce announcements during <sup>fl</sup>uctuating <sup>fi</sup>nancial markets, Journal of Electronic Commerce Research 6 (4) (2005) 312–326.

[24] B. Dehning, V.J. Richardson, A. Urbaczewski, J.D. Wells, Reexamining the value relevance of e-commerce initiatives, Journal of Management Information Systems 21 (1) (2004) 55–82.

[25] B. Dehning, V.J. Richardson, R.W. Zmud, The value relevance of announcements of transformational information technology investments, MIS Quarterly 27 (4) (2003) 637-656

[26] B.L. Dos Santos, K. Peffers, D.C. Mauer, The impact of information technology investment announcements on the market value of the <sup>fi</sup>rm, Information Systems Research 4 (1) (1993) 1–24.

[27] P.F. Drucker, Management: Tasks, Responsibilities, Practices, 1st ed. Heinemann, London, 1974.

[28] J.B. Earp, A.I. Anton, L. Aiman-Smith, W.H. Stuf<sup>fl</sup>ebeam, Examining Internet privacy policies within the context of user privacy values, IEEE Transactions on Engineering Management 52 (2) (2005) 227–237.

[29] B. Ensor, M.d. Lussanet, T.v. Tongeren, L. Camus, UK Online Banking Forecast: 2007 to 2012, Forrester Research, 2007. 1–17.

[30] R. Faff, A simple test of the Fama and French model using daily data: Australian evidence, Applied Financial Economics 14 (2) (2004) 83–92.

[31] E.F. Fama, Market ef<sup>fi</sup>ciency, long-term returns, and behavioral <sup>fi</sup>nance, Journal of Financial Economics 49 (3) (1998) 283–306.

[32] E.F. Fama, K.R. French, The cross-section of expected stock returns, Journal of Finance 47 (2) (1992) 427–465

[33] E.F. Fama, K.R. French, Common risk factors in the returns on stocks and bonds, Journal of Financial Economics 33 (1) (1993) 3–56.

[34] E.F. Fama, K.R. French, Value versus growth: the international evidence, Journal of Finance 53 (6) (1998) 1975–1999.

[35] A. Garg, J. Curtis, H. Halper, Quantifying the <sup>fi</sup>nancial impact of IT security breaches, Information Management & Computer Security 11 (2) (2003) 74–83

[36] K. Gatzlaff, K.A. McCullough, The effect of data breaches on shareholder wealth, Risk Management and Insurance Review, 2010. 61–83.

[37] S. Gaudin, Identity Theft Driven by Dramatic Spikes in Threats, InformationWeek, March 28th, 2007, http://www.informationweek.com/news/security/showArticle. jhtml?articleID=198700822.

[38] J.L. Gibbs, K.L. Kraemer, A cross-country investigation of the determinants of scope of e-commerce use: an institutional approach, Electronic Markets 14 (2) (2004) 124–137.

[39] S. Goel, H.A. Shawky, Estimating the market impact of security breach announcements on <sup>fi</sup>rm values, Information & Management 46 (7) (2009) 404–410

[40] L.A. Gordon, M.P. Loeb, The economics of information security investment, ACM Transactions on Information and System Security 5 (4) (2002) 438–457.

[41] G. Goth, Phishing attacks rising, but dollar losses down, IEEE Security & Privacy Magazine 3 (1) (2005) 8.

[42] R. Hall, A framework linking intangible resources and capabilities to sustainable competitive advantage, Strategic Management Journal 14 (8) (1993) 607–618

[43] A. Hawker, Security and Control in Information Systems: A Guide for Business and Accounting, Routledge, London, 2000

[44] G.V. Henderson, Problems and solutions in conducting event studies, The Journal of Risk and Insurance 57 (2) (1990) 282–306.

[45] A. Hovav, J. D'Arcy, The impact of denial-of-service attack announcements on the market value of <sup>fi</sup>rms, Risk Management and Insurance Review 6 (2) (2003) 97-121.

[46] A. Hovav, J. D'Arcy, The impact of virus attack announcements on the market value of <sup>fi</sup>rms, Information Systems Security 13 (3) (2004) 32–40.

[47] A. Hovav, J. D'Arcy, Capital market reaction to defective IT products: the case of computer viruses, Computers & Security 24 (5) (2005) 409–424.

[48] K.S. Im, K.E. Dow, V. Grover, Research report: a reexamination of IT investment and the market value of the <sup>fi</sup>rm — an event study methodology, Information Systems Research 12 (1) (2001).103–117

[49] T. Jagatic, N. Johnson, M. Jakobsson, F. Menczer, Social phishing, Communications of the ACM 50 (10) (2006) 1–10.

[50] M. Jakobsson, S. Myers, Phishing and Countermeasures: Understanding the Increasing Problem of Electronic Identity Theft, Wiley-Interscience, Hoboken, N.J., 2007

[51] L. James, Phishing Exposed, Syngress, Rockland, Mass., 2005

[52] K. Kannan, J. Rees, S. Sridhar, Market reactions to information security breach announcements: an empirical analysis, International Journal of Electronic Commerce 12 (1) (2007) 69–91

[53] B. Kaplan, D. Duchon, Combining qualitative and quantitative methods in information systems research: a case study, MIS Ouarterly 12 (4) (1988) 571–586

[54] J.M. Karpoff, A theory of trading volume, Journal of Finance 41 (5) (1986) 1069-1087

[55] J.M. Karpoff, The relation between price changes and trading volume: a survey, Journal of Financial and Ouantitative Analysis 22 (1) (1987) 109–126.

[56] V. Katos, C. Adams, Modelling corporate wireless security and privacy, The Journal of Strategic Information Systems 14 (3) (2005) 307–321.

[57] O. Kim, R.E. Verrecchia, Trading volume and price reactions to public announcements, Journal of Accounting Research 29 (2) (1991) 302–321.

[58] E. Kirda, C. Kruegel, Protecting users against phishing attacks, The Computer Journal 49 (5) (2006) 554–561.

[59] R. Koenker, K.F. Hallock, Quantile regression, Journal of Economic Perspectives 15 (4) (2001) 143–156.

[60] W.R. Landsman, E.L. Maydew, Has the information content of quarterly earnings announcements declined in the past three decades? Journal of Accounting Research 40 (3) (2002) 797–808.

[61] A. Litan, Phishing Attacks Escalate, Morph and Cause Considerable Damage, Gartner Research, 2007. 1–14.

[62] A. Litan, The war on phishing is far from over Gartner Research, 2009. 1–12.

[63] K.D. Loch, H.H. Carr, M.E. Warkentin, Threats to information systems: today's reality, yesterday's understanding, MIS Quarterly 16 (2) (1992) 173–186.

[64] J. Lynch, Identity theft in cyberspace: crime control methods and their effectiveness in combating phishing attacks, Berkeley Technology Law Journal 20 (1) (2005) 259–300.

[65] T.J. Madden, F. Fehle, S. Fournier, Brands matter: an empirical demonstration of the creation of shareholder value through branding, Journal of the Academy of Marketing Science 34 (2) (2006) 224–235.

[66] M.T. Maloney, J.H. Mulherin, The complexity of price discovery in an ef<sup>fi</sup>cient market: the stock market reaction to the challenger crash, Journal of Corporate Finance 9 (4) (2003) 453–479.

[67] R. Martin, Cyberthreats Outpace Security Measures, Says McAfee CEO, InformationWeek, September 18th, 2007, http://www.informationweek.com/ news/management/showArticle.jhtml?articleID=201807230.

[68] A. McWilliams, D. Siegel, Event studies in management research: theoretical and empirical issues, Academy of Management Journal 40 (3) (1997) 626–657.

[69] N. Melville, K. Kraemer, V. Gurbaxani, Review: information technology and organizational performance: an integrative model of IT business value, MIS Quarterly 28 (2) (2004) 283–322.

[70] T. Moore, R. Clayton, Examining the impact of website take-down on phishing, Proceedings of the Anti-phishing Working Groups 2nd Annual eCrime Researchers Summit eCrime 2007, 2007, pp. 1–13.

[71] T. Moore, R. Clayton, How Hard Can It Be to Measure Phishing? 2010. 1–4.

[72] E. Noma, D. Olivastro, Are there enduring patents? Journal of the American Society for Information Science 36 (5) (1985) 297–301.

[73] W. Oh, J.W. Kim, V.J. Richardson, The moderating effect of context on the market reaction to IT investments, Journal of Information Systems 20 (1) (2006) 19–44.

[74] K. Palepu, Diversi<sup>fi</sup>cation strategy, pro<sup>fi</sup>t performance and the entropy measure, Strategic Management Journal 6 (3) (1985) 239–255.

[75] N.K. Park, A guide to using event study methods in multi-country settings, Strategic Management Journal 25 (7) (2004) 655–668.

[76] P. Petratos, Weather, information security, and markets, IEEE Security & Privacy 5 (6) (2007) 54–57.

[77] I.P.L. Png, C.Y. Wang, Q.H. Wang, The deterrent and displacement effects of information security enforcement: international evidence, Journal of Management Information Systems 25 (2) (2008) 125–144.

[78] P. Pradhan, Survey Shows Online Banking Needs Changes, Tech2.com India, January 29th, 2007, http://www.tech2.com/india/news/general/survey-shows-online-banking-needs-changes/3987/0.

[79] C. Saran, 90% of Online Adults Worried About Phishing, ComputerWeekly.com, August 30th 2007. http://www.computerweekly.com/Articles/2007/08/30/226464/90-of-online-adults-worried-about-phishing,htm.

[80] D. Schoder, P.-L. Yin, Building <sup>fi</sup>rm trust online, Communications of the ACM 43 (12) (2000) 73-79.

[81] A. Sorescu, V. Shankar, T. Kushwaha, New product preannouncements and shareholder value: don't make promises you can't keep, Journal of Marketing Research 44 (3) (2007) 468–489.

[82] M. Subramani, E. Walden, The impact of e-commerce announcements on the market value of <sup>fi</sup>rms, Information Systems Research 12 (2) (2001) 135–154.

[83] V. Swaminathan, C. Moorman, Marketing alliances, <sup>fi</sup>rm networks, and <sup>fi</sup>rm value creation, Journal of Marketing 73 (5) (2009) 52–69.

[84] R. Telang, S. Wattal, An empirical analysis of the impact of software vulnerability announcements on firm stock price JEEE Transactions on Software Engineering 33 (8) (2007) 544–557.

[85] B. von Solms, Information security — the third wave? Computers & Security 19 (7) (2000) 615–620.

[86] M. Wade, J. Hulland, The resource-based view and information systems research: review, extension, and suggestions for future research, MIS Quarterly 28 (1) (2004) 107–142.

[87] F.H. Westerhoff, Technical analysis based on price-volume signals and the power of trading breaks, International Journal of Theoretical & Applied Finance 9 (2) (2006) 227–244.

[88] R. Wetzel, Tackling phishing, Business Communications Review 35 (2) (2005) 46–51.

[89] C. Yue, H. Wang, BogusBiter: a transparent protection against phishing attacks, ACM Transactions on Internet Technology 10 (2) (2010) 1–31

![](/api/attachments/AGT2V4QF/fulltext/images/7fd142d2d2df1d6697a247f47a0dea02cb3e68d7c6c55bab358f9d28a02ca8de.jpg)

Indranil Bose is Professor and Group Co-ordinator of Management Information Systems at the Indian Institute of Management, Calcutta. He holds a B.Tech. from the Indian Institute of Technology, M.S. from the University of Iowa, and M.S. and Ph.D. from Purdue University. His research interests are in business analytics, information security, telecommunications, and business value of information technology. His publications have appeared in Communications of the ACM, Communications of AIS, Computers and Operations Research, Decision Support Systems, Ergonomics, European Journal of Operational Research, Information & Management, International Journal of Production Economics, Journal of Organizational Computing and Electronic Commerce, Journal of the American Society for Information

Science and Technology, Operations Research Letters etc. He serves on the editorial board of Decision Support Systems, Information & Management, Communications of AIS, and several other IS journals.

![](/api/attachments/AGT2V4QF/fulltext/images/0e20cac65182c81159848130541e13ea8ecf6ae7c99c850852b9dae42d9178d9.jpg)

Alvin Chung Man Leung is Assistant Professor at City University of Hong Kong. He received his Ph.D. from McCombs School of Business, The University of Texas at Austin. He obtained his BBA (Information Systems), BEng (Software Engineering), and Master of Philosophy degrees from the University of Hong Kong and MSc in Information, Risk, and Operations Management from the University of Texas at Austin. His research interests include social networks and information security. His works have been published in various journals and international conference proceedings such as Decision Support Systems, Communications of the Association of Information Systems, Communications of the ACM and the International Conference on Information Systems.

Please cite this article as: I. Bose, A.C.M. Leung, Do phishing alerts impact global corporations? A <sup>fi</sup>rm value analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.006
