---
otero_id: 12642
otero_key: "E836AV5V"
title: "Going the last mile: A spatial decision support system for wireless broadband communications"
authors: "Kevin P. Scheibe; Laurence W. Carstensen; Terry R. Rakes; Loren Paul Rees"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.02.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Going the last mile: A spatial decision support system for wireless broadband communications

Kevin P. Scheibe<sup>a,\*</sup>, Laurence W. Carstensen Jr.<sup>b</sup>, Terry R. Rakes<sup>c</sup>, Loren Paul Rees<sup>c</sup>

<sup>a</sup>Department of Logistics, Operations, and Management Information Systems, College of Business, Iowa State University, 2340 Gerdin Business Building, Ames, IA 50011-1350, USA

<sup>b</sup>Department of Geography, Virginia Polytechnic Institute and State University, Blacksburg, VA 24061, USA

<sup>c</sup>Department of Business Information Technology, Virginia Polytechnic Institute and State University, Blacksburg, VA 24061, USA

Available online 17 May 2005

## Abstract

High-speed, wireless communication networks are increasing in popularity; however they can be costly and difficult to plan. In this paper we present a spatial decision support system that incorporates expert knowledge of wireless communications, area topography, demographics and propensity to pay for service in order to aid wireless network planners determine optimal placement of equipment to maximize profit or minimize cost. Moreover, the system can be useful in performing policy analysis to determine pricing, governmental subsidy levels, etc. By integrating a GIS tool into the DSS, planners can easily adjust parameters to better understand the problem at hand and move toward bringing broadband connectivity to the last mile. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: GIS; Spatial decision support; Broadband wireless communication; Last mile

## 1. Introduction

Broadband communication continues to gain popularity among individual consumers and small offices and home offices, yet a majority of American households are left asking why they cannot have high-speed Internet service [11] and many of the remainder wonder why they have so few choices of broadband service providers or why such service is so expensive. The United States has a transcontinental fiber optic infrastructure that investors have poured US\$90 billion into, yet today a mere 3% of that backbone is in use—it is the <sup>b</sup>digital equivalent of fallow farmland [23].<sup>Q</sup> The problem is that entrepreneurs failed to foresee the enormous cost of upgrading the <sup>b</sup>last mile— copper telephone wires that connect individual homes and small businesses to the broadband backbone [23].<sup>Q</sup> Although most Americans live within 1 mile of the broadband backbone and nine out of ten American businesses with more than 100 workers are also within 1 mile of the backbone, the cost of laying or upgrading existing cables for that last mile is prohibitive [1].

TechNet, a bipartisan group comprising more than 300 chief executive officers and senior partners of the major companies in the fields of information technology, biotechnology, venture capital, investment banking and law, claims that (1) <sup>b</sup>widespread adoption of true broadband will increase the efficiency and productivity of Americans at work and at home—with a potential US\$500 billion impact on the United States economy. The benefits to quality of life are immeasurable,<sup>Q</sup> and that (2) true broadband is the key to the next generation of communications and Internet services [42]. They have called on the President and policymakers to make broadband a national priority and to set a goal of making affordable 100- Mbps broadband connections available to 100 million American homes and small businesses by 2010. They note that to achieve the 100 million homes goal will require network providers to invest hundreds of billions of dollars to upgrade infrastructures and increase bandwidth capacity in the last mile, primarily by providing new fiber connections to homes and offices. Today, virtually no homes have connections with such bandwidth. An intermediate goal is the <sup>b</sup>availability of affordable broadband at speeds of at least 6 Mbps from 2 or more providers to at least 50% of U.S. households and small businesses by 2004 [42].<sup>Q</sup>

Copper wires and coaxial cables connecting buildings do not possess the gigabit per second capacity necessary to carry advanced bandwidth-intensive services and applications, whereas optical fiber bridges needed to connect millions of users to the optical-fiber backbone would cost too much to install. As these costs are prohibitive, service providers are looking to other transmission media and in particular to wireless telecommunications. Ref. [50] cites an example whereby a fiber potential cost of US\$400,000 was reduced to US\$60,000 with a wireless system. However, simply installing wireless networks does not ensure profitability. Proper wireless network planning is crucial and the planning must include more than just technical viability; profitability must be explicitly addressed in network planning.

Broadly speaking, the focus of this research is integrating a geographic information system (GIS) with a decision support system (DSS) for the purpose of planning broadband fixed wireless telecommunication networks. In particular, this paper examines the wireless provision of broadband service to homes and small businesses using current costs and technologies. Because the wireless technologies require <sup>b</sup>line of sight<sup>Q</sup> (LOS) or <sup>b</sup>near line of sight<sup>Q</sup> operation, it will be necessary to develop a special-purpose GIS and then integrate it with the mathematical programming formulation we derive. The spatial decision support system (SDSS) we build will be useful in two main capacities: (1) to determine the best site location under a given economic strategy and (2) as a managerial tool to perform economic policy analysis that examines various economic strategies. To illustrate these capabilities, solutions will be generated for both <sup>b</sup>for profit<sup>Q</sup> and government-subsidized scenarios. Finally, the SDSS developed here will be demonstrated for a rural county in the mid-Atlantic region of the United States and several implications will be drawn for the last mile problem and for the spatial augmentation of DSS for addressing this planning problem.

## 2. Background

Broadband is the capacity to deliver Internet access with a continuous <sup>d</sup>always on<sup>T</sup> connection and the ability to both receive and transmit digital content or services at high speeds [42]. Although other definitions of the term abound, most agree with this one— except as to what precisely is meant by high speeds. Today, approximately only 4.4% of American households have speeds approaching 400 Kbps [42]. In order to facilitate telecommuting, it is estimated that speeds of 10 Mbps will be required and many experts have defined 100 Mbps as the speed at which the web’s true potential can be achieved [42].

## 2.1. Wireless telecommunication

