---
otero_id: 25150
otero_key: "4VN2HTVZ"
title: "A Choice Model for the Selection of Computer Vendors and Its Empirical Estimation"
authors: ""
year: "2001"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2001.11045664"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Choice Model for the Selection of Computer Vendors and Its Empirical Estimation

Kar Yan Tam, Kai Lung Hui

To cite this article: Kar Yan Tam, Kai Lung Hui (2001) A Choice Model for the Selection of Computer Vendors and Its Empirical Estimation, Journal of Management Information Systems, 17:4, 97-124

To link to this article: http://dx.doi.org/10.1080/07421222.2001.11045664

![](/api/attachments/4VN2HTVZ/fulltext/images/31cfc2e85b7158b6b2ab04b9c52922ffbbc24361681220d1132b536ae2f54ad5.jpg)

Published online: 09 Jan 2015.

![](/api/attachments/4VN2HTVZ/fulltext/images/e8458bb33ab72f61d835f9d3e1a796e91bf75902ef6fc04fff32c16f8a1df0ae.jpg)

Submit your article to this journal

![](/api/attachments/4VN2HTVZ/fulltext/images/fd701331362d18308a3879d9eec398e650efba76b33dfa2b29668e78ec9262a5.jpg)

Article views: 22

![](/api/attachments/4VN2HTVZ/fulltext/images/694781d6ca44f77ad1959c0331bc641c6480da46e8b0f774e05713c383e68cdf.jpg)

View related articles

# A Choice Model for the Selection of Computer Vendors and Its Empirical Estimation

KAR YAN TAM AND KAI LUNG HUI

KAR YAN TAM is Professor of Information & Systems Management and Senior Weilun Fellow at the Hong Kong University of Science & Technology. His research interests include information technology applications and electronic commerce. He has published extensively on these subjects in major information system journals, including Management Science, Information Systems Research, Journal of Management Information Systems, MIS Quarterly, Decision Support Systems, and IEEE Transactions on Engineering Management. He is currently on the editorial board of MIS Quarterly, Decision Support Systems, Journal of AIS, International Journal of Electronic Commerce, Information Systems Frontiers, and Journal of Global Information Management. Dr. Tam has extensive consulting experience with major local and overseas companies. He is currently leading a team of consultants to design and implement an Electronic Library for the Open University of Hong Kong. The Electronic Library was granted the Stockholm Challenge Award by the European Commission in June 2000. Professor Tam has developed a Mondex Internet payment solution in collaboration with Hongkong and Shanghai Banking Corporation (HSBC). The project is the first of its kind in the Asia Pacific region and has been approved by Mondex International.

KAI LUNG HUI is Assistant Professor in the School of Computing at the National University of Singapore. He received his Ph.D. in Information Systems from the Hong Kong University of Science and Technology. His research interests include demand and supply considerations of IT products, digital product characteristics and competitions, and electronic commerce. He has papers published or forthcoming in Communications of the ACM, IEEE Transactions on Engineering Management, and Information and Management.

ABSTRACT: Despite the important role of vendors in the IT procurement process, very few studies have considered vendor characteristics and their effects on the decision outcome of IT managers. In this paper, we present a discrete choice model to examine the effects of vendor characteristics on the purchase decisions of IT managers. Our intent is to empirically assess the effects of product variety, brand name, average price, and network externalities in the selection of computer vendors. To ensure that the effects are not technology-dependent, we deliberately use long time series data to calibrate the model. Annual data at the vendor level from 1965 to 1993 is used to infer the choice criteria of IT managers in three computer categories: mainframe, minis, and small systems. Our empirical findings indicate that a broader product line and a strong brand can effectively enhance the choice probability of a vendor. Implications of these findings and possible extensions are also discussed.

KEY WORDS AND PHRASES: brand, choice model, IT procurement, network externality, price.

RESEARCH IN IS HAS PRIMARILY ADDRESSED the demand side of information technology (IT), with a focus on its application and management. Work that addresses issues related to the supply side of IT has been scant, despite its growing importance.<sup>1</sup> An important IT management function that involves serious consideration on supply side factors is the procurement of IT products. IT managers are constantly faced with purchase decisions aimed at upgrading capacity, system enhancement, and efficiency improvement. As Attewell [2] has pointed out, vendors play a key role in the computerization of an organization. For instance, it is typical for an IT manager to consider supply side factors—such as vendor reputation, availability of upgrade path, scalability of the product, and installed base—before making a decision.

It is important to understand how IT managers make purchase decisions, the decision criteria used, and how these decisions affect market share of competing vendors. Such information is crucial to IT vendors, since the selection of suppliers often encompasses more than simply selecting the best product configuration. And for largebudget IT procurements, the decision often leads to a long-term strategic relationship with the selected vendor. For IS researchers, procurement-related purchase decisions deserve more attention as IT has now become a strategic asset of a firm [41]. So far, work in this area has largely been focused on the process of decision-making as it relates to project selection and management [28, 32, 39, 46] and to IT governance structures [9, 16, 29, 30, 43, 54]. Little work has been done to investigate factors that affect the purchase decision outcome. The current work attempts to fill this gap by framing the purchase decision as a choice outcome among competitive vendors and to measure the effects of supply side factors on the decision outcome.

Vendors take part in shaping the market demand by deciding on the mix of IT products, setting prices, and scheduling product launches. IT managers, on the other hand, evaluate the options available in the market and choose the products that meet their needs [19]. Knowing the decision criteria of IT managers provides IS researchers with a better understanding of the interplay between supply side characteristics and the procurement of IT products.

As an exploratory study, the current work confines IT vendors to suppliers of computers. The present study develops a formal choice model of the selection of computer vendors within different computer categories (mainframe, minis, and small systems). The sales of different computer models by each vendor are aggregated to derive the vendor’s market share in each computer category. Since our major objective is to examine IT managers’ decision criteria, theories on discrete choice prove useful for this purpose [1, 5, 36]. A discrete choice model makes it possible to estimate the effects of choice criteria from aggregated market share data. This is a methodological advantage, since we do not need to obtain data on individual purchases, which are practically impossible to collect given the long time period and the scope of analysis of the current study.

Specifically, our model is developed to measure the effects of product variety, brand effect, price, and network externalities (measured by total installed base of computers) in a particular category. Three discrete choice models—one each for mainframes, minis, and small systems, respectively—are developed to examine these variables. Personal computers (PCs) are not included in the present study because the market for PCs is quite different from that for other categories. Many PC users purchase PCs for home and entertainment uses. The profiles of business users and home users are quite different, and their decision criteria are likely to be different. Mixing them in the model would produce undesirable biased estimates of the variables.

While previous works in MIS, marketing, and economics have addressed these variables, most of these earlier studies focused on variables either at the individual product level or the aggregate economy level [20, 51]. Very few studies have looked at the joint effects of these variables over a relatively long time horizon. In this paper, we attempt to integrate all these variables into a single discrete choice framework. Using recent methodological advances in discrete choice model estimation, we provide empirical evidence on these vendor side variables.

This paper is organized as follows: The following section presents a brief review of the theory of discrete choice modeling and, in particular, the multinomial Logit model. The next section presents Berry’s approach as compared to the original MNL model. Following that we present the research model and variables of the present study. In the two subsequent sections the data source and data definitions are given and the analysis of the data and findings are discussed. Finally, we present some of the findings and limitations of the current study, and then conclusions.

## Review of Discrete Choice Modeling

DISCRETE CHOICE THEORY HAS BEEN BROADLY APPLIED to model individuals’choices of discrete alternatives [12, 31, 33, 52]. In general, traditional discrete choice models can be classified into two categories: models with stochastic decision rules and models with stochastic utility [1]. Models with stochastic decision rules attempt to capture the “bounded rationality” aspect of individuals, and in these models the individuals do not necessarily choose the alternative that gives them the highest utility. Stochastic utility models, on the other hand, are consistent with utility maximization, and individuals are assumed to opt for the alternative that gives the best outcome. Within the category of stochastic utility model, the two most commonly employed models are the Multinomial Logit (MNL) and the Generalized Extreme Value (GEV) model. McFadden [36, 37, 38] made significant contributions in this area by deriving the economic considerations and econometric properties of these two models.

Using discrete choice modeling, one can infer the effects of choice criteria of individuals from aggregated market data. As shown in Figure 1, the framework allows researchers to examine empirically the effects of a set of variables that may affect the choice outcome without using individual purchase data. Discrete choice modeling provides the theoretical foundation that links micro-level choice behavior with market-level outcome.

![](/api/attachments/4VN2HTVZ/fulltext/images/365376f174f0de7eb033baf66004c962f3472575f588c31959e4b05288c89d91.jpg)  
Figure 1. Linking Micro-Level Choice Outcome with Aggregated Market Data

