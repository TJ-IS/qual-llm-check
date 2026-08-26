---
otero_id: 4930
otero_key: "2TAYMFHP"
title: "Internet Exchanges for Used Books: An Empirical Analysis of Product Cannibalization and Welfare Impact"
authors: "Anindya Ghose; Michael D. Smith; Rahul Telang"
year: "2006"
journal: "Information Systems Research"
doi: "10.1287/isre.1050.0072"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Internet Exchanges for Used Books: An Empirical Analysis of Product Cannibalization and Welfare Impact

Anindya Ghose

Information Systems, Leonard Stern School of Business, New York University, KMC 8-94, 44 West 4th Street, New York, New York 10012, aghose@stern.nyu.edu

Michael D. Smith, Rahul Telang

H. John Heinz III School of Public Policy and Management, Carnegie Mellon University, 4800 Forbes Avenue, Hamburg Hall, Pittsburgh, Pennsylvania 15213 {mds@andrew.cmu.edu, rtelang@andrew.cmu.edu}

nformation systems and the Internet have facilitated the creation of used-product markets that feature a Idramatically wider selection, lower search costs, and lower prices than their brick-and-mortar counterparts do. The increased viability of these used-product markets has caused concern among content creators and distributors, notably the Association of American Publishers and Author’s Guild, who believe that used-produc markets will significantly cannibalize new product sales.

This proposition, while theoretically possible, is based on speculation as opposed to empirical evidence. In this paper, we empirically analyze the degree to which used products cannibalize new-product sales for books—one of the most prominent used-product categories sold online. To do this, we use a unique data set collected from Amazon.com’s new and used book marketplaces to measure the degree to which used products cannibalize new-product sales. We then use these estimates to measure the resulting first-order changes in publisher welfare and consumer surplus.

Our analysis suggests that used books are poor substitutes for new books for most of Amazon’s customers. The cross-price elasticity of new-book demand with respect to used-book prices is only 0.088. As a result, only 16% of used-book sales at Amazon cannibalize new-book purchases. The remaining 84% of used-book sales apparently would not have occurred at Amazon’s new-book prices. Further, our estimates suggest that this increase in book readership from Amazon’s used-book marketplace increases consumer surplus by approxi mately \$67.21 million annually. This increase in consumer surplus, together with an estimated \$45.05 million loss in publisher welfare and a \$65.76 million increase in Amazon’s profits, leads to an increase in total welfare to society of approximately \$87.92 million annually from the introduction of used-book markets at Amazon.com.

Key words: publisher welfare; retailer welfare; consumer surplus; price competition; used-books sales; electronic markets

History: Sanjeev Dewan, Senior Editor; Alok Gupta, Associate Editor. This paper was received on September 7, 2004, and was with the authors 3 <sup>1</sup> months for 2 revisions.

## 1. Introduction

   as a leader in the bookselling industry, Amazon’s [used book] sales practices can have a significantly deleterious effect on new book sales. If your aggressive promotion of used book sales becomes popular among Amazon’s customers, this service will cut significantly into sales of new titles, directly harming authors and publishers.

—Author’s Guild and Association of American Publishers, open letter to Jeff Bezos (CEO Amazon.com), dated April 9, 2002

We’ve found that our used books business does not take business away from the sale of new books. In fact, the opposite has happened. Offering customers a lower-priced option causes them to visit our site more frequently, which in turn leads to higher sales of new books while encouraging customers to try authors and genres they may not have otherwise tried. In addition, when a customer sells used books, it gives them a budget to buy more new books.

—Jeff Bezos, open letter to Amazon.com’s used booksellers, dated April 14, 2002

Globally networked information systems can reduce the search and transaction costs for buyers and sellers to locate and trade products (Bakos 1997), and can thereby facilitate the creation of technologymediated electronic exchanges (Malone et al. 1987). These exchanges allow sellers to easily reach a worldwide market, and allow buyers to easily locate items that frequently would be unavailable in traditional physical stores.

Several papers in the literature have empirically analyzed the impact of lower search costs on retailerlevel competition (e.g., Brynjolfsson and Smith 2000, Smith and Brynjolfsson 2001, Chevalier and Goolsbee 2003). In this paper, we empirically analyze the impact of lower consumer search costs on product-level competition—specifically, competition between new and used books. The Internet facilitates the creation of side-by-side new- and used-product markets, allowing consumers shopping for new products to easily locate competing used-product offers.

There is, of course, nothing new about the sale of used products. In the United States, the First Sale Doctrine (17 U.S.C. §109) allows for the resale of copyrighted works such as books, and used bookstores are common in physical settings. Rather, electronic exchanges alter the scale, scope, and efficiency of what is possible with regard to the sale of used products. Thus, while brick-and-mortar bookstores have high search costs, limited inventory capacity, limited geographical coverage, and relatively high prices, IT-enabled markets for used books offer low search costs, nearly unlimited (virtual) inventory capacity, global coverage, and—through competition among sellers—relatively low prices. These market characteristics are clearly attractive for consumers. Internet sales of used books made up an estimated 67% of all used-book sales in 2004 (Wyatt 2005). This represents the highest Internet penetration for any physical product category that we are aware of, and compares to a penetration of only 12.7% for Internet sales of new books.

These changes in used-book sales have also raised concerns among publishers and authors. Groups such as the Author’s Guild and the Association of American Publishers reason that because authors and publishers are only paid for the initial sale of a product, the lower search costs, increased selection, and lower prices of online used-book markets will cannibalize new-book sales and cut significantly into both publisher revenues and author royalty payments.

However, to date, the publishing industry has been unable to precisely measure the degree to which used books cannibalize new-book sales because key sales data have been unobservable in online markets. For example, Tedeschi (2004) quotes Paul Aiken, the Executive Director of the Author’s Guild, as saying “[t]here has always been used-book sales, but it’s always been a background noise sort of thing. Now it’s right there next to the new book on Amazon    We think it’s not good for the industry and it has an effect, but we can’t measure it” (emphasis ours). Likewise, Kelly Gallagher, chairperson of the Book Industry Study Group’s Research Committee, observes “everybody has anecdotal evidence to show used books’ cannibalization of new books, but we don’t have any accurate numbers” (emphasis ours, Publishing Trends 2004).

Therefore, the motivation of this study is to provide direct empirical estimates of the degree to which used books cannibalize new-book sales, and analysis of the resulting impact on publisher welfare, consumer surplus, and social welfare. Our paper contributes to the literature in that, while a variety of analytic models have analyzed competition to new-product sales from used-product markets, ours is the only paper we are aware of to empirically analyze the elasticity of new-product demand with respect to used-product prices, and the resulting changes in new and usedproduct sales and overall surplus. This analysis also contributes to the literature by providing publishers and industry analysts with a methodology to conduct similar analyses based on data that can be readily collected from Internet markets, which as noted above is a capability publishers and content creators have been lacking.

We use Amazon.com’s used-book market as our setting to answer this question because it is one of the most prominent used- and new-book marketplaces online (Brynjolfsson et al. 2003, Brynjolfsson and Smith 2000), and it lists new and used products side by side on product pages. This creates a setting where cannibalization is most likely to occur as newbook purchasers can easily become aware of competing used-product offers. We use this market to collect a unique data set from Amazon.com’s new and used marketplaces documenting prices and quantities sold for new and used books. Our data cover two samples: one collected from September 2002 to March 2003, and one collected from April to July 2004. Together these samples include 41,994 observations for 393 individual book titles.

Our data suggest that used books are not a strong substitute for new books for most of Amazon’s customers. The cross-price elasticity of demand for new books with respect to used-book prices is only 0.088. As a result, only 16% of used-book sales at Amazon cannibalize new-book purchases. The remaining 84% of used-book sales apparently would not have occurred at Amazon’s new-book prices.

This increased access to low-priced (used) book titles increases consumer surplus by \$67.21 million annually. While much of the discussion of the value of the Internet to consumers has revolved around lower prices, consumers’ benefit from access to used-book markets is nearly as large as consumers’ benefit from access to lower prices on new books (Brynjolfsson et al. 2003).<sup>1</sup>

With respect to retailer losses, our results show that without raising prices, book publishers lose approximately \$45.05 million annually in gross profit from the presence of Amazon’s used-book markets. This represents approximately 0.3% of total publisher gross profits in 2003.<sup>2</sup> It is also important to note that this figure does not take into account any secondary revenue that might accrue to authors from increased readership. Moreover, this number does not take into account the possibility that publishers could raise their prices on new books as a result of consumer resale opportunities in the used marketplace (Ghose et al. 2005).

