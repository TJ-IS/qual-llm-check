---
otero_id: 26423
otero_key: "AHS84NUF"
title: "Business Planning for Network Services: A Systems Thinking Approach"
authors: "Amitava Dutta"
year: "2001"
journal: "Information Systems Research"
doi: "10.1287/isre.12.3.260.9713"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/AHS84NUF/fulltext/images/27a3a19e0e0eb134f58ea9dc94747154ab219105b75d9509ab447bef2e1a149b.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Business Planning for Network Services: A Systems Thinking Approach

Amitava Dutta,

To cite this article:

Amitava Dutta, (2001) Business Planning for Network Services: A Systems Thinking Approach. Information Systems Research 12(3):260-283. http://dx.doi.org/10.1287/isre.12.3.260.9713

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2001 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/AHS84NUF/fulltext/images/a35adfecc0ea444adc44d52de80c81c946bfb48513480267ab41394b9bf1a93b.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Business Planning for Network Services: A Systems Thinking Approach

Amitava Dutta

School of Management, George Mason University, 4400 University Drive, Fairfax, Virginia 22030-4444 adutta@gmu.edu

A s demand for online network services continues to grow, service providers are looking to meet this need and avail themselves of business opportunities. However, despite strong growth in demand, providers continue to have difficulty achieving profitability, customer churn remains high, and network performance continues to draw complaints. We suggest that strategic business planning for network services would benefit from a systems thinking approach that analyzes the feedback effects present in the underlying business process. These feedback loops can be complex and have significant impact on business performance. For instance, while the size of a provider’s customer base depends on price and network performance, network performance is itself dependent on the size of the customer base. In this paper, we develop a planning model that represents these feedback effects using the finite difference equations methodology of systems dynamics. The model is validated by showing its fit with essential characteristics of the underlying problem domain, and by showing its ability to replicate observed reference mode behaviors. Simulations are then carried out under a variety of scenarios to examine issues important to service providers. Among other findings, the simulations suggest that (a) under flat-rate pricing, lowering price to increase customer base can hurt profitability as well as network performance; (b) under usage-based pricing, lowering price need not necessarily lead to a larger customer base; and (c) in addition to price, the customers threshold of tolerance for performance degradation plays a significant role in balancing market share with profitability. We briefly present a prototype decision support system based on the systems thinking approach, and suggest ways in which it could be used to help business planning for network services.

(Online Services; Systems Dynamics; Business Performance; Decision Support)

## 1. Introduction

Networks are playing an increasing role in business, social, and political activities, fueled in part by growth of the Internet. The worldwide growth of the Internet coupled with development of user-friendly browser technology and standards such as XML (POET 1998) has led to intense interest in its use for electronic commerce (Rao et al. 1998, Keeney 1999). The Internet has also had significant impact on educational, social, and political activities worldwide (Hauben and Hauben

1997, Petrazzini and Kibati 1999). It serves as a forum for discussion of societal issues and as a means of delivering government services. It is not surprising to find that the demand for network services has exploded and is predicted to grow rapidly through the near term (Hoffman et al. 1996).

On the supply side, Internet Service Provision (ISP) has become a significant business activity attracting a variety of vendors and technologies (Lange 1998, Riezenman 1998). The quality of service and price tends to vary across providers, and these factors have a significant effect on customer satisfaction.<sup>1</sup> Of the roughly 4,000 Internet service providers, few are showing any profits, operating margins are getting tighter, and competition is increasing (Fattah 1998). While flatrate pricing—“all you can use for \$19.95”—may attract more customers, many ISPs do not have the financial strength to invest in new capacity to accommodate this growth in customer base. Smaller providers often face a dilemma—grow the customer base but remain unprofitable, or stay small and achieve profitability. Even large providers like Netcom and AOL face similar pressures.

The preceding observations are suggestive of the complex interactions that characterize the underlying business process. A few examples of specific interactions follow. For instance, low prices attract more customers, which generates more network traffic. As traffic levels rise, network performance drops, inviting customers to switch to competitors. To improve network performance, however, the provider must invest in additional capacity, but the lower prices have a negative impact on its ability to pay for capacity. In short, while customer behavior, network performance, and financial consequences may each be easy to characterize in isolation, there is feedback and interaction among them. This complicates the business-planning process considerably, and makes it much more difficult to gauge the impact of management decisions on business performance. An integrated view is therefore needed to gain a better understanding of the business process underlying network service provision. If such a view can be captured in a computer-based model, it can also provide the basis for ongoing decision support (Swami 1995, Tumay 1996, Liles and Presley 1996).

In this paper we develop a basic business model of network service provision using the finite difference equation methodology of systems dynamics. Because the emphasis is on capturing key interactions in the business process, individual structural components are represented in aggregated form. Simplifying assumptions and aggregations will be noted as the model is described in detail. The distinctive features of the model are:

(1) Its structural characteristics capture interactions among customer behavior, financial performance, and network operations inherent in network service provision. It is a systems model that takes an integrative view of the business.

(2) The model can be simulated to examine the dynamics generated by these interactions.

Such an integrated systems model can be expected to contribute in at least two ways. First, it offers a reasonably holistic synthetic environment within which to examine questions of importance to network service providers. For instance, effects of price changes or growth strategies may be studied with the knowledge that business performance behavior generated by the model includes the complex interactions among major functional areas. Once calibrated for a specific organization, such a systems model may also be used to provide decision support for specific businessplanning activities. Section 2 develops the model in top-down fashion. Validation is carried out by first showing the fit between model structure and characteristics of the real operating environment. Subsequently, we show the model’s ability to replicate actual observed reference behavior modes. In §3, this validated model is used as a simulated environment within which to gain insights into issues facing service providers. Section 4 briefly presents a prototype decision support system based on this model, and discusses how it may be used in support of business planning. Limitations and extensions of the model are discussed in conclusion.

## 2. A Basic Business-Planning Model

We have used the well-known finite difference equation methodology of systems dynamics (SD) (Forrester 1961, Goodman 1974) to develop a basic businessplanning model for network service provision. There are, or course, different ways to model the dynamic behavior of systems, each with its own strengths and weaknesses. SD is known to be particularly well suited for high-level process modeling (Wolstenholme 1990) where process scope needs to be wide, but the level of detail is somewhat aggregated. The business-planning process being studied requires precisely such highlevel modeling. Further, the business process being modeled here has quantifiable variables such as price and capacity, as well as hard-to-measure variables such as customer perception of quality. The systems dynamics approach facilitates the representation of both types in one model. There are other advantages to SD associated with the process of model building in a cross-functional context (Wolstenholme 1990) that make it an attractive vehicle for building the model as a decision support tool. For purposes of this paper, it is sufficient to note that SD has the following major characteristics:

(1) SD uses stocks and flows to model organizational processes. Stocks represent accumulations in the system. Both physical and nonphysical variables can accumulate.<sup>2</sup>

(2) Flows connect pairs of stocks and cause changes in stock levels. They obey the laws of flow conservation—i.e., reduction in one stock results in an equivalent increase in the second.

(3) Connectors convey information only, and information flows are not conserved. They can serve to control physical flow rates.

(4) Converters are used to hold inputs, outputs, intermediate values, and to perform computations. They do not accumulate.

(5) Feedback effects can be captured in SD models and they play an important role in determining dynamic behavior.

(6) SD can model closed as well as open systems, the latter having no feedback.

(7) Different forms of delay and nonlinearity can be captured in SD models. Most systems have some form of nonlinearity that bounds system behavior in the long run.

SD models are generally represented graphically using standard symbols for stocks, flows, connectors, and converters. The underlying model is a system of finite difference equations. This mapping between the graphical and mathematical representations will be shown shortly. Models are simulated by iteratively evaluating the system of equations.

## 2.1. A High-Level Model Description

The SD model is presented in a top-down manner. The high-level description to be presented in this section shows major structural components and feedback effects among them. Each structural component will be described in detail, together with an explanation of its fit with essential characteristics of the underlying problem domain. Such justification is necessary as a first step towards showing model validity. The standard SD symbols are reproduced in Figure 1 and the highlevel model appears in Figure 2.

To facilitate identification of components in systems diagrams, we will use superscripts S, F, Cn, Cv, for stock, flow, connector, and converter variables, respectively. To get an integrated view of service provision, we begin with new customers signing up with the provider. New customers increase its customer base. Customers generate traffic on the provider’s network, experience a certain quality of service, and pay fees that generate revenue. Figure 2 captures these three basic components of service provision—customers, the network, and finances—as follows. The provider’s customer base is represented by TotCust<sup>S</sup>. In each period, a certain number of new customers sign up while some existing customers leave, represented by the flows NewCustomers<sup>F</sup> and DepartingCustomers<sup>F</sup>, respectively. The difference between these two flows represents net additional customers added in a period. Over time, if the two flows balance, TotCust<sup>S</sup> levels off to a steady value. When inflow exceeds outflow, TotCust<sup>S</sup> increases and vice versa.

Similarly, network capacity is represented by the stock Network<sup>S</sup>. The flow into this stock, Cap-Expansion<sup>F</sup>, is the result of investments in additional capacity and other network enhancements. In this basic model, capacity is never removed; hence there is no outflow from Network<sup>S</sup>. Financial operations are also represented in a simple manner by a single stock, RetEarnings<sup>S</sup>. There is a periodic inflow of Revenues<sup>F</sup> driven by customer base and price,<sup>3</sup> and a periodic outflow of Expenses<sup>F</sup> associated with operational costs and reinvestments in the network. The difference between the two flows accumulates as the provider’s retained earnings.