The MNL model is the basic building block of the model developed in this study. A brief review of the model is given below.

Suppose purchaser i’s utility for choosing alternative j among finitely many alternatives takes the form:

$$
U _ {i j} = V _ {j} + \varepsilon_ {i j},\tag{1}
$$

where $V _ { j }$ is the deterministic component that represents the utility of selecting alternative $j ,$ and $\mathfrak { E } _ { i j }$ is the random component that is assumed to be independent and identically distributed with second-order exponential distributions. That is, $\Pr ( \varepsilon _ { i j } \leq x ) =$ $\exp [ - \exp - ( x / \mu + \gamma ) ]$ , where $\gamma$ is the Euler’s constant (» 0.5772) and $\mu$ is a scaling parameter. Under this assumption, the choice probabilities, $P _ { j }$ ,of the alternatives are:

$$
P _ {j} = e ^ {\frac {V _ {j}}{\mu}} \Bigg / \sum_ {i} e ^ {\frac {V _ {i}}{\mu}}.\tag{2}
$$

Although Equation 2 has been applied extensively in the choice modeling literature, there are a number of limitations associated with this approach. First, the model takes care of observable product characteristics only, and any unobservable factors (to the researcher developing the model) are lumped into the random error term $\varepsilon _ { i j } .$ . Such an approach mixes up the influence of product-level unobservable characteristics or sampling errors with purchaser-level sampling errors. When using the traditional MNL model, the researcher needs to identify all relevant product characteristics in order to produce a good model fit. This is not always feasible, since in most cases relevant attributes are simply unidentifiable. Hence it is impossible to account explicitly for product-level sources of errors in typical MNL models, and this imposes a limitation on the accuracy and application of the MNL model to typical choice situations.

Second, the MNL approach requires purchasers to choose one of the alternatives in the choice set. There is no “no purchase” option, and purchasers must make choices in response to any change in product attributes, even if such change has little impact on their decisions. While this assumption can be handled through adding the “no purchase” option to the choice set, data on such an option (the number of purchasers in the market who are not buying) may not be readily available and it would be difficult to define the values of product attributes for the “no purchase” alternative.

To resolve the above limitations, we adopt the estimation method proposed by Berry [6], which looks explicitly at the mean utility levels of purchasers. Using a modified formulation and estimation procedure, Berry’s methodology can effectively separate out the effects of product level sources of errors from purchaser-level errors, as well as taking into account the “no purchase” option. A brief review of the approach is presented in the next section.

The idea of Berry’s estimation method is to “invert” the market share equations to come up with the mean utility levels of purchasers toward the products.<sup>2</sup>

## An Alternative Estimation Method of Discrete Choice Models

Based on the MNL model as stated in Equation 1, consider the mean utility (denoted by d ) of vendor j:

$$
\delta_ {j} = x _ {j} ^ {\prime} \beta + \xi_ {j},\tag{3}
$$

where $x _ { j }$ is a vector that represents the vendors’ observable attributes. b is the parameter vector to be estimated, and $\xi _ { j }$ is the mean valuation of IT managers on some unobservable (to the researcher) characteristics of the vendor.

If values of $\ S _ { j }$ are known, then the above expression can be treated as a simple OLS estimation equation of $\ S _ { _ j }$ regressing on $\mathbf { X } _ { j } ,$ with $\xi _ { j }$ as the standard least square error, which has zero mean and normal distribution. Solving for $\ S _ { j }$ depends on the context of analysis, and different techniques and assumptions may be required for different models [10].

In the case of MNL, it is easy to show that $\ S _ { j }$ can be solved as

$$
\delta_ {j} = l n (s _ {j}) - l n (s _ {0}) = x _ {j} ^ {\prime} \beta + \xi_ {j}.\tag{4}
$$

That is, the mean utility levels of IT managers can be solved using market share information. These mean utilities can then be regressed on vendor characteristics to determine the effects of different vendor characteristics toward IT managers’ choice decisions. Note that the calculation on $\ S _ { j }$ also requires knowledge of $s _ { o } ,$ the market share of the “no purchase” alternative. Later in this paper, we shall show that $s _ { 0 }$ can be obtained by applying a priori knowledge to the total market potential.

As mentioned earlier, Equation 5 can effectively take care of unobservable characteristics (by building them into the $\xi _ { j }$ term). It also allows for the existence of “no purchase” customers. An added benefit here is that the characteristics come into the model in a linear fashion, and hence substantial effort is saved in the model’s estimation. Also, the explicit modeling of mean utilities as the dependent variable offers a direct interpretation of the model parameters.

Given the simple estimation procedure and the added robustness over other traditional estimation methods, Berry’s approach has been utilized in a number of empirical discrete choice studies to analyze demands for different types of products. In cases of nondurable goods, Besanko et al. [8] applied this technique to study the demand for yogurt and ketchup and the associated pricing behavior. For durable goods, Berry et al. [7] adopted this technique to study the U.S. automobile market. Recently, Bresnahan et al. [10] also took a similar approach in studying market segmentations of personal computers in the late 1980s.

## A Choice Model of Vendor Selection

IN OUR MODEL, AN IT MANAGER IS FACED WITH A DECISION to select among competing vendors for each computer purchase. The basic assumption is that the market is able to provide more than one alternative for the IT manager. In other words, the needs of the IT manager can be met by product offerings from different vendors and the decision becomes which vendor to select. The assumption does not deviate much from real practice, particularly in organizations where a formal tendering and procurement process is employed. Since a vendor will propose the most suitable model and configuration in its reply to a tender, the decision is equivalent to selecting the best proposal among competing ones from different vendors.

In our analysis, all computer models in a category produced by a vendor are aggregated and the total units sold are used to calculate the market share of the vendor in that category. One estimation equation is proposed for each of the three categories: mainframe, minis, and small systems. The model and the variables are shown in Figure 2.

## Model Variables

## Product Variety

The variety of computer models offered by a vendor in a category is considered to be an important variable. Organizations have different needs in terms of computing power. By providing multiple models and configurations, a vendor can serve a wider range of customers. By offering a broader product line, a vendor can broaden its customer base, which may lead to an increase in market share. Therefore IT managers will be inclined to select vendors that produce more computer models than those producing fewer models in a given category.

## Brand Name

We include vendor-specific dummies that capture the brand name effect of different vendors. The effect of brand on consumers’ choices and judgments has been well analyzed in the marketing literature (e.g., [22, 40]). Here, brand name refers to persistent factors—such as production quality, ability to match demand with appropriate features, and customer relationship—on which an overall impression of the vendor is formed. The brand name effect is a long-term effect that does not change on a yearby-year basis.

![](/api/attachments/4VN2HTVZ/fulltext/images/e5d2aab3577b2fc91b73dfe39cb38b7c64b34e947de184f16fdd84d72e918437.jpg)  
Figure 2. Variables Affecting the Selection of the Computer Vendor

Since our data sample runs over a period of 29 years, it is likely that the brand effect is not invariant over the entire duration. In particular, given the dynamic nature of computer markets, it is possible that computer vendors experience shift in corporate brand building strategies over time. An ideal remedy here is to assign one dummy variable to each brand in each year. However, in our situation, this is not possible because the number of parameters explodes substantially, which significantly hinders the models’ identification and efficiency.

To allow for more reasonable patterns of brand effect while keeping control of the total number of parameters to be estimated, we impose two brand dummies for each computer vendor. One brand dummy is used to capture the brand effect in the first half of our sample (1965–1979), while the other one captures the latter half (1979–1993). This explicitly allows us to examine the shifts in relative brand power in the computer market starting from the year 1980,<sup>3</sup> while efficiency of the final model is preserved.

## Network Externalities

Network externalities is a common phenomenon in many areas of economics and sociology. It is used to describe the situation where “the utility that a given user derives from the good depends upon the number of other users who are in the same network” [26, p. 424]. Typical IT innovations that exhibit positive network externality include phone, fax, and e-mail. As the user base of these products grows, the value for other users increases because it facilitates direction connection. Subsequently, the chance for future adoption improves.

The analytical properties of network externalities have been extensively developed in the economics literature [15, 26, 27]. Recently, network externalities have also been used to analyze new product upgrade decisions [42]. Nevertheless, most of these studies focus on deriving the analytical implications of network externalities. Very few studies have empirically estimated their effects. An exception is the work by Brynjolfsson and Kemerer [11]. They studied the impact of network externalities on microcomputer software. Using a simple hedonic regression model, Brynjolfsson and Kemerer empirically estimated the impact of network externalities on the price of spreadsheet software.