For years, many consumer devices such as AM/FM radio, cordless and cellular phones, satellite television, CB radios, pagers, car alarm signalers, garage door openers, and television remote controls have applied wireless technology. More recently, wireless computer networking has grown in popularity. People are installing wireless local area networks (LAN) in their homes and businesses. Coffee shops, book stores, restaurants, truck stops, and airports are installing hotspots or local access points to attract and entertain patrons [24,31,34,37]. If users have wireless access cards in their computer or PDA, then they can access the Internet either for free or a modest fee. These access points operate in a frequency range that is typically license-free and relatively low in throughput and LOS from the access card to the access point is not necessary. As frequencies increase, requisite bandwidth becomes greater, license fees may exist, and LOS becomes essential. At a higher end of the current frequency spectrum are technologies such as local multipoint distribution services (LMDS) [20,33,43], microwave, and laser [1]. These wireless technologies offer very high bandwidth (fiber optic levels), are more expensive, and are very constrained by visibility or LOS (i.e., the LOS constraint becomes a critical issue with fixed wireless networks because any obstruction between the transmitter and receiver will block the signal and disrupt the connection).

## 2.2. Wireless systems

Operationally, wireless radio systems may be classified along several dimensions. The systems we explore here are fixed, point-to-multipoint (PMP) systems. <sup>b</sup>Fixed<sup>Q</sup> wireless networks are those where the transmitter and receiver locations are fixed, as opposed to mobile networks, such as utilized with cellular telephones. PMP networks are those where a single source (in our case an antenna or antennas on top of a tower) connected to a backbone network propagates signal to multiple customers (in our case, receiving antennas located at customer premises). See Fig. 1 for an example PMP network.

Other architectures exist, such as multipoint-tomultipoint networks or mesh networks [12,51], whereby multiple sources at different locations all transmit signal to perhaps the same customers. However, these are beyond the scope of this paper.

## 2.3. Differences among wireless systems

It might be supposed that one could apply directly a solution methodology from cellular telephone networks to the wireless network determination problem. Such is not the case, however, because of three primary differences between the two wireless technologies. First, the receivers in the cell phone scenario are mobile, allowing users to switch from one tower to the next as they travel; utilizing the same frequencies at adjacent towers is not a problem. This is not the case with broadband. Second, the expectations in terms of service level are much higher for broadband (the socalled <sup>b</sup>five nines<sup>Q</sup>—99.999% reliability), as opposed to cell phone users accustomed to breakup, callbacks, and frequent fading and/or loss of signal. Third, the transmission range from towers for cell phones is much greater than for broadband because cell phone frequencies are much lower. Consequently, to determine a broadband distribution network requires the ability to position towers in locations that guarantee reliable LOS transmission. To make this determination, we turn to GIS and DSS.

![](/api/attachments/E836AV5V/fulltext/images/f1dd151aacc53e3eafaf271fd1925219134f928075958aa591771a3d92156fc0.jpg)  
Fig. 1. Example of a wireless PMP network.

## 2.4. Geographic information systems and decision support systems

Decision support systems has been a topic of ongoing research for the past 30 years. Using data, model and user interface components, DSS aid decision makers to solve semi-structured or unstructured problems [6] and cover all phases of Simon’s [36] decision-making process. Unstructured decisions are defined as those for which no algorithm can be written, whereas algorithms can be specified for structured decisions [21]. Semi-structured decisions fall between the other two.

GIS are used to collect, store, retrieve, and analyze spatial data and can provide decision support. GIS link tabular data to graphical data by relating graphical layers to database tables. For example, a demographic layer of a town map may have sections linked to economic information such as household income or school zoning information [10].

Marrying DSS and GIS creates spatial decision support systems (SDSS). The advantage of an SDSS is its ability to integrate the model portion of the DSS with the graphical representation of the GIS, thereby aiding decision makers with semi-structured or unstructured spatial problems. Ref. [9] determined that SDSS enabled decision makers to complete their tasks quicker, more efficiently, and with greater understanding of the problem through visualization.

SDSS is a relatively new research area, primarily because GIS software has historically needed a great amount of computing power, memory, and hard disk space. Since such equipment was very expensive, GIS software required large budgets. As computers have become cheaper and more powerful, GIS packages can now run on desktop computers creating more SDSS research possibilities. SDSS have been applied to (among others) siting problems [25,47], land planning [30], and vehicle routing [22,41]. Ref. [29] determined that as task complexity increased, SDSS enabled decision makers to be more efficient. Furthermore, it showed that when decision makers lacked expert knowledge of the problem, the SDSS enabled them to be more accurate in their decisions.

As part of the National Mapping Program, the United States Geological Survey (USGS) produces digital elevation models (DEM). A DEM is a digital file containing terrain elevation information that has been sampled at regularly spaced intervals and stored in raster (matrix of rows and columns) format. There are five DEM products for sale by the USGS, 7.5V, 7.5 Alaska, 15V, 2 arc sec, and 18. These five products fall into one of three different scale categories, large, medium, and small. Larger scale means greater map detail. The large-scale category includes 7.5V and 15 maps with ratios of 1 : 24,000 and 1 : 63,360, respectively; the medium-scale category includes 2-arc sec maps with a ratio of 1 : 100,000; and the small-scale category includes the 18 case with a ratio of 1 : 250,000.

The 7.5V DEM provides the greatest level of detail from the USGS with 30  30 m data spacing. These maps are produced either by digitizing cartographic map contour overlays or by scanning photographs from the National Aerial Photography Program [44].

One of our coauthors, under a National Science Foundation grant, built a special-purpose GIS specifically engineered to analyze wireless systems. In this research we use this system, called the Geographic-Engineering Tool for Wireless: Evaluation of Broadband Systems (GETWEBS) [7]. GETWEBS was built starting with ESRI’s ArcView version 3.2 [10].

## 2.5. Tower location problems

