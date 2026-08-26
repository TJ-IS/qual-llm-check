---
otero_id: 11414
otero_key: "U8BVGZHH"
title: "Economic decision criteria for the migration to cloud storage"
authors: "Maurizio Naldi; Loretta Mastroeni"
year: "2016"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2014.34"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
EMPIRICAL RESEARCH

# Economic decision criteria for the migration to cloud storage

Maurizio Naldi<sup>1</sup> and Loretta Mastroeni<sup>2</sup>

<sup>1</sup>Dipartimento di Ingegneria Civile e Ingegneria Informatica, Università di Roma Tor Vergata, Roma, Italy; <sup>2</sup>Dipartimento di Economia, Università di Roma Tre, Rome, Italy

Correspondence: Maurizio Naldi, Dipartimento di Ingegneria Civile e Ingegneria Informatica, Università di Roma Tor Vergata, Roma, 00133, Italy. Tel: +39 06 7259 7269; E-mail: naldi@disp.uniroma2.it

## Abstract

Cloud storage has fast become a widespread alternative to in-house costly storage infrastructures. However, the migration to cloud storage is not necessarily everybody’s best choice and should be evaluated in a rigorous quantitative way against the alternative over a long time horizon. We propose a methodological approach for the comparison of cloud vs in-house solutions, based on the use of the Net Present Value and employing stochastic models for storage prices and memory needs. We analyse two decision criteria, which employ the median and the mean value of the Differential Net Present Value (DNPV), respectively. Through three appropriate risk measures, we show that the mean DNPV is the less risky decision criterion. Since the DNPV is a stochastic quantity, we also consider a protection measure against the risk of taking the wrong decision, which relies on underwriting an insurance policy. Through the real options approach, we propose a pricing formula for such policy, showing that it is an affordable means to hedge against risk for smaller companies and over a limited time horizon. Both the decision criteria and the insurance pricing formula are applied in a typical scenario.

European Journal of Information Systems advance online publication, 30 September 2014; doi:10.1057/ejis.2014.34

Keywords: Cloud storage; Buy vs Lease; IaaS; Economic decision criteria

## Introduction

In cloud storage, a company decides to store its data on repositories (the cloud) owned by an external party (the cloud provider) rather than on its own storage facilities. The external repository may be employed as a back-up or as a complete replacement. In the former case, the company has to maintain an in-house storage facility, while the alternative allows the company to get rid of it. The alternative between in-house storage and cloud storage is often referred to as a ‘Buy vs Lease’ decision: in the in-house solution, the company has to buy its own storage infrastructure; in the cloud solution, the company leases the cloud provider’s infrastructure.

With the migration of all its data to the cloud, the company zeroes its investments in storage devices, and switches from an infrastructure-based to a service-based mode of operation. Actually, cloud storage is a major example of the IaaS (Infrastructure as a Service) paradigm and an important component of the current virtualization trend (Lenk et al, 2009).

Since migration involves a signi<sup>fi</sup>cant one-off effort to move all the data on the new platform, and that can be exploited by cloud providers to cage the company in a lock-in condition, the decision to migrate has to be examined thoroughly. In particular, the timing of decisions has an impact on the possibility of fully exploiting growth options (Khan et al, 2013) and the pro<sup>fi</sup>tability of migrations (Laatikainen et al, 2014; Naldi, 2014).

A major promise of cloud storage is to reduce costs for the company. Actually shifting to IaaS means trading capital expenditures (CAPEX), due to purchasing disks, for operational expenditures (OPEX), due to paying the service offered by cloud providers. Aside from the organizational, security, and reliability issues that are involved in the migration to the cloud, the main focus in an economical analysis is on the comparison between the costs involved in the two alternatives.

Some cost analyses have been conducted on clouds. A cost breakdown has been provided for data centres by Greenberg et al (2009), which includes the costs of servers and networking facilities in addition to storage facilities and power. A comprehensive cost model for hybrid clouds, including both private and public clouds has been described in Kashef & Altmann (2011). A toolkit has been described by Khajeh-Hosseini et al (2012) to compute the cost of cloud adoption on the basis of a detailed schedule of resource needs. While all these papers consider the more general cloud computing service rather than simply cloud storage, their focus is on the cost analysis of the cloud solution rather than the comparison with the in-house storage alternative. Bhattacherjee & Park (2014) have instead proposed a model of end-user migration from client-hosted computing to cloud computing using migration theory, rather than through an economics-based approach.

An economical comparison of the owned and leased storage solutions is instead provided by Walker et al (2010), where forecasts for the price of disks are employed to obtain a single <sup>fi</sup>gure of comparison between the two alternatives, based on the Net Present Value (NPV) tool. The framework employed by Walker et al (2010) is, however, completely deterministic. Mastroeni & Naldi (2011b) have replaced that framework by a probabilistic one, which allows to model the uncertainty unavoidably associated to future trends in both prices and storage demand. Another shortcoming of the deterministic approach proposed by Walker et al (2010) is that it does not allow to evaluate the risk associated to migration. In fact, the decision taken on the basis of that single comparison <sup>fi</sup>gure may turn out to be wrong. An early attempt to provide a risk measure in the cloud adoption decision has been made by Mastroeni & Naldi (2011a).

In this paper, we examine with an economics-based approach the problem of deciding whether to adopt cloud storage or buy and run a storage infrastructure. We formulate a set of probabilistic models, which provide a complete view of the costs associated to either decision. We propose and compare two decision criteria, based on the mean and the median value of the Differential Net Present Value (DNPV), respectively. We compare them by evaluating the associated risk through three risk measures: the probability of taking a wrong decision, the Value-at-Risk (VaR), and the Conditional Value-at-Risk (CVaR). The latter two are imported from the <sup>fi</sup>eld of <sup>fi</sup>nancial evaluation. In order to hedge against the risk of taking the wrong decision, we propose an insurance scheme and provide an insurance pricing formula based on the real options approach. Though the security of cloud solutions is an issue of concern, at present no thorough experimental comparisons of the security performance of cloud vs in-house storage have appeared in the literature. In the following, we consider just the economic pros and cons of migration, assuming that the two alternative storage solutions do not exhibit signi<sup>fi</sup>cantly different security characteristics, though we are aware that the decision to migrate may be taken on the basis of other factors in addition to the purely economic one.

Our main <sup>fi</sup>ndings show that: (1) the mean DNPV is to be preferred as a decision criterion, as it leads to lower risks; (2) there is a region of greater uncertainty between the two alternative decisions to buy or lease; (3) the advantage of the mean over the median DNPV is, however, limited to that region of greater uncertainty, while the two criteria are otherwise essentially equivalent; (4) the decision to buy rather than lease is favoured for large companies and for longer time horizons; (5) the price of the insurance policy is particularly affordable for smaller companies and over limited time horizons, while it may get very large for larger companies and longer time horizons.

The paper is structured as follows. We <sup>fi</sup>rst provide an overview of the current offer by cloud providers and the future demand of storage capacity. We then describe all the cost components appearing in the comparison between the two alternative decisions. After recalling the main analysis tool adopted for the comparison, the NPV, we use that tool to formulate two decision criteria. We then introduce some risk measures and report the comparison results. Finally, we propose an insurance-based approach to protect against changes in the envisaged scenario.

## Cloud storage market

As recalled in the ‘Introduction’, the great promise of cloud storage is to reduce costs for the enterprise. However, the success of cloud storage is also fuelled by an increasing production of digital documents, which drives the demand for storage. This demand has attracted the attention of many companies on the supply side, which see an interesting business opportunity in providing remote storage. In this section, we brie<sup>fl</sup>y review both factors: the expansion of storage needs of prospective cloud users and the related proliferation of cloud offers. In addition, we also consider the technological evolution of disks, which brings along a reduction of the physical space needed to store the same quantity of data.