![](/api/attachments/AHS84NUF/fulltext/images/745a15f3ca777ba7a971cc0cc18ea6f5714c60ac8f0475a2684a996290365c2e.jpg)  
Information Systems Research Vol. 12, No. 3, September 2001

Figure 2 High-Level SD Representation of Basic Business Model  
![](/api/attachments/AHS84NUF/fulltext/images/dd8ea635151533400fd93b326c58847f51c96ac5498b05846434c7a5a687b666.jpg)

Even without further detail about the three components, it is easy to trace feedback loops in Figure 2, highlighting the complexity of business planning. Following connectors (the thin directed lines) in Figure 2, one can trace a positive feedback loop from TotCust<sup>S</sup>, to Revenues<sup>F</sup>, on through to Network<sup>S</sup> and back again to TotCust<sup>S</sup>. For a given price, an increase in TotCust<sup>S</sup> increases Revenues<sup>F</sup>, which in turn permits an increase in Network<sup>S</sup>. This improves network performance, in turn increasing NewCustomers<sup>F</sup> and causing an increase in TotCust<sup>S</sup>.

There is also a counteracting negative feedback loop from TotCust<sup>S</sup> to Perf<sup>Cv</sup> back to DepartingCustomers<sup>F</sup>.

An increase in TotCust<sup>S</sup> increases traffic on the network, reducing network performance (Perf<sup>Cv</sup>), which in turn increases the number of Departing-Customers<sup>F</sup>—leading to a reduction in TotCust<sup>S</sup>. There is another negative feedback loop between the network and financial components in Figure 2. As the stock RetEarnings<sup>S</sup> increases, the provider may choose to invest more in expansion, thereby increasing Network<sup>S</sup>. However, as the network gets larger, operational costs would increase, which in turn would increase expenses and lower RetEarnings<sup>S</sup>. Apart from these feedback loops, there is interaction between FlatPrice<sup>Cv</sup>, Tot-Cust<sup>S</sup>, and Revenues<sup>F</sup>, where the impact of price changes on revenue will be affected by the elasticity of demand. Because Figure 2 hides further details of each of the three components, there are additional interactions and feedback loops that have not been enumerated in this high-level description. Nevertheless, the interactions and feedback loops identified thus far are sufficient to make the case for an integrated view of network service provision for business-planning purposes.

Figure 3 Structural Components of Customer Sector  
Customer Sector  
![](/api/attachments/AHS84NUF/fulltext/images/8c79ab863afe61244116d4a750038fcec58ea985e1fda84c9e8a7a36321ac7d1.jpg)

We had mentioned earlier that the graphical representation of a SD model is always associated with an underlying mathematical model. The set of finite difference equations corresponding to the systems model is shown in the Appendix. Having shown this equivalence, we will adopt the graphical representation for the rest of the paper.

## 2.2. Sector Details and Face Validity of Model

This section develops further structural details of each major component in the high-level model. In SD parlance, major model components are referred to as “sectors.” With reference to Figure 2, the basic model therefore consists of three interacting sectors. In describing each sector, we explain the fit between model structure and essential characteristics of the underlying problem domain. The major items of correspondence are also summarized in tabular form at the end of each sector. These justifications serve as face validity for the model.

2.2.1. The Customer Sector—Structure and Validity. The structural details appear in Figure 3. NewCustomers<sup>F</sup> starts from a “cloud” and flows into TotCust<sup>S</sup>. The cloud represents an infinite stock, reflecting our assumption that customers arrive from an infinite population of potential customers. This assumption can be readily justified by the rapid growth in demand for network services.<sup>4</sup> Inbound connectors from CurrentQualRep<sup>Cv</sup> and FlatPrice<sup>Cv</sup> to New-Customers<sup>F</sup> specify that arrival of new customers depends only on price and the provider’s current reputation for service quality. While this is somewhat of a simplification, it is supported by survey findings in the literature (Burden 1998, Wang et al. 1996). From a customer perspective, service quality refers to overall perception of a combination of variables including network reliability, availability, security, and customer support.<sup>5</sup> Connectors from FlatPrice<sup>Cv</sup> and Perceived-Qual<sup>F</sup> to DepartingCustomers<sup>F</sup> specify that departures of existing customers also depend on price and perceived service quality. Industry evidence (Wallace and

Wagner 1997) indicates that in a competitive market customers are inclined to jump ship when they experience poor performance. Of course, noncompetitive prices will also cause defection.

There is however, a difference in the way that incoming and outgoing customers perceive service. Departing customers have perceptions based on the service they have actually received from the provider. Arriving customers, however, have not yet actually experienced service, and their perceptions are based more on the provider’s reputation for quality. This distinction is captured in the following way. In Figure 3, QualityRep<sup>Cv</sup> represents an “initial” reputation for quality. The provider’s current reputation is determined by adjusting the initial reputation based on trends in actual service quality, hence the connectors from QualityRep<sup>Cv</sup> and PerceivedQual<sup>F</sup> to Current-QualRep<sup>Cv</sup>. The latter becomes one of the drivers of NewCustomers<sup>F</sup>. This structure can capture the scenario where a provider improves its service reputation by progressively improving its actual service quality. Conversely, reputation can drop if actual service quality worsens over time. Note however that Perceived-Qual<sup>F</sup> rather than CurrentQualRep<sup>Cv</sup> governs Departing-Customers<sup>F</sup>. In other words, departing customers base perceptions on actual experience rather than reputation.

Figure 3 also captures the “delayed response” commonly seen in customer behavior (Lilien et al. 1992). It is represented by the conveyer<sup>6</sup> PercepDelay<sup>Cy</sup>. From a modeling standpoint, delays are interesting because they can lead to unstable behavior and make it harder to drive a system towards desired goals. Observe that ServiceQuality<sup>F</sup> is driven by Perf<sup>Cv</sup>, and the latter appears as a dotted circle. A dotted symbol (dotted flow, stock, or converter) indicates that the variable is a copy of one that exists elsewhere in the model. It is just a visually convenient way of avoiding crisscrossing connectors that would otherwise clutter the diagrams. The original copy of Perf<sup>Cv</sup> can be found in the Network sector to be described shortly.

Some comments on the price variable, FlatPrice<sup>Cv</sup>, are in order. Unlimited-use flat pricing is currently popular among providers (James 1996). Conceptual arguments in favor of flat pricing have also been made in the literature (Anania and Solomon 1998) based on regulatory issues, heterogeneity of infrastructure, and advances in technological capabilities. However, providers are also giving consideration to usage-based pricing. They have not been able to install capacity fast enough to meet increased demand arising from flat fees (James 1997) and vendor profitability has been hurt (Barret 1997). Early adopters of flat pricing, such as Netcom, have been moving away to alternate pricing schemes including usage-based pricing (Firdman 1997, Flynn 1997). Arguments for usage-based pricing, based on congestion and economic value of services, have also appeared in the literature (MacKie-Mason et al. 1998). Nevertheless, because flat pricing is so prevalent, we use it in most of this paper.<sup>7</sup>

Although price and service quality are important variables affecting customer dynamics, they are not the only ones (Bolton 1998). While they are not explicitly represented, it is possible to include some of their effects indirectly by appropriate shaping of the demand curve. For example, assume that Figure 4(a) shows a baseline price-demand curve. If a provider has a reputation for superior content, its potential customers would likely have a higher willingness to pay, and the demand curve would shift or bow out to the right as in Figure 4(b). Conversely, a negative reputation would make the curve shift or bow inwards as shown in Figure 4(c). The outflow of customers, Departing-Customers<sup>F</sup>, can be shaped similarly.

Figure 4 Different Functional Forms of the Price-Demand Curve  
![](/api/attachments/AHS84NUF/fulltext/images/36c2c932b3c1bd97bfba0c40b74f36e572b70f07e1d922802e6b170d963ab97c.jpg)

Table 1 summarizes the preceding discussion of fit between structure of the customer sector and major characteristics of the problem domain.

2.2.2. The Financial Sector—Structure and Validity. Structural details appear in Figure 5. The stock RetEarnings<sup>S</sup> accumulates retained earnings of the provider. Operating income is the difference between Revenues<sup>F</sup> and Expenses<sup>F</sup> and is represented by Opincome<sup>Cv</sup>. Several simplifications are evident in Figure 5. For instance, we do not model details such as dividend policy, debt or equity structure, and asset structure and tax expenses. These details, while important, would add complexity without shedding additional light on the interactions being studied here. Expenses<sup>F</sup> is the sum of operating expenses and investment in additional network capacity. Operating expenses, represented by OpExpense<sup>Cv</sup>, depend on network size. Hence OpExpense<sup>Cv</sup> is connected to the dotted stock Network<sup>S</sup>. This connection can be traced as being part of the feedback loop between the Network and Financial sectors.

The relationship between Network<sup>S</sup> and OpExpense<sup>Cv</sup> is assumed to be continuous and concave, thereby exhibiting scale economies. There is ample evidence for this assumption (Proceedings IEEE Network Operations 1998). Operational expenses cover activities such as fault diagnosis, repair, reconfiguration, performance monitoring, etc. With modern automated tools, it is easier to scale up these activities as networks grow (Stamper 1999), resulting in concave costs. The second component of expenses consists of amounts reinvested in network enhancements, represented by Reinv\$<sup>Cv</sup>. This expenditure is assumed to be a function of Revenues<sup>F</sup> and a management decision regarding the percentage of revenue to be reinvested—ReinvRate<sup>Cv</sup>. The foregoing discussions of the fit between sector structure and problem domain characteristics are summarized in Table 2.

Figure 5 Structural Components of Financial Sector  
![](/api/attachments/AHS84NUF/fulltext/images/f04c6e41fa0d08f5bbb35627360cb120e1007478dd1bf69e1ff50f1b13b12ebf.jpg)

