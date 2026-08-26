---
otero_id: 20901
otero_key: "GQTD983Q"
title: "Analysis and visualization of market power in electric power systems"
authors: "Thomas J. Overbye; James D. Weber; Kollin J. Patten"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00101-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analysis and visualization of market power in electric power systems

Thomas J. Overbye <sup>a,)</sup>, James D. Weber <sup>a</sup>, Kollin J. Patten <sup>b</sup>

<sup>a</sup> Department of Electrical and Computer Engineering, UniÕersity of Illinois at Urbana–Champaign, 1406 W. Green,

Urbana, IL, 61801, USA

<sup>b</sup> PowerWorld Corporation, 2004 S. Wright St., Urbana, IL, 61801, USA

## Abstract

This paper discusses the assessment and visualization of market power in bulk electricity markets, with the explicit consideration of transmission system constraints. In general, market power is the ability of a particular seller or group of sellers to maintain prices profitably above competitive levels for a significant period of time. When an entity has and exercises market power, it ceases to be a price-taker and becomes a price-maker. The restructuring of the electric industry in many parts of the world has encouraged competitive markets with the objective of reaping the benefits of lower prices and innovation that competition can provide. Such benefits are not attainable when a player utilizing the electric transmission system may exert market power. This paper describes the procedures for analyzing and visualizing such situations. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Power system market power analysis; Power system visualization

## 1. Introduction

The electric power industry throughout the world is in a period of radical and rapid restructuring, with the traditional paradigm of the vertically integrated electric utility structure being replaced by competitive markets in unbundled electricity services with disaggregated structures. In the United States, the Federal Energy Regulatory Commission FERC is- Ž . sued its Order 592 APolicy Statement on Utility MergersB in December 1996 1 with the explicit<sup>w</sup> <sup>x</sup> objective of streamlining and expediting the processing of merger applications in the new competitive environment. The central focus of this policy is on the Aeffect on competitionB of proposed mergers. FERC’s formal adoption of the Department of Justice<sup>r</sup>Federal Trade Commission DOJŽ . <sup>r</sup>FTC Horizontal Merger Guidelines <sup>w</sup> <sup>x</sup> 2 as the framework for competition has triggered a strong interest in the analysis of market power issues in electricity markets. The same guidelines appear in the more recent FERC proposed rulemaking 3 .<sup>w</sup> <sup>x</sup>

Market power is the antithesis of competition. It is the ability of a particular seller or group of sellers to maintain prices profitably above competitive levels for a significant period of time. When an entity has and exercises market power, it ceases to be a price-taker and becomes a price-maker. The ambitious restructuring of the electricity industry has as its goal to reap the benefits of lower prices and innovation resulting from the establishment of competitive marketplaces for electricity products and services. This drive to competition is being accompanied by the unbundling of services and the disintegration of the vertical structures of the industry.

However, this drive to competition has also given rise to significant concerns that the potential benefits resulting from the breaking of the vertical market power of the traditional utility could, in time, be supplanted by the establishment of horizontal market power. Events during the week of June 22, 1998 on the U.S. Midwest electrical system indicate that the potential impact on prices could be substantial. As reported in Ref. 4 , during periods of heavy loading, <sup>w</sup> <sup>x</sup> spot prices in the Midwest soared up to US\$7500 per MW h, over 100 times the average energy price.

The restructuring in electricity markets and the issuance of the FERC Merger Guidelines have brought about intense interest in the study of market power issues in the electricity industry 5–7 . Most <sup>w</sup> <sup>x</sup> studies of market power review the structure, conduct and performance of a market. However, significantly less work has been done to investigate the key impact the transmission system has on market power issues.

The objective of this paper is to provide an overview of the impact that the electrical transmission system has on the analysis of market power issues, with particular emphasis on the impacts of transmission congestion. Additionally, given the complexity of the issue, an important component of this work is effective visualization of the issues involved in market power analysis, particularly, with regard to the analysis of large systems. The paper discusses several pertinent visualization ideas, including contouring and the use of virtual reality Ž . VR data visualization.

## 2. Market power analysis in electricity markets

The analysis of market power typically involves the following steps 1 : <sup>w</sup> <sup>x</sup>

v Identification of the relevant products<sup>r</sup>services,

v Identification of the relevant geographic market,

v Evaluation of market concentration.

For market power analysis in electricity markets, FERC has typically considered at least three distinct products: nonfirm energy, short-term capacity firmŽ energy and long-term capacity. Product groupings. are allowed when the products are reasonable substitutes for each other from the buyer’s perspective. As restructuring progresses, the emphasis appears to be shifting from the long-term capacity market to the short-term energy markets 3 . Therefore, the empha-<sup>w</sup> <sup>x</sup> sis of this paper will be on the short-term energy markets. The challenge in performing this analysis is that electricity demand varies substantially over time and, of course, there are few economic means for storing this energy. This requires analysis for a variety of different market conditions.

The second and by far the most difficult step in performing market power analysis for an electricity network is the determination of the geographic scope of the market for the product. In our definition, the market is based on the capability of a supplier, say a generator, to deliver the product<sup>r</sup>service to a buyer, say a load. The size of the electricity markets is dependent upon both the physical<sup>r</sup>operational characteristics of the transmission network used to enable the movement of electricity from the supplier to the customer and the impacts of the services in transporting this energy, including any prices charged. These issues are the key focus of this paper and will be discussed in-depth.

A key step in performing market power analysis is the analysis of market concentration. A commonly used methodology is the Herfindahl–Hirschman index HHI 8 , defined as:Ž . <sup>w</sup> <sup>x</sup>

