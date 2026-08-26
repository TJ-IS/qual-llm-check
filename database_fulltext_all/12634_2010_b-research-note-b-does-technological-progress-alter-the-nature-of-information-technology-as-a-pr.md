---
otero_id: 12634
otero_key: "CK7ZR9VF"
title: "<b>Research Note</b>—Does Technological Progress Alter the Nature of Information Technology as a Production Input? New Evidence and New Results"
authors: "Paul Chwelos; Ronald Ramirez; Kenneth L. Kraemer; Nigel P. Melville"
year: "2010"
journal: "Information Systems Research"
doi: "10.1287/isre.1090.0229"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/CK7ZR9VF/fulltext/images/5ccbf3f820fddbda4aac6e1fc362affa2d1bce1e266b69727354a2858104c339.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Note—Does Technological Progress Alter the Nature of Information Technology as a Production Input? New Evidence and New Results

Paul Chwelos\* , Ronald Ramirez, Kenneth L. Kraemer, Nigel P. Melville,

## To cite this article:

Paul Chwelos\* , Ronald Ramirez, Kenneth L. Kraemer, Nigel P. Melville, (2010) Research Note—Does Technological Progress Alter the Nature of Information Technology as a Production Input? New Evidence and New Results. Information Systems Research 21(2):392-408. http://dx.doi.org/10.1287/isre.1090.0229

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2010, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/CK7ZR9VF/fulltext/images/2bdf0e7532a56f89b6ecf92f65ead0e4af6dfefe0026e780a369f0f0ee947962.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

Research Note

# Does Technological Progress Alter the Nature of Information Technology as a Production Input? New Evidence and New Results

Paul Chwelos∗

Sauder School of Business, University of British Columbia, Vancouver, British Columbia V6T 1Z2, Canada

Ronald Ramirez

Business School, University of Colorado Denver, Denver, Colorado 80217, ronald.ramirez@ucdenver.edu

Kenneth L. Kraemer

Personal Computing Industry Center, University of California, Irvine, Irvine, California 92697, kkraemer@uci.edu

Nigel P. Melville Stephen M. Ross School of Business, University of Michigan, Ann Arbor, Michigan 48109, npmelv@umich.edu

rior research at the firm level finds information technology (IT) to be a net substitute for both labor and non-IT capital inputs. However, it is unclear whether these results hold, given recent IT innovations and continued price declines. In this study we extend prior research to examine whether these input relationships have evolved over time. First, we introduce new price indexes to account for varying technological progress across different types of IT hardware. Second, we use the rental price methodology to measure capital in terms of the flow of services provided. Finally, we use hedonic methods to extend our IT measures to 1998, enabling analysis spanning the emergence of the Internet. Analyzing approximately 9,800 observations from over 800 Fortune 1,000 firms for the years 1987–1998, we find firm demand for IT to be elastic for decentralized IT and inelastic for centralized IT. Moreover, Allen Elasticity of Substitution estimates confirm that through labor substitution, the increasing factor share of IT comes at the expense of labor. Last, we identify a complementary relationship between IT and ordinary capital, suggesting an evolution in this relationship as firms have shifted to more decentralized organizational forms. We discuss these results in terms of prior research, suggest areas of future research, and discuss managerial implications.

Key words: IT business value; productivity; substitute; complement; hedonic; capital services; technological change; rental price; price index; organizational decentralization

History: Vallabh Sambamurthy, Senior Editor; Chris Forman, Associate Editor. This paper was received on February 13, 2007, and was with the authors 10 <sup>1</sup> months for 3 revisions. Published online in Articles in Advance August 31, 2009.

## 1. Motivation

Microeconomic theory posits that the demand for information technology (IT) is a reflection of its own price, the price of other production inputs, and the relationship between inputs $( \mathrm { i . e . , }$ marginal rate of technical substitution). Two inputs are substitutes if their cross-price elasticity of demand is positive: Increased price for input $x _ { 1 }$ drives increased demand for input $x _ { 2 }$ . The reverse is true for complements: Increased price for input $x _ { 1 }$ drives decreased demand for input $x _ { 2 } .$ Understanding the relationship between information technology and other production inputs—substitute versus complement—is necessary for an accurate theoretical representation of IT within production-theoretic frameworks. Moreover, because IT investment and application have enabled enormous improvements in organizational productivity and performance (Brynjolfsson and Hitt 2000, Melville et al. 2004, Stiroh 2002), understanding its relationship with other production inputs informs managerial decision making.

Table 1 Prior Research Comparison—Substitutability of IT and Other Production Inputs

<table><tr><td></td><td>Current study</td><td>Dewan and Min (1997)</td><td>Chun and Mun (2006)</td></tr><tr><td colspan="4">Data</td></tr><tr><td>IT data source</td><td>Computer intelligence</td><td>IDG/computerworld</td><td>BEA</td></tr><tr><td>IT components</td><td>Hardware</td><td>Hardware, IS labor</td><td>Hardware, software, comm. equip.</td></tr><tr><td>IT measure</td><td>Capital services</td><td>Capital stock</td><td>Capital services</td></tr><tr><td rowspan="2">IT deflator</td><td>PCs (BR01*1)</td><td>All IT (G90*2)</td><td>BEA (by component)</td></tr><tr><td>Other IT HW (BEA)</td><td></td><td></td></tr><tr><td rowspan="4">Sample</td><td>1987–1998</td><td>1988–1992</td><td>1984–1999</td></tr><tr><td>Approx. 800 firms</td><td>Approx. 360 firms</td><td>N = 41 (industries)</td></tr><tr><td>N &gt; 9,800 (firm-year)</td><td>N &gt; 1,131 (firm-year)</td><td>Mfg and service</td></tr><tr><td>Mfg and service</td><td>Mfg and service</td><td></td></tr><tr><td colspan="4">Model</td></tr><tr><td>Estimation</td><td>Translog, CES-trans.</td><td>Translog, CES-trans.</td><td>SGM cost function</td></tr><tr><td>Substitution</td><td>Allen</td><td>Allen</td><td>Allen, Morishima</td></tr><tr><td colspan="4">Result</td></tr><tr><td>AES IT-K</td><td>-3.4058</td><td>1.006</td><td>4.695</td></tr><tr><td>AES IT-L</td><td>3.0120</td><td>1.063</td><td>2.416</td></tr><tr><td>Subsamples: Mfg./serv.</td><td>Consistent</td><td>Consistent</td><td>Consistent</td></tr></table>

∗<sup>1</sup>Berndt and Rappaport (2001); ∗<sup>2</sup>Gordon (1990).

One mechanism by which IT enhances organizational efficiency is via substitution for more costly labor and regular capital. For example, IT can automate paper-based administrative processes like purchasing (invoicing, purchase orders, etc.), allowing one clerk and one computer to do the work of multiple clerks and no computers. Available empirical evidence is consistent with the substitution narrative (Table 1). In one study, estimation of the Allen elasticity of substitution (AES) suggests that firms used IT as a net substitute for labor and regular capital between 1988 and 1992 (Dewan and Min 1997). Analysis of 41 U.S. industries spanning 1984–1999 is consistent with these firm-level results, while also suggesting that IT is an Allen complement for intermediate goods (Chun and Mun 2006).

Beyond the replacement of IT for other production factors, IT also enables new processes and services. Indeed, although firms continued to automate activities through the use of IT in the late 1980s and early 1990s, they also looked to use IT in ways beyond mere substitution. Factory machinery, for example, became increasingly embedded with microprocessors and memory modules to improve automated control and to track system performance. Last-minute fare sales electronically communicated via e-mail help fill empty seats on otherwise underused airline flights. The result of such innovative uses of IT is the need for more computers to share and process increased volumes of data and information, i.e., a complementary relationship between IT and ordinary capital. In addition, these types of applications provide differentiated benefits to automation, suggesting that a more nuanced use of IT could offer greater benefits relative to those accruing from straightforward substitution.

Unfortunately, the dearth of prior research on this subject means that we do not know collectively whether rapid technological progress in IT has altered the nature of IT as a production factor for firms in the U.S. economy. We could only find two prior published studies on this topic (Chun and Mun 2006, Dewan and Min 1997)—and not a single firm-level study that uses data after the emergence of the Internet. In contrast, empirical analysis of other important production inputs, such as research and development (R&D) and energy, has been prolific. More than 30 empirical studies have examined the extent to which public and private investment in R&D are substitutes or complements to other inputs (David et al. 2000). In the case of energy, price increases and price shocks have spurred more than 25 studies examining whether energy is a substitute or complement with capital (Apostolakis 1990).

Thus, given rapid technological progress in how IT is applied by firms in the Internet era, the possibility that such application may alter the nature of IT as a production input, the significant implications for productivity and growth, and the lack of prior research, there is a need for additional research examining the nature of IT as a production factor.

