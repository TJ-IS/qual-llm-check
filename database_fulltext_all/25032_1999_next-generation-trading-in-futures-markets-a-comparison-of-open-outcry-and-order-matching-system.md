---
otero_id: 25032
otero_key: "JXW2US7Y"
title: "Next-Generation Trading in Futures Markets: A Comparison of Open Outcry and Order Matching Systems"
authors: "Bruce W. Weber"
year: "1999"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1999.11518244"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Next-Generation Trading in Futures Markets: A Comparison of Open Outcry and Order Matching Systems

Bruce W. Weber

To cite this article: Bruce W. Weber (1999) Next-Generation Trading in Futures Markets: A Comparison of Open Outcry and Order Matching Systems, Journal of Management Information Systems, 16:2, 29-45, DOI: 10.1080/07421222.1999.11518244

To link to this article: http://dx.doi.org/10.1080/07421222.1999.11518244

![](/api/attachments/JXW2US7Y/fulltext/images/ff73b0ca7f7899222f77d1225d9322532259c801fb34b31d178ea77334bf14d1.jpg)

Published online: 02 Dec 2015.

![](/api/attachments/JXW2US7Y/fulltext/images/5aacac6b787e13ed8ace67ca7e0e1bd4712abf5742dfafae8fd34124fa074ce5.jpg)

Submit your article to this journal ↗

![](/api/attachments/JXW2US7Y/fulltext/images/bed512cd2f7f0caeaac740a7b64ba713fdeb7b819b88566aad5a6d8b9fa93fe8.jpg)

Article views: 1

![](/api/attachments/JXW2US7Y/fulltext/images/e1dfba6317e63c7d38e4a4743023328fff2a9960e803af18f6f351551b12aaf4.jpg)

View related articles ↗

# Next-Generation Trading in Futures Markets: A Comparison of Open Outcry and Order Matching Systems

BRUCE W. WEBER

BRUCE W. WEBER: See the Guest Editors' introduction for biographical information.

ABSTRACT: The introduction of new screen-based systems for trading securities and futures contracts has led to the emergence of a “market for markets,” and exchanges, broker-dealer firms, and market data vendors are competing to offer trade execution services that will attract customers and trading volumes. This competition is favored in the United States by regulatory bodies such as the SEC and the CFTC, which have taken steps such as encouraging the listing of equity options on multiple exchanges and approving the applications of screen-based systems for designation as contract markets. This paper examines the design of one screen-based futures market, the Cantor Financial Futures Exchange (CX), and describes its capabilities relative to the rival, floor-based market in Chicago. In comparison to traditional open-outcry mechanisms, the CX order-matching system maintains strict first-in-first out time priority among submitted orders. Using a simple simulation model, we see that order matching leads to faster completion of desired trades and about a one-third reduction in transactions costs.

KEY WORDS AND PHRASES: electronic futures trading, screen-based trading, trading automation.

THIS PAPER COMPARES "OPEN OUTCRY," AN ESTABLISHED AND WIDELY USED method for trading futures contracts on a market or exchange floor with a screen-based alternative, electronic "order matching." In a number of markets today, automation reliably handles trading functions, including order routing, quote display, price determination, and trade execution. And yet, research into the relative merits of alternative market structures has not yielded a conclusive answer to the question, What trading mechanism maximizes participants' satisfaction and minimizes transactions costs? Today, floor markets and screen-based markets, with different trading mechanisms, coexist and both operate and provide good levels of liquidity to participants [9, 11].

Studies have shown that well-designed trading automation can be valuable to investors and traders in markets $[4, 5, 12]$ . For example, the introduction of the SEAQ screen-based market system as part of the London Stock Exchange's 1986 Big Bang market reforms improved the quality of the LSE market $[3]$ and played a part in increasing trading volumes from \$280 million a day in 1985 to \$4.1 billion a day in 1994. In the same period, bid-ask spreads (an important trading cost) for FTSE 100 stocks fell from 1.0 percent to 0.8 percent, and commissions shrank from 0.33 percent to 0.17 percent. Thus, the cost of a round-trip investment (purchase and subsequent sale) fell to 1.14 percent (= 0.8 percent + 2 × 0.17 percent) from 1.66 percent. Comparing SEAQ to the floor, London's electronic market proved to be more open and competitive than the floor market and led to lower transactions costs for investors. Similarly, the introduction of the Nasdaq screen market in 1971 to replace the OTC "pink sheets" led to a reduction of the average bid-ask spread in a 174-stock sample to 40.3 cents from 48.7 cents [8]. The best explanation for the reduction in trading costs from SEAQ and Nasdaq is that market makers' quotes were made visible on a computer terminal, which forced dealers to compete by posting more aggressive bid and offer quotes, thus narrowing the bid-ask spread.

Today, alternative venues and market mechanisms exist for the trading of U.S. Treasury securities futures contracts. $^{1}$ From the introduction of Treasury futures in 1977 until 1998, trading occurred exclusively in an open-outcry market structure on the floor of the Chicago Board of Trade (CBOT). A competing market, the Cantor Financial Futures Exchange (CX), opened in 1998 and provides screen-based order matching with two distinctive innovations compared with open-outcry markets: (1) first in–first out (FIFO) time priority among orders at a particular price, and (2) a “clearing time” period and “exclusive time” period for the providers of the best bid and ask quotes in the market. $^{2}$ The significance of this market, and the presence of alternative trading venues with very different trading mechanisms, highlights the importance of careful study of the impact of trading alternatives.