Table 1 Customer Sector—Fit with Problem Domain Characteristics

<table><tr><td>Structural element of model</td><td>Type of structural element</td><td>How element is specified in model</td><td>Characteristics of problem domain offering face validity for element specification</td></tr><tr><td>FlatPrice</td><td>Converter</td><td>Numeric constant</td><td>Most network service providers offer unlimited-use flat pricing (e.g., James 1996)</td></tr><tr><td>NewCustomers</td><td>Flow</td><td>Decreasing in FlatPrice, increasing in CurrentQualRep. Relation may be linear or nonlinear</td><td>Price and quality are the two major factors attracting new customers according to surveys (e.g., Burden 1998)</td></tr><tr><td>Departing Customers</td><td>Flow</td><td>Increasing in FlatPrice; decreasing in PerceivedQual. Relation can be linear or nonlinear</td><td>Higher price causes more customers to leave. Better quality reduces customer turnover (e.g., Bolton 1998)</td></tr><tr><td>TotCust</td><td>Stock</td><td>Accumulation of difference between New and Departing Customer flows</td><td>Valid by algebraic definition. New customers increase customer base, while departing customers reduce it</td></tr><tr><td>CurrentQualrep</td><td>Converter</td><td>Moving average of PerceivedQual</td><td>Customer&#x27;s perceptions of quality have memory effects (e.g., Lilien et al. 1992)</td></tr><tr><td>PercepDelay</td><td>Conveyer</td><td>Time delay of specified number of periods</td><td>Quality improvements may not be recognized immediately by customers (e.g., Tedesco 1997)</td></tr><tr><td>Perf</td><td>Converter</td><td>Copy of element</td><td>See Table 3 for Network Sector</td></tr></table>

Table 2 Financial Sector—Fit with Problem Domain Characteristics

<table><tr><td>Structural element of model</td><td>Type of structural element</td><td>How element is specified in model</td><td>Characteristics of problem domain offering face validity for element specification</td></tr><tr><td>Revenues</td><td>Flow</td><td>Number of customers * FlatPrice</td><td>Valid by algebraic definition of revenue under flat pricing</td></tr><tr><td>Expenses</td><td>Flow</td><td>Sum of operating expense and amount invested in network capacity expansion</td><td>Valid by algebraic definition under simplified view of financial sector</td></tr><tr><td>RetEarnings</td><td>Stock</td><td>Accumulation of revenues minus expenses</td><td>Valid by algebraic definition under simplified view of retained earnings (no dividends, etc.)</td></tr><tr><td>OpIncome</td><td>Converter</td><td>Revenues minus expenses</td><td>Valid by algebraic definition under simplified view of financial sector</td></tr><tr><td>OpExpense</td><td>Converter</td><td>Concave function of network capacity</td><td>As network becomes larger, operational costs increase, but there are economies of scale (e.g., IEEE Network Operations 1998)</td></tr><tr><td>Reinv$</td><td>Converter</td><td>Revenues * ReinvRate</td><td>Valid by algebraic definition. Investment in network expansion/ enhancements is critical to maintain service quality (e.g., Vijayan 1999)</td></tr><tr><td>ReinvRate</td><td>Converter</td><td>Numeric constant between 0 and 1</td><td>Model input parameter to compute Reinv$</td></tr><tr><td>TotCust</td><td>Stock</td><td>Copy of element</td><td>See Table 1 for Customer Sector</td></tr><tr><td>Network</td><td>Stock</td><td>Copy of element</td><td>See Table 2 for Network Sector</td></tr></table>

The two variables—OpIncome<sup>Cv</sup> and RetEarnings<sup>S</sup>— have significant impact on other financial variables associated with a firm. For example, when AOL faced its network performance problems in 1996, it spent large sums over a very short period to boost network capacity. Operating income dropped, and they suffered a significant loss in market valuation. Thus, the two financial variables represented here can serve as adequate indicators of financial health.

2.2.3. The Network Sector—Structure and Validity. Structural details of the Network sector appear in Figure 6. Network<sup>S</sup> represents the provider’s collection of network assets such as transmission lines, switches, various kinds of network software, etc. In view of the integration of multiple sectors within the model, we have chosen not to represent network characteristics at a finer level of detail. Note that there is no outflow from Network<sup>S</sup>, implying that the network can only grow in capacity. This is reasonable given the explosive growth in demand for network services. Figure 6 also captures the fact that it may take time to install additional capacity. This delay is represented by ImpDelay<sup>Cy</sup>, and can be varied within the model. As a practical matter, ImpDelay<sup>Cy</sup> is low when capacity is leased, but when facilities have to be physically installed, much longer delays are involved.

The investment in additional capacity is represented by Reinv\$<sup>Cv</sup> and is connected to CostofCap<sup>Cv</sup>, the latter representing the relationship between cost and network capacity. This relationship is concave and known to exhibit economies of scale (Kleinrock 1976, Tanenbaum 1996) and is identified explicitly in Figure 6. The dotted stock TotCust<sup>S</sup> is a copy from the Customer sector. Network utilization, NetUtil<sup>Cv</sup>, is computed as total offered traffic divided by network capacity, the numerator being obtained by multiplying TotCust<sup>S</sup> by the average traffic generated by a customer, AvgTraffic<sup>Cv</sup>. Utilization, in turn, determines performance, indicated by the connector from NetUtil<sup>Cv</sup> to Perf<sup>Cv</sup>.

Figure 6 Structural Details of Network Sector  
![](/api/attachments/AHS84NUF/fulltext/images/28d5b98a9032e452a820ab7c7e70c9be9cdb9a061095fe978bac523ba59ffc30.jpg)

It was mentioned earlier that perceived quality of service is determined by the combined effect of several different variables. The relationship between network utilization and some of these variables is well known. For example, a variety of queuing models have shown the nonlinear relationship between utilization and average delay (Kleinrock 1976, Tanenbaum 1996) for data networks; beyond a certain threshold value of utilization, average delay deteriorates quite rapidly. Other performance characteristics such as error rates, delay variability, and probability of disconnection all degrade rapidly as the network gets heavily utilized. Also, as network utilization increases, there is less flexibility in adjusting network parameters to keep performance levels steady. In short, there is considerable evidence for the nonlinear Utilization-Performance relationship shown in Figure 6. The preceding discussion of the fit between structure of the network sector and characteristics of the underlying problem domain is summarized in Table 3.

## 2.3. Model Validity—Replication of Reference Behavior Modes

In the foregoing sections, we have provided details of the structure of each of the three model sectors. The structure of each sector has been justified by showing the fit with characteristics of the underlying problem domain. To further strengthen validity of the model, it is important to go beyond face validity, and test whether the model can endogenously reproduce behavior modes characterizing real environments. One can then have increased confidence that insights provided by the model have some basis in how these relationships will play out in the reference environment. This testing is referred to as replication of reference mode behaviors. To this end, we identified a set of reference behaviors from the practitioner literature and tested the model’s ability to reproduce them. We describe one such test in detail, while the others are provided in summary form.

The reference behavior whose replication we present in detail is drawn from a very visible event in the industry. In December 1996, AOL, the leading provider of network services, changed its pricing from usagebased rates to flat-rate unlimited usage. What followed were major financial troubles and a public relations disaster as its customer base shrank because of defections (Barret 1997, Dellcave 1997). It took some time and a substantial investment in network capacity for AOL to recover (Tedesco 1997). Figure 7 shows our systems dynamics model replicating this reference behavior.

Table 3 Network Sector—Fit With Problem Domain Characteristics

<table><tr><td>Structural element of model</td><td>Type of structural element</td><td>How element is specified in model</td><td>Characteristics of problem domain offering face validity for element specification</td></tr><tr><td>Reinv$</td><td>Converter</td><td>Copy of Element</td><td>See Table 2 for Financial Sector</td></tr><tr><td>CostofCap</td><td>Converter</td><td>Concave function of network capacity</td><td>Economies of scale exist in the cost of leased or installed capacity (e.g., Tanenbaum 1996)</td></tr><tr><td>ImpDelay</td><td>Conveyer</td><td>Time delay of specified number of periods</td><td>Installation of physical network infrastructure is not instantaneous (e.g., Robertazzi 1999)</td></tr><tr><td>CapExpansion</td><td>Flow</td><td>Same as AuthorizedCap, but delayed by ImpDelay time units</td><td>Valid by definition of delay. If 10 units of capacity are authorized, those 10 units get installed only after ImpDelay time units</td></tr><tr><td>Network</td><td>Stock</td><td>Initial capacity + accumulated CapExpansion</td><td>Valid by algebraic definition under simplified scenario of no capacity removal</td></tr><tr><td>NetUtil</td><td>Converter</td><td>(TotCust*AvgTraffic)/ Network capacity</td><td>Standard definition of network utilization in literature (e.g., Kleinrock 1976)</td></tr><tr><td>Perf</td><td>Converter</td><td>Nonlinear decreasing function of NetUtil</td><td>Standard result from queuing analysis of networks (e.g., Kleinrock 1976) and operational observations (e.g., Fonseca 1999)</td></tr><tr><td>TotCust</td><td>Stock</td><td>Copy of element</td><td>See Table 1 for Customer Sector</td></tr></table>