$$
\mathrm{HHI} = \sum_ {i = 1} ^ {N} q _ {i} ^ {2},\tag{1}
$$

where N is the number of market participants and $q _ { i }$ is the percentage market share of each participant. Hence, the HHI for a monopoly would be $1 0 0 ^ { 2 } =$ 10,000, while HHI would be a small number when

N is large and no participant has more than say 5% market share. Under DOJ<sup>r</sup>FTC standards for horizontal market power 2 , post-merger values of HHI under 1000 are considered to represent an unconcentrated market that are unlikely to have adverse competitive effects. Post-merger values between 1000 and 1800 are considered to be moderately concentrated. Values above 1800 are deemed to be highly concentrated; mergers increasing the HHI by more than 100 points are viewed as likely to create or enhance market power.

## 3. Market power analysis without transmission considerations

For electricity markets, the appropriate definition of the market is critical. Clearly, both physical factors — the transmission network and its operation — and economic factors — the market structure and its rules — are determining elements in this definition. To motivate this discussion, initially consider the case in which the transmission system is not explicitly considered and no transportation charges are incurred in moving power from the generator to the load. Without explicit consideration of the transmission system, there is a tacit assumption that each MW of generation could reach any desired load location, or conversely that each MW of load may use as a source of supply any generator within the interconnected system. The degree to which any single producer can exercise market power depends solely on its concentration of ownership relative to that of the other producers for the entire interconnected system.

For such systems, calculation of the HHI values is straightforward. For example, in North America, the HHI values can be calculated using data from the North American Electric Reliability Council NERC ,Ž . which lists generation capacity for both the winter and summer peaks. Using the 1997 data average ofŽ summer<sup>r</sup>winter peaks , the Eastern Interconnect had . a total capacity of 593 GW with about 650 different market participants. Without any consideration of the transmission network, the associated HHI for the Eastern Interconnect is about 170. Clearly, for this conceptual case, completely ignoring consideration of transmission system constraints and transportation charges, no market power exists. Mergers between even the largest utilities in the Interconnect would not substantially affect this value. Similar values for each of the NERC Reliability Councils are reported in Ref. 7 .<sup>w</sup> <sup>x</sup>

Of course, neglecting the transmission system and its associated charges is usually inappropriate, particularly, for a large system. To aid in determining the appropriate geographic market of potential suppliers to a particular customer, FERC requires that the suppliers must be able to reach the market both economically and physically. The FERC economic criteria require that a supplier must be able to deliver to a customer at a cost no greater than 105% of the competitive price to that customer. The delivered cost is the sum of the variable generation cost and the transmission and ancillary service charges. Therefore, the market size is dependent upon the particular mechanism used for transmission pricing.

Several mechanisms are used for pricing transmission services, with a recent survey found in Ref. 9 .<sup>w</sup> <sup>x</sup> Whenever there are a number of transmission providers whose services are used to get delivery of power<sup>r</sup>energy from a designated source to a designated sink, the ApancakingB of the transmission charges of each provider may occur. The net effect of these pancaked rates is to limit the size of the market since more distant suppliers incur increasingly larger transmission charges. The move away from pancaking is a big motivator for the establishment of the so-called Independent System Operator Ž . ISO . The ISO is a control entity that is the sole operator<sup>r</sup>controller of the transmission system in a specified region. Under the 11 ISO principles promulgated by FERC in its Order No. 888, a single rate for the interconnection supplants the various tariffs of the transmission providers. The establishment of an ISO and its accompanying ApostagestampB pricing mechanisms have the desirable impact of enlarging the seller’s and<sup>r</sup>or buyer’s potential market in a given region, effectively lowering the HHI.

## 4. Market power analysis with transmission constraints

Market size can be limited not only by economics, but also by the physical capability of the transmission system. A key issue to be addressed is how to incorporate the impact of the transmission system and any consequent congestion. Congestion arises because the capacity of the transmission system has a finite but usually not easily determined value. That is to say, the ability of the transmission system to support additional power transactions is limited by the need to maintain system security. Transmission system capacity is limited due to a number of different mechanisms, including transmission line<sup>r</sup>transformer line limits, bus voltage lim-Ž . its, transient stability constraints and the need to maintain system voltage stability. Here, we just consider the impact of line limits, but the incorporation of bus voltage limits is relatively straightforward. Other limits could be directly incorporated if they can be recast in terms of line<sup>r</sup>flowgate limits. A line is said to be congested anytime it is loaded at or above its MV A limit.

![](/api/attachments/GQTD983Q/fulltext/images/2ec9e09db24cab313bdefeaa880b55407b4a611cc4fdb7f3bc93d67ac05a5c75.jpg)  
Fig. 1. Radial system with market power.

The simplest case illustrating the impact of the transmission system in market power analysis is the radial single bus system modeled in Fig. 1. Here, the load at bus A can be served either by local generation at bus A, or through the single transmission line joining bus A with the rest of the electric system. The pie-chart in the line shows the percentage loading on the line; here the line is loaded at 100% of its rated capacity so the pie-chart is completely filled-in, with the arrows indicating the direction of flow 10 .<sup>w</sup> <sup>x</sup> Because of this 100 MV A flow limitation on the line, the generator at bus A has complete market power anytime the load at the bus exceeds 100 MW. That is, in the short term, the only option available to the customers receiving energy at bus A is to pay the price charged by the bus A generator, or to do without. Hence, the number of participants in the generation market available to the bus A Aload pocketB is effectively one. Hence, the effective HHI is 10,000. Note that this limitation is completely independent of generator costs and transmission tariffs. Of course, if the load is variable, such market power is only present when the bus A load exceeds the line’s import capacity.

