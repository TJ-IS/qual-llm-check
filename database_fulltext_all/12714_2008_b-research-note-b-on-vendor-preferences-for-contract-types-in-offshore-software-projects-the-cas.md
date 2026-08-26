---
otero_id: 12714
otero_key: "9G3HF87T"
title: "<b>Research Note</b>—On Vendor Preferences for Contract Types in Offshore Software Projects: The Case of Fixed Price vs. Time and Materials Contracts"
authors: "Anandasivam Gopal; Konduru Sivaramakrishnan"
year: "2008"
journal: "Information Systems Research"
doi: "10.1287/isre.1070.0162"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/9G3HF87T/fulltext/images/a25ea906ec56cb0b40cee9c97f53f7b2218596028a7d6ff5cbf0f3eae31b2f7b.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Note—On Vendor Preferences for Contract Types in Offshore Software Projects: The Case of Fixed Price vs. Time and Materials Contracts

Anandasivam Gopal, Konduru Sivaramakrishnan,

Anandasivam Gopal, Konduru Sivaramakrishnan, (2008) Research Note—On Vendor Preferences for Contract Types in Offshore Software Projects: The Case of Fixed Price vs. Time and Materials Contracts. Information Systems Research 19(2):202-220. http://dx.doi.org/10.1287/isre.1070.0162

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2008, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/9G3HF87T/fulltext/images/468a5b45458946f5b97f16d8895273b05bfadf403b3bc5061d824a0191db4fa7.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# On Vendor Preferences for Contract Types in Offshore Software Projects: The Case of Fixed Price vs. Time and Materials Contracts

Anandasivam Gopal

Robert H. Smith School of Business, University of Maryland, College Park, Maryland 20742, agopal@rhsmith.umd.edu

Konduru Sivaramakrishnan

C.T. Bauer College of Business, University of Houston, Houston, Texas 77204, shiva@uh.edu

rior research has indicated that, on average, offshore vendors have higher profits associated with time and materials (T&M) contracts than fixed price (FP) contracts. This research raises two questions. First, Is the relative importance of various profit drivers different across two contractual regimes? Second, Does it follow that vendors unconditionally prefer T&M contracts for all projects? We address these questions by using data on 93 offshore projects completed by a leading Indian vendor. We use an endogenous switching regression framework and the program evaluation methodology to show that profit equations are distinctly different for the two contractual regimes. Using these two profit equations, we also identify contingencies under which the vendor prefers an FP contract to a T&M contract. We hypothesize that the vendor’s ability leverage information asymmetry about capabilities and experiences translates into the vendor preferring FP contract to secure larger information rents. Our results support this hypothesis and suggest that the vendor would prefer the FP contract for larger and longer projects with larger teams. However, vendors would prefer a T&M contract when the risk of employee attrition from the project team is high. In addition, we discuss managerial implications of these results in the paper.

Key words: software outsourcing; offshore software development; contracts; profitability; regression analysis History: Vallabh Sambamurthy, Senior Editor. This paper was received on September 6, 2006, and was with the authors 3 months and 3 weeks for 2 revisions.

## 1. Introduction

The rapid growth of offshore software development has triggered considerable research on important managerial issues in offshore development, such as the effect of prior ties between clients and vendors (Ethiraj et al. 2005), the impact of cross-cultural problems (Krishna et al. 2004), and the role of communication mechanisms (Gopal et al. 2002). Contracting practices in the industry have also become the subject of significant research interest, because contracts determine how risks are shared between clients and vendors (Lacity and Hirschheim 1993). Offshore contracts are typically of two types—T&M contracts and FP contracts—with differing risk implications for offshore clients and vendors. Recent work has shown that, on average, the vendor makes higher profits in

T&M contracts than in FP contracts (Gopal et al. 2003, Ethiraj et al. 2005).

However, extant research has paid little attention to whether vendors manage T&M projects differently from FP projects and the consequent implications for vendor profitability. Indeed, evidence suggests that the daily management of a project is influenced by the contract type. Vendors often assign more trained personnel to FP contracts because they bear higher risk in these projects (Arora and Asundi 1999). They are much less likely to accept requirement changes and more stringent controls from clients in FP contracts (Kalnins and Mayer 2004). Therefore, profit drivers are likely to affect profitability differently across the two contract types. Identifying and characterizing these differences is important in advancing our understanding of contracting practices in offshore projects. Motivated by these considerations, we examine differing marginal effects of various profit drivers on profitability under T&M and FP contracts by estimating them as two distinct contractual regimes, rather than assume that the contract type merely shifts project profitability without influencing the profit drivers themselves.

In light of such differences across contractual regimes, a natural question that arises is whether a vendor might, in fact, prefer FP contracts for certain projects and T&M contracts for other projects. Evidence indicates that vendors are protected from risk in T&M contracts and that these contracts provide, on average, higher profitability compared to FP contracts (Ethiraj et al. 2005, Banerjee and Duflo 2000). But there is also evidence suggesting that the vendor might prefer FP contracts for some projects. For instance, there is reason to believe that capable and reputable vendors prefer higher risk FP contracts for some projects because the returns can be higher (Ethiraj et al. 2005, Lichtenstein 2004). It is not clear what distinguishes these projects from others for which the vendor might prefer the risk protection of a T&M contract. This issue cannot be addressed if we were to assume that the effects of various profit drivers are equal across the two contract types. By explicitly framing and testing the two-regime model, we can explore the conditions under which the vendor might prefer an FP contract to a T&M contract.<sup>1</sup>

The FP contract presents a trade-off to the vendor. It imposes greater risk relative to the T&M contract. On the other hand, it allows the vendor to benefit from any private information that the vendor possesses about his capabilities, true operating costs and domain knowledge, unknown to clients, that may provide him with information rents (Bajari and Tadelis 2001, Banerjee and Duflo 2000). Indeed, prior research suggests that service providers gain significant information rents by using their private information (Nayyar 1993). In contrast, information rents that accrue to the vendor under a T&M contract are reduced because clients have a greater incentive to monitor the vendor (Bajari and Tadelis 2001). Thus the vendor trades off the benefit from information asymmetry under an FP contract versus risk protection under the T&M contract. Prior research also suggests that vendor payoffs should be expected to increase under the FP contract relative to the T&M contract as projects become more risky, intangible, and represent knowledge work higher up in the value chain (Ethiraj et al. 2005, Shah 2004). Nayyar (1993) refers to these services as “experience based,” where clients have to experience the services before being able to judge service quality. Accordingly, we hypothesize that the vendor would be more inclined to prefer the FP contract for (riskier) projects whenever it is possible to extract significant information rents from clients.

To test this hypothesis, we use the program evaluation methodology (Maddala 1983) to estimate the vendor’s expected profit from the chosen contract (say, T&M), and the expected profit had the alternative contract type (FP) been chosen. By comparing the vendor’s profit expectation under the chosen contract and under the alternative contract, we can quantify the extent to which the vendor would prefer one contract type over the other for a given project. In addition, we can empirically determine the impact of project characteristics such as project size, duration, and team size on the vendor’s preferences over contracts.

Using data collected on 93 software development projects from an offshore software vendor located in India, our research shows that the vendor prefers FP contracts for large projects with longer durations and larger teams. These projects allow the vendor to extract greater information rents from the client based on the vendor’s private information about his capabilities and experience. However, in cases where there is significant risk of employee attrition from the project team, the vendor prefers T&M contracts. Our analysis thus provides a more nuanced examination of vendor preferences over contract types based on risk exposure and information asymmetry. We develop our hypotheses in the next section. Section 3 describes the data. Section 4 describes the methodology and estimation procedures. In §5, we present the results, and in §6, we provide a conclusion with some managerial implications of our work.

## 2. Theory and Hypotheses

## 2.1. Two Contractual Regimes

Our primary objective in this paper is to evaluate the ex ante preferences of the vendor with respect to contract types at the project level. Prior research has indicated that, on average, vendor profits are higher under T&M contracts, all else being equal (Gopal et al. 2003, Ethiraj et al. 2005). However, it does not necessarily follow that the vendor would prefer a T&M contract over an FP contract for all projects. It is possible, for instance, that the risk protection provided by the T&M contract might be overshadowed by the profitability potential in FP contracts for a small set of projects. Indeed, prior research has shown that risk protection may not explain an agent’s preferences over contracts entirely (Allen and Lueck 1999). To identify contingencies where the vendor might prefer an FP contract, it is first necessary to modify the existing approach that characterizes the effect of contract type on profitability.

Typically, the impact of contract type on profitability in a project is measured by modeling the contract type as a binary variable in a profit regression (Gopal et al. 2003, Ethiraj et al. 2005). The effect of a different contract choice is captured by the coefficient of this binary variable. This approach implicitly assumes that the vendor manages both FP and T&M contracts in the same manner; the binary contract variable merely moves the regression intercept without affecting the coefficients of the profit drivers in any way. However, it seems more reasonable to suppose that the vendor would manage FP and T&M projects differently for a variety of reasons.

First, the vendor faces distinctly different incentives under the two contractual regimes. The FP contract places a cap on revenues from a project. Therefore, a profit-maximizing vendor would strive to minimize the project cost (Kalnins and Mayer 2004) by allocating less expensive resources and/or ensuring efficient utilization of the resources allocated (Arora and Asundi 1999). Under a T&M contract, however, the vendor has a natural incentive to increase effort (or duration) and/or allocate more resources to the project because the margin from the project is a function of the total effort. This might even lead the vendor to overinvest in enhancing project functionality and overdelivering on project requirements when a T&M contract is used (Corts and Singh 2004, Kalnins and Mayer 2004).

