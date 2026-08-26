---
otero_id: 21834
otero_key: "DTA28994"
title: "Dynamic behavior of differential pricing and quality of service options for the internet"
authors: "Peter C. Fishburn; Andrew M. Odlyzko"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00079-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Dynamic behavior of differential pricing and quality of service options for the internet

Peter C. Fishburn, Andrew M. Odlyzko

AT&T Labs — Research, 180 Park AÕenue, Florham Park, NJ 07932, USA

## Abstract

The simple model on which the Internet has operated, with all packets treated equally, and charges only for access links to the network, has contributed to its explosive growth. However, there is wide dissatisfaction with the delays and losses in current transmission. Further, new services, such as packet telephony, require assurance of considerably better service. These factors have stimulated the development of methods for providing Quality of Service QoS , and this will make the InternetŽ . more complicated. Differential quality will also force differential pricing, and this will further increase the complexity of the system.

The solution of simply putting in more capacity is widely regarded as impractical. However, it appears that we are about to enter a period of rapidly declining transmission costs. The implications of such an environment are explored by considering models with two types of demands for data transport, differing in sensitivity to congestion. Three network configurations are considered: 1 with separate networks for the two types of traffic, 2 with a single network that providesŽ . Ž . uniformly high QoS, and 3 with a single physical network that provides differential QoS. The best solution depends on theŽ . assumptions made about demand and technological progress. However, we show that the provision of uniformly high QoS to all traffic may well be best in the long run. Even when it is not the least expensive, the additional costs it imposes are usually not large. In a dynamic environment of rapid growth in traffic and decreasing prices, these costs may well be worth paying to attain the simplicity of a single network that treats all packets equally and has a simple charging mechanism. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Dynamic behavior; Premium pricing; Network utilization; Quality of service; Price-sensitive demand

## 1. Introduction

The Arpanet, which evolved into today’s Internet, was a research project that did not provide for any payment mechanisms and treated all packets on an equal ‘‘best-effort’’ basis. The Internet has with Ž minor exceptions inherited these properties. Packets. are basically still treated equally. Charging usually is only for the bandwidth of the connection to the Internet, and is independent of the amount of data sent and received See Ref. 11 , especially Ref. 10 , Ž <sup>w x</sup> <sup>w x</sup> for a survey of the economics of the Internet . These. features, which provide for extreme simplicity in both operation and economics, have contributed to the spectacular growth of the Internet.

Although there have been persistent criticisms about the lack of Quality of Service QoS provisionŽ . on the Internet, and about the charging scheme, thus far they have not been sufficiently convincing to modify the system. However, there are signs that change is imminent. Dissatisfaction with endemic congestion on the public Internet, which makes even Web surfing annoying, and the need to provide QoS for novel applications that are delay-sensitive, such as packet telephony and videoconferencing, are leading to demands for differential treatment of packets. Similar demands are coming from the corporate side. Private line networks use the same Internet protocol Ž . IP technology, are far larger in aggregate than the public Internet 3 , and have been providing high <sup>w</sup> <sup>x</sup> QoS largely through low utilization levels 13 . How-<sup>w</sup> <sup>x</sup> ever, with demand for bandwidth rising, corporate network managers are also demanding tools such as prioritization to ensure higher efficiency of network usage. Differential service quality will inevitably force introduction of more complicated pricing schemes than the present one, since it will be necessary to prevent all traffic from being sent on the highest quality level. The departure from the simple network operations and charging mechanisms of the Internet would represent at least a partial victory for the ‘‘Bell-heads’’ in the infamous controversy over networking 16 .<sup>w</sup> <sup>x</sup>

The ‘‘Net-head’’ approach to the problems of poor service has been to provide greater bandwidth and keep the charging algorithm simple. This solution is used universally in local area networks LANsŽ . and has worked for corporate and research networks in the past. The objection to the ‘‘Net-head’’ approach is that it is too expensive, at least for the public Internet, since more than 2 decades of experience have shown that any bandwidth gets saturated quickly.

Data transport is a serious constraint on Internet service providers ISPs , as it accounts for about halfŽ . of the total cost of long-haul networks. While new optical fiber technologies led to a dramatic drop in rates for leased lines in the 1980s and early 1990s, prices have been increasing recently as a consequence of scarcity of supply and rapidly growing demand see Refs. 3,15 for examples . NetworkŽ <sup>w</sup> <sup>x</sup> . operators have been lowering their cost per unit of bandwidth by moving to higher capacity lines see Ž Section 2 for data and discussion of this issue and. by signing long-term leases. In an environment of rising prices, differential QoS and more sophisticated pricing schemes appear essential to meet the explosive data transport needs at an affordable cost.

Do we have to give up on the simple operation and charging mechanisms of the current Internet? Both splitting of traffic into different QoS classes and complicated charging mechanisms impose heavy costs on developers of applications and network systems, and on network operators. Further factors in favor of simple fixed-fee charging mechanisms come from customer preferences even those of large cor-Ž porate customers , which often lead to higher rev- . enues for service providers who use such pricing approaches 5,6 . An early 1988 paper by Anania and <sup>w</sup> <sup>x</sup> Solomon 1 already presented several arguments for a simple flat-rate pricing approach to broadband networks.

Although simple flat-rate pricing with uniform best-effort data transport is attractive, it has many defects. It provides a single level of service quality, and does not allow users to select what is best for their needs. Economists, in general, oppose it on the grounds that it leads to misallocation of resources. For a fuller description of the arguments for abandoning the traditional Internet model, and for further references, see Ref. 11 for example. However, those <sup>w</sup> <sup>x</sup> arguments are based on experience with an environment that is likely to change drastically It is alreadyŽ an environment far removed from the traditional telecommunications world studied in Ref. 12 , for<sup>w</sup> <sup>x</sup> example, and will diverge from it even further . As. mentioned above, long distance data transport prices have been rising in the last few years. The basic fiber optic network that carries both voice and data traffic was designed primarily for voice, and until a few years ago, most of the bandwidth was devoted to voice. In revenues, the network is still dominated by voice. However, the bandwidth devoted to data is already comparable to that used for voice 3 , and data traffic is growing much more rapidly. Thus, we can expect that communications networks will grow rapidly and be increasingly dominated by data. Furthermore, wavelength division multiplexing WDMŽ . technology allows for expanding capacity without laying down more fiber at least not on long distanceŽ routes , which is a very expensive process, especially . when acquisition of rights-of-way is included. Within a few years, existing fiber will provide 100 or even 1000 times the bandwidth it did a couple of years ago, at a modest additional cost. The main determinants of network costs will be the electronics needed to provide WDM and switching. However, in electronics, ‘‘Moore’s Law’’ reigns, with performance increasing while prices drop. What this means is that we are likely to enter an era in which the price of bandwidth continues dropping dramatically for a decade or more. The question is, what will this mean for service providers and consumers?

It is instructive to consider microprocessors. Table 1 shows the last dozen years from the history of Intel. For each year, the microprocessor listed is the most powerful model introduced that year, with the price the one available at the end of that year AllŽ dollar figures are in nominal dollars, and the prices are for orders of 100 or 1000 chips at a time . The. processing power, in millions of instructions per second mips , is an imperfect measure of the com-Ž . puting power of processors. Still, it illustrates how the power of state-of-the-art microprocessors has been growing at an exponential rate, while their prices have remained about constant. At the same time, revenues and profits have increased. Over the period illustrated by Table 1, computing power has grown over 60% per year, with prices of the most powerful available processors rather stable, while Intel’s revenues have grown about 30% per year. A similar scenario appears to be realistic for high bandwidth communication networks in the next decade.

Intel and its microprocessors. For each year we list the most powerful general purpose microprocessors sold by Intel, its computing power, price at the end of the year in US\$ , and Intel’sŽ . revenues and profits for that year in millions US\$Ž .

<table><tr><td>Year</td><td>Processor</td><td>Mips</td><td>Price</td><td>Revenue</td><td>Net profit</td></tr><tr><td>1986</td><td>386 DX (16 MHz)</td><td>5</td><td>300</td><td>1265</td><td>-173</td></tr><tr><td>1987</td><td>386 DX (20 MHz)</td><td>6</td><td></td><td>1907</td><td>248</td></tr><tr><td>1988</td><td>386 DX (25 MHz)</td><td>8</td><td></td><td>2875</td><td>453</td></tr><tr><td>1989</td><td>486 DX (25 MHz)</td><td>20</td><td>950</td><td>3127</td><td>391</td></tr><tr><td>1990</td><td>486 DX (33 MHz)</td><td>27</td><td>950</td><td>3922</td><td>650</td></tr><tr><td>1991</td><td>486 DX (50 MHz)</td><td>41</td><td>644</td><td>4779</td><td>819</td></tr><tr><td>1992</td><td>DX2 (66 MHz)</td><td>54</td><td>600</td><td>5844</td><td>1067</td></tr><tr><td>1993</td><td>Pentium (66 MHz)</td><td>112</td><td>898</td><td>8782</td><td>2295</td></tr><tr><td>1994</td><td>Pentium (100 MHz)</td><td>166</td><td>935</td><td>11,521</td><td>2266</td></tr><tr><td>1995</td><td>Pentium Pro (200 MHz)</td><td>400</td><td>1325</td><td>16,202</td><td>3566</td></tr><tr><td>1996</td><td></td><td></td><td></td><td>20,847</td><td>5157</td></tr><tr><td>1997</td><td>Pentium II (300 MHz)</td><td>600</td><td>735</td><td>25,070</td><td>8945</td></tr></table>

