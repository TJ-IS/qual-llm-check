---
otero_id: 7242
otero_key: "UHFJCKYT"
title: "Crowdfunding for Microfinance Institutions: The New Hope?"
authors: "Xuechen Luo; Ling Ge; Chong (Alex) Wang"
year: "2022"
journal: "MIS Quarterly"
doi: "10.25300/misq/2022/15406"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# CROWDFUNDING FOR MICROFINANCE INSTITUTIONS: THE NEW HOPE?<sup>1</sup>

Xuechen Luo School of Business and Management, Shanghai International Studies University Shanghai, CHINA {luoxuechen@shisu.edu.cn}

Ling Ge Department of Information Technology and Decision Sciences, G. Brint Ryan College of Business, University of North Texas, Denton, TX, U.S.A. {Ling.Ge@unt.edu}

Chong (Alex) Wang Guanghua School of Management, Peking University Beijing, CHINA {alexwang@gsm.pku.edu.cn}

As an innovative alternative financing channel, online crowdfunding holds the promise of empowering entrepreneurs and small businesses. However, doubts have been expressed as to whether online crowdfunding can deliver on its promises because of the lack of empirical evidence regarding its effects. In this study, we investigate the effects of prosocial crowdfunding on traditional microfinance institutions (MFIs). Combining multiple data sources, including data from Kiva.org and the Microfinance Information Exchange Market (MIX Market), we examine how access to crowdfunding influences MFIs sustainability and interest rates. We find that after joining Kiva, MFIs’ sustainability improves and interest rates decrease. Further investigation suggests that the changes mainly result from efficiency improvement, rather than from increased supply of low-cost funds. We propose that joining an online crowdfunding platform induces greater transparency and crowd monitoring, which motivates and empowers MFIs to improve operations and become more efficient.

Keywords: Crowdfunding, microfinance, prosocial lending, interest rate, sustainability, information disclosure, crowd monitoring

## Introduction

Online crowdfunding has emerged as an alternative financing channel for individuals and small enterprises. Crowdfunding platforms can effectively pool small contributions from a large number of individuals and match funds to projects, ventures, or other financial needs.<sup>2</sup> Using innovative business models, crowdfunding platforms target clients that are underserved by traditional financial institutions (Mackenzie 2015). The lack of access to financial services is one of the largest obstacles to socioeconomic development (Candelise 2015), and by improving such access, crowdfunding is expected to create both economic and social benefits. However, academic discussion and empirical evidence showing how online crowdfunding, with its innovative business model, creates value are lacking. Crowdfunding has even been criticized for causing overborrowing and other problems (e.g., Chava et al. 2017; DiMaggio and Yao 2019; Dore and Mach 2019). To shed light on the value of online crowdfunding, this paper examines how partnership with a crowdfunding platform— more specifically, the prosocial lending platform, Kiva— influences microfinance institutions (MFIs).

Prosocial lending, an important type of online crowdfunding, refers to the practice of funding projects with zero-interest loans through an online platform (e.g., Gajjala et al. 2011; Galak et al. 2011; Burtch et al. 2014). As a prominent example of financial inclusion improvement, prosocial lending allows poor people to raise funds for self-development projects from lenders who seek no financial returns. In practice, because borrowers targeted by prosocial-lending crowdfunding platforms often lack both access to basic financial/IT infrastructure and the necessary skills to present themselves and execute online transactions, platforms need to collaborate with local organizations to reach borrowers and facilitate loans.<sup>3</sup> Most of these local organizations are MFIs, which organize and present borrowers and projects on crowdfunding websites, receive and disburse loans, and manage repayments.

MFIs aim to alleviate poverty by providing small and uncollateralized loans (microloans) to local people (typically in poorer areas) to support self-development activities (Morduch 1999; Daley-Harris 2006). <sup>4</sup> To sustain their businesses, they charge interest on microloans to cover financial, operational, and risk costs. The annual interest rate is between 20% and 60%, and some MFIs charge even higher rates. The tension between sustainability and high interest rates is a primary concern surrounding MFIs: They need interest income to remain viable, but high interest rates significantly reduce the affordability of microloan services to the poor (Morduch 1999; Cull et al. 2009; Rosenberg et al. 2009; Dehejia et al. 2012). MFIs face many obstacles to reducing interest rates, including high default risk, limited access to low-cost capital (Roy and Chowdhury 2009; Bogan 2012), low operational efficiency (Drake and Rhyne 2002; Cull et al. 2007; Balkenhol and Hudon 2011), and insufficient monitoring of the use of subsidies and donations (e.g., Yunus 2000). Collaborating with online crowdfunding platforms could help alleviate these challenges. Understanding whether crowdfunding enables positive changes for MFIs, thus offering new hopes for the alleviation of poverty, is crucial.

In this paper, we investigate how crowdfunding affects MFIs’ sustainability and interest rates using data both from Kiva.org—the largest prosocial-lending crowdfunding platform—and from the Microfinance Information Exchange Market (MIX Market), an online database of MFI annual reports. With the assembled panel data, we gauge the causal link between Kiva partnerships and changes in sustainability and interest rates using different empirical methods, including the difference-in-differences model with matched sample (e.g., Angrist and Pischke 2009), the tree-based approach (Yahav et al. 2016), and the Heckman selection model. The results consistently show that a Kiva partnership leads to better sustainability and lower interest rates, confirming the positive effects of crowdfunding on MFIs. Interestingly, further analysis reveals that sustainability improves first and interest rate reduction follows. This dynamic pattern implies that MFIs reduce interest rates, which benefits borrowers, after they have acquired enough margin to survive.

We also explore the underlying mechanisms that lead to improved sustainability and lower interest rates by investigating changes in MFIs’ capital costs (financial expenses) and efficiency (operational efficiency and risk management effectiveness). We find that the financial expenses of MFIs do not decrease after joining Kiva, but their risk management effectiveness and operational efficiency improve. These findings suggest that declines in interest rates and increased sustainability might not result directly from lower capital costs. Instead, collaboration with online crowdfunding seems to induce more fundamental changes in operational efficiency and risk management effectiveness.

Our study contributes to several aspects of the information systems (IS) literature. First, we contribute to the literature on crowdfunding. The extant literature has focused on how the platform works. Prior research has revealed valuable insights regarding platform mechanisms and designs and has identified factors that affect projects’ funding success and lenders’ decisions (e.g., Lin et al. 2013; Burtch et al. 2013, 2014; Liu et al. 2015; Lin and Viswanathan 2016; Kim and Viswanathan 2019). Only recently have studies emerged that examine the societal outcomes of crowdfunding (e.g., Blaseg and Koetter 2015; Burtch and Chan 2019; Kim and Hann 2019). Evidence from these studies suggests that crowdfunding can serve as an effective financing source for ventures when banks are stressed (Blaseg and Koetter 2015) and can help individuals who face financial distress as a result of medical expenses (Burtch and Chan 2019) or because of tightened constraints on credit (Kim and Hann 2019). <sup>5</sup> Our study examines the effect of online crowdfunding at the organizational level and demonstrates with convincing evidence that raising money from “the crowd” has positive effects on participating organizations. Moreover, we explicate the underlying mechanisms that lead to improved sustainability and lower interest rates and establish that crowdfunding is not only an innovative and viable financing channel but also enables positive managerial changes in organizations.

Second, this study enriches the literature on the impact of information technology (IT) (e.g., Brynjolfsson and Hitt 2000; Brynjolfsson and Simester 2011). IT impact research highlights the important role of information technologies by demonstrating how various information systems and technologies enable changes and affect businesses, organizations, economies, and social welfare (e.g., Tam 1998; Bhargava and Choudhary 2004; Ray et al. 2005; Ghose et al. 2006; Xu and Zhang 2013; Weiss and Tarchinskaya 2015; Zhang and Zhang 2015). Online platforms have already profoundly changed how offline businesses operate and are organized. Our study provides new perspectives and evidence of the transformative power of internet-enabled crowdfunding platforms. It also sheds light on how general multisided platforms affect the individuals and organizations who carry out transactions on these platforms. We also contribute to the literature on information technology for development (IT4D) (e.g., Venkatesh and Skykes 2013; Jha et al. 2016; Leong et al. 2016; Srivastava et al. 2016; Venkatesh et al. 2019). This stream of literature examines how the use of information technology can address societal problems such as the alleviation of poverty (Jha et al. 2016) and social inclusion (Andrade and Doolin 2016), especially in less developed countries. Our study shows how online crowdfunding empowers the development of microfinance, which targets the alleviation of poverty.

Third, we extend the academic discussion about microfinance. Our study reveals that adopting internet financing has significant implications for MFIs. Based on the potential offered by new information technologies, research in microfinance, which has traditionally been viewed as a subfield of economics and finance, might explore opportunities to change the microfinance industry through IT innovations in ways that better serve underprivileged populations.

The rest of the paper is organized as follows. In the following section, we introduce the research background and develop empirical conjectures. Then, we describe the data and our empirical approaches. The results are reported in the next section, followed by a series of robustness checks and falsification tests. We then conduct additional analysis to examine the underlying mechanisms of crowdfunding effects. Finally, we conclude with a discussion about the theoretical and managerial implications and limitations of the study.

## Background and Theoretical Development

## About Kiva

Kiva.org, the dominant global prosocial-lending crowdfunding platform, is our empirical context (e.g., Gajjala et al. 2011; Galak et al. 2011; Burtch et al. 2014). Kiva pursues a mission of poverty alleviation by facilitating crowd-funded interest-free loans for underserved individuals and groups in developing countries. Kiva’s loans since its launch in 2005 exceed \$1.46 billion from more than 1.9 million lenders, helping more than 3.6 million borrowers in 82 countries. Despite its rapid growth, Kiva has maintained a surprisingly high repayment rate of 95.7%.

Kiva collaborates with local organizations (field partners) who are responsible for posting and managing loan projects. Most of the field partners are MFIs in different countries (Kiva 2015).<sup>6</sup> The partnership between Kiva and its field partners works as follows. A field partner selects a local project, collects the required information (including the borrowers’ background, the funding goal, and the intended use of funds), and submits a loan application to Kiva. After Kiva’s approval, the project is presented on Kiva’s website for funding. Like on other crowdfunding websites, lenders from anywhere can make (small) contributions as loans to the project. However, Kiva lenders do not receive interest nor are they refunded if borrowers default; they lend for altruistic reasons (Burtch et al. 2013). When the funding goal is reached, funds are transferred to the field partner for disbursement. Since its launch, Kiva has accumulated a stable pool of prosocial lenders. According to Kiva, around 98% of loan projects posted on Kiva have been successfully funded.

Although Kiva lenders do not receive any interest on loans, field partners charge borrowers at their own discretion. According to data disclosed on Kiva, the average interest rate charged by field partners is 33.39%.<sup>7</sup> Field partners monitor the project progress, collect repayments, and continuously update loan information on Kiva. After the loan is repaid (based on an individualized loan repayment schedule), lenders on Kiva receive repayments. They can then withdraw the money from Kiva or use the money to fund other projects. As a nonprofit organization, Kiva does not charge field partners, borrowers, or lenders, nor does it take any commission on loans. All Kiva’s operating expenses are covered with external funding that is independent of the loan funds contributed by lenders on the platform.

## The Impact of Kiva on Microfinance Institutions

Partnership with Kiva helps MFIs, whose operations are primarily offline, establish an online presence. A partnership with Kiva influences MFIs through two main channels. First, taking advantage of the internet and its online platform, Kiva has access to a global pool of lenders who contribute interestfree capital and thus gives MFIs access to low-cost funding. Traditionally, MFIs have relied primarily on donations, government grants, and commercial or noncommercial loans for funding (Cull et al. 2009; Bogan 2012; Tchuigoua 2014).<sup>8</sup> Donations and government grants are interest-free but in limited supply. Noncommercial loans from institutions such as the World Bank have low interest rates but supply also is limited and competition for such loans is fierce (Bogan 2012; Tchuigoua 2014). Commercial loans often have high qualification requirements for MFIs and higher interest rates. As a result, MFIs’ capital costs are often high, making sustainability more difficult and driving up the interest rate that they must charge to cover costs (Roy and Chowdhury 2009; Bogan 2012). In contrast, Kiva loans are interest free, and millions of prosocial lenders ensure a stable supply. Therefore, MFIs can reduce their cost of capital by using Kiva. Lower capital costs make it easier for them to become sustainable and to create a margin that allows for lower interest rates.

However, the potential financial slack resulting from lower capital costs also might have negative consequences. First, financial slack might make MFIs lose their focus on efficiency. With limited resources, MFIs must deploy resources efficiently and make prudent decisions (Spann and Hudson 1988; Starr and MacMillan 1990; Baker et al. 2000). When abundant and low-cost funding from crowdfunding reduces such pressure, MFIs are more likely to be satisfied with their performance and less motivated to control operation costs and manage risks (e.g., Leibenstein 1966, 1978; Bergström 2000; George 2005). Second, excess deployable resources might even tempt MFI managers to pursue their own agendas, which could be detrimental to the institution (Jensen 1986; Denis 2011). Previous research on MFIs has found evidence of such inefficiency. For instance, Garmaise and Natividad (2013) determined that with subsidized credit, MFI managers tend to hire more noncore staff, resulting in increased administrative expenses and decreased productivity. Similarly, Bogan (2012) and Cull et al. (2009) showed that MFIs are likely to invest in riskier projects when they have substantial low-cost capital (e.g., grants and subsidized loans). Therefore, the cost savings achieved with Kiva loans do not necessarily lead to better sustainability or lower interest rates.

The second channel through which Kiva makes an impact is crowd monitoring. To establish their online presence, MFIs need to follow the procedures that Kiva sets and enforces in initiating and managing loans. Kiva loans require extensive information disclosure. The details of every project, as well as periodic status updates on the repayments of each loan, are available on the platform. The key indicators of an MFI, such as default rate, interest rate, and delinquency rate, also are disclosed. Lenders (the crowd) can examine project profiles and performance, as well as the MFI’s overall performance, which thus exerts monitoring pressure on MFIs.

