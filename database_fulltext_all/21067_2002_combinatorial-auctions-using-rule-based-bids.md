---
otero_id: 21067
otero_key: "Q66BRGP6"
title: "Combinatorial auctions using rule-based bids"
authors: "Joni L. Jones; Gary J. Koehler"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00004-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Combinatorial auctions using rule-based bids

Joni L. Jones <sup>a,</sup>\*, Gary J. Koehler <sup>b</sup>

<sup>a</sup>University of Michigan Business School, 701 Tappan St. D5210, Ann Arbor, MI 48109, USA <sup>b</sup>Warrington College of Business, University of Florida, Gainesville, FL USA

Accepted 1 December 2001

## Abstract

The migration of auctions to the Internet provides a unique opportunity to harness the power of computing to create new auction forms that were previously impossible. We describe a new type of combinatorial auction that accepts rule-based bids. Allowing bids in the form of high-level rules relieves the buyer from the burden of enumerating all possible acceptable bundles. The allocation of goods requires solving a complex combinatorial problem, a task that is completely impractical in a conventional auction setting. We describe simplifying winner determination heuristics developed in this study to make large problems of this nature manageable. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Combinatorial auction; Heuristics; Constraint satisfaction; Integer programming

## 1. Introduction and background

Electronic or Internet-based auctions have garnered a great deal of interest in recent years. The renewed popularity of auctions stems from various characteristics unique to this form of commerce. Web-based auctions enjoy a broad audience due to their accessibility to anyone with an Internet connection, thereby growing the buyer pool, increasing competition and thus enhancing profits [10,11]. Also, the expense and logistics of gathering at one location, a major deterrent to conventional auctions, has been replaced with inexpensive websites. Barriers to entering the electronic auction market have been lowered for all participants. Finally, electronic auctions provide an opportunity, through harnessing the power of computing, to establish more complex trading rules and handle more complex goods. This research presents a complex auction mechanism that capitalizes on this opportunity and the associated winner determination algorithm.

Traditional single item auctions take several forms. The most familiar is the English auction, a progressive ascending open auction. Other forms include the Dutch (open descending), and the First Price and Vickrey’s second price sealed bid auctions. The first ‘‘multipleitem auction’’ was proposed by Vickrey [31] and allowed several identical units to be sold to bidders who desired but one item. Two variations of the progressive auction, simultaneous and sequential, are most commonly used to facilitate multi-unit sales. How the auction is conducted within the multi-unit environment (i.e., sequentially or simultaneously) propagate a variety of alternative designs. For example, the popular Internet-based Yankee Auction [30] and the Groves/ Vickrey design [3], in which a specified number of identical items are offered for sale simultaneously with the items going to the top bidders whose aggregate demand equals the number of items for sale, have been extensively studied. The FCC Spectrum license sales, which began in the mid-1990s, have shown that by executing single items auctions simultaneously, buyers could aggregate a desired collection of complementary goods [7,18].

None of the above designs allow the bidder to submit a single bid for a combination of heterogeneous items. Allowing bidders to create a bundle of desired goods for which a single bid price is submitted, referred to as a package or bundled bid, is a logical extension and has been proposed and studied by others [2,4, 25,33]. When complementarities, indivisibilities, or other complications exist between the different items in a bundle, combinatorial considerations must be explored. Such combinatorial auctions allow the buyer to create and submit bids for one or more (‘‘exclusive or’’) bundles and are often superior to other multi-object sales mechanisms [8].

Winner determination in combinatorial auctions involves selecting a collection of bids that maximizes seller revenue without exceeding the availability of the goods being auctioned. This is an NP-complete combinatorial optimization problem [27]. Several researchers have tried circumventing this challenge by either restricting the bid structure to reduce the computational intractability [27] or by extending single item mechanisms in some heuristic fashion [14,15, 23,34]. In general, fast heuristics are almost always required.

Price alone may not be sufficient to distinguish between bundles. Other attributes of a bundle may be important and not easily ‘‘priced.’’ In many auction settings [16,33], the very process of determining acceptable bundles and bid prices is nontrivial. For example, a buyer may want a certain band width between two points at a certain time and quality level. Spelling-out the different connections that might satisfy this objective itself requires exploring a combinatorial space with many bidder constraints. We believe combinatorial auction mechanisms that place the burden of determining all acceptable bundles on the buyer are inherently impractical for many applications. To date, complicated transactions such as these have often been handled through negotiated sales but auctions may provide an effective means of price discovery, especially for products hard to price a priori or when information asymmetries are present [5,9,21].

This research explores a new auction mechanism that directly addresses combinatorial auctions without requiring bidders to enumerate their desired bundles, prices, and attributes. Instead, bidders provide a highlevel specification or set of rules describing their ultimate requirements and the auction mechanism directly determines both the formation of acceptable bundles and a revenue-maximizing allocation of resources. This malleable bid along with the ability of the bidder to dictate various aspects of the final bundle, beyond her willingness to purchase units at a particular price, makes it possible to use this type of mechanism to replace or enhance a negotiated environment. To illustrate our ideas, we focus on a market traditionally reliant on negotiated sales. Specifically, we look at the sales of primetime television advertising.

This paper is organized as follows. We describe the overall design of the proposed auction mechanism in Section 2. In Section 3, we provide a brief overview of the TV advertising problem that is modeled as an integer program in Section 4 for preciseness. The heuristic methodology to facilitate winner determination within the proposed auction mechanism is defined in Section 5. Sections 6 and 7 discuss the experiments designed to test the efficacy of the mechanism. Limitations of the study are identified in Section 8 and we conclude with a summary and future research proposals in Section 9.

## 2. Auction mechanism

The overall design of our auction, referred to as the Incompletely Specified Combinatorial Auction (ISCA), is shown in Table 1. We propose a progressive semi-sealed auction format that allows the bidder to provide high-level requirements that guide the auction mechanism to create feasible bundles while maximizing seller revenue. In many markets, buyers and sellers jealously protect information on product availability and price. To accommodate this, we employ a semi-sealed format where suggestions are provided to the bidders to help them formulate new bids, but active pricing and overall allocations are not disclosed to other bidders. [29]. Bidders are given the flexibility to change their bids after each round until a stopping criterion has been reached.

Table 1  
Incompletely Specified Combinatorial Auction (ISCA) design

<table><tr><td rowspan="4">Auction type</td><td>Progressive</td><td>Multiple rounds</td></tr><tr><td>Ascending (relaxing)</td><td>Increasing bid amount (relaxing tight constraints)</td></tr><tr><td>Semi-sealed</td><td>No open display of bid information—recommended reentry bids provided</td></tr><tr><td>Combinatorial</td><td>Allows package bids</td></tr><tr><td rowspan="5">Bids</td><td>Incompletely specified</td><td>Includes price and various high-level rules</td></tr><tr><td>Modification (signalling)</td><td>Increase amount by minimum percentage increment, suggested new bid and/or relax tight constraint(s)</td></tr><tr><td>Eligibility</td><td>No restrictions</td></tr><tr><td>Jump bidding</td><td>Permitted</td></tr><tr><td>Withdrawal</td><td>Not allowed—only if nonwinning bid</td></tr><tr><td rowspan="3">Closing rules</td><td>Minimum revenue</td><td>Achieve a predetermined seller revenue goal (not revealed to buyer)</td></tr><tr><td>Activity</td><td>No new bids or bid modifications received</td></tr><tr><td>Maximum round</td><td>Attain a predetermined round (not revealed to buyer)</td></tr></table>

Three potential stopping rules are proposed and tested for ISCA. The Activity Rule resembles the progress of a classic English auction allowing the auction to continue until no further bids are submitted. The two other stopping rules terminate the auction when a predetermined revenue goal has been reached or a designated round has been completed. The predefined conditions in the last two alternative stopping rules are not revealed to the buyer to entice the bidder to participate in early rounds.

## 3. Illustrative example —Primetime Advertising

