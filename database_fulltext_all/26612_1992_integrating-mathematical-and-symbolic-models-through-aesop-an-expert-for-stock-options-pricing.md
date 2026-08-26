---
otero_id: 26612
otero_key: "KDG34Y4S"
title: "Integrating Mathematical and Symbolic Models Through AESOP: An Expert for Stock Options Pricing"
authors: "James Clifford; Henry C. Lucas; Rajan Srikanth"
year: "1992"
journal: "Information Systems Research"
doi: "10.1287/isre.3.4.359"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/KDG34Y4S/fulltext/images/a535acd22f3f966efb1312cda9580a201eb3047f33b835f5e7cd23673876363c.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Integrating Mathematical and Symbolic Models Through AESOP: An Expert for Stock Options Pricing

James Clifford, Henry C. Lucas, Rajan Srikanth,

## To cite this article:

James Clifford, Henry C. Lucas, Rajan Srikanth, (1992) Integrating Mathematical and Symbolic Models Through AESOP: An Expert for Stock Options Pricing. Information Systems Research 3(4):359-378. http://dx.doi.org/10.1287/isre.3.4.359

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1992 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/KDG34Y4S/fulltext/images/935f58ffaa3aca3b650bd1e396dc20cf0c8d7d8b84a150532eaab9bd0bd6e470.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Integrating Mathematical and Symbolic Models Through AESOP: An Expert for Stock Options Pricing

James Clifford

Leonard N Stern School of Business

New York University

Henry C. Lucas, Jr.

Rajan Srikanth

New York, New York 10012

Leonard N–Stern School of Business

New York Universuy

New York, New York 10012-1126

Walter A Haas Schooł of Business Unıversıty of Californıa, Berkeley Berkeley, Calfornua 94720

This paper reports on an effort to integrate symbolic and mathematical models to tailor the output of a mathematical model to the particular domain of a decision maker. AESOP combines the Black-Scholes model of stock options pricing with an expert system; the integrated model is designed for use by an options specialist on the American Stock Exchange. The specialist makes a number of adjustments to the output of the mathematical model; the purpose of the symbolic model is to make as many of these modifications as possible automatically. The paper reports on the development and structure of AESOP and presents data on its use.

Expert systems—-Systems design--Symbolic models—Mathematical models—Black-Scholes model

## 1. Introduction

perations Research has made a major contribution to management through mathematical modeling. A model may provide an optimal solution for the decision-maker given that the model's assumptions are valid. A number of factors can, however, limit the applicability or usefulness of these models in real-world situations. For example, a user who is not well-versed in operations research may find it difficult to interpret the output of a mathematical model. Also a mathematical model may provide an optimal solution for a general class of problems, but the user may need to adjust the model to fit his or her particular domain.

As an example, the Black-Scholes model for stock options pricing presented later in this paper provides a theoretical point estimate for the price of an option. For an investor interested in purchasing or selling an option, this price may be entirely satisfactory. However, for the market-maker or specialist on the Exchange floor, a theoretical point estimate is not adequate for direct use. The specialist's problemsolving domain and the rules he uses to adjust the output of the model are difficult to represent in the framework of a mathematical model.

## 1.1. Integrated Models

What options are available to the model-builder when it is difficult or impossible for mathematics to reflect all of the relevant aspects of a problem setting? In such a case, it may be possible to combine a symbolic and mathematical model to form an enriched model for a particular domain. One type of symbolic model is an Expert System (ES), a system which attempts to apply human knowledge to solving a complex problem. An Expert System combines a knowledge base about some domain or application area with an inference capability to perform tasks that normally require considerable human expertise (Turban 1988); for examples of ES see (Reitman 1984).

A mathematical model represents a decision problem with variables and relationships among variables. In a management setting, the goal of the modeler is often to provide an optimal solution to a problem. Techniques for solving mathematical models include the use of linear programming, dynamic programming and calculus to solve for a minimum cost solution.

A symbolic model uses variables or symbols, too. However, this model resembles logic more than computational mathematics. The symbolic model might represent a complex decision through the use of IF THEN rules or through first-order predicate calculus. Symbolic models of this type do not attempt to optimize; rather they describe a problem domain and its solution through logic.

How can a symbolic model be integrated with a mathematical one to provide enhanced problem-solving capability? There are several possibilities:

## I. The symbolıc model helps the user build or use the mathematical model.

This first type of integrated model features a symbolic component which assists the decision-maker in building and /or using a mathematical model. For example, Ma et al. (1989) have developed an expert system to help a user formulate large linear programming models, and Krishnan (1990) has proposed a logic model to help generate linear programs for production and inventory applications.

Il. The mathematcal model generates output which is modified in some way by the symbolic model.

Another possibility is for the symbolic model to adjust the output of the mathematical model so that it fits the domain of the problem-solver. AESOP, the expert system discussed in this paper, is an integrated model of this type.

III. The symbolic model chooses an appropriate mathematical model.

The symbolic model examines the problem domain and uses its knowledge to recommend the appropriate mathematical model. Nostradamous (Weitz 1986) is an example of this type of system; it examines a user's forecasting problem and selects an appropriate mathematical forecasting model given the user's domain. Nicklaus et al. (1988) have developed a system which helps an engineer choose and parameterize optimization models for design.

IV. The symbolic and mathematical models interact during execution.

This final possibility represents the closest possible coupling of mathematical and symbolic models. While we are unaware of an example of this level of integration, it is possible to envision a system in which an iterative procedure like a goal programming model interacts with a symbolic model to modify or revise goals during problem solution.

## 1.2. An Example

As an example of type Il integration, suppose that a mathematical model for pricing a stock option produced a theoretical price of \$4.50. Further, assume that the problem domain had the following requirements represented in a symbolic model:

• Prices of options above \$3 must have their fractions stated in eighths.

• There is to be a bid/ask spread of \$0.50 (i.e., the decision-maker wants to have two prices; he is willing to buy options at the bid price and sell them at the ask price).

• The bid/ask spread should be symmetric around the theoretical price.

• There is a limit order to sell a May 40 call at $4 { \hat { \ } } 5$

The symbolic model would apply the rules above to recommend prices of $\$ 42$ bid, \$4^6 askeċ where $\mathit { \hat { \Pi } } ^ { \star } \widehat { \mathbf { \Pi } } ^ { \star }$ is $^ { 2 } _ { 8 } ,$ etc.

The symbolic model would examine the theoretical price of \$4.50 and recommend a bid price of the theoretical price minus one-half the spread price and an ask price of the theoretical price plus one-half the spread price. Before recommending this price, however, it would discover the existence of a limit order within this range. The symbolic model would therefore adjust the ask price down to $\begin{array} { c } { { \dot { \mathbf { y } } } } \\ { { \mathbf { 8 } } } \end{array}$ and recalculate the bid at 4^1. It would then recognize that 0.25 is $\begin{array} { c } { { \vdots } } \\ { { \tilde { 8 } } } \end{array}$ and 0.75 is ${ \bf \Pi } _ { 8 } ^ { 0 } ,$ , resulting in the final recommended bid/ask prices.