Crowd monitoring can have positive effects on MFIs. Traditionally, MFIs are subject neither to strong regulation and supervision nor to compulsory reporting requirements (McGuire 1999; Garmaise and Natividad 2010). Without external monitoring, MFIs might have exhibited organizational inefficiency (Callen et al. 2003; Glaeser 2003; Hartarska 2005; Servin et al. 2012), mismanagement of resources (Haq et al. 2010), or inefficient expansion (Garmaise and Natividad 2013). However, after joining Kiva and establishing an online presence, the heightened information disclosure requirements put each project and each MFI under the scrutiny of online lenders. Hiding or manipulating information becomes more difficult when project-level details are openly accessible (Cho 2015). Selfinterested actions or shirking are reduced because managers’ actions and consequences are more observable and may be questioned by lenders (Berger and Hann 2003). More positively, because records are disclosed on the platform, crowd monitoring might also create a sense of achievement when loans are successfully funded, paid back, and displayed for lenders. Therefore, with Kiva, MFI managers are more motivated to work in accordance with lenders’ interests and the organization’s goals. They are more likely to improve efficiency, reduce costs, and avoid overcompensating themselves. Moreover, the formalized information collection and reporting process increases the frequency and intensity of progress checks and risk management for the funded projects.

In addition, each MFI has a rating assigned by Kiva, which is based on Kiva’s evaluation of the MFI’s governance, management, transparency, business model, and financials. Regular evaluation improves transparency and information quality (see, e.g., Bushman and Smith 2001; Healy and Palepu 2001; Fan and Wong 2005). The Kiva rating offers effective external governance, enforces standards on operations, and disciplines MFIs to perform well (Garmaise and Natividad 2010). Therefore, we expect that monitoring from the crowd and from Kiva motivates MFIs to improve efficiency and to achieve better financial performance, contributing to better sustainability and lower interest rates.

To summarize, crowdfunding can lead to profound changes in MFIs. First, access to low-cost Kiva loans is intended to lower capital costs. However, financial slack, which takes pressure off MFI management, might lead to problems such as lower efficiency, higher costs, and higher risks. Second, more intensive information disclosure requirements and crowd monitoring motivate MFIs to improve efficiency and can mitigate the possible negative effects of financial slack. With greater efficiency, MFIs can improve their sustainability, which offers a better chance of reduced interest rates. Therefore, overall, as long as the positive effects of low-cost capital and crowd monitoring exceed the potential negative effects of financial slack, Kiva partnerships help MFIs achieve better sustainability, allowing them to focus more on their social mission of helping borrowers and to share the benefits of their sustainability with borrowers by lowering interest rates (Morduch 1999; Malkin 2008).

## Empirical Methodology

## MFI Data