What we explore are the implications of this kind of environment for the provision of QoS on the Internet. If available capacity doubles each year, or every 2 yr, while total costs increase much more slowly, so that the price per unit of bandwidth decreases rapidly, it might make sense to provide a uniformly high QoS for everybody and avoid the complexities of the schemes that are being considered.

Existing work on QoS, surveyed in Ref. 4 , does<sup>w</sup> <sup>x</sup> not contain any projections of the degree to which the different proposals for providing QoS will lower network utilization. The relation between utilization of network capacity and perceived quality of service is a complex one. It is possible to have a lightly utilized network that delivers horrible service, but in general, the lower the utilization rate, the better the service. Further, many networks, such as corporate Intranets, are already providing QoS largely through low utilization rates 13 . High-quality experimental <sup>w</sup> <sup>x</sup> networks, such as vBNS, also have very low utilizations. These networks are still operated on the ‘‘best-effort’’ basis, with no explicit guarantees butŽ with sophisticated traffic engineering tools . Conges-. tion episodes are infrequent enough for this to be acceptable. In general, no matter how a network is engineered, lowering the traffic load on it will result in better service. The routers and switches are already fast enough, that if congestion does not cause buffers to fill up, the quality is sufficient for all anticipated demands.

In this work, we will assume, as a first approximation, that improved QoS is associated directly with low utilization levels. Although schemes like those in Ref. 4 can increase the efficiency of the<sup>w</sup> <sup>x</sup> network, whether it has just a single best-effort service, or several classes of service, it is hard to incorporate them into an economic model until more is known about their performance.

To explore potential futures for QoS on the Internet with and without differential pricing, we will assume two types of demands in our models. One is for transport that is delay insensitive, such as many bulk file transfers or even e-mail. The other is for transport of information that is sensitive to delay, such as packet telephony, or even some Web browsing In effect, we will thus be considering Class ofŽ Service models for the Internet, and not the more involved QoS ones . We refer to delay insensitive .

demand, or to its users, as type A, and to delay sensitive demand, or its users, as type B.

Within a given time period, each type has a potential volume or potential demand, which is the total Internet transfer volume the type would use if the transfer charge or price were essentially zero. We denote their potential volumes by $V _ { \mathrm { A } }$ and $V _ { \mathrm { { B } } }$ , or simply by V as a general designation.

We will vary the ratio of $V _ { \mathrm { A } }$ and $V _ { \mathrm { { B } } }$ , but only within a narrow range, near equality. The justification for this is that in current data networks, the volumes of data sent over the congested public Internet and over the uncongested private line networks are comparable. If $V _ { \mathrm { { A } } }$ were much larger than $V _ { \mathrm { { B } } }$ then clearly it would be best to send all data over an uncongested network designed for type A traffic. On the other hand, if $V _ { \mathrm { { B } } }$ were much larger than $V _ { \mathrm { { A } } }$ , the case for a separated network or a two-tiered network would be much stronger.

Because real use will be price-sensitive, the actual volume carried for a user type during the period is modeled by $P ( x ) V ,$ where x is the price per unit of volume and $P ( x )$ is the probability that a potential user will subscribe to the service at price x. We refer to P as the demand function and assume that $P ( 0 )$ $= 1$ , and that $P ( x )$ decreases toward 0 as x increases. An approximate but revealing measure of customer satisfaction is the demand satisfaction expressed as the percent of potential volume that customers subscribe to during the period, i.e., $1 0 0 P ( x )$ This should not be confused with the utilization of available network capacity since, for example, a channel that carries priority data may have a high demand satisfaction yet provide very good QoS because its transport capacity substantially exceeds the priority demands. Several forms will be considered for P to account for the possibility that our conclusions may depend on assumptions about the demand function.

Three network configurations are examined for provision of service to types A and B, as follows:

1. physically separate networks are used for each of A and B, with each network having its own cost, QoS, and price characteristics;

2. a single network is used for both A and B, with one price for all users that is constructed to provide the high QoS desired by B;

3. a single network is used for A and B, but the types are logically separated by a software that differentiates between them and allows different QoS and prices for the two.

We refer to 1 as the separated network, to 2 asŽ . Ž . the one-price network, and to 3 as the two-tiered Ž . network. We assume for 3 that the types use logi- Ž . cally separated channels and ignore techniques, such as those in Ref. 4 , that can lead to greater efficien- <sup>w</sup> <sup>x</sup> cies, as when low-priority traffic is used to fill gaps in high-priority traffic. We also ignore the large increases in utilization rates that can be gained by exploiting different time-of-day patterns of use Žwhich are discussed in detail in Ref. 14 . The main<sup>w</sup> <sup>x</sup>. conclusion of our models is that factors of two in price or utilization do not matter much in an environment of increasing demand and falling prices.

The advantage of 3 over 1 is that the unifiedŽ . Ž . network can take advantage of economies of scale. We will not consider the added costs of providing for logical separation of the two traffic types on a two-tiered network.

As shown in Ref. 13 , current data networks are<sup>w</sup> <sup>x</sup> an inefficient amalgam of the separated network and the one-price network. They do resemble a separated network, with the public Internet operating in a congested mode with relatively high utilization rate Žalthough lower than that of the switched voice network , while corporate networks have very low. utilization rates. However, this is not the separated network of our model, since all corporate data, whether it is sensitive to delay or not, travels over underutilized networks, while all public Internet traffic goes over congested links. Thus, we have two separate one-price networks.

The economic models used to determine prices for the three configurations we study are based on providers’ costs and revenues. Costs include ongoing operational costs, depreciation and other overhead charges, and a reasonable rate of return or profit that might be limited by competition or regulatory constraints. We assume for each period that total cost is a function of actual volume carried, as described in Section 2.

Per-period revenue equals price times actual volume, i.e.,

Revenue<sup>s</sup>xP x V Ž . .

We then compute the actual price charged as the smallest x at which revenue equals cost. In doing this, we are not trying to maximize profit because it is already built into costs; we seek only to determine a reasonable price based on equality between costs and revenues. If no value of x satisfies the Revenue <sup>s</sup>Cost equation, then revenue is insufficient to cover cost at any price, and we refer to the configuration as infeasible. Although our models are based on equilibrium between revenue and cost rather than optimization schemes per se, we will compare prices, demand satisfactions, and revenues of the three network configurations to assess their performances with respect to each other.

We regard our models as informative but very rough approximations to an extremely complex environment and uncertain future. Explanations of aspects of cost, including economies of scale, effects on cost of enhanced QoS, and how costs may change over time in a competitive marketplace with rapidly increasing volume are described in Section 2. Section 3 specifies the models more completely for the three network configurations in a static one-period scenario and describes solution procedures. Section 4 then extends the models to the dynamic scenario of a succession of periods in which potential volumes, costs, and implied prices change from period to period.

For computational simplicity in the dynamic analysis, we will assume that potential volume doubles from period to period. This assumption is made palatable by not fixing period lengths in advance. For example, 2-yr periods might be assumed. See Ref. 3 for history and projections of growth pat-<sup>w</sup> <sup>x</sup> terns in data traffic. While voice traffic has been growing at around 10% per year, Internet traffic Ž . measured in bytes has been just about doubling each year in the 1990s, with the exception of 1995 and 1996, when it grew by factors of about 10 in each of those 2 years.

We have already mentioned that different market demand functions will be considered. A further accommodation for an uncertain future will be made by considering two very different patterns for changes in costs over time. The first is a conventional pattern in which costs change only because of the potential volume doubling from period to period. The second, which we refer to as the dynamic pattern, reflects not only the doubling assumption but also cost reductions driven by competition and technological advances. Dynamic-pattern revenues increase from period to period except in one extreme scenario whereŽ they remain constant , but at a much slower rate than. conventional-pattern costs. Both patterns are specified more completely in Section 2.