While the network externalities’ effect on selected software products has been demonstrated, their impact on the demand for computers is not well researched. In the case of business computing, computer vendors incorporate different built-in features into their products. For instance, a mainframe computer may have its own communication protocol (e.g., IBM’s SNA) or file structure, so that other computers must incorporate the same system in order to communicate with it. Because of these vendor-specific features and industry standards,<sup>4</sup> IT managers are likely to consider the existing installed base of the vendor’s computers before making the purchase decision. This is because as more organizations purchase the vendor’s computers in that category, one can gain positive externalities through better connectivity and interoperability, a larger pool of expertise in the market, availability of more application software, and the existence of a secondary market (i.e., increased resale value).

## Average Price

Price has been an important variable in traditional demand analysis and has a significant impact on consumers’choice behavior [18, 48]. At the economy level, Gurbaxani and Mendelson [21] related price to the growth of IT spending. They found that other than the technology diffusion effect, price also plays an important role in shaping the market demand for IT. Their work, together with several subsequent studies (e.g., [44, 51]), confirms the importance of price in aggregate demand analysis. Following previous work, the current study includes price as a decision variable. Note that there is a difference between the price used in the current study and the price used in previous work. Here, the price variable is defined as the average price of all models produced by a single vendor in a category. It measures the average category price set by a computer vendor instead of the economy-wide price level typically measured by a computer price index. While the latter has been the focus of most existing literature, it does not fit the purpose of the present study.

## Model Form

Given the model in Figure 2, the utility of IT manager i toward vendor j in category k (k = mainframe, mini, or small) in year t is modeled as

$$
\begin{array}{r} U _ {i j k t} = \beta + \alpha_ {t} N O \_ M O D E L _ {j k t} + \alpha_ {2} A P _ {j k t} + \alpha_ {3} I B _ {j k t} + \alpha_ {4} M A _ {j k} \\ + \alpha_ {5} M B _ {j k} + \alpha_ {6} Y _ {t} + \xi_ {j k t} + \varepsilon_ {i j k t}, \end{array}\tag{5}
$$

where $N O \_ M O D E L _ { j k t }$ is the number of computer models produced by vendor j in category k in year $t ; A P _ { j k t }$ is the average price of computer models produced by vendor j in category k in year $t ; I B _ { j k t }$ is the installed base of vendor j’s computers in category k in year $t { - } l ; M A _ { j k }$ represents vendor-specific dummies between 1965 and 1979, and $M B _ { j k }$ represents the dummies from 1980 to 1993. Each vendor is assigned a unique pair of MA and MB in each category. $Y _ { t }$ is a year variable that controls for any variation due to time trend. $\displaystyle { \therefore \xi _ { j k t } }$ represents the vendor’s unobservable characteristics and $\mathfrak { E } _ { i j k t }$ is the sampling error.

Note that $\xi _ { j k t }$ is vendor-specific. It attempts to capture all unobservable (to the researcher) vendor characteristics that may affect the IT managers’choice outcome in a particular year. These may include advertising efforts expensed by the vendor in promoting its products or promotion tactics used by a vendor in category k and year t. Notice the difference between $\xi _ { j k t }$ and ${ M A } _ { j k }$ (or $M B _ { j k } )$ here. Although both variables are vendor-specific, the effect of the brand dummies is assumed to be relatively longlasting, consistent across all years that they are assigned, and pertaining only to the brand. On the other hand, $\xi _ { j k t }$ can vary on a yearly basis, reflecting vendor characteristics that are not observable by the researcher but would have short-term impact on the IT manager’s choice outcome.

Following Equation 3, the mean utility of IT managers on vendor j in category k in year t is:

$$
\delta_ {j} = \beta + \alpha_ {1} N O \_ M O D E L _ {j k t} + \alpha_ {2} A P _ {j k t} + \alpha_ {3} I B _ {j k t} + \alpha_ {4} M A _ {j k} + \alpha_ {5} M B _ {j k} + \alpha_ {6} Y _ {t} + \xi_ {j k t}\tag{6}
$$

and the corresponding estimation equations are:

$$
l n (s _ {j k t}) - l n (s _ {0 k t}) = \delta_ {j} = \beta + \alpha_ {1} N O \_ M O D E L _ {j k t} + \alpha_ {2} A P _ {j k t} + \alpha_ {3} I B _ {j k t} + \alpha_ {4} M A _ {j k}
$$

$$
+ \alpha_ {5} M B _ {j k} + \alpha_ {6} Y _ {t} + \xi_ {j k t},\tag{7}
$$

where $s _ { j k t }$ is the market share of vendor j in category k in year $t . s _ { 0 k }$ is the market share of the “no purchase” alternative in category k in year t. The value of this variable is obtained by subtracting all sales from the market potential in each category every year. Details of the data source and data definitions are described in the next section.

## Data Source and Definitions

THE DATA UTILIZED IN THIS STUDY ARE OBTAINED from International Data Corporation (IDC). IDC collects annual sales data of computer vendors in the United States. The data include the average price and sales of each model produced by a computer vendor in each category from 1965 to 1993. The computer models are classified into three categories, as defined in Table 1. Definitions of the variables are given in Table 2.

To estimate Equation 7, the market potential of all three categories is needed. Previous work used population (e.g., total number of firms) as a proxy for market potential. However, because there is enormous heterogeneity across firms, it would therefore be misleading to use the number of firms as our market potential for computers. To obtain reliable estimates of computer market potential, we adopt the Bass model [3]. The Bass diffusion model is widely used in the literature to capture the diffusion pattern of new innovations, and it has been extensively studied and applied in the marketing literature (e.g., [35]). Because of their parsimonious nature, diffusion models have started to become a popular tool to address diffusion-related studies in IS research [20, 23, 29, 30, 51]. Other than its robustness in capturing diffusion patterns, the Bass model also provides an estimation of the market potential that proves useful in the present context.

The estimation results using the Bass model are presented in Table 3. From the table, we can see that the adjusted R<sup>2</sup> is consistently high (> 0.8) across all three categories, implying that the Bass model captures the actual demand pattern reasonably well. The plot of the actual demand against the predicted value using the Bass model is shown in Figures 3a to 3c. Although there are some discrepancies in different time periods, the estimated Bass model matches the actual demand curves reasonably well. Three Bass models are estimated, with one for each category. The estimate M of each model is used as the market potential for that category. Details of the Bass model can be found in Appendix A.

## Data Analysis and Findings

TABLE 4 PRESENTS SOME OF THE DESCRIPTIVE STATISTICS of the data sample used in the current study.

The three equations (Equation 7) are estimated using ordinary least squares (OLS). The differences between a vendor’s market share and the “no purchase” alternative are regressed on the variables defined in Table 2.

## Estimation Results

## Selection of Mainframe Computer Vendors

There are altogether 229 observations of mainframe computer sales over the 29-year period. A total of 19 vendors offered mainframe computers in this period. As shown in Table 5, the adjusted R<sup>2</sup> is 0.7708, which is considered acceptable given the exploratory nature of the current study. Among the decision variables, product variety and most brand dummies are significant, whereas the average price of models and the installed base are insignificant.

<table><tr><td colspan="4">Table 1. Definitions of Computer Categories</td></tr><tr><td>Category</td><td>Definitions</td><td>Price Range</td><td>Typical Examples</td></tr><tr><td>Mainframe</td><td>Large general purpose or high-speed computers. Currently shipping models typically support over 128 users in a commercial environment.</td><td>Generally in excess of US$1 million.</td><td>IBM 308X, 3090, and water-cooled 390 series.</td></tr><tr><td>Mini</td><td>Includes traditional supermini-class computers and some systems classified by their vendors as small mainframes. Currently shipping models typically support 33 to 128 users in a commercial environment. Typically packaged in large file-cabinet-sized or rack-mountable configurations.</td><td>Average price ranges from US$100,000 to 1 million.</td><td>IBM System/38s and upper ranges of Digital&#x27;s VAX series (including all 8000s and 6000s).</td></tr><tr><td>Small Systems</td><td>Commonly used in automation, control, and communications processing environments. Currently shipping models usually support 2 to 32 users in a commercial environment. Typically packaged in desktop boxes or deskside towers.</td><td>Average price ranges from US$10,000 to $100,000.</td><td>All Digital&#x27;s lower range VAX, Series/1, System/36, and IBM&#x27;s RISC System/6000 and smaller AS/400 models.</td></tr><tr><td colspan="4">Source: International Data Corporation, 1997.</td></tr></table>

Table 2. Definitions of the Variables