We illustrate the potential of the ISCA by applying it in the highly complex multidimensional process of media buying, specifically the sale of television advertising airtime. Airtime is a perishable commodity product that is currently sold through negotiations ‘‘frequently based on long-term relationships and editorial and demographic synergies, not just getting the lowest price’’ [32,p. 1]. Units are typically allocated on a first come first serve basis rather than dictated by competitive forces that could enhance the network’s ability to achieve an equilibrium-based distribution of goods. The complexity of determining an allocation that simultaneously satisfies the market participants’ demands for different demographic exposure, advertisement placement, various commercial lengths, etc., while maximizing revenue restricts the seller’s ability to promote competitive bargaining. Similarly, buyers must determine an advertising mix that meets their demographic campaign goals while satisfying other considerations such as image, frequency (how often a commercial appears), and reach (how may viewers exposed to the commercial) within a predetermined budget.

An indication of the desire and ability to promote competition in this market is the appearance of a number of web-based auctions selling excess last minute advertising inventory. These sites, such as AdOutlet. com and OneMediaPlace.com, are simplistic in nature, selling single units of time that are considered ‘‘fire sale’’ spots or unsold airtime within close proximity to airdate. These sites have been criticized for their limited offerings and their focus on ‘‘distressed’’ inventory [6,28].

## 4. Auction description

We explore an auction for ‘‘up-front’’ sales. This market is a large one-time sale of spot advertising time for annual TV campaigns. That is, a typical week’s advertising schedule is determined, the pattern of which will be repeated throughout some specified number of weeks. We concentrate on primetime advertising where approximately 300 to 350 buyers compete for commercial airtime in the upcoming season. Primetime extends from 8 p.m. to 11 p.m. with shows varying in length from 30 minutes to 2 hours. A one-hour show generally contains five to seven commercial breaks referred to as pods and roughly four to eight 15-second slots or units per pod. The base unit of allocation in this auction is the 15-second unit.

To describe accurately the primetime sales auction, we model it as an integer program. A summary of the notation is presented in Appendix A for ease of reference. Our main decision variable is $x _ { u , p , s , b } ,$ a binary variable set to 1 if buyer b is allotted a 15-second unit u in pod p for show s. The model is not meant to be a direct prescription of the input into an IP solver since many known formulation alternatives would produce tighter LP relaxations [12], but is given merely to define accurately and simply the problem at hand. Additionally, a detailed description of the specific problem tackled in this research serves to illustrate the level of complexity our auction can accommodate.

The seller solves problem P1, which includes the following objective and constraints (1) – (11d).

Objective function

$$
\max \sum_ {b = 1} ^ {B} a _ {b} y _ {b}\tag{P1}
$$

The objective function maximizes the total revenue from accepted bids $a _ { b } ,$ where $y _ { b } = 1$ indicates bidder b has a winning bid.

The reservation requirement in the television industry is based on an unpublished list price for each show, $L _ { s } .$ The sum of the accepted bids must be greater than the sum of the internal list prices for the units sold. This constraint operates on an aggregate level—an individual bidder may actually pay less than the sum of the list prices of the units she purchases.

Reservation requirement

$$
\sum_ {b = 1} ^ {B} a _ {b} y _ {b} \geq \left(\sum_ {b = 1} ^ {B} \left(\sum_ {s = 1} ^ {S} \left(\sum_ {p = 1} ^ {P _ {s}} \sum_ {u = 1} ^ {U _ {p, s}} x _ {u, p, s, b}\right) L _ {s}\right)\right)\tag{1}
$$

Not all of the advertising inventory is released to ‘‘up-front’’ sales. Networks often reserve a portion of their supply for sales in later markets. The maximum coverage constraint limits the number of commercials sold in show s to $C _ { s } ,$ the number of units made available.

Maximum coverage

$$
\sum_ {b = 1} ^ {B} \sum_ {p = 1} ^ {P _ {s}} \sum_ {u = 1} ^ {U _ {p, s}} x _ {u, p, s, b} \leq C _ {s} \quad s = 1, \ldots , S\tag{2}
$$

Each show is broken into pods, usually 1- to 2-min blocks of airtime reserved for commercial placement. The number of pods per show and their length vary from show to show. The following guarantees that the number of commercial placements per pod does not exceed the number of units available to accommodate them, $U _ { p , s }$

Max availability=pod

$$
\begin{array}{l} \sum_ {b = 1} ^ {B} \sum_ {u = 1} ^ {U _ {p, s}} x _ {u, p, s, b} \leq U _ {p, s} \\ p = 1, \ldots , P _ {s} \quad s = 1, \ldots , S \end{array}\tag{3}
$$

If a particular bidder b does not obtain any airtime, the following constraint forces all her x values to zero and thus drops her bid from consideration.

Buyer selection indicator

$$
\begin{array}{l} \sum_ {s = 1} ^ {S} \sum_ {p = 1} ^ {P _ {s}} \sum_ {u = 1} ^ {U _ {p, s}} x _ {u, p, s, b} \leq \left(\sum_ {s = 1} ^ {S} \sum_ {p = 1} ^ {P _ {s}} U _ {p, s}\right) y _ {b} \\ b = 1, \ldots , B \end{array}\tag{4}
$$

Advertising campaigns may consist of commercials of varying lengths. A campaign composed of only 30-, 45-, or 60-second spots must eliminate any collection of 15-second units in an individual pod that will not form a desired commercial length. Buyers may also have mixed campaigns, or campaigns that consist of a combination of lengths. $N _ { s , b }$ is a set of permissible commercial lengths for each show s supplied by buyer b. Note that the permissible collection of lengths can vary by show facilitating a buyer’s need to vary the length(s) of its commercials. Industry practice dictates that no more than one commercial per buyer appears in the same pod. An exception to this rule allows that at most two 15-second units from the same advertiser may be placed in the same pod. To account for this exception, we modify the set $N _ { s , b }$ by adding ‘‘2’’ as an allowable size if the bidder permits a 15-second unit.