Second, prior research establishes that the risk exposure to the vendor under FP contracts is significantly different from that under T&M contracts (Banerjee and Duflo 2000, Kalnins and Mayer 2004). Indeed, much of the empirical literature on contracts considers risk sharing as central to contract choice (Masten and Saussier 2002). FP contracts expose the vendor to greater risk because any cost and schedule over runs are borne by the vendor (Banerjee and Duflo 2000) which is not the case under T&M contracts.

The greater risk exposure under the FP contract will likely induce the vendor to adopt stronger risk mitigation strategies by purposefully deploying his critical resources on an FP project rather than on a T&M project. The literature suggests that managerial and technical resources in information technology (IT) are critical in providing firms with a competitive advantage and are in short supply in the offshore market (Powell and Dent-Micallef 1997, Bharadwaj 2000, Ethiraj et al. 2005). Therefore the difference in risk exposure and incentives between contracts will result in differential deployment of experienced personnel to projects based on contract. Indeed, anecdotal evidence suggests that outsourcing vendors place more experienced and senior staff on FP projects, while staffing T&M projects with relatively junior managers (Arora and Asundi 1999).

A significant aspect of risk mitigation in software projects pertains to the project and process management activities (Pressman 1992). The rise of the software process initiatives in the global software industry is a reaction to the need for enhanced project and risk management experience in the industry (Gopal et al. 2002). It is also well established that software processes and project management activities are costly (Krishnan et al. 2000, Gopal et al. 2002). Given the focus on efficient utilization of resources under FP contracts alluded to earlier, it is reasonable to argue that projects under FP contracts would receive greater management attention, on the margin, than T&M contracts.

Finally, the client’s role is likely to differ across T&M and FP regimes. It is well known in the principal-agent literature that when the agent’s effort is unobservable, any additional information made available by monitoring the agent enhances the value of the contract (Holmstrom 1979). The relevance of client monitoring has been established in the literature on outsourcing as being beneficial to the overall health of the project (Lacity and Hirschheim 1993). The extent to which the client monitors the vendor will be directly proportional to the risks borne by the client. Under T&M contracts, the client bears the bulk of the uncertainty, leading to a greater level of client monitoring and control (Ethiraj et al. 2005, Kirsch et al. 2002). On the margin, FP contracts substitute the need for monitoring the vendor with stronger incentives for vendor efficiency and self-monitoring (Bajari and Tadelis 2001).

On the basis of the differences in risk exposures, incentives, project management, and client involvement, we have the following proposition.

Proposition 1. There exist two distinct contractual regimes in the offshore outsourcing model, i.e., the marginal effects of profit drivers on vendor profitability are different across FP and T&M contracts.

While it seems more reasonable to assume that FP and T&M represent two distinct contractual regimes than to assume a single regime (as in prior studies), we explicitly test for the existence of two distinct regimes as a matter of empirical rigor—we outline these tests in the analysis section of this paper. However, because our primary focus is on analyzing the preferences of the vendor over contract types, we turn our attention to identifying conditions under which the vendor prefers an FP contract over the T&M contract.

## 2.2. Vendor’s Preferences Over Contract Type

At the time of contracting, a rational vendor evaluates the profitability expectations from both contract types for the project and prefers the contract with the higher expected profit (Corts and Singh 2004, Kalnins and Mayer 2004). It is, however, not necessary that the contract that is finally chosen be the vendor’s preferred contract; both vendor and client preferences and their relative negotiating powers need to be considered in rationalizing the final contract choice (Svejnar 1986).

To tease out vendor contract preferences at the level of the individual project, it is necessary to analyze vendor profitability expectations at the subsample level, i.e., within the (realized) T&M and FP subsamples. Analysis conducted at the level of the complete sample can only provide insight into which contract type delivers, on average, higher expected profitability for the vendor (Gopal et al. 2003, Ethiraj et al. 2005). In contrast, by studying the profit expectations within the FP and T&M subsamples, we can identify conditions where the realized contract type deviated from the vendor’s preferred contract. Note that under the assumption of one contractual regime (as seen in Gopal et al. 2003 and Ethiraj et al. 2005), it would not be possible to perform this analysis because the only conclusion that can be drawn is that the vendor’s profit expectation would always be higher in T&M contracts compared to FP contracts, all else being equal.

Prior empirical research has examined preferences of the contracting parties based primarily on risksharing (Gopal et al. 2003, Kalnins and Mayer 2004, Corts and Singh 2004). The definition of risk in an offshore software project includes the probability of incurring significant ex post costs of renegotiation (Bajari and Tadelis 2001). The effects of risk are exacerbated because of the technical and managerial issues that surround a typical software outsourcing engagement (Lacity and Hirschheim 1993). Therefore, given the primacy of risk exposure, if the T&M contract is the chosen contract for a given project, the vendor likely prefers it over the FP contract for that project. That is, in every realized T&M project, the vendor’s preference would be for the T&M contract over the FP contract. The riskier the project, the greater is the ex ante preference for the T&M contract. Therefore, we postulate the following hypothesis, which can be seen as an affirmation of the arguments made in Gopal et al. (2003)<sup>2</sup> and in other work on contract choice (Kalnins and Mayer 2004).

Hypothesis 1. In the T&M subsample, the ex ante profit expectation of the vendor is higher under the T&M contract relative to the ex ante profit expectation under the FP contract.

Risk exposure, however, is not the only factor that explains the vendor’s preference for a contract type. In a series of papers on agricultural contracts, Allen and Lueck (1992, 1995, 1999) have explored the role of client and vendor risk postures in determining the choice between crop-share and cash-rent contracts. Crop-share contracts divide the risk inherent in farming between the landowner and the farmer, whereby the landowner receives a share of the harvested crop. In contrast, cash-rent contracts involve a one-time cash payment made by the farmer to the landowner for use of the land. The farmer then owns any surplus (net of the rent) from farming the land but also bears all the risk in this activity. The cash-rent contract is analogous to the FP contract, while the crop-share contract shares some of the incentive and risk-sharing elements of T&M contracts.

Intuitively, increased risk of farming a certain crop should lead to a higher use of crop-sharing contracts because they allow risk-averse farmers to share risk with the land-owners, as per agency theory. As farming gets less risky, the probability of a cash-rent should increase. However, the bulk of the empirical evidence shows that this is not the case. There appears to be no significant correlation between the riskiness of farming and the use of the crop-share contract, indicating that the chosen contract is driven not just by risk sharing, but by other considerations such as information asymmetry and measurement costs (Allen and Lueck 1999, p. 727).

Indeed, information asymmetry is a significant problem that characterizes the services industry, in general, and the offshore context, in particular. Clients often face a serious problem of gauging seller reliability, quality, and efficiency. While several mechanisms can be adopted to reduce the impact of this information asymmetry (such as certification and reputation (Akerlof 1970)), Nayyar (1990) argues that they do so only imperfectly. These imperfect mechanisms provided well-diversified sellers with opportunities to benefit from residual informational asymmetries. Thus, sellers often have private information about their capabilities and resources, which can allow them to extract information rents from their clients. The potential for information rents is larger for experience or credence services, such as software outsourcing, because information asymmetry is more pronounced (Nayyar 1993, p. 42).<sup>3</sup> In our context, this raises the possibility that the vendor might actually prefer an FP contract for some projects if the resulting information rents outweigh the benefits of risk protection in a T&M contract.

Under the FP contract, riskier projects provide the vendor with the means to leverage information asymmetry, with respect to the true cost of development and the true scale of vendor capabilities available. In contrast, the client has a greater incentive to monitor the vendor under a T&M contract (as discussed earlier), which reduces any information rents a diversified vendor might otherwise be able to extract (Bajari and Tadelis 2001). Similar arguments have been made by other researchers in the offshore domain without explicitly focusing on the trade-offs between information asymmetry and risk exposure. For instance, Ethiraj et al. (2005) postulated that as the Indian industry matures from low-risk projects to high-risk development, the potential payoffs should be higher in FP contracts than in T&M contracts. However, this is possible only if the clients do not accordingly adjust their expectations with respect to Indian vendors. If clients have complete information about vendor capabilities and cost structure, there is no reason to believe this information will not be leveraged, thereby reducing the difference between the gains from FP and T&M contracts for the vendor. Additionally, high-risk activities include business consulting and high-end implementation projects, which are more “experience based” and intangible (Nayyar 1993), providing the vendor with greater abilities to leverage his private information through the FP contract than the T&M contract.

This reasoning raises the possibility that the FP subsample of projects includes projects where the FP contract was imposed on the vendor by the client and those where the vendor preferred the FP contract to secure larger information rents. The issue is one of identifying projects that provide the vendor with higher information rents. Prior research shows that the seller’s returns from information asymmetry increase as service offerings become more intangible and less difficult to evaluate (Nayyar 1993). Because software services characterized by higher intangibility and difficulty in evaluation represent riskier projects (Kalnins and Mayer 2004), the gains from information asymmetry for vendors should be increasing in dimensions of project risk. Larger and longer projects are generally considered riskier because there is a high chance of specifications changing (Nidumolu 1995, Pressman 1992), the complexity of the code and various modules add to the risk in the project (Barki et al. 1993), and client interaction is costly and difficult (Carmel and Agarwal 2002). Therefore project duration and total effort are good proxies for the risks in the project. In addition, projects with larger teams require significant coordination and project management and are also considered riskier (Ethiraj et al. 2005, Arora and Asundi 1999). Therefore, we propose the following hypothesis.

Hypothesis 2. In the FP subsample, the vendor’s (ex ante) profit expectation is higher under the FP contract relative to the T&M contract for projects characterized by large size, longer durations, and larger teams.