<table><tr><td>Model Variables</td><td>Variable Definitions</td></tr><tr><td>Market Shares ( $s_{jkt}$ )</td><td>Total units of computers sold divided by the total market potential of a category.</td></tr><tr><td>Number of Models ( $NO\_MODEL_{jkt}$ )</td><td>Total number of models in a category that are selling in the market in year  $t$ .</td></tr><tr><td>Average Price ( $AP_{jkt}$ )</td><td>The average price across all models within a category in year  $t$ . Only models that are selling in the year are included in this calculation.</td></tr><tr><td>Installed Base of Computers ( $IB_{jk}$ )</td><td>The cumulative installed base (in units) of computers in a category in the preceding year (net of retired machines)</td></tr><tr><td>Brand Name ( $MA_{jk}$  and  $MB_{jk}$ )</td><td>Vendor-specific dummies are assigned to each vendor and a unique pair of  $MA$  and  $MB$  will be assigned in each category.* For the same vendor, if year &lt; 1980, then  $MA = 1$  and  $MB = 0$ . If year ≥ 1980, then  $MA = 0$  and  $MB = 1$ .</td></tr><tr><td>Unobservable Firm Characteristics ( $\xi_{jkt}$ )</td><td>These values are estimated as the least squares residuals using Berry&#x27;s methodology.</td></tr><tr><td>Market Share of the Outside Alternative ( $s_{0kt}$ )</td><td>The nonpurchased population (i.e., market potential – purchased units) divided by the market potential.</td></tr></table>

\* Note that one control firm is needed when assigning dummies to avoid the dummy variable “trap.” IBM is used as the control here.

Table 3. Estimation Results of the Bass Model

<table><tr><td>Category</td><td> $a^{*}$ </td><td> $b^{*}$ </td><td> $M^{*}$ </td><td>Adjusted  $R^{2}$ </td></tr><tr><td>Mainframe</td><td> $1.35 \times 10^{-3}$  $(2.74 \times 10^{-3})$ </td><td> $0.203^{**}$  $(1.7 \times 10^{-2})$ </td><td> $32249.23^{**}$  $(1100.61)$ </td><td>0.83</td></tr><tr><td>Mini</td><td> $-2.2 \times 10^{-3}$  $(2.96 \times 10^{-3})$ </td><td> $0.247^{**}$  $(2.29 \times 10^{-2})$ </td><td> $392058.67^{**}$  $(18825.8)$ </td><td>0.86</td></tr><tr><td>Small Computer</td><td> $2 \times 10^{-3}$  $(2.15 \times 10^{-3})$ </td><td> $0.258^{**}$  $(1.74 \times 10^{-2})$ </td><td> $3121861.06^{**}$  $(96907.18)$ </td><td>0.91</td></tr><tr><td colspan="5">* Standard errors in parentheses.** Significant at the 1 percent level.</td></tr></table>

The effect of product variety is significant and positive. IT managers are inclined to select a vendor that offers more products in the same category. The installed base of the vendor’s mainframe computers is not significant, suggesting that the externality effect may not be as important as we conjectured. A large existing installed base does not guarantee higher market share in future years.

![](/api/attachments/4VN2HTVZ/fulltext/images/e9c637eafcf8046d4cbea39179f79ff71519b8ee9a7e77af9fe63f53d7631a7a.jpg)  
Figure 3a. Plot of Actual Against Predicted Demand—Mainframe Market

![](/api/attachments/4VN2HTVZ/fulltext/images/bc46f1070d352b44bff7f208a8102eaf00b62aa70d31ad7acb707489b41101d8.jpg)  
Figure 3b. Plot of Actual Against Predicted Demand—Mini Market

![](/api/attachments/4VN2HTVZ/fulltext/images/63665049eef56be0f85ce434eb860c8b748cbc7bdcbbd31cebd5bd4f48f33170.jpg)  
Figure 3c. Plot of Actual Against Predicted Demand—Small Computer Market

Most vendor-specific dummies are significant and negative. When compared with IBM (our control firm), most vendors are inferior in terms of brand effect. IT managers show lower purchase desire for most brands other than IBM. Note that Tandem Computer was the only mainframe vendor that had an insignificant brand dummy from 1980 to 1993. A close look at the data reveals that the market share of Tandem increased in the later years. Since its appearance in the mainframe market in 1989, Tandem’s market share rose from 1.1 to 9.18 percent in 1993. Given the relatively large scale and high price of mainframes (in 1993, an average Tandem mainframe cost around two million U.S. dollars), this improvement was quite substantial. Other brands that had relatively smaller brand dummies are Unisys, Digital, and Amdahl. According to our data, these were consistently the closest competitors to IBM in the mainframe market. By comparing columns three and five in Table 5, we see that the brand dummies of most firms, although still significantly negative, improved slightly in the latter half of the sample. It appears that a number of other mainframe vendors tried to build up their brand over the studied period.

Table 4. Descriptive Statistics of the Data Sample

<table><tr><td></td><td>Total Number of Models Produced</td><td>Average Price of Computer Models (in US$000)</td><td>Total Number of Vendors</td></tr><tr><td colspan="4">Mainframe</td></tr><tr><td>Max</td><td>75</td><td>19804.33</td><td>15</td></tr><tr><td>Min</td><td>7</td><td>2603.43</td><td>4</td></tr><tr><td>Avg</td><td>33.17</td><td>6096.83</td><td>7.9</td></tr><tr><td colspan="4">Mini</td></tr><tr><td>Max</td><td>212</td><td>1011.09</td><td>50</td></tr><tr><td>Min</td><td>25</td><td>459.06</td><td>6</td></tr><tr><td>Avg</td><td>91.31</td><td>622.39</td><td>23.52</td></tr><tr><td colspan="4">Small Computer</td></tr><tr><td>Max</td><td>381</td><td>124.11</td><td>114</td></tr><tr><td>Min</td><td>19</td><td>29.71</td><td>9</td></tr><tr><td>Avg</td><td>198.66</td><td>53.19</td><td>58.83</td></tr></table>

Table 5. OLS Results for the Mainframe Market

<table><tr><td colspan="2">Variable</td><td colspan="3">Parameter Estimates†</td></tr><tr><td>NO_MODEL</td><td></td><td>0.17**</td><td>(2.91x10-2)</td><td></td></tr><tr><td>AP</td><td></td><td>-9.26x10-6</td><td>(1.94x10-5)</td><td></td></tr><tr><td>IB</td><td></td><td>1.08x10-4</td><td>(8.14x10-5)</td><td></td></tr><tr><td>Amdahl</td><td>MA1</td><td>-1.96** (0.49)</td><td>MB1</td><td>-1.19** (0.45)</td></tr><tr><td>Control Data Systems</td><td>MA2</td><td>-2.63** (0.37)</td><td>MB2</td><td>-2.28** (0.47)</td></tr><tr><td>Convex</td><td>MA3</td><td>N/A</td><td>MB3</td><td>-2.89** (0.70)</td></tr><tr><td>Denelcor</td><td>MA4</td><td>N/A</td><td>MB4</td><td>-4.41** (0.70)</td></tr><tr><td>Digital Equipment</td><td>MA5</td><td>-1.97** (0.49)</td><td>MB5</td><td>-1.51** (0.51)</td></tr><tr><td>Evans</td><td>MA6</td><td>N/A</td><td>MB6</td><td>-4.02** (0.95)</td></tr><tr><td>Fujitsu</td><td>MA7</td><td>N/A</td><td>MB7</td><td>-3.94** (0.68)</td></tr><tr><td>Groupe Bull</td><td>MA8</td><td>-1.96** (0.36)</td><td>MB8</td><td>-1.68** (0.46)</td></tr><tr><td>Hitachi</td><td>MA9</td><td>-1.97** (0.58)</td><td>MB9</td><td>-3.00** (0.46)</td></tr><tr><td>Intel</td><td>MA10</td><td>N/A</td><td>MB10</td><td>-2.75** (0.70)</td></tr><tr><td>Kendal</td><td>MA11</td><td>N/A</td><td>MB11</td><td>-2.85** (0.71)</td></tr><tr><td>NEC</td><td>MA12</td><td>N/A</td><td>MB12</td><td>-4.55** (0.76)</td></tr><tr><td>Saxpy</td><td>MA13</td><td>N/A</td><td>MB13</td><td>-4.92** (0.94)</td></tr><tr><td>Silicon Graphics</td><td>MA14</td><td>-4.41** (0.53)</td><td>MB14</td><td>-2.51** (0.48)</td></tr><tr><td>Tandem Computers</td><td>MA15</td><td>N/A</td><td>MB15</td><td>-0.68 (0.62)</td></tr><tr><td>Thinking Machines</td><td>MA16</td><td>N/A</td><td>MB16</td><td>-2.22** (0.56)</td></tr><tr><td>Unisys Corporation</td><td>MA17</td><td>-1.72** (0.37)</td><td>MB17</td><td>-1.01* (0.42)</td></tr><tr><td>Xerox</td><td>MA18</td><td>-2.76** (0.47)</td><td>MB18</td><td>N/A</td></tr></table>

