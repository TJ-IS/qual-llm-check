---
otero_id: 24910
otero_key: "PSYWYP2H"
title: "Next-Generation Securities Market Systems: An Experimental Investigation of Quote-Driven and Order-Driven Trading"
authors: "Robert A. Schwartz; Bruce W. Weber"
year: "1997"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1997.11518165"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Next-Generation Securities Market Systems: An Experimental Investigation of Quote-Driven and Order-Driven Trading

Robert A. Schwartz & Bruce W. Weber

To cite this article: Robert A. Schwartz & Bruce W. Weber (1997) Next-Generation Securities Market Systems: An Experimental Investigation of Quote-Driven and Order-Driven Trading, Journal of Management Information Systems, 14:2, 57-79, DOI: 10.1080/07421222.1997.11518165

To link to this article: http://dx.doi.org/10.1080/07421222.1997.11518165

![](/api/attachments/PSYWYP2H/fulltext/images/6b7b78daa21a5b0a531abae85214e93ef75740b1ad33a92a14ab8b43d9bb5327.jpg)

Published online: 08 Dec 2015.

![](/api/attachments/PSYWYP2H/fulltext/images/b2df5539c93b79561f212a33e7c47e8a50eea7268f2951dee338709299bea432.jpg)

Submit your article to this journal ↗

![](/api/attachments/PSYWYP2H/fulltext/images/f56881d194a7f17fa8e86adaa1f211255ed0ae1818ef286ec4ccef2607003d49.jpg)

Article views: 1

![](/api/attachments/PSYWYP2H/fulltext/images/0e2e9490bd8485cc9e4f74d019550f32a9a9b52fdf27a1d7c1edd3d754fa1fb3.jpg)

View related articles ↗

![](/api/attachments/PSYWYP2H/fulltext/images/2191f954f42cc01634ae3a589d47394093b1e50114a0a82bbbcb1e5bc9b285ce.jpg)

Citing articles: 5 View citing articles ↗

# Next-Generation Securities Market Systems: An Experimental Investigation of Quote-Driven and Order-Driven Trading

ROBERT A. SCHWARTZ AND BRUCE W. WEBER

BRUCE W. WEBER. For biographical information, see the Special Section, Guest Editors' Introduction.

ROBERT A. SCHWARTZ is the Marvin M. Speiser Professor of Finance at Baruch College of the City University of New York. He received his Ph.D. in economics from Columbia University and was previously on the faculty of Stern School of Business, New York University for thirty-two years. His research is in the area of financial economics, with a primary focus on the structure of securities markets. He has published numerous journal articles and seven books, including Reshaping the Equity Markets: A Guide for the 1990s. In December, 1995, Professor Schwartz was named the first chairman of Nasdaq's Economic Advisory Board.

ABSTRACT: Several major securities markets including Nasdaq in the United States and the London Stock Exchange's SEAQ are organized as dealer markets that use computer screen displays of competitive dealer quotes to establish fair trade prices. To improve their markets and to reduce investors' trading costs, these exchanges are introducing new rules and systems for handling investors' orders. The redesign of a market structure raises important strategic issues for exchanges; more attractive trading mechanisms will increase order flow and improve liquidity, but margins and total profits earned by traditional exchange intermediaries may be reduced. To examine the consequences of market structure changes, we conducted experimental tests of the integration of an order-driven trading system into a dealer/quote-driven market. Using computer-based simulations of a stock market, experimental subjects traded using a traditional dealer quote screen to which a public limit order facility was added. Data captured on subjects' trading decisions revealed that the limit order system was used by the subjects, attracting some orders that would have otherwise gone to dealers, and lowered investor trading costs. The integration of limit orders reduced dealers' activities as a percentage of total market volume and lowered dealers' trading margins, except in a special "informed dealer" case.

KEY WORDS AND PHRASES: financial markets, market experiments, market microstructure, securities exchange technology, simulation, trading systems.

COMPUTERS AND NETWORKS MAKE POSSIBLE A RANGE OF TRADING mechanism innovations that can improve securities market institutions, and regulators and market participants have called for new trading mechanisms, which are now being introduced in several major stock markets. The effects of changes in a market's structure, however, are difficult to forecast $[2, 3, 16]$ . In market structure research, an important distinction is made between quote-driven and order-driven market structures. Quote-driven markets rely on dealers to compete to provide the most attractive quotes to buy and to sell shares. Examples are the U.S. government bond market, the foreign-exchange market, and the Nasdaq stock market. In an order-driven market, prices are established by limit orders to buy and sell that are submitted to a limit order book by traders and investors $[13]$ . Examples are the Paris Bourse and the Toronto Stock Exchange. Both structures have their advantages, and neither can claim to be closer to the economic ideal of a perfect market. More advanced technology and growing competition between markets, however, are leading stock exchanges to consider new trading systems and changes in their market structures.

Several of the major stock exchanges that are dealer markets—including the London Stock Exchange (LSE) and Nasdaq in the United States—are in the midst of combining quote-driven and order-driven trading mechanisms. In the United States, the Securities and Exchange Commission (SEC) has recommended that Nasdaq modify its systems to:

display immediately customer limit orders. . . . This would improve competition among market participants by providing investors enhanced access to the market and, consistent with the statutory directive of achieving a national market system, would provide greater opportunities for investors' orders to interact with one another. [12, p. 56]

## In London,

[Because] the current [LSE] structure does not easily allow trades to be executed on a "patient" basis, without paying for the cost of risk capital . . . the Exchange intends to provide a vibrant and attractive order book providing liquidity and immediacy for a significant proportion of trades on the Exchange. [9]

However, introducing a limit order mechanism into dealer markets is controversial and has many detractors. In the United States, the NASD has

considered proposing changes that would allow market orders to interact with limit orders between the inside spread, thereby increasing the number of trades executed inside the spread. . . . The NASD staff anticipated that many market makers would oppose this change. [12, p. 31]

And, as reported in the London Financial Times,

there could be a combined quote- and order-driven system [for the LSE], a possibility known as the “hybrid” approach. Marketmakers oppose a hybrid, arguing it would not provide high enough returns . . . . [However] large investors have made it clear they want some form of computerized order-matching system. This would keep costs down by cutting out the middleman. [5, p. 4]

[M]any of the UK's marketmaking firms are resisting order-driven trading. . . . Ministers of Parliament questioned whether a cartel of large market-making companies engineered Mr. Michael Lawrence's ousting [as LSE Chief Executive] in order to block the introduction of order-driven trading in place of their traditional quote-driven system. [1]

One contention is that a limit order facility will benefit the market by reducing costs and giving investors greater flexibility. A counterargument is that a limit order facility will damage dealer firms, and eliminate their profits and willingness to provide liquidity to the market. It is also possible that a limit order facility in competition with dealers will simply not attract enough orders to be relevant and to have an effect on market quality.

To test these conjectures, we developed an experimental trading environment designed to facilitate assessment of these market design modifications. This paper shows how computer simulation can be used to evaluate the effects of market structure changes by capturing data on subjects' order placement behavior and on market quality. We detail an experimental design in which live participants, playing the role of brokerage firms entering discretionary customer orders, interact with the simulated market under three different market structure conditions:

\- The first scenario is a base case with a “pure” dealer market in which users can only submit market orders; all buying and selling is accomplished through dealer-intermediaries.

\- The second scenario integrates a limit order book with the dealer quotes and enable users to enter both market orders and limit orders.

\- In the third scenario, the dealers are given an informational advantage that enables them to trade more aggressively.

The paper goes on to present summary data from the tests, analyze the findings, and summarize our thoughts concerning the effectiveness of simulation as an analytic tool for stock markets that are considering structural changes.

## Simulation of a Realistic Market Environment

## Experimental Objectives

THE OBJECTIVE OF OUR COMPUTER SIMULATION IS TO PROVIDE a backdrop for assessing the market decisions of live participants. Specifically, we have created a controlled background of public order flow and market maker quote setting that can interact with a user $[16]$ . This has enabled us to analyze a dealer market, and a combined dealer and order book market. The success of real-world markets—such as the LSE and Nasdaq—in combining dealer and order book systems depends on adequate acceptance and use by traders. The results from our experiment shed light on how such combined market structures will be used.

Standard tests in experimental economics have not, thus far, used computers to create background order flow into which participants individually enter orders $[14]$ . Our test environment does. This methodological difference has important implications for the development of experimental economics results for market design questions $[13, 15]$ . The computer-generated market provides the controlled and replicable background in which the live participants operate. Moreover, it enables us to combine human decision making with an environment that “mechanically” reproduces trading patterns and strategies that are empirically observed.

Our simulation experiments are an alternative to analytical modeling and empirical tests of actual market data. To be used effectively, simulation models must reflect real-world dynamics without being burdened by unnecessary real-world detail $[8]$ . A market simulation model also requires a strong foundation that is not arbitrary and is consistent with economic theory. The advantage of simulation over theoretical modeling is that “theorizing” requires abstracting away from the very details of market structure that exchange officials and regulators wish to study. Consequently, theoretical modeling can give only limited insight into the effects of market design changes on the behavior of market participants. The advantage of simulation over empirical testing of new market structures is that the simulated experiments can be run at much lower cost, and across a broader range of alternatives.

For our experiments, the computer simulation model accomplishes the following:

\- It establishes the individual bid and ask quotes of five dealers. The quotes are dynamically updated as orders arrive, as trades are made, and as the dealers' inventories reach position limits (both long and short).

\- It generates a public order flow that can (1) execute against the dealer quotes, and in two of the three test scenarios, can (2) be placed on a public limit order book for later execution, or (3) execute against the public limit order book.

\- It instructs live participants to buy a certain quantity of stock. Depending on the test scenario, the live participants can (1) execute these orders against dealer quotes, (2) place them on a public limit order book, or (3) execute them against the public limit order book.

\- It maintains the screen that displays (1) the quotes of the five dealers, (2) orders on the public limit order book, (3) a time-stamped record of all transaction sizes and prices for each trading session, and (4) the value of the market index (see figures 1–4).

\- It captures information concerning (1) the live participants' decisions and (2) market quality measures such as bid-ask spreads. This information is assessed to determine the effect of market structure on the behavior of market participants.

In our person–machine interactive environment, the computer can generate orders from an unlimited number of “machine-resident” traders and investors. This enables us easily to satisfy the conditions for an active, competitive market. This facilitates assessing the relative performance of all participants in an experiment and economizes on our use of live subjects.

Overall, our objective is not to describe subtleties in markets, but to gain insights that will be useful in analyzing a combined dealer and order book market structure, and for recommending market design and rule modifications. We report below on tests run with students and industry executives as live users of the trading simulation.

## Assumptions in the Simulated Market