As described by Nayyar (1990) and Kalnins and Mayer (2004), there are some aspects of the relationship between the vendor and client that work toward reducing information asymmetry. Specifically, the presence of repeated interactions between the client and vendor provides the client with more insight into the vendor’s capabilities and also informs the client about the vendor’s true cost structure. This reduces information asymmetry, if any, while deepening the trust and cooperation between the contracting partners (Gulati 1995). Learning accrued from previously completed projects for the same client can also reduce the uncertainty in the project for the vendor (Corts and Singh 2004). Therefore, for both the T&M and FP subsamples, the vendor’s preference for FP contracts will be dampened in repeat projects for the same client, all else being equal. Although the final chosen contract for the project is based on both the vendor’s and client’s preferences, empirical results in Kalnins and Mayer (2004) as well as Corts and Singh (2004) on the final chosen contract indicate a higher probability of T&M contracts in repeat interactions between contracting partners. Therefore we hypothesize.

Hypothesis 3. For both the T&M and FP subsamples, the (ex ante) profit expectation of the vendor is higher under the T&M contract relative to the FP contract for repeat projects with the same client, all else being equal.

Finally, we consider the issue of acquiring and retaining trained personnel for the project on the vendor’s contract preferences. Employee attrition is a serious issue in the Indian software industry, where, on average, firms lose 30% of their employees per year (Nidumolu and Goodman 1993, Ethiraj et al. 2005). Therefore, for projects in technologies or domains where there is considerable difficulty in acquiring or retaining trained personnel, the risks faced by the vendor are considerable. In addition, information about attrition in the Indian industry is easily available from the public domain, and therefore there are no information asymmetries in this respect. Employee turnover from teams is driven by the dynamics of the labor market and no efficient risk mitigation techniques can fully cover the vendor against these effects. In these circumstances, the ex ante risk protection provided by the T&M contract will dominate any possible rent-making from an FP contract. Hence we propose:

Hypothesis 4. For both the T&M and FP subsamples, the ex ante profit expectation of the vendor is higher under the T&M contract relative to the FP contract for projects with a higher risk of employee attrition, all else being equal.

## 3. Data Collection and Measurement

The data for this paper are the same data set used in Gopal et al. (2003). For the sake of brevity, we are not reproducing descriptions of the data collection process, which are available in Gopal et al. (2003). Briefly, the data were collected from a leading Indian offshore development firm. The sample consists of 55 FP and 38 T&M projects.<sup>4</sup> The projects were customized business systems using 4GL and client-server technologies. To maintain consistency with Gopal et al. (2003), we use the same variables in the contract choice probit equation. The variable descriptions are shown in Table 1 and summary statistics for the sample are shown in Table 2. Table 3 shows the summary statistics of the variables of interest in this paper, reported by contract type.

Table 1 Variable Descriptions

<table><tr><td>Variable name</td><td colspan="5">Measurement</td></tr><tr><td>Variable Size (Effort)</td><td colspan="5">Person-days. The correlation between effort and size is very high (Pressman 1992), and therefore the use of effort is acceptable</td></tr><tr><td>Requirements uncertainty</td><td colspan="5">Measured using four questionnaire items adapted from Barki et al. (1993)</td></tr><tr><td>Project type</td><td colspan="5">Categorical variable: development, reengineering, and maintenance</td></tr><tr><td>Human resources—Training</td><td colspan="5">Measured the availability of trained personnel for the project using three questionnaire items, adapted from Barki et al. (1993)</td></tr><tr><td>Client MIS experience</td><td colspan="5">Measured using four questionnaire items adapted from discussion in Lacity and Hirschheim (1993)</td></tr><tr><td>Client experience with outsourcing</td><td colspan="5">Measured the client&#x27;s past experience with outsourcing using two questionnaire items adapted from Lacity and Hirschheim (1993)</td></tr><tr><td>Project importance</td><td colspan="5">Measured using one questionnaire item on a 5-point Likert scale</td></tr><tr><td>Client reputation</td><td colspan="5">Measured using one questionnaire item on a 5-point Likert scale</td></tr><tr><td>Future business</td><td colspan="5">Measured using one questionnaire item on a 5-point Likert scale</td></tr><tr><td>Client size</td><td colspan="5">Measured as the number of employees in the whole client organization</td></tr><tr><td>Competition-client</td><td colspan="5">Presence of alternative development firms in the client country</td></tr><tr><td>Competition-vendor</td><td colspan="5">Presence of other competing development firms in India.</td></tr><tr><td>Number of prior projects</td><td colspan="5">Number of projects completed by the vendor for the same client</td></tr><tr><td>Contract type</td><td colspan="5">Contract type is binary: FP and T&amp;M</td></tr><tr><td>Employee turnover</td><td colspan="5">The impact of team member turnover during the duration of the project. Two questionnaire items</td></tr><tr><td>Duration</td><td colspan="5">Duration of the project in days, between start of the project and final sign off</td></tr><tr><td>Team size</td><td colspan="5">Number of personnel on project core team</td></tr></table>

<sup>Notes</sup>. N <sub>=</sub> 93. C.A.: Cronbach’s alpha, Var(1): % variance explained by first factor.

It is important to establish that our sample is reasonably representative of the offshore industry in India. The Indian software exports industry is heavily concentrated in a few firms, which have significant market power. NASSCOM, an Indian industry trade association reports that in 2000, 25 firms (0.8% of the firms in India) accounted for more than 60% of the software exports in India.<sup>5</sup> The top 10 firms account for more than 50% of the export business. A thorough analysis of one of these firms provides the researcher with representative coverage of more than 40% of the market. This concentration of market power in a few firms has not changed in the years because 2000. In 2005, the top five firms alone accounted for more than 31% of the software exports from India.<sup>6</sup>

Table 3 Summary Statistics for Profit Drivers by Contract Type

<table><tr><td>Subsample</td><td>Mean</td><td>Std. dev.</td><td>Minimum</td><td>Maximum</td></tr><tr><td colspan="5">FP, N = 55</td></tr><tr><td>Turnover</td><td>1.82</td><td>0.80</td><td>1.00</td><td>4.50</td></tr><tr><td>Duration</td><td>345.96</td><td>279.43</td><td>60.00</td><td>1,094.00</td></tr><tr><td>Effort</td><td>1,149.9</td><td>1,605.33</td><td>31</td><td>8,100</td></tr><tr><td>Team</td><td>10.20</td><td>9.80</td><td>3.00</td><td>50.00</td></tr><tr><td>Prior</td><td>10.72</td><td>15.97</td><td>0.00</td><td>75.00</td></tr><tr><td colspan="5">T&amp;M, N = 38</td></tr><tr><td>Turnover</td><td>2.01</td><td>0.80</td><td>1.00</td><td>4.00</td></tr><tr><td>Duration</td><td>371.70</td><td>309.36</td><td>27.00</td><td>1,320.00</td></tr><tr><td>Effort</td><td>754.48</td><td>784.54</td><td>31</td><td>3,100</td></tr><tr><td>Team</td><td>7.5</td><td>5.01</td><td>1.00</td><td>20.00</td></tr><tr><td>Prior</td><td>4.19</td><td>6.00</td><td>0.00</td><td>30.00</td></tr></table>

Our research site is one among the 10 top firms, though for confidentiality reasons, we cannot reveal its identity. The firm provides outsourcing services to offshore customers, similar to the ones described above. The vast majority of the systems developed during 1995–1999, which is roughly the time period for our data collection, were customized business systems using 4GL and client-server technologies. These projects form the bulk of our sample. The projects in our sample are also similar to the projects seen in current research in the Indian offshore industry (Banerjee and Duflo 2000, Ethiraj et al. 2005). Thus we believe that though our data comes from one firm, our sample of 93 projects is adequately representative of the offshore Indian industry.

Because our primary objective is to establish contract preferences formed ex ante, we maintain parsimony by considering the impact of a small set of profit drivers that have been shown to influence profitability in prior work (Gopal et al. 2003). We are constrained by the relatively small sample size in the subsamples. Therefore we choose profit drivers where there are clear links to profitability from past research. In addition, we choose variables that are either available to the vendor during contracting or can be reasonably assessed for making contracting decisions. Prior research also indicates that a relatively small set of key factors are used in contractual decision-making (Banerjee and Duflo 2000); our objective is to capture the relevant set of information in as parsimonious a manner as possible. Therefore we choose effort, duration, and team size, as these are important variables that have been studied in both the outsourcing and software development literature (Pressman 1992). In addition, estimates of these factors are used in decision making during the contracting stage (Banerjee and Duflo 2000). The impact of employee attrition on development teams has been discussed in past work (Nidumolu and Goodman 1993). Finally, prior experience with the client has been shown to influence vendor profitability (Ethiraj et al. 2005) and is an important factor in determining governance mechanisms in contracting situations (Gulati 1995, Corts and Singh 2004).<sup>7</sup> We provide a brief description of these drivers below.

(1) Duration of the project (Duration): The elapsed time in days between start and end of the project. Project duration is a significant risk factor; longer projects being riskier (Pressman 1992).

(2) Team Size (Team): The size of the core team of the project. The core team is instrumental in determining both project costs and team productivity (Banker et al. 1991).

(3) Employee turnover from the team (Turnover): High attrition rates in software development firms are common in the Indian software industry (Nidumolu and Goodman 1993). It is often difficult to measure the effects of attrition accurately because personnel occupy different levels of importance in a team. The loss of a project manager is more keenly felt than the loss of a programmer. Therefore, rather than using the number of members leaving the project team, we use two questionnaire items that were filled out by the project manager. The two items showed good reliability (Cronbach’s alpha 073) and loaded together on one factor in exploratory factor analysis.