If a second line is added between bus A and the rest of the system, the situation becomes substantially more complex. Bus A is no longer radially connected to the remainder of the network, but is now an integral part of the network. A key point in performing this analysis is that the maximum power that can be imported into the bus A load pocket is not, in general, equal to the sum of the limits of the two lines joining it with the remainder of the network. Rather, this sum only provides an upper limit. The actual import limit depends upon both the impedance of the remainder of the network and the particular power flows in that network. The interface Ži.e., all of the lines joining bus A to the rest of the system is congested anytime either of the lines . reaches its limit. The import limit can actually be less than the individual line limits. Such a situation is illustrated in Fig. 2 for a simple three-bus system in which 25 MW is being AwheeledB through bus A, decreasing its import capability to about 74 MW, below either of the 100 MV A line limits. An important point for such a networked case is that the ability of bus A to import or export power depends strongly upon conditions in the rest of the electrical system.

![](/api/attachments/GQTD983Q/fulltext/images/cb95f1a4efba6446aed71810118cc21dea643df7217176a0d4b9f2b1a450af92.jpg)  
Fig. 2. Three-bus example with import<sup>s</sup>74 MW.

For the generalized case, define the area A load pocket as the set of loads, possibly located at multiple buses, that buy power in aggregate and, hence, are subject to similar or identical pricing. ExamplesŽ . of load pockets could be a municipality without sufficient internal generation, a cooperative system, or a load aggregator. The load pocket is then connected to the remainder of the interconnected system through a set of transmission lines. The degree of market power enjoyed by a set of commonly owned generators i.e., a portfolio of generators with re- Ž . spect to serving the area A load pocket depends upon the generation market available to area A. This, in turn, depends upon the characteristics of the transmission system, including its present level of loading.

Our approach to determining the generation market available to a particular load pocket starts with results provided by the Simultaneous Interchange Capability SIC algorithm. SIC seeks to quantify theŽ . amount of power that can be imported into a particular load pocket. Determination of SIC is, thus, an optimization problem whose objective is to determine the generation dispatch that maximizes the amount of power that can be imported into the load pocket. Linear load flow and linear programming solutions have made SIC calculation relatively fast and easy 11–15 when appropriate assumptions are<sup>w</sup> <sup>x</sup> made concerning the response of the affected generation. If assumptions are made that all generators respond in such a way to maximize the interchange value, the SIC provides an upper bound on power import. For the Fig. 2 three-bus system the SIC value is 200 MW, which is achieved when bus B generation is 200 MW and bus C generation is 300 MW. However, the SIC solution is not identical to solving the market power problem. The key difference lies in the assumptions concerning the response of the generators — in a competitive marketplace, all generators will certainly not respond in a way to maximize import. While some generation portfolios may indeed be working to maximize the import into the load pocket, others may actually seek to minimize this value to enhance their ability to exploit market power.

In order to understand the potential implications of this behavior on market power analysis, two interrelated issues must be discussed. First, in a networked transmission system the incremental changes in the amount of power generated and<sup>r</sup>or consumed at a set of buses can result in changes in the power flow throughout a large portion of the network. That is, a power transfer through the system can potentially impact other parties not involved in the transfer; this is commonly referred to as Athird-party impactsB or Aloop flows.B How the power distributes through the system depends upon the particular direction considered, as well as on the characteristics of the transmission system. This incremental change in flows associated with a particular direction has been defined by NERC as the power transfer distribution factors PTDF s. The PTDF val-Ž . ues provide a linear approximation of how the power flows would change for a particular power transfer between different pairs of generation portfolios and load pockets.

The second issue is that whenever a line or interface is congested, the system’s ability to support additional power transfers can be limited, even for directions remote from the point of congestion. Which directions are limited depends upon whether a transfer would increase or decrease loading on the congested line.

To illustrate these two issues, consider the ninebus system shown in Fig. 3. For simplicity, this system has been designed with the following characteristics:

1. Each bus has a single generator with a capacity of 500 MW and a single 250-MW load,

2. Each bus initially corresponds to a single market participant a single operating area , Ž .

![](/api/attachments/GQTD983Q/fulltext/images/f690f1d3f25bb2bc71e21019f0bd7e7eb7b38d7034dc5e4ce3b4f89203e8e319.jpg)  
Fig. 3. Nine-bus base case flows.

3. All transmission lines have impedance of j0.1 per unit and a limit of 200 MV A.

Each area is assumed to be controlling its interchange, with several initial base case transactions modeled as shown in Fig. 3. For this case, the SIC value is greater than the load at each bus. Therefore, as a starting point, we will assume that each load can buy from any of the nine generators. Thus, the effective market encompasses the entire system, allowing for straightforward calculation of the HHI index using generator capacity . Each of the nine Ž . participants has 11.1% market share resulting in an HHI of 1110, indicating no market power.

Starting from the base case flows, the PTDF values can be used to provide a linear approximation of the impact caused by a proposed power transfer from a source to a sink. Note that while the PTDF values are only a linearized approximation, this approximation is usually valid over a wide variation in operating points. As an example, Fig. 4 shows the PTDF values for the nine-bus system for a proposed power transfer from bus A to bus I to reduce clutter,Ž the buses<sup>r</sup>generators<sup>r</sup>loads are now shown as just an ellipse . The pie-chart values now show the PTDF. values, expressed in terms of a percentage of the power transfer amount. Fig. 4 indicates that 44% of the transaction flows along the transmission line from bus A to B, while 35% flows from G to F. The change in flow along the particular path is then the PTDF value multiplied by the power transfer. Thus, a 50 MW transfer from A to I increases the MW flow from A to B by about $5 0 \times 4 4 \% = 2 2 \mathrm { M W }$ . The