As we will see in Section 4, the implications of our dynamic models depend on our different demand functions and cost patterns, but some trends emerge. For example, in comparisons between the separated network and two-tiered network, the prices for both A ordinary service and B premium service tend toŽ . Ž . be slightly higher for the separated network, whereas demand satisfactions are comparable. An anticipated finding is that dynamic-pattern costs drive prices substantially below those for conventional-pattern costs in all three networks. Another result that was not anticipated at the outset, is that the one-price network with its uniformly high QoS is competitive with the others under several assumptions. In regard to revenues Ž . <sup>s</sup>costs , which are aggregated for A and B in the separated network, the highest revenues occur for either the separated network or the one-price network, whereas the lowest revenues occur for either the one-price network or the two-tiered network. The differences in the revenue picture are caused more by the different cost patterns than by the different demand functions. A more complete picture of these matters is given at the end of Section 4. The main conclusions, though, are that differences between the different networks are not great.

How can the one-price network be superior to the separated one? We show this with an example that simplifies our model by ignoring effects of price on demand. Suppose that type A and type B traffic are the same when measured in bytes, but that type B transmission requires much less congested networks, with a capacity four times as large as that for type A. Suppose also that the cost of a network of bandwidth x is $x ^ { 1 / 2 }$ ŽSection 2 discusses cost formulas in detail . Then, the cost of the separated network is 3 . $( = 1 + 4 ^ { 1 / 2 } )$ , whereas that of the one-price network is $8 ^ { 1 / 2 } = 2 . 8 2 8 4$ , as the capacity has to be eight times that of just the A network. Thus in this scenario, providing uniformly high QoS to everybody saves 6% of the cost. A much larger savings come from having a single network, which makes life simpler for customers. On the other hand, there are also costs. For example, if there is no way to charge different prices for A and B traffic on a single network as we will be assuming throughout theŽ paper , then, type A users will pay 1.4142 half of. Ž total cost instead of 1.0 for their own separate. network, whereas type B users would see their charges drop from 2 to 1.4142. Thus, different types of networks have varying impacts on social welfare. However, we argue that in the long run such costs might be bearable in the interests of simplicity. The reason is that rapidly decreasing costs of data transport mean everyone is as well off within one or two time periods as they would be with any other network solution.

The temporal aspects of technological change have a large impact on the marketplace. For example, for a long time, Intel microprocessors were slower, usually by at least a factor of 2, than comparably priced RISC chips. However, Intel was usually able to provide comparable price<sup>r</sup>performance ratio within 2 or 3 yr. This, combined with the advantages of compatibility i.e., lower costs to customers in up- Ž grading allowed Intel to increase its dominance in . the processor business. Similar effects might favor simple schemes such as the one-price network over Ž . more efficient and socially optimal ones in data networks.

A summary of our study is provided in Section 5.

## 2. Economies of scale and other cost factors

Forecasting prices of telecommunications services has been a risky enterprise in recent decades. In switched voice services, there have been steady reductions in prices over the last century. On the other hand, in data services, the recent record is much more erratic. As an example, we cite Ref. 8 . Writ-<sup>w</sup> <sup>x</sup> ten in 1992 and published in 1993, it develops two models for leased line prices in the United States. Both models predicted a drop in prices of about 50% by 1998. Instead, prices have increased by approximately 50% since 1992, so they are about three times as high as predicted by Irvin’s model. However, we feel that this was an anomaly, caused by an unexpectedly high demand for data network bandwidth and little new growth in supply. At some point in the future, prices are likely to resume their decline.

There is no simple formula for costs of communication networks. It is almost always true that larger transfer volume or bandwidth purchases are less expensive per unit of volume or bandwidth than smaller ones, but even that is not always the case. For example, in April 1998, UUNet 17 was citing<sup>w</sup> <sup>x</sup> the following prices for dedicated Internet connections not including the cost of local connections toŽ the nearest UUNet site :.

Speed Price per month 56 kbps US\$595 1.5 Mbps T1Ž . US\$1795 45 Mbps T3Ž . US\$54,000

In this case, a 24-fold increase in bandwidth from a 56 kbps line to a T1 incurs only a three-fold increase in price, but the 28-fold increase in speed from a T1 to a T3 raises the cost by a factor of 30. This pricing may reflect scarcity of high-capacity lines, and possibly of handling the traffic from a T3 connection on a network that consists largely of T3 links. Similar linear pricing in bandwidth applies to speeds between T3 and OC3 Sprint charges for these threeŽ speeds are US\$897, US\$2062 and US\$20,620, respectively, according to data in Ref. 2 , but these<sup>w</sup> <sup>x</sup> figures may not be strictly comparable to UUNet’s because of special conditions and features ..

A better view of transmission costs might be offered by examining leased line prices. In April 1998, the tariffed monthly rates for an approximately 300 air mile private line, with about 5 miles of local connections that are leased from a local phone company were about, as shown in Table 2 In practice, Ž long-term leases and bulk purchase discounts might reduce these costs by up to 50%, see Ref. 9 for<sup>w</sup> <sup>x</sup> example. It is worth noting that the local access connections account for about 60% of the cost of a 9.6 or 56 kbps line and about 17% of a T1 or a T3 .. The exact figures depend on distance 9 , but this<sup>w</sup> <sup>x</sup> dependence has decreased greatly over time 3 .<sup>w</sup> <sup>x</sup>

Table 2

<table><tr><td>Speed</td><td>Price per month (US$)</td></tr><tr><td>9.6 kbps</td><td>1150</td></tr><tr><td>56 kbps</td><td>1300</td></tr><tr><td>128 kbps</td><td>3000</td></tr><tr><td>256 kbps</td><td>3800</td></tr><tr><td>512 kbps</td><td>5100</td></tr><tr><td>1.5 Mbps (T1)</td><td>7000</td></tr><tr><td>7.7 Mbps</td><td>37,000</td></tr><tr><td>45 Mbps (T3)</td><td>66,000</td></tr></table>

Using the leased line prices cited above, we can see that a moderately good fit for the cost of carrying a given volume is one time period at the most common speeds between 56 and 45 Mbps is obtained by making the cost proportional to the volume, raised to a power in the range of 0.5 to 0.7, that we denote by $s ,$ and refer to as the economy-of-scale parameter In the general economics literature,Ž $1 / s$ is known as the elasticity of scale, and we are assuming it is constant . Economies of scale can. arise from reduced requirements for the multiplexing equipment needed to provide low speed links on a high-capacity network as well as lower costs of sales, administration, maintenance, and related operational costs. It is reasonable to suppose that the same s value will apply in the future for greater volumes. Although later examples assume a value of $s = 2 / 3$ , we write our cost formulas for general s ŽFor comparison, Ref. 7 uses a value of<sup>w</sup> <sup>x</sup> $s = 1 / 2 )$ Today, $s = 2 / 3$ applies only through T3 speeds, and charges for OC3 155 Mbps private lines are report-Ž . edly often higher than for equivalent capacity in T3 lines. However, as traffic grows, and new technologies are deployed, it is reasonable to expect that our cost formula will apply at higher bandwidths as well.

A value of $s = 2 / 3$ also fits well with the historical record of prices of long distance phone calls 8 .<sup>w</sup> <sup>x</sup> In that case, though, it reflects technological progress Ž . the learning curve , and not economies of scale.

In particular, we will assume that the cost for demand type $\mathbf { A }$ in a period with potential volume $V _ { \mathrm { { A } } }$ and demand probability $P ( x )$ at price x is given by Cost for A <sup>s</sup> P x V Ž . .

This applies to the separated network, where costs are scaled in units determined for the separated A case. Using the same scale, we assume that the cost for demand type B under similar conditions is

$$
\text { Cost   for   B } = \left[ \psi P (x) V _ {\mathrm{B}} \right] ^ {s},
$$

where $\psi ,$ , which we refer to as the premium factor, is a parameter that exceeds 1 to account for higher cost and enhanced QoS for type B users. Reasonable values for $\psi$ might lie in the range of 2 to 4, judging by the comparison of different networks in Ref. 13 .<sup>w</sup> <sup>x</sup> For example, if $\psi = 2 ,$ , then, the B part of the separated network is arranged to carry the same volume as the $\mathbf { A }$ part at twice the capacity. Singleperiod costs for one-price and two-tiered networks have related forms that are described in Section 3.

The preceding costs apply to an initial period, which can be taken to be the present or some other base period. The conventional pattern for costs, in which costs change from period to period only as a function of the doubling of potential volume, implies that costs t periods in the future from the base period will be

$$
\left[ P (x) 2 ^ {t} V _ {\mathrm{A}} \right] ^ {s} = \left[ P (x) V _ {\mathrm{A}} \right] ^ {s} 2 ^ {t s} \quad \text { for   A }
$$

and