† Standard errors in parentheses. N/A means that the firm did not sell in the mainframe market in that particular period.  
\*\* Significant at the 1 percent level.  
\* Significant at the 5 percent level.  
Number of observations: 229.  
Adjusted R<sup>2</sup>: 0.7708.  
Years: 1965–1993.

## Selection of Minicomputer Vendors

We included altogether 298 observations of minicomputer sales from 1965 to 1993. Notice that in each year we only choose vendors that had market shares that were greater than 1 percent. The reason here is that there were a number of vendors that sold only one or two units in each year. These vendors are highly scattered, and including them increases our parameters significantly. Most of the time these vendors appear only one or two times during the 29-year period. Therefore, we choose to exclude them to save the degrees of freedom in our estimation.

Altogether, 26 firms are included in the final data set. As shown in Table 6, the adjusted R<sup>2</sup> is 0.7681, indicating satisfactory model fit. Most of the estimated results resemble those of the mainframe market. Again, product variety is significant and positive. The installed base of the vendor’s own minicomputers continues to be insig nificant, indicating a null externality effect. Most firm-specific dummies are significant and exhibit negative coefficients. This again demonstrates the strong brand power of IBM in the minicomputer market. All these results are consistent with those of the mainframe market. Nevertheless, the average price charged by the vendors is significant and negative in the minicomputer market. Vendors that consistently charged more tended to drive away customers.

The brand dummies indicate that three minicomputer vendors, namely Digital Equipment Corporation (DEC), Hewlett-Packard (HP), and SUN Microsystems, may not be inherently weaker than IBM in terms of brand power in the 1980s and early 1990s. SUN appeared in the mini market only in the early 1990s, but once it entered the market it sold a significant number of units. Both HP and DEC took part in this market in the early 1970s. Although IBM dominated these two firms in the early half of the sample, HP and DEC caught up (in terms of building a good brand) after 1980. In fact, DEC was consistently the “second place” player in the minicomputer market, and in some years (e.g., from the late 1970s to the early 1980s), it even challenged the leading position of IBM. Similarly, the market shares of HP were consistently high, and it was one of the biggest players in the minicomputer market.

Table 6. OLS results for the Mini Market

<table><tr><td colspan="2">Variable</td><td colspan="3">Parameter Estimates†</td></tr><tr><td>NO_MODEL</td><td></td><td colspan="3">6.28x10-2** (1.34x10-2)</td></tr><tr><td>AP</td><td></td><td colspan="3">-4.92x10-4* (1.97x10-4)</td></tr><tr><td>IB</td><td></td><td colspan="3">2.20x10-5 (1.19x10-5)</td></tr><tr><td>Computer Vision</td><td>MA1</td><td>-2.79** (0.48)</td><td>MB1</td><td>-1.28** (0.34)</td></tr><tr><td>Concurrent Computer</td><td>MA2</td><td>-2.62** (0.40)</td><td>MB2</td><td>-1.42** (0.37)</td></tr><tr><td>Control Data Systems</td><td>MA3</td><td>-2.97** (0.35)</td><td>MB3</td><td>N/A</td></tr><tr><td>Data General</td><td>MA4</td><td>-2.45** (0.41)</td><td>MB4</td><td>-1.20** (0.36)</td></tr><tr><td>Digital Equipment</td><td>MA5</td><td>-1.88** (0.29)</td><td>MB5</td><td>-0.44 (0.27)</td></tr><tr><td>Encore Computer</td><td>MA6</td><td>N/A</td><td>MB6</td><td>-1.78** (0.40)</td></tr><tr><td>Groupe Bull</td><td>MA7</td><td>-1.23** (0.27)</td><td>MB7</td><td>-1.19** (0.32)</td></tr><tr><td>Hewlett-Packard</td><td>MA8</td><td>-2.17** (0.38)</td><td>MB8</td><td>-0.48 (0.34)</td></tr><tr><td>ICL</td><td>MA9</td><td>N/A</td><td>MB9</td><td>-2.08** (0.77)</td></tr><tr><td>MAI Systems</td><td>MA10</td><td>N/A</td><td>MB10</td><td>-1.72** (0.43)</td></tr><tr><td>Marixx</td><td>MA11</td><td>N/A</td><td>MB11</td><td>-1.03* (0.49)</td></tr><tr><td>McDonnell Info. Sys.</td><td>MA12</td><td>N/A</td><td>MB12</td><td>-1.77** (0.52)</td></tr><tr><td>Modular Comp. Sys.</td><td>MA13</td><td>-3.11** (0.43)</td><td>MB13</td><td>-1.95* (0.80)</td></tr><tr><td>Motorola Comp. Sys.</td><td>MA14</td><td>-3.13** (0.74)</td><td>MB14</td><td>N/A</td></tr><tr><td>NCR</td><td>MA15</td><td>-2.16** (0.30)</td><td>MB15</td><td>-1.30** (0.37)</td></tr><tr><td>NCR (Tandem)</td><td>MA16</td><td>N/A</td><td>MB16</td><td>-1.70** (0.64)</td></tr><tr><td>Sequent Comp. Sys.</td><td>MA17</td><td>N/A</td><td>MB17</td><td>-1.18* (0.48)</td></tr><tr><td>Siemens Nixdorf</td><td>MA18</td><td>N/A</td><td>MB18</td><td>-1.81** (0.47)</td></tr><tr><td>Silicon Graphics</td><td>MA19</td><td>N/A</td><td>MB19</td><td>-1.85** (0.63)</td></tr><tr><td>Stratus Computer</td><td>MA20</td><td>N/A</td><td>MB20</td><td>-1.94** (0.45)</td></tr><tr><td>Sun Microsystems</td><td>MA21</td><td>N/A</td><td>MB21</td><td>-0.53 (0.81)</td></tr><tr><td>Tandem Computers</td><td>MA22</td><td>N/A</td><td>MB22</td><td>-0.99** (0.38)</td></tr><tr><td>Unisys Corporation</td><td>MA23</td><td>-1.63** (0.28)</td><td>MB23</td><td>-1.44** (0.35)</td></tr><tr><td>Wang</td><td>MA24</td><td>N/A</td><td>MB24</td><td>-1.43** (0.39)</td></tr><tr><td>Xerox</td><td>MA25</td><td>-3.29** (0.33)</td><td>MB25</td><td>N/A</td></tr></table>

† Standard errors in parentheses. N/A means that the firm did not sell in the mini market in that particular period.  
\*\* Significant at the 1 percent level.  
\* Significant at the 5 percent level.  
Number of observations: 298.  
Adjusted R<sup>2</sup>: 0.7686.  
Years: 1965–1993.

From our estimation results, it appears that the brand power of IBM (relative to all other vendors in the market) dropped gradually over the years. The brand dummies of almost all other vendors have improved over the studied period.

## Selection of Small Computer Vendors

For the same reason as in the mini market, we include only vendors that captured more than 1 percent of the total market share in our data analysis. There were 448 observations of small computer sales during the entire period and a total of 59 firms were included in the data. The adjusted R<sup>2</sup> is 0.8956, indicating good model fit. Detailed estimation results are shown in Table 7.

Table 7. OLS Results for the Small System Market

<table><tr><td colspan="2">Variable</td><td colspan="3">Parameter Estimates†</td></tr><tr><td>NO_MODEL</td><td></td><td colspan="3">3.96x10-2** (1.01x10-2)</td></tr><tr><td>AP</td><td></td><td colspan="3">9.56x10-4 (1.35x10-3)</td></tr><tr><td>IB</td><td></td><td colspan="3">-5.88x10-7 (1.39x10-6)</td></tr><tr><td>Unisys Corporation</td><td>MA1</td><td>-1.56** (0.21)</td><td>MB1</td><td>-1.48** (0.23)</td></tr><tr><td>Hewlett-Packard</td><td>MA3</td><td>-1.42** (0.24)</td><td>MB3</td><td>-1.41** (0.22)</td></tr><tr><td>Digital Equipment</td><td>MA4</td><td>-0.42 (0.22)</td><td>MB4</td><td>-0.30 (0.20)</td></tr><tr><td>NCR</td><td>MA5</td><td>-2.41** (0.20)</td><td>MB5</td><td>-1.42** (0.23)</td></tr><tr><td>Data General Corp.</td><td>MA6</td><td>-0.96** (0.26)</td><td>MB6</td><td>-1.90** (0.23)</td></tr><tr><td>Texas Instruments</td><td>MA12</td><td>-1.40** (0.27)</td><td>MB12</td><td>-1.38** (0.24)</td></tr><tr><td>Wang</td><td>MA13</td><td>-1.05** (0.33)</td><td>MB13</td><td>-1.63** (0.24)</td></tr><tr><td>Tandy/Radio Shack</td><td>MA20</td><td>N/A</td><td>MB20</td><td>-0.49 (0.28)</td></tr><tr><td>SCI Systems</td><td>MA21</td><td>N/A</td><td>MB21</td><td>-1.51** (0.45)</td></tr><tr><td>Integrated Bus. Comp.</td><td>MA27</td><td>N/A</td><td>MB27</td><td>-1.54** (0.45)</td></tr><tr><td>Televideo</td><td>MA31</td><td>N/A</td><td>MB31</td><td>-1.46** (0.45)</td></tr><tr><td>Classic Technology</td><td>MA33</td><td>N/A</td><td>MB33</td><td>-1.56** (0.46)</td></tr><tr><td>Sun Microsystems</td><td>MA36</td><td>N/A</td><td>MB36</td><td>-1.14** (0.36)</td></tr><tr><td>Compaq Comp. Corp.</td><td>MA37</td><td>N/A</td><td>MB37</td><td>-1.26** (0.38)</td></tr></table>