In this study we report new evidence and new results examining the nature of IT as a production input. Our basic thesis is that during the pre-Internet era (pre-1992), firms used IT to substitute away from labor and capital, with the result being IT capital deepening and improved firm efficiency. In contrast, we posit that during the emerging Internet era (post-1992), firms began to use IT in very different ways. Rather than substituting IT for capital, new capitalbased applications required IT for their functioning and to enhance their efficiency, resulting in a shift toward a complementary relationship between IT and capital. The overall pattern of empirical results supports our basic thesis, while raising new questions about maintained assumptions concerning the nature of IT as a production factor.

This study contributes substantively to what we know about the nature of IT as a production factor, practically to inform management about how best to leverage IT to enhance firm performance, and methodologically to the way in which IT is measured. First, given different rates of technological progress across different types of IT hardware, we introduce new price indexes that provide a finer-grained measure of IT capital. Second, given the importance of the flow of capital services resulting from IT application, especially in the Internet era, we use the rental price methodology to measure capital in terms of the flow of services provided. Finally, use of the hedonic approach enables us to extend the IT measure through 1998, enabling analysis of two periods spanning the emergence of the Internet.

The remainder of the paper is organized as follows. Section 2 discusses the theory and methods used in this study. Section 3 details the data and measurement methods used, whereas Section 4 presents empirical results. Section 5 discusses managerial implications and provides concluding remarks.

## 2. Theory and Conceptual Background

In this study we extend prior research by exploring how technological progress alters the nature of information technology as a production input. We examine this question using two complementary approaches. First, we examine the difference in price elasticity of demand between centralized information systems (IS) that were more common during the earlier dataprocessing era of technology, and decentralized IS, a type of technology more common today. Analogous to necessary goods such as bread and cooking oil, we expect that older, centralized IS has a relatively inelastic price elasticity of demand. In contrast, newer systems rooted in personal computers would be relatively elastic to changes in price. Second, we analyze whether technological progress, especially in the past decade of Internet transformation, alters the nature of information technology as a production input. We expect that the substitutability for IT and regular capital changed across an earlier period in which the World Wide Web had not yet emerged (1988–1992) to a later period marked by rapid Internet adoption and diffusion (1993–1998).

## 2.1. Price Elasticity of Demand: Centralized vs. Noncentralized Information Systems

According to microeconomic theory, the price elasticity of demand is a measure of how responsive demand is to a change in price. For a normal good (i.e., an item for which an increase in income means an increase in demand), demand for that good will always increase when its price decreases. The question is, to what extent? Typically, the more necessary a good is (milk, heating oil, etc.), the less sensitive its demand will be to price changes (relatively inelastic). This logic suggests that information systems that are essential to a firm’s everyday operation will be less elastic relative to those that may be important, but not a necessity.

Prior research suggests that IT has a relatively elastic price elasticity of demand. Brynjolfsson (1996) estimates the price elasticity of demand for office, computing, and accounting machinery (OCAM) using industry data spanning 1970–1989 to be 1.33, indicating that IT is relatively elastic. However, because OCAM was not disaggregated, it is an open question as to whether this result holds for all types of computing technology. Hendel (1999) estimates crossprice elasticity of demand for various types of personal computers in firms, finding that PCs are elastic relative to price increases of PCs with similar speeds and similar perceived quality. Prince (2008) estimates the price elasticity of demand for personal computers in households, for both short-run and long-run changes in price, finding that household demand for PCs is elastic in both the short and long run. However, we could not identify a study that estimates the price elasticity of different types of IT at the firm level.

In particular, we are interested in whether there are differences in the price elasticity of centralized versus decentralized computing. These technologies generally represent the evolution of technology from one focused on the centralized processing of data in the support of hierarchical, industrial-era corporations, to one focused on distributed processing power used across a more team-oriented and flexible highperforming organization (Bresnahan et al. 2002).

Over time, there has been a general shift toward the use of more decentralized computing, thereby reducing the amount of centralized computing technologies as compared to that used in the previous era. However, centralized computing still maintains an (albeit reduced) essential role in today’s organizations. As such, the demand for centralized computing is expected to be inelastic to price changes. On the other hand, decentralized computing technologies are more prevalent in firms. Although they too play an essential role in today’s organizations, more of these technologies are being applied toward new and experimental means for generating future growth. As such, we expect these types of technologies to be more sensitive to price changes (price elastic).

As a first step in our analysis we test the extent to which the demand for IT is affected by the price of IT. An increase in IT demand given favorable changes in IT prices would indicate that firms are deepening their investments in IT and have a need to adjust their production input mix. Moreover, an analysis of the price elasticity by type of technology will identify if demand varies for different types of technologies given similar price changes. This provides an indication of the need to account for technology differences in our input relationship analysis.

We conduct our analysis by estimating the price elasticity of demand for IT, which represents the percentage change in quantity of IT demanded for a percentage change in price of IT. We represent the quantity $Q _ { i j }$ of decentralized (PCs) and centralized (other IT) IT demanded with an IT demand equation introduced in earlier research (Brynjolfsson 1996) that incorporates a widely used functional form (Oum 1989). For estimation, the demand equation is transformed into log form, and an error term is added:

$$
Q _ {i j} = e ^ {\alpha} P _ {j} ^ {\beta_ {1}} Y _ {i j} ^ {\beta_ {2}},\tag{1}
$$

where

$$
\begin{array}{l} P _ {j} = \text { purchase   price   of   IT   in   year } j, \text { and } \\ Y _ {i j} = \text { sales   of   firm } i \text { in   year } j. \end{array}
$$

In log form,

$$
\ln Q _ {i j} = \alpha + \beta_ {1} \ln P _ {j} + \beta_ {2} \ln Y _ {i j} + \varepsilon .\tag{2}
$$

In (2), $\beta _ { 1 }$ and $\beta _ { 2 }$ can be interpreted as the price and income elasticities of demand for IT, respectively. Given our argument above, we would expect that $\beta _ { 1 }$ would be less than zero (normal good) for both PCs and other IT. However, in absolute terms, we expect $| \beta _ { 1 } | > 1$ for decentralized IT (elastic) and $| \beta _ { 1 } | < 1$ for centralized IT (inelastic).

Given putative differences in the price elasticity of demand across the two different types of IT, using a single price index to deflate a measure of IT becomes tenuous. Prior IT business value research (e.g., Brynjolfsson et al. 2002, Brynjolfsson and Hitt 1996, Melville et al. 2007) does just this by using a single price index developed for centralized (mainframe) IT systems by Gordon (1990). This value (<sub>−</sub>19.3%), estimated from processor and peripheral price data over a time period ending in 1984, is extrapolated across time frames that extend beyond 1990 and across all types of IT hardware including nonmainframe technology such as personal computers. If we find that the price elasticity of demand is different for the two types of technology, it would seem prudent to extend the Gordon (1990) centralized computing deflator and identify and apply a separate index for decentralized computing. Indeed, we might expect this to be the case given that different types of technology can have different organizational impacts (Gurbaxani et al. 1998, Aral and Weill 2007).

Observation of the rapid technological progress in personal computers underscores this point. Between 1989 and 1992, the average PC microprocessor (CPU) grew 80% in speed from 15.06 to 27.78 megahertz, RAM capacity grew from one to four megabytes, and hard-disk capacity grew from 45 to 123 megabytes (Berndt et al. 1995). In contrast, a turn-of-themillennium PC operated with gigahertz speeds had gigabyte hard drives and multiple megabytes of RAM (Berndt and Rappaport 2001). From 2000 to 2007, desktops had incorporated roughly a threefold improvement in clock speed, typically incorporated two to four cores (separate CPUs on one chip), shipped with 50–100 GB hard drives, and had from 0.5 to 4 GB of RAM.

Because the quality of IT hardware changes so rapidly, it is necessary to use quality-adjusted indexes to account for technological innovations embedded in new computer models and surviving vintages of computers by type of IT. This provides a more accurate representation of the technology in use at U.S. corporations (Berndt et al. 1995), and is critical given that accurate IT indexes are crucial to our line of research because output and productivity estimates are sensitive to the IT indexes used (Griliches 1995, Eldridge 1999, Landefeld and Grimm 2000, Moulton 2001, Nordhaus 2002). Indeed, the application of inappropriate price indexes has been cited as a primary driver of spurious results in early IT value research (Barua and Lee 1997).

## 2.2. IT and Other Input Factors: Substitute vs. Complement in the Internet Era

It is ironic that despite the core role of information technology in the postindustrial era, there are so few studies of its behavior as a production input. As a counterexample, consider the case of other production inputs, such as R&D and energy. In the case of R&D, more than 30 studies at the line of business, firm, industry, and aggregate economy level have been published on this topic (David et al. 2000). The research suggests that as private R&D spending may be more efficient than public R&D spending, the degree to which public spending spurs private spending (complementary) is important. However, even with this level of scholarly attention, the body of evidence is equivocal on the complement/substitute issue.

Another example is energy, which is important given that oil shocks impact the demand for capital depending on its substitutability or complementarity with energy. In a review of more than 25 empirical studies on this topic, Apostolakis (1990) finds that the type of analysis impacts the findings: time-series data studies find complementarity, whereas timeseries cross-sectional data studies find substitutability of energy with capital. Despite the equivocal nature of findings, the variation in methods, data sources, and levels of analysis across the large set of published studies provides a rich set of findings from which to infer patterns consistent with received wisdom and to guide future research.

