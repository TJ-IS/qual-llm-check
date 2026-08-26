---
otero_id: 21007
otero_key: "AHAKJCEF"
title: "Comparative analysis of multi-item online auctions: evidence from the laboratory"
authors: "Ravi Bapna; Paulo Goes; Alok Gupta"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00107-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Comparative analysis of multi-item online auctions: evidence from the laboratory

Ravi Bapna <sup>a</sup>, Paulo Goes <sup>b</sup>, Alok Gupta <sup>b,)</sup>

Northeastern UniÕersity, Boston, MA, USA

<sup>b</sup> Department of Operations and Information Management, U-2041, School of Business Administration, UniÕersity of Connecticut, Storrs, CT 06269-2041, USA

## Abstract

The dynamics of customer relationship are being reshaped by price-setting processes such as online auctions. This paper analyzes price setting process in business-to-consumer B2C online auctions. Typically, these auctions involve multiple Ž . identical units and utilize a variant of the traditional English-auction mechanism. We describe an online laboratory experiment that compares the efficiency of such a mechanism with a multi-item version of Vickrey’s Journal of Finance 41<sup>w</sup> Ž . 1961 8. second-price auction with respect to both seller’s revenue and allocative efficiency. Our results reject the revenue<sup>x</sup> equivalence principle and indicate that English auctions may dominate the Vickrey auctions. However, we observe that the allocative efficiency of Vickrey auctions is higher than the English auctions. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Online auctions; Electronic commerce; Laboratory experimentation; CRM

## 1. Introduction

The emergence of widespread commercial activity over a ubiquitous Internet Protocol based network of networks has brought about significant changes in the relationships between businesses and consumers. Armed with increased access to information and the absence of spatial and temporal constraints, consumers, who previously were resigned to be mere price-takers, are now empowered to influence the price-setting process 17 . This is best reflected in the<sup>w</sup> <sup>x</sup> growing popularity of online auctions and their emergence as a viable mercantile process in the electronic marketspace, both from the point of view of consumers and businesses. Online auctions have fueled the fire of dynamic pricing on the web and have given consumers an alternative to the fixed posted price mechanism.

The issue of facilitating competitive price setting is an important but ignored part of the discussion in the customer relationship management CRM litera- Ž . ture. The primary focus of CRM is to optimize customer interaction in all aspects of customer relationships 24,27 . We contend that providing compet- <sup>w</sup> <sup>x</sup> itive pricing has to be one of the foundation stones for CRM. Online auctions provide consumers intimacy with the price-setting process, and above all, the possibility of a bargain. As a result, they are now a critical mechanism in the portfolio of mercantile processes of all major e-tailers, such as Amazon and Yahoo. These auctions provide a sense of fairness and competitive thrill to the consumers and help in building brand loyalty, which could then spill into cross channel payoffs from increased posted price sales.

Businesses, on the other hand, are looking towards auctions to liquidate excess inventory, facilitate price-discovery for items that are otherwise difficult to price, and to enhance portions of the supply chain, such as procurement. Significantly, companies such as Ebay are pioneering new secondary markets, and, in the process, raising consumer-to-consumer competitive exchange to levels that were unimaginable just a few years ago.

While both consumer-to-consumer and businessto-business online auctions promise to occupy a prominent place in the emerging electronic marketplace we focus our analysis on the business-to-consumer B2C category. Cambridge, MA-based For- Ž . rester Research has predicted that B2C interactions would account for 66% of a US\$19 billion consumer-related online auction market by 2003, with the remaining 34% belonging to the consumer-toconsumer category.

Van Heck and Vervest 31 called for an extensive<sup>w</sup> <sup>x</sup> examination of the pervasive impact of advance electronic communication on the theory and practice of auctions. Klein and O’Keefe 18 present an overview<sup>w</sup> <sup>x</sup> of the impact the Web is having on the viability, operation and diffusion of the practice of auctions. Bapna et al. 4,5 comprehensively summarize the<sup>w</sup> <sup>x</sup> online auction landscape and pay close attention to the workings of auctions in the B2C domain. They observe that the majority of these B2C auctions involve multiple items, which incidentally is a much-neglected area of research in auction theory. In contrast, most consumer-to-consumer online auctions involve single items. This is primarily due to the special interest or collectible nature of merchandise that is sold using this channel. There is a lack of theoretical work in the area of multi-item auctions as stated by McAfee and McMillan 21 and by Mil-<sup>w</sup> <sup>x</sup> grom 25 . <sup>w</sup> <sup>x</sup>

The utilization of multiple item auctions in the B2C domain makes sense if one examines the kind of merchandise being sold. The majority of these auctions involve multiple units of identical goods such as rapidly aging computer hardware and consumer electronics. The global reach of the Internet provides a critical mass of consumers who are interested in these goods, which in turn makes the auctioning of multiple units of items at a time feasible. This accelerates the process of clearing aging inventory, and clears shelf space for current models that are likely to provide higher returns and could be sold using the integrated, traditional posted-price storefront that accompanies most prominent B2C auction sites Onsale and Egghead have now merged . GivenŽ . the wide dispersion in consumers’ valuations across the globe, firms are discovering that using auctions to dispose aging inventory is far more attractive than extracting a small salvage value for these ‘obsolete items. After all, what is obsolete in one part of the globe may yet be of significant value in another.

The key research question in this paper is how the current online auction mechanisms used in the B2C domain compare with their theoretical or practical counterparts. Given the wide variety of mercantile processes in the B2C space, such as posted price, auctions, reverse auctions http: Ž <sup>rr</sup>www.reverseauction.com , and quantity discounts http:. Ž <sup>rr</sup>www. mobshop.com or http:<sup>rr</sup>www.mercata.com , what. are the implications on consumers who have a process choice to make and subsequently strategize on how much to bid. Some recent work by Mehta and Lee 23 compared posted price vs. auctions for the<sup>w</sup> <sup>x</sup> sale of same goods from the point of view of the consumers’ welfare. Their preliminary analysis found evidence of winner’s curse in that Anon-expertB bidders paid 18.5% more than would be considered the rational price.

Bapna et al. 4 observe that the majority of<sup>w</sup> <sup>x</sup> multi-item online auctions involve indivisible goods and are open, ascending and pay-your-bid type of auctions termed MIPEA, for Multiple Item Progres-Ž sive Electronic Auctions . Thus, they resemble the. English auction process, with the difference that most auctioneers endogenously set a bid-increment and hence at any given instance, only a subset of the current winning bidders is affected by an incoming higher bid. This discretizes the commonly assumed continuous probability structure surrounding the auctioneer’s revenue and leads to interesting strategic behavior among bidders. A secondary research objective of this paper is to examine the impact of different bid-increment levels on the revenue generation process of MIPEA.

Another variety of B2C auctions observed on the web is termed a Dutch auction by sites such as Ebay.com and Amazon.com. However, unlike the traditional Dutch auction that is descending in nature and most closely resembles the sealed-bid first price auction in the single-item case , the auction mecha- Ž . nism offered by Ebay is a multi-item, progressively ascending, uniform price, lowest winning bid, open auction. For instance, if five identical units were being auctioned, the five highest bidders would win and would pay the same price that is equal to the lowest winning bid. The openness of Dutch auctions ironically negates the important incentive compatibility property that comes along with the sealed-bid versions of such auctions 32 . In on-line Dutch<sup>w</sup> <sup>x</sup> auctions, rational individuals do not have the incentive to reveal their true valuations. Instead, they utilize the extra information they receive in the form of their competitors’ bids and derive a new set of preferences that may or may not coincide with their true valuations. Theoretically, this implies that the allocative efficiency of such mechanisms is dominated by mechanisms that are incentive-compatible. Allocative efficiency is defined as the ratio of auctioneer’s revenue plus consumers’ surplus allocated by the mechanism under consideration to the allocation if there were full demand revelation, i.e., consumers’ bid their true valuations 1,10 .<sup>w</sup> <sup>x</sup>

While the rewards of observing real-world economic agents participate in meaningful exchange are many, the one drawback is the lack of control that a researcher can exert to isolate her variables of interest. It is here that controlled laboratory experimentation methodology is a perfect fit. In such environments, all factors other than the one being tested can be controlled and in the process can reinforce or refute empirical and analytical findings.