(4) Number of prior projects completed for the client (Prior): Ethiraj et al. (2005) argue that prior experience with the same client enables the vendor to accrue valuable insight and learning into the client’s business processes. Thus the vendor’s capabilities are enhanced. Therefore, this should lead to greater profitability on projects, all else being equal.

(5) Effort in person-days (Effort)

Profitability on the project was extracted from the vendor’s databases and is calculated as the net of the revenues attributed to the project and the costs allocated to the project (in Indian rupees). The costs allocated to the project include some business unit overhead cost allocations as well as all direct costs such as personnel salaries, travel, telecommunication expenses, and administrative costs. Our measure of profitability at the project is an imperfect measure, as some corporate overheads may not be apportioned to individual projects; this is an accounting decision on the part of the vendor firm. Our profitability measures are, however, extracted from the same source that the firm uses in accounting decision making and represent the best and closest approximation to vendor surplus from a project.

## 4. Methodology

## 4.1. The Two-Regime Profit Model

This section describes the econometric model that we use in first establishing the presence of two contractual regimes, and subsequently analyzing vendor profit expectations across the two contractual regimes. A regime is simply the econometric equivalent of a particular management process as characterized by the marginal effects of chosen drivers on profitability. Previous work on contracts (Gopal et al. 2003, Ethiraj et al. 2005), which uses a binary contract variable constrains the analysis to a single regime. Such a specification can only help in assessing whether the average profit under a T&M contract will be different from that under an FP contract. In contrast, a two-regime specification allows us to test if the impact of profit drivers in a T&M regime is significantly different from an FP regime.

It is important to keep in mind that the contract choice is itself endogenous. In other words, the final contract choice is a function of ex ante expectations of profitability. In the presence of this endogeneity, ordinary least square (OLS) estimation of a profit regression with the contract type as an independent variable yields biased and inefficient estimates (Maddala 1983).<sup>8</sup> The endogeneity also affects our ability to estimate separate profit regimes for FP and T&M contracts. If the two contract types were randomly distributed in our sample, we could estimate two independent profit equations for the FP and T&M subsamples using OLS and directly compare marginal effects of profit drivers. However, because the contract is chosen based on expectations of risk and profitability, the two profit equations are not independent. Therefore we use a variant of the Heckman two-stage endogenous switching regression technique described below.

A test for the presence of two contractual regimes is akin to a test of the moderating influence of contract choice on the relationships between the profit drivers (independent variables) and profitability (dependent variable). The common approach of testing for moderation through the use of hierarchical regression and interaction terms (Baron and Kenny 1986) cannot be used in this case; the estimated coefficients will be biased and inconsistent because of the presence of endogeneity. The Heckman two-stage methodology we use, however, accounts for the endogeneity of contract choice (Nakosteen and Zimmer 1986).

We consider the following contract choice model:

$$
C ^ {*} = \gamma^ {\prime} Z _ {i} - \varepsilon_ {i},\tag{1}
$$

where $C ^ { * }$ is the latent variable representing the cumulative net preference for a contract type and $\gamma$ represents regression coefficients, $Z _ { i }$ are exogenous variables determining contract choice and $\varepsilon _ { i } \sim$ $N ( 0 , \sigma _ { \varepsilon } ^ { 2 } )$ . The latent variable $C ^ { * }$ is not observable. Instead, we observe the chosen contract C for a project. The observed contract choice is $C = 1 \ ( C ^ { * } \geq 0 )$ if an FP contract is chosen and $C = 0 \ ( C ^ { * } < 0 )$ if a

T&M contract is chosen. As in Heckman (1976), we use a probit regression specification to estimate Equation (1) in the first stage.

It is useful to view contract choice as a function of both the vendor’s and client’s preferences based on project parameters $Z _ { i } ,$ weighted by their respective bargaining powers (Svejnar 1986). The net effect of these bargaining powers is subsumed in the coefficients $\gamma . ^ { 9 }$ It is entirely possible that the vendor’s preference for a contract is different from the final contract chosen for the project. However, given a chosen contract for a project, the vendor’s profit equations in the two contract types are represented by the following equations:

$$
P _ {T} = \beta_ {T} ^ {\prime} X _ {T i} + U _ {T i} \quad \mathrm{if} C = 0 \mathrm{when} \varepsilon_ {i} \geq \gamma^ {\prime} Z _ {i}\tag{2}
$$

$$
P _ {F} = \beta_ {F} ^ {\prime} X _ {F i} + U _ {F i} \quad \mathrm{if} C = 1 \mathrm{when} \varepsilon_ {i} <   \gamma^ {\prime} Z _ {i},\tag{3}
$$

where $\beta _ { T } , \beta _ { F }$ are vectors of regression coefficients in the T&M and FP regimes, respectively, $X _ { T i }$ and $X _ { F i }$ represent profit drivers affecting profits in T&M and FP contracts and the error terms are distributed as follows: $U _ { T i } \sim N ( 0 , \sigma _ { T } ^ { 2 } )$ and $U _ { F i } \sim N ( 0 , \sigma _ { F } ^ { 2 } )$

If $\varepsilon _ { i }$ from the contract choice model were entirely uncorrelated with $( U _ { T i } , U _ { F i } )$ , Equations (2) and (3) can be estimated using OLS. However, given the endogeneity of contract choice, it is more realistic to assume that $\varepsilon _ { i }$ is correlated with $( U _ { T i } , U _ { F i } )$ . Therefore, consistent with Heckman (1976), we assume $\varepsilon _ { i } , ~ U _ { T } , ~ U _ { F }$ are trivariate normally distributed with $C O V ( \varepsilon _ { i } , U _ { T } ) = \sigma _ { \varepsilon T }$ and $C O V ( \varepsilon _ { i } , U _ { F } ) = \sigma _ { \varepsilon F }$ (Nakosteen and Zimmer 1986, Shehata 1991).<sup>10</sup> The following appropriate equations to be estimated for the tworegime case are (Maddala 1983):

$$
P _ {F} = \beta_ {F} ^ {\prime} X _ {F i} + \sigma_ {\varepsilon F} \lambda_ {F i} + V _ {F i}\tag{4}
$$

$$
P _ {T} = \beta_ {T} ^ {\prime} X _ {T i} + \sigma_ {\varepsilon T} \lambda_ {T i} + V _ {T i},\tag{5}
$$

where $X _ { F i }$ and $X _ { T i }$ are the profit drivers (independent variables) in the FP and T&M subsamples respectively, $\lambda _ { F i } = - [ \phi ( \gamma ^ { \prime } Z _ { i } ) / \Phi ( \gamma ^ { \prime } Z _ { i } ) ] , \lambda _ { T i } = [ \phi ( \gamma ^ { \prime } Z _ { i } ) / 1 -$ $\Phi ( \gamma ^ { \prime } Z _ { i } ) ] .$ , and $V _ { T i } , \ V _ { F i }$ are random error terms with zero expectations. Equations (4) and (5) are corrected for endogeneity from contract choice and can be estimated using OLS to obtain unbiased coefficients (Heckman 1976). The  terms are the “inverse Mills ratios,” and are calculated using parameters from the probit model estimated in the first stage. The coefficients of the  terms capture estimates of the covariance between the error terms in the contract choice equation and the profit equations.

Our primary research question is to evaluate whether the vendor prefers the FP contract over the T&M contract for any subset of projects and if so, which projects. To perform this analysis and provide tests for Hypotheses 1—4, we use the program evaluation methodology described in the next section. While Proposition 1 asserts the existence of two distinct contractual regimes, we perform a formal test to validate it as a matter of statistical rigor. This test is described in the appendix.

## 4.2. Program Evaluation Methodology

The program evaluation methodology (Maddala 1983) concerns the evaluation of the benefits to an individual from attending one kind of a program versus another (e.g., from attending a social intervention versus no intervention). Accordingly, an important aspect of the methodology is to evaluate the ex ante suitability or efficacy of a program. To do this, Maddala (1983) recommends computing the predicted value of the dependent variable (profit) under the alternative regime. By comparing the expected profit in a given project from both contractual regimes, we can effectively evaluate the vendor’s preferences for contract type in a given project.

Recall that Equations (4) and (5) refer to the endogeneity-corrected profit equations for the FP and T&M regimes respectively. The ex ante profit expectations in the FP and T&M regimes, can thus be calculated through the estimated coefficients $\beta _ { F }$ and $\beta _ { T }$ as follows:

$$
E (P _ {F P}) = \beta_ {F} ^ {\prime} X _ {F i} + \sigma_ {\varepsilon F} \lambda_ {F i},
$$

$$
E (P _ {T M}) = \beta_ {T} ^ {\prime} X _ {T i} + \sigma_ {\varepsilon T} \lambda_ {T i},\tag{6}
$$

(7)

where $E ( P _ { F P } )$ and $E ( P _ { T M } )$ are expected profits in the FP and T&M regimes, respectively.

In addition, we also estimate the expected profit for the project under the alternative contractual regime as suggested by Maddala (1983). Specifically, we estimate the expected profit for all FP projects in the T&M regime and vice versa as follows:

$$
E (P _ {F P} \mid T M) = \beta_ {F} ^ {\prime} X _ {T i} + \sigma_ {\varepsilon F} \lambda_ {T i},\tag{8}
$$

$$
E (P _ {T M} \mid F P) = \beta_ {T} ^ {\prime} X _ {F i} + \sigma_ {\varepsilon T} \lambda_ {F i}.\tag{9}
$$