In contrast, we could only find two published studies analyzing the issue of IT-capital substitutability (Chun and Mun 2006, Dewan and Min 1997). Moreover, given the data sources used by these studies, it is not clear whether firms will use more or less labor and non-IT capital in response to the consistently falling price (and therefore increasing use) of IT in today’s environment. Case studies of IS implementation in organizations illustrate examples of both complementary and substitute relationships between particular IT systems and other factors of production. However, we do not know which type of relationship is more prevalent overall. For example, Gurbaxani and Whang (1991) theorize that IT can be used to improve the monitoring of workers, thereby reducing agency costs through improved behavior control. This ability enables a firm to both increase the productivity of its existing workers and reduce the demand for new workers (IT a substitute for labor).

Zuboff (1985) posits that IT’s automating capabilities may enable a substitution of technology for other factors of production, enabling firms to take advantage of the falling price of IT to reduce operational costs (IT a substitute for other capital and labor). On the other hand, IT’s informating capabilities may allow managers to combine technology with other capital and labor in innovative ways to create new business processes that generate higher levels of performance. Milgrom and Roberts (1990) argue that IT can be used as a complementary investment to physical capital, enabling a flexible production line and a faster, more responsive manufacturing environment (IT a complement to other capital). More recently, industrial theorists have argued that IT can be used to create virtual production networks to outsource manufacturing activities to global production partners, again making IT a substitute for labor and other capital within firms (Sturgeon 2002).

Thus, although there is abundant IS research consistent with the existence of both complementary and substitute relationships between IT and other inputs, there is insufficient empirical evidence to make general statements about which type of relationship will obtain overall. Moreover, it is unclear whether prior research at the firm level, which identifies IT as a net substitute for capital and labor (Dewan and Min 1997), is applicable in the Internet era.

When examining whether the falling price and increasing use of IT will lead to more or less use of other factors of production, i.e., labor and non-IT capital, we ask the question, “Is IT a substitute for non-IT capital and labor?” To determine the net relationship between IT and other inputs, we use the elasticity of substitution. This measure captures the ease with which two inputs can be substituted for each other (Hicks 1932) and represents the input adjustments that a firm makes in response to changes in relative input prices, holding output constant (i.e., movement along a single isoquant). In a multifactor case, the most common measure of substitutability is the AES, which defines Allen complements as two inputs whose AES is less than zero, i.e., $\sigma _ { i j } < 0 ;$ and Allen substitutes as two inputs whose AES is greater than zero, i.e., $\sigma _ { i j } > 0$ . The $\mathrm { \ A E S ^ { 1 } }$ is defined as

$$
\sigma_ {i j} = \frac {\sum f _ {i} x _ {i}}{x _ {i} x _ {j}} \cdot \frac {| H _ {i j} |}{| H |},\tag{3}
$$

where

f<sub>i =</sub> marginal product of input $i ;$

H the determinant of the Bordered Hessian

$$
x _ {i} = \text { input } i;
$$

$$
\left| H _ {i j} \right| = \text { the   cofactor   of } f _ {i j}.
$$

Calculating the AES requires the use of factors estimated from a production function. A popular form of the production function is the Cobb-Douglas; however, this specification imposes a number of restrictions on the relationships between inputs; in particular, it constrains the inputs to be perfect substitutes (i.e., the elasticity of substitution is 1.0). To relax these restrictions and reduce the possibility of model specification assumption errors, we follow earlier research (Dewan and Min 1997) and introduce two flexible functional forms: the Translog and the CES-Translog.

Translog:

$$
\begin{array}{r l} \ln \mathrm{VA} _ {i j} & = \alpha + \beta_ {1} \ln \mathrm{IT} _ {i j} + \beta_ {2} \ln \mathrm{K} _ {i j} + \beta_ {3} \ln \mathrm{L} _ {i j} \\ & + \beta_ {4} \ln (\mathrm{IT} _ {i j}) \ln (\mathrm{K} _ {i j}) + \beta_ {5} \ln (\mathrm{IT} _ {i j}) \ln (\mathrm{L} _ {i j}) \\ & + \beta_ {6} \ln (\mathrm{K} _ {i j}) \ln (\mathrm{L} _ {i j}) + \beta_ {7} (\ln \mathrm{IT} _ {i j}) ^ {2} + \beta_ {8} (\ln \mathrm{K} _ {i j}) ^ {2} \\ & + \beta_ {9} (\ln \mathrm{L} _ {i j}) ^ {2} + \text { controls } + \varepsilon_ {i j}. \end{array} \tag {4}\tag{4}
$$

CES-Translog:

$$
\begin{array}{l} \ln \mathrm{VA} _ {i j} = \alpha - \frac {1}{\rho} \ln [ \delta_ {1} \mathrm{IT} _ {i j} ^ {- \rho} + \delta_ {2} \mathrm{K} _ {i j} ^ {- \rho} + (1 - \delta_ {1} - \delta_ {2}) \mathrm{L} _ {i j} ^ {- \rho} ] \\ \qquad + \beta_ {4} \ln (\mathrm{IT} _ {i j}) \ln (\mathrm{K} _ {i j}) + \beta_ {5} \ln (\mathrm{IT} _ {i j}) \ln (\mathrm{L} _ {i j}) \\ \qquad + \beta_ {6} \ln (\mathrm{K} _ {i j}) \ln (\mathrm{L} _ {i j}) + \beta_ {7} (\ln \mathrm{IT} _ {i j}) ^ {2} \\ \qquad + \beta_ {8} (\ln \mathrm{K} _ {i j}) ^ {2} + \beta_ {9} (\ln \mathrm{L} _ {i j}) ^ {2} + \text {controls} + \varepsilon_ {i j}. \end{array}\tag{5}
$$

Both are flexible in that they permit a larger variation in the substitution patterns between inputs; the Translog is a generalization of the Cobb-Douglas with the squares and interactions of the inputs, and provides a second-order approximation of any twice continuously differentiable function. Likewise, the CES-Translog is a generalization of both the Translog and the CES functions and enables econometric testing of the Translog form (Pollak et al. 1984).

## 3. Data and Empirical Methods

In this section we explicate data sources, the hedonic method used to extend IT data through 1998, the refined price index computation, and the computation of service flows.

## 3.1. Data Sources

We use the Computer Intelligence (CI) database for IT investment data within Fortune 1,000 firms between the years 1987 and 1998. The CI database details the quantity of mainframe, peripheral, minicomputer, and PC systems, as well as other IT hardware for approximately 800 firms in each year. These data were collected using a variety of methods, including surveys, site visits, physical audits, and telephone interviews. Once the hardware counts were collected at the site and establishment level, CI aggregated these data to the firm level and calculated the total value of IT capital stock based on CI’s estimates of the market values of each hardware asset. The CI data are augmented with financial data from Standard and Poor’s Compustat. Using the methods outlined in previous research (e.g., Brynjolfsson and Hitt 1995, 1996; Dewan and Min 1997), we use these financial data to construct estimates of value added (VA), non-IT capital stock (K), and labor expense (L), all of which are summarized in Table 2.<sup>2</sup>

## 3.2. Hedonic Method for Extending CI Data Through 1998

An issue with the CI database is a change in the definition of IT stock that took place in 1995. Prior to 1995, IT stock represents the value of all IT systems within the firm. From 1995 onward, the measure encompasses only the market value of computer processors. To leverage all available years of CI data, we use hedonic methods to make the post-1994 values of IT stock comparable to the previous and more comprehensive measures. First, using the measures of the IT assets of firms in the 1987–1994 period, we estimate the implicit prices used in constructing the CI IT stock measure. Next, we apply these implicit prices to the 1995–1998 period and use CI IT hardware counts to estimate a new IT stock measure, thereby creating a data set for the 1987–1998 time period that uses consistent measurement methods and is highly correlated to the original CI measure (Appendix A).<sup>3</sup>

## 3.3. Refined IT Price Index Computation

To improve the application of price indexes in future IT research, we need to improve the approach of using a single value as a multiplicative index across years. In the log form used within IT value estimations, the application of a single value index is simply a linear shift in the IT capital stock measure, and thus has no effect on the estimated IT elasticities; it is equivalent to using nominal values or applying no index at all.

In addition, we need to account for the shift in computing that has taken place since 1984. More specifically, we need to use a price index that accounts for the wide adoption of end-user computing technology in business, primarily personal computers. As stated by Gordon, “   to the extent that price reductions were more rapid on mini and micro (i.e., PC-type) computers than on mainframes, a ‘true’ price index for computer processors would decline more rapidly than the processor index developed here    ” (Gordon 1990, p. 228). Indeed, as Gordon (1990) found, a price index for personal computer processors over the 1981–1987 time period declines more rapidly than the price index for IBM mainframes over the 1972–1984 time period.