In this paper, we describe a controlled laboratory experiment to compare the MIPEA mechanism with a sealed-bid, uniform price, highest-rejected bid multi-item auction that is based on Vickrey’s 32 <sup>w</sup> <sup>x</sup> original, incentive-compatible, second-price auction. While not as widespread yet as the MIPEA, we would like to point out that major financial institutions such as OpenIPO.com a subsidiary of WRŽ . <sup>1</sup> Hambrecht are in fact using the MVA auction.

We also discuss the implication of our results in the context of Ebay’s ‘Dutch’ auction that possesses some of the features of the Vickrey auction without the incentive compatibility property. We are able to derive results that compare the auction mechanisms in terms of the revenue generated and the allocative efficiency.

In the next section we present the prior research in this area. In Section 3 we describe the experimental design, which is based on the induced values theory. In Section 4 we present our test hypothesis and results, and in Section 5 we discuss directions for future research.

## 2. Prior research

Most researchers attempting to test the predictions of auction theory have been forced to rely on the experimental laboratory to simulate real-world behavior. Empirical research has been rare due the lack of meaningful data sets, which in turn could be attributed to the lack of mainstream appeal of auctions. The best data set available prior to the arrival of the web-based auctions covers US Forest Service sales of contracts for harvesting timber in the Pacific Northwest during 1977. Hansen 14 uses this data<sup>w</sup> <sup>x</sup> set to provide evidence in favor of revenue equivalence between a sealed-bid and an open auction under a common-values setting. This is in contrast to earlier work by Mead et al. 22 , which reported a roughly 10% higher price with sealed-bid auctions. Early lack of empirical and<sup>r</sup>or realistic experimental test environments is increasingly disappearing with the technological advancements in online auction technology. The widespread popularity of online auctions, coupled with the open computing paradigm upon which the Internet applications are built, together present a golden opportunity for researchers to revisit the various branches of auction theory in a setting that is more realistic and has higher inductive value.

Lucking-Reiley 20 acknowledges the difficulty<sup>w</sup> <sup>x</sup> in obtaining field data that allows for testing of equivalences between the basic auction. His field experiments that auction collectible magic cards to real world subjects involve real monetary payoffs and utilize a natural web based interface that is familiar to consumers interested in his wares. While testing the revenue equivalence of single-item auction formats, Lucking-Reiley 20 finds that Dutch<sup>w</sup> <sup>x</sup> auctions yield 30% higher revenues than the firstprice auction formats and that the English and second-price formats produce roughly equivalent revenues. This contradicts the theoretical predictions of revenue equivalence.

Of late there is evidence of research spawning in multi-item auctions. List and Lucking-Reiley 19<sup>w</sup> <sup>x</sup> examine the case when consumers are allowed to bid for more than one item under two different types of two-unit, two-person sealed bid auctions. When consumers are allowed to bid for more than one-item in an m-item auction, Vickrey’s original proposition— full demand revelation occurs in a sealed-bid auction —does not hold 2 . Instead, the rule has to be<sup>w</sup> <sup>x</sup> modified such that for an m-item Vickrey auction bidders can submit as many indiÕidual unit bids as they like. Further, the top m bids are declared winners and for the jth unit won by a bidder, she pays an amount equal to the jth highest of the rejected bids submitted by others 9,13 . Hence, this revised <sup>w</sup> <sup>x</sup> mechanism offers discriminating prices in contrast to the original mechanisms’ uniform pricing. Appendix A provides an example that differentiates these two mechanisms.

In the two-item case, List and Lucking-Reiley <sup>w</sup> <sup>x</sup> 19 indicate that there is evidence of demand reduction, i.e., lowering of the second bid below the true valuation, when the uniform-pricing rule is applied. This is a cause for concern and leads to lower allocative efficiency. In the case of real-world B2C online multi-item auctions consumers are allowed to bid for more than one-item but these bids cannot be discriminating, i.e., they all have to be of the same amount. For instance, a given individual can bid for three items at US\$100 each but cannot bid for two items at US\$110 and one item for US\$80. Whether this constraint is designed to prevent demand reduction in auctions that sell multiple far greater thanŽ two units is an open and interesting research ques- . tion.

Bapna et al. 4 raise the revenue comparison<sup>w</sup> <sup>x</sup> question for multi-item online auctions while analyzing the revenue structure of MIPEA. Because of the lack of real-world data from auction mechanisms other than the MIPEA, they rely on estimating the revenues of alternative mechanisms by extrapolating the behavior of bidders under MIPEA to other mechanisms. They assume that net-worth maximizing rational bidders under MIPEA would shave their valuations by at least one bid-increment and utilize this to estimate revenue from multi-item extension of Vickrey’s original single-item uniform highest-rejected-bid auction termed MVA, for Multiple Vick-Ž rey Auction . Thus, the conjecture was that assuming . that the MVA is incentive-compatible, an individual bidding US\$ x would be willing to bid US\$Ž . x<sup>q</sup>k under MIPEA where k represents the bid-increment.

Another interesting analytical and empirical finding of Bapna et al. 4 was that the hitherto unde- <sup>w</sup> <sup>x</sup> scribed discrete and sequential nature of MIPEA, caused by the presence of the bid increment, had a significant impact on the revenue realization process. Thus, we extend our experimental objective to test whether for the same item, can yield different choices in the bid-increment yield different revenues.

There have been other attempts to compare the efficiency of different auction mechanisms both theoretically and empirically 8 . The focus has been on<sup>w</sup> <sup>x</sup> comparing single-item sealed-bid competitive auctions with sealed-bid discriminatory auctions. In the former mechanism, the highest bidder wins; however, the price paid is the second highest bid, whereas in the latter the highest bidder wins with the price being the highest bid. Competitive auctions were first suggested by Vickrey 32 in his seminal article; <sup>w</sup> <sup>x</sup> the special property of this mechanism is that all the bidders have incentive to bid their true valuation. Plot and Smith 26 were among the first to design a <sup>w</sup> <sup>x</sup> controlled laboratory experiment to compare competitive auctions with discriminatory auctions. Actual bidding data have also been analyzed by various researchers such as Baker 3 . The key results of<sup>w</sup> <sup>x</sup> these empirical investigations have been inconclusive with respect to sellers’ revenue. Harris and Raviv 15 compare the efficiency and expected rev-<sup>w</sup> <sup>x</sup> enue of the uniform price Vickrey-like auctionŽ . mechanism with that of the discriminating first priceŽ sealed-bid mechanism when a fixed quantity of. diÕisible goods are to be sold to many buyers. Their results indicate that the sellers’ revenue under a specific mechanism depend on the risk characteristics of the bidders.

To the best of our knowledge, our work represents the first analysis and comparison of expected revenue between a discriminatory open ascending auction and a competitive Vickrey sealed-bid auc-Ž . tion with multiple units of indiÕisible goods and multiple buyers.

In this paper we revisit the revenue equivalence question through the controlled environment of a laboratory experiment. Much like Lucking-Reiley’s work, we exploit the online auction technology to create an environment that closely resembles its real-world counterpart. The only methodological difference between our laboratory environment and that of Lucking-Reiley’s field experiment is that whereas his subjects are drawn from the real world we choose to control within-subject variation by utilizing undergraduate student subjects. The commodity being auctioned is picked from the list of goods that are commonly sold in the real-world online B2C auction domain and our web interface closely resembles real auctions conducted on the web. Both approaches utilize salient monetary incentives.

In summary, the objectives for our controlled laboratory experiment are as follows. First, keeping everything else constant we compare the auctioneer’s revenue from the typical B2C online auctions with that from the MVA. Second, keeping everything else constant we assess the impact of the bid increment on the auctioneers’ revenues. Finally, we investigate the allocative efficiency of these mechanisms with respect to the aforementioned treatments.

## 3. Experimental design

To answer the above-mentioned research questions we created an online auction environment utilizing state-of-the-art interactive web development technologies Javascript and dynamic HTML for theŽ front end, and an IDC<sup>r</sup>HTX connection to an ODBC data source for the back end that closely resembles. its real-world counterpart. Student subjects are typical Internet users and we deal with real goods that are sold in similar real-world online auctions. Importantly, the web based auction environment is identical to its real-world counterpart and allows us to isolate the impact of our treatment variables. In the next subsection we set the stage for our experiment by elaborating on the incentive structures that we designed for the different economic agents involved. As with any laboratory experimentation, the key concern was that the results obtained from the laboratory should have real-world implications.