In Figure 7, the service provider changes over from usage-based pricing to flat-rate pricing at about T  30. Note that prior to T  30, the provider’s business performance as indicated by the plots of network performance Perf<sup>Cv</sup>, customer base TotCust<sup>S</sup>, operating income OpIncome<sup>Cv</sup>, and retained earnings RetEarnings<sup>S</sup> is quite healthy. The change to flat-rate pricing at about T  30 results in the following effects on business performance in the model. The customer base, TotCust<sup>S</sup>, begins a precipitous slide and remains at a much lower steady-state value. OpIncome<sup>Cv</sup> drops sharply and RetEarnings<sup>S</sup> begins to gradually drop. Network performance, Perf<sup>Cv</sup>, drops too and is unstable as well. These are exactly the same effects experienced by AOL (Dellcave 1997). Of course, no provider would let this situation continue without a response, and neither did AOL. It made major investments in network capacity and gradually regained business performance.

Figure 8 shows the model replicating this recovery behavior. The switch to flat pricing occurs at about

T  50, and major investments in network capacity are made from about T  100 onwards. We have deliberately let some time elapse before responding with additional capacity, simply to demonstrate the model’s behavior more clearly. Notice that TotCust<sup>S</sup> increases after T  100, but the growth in customer base is much more gradual compared to the sharp decline in response to the flat-pricing change at T50. Ret-Earnings<sup>S</sup> finally starts to increase again, but it remains flat for a while after $T \ = \ 1 0 0 .$ . The slow recovery is attributable to the memory effects of customers captured in the model and described earlier in the model. Once again, our model is able to replicate the recovery behavior experienced by AOL.

We tested the model’s ability to replicate other reference behaviors as well. The detailed plots for each one of those tests are not reproduced here for brevity. Instead, we summarize those results in the list below. For each test, we briefly state the reference behavior, provide a reference from the practitioner literature for that behavior, state how the model was tested, and summarize the corresponding model output that confirms its ability to replicate the behavior.

## Customer Sensitivity to Network Performance

(1) Reference Behavior: For many customers, network performance is just as important as low price. In these circumstances, a low price will not stem customer flight if network performance falls (Burden 1998).

Figure 7 Reference Mode Behavior Replication—Switch to Flat Price  
![](/api/attachments/AHS84NUF/fulltext/images/31ccfaabdee66378082ecf98141cc0e1ea75df2bf458aa56e5fe05d2dd3deecc.jpg)

Figure 8 Replication of Reference Mode Behavior—Recovery Through Investment  
![](/api/attachments/AHS84NUF/fulltext/images/b7ff98bed969532583e29c8d9fd78e3faff99d78b0f8c904218a253e8d54dbfa.jpg)  
Graph 2: p2 (Company Vitals) Months

(2) Test Procedure: Carried out four simulation runs with the following model parameter combinations— (average price, average performance sensitivity), (low price, average performance sensitivity), (average price, high performance sensitivity), (low price, high performance sensitivity).

(3) Model Output: A drop in price resulted in a larger increase in customer base (TotCust<sup>S</sup>) under average sensitivity compared to high sensitivity.

## Impact of Inadequate Capacity Planning

(1) Reference Behavior: As more customers engage in online activities and as the complexity of those activities increases, traffic levels have increased sharply. Proactive network capacity planning has become increasingly important. Without it, performance suffers and providers lose customers (Fonseca 1999, Vijayan 1999).

(2) Test Procedure: Carried out two simulation runs. In the first, average traffic offered by a customer was given a step increase at one point in time, without a corresponding capacity increase. In the second run, a step increase in capacity preceded the step increase in average offered traffic.

(3) Model Output: In the first run, number of customers, TotCust<sup>S</sup>, decreased to a new lower steady-state value after the step increase in average traffic. In the second, TotCust<sup>S</sup> experienced practically no drop in value.

## Continuing Profitability Problems

(1) Reference Behavior: Many providers have increased their customer base through aggressive pricing, but have seen profitability drop (Fattah 1998).

(2) Test Procedure: Multiple runs of the model keeping all input parameters fixed except price. Price was progressively reduced from one run to the next.

(3) Model Output: Over a large range of variation, lowering of price resulted in a higher steady-state value of TotCust<sup>S</sup>, but a lower steady-state value for both OpIncome<sup>Cv</sup> and RetEarnings<sup>S</sup>.

## Importance of Building Customer Relationships

(1) Reference Behavior: Service providers are attempting to contain customer churn through improved customer service, friendlier user interfaces, etc. These efforts are aimed at building stronger relationships with the customer and are helping to reduce churn (Green 1998).

(2) Test Procedure: Three separate runs of model with the function for DepartingCustomers<sup>F</sup> shaped to reflect different strengths of customer relationships (see discussion in §2.1.1. on alternate function shapes). All other input parameters remain unchanged. Churn is measured by the ratio DepartingCustomers<sup>F</sup>/ TotCust<sup>S</sup>.

(3) Model Output: The steady-state value of churn decreased significantly as the customer relationship was made stronger.

The preceding tests indicate that our systems model is capable of replicating some of the major reference behavior modes observed in the real environments of network service provision. Taken in conjunction with earlier descriptions of the fit between model structure and the underlying problem domain, we consider the model to be a reasonably validated representation of the underlying business process.

## 3. Applications of Systems Thinking Model

In the remainder of the paper, we will demonstrate two potentially useful applications of the systems thinking model. First, we use the model as a microworld to examine issues of some importance to service providers, similar to approaches taken elsewhere for other problem domains (Sengupta and Abdel-Hamid 1993). This exercise also offers us qualitative insights into the behavior of the business process underlying network service provision. Subsequently, in §4, we suggest ways in which the model could serve as a decision support tool for ongoing decision making by a service provider.

## 3.1. Qualitative Insights into Underlying Business Process

There are many business issues of concern to service providers. Some of them are related to steady-state types of behavior of the underlying business process. The impact of price on the number of customers and profitability is one such example. Other issues are related to transient behavior of the underlying process. For example, a competitor may suddenly slash prices and the provider may feel forced to follow suit. How quickly will business performance stabilize after such disruptions? Will it stabilize at all? If so, at what values will it stabilize? In short, it is useful to examine both the steady-state and transient behavior to get insights into the issues facing providers. We identify several such issues and generate corresponding scenarios for model simulation. The behaviors generated by the model are explained in terms of the causal forces represented by its structural components. Making the link between behavior and process structure will provide a better understanding of the issues facing service providers. It is first necessary to identify the variables used to generate scenarios representative of those issues, and associated business performance measures.

## 3.2. Scenario Generation Variables

To examine business issues, scenarios are generated by varying the following variables—AvgTraffic<sup>Cv</sup>, PercepDelay<sup>Cy</sup>, QualityRep<sup>Cv</sup>, FlatPrice<sup>Cv</sup>, ImpDelay<sup>Cy</sup>, and ReinvRate<sup>Cv</sup>. It is useful to note that the extent to which a service provider can affect them, and hence the underlying process, is different for each. For instance, FlatPrice<sup>Cv</sup> and ReinvRate<sup>Cv</sup> are management decisions and can be changed quickly and significantly if desired. Even ImpDelay<sup>Cy</sup> can be changed, albeit more slowly, by improving internal management procedures. Similarly, the provider’s initial reputation for quality, QualityRep<sup>Cv</sup>, is under its control, but only gradually since customer processes such as word of mouth also have an effect. In contrast, AvgTraffic<sup>Cv</sup> is an exogenous variable, which can be estimated, but not directly altered, by a provider. Similarly, Percep-Delay<sup>Cy</sup> can be altered, but only gradually through improved communication with customers.

## 3.3. Business Performance Variables

We have identified four key measures of business performance—the provider’s customer base, operating income, retained earnings, and network performance— represented by TotCust<sup>S</sup>, Opincome<sup>Cv</sup>, RetEarnings<sup>S</sup>, and Perf<sup>Cv</sup>, respectively. Earlier in the paper, we had alluded to the difficulty experienced by service providers in achieving a balance among their business goals of large market share, profitability, and quality service. The business performance variables just mentioned are closely related to these objectives and are central to issues facing providers.

This is an appropriate point to make some important observations regarding the interpretation of numbers that will appear in the simulations to follow. First, in examining system behavior, we will rarely be concerned with absolute numerical values. The behavior pattern is what is significant. For example, we are interested in knowing if TotCust<sup>S</sup> increases or decreases with time, whether it remains stable, how rapidly it achieves stability, etc., rather than its absolute values. Also, when comparing steady-state outcomes from different scenarios, it is the relative magnitude of performance variables that will be of interest. Second, selected scenario variables, which do not have an obvious range associated with them, are standardized. Specifically, AvgTraffic<sup>Cv</sup>, FlatPrice<sup>Cv</sup>, and Quality-Rep<sup>Cv</sup> are standardized to range between zero and one. ReinvRate<sup>Cv</sup> has an obvious range from zero to one. The two delays—ImpDelay<sup>Cy</sup> and PercepDelay<sup>Cy</sup>— have to be expressed in units of simulation time periods and can take on nonnegative values greater than one.

The presentation of each simulation run has three parts—(a) a graph showing dynamic behavior of the four business performance variables, (b) values of scenario variables shown to the right of the graph under the heading “Input Parameters,” and (c) end-of-run values of the four business performance measures shown to the right of the graph and below the scenario variables. It will be obvious from the dynamics that these end-of-run values will also be the steady-state values for some performance measures.

## 3.4. Price Effects on Business Performance

If we had to identify one issue that dominates a provider’s activities, it is an understanding of the impact of prices on business performance. We therefore examine this issue in some detail. Specifically, we examine transient as well as steady-state business performance as a function of price, and try to identify the underlying causes for this behavior. Figures 9 and 10 show the impact of high and low values of FlatPrice<sup>Cv</sup> on dynamic behavior, respectively. The only difference in the scenario variables between Figures 9 and 10 is the value of price. The values of these other scenario variables indicate that, in both figures, there are zero implementation and customer perception delays, the initial quality reputation is high, and there is no investment in capacity expansion—i.e., network capacity remains constant. Observe that the three performance measures, OpIncome<sup>Cv</sup>, NetPerf<sup>Cv</sup>, and TotCust<sup>S</sup>, all reach steady-state values in both cases. This is caused by the negative feedback loop between departing customers and the network sector that had been identified earlier in the paper, which acts as a corrective force whenever the system strays from steady-state values.