$$
\left[ \psi P (x) 2 ^ {t} V _ {\mathrm{B}} \right] ^ {s} = \left[ \psi P (x) V _ {\mathrm{B}} \right] ^ {s} 2 ^ {t s} \quad \text { for   B }
$$

in the separated network.

However, competition and technological advances along with rising demand may lead to substantially lower costs than those given by the conventional pattern. Among other things, developments in WDM mean that fiber capacity is not a limiting factor. Instead, the electronics that connect end users to the fiber are becoming the main obstacle, and improvements in optical and silicon technology are likely to induce rapid decreases in the price<sup>r</sup>performance ratio. Although prices of connections of a fixed speed might not drop dramatically, the bulk of the data transport capacity that is purchased is likely to cost far less per unit of volume than at present That isŽ the pattern seen in prices of microprocessors and DRAMs . We model such effects in our dynamic. pattern for costs by dividing the conventional next period cost by $\sqrt { 2 }$ , a factor that accumulates exponentially over time. For example, the present cost of $[ P ( x ) V _ { \mathrm { A } } ] ^ { s }$ for $\mathbf { A }$ in the separated network translates into the dynamic-pattern cost of

$$
\left[ P (x) 2 ^ {t} V _ {\mathrm{A}} \right] ^ {s} 2 ^ {- t / 2} = \left[ P (x) V _ {\mathrm{A}} \right] ^ {s} 2 ^ {t (s - 1 / 2)}
$$

t periods in the future, which is substantially less than the figure of $[ P ( x ) V _ { \mathrm { A } } ] ^ { s } 2 ^ { t s }$ for the conventional pattern. We regard $\sqrt { 2 }$ as a fairly drastic dynamic factor, representing an extreme case for unit cost reduction. For example, if $s = 1 / 2 ,$ , then total cost remains the same as potential volume doubles.

Because period lengths are flexible, we allow for varying rates of decrease in unit cost as time progresses. If period length is 1 yr and $s = 2 / 3$ , the conventional pattern presumes a yearly decrease of about 20% in unit cost, and the dynamic pattern presumes a yearly decrease of about 44% in unit cost. If period length is 2 yr and $s = 2 / 3$ , the yearly unit cost decreases are 10% for the conventional pattern and 22% for the dynamic pattern.

## 3. One-period static analysis

This section discusses our models for a fixed period in which A has potential volume $V _ { \mathrm { A } }$ , B has potential volume $V _ { \mathrm { { B } } }$ , and both have demand function P. As before,  is the premium factor for higher QoS, and $s < 1$ is the economy-of-scale parameter. The example later in this section takes $V _ { \mathrm { A } } = V _ { \mathrm { B } }$ $\psi = 3$ and $s = 2 / 3$ . Section 4 considers other arrangements for $V _ { \mathrm { A } } , V _ { \mathrm { B } } , \psi$ and s.

Let x, y, and z denote the prices for type A in the separated network, for type B in the separated network, and for both types in the one-price network, respectively. The costs for these networks are as follows:

separated: A cos $: = \left[ P ( \ v { x } ) V _ { \mathrm { A } } \right] ^ { s }$

B cost $= \left[ { \psi } P ( \boldsymbol { y } ) V _ { \mathrm { { B } } } \right] ^ { s }$

Total $= \left[ P ( \ v x ) V _ { \mathrm { A } } \right] ^ { s } + \left[ \psi P ( \ v y ) V _ { \mathrm { B } } \right] ^ { s }$

$$
\begin{array}{r l} \text { one - price:   Cost } & = \left\{\psi \left[ P (z) V _ {\mathrm{A}} + P (z) V _ {\mathrm{B}} \right] \right\} ^ {s} \\ & = \left[ \psi P (z) \right] ^ {s} \left(V _ {\mathrm{A}} + V _ {\mathrm{B}}\right) ^ {s}. \end{array}
$$

For one-price, applies to both A and B because this network offers the premium service to both types.

The Revenue<sup>s</sup>Cost equations for the preceding networks are

$$
x P (x) V _ {\mathrm{A}} = \left[ P (x) V _ {\mathrm{A}} \right] ^ {s}
$$

$$
y P (y) V _ {\mathrm{B}} = \left[ \psi P (y) V _ {\mathrm{B}} \right] ^ {s}
$$

and

$$
z P (z) \left(V _ {\mathrm{A}} + V _ {\mathrm{B}}\right) = \left[ \psi P (z) \left(V _ {\mathrm{A}} + V _ {\mathrm{B}}\right) \right] ^ {s}.
$$

In the first equation, $x P ( x )$ for the forms we use for P increases to a maximum and then decreases for larger x, whereas $P ( x ) ^ { s }$ on the right side decreases from 1 at $x = 0 .$ , and approaches 0 as x gets large. If the single-peaked curve for $x P ( x ) V _ { \mathrm { A } }$ lies beneath the decreasing curve for $[ P ( x ) V _ { \mathrm { A } } ] ^ { s } ,$ , i.e., if $x P ( x ) V _ { \mathrm { A } }$ $< [ P ( x ) V _ { \mathrm { A } } ] ^ { s }$ for all $x \ge 0$ , then the A part of the separated network is infeasible. Otherwise, there will typically be two x values, say $x _ { 1 } < x _ { 2 }$ , where the curves cross. We take $x _ { 1 }$ as our price solution to $x P ( x ) V _ { \mathrm { A } } = [ P ( x ) V _ { \mathrm { A } } ] ^ { s }$ because it gives a lower price, higher revenue, and greater utilization than $x _ { 2 }$ . Similar remarks apply to the other Revenue<sup>s</sup>Cost equations.

We introduce a new parameter for the two-tiered network. It is the ratio $\lambda \geq 1$ of the higher to the lower price in this network, i.e., $\lambda = y / x$ when y is the premium price and x is the ordinary price. When is not made explicit, the two-tiered Revenue<sup>s</sup>Cost equation is

$$
x P (x) V _ {\mathrm{A}} + y P (y) V _ {\mathrm{B}} = \left[ P (x) V _ {\mathrm{A}} + \psi P (y) V _ {\mathrm{B}} \right] ^ {s}.
$$

Unlike the one-price case, applies here only to the premium service because of the two-tiered structure. In keeping with the rationale of a two-tiered network, we regard this network as feasible only if the preceding equation holds for some $\left( { x , y } \right)$ with $y \geq x$ We note also that costs could be increased slightly for the two-tiered network because of the additional costs of network operators, as well as those of users, who have to adjust to a more complicated pricing scheme. However, we do not believe that this matters very much since the models are approximate in the first place.

A feasible two-tiered network offers more freedom of choice than the others because it typically has a continuum of $\left( x , y \right)$ solutions to the Revenue <sup>s</sup>Cost equation in which y increases as x decreases in moving away from the equal-prices solution, where $x = y$ . We have found that two-tiered revenue is often greatest when x and y are close together, but note also that $x = y$ defeats the purpose of a two-tiered network. We shall therefore regard $\lambda = y / x$ as a control variable subject to policy decision. Reasonable values for range from about 2 to 4, so that the premium service costs about two to four times as much as the ordinary service per unit volume. Our use of also eases the computational burden of solving the Revenue<sup>s</sup>Cost equation since, when is given, we need only solve for x, and then obtain y from $y = \lambda x .$

Table 3  
![](/api/attachments/DTA28994/fulltext/images/9ede3c314d1b5ed5357b2f6515929a76dc68e6dd8e8dafdf8f76a63f1672a77c.jpg)  
Fig. 1. Three demand functions.

When  x is substituted for y in the preceding two-tiered equation, it becomes

$$
\begin{array}{c} x \big [ P (x) V _ {\mathrm{A}} + \lambda P (\lambda x) V _ {\mathrm{B}} \big ] \\ = \big [ P (x) V _ {\mathrm{A}} + \psi P (\lambda x) V _ {\mathrm{B}} \big ] ^ {s}. \end{array}
$$

As for the other networks, the solution is taken as the smallest x that satisfies the equation when it is feasible.

We consider three forms for the demand function P in the example that follows. They are

$$
P _ {1} (x) = e ^ {- x ^ {2}} \quad \text { for } x \geq 0,
$$

$$
P _ {2} (x) = \frac {e ^ {- x}}{1 + x} \quad \text { for } x \geq 0,
$$

$$
P _ {3} (x) = \frac {1}{1 + x ^ {4}} \quad \text { for } x \geq 0,
$$

Fig. 1 illustrates the differences among the three. $P _ { 1 }$ and $P _ { 3 }$ begin high for small x, decrease rapidly as x gets into a mid-range, and have very narrow tails. $P _ { 2 }$ begins its descent immediately, levels off sooner than $P _ { 1 }$ and $P _ { 3 }$ and has a fat tail. When prices are low, $P _ { 2 }$ is much more sensitive than the others to small price changes. This is the most important difference between them because most of the solutions we have seen for our networks have prices well below 1.