We update the IT price index used in existing IT productivity research by splitting the IT stock estimates into two major components—PCs and other IT hardware (CPE)—and deflate each value separately using appropriate quality-adjusted price indexes for each category. These improvements enable us to more accurately reflect the quality and price changes of the different types of computer in use today. This is consistent with earlier research demonstrating index differences across hardware categories (Berndt and Rappaport 2001, Berndt et al. 1995).

For PCs, we apply the PC price index provided by Berndt and Rappaport (2001), which was constructed using hedonic methods. PCs show a particularly high rate of price decline consistent with its high rate of innovation; the average annual rate of qualityadjusted price change is 28.1% per year between 1987 and 1998. The midpoint of the CI data set, 1993, was chosen as the base year for all adjustments. For all other classes of IT (i.e., mainframes, minicomputers, networking equipment, and computer peripherals), we applied the Bureau of Economic Analysis (BEA) price index for computers and peripheral equipment, which averaged 15.7% annually during the 1987–1998 time frame.<sup>4</sup> Together, the shareweighted average of our price indexes is 23.5% per year. However, as demonstrated by the firms in our data set (numbering from 783 in 1987 to 845 in 1998), the share of PCs within overall IT capital stock grows over time. As such, the actual effective index increases in magnitude in the later years of our sample. Given that our measures of IT price differ from measures used in previous research, in terms of average rate of price change and in the rate of price change across years, we would expect our results to differ from those presented in previous research. Indeed, as Gordon (2006) recently noted, existing computer price indexes, being focused on a single category of hardware, ignore the transition from mainframes to PCs. Using two shareweighted price indexes allows us to capture this very important change, and estimates that directly depend on IT prices, in particular the AES, will be affected.

Nominal values for non-IT capital stock, labor expense, and the components of value-added are deflated using appropriate industry-specific price indexes where available, with the midpoint (1993) again used as the base year. The average annual price change for these indexes ranges from a low of 0.15% per year to a high of 4.05% per year, much smaller in absolute terms than the IT price indexes.<sup>5</sup>

<sup>5</sup> BEA-implicit GDP price deflators by industry are used to deflate sales; the Bureau of Labor Statistics (BLS) producer price index

## 3.4. Computation of Service Flows

In this section, we argue that the flow of IT services is a better representation of the value provided by IT than is a summation of IT assets. IT assets provide a useful proxy for IT services, and have been widely used in prior research using production theory (Brynjolfsson and Hitt 1996, Lichtenberg 1995). However, for the purpose of production function estimation, a more appropriate measure of inputs is the flows of services from (or, equivalently, payments to) assets that are used, but not consumed in the production process (Jorgenson and Griliches 1967). Payments to employees (labor) are traditionally measured in this way, but capital inputs are often measured in terms of total stock rather than the value of services derived from that stock.

Although capital stocks and flows are related through rental prices, the use of stocks rather than flows has long been understood to introduce a number of measurement errors, the most important of which is the implicit assumption that capital service prices are proportional to capital asset prices for different types of capital (Jorgenson and Griliches 1967). Measuring capital assets in terms of stock calls for adding together capital stocks at constant prices to obtain an overall measure of capital input. Because we expect the rental prices of PCs and CPE to be quite different, we will use capital service flows to avoid this source of bias.

To convert capital stock measures to service flows, we use the rental price methodology as implemented by the BLS and other statistical agencies. Rental prices, or “user cost” of capital, are defined as the sum of rate of return, depreciation, and the expected rate of asset price appreciation or depreciation, net of income and property taxes. Although the BLS is the primary source of rental prices, we adjust these data to make use of our new price indexes.

Rental prices were calculated using the traditional methodology used by the BLS. As illustrated in Equation (6), rental prices, or “user cost” of capital, are defined as the sum of rate of return, depreciation, and the expected rate of asset price appreciation or depreciation, net of income, and property taxes. Consistent with our conjecture of a salient difference between PCs and centralized computing, we compute separate rental prices for 12 SIC industries (Appendix B).

$$
R _ {i t} = P _ {i} (R _ {i} + \delta_ {i t} - E (p _ {i t})) T _ {t} + W _ {t}\tag{6}
$$

where,

$$
\begin{array}{l} R _ {i t} = \text { rental   price   of   asset } i \text { in   year } t, \\ P _ {i} = \text { purchase   price   of   asset } i, \\ R _ {i} = \text { nominal   rate   of   return }, \\ T _ {t} = \text { income   tax   parameter   in   year } t, \\ W _ {t} = \text { wealth   tax   parameter   in   year } t, \\ \delta_ {i t} = \text { depreciation   rate   of   asset } i \text { in   year } t, \\ E (p _ {i t}) = \text { expected   rate   of   capital   gains   on   asset } i \\ \text { in   year } t. \end{array}
$$

Rental prices were created for three classes of assets: non-IT capital, $\mathrm { P C } s ,$ and CPE. Averaging across all industries and years, the mean rental price for non-IT capital is 12.64% of the asset purchase price. In contrast, the average rental prices for PCs and CPE across the time frame are 70.31% and 55.48% of the asset price, respectively. These rental prices reflect the well-known finding that the ratio of rentalto-purchase price is much higher for IT assets than for non-IT assets, given the rapid price declines of IT versus regular capital (Chwelos 2003). Averaging across the data set using the volume of asset types (PC versus CPE) as weights, the ratio of rental prices for IT versus non-IT capital in the panel is approximately 4.68:1, reflecting the much shorter service life (depreciation) and more rapid obsolescence (negative asset price change because of innovation) of IT assets. Using capital stocks would have implicitly assigned an equal weight to the stocks of PCs and CPE, resulting in mismeasurement of the IT input.

Service flows are computed using the average of the starting and finishing capital stock values for the year in question; the resulting median values of IT and non-IT capital stocks and service flows, as well as labor and value-added, are shown in Table 2. Whereas valueadded, labor, and non-IT capital stocks grow modestly over the sample time period, the value of real IT capital stock increases by more than an order of magnitude between 1987 and 1998. More pronounced still is the growth of IT capital services, which, reflecting the higher rental prices, grows faster than does IT capital stock. By 1998, IT capital services are approximately 31% of total capital services, up from only 4% in 1987.

Table 2 Data Sample—Firm Characteristics

<table><tr><td>Year</td><td>Firms</td><td>Value added</td><td>Labor</td><td>Non-IT capital stock</td><td>Non-IT capital services</td><td>IT capital stock</td><td>IT capital services</td></tr><tr><td>1987</td><td>783</td><td>716.84</td><td>367.76</td><td>527.64</td><td>64.35</td><td>5.19</td><td>2.93</td></tr><tr><td>1988</td><td>793</td><td>743.53</td><td>385.68</td><td>518.81</td><td>63.58</td><td>6.19</td><td>3.15</td></tr><tr><td>1989</td><td>797</td><td>797.27</td><td>410.85</td><td>539.32</td><td>59.80</td><td>6.80</td><td>3.51</td></tr><tr><td>1990</td><td>795</td><td>773.00</td><td>404.62</td><td>549.21</td><td>58.12</td><td>7.68</td><td>3.66</td></tr><tr><td>1991</td><td>813</td><td>713.91</td><td>415.76</td><td>572.98</td><td>54.55</td><td>8.67</td><td>3.95</td></tr><tr><td>1992</td><td>820</td><td>679.54</td><td>410.27</td><td>538.66</td><td>49.65</td><td>10.78</td><td>5.06</td></tr><tr><td>1993</td><td>822</td><td>724.17</td><td>426.65</td><td>569.99</td><td>52.08</td><td>12.64</td><td>6.48</td></tr><tr><td>1994</td><td>840</td><td>763.97</td><td>442.25</td><td>559.17</td><td>53.61</td><td>16.29</td><td>8.83</td></tr><tr><td>1995</td><td>888</td><td>814.43</td><td>459.35</td><td>602.02</td><td>64.79</td><td>18.54</td><td>10.86</td></tr><tr><td>1996</td><td>888</td><td>910.62</td><td>466.79</td><td>617.79</td><td>65.89</td><td>26.45</td><td>14.43</td></tr><tr><td>1997</td><td>862</td><td>987.60</td><td>520.22</td><td>670.73</td><td>72.30</td><td>32.11</td><td>19.66</td></tr><tr><td>1998</td><td>845</td><td>1,116.27</td><td>585.66</td><td>705.45</td><td>87.23</td><td>73.17</td><td>38.40</td></tr></table>

Note. Median values, in millions of 1993 dollars, for all columns except Yea and Firms.

## 4. Results

Before we begin our examination of the effects of IT price changes on the role of IT in production, we estimate the returns to IT for firms in our data set. We find consistent evidence of positive and significant IT returns, providing one indication that the new price indexes and input measurement methods used in our research do not adversely affect the core results found in existing IT business value research. Table 3 presents regression results for Cobb-Douglas, Translog, and CES-Translog specifications, with the estimated output elasticity for each input in the bottom three rows. We also display the standard deviations of these estimates derived from bootstrapping, as described in Section 4.2 below. All estimated production functions satisfy the quasi-concavity assumption as the bordered Hessian is, in all cases, negative semidefinite at the median values of the inputs. Controls were used for both industry and year, and Huber-White robust estimators were used to account for nonindependent variance within repeated observations of the same firm.