However, it is also instructive to compare transient behavior in these two figures to understand underlying structural causes. In both figures, network performance, $\mathrm { P e r f } ^ { C v } ,$ exhibits oscillatory behavior prior to reaching steady state. Since ReinvRate<sup>Cv</sup>0, there is no new investment in the network, and its capacity remains fixed. The low price setting in Figure 10 encourages a large inflow of new customers, which increases network traffic significantly. Network utilization increases sharply, degrades performance, and results in a large outflow of dissatisfied customers. This departure acts as a corrective force because the increased departures lighten traffic load on the network, thereby improving performance. The oscillation continues until a customer base is reached consistent with network capacity and customers’ willingness to pay for performance. The system reaches dynamic equilibrium at that point, and steady state obtains. Note that the duration of oscillation of $\mathrm { P e r f } ^ { C v }$ is much shorter under high prices because the inflow of new customers is smaller and the resulting drop in network performance is less extreme—hence the system can adjust more quickly.

The dynamics of OpIncome<sup>Cv</sup> and TotCust<sup>S</sup> are directly related to that of Perf<sup>Cv</sup>, and their causes can be traced back to the same feedback loop just mentioned. Notice that in Figure 9 and 10 both OpIncome<sup>Cv</sup> and TotCust<sup>S</sup> show small oscillations on their way to steady state. The same customer departure process that caused Perf<sup>Cv</sup> to oscillate is behind the oscillations in TotCust<sup>S</sup> as it proceeds to steady state. We know from basic control theory that the magnitude of the corrective force in a negative feedback loop is a function of the magnitude of the perturbation. As a result, oscillations finally dissipate and business performance reaches steady state. Since OpIncome<sup>Cv</sup> is based on revenues generated by TotCust<sup>Cv</sup>, it exhibits the same dynamic behavior pattern as TotCust<sup>Cv</sup>. (Expenses<sup>F</sup> remain fixed since there is no network expansion). The dynamics of RetEarnings<sup>S</sup> is easy to follow because it is simply the integral of the OpIncome<sup>Cv</sup> curve. In our model, since there are no dividend payoffs or other financial outflows, retained earnings are simply accumulated operating income.

Figure 9 Dynamics of Business Performance—High Price Setting  
![](/api/attachments/AHS84NUF/fulltext/images/161cd297dd70f8e20145ae97017e390d2bc88d376a5708cdb7587538a356bb03.jpg)

<table><tr><td colspan="3">Input Par...▼</td></tr><tr><td></td><td>AvgTraffic</td><td>0.5</td></tr><tr><td></td><td>FlatPrice</td><td>0.9</td></tr><tr><td></td><td>ImpDelay</td><td>0</td></tr><tr><td></td><td>PercepDelay</td><td>0</td></tr><tr><td></td><td>Quality Rep</td><td>1</td></tr><tr><td></td><td>ReinvRate</td><td>0</td></tr></table>

<table><tr><td>Perf</td><td>0.83</td></tr><tr><td>OpIncome</td><td>0.77</td></tr><tr><td>TotCust</td><td>0.89</td></tr><tr><td>RetEarnings</td><td>22.8</td></tr></table>

Figure 10 Dynamics of Business Performance—Low Price Setting  
![](/api/attachments/AHS84NUF/fulltext/images/463d7e8a834dd8a9acd94b756c04e24ff07daa3e1c180154b34f883db3df3fd1.jpg)

<table><tr><td colspan="3">Input Par...▼</td></tr><tr><td></td><td>AvgTraffic</td><td>0.5</td></tr><tr><td></td><td>FlatPrice</td><td>0.1</td></tr><tr><td></td><td>ImpDelay</td><td>0</td></tr><tr><td></td><td>PercepDelay</td><td>0</td></tr><tr><td></td><td>Quality Rep</td><td>1</td></tr><tr><td></td><td>ReinvRate</td><td>0</td></tr></table>

A comparison of the end-of-run values at the right bottom corner of Figures 9 and 10 shows that the steady-state value of TotCust<sup>S</sup> is higher when price is low compared to when it is high. While standard “price-quantity” demand functions would imply this behavior, it is not obvious that it should remain so in the presence of the feedback loop between customer behavior and network performance. The smaller customer base under high prices is enjoying better network performance compared to the larger customer base under low prices, as indicated by the respective end-of-run values for Perf<sup>Cv</sup> in the two figures. The lower price setting has resulted in an increased customer base, but profitability has been adversely affected as seen by comparing the end-of-run values for OpIncome<sup>Cv</sup> and RetEarnings<sup>S</sup> in Figures 9 and 10. In summary, price changes affect the dynamic and steady-state performance of all three sectors through the feedback loops identified above. It is therefore important to recognize these feedback effects in business planning.

<table><tr><td>Perf</td><td>0.72</td></tr><tr><td>OpIncome</td><td>0.10</td></tr><tr><td>TotCust</td><td>1.27</td></tr><tr><td>RetEarnings</td><td>3.0</td></tr></table>

3.4.1. Impact of Usage-Based Pricing on Business Performance. Earlier in the paper we noted that service providers commonly use flat pricing. We also observed that usage-based pricing was under consideration. In general, we observed that transient behavior of the model under flat and usage-based pricing is quite similar. However, steady-state behavior under usage-based pricing was sometimes counterintuitive. We give one such example.

Figures 11a and 11b show simulation runs with Price  0.4 and 0.6, respectively. A comparison of steadystate values of TotCust<sup>S</sup> in the two figures indicates that a higher price has resulted in a larger number of customers. This is not quite intuitive—as price increased, so did demand—but can occur under usagebased pricing for the following reasons.

Figures 11a & b  
![](/api/attachments/AHS84NUF/fulltext/images/484ea8e3e2b704826058d84591b545e6051682948d61253fb9438fca333243a7.jpg)

![](/api/attachments/AHS84NUF/fulltext/images/b797b62b702c8de348afc9d1255a153fdf3283d309796d6113763541786ccb53.jpg)

Referring back to the model in Figure 2, when usagebased price is increased, the inflow of new customers, NewCustomers<sup>F</sup>, drops off. However, now that customers are paying based on usage, a price increase also decreases the average traffic load offered by each customer. Thus, the price increase has a quadratic effect on the reduction in total load offered to the network (which is simply the number of customers times average traffic per customer). This causes a sharp improvement in network performance and results in a sharper reduction in DepartingCustomers<sup>F</sup> compared to the reduction in NewCustomers<sup>F</sup>. The net effect is an increase in TotCust<sup>S</sup>. Once again, the importance of understanding feedback effects among the different sectors becomes clear.

## 3.5. Effects of Average Customer Traffic Levels on Business Performance

It is well known that network performance is a major issue facing service providers. The major exogenous determinant of network performance is the average traffic offered to the network by a customer. As Internet applications have become more sophisticated and as customers become more comfortable with online activity, the average traffic offered by a customer has continued to increase. It is therefore useful to examine the impact of average traffic levels on business performance.

A single number, AvgTraffic<sup>Cv</sup>, represents the traffic offered on the network by each customer. This is common practice in the literature on network planning (Robertazzi 1999). A variety of methods for estimating AvgTrafic<sup>Cv</sup> may be found in the literature on traffic engineering (Boucher 1993). To minimize the number of graphs that are presented, Figure 9 is reused for comparison. All scenario variables in Figure 12 have values identical to those in Figure 9, except Avg-Traffic<sup>Cv</sup>, which has a value of 0.1.

As before, all performance variables (except retained earnings, of course) reach steady state. However, unlike Figure 9, Perf<sup>Cv</sup> does not oscillate significantly on its way to steady state in Figure 10. Neither does TotCust<sup>S</sup> or OpIncome<sup>Cv</sup>; the system settles into steady state in a relatively monotonic manner. With a lower value of AvgTraffic<sup>Cv</sup>, the network is subject to far more modest swings in traffic during the transient phase. As a result, the feedback loop between customers and network performance does not oscillate as much while proceeding to steady state. Notice, however, that the system takes much longer to settle into steady state when AvgTraffic<sup>Cv</sup> is low (Figure 12) than when it is high (Figure 9). An analogy with electrical circuits is helpful here. The transient behavior for OpIncome<sup>Cv</sup>, TotCust<sup>S</sup>, and Perf<sup>Cv</sup> in Figure 12 is very similar to that of current in an electrical circuit formed by a resistor and capacitor in series, when a step change in voltage occurs. The “time constant” for the rise or fall in current is given by (resistance\* capacitance). The larger the time constant, the slower the rise or fall. In our domain, a low value of Avg-Traffic<sup>Cv</sup> means that departing customers take away with them only a small amount of offered traffic—i.e., the current of departing traffic is low. This is equivalent to a high resistance, meaning the time constant is high. This is what leads to a slow progress towards steady state in Figure 12 as compared to Figure 9.

Figure 12 Dynamics of Business Performance—Low Average Traffic Demand  
![](/api/attachments/AHS84NUF/fulltext/images/f0b9c997ecc2a6d66bd751e3f82ff508bf208eb2d8d7e0383988396f1b0ca08d.jpg)

<table><tr><td colspan="2">Input Par...▼</td></tr><tr><td></td><td>AvgTraffic 0.1</td></tr><tr><td></td><td>FlatPrice 0.9</td></tr><tr><td></td><td>ImpDelay 0</td></tr><tr><td></td><td>PercepDelay 0</td></tr><tr><td></td><td>Quality Rep 1</td></tr><tr><td></td><td>ReinvRate 0</td></tr></table>