We also note that the overall impact of used-book markets on social welfare is overwhelmingly positive. The consumer surplus gains and producer surplus losses, together with an estimated \$65.76 million increase in Amazon.com’s gross profit from the usedbook exchanges, suggest a net welfare gain to society of approximately \$87.92 million from these used-book exchanges.

The remainder of this paper proceeds as follows. In §2, we discuss the literature relevant to our present work. In §3, we develop an analytic model of used-product markets to highlight the importance of empirical measurements in determining the degree to which used products cannibalize new-product sales. In §4, we compare the characteristics of the brick-andmortar used-book market to the Internet used-book market to show that the Internet may have a significant effect on used-book sales. We describe our data in §5 and present our empirical model and results in §6. We discuss the implications of our results in §7.

## 2. Literature

Our research is related to different streams of extant work. The first stream of relevant literature relates to implications of concurrent availability of new and used goods. The difficulty of maintaining monopoly power on durable goods is due in part to the problem of time inconsistency first pointed out by Coase (1972). Coase conjectured that if a firm were to exploit its residual demand in future periods, then rational consumers would anticipate this behavior and price would rapidly fall to the competitive level. The interrelationship between the markets for new and used goods was pointed out by Benjamin and Kormendi (1974) and Liebowitz (1982). They argued that a monopolist can maintain market power by restricting the used market. Using the textbook market as an example, Miller (1974) suggests that the opening of secondary markets will force publishers to increase new-good prices to extract the maximum possible profit from the onetime sale of a new good. Further research in this area has shown that a monopolist can avoid the commitment problem by leasing as opposed to selling (Bulow 1982), and that depreciation reduces the monopolist’s incentive to cut price (Bond and Samuelson 1984). The main argument of these papers is that secondhand markets need not hurt the manufacturer because manufacturers will anticipate the resale value of their product and will increase the price of the new good accordingly.

A more recent stream of the literature uses analytic models to show that secondary markets also create a substitution effect because new goods face competition from used goods (Anderson and Ginsburgh 1994, Hendel and Lizzeri 1999). When considering the impact of used-good markets in competitive newgood markets, upstream suppliers such as book publishers can benefit from secondary markets under some conditions, as shown by Ghose et al. (2005).

Recent empirical work in the context of used goods has used aggregate data to show that textbook sell-through—new sales as a proportion of total sales—declines radically from 90% in the first year of a textbook’s publication to 45% in the second year and 10% in the third year (Greco 2005, pp. 185–186; Greco et al. 2005). A more recent study also uses textbook data to show that students are forward looking when making their purchases—and that their value of a textbook declines when the release of a new edition will foreclose on the resale market for a new textbook purchase (Chevalier and Goolsbee 2005).

A third stream of literature relevant to our study is research developing techniques to estimate welfare effects from the introduction of new goods. Classic economic theory shows that if the price of an existing good changes from $p _ { 0 }$ to $p _ { 1 \cdot }$ , the resulting change in welfare is given by how much the consumer would pay, or would need to be paid, to be just as well off after the price change as they were before the price change. This measure corresponds to Hicks’ (1942) compensating variation measure. To measure the welfare change from the introduction of a new good, Hausman (1997a) modifies Hick’s measure by using the product’s “virtual price”—the price that would set demand to zero—as $p _ { 0 }$ and the introductory price as $p _ { 1 }$ . This technique has been applied to measure welfare gains for new goods ranging from Honeynut Cheerios (Hausman 1997b) to increased product variety on the Internet (Brynjolfsson et al. 2003). Related techniques have also been used to analyze the welfare impact from online auction sites (Bapna et al. 2005).

Finally, our research draws on the literature relating to competition on the Internet (e.g., Brynjolfsson and Smith 2000, Clay et al. 2001, Baye et al. 2004), and specifically the direct measurement of consumer price sensitivity. Papers in this literature have shown that BarnesandNoble.com seems to face much stronger competition from Amazon.com than Amazon does from Barnes & Noble (Chevalier and Goolsbee 2003). Various papers in this literature have also analyzed the own-price elasticity for offers listed at shopbots, finding elasticity measures ranging from <sub>−</sub>6 to <sub>−</sub>10 for shopbots listing books (Brynjolfsson et al. 2004) and PDAs (Baye et al. 2004) sold by differentiated sellers to <sub>−</sub>50 for a shopbot listing computer motherboards and memory modules sold by undifferentiated sellers. Elasticity measures at Internet shopbots are relevant for our study because the display of information at these services is comparable to the information display in Amazon’s used-book marketplace.

## 3. Theoretic Analysis

In this section, we develop a model to analyze the impact of secondary markets on welfare to publishers, retailers, and consumers. Our model spans two periods and consists of a single publisher, S selling a new good through a retailer at a wholesale price of $w ,$ to a unit mass of consumers. The book is new when it is marketed in Period 1 and can be sold as used in Period 2 when it undergoes some degradation in quality. The retailer opens a secondary (used book) market where consumers can buy and sell used goods. Whenever a consumer sells the used book, the retailer gets a commission k per used good sold, while the rest 1 k is the gain to the consumer. For example, Amazon charges a 15% commission (as a fraction of the used-book sale price) to each used book seller, while the remaining 85% of the used-book sale price goes to the consumer.

Further, let  be a consumer’s valuation for a good, where $\theta \sim U [ 0 , 1 ]$ . The type parameter  indicates a consumer’s marginal valuation for quality. For any given quality, a consumer with a higher  is willing to pay more for the product than one with a lower . Without loss of generality, let 1 denote the quality of the new good and q denote the quality of the used good, where $0 < q < 1 ;$ thus, q can be interpreted as the degree of quality degradation of new book. If a consumer purchases a book of quality q at price $p ,$ her utility is $U ( \theta ) = \theta q - p$

The game is modeled as a multistage game. First the retailer chooses an optimal new good price given the per-unit wholesale price w set by the supplier. Then market forces determine the optimal price of used goods from clearance conditions. Finally, consumers demand is realized. We consider a subgame perfect equilibrium of this game using backward induction.

## 3.1. No Secondary Electronic Market

We begin by modeling the case where only new goods are sold in the marketplace. We denote the price of the new good in the absence of a used-good market as $P _ { N }$ Thus, consumers buy a new book as long as they get positive surplus; i.e., as long as $\theta - P _ { N } > 0$ . Hence, the demand for a new book is $D _ { N } ( P _ { N } ) = 1 - \theta = 1 - P _ { N }$ Under these conditions the profit of the publisher is,

$$
\pi_ {S} = D _ {N} * w = (1 - P _ {N}) w\tag{1}
$$

and profit to the retailer is

$$
\pi_ {R} = D _ {N} * (P _ {N} - w) = (1 - P _ {N}) (P _ {N} - w).\tag{2}
$$

In equilibrium, the retailer maximizes this profit by setting $P _ { N } ^ { * } = ( 1 + w ) / 2$ . At this price, the publisher makes a profit of $\pi _ { S } = ( w ( 1 - w ) ) / 2$ while the total profit of the retailer is

$$
\pi_ {R} = D _ {N} * (P _ {N} - w) = (1 - P _ {N}) (P _ {N} - w) = \frac {(1 - w) ^ {2}}{4}.\tag{3}
$$

Note from (1) that in equilibrium the publisher will set $w ^ { * } = 1 / 2$

## 3.2. Retailer Establishes a Secondary Electronic Market

The presence of a secondary market allows new-book buyers to sell them later. Rational consumers take this into account in their utility function in the buying process. As a result, the retailer (and/or publisher) should be able to sell the new book at a higher price. This is the price-increase effect, as outlined in the prior literature (e.g., Miller 1974, Swan 1980).

However, Waldman (1997) and Hendel and Lizzeri (1999) argue that the used-book market also creates a substitution effect. The substitution effect arises from the fact that new books face competition from used books. Accordingly, some consumers who previously would have bought a new book will shift to the used-book market, cannibalizing new-book sales. The price-increase effect will increase publisher welfare, while the cannibalization effect will decrease publisher welfare. The actual impact of used-book markets on publisher welfare depends on the actual elasticity and propensity to resell books observed in the market.