We now turn to an example with parameter values $\psi = 3 , s = 2 / 3 ,$ , and $\lambda \in \{ 2 , 4 \}$ . The example has six scenarios in the two-by-three cross classification low potential volume, high potential volume4 $\times \{ P _ { 1 } , P _ { 2 }$ $P _ { 3 } \}$ . With $V _ { \mathrm { A } } = V _ { \mathrm { B } }$ , we set the low potential volume for each of A and B at $V _ { 1 } = 3 2$ , and set the high potential volume at $V _ { 2 } = 6 4 V _ { 1 }$

We consider the separated and one-price networks first. The Revenue<sup>s</sup>Cost equations for A separate, B separate, and the one-price network are, for $V = V _ { 1 }$

$$
\begin{array}{l} x P (x) V _ {1} = \left[ P (x) V _ {1} \right] ^ {2 / 3} \\ x P (x) V _ {1} = \left[ 3 P (x) V _ {1} \right] ^ {2 / 3} \\ x P (x) (2 V _ {1}) = \left[ 3 P (x) (2 V _ {1}) \right] ^ {2 / 3}, \end{array}
$$

Prices, demand satisfactions, and revenues for separated and one-price networks

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">A separate</td><td colspan="3">B separate</td><td colspan="2">Separated network totals</td><td colspan="3">One-price networks</td></tr><tr><td>x</td><td>S</td><td>R</td><td>x</td><td>S</td><td>R</td><td>S</td><td>R</td><td>x</td><td>S</td><td>R</td></tr><tr><td rowspan="3"> $V_1$  (Low)</td><td> $P_1$ </td><td>0.33</td><td>90</td><td>9.4</td><td>0.82</td><td>51</td><td>13.4</td><td>71</td><td>22.8</td><td>0.58</td><td>71</td><td>26.6</td></tr><tr><td> $P_2$ </td><td>0.40</td><td>48</td><td>6.1</td><td>1.4</td><td>10</td><td>4.6</td><td>29</td><td>10.7</td><td>0.85</td><td>23</td><td>12.6</td></tr><tr><td> $P_3$ </td><td>0.32</td><td>99</td><td>10.0</td><td>0.71</td><td>80</td><td>18.1</td><td>90</td><td>28.1</td><td>0.53</td><td>93</td><td>31.6</td></tr><tr><td rowspan="3"> $V_2$  (High)</td><td> $P_1$ </td><td>0.079</td><td>99</td><td>160</td><td>0.17</td><td>97</td><td>331</td><td>98</td><td>491</td><td>0.13</td><td>98</td><td>527</td></tr><tr><td> $P_2$ </td><td>0.084</td><td>85</td><td>146</td><td>0.18</td><td>70</td><td>266</td><td>78</td><td>412</td><td>0.14</td><td>76</td><td>444</td></tr><tr><td> $P_3$ </td><td>0.079</td><td>100</td><td>162</td><td>0.16</td><td>100</td><td>336</td><td>100</td><td>498</td><td>0.13</td><td>100</td><td>536</td></tr></table>

respectively. These simplify to