This paper describes developments in electronic markets for futures trading and then details a model of order arrival and trading that will be used to compare open-outcry trading with a FIFO-based order-matching alternative. It is found that the use of an order book, imposing time and price priority, does indeed improve market quality and customer satisfaction, and does indeed reduce trading costs for investors. Moreover, as explored in a later section, these results hold true even under the most conservative of assumptions concerning the behavior of market participants after the introduction of electronic alternatives.

## Environment for the Electronic Futures Trading

MORE SOPHISTICATED STRATEGIES AND INVESTORS' DESIRE for more direct market access and greater control over trading are leading to growing interest in screen-based trading systems [10]. In Europe, futures trading has moved rapidly to screen-based markets (see Table 1). The rise of these screen-based markets, and the erosion of activity in Europe's open-outcry floor markets surprised many observers.

While a number of factors may have contributed to the success of these screen-based markets, one contributing factor may be the attractiveness of their order-matching trading mechanisms relative to the open-outcry markets they displaced. In order matching, limit orders $^{3}$ placed by market participants can be maintained in time priority, unlike open outcry, in which shouted orders that are tied at the same price are eligible for execution.

Table 1. Recent Developments in Screen-Based Futures Trading in Europe

<table><tr><td>Market</td><td>Recent developments</td></tr><tr><td>Marche à Terme International de France (Matif) Paris-based futures market opened in 1985.</td><td>On June 2, 1998, less than two months after the April 8, 1998 introduction of its Nouveau Systeme de Coation-Version Future (NSC-VF) system, floor trading was ended for Matif&#x27;s interest rate futures contracts.Matif had planned for a longer period of parallel operations of its open-outcry pit market and NSC-VF. In 1997,after-hourstrading of Matif contracts on the Globex system accounted for just 9 percent of the exchange&#x27;s total volumes.In the days after the NSC&#x27;s launch, however, floor trading fell to 30 percent of the total. After a month, pit trading had dwindled to 10 percent, down from over 90 percent, and the population of floor traders fell from 400 to 100.Later in 1998, floor trading ended in options and physical commodities futures, and was moved to electronic trading exclusively.</td></tr><tr><td>Deutsche Terminbörse (DTB) screen-based futures market of the Frankfurt-headquartered Deutsche Börse. Opened January 26, 1990. Re-named Eurex in 1998.</td><td>From 1991 to 1997, over 70percentof trading volume in the German government 10-year bond future (Bund) occurred on the floor of the London International Financial Futures Exchange (LIFFE). The other 20–30 percent took place on the DTB.In 1997, the Bund was the world&#x27;s third most actively traded futures contract, after the U.S. T-Bond (CBOT) and the 3-month Eurodollar contracts (CME).In the first quarter of 1998, trading volumes on the Deutsche Terminbörse (DTB), the screen-based market of the Frankfurt-headquartered Deutsche Börse began to exceed the LIFFE&#x27;s volumes for the first time.In April 1998, the DTB had a 70 percent share of trading in the Bund, and the DTB&#x27;s share reached 82% on Wednesday April 22, when it traded 430,187 Bund contracts.The period of competition between the LIFFE and DTB markets led to reductions in exchange trading fees per contract to about $0.45 on LIFFE and to about $0.25 on the DTB.</td></tr></table>

Sources: "Frankfurt Exchange Overtakes LIFFE," Financial Times (June 3, 1998), p. 17; "DTB Bund Volumes Overtake Chicago," Financial News (London) (April 27, 1998), p. 15; "Matif Set to End Open Outcry," Financial Times (May 14, 1998), p. 20; "Matif Brokers Ponder Future," Futures (June 1998), pp. 14–16.

To assess order-matching markets, and the implications of their broader adoption for traders, we examine the U.S. Treasury futures market, which has the greatest trading volume of any futures market worldwide. With a model of order arrival and trading, market quality under open-outcry rules is compared with order-matching rules.

## The U.S. Treasury Futures Market: Current Order Handling and the Potential for Screen-Based Trading

THE U.S. TREASURY SECURITIES MARKET IS THE WORLD'S LARGEST fixed-income securities market and is one of the largest and most sophisticated financial markets. The U.S. Treasury debt outstanding was \$5.4 trillion as of fourth quarter 1997. The treasury market is intended to facilitate the distribution of the U.S. national debt through as efficient a mechanism as possible. Treasury securities are issued in regularly scheduled auctions. Participating directly in the auctions are about thirty-six primary dealers who bid for securities in monthly and quarterly refinancings. There can be as many as 156 separate auctions per year, and recently about \$2 trillion in Treasury securities have been auctioned per year [1]. After issuance, Treasury securities trade in an active cash or secondary market. Investors hold treasury securities because of their high credit quality and because of the market's vast liquidity [6].

## The Treasury Futures Market

Derivatives of treasury securities are actively traded. In May 1999, the Chicago Board of Trade (CBOT) traded 9.6 million Treasury bond futures contracts, making it the most active futures contract in the world. T-Bond futures accounted for over 39 percent of the total 24.5 million futures and options contracts traded in May 1999 at the CBOT. The value of Treasury futures contracts traded on an average day is about \$60 billion and represents about 40 percent of cash market volume.