## 3.1. InductiÕe Õalue and incentiÕe mechanism

The question of inductive value of our exercise is a key one. An economic experiment consists of agents e.g., buyers and sellers and market institu-Ž . tions e.g., different types of auctions . For an exper-Ž . iment that takes place in a controlled economic environment of a laboratory to have general theoretical implications, one cannot rely on deductive logic. Instead, we have to rely on the general principle of induction, which maintains that behavioral regularities will persist in new situations as long as the relevant underlying conditions remain substantially unchanged. An important underlying condition for the successful design of a controlled economic experiment is the ability to control agents’ characteristics. We rely on Vernon Smith’s 29 induced-value<sup>w</sup> <sup>x</sup> theory that identifies sufficient conditions for experimental control. The key idea is that proper use of a reward mechanism allows an experimenter to induce pre-specified characteristics in experimental subjects. Proper use is further defined to comprise of a monotonic non-satiable utility for the reward and that the incremental reward a person receives depends on her actions and those of other agents as defined by theŽ . institutional rules that she understands. The use of real currency is known to satisfy these important conditions. Jamal and Sunder 16 find that use of<sup>w</sup> <sup>x</sup> above described salient rewards tend to increase the reliability of results. Smith and Walker 30 provide<sup>w</sup> <sup>x</sup> a summary of evidence that further supports the use of real monetary rewards in experimental economics.

Based on the above theory we designed our experiment to consist of agents student buyers whoŽ . participate in online auctions of consumer goods like computer hardware and receive a real monetary reward that is a direct function of their performance. While drawing parallels between behavior exhibited by naıve students and experienced auction partici-¨ pants may be a far stretch for traditional auctions dealing with high value goods, the case of online auctions points to the contrary. In fact, uniÕersity students represent a significant portion of all Internet users, which gives credence to the inductive value of our proposed exercise.

The final compensation scheme, detailed in the next sub-section, ensures that the expected payoff for the students was US\$7 for 45 min of their time, which is 50% above the comparable hourly wage of US\$6. The idea being that participating in the auction is worth their while. Freidman and Sunder 11 <sup>w</sup> <sup>x</sup> state that most economists believe this to be the appropriate reward level to generate interest among participants.

## 3.2. The enÕironmental Õariables

We constructed an experimental design that ensures a sufficient sample size, and reliable data. The auction item was a set of five floppy diskettes. Students require these for a variety of tasks in the School of Business Administration, for example, to submit assignments, projects and taking computer lab work from the school to their residences. The number of batches for sale lot size was fixed at fiveŽ . per auction. The desired number of participants for each auction was 10. In all, we had four treatment levels, namely, the two types of auction mechanisms and two levels of the bid increment. However, since the bid increment is only applicable to the MIPEA we were able to economize our design by exploiting this commonality to have three distinct treatment levels. Thus, the total number of distinct student subjects required was around 300.

By utilizing distinct subjects from the same pool of undergraduate students, we ensured that the treatment comparison is made within a homogenous pool of subjects and at the same time there are no learning effects from earlier treatments. This could have occurred if we had chosen a pure crossover design and not restricted subjects from repeating experiments.

The subjects were recruited from the 350 students enrolled in the junior level courses at the School of Business Administration. To account for no-shows, we actually allowed up to 12 students to sign up for any give auction. Eventually, the number of participants for each experiment ranged from 8 to 12 with an average value of 9.2.

Each subject was promised an up-front sum of US\$5 for participation. Freidman and Sunder 11<sup>w</sup> <sup>x</sup> recommend this practice for three reasons: a toŽ . reduce tardiness, b to establish ex ante credibilityŽ . with the subjects that the rewards being promised to them will be paid to them promptly, and c to Ž . provide an initial cushion of wealth they can afford to lose in the actual experiment without dipping into their own wallets.

To create uncertainty regarding the exact price Ž . value of diskettes, in each experiment, we randomly drew the value of a set of five diskettes from a uniform distribution, with intervals ranging from US\$3 to US\$7, after the winners of a particular auction were determined. The final payoff of a winner was calculated based on the price they paid and the randomly drawn value. For example, suppose Ž . the randomly drawn value is US\$5 and a participant bids US\$6 and wins the auction, then he<sup>r</sup>she will get the diskettes<sup>q</sup>US\$4 US\$5 Ž <sup>y</sup>1 for overbidding and loss of surplus . If he. <sup>r</sup>she bids US\$3 and wins, then they get diskettes<sup>q</sup>US\$7 US\$5 Ž <sup>q</sup>2 gain of surplus . Example 1 illustrates this process in detail. for the MIPEA.

## 3.3. Example 1

Suppose there are 10 participants competing for five units of the commodity being auctioned. Let the randomly determined true market value be US\$4. Table 1 shows the bidders’ list after the close of the market and the corresponding payoffs. The bids are ordered by bid amount and by time within bid amount. Hence, the first five bids are the winning bids and the last five bids are the losing bids.

## 3.3.1. Case Jane Smith winner( )

Final bid<sup>s</sup>US\$6. Since the true market value was determined randomly to be US\$4, Jane inŽ .

Table 1  
Example list of final bids for the MIPEA

<table><tr><td>User-ID</td><td>Final winning bid (US$)</td><td>Net payoff (US$5 + true value – final winning bid)</td></tr><tr><td>AA</td><td>7.5</td><td>1.5 + Floppies</td></tr><tr><td>CC</td><td>6.5</td><td>2.5 + Floppies</td></tr><tr><td>Jane Smith</td><td>6</td><td>3 + Floppies</td></tr><tr><td>BB</td><td>4.5</td><td>4.5 + Floppies</td></tr><tr><td>Ram Singh</td><td>3.75</td><td>5.25 + Floppies</td></tr><tr><td>ZZ</td><td>3.5</td><td>5</td></tr><tr><td>FF</td><td>3.25</td><td>5</td></tr><tr><td>John Doe</td><td>3.0</td><td>5</td></tr><tr><td>RR</td><td>2.75</td><td>5</td></tr><tr><td>QQ</td><td>2</td><td>5</td></tr></table>

effect overbid by an amount equal to US\$6<sup>y</sup>4<sup>s</sup>2. Since Jane is among the top five bidders, she will receive the set of five floppy disks. However, the amount she overbid by, that is US\$2, will be subtracted from her participation money of US\$5. Hence, Jane Smith’s net payoff will be the Set of five floppy diskettes<sup>H</sup>[ ( ) US\$5 participation money <sup>H</sup>4 ( ) ( ) ]true market value <sup>I</sup>6 Jane’s bid <sup>s</sup>3 .

## 3.3.2. Case John Doe loser ( )

Final bid<sup>s</sup>US\$3. John is not among the top five bidders, hence he shall not receive the floppy diskettes. Hence, John Doe’s net payoff will be the US\$5 participation money( ).

## 3.3.3. Case Ram Singh winner( )

Final bid<sup>s</sup>US\$3.75. Since the true market value was determined randomly to be US\$4, Ram in Ž . effect under bid by an amount equal to US\$4<sup>y</sup>3.75 <sup>s</sup>0.25. Since Ram is among the top five bidders, he will receive the set of five floppy disks. Additionally, the amount he underbid by, that is US\$0.25, will be added to his participation money of US\$5. Hence, Ram Singh’s net payoff will be the Set of five floppy diskettes <sup>H</sup> [ ( US\$5 participation money) ( ) ( <sup>H</sup>4 true market value <sup>I</sup>3.75 Ram’s bid) ]<sup>s</sup>5.25 .

Because of the relative unfamiliarity of Vickreylike uniform-pricing auctions, the instructions for the MVA Appendix C contained some extra examples for the benefit of the subjects’ understanding. In particular, three examples were used to represent the cases when the overall bid values were a aroundŽ . the expected value of US\$5, b extremely low, andŽ . Ž .c extremely high, respectively. These three examples provided the subjects with a comprehensive overview of the range of expected revenue and incentive structures that could arise due to the MVA. Example 2 presents the first of the three examples utilized.

## 3.4. Example 2