![](/api/attachments/GQTD983Q/fulltext/images/0dfcab0cd4101728a48bd8207e52ec6eb84ec3fb988126b809c461132f4809d4.jpg)  
Fig. 4. PTDF values for transfer from A to I.

![](/api/attachments/GQTD983Q/fulltext/images/7e578bb7925761c34e4bb7fb7448633f1d5e3931964cfed804d862626d6d5e7e.jpg)  
Fig. 5. PTDF values for transfer from G to F.

PTDF values for a transfer from G to F are shown in Fig. 5. Note that the PTDF values for both cases indicate that the transfers would have significant impacts on almost all of the transmission line flows. Present NERC line-loading relief criteria deem any transaction having a PTDF value of greater than 5% on a limiting element as having a significant impact on the element’s flow.

The PTDF values can also be used to help estimate the maximum amount of power that can be transferred on a particular direction i.e., a specifiedŽ source<sup>r</sup>sink pair 16 . This value is determined by. <sup>w</sup> <sup>x</sup> recognizing that for a direction j, the real power flow on any line i, $P _ { i } ,$ due to a transaction in direction j can be approximated as:

$$
P _ {i} = P _ {i 0} + d _ {i j} P _ {\mathrm{Tj}},\tag{2}
$$

where $d _ { i j }$ is the PTDF for line i in direction j, $P _ { i 0 }$ is the base case flow on the line and $P _ { \mathrm { T } j }$ is the magnitude of the proposed transfer. If the limit on line i is $P _ { i \mathrm { \ m a x } }$ , the maximum power that can be transferred in direction j without overloading line i is:

$$
P _ {\mathrm{Tjmax} i} = \frac {P _ {i \max} - P _ {i 0}}{d _ {i j}}.\tag{3}
$$

The maximum value of $P _ { \mathrm { T } j \mathrm { \ m a x } }$ that can be transferred without overloading any line in the set consisting of all lines in the system, , is then:

$$
P _ {\mathrm{T} j \max} = \min _ {i \in \Lambda} \left[ \frac {P _ {i \max - P _ {i 0}}}{d _ {i j}} \right].\tag{4}
$$

With the nine-bus case, the maximum transfer from A to I is actually limited by minimum generation in area I. If this constraint is ignored, the maximum allowable additional transfer is 148 MW; the limiting element will be the line from A to G. The maximum for the G to F transfer is about 94 MW, with the line from G to F the limiting element.

PTDF calculations are important to consider in market power analysis because operating practice forbids the initiation of new transfers that register a significant PTDF on the congested line or interface, in the direction such that the transfer would increase the loading on the congested element, where significant PTDF is often quantified as a PTDF in excess of 5%. For example, for the nine-bus system, Table 1 shows the PTDF values for line G–F with flowŽ from G to F assumed to as positive for different. suppliers sending power to the I load pocket. Thus, if congestion was present on the line from G to F, the number of sellers that have access to the bus I load pocket is significantly decreased 17 . For such a<sup>w</sup> <sup>x</sup> case, area I consumers could only buy from areas I, E and F. Therefore, the resultant market power index for area I is now $3 \times 3 3 . 3 ^ { 2 } = 3 3 2 7$ , indicating significant market concentration.

Results from Ref. 18 show that for markets with<sup>w</sup> <sup>x</sup> such small numbers of producers optimal bidding strategies require bids substantially above the producers marginal costs. Note though that this market power only exists when the line is congested. Also, this congestion is one sided. When the direction is reversed the PTDF values simply change sign inŽ general, this is true only for a lossless system, such as the one considered here, with no active singlesided limits such as generator MW limits or transformer phase shifter limits . Therefore, generation in. I can sell to all other areas except for F.

Table 1 Line G to F PTDF values

<table><tr><td>Seller/buyer (direction)</td><td>Line G to F PTDF (%)</td></tr><tr><td>A to I</td><td>35</td></tr><tr><td>B to I</td><td>29</td></tr><tr><td>C to I</td><td>11</td></tr><tr><td>D to I</td><td>5</td></tr><tr><td>E to I</td><td>-1</td></tr><tr><td>F to I</td><td>-20</td></tr><tr><td>G to I</td><td>41</td></tr><tr><td>H to I</td><td>21</td></tr></table>

## 5. Strategic market power

The fact that transmission congestion can limit market size creates the possibility that owners of portfolios of generators could deliberately dispatch their generation in order to induce congestion for strategic purposes 17 . For example, again, consider <sup>w</sup> <sup>x</sup> the Fig. 3 nine-bus case. Initially, this system has an apparent HHI of 1110, indicating no market concentration. Now assume that areas F and G merge, creating area FG, which now has a 22.2% market share. The other seven participants still have a 11.1% share, resulting in an apparent HHI of only 1355. However, with geographically dispersed generation, FG now has at least some ability to unilaterally AmanipulateB the flows throughout the system and, hence, the potential to deliberately induce congestion for strategic purposes.

To quantify this potential, we first examine the ability of a particular set of generators with common ownership to unilaterally control the flow of power on various lines. Assume that a set of N generators is currently producing some total base case output and that the generators owner is free to control their dispatch. Hence, the generators could be redispatched in such a way to modify the flow on a particular line i, provided the net change in generation is zero. Therefore, the maximum ability of this set of N generators to unilaterally control the flow on a particular line i can be formulated as a maximization problem:

$$
\max \Delta P _ {i} = \sum_ {k = 1} ^ {N} d _ {i k} \Delta P _ {k} \quad \text { s   .   t   . } \quad \sum_ {k = 1} ^ {N} \Delta P _ {k} = 0,\tag{5}
$$

where $d _ { i k }$ is the sensitivity of the line i power flow to a 1 MW increase in the bus k generation, $\varDelta P _ { k }$ is the change in the bus k generation and $\varDelta P _ { i }$ is the change in the flow on line i. For convenience, we define this value as the Unilateral Line Control Factor ULCF . The ULCF for lineŽ . i is maximized by increasing the generators with the most positive $d _ { i k }$ and decreasing those with the most negative values, subject to generator maximum<sup>r</sup>minimum MW limits. Hence, the ability of a portfolio of generators to unilaterally control flows depends upon the number and capacity of the generators in the portfolio and their geographic location within the transmission system.

For the merged two generator FG area, with $\varDelta P _ { \mathrm { F } } = - \varDelta P _ { \mathrm { G } }$ , Eq. 5 reduces to:Ž .

$$
\mathrm{ULCF} _ {i} = d _ {i \mathrm{F}} \Delta P _ {\mathrm{F}} - d _ {i \mathrm{G}} \Delta P _ {\mathrm{F}} = \Delta P _ {\mathrm{F}} \left(d _ {i \mathrm{F}} - d _ {i \mathrm{G}}\right),\tag{6}
$$

where the flow sensitivity values, $d _ { i \mathrm { F } } - d _ { i \mathrm { G } }$ , are shown in Fig. 5. Starting from the Fig. 3 base flows and a maximum allowable change of $\varDelta P _ { \mathrm { F } }$ of 250 MW, the implication is area FG can unilaterally induce congestion on line G–F and, hence, block areas A, B, D and H from the area I market. The percentage line loadings for this scenario are shown in Fig. 6. FG can still sell into the area I market because generation at F is not blocked.

A market participant’s physical ability to create congestion depends upon the mechanism used to obtain transmission access<sup>r</sup>dispatch generation, the portfolio of available generation and the current system operating point. From FG’s point of view, the best mechanism for transmission access<sup>r</sup>generation might be one in which it had complete priority in access to transmission line G to F, such as that given a utility when serving its native load. At the other end of the spectrum might be a bid-based ISO. However, even with such an ISO, area FG could still devise a bidding strategy which allowed it to achieve congestion on line G to F and, hence, sell into a relatively constrained area I. The success of such a strategy would, of course, be dependent upon expected system loading.

![](/api/attachments/GQTD983Q/fulltext/images/274f951a3606ddfbd1d70151bef79c4cefe5b2b61d32872cf361e6b599888796.jpg)  
Fig. 6. Area FG Blocking Area I Market.

A strategy of deliberately creating congestion could certainly involve additional cost to the congestor, with the exact value dependent upon how far it must deviate from an economic dispatch. The increase in profit is then the difference between the additional income gained from the congestion and the costs incurred in creating the congestion. The congestor would only pursue such a strategy if they had a reasonably good expectation of profit. However, as was mentioned in the introduction, events during summer 1998 indicate that such profits could be substantial. From a long-term perspective, market participants should certainly be cognizant in procuring their generation portfolios of both their own and the ability of their competitors, to engage in such strategic behavior. Likewise, those involved with devising market rules, approving generation portfolios and policing the system, must also be aware of such strategic behavior.

## 6. Market power assessment

Assessment of market power requires determination of the generation market available to each load pocket, or conversely, the load market available to each generation portfolio, taking into account the potential for strategic behavior by one or more market participants. Thus, the problem has two sets of players, those who are seeking to sell to the load and, hence, will try to maximize the power transfer to the load pocket the Maximizers and those seek-Ž . ing to prevent others from gaining access to the load Ž . the congestors or the Minimizers . An exact solution to this problem would require a noncooperative game theory approach in which the two players simultaneously seek the best possible outcome assuming the worst possible choice by the other 19 . A direct<sup>w</sup> <sup>x</sup> solution to this problem could be computationally taxing, particularly, for large systems.

Here, we propose to approximate this solution by solving the SIC problems with simplified assumptions about the impact of the congestors. Once a set of congestors has been specified, the ULCF results of Eq. 5 could be used to derate the limits on eachŽ .

![](/api/attachments/GQTD983Q/fulltext/images/6a1806bf53ac9914354a0fc21b8fb073f31a99b00000017b2313094327805a9e.jpg)  
Fig. 7. Nine-bus system with congestion from G to F.

line i by the amount ULCF . Please note that ULCF is the maximum amount by which the congestors can unilaterally manipulate the flow on line i. If the SIC problem is solved using these assumptions, the results provide the minimum amount of power that can be imported into the load pocket. This value is minimum because the congestors could not simultaneously modify the flow on all the affected lines by that line’s maximum amount ULCF .

As an example, Fig. 7 again shows the Fig. 6 case of area FG attempting to block the import of power into I from other areas. Here the line limits were first derated using Eq. 5 . Results of these derated limitsŽ . are shown in Table 2. The SIC algorithm was then solved using the derated limits with the assumptions that all the other generators in the system i.e., all Ž but the generators at F and G are redispatched so as . to increase the net import of power into area I. SIC results are shown in Table 3.

Table 2  
Derated line limits