IT output elasticity is estimated to be positive and significant across all functional forms, with estimates of 0.0636, 0.0652, and 0.0744 for the Cobb-Douglas,

∗p < 010; ∗∗p < 005; ∗∗∗p < 001.

Table 3 Estimate of IT Impact on Firm Output, 1987–1998

<table><tr><td></td><td>Cobb-Douglas</td><td>Translog</td><td>CES-Translog</td></tr><tr><td>Constant</td><td>2.2989(0.1702)***</td><td>16.0729(1.7030)***</td><td>3.0131(0.1068)***</td></tr><tr><td> $\rho$ </td><td>—</td><td>—</td><td>0.2275(0.0419)***</td></tr><tr><td>IT</td><td>0.0636(0.0103)***</td><td>0.4948(0.1120)***</td><td>0.6542(0.0499)***</td></tr><tr><td>K</td><td>0.193(0.0111)***</td><td>0.2063(0.0950)**</td><td>0.2886(0.0455)***</td></tr><tr><td>L</td><td>0.6946(0.0189)***</td><td>-1.04(0.2280)***</td><td>—</td></tr><tr><td>IT * IT</td><td>—</td><td>0.0069(0.0031)**</td><td>0.0284(0.0029)***</td></tr><tr><td>IT * K</td><td>—</td><td>0.0126(0.0045)***</td><td>-0.0177(0.0063)***</td></tr><tr><td>IT * L</td><td>—</td><td>-0.044(0.0101)***</td><td>-0.0638(0.0049)***</td></tr><tr><td>K * K</td><td>—</td><td>0.0256(0.0029)***</td><td>0.0416(0.0029)***</td></tr><tr><td>K * L</td><td>—</td><td>-0.0574(0.0087)***</td><td>-0.0622(0.0034)***</td></tr><tr><td>L * L</td><td>—</td><td>0.0869(0.0107)***</td><td>0.0703(0.0021)***</td></tr><tr><td>N</td><td>9,847</td><td>9,847</td><td>9,847</td></tr><tr><td>Firms</td><td>1,514</td><td>1,514</td><td>1,514</td></tr><tr><td>Controls</td><td>Industry, year</td><td>Industry, year</td><td>Industry, year</td></tr><tr><td> $R^{2}$ </td><td>0.9213</td><td>0.9294</td><td>0.9265</td></tr><tr><td> $\eta_{IT}$ </td><td>0.0636(0.0103)***</td><td>0.0652(0.0045)***</td><td>0.0744(0.0065)***</td></tr><tr><td> $\eta_{K}$ </td><td>0.193(0.0111)***</td><td>0.1803(0.0043)***</td><td>0.1841(0.0055)***</td></tr><tr><td> $\eta_{L}$ </td><td>0.6946(0.0189)***</td><td>0.6957(0.0067)***</td><td>0.7045(0.0069)***</td></tr></table>

Notes. Log VA-dependent variable, log input variables, 1993 base year. Robust standard errors for coefficient estimates in parentheses computed using White’s estimator. Standard error for elasticity in Translog and CES Translog models computed using the bootstrap procedure.

Translog, and CES-Translog functional forms, respectively. All adjusted R-squared are above 0.92, indicating good explanatory power for each specification. The restrictions imposed by the Cobb-Douglas specification versus the Translog are strongly rejected $( F _ { 6 , 1 , 5 1 3 } = 2 3 . 9 3 , ~ p < 0 . 0 0 0 1 )$ . Likewise, the restriction implied by the Translog versus the CES-Translog specification is also rejected $( F _ { 1 , 9 , 8 1 5 } = 2 9 . 5 4 ,$ $p < 0 . 0 0 0 1 ) . ^ { 6 }$ Thus, the use of more flexible functional forms is appropriate. However, given the widespread use of the Cobb-Douglas and Translog specifications in the IT business value literature, we include the results for all specifications in Table 3 to enable comparisons with prior (and future) research.

Our estimates of IT output elasticity are slightly higher in absolute magnitude than those reported in earlier research using CI data, although somewhat lower than those reported in IT-substitution research we update in this paper.<sup>7</sup> We attribute the difference in results to differences in capital measurement, specifically, to measuring real capital using (a) updated and more asset-specific price indexes tied to the industry, asset, and year in question, and (b) the rental price approach to measuring capital service flows. These differences result in capital measures that more accurately capture the relative economic importance of the service flows across IT and non-IT capital. As well, these measures correctly aggregate different types of IT capital (PCs and other IT) that have significantly different rental prices, mitigating any potential aggregation bias.<sup>8</sup> Nonetheless, our estimated output elasticities are consistent with earlier research.

## 4.1. Price Elasticity of Demand

We examine the price elasticity of demand as a first step in analyzing the effects of IT price and quality changes. Equation (2) is estimated for both PCs and CPE using both ordinary least squares (OLS) and, as a check on the impact of the supply side, two-stage least squares (2SLS). To identify the supply side, we use a semiconductor price index for microprocessors as an instrument for the purchase price of IT. For the years 1987–1992, we use the summary price index for microprocessors from Grimm (1998); for 1992–1998 we use the microprocessor price index from Aizcorbe et al. (2002). Research has demonstrated that microprocessor prices are correlated with the purchase price of IT, including those of computers and other networking equipment (Aizcorbe et al. 2002, Chwelos 2003, Doms and Forman 2005). Moreover, they are the basis for Moore’s law and the rapid price declines of IT.

When estimating Equation (2), the noise term may also contain other (unmeasured) factors that may be associated with, or drive, demand. For information technology, such factors may include new technology form factors, complementary peripherals, marketing campaigns, advertising, and the like. Firm demand for technology may also be driven by organizational characteristics (structure, size, function, etc.), the brand of technology under consideration, and the firm’s evaluation of its current IT capabilities to meet future needs (Hendel 1999, Prince 2008). However, semiconductor prices are driven primarily by the latest technological breakthrough, with more leading-edge microprocessor technologies commanding higher prices (Aizcorbe et al. 2002). Semiconductor prices are also not likely to be related to individual firm demand for IT because it is unlikely that an individual firm will influence aggregate semiconductor prices.<sup>9</sup> Thus, although semiconductor prices are correlated with the purchase price of IT, we do not believe semiconductor prices are correlated with the error term of Equation (2). As such, they make a reasonable candidate for an instrumental variable in our 2SLS analysis.

The results from the two approaches are nearly identical, confirming that controlling for supply effects had little impact. The results of the 2SLS approach are presented in Table 4. The price elasticity of demand for PCs is estimated to be 1.19, indicating that the demand for PCs is elastic. That is, a 1% decrease in the price of PCs leads to a 1.19% increase in purchases of PCs. This finding is consistent with that of Hendel (1999), who estimates demand price elasticities across 14 categories of PCs in 1988 and finds that they are all elastic. However, the price elasticity of demand for CPE is only 0.58, which is inelas-$t i c ,$ indicating that a 1% drop in the price of other IT leads to only a 0.58% increase in purchases of other IT. Our estimate of $\varepsilon _ { \mathrm { P C } } = 1 . 1 9$ is slightly smaller than the price elasticity of 1.33 reported in earlier research (Brynjolfsson 1996), likely because of differing levels of analysis: firm versus economy. Our firm-level estimate does not include consumer use of computing technology (home PCs); consumer demand for computing may be more price elastic than business demand. Alternately, the difference may simply stem from the later time frame of our study.

Table 4 Price Elasticity of Demand for PCs and Other IT, 1987–1998

<table><tr><td></td><td>PCs</td><td>Other IT</td></tr><tr><td>Constant</td><td>-5.3347(0.5859)***</td><td>-3.424(0.5933)***</td></tr><tr><td>p</td><td>-1.1867(0.0103)***</td><td>-0.5762(0.0289)***</td></tr><tr><td>y</td><td>0.8844(0.0232)***</td><td>0.8376(0.0232)***</td></tr><tr><td>N</td><td>7,932</td><td>7,412</td></tr><tr><td>Firms</td><td>1,283</td><td>1,265</td></tr><tr><td>Controls</td><td>Industry</td><td>Industry</td></tr><tr><td> $R^2$ </td><td>0.8136</td><td>0.4658</td></tr></table>

Notes. Log PC or other IT purchases are the dependent variable, log input variables. Robust standard errors in parentheses computed using White’s estimator. Results are robust to empirical specification, including OLS and 2SLS (presented here).  
∗p < 010; ∗∗p < 005; ∗∗∗p < 001.