U.S. Treasury bond and note futures are widely used by a number of different groups to transfer risk and to manage the risks of holding Treasury and other fixed-income securities. For instance, firms that originate mortgages (i.e., lend at fixed rates to home buyers) will hold and trade futures contracts to hedge the interest-rate risk of their mortgage positions. Other common uses of futures on treasury securities in investment management are [2]:

\- Lock in a purchase price: If an investment manager anticipates positive cash inflows that will be used to purchase fixed-income securities in the future and is concerned about the possibility of higher prices, he or she can buy Treasury futures with delivery months near the time of the anticipated cash flows. This establishes a maximum purchase price.

\- Safeguard investment value: By selling Treasury futures, an investment manager can lock in attractive selling prices and preserve the value of a portfolio or a security against possible price falls.

\- Cross-hedge: U.S. Treasury securities prices and yields are the benchmark against which most other fixed-income instruments are compared. Treasury futures can be used to control risk and enhance the returns from non-U.S. government securities. For instance, an investment-grade corporate bond maturing in 10 years could have its yield quoted as 85 basis points over the benchmark Treasury security, which in this case is the 10-year treasury note. As a result of its benchmark characteristics, Treasury futures are useful risk-management tools for corporate bonds, mortgage-backed securities, agency securities, Eurobonds, non-U.S. government and private-sector bonds, and other fixed-income instruments.

\- Enhance returns: Treasury futures are used to increase exposure to changing rates, allowing investors to profit from anticipated interest-rate moves and to enhance overall returns.

\- Fine-tune positions: Treasury futures are used to adjust positions or to fine-tune risk-management strategies. By buying or selling futures, a fund manager can lengthen or reduce the duration of a portfolio, thereby increasing or decreasing sensitivity to interest-rate changes.

\- Profit from shifts in the yield curve: Investors can construct trades based on the differences in interest-rate movements at different points on the yield curve. For instance, an investor that expects the yield curve to steepen, making short maturity instruments gain in value relative to long dated instruments, can sell bond futures and buy two-year-note futures contracts.

These strategies are beneficial because they give investors a chance to customize the risk and return characteristics of their portfolio and to adjust positions quickly to reflect their outlook on interest rates and the market.

## Current Open-Outcry Practices

To trade most futures contracts, including Treasury security futures, a market participant must have an account with a broker or Futures Commission Merchant (FCM). As figure 1 indicates, the FCM receiving the customer's order will phone a floor broker with a booth on the appropriate futures exchange. The clerk will write down the order and time-stamp it, and then either pass the order ticket to a runner who will deliver it to the firm's trader in the pit or flash it to the trader using hand signals. Once the order is executed in the pit, information on the filled order is sent back to the booth and relayed to the customer. The process may take from several seconds to several minutes, depending on the complexity of the order and the level of activity in the pit [10].

In recent years, the major futures markets have installed order-routing systems to deliver orders electronically to the FCM booth or to the trading pit. Two systems, TOPS and COMET, are used in the CBOT markets. While such systems eliminate paperwork and speed the transmission of information, they essentially automate existing practices. TOPS transmits the customer's order in electronic form from a remote trading desk to the FCM's booth, or, if it is for 10 contracts or less, directly to an "electronic clerk" (EC) terminal in the trading pit. COMET terminals are in place in most FCM booths and are used to direct orders received over the telephone to an EC terminal in the appropriate pit. Once an order arrives at the EC terminal, it is routed to the appropriate trader, who fills the order and sends the fill information back to the FCM booth and the customer. In addition, several floor-based markets have screen-based systems for after-hours trading. These systems and their sponsors include:

![](/api/attachments/JXW2US7Y/fulltext/images/18444bd81a365c4348bba4f5f2fc6a59a3f58cce14d141be1f8afe8231e53920.jpg)  
Figure 1. Open-Outcry Market Flows  
A customer's order is phoned to the booth of the Future Commission Merchant (FCM) along the wall of the market floor. The instructions are written on an order ticket and then either flashed with hand signals to a broker with the FCM firm or a runner delivers a ticket to the broker in the pit.

Project A (CBOT), Globex (Chicago Mercantile Exchange), and Access (New York Mercantile Exchange). All are screen-based mechanisms for trading derivatives contracts after normal trading hours. To date, few exchanges have run trading systems in direct competition during the open hours of their floor markets.

## Electronic Trading: The CX Example

In electronic futures markets, participants also have accounts with a broker or a clearing bank, who backs their trades financially. Instead of relaying information through the broker floor staff, the investor can monitor quoted prices on a screen and can enter buy or sell orders directly into the market $[7]$ . In the CX market, there are two ways participants can access the market (see figure 2): They can directly enter their own orders via their workstation keyboard or they can phone a CX “terminal operator” (TO), who inputs orders into the system and can rapidly modify customer orders. The TO provides a clerical function, exercises no trading discretion, and does not accept “not held orders.”

The CX trading system is designed to provide a competitive market and to handle peak trading volumes efficiently. The CX currently does not maintain an order book or a “deck.” The CX screen simply shows the best bid and best offer quotes with their size. Bids or offers are deleted from the screen after a better-priced order arrives. For example, bids to buy at 115 are deleted when a better bid of $115\frac{1}{32}$ or greater arrives. In some markets, these less competitive bids and offers are retained in an order book that may be visible to the market. Quoted sizes on the CX screen could be the aggregate of several orders at that price, or a single order.

