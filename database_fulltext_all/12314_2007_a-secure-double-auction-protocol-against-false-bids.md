---
otero_id: 12314
otero_key: "Y5674U2P"
title: "A secure double auction protocol against false bids"
authors: "JungHoon Ha; Jianying Zhou; SangJae Moon"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.03.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# A secure double auction protocol against false bids

JungHoon Ha <sup>a,⁎</sup>, Jianying Zhou <sup>b</sup>, SangJae Moon

<sup>a</sup> School of Electrical Eng. and Computer Science, Kyungpook National Univ., 1370, Sankyukdong, Pukgu, Daegu, South Korea <sup>b</sup> Institute for Infocomm Research (I<sup>2</sup>R), 21 Heng Mui Keng Terrace, 119613 Singapore

Received 12 September 2005; received in revised form 15 March 2007; accepted 25 March 2007 Available online 30 March 2007

## Abstract

M. Yokoo et al. analyzed some weaknesses in McAfee's double auction (MCD) protocol and proposed a robust threshold price double auction (TPD) protocol against false-name bids. Unfortunately, as their protocol strongly depends on the trust of auctioneer, the auctioneer's misbehavior may fail an auction process. In addition, their scheme is in fact not robust in terms of comprehensive false bids. In this paper, we further investigate weaknesses in both MCD and TPD protocols, and then propose an improved double auction protocol against false bids. We also extend it for a practical and secure double auction implementation. This is based on a hybrid trust model, where computation load is distributed to buyers and sellers while a semi-trusted manager handles the registration phase. A prominent feature of the extended protocol is its high robustness, achieved by using a publicly verifiable secret sharing scheme with threshold access structure. © 2007 Elsevier B.V. All rights reserved.

Keywords: Double auction; Signature of knowledge; False-name bids; Security

## 1. Introduction

Auctions are a popular model for commercial transactions with a long history. The Internet provides this traditional business practice with a new platform for more efficient transactions. Currently, many auction services exist on the Internet that satisfies a variety of requirements. Auction protocols can be classified into two types, namely one-sided auction protocols in which a single seller (or buyer) accepts bids from multiple buyers (or sellers), and two-sided or double auction protocols in which multiple buyers and sellers are permitted to bid/ask for designated goods [9]. (We use the term bid for a buyer's declaration of value, and ask for a seller's declaration of value).

For one-sided auctions, such as English auction, Vickrey auction and sealed-bid auction, there have been many papers in the literature considering various security properties [11–14,17,23]. However, not much research has been done regarding the security issues in double auctions. This is because the theoretical analysis is complicated since there exist multiple buyers and sellers in the double auction.

Recently, Wang and Leung [24] proposed a set of double auction protocols based on McAfee's [16] and Yokoo's [25] protocols. Their scheme possesses good security properties such as full privacy protection, public verifiability and robustness, by employing homomorphic ElGamal encryption and distributing the private key among the all participants. Unfortunately, it is not secure due to the original weakness in McAfee's and Yokoo's protocols.

In case of the scheme based on McAfee's protocol, the auctioneer cannot find out whether some malicious bidders have submitted false bids or not, while auction results can be varied according to auctioneer's profit in the scheme based on Yokoo's protocol.

In fact, Yokoo showed that McAfee's protocol is vulnerable against false name bids which are made under a fictitious name, and then proposed a robust threshold price double auction protocol against false name bids [25,26].

Unfortunately, as Yokoo's protocol strongly depends on the trust of auctioneer, auctioneer's misbehavior may fail an auction process. Even though the auctioneer is a non-trading agent who is not able to attend an auction process, he may desire to make more profit by choosing the relevant threshold r. In fact, the earnings of the auctioneer and the number of traders change with the threshold price r which he chooses. In addition, their scheme is not robust in terms of comprehensive false bids.

## 1.1. Present contribution and organization

Our main result is the first to analyze some weaknesses in both McAfee's and Yokoo's protocols, and then propose an improved double auction protocol against false bids, which excludes the possibility of false bids by giving the disadvantage to the participants submitting a false bid.

In the proposed scheme, the trading price and the number of traders are determined by demand and supply of buyers and sellers instead of threshold price of Yokoo's protocol, which reflects on a liberal economy and competitive pricing well.

Secondly, we extend our scheme for a practical and secure double auction implementation. This is based on a hybrid trust model with the relevant assumption. Trust and computation are distributed to buyers and sellers themselves in order to determine traders and trading price, so that the proposed protocol works well even when some buyers or sellers do not fulfill the auction process because of possible network problems or malicious behavior. In addition, a manager's misbehavior can be detected because of the monitor of buyers and sellers.

The rest of this paper is structured as follows. Section 2 describes McAfee's double auction protocol and analyzes its weakness. In Section 3, we review Yokoo's threshold price double auction protocol and analyze its weakness. Section 4 presents the improved double auction protocol against false bids and extends it for a secure and practical double auction implementation in Section 5. We analyze security and efficiency of our protocol in Section 6. Finally, Section 7 contains our conclusions and future works.

## 2. MCD protocol

In this section, we first describe McAfee's double auction protocol [16] and then analyze its weakness. We call this protocol the MCD protocol.

## 2.1. Protocol description

Let declared buyers' valuations (bids) be $b _ { 1 } , . . . , b _ { m }$ and declared sellers' valuations (asks) be $a _ { 1 } , . . . , a _ { n } ,$ , where

$$
b _ {(1)} \geq b _ {(2)} \geq \dots \geq b _ {(m)} \text { and } a _ {(1)} \leq a _ {(2)} \leq \dots \leq a _ {(n)}
$$

Please note the different orderings for buyers' and sellers' valuations. We use the notation (i) for the i-th highest valuation of buyers and the i-th lowest valuation of sellers. Choose k so that $b _ { ( k ) } \geq a _ { ( k ) }$ and $b _ { ( k + 1 ) } { < } a _ { ( k + 1 ) }$ hold. Since for (1) to (k), the evaluation value of the buyers is larger than that of the sellers, at most k trades are possible. The candidate of a trading price $p _ { \mathrm { t } }$ is defined as

$$
p _ {t} = \frac {1}{2} (b _ {(k + 1)} + a _ {(k + 1)})
$$

The MCD protocol works as follows,

• If $a _ { ( k ) } \le p _ { \mathrm { t } } \le b _ { ( k ) }$ holds: the buyers/sellers from (1) to (k) trade at price $p _ { \mathrm { t } }$ .

• If $p _ { \mathrm { t } } { > } b _ { ( k ) }$ or $\mathrm { \Omega } p _ { \mathrm { t } } { < } a _ { ( k ) }$ holds: the buyers/sellers from (1) to $( k - 1 )$ trade. Each buyer pays $b _ { ( k ) } .$ , and each seller gets $a _ { ( k ) }$

If the second condition holds, since the price for buyers $b _ { ( k ) }$ is larger than the price for sellers $a _ { ( k ) } ,$ , the amount $( k - 1 ) \cdot ( b _ { ( k ) } - a _ { ( k ) } )$ is left over. It is usually assumed that the auctioneer receives this amount.

## 2.2. Weakness in MCD scheme

M. Yokoo described that the MCD protocol is vulnerable against false name bids which are made under a fictitious name, such as using multiple e-mail address [25,26]. However, these malicious actions can be easily prevented by limiting multiple submission using entity authentication of registration phase and cryptographic devices. We will explain it in Section 5.

In addition, MCD protocol has another weakness. To explain it, we expand the meaning of the false name bids. That is, we define the word, comprehensive false bids, in which buyers or sellers submit even higher or lower bids than their true valuations to succeed in auction, but they in fact aren't willing to pay these valuations. Hereinafter, the word false bids will be used including both comprehensive false bids and false name bids for the sake of convenience. To have a clear understanding, we consider a simple example.

Example 1. Let us assume the true valuations of buyers and sellers are as follows.

• Buyers' valuations: $2 0 { > } 1 8 { > } 1 6 { > } 1 4$

• Sellers' valuations: $1 3 < 1 5 < 1 7 < 1 9$

If each participant truthfully declares his valuation, the first condition of the MCD protocol holds, and buyers and sellers from (1) and (2) trade at the price $p _ { \mathrm { t } } { = }$ $( 1 6 + 1 7 ) / 2 = 1 6 . 5 .$

On the other hand, if the buyer submits a very high bid 100 instead of 14 to succeed in an auction, the declared valuations become as follows.

• Buyers' valuations: $1 0 0 { > } 2 0 { > } 1 8 { > } 1 6$

• Sellers' valuations: $1 3 < 1 5 < 1 7 < 1 9$

In this case, the number of traders<sup>1</sup> changes and the buyer submitting 100 instead of 14 becomes a trader, but he just pays the trading price $p _ { \mathrm { t } } { = } ( 1 6 { + } 1 9 ) / 2 { = } 1 7 . 5$ instead of 100. We can consider his bidding as false bid in comprehensive meaning because the buyer submitted it to just succeed in auction. If the buyer asserts that his bidding is true valuation, we have no idea but to trust him.