Equation (8) provides expected profit for a T&M project if the project had been completed under an FP regime. Similarly, Equation (9) provides expected profit for an FP project if the project had been completed under a T&M regime.

We can then define

$$
\Delta_ {F P} = E (P _ {F P}) - \big (E (P _ {T M} \mid F P) \big),\tag{10}
$$

$$
\Delta_ {T M} = E (P _ {T M}) - \left(E (P _ {F P} \mid T M)\right)\tag{11}
$$

where $\Delta _ { F P } ( \Delta _ { T M } )$ captures the difference between ex ante expected profits on an actual FP (T&M) project and the ex ante expected profits if the same project had been completed in a T&M (FP) regime. Thus $\Delta _ { F P }$ and $\Delta _ { T M }$ pertain to two mutually exclusive and collectively exhaustive sets of projects.<sup>11</sup> The  terms, being the ex ante difference in profitability between the contract types, provides us with a measure of the vendor’s preference for one contract type over the other and enables testing Hypotheses 1—4. This econometric framework also allows us to rigorously evaluate the extent to which the vendor is able to self-select into a contractual regime. We describe these results in detail in the next section.

## 5. Analysis and Results

We estimate the probit regression for the contract choice (reduced form of Equation (1)) consistent with the contract choice model in Gopal et al. (2003). The results from this estimation are reproduced in Table 4 for convenience.

Table 4 Probit Analysis Results

<table><tr><td>Variable</td><td>Coefficient</td><td>Std. error</td><td>Pr &gt; Chi-sq</td></tr><tr><td>Requirements uncertainty</td><td>-0.90</td><td>0.32</td><td>0.005</td></tr><tr><td>Effort</td><td>-0.42</td><td>0.22</td><td>0.05</td></tr><tr><td>Human resources—Training</td><td>-0.90</td><td>0.28</td><td>0.001</td></tr><tr><td>MIS experience</td><td>0.80</td><td>0.31</td><td>0.01</td></tr><tr><td>Client experience</td><td>0.22</td><td>0.21</td><td>0.28</td></tr><tr><td>Client reputation</td><td>0.05</td><td>0.16</td><td>0.73</td></tr><tr><td>Future business</td><td>0.30</td><td>0.19</td><td>0.11</td></tr><tr><td>Client size</td><td>0.59</td><td>0.26</td><td>0.02</td></tr><tr><td>Project importance</td><td>-0.58</td><td>0.27</td><td>0.03</td></tr><tr><td>Competition (vendor)</td><td>-1.37</td><td>0.34</td><td>0.0001</td></tr><tr><td>Competition (client)</td><td>0.83</td><td>0.32</td><td>0.009</td></tr><tr><td>Number of prior projects</td><td>-0.08</td><td>0.02</td><td>0.001</td></tr><tr><td>Project type</td><td>-0.80</td><td>0.36</td><td>0.02</td></tr></table>

2 log L 60594, model fit 39615 with 13 DF, significant at p 00002. Association of predicted probabilities and observed responses 902%.  
<sup>Notes</sup>. 0—T&M, 1—FP, N 93.

The predictive power of the probit contract choice model reported in Gopal et al. (2003) is high; over 90% of the projects in the sample are correctly categorized into FP and T&M contracts by the model. The contract choice model therefore provides us with an adequate control for endogeneity arising from contract choice.

## 5.1. Characteristics of FP and T&M Regimes

We calculate the appropriate inverse Mills ratios and estimate Equations (4) and (5) in the following multiple regression forms:

$$
\mathrm{Profit} _ {T M} = f (\text {Constant}, \text {Turnover}, \text {Duration}, \text {Team},
$$

$$
\text { Effort,   Prior, } \lambda_ {T i}) + V _ {T i},\tag{12}
$$

$$
\text { Profit } _ {F P} = f (\text { Constant }, \text { Turnover }, \text { Duration }, \text { Team },
$$

$$
\mathrm{Effort,Prior,} \lambda_ {F i}) + V _ {F i}.\tag{13}
$$

The results for the two equations are shown in Table 5. As a means of comparison, we also estimate the above equations without the correction for endogeneity. As indicated by Shaver (1998), it is often useful to present the uncorrected results as a robustness check. The uncorrected OLS results are shown in the first columns under each contractual regime in Table 5, while estimates from Equations (12) and (13) are shown in the second columns. Although correcting for endogeneity does not radically change the magnitude of the coefficient estimates, the significance of the obtained coefficients improves markedly. This allows us to make stronger statements about the different marginal effects of the profit drivers on profit in the two contractual regimes.

Table 5 Results from the Two-Stage Heckman (1976) Procedure

<table><tr><td rowspan="2">Variables</td><td colspan="2">Profit equation-Fixed price contracts</td><td colspan="2">Profit equation-time and materials contracts</td></tr><tr><td>OLS coefficients</td><td>Endogeneity-corrected coefficients</td><td>OLS coefficients</td><td>Endogeneity-corrected coefficients</td></tr><tr><td>Constant</td><td>289.65(204.86)</td><td>142.55(205.15)</td><td>105.13(72.55)</td><td>108.59(70.99)</td></tr><tr><td>Turnover</td><td>-202.50**(80.42)</td><td>-220.68***(77.95)</td><td>-47.99(27.86)</td><td>-57.09**(28.66)</td></tr><tr><td>Duration</td><td>0.546**(0.251)</td><td>0.434*(0.24)</td><td>0.140*(0.085)</td><td>0.153**(0.081)</td></tr><tr><td>Team</td><td>12.67*(6.55)</td><td>14.73**(6.27)</td><td>10.29*(4.76)</td><td>10.69**(4.62)</td></tr><tr><td>Effort</td><td>319.07***(61.53)</td><td>354.36***(64.02)</td><td>152.81**(43.32)</td><td>154.39***(42.09)</td></tr><tr><td>Prior</td><td>0.53(3.90)</td><td>0.7(4.27)</td><td>-2.58(3.64)</td><td>-2.50(3.55)</td></tr><tr><td>Lambda</td><td></td><td>-424.26***(158.94)</td><td></td><td>5.25(46.22)</td></tr><tr><td>N</td><td>55</td><td>55</td><td>38</td><td>38</td></tr><tr><td> $R^2$ </td><td>0.63</td><td>0.67</td><td>0.56</td><td>0.56</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.59</td><td>0.63</td><td>0.5</td><td>0.49</td></tr><tr><td>F-statistic</td><td>18.09***</td><td>16.97***</td><td>8.84***</td><td>6.80***</td></tr></table>

<sup>Note</sup>. Standard errors in parenthesis.  
∗p < 0 10 ∗∗p < 005 ∗∗∗p < 001

The results in Table 5 clearly show the differential impacts of the profit drivers on project profitability in the two regimes. Given that the FP contract exposes the vendor to greater risk, we see evidence for the actual materialization of these risks. Employee turnover on projects reduces profits in FP contracts, all else being equal. Replacing personnel on FP contracts adds to project costs for the same revenue, thereby reducing profits. Although employee turnover from a T&M project affects profits negatively, the overall impact is much smaller. The impact of turnover is almost four times as much in FP contracts as in T&M contracts, all else being equal.

The impact of team size and effort on profit is significantly larger for FP contracts than for T&M contracts. This is interesting because the period between 1995 and 2000 saw more Indian companies move from low-tech maintenance-oriented projects to more risky, end-to-end development projects [NASSCOM, 2000 Software Directory]. Therefore, for Indian firms, the added risks inherent in high-end development work could have potentially higher payoff in contracts with stronger incentives, i.e., FP contracts. In such situations, it is optimal for the vendor to strategically assign his most valuable resources to FP contracts, as argued earlier. In other words, the vendor would assign his most experienced developers, systems analysts, designers, and testers to FP contracts rather than T&M contracts because his potential payoff is higher in these contracts. As a result, the marginal contribution to profitability from effort and team size is higher under FP contracts than under T&M contracts. Our analysis indirectly speaks to the importance of these resources and their limited supply in the offshore domain (Bharadwaj 2000). However, the negative impact of risk is also substantially higher in FP contracts than in T&M contracts, implying the need for superior project management and execution in the offshore domain.

A similar effect appears to be driving the results for project duration. Longer projects, all else being equal, are riskier because longer cycle times in the IT domain could lead to greater technological risk, requirements instability, and business transformations (Gopal et al. 2003). The vendor’s marginal payoff from longer (hence, riskier) projects is higher in FP contracts than in T&M contracts. This is expected because profitability is built into the billing rate per unit of effort under T&M contracts. However, under FP contracts, the vendor’s costs are based on project duration in terms of personnel salaries. Therefore he has an incentive to reduce duration, all else equal. However, our results show that the revenue generated by an additional day on an FP project is still higher than the cost of personnel. One possible explanation for this effect is that under FP contracts, the vendor ensures efficient project management and resource utilization. Therefore, better management of these projects indicates that for each additional day on the project, revenues outweigh the incurred costs. This net positive effect is significantly higher in FP than in T&M contracts.

Our discussions with offshore project managers both at the research site and at other firms, revealed another possible explanation for these findings. Because the FP contract provides the vendor with more flexibility in managing the development process (Banerjee and Duflo 2000), it is often not necessary for an experienced programmer or project leader to be assigned to the project throughout the duration of the project. It is possible that experienced personnel are assigned to multiple projects over the time period of a project in our sample, thereby increasing the revenues for the vendor while holding costs constant. The vendor is thus able to leverage experienced personnel by not only assigning them to FP projects, but also shuffling them quickly from one FP project to another or keeping them on multiple projects concurrently. Project managers at the research site indicated that this was possibly one reason why experienced and competent software professionals were at a premium in the offshore industry (Shah 2004). However, note that this strategy in FP contracts would only work if the clients were not aware of how exactly the project was being executed at the vendor site. In other words, some information asymmetry is required between the clients and the vendor. This strategy is not directly applicable in T&M projects because the client is billed for services performed during the billing period, and therefore requires staff dedicated to a project on a sustained basis (Arora and Asundi 1999).