The Cantor Exchange was developed and is operated by Cantor Fitzgerald, the leading interdealer broker in the U.S. Treasury market. The CX is owned by the New York Board of Trade (NYBOT) and its members. The NYBOT is responsible for self-regulatory oversight and clearing of all trades executed on CX.

Compared with open-outcry markets, the CX imposes different pricing and trade-allocation priorities, which are intended to create incentives to provide liquidity and place orders at attractive prices. The CX screen displays orders anonymously, showing bids and offers with size, and the last trade price, but no information about the

<table><tr><td rowspan="3">Authorized Traderor Customer viaFCM</td><td rowspan="3">Phone (or)direct access</td><td rowspan="2">CX T.O.</td><td rowspan="2">CX TradingScreen</td><td rowspan="2">T.O.</td><td>Other customers</td></tr><tr><td rowspan="2">Proprietary traders</td></tr><tr><td colspan="3">Trade details for clearing</td></tr><tr><td>Clearing member</td><td colspan="5">NYBOTCC (Clearinghouse)</td></tr></table>

Figure 2. CX Market Flows

A customer's order is phoned to a CX terminal operator and displayed on a trading screen for other market participants to react to and trade with. Because traders on the CX enter orders in the market directly or through a TO, a layer of interaction and information transmission that occurs on the floor is eliminated.

Table 2. Comparison of Market Characteristics and Traded Contracts on CBOT and CX

<table><tr><td>CBOT</td><td>CX</td></tr><tr><td>65,000 sq. ft. floor opened February 1997 at cost of $182 million. Holds 8,000 people. Formed as an agricultural products market in 1848.</td><td>Screen-based, interactive matching market opened in September 1998.</td></tr><tr><td>Users contact floor brokers directly or indirectly through an FCM. Floor broker transmits order into trading pit for execution.</td><td>Users enter orders directly or contact TOs, who enter their orders for immediate display or execution. The step of moving the order into the trading pit is eliminated.</td></tr><tr><td>Prices determined by open outcry in designated trading pits.</td><td>Price determined electronically on screen using an order-matching algorithm.</td></tr><tr><td>Price data available to the public immediately after trade. Indicative price quotes available from service providers.</td><td>Firm bid and offer quotes with size shown on screen. Trade price and quantity information provided live at the time of execution.</td></tr><tr><td>Contract delivery months: March, June, September, December</td><td>Contract delivery months: March, June, September, December</td></tr><tr><td>Trading hours: 7:20 A.M. -2:00 P.M., Chicago time</td><td>Trading hours: 7:30 A.M.-5:30 P.M., New York time</td></tr><tr><td colspan="2">Other differences between the CX market and open outcry markets: Anonymity: The source of an order may be revealed or inferred in an open-outcry trading pit. The identify of a CX order is not revealed during trading and is not revealed during clearing and settlement because the NYBOT clearinghouse steps in and is counterparty to the two sides of each trades. Transparency: The CX will provide firm and executable bid and offer quotes with sizes that are visible to all market participants. Open-outcry markets do not provide the same degree of pretrade transparency.</td></tr></table>

counterparties is displayed. A trade in the system occurs when an order that was entered and displayed is “hit” (sold to) or “lifted” (bought from). The trader that is the “aggressor”—that is, who actively initiates a trade by hitting or lifting a displayed quote—will pay a transaction fee (see Table 2).

## A Simulation Comparison of Open Outcry and Electronic Order Matching

EARLIER WE SAW HOW ELECTRONIC FUTURES TRADING WAS GROWING in importance worldwide. We then looked at the current status of the U.S. Treasury futures market, and at CX, an electronic system for trading treasuries futures contracts. This section develops a simulation model to demonstrate the potential improvements available to these markets from the use of electronic trading systems.

In the CX, and in most electronic order-matching systems, orders are filled according to price and time priority. That is, a market order to sell will be matched with the best (highest price) buy order (bid) that arrived the earliest. Similarly, arriving buy orders execute at the lowest available offer price and are matched with the earliest arriving sell order(s) at that price. In an open-outcry market, sell (buy) orders must be traded at the highest shouted bid (offer) quote, but time priority is not maintained at a particular price level. As a result, any of the traders in a pit that are shouting the same bid or offer quote could fill the next order.

To compare open-outcry and electronic order matching, a simulation model was developed in Crystal Ball 4.0, an Excel spreadsheet add-in. Simulation has provided insights into other market-structure questions, when institutional details precluded obtaining results in closed form [4]. In each run of the simulation, a sequence of 250 buy and sell orders is entered into the market. Orders are either market orders or limit orders. Averaged over 5,000 trial runs of the simulation, the sequence of 250 orders in the model generated 112.5 trades, which reflects about 30 minutes of trading activity during a typical day in the CBOT T-Bond futures market. About 10 percent of the arriving orders are limit orders that ultimately do not execute.

## Modeling Assumptions

