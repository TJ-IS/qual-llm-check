---
otero_id: 26552
otero_key: "TZDMH2AG"
title: "The Return on Information Technology: Who Benefits Most?"
authors: "Emmanuel Dhyne; Jozef Konings; Jeroen Van den bosch; Stijn Vanormelingen"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2020.0960"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.241.16.16] On: 04 December 2020, At: 18:59 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## Information Systems Research

![](/api/attachments/TZDMH2AG/fulltext/images/acbe37c4553053d02fefb47925cf412517d2de2b8b75c7aaef8dc26e0aeae4be.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## The Return on Information Technology: Who Benefits Most?

Emmanuel Dhyne, Jozef Konings, Jeroen Van den bosch, Stijn Vanormelingen

To cite this article:

Emmanuel Dhyne, Jozef Konings, Jeroen Van den bosch, Stijn Vanormelingen (2020) The Return on Information Technology: Who Benefits Most?. Information Systems Research

Published online in Articles in Advance 24 Nov 2020

https://doi.org/10.1287/isre.2020.0960

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Return on Information Technology: Who Bene<sup>fi</sup>ts Most?

Emmanuel Dhyne,<sup>a,b</sup> Jozef Konings,<sup>c,d,e</sup> Jeroen Van den bosch,<sup>d,f</sup> Stijn Vanormelingen<sup>d</sup>

<sup>a</sup> National Bank of Belgium, 1000 Brussels, Belgium; <sup>b</sup> University of Mons, 7000 Mons, Belgium; <sup>c</sup> University of Liverpool, Liverpool L69 7ZH, United Kingdom; <sup>d</sup> KU Leuven, 3000 Leuven, Belgium; <sup>e</sup> Centre for Economic Policy Research, London EC1V 0DX, United Kingdom; <sup>f</sup> IMEC Leuven, 3001 Leuven, Belgium

Contact: emmanuel.dhyne@nbb.be (ED); joep.konings@kuleuven.be (JK); jeroen.vandenbosch@kuleuven.be (JVdb); stijn.vanormelingen@kuleuven.be, https://orcid.org/0000-0002-5784-9713 (SV)

Received: April 25, 2019 Revised: February 28, 2020; June 22, 2020 Accepted: July 2, 2020 Published Online in Articles in Advance: November 24, 2020

https://doi.org/10.1287/isre.2020.0960

Copyright: © 2020 INFORMS

Abstract. This paper uses a new microdata set of business-to-business firm-level transactions in Belgium to construct a measure of information and communication technology (ICT) investment at the firm level, which we combine with the income statement of firms to analyze the impact of ICT on productivity. We find that a firm investing an additional euro in ICT increases value added by 1 euro and 35 cents on average. This marginal product of ICT investment increases with firm size and varies across sectors. Although we find substantial returns of ICT at the firm level, such returns are much lower at the aggregate level. This is due to underinvestment in ICT (ICT capital deepening is low) and misallocation of ICT investments.

History: D. J. Wu, Senior Editor; Jesse Bockstedt, Associate Editor Funding: Financial support from the Fonds Wetenschappelijk Onderzoek [FWO Grant G055914N] and KU Leuven (the “Econopolis Chair” program on firm growth and a Methusalem grant) is gratefully acknowledged. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2020.0960.

Keywords: information and communication technology • productivity • <sup>fi</sup>rm-level data

## 1. Introduction

The financial crisis of 2008 triggered a collapse in productivity growth, which has not caught up with its long-run trend since then. This seems at odds with the increased spread of information technology, artificial intelligence, and automation of the last couple of decades. This productivity puzzle has been widespread in Organisation for Economic Co-operation and Development (OECD) countries and more recently also in emerging economies (Syverson 2017). It seems that the Solow (1987) paradox, which refers to the disconnect between observed productivity statistics and the emergence of information technology, is more relevant than ever.

This paper investigates heterogeneity in the returns on information and communication technology (ICT) across firms, industries, and time and analyzes how granular (firm-level) channels affect the aggregate productivity numbers. We decompose aggregate gross domestic product (GDP) growth into various microchannels to understand from where the relatively low aggregate returns on ICT emerge, which is illustrated in Figure 1. In particular, GDP in a country can increase by using more production factors, such as labor or capital. We distinguish between ICT and non-ICT capital investments and investigate their return. Figure 1 also shows that GDP growth can occur as a result of productivity growth, which means that a country produces more goods with the same amount of labor and capital, and hence it is producing more efficiently. Such productivity growth can also happen when resources are allocated to its most productive use: This is what we call the reallocation effect. In this case, ICT capital contributes to aggregate productivity growth when it is invested in firms that benefit most from ICT.

We use a new and comprehensive microdata set of business-to-business (B2B) firm-level transactions in Belgium to construct a measure of ICT investments at the firm level, which we trace between 2002 and 2013. Our measure of ICT includes all domestic purchases and imports from ICT suppliers, which is an improvement to earlier research, mainly based on survey data of mostly large firms. Hence these tend to miss a large fraction of investments and firm heterogeneity (Brynjolfsson and Yang 1996, Dedrick et al. 2003). Furthermore, most of the literature identifies ICT as broad investments in office and computing equipment and therefore does not capture precisely the extent of technological change, which may also be induced by software and communications technology, especially in the last two decades.

We combine this newly constructed panel data on ICT investments with financial and operational information from the income statements of firms, which allows us to estimate the impact of ICT on firm-level productivity. To this end, we use a control function approach to estimate the output elasticity and marginal product of ICT capital. This approach deals with biases in estimating production functions related to the simultaneity of input and output decisions, measurement errors, and omitted variables (Brynjolfsson and Hitt 1995, Hempell 2005, Cardona et al. 2013). Another advantage of our data is that they cover all incorporated firms in the Belgian economy. Earlier work did not have access to such comprehensive data, which makes it harder to draw inferences about the impact of ICT on aggregate productivity growth (Brynjolfsson and Hitt 2000). We also exploit the cross section and time dimension of our panel data set and show the return on ICT across industries and time. The wide coverage of our data set enables us to contribute to the scarce evidence on differences in returns on ICT depending on the size of the firm (Bloom et al. 2010, Tambe and Hitt 2012). By exploiting information about the identity of the ICT supplier, we are able to split ICT purchases into information technology (IT) goods, IT services, communication goods, and communication services. We relate heterogeneity in the composition of ICT capital to reconcile the heterogeneity in returns on ICT across industries and the firm size distribution.

Figure 1. Decomposing GDP Growth  
![](/api/attachments/TZDMH2AG/fulltext/images/c5a1a5de444b69ae8e90716912140316d91cf0a222643009257887c4ef3e5b3c.jpg)

We confirm earlier findings that ICT capital effectively contributes to output and, more importantly, that there exist excess returns on ICT because ICT investment costs are lower than their gross returns. This effect is not only confined to the ICT producing industries but also to the ICT using industries. We find that large firms benefit more from ICT than small firms. This finding is not caused by differences in the composition of ICT capital, and it is robust to adding firm fixed effects, controlling for labor quality, decentralization, and management practices. To see whether these findings can be reconciled with the limited impact of ICT at the aggregate level, we compute aggregate productivity growth from our microlevel data set and use the decomposition introduced by Petrin and Levinsohn (2012), as summarized in Figure 1. Our results indicate that part of the observed productivity puzzle can be explained by two causes: (i) low ICT investments, especially by large firms, and (ii) misallocation of ICT investments.

We find these effects to be particularly apparent after the Great Recession of 2007-2009.

The rest of this paper is organized as follows. The next section summarizes the relevant literature. Section 3 discusses the various data sets used to construct ICT capital. Section 4 explains the econometric model and the control function approach that we use to estimate productivity, taking into account that ICT in vestment is an endogenous choice by the firm. Section 5 discusses the results, and Section 6 concludes.

## 2. Literature Review

Early research by Roach (1987) and Solow (1987) concluded that ICT appeared everywhere but in the productivity statistics. This so-called productivity paradox was resolved in various firm-level studies, among others by Brynjolfsson (1993), Lichtenberg (1995), Brynjolfsson and Hitt (1996), Aral et al. (2006), Mithas et al. (2012), and Aral et al. (2012). Review papers on the literature by Brynjolfsson and Hitt (2000), Melville et al. (2004), Cardona et al. (2013), and Biagi (2013) concluded that ICT has a positive effect on productivity, albeit with large heterogeneity in estimated returns on ICT across studies.

Several factors explain the large heterogeneity in estimated returns on ICT. The research design of studies explains about 35% of the variation in empirical estimates of ICT elasticities (Stiroh 2005). In particular, Sabherwal and Jeyaraj (2015) found that the return on ICT is estimated higher when primary data sources are used and sample sizes are larger. Kohli and Devaraj (2003) suggested to focus on gathering large panel data sets from primary sources and using productivity-based dependent variables to assess the payoff from ICT. The introduction of such a framework to evaluate the return on ICT is an important contribution of this paper.

Another challenge in ICT studies is related to measurement. Firms are typically not required to report ICT investments separately from other capital investments. Furthermore, ICT investments often require large complementary investments in the reorganization of work practices or the development of new business processes and worker skills. Brynjolfsson and Yang (1997) found that up to 9/10ths of the costs of computer capital are embodied in intangible assets. Bharadwaj (2000), Black and Lynch (2001), Bresnahan et al. (2002), and Aral and Weill (2007) showed that alignment between ICT investments and complementary workplace organization practices is important to realize profit and productivity gains from ICT. It is thus important to capture the complete extent of the ICT investment, which is typically not confined to hardware expenditures. To this end, this paper proposes a comprehensive ICT investment measure that captures both ICT goods and ICT services.

Because of the unavailability of ICT investment data in financial statements of firms, researchers are often restricted to survey data of selected samples of large firms.<sup>1</sup> This results in a selection bias in many firm-level studies and a lack of insights on heterogeneity in returns on ICT across countries, industries, and the firm size distribution (Tam 1998). Bloom et al. (2010) found no evidence of a size premium in returns on ICT, whereas Tambe and Hitt (2012) found that large firms benefit more from ICT. Note, however, that “small” firms in these samples are still relatively large. For example, a small firm in Tambe and Hitt (2012) is a non-Fortune 500 firm with an average value added of over \$500 million. In our data we cover the full range of the size distribution, including micro firms.

Although adequate data for estimating productivity is available in the financial statements of firms, there are various endogeneity issues that need to be accounted for to obtain unbiased estimates of ICT elasticities; see Stiroh (2005), Van Biesebroeck (2007), and Van Beveren (2012). State-of-the-art techniques to do so require relatively large panel data sets. This is probably why such methods are not frequently used in ICT studies. The only studies that do so are Bloom et al. (2010) and Bloom et al. (2012), who relied on the Olley and Pakes (1996) estimation procedure to obtain unbiased production function coefficients. This paper introduces more novel semiparametric estimation techniques by Ackerberg et al. (2015) and Collard-Wexler and De Loecker (2016) in the ICT literature.

Studies on the macroeconomic impact of ICT typically rely on industry-level data and strong assumptions such as constant returns to scale and competitive markets (Oliner and Sichel 2000, Jorgenson 2001, Stiroh 2002,

Jorgenson et al. 2008, van Ark et al. 2008). However, just as there is substantial heterogeneity within industries in firm size and productivity, there is firm heterogeneity in returns on ICT. Industry average returns on ICT hide this heterogeneity, whereas the aggregate impact of ICT also depends on which firms are investing in ICT. This could explain why most studies find large returns on ICT at the micro level but lower productivity gains at the macro level, es pecially in Europe (van Ark 2014). We compute aggregate growth and subsequently decompose it in its different microlevel foundations using the Petrin and Levinsohn (2012) decomposition.

## 3. Data

We combine different confidential micro data sets that were provided by the National Bank of Belgium. The first one covers a subset of B2B transactions data described in Dhyne et al. (2015). This data set is constructed from the yearly customer listing in the tax declarations of firms. In this customer listing, firms have to report the sales invoices per customer. We use the customer listing of all firms that are active in ICT producing and selling industries to calculate how much each of their customers has spent on ICT per year for the period 2002–2013. This approach is similar to Hitt et al. (2002), who retrieved a measure for IT investments from the customer listing of a large SAP supplier in the United States. Our data set is more comprehensive because it covers all ICT suppliers. We define ICT producers based on their four-digit primary Nomenclature of Economic Activities (NACE) sector code as shown in Table 1.<sup>2</sup> We differentiate between IT goods, IT services, communication goods and communication services within these purchases.<sup>3</sup> For example, if a firm makes a purchase from a supplier

Table 1. ICT Producing Industries

<table><tr><td>ICT type</td><td>NACE Rev. 2 code</td><td>Description</td></tr><tr><td rowspan="4">IT goods</td><td>2620</td><td>Manufacture of computers and peripheral equipment</td></tr><tr><td>4651</td><td>Wholesale of computers, computer peripheral equipment, and software</td></tr><tr><td>4741</td><td>Retail sale of computers, peripheral units, and software in specialized stores</td></tr><tr><td>5829</td><td>Other software publishing</td></tr><tr><td rowspan="7">IT services</td><td>6200</td><td>Computer programming, consultancy, and related activities</td></tr><tr><td>6201</td><td>Computer programming activities</td></tr><tr><td>6202</td><td>Computer consultancy activities</td></tr><tr><td>6203</td><td>Computer facilities management activities</td></tr><tr><td>6209</td><td>Other information technology and computer service activities</td></tr><tr><td>6311</td><td>Data processing, hosting, and related activities</td></tr><tr><td>6312</td><td>Web portals</td></tr><tr><td rowspan="3">Communication goods</td><td>2630</td><td>Manufacture of communication equipment</td></tr><tr><td>4652</td><td>Wholesale of electronic and telecommunications equipment and parts</td></tr><tr><td>4742</td><td>Retail sale of telecommunications equipment in specialized stores</td></tr><tr><td rowspan="4">Communication services</td><td>6110</td><td>Wired telecommunications activities</td></tr><tr><td>6120</td><td>Wireless telecommunications activities</td></tr><tr><td>6130</td><td>Satellite telecommunications activities</td></tr><tr><td>6190</td><td>Other telecommunications activities</td></tr></table>

Figure 2. Composition of ICT Investments by Sector Composition ICT investments

that has its primary activity in sector 2620 (Manufacture of computers and peripheral equipment), we classify this purchase as an investment in IT goods.

Although the interfirms transaction data set provides information on domestic ICT investments for all Belgian firms, it is possible in a small and open economy such as Belgium that firms import ICT. Therefore, we add import data at the product-firm level to capture ICT purchases from abroad. This data set is collected from the customs office for imports from outside the European Union (EU) and the Intrastat trade survey for imports from within the EU. We merge this data set based on the detailed Harmonized System (HS) eight-digit codes. Altogether, this results in an ICT investment data set that is representative for the entire Belgian population of incorporated firms for the period 2002–2013. Figure 2 shows that in most sectors, IT goods account for the largest share of ICT purchases, followed by IT services, communication services, and communication goods.

The third data set refers to the value-added tax declarations, which provide the total investments and intermediate input expenditures of the firm. By merging the investment data with the interfirm transactions data set, we can compute ICT and non-ICT investment flows, from which we construct ICT capital stocks and non-ICT capital stocks following the perpetual inventory method (PIM). Online Appendices C2 and C3 provide more information on the ICT purchases data and how the ICT and non-ICT capital stocks are constructed, and they present ICT intensity measures to show that our ICT measure behaves as expected. Online Appendix D2 contains various robustness checks on the choices that we make in this process.

![](/api/attachments/TZDMH2AG/fulltext/images/308607570daea428988028025f5586f780b7fa7a089f92b1f865a0b709823022.jpg)  
Notes. Own calculations are based on ICT purchases data. Industry average investment shares of firm average ICT purchases are shown.

The fourth data set consists of the annual company accounts with detailed financial and operational information, which we use to estimate productivity at the firm level. These data also report information on the education level of employees in the firm. All incorporated firms in Belgium are required to submit company accounts to the National Bank of Belgium. We have data for the whole private sector, excluding the financial sector for which the company accounts are not available under the same format as nonfinancial firms.

The final data set that we use is the annual FDI survey organized by the National Bank of Belgium, which serves as an input for the national accounts. It is a comprehensive survey of all inward and outward foreign direct investments in Belgium. Online Appendix C1 provides more information on how we merge all data sets together and construct the estimation sample.

Table 2 provides summary statistics of the main firm-level variables that we use in our analysis. The average firm employs 10 full-time equivalents in our sample, whereas the median firm employs 2 full-time workers. Average value added is equal to EUR 859,000, implying labor productivity in the average firm to be about EUR 86,000.<sup>4</sup> The average non-ICT and ICT capital stocks are equal to EUR 792,000 and EUR 75,000, respectively. This means that an employee in the average firm has about EUR 7,500 ICT capital to work with. The standard deviation is high, which indicates there are large differences at the firm level in the ICT capital stock. So the aggregate picture hides a lot of firm-level heterogeneity.

## 4. Empirical Framework

In order to estimate the return on ICT, we rely on a Cobb–Douglas production function. Tambe and Hitt (2012) adapted the standard production function by distinguishing between IT labor and non-IT labor. We take a similar approach and distinguish between ICT capital and non-ICT capital. By considering ICT capital as a separate input in the production function next to non-ICT capital, we follow Brynjolfsson and Hitt (1996, 2003), Dewan and

Table 2. Summary Statistics (in 2010 Euros)

<table><tr><td></td><td>Mean</td><td>Median</td><td>SD</td></tr><tr><td>Value Added (×1,000 €)</td><td>859</td><td>136</td><td>12,768</td></tr><tr><td>Non-ICT Capital (×1,000 €)</td><td>792</td><td>95</td><td>22,044</td></tr><tr><td>ICT Capital (×1,000 €)</td><td>75</td><td>5</td><td>2,212</td></tr><tr><td>Employment</td><td>10.4</td><td>2</td><td>135</td></tr><tr><td>Non-ICT Investment (×1,000 €)</td><td>145</td><td>17</td><td>3,506</td></tr><tr><td>ICT Investment (×1,000 €)</td><td>24</td><td>1.7</td><td>553</td></tr></table>

Note. Summaries are at the firm level, after taking averages over time per firm.

Kraemer (2000), Commander et al. (2011), and Bloom et al. (2012). The log-linearized Cobb–Douglas production function looks as follows:

$$
y _ {i t} = \beta_ {l} l _ {i t} + \beta_ {\mathrm{ICT}} k _ {i t} ^ {\mathrm{ICT}} + \beta_ {\mathrm{NICT}} k _ {i t} ^ {\mathrm{NICT}} + \omega_ {i t} + \epsilon_ {i t},\tag{1}
$$

in which the i and t subscripts refer to firm and year and small letters denote logs. The term $y _ { i t }$ refers to value added in firm i at time t; $l _ { i t } , k _ { i t } ^ { \mathrm { I C T } }$ , and $k _ { i t } ^ { \mathrm { { N I C T } } }$ refer to labor, the ICT capital stock, and the non-ICT capital stock, respectively; and $\omega _ { i t }$ is the firm’s total factor productivity (TFP) in firm i at time t. Econometricians do not observe a firm’s TFP, which gives rise to a simultaneity bias (Marschak and Andrews 1944); that is, firms typically adjust their capital and labor inputs in function of their productivity resulting in biased output elasticities. When highly productive firms invest more in ICT, the output elasticity $\beta _ { \mathrm { I C T } }$ would typically be overestimated with an ordinary least squares (OLS) estimation of Equation (1).

To account for such endogeneity, the literature puts forward several parametric and nonparametric approaches (Van Biesebroeck 2007, Van Beveren 2012). In practice, the most often used solutions are firm fixed effects, first differences, and semiparametric estimation. Estimating Equation (1) with firm fixed effects or in first differences results in unbiased estimates of the output elasticities if firm-level productivity is constant over time. However, these methods do not control for firm-specific productivity shocks and can lead to a substantial downward bias in the coefficient estimates of variables that display substantial serial correlation (Griliches and Hausman 1986). For this reason, the use of semiparametric estimators is typically preferred when sample sizes are sufficiently large. Semiparametric estimation of production functions was introduced by Olley and Pakes (1996) and further extended by Levinsohn and Petrin (2003) and Ackerberg et al. (2015). The idea is that firms signal their productivity, which is known to the firm but unknown to the econometrician, through other decisions such as investments and material purchases. This allows to proxy for unobserved productivity with a control function. Including this control function then allows to obtain unbiased production function coefficients. In Online Appendix B1 we discuss in more detail the approach we follow—in particular, the generalized method of moments (GMM) control function approach of Ackerberg et al. (2015) and a novel GMM estimator recently introduced by Collard-Wexler and De Loecker (2016) that also controls for measurement error in the capital stock. In Online Appendix D1 we add robustness checks to allow for endogenous productivity growth, alternative data generating processes, and mismeasurement in the capital stocks.

Using the output elasticities, we compute the marginal product of ICT capital as in Brynjolfsson and Hitt (1996) and Tambe and Hitt (2012), which is equal to the output elasticity of ICT capital multiplied by the ratio of output to ICT capital:

$$
M P _ {K ^ {\mathrm{ICT}}} = \frac {\partial Y}{\partial K ^ {\mathrm{ICT}}} = \frac {\partial Y}{\partial K ^ {\mathrm{ICT}}} \frac {K ^ {\mathrm{ICT}}}{Y} \frac {Y}{K ^ {\mathrm{ICT}}} = \beta_ {\mathrm{ICT}} \frac {Y}{K ^ {\mathrm{ICT}}} = \frac {\beta_ {\mathrm{ICT}}}{\frac {K ^ {\mathrm{ICT}}}{Y}}.\tag{2}
$$

We calculate the ICT capital input share for each observation and take the mean of the resulting distribution after winsorizing at the 1% level to avoid biases from outliers.

## 5. Results

## 5.1. Baseline Results

Table 3 reports production function estimates for the private sector as a whole. All specifications control for industry and year fixed effects. The first column shows OLS results, the second and third columns report results including firm fixed effects and first differences estimates, respectively. Columns (5)

Table 3. Results Private Sector (NACE 1–82)

<table><tr><td>Value-added prod. function</td><td>OLS</td><td>Firm fixed effects</td><td>First differences</td><td>ACF</td><td>CWDL</td></tr><tr><td>Labor</td><td>0.6739***(0.0015)</td><td>0.5013***(0.0021)</td><td>0.3376***(0.0022)</td><td>0.6226***(0.0038)</td><td>0.4573***(0.0058)</td></tr><tr><td>Non-ICT Capital</td><td>0.1846***(0.0013)</td><td>0.1170***(0.0015)</td><td>0.0902***(0.0016)</td><td>0.2111***(0.0055)</td><td>0.4467***(0.0286)</td></tr><tr><td>ICT Capital</td><td>0.1079***(0.0009)</td><td>0.0695***(0.0010)</td><td>0.0599***(0.0011)</td><td>0.1151***(0.0032)</td><td>0.1387***(0.0313)</td></tr><tr><td>No. of observations</td><td>1,044,353</td><td>1,044,353</td><td>870,626</td><td>867,867</td><td>826,685</td></tr><tr><td>No. of firms</td><td>137,504</td><td>137,504</td><td>137,504</td><td>137,504</td><td>137,504</td></tr></table>

Notes. Standard errors are clustered at the firm level. The estimation sample is identical in number of firms. The number of observations is lower due to missing lags/instruments for some observations in one/multiple years for a firm in the First differences, ACF and CWDL estimator. All estimations include year fixed effects and two-digit industry fixed effects, except for columns 2 and 3 where the industry fixed effects are absorbed by the firm fixed effects and first differences respectively. \*\*\*Significant at the 1% level

and (6) report the results of two GMM estimators: the Ackerberg, Caves and Frazer control function estimator (ACF) and the Collard-Wexler and De Loecker approach $( \mathrm { C W D L } ) . ^ { 6 }$ For Table 3, we limit the estimation sample to the firms that we have sufficient information on to use in each estimator.

Similar to Brynjolfsson and Hitt (1995), we observe that the magnitude of the ICT capital output elasticity drops roughly 50% when adding firm fixed effects or estimating first differences. Cross-sectional firm heterogeneity is thus important in explaining the return on ICT capital. This is consistent with the idea that differences in ICT capital also reflect other unobserved persistent firm characteristics such as innovativeness, management practices, and workplace organization (Bresnahan et al. 2002). Another explanation is provided by Griliches and Hausman (1986), who noted that when a variable is highly serially correlated over time, fixed effects regressions can introduce a substantial downward bias in the coefficient estimates. The GMM estimators in columns (5) and (6) are expected to control for these biases. The ACF estimator controls for the potential endogeneity of inputs, most relevant for a variable input such as labor. As expected, the coefficient on labor drops. The ICT capital coefficient is comparable to the OLS one. Note that it is difficult to determine a priori the bias in the OLS estimate for the ICT capital coefficient. First, there can be an endogeneity bias if ICT is correlated with unobserved productivity, but second, the estimate is also affected by biases in other variables coefficients that spill over to the ICT capital coefficient. As expected, correcting for measurement error in the capital stocks with the CWDL estimator in column (6) increases the capital coefficients.<sup>7</sup> For the remainder of this paper, we proceed with the ACF estimator as this is the workhorse model in the productivity literature. The ICT capital output elasticity is estimated around 0.11, so increasing the ICT capital stock with 1% increases value added on average with 0.11%.<sup>8</sup> This is higher than in earlier work; see Table A-1 in Online Appendix A for a comparison with earlier studies.

Although output elasticities have the advantage of being independent of the units in which outputs and inputs are measured, they cannot be easily compared with studies on other samples that have different average levels of ICT investments or other factor input shares. Therefore, we follow Tambe and Hitt (2012) and Brynjolfsson and Hitt (1996) and compute the marginal product of the inputs. The ICT capital input share $\frac { K ^ { \mathrm { I C T } } } { V A }$ is on average 8.53% of value added, comparable to Brynjolfsson and Hitt (1995), who found an input share of 9.35% for IT capital and IT labor together. Based on the estimated output elasticities of

ICT capital, the marginal product of ICT capital is 1.35, or

$$
M P _ {K ^ {\mathrm{ICT}}} = \beta_ {\mathrm{ICT}} \left(\frac {K ^ {\mathrm{ICT}}}{Y}\right) ^ {- 1} = \frac {0 . 1 1 5 1}{0 . 0 8 5 3} = 1. 3 5.
$$

Thus, investing an additional euro in ICT capital increases value added on average by 1 euro and 35 cents. For non-ICT capital and labor, the input shares are 1.17 and 0.63, respectively, so the marginal product of non-ICT capital is EUR 0.18 $( M P _ { K ^ { \mathrm { N I C T } } } =$ $\frac { 0 . 2 1 1 1 } { 1 . 1 6 5 9 } = 0 . 1 8 )$ , and the marginal product of labor is EUR 0.99 $\begin{array} { r } { ( M P _ { \mathrm { L } } = \frac { 0 . 6 2 2 6 } { 0 . 6 2 9 1 } = \bar { 0 } . 9 9 ) . ^ { 9 } } \end{array}$ Our estimates are higher than those of Brynjolfsson and Hitt (1996), who found the marginal product of IT capital to be 0.81 for a sample of 1,121 large U.S. firms. The marginal product tells us how much the last dollar of ICT capital contributes to value added. Inframarginal investments generally have a higher rate of return, so our results indicate that the average return on investing in ICT capital is even higher than EUR 1.35. However, the net rate of return of ICT capital also depends on the user costs that are associated with maintaining ICT capital and the associated large adjustment costs that have to be covered when investing in ICT (Stiroh 2005).<sup>10</sup> According to EU KLEMS data (Jager¨ 2017 and Stehrer et al. 2019), ICT capital depreciates at a rate of 31.5% per year. Non-ICT capital depreciation rates are lower and estimated be tween 5% and 15% per year. As a result, the net rate of return on ICT capital is about $1 . 3 5 - 0 . 3 1 5 \approx 1 . 0 4 ,$ whereas the net rate of return of non-ICT capital is about $0 . 1 8 - 0 . 1 0 \approx 0 . 0 8$ . Table 4 shows that our results are robust to various alternative modeling approaches.

Altogether, our results indicate excess returns on ICT capital. Although part of this return on ICT is required to cover adjustment costs and unmeasured complementary assets, an increase in ICT capital would result in increased output and growth in (measured) multifactor productivity. This finding is, of course, not new; see Biagi (2013) for an overview of the literature on ICT and productivity. Yet it is valuable to assess the return on ICT outside the United States with recent, more detailed data and robust estimators. More important, these baseline results hide a lot of heterogeneity as shown in Figure A-1 in Online Appendix A. In the remainder of the paper, we disentangle the return on ICT across industries, firm size, and time. We also show how aggregate output and productivity growth is affected by ICT using a decomposition exercise.

## 5.2. Industry Heterogeneit

As pointed out by Tambe and Hitt (2012), limited availability of data in earlier work did not allow for engaging in sectoral comparisons. Our data contain information on firm-level ICT investments for the entire nonfinancial private sector. Table 5 shows splitsample results for manufacturing and services sectors as a first step in disentangling this heterogeneity.

Table 4. Robustness Checks

<table><tr><td>Robustness check</td><td>Potential concern</td><td>Robustness analysis</td><td>Results</td></tr><tr><td>R. 1</td><td>Entry and exit dynamics could affect the ICT output elasticity.</td><td>Estimate the production function on a balanced sample.</td><td>✓</td></tr><tr><td>R. 2</td><td>Productivity could evolve endogenously with ICT investments.</td><td>Include ICT investments in the law of motion of productivity.</td><td>✓</td></tr><tr><td>R. 3</td><td>Timing assumptions on the moment ICT investments become productive.</td><td>Use current/lagged instruments for ICT capital.</td><td>✓</td></tr><tr><td>R. 4</td><td>ICT capital stock can be constructed in various ways.</td><td>Estimate initial capital stocks from aggregated ICT intensity measures.</td><td>✓</td></tr><tr><td>R. 5</td><td>Sensitivities in ICT investments could spill over to non-ICT investments.</td><td>Use ICT capital with PIM, non-ICT capital as the residual book value of tangible fixed assets or as the total book value of tangible fixed assets.</td><td>✓</td></tr><tr><td>R. 6</td><td>There are high ICT purchases compared with total investments.</td><td>Drop observations for which ICT purchases are larger than total investments.</td><td>✓</td></tr><tr><td>R. 7</td><td>ICT capital depreciation rate could be too conservative.</td><td>Assume no depreciation for ICT capital.</td><td>✓</td></tr></table>

Note. The results of these robustness checks are included in Online Appendix D.

As in Kudyba and Diwan (2002), we find that the output elasticity of ICT capital in the manufacturing and services sector is very similar. However, the manufacturing industries have lower ICT intensity than the services industries, as measured by the ratio of ICT capital to value added. As a result, the marginal product of ICT capital is higher for manufacturing industries more precisely: 1.58 in the manufacturing sector compared with 1.17 in the services sector. The marginal products of non-ICT capital and labor are 0.21 and 0.94 for the manufacturing sector and 0.16 and 1.00 for the services sector, respectively.<sup>11</sup> There are two possible explanations for such a high marginal product of ICT capital in the manufacturing industry: Either the user costs and adjustment costs from increasing ICT capital are large such that firms refrain from investing in ICT capital or there is a market failure that results in manufacturing firms underinvesting in ICT capital. To gain a deeper understanding of industry heterogeneity, we estimate our production function at a more disaggregated level. Table 6 and Table A-6 in Online Appendix A provide further details on differences in the output elasticity and the marginal product of ICT capital across industries.<sup>12</sup>

In the manufacturing sector, spending an additional euro on ICT has a larger gross return in hightech industries. The difference between high-tech and other manufacturing is primarily driven by a higher output elasticity of ICT capital in high-tech industries, whereas the ICT input shares do not differ much between high-tech manufacturing and other manufacturing. Table A-6 in Online Appendix A estimates the return on ICT at the more disaggregated two-digit level. Within manufacturing, the gross return on ICT is lowest in the printing industry and highest in manufacturing of metal. Outside manufacturing, we find that the marginal product of ICT capital is high for utilities and construction industries and in general low in services industries as a result of relatively high ICT input shares. For the services industries, the output elasticity of ICT capital is highest for the information and communication industries. This is consistent with Bosworth and Triplett (2007), who showed that productivity growth from IT capital within the services sector was highest for these industries. Yet the ICT input share is also highest in the information and communication industries, resulting in a marginal product of ICT that is relatively low.

Abstracting from potential discrepancies in adjustment costs across industries, creating productivity growth through investments in ICT is hardest in industries that have a relatively low marginal product of ICT capital. Our results suggest that it is easier for manufacturing firms to increase productivity by investing in ICT compared with services industries. Table 6 shows that this is primarily due to relatively high ICT capital stocks compared with the added value of firms in services industries.

Table 5. Results Manufacturing (NACE Codes 10–33) and Services (NACE Codes 45–82)

<table><tr><td>Value-added production function</td><td>Manufacturing</td><td>Services</td></tr><tr><td>Labor</td><td>0.6509***(0.0124)</td><td>0.6153***(0.0046)</td></tr><tr><td>Non-ICT Capital</td><td>0.2249***(0.0148)</td><td>0.1995***(0.0071)</td></tr><tr><td>ICT Capital</td><td>0.1212***(0.0071)</td><td>0.1204***(0.0046)</td></tr><tr><td>No. of observations</td><td>122,415</td><td>570,484</td></tr><tr><td>No. of firms</td><td>18,451</td><td>112,263</td></tr></table>

Notes Standard errors are clustered at the firm level. Results are obtained from the ACF estimator. Tables A-3 and A-4 in Online Appendix A show results for alternative estimators. All specifications include industry and year fixed effects.  
\*\*\*Significant at the 1% level.

Table 6. Results per Industry

<table><tr><td>Industry (NACE codes)</td><td>No. of firms</td><td>Labor</td><td>Non-ICT Capital</td><td>ICT Capital</td><td>ICT Input Share</td><td>Marginal Product ICT</td></tr><tr><td>Agriculture, forestry and fishing (1–3)</td><td>2,230</td><td>0.43</td><td>0.41</td><td>0.06</td><td>0.03</td><td>1.89</td></tr><tr><td>High-tech manufacturing (21, 26, 30)</td><td>2,509</td><td>0.73</td><td>0.16</td><td>0.15</td><td>0.09</td><td>1.65</td></tr><tr><td>Other manufacturing (10–33, except high-tech)</td><td>15,942</td><td>0.64</td><td>0.24</td><td>0.11</td><td>0.07</td><td>1.52</td></tr><tr><td>Utilities (35–39)</td><td>823</td><td>0.55</td><td>0.31</td><td>0.09</td><td>0.04</td><td>2.43</td></tr><tr><td>Construction (41–43)</td><td>30,751</td><td>0.64</td><td>0.24</td><td>0.09</td><td>0.04</td><td>2.38</td></tr><tr><td>Wholesale and retail (45–47)</td><td>51,914</td><td>0.60</td><td>0.19</td><td>0.15</td><td>0.10</td><td>1.45</td></tr><tr><td>Transportation and storage (49–53)</td><td>8,386</td><td>0.65</td><td>0.23</td><td>0.07</td><td>0.04</td><td>1.85</td></tr><tr><td>Accommodation and food service (53–56)</td><td>18,025</td><td>0.60</td><td>0.25</td><td>0.06</td><td>0.05</td><td>1.16</td></tr><tr><td>Information and communication (58–63)</td><td>1,389</td><td>0.64</td><td>0.15</td><td>0.19</td><td>0.21</td><td>0.93</td></tr><tr><td>Financial and insurance (64–66)</td><td>2,217</td><td>0.68</td><td>0.18</td><td>0.12</td><td>0.14</td><td>0.86</td></tr><tr><td>Real estate (68)</td><td>3,602</td><td>0.50</td><td>0.34</td><td>0.12</td><td>0.14</td><td>0.83</td></tr><tr><td>Professional, scientific and technical. activities (69–75)</td><td>18,147</td><td>0.63</td><td>0.15</td><td>0.13</td><td>0.17</td><td>0.77</td></tr><tr><td>Administrative and support activities (77–82)</td><td>8,583</td><td>0.64</td><td>0.23</td><td>0.12</td><td>0.13</td><td>0.96</td></tr></table>

Notes. Results obtained from the ACF estimator. The production functions include industry and year fixed effects. Standard errors are clustered at the firm level. All output elasticities are significant at the 1% level, except for utilities industries, where results are significant at the 10% level The number of observations for mining and quarrying firms is low; therefore these are omitted.

To improve our understanding in the heterogeneity in gross marginal returns on ICT across industries, we further exploit our B2B data. As detailed in Table 1, we can classify the type of ICT investments based on the primary industry code of the ICT seller. In Table 7, we regress the marginal product of ICT capital on the share of IT goods, IT services, communication goods, and communication services.

Wilson (2009) showed that the marginal product of communication goods is lower than the marginal product of hardware and software. Controlling for industry and year fixed effects, our results indicate that higher investments in communication goods and services have no statistically significant effect on the marginal product of ICT capital, which is not surprising given the small share of communication goods and services investments in total ICT investments as shown in Figure 1. We find that the marginal product of ICT capital is higher (lower) in industries where firms allocate more of their ICT investments to IT goods (services). With regard to realizing productivity growth through ICT investments, this implies that investing in IT goods is more beneficial than investing in IT services.

## 5.3. Firm Size Heterogeneity

Most of the literature has focused on large firms, often using survey data, but it is unclear whether these earlier findings can be generalized to the population of small firms, which represent the bulk of the economy. Tambe and Hitt (2012) indicated this to be a major shortcoming of the literature. To the best of our knowledge, only Tambe and Hitt (2012), Hyatt and Nguyen (2010), and Bloom et al. (2010) investigated whether returns on ICT are related to firm size. Whereas Tambe and Hitt (2012) found that large firms benefit more from ICT, Hyatt and Nguyen (2010) found the opposite, and Bloom et al. (2010) did not find differences in returns on ICT between small and large firms. The average number of employees in the study of Tambe and Hitt (2012) is more than 10,000 employees, whereas in Hyatt and Nguyen (2010) and Bloom et al. (2010), this is 237 and 400 employees, respectively. Figure A-2 of Online Appendix A shows that our data set covers the firm size distribution more exhaustively. Mean and median employment in our data set is 10.4 and 2 employees, respectively, but our sample also contains very large firms with more than 10,000 employees. This allows us to more adequately test whether a size premium exists in returns on ICT. We divide the population of firms into seven bins according to firm size and reestimate the production function to retrieve a size bin–specific output elasticity and marginal product of ICT in Table 8.<sup>13</sup>

Table 7. Explaining Industry Heterogeneity

<table><tr><td></td><td> $MP^{ICT}$ </td><td> $MP^{ICT}$ </td><td> $MP^{ICT}$ </td><td> $MP^{ICT}$ </td></tr><tr><td>Share of IT Goods</td><td>0.0101*(0.0059)</td><td></td><td></td><td></td></tr><tr><td>Share of IT Services</td><td></td><td>-0.0146**(0.0058)</td><td></td><td></td></tr><tr><td>Share of Communication Goods</td><td></td><td></td><td>-0.0022(0.0065)</td><td></td></tr><tr><td>Share of Communication Services</td><td></td><td></td><td></td><td>0.0094(0.0085)</td></tr><tr><td>No. of observations</td><td>816</td><td>816</td><td>816</td><td>816</td></tr></table>

Notes. Standard errors are clustered at the NACE two-digit level. We have 68 two-digit industry codes for 12 vears, resulting in 816 observations. The dependent variable is the log linearized marginal product of ICT capital, obtained from the NACE two-digit level output elasticities in Table A-6 and the cost share of ICT averaged by two-digit code and year. The independent variables are the ICT-type investment shares as defined in Table 1 and Figure 2, rescaled between 0 and 100, and also averaged by two-digit code and year. FE, fixed effects. All specifications include industry and year fixed effects.  
\*\*Significant at the 5% level; \*significant at the 10% level.

In Section 5.1, we found an average ICT input share of 0.0853 and a marginal product of ICT capital equal to 1.35 for the entire private sector. Table 8 shows that there is heterogeneity in firm size underlying these results. Although there is no clear correlation between firm size and the labor and non-ICT capital coefficients, there is a positive correlation between the output elasticity of ICT capital and firm size. Because the ICT input share is relatively constant across the firm size distribution, the marginal product of ICT capital increases with firm size. In line with the findings of Tambe and Hitt (2012), we find that large firms benefit more from ICT. This upward trend in the marginal product of ICT capital also appears at more disaggregated levels of the firm size distribution; see Figure A-3 in Online Appendix A.

It is possible that the ICT capital coefficient is picking up omitted complementary intangibles. For example, management practices are positively related to ICT intensity (Bloom et al. 2012, 2014). As large firms are typically better managed (Bloom and Van Reenen 2007), differences in returns across the firm size distribution could partly represent unmeasured management quality. If this is not controlled for, the estimated return on ICT capital could be biased upward. Although we use state-of-the-art techniques to control for unobserved productivity in estimating the output elasticity of ICT capital, these only control for management insofar comprised in firm productivity. Under the assumption that management quality is fixed over time, a fixed effects model allows to validate the robustness of our results.<sup>14</sup> Table 9 shows the output elasticities of ICT capital for each firm size bin, with firms that have less than five employees as a reference category, with and without firm fixed effects.

Without accounting for firm fixed effects, the return on ICT capital is significantly higher for each size bin compared with the size bin just below. After accounting for firm fixed effects, we only find a significantly higher output elasticity of ICT capital for firms with more than 100 employees. This result implies that increasing ICT capital increases output more in the subgroup of firms with more than 100 employees than in smaller firms. The result that firms with less than 100 employees only have a higher output elasticity without accounting for firm fixed effects suggests that our ICT capital coefficient could indeed reflect unmeasured complementary assets to a certain extent. Table 10 further investigates whether the firm size premium in the return on ICT can be attributed to management, decentralization, or skilled labor.

Bloom et al. (2012) found that U.S. firms have a higher output elasticity on ICT capital than European firms and that this difference in the return on ICT becomes statistically insignificant after controlling for people management. To test whether better peo ple management in large firms explains the output elasticity premium of ICT capital in large firms, we exploit data on management practices that we

Table 8. Results per Size Bin

<table><tr><td>Firm size</td><td>No. of firms</td><td> $\beta_{l}$ </td><td> $\beta_{\text{NICT}}$ </td><td> $\beta_{\text{ICT}}$ </td><td>ICT Input Share</td><td>Marginal Product ICT</td></tr><tr><td>≤5 employees</td><td>124,301</td><td>0.4333</td><td>0.2292</td><td>0.0952</td><td>0.0894</td><td>1.2991</td></tr><tr><td>6–10 employees</td><td>17,959</td><td>0.7659</td><td>0.1556</td><td>0.0705</td><td>0.0812</td><td>1.0436</td></tr><tr><td>11–25 employees</td><td>13,156</td><td>0.8085</td><td>0.1230</td><td>0.0877</td><td>0.0796</td><td>1.3078</td></tr><tr><td>26–50 employees</td><td>5,246</td><td>0.8500</td><td>0.1068</td><td>0.1051</td><td>0.0791</td><td>1.5702</td></tr><tr><td>51–100 employees</td><td>2,098</td><td>0.8167</td><td>0.0841</td><td>0.1152</td><td>0.0798</td><td>1.6943</td></tr><tr><td>101–250 employees</td><td>1,226</td><td>0.8437</td><td>0.1012</td><td>0.1725</td><td>0.0817</td><td>2.4453</td></tr><tr><td>&gt;250 employees</td><td>680</td><td>0.7403</td><td>0.1321</td><td>0.1959</td><td>0.0833</td><td>2.6783</td></tr></table>

Notes. The results in this table are from an ACF estimator. The production functions include industry and year fixed effects. Standard errors are clustered at the firm level, and all output elasticities are significant at the 1% level, except in the size bin of more than 250 employees, where the ICT capital coefficient is significant at the 18% level because of a small number of observations in this size category.

Table 9. Results for Different Size Bins with Fixed Effects

<table><tr><td>Value-added production function</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>ICT Capital</td><td>0.1095***(0.0009)</td><td>0.0940***(0.0010)</td><td>0.0722***(0.0010)</td><td>0.0691***(0.0011)</td></tr><tr><td>ICT Capital × ≤5 employees</td><td></td><td>/</td><td></td><td>/</td></tr><tr><td>ICT Capital × 6–10 employees</td><td></td><td>-0.0061***(0.0018)</td><td></td><td>-0.0075***(0.0014)</td></tr><tr><td>ICT Capital × 11–25 employees</td><td></td><td>0.0045***(0.0021)</td><td></td><td>-0.0068***(0.0018)</td></tr><tr><td>ICT Capital × 26–50 employees</td><td></td><td>0.0109***(0.0031)</td><td></td><td>-0.0075***(0.0026)</td></tr><tr><td>ICT Capital × 51–100 employees</td><td></td><td>0.0254***(0.0048)</td><td></td><td>0.0046(0.0042)</td></tr><tr><td>ICT Capital × 101–250 employees</td><td></td><td>0.0495***(0.0074)</td><td></td><td>0.0109*(0.0062)</td></tr><tr><td>ICT Capital × &gt;250 employees</td><td></td><td>0.0747***(0.0112)</td><td></td><td>0.0266***(0.0096)</td></tr><tr><td>No. of observations</td><td>1,083,534</td><td>1,083,534</td><td>1,083,534</td><td>1,083,5345</td></tr><tr><td>No. of firms</td><td>164,666</td><td>164,666</td><td>164,666</td><td>164,666</td></tr><tr><td>Firm fixed effects</td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr></table>

Notes. Standard errors are clustered at the firm level. Models (1) and (3) are the standard OLS production function with and without firm fixed effects. Models (2) and (4) are the same that Bloom et al. (2010) used to infer whether there is a size premium in returns on ICT capital: $y _ { i t } = \beta _ { l } l _ { i t } + \beta _ { I T } k _ { i t } ^ { \mathrm { I C T } } +$ $\beta _ { N I T } k _ { i t } ^ { \mathrm { \scriptsize { N I C T } } } + \beta ^ { S ^ { j } } s _ { i t } ^ { j } + \beta _ { I T } ^ { S ^ { j } } ( k _ { i t } ^ { \mathrm { \scriptsize { I C T } } } \times s _ { i t } ^ { j } ) + Z _ { i t } + \epsilon _ { i t }$ with $\dot { s } _ { i t } ^ { j }$ size bin dummies, and $\bar { Z _ { i t } } ^ { \bar { } }$ the vector of year and industry controls. We show only $\beta _ { \mathrm { I C T } }$ and $\beta _ { \mathrm { I C T } } ^ { S ^ { j } } ,$ which measure the effect of ICT capital for firms with fewer than five employees and the additional effect according to the firm’s size respectively./, no coefficient estimate for this variable.  
\*\*\*Significant at the 1% level; \*significant at the 10% level.

collected following the format of the World Management Survey in 163 Belgian manufacturing firms.<sup>15</sup> Estimating a production function including the people management score does not change the finding that large firms benefit more from ICT. Neither does our findings change when adding the overall management score. The firm size premium on ICT does not appear to be reflecting differences in management practices.

Table 10. Large Firms Benefit More from ICT

<table><tr><td>Value-Added production function</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Labor</td><td>0.3922***(0.0051)</td><td>0.5411***(0.1180)</td><td>0.5392***(0.1191)</td><td>0.3924***(0.0051)</td><td>0.3457***(0.0084)</td></tr><tr><td>Non-ICT capital</td><td>0.1198***(0.0015)</td><td>0.1059***(0.0340)</td><td>0.1083***(0.0339)</td><td>0.1198***(0.0015)</td><td>0.1415***(0.0023)</td></tr><tr><td>ICT capital</td><td>0.0584***(0.0012)</td><td>-0.0039(0.0478)</td><td>-0.0033(0.0487)</td><td>0.0584***(0.0012)</td><td>0.0806***(0.0019)</td></tr><tr><td>ICT capital × Size</td><td>0.0126***(0.0006)</td><td>0.0223**(0.0094)</td><td>0.0226***(0.0010)</td><td>0.0126***(0.0006)</td><td>0.0110***(0.0010)</td></tr><tr><td>General Management</td><td></td><td>0.0741(0.0646)</td><td></td><td></td><td></td></tr><tr><td>People management</td><td></td><td></td><td>0.0424(0.0526)</td><td></td><td></td></tr><tr><td>Decentralization</td><td></td><td></td><td></td><td>0.0946***(0.0157)</td><td></td></tr><tr><td>Skilled labor</td><td></td><td></td><td></td><td></td><td>0.0228***(0.0042)</td></tr><tr><td>No. of observations</td><td>1,083,534</td><td>1,699</td><td>1,699</td><td>1,083,534</td><td>602,482</td></tr><tr><td>No. of firms</td><td>164,666</td><td>163</td><td>163</td><td>164,666</td><td>137,548</td></tr><tr><td>Firm fixed effects</td><td>YES</td><td>NO</td><td>NO</td><td>YES</td><td>YES</td></tr></table>

Notes. Standard errors are clustered at the firm level. The World Management Survey is a cross section, so firm fixed effects cannot be included in that estimation. The number of observations in the regression with skilled labor is lower, as we only observe this information for a subset of firms since 2008.  
\*\*\*Significant at the 1% level; \*\*significant at the 5% level.

Acemoglu et al. (2007) showed that decentralized firms are more productive and that this effect is stronger in ICT-intensive industries. To test whether decentralization plays a role in explaining the productivity returns of ICT capital, we estimate a production function that includes a dummy indicating whether a firm has inward or outward foreign direct investments (FDIs).<sup>16</sup> The coefficient on the interaction between firm size and ICT capital is not affected by including the FDI dummy, indicating that large firms do not benefit more from ICT because of higher decentralization.

Bresnahan et al. (2002) discussed the process through which ICT affects labor demand toward more skilled labor. Goos et al. (2014) also showed that there is a shift toward skilled jobs as a result of the surge in ICT investments. To investigate whether skilled labor is at the origins of the ICT output elasticity premium in large firms, we exploit information on the education level of employees. We add the share of highly educated employees to the model as a proxy for skilled labor and find that the interaction coefficient between employment and ICT capital remains unaffected. The same conclusion holds when we add wages, measured by the ratio of the wage bill to the number of employees, to proxy for labor quality as in Broersma et al. (2003). Differences in the degree of skilled labor are also not the reason why large firms benefit more from ICT.

Bloom et al. (2014) showed that information technology and communication technology serve different uses. Communication technology investments result in a reduction of employee autonomy, because decisions can be passed to the center of the firm. Information technology investments have the opposite effect, facilitating employee decision making. We exploit our B2B data to infer how centralized decision making takes place in firms by investigating the differences in the investment shares of ICT types across the firm size distribution. Figure 3 disentangles ICT investments, which are the basis of the ICT capital stocks, for the different size groups.

The share of IT goods and communication services in ICT investments—and hence in ICT capital—decreases with firm size, whereas the share of IT services and communication goods increases with firm size. This pattern indicates opposing forces with regard to the level of decision making in the firm: IT goods investments push the level of decision making down; investments in communication goods are likely to push the level of decision making up. Although there is no clear relationship between the level of decision making and the size premium in returns of ICT capital, Figure 3 does show a clear decrease in the share of IT goods and an increase in IT services with firm size.

![](/api/attachments/TZDMH2AG/fulltext/images/0c9bc583b8a68838b81a7455de6bbd7dba8400d5bf0823950bc9b7c473cf4221.jpg)  
Note. Average industry shares after averaging the investment shares at the firm level are shown.

It is important to note that large firms are also more likely to provide IT and communication services in house instead of buying them externally. Because inhouse ICT developments are not accounted for in our ICT investment data, we could possibly underestimate the ICT input share in large firms, leading to an upward bias in the marginal product estimate in large firms. There are two reasons why this phenomenon is unlikely to affect our results. First, Figure 3 shows that the share of IT services increases instead of decreases with firm size. Second, this argument does not hold for the provision of ICT goods, as these are unlikely to be produced in house. When measuring excess returns using only ICT goods to construct the capital stock, we get a similar picture as before (see Figures A-4 and A-5 in Online Appendix A).

## 5.4. Heterogeneity over Time

We investigated the heterogeneity in returns on ICT in the cross section of our unique panel data set by looking at variation in the return on ICT across industries and across the firm size distribution. In the remainder of the paper, we exploit the time dimension of our data by looking at the evolution in the marginal product of ICT capital and by investigating how ICT capital contributes to aggregate output and productivity growth in Section 5.5. Similar to earlier analyses, we show in Table 11 a split-sample estimation by year.

There is no clear trend in the labor and non-ICT capital elasticities over time, but there is a clear downward trend in the output elasticity of ICT capital while the ICT input share increases over time. As a result, the marginal product of ICT capital decreases over time. Whereas spending an additional euro on ICT had a gross return of EUR 1.58 in 2005, this was almost halved by 2013 to EUR 0.85.<sup>17</sup> A potential explanation for the downward trend is that it takes some time before ICT innovations spread out to other firms. Once they do, the premium of ICT investments drops over time.<sup>18</sup> In Figure 4, we investigate the heterogeneity in returns on ICT over time further and exploit our B2B data to show the composition of ICT investments over time.

Table 11. Results by Year

<table><tr><td>Year</td><td>No. of firms</td><td> $\beta_l$ </td><td> $\beta_{NICT}$ </td><td> $\beta_{ICT}$ </td><td>ICT Input Share</td><td>Marginal Product ICT</td></tr><tr><td>2003</td><td>77,277</td><td>0.6519</td><td>0.1962</td><td>0.1049</td><td>0.0667</td><td>1.5731</td></tr><tr><td>2004</td><td>80,055</td><td>0.6338</td><td>0.1958</td><td>0.1544</td><td>0.0716</td><td>2.1557</td></tr><tr><td>2005</td><td>86,205</td><td>0.6285</td><td>0.2107</td><td>0.1218</td><td>0.0771</td><td>1.5785</td></tr><tr><td>2006</td><td>90,977</td><td>0.6180</td><td>0.2147</td><td>0.1160</td><td>0.0797</td><td>1.4545</td></tr><tr><td>2007</td><td>94,577</td><td>0.6250</td><td>0.2013</td><td>0.1281</td><td>0.0818</td><td>1.5667</td></tr><tr><td>2008</td><td>95,029</td><td>0.6086</td><td>0.2239</td><td>0.1131</td><td>0.0862</td><td>1.3123</td></tr><tr><td>2009</td><td>96,160</td><td>0.6082</td><td>0.2187</td><td>0.1052</td><td>0.0917</td><td>1.1471</td></tr><tr><td>2010</td><td>96,963</td><td>0.6040</td><td>0.2286</td><td>0.1080</td><td>0.0939</td><td>1.1495</td></tr><tr><td>2011</td><td>99,547</td><td>0.6132</td><td>0.2172</td><td>0.1051</td><td>0.0961</td><td>1.0938</td></tr><tr><td>2012</td><td>97,425</td><td>0.6225</td><td>0.2131</td><td>0.0977</td><td>0.1016</td><td>0.9622</td></tr><tr><td>2013</td><td>95,116</td><td>0.6294</td><td>0.2122</td><td>0.0893</td><td>0.1060</td><td>0.8426</td></tr></table>

Notes. The results in this table are from the ACF estimator. Because the ACF estimator needs the first lag as instruments in the estimation, we lose the year 2002. The production functions includes industry fixed effects. Standard errors are clustered at the firm level, and all output elasticities are significant at the 1% level.

Over time, the output elasticity of ICT capital declines simultaneously with an increase in the share of ICT investments attributed to IT services of about 15 percentage points and a decrease in the share attributed to communication services of 15 percentage points. The share of ICT investments attributed to IT goods and communication goods remains relatively stable: about 50% and 3% of total ICT investments, respectively. The finding that the return on

Figure 4. Composition ICT Investments by Year  
![](/api/attachments/TZDMH2AG/fulltext/images/d1e7ccb3ee9cf62e3259517a8a77ea82be99b3345b8ff286189d47c3b1af4038.jpg)  
Note. The average share of each ICT type in total ICT investments across firms by year is shown.

ICT decreases when the share of IT services increases is consistent with our findings in Section 5.2. To validate whether the increase in importance of IT services can offer an explanation for the downward trend in the output elasticity of ICT capital, Table A-7 in Online Appendix A replicates the results of Table 11 when constructing ICT capital with IT goods and communication goods only. If the change in the composition of ICT investments is the reason for the decline in the marginal product of ICT over time, one would expect the downward trend in the marginal product of ICT to disappear. However, we find this not to be the case and conclude that compositional changes are unlikely to be the reason behind the trend. Providing a full and detailed explanation of this trend would be interesting but lies outside the scope of the current paper, and we leave this for future research.

## 5.5. ICT and (Aggregate) Productivity Growth

Early work in the literature on returns on ICT capital was spurred by the famous quote of Robert Solow (1987, p.36): “You can see the computer age everywhere but in the productivity statistics.” This quote received a lot of attention because productivity growth indeed started to decline right at the moment computer investments took off. Houseman et al. (2015) showed that it is crucial to distinguish between ICT producing and ICT using industries. They found that productivity growth rates in the United States between 1997 and 2007 fall by almost half when computer producing industries are excluded. Also, Acemoglu et al. (2014) found that ICT producing industries drive the positive impact of ICT investments on labor productivity. They conclude that the statement of ICT to improve productivity in all industries may be exaggerated.

To gauge the impact from ICT capital on aggregate GDP and aggregate productivity over the last decade we use the Petrin and Levinsohn (2012, henceforth referred to as PL) decomposition and extend it by including ICT capital and non-ICT capital separately as production inputs. The intuition of the decomposition is shown in Figure 1, and Online Appendix B2 provides more details on the model. This decomposition allows us to shed light on the contribution of ICT capital deepening to aggregate value-added growth, which learns whether firms did or did not invest (enough) in ICT capital. Furthermore, this decomposition contains a reallocation component for each production input. In a profit maximizing world, one would expect firms to reallocate resources toward its most profitable use. The reallocation components show the contribution to aggregate productivity growth from this mechanism. More specifically, it measures the contribution to productivity growth from reallocation of resources from low marginal value activities to high marginal value activities (relative to costs).<sup>19</sup> The ICT capital reallocation component learns whether firms that should (not) invest in ICT—namely, those with (low) high returns on ICT capital—did (not) invest.

Tables 12 and 13 show the results of the PL decomposition in two steps. Table 12 decomposes economywide value-added growth in labor deepening, non-ICT capital deepening, ICT capital deepening, and productivity growth. Table 13 further decomposes aggregate productivity growth into (i) within-firm technical efficiency growth, which shows whether firms become more productive on average, (ii) productivity growth through reallocation of resources from low to high marginal value activities, and (iii) a residual fixed cost component. Productivity growth from reallocation is further split in productivity growth from labor reallocation, non-ICT capital reallocation, and ICT capital reallocation.

On average, aggregate value added increased by 2.07% per year. It is apparent that this growth is largely driven by total factor productivity growth. The contribution of ICT capital deepening to aggregate value added growth is 0.23% on average. Especially during and after the Great Recession, there is a relatively low contribution to aggregate value-added growth from ICT capital deepening. This finding suggests that firms reduced their ICT investment intensity over time. To obtain additional insights into the results on ICT capital deepening from the PL decomposition, Figure 5 shows the evolution of the ratio of ICT investments per employee and the share of ICT investments in revenues.

Average ICT investments per employee increased from about EUR 1,700 per employee in 2003 to EUR 2,600 per employee in 2006 and remained relatively constant afterward. The same trend occurs when measuring ICT investment intensity as the ratio of ICT investments to revenues. The share of ICT investments in revenues almost doubled from 0.6% in 2003 to 1% in 2006 but stalled afterward. This ex plains why the contribution of ICT capital deepening to output growth declines after the Great Recession.

The result that ICT investment growth is lower after the Great Recession indicates that firms became cautious in their investment decisions. The low in vestment intensity is believed to be one of the rea sons for the productivity puzzle of the last decade. Section 5.4 shows a decrease over time in the marginal product of ICT, so it is possible that firms found it less opportune to invest in ICT after the Great Recession. Yet the marginal product of ICT is still high in the most recent years of the sample, so one would expect firms to invest in ICT, especially large firms and firms in industries with excess returns on ICT.

Table 12. PL Decomposition I (in Percentages)

<table><tr><td>Year</td><td>Aggregate output growth</td><td>Contribution from labor deepening</td><td>Contribution from non-ICT capital deepening</td><td>Contribution from ICT capital deepening</td><td>Contribution from productivity growth</td></tr><tr><td>2003</td><td>3.45</td><td>0.38</td><td>0.95</td><td>0.20</td><td>1.91</td></tr><tr><td>2004</td><td>4.62</td><td>0.61</td><td>0.46</td><td>0.36</td><td>3.19</td></tr><tr><td>2005</td><td>1.04</td><td>0.60</td><td>0.19</td><td>0.36</td><td>-0.11</td></tr><tr><td>2006</td><td>4.56</td><td>1.05</td><td>0.33</td><td>0.54</td><td>2.64</td></tr><tr><td>2007</td><td>4.48</td><td>1.48</td><td>0.57</td><td>0.21</td><td>2.22</td></tr><tr><td>2008</td><td>1.12</td><td>0.71</td><td>0.81</td><td>0.17</td><td>-0.57</td></tr><tr><td>2009</td><td>-3.85</td><td>-1.73</td><td>-0.13</td><td>0.13</td><td>-2.12</td></tr><tr><td>2010</td><td>3.30</td><td>-0.12</td><td>-0.29</td><td>0.13</td><td>3.58</td></tr><tr><td>2011</td><td>3.29</td><td>1.10</td><td>0.25</td><td>0.15</td><td>1.79</td></tr><tr><td>2012</td><td>0.46</td><td>0.26</td><td>-0.11</td><td>0.14</td><td>0.17</td></tr><tr><td>2013</td><td>0.25</td><td>-0.26</td><td>-0.31</td><td>0.11</td><td>0.72</td></tr><tr><td>Avg.</td><td>2.07</td><td>0.37</td><td>0.25</td><td>0.23</td><td>1.22</td></tr><tr><td>SD</td><td>2.57</td><td>0.87</td><td>0.43</td><td>0.13</td><td>1.75</td></tr></table>

Notes. The decomposition is based on a balanced subsample of 42,228 firms for which value added and the production inputs are positive and available for all years. Table A-12 in Online Appendix A shows a comparison with other OECD countries.

Table 13. PL Decomposition II (in Percentages)

<table><tr><td rowspan="2">Year</td><td rowspan="2">Aggregate productivity growth</td><td rowspan="2">Within-firm productivity growth</td><td colspan="3">Productivity growth through reallocation</td><td rowspan="2">Fixed cost</td></tr><tr><td>Labor</td><td>Non-ICT capital</td><td>ICT capital</td></tr><tr><td>2003</td><td>1.91</td><td>-3.03</td><td>0.39</td><td>0.72</td><td>4.05</td><td>-0.22</td></tr><tr><td>2004</td><td>3.19</td><td>0.02</td><td>0.13</td><td>0.88</td><td>2.37</td><td>-0.20</td></tr><tr><td>2005</td><td>-0.11</td><td>-2.78</td><td>0.36</td><td>0.61</td><td>1.77</td><td>-0.07</td></tr><tr><td>2006</td><td>2.64</td><td>0.98</td><td>0.29</td><td>0.31</td><td>1.21</td><td>-0.15</td></tr><tr><td>2007</td><td>2.22</td><td>0.94</td><td>0.18</td><td>0.31</td><td>0.84</td><td>-0.04</td></tr><tr><td>2008</td><td>-0.57</td><td>-1.81</td><td>0.28</td><td>0.08</td><td>0.64</td><td>0.25</td></tr><tr><td>2009</td><td>-2.12</td><td>-2.49</td><td>0.22</td><td>-0.24</td><td>0.21</td><td>0.18</td></tr><tr><td>2010</td><td>3.58</td><td>3.47</td><td>0.08</td><td>-0.16</td><td>0.35</td><td>-0.15</td></tr><tr><td>2011</td><td>1.79</td><td>0.98</td><td>0.23</td><td>0.02</td><td>0.45</td><td>0.11</td></tr><tr><td>2012</td><td>0.17</td><td>-0.75</td><td>0.37</td><td>-0.18</td><td>0.32</td><td>0.39</td></tr><tr><td>2013</td><td>0.72</td><td>0.19</td><td>0.31</td><td>-0.13</td><td>0.18</td><td>0.17</td></tr><tr><td>Avg.</td><td>1.22</td><td>-0.39</td><td>0.26</td><td>0.20</td><td>1.13</td><td>0.02</td></tr><tr><td>SD</td><td>1.75</td><td>2.00</td><td>0.10</td><td>0.39</td><td>1.20</td><td>0.21</td></tr></table>

Note. The decomposition is based on a balanced subsample of 42,228 firms for which value added and the production inputs are positive and available for all years.

To reconcile the heterogeneity in returns on ICT across industries and the firm size distribution with aggregate productivity and output growth, we look at the evolution of the reallocation component in Table 13.

Consistent with earlier research on the Belgian economy, we find that the largest share of productivity growth is driven by reallocation of resources (Van den bosch and Vanormelingen 2017). We find that ICT capital reallocation (i.e., increases in ICT capital in firms that have high benefits compared with costs from increasing ICT capital) contributes on average 1.13% to aggregate productivity growth. As in our results on ICT capital deepening, we find that this average is entirely driven by the prerecession period. After the Great Recession, the contribution of ICT capital reallocation, as well as non-ICT capital reallocation, dropped substantially. These result indicate that in the postrecession period there was only a modest impact from ICT capital reallocation to aggregate productivity growth—or, in other words, our results suggest that firms with excess returns on ICT capital invested too little in ICT. The residual fixed cost term is relatively small in comparison with total reallocation, which indicates that reallocation of resources from low-value to high-value activities does a good job in explaining total reallocation.

Figure 6 shows the ICT investment intensity across the percentiles of the output elasticity – input cost share distribution. The graph indicates whether firms that have a large “gap” between returns and costs from investing in (non-ICT) ICT capital and hence are in the upper percentiles of the gap distribution, accordingly invest in (non-ICT) ICT capital.

Figure 6 shows the ICT investment intensity in function of the opportunities associated with ICT investments. On the left are those firms for which the benefits from ICT investments are low, and on the right are the firms for which benefits from ICT investments are high. The figure shows a heavy left tail of observations for which the ICT investment intensity is relatively high, whereas the investment opportunity gap for ICT is low. The firms in this left tail are relatively small and ICT capital intensive, with ICT capital being on average 30% of the total capital stock, whereas this is only 10% in the other firms. Apart from the left tail, ICT investment intensity is relatively flat across the distribution. The same trend holds for non-ICT investments, where the left tail of the distribution is even heavier. This result is striking because one would expect that firms with large opportunities invest more. So there is a small group of firms that is ICT intensive and persistently invests in ICT while additional returns are rather low, whereas the majority of firms do not invest enough based on the difference between benefits and costs from ICT investments.

Figure 5. ICT Capital Deepening  
![](/api/attachments/TZDMH2AG/fulltext/images/40b5a824de4f6d7eb653248679848cac1965d64d72a8a7931fbbf88761494af1.jpg)  
Notes. Employment-weighted average of the ratio of real ICT in vestments to the number of full-time equivalents (FTE) and deflated revenues by year is shown. The same sample is used as in the decomposition.

Figure 6. ICT Capital Deepening and Capital Reallocation  
![](/api/attachments/TZDMH2AG/fulltext/images/e5f312c69a87cdbbdaee7db27bad8a14ecfe8894bf42fd967c0fcfb90d64c23b.jpg)  
Notes. The graph shows for each percentile of the distribution of the employment-weighted gap between the output elasticity and the input cost share of (non-IT) IT investments the value-added weighted median next-period (non-ICT) ICT investment intensity, expressed as the ratio of real (non-ICT) ICT investments per employee. The same sample is used as in the decomposition. FTE, full-time equivalent.

There could be external and/or internal frictions that make firms forgo investments in new ICT, which could explain the observed suboptimal allocation of ICT investments. New ICT often disrupts current working practices, so employees might be resistant toward adopting ICT, whereas actual usage is crucial for obtaining productivity effects (Devaraj and Kohli 2003). Also, it is not obvious to align the adoption of new ICT systems with appropriate organizational commitment toward these new ICT systems (Steelman et al. 2019). These frictions might be especially relevant in large firms compared with smaller firms, where changing working routines is easier to implement. This could explain why the firms in the left tail of Figure 6 are smaller in size than those on the right. Whatever the reason, the observed misallocation of ICT investments, together with our findings on low ICT capital deepening, can reconcile the paradox of identifying relatively high returns on ICT capital at the micro level, whereas they are not present or small at the aggregate macroeconomic level.

Tables A-8–A-11 in Online Appendix A present the results of the PL decomposition for the subset of manufacturing and services industries separately. In line with our expectations for the Belgian economy, which is characterized by a decline in manufacturing and shift to services, we find that labor deepening is the most important determinant for aggregate output growth in services while having a negative impact on output growth in manufacturing. On the other hand, productivity growth is by far the most important factor for value-added growth in the manufacturing sector, although it is not that important in the services sector. The contribution from ICT capital deepening is relatively low in services as well as in manufacturing industries, and in both sectors, the postrecession slowdown in the contribution of ICT and non-ICT capital deepening clearly stands out. So despite excess returns on ICT investments—especially in manufacturing industries, as shown in Section 5.2—there was a slowdown in ICT investment after the Great Recession that coincided with a general slowdown in productivity growth. Taking a closer look at the determinants of aggregate productivity growth in manufacturing and services industries, we find that reallocation of resources explains about 60% of productivity growth in the manufacturing sector, whereas it explains all of productivity growth in the services sector. Similar to the general downward trend over time in ICT capital deepening, we find a downward trend in the contribution of (non-ICT) ICT capital reallocation to aggregate productivity over time in both manufacturing and services industries.

Our findings of a low contribution from ICT capital deepening to aggregate output and a high concentration of ICT investments in a small group of firms is furthermore consistent with the empirical findings of declining business dynamism. Bijnens and Konings (2018) showed that the decline in Belgian dynamism is highest for the most ICT-intensive industries.

## 6. Conclusion

ICT has been transforming our society drastically over past couple of decades. However, because of a lack of comprehensive firm-level data on ICT investments, there has only been limited evidence on differences in the return on ICT across industries and across the firm size distribution. Moreover, there exists a disconnect in the ICT literature between microeconomic studies, which document substantial positive returns on ICT, and macroeconomic studies, which show a limited return of ICT on aggregate productivity growth, especially in Europe (van Ark 2014).

This paper uses a hitherto unexploited firm-level panel data set on B2B ICT purchases from 2002 to 2013, which we combine with the income statements of firms to provide new evidence on the impact of ICT on productivity. The data set on B2B ICT purchases is administratively collected from tax declarations; hence all firm sizes and industries are represented in the data. The recorded ICT expenditures cover both tangible and intangible ICT purchases. This is a more comprehensive measure of ICT capital than in earlier studies, which often relied on the number of computers per worker and hence exclude the intangible component of ICT capital (e.g., Bloom et al. 2010). This paper contributes to the ICT literature by investigating who benefits most from ICT and by decomposing the relation between ICT and productivity at the firm and the aggregate level.

We find an output elasticity of ICT capital of 0.10, which implies that a 10% increase in ICT capital increases value added with 1.1%. This is higher than in earlier studies, where the output elasticity of ICT capital was estimated at about 0.05–0.06 (Cardona et al. 2013). The gap between the output elasticity of ICT capital and its input share is substantial and higher than for other production factors. Investing an additional euro in ICT increases value added on average by EUR 1.35. The marginal product for ICT capital is higher than for other production inputs—a finding that is consistent with earlier studies.

The novelty in our study, apart from how we construct the ICT capital stock, is that we can uncover the heterogeneity in returns on ICT across industries, firm sizes, and time and that we show how the composition of ICT investments relates to this heterogeneity. We show that both at the industry and firm levels, there are differences in the output elasticity and marginal product of ICT capital. We find that the marginal product of ICT capital is higher in manufacturing industries than in services industries. Next, we show there exists a size premium in returns on ICT capital. This finding is robust to various estimation methods and other factors that might affect productivity growth such as labor quality, decentralization, and management practices. Furthermore, we revisit the Solow paradox. Our results indicate that this paradox can be explained by two causes: (i) low ICT investments and (ii) misallocation of ICT investments. We find this effect to be particularly apparent after the Great Recession, which suggests that underinvestment in ICT is at least one of the reasons for the slowdown in productivity growth in the last decade.

## Acknowledgments

The authors thank the editor, associate editor, and three anonymous referees for comments and suggestions that have substantially improved the paper. They also thank James Bessen, Todd Gerarden, Ariell Reshef, Mark Roberts, Fabiano Schivardi, and Jakob Vanschoonbeek and two anonymous referees of the National Bank of Belgium for useful comments and suggestions. The results presented in this paper comply with the legal rules on statistical secrecy. The views expressed in this paper are those of the authors and do not necessarily reflect the views of the National Bank of Belgium or any other institutions to which the authors are affiliated.

## Endnotes

<sup>1</sup> Examples include the Computerworld magazine survey (Fortune 500 firms), InformationWeek magazine survey (top 500

IT-intensive firms in the United States), Computer Intelligence Technology Database survey (Fortune 1000 firms), and Harte Hanks survey (sample of firms with more than 100 employees in Europe and United States).

<sup>2</sup> Earlier studies used more aggregate—mostly two-digit, sometimes three-digit—definitions of ICT producing industries and thus contain more noise. For example, Houseman et al. (2015) and Acemoglu et al. (2014) use data from the North American Industrial Classifi cation System 334 industry code, which also includes manufacturing of audio and video equipment, navigational measuring, electromedical and control instruments, and magnetic and optical media.

<sup>3</sup> We have no information on whether the purchase is tangible or intangible. Also, a breakdown that shows how much of the ICT purchase are investments, how much are unutilized, or how much are utilized intermediate inputs is unfortunately not available. Online Appendix C2 discusses this further, and Online Appendix C3 in cludes robustness checks on this potential issue.

<sup>4</sup> All monetary values in the paper are expressed in 2010 euros.

<sup>5</sup> Dewan and Min (1997) showed that the Cobb–Douglas production function is a good approximation of the actual underlying production function in the ICT and productivity context. They found that the Translog and CES-translog production functions yield virtually identical estimates for the ICT capital output elasticity and that the elasticities of substitution between ICT and non-ICT inputs are estimated to be very close to unity, consistent with the Cobb–Douglas model. Also, Kundisch et al. (2014) provided theoretical and empirical justification for the use of Cobb–Douglas production functions to measure the returns of information technology.

<sup>6</sup> We also experimented with the system GMM approach (Blundell and Bond 2000). The point estimates for this estimator are similar to the OLS and control function estimates.

<sup>7</sup> The ICT capital coefficient estimate of the CWDL approach is significantly higher than the estimate of the ACF approach $\bar { ( z = 4 ; p < 0 . 0 5 ) }$ . <sup>8</sup> Or a 10% increase in ICT capital multiplies value added with e<sup>0.1151×ln</sup>(<sup>1.1</sup>) 1.011. So a 10% increase in ICT capital increases value added by 1.1%.

<sup>9</sup> This is the marginal product of labor, which is based on the wage bill input share and represents the increase in value added from spending an additional euro on labor. Note that MP can also be calculated as the increase in value added from adding a full-time equivalent worker. The input share is then 0.00002 and $\begin{array} { r } { \bar { M } P _ { L } = \frac { 0 . 6 2 2 6 } { 0 . 0 0 0 0 2 } \approx 3 \bar { 1 } , 0 0 0 . } \end{array}$ . So hiring an additional full-time equivalent worker for a year increases value added on average by EUR 31,000.

<sup>10</sup> The marginal product of an input is interpreted as its gross rate of return, whereas the net rate of return is defined as the difference between the marginal product and the depreciation rate, as in Hall et al. (2010). <sup>11</sup> For manufacturing, $\begin{array} { r } { M P _ { K ^ { \mathrm { I C T } } } = \frac { 0 . 1 2 1 2 } { 0 . 0 7 6 9 } = 1 . 5 8 , ~ M P _ { K ^ { \mathrm { N I C T } } } = \frac { 0 . 2 2 4 9 } { 1 . 0 7 4 9 } = 0 . 2 1 , } \end{array}$ and $\begin{array} { r } { M P _ { L } = \frac { 0 . 6 5 0 9 } { 0 . 6 9 0 8 } = 0 . 9 4 ; } \end{array}$ ; for services, $\begin{array} { r } { M P _ { K ^ { \mathrm { I C T } } } = \frac { 0 . 1 2 0 4 } { 0 . 1 0 2 9 } = 1 . 1 \dot { 7 } , \dot { M } P _ { K ^ { \mathrm { N I C T } } } = } \end{array}$ $\frac { 0 . 1 9 9 5 } { 1 . 2 1 8 5 } = 0 . 1 6 ,$ , and $\begin{array} { r } { M P _ { L } = \frac { 0 . 6 1 5 3 } { 0 . 6 1 7 5 } = 1 . 0 0 } \end{array}$ . When computing MP based on the number of full-time equivalents, $M P _ { L } \stackrel { \cdot } { = } \frac { 0 . 6 5 0 9 } { 0 . 0 0 0 0 2 } = 3 2 { , } 6 9 0$ for manufacturing and $\begin{array} { r } { M P _ { L } = \frac { \hat { 0 } . 6 1 5 3 } { 0 . 0 0 0 0 2 } = 3 0 { , } 6 4 5 } \end{array}$ for services.

<sup>12</sup> Table A-5 in Online Appendix A shows the results when ICT capital is constructed solely from ICT goods. ICT services can be developed in house. Such ICT capital is unobserved in our data and could confound industry comparisons. We find that excluding ICT services typically decreases the ICT input share more than the output elasticity; as a result, the marginal product of ICT increases. The ranking of Table 6 remains largely unchanged, except for some industries in which ICT services are an important part of the ICT capital stock, such as the financial and insurance industries.

<sup>13</sup> In Online Appendix E, we move beyond split-sample analyses and fully recognize firm heterogeneity by identifying firm-specific output elasticities with a random coefficients production function. This approach also shows a positive relationship between firm size and the output elasticity of ICT capital.

<sup>14</sup> The firm fixed effects estimator identifies whether there is a difference between the size bins in how within-firm variation in ICT capital is related to within-firm variation in output. It controls for any time fixed unobserved heterogeneity, which one can argue management to be, but also for returns on the part of the ICT stock that is persistent over time. Therefore, the firm fixed effects estimator is likely to underestimate the return on ICT capital.

<sup>15</sup> The World Management Survey is a worldwide initiative to measure management that has been run in over 20,000 firms across 35 countries. The survey consists of 18 questions on talent management, target setting, operations management, and lean manufacturing. The average score across the 18 questions is used to measure “management.” People management practices relate to promotions, rewards, hiring, and firing. For more information about the World Management Survey, we refer to Bloom and Van Reenen (2007).

\_ Acemoglu et al. (2007) measured decentralization as having foreign profit centers, which is closely related to our measure of decentralization. FDI participation is an indirect proxy for decentralization and is also correlated to other unobservables. It is thus reassuring to see that the results hold after adding this control variable to the model. <sup>17</sup> We test in Online Appendix D.5 whether our results on heterogeneity in returns on ICT across industries and firm size are related to the evolution over time in returns on ICT and find all earlier results to be robust.

<sup>18</sup> We thank an anonymous referee for this explanation.

<sup>19</sup> In a neoclassical setting without frictions, the value of the marginal product is equal to the marginal cost, leaving no room for improvements in aggregate productivity through reallocation of resources. In this scenario, the elasticity of output with respect to an input is equal to the share of expenditures for that input in total revenue. However, in a world of imperfect competition, markups, taxes, and adjustment costs drive a wedge between marginal products, which leads to a possible role for reallocation of resources in increasing aggregate productivity growth (Basu and Fernald 2002).

## References

Acemoglu D, Aghion P, Lelarge C, Van Reenen J, Zilibotti F (2007) Technology, information, and the decentralization of the firm. Quart. J. Econom. 122(4):1759–1799.

Acemoglu D, Autor D, Dorn D, Hanson G, Price B (2014) The return of the Solow paradox? IT, productivity, and employment in U.S. manufacturing. Amer. Econom. Rev. 104(5):394–399.

Ackerberg DA, Caves K, Frazer G (2015) Identification properties of recent production function estimators. Econometrica 83(6): 2411-2451.

Aral S, Weill P (2007) IT assets, organizational capabilities, and firm performance: How resource allocations and organizational dif ferences explain performance variation. Organ. Sci. 18(5):763–780.

Aral S, Brynjolfsson E, Van Alstyne M (2012) Information, technology, and information worker productivity. Inform. Systems Res. 23(3):849–867.

Aral S, Brynjolfsson E, Wu DJ (2006) Which came first, IT or productivity? The virtuous cycle of investment and use in enterprise systems. Proc. 27th Internat. Conf. Inform. Systems (Curran Associates, Red Hook, NY), 1819–1840.

Basu S, Fernald JG (2002) Aggregate productivity and aggregate technology. Eur. Econom. Rev. 46(6):963–991.

Bharadwaj AS (2000) A resource-based perspective on information technology capability and firm performance: An empirical in vestigation. MIS Quart. 24(1):169–196.

Biagi F (2013) ICT and productivity: A review of the literature. JRC Digital Economy Working Paper 2013/9, European Commission, Brussels, Belgium.

Bijnens G, Konings J (2018) Declining Business Dynamism (Centre fo Economic Policy Research, London).

Black SE, Lynch M (2001) How to compete: The impact of workplace practices and information technology on productivity. Rev. Econom. Statist. 83(3):434–445.

Bloom N, Van Reenen J (2007) Measuring and explaining management practices across firms and countries. Quart. J. Econom. 122(4):1351–1408.

Bloom N, Sadun R, Van Reenen J (2012) American do IT better: U.S. multinationals and the productivity miracle. Amer. Econom. Rev. 102(1):167–201.

Bloom N, Garicano R, Sadun R, Van Reenen J (2014) The distinct effects of information technology and communication technology on firm organization. Management Sci. 60(12):2859–2885.

Bloom N, Draca M, Kretschmer T, Sadun R, Van Reenen J (2010) The economic impact of ICT. Final Report N.2007/0020, Centre for Economic Performance, London School of Eco nomics, London.

Blundell R, Bond S (2000) GMM estimation with persistent pane data: An application to production functions. Econometric Rev. 19(3):321–340.

Bosworth B, Triplett J (2007) Services productivity in the United States: Griliches’s Services Volume revisited. Berndt R, Hulten CR, eds. Hard-to-Measure Goods and Services: Essays in Honor of Zvi Griliche (University of Chicago Press, Chicago), 413–447.

Bresnahan T, Brynjolfsson E, Hitt LM (2002) Information technology, workplace organization, and the demand for skilled labor: Firm level evidence. Quart. J. Econom. 117(1):339–376.

Broersma L, McGuckin RH, Timmer MP (2003) The impact of computers on productivity in the trade sector: Explorations with Dutch microdata. Economist 151(1):53–79.

Brynjolfsson E (1993) The productivity paradox of information technology. Comm. ACM 36(12):66–77.

Brynjolfsson E, Hitt LM (1995) Information technology as a factor of production: The role of differences among firms. Econom. Innovation New Tech. 3(4):183–200.

Brynjolfsson E, Hitt LM (1996) Paradox lost? Firm-level evidence on the returns to information systems spending. Management Sci. 42(4):541–558.

Brynjolfsson E, Yang S (1996) Information technology and produc tivity: A review of the literature. Zelkowitz MK, ed. Advances in Computers, Vol. 4 (Academic Press, New York), 179–214.

Brynjolfsson E, Yang S (1997) The intangible benefits of costs of computer investments: Evidence from the financial markets. Proc. 18th Internat. Conf. Inform. Systems (Association for Infor mation Systems, Atlanta), 147–166.

Brynjolfsson E, Hitt LM (2003) Computing productivity: Firm level evidence. Rev. Econom. Statist. 85(4):793–808.

Brynjolfsson E, Hitt LM (2000) Beyond computation: Information technology, organizational transformation and business per formance. J. Econom. Perspect. 14(4):23–48.

Cardona M, Kretschmer T, Strobel T (2013) ICT and productivity: Conclusions from the empirical literature. Inform. Econom. Policy 25(4):109–125.

Collard-Wexler A, De Loecker J (2016) Production function estimation with measurement error in inputs. NBER Working Paper 22437, National Bureau of Economic Research, Cambridge, MA.

Commander S, Harrison R, Menezes-Filho N (2011) ICT and productivity in developing countries: New firm-level evidence from Brazil and India. Rev. Econom. Statist. 93(2):528–541.

Dedrick J, Gurbaxani V, Kraemer KL (2003) Information technology and economic performance: A critical review of the empirical evidence. ACM Comput. Surveys 35(1):1–28.

Devaraj S, Kohli R (2003) Performance impacts of information technology: Is actual usage the missing link? Management Sci. 49(3):273–289.

Dewan S, Kraemer KL (2000) Information technology and productivity: Evidence from country-level data. Management Sci. 46(4):548–562.

Dewan S, Min C (1997) The substitution of information technology for other factors of production: A firm level analysis. Management Sci. 43(12):1660–1675.

Dhyne E, Magerman G, Rubinova S (2015) The Belgian production network 2002–2012. NBB Working Paper 288, National Bank of Belgium, Brussels.

Goos M, Manning A, Salomons A (2014) Explaining job polarization: Routine-biased technological change and offshoring. Amer. Econom. Rev. 104(8):2509–2526.

Griliches Z, Hausman JA (1986) Errors in variables in panel data. J. Econometrics 31(1):93–118.

Hall BH, Mairesse J, Mohnen P (2010) Measuring the returns to R&D, Handbook of the Economics of Innovation, vol. 2 (Elsevier, Amsterdam), 1033–1082.

Hempell T (2005) What’s spurious, what’s real? Measuring the productivity impacts of ICT at the firm-level. Empirical Econom. 30(2):427–464.

Hitt LM, Wu DJ, Zhou X (2002) Investment in enterprise resource planning: Business impact and productivity measures. J. Man agement Inform. Systems 19(1):71–98.

Houseman S, Bartik T, Sturgeon T (2015) Measuring manufacturing: How the computer and semiconductor industries affect the numbers and perceptions. Houseman SN, Mandel M, eds. Measuring Globalization: Better Trade Statistics for Better Policy, Vol. 1 (W.E. Upjohn Institute for Employment Research, Kala mazoo, MI), 151–193.

Hyatt H, Nguyen S (2010) Computer networks and productivity revisited: Does plant size matter? Working paper, Center for Economic Studies, U.S. Census Bureau, Washington, DC.

Jager K (2017) EU KLEMS growth and productivity accounts 2017¨ release—Description of methodology and general notes. Release notes, The Conference Board, Brussels.

Jorgenson DW (2001) Information technology and the U.S. economy. Amer. Econom. Rev. 91(1):1–32.

Jorgenson DW, Ho MS, Stiroh KJ (2008) A retrospective look at the U.S. productivity growth resurgence. J. Econom. Perspect. 22(1):3–24.

Kohli R, Devaraj S (2003) Measuring information technology payoff: A meta-analysis of structural variables in firm-level empirical research. Inform. Systems Res. 14(2):127–145.

Kudyba S, Diwan R (2002) Increasing returns to information tech nology. Inform. Systems Res. 13(1):104–111.

Kundisch DO, Mittal N, Nault BR (2014) Using income accounting as the theoretical basis for measuring IT productivity. Inform. Systems Res. 25(3):449–467.

Levinsohn J, Petrin A (2003) Estimating production functions using in puts to control for unobservables. Rev. Econom. Stud. 70(2):317–341.

Lichtenberg FR (1995) The output contributions of computer equipment and personnel: A firm-level analysis. Econom. Innovation New Tech. 3(3–4):201–218.

Marschak J, Andrews WH (1944) Random simultaneous equations and the theory of production. Econometrica 12(3):143–205.

Melville N, Kraemer K, Gurbaxani V (2004) Information technology and organizational performance: An integrative model of IT business value. MIS Quart. 28(2):283–322.

Mithas S, Tafti A, Bardhan I, Goh JM (2012) Information technology and firm profitability: Mechanisms and empirical evidence. MIS Quart. 36(1):205–224.

Oliner SD, Sichel DE (2000) The resurgence of growth in the late 1990s: Is information technology the story? J. Econom. Perspect. 14(4):3–22.

Olley GS, Pakes A (1996) The dynamics of productivity in the tele communications equipment industry. Econometrica 64(6):1263–1297.

Petrin A, Levinsohn J (2012) Measuring aggregate productivity growth using plant-level data. RAND J. Econom. 43(4):705–725.

Roach S (1987) America’s technology dilemma: A profile of the information economy. Special economic study, Morgan Stanley, New York.

Sabherwal R, Jeyaraj A (2015) Information technology impacts on firm performance: An extension of Kohli and Devaraj (2003). MIS Quart. 39(4):809–836.

Solow RM (1987) “We’d better watch out”: Review of Manufacturing Matters: The Myth of the Post-Industrial Economy by Stephen S. Cohen and John Zysman. New York Times (July 12) 36.

Steelman ZR, Havakhor T, Sabherwal R, Sabherwal S (2019) Per formance consequences of information technology investments: Implications of emphasizing new or current information tech nologies. Inform. Systems Res. 30(1):204–218.

Stehrer R, Bykova A, Jager K, Reiter O, Schwarzhappel M (2019) ¨ Industry level growth and productivity data with special focus on intangible assets. wiiw Statistical Report 8, Vienna Institute for International Economic Studies, Vienna.

Stiroh K (2002) Information technology and the U.S. productivity revival: What do the industry data say? Amer. Econom. Rev. 92(5):1559–1576.

Stiroh K (2005) Reassessing the impact of IT in the production function: A meta-analysis and sensitivity tests. Ann. Econom. Statist. (79/80):529–561.

Syverson C (2017) Challenges to mismeasurement explanations for the US productivity slowdown. J. Econom. Perspect. 31(2): 165–186.

Tam KY (1998) The impact of information technology investments on firm performance and evaluation: Evidence from newly indus trialized economies. Inform. Systems Res. 9(1):85–98.

Tambe P, Hitt LM (2012) The productivity of information technology investments: New evidence from IT labor data. Inform. System Res. 23(3, Part 1):599–617.

van Ark B (2014) Total Factor productivity: Lessons from the past and directions for the future. Working paper 271, National Bank of Belgium.

van Ark B, O’Mahoney M, Timmer MP (2008) The productivity gap between Europe and the United States: Trends and causes. J. Econom. Perspect. 22(1):25–44.

Van Beveren I (2012) Total factor productivity estimation: A practical review. J. Econom. Surveys 26(1):98–128.

Van Biesebroeck J (2007) Robustness of productivity estimates. J. Indust. Econom. 55(3):529–569.

Van den bosch J, Vanormelingen S (2017) Productivity growth over the business cycle: Cleansing effects of recessions. VIVES Discussion Paper 60, VIVES-Research Centre for Regional Eco nomics, KU Leuven, Brussels.

Wilson DJ (2009) IT and beyond: The contribution of heterogeneous capital to productivity. J. Bus. Econom. Statist. 27(1):52–70.