† Standard errors in parentheses. N/A means that the firm did not sell in the small computer market in that particular period. All excluded brand dummies are significant and their effects are negative relative to IBM. The magnitudes of all excluded dummies exceed –1.6, with the majority lying around –2.0 to –3.0. \*\* Significant at the 1 percent level. \* Significant at the 5 percent level. Number of observations: 448. Adjusted R<sup>2</sup>: 0.8956. Years: 1965–1993.

Since there are too many brands included in the small computer category, in Table 7 we report only those brand dummies that are exceptional—that is, either they had relatively strong brands as compared to IBM or they exhibited substantially different parameters over the two periods of the study.

In Table 7, we see that product variety is again found to be significant and positive. Producing more small computer models may improve the vendor’s chance of being selected by IT managers. Similar to the mainframe market, average price and the installed base of the vendor’s own small computers are not significant factors in the IT managers’ choice of computer vendors. Having a large customer base may not necessarily improve market share of a small computer vendor.

For the firm-specific dummies, almost all firms (56 out of 58) have significant and negative parameters as compared to IBM. This once again demonstrates the market dominance of IBM in this category. The two exceptional firms are DEC and Tandy/

Market Shares of Sun and Compaq  
![](/api/attachments/4VN2HTVZ/fulltext/images/7036501cb4b4adacb4439b3c30d2fc3b2e1bda71362906aef1decc8b3a90b658.jpg)  
Figure 4. Market Shares of Sun and Compaq in the Small Computer Market (1990–1994)

Radio Shack. DEC was again the closest competitor to IBM in the small computer category. Indeed, during the 1970s and early 1980s it overtook IBM’s leading position to become the champion in market share. In the early 1990s, the market performance of DEC still followed closely behind IBM and their difference in market share was often within a small margin. Hence DEC was consistently one of the “strongest” players in the small computer market, and our estimation results show that its brand power was not weaker than IBM in both the early years as well as in the more recent period.

Tandy/Radio Shack grew to be a significant player in the small computer market only during 1982 to 1988. However, during that period, its sales increased considerably. And during the peak years (1983 and 1984) it successfully squeezed into the hall of fame by capturing more than 10% of the total market share.<sup>6</sup>

Note that there are two relatively “new” brands that have quite strong brand power as compared to IBM. These are SUN Microsystems and Compaq. When we look closely at the actual data (e.g., the market share of SUN and Compaq in the early 1990s, as shown in Figure 4), these two companies, although joining the market only after 1990, emerged to become key players within this market. It appears that the brand effect of IBM has been challenged by a few emerging vendors in the small computer category in recent years.

## Discussion and Limitations

OUR OBJECTIVE IS TO EXAMINE THE CHARACTERISTICS of computer vendors and their impact on IT managers in making purchase decisions. More specifically, we investigate the effects of product variety, brand name effect, installed base, and average price on the purchase of three categories of computers over the period from 1965 to 1993. Some of the major findings are discussed below.

First, product variety is consistently significant across all three computer categories. This is consistent with our expectation that by offering more models in the same product category a vendor will increase its likelihood of being selected. This result supports Kahn’s [25] proposal of offering high-variety product lines as an effective competitive strategy against rivals. Ahigh-variety vendor reduces the information search cost as well as the switching cost of IT managers. In economic terms, the overall effect is an increase in consumer surplus. As argued by Sutton et al. [50], rapid technological changes as observed in the computer industry render it very difficult to acquire and evaluate relevant information. IT managers may find it more cost-effective to select a vendor with a broader product line so that, in case of upgrade and replacement, the search cost for different alternatives can be reduced. Also, switching cost is a major concern in the high-technology market. Previous work has shown that organizational buyers tend to select their existing vendor for high-tech products such as computer equipment to reduce switching costs [47]. For computer purchases, switching cost refers to efforts in porting existing software to the new platform, developing technical expertise, and establishing vendor–customer relationships. To reduce switching costs, IT managers may have little incentive to select other vendors if the existing vendor can provide alternative models to meet their emerging needs. Engaging a vendor that offers a broader product line provides more options for IT managers in the future. Further choices can be regarded as real options, as suggested in the recent capital budgeting literature [13, 34]. Real options can be interpreted as the right of the manager to upgrade, trade-in, and replace existing computers with lower information and switching cost. Real options have value, and this value could be realized by selecting a large-variety vendor. One interesting line of future research is to investigate the extent to which compatibility, interoperability, and interconnectivity—which are ranked among the top priorities in IT procurement [14]—can be reflected in product variety.

Second, our results indicate that IT managers are subject to strong brand effect in the decision process. The brand effect is strong and prevailing over the investigated period. IBM has the strongest brand effect across all three computer categories. Most other vendors (except several insignificant cases) face an inherent disadvantage when compared with IBM. Many business customers simply regard IBM as the “default” brand when considering buying computers, as reflected in a popular saying that “no one was ever fired for buying IBM.” This popularity and “authoritative” brand impression of IBM gives it a definite advantage across all three categories. According to an Adscope report [49, p. 204], which tracks advertising spending of computer vendors, Compaq, with an advertising expenditure totaling US\$47,237,724, was second only to IBM (US\$77,501,023) in advertising spending in 1992. Incidentally, our findings in the small computer market indicate that the brand effect of Compaq, although still weaker than IBM, is among one of the strongest in the small computer category. The dominant effect of brand on IT managers’ purchase decisions may suggest a buying behavior that deviates from what has been described in the existing IT management literature.

Third, the installed base of the vendor’s computers is not significant in all three computer categories. This may be due to several reasons. First, the installed bases of these three categories of computers are generally small and therefore the “networks” of adopters are also much smaller. Given that externality is a phenomenon that depends on the size of the user base, the relatively small installed base of these largescale computer systems may render the externality effect insignificant in these markets. Second, as application software and computer hardware were tightly coupled in the 1960s and 1970s [55], the installed base had little power to induce a large number of independent software vendors to produce application software for a particular computer. As a result, past sales may not necessarily guarantee market share improvement in the future. The external influence or “word of mouth” effect owing to existing users may not be a significant facilitator for new sales in these computer markets.

Third, for many IT products, like software or personal computers, internal compatibility within the organization typically serves as a major source of externality.<sup>7</sup> For large-budget items such as computers, they tend to have longer life span and repurchases will not be frequent. This may limit the applicability of internal compatibility, which may also contribute to this finding of insignificance.

Finally, the impact of price on choice outcome may not be substantiated. Nevertheless, readers are reminded that the average price measurement that we adopt in this study is intrinsically limited. In particular, price tags for these large-scale computer systems can be quite illusive, since these computers are often customizable and extensible.<sup>8</sup> There is a significant possibility that the price variable does not efficiently capture some unobserved financial arrangements, development and maintenance agreements, or software bundling options that were made between the vendors and the customers [45, 53]. Hence the results associated with the price variable should be interpreted with care.

## Limitations and Extensions

Since the model studied in this paper is built from a number of aggregate variables and estimation assumptions, there are some possible sources of measurement or specification limitations that are worth mentioning.

First, the current study uses total number of models as a proxy for product variety. While this is the closest and the best possible measurement that we can construct to capture the diversification aspect of computer vendors, we do realize that it may be too general, especially for larger-scale computer systems. In particular, mainframe buyers and sellers often need to come into exclusive agreements about the final product configuration, and these computers are often customized before shipping to customers. However, this phenomenon tends to be less pervasive as the size of computer systems gets smaller. Furthermore, the variety variable is shown to be highly significant in our estimated model.

Second, although product data and price for each purchase certainly help to calibrate the price effect more accurately, the unavailability of transaction data over such an extended period makes it very difficult to do so. The average price serves as a proxy for the cost of purchase in this paper and the readers should interpret the results with this limitation in mind.