Each simulated order in the model has an associated quantity (a uniformly distributed number of contracts from 1 to 50), and a reservation price that is sampled from a lognormal distribution around a simulated equilibrium value for the futures contract. This value, $P^*$ , itself follows a white-noise random walk over the simulation period with the 250 interevent returns i.i.d. $N(0, \sigma^2)$ , where $\sigma^2 = 0.015$ percent. The resulting high-low ranges in the simulation averaged 38 cents, or 0.33 percent of the contract's value, which is consistent with the actual market's ranges during half-hour periods in the trading day. $^4$

The simulated market processes successive orders according to the following logic:

## • A buyer with a reservation price

—that is greater than the current lowest offer price buys using a market order the size of his or her order, or the size of the current offer quote, whichever is less.
—that is less than the current lowest offer will enter that order as a limit order into the market. If the limit price is greater than the current highest bid, a new improved bid is quoted in the market.

![](/api/attachments/JXW2US7Y/fulltext/images/564048648587e88523e528bc86172574bc6375a58a01c42b2461050013ad9dd9.jpg)  
Figure 3. One Simulation Run of 250 Orders, Showing $P^*$ , and the Sell Market Order-Initiated (Sells) Trades and the Buyer-Initiated (Buys) Trades

Notice in the first part of the run that buying orders with higher reservation prices than the current market offer quote depleted the sell orders and led to price increases. In the last part of the run, selling initiated by orders with lower reservation prices drove trading prices down.

—that is at the same price as the bid has an increased quantity available to buy at the bid. If the reservation price is below the current bid, the order is canceled.

\- Similarly, for sellers, their orders will hit the bid if their reservation price is less than or equal to the bid quote, or they will provide an offer quote that could join the current offer quote, or improve on it by offering to sell at a lower price level.

Since reservation prices are distributed around the $P^{*}$ value, buying and selling will lead to market price changes that will keep quote and trade prices in line with $P^{*}$ . Figure 3 shows an example of the evolution of $P^{*}$ and market prices over the course of one simulation run. The price increment in the market is $\frac{1}{32}$ of a point, as is used in the actual Treasury market. The initial price is 115, which reflects the approximate current price levels of Treasury bond futures contracts.

The distinction in order handling across the two markets is that the electronic order-matching system holds the orders in time priority, and in the simulation of the open-outcry mechanism, when several orders are tied at the same bid or offer quote price, the simulation randomly assigns which of the orders will execute the next trade. This distinction could lead to different order-placement strategies, but, for now, we will hold constant the background conditions in the simulated market and examine the impact of the order-matching mechanism on an individual market participant. (The decision to hold order-placement strategy constant is the most conservative strategy available; that is, if the use of the order book improves market quality for investors even without changes or adaptation in their behavior, it would be reasonable to assume that after learning and adaptation these benefits would only increase.)

## Model of an Individual Trading Strategy with Measurable Trading Costs

To compare trading costs, we model a hypothetical trader who seeks to open a long position (buy a futures contract) and later close (sell) it. This is done without loss of generality, and the results would be equivalent if the focal trading strategy were to go short by selling and later cover with a buy order. The approach the modeled trader uses is to place a limit buy order for one contract at the 100th order in the simulation sequence, and close out the position using a sell limit order at the 200th order in the sequence. The buy order is placed to establish a new best bid in the market, and the sell order is placed one price increment better than the offer quote. For example, if the market quote is 115 3/32 bid, the arriving buy order is placed at 115 4/32. If, at the point of the 200th order in the simulation, the ask quote is 115 6/32, the sell order will be placed at 115 5/32.

For both orders, the simulated trader will only wait for the arrival of ten orders, and if his or her limit price was not reached the simulated trader will cancel it and buy or sell with a market order. The advantage of this strategy is that it enables users to “earn” the bid-ask spread when their limit orders execute. However, after a period of ten orders, the user will “pay” the spread and buy or sell with a market order at the time of the 111th or 211th order. The strategy described is realistic and allows for trading costs and limit order execution probabilities to be computed.

Because other processes in the simulation were held constant except for the results achieved by the hypothetical simulated trader, many market measures are the same for both mechanisms. The overall market conditions are shown in Table 3.

The bid-ask spread was about 7 cents or 2.2 ticks (a tick is $\frac{1}{32}$ of \$1), which is consistent with market-quality data from the actual market. The high-low range of prices over the simulation of 250 order arrivals averaged about 38 cents with a standard deviation of 13 cents. This is about 33 basis points ( $0.38/115 = 0.33$ percent) of variation on average in the simulation period. A longer window would lead to a wider price range but would not change the results substantially. Comparisons of the two trading mechanisms are shown in Table 4.

Trading costs (average difference between the buying price and selling price) incurred by the individual trader are 2.3 cents under open-outcry trading and fall to 1.6 cents with order matching. Trading costs are positive because the trader's market orders pay the bid-ask spread, and because the trader's limit orders are subject to adverse selection [7, 11], since he or she is assumed to have no privileged information about $P^*$ .

The trading cost reduction of 33 percent under order matching is mainly due to more of the individual's orders executing as limit orders, 55 percent, compared with the open-outcry market, 45.1 percent. Limit orders that execute reduce trading costs, and the CX's FIFO priority enables the individual's orders to execute before others at the price they established. In the open outcry, random assignment means that a later-arriving order could execute before the individual's buy or sell order.