As another example, consider the seller submitting 2 instead of 19. In fact, she does not want to sell some goods at the price 2.

• Buyers' valuations: $2 0 { > } 1 8 { > } 1 6 { > } 1 4$

• Sellers' valuations: $2 < 1 3 < 1 5 < 1 7$

In this case, the number of traders changes and the seller submitting 2 becomes a trader. People can think her bidding false because she submitted a very low valuation compared with valuations of other sellers. Unfortunately, since there is no proof to explain her false valuation, we have to believe her, so that she can trade at the price $p _ { \mathrm { t } } \mathrm { = } ( 1 6 + 1 5 ) / 2 \mathrm { = } 1 5 . 5$

From the above Example 1, we know that whoever submits very high or low bid/ask can always become a trader, while he or she just pays or gets the reasonable price. Thus, any disadvantage has to be imposed for him or her submitting a false bid. We explain how to solve this problem in Section 4.

## 3. TPD protocol

In this section, we review Yokoo's threshold price double auction protocol [26] and analyze its weakness. We call this protocol the TPD protocol.

## 3.1. Protocol description

First, the auctioneer determines a threshold price r. Auctioneer is a non-trading agent who does not desire to buy or sell the goods. He determines this threshold price without consulting the declared valuations of buyers and sellers. The declared buyers' valuations are $b _ { 1 } , . . . , b _ { m }$ and declared sellers' valuations are $a _ { 1 } , . . . , a _ { n } ,$ where

$$
b _ {(1)} \geq \dots \geq b _ {(i)} \geq r > b _ {(i + 1)} \geq \dots \geq b _ {(m)},
$$

$$
a _ {(1)} <   \dots \leq a _ {(j)} \leq r <   a _ {(j + 1)} \leq \dots a _ {(n)}
$$

TPD protocol is defined as follows,

• When $i = j \colon$ the buyers and sellers from (1) to (i) trade at the price r.

• When $i { > } j \colon$ the buyers and sellers from (1) to ( j) trade. Each buyer pays $b _ { ( j + 1 ) }$ and each seller gets r. The auctioneer gets the amount of $j ( b _ { ( j + 1 ) } - r )$

• When $i { < } j { \mathrm { : } }$ the buyers and sellers from (1) to (i) trade. Each buyer pays r and each seller gets $a _ { \mathrm { i + 1 } }$ . The auctioneer gets the amount of $i ( r - a _ { ( \mathrm { i + 1 } ) } )$

## 3.2. Weakness in TPD scheme

TPD protocol also has the same weakness as we described in Section 2.2. Here, we describe another weakness in TPD protocol. TPD protocol makes two assumptions about the auctioneer, that is, the auctioneer is a non-trading agent and determines the threshold price without consulting with buyers and sellers. Even though the auctioneer cannot attend an auction process, he may desire to make more profit by choosing the relevant threshold price r. We give an example where the earnings of the auctioneer and the number of traders change with the threshold price r which the auctioneer chooses.

Example 2. We use the same example of TPD protocol [26]. Let us assume the true valuations of buyers and sellers are as follows.

• Buyers' valuations: $9 { > } 8 { > } 7 { > } 4 0$

• Sellers' valuations: $2 < 3 < 4 < 1 2$ • When the auctioneer chooses r as $^ { 6 , }$ because this corresponds to case 1 of TPD protocol, the buyers and sellers from (1) to (3) trade at the price $r { = } 6 .$ . At this time, the auctioneer cannot have any profit by the rules of TPD protocol.

• When the auctioneer chooses r as 3.5, because this corresponds to case 2 of TPD protocol, the buyers and sellers from (1) to (2) trade. Each seller gets the threshold price $r { = } 3 . 5$ and each buyer pays 7. At this time, the auctioneers gets the profit $2 \cdot ( 7 - 3 . 5 ) { = } 7$

• When the auctioneer chooses r as 8.5, because this corresponds to case 3 of TPD protocol, only one buyer and seller can trade. The buyer pays the threshold price $r { = } 8 . 5$ and the seller gets 3. At this time, the auctioneers gets the profit $1 \cdot ( 8 . 5 - 3 ) { = } 5 . 5 $

In the above Example 2, the auctioneer's profit depends on his selection of the threshold price $r ,$ so that the auctioneer will determine the threshold price r as 3.5 to get maximum profit. In fact, the auctioneer can choose another threshold price r by considering not only above 3 cases but also other cases. In TPD protocol, since the threshold price is released after all participants have bidden, the auctioneer can choose the relevant r to make more earnings. His action can determine not only his own earnings but also the number of traders. That is, the number of traders including both winning buyers and sellers is 6, 4, 2 in cases 1, 2, 3 respectively. Even though many buyers and sellers participate in the auction process, the number of traders can be limited by the auctioneer due to his profit. In fact, this property is not desirable because the trading price does not depends on the demand and supply of buyers and sellers but is determined by the auctioneer's profit.

## 4. Improved double auction protocol against false bids

In this section, we propose an improved double auction protocol against false bids and verify it by means of an example.

## 4.1. Notation

<table><tr><td> $B_{i}$ </td><td>an identity of  $i$ -th buyer ( $i=1,..,m$ )</td></tr><tr><td> $b_{i}$ </td><td>a bid of  $B_{i}$ </td></tr><tr><td> $S_{j}$ </td><td>an identity of  $j$ -th seller ( $j=1,..,n$ )</td></tr><tr><td> $a_{j}$ </td><td>an ask of  $S_{j}$ </td></tr><tr><td> $\mathcal{P}_{B_{i}}$ </td><td>a payment of  $B_{i}$ </td></tr><tr><td> $\mathcal{I}_{S_{j}}$ </td><td>an income of  $S_{j}$ </td></tr><tr><td> $\mathcal{U}_{B_{i}},\mathcal{U}_{S_{j}}$ </td><td>utility of  $B_{i}$  and  $S_{j}$ , respectively</td></tr><tr><td> $\mathcal{E}_{A}$ </td><td>earnings of auctioneer</td></tr><tr><td> $p_{s}$ </td><td>standard price</td></tr></table>

## 4.2. Protocol description

To reflect a liberal economy and competitive pricing well, our scheme is based on the demand and supply of buyers and sellers instead of threshold price. Our scheme is in fact based on MCD protocol, but we change the terms of payment and income for buyers and sellers, and add some notations for a definite analysis. That is, to explain an advantage of buyer, seller and auctioneer by an auction, we define both utility of participants, , and earnings of an auctioneer, . We call this protocol the improved MCD protocol.

Let a declared valuation of buyer $B _ { i }$ be $b _ { i } \left( b i d \right)$ and a declared valuation of seller $S _ { j }$ be $a _ { j } \left( a s k \right)$ , where $i = 1$ m and $j = 1 , . . . , n$ . The submitted $b _ { i }$ and $a _ { j }$ are rearranged in the prices. At this time, to avoid the notation confusion, we use $b _ { ( i ) }$ and $a _ { ( j ) }$ for rearranged bids and asks, respectively. The declared valuations are as follows:

$$
\begin{array}{l} b _ {(1)} \geq \ldots \geq b _ {(f)} \geq \ldots \geq b _ {(m)}, \\ a _ {(1)} \leq \ldots \leq a _ {(f)} \leq \ldots \leq a _ {(n)} \end{array}
$$

Please note the different orderings for buyers' and sellers' valuations. We use the notation $( f )$ for the f-th highest valuation of buyers and the f-th lowest valuation of sellers. Let the buyer corresponding to $b _ { ( f ) }$ be $B _ { ( f ) }$ and the seller corresponding to $a _ { ( f ) }$ be $S _ { ( f ) } .$ . Choose k so that $b _ { ( k ) } \geq a _ { ( k ) }$ and $b _ { ( k + 1 ) } < a _ { ( k + 1 ) }$ hold. Since for (1) to $( k )$ , the evaluation value of the buyers is larger than that of the sellers, at most k trades are possible. To set a standard for trading price, we define standard price as follows:

$$
p _ {\mathrm{s}} = \frac {1}{2} (b _ {(k + 1)} + a _ {(k + 1)})
$$

The improved MCD protocol works as follows,

• If $a _ { ( k ) } \le p _ { \mathrm { s } } \le b _ { ( k ) }$ holds, the trade corresponding to the buyers/sellers from (1) to (k) is possible.

• Each buyer $B _ { ( f ) }$ pays $\mathcal { P } _ { B _ { ( f ) } } = \frac { 1 } { 2 } \left( b _ { ( f ) } + p _ { \mathrm { s } } \right)$ and gets a utility $\mathcal { U } _ { B _ { ( f ) } } { = } b _ { ( f ) } { - } \mathcal { P } _ { B _ { ( f ) } } { = } \frac { 1 } { 2 } ( \bar { b _ { ( f ) } } { - } p _ { \mathrm { s } } ) ,$