Prior experience with the client does not seem to have a significant impact in our analysis. Although it is possible that prior experience leads to capability building at the vendor site (Ethiraj et al. 2005) and learning, we do not see any systematic effect. A potential limitation in our analysis is the small sample size. The FP subsample has 55 projects, which is a reasonable sample size compared to prior research in software development. However, the T&M subsample has 38 projects. It is possible that potentially significant relationships do not achieve statistical significance because of the small sample size. Our results, with respect to prior experience, have to be evaluated accordingly.

## 5.2. Evaluation of Vendor Preference for Contract

Because the proposed hypotheses pertain to subsample analysis to evaluate vendor preferences, we focus on the distributions of the  terms within the FP and T&M subsamples, calculated as per Equations (10) and (11). Consider the $\Delta _ { T M }$ terms first. The $\Delta _ { T M }$ terms capture the difference in ex ante profitability between the T&M contract and the FP contract, had the FP contact been chosen for the project. The mean value of $\Delta _ { T M }$ is 378,000.00 and the standard deviation is $2 7 0 { , } 0 0 0$ . The minimum value for $\Delta _ { T M }$ is $^ { 4 , 4 3 4 , }$ while the maximum is 959,428. There are two striking aspects to the distribution of $\Delta _ { T M } .$ . First, the mean value of $\Delta _ { T M }$ informs us about the extent to which the vendor is able to self-select into the T&M regime. Because the $\Delta _ { T M }$ terms are all positive, it appears that in each project where the T&M contract was chosen, the vendor would have done worse in an FP contract. In other words, there is congruence between the contract type the vendor prefers for the project and the final chosen contract for that project. Therefore the distribution of the $\Delta _ { T M }$ terms indicates that the vendor is either able to self-select into a T&M contract for these projects or is able to negotiate with the client and jointly choose the T&M contract. It is also possible that the client drives the choice of a T&M contract, as some scholars have pointed out (Kalnins and Mayer 2004, Ethiraj et al. 2005) for institutional reasons.<sup>12</sup> However, note that none of these projects would have provided the vendor with higher ex ante profitability under the FP regime. Therefore, though client mandate is a possible reason for choosing the T&M contract, the vendor’s preferences also point to the T&M contract for these projects.

The second point to note is that because the T&M contract provides the vendor with greater risk protection and the $\Delta _ { T M }$ terms are uniformly positive, it appears that the primary criterion for choice of T&M contract is risk protection. The $\Delta _ { T M }$ terms therefore provide support for Hypothesis 1, which indicates that for all these projects, the ex ante profitability is higher for the T&M contract than for the FP contract. Because there are fewer significant information rents that can be leveraged by the vendor within a T&M contract, the risk protection is the primary benefit from this contact type.

Turning to the $\Delta _ { F P }$ terms within the FP subsample, we see strikingly different results. The mean value of $\Delta _ { F P } \mathrm { i s } - 9 7 , 0 0 0$ , while the standard deviation is 309,000. The maximum value is 1,410,000, while the minimum value is −508,000. More important, 22 of the 55 projects show a negative $\Delta _ { F P } ,$ while the remaining show a positive $\Delta _ { F P }$ . Clearly, unlike the $\Delta _ { T M }$ case, there is some diversity in the vendor’s ex ante preference for projects based on some project parameters. From the negative mean value of $\Delta _ { F P } ,$ it is clear that the vendor is not able to self-select into the FP contract (or self-select out of the FP contract). However, to explore this result more, we calculate correlations between the $\Delta _ { F P }$ terms and the five project-level factors, as shown in the second and fourth columns of Table 6. These results are also shown graphically in Figure 1. In addition, to account for simultaneous effects that may not be apparent in univariate correlations, we estimate a simple analysis of variance (ANOVA) between the $\Delta _ { F P }$ terms and the project factors, also shown in the third and fifth columns of Table 6.

Table 6 Correlations and ANOVA Results of Project Factors on Deltas

<table><tr><td></td><td>Correlations(FP projects)</td><td>Dependentvariable = Delta (FP)</td><td>Correlations(T&amp;M projects)</td><td>Dependentvariable = Delta (T&amp;M)</td></tr><tr><td>Constant</td><td></td><td>170.57***(62.92)</td><td></td><td>163.9(112.29)</td></tr><tr><td>Effort</td><td>0.753***</td><td>164.84***(21.81)</td><td>-0.285*</td><td>-106.03*(58.70)</td></tr><tr><td>Duration</td><td>0.707***</td><td>0.414***(0.09)</td><td>-0.337*</td><td>-0.257**(0.12)</td></tr><tr><td>Team</td><td>0.33*</td><td>2.50(2.29)</td><td>-0.330*</td><td>-13.94**(7.03)</td></tr><tr><td>Turnover</td><td>-0.088**</td><td>-142.95***(27.01)</td><td>0.421**</td><td>219.49***(46.06)</td></tr><tr><td>Prior</td><td>0.023</td><td>-1.30(1.27)</td><td>-0.195</td><td>-6.14(9.92)</td></tr><tr><td>N</td><td>55</td><td>55</td><td>38</td><td>38</td></tr><tr><td> $R^2$ </td><td></td><td>0.73</td><td></td><td>0.44</td></tr><tr><td>F-statistic</td><td></td><td>39.13***</td><td></td><td>6.99***</td></tr></table>

<sup>Notes.</sup> Standard errors in parenthesis.  
<sup>∗</sup> p < 010, <sup>∗∗</sup> p < 005, <sup>∗∗∗</sup> p < 001.

The correlations and ANOVA coefficients in the FP subsample show that as effort and duration increase, the value of $\Delta _ { F P }$ increases. In other words, for larger and longer projects, the ex ante profit difference between the FP contract and alternative (T&M) contract increases. In addition, the correlation between team size and $\Delta _ { F P }$ is also positive. Thus, Hypotheses 2 is also supported. Specifically, the greater the ex ante risk in the project, the greater is the benefit from information rents that accrue to the vendor through the FP contract.

To test Hypotheses 3 and 4, we again refer back to Table 6, where the correlations and ANOVA coefficients between the  terms and the profit drivers are shown for both the FP and T&M subsamples. Hypothesis 3 is not statistically supported in either subsample. The correlations as well as the ANOVA coefficients between the  terms and prior interactions with the client show no significant relationship. However, we see support for Hypothesis 4 across both subsamples. In the FP subsample, as the risk of turnover increases in the project, the vendor’s ex ante preference for the FP contract reduces $( r = - 0 . 0 8 8 , p <$ 005). Similarly, in the T&M subsample, as the risk of turnover increases, the vendor’s preference for a T&M contract increases significantly $( r = 0 . 4 2 1 , p < 0 . 0 5 )$

Although we had not postulated any hypotheses about the variation of the $\Delta _ { T M }$ terms, the results pertaining to the $\Delta _ { T M }$ terms in Table 6 provide some interesting insights. As the risk in the project increases, (i.e., larger and longer projects with larger team sizes), the vendor’s relative advantage in a T&M contract tends to reduce. Although all the $\Delta _ { T M }$ terms are uniformly positive, it appears that for larger and longer durations, the risk protection accorded by the T&M contract might reduce in value for the vendor. It is possible, therefore, that when this result is combined with the results from the FP subsample, it appears that larger and longer projects provide greater information rents for the vendor in the FP regime than the T&M regime. This result is strongly significant for the FP subsample and weakly significant in the T&M subsample. However, more work is required to clearly establish these results and represents an avenue for future research.

To summarize, prior research has indicated that offshore vendors should prefer T&M contracts because they provide higher ex post profitability, all else being equal (Gopal et al. 2003, Ethiraj et al. 2005). This was postulated to emerge from the risk protection provided by the T&M contract. However, it may not follow that risk protection is the only driving force in forming the vendor’s preferences. The analysis presented here shows that in some cases, the vendor will prefer the FP contract because the information rents available from the FP contract provide greater value than risk protection. In projects characterized by large size, longer duration, and large team sizes, the vendor’s preference for FP contracts, based on ex ante profit expectations, is higher than the risk protection benefits from the T&M contract. The program evaluation methodology allows us to tease out the how the vendor’s preferences might be modified by project characteristics such as project size, staffing, and prior client interactions, leading to a more nuanced understanding of contract preferences.

Figure 1 Graphs of  versus Effort, Duration, Team Size, and Attribution  
![](/api/attachments/9G3HF87T/fulltext/images/cb42266ad8b32790a9682f71cdfe9620a3c839c88789f6d82369e4b48d87a2fc.jpg)

![](/api/attachments/9G3HF87T/fulltext/images/dff3b21231e8bb12c8b91353200bc866d7977c66a2c340a4af0b1ccfb76922b4.jpg)

![](/api/attachments/9G3HF87T/fulltext/images/e1544860519e8015ac809471754fb7ca0c930c941b0d882102d5609c301eb58f.jpg)

![](/api/attachments/9G3HF87T/fulltext/images/0fa385cc73e98d8db24c87c4bca09480bc1bbb1cf544f75055feaa8c06de07a9.jpg)

![](/api/attachments/9G3HF87T/fulltext/images/7da32e434b864c8f8daba51bdd81b6f7432067c6c4f71fa1daa7ec8d962d8ab0.jpg)