A second important improvement in the order-matching environment is that traders' limit orders that establish a new best bid or new best ask quote execute more rapidly than in open outcry, where a later-arriving order could be filled first. Under order-matching rules, limit orders that executed were filled after the arrival of 4.2 subsequent orders on average, compared with an average wait for 5.6 orders to arrive for an open-outcry execution. The overall averages were 7.7 orders and 6.5 orders of delay and are somewhat greater due to the market orders used at the time of the eleventh order arriving after the limit order was placed.

Table 3. Overall Market Characteristics (5,000 Simulation Trials)

<table><tr><td>Market means</td><td>Results (same under two market designs) and sample standard deviations</td></tr><tr><td>(Initial price = $115) High</td><td>$115.185 (0.164)</td></tr><tr><td>Low</td><td>$114.810 (0.165)</td></tr><tr><td>Price range</td><td>37.8 cents (13.0)</td></tr><tr><td>Bid-ask spread</td><td>6.84 cents (2.07)</td></tr><tr><td>Number of trades (resulting from 250 orders)</td><td>112.5 (7.3)</td></tr><tr><td>Orders contained in best bid quote and ask quote</td><td>3.20 (0.94)</td></tr><tr><td>Quantity of contracts contained in best bid and ask quotes</td><td>44.4 (13.7)</td></tr></table>

Upon reflection, these results appear reasonable. In particular, if time priority is not maintained, then any limit order at a given price has a greater chance of “bumping up against” the ten-order limit. That is, if time priority is not maintained, then the variance in execution time increases, and, if other traders can trade ahead of a customer’s limit order, this increases the number of limit orders that do not execute within ten trades. This, in turn, increases the number of limit orders that are “canceled” and converted into market orders. This explains the principal simulation results under open-outcry trading:

\- More limit orders are converted to costly market orders.

\- More customer orders pay the bid–ask spread.

\- Fewer customer limit orders are available to provide price improvement to the market.

As a result of a fairly small enhancement, FIFO order matching in an electronic futures market, market users derive substantial benefits. Round-trip trading costs are reduced by 33 percent with order matching, and the delay between placing a limit order and its execution falls by 16 percent.

## Other CX Features

In addition to its FIFO order-matching algorithm, the CX market provides a clearing time period and an exclusive time period for the providers of the best bid and ask quotes in the market. These features also distinguish it from open-outcry trading. The duration of these time periods will be set by the CX to create the appropriate level of incentives to place orders. The more liquid and actively traded the contract, the shorter these time periods are likely to be.

Table 4. Comparisons of Market Quality and Costs (5,000 Simulation Trials)