Figure 1 Market Segmentation in the Presence of a Secondary Electronic Market

<table><tr><td>Buy nothing</td><td>Buy used</td><td>Buy new and sell</td></tr><tr><td>0</td><td> $\theta_{2}$ </td><td> $\theta_{1}$ </td></tr></table>

Figure 1 describes the segmentation of the market based on consumer types. Let $P _ { N } ^ { U }$ and $P _ { U }$ denote the new and used-book prices, respectively, in the presence of used-book markets. An artifact of secondary markets is that not all consumers resell their used books. There could be multiple reasons for some consumers to hold on to their used book. For example, not all consumers may be aware of the existence of the used-book market, or the transactions and search costs faced by some consumers could be sufficiently large that they do not have an incentive to participate in the used-book markets. In short, the net utility to some consumers from keeping the book might exceed that from selling it. To account for this fact, we assume that only a proportion  of new-good buyers eventually sell their used goods.<sup>3</sup> Hence, the expected revenue from a used-book sale (which is equivalent to $( 1 - k ) P _ { U } )$ realized by consumers is $\alpha ( 1 - k ) P _ { U }$ , where $\alpha \in ( 0 , 1 )$ and the commission charged by retailers for selling used books is k. Hence, the corresponding expected utilities derived from various strategies are as follows:

(ii) Buy used good: $\theta q - P _ { U }$

$$
\theta - P _ {N} ^ {U} + \alpha (1 - k) P _ {U}.
$$

(iii) Buy nothing: 0.

Thus, higher-valuation consumers buy new goods and lower-valuation consumers wait and buy used goods later. It is important to recognize that, in our model, the number of consumers in these groups emerges endogenously. This ensures that clearance conditions will equalize demand and supply of used goods at all times. The new profit of the publisher is given by

$$
\pi_ {S} ^ {U} = D _ {N} ^ {U} w ^ {U} = (1 - \theta_ {1}) w ^ {U},\tag{4}
$$

where $D _ { N } ^ { U }$ denotes the demand for new books in the presence of used books. Similarly, profits for the retailer can be written as

$$
\begin{array}{r l} & {\pi_ {R} ^ {U} = D _ {N} ^ {U} (P _ {N} ^ {U} - w ^ {U}) + D _ {U} P _ {U} k} \\ & {\quad = (1 - \theta_ {1}) (P _ {N} ^ {U} - w ^ {U}) + (\theta_ {1} - \theta_ {2}) P _ {U} k.} \end{array}\tag{5}
$$

Here the $D _ { U }$ is demand for the used books. Note that retailers, like Amazon, also enjoy the benefits of increased used-book sales on its marketplace through the commission k that it charges to used-book sellers. This used-book demand effect is not available to publishers. Thus, in general, retailers are more likely to benefit from used-book markets than publishers are.

By comparing (1) and (4), we get the publisher’s loss/gains from the establishment of a used-book market as

$$
\begin{array}{r l} & {\pi_ {S} ^ {U} - \pi_ {S} = D _ {N} ^ {U} w ^ {U} - D _ {N} w} \\ & {\qquad = \underbrace {(D _ {N} ^ {U} - D _ {N})} _ {\mathrm{Substitutioneffect}} w + \underbrace {(w ^ {U} - w)} _ {\mathrm{Price-increaseeffect}} D _ {N} ^ {U}.} \end{array}\tag{6}
$$

Similarly, for the retailer, the loss/gain from the establishment of the used-book market (after substituting $R ^ { U }$ for $( P _ { N } ^ { U } - w ^ { U } )$ and R for $( P _ { N } - w )$ and comparing (2) and (5)) is given by

$$
\begin{array}{c} \pi_ {R} ^ {U} - \pi_ {R} = D _ {N} ^ {U} R ^ {U} - D _ {N} R + D _ {U} k P _ {U} \\ = \underbrace {(D _ {N} ^ {U} - D _ {N})} _ {\text {Substitution effect}} R + \underbrace {(R ^ {U} - R)} _ {\text {Price - increase effect}} D _ {N} ^ {U} \\ + \underbrace {D _ {U} k P _ {U}} _ {\text {Used - book demand effect}}. \end{array}\tag{7}
$$

Thus, consistent with the prior literature, used-book markets have two countervailing effects on publisher welfare. On one hand, used books cannibalize the sales of new books, reducing publisher welfare. On the other hand, the presence of the used-book market may lead to increased consumer willingness to pay for new books, and as a result higher prices. Which of these two effects dominates depends on the actual behavior of customers in the market—notably, the sensitivity of consumers to used-book prices, which can be measured by the own- and cross-price elasticities of demand observed in the market.<sup>4</sup> However, while these effects have been well studied in the analytic literature, we are aware of no papers in the empirical literature that have directly measured them. Moreover, as noted above, direct estimates of the cannibalization of new books by used markets is a very important—and currently unavailable—measure for publishers and authors. Thus, a key contribution of our research is to develop and implement a methodology for creating these measures.<sup>5</sup>

To do this, we note that the relevant prices and margins in (6) and (7) can typically be observed through secondary sources. Likewise, recent research results (Brynjolfsson et al. 2003) can shed light on Amazon’s used-book sales $( D _ { U } )$ . However, the substitution effect cannot be measured directly. To measure this effect, we note that under the standard definition of elasticity $( \eta = ( \Delta Q / \Delta P ) ( P / Q ) )$ , the substitution effect can be measured as

$$
D _ {N} ^ {U} - D _ {N} = \Delta Q = D _ {N} \times \eta \times \frac {P _ {N} ^ {U} - P _ {U}}{P _ {N} ^ {U}}.\tag{8}
$$

This shows that measuring the cross-price elasticity of new-book demand with respect to used-book prices  is critical to being able to measure the substitution effect, and therefore the change in publisher and retailer surplus. One contribution of our work is implementing a methodology to measure this elasticity in the context of Internet sales.

Thus, the key insight from this model is that the extent of gains (and losses) critically depends on the effects outlined in (6) and (7). However, the substitution effect, price-increase effect, and used-book demand effects are inherently empirical in nature. Therefore, the theoretical model provides us with key measures that need to be quantified to assess the benefits of used-book markets to different parties involved in these transactions. Hence, in our empirical analysis we estimate the extent of substitution effect (or cannibalization effect) and extent of used-book demand effect. With this information, we then quantify the gains (and losses) to publishers and retailers based on real-world data from an Internet used-book market.

## 4. Analysis of Brick-and-Mortar vs. Internet Used-Book Markets

As noted above, there is nothing new about the sale of used books. Rather, what changes on the Internet is a radical increase in the variety of used books offered for sale, a radical decrease in the prices of these used books, and a radical decrease in the associated search costs for consumers to locate these used books. To illustrate the magnitude of these changes, in June 2004 we generated a list of 30 randomly selected books from the October 2002 Bowker’s Books in Print listings, and 30 randomly selected books from the 2002 New York Times bestseller lists. These lists are useful because they are old enough to include books that would generally be available in physical bookstores, and they contain a mix of popular and less popular titles.

We searched for these books at Amazon.com and found that at least one used copy was available for each of the 60 books we sampled—even though 13 of the books were out of print and did not have new copies available from Amazon itself. Moreover, there was an average of 22.6 competing used-book offers for each random book, and an average of 241.3 competing offers for each former New York Times bestsellers. These multiple offers create competition among sellers to lower their prices. As a result, the random books have an average 40.1% discount off the new-book list price and the former bestsellers have an average 84.5% discount off list price. As a point of comparison, Amazon’s new books had an average 9.1% and 30% discount off list price for these random and former bestselling titles.

To understand how the used-title selection at Amazon would compare to the selection of a typical brick-and-mortar used-book store, we searched the catalogs of four brick-and-mortar used-book stores in the Pittsburgh area advertising themselves as having a “general selection.” Three of the four stores did not carry any of the 60 books on our list. The fourth, Eljay’s Used Books, carried none of the random books and only six of the former bestsellers. Moreover, Amazon’s used price was an average of 75% (\$8.16) lower than the price at Eljay’s for these six books.