• Each seller $S _ { ( f ) }$ gets $\begin{array} { r } { \mathbb { Z } _ { S _ { ( f ) } } = \frac { 1 } { 2 } \left( a _ { ( f ) } + p _ { \mathrm { s } } \right) } \end{array}$ and a utility $\begin{array} { r } { \mathcal { U } _ { S _ { ( f ) } } = \mathcal { T } _ { S ( f ) } - a _ { ( f ) } = \frac { 1 } { 2 } ( p _ { \mathrm { s } } - a _ { ( f ) } ) , } \end{array}$

• The auctioneer gets $\begin{array} { r } { \mathcal { E } _ { A } { = } \sum _ { f { = } 1 } ^ { k } \mathcal { P } _ { B _ { ( f ) } } { - } \sum _ { f { = } 1 } ^ { k } \mathcal { T } _ { S _ { ( f ) } } { = } } \end{array}$ $\begin{array} { r } { \sum _ { f = 1 } ^ { k } \frac { 1 } { \gamma } ( b _ { ( f ) } - a _ { ( f ) } ) } \end{array}$ , where $f { \overset { \cdot } { = } } 1 , . . . , k .$

• If $p _ { \mathrm { s } } { > } b _ { ( k ) }$ or ${ p _ { \mathrm { s } } } ^ { < } a _ { ( k ) }$ holds, the buyers/sellers from (1) to $( k - 1 )$ trade.

• Each buyer $B _ { ( f ) }$ pays $\mathcal { P } _ { B _ { ( f ) } } = \textstyle { \frac { 1 } { 2 } } ( b _ { ( f ) } + p _ { \mathrm { s } } )$ and gets a utility $\begin{array} { r } { \mathcal { U } _ { B _ { ( f ) } } b _ { ( f ) } - \mathcal { P } _ { B _ { ( f ) } } = \frac { 1 } { \gamma } \left( b _ { ( f ) } - p _ { \mathrm { s } } \right) } \end{array}$

• Each seller $S _ { ( f ) }$ gets $\begin{array} { r } { \overline { { \mathcal { T } _ { S ( f ) } } } ^ { - } = \frac { 1 } { 2 } ( a _ { ( f ) } + p _ { \mathrm { s } } ) } \end{array}$ and a utility $\mathcal { U } _ { S _ { ( f ) } } { = } \mathcal { T } _ { S _ { ( f ) } } { - } a _ { ( f ) } { = } \frac { 1 } { 2 } ( \ p _ { \mathrm { s } } { - } a _ { ( f ) } { ) } ,$

• The auctioneer gets $\begin{array} { r } { \mathcal { E } _ { A } { = } \sum _ { f = 1 } ^ { k - 1 } \mathcal { P } _ { B _ { ( f ) } } { - } \sum _ { f = 1 } ^ { k - 1 } \mathcal { T } _ { S _ { ( f ) } } { = } } \end{array}$ $\begin{array} { r } { \sum _ { f = 1 } ^ { k - 1 } \frac { 1 } { 2 } ( b _ { ( f ) } - a _ { ( f ) } ) } \end{array}$ , where $f { \overset { \cdot } { = } } 1 , . . . , k { - } 1$

## 4.3. Example

In this section, we verify the robustness against false bids with an example.

Example 3. Let us assume the valuations are identical to Example 1.

• Buyers' valuations: $2 0 { > } 1 8 { > } 1 6 { > } 1 4$

• Sellers' valuations: $1 3 < 1 5 < 1 7 < 1 9$

In this case, because the standard price is $p _ { \mathrm { { s } } } =$ ${ \frac { 1 } { \gamma } } \left( 1 6 + 1 7 \right) = 1 6 . 5 ,$ buyers and sellers from (1) to (2) can trade. The buyers $B _ { 1 }$ and $B _ { 2 }$ pay $\mathcal { P } _ { B _ { 1 } } = 1 8 . 2 5$ and $\mathcal { P } _ { B _ { 2 } } = 1 7 . 2 5$ , respectively. The sellers $S _ { 1 }$ and $S _ { 2 }$ get ${ \mathcal { T } } _ { S _ { 1 } } { \stackrel { - } { = } } 1 4 . 7 5$ and $\mathcal { T } _ { S _ { 2 } } { = } 1 5 . 7 5$ , respectively. At this time, the earnings of the auctioneer are $\mathcal { E } _ { A } { = } 5$ . Table 1 represents all auction information related to Example 3. From Table 1, we know that the buyer submitting the higher bid has the higher utility though he makes more payment compared with another buyer. This is desirable because he has more advantage compared with his own valuation. The case of sellers is similar to that of buyers.

On the other hand, if the buyer submits a very high bid 100 instead of 14 to just succeed in an auction, the declared valuations become as follows. (Thus we will consider it as false bid).

• Buyers' valuations: $1 0 0 { > } 2 0 { > } 1 8 { > } 1 6$

• Sellers' valuations: $1 3 < 1 5 < 1 7 < 1 9$

In this case, the number of traders changes and the buyer submitting 100 instead of 14 becomes a trader, but he has to pay much higher $P _ { B _ { 4 } } { = } 5 8 . 7 5$ than other traders. Even though he has very high utility compared with other buyers, it is useless for him because his bidding 100 is false. As a result, the auctioneer can make more profit. Table 2 represents auction results for the false bid of buyer $B _ { 4 }$

Table 1  
Auction results when participants submit true valuations

<table><tr><td></td><td> $B_{(1)}$ </td><td> $B_{(2)}$ </td><td> $B_{(3)}$ </td><td> $B_{(4)}$ </td><td> $S_{(1)}$ </td><td> $S_{(2)}$ </td><td> $S_{(3)}$ </td><td> $S_{(4)}$ </td></tr><tr><td>Identity</td><td> $B_1$ </td><td> $B_2$ </td><td> $B_3$ </td><td> $B_4$ </td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_4$ </td></tr><tr><td> $b_{(f)}/a_{(f)}$ </td><td>20</td><td>18</td><td>16</td><td>14</td><td>13</td><td>15</td><td>17</td><td>19</td></tr><tr><td> $p_s$ </td><td colspan="8"> $(16+17)/2=16.5$ </td></tr><tr><td>Trader</td><td>Y</td><td>Y</td><td>N</td><td>N</td><td>Y</td><td>Y</td><td>N</td><td>N</td></tr><tr><td> $\mathcal{P}_{B_{(f)}}$ </td><td>18.25</td><td>17.25</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td></tr><tr><td> $\mathcal{I}_{S_{(f)}}$ </td><td></td><td></td><td></td><td></td><td>14.75</td><td>15.75</td><td>-</td><td>-</td></tr><tr><td> $\mathcal{U}_{B_{(f)}}$ </td><td>1.75</td><td>0.75</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td></tr><tr><td> $\mathcal{U}_{S_{(f)}}$ </td><td></td><td></td><td></td><td></td><td>1.75</td><td>0.75</td><td>-</td><td>-</td></tr><tr><td> $\mathcal{E}_A$ </td><td>5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table 2  
Auction results when the buyer $B _ { 4 }$ submits a false bid

<table><tr><td></td><td> $B_{(1)}$ </td><td> $B_{(2)}$ </td><td> $B_{(3)}$ </td><td> $B_{(4)}$ </td><td> $S_{(1)}$ </td><td> $S_{(2)}$ </td><td> $S_{(3)}$ </td><td> $S_{(4)}$ </td></tr><tr><td>Identity</td><td> $B_4$ </td><td> $B_1$ </td><td> $B_2$ </td><td> $B_3$ </td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_4$ </td></tr><tr><td> $b_{(f)}/a_{(f)}$ </td><td>100</td><td>20</td><td>18</td><td>16</td><td>13</td><td>15</td><td>17</td><td>19</td></tr><tr><td> $p_s$ </td><td colspan="8">(16+19)/2=17.5</td></tr><tr><td>Trader</td><td>Y</td><td>Y</td><td>Y</td><td>N</td><td>Y</td><td>Y</td><td>Y</td><td>N</td></tr><tr><td> $\mathcal{P}_{B_{(f)}}$ </td><td>58.75</td><td>18.75</td><td>17.75</td><td>-</td><td></td><td></td><td></td><td></td></tr><tr><td> $\mathcal{I}_{S_{(f)}}$ </td><td></td><td></td><td></td><td></td><td>15.25</td><td>16.25</td><td>17.25</td><td>-</td></tr><tr><td> $\mathcal{U}_{B_{(f)}}$ </td><td>41.25</td><td>1.25</td><td>0.25</td><td>-</td><td></td><td></td><td></td><td></td></tr><tr><td> $\mathcal{U}_{S_{(f)}}$ </td><td></td><td></td><td></td><td></td><td>2.25</td><td>1.25</td><td>0.25</td><td>-</td></tr><tr><td> $\mathcal{E}_A$ </td><td>46.5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

As another example, consider the seller submitting very low 2 instead of 19. In fact, she does not want to sell some goods at the price 2. (Thus we will consider it as false ask).

• Buyers' valuations: $2 0 { > } 1 8 { > } 1 6 { > } 1 4$

• Sellers' valuations: $2 < 1 3 < 1 5 < 1 7$