The tower location problem, a problem we must solve to meet our SDSS’s dual purposes, is not new. There have been several variations in the literature and it is worth noting their similarities and dissimilarities to the approach discussed in this paper. First, the solution methodology for this problem has entailed integer programming models [3,27], stochastic methods [16], simulation [39], and heuristics [16,27,32,45]. Many of the approaches to solving tower location problems have focused primarily on the characteristics of the towers themselves, such as tower power [3], frequency and radio strength constraints [27,32], physical attributes of towers such as height and angle [2], and the mobility of the tower [5]. Another distinction among tower location problems is the type of network analyzed. Some authors focus on fixed wireless networks [2] (which is our focus as well), whereas others center on tower placement for mobile networks such as cellular telephones [3,5,13,16,45,49], ad hoc networks [15,28], and mobile user location within the network [4,8,14,32,39]. Interestingly, while all of the research mentioned have an implicit spatial component, either geography is a non-issue, as when the frequency is such that obstructions do not matter, or it has been addressed a priori to the point in which their research begins. Furthermore, most of the constraints presented in the aforementioned solutions are technical in an engineering sense, such as frequency, azimuth, power levels, etc. While some researchers do indicate that other constraints may be added, none addresses economics. Conversely, the methodology presented in this paper does not assume the terrain problem has already been solved; rather, it incorporates geography directly and spotlights the economic portion of the model, thereby making its solutions very relevant to decision makers interested in the bottom line.

## 3. A spatial decision support system

An optional component of a DSS is the knowledge component. It is here that a GIS really can bring power to an SDSS, although a GIS can serve in all component areas. The interface of a GIS is uniquely suited for addressing spatial problems and the functionality of a GIS can be used to solve spatial issues such as distance, proximity, coverage, etc. GETWEBS specifically incorporates expert knowledge concerning the characteristics of radio frequency ranges, visibility, and propagation. We modified and integrated GETWEBS into our SDSS as knowledge and data components. In particular, the modified GETWEBS system can determine the visibility over an area of any tower signal, given the height and tower location on a DEM, and the transmission signal strength. However, to use the original system, the user had to possess expertise in wireless communications as well as GIS. The GETWEBS tool is excellent for determining via trial and error where a tower ought to be placed to provide coverage for a particular area. It allows the network planner to view the terrain, determine logically intuitive tower locations, and calculate whether or not coverage is attainable in that configuration. If it is not, then the user can (guess and) adjust the location of the tower and recalculate. By itself, this tool has proven to be invaluable in planning specific wireless networks. But by integrating GETWEBS into an SDSS, we will show how we can determine the optimal number and placement of towers to create a wireless area network to reach the last mile given terrain, demographics, equipment cost, and profitability. Fig. 2 delineates how we integrated the spatial component into a traditional DSS architecture for wireless area network planning.

The data component of our SDSS is comprised of economic data, gathered or derived from census data, and from geographic data, such as topography and the location of customers. The GIS component of the DSS plays a large role in supplying data.

The model component of our SDSS consists of traditional mathematical programming techniques— in our case a variation of the set covering problem (discussed later), as well as GIS-based models such as distance, coverage area, and determination of visibility between two points. We built the SDSS to implement the mathematical modeling features with the GETWEBS geographic information system. The point to be noted here with this SDSS is that general modules have been/can be written to allow various equipment, forecasting, and financial modeling to be intertwined in the appropriate mix. A graphic description of the SDSS architecture we employed is shown in Fig. 3.

![](/api/attachments/E836AV5V/fulltext/images/4298be3b6105e955051b916660ea64ad5667b16d8555698cc9e81b5ad7ab2056.jpg)  
Fig. 2. The integration of the GETWEBS GIS into the spatial decision support system.

Fig. 3 shows three main paths to the (output) profit-shed module: from the visibility module, the revenue module, and the evaluation module. The visibility module consists of the equipment definition sub-module, and the view-shed sub-module. In addition to descriptive information on each type of equipment, the equipment sub-module contains technical capabilities, including the range, angle of transmission, and shape of the region covered by each antenna (e.g., circular, elliptical, etc.). The view-shed sub-module invokes GETWEBS and calculates exposure given the antenna specified and the terrain specified by the DEM. The revenue module includes the census data access and various marketing revenue sub-modules and the evaluation module contains the maximum profit and maximum exposure mathematical programming models (to be discussed) as well as requisite financial sub-modules.

The SDSS interface integrates the GETWEBS graphical program output with Microsoft Excel. Fig. 4 shows one screenshot from our SDSS interface.

The knowledge component of our SDSS is the knowledge that has been collected and implemented

![](/api/attachments/E836AV5V/fulltext/images/58ff9064a1458929debd97245005600918ab4ab0168c55870207062911d47980.jpg)  
Fig. 3. The wireless spatial decision support system architecture.

![](/api/attachments/E836AV5V/fulltext/images/ebffad4eb8df2f21d0cf9afcd7ba241d7233cb596205ddc77488ccad6da2a53a.jpg)  
Fig. 4. An SDSS screenshot, illustrating the system’s interface. The tower coverage window shown would actually be a GETWEBS display with an area broken down into discrete cells. This is a simple, example solution showing maximal profit coverage with a specific type of antenna and particular propensity to pay levels for different cells.

in the GETWEBS program itself. This knowledge is specific to the propagation of a wireless signal. Issues such as the curvature of the earth, dead spots or Fresnel zones, degradation of signal over distances, interference, etc., are some of the knowledge stored and utilized in the program.

## 4. Last mile modeling approach

Obviously the SDSS developed here can be used to analyze any situation for which costs and other data can be generated. The particular interest of this paper, however, is to demonstrate the SDSS in rural regions where the last mile problem is most difficult to solve economically. Unfortunately, rural areas are also faced with a paucity of data. Consequently, as will now be explained, first-cut approximations have been made in our data modeling. Results obtained must be properly couched in this context.