As another point of comparison, we used ABEbooks.com to search for the used-book store in the United States with the widest selection of titles in our sample. ABEbooks catalogs the inventory of 7,680 used-book sellers in the United States.<sup>6</sup> According to ABEbooks’ listings, Powell’s Books of Portland, Oregon, had the best selection of any of these 7,680 booksellers for the books in our sample—but still only carried 11 of the 30 random titles and 29 of the 30 former bestsellers. Moreover, the used price at Amazon averaged 38% (\$4.93) lower than the Powell’s price on the random books and 67% (\$7.03) lower than the Powell’s price on the former bestsellers.

Thus, a used-book shopper at Amazon.com would have lower search costs to locate a book, significantly larger selection (both in terms of availability and the number of competing offers), and dramatically lower prices than they are likely to find at their local used-book store (even if they are fortunate enough to live close to Powell’s Books in Portland). Moreover, because new and used books are listed side by side in many Internet markets, new-book shoppers can more easily become aware of used-book offerings than they could in a typical brick-and-mortar bookstore, and might be tempted by the wide selection and low prices to buy a used book instead of a new book. Together, these factors may be what is driving the penetration of used-book sales through the Internet channel: used-book sales are growing at a rate of 30% per year (Wyatt 2005) and accounted for 54.4% of all used-book sales in 2003 (Siegel and Siegel 2004) and 67% of all used-book sales in 2004 (Wyatt 2005). As a point of comparison, new-book sales on the Internet accounted for only 12.7% of total book sales in 2003 (Rappaport 2004).

## 5. Data

Our data are compiled from publicly available information on new- and used-book prices and sales ranks at Amazon.com. The data are gathered using automated Perl scripts to access and parse HTML pages downloaded from the retailer. The data were collected in two separate samples. The first was collected over a 180-day period from September 2002 to March 2003 and includes 273 individual book titles. This panel of books includes an equal number of books from each of five major categories—New York Times best sellers, former New York Times bestsellers, Amazon Computer bestsellers, best-selling textbooks, and new and upcoming books. New York Times bestsellers were selected at random from the current New York Times list at the beginning of the sample and were replaced as they were removed from the list. Former bestsellers were selected at random from the full list of books appearing in New York Times bestseller listings in the year 1999. Computer bestsellers and new and upcoming books were selected at random from the respective list at Amazon.com. Finally, bestselling textbooks were selected from the facultyonline.com bestseller list.

In early 2004 Amazon.com added a new variable to their XML data feed to developers, allowing us to obtain accurate measures of their used-book sales (which we describe in more detail below). At this point, we created a similar sample of books, drawing 40 books from each of four categories: current bestsellers, former bestsellers, new and upcoming, and random. New and upcoming books were selected in the same way as the first sample. Current and former bestsellers were drawn from the current list of Amazon best-selling books and Amazon’s top-selling books in 2002. Finally, random books were selected at random from all Amazon.com titles listed in the “browse” section (which we believe includes all titles offered for sale by Amazon). In this sample, we dropped 15 books (10 random titles and 5 former bestsellers) that were out of print and therefore did not have new Amazon prices. These data were collected over an 85-day period from April to July 2004. Our total data sample includes 41,994 observations of 393 titles.

For each sample, we collect data on the Amazon. com sales rank and new-book price, and the book prices charged by Amazon.com marketplace sellers. Our marketplace data include the price, condition, and seller rating for each used book listed for sale. Book condition is self-reported by the seller and can be either “like new,” “very good,” “good,” or “acceptable.” We also collect the seller rating for each used bookseller, which is a one to five-star measure of the reported experiences of prior buyers with each seller.

In addition to these variables, in the second sample we were able to use Amazon’s XML data feed to collect the number of used books sold. We do this by using the unique product identifier for each product listed in the used-book market. This unique identifier was added to the XML feed sometime between March 2003 and April 2004, making it available only in the second half of our sample. Using this product identifier, we infer that a sale has occurred when an identifier that appeared in the previous collection period does not appear in the current collection period’s XML listings. We collected this data once every two hours for books with a sales rank lower than 10,000, and every six hours for all other titles. In our empirical estimates below, for sessions where multiple sales are observed in-between two collection periods (11% of the sessions in our sample), we assume that the books were sold in order of price. This is consistent with the strong preference we observe in our data for low-priced books. To the extent that this assumption is incorrect, it will inflate our estimates of the own-price elasticity of used-book demand and mean that our consumer surplus estimates represent a lower bound on the true consumer surplus gain.

Finally, for the second sample, we collect the number of lifetime ratings for each seller at the start of our data collection.<sup>7</sup> From the number of lifetime ratings, we generate two additional variables: a dummy variable identifying when a particular seller has zero lifetime ratings, and a dummy variable for the top 10 sellers in our sample on the basis of the most lifetime ratings.<sup>8</sup> Table 1 lists summary statistics for our data. All prices represent the lowest price for each ISBN.

Table 1 Summary Statistics

<table><tr><td>Variable</td><td>Obs.</td><td>Mean</td><td>St. dev.</td><td>Min</td><td>Max</td></tr><tr><td>Amazon rank</td><td>41,994</td><td>74,169</td><td>238,283</td><td>1</td><td>2,556,356</td></tr><tr><td>List price</td><td>41,994</td><td>30.60</td><td>30.05</td><td>5.99</td><td>299.99</td></tr><tr><td>Amazon price</td><td>41,994</td><td>24.04</td><td>26.47</td><td>1.95</td><td>209.99</td></tr><tr><td>Best “like new” used price</td><td>41,492</td><td>15.16</td><td>21.32</td><td>0.01</td><td>194.25</td></tr><tr><td>Best “very good” used price</td><td>33,517</td><td>11.26</td><td>18.41</td><td>0.01</td><td>207.60</td></tr><tr><td>Best “good” used price</td><td>31,939</td><td>11.24</td><td>16.42</td><td>0.01</td><td>200.00</td></tr><tr><td>Best “acceptable” used price</td><td>20,368</td><td>7.86</td><td>15.70</td><td>0.01</td><td>222.35</td></tr><tr><td>Best used price (all conditions)</td><td>41,994</td><td>13.14</td><td>19.16</td><td>0.01</td><td>151.95</td></tr><tr><td>Seller rating</td><td>41,994</td><td>3.97</td><td>1.65</td><td>1</td><td>5</td></tr><tr><td>Count of used books</td><td>41,994</td><td>81.15</td><td>131.78</td><td>1</td><td>753</td></tr><tr><td>Days since release</td><td>41,994</td><td>717.87</td><td>1,336.94</td><td>1</td><td>21,235</td></tr></table>

## 6. Results

## 6.1. Sales Rank to Quantity Calibration

Until recently, it was difficult to calculate the price elasticity for products sold on the Internet because, while the price of individual items could be readily observed, the quantity sold was generally unobservable. Two recent papers address this problem, providing a way to map the observable Amazon.com sales rank to the corresponding number of books sold. In both cases, the authors find a stable relationship between the ordinal sales rank of a book and the cardinal number of sales, using roughly the following Pareto relationship:

$$
Q u a n t i t y = \delta \cdot R a n k ^ {\beta}.\tag{9}
$$

Chevalier and Goolsbee (2003) calibrate this relationship using a creative and easily executed experiment where the authors obtain a book with a known number of weekly sales, purchase several copies of the book in rapid succession from Amazon.com, and track the Amazon sales rank before and shortly after their purchase. Using these two points, they estimate $\beta = - 0 . 8 5 5 . ^ { 9 }$ They also estimated this parameter from similar sales-rank experiments conducted by

Weingarten (2001) and Poynter (2000) as 0952 and <sub>−</sub>0834, respectively.

Brynjolfsson et al. (2003) calibrate this relationship using data from a publisher mapping the Amazon sales rank to the number of copies the publisher sold to Amazon in the summer of 2001. The data include weekly sales and rank observations for 321 books with sales ranks ranging from 238 to 961,367. Using these data, they estimate $\beta = - 0 . 8 7 1$

For the purposes of this paper, we will use the Brynjolfsson et al. (2003) estimate because it is based on 861 data points as opposed to two data points in the experiments; however, our results are not particularly sensitive to this choice versus one of the other estimated parameter values.

Note that the $\beta$ parameter will be stable over time as long as customers’ relative tastes for popular and obscure books do not change. Increases in sales over time (holding tastes constant) will only shift the  parameter, a scaling parameter that does not impact our elasticity calculations. Also note that any shifts in customer preferences for new books that resulted from the introduction of used-book marketplaces would be incorporated into our parameter estimate, as the sales-rank data used by both Chevalier and Goolsbee (2003) and Brynjolfsson et al. (2003) were gathered well after the December 2000 introduction of Amazon’s used marketplace.