Suppose there are 10 participants competing for five units of the commodity being auctioned. Let the randomly determined true market value be US\$3.25. The following table shows the bidders’ list after the close of the market and the corresponding payoffs. The bids are ordered by bid amount and by time within bid amount. Hence, the first five bids are the winning bids and the last five bids are the losing bids. Observe that ZZ the 6th highest bidder is( ) the marginal consumer at a level of US\$3.5. Hence, the auction price for all five winners will be equal to ZZ’s bid, that is US\$3.5.

## 3.4.1. Case Jane Smith winner( )

Final bid<sup>s</sup>US\$6. Since the true market value was determined randomly to be US\$3.25, and theŽ . auction price ZZ the marginal consumer’s bid isŽ . US\$3.5, Jane in effect over bid by an amount equal to US\$3.5<sup>y</sup>3.25<sup>s</sup>0.25. Since Jane is among the top five bidders, she will receive the set of five floppy disks. However, the amount she overbid by, that is US\$0.25, will be subtracted from her participation money of US\$5. Hence, Jane Smith’s net payoff will be the Set of five floppy diskettes<sup>H</sup> [ ( ) ( US\$5 participation money <sup>H</sup>3.25 true market value) ( ) ] <sup>I</sup>3.5 uniform auction price <sup>s</sup>4.75 .

## 3.4.2. Case John Doe loser( )

Final bid<sup>s</sup>US\$3. John is not among the top 5 bidders, hence he shall not receive the floppy diskettes. Hence, John Doe’s net payoff will be the US\$5 participation money ( ).

## 3.4.3. Case Ram Singh winner( )

Final bid<sup>s</sup>US\$3.75. Since this a uniform-pricing auction, the price for Ram will be the same as the

Table 2  
Example list of final bids for the MVA