## 4.1. Visibility

Introducing the LOS requirement necessitates a fundamentally different analysis because terrain, buildings, and (sometimes) even trees must be considered. <sup>b</sup>Near<sup>Q</sup> line of sight is less restrictive. Signals still cannot go through large obstructions such as mountains; however, trees and smaller hindrances are not a problem. This means that DEM maps contain the topographic detail necessary to ascertain near LOS capability.

The visibility component of the SDSS performs two functions: defining the wireless equipment to be deployed and specifying a view shed. A view shed is that area which is visible, given a tower location and height on a DEM, and the transmission signal strength. Fig. 5 shows (superimposed on a DEM) the view shed, i.e., area that can see a tower’s transmission, in light grey, given the tower’s location and height (40 ft) in a moderately mountainous rural county in the mid-Atlantic United States. Note that a profit-shed may be defined as that region that can both see a tower’s signal and generate a profit for a service provider.

![](/api/attachments/E836AV5V/fulltext/images/5fcbae7a4e687cd1b75345b1c3121e605686d1ebf4d07edd01464364bddd13da.jpg)  
Fig. 5. A GETWEBS screen shot indicating the view shed (in light grey) of a tower placed at the dot in the center of the circle with range indicated by the circle.

## 4.2. Equipment definition

We examine the three fixed, PMP technological options currently considered most viable for bringing wireless broadband to an area: local multipoint distribution service (LMDS) [20,33,43], the 802.16 (WirelessMAN) standard, and 802.11 (Wi–Fi). The parameters we used are based on published data. LMDS operates in the 28 GHz band and can reach throughput levels of up to 2 Gbps. LMDS can service 80,000 customers with data and voice from a single node [48] and has a range up to 14 km [17]. LMDS can be quite costly with the cost of customer premise equipment (CPE) exceeding US\$1000 [26]. Wireless-MAN operates between 2 and 11 GHz, can transmit up to 75 Mbps, and has a range of up to 30 miles but typically has a cell radius of 4–6 miles [18,19]. Wi–Fi operates between 2.4 to 5 GHz, can transmit practically from 5 to 10 miles [38], and has a throughput of up to 11 Mbps (at the 802.11 b standard).

We use a range (i.e., transmission signal from the tower) of $5 \sqrt { 2 } \approx 7 . 1$ km. This value is within the scope of all three systems and is chosen because a tower placed at the center of a 2-km cell (this is a size choice we will explain later) can reach diagonally to all households two cells away. For all cases, we also assume four 908 sectored antennas at each tower, providing omnidirectional coverage.

Fixed, PMP systems incur a tower cost at the hub (the <sup>b</sup>point<sup>Q</sup>) as well as customer premise equipment costs (the <sup>b</sup>multipoints<sup>Q</sup>). Tower costs can vary widely, depending on location and terrain, and include components such as cost of land/right of way, structure, connecting the tower to the backbone, power, bringing power to the tower, antennas, and annual maintenance.

As the non-antenna costs dominate, it is a reasonable approximation to say the tower costs of all three technologies are the same and they will vary considerably depending on the location and accessibility to other infrastructure elements. Talks with those familiar with wireless installation costs suggested that installed tower costs would vary from a low of US\$100K to a high of US\$500K, with a most likely cost of US\$150K. Consequently, we model tower costs probabilistically, using a triangular distribution with three appropriate values as an approximation to the beta distribution in the same way that PERT/CPM uses estimates of low, expected, and high values of task times.

At each customer site, there are customer premise equipment (CPE) costs comprised of receiving antenna costs and installation costs (so-called <sup>b</sup>truck rolls<sup>Q</sup> [35]), which include antenna alignment and positioning expenses. Receiver antenna costs do vary widely by technology and depend primarily on the electronics costs of each system. The costs we used were US\$7900 for LMDS, US\$1295 for the WirelessMAN, and US\$230 for the Wi–Fi system. These costs were compiled from conversations with LMDS experts in the Center for Wireless Telecommunications at our university, wireless equipment distributors, and from wireless network service providers during the 2002/ 2003 year. We note that prices have and will continue to change rapidly; however the generalizability of the SDSS is not affected by such changes.

## 4.3. Revenue

Actual year 2000 number of households and per household annual income are available or can be calculated from United States census data down to (as mentioned) a $3 0 \times 3 0$ m grid. In this research we define a $2 \times 2$ km grid—each $2 \times 2$ km square is a <sup>b</sup>cell<sup>Q</sup>; the tradeoff with grid size is computational accuracy versus computational effort.

We assume the following functional form to calculate revenue: $\scriptstyle { \% } P = f ( I | p _ { \mathrm { m } } )$ , where $\% P$ is the percentage participation, I is the average annual household income for a cell, and $p _ { \mathrm { m } }$ is the price per month for the wireless broadband offering. That is, the percentage of households in a cell purchasing (<sup>b</sup>participating<sup>Q</sup>) in the broadband offering is a function of the average household income in that cell, given the monthly price of that service. These functional relationships were estimated from information on <sup>b</sup>related<sup>Q</sup> services in the local area, namely, the price charged for DSL and for cable modem <sup>b</sup>high-speed<sup>Q</sup> Internet service (3 Mbps download/256 Kbps upload). At a similar price, one would expect the wireless broadband service to be at least as desirable as the two alternatives mentioned, as the wireless bandwidth would be an order of magnitude or so better on the upload speed, depending on the wireless technology employed. The particular functional relationships employed in the study are shown in Table 1. Note that in that table, I is the average perhousehold annual income (in thousands of dollars), $p _ { \mathrm { m } }$ is expressed in dollars, and $\% P$ is a number between 0 and 100. As mentioned, the values in this table were estimated based on knowledge of similar service offerings in the local area. A market survey would be appropriate to determine true participation levels and is a future step we hope to pursue with additional funding.

## 4.4. Profit-maximization model