<table><tr><td>Perf</td><td>0.83</td></tr><tr><td>OpIncome</td><td>3.95</td></tr><tr><td>TotCust</td><td>4.42</td></tr><tr><td>RetEarnings</td><td>363.1</td></tr></table>

Figure 13 Steady-State Business Performance as Function of Price Steady State Performance Measures  
![](/api/attachments/AHS84NUF/fulltext/images/f510251f704fe2f2b295e09802cd11bea8a5ee7a6eb33e448cb9e1f18a5c7730.jpg)

## 3.6. Price and Traffic Effects on Steady-State Performance

When examining issues facing service providers in the preceding subsections, we focused mainly on associated transient behavior of business performance variables and the underlying structural causes. In this subsection we take a more detailed look at steady-state behaviors associated with those issues. As before, we try to explain these steady-state behaviors in terms of model structure, thereby offering more insight into underlying causes. Because it is one of the performance measures of interest, the value of RetEarnings<sup>S</sup> is also examined, even though it is not expected to reach any kind of steady-state value. In order to have a meaningful comparison of RetEarnings<sup>S</sup> as the scenario variables are changed, we ensured that all simulation runs were of exactly the same duration. As before, $\mathrm { R e i n v R a t e } ^ { C v }$ , PercepDelay<sup>Cy</sup>, and ImpDelay<sup>Cy</sup> are set to zero. The plots presented thus far in §3 have time as their x-axis to show dynamic behavior. It may be helpful to point out explicitly that in the three graphs to follow, each data point represents a complete simulation and the x-axes represent different scenario variables, not time.

Figure 13 shows how the steady-state values of performance variables change in response to FlatPrice<sup>Cv</sup>, other scenario variables remaining constant. As price increases, the steady-state value of TotCust<sup>S</sup> drops while that of $\mathrm { P e r f } ^ { C v }$ increases. This behavior is consistent with the fact that network capacity is remaining constant (ReinvRat ${ \mathfrak { a } } ^ { C v } = 0 )$ . It is also interesting to see that this intuitive relationship between price and quantity (the steady-state customer base) holds despite the feedback loop between customer behavior and network performance. We have found this relationship between FlatPrice<sup>Cv</sup> and TotCust<sup>S</sup> to hold even when customers are sensitive to degradation in network performance. The cause of this behavior may be found in the structure shown earlier in Figure 3. Existing customers base perceptions on actual performance— PerceivedQual<sup>F</sup>, while new ones arrive based on reputation—CurrentQualRep<sup>Cv</sup>. Because trends in PerceivedQual<sup>F</sup> drive CurrentQualRep<sup>Cv</sup>, the latter changes more slowly. As a result, a price drop attracts more customers than are driven away by performance degradation, resulting in a net increase in the steadystate value of TotCust<sup>S</sup>.

OpIncome<sup>Cv</sup> and RetEarnings<sup>S</sup>, however, do not change monotonically in response to price changes. Both exhibit a maximum, implying that from a financial perspective, there is a “best price.” The shape of these two plots can be explained in part by the revenue pattern generated by a linear demand curve with respect to price<sup>8</sup> (see Figure 3 for this curve). Note, however, that the peaks for OpIncome<sup>Cv</sup> and Ret-Earnings<sup>S</sup> in Figure 13 are not located at the mid-price point, as would be expected with a linear demand curve. They are shifted to the right towards the highprice end. This shift is caused by the nonlinear relationship between demand and network performance (see Figure 3 for this curve) described earlier in the paper. Customers are tolerant of performance degradation up to a threshold, after which there is a rapid drop in demand. Recognition of the effect of this threshold on profitability is important for business planning. If this feedback loop between customer dynamics and network performance is ignored, providers may not recognize the full impact of customers’ threshold of tolerance for performance degradation, thereby dropping price too far in their quest for market share, and hurting profitability in the process.

Figure 14 shows how the steady-state values of the business performance measures vary with average traffic offered by a customer. Under flat pricing, this parameter is not under the provider’s control, but an understanding of its effects is important. Note from Figure 14 that a change in average traffic has absolutely no effect on steady-state network performance. Since the network has a fixed capacity (Reinv-Rate<sup>Cv</sup>0), a higher average traffic simply means there will fewer customers in steady state, as seen in the downward sloping TotCust<sup>S</sup> curve. It follows that steady-state operating income must also decrease as average traffic increases, since price is usageindependent. Figure 14 therefore implies that for business planning under flat pricing, it is particularly important to forecast the average traffic that would be offered by a customer. This estimate affects the network size needed to reach targeted levels for customer base and profitability.

Figure 15 shows the steady-state values of business performance measures when QualityRep<sup>Cv</sup> is varied from a low to high value. Three measures—total customers, operating income, and retained earnings— show upward trends. Because network capacity is fixed (ReinvRate<sup>Cv</sup>0), network performance must slope downwards. Intuitively, this is to be expected, since better initial reputation for quality attracts more customers. For management purposes however, the more interesting observation in Figure 15 is the very gradual increase in TotCust<sup>S</sup>, OpIncome<sup>Cv</sup>, and Ret-Earnings<sup>S</sup> as QualityRep<sup>Cv</sup> increases. There also appears to be indication of a saturation effect in that, at high values, increase in QualityRep<sup>Cv</sup> does not result in appreciable increase in performance values. We find this behavior interesting because it confirms the importance of maintaining service quality on an ongoing basis. The gradual increases in Figure 15 indicate that the beneficial effects of initial quality perceptions are short-lived. Perceptions of ongoing service quality have a more sustained influence on business performance.

## 3.7. Effects of Delays on Business Performance

In the preceding simulations, the two delay parameters, PercepDelay<sup>Cy</sup> and ImpDelay<sup>Cy</sup>, were kept at zero. Although the delays themselves are not management issues, we need to examine their effects because it is well known from systems theory that delays can introduce instabilities in system behavior, and stability of business performance is a management issue. A nonzero PercepDelay<sup>Cy</sup> means customers do not react to performance changes instantaneously. Due to the customer-network performance feedback loop identified earlier, this lag results in oscillatory behavior.

Figure 14 Steady-State Business Performance as Function of Average Customer Traffic Steady State Performance Indicators  
![](/api/attachments/AHS84NUF/fulltext/images/b0c524b016e3dc63fdcf1baa8fc2e5cf319150173e94b0f269be766de953b016.jpg)

Figure 15 Steady-State Business Performance as Function of Quality Reputation Steady State Performance Indicators  
![](/api/attachments/AHS84NUF/fulltext/images/edaa76055b52a5ffb29506d7e448ca0c29cece719fea7af248d35a5cfb2d700c.jpg)

In Figure 16, all scenario variables are exactly the same as Figure 10, except PercepDelay<sup>Cy</sup>, which has been set to 1. In Figure 10, where $\mathrm { P e r c e p D e l a y } ^ { C y } = 0 ,$ oscillations were present during the transient phase, but the system quickly reached steady state at about $T = 1 3$ . In contrast, Figure 14 shows that strong oscillations persist well after $T = 1 3$ with no signs of dissipation. In fact, larger delays result in oscillations with larger amplitude and longer time periods. Such ups and downs in business performance are usually not desirable and often have adverse impact on how a provider is viewed by the financial markets. Hence the management implication here is that a service provider should take the necessary steps to minimize perception delays through appropriate modes of communication with customers.

Implementation delays are only relevant when the provider is planning to expand the network—i.e., $\mathrm { \bar { R e i n v R a t e } } ^ { C v }$ is greater than zero. A nonzero Imp-$\mathrm { { D e l a y } } ^ { C y }$ will simply cause customer base, operating income, and retained earning levels to be delayed in time. Since all simulation runs so far have set $\mathrm { R e i n v R a t e } ^ { C v } ~ = ~ 0 ,$ , we will postpone presenting the effects of nonzero $\mathrm { I m p D e l a y } ^ { C \bar { y } }$ until §4, where decisionsupport capabilities are shown using positive reinvestment rates.

Figure 16 Dynamics of Business Performance with Perception Delays  
![](/api/attachments/AHS84NUF/fulltext/images/856041a3698d7e469d6d1fce2ab7704a64b351b3969434ddb5edbffb2e362041.jpg)

## 3.8. Summary of Insights into Business Process

At the start of §3.0, we mentioned that one of the useful applications of this systems model is to use it as a microworld within which to examine and understand issues facing service providers. Here we summarize some of the insights obtained from the simulations that were just described. Structurally, it is clear that the feedback loop between network operations, pricing, and customer dynamics is central to understanding basic system behavior. At the strategic planning level, one business implication of this finding is that it is critical to make marketing decisions in conjunction with network planning and operations. The experience of AOL in 1996 and others (Radosevich 1997) indicates that even prominent service providers sometimes neglect to consider this important interaction, causing damage to finances and reputation.

Another insight obtained from these simulations is the need to perform traffic engineering well. Specifically, it is necessary to have good estimates of average loads offered to the network by a typical user. A comparison of Figures 9 and 12 shows the significant impact of this parameter on steady-state network performance and the financials of the service provider. The tests also indicate that higher levels of average traffic per customer can also result in greater variability in business performance (compare transient behavior in Figures 9 and 12). The market usually does not view such variability positively. Historically, the old regulated telephone companies have always devoted considerable resources to traffic engineering, but online service providers have only recently begun to recognize this need (Fonseca 1999).