Taken together, the results of our price elasticity of demand analysis suggest that by the late 1990s, firm demand for computing power was focused on decentralized rather than centralized systems. The shift in demand was driven not only by improvements in client-level computing power, but by new organizational designs centered around a team-oriented structure. The results also indicate that with continued improvements in the price and quality of technology—something that has occurred since the inception of Moore’s Law in 1965—firms will turn increasingly towards IT as a production input. This not only supports the need to examine the continuing shift in firm production inputs as a whole (toward more IT), but also the need to account for the different types of technology that make up the IT input category. This is further support for our identification and use of individual price indexes for centralized and decentralized technologies.

Table 5 Allen Elasticity of Substitution Estimates 1987–1998, Capital Services

<table><tr><td></td><td>Translog (I)</td><td>CES-Translog (II)</td><td>Mfg. Translog (III)</td><td>Services Translog (IV)</td><td>Mfg. CES-Translog (V)</td><td>Services CES-Translog (VI)</td></tr><tr><td colspan="7"> $\sigma_{ITK}$ </td></tr><tr><td>Estimate</td><td>-2.5686</td><td>-3.4058</td><td>-1.7233</td><td>-3.7073</td><td>-2.0318</td><td>-5.8811</td></tr><tr><td>Standard error</td><td>(0.8077)***</td><td>(0.8518)***</td><td>(1.1814)*</td><td>(1.7483)***</td><td>(1.0467)***</td><td>(2.2804)***</td></tr><tr><td>95% Bias-corrected confidence interval</td><td>-4.6336 to -1.4481</td><td>-5.1113 to -1.5613</td><td>-4.4732 to 0.2419</td><td>-8.4824 to -1.5225</td><td>-4.9864 to -0.3391</td><td>-12.8029 to -3.1859</td></tr><tr><td colspan="7"> $\sigma_{ITL}$ </td></tr><tr><td>Estimate</td><td>2.6005</td><td>3.0120</td><td>2.3400</td><td>2.6140</td><td>2.2291</td><td>2.8018</td></tr><tr><td>Standard error</td><td>(0.3767)***</td><td>(0.4672)***</td><td>(0.4496)***</td><td>(0.6426)***</td><td>(0.4711)***</td><td>(0.7170)***</td></tr><tr><td>95% Bias-corrected confidence interval</td><td>2.0017 to 3.4989</td><td>2.3121 to 4.2359</td><td>1.6839 to 3.4533</td><td>1.7684 to 4.3265</td><td>1.7160 to 3.8995</td><td>1.8732 to 4.8413</td></tr><tr><td colspan="7"> $\sigma_{KL}$ </td></tr><tr><td>Estimate</td><td>2.1381</td><td>2.2435</td><td>1.7974</td><td>3.2169</td><td>1.7743</td><td>3.8324</td></tr><tr><td>Standard error</td><td>(0.1611)***</td><td>(0.1723)***</td><td>(0.1578)***</td><td>(0.6384)***</td><td>(0.1772)***</td><td>(0.9276)***</td></tr><tr><td>95% Bias-corrected confidence interval</td><td>1.9180 to 2.5047</td><td>1.9999 to 2.7255</td><td>1.5570 to 2.1587</td><td>2.4455 to 4.839</td><td>1.5127 to 2.2457</td><td>2.7457 to 6.1522</td></tr></table>

Notes. Translog models estimated using linear least squares regression. CES-Translog models estimated using nonlinear least squares regression. AES standard errors and confidence intervals computed using the bootstrap procedure.  
∗p < 010; ∗∗p < 005; ∗∗∗p < 001.

## 4.2. Substitution

4.2.1. Baseline Results. Table 5 presents the AES estimates, which are evaluated at the median values of IT, K, L, and VA. Because the elasticities of substitution (as well as the output elasticities for the Translog and CES-Translog functional forms) are highly nonlinear functions of the estimated parameters, their distributions must be estimated using numerical techniques. Estimates of the standard deviations and confidence intervals for the output and substitution elasticities are calculated using the bootstrap procedure (Efron and Tibshirani 1993) with 1,000 replications.

As expected, ordinary capital and labor emerge as net substitutes $( \sigma _ { K L } > 0 )$ , as do IT capital and labor $( \sigma _ { I T L } > 0 )$ under both specifications (Translog, CES-Translog). To further probe our results, we split the sample into the manufacturing (SIC code 4) and service sectors (SIC code > 4) and repeat the regressions. All labor-related AES estimates are similar in both samples and across both specifications, indicating again that labor is a substitute for both IT and non-IT capital.<sup>10</sup> High labor cost appears to remain an issue for all types of firms and the reduction of labor expense through capital substitution remains a key managerial objective.

Our analysis of the relationship between IT and non-IT capital inputs yields unique results. AES estimates show that firms are using these two factors in complementary ways. Specifically, for the overall sample, we find that $\sigma _ { I T K } < 0 .$ . This result holds across both the Translog and CES-Translog functional forms and is consistent across analysis of manufacturing and service sector sample splits. It appears that firms of all types have turned to capital investments as a means for completing production activities. Indeed, these results provide empirical support for earlier case studies describing combined non-IT and IT capital solutions.

4.2.2. Technological Progress. Our identification of an IT-K complementary relationship in firms over the 1987–1998 time period is unique and differs from the IT-K input relationship identified in earlier research examining an earlier time frame (Dewan and Min 1997). We posit that the evolution of organizations toward more decentralized forms (via decentralization of decision authority, self-management teams, work cells, etc.), enabled by new types of decentralized technologies (e.g., PCs, servers, networking, etc.), has helped bring about a change in how IT and ordinary capital inputs are used in firms. As industrial era firms began to use IT, application was targeted primarily at replacing more costly capital inputs. However, as firms gained experience with IT and as technological innovation continued, especially the rise of Internet and networking technologies, the shift toward using IT as more of a complement to ordinary capital accelerated. Given limited prior research on IT substitutability, we assume this shift started after 1992.

To test our supposition, we split our sample into two time periods and estimate the IT-K-L input relationships to examine if there has been a change in these relationships over time. We first estimate the input relationships for 1988–1992 (period 1) to provide a baseline for comparison to the later 1993–1998 time period (period 2). The choice of these years also allows us to directly compare our estimated relationships to those of the earlier study by Dewan and Min (1997), which used the 1988–1992 time frame. We then repeat our analysis by using the Gordon (1990) IT price index and IT capital stock measurement method. This analysis allows us to test whether the choice of price indexes and measurement methods impacts our core results. It also allows for a more seamless comparison of results with Dewan and Min across similar time periods.

Table 6 presents the estimated output elasticities and substitution elasticities for three periods across two empirical methods. A CES-Translog specification similar to Equation (5) is used in this analysis with value-added as the dependent variable and IT, K, and L as independent variables. As before, bootstrapping is used to develop all confidence intervals for the substitution elasticity estimates. The results are split based on the use of the updated IT price indexes introduced in this paper and the capital services methodology (CR-Flow) and the use of the Gordon IT price index and IT capital stocks (Gordon-Stock). Within these two major subgroups, estimates are provided for the 1988–1992, 1993–1998, and 1988–1998 time periods.

The pattern of results using updated price indexes and capital services adopted herein provides support for the evolution of the IT-K relationship over time. In period 1 (1988–1992), we find $\sigma _ { I T K }$ to be negative but not significant (Column I). Thus, at this point in time, we can only say that IT and ordinary capital inputs are being used in many ways, in both a substitution and complementary fashion, with neither type obtaining overall. However, our results indicate that a shift occurs in the late 1990s. During the 1993–1998 time period (Column II), we find $\sigma _ { I T K }$ to

Table 6 Time Period Results by Methodology with Comparison to Prior Research

<table><tr><td rowspan="2"></td><td colspan="3">Updated price index/Capital services</td><td colspan="4">Gordon price index/Capital stock</td></tr><tr><td>1988–1992(I)</td><td>1993–1998(II)</td><td>1988–1998(III)</td><td>1988–1992DM97 (IV)</td><td>1988–1992(V)</td><td>1993–1998(VI)</td><td>1988–1998(VII)</td></tr><tr><td> $\eta_{IT}$ </td><td>0.075***</td><td>0.090***</td><td>0.080***</td><td>0.104***</td><td>0.084***</td><td>0.072***</td><td>0.077***</td></tr><tr><td> $\eta_K$ </td><td>0.177***</td><td>0.183***</td><td>0.184***</td><td>0.281***</td><td>0.178***</td><td>0.206***</td><td>0.194***</td></tr><tr><td> $\eta_L$ </td><td>0.718***</td><td>0.690***</td><td>0.701***</td><td>0.601***</td><td>0.710***</td><td>0.682***</td><td>0.690***</td></tr><tr><td> $\sigma_{ITK}$ </td><td>-5.895</td><td>-2.713***</td><td>-2.829***</td><td>1.006+</td><td>-0.773</td><td>-1.792***</td><td>-1.60***</td></tr><tr><td> $\sigma_{ITL}$ </td><td>5.295</td><td>2.480***</td><td>2.729***</td><td>1.063**</td><td>2.863***</td><td>2.427***</td><td>2.383***</td></tr><tr><td> $\sigma_{KL}$ </td><td>2.654</td><td>2.114***</td><td>2.161***</td><td>1.005***</td><td>2.216***</td><td>2.031***</td><td>2.140***</td></tr></table>