We divide the service region into n small (2 km  2 km) cells. If a and b are vectors, let the superscript $\mathbf { \ddot { \rho } } ^ { 6 6 } \mathbf { \vec { t } } ^ { \flat }$ designate the transpose of a vector and the dot operator <sup>bd Q</sup> the vector inner product of two vectors, as in $\pmb { a } ^ { \mathrm { t } } \cdot \pmb { b }$

The estimated percentage participation of households (in the example rural county) as a function of average household annual income, given the price per month $( p _ { \mathrm { m } } )$ for wireless service

<table><tr><td rowspan="2">Average annual household income, in thousands (I)</td><td colspan="3">Percent participation (%P)</td></tr><tr><td> $p_m$ =US$50/month</td><td> $p_m$ =US$75/month</td><td> $p_m$ =US$100/month</td></tr><tr><td>US$0–75</td><td>%P=0.2 I</td><td>%P=0.1 I</td><td>%P=0.05 I</td></tr><tr><td>US$75–100</td><td>%P=0.4 I–15</td><td>%P=0.1 I</td><td>%P=0.05 I</td></tr><tr><td>&gt;US$100</td><td>%P=25</td><td>%P=10</td><td>%P=5</td></tr></table>

Now define r, r, c, and $c _ { \mathrm { c p e } }$ as nx1 vectors representing profit, revenue, tower costs, and costs of customer premise equipment, respectively, for the i cells. Furthermore, let x be an nx1 decision vector such that $\mathbf { \nabla } x _ { i } = 1$ if a tower is placed in cell i and 0 otherwise; e be the nx1 vector of all ones; and z another nx1 vector such that $z _ { i } = 1$ if cell i receives at least one signal and 0 otherwise. Finally, define the scalar M as the budget limit, whether specified by a for-profit firm or as the maximum subsidy by the public sector; and the matrix V as the view-shed matrix, where $\mathbf { V } _ { i i } { = } 1$ if a tower placed in cell $j ,$ given the terrain, provides a signal to cel $^ { \cdot \ i , }$ and 0 otherwise. Values for V must be determined using the modified GETWEBS software embedded in our system.

If we assume $c _ { \mathrm { c p e } }$ to be constant across all cells and note that $\rho _ { i } { = } r _ { i } - c _ { \mathrm { c p e } } ,$ then the wireless broadband fixed, PMP profit maximization model may be written as:

$$
\max \rho^ {\mathbf {t}} \cdot \mathbf {z} - \mathbf {c} ^ {\mathbf {t}} \cdot \mathbf {x}\tag{1a}
$$

$$
\text { subject   to }: \quad \mathbf {V} x \geq z\tag{1b}
$$

$$
\boldsymbol {c} ^ {\mathbf {t}} \cdot \boldsymbol {x} + \boldsymbol {c} _ {\mathrm{cpe}} ^ {\mathbf {t}} \cdot \boldsymbol {z} \leq M\tag{1c}
$$

$$
\boldsymbol {x}, \boldsymbol {z} \varepsilon [ 0, 1 ].\tag{1d}
$$

If everyone must receive a signal, then constraint Eq. (1e) below is added to the system:

Vx<sub>z</sub>e:

ð1eÞ

If there is no budgetary or subsidization restriction, then M is allowed to approach infinity and constraint Eq. (1c) is removed from the model. The model is based upon the set covering problem; interested readers may pursue, for example, Ref. [40] or Ref. [46].

## 4.5. Exposure maximization model

An important alternative to the profit maximization model formulated above is a model which maximizes exposure within a prescribed budget. This model is useful for examining regions where profit cannot be made but where government subsidy is considered at a specified level. $\operatorname { I f } h _ { i } ,$ the ith component of the vector h, is the number of households in cell i, then the exposure model is:

$$
\max \boldsymbol {h} ^ {\mathrm{t}} \cdot \boldsymbol {z}\tag{2a}
$$

$$
\text { subject   to } \quad V x \geq z\tag{2b}
$$

$$
\mathbf {c} ^ {\mathrm{t}} \cdot \boldsymbol {x} + \boldsymbol {c} _ {\text { cpe }} ^ {\mathrm{t}} \cdot \boldsymbol {z} \leq M\tag{2c}
$$

$$
\boldsymbol {x}, \boldsymbol {z} \varepsilon [ 0, 1 ].\tag{2d}
$$

## 5. Last mile scenarios

We consider several last mile, wireless broadband scenarios in the medium-sized county mentioned earlier. This county has a population of 77,500 (about 29,000 households) in a rural setting and has an active interest in low-cost, high-speed Internet service, partly due to the presence of a large land-grant university. Fig. 5, seen earlier, shows a screenshot of this county displayed in the GETWEBS program.

The county is approximately a 40  40 km rectangle, which we subdivide into 394 cells (arranged roughly as 20 rows with 20 columns), each cell being a square of side 2 km. As mentioned, census data down to squares 30 m on a side is available and the process described below would be unchanged if analysis in greater detail were desired, although computational complexity would be significantly multiplied. For simplicity, we assume transmission towers may be placed only in the middle of any 2-km cell. A 15-year economic horizon with no leasing of CPE is assumed for all cases below.

GETWEBS considers a transmission tower centrally placed in a cell and then determines whether near LOS exists to each of the other (<sup>b</sup>receiving<sup>Q</sup>) cells. Three notes should be made with respect to this calculation: (1) this is a PMP GIS calculation, from the tower to each locale in the receiving cell; (2) the software reports the percentage of the receiving cell able to get a signal; and (3) the computational search over the receiving cells can be significantly reduced by the range of the signal. For example, in one scenario considered here, the signal is such that any one transmitting cell can reach at most only 28 other cells and transmitting cells on edges of the region have an even further reduced set of possible receiving cells.