We also empirically confirmed that during the time of our study Amazon’s sales rank was calculated based only on new-book sales, as opposed to new and marketplace sales.<sup>10</sup> To do this, we located a book with a high sales rank and observed the rank of this title over the course of several weeks. During our observation period, the sales rank of the book varied between 596,625 and 606,439, and based on the movement of the rank, the book appeared to have one sale every two weeks. Having established the initial rank of the book, we then listed five used books for this title in Amazon’s used-book marketplace and purchased them on Monday, October 23, 2002, using five different Amazon.com buyer accounts. The sales rank before we made the purchase was 599,352 and it remained stable until October 30, when it increased to 601,457. On October 30, we purchased five copies of the new book using the same Amazon accounts, and the next morning the sales rank was 4,647. We infer from this that marketplace sales were not included in Amazon’s sales-rank figures during our study period. (Note that, assuming this book had one sale every two weeks at a rank of 599,352, our estimated  parameter for this experiment would be 0877.)

## 6.2. Estimation

We run two regressions to analyze the structure of Amazon’s new- and used-book marketplaces. First, we analyze the impact of new and used prices on new-book sales by estimating models of the form

$$
\begin{array}{r} \mathrm{Log} (R a n k _ {b t}) = c + \Gamma \cdot \mathrm{Log} (A m a z o n P r i c e _ {b t}) \\ + \Psi \cdot \mathrm{Log} (U s e d P r i c e _ {b t}) + \Omega^ {\prime} X + \varepsilon_ {b t}, \end{array}\tag{10}
$$

where b and t index book and date. The dependant variable is the log of rank. The independent variables are Amazon price (AmazonPrice), the lowestpriced used book in the market (Used-Price), and a vector of other control variables X. Our control variables include the log of the time since the book was released, the condition of the lowest-priced used book, the seller rating for the lowest-priced used book, and the log of the number of used books offered for sale for a particular book.  , , and ! are the parameter vectors to be estimated.

Note that because of the structure of this industry, quantity and price are not jointly determined, and thus we do not face the endogeneity concerns that would normally arise in demand regressions. With regard to Amazon’s own price, because books are produced in large printings prior to going to market, the quantity of new books Amazon can sell is predetermined (and usually virtually infinite) at the time Amazon sets their price. Likewise, used price is not a function of current-period sales at Amazon, as used copies typically would take some time before they enter the used-book market.<sup>11</sup> This follows the standard approach taken in the literature for demand estimation of Internet book sales (see, for example, Chevalier and Goolsbee 2003).

For the second regression, we use the fact that we observe each of the marketplace offers shown to Amazon’s used-book customers along with the offer each customer chose to purchase. Because of this, we can use the multinomial logit model (Ben-Akiva and Lerman 1985, Guadagni and Little 1983) to determine the sensitivity of customers to the parameters of the offered products. Specifically, under the multinomial logit model we assume that used-book customers maximize an indirect utility function of the form

$$
u _ {i j} = z _ {j} \theta + \varepsilon_ {i j},\tag{11}
$$

where $u _ { i j }$ represents the utility of user i for offer $j ,$ which is a linear combination of the observed product characteristics z and their associated parameters , and a mean zero random disturbance $( \varepsilon _ { i j } )$ . Under the assumption that $\varepsilon _ { i j }$ follows a Type-I extreme value distribution, if consumers select the offer that maximizes their utility, then the conditional probability that offer j will be selected is given by a standard multinomial logit equation

$$
P _ {j} = \frac {\exp (z _ {j} \theta)}{\sum_ {r = 1} ^ {J} \exp (z _ {r} \theta)}.\tag{12}
$$

Table 2 presents regression results of the impact of new and used price on sales rank (Equation (10)). To estimate this model, we use OLS with book-level fixed effects.<sup>12</sup> Models 1–4 in Table 2 progressively add control variables to check the stability of our parameters of interest. Note that the parameters of interest (Amazon and used prices) have the expected signs (recall that an increase in sales rank implies a decrease in sales), are precisely estimated, and the parameter estimates and associated standard errors are stable across specifications, suggesting that the estimates are robust and that multicollinearity is not a significant problem in the model.<sup>13</sup>

The other control variables suggest that, as expected, sales of new books decrease over time, and older books and books with more used copies for sale have higher rank. It might be initially surprising that both seller rating and condition are insignificant in our regressions. However, it is important to realize that this does not necessarily mean that condition and/or rating are unimportant to used-book purchasers, but rather that the condition and rating of the lowest-priced book are not what is driving the cannibalization of new-book sales.

Table 2 Results for New-Book Market

<table><tr><td>Indep. vars.</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Constant</td><td>-2.059**(0.161)</td><td>-2.067**(0.161)</td><td>-2.078**(0.161)</td><td>-2.161**(0.162)</td></tr><tr><td>Ln(Amazon price)</td><td>1.347**(0.048)</td><td>1.347**(0.048)</td><td>1.347**(0.048)</td><td>1.345**(0.048)</td></tr><tr><td>Ln(min. used price)</td><td>-0.105**(0.010)</td><td>-0.105**(0.010)</td><td>-0.105**(0.010)</td><td>-0.102**(0.010)</td></tr><tr><td>Ln(days since release)</td><td>1.142**(0.015)</td><td>1.140**(0.015)</td><td>1.140**(0.015)</td><td>1.120**(0.015)</td></tr><tr><td>Condition rating</td><td></td><td>0.009*(0.004)</td><td>0.008(0.004)</td><td>0.008(0.004)</td></tr><tr><td>Seller rating</td><td></td><td></td><td>0.003(0.003)</td><td>0.003(0.003)</td></tr><tr><td>Ln(number of used for sale)</td><td></td><td></td><td></td><td>0.057**(0.011)</td></tr><tr><td>No. of observations</td><td>41,994</td><td>41,994</td><td>41,994</td><td>41,994</td></tr><tr><td>Pseudo  $R^2$ </td><td>0.229</td><td>0.229</td><td>0.229</td><td>0.228</td></tr></table>

Notes. The dependent variable is Ln(sales rank). Standard errors are listed in parenthesis; ∗∗ and ∗ denote significance at 0.01 and 0.05, respectively. All models use book-level fixed effects.

However, while condition and seller rating do not appear to be driving the cannibalization of newbook sales, they do have a strong impact on the choices of used-book customers. This can be seen in Table 3, which provides estimates of the taste parameters ( in Equation (11)) for Amazon.com’s used-book customers. These parameters are precisely estimated and relatively stable across specifications. The signs of the parameters suggest that, as expected, higherpriced used books are less likely to be purchased, and books in “very good” condition are preferred to “good” condition books, which are in turn preferred to “acceptable” books. It is surprising that each of these conditions is preferred to “like new” condition books, the referenced category. This could be driven by the fact that used-book customers are very sensitive to price and “like new” condition books carry much higher prices than the other used-book categories. Finally, we see from Table 3 that seller characteristics matter for customer choice. Sellers with higher ratings and more lifetime ratings are preferred to other sellers, sellers with at least one rating are strongly preferred to sellers with no ratings, and the top 10 sellers in our sample (who are exclusively large professional book sellers) are preferred to other sellers.

Table 3 Multinomial Choice Results for Used-Book Market

<table><tr><td>Indep. vars.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>6</td></tr><tr><td>Used price</td><td>-0.055**(0.001)</td><td>-0.054**(0.001)</td><td>-0.054**(0.001)</td><td>-0.055**(0.001)</td><td>-0.055**(0.001)</td></tr><tr><td>“Very good”condition (0/1)</td><td></td><td>0.210**(0.011)</td><td>0.191**(0.011)</td><td>0.184**(0.011)</td><td>0.184**(0.011)</td></tr><tr><td>“Good” condition (0/1)</td><td></td><td>0.186**(0.015)</td><td>0.163**(0.015)</td><td>0.147**(0.015)</td><td>0.148**(0.015)</td></tr><tr><td>“Acceptable”condition (0/1)</td><td></td><td>0.095**(0.027)</td><td>0.068*(0.027)</td><td>0.053(0.027)</td><td>0.051(0.027)</td></tr><tr><td>Rating (1–5 stars)</td><td></td><td></td><td>0.032**(0.003)</td><td>0.013**(0.003)</td><td>0.011**(0.004)</td></tr><tr><td>Ln(lifetime ratings + 1)</td><td></td><td></td><td></td><td>0.014**(0.002)</td><td>0.008**(0.002)</td></tr><tr><td>Top 10 sellingmerchant (0/1)</td><td></td><td></td><td></td><td></td><td>0.042*(0.017)</td></tr><tr><td>No seller ratings (0/1)</td><td></td><td></td><td></td><td></td><td>-0.058*(0.023)</td></tr></table>