In this case, even though the seller $S _ { 4 }$ becomes a trader, she just can get the low income $\mathcal { T } \mathrm { { s } } _ { 4 } { = } 8 . 7 5$ compared with incomes of other sellers. Table 3 represents auction results for the false bid of seller $S _ { 4 }$

In the above Example 3, even though some participants by submitting a false bid or ask can become traders, they have to be willing to receive disadvantage. That is, buyers have to make more payment and sellers must accept much lower income. If participants are rational, they will not submit false bids as taking a risk of disadvantage, thus our proposed scheme is robust against false bids.

Table 3  
Auction results when the seller $S _ { 4 }$ submits a false bid

<table><tr><td></td><td> $B_{(1)}$ </td><td> $B_{(2)}$ </td><td> $B_{(3)}$ </td><td> $B_{(4)}$ </td><td> $S_{(1)}$ </td><td> $S_{(2)}$ </td><td> $S_{(3)}$ </td><td> $S_{(4)}$ </td></tr><tr><td>Identity</td><td> $B_1$ </td><td> $B_2$ </td><td> $B_3$ </td><td> $B_4$ </td><td> $S_4$ </td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td></tr><tr><td> $b_{(f)}/a_{(f)}$ </td><td>20</td><td>18</td><td>16</td><td>14</td><td>19</td><td>13</td><td>15</td><td>17</td></tr><tr><td> $p_s$ </td><td colspan="8">(14+17)/2=15.5</td></tr><tr><td>Trader</td><td>Y</td><td>Y</td><td>Y</td><td>N</td><td>Y</td><td>Y</td><td>Y</td><td>N</td></tr><tr><td> $\mathcal{P}_{B_{(f)}}$ </td><td>17.75</td><td>16.75</td><td>15.75</td><td>-</td><td></td><td></td><td></td><td></td></tr><tr><td> $\mathcal{I}_{S_{(f)}}$ </td><td></td><td></td><td></td><td></td><td>8.75</td><td>14.25</td><td>15.25</td><td>-</td></tr><tr><td> $\mathcal{U}_{B_{(f)}}$ </td><td>2.25</td><td>1.25</td><td>0.25</td><td>-</td><td></td><td></td><td></td><td></td></tr><tr><td> $\mathcal{U}_{S_{(f)}}$ </td><td></td><td></td><td></td><td></td><td>6.75</td><td>1.25</td><td>0.25</td><td>-</td></tr><tr><td> $\mathcal{E}_A$ </td><td>22</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 5. Extension of improved MCD protocol

In this section, we extend the improved MCD protocol to implement a secure and practical double auction protocol. For this, we first define some assumptions and explain trust model.

In fact, in most of the previous secure auction protocols, trust models can be classified into three types [8]. In the threshold trust model, there are m auctioneers, out of which a fraction are assumed to be trustworthy [13]. The third-party trust model assumes a third party who is not fully trusted but does not collude with other parties including auctioneers [1,5]. The buyer/seller self-resolving model distributes trust to all the buyers/ sellers [3,4]. These models might be selected based on the security requirements and the application environments. However, any of these trust models alone cannot achieve most of the requirements for secure double auction [19].

Thus, our proposed double auction protocol is a based on a hybrid model with the relevant assumptions. First, we distribute both trust and computation for the determination of traders and trading price to buyers and sellers themselves. With a publicly verifiable secret sharing scheme based on a threshold access structure, the proposed auction protocol works well even if some buyers or sellers do not fully corporate in an auction process due to an unstable network or malicious behaviors, so that it can achieve flexibility and robustness. Second, we make use of a semi-trusted manager, in which the manager is assumed not to release the pseudonyms of participants except at the identity announcement step of traders or because of user misbehavior. The manager may impersonate a valid trader and illegally attend an auction using an auction ticket of other participants. However, the manager's action can be monitored by buyers and sellers, thus his misbehavior can be detected.

## 5.1. Cryptographic primitive

## 5.1.1. Signature of knowledge

We use the signature of knowledge introduced by B. Lee et al. [14] as anonymous signature, in which they extended the signature of knowledge discrete logarithm introduced by Camenisch and Stadler [6].

That is, it can be used as an anonymous signature if $( \boldsymbol { y } ^ { r } ,$ $g ^ { r } )$ are challenged for a secret random number $r \in \mathbb { Z } _ { q }$ instead of $( y , g )$ of Camenisch and Stadler' scheme. The signer computes $( c , s )$ satisfying $c { = } h ( m \vert \vert y ^ { r } \vert \vert g ^ { r } \vert \vert ( g ^ { r } ) ^ { s } ( y ^ { r } ) ^ { c } )$ for challenged $( \boldsymbol { y } ^ { r } , \boldsymbol { g } ^ { r } )$ . We denote this signature as

$$
V = S K [ x: y ^ {r} = (g ^ {r}) ^ {x} ] (m),
$$

where SK represents both the proof of knowledge of the private key x and a signature on message m. Readers are referred to [14] for the technical details.

## 5.1.2. PVSS scheme

The extended protocol requires a publicly verifiable secret sharing (PVSS) scheme rather than a verifiable secret sharing (VSS) scheme [7,18]. In a VSS scheme, the objective is to resist malicious players such as

• a dealer sending incorrect shares to some or all of the participants, and

• participants submitting incorrect shares during the reconstruction phase.

In a PVSS scheme, however, it is an explicit goal that not just the participants can verify their own shares, but that anybody can verify that the participants received correct shares [22]. To allow for public verifiability in double auction, we employ Schoenmakers' PVSS [20] which is much simpler than other schemes [10,22]. Readers are referred to [20] for technical details.

## 5.2. Notation

We add the following parameters to Section 4.1's notation for implementing a secure and practical double auction protocol.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$T_{B_{i}}$  an auction ticket for  $B_{i}$ $T_{S_{j}}$  an auction ticket for  $S_{j}$ $Cert_{A}$  certificate of A issued by CA (Certification Authority)
 $Sig_{A}(m)$  digital signature of message m generated by entity A
 $(m_{1}\|\ldots\|m_{n})$  concatenation of n strings
 $H(m_{1}\|\ldots\|m_{n})$  one-way hash function with input strings  $m_{1},\ldots,m_{n}$
</div>

## 5.3. The extended double auction protocol

The extended double auction protocol consists of the following four phases: system set-up, registration, bid ask submission, and bid/ask opening.

## 5.3.1. System set-up

The entities include a manager M, m buyers $B _ { i }$ for $i \in \mathbb { Z } _ { m }$ and n sellers $S _ { j }$ for $j \in \mathbb { Z } _ { n }$ . The role of each entity is as follows:

## 5.3.1.1. Manager M.

• is semi-trusted party who is assumed not to release the pseudonyms of participants except at the identity announcement step of traders or because of user misbehavior.

• may impersonate a valid participant and illegally attend an auction using an auction ticket of other participants. However, the manager's action can be monitored by participants, thus his misbehavior can be detected.

• is in charge of the registration of buyers/sellers and provides each participant with an auction ticket as pseudonym.

• publishes the signature scheme, the public key for verification of signature and the certificate.

• releases $G _ { q }$ which has a group of prime order $q .$ • let $g$ denote the selected generator of $G _ { q }$

• announces the offer valuation range.

• let $L = \{ l _ { 1 } , . . . , l _ { w } \}$ be a set of w possible discrete bidding/asking prices.

• on behalf of participants, verifies the proofs of buyers and sellers and then determines the trading price and traders according to the auction rules.

## 5.3.1.2. Buyer $B _ { i } .$

• has private key $x _ { i }$ and the corresponding public key $y _ { i } { = } g ^ { x _ { i } }$ certified by CA.

• registers with the manager and receives an auction ticket $T _ { B _ { i } }$ from him.

• submits a bid in the submission phase and decrypts the encrypted shares of seller in the opening phase.

5.3.1.3. Seller $S _ { j } .$

• has private key $\tilde { x } _ { j }$ and the corresponding public key $\tilde { y } _ { j } { = } g ^ { \tilde { x } _ { j } }$ issued by $\mathrm { \overline { { C } } A } . ^ { 2 }$

• registers with the manager and receives an auction ticket $T _ { S _ { i } }$ from him.

• submits an ask in the submission phase and decrypts the encrypted shares of buyer in the opening phase.

In the proposed protocol, 4 bulletin boards are used, i.e., a registration bulletin board, a submission bulletin board, an opening bulletin board, and a trader announcement bulletin board. A bulletin board is a public communication channel which can be read by anybody but only be written by the legitimate party in an authentic way.

## 5.3.2. Registration phase

All buyer $B _ { i }$ and seller $S _ { j }$ register with the manager M as follows:

(1) $B _ { i }$ chooses a random number $r _ { i }$ and $k _ { i } \in \mathbb { Z } _ { q } \backslash \{ 0 \}$ and keeps them confidential.