We obtained MFI data from MIX Market (http://www.themix.org). MIX Market is a digital data platform that allows MFIs to share and exchange information. At the time of our data collection, the MIX Market dataset included annual reports of 2,796 MFIs in 121 countries, covering the period between 1995 and 2015. Each report contains information about the MFI’s financial performance, loan portfolios, and operations. MIX Market offers the most comprehensive dataset of MFI operations and it has been used in many recent studies (e.g., Cull et al. 2009; Ahlin et al. 2011; Quidt et al. 2018). Following the due diligence procedures suggested in the literature (Ahlin et al. 2011; Hermes et al. 2011; Quidt et al. 2018), we carefully examined the data and eliminated those entries that had a significant number of missing fields or unusable inputs. The final dataset contains unbalanced panel data of 1,477 MFIs over the period 1995- 2014, for a total of 6,235 MFI-year observations.

## KIVA Data

The dataset collected from the Kiva.org website contains information of all projects and field partners from the platform’s launch in 2005 to June 1, 2014. During this period, borrowers from 81 countries posted a total of 670,865 projects and raised more than \$550 million. For each project, the available details include description, funding goal, repayment schedule, and the field partner managing the project. For each field partner, we observed its name, the time it joined Kiva, and its Kiva rating.

We manually matched the Kiva and MIX Market data to identify the MFIs appearing in both datasets: 107 Kiva field partners have records in the MIX dataset, 96 of which have records for the periods both before and after they joined Kiva. We also collected country-level data from the World Bank, China Economic Information Center (CEIC), and Federal Reserve Economic Data (FRED). Our panel of observations is at the MFI-year level.

## Empirical Study Design

## Difference-in-Differences Mode

In our context, MFIs joined Kiva in different years, and some of the MFIs did not join Kiva during the observation period. The temporal differences in Kiva partnerships allow for a difference-in-differences (DID) design, which compares the differences between periods before and after MFIs joined Kiva (Kiva MFIs) to the same differences for MFIs that did not join (non-Kiva MFIs). DID models are often considered to be quasi-experimental designs that can identify causal relationships. The DID approach mitigates the effects of confounding factors (e.g., unobserved trends and co-occurring events) (Chevalier and Mayzlin 2006; Angrist and Pischke 2009; Manchanda et al. 2015; Gertler et al. 2016; Wing et al. 2018).

To understand the DID design, consider Kiva’s impact on the interest rate charged by Kiva MFI i that joined Kiva in year t. The within-subject comparison of a Kiva MFI captures the difference in interest rates before and after year t. Kiva might have caused this change, but it might just as well be the result of a time trend or other factors, such as macrolevel economic conditions, government regulations, or natural disasters. To control for such confounding effects, we used the before-andafter interest rate change of non-Kiva MFI j in year t to serve as a counterfactual—that is, the interest rate change of Kiva MFI i if it had not joined Kiva in year t. The difference between these two differences then reflects the effect of Kiva. The method has been widely used in the literature to identify causal relationships (e.g., Jin and Leslie 2003; Acharya and Subramanian 2009; Chan and Ghose 2014). For example, with the same DID design, Jin and Leslie (2003) studied the effect of information on product quality, and Chan and Ghose (2014) examined the causal relationship between online intermediaries and HIV transmission.

Specifically, we estimated the following DID model.

$$
\begin{array}{r} D e p _ {i t} = \beta_ {0} + \beta_ {1} A f t e r K i v a _ {i t} + C o n t r o l V a r i a b l e s _ {i t} \\ + u _ {i} + \delta_ {t} + \varepsilon_ {i t}, \end{array}\tag{1}
$$

where i indexes an MFI and t indexes a year. $D e p _ { i t }$ represents the dependent variables. In the main analysis, we are interested in MFIs’ sustainability and interest rate. After Kiva is a dummy variable that equals one if the MFI is a field partner during the year, and zero otherwise. ?????????????? ?????????????????? includes the age and size of MFI i in year t, as well as GDP per capita, population, workforce participation, and inflation of that MFI’s country. $u _ { i }$ and $\delta _ { t }$ denote MFI- and time-fixed effects, respectively. For all models, we clustered the error terms at the MFI level to account for the autocorrelation that may present in panel data (Bertrand et al. 2004). The MFI-level fixed effect controls for the time-invariant heterogeneity of MFIs and other timeinvariant, unobserved confounding factors (Angrist and Pischke 2009; p. 221). The DID estimator $\beta _ { 1 }$ in Equation (1) captures the effect of Kiva.

## DID with Matched Sample

Joining Kiva (the treatment) is likely not random in our context. MFIs that did not join Kiva during the observation period could be different from the ones that did, which leads to the concern that non-Kiva MFIs might not serve as good control groups because of the self-selection issue (Autor 2003; Angrist and Pischke 2009; Manchanda et al. 2015). In quasiexperiments with nonequivalent treatment and control groups, some characteristics that show significant differences between the treatment group and the control group might interact with the treatment, thus affecting the validity of identification (Campbell and Stanley 1963). For example, mature MFIs might be more likely to become Kiva partners who can also benefit more from the partnership.

To address selection bias due to observables and to obtain more similar Kiva MFI and non-Kiva MFI groups (Rosenbaum and Rubin 1983; Manchanda et al. 2015; Yahav et al. 2016), we adopted a matched-sample DID design using the propensity score matching (PSM) method (Chen et al. 2018). Kiva MFIs were matched with non-Kiva MFIs based on their propensity to join. We conducted PSM using the oneto-one nearest-neighbor method, without replacement, under a caliper size of 0.05 times the standard deviation of the propensity scores (Goh et al. 2013; Chan et al. 2014; Dambra and Gustafson 2021). To compute the propensity score, we used variables of MFIs’ characteristics, including age, size, personnel (number of staff members), and return on assets (ROA); loan portfolio characteristics (e.g., percentage of loans to women, cost per loan, and write-off ratio); and country variables (e.g., population and GDP per capita). The PSM obtained a valid matched sample of 146 MFIs and 990 MFIyear observations.

Figure 1 demonstrates the distribution of propensity scores of the treatment group (Kiva MFIs) and control group (non-Kiva MFIs) before and after matching. It shows that the propensity score distribution of the matched control MFIs is very similar to that of the treated MFIs. We report the statistics of the two groups of MFIs before and after the matching in Appendix A (Table A1). As shown, the differences in the characteristics of the treated and control groups are reduced and become statistically insignificant after the matching. We then estimated the DID model again using the matched sample.

## Alternative Identification Approaches

To further strengthen causal identification of the impact of Kiva partnership on MFIs, we considered two additional methods: the tree-based approach (Yahav et al. 2016) and the Heckman selection model (Heckman 1979; Chen et al. 2009; Liu et al. 2014).

The tree-based method helps to address two concerns about the matched sample DID. First, data dredging might occur when researchers selectively report models that offer the best or the expected results. Second, objects with similar propensity scores could still have very different profiles (Miller 2013; Yahav et al. 2016). The tree-based method classifies observations into subgroups using a decision-tree algorithm (Yahav et al. 2016). Within each subgroup, the observations have a similar propensity to join. Because subgroups are automatically separated without modeling choices, the approach helps to avoid data dredging. Moreover, by design, the algorithm separates the observations based on variations in observed variables. For instance, separating by MFI age can lead to two subgroups of MFI observations: mature ones and new and young ones. Thus, observations that are separated into the same subgroup would have similar profiles and a similar propensity to join, alleviating the second concern about the PSM method. Given the setup, by comparing the performance of Kiva MFIs and non-Kiva MFIs within the same subgroup (the terminal node), we can identify Kiva’s effect.

The Heckman selection model offers a means of correcting for non-randomly selected samples (Heckman 1979). It further alleviates endogeneity concerns for self-selection and helps to correct potential self-selection bias due to unobserved factors (Chen et al. 2009; Aral et al. 2012; Goh et al. 2013; Liu et al. 2014). Although the PSM method accounts for selection on observables, it does not allow for selection on unobservable factors (Goh et al. 2013).

![](/api/attachments/UHFJCKYT/fulltext/images/7cfcd85f9ccd0277fe13d975715e4cf68ca506cf5ea4bd8e15189509644f60f1.jpg)

Figure 1. Distribution of Propensity Scores for Treatment Groups and Control Groups before and after Matching

<table><tr><td colspan="2">Table 1. Variable Descriptions</td></tr><tr><td>Variable</td><td>Definition</td></tr><tr><td colspan="2">Main variables</td></tr><tr><td>OSS</td><td>Financial revenue / (financial expense + impairment loss + operating expense), measuring the ability of MFIs to cover their costs with operating revenues</td></tr><tr><td>Interest rate</td><td>Yield on gross portfolio (nominal) = interest and fees on loan portfolio / loan portfolio</td></tr><tr><td>After Kiva</td><td>Dummy variable of whether the MFI joins Kiva; one if yes, zero otherwise</td></tr><tr><td colspan="2">Control variables</td></tr><tr><td>MFI age</td><td>Indicator of the maturity of the MFI (new, young, and mature).</td></tr><tr><td colspan="2">MFI size</td></tr><tr><td>Number of borrowers</td><td>Number of active borrowers</td></tr><tr><td>Average loan size</td><td>Average loan portfolio / average number of active loans</td></tr><tr><td>Asset to loan ratio</td><td>Assets / average gross loan portfolio</td></tr><tr><td>GDP per capita</td><td>GDP per capita of the MFI&#x27;s country</td></tr><tr><td>Population</td><td>Population of the MFI&#x27;s country</td></tr><tr><td>Workforce participation</td><td>Labor force participation rate = labor force / population aged 15+</td></tr><tr><td>Inflation</td><td>Consumer price inflation of the MFI&#x27;s country</td></tr></table>

The Heckman correction procedure is a two-stage estimation method. The first stage explicitly models the choice of joining Kiva and derives an inverse Mills ratio (IMR), which is an estimate of the correlation between unobserved determinants of the decision and the dependent variables. The second stage estimates the dependent variables on the independent variables, as well as the IMRs that capture the effect of unobserved factors (Thirumalai and Sinha 2013). A significant IMR coefficient indicates the presence of selection bias (Byoun and Moore 2003; Lennox et al. 2012; Thirumalai and Sinha 2013).

## Variables

Table 1 summarizes the variables considered in our main analysis. The measures of sustainability and interest rate are based on the extant microfinance literature (e.g., Cull et al. 2009; Ahlin et al. 2011; Garmaise and Natividad 2013). Specifically, sustainability is measured by operational selfsufficiency (OSS): the ratio of annual financial revenue to annual total expense, which is the sum of financial expense, operating expense, and loan loss provision expense (impairment loss) (Ahlin et al. 2011; Cull et al. 2009). OSS indicates whether MFIs can generate sufficient revenue to cover their costs (Morduch 1999; Ahlin et al. 2011). An MFI with OSS greater than 100% has sufficient revenue to cover its costs and thus can sustain itself. To measure the interest rate, we used yield on gross portfolio, which is the total cash financial revenue from lending divided by the average gross loan portfolio. We used this measure, which represents the average interest rate charged by MFIs, because detailed information on individual loans was not available. It is a commonly adopted measure of annual interest rates in microfinance literature (e.g., Cull et al. 2009; Dehejia et al. 2012; Quidt et al. 2018). A higher yield on gross portfolio suggests that borrowers are, on average, paying more for microloans.

Our independent variable of interest is After Kiva. After Kiva equals one if the MFI is a field partner in the year, zero otherwise. <sup>9</sup> Because the extent to which MFIs use Kiva varies, we also considered the number of projects that each MFI listed on Kiva in each year (number of projects on Kiva) as an alternative independent variable.

We controlled for observable differences of MFIs and for macroeconomic conditions that may affect MFIs’ performance during the observation period. MFI age and MFI size account for the differences in MFI experiences and in their scale of operations (e.g., Cull et al. 2009; Mersland and Strøm 2009; Ahlin et al. 2011). MFI age measures each MFI’s maturity level based on the year of establishment and has three categories: new, young, and mature. Following the literature, MFI size is measured with three variables: number of borrowers, average loan size, and asset-to-loan ratio (Ahlin et al. 2011). For macroeconomic conditions, we used country-level variables of the MFI’s home country: GDP per capita, population, workforce participation, and inflation (Ahlin et al. 2011; Strøm et al. 2014; Quidt et al. 2018).

Table 2 reports the summary statistics. The mean of OSS is around 1.16, and the mean of the interest rate for all MFIs over the observation period is 31.86%, which is similar to the numbers reported in other papers. Around 5.7% of the observations belong to the “after Kiva” period.

## Results and Robustness Checks

## Kiva’s Impact on OSS and Interest Rates

Table 3 reports the results of our DID analysis of Kiva’s effect on OSS and interest rates. Columns 1 and 2 report the estimates of the DID model using the full sample; coefficient estimates for After Kiva are 0.0415 (OSS) and -0.0129 (interest rate). Columns 3 and 4 report the results of the matched-sample DID analysis, which further controls for bias resulting from selection on observables. Coefficient estimates for After Kiva are 0.1006 (OSS) and -0.0138 (interest rate). All estimates of the main effect are statistically significant. <sup>10</sup> The results suggest that Kiva leads to increased OSS and decreased interest rates. A back-of-the-envelope calculation suggests that, after becoming a field partner with Kiva, an MFI’s OSS improves by 3.70% and its interest rate drops by 4.10%.<sup>11</sup>

## Robustness Checks

As discussed in the Empirical Study Design section above, we performed several robustness checks to corroborate findings from the DID analysis. To further alleviate concerns of selfselection, we performed robustness checks using: (1) a treebased approach for treatment effect identification and (2) a Heckman selection model. We also used an alternative measure of Kiva partnership and checked for reverse causality.

## Tree-Based Approach

Figure 2 illustrates the resulting tree and statistical test results.<sup>12</sup> In the boxes under each node in Figure 2, n (Kiva, no Kiva) states the sample size. PE is the mean difference between Kiva and non-Kiva MFIs within the node. We compared the OSS and interest rate of Kiva MFIs vs. non-Kiva MFIs within each terminal node that had enough (balanced) observations of both. In total, seven terminal nodes were selected (i.e., Nodes 6, 7, 13, 14, 20, 21, and 23).

According to Figure 2, a Kiva partnership has positive and significant effects on OSS for MFIs in Nodes 6 and 7. In other nodes, the differences are not statistically significant. We note that Nodes 6 and 7 are featured with observations from year 2007 to year 2009—the period during which more than half of the Kiva MFIs in our sample joined the platform. Regarding interest rates, six of the seven nodes exhibit negative effects; the exception, Node 21, shows an insignificant positive effect. The two significant nodes, Nodes 13 and 23, are featured with observations from periods after 2009, which suggests that observations after 2009 show a more significant decrease in the interest rate among Kiva MFIs. Combining the results of OSS and the interest rate, we infer that the changes in OSS and in interest rates happened at different time periods. Kiva helped MFIs improve sustainability at the beginning; after MFIs gained enough of a margin to survive, they focused on improving borrowers’ welfare by reducing interest rates. The tree-based analysis reveals heterogeneity in the effects of Kiva, which is an advantage of the tree-based method (Yahav et al. 2016). We discuss the dynamic features of Kiva effects in the Falsification Test section below.

<table><tr><td colspan="7">Table 2. Summary Statistics of Variables</td></tr><tr><td>Variable</td><td>Obs.</td><td>Mean</td><td>Std. dev.</td><td>Median</td><td>25th percentile</td><td>75th percentile</td></tr><tr><td colspan="7">Main variables of interest</td></tr><tr><td>OSS</td><td>6,083</td><td>1.1556</td><td>0.2841</td><td>1.1328</td><td>1.0203</td><td>1.2869</td></tr><tr><td>Interest rate</td><td>5,592</td><td>0.3186</td><td>0.1221</td><td>0.2907</td><td>0.2242</td><td>0.3894</td></tr><tr><td>After Kiva</td><td>6,215</td><td>0.0566</td><td>0.2312</td><td>0</td><td>0</td><td>0</td></tr><tr><td colspan="7">Control variables</td></tr><tr><td colspan="7">MFI age</td></tr><tr><td>Age (young)</td><td>6,215</td><td>0.1884</td><td>0.3911</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Age (mature)</td><td>6,215</td><td>0.7340</td><td>0.4419</td><td>1</td><td>0</td><td>1</td></tr><tr><td colspan="7">MFI size</td></tr><tr><td>Asset-to-loan ratio</td><td>6,215</td><td>2.6652</td><td>1.9349</td><td>2.3742</td><td>1.7694</td><td>3.2010</td></tr><tr><td>Number of borrowers (1000 s)</td><td>6,215</td><td>91.860</td><td>431.05</td><td>13.057</td><td>3.815</td><td>45.422</td></tr><tr><td>Average loan size</td><td>6,215</td><td>1263.0</td><td>2618.0</td><td>524</td><td>188</td><td>1383</td></tr><tr><td>GDP per capita (natural log of)</td><td>6,215</td><td>7.7154</td><td>0.9600</td><td>7.6863</td><td>6.9942</td><td>8.4600</td></tr><tr><td>Population (natural log of)</td><td>6,215</td><td>17.270</td><td>1.7238</td><td>16.938</td><td>15.978</td><td>18.502</td></tr><tr><td>Workforce participation</td><td>6,215</td><td>0.6202</td><td>0.1059</td><td>0.6189</td><td>0.5493</td><td>0.6839</td></tr><tr><td>Inflation</td><td>6,215</td><td>0.0857</td><td>0.1101</td><td>0.0613</td><td>0.0363</td><td>0.0931</td></tr></table>

Note: For each variable, statistics are calculated based on the observations in the regression with the maximum number of observations that include the variable.

<table><tr><td colspan="5">Table 3. Impact of Kiva on OSS and Interest Rate</td></tr><tr><td rowspan="2"></td><td colspan="2">Full sample</td><td colspan="2">Matched sample</td></tr><tr><td>OSS</td><td>Interest rate</td><td>OSS</td><td>Interest rate</td></tr><tr><td>After Kiva</td><td>0.0415*(0.0246)</td><td>-0.0129*(0.0077)</td><td>0.1006***(0.0301)</td><td>-0.0138*(0.0077)</td></tr><tr><td>Age (Young)</td><td>0.0999***(0.0210)</td><td>0.0089(0.0057)</td><td>0.1736**(0.0711)</td><td>0.0154(0.0138)</td></tr><tr><td>Age (Mature)</td><td>0.1272***(0.0256)</td><td>0.0067(0.0077)</td><td>0.2014***(0.0761)</td><td>0.0050(0.0189)</td></tr><tr><td>GDP per capita</td><td>0.0895**(0.0402)</td><td>0.0004(0.0135)</td><td>-0.0634(0.0940)</td><td>-0.0349(0.0256)</td></tr><tr><td>Population</td><td>0.3674*(0.1937)</td><td>0.0920*(0.0526)</td><td>0.2097(0.4095)</td><td>0.0699(0.1224)</td></tr><tr><td>Workforce participation</td><td>0.0195(0.0940)</td><td>0.0753**(0.0307)</td><td>0.0447(0.1670)</td><td>0.0560(0.0591)</td></tr><tr><td>Inflation</td><td>0.1780*(0.0994)</td><td>0.0454**(0.0225)</td><td>0.0571(0.1965)</td><td>-0.0591(0.0592)</td></tr><tr><td>Constant</td><td>-5.9684*(3.3486)</td><td>-1.3076(0.8968)</td><td>-2.0416(6.8174)</td><td>-0.5260(2.0304)</td></tr><tr><td>MFI size controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>MFI fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>6,071</td><td>5,592</td><td>971</td><td>948</td></tr><tr><td> $R^2$ </td><td>0.0496</td><td>0.0579</td><td>0.1194</td><td>0.1193</td></tr></table>

Note: \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01, robust standard errors in parentheses.

![](/api/attachments/UHFJCKYT/fulltext/images/fb12b349d23989accdbd931311187d9f44f6b36406aae038798404f7f7ead37d.jpg)  
Note: ${ } ^ { \star } p < 0 . 1 , { } ^ { \star \star } p < 0 . 0 5 , { } ^ { \star \star \star } p < 0 . 0 1 ;$ for each node, we report the sample size n = (Kiva, no Kiva) and PE (partnership effect) on OSS and interest rate.

Figure 2. Classification Tree for T = Kiva / No Kiva

## Heckman Selection Model

For the first-stage estimation in the Heckman selection model, we included MFI-level variables, such as age, size, percentage of loans to women, average loan balance per borrower, and return on assets (ROA), as well as macroeconomic indicators (e.g., GDP per capita, population, workforce participation, and inflation) to predict MFIs’ becoming a field partner. We also included the internet penetration rate and percentage of population in rural areas data from the World Development Indicators (WDI) and the International Telecommunication Union (ITU) as “exclusion restrictions” (Little 1985; Lennox et al. 2012; Goh et al. 2013).<sup>13</sup> One MFI joining Kiva is not likely to change these variables, but the internet penetration rate and percentage of population in rural areas can affect the need for collaboration between MFIs and crowdfunding platforms, thus affecting the probability of Kiva partnership.

Table 4 reports the second-stage estimation results for OSS (Column 1) and interest rates (Column 2), respectively.<sup>14</sup> As the table shows, the coefficients of the IMR in both Columns 1 and 2 are significant, suggesting a correction for selection bias. Controlling for the endogeneity of Kiva partnership and the potential selection bias, the coefficients of After Kiva in both models are positive and statistically significant (p < 0.05). The results are consistent with our main analysis.

## Using the Number of Kiva Projects as an Alternative Measure

The third robustness check examines whether MFIs’ activity level on Kiva affects the magnitude of change. We used the number of projects each MFI listed on Kiva per year as the independent variable. As shown in Table 5, the coefficient for number of projects on Kiva (natural log of) is positive and significant in the OSS model (Column 1) and negative and significant in the interest rate model (Column 2). The pattern is consistent with our main models and suggests that the more an MFI uses Kiva loans, the better the OSS and the lower the interest rate.

<table><tr><td colspan="3">Table 4. Estimation Results: Heckman Selection Model</td></tr><tr><td>Variables</td><td>OSS</td><td>Interest rate</td></tr><tr><td>After Kiva</td><td>0.0421**(0.0174)</td><td>-0.0132***(0.0047)</td></tr><tr><td>Age (young)</td><td>0.0814***(0.0160)</td><td>-0.0131***(0.0045)</td></tr><tr><td>Age (mature)</td><td>0.1086***(0.0194)</td><td>-0.0159***(0.0055)</td></tr><tr><td>GDP per capita</td><td>0.1018***(0.0273)</td><td>0.0133(0.0078)</td></tr><tr><td>Population</td><td>0.3547***(0.1057)</td><td>0.0704**(0.0291)</td></tr><tr><td>Workforce participation</td><td>0.0184(0.0810)</td><td>0.0710***(0.0227)</td></tr><tr><td>Inflation</td><td>0.2142***(0.0715)</td><td>0.0935***(0.0197)</td></tr><tr><td>IMR</td><td>-0.0934**(0.0367)</td><td>-0.1102***(0.0104)</td></tr><tr><td>Constant</td><td>-5.3540***(1.8150)</td><td>-0.9062*(0.4987)</td></tr><tr><td>MFI size controls</td><td>Yes</td><td>Yes</td></tr><tr><td>MFI fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td></tr></table>

Note: \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01, robust standard errors in parentheses.

<table><tr><td colspan="3">Table 5. Robustness Checks of the Impact: Alternative Independent Variable</td></tr><tr><td>Variables</td><td>OSS</td><td>Interest rate</td></tr><tr><td>Ln (number of projects on Kiva)</td><td>0.0063*(0.0037)</td><td>-0.0022*(0.0012)</td></tr><tr><td>Age (young)</td><td>0.0997***(0.0210)</td><td>0.0089(0.0057)</td></tr><tr><td>Age (mature)</td><td>0.1272***(0.0256)</td><td>0.0066(0.0077)</td></tr><tr><td>GDP per capita</td><td>0.0893**(0.0402)</td><td>0.0004(0.0135)</td></tr><tr><td>Population</td><td>0.3722*(0.1935)</td><td>0.0907*(0.0524)</td></tr><tr><td>Workforce participation</td><td>0.0195(0.0940)</td><td>0.0755**(0.0307)</td></tr><tr><td>Inflation</td><td>0.1780*(0.0994)</td><td>0.0453**(0.0225)</td></tr><tr><td>Constant</td><td>-6.0495*(3.3450)</td><td>-1.2858(0.8935)</td></tr><tr><td>MFI size controls</td><td>Yes</td><td>Yes</td></tr><tr><td>MFI fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>6,071</td><td>5,592</td></tr><tr><td> $R^2$ </td><td>0.0496</td><td>0.0582</td></tr></table>

Note: \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01, robust standard errors in parentheses.

## Falsification Test

Checking for reverse causality rules out the concern that Kiva MFIs might already have been improving their sustainability or decreasing their interest rate and that joining Kiva is actually a result of such efforts. We conducted a falsification test by including lead periods (−1, −2, and −3 years before) and lagged periods (0, +1, +2, +3 and +4 years forward after) of Kiva partnership as independent variables (Autor 2003; Hwang and Kim 2016; Burtch et al. 2018). If an increasing or decreasing trend in sustainability and interest rates existed before the joining event, the positive or negative effects should be observed in the lead periods. We used the same DID design to estimate the model.

The results of the falsification test are reported in Table 6. The coefficients of before-period indicators are not significant in either Column 1 or Column 2, suggesting that there is no evidence of reverse causality. The results also provide evidence to support the critical parallel trends assumption of the DID method, which is that the trends in OSS and interest rates for Kiva and non-Kiva MFIs should have no difference before the Kiva partnership (Khurana et al. 2019; Cheng et al. 2020).<sup>15</sup>

By examining the effects of the after-Kiva periods, we demonstrate that the effects of Kiva are dynamic. For OSS, the coefficients of Kiva<sub>t0</sub> and Kiva<sub>t+1</sub> suggest a 7.59% and a 7.07% increase in OSS, respectively, while those of subsequent periods are not significant. In contrast, for interest rates, the coefficient estimates are negative, but they are not statistically significant until the third year after the MFI joins Kiva. At that point, the coefficients of Kiva<sub>t+3</sub> and Kiva<sub>t+4</sub> <sub>forward</sub> suggest significant 3.70% and 3.16% decreases, respectively. The findings suggest that Kiva partnership leads to an immediate improvement in OSS, and a significant decrease in interest rates occurs after three years. This temporal pattern of changes implies that a Kiva partnership first helps MFIs reduce survival pressure (e.g., increasing OSS). When MFIs become more sustainable, they choose to share the benefit with their borrowers by decreasing interest rates. This finding is consistent with our discovery from the tree-based analysis.

In sum, the robustness checks confirm the findings that Kiva leads to better sustainability and lower interest rates. Moreover, the results reveal interesting dynamic patterns in the effects of Kiva partnerships: MFIs tend to improve their sustainability at the beginning and then focus on their social mission by decreasing interest rates.

## Additional Analysis

## Changes in Capital Costs and Efficiencies

To understand how a partnership with Kiva leads to positive changes in sustainability and interest rates, we examined changes in capital costs and in the efficiency of MFIs after joining Kiva. Table 7 reports the definitions of variables considered in this analysis. Capital cost is measured by financial expense, which is equal to the total financial expense divided by the average gross loan portfolio.<sup>16</sup> Total financial expense includes all interest, fees, and commissions incurred on all liabilities, including commercial and concessional borrowings, mortgages, and other financial liabilities. There is significant heterogeneity in the sources of funds for lending. MFIs that rely more on commercial channels typically have higher financial expenses.

The efficiency of MFIs has two aspects: operational efficiency and risk management effectiveness (Cull et al. 2009; Garmaise and Natividad 2013). Operational efficiency refers to MFIs’ ability to operate without incurring significant operational expenses. We included two measures: operational cost and loans per loan officer. Operational cost is measured by operating costs per dollar loaned, which is calculated by dividing operating costs by the average gross loan portfolio. Operating costs include expenses related to operations, including personnel expenses, administrative expenses, and depreciation (Cull et al. 2009; Ahlin et al. 2011; Garmaise and Natividad 2013). Loans per loan officer is the ratio of total number of loans outstanding to the number of loan officers. More loans per loan officer indicate that MFIs make better use of the human resources of their loan officers (Garmaise and Natividad 2010).

Regarding risk management effectiveness, we considered two measures: impairment expense and portfolio at risk 30. Impairment expense is the amount provisioned for bad loans as a fraction of the average loan portfolio over the year. Portfolio at risk 30 is the fraction of the loan portfolio at risk (loans behind schedule on payments) for more than thirty days. It is an early signal of default problems (Ahlin et al. 2011).

Table 8 presents the summary statistics. The mean of financial expense is 7.03%, and operational cost is 22.79%. The mean of impairment expense is 1.97%, and portfolio at risk 30 is 4.61%.

<table><tr><td colspan="3">Table 6. Falsification Test Using Decomposed Indicators</td></tr><tr><td>Variables</td><td>OSS</td><td>Interest rate</td></tr><tr><td>Kivat-3</td><td>-0.0020(0.0250)</td><td>-0.0159(0.0144)</td></tr><tr><td>Kivat-2</td><td>0.0145(0.0303)</td><td>-0.0083(0.0126)</td></tr><tr><td>Kivat-1</td><td>0.0009(0.0333)</td><td>-0.0137(0.0138)</td></tr><tr><td>Kivat0</td><td>0.0759**(0.0351)</td><td>-0.0161(0.0145)</td></tr><tr><td>Kivat+1</td><td>0.0707*(0.0418)</td><td>-0.0179(0.0144)</td></tr><tr><td>Kivat+2</td><td>0.0460(0.0393)</td><td>-0.0216(0.0153)</td></tr><tr><td>Kivat+3</td><td>-0.0030(0.0409)</td><td>-0.0370**(0.0158)</td></tr><tr><td>Kivat+4 forward</td><td>-0.0154(0.0469)</td><td>-0.0316*(0.0185)</td></tr><tr><td>Age (young)</td><td>0.0988***(0.0211)</td><td>0.0089(0.0057)</td></tr><tr><td>Age (mature)</td><td>0.1269***(0.0257)</td><td>0.0068(0.0077)</td></tr><tr><td>GDP per capita</td><td>0.0882**(0.0400)</td><td>0.0004(0.0135)</td></tr><tr><td>Population</td><td>0.4008**(0.1968)</td><td>0.0998*(0.0533)</td></tr><tr><td>Workforce participation</td><td>0.0417(0.0943)</td><td>0.0790**(0.0308)</td></tr><tr><td>Inflation</td><td>0.1742*(0.0994)</td><td>0.0452**(0.0224)</td></tr><tr><td>Constant</td><td>-6.5446*(3.4003)</td><td>-1.4427(0.9079)</td></tr><tr><td>MFI size controls</td><td>Yes</td><td>Yes</td></tr><tr><td>MFI fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>6,071</td><td>5,592</td></tr><tr><td> $R^2$ </td><td>0.0523</td><td>0.0604</td></tr></table>

Note: \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01, robust standard errors in parentheses.

<table><tr><td colspan="2">Table 7. Variable Descriptions</td></tr><tr><td>Variable</td><td>Definition</td></tr><tr><td colspan="2">Cost of capital</td></tr><tr><td>Financial expense</td><td>Total financial expense / average gross loan portfolio</td></tr><tr><td colspan="2">Efficiency</td></tr><tr><td colspan="2">Operational efficiency</td></tr><tr><td>Operational cost</td><td>Operating cost / average gross loan portfolio</td></tr><tr><td>Loans per loan officer</td><td>Number of loans outstanding / number of loan officers</td></tr><tr><td colspan="2">Risk management effectiveness</td></tr><tr><td>Impairment expense</td><td>Provision for loan impairment / average gross loan portfolio</td></tr><tr><td>Portfolio at risk 30</td><td>Loans overdue by more than 30 days / average gross loan portfolio</td></tr></table>

<table><tr><td colspan="7">Table 8. Summary Statistics of Variables</td></tr><tr><td>Variable</td><td>Obs.</td><td>Mean</td><td>Std. dev.</td><td>Median</td><td>25th percentile</td><td>75th percentile</td></tr><tr><td colspan="7">Cost of capital</td></tr><tr><td>Financial expense</td><td>6,190</td><td>0.0703</td><td>0.0542</td><td>0.0647</td><td>0.0372</td><td>0.0961</td></tr><tr><td colspan="7">Efficiency</td></tr><tr><td colspan="7">Operational efficiency</td></tr><tr><td>Operational cost</td><td>5,596</td><td>0.2279</td><td>0.1346</td><td>0.1869</td><td>0.1272</td><td>0.2923</td></tr><tr><td>Loans per loan officer</td><td>5,518</td><td>288.03</td><td>145.02</td><td>261</td><td>177</td><td>366</td></tr><tr><td colspan="7">Risk management effectiveness</td></tr><tr><td>Impairment expense</td><td>5,569</td><td>0.0197</td><td>0.0195</td><td>0.0140</td><td>0.0048</td><td>0.0288</td></tr><tr><td>Portfolio at risk 30</td><td>5,463</td><td>0.0461</td><td>0.0434</td><td>0.0340</td><td>0.0133</td><td>0.0637</td></tr></table>

Like in the main analysis, we implemented both the DID analysis and the tree-based approach to identify the effects of a Kiva partnership. Table 9 reports the estimation results from the DID models. First, financial expenses do not decrease but slightly increase after joining Kiva, suggesting that MFIs might leverage the interest-free money from Kiva to expand by borrowing more from other sources. To confirm this conjecture, we further examined loan portfolio (natural log of) changes after joining Kiva. The results in Table 10 provide evidence that the size of MFIs’ loan portfolios increases after joining Kiva. Second, operational costs decrease, suggesting that MFIs become more efficient in managing expenses. Third, impairment expenses also decrease, which indicates signs of improvement in risk management effectiveness. Based on our back-of-the-envelope calculations, after becoming a field partner with Kiva, an MFI’s operational costs decrease by 8.34% (= 0.0189/0.2267), and its impairment expenses decrease by 17.77% (= 0.0035/0.0197), suggesting an economically significant impact of Kiva partnerships.

Results from the tree-based approach are shown in Figure 3, and they are consistent with the findings from the DID analysis. In particular, Nodes 14 and 23 show a positive and significant effect of Kiva partnership on financial expenses. Nodes 6, 7, 13, and 14 indicate a negative and significant partnership effect on operational costs. Nodes 13 and 23 suggest a positive and significant effect on loans per loan officer. Five nodes (except Nodes 6 and 23) exhibit a negative effect on impairment expenses, and three of these results are significant (Nodes 7, 13, and 20). Finally, all nodes show a negative effect on portfolio at risk 30, and four of them are statistically significant (Nodes 14, 20, 21, and 23).

## Discussion

Regarding the improvement in risk management effectiveness, the concern might be raised that MFIs become more selective with projects to reduce risk after joining Kiva. If they favor borrowers that already have good credit, MFIs might be shying away from their social responsibilities of helping those most in need. Thus, we further examined temporal changes in the characteristics of Kiva MFIs’ loan portfolios on Kiva. Table 11 summarizes the definitions of these variables, including average loan amount, average repayment term, number of loan categories, percentage of loans to women, and percentage of group loans. According to the literature, larger loan sizes, longer repayment terms (Morduch 1999; Field et al. 2013), and female borrowers are considered riskier (Banerjee and Duflo 2011), while group loans are considered less risky (e.g., Morduch 1999). Number of loan categories measures the diversity of MFI portfolios. Table 12 reports the summary statistics.

We regressed the loan characteristics on a time variable, which is the number of years since an MFI has joined Kiva. In Table 13, the results show that the average loan size and repayment term increase over time. The number of loan categories increases. The percentage of loans to women and the percentage of group loans show no significant change. It seems that MFIs’ loan portfolios on Kiva grow riskier over time, in terms of size and repayment terms, and they become more diversified. We can conclude that MFIs do not intentionally select less risky projects for the purpose of maintaining good risk management status after joining Kiva.

We further examined the relationship between the average number of lenders per project for each MFI and operational efficiency. If our hypothesized crowd monitoring is effective, we would expect that the improvement in operational efficiency increases with the number of lenders because more lenders mean more intensive monitoring pressure. Table 14 reports the estimation results, which show that a higher number of lenders per project leads to improved efficiency (i.e., a decrease in operational costs and a decrease in impairment expense).

<table><tr><td colspan="6">Table 9. Underlying Changes of MFIs After Joining Kiva</td></tr><tr><td rowspan="3">Variables</td><td rowspan="2">Cost of capital</td><td colspan="4">Efficiency</td></tr><tr><td colspan="2">Operational efficiency</td><td colspan="2">Risk management effectiveness</td></tr><tr><td>Financial expense</td><td>Operational cost</td><td>Loans per loan officer</td><td>Impairment expense</td><td>Portfolio at risk 30</td></tr><tr><td rowspan="2">After Kiva</td><td>0.0070*</td><td>-0.0189**</td><td>7.1487</td><td>-0.0035**</td><td>-0.0015</td></tr><tr><td>(0.0036)</td><td>(0.0082)</td><td>(10.048)</td><td>(0.0018)</td><td>(0.0036)</td></tr><tr><td rowspan="2">Age (young)</td><td>0.0063</td><td>-0.0401***</td><td>12.377</td><td>-0.0014</td><td>-0.0008</td></tr><tr><td>(0.0041)</td><td>(0.0075)</td><td>(8.7305)</td><td>(0.0014)</td><td>(0.0032)</td></tr><tr><td rowspan="2">Age (mature)</td><td>0.0088*</td><td>-0.0504***</td><td>17.821</td><td>-0.0030</td><td>0.0012</td></tr><tr><td>(0.0048)</td><td>(0.0095)</td><td>(12.159)</td><td>(0.0018)</td><td>(0.0041)</td></tr><tr><td rowspan="2">GDP per capita</td><td>0.0207***</td><td>-0.0367**</td><td>35.671*</td><td>-0.0048</td><td>-0.0230***</td></tr><tr><td>(0.0064)</td><td>(0.0148)</td><td>(18.609)</td><td>(0.0031)</td><td>(0.0053)</td></tr><tr><td rowspan="2">Population</td><td>0.0055</td><td>-0.0384</td><td>161.11**</td><td>-0.0184</td><td>-0.0743***</td></tr><tr><td>(0.0235)</td><td>(0.0637)</td><td>(63.296)</td><td>(0.0127)</td><td>(0.0251)</td></tr><tr><td rowspan="2">Workforce participation</td><td>-0.0143</td><td>0.0904***</td><td>-69.805</td><td>-0.0002</td><td>-0.0160</td></tr><tr><td>(0.0138)</td><td>(0.0290)</td><td>(48.411)</td><td>(0.0085)</td><td>(0.0190)</td></tr><tr><td rowspan="2">Inflation</td><td>0.0187</td><td>-0.0280</td><td>88.292**</td><td>-0.0118</td><td>-0.0366**</td></tr><tr><td>(0.0138)</td><td>(0.0312)</td><td>(40.840)</td><td>(0.0079)</td><td>(0.0160)</td></tr><tr><td rowspan="2">Constant</td><td>-0.1895</td><td>1.1887</td><td>-2,790.0**</td><td>0.3787*</td><td>1.5107***</td></tr><tr><td>(0.4046)</td><td>(1.0983)</td><td>(1100.4)</td><td>(0.2186)</td><td>(0.4306)</td></tr><tr><td>MFI size controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>MFI fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>6,190</td><td>5,596</td><td>5,518</td><td>5,569</td><td>5,463</td></tr><tr><td>R2</td><td>0.0293</td><td>0.0757</td><td>0.0385</td><td>0.0282</td><td>0.0418</td></tr></table>

Note: \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01, robust standard errors in parentheses.

<table><tr><td colspan="2">Table 10. Impact of Kiva on MFI Loan Portfolio</td></tr><tr><td>Variables</td><td>Loan portfolio</td></tr><tr><td>After Kiva</td><td>0.2246***(0.0701)</td></tr><tr><td>Age (young)</td><td>0.3500***(0.0650)</td></tr><tr><td>Age (mature)</td><td>0.4519***(0.0854)</td></tr><tr><td>GDP per capita</td><td>1.1974***(0.1075)</td></tr><tr><td>Population</td><td>1.7459***(0.5683)</td></tr><tr><td>Workforce participation</td><td>-0.7997***(0.2487)</td></tr><tr><td>Inflation</td><td>0.2885(0.2115)</td></tr><tr><td>Constant</td><td>-24.103**(9.8974)</td></tr><tr><td>MFI size controls</td><td>Yes</td></tr><tr><td>MFI fixed effects</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td></tr><tr><td>Observations</td><td>6,215</td></tr><tr><td> $R^2$ </td><td>0.6229</td></tr></table>

Note: \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01, robust standard errors in parentheses.

![](/api/attachments/UHFJCKYT/fulltext/images/8be6f71a78e0ca4c38c76d2983ac06d356aba8e87aab9541619886e0f4f0f440.jpg)  
Note: ${ } ^ { \star } p < 0 . 1 , { } ^ { \star \star } p < 0 . 0 5 , { } ^ { \star \star \star } p < 0 . 0 1 ;$ for each node, we specify the sample size n = (Kiva, no Kiva) and partnership effect (PE)

## Figure 3. Classification Tree for T = Kiva / No Kiva: Underlying Changes

<table><tr><td colspan="2">Table 11. Loan Characteristic Variables and Definitions</td></tr><tr><td>Variable</td><td>Definition</td></tr><tr><td>Average loan amount</td><td>Total loan amount / total number of loans</td></tr><tr><td>Average repayment term</td><td>The average number of months of the repayment term</td></tr><tr><td>Number of loan categories</td><td>Number of loan categories covered by the MFI. There are 16 available categories on Kiva, indicating the diversity of projects.</td></tr><tr><td>Percentage of loans to women</td><td>Number of loans to female borrowers / total number of loans</td></tr><tr><td>Percentage of group loans</td><td>Number of group borrowers&#x27; projects / total number of loans</td></tr></table>

<table><tr><td colspan="7">Table 12. Summary Statistics of Loan Characteristic Variables</td></tr><tr><td>Variable</td><td>Obs.</td><td>Mean</td><td>Std. dev.</td><td>Media</td><td>25th percentile</td><td>75th percentile</td></tr><tr><td>Average loan amount</td><td>329</td><td>1094.4</td><td>780.85</td><td>801.97</td><td>609.75</td><td>1301.9</td></tr><tr><td>Average repayment term</td><td>329</td><td>13.829</td><td>5.4926</td><td>13.438</td><td>10.015</td><td>15.971</td></tr><tr><td>Number of loan categories</td><td>329</td><td>11.347</td><td>3.0386</td><td>12</td><td>9</td><td>14</td></tr><tr><td>Percentage of loans to women</td><td>329</td><td>0.7175</td><td>0.2264</td><td>0.7488</td><td>0.5613</td><td>0.9164</td></tr><tr><td>Percentage of group loans</td><td>329</td><td>0.0948</td><td>0.1797</td><td>0</td><td>0</td><td>0.1045</td></tr></table>

<table><tr><td colspan="6">Table 13. Time Effect on Loan Characteristics on Kiva</td></tr><tr><td>Variables</td><td>Average loan amount</td><td>Average repayment term</td><td>Number of loan categories</td><td>Percentage of loans to women</td><td>Percentage of group loans</td></tr><tr><td>Time</td><td>103.94***(32.184)</td><td>0.1842*(0.1016)</td><td>0.6677***(0.0998)</td><td>-0.0065(0.0045)</td><td>-0.0001(0.0063)</td></tr><tr><td>Age (young)</td><td>-222.55(266.20)</td><td>-0.7552(0.8279)</td><td>-1.7779**(0.8245)</td><td>0.0212(0.0448)</td><td>-0.0876(0.1481)</td></tr><tr><td>Age (mature)</td><td>-211.43(375.87)</td><td>-1.3830(1.1219)</td><td>-1.6854(1.1174)</td><td>0.0640(0.0532)</td><td>-0.0794(0.1440)</td></tr><tr><td>Constant</td><td>999.71***(335.15)</td><td>14.211***(0.8894)</td><td>10.999***(0.9036)</td><td>0.6765***(0.0476)</td><td>0.1760(0.1458)</td></tr><tr><td>MFI size controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>MFI fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>329</td><td>329</td><td>329</td><td>329</td><td>329</td></tr><tr><td> $R^2$ </td><td>0.1501</td><td>0.1072</td><td>0.2510</td><td>0.0218</td><td>0.0143</td></tr></table>

Note: \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01, robust standard errors in parentheses.

<table><tr><td colspan="5">Table 14. Impact of Number of Lenders on MFIs&#x27; Efficiency</td></tr><tr><td>Variables</td><td>Operational cost</td><td>Loans per loan officer</td><td>Impairment expense</td><td>Portfolio at risk 30</td></tr><tr><td>Ln (number of lenders)</td><td>-0.0050*(0.0027)</td><td>2.6180(2.9566)</td><td>-0.0012**(0.0005)</td><td>-0.0007(0.0011)</td></tr><tr><td>Age (young)</td><td>-0.0401***(0.0075)</td><td>12.456(8.7245)</td><td>-0.0014(0.0014)</td><td>-0.0008(0.0032)</td></tr><tr><td>Age (mature)</td><td>-0.0503***(0.0095)</td><td>17.885(12.154)</td><td>-0.0030(0.0018)</td><td>0.0012(0.0041)</td></tr><tr><td>GDP per capita</td><td>-0.0366**(0.0148)</td><td>35.558*(18.613)</td><td>-0.0048(0.0031)</td><td>-0.0229***(0.0053)</td></tr><tr><td>Population</td><td>-0.0398(0.0634)</td><td>161.05**(63.235)</td><td>-0.0185(0.0126)</td><td>-0.0741***(0.0250)</td></tr><tr><td>Workforce participation</td><td>0.0906***(0.0291)</td><td>-70.169(48.361)</td><td>-0.0001(0.0085)</td><td>-0.0159(0.0190)</td></tr><tr><td>Inflation</td><td>-0.0278(0.0312)</td><td>88.461**(40.848)</td><td>-0.0118(0.0079)</td><td>-0.0368**(0.0160)</td></tr><tr><td>Constant</td><td>1.2115(1.0932)</td><td>-2,780.0**(1099.4)</td><td>0.3802*(0.2174)</td><td>1.5063***(0.4294)</td></tr><tr><td>MFI size controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>MFI fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>5,596</td><td>5,518</td><td>5,569</td><td>5,463</td></tr><tr><td> $R^2$ </td><td>0.0751</td><td>0.0386</td><td>0.0285</td><td>0.0419</td></tr></table>

Note: \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01, robust standard errors in parentheses.

We also checked the robustness of the results by using the number of projects on Kiva and total loan amount on Kiva as alternative proxies of crowd monitoring intensity. The results also suggest that more intensive crowd monitoring (a larger number of projects and a higher total loan amount on Kiva) results in better efficiency (additional results are available from the authors on request). Therefore, when the intensity of crowd monitoring increases (i.e., more people pay attention), MFIs tend to perform more efficiently. These findings provide supporting evidence for our argument about crowd monitoring.

We summarize our findings of how MFIs change after they join Kiva here. First, MFIs do not directly apply the funds from low-cost crowdfunding to lower their financial expenses. Instead, they leverage the resources to expand their services. Second, stronger sustainability and lower interest rates result primarily from improved efficiency and risk management effectiveness. These findings suggest that crowd monitoring, which motivates MFIs to improve their efficiency and risk management, can mitigate the potential negative effects of financial slack resulting from low-cost capital. As a result, we observe that a Kiva partnership helps MFIs to improve their sustainability and use extra resources to pursue their social goals by lowering interest rates.

## Conclusion and Implications

The study investigates the impact of crowdfunding on MFIs and explores the underlying mechanisms that drive the changes. We empirically identify the causal impact of Kiva on MFIs’ sustainability and interest rates. We validate the findings with a series of empirical models and robustness checks. Our results show that after MFIs use the Kiva platform for funding, their sustainability improves, and their interest rate decreases. Further evidence suggests that crowdfunding helps MFIs initially to achieve better sustainability, and once they do, they may use the extra resources to lower interest rates, fulfilling their social mission.

We also explore whether the changes result from a decrease in capital costs (financial expense) and/or an improvement in efficiency (operational efficiency and risk management effectiveness). Interestingly, we find that financial expenses do not decrease but slightly increase. MFIs might leverage their low-cost Kiva funds to expand their loan portfolio. Meanwhile, operations become more efficient, as operational costs decrease. Risk management also becomes more effective, as evidenced by declines in impairment expense. Gathering the evidence together, we understand that the improvement in sustainability and interest rates might result not directly from the appropriation of lower capital costs, but from the improved operational efficiency and risk management effectiveness.

The implications of using crowdfunding platforms are richer than can be assumed by seeing them simply as an alternative funding source to reduce financial expenses. The empirical results testify to our theoretical arguments that the information disclosure for and monitoring from the crowd and the platform can motivate MFIs to achieve better performance in service to their mission. The efficiency improvement is what enables MFIs to offer lower interest rates while still achieving improved sustainability. Our study has significant theoretical and practical implications.

## Theoretical Implications

Our theoretical contributions are threefold. First, this study contributes to the literature on crowdfunding by deepening the understanding of the impact of crowdfunding. With organization-level data, we examine the actual operational and managerial changes in participating organizations, extending the research on the societal outcomes of crowdfunding (Blaseg and Koetter 2015; Burtch and Chan 2019; Kim and Hann 2019). We demonstrate that crowdfunding can act as more than an emerging funding source. MFIs can better sustain themselves and offer lower interest rates because of the improvement in operational efficiency and risk management effectiveness—not as a direct consequence of the low-cost money from crowdfunding. We propose that crowd monitoring, which is enabled by effective information disclosure, plays an important role. This study sheds light on more general crowdfunding settings, particularly because a variety of organizations have started to use crowdfunding as an alternative financing channel. For instance, Indiegogo has launched a service called Enterprise Crowdfunding, which traditional enterprises can use to crowdfund new products or projects.

Second, we contribute to the broader literature on the impact of information technologies (e.g., Brynjolfsson and Hitt 2000; Brynjolfsson and Simester 2011), particularly the impact of online platforms (e.g., Xu and Zhang 2013; Zhang and Zhang 2015; Hao and Tan 2017; Kwark et al. 2017). As the economy shifts to incorporate more digital and online features, IT is increasingly impacting all aspects of economic and social life. In particular, online platforms connect and empower individuals and organizations to foster change. For instance, research has shown the influence of social media on how companies disclose information (Xu and Zhang 2013), how user-generated content influences firms’ product design decisions (Kwark et al. 2017), how online advertising platforms (Craigslist) have affected local newspapers (Seamans and Zhu 2013), and how companies adjust supplychain information strategies on e-commerce platforms (Hao and Tan 2017). We add to this IT literature by demonstrating how crowdfunding platforms change offline organizations informational and institutional environments, resulting in improvements in operations and performance. Our study sheds light on how empowered individual lenders can foster change by using a crowdfunding platform in the context of microfinance. Our findings also add to IT4D research by showing the effect of online crowdfunding on MFIs— organizations that work for poverty alleviation.

Third, we contribute to the literature on microfinance by discussing a new financing alternative and its effects on MFIs. Current research and practices highlight the challenges of MFIs—including sustainability, high interest rates, and low operational efficiency (Morduch 1999; Drake and Rhyne 2002;

Cull et al. 2007, 2009; Balkenhol and Hudon 2011; Dehejia et al. 2012). However, the literature offers limited help in facing and surmounting these challenges (Conning 1999; Morduch 1999; Garmaise and Natividad 2010). Our study highlights that online crowdfunding might be a plausible solution for MFIs because crowdfunding not only provides a reliable, low-cost funding source, but also intensifies information disclosure and crowd monitoring. Our results show that MFIs can improve their operational efficiency and alleviate the problems of high interest rates by collaborating with an online, prosocial lending, crowdfunding platform.

## Managerial Implications

Our study generates important insights for microfinance practices and for online crowdfunding platforms. First, online crowdfunding appears to be a promising solution to some key challenges of the microfinance industry. The economic magnitude of Kiva’s impact is not negligible. Our back-of-the-envelope calculation suggests a 3.7% increase in OSS and a 4% decrease in interest rates. While the industry has often struggled with the balance between sustainability and lower interest rates (Morduch 1999; Cull et al. 2009; Rosenberg et al. 2009; Dehejia et al. 2012), Kiva partnership helps MFIs achieve both goals at the same time by making MFIs more efficient. There is hope and opportunity in this new way of financing MFIs.

Second, our analysis suggests that the effect of partnership with online crowdfunding is not only a short-term remedy that provides access to low-cost funds but is also a trigger to induce long-term structural changes that help MFIs improve efficiency. The due diligence that MFIs must perform in the partnership (e.g., information disclosure, project descriptions and updates, interaction with an online community of lenders) can lead to much-needed organizational changes. Further, MFIs can connect and even compete with other MFIs globally to increase awareness and learn about best practices. Indeed, our calculation of the magnitude of the effects suggests remarkable improvement: The decrease in impairment expense and in operational costs triggered by a Kiva partnership represents about 17.77% of the average impairment expense and 8.34% of the average operational cost.

Third, our study provides insights into how crowdfunding platforms can foster change and have a long-term effect through crowd monitoring, information disclosure, and regular evaluation. Platforms should focus on policies aiming to improve transparency, design effective mechanisms to encourage disclosure, induce active participation from lenders, and build constructive relationships between lenders and field partners.

Fourth, governments still are debating whether crowdfunding should be encouraged, given the issues and doubts accompanying its quick development. Our study provides compelling evidence that prosocial crowdfunding generates social benefits beyond providing funds. It helps to enable changes that improve the self-sufficiency of MFIs. We believe that by opening the funding process and properly enforcing best practices in crowdfunding, the positive effects on participants can generalize to other crowdfunding contexts.

## Limitations and Future Research

This study has a few limitations. First, our investigation is constrained by data availability, which is a common challenge faced by studies on microfinance. Although we have made great efforts to deliver a thorough investigation using the available data, we do not have access to more detailed data on MFIs’ operations and loan portfolios (e.g., funding sources) to further strengthen the analysis. Meanwhile, many MFIs are from developing countries, meaning that macroeconomic indexes, such as liquidity indicators, are not easily accessible. Future research that gains access to more detailed data on MFIs’ practices could reveal additional nuances regarding how MFIs handle partnerships with online crowdfunding platforms. For example, without observations about MFIs’ accounting practices, we cannot assess how accounting methods might influence our measurement (e.g., gross yield) and analysis. Moreover, because MIX Market reporting is not mandatory, there might be sample selection bias, and data quality varies across MFIs. Although our robustness checks strengthen the causal inference about the effects of a Kiva partnership, we should be careful in drawing general conclusions.

Second, our empirical evidence about the underlying mechanisms of the crowdfunding effects is from the analysis of secondary data. Thus, our inferences can only be based on proxy indicators; future studies could use case studies or firsthand data to understand the mechanisms more deeply.

Third, although all our analysis suggests a consistent and economically significant effect of Kiva partnerships, some of our estimates are marginally significant statistically. On the one hand, our analysis is constrained by a relatively small sample size because online prosocial-lending crowdfunding is still in development and only a small portion of MFIs have adopted it. On the other hand, our tree-based analysis suggests the potential for heterogeneous treatment effects among MFIs. As online crowdfunding continues to develop, and richer data become available, future research could examine the heterogeneous effects of online crowdfunding on offline institutions at a more granular level and address other intriguing issues, such as competition and multihoming.

## Acknowledgments

The authors thank the senior editor, Dr. Siva Viswanathan, the associate editor and three anonymous reviewers for their constructive comments. The authors thank the advisors and participants in the Information Systems Summer Research Workshop at City University of Hong Kong. The authors are also grateful to seminar participants at the 10th China Summer Workshop on Information Management, the 15th Workshop on e-Business, and City University of Hong Kong. We thank Dr. Yulin Fang, Dr. Alvin Leung, Dr. Xin Li, Dr. Ben Liu, Dr. Kai Lim, Dr. Wei Thoo Yue, and Dr. Leon Zhao, for their helpful feedback. This research was supported in part by the National Natural Science Foundation of China [Grant 72101155, 72131001, 92146003, 71942003] and the Research Grants Council of the Hong Kong Special Administrative Region, China [Grant 7004776]. All remaining errors are our own.

## References

Acharya, V. V., and Subramanian, K. V. 2009. “Bankruptcy Codes and Innovation,” Review of Financial Studies (22:12), pp. 4949- 4988.

Agrawal, A., Catalini, C., and Goldfarb, A. 2015. “Crowdfunding: Geography, Social Networks, and the Timing of Investment Decisions,” Journal of Economics & Management Strategy (24:2), pp. 253-274.

Agarwal, S., and Qian, W. 2014. “Consumption and Debt Response to Unanticipated Income Shocks: Evidence from a Natural Experiment in Singapore,” American Economic Review (104:12), pp. 4205-4230.

Ahlers, G. K., Cumming, D., Günther, C., and Schweizer, D. (2015). “Signaling in Equity Crowdfunding,” Entrepreneurship Theory and Practice (39:4), pp. 955-980.

Ahlin, C., Lin, J., and Maio, M. 2011. “Where Does Microfinance Flourish? Microfinance Institution Performance in Macroeconomic Context,” Journal of Development Economics (95:2), pp. 105-120.

Andrade, A. D. and Doolin, B. 2016. “Information and Communication Technology and the Social Inclusion of Refugees,” MIS Quarterly (40:4), pp. 405-416.

Angrist, J. D., and Pischke, J. S. 2009. Mostly Harmless Econometrics: An Empiricist’s Companion, Princeton University Press.

Aral, S., Brynjolfsson, E., and Van Alstyne, M. 2012. “Information, Technology, and Information Worker Productivity,” Information Systems Research (23:3, Part 2 of 2), pp. 849-867.

Autor, D. H. 2003. “Outsourcing at Will: The Contribution of Unjust Dismissal Doctrine to the Growth of Employment Outsourcing,” Journal of Labor Economics (21:1), pp. 1-42.

Baker, T., Pricer, R., and Nenide, B. 2000. “When Less Is More: Undercapitalization as a Predictor of Firm Success,” Frontiers of Entrepreneurship Research (15:4), pp. 346-363.

Balkenhol, B., and Hudon, M. 2011. “Efficiency,” in B. Armendariz and M. Labie (Eds.), The Handbook of Microfinance, World Scientific, pp. 383-396.

Banerjee, A. V., and Duflo, E. 2011. Poor Economics: A Radical Rethinking of the Way to Fight Global Poverty, Public Affairs.

Berger, P. G., and Hann, R. 2003. “The Impact of SFAS No. 131 on Information and Monitoring,” Journal of Accounting Research (41:2), pp. 163-223.

Bergström, F. 2000. “Capital Subsidies and the Performance of Firms,” Small Business Economics (14:3), pp. 183-193.

Bertrand, M., Duflo, E., and Mullainathan, S. 2004. “How Much Should We Trust Differences-in-Differences Estimates?,” The Quarterly Journal of Economics (119:1), pp. 249-275.

Best, J., Neiss, S., and Swart, R. 2013. Crowdfunding’s Potential for the Developing World, infoDev.

Bhargava, H. K., and Choudhary, V. 2004. “Economics of an Information Intermediary with Aggregation Benefits,” Information Systems Research (15:1), pp. 22-36.

Blaseg and Koetter. 2015. “Friend or Foe? Crowdfunding Versus Credit when Banks are Stressed,” IWH Discussion Papers 8/2015, Halle Institute for Economic Research.

Bogan, V. L. 2012. “Capital Structure and Sustainability: An Empirical Study of Microfinance Institutions,” Review of Economics and Statistics (94:4), pp. 1045-1058.

Brynjolfsson, E., and Hitt, L. M. 2000. “Beyond Computation: Information Technology, Organizational Transformation and Business Performance,” Journal of Economic Perspectives (14:4), pp. 23-48.

Brynjolfsson, E., Hu, Y., and Simester, D. 2011. “Goodbye Pareto Principle, Hello Long Tail: The Effect of Search Costs on the Concentration of Product Sales,” Management Science (57:8), pp. 1373-1386.

Brynjolfsson, E., Hui, X., and Liu, M. 2019. “Does Machine Translation Affect International Trade? Evidence from a Large Digital Platform,” Management Science (65:12), pp. 5449-5460.

Burtch, G. and Chan, J. 2019. “Investigating the Relationship Between Medical Crowdfunding and Personal Bankruptcy in the United States: Evidence of a Digital Divide,” MIS Quarterly (43:1), pp. 237-262.

Burtch, G., Ghose, A., and Wattal, S. 2013. “An Empirical Examination of the Antecedents and Consequences of Contribution Patterns in Crowd-Funded Markets,” Information Systems Research (24:3), pp. 499-519.

Burtch, G., Ghose, A., and Wattal, S. 2014. “Cultural Differences and Geography as Determinants of Online Pro-Social Lending,” MIS Quarterly (38:3), pp. 773-794.

Burtch, G., Ghose, A., and Wattal, S. 2015. “The Hidden Cost of Accommodating Crowdfunder Privacy Preferences: A Randomized Field Experiment,” Management Science (61:5), pp. 949-962.

Burtch, G., Ghose, A., and Wattal, S. 2016. “Secret Admirers: An Empirical Examination of Information Hiding and Contribution Dynamics in Online Crowdfunding,” Information Systems Research (27:3), pp. 478-496.

Burtch, G., Carnahan, S., and Greenwood, B. N. 2018. “Can You Gig It? An Empirical Examination of the Gig Economy and Entrepreneurial Activity,” Management Science (64:12), pp. 5497-5520.

Bushman, R. M., and A. J. Smith. 2001. “Financial Accounting Information and Corporate Governance,” Journal of Accounting & Economics (32:1), pp. 237-333.

Byoun, S., and Moore, W. T. 2003. “Stock vs. Stock-Warrant Units: Evidence from Seasoned Offerings,” Journal of Corporate Finance (9:5), pp. 575-590.

Callen, J. L., Klein, A., and Tinkelman, D. 2003. “Board Composition, Committees, and Organizational Efficiency: The Case of Nonprofits,” Nonprofit and Voluntary Sector Quarterly (32:4), pp. 493-520.

Campbell, D. T., and Stanley, J. C. 1963. Experimental and Quasi-Experimental Designs for Research, Rand McNally.

Candelise, C. 2015. “Crowdfunding and the Energy Sector,” Exchange (18), pp. 1-11.

Chan, J., and Ghose, A. 2014. “Internet’s Dirty Secret: Assessing the Impact of Online Intermediaries on HIV Transmission,” MIS Quarterly (38:4), pp. 955-976.

Chava, S., Paradkar, N., and Zhang, Y. 2017. “Winners and Losers of Marketplace Lending: Evidence from Borrower Credit Dynamics,” Georgia Tech Scheller College of Business Research Paper No. 18-16, Georgia Tech University.

Chen, G., Crossland, C., and Huang, S. 2020. “That Could Have Been Me: Director Deaths, CEO Mortality Salience, and Corporate Prosocial Behavior,” Management Science (66:7), pp. 3142-3161.

Chen, Y., Ganesan, S., and Liu, Y. 2009. “Does a Firm’s Product-Recall Strategy Affect Its Financial Value? An Examination of Strategic Alternatives During Product-Harm Crises,” Journal of Marketing (73:6), pp. 214-226.

Chen, Y. C., Hung, M., and Wang, Y. 2018. “The Effect of Mandatory CSR Disclosure on Firm Profitability and Social Externalities: Evidence from China,” Journal of Accounting and Economics (65:1), pp. 169-190.

Cheng, Z., Pang, M. S., and Pavlou, P. A. 2020. “Mitigating Traffic Congestion: The Role of Intelligent Transportation Systems,” Information Systems Research (31:1), pp. 653-674.

Chevalier, J. A., and Mayzlin, D. 2006. “The Effect of Word of Mouth on Sales: Online Book Reviews,” Journal of Marketing Research (43:3), pp. 345-354.

Cho, Y. J. 2015. “Segment Disclosure Transparency and Internal Capital Market Efficiency: Evidence from SFAS No. 131,” Journal of Accounting Research (53:4), pp. 669-723.

Conning, J. 1999. “Outreach, Sustainability and Leverage in Monitored and Peer-Monitored Lending,” Journal of Development Economics (60:1), pp. 51-77.

Cull, R., Demirguc-Kunt, A., and Morduch, J. 2007. “Financial Performance and Outreach: A Global Analysis of Leading Microbanks,” Economic Journal (117:517), pp. F107-F133.

Cull, R., Demirgüç-Kunt, A., and Morduch, J. 2009. “Microfinance Meets the Market,” Journal of Economic Perspectives (23:1), pp. 167-192.

Daley-Harris, S. 2006. State of the Microcredit Summit Campaign: Report 2006, Microcredit Summit Campaign.

Dambra, M., and Gustafson, M. 2021. “Do the Burdens to Being Public Affect the Investment and Innovation of Newly Public Firms?,” Management Science (7:1), pp. 594-616..

Dehejia, R., Montgomery, H., and Morduch, J. 2012. “Do Interest Rates Matter? Credit Demand in the Dhaka Slums,” Journal of Development Economics (97:2), pp. 437-449.

Denis, D. J. 2011. “Financial Flexibility and Corporate Liquidity,” Journal of Corporate Finance (17:3), pp. 667-674.

DiMaggio, M., and Yao, V. 2019. “Fintech Borrowers: Lax-Screening or Cream-Skimming?.” (available at https://ssrn.com/abstract=3224957).

Dore, T., and Mach, T. 2019. “Marketplace Lending and Consumer Credit Outcomes: Evidence from Prosper,” FEDS Working Paper No. 2019-022 (available at SSRN: https://ssrn.com/abstract=3367450).

Dorfleitner, G., Leidl, M., Priberny, C., and von Mosch, J. 2013. “What Determines Microcredit Interest Rates?,” Applied Financial Economics (23:20), pp. 1579-1597.

Dorfleitner, G., Röhe, M., and Renier, N. 2017. “The Access of Microfinance Institutions to Debt Capital: An Empirical Investigation of Microfinance Investment Vehicles,” The Quarterly Review of Economics and Finance (65), pp. 1-15.

Drake, D., and Rhyne, E. 2002. The Commercialization of Microfinance: Balancing Business and Development. Kumarian Press.

Drake, M. S., Guest, N. M., and Twedt, B. J. 2014. “The Media and Mispricing: The Role of the Business Press in the Pricing of Accounting Information,” The Accounting Review (89:5), pp. 1673-1701.

Fan, J. P., and Wong, T. J. 2005. “Do External Auditors Perform a Corporate Governance Role in Emerging Markets? Evidence from East Asia,” Journal of Accounting Research (43:1), pp. 35- 72.

Field, E., Pande, R., Papp, J., and Rigol, N. 2013. “Does the Classic Microfinance Model Discourage Entrepreneurship Among the Poor? Experimental Evidence from India,” American Economic Review (103:6), pp. 2196-2226.

Gajjala, V., Gajjala, R., Birzescu, A., and Anarbaeva, S. 2011. “Microfinance in Online Space: A Visual Analysis of Kiva.Org,” Development in Practice (21:6), pp. 880-893.

Galak, J., Small, D., and Stephen, A. T. 2011. “Microfinance Decision Making: A Field Study of Prosocial Lending,” Journal of Marketing Research (48:SPL), pp. S130-S137.

Garmaise, M. J., and Natividad, G. 2010. “Information, the Cost of Credit, and Operational Efficiency: An Empirical Study of Microfinance,” Review of Financial Studies (23:6), pp. 2560- 2590.

Garmaise, M. J., and Natividad, G. 2013. “Cheap Credit, Lending Operations, and International Politics: The Case of Global Microfinance,” Journal of Finance (68:4), pp. 1551-1576.

George, G. 2005. “Slack Resources and the Performance of Privately Held Firms,” Academy of Management Journal (48:4), pp. 661- 676.

Gertler, P. J., Martinez, S., Premand, P., Rawlings, L. B., and Vermeersch, C. M. 2016. Impact Evaluation in Practice. The World Bank.

Ghose, A., Smith, M. D., and Telang, R. 2006. “Internet Exchanges for Used Books: An Empirical Analysis of Product Cannibalization and Welfare Impact,” Information Systems Research (17:1), pp. 3-19.

Glaeser, E. 2003. “Introduction to the Governance of Not-for-Profit Organizations,” in The Governance of Not-for-Profit Organization, E. L. Glaeser (ed.), University of Chicago Press, pp. 1-43.

Gonzalez, A. 2010. “Analyzing Microcredit Interest Rates: A Review of the Methodology Proposed by Mohammed Yunus,” MIX Data Brief No. 4, www.themix.org.

Goh, K. Y., Heng, C. S., and Lin, Z. 2013. “Social Media Brand Community and Consumer Behavior: Quantifying the Relative Impact of User- and Marketer-Generated Content,” Information Systems Research (24:1), pp. 88-107.

Hao, L., and Tan, Y. 2017. “Who Wants Consumers to Be Informed? Facilitating Information Disclosure in a Distribution Channel,” Information Systems Research (30:1), pp. 34-49.

Haq, M., Skully, M., and Pathan, S. 2010. “Efficiency of Microfinance Institutions: A Data Envelopment Analysis,” Asia-Pacific Financial Markets (17:1), pp. 63-97.

Hartarska, V. 2005. “Governance and Performance of Microfinance Institutions in Central and Eastern Europe and the Newly Independent States,” World Development (33:10), pp. 1627-1643.

Healy, P. M., and Palepu, K. G. 2001. “Information Asymmetry, Corporate Disclosure, and the Capital Markets: A Review of the Empirical Disclosure Literature,” Journal of Accounting and Economics (31:1), pp. 405-440.

Heckman, J. J. 1979. “Sample Selection Bias as a Specification Error,” Econometrica: Journal of the Econometric Society (47:1), pp. 153-161.

Helms, B., and Reille, X. 2004. “Interest Rate Ceilings and Microfinance: The Story So Far,” CGAP Occasional Paper No. 9 (https://www.cgap.org/sites/default/files/CGAP-Occasional-Paper-Interest-Rate-Ceilings-and-Microfinance-The-Story-So-Far-Sep-2004.pdf).

Hermes, N., Lensink, R., and Meesters, A. 2011. “Outreach and Efficiency of Microfinance Institutions,” World Development (39:6), pp. 938-948.

Holtmann, M., and Aijazuddin, M. 2015. “Small Beginnings for Great Opportunities: Lessons Learned from 20 Years of Microfinance Projects in IFC (English),” World Bank Group.

Hothorn, T., Hornik, K., and Zeileis, A. 2006. “Unbiased Recursive-Partitioning: A Conditional Inference Framework,” Journal of Computational and Graphical Statistics (15:3), pp. 651-674

Hwang, S., and Kim, W. 2016. “When Heirs Become Major Shareholders: Evidence on Pyramiding Financed by Related-Party Sales,” Journal of Corporate Finance (41), pp. 23-42.

Jensen, M. C. 1986. “Agency Costs of Free Cash Flow, Corporate Finance, and Takeovers,” American Economic Review (76:2), pp. 323-329.

Jha, S. K., Pinsonneault, A., and Dubé, L. 2016. “The Evolution of an ICT Platform-Enabled Ecosystem for Poverty Alleviation: The Case of eKutir,” MIS Quarterly (40:2), pp. 431-445.

Jin, G. Z., and Leslie, P. 2003. “The Effect of Information on Product Quality: Evidence from Restaurant Hygiene Grade Cards,” The Quarterly Journal of Economics (118:2), pp. 409-451.

Karlan, D. S., and Zinman, J. 2008. “Credit Elasticities in Less-Developed Economies: Implications for Microfinance,” American Economic Review (98:3), pp. 1040-1068.

Kim, K. and Hann, I. 2019. “Crowdfunding and the Democratization of Access to Capital: An Illusion? Evidence from Housing Prices,” Information Systems Research (30:1), pp. 276-290.

Kim, K., and Viswanathan, S. 2019. “The Experts in the Crowd: The Role of Experienced Investors in a Crowdfunding Market,” MIS Quarterly (43:2), pp. 347-372.

Kiva. 2015. A Guide to Kiva for Potential Field Partners. Kiva.org.

Khurana, S., Qiu, L., and Kumar, S. 2019. “When a Doctor Knows, It Shows: An Empirical Analysis of Doctors’ Responses in a Q&A Forum of an Online Healthcare Portal,” Information Systems Research (30:3), pp. 872-891.

Kwark, Y., Chen, J., and Raghunathan, S. 2017. “User-Generated Content and Competing Firms’ Product Design,” Management Science (64:10), pp. 4608-4628.

Leibenstein, H. 1966. “Allocative Efficiency vs. ‘X-efficiency,’” American Economic Review (56:3), pp. 392-415.

Leibenstein, H. 1978. “On the Basic Proposition of X-Efficiency Theory,” American Economic Review (68:2), pp. 328-332.

Lennox, C. S., Francis, J. R., and Wang, Z. 2012. “Selection Models in Accounting Research,” The Accounting Review (87:2), pp. 589- 616.

Leong, C., Pan, S. L., Newell, S., and Cui, L. 2016. “The Emergence of Self-organizing E-commerce Ecosystems in Remote Villages of China: A Tale of Digital Empowerment for Rural Development,” MIS Quarterly (40:2), pp. 475-484.

Lin, M., Prabhala, N. R., and Viswanathan, S. 2013. “Judging Borrowers by the Company They Keep: Friendship Networks and Information Asymmetry in Online Peer-to-Peer Lending,” Management Science (59:1), pp. 17-35.

Lin, M., and Viswanathan, S. 2016. “Home Bias in Online Investments: An Empirical Study of an Online Crowdfunding Market,” Management Science (62:5), pp. 1393-1414.

Little, R. J. 1985. “A Note about Models for Selectivity Bias,” Econometrica: Journal of the Econometric Society (53:6), pp. 1469-1474.

Liu, D., Brass, D., Lu, Y., and Chen, D. 2015. “Friendships in Online Peer-to-Peer Lending: Pipes, Prisms, and Relational Herding,” MIS Quarterly (39:3), pp. 729-742.

Liu, A., Mazumdar, T., and Li, B. 2014. “Counterfactual Decomposition of Movie Star Effects with Star Selection,” Management Science (61:7), 1704-1721.

Lück, S., Balsmeier, B., Seliger, F., and Fleming, L. 2020. “Early Disclosure of Invention and Reduced Duplication: An Empirical Test,” Management Science (66:6), pp. 2677-2685.

Mackenzie, A. 2015. “The Fintech Revolution,” London Business School Review (26:3), pp. 50-53.

Malkin, E. 2008. “Microfinance’s Success Sets off a Debate in Mexico,” New York Times, April 5, 2008, p. C1.

Manchanda, P., Packard, G., and Pattabhiramaiah, A. 2015. “Social Dollars: The Economic Impact of Customer Participation in a Firm-Sponsored Online Customer Community,” Marketing Science (34:3), pp. 367-387.

McGuire, P. B. 1999. “Policy and Regulation for Sustainable Microfinance: Country Experiences in Asia,” Journal of International Development (11:5), pp. 717-729.

Mersland, R., and Strøm, R. Ø. 2009. “Performance and Governance in Microfinance Institutions,” Journal of Banking & Finance (33:4), pp. 662-669.

Miller, M. K. 2013. “The Case Against Matching,” paper presented at PolMeth XXX, the 30th Annual Meeting of the Society for Political Methodology, University of Virginia, July 18-20.

Mollick, E. 2014. “The Dynamics of Crowdfunding: An Exploratory Study,” Journal of Business Venturing (29:1), pp. 1-16.

Morduch, J. 1999. “The Microfinance Promise,” Journal of Economic Literature (37:4), pp. 1569-1614.

Quidt, J., Fetzer, T., and Ghatak, M. 2018. “Commercialization and the Decline of Joint Liability Microcredit,” Journal of Development Economics (134), pp. 209-225.

Ray, G., Muhanna, W. A., and Barney, J. B. 2005. “Information Technology and the Performance of the Customer Service

Process: A Resource-Based Analysis,” MIS Quarterly (29:4), pp. 625-652.

Reed, L. R., Rao, D. S. K., Rogers, S., Rivera, C., Diaz, F., Gailly, S., Marsden, J., and Sanchez, X. 2015. Mapping Pathways out of Poverty: The State of the Microcredit Summit Campaign Report, Microcredit Summit Campaign.

Roodman, D. 2012. Due Diligence: An Impertinent Inquiry into Microfinance, Brookings Institution Press.

Rosenbaum, P. R., and Rubin, D. B. 1983. “The Central Role of the Propensity Score in Observational Studies for Causal Effects,” Biometrika (70:1), pp. 41-55.

Rosenberg, R., Gonzalez, A., and Narain, S. 2009. “The New Moneylenders: Are the Poor Being Exploited by High Microcredit Interest Rates?” CGAP Occasional Paper No. 15 (https://www.cgap.org/sites/default/files/CGAP-Occasional-Paper-The-New-Moneylenders-Are-the-Poor-Being-Exploitedby-High-Microcredit-Interest-Rates-Feb-2009.pdf). CGAP.

Roy, J., and Chowdhury, P. R. 2009. “Public-Private Partnerships in Micro-Finance: Should NGO Involvement Be Restricted?” Journal of Development Economics (90:2), pp. 200-208.

Seamans, R., and Zhu, F. 2013. “Responses to Entry in Multi-Sided Markets: The Impact of Craigslist on Local Newspapers,” Management Science (60:2), pp. 476-493.

Servin, R., Lensink, R., and van den Berg, M. 2012. “Ownership and Technical Efficiency of Microfinance Institutions: Empirical Evidence from Latin America,” Journal of Banking & Finance (36:7), pp. 2136-2144.

Spann, M., and Hudson, R. 1988. “Resource Acquisition by Entrepreneurial Firms: Another Look,” in The New Institutionalism in Organizational Analysis, W. Powell and P. DiMaggio (eds.), University of Chicago Press.

Starr, J., and MacMillan, I. 1990. “Resource Cooptation via Social Contracting: Resource Acquisition Strategies for New Ventures,” Strategic Management Journal (11), pp. 79-93.

Strøm, R. Ø., D’Espallier, B., and Mersland, R. 2014. “Female Leadership, Performance, and Governance in Microfinance Institutions,” Journal of Banking & Finance (42), pp. 60-75.

Srivastava, S. C., Teo, T. S., and Devaraj, S. 2016. “You Can't Bribe a Computer: Dealing with the Societal Challenge of Corruption Through ICT,” MIS Quarterly (40:2), pp. 511-526.

Tam, K. Y. 1998. “The Impact of Information Technology Investments on Firm Performance and Evaluation: Evidence from Newly Industrialized Economies,” Information Systems Research (9:1), pp. 85-98.

Tchuigoua, H. T. 2014. “Institutional Framework and Capital Structure of Microfinance Institutions,” Journal of Business Research (67:10), pp. 2185-2197.

Thirumalai, S., and Sinha, K. K. 2013. “To Personalize or Not to Personalize Online Purchase Interactions: Implications of Self-Selection by Retailers,” Information Systems Research (24:3), pp. 683-708.

Venkatesh, V. and Sykes, T. A. 2013. “Digital Divide Initiative Success in Developing Countries: A Longitudinal Field Study in a Village in India,” Information Systems Research (24:2), pp. 239- 260.

Venkatesh, V., Sykes, T. A., Rai, A., and Setia, P. 2019. “Governance and ICT4D Initiative Success: A Longitudinal Field Study of Ten Villages in Rural India,” MIS Quarterly (43:4), pp. 1081-1104.

Weiss, M., and Tarchinskaya, E. 2015. “The Role of Information Technologies in Changing the Status of Women to Improve

Human Conditions,” in Grand Societal Challenges in Information Systems Research and Education, J. vom Brocke, A. Stein, S. Hofmann, and S. Tumbas (eds.), Springer, pp. 51-60.

Wing, C., Simon, K., and Bello-Gomez, R. A. 2018. “Designing Difference in Difference Studies: Best Practices for Public Health Policy Research,” Annual Review of Public Health (39), pp. 453- 469.

Xu, S. X., and Zhang, X. 2013. “Impact of Wikipedia on Market Information Environment: Evidence on Management Disclosure and Investor Reaction,” MIS Quarterly (37:4), pp. 1043-1068.

Yahav, I., Shmueli, G., and Mani, D. 2016. “A Tree-Based Approach for Addressing Self-Selection in Impact Studies with Big Data,” MIS Quarterly (40:4), pp. 819-848.

Yunus, M. 2000. “How Donor Funds Could Better Reach and Support Grassroots Microcredit Programmes: Working Towards the Microcredit Summit’s Goal and Core Themes,” Bangladesh Development Studies (26:2-3), pp. 1-14.

Zhang, J., and Liu, P. 2012. “Rational Herding in Microloan Markets,” Management Science (58:5), pp. 892-912.

Zhang, X. M., and Zhang, L. 2015. “How Does the Internet Affect the Financial Market? An Equilibrium Model of Internet-Facilitated Feedback Trading,” MIS Quarterly (39:1), pp. 17-38.

Zheng, H., Li, D., Wu, J., and Xu, Y. 2014. “The Role of Multidimensional Social Capital in Crowdfunding: A Comparative Study in China and US,” Information & Management (51:4), pp. 488-496.

## About the Authors

Xuechen Luo is an assistant professor in the School of Business and Management at Shanghai International Studies University. She holds a Ph.D. in information management from the College of Business, City University of Hong Kong. Her main research interest is in the economics of information systems. She is interested in understanding how information technology disrupts financial systems and the digital divide.

Ling Ge is an assistant professor of business analytics at the University of North Texas. She graduated from the University of Texas at Austin and has published in Information Systems Research, Journal of Marketing, Journal of the Association of Information Systems, and other journals. Her research interests are in online platforms, financial analytics, healthcare analytics, and the interactions between online and offline business strategies. Before joining UNT, she worked at the City University of Hong Kong.

Chong (Alex) Wang is an associate professor at the Peking University Guanghua School of Management. He holds a Ph.D. in information management from HKUST Business School, an M.Sc. in finance from Tsinghua University, and a B.S. in applied mathematics from Peking University. Dr. Wang’s research interests concern the impact of technology development on creating, disseminating, and processing information in the digital economy. His work examines social media, online social networks, open innovations, matching in online platforms, privacy, and emerging fintech applications.

## Appendix A

## Descriptive Statistics for Treated and Control Group before and after Matching

<table><tr><td colspan="8">Table A1. Descriptive Statistics for Treated and Control Group Before and After Matching</td></tr><tr><td rowspan="3">Variable</td><td rowspan="2">Treatment group</td><td colspan="6">Control group</td></tr><tr><td colspan="3">Before matching</td><td colspan="3">After matching</td></tr><tr><td>Mean</td><td>Mean</td><td>Mean diff.</td><td>t stat.</td><td>Mean</td><td>Mean diff.</td><td>t stat.</td></tr><tr><td>Age (new)</td><td>0.0685</td><td>0.0804</td><td>0.0119</td><td>0.3973</td><td>0.0685</td><td>0.0000</td><td>0.0000</td></tr><tr><td>Age (young)</td><td>0.1781</td><td>0.1890</td><td>0.0109</td><td>0.2397</td><td>0.1918</td><td>0.0137</td><td>0.2117</td></tr><tr><td>Age (mature)</td><td>0.7534</td><td>0.7306</td><td>-0.0228</td><td>-0.4457</td><td>0.7397</td><td>-0.0137</td><td>-0.1890</td></tr><tr><td>MFI size (millions)</td><td>71.400</td><td>152.00</td><td>80.900</td><td>3.9286***</td><td>76.200</td><td>4.7875</td><td>0.1805</td></tr><tr><td>Personnel</td><td>469.97</td><td>475.54</td><td>5.5676</td><td>0.0216</td><td>422.90</td><td>-47.069</td><td>-0.1691</td></tr><tr><td>ROA</td><td>0.0225</td><td>0.0145</td><td>-0.0080</td><td>-1.0055</td><td>0.0132</td><td>-0.0093</td><td>-0.5807</td></tr><tr><td>Percentage of loans to women</td><td>0.6972</td><td>0.6475</td><td>-0.0497</td><td>-1.7601*</td><td>0.6745</td><td>-0.0227</td><td>-0.5714</td></tr><tr><td>Cost per loan</td><td>4.6691</td><td>4.6547</td><td>-0.0144</td><td>-0.1527</td><td>4.6912</td><td>0.0221</td><td>0.1347</td></tr><tr><td>Write-off ratio</td><td>0.0167</td><td>0.0199</td><td>0.0032</td><td>1.1429</td><td>0.0141</td><td>-0.0026</td><td>-0.6592</td></tr><tr><td>Population (millions)</td><td>44.300</td><td>179.00</td><td>134.00</td><td>7.2361***</td><td>44.800</td><td>0.4588</td><td>0.0191</td></tr><tr><td>GDP per capita</td><td>2729.8</td><td>3518.4</td><td>788.61</td><td>3.1853***</td><td>2398.7</td><td>-331.11</td><td>-0.9934</td></tr></table>

Note: \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01.

## Appendix B

## Tree-Based Approach

## Generating the Tree

Following the tree-based approach for treatment effect identification, we used the conditional inference (CI) trees to generate a decision tree that predicts Kiva partnership (Yahav et al. 2016; Hothorn et al. 2006). We partitioned observations at the MFI-year level. Table B1 reports the variables used to generate the tree. Figure B1 depicts the resulting tree and the number of observations of the treatment and control groups at each terminal node. There are 14 terminal nodes in total.

## Elimination of Terminal Nodes

When a terminal node is dominated by one group or is without sufficient observations, it might lack the statistical power needed to examine the treatment effect (Yahav et al. 2016). Therefore, we eliminated Nodes 3, 8, 18, 19, 24, 26, and 27.

<table><tr><td colspan="2">Table B1. Variable Descriptions</td></tr><tr><td>Variable</td><td>Definition</td></tr><tr><td colspan="2">MFIs characteristics</td></tr><tr><td>MFI age</td><td>Indicator of the maturity of the MFI (new, young, and mature)</td></tr><tr><td>MFI size</td><td>Measured number of borrowers, average loan size, and asset-to-loan ratio</td></tr><tr><td>Personnel</td><td>Number of staff members</td></tr><tr><td>Return on Assets (ROA)</td><td>Net operating income / assets</td></tr><tr><td colspan="2">Loan portfolio characteristics</td></tr><tr><td>Percentage of loans to women</td><td>Number of loans to female borrowers / total number of loans</td></tr><tr><td>Cost per loan</td><td>Operating expense / average number of outstanding loans</td></tr><tr><td>Write-off ratio</td><td>Total amount of loans written off / average gross loan portfolio</td></tr><tr><td colspan="2">Macroeconomic variables</td></tr><tr><td>GDP per capita</td><td>GDP per capita of MFI&#x27;s country</td></tr><tr><td>Population</td><td>Population of MFI&#x27;s country</td></tr><tr><td>Workforce participation</td><td>Labor force participation rate = labor force / population aged 15+</td></tr><tr><td>Inflation</td><td>Consumer price inflation of MFI&#x27;s country</td></tr><tr><td>Region</td><td>The region of MFIs, including Africa (R1), East Asia and the Pacific (R2), Eastern Europe and Central Asia (R3), Latin America and The Caribbean (R4), Middle East and North Africa (R5) and South Asia (R6)</td></tr><tr><td>Fiscal year</td><td>The fiscal year of observations</td></tr></table>

![](/api/attachments/UHFJCKYT/fulltext/images/2254693d95ea3196f02a91accf25d304a78721066d53ee08f71f305d08126a60.jpg)  
Figure B1. Classification Tree T = Kiva / No Kiva—For Each Node, We Specify the Sample Sizes n = (Kiva, no Kiva)

## Appendix C

## Heckman Selection Model Details

The first-stage selection model is shown in the following equations. For selection variables, we first relied on the internet penetration rate and percentage of rural population as the exclusion restrictions. We then included more variables to model the selection of a Kiva partnership. We considered age, size, indicators of social orientation (e.g., percentage of loans to women, average loan balance per borrower), and return on assets (ROA), which are related to the main requirements of a Kiva partnership (e.g., social mission and size) (Hermes et al. 2011; Dorfleitner et al. 2017). We also included other macroeconomic variables: GDP per capita, population, workforce participation, and inflation.

$$
\begin{array}{r l} & {J o i n K i v a _ {i} ^ {*} = \delta_ {1} A g e _ {i} + \delta_ {2} F e m a l e \% _ {i} + \delta_ {3} A v g B a l a n c e _ {i} + \delta_ {4} R O A _ {i} + \delta_ {5} I n t e r n e t _ {i} + \delta_ {6} \% R u r a l _ {i} + \delta_ {7} G D P _ {i} + \delta_ {8} P o p u l a t i o n _ {i}} \\ & {\qquad + \delta_ {9} W o r k f o r c e _ {i} + \delta_ {1 0} I n f l a t i o n _ {i} + \varepsilon_ {i}} \\ & {\qquad J o i n K i v a _ {i} = 1 \mathrm{if} J o i n K i v a _ {i} ^ {*} > 0, \mathrm{and} J o i n K i v a _ {i} = 0 \mathrm{otherwise}} \\ & {\qquad \operatorname{Prob} (J o i n K i v a _ {i} = 1 | v _ {i}) = \Phi (v _ {i} \delta),} \\ & {\qquad \operatorname{Prob} (J o i n K i v a _ {i} = 0 | v _ {i}) = 1 - \Phi (v _ {i} \delta),} \end{array}
$$

where $v _ { i }$ is the vector of covariates in the first-stage model. The estimation result from the first-stage model is reported in Table C1.

The second-stage model is:

$$
D e p _ {i t} = \beta_ {0} + \beta_ {1} A f t e r K i v a _ {i t} + C o n t r o l V a r i a b l e s _ {i t} + \mu_ {i} + \delta_ {t} + \lambda (\cdot) + \epsilon_ {i t}
$$

We included the same controls as in the difference-in-differences model analysis. ??(∙) refers to the inverse Mills ratio from the first-stage model.

<table><tr><td colspan="2">Table C1. Heckman Selection Model: Selection Stage</td></tr><tr><td></td><td>Joined Kiva</td></tr><tr><td rowspan="2">Age (young)</td><td>0.2177*</td></tr><tr><td>(0.1155)</td></tr><tr><td rowspan="2">Age (mature)</td><td>0.2191**</td></tr><tr><td>(0.1069)</td></tr><tr><td rowspan="2">Percentage of loans to women</td><td>0.8087***</td></tr><tr><td>(0.1306)</td></tr><tr><td rowspan="2">Average loan balance per borrower</td><td>-0.1440***</td></tr><tr><td>(0.0350)</td></tr><tr><td rowspan="2">ROA</td><td>-0.0345</td></tr><tr><td>(0.2177)</td></tr><tr><td rowspan="2">Internet penetration rate</td><td>-0.1257</td></tr><tr><td>(0.2418)</td></tr><tr><td rowspan="2">Percentage of rural population</td><td>-0.9261***</td></tr><tr><td>(0.1963)</td></tr><tr><td rowspan="2">GDP per capita</td><td>-0.1869***</td></tr><tr><td>(0.0519)</td></tr><tr><td rowspan="2">Population</td><td>-0.3090***</td></tr><tr><td>(0.0201)</td></tr><tr><td rowspan="2">Workforce participation</td><td>0.0164</td></tr><tr><td>(0.2173)</td></tr><tr><td rowspan="2">Inflation</td><td>-0.5298**</td></tr><tr><td>(0.2247)</td></tr><tr><td rowspan="2">Constant</td><td>5.0302***</td></tr><tr><td>(0.6407)</td></tr><tr><td>MFI size controls</td><td>Yes</td></tr><tr><td>Pseudo R2</td><td>0.1015</td></tr></table>

Note: \*p < 0.1 \*\*p < 0.05 \*\*\*p < 0.01, robust standard errors in parentheses.

## Appendix D

## Discussion: Parallel Trend Assumption

Examining the parallel trend assumption to ensure the validity of difference-in-differences models is critical. We provide visual and statistical evidence in support of a parallel trend assumption. First, to visually inspect the assumption, we plotted the average values of operational self sufficiency (OSS) and interest rates of the treatment and control groups from t-4 to t+3 using both the full sample (Figure D1a) and the matched sample (Figure D1b) (Agarwal and Qian 2014; Brynjolfsson et al. 2019; Chen et al. 2020; Lück et al. 2020). As shown in Figures D1a and D1b, the trends between the treatment group and control group have no obvious and meaningful difference before a Kiva partnership, suggesting that the parallel trend assumption holds.

Second, we used the leads and lags model to statistically test the assumption (see the Falsification Test section in the main body of the paper). As shown in Table 6, the coefficients of before-period indicators (i.e., Kiva <sub>t-3</sub>, Kiva <sub>t-2</sub>, and Kiva <sub>t-1</sub>) are not significant, suggesting that there is no significant difference in OSS and interest rates between the treatment and control groups over time before a Kiva partnership, which also supports the parallel trend assumption (Khurana et al. 2019; Cheng et al. 2020).

![](/api/attachments/UHFJCKYT/fulltext/images/2e1ea2d8632e9112b1b0ec7a589877ccb6df79f03ababf593b00e7ca02f87318.jpg)

![](/api/attachments/UHFJCKYT/fulltext/images/d29dec1d321a821ee639f17deab9bb6c42c931488e0e2b8ad524c35c1509b2de.jpg)

![](/api/attachments/UHFJCKYT/fulltext/images/4ecc8464740872c3cbba42f5d3b3859206f2cc6ccaeed4521c7995898d34fccd.jpg)  
(a) Full Sample

![](/api/attachments/UHFJCKYT/fulltext/images/32388599b2b8bdeb7b79885008312326b88b78672be7009067337a29a9517fe1.jpg)  
(b) Matched Sample