Notes. Column (IV) from Dewan and Min (1997, p. 1668), Table 4, Col. 1 and 2. All other columns are current study results. All models use value-added as a dependent variable, with labor ordinary capital, and IT as independent variables. Industry and year controls. CES-Translog specification using nonlinear least squares regression. Standard error for elasticity and AES computed using the bootstrap procedure.

$$
^ {+} p <   0. 1 5; ^ {*} p <   0. 1 0; ^ {* *} p <   0. 0 5; ^ {* * *} p <   0. 0 1.
$$

be both negative and significant. Thus, given technological progress, experience, and other organizational advances, we identify an evolution in the IT-K relationship from one that is mixed-used to one that is complementary in nature.

Comparing our results to those using Gordon-Stock, we find similar results across the entire time frame (Column VII) and within the late 1990s time period (Column VI). The substitution elasticities between the input factors are found to be the same (sign and significance) as those estimated using CR-Flow. Differences do occur in the earlier time period (Column V), with $\sigma _ { I T L }$ and $\sigma _ { K L }$ being the same sign (positive) but also being statistically significant. However, for $\sigma _ { I T K }$ , both the sign (negative) and lack of significance at a minimum $p < 0 . 1 5$ level is the same across CR-Flow and Gordon-Stock. Thus, our finding of an evolving IT-K relationship across time periods is also found in analysis using Gordon-Stock, indicating that our results are not a byproduct of the price index used or the method for measuring IT usage. Finally, estimated substitution elasticities across the 1988–1992 time frame using Gordon-Stock allow us to closely replicate the Dewan and Min (1997) study. Our estimates for $\sigma _ { I T L }$ and $\sigma _ { K L }$ (Column V) are very similar to those of Dewan and Min (replicated in Column IV), both in sign and significance. Both forms of capital are found to be substitutes for labor. A difference exists with our estimate of $\sigma _ { I T K }$ which is negative but not significant. This differs from the $\sigma _ { I T K } > 0$ $( p < 0 . 1 5 )$ result of Dewan and Min (1997).

Despite the basic consistency of results across both studies, there are differences between our analysis and that of Dewan and Min (1997). These include the number of firms in the sample, size of firms, and mix of firms, among others. Of special note is their inclusion of a software input, based on three-times IS labor, within their measure of IT investment. The use of an IS labor measure within the IT measure may potentially be a contributor to their finding of an IT-K substitution relationship.

## 5. Discussion and Conclusion

## 5.1. Discussion

In this study we extend prior research on the substitutability of information technology with other production inputs (Chun and Mun 2006, Dewan and Min

1997) to examine the extent to which technological progress has altered the nature of IT as a production factor. Our maintained thesis is that the emergence of the commercial Internet in the 1990s enabled firms to go beyond mere substitution to enable entirely new processes and services, engendering the possibility of new relationships among production inputs. Given the critical role of IT in the modern economy, understanding the answer to this question is important to researchers, business managers, and public policy makers.

Several key results emerge from our empirical analysis of 9,800 observations from approximately 800 large, Fortune 1,000 firms for the years 1987–1998. First, there is a significant difference in the price elasticity of demand between centralized and decentralized computing. Specifically, the price elasticity of demand for decentralized IT computing power (PCs) is estimated to be 1.19, indicating that the demand for decentralized computer power is relatively elastic. This means that a change in demand for PCs will be larger than a relative change in their price. In our case, a 1% decrease in PCs prices will result in a 1.19% increase in demand for PCs. On the other hand, the price elasticity for centralized computer power (CPE) is relatively inelastic, meaning that a 1% decrease in the price of CPE will yield only a 0.58% increase in demand. Thus, although current demand for IT is driven by decentralized computing needs—motivated by modern organizational structures—there remains a need for centralized, shared computing power that enables firms to conduct core business processes. We draw an analogy between necessary goods such as heating oil and such necessary centralized computing power—both are relatively inelastic. Thus, technological progress and the proliferation of decentralized computing yields a different price elasticity of demand relative to earlier types of computing systems.

Second, we find that across all types of firms, IT remains a net substitute for labor through 1998 $( \sigma _ { I T L } > 0 , ~ p < 0 . 0 1 )$ ), updating a similar finding by Dewan and Min (1997) whose analysis time period ended in 1992. Labor has the largest factor share and is the primary cost driver for firms. IT and its automating capabilities provide an opportunity to reduce these costs, and today’s firms continue to turn to technology as a replacement for labor in the production process.

Third, in contrast to prior research, we find that IT is a net complement to non-IT capital. This indicates that firms are increasing their use of ordinary capital in combination with IT; specifically, we find that IT is being used as a complement to non-IT capital $( \sigma _ { I T K } < 0 , p < 0 . 0 1 )$ . Firms can take advantage of IT’s new capabilities to produce their goods and services through the joint application of IT and regular capital. This result holds across the entire study period for various subsamples: service and manufacturing sector firms appear to have designed their production processes to use IT as a replacement for labor and as a complement to ordinary capital.

Moreover, comparing our findings to those of Dewan and Min (1997)—by splitting our sample into subperiods (1988–1992; 1993–1998) and using similar methods—indicates that the IT-K net complement result is strong in the more recent period, and weak in the earlier period. This provides further support for our thesis that as firms began to adopt Internet business practices, such as selling online, their use of IT and non-IT capital shifted from a substitution to a complementarity relationship.

Finally, the $\sigma _ { I T L }$ estimates indicate a potential difference in IT labor substitution across industry sectors, with $\sigma _ { I T L }$ being higher in service firms than in manufacturing firms. This variation is feasible given the “leanness” of current manufacturing. Over time, these firms have adopted organizational innovations (Total Quality Management, employee empowerment, self managed teams, etc.) to remain competitive with global competition and may have already established efficient levels of labor. Compound this with the adoption of outsourcing in this sector, and we have a scenario where further substitution levels may be marginally limited. On the other hand, firms in the growing service industry are relatively newer at these IT-based, labor-saving applications, and as such, marginally large labor substitution opportunities may still remain in these types of firms. However, we hesitate to form any concrete conclusions in this regard because our $\sigma _ { I T L }$ results contradict those related to industry-level analysis during the same time period (Chun and Mun 2006). Many key data and methodological differences exist between our study and that of Chun and Mun, central of which is our examination of large Fortune 1,000 firms and their examination of 41 industries. However, given the potential implications of our sector-based findings (e.g., identification of labor-based outsourcing opportunities in services), future research is needed to identify the labor substitution characteristics of non-Fortune 1,000 firms.

## 5.2. Implications

Given our findings of a different price elasticity of demand across different types of IT, the use of multiple price indexes for different categories of IT provides a more precise estimate of constant dollar IT measures such as capital and the flow of services. This is especially important given the proliferation of different categories of information technology. We have identified two sources for such indexes: one for distributed computing (PCs) and one for centralized computing (mainframe). The application of categoryspecific indexes accounts for evolutionary changes in a firm’s IT asset mix. Given the highly innovative nature of the IT sector, we expect that the priceperformance ratio of IT hardware will continue well into the future, making the use of appropriate IT price indexes crucial to precise empirical coefficient estimates and meaningful analysis results.

Second, as argued by Jorgenson and Griliches (1967), for the purposes of production function estimation, the appropriate measure of inputs is the flow of services from assets that are used, but not consumed, in the production process. Although this approach imposes an additional burden on researchers to calculate rental prices, the data required to do so are publicly available from the BLS. In addition, this approach avoids capital aggregation biases inherent in the capital stock approach, and is theoretically consistent with the production function approach commonly used in the IT returns area of research.

The managerial implications of this research arise from the ongoing shift in the use of labor, non-IT capital, and IT capital driven by changes in their relative prices. As long as price and quality improvements in IT continue, demand for IT should remain strong, providing opportunities for IT-producing firms and IT service firms. Continued investment in IT innovation and new product development is prudent for firms assisting in adoption and implementation of new technologies.

Given our finding that IT is a net complement to non-IT capital, we expect investments in non-IT capital to increase along with those in IT. Because IT has a central role in the new information economy, managers should explore different ways to apply IT in conjunction with other forms of capital to enable new business processes that reduce costs, increase revenues, or improve quality. In addition, as a result of the continued price and quality improvements in IT, managers should continue to look for additional ways to reduce labor requirements and related costs. Interestingly, in the United States, this laborsaving technological change is currently being reinforced by the growth of IT-enabled “offshoring” of labor services to developing economies. Although the ability of firms to produce more output with a smaller workforce is an indication of improved productivity and efficiency of operations—both of which are now necessities for competitiveness in the global economy—programs may be needed to reduce the short-term impact of the reduced labor requirement. Retraining is one such program that will help minimize any negative impacts and enable the workforce to move to growing sectors of the economy and enjoy higher real wages in the long run.

## 5.3. Conclusions and Future Research