The output from our view-shed software is a 394 by 394 matrix filled with percentages. We arbitrarily specify that a cell with greater than 50% coverage from a tower is covered and enter $\mathrm { ~ a ~ } \ ^ { 6 6 } 1 ^ { 5 }$ in the corresponding cell for the view-shed matrix. Obviously the 50% threshold may be adjusted to meet particular circumstances.

## 6. Results

To demonstrate viability of our SDSS for planning broadband, fixed wireless telecommunication networks, the profit model developed above is run for each of the three technologies described. First, the view-shed matrix V is determined by GETWEBS and substituted into Eq. (1b). Then the system given by Eqs. (1a) (1b) (1c) and (1d) is solved.

## 6.1. LMDS at US\$50 per month

Results from the model indicate that this technology, though touted for several years until the fairly recent past, is substantially too expensive for deployment in a county similar to the one in our example with revenues set at US\$50 per month. The maximizing-profit (Eqs. (1a-d)) solution declares that no profit can be made and that, hence, no towers should be placed.

## 6.2. WirelessMAN at US\$50 and US\$100 per month

The WirelessMAN reduces the customer premise equipment to US\$1295. Nonetheless, at a price of US\$50/month, once again wireless service is not profitable. At a price of US\$100/month, the optimal solution suggests that one tower be placed reaching approximately 700 households (less than 3% of the county total). Moreover, only (approximately) US\$25,000 in profit is generated. The one tower placed is positioned in the northern portion of the county where the population is densest.

## 6.3. Wi–Fi at US\$50 per month

With CPE down to US\$230, the Wi–Fi alternative generates a significant profit. Almost 80% of the county is projected to participate, requiring 6 towers (see Fig. 6), generating a profit of US\$5M on a cost of US\$6.2M.

## 6.4. Wi–Fi at US\$75 per month

With CPE still at US\$230 but $p _ { \mathrm { m } } { = } \mathrm { U S S } 7 5 / \mathrm { m o n t h } ,$ the Wi–Fi alternative generates a significantly greater profit (in comparison to the US\$50 per month scenario) of US\$11M on a cost of US\$8.2M. In the US\$75 per month scenario 13 towers cover 90% of the county population.

## 7. Discussion

The previous section examined using our SDSS to evaluate three wireless technologies in a <sup>b</sup>forprofit<sup>Q</sup> context of solving the last mile problem. Even with the Wi–Fi scenario, universal service was not nearly achieved. As a planning tool for potential wireless network providers, it is valuable to allow <sup>b</sup>what-if<sup>Q</sup> scenarios to be explored for other options. For example, we now consider the case where a for-profit service provider has found a limited level of service profitable, but the government wishes to increase the number of households reached. In the US\$50 per month Wi–Fi example given above, the maximum-profit solution provides service to 80% of the households in the county, but the government may stipulate service for (say) 90% of the households. If the government agrees to make up for the provider’s loss in profit over the 5-year horizon (see Fig. 7 for some results at different levels of coverage), the subsidy would be approximately US\$500K in the county.

![](/api/attachments/E836AV5V/fulltext/images/602817e3dc1e746a26ef2e071037059603f4bc970a19906728c4447f4c89a113.jpg)

Alternatively, if the government agreed to make up for the difference in total costs (not shown), the subsidy would be US\$1.7M. Further analysis indicates that the profit begins to drop quite sharply beyond 90% coverage, where tower costs increase dramatically; with the easiest-to-reach people having been served, towers must be placed that cover relatively few individuals. For our example county, a government subsidy to provide service beyond 90% would give relatively little marginal benefit for the marginal expenditure.

A second subsidization alternative beyond the cooperative venture between the government and a forprofit firm is one in which no for-profit wishes to provide broadband service to a region. In such a case the government may believe it is necessary to subsidize the entire project. In this situation the maximum exposure model of Eqs. (2a-d) could be utilized, specifying the subsidization amount M in Eq. (2c).

![](/api/attachments/E836AV5V/fulltext/images/b32c4ec7addc9c332c9b31b0b8079a4a57477858e1c99e9073d4155786bb41ad.jpg)  
Fig. 6. Tower placement and profit-sheds (white) for Wi–Fi service offered at US\$50/month.

![](/api/attachments/E836AV5V/fulltext/images/7e765d7fde8e198c6b51478cd55665d0b421b4b007cc82b1bef02c2dd0bc7025.jpg)  
Fig. 7. Profit, households, and towers in the rural county as a function of percent coverage with Wi–Fi broadband.

For example, for a small subsidy of US\$500K in the example, 1670 households can be reached, with one tower being placed.

## 8. Conclusions

This paper has shown how a specially designed GIS can add multiple levels of functionality to a DSS. The GETWEBS tool not only augmented the DSS by geographic modeling but also contributed knowledge, spatial data and computation, and graphical output. In turn, the GETWEBS tool was augmented by traditional modeling and the ability to view <sup>b</sup>what-if<sup>Q</sup> scenarios, which is typical of most DSS. Bringing the two together created an extremely powerful tool that we believe will prove invaluable to wireless network planners in solving the tower location problem and to policy analysts in addressing for-profit versus subsidization scenarios. We presented several location models of wireless broadband deployment to help provide answers to solving the last mile problem. Both profitmaximization and subsidization scenarios were presented to illustrate the procedure in a particular county in the mid-Atlantic United States region and to draw specific and more general implications. For example, it was seen that of the three technologies examined, only Wi–Fi has potential in counties similar to the one we studied—and, universal service is not a feasible economic option there. In areas less sparsely populated or more mountainous, the economic provision of wireless technologies is less likely at current costs.

The results developed in this paper from the SDSS apply mainly to one county and are based on estimates. The generation of results for the entire United States is possible thereby providing an estimate of the magnitude of the national last mile problem. Nonetheless, significant effort would be required to generate reliable estimates. In particular, census data maps are available with household data, as well as DEMs to develop view sheds. The greatest efforts would be expended in developing appropriate tower costs as well as building reliable market research models.