Notes. The dependent variable is whether a used book is sold. Standard errors are listed in parenthesis; ∗∗ and ∗ denote significance at 0.01 and 0.05, respectively. We observe 9.8 million offers across 56,091 choice sets.

We can use the results of these two regressions to calculate the relevant own- and cross-price elasticities in the new and used markets. With respect to the new market, one can easily show from (9) and (10) that own- and cross-price elasticity are given by  and  , respectively. Thus, using  <sub>=</sub> <sub>−</sub>0871, we see that Amazon’s own-price elasticity is approximately 117, while the cross-price elasticity of new-book sales to used-books prices is approximately 0.088.<sup>14</sup>

Both results have the expected signs. Amazon’s ownprice elasticity is close to 1, which is consistent with what one might expect from a firm with significant market power. The cross-price elasticity estimates are quite low, suggesting that used books are not a strong substitute for new books for most of Amazon’s customers.

To calculate the own-price elasticity of used-book offers, we note that under the multinomial logit model, the own-price elasticity of demand for an individual offer is given by (Ben-Akiva and Lerman 1985, p. 111):

$$
\eta_ {j k} = \alpha_ {k} p _ {k} (1 - P _ {j}),\tag{13}
$$

where $\alpha _ { k }$ is the estimated parameter of used price, $p _ { k }$ is used price itself, and $P _ { j }$ is the conditional choice probability defined in Equation (11). Using (13), we can calculate the average own-price elasticity imputed for offers in each session and take the average of this across sessions to obtain an own-price elasticity of 487.<sup>15</sup>

This elasticity, as expected, is high—suggesting that the used-book marketplace is competitive and small price changes have large impact on the probability of a book being sold. Similar, although generally larger, estimates for demand elasticities are also found by other researchers in the context of shopbots—settings where the layout of offers is very similar to Amazon’s used-book marketplace.<sup>16</sup> The fact that our elasticity is slightly lower is likely due to the degree of differentiation in offerings across the studies: In our study both products (quality) and sellers (ratings) are differentiated, while prior studies of shopbot elasticity were conducted in the context of either undifferentiated products (Brynjolfsson et al. 2004) or both undifferentiated sellers and undifferentiated products (Ellison and Ellison 2004).

## 6.3. Welfare Estimations

6.3.1. Publisher Welfare. As noted in §3, publishers are worse off in the presence of a usedbook marketplace if there is no increase in the price of new books after the introduction of the usedbook markets. Conversations with representatives of three major publishers revealed no changes in the wholesale prices of books following the introduction of Internet used-book marketplaces. Al Greco, the author of the Book Industry Study Group’s annual Book Industry Trends and a professor at Fordham University, confirmed that in his research there have been “no significant changes in wholesale prices” in recent years as a result of the introduction of used-book markets on the Internet.<sup>17</sup> Because of this, we assume in our welfare calculations that publisher prices have not changed as a result of the introduction of Internet exchanges for used books.<sup>18</sup> Under this assumption, we can use our elasticity estimates and Equation (8) above to estimate the loss in publisher profit from the presence of Amazon’s used-book market.

Brynjolfsson et al. (2003) calculate that after the introduction of the used marketplace Amazon sold approximately 99.4 million books per year. However, this represents sales after the introduction of the used-book marketplace $( D _ { N } ^ { U } )$ , not before $( D _ { N } )$ . Thus, we must rewrite (8) in terms of observed variables (specifically D<sup>U</sup> ), which gives us

$$
\begin{array}{l} \Delta Q = (D _ {N} ^ {U} - D _ {N}) = D _ {N} ^ {U} \frac {\eta \cdot \Delta P \%}{(1 - \eta \cdot \Delta P \%)} \\ \text {where} \quad \Delta P \% = \left(\frac {P _ {N} ^ {U} - P _ {u}}{P _ {N} ^ {U}}\right). \end{array}\tag{14}
$$

From our calculations above, the cross-price elasticity of new-book sales to used-book prices  is approximately 0.088. Finally, used books in our sample are sold at an average discount of 50.6% off Amazon’s new price $( \Delta P \% = 0 . 5 0 6 )$ . From these figures, Equation (14) shows that Amazon lost 4.63 million sales Q due to the presence of used-book markets.

We can use (6) to characterize the loss in publisher profit from this change in sales by noting that according to Brynjolfsson et al. (2003), the wholesale cost of adult trade books is between 43%–51% off the book’s list price, and publisher gross margins on sales are typically 56%–64%. Then taking 60% as the typical margin, 47% as the typical discount off list price for wholesale prices, and noting that the average list price in our sample is \$30.60, we calculate that publisher lost gross profit from Amazon.com’s used-book market is approximately \$45.05 million.<sup>19</sup>

6.3.2. Retailer Welfare. With regard to retailer welfare, Amazon.com incurs a loss from the decrease in the quantity of new books sold, which may be mitigated by an increase in revenue from used-book marketplace sales that otherwise would not have occurred at the new-book prices. Because we observe $Q _ { n } , P _ { n } ,$ and the relevant cross-price elasticities, we can measure the net change in retailer welfare from these two effects. To do this, we first calculate Amazon’s dollar contribution margins on new and used books. For new books, Wingfield (2003) places Amazon’s gross margins on new-book sales at approximately 22% which, given Amazon’s average price \$24.04 for new books, gives a dollar contribution margin of \$5.29.