Third, the internal compatibility and interoperability aspect of the network effect is particularly difficult to capture, especially when we lack individual transaction and purchase data. Therefore the total installed base variable that we adopt in this study may not represent an all-around externality measurement.

Fourth, although the Bass model has been empirically demonstrated to be robust across many product categories, we realize that it does not take into account repurchases from the same customer (in our context, the same IT manager). If repurchases are frequent, then the Bass model estimates may not be consistent and the model may tend to overestimate the resulting market potential. To further examine the robustness of the proposed estimation model with respect to market size, we conduct a sensitivity analysis with respect to different market potentials in Appendix B. The result shows that the estimated parameters in our model are quite stable across different market size estimates.

Fifth, a possible source of specification error comes from the relationship between the model variables $( x _ { j } )$ and the unobservable vendor characteristics $( \xi _ { j } )$ . One of the basic assumptions in least square estimation is that these terms should be independent. However, since some vendor variables (an often mentioned example here is price) may be inherently related to $\xi _ { j } ,$ the actual values of those variables may be endogenously determined by the demand system. In those cases, the independence assumption is violated, and the final least squares estimators (b and a) may be inconsistent. It has been well demonstrated that this endogeneity problem tends to bias the least square estimators downward [6, 7, 8, 10, 17]. The traditional solution to this problem is to rely on “instrument” variables, which are correlated with the model variables $( x _ { j } )$ , but yet which are independent from the error $( \xi _ { j } )$ . As suggested by Berry [6] and other related studies, one associated benefit of this methodology is that the formulation of market shares and utilities can effectively allow for instrumental variable estimations even on the Logit formulation. However, in our current work, since the variables are captured at the vendor level and the data series runs over a period of 29 years, it is very difficult for us to construct and collect data on meaningful instruments that can satisfy the above requirements. While supply side cost shifters are often regarded as a source of good instruments, such information is lacking and no instrument is used in the present study. If instrumental variable estimation is possible, one should expect the estimated parameters to grow in magnitude.

Finally, the present study lumps all unobservable vendor characteristics into one single term. Due to the limited amount of data, we have not been able to add more variables into our model. If those uncontrolled variables follow the general least squares error assumptions, then their resultant effects on the final estimations may not be too pervasive or detrimental. However, even if this assumption is satisfied, it would still be beneficial for us if we could explicitly isolate the variables and examine their resulting impacts on consumers’ utilities. For instance, knowledge of the firms’ advertising spending in each computer category can help us understand more about IT managers’ receptiveness to computer ads.

## Conclusion

WE HAVE DEVELOPED A FORMAL CHOICE MODEL on the selection of computer hardware vendors. Several variables, including average price, product variety, network externality, and brand name, which may affect the choice of vendors, are examined. Our empirical findings indicate that broader product lines and a reputable brand can effectively enhance the choice probability of the vendor. The effect of average price varies among computer categories, and it is insignificant in both the mainframe and small computer markets. Finally, network externality is consistently shown to be insignificant in all three computer categories.

The current study represents a pioneering effort, focusing specifically on the choice of IT vendors. While a large number of IS studies have been conducted on the demand side of IT products, very few have explicitly incorporated nontechnological vendor characteristics in their analyses. Today, users and vendors are working more closely together than before. Strategic alliances between vendors and user organizations are being established at a surging rate. For practitioners and researchers alike, supply side factors will become more and more important in many aspects of IT management.

## NOTES

1. Recently, the industrial structures of IT products and supply side considerations have received increasing attention from IT researchers. Major journals, including Management Science and Information Systems Research, have announced special issues aimed at the IT industry.

5. The starting year (1965) is assigned a value of 1 for the year variable.

6. The shares of Tandy/Radio Shack were even greater than IBM in those two years.

7. Substantial training and adjustments in organizational culture need to be carried out if a switch of software or computer standard is brought about within the organization.

chase customers. The authors would like to thank Stan Liebowitz from the University of Texas– Dallas for pointing this out to us.

## REFERENCES

1. Anderson, S.P.; Palma, A.D.; and Thisse, J. Discrete Choice Theory of Product Differentiation. Cambridge, MA: MIT Press, 1992.

2. Attewell, P. Technology diffusion and organizational learning: the case of business computing. Organizational Science, 3, 1 (1992), 1–19.

3. Bass, F.M. A new product growth model for consumer durables. Management Science, 15, 1 (1969), 215–227.

4. Beatty, S., and Smith, S.M. External search effort: an investigation across several product categories. Journal of Consumer Research, 14, 1 (June 1987), 83–95.

5. Ben-Akiva, M., and Lerman, S.R. Discrete Choice Analysis: Theory and Application to Travel Demand. Cambridge, MA: MIT Press, 1985.

6. Berry, S.; Levinsohn, J.; and Pakes, A. Automobile prices in market equilibrium. Econometrica, 63, 4 (1995), 841–890.

7. Berry, S.T. Estimating discrete-choice models of product differentiation. RAND Journal of Economics, 25, 2 (1994), 242–262.

8. Besanko, D.; Gupta, S.; and Jain, D. Logit demand estimation under competitive pricing behavior: an equilibrium framework. Management Science, 44, 11 (November 1998), 1533– 1547.

9. Bresnahan, J. Someone to watch over IT. CIO, 11, 15 (1998), 36–41.

10. Bresnahan, T.F.; Stern, S.; and Trajtenberg, M. Market segmentation and the sources of rents from innovation: personal computers in the late 1980s. RAND Journal of Economics, 28 (1997), S17–S44.

11. Brynjolfsson, E., and Kemerer, C. Network externalities in microcomputer software: an econometric analysis of the spreadsheet market. Management Science, 42, 12 (1996), 1627– 1647.

12. Bunn, M. Taxonomy of buying decision approaches. Journal of Marketing, 57, 4 (1993), 38–56.

13. Busby, J.S. Real options and capital investment decisions. Management Accounting, 75, 10 (1997), 38–39.

14. Chau, P.Y.K., and Tam, K.Y. Factors affecting the adoption of open systems: an exploratory study. MIS Quarterly, 21, 1 (1997), 1–24.

15. Farrell, J., and Saloner, G. Standardization, compatibility and innovation. RAND Journal of Economics, 16, 1 (1985), 70–83.

16. Fuller, M.K., and Swanson, E.B. Information centers as organizational innovation. Journal of Management Information Systems, 9, 1 (Summer 1992), 47–67.

17. Greene, W.H. Econometric Analysis. New York: Macmillan, 1993.

18. Grewal, D., and Marmorstein, H. Market price variation, perceived price variation, and consumers’ price search decisions for durable goods. Journal of Consumer Research, 21, 3 (1994), 453–460.

19. Griese, J., and Kurpicz, R. Investigating the buying process for the introduction of data processing in small and medium-sized firms. Information and Management, 8, 1 (1982), 41– 51.

20. Gurbaxani, V. Diffusion in computing networks: the case of BITNET. Communications of ACM, 33 (1990), 65–75.

21. Gurbaxani, V., and Mendelson, H. An integrative model of information systems spending growth. Information Systems Research, 1, 1 (1990), 23–46.

22. Hoyer, W.D., and Brown, S.P. Effects of brand awareness on choice for a common, repeat-purchase product. Journal of Consumer Research, 17, 2 (1990), 141–148.

23. Hu, Q.; Saunders, C.; and Gebelt, M. Diffusion of information systems outsourcing: a reevaluation of influence sources. Information Systems Research, 8, 3 (1997), 288–301.

24. Johnston, W.J., and Bonoma, T. The buying center: structure and interaction patterns. Journal of Marketing, 45, 2 (1981), 143–156.

25. Kahn, B.E. Dynamic relationships with customers: high-variety strategies. Journal of the Academy of Marketing Science, 26, 1 (1998), 45–53.

26. Katz, M.L., and Shapiro, C. Network externalities, competition, and compatibility. American Economic Review, 75, 3 (1985), 424–440.

27. Katz, M.L., and Shapiro, C. Technology adoption in the presence of network externalities. Journal of Political Economy, 96, 4 (1986), 822–841.

28. Kemerer, C.F. Software Project Management: Reading and Cases. New York: Irwin/ McGraw-Hill, 1997.

29. Loh, L., and Venkatraman, N. Determinants of information technology outsourcing. Journal of Management Information Systems, 9, 1 (Summer 1992a), 7–24.

30. Loh, L., and Venkatraman, N. Diffusion of information technology outsourcing: influence sources and the Kodak effect. Information Systems Research, 3, 4 (1992b), 334–358.

31. Louviere, J.J. Using discrete choice models with experimental design data to forecast consumer demand for a unique cultural event. Journal of Consumer Research, 10, 3 (1983), 348–361.