Although this SDSS has not yet been applied to a <sup>b</sup>real world<sup>Q</sup> wireless network plan or to a large-scale policy analysis, we believe we have demonstrated the system’s capabilities to do both. Moreover, wireless electronics developers could use this system <sup>b</sup>backwards<sup>Q</sup> to estimate cost levels necessary for profitable hardware development. Ultimately, all of these efforts would ensure greater success in wireless broadband deployment and fewer people would need to ask why they cannot have high-speed Internet service.

## References

[1] A. Acampora, Last mile by laser—short-range infrared lasers could beam advanced broadband multimedia services directly into homes and offices, Scientific American 287 (1) (2002) 48– 53.

[2] S.M. Allen, S. Hurley, R.K. Taplin, R.M. Whitaker, Automatic cell planning of broadband fixed wireless networks. Vehicular technology Conference, 2001. VTC 2001 Spring. IEEE VTS 53rd. 2001.

[3] E. Amaldi, A. Capone, F. Malucelli, Discrete models and algorithms for the capacitated location problems arising in UMTS network planning, Proceedings of the 5th international workshop on discrete algorithms and methods for mobile computing and communications, ACM Press, Rome, Italy, 2001.

[4] D.O. Awduche, A. Ganz, A. Gaylord, An optimal search strategy for mobile stations in wireless networks, Universal personal communications, 1996. Record., 1996 5th IEEE International Conference, 1996.

[5] M.R. Bartolacci, B. Peltsverger, A. Konak, S. Peltsverger, Allocation of multiple wireless access points in mobile networks, Proceedings of the 42nd annual southeast regional conference, ACM Press, Huntsville, Alabama, 2004.

[6] J.L. Bennet, Building decision support systems, in: P.G.W. Keen, C.B. Stabell (Eds.), Addison–Wesley series on decision support, vol. 1, Addison–Wesley, Reading, Massachusetts, 1983.

[7] L.W. Carstensen, C.W. Bostian, G.E. Morgan, Combining electromagnetic propagation: geographic information systems, and financial modeling in a software package for broadband wireless wide area network design, International conference on electromagnetics in advanced applications, 2001, ISBN: 88-8202-098-3 (Torino, Italy).

[8] G. Cho, L.F. Marshall, An efficient location and routing scheme for mobile computing environments, IEEE Journal on Selected Areas in Communications 13 (5) (1995) 868 – 879.

[9] M.D. Crossland, B.E. Wynne, W.C. Perkins, Spatial decision support systems: an overview of technology and a test of efficacy, Decision Support Systems 14 (3) (1995) 219– 235.

[10] ESRI, Getting to know ArcView GIS: the geographic information system (GIS) for everyone, Third ed., Environmental Systems Research Institute, Inc., New York, 1999.

[11] K. Fisher, Wimax Technology may solve <sup>d</sup>last mile<sup>T</sup> problem for high-speed access, http://arstechnica.com/news/posts/ 1074799974.html.

[12] T. Fowler, Mesh networks for broadband access, IEE Reviews 47 (1) (2001) 17 – 22.

[13] M. Galota, C. Glaber, S. Reith, H. Vollmer, A polynomial-time approximation scheme for base station positioning in UMTS networks, Proceedings of the 5th international workshop on discrete algorithms and methods for mobile computing and communications, ACM Press, Rome, Italy, 2001.

[14] P.R.L. Gondim, Genetic algorithms and the location area partitioning problem in cellular networks, Vehicular technology conference, 1996. <sup>d</sup>Mobile technology for the human race<sup>T</sup>. IEEE 46th, 1996.

[15] S. Guo, O.W. Yang, Antenna orientation optimization for minimum-energy multicast tree construction in wireless ad hoc networks with directional antennas, Proceedings of the 5th ACM international symposium on mobile ad hoc networking and computing, ACM Press, Roppongi Hills, Tokyo, Japan, 2004.

[16] S. Hurley, R.M. Whitaker, An agent based approach to site selection for wireless networks, Proceedings of the 2002 ACM symposium on applied computing, ACM Press, Madrid, Spain, 2002.

[17] IEC, Local multipoint distribution systems (LMDS), http:// www.iec.org/online/tutorials/lmds/.

[18] IEEE, Ieee 802.16 Backgrounder, http://www.ieee802.org/16/ pub/backgrounder.html.

[19] Intel, Ieee 802.16\* and Wimax, http://www.intel.com/ebusiness/ pdf/wireless/intel/80216<sup>\_</sup>wimax.pdf.

[20] E. Jensen, LMDS gets down to business, Wireless Review 15 (11) (1998) 54.

[21] P.G.W. Keen, M.S. Scott Morton, Decision support systems: an organizational perspective, in: P.G.W. Keen, C.B. Stabell (Eds.), Addison–Wesley Series on Decision Support, Addison–Wesley, Reading, Massachusetts, 1978.

[22] P.B. Keenan, Spatial decision support systems for vehicle routing, Decision Support Systems 22 (1) (1998) 65 – 71.

[23] K. Kornbluh, The broadband economy, New York Times, New York, 2001, p. 21.

[24] M. Langberg, San Jose Mercury News, Calif., Mike Langberg Column, Knight Ridder Tribune Business News, No. (2004) p. 1.

[25] V. Maniezzo, I. Mendes, M. Paruccini, Decision support for siting problems, Decision Support Systems 23 (3) (1998) 273– 284.

[26] R. Marks, What is LMDS?, http://www.nwest.nist.gov/ lmds.html.

[27] R. Mathar, T. Niessen, Optimum positioning of base stations for cellular radio networks, Wireless Networks 6 (6) (2000) 421– 428.

[28] S. Meguerdichian, S. Slijepcevic, V. Karayan, M. Potkonjak, Localized algorithms in wireless ad-hoc networks: location discovery and sensor exposure, Proceedings of the 2nd ACM international symposium on mobile ad hoc networking and computing, ACM Press, Long Beach, CA, USA, 2001.