<table><tr><td>Line</td><td>Limits (MV A)</td><td>ULCF (MW)</td><td>Derated limits (MV A)</td></tr><tr><td>A to B</td><td>200</td><td>15</td><td>185</td></tr><tr><td>A to G</td><td>200</td><td>15</td><td>185</td></tr><tr><td>B to C</td><td>200</td><td>45</td><td>155</td></tr><tr><td>B to G</td><td>200</td><td>30</td><td>170</td></tr><tr><td>C to D</td><td>200</td><td>15</td><td>185</td></tr><tr><td>C to E</td><td>200</td><td>30</td><td>170</td></tr><tr><td>D to E</td><td>200</td><td>15</td><td>185</td></tr><tr><td>E to F</td><td>200</td><td>47</td><td>153</td></tr><tr><td>E to I</td><td>200</td><td>2</td><td>198</td></tr><tr><td>F to G</td><td>200</td><td>153</td><td>47</td></tr><tr><td>F to I</td><td>200</td><td>50</td><td>150</td></tr><tr><td>G to H</td><td>200</td><td>52</td><td>148</td></tr><tr><td>H to I</td><td>200</td><td>52</td><td>148</td></tr></table>

Table 3  
SIC results for Fig. 7 case

<table><tr><td>Generator</td><td>Change (MW)</td></tr><tr><td>Export from Area A</td><td>0</td></tr><tr><td>Export from Area B</td><td>0</td></tr><tr><td>Export from Area C</td><td>38.2</td></tr><tr><td>Export from Area D</td><td>66.5</td></tr><tr><td>Export from Area E</td><td>95.3</td></tr><tr><td>Export from Area H</td><td>0</td></tr><tr><td>Import into Area I</td><td>200</td></tr></table>

Note that the Fig. 7 results differ from those of Fig. 6. In the Fig. 6 case, the assumption is that FG initially congests the line from G to F; subsequently, the only areas that can sell into area I are those with negative line GF PTDF values. This is analogous to the case where each area independently dispatches its generation. In contrast, in the Fig. 7 case, the system is assumed to be dispatched simultaneously, analogous to what might occur in an ISO. Area I could now receive at least some power from Areas C and D as well as from Areas E, F and G.

## 7. Large system visualization

While the previous issues were demonstrated using a small system, they are certainly applicable to practical cases of any size. An example of a larger case is the 1998 ECAR FERC 715 case, which contains a very good representation of the transmission system in the Eastern Interconnect, with over 30,000 buses, 5000 generators, 41,000 transmission lines<sup>r</sup>transformers and 130 control areas 20 . A<sup>w</sup> <sup>x</sup> portion of the high-voltage transmission system for this system is shown in Fig. 8. The potential for strategic market power situations can be seen by noting the extensively large number of loops in the system. The presence of congestion involving only small portions of the system may result in the cancellation of a large number of transactions. An important additional issue is that with thousands of transmission-dependent utilities, such as many municipal, cooperative systems and, in the future, perhaps load aggregators, market power needs to be assessed not just for the system as a whole, but also for the thousands of individual Aload pocketsB that these systems represent.

![](/api/attachments/GQTD983Q/fulltext/images/aa5be8b6b4be418a7681cbf0238058ebe6c01e762012d9d488134692f70084fd.jpg)  
Fig. 8. High-voltage transmission system flows in Eastern North America.

A difficulty in analyzing such large systems is to relatively quickly convey to the user information about system loading and, hence, the potential for market power abuse. Here, we present several visualization techniques for addressing this issue.

The first technique for quickly indicating the loading of a large network has been the use of dynamically-sized pie-charts to indicate loading on each transmission line. As an example, Fig. 9 again shows the Fig. 8 system with pie-charts used to indicate the loading on each transmission line. The percentage fill in each pie-chart is equal to the percentage loading on the line, while the size and color of the pie-chart can be dynamically sized when the loading rises above a specified threshold. For example, assume in the Fig. 8 case that the user was only concerned with those lines at or above 70% loading. By specifying that the pie-chart increase in size by a factor of 5 if above 70% or a factor of 7 if above 80%, it is easy, even in a large system, to see the heavily loaded lines.

![](/api/attachments/GQTD983Q/fulltext/images/b75eac2543ae62170ccbe5efa17d04b2559aca68a1462f2f072ffff9305d888d.jpg)  
Fig. 9. Pie charts showing line MV A percentages.

Using pie-charts to visualize these values is helpful, but this technique also runs into difficulty when a large number of pie-charts appear on the screen or in situations where the fill-in on each pie-chart is small. To remedy this problem, an entirely different visualization approach was investigated: contouring. Contouring has, of course, long been used for the display of spatial data, with the newspaper temperature contour maps one well-known example. Application of contouring to power system voltage magnitudes and line flows has been previously discussed in Refs. 21,22 . An example of a line flow contour is<sup>w</sup> <sup>x</sup> shown in Fig. 10. Key to effective use of line flow contours is to only show those line flows loaded above a specified percentage. This is akin to a TV radar image in which only areas of precipitation are shown. In the Fig. 10 case, only those lines loaded above 50% are highlighted.

Additional uses of contouring could be to show the PTDF values associated with a particular power transfer or the ULCF values for a particular portfolio of generators. For example, Fig. 11 shows a contour of the PTDF values associated with a power transfer between Southern Company to the New York Power

![](/api/attachments/GQTD983Q/fulltext/images/4b308336d6728a8aa282f4b539e2b6daa26d8977bca936573a04f20b2a16357e.jpg)  
Fig. 10. Percent MV A percentage contours.

![](/api/attachments/GQTD983Q/fulltext/images/f71273f60945bad21dc2215c8e19cd08d812f66a63f5deeb7a4fc88fb87f0cb3.jpg)  
Fig. 11. PTDFs for transfer from southern to NYPP.