<table><tr><td>User-ID</td><td>Final winning bid (US$)</td><td>Net payoff (US$5 + true value – marginal consumer&#x27;s bid)</td></tr><tr><td>AA</td><td>7.5</td><td>4.75 + Floppies</td></tr><tr><td>CC</td><td>6.5</td><td>4.75 + Floppies</td></tr><tr><td>Jane Smith</td><td>6</td><td>4.75 + Floppies</td></tr><tr><td>BB</td><td>4.5</td><td>4.75 + Floppies</td></tr><tr><td>Ram Singh</td><td>3.75</td><td>4.75 + Floppies</td></tr><tr><td>ZZ</td><td>3.5</td><td>5</td></tr><tr><td>FF</td><td>3.25</td><td>5</td></tr><tr><td>John Doe</td><td>3.0</td><td>5</td></tr><tr><td>RR</td><td>2.75</td><td>5</td></tr><tr><td>QQ</td><td>2</td><td>5</td></tr></table>

price for Jane Smith. Hence, Ram Singh’s net payoff will be the Set of five floppy diskettes <sup>H</sup> [ ( ) ( US\$5 participation money <sup>H</sup>3.25 true market value) ( ) ] <sup>I</sup>3.5 uniform auction price <sup>s</sup>4.75 ŽTable 2 ..

Each online auction was designed to last for about 45 min. It commenced with an instructional and familiarization session see Appendix B for MIPEAŽ and Appendix C for MVA that was supplemented . by using visual aids, which was followed by a trading session. The instructions of Appendices B or C were read out aloud to students and they were given the opportunity to clarify any doubts prior to the commencement of the trading. Just like in real online auctions, student subjects were asked to register by providing their name, social security number and a user-id that would protect their real identity during the course of the auction. Fig. 1 contains a snapshot of the login screen. Care was taken in designing the laboratory online auction interface, depicted below in Fig. 2 for MIPEA, so that it closely resembles its real world counterpart.

![](/api/attachments/AHAKJCEF/fulltext/images/f8ba00be8b4e5a9127d12b88c0a03d2093191e8fb9c0d667ea98c59fe7f8eca4.jpg)  
Fig. 1. Login screen for online auction experiment.

![](/api/attachments/AHAKJCEF/fulltext/images/2d044cc5a5ecbc9a5c8b74262ac726ce16ddff82fea5667cbcc6fa5f2fdb31a9.jpg)  
Fig. 2. Snapshot of MIPEA auctions conducted in the laboratory.

Additionally, an interactive console was designed as shown in Fig. 3. This console allowed the auctioneer to control the various parameters for each auction. Two pilot runs were carried out with the dual objectives of training the facilitator, and identifying and correcting any bugs in the online auction system. It should be noted that no special expertise or knowledge was required from the students in order to participate in the bidding process. Unlike other types of behavioral experiments, this was not a case where performance in the experiments was tied to previous expertise in the domain of the experiment.

## 4. Theoretical basis, test hypothesis and results

## 4.1. Auction mechanism as treatment Õariable, MI-PEA Õs. MVA

We first provide the theoretical basis for the development of our hypothesis of interest, which compares the revenues from the two auction mechanisms. Let V be the marginal consumer’s valuation, and be a segment of the bid increment k that measures the distance between the marginal consumer’s valuation V and the nearest lower feasible bid. Then the lower bound and the upper bound on the revenue of a seller selling multiple units under MIPEA are N VŽ . Ž . <sup>y</sup> and N V<sup>y q</sup>k , respectively, where N is the lot size and k is the bid increment 6 . Since the MVA is expected to be <sup>w</sup> <sup>x</sup> incentive compatible 32 , the total revenue for the <sup>w</sup> <sup>x</sup> seller selling N goods using MVA is NV, which leads us to the following hypothesis:

H1. There is no significant difference in the auctioneer’s revenues under MIPEA and under MVA.

For the MVA, the incentive mechanism and the objects being auctioned were kept the same as above.

![](/api/attachments/AHAKJCEF/fulltext/images/f1488ca2690753229d45fb1bda563041a4c6e4e3ee784526251e7e6d4773cf3f.jpg)  
Fig. 3. Interactive console for controlling online auctions in the laboratory.

The subjects were reminded that MVA was a sealed bid auction and that they got only one, irreversible chance at bidding. Fig. 4 below depicts the online screen that was designed for the MVA auction.

Table 3 below displays the results of the test H1. It is very clear that the MIPEA dominates MVA in our controlled laboratory setting, and the results are indeed statistically significant. This is in contrast to the implied empirical evidence of Bapna et al. 4<sup>w</sup> <sup>x</sup> where the MIPEA empirical data were used to infer MVA revenues. The results there indicted that there was little to choose between the two mechanisms revenues.

At the same time, it should be emphasized that the relatively high revenues obtained from MIPEA are neither unreasonable nor unexpected. In fact, given the a priori knowledge of the valuation of the object being auctioned a set of five floppy diskettesŽ . it is not surprising that the equilibrium points reached were towards the maximum expected revenue from such auctions as described by Bapna et al. 4 .<sup>w</sup> <sup>x</sup> Additionally, it should be borne in mind that no online auctioneer is actually conducting the MVA and thus the empirical estimate utilized in that study was the observable behavior of the marginal consumer under MIPEA that was adjusted for the MVA.

## 4.2. Bid increment as treatment Õariable

Given that all B2C online auctions set a discrete bid increment, we next examine the impact the choice of the bid increment has on the auctioneers’ revenue. It should be mentioned that there has been very little research done on the impact of discrete bid levels in auctions. In contrast, the standard auction theory assumption is to model the amount bid as a continuous variable. Yamey 33 and Rothkopf and Harstad<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 28 are the only researchers who have dealt with the

![](/api/attachments/AHAKJCEF/fulltext/images/40dd14ac8d6489ef58bcc25c958b233a09950090c728704b72baa06fdbf5aa57.jpg)  
Fig. 4. The screen for the MVA reminds subjects of its sealed-bid nature.

somewhat related issue of analyzing auctions from a more decision theoretic perspective rather than a game theoretic perspective. However, their analysis deals with single item auctions. Thus, based on the gap in the literature and our empirical evidence we chose the bid increment as a treatment variable, leading to our hypothesis of interest:

Table 3  
Results of MIPEA vs. MVA

<table><tr><td colspan="3">t-Test: two samples assuming unequal variances</td></tr><tr><td></td><td>MIPEA</td><td>MVA</td></tr><tr><td>Mean</td><td>24.485</td><td>19.95</td></tr><tr><td>Variance</td><td>13.76503</td><td>7.552778</td></tr><tr><td>Observations</td><td>20</td><td>10</td></tr><tr><td>Hypothesized mean difference</td><td>0</td><td></td></tr><tr><td>df</td><td>24</td><td></td></tr><tr><td>t Stat</td><td>3.774544</td><td></td></tr><tr><td> $P(T \leq t)$  one-tail</td><td>0.000465</td><td></td></tr><tr><td>t Critical one-tail</td><td>1.710882</td><td></td></tr><tr><td> $P(T \leq t)$  two-tail</td><td>0.00093</td><td></td></tr><tr><td>t Critical two-tail</td><td>2.063898</td><td></td></tr></table>

H2. There is no significant difference between the B2C online auction revenues with different values of the bid increment.

Keeping everything else constant we manipulated the bid increment k and observed the effect on the auctioneer’s revenue. Two levels of the treatment variables where chosen as k<sup>s</sup>US\$0.10 and k<sup>s</sup> US\$0.25 corresponding to a dime and a quarter, Ž respectively and 10 auctions were conducted at each. level. Table 4 below shows the results obtained from this experiment. As can be seen, both levels of the treatment variables yielded approximately the same average revenue and the large variance lead to the t-statistic having a low and insignificant value. In essence, the results show that the step size did not make a difference in MIPEA revenue. While this result might seem surprising, we believe that this result is influenced by relative closeness of absolute value of increments and students were not much affected by the range of bid increment when purchasing commodities that are relatively inexpensive.

Table 4  
Results with bid increment as the treatment variable

<table><tr><td colspan="3">t-Test: two samples assuming unequal variances</td></tr><tr><td></td><td>k = 10</td><td>k = 25</td></tr><tr><td>Mean</td><td>24.53</td><td>24.44</td></tr><tr><td>Variance</td><td>16.35789</td><td>12.69711</td></tr><tr><td>Observations</td><td>10</td><td>10</td></tr><tr><td>Hypothesized mean difference</td><td>0</td><td></td></tr><tr><td>df</td><td>18</td><td></td></tr><tr><td>t Stat</td><td>0.0528</td><td></td></tr><tr><td>P(T ≤ t) one-tail</td><td>0.479237</td><td></td></tr><tr><td>t Critical one-tail</td><td>1.734063</td><td></td></tr><tr><td>P(T ≤ t) two-tail</td><td>0.958473</td><td></td></tr><tr><td>t Critical two-tail</td><td>2.100924</td><td></td></tr></table>

## 4.3. Experimental Õalidity and robustness

In order to test the validity of our experimental design we examined our data to determine whether the incentive structure that was induced on the market did indeed control the subjects’ characteristics. Recall that the subjects were told that the true value of the objects being auctioned would be randomly drawn from a distribution US\$3, US\$7 . Interest- <sup>w</sup> <sup>x</sup> ingly, we found that the median value of all the bids that were placed in the 30 trials to be exactly US\$5, which coincides with the expected value of any symmetric distribution between the interval US\$3,<sup>w</sup> US\$7 .<sup>x</sup>

In addition, to examine the robustness of the design, we tested the three treatments for equality of variance. Table 5 displays the F-statistic for the pair-wise tests for equality of variance. The values clearly indicate that there is no significant difference in the variances between the treatments indicating that subjects behaved similarly over the course of the trials.

## 4.4. AllocatiÕe efficiency

The allocative efficiency measure used in this study to compare the allocations of our various treatments is the percentage of the maximum possible gains that are realized by the allocation process. Our metric for allocative efficiency is based on Becker’s 7 realization that basic features of an<sup>w</sup> <sup>x</sup> economic mechanism can be measured by market level consequences. It is difficult to control the market agents’ behavior exactly 12 ; however, the<sup>w</sup> <sup>x</sup> market level consequences remain more robust.

Let S be the consumer surplus for each bidder in the auctions. It is calculated as S<sup>s</sup>Žrandomly drawn value<sup>y</sup>actual bid.. Note that the quantity S can be either negative or positive. The overall allocative efficiency  for a given auction is computed as:

$$
\eta = \frac {\text {(Total auction revenue + Total consumer surplus)}}{\text {Benchmark revenue assuming full demand revelation}}\tag{1}
$$

The above metric provides the ratio of:

<sup>Ø</sup> The sum of the auctioneer’s revenue and the consumer surplus resulting from the allocation process, and

<sup>Ø</sup> The sum of the auctioneer’s revenue and the consumer surplus that would be realized if there were full demand revelation.

To compute this, we first need to estimate the benchmark revenue that would have accrued had there been full demand revelation. We utilize the experimental data obtained from the MVA sinceŽ it is incentive compatible for consumers to com-.

Table 5  
Pairwise F-test for equality of variance test

<table><tr><td>Treatment 1</td><td>Treatment 2</td><td>F-Statistic</td><td>p-Value</td></tr><tr><td>MVA</td><td>MIPEA(bid increment = US$0.10)</td><td>2.165</td><td>0.132</td></tr><tr><td>MVA</td><td>MIPEA(bid increment = US$0.25)</td><td>1.681</td><td>0.225</td></tr><tr><td>MIPEA(bid increment = US$0.10)</td><td>MIPEA(bid increment = US$0.25)</td><td>1.288</td><td>0.356</td></tr></table>

pute the median bids at each of the top 5 winning positions and take the sum of the medians, across auctions, to obtain our benchmark revenue de-Ž nominator . Note that the bids are consumers’ true. valuations and not the price they pay and thus include both the price they paid and the surplus they keep.

The allocative efficiency for the MVA turns out to be 96%, the efficiency of the MIPEA with bid increment of US\$0.10 is 84.8% and that with bid increment of US\$0.25 is 85.7%. Thus, we observe that while the MIPEA yields significantly higher revenue for the auctioneer, from a social welfare perspective it is dominated by the MVA since it has a high allocative efficiency of 96%. The result implies that the MVA should be the mechanism of choice in the design of auctions where social welfare maximization is the objective. This is the case of the auction of bandwidth for public data networks, which are considered public goods.

## 5. Directions for future research

At present the spirited and tenacious entrepreneurs of the networked economy are carrying out bold, but at times direction-less experimentation with regards to adopting new mercantile processes. There exists a unique opportunity for researchers who can anticipate these future trends and present a priori evidence for or against a given mechanism in a given domain. We demonstrated one such approach when we compared the revenue from the MVA with that of the MIPEA. Our research clearly suggests that the question regarding the choice of the optimal auction mechanism for multi-item B2C online auctions is still an unanswered one. Online auction laboratory environments such as ours can provide a low-risk high inductive value environment for testing the efficacy of alternative mechanisms before they are implemented in the real world.

An immediate question that needs to be answered deals with the comparison of the two mechanisms described above and the so-called ‘Dutch’ auction conducted by sites like Ebay and Amazon. From a theoretical perspective, the open uniform-pricing ‘Dutch’ auctions conducted by sites like Ebay and

Amazon do not offer the necessary incentives for consumers to reveal their true valuations. This leads us to hypothesize that their allocative efficiency will be dominated by both MIPEA and the MVA. Testing this hypothesis in an empirical setting would require auctions of the same items using the same lot size under the three different mechanisms, an event that is unlikely to happen. Instead, researchers can rely on a laboratory setting like ours and test this hypothesis under a controlled environment.

There is immense potential in the extension of this approach to other domains. In the domain of consumer-to-consumer online auction that primarily deals with collectibles, it would be interesting to see whether individuals’ valuations are correlated and whether a true descending Dutch auction can be utilized to yield higher revenues in the presence of risk-averse bidders. In the domain of business-tobusiness online auction, where sealed bids for contracts and procurement fulfillment are de rigueur, a stock market-like Walraisan bid-ask market mechanism can be designed that could increase the efficiency of the procurement process.

As the networked economy makes auction-based dynamic pricing increasingly prevalent and expands its reach to a wide variety of goods and services, the challenges to the academic community are many. No longer can these online mercantile processes be analyzed in a vacuum, out of context of the markets in which they take place. Another interesting area of research where the laboratory experiments will be valuable is in examining the complimentarities and interactions between the posted price-based electronic catalog method of selling on the web and the emerging auction-based dynamic pricing mechanism. The problem can be viewed from both the sellers’ and the buyers’ perspective. In what situations and under what criteria should sellers switch from one mechanism to the other. From the consumers’ point of view, the two models increase selection and coexist very nicely. Consumers do not wake up in the morning and say, AI want to buy something using the auction mechanism.B Presumably, they know what they are looking for and have to determine where they can find it. Whether they ultimately get it via a fixed price or auction mechanism will be a function of their variables of interest, which need to be further understood.

In the future we anticipate further enrichment of the portfolio of mercantile processes. There will be different horses for different courses and many different kinds of negotiating mechanisms will co-exist on the web. An interesting research question is determining the correct mapping between a given mechanism and a target domain in the online environment. For instance, can we establish that an MVA type uniform-pricing mechanism will always be preferable to an equivalent discriminatory mechanism in situations where the maximum valuations of the objects being auctioned are well known? This could apply to consumer electronics where the maximum valuation for any auction participant should not be greater than the lowest posted price which can Ž easily be determined using a shopping agent like www.shopper.com . On the other hand, if the do-. main is unique collectible items one could hypothesize that individuals’ valuations will be correlated to their counterparts’ valuations and hence a discriminatory auction would yield higher expected revenues.

Another candidate posted-price mechanism is the one utilized by companies like Egghead.com where goods are said to be priced ‘at cost’ plus a small premium that is revealed to the consumers. Egghead also has one of the premium B2C auction sites on the web. An interesting research question would be examining the rationale behind the consumers’ decision to adopt either of these mechanisms. This would provide insights into when and why consumers prefer the certainty of fixed prices to auctions.

Lastly, the reach of the controlled laboratory experimental setting can be extended to create pricing models currently lacking for real-time information goods, like event webcasts, that have to be delivered with a certain quality-of-service.

## Acknowledgements

This research is supported in part by Treibick Electronic Commerce Initiative, Department of OPIM, University of Connecticut.

The third author’s research was also supported in part by NSF Career grant number IIS-0092780 but does not necessarily reflect the views of NSF.

## Appendix A. Example of auction mechanisms with multi-item demand

We consider the case when consumers are allowed to bid for more than one-item in an m-item auction. Vickrey’s original definition of an incentive compatible mechanism where each bidder submitsŽ one bid, the top m bidders each win one good at a uniform price equal to the first bid rejected holds. only when individuals are allowed to bid for only one item.

Example 1: consider an auction of three goods and let there be seven bidders with the following final bids each for one quantity.

<table><tr><td>Consumer</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E(marginalconsumer)</td><td>F</td><td>G</td></tr><tr><td>Final bid</td><td>10</td><td>20</td><td>15</td><td>10</td><td>15</td><td>30</td><td>30</td></tr></table>

F, G, and B will be declared winners and they will all pay US\$15 E’s bid assuming that ties are Ž . broken randomly. All bidders have it in their interest to bid their true valuations. The auctioneer’s revenue is US\$45.

If, however, the bidders were allowed to bid for more than one item and that these bids could be of different values then incentive compatibility does not hold.

Example 2: consider an auction of three goods where bidders can submit as many individual bids that they like. Let there be seven bidders and assume that each individual places bids for two items.

<table><tr><td>Consumer</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E(marginalconsumer)</td><td>F</td><td>G</td></tr><tr><td> $Bid^1$ </td><td>10</td><td>20</td><td>15</td><td>10</td><td>15</td><td>30</td><td>30</td></tr><tr><td> $Bid^2$ </td><td>10</td><td>5</td><td>5</td><td>10</td><td>15</td><td>10</td><td>20</td></tr></table>

For this mechanism to be incentive compatible that the top three bids $\{ \boldsymbol { \mathrm { F } } ^ { 1 } , \boldsymbol { \mathrm { G } } ^ { 1 } , \boldsymbol { \mathrm { B } } ^ { 1 } \}$ are declared winners, and that for the jth unit won by a bidder, she must pay an amount equal to the jth highest of the rejected bids submitted by others. Thus, F, G and B are charged US\$20, US\$15, and US\$15, respectively. This results in the auctioneer’s revenue being US\$50.

Appendix B. Instructions for Multiple Item Progressive Electronic Auctions MIPEA( )

## B.1. General

This is an experiment in the economics of electronic markets. Various research grants have provided funds for this research. The instructions are simple and if you follow them carefully and make good decisions, you might derive a considerable amount of benefit, some of which will be in the form of cash given to you at the end of the experiment.

In this experiment we are going to simulate a market that closely resembles many of the current auctions conducted on the Internet. You and your fellow participants in the experiment will be competing to buy a single unit of a homogenous product when multiple units are being sold in a given trading period. By homogenous product, we mean that there is no difference of any kind between any two units. A single unit of the product in this experiment is a set of five Maxell High Density floppy diskettes. Each auction will attempt to sell five such units. The duration of the trading period will be announced beforehand. All participants have been provided the same information regarding the experiment.

All participants will be given a sum of US\$5 for participating in the experiment. This amount will be disbursed after the market clears at the end of the experiment. In addition, at the end of the experiment we will determine the true market value of a single unit of the product by randomly choosing a value ranging from US\$3 to US\$7. This range of true value accounts for the variation in the market conditions such as price fluctuations that arise from changes in demand and supply. Once the market value is determined and if you are among the auction winners, then you may receive an additional amount equal to the difference between the market value and your winning bid. If your bid is higher than the market value, then the difference will be deducted from your participation payoff. In case the difference is such that your net participation payoff is less than zero, then your payoff will be set to US\$0. Later, we will discuss examples that will further clarify the total payoff for both winners as well as losers.

## B.2. Registration

To participate in this experiment you have to register by providing your name and social security number. Additionally, to protect your identity during the course of the experiment you will be asked to select a ‘user id <sub>–</sub> ’ that will serve as your anonymous nametag. Please choose an id that does not reveal your true identity.

## B.3. Market organization

The market for this commodity is organized as follows: we open the market for each trading period that lasts approximately 15 min. The number of units of the commodity being auctioned, the bid increment, the current minimum required bid, the current list of winning bids and the auction closing time will be displayed on your web browser. If you have successfully registered and if the market is open, you can place a bid for a single unit of the commodity being auctioned. Bids are placed by entering a bid amount and by pressing the submit button on your web browser. The bid has to be at least as high as the current minimum bid. It can be higher than the current minimum bid.

By placing a bid you express a desire to obtain a set of five floppies at your given bid level and you understand that your net payoff will be affected by your bid amount. After the auction closes the list of winners, that is the five highest bidders will be announced and the market will clear. The bids are ranked by bid amount and by time within bid amount. This implies that if person A bids US\$ x before person B bids US\$ x than A will be higher on the winners’ list.

## Appendix C. Instructions for Multiple Vickrey Auctions MVA( )

## C.1. General

This is an experiment in the economics of electronic markets. Various research foundations have provided funds for this research. The instructions are simple and if you follow them carefully and make good decisions you might derive a considerable amount of benefit, some of which will be in the form of cash given to you at the end of the experiment. In this experiment we are going to simulate a market that closely resembles many of the current auctions conducted on the Internet. You and your fellow participants in the experiment will be competing to buy a single unit of a homogenous product when multiple such units are being sold in a given trading period. By homogenous product, we mean that there is no difference of any kind between any two products. A single unit of the product in this experiment is a set of five Maxell High Density floppy diskettes. Each auction will attempt to sell five such units. The duration of the trading period will be announced before hand. All participants have been provided the same information regarding the experiment.

All participants will be given a sum of US\$5 for participating in the experiment. This amount will be disbursed after the market clears at the end of the experiment. In addition, at the end of the experiment we will determine the true market value of a single unit of the product by randomly choosing a value ranging from US\$3 to US\$7. This range of true value accounts for the variation in the market conditions such as price fluctuations that arise from changes in demand and supply. Once the market value is determined and if you are among the auction winners, then you may receive an additional amount equal to the difference between the market value and the price of the product determined by the auction. The auction price of the product will be uniformly set to the 6th highest bid. Thus, all the five winners, that is the five highest bidders, will receive the product at a price equal to the bid made by the 6th highest bidder. If the auction price is higher than the market value, then the difference will be deducted from your participation payoff. In case the difference is such that your net participation payoff is less than zero, then your payoff will be set to US\$0. Later, we will discuss examples that will further clarify the total payoff for both winners as well as losers.

## C.2. Registration

To participate in this expermient you have to register by providing your name and social security number. Additionally, to protect your identity during the course of the experiment you will be asked to select a ‘user id <sub>–</sub> ’ that will serve as your anonymous nametag. Please choose an id that does not reveal your true identity.

## C.3. Market organization

The market for this commodity is organized as follows: we open the market for each trading period that lasts not greater than 10 min. The auction will automatically close after bids from all 10 participants are received. The number of units of the commodity being auctioned will be displayed on your web browser. If you have successfully registered and if the market is open, you can place a bid for a single unit of the commodity being auctioned. Bids are placed by entering a bid amount and by pressing the submit button on your web browser. Since this is a sealed-bid auction, no information regarding the bids will be displayed during the course of the auction. Also, you can place only one bid for the commodity and this bid cannot be revised.

By placing a bid, you express a desire to obtain a set of five floppies at your given bid level and you understand that your net payoff will be affected by your bid amount. After the auction closes, the list of winners, that is, the five highest bidders will be announced and the market will clear. The price charged to each of the five winners will be equal to bid of the 6th highest bidder, that is, the first losing bidder. The bids are ranked by bid amount and by time within bid amount. This implies that if person A bids US\$ x before person B bids US\$ x, then A will be higher on the winners list.

## C.4. Example 2

Let the randomly determined true market value be US\$5.00. Table C1 below shows the bidders’ list after the close of the market and the corresponding payoffs. The bids are ordered by bid amount and by time within bid amount. Hence, the first five bids are the winning bids and the last five bids are the losing bids. Observe that ZZ the 6th highest bidder is( )

Table C1  
Example list of bids for the MVA

<table><tr><td>User-ID</td><td>Final winning bid (US$)</td><td>Net payoff (US$5 + true value – marginal consumer&#x27;s bid)</td></tr><tr><td>AA</td><td>10</td><td>0 + Floppies</td></tr><tr><td>CC</td><td>10</td><td>0 + Floppies</td></tr><tr><td>Jane Smith</td><td>10</td><td>0 + Floppies</td></tr><tr><td>BB</td><td>10</td><td>0 + Floppies</td></tr><tr><td>Ram Singh</td><td>10</td><td>0 + Floppies</td></tr><tr><td>ZZ</td><td>10</td><td>5</td></tr><tr><td>FF</td><td>5</td><td>5</td></tr><tr><td>John Doe</td><td>5</td><td>5</td></tr><tr><td>RR</td><td>5</td><td>5</td></tr><tr><td>QQ</td><td>5</td><td>5</td></tr></table>

the marginal consumer at a level of US\$10. Hence, the auction price for all five winners will be equal to ZZ’s bid, that is, US\$10.

## C.4.1. Case Jane Smith winner( )

Final bid<sup>s</sup>US\$10. Since the true market value was determined randomly to be US\$5, and the Ž . auction price ZZ the marginal consumer’s bid isŽ . US\$10, Jane in effect overbid by an amount equal to US\$10<sup>y</sup>5<sup>s</sup>5. Since Jane is among the top 5 bidders, she will receive the set of five floppy disks. However, the amount she overbid by, that is US\$5, will be subtracted to her participation money of US\$5. Hence, Jane Smith’s net payoff will be the Set of five floppy diskettes<sup>H</sup>[ ( US\$5 participation money) ( ) ( <sup>H</sup>5 true market value <sup>I</sup>10 uniform auction price) ] <sup>s</sup>0 .

## C.4.2. Case John Doe loser( )

Final bid<sup>s</sup>US\$5. John is not among the top 5 bidders, hence he shall not receive the floppy diskettes. Hence, John Doe’s net payoff will be the US\$5 participation money( ).

## C.4.3. Case Ram Singh winner ( )

Final bid<sup>s</sup>US\$10. Since this a uniform-pricing auction, the price for Ram will be the same as the price for Jane Smith. Hence, Ram Singh’s net payoff will be the Set of five floppy diskettes <sup>H</sup> [ ( ) ( US\$5 participation money <sup>H</sup> 5 true market value) ( ) ] <sup>I</sup>10 uniform auction price <sup>s</sup>US\$0 ŽTable C1 ..

## C.5. Example 3

Let the randomly determined true market value be US\$5.00 once again. Table C2 below shows the bidders’ list after the close of the market and the corresponding payoffs. The bids are ordered by bid amount and by time within bid amount. Hence, the first five bids are the winning bids and the last five bids are the losing bids. Observe that ZZ the 6th( highest bidder is the marginal consumer at a) level of US\$3.25. Hence, the auction price for all five winners will be equal to ZZ’s bid, that is US\$3.25.

## C.5.1. Case Jane Smith winner( )

Final bid<sup>s</sup>US\$3.50. Since the true market value was determined randomly to be US\$5, and theŽ . auction price ZZ the marginal consumer’s bid isŽ . US\$3.25, Jane in effect underbid by an amount equal to US\$5<sup>y</sup>3.25<sup>s</sup>1.75. Since Jane is among the top five bidders she will receive the set of five floppy disks. However, the amount she underbid by, that is US\$1.75, will be added to her participation money of US\$5. Hence, Jane Smith’s net payoff will be the Set of five floppy diskettes<sup>H</sup>[ ( US\$5 participation money) ( ) ( <sup>H</sup>5 true market value <sup>I</sup>3.25 uniform auction price) ] <sup>s</sup>6.75 .

Table C2  
Example list of bids for the MVA

<table><tr><td>User-ID</td><td>Final winning bid (US$)</td><td>Net payoff (US$5 + true value – marginal consumer&#x27;s bid)</td></tr><tr><td>AA</td><td>4</td><td>6.75 + Floppies</td></tr><tr><td>CC</td><td>3.75</td><td>6.75 + Floppies</td></tr><tr><td>Jane Smith</td><td>3.5</td><td>6.75 + Floppies</td></tr><tr><td>BB</td><td>3.5</td><td>6.75 + Floppies</td></tr><tr><td>Ram Singh</td><td>3.5</td><td>6.75 + Floppies</td></tr><tr><td>ZZ</td><td>3.25</td><td>5</td></tr><tr><td>FF</td><td>3</td><td>5</td></tr><tr><td>John Doe</td><td>3</td><td>5</td></tr><tr><td>RR</td><td>3</td><td>5</td></tr><tr><td>QQ</td><td>3</td><td>5</td></tr></table>

## C.5.2. Case John Doe loser( )

Final bid<sup>s</sup>US\$3.25. John is not among the top five bidders, hence he shall not receive the floppy diskettes. Hence, John Doe’s net payoff will be the US\$5 participation money( ).

## C.5.3. Case Ram Singh winner ( )

Final bid<sup>s</sup>US\$3.5. Since this is a uniform-pricing auction, the price for Ram will be the same as the price for Jane Smith. Hence, Ram Singh’s net payoff will be the Set of five floppy diskettes<sup>H</sup> [ ( ) ( US\$5 participation money <sup>H</sup> 5 true market value) ( ) ] <sup>I</sup>3.25 uniform auction price <sup>s</sup>6.75 ŽTable C2 ..

## References

<sup>w</sup> <sup>x</sup> 1 P. Alsemgeest, C. Noussair, M. Olson, Experimental comparisons of auctions under single and multi-unit demand, Economic Inquiry 36 1998 87–98, Jan.Ž .

<sup>w</sup> <sup>x</sup> 2 L.M. Ausubel, P.C. Cramton, Demand reduction and inefficiency in multi-unit auctions, Working paper, University of Maryland 1999 .Ž .

<sup>w</sup> <sup>x</sup> 3 C. Baker, Auctioning coupon-bearing securities: a review of treasury experience, in: Y. Amihud Ed. , Bidding and Auc-Ž . tioning for Procurement and Allocation, NYU Press, New York, 1976, pp. 146–154.

<sup>w</sup> <sup>x</sup> 4 R. Bapna, P. Goes, A. Gupta, A theoretical and empirical investigation of multi-item online auctions, Information Technology and Management 1 1 2000 1–23. Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 R. Bapna, P. Goes, A. Gupta, Online auctions: insights and analysis, Communications of the ACM 2001 forthcoming. Ž .

<sup>w</sup> <sup>x</sup> 6 R. Bapna, P. Goes, A. Gupta, Analysis and Design of Business-to-Consumer Online Auctions, Working Paper Treibick Electronic Commerce Initiative Series, University of Connecticut Jan. 2000 .Ž .

<sup>w</sup> <sup>x</sup> 7 G. Becker, Irrational behavior and economic theory, Journal of Political Economy 70 1962 1–13, Feb. Ž .

<sup>w</sup> <sup>x</sup> 8 J. Bulow, J. Roberts, The simple economics of optimal auctions, Journal of Political Economy 7 5 1989 1060– Ž . Ž . 1090.

<sup>w</sup> <sup>x</sup> 9 E.H. Clarke, Multipart pricing of public goods, Public Choice 11 1971 19–33, Fall.Ž .

<sup>w</sup> <sup>x</sup> 10 J.C. Cox, V.L. Smith, J.M. Walker, Expected revenue in discriminative and uniform price sealed-bid auctions, Research in Experimental Economics 3 1985 183–232.Ž .

<sup>w</sup> <sup>x</sup> 11 D. Freidman, S. Sunder, experimental Methods: a primer for economists Cambridge Univ. Press .Ž .

<sup>w</sup> <sup>x</sup> 12 D.K. Gode, S. Sunder, Allocative efficiency of markets with zero-intelligence traders: markets as a partial substitute for individual rationality, Journal of Political Economy 10 1Ž . Ž .1993 119–137.

<sup>w</sup> <sup>x</sup> 13 T. Groves, Incentives in teams, Econometrica 41 4 1973Ž . Ž . 617–631, July.

<sup>w</sup> <sup>x</sup> 14 R.G. Hansen, Empirical testing of auction theory, American Economic Review 75 2 1985 156–159, May. Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 M. Harris, A. Raviv, Allocation mechanism and the design of auctions, Econometrica 49 6 1981 1477–1499, Nov.Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 K. Jamal, S. Sunder, Money vs. gaming: the effects of salient monetary payments in double oral auctions, Organizational Behavior and Human Decision Processes 49 1991 161–166.Ž .

<sup>w</sup> <sup>x</sup> 17 B.A. Johnson, Fault Lines in CRM: New E-Commerce Business Models and Channel Integration Challenges, http:<sup>rr</sup> www.johnson.CRMproject.com<sup>r</sup> Ž . 2000 .

<sup>w</sup> <sup>x</sup> 18 S. Klein, R.M. O’Keefe, The impact of the web on auctions: some empirical evidence and theoretical considerations, International Journal of Electronic Commerce 3 3 1999Ž . Ž . Spring.

<sup>w</sup> <sup>x</sup> 19 A. List, D. Lucking-Reiley, Demand reduction in mutli-unit auctions: evidence from a sporstscard field experiments, American Economic Review 2000 forthcoming.Ž .

<sup>w</sup> <sup>x</sup> 20 D. Lucking-Reiley, Using field experiments to test equivalence between auction formats: magic on the internet, American Economic Review 2000 forthcoming.Ž .

<sup>w</sup> <sup>x</sup> 21 P.R. McAfee, J. McMillan, Auctions and bidding, Journal of Economic Literature 25 1987 699–738.Ž .

<sup>w</sup> <sup>x</sup> 22 W.J. Mead, M. Schniepp, R.B. Watson, The Effectiveness of Competition and Appraisals in the Auction Markets for National Forest Timber in the Pacific Northwest, US Forest Service Contract No. 53-3187-1-43 1981 .Ž .

<sup>w</sup> <sup>x</sup> 23 K. Mehta, B. Lee, Efficiency comparison in electronic market mechanisms: posted price versus auction market, Proceedings of WISE 1999 Charlotte, NC . Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 M. Menconi, CRM 101—Building a Great Customer Relationship Management Strategy, http:<sup>rr</sup>www.menconi. crmproject.com<sup>r</sup> Ž . 2000 .

<sup>w</sup> <sup>x</sup> 25 P. Milgrom, Auctions and bidding: a primer, Journal of Economic Perspectives 3 1989 3–22.Ž .

<sup>w</sup> <sup>x</sup> 26 C.R. Plot, V.L. Smith, An experimental examination of two exchange institutions, Review of Economic Studies 45 1Ž . Ž . 1978 133–153.

<sup>w</sup> <sup>x</sup> 27 R. Robinson, Customer relationship management, Computerworld 34 9 2000 67, Feb. 28.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 M.H. Rothkopf, R.M. Harstad, On the role of discrete bid levels in oral auctions, European Journal of Operations Research 74 1994 572–581.Ž .

<sup>w</sup> <sup>x</sup> 29 V. Smith, Experimental economics: induced value theory, American Economic Review 66 2 1976 274–279, May.Ž . Ž .

<sup>w</sup> <sup>x</sup> 30 V. Smith, J.M. Walker, Rewards, experience and decision costs in first price auctions, Economic Inquiry 1992 .Ž .

<sup>w</sup> <sup>x</sup> 31 E. Van Heck, P. Vervest, How should CIO’s deal with web-based auctions? Communications of the ACM 41 7Ž . Ž . 1998 99–100, July.

<sup>w</sup> <sup>x</sup> 32 W. Vickrey, Counter-speculation, auctions, and competitive sealed tenders, Journal of Finance 41 1961 8–37.Ž .

<sup>w</sup> <sup>x</sup> 33 B.S. Yamey, Why US\$2 310 000 for a Velazquez? An auction bidding rule, Journal of Political Economy 80 1972 Ž . 1323–1327.

![](/api/attachments/AHAKJCEF/fulltext/images/ceae9a2d98665957980d55360f2bddcc4188d9eb14ab9a758e576c500fbbb25e.jpg)

Alok Gupta, Assistant Professor and Co-Director Treibick Electronic Commerce Initiative, Department of OPIM, University of Connecticut.

Alok Gupta received his PhD in Management Science and Information Systems from The University of Texas at Austin in 1996. His areas of specialization include data communication, electronic commerce, design and evaluation of economic mechanisms, mathematica modeling of information systems,

large-scale systems simulation, and economics of information systems. His research has been published in various information systems, economics, and computer science journals such as ISR, CACM, JMIS, Journal of Economic Dynamics and Control, Computational Economics, Decision Support Systems IEEE Internet Computing, International Journal of Flexible Manufacturing Systems, Information Technology Management, and Journal of Organizational Computing and Electronic Commerce. In addition, his articles have been published in several leading books in the area of economics of electronic commerce. His current research and teaching interest is in the area of economic modeling and analysis of electronic commerce. He is co-director of Treibick Electronic Commerce Initiative, an endowed research initiative at Dept. of OPIM, University of Connecticut. He serves on the editorial boards of DSS and Brazilian Electronic Journal of Economics.

Paulo B. Goes, Associate Professor and Gladstein Professor of Information Technology and Innovation, Co-Director of the Treibick Electronic Commerce Initiative TECI and Associate DirectorŽ . of CITI— Connecticut Information Technology Institute, Department of Operations and Information Management, University of Connecticut. Dr. Goes received his M.S. and Ph.D. degrees in Computers and information Systems from the University of

![](/api/attachments/AHAKJCEF/fulltext/images/1f0ae54dc9788fdd9d8cb1a4a34595429613b8aad0fce073d1ac63cf64dbc89b.jpg)

Rochester. He also has a M.S. degree in production Engineering from the Federal University of Rio de Janeiro, Brazil. His research interests are in the areas of Internet technologies and electronic commerce, design and evaluation of models for e-business, online auctions, database recovery and security, computer networking and technology. Dr. Goes joined the University of Connecticut in 1990. His publications have appeared in several leading journals including Operations Research, Communications of the ACM, IEEE Transactions on Communications, IEEE Transactions on Computers, INFORMS Journal on Computing, and Decision Support Systems. He is a member of ACM and INFORMS.

![](/api/attachments/AHAKJCEF/fulltext/images/2f65879cbafa3673c367ad36d6de3be5c9e38a5e2c0a2cbac0c17a5e00f836c0.jpg)

Ravi Bapna received his PhD in Operations and Information Management from the University of Connecticut in 1999. Before joining Northeastern University in Fall 2000, Dr. Bapna was an Assistant Professor at School of Management at University of Texas at Dallas during 1999–2000 academic year. Dr. Bapna’s research interests are in the area of electronic commerce, e-mercantile process

Ravi Bapna, Assistant Professor, Northeastern University.

design and evaluation, Internet auctions, and economics of information system. His research has been published in a wide array of journals such as CACM, Naval Research Logistics, DSS, and Information Technology and Management.