Could the symbolic model be stated in mathematical terms? It is possible to state the logic in the example mathematically, though the presence of the limit order introduces a great deal of complexity. The logic of the symbolic model is easier to follow in the form of the rules presented above. In addition, it is easy to envision many more complex requirements that would be difficult to represent in a mathematical model.

Having expertise expressed symbolically in the form of rules, rather than hidden inside a closed-form equation, allows the system to explain why it has recommended a particular price by displaying the rules that it followed to generate the recommendation. This use of a mathematical model combined with a set of rules of expertise in effect mimics the way the options specialist, himself, uses the Black-Scholes model The combination of mathematical and symbolic models provides an enriched model; it produces results that are more useful to the decision-maker than the output of either model alone.

This paper reports on the development of a system which combines mathematical and symbolic models to assist an options specialist on the American Stock Exchange establish quotations for stock options. AESOP, An Expert for Stock Options Pricing, integrates the mathematical Black-Scholes options pricing model with a symbolic model in the form of an Expert System to support pricing decisions by the specialist. This system must perform in a demanding environment in “real-time."

The specialist has limited time to arrive at quotations and can incur a significant financial loss by posting a poor price. He must perform a large number of calculations and apply judgment to the results in a very short period of time. An expert specialist participated in the development of the system described here, and another specialist in his firm used the system for several months on the Exchange floor.

The major contributions of this research are (1) the development of an integrated mathematical and symbolic model, and (2) the successful application of the resulting system in a demanding environment.

<table><tr><td colspan="7">TABLE 1An Example of a Call Option</td></tr><tr><td colspan="7">XYZ CallsStock Price $42 00</td></tr><tr><td rowspan="2"></td><td colspan="2">40</td><td colspan="2">45</td><td colspan="2">50</td></tr><tr><td>Bid</td><td>Ask</td><td>Bid</td><td>Ask</td><td>Bid</td><td>Ask</td></tr><tr><td>May</td><td>3^5</td><td>3^7</td><td>0^05</td><td>0^4</td><td>0^0</td><td>0^1</td></tr><tr><td>June</td><td>4^1</td><td>4^3</td><td>0^13</td><td>1^0</td><td>0^0</td><td>0^1</td></tr></table>

## 2. The Domain: AMEX and Options Trading

## 2.1. The Stock Option

An option is a security giving the holder the right to buy or sell an asset at a specified time. A stock option call is the right to buy a share of stock at a certain price at a future date, while a put is the right to sell a share of stock. The price at which one may purchase or sell the stock is called the strike price. On the American Stock Exchange (AMEX), options have an expiration date before which they may be exercised; a position in an option may also be closed out by purchasing an offsetting contract. All options expire on the third Saturday of the month of exercise.

Table 1 is an example of a call option for XYZ stock. The price of a May option to buy a share of X YZ at \$40 (the ask price) is \$3 and $_ 8 ^ { 7 } .$ (Below \$3, options are priced in sixteenths, and above \$3 they are priced in eighths.) The bid price for the May 40 is \$3 and $_ 8 ^ { 5 } .$ The quote for the May 50 call option is no bid, $\mathbf { \Sigma } _ { 8 } ^ { 1 }$ asked, meaning the specialist will pay nothing to buy the option but is willing to sell it for $\$ 1$ . The price is given for an option to buy or sell one share of the stock, however, contracts on the AMEX are for 100 shares. An option for a stock at a certain strike price is called an options sertes.

Assume that the current price of a share of XYZ is \$42. A May 40 call is said to be in the money because, if the stock price holds until expiration, an option owner has the right to buy a share for \$40 and can sell it immediately for \$42. The May 45 and 50 calls are out of the money. For puts, the opposite logic holds. A May 40 put is out of the money because, if the \$42 stock price holds until the option expires, there is no gain from having the right to sell a share of stock at \$40 when the market price is \$42. The May 45 and May 50 puts, on the other hand, are in the money.

## 2.2. The Specialist

The options specialist is a market maker in an option. He or she is responsible for posting the bid and ask quotes for the stock option at the options post on the floor of the Exchange. There is only one specialist on the Exchange for each stock option. The specialist maintains an entire inventory of options and can trade from his or her own account. Specialists also maintain a position in the underlying stock as a hedge on their inventory of options. The role of the specialist is to assure a fair and orderly market; the specialist buys and sells from his own account to prevent price changes from being unduly erratic.