Overall, our analysis highlights the central role of technological progress in the evolving nature of information technology as a production factor in developed economies. Although our main findings are strong, several questions emerge that provide fruitful opportunities for future research. First, although we found strong results for two broad categories of hardware—decentralized versus centralized—future research might examine a broader set of information systems categories, perhaps including software.<sup>11</sup> Second, our findings are generated from a firmlevel analysis. As with the case of other important streams of literature, such as the energy-capital substitution debate (David et al. 2000), future research at the industry level using cost-function approaches and other measures of substitutability (e.g., Morishima elasticity of substitution) would provide additional empirical evidence. This would also inform the types of general technology investments that may be needed within specific industries (e.g., decentralized IT to enable offshore outsourcing). Future macroeconomy analysis, such as comparing developed economies with emerging economies, would provide a crucial examination of whether the use of information systems by local economies is influenced by local market conditions (Kraemer et al. 2006, Dewan and Kraemer 2000). Third, future research might examine specific industries or differences across industries to determine the extent to which differing types and uses of IT in the organizational context, especially small and medium-sized organizations, may be reflected in the substitutability of IT for ordinary capital and labor.<sup>12</sup> Finally, an open question is whether the price elasticity of demand for information technology is becoming less elastic over time in the 2000s. Our estimates of the price elasticity of demand for IT in the 1990s are lower than those in earlier research addressing the 1970s and 1980s. However, future research examining more recent periods, say, 2000–2007, would address the question of whether this result is stable, on par with other general-purpose technologies, or merely a temporary phenomenon.

## Acknowledgment

Ronald Ramirez is the corresponding author for this paper.

## References

Aizcorbe, A., K. Flamm, A. Khurshid. 2002. The role of semiconductor inputs in IT hardware price decline: Computers vs. communications. Finance and Economics Discussion Series. Board of Governors of the U.S. Federal Reserve Systems, Washington, DC, 2002–2037.

Allen, R. 1938. Mathematical Analysis for Economists. St. Martin’s, New York.

Apostolakis, B. E. 1990. Energy-capital substitutability/complementarity: The dichotomy. Energy Econom. 12(1) 48–58.

Aral, S., P. Weill. 2007. IT assets, organizational capabilities and firm performance: How resource allocations and organizational differences explain performance variation. Organ. Sci. 18(5) 1–18.

Barua, A., B. Lee. 1997. The information technology productivity paradox revisited: A theoretical and empirical investigation in the manufacturing sector. Internat. J. Flexible Manufacturing Systems 9(2) 145–166.

Berndt, E. R., N. J. Rappaport. 2001. Price and quality of desktop and mobile personal computers: A quarter century historical overview. Amer. Econom. Rev. 91(2) 268–273.

Berndt, E., Z. Griliches, N. Rappaport. 1995. Econometric estimates of price indexes for personal computers in the 1990’s. J. Econometrics 68(1) 243–268.

Bresnahan, T., E. Brynjolfsson, L. Hitt. 2002. Intangible assets: Com puters and organizational capital. Brookings Papers Econom. Activity 1 138–199.

Brynjolfsson, E. 1996. The contribution of information technology to consumer welfare. Inform. Systems Res. 7(3) 281–300.

Brynjolfsson, E., L. Hitt. 1995. Information technology as a factor of production: The role of differences among firms. Econom. Innovation New Tech. 3(4) 183–199.

Brynjolfsson, E., L. Hitt. 1996. Paradox lost? Firm-level evidence on the returns to information systems spending. Management Sci. 42(4) 541–558.

Brynjolfsson, E., L. Hitt. 2000. Beyond computation: Information technology, organizational transformation and business perfor mance. J. Econom. Perspect. 14(4) 23–48.

Brynjolfsson, E., L. Hitt. 2003. Computing productivity: Firm-level evidence. Rev. Econom. Statist. 85(4) 793–808.

Brynjolfsson, E., L. Hitt, S. Yang. 2002. Beyond computation: Information technology, organizational transformation, and busi ness performance. J. Econom. Perspect. 14(4) 23–48.

Chun, H., S. Mun. 2006. Substitutability and accumulation of information technology capital in U.S. industries. Southern Econom. J. 72(4) 1002–1015.

Chwelos, P. 2003. Approaches to performance measurement in hedonic analysis: Price indexes for laptop computers in the 1990s. Econom. Innovation New Tech. 12(3) 199–224.

David, P. A., B. Hall, A. A. Toole. 2000. Is public R&D a complement or substitute for private R&D? A review of the econometric evidence. Res. Policy 29(4–5) 497–529.

De La Grandville, O. 1997. Curvature and the elasticity of substitution: Straightening it out. J. Econom. 66(1) 23–34.

Dewan, S., K. L. Kraemer. 2000. Information technology and productivity: Evidence from country-level data. Management Sci. 46(4) 548–562.

Dewan, S., C. Min. 1997. The substitution of information technology for other factors of production: A firm level analysis. Management Sci. 43(12) 1660–1675.

Doms, M., C. Forman. 2005. Prices for local area network equipment. Inform. Econom. Policy 17 365–388.

Efron, B., R. J. Tibshirani. 1993. An Introduction to the Bootstrap. Chapman & Hall, New York.

Eldridge, L. P. 1999. How price indexes affect BLS productivity measures. Monthly Labor Rev. 2 35–46.

Gordon, R. J. 1990. The Measurement of Durable Goods Prices. University of Chicago Press, Chicago.

Gordon, R. J. 2006. Will diminishing returns in technology turn out the lights on future productivity growth? Presentation, WISE 2006, Evanston, IL.

Griliches, Z. 1995. Comment on measurement issues in relating IT expenditures to productivity growth. Econom. Innovation New Tech. 3 317–321.

Grimm, B. T. 1998. Price indexes for selected semiconductors, 1974–1996. Survey Current Bus. 78(2) 8–24.

Gurbaxani, V., S. Whang. 1991. The impact of information systems on organizations and markets. Comm. ACM 34(1) 59–73.

Gurbaxani, V., N. Melville, K. Kraemer. 1998. Disaggregating the return on investment to IT capital. Proc. Internat. Conf. Inform. Systems, International Conference on Information Systems, Helsinki, Finland.

Hendel, I. 1999. Estimating multi-discrete choice models: An application to computerization returns. Rev. Econom. Stud. 66 423–446.

Hicks, J. 1932. The Theory of Wages. Macmillan, London.

Jorgenson, D. W., Z. Griliches. 1967. The explanation of productivity change. Rev. Econom. Stud. 34 249–283.

Kraemer, K. L., J. Dedrick, N. P. Melville, K. Zhu. 2006. Global E-Commerce: Impacts of National Environment and Policy. Cambridge University Press, New York, 466.

Landefeld, J. S., B. T. Grimm. 2000. A note on the impact of hedonics and computers on real GDP. Survey Current Bus. 80(12) 17–22.

Lichtenberg, F. R. 1995. The output contributions of computer equipment and personnel: A firm-level analysis. Econom. Innovation New Tech. 3(3–4) 201–217.

Melville, N., V. Gurbaxani, K. Kraemer. 2007. The productivity impact of information technology across competitive regimes: The role of industry concentration and dynamism. Decision Support Systems 43(1) 229–242.

Melville, N., K. Kraemer, V. Gurbaxani. 2004. Information technology and organizational performance: An integrative model of IT business value. MIS Quart. 28(2) 283–322.

Milgrom, P., J. Roberts. 1990. The economics of modern manufacturing: Technology, strategy, and organization. Amer. Econom. Rev. 80(3) 511–528.

Moulton, B. R. 2001. The expanding role of hedonic methods in the official statistics of the United States. U.S. Bureau of Economic Analysis, U.S. Department of Commerce, Washington, DC. http://www.bea.gov/bea/about/expand3.pdf.

Nordhaus, W. D. 2002. Productivity growth and the new economy. Brookings Papers Econom. Activity 2 211–265.

Oum, T. H. 1989. Alternative demand models and their elasticity estimates. J. Transport Econom. Policy 23(2) 163–187.

Pollak, R. H., R. C. Sickles, T. J. Wales. 1984. The CES-translog: Specification and estimation of a new cost function. Rev. Econom. Statist. 66(4) 602–607.

Prince, J. 2008. Repeat purchase amid rapid quality improve ment: Structural estimation of demand for personal computers. J. Econom. Management Strategy 17(1) 1–33.

Stiroh, K. J. 2002. Information technology and the U.S. productivity revival: What do the industry data say? Amer. Econom. Rev. 92(5) 1559–1576.

Sturgeon, T. J. 2002. Modular production networks: A new American model of industrial organization. Indust. Corporate Change 11(3) 451–496.

Triplett, J. E. 2004. Handbook on quality adjustment of price indexes for information and communication technology products. Working paper, OECD Directorate for Science, Technology and Industry, OECD, Paris.

Van Reenan, J. 2006. The growth of network computing: Qualityadjusted price changes for network servers. Econom. J. 116(February) 29–44.

Zuboff, S. 1985. Automate/informate: The two faces of intelligent technology. Organ. Dynam. 14(2) 5–18.