![](/api/attachments/9G3HF87T/fulltext/images/bcfb25023a1be9d0474b3b176ed8c2552c2bd76798a594a4c6fafaf886359be3.jpg)

![](/api/attachments/9G3HF87T/fulltext/images/be4756b9b95e3590b428c7fafff4af5cf586067d355d29067a92ff52b0f514f6.jpg)

(h)  
![](/api/attachments/9G3HF87T/fulltext/images/c0f70ae221d7fd9fb24e4807c48215cf423645c7cca64a7eca4ac329c38ec9f2.jpg)  
Notes. The Delta terms are in Indian Rupees and represent the difference in ex ante profit between the chosen contract and the alternative contract type. Team size in number of core team members, effort in total person-days on the project and duration in number of days on the project. Attrition measured by a 1–5 Likert scale

## 6. Conclusion

We draw our motivation for this work from Gopal et al. (2003), which showed that vendors, on average, realize higher profits from T&M contracts relative to FP contracts. We investigate whether the relative impacts of known profit drivers in the offshore software development context are different across T&M and FP contracts, i.e., whether these are two distinct contract regimes. Prior work in offshore outsourcing (Ethiraj et al. 2005) as well as anecdotal evidence (Arora and Asundi 1999) suggests that offshore vendors would manage FP and T&M projects differently because of the risk perceptions, incentives, and resource constraints inherent in the software outsourcing context. Our tests, based on a variant of the Heckman two-stage procedure, show that this is indeed true.

More important, the second question that we address is whether vendors would unconditionally prefer T&M contracts for all projects, as one may infer from previous research on contract choice models (Gopal et al. 2003, Kalnins and Mayer 2004). Our results suggest that vendor’s expected profits would, in fact, be higher under FP contracts than under T&M contracts for riskier projects with longer durations and larger teams. Our analysis also indicates that the vendors do not always get the contract type they want, i.e., the vendor cannot freely self-select into the preferred contract type. In certain cases, the final contract chosen is clearly not what would have resulted in higher ex ante profit for the vendor. We see this in the FP subsample, wherein the vendor’s ex ante profits were higher in the T&M contract. Thus the use of the Heckman procedure for endogenous project choice is vital in establishing the presence of the two contractual regimes.

There are several managerial implications that arise from the results in this paper. Although T&M contracts provide risk protection, offshore vendors would prefer (and should consider) FP contracts for larger and longer projects with larger teams. These projects tend to provide the vendor with higher ex ante profitability. As the Indian industry matures from smaller low-risk projects to riskier high-end systems development (Shah 2004), vendors will likely prefer to carry their own risk at significant premia based on their capabilities. Capabilities in this context include significant project and process management skills in the vendor organization to manage the risks inherent in offshoring. Our analysis supports the assertion made by Ethiraj et al. (2005) that FP contracts will provide vendors with greater profitability. Our results, however, point to two caveats—this assertion appears to be true for large projects with large teams and is true for vendors who have the capabilities and/or the experience to leverage their private information and extract rents. Without the benefits of private information, the contracting process would tend to nullify the differences in expected profitability between the FP and T&M contracts for the vendor, i.e., the client would be able to bargain project parameters based on common information such that any rent-making would be reduced significantly.

Along the same lines, we observe that factors that do not provide the vendor with any private information or indeed, reduce the level of private information tend to increase the vendor’s preference for T&M contracts. The extent to which attrition hampers the project is out of the vendor’s control to some degree and also provides no benefit from information asymmetry. Similarly, repeat projects with the same client provide the client with a more accurate idea of the vendor’s abilities. Both these factors are associated with an increasing preference for T&M contracts because risk protection overwhelms any rent-making for the vendor.

The analysis presented in the paper is subject to a few caveats. First, we do not explicitly measure information asymmetry. Future research is required to quantify the impact of asymmetry by using more direct measures. Second, it is conceivable that the profit drivers we study, such as duration and team size, are themselves endogenously determined. We assume that these variables are exogenous, as does most extant research in software development teams. However, this assumption could lead to some bias in the coefficients of the profit drivers in the two contract regimes. Third, we do not allow for a “mixed” or “hybrid” contract where the contract terms might be endogenously determined for the project. This is because of the dominance of the two contract types observed in the data and in the offshore domain. However, the switching regression framework can easily be extended to such hybrid contracts that combine aspects of FP and T&M contracts. As long as it can be assumed that such a hybrid contract provides the vendor with a combination of risk protection and information rents under some monotonic conditions, our primary hypotheses would still hold. Casual evidence suggests that such contractual forms are also evolving (such as the incentive-based contracts and mixed contracts, which include aspects of both FP and T&M contracts). Further research is needed to understand these forms. Finally, we have analyzed a relatively small sample, but this is not uncommon in extant research in the offshore outsourcing domain.

While our analysis provides some indications of contract preferences in offshore projects, more research is required in the offshore domain to clearly establish the relationship between contract preferences and profitability. The trade-off between risk protection and information asymmetry at the time of contracting has not been explicitly addressed in the extant literature on software contracts, which has focused mostly on the influence of risk. In addition, while we focus on a set of project-level variables that address risk in the offshoring domain, other factors such as cultural differences between client and vendor organizations could also influence vendor preferences over contracts. Finally, it is highly likely that client preferences for contracts are also relatively finegrained over risk and information asymmetry as vendor preferences have seen in this analysis. These represent significant gaps in our understanding of how contracts affect profitability; our work thus points to the need for more empirical work in addressing these gaps in the literature.

## Acknowledgments

The authors thank three anonymous reviewers, Ritu Agarwal, M. S. Krishnan, Tridas Mukhopadhyay, V. Sambamurthy, and Sandra Slaughter for many helpful comments. The first author received generous support from the Carnegie Bosch Institute for International Management at Carnegie Mellon University.

## Appendix

In this appendix, we present a rigorous test of our proposition that there exist two distinct FP and T&M contractual regimes in the offshore outsourcing model (Proposition 1). A regime is characterized by significantly different marginal effects of the independent variables on the dependent variable.

Under the probit regression estimation of the contract choice Equation (1), the probability of choosing an FP (C = 1) contract for any given project is given by the probability that $\pmb { \varepsilon } _ { i } < \gamma ^ { \prime } Z _ { i }$ . With normally distributed error terms, this probability is

$$
\operatorname{Prob} (\text { FP   chosen }) \equiv \operatorname * {P r} (C = 1) = \Phi (\gamma^ {\prime} Z _ {i}),\tag{14}
$$

where 	  standard normal cumulative distribution function. Similarly, the probability of choosing a T&M contract is

$$
\operatorname{Prob} (\mathrm{T} \& \mathrm{M} \text { chosen }) \equiv \operatorname * {P r} (C = 0) = 1 - \Phi (\gamma^ {\prime} Z _ {i}).\tag{15}
$$

Because all projects in the sample are either FP or T&M, we can derive the expected profit E(P) for any given project as:

$$
E (P) = E (P \mid C = 1). \operatorname * {P r} (C = 1) + E (P \mid C = 0). \operatorname * {P r} (C = 0).\tag{16}
$$

We can substitute Equations (2), (3), (14), and (15) into Equation (16) to derive the following expected profit equation (for detailed derivation, see Maddala 1983, pp. 226–227):

$$
\begin{array}{r l} & E (P) = \beta_ {T} ^ {\prime} X _ {i}. \Phi (\gamma^ {\prime} Z _ {i}) + \beta_ {F} ^ {\prime} X _ {i}. [ 1 - \Phi (\gamma^ {\prime} Z _ {i}) ] \\ & \qquad + \phi (\gamma^ {\prime} Z _ {i}) [ \sigma_ {\varepsilon F} - \sigma_ {\varepsilon T} ], \end{array}\tag{17}
$$

where 	  standard normal density function. In our case, the exogenous variables affecting profits are the same in both regimes $( X _ { i } )$ , and so we can combine the first two terms in the right-hand side in (7). Because we would like to empirically test for the validity of the two-regime model first, this implies a test for whether $\beta _ { T } = \beta _ { F }$ in Equation (17). We can therefore rewrite (17) as follows:

$$
E (P) = \beta_ {F} ^ {\prime} X _ {i} + (\beta_ {T} - \beta_ {F}) X _ {i} \Phi (\gamma^ {\prime} Z _ {i}) + \phi (\gamma^ {\prime} Z _ {i}) [ \sigma_ {\varepsilon F} - \sigma_ {\varepsilon T} ].\tag{18}
$$

The reduced form for the above equation is

$$
E (P) = \beta_ {F} ^ {\prime} X _ {i} + \theta_ {1} X _ {i} \Phi (\gamma^ {\prime} Z _ {i}) + \theta_ {2} \phi (\gamma^ {\prime} Z _ {i}),\tag{19}
$$

where $\theta _ { 1 } = ( \beta _ { T } - \beta _ { F } )$ and $\theta _ { 2 } = [ \sigma _ { \varepsilon F } - \sigma _ { \varepsilon T } ] .$

Therefore, an appropriate test for the two-regime case is to test whether $\theta _ { 1 } ,$ the estimated coefficient vector on the interaction terms $X _ { i } \Phi ( \gamma ^ { \prime } Z _ { i } )$ in (19) equals 0. If $\theta _ { 1 } \neq 0 ,$ , we can then reject the null of a single contractual regime, and conclude that the two contractual regimes are distinct and separable. This test rigorously establishes that the contractual regimes representing FP and T&M contracts can be separated out, as shown in Equations (4) and (5).