## The demand for storage

The development of digital consumer electronics has moved to the digital domain much of the content that was stored in an analogue fashion, for example, documents, photos, videos. In addition, native digital applications (e.g., the apps running on tablets or smartphones) continually generate new data.

The total amount of data generated in the world has grown from 2.6 exabytes in 1986 to 295 exabytes in 2007, with a 23% compound annual growth rate (CAGR) over the latest two decades (Hilbert & López, 2011). More recent data, extending into 2011, show that the total amount of generated digital data was 1699 exabytes in 2011, with a 55.7% CAGR over the years 2006–2011 (Makarenko, 2011). Actually, that relatively low value reported by Hilbert was due to the high base level provided by analogue storage devices prevalent at the beginning of the analysis period. As reported by Hilbert & López (2011), roughly half of this volume of data is stored on hard disks, servers, and mainframe systems.

Nearly a decade ago, Coughlin provided historical data and a forecast concerning the amount of digital memory installed. His study spanned the period from 2000 to 2005, showing an exponential growth trend with a yearly growth rate of 70% (the amount of memory installed would double every 15.7 months) (Coughlin, 2003).

According to the 2014 report by IDC, the worldwide size of data was 4.4 zettabytes in 2014 and is going to exhibit a tenfold increase by 2020 (VV.AA., 2014).

In two previous analyses of the pro<sup>fi</sup>tability of data migration (Mastroeni & Naldi, 2011b; Walker et al, 2010), the overall size of data stored by the company was assumed to grow linearly over time. Actually, the data reported above show that the amount of digital data to be stored is growing much faster.

Here, we assume the amount of memory M grows at an exponential rate:

$$
M _ {t} = M _ {0} (1 + g _ {m}) ^ {t},\tag{1}
$$

where t is the number of years from now, and $g _ { m }$ is the yearly growth rate.

## Disk capacity

The storage needs can be accommodated by deploying an increasingly large number of disks. However, time also brings along a technological evolution: even established storage means (such as tapes or hard disks) exhibit an increasing capacity, so that devices of limited size store more and more data.

A measure of the increase in storage capacity is the areal density of disks, which is the data amount that can be stored per disk unit area and is typically measured in GB/square inch. In the 1990s the areal density of hard disk drives grew exponentially, at a CAGR of up to 100%. However, this rate has then slowed to values as low as 20%, and currently is around 30% (Eleftheriou et al, 2010).

If we assume a <sup>fi</sup>xed area for the disks, the growth in disk capacity follows that in the areal density. We can therefore adopt an exponential model for the growth of the capacity of a disk. At time t the capacity Ω of each new disk is

$$
\Omega_ {t} = \Omega_ {0} (1 + g _ {c}) ^ {t},\tag{2}
$$

where g is the yearly growth rate. According to the latest trend, we could set $g _ { c } { = } 0 . 3$

Increased capacity applies just to new disks. As it happens in reality, we assume that, at each time step, the owner of the storage infrastructure leaves in place the working disks (whose capacity is that dictated by the time when they were bought), replaces the failed disks with new ones of capacity allowed by the current technological state, and buys new disks to cope with the increasing needs (again of current capacity).

Table 1 Cloud storage unit price (1 TB of storage space)

<table><tr><td>Provider</td><td>Unit price ($)</td></tr><tr><td>Amazon</td><td>0.095</td></tr><tr><td>Google Drive</td><td>0.05</td></tr><tr><td>IDrive</td><td>0.08</td></tr><tr><td>Dropbox</td><td>0.06625</td></tr><tr><td>Mozy</td><td>0.39</td></tr><tr><td>Mean</td><td>0.13625</td></tr><tr><td>Standard deviation</td><td>0.1428</td></tr></table>

## Cloud providers

We have already provided an analysis of major cloud providers and their storage prices (Mastroeni & Naldi, 2012a; Naldi & Mastroeni, 2013). Most providers offer pricing plans aimed separately at consumers and business customers. With the exception of Amazon, the pricing plans of all providers are formulated through a set of capacity brackets and a <sup>fi</sup>xed fee for each bracket (the so-called bundling pricing model). The resulting unit price curve is a piecewise hyperbolic curve.

In Table 1, we report a comparison of the prices surveyed in Naldi & Mastroeni (2013). We have limited ourselves to providers offering pricing plans directed at business customers, with a maximum capacity of at least 1 terabyte (TB). There is a signi<sup>fi</sup>cant dispersion of values, since the standard deviation is nearly equal to the mean value. Actually, among the <sup>fi</sup>ve providers, four offer quite similar prices, below US\$0.1, while one can be considered as an outlier. This analysis provides us with a range of unit prices to use in the migration evaluation.

## Storage costs

A company needing to store its data must compare the alternatives of owning its storage infrastructure or leasing it from a cloud provider. From an economic point of view, comparing the two alternatives means comparing their costs and revenues. In this section, we show that the comparison can be restricted to costs alone and provide an overview of all the cost items associated to either solution.

We examine <sup>fi</sup>rst the plus side of any pro<sup>fi</sup>t equation, that is, the revenues. When leasing storage resources from a cloud provider, the company does not receive any direct pro<sup>fi</sup>t from storing the data, but rather pays the cloud provider for the storage service. Instead, it gets revenues from the usage of the data stored on the cloud to provide services to its customers. Similarly, the data centre directly owned by a company is a cost centre (assuming that it is used for the company’s data only and does not provide storage services to other parties) and does not provide direct revenues, which are obtained through selling services that use those data, as in the cloud solution. If selling services does not rely on the ownership of the infrastructure, the services sold when the data reside either on the cloud or in the company’s data centre are just the same. There is no difference between the revenues got with either solution. We can then safely limit ourselves to compare the costs incurred, rather than both revenues and costs.

The only exception to this assumption is related to the ownership of the storage infrastructure, which has a value by itself. In the cloud case, the company does not own the infrastructure and cannot exploit that value. Instead, if the company owns a data centre, it can sell its storage resources on the secondary market. As the comparison must be conducted on a level ground, we must take into account, on the plus side of the Buy solution, the value of the storage infrastructure on the secondary market (the salvage value) as the only revenue considered in this context.

In the coming subsections, we <sup>fi</sup>rst examine the cost drivers and then describe separately each of the following items:

● disk purchase;

● power and personnel;

● revenues from salvage;

● leasing fee;

● transfer and management (T&M);

● racking space.

Some of these costs are incurred just under either decision, while some other are incurred, though to a different extent, under both decisions. In Table $^ { 2 , }$ we classify the cost categories.

## Disk purchase

A major cost item, when a company owns its storage infrastructure, is the purchase of disks. Disks are bought both to cope with the growing storage needs and to replace failed disks. In order to predict the amount of money spent on disks, we have to model both quantities: the price of disks and the rate of failure.

Walker et al (2010) have reported the results of an extensive survey, conducted on SATA disk prices every week over more than 5 years. According to that survey, the price of disks falls over time according to an exponential trend:

Table 2 Cash <sup>fl</sup>ow components

<table><tr><td>Item</td><td>Category</td><td>Buy-or-lease</td></tr><tr><td>Disks</td><td>CAPEX</td><td>B</td></tr><tr><td>Power</td><td>OPEX</td><td>B</td></tr><tr><td>Personnel</td><td>OPEX</td><td>B/L</td></tr><tr><td>Salvage</td><td>Revenues</td><td>B</td></tr><tr><td>Lease</td><td>OPEX</td><td>L</td></tr><tr><td>T&amp;M</td><td>OPEX</td><td>L</td></tr><tr><td>Space</td><td>OPEX</td><td>B</td></tr></table>

