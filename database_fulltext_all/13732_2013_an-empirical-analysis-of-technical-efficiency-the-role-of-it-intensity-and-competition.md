---
otero_id: 13732
otero_key: "F5XWR349"
title: "An Empirical Analysis of Technical Efficiency: The Role of IT Intensity and Competition"
authors: "Young Bong Chang; Vijay Gurbaxani"
year: "2013"
journal: "Information Systems Research"
doi: "10.1287/isre.1120.0438"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Empirical Analysis of Technical Efficiency: The Role of IT Intensity and Competition

Young Bong Chang School of Business, SungKyunKwan University, Seoul, Republic of Korea 110-745, ybchang01@gmail.com

Vijay Gurbaxani

Center for Digital Transformation, The Paul Merage School of Business, University of California, Irvine, California 92697, vgurbaxa@uci.edu

W<sup>e</sup> <sup>analyze</sup> <sup>the</sup> <sup>impact</sup> <sup>of</sup> <sup>information</sup> <sup>technology</sup> <sup>(IT)</sup> <sup>on</sup> <sup>the</sup> <sup>technical</sup> <sup>efficiency</sup> <sup>of</sup> <sup>firms</sup> <sup>in</sup> <sup>the</sup> <sup>context</sup> of their observed competitive settings. Because competition can be a driver of efficiency and industries display varying degrees of competitiveness, firm-level efficiency is likely to display considerable heterogeneity. To shed light on these questions, we analyze the economic impact of IT on technical efficiency, a key component of efficiency, in heterogeneous competitive settings. Our study employs a number of econometric techniques, including a stochastic frontier and a generalized method of moments approach, on data from firms in a wide cross-section of industries. We find, after controlling for firm-level heterogeneity and potential endogeneity, that IT is positively associated with gains in technical efficiency but its impact is moderated by the degree of competition. Firms display large variation in their levels of technical efficiency partly because of the heterogeneous market competitiveness conditions they face. In more competitive industries, firms tend to deploy IT more intensively and use it more efficiently. Our study makes a distinct contribution relative to prior studies that have focused on the productivity impacts of IT while assuming perfect competition and not allowing for potential heterogeneity in firm-level efficiency. Overall, our results demonstrate that IT and competition are significant determinants of gains in technical efficiency and provide insight into how competition affects the returns to IT investment.

Key words: technical efficiency; competition; productivity; economics of IS; business value of IT History: Anitesh Barua, Senior Editor; Siva Viswanathan, Associate Editor. This paper was received on August 10, 2009, and was with the authors 20 months for 3 revisions. Published online in Articles in Advance.

## 1. Introduction

Expenditures on information technology (IT) by U.S. firms have grown rapidly over the last 50 years, peaking at almost half of new capital investment in the late 1990s, although recent growth has slowed in the current economic downturn (Computerworld 2010). Not surprisingly, U.S. non-farm business sectors achieved rapid productivity improvement in the late 1990s with the average growth rate rising to 2.7% (Jorgenson and Stiroh 2000, Stiroh 2002). Because IT constitutes a significant and increasing share of total capital, there has been widespread examination of the relationship between IT investment and productivity growth. The consensus view now is that IT contributes significantly to productivity and to output growth (Jorgenson and Stiroh 2000, Brynjolfsson and Hitt 2003, Dedrick et al. 2003).

Productivity growth results from both technical progress and efficiency improvement (Fare et al. 1994, Banker et al. 2005). Technical progress shifts the production possibility frontier outwards and can be achieved by employing new technologies or by introducing product and process innovations. An example of technical progress is the migration to a new business model or a reengineered process enabled by solutions based on the complementary set of mobile and cloud technologies. In contrast, efficiency gains are achieved when firms move up the production possibility frontier by extracting more output from any given set of inputs and extant technology. For instance, firms can improve the quality of decision making, and as a result the performance of operating processes such as supply chain or customer acquisition, through the use of business intelligence software that enables the application of sophisticated analytics on existing data.

Moreover, multiple firms can achieve efficiency gains when superior management practices diffuse from one firm to others (Basker 2005, Nishimizu and Page 1982, Barros 2008). Increases in the intensity of IT capital, competition, and their interaction can accelerate this process. For instance, increases in IT intensity, especially as manifested in interorganizational systems, can lead to a greater level of sharing of both IT and business know-how between trading partners (Chang and Gurbaxani forthcoming). In addition, managers may be more motivated to adopt best practices and reduce managerial slack in more competitive environments (Wilson and Jadlow 1982, Hart 1983). In our context, increased competition would lead to firms’ becoming more efficient in the leveraging of IT. As a result, variation in IT intensity, in the degree of competition, and their interaction may lead to observed differences in efficiency levels across firms and industries.

Traditional productivity studies do not account for these differences at the individual firm level. For instance, the role of differences in efficiency levels between firms as an explanatory factor for the considerable variation in firm-level productivity growth has not been examined. Moreover, increased competition compels firms to adapt to changes in the market by exploiting input resources more efficiently. In fact, the consensus view of the impact of IT on productivity growth derives mainly from studies that implicitly assume perfect competition (Dewan and Min 1997, Brynjolfsson and Hitt 2003) and therefore cannot assess whether IT and increased competition help firms move closer to the production frontier. Specifically, the relationship between IT and efficiency and how it is moderated by competition are not well understood. In particular, because technological progress in IT is particularly rapid and can contribute substantially to productivity improvement, it is important to isolate the payoff that accrues from efficiency gain, which is a key dimension of firm performance. Given the perception that the return on existing IT investments often do not meet expectations, it is important to develop a more detailed understanding of the mechanisms by focusing on efficiency as a determinant of economic value.

These considerations lead to the following key research questions. Although it is well recognized that firms receive a productivity payoff from IT investment, is the efficiency impact significant and does it vary among firms? Which mechanisms allow firms to achieve greater improvements in efficiency? In this paper, we examine the contribution of IT to technical efficiency levels and consider the moderating impact of competition. Although economic efficiency can be decomposed into technical and allocative efficiency<sup>1</sup> (Farrell 1957, Green and Mayes 1991), we focus on technical efficiency because of its demonstrated importance as a determinant of firm performance (Leibenstein 1966, Daly et al. 1985, Green and Mayes 1991, Amess 2003). Of course, firm performance can also be affected by allocative efficiency.<sup>2</sup> However, empirical evidence suggests that estimates of technical efficiency do not depend on whether a firm achieves allocative efficiency, validating the appropriateness of this approach (Schmidt and Lovell 1980, Kalirajan and Shand 1992). Following this common practice in the stochastic frontier estimation literature, we focus on technical efficiency and judge that we can measure it with reasonable precision.<sup>3</sup>

In the IT context, the study of technical efficiency is particularly relevant. Prior studies have reported large variation in firm-level returns to IT investment (Brynjolfsson and Hitt 2000, Gilchrist et al. 2001), suggesting the likelihood of considerable variation in their underlying technical efficiency.<sup>4</sup> Yet productivity analyses implicitly assume that all firms are equally technically efficient. In our analysis, we refine the methodology of traditional productivity studies by allowing for variation in technical efficiency levels and by considering heterogeneous competitive environments. Our approach enables us to assess the level of efficiency with which firms exploit IT relative to their peers and whether and how the degree of competition influences the impact of IT.

We begin by building the firm-level stochastic frontier function to estimate the level of technical efficiency. We conduct our analysis on a pooled sample of firms in multiple industries and in the manufacturing and non-manufacturing industries separately to control for differences in the nature of production between these two sectors. Because the production function is a restricted form of the stochastic frontier function, we also replicate prior productivity studies and confirm IT’s positive impact. We find that increases in the intensity of both IT and ordinary capital improve technical efficiency. That is, incremental investment in IT and ordinary capital enables firms to move closer to the production frontier. When interpreted in conjunction with our productivity results, these findings indicate that improved efficiency is an important source of productivity gains for the firms in our sample. Interestingly, IT has a greater impact than ordinary capital on technical efficiency. Overall, firms operating in more competitive environments tend to invest more in IT and achieve higher levels of efficiency. Moreover, a significant portion of the improvement in efficiency from IT investments can be attributed to the degree of competition. Interestingly, less efficient firms can accelerate the achievement of improvement of efficiency by increasing their IT investment.

To the best of our knowledge, this is one of very few studies that assess the impact of IT on efficiency gains in the context of heterogeneous competitive environments and especially its role in accelerating efficiency improvement. Although some notable studies (Lee and Barua 1999, Shao and Lin 2002) have examined the efficiency impact of IT, they do not consider the moderating role of competition and whether there are differences in the available opportunities to exploit IT based on differences in existing efficiency levels. Lee and Barua (1999) find that manufacturing firms reduce inefficiency by deploying more IT in their production processes. They also show that the magnitude of inefficiency has decreased over time, which they argue is due to learning effects in IT management. Shao and Lin (2002) use data envelopment analysis (DEA) to show that IT has a positive impact on technical efficiency possibly because of the ability of IT to enable better resource utilization and decision making. Because technical efficiency is a component of productivity, they argue that the positive association of IT with productivity results partially from enhanced technical efficiency. One study (Melville et al. 2007) does examine the role of competition in IT returns. However, its focus is on productivity that, as discussed earlier, includes both technical progress and efficiency. Accordingly, the role of efficiency improvements in the positive IT payoff in the study is unclear. We provide a fuller understanding of the mechanisms by which IT enables economic gains by focusing on technical efficiency as the output measure. In sum, our study builds on the previous literature and makes significant new contributions by shedding light on the mechanism by which the degree of competition and IT interact to shape a firm’s efficiency level.

The paper is organized as follows. In §2, we provide a review of the relevant literature. In §3, we provide analytical frameworks of how IT and competition affect efficiency. We describe the data in §4. Empirical results are provided in §5. Section 6 concludes.

## 2. Literature Review

We review two related research streams in the literature: the economic impacts of IT and the role of competition in IT-enabled value creation. We begin by reviewing the literature on the economic impacts of IT that has generally focused on productivity as an output measure and conclude that it is valuable to study efficiency as an alternative to productivity. We then review the literature that considers the impact of competition on firm performance, which we recognize as an important moderator of value creation.

## 2.1. IT, Productivity, and Efficiency

The relationship between IT investment and productivity has been the subject of considerable research (see Dedrick et al. 2003 for an excellent review). At the firm level, these studies have mainly focused on the economic contributions of IT to productivity using the production function approach. The impact of IT on aggregate economic growth has also been the focus of inquiry (Jorgenson and Stiroh 2000). At this level of analysis, economists have typically adopted a growth accounting approach, which relies on neoclassical economic assumptions, to measure productivity.

Most studies in this line of research find that IT has a positive impact on productivity at the firm and industry levels. For instance, some studies show positive IT returns using U.S. firm-level data (Brynjolfsson and Hitt 1995, Dewan and Min 1997, Hitt and Brynjolfsson 1996, Melville et al. 2007). Their estimates of the output elasticity of IT range from 0.03 to 0.1. More recent studies report that in specific industries, such as the IT-producing industry and other IT-intensive industries, the impact of IT is larger than what neoclassical theory would predict (Gilchrist et al. 2001, Stiroh 2002). They also show that in other industries, such as those with low ITintensity, firms receive limited benefits from their IT investments (Gilchrist et al. 2001, Stiroh 2002). These findings are consistent with Brynjolfsson and Hitt (2000), who show that there are large variations in returns to IT investment. In sum, the consensus view is that IT creates considerable economic impact but that the impact varies across firms or industries.