(2) $B _ { i }$ computes $c _ { i } { = } H ( m _ { i } | | y _ { i } ^ { r _ { i } } | | g ^ { r _ { i } } | | g ^ { r _ { i } } )$ and $s _ { i } { = } r _ { i } ^ { - 1 } \cdot k _ { i } -$ $c _ { i } \cdot x _ { i } ,$ where $m _ { i } { = } ( B _ { i } | | \mathrm { C e r t } _ { B i } | |$ Buyer) and Buyer indicates that he wants to buy some goods.

(3) $B _ { i }$ sends $( m _ { i } , c _ { i } , s _ { i } , y _ { i } ^ { r _ { i } } , g ^ { r _ { i } } )$ to M secretely.

(4) The manager checks $c _ { i } { = } H ( m _ { i } | | y _ { i } ^ { r _ { i } } | | g ^ { r _ { i } } | | ( g ^ { r _ { i } } ) ^ { s _ { i } } \cdot ( y _ { i } ^ { r _ { i } } ) ^ { c _ { i } } ) .$

(5) After verifying the correctness of $( \boldsymbol { c } _ { i } , \ \boldsymbol { s } _ { i } )$ and authenticating the buyer, the manager computes $h _ { i } { = } H ( y _ { i } ^ { r _ { i } } )$ and $\nu _ { i } { = } \mathrm { S i g } _ { M } ( y _ { i } ^ { r _ { i } } | | h _ { i } )$ and generates an auction ticket $T _ { B _ { i } } { = } ( y _ { i } ^ { r _ { i } } | | h _ { i } | | \nu _ { i } )$ , and shuffles it on the registration bulletin board.

After the above registration, each buyer $B _ { i }$ can easily confirm whether his auction ticket is on that bulletin board or not. Because the auction ticket $T _ { B _ { i } }$ can be recognized only by the buyer who knows the relevant $y _ { i }$ and $r _ { i }$ for $T _ { B _ { i } ; }$ it could be used as a pseudonym for anonymity.

Similarly, seller $S _ { j }$ registers with the manager M and obtains her auction ticket $T _ { S _ { j } } { = } ( \tilde { y } _ { j } ^ { \tilde { r _ { j } } } | | \tilde { h _ { j } } | | \tilde { \nu } _ { j } )$ from the registration bulletin board.

## 5.3.3. Bid/ask—submission phase

Every buyer and seller first determines their own evaluation for an item traded by auction. Note that the proposed double auction protocol assumes w possible discrete bidding/asking price steps where w is sufficiently large. First, consider the submission from a buyer $B _ { i }$ Each buyer $B _ { i }$ chooses an evaluation $l _ { e } { \in } L , e { = } 1 , . . . , \nu$ w and selects a random polynomial $p _ { i } ( x )$ such that

$$
p _ {i} (x) = \prod_ {k = 0} ^ {t - 1} \alpha_ {k} x ^ {k} = \alpha_ {t - 1} x ^ {t - 1} + \ldots + \alpha_ {0},\tag{1}
$$

where $\mathsf { \Pi } \alpha _ { 0 } = l _ { e }$ and $t \leq n , n$ is the total number of sellers participating in the auction. The buyer $B _ { i }$ keeps this polynomial secret. Each buyer then computes shares $p _ { i } ( k ^ { + } 1 )$ for $0 \leq k \leq n - 1$ and encrypts them using the auction ticket of the seller, i.e., using the anonymous public key $\tilde { y } _ { j } ^ { \tilde { r _ { j } } }$ included in the auction ticket $T _ { S _ { i } }$ on the registration bulletin board. Then, the buyer $\mathring { B } _ { i }$ signs the encrypted shares including the pseudonym of sellers as follows:

$$
\begin{array}{l} V _ {B _ {i}} = S K [ x _ {i}: y _ {i} ^ {r _ {i}} = (g ^ {r _ {i}}) ^ {x _ {i}} ] (m _ {i}) \\ m _ {i} = ((T _ {S _ {0}}, (\widetilde {y} _ {0} ^ {\widetilde {r} _ {0}}) ^ {p _ {i} (1)}) | |... | | (T _ {S _ {n - 1}}, (\widetilde {y} _ {n - 1} ^ {\widetilde {r} _ {n - 1}}) ^ {p _ {i (n)}})), \end{array}
$$

and sends the signed message to the submission bulletin board. At this time, the buyer $B _ { i }$ should prove the correctness of the encrypted shares using the methods such as Chaum's proof of equality of discrete logarithm [7] or DLEQ protocol [20].

In a similar way, each seller S chooses the polynomial, computes shares and signs the message including both the encrypted shares and the auction tickets of buyers.

## 5.3.4. Bid/ask—opening phase

The bid/ask opening phase consists of the following four steps: decryption of encrypted shares, reconstruction of bid/ask, determination of the trading price and number of the traders, and identity announcement of traders.

5.3.4.1. Step 1: decryption of encrypted shares. Each participant first verifies the correctness of auction tickets related to the entities who have sent the messages. To have a clear understanding, we consider a simple example. Assume some buyers $B _ { 0 } , B _ { 1 }$ and $B _ { 2 }$ encrypted their shares $p _ { 0 } ( 1 ) , p _ { 1 } ( 1 )$ and $p _ { 2 } ( 1 )$ using an auction ticket $T _ { S _ { 0 } }$ in the bid submission phase, and they then submitted the encrypted shares to the submission bulletin board. For decryption of encrypted shares, the seller $S _ { 0 }$ first confirms whether her auction ticket exists in the messages that the buyers submitted to the submission bulletin board. After checking the integrity of her own auction ticket, she verifies the correctness of the auction tickets $T _ { B _ { 0 } } , T _ { B _ { 1 } }$ and $T _ { B _ { 2 } }$ corresponding to the buyers $B _ { 0 } , \ B _ { 1 }$ and $B _ { 2 }$ , respectively. If the verification is correct, she decrypts the encrypted shares $( \tilde { y } _ { 0 } ^ { \tilde { r } _ { 0 } } ) ^ { p _ { 0 } ( 1 ) }$ $( \tilde { y } _ { 0 } ^ { \tilde { r } _ { 0 } } ) ^ { p _ { 1 } ( 1 ) }$ and $( \tilde { y } _ { 0 } ^ { \tilde { r } _ { 0 } } ) ^ { p _ { 2 } ( \tilde { 1 } ) }$ using her secret keys $\tilde { \mathbf { X } } _ { 0 }$ and $\tilde { \mathrm { { r } } } _ { 0 }$ as follows:

$$
\begin{array}{l} ((\widetilde {y} _ {0} ^ {\widetilde {r} _ {0}}) ^ {p _ {0} (1)}) ^ {1 / \widetilde {x} _ {0} \widetilde {r} _ {0}} = ((g ^ {\widetilde {x} _ {0} \widetilde {r} _ {0}}) ^ {p _ {0} (1)}) ^ {1 / \widetilde {x} _ {0} \widetilde {r} _ {0}} = g ^ {p _ {0} (1)} \\ ((\widetilde {y} _ {0} ^ {\widetilde {r} _ {0}}) ^ {p _ {1} (1)}) ^ {1 / \widetilde {x} _ {0} \widetilde {r} _ {0}} = ((g ^ {\widetilde {x} _ {0} \widetilde {r} _ {0}}) ^ {p _ {1} (1)}) ^ {1 / \widetilde {x} _ {0} \widetilde {r} _ {0}} = g ^ {p _ {1} (1)} \\ ((\widetilde {y} _ {0} ^ {\widetilde {r} _ {0}}) ^ {p _ {2} (1)}) ^ {1 / \widetilde {x} _ {0} \widetilde {r} _ {0}} = ((g ^ {\widetilde {x} _ {0} \widetilde {r} _ {0}}) ^ {p _ {2} (1)}) ^ {1 / \widetilde {x} _ {0} \widetilde {r} _ {0}} = g ^ {p _ {2} (1)} \end{array}
$$

After decrypting the encrypted shares, the seller $S _ { 0 }$ signs the decrypted shares and releases the signed messages to the opening bulletin board. At this point, the signed message must include the proof that the decrypted shares are correctly computed, which is possible by a zero-knowledge such as DLEQ protocol [20] or Chaum's proof of equality of discrete logarithm [7]. The signed message is as follows:

$$
\begin{array}{l} V _ {S _ {0}} = S K [ \widetilde {x} _ {0}: \widetilde {y} _ {0} ^ {\widetilde {r} _ {0}} = (g ^ {\widetilde {r} _ {0}}) ^ {\widetilde {x} _ {0}} ] (\widetilde {m} _ {0}), \\ \widetilde {m} _ {0} = ((T _ {B _ {0}}, g ^ {p _ {0} (1)}) | | (T _ {B _ {1}}, g ^ {p _ {1} (1)}) | | (T _ {B _ {2}}, g ^ {p _ {2} (1)})) \end{array}
$$