$$
P _ {t} \simeq P _ {0} e ^ {- \beta t},\tag{3}
$$

with $P _ { 0 } { = } 5 0 . 3$ and $\beta = 0 . 4 3 8$ . That trend is the outcome of a regression analysis: the actual prices collected in that survey <sup>fl</sup>uctuated around the regression trend. Walker et al (2010) assumed future prices to change deterministically, while we expect that trend to be just a prediction of the average value of future price.

Here, as in Mastroeni $\&$ Naldi (2011b), we abandon the deterministic model and assume instead that the future price is described by a Geometric Brownian Motion random process (Chan & Wong, 2006):

$$
P _ {t} = P _ {0} e ^ {\nu t + \sigma W _ {t}} = P _ {0} e ^ {\big ((\mu - \sigma^ {2}) / 2 \big) t + \sigma W _ {t}},\tag{4}
$$

with $W _ { t }$ being a Wiener process sampled at time t. The terms $\nu$ and $\bar { \sigma } ^ { 2 }$ are, respectively, the drift and variance of the process. As the expected value of such a process is

$$
\mathbb {E} [ P _ {t} ] = P _ {0} e ^ {\mu t},\tag{5}
$$

we can easily match the characteristics of this process with our assumption (3) on the expected value of the price. Namely, the match is perfect by setting $\mu = - \beta .$ At any time t, the price follows a lognormal distribution around its expected value (3). The use of the lognormal distribution guarantees that the price provided by the model will not turn negative, even in the long run.

We now turn to the analysis of the number of disks to buy. We recall that the amount of memory needed is de<sup>fi</sup>ned by Eq. (1) and the capacity of disks grows over the years according to Eq. (2). In order to evaluate how many disks to buy each year, we take into account both how many fail and how old they are (the failed disks may then have different capacity). The resulting procedure goes through the following steps:

1. Evaluate the memory requirement M<sub>t</sub> for time t through Eq. (1)

2. Determine which disks fail and their overall storage− capacity $F _ { t }$

3. Compute the overall storage capacity to buy $B _ { t } { = } M _ { t } { - } M _ { t - 1 } { + } F _ { t }$

4. Compute the number of disks to buy $\Delta D _ { t } = \left\lceil { B _ { t } } / { \Omega _ { t } } \right\rceil$

In this procedure, Steps 1, 3, and 4 are straightforward. Instead, for Step 2 we need a model to simulate the failure of disks. Walker et al (2010) assumed failures (and therefore replacements) to take place deterministically, at a <sup>fi</sup>xed rate each year. This assumption is quite unrealistic, as failures occur randomly. In this paper, we take therefore the more realistic assumption that failures take place randomly.

Failure data are typically reported through the Annual Replacement Rate (ARR), the percentage of disks replaced each year. Just a few extensive studies on disk failures are reported in the literature. We cite two studies, one of which is also considered by Walker et al (2010), whose conclusions are based on the observation of more than one hundred thousand disks. Pinheiro et al (2007) categorize the failure data by the disk age. The reported ARRs vary from a minimum of 1.7% for disks in their <sup>fi</sup>rst year of operation to a maximum of 8.6% for 3-year-old disks. A wider range is reported by Schroeder & Gibson (2007), with ARRs varying between 0.5 and 13.5% (3% being the most frequent value).

In order to consider both the aggregate failure rate and its dependence on the disk age, we adopt a strati<sup>fi</sup>ed model, where we <sup>fi</sup>rst determine the number of failed disk each year, and then which disks fail (which takes into account their age). As disks are assumed to fail independently, the number of failures per year follows a binomial distribution, where the marginal failure probability of a disk during a year is assumed to be well estimated by the ARR. We then distribute the failures among the array of installed disks. From the analysis of the failure rates reported by Pinheiro et al (2007), we can recognize two regions: the failure rate is quite low during the <sup>fi</sup>rst year in the disk’s lifetime, but then stabilizes around a higher plateau. For each disk we assume that the probability of being among the failed ones is proportional to that agedependent failure rate. In this paper, we assume here that the failure rate for older disks is fourfold that of new disks (i.e., with a lifetime of 1 year or less).

We can associate the generic i-th working disk at time t with its age $A _ { i }$ and its state $R _ { i , t }$ at that time (the state takes the value 1 if the i-th disk is working and 0 otherwise). We have then

$$
\frac {\mathbb {P} \left[ R _ {i , t + 1} = 0 \mid R _ {i , t} = 1 , A _ {i} > 1 \right]}{\mathbb {P} \left[ R _ {i , t + 1} = 0 \mid R _ {i , t} = 1 , A _ {i} \leqslant 1 \right]} = 4.\tag{6}
$$

In order to select the disks that fail at time t+1 among those working at time t, we employ the following procedure:

1. associate to each disk a uniform random variable with a domain de<sup>fi</sup>ned so as to comply with the condition (6);

2. generate a uniform pseudo-random number for each working disk according to Step 1;

3. rank in descending order the disks by the associated pseudo-random number generated at Step 2;

4. discard the top disks in the ranking obtained at Step 3 (i.e., those exhibiting the largest pseudo-random numbers).

## Power and personnel expenses

In addition to CAPEX, the company incurs some power and personnel expenses (both of which are OPEX) to run the disks. These expenses are incurred, though to a different extent, both in the Buy and in the Lease cases.

Under the Buy case we consider both power costs and personnel costs. For power costs, the cost driver is the amount of energy consumed, expressed in kWh. We consider a unit cost δ per kWh, and a power $E _ { c o n t }$ for the controller and $E _ { d i s k }$ for each disk (both expressed in kW).

For personnel costs, the cost driver is instead the amount of time spent by the personnel taking care of the storage infrastructure during the period of reference (i.e., each year). For the year t, the personnel OPEX is a multiple λ of the unit cost H .

The overall OPEX incurred at time t under the Buy decision is then

$$
O _ {b u y, t} = 3 6 5 \cdot 2 4 \cdot \delta (E _ {c o n t} + E _ {d i s k} D _ {t}) + \lambda H _ {t}.\tag{7}
$$

If the company leases the disks through the cloud, it instead incurs no energy costs, as these pertain to the data centre’s lessor, but still incurs a portion of the personnel costs. In fact, some personnel is still needed, at least for the following essential functions: cloud storage procurement; storage volume planning; technical interface between the company’s own IT systems and the cloud. We indicate by $\phi$ the multiple of the unit personnel cost incurred. The OPEX incurred at time t under the Lease decision is then

$$
O _ {l e a s e, t} = \phi H _ {t}.\tag{8}
$$

## Salvage value

Under the Buy decision, the company possesses its own disks. At the end of the time period considered for the analysis, it is however left with a number of disks it would not have under the Lease decision. Such disks have a value on the secondary market. In order to perform a level comparison between the two decisions, we have to take into account the salvage value of the disks and include it among the positive contributions to the NPV under the Buy decision.

We assume that the sale is accomplished at the end of the analysis period, and the salvage value is a <sup>fi</sup>xed percentage of the market price for a new disk of the same capacity, regardless of the actual age of the disk sold on the secondary market (Mastroeni & Naldi, 2011b; Walker et $^ { a l , }$ 2010). If we indicate by γ<1 that percentage (the salvage factor), the salvage value S of the disks sold at time n is