$$
\overline {{N}} _ {s, b} = \left\{ \begin{array}{l l} N _ {s, b} \cup \{2 \} & \text { if } 1 \in N _ {s, b} \text { and } 2 \not \in N _ {s, b} \\ N _ {s, b} & \text { otherwise } \end{array} \right..
$$

Below, Equations (5a) and (5b) jointly control the allocation of correct length commercials. Variable $I _ { p , s , b , i }$ in Eq. (5a) is set to one if pod p of show s for buyer b uses an allowable number (i) of advertising slots. Thus, the equation requires that the cumulative number of units assigned to buyer b in each pod correspond to one of her allowable commercial lengths (listed in $\overline { { N } } _ { s , b } ) .$ Ordering of assigned unit slots in a pod is not considered here. In practice, they are positioned within a pod just before airtime to handle the concatenation and sequencing problem.

Campaign length

$$
\begin{array}{l} \sum_ {u = 1} ^ {U _ {p, s}} x _ {u, p, s, b} = \sum_ {k \in \overline {{N}} _ {s, b}} k I _ {p, s, b, i} \\ p = 1, \ldots , P _ {s} \quad s = 1, \ldots , S \quad b = 1, \ldots , B \end{array}\tag{5a}
$$

Equation (5b) prevents more than one correct length commercial for buyer b from appearing in pod $p$ of show s.

Commercials=pod

$$
\begin{array}{l} z _ {p, s, b} \leq 1 \quad p = 1, \ldots , P _ {s} \\ s = 1, \ldots , S \quad b = 1, \ldots , B \end{array}\tag{5b}
$$

Variable $z _ { p , s , b } ,$ defined by,

$$
z _ {p, s, b} \equiv \sum_ {i \in \overline {{N}} _ {s, b}} I _ {p, s, b, i}
$$

is 1 if buyer b has a correct length commercial in pod $p$ of show s.

Placing a large number of different commercials in the same pod weakens the impact of all commercial messages within that pod. This phenomenon results from the ‘‘clutter’’ exacerbated by the use of 15-second commercials. Networks seek to avoid this problem by allowing at most two 15-second ads to appear in each pod (see Eq. (6)).

Anti 	 clutter

$$
\sum_ {b = 1} ^ {B} I _ {p, s, b, 1} \leq 2 \quad p = 1, \dots , P _ {s} \quad s = 1, \dots , S\tag{6}
$$

Controlling the number of commercials appearing in each show allows the buyer to spread or aggregate commercials over the campaign week. $K _ { s , b }$ is the number of correct length commercials that are permitted in show s by buyer b. Also, a buyer can identify a forbidden show, say show $s ^ { \prime }$ , by setting $K _ { s ^ { \prime } , b } = 0$ . Eq. (7) provides for such constraints.

Maximum spots=show

$$
\sum_ {p = 1} ^ {P _ {s}} z _ {p, s, b} \leq K _ {s, b} \quad s = 1, \dots , S \quad b = 1, \dots , B\tag{7}
$$

Media buyers desire a specific amount of demographic gross impressions, or number of viewers exposed to their commercial during their campaign. There are a variety of demographic categories upon which a show is rated. Each show’s gross impressions per category forms the demographic vector $\pmb { D } _ { s }$ and indicates the seller’s estimated reach for that particular show in the upcoming season. In this study, $\pmb { D } _ { s }$ is ordered by the categories: Women 18 to 49, Women 25 –54, Men 18 – 49, Men 25–54, Adults 18–49 and Adults 25–54. $\pmb { T } _ { b }$ represents the vector of demographic reach or gross impressions that the buyer needs to meet the product’s campaign goals in each category. $\pmb { D } _ { s }$ is estimated at sales time, but later confirmed shortfalls (determined from actual Nielson viewership ratings) are made-up with surplus inventory held back for such possibilities. Also, although the total number of gross impressions, $\pmb { D } _ { s } ,$ is not believed to be a function of commercial length (i.e., a 30-second commercial gives the same number of gross impressions as does a 60-second commercial), industry practice computes demographic exposures assuming that gross impressions are proportional to the commercial length. Eq. (8) assures that the minimum demographic requirement is achieved. The sum of the total number of 15-second units, times the specified demographic gross impressions over all selected shows must meet or exceed the required impressions for the specified demographic group(s).

Demographic reach required

$$
\sum_ {s = 1} ^ {S} \left(\sum_ {p = 1} ^ {P _ {s}} \sum_ {u = 1} ^ {U _ {p, s}} x _ {u, p, s, b}\right) \boldsymbol {D} _ {s} \geq \boldsymbol {T} _ {b} y _ {b} \quad b = 1, \dots , B\tag{8}
$$

In addition to the actual dollar amount bid and demographic requirements, a buyer may specify desired shows within which they would like their commercials placed. Setting $h _ { s , b }$ to 1 indicates that buyer b would prefer placement in show s. She can further indicate her willingness to deviate from her program preferences by setting the upper $\overline { { H } } _ { b }$ and lower $\underline { { H } } _ { b }$ bounds to the number of shows required. Eqs. (9a) and (9b) determine variable $j _ { s , b }$ that captures which shows buyer b has been allocated.

$$
\sum_ {p = 1} ^ {P _ {s}} z _ {p, s, b} \geq j _ {s, b} \quad s = 1, \dots , S \quad b = 1, \dots , B\tag{9a}
$$

Show allocation

$$
\sum_ {p = 1} ^ {P _ {s}} z _ {p, s, b} \leq P _ {s} j _ {s, b} \quad s = 1, \dots , S \quad b = 1, \dots , B\tag{9b}
$$

Eq. (10) ensures that a buyer is allotted at least $\underline { { H } } _ { b }$ shows and no more than $\overline { { H } } _ { b }$ of the shows requested.

Desired shows

$$
\overline {{{H}}} _ {b} \geq \sum_ {s = 1} ^ {S} h _ {s, b} j _ {s, b} \geq \underline {{{H}}} _ {b} y _ {b} \quad b = 1, \dots , B\tag{10}
$$

Networks routinely guarantee that competing $( \mathrm { i . e . }$ when $M _ { i } { = } M _ { j } )$ advertisements do not appear in the same pod. The group of Eqs. (11a) – (11d) implements this notion of ‘‘pod protection.’’ Pod protection is normally not given for a single 15-second commercial, therefore we need only implement anti-competition when a buyer has two or more units in a particular pod. The decision variable $f _ { p , s , b }$ is set to 1 if a bidder b has two or more 15-second units in a particular pod p of show s. When the number of units a bidder has per show is 0, there is no competition and Eq. (11a) forces both $f _ { p , s , b }$ and $z _ { p , s , b }$ to 0.

Pod protection A :

$$
\begin{array}{l} \sum_ {u = 1} ^ {U _ {p, s}} x _ {u, p, s, b} \geq z _ {p, s, b} + f _ {p, s, b} \\ p = 1, \ldots , P _ {s} \quad s = 1, \ldots , S \quad b = 1, \ldots , B, \end{array}\tag{11a}
$$

In the case where one unit is assigned in a particular show to buyer $^ { b , }$ pod protection is not enforced and the requirement that $z _ { p , s , b }$ equal or exceed $f _ { p , s , b }$ in Eq. (11b) sets $f _ { p , s , b }$ to zero, and $z _ { p , s , b }$ to at most one. This corresponds with the fact that buyer b has a single unit in any pod of show s.

Pod protection B :

$$
\begin{array}{l l} f _ {p, s, b} \leq z _ {p, s, b} & p = 1, \ldots , P _ {s} \\ s = 1, \ldots , S & b = 1, \ldots , B \end{array}\tag{11b}
$$

Eq. (11c) will force $z _ { p , s , b }$ to 1 in this case.

When two or more units are assigned within the same pod of a show to a single bidder, thereby generating a potential 30-second or longer commercial, Eqs. (11a)–(11c) will force $z _ { p , s , b }$ and $f _ { p , s , b }$ to 1.

Pod protection C :

$$
\begin{array}{l} \sum_ {u = 1} ^ {U _ {p, s}} x _ {u, p, s, b} \leq z _ {p, s, b} + \left(\sum_ {p = 1} ^ {P _ {s}} U _ {p, s} - 1\right) f _ {p, s, b} \\ p = 1, \ldots , P _ {s} \quad s = 1, \ldots , S \quad b = 1, \ldots , B \end{array}\tag{11c}
$$

Finally, Eq. (11d) will keep competitors away from buyer b’s protected pod in show s.

Pod protection D :

$$
\begin{array}{l} f _ {p, s, i} + z _ {p, s, j} \leq 1 \quad i <   j, j = 2, \ldots , B \\ \forall M _ {i} = M _ {j}, \quad p = 1, \ldots , P _ {s} \quad s = 1, \ldots , S \end{array}\tag{11d}
$$

## 5. Heuristic development

A direct attack on solving problem P1 to optimality is probably doomed. For example, in a representative problem with 325 bidders competing for 587 units in 109 pods across 24 shows, P1 has approximately 278,000 binary variables and 587,000 constraints. A heuristic is clearly needed. The solution methodology employed to allocate units in our Incompletely Specified Combinatorial Auction is fairly complicated incorporating a mixture of strategies including aggregation and linear, constraint and dynamic programming methods.

The auction begins with the collection of bids. Each bid is subjected to an initial feasibility check to ensure that it meets minimum requirements for entry. This is accomplished by solving an aggregate problem defined below. Once all bids have been tendered, an initial feasible solution is generated with the use of heuristics. An upper bound is established using a linear relaxation of a second type of aggregate integer program. This bound is used to judge the quality of our solutions. The best solution to date is then used to start a branch and bound search. At the end of each auction round, the selected stopping criterion is checked. If stopping conditions are not met, bidders are informed of the results and losing bidders will have the opportunity to change their bids commensurate with their behavior profile.

When all stopping conditions have been met, the current bid amounts are replaced with bidder reservation prices (but otherwise unaltered) and the solution to this problem is used to calculate the mechanism’s efficiency.

## 5.1. Aggregate subproblems

The majority of constraints involved in the auction problem can be determined by examining the allocations of each show rather than a pod or unit level allocation. The overall driving heuristic is a greedy allocation of show advertising units to bidders. Each bid is considered sequentially, conditional on the tentative allocations made to other bidders. Let $\delta ( x )$ be the normal Kronecker delta function. Also, let $x _ { s , b }$ be the number of advertising units that bidder b purchases in show s and $X _ { s , b }$ be the current domain of $x _ { s , b } .$ . Using constraint programming methodologies, the domain of $x _ { s , b }$ will change as other variables associated with earlier accepted bids are instantiated either because units become unavailable or some constraint such as pod protection or maximum spots per show would be violated. As we will show, $X _ { s , b }$ incorporates all the constraints given in Eqs. $( 2 ) \mathrm { - } ( 1 1 \mathrm { d } )$ except for demographic reach and the desired shows constraints. These latter two are handled directly in the following aggregate problem.

We define the aggregated problem $( \mathsf { A P } _ { b } )$ for each bidder as

Aggregate problem

$$
\begin{array}{c} \sigma_ {b} = \min _ {x _ {s, b} \in X _ {s, b}} \sum_ {s = 1} ^ {S} L _ {s} x _ {s, b} (\mathrm{AP} _ {b}) \\ \sum_ {s = 1} ^ {S} D _ {s} x _ {s, b} \geq T _ {b} \end{array}
$$

$$
\underline {{H}} _ {b} \leq \sum_ {s = 1} ^ {S} h _ {s} \delta (x _ {s, b}) \leq \overline {{H}} _ {b}
$$

The aggregate problem formulation relies heavily on the domains $X _ { s , b }$ . A simple recursive procedure, detailed by Jones [13], shows how the domains are constructed. When there are no current other assignments, the objective value of $\mathrm { A P } _ { b }$ is labeled $\sigma _ { b } .$ , which gives the minimum show costs for bidder b needed to satisfy all problem constraints (2) – (11d). When there are current assignments meeting constraints (2) – (11d), then $\mathsf { A P } _ { b }$ provides an assignment for this bid (if it has a feasible solution) that, together with the current assignments, meets all constraints (2)– (11d). By minimizing the costs, we satisfy the one remaining constraint, Eq. (1), the seller reservation price constraint. A simple check confirms this. If the problem is not feasible due to a violation of the seller reservation price constraint, free-loading bidders are removed until the condition is satisfied.

If there is no feasible solution to $\mathrm { A P } _ { b } ,$ then we set the $x _ { u , p , s , b }$ variables to 0. Otherwise, a solution can be expanded to yield $x _ { u , p , s , b }$ values by recovering a combination yielding the correct entry in $X _ { s , b } .$ There may be many such combinations. No currently protected pod will be violated by these $x _ { u , p , s , b }$ values. If $\mathrm { A P } _ { b }$ has a feasible solution, then we set $y _ { b } = 1$ . If not, we set $y _ { b } = 0$ The remaining decision variables in the original problem P1 can be recovered by a simple analysis of the expanded solution $x _ { u , p , s , b } \mathbf { \hat { s } }$

The aggregate problem $\mathsf { A P } _ { b }$ is solved using dynamic programming methods. The final constraint can make this a nonlinear problem (because of the Kronecker operation) if either or both $\underline { { H } } _ { b }$ and $\overline { { H } } _ { b }$ are greater than 0 and the h’s have values necessitating the consideration of these constraints. We utilize one of several dynamic programming routines designed to solve the subproblem, the choice of which depends on the values of $\underline { { H } } _ { b }$ and $\overline { { H } } _ { b }$ and the bidder’s assignment of her $h \mathbf { \bar { s } }$ . The dynamic programs provide exact optimal solutions to $\mathrm { A P } _ { b }$ . However, these can take some time to solve since the $\pmb { T } _ { b }$ values may be large. At various points, to be discussed, we use a heuristic based on linear programming relaxations to give good (often optimal) solutions to the aggregate problem $\mathrm { A P } _ { b } .$ . We call these methods FastAP.

Just as we utilize one of several dynamic programming routines designed to solve the aggregate subproblem, we also have different FastAP versions. When the show selection constraints are not needed, this is a straightforward LP Knapsack problem. A slightly more complicated version is employed to satisfy show selection constraints. Each solution is refined using problem reduction methods that shrink the domains based on simple dominance tests.

## 5.2. Master problem

An overview of the master problem is presented in Fig. 1. The goal is to find a solution that maximizes seller profits while satisfying constraints (1) – (11d). To establish a good initial solution to the allocation problem, consider the following two greedy algorithms. Assume we are given B bids.

![](/api/attachments/Q66BRGP6/fulltext/images/cb96a0767361fbf99e6b1340c894f495948d01950d2f98e3eac0033be37112f2.jpg)  
Fig. 1. Heuristic flowchart

Step 1: Repeat the following until all bids have been processed.

Sort the remaining bids by some criterion of interest with the most desirable bid designated as the top-most bid. (In our application, we order the bidders in such a way that those which contribute the most to maximizing seller revenue are assigned first. We do this by selecting the bidder with the highest bid per thousand demographic requirements normalized by the cost of the specific demographic category and demand within that category).

Solve the aggregate subproblem for the top-most remaining bid and make the appropriate assignments to the variables of P1.

Step 2: While the amount bid by the selected bidders is less that the seller’s reservation price for the collection of allocated units, i.e.

$$
\sum_ {b = 1} ^ {B} a _ {b} y _ {b} <   \left(\sum_ {b = 1} ^ {B} \left(\sum_ {s = 1} ^ {S} \left(\sum_ {p = 1} ^ {P _ {s}} \sum_ {u = 1} ^ {U _ {p, s}} x _ {u, p, s, b}\right) L _ {s}\right)\right)
$$

Sort the remaining feasible bids by some criterion of interest with the least desirable bid designated as the top-most bid (i.e., the biggest freeloader).

Set the top-most active bid’s aggregate subproblem solution to infeasible and remove any current allocations to this bidder.

The above procedure yields a feasible solution to the auction problem since Step 2 guarantees the feasibility of the reservation requirement (1) and construction of the domains for each aggregate subproblem plus the constraints of $\mathsf { A P } _ { b }$ assures the feasibility of all the remaining constraints.

## 5.3. Branch and bound

Branch and bound techniques are employed to investigate the various combinations of bids that will maximize seller revenue. Since total enumeration of the various combinations is impossible, we utilize heuristics to guide our branching behavior. At each branch, we take the partial solution from predecessor branches and solve $\mathsf { A P } _ { b }$ or FastAP.

The amount of time allotted to computation in each round is predefined by the auction rules. We use time remaining to guide the search process. After preprocessing is complete, an initial solution determined and an upper bound on P1 computed, 30% of the remaining time is spent in a Breadth First Search (BFS), the rest is dedicated to a Depth First Search (DFS).

The Breadth First Search extends to three levels. This means that it looks at all orderings of all combinations of three bidders as the first three allocations— time permitting. Below level three, depth first search is used but is limited to a relatively small number of branchings (we use five times the number of bidders). Bids are initially ordered by the above heuristics to rank them so that the top-most bids contribute the most to maximizing revenue. However, conflicts between these bids may prevent all of these most desirable bids from achieving an allocation. The order in which the bids are processed affects the allocation so all permutations of the first three bids are explored. During the Breadth First phase, the FastAP heuristic is used.

A Depth First Search is employed during the final 70% of computational time to seek out the best combination of bids. This search is conducted in two stages, the first solves (AP<sub>b</sub>) exactly using dynamic programming and lasts for 60% if the time allotted. Stage 2 utilizes FastAP and runs until the conclusion of the computational time.

## 6. Experiments

Our experiments consisted of simulating the execution of our auction under various conditions to analyze the mechanism’s performance. Our simulation uses software agents to represent bidders for prime-time commercials. We do this not to suggest that these agents be used in an actual auction but merely as a way to test our mechanisms. A real implementation would use real bidders. Profiles for our simulated bidders were determined from an analysis of data received from a representative of a major television network. Based on such data, distributions for bidder reservation prices, demographic requirements, product category, and mix of commercial lengths were determined (see Ref. [13] for details). These distributions were used to randomly generate representative agents for our simulated experiment.

A bidding strategy was defined for each agent type used in the experiment based on results due to Bapna et al. [3], who identified three specific types of bidders in current online auction settings: Participators, Evaluators and Opportunists. Participators bid actively throughout the auction, Evaluators place a single bid representing their reservation price early in the auction, and Opportunists enter just before the auction’s close seeking bargains. Opportunists were not included in our study because the soft closing rules and semi-sealed environment does not provide bidders the necessary signal information to determine the auction’s end. Bid modification tactics are broken into six styles, five Participator types and one Evaluator type. Of the Participators, two modify their bid amount only, two modify both their bid amount and the constraints imposed on commercial placement and one modifies only the constraints. We define BidAdjustors as those bidders who modify the price they are willing to pay for an allocation. ConstraintAdjustors modify only the demand for, or restriction to, the shows included in the allocation, and AllAdjustors combine the techniques of bid and constraint modification. We further distinguish BidAdjustors and AllAdjustors into ‘‘max’’ and ‘‘min’’ types. A max(min) agent bids the maximum(minimum) of the minimum bid increment and the recommended bid increase specified by the auction mechanism. A preliminary set of experi ments was conducted to understand better various possible agent behaviors on the auction mechanism (see the first section of Table 3). Based on these results and advise from an industry expert, we generated 325 agents made up of roughly 5% Evaluators, 20% BidAdjustors-Max, 20% BidAdjustors-Min, 30% AllAdjustors-Max, 20% AllAdjustors-Min and 5% ConstraintAdjustors to capture a reasonable approximation of the marketplace. Our second simulation uses this framework, referred to as the Generic Bidder Set, to examine our auction mechanism under various conditions (see Table 2).

The measures used to evaluate the Incompletely Specified Combinatorial Auction’s performance are allocative efficiency, assignment optimality, and the length of the auction. When the seller always sells an object to the bidder with the highest realized valuation for that object, as long as that value is greater than the seller’s reservation price, the auction is said to be efficient [1]. While this measure is fairly straightforward in a single unit environment, complications arise when trying to evaluate efficiency for auctions involving package bids. In a combinatorial auction, one must consider the impact of overlapping demand for the various items that may limit the feasible allocation of units when determining a mechanism’s efficiency. To determine the efficiency of our auction, we define the final allocation of the auction mechanism as:

Experimental design for auction mechanism using Generic Bidder Set

<table><tr><td>Stopping rule</td><td>Minimum bid increment</td><td>Calculation time</td></tr><tr><td>Activity</td><td></td><td></td></tr><tr><td>Minimum revenue</td><td>5%, 10%, 15%</td><td>5, 15, 30, 60 min</td></tr><tr><td>Maximum round (10)</td><td></td><td></td></tr></table>

$$
y _ {b} (A) = \arg \max \sum_ {b = 1} ^ {B} a _ {b} y _ {b} \quad \text { s.t.   Constraints } \tag {1-11}\tag{1) - (11d}
$$

Further we determine an upper bound on the value attainable in the auction as:

$$
V ^ {*} = \max \sum_ {b = 1} ^ {B} v _ {b} y _ {b} \quad \text { s.t.   Constraints } (1) - (1 1 d)
$$

From these two equations, we can formulate an efficiency measure similar to those used in prior combinatorial auctions studies [4,8,17].

$$
E = \frac {\sum_ {b = 1} ^ {B} v _ {b} y _ {b} (A)}{V ^ {*}}
$$

Note that this is an estimation of the efficiency as it relies on the outcome of our heuristic that may not achieve an optimal solution to either problem. However, when solving each problem, we end with a range from our final feasible solution to a theoretical upper bound. This gap is often small and is reported in our experiments.

Optimal auctions are those that maximize seller revenue. Maximum revenue, in a single item auction, results from allocating efficiently then extracting as much buyer surplus as possible [22]. We report the percentage of the maximum possible revenue from the final allocation actually captured by the seller as our measure of optimality.

$$
\text { Optimality } = 1 - \frac {\sum_ {b = 1} ^ {B} (v _ {b} - a _ {b}) y _ {b} (A)}{\sum_ {b = 1} ^ {B} v _ {b} y _ {b} (A)}
$$

## 7. Results

The results from experiment one are shown in Table 3. The auction simulation consisting of all ConstraintAdjustors posted the best overall results. This bidder category was not only able to achieve the highest revenue but also had the highest number of winning bidders, had minimal or no unsold inventory and 100% optimality and efficiency. These results were achieved in as little as 14 rounds in most cases. The data show that auctions consisting of only AllAdjustors also performed well with regard to maximizing revenue, allocating units to a consistently high number of bidders and leaving very little inventory unsold. Evaluators also faired well posting the second highest achieved revenue, 100% efficiency and optimality, with only one or two units of unsold inventory. BidAdjustors underperformed, leaving significant amounts of inventory unsold, achieving the least amount of revenue, selecting the fewest winners and functioning poorly in terms of efficiency and optimality.

We also analyzed a uniform distribution of bidder types as well as the suggested generic distribution. As might be expected, the combination of bidder types had results somewhere between the two extremes of the flexible and inflexible bidder types. These results suggest that the auction performs differently with varying bidder characteristics. Since auction agents typically behave suboptimally, one should expect better results outside the simulated environment.

Table 4 shows the results from our second experiment. A Manova test was conducted to determine the impact of the independent variables (minimum bid increment, stopping rule, and calculation time) on the dependent variables (optimality, efficiency, and realized revenue). The results indicated that the minimum bid increment and stopping rule had a significant (at a 99% level) effect on the auction’s performance characteristics but the amount of calculation time given the heuristic did not.

An analysis of the data in Table 4 indicates that increasing the minimum bid increment yields greater seller revenue in less time. However, when using the activity stopping rule, the largest (15%) increment demonstrated a decrease of the maximum overall revenue from that achieved with a 10% increment. We attribute this to the fact that the agents are budget constrained and a high minimum increment forced budget constrained bidders out of the auction sooner, thus decreasing competition by reducing the bidder pool [26].

Table 3  
Experimental results for bidder behavior (activity stopping rule, 15-min calculation time, 5% minimum bid increment)

<table><tr><td colspan="12">Bidder distribution</td></tr><tr><td>Evaluators</td><td></td><td>100%</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1/6</td><td>5%</td></tr><tr><td rowspan="2">BidAdjustors</td><td>Min</td><td>0</td><td>100%</td><td>0</td><td>0</td><td>0</td><td>0</td><td>50%</td><td>0</td><td>1/6</td><td>20%</td></tr><tr><td>Max</td><td>0</td><td>0</td><td>100%</td><td>0</td><td>0</td><td>0</td><td>50%</td><td>0</td><td>1/6</td><td>20%</td></tr><tr><td rowspan="2">AllAdjustors</td><td>Min</td><td>0</td><td>0</td><td>0</td><td>100%</td><td>0</td><td>0</td><td>0</td><td>50%</td><td>1/6</td><td>20%</td></tr><tr><td>Max</td><td>0</td><td>0</td><td>0</td><td>0</td><td>100%</td><td>0</td><td>0</td><td>50%</td><td>1/6</td><td>30%</td></tr><tr><td>Constraint</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>100%</td><td>0</td><td>0</td><td>1/6</td><td>5%</td></tr><tr><td colspan="12">Results set 1</td></tr><tr><td>Revenue</td><td></td><td>25,472</td><td>23,451</td><td>20,031</td><td>26,042</td><td>24,414</td><td>27,393</td><td>22,496</td><td>25,337</td><td>24,866</td><td>24,579</td></tr><tr><td>Round achieved</td><td></td><td>3</td><td>22</td><td>11</td><td>20</td><td>16</td><td>18</td><td>16</td><td>22</td><td>12</td><td>15</td></tr><tr><td>Efficiency</td><td></td><td>100</td><td>94.39</td><td>86.67</td><td>96.04</td><td>93.48</td><td>100</td><td>90.47</td><td>95.30</td><td>95.62</td><td>96.07</td></tr><tr><td>Optimality</td><td></td><td>100</td><td>91.83</td><td>86.67</td><td>98.95</td><td>91.83</td><td>100</td><td>89.84</td><td>94.88</td><td>94.95</td><td>93.62</td></tr><tr><td>Unsold inventory</td><td></td><td>4</td><td>4</td><td>49</td><td>1</td><td>1</td><td>1</td><td>13</td><td>3</td><td>0</td><td>3</td></tr><tr><td>Number of winners</td><td></td><td>119</td><td>121</td><td>113</td><td>134</td><td>141</td><td>139</td><td>120</td><td>138</td><td>121</td><td>128</td></tr><tr><td>Percent bounded</td><td></td><td>11%</td><td>13%</td><td>10%</td><td>1%</td><td>5%</td><td>1%</td><td>11%</td><td>4%</td><td>7%</td><td>5%</td></tr><tr><td colspan="12">Results set 2</td></tr><tr><td>Revenue</td><td></td><td>25,345</td><td>23,552</td><td>20,566</td><td>26,263</td><td>24,164</td><td>27,405</td><td>22,752</td><td>25,554</td><td>25,056</td><td>24,451</td></tr><tr><td>Round achieved</td><td></td><td>5</td><td>11</td><td>12</td><td>14</td><td>14</td><td>14</td><td>19</td><td>14</td><td>20</td><td>16</td></tr><tr><td>Efficiency</td><td></td><td>100</td><td>97.71</td><td>93.07</td><td>98.54</td><td>92.76</td><td>100</td><td>93.04</td><td>97.84</td><td>96.27</td><td>95.76</td></tr><tr><td>Optimality</td><td></td><td>100</td><td>91.89</td><td>88.72</td><td>96.95</td><td>91.58</td><td>100</td><td>91.21</td><td>94.87</td><td>96.43</td><td>93.20</td></tr><tr><td>Unsold inventory</td><td></td><td>3</td><td>2</td><td>40</td><td>2</td><td>0</td><td>0</td><td>9</td><td>0</td><td>1</td><td>6</td></tr><tr><td>Number of winners</td><td></td><td>118</td><td>110</td><td>116</td><td>133</td><td>139</td><td>141</td><td>112</td><td>132</td><td>127</td><td>126</td></tr><tr><td>Percent bounded</td><td></td><td>9%</td><td>15%</td><td>18%</td><td>2%</td><td>4%</td><td>1%</td><td>13%</td><td>3%</td><td>9%</td><td>5%</td></tr></table>

Using the highest minimum bid increment produced the best optimality results. Generally, auctions that were able to extract the most surplus from the winning bidders required a 15% bid increment.

Experiments to determine the most efficient auction, or the auction that most effectively assigned units to the bidders that value them the most, produced less consistent results in terms of the impact of the minimum bid increment. When the auction was allowed to continue for several rounds, as in the case of those using the activity and maximum round (10) stopping rules, the higher percentage increases forced higher efficiency. This could be attributed to the fact that requiring a higher subsequent bid made the bidders’ true valuations surface earlier, thus giving the mechanism the opportunity to assign units to those with the highest revealed valuations. However, in the case of the minimum revenue stopping rule, the results were inconsistent between the 10% and 15% increments. Minimum revenue was achieved in round 3 under these parameters and one could speculate that the small number of rounds did not give an opportunity for those bidders with the highest true valuations to become the dominant bidders. Due to the short duration of the auction, it was not allowed to converge to equilibrium.

Another aspect of the auction influenced by the minimum increment percentage is the number of rounds needed to achieve competitive equilibrium. Tests showed that on average, when the activity stopping rule was employed, auctions requiring only 5% increments lasted an average of 22 rounds, 10% minimum increase auctions averaged 20 rounds, while those requiring at least 15% added to previous unsuccessful bids concluded in 19 rounds. Fig. 2 shows the revenue progression for 15-min calculation times. Notice that the higher the required increment, the faster the initial revenue gain; however, the 10% increment eventually achieves the highest revenue. In this case, budget constrained bidders were able to remain in the auction longer, giving the mechanism a greater opportunity to extract buyer surplus, thus increasing overall revenue.

Table 4  
Experimental results auction performance characteristics

<table><tr><td rowspan="2">Stopping rule</td><td colspan="2">Percent = 5%</td><td colspan="2">Percent = 10%</td><td colspan="2">Percent = 15%</td></tr><tr><td>5 min</td><td>15 min</td><td>5 min</td><td>15 min</td><td>5 min</td><td>15 min</td></tr><tr><td colspan="7">Revenue (000)</td></tr><tr><td colspan="7">Set 1</td></tr><tr><td>Activity</td><td>24,391.70</td><td>24,578.50</td><td>25,264.10</td><td>25,052.10</td><td>24,979.40</td><td>24,818.50</td></tr><tr><td>MinRev</td><td>23,146.70</td><td>23,487.20</td><td>23,538.10</td><td>23,617.70</td><td>23,377.90</td><td>23,284.90</td></tr><tr><td>MaxRound</td><td>24,387.60</td><td>24,522.30</td><td>24,919.10</td><td>25,143.20</td><td>24,869.20</td><td>25,069.40</td></tr><tr><td colspan="7">Set 2</td></tr><tr><td>Activity</td><td>24,409.40</td><td>24,334.10</td><td>24,641.60</td><td>24,588.60</td><td>23,593.50</td><td>24,849.00</td></tr><tr><td>MinRev</td><td>23,498.80</td><td>23,203.60</td><td>23,586.20</td><td>23,498.30</td><td>23,298.00</td><td>23,395.00</td></tr><tr><td>MaxRound</td><td>24,287.20</td><td>24,138.00</td><td>24,467.90</td><td>24,370.70</td><td>24,923.30</td><td>24,646.20</td></tr><tr><td colspan="7">Optimality (percent of bidder surplus extracted from winning bidders)</td></tr><tr><td colspan="7">Set 1</td></tr><tr><td>Activity</td><td>93.4445</td><td>93.6227</td><td>95.5487</td><td>95.2880</td><td>96.2838</td><td>95.4169</td></tr><tr><td>MinRev</td><td>91.0156</td><td>92.4770</td><td>93.9426</td><td>94.0618</td><td>93.3870</td><td>93.7843</td></tr><tr><td>MaxRound</td><td>93.4635</td><td>93.8447</td><td>95.3553</td><td>95.4414</td><td>95.7468</td><td>95.7616</td></tr><tr><td colspan="7">Set 2</td></tr><tr><td>Activity</td><td>93.2974</td><td>93.3839</td><td>94.0773</td><td>94.3596</td><td>94.7172</td><td>94.6865</td></tr><tr><td>MinRev</td><td>92.3043</td><td>91.9155</td><td>93.4855</td><td>93.3097</td><td>92.9948</td><td>93.2119</td></tr><tr><td>MaxRound</td><td>93.9622</td><td>92.6800</td><td>94.3917</td><td>93.9918</td><td>94.9689</td><td>94.3543</td></tr><tr><td colspan="7">Efficiency (ratio of the value of the winning bids to the highest attainable value for a feasible solution considering all bidders competing in the final round)</td></tr><tr><td colspan="7">Set 1</td></tr><tr><td>Activity</td><td>94.7058</td><td>96.0650</td><td>97.4008</td><td>96.5083</td><td>96.9639</td><td>96.7413</td></tr><tr><td>MinRev</td><td>89.4526</td><td>90.8648</td><td>91.5521</td><td>91.8615</td><td>98.0020</td><td>91.2745</td></tr><tr><td>MaxRound</td><td>93.9347</td><td>94.8273</td><td>95.0520</td><td>95.7361</td><td>95.7839</td><td>97.3613</td></tr><tr><td colspan="7">Set 2</td></tr><tr><td>Activity</td><td>96.4054</td><td>95.5788</td><td>95.2012</td><td>95.9128</td><td>97.3315</td><td>94.9535</td></tr><tr><td>MinRev</td><td>91.6006</td><td>90.6344</td><td>91.5030</td><td>91.3863</td><td>97.4600</td><td>91.8082</td></tr><tr><td>MaxRound</td><td>93.1122</td><td>92.5738</td><td>94.0633</td><td>94.1339</td><td>95.6039</td><td>94.3855</td></tr></table>

Evidence from the experiments conducted in this study indicates that the choice of stopping rule does indeed influence the mechanism’s performance characteristics. Table 4 details the variability of the performance measures between rules. As one might expect, the activity rule realized the best overall performance measures as it allowed the auction to converge to a natural stopping point. When the minimum revenue and maximum round (10) rules were employed, the auction stopped accepting bids even though there may have been bidders willing to participate, thus extracting less surplus and possibly inefficiently allocating units.

![](/api/attachments/Q66BRGP6/fulltext/images/00fc6e09f927b2293460d743c81749aa62adb2c20d412005f669557bae3ed17b.jpg)  
Fig. 2. Revenue attained and stopping round for each percentage increment.

While analyzing the data on auctions using the activity rule, we noted a phenomenon that we refer to as the Trickle Effect. In a number of the experiments, the bidding continued for several rounds yet there was no improvement in revenue. The auction did not terminate since, during each round, at least one revised bid was submitted. A more detailed look at the data indicated that the majority of revisions were being made to constraints, for example decreasing the number of shows required. Due to the nature of the multi-criteria bid, a bidder could conceivably enter a highly restrictive low bid in the initial rounds and continue making modifications to constraints and or her bid amount for an extended number of rounds. There may be some merit to this approach; the bidder could be attempting to obtain signal information from the recommended bids provided by the mechanism. This type of bidding could prolong the auction beyond a natural stopping point.

The final controlled variable in our experiments is the calculation time given our heuristic to determine an allocation. We experimented with four periods, 5, 15, 30 and 60 min. The preliminary results from tests using the activity stopping rule indicated there was no significant improvement from the longer 30- and 60-min runs. Therefore, we tested the remaining closing rules using only 5- and 15-min calculation times. Refer to Table 4 for a summary of the impact on the performance measures from altering the calculation time.

It was anticipated that the longer the mechanism was given to determine an allocation, the better that allocation. However, at first glance it would appear that on occasion, the additional calculation time had a negative effect on the performance parameters. We were able to attribute the occasional reduced performance to the ability of our mechanism to find earlier allocations for more bidders given longer calculation times. Although the auction performs better in initial rounds, improvement in later rounds is reduced because the broader early allocations reduce the ability of the mechanism to extract buyer surplus. Additionally, results from a Manova, testing the impact of calculation time on optimality, efficiency, and realized revenue, indicated that the time given to the mechanism to determine an allocation is not a significant factor influencing the auction’s performance characteristics.

The solution to the integer problem presented in Section 4 acts as a benchmark against which we compare our heuristic’s performance. To facilitate achieving a solution using a commercial integer programming solver, CPLEX 6.5, the problem had to be scaled down considerably from the size represented in the previous experiments. The reduced problem consists of 30 bidders vying for 104 units distributed across 3 shows. We chose to compare the results from one round of activity. The integer problem was generated using the parameters of the third round of bidding from an auction using 5 min of calculation time, 10% minimum bid increments and the activity stopping rule. The number of active bidders in round 3 had been reduced to 12 from the original 30. With the above parameters, the Incompletely Specified Combinatorial Auction was able to complete the entire auction consisting of five rounds in a total of 15 min. The duration of the auction includes time used to generate agents, calculate upper bounds, output an MPS formatted version of the problem for CPLEX at each auction round, output all solution files for possible CPLEX usage as well as determine the appropriate allocation of units in each of the five rounds. The ISCA found a solution that produced revenue of US\$1728.31 for the seller with a gap less than 0.04%. The small gap suggests that this answer may be optimal.

The integer programming problem representing a single round of the auction was entered into CPLEX. After over 43 hours, the program was unable obtain a single feasible integer solution. We then seeded CPLEX with the solution obtained by our mechanism for round three. CPLEX confirmed that the solution was indeed feasible and after 24 hours was unable to improve on the solution. The initial gap reported by CPLEX for this solution was 43.74%, significantly higher than that achieved by the heuristic. All of the runs were performed on the same 600 MHz, dual processor, Windows 2000 machine.

## 8. Limitations

This research presents a preliminary investigation into a new auction mechanism. The nature of the investigation has important limitations. First, in order to gain insight into the efficacy of the mechanism, we have limited our experiments to simulation with artificial agents. We acknowledge the fact that all nuances inherent to human behavior cannot be adequately programmed into agents. Additional human trials are necessary.

Our model accommodates the sale of a week of airtime and we make the simplifying assumption that buyers’ campaigns are continuous and thus the purchase pattern will repeat from week to week throughout the year. In reality, many buyers will want to ‘‘flight their campaigns,’’ or place advertising only during specific weeks or days of the year. In order to accommodate flighting, our mechanism will need to be expanded to 52 weeks and accept buyer-specified airdates. Extending our simple bid structure to 52 weeks will be challenging.

Finally, our mechanism is designed to assist or replace a negotiated environment, yet we have not attempted to analyze the business process changes necessary to facilitate the transition. We anticipate, especially in the television industry, that conversion from negotiation to a business-to-business electronic auction may be met with a great deal of resistance.

## 9. Conclusions and future research

This research has presented evidence that computersupported on-line auctions can be developed to accommodate the special needs of a traditionally negotiated environment. The mechanism designed in this study accepts rule-based bids, providing guidelines to direct rather than dictate the allocation of goods. Bidders are also given the ability to impose restrictions on the allocation through specifications of the multi-criteria package bid. Experiments establish the Incompletely Specified Combinatorial Auction mechanism is efficient and revenue maximizing. The heuristic developed accommodates large problem dimensions inherent in this environment and tests indicate that the solutions are near optimal. As important, the time it takes the heuristic to reach a satisfying solution is minimal and well within the limits imposed by the real-world environment. The development and proven efficacy of the mechanism described in this research suggests effective electronic auction mechanisms can be developed to support complex environments.

As indicated earlier, this is a preliminary study of our mechanism and as such, there is a great deal yet to discover about the mechanism’s use as well as new design issues to explore. Several design modifications are of interest. For example, the mechanism could be extended to become a market clearinghouse by incorporating all market participants (i.e., the entire network and cable industry). Additionally, the current design does not allow the bidder to reject an allocation. It can be argued that since the units assigned are not necessarily completely specified by the buyer, due to the inexact nature of the bid, that the buyer should have the option to reject an individual allocation. A doublesided auction would provide the necessary bid-ask format to facilitate the bidder’s rejection of an unacceptable allocation. Additionally, not all industries are as protective of their pricing and inventory information as the one represented in this study, therefore an obvious model modification would be to design an open format that provides signal information to buyers.

One of the limitations of this research is the use of simulation as the sole means of testing the mechanism’s performance. An experimental study using human subjects would supplement our understanding of the effectiveness of the auction mechanism. Several issues, such as human computer interaction, complexity, trust, collusion, and bidding strategies, can be explored empirically. Establishing bidder trust in a semi-sealed auction has, to our knowledge, not been investigated, yet could be a defining issue on the mechanism’s acceptance. The fact that the mechanism suggests bids to inactive buyers implies that the mechanism must be considered trustworthy if bidders are to act on the information provided. Another question about the semi-sealed format is its impact on collusion. Sealed-bid auctions are less susceptible to collusion than are open auctions because actual bids are not displayed allowing bidders to deviate from collusive pricing agreements without fear of detection [19,20]. It would appear that the same results would hold for the semi-sealed format but this has yet to be investigated.

Finally, although the heuristic developed in this study proved to be effective and timely for winner determination, other solution methodologies and mechanisms should be investigated. For example, our results show that a high percentage of bidder surplus was extracted, but a post-auction settlement, perhaps akin to the Vickrey–Groves –Clarke procedure, might produce a better truth-revealing bidding mechanism (see, for example, Ref. [24]).

## Appendix A. Summary of notation

$u , p , s , b , i$ Subscripts s = show, b = buyer, p = pods, u = pod part, i = allowable commercial length (using this order) $S$ Number of shows $P _ { s }$ Number of pods in show s $L _ { s }$ List price for each 15-second unit in show s $\pmb { D } _ { s }$ Vector of 15-second demographic values for show s $U _ { p , s }$ Number of 15-second portions in pod p for show s $C _ { s }$ Maximum number of total units in show s available to sell $B$ Number of buyers

$\pmb { T } _ { b }$ Target vector of desired demographic impressions for buyer b

$\pmb { h } _ { b }$ Vector of desired shows for buyer b $( h _ { s , b } = 1$ if show s is desired by buyer $b , 0$ otherwise; note that $\pmb { h } _ { b }$ can be a zero vector)

$N _ { s , b }$ Set of specified commercial length(s) in show s for buyer b

$\overline { { N } } _ { s , b }$ Set of allowable commercial length(s) in show s for buyer b

$\underline { { H } } _ { b } , \overline { { H } } _ { b }$ Min/max number of desired shows that buyer b must have $( \underline { { H } } _ { b } \le h _ { b } \le \overline { { H } } _ { b } )$

$K _ { s , b }$ Number of correct length commercials allowed in show s by buyer b

$$
M _ {b}
$$

$$
v _ {b} (\boldsymbol {d})
$$

$$
b ^ {\prime} \mathrm{s}
$$

$$
a _ {b}, h _ {b}, \underline {{H}} _ {b}, \overline {{H}} _ {b}, \boldsymbol {T} _ {b}, N _ {s, b}, M _ {b}, K _ {s, b}
$$

parameters of bid submitted by buyer $b ( a _ { b }$ i the amount bid)

## Binary decision variables

$f _ { p , s , b }$ DV: 1 if bidder b has more than 15 seconds in pod p in show s.

$y _ { b }$ DV: 0,1 variable. If 0, buyer b cannot buy any pods p.

$x _ { u , p , s , b }$ DV: 0,1 variable. If 1, buyer b has spot u in pod p in show s.

$I _ { p , s , b , i }$ DV: 0,1 variable. If 1, pod p of show s for buyer b uses an allowable number (i) of advertising slots.

$z _ { p , s , b }$ DV: 0,1 variable; 1 if $\begin{array} { r } { \sum _ { i \in \overline { { N } } _ { s , b } } I _ { p , s , b , i } = 1 } \end{array}$ otherwise 0. (Used for notational simplicity.)

$j _ { s , b }$ DV: 0,1 variable. If 1, buyer b has any unit in show s.

## References

[1] M. Armstrong, Optimal Multi-Object Auctions, Unpublished working paper Nuffield College, Oxford, UK, 1999.

[2] J.S. Banks, J.O. Ledyard, D. Porter, Allocating uncertain and unresponsive resources: an experimental approach, The Rand Journal of Economics 20 (1989) 1 – 25.

[3] R. Bapna, P. Goes, A. Gupta, A theoretical and empirical investigation of multi-item on-line auctions, Information Technology and Management 1 (1) (2000) 1 – 23.

[4] M.M. Bykowsky, R.J. Cull, J.O. Ledyard, Mutually destructive bidding: the FCC auction design problem, Journal of Regulatory Economics 17 (3) (May 2000) 205 – 228.

[5] S.Y. Choi, A.B. Whinston, The Internet Economy: Technology and Practice, Smart Econ Publishing, Austin, TX, 2000.

[6] C.Y. Coleman, Two start-up plans to market unsold radio time on the web. Wall Street Journal, November 12, 1999.

[7] P.C. Cramton, The PCS spectrum auctions: an early assessment, Journal of Economics and Management Strategy 6 (3) (1995) 431–495.

[8] C. DeMartini, A.M. Kwasnica, J.O. Ledyard, D. Porter, A new and improved design for multi-object iterative auctions. Caltech Social Science Working Paper No. 1054, November 1998, revised September 1999.

[9] R. Engelbrecht-Wiggans, Auctions and bidding models: a survey, Management Science 26 (2) (1980) 119– 142.

[10] M. Harris, A. Raviv, Allocation mechanisms and the design of auctions, Econometrica 49 (1981) 1477 – 1499.

[11] C.A. Holt Jr., Competitive bidding for contracts under alternative auction procedures, Journal of Political Economy 88 (1979) 433 – 445.

[12] E.L. Johnson, G.L. Nemhauser, M.W.P. Savelsbergh, Progress in linear programming — bases algorithms for integer programming: an exposition, INFORMS Journal of Computing 12 (1) (Winter 2000) 2 – 23.

[13] J.L. Jones, Incompletely specified combinatorial auction: an alternative allocation mechanism for business-to-business negotiations. Doctoral Dissertation, University of Florida, 2000.

[14] F. Kelly, R. Steinberg, A combinatorial auction with multiple winners for universal service, Management Science 46 (2000) 586–596.

[15] E. Kutanoglu, S.D. Wu, On combinatorial auction and Lagrangean relaxation for distributed resource scheduling, IIE Transactions 31 (1999) 813– 826.

[16] A.A. Lazar, N. Semret, Design and analysis of the progressive second price auction for network bandwidth sharing, Presented at 8th International Symposium on Dynamic Games and Applications, Maastricht, The Netherlands (July 1998) and at the DIMACS Workshop on Economics, Game Theory, and the Internet, Rutgers, NJ (April 1997).

[17] J.O. Ledyard, D. Porter, A. Rangel, Experiments testing multiobject allocation mechanisms, Journal of Economics and Management Strategy 6 (3) (1997) 639– 675.

[18] J. McMillan, Selling spectrum rights, Journal of Economic Perspectives 8 (3) (1994) 145 – 162.

[19] W.J. Mead, Natural resource disposal policy — oral auction versus sealed bid, Natural Resources Planning Journal M (1967) 194 – 224.

[20] P. Milgrom, Auction theory, in: T.F. Bewley (Ed.), Advances I Economic Theory: Fifth World Congress, Cambridge Univ. Press, Cambridge, 1987.

[21] P. Milgrom, Auctions and bidding: a primer, Journal of Economic Perspectives 3 (3) (1989) 3 – 22.

[22] R.B. Myerson, Optimal auction design, Mathematics of Operations Research 6 (1) (1981) 58 – 73.

[23] D.C. Parkes, L.H. Ungar, Iterative combinatorial auctions: theory and practice, Proceedings of 17th National Conference on Artificial Intelligence (AAAI-00), 2000, pp. 74 – 81.

[24] D.C. Parkes, L.H. Ungar, Preventing strategic manipulation in

iterative auction: proxy agents and price adjustment, Proceedings of 17th National Conference on Artificial Intelligence (AAAI-00), MIT Press Cambridge, MA, 2000, pp. 82 – 89.

[25] S.J. Rassenti, V.L. Smith, R.L. Bulfin, A combinatorial mechanism for airport time slot allocation, Management Science 44 (8) (1982) 1131– 1147.

[26] M.H. Rothkopf, R.M. Harstad, On the role of discrete bid levels in oral auctions, European Journal of Operational Research. 74 (1994) 572– 581.

[27] M.H. Rothkopf, A. Pekecˇ, R.M. Harstad, Computationally manageable combinational auctions, Management Science 44 (8) (1998) 1131–1147.

[28] J. Stewart, Dot.coms on NAPTE Floor. Spots-n-dots: The Daily News of TV Sales, Friday, January 28, 2000.

[29] J. Teich, H. Wallenius, J. Wallenius, A. Zaitsev, A multiple unit auction algorithm: some theory and a web implementation, Electronic Markets 9 (3) (1999) 1 – 7.

[30] Y. Vakrat, A. Seidmann, Analysis and design models for online auctions, Presented at INFORMS 4th Conference on Information Systems and Technology, May 26, 1998.

[31] W. Vickrey, Counterspeculation, auctions, and competitive sealed tenders, The Journal of Finance 16 (1961) 8 – 37.

[32] J. Weaver, How Much Do I Hear for that Ad? MSNBC News Article. http://www.msnbc.com/news.325684.asp., Oct. 25, 1999.

[33] M.P. Wellman, W.E. Walsh, P.R. Wurman, J.K. MacKie-Mason, Auction protocols for decentralized scheduling, Presented at the. Eighteenth International Conference on Distributed Computing Systems, Amsterdam, May, 1998.

[34] P.R. Wurman, M.P. Wellman, W.E. Walsh, A Parameterization of the auction design space, Games and Economic Behavior 35 (1/2) (Apr. 2001) 271– 303.

![](/api/attachments/Q66BRGP6/fulltext/images/4d05c360b747ecd525866a228d55a5c3dfa90c6cd90e3f0174a673b955dab8d3.jpg)  
Joni L. Jones is an Assistant Professor in the Computer and Information Systems Department at the University of Michigan School of Business. She is the recipient of the Michael R. and Mary Kay Hallman Electronic Business Research Fellowship. Dr. Jones received her doctorate in Decision and Information Sciences from the University of Florida Warrington College of Business.

![](/api/attachments/Q66BRGP6/fulltext/images/95a932238e0463715decdbc09f6477f7791743b269b87c0c296c58629ec96635.jpg)  
Gary J. Koehler is the John B. Higdon Eminent Scholar and Professor of Decision and Information Sciences in the Warrington School of Business at the University of Florida. He was recently Professor and Area Head at the Krannert Graduate School of Management at Purdue University.