Although previous studies have addressed the economic impact of IT in terms of productivity growth, there is a limited understanding of whether firms deploy IT efficiently to improve their performance. For instance, an inefficient firm that does not fully exploit inputs including IT may be categorized as productive when technical progress is rapid as is the case with IT (Fare et al. 1994, Banker et al. 2005).<sup>5</sup> That is, a firm’s productivity can be increased by technical progress without improvements in its efficiency level. So although the literature allows us to say conclusively that IT contributes to productivity, we cannot say whether firms do so efficiently (Lee and Menon 2000). Surprisingly, relatively little attention has been paid to gauge the economic impacts of IT on efficiency.

One of the first studies to focus on IT and efficiency was conducted by Banker et al. (1990). Using the DEA approach, they found that restaurants became more efficient when they were equipped with (then) advanced IT such as point-of-sale (POS) systems. Using a similar approach, Shao and Lin (2002) found that IT has a positive impact on technical efficiency. They argue that IT supports better management and smoother communications within an organization, resulting in higher efficiency. Lee and Barua (1999) studied the efficiency of manufacturing firms using the stochastic frontier function approach that allows for potential inefficiencies in production. They found that inefficiencies were prevalent in their sample, possibly because of underutilized IT capital in the production process. They argue that firms cannot fully exploit IT capital in the short run as a strong substitute for non-IT capital given the time required for deployment and training. However, their analysis suggests that firms did achieve higher efficiency levels with increases in IT intensity over time.

Although the efficiency analyses reviewed above complement productivity studies, their focus is on demonstrating the existence of inefficiency and a causal relationship between IT and efficiency. Accordingly, they do not try to explain the underlying factors that lead to differences in IT returns across firms. In this paper, by building on earlier research, we are able to uncover the mechanisms by which IT payoffs, or efficiency gains in our context, accrue differently to firms. Specifically, we aim to address this gap in the literature by examining the moderating effects of competition on the efficiency impacts of IT.

## 2.2. Competition, Productivity, and Efficiency

Many studies have examined the relationship between competition and efficiency or productivity (Tirole 1988). In general, the industrial organization literature has argued that a higher degree of competition induces firms to be more productive or efficient (Hart 1983, Hay and Liu 1997, Winter 1971). Efficiency gains are expected to occur because competition reduces managerial slack by providing managers with stronger incentives to make their best effort (Hart 1983, Winter 1971). For instance, limited information or agency issues may result in the adoption of inefficient technology because owners cannot perfectly monitor managers (Hay and Liu 1997). When the degree of competition is high, however, the survival imperative “forces” managers to choose the best technology. As a result, competition eventually encourages investment in the best technology, leading to industry-wide efficiency (Winter 1971).

Also, a firm’s performance could be more sensitive to management effort when the product market is competitive (Willig 1987) making it easier for owners to recognize whether poor performance stems from managerial slack or from other industry-wide shocks. In such cases, managers have stronger incentives to improve efficiency (Willig 1987). This is consistent with the well-known X-inefficiency theory in that less competitive pressure allows opportunistic behavior by managers so that overall efficiency declines (Primeaux 1977). In summary, competitive pressure is viewed as a mechanism that reduces possible inefficiency by decreasing managerial slack.

Studies have also shown empirically the positive impact of competition on efficiency and productivity (Caves and Barton 1990, Hay and Liu 1997, Gort and Sung 1999). Caves and Barton (1990) estimate technical efficiency using a large U.S. manufacturing data set and find that the concentration ratio is inversely associated with efficiency levels. In a study of 19 UK manufacturing sectors, Hay and Liu (1997) show that firms in a more competitive environment are likely to improve efficiency by increasing capital investment. The U.S. telephone industry has also achieved significant productivity growth via induced market competition after the deregulation of long-distance telephone services (Gort and Sung 1999). Their study shows that competition encourages firms to better exploit existing capital and infrastructure, resulting in efficiency gains.

Taken together, these studies have shown the importance of competition as a driver of increased efficiency and productivity. Because productivity growth is a composite of technical progress and efficiency improvement, it is predictable that competition will impact productivity through efficiency gains and technical progress.

## 2.3. IT, Efficiency, and Competition

As we have seen above, studies have demonstrated both the productivity and efficiency impacts of IT. Research has also shown that increases in industrywide competition drive firms to accrue greater productivity impact from their IT investments (Melville et al. 2007). Because increased competition in general leads to improved efficiency, it is reasonable to infer that competition should also moderate the impact of IT on efficiency. There is some early evidence of the moderating role of competition on IT adoption and its impact on industry-level efficiency. For example, studies have found that Wal-Mart’s success with IT stimulated competitive pressure in the retail sector, resulting in industry-wide IT adoption and efficiency (McKinsey Global Institute 2001, Basker 2005). Cooper et al. (2000) argue using case study evidence that firms leverage IT to improve their strategic position in the presence of competition. As a result, we expect competition to be an influential moderator of the efficiency impact of IT, with an increase in industry competitiveness resulting in an increase in IT’s impact.

Moreover, as a general purpose technology, IT has a large variety of potential uses that typically require complementary investments in organization capital to realize the full benefits (Brynjolfsson and Hitt 2003, Brynjolfsson and Saunders 2009). Given the managerial discretion inherent in making the corresponding organizational investments, we expect competition to be an influential moderator of IT’s efficiency impacts, particularly when compared to the deployment of other forms of capital. Non-IT, or ordinary, capital is largely composed of specialized or mature technologies that are utilized by fewer users, where the associated techniques for deriving value are better understood, and that perhaps require less managerial discretion (David 1990). As a result, we conjecture that the moderating role of competition influences IT’s impact on efficiency more so than that of ordinary capital.

## 3. Analytical and Empirical Strategy

In this section, we describe our conceptual framework and the resulting empirical strategy. We begin, however, by distinguishing between efficiency and productivity.

## 3.1. Efficiency and Productivity

Efficiency and productivity are closely related but distinct concepts. Firms are technically efficient when they produce the maximum potential output for any given input vector and production technology (Kumbhakar and Lovell 2000).<sup>6</sup> On the other hand, as discussed earlier, productivity improvements result from both technical progress, as would be the case when firms acquire better production technologies, and from efficiency gains when firms generate more output from the same inputs, holding technology constant (Fare et al. 1994, Banker et al. 2005).

The relationship of efficiency to productivity can be specified as follow $\mathrm { { s } } ; 7$ First, an output distance function $D F ^ { t } ( x ^ { t } , y ^ { t } )$ is defined at time t as

$$
D F ^ {t} (x ^ {t}, y ^ {t}) = \min \{\theta \colon (x ^ {t}, y ^ {t} / \theta) \in S ^ {t} \},\tag{1}
$$

where $x ^ { t }$ is the input vector, $y ^ { t }$ is the output vector, and $S ^ { t }$ is production technology, which consists of all feasible input/output vectors for the given technology.

 is a scale that reflects the extent to which output increases with extant input resources. When  equals 1, a firm’s technology is on the production frontier; namely, it is technically efficient. When  is less than 1, a firm can still expand output proportionally by the difference between  and 1. For instance, if  is 0.5, a firm could double its output by achieving technical efficiency. Therefore,  reflects how efficiently a firm uses inputs to produce output y at time t. Then, productivity change can be decomposed into technology change and efficiency as<sup>8</sup>

$$
\begin{array}{c} \frac {D F ^ {t} (x ^ {t + 1} , y ^ {t + 1})}{D F ^ {t} (x ^ {t} , y ^ {t})} \\ = \frac {D F ^ {t} (x ^ {t + 1} , y ^ {t + 1})}{D F ^ {t + 1} (x ^ {t + 1} , y ^ {t + 1})} \times \frac {D F ^ {t + 1} (x ^ {t + 1} , y ^ {t + 1})}{D F ^ {t} (x ^ {t} , y ^ {t})}. \end{array}\tag{2}
$$

Following the literature (Fare et al. 1994), we define productivity change as the product of the change in technological progress and the change in efficiency from one period to the next. The first term on the right-hand side of Equation (2) measures the extent of technical progress by comparing the distance function for the same set of inputs and output in periods t and $t + 1$ . When there is no technological change, the distance from the production frontier is the same in both periods and the ratio equals 1. In the presence of technical progress, the maximum potential output with the extant production technology in the period is greater at $t + 1$ than at t. That is, the value of the distance function evaluated at $( x ^ { t + 1 } , y ^ { t + 1 } )$ in period t is od/oc in Figure 1, which is greater than 1. In Figure 1, for instance, a firm produces $y ^ { t + 1 }$ using input level $x ^ { t + 1 }$ with extant technology in period $t + 1$ that extends beyond the feasible set of production in period t, illustrating that technical progress has occurred. The second term on the right-hand side of Equation (2) is the efficiency change between the two periods. Because a firm uses $\overset { \smile } { x ^ { t } } ( x ^ { t + 1 } )$ to produce $\mathbf { \dot { \boldsymbol { y } } } ^ { t } ( \boldsymbol { \boldsymbol { y } } ^ { t + 1 } )$ 5 using extant technology, the ratio of the distance function in the numerator and that in the denominator reflects the change in efficiency between the two periods. That is, the term reveals whether production technology is closer to the production frontier or not. We see from this discussion that efficiency gains are positively associated with productivity improvements, whereas improved productivity may not necessarily result from efficiency gains.

Figure 1 The Productivity Index Based on Output Distant Function  
![](/api/attachments/F5XWR349/fulltext/images/6087a0a38a1ba7bb98622d03df6001b0662ef8458ebefa8d0deeb7f6bdda9550.jpg)  
Source. Fare et al. (1994). Original graphic was modified by restricting benchmark technology to period t.  
<sup>+</sup>: Actual input and output at time t and t + 1.

In sum, efficiency is concerned with the level of output a firm produces relative to the maximum using extant technology, allowing us to extract information on whether a firm utilizes best practices. On the other hand, productivity, which includes technical progress, is the more comprehensive concept.

## 3.2. Modeling Efficiency and Its Determinants

3.2.1. Estimation of Efficiency Using a Stochastic Frontier Function. Since Farrell (1957) suggested a means by which to study efficiency, considerable effort has been made to estimate efficiency levels under various circumstances. These approaches can be divided into two general categories. The first approach is adapted from the nonparametric technique, DEA. This methodology has the advantage that it does not require a specific functional form nor does it impose any distributional assumptions. However, DEA cannot reflect economic fluctuations caused by factors such as a recession or bad weather that can be captured with a stochastic distribution. When the DEA methodology is employed, all deviations from the frontier are considered as inefficiencies because the production frontier is assumed to be deterministic with no random error term. Alternatively, using a stochastic frontier function allows for the capture of economic fluctuations and efficiency levels by imposing distributional assumptions.

After the pioneering work of Aigner et al. (1977), studies in various fields have attempted to apply the stochastic frontier function approach to examine economic efficiency. For instance, in the banking industry, Kaparakis et al. (1994) applied a flexible stochastic frontier function to estimate short run cost inefficiency. In the IT context, Lee and Barua (1999) used the stochastic frontier approach to incorporate potential inefficiencies embedded in the production process for manufacturing firms (Lee and Barua 1999). By doing so, they were able to examine the contributions of IT to efficiency.