[29] B.E. Mennecke, M.D. Crossland, B.L. Killingsworth, Is a map more than a picture? The role of SDSS technology, subject characteristics, and problem complexity on map

reading and problem solving, Mis Quarterly 24 (4) (2000) 601–629.

[30] C.C. Nehme, M. Simo˜ es, Spatial decision support system for land assessment, ACM GIS, ACM Press, Kansas City (MO), 1999.

[31] T. Olavsrud, IBM helps take truck stops wireless with Linux, http://www.internetnews.com/wireless/article.php/2112361.

[32] Z. Salcic, GSM mobile station location using reference stations and artificial neural networks, Wireless Personal Communications 19 (3) (2001) 205–226.

[33] D. Sextro, LMDS: a license to drive, Wireless Review 15 (15) (1998) 64.

[34] R. Shim, At and T sets Wi–Fi aloft in Philly Airport, http:// zdnet.com.com/2110-1104<sup>\_</sup>2-5095672.html.

[35] B. Shrick, M.J. Riezenman, Wireless broadband in a box, IEEE Spectrum 39 (6) (2002) 38 – 43.

[36] H. Simon, The new science of management decision, vol. 1, Harper and Row, New York, 1960.

[37] M. Singer, Wi–Fi gets <sup>d</sup>super sized<sup>T</sup>, http://www.wi-fiplanet. com/news/article.php/2107771.

[38] A. Stone, Long distance Wi–Fi, http://www.wi-fiplanet.com/ columns/article.php/2191841.

[39] S. Tabbane, An alternative strategy for location tracking, IEEE Journal on Selected Areas in Communications 13 (5) (1995) 880 – 892.

[40] H.A. Taha, Integer programming—theory, applications, and computations, Academic Press, New York, 1975.

[41] C.D. Tarantilis, C.T. Kiranoudis, Using a spatial decision support system for solving the vehicle routing problem, Information and Management 39 (5) (2002) 359– 375.

[42] TechNet, A national imperative: universal availability of broadband by 2010, http://www.technet.org/news/newsreleases/ 2002-01-15.64.pdf.

[43] K. Todd, The will to succeed, Wireless Review 15 (10) (1998) 16.

[44] USGS, USGS digital elevation model data, http://edc.usgs. gov/products/elevation/dem.html.

[45] M. Vasquez, J.-K. Hao, A heuristic approach for antenna positioning in cellular networks, Journal of Heuristics 7 (5) (2001) 443–472.

[46] R.R. Vemuganti, Application of set covering, set packing and set partitioning models: a survey, in: D.-Z. Zu, P.M. Pardalos (Eds.), Handbook of combinatorial optimization, Kluwer Academic Publishers, 1998, pp. 573 – 746.

[47] M. Vlachopoulou, G. Silleos, V. Manthou, Geographic infor mation systems in warehouse site selection decisions, International Journal of Production Economics 71 (1–3) (2001) 205–212.

[48] Webopedia, LMDS, http://www.webopedia.com/TERM/L/ LMDS.html.

[49] R.M. Whitaker, S. Hurley, On the optimality of facility location for wireless transmission infrastructure, Computers & Industrial Engineering 46 (1) (2004) 171–191.

[50] H.A. Willebrand, B.S. Ghuman, Fiber optics without fiber, IEEE Spectrum 38 (8) (2001) 41 – 45.

[51] B. Willis, T. Hasletad, T. Friiso, O.B. Holm, Exploiting peerto-peer communications—mesh fixed and ODMA mobile radio, Journal of the IBTE 2 (2) (2001) 48– 53.

Kevin P. Scheibe is an assistant professor in Logistics, Operations, and Management Information Systems in the College of Business at Iowa State University. His research interests include spatial decision support systems, wireless telecommunications, knowledge management, cognitive mapping and heuristics. He is a member of the Association for Information Systems, the Association for Computing Machinery, the Decision Sciences Institute, the Institute of Electrical and Electronics Engineers, and the Institute for Operations Research and the Management Sciences. He received his PhD in Business Information Technology from Virginia Polytechnic Institute and State University.

Laurence W. Carstensen, Jr. is professor of Geography at Virginia Polytechnic Institute and State University. His research interests are in applying a <sup>b</sup>geographic brain<sup>Q</sup> in technology. His recent work has been in wireless propagation modeling within Geographic Information Systems (GIS) and in the use of GIS in navigation of autonomous ground vehicles. He has published in cartographic and GIS journals including Cartographica, Cartography and Geographic Information Systems, Photogrammetric Engineering and Remote Sensing and the Journal of Geography. He received a PhD in Geography from the University of North Carolina at Chapel Hill.

Terry R. Rakes is William C. and Alix C. Houchens professor of Information Technology at Virginia Polytechnic Institute and State University. His research interests are in wireless telecommunications, software agents, and the application of decision support and artificial intelligence methodologies to problems in information systems. He has published in such journals as Management Science, Decision Sciences, Annals of Operations Research, Operations Research Letters, Information and Management, Journal of Information Science, and others. He is a member of the Decision Sciences Institute and The Institute for Operations Research and the Management Sciences. He received the PhD in Management Science from Virginia Polytechnic Institute and State University.

Loren Paul Rees is Andersen/Andersen consulting alumni professor in Information for Management at Virginia Polytechnic Institute and State University. He was formerly a member of the Technical Staff at Bell Telephone Laboratories. His research interests include simulation optimization, wireless telecommunications, and software agents and he has published in such journals as Naval Research Logistics, Transportation Research, IIE Transactions, Decision Sciences, and others. He is a member of the American Association for Artificial Intelligence, The Institute for Operations Research and the Management Sciences, and the Decision Sciences Institute. He received his PhD in Industrial and Systems Engineering from the Georgia Institute of Technology.