<table><tr><td>Means for individual trader (buy: order #100–#110, and sell: order #200-#210)</td><td>Open outcry</td><td>Order-matching system</td><td>Difference (std. error)*</td></tr><tr><td>Round-trip trading costs (difference between buying and selling prices)</td><td>2.326 cents</td><td>1.555 cents</td><td>0.771 cents (0.0005)</td></tr><tr><td>Average wait until order filled: limit orders only</td><td>5.56 orders</td><td>4.20 orders</td><td>1.36 (0.029)</td></tr><tr><td>Average wait until order filled: all</td><td>7.67 orders</td><td>6.45 orders</td><td>1.10 (0.025)</td></tr><tr><td>Percentage of orders filled as limit orders</td><td>45.1</td><td>55.0</td><td>9.9 (0.6)</td></tr><tr><td>Percentage of orders converted to market orders</td><td>54.9</td><td>45.0</td><td>9.9 (0.6)</td></tr><tr><td colspan="4">* F-test significant at 0.001 level.</td></tr></table>

\- Clearing time is a period in which the AT (a CX acronym for authorized trader) that placed the first best bid or offer has an exclusive right to respond to a contra offer or bid that has just arrived. During this time, the AT whose bid or offer is showing can trade against the newly arrived contra-side order. If the AT does not respond, then other ATs can trade with the order. For instance, if two bids for 10 contracts each are displayed 120–01, and an order to sell 10 at 120–02 arrives from another AT, then the first of the two bidders has the duration of the clearing time to decide how much, if any, of the 10 contracts he or she wants to buy at 120–02.

\- Exclusive time is given to the AT who placed the first best bid or offer, and whose order was just hit or taken by a contra order. After the AT's order was traded, exclusive time begins and gives the AT the chance to do any additional quantity that the aggressor has to trade. For example, if two bids for 10 contracts each are displayed 120–01, and a sell order for 20 arrives from another AT who is interested in selling an additional 30 (for a total sale of 50), then the first of the two bidders has the duration of the Exclusive Time to decide how much, if any, of the 30 additional contracts he wants to buy at 120–01.

A third time period, “execution time,” is not fixed by the CX but determined by the sequence of orders and trades that occur. During execution time, the price and current volume transacted flash on the screen, indicating that a trade is being “worked up” to a larger quantity. Once the buying interest or selling interest at that price is exhausted, the execution time ends and the price and quantity traded no longer flash.

<table><tr><td colspan="2">Price</td><td colspan="2">Quantity</td></tr><tr><td>BID (buy)</td><td>OFFER (sell)</td><td>BUY (Bids)</td><td>SELL (Offers)</td></tr><tr><td>* 120.01</td><td>—</td><td colspan="2">100 $\times$ </td></tr></table>

Figure 4. A Buy Order Arrives

After trading opens, an authorized trader (AT A) enters a buy order for the September Treasury bond contract by placing a bid at 120 $\frac{1}{32}$ for 100 contracts. On the CX screen, this will be displayed as “120.01.” An asterisk (\*) is placed next to the price to indicate that it is newly arrived. The 120 $\frac{1}{32}$ bid for 100 is the “first best bid” because it was the first posted on the Cantor System and provided the highest bid at the time.

<table><tr><td colspan="2">Price</td><td colspan="2">Quantity</td></tr><tr><td>BID (buy)</td><td>OFFER (sell)</td><td>BUY (Bids)</td><td>SELL (Offers)</td></tr><tr><td>120.01</td><td>120.02*</td><td>100×150</td><td></td></tr></table>

Figure 5. A Sell Order Arrives  
As in figure 4, AT B enters an offer to sell 150 contracts at 120 $\frac{2}{32}$

## Examples of CX Orders and Trades

When an AT enters an order or phones a CX TO, the AT must specify: the code for the customer account or the proprietary order, the contract delivery month, the order type (buy or sell), the quantity, and the price. Figures 4 and 5 illustrate the operation of the CX market system.

After the counterpart offer quote arrives from AT B, “clearing time” begins. During clearing time, AT A, by virtue of having placed the first best bid, is given an exclusive right to respond to the offer quote that just arrived. AT A has several alternatives during clearing time:

1. AT A can do nothing, and the market remains quoted as in figure 5, or any of numbers 2 through 5 below.

2. A can be the “aggressor,” and lift 100 of the 150 contracts offered. A trade of 100 occurs and flashes on the screen as “TAK 100,” indicating that 100 contracts have been “taken” or bought (figure 6). Both ATs fill out tickets, and the TO passes the trade data on for transmission to the CCC, which forwards it via TIPS (Trade Input Processing System, a clearing system used by the NYBOT) to the respective clearing members, who accept or reject it within thirty minutes of posting.

3. Or A can be the aggressor and take the entire offer. The screen will flash the completed trade of 150 contracts at $120\frac{2}{32}$ . The “exclusive time” begins, and A and B have exclusive rights to trade more with each other or with others who wish to buy or sell at $120\frac{2}{32}$ . If both A and B decline to trade any additional quantity, the trade price and size will stop flashing (figure 7).

<table><tr><td colspan="2">Price</td><td colspan="2">Quantity</td></tr><tr><td>BID (buy)</td><td>OFFER (sell)</td><td>BUY (Bids)</td><td>SELL (Offers)</td></tr><tr><td>120.—</td><td>120.02</td><td colspan="2"> $\times$ TAK 100</td></tr><tr><td>BID (buy)</td><td>OFFER (sell)</td><td>BUY (Bids)</td><td>SELL (Offers)</td></tr><tr><td>120.—</td><td>120.02</td><td colspan="2"> $\times$ 50</td></tr></table>

Figure 6.

<table><tr><td colspan="2">Price</td><td colspan="2">Quantity</td></tr><tr><td>BID (buy)</td><td>OFFER (sell)</td><td>BUY (Bids)</td><td>SELL (Offers)</td></tr><tr><td>120.—</td><td>120.02</td><td colspan="2"> $\times$ TAK 150</td></tr></table>

Figure 7.

<table><tr><td colspan="2">Price</td><td colspan="2">Quantity</td></tr><tr><td>BID (buy)</td><td>OFFER (sell)</td><td>BUY (Bids)</td><td>SELL (Offers)</td></tr><tr><td>120.—</td><td>120.02</td><td colspan="2"> $\times$ TAK 250</td></tr></table>

Figure 8.

4. If A wants to buy more, and B wants to sell more, A has the exclusive right to buy more at that price. If B offers to sell another 100 contracts, and A accepts, the screen will appear as in figure 8.

5. If $B$ declines to sell more, then $C$ , another AT who wants to sell, can offer to sell an additional quantity to $A$ .

At any time, except during the execution time, any account may improve upon $A$ 's bid or $B$ 's offer. In that case, the improved quote shows on the screen and the other is automatically removed. For instance, if $C$ offers to sell 100 at $100 \frac{1}{32}$ , then $B$ 's offer will be removed and $A$ has the right to trade with $C$ .

Notice that the trade algorithm did not require the participants initially to display the full size of their orders. Both features, price protection and the ability to restrict the display to a size that will not cause market impact, should improve the quality of the market.

## Conclusions

A NUMBER OF NEW SCREEN-BASED TRADING SYSTEMS FOR DERIVATIVES TRADING such as CX are based on price and time priority matching algorithms. Because the most competitively priced orders in the system are filled first, such systems provide an incentive to place market-improving quotes, which lead to trading-cost advantages and reductions in trading delays compared with current practices. The CX is evidence that a “market for markets” has emerged, which will improve the trading choices available to market participants and the quality of the market.

<table><tr><td>Portfolio decision making →</td><td>Implementation /trading →</td><td>Posttrade processing →</td><td>Position accounting and risk management</td></tr><tr><td>Research, decision support Investment analytics Cash-flow needs Liability matching</td><td>Real-time market data Order handling Trading</td><td>Resolution of out-trades, errors, etc. Clearing Margining: original and variation Settlement and delivery</td><td>Position analysis Risk-adjusted return on capital Value at risk</td></tr></table>

Figure 9. A Simplified Value Chain for Institutional Investors in Fixed-Income Securities Depicting the Activities at Each of Four Stages—Information technology is increasingly used to integrate and streamline the linkages between these activities.

In addition to trading enhancements, screen-based markets provide operational improvements. A value chain for an institutional investor in fixed-income securities is depicted in figure 9.

Traditionally, exchange markets have supported the middle of the value chain, that is, the trading and trade-processing functions. Separate technologies are used by fund managers to support portfolio decision making and to manage risk. Electronic markets, such as Eurex and NSC in Europe, and the CX however, offer the capability of integrating investors' portfolio systems with the placement of orders into the market. And, with an electronic price and clearing feeds, investors can have real-time position accounting in order to manage risks more effectively.

The economic advantages of order matching were analyzed here and shown to be favorable. This can partly explain market users' willingness to adopt a number of screen-based markets that were in competition with established open-outcry market.

For exchange officials, the implications of order matching's benefits and the good response to screen trading by market participants in Europe indicate that:

1. Traders want direct access to the trading and discovery process and benefit from the trading priorities that can be enforced in screen-based markets.

2. Financial markets will move rapidly to "better" venues when there are benefits to an alternative mechanism for trading.

3. Exchanges must compete by reducing costs and trading fees and by implementing rules and systems that meet the needs of investor-customers, even when these changes may erode privileges enjoyed by member-firm intermediaries.

Although trading volumes on the CX in the first months after its September 8, 1998 launch were modest, by April 1999, about 10,000 contracts a day were trading, or about 2 percent of the 450,000 contracts trading a day on the CBOT. As liquidity develops and as the advantages of screen-based mechanisms for trading become more widely recognized, the CX and other screen-based markets will challenge the dominance of many of today's established open-outcry futures markets. Established markets that do not respond with improvements will see trading activity quickly won over by screen-based order-matching rivals.

## NOTES

Acknowledgments: Phil Ginsberg and John Eley of Cantor Fitzgerald provided thorough descriptions of the CX's trading mechanism and its attractions for market participant. Mike Uretsky provided useful comments on an earlier version of the paper. Eric K. Clemons likewise provided useful comments on a later draft.

1. A futures contract is an agreement to purchase or sell a commodity for delivery at a specified time in the future (e.g., December 1999) at a price that is determined at the time of the purchase of the contract in a futures market. In the case of the U.S. T-Bond, it is a contract for \$100,000 face value of 8 percent coupon T-Bonds. Higher interest rates will lead to lower futures prices.

2. A bid is a firm indication of willingness to buy at a stated price. An ask or an offer is a firm indication of willingness to sell at a given price.

3. Participants in a futures market submit buy and sell orders usually through a broker. An order can be a market order, an instruction to buy or sell at the best available price in the market at that moment, or a limit order, which sets a limit price as a upper bound on the most they will pay to buy, or a lower bound on what they will sell for.

4. A section of the CBOT web site, http://www.cbot.com/mplex/quotes/, provides times and sale data that can be used to determine high-low ranges for short intraday trading periods.

## REFERENCES

1. Bartolini, L., and Cottarelli, C. Designing effective auctions for Treasury securities. Current Issues in Economics and Finance (Federal Reserve Bank of New York) (July 1997), 1–6.

2. Bortz, G. Does the treasury bond futures market destabilize the treasury bond cash market? Journal of Futures Markets, 4, 1 (Spring 1984), 14–24.

3. Clemons, E.K., and Weber, B.W. London's big bang: a case study of information technology, competitive impact, and organizational change. Journal of Management Information Systems, 6, 4 (1990), 41–60.

4. Clemons, E.K., and Weber, B.W. Alternative securities trading systems: tests and regulatory implications of the adoption of technology. Information Systems Research (June 1996), 163–188.

5. Domowitz, I., and Steil, B. Automation, trading costs, and the structure of the securities trading industry. Working Paper, Royal Institute of International Affairs, London, February 1998.

6. Fleming, M. The around the clock market for U.S. treasury securities. FRBNY Economic Policy Review (July 1997), 9–32.

7. Grunbichler, A.; Longstaff, F.; and Schwartz, E. Electronic screen trading and the transmission of information: an empirical examination. Journal of Financial Intermediation, 3 (1994), 166–187.

8. Hamilton, J. Marketplace organization and marketability: Nasdaq, the Stock Exchange, and the national market system. Journal of Finance, 33 (March 1978), 487–503.

9. Hamilton, J. Electronic market linkages and the distribution of order flow: the case of

off-board trading of NYSE-listed stocks. In H. Lucas, Jr., and R. Schwartz (eds.), The Challenge of Information Technology for the Securities Markets: Liquidity, Volatility, and Global Trading. Homewood, IL: Dow Jones-Irwin, 1989.

10. Massimb, M., and Phelps, B. Electronic trading, market structure and liquidity. Financial Analysts Journal (January–February 1994), 39–50.

11. Schwartz, R.A. Reshaping the Equities Markets: A Guide for the 1990s. Chicago: Business One Irwin, 1993.

12. Schwartz, R.A., and Weber, B.W. Next-generation securities market systems: an experimental investigation of quote-driven and order-driven trading. Journal of Management Information Systems, 14, 2 (Fall 1997), 57–79.