Pool NYPP . Note that the power flows spreadŽ . throughout a large portion of the system. Overall for this transfer about 280 lines have PTDF values above the 5% threshold. While this is a small fraction of the 41,000 lines in the case, the impacted lines tend to be the high-voltage lines that would be used by numerous transfer directions.

## 8. Virtual environment data visualization

The previous data visualization techniques can be quite useful when one is primarily concerned with visualization of a single type of spatially oriented data, such as transmission line voltages or bus voltages. However, often in power systems, the relationships between a number of layered systems need to be considered. A pertinent example could be the relationship between the actual transmission system flows and the PTDF values associated with a proposed transaction. Here we provide some initial results on the use of VR to visualize such systems.

Virtual environments, or VR, provide a fully three-dimensional 3D interface for both the display Ž . and control of interactive computer graphics 23 . <sup>w</sup> <sup>x</sup> Thus, the main idea behind VR systems is to give the user the feeling that they are immersed in a 3D world, populated by computer-generated objects. The most compelling illusions are achieved through the use of wide-field-of-view strereoscopic head-tracked display systems 24 . The use of VR for operator-<sup>w</sup> <sup>x</sup> training in power systems is described in Refs. <sup>w</sup> <sup>x</sup> 25,26 .

![](/api/attachments/GQTD983Q/fulltext/images/6982287bcd75aef08eb24e937b9d04fdff997f30ac596423a95fb3f372013245.jpg)  
Fig. 12. VR view of a 30-bus system.

For the results presented here, PowerWorld Simulator 27 was modified to allow 3D drawing and<sup>w</sup> <sup>x</sup> interaction using OpenGL. OpenGL itself is a software interface, originally developed by Silicon Graphics, for graphics hardware that facilitates the modeling of 3D systems 28 . Similar to Ref. 26 ,<sup>w x</sup> <sup>w x</sup> the PowerWorld Simulator implementation uses a regular PC-type display to provide a less ambitious, but quite compelling virtual world. The key to achieving a VR illusion is to provide the user with the ability to move about freely in three dimensions and to look in any desired direction.

As an example, Fig. 12 shows a one line for a 30-bus, except with the modification that the one line has been mapped into a 3D view and that bus AheightB and color is now proportional to the bus voltage magnitude. When the simulation is running, flows on the transmission lines are also animated. By moving about in this virtual world, the user begins to feel more as if he<sup>r</sup>she is within the one line, rather than just looking at it. This allows the potential to gain a much better intuitive appreciation for the relationship between different power system quantities, such as voltage magnitude and flows in this example.

![](/api/attachments/GQTD983Q/fulltext/images/f9d897aa3e0514906d01ab0e39ff45e4c8380ccb9639eb86e4e9994e9979af7f.jpg)  
Fig. 13. Relationship between actual area to area flows, and PTDF values.

The potential for VR systems to show relationships between the actual flow of power and the PTDF values is illustrated in Fig. 13. This example shows data for the 1998 ECAR case with the PTDF values calculated for a power transfer from Wisconsin to TVA. However, rather than showing individual line flow values, only the area-to-area values are shown. The actual area-to-area flows are shown in the XY plane, while the PTDF values have been added to the display as trajectory arcs between the different areas. The height of the arc is proportional to the PTDF value, with the movement of the spheres superimposed on the trajectories used to indicate the PTDF direction. For reference, in the figure, the observer location is in Northwest Missouri looking towards Lake Michigan.

VR systems can provide an extremely effective method for visualizing power system data. However, we conclude this section by noting that they are usually best for describing relationships qualitative relationships between different variables. For exact quantitative results, text-based displays can be better. Therefore, we recommend the use of the proposed visualization techniques to supplement, but certainly not replace, existing techniques.

## 9. Conclusion

This paper has provided an overview analysis of market power issues involved in analysis of networks, including the impact of congestion. Given the importance of the network structure in bulk power markets, the explicit consideration of both the physical and the operation constraints and the economic aspects of transmission services and generation markets is paramount to correctly assess market power in specific situations. The consideration of market concentration by itself is inadequate, in most cases, for the assessment of market power. As is clear from the various examples, the transmission network plays a pivotal role in the evaluation of potential market power situation. In fact, it is possible for players in various interconnected systems to exercise market power without a dominant position of market concentration.

## References

<sup>w x</sup>1 U.S. FERC, Order No. 592, RM96-6-000, Dec. 1996.

<sup>w</sup> <sup>x</sup> 2 U.S. Justice Department and Federal Trade Commission, Horizontal Merger Guidelines, April 1992, Revised April 1997, http:<sup>rr</sup>www.usdoj.gov<sup>r</sup>atr<sup>r</sup>public<sup>r</sup>guidelines.

<sup>w</sup> <sup>x</sup> 3 U.S. FERC, Notice of Proposed RuleMaking, RM98-4-000, April, 1998.

<sup>w</sup> <sup>x</sup> 4 Staff Report to the U.S. FERC on the Causes of Wholesale Electric Pricing Abnormalities in the Midwest during June 1998, Sept. 1998.

<sup>w</sup> <sup>x</sup> 5 G. Werden, Identifying market power in electric generation, Public Utilities Fortnightly 1996 19.Ž .

<sup>w</sup> <sup>x</sup> 6 M. Frankena, J. Morris, Why applicants should use computer simulation models to comply with FERC’s new merger policy, Public Utilities Fortnightly 1996 22–26.Ž .

<sup>w</sup> <sup>x</sup> 7 J.B. Cardell, C.C. Hitt, W.W. Hogan, Market power and strategic interaction in electricity networks, Resource and Energy Economics 19 1997 109–137.Ž .