Now, consider the decryption for the encrypted shares of sellers in a generalized case. Like the seller in the previous example, each buyer $B _ { i }$ verifies the messages and auction tickets of sellers, and decrypts the shares encrypted by them. Then he signs the message $m _ { i } { = } ( ( T _ { S _ { 0 } } , g ^ { \hat { \tilde { p } } _ { 0 ( i + 1 ) } } ) | | . . . | | ( T _ { S _ { n - 1 } } , g ^ { \tilde { p } _ { n - 1 } ( i + 1 ) } ) )$ , where $i \in \mathbb { Z } _ { m } ,$ and publishes it on the opening bulletin board.

5.3.4.2. Step 2: reconstruction of bid/ask. To recover an evaluation of each participant, at least t correctly decrypted shares are needed. After verifying the messages and proofs of sellers submitted in the previous step, on behalf of participants, the manager M recovers the evaluation $l _ { e }$ of buyer $B _ { i }$ using Lagrange interpolation (Suppose that t sellers produce correct values for $g ^ { p _ { i } ( k ) }$ , for $k { = } 1 , { \ldots } , t )$

$$
\prod_ {k = 1} ^ {t} \left(g ^ {p _ {i} (k)}\right) ^ {\lambda_ {k}} = g ^ {\sum_ {k = 1} ^ {t} p _ {i} (k) \lambda_ {k}} = g ^ {p _ {i} (0)},\tag{2}
$$

where $\scriptstyle \lambda _ { k } = \Pi _ { j \neq k { \frac { j } { j - k } } }$ is a Lagrange coefficient and $p _ { i } ( 0 ) =$ $l _ { e } .$ Because the manager holds w discrete bidding/ asking prices in the system set-up phase, he can precompute $g ^ { l e }$ for $e { = } 1 , . . . ,$ w so that he gets the evaluation $l _ { e }$ of the buyer from the above value $\bar { g } ^ { p _ { i } ( 0 ) }$

In the same way, the manager recovers the evaluation of each seller $S _ { j } .$

5.3.4.3. Step 3: determination of the trading price and number of the traders. In this step, the trading price and the number of traders are determined according to the improved MCD protocol of Section 4. All reconstructed bids and asks are rearranged in the price, and then are published in the opening board. The declared valuations are as follows:

$$
\begin{array}{c} T _ {B _ {(1)}}, b _ {(1)} \geq ... \geq T _ {B _ {(f)}}, b _ {(f)} \geq ... \geq T _ {B _ {(m)}}, b _ {(m)} \\ T _ {S _ {(1)}}, a _ {(1)} \leq ... \leq T _ {S _ {(f)}}, a _ {(f)} \leq ... \leq T _ {S _ {(n)}}, a _ {(n)} \end{array}
$$