We perform this test using data collected on 93 software development projects from an offshore software vendor located in India. For a description of the variables, refer to §3. The results are shown in Table 7. The null hypothesis is that of a single contractual regime, whereas we argued for the presence of two distinct contractual regimes. The joint test that the coefficients of interaction terms equal zero $( \theta _ { 1 } =$ 0 is rejected at conventional levels of significance, as seen from the F -statistic in Table A.1 $( F _ { 5 , 8 6 } = 6 \bar { . } 5 8 , p < 0 . 0 1 )$ , indicating that there are two distinct two regimes—one for FP contracts and the other for T&M contracts. In addition, we also perform the Chow’s test on the individual profit driver coefficients obtained from the regressions in FP and T&M subsamples, shown in Table 5. The Chow’s test is used to test if coefficients from different regressions are statistically

R<sup>2</sup> <sub>=</sub> 0727

Table 7 OLS Estimation of Equation (19), Dependent Variable: Profit

<table><tr><td>Variable</td><td>Coefficient</td><td>p-value</td></tr><tr><td>Constant</td><td>219.29*</td><td>0.08</td></tr><tr><td></td><td>(124.13)</td><td></td></tr><tr><td>Turnover</td><td>-126.57**</td><td>0.03</td></tr><tr><td></td><td>(60.53)</td><td></td></tr><tr><td>Duration</td><td>0.59***</td><td>0.007</td></tr><tr><td></td><td>(0.216)</td><td></td></tr><tr><td>Team</td><td>-4.05</td><td>0.52</td></tr><tr><td></td><td>(6.33)</td><td></td></tr><tr><td>Effort</td><td>216.41***</td><td>0.00</td></tr><tr><td></td><td>(48.16)</td><td></td></tr><tr><td>Prior</td><td>-1.69</td><td>0.56</td></tr><tr><td></td><td>(2.94)</td><td></td></tr><tr><td>Turnover × φ</td><td>43.13</td><td>0.68</td></tr><tr><td></td><td>(104.5)</td><td></td></tr><tr><td>Duration × φ</td><td>-0.91**</td><td>0.02</td></tr><tr><td></td><td>(0.38)</td><td></td></tr><tr><td>Team × φ</td><td>42.13***</td><td>0.006</td></tr><tr><td></td><td>(14.91)</td><td></td></tr><tr><td>Effort × φ</td><td>438.9***</td><td>0.001</td></tr><tr><td></td><td>(130.58)</td><td></td></tr><tr><td>Prior × φ</td><td>-1.06</td><td>0.93</td></tr><tr><td></td><td>(13.95)</td><td></td></tr><tr><td>φ</td><td>120.95</td><td>0.62</td></tr><tr><td></td><td>(246.9)</td><td></td></tr></table>

Adjusted R<sup>2</sup> <sub>=</sub> 069  
Model F statistic—F 11 81 1966 p < 0001  
Test of restrictions for interaction terms $( \theta _ { 1 } = 0 ) \colon$  
F 5 81 <sub>=</sub> 6581, $p < 0 . 0 0 1$  
<sup>Reject</sup> the null of a single regime in the profitability model  
<sup>Notes.</sup> Standard errors in parenthesis. <sup>∗</sup> p < 010, <sup>∗∗</sup> p < 005, <sup>∗∗∗</sup> p < 001. N 93.

dissimilar. The coefficients for Duration, Team and Effort in the FP regime are statistically different $( p < 0 . 1 0 )$ from the coefficients in the T&M regime. These results mirror the results shown in Table 7.

## References

Akerlof, G. 1970. The market for “Lemons”: Qualitative uncertainty and the market mechanism. Quart. J. Econom. 84(3) 488–500.

Allen, D., D. Lueck. 1992. Contract choice in modern agriculture: Cash-rent versus cropshare. J. Law Econom. 35(2) 397–426.

Allen, D., D. Lueck. 1995. Risk preferences and the economics of contracts. Amer. Econom. Rev. 85(2) 447–451.

Allen, D., D. Lueck. 1999. The role of risk in contract choice. J. Law, Econom. Organ. 15(3) 704–736.

Arora, A., J. Asundi. 1999. Quality certification and the economics of contract software development: A study of the Indian software service companies. NBER Conf. Organ. Change and Perfor mance, Santa Rosa, CA.

Bajari, P., S. Tadelis. 2001. Incentive versus transaction costs: A theory of procurement contracts. RAND J. Econom. 32(3) 387–407.

Banerjee, A. V., E. Duflo. 2000. Reputation effects and the limits of contracting: A study of the Indian software industry. Quart. J. Econom. 115(3) 989–1017.

Banker, R. D., S. M. Datar, C. F. Kemerer. 1991. A model to evaluate variables impacting the productivity of software maintenance Management Sci. 37

Barki, H., S. Rivard, J. Talbot. 1993. Toward an assessment of software development risk. J. Management Inform. Systems 10(2) 203–225.

Baron, R. M., D. A. Kenny. 1986. The moderator-mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations. J. Personality Soc. Psych. 51(6) 1173–1182.

Bharadwaj, A. S. 2000. A resource-based perspective on information technology capability and firm performance: An empirical investigation. MIS Quart. 24(1) 169–196.

Carmel, E., R. Agarwal. 2002. The maturation of offshore sourcing of information technology work. MIS Quart. Executive 1(2) 65–77.

Corts, K. S., J. Singh. 2004. The effect of repeated interaction on contract choice: Evidence from offshore drilling. J. Law, Econom. Organ. 20(1) 230–260.

Ethiraj, S. K., P. Kale, M. S. Krishnan, J. V. Singh. 2005. Where do capabilities come from and how do they matter? A study in the software services industry. Strategic Management J. 26(1) 25–45.

Gopal, A., T. Mukhopadhyay, M. S. Krishnan. 2002. The role of communication and processes in offshore software development. Comm. ACM 45

Gopal, A., K. Sivaramakrishnan, M. S. Krishnan, T. Mukhopadhyay. 2003. Contracts in offshore software development: An empirical analysis. Management Sci. 49(12) 1671–1683.

Gulati, R. 1995. Does familiarity breed trust? The implications of repeated ties for contractual alliances. Acad. Management J. 38(1) 85–112.

Hamilton, B., J. Nickerson. 2003. Correcting for endogeneity in strategic management research. Strategic Organ. 1 53–80.

Heckman, J. 1976. The common structure of statistical models of truncation, sample selection and limited dependent variables and a simple estimator for such models. Ann. Econom. Soc. Measurement 5 475–492.

Holmstrom, B. 1979. Moral hazard and observability. Bell J. Econom. 10(1) 74–91.

Kalnins, A., K. J. Mayer. 2004. Relationships and hybrid contracts: An analysis of contract choice in information technology. J. Law, Econom. Organ. 20(1) 207–229.

Kirsch, L., V. Sambamurthy, D.-G. Ko, R. Purvis. 2002. Controlling information systems development projects: The view from the client. Management Sci. 48(4) 484–498.

Krishna, S., S. Sahay, G. Walsham. 2004. Managing cross-cultural issues in global software outsourcing. Comm. ACM 47(4) 62–66.

Krishnan, M. S., C. H. Kriebel, S. Kekre, T. Mukhopadhyay. 2000. An empirical analysis of productivity and quality in software products. Management Sci. 46(6) 745–759.

Lacity, M. C., R. A. Hirschheim. 1993. Information Systems Outsourcing! Myths, Metaphors and Realities. John Wiley and Sons, New York.

Lichtenstein, Y. 2004. Puzzles in software development contracting. Comm. ACM 47(2) 61–65.

Maddala, G. S. 1983. Limited-Dependent and Qualitative Variables in Econometrics. Cambridge University Press, Cambridge, UK.

Masten, S. E., S. Saussier. 2002. Econometrics of contracts: An assessment of developments in the empirical literature on contracting. E. Brousseau, J.-M. Glachant, eds. The Economics of Contracts! Theories and Applications. Cambridge University Press, Cambridge, UK, 273–291.

Nakosteen, R., M. Zimmer. 1986. Marital status and earnings of young men: A model with endogenous selection. J. Human Resources 22(2) 248–268.

Nayyar, P. R. 1990. Information asymmetries: A source of competitive advantage for diversified service firms. Strategic Management J. 11(7) 513–519.

Nayyar, P. R. 1993. Performance effects of information asymmetry and economies of scope in diversified service firms. Acad. Management J. 36(1) 28–57.

Nidomolu, S. 1995. The effect of coordination and uncertainty on software project performance: Residual performance risk as an intervening variable. Inform. Systems Res. 6(3) 191–219.

Nidomolu, S. R., S. E. Goodman. 1993. Computing in India: An Asian elephant learning to dance. Comm. ACM 36(4) 15–22.

Powell, T. C., A. Dent-Micallef. 1997. Information technology as competitive advantage: The role of human, business and tech nology resources. Strategic Management J. 18(5) 375–405.

Pressman, R. S. 1992. Software Engineering! A Practitioner’s Approach. McGraw-Hill, New York.

Shah, S. 2004. India’s dwindling IT labor advantage. Optim. Magazine (September) 66–71.

Shaver, J. M. 1998. Accounting for endogeneity when assessing strategy performance: Does entry mode choice affect FDI survival? Management Sci. 44(4) 571–585.

Shehata, M. 1991. Self-selection bias and the economic consequences of accounting regulation: An application of two-stage switching regression to SFAS No. 2. Accounting Rev. 66(4) 768–787.

Svejnar, J. 1986. Bargaining power, fear of disagreement, and wage settlements: Theory and evidence from U.S. industry. Econometrica 54(5) 1055–1078.