Beyond the simple estimation of efficiency, many studies link estimated efficiency levels with firmspecific variables. For instance, Pitt and Lee (1981) investigate the sources of inefficiency in the Indonesian weaving industry by regressing estimated efficiency on firm characteristics. Kirkley et al. (1998) utilize a stochastic frontier function and then examine the relationship between efficiency and characteristics of skills such as education and experience in a fishery.

We construct the stochastic frontier model for panel data as follows:

$$
y _ {i t} = f (K _ {i t}, I T _ {i t}, L _ {i t}) \exp (v _ {i t} - u _ {i t})\tag{3}
$$

where for firm i in period t, $K _ { i t } , I T _ { i t }$ and $L _ { i t }$ are ordinary (non-IT) capital, IT capital, and labor, respectively, and $y _ { i t }$ is output; $f ( \bar { K _ { i t } } , I T _ { i t } , L _ { i t } ) \exp ( v _ { i t } )$ is the stochastic production frontier; $v _ { i t }$ are random variables that are assumed to be i.i.d. with zero mean and variance $\sigma _ { v } ^ { 2 } ;$ and $u _ { i t }$ are nonnegative random variables with mean $m _ { i t }$ and variance $\sigma _ { u } ^ { 2 }$

We further assume, consistent with previous productivity research (Brynjolfsson and Hitt 1995, Dewan and Min 1997, Melville et al. 2007) that $f ( K _ { i t } , I T _ { i t } , L _ { i t } )$ is Cobb-Douglas. Taking the natural log of both sides, we get

$$
\begin{array}{c} \ln y _ {i t} = \tau_ {i} + \alpha_ {1} \ln K _ {i t} + \alpha_ {2} \ln I T _ {i t} + \alpha_ {3} \ln L _ {i t} \\ + c o n t r o l s + v _ {i t} - u _ {i t} \end{array}\tag{4}
$$

where controls include year dummies and industry dummies at the two-digit Standard Industrial Classification (SIC) level.