Please note the different orderings for buyers' and sellers' valuation. We use the notation ( f ) for the f-th highest valuation of buyers and the f-th lowest valuation of sellers. Let the auction ticket corresponding to $b _ { ( f ) }$ be $T _ { B _ { ( f ^ { \prime } } }$ and another auction ticket corresponding to $a _ { ( f ) }$ be $T _ { S _ { ( f ) } } .$ By auction rules, the $k$ satisfying both $b _ { ( k ) } \geq a _ { ( k ) }$ and $b _ { ( k + 1 ) } < a _ { ( k + 1 ) }$ is chosen and the standard price is then defined as follows:

$$
p _ {\mathrm{s}} = \frac {1}{2} (b _ {(k + 1)} + a _ {(k + 1)})
$$

The trading price and the number of traders are determined as follows,

• If $a _ { ( k ) } \le p _ { \mathrm { s } } \le b _ { ( k ) }$ holds, the buyers and sellers corresponding to auction tickets from (1) to (k) can trade.

• Each buyer $B _ { ( f ) }$ corresponding to auction ticket $T _ { B _ { ( f ) } }$ pays $\mathcal { P } _ { B _ { ( f ) } } = { \frac { 1 } { 2 } } ( b _ { ( f ) } + p _ { \mathrm { s } } )$ and gets a utility ${ { \mathcal { U } } _ { { { B _ { ( f ) } } } } } =$ $b _ { ( f ) } - \mathcal { P } _ { B _ { ( f ) } } { = } \frac { 1 } { \gamma } ( b _ { ( f ) } - p _ { \mathrm { s } } ) .$

Each seller $\mathsf { \bar { S } } _ { ( f ) }$ corresponding to auction ticket $\mathcal { T } _ { S _ { ( f ) } }$ gets $\begin{array} { r } { \mathcal { T } _ { S _ { ( f ) } } = \frac { 1 } { 2 } ( a _ { ( f ) } + p _ { \mathrm { s } } ) } \end{array}$ and a utility ${ \mathcal U } _ { S _ { ( f ) } } =$ $\begin{array} { r } { \mathcal { T } _ { S _ { ( f ) } } - a _ { ( f ) } = \frac { 1 } { 2 } ( p _ { \mathrm { s } } - a _ { ( f ) } ) , } \end{array}$

• The manager gets $\begin{array} { r } { \mathcal { E } _ { A } = \sum _ { f = 1 } ^ { k } \mathcal { P } _ { B _ { ( f ) } } - \sum _ { f = 1 } ^ { k } \mathcal { T } _ { S _ { ( f ) } } = } \end{array}$ $\sum _ { f = 1 } ^ { k } \frac { 1 } { 2 } ( b _ { ( f ) } - a _ { ( f ) } ) ,$ , where $f { = } 1 , . . . , k .$

• If $p _ { \mathrm { s } } { > } b _ { ( k ) } ^ { - }$ or $p _ { \mathrm { s } } { < } a _ { ( k ) }$ holds, the buyers and sellers corresponding to auction tickets (1) to $( k - 1 )$ can trade.

• Each buyer $B _ { ( f ) }$ corresponding to auction ticket $\tau _ { B _ { ( f ) } }$ pays $\mathcal { P } _ { B _ { ( f ) } } = \frac { 1 } { \gamma } ( b _ { ( f ) } + p _ { \mathrm { s } } )$ and gets a utility $\mathcal U _ { B _ { ( f ) } } = b _ { ( f ) } - \mathcal P _ { B _ { ( f ) } } \stackrel { - } { = } \frac { 1 } { \gamma } ( b _ { ( f ) } - p _ { \mathrm { s } } )$

• Each seller $S _ { ( f ) }$ corresponding to auction ticket $\mathcal { T } _ { S _ { ( f ) } }$ gets ${ \overline { { \cal { T } } } } _ { S _ { ( f ) } } = { \frac { 1 } { 2 } } ( a _ { ( f ) } + p _ { \mathrm { { s } } } )$ and a utility $\mathcal { U } _ { S _ { ( f ) } } =$ $\begin{array} { r } { \mathbb { Z } _ { S _ { ( f ) } } - a _ { ( f ) } = \frac { 1 } { 2 } ( p _ { \mathrm { s } } - a _ { ( f ) } ) , } \end{array}$

• The manager gets $\begin{array} { r } { \mathcal { E } _ { A } = \sum _ { f = 1 } ^ { k - 1 } \mathcal { P } _ { B _ { ( f ) } } - } \end{array} \sum _ { f = 1 } ^ { k - 1 } \mathcal { T } _ { S _ { ( f ) } } =$ $\begin{array} { r } { \sum _ { f = 1 } ^ { k - 1 } \frac { 1 } { 2 } ( b _ { ( f ) } - a _ { ( f ) } ) } \end{array}$ , where $f { = } 1 , { \ldots } , k { - } 1$

## 5.3.4.4. Step 4: identity announcement of traders 5.3.4.4. Step 4: identity announcement of traders.

The manager releases the original identities of the traders on the trader announcement bulletin board. For public verification, he publishes the registration information $( { c _ { i } } ,$ $s _ { i } , m _ { i } { = } ( B _ { i } | | \mathrm { C e r t } _ { B _ { i } } | | \mathrm { B u y e r } )$ , y<sub>i</sub><sup>ri</sup>, $g ^ { r _ { i } } , T _ { B _ { i } } )$ related to winning buyers. Note that $( c _ { i } , \ s _ { i } , \ m _ { i } )$ are values used to authenticate an identity. Therefore, all entities including the lost participants or observers can identify the winning buyers. In the same way, the manager releases the registration information corresponding to the winning sellers, so that any entities can identify the traders.

## 6. Analysis

Here we perform an analysis of our extended protocol with respect to security and efficiency.

## 6.1. Security

The extended double auction protocol is based on intractability of discrete logarithm problem and a publicly verifiable secret sharing scheme with threshold access structure. First, we define the discrete logarithm problem (DLP).

Definition 1. Given g and $g ^ { x } \in G ,$ , determine the unique integer $x { \in } \mathbb { Z } _ { q } ,$ where $G = < g >$ be a single cyclic group with prime order q and $g$ is generator.

To solve the DL problem is assumed to be intractable [2,15,21].

## 6.1.1. Anonymity

We have assumed the semi-trusted manager who doesn't open the real identity during the auction process except at the identity announcement step of traders or because of user misbehavior, while he may try to illegally attend an auction by impersonating other participants. However, his misbehavior can be detected because of a monitoring of buyers and sellers. Thus, as long as the manager does not open the real identity, the anonymity is guaranteed by the following Lemma 1.

Lemma 1. Nobody, except the manager, can associate an auction ticket $T _ { B _ { i } }$ or $T _ { S _ { j } }$ with the real identity $B _ { i }$ or $S _ { j }$ of buyer or seller, respectively.

Proof. In the extended double auction protocol, the information related to an identity of participants is included in auction ticket, $T { = } ( \boldsymbol { y } ^ { r } | | h | | \nu )$ , where $h { = } H \left( y ^ { r } \right)$ $y = g ^ { x }$ and $\nu = \mathrm { S i g } _ { M } ( y ^ { r } | | h )$ . We suppose that an adversary A has sufficient certificate lists related to auction participants in the previous auctions. To break the anonymity and find the identity of a participant, the adversary tries to recover the y from the known $y ^ { r } ,$ and compares it with some certificate lists which he has collected. Let $y ^ { r } { = } y ^ { \prime }$ and $t { = } x \cdot r$ mod q. If can find t from $y { = } g ^ { t } ,$ , given y and $g ,$ he can also recover y from $y ^ { r }$ $\scriptstyle ( = g ^ { x \cdot r } )$ , however, which is impossible due to the intractability of discrete logarithm problem mentioned early. Therefore, cannot recover the original identity so that the anonymity is guaranteed in the extended double auction protocol.

## 6.1.2. Impossibility of impersonation

Since an anonymity service is guaranteed in the extended double auction protocol, an entity may try to illegally submit a faked bid or ask and impersonate a legal entity using the auction ticket of other participants. However, impersonation is technically impossible in our scheme, as shown in the following Theorem 1.

To induce Theorem 1, we first prove the following lemma.

Lemma 2. An attacker who intercepts the valid information of any participant such as $( \nu ^ { r } , g ^ { r } )$ and injects a faked bid or ask cannot generate a valid signature.

Proof. In the extended double auction protocol, every participant has to submit a signature $V { = } S K \ [ x { : } y ^ { r } { = } ( g ^ { r } ) ^ { x } ]$ $( m ^ { \prime } )$ with auction ticket $T { = } ( \boldsymbol { y } ^ { r } \| h \| \nu )$ for bidding. At this point, since v is the signature generated by the manager M and is released in registration bulletin board, it is impossible for an attacker to generate the specific $y ^ { r }$ and auction ticket himself. Therefore, the attacker tries to forge a signature using the intercepted information of participants. Suppose an attacker can generate a valid signature $( c ^ { \prime } , s ^ { \prime } )$ to inject a faked bid or ask message $m ^ { \prime }$ using the intercepted valid value $( \boldsymbol { \nu } ^ { r } , \boldsymbol { g } ^ { r } )$ . The attacker then releases $( m ^ { \prime } , c ^ { \prime } , s ^ { \prime } , y ^ { r } , g ^ { r } )$ , i.e., $V { = } S K \ [ x { : } y ^ { r } { = } ( g ^ { r } ) ^ { x } ]$ $( m ^ { \prime } )$ , on the submission bulletin board so that he can impersonate a legal entity corresponding to the parameter $y ^ { r } .$ To pass a successful signature verification, the following equation should be satisfied.

$$
c ^ {\prime} = H (m ^ {\prime} | | y ^ {r} | | g ^ {r} | | (g ^ {r}) ^ {s ^ {\prime}} \cdot (y ^ {r}) ^ {c ^ {\prime}})\tag{3}
$$

That is, the attacker generates $c ^ { \prime }$ as follows:

$$
c ^ {\prime} = H (m ^ {\prime} | | y ^ {r} | | g ^ {r} | | (g ^ {k ^ {\prime}})\tag{4}
$$

From Eqs. (3) and (4), the following equations are induced:

$$
g ^ {k ^ {\prime}} = (g ^ {r}) ^ {s ^ {\prime}} \cdot (y ^ {r}) ^ {c ^ {\prime}} = g ^ {r \cdot s ^ {\prime} + c ^ {\prime} x \cdot r}\tag{5}
$$

From Eq. (5), we know that needs to generate $k ^ { \prime }$ such that $k ^ { \prime } { = } r \cdot s ^ { \prime } { + } c ^ { \prime } { \cdot } x \cdot r .$ However, the only way to get both r and x is to find the discrete logarithm of $g ^ { r }$ and then to solve another discrete logarithm problem of $y ^ { r } =$ $( g ^ { x } ) ^ { r } { = } ( g ^ { r } ) ^ { x }$ , respectively. Since this is contradictory to the intractability of DLP under a group, our assumption that an attacker can generate a valid signature using the parameters $( \boldsymbol { y } ^ { r } , \boldsymbol { g } ^ { r } )$ of another entity is not valid.

Lemma 3. The manager also cannot impersonate a valid participant.

Proof. This can be proved straightforwardly by means of Lemma 2, so we will omit the detailed proof. □

From Lemmas 2 and 3, we can induce the following security theorem.

Theorem 1. Nobody, not even manager, can forge the valid signature to submit a faked bid or ask, thereby making the impersonation impossible in extended double auction protocol.

## 6.1.3. Non-repudiation

In extended double auction protocol, the signature of knowledge is used during auction process. Even though it guarantees the anonymity, no participant can deny his signature. First, we consider the registration phase. Suppose that a buyer B submits the following entity information $m { = } ( B | | C e r t _ { B } | | B u y e r )$ , signature pair $( c , \ s )$ and $( \boldsymbol { y } ^ { r } , \boldsymbol { g } ^ { r } )$ to the manager for registration, where $c = h$ $( m \| y ^ { r } \| g ^ { r } \| ( g ^ { r } ) ) ^ { s } ( y ^ { r } ) ^ { c } )$ . This signature is uniquely generated by an entity who only knows the relevant private key x and $r ,$ which is already identified in proof for Lemma 2. Since all information related to the registration is released on trader announcement step, any one cannot deny that he or she has submitted an ask or bid. Since the case of signature in bid/ask submission or bid/ ask opening phase is similar to the registration phase, we omit an detailed explanation. From the foregoing description and Theorem 1, we can also induce the following theorem.

Theorem 2. In the extended double auction protocol, every entity participating in auction process cannot deny that he or she has submitted an ask or bid.

## 6.1.4. Robustness and correctness

Even though some buyers and sellers cannot participate in or are dropped from an auction process due to an unstable network environment or their misbehavior, the extended double auction protocol still works well as long as at least t sellers and buyers among n sellers and m buyers are able to honestly attend an auction process. This robustness and correctness, which is a major property being emphasized in our protocol, is satisfied by the threshold access structure, and the evaluation of participants is obtained by using Lagrange interpolation as follows:

$$
\prod_ {k = 1} ^ {t} \left(g ^ {p (k)}\right) ^ {\lambda_ {k}} = g ^ {\sum_ {k = 1} ^ {t} p (k) \lambda_ {k}} = g ^ {p (0)}
$$

where $\lambda _ { k } { = } \Pi _ { i \neq k } \frac { i } { i - k }$ is a Lagrange coefficient and $p ( 0 ) { = } l _ { \mathrm { e } } .$

<sup></sup>Note that the modification of a bid or ask is possible if more than k buyers and sellers collude in extended double auction protocol. In addition, in case that an adversary compromises $n - k + 1$ buyers or seller, the normal auction process is impossible. Therefore, the threshold value k will need to be appropriately chosen to resist 's attack and collusion with considering auction environment.

## 6.1.5. Public verifiability

In the proposed protocol, any one can check the validity of submitted signatures and offers from participants. This is achieved by the publicly verifiable secret sharing scheme, the signature of knowledge, and some zero-knowledge proofs.

## 6.2. Efficiency

## 6.2.1. Communication

Our protocol has very low communication overheads: one round for registration, one round for bid/ask submission, one round for determining the trading price and winners.

## 6.2.2. Computation

In terms of computation overheads, we compare the extended double auction protocol with Wang and Leung's protocol [24], because both schemes are based on MCD and TPD protocol. The computational cost is

Total computation comparison

Table 4

<table><tr><td colspan="2">Computational cost</td><td>Wang and Leung&#x27;s protocol</td><td>Our protocol</td></tr><tr><td rowspan="3">Buyers</td><td> $E$ </td><td> $2mw$ </td><td> $3mn$ </td></tr><tr><td> $M$ </td><td> $3mw$ </td><td> $2m$ </td></tr><tr><td> $ZK$ </td><td> $w(2m+1)$ </td><td> $2mn$ </td></tr><tr><td rowspan="3">Sellers</td><td> $E$ </td><td> $2nw$ </td><td> $3mn$ </td></tr><tr><td> $M$ </td><td> $3nw$ </td><td> $2n$ </td></tr><tr><td> $ZK$ </td><td> $w(2n+1)$ </td><td> $2mn$ </td></tr><tr><td rowspan="2">Manager</td><td> $E$ </td><td> $-$ </td><td> $2t$ </td></tr><tr><td> $M$ </td><td> $2\{(m-1)^{w}+(m-1)^{w}+w(m+n+1)\}$ </td><td> $-$ </td></tr></table>

considered in terms of modular arithmetic, including modular exponentiation E and modular multiplication $M ,$ and zero-knowledge ZK for proving the correctness of private key, encrypted shares and decrypted shares. We assume that both protocols use the same zero-knowledge. Table 4 represents the total computational overheads, where m and n are the number of buyers and sellers, respectively, w indicates the possible offering prices and t is threshold value of $( t , m )$ and (t, n) threshold access structure. In Wang and Leung's protocol, note that the manager does not exist, however, in fact the auctioneer serves as the manager. From Table 4, we can see the price range w has no effect on the computational overheads in our protocol. As a result, our protocol is more efficient than Wang and Leung's protocol, especially when w becomes large.

## 7. Conclusion and future work

We analyzed some weaknesses in MCD and TPD protocols and proposed an improved double auction protocol. Even though our scheme is based on MCD protocol, it is robust against false bids. Moreover, we extended it to meet most security requirements for a secure and practical double auction protocol. Since the extended double auction protocol is based on a threshold access structure, even if some participants dropped out of the auction process early due to an unstable network or misbehavior, it is still able to be successfully completed. Moreover, it is relatively efficient in terms of computations and communications.

In future research, the trust and dependence of the manager can be improved by subdividing the manager into registration manager and market manager. The registration manager manages participants in double auction market and holds the corresponding relation of the identity and a auction ticket, while market manager holds auction process. At this point, it is required that neither registration manager nor market manager alone is able to trace a participant. Secondly, to reinforce the results of the proposal, the formal analysis needs to be used with informal security analysis.

## Acknowledgements

We would like to thank anonymous reviewers for their helpful comments to improve our manuscript. This research was supported by the MIC of Korea, under the ITRC support program supervised by the IITA(IITA-2006-C1090-0603-0026).

## References

[1] O. Baudron, J. Stern, Non-interactive Private Auctions, Financial Cryptography'01, LNCS, vol. 2339, Springer Verlag, 2001, pp. 364–378.

[2] D. Boneh, The decision Diffie–Hellan problems, Proceeding of the Third Algorithmic Number Theory Symposium, LNCS, vol. 1423, Springer Verlag, 1998, pp. 48–63.

[3] F. Brandt, Secure and private auctions without auctioneers, Technical Report FKI-245-02, Institut fur Informatick, Technishce Universitat Munchen, 2002.

[4] F. Brandt, Fully private auctions in a constant number of rounds, Financial Cryptography'03, LNCS, vol. 2742, Springer Verlag, 2003, pp. 223–228.

[5] C. Cachin, Efficient private bidding and auctions with an oblivious third party, ACM CCS'99, 1999, pp. 120–127.

[6] J. Camenisch, M. Stadler, Efficient group signature scheme for large groups, CRYPTO'97, LNCS, vol. 1294, Springer Verlag, 1997.

[7] D. Chaum, T.P. Pedersen, Wallet databases with observers, CRYPTO'92, LNCS, vol. 740, Springer Verlag, 1992, pp. 89–105.

[8] X. Chen, B. Lee, K. Kim, Receipt electronic auction schemes using homomorphic encryption, ICISC'03, LNCS, vol. 2971, Springer Verlag, 2003, pp. 259–273.

[9] D. Friedman, J. Rust, The Double Auction Market, Addison-Wesley Publishing Company, 1993.

[10] E. Fujisaki, T. Okamoto, A practical and provably secure scheme for publicly verifiable secret sharing and its applications, EUROCRYPT'98, LNCS, vol. 1403, Springer Verlag, 1998, pp. 32–46.

[11] W. Ham, K. Kim, H. Imai, Yet another strong sealed-bid auctions, SCIS'03, vol. 1/2, 2003, pp. 11–16.

[12] Z. Hidvégi, W. Wang, A.B. Whinston, Binary vickery auction — a robust and efficient multi-unit sealed-bid online auction protocol against buyer multi-identity bidding, Decision Support Systems 43 (2007) 301–312.

[13] H. Kikuchi, (M + 1)st-price auction protocol, Financial Cryptography'01, LNCS, vol. 2339, Springer Verlag, 2001.

[14] B. Lee, K. Kim, J. Ma, Efficient public auction with one-time registration and public verifiability, Indocrypt'01, LNCS, vol. 2247, Springer Verlag, 2001.

[15] U. Maurer, S. Wolf, The relationship between breaking the Diffie–Hellman protocol and computing discrete logarithm, SIAM Journal on Computing 28 (5) (1999) 1689–1721.

[16] P. McAfee, A dominant strategy double auction, Journal of Economic Theory 56 (1992) 434–450.

[17] K. Omote, A. Miyaji, A practical English auctin with one-time registration, ACISP'01, LNCS, vol. 2119, Springer Verlag, 2001, pp. 221–234.

[18] T.P. Pedersen, Non-interactive and information-theoretic secure verifiable secret sharing, CRYPTO'91, LNCS, vol. 576, Springer Verlag, 1991, pp. 129–140.

[19] K. Peng, C. Boyd, E. Dawson, K. Viswanathan, Robust, privacy protecting and publicly verifiable sealed-bid auction, ICICS'02, LNCS, vol. 2513, 2002, pp. 147–159.

[20] B. Schoenmakers, A simple publicly verifiable secret sharing scheme and its application to electronic voting, CRYPTO'99, LNCS, vol. 1666, Springer Verlag, 1999, pp. 148–164.

[21] V. Shoup, Lower bounds for discrete logarithms and related problems, EUROCRYPT'97, LNCS, vol. 1233, Springer Verlag, 1997, pp. 256–266.

[22] M. Stadler, Publicly verifiable secret sharing, EUROCRYPT'96, LNCS, vol. 1070, Springer Verlag, 1996, pp. 190–199.

[23] W. Vickrey, Counterspeculation, auction, and competitive sealed tenders, Journal of Finance 16 (1) (1961) 8–37.

[24] C. Wang, F. Leung, Secure double auction protocols with full privacy protection, ICISC'03, LNCS, vol. 2971, Springer Verlag, 2003, pp. 215–229.

[25] M. Yokoo, Y. Sakurai, S. Matsubara, Robust Double Auction Protocol against False-name Bids. Proceeding of the 21st International Conference on Distributed Computing Systems, IEEE Computer Society, pp. 147–145, 2001, (39), pp 241–252, 2005.

[26] M. Yokoo, Y. Sakurai, S. Matsubara, Robust double auction protocol against false-name bids, Decision Support Systems 39 (2005) 241–252.

![](/api/attachments/Y5674U2P/fulltext/images/dffbdd149656821d39565d72dda34de8cff5b50b8133ce1c739b2d992384e1f2.jpg)  
JungHoon Ha received his B. E. and M. E. degrees in Electronics from Kyungpook National University, Korea, in 2002 and 2004, respectively, and now is Ph.D. candidate. Currently, he is a research engineer with Mobile Network Security Research Center (MSRC), where he conducts research and development of public-key cryptosystems, digital signature schemes, cryptographic security protocols, and formal security analy

sis methodology. His research interests also include network security, ubiquitous communication security for cellular, mobile ad-hoc, RFID networks, and development of secure auction protocol for e-commerce.

![](/api/attachments/Y5674U2P/fulltext/images/56817148d5b935fdc348ed10f6d3a3b02cd2e23b2b86da0f31124a58f2afc8be.jpg)

Jianying Zhou is a lead scientist at Institute for Infocomm Research, and heads the Internet Security Lab. He is also an adjunct professor in University of Science and Technology of China and in Shanghai Jiaotong University, and an adjunct senior scientist in University of Malaga. Dr. Zhou obtained PhD degree in Information Security from University of London. His research interests are in computer and network security, cryptographic protocol,

digital signature and non-repudiation, mobile communications security, public-key infrastructure, and secure electronic commerce. He is a worldleading researcher on non-repudiation, and authored the book “Nonrepudiation in Electronic Commerce” which was published by Artech House in 2001. He is a co-founder and steering committee member of International Conference on Applied Cryptography and Network Security (ACNS).

![](/api/attachments/Y5674U2P/fulltext/images/03a90a9e2931ab26741ab103cc500e7d1b66f63e11c32d9d9a6d280a16e874e2.jpg)

SangJae Moon received his B. E. and M. E. degrees in Electronics from Seoul National University, Korea in 1972 and 1974 respectively. He received Ph.D. in Communication Engineering from the University of California, Los Angeles, USA, in 1984. He was working as a consultant of Omnet, Co., USA from 1984 to 1985. Currently, he is a professor at the School of Electrical Engineering and Computer Science, Kyungpook National

University, Korea, and the director of Mobile Network Security Technology Research Center(MSRC). He is also an honorary president of the Korean Institute of Information Security and Cryptology. His current research interests are the information security in mobile, ubiquitous, and RFID networks including the physical security on smart IC cards. He took part in the Korea Certificate-based Digital Signature Algorithm (KCDSA) Standard project. He has a number of issued patents and more than one hundred technical publications in international journals and conferences in the areas of information security.