<table><tr><td colspan="3">Input Par...</td></tr><tr><td></td><td>AvgTraffic</td><td>0.5</td></tr><tr><td></td><td>FlatPrice</td><td>0.1</td></tr><tr><td></td><td>ImpDelay</td><td>0</td></tr><tr><td></td><td>PercepDelay</td><td>1</td></tr><tr><td></td><td>Quality Rep</td><td>1</td></tr><tr><td></td><td>ReinvRate</td><td>0</td></tr></table>

<table><tr><td>Perf</td><td>0.81</td></tr><tr><td>OpIncome</td><td>0.09</td></tr><tr><td>TotCust</td><td>1.15</td></tr><tr><td>RetEarnings</td><td>7.3</td></tr></table>

The importance of good communications with customers is also evident from our tests. This follows from test results involving system delays (compare transient behavior in Figures 10 and 16). They indicate that longer perception delays result in greater system instabilities, implying greater variability in business performance. Perception delays can be reduced by disseminating accurate, relevant, and timely information to customers through a variety of channels. While good communication with customers is generally recognized by service providers as being important, the reasons cited are usually customer satisfaction and retention. Our added insight is that good communications minimizes perception delays, thereby reducing business performance variability—a desirable objective.

Our steady-state tests confirm the well-known fact that a larger market share may not coincide with higher profitability (compare the plots of RetEarnings<sup>S</sup> and TotCust<sup>S</sup> in Figure 13). However, the interesting insight from Figure 13 is that the provider needs to have a good idea of customers’ threshold for acceptable network performance in order to balance their goals of high profitability and large subscriber base. This information can be obtained through a combination of user surveys and analysis of network traffic. As explained previously in §3.6, this performance threshold determines the price at which operating income and retained earnings will peak. Consequently, knowledge of this threshold value will enable business planners to determine practical ranges within which to trade off profitability and market share as desired.

The steady-state tests in Figure 15 indicate the need to maintain service quality on an ongoing basis (see the flat plots of business performance variables in Figure 15). In other words, initial reputation for quality is not a major determinant of ongoing business performance. The business implication, of course, is to emphasize the need for proactive network planning and operations management, and this need is being increasingly recognized by service providers (Vijayan 1999).

The insights into the impact of pricing changes are also interesting. In particular, we saw that with usagebased pricing, the impact of pricing changes can be counterintuitive. A price reduction (within appropriate ranges) results in a decrease in profitability as well as customer base (compare steady-state values in Figures 11a & b). Under flat pricing, a price reduction results in an increase in the number of subscribers but can also depress profitability. These patterns were shown to arise from the feedback loop between customer behavior and network performance, and they reinforce the importance of taking a systems view in making pricing decisions.

In summary, the systems model developed here can be used to gain better qualitative insights into the business process underlying the delivery of network services. Of course, the model is an aggregate one and is therefore simplified in certain respects. Nevertheless, it demonstrates the kind of systemic understanding necessary for business planning. Some of the insights summarized above have been suggested anecdotally in the practitioner literature. However, based on experiments with our model, we have a much firmer causal basis for understanding them.

## 4. Decision Support Capabilities

Beyond providing insights into issues of importance to service providers, our systems model can also be applied as a decision support tool for business planning. We show two examples using a prototype DSS that has been implemented. Figure 17 shows its user interface. The button labeled “Model Details” allows one to drill down to underlying structural details. Detailed features of the prototype will not be presented here. The first example involves a scenario in which a service provider wishes to plan for a steady target growth rate in TotCust<sup>S</sup>, its customer base, while maintaining a reasonable level of network performance. From discussions in §3, it is obvious that this cannot be achieved without expanding network capacity. Figure 18 shows a simulation with ReinvRate<sup>Cv</sup> rate set to 6%. Notice how TotCust<sup>S</sup> keeps increasing steadily with no degradation in Perf<sup>Cv</sup>. By carrying out sensitivity analysis on ReinvRate<sup>Cv</sup>, an acceptable balance between customer growth, network performance, and financial performance may be achieved. It is easy to identify other planning uses for the DSS.

Figure 17 Prototype DSS Implementation—User Interface Panel  
![](/api/attachments/AHS84NUF/fulltext/images/213a9954cd3c63bae6266a23c0ca4d1bc67cbe2508c683d444150651aef4cf27.jpg)

We close this section by showing the effects of nonzero implementation delay—ImpDelay<sup>Cy</sup>—which we had postponed from §3. The baseline behavior will be that in Figure 18, where $\mathrm { I m p D e l a y } ^ { C y } = 0 $ and $\mathrm { R e i n v R a t e } ^ { C v } = 6 \%$ . The values of scenario variables in Figure 19 are identical to those in Figure 18, except ImpDelay<sup>Cy</sup>, which equals 10 time periods. The dynamic behavior in the two figures is quite similar. Compared to Figure 18 however, the growth in Tot-Cust<sup>S</sup> starts much later in Figure 19, and there is more variability in Perf<sup>Cv</sup> prior to its stabilizing. Also, the end-of-run values of the performance variables are lower in Figure 19. In short, implementation delays will delay the realization of business benefits of network expansion, and may result in some interim instability in business performance. The decision support tool can be used in several other ways, but the preceding examples give some indication of its capabilities and modes of use.

## 4.1. Calibration Issues

In order to use the model for decision support, it will need to be calibrated for the specific circumstances of its use. This would be a major undertaking for a provider, but can be justified by the recurring benefits of using the calibrated model for ongoing decision support. In our view, the bulk of the effort required to calibrate this model involves estimating the functional relationships present therein. Of these, the relation between network capacity and installation cost, and network capacity and operational cost, can be approximated based on the historical records in the provider’s accounting or asset management information systems. Since network costs are a major element of fixed costs, most service providers maintain elaborate records on them. Industry studies on network costs also exist (Hamblen 1998) and may be adapted for use.

Historical records in the provider’s customer database can provide useful input on sensitivity to price changes. Software for tracking this kind of information is becoming available (Fonseca 1999), and may make it easier to generate the necessary data. However, this may need to be supplemented with customer surveys to identify users’ performance tolerances. Industry surveys on customer attitudes towards network service quality are becoming more common (Mehta 1999) and the results could be adapted for use here.

<table><tr><td colspan="3">Input Par...▼</td></tr><tr><td></td><td>AvgTraffic</td><td>0.5</td></tr><tr><td></td><td>FlatPrice</td><td>0.6</td></tr><tr><td></td><td>ImpDelay</td><td>10</td></tr><tr><td></td><td>PercepDelay</td><td>0</td></tr><tr><td></td><td>Quality Rep</td><td>1</td></tr><tr><td></td><td>ReinvRate</td><td>0.06</td></tr></table>

Figure 18 Business Planning Using Systems Model-Based DSS  
![](/api/attachments/AHS84NUF/fulltext/images/3783c3772f61b20e5c5d828dc1f3917ff4c7137b17b1e37b0ef0f44c2b866e41.jpg)

<table><tr><td colspan="3">Input Par...</td></tr><tr><td></td><td>AvgTraffic</td><td>0.5</td></tr><tr><td></td><td>FlatPrice</td><td>0.6</td></tr><tr><td></td><td>ImpDelay</td><td>0</td></tr><tr><td></td><td>PercepDelay</td><td>0</td></tr><tr><td></td><td>Quality Rep</td><td>1</td></tr><tr><td></td><td>ReinvRate</td><td>0.06</td></tr></table>

<table><tr><td>Perf</td><td>0.94</td></tr><tr><td>OpIncome</td><td>7.25</td></tr><tr><td>TotCust</td><td>13.19</td></tr><tr><td>RetEarnings</td><td>269.4</td></tr></table>

Figure 19 Dynamic Effects of Implementation Delay  
![](/api/attachments/AHS84NUF/fulltext/images/ee37d7f2c88b86f18cce21a6b939a252679de1ed97ecb60547b211be25bcf1a9.jpg)

<table><tr><td>Perf</td><td>0.92</td></tr><tr><td>OpIncome</td><td>5.37</td></tr><tr><td>TotCust</td><td>9.84</td></tr><tr><td>RetEarnings</td><td>178.6</td></tr></table>

Some parameters of the model are much less complex to estimate. For instance, typical values for implementation delay, ImpDelay<sup>Cy</sup>, can be approximated from operational records of equipment acquisition and deployment. Estimates for AvgTraffic<sup>Cv</sup> can be determined from network operations logs. Because network planning is generally a central activity for any service provider, the data for these estimates should not be hard to find.

## 5. Concluding Remarks

In this paper we have argued the need for adopting a systems thinking approach to business planning for network services, and developed a basic model using the systems dynamics methodology. It captures interactions and feedback effects characteristic of network service provision. The validated basic model offered a vehicle with which to achieve qualitative insights into the behavior of underlying business processes and examine important business issues facing service providers. The model, calibrated for specific circumstances, can also provide ongoing decision support to help network service providers increase customer retention, market share, and profits. Practitioners have recognized the need for such decision support products (Bucholtz 1998).

Clearly, the systems model developed here has limitations and can be enhanced in several ways. For instance, the customer arrival and departure processes can be modeled in more detail. In the current model, customers are implicitly assumed to be “memoryless.” In practice, however, a bad experience may result in the customer never returning to the same provider. Also, customers are not homogeneous in their needs and priorities. For the occasional user, price may be the major driver of behavior, while heavy users may be more sensitive to network performance than price. In the network operations sector, one can also enhance the model to include different classes of service, each with its own pricing scheme (Gagne 1998). The finance sector can be refined to reflect price-performance trends in technology and improved efficiencies in network operations made possible by new tools and technical standards.