$$
S = \sum_ {i = 1} ^ {D _ {n}} \gamma \Omega_ {n - A _ {i}} P _ {n} = \gamma P _ {n} \sum_ {i = 1} ^ {D _ {n}} \Omega_ {n - A _ {i}},\tag{9}
$$

where $\Omega _ { n - A _ { i } }$ represents the capacity of the i-th of age A working at time n.

## Leasing fee

When opting for the Lease decision, the company opts to pay for the service provided by the cloud owner rather than for the equipment provided by the disk vendor. In the business model dominant so far, as described in the section on storage costs, the cloud service is provided for a <sup>fi</sup>xed fee, which depends on the amount of storage capacity required by the company. In this subsection, we describe the model adopted for this leasing fee.

The leasing fee is essential to the business model of the cloud provider. It allows the provider to cover its own expenses and make some pro<sup>fi</sup>t. What the cloud provider has to spend to build and run its storage facility is not different in nature by what the company would spend to build and run its own storage facility. The sustainability of the cloud business model lies mainly in the economies of scale that the cloud allows for, as the cloud provider would run a very large storage facility to cater for the needs of a very large number of companies.

Walker et al (2010) adopted a leasing fee scheme with unit fees slightly decreasing with memory size. However, no consideration was given to the evolution of pricing schemes over time. Actually, we have seen that the price of disks has fallen over the years, and we can expect it to follow a similar trend in the future. At the same time, we recognize that disk purchasing is a major expense item for the cloud provider as well. We can conclude that the future price of cloud storage would re<sup>fl</sup>ect the downward trend of disks.

Following the model introduced by Mastroeni & Naldi (2011b), we assume here that the leasing fee follows the price of disks:

$$
L _ {t} = \eta P _ {t},\tag{10}
$$

where the coef<sup>fi</sup>cient $\eta$ is the leasing surcharge.

The leasing surcharge is a major parameter determining the economical convenience of the offer of any cloud provider: any increase of the leasing surcharge progressively shifts the balance towards the Buy decision.

Of course, the leasing fee may be expected to depend on the quality of storage (e.g., the availability and reliability performances), which may be embedded in a Service-Level Agreement (SLA). Though at present just Amazon offers pricing plans differentiated by quality, it may be followed by others in the future. In the following, we assume that the leasing fee incorporates SLA parameters adequate for the company’s needs and of the same level as those provided by the in-house solution.

## T&M costs

When adopting the cloud to store data, what is paid for actually storing the data may not be the only expense related to the use of the cloud. There can be costs due to transferring the data to/from the cloud (uploading and downloading operations) and to the management of <sup>fi</sup>les residing on the cloud. For example, Amazon charges a price of \$0.01 for each block of 1000 management requests (PUT, COPY, POST, or LIST operations) and an additional price for each GB transferred out of the cloud to the Internet. The impact of <sup>fi</sup>le management operations on vendor switching has been analysed by Abu-Libdeh et al (2010). Such costs may be particularly relevant if the cloud is used as a mass distribution tool, as in the case of the Video-on-Demand service (Li et al, 2011).

In this paper, we consider both T&M costs. Transfer costs are naturally determined by the volume of data moved in and out of the cloud. We can assume them to be proportional to the amount of data stored in the cloud. Management costs are determined instead by the number of operations performed on <sup>fi</sup>les residing on the cloud, but we assume likewise that the number of operations is proportional to the amount of data stored as well. In the end, T&M costs as a whole can be considered as OPEX costs proportional to the amount of data stored. At time t, we have

$$
V _ {t} = \tau M _ {t}.\tag{11}
$$

The unit cost τ takes into account both the price charged for each unit of data moved in or out of the cloud and the number of operations (either management or transfer ones) for each unit of data stored.

## Cost of racking space

If the company opts for an in-house solution, it has to physically devote a portion of space to host its disks. Such cost has to be considered among those pertaining to the BUY solution; in the LEASE solution, the disks will be part of the cloud provider’s infrastructure.

The cost of space is proportional to the surface occupied by the disks. Assuming that the space is rented, that cost is expressed as a yearly rental fee $\mu$ per $\mathrm { m } ^ { 2 }$ . In turn, disks are stacked on a rack, whose vertical capacity is typically measured in U-units (a rack unit is 1.75 inches high). If we indicate the footprint of a rack by ξ (expressed in $\mathrm { i n } ^ { 2 } )$ and the capacity of a rack by $\psi$ (the number of disks per rack), the yearly cost is

$$
W _ {t} = \frac {\mu \xi}{\psi} D _ {t}.\tag{12}
$$

Since it is paid as a yearly fee, the cost of space is an OPEX item.

## Migration convenience metrics

We have reviewed all the cost items involved in either the Buy or the Lease decision. These costs have to be accounted for together to arrive at an overall comparative evaluation of the two alternatives. For this purpose, we resort to a well-known tool in the economic analysis of investments: the NPV. In this section, we brie<sup>fl</sup>y recall the de<sup>fi</sup>nition of NPV and present its formulation and use in the cloud storage context.

## The NPV

The NPV provides us with an estimate of the value of an investment project (Newman et al, 2004). The project is represented by the set of its cash <sup>fl</sup>ows: revenues are positive cash <sup>fl</sup>ows, while expenses are negative ones. For a project lasting n years, the NPV considers all its cash <sup>fl</sup>ows over the project’s lifetime, lumping up the cash <sup>fl</sup>ows occurring during each year in a single <sup>fi</sup>gure. If we indicate the net cash <sup>fl</sup>ow pertaining to the year t by $C F _ { t } ,$ the NPV of the project is

$$
N P V = \sum_ {t = 0} ^ {n} \frac {C F _ {t}}{(1 + k) ^ {t}},\tag{13}
$$

where k is the discount rate to take into account the time value of money. The discount rate accounts for the pro<sup>fi</sup>tability expected of the project and has to incorporate the risk associated to the investment: the higher the risk, the higher the discount rate. It can be thought of as the sum of the risk-free discount rate (the return expected on an activity considered as free of risk, for example the investment in a government bond such as the bill issued by the United States) and a risk premium.

A project is pro<sup>fi</sup>table if its NPV is positive, so that the overall revenues exceed costs. Moreover, the larger the NPV, the better the project.

We can use the NPV also to compare two alternative projects. Since we seek for an NPV as large as possible, we prefer the project exhibiting the larger NPV. This can be pursued by computing the difference between the NPV’s pertaining to the two project, which goes under the name of DNPV, and opting for either project depending on the sign of the DNPV. In our case, we can formulate the Differential NPV as

$$
D N P V = N P V _ {B u y} - N P V _ {L e a s e},\tag{14}
$$

so that the company should opt to build its own storage infrastructure if DNPV > 0. We note that we should include the revenues in the computation of both the NPV and the DNPV, but, under the assumption that both alternatives allow to offer the same services and get the same revenues, the revenues components cancel out in Eq. (14), excepting the previously mentioned salvage value, and we can limit ourselves to consider just the cost components.

We have already detailed all the cost components. We summarize them in Table 2, indicating the category they belong in (Revenues, CAPEX, or OPEX), and if they are incurred just when buying (B), when leasing (L), or in both cases (B/L).

The <sup>fi</sup>nal expression of the Differential NPV is then

$$
D N P V = \sum_ {t = 0} ^ {n} \frac {L _ {t} - C _ {t} + O _ {\text { lease } , t} - O _ {\text { buy } , t} + V _ {t} - W _ {t}}{(1 + k) ^ {t}} + \frac {S}{(1 + k) ^ {n}},\tag{15}
$$