The simulation has been kept as simple as possible. Key processes in the market are represented, but specific institutional arrangements need not be included. For example, interdealer trading is essential and is included in the simulation, but a separate interdealer trading facility (e.g., SelectNet, Instinet, or London's IDBs) is not explicitly incorporated into the model. The model allows for trading just one security; thus, arbitrage and “pairs” trading are not possible. The subjects’ computers are not connected in a network, and each live participant interacts with the model and their screen individually. Thus, negotiation between two or more live participants is not possible. Further complexity along these and other lines could be added in the future, and the live participants could be given further training, if needed, before participating in more sophisticated experimentation.

![](/api/attachments/PSYWYP2H/fulltext/images/3bb4bfb6c31920a37171cfff20011570051654316ed9870e388f99a6864a3f71.jpg)  
Figure 1. User Trading Screen from the Simulation Experiment: Initial Menu

![](/api/attachments/PSYWYP2H/fulltext/images/2f5294f129d611fcce3a54e9f8f32a279fe09c51e7e1c53725dc47ace0b5bcde.jpg)  
Figure 2. Beginning of Scenario 1 (Dealer-Only) Experimental Run
Current best bid is \$25 and best offer is \$25 $^{2}$ /8. Ticker at top of screen indicates four trades have occurred between \$25 $^{1}$ /4 and \$25 $^{1}$ /8. User has just received instructions to buy 167 units. Benchmark price that the user seeks to buy as far below as possible is currently \$25 $^{3}$ /8.

![](/api/attachments/PSYWYP2H/fulltext/images/a5ef20378af3787898c5c1a1ef7c86c6a0064643c3989160a3fe8d7276bb1ccc.jpg)  
Figure 3. Nearly Two Hours into the Scenario 1 Trading Day (11:02)
User has executed three trades, buying 33, then 40, and most recently 10 from dealers. User has 11 units remaining to buy. The trade of 40 is the most profitable, and the user's cumulative profit is 25.375.

![](/api/attachments/PSYWYP2H/fulltext/images/947032513609b5a73faba670f72493bc9abe664912fa29d87e4803efd59b9735.jpg)  
Figure 4. About Three Hours into Scenario 2 Experimental Run
The limit order book appears below the dealer montage and shows that the best bid and offer of \$25 and \$25 $^{3}$ / $_{8}$ , are both currently being made by limit orders. The user has one limit order to buy 40 at \$24 $^{7}$ / $_{8}$ on the limit order book. The user has executed 5 orders so far, buying 95 with market and limit orders at \$25 and \$25 $^{1}$ / $_{8}$ .

The simulation reflects the runs and reversals in price changes that characterize price adjustments in real-world markets [6]. These patterns give the live participants a rich environment in which to make decisions. The runs and reversal are introduced by specifying an equilibrium (balance) price, $P^*$ , and generating orders from three sources. The $P^*$ price reflects the broad market's assessment of the value of the stock being traded. The live participants do not see $P^*$ , and it follows a random walk jump process (see figure 5). Given $P^{*}$ and the current level of the best bid and offer on the market, orders in the model are generated by three types of machine traders: liquidity traders, informed traders, and momentum traders.

![](/api/attachments/PSYWYP2H/fulltext/images/bbeb4290e6904216b6eeaca255df6d991420c6530618b03c4a6625e509071ad9.jpg)  
Figure 5. Trace of Market Simulation Showing $P^*$ and Evolution of Inside Dealers' Quotes

\- Liquidity traders are simply adding or withdrawing cash from their portfolios without reference to any privileged information about the stock. Liquidity orders may be market orders, or limit orders, whose limit prices are from a triangular distribution with its minimum at the bid quote and mode at the offer price (for sell orders), or its maximum at the offer and its mode at the bid (for buy orders). (See figure 6.)

\- Informed traders have special knowledge that the market prices are too high or too low relative to $P^*$ . Their orders are obtained by referencing the equilibrium price, $P^*$ , and by drawing orders from a tight distribution around $P^*$ whenever $P^*$ lies outside the bid-ask spread.

\- Momentum traders buy or sell when they believe that information-driven trading is occurring. Momentum orders are obtained by increasing the probability that the next order will be a buy (or a sell) whenever three or more buy orders (or sell orders) arrive consecutively.

After the equilibrium value jumps randomly from one level to another, the orders of the informed traders pull the quotes and transaction prices to—and cause them to trend toward—the new level. Occasionally, market prices can also trend away from

![](/api/attachments/PSYWYP2H/fulltext/images/40e03ceed36b2cf11a902db34fe403a8a020266a885abe402b165e617933197c.jpg)  
Figure 6. Distribution of Sell Limit Order Prices around Market Quotes Double Triangular Distribution (Yawl Distribution)

$P^{*}$ because of the orders of momentum traders. However, movements away from $P^{*}$ are unsustainable; eventually, price reverses toward $P^{*}$ . The appendix provides additional details on the model.

## Experimental Design and Hypotheses

SUBJECTS PLAYED THE SIMULATION GAME IN LABORATORY SESSIONS that lasted two hours. Roughly one hour was devoted to explaining the simulation and to allowing the subjects to practice entering orders in the market, and one hour to formal testing. The experiment had three different simulation environments, each of which took about twenty minutes to complete.

## Subjects' Decisions

In the simulation, live participants played the role of public order entry firms, and at different points during the experiment received “instructions” from the computer to buy a quantity of shares. Giving only buy orders was a way of simplifying the subjects’ decisions and controlling complexity. The quantity a user was given was large enough that it could not be fully executed in one trade. This required subjects to exercise discretion in deciding how to break up the instruction into smaller trading orders and when to submit market and limit orders. Each test run covered three simulated days of trading, each of which lasted a simulated 6½ hours (from 9:30 A.M. to 4:00 P.M.). During a “day,” a subject received two buy instructions. Combining subjects’ orders with trading from the computer-generated orders resulted in about 100 trades a day; the subjects were participants in about 10 percent of the trading activity, with the other 90 percent attributable to the machine-resident traders.

## Incentives

The participants in a laboratory session were ranked by a performance measure, and each was given a payment in dollars at the end of the session that depended on his or her relative ranking for the session. $^{1}$ The buy instructions given would create “market impact” and drive up prices if submitted as market orders in large pieces; good performance results from buying at prices that are low relative to subsequent trades. The performance measure for each participant was constructed as follows: Each time the participant brings part of his or her buy instruction to the market, the computer assesses the average share price that would be obtained if the full set of shares were brought to the market in its entirety and executed at one price. We refer to this price as the “benchmark price.” The participant’s “profit” for any trade is the benchmark price minus the actual purchase price, times the number of shares bought. The participant’s performance measure is the cumulative profits over all trades. After each experimental session, participants in the session were paid according to the sum of their performance measures across the three scenarios.

Careful order handling enabled subjects to increase their performance measure by buying at lower prices. Orders can be “worked” by breaking them up into smaller pieces, and by placing limit orders $[4, 6]$ (see figure 4). However, if a limit order executes because the balance price $(P^{*})$ has decreased, the benchmark price will fall accordingly, and the subject will receive a relatively poor profit score for the trade. In effect, the profit score on a trade reflects “ex-post regret” of trading. If a trader buys, but could have bought for less later, the benchmark will fall and profit will be small, or negative. If the trader buys and prices rise, the benchmark increases and profits will be greater. This provides realistic incentives to trade strategically and cost-effectively. In total, overly eager order handling is likely to result in poor scores because of market impact, and excessively patient trading commonly resulted in low scores because the full instruction to buy would not be completed by the end of a simulation run. We cannot derive an optimal order placement strategy for the specific parameterizations of the model used, but subjects’ use of limit orders varied widely, with little correlation to their performance (see figure 7). This was desirable because we are not testing ability to carry out a particular trading strategy, but to observe how subjects balance their use of limit and market orders (figure 8).

Empirical data on limit order and market order use are limited because few markets support both. The New York Stock Exchange (NYSE) market is based on a limit order book and a single dealer, called a specialist, in each stock. Although not directly comparable to the competing dealer and order book market considered here, NYSE indicates that about half of all orders submitted to their market electronically are limit orders, and 73 percent of the shares in orders submitted are limit orders. However, just 44 percent of the shares submitted as limit orders eventually execute [11].

![](/api/attachments/PSYWYP2H/fulltext/images/8fa125042f18bd4963ce27f3d54e9512bf71cec9deba4df86fed626b9a1a3f45.jpg)  
Figure 7. User Profit Measure and Limit Order Usage in Scenarios 2 and 3  
In scenario 2 (squares) and scenario 3 (dots), users' limit orders accounted for between $0\%$ and $85\%$ of their total trading volume. Trading via limit orders was not related to profit performance.

## Hypotheses

A combined trading system will be viable only if its component trading mechanisms are adequately utilized. Of fundamental interest in our experiments is the extent to which the live participants actually use limit orders. The use of limit orders can be measured in two ways: the level (the actual frequency with which limit orders are placed) and the change of the level (how the frequency of use responds to a change in the simulation structure). The level is easier to measure but may be overly dependent on simulation parameters that are somewhat arbitrary. The change in the level is difficult to capture but more meaningful. We place primary emphasis on the change of the level. We hypothesize that limit order use and its changes will depend on conditions in the market.

The experiments enable us to test three hypotheses:

H1. Live participants will use more limit orders when market bid-ask spreads are wider.

The bid-ask spread is the price of immediacy for investors, and at higher values it will encourage limit order use. The greater the price of immediacy, the more likely a public participant will enter limit orders.

H2. Participants will use limit orders less frequently when dealers have an informational advantage regarding the location of $P^{*}$ .

Assume that in the combined quote- and order-driven market structure, the expressions of trading interest are those reflected below. The stock currently has a bid quote of \$24 $^{1/4}$ , which reflects the limit order to buy 15. Three dealers have a bid quote of \$24 $^{1/8}$ , which is inferior to the limit order buyer willing to pay \$24 $^{1/4}$ . The best offer to sell is at \$24 $^{1/2}$ by Dealers no. 1 and 3. The lowest limit order to sell is at \$24 $^{5/8}$ , which is inferior to the dealers' ask quotes. A dealer's quote is good for up to 25 units. However, after a trade occurs, all dealers have the option to move their quotes. This implies that it may not be possible to buy 50 at the current offer price of \$24 $^{1/2}$ .

Combined Dealer Quotes and Limit Order Book Market Structure

<table><tr><td>Limit orders to buy (no. of shares)</td><td>Dealers&#x27; bid</td><td>Price</td><td>Dealers&#x27; offer</td><td>Limit orders to sell (no. of shares)</td></tr><tr><td></td><td></td><td>$24 $\frac{3}{4}$ </td><td>—</td><td>12</td></tr><tr><td></td><td></td><td>24 $\frac{5}{8}$ </td><td>Nos. 2, 4, 5</td><td>10</td></tr><tr><td></td><td></td><td>24 $\frac{1}{2}$ </td><td>Nos. 1, 3</td><td></td></tr><tr><td></td><td></td><td>24 $\frac{3}{8}$ </td><td></td><td></td></tr><tr><td>15</td><td></td><td>24 $\frac{1}{4}$ </td><td></td><td></td></tr><tr><td>6</td><td>Nos. 2, 4, 5</td><td>24 $\frac{1}{8}$ </td><td></td><td></td></tr><tr><td>22</td><td>Nos. 1, 3</td><td>24</td><td></td><td></td></tr></table>

Limit order strategy: To execute an order to buy, an investor could place a limit buy order (a bid) at $24^{3/8}$ or less. If entered at $24^{3/8}$ , it does not immediately execute, but supersedes the bid of $24^{1/4}$ as the best bid. The hope is that a market sell order arrives and executes against the limit buy order at $24^{3/8}$ , or that a dealer that has become long sells the stock to the limit order.

Market order strategy: Under the same circumstances, an investor using a market order can buy immediately at the offer price of $24^{1/2}$ .

The limit order trader can avoid the cost of immediate execution ( $0.25$ in this example). Limit orders, however, face the risk of not executing, and the risk that the price will move adversely while they are on the book. For instance, the offer price could move higher without the limit order at $24^{3/8}$ executing.

Figure 8. Market Order and Limit Order Illustration

In actual markets, some public customers are at times at an informational disadvantage vis-à-vis dealers who are professionals, and whose contact with a broad array of customers (including institutional clients) is frequent. Dealers may capitalize on any informational advantage via the placement of their quotes and by “picking off” mispriced limit orders. We hypothesize that, if the dealers do so, the live participants will be discouraged from using limit orders. The dealers were given more of an informational advantage in scenario 3 than in scenario 2.

H3. The limit order book will reduce dealer profits by “disintermediating” some of the trading volume, but the order-driven facility will give dealers a new way to lay off positions and risk.

A limit order book allows for trading to take place without dealer participation. Limit orders can provide liquidity to dealers as well as other investors. Since market makers avoid large long or short positions, the presence of limit orders can help dealers to control their risk and reduce the size of their losses from adverse price movements. The reduction in dealer profits from a limit order book could be offset by decreased risk.

To test these hypotheses, we vary market conditions by creating three alternative scenarios, and by assessing the participants' differential use of limit orders. The first scenario is a dealer screen only (no limit order facility). The second and third scenarios, which include a limit order facility, are differentiated by the following in number 3: (1) the dealers' ability to have superior knowledge of the equilibrium (balance) price, $P^*$ , and (2) the dealer bid-ask spread, or the price of dealer-provided immediacy.

Subjects undertook the buying exercise in three scenarios:

\- Scenario 1: Uninformed dealers. Dealers have no special information concerning the location of $P^*$ and its changes. Dealer quotes are relatively wide and, hence, the price of dealer provided immediacy is relatively high. In scenario 1, all trading takes place via market orders trading at dealers' quoted bid and ask prices.

\- Scenario 2: Uninformed dealers with quote-setting as in number 1. The limit order book is integrated into the market, and price priority is enforced so that a limit order at a better price than the best dealer quote will trade first. If the best dealer quote and the best limit order are tied at the same price, then the quote or order placed earliest has priority.

\- Scenario 3: Dealers are informed of $P^{*}$ changes about half the time giving them better information concerning the location of $P^{*}$ than the live participants. It is reasonable to assume that with better information, dealer quotes can be narrowed and the price of dealer-provided immediacy reduced without losses. Dealers will tighten the bid-ask spread from \$ $^{3/4}$ in scenarios 1 and 2, to \$ $^{1/2}$ .

The informational advantage of dealers in scenario 3 was controlled as follows: As noted earlier, quotes and transaction prices can differ from the $P^{*}$ level after a change in $P^{*}$ , or when temporarily pushed away from $P^{*}$ by momentum traders or chance one-sided liquidity order flow. In scenario 1 and 2, we gave the dealers no special information about $P^{*}$ , but in scenario 3, when the dealers know the new value of $P^{*}$ half of the time when it change. When it falls below public buy limit orders (or rises above public sell limit orders), the dealers sell to the overpriced public bids with their own sell orders (or buy from the underpriced public offers with their own buy orders). In the process, they adjust their bid and offer quotes to straddle $P^{*}$ . Although dealer spreads are \$0.25 narrower, the profits of the machine dealers are increased by the occasional information signal they are given (see Table 5).

## Conduct of the Experiments

OUR TESTS CONSISTED OF FOUR LABORATORY SESSIONS conducted with four students each (sixteen subjects), and one with eight industry participants (a total of 24 subjects). Eight of the subjects were Ph.D. students at NYU's Stern School of Business, and eight were graduate students at The Wharton School. A simulation experiment was also conducted with eight industry executives. Each experimental session lasted two hours. Roughly one hour was spent introducing the participants to the experiment and the simulation, and having them practice entering orders into the simulated market. One hour was then devoted to running the formal tests.

Each formal test period was divided into three twenty-minute periods. The subjects completed one scenario in each twenty-minute interval. The first period included the dealer only scenario, while a limit order facility was included in the second and third periods. For the second period, about half of the subjects had the “uninformed dealer” scenario; the other half completed the “informed dealer” scenario. This controlled for ordering effects in the presentation of the scenarios. The final scenario completed was whichever scenario remained for the subject.

Fundamental parametric values were held constant across all simulation runs, and the tests were structured so that valid, ceteris paribus contrasts could be made. Each new simulation run began with a different random number seed to keep the subjects uncertain about what the new price changes would be. Changing the random number seed, however, results in a different sample of returns, and some random number seeds produce more volatile returns or price trending than others. To mitigate any bias that this might cause, the random number seeds were rotated between the three twenty-minute windows for the different experimental groups.

## Results

TABLES 1A AND 1B PRESENT A BREAKDOWN OF THE SUBJECTS' orders by type of order and scenario. Scenario 1 is dealers-only trading, and dealers are not informed of $P^*$ changes. Scenario 2 combines the uninformed dealer market with a limit order facility, and scenario 3 is informed dealers and limit order facility. The live subjects used limit orders about as much as they used market orders in scenarios 2 and 3 (the only scenarios where they are allowed). Limit orders ranged from 46 percent to 57 percent of the total orders submitted. Because not all limit orders execute, market orders were used for over half of the shares actually bought. The data from the industry subjects are only reported separately in Table 1a, but because meaningful differences did not appear, we report all subsequent data in aggregate.

Table 2 shows the frequency with which the various spread values occurred, and the frequency with which market orders are entered at different values of the spread. The use of market orders diminishes when the spread is at its widest level (e.g., $\frac{5}{8}$ and

Table 1. Subjects' Order Placement Decisions  
a. Breakdown of Subjects' Orders by Type and Scenario

<table><tr><td rowspan="2">No. of shares</td><td colspan="3">Students (n = 16)</td><td colspan="3">Industry practitioners (n = 8)</td></tr><tr><td>Scen. 1</td><td>Scen. 2</td><td>Scen. 3</td><td>Scen. 1</td><td>Scen. 2</td><td>Scen. 3</td></tr><tr><td>Market orders</td><td>4,917</td><td>3,148</td><td>3,003</td><td>2,618</td><td>1,530</td><td>1,748</td></tr><tr><td>Limit orders placed</td><td>0</td><td>4,123</td><td>2,523</td><td>0</td><td>1,736</td><td>1,748</td></tr><tr><td>Limit orders executed</td><td>0</td><td>1,763</td><td>1,345</td><td>0</td><td>1,032</td><td>870</td></tr><tr><td>Limit orders as percentage of total placed</td><td>NA</td><td>56.7%</td><td>45.7%</td><td>NA</td><td>53.2%</td><td>50.0%</td></tr><tr><td>Limit order as percentage of total executed</td><td>NA</td><td>35.9%</td><td>30.9%</td><td>NA</td><td>40.3%</td><td>33.2%</td></tr></table>

b. Aggregated Data

<table><tr><td rowspan="2">No. of shares</td><td colspan="3">All subjects (n = 24)</td></tr><tr><td>Scenario 1</td><td>Scenario 2</td><td>Scenario 3</td></tr><tr><td>Market orders</td><td>7,535</td><td>4,678</td><td>4,751</td></tr><tr><td>Limit orders placed</td><td>0</td><td>5,859</td><td>4,271</td></tr><tr><td>Limit orders executed</td><td>0</td><td>2,795</td><td>2,215</td></tr><tr><td>Limit orders as percentage of total placed</td><td>NA</td><td>56.1%</td><td>46.7%</td></tr><tr><td>Limit orders as percentage of total executed</td><td>NA</td><td>36.8%</td><td>31.5%</td></tr><tr><td>Limit order execution rate</td><td>NA</td><td>45.7%</td><td>52.4%</td></tr></table>

3/4). For example, in scenario 1, the bid-ask spread was 5/8 or 3/4 36.9 percent of the time, but only 23.4 percent of the total market orders were placed when the spread was that wide. The dealers' spread was reduced from 3/4 to 1/2 in scenario 3, and as a result the maximum market spread is 1/2, and no data cells are needed in the lower right of the table.

Table 3 shows the frequency with which limit orders are entered at different values of the spread. Limit orders are used at all values of the spread, but they are used least when the spread is narrowest ( $\frac{1}{8}$ and $\frac{1}{4}$ ).

Table 4 focuses on the use of limit orders versus market orders. A meaningful pattern appears to exist between the use of these two types of orders and spread size. When the spread is narrow, subjects used relatively more market orders, which is sensible and supports our first hypothesis. The only exception is in scenario 2, when limit orders were used less at the widest spreads (5/8 or 3/4) than when the spread was an intermediate level (3/8 and 1/2). However, 5/8 and 3/4 spreads only occurred 18.9 percent of the time in scenario 2. We also find that, overall, limit orders are used less than market orders in scenario 3 than in scenario 2. In scenario 3, reduced limit order use may result from the narrower spreads observed in scenario 3, or from the information advantage given to the dealers. Comparing the two scenarios when spreads were 3/8 and 1/2, indicates that some of the diminished attractiveness of limit orders is due to the dealers' information advantage. This supports the second hypothesis: The risk of informed dealers "picking off" limit orders (following a change in the balance price, $P^{*}$ ) reduces the incentive to use limit orders. The order book will be better utilized the smaller the information advantage enjoyed by dealers relative to public investors.

Table 2. Subjects' Market Orders Placed at Different Bid-Ask Spreads

<table><tr><td rowspan="2"></td><td colspan="2">Scenario 1 (base)</td><td colspan="2">Scenario 2 (uninformed)</td><td colspan="2">Scenario 3 (informed)</td></tr><tr><td></td><td rowspan="2">Market orders entered</td><td rowspan="2">Spread freq.</td><td rowspan="2">Market orders entered</td><td rowspan="2">Spread freq.</td><td rowspan="2">Market orders entered</td></tr><tr><td>Spread (in $)</td><td>Spread freq.</td></tr><tr><td> $\frac{1}{8}$  &amp;  $\frac{1}{4}$ </td><td>24.3%</td><td>26.7%</td><td>39.2%</td><td>44.9%</td><td>71.7%</td><td>72.7%</td></tr><tr><td> $\frac{3}{8}$  &amp;  $\frac{1}{2}$ </td><td>38.8%</td><td>49.9%</td><td>41.9%</td><td>38.5%</td><td>28.3%</td><td>27.3%</td></tr><tr><td> $\frac{5}{8}$  &amp;  $\frac{3}{4}$ </td><td>36.9%</td><td>23.4%</td><td>18.9%</td><td>16.6%</td><td>NA</td><td>NA</td></tr></table>

Table 3. Subjects' Limit Orders Placed at Different Spreads

<table><tr><td rowspan="2">Bid-ask spread</td><td colspan="2">Scenario 2</td><td colspan="2">Scenario 3</td></tr><tr><td>Spread frequency</td><td>% limit orders entered at this spread</td><td>Spread frequency</td><td>% limit orders entered at this spread</td></tr><tr><td> $\frac{1}{8}$  &amp;  $\frac{1}{4}$ </td><td>39.1</td><td>31.1</td><td>71.7</td><td>69.5</td></tr><tr><td> $\frac{3}{8}$  &amp;  $\frac{1}{2}$ </td><td>41.9</td><td>51.8</td><td>28.3</td><td>30.5</td></tr><tr><td> $\frac{5}{8}$  &amp;  $\frac{3}{4}$ </td><td>18.9</td><td>17.1</td><td>NA</td><td>NA</td></tr></table>

Based on the results shown in Tables 1 through 4, we conclude that the subjects are responding rationally to the availability of the limit order book. They use limit orders when allowed to do so, and cut back on their use of market orders at very wide spreads. Use of limit orders is positively related to the costs of trading immediacy; more limit orders are submitted when the spread widens from $\frac{1}{8}$ and $\frac{1}{4}$ to $\frac{3}{8}$ and $\frac{1}{2}$ . And the subjects cut back on their use of limit orders when the limit orders are at risk of being picked off by better informed dealers (scenario 3 compared with scenario 2).

Table 5 presents summary statistics for the three scenarios. Comparing scenario 1 with the others, the introduction of the limit order facility narrows the bid-ask spread, reducing trading costs for investors. The dealers' share of trading volume falls from 100 percent in scenario 1 to about 64 percent in scenario 2. This indicates that investor limit orders are able to provide liquidity to arriving market orders over a third of the time. In the hybrid market, the need for dealer intermediaries is reduced, but not eliminated. In scenario 3, when dealers are informed and tighten the bid-ask spreads that they each quote to $\frac{1}{2}$ from $\frac{3}{4}$ , they regain market share and are counterparties to over three-quarters of trading volume.

As expected, dealer profits fall from scenario 1 to scenario 2, and the third hypothesis is supported. Dealer margins (profits divided by the value of dealer trading) were slightly reduced in scenario 2. Moreover, the dealers' average position size decreases about 25 percent, and hence dealers' position risk is lower in the presence of an active order book. In scenario 3, dealers are informed about half of all $P^*$ changes, and their profits increase substantially. This is certainly due to the ability to quote the "right" price and avoid losses from trading with informed investors. Another effect of the order-driven facility is a reduction in interdealer trading volumes, as dealers can often balance their inventory positions with limit orders rather than trading with rival dealers.

Table 4. Ratio of Subjects' Limit Orders Placed Relative to Market Orders

<table><tr><td>Bid-ask spread</td><td>Scenario 2 limit ÷ market</td><td>Scenario 3 limit ÷ market</td></tr><tr><td>All values</td><td>1.28</td><td>0.90</td></tr><tr><td> $\frac{1}{8}$  &amp;  $\frac{1}{4}$ </td><td>0.88</td><td>0.86</td></tr><tr><td> $\frac{3}{8}$  &amp;  $\frac{1}{2}$ </td><td>1.72</td><td>1.00</td></tr><tr><td> $\frac{5}{8}$  &amp;  $\frac{3}{4}$ </td><td>1.31</td><td>NA</td></tr></table>

Table 5. Market Aggregates

<table><tr><td></td><td>Scenario 1</td><td>Scenario 2</td><td>Scenario 3</td></tr><tr><td>Average bid-ask spread</td><td>50.4¢</td><td>38.0¢</td><td>26.0¢</td></tr><tr><td>Percentage of price</td><td>2.0</td><td>1.6</td><td>1.1</td></tr><tr><td>Percentage of total trading volume with a dealer counterparty</td><td>100.0</td><td>63.7</td><td>76.8</td></tr><tr><td>Average dealer profits (normalized)</td><td>100.0</td><td>56.9</td><td>299.8</td></tr><tr><td>Dealer margin in basis points</td><td>9.3</td><td>8.3</td><td>36.3</td></tr><tr><td>Average absolute dealer inventory position</td><td>19.9</td><td>14.3</td><td>19.3</td></tr><tr><td>Interdealer trading volume as percentage of total volume</td><td>33.2</td><td>16.3</td><td>16.7</td></tr></table>

Table 6 highlights the spread-narrowing benefits of enabling market participants to place limit orders. In both scenarios 2 and 3, over 40 percent of user limit orders reduced the bid-ask spread. When users placed limit orders at prices greater than the existing bid quote, the average improvement on the existing best bid was 18 cents in scenario 2, and 13 cents in scenario 3. These improvements over the existing bid are about half of the average spread in scenarios 2 and 3.

## Conclusions and Future Research

THE MARKET SIMULATION PROVIDED AN EXPERIMENTAL TRADING environment that we used to test the characteristics of a hybrid quote-driven and order-driven market structure. Critical to its success, the simulation was kept simple enough to be workable for the live subjects, but also rich enough to generate useful results. Twenty-four live subjects had no difficulty learning the simulation, and they appeared to find the exercise interesting and enjoyable.

The simulation runs generated a considerable amount of data which we captured. The important results can be highlighted:

\- The subjects used the limit order facility actively, and dealers saw some of the trading activity bypass them as investor limit orders traded against investor market orders in the order book.

Table 6. Subjects' Placement of Buy Limit Orders Relative to Existing Bid Quote

<table><tr><td></td><td colspan="2">Scenario 2</td><td colspan="2">Scenario 3</td></tr><tr><td>Number of limit orders entered</td><td colspan="2">394</td><td colspan="2">258</td></tr><tr><td>Average (per subject)</td><td colspan="2">16.4</td><td colspan="2">10.7</td></tr><tr><td>Range (per subject)</td><td colspan="2">(4–43)</td><td colspan="2">(0–20)</td></tr><tr><td>Greater than existing bid quote and average improvement</td><td>41.0%</td><td>18.0¢</td><td>42.2%</td><td>13.4¢</td></tr><tr><td>At existing bid quote</td><td>26.6%</td><td>—</td><td>34.3%</td><td>—</td></tr><tr><td>Less than existing bid and average amount less than bid</td><td>32.4%</td><td>30.4¢</td><td>23.5%</td><td>19.8¢</td></tr><tr><td></td><td>100.0%</td><td>—</td><td>100.0%</td><td>—</td></tr></table>

\- The limit order book reduced the market's bid-ask spread.

\- The relative use of limit orders and market orders was correlated with spread width in a reasonable fashion; wider spreads led to greater limit order submission by subjects, and many of those limit orders narrowed the spread.

\- The introduction of a limit order facility reduced aggregate dealer profits and margins when the dealer did not have privileged $P^*$ information. It also lowered dealers' percentage of trading volume. This implies that, in a hybrid market, dealer profits will decrease unless (1) overall trading activity increases sufficiently to offset the order book's volumes, or (2) dealers have some informational advantages that enable them to exploit the orders in the order book.

Our tests indicate that market design changes have significant impacts on trader behavior and market quality, and that the market simulation environment is a workable device for undertaking experimental analysis of these effects. A two-hour experiment with mostly student subjects will naturally have limitations, and we expect to make the following enhancements in the conduct of the experiments and in the structure of the simulation.

The inclusion of buy and sell orders: In the current version of the simulation, the live subjects entering orders were given buy orders only so as to keep their role as order entry firms as simple as possible. With more training, the subjects could be given both buy and sell orders. This would make their task more realistic and more challenging. It would also enable a simpler performance measure to be used. By balancing the buy and sell orders given to each subject so that the sum of all shares bought equaled the sum of all shares sold over the course of a simulation run, we would then assess each participant's performance by a simple profits calculation: The sum of all positive cash flows from sales, less the sum of all negative cash flows from purchases.

Live subjects play the role of dealers: In the current tests, the live subjects played the role of investors entering orders. Tests should also be run with the subjects playing the role of dealers. There are open questions about how dealers strategies might change as a result of new limit order systems. Subject dealers could have the option of changing their bid-ask spreads, committing more or less capital to their trading, reducing the size of trades they accept, or passing small orders directly onto an order book and providing liquidity only for large, block trades.

Alternative treatment variables: Important market structure questions concern the most desirable level of market transparency and visibility. In several order-driven markets, traders can choose to reveal only part of their overall trading order on the market screen, while the rest remains “hidden,” and will appear only once the visible order executes. Because the publication of large block trades often signals that a dealer holds a large, potentially unwanted position, some markets allow for delayed dissemination of trade prices to enable dealers to reduce their positions and their risk. In the United States, several markets are implementing finer price increments for stock (i.e., reducing the minimum price variation from \$1/8 to \$1/16), and there is discussion of moving to decimal prices and allowing for share prices in units as low as pennies. These issues could be examined using simulation trading experiments, and the results would provide guidance on the behavioral responses of traders to such important market design considerations.

To summarize, we use computer-based simulations of a stock market as a background for examining the effects of combining an order-driven trading system into a dealer/quote-driven market. The results indicate that market participants will use a limit order facility, and that the combined market structure will reduce investor trading costs. An active limit order facility reduces the role of dealer-intermediaries in trading, and erodes dealer profitability. If dealers have some informational advantages, or aggregate trading volumes increase as a result of an improved market, however, a combined market may not necessarily make intermediaries worse off. Interactive simulations appear to be useful for analyzing the effect of market design changes on trader behavior and market quality. The results can provide guidance on market structure issues such as those facing exchanges that are involved in the development of combined order-driven and quote-driven trading systems.

## NOTES

Acknowledgments: Financial support from the Nasdaq Stock Market and the NYU Salomon Center. Hugo Levecq, a Ph.D. student in the Information Systems Department, Stern School, NYU, tested the simulation software and conducted several of the trading experiments.

1. Cash payments ranged from \$20 to \$30 for two hours. Payments were not made in the industry practitioner experimental session. Instead, results were tabulated and displayed.

## REFERENCES

1. Backtracking angers brokers. Financial Times (April 24, 1996).

2. Clemons, E., and Weber, B. Alternative securities trading systems: tests and regulatory implications of the adoption of technology. Information Systems Research, 7, 2 (June 1996), 163–188.

3. Cohen, K.; Conroy, R.; and Maier, S. Order flow and the quality of the market. In Y. Amihud,

T. Ho, and R. Schwartz (eds.), Market Making and the Changing Structure of the Securities Industry. Lexington, MA: Lexington Books, 1985, pp. 93–109.

4. Conroy, R., and Winkler, R. Informational differences between limit and market orders for a market maker. Journal of Financial and Quantitative Analysis (December 1981), 703–724.

5. Gapper, J. Options for order-driven system published. Financial Times (January 13, 1996), 4.

6. Handa, P., and Schwartz, R. Limit order trading. Journal of Finance, L1, 5 (December 1996), 1835–1861.

7. Ho, T., and Macris, R. Dealer market structure and performance. In Y. Amihud, T. Ho,

and R. Schwartz (eds.), Market Making and the Changing Structure of the Securities Industry. Lexington, MA: Lexington Books, 1985.

8. Law, A., and Kelton, W.D. Simulation Modeling and Analysis, 2d ed. New York: McGraw-Hill, 1991.

9. London Stock Exchange. New Electronic Trading Services: Proposal for the Introduction of a Public Limit Order Book. May 1996.

10. Mendelson, H. Consolidation, fragmentation, and market performance. Journal of Financial and Quantitative Analysis, 22 (June 1987), 189–207.

11. New York Stock Exchange. Fact Books. And correspondence with Research Department, 1989–1995.

12. Report pursuant to section 21(a) of the Securities Exchange Act of 1934 regarding the NASD and the Nasdaq market. Securities Exchange Commission, August 1996.

13. Schwartz, R. Reshaping the Equities Markets: A Guide for the 1990s. Homewood, IL: Business One Irwin, 1993.

14. Smith, V. Microeconomic systems as an experimental science. American Economic Review Proceedings (1982), 923–955.

15. Smith, V., and Williams, A. Experimental market economics. Scientific American (December 1992), 116–121.

16. Weber, B. Assessing alternative market structures using simulation modeling. In R. Schwartz (ed.), Global Equity Markets: Technological, Competitive, and Regulatory Challenges. Homewood, IL: Business One Irwin, 1994.

17. Weber, B. Bypass trading and market quality in electronic securities exchanges. Journal of Organizational Computing, 5, 3 (1995), 327–353.

## APPENDIX: Details of the Simulation Model

THIS APPENDIX DESCRIBES THE MAJOR FEATURES of the simulation model and the user instructions. The simulation involves one live person interacting with a computer-driven “market background.” There is one risky security, and the live user plays the role of a public order entry firm.

The computer screen has two parts: (1) A dealer montage that shows the quotes of five dealers—this screen is similar to, but not a replication of, the Nasdaq screen; the display is simplified to economize on information load and to facilitate comprehension by the live participants; and (2) a limit order file that resembles an open order book-type facility. The screens are shown in figure 1.

Quotes and orders are generated by the computer. The computer-driven orders arrive stochastically, according to a poisson order arrival process. Order interarrival time is a parameter in the model. We set the order arrival rate to thirty orders per hour. Dealer quote setting is based on heuristic rules built into the model that result in market makers adjusting their bids and offers according to their inventory and position limits. (See figure 5.)

In the dealer-only simulation (scenario 1), all public orders are market orders.

Market orders trade immediately at the best bid quote (if it is a market sell order) or at the best offer quote (if it is a market buy order). In the dealer and limit order file model, a limit order that arrives in the market indicates the maximum price at which a purchase is to be made, or the lowest price at which a sale is to be made. The procedures used for generating machine orders are discussed in further detail below.

All orders, whether generated by the computer or by the live participant, are integer values of from one to twenty-five units of the security. The initial value of the equilibrium price is \$25.00, and moves in increments of $\frac{1}{8}$ (12.5 cents). $^{1}$

## Order Size

On the basis of its fit with empirical data, the Beta distribution was selected for order sizes in the simulation. The Beta distribution is useful for modeling activity completion times and quantity demands that are bounded on a finite interval. In the simulation, order sizes are distributed as a discrete linear transformation of a $\text{Beta}(a,b)$ random variable, resulting in integers between 1 and 25.

## Order Preferencing

Public market orders that execute against dealer quotes are directed to specific dealers by the following procedure: To simplify the discussion, consider the arrival of a market sell order (the handling of a market buy order is symmetrical). If all of the dealers are making the best bid price, an incoming sell order is allocated to a dealer on the basis of market share. For instance, a dealer with a 20 percent market share has a one-fifth chance of getting the next incoming order. If only some dealers are making the best price, the order may be preferred to a dealer who is not setting the best bid or offer, but who will trade at the inside quote. In this case, the order will go to a dealer based on the following market share adjustment: The market shares of all dealers making the best quote are multiplied by 1.3 and added to the market shares of the other dealers. This new sum is used to scale back the individual market shares of all dealers so that the final sum is unity. $^{2}$ This procedure reduces the probability of receiving a customer order when a dealer is not making the inside quote.

## Order Flow

Three sources of machine-driven orders are included in the simulation model: liquidity traders, informational traders, and momentum traders. The liquidity traders provide a base level of trading volume. Orders from liquidity traders arrive stochastically, according to a poisson order arrival process. An individual liquidity order is either a buy order or a sell order with equal probability.

Each liquidity order is drawn from a double triangular distribution that has one probability peak at the market bid and a second probability peak at the market ask (see figure 6). This probability structure assures the preservation of a nontrivial bid-ask spread in the market. By varying parameters of the double triangular distribution, we are able to control, stochastically, the size of the bid-ask spread. Both market and limit orders are drawn from the distribution. For a buy order, a draw from the distribution at or above the market ask is a market buy order; a draw from the distribution below the ask is a limit order, and it is placed on the limit order file. Sell orders are handled symmetrically.

As the market bid and ask quotes change with the course of the simulation, the location of the double triangular distribution shifts with them. $^{3}$ If the double triangular distribution were the only source of order flow, transaction prices generated by the simulation would follow a random walk with a bid-ask bounce. Over time, with a random walk, prices will drift from one level to another; the price drift would be consistent with random informational change and instantaneous, perfect adjustment to that change in the marketplace. The environment would be what financial economists refer to as “informationally efficient.”

Informed traders generate one-sided (buy or sell) volume, above the base level, whenever the market makers' quotes do not straddle an underlying equilibrium price, $P^{*}$ , as discussed above. $P^{*}$ is not seen by the live traders. Changes in $P^{*}$ create profit opportunities for the informed traders. The trades of the informed participants cause the market bid and ask quotes to move toward, and eventually to straddle, $P^{*}$ . One-sided orders from informed traders are generated according to the poisson order arrival process. The time between information change is exponentially distributed with a mean of four hours. $^{4}$

The expected arrival rate of informed orders depends on the relationship between market quotes and $P^{*}$ . If the bid and offer quotes straddle $P^{*}$ —for example, $P^{*} = 24\frac{5}{8}$ , and the bid is $24\frac{1}{2}$ and the offer is $24\frac{7}{8}$ —there is no informed order flow. When $P^{*}$ is above (below) the bid-offer range, buy (sell) orders are generated by a poisson arrival process that reflects the rate at which “informed” machine traders become aware of the relatively high (low) value of $P^{*}$ . We control the arrival rate of informed orders by increasing the base order arrival rate for buy orders by 75 percent (when $P^{*}$ is above the ask) and for sell orders by 75 percent (when $P^{*}$ is below the bid). The increased order flow from informed traders provides the link that keeps the equilibrium value ( $P^{*}$ ) loosely aligned with market maker quotes. Adjustment of the quotes to change in $P^{*}$ is not immediate, and volume tends to increase when the equilibrium price and the quotes diverge.

Momentum traders are a class of investors who trade whenever they sense that trending in the market has been caused by a change of $P^{*}$ . Momentum traders enter orders over and above the base volume whenever there is a sequence of three or more trades or quote improvements on one side of the market. If they follow sufficiently closely on the heels of informed traders, this can be a profitable short-term strategy. The strategy is unlikely to be profitable if the trend is merely a chance arrival of three liquidity orders on the same side of the market.

## Market Makers

Each of the five dealers is assigned a market share and a position limit. In the course of the simulation, when a dealer's inventory position increases beyond a position limit, he or she takes a number of steps to reduce the size of the position. The first step taken is to raise or lower his or her quotes. When the position becomes twice the position limit, the dealer initiates trades with other dealers, hitting their bids or lifting their offers. A dealer also initiates trades with other dealer(s) whenever raising or lowering a quote would lead to a “locked” market (the bid and offer quotes are equal).

Instructions to the user are generated by the computer. Once an instruction to buy is given, orders can also be entered by the live participant at his or her discretion.

## Market Rules/Trade Priorities

When the limit order book is available, the limit orders are “protected” from trade-throughs. For instance, a limit order to buy at 23 $^{1/4}$ must be filled before any trades can occur at 23 $^{1/8}$ . Public limit orders are generally executed according to strict time and price priority vis-à-vis other public limit orders and dealer quotes. If a large order executes against two or more limit orders placed at different prices, the entire block is executed at the lowest bid that it executes against (for a sell), or at the highest ask that it executes against (for a buy). From the user’s perspective, there are no negotiations; all transactions are made at posted quotes.

Interdealer trading is an important component in dealer markets, as it is the means by which public buying/selling pressure on one dealer is transmitted to other dealers. Real-world facilities for interdealer trading include Instinet (in the United States) and the IDBs (in the United Kingdom). It is not necessary for our purposes to include a specific facility in the simulation, and doing so would only complicate the screen for the live participants. We simply trigger direct dealer-to-dealer trading whenever the inventory adjustment rules call for one dealer to hit or lift the quote of another dealer. All initiated interdealer trades are of size 10 units. All interdealer orders received by another dealer are of size 1 to 10 units, depending on the size of public limit orders on the book that have priority. Interdealer trades are not preferred, meaning that only dealers quoting the best price will receive the next order.

## Order Book/Dealer Interactions

Our simulation allows for interaction between the dealer screen and the limit order screen. Dealers can hit public buy orders and lift public offers to sell on the limit order book. The dealers also take public limit order prices into account when setting their own quotes. At all times, strict time and price priority is given to orders on the public limit order file vis-à-vis each other. Time priority also determines the sequence of order execution when a public limit order is tied in price with a dealer quote. A large incoming market order can execute partially against the limit order file and partially against a dealer quote if the incoming market order is larger than the sum of the public limit orders that have priority over the dealer quotes. When this occurs, the entire block executes at a single price (the highest price reached for a buy, or the lowest price reached for a sell). Outcomes and market quality may be highly sensitive to rules such as these.

## Appendix Notes

1. If one unit is viewed as representing 300 shares, the size and price values would reflect a convenient normalization, which is reasonably realistic for the Nasdaq market (trade sizes of \$4,000 to \$100,000 account for about 70 percent of the total value of Nasdaq trades). Beyond 25 units, we assume the trade would be handled as a negotiated block trade, or would arrive in the market in a sequence of smaller pieces.

2. For instance, assume four dealers, that two of the four have 20 percent market shares and are making the best quote, and that the other two dealers have a 30 percent market share and are not making the best quote. The probability that one of the dealers on the quote will get the trade is $1.3 \times 20/(2 \times 1.3 \times 20 + 2 \times 30) = 23.2$ percent > 20.0 percent. The probability of one of the other dealers receiving the order is 30/112 = 26.8 percent < 30.0 percent. Note that $2(23.2) + 2(26.8) = 100$ .

3. Specifically, two double triangular distributions are used: one for the generation of buy orders and another, its mirror image, for the generation of sell orders.

4. $P^{*}$ , when it changes, follows a random walk without return drift. To assure nonnegative prices, $P^{*}$ is determined using a log-normal distribution. That is,

$$
\ln P _ {t} ^ {*} = \ln P _ {t - T} ^ {*} + e _ {t} \quad \text { where } e _ {t} N (0, T V),
$$

where $t$ is an index on time, $T$ is the elapsed time since the last price change, and $V$ is a variance parameter.