One significant extension that is planned for future work is to capture the impact of content provision more explicitly, instead of parametrically, as is being done in this study. Modeling this effect introduces additional complexities in the customer sector of the SD model. One difficulty arises due to our still incomplete understanding of the different dimensions of content. As a result, it is not clear how one ought to operationalize the concept of provider content within an SD model. Also, with the introduction of content, the revenue generation structure in the SD model will need to change. Some websites, for example, offer free access and derive all their revenues from advertising. In turn, this advertising revenue is driven by how many users sign up for this free service. One reason some ISPs charge low flat-rate fees is simply to use that mechanism to attract more customers and then derive their revenues mostly from advertising. In short, the revenue generation structure needs to be extended to include network externalities arising from content provision and flat fees. Similarly, the impact of actions by competitors can be captured more explicitly in the Customer segment of the model structure instead of it being handled parametrically. This will involve building a feedback loop from the actions of competitors to the drivers of departing customer behavior for the service provider being analyzed. For instance, a price drop by a competitor will feed back to increase the departure rate of existing customers from the ISP. However, this means that some existing detail will have to be sacrificed from remaining model sectors to keep the overall model tractable.

It is important to emphasize that we see such systems thinking-based models as a part of a portfolio of tools that can help manage network service provision. It is useful for high-level types of planning activity and complements other models and methodologies (e.g., network performance models, Proceedings IEEE Modeling Analysis and Simulation 1998) that are used to address narrower aspects but in more detail.

## Acknowledgments

The authors wish to thank the associate editor and two anonymous referees for their detailed suggestions that improved the sections on model validity and qualitative insights.

## Appendix

Difference Equations for the Systems Dynamics Model of Network Service Provision

Legend of Symbols Preceding Equations:

▫ Stock

⇒ Flow into a stock

⇐ Flow out of a stock

O Converter

 Input converter

▫ PercepDelay(t)  PercepDelay(t  Dt) - (ServiceQuality  PerceivedQual) \* Dt

⇒ ServiceQuality  Perf

⇐ PerceivedQual  CONVEYOR OUTFLOW

▫ TotCust(t)  TotCust(t  Dt) - (NewCustomers 

DepartingCustomers) \* Dt

⇒ NewCustomers  FUNC(FlatPrice,CurrentQualrep)

⇐ DepartingCustomers  FUNC(FlatPrice,PerceivedQual)

▫ RetEarnings(t)  RetEarnings(t  Dt) - (Revenues Expenses) \* Dt

$$
\begin{array}{l} \Rightarrow \text { Revenues } = \text { TotCust*FlatPrice } \\ \Leftarrow \text { Expenses } = \text { Reinv   +   OpExpense } \end{array}
$$

▫ ImpDelay(t)  ImpDelay(t  Dt) - (AuthorizedCap  InstalledCap) \* Dt ⇒ AuthorizedCap  CostofCap ⇐ InstalledCap  CONVEYOR OUTFLOW

▫ Network(t)  Network(t  Dt) - (CapExpansion) \* Dt ⇒ CapExpansion  InstalledCap

O NetUtil  MIN(TotCust\*AvgTraffic/Network,1) O CostofCap  GRAPH(Reinv\$) O Perf  GRAPH(NetUtil) O OpIncome  Revenues  Expenses O Reinv\$  Revenues\*ReinvRate O OpExpense  GRAPH(Network) O CurrentQualRep  FUNC(QualityRep,PerceivedQual)

 FlatPrice  0.5  QualityRep  1  AvgTraffic  0.5  ReinvRate  0  PercepDelay [transittime]  0  ImpDelay [transittime]  0

## References

Anania, L., R. J. Solomon. 1998. Flat—the minimalist price. L. W. McKnight, J. P. Bailey, eds. Internet Economics. The MIT Press, Cambridge MA 91–118.

Barret, A. 1997. At AOL, more holes by the minute. Business Week 37 (Feb 24).

Bolton, R. N. 1998. A dynamic model of the duration of the customer’s relationship with a continuous service provider: The role of satisfaction. Marketing Sci. 17(1) 46–65.

Boucher, J. R. 1993. Traffic System Design Handbook: Timesaving Telecommunications Traffic Tables and Programs. IEEE Press, No. PP3251-QAJ, New York.

Bucholtz, C. 1998. NCR fights churn, Internet-style. Telephony 234(9) 58.

Burden, K. 1998. Choosing an internet service provider: What your peers say. Computerworld 32(4) 79.

Dellcave, T., Jr. 1997. AOL offline. Sales and Marketing Management. March 5.

Fattah, H. 1998. 1998 forecast: ISPs surviving the boom at \$19.95. MC Tech. Marketing Intelligence 18(1) 20.

Firdman, E. 1997. Rx for the Internet: Usage-based pricing. Data Comm. 26(1) 27.

Flynn, L. J. 1997. Netcom’s new price model tailors Internet services. New York Times (Mar 25).

Fonseca, B. 1999. Management tools for ISPs and carriers making headway. InfoWorld 21(50) 28.

Forrester, J. W. 1961. Industrial Dynamics. MIT Press, Cambridge, MA.

Gagne, C. 1998. What the experts say: Choosing an Internet service provider. Computerworld 32(4) 79–80.

Goodman, M. R. 1974. Study Notes in Systems Dynamics. MIT Press, Cambridge, MA.

Green, H. 1998. User-friendly wins the race. Business Week (Nov. 2) 114.

Hamblen, M. 1998. Network planning keeps costs down. Computerworld 32(42) 120.

Hamu, D. S., M. Fayad. 1998. Achieving bottom line improvements with enterprise wide frameworks. Comm. of The ACM 41(8)110– 113.

Hauben, M., R. Hauben. 1997. Netizens: On the History and Impact of Usenet and the Internet. IEEE Press, No. BP7706-QAJ, New York.

Hoffman, D. L., W. B. Kalsbeek, T. B. Novak. 1996. Internet and web use in the U.S. Comm. The ACM 39(12) 36–46.

James, K. 1996. AOL offers flat fee for unlimited use. USA Today (Oct 30).

——. 1997. AOL users take issue with refund deal. USA Today (Jan 31).

Keeney, R. L. 1999. The value of Internet commerce to the customer. Management Sci. 45(4) 533–542.

Kleinrock, L. 1976. Queuing Systems, Volume 2: Computer Applications. Wiley Interscience, New York.

Lange, L. 1998. The Internet in technology 1998: Analysis and forecast. IEEE Spectrum 35(1) 37–42.

Liles, D. H., A. R. Presley. 1996. Enterprise modeling within an enterprise engineering framework. J. M. Charnes, D. J. Morrice, D. T. Brunner, J. J. Swain, eds. Proc. 1996 Winter Simulation Conf. IEEE, Piscataway, NJ 993–999.

Lilien, G. L., P. Kotler, K. S. Moorthy. 1992. Marketing Models. Prentice Hall, Englewood Cliffs, NJ.

MacKie-Mason, J. K., L. Murphy, J. Murphy. 1998. Responsive pricing in the Internet. L. W. McKnight, J. P. Bailey, eds. Internet Economics. The MIT Press, Cambridge MA. 279–303

Mehta, M. 1999. ISP support & satisfaction. PC Magazine. 18(13) 229.

Petrazzini, B., M. Kibati. 1999. The Internet in developing countries. Comm. The ACM 42(6) 31–36.

POET White Paper. 1998. XML and the Internet: Driving the future of EDI. http://www.poet.com/edi.html#contents-.

Proc. IEEE Network Operations and Management Symposium. 1998. IEEE Communications Society, IEEE Press, No. CH36158-QAJ.

Proc. 6th International Symposium on Modeling, Analysis, and Simulation of Computer and Telecommunication Systems. 1998. IEEE Computer Society, IEEE Press, No. PR8566-QAJ.

Radosevich, L. 1997. ISP sings deregulation blues. InfoWorld 19(49) 1.

Rao, H. R., A. F. Salam , B. DosSantos eds. 1998. Marketing and the Internet. Comm. the ACM 41(3) 32–33.

Riezenman, M. J. 1998. Communications, in technology 1998: Analysis and forecast. IEEE Spectrum (January) 35(1) 29–36.

Robertazzi, T. G. 1999. Planning Telecommunications Networks. IEEE Press, No. PC5755-QAJ, New York.

Sengupta, K., T. Abdel-Hamid. 1993. Alternative conceptions of feedback in dynamic environments: An experimental investigation. Management Sci. 39(2) 411–428.

Stamper, D. A. 1999. Business Data Communications. Addison-Wesley Longman Inc., Reading, MA.

Swami, A. 1995. Building the business using process simulation. C. Alexopoulos, K. Kang, W. R. Lilegdon, D. Goldsman, eds. Proc. of IEEE 1995 Winter Simulation Conf. Piscataway, NJ 1081–1086.

Tanenbaum, A. 1996. Computer Networks. Prentice-Hall, New York.

Tedesco, R. 1997. AOL turns a profit, maybe a corner. Broadcasting and Cable 127(20) 60.

Tumay, K. 1996. Business Process Simulation. J. M. Charnes, D. J. Morrice, D. T. Brunner, J. J. Swain, eds. Proc. 1996 Winter Simulation Conference. 93–98.

Vijayan, J. 1999. Capacity planning more vital than ever. Computerworld 33(7) 64.

Wallace, B., M. Wagner. 1997. AOL debacle raises service quality fears. Computerworld 31(5) 1.

Wang, Y. M., J. Gallaugher, S. Vasudevan. 1996. The determinants of network growth: The case of online information services. Proc 17th Int’l Conference on Information Systems, Cleveland OH, 35–248.

Wolstenholme, E. F. 1990. System Enquiry—A System Dynamics Approach. Wiley, New York.

Edward Stohr, Associate Editor. This paper was received on June 9, 1999 and has been with the author 6 months for 2 revisions.