where $C _ { t }$ is the capital expense (CAPEX) incurred at time t to purchase the disks and the pertaining controllers, $O _ { b u y , t }$ and $O _ { l e a s e , t }$ are, respectively, the operational expenses (OPEX) at time t associated to the two decisions (which include personnel and power), $L _ { t }$ is the leasing cost at time t (the fee paid to the cloud provider), $V _ { t }$ is the cost of <sup>fi</sup>le T&M operations, $W _ { t }$ is the cost of racking space, and S is the salvage value of the disks purchased (collected at time n by selling the disks on the secondary market).

## Decision criteria

The decision criterion presented by Walker et al (2010) was based on the DNPV, but, when considering the random nature of many variables involved in the storage management (e.g., the failures of disks and their future prices), the DNPV is not a single value but a random variable itself. We need to de<sup>fi</sup>ne a decision criterion to use in a more realistic random context. In this section, we de<sup>fi</sup>ne two criteria based on the mean value and the median value of the DNPV, respectively.

In a deterministic context, the decision criterion led to buy disks if DNPV > 0, as de<sup>fi</sup>ned in Eq. (14), and to lease the storage space in the opposite case. When taking into account the random nature of the DNPV, we need to identify a single measure of its distribution, which accounts for the location of the bulk of the DPNV values. The two most important location parameters of a probability distribution are the mean and the median value.

The mean value DNPV provides us with the value whose squared distance from the observed DNPV values is minimum. Instead, the median value DNPV<sup>d</sup> minimizes the absolute deviation from all the observed values.

The corresponding decision criteria are formulated as follows using the mean and the median, respectively:

$$
\overline {{D N P V}} = \left\{\begin{array}{l l}\geqslant 0&\rightarrow B U Y\\<   0&\rightarrow L E A S E\end{array}\right.\tag{16}
$$

$$
\widehat {D N P V} = \left\{\begin{array}{l l}\geqslant 0&\rightarrow B U Y\\<   0&\rightarrow L E A S E\end{array}\right.\tag{17}
$$

Using the mean criterion leads to a positive return on the average, while with the median we are right at least 50% of the cases. The most useful property of the median is that it is quite insensitive to outliers. In this context, this represents a protection against being in<sup>fl</sup>uenced by exceedingly large, though very unlikely, values of the DNPV.

## Migration risk

We have just described two decision criteria that should help a company in determining which of the two alternatives (Buy or Lease) is more pro<sup>fi</sup>table. But the scenario we have sketched through the models of previous sections is unavoidably affected by random events: storage requirements, disk sizes, disk prices, cloud prices refer to the future, and we can just formulate forecasts for them. The decision taken by either criterion de<sup>fi</sup>ned in the previous section relies on an aggregate measure of the DNPV, which accounts for each random event through its probability. But events that lead to a DNPV of different sign than what the aggregate measure predicts are possible. In that case, the company’s decision turns wrong and an opportunity loss takes place: if the company decided to stay with its own storage facility, it would have better migrated to the cloud, or vice versa.

The possibility of wrong decisions and the associated losses represents a risk for the company. In order to evaluate the quality of the decision criterion, we need a risk measure. The <sup>fi</sup>nancial sector provides us with several possibilities, which we can apply to our context, as we have taken an economics-based approach to our evaluation task. In this section, we describe three risk measures, namely, the probability of error, the VaR, and the CVaR.

Finally, we apply these measures in several scenarios to arrive at a comprehensive evaluation of the quality of the two decision criteria.

Table 3 Outcomes of migration decisions

<table><tr><td></td><td>Buy</td><td>Lease</td></tr><tr><td>DNPV&gt;0</td><td>Right</td><td>Wrong</td></tr><tr><td>DNPV&lt;0</td><td>Wrong</td><td>Right</td></tr></table>

## Risk measures

As just stated, we associate the risk to the event that we take the wrong migration decision. For that purpose, we consider three measures of risk:

● Probability of error

● VaR

● CVaR

In order to de<sup>fi</sup>ne the <sup>fi</sup>rst indicator, we consider Table 3, where we have described all the events that may take place when applying either decision criterion. The columns represent the two alternative decisions we take, according to the value of the mean or median DNPV. The rows represent the actual value of DNPV as it has unfolded over the years. We are wrong whenever the signs of the expected (mean or median) aggregate indicator and the actual DNPV disagree. Since the resulting four cases form a partition of the outcome-decision plane, the error probability $\mathbb { P } _ { e r r }$ is the sum of the probabilities of the two mutually exclusive events, that is, the probability that the DNPV turns out to be positive after deciding to lease plus the probability that the DNPV turns out to be negative after deciding to buy:

$$
\mathbb {P} _ {\text { err }} = \mathbb {P} [ D N P V > 0 \mid L E A S E ] + \mathbb {P} [ D N P V <   0 \mid B U Y ].\tag{18}
$$

It is to be noted that this indicator does not associate any money value to the wrong decision: the company could be wrong even by an extremely low amount, so to make the two decisions practically equivalent.

For that reason, a more meaningful indicator should take into account the distribution of the opportunity loss, or, equivalently, the distribution of the DNPV. An established indicator in the <sup>fi</sup>nancial market to describe the risk incurred by a company holding a marketed asset is the VaR. The exact de<sup>fi</sup>nition of VaR involves the probability distribution of the loss J. With a con<sup>fi</sup>dence level α the VaR is de<sup>fi</sup>ned as a quantile of the loss distribution (McNeil et al, 2005):

$$
\begin{array}{l l} V a R _ {\alpha} = \inf \{l \in \mathbb {R} & : \mathbb {P} [ J > l ] \leqslant 1 - \alpha \} \\ = \inf \bigl \{l \in \mathbb {R} & : F _ {J} (l) \geqslant \alpha \bigr \}. \end{array}\tag{19}
$$

The value of $V a R _ { \alpha }$ is then the maximum loss that is incurred in the 100α% of the cases. If α is very close to 1, the VaR is a proxy for the maximum loss. Typically, the con<sup>fi</sup>dence level is set as $\alpha { = } 0 . 9 5$ or 0.99.

In our context, we consider the distribution of the DNPV rather than the distribution of losses. In order to highlight the worst 100(1 α)% of cases, we have to take into account the sign of the decision variable. The de<sup>fi</sup>nition of the VaR, when we use the median DNPV becomes

$$
V a R _ {\alpha} = \left\{ \begin{array}{l l} \inf \{l: \mathbb {P} [ D N P V <   - l ] \leqslant 1 - \alpha \} & \text { if } D \widehat {D N P V} > 0 \\ \inf \{l: \mathbb {P} [ D N P V > l ] \leqslant 1 - \alpha \} & \text { if } D \widehat {D N P V} <   0. \end{array} \right.\tag{20}
$$

A similar expression applies when we use the mean DNPV rather than median, just by replacing DNPV<sup>d</sup> with DNPV. As we are considering the distribution of the DNPV− rather than that of losses, the VaR, as de<sup>fi</sup>ned by Eq. (20), may turn out to be negative. In that case, the probability of loss is lower than 1 α.

Though widespread among practitioners, the VaR has several shortcomings. A survey of the criticisms, with some indications about better risk measures, is reported by Szegö (2005). A major issue is the fact that the VaR does not say anything about the extreme values of losses: the actual loss could be much larger than the VaR. A measure of risk that solves that problem (and exhibits other theoretical properties that a risk measure should exhibit and the VaR does not) is the CVaR, which is also known as Tail Valueat-Risk or Expected Shortfall. The CVaR is the expected value of the losses exceeding the VaR

$$
\mathrm{CVaR} = \frac {1}{1 - \alpha} \int_ {\alpha} ^ {1} \mathrm{VaR} _ {u} d u,\tag{21}
$$

which we can apply to our DNPV-based context by− − employing the de<sup>fi</sup>nition (20) of the VaR. As for VaR, if the CVaR is negative, the probability of a loss is lower than 1 α, and, in the worst 100(1 α)%, losses are exceeded by gains.

So far, we have de<sup>fi</sup>ned three measures of the quality of the decisions taken by the decision criteria we have adopted. These measures have been given in order of increasing meaningfulness: each measure corrects some shortcoming of the previous one. However, they emphasize a different aspect of the problems incurred in the decision to migrate to the cloud. In the following, we will adopt all of them to analyse the behaviour of the decision criteria in realistic scenarios.

## Risk analysis

We now turn to compare the decision criteria in a realistic scenario through the risk indicators just de<sup>fi</sup>ned. We set the values of the parameters as reported in Table 4, following in the steps of Walker et al (2010). The value of the discount rate depends on the economic cycles (it tends to be higher in a expansive phase and lower in a recessive phase) and on the risk associated to the activity at hand. At present, the yield expected of a 10-year U.S.A. Treasury note is roughly 2%. Considering a risk premium of 3% gives us an overall discount rate k = 5%. As to the racking space rental, we employ values rather typical of the present situation (see, e.g., the detailed analysis performed in Patel & Shah, 2005), which lead to a yearly cost of \$2.5 per disk. In order to account for the randomness of failure phenomena, we employ a straightforward MonteCarlo simulation with 1,00,000 simulation runs for each case.

Table 4 Simulation scenario

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>CAGR for memory gm</td><td>0.7</td></tr><tr><td>Initial disk capacity [TB]</td><td>2–20</td></tr><tr><td>CAGR for disk size gc</td><td>0.3</td></tr><tr><td>Disk power [kW]</td><td>0.01</td></tr><tr><td>Controller cost [$]</td><td>2000</td></tr><tr><td>Controller power [kW]</td><td>0.7</td></tr><tr><td>Energy cost [$/kWh]</td><td>0.04</td></tr><tr><td>Salvage factor γ</td><td>0.1</td></tr><tr><td>Personnel cost Ht [$]</td><td>70000</td></tr><tr><td>Personnel factor λ-φ</td><td>1</td></tr><tr><td>Marginal failure probability</td><td>0.03</td></tr><tr><td>Leasing surcharge η</td><td>30</td></tr><tr><td>Transfer and Management cost factor τ [$/GB]</td><td>0.1</td></tr><tr><td>Rental fee [$/m2]</td><td>50</td></tr><tr><td>Rack footprint [m2]</td><td>2.5</td></tr><tr><td>Rack capacity [disks per rack]</td><td>500</td></tr><tr><td>Time horizon [years]</td><td>5–15</td></tr><tr><td>Discount rate k</td><td>0.05</td></tr></table>

![](/api/attachments/U8BVGZHH/fulltext/images/9e763f208b51997dae9749940236ac46c49821707b8ee9293271e8821e5629e0.jpg)  
Figure 1 Memory size and DNPV.

Here, we report in particular the impact of the size of the company examining the migration to cloud storage and the length of the time horizon. The size of the company is embodied by its storage requirement, precisely the initial memory requirement, for which we consider the range from 2 to 20 TB. The time horizon is set to 10 years.

In Figure 1, we show the values of the two decision variables: the mean and median DNPV. Both grow with the storage requirements, indicating that the migration is preferable for smaller companies, while larger companies had better buy their own storage infrastructure. On the same graph, we have plotted the zero line, which marks when the Buy decision gets preferable. The mean DNPV crosses that zero line earlier than the median DNPV: the use of the mean as a decision criterion favours the Buy decision.

We examine now how the company’s size impacts on the risk. In Figure 2, we consider the <sup>fi</sup>rst of the three risk indicators we have described in the previous section: the probability of taking the wrong decision. As expected, the decision is quite safe when the company is either very small or very large. At the two extremes (initial size of 2 TB and 20 TB, respectively), the error probability is, respectively, $5 \times 1 0 ^ { - 4 }$ and negligible. This probability grows as we get closer to the size values for which the decision is more uncertain (i.e., those where the aggregate DNPV is closer to zero). The error probability is equal for the two decision criteria for most sizes, but we note a different behaviour in the region of greater uncertainty. While the error probability cannot be larger than 50% when we employ the median DNPV, it grows to nearly 60% when we use the mean DNPV. For a small percentage of cases, the mean criterion leads us to err more often than the median.

![](/api/attachments/U8BVGZHH/fulltext/images/bc70b3b7675ebd4f3d22c9bf587d59f9ba3305a811085d46e1b24da40305eb13.jpg)  
Figure 2 Probability of taking the wrong decision.

![](/api/attachments/U8BVGZHH/fulltext/images/d93c2c4d5646232b805c62c9c97580a8552b0fd61eadce08f61e61090fbf6983.jpg)  
Figure 3 Value-at-Risk (95%).

However, we recall that the error probability does not consider the amount of money that is lost when we take the wrong decision. Actually, we note that the largest values of the error probability are incurred when the aggregate DNPV is close to zero. In order to examine the amount of losses we <sup>fi</sup>rst plot the VaR. In Figure 3, we show the 95% VaR. We observe the same trend as the error probability: low values on the tails and large values near the zero DNPV line. However, in the region of greater uncertainty, it is now the median DNPV that exhibits the worse behaviour. Though the two decision criteria bear the same risk for most sizes. the mean DNPV is the less risky on the overall. As previously mentioned, the negative values appearing in Figure 3 signal that the probability of a real loss is lower than 5%.

![](/api/attachments/U8BVGZHH/fulltext/images/d7e0f58c60512036184742e5b7bc225b5667ebcf422dc8215fefdeaeb105e00a.jpg)  
Figure 4 Conditional Value-at-Risk (95%).

![](/api/attachments/U8BVGZHH/fulltext/images/cc53062822a4ae258aac59d9c0f2885e12772cd92be3a92fc3d6f3b42b6ddfc8.jpg)  
Figure 5 Evolution of the DNPV over the years.

If we turn to the last risk indicator, the CVaR de<sup>fi</sup>ned by Eq. (21), we obtain the curves reported in Figure 4, which con<sup>fi</sup>rm the superiority, though strict just for a small number of cases, of the mean DNPV as a decision criterion.

We can now examine the impact of time horizon. As stated in Mastroeni & Naldi (2011a), cloud migration must be examined in the long run. The presence of lock-in phenomena and the one-off operational cost of moving make short-term moves unfeasible. We consider a time horizon from 5 to 15 years. For the parameter values reported in Table 4, we consider an initial memory requirement of 5 TB to illustrate the passage from Lease to Buy.

![](/api/attachments/U8BVGZHH/fulltext/images/db9863589510c767a006f613b8877fcc8c0c7c2551ac94ed409e3c19f9798711.jpg)  
Figure 6 Error probability and time horizon.

In Figure 5, we see how the two aggregate indicators of the DNPV change when we lengthen the time period over which we evaluate migration. A longer time horizon favours the Buy decision. If we use the mean DNPV, the limit time horizon marking the passage is shorter.

![](/api/attachments/U8BVGZHH/fulltext/images/d9a72265be965892206736c56a5ed233c5114d2616f191709ecb02c1443e2499.jpg)  
Figure 7 Impact of time horizon on the VaR (95%).

In order to compare the two decision criteria, we now assess the risk. We start with considering the error probability, shown in Figure 6. We see a pattern similar to what we found when considering the impact of the company’s size. The two indicators bear the same error probability nearly all over the range but the region of greater uncertainty (where the DNPV is close to zero), where the criterion based on the mean leads us to err more frequently.

But, if we turn to the measure of the actual loss, we see in Figure 7 that the mean DNPV leads to a lower VaR. This is con<sup>fi</sup>rmed if we also weigh the losses exceeding the VaR by using the CVaR <sup>fi</sup>gure of merit, as shown in Figure 8.

## Protection against migration risks

The analysis of the NPV has shown that any decision is subject to risk. Many variables entering the decision context are inherently stochastic and may lead to a different result than that predicted by either the mean or the median DNPV. For example, pricing plans may change; though we do not expect changes to take place on a daily or monthly basis, the time horizon considered in any migration analysis is long enough to include one or more changes in pricing plans. The company considering migration to the cloud may seek protection against the risks associated to these changes. Real options are an established tool to deal with contingencies. Mastroeni & Naldi (2012b) employed a real option analysis to protect through an insurance policy against price changes departing from the expected trend. But changes may take place not just in pricing plans. For example, the company’s memory needs may change with respect to the plan, or the cost of disks may change. In this section, we consider again the real option framework to protect the migrating company against the overall risk of a wrong decision. We adopt the real options approach to formulate an insurance policy and determine the fair price a migrating company should pay to protect itself against that risk.

![](/api/attachments/U8BVGZHH/fulltext/images/e68e8cb068e24af4bad00d95564a05bb5aa564c1ac1162144d791919f1f21189.jpg)  
Figure 8 Impact of time horizon on the CVaR (95%).

We see <sup>fi</sup>rst how the risk protection problem can be formulated through a real options approach. We have adopted the DNPV as the leading indicator to decide for either solution. The DNPV is actually made of two components, the NPVs associated to the Buy and the Lease solution, respectively, which are stochastic quantities and change as time proceeds. If we stick to the mean DNPV as the migration criterion (as suggested in the previous sections), we migrate when DNPV<0 and build an in-house storage infrastructure otherwise. Though− − DNPV<0 (DNPV>0), it may turn out that $N P V _ { B u y } >$ $N P V _ { L e a s e } \left( N P V _ { B u y } { < } N P V _ { L e a s e } \right)$ . If that’s the case, the decision turns into a loss $\jmath = N P V _ { B u y } - N P V _ { L e a s e } ( J = N P V _ { L e a s e } - N P V _ { B u y } ) .$ If the company wants to indemnify itself against the risk of incurring that loss, it must underwrite an insurance policy whose payoff is exactly that loss. In order to account for both possibilities, the company may therefore formulate a call option whose payoff C is

$$
C = \left\{ \begin{array}{l l} \max \bigl \{N P V _ {B u y} - N P V _ {L e a s e}, 0 \bigr \} & \text { if } \overline {{D N P V}} <   0 \\ \max \bigl \{N P V _ {L e a s e} - N P V _ {B u y}, 0 \bigr \} & \text { if } \overline {{D N P V}} > 0 \end{array} \right.\tag{22}
$$

The payoff described by Eq. (22) characterizes what is called a spread option. The option price Z represents the premium to pay to underwrite the insurance policy. Under the hypothesis that both the NPVs deriving from the two solutions follow an arithmetic brownian motion (which allows for either being negative), Poitras (1998) has provided a pricing formula, which we may adapt to the case at hand

$$
Z = - \left| \overline {{D N P V}} \right| G (\gamma) + Q g (\gamma),\tag{23}
$$

where G(⋅) and g(⋅) are, respectively, the cumulative distribution function and the probability density function of the standard normal variable, and the two quantities Q and y are de<sup>fi</sup>ned as

$$
Q = \sigma \sqrt {\frac {1 - e ^ {- 2 r T}}{2 r}},\tag{24}
$$

$$
\gamma = \frac {\overline {{D N P V}}}{Q},\tag{25}
$$

with T being the time horizon considered for the evaluation of the migration decision, r being the risk-free interest rate, and σ being the standard deviation of DNPV.

We can now apply the pricing formula (22) to the scenario of Table 4. We report <sup>fi</sup>rst the resulting premium (the insurance policy price) in Figure 9. Since a longer time horizon allows for a greater variability of all the variables at hand, we expect the risk of having a downturn to grow with the expiration time of the insurance policy. Actually, we see that the premium grows with the expiration time. The growth trend is rather linear for the case of larger companies (here represented by the 10 TB initial memory requirement).

But since the payoff is paid when the prospected bene<sup>fi</sup>t does not materialize, we should compare the price paid for protection against that bene<sup>fi</sup>t, that is, the DNPV we expect from the migration decision. In Figure 10, we plot the ratio of those two quantities. A price/bene<sup>fi</sup>t ratio quite smaller than 1 indicates that the policy is an affordable means to hedge. On the other hand, if that ratio is larger than 1, the company is asked to pay a price for protection that is even larger than the expected bene<sup>fi</sup>t. In that case, the insurance policy is probably not worth underwriting. We see in 10 that the trend is different for the two initial memory sizes. In the case of the smaller company, the policy gets more and more costly as the policy expiration date extends in the future, as a longer horizon brings more risks. But in the larger company case, that trend is reversed, because extending the time horizon may also lead to increased advantages from migration. Actually, the DNPV grows with the time horizon as well as the insurance premium. The trend observed for their ratio is therefore largely a function of the speci<sup>fi</sup>c scenario.

![](/api/attachments/U8BVGZHH/fulltext/images/117d1d2fde8956b3c9b1cb132fc75d618fecff0a9d506de6f2fb784f1e874b7c.jpg)  
Figure 9 Insurance premium.

![](/api/attachments/U8BVGZHH/fulltext/images/3b917937f6854ed418e69f8a83ad18fd123e91ae01a57d13387fd23e6461338b.jpg)  
Figure 10 Normalized insurance price.

![](/api/attachments/U8BVGZHH/fulltext/images/addc98bc6e080c5470726e938dee79ccf71f6f6e452fb530624850730bb2f38e.jpg)  
Figure 11 Insurance price and error probability.

Finally, the payoff is paid when the net balance between the NPVs associated to the two alternative migration decisions turns out to have a sign different than the expected one, that is, when the migration decision has been wrong. We can then relate the opportunity to underwrite the insurance policy to the probability of taking the wrong migration decision, shown in Figures 2 and 6. In Figure 11, we see that greater chances of wrong decisions are accompanied by a larger insurance premium.

## About the Authors

<sup>Maurizio Naldi</sup> has been a tenured Aggregate Professor of ICT Economics at the University of Rome at Tor Vergata

## Conclusions

The migration to cloud storage requires a preliminary economical analysis, which should consider a long time horizon and account for the uncertainty related to the evolution of prices and storage needs. We have formulated a set of probabilistic models that allows us to perform that analysis and compare two alternative decisions: buy a storage infrastructure or use the storage service offered by a cloud provider. We have proposed two decision criteria, which employ, respectively, the median and the mean value of the DNPV, as aggregate indicators of the differences between the costs associated to the two alternatives. The comparison of the two aggregate indicators through three risk measures suggests that the mean DNPV is the less risky decision criterion, though the difference is limited to the region of greater uncertainty, where both indicators are close to zero. The application of the decision criterion to a realistic scenario shows that large companies with a long time horizon should opt to buy and run their own storage infrastructure. We have <sup>fi</sup>nally provided a formula for pricing an insurance policy to protect against the risk of taking the wrong decision. The price turns out to be rather affordable for smaller companies and over a limited time horizon.

It is to be noted that our approach considers the direct economic impact of migration to the cloud. A wider view should consider also organizational issues and minor sources of economic differences between the two decisions. While this affects the number and type of terms that come into the balance equation, we expect that they can be dealt with through the same NPV-based comparison approach we have adopted here. Another issue that deserves to be investigated is the nature of risks and the mathematical models adopted to analyse them and de<sup>fi</sup>ne the pertaining countermeasures. Mastroeni & Naldi (2012b) have investigated the possibility to insure against pricing changes. Here we have taken a more holistic approach, considering an arithmetic brownian motion as a model for the NPVs incurred under the two decisions, without delving into the details of what may alter the NPV over time. The speci<sup>fi</sup>c nature of the risks we have to face when deciding for either solution (leasing vs buying) has, however, to be taken into account, with possible deviations from the speci<sup>fi</sup>c stochastic model we have adopted here. This latter issue is probably the most relevant to deal with and <sup>fi</sup>rst on the list of future research.

## Acknowledgements

This work was supported in part by the Italian Ministry of Education, University, and Research (MIUR) under PRIN 2012C4E3KT national research project AMANDA – Algorithmics for MAssive and Networked DAta.

since 2000. Prior to moving to academia, he pursued an industrial career over 12 years in several telecommunications companies and was an Associate Rapporteur at ITU in Geneva. He holds a PhD in telecommunications and an MS degree magna cum laude in Electronic Engineering. His current research interests lie in the <sup>fi</sup>elds of network and service economics as well as computational statistics.

<sup>Loretta Mastroeni</sup> has a magna cum laude degree in Mathematics and is currently Associate Professor of

## References

ABU-LIBDEH H, PRINCEHOUSE L and WEATHERSPOON H (2010) Racs: a case for cloud storage diversity. In Proceedings of the 1st ACM Symposium on Cloud Computing, SoCC 2010, pp 229–240, ACM Publications, Indianapolis, Indiana, USA.

BHATTACHERJEE A and PARK SC (2014) Why end-users move to the cloud. European Journal of Information Systems 23(3), 357–372.

CHAN NH and WONG HY (2006) Simulation Techniques in Financial Risk Management. John Wiley, Hoboken, NJ.

COUGHLIN T (2003) Current trends in data storage backup and restoration. Graduate Engineering Seminar, Santa Clara University. [WWW document] http://www.tomcoughlin.com/Techpapers/SCU%20Backup% 20Presentation,%20021303.pdf (accessed 22 July 2014).

ELEFTHERIOU E, HAAS R, JELITTO J, LANTZ MA and POZIDIS H (2010) Trends in storage technologies. IEEE Data Engineering Bulletin 33(4), 4–13.

GREENBERG AG, HAMILTON JR, MALTZ DA and PATEL P (2009) The cost of a cloud: research problems in data center networks. Computer Communication Review 39(1), 68–73.

HILBERT M and LÓPEZ P (2011) The world’s technological capacity to store, communicate, and compute information. Science 332(6025), 60–65.

K MM and A J (2011) A cost model for hybrid clouds. TEMEP Discussion Paper 2011:82, Seoul National University, College of Engineering Technology Management, Economics, and Policy Program.

K -H A, G D, S JW and S I (2012) The cloud adoption toolkit: supporting cloud adoption decisions in the enterprise. Software, Practice and Experience 42(4), 447–465.

KHAN SS, KHOUJA MJ and KUMAR RL (2013) Effects of time-inconsistent preferences on information technology infrastructure investments with growth options. European Journal of Information Systems 22(2), 206–220.

LAATIKAINEN G, MAZHELIS O and TYRVÄINEN P (2014) Role of acquisition intervals in private and public cloud storage costs. Decision Support Systems 57(1), 320–330.

LENK A, KLEMS M, NIMIS J, TAI S and SANDHOLM T (2009) What’s inside the cloud? An architectural map of the cloud landscape. In Proceedings of the 2009 ICSE Workshop on Software Engineering Challenges of Cloud Computing, CLOUD ‘09, pp 23–31, IEEE Computer Society, Washington DC, USA.

LI H, ZHONG L, LIU J, LI B and XU K (2011) Cost-effective partial migration of vod services to content clouds. In IEEE International Conference on Clouo Computing, CLOUD 2011, pp 203–210, IEEE, Washington DC, USA.

MAKARENKO AV (2011) Phenomenological model for growth of volumes digital data. CoRR, abs/1102.5500. arXiv preprint series.

Mathematical Finance at the University Roma Tre, Department of Economics. Her research interests focus on <sup>fi</sup>nancial risk management, energy <sup>fi</sup>nance, <sup>fi</sup>nancial models in telecommunications and cloud computing. She is the author of several publications. She is currently an expert evaluator for European projects and is engaged in a number of research projects. She acts as a referee for a number of peer-reviewed journals.

MASTROENI L and NALDI M (2011a) Long-range evaluation of risk in the migration to cloud storage. In 13th IEEE Conference on Commerce and Enterprise Computing, CEC 2011, pp 260–266, IEEE, Luxembourg.

MASTROENI L and NALDI M (2011b) Storage buy-or-lease decisions in cloud computing under price uncertainty. In 7th EuroNF Conference on Next Generation Internet, IEEE, Kaiserslautern.

MASTROENI L and NALDI M (2012a) Analysis of cloud storage prices. arXiv preprint series, CoRR. Preprint no. 1207.6011v1.

MASTROENI L and NALDI M (2012b) Pricing of insurance policies against cloud storage price rises. SIGMETRICS Performance Evaluation Review 40(2).42-45.

MCNEIL AJ, FREY R and EMBRECHTS P (2005) Quantitative Risk Management: Concepts, Techniques and Tools. Princeton Series in Finance. Princeton University Press, Princeton, NJ.

NALDI M (2014) Forecast uncertainty in procurement decisions for cloud storage. In 2014 UKSim-AMSS 16th International Conference on Computer Modelling and Simulation, pp 237–242, IEEE, Cambridge, UK.

NALDI M and MASTROENI L (2013) Cloud storage pricing: a comparison of current practices. In HotTopiCS Workshop, Colocated with the 4th ACM/ SPEC International Conference on Performance Engineering ICPE, pp 27–34, ACM Publications, Prague.

NEWMAN DG, ESCHENBACH TG and LAVELLE JP (2004) Engineering Economic Analysis, 9th edn, Oxford University Press, Oxford, UK.

PATEL CD and SHAH AJ (2005) Cost model for planning, development and operation of a data center. Technical Report HPL-2005-107R1, HP.

PINHEIRO E, WEBER WD and BARROSO LA (2007) Failure trends in a large disk drive population. In 5th USENIX Conference on File and Storage Technologies, FAST 2007, pp 17–28, USENIX, San Jose, CA, USA.

POITRAS G (1998) Spread options, exchange options, and arithmetic brownian motion. The Journal of Futures Markets 18(5), 487–517.

SCHROEDER B and GIBSON GA (2007) Disk failures in the real world: what does an MTTF of 1,000,000 hours mean to you? In 5th USENIX Conference on File and Storage Technologies, FAST 2007, pp 1–16, USENIX, San Jose, CA, USA.

SZEGÖ G (2005) Measures of risk. European Journal of Operational Research 163(1), 5–19.

VV.AA. (2014) The digital universe of opportunities. Technical Report, EMC-IDC.

WALKER E, BRISKEN W and ROMNEY J (2010) To lease or not to lease from storage clouds. IEEE Computer 43(4), 44–50.