The error term $v _ { i t }$ captures random noise and $u _ { i t }$ captures the effect of inefficiency arising from a variety of sources such as inefficient use of IT, ordinary capital, or less competitive environments. We allow for time-varying inefficiency $\left( u _ { i t } \right)$ because the production frontier can vary over time for the same firm (Battese and Coelli 1988, Cornwell et al. 1990, Hay and Liu 1997). Our stochastic frontier function also includes firm-specific effects (<sub>i</sub>5 to capture unobserved heterogeneity among firms by taking advantage of panel data properties. We do so because the estimate of efficiency $\left( u _ { i t } \right)$ is likely to be biased when firm-specific effects are not controlled for (Kumbhakar 1991, Kumbhakar and Hjalmarsson 1995). Finally, we include year and industry dummies to control for additional heterogeneity arising from time and industry-specific effects, respectively.

A common approach for estimating inefficiency is to make distributional assumptions by imposing $u _ { i t }$ and $v _ { i t }$ as following the truncated-normal and normal distributions, respectively. Then Equation (4) can be estimated using the maximum likelihood (ML) method to obtain efficiency levels for individual firms by decomposing the error terms into the two parts, $u _ { i t }$ and $v _ { i t }$ (Kumbhakar and Lovell 2000). However, we cannot rule out the possibility that inputs such as IT capital and labor are endogenously determined. One could consider the construction of a system of equations with the first-order condition of profit maximization to address the endogeneity issues (Kumbhakar et al. 1991, Barua and Lee 1997). However, our ML-based estimation technique in the context of a stochastic frontier does not allow us to adopt this estimation strategy without additional data such as input and output prices and cost shares. As an alternative, we estimate the stochastic frontier function with lagged inputs as instruments (Hay and Liu 1997, Wang 2003). Although dependent on the choice of instruments, this approach allows us to examine the sensitivity of our results when we substitute lagged variables for contemporaneous variables (Good et al. 1993, Wang 2003).

Then the efficiency level of an individual firm at time t ranges between 0 and 1 and is defined as follows (Battese and Coelli 1988, Wang 2003):

$$
0 \leq \exp (- u _ {i t}) = \frac {E (y _ {i t} \mid u _ {i t} , K _ {i t} , I T _ {i t} , L _ {i t})}{E (y _ {i t} ^ {*} \mid 0 , K _ {i t} , I T _ {i t} , L _ {i t})} \leq 1,\tag{5}
$$

where $y _ { i t }$ is actual output, and $y _ { i t } ^ { * }$ is potential output when a firm is efficient (i.e., $u _ { i t } = 0 )$

If $u _ { i t }$ is equal to $0 ,$ a firm’s technology is at the frontier level and it produces the maximum output level for its level of inputs. On the other hand, if $u _ { i t }$ is greater than 0, it indicates that a firm’s production lies below the production frontier and that it is technically inefficient.

Following previous studies that use stochastic frontier estimates (e.g., Battese and Coelli 1988), variance terms are parameterized by the variance ratio $( \gamma = \sigma _ { u } ^ { 2 } / ( \sigma _ { u } ^ { 2 } + \sigma _ { v } ^ { 2 } ) )$ to reflect how much variation is explained by the inefficiency terms $\left( u _ { i t } \right)$

3.2.2. Estimation of Factors that Influence Efficiency. Once we obtain efficiency levels for an individual firm using the stochastic frontier function (Equation (4)), the next steps are to identify factors that influence efficiency levels and to estimate the associated parameters. In this section, we investigate the factors that lead to variations in efficiency levels and discuss our estimation strategy. First, as discussed above, research has provided strong evidence that IT improves firm performance. For example, IT capital deepening may allow employees to work more efficiently and productively by automating routine work, streamlining decision processes, and facilitating communication across organizations. Further, a growing body of research has provided evidence of the substantial role of IT in business performance and economic growth (Oliner and Sichel 2000, Basu et al. 2004), possibly due to higher efficiency. Accordingly, we specify a firm’s efficiency levels as a function of IT intensity (IT/L) (see Lee and Barua 1999). Second, ordinary capital may also contribute to efficiency gains via capital deepening just as in the case of IT capital (Krugman 1994, Oum and Zhang 1995, Young 1995, Borsch-Supan 1998).<sup>9</sup> All of these studies emphasize the role of capital accumulation in shaping high performance at the level of firm, industry, and country. Accordingly, we add ordinary capital intensity $( \dot { K } / L )$ to control for efficiency gains via capital deepening. Although the factors IT and K were already considered in the first stage analysis, the stochastic frontier approach separates out the inefficient aspects of input utilization. That is, the effects of inefficiency in input utilization are not captured in the coefficients of the input terms estimated from the stochastic frontier function but rather in ${ u _ { i t } } . ^ { 1 0 }$ Accordingly, the stochastic frontier literature often includes the same input variables in both production and efficiency equations (Pitt and Lee 1981, Battese and Coelli 1995, Shao and Lin 2002, Kompas et al. 2004, Kneller and Stevens 2006). Third, based on X-inefficiency theory (Primeaux 1977) and related literature (Hart 1983, Winter 1971), we include the degree of competition as a factor in efficiency gains. Finally, we include firmspecific effects ( 5 in Equation (6) to capture timeinvariant unmeasured heterogeneity.

Our model also allows for the dynamic nature of efficiency by including variables for lagged efficiency levels and efficiency changes between two successive periods. For instance, a firm’s successful performance in the past may be a result of better management techniques and know-how. Because superior management and know-how typically persist, it is not unusual to assume that a firm’s current efficiency level is correlated with past performance (Nickell 1996, Oulton 1998, Levine et al. 2000, Koke and Renneboog 2005). The lagged efficiency terms in our model allow us to capture these underlying, and likely autocorrelated, heterogeneities (Jacobson 1990). We also account for potential time-varying changes in efficiency. In practice, firms often attempt to improve their efficiency position (Hay and Liu 1997) possibly through unobserved attributes such as improvements in management quality.<sup>11</sup> For instance, efficiency change can be considered as a change in management quality to the extent that the effort to improve management quality leads to a positive change in efficiency (Wheelock and Wilson 2000). Accordingly, we include betweenperiod change in efficiency (from t − 1 to t − 2) to capture these time-varying unobservables such as management quality.<sup>12</sup> Given that one of our foci is to examine the moderating impact of competition, we include interaction terms between IT intensity (and ordinary capital intensity) and competition. Further, we conjecture that firms with higher IT intensity may be better able to improve their efficiency position. We account for this potential interplay by including an interaction term between IT (and ordinary capital) intensity and a firm’s inefficiency. Finally, we incorporate industry (at the two-digit SIC level) and year dummies.

Taken together, the efficiency equation is specified as a function of lagged efficiency, efficiency change, IT intensity, ordinary capital intensity, the degree of competition, and the interaction terms as follows:

$$
\begin{array}{l} \text {eff} _ {i, t} = \eta_ {i} + \lambda_ {1} \text {eff} _ {i, t - 1} + \lambda_ {2} \Delta \text {eff} _ {i, t - 1} \\ \quad + \beta_ {1} (\text {IT intensity}) _ {i, t} + \beta_ {2} (\text {K intensity}) _ {i t} \\ \quad + \beta_ {3} (\text {comp}) _ {i, t} + \beta_ {4} (\text {comp} \times (\text {IT intensity})) _ {i, t} \\ \quad + \beta_ {5} (\text {comp} \times (\text {K intensity})) _ {i, t} \\ \quad + \beta_ {6} ((\text {IT intensity}) _ {i, t} \times \text {ineff} _ {i, t - 1}) \\ \quad + \beta_ {7} ((\text {K intensity}) _ {i, t} \times \text {ineff} _ {i, t - 1}) \\ \quad + \text {controls} + w _ {i, t}, \end{array}\tag{6}
$$

where $e f f$ is efficiency level defined in Equation (5); $\eta _ { i }$ is unobserved firm-specific characteristics; $\Delta e f f _ { t - 1 }$ denotes first differences from t − 1 to t − 2; IT and K intensity are measured as IT and ordinary capital per unit of labor, respectively; comp denotes the degree of competition;<sup>13</sup> ineff is defined as $1 - e f f ;$ controls include dummies for year and for industry at the two-digit SIC level; and $w _ { i t }$ is an error term that is assumed to be i.i.d.

Our model is specified to capture unobserved heterogeneity by including variables for firm-specific effects and dynamics with a lagged dependent variable, making the estimation procedures nontrivial. If all the variables on the right-hand side in Equation (6) are exogenous and there are no lagged dependent variables, we can obtain consistent estimates using ordinary least squares-based techniques such as the fixed effects model (Bond et al. 2003, Dearden et al. 2006). However, in our case, the lagged dependent variable is correlated with the error terms by construction and the other independent variables are likely to be endogenous. More specifically, unobserved firm-characteristics $( \eta _ { i } )$ can become a source of endogeneity bias if they affect both dependent and independent variables. For instance, well managed firms may be able to achieve higher efficiency. For precisely the same reason, these firms may also be better able to exploit IT, resulting in more IT investment. In this situation, the error term $( w _ { i t } )$ and the unobserved firm-specific characteristics $( \eta _ { i } )$ will be correlated, resulting in biased estimated parameters. In addition, inputs such as IT could be simultaneously determined with output leading to a non-zero correlation between inputs and the error term. We use the generalized method of moments (GMM) technique to address these issues (Arellano and Bond 1991, Arellano and Bover 1995, Blundell and Bond 1998). Consistent with the GMM approach, we take the first difference of Equation (6) to remove firmspecific heterogeneity and assume that the error terms are serially uncorrelated. When the error terms $( w _ { i , t } )$ are serially uncorrelated, the first differences follow the first-order moving average, MA(1), whose autocorrelation over the first order is zero (Hamilton 1994). Then we use lagged values of the independent variables as instruments for current period independent variables. In our empirical setting, instruments dated back two periods and earlier<sup>14</sup> can be candidates for valid instruments (Arellano and Bond 1991, Hamilton 1994, Arellano and Bover 1995).<sup>15</sup> The GMM estimators are obtained by instrumenting the differenced variables that are not strictly exogenous with their available lags in levels. This allows us to construct a set of moment conditions as follows:<sup>16</sup>

$$
E (x _ {i, t - s} \Delta w _ {i, t}) = 0 \quad t \geq 4 \text { and } s \geq 2,\tag{7a}
$$

where x is a vector of independent variables on the right-hand side.

However, a firm’s efficiency level may persist to some extent because of innate skills, capabilities, and experience. In such cases, the lagged endogenous variables used as instruments in Equation $( 7 \mathsf { a } )$ are weakly correlated with the first-differenced variables in Equation (6) and can result in substantially biased estimates (Arellano and Bover 1995, Blundell and Bond 1998). To reduce the potential bias resulting from weak instruments, our estimation strategy turns to the system GMM approach by constructing additional moment conditions as follows (Arellano and Bover 1995, Blundell and Bond 1998, Levine et al. 2000):<sup>171</sup> <sup>18</sup>

$$
E (\Delta x _ {i, t - s} (\eta_ {i} + w _ {i, t})) = 0 \quad t \geq 4 \text { and } s \geq 2.\tag{7b}
$$

With appropriate instruments that construct moment conditions (7a) and (7b), the system GMM approach provides consistent estimates while controlling for potential bias from heterogeneity and simultaneity. The underlying idea of GMM is to choose parameters for the right-hand side variables that make the sample moments (Equations (7a) and (7b)) as close to zero as possible (Hamilton 1994). In empirics, we test the validity of our instruments, which form moment conditions (7a) and (7b), by conducting the Hansen test of over-identifying restrictions and the test of autocorrelation in the residuals (see Tables 5 and 6).

## 4. Data

The data for our study are obtained from Compustat and Computer Intelligence InfoCorp (CII).<sup>19</sup> We use Compustat to get financial information on sales, labor, and non-IT capital. The CII database consists of IT investment data from Fortune 1,000 firms, implying that sample data are from large companies.

We use two-digit SIC industry level deflators from the U.S. Bureau of Economic Analysis for output prices. Because CII redefined IT capital starting in 1995, for purposes of consistency we consider a sample period from 1987 to 1994. We discard observations when any input or output variables are missing from the data set. This results in 3,828 observations from the durable and nondurable manufacturing, services, and trade and transportation sectors.

Table 1 Descriptive Statistics for Input and Output Variables

<table><tr><td>Variable</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td></tr><tr><td colspan="5">All (n = 3,828)</td></tr><tr><td>Value added ($M)</td><td>1,613</td><td>3,155</td><td>3.9</td><td>63,104</td></tr><tr><td>K ($M)</td><td>2,474</td><td>4,990</td><td>4.31</td><td>69,464</td></tr><tr><td>L ($M)</td><td>1,014</td><td>2,044</td><td>5.3</td><td>37,108</td></tr><tr><td>IT ($M)</td><td>32.8</td><td>73.9</td><td>0.1</td><td>1,432</td></tr><tr><td>HHI</td><td>0.186</td><td>0.149</td><td>0.02</td><td>1</td></tr><tr><td colspan="5">Manufacturing (n = 2,556)</td></tr><tr><td>Value added ($M)</td><td>1,672</td><td>3,616</td><td>3.9</td><td>63,104</td></tr><tr><td>K ($M)</td><td>2,436</td><td>4,387</td><td>6.88</td><td>69,464</td></tr><tr><td>L ($M)</td><td>1,066</td><td>2,295</td><td>5.3</td><td>37,108</td></tr><tr><td>IT ($M)</td><td>29.7</td><td>69.3</td><td>0.1</td><td>1,210</td></tr><tr><td>HHI</td><td>0.205</td><td>0.148</td><td>0.05</td><td>1</td></tr><tr><td colspan="5">Non-manufacturing (n = 1,272)</td></tr><tr><td>Value added ($M)</td><td>1,495</td><td>2,414</td><td>16.5</td><td>25,643</td></tr><tr><td>K ($M)</td><td>2,552</td><td>5,730</td><td>4.31</td><td>31,116</td></tr><tr><td>L ($M)</td><td>910</td><td>1,651</td><td>13</td><td>21,139</td></tr><tr><td>IT ($M)</td><td>38.9</td><td>79.3</td><td>0.1</td><td>1,432</td></tr><tr><td>HHI</td><td>0.148</td><td>0.142</td><td>0.02</td><td>0.979</td></tr></table>

Descriptive statistics are presented in Table 1. The average value added for a firm is 1.6 billion for the full sample, ranging from \$3.9 million to \$63 billion, consistent with a sample drawn from large firms. The magnitude of IT capital varies from \$0.1 million to \$1.4 billion. The other variables including ordinary capital and labor also show large variations resulting in high explanatory power in regression analyses. When we divide the sample into manufacturing and non-manufacturing sectors, we see that firms in manufacturing are slightly larger on average than those in the non-manufacturing sector in terms of value added. However, IT intensity, measured as IT per unit of labor, is higher in the non-manufacturing sector than in the manufacturing sector.

We construct the widely used Herfindahl-Hirschman index (HHI), which captures industry concentration and is interpreted as an inverse measure of the degree of competition. This index is specified as

$$
H H I _ {j, t} = \sum_ {i = 1} ^ {n _ {j}} s _ {i j, t} ^ {2},\tag{8}
$$

where $s _ { i j , t }$ is the market share of firm i in industry j in year t and $n _ { j }$ is the number of firms in industry j at the three-digit SIC level. Market share is defined as a firm’s sales over total industry sales. Following the usual interpretation in the literature, a higher value of HHI is associated with a lower degree of competition. In general, our sample statistics suggest that the manufacturing sector is more concentrated (less competitive) than is the non-manufacturing sector.

Table 2 IT Intensity by the Herfindahl-Hirschman Index

<table><tr><td>IT intensity</td><td>High competition(low concentration)(%)</td><td>Low competition(high concentration)(%)</td><td>Difference</td></tr><tr><td>All</td><td>4.06 (n = 1,558)</td><td>2.74 (n = 2,270)</td><td>1.32***</td></tr><tr><td>Manufacturing</td><td>3.52 (n = 965)</td><td>2.35 (n = 1,591)</td><td>1.17**</td></tr><tr><td>Non-manufacturing</td><td>5.15 (n = 593)</td><td>3.53 (n = 679)</td><td>1.62***</td></tr></table>

$$
^ {* *} p <   0. 0 5, ^ {* * *} p <   0. 0 1.
$$

Next, we present descriptive statistics for the magnitude of IT intensity categorized by the degree of competition. We divide the sample into two groups based on the HHI index: high competition (below average) and low competition (above average). The average magnitude of IT intensity in the high competition group for the full sample is 4.06%, greater than the average of 2.74% in the low competition group, and the two are statistically different at the 1% level (see Table 2). We also see a similar pattern in the magnitude of IT intensity for the manufacturing and non-manufacturing samples. These findings seem to imply that firms substitute IT for other inputs more aggressively in the presence of competition, resulting in higher IT intensity. This result provides preliminary support for the notion that the degree of competition and IT investment are correlated and motivates a more formal examination of the moderating role of competition in IT value creation.

## 5. Empirical Analysis

In this section, we estimate the levels of technical efficiency using the stochastic frontier function. Then we examine whether IT improves a firm’s technical efficiency and the conditions that moderate its impact.

## 5.1. Estimation Results from

## Production Frontier Function

We estimate Equation (4) using stochastic frontier function analysis. First, note that our study is an extension of traditional productivity studies. One important distinction from prior literature is that we add an error term $( u _ { i t } \ge 0 )$ to the traditional production function. By doing so, we are able to distinguish between firms on the frontier $( u _ { i t } = 0 )$ and firms that are not $( u _ { i t } > 0 )$ . On the other hand, traditional productivity studies assume that all firms are on the frontier by imposing the restriction that the error term $\left( u _ { i t } \right)$ equals 0. In this context, we interpret productivity studies with $u _ { i t } = 0$ as a restricted form of stochastic frontier analysis. Therefore, our efficiency analysis can provide input coefficients estimated from the stochastic frontier function just as productivity analyses do. For instance, the output elasticity of IT capital from the stochastic frontier function lies in the range of 0.013 to 0.048 (see Table 3) depending on the instruments used and the sample. At the high end of the range, this indicates that a 1% increase in IT capital leads to an increase in output of 0.048%. The coefficients of all inputs are precisely estimated with reasonable magnitudes and are consistent with prior studies (Brynjolfsson and Hitt 1995, Dewan and Min 1997, Hitt and Brynjolfsson 1996, Melville et al. 2007). Our study echoes earlier findings that IT has a positive impact on productivity while also providing perspective on its impact on technical efficiency.<sup>20</sup>

The variance ratios $( \gamma = \sigma _ { u } ^ { 2 } / ( \sigma _ { u } ^ { 2 } + \sigma _ { v } ^ { 2 } ) )$ range from 75% to 93% and are all highly significant at the 1% level for all industries in our sample, implying that a significant portion of the variation is captured by the efficiency terms $( - u _ { i t } )$ that are the focus of this paper. Put differently, this level of variation suggests that firm-specific factors may play an important role in the achieved level of efficiency.

The average technical efficiency estimated from Equation (4) suggests that firms in more competitive (less concentrated) environments are closer to the production frontier (see Table 4). This implies that a larger portion of firms in these sectors achieves output levels close to the maximum for their level of inputs possibly because of the higher level of competition. However, this analysis does not allow us to examine the channels through which firms achieve higher efficiency in more competitive environments. We address these issues in the next section.

## 5.2. Estimation Results from the Efficiency Equation

Our production frontier function analysis suggests that the efficiency term $( - u _ { i t } )$ has a significant impact on a firm’s level of production. Accordingly, it is important to examine the factors that may affect the level of efficiency. Earlier, we identified several factors that may affect a firm’s efficiency. These are lagged efficiency, efficiency change, IT and ordinary capital intensity, and the degree of competition and interactions between input intensities and competition and between input intensities and lagged inefficiency.

We begin by assessing our empirical model, estimated using the GMM method. Before presenting our results, we confirm the validity of the set of instruments using the Hansen test (Arellano and Bond 1991). We are not able to reject the null hypothesis that the instrument variables are exogenous at the conventional levels. Second, we need to ensure that there is no serial correlation in the residuals to avoid inconsistent estimates (Arellano and Bover 1995, Blundell and Bond 1998). The test results suggest that the instruments are orthogonal to the error terms and there is no serial correlation (see the last two rows of Table 5).

Table 3 Estimates of Input Coefficients from the Stochastic Frontier Function (Equation (4))

<table><tr><td rowspan="2">Dependent variable: Output</td><td>Estimates with one-year lags</td><td>Estimates with two-year lags</td><td>Estimates with contemporaneous variables</td><td>Estimates with one-year lags</td><td>Estimates with one-year lags</td></tr><tr><td>All</td><td>All</td><td>All</td><td>Manufacturing</td><td>Non-manufacturing</td></tr><tr><td>K</td><td>0.147***(0.009)</td><td>0.138***(0.011)</td><td>0.140***(0.006)</td><td>0.197***(0.012)</td><td>0.103***(0.013)</td></tr><tr><td>L</td><td>0.730***(0.010)</td><td>0.795***(0.014)</td><td>0.841***(0.008)</td><td>0.664***(0.016)</td><td>0.764***(0.014)</td></tr><tr><td>IT</td><td>0.033***(0.006)</td><td>0.035***(0.008)</td><td>0.013***(0.004)</td><td>0.048***(0.008)</td><td>0.021**(0.011)</td></tr><tr><td>Variance ratio</td><td>0.851***(0.022)</td><td>0.753***(0.034)</td><td>0.837***(0.008)</td><td>0.817***(0.028)</td><td>0.928***(0.026)</td></tr><tr><td>Observations</td><td>3,223</td><td>2,643</td><td>3,828</td><td>2,193</td><td>1,030</td></tr></table>

$^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p < 0 . 0 1$ ; standard errors in parenthesis. Industry and year dummies are not reported for expositional brevity.

Table 4 Average Efficiency by the Degree of Competition (HHI)

<table><tr><td></td><td>High competition(less concentrated)</td><td>Low competition(more concentrated)</td></tr><tr><td>All</td><td>0.822 (n = 1,308)</td><td>0.722 (n = 1,915)</td></tr><tr><td>Manufacturing</td><td>0.813 (n = 815)</td><td>0.733 (n = 1,388)</td></tr><tr><td>Non-manufacturing</td><td>0.837 (n = 493)</td><td>0.692 (n = 527)</td></tr></table>

Now that we have validated our model, we begin by assessing the main effect of IT, ordinary capital, and competition on technical efficiency. Columns (i) through (iv) display the results for the full sample with no interaction terms and with different combinations of interaction terms. Columns (v) and (vi) present the results with all interaction terms for the manufacturing and the non-manufacturing sectors. In general, I T , ordinary capital 4K5 intensity, and the HHI index are significantly associated with efficiency and show the expected signs (see Table 5). The coefficient for the lagged efficiency variable is positive and significant at the 1% level in all specifications, reflecting the notion that a firm’s efficiency level persists to some extent possibly because of inherited heterogeneities. The coefficient of efficiency change, which we believe captures time-varying unobserved heterogeneities, is also positive and significant at the conventional levels except in the case of the manufacturing sector (Column v).

To summarize, both IT and ordinary capital intensity have a direct impact on efficiency gains in most cases. Consistent with our expectation, reduced competition results in lower levels of firm efficiency. We conduct the Wald test to check whether the magnitudes of the coefficients of IT and ordinary capital are statistically different. We are able to confirm at the 1% significance level that the main impact of IT is greater than that of ordinary capital in all our model specifications except in the case of the non-manufacturing sector (Column vi).

Although the analysis generally supports the positive impact of IT intensity and competition on efficiency, our main interest is in examining how the impact of IT varies with the degree of competition. As expected, the estimated coefficients of the interaction terms for efficiency with both IT and capital intensity are negative and significant. This implies that both IT and ordinary capital play a greater role in improving efficiency levels in more competitive environments. Note the magnitudes of the interaction terms between competition and the two capital inputs. In the full sample, we observe a difference in the magnitude of the two terms (see Column iv). Similarly, in the nonmanufacturing sector, the coefficient of the interaction term with IT is −00043 and that of ordinary capital is statistically indistinguishable from 0 (see Column (vi) in Table 5). However, in the manufacturing sector, there is no significant difference in the magnitudes of the moderating effect of competition (−00036 and −00034 for the interaction with IT intensity and K intensity, respectively). We conduct the Wald test and statistically confirm that the interaction of IT and competition has a greater impact on efficiency than that of ordinary capital and competition for the full sample and in the non-manufacturing sector. In general, a firm’s efficiency level responds significantly to increased competition through IT capital and less so through ordinary capital except in the manufacturing sector where ordinary capital is often an important factor of production. In manufacturing, our results suggest that ordinary capital is no less important than IT capital in improving efficiency in the presence of competition.

Our empirical model also controls for the potential interplay between a firm’s IT intensity and its lagged inefficiency. The IS and strategy literatures stress the importance of a firm’s capability to absorb and utilize new knowledge, and IT intensity is often regarded as an important measure of IT capability (Cohen and Levinthal 1990, Bharadwaj et al. 1999, Bharadwaj 2000). For instance, firms with higher levels of IT intensity may be able to exploit IT better to improve efficiency because of the accumulated knowledge and experience associated with higher levels of IT investment. Moreover, it is reasonable to conjecture that less efficient firms have greater potential to improve. As a result, we expect the interaction terms to be positively associated with efficiency. Indeed, we find that these interaction terms are generally positive and statistically significant at the conventional levels (see Columns (iii) through (v)) with the exception of ordinary capital intensity in non-manufacturing (see Column (vi)). Overall, however, our results indicate that firms close efficiency gaps relative to the efficient frontier more rapidly through capital deepening in both IT and ordinary capital, especially when investment intensity is high.

Table 5 The Effect of IT , K , HHI , and Interaction Terms on Efficiency Levels (Equation (6))

<table><tr><td>Dependent variable: Efficiency</td><td>(i)</td><td>(ii)</td><td>(iii)</td><td>(iv)</td><td>(v)</td><td>(vi)</td></tr><tr><td>Lagged efficiency</td><td>0.353***(0.080)</td><td>0.343***(0.079)</td><td>0.562***(0.071)</td><td>0.585***(0.072)</td><td>0.555***(0.114)</td><td>0.594***(0.070)</td></tr><tr><td>Efficiency change</td><td>0.064***(0.016)</td><td>0.061***(0.016)</td><td>0.030**(0.014)</td><td>0.026*(0.014)</td><td>-0.008(0.026)</td><td>0.036**(0.016)</td></tr><tr><td>IT intensity</td><td>0.050**(0.025)</td><td>0.063***(0.021)</td><td>0.050***(0.016)</td><td>0.036**(0.016)</td><td>0.105**(0.050)</td><td>0.020(0.018)</td></tr><tr><td>K intensity</td><td>0.016***(0.002)</td><td>0.020***(0.003)</td><td>0.026*(0.015)</td><td>0.043(0.029)</td><td>0.061***(0.012)</td><td>0.071***(0.056)</td></tr><tr><td>HHI</td><td>-0.017***(0.005)</td><td>0.0002(0.009)</td><td>-0.009*(0.005)</td><td>-0.025***(0.008)</td><td>-0.013**(0.006)</td><td>-0.010*(0.006)</td></tr><tr><td>IT intensity* HHI</td><td></td><td>-0.038***(0.010)</td><td></td><td>-0.025*(0.016)</td><td>-0.036**(0.017)</td><td>-0.043*(0.022)</td></tr><tr><td>K intensity* HHI</td><td></td><td>-0.014**(0.006)</td><td></td><td>-0.018***(0.005)</td><td>-0.034***(0.012)</td><td>-0.001(0.007)</td></tr><tr><td>IT intensity* lagged inefficiency</td><td></td><td></td><td>0.047***(0.016)</td><td>0.045***(0.008)</td><td>0.068*(0.041)</td><td>0.028*(0.015)</td></tr><tr><td>K intensity* lagged inefficiency</td><td></td><td></td><td>0.038***(0.007)</td><td>0.042***(0.007)</td><td>0.051***(0.010)</td><td>0.002(0.007)</td></tr><tr><td>Sales growth</td><td>0.099**(0.047)</td><td>0.121***(0.044)</td><td>0.093**(0.037)</td><td>0.107***(0.040)</td><td>0.113***(0.041)</td><td>0.154**(0.071)</td></tr><tr><td>Leverage</td><td>0.030(0.032)</td><td>0.040(0.032)</td><td>0.018(0.023)</td><td>0.019(0.022)</td><td>0.006(0.024)</td><td>-0.019(0.033)</td></tr><tr><td>Firm size</td><td>0.007(0.005)</td><td>0.006(0.005)</td><td>0.001(0.004)</td><td>0.001(0.004)</td><td>0.006(0.005)</td><td>0.012(0.008)</td></tr><tr><td>Constant</td><td>0.078(0.068)</td><td>0.094(0.072)</td><td>0.144*(0.084)</td><td>0.135(0.087)</td><td>0.217**(0.085)</td><td>0.042(0.135)</td></tr><tr><td>Observations</td><td>2,622</td><td>2,622</td><td>2,622</td><td>2,622</td><td>1,803</td><td>819</td></tr><tr><td>Serial correlation (p-value)</td><td>0.162</td><td>0.285</td><td>0.274</td><td>0.272</td><td>0.254</td><td>0.253</td></tr><tr><td>Instrument validity (p-value)</td><td>0.184</td><td>0.213</td><td>0.224</td><td>0.235</td><td>0.260</td><td>0.227</td></tr></table>

$^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p < 0 . 0 1 ;$ Columns (i) through (iv) present the results with the full sample. Columns (v) and (vi) present the results with manufac turing and non-manufacturing firms, respectively. Standard errors in parenthesis. Industry and year dummies are not reported for expositional brevity

## 5.3. Further Analysis

So far, our analysis was conducted under the premise that competition makes firms more efficient via the better utilization of IT. However, we cannot completely rule out the possibility that IT induces a higher level of competition, which can also lead to the same estimates of the interaction terms of IT intensity and competition. That is, when firms can reshape the landscape of market competitiveness they face by deploying IT, we should empirically expect the interaction term, (IT intensity) ∗ HHI, to be negative. To rule out the alternative explanation, we conduct a Granger-Causality test (Hamilton 1994) between the two variables of interest, competition and IT. The null hypothesis, that competition does not cause any change in IT levels, is rejected at the 5% significance level. This implies that a firm’s IT investment may be affected by the market competitiveness it faces. However, the results do not reject reverse Granger causality, which hypothesizes that IT does not cause any changes in the degree of competition.

Next, we check the robustness of our results to the choice of the measure of competition by using price-cost margin as an alternative measure of industry competitiveness. First, like the HHI index, price-cost margin has been widely used to capture competitive effects (Hall 1988, Nickell 1996, Boone 2000, Aghion et al. 2005). Hall (1988, p. 945) argues that “The most obvious explanation of the finding of price far in excess of marginal cost is market power in the product market.” Boone (2000) suggests that any parameters that would increase the price-cost margin are suitable measures for the measurement of competition. Accordingly, if the empirical results using the two alternative measures of industry competition, HHI and price-cost margin, are qualitatively similar, our findings will be strengthened.

Constructing price-cost margin requires us to observe marginal costs, which are the private information of firms. In empirics, it is not unusual to use average cost as a surrogate for marginal cost and it is considered to be a reasonable approximation to marginal cost (Scherer 1980, Lindenberg and Ross 1981, Aghion et al. 2005, Gaspar and Massa 2006). Here, following prior studies, we first compute the price-cost margin for an individual firm as operating profits over sales (Lindenberg and Ross 1981, Gaspar and Massa 2006). Then we construct an industry-level competition index based on the firm-level price-cost margin as follows (see, e.g., Aghion et al. 2005):

$$
C _ {j, t} = 1 - \frac {1}{n _ {j}} \sum_ {i = 1} ^ {n _ {j}} \mathrm{PCM} _ {i j, t}\tag{9}
$$

where $\mathrm { P C M } _ { i j , t }$ is the price-cost margin of firm i in industry j in year t and $n _ { j }$ is the number of firms in industry j at the three-digit SIC level.

As was the case with HHI, the industry-level competition index based on the price-cost margin is lower (less competitive) for the manufacturing sector than for the non-manufacturing sector. Specifically, the magnitudes of the industry-level competition index for the full sample, the manufacturing sector, and the non-manufacturing sector are 0.880, 0.861, and 0.917, respectively. We also examine the relatedness of these two measures as a robustness check. As expected, the correlation between the two indices is negative and statistically significant at the 1% level $( - \bar { 0 } . 3 2 4 ^ { * * * } , p < 0 . 0 1 )$ . This finding confirms that these two measures are related and reinforces the notion that our estimates for the two measures are reasonably constructed.

Next we replicate our earlier analyses for the full sample with price-cost margin. We once again use the GMM technique to estimate the efficiency equation (Equation (6)), which is appropriate in the presence of potential endogeneity. The results are presented in Table 6. As before, we check instrument validity and test the serial correlation of residuals to ensure that our results are consistently estimated. All test results suggest that our instruments are exogenous and there is no serial correlation in the error terms. Similar to the results with the HHI index, our estimates with the alternative competition index are precisely estimated at the conventional level with expected signs. For instance, the coefficient of the competition index is positive and statistically significant in most cases, implying that competition enhances a firm’s efficiency level. Also similar to our earlier results with HHI, the interaction terms of competition with IT and ordinary capital intensities are statistically significant with the expected signs, and the magnitude of the interaction term with IT is greater than that with ordinary capital. Overall, incorporating the alternative competition index in our analysis leads to qualitatively similar results to those using HHI increasing the robustness of our results.

We further check the robustness of our results to potential endogeneity between IT intensity and efficiency by setting up simultaneous equations as follows:<sup>21</sup>

$$
\begin{array}{l} \text {eff} _ {i, t} = \eta_ {i} + \lambda_ {1} \text {eff} _ {i, t - 1} + \lambda_ {2} \Delta \text {eff} _ {i, t - 1} \\ \quad + \beta_ {1} (\text {IT intensity}) _ {i, t} + \beta_ {2} (\text {K intensity}) _ {i t} \\ \quad + \beta_ {3} (\text {comp}) _ {i, t} + \beta_ {4} (\text {comp} * (\text {IT intensity})) _ {i, t} \\ \quad + \beta_ {5} (\text {comp} * (\text {K intensity})) _ {i, t} \\ \quad + \beta_ {6} ((\text {IT intensity}) _ {i, t} * \text {ineff} _ {i, t - 1}) \\ \quad + \beta_ {7} ((\text {K intensity}) _ {i, t} * \text {ineff} _ {i, t - 1}) \\ \quad + \text {controls} + w _ {i, t} \end{array} \tag {10}\tag{10a}
$$

$$
\begin{array}{r l} I T \text {   intensity } _ {i, t} & = \psi_ {i} + \theta_ {1} (I T \text {   intensity }) _ {i, t - 1} + \phi_ {1} e f f _ {i, t - 1} \\ & \quad + \phi_ {2} \Delta e f f _ {i, t - 1} + \theta_ {2} (\text { comp }) _ {i t} \\ & \quad + \theta_ {3} (\text { comp }) _ {i, t} + \text { controls } + \varepsilon_ {i, t} \end{array} \tag {10b}
$$

where all the variables are defined in the same way as in Equation (6).

In this empirical specification, note that Equation (10a) is identical to Equation (6) but we introduce Equation (10b) to explicitly consider IT intensity as an endogenous variable. Although we could also include an additional equation with competition and IT intensity as dependent and independent variables, respectively, we choose not to do so because our Granger-Causality analysis suggests that IT does not cause any changes in the degree of competition. We use three-stage least squares (3SLS) to estimate Equations (10a) and (10b) and employ two and three-year lagged values as instruments just as we did in the GMM analyses.

Table 6 The Effect of IT , K , Competition Index Based on Price-Cost Margin, and Interaction Terms on Efficiency Levels (Equation (6))

<table><tr><td colspan="7">Dependent variable:</td></tr><tr><td>Efficiency</td><td>(i)</td><td>(ii)</td><td>(iii)</td><td>(iv)</td><td>(v)</td><td>(vi)</td></tr><tr><td>Lagged efficiency</td><td>0.342***(0.080)</td><td>0.324***(0.077)</td><td>0.617***(0.066)</td><td>0.552***(0.079)</td><td>0.501***(0.119)</td><td>0.590***(0.070)</td></tr><tr><td>Efficiency change</td><td>0.064***(0.016)</td><td>0.062***(0.016)</td><td>0.013(0.012)</td><td>0.011(0.024)</td><td>0.024(0.018)</td><td>0.023*(0.012)</td></tr><tr><td>IT intensity</td><td>0.045*(0.025)</td><td>0.032***(0.010)</td><td>0.018*(0.010)</td><td>0.022*(0.013)</td><td>0.045*(0.025)</td><td>0.060(0.039)</td></tr><tr><td>K intensity</td><td>0.018***(0.003)</td><td>0.017***(0.003)</td><td>0.014***(0.004)</td><td>0.012***(0.004)</td><td>0.045***(0.008)</td><td>0.010**(0.054)</td></tr><tr><td>Competition</td><td>0.019***(0.006)</td><td>-0.005(0.012)</td><td>0.070***(0.010)</td><td>0.058**(0.027)</td><td>0.010**(0.005)</td><td>0.015**(0.060)</td></tr><tr><td>IT intensity* Competition</td><td></td><td>0.046*(0.027)</td><td></td><td>0.080***(0.031)</td><td>0.013*(0.077)</td><td>0.090*(0.052)</td></tr><tr><td>K intensity* Competition</td><td></td><td>0.0009*(0.0005)</td><td></td><td>0.020**(0.007)</td><td>0.006***(0.003)</td><td>0.012(0.011)</td></tr><tr><td>IT intensity* lagged inefficiency</td><td></td><td></td><td>0.062***(0.019)</td><td>0.069**(0.033)</td><td>0.025**(0.012)</td><td>0.022*(0.012)</td></tr><tr><td>K intensity* lagged inefficiency</td><td></td><td></td><td>0.050***(0.010)</td><td>0.047***(0.010)</td><td>0.040***(0.010)</td><td>0.003(0.006)</td></tr><tr><td>Sales growth</td><td>0.103**(0.048)</td><td>0.129***(0.039)</td><td>0.030(0.021)</td><td>0.066**(0.028)</td><td>0.105***(0.038)</td><td>0.131**(0.070)</td></tr><tr><td>Leverage</td><td>0.032(0.032)</td><td>0.044(0.031)</td><td>-0.027(0.037)</td><td>-0.010(0.035)</td><td>0.041(0.027)</td><td>-0.015(0.030)</td></tr><tr><td>Firm size</td><td>0.007(0.005)</td><td>0.005(0.005)</td><td>0.007(0.005)</td><td>0.003(0.006)</td><td>0.009(0.005)</td><td>0.017(0.008)</td></tr><tr><td>Constant</td><td>0.099(0.098)</td><td>0.097(0.066)</td><td>0.019**(0.009)</td><td>0.072(0.093)</td><td>0.060(0.006)</td><td>0.015(0.016)</td></tr><tr><td>Observations</td><td>2,622</td><td>2,622</td><td>2,622</td><td>2,622</td><td>1,803</td><td>819</td></tr><tr><td>Serial correlation (p-value)</td><td>0.280</td><td>0.279</td><td>0.109</td><td>0.251</td><td>0.239</td><td>0.273</td></tr><tr><td>Instrument validity (p-value)</td><td>0.126</td><td>0.167</td><td>0.220</td><td>0.148</td><td>0.182</td><td>0.218</td></tr></table>

$^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p < 0 . 0 1 ;$ ; Columns (i) through (iv) present the results with the full sample. Columns (v) and (vi) present the results with manufacturing and non-manufacturing firms, respectively. Standard errors in parenthesis. Industry and year dummies are not reported for expositional brevity.

We present the results from the two equations in Table 7. Although a few estimates are now insignificant because of larger standard errors, the estimates from Equation (10a) are not qualitatively different from the GMM-based estimates from Equation (6). All the coefficients are estimated precisely with the expected signs. In addition, the explanatory power is reasonably high, ranging from 72% to 80%. Turning to Equation (10b), the coefficient for lagged IT intensity is positive and significant at the 1% level. Interestingly, the coefficients for the efficiency terms are positive and statistically significant at the conventional levels across all specifications. This suggests that IT is indeed endogenously determined with respect to efficiency. Our results also suggest that firms in more competitive (less concentrated) industries are more aggressive in making IT investments, which confirms our preliminary analysis (see Table 2). Overall, our results with 3SLS give us more confidence in the causal relationships among the variables we are interested in.

## 6. Discussion and Concluding Remarks

This paper examines the contributions of IT to efficiency levels in the presence of the moderating impact of competition. Our results broadly support the notion that IT intensity, the degree of industry competitiveness, and their interplay are important determinants of efficiency. Specifically, we find that firms achieve bigger efficiency improvements with more intensive investments in IT and in ordinary capital. We further show that firms achieve greater efficiency gains from both IT and ordinary capital in more competitive environments. However, the moderating impact of competition is greater for IT than for ordinary capital. We conjecture that the differences in the underlying investments that constitute IT and ordinary capital, as well as in the managerial effort required to derive the associated efficiency improvements, explain this finding. That is, IT capital reflects an ever-changing set of new technologies and achieving efficiency improvement requires high levels of complementary managerial effort. In contrast, ordinary capital incorporates many mature technologies that are better understood and efficiency improvements likely require less managerial intervention.

Table 7 The Effect of IT , K, HHI, and Interaction Terms on Efficiency Levels (3SLS)—Equations (10a) and (10b)

<table><tr><td>Dependent variable: Efficiency in Equation (10a)</td><td>(i)</td><td>(ii)</td><td>(iii)</td><td>(iv)</td><td>(v)</td><td>(vi)</td></tr><tr><td>Lagged efficiency</td><td>0.452***(0.140)</td><td>0.473***(0.169)</td><td>0.615***(0.141)</td><td>0.652***(0.139)</td><td>0.673***(0.219)</td><td>0.588***(0.150)</td></tr><tr><td>Efficiency change</td><td>0.054***(0.011)</td><td>0.041**(0.020)</td><td>0.035*(0.019)</td><td>0.041*(0.024)</td><td>0.022(0.021)</td><td>0.053**(0.026)</td></tr><tr><td>IT intensity</td><td>0.055*(0.031)</td><td>0.065**(0.026)</td><td>0.040**(0.019)</td><td>0.059**(0.026)</td><td>0.098**(0.047)</td><td>0.042(0.038)</td></tr><tr><td>K intensity</td><td>0.020*(0.011)</td><td>0.023(0.015)</td><td>0.030*(0.016)</td><td>0.059*(0.035)</td><td>0.052*(0.029)</td><td>0.043(0.033)</td></tr><tr><td>HHI</td><td>-0.025**(0.011)</td><td>-0.005(0.005)</td><td>-0.013*(0.007)</td><td>-0.034*(0.018)</td><td>-0.032(0.029)</td><td>-0.028(0.020)</td></tr><tr><td>IT intensity* HHI</td><td></td><td>-0.046**(0.023)</td><td></td><td>-0.033*(0.019)</td><td>-0.042*(0.022)</td><td>-0.033*(0.017)</td></tr><tr><td>K intensity* HHI</td><td></td><td>-0.019**(0.009)</td><td></td><td>-0.020*(0.011)</td><td>-0.036*(0.019)</td><td>0.011(0.013)</td></tr><tr><td>IT intensity* lagged inefficiency</td><td></td><td></td><td>0.052**(0.025)</td><td>0.049***(0.018)</td><td>0.055*(0.032)</td><td>0.030*(0.016)</td></tr><tr><td>K intensity* lagged inefficiency</td><td></td><td></td><td>0.029**(0.014)</td><td>0.043***(0.011)</td><td>0.055***(0.011)</td><td>0.004(0.008)</td></tr><tr><td>Sales growth</td><td>0.121**(0.056)</td><td>0.130**(0.054)</td><td>0.147*(0.087)</td><td>0.155***(0.052)</td><td>0.142***(0.052)</td><td>0.162**(0.087)</td></tr><tr><td>Leverage</td><td>0.037(0.035)</td><td>0.053(0.042)</td><td>0.042(0.033)</td><td>0.029(0.030)</td><td>0.015(0.032)</td><td>0.023(0.037)</td></tr><tr><td>Firm size</td><td>0.012(0.007)</td><td>0.032(0.025)</td><td>0.011(0.014)</td><td>0.007(0.005)</td><td>0.005(0.004)</td><td>0.015(0.012)</td></tr><tr><td>Constant</td><td>0.065(0.061)</td><td>0.119(0.085)</td><td>0.132(0.094)</td><td>0.184(0.127)</td><td>0.199*(0.118)</td><td>0.043(0.127)</td></tr><tr><td>R square</td><td>0.718</td><td>0.744</td><td>0.783</td><td>0.802</td><td>0.793</td><td>0.817</td></tr><tr><td>Dependent variable: IT intensity in Equation (10b)</td><td>(i)</td><td>(ii)</td><td>(iii)</td><td>(iv)</td><td>(v)</td><td>(vi)</td></tr><tr><td>Lagged IT intensity</td><td>0.532***(0.198)</td><td>0.426**(0.201)</td><td>0.498**(0.241)</td><td>0.511**(0.233)</td><td>0.471**(0.239)</td><td>0.561**(0.252)</td></tr><tr><td>Lagged efficiency</td><td>0.032**(0.013)</td><td>0.051***(0.019)</td><td>0.048**(0.024)</td><td>0.044*(0.023)</td><td>0.039*(0.023)</td><td>0.046*(0.025)</td></tr><tr><td>Efficiency change</td><td>0.011*(0.006)</td><td>0.023**(0.012)</td><td>0.019**(0.009)</td><td>0.022**(0.011)</td><td>0.032*(0.017)</td><td>0.024*(0.013)</td></tr><tr><td>HHI</td><td>-0.123**(0.059)</td><td>-0.153*(0.082)</td><td>-0.136*(0.072)</td><td>-0.127**(0.063)</td><td>-0.142*(0.079)</td><td>-0.140**(0.068)</td></tr><tr><td>Sales growth</td><td>0.332*(0.198)</td><td>0.358*(0.211)</td><td>0.429*(0.255)</td><td>0.411*(0.239)</td><td>0.453*(0.242)</td><td>0.399**(0.201)</td></tr><tr><td>Leverage</td><td>-0.198(0.121)</td><td>-0.215*(0.123)</td><td>-0.242*(0.136)</td><td>-0.255*(0.141)</td><td>-0.212*(0.115)</td><td>-0.265*(0.152)</td></tr><tr><td>Firm size</td><td>0.048(0.032)</td><td>0.062(0.043)</td><td>0.056(0.045)</td><td>0.033(0.039)</td><td>0.048(0.054)</td><td>0.035(0.029)</td></tr><tr><td>Constant</td><td>0.198(0.150)</td><td>0.211(0.176)</td><td>0.223(0.177)</td><td>0.211(0.197)</td><td>0.258(0.231)</td><td>0.207(0.187)</td></tr><tr><td>R square</td><td>0.572</td><td>0.587</td><td>0.579</td><td>0.582</td><td>0.565</td><td>0.575</td></tr><tr><td>Observations</td><td>2,622</td><td>2,622</td><td>2,622</td><td>2,622</td><td>1,803</td><td>819</td></tr></table>

$^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p < 0 . 0 1 ;$ ; Columns (i) through (iv) present the results with the full sample. Columns (v) and (vi) present the results with manufac turing and non-manufacturing firms, respectively. Standard errors in parenthesis. Industry and year dummies are not reported for expositional brevity

The output elasticities of IT capital estimated from the stochastic frontier function lie in a reasonable range, confirming the results from prior IT productivity studies and reinforcing our results. We strengthen the validity of our findings by examining the direction of causality between IT and competition, finding both that increased competition leads to greater IT investment and that we cannot reject the hypothesis that IT investment does not result in changes in competitiveness. Finally, our analysis shows that firms are able to close the efficiency gap with frontier firms more quickly when they have invested in IT intensively. In sum, our study highlights the importance of IT and the moderating role of competition in improving a firm’s efficiency position.

Our efficiency analysis complements earlier IT productivity studies by focusing on a different outcome measure and by allowing for heterogeneous efficiency levels across firms. For instance, our findings may help explain the considerable observed variation in prior studies of firm-level returns to IT investment, indicating that it might, in part, result from the differences in firms’ efficiency levels, which in turn is related to the degree of competition they face. Our findings also suggest that the level of competition in an industry not only has implications for social welfare and consumer surplus but also for economic growth by spurring increases in IT investment and productivity.

The results of our study have important implications for managers. Because productivity improvements stem from both technical progress and efficiency gains, managers should focus not just on adopting new technological innovations but also on deriving improvements in efficiency from their prior IT investments. Firms display considerable variation in technical efficiency because of, in part, differences in firm-specific factors including IT intensity, management quality, and know-how and also because of varying degrees of competition in different industries. Because IT intensity, which is an important determinant of the value derived from efficiency improvements, has been correlated with IT know-how, we infer that investing in IT and acquiring IT-related management know-how can help managers move towards industry-leading levels of efficiency. This may be even more relevant for firms in less competitive industries that are not as driven to achieve higher levels of efficiency.

Recently, subsequent to the end date of our data set, the degree of competition in many industries has increased (Brynjolfsson and Saunders 2009), spurring firms towards greater efficiency. At the same time, the rapid technical progress in IT implies that the efficient production frontier continues to be pushed out. In the face of the growing scope and impact of new IT innovations and the increasing complexity of these ever more sophisticated technological environments that continue to raise efficient output levels, firms should continue to focus on investing in management effort complementary to their IT investments to achieve improvements in efficiency.

Our research is not without limitations. First, the data in our study are from very large (Fortune 1000) firms. Because firms that are successful in leveraging IT are more likely to be represented in the data set, we may be overestimating the contribution of IT. Although our GMM-based estimation strategy enables us to obtain consistent estimates by controlling for unobserved firm-specific characteristics, we are not able to address the efficiency impact of factors other than IT and competition. For instance, our study does not directly control for the role of management quality in improving firm efficiency and its potential interplay with competition. However, we do include efficiency change as a variable in our estimations, which has a related, but not identical, interpretation. Identifying and measuring additional factors that explain the differences in efficiency in the IT context would be a promising avenue for future studies.

Finally, we limit our attention to technical efficiency. A richer understanding of the value created by IT can be achieved by examining both technical and allocative efficiency. However, this requires further data on input and output prices. Despite these limitations, we believe that our research provides valuable insights into the interplay between competition, IT investments, and efficiency.

## Appendix

## Variables and Data Construction

Ordinary capital (K): computed from the total book value of property, plant, and equipment. The value was deflated by the GDP implicit price deflator for fixed investment. The deflator was constructed based on the computed average age of equipment using straight-line depreciation to determine the average age. The constant dollar value of IT capital was subtracted out. Accordingly, the sum of ordinary capital and IT capital equals the total value of capital.

IT capital (IT): based on the current value of installed computer-related equipment. This value is deflated by the deflator for computer systems (Gordon 1990).

Labor expenses (L): taken from Compustat (labor and related expenses) if present. Otherwise, it was computed as a sector average labor cost per employee multiplied by total number of employees. Then it was deflated by the price index for total compensation.

Number of employees: taken from Compustat. This was reported by some firms as an average number of employees and by some as the number of employees at year end. No adjustments were made.

Value added (Y ): computed as the constant dollar value of sales minus the constant dollar value of materials expenses. Sales data were taken from Compustat and deflated by the two-digit industry level deflator. Material was computed by taking differences between total expenses and labor expenses and deflated by the producer price index for intermediate materials, supplies and components.

## References

Aghion P, Bloom N, Blundell R, Griffith R, Howitt P (2005) Competition and innovation: An inverted U relationship. Quart. J. Econom. 120(2):701–728.

Aigner D, Lovell K, Schmidt P (1977) Formulation and estimation of stochastic frontier production function models. J. Econometrics 6(1):21–37.

Amess K (2003) The effect of management buyouts on firm-level technical inefficiency: Evidence from a panel of UK machinery and equipment manufacturers. J. Indust. Econom. 51(5):35–44.

Arellano M, Bond S (1991) Some tests of specification for panel data: Monte Carlo evidence and an application to employment equations. Rev. Econom. Statist. 58(2):277–297.

Arellano M, Bover O (1995) Another look at the instrumentalvariable estimation of error-components models. J. Econometrics 68(1):29–52.

Banker R, Chang H, Natarajan R (2005) Productivity change, technical progress, and relative efficiency change in the public accounting industry. Management Sci. 51(2):291–394.

Banker R, Kauffman R, Morey R (1990) Measuring gains in operational efficiency from information technology: A study of the Positran deployment at Hardee’s Inc. J. Management Inform. Systems 7(2):29–54.

Barua A, Lee B (1997) The information technology productivity paradox revisited: A theoretical and empirical investigation in the manufacturing sector. Internat. J. Flexible Manufacturing Systems 9(2):145–166.

Barros C (2008) Efficiency analysis of hydroelectric generating plants: A case study for Portugal. Energy Econom. 30(1):59–75.

Basker E (2005) Job creation or destruction? Labor market effects of Wal-Mart expansion. Rev. Econom. Statist. 87(1):174–183.

Basu S, Fernald J, Oulton N, Srinivasan S (2004) The case of the missing productivity growth: Or, does information technology explain why productivity accelerated in the United States but not the United Kingdom? Gertler M, Rogoff K, eds. NBER Macroeconomics Annual 2003 (MIT Press, Cambridge, MA).

Battese G, Coelli T (1988) Prediction of firm-level technical efficiencies with a generalized frontier production function and panel data. J. Econometrics 38(3):387–399.

Battese G, Coelli T (1995) A model for technical inefficiency effects in a stochastic frontier production function for panel data. Empirical Econom. 20(2):325–332.

Baum C, Schaffer M, Stillman S (2003) Instrumental variables and GMM: Estimation and testing. Working Paper 545, Department of Economics, Boston College, Newton, MA.

Bharadwaj A (2000) A resource-based perspective on information technology capability and firm performance: An empirical investigation. MIS Quart. 24(1):169–196.

Bharadwaj AS, Sambamurthy V, Zmud RW (1999) IT capabilities: Theoretical perspectives and empirical operationalization. Proc. Internat. Conf. Inform. Systems, Charlotte, NC, 378–385.

Blundell R, Bond S (1998) Initial conditions and moment restrictions in dynamic panel data models. J. Econometrics 87(1):115–143.

Bond S, Elston J, Mairesse J, Mulkay B (2003) Financial factors and investment in Belgium, France, Germany, and the United Kingdom: A comparison using company panel data. Rev. Econom. Statist. 85(1):153–165.

Boone J (2000) Competitive pressure: The effects on investments in product and process innovation. Rand J. Econom. 31(3):549–569.

Borsch-Supan A (1998) Capital’s contribution to productivity and the nature of competition. Brookings Papers Econom. Activity, Microeconom. 1998:205–248.

Brynjolfsson E, Hitt L (1995) Information technology as a factor of production: The role of differences among firms. Econom. Innovation New Tech. 3(4):183–200.

Brynjolfsson E, Hitt L (2000) Beyond computation: Information technology, organizational transformation and business performance. J. Econom. Perspect. 14(4):23–48.

Brynjolfsson E, Hitt L (2003) Computing productivity: Firm-level evidence. Rev. Econom. Statist. 85(4):793–808.

Brynjolfsson E, Saunders A (2009) Wired for Innovation: How Information Technology is Reshaping the Economy (MIT Press, Cambridge, MA).

Casu B, Girardone C (2009) Testing the relationship between competition and efficiency in banking: A panel data analysis. Econom. Lett. 105(1):134–137.

Caves R, Barton D (1990) Efficiency in US Manufacturing Industries (MIT Press, Cambridge, MA).

Chang Y, Gurbaxani V (2012) The impacts of IT-related spillovers on long-run productivity: An empirical analysis. Inform. Systems Res. 23(3, Part 2):868–886.

Cohen W, Levinthal D (1990) Absorptive capacity: A new perspective on learning and innovation. Admin. Sci. Quart. 35(1):128–152.

Computerworld (2010) Forrester downgrades U.S. IT spending forecast. Accessed September 13, 2012. http://www .computerworld.com/s/article/9191401/Forrester\_downgrades \_U.S.\_IT\_spending\_forecast.

Cooper B, Watson H, Wixom B, Goodhue D (2000) Data warehousing supports corporate strategy at First American Corporation. MIS Quart. 24(4):547–567.

Cornwell C, Schmidt P, Sickles R (1990) Production frontiers with cross-sectional and time-series variation in efficiency levels. J. Econometrics 46(1–2):185–200.

Daly A, Hitchens D, Wagner K (1985) Productivity, machinery and skills in a sample of British and German manufacturing plant. National Institute Econom. Rev. 3. 111(1):48–61.

David P (1990) The dynamo and computer: An historical perspective on the modern productivity paradox. AEA Papers Proc. 80(2):355–361.

Dearden L, Reed H, Van Reenen J (2006) The impact of training on productivity and wages: Evidence from British panel data. Oxford Bulletin Econom. Statist. 68(4):397–421.

Dedrick J, Gurbaxani V, Kraemer K (2003) Information technology and economic performance: A critical review of the empirical evidence. ACM Comput. Survey 35(1):1–28.

Dewan S, Min C (1997) The substitution of information technology for other factors of production: A firm level analysis. Management Sci. 43(12):1660–1675.

Fare R, Grosskopf S, Norris M, Zhang Z (1994) Productivity growth, technical progress and efficiency change in industrialized countries. Amer. Econom. Rev. 84(1):66–83.

Farrell (1957) The measurement of productive efficiency. J. Royal Statist. Soc. A 120:253–281.

Folland S, Hofler R (2001) How reliable are hospital efficiency estimates? Exploring the dual to homothetic production. Health Econom. 10(8):683–698.

Gaspar J, Massa M (2006) Idiosyncratic volatility and product market competition. J. Bus. 79(6):3125–3152.

Gilchrist S, Gurbaxani V, Town R (2001) Productivity and PC revolution. Working paper, Center for Research on Information Technology and Organizations, University of California, Irvine.

Good D, Nadiri I, Roller L, Sickles R (1993) Efficiency and productivity growth comparisons of European and US air carriers: A first look at the data. J. Productivity Anal. 4(1–2):115–125.

Gordon R (1990) The Measurement of Durable Goods Prices (University of Chicago Press, Chicago).

Gort M, Sung N (1999) Competition and productivity growth: The case of the U.S. telephone industry. Econom. Inquiry 37(4):678–691.

Green A, Mayes D (1991) Technical inefficiency in manufacturing industries. Econom. J. 101(406):523–538.

Hall R (1988) The relation between price and marginal cost in U.S. industry. J. Political Econom. 96(5):921–947.

Hamilton J (1994) Time Series Analysis (Princeton University Press, Princeton, NJ).

Hart O (1983) The market mechanism as an incentive scheme. Bell J. Econom. 14(2):366–382.

Hay D, Liu G (1997) The efficiency of firms: What difference does competition make? Econom. J. 107(442):597–617.

Hitt L, Brynjolfsson E (1996) Productivity, business profitability and consumer surplus: Different measures of information technology value. MIS Quart. 20(2):121–142.

Jacobson R (1990) Unobservable effects and business performance. Marketing Sci. 9(1):74–85.

Jorgenson D, Stiroh K (2000) Raising the speed limit: U.S. economic growth in the information age. Brookings Papers Econom. Activity 1:125–211.

Kalirajan K, Shand R (1992) Causality between technical and allocative efficiencies: An empirical testing. J. Econom. Stud. 19(2):3–17.

Kaparakis E, Miller S, Noulas A (1994) Short-run cost inefficiency of commercial banks: A flexible stochastic frontier approach. J. Money, Credit Banking 26(4):875–893.

Kirkley J, Squires D, Strand I (1998) Characterizing managerial skill and technical efficiency in a fishery. J. Productivity Anal. 9(2):145–160.

Kneller R, Stevens A (2006) Frontier technology and absorptive capacity: Evidence from OECD manufacturing industries. Oxford Bulletin Econom. Statist. 68(1):1–21.

Koke J, Renneboog L (2005) Do corporate control and product market competition lead to stronger productivity growth? Evidence from market-oriented and blockholder-based governance regimes. J. Law Econom. 48(2):475–516.

Kompas T, Che T, Grafton R (2004) Technical efficiency effects of input controls: Evidence from Australia’s banana prawn fishery. Appl. Econom. 36(15):1631–1642.

Krugman P (1994) The myth of Asia’s miracle. Foreign Affairs 73(6):62–78.

Kumbhakar S (1991) Estimation of technical inefficiency in panel data with firm- and time-specific effects. Econom. Lett. 36(1): 43–48.

Kumbhakar S, Hjalmarsson L (1995) Labour-use efficiency in Swedish social insurance offices. J. Appl. Econometrics 10(1): 33–47.

Kumbhakar S, Lovell C (2000) Stochastic Frontier Analysis (Cambridge University Press, Cambridge, UK).

Kumbhakar S, Ghosh S, McGuckin J (1991) A generalized production frontier approach for estimating determinants of inefficiency in U.S. dairy farms. J. Bus. Econom. Statist. 9(1):279–286.

Lee B, Barua A (1999) An integrated assessment of productivity and efficiency impacts of information technology investments: Old data, new analysis and evidence. J. Productivity Anal. 12(1): 21–43.

Lee B, Menon N (2000) Information technology value through different normative lenses. J. Management Inform. Systems 16(4):99–119.

Leibenstein H (1966) Allocative efficiency v.s. X-efficiency. Amer. Econom. Rev. 56(3):392–415.

Levine R, Loayza N, Beck T (2000) Financial intermediation and growth: Causality and causes. J. Monetary Econom. 46:31–77.

Lindenberg E, Ross S (1981) Tobin’s q ratio and industrial organization. J. Bus. 54(1):1–32.

McKinsey Global Institute (2001) U.S. productivity growth 1995– 2000. McKinsey Global Institute, Washington, DC.

Melville N, Gurbaxani V, Kraemer K (2007) The productivity impact of information technology across competitive regimes: The role of industry concentration and dynamism. Decision Support Systems 43(1):229–242.

Nickell S (1996) Competition and corporate performance. J. Political Econom. 104(4):724–746.

Nishimizu M, Page J (1982) Total factor productivity growth, technical progress and technical efficiency change: Dimensions of productivity change in Yugoslavia, 1965–78. Econom. J. 92(368):920–936.

Oliner S, Sichel D (2000) The resurgence of growth in the late 1990s: Is information technology the story? J. Econom. Perspect. 14(4):3–22.

Oulton N (1998) Competition and the dispersion of labour productivity amongst UK companies. Oxford Econom. Papers 50(1): 23–38.

Oum T, Zhang Y (1995) Competition and allocative efficiency: The case of the U.S. telephone industry. Rev. Econom. Statist. 77(1):82–96.

Pitt M, Lee L (1981) Measurement and sources of technical inefficiency in the Indonesian weaving industry. J. Development Econom. 9(1):43–64.

Primeaux W (1977) An assessment of X-efficiency gained through competition. Rev. Econom. Statist. 59(1):105–108.

Scherer F (1980) Industrial Market Structure and Economic Performance (Houghton Mifflin, Boston).

Schmidt P, Lovell K (1980) Estimating stochastic production and cost frontiers when technical and allocative inefficiency are correlated. J. Econometrics 13(1):83–100.

Shao B, Lin W (2002) Technical efficiency analysis of information technology investments: A two-stage empirical investigation. Inform. Management 39(5):391–401.

Stiroh K (2002) Information technology and U.S. productivity revival: What do the industry data say? Amer. Econom. Rev. 92(5):1559–1576.

Tirole J (1988) The Theory of Industrial Organization (MIT Press, Cambridge, MA).

Wang H (2003) A stochastic frontier analysis of financing constraints on investment: The case of financial liberalization in Taiwan. J. Bus. Econom. Statist. 21(3):406–419.

Wheelock D, Wilson P (2000) Why do banks disappear? The determinants of U.S. bank failures and acquisitions. Rev. Econom. Statist. 82(1):127–138.

Williams J (2004) Determining management behavior in European banking. J. Banking and Finance 28(10):2427–2460.

Willig RD (1987) Corporate governance and product market structure. Razin A, Sadaka E, eds. Economic Policy in Theory and Practice (Macmillan Press, London), 481–494.

Wilson G, Jadlow J (1982) Competition, profit incentives, and technical efficiency in the provision of nuclear medicine services. Bell J. Econom. 13(2):472–482.

Winter S (1971) Satisficing selection, and innovating remnant. Quart. J. Econom. 85(2):237–261.

Young A (1995) The tyranny of numbers: Confronting the statistical realities of the East Asian growth experience. Quart. J. Econom. 110(3):641–680.