32. Lucas, H.C. Implementation: The Key to Successful Information Systems. New York: Columbia University Press, 1981.

33. Luce, R.D. Individual Choice Behavior: A Theoretical Analysis. New York: Wiley, 1959.

34. Luehrman, T.A. Investment opportunities as real options. Harvard Business Review, 76, 4 (1998), 51–67.

35. Mahajan, V.; Muller, E.; and Bass, F.M. Diffusion of new products: empirical generalizations and managerial uses. Marketing Science, 14, 3 (1995), G79–G88.

36. McFadden, D. Conditional logit analysis of qualitative choice behavior. In P. Zarembka (ed.), Frontiers in Econometrics. New York: Academic Press, 1974, pp. 105–142.

37. McFadden, D. Modeling the choice of residential location. In A. Karlgvist, L. Lundqvist,

F. Snickars, and J.W. Weibull (eds.), Spatial Interaction Theory and Planning Models. Amsterdam: North-Holland, 1978, pp. 75–96.

38. McFadden, D. Econometric models of probabilistic choice. In C.F. Manski and D. McFadden (eds.), Structural Analysis of Discrete Data with Econometric Applications. Cambridge, MA: MIT Press, 1981, pp. 198–272.

39. McFarlan, F.W. Portfolio approach to information systems. Harvard Business Review, 59, 5 (September–October 1980), 142–150.

40. Muthukrishnan, A.V. Decision ambiguity and incumbent brand advantage. Journal of Consumer Research, 22, 1 (1995), 98–109.

41. OECD. Information Technology Outlook 1997. OECD, France, 1997.

42. Padmanabhan, V.; Rajiv, S.; and Srinivasan, K. New products, upgrades, and new releases: a rationale for sequential product introduction. Journal of Marketing Research, 34, 4 (1997), 456–472.

43. Panko, R. End-User Computing. New York: John Wiley & Sons, 1988.

44. Parker, P.M. Price elasticity dynamics over the adoption life cycle. Journal of Marketing Research, 29, 3 (1992), 358–367.

45. Puri, S.J., and Sashi, C.M. Anatomy of a complex computer purchase. Industrial Marketing Management, 23, 1 (1994), 17–27.

46. Raymond, L. Organizational context and information system success: a contingency approach. Journal of Management Information Systems, 6, 4 (Spring 1990), 5–20.

47. Rosenthal, S.R. Progress toward the factory of the future. Journal of Operation Management, 4 (May 1984), 203–228.

48. Russo, J.E. The value of unit price information. Journal of Marketing Research, 14, 2 (1977), 193–201.

49. The 6th Annual Computer Industry Almanac. Austin: The Reference Press, 1993.

50. Sutton, R.; Eisenhardt, K.; and Jucker, J. Managing organizational decline: lessons from Atari. Organizational Dynamics, 14, 1 (1985), 17–29.

51. Tam, K.Y. Dynamic price elasticity and the diffusion of mainframe computing. Journal of Management Information Systems, 13, 2 (Fall 1996), 163–183.

52. Tversky, A. Elimination-by-aspects: a theory of choice. Psychological Review, 79 (1972), 281–299.

53. Vyas, N., and Woodside, A.G. An inductive model of industrial supplier choice processes. Journal of Marketing, 48, 4 (1984), 30–45.

54. White, C.E., and Christy, D.P. The information center concept: a normative model and a study of six installations. MIS Quarterly, 11, 4 (December 1987), 451–458.

55. Yoffie, D.B. Strategic Management in Information Technology. Englewood Cliffs, NJ: Prentice Hall, 1994.

<sub>nsitivityAnalysisforthe</sub>M<sup>ainframeCompu</sup>

<table><tr><td rowspan="2">Variable</td><td colspan="5">Parameter Estimates $^{\dagger}$ </td></tr><tr><td colspan="2">Bass Estimate</td><td colspan="2">Bass Estimate + 10 percent</td><td>Bass Estimate – 10 percent</td></tr><tr><td>Adjusted R $^{2}$ </td><td colspan="2">0.7708</td><td colspan="2">0.7584</td><td>0.7681</td></tr><tr><td>NO_MODEL</td><td>0.17**</td><td>(2.91x10 $^{-2}$ )</td><td>0.18**</td><td>(2.93x10 $^{-2}$ )</td><td>0.16** (3.03x10 $^{-2}$ )</td></tr><tr><td>AP</td><td>-9.26x10 $^{-6}$ </td><td>(1.94x10 $^{-5}$ )</td><td>-1.70x10 $^{-5}$ </td><td>(1.96x10 $^{-5}$ )</td><td>1.76x10 $^{-5}$  (2.02x10 $^{-5}$ )</td></tr><tr><td>IB</td><td>1.08x10 $^{-4}$ </td><td>(8.14x10 $^{-5}$ )</td><td>1.55x10 $^{-4}$ </td><td>(8.20x10 $^{-5}$ )</td><td>-6.33x10 $^{-5}$  (8.47x10 $^{-5}$ )</td></tr><tr><td>Brand Dummies</td><td colspan="2">As reported in Table 5.</td><td colspan="2">Of the 25 dummies included, only one has a change in significance.</td><td>Of the 25 dummies included, only one has a change in significance.</td></tr><tr><td colspan="6"> $^{\dagger}$  Standard errors in parenthesis. ** Significant at the 1 percent level.</td></tr></table>

<sub>SensitivityAnalysisforthe</sub>M<sup>inicompute</sup>

<table><tr><td rowspan="2">Variable</td><td colspan="3">Parameter  $Estimates^†$ </td></tr><tr><td>Bass Estimate</td><td>Bass Estimate + 10 percent</td><td>Bass Estimate – 10 percent</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.7681</td><td>0.7482</td><td>0.7962</td></tr><tr><td>NO_MODEL</td><td> $6.28x10^{-2**} (1.34x10^{-2})$ </td><td> $6.00x10^{-2**} (1.36x10^{-2})$ </td><td> $6.82x10^{-2**} (1.33x10^{-2})$ </td></tr><tr><td>AP</td><td> $-4.92x10^{-4*} (1.97x10^{-4})$ </td><td> $-5.06x10^{-4*} (1.99x10^{-4})$ </td><td> $-4.51x10^{-4*} (1.96x10^{-4})$ </td></tr><tr><td>IB</td><td> $2.20x10^{-5} (1.19x10^{-5})$ </td><td> $2.28x10^{-5} (1.20x10^{-5})$ </td><td> $1.91x10^{-5} (1.18x10^{-5})$ </td></tr><tr><td>Brand Dummies</td><td>As reported in Table 6.</td><td>Of the 34 dummies included, none of them has a change in sign or significance.</td><td>Of the 34 dummies included, none of them has a change in sign or significance.</td></tr></table>

<sub>ificantat5</sub>p<sup>ercentl</sup> <sub>ficantat1</sub>p<sup>ercentl</sup> <sub>darderrorsi</sub>n<sup>parenth</sup>

<sub>ificantat5</sub>p<sup>ercentl</sup> <sub>ficantat1</sub>p<sup>ercentl</sup> <sub>darderrorsi</sub>n<sup>parenth</sup>

Ap

<table><tr><td rowspan="2">Variable</td><td colspan="3">Parameter Estimates $^{\dagger}$ </td></tr><tr><td>Bass Estimate</td><td>Bass Estimate + 10 percent</td><td>Bass Estimate – 10 percent</td></tr><tr><td>Adjusted R $^{2}$ </td><td>0.8956</td><td>0.8749</td><td>0.9190</td></tr><tr><td>NO_MODEL</td><td>3.96x10 $^{-2**}$  (1.01x10 $^{-2}$ )</td><td>3.47x10 $^{-2**}$  (1.05x10 $^{-2}$ )</td><td>5.29x10 $^{-2**}$  (9.80x10 $^{-3}$ )</td></tr><tr><td>AP</td><td>9.56x10 $^{-4}$  (1.35x10 $^{-3}$ )</td><td>3.24x10 $^{-4}$  (1.41x10 $^{-3}$ )</td><td>2.70x10 $^{-3*}$  (1.31x10 $^{-3}$ )</td></tr><tr><td>IB</td><td>-5.88x10 $^{-7}$  (1.39x10 $^{-6}$ )</td><td>-8.04x10 $^{-7}$  (1.45x10 $^{-6}$ )</td><td>-4.53x10 $^{-7}$  (1.35x10 $^{-6}$ )</td></tr><tr><td>Brand Dummies</td><td>As reported in Table 5.</td><td>Of the 76 dummies included, only one has a change in significance.</td><td>Of the 76 dummies included, only one has a change in significance.</td></tr></table>