If the specialist posts an incorrect price, he or she does not obtain the maximum return on invested capital and runs the risk of incurring a large loss. Investors, noting a discrepancy between the price of the option and the underlying stock, will arbitrage against the specialist. Errors in pricing provide the investor with an opportunity for nearly risk-free profits. (The specialist's exposure is limited because a public quote is only good for a limited number of contracts).

An important role of the specialist is to represent limit orders. The limit order is an offer to buy or sell an option at a particular price. The specialist is responsible for executing a trade for the limit order when the option price reaches the price on the limit order, assuming he has a customer who will take the other side of the trade or that he will handle the trade from inventory.

For example, assume the specialist has a customer who puts in a limit order to buy at 4 and $_ { \mathrm { ~ 8 ~ } } ^ { \mathrm { ~ 2 ~ . ~ } }$ the current bid price for the option is 4 and $_ { 8 } ^ { 3 } .$ The specialist can lower his quotation so that the public bid price is 4 and $_ 8 ^ { 2 } \colon$ however. he cannot lower it to 4 and ! because he: holds a limit order from a buyer willing to pay 4 and ${ \bf \Xi } _ { 8 } ^ { 2 } .$ . Representing limit orders is currently a manual process relying on slips of paper and a good memory on the part of stock options specialists at the AMEX. A limit order is placed for the day only or on a good until cancelled (GTC') basis. According to the specialist, many of the errors made in pricing are due to the difficulty of remembering all of the limit orders on hand and reflecting them in his pricing strategy.

## 2.3. The AMEX Floor

The atmosphere on the exchange floor is not especially conducive to decision making; the more active an option, the more turbulent the environment. The specialist may have from 1 to 20 or more floor traders and brokers gathered around his or her post. This boisterous crowd consists of individuals shouting for information or delivering pids and limit orders. The environment is a difficult one for the introduction of a computer-based system.

## 3. The Black-Scholes Model

Many of the options specialists at the AMEX use a classic model for valuing options developed by Black and Scholes (Black and Scholes 1973). The model arrives at a theoretical options price based on the following assumptions:

(1) a known and constant interest rate,

(2) a stock price following a random walk with a variance proportional to the square of the price,

(3) the stock pays no dividends or distributions,

(4) the option is exercised only at expiration,

(5) there are no transa tions costs.

(6) one can borrow to purchase or hold at the interest rate in (1),

(7) there are no penalties to selling short, i.e., selling without owning the security

Given these assumptions, the model for the theoretical price of an option is (Black and Scholes 1973):

$$
w (x, t) = X \times N (d _ {1}) - c \times e ^ {r (t - t ^ {*})} \times N (d _ {2}),\tag{1}
$$

$$
d _ {1} = (\ln x / c + (r + 0. 5 v ^ {2} (t ^ {*} - t)) / (v \times \sqrt {t ^ {*} - t}),\tag{2}
$$

$$
d _ {2} = (\ln x / c + (r - 0. 5 v ^ {2}) (t ^ {*} - t)) / (v \times \sqrt {t ^ {*} - t}). \quad \text { where }\tag{3}
$$

$w \{ x , t \}$ is the value of an option on a stock with price x at time t,

• c is the exercise (strike) price,

• r is the T-bill rate,

$t ^ { * } - \mathbf { t }$ is the duration of the option,

• v is the variance of the rate of return or the volatility of the stock, and

• N is the cumulative normal density function.

A pricing model for options is not an optimizing model. It calculates an option price (given the price of the underlying stock and other parameters) that prevents an investor from earning a risk-free profit by arbitraging between a stock and its option. Black-Scholes was not designed to meet the unique needs of the market maker. However, as discussed below, the model is used extensively by specialists at the AMEX.

## 3.1. The Specialist and the Model

The specialist involved in this research has used the Black-Scholes model for a number of years and would have been reluctant to change models. His current system for computing the model runs on a personal computer and was provided by his options clearing firm. This Options Valuation System (OVS) maintains a record of the specialist's position in options and underlying stock and also computes the Black-Scholes theoretical prices for his options.

The specialist provides the parameters for the model; his most frequent change is in the underlying stock price. The stock for his options is traded on the New York Stock Exchange and the monitor at his post displays the bid and ask prices as well as the last sale price of the underlying stock at the NYSE. The specialist also changes the interest rate used by the model and inputs new volatilities for the stock.

To provide him with an idea of the sensitivity of option prices to movement in the underlying stock price, the specialist uses OVS each morning to print out a matrix of theoretical prices which he references when the stock price fluctuates during the day. Looking at the theoretical prices, the specialist posts quotations by putting a bid/ask spread around the theoretical price for each options series.

The output of the Black-Scholes model is of invaluable assistance to the specialist. However, due to the assumptions of the model and the unique situation of the specialist, he must modify the theoretical prices. Instead his pricing strategy requires that he take the following into consideration when pricing:

• The model outputs point estimates; the specialist must put a bid/ask spread around the theoretical price. (The specialist has a desired spread which is one of his decision variables; the stock exchange also has guidelines for spreads which are a constraint on the decision process.)

• The specialist can not price through limit orders; he must constantly check his book of limit orders.

• The exchange regulations on pricing, e.g., the maximum spread allowed between bid and ask prices, the requirement to price in $\mathbf { \Pi } _ { 1 6 } ^ { 1 }$ below \$3 and $\mathbf { \Sigma } _ { 8 } ^ { 1 }$ above.

• The specialist's own inventory position in a series.

• The possibility that certain quotations when combined provide an opportunity for someone to arbitrage against the specialist. (The theoretical price prevents arbı- trage, but some of the constraints cited in this section force the specialist to post prices that differ from the theoretical price and therefore create opportunities for arbitrage.)

• The level of current trading activity in the option.

## 4. AESOP

AESOP integrates the Black-Scholes mathematical model with a symbolic model in the form of an expert system; AESOP provides recommended quotations for the specialist which are closer to what he can post than the theoretical prices produced by the mathematical model alone. The AMEX sponsored the development of the system with a research grant; its objective was to assess the use of Expert Systems technology at the exchange. The objectives of the researchers were to demonstrate that the combination of a mathematical model and a symbolic one would produce more useful results than either model alone in the specialized domain of a decision maker

The researchers also wanted to show that the special circumstances of the specialist could best be modeled symbolically and that the symbolic and mathematical models could be successfully integrated. It is possible that one could develop a new mathematical or economic model for the specialist. The research team feels that such a model would be very difficult to create; it is not clear how to model all of the constraints imposed on the specialist.

Another goal was to show that such an integrated model could succeed in the challenging environment of the exchange floor. Many expert systems are advisory and operate with loose time constraints. The options-pricing specialist must function in close to “real-time" as the market changes. The existing Black-Scholes model was used in “batch mode;" typically the specialist worked with a printed report showing theoretical options prices for different underlying stock prices. AESOP would have to function on the floor of the Exchange and provide recommendations whenever the specialist changed input parameters; the recommended prices would have to appear quickly enough to be posted to the public quote board before a trader could take advantage of an “old" price.

## 4.1. The Expert

The Expert System was developed over a two-year period with a senior options specialist at the AMEX as the human expert. (A significant amount of time was lost during and after October 1987.) The ES uses rules to represent the knowledge of the specialist. This particular approach to knowledge representation seemed natural given the environment; the American Stock Exchange has a series of rules that apply to options prices. The heuristics used by the expert specialist also seemed to follow an if-then structure: for example, “IfI am long on contracts, then reduce the asking price by one increment." The expert model is presented in greater detail later in the paper.

## 4.2. Overview of AESOP

Figure 1 presents an overview of the AESOP system. The specialist interacts with the svstem through the user interface which is managed bv AESOP's control module. The functions provided by the interface are explained in the next section. When the user changes any parameter. the control module invokes the Black-Scholes mathematical mcdel to generate theoretical prices for each series. If the specialist has four different strike prices for each expiry month, with four months listed for both puts and calls, there are 32 theoretical values to be computed (four strikes × four months for puts and calls).

The symbolic model represents the pricing strategy of the specialist, a domain that may not be receptive to mathematical modeling (something that would be difficult to do mathematically). The symbolic model always considers the specialist's desired spreads (the difference between bid and ask prices) and always applies the specialist's rounding rules. (Public quotations must be stated in sixteenths and eighths of a dollar.)

If the specialist's position in any series exceeds a threshold level, then the symbolic model adjusts the price of that option to encourage (specialist is long) or discourage (specialist is short) trading. The symbolic model also looks for limit orders and adjusts the bid/ask prices based on the presence of these orders. Limit order adjustments are the most complicated and potentially the most valuable feature of the symbolic model.

![](/api/attachments/KDG34Y4S/fulltext/images/f8ac3acbe696f4401647aae5cb06ee8fdfc3eb01a008aad25d8aba477b031393.jpg)  
FIGURE 1. The AESOP Model.

The symbolic model always checks the AMEX rules to be sure that exchange regulations are not violated. The model also scans for arbitrage possibilities. In almost all cases. arbitrage arises because bid/ask prices have been adjusted away from the theoretical price for some reason, most often because of the presence of a limit order.

AESOP presents the recommended quotations of the symbolic model along with the theoretical prices generated by the mathematical model. The user is free to override any recommendations, ask for an explanation or trace of the symbolic model, and/or change parameters and rerun the entire system.

## 4.3. The User Interface

The interface development effort grew well beyond what the researchers had originally envisioned. Figure 2 shows a hard copy of the main AESOP screen, but the figure in no way does justice to the color coding and pop up windows that characterize the interface. The menu within the user interface is activated by function keys shown at the bottom of Figure 2; submenus appear on the second and third line of the screen and follow Lotus conventions. The interface to AFSOP provides the following functions:

AESOP: An Expert for Stock Options Pricing

<table><tr><td colspan="10">AESOP - AN EXPERT SYSTEM FOR OPTIONS PRICING ACCT: RIC OPTION: TANCALLS</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>2:05 pm</td></tr><tr><td rowspan="2">MONTH</td><td rowspan="2">STRIKE</td><td rowspan="2">TH.VA</td><td colspan="2">LIMIT.BOOK</td><td colspan="2">RECCO.QUOTE</td><td colspan="2">CURR.BOARD</td><td></td></tr><tr><td>BID</td><td>ASK</td><td>BID</td><td>ASK</td><td>BID</td><td>ASK</td><td>STOCK</td></tr><tr><td rowspan="3">MAY</td><td>40.00</td><td>3.72</td><td></td><td></td><td> $3^5$ </td><td> $3^7$ </td><td> $3^6$ </td><td> $4^0$ </td><td>43.500</td></tr><tr><td>45.00</td><td>0.35</td><td></td><td></td><td> $0^05$ </td><td> $0^4$ </td><td> $0^3$ </td><td> $0^09$ </td><td>XDIV</td></tr><tr><td>50.00</td><td>0.00</td><td></td><td> $0^1$ </td><td> $0^0$ </td><td> $0^1$ </td><td> $0^0$ </td><td> $0^1$ </td><td>06/25/89</td></tr><tr><td rowspan="3">JUN</td><td>40.00</td><td>4.15</td><td></td><td></td><td> $4^1$ </td><td> $4^3$ </td><td> $4^2$ </td><td> $4^4$ </td><td>INT.RATE</td></tr><tr><td>45.00</td><td>0.89</td><td></td><td></td><td> $0^13$ </td><td> $1^0$ </td><td> $0^7$ </td><td> $1^1$ </td><td>10.25</td></tr><tr><td>50.00</td><td>0.06</td><td></td><td> $0^2$ </td><td> $0^0$ </td><td> $0^1$ </td><td> $0^01$ </td><td> $0^03$ </td><td>V1</td></tr><tr><td rowspan="4">JUL</td><td>35.00</td><td>9.15</td><td></td><td></td><td> $9^0$ </td><td> $9^3$ </td><td> $9^1$ </td><td> $9^5$ </td><td>22</td></tr><tr><td>40.00</td><td>4.52</td><td></td><td></td><td> $4^3$ </td><td> $4^6$ </td><td> $4^4$ </td><td> $4^7$ </td><td>V2</td></tr><tr><td>45.00</td><td>1.34</td><td> $0^09$ </td><td></td><td> $1^1$ </td><td> $1^3$ </td><td> $1^2$ </td><td> $1^4$ </td><td>21</td></tr><tr><td>50.00</td><td>0.21</td><td> $0^2$ </td><td> $0^5$ </td><td> $0^2$ </td><td> $0^05$ </td><td> $0^2$ </td><td> $0^3$ </td><td>V3</td></tr><tr><td rowspan="3">OCT</td><td>40.00</td><td>5.65</td><td> $2^1$ </td><td></td><td> $5^4$ </td><td> $5^7$ </td><td> $5^4$ </td><td> $6^0$ </td><td>20</td></tr><tr><td>45.00</td><td>2.54</td><td></td><td> $4^0$ </td><td> $2^05$ </td><td> $2^09$ </td><td> $2^3$ </td><td> $2^5$ </td><td>V4</td></tr><tr><td>50.00</td><td>0.88</td><td></td><td> $1^3$ </td><td> $0^13$ </td><td> $1^0$ </td><td> $0^7$ </td><td> $1^01$ </td><td>20</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>FN. KEYS</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>AF1 DEL.LO</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>AF3 CHG.PR</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>AF5 DL.OVR</td></tr></table>

(1) entering and processing limit orders.

(2) invoking the OVS system for updating contracts, positions, etc.,

(3) changing parameters in the Black-Scholes model or bid/ask spreads.

(4) explaining the reasoning behind each price quotation.

(5) alerting the user to arbitrage possibilities,

(6) manually overriding any recommended price,

(7) simulating the posting of prices to the “current board."

(8) displaying the position or changing the threshold position for position rules to apply,

(9) logging the interaction with the system, and

(10) Running the Black-Scholes model

## 5. The Symbolic Model

Before the development of the Black-Scholes model the specialist computed quotations from experience and a feel for the market. After the development of the Black-Scholes model, in theory the specialist could calculate prices automatically for posting. However, as described in §3, the specialist cannot post the Black-Scholes recommended quotations directly due to (1) the need to place a bid/ask spread around the recommended price, (2) exchange rules, and (3) the specialist's limit orders and position.

The symbolic part of AESOP takes the output of the mathematical Black-Scholes model and adjusts it to incorporate the pricing strategies of a specialist on the American Stock Exchange. The goal of the symbolic model is to recommend bid and ask prices for each put and call for a particular option series assigned to the specialist.

<table><tr><td>TABLE 2Example Rules</td></tr><tr><td>TABLE 2aExample Rule Without Variables</td></tr><tr><td>reflect_limit_orders←determine_active_limit_ordersAND reflect_active_limit_orders</td></tr><tr><td>TABLE 2bExample Rule With Variables</td></tr><tr><td>limit_order_is_active(Option,buy,Price_List)←current_recommendation(Option,Quote_Bid)AND maximum(Price_List,Highestst_Order)AND Highest_Order ≥ Quote_Bid</td></tr></table>

## 5.1. Details of the Model

The symbolic model of AESOP is represented using a large number of Prolog predicates. Some of these predicates capture the pricing rules used by the specialist and constitute the knowledge base of AESOP, while other predicates are used to control the overall execution of AESOP, in particular the priority of various rules in the overall pricing strategy. To illustrate the symbolic model, this section presents rules used by the expert for reflecting any limit orders in the bid and ask prices, checking that no AMEX rules are violated by the proposed prices, and alerting the specialist to potential arbitrage possibilities.

Table 2 presents two examples of rules, one with and one without arguments. The rules are presented as first-order predicate calculus formulas, rather than in Prolog syntax, for ease of presentation. The rule in Table 2a is declarative and can be read as a logical axiom; the sy mbol “" represents logical implication. Such rules can be read backwards or forwards; for the purposes of this paper forward reading is employed. The rule in Table 2a can therefore be read as:

```sql
TO reflect_limit_orders,
determine_active_limit_orders
AND
reflect_active_limit_orders
```

Rules may also have predicates with arguments; in the tables of examples, AESOP arguments which are constants begin with lower-case letters and those which are variables begin with upper-case letters. When a rule has variables or constants, its meaning is slightly more complex as shown by the example in Table 2b. Variables in the body or right-hand side of the clause (on the right of the ←) are existentially quantified. Variables in the head of the clause, on the left-hand side of the ← are universally quantified. The rule in Table 2b should be read as:

AND

TABLE 3  
V’ariables Used in the Modet

<table><tr><td>Variable</td><td>Explanation</td></tr><tr><td>Actual_Dividend</td><td>The actual dividend of the underlying stock</td></tr><tr><td>Ask</td><td>The Ask price for a particular option in a series</td></tr><tr><td>Ask_Reasons</td><td>The (coded) explanation behind the recommended Ask price</td></tr><tr><td>Bid</td><td>The Bid price for a particular option in a series</td></tr><tr><td>Bid_Reasons</td><td>The (coded) explanation behind the recommended Bid price</td></tr><tr><td>Buy_Or_Se.l</td><td>Whether the price is the buy or sell price</td></tr><tr><td>Carry</td><td>The cost of carrying a position</td></tr><tr><td>Curr_Spread</td><td>The current difference between Bid and Ask prices</td></tr><tr><td>Daily_Interest</td><td>The daily interest rate</td></tr><tr><td>Dividend</td><td>The dividend of the stock underlying the option</td></tr><tr><td>Highest_Order</td><td>The highest limit order bid for a series (in limit order book)</td></tr><tr><td>Lowest_Order</td><td>The lowest limit order asking price for a series (in limit order book)</td></tr><tr><td>Max</td><td>AMEX maximum allowable spread for month and bid</td></tr><tr><td>Min</td><td>AMEX minimum allowable spread for month and bid</td></tr><tr><td>Month</td><td>The month the option expires</td></tr><tr><td>NewAsk</td><td>A computed asking price</td></tr><tr><td>NewBid</td><td>A computed bid price</td></tr><tr><td>Num_Days</td><td>The number of days to expiration of an option</td></tr><tr><td>Option</td><td>Either to buy or sell, with a month and a strike price</td></tr><tr><td>Percentage</td><td>A “fudge” factor on how much of the Carry cost to consider</td></tr><tr><td>Price_List</td><td>A list of limit orders and their prices</td></tr><tr><td>Problem</td><td>Represents the type of AMEX rule violation</td></tr><tr><td>Quote_Ask</td><td>The currently quoted Asking price</td></tr><tr><td>Quote_Bid</td><td>The currently quoted Bid price</td></tr><tr><td>Spread</td><td>The difference between the Bid and Ask prices</td></tr><tr><td>Stockprice</td><td>The current price of the stock underlying the option</td></tr><tr><td>Strike_Increment</td><td>The difference between two strike prices</td></tr><tr><td>Units</td><td>The appropriate unit of a Bid or Ask, i.e. eights or sixteenths</td></tr><tr><td>Which</td><td>Represents whether to adjust the Bid or the Ask price (or neither) to rectify an AMEX rule violation</td></tr><tr><td>Xdiv_Days</td><td>Number of days remaining until the underlying stock goes exdivided</td></tr></table>

maximum himit order on the Price\_list is Highest\_Order  
Highest\_Order is greater than the Quote\_Bid

Table 3 contains a list of variables used in the symbolic model along with their definitions.

## 5.2. The Highest Level

As described earlier, the user works with AESOP through the interface module. Any actions taken by the user which potentially impact the Black-Scholes theoretical prices cause AESOP to automatically compute new theoretical prices. As an example, if the user changes the underlying stock price, interest rates or volatilities, adds limit orders or makes similar changes, AESOP reinvokes the Black-Scholes model. Whenever the system invokes Black-Scholes, it also applies the symbolic model to each theoretical price to make adjustments reflected in recommended quotes.

AESOP's expert system component contains over 3,000 lines of Prolog code with nearly 200 rules consisting of 400 clauses and nearly 1,500 terms. It is impossible to present the full details of the symbolic model in a reasonable amount of space. The rest of this section presents examples of limit order rules, stock exchange rules, and rules for detecting arbitrage opportunities.

## 5.3. Limit Order Rules

Table 4 contains the limit order rules. AESOP must first determine if a limit order is active, that is, if there is a limit order that affects a given series. The first four predicates in Table 4 determine whether or not a limit order affects this series. A limit order must be considered if it is a buy limit order and the price of the limit order is higher than the bid price AESOP would like to recommend. Posting the recommended quotation is not allowed because a buyer with a limit order is willing to pay more than the recommended quotation. Similar logic applies if there is an active sell limit order with a limit order price less than the price that AESOP would like to recommend.

The last four predicates in Table 4 show how AESOP adjusts the recommended quotes to reflect limit orders. For example, in the first reflect\_active\_limit\_orders predicate, if there is a sell limit order with a price higher than the recommended quote, AESOP will post the highest limit order price as the recommended buy quote along with the ask quote already computed from earlier rules.

## 5.4. AMEX Rules

The AMEX rules have a high priority as the specialist in general does not want to violate an exchange regulation. The second predicate in Table 5, as an example, checks to be sure that AESOP's recommended spread is not larger than the maximum spread allowed by Exchange rules. If the spread is too big, AESOP must adjust it to fall within regulations. It is also possible that a spread is too small; the third predicate in Table 5 examines this possibility.

Adjusting recommended quotes at this point is complex because conflicts may develop. In general, conflicts are resolved in AESOP by the ordering in which the specialist's rules are applied. The most general rules—for example, to create prices using a standard bid/ask spread around the Black-Scholes theoretical value—are applied first. The effect of earlier rules may subsequently be modified, when appropriate, by the application of more specific or stringent rules that might apply to a particular option. Some conflicts can arise which are beyond the scope of AESOP's knowledge base. In such cases AESOP alerts the specialist to the presence and the nature of a conflict; it is up to the specialist, alerted by AESOP, to take some action to resolve the conflict.

For example, suppose that two limit orders have narrowed the spread on an option to the point that it violates Exchange rules. There is no solution that AESOP can apply; if the system widens the spread to satisfy Exchange rules, it will price through a limit order and violate limit order rules. There is a conflict which the system cannot resolve; it will report the conflict back to the human specialist to solve. (His most likely course of action is to process one or both of the limit orders to eliminate their influence on the recommended quotations.) Most of the predicates in Table 5, then, deal with trying to resolve a violation of AMEX rules.

## 5.5. Arbitrage Rules

Table 6 contains the predicates AESOP uses to check for four types of arbitrage; the first predicate includes each type: box, conversion, dividend and discount. The different types of arbitrage can be performed against the specialist; the arbitrageur makes money at the expense of the specialist (or a customer who has entered a limit order). As an example, in conversion arbitrage, the arbitrageur buys the underlying stock and buys a put option while selling a call option having the same term. Under certain conditions, this position will have a locked-in profit if the total cost of the position is less than the strike price of the option.

TABIE 4 Limı Order Rules  
```csv
reflect_limit_orders ←
    determine_active_limit_orders
    AND reflect_active_limit_orders

determine_active_limit_orders ←
    limit_order(Option,Buy_Or_Sell,Price_List,inactive)
    AND limit_order_is_active(Option,Buy_Or_Sell,Price_List)

limit_order_is_active(Option,buy,Price_List) ←
    current_recommendation(Option,Quote_Bid)
    AND maximum(Price_List,Highest_Order)
    AND Highest_Order ≥ Quote_Bid

limit_order_is_active(Option,sell,Price_List) ←
    current_recommendation(Option,Quote_Ask)
    AND minimum(Price_List,Lowest_Order)
    AND Lowest_Order < Quote_Ask

reflect_active_limit_orders(Option,buy,Price_List) ←
    active_limit_order(Option,sell)
    AND current_recommendation(Option,Quote_Bid,Quote_Ask)
    AND maximum(Price_List,Highest_Order)
    AND post(current_recommendation(Option,Highest_Order.Ask))

reflect_active_limit_orders(Option,buy,Price_List) ←
    current_recommendation(Option,Quote_Bid,Quote_Ask)
    AND maximum(Price_List,Highest_Order)
    AND spread_to_apply_is(Option,buy,Highest_Order,Spread)
    AND new_ask_is(Option,Highest_Order,Spread,NewAsk)
    AND post(current_recommendation(Option,Highest_Order,NewAsk))

reflect_active_limit_orders(Option,sell,Price_List) ←
    active_limit_order(Option,buy)
    AND current_recommendation(Option,Quote_Bid,Quote_Ask)
    AND minimum(Price_List.Lowest_Order)
    AND post(current_recommendation(Option,Quote_Bid,Lowest_Order))

reflect_active_limit_orders(Option,sell,Price_List) ←
    current_recommendation(Option,Quote_Bid,Quote_Ask)
    AND minimum(Price_List,Lowest_Order)
    AND spread_to_apply_is(Option,sell,Lowest_Order,Spread)
    AND new_bid_is(Option,Lowest_Order.Spread,NewBid)
    AND post(current_recommendation(Option,NewBid,Lowest_Order))
```

McMillan (1986) gives the following example:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Stock price $55 00 Buy
January 50 call at $6 and $^{1}_{2}$ Sell
January 50 put at $1 Buy
</div>

The arbitrageur pays \$55 for the stock and receives \$6.50 for selling the call while paying \$1 for the put, yielding a total cost of \$49.50. The arbitrageur is guaranteed a

## TABLE 5

## AMEX Rules

check\_\_amex\_rules(Option) current\_\_recommendation(Option,Quote\_Bid,Quote\_Ask,Bid\_Reasons,Ask\_\_Reasons) AND max\_spread(Quote\_Bid,Month,Max) AND min.\_spread(Quote\_Bid,Min) AND Curr\_Spread = Quote\_Ask – Quote\_Bid AND check\_amex\_rules1(Option,Quote\_Bid,Quote\_Ask,Bid\_Reasons,Ask\_Reasons, Max,Mın,Curr\_Spread)

check\_\_amex\_rules1(Option,Quote\_Bid,Quote\_Ask,Bid\_\_Reasons,Ask\_Reasons Max.Min.Curr\_Spread) ← Curr\_Spread > Max AND which\_is\_adjustable(Bid\_Reasons,Ask\_Reasons,Which) AND make\_amex\_adjustment(Option,Quote\_Bid,Quote\_\_Ask,Max,Min,toobig,Which)

check\_\_amex\_rules1(Option,Quote\_Bid,Quote\_Ask,Bid\_Reasons,Ask\_Reasons Max,Min,Curr\_Spread) ← Curr\_Spread < Min AND which\_is\_adjustable(Bid\_Reasons,Ask\_Reasons,Which) AND make\_amex\_adjustment(Option,Quote\_Bid,Quote\_Ask,Max,Min,toosmall,Which)

which\_is\_adjustable(Bid\_Reasons,Ask\_Reasons,neither) member(Ask\_Reasons,lımit\_order) AND member(Bid\_\_Reasons,lımit\_\_order)

which\_is\_adjustable(Bid\_Reasons,Ask\_\_Reasons,bid) (member(Ask\_Reasons,limit\_order) AND NOT (member(Bid\_Reasons,lımit\_order))) OR (member(Ask\_Reasons,override) AND NOT (member(Bid\_Reasons,override))) OR (member(Ask\_Reasons,position\_adjustment) AND NOT (member(Bid\_Reasons,position\_adjustment)))

which\_is\_adiustable(Bid\_Reasons,Ask\_Reasons,ask) (member(BidReasons,limit\_order) AND NOT (member(Ask\_Reasons,lımit\_order))) OR(member(Bid\_Reasons,override) AND NOT (member(Ask.\_Reasons,override))) OR(member(Bid\_Reasons,position\_adjustment) AND NOT (member(Ask\_Reasons.position\_adjustment)))

## which\_\_is\_adjustable(Bid\_Reasons,Ask\_Reasons,both)

make\_amex\_adjustment(Option,Quote\_\_Bid,Quote.\_Ask,Max,Min,Problem,neither) post\_warning(amex\_rule\_\_violation)

make\_amex\_adjustment(Option,Quote\_\_Bid,Quote\_Ask,Max,Min,toosmall,bid) ← New\_Bid = Ask - Min AND New\_\_Bid > = 0 AND post(current\_\_recommendation(Option,New\_Bid,Quote\_Ask))

make\_amex\_adjustment(Option,Quote\_Bid,Quote\_Ask,Max.Min,toosmall,bid) ← New.Ask = Min AND post(current\_recommendation(Option,0,New\_Ask))

make\_amex\_adjustment(Option,Quote\_Bid,Quote\_Ask,Max,Min,toosmall,ask) ← NewAsk = Bid + Min AND post(current\_recommendation(Option,Quote\_Bid,New\_Ask))

TABLE 5 (cont'd)  
```csv
make_amex_adjustment(Option,Quote_Bid,Quote_Ask,Max,Min,toobig,bid) ←
    New_Bid = Ask - Max
    AND    New_Bid >= 0
    AND    post(current_recommendation(Option,New_Bid,Quote_Ask))
    make_amex_adjustment(Option,Quote_Bid,Quote_Ask,Max,Min,toobig,bid) ←
    New_Ask = Max
    AND    post(current_recommendation(Option,0,New_Ask))
    make_amex_adjustment(Option,Quote_Bid,Quote_Ask,Max,Min,toobig,ask) ←
    New_Ask = Bid + Max
    AND    post(current_recommendation(Option,Quote_Bid,New_Ask))
    make_amex_adjustment(Option,Quote_Bid,Quote_Ask,Max,Min,toosmall,both) ←
    New_Ask = Bid + Min
    AND    post(current_recommendation(Option,Quote_Bid,New_Ask))
    make_amex_adjustment(Option,Quote_Bid,Quote_Ask,Max,Min,toobig,both) ←
    New_Ask = Bid + Max
    AND    post(current_recommendation(Option,Quote_Bid,New_Ask))
```

minimum profit of \$0.50. If the stock price is above \$50 at option expiration, the call option will be exercised and the stock sold at \$50 (the strike price of the call). The put will expire since the stock price is \$50 or above. The cost of the position was \$49.50 and the profit is \$0.50.

If the stock price is below \$50 at option expiration, the arbitrageur would exercise his put and sell the stock for \$50 while the call expires as worthless. Again, the guaranteed profit is \$0.50. Of course, this example assumes no transactions costs and carrying costs.

The arbitrage rules in Table 6 check across options series for arbitrage possibilities; note that the conversion above involves a put and a call. While all other AESOP rules apply to a single series, the arbitrage rules must check across series. These rules compute a cost of carrying a position based on daily interest rates and warn the specialist if an arbitrage opportunity exists. Generally arbitrage opportunities are created when quotes have been adjusted due to limit orders.

Since the specialist may respond in any number of ways to an arbitrage situation, AESOP restricts itself to alerting him to the possibility. By using the trace function in the interface, the user can display a pop-up window explaining exactly what the potential is and the nature of the arbitrage, e.g., a conversion.

## 6. Evaluation

AESOP was used on an experimental basis for two months by a specialist who works with ihe expert who helped design the system. Literature on system implementation (Lucas 1981) suggests that one measure of success for a voluntary system is use. AESOP is clearly a voluntary system; since it contains the previously used Black-Scholes computation and inventory system in its entirety, the specialist could ignore the expert part of the system and work from a report of theoretical prices for different stock price ranges. However, the specialist used the system with enthusiasm and provided a great deal of feedback during the experimental period.

It is possible that the system provided the specialist with some insights on the pricing decision. However, the specialists using the system were veterans; they generally understood the system's recommendations by glancing at limit orders or recalling their own spread rules. It is possible that a system like AESOP could be valuable in training a new specialist who could use the system to gain insights on pricing.

TABLE 6 Arbitrage Rules  
```csv
Arbitrage Rules

check_for_arbitrage ←
box_arbitrage_check
AND conversion_arbitrage_check
AND dividend_arbitrage_check
AND discount_arbitrage_check

box_arbitrage_check ←
quote(put,Month,Strike1,Put_Bid1,Put_Ask1)
AND quote(call,Month,Strike1,Call_Bid1,Call_Ask1)
AND next_higher_quote(put,Month,Strike1,Strike2,Put_Bid2,Put_Ask2)
AND quote(call,Month,Strike2,Call_Bid2,Call_Ask2)
AND Strike_Increment = Strike2 - Strike1
AND box_arbitrage_potential1(Month,Strike1,Call_Ask1,Call_Bid2
Put_Ask2,Put_Bid1,Strike_Increment)
AND box_arbitrage_potential2(Month,Strike1,Call_Bid1,Call_Ask2
Put_Bid2,Put_Ask1,Strike_Increment)

box_arbitrage_potential1(Month,Strike1,Call_Ask1,Call_Bid2
Put_Ask2,Put_Bid1,Strike_Increment) ←
(Call_Ask1 - Call_Bid2) + (Put_Ask2 - Put_Bid1) < Strike_Increment

box_arbitrage_potential2(Month,Strike1,Call_Bid1,Call_Ask2
Put_Bid2,Put_Ask1,Strike_Increment) ←
(Call_Bid1 - Call_Ask2) + (Put_Bid2 - Put_Ask1) > Strike_Increment

conversion_arbitrage_check ←
global_facts(Stockprice.Dividend,Xdiv_Days,Daily_Interest,Percentage)
AND quote(put,Month,Strike,Put_Bid,Put_Ask)
AND quote(call,Month,Strike,Call_Bid,Call_Ask)
AND days_to_expiration(Num_Days)
AND dividend(Num_Days,Xdiv_Days Dividend,Actual_Dividend)
AND Carry1 = Strike*Daily_Interest*Num_Days
AND conversion_arbitrage_potential(Month,Strike,Call_Bid,Put_Ask,
Actual_Dividend,Stockprice,Carry1)
AND Carry2 = Carry1*Percentage
AND reversal_arbitrage_potential(Month,Strike,Put_Bid,Call_Ask,
Actual_Dividend,Stockprice,Carry2)

conversion_arbitrage_potential(Month,Strike,Call_Bid,Put_Ask,Dividend,Stockprice,Carry) ←
Strike + Call_Bid + Dividend - Stockprice - Put_Ask - Carry > 0

reversal_arbitrage_check(Month,Strike,Put_Bid,Call_Ask,Dividend,Stockprice,Carry) ←
Stockprice + Put_Bid - Strike - Call_Ask - Dividend + Carry > 0

dividend_arbitrage_check ←
global_facts(Stockprice,Dividend,Xdiv_Days,Daily_Interest)
quote(put,Month,Strike,Quote_Ask)
AND Carry = (Ask + Stockprice) * Daily_Interest * Xdiv_Days
AND dividend_arbitrage_potential(Month,Strike,Quote_Ask,Stockprice,Carry.Dividend)

dividend_arbitrage_potential(Month,Strike,Quote_Ask,Stockprice,Carry.Dividend) ←
Ask + Stockprice + Carry < Strike + Dividend

discount_arbitrage_check ←
global_facts(Stockprice,Dividend,Xdiv_Days,Daily_Interest)
AND quote(put,Month,Strike,_Put_Ask)
AND quote(call,Month,Strike,_Call_Ask)
AND disc_arb_put_potential(Month,Strike,Put_Ask,Stockprice)
AND disc_arb_call_potential(Month.Strike,Call_Ask,Stockprice)

disc_arb_put_potential(Month.Strike,Put_Ask,Stockprice) ←
Put_Ask + Stockprice < Strike

disc_arb_call_potential(Month.Strike,Call_Ask,Stockprice) ←
Call_Ask + Strike < Stockprice
```

O'Leary (1987) has proposed a framework for validating expert systems. He suggests that validation should test what the system knows and does not know, and what it knows incorrectly. The validation of AESOP included a number of the techniques O'Leary recommends. In particular, the expert was heavily involved in the definition of the rules which is one approach to establishing content validity. Repeated testing and use on the exchange floor demonstrated reliability; the system produced the same recommendations given the same input conditions.

O'Leary contends that “the primary criterion for system validation is the relationship between the decisions developed by the system and decisions developed by human experts" (criterion validity). O'Keefe et al. (1987) suggest a similar approach to validation which emphasizes acceptable performance and suggests that one cannot expect perfect results since the human decision maker is imperfect. Similar approaches are recommended or have been used in the past to validate expert systems: for example see the papers in Gupta (1991).

AESOP's recommended prices were compared with the prices posted by the expert specialist on various days when the system was in use at the exchange. To evaluate the criterion validity and the performance of the system in general, the designers logged all user input for a sample of different days over a one-month period. For each of these days, the exchange provided an audit trail of posted quotations for the specialist's option. The two sources of data were combined and sorted into time sequence by day.

Programs compared AESOP's recommendations with the actual price posted by the specialist. It was assumed that the AESOP recommendations were valid for 30 minutes; changes within 30 minutes of an AESOP run were considered to be influenced by the system. Changes past 30 minutes beyond an AESOP run were assumed to come from trades or market conditions. (It is fairly common to change quoted prices immediately after a trade.)

Figure 3 compares AESOP's recommendations with the actual quotes posted by the specialist for calls with an ask price in eighths. The graph presents the number of times the specialist posted what AESOP recommended (the “=" column in Figure 3) and a distribution for the number of increments by which the specialist's and AESOP's quotes differed. As an example, Figure 3 shows that 269 times the specialist posted the ask price in eighths recommended by AESOP; 151 times the specialist raised the recommended by by  and 256 times he lowered it by . Figure 4 provides a similar graph for put bid prices in eighths.

The same analysis was performed for both puts and calls with prices in eighths and sixteenths. 'Table 7 summarizes the results showing when AESOP either equaled or was within one increment of the price eventually posted by the specialist (within 30 minutes of an AESOP run). It appears from Table 7 that AESOP performs best on calls; there is more trading activity in calls than in puts. AESOP also performs better on eighths than sixteenths which seems reasonable as it is more difficult to select the “right price" out of 16 increments than out of 8.

Looking over all of the data and graphs, it was clear that AESOP tended to recommend a call price that was too high and a put price that was too low. These biases are consistent with the known biases of the Black-Scholes pricing model. In the case of puts, especially those out of the money and in a far out month, the specialist posted high prices to discourage trading. Observations on the floor of the Exchange also suggested that the specialist generally changed prices with each transaction without referring to any pricing model; in this case the “market" was determining the price.

Clifford • Lucas • Srikanth  
![](/api/attachments/KDG34Y4S/fulltext/images/ae9a1acc2791d1d6b925a348f906e6933cd9cd1edfe5f5e0412a7f88706b27ec.jpg)  
FiGURE 3. Calls Ask Price in Eighths

![](/api/attachments/KDG34Y4S/fulltext/images/d678b4dbbfdaeaa5a281811078808955dc773ee7d19eff69de01921ca82137a2.jpg)  
FiGURE 4. Puts Bid Price in Eighths.

TABLE 7  
Percentage of AESOP Quotattons Equal to or W ithn One Increment of Quotauon Posted by the Specialtsı

<table><tr><td colspan="2"></td><td>Eighths</td><td>Sixteenths</td></tr><tr><td rowspan="2">CALLS</td><td>Bid</td><td>52%</td><td>44%</td></tr><tr><td>Ask</td><td>48%</td><td>45%</td></tr><tr><td rowspan="2">PUTS</td><td>Bid</td><td>50%</td><td>27%</td></tr><tr><td>Ask</td><td>47%</td><td>37%</td></tr></table>

All of the evidence indicates that AESOP represents an improvement over the regular Black-Scholes model. With the exception of puts priced in sixteenths, almost half the time the AESOP recommendation was equal to or within one increment of what the specialist actually posted.

The American Stock Exchange is installing a touch-screen system for posting specialist quotations; it is connected directly to the official price displays (unlike AESOP). The specialist who has used both AESOP and the AMEX system has indicated that AESOP's pricing rules come closer to what he posts than the exchange system, despite the fact that the AMEX system allows the user to choose different options pricing models and different parameters for each series. Discussions are currently underway with the Exchange to transfer the AESOP knowledge base to the touch-screen system.

Given a 1 of the arguments above, it seems safe to conclude that this research was successful in building an integrated mathematical and symbolic model. The system did recommend prices that were much closer to the specialist's final quotations than the mathematical model alone. In addition, the system functioned successfully in the demanding environment of a stock exchange trading floor.

## 7. Conclusions

The purpose of this research was (1) to develop a system which integrated mathematical and symbolic models to support a particular decision-maker's pricing strategy, and (2) to show that such a system could function in a difficult, real-time environment. The success of the system suggests that integrating symbolic and mathematical models is an excellent way to support decision-makers. Each model makes a unique contribution to the recommendations made to the user. For this type Il integration, the strength of the mathematical model is its ability to clearly express a theoretical solution. The symbolic model makes it possible to adjust a theoretical solution to the domain of a decision maker; it strengthens the interface between theory and reality. The integrated model does not require sophisticated mathematical and decision theory tools and it relates to the way the decision maker thinks about his or her problem.

In the case of AESOP a number of rules exist in the problem domain; some come from the stock exchange while others are decision rules used by the specialist. The Black-Scholes model provides a theoretical price estimate while the symbolic model recommends bid and ask prices for posting in the marketplace. The AESOP experience provides evidence that the integration of symbolic and mathematical models offers great promise for matching models to specific problem domains.\*

Acknowledgements. The authors wish to thank Professors Vasant Dhar and Rob Weitz, and Robert Schwartz and the anonymous referees for their comments on an earlier draft of this paper.

## References

Alter, S., Dectston Support Systems, Addison-Wesley, Reading, MA, 1980.

Black, F. and M. Scholes, “The Pricing of Options and Corporate Liabilities," Journal of Poltical Economy, 81, 3 (May-June 1973), 637–654.

Bouwman, M., “Human Diagnostıc Reasonıng by Computer' An Illustration for Financial Analysis," Management Sctence. 29, 6 (June 1983), 653–672.

Gupta, U., Valıdating and Verifyıng Knowledge-Based Systems, IEEE Press, Los Alamitos, CA, 1991.

Kowalık J. and C. Kitzmiller (Eds.), Couplıng Symbolıc and Numerical Computıng in Expert Systems II, North-Holland, Amsterdam, 1988.

Krishnan, R , “A Logic Modeling Language for Automated Model Construction," Dectston Support Sys tems, 6, 2 (1990), 123–152.

Lucas, H, C. Jr , Implementation, The Key to Successful Information Systems, Columbia Univ. Press, New York, 1981.

Ma, P., P F. Murphy and E. Stohr. “A Graphics Interface for Linear Programming," Communications of the ACM, 32, 8 (August 1989), 996-1012.

McMillan, L. G., Options as a Strategıc Investment, Institute of Finance, New York, 1986.

Nicklaus, D., K Overton, S. Tong and C. Russo, “Knowledge Representation and Technique for Engineering Design Automation," in Couplıng Symbolıc and Numerical Computing in Expert Systems II, North-Holland, Amsterdam, 1988

O'Keefe, R . O Balcı and E. Smith, “Validatıng Expert System Performance," IEEE Expert (Winter 1987),81-87

O'Leary, D., “Validation of Expert Systems with Applications to Auditing and Accounting Expert Systems," Decision Sctences, 18 (1987), 468–486.

Reitman, W. (Ed.), Artificial Intelligence Appltcations for Busıness, Ablex, Norwood, NJ, 1984.

Sprague, R. and E. Carlson, Butldıng Effective Dectston Support Systems, Prentice-Hall, Englewood Cliffs. NJ, 1982.

Turban, E. and P. Watkins, “Integrating Expert Systems and Decision Support Systems," MIS Quarterly, 10, 2 (June 1986), 159–177.

-, Dectston Support Systems and Expert Svstems, Macmillan, New York, 1988.

Weitz, R., “NOSTRADAMUS: A Knowledge-Based Forecasting Advisor," International Journal of Forecasting, 2, 3 (1986), 273–283.