$$
\left. \begin{array}{l} P _ {1}: x ^ {3} e ^ {- x ^ {2}} \\ P _ {2}: x ^ {3} e ^ {- x} / (1 + x) \\ P _ {3}: x ^ {3} / (1 + x ^ {4}) \end{array} \right\} = \left\{ \begin{array}{l l} 1 / 3 2 & \text { A   separate } \\ 9 / 3 2 & \text { B   separate } \\ 9 / 6 4 & \text { one - price }. \end{array} \right.
$$

The right-hand sides of these equations are multiplied by $1 / 6 4$ to obtain the corresponding equations for $V _ { 2 } .$ .

Table 3 shows approximate solution values in terms of price x, demand satisfaction S and revenue R. The one-price network price in each row is midway between the prices for A and B in the separated network, $P _ { 2 }$ induces slightly higher prices than $P _ { 1 }$ and $P _ { 3 } ,$ and prices drop dramatically with high volume. The ratios of premium service to ordinary service prices for the separated network lie between 2 and 3.5.

In all cases, demand satisfaction is substantially higher for $P _ { 1 }$ and $P _ { 3 } { \mathrm { : } }$ , than $P _ { 2 }$ , and aggregated demand satisfaction for the separated network is about the same as one-price satisfaction.

Revenues are obviously higher for the high vol ume cases, but the high-to-low ratios are smaller than the 64-fold increase in volume because of economies of scale. Moreover, because $P _ { 3 }$ implies greater propensity to subscribe than $P _ { 2 }$ , and $P _ { 1 }$ implies greater propensity to subscribe than $P _ { 2 }$ for all prices in the table, revenues run highest for $P _ { 3 } ,$ next highest for $P _ { 1 }$ and lowest for $P _ { 2 } .$ . There is significantly less difference proportionately between revenues at high volume than at low volume.

We now bring the two-tiered network into the picture with x the cheaper two-tiered price and $y = \lambda x$ the premium service price. The Revenue<sup>s</sup> Cost equation noted earlier for the two-tiered network reduces to

$$
\begin{array}{l} \frac {x e ^ {- x ^ {2}} + \lambda x e ^ {- (\lambda x) ^ {2}}}{[ e ^ {- x ^ {2}} + 3 e ^ {- (\lambda x) ^ {2}} ] ^ {2 / 3}} = \frac {1}{(3 2) ^ {1 / 3}} \quad \text { for } \quad P = P _ {1}, \\ V = V _ {1}. \\ \frac {x e ^ {- x} / (1 + x) + \lambda x e ^ {- \lambda x} / (1 + \lambda x)}{[ e ^ {- x} / (1 + x) + 3 e ^ {- \lambda x} / (1 + \lambda x) ] ^ {2 / 3}} \\ = \frac {1}{(3 2) ^ {1 / 3}} \quad \text { for } \quad P = P _ {2}, \quad V = V _ {1}. \\ \frac {x / (1 + x ^ {4}) + \lambda x / (1 + (\lambda x) ^ {4})}{[ 1 / (1 + x ^ {4}) + 3 / (1 + (\lambda x) ^ {4}) ] ^ {2 / 3}} \\ = \frac {1}{(3 2) ^ {1 / 3}} \quad \text { for } \quad P = P _ {3}, \quad V = V _ {1}. \end{array}
$$

The right sides of these are multiplied by $1 / ( 6 4 ) ^ { 1 / 3 }$ $= 1 / 4 \mathrm { ~ f o r ~ } V _ { 2 }$

Table 4 shows the two-tiered results to the right of the one-price results. Comparisons between $\lambda = 2$ and <sup>s</sup>4 for the two-tiered case reveal little difference in demand satisfaction or revenue. In each row, the two prices for <sup>s</sup>4 e.g., 0.18 andŽ $4 \times 0 . 1 8 =$ 0.72 surround the prices for. Ž <sup>s</sup>2 e.g., 0.28 and $2 \times 0 . 2 8 = 0 . 5 6 )$ . Without exception, the one-price network price is greater than the average of the two two-tiered prices for a given category $( V _ { i } , \ P _ { j } ,$ . , , and can be greater than the larger of these two as for $\lambda = 2$ in rows 1 and 2. Finally, the one-price network has uniformly higher revenue and lower demand satisfaction than the two-tiered network.

Table 4  
Prices, demand satisfactions, and revenues for one-price and two-tiered networks

<table><tr><td rowspan="3" colspan="2"></td><td colspan="3">One-price network</td><td colspan="6">Two-tiered network</td></tr><tr><td rowspan="2">x</td><td rowspan="2">S</td><td rowspan="2">R</td><td colspan="3">λ = 2</td><td colspan="3">λ = 4</td></tr><tr><td>x</td><td>S</td><td>R</td><td>x</td><td>S</td><td>R</td></tr><tr><td rowspan="3"> $V_1$  (Low)</td><td> $P_1$ </td><td>0.58</td><td>71</td><td>26.6</td><td>0.28</td><td>83</td><td>21.8</td><td>0.18</td><td>78</td><td>19.2</td></tr><tr><td> $P_2$ </td><td>0.85</td><td>23</td><td>12.6</td><td>0.36</td><td>40</td><td>12.5</td><td>0.28</td><td>37</td><td>10.9</td></tr><tr><td> $P_3$ </td><td>0.53</td><td>93</td><td>31.6</td><td>0.27</td><td>96</td><td>24.4</td><td>0.17</td><td>92</td><td>23.2</td></tr><tr><td rowspan="3"> $V_2$  (High)</td><td> $P_1$ </td><td>0.13</td><td>98</td><td>527</td><td>0.065</td><td>99</td><td>397</td><td>0.040</td><td>99</td><td>400</td></tr><tr><td> $P_2$ </td><td>0.14</td><td>76</td><td>444</td><td>0.071</td><td>82</td><td>349</td><td>0.044</td><td>82</td><td>339</td></tr><tr><td> $P_3$ </td><td>0.13</td><td>100</td><td>536</td><td>0.066</td><td>100</td><td>407</td><td>0.040</td><td>100</td><td>406</td></tr></table>

## 4. Dynamic analysis

We present results of our dynamic analysis primarily for the separated and one-price networks to keep matters fairly simple. The results for the twotiered network in the dynamic case are similar to those in Section 3 in comparison to the other networks, and their trends over time are similar to the trends described in this section. For example, for an array of parameters, <sup>s</sup>2 and <sup>s</sup>4 have very similar demand satisfactions and revenues although their prices, x and x, obviously differ. The cheaper two-tier price at <sup>s</sup>4 is about 60% of the cheaper price at <sup>s</sup> 2, so the premium price at <sup>s</sup> 4 is about 20% higher than the premium price at <sup>s</sup>2. Revenue comparisons show a general pattern in which a two-tiered network either has the lowest revenue or the middle revenue of the three networks.

For the separated and one-price networks, we begin our dynamic process at period t<sup>s</sup>0 with low potential volumes, and run each network through 11 periods. In our initial runs, which are partly shown in Tables 5–8, we took $V _ { \mathrm { A } } = V _ { \mathrm { B } }$ , with a value of 4 at t<sup>s</sup>0 and $2 ^ { t } ( 4 )$ for $t \geq 1$ . These tables also use $\psi = 3$ and $s = 2 / 3$ . An infeasible situation is shown by asterisks.

Tables 5–8 consider the ‘‘low’’ and ‘‘high’’ demand functions $P _ { 2 }$ and $P _ { 3 }$ Ž . see Fig. 1 , along with the conventional cost pattern $C _ { \mathrm { I } }$ and the extreme dynamic pattern $C _ { \mathrm { I I } }$ of rapidly decreasing unit cost. The tables pertain to $( P _ { 2 } , C _ { \mathrm { I } } ) , ( P _ { 2 } , C _ { \mathrm { I I } } ) , ( P _ { 3 } , C _ { \mathrm { I } } )$ and $( P _ { 3 } , \ C _ { \mathrm { I I } } )$ , respectively. The Revenue<sup>s</sup>Cost equations for the separated network can be written as follows:

$$
\begin{array}{l l l} & \text {A separate} & \text {B separate} \\ (P _ {2}, C _ {\mathrm{I}}) & x ^ {3} e ^ {- x} / (1 + x) & x ^ {3} e ^ {- x} / (1 + x) \\ & = 1 / 2 ^ {t + 2} & = 9 / 2 ^ {t + 2} \\ (P _ {2}, C _ {\mathrm{II}}) & x ^ {3} e ^ {- x} / (1 + x) & x ^ {3} e ^ {- x} / (1 + x) \\ & = 1 / 2 ^ {(5 t + 4) / 2} & = 9 / 2 ^ {(5 t + 4) / 2} \\ (P _ {3}, C _ {\mathrm{I}}) & x ^ {3} / (1 + x ^ {4}) & x ^ {3} / (1 + x ^ {4}) \\ & = 1 / 2 ^ {(t + 2)} & = 9 / 2 ^ {(t + 2)} \\ (P _ {3}, C _ {\mathrm{II}}) & x ^ {3} / (1 + x ^ {4}) & x ^ {3} / (1 + x ^ {4}) \\ & = 1 / 2 ^ {(5 t + 4) / 2} & = 9 / 2 ^ {(5 t + 4) / 2}. \end{array}
$$

The one-price equations for $C _ { \mathrm { I } }$ are identical to the B separate equations when t in those equations is replaced by t<sup>q</sup>1: i.e., change $2 ^ { t + 2 } \mathrm { \Delta t o ^ { - } } 2 ^ { t + 3 }$ . The corresponding one-price change for $C _ { \mathrm { I I } }$ replaces $2 ^ { ( 5 t + 4 ) / 2 } \ \mathrm { b y } \ \overline { { 2 } } ^ { ( 5 t + 6 ) / 2 }$ in the B separate equations for period t.

We considered changes in , s, and $V _ { \mathrm { { A } } }$ and $V _ { \mathrm { { B } } }$ to see how much they affect the nature of the results shown in the tables. The specific changes include $\psi = 2 , s = 1 / 2 , ( V _ { \mathrm { A } } , V _ { \mathrm { B } } ) = ( 4 , 1 6 )$ and $( V _ { \mathrm { { A } } } , V _ { \mathrm { { B } } } ) =$ Ž . 16,4 for the initial period. We comment on these briefly after noting aspects of Tables 5–8.

## 4.1. ReÕenue

Except for very low potential volume, a provider who offers either the A service or the B service for comparable potential volumes in the separated network makes more money from the premium B service. A provider who offers one of the two main network configurations shown in the tables earns more with the one-price network, but the difference between the two is not great in any case.

Table 5 $P _ { 2 } , C _ { \mathrm { I } }$

<table><tr><td rowspan="2">t</td><td colspan="3">A separate</td><td colspan="3">B separate</td><td colspan="2">Separated totals</td><td colspan="3">One-price network</td></tr><tr><td>x</td><td>S</td><td>R</td><td>x</td><td>S</td><td>R</td><td>S</td><td>R</td><td>x</td><td>S</td><td>R</td></tr><tr><td>0</td><td>1.3</td><td>13</td><td>0.63</td><td>*</td><td>*</td><td>*</td><td>6</td><td>0.63</td><td>*</td><td>*</td><td>*</td></tr><tr><td>1</td><td>0.79</td><td>25</td><td>1.60</td><td>*</td><td>*</td><td>*</td><td>13</td><td>1.60</td><td>*</td><td>*</td><td>*</td></tr><tr><td>2</td><td>0.55</td><td>37</td><td>3.28</td><td>*</td><td>*</td><td>*</td><td>19</td><td>3.28</td><td>1.4</td><td>10</td><td>4.61</td></tr><tr><td>3</td><td>0.40</td><td>48</td><td>6.15</td><td>1.4</td><td>10</td><td>4.61</td><td>29</td><td>10.8</td><td>0.85</td><td>23</td><td>12.6</td></tr><tr><td>4</td><td>0.30</td><td>59</td><td>11.0</td><td>0.85</td><td>23</td><td>12.6</td><td>40</td><td>23.6</td><td>0.59</td><td>35</td><td>26.3</td></tr><tr><td>5</td><td>0.23</td><td>65</td><td>19.0</td><td>0.59</td><td>35</td><td>26.3</td><td>50</td><td>45.3</td><td>0.43</td><td>46</td><td>49.9</td></tr><tr><td>6</td><td>0.18</td><td>71</td><td>32.3</td><td>0.43</td><td>46</td><td>49.9</td><td>59</td><td>82.2</td><td>0.32</td><td>55</td><td>89.8</td></tr><tr><td>7</td><td>0.14</td><td>77</td><td>53.8</td><td>0.32</td><td>55</td><td>89.8</td><td>66</td><td>144</td><td>0.24</td><td>63</td><td>156</td></tr><tr><td>8</td><td>0.11</td><td>81</td><td>88.9</td><td>0.24</td><td>63</td><td>156</td><td>72</td><td>245</td><td>0.19</td><td>70</td><td>266</td></tr><tr><td>9</td><td>0.084</td><td>85</td><td>146</td><td>0.19</td><td>70</td><td>266</td><td>78</td><td>412</td><td>0.14</td><td>76</td><td>444</td></tr><tr><td>10</td><td>0.066</td><td>88</td><td>237</td><td>0.14</td><td>76</td><td>444</td><td>82</td><td>682</td><td>0.11</td><td>81</td><td>732</td></tr></table>

Table 6 $P _ { 2 } , C _ { \mathrm { I I } }$

<table><tr><td rowspan="2">t</td><td colspan="3">A separate</td><td colspan="3">B separate</td><td colspan="2">Separated totals</td><td colspan="3">One-price network</td></tr><tr><td>x</td><td>S</td><td>R</td><td>x</td><td>S</td><td>R</td><td>S</td><td>R</td><td>x</td><td>S</td><td>R</td></tr><tr><td>0</td><td>1.3</td><td>14</td><td>0.63</td><td>*</td><td>*</td><td>*</td><td>6</td><td>0.63</td><td>*</td><td>*</td><td>*</td></tr><tr><td>1</td><td>0.47</td><td>42</td><td>1.6</td><td>*</td><td>*</td><td>*</td><td>21</td><td>1.6</td><td>1.1</td><td>17</td><td>2.9</td></tr><tr><td>2</td><td>0.23</td><td>65</td><td>2.4</td><td>0.59</td><td>35</td><td>3.3</td><td>50</td><td>5.7</td><td>0.43</td><td>46</td><td>6.2</td></tr><tr><td>3</td><td>0.12</td><td>79</td><td>3.1</td><td>0.28</td><td>60</td><td>5.3</td><td>69</td><td>8.3</td><td>0.21</td><td>67</td><td>9.0</td></tr><tr><td>4</td><td>0.066</td><td>88</td><td>3.7</td><td>0.14</td><td>76</td><td>6.9</td><td>82</td><td>10.6</td><td>0.11</td><td>81</td><td>11</td></tr><tr><td>5</td><td>0.036</td><td>93</td><td>4.3</td><td>0.077</td><td>86</td><td>8.5</td><td>90</td><td>12.8</td><td>0.061</td><td>89</td><td>14</td></tr><tr><td>6</td><td>0.020</td><td>96</td><td>4.9</td><td>0.043</td><td>92</td><td>10</td><td>94</td><td>15.0</td><td>0.034</td><td>94</td><td>16</td></tr><tr><td>7</td><td>0.012</td><td>98</td><td>6.0</td><td>0.024</td><td>95</td><td>12</td><td>97</td><td>17.7</td><td>0.019</td><td>96</td><td>19</td></tr><tr><td>8</td><td>0.007</td><td>99</td><td>7.1</td><td>0.014</td><td>97</td><td>14</td><td>98</td><td>21.0</td><td>0.011</td><td>98</td><td>22</td></tr><tr><td>9</td><td>0.004</td><td>99</td><td>8.1</td><td>0.008</td><td>98</td><td>16</td><td>99</td><td>24.3</td><td>0.006</td><td>99</td><td>24</td></tr><tr><td>10</td><td>0.002</td><td>100</td><td>8.2</td><td>0.005</td><td>99</td><td>20</td><td>99</td><td>28.4</td><td>0.004</td><td>99</td><td>33</td></tr></table>

## 4.2. Separated Õersus one-price prices

The one-price network price always falls between the A-separate and B-separate prices. It tends to be about midway between the separated network prices when $C _ { \mathrm { I } }$ applies, and is closer to the A-separate price when $C _ { \mathrm { I I } }$ applies.

## 4.3. Demand satisfaction

As time passes, demand satisfactions approach 100%. The approach is much more rapid for $C _ { \mathrm { I I } }$ . In either case, the forces that drive down unit cost make the service affordable to virtually every potential user.

The main trends noted above and in the preceding section do not change substantially when other values of the parameters are used. In most cases, we are near a full-utilization scenario of 100% by $t = 1 0$ , so there is no significant difference among $P _ { 1 } , \ P _ { 2 }$ , and $P _ { 3 }$ for larger t. Revenues at such a time are a bit higher for the one-price network, but the difference

Table 7 $P _ { 3 } , C _ { \mathrm { I } }$

<table><tr><td rowspan="2">t</td><td colspan="3">A separate</td><td colspan="3">B separate</td><td colspan="2">Separated totals</td><td colspan="3">One-price network</td></tr><tr><td>x</td><td>S</td><td>R</td><td>x</td><td>S</td><td>R</td><td>S</td><td>R</td><td>x</td><td>S</td><td>R</td></tr><tr><td>0</td><td>0.67</td><td>83</td><td>2.2</td><td>*</td><td>*</td><td>*</td><td>42</td><td>2.2</td><td>*</td><td>*</td><td>*</td></tr><tr><td>1</td><td>0.51</td><td>94</td><td>3.8</td><td>*</td><td>*</td><td>*</td><td>47</td><td>3.7</td><td>1.2</td><td>32</td><td>6.2</td></tr><tr><td>2</td><td>0.40</td><td>98</td><td>6.3</td><td>1.2</td><td>32</td><td>6.2</td><td>65</td><td>12.5</td><td>0.71</td><td>80</td><td>18.1</td></tr><tr><td>3</td><td>0.32</td><td>99</td><td>10.0</td><td>0.71</td><td>80</td><td>18.1</td><td>90</td><td>28.1</td><td>0.53</td><td>93</td><td>31.6</td></tr><tr><td>4</td><td>0.25</td><td>100</td><td>16.0</td><td>0.53</td><td>93</td><td>31.6</td><td>96</td><td>47.6</td><td>0.42</td><td>97</td><td>51.8</td></tr><tr><td>5</td><td>0.20</td><td>100</td><td>25.4</td><td>0.42</td><td>97</td><td>51.8</td><td>99</td><td>77.2</td><td>0.33</td><td>99</td><td>83.2</td></tr><tr><td>6</td><td>0.16</td><td>100</td><td>40.4</td><td>0.33</td><td>99</td><td>83.2</td><td>100</td><td>124</td><td>0.26</td><td>100</td><td>133</td></tr><tr><td>7</td><td>0.13</td><td>100</td><td>64.5</td><td>0.26</td><td>100</td><td>133</td><td>100</td><td>198</td><td>0.21</td><td>100</td><td>212</td></tr><tr><td>8</td><td>0.10</td><td>100</td><td>102</td><td>0.21</td><td>100</td><td>212</td><td>100</td><td>314</td><td>0.16</td><td>100</td><td>336</td></tr><tr><td>9</td><td>0.079</td><td>100</td><td>162</td><td>0.16</td><td>100</td><td>336</td><td>100</td><td>497</td><td>0.13</td><td>100</td><td>536</td></tr><tr><td>10</td><td>0.063</td><td>100</td><td>258</td><td>0.13</td><td>100</td><td>536</td><td>100</td><td>794</td><td>0.10</td><td>100</td><td>852</td></tr></table>

Table 8

$$
P _ {3}, C _ {\mathrm{II}}
$$

<table><tr><td rowspan="2">t</td><td colspan="3">A separate</td><td colspan="3">B separate</td><td colspan="2">Separated totals</td><td colspan="3">One-price network</td></tr><tr><td>x</td><td>S</td><td>R</td><td>x</td><td>S</td><td>R</td><td>S</td><td>R</td><td>x</td><td>S</td><td>R</td></tr><tr><td>0</td><td>0.67</td><td>83</td><td>2.2</td><td>*</td><td>*</td><td>*</td><td>42</td><td>2.2</td><td>*</td><td>*</td><td>*</td></tr><tr><td>1</td><td>0.36</td><td>98</td><td>2.8</td><td>0.84</td><td>66</td><td>4.5</td><td>82</td><td>7.3</td><td>0.61</td><td>88</td><td>8.6</td></tr><tr><td>2</td><td>0.20</td><td>100</td><td>3.2</td><td>0.42</td><td>99</td><td>6.5</td><td>99</td><td>9.7</td><td>0.33</td><td>99</td><td>10.4</td></tr><tr><td>3</td><td>0.11</td><td>100</td><td>3.6</td><td>0.23</td><td>100</td><td>7.4</td><td>100</td><td>11.0</td><td>0.18</td><td>100</td><td>11.8</td></tr><tr><td>4</td><td>0.063</td><td>100</td><td>4.0</td><td>0.13</td><td>100</td><td>8.4</td><td>100</td><td>12.4</td><td>0.10</td><td>100</td><td>13.3</td></tr><tr><td>5</td><td>0.036</td><td>100</td><td>4.6</td><td>0.073</td><td>100</td><td>9.3</td><td>100</td><td>14.0</td><td>0.058</td><td>100</td><td>14.8</td></tr><tr><td>6</td><td>0.020</td><td>100</td><td>5.1</td><td>0.041</td><td>100</td><td>10.5</td><td>100</td><td>15.6</td><td>0.033</td><td>100</td><td>16.9</td></tr><tr><td>7</td><td>0.012</td><td>100</td><td>6.1</td><td>0.023</td><td>100</td><td>11.8</td><td>100</td><td>17.9</td><td>0.019</td><td>100</td><td>19.5</td></tr><tr><td>8</td><td>0.007</td><td>100</td><td>7.2</td><td>0.013</td><td>100</td><td>13.3</td><td>100</td><td>20.5</td><td>0.011</td><td>100</td><td>22.5</td></tr><tr><td>9</td><td>0.004</td><td>100</td><td>8.2</td><td>0.008</td><td>100</td><td>16.3</td><td>100</td><td>24.6</td><td>0.006</td><td>100</td><td>24.6</td></tr><tr><td>10</td><td>0.002</td><td>100</td><td>8.2</td><td>0.005</td><td>100</td><td>20.5</td><td>100</td><td>28.7</td><td>0.004</td><td>100</td><td>32.8</td></tr></table>

is not great. There is clearly an advantage in price for priority users with the one-price network, which penalizes ordinary users by about 30% or higher prices than in the separated network. However, the lower A-separate price is approximately equal to the single price for the one-price network one or two periods hence, so in a dynamic world the ordinary users do not fare too badly and might even become attracted to the QoS provided by a one-price network.

Prices for separate and one-price networks  
![](/api/attachments/DTA28994/fulltext/images/6407d198deece567761a6ed72af3fb8d069ea50d81440cb853467993a615571a.jpg)  
Fig. 2. Evolution of prices for A in a separate network line with Ž squares , for B users in a separate network line with crosses , and. Ž . in a one-price network line with circles , for the scenario of TableŽ . 8.

Fig. 2 shows the prices from Table 8 for the separate and one-price networks. It shows graphically how quickly the prices on the one-price network get reduced to the levels of the separate network for A users.

## 5. Summary

Our purpose has been to compare three network configurations for data transmission over the Internet when user demands are divided into delay-sensitive and delay-insensitive demands. Prices for the demand types were based on transfer volume and determined by equality between network costs and revenues. Dynamic uncertainties were accounted for by considering alternative futures for demands and costs, including economies of scale for costs and possible effects of competition and technological advances.

The three network configurations investigated were a separated network for the demand types, a single one-price network that provides high QoS to all users, and a two-tiered network that logically distinguishes between types. Dynamic analysis showed that network comparisons can be sensitive to demand and cost scenarios, no network is obviously superior to the others, and as t gets large, the trends are pretty well fixed. In terms of prices, the premium-service one-price network benefits delay-sensitive users but penalizes delay-insensitive users, and the two-tiered network usually gives a modest advantage over the separated network to both types. The largest revenues occur either for the separated network or the one-price network. Demand satisfaction percentages for the three are comparable, with no network uniformly superior to the others. Potential user participation approaches 100% as time passes, and this happens quickly when unit costs and prices decrease rapidly. Even the delay-sensitive users see their prices and demand satisfactions approach what they could obtain on a separate network within one or two time periods.

## Acknowledgements

We thank Dave Belanger, Chuck Kalmanek, Tony Lauck, and Clem McCalla for helpful comments.

## References

<sup>w</sup> <sup>x</sup> 1 L. Anania, R.J. Solomon, Flat — the minimalist price, in: L.W. McKnight, J.P. Bailey Eds. , Internet Economics, MITŽ . Press, 1997, pp. 91–118. http:<sup>rr</sup>www.press.umich.edu<sup>r</sup> jep<sup>r</sup>, Preliminary version in J. Electronic Publishing, special issue on Internet economics.

<sup>w</sup> <sup>x</sup> 2 Boardwatch magazine, http:<sup>rr</sup>www.boardwatch.com<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 3 K.G. Coffman, A.M. Odlyzko, The size and growth rate of the Internet, First Monday Vol. 3 No. 10 1998 .Ž . Ž . http:<sup>rr</sup>www.firstmonday.dk<sup>r</sup>, October ; Also available atŽ . http:<sup>rr</sup>www.research.att.com<sup>r ;</sup>amo.

<sup>w</sup> <sup>x</sup> 4 P. Ferguson, G. Huston, Quality of Service: Delivering QoS on the Internet and in Corporate Networks, Wiley, 1998.

<sup>w</sup> <sup>x</sup> 5 P.C. Fishburn, A.M. Odlyzko, R.C. Siders, Fixed fee versus unit pricing for information goods: competition, equilibria, and price wars, First Monday Vol. 2 No. 7 1997 .Ž . Ž . http:<sup>rr</sup>www.firstmonday.dk<sup>r</sup>, July .Ž .

<sup>w</sup> <sup>x</sup> 6 P.C. Fishburn, A.M. Odlyzko, R.C. Siders, Fixed fee versus unit pricing for information goods: competition, equilibria, and price wars, Hurley, D., Kahin, B., Varian, H. Eds. , Ž . Also to appear in Internet Publishing and Beyond: The Economics of Digital Information and Intellectual Property, MIT Press. Available at http:<sup>rr</sup>www.research.att.com<sup>r ;</sup> amo.

<sup>w</sup> <sup>x</sup> <sup>U</sup> 7 J. Harms, From SWITCH to SWITCH — extrapolating from a case study, Proc. INET’94, pp. 341-1 to 341-6. Available at http:<sup>rr</sup>info.isoc.org<sup>r</sup>isoc<sup>r</sup>whatis<sup>r</sup>conferences<sup>r</sup>inet<sup>r</sup>94<sup>r</sup>papers<sup>r</sup>index.html.

<sup>w</sup> <sup>x</sup> 8 D.R. Irvin, Modeling the cost of data communication for multi-node computer networks operating in the United States, IBM J. Res. Dev. 37 1993 537–546.Ž .

<sup>w</sup> <sup>x</sup> 9 B. Leida, A cost model of Internet service providers: Impli-

cations for Internet telephony and yield management, MS thesis, Department of Electr. Eng. and Comp. Sci. and Technology and Policy Program, MIT, 1998. Available at http: <sup>r r</sup> www.nmis.org <sup>r</sup> AboutNMIS<sup>r</sup> Team <sup>r</sup> BrettL <sup>r</sup> contents.html.

<sup>w</sup> <sup>x</sup> 10 J.K. MacKie-Mason, H.R. Varian, Economic FAQs about the Internet, in: L.W. McKnight, J.P. Bailey Eds. , InternetŽ . Economics, MIT Press http:<sup>rr</sup>www.press.umich.edu<sup>r</sup>jep<sup>r</sup>, 1997, pp. 27–62, A version is available in J. Electronic Publishing, special issue on Internet economics.

<sup>w</sup> <sup>x</sup> 11 L.W. McKnight, J.P. Bailey Eds. , Internet Economics, MITŽ . Press http:<sup>rr</sup>www.press.umich.edu<sup>r</sup>jep<sup>r</sup>, 1997, Preliminary version of many papers available in J. Electronic Publishing, special issue on Internet economics.

<sup>w</sup> <sup>x</sup> 12 B.M. Mitchell, I. Vogelsang, Telecommunications Pricing: Theory and Practice, Cambridge Univ. Press, 1991.

<sup>w</sup> <sup>x</sup> 13 A.M. Odlyzko, Data networks are lightly utilized, and will stay that way. Available at http:<sup>rr</sup>www.research.att.com<sup>r</sup> <sup>;</sup>amo.

<sup>w</sup> <sup>x</sup> 14 A.M. Odlyzko, The economics of the Internet: Utility, utilization, pricing, and Quality of Service. Available at http:<sup>rr</sup>www.research.att.com<sup>r ;</sup>amo.

<sup>w</sup> <sup>x</sup> 15 J. Rendleman, Connectivity crunch stymies IT access to high-speed lines, PCWeek, April 13, 1998, pp. 1 and 20. Available at http:<sup>rr</sup>www.zdnet.com<sup>r</sup>pcweek<sup>r</sup>news<sup>r</sup> 0413<sup>r</sup>13tl.html.

<sup>w</sup> <sup>x</sup> 16 S.G. Steinberg, Netheads vs. Bellheads, Wired, 4, No. 10 Ž . Oct. 1996 , pp. 144-147, 206-213. Available at http:<sup>rr</sup>www.wired.com<sup>r</sup>wired<sup>r</sup>4.10<sup>r</sup>features<sup>r</sup>atm.html.

<sup>w</sup> <sup>x</sup> 17 UUNet Access Services, available at http:<sup>rr</sup>www.us.uu. net<sup>r</sup>html<sup>r</sup>access services.html. <sub>–</sub>

Peter C. Fishburn received the BS degree in industrial engineering from Pennsylvania State University, University Park, in 1958 and the PhD degree in operations research from Case Institute of Technology, Cleveland, OH, in 1962. He joined AT&T Bell Laboratories in 1978 and is now with AT&T Labs-Research. He is the author or co-author of nine books. Dr. Fishburn was elected fellow of The Econometric Society in 1974 and The Institute of Mathematical Statistics in 1984. He was awarded the Frank P. Ramsey Medal of the Operations Research Society of America in 1987 and the John von Neumann Theory Prize of the Institute of Operations Research and the Management Sciences in 1996.

Andrew Odlyzko is Head of the Mathematics and Cryptography Research Department at AT&T Labs, and also Adjunct Professor at the University of Waterloo. He has done extensive research in technical areas such as computational complexity, cryptography, number theory, combinatorics, coding theory, analysis, and probability theory. In recent years, he has also been working on electronic publishing, electronic commerce, and economics of data networks. He is the author of such widely cited papers as ‘‘Tragic loss or good riddance? The impending demise of traditional scholarly journals,’’ ‘‘The decline of unfettered research,’’ and ‘‘The bumpy road of electronic commerce.’’ His home page is http:<sup>rr</sup>www.research.att.com<sup>r ;</sup>amo.