For used books, Amazon also earns revenue of \$0.99 plus 15% of the sale price on their used-book sales.<sup>20</sup> In addition, Amazon charges buyers \$3.49 for shipping and reimburses sellers \$2.26 for their shipping costs, and thus earns \$1.23 on shipping per unit sold. Given that the average price of used books in our sample that are sold is \$8.76,<sup>21</sup> the dollar contribution margin on used-book sales is approximately \$3.04 (35%).<sup>22</sup> Thus, Amazon’s losses on cannibalized new-book sales net their gains on the corresponding used-book sale work out to approximately (\$225 \$529 \$304 for each cannibalized new book, or a total of \$10.42 million for the 4.63 million cannibalized new-book sales.

However, as noted above, Amazon also gains incremental customers from the presence of their used marketplaces. Our results suggest that these incremental customers could be quite substantial. Milliot (2002) notes that across all product categories sold at Amazon.com, used products accounted for 23% of Amazon’s sales. Moreover, used sales in the book category were one of the strongest of any product category, according to Jeffrey Bezos. Thus, 23% may be an underestimate of the actual proportion of used sales in the book category.

If Amazon sells 99.4 million new books annually (Brynjolfsson et al. 2003) and used-book sales made up 23% of total book sales (both new and used), then approximately 29.69 million used books are sold through Amazon’s marketplace annually. Recalling that only 4.63 million of these sales cannibalized newbook sales, we estimate that Amazon sold approximately 25.06 million used-book copies that would not otherwise have been sold new on the site. Said another way, only 16% (4.63 million/29.69 million) of Amazon’s used-book sales directly cannibalize newbook sales. The remaining 84% of used-book sales apparently would not have occurred at the new-book prices on Amazon’s site. Using our figures above, these additional 25.06 million used-book sales add approximately \$76.18 million to Amazon’s profitability (25.06 million <sub>∗</sub> \$3.04/used sale). Thus, on balance, the presence of Amazon’s used-book market added \$65.76 million to the company’s profitability.<sup>23</sup>

6.3.3. Consumer Surplus. To calculate the consumer surplus gain from the introduction of Amazon’s used-book markets, we apply the methodology of Hausman and Leonard (2002) with respect to the consumer surplus gain from the introduction of new goods. Prior research has shown that income elasticity can be ignored for consumer products that represent a small proportion of overall consumer expenditures (e.g., Brynjolfsson 1995 in the context of computer purchases, Hausman 1997a in the context of telecommunications services, and Brynjolfsson et al. 2003 in the context of Internet book sales). Ignoring income elasticity, the consumer surplus gain from the introduction of the used-book market at Amazon.com should be given by<sup>24</sup>

$$
C V = - \frac {p _ {u} q _ {u}}{(1 + \eta_ {u})},\tag{15}
$$

where $p _ { u }$ is the average price of used book sold, $q _ { u }$ is the number of used books sold, and $\eta _ { u }$ is the ownprice elasticity of used-book demand.

Given the used-book own-price elasticity of 487, the average sale price of used books (\$8.76), and the quantity of used books sold (29.69 million), we estimate that the consumer surplus gain from the introduction of Amazon.com’s used-book market is \$67.21 million.

## 7. Discussion

While many papers in the IT, economics, and marketing literatures have analyzed the characteristics of new books sold in electronic markets (e.g., Brynjolfsson and Smith 2000, Clay et al. 2001, Pan et al. 2002, Baye et al. 2004), used books—and other used products—sold in IT-enabled exchanges may have an even larger impact on both electronic and physical markets.

IT-enabled markets for used products are able to aggregate supply and demand over a global marketplace, making it easier for buyers to find sellers and for sellers to find buyers. Because of this, these markets have significant advantages in terms of price, search costs, and selection over physical markets. As noted above, while Amazon’s used-book marketplace features at least one used book for almost every book in print and many out-of-print books, a typical physical used-book store carries only between 5,000 to 30,000 unique titles. Likewise, prices of used books sold on the Internet are 38%–75% lower than comparable prices in physical stores.<sup>25</sup> Because of these advantages, the Internet makes up an estimated 67% of all used-book sales (Wyatt 2005), versus only 12.7% of new-book sales in the same channel (Rappaport 2004).

The question remains: How will these IT-enabled exchanges impact new-product sales and resulting social welfare? The increased viability of usedproduct sales in electronic markets may pose a significant threat for many categories of information goods—such as books, music, and movies—where there is relatively little degradation in the quality of the good over time, and where artists and publishers are only compensated for the initial sale of the product. In these product categories, the increased variety, low prices, and low search costs available in online used-product markets may attract customers who would have otherwise purchased a new copy of the product. If cannibalization of new-product sales were to become widespread, it could undermine the profitability of the publishing business and reduce authors’ and artists’ creative incentives. Because of this, the Association of American Publishers and the Authors’ Guild have asked Amazon to create artificial search costs for new-book shoppers to locate used-book copies by separating the two markets on Amazon’s site.

In this research, we analyze the impact of usedbook markets on new-book sales at Amazon.com. Using a unique data set, we find that the cross-price elasticity of new-book sales with respect to usedbook prices is rather low (0.088). This means that only 16% of Amazon’s used-book sales directly cannibalize new-book purchases; the remaining 84% of sales represent purchases that otherwise would not have occurred at new-book prices. Thus, while cannibalized sales result in an estimated \$45.05 million loss to publishers annually, the total welfare gain to society from this IT-enabled market is \$87.92 million annually after considering the \$65.76 million gain in Amazon.com’s gross profits and the \$67.21 million gain in consumer surplus.

The implication of this finding for publishers is that, at least at present, used books do not appear to be a strong substitute for new-book purchases for most consumers. Further, any lost publisher revenue from these used markets must be viewed in the context of the many ways the Internet has helped to increase new-book sales: by lowering retail prices (while holding wholesale prices constant) (Brynjolfsson and Smith 2000), increasing product variety (Brynjolfsson et al. 2003), and providing a sales channel to customers who do not have local access to large bookstores (Brynjolfsson and Smith 2000). Finally, it is significant to note that the estimated \$45.05 million loss in annual gross profits represents only 0.3% of total publisher gross profits.

For authors, while the observed levels cannibalization will lead to somewhat lower royalty payments, authors may experience an additional, indirect gain through additional readership from the 84% of usedbook sales that otherwise would not have occurred. For example, authors may accrue some added income from these additional readers through speaking fees, licensing deals, or advances on future books. These new readers may also buy new versions of subsequent releases by the same author(s). Further, usedbook markets could spur new-book sales due to an increase in valuation from the possibility of resale (Ghose et al. 2005).

However, book publishers, and producers of other comparable information goods, should remain attentive to potential changes in customer sensitivity toward used products. In the book category, customer sensitivity to used books may change over time as customers gain comfort with the quality and reliability of products sold in used markets. Likewise, producers of products with a stronger digital component than books should analyze the impact of cannibalization by used products. We speculate that cannibalization may be particularly acute for digital products, such as CDs and DVDs. Higher cannibalization levels might arise on the demand side because digital content typically does not degrade from use, reducing the importance of quality differentiation. On the supply side, most digital content (including CDs and DVDs) can be easily copied (and thus effectively retained) before they are resold, potentially making them more likely to be introduced for resale by (unscrupulous) sellers. In this regard, we believe that another key contribution of our work is in providing an easily executed methodology for product sellers and academic researchers to analyze the impact of cannibalization in other product categories.

It is also important to note that while cannibalization can reduce revenue to publishers and content creators, information technology can also provide new tools for controlling or eliminating used-product markets. For example, licensing restrictions can prohibit the resale of some products purchased digitally (e.g., eBooks and music purchased through online music stores) and can create rental markets under more direct industry control (e.g., the older Divx and more recent Flexplay movie formats). Issues surrounding the viability and effectiveness of technology-enabled control over used-product markets would make an important area for future research.

Finally, there are several limitations of our study deserving mention. First, our data come from a single retailer. Future research could include data from other used-book sellers such as ABEbooks or Half.com. Second, our study focused only on used books. Future studies may wish to look at other similar product categories, such as CDs and DVDs. Finally, our study represents only a snapshot in the evolution of the online used-book marketplace. Consumer sensitivity may change over time as consumers gain more familiarity with used products sold through online markets.

## Acknowledgments

The authors thank Al Greco, Paul Kattuman, Otto Koppius, Hank Lucas, Ivan Png, Susan Siegel, Hal Varian, Bruce Weber, Andy Whinston, and participants at the 2005 International Industrial Organization Conference, the 2004 International Conference on Information Systems, the 2004

INFORMS Annual Conference, the 2004 MISRC/CRITO Symposium on the Digital Divide, Michigan State University, Ohio State University’s Fisher School of Business, the 2003 International Conference on Information Systems, Indiana University’s Kelley School of Business, the University of California at Davis, the New York University’s Stern School of Business, and the Tepper School of Business and H. John Heinz School of Public Policy and Management at Carnegie Mellon University for valuable comments on this research. The authors thank representatives of the Book Industry Study Group, MIT Press, Prentice Hall Publishing, and various other publishers for providing valuable information on the book industry. They also thank David Dewey, Samita Dhanasobhon, Steve Gee, Stoyan Arabadjiyski, Sumiko Hossain, Jae Hong Park, Nat Luengnaruemitchai, and Sriram Gollapalli for outstanding research assistance. Michael Smith acknowledges the generous financial support of the National Science Foundation through CAREER Award IIS-0448516.

## Appendix

Recall the consumer utility functions in §3.2. By equating (i), (ii) and (ii), (iii), we derive the two indifference points $\theta _ { 1 } =$ $( P _ { N } - ( 1 + \alpha ( 1 - k ) ) P _ { U } ) / ( 1 - q )$ and $\theta _ { 2 } = P _ { U } / q$ , which define the consumer market segments. By equating the demand of used goods $\left( \theta _ { 1 } - \theta _ { 2 } \right)$ with the supply of used goods $\alpha ( 1 - \theta _ { 1 } )$ we get the market-clearing used-good price,

$$
P _ {U} = \frac {q (P _ {N} ^ {U} (1 + \alpha) - \alpha (1 - q))}{1 - \alpha q (k (1 + \alpha) - \alpha - 2)}.
$$

The retailer’s profit is then

$$
\pi_ {R} = (1 - \theta_ {1}) (P _ {N} ^ {U} - w ^ {U}) + (\theta_ {1} - \theta_ {2}) k P _ {U}.
$$

Substituting $P _ { U }$ in the retailer’s profit equation and optimizing with respect to $P _ { N } ,$ , we get the optimal new-good price,

$$
\begin{array}{l} P _ {N} = \big ((1 + w ^ {U}) (1 + \alpha q (\alpha - k)) \\ \qquad + \alpha q \big [ 3 + \alpha^ {2} q (1 - k) + 2 w ^ {U} + \alpha (2 q - k (2 q + w ^ {U} - 1)) \big ] \big) \\ \cdot (2 + (6 + 4 \alpha) q) ^ {- 1} \end{array}
$$

and the used-good price

$$
P _ {U} = \frac {q ((1 + \alpha (1 - k) + k) q + w ^ {U})}{1 + (1 + 2 \alpha (1 - k) + 2 k) q}.
$$

These expressions enable us to derive the relevant profits expressions for publisher and retailer as follows:

$$
\pi_ {S} ^ {U} = (1 - \theta_ {1}) w = \frac {1}{2} \frac {(1 + \alpha q - w ^ {U}) w ^ {U}}{(1 + \alpha q (2 + \alpha))}
$$

and

$$
\pi_ {R} ^ {U} = \frac {1}{4} \frac {(1 + \alpha q - w ^ {U}) ^ {2}}{(1 + \alpha q (2 + \alpha))}.
$$

The publisher can optimize its profit with respect to $w ^ { U }$ and can set $w ^ { U } = ( 1 / \stackrel {  } { 2 } ) ( 1 + \alpha q )$ . Without the used-book market, the publisher makes a profit of $\pi _ { S } = ( w ( 1 - w ) ) / 2$ and the retailer makes a profit of $\pi _ { R } = ( 1 - w ) ^ { 2 } / 4$ . Comparing these respective profits, it is easy to see that $\pi _ { S } ^ { U } - \pi _ { S } \bar { < } 0$ for all values of $w ^ { U } ,$  and q and w is set at optimal $w = 1 / 2$ On the other hand, $\pi _ { R } ^ { U } - \pi _ { R } > 0$ for all $\overline { { { w } } } ^ { U } < 1 + \alpha q -$ $( 1 / 2 ) \sqrt { 1 + \alpha ( 2 + \alpha ) q }$ . Thus, as long as the publisher does not increase its wholesale price, the retailer always benefits and the publisher always loses. Note that for simplicity we do not consider changes in retailer and wholesale prices across time. The various effects of the secondary market we have identified for publisher and retailer will still persist even if we solved for first period retail and wholesale prices separately.

## References

Anderson, S., V. Ginsburgh. 1994. Price discrimination by second hand markets. Eur. Econom. Rev. 38 23–44.

Bakos, J. Y. 1997. Reducing buyer search costs: Implications for electronic marketplaces. Management Sci. 43(12) 1613–1630.

Bapna, R., W. Gank, G. Shmueli. 2005. Consumer surplus in online auctions. Working paper, University of Connecticut, Storrs, CT.

Baye, M. R., J. Morgan, P. Scholten. 2004. Price dispersion in the small and in the large: Evidence from an Internet price comparison site. J. Indust. Econom. 52(4) 463–496.

Ben-Akiva, M., S. Lerman. 1985. Discrete Choice Analysis: Theory and Application to Travel Demand. The MIT Press, Cambridge, MA.

Benjamin, D., R. Kormendi. 1974. The interrelationship between the markets for used and new durable goods. J. Law Econom. 17 381–401.

Bond, E., L. Samuelson. 1984. Durable good monopolies with rational expectations and replacement sales. RAND J. Econom. 15(3) 336–345.

Book Industry Study Group. 2004. Book Industry Trends. New York.

Brynjolfsson, E. 1995. The contribution of information technology to consumer welfare. Inform. Systems Res. 7(3) 281–300.

Brynjolfsson, E., M. Smith. 2000. Frictionless commerce? A comparison of Internet and conventional retailers. Management Sci. 46 563–585.

Brynjolfsson, E., Astrid A. Dick, Michael D. Smith. 2004. Search and product differentiation at an Internet shopbot. Working paper, Carnegie Mellon University, Pittsburgh, PA.

Brynjolfsson, E., Y. Hu, M. Smith. 2003. Consumer surplus in the digital economy: Estimating the value of increased product variety. Management Sci. 49(11) 1580–1596.

Bulow, J. 1982. Durable-goods monopolist. J. Political Econom. 90(2) 314–322.

Chevalier, J., A. Goolsbee. 2003. Measuring prices and price competition online: Amazon and Barnes and Noble. Quant. Marketing Econom. 1(2) 203–222.

Chevalier, J., A. Goolsbee. 2005. Are durable goods consumers forward looking? Evidence from college textbooks. Working paper, Yale School of Management, New Haven, CT.

Clay, K., R. Krishnan, E. Wolff. 2001. Price strategies on the Web: Evidence from the online book industry. J. Indust. Econom. 49(4) 521–540.

Coase, R. 1972. Durability and monopoly. J. Law Econom. 15 143–149.

Ellison, G., S. Ellison. 2004. Search, obfuscation, and price elasticities on the Internet. Working paper, Massachusetts Institute of Technology, Cambridge, MA.

Ghose, A., R. Telang, R. Krishnan. 2005. Effect of electronic secondary markets on supply chain. J. Management Inform. Systems 22(2) 91–120.

Greco, A. 2005. The Book Publishing Industry. Lawrence Erlbaum Associates, Mahwah, NJ.

Greco, A., R. M. Wharton, H. Estalemi. 2005. The changing market for university press books in the United States. J. Scholarly Publishing 36(4) 187–220.

Guadagni, P., J. Little. 1983. A logit model of brand choice calibrated on scanner data. Marketing Sci. 2(3) 203–238.

Hausman, J. A. 1997a. Valuing the effect of regulation on new services in telecommunications. Brookings Papers on Economic Activity: Microeconomics 1997 1–38.

Hausman, J. A. 1997b. Valuation of new goods under perfect and imperfect competition. Timothy F. Bresnahan, Robert J. Gordon, eds. The Economics of New Goods. The University of Chicago Press, Chicago, IL, 209–237.

Hausman, J. A., G. Leonard. 2002. The competitive effects of a new product introduction: A case study. J. Indust. Econom. 50(3) 237–263.

Hendel, I., A. Lizzeri. 1999. Interfering with secondary markets. RAND J. Econom. 30(1) 1–21.

Hicks, J. R. 1942. Consumers’ surplus and index numbers. Rev. Econom. Stud. 9(2) 126–137.

Liebowitz, S. J. 1982. Durability, market structure and new-used goods models. Amer. Econom. Rev. 72(9) 816–824.

Malone, Thomas, JoAnne Yates, Robert Benjamin. 1987. Electronic markets and electronic hierarchies. Comm. ACM 30(6) 484–497.

Miller, L. H. 1974. On killing off the market for used textbooks

and the relationship between markets for new and secondhand goods. J. Political Econom. 82(3) 612–619.

Milliot, J. 2002. Amazon focused on unit growth. Publishers Weekly 249(44) 15.

Pan, X., V. Shankar, B. Ratchford. 2002. Price competition between pure play versus bricks-and-clicks e-tailers: Analytical model and empirical analysis. Adv. Appl. Microeconom. 11 29–61.

Poynter, D. 2000. Publishing Poynters (April–June) Accessed March 21, 2005. http://parapub.com/getpage.scfm?file newsletter/ News0400.html.

Publishing Trends. 2004. Used blues: Used books become newer everyday, to many publishers dismay. Publishing Trends Newsletter 11(7) 1–7.

Rappaport, B. 2004. Ipsos BookTrends 2004. Ipsos-Insight, Chicago, IL.

Siegel, S., D. Siegel. 2004. A Portrait of the U.S. Used Book Market. Book Hunter Press, Yorktown Heights, NY.

Smith, Michael, Erik Brynjolfsson. 2001. Customer decision making at an Internet shopbot: Brand still matters. J. Indust. Econom. 49(4) 541–558.

Swan, P. L. 1980. Alcoa: The influence of recycling on monopoly power. J. Political Econom. 88(1) 76–99.

Tedeschi, B. 2004. Online battle of low-cost books. New York Times (July 12) C5.

Waldman, M. 1997. Eliminating the market for secondhand goods: An alternative explanation for leasing. J. Law Econom. 40(1) 61–92.

Weingarten, Gene. 2001. Below the beltway. Washington Post Magazine (June 17) W.03.

Wingfield, N. 2003. New chapter: In latest strategy shift, Amazon is offering a home to retailers. The Wall Street Journal (September 24) A1.

Wyatt, Edward. 2005. Internet grows as a factor in used-book business. New York Times (September 29) 4.