<sup>w</sup> <sup>x</sup> 8 F.M. Scherer, Industrial Market Structure and Economic Performance, Rand McNally College Publishing, 1980.

<sup>w</sup> <sup>x</sup> 9 Special Issue on Transmission Pricing, Utilities Policy, Vol. 6, September 1997.

<sup>w</sup> <sup>x</sup>10 T.J. Overbye, G. Gross, M.J. Laufenberg, P.W. Sauer, Visualizing power system operations in the restructured environment, IEEE Computer Applications in Power 1997 53–58.Ž .

<sup>w</sup> <sup>x</sup> 11 G.L. Landgren, H.L. Terhune, R.K. Angel, Transmission interchange capability — analysis by computer, IEEE Transactions on Power Apparatus and Systems PAS-91 6 1972Ž . Ž . 2405–2414.

<sup>w</sup> <sup>x</sup> 12 G.L. Landgren, S.W. Anderson, Simultaneous power interchange capability analysis, IEEE Transactions on Power Apparatus and Systems PAS-92 6 1973 1973–1986.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 L.L. Garver, P.R. Van Horne, K.A. Wirgau, Load supplying capability of generation–transmission networks, IEEE Transactions on Power Apparatus and Systems PAS-98 3 1979Ž . Ž . 957–962.

<sup>w</sup> <sup>x</sup> 14 G.T. Heydt, B.M. Katz, A stochastic model in simultaneous interchange capacity calculations, IEEE Transactions on Power Apparatus and Systems PAS-94 2 1975 350–359.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 Union Electric, Simultaneous Transfer Capability: Direction for Software Development, EPRI Report EL-7351, Project 3140-1, EPRI, Palo Alto, CA, August 1991.

<sup>w</sup> <sup>x</sup> 16 L.R. Januzik, R.F. Paliza, R.P. Klump, C.M. Marzinzik, MAIN regional ATC calculation effect, Proceedings of the American Power Conference 1997 Chicago, IL.Ž .

<sup>w</sup> <sup>x</sup> 17 F.L. Alvarado, Market Power: A Dynamic Definition, Bulk Power Systems Dynamics and Control IV: Restructuring Conference, Santorini, Greece, 1998.

<sup>w</sup> <sup>x</sup> 18 J.D. Weber, T.J. Overbye, P.W. Sauer, Simulation of Electricity Markets with Player Bidding, Bulk Power Systems Dynamics and Control IV: Restructuring Conference, Santorini, Greece, 1998.

<sup>w</sup> <sup>x</sup> 19 A. Mas-Colell, M.D. Whinston, J.R. Green, Microeconomic Theory, Oxford Univ. Press, New York, NY, 1995.

<sup>w</sup> <sup>x</sup> 20 ECAR 1998 Fall Peak Input, Output, Data Dictionary ,Ž . http:<sup>rr</sup>www.ferc.fed.us<sup>r</sup>electric<sup>r</sup>F715.

<sup>w</sup> <sup>x</sup> 21 J.D. Weber, T.J. Overbye, Power system visualization through contour plots, Proceedings of the North American Power Symposium, Laramie, WY 1997 .Ž .

<sup>w</sup> <sup>x</sup> 22 T.J. Overbye, J.D. Weber, Visualization of large scale power systems,Proceedings of EPSOM ’98, Zurich, Switzerland, 1998.

<sup>w</sup> <sup>x</sup>23 S. Bryson, C. Levit, The virtual wind tunnel: an environment for the exploration of three-dimensional unsteady fluid flows,IEEE Visualization ’91, San Diego, CA, 1991.

<sup>w</sup> <sup>x</sup> 24 S. Bryson, Virtual reality in scientific visualization, Computers and Graphics 17 1993 679–685.Ž .

<sup>w</sup> <sup>x</sup> 25 A.O. Veh et al., Design and operation of a virtual reality operator-training system, IEEE Transactions on Power Systems 11 1996 1585–1591.Ž .

<sup>w</sup> <sup>x</sup> 26 E.K. Tam et al., A low-cost PC-oriented virtual environment for operator training,Proceedings of the 1997 PICA, 1997, pp. 358–364.

<sup>w</sup> <sup>x</sup> 27 htpp:<sup>rr</sup>www.powerworld.com.

<sup>w</sup> <sup>x</sup> 28 M. Woo, J. Neider, T. Davis, OpenGL Programming Guide, 2nd edn., Addison-Wesley Developers Press, Reading, MA, 1997.

## Biographies

Thomas J. Overbye received his BS, MS and PhD degrees in Electrical Engineering from the University of Wisconsin-Madison in 1983, 1988 and 1991, respectively. He was employed with Madison Gas and Electric from 1983 to 1991. He is currently an Associate Professor of Electrical and Computer Engineering at the University of Illinois at Urbana–Champaign. In 1993, he was the recipient of the IEEE PES Walter Fee Outstanding Young Engineer Award.

James D. Weber received his BS degree in Electrical Engineering from the University of Wisconsin-Platteville in 1995 and his MS degree in Electrical and Computer Engineering from the University of Illinois at Urbana–Champaign in 1997. He was a summer intern at Wisconsin Power and Light in 1994 and 1995. He is currently a graduate student in Electrical and Computer Engineering at the University of Illinois at Urbana–Champaign while working as a software developer for PowerWorld.

Kollin J. Patten received his BS and MS degrees in Electrical and Computer Engineering from the University of Illinois at Urbana– Champaign in 1997 and 1999, respectively. Since 1998, he has been employed with PowerWorld.
