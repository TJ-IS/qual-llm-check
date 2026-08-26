---
otero_id: 20415
otero_key: "PC25MHJZ"
title: "Information disclosure and blockchain technology adoption strategy for competing platforms"
authors: "Yao-Yu Wang; Feng Tao; Jiancai Wang"
year: "2022"
journal: "Information & Management"
doi: "10.1016/j.im.2021.103506"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information disclosure and blockchain technology adoption strategy for competing platforms

Yao-Yu Wang <sup>a</sup>, Feng Tao <sup>b,\*</sup>, Jiancai Wang <sup>c</sup>

<sup>a</sup> Research Center for Smarter Supply Chain, Dongwu Business School, Soochow University, Suzhou, Jiangsu, China

<sup>b</sup> Department of Management Science and Engineering, East China University of Science and Technology, Shanghai, China

<sup>c</sup> School of Management and Economics, Beijing Institute of Technology, Beijing, China

## A R T I C L E I N F O

Keywords: Blockchain technology Information disclosure Competition Platforms

## A B S T R A C T

A key strategic decision for platforms such as Amazon, JD.com, and eBay is the extent to which they provide information to consumers because product information plays an important role in consumers’ purchasing de cisions. Considering that consumers may doubt the disclosed information, these platforms may have the incentive to implement blockchain technology to authenticate their disclosed information and, therefore, eliminate consumer distrust. In this paper, we develop an analytical model to investigate the optimal information disclosure and equilibrium blockchain adoption strategy for competing platforms and analyse how the consumers’ beliefs and blockchain cost will affect the equilibrium results. Our results show that the equilibrium blockchain adoption strategy is a threshold-structured policy. To be specific, there are two critical values of blockchain cost. If the blockchain cost is larger than the upper threshold, then neither of the platforms has the incentive to apply blockchain technology, and the market is full of unverified information: however, if the blockchain cost is less than the lower threshold, both platforms prefer to apply blockchain technology, and the amount of authenticated information is larger than that of unverified information in the nonblockchain case Finally, if the blockchain cost is between the two bounds, then a mixed strategy becomes the equilibrium; that is, one platform adopts the blockchain technology, while the other does not. In this case, the amount of authen ticated information may be larger than that of unverified information, but the platform that ignores using blockchains is also better off with this new technology. We make several extensions, and the results show that our main conclusions remain unchanged, which indicates that the conclusions can be generalized.

## 1. Introduction

Information is an important factor that affects consumer demand [13,18,36]. Compared with traditional retailers, one of the biggest ad vantages of an online platform (e.g., Amazon in the US, JD.com in China) is that it can release various forms of information about pro ducts—such as quality, pricing, product online reviews, and product availability—in a timely manner through a variety of ways, such as a literal description, picture, video, and even a live stream $[ 6 , 1 4 . ]$ As a result, the market is full of product information [6]. This disclosed in formation can determine whether consumers purchase the product or not [1,7,18]. Sometimes, having more information will increaze the likelihood of attracting consumers and increasing their tendency to purchase; however, in some other situations, less information will attract more consumers because having less information may arouse consumer curiosity [36]. Therefore, it is not always beneficial for a platform to release much product information.

More importantly, consumers may not believe that the information releazed is reliable [3]. The reasons for this are twofold. (1) Some online platforms may engage in undesirable and/or unethical behaviors [37], for example, generating fake reviews using fake accounts [19]. (2) It is difficult and costly for consumers to verify the information’s authen ticity or conduct quality inspections [8], [33]. Specifically, it takes a long time to confirm detailed product information, such as paper doc uments. Sometimes, these documents may even be fake [7,16]. An empirical study shows that almost 60% of consumers do not trust their data being collected; therefore, they lack trust in vendors [22]. Thus, how to authenticate the information and increaze consumers’ trust be comes an important issue [2,5].

Blockchain is an emerging technology that is famous for its features as immutable, irreversible, traceable, and trustworthy [27]. Therefore, blockchain technology can be used to authenticate information and verify transactions [7,31]. For example, with the help of blockchain technology, Walmart can trace mangos from Mexico to its shelves, thus providing full and honest product information [21]. Using blockchain technology costs nothing for consumers to check the disclosed infor mation, which effectively reduces consumers’ distrust of the disclosed information and increazes their purchasing. Consequently, an increasing number of platforms, such as Everledger, are providing blockchain technology–supported systems to disclose authorized and trusted prod uct information [8]. However, the cost of this technology is an important factor that cannot be neglected. On the one hand, publishing product information will increaze platform costs. For example, online retailing platforms may introduce a consumer review system or build a virtual dressing room to facilitate information disclosure, yet these information tools require heavy investments [36]. On the other hand, adopting blockchain technology also requires other forms of investment, such as the operation cost, including the fixed cost for operating the coding system and variable cost for data storage and traffic [34], changing/ standardizing business processes [25], integrating different existing systems, and higher energy consumption [16].

In this context, we attempt to answer the following research ques tions: (1) What is the optimal information disclosure strategy for plat forms and how does the blockchain technology adoption strategy affect the optimal amount of disclosed information? (2) What is the equilib rium blockchain technology adoption strategy for competitive plat forms? (3) How do environmental parameters (e.g., competition, cost, consumer belief) affect the above conclusions?

To answer these questions, we first build a simple game theory–based analytical model in which two competing platforms move simulta neously; this model will help decide whether to adopt blockchain technology. Because each platform has the option to adopt or not adopt blockchain technology, we analyse the following three cases:

Case 1: Both platforms decide not to implement blockchain tech nology. We refer to this as strategy-[NN] in the following discussions. Case 2: One platform adopts blockchain technology, while the other platform does not implement blockchain technology. We refer to this as strategy-[BN].

Case 3: Both platforms implement blockchain technology. We refe to this as strategy-[BB] in the following discussions.

Based on the models, we first derive the optimal outcomes of each case and then try to analyse the platforms’ optimal information disclo sure behavior to obtain the equilibrium blockchain adoption strategy. Our results show that the equilibrium blockchain technology adoption strategy is a typical threshold-structured policy. Specifically, there are two critical values of blockchain technology cost. When the blockchain cost is larger than the upper threshold, the equilibrium strategy is the [NN]-strategy, where consumers distrust the disclosed information; however, when the blockchain cost is less than the lower threshold, the equilibrium strategy is the [BB]-strategy, where the amount of authentic information is larger than that of the unverified information in the [NN] case. Furthermore, when the blockchain cost is at an intermediate level and falls between the two critical values, the [BN]-strategy becomes the equilibrium strategy, where the amount of authentic information dis closed by the platform with blockchain technology might be larger than that of the unverified information disclosed by the platform without blockchain technology. To test whether our conclusions can be gener alized, we make several extensions, and our results show that the main conclusions of the current paper remain unchanged.

The rest of the present paper is organized as follows. Section 2 pro vides a literature review. Section 3 gives a brief description of the model and the assumptions. Section 4 derives the optimal outcomes for the three cases under the basic model and provides some analysis. Section 5 makes some extensions to test our conclusions, and Section 6

summarizes the paper.

## 2. Literature review

Our work is mainly related to two streams of existing research: product information disclosure and blockchain technology.

First, we consider issues regarding product information disclosure, which is a hot topic in both practice and academic areas [12.14.15.23]. Disclosing product information is an effective way to resolve consumer uncertainty and doing so increazes purchasing and reduces product returns [36]. Therefore, many studies have focused on information disclosure strategies. Zimmer et al. [37] propose an information disclosure model to achieve a competitive advantage for retailers by matching consumers’ needs. Gu and Xie [13] investigate firms’ infor mation disclosure strategies regarding whether to assist consumers in finding their fit to product attributes. Guan et al. [14] classify consumers into naïve and sophisticated types and propose a threshold value that determines a monopolistic retailer’s private quality information disclosure policy based on these two consumer types. Regarding the amount of disclosed information, different studies have different or even opposite conclusions. For example, Chu and Zhang [9] argue that the disclosed information should be limited. However, Shulman et al. [30] find that firms may benefit from disclosing less information. Further more, by formulating an information disclosure model in a dynamic sequential screening setting, Li and Shi [20] point out that disclosing full information is not always optimal for sellers. The best way to do this is to provide different amounts of information to different consumer types. In contrast, Zhang et al. [36] reveal that firms can benefit from disclosing more information if the related cost of disclosure decreazes. Allcott and Sweeney [1] carry out a field experiment to investigate the role of agents in releasing information to consumers; they argue that to stimulate de mand, retailers should incentivize agents when these agents choose to provide more information. Whether more or less, another aspect of product information that deserves attention is the authenticity/trust of that information [8,37]. To increaze product visibility and encourage more consumer participation, firms may manipulate platform data to target consumers [19]. However, in most cases, it is expensive and sometimes infeasible for consumers to verify the information [4.8.19]. Different from the aforementioned work, we consider two competing platforms selling substitutable products to the market that take advan tage of blockchain technology to authenticate their disclosed information. We show that it is profitable for the platform that adopts blockchain technology to release more information than the platform that does not adopt it.

Our work also pertains to the application of blockchain technology. Since Bitcoin—an important application of blockchain technology—was introduced in 2008 [26], the merits of blockchain have been discovered; since then, this technology has been used and developed in many in dustries, such as finance and supply chain management [3,27,35]. Recently, Iansiti and Lakhanl [17] have discussed the essential features of blockchains and identified some applications in the digital world. Specifically, blockchains can distribute ledgers that can be validated, stored. and easily shared in transactions: thus. smart contracts are a potential application of this technology [10,28]. Using blockchains, smart contracts can be automatically self-executed with security and trust. Dolgui et al. [11] model a blockchain-based smart contract as a flow shop scheduling problem with multiple objectives and develop an algorithm to balance the lead time and cost. Blockchains can illuminate transaction fraud because all data can be continuously traced and vali dated [27]. Therefore, another major application is to engender trust in information and lower the transaction cost in the supply chain, which has proliferated extensively in recent years $[ 4 , 7 , 2 4 , 3 1 ]$ ]. Wang et al. [32] conduct an empirical study to evaluate the potential use of blockchain technology in supply chains by considering the perceived benefits, po tential adoption areas, and perceived challenges. Integrating RFID technology and blockchain technology, Mondal et al. [24] develop an architecture to trace and monitor food safety to increaze food supply chain performance. Bai and Sarkis [4] apply blockchain technology to increaze the transparency of sustainable supply chains and evaluate blockchain selection decisions by formulating a group decision model. Choi et al. [7] builds an analytical model to explore the benefits of blockchain technology in a luxury supply chain; here, the author as sumes that blockchains can authenticate and certify luxury products, such as diamonds. Furthermore, Choi et al. [8] take price as an exoge nous parameter and develop a duopoly model between two platforms that play the Nash game, in which they derive an equilibrium product information disclosure strategy when implementing blockchain tech nology. The difference between our paper and the above literature is twofold. (1) Due to its features, we consider blockchain to be an effective tool to increaze consumers’ belief in what information platforms provide to the market [7]. (2) We develop equilibrium blockchain adoption strategies, as well as an information disclosure policy, for platforms.

## 3. Model assumptions

We assume that there are two platforms selling two substitutable products in the market. The product on platform i is referred to as product $i , i = 1 , 2 .$ . To entice more demand, platform i decides to disclose some product information, and the amount of information disclosure is denoted by $b _ { i } , i = 1 , 2 .$ . In our paper, the disclosed information refers to the additional and preferable information that would capture the con sumer’s curiosity and favorite products, hence stimulating consumers needs [1,7].

However, consumers may not fully believe in the information dis closed by the platforms. We assume that the degree of consumer belief in the disclosed information is δ and $0 \leq \delta \leq 1$ . When $\delta = 0 ,$ this means that consumers do not trust the disclosed information at all, which is com mon in the case where the product is greatly exaggerated. When $\delta = 1$ this refers to the case where consumers believe that all the disclosed information is authentic and believe in what the platform says. Usually, consumers may completely believe in the information provided by some large platforms with good reputations. For the most common cases, consumers show some doubt about the disclosed information. that is. 0 $< \delta < 1$ . When blockchain technology is applied, the disclosed infor mation can be traced and proven to be true; thus, $\delta = 1$

The market demand for products is assumed to be deterministic and sensitive to both the price and disclosed information. Specifically, we assume that the demand decreazes in the platform’s own selling price and the competitor’s disclosed information but is increasing in its own disclosed information and the competitor’s selling price. Considering whether a platform uses blockchain technology or not, the corre sponding demand function takes the following form:

(1) When both platforms do not use blockchain technology to verify the information’s authenticity, the demand function can be stated as:

$$
D _ {i} ^ {N N} = a - p _ {i} + \beta p _ {j} + \delta (b _ {i} - \gamma b _ {j}), i = 1, 2, j = 3 - i,\tag{1}
$$

where δ is the consumer’s belief in the disclosed information, and $0 < \delta$ < 1. a is the potential market, β is the cross-price sensitivity, and γ is the cross-information sensitivity. For ease of analysis, we assume $\beta \geq \gamma .$

(1) When one of two platforms applies blockchain technology, that is, platform i adopts the technology, the information’s authen ticity that is disclosed by this platform is verified and traceable, and the corresponding consumer’s belief in the disclosed infor mation is 1. However, the consumer’s belief in platform j’s dis closed information is still δ. Consequently, the demand functions become as follows:

$$
D _ {i} ^ {B N} = a - p _ {i} + \beta p _ {j} + b _ {i} - \delta \gamma b _ {j},\tag{2}
$$

$$
D _ {j} ^ {B N} = a - p _ {j} + \beta p _ {i} + \delta b _ {j} - \gamma b _ {i}.\tag{3}
$$

(2) When both platforms implement blockchain technology, the in formation’s authenticity is verified and traceable; thus, the con sumer’s belief in the disclosed information is 1 for both platforms. The demand function is shown as follows:

$$
D _ {i} ^ {B B} = a - p _ {i} + \beta p _ {j} + b _ {i} - \gamma b _ {j}, i = 1, 2, j = 3 - i.\tag{4}
$$

To attract demand, a platform would choose to disclose some “favorable” information to consumers, such as adding positive senti ments to encourage consumer participation in the movie industry [19]. The objective of revealing this information is to increaze consumers utility. The disclosed information, although additional, seems to increaze the product’s “quality.” Thus, we assume that the cost of releasing information increazes with the information provided and takes a generally used quadratic form $t { \cdot } b _ { i } ^ { 2 } / 2 ,$ where $t \left( \geq 1 \right)$ is the coefficient and $b _ { i }$ is the disclosed information.

As mentioned, consumers may not believe in the platform’s disclosed information. To solve this problem, a platform can use blockchain technology to ensure that the disclosed information about each product is authentic and traceable. Blockchain technology ensures that a plat form can check, audit, and update every piece of disclosed information on each product. Hence, it incurs a unit cost $c _ { B } .$ . We use unit blockchain cost or unit information cost interchangeably in this paper. For ease of exposition, we normalize the procurement cost to zero.

## 4. Model and analysis

In this section, we first consider a simple situation where two plat forms sell substitutable products to consumers and play a vertical Nash game. In Section 5, we make two extensions, one considering a case where the two platforms play a Stackelberg game and the other incor porating upstream suppliers. Our results show that the main conclusions remain valid under these extensions.

## 4.1. Strategy-[NN]

In this scenario, neither of the two platforms uses blockchain tech nology to authenticate their disclosed information. Therefore, con sumers may think that the disclosed additional information may not be 100% accurate $( 0 \leq \delta < 1 )$ . Under Strategy-[NN], platform i’s optimal profit function is:

$$
\pi_ {i} ^ {N N} = (p _ {i} - c) \cdot D _ {i} ^ {N N} - t \cdot b _ {i} ^ {2} / 2, i = 1, 2.\tag{5}
$$

where the superscript $" N N "$ indicates that both platforms choose to disclose additional information without the help of blockchain tech nology. Substituting Eq. (1) into Eq. (5) and solving the corresponding objective function yields the following equilibrium solutions.

Proposition 1. For the NN scenario, the optimal selling prices and the corresponding optimal amounts of disclosed information are:

$$
p _ {1} ^ {N N} = p _ {2} ^ {N N} = \frac {(a + c) t + (\gamma - 1) \delta^ {2} c}{(2 - \beta) t + (\gamma - 1) \delta^ {2}}, b _ {1} ^ {N N} = b _ {2} ^ {N N} = \frac {\delta (a + (\beta - 1) c)}{(2 - \beta) t + (\gamma - 1) \delta^ {2}}.
$$

and the resulting profits of the two platforms are:

$$
\pi_ {1} ^ {N N} = \pi_ {2} ^ {N N} = \frac {t (2 t - \delta^ {2}) (a + (\beta - 1) c) ^ {2}}{2 ((2 - \beta) t + (\gamma - 1) \delta^ {2}) ^ {2}}.
$$

From this proposition, it can be seen that the selling price, disclosed information, and optimal profit all depend on the consumer’s belief in the disclosed information. Based on the optimal solutions, we have the following conclusions:

Corollary 1. For the NN scenario, we have:

(1) $\begin{array} { r } { \frac { d p _ { i } ^ { N N } } { d \delta } > 0 , \frac { d b _ { i } ^ { N N } } { d \delta } > 0 ; } \end{array}$

(2) There is a threshold value of consumers’ belief $\overleftarrow { \delta } ^ { * }$ such that when $\delta ^ { 2 }$ < δ<sup>∗</sup>, <sup>dπNNi</sup> > 0; otherwise, dδ $\begin{array} { r } { \frac { d \pi _ { i } ^ { N N } } { d \delta } \leq 0 , i = 1 , 2 . } \end{array}$

The first part of Corollary 1 shows that increasing the belief in the information that platforms give will directly benefit consumers because the platforms will decreaze the selling prices accordingly. This is mainly because when customers strengthen their belief in what platforms have disclosed, the demand for products increazes; thus, platforms have an incentive to decreaze the selling prices to further stimulate the demand. On the other hand, the greater their belief, the more disclosed infor mation. In other words, if consumers are losing belief in what is dis closed, it is better for platforms to release less information. This is also an explanation for why some retailers on the TMALL platform do not respond much to rumors, which leads to a loss of trust in their products.

Intuitively, the more consumers believe in the disclosed information, the better this is for platforms. Surprisingly, and interestingly, according to the second part of Corollary 1, platforms are better off only if con sumers’ belief is less than a certain threshold value. Here, there are two effects that can explain this phenomenon: the revenue increment and cost increment. Specifically, we know that the selling price decreazes with a decreaze of consumers’ beliefs, which further stimulates demand, and the amount of information increazes with an increaze of consumers beliefs, which incurs more information costs $( t \cdot b _ { i } ^ { 2 } / 2 )$ . When consumers belief is less than the threshold value, the revenue increaze resulting from the rising demand is larger than the cost increment caused by additional disclosed information. Consequently, platform profit increa zes with an increaze of consumers’ beliefs. Nonetheless, when con sumers’ beliefs exceed the threshold value, the cost increment overwhelms the revenue increment: therefore, platforms are worse off as consumers’ beliefs increaze. This reveals that for platforms, it is un necessary to disclose as much information as possible to improve con sumers’ beliefs about their products.

## 4.2. Strategy-[BN]

In this scenario, one platform adopts blockchain technology to authenticate its disclosed information, and the other platform does not apply this technology. Accordingly, consumers believe that the disclosed information releazed by the former platform is genuine and have no doubts about this information. However, they still show some distrust about the disclosed information issued by the other platform. Without a loss of generality, we assume platform i uses blockchain technology and platform j does not adopt this technology. Therefore, their profits can be stated as follows:

$$
\pi_ {i} ^ {B N} = (p _ {i} - c - c _ {B}) \cdot D _ {i} ^ {B N} - t \cdot b _ {i} ^ {2} / 2,\tag{6}
$$

$$
\pi_ {j} ^ {B N} = (p _ {j} - c) \cdot D _ {j} ^ {B N} - t \cdot b _ {j} ^ {2} / 2.
$$

(7)

The equilibrium solutions are summarized in the following proposition.

Proposition 2. For the BN scenario, the optimal selling prices are:

$$
p _ {i} ^ {B N} = c + c _ {B} + t \cdot b _ {i} ^ {B N}, p _ {j} ^ {B N} = \frac {t \cdot b _ {j} ^ {B N}}{\delta} + c.
$$

the optimal amounts of disclosed information are:

$$
b _ {i} ^ {B N} = \frac {(a + (\beta - 1) c + \beta c _ {B}) (\beta t - \gamma \delta^ {2}) + (a + (\beta - 1) c - c _ {B}) (2 t - \delta^ {2})}{(2 t - 1) (2 t - \delta^ {2}) - (\beta t - \gamma) (\beta t - \gamma \delta^ {2})},
$$

$$
b _ {j} ^ {B N} = \frac {(a + (\beta - 1) c - c _ {B}) (\beta t - \gamma) + (a + (\beta - 1) c + \beta c _ {B}) (2 t - 1)}{(2 t - 1) (2 t - \delta^ {2}) - (\beta t - \gamma) (\beta t - \gamma \delta^ {2})} \delta .
$$

and the corresponding profits are:

$$
\pi_ {i} ^ {B N} = \frac {t (2 t - 1) \big ((a + (\beta - 1) c + \beta c _ {B}) (\beta t - \gamma \delta^ {2}) + (a + (\beta - 1) c - c _ {B}) (2 t - \delta^ {2}) \big) ^ {2}}{2 ((2 t - 1) (2 t - \delta^ {2}) - (\beta t - \gamma) (\beta t - \gamma \delta^ {2})) ^ {2}},
$$

$$
\pi_ {j} ^ {B N} = \frac {t (2 t - \delta^ {2}) ((a + (\beta - 1) c - c _ {B}) (\beta t - \gamma) + (a + (\beta - 1) c + \beta c _ {B}) (2 t - 1)) ^ {2}}{2 ((2 t - 1) (2 t - \delta^ {2}) - (\beta t - \gamma) (\beta t - \gamma \delta^ {2})) ^ {2}}.
$$

Because of competition, even though platform i adopts blockchain technology to authenticate the disclosed information $( \delta = 1 ) ,$ , its selling price, disclosed information, and profit are all related to consumers belief, δ. This is simply because platform i’s consumers still show some distrust of platform $j ^ { \prime } s$ disclosed information, which further affects the demand. On the other hand, although platform j does not use blockchain technology and consumers distrust its information, this platform’s selling price, disclosed information, and profit all depend on blockchain cost. In other words, as long as blockchain technology is applied by one platform, no one can be isolated from the impact of this new technology, whether the platform uses it or not.

## Corollary 2. For the BN scenario, we have the following:

(1) In terms of consumers’ belief in the disclosed information, for retailer $i ,$ when $\beta > 2 \gamma ,$ , then $\begin{array} { r } { \frac { d p _ { i } ^ { B N } } { d \delta } > 0 , \frac { d b _ { i } ^ { B N } } { d \delta } > 0 , } \end{array}$ , and $\frac { d \pi _ { i } ^ { B N } } { d \delta } > 0 ;$ otherwise, $\begin{array} { r } { \frac { d p _ { i } ^ { B N } } { d \delta } \leq 0 , \frac { d b _ { i } ^ { B N } } { d \delta } \leq 0 ; } \end{array}$ , and $\frac { d \pi _ { i } ^ { B N } } { d \delta } \leq 0 .$ . However, for retailer j, $\begin{array} { r } { \frac { d p _ { j } ^ { B N } } { d \delta } > 0 , \frac { d b _ { j } ^ { B N } } { d \delta } > 0 , \frac { d \pi _ { j } ^ { B N } } { d \delta } > 0 . } \end{array}$

(2) In terms of blockchain cost, $\begin{array} { r } { \frac { d p _ { i } ^ { B N } } { d c _ { B } } > 0 , \frac { d b _ { i } ^ { B N } } { d c _ { B } } < 0 , \frac { d \pi _ { i } ^ { B N } } { d c _ { B } } < 0 , \frac { d p _ { j } ^ { B N } } { d c _ { B } } > 0 , } \end{array}$ $\begin{array} { r } { \frac { d b _ { j } ^ { B N } } { d c _ { B } } > 0 , \mathrm { a n d } \frac { d \pi _ { j } ^ { B N } } { d c _ { B } } > 0 . } \end{array}$

From Corollary 2(1), we can see that although platform i has applied blockchain technology to authenticate its disclosed information $( \delta = 1 ) ,$ this platform should also care about the consumers’ belief in platform j’s disclosed information. When consumers’ demand is less sensitive to the disclosed information $( \beta > 2 \gamma )$ , platform i can be better off by providing more authentic information as consumers’ beliefs increaze, which means the greater the consumers believe the information is true, the more authentic the information and thus, the more the profits. In contrast, when consumers are more sensitive to the disclosed informa tion $( \beta \leq 2 \gamma )$ , platform i will be worse off and will prefer to disclose less authentic information because consumers’ beliefs will increaze, which means the greater the consumers’ beliefs, the less authentic the infor mation and the less the profits. On the other hand, for retailer j, when consumers' beliefs increaze, this platform will provide more information and be more profitable. In summary, in BN, when consumers are less sensitive to the disclosed information, both platforms are motivated to improve consumers’ beliefs. Under this condition, the platform that adopts blockchain technology to authenticate the disclosed information will also be hurt by the decreasing level of consumer trust in the com petitor’s information. However, when consumers are more sensitive to the disclosed information, only the platform that decides not to adopt blockchain technology has the incentive to increaze consumers' beliefs.

Under this condition, the platform that applies blockchain technology will now be hurt by the increasing consumer belief in the competitor’s information.

Intuitively, platform i’s profit decreazes with respect to the unit blockchain cost, which is shown in part 2 of Corollary 2. We can see that with increasing blockchain costs, both platforms increaze their selling prices. However, platform i, which uses blockchain technology, will decreaze the amount of authentic information accordingly, and platform $j ,$ which ignores blockchain technology, will release more information instead. The reason is that when the blockchain cost increazes, it is costly for platform i to disclose more information, and it is beneficial for platform j to release more information to attract more demand, which further increazes it is profit. This conclusion reveals that in case BN, reducing the blockchain cost will directly benefit the platform that ap plies the technology and hurt the platform that does not.

## Lemma 1. Platform i’s blockchain adoption strategy is as follows:

(1) There are two critical values of blockchain costs $c _ { 1 } ^ { * }$ and $c _ { 1 } ^ { b }$ that if $0 \leq c _ { B } \leq c _ { 1 } ^ { * }$ , then $b _ { i } ^ { B N } > b _ { i } ^ { N N }$ and $\pi _ { i } ^ { B N } \geq \pi _ { i } ^ { N N } ; \mathrm { i f } \ c _ { 1 } ^ { * } < c _ { B } < c _ { 1 } ^ { b } ,$ , then $b _ { i } ^ { B N } > b _ { i } ^ { N N }$ and $\pi _ { i } ^ { B N } < \pi _ { i } ^ { N N } ;$ ; otherwise, if $c _ { 1 } ^ { b } \leq c _ { B } < \overline { { c _ { 1 } } }$ , then $b _ { i } ^ { B N } \leq$ $b _ { i } ^ { N N }$ and $\pi _ { i } ^ { B N } < \pi _ { i } ^ { N N }$

(2) There are two critical values of blockchain costs $c _ { 1 } ^ { + }$ and $c _ { 1 } ^ { b n }$ that if $0 \leq c _ { B } \leq c _ { 1 } ^ { + }$ , then $b _ { i } ^ { B N } > b _ { j } ^ { B N }$ and $\pi _ { i } ^ { B N } \geq \pi _ { j } ^ { B N } ; { \mathrm { i f ~ } } c _ { 1 } ^ { + } < c _ { B } < c _ { 1 } ^ { b n }$ , then $b _ { i } ^ { B N } > b _ { j } ^ { B N }$ and $\pi _ { i } ^ { B N } < \pi _ { j } ^ { B N } ;$ otherwise, if $c _ { 1 } ^ { b n } \leq c _ { B } < \overline { { c _ { 1 } } }$ , then $b _ { i } ^ { B N } \leq$ $b _ { j } ^ { B N }$ and $\pi _ { i } ^ { B N } < \pi _ { j } ^ { B N }$

(3) There are two critical values of blockchain costs $c _ { 1 } ^ { \wedge }$ and $c _ { 1 } ^ { n }$ that if $0 \leq c _ { B } < c _ { 1 } ^ { \wedge }$ , then $b _ { j } ^ { B N } < b _ { j } ^ { N N }$ and $\pi _ { j } ^ { B N } < \pi _ { j } ^ { N N } ; \mathrm { i f } \ : c _ { 1 } ^ { \wedge } \leq c _ { B } < c _ { 1 } ^ { n }$ , then $b _ { j } ^ { B N } \geq b _ { j } ^ { N N }$ and $\pi _ { j } ^ { B N } < \pi _ { j } ^ { N N } ;$ ; otherwise, if $c _ { 1 } ^ { n } \leq c _ { B } < \overline { { c _ { 1 } } } ,$ then $b _ { j } ^ { B N } >$ $b _ { j } ^ { N N }$ and $\pi _ { j } ^ { B N } \geq \pi _ { j } ^ { N N }$

The expressions of $c _ { 1 } ^ { b } , c _ { 1 } ^ { b n } , c _ { 1 } ^ { n } , c _ { 1 } ^ { * } , c _ { 1 } ^ { + } , c _ { 1 } ^ { \wedge }$ , and $\overline { { c _ { 1 } } }$ are shown in the appendix.

From Lemma 1, we can see that when the blockchain cost is small, blockchain technology will be a benefit for the platform that applies it and will encourage the platform to disclose more authentic information (see Lemma 1(1)); however, it will hurt the platform that decides not to use it, which results in disclosing less information (see Lemma 1(3)). The reason is that when platform i adopts blockchain technology, although it incurs more technology costs, it is also beneficial because it improves consumers’ beliefs, hence increasing demand, which can compensate for the blockchain cost. Under this condition, there is more authentic in formation and less unconfirmed information (see Lemma 1(2)). The total amount of information is more accurate and authentic. When the blockchain cost is large, blockchain technology will benefit the platform that ignores it and will induce the corresponding platform to disclose more unconfirmed information (see Lemma 1(3)); however, it will hurt the platform that applies it. leading to less authentic information (see Lemma 1(1)). The reason is that the positive effect of the increazed demand resulting from an improvement of consumers’ beliefs cannot cover the negative effect of technology cost increments anymore. Under this condition, there is more unconfirmed information than authentic information in the market (see Lemma 1(2)). When the cost is at an intermediate level (such as $c _ { B } \in [ c _ { 1 } ^ { * } , c _ { 1 } ^ { b } ) \cap [ c _ { 1 } ^ { \wedge } , c _ { 1 } ^ { n } ) )$ , blockchain technology may hurt the two platforms simultaneously but lead them to disclose more information (see Lemma 1(1) and $( 3 ) ) ^ { 2 }$ . Under this condition, there may be more authentic information than unconfirmed information in the market. However, the platform with blockchain technology would suffer more losses than the platform without the technology. Eventually, no one has the incentive to apply blockchain technology. However, interestingly and importantly, when $c _ { 1 } ^ { * } > c _ { 1 } ^ { n }$ and $c _ { 1 } ^ { n } < c _ { B } < c _ { 1 } ^ { * 3 }$ , blockchain technology not only benefits the platform that applies it but also makes the platform that ignores it better off, representing the exter nalities of adopting blockchain technology.

Compared with the NN case, in the BN case, it is better for the platform that adopts blockchain technology to provide more accurate and authentic information than the competitor platform when the blockchain cost is small and to provide less accurate and authentic in formation than the competitor platform when the blockchain cost is large.

## 4.3. Strategy-[BB]

In this scenario, both platforms use blockchain technology to verify the truthfulness of their disclosed information. Thus, consumers believe that the additional information from both platforms is accurate and authentic. Platforms need to pay for blockchain technology at $c _ { B }$ per unit. Thus, the profit is as follows:

$$
\pi_ {i} ^ {B B} = \left(p _ {i} - c - c _ {B}\right) \cdot D _ {i} ^ {B B} - t \cdot b _ {i} ^ {2} / 2, i = 1, 2, j = 3 - i.\tag{8}
$$

Following a similar procedure, the equilibrium solutions in the BB scenario are summarized in the following proposition.

Proposition 3. For the BB scenario, the optimal selling prices and the corresponding optimal amounts of disclosed information are:

$$
\begin{array}{l} p _ {1} ^ {B B} = p _ {2} ^ {B B} = \frac {(a + c + c _ {B}) t - (1 - \gamma) (c + c _ {B})}{(2 - \beta) t - (1 - \gamma)}, b _ {1} ^ {B B} = b _ {2} ^ {B B} \\ = \frac {a + (\beta - 1) (c + c _ {B})}{(2 - \beta) t - (1 - \gamma)} \end{array}
$$

and the corresponding profits are:

$$
\pi_ {1} ^ {B B} = \pi_ {2} ^ {B B} = \frac {t (2 t - 1) (a + (\beta - 1) (c + c _ {B})) ^ {2}}{2 ((2 - \beta) t - (1 - \gamma)) ^ {2}}.
$$

Note that in the BB scenario, consumers’ belief in the disclosed in formation is equal to 1. The equilibrium solutions are all influenced by the unit blockchain cost. From Proposition 3, we can obtain Corollary 3 as follows:

## Corollary 3. For the BB scenario, we have $\begin{array} { r } { \frac { d p _ { i } ^ { B B } } { d c _ { B } } > 0 , \frac { d b _ { i } ^ { B B } } { d c _ { B } } < 0 , \frac { d \pi _ { i } ^ { B B } } { d c _ { B } } < 0 . } \end{array}$

When both platforms choose to use blockchain technology simulta neously, the monotonicity of the equilibrium solutions is different from the BN scenario, especially for the platform that also adopts blockchain in the BN case. Specifically, as the cost of blockchain technology increazes, the selling prices increaze as well. However, the selling price for platform i in the BN case additionally depends on the demand sensitivity of both the selling price and amount of disclosed information. For platform j, when this platform applies blockchain as platform i does, it tends to release more information when the blockchain cost decreazes. Finally, with the increasing blockchain cost, although the two platforms can improve their selling prices to transfer the incremental cost to consumers and decreaze the amount of disclosed information to save on the information cost, they are worse off. In other words, reducing the blockchain costs is mutually preferable for platforms and consumers because the former can be more profitable and the latter can obtain lower prices with more accurate and authentic information.

Lemma 2. Comparing case BN with case BB:

(1) There are two critical values of blockchain cost $c _ { 2 } ^ { * }$ and $c _ { 2 } ^ { b }$ that if $0 \leq c _ { B } \leq c _ { 2 } ^ { * } ,$ , then $b _ { j } ^ { B B } > b _ { j } ^ { B N }$ and $\pi _ { j } ^ { B B } \geq \pi _ { j } ^ { B N } ; i f c _ { 2 } ^ { * } < c _ { B } < c _ { 2 } ^ { b } ,$ , then $b _ { j } ^ { B B }$ $> b _ { j } ^ { B N }$ and $\pi _ { j } ^ { B B } < \pi _ { j } ^ { B N } ;$ otherwise, $i f c _ { 2 } ^ { b } \leq c _ { B } < \operatorname* { m i n } \{ \overline { { { c _ { 1 } } } } , \overline { { { c _ { 2 } } } } \}$ , then $b _ { j } ^ { B B } \leq b _ { j } ^ { B N }$ and $\pi _ { j } ^ { B B } < \pi _ { j } ^ { B N } ;$

(2) There is a critical value of blockchain cost $c _ { 2 } ^ { + }$ such that $i f 0 \leq c _ { B } < c _ { 2 } ^ { + }$ then $b _ { i } ^ { B B } < b _ { i } ^ { B N }$ and $\pi _ { i } ^ { B B } < \pi _ { i } ^ { B N } ; i f c _ { 2 } ^ { + } < c _ { B } <$ < min{c , c }, then $b _ { i } ^ { B B } \geq$ $b _ { i } ^ { B N }$ and $\pi _ { i } ^ { B B } \geq \pi _ { i } ^ { B N }$

The first part of Lemma 2 summarizes one platform’s (platform j) blockchain adoption strategy given that the other platform (platform i) uses blockchain technology to authenticate the information. On the one hand, when the unit blockchain cost is small, platform j tends to provide more authentic information if it chooses to adopt blockchain technology as platform i does, and this decision is also beneficial. However, now, platform i, which already applies blockchain technology, may be hurt (i. $\mathrm { e } . , c _ { B } < \operatorname* { m i n } \{ c _ { 2 } ^ { * } , c _ { 2 } ^ { + } \}$ , see part 2 of Lemma 2), and platform j’s actions will lead to platform i reducing the amount of authentic information to the market as a response. The reason is that when the competing platform applies blockchain technology as well, the advantage of improving consumers’ beliefs decreazes; thus, it is better to decreaze the amount of information to save on the information cost. In this case, platform $j ^ { \prime } s$ adoption decision hurts platform i. On the other hand, a high unit blockchain cost will lead to less authentic information releazed by platform j adopting this technology, which will also lead to less profit. In contrast, platform $\cdot \ i ,$ which uses blockchain technology, may be better off $( \mathrm { i . e . , } ~ c _ { B } > \operatorname* { m a x } \{ c _ { 2 } ^ { b } , c _ { 2 } ^ { + } \} )$ , and platform $j ^ { \prime } s$ behavior will encourage plat form i to release more authentic information to the market. The reason is that despite the high cost of blockchain technology, platform j still adopts this technology. Right now, for platform $j ,$ it is unnecessary to release more information than in the nonblockchain case $( b _ { j } ^ { B B } \leq b _ { j } ^ { B N } )$ However, all the information it releases is authentic. Therefore, to maintain a competitive advantage. platform i needs to disclose more information than before. Apparently, in this case, platform $j ^ { \prime } s$ adoption decision makes platform i better off. Finally, when the unit blockchain cost is at the intermediate level, if platform j decides to adopt blockchain technology, it needs to disclose more authentic information but decreazes profit compared with the situation without blockchain tech nology. Therefore, when the unit blockchain exceeds a threshold value $( \mathrm { i } . \mathrm { e } . , c _ { 2 } ^ { * } )$ , it prevents the platform from adopting this new technology.

Lemma 3. Comparing case BB with case NN, there are two critical values $o f$ the blockchain cost such that $i f \ 0 \leq c _ { B } \leq c _ { 3 } ^ { * } ,$ , then $b _ { i } ^ { B B } \ > b _ { i } ^ { N N }$ and $\pi _ { i } ^ { B B } \geq \pi _ { i } ^ { N N } ; ~ i f ~ c _ { 3 } ^ { * } < c _ { B } < c _ { 3 } ^ { b } .$ , then $b _ { i } ^ { B B } > b _ { i } ^ { N N }$ and $\pi _ { i } ^ { B B } < \pi _ { i } ^ { N N } .$ ; otherwise, $i f$ $c _ { 3 } ^ { b } \leq c _ { B } < \overline { { c _ { 2 } } } ,$ , then $b _ { i } ^ { B B } \leq b _ { i } ^ { N N }$ and $\pi _ { i } ^ { B B } < \pi _ { i } ^ { N N }$

Lemma 3 discusses the common motivation of both platforms to adopt blockchain technology. It is also a threshold strategy. When the unit blockchain cost is small, both platforms benefit from blockchain technology, and they are encouraged to release more accurate and authentic information than the case without blockchain technology. Therefore, the total amount of information releazed to the market is not only sufficient but also authentic.

## 4.4. Equilibrium adoption strategy

Because $\pi _ { j } ^ { N N } = \pi _ { i } ^ { N N } , \pi _ { i } ^ { N B } = \pi _ { j } ^ { B N } , \pi _ { j } ^ { N B } = \pi _ { i } ^ { B N }$ , and $\pi _ { i } ^ { B B } ~ = \pi _ { j } ^ { B B }$ , from Lemmas 1(1) and $^ { 2 , }$ , we can directly obtain the following conclusions.

Proposition 4. The equilibrium blockchain strategies are characterized a follows:

(1) if $0 \le c _ { B } <$ < min $\{ c _ { 1 } ^ { * } , ~ c _ { 2 } ^ { * } \}$ , the equilibrium strategy is that both platforms adopt blockchain technology;

(2) if max $\{ c _ { 1 } ^ { * } , c _ { 2 } ^ { * } \} \le c _ { B }$ < min $\left\{ \overline { { c _ { 1 } } } , \overline { { c _ { 2 } } } \right\}$ , the equilibrium strategy is that neither platform adopts blockchain technology;

(3) If min $\{ c _ { 1 } ^ { * } , c _ { 2 } ^ { * } \} \leq c _ { B } < \operatorname* { m a x } \{ c _ { 1 } ^ { * } , c _ { 2 } ^ { * } \}$ , the mixed strategy will make the two platforms better off compared with the BB or NN strategy.

From Lemmas 1(1) and 2, we can directly prove this proposition. The equilibrium strategies critically depend on the blockchain cost. Both platforms will choose to apply blockchain technology (nonblockchain) if the unit blockchain cost is low (high), while a mixed strategy will take place if the cost lies in the intermediate area. The reason for the mixed blockchain adoption strategy is twofold. (1) When one platform decides to apply blockchain technology to authenticate the disclosed informa tion, there is the incentive for the other platform to ignore this tech nology to save on the blockchain cost. Although not using blockchain technology will come with the detriment of consumers’ distrust of the disclosed information, the platform can provide more information (see Lemma 1(3)) to stimulate the demand, which further alleviates thi disadvantage. (2) When one platform decides to ignore blockchain technology, it is beneficial for the other platform to implement block chain technology to authenticate the disclosed information to improve consumers’ beliefs and increaze the demand. Although applying the technology will bear a blockchain cost, the platform can disclose more authentic information than before and, hence, be better off (see Lemma 1(1)). In other words, because of the externalities of blockchain tech nology, it can benefit both platforms simultaneously, regardless of which one platform uses the technology. In addition, there is more ac curate and authentic information than unconfirmed information in the market.

The above proposition only discusses the impact of the blockchain cost on the equilibrium strategy; however, we can see that the critical values of the blockchain cost are all related to consumers’ beliefs. Because of the infeasibility of deriving the analytical threshold values as the blockchain cost, we resort to a numerical study to illustrate the impact of consumers’ beliefs and the blockchain cost on the equilibrium strategies. In general, we arbitrarily seta $= 5 0 , c = 5 , t = 1 , \beta = 0 . 8 ,$ and $\gamma = 0 . 4 ,$ , assume δ and $c _ { B }$ are uniformly distributed, and take 21 values from 0–1 and $0 { - } 5 0 ,$ , respectively.<sup>4</sup> The numerical results are shown in Fig. 1.

Despite the complexity of deriving the threshold values of consumers’ beliefs on the equilibrium strategies, Fig. 1 explicitly depicts the correlation between consumers’ beliefs and blockchain adoption stra tegies; it also demonstrates a threshold-type structure. Specifically, given the unit blockchain cost, when consumers show less trust in the information, it is always beneficial for at least one platform to apply this new technology; when consumers’ beliefs are greater, it is better to ignore blockchain technology.

![](/api/attachments/PC25MHJZ/fulltext/images/f53b1fdebe04545009bb5f7d7f41dc900370ec40b2addde5431a87903083ff5d.jpg)  
Fig. 1. Equilibrium blockchain adoption strategies.

From the figure, we can see that the blockchain cost plays a more important role than consumers’ beliefs when deciding whether to adopt this technology. Even though platforms bear a dramatically low level of consumer belief, if the blockchain cost is very high, it is not a good idea to apply blockchain technology to authenticate information. This is mainly because the effect of the blockchain cost dominates the effect of consumers’ distrust of the disclosed information. Although consumers may not trust what platforms have releazed to the public, platforms can choose to disclose more information to reduce this weakness. Addi tionally, even without considering the high blockchain cost, to be better off, applying blockchain technology means that the platform needs to release more authentic information than in the nonblockchain case (see Lemma 1(1)), which results in a higher information cost.

## 5. Some extensions

The above conclusions are obtained under some restrictive assump tions, such as the two platforms sharing equal power and moving simultaneously, the blockchain cost being constant, and the upstream suppliers not being incorporated. To examine whether our conclusions can be generalizable, we consider the extensions below.

## 5.1. Stackelberg game

In this section, we consider the case in which the two platforms play the Stackelberg game, with one platform moving first and the other one moving sequentially. Without loss of generality, we assume that plat form i is the leader that makes decisions first and platform j is the fol lower that makes its decisions subsequently. The decision sequence is as follows. First, platform i, acting as the leader, decides whether to adopt blockchain technology to authenticate the information and then de termines its selling price and amount of disclosed information; second, after observing platform i’s decisions, platform j, which is the follower, decides whether to use blockchain technology and then determines its selling price and amount of disclosed information; finally, the market demand comes. We use backward induction to derive the equilibrium solutions.

Because the decisions are sequentially made between two platforms, there are four subcases: (1) both platforms do not apply blockchain technology, which is labeled Strategy-[SNN]; (2) only platform i chooses to apply blockchain technology, which is labeled Strategy-[SBN]; (3) only platform j chooses to apply blockchain technology, which is labeled Strategy-[SNB]; and (4) both platforms choose to apply blockchain technology, which is labeled Strategy-[SBB]. In what follows, we discuss the four cases one after the other. For the sake of simplicity, we move all the derivation procedures and optimal results in the appendix and only discuss the equilibrium strategy.

Proposition 5. The equilibrium information disclosure strategies in the Stackelberg game are as follows:

(1) In Strategy-[SNN], $\begin{array} { r } { b _ { S i } ^ { N N } = \frac { ( A _ { S 1 } - c B _ { S 1 } ) E _ { S 1 } } { t B _ { S 1 } - E _ { S 1 } ^ { 2 } } } \end{array}$ and $\begin{array} { r } { b _ { S j } ^ { N N } = \frac { ( a - c + \beta p _ { S i } ^ { N N } - \gamma \delta b _ { S i } ^ { N N } ) \delta } { 2 t - \delta ^ { 2 } } ; } \end{array}$

(2) In Strategy- $\begin{array} { r } { [ \mathrm { S B N } ] , b _ { S i } ^ { B N } = \frac { ( A _ { S 2 } - ( c + c _ { B } ) B _ { S 1 } ) E _ { S 2 } } { t B _ { S 1 } - E _ { S 2 } ^ { 2 } } \mathrm { a n d } ~ b _ { S j } ^ { B N } = \frac { ( a - c + \beta p _ { S i } ^ { B N } - \gamma b _ { S i } ^ { B N } ) \delta } { 2 t - \delta ^ { 2 } } \mathrm { ; } } \end{array}$

(3) In Strategy-[SNB], $\begin{array} { r } { b _ { S i } ^ { N B } = \frac { ( A _ { S 3 } - c B _ { S 2 } ) E _ { S 3 } } { t B _ { S 2 } - E _ { S 3 } ^ { 2 } } \mathrm { a n d } b _ { S j } ^ { N B } = \frac { a - ( c + c _ { B } ) + \beta p _ { S i } ^ { N B } - \delta \gamma b _ { S i } ^ { N B } } { 2 t - 1 } ; } \end{array}$

(4) In Strategy- $\begin{array} { r l } { \cdot [ \mathrm { S B B } ] , b _ { S i } ^ { B B } \ = \ } & { { } \frac { \left( A _ { S 4 } - ( c + c _ { B } ) B _ { S 2 } \right) E _ { S 4 } } { t B _ { S 2 } - E _ { S 4 } ^ { 2 } } \mathrm { a n d } b _ { S j } ^ { B B } } \end{array}$ 一$\frac { a - ( c + c _ { B } ) + \beta p _ { S i } ^ { B B } - \gamma b _ { S i } ^ { B B } } { 2 t - 1 } ;$

where $A _ { S m } , B _ { S k } , E _ { S m } , p _ { S i } ^ { N N } , p _ { S i } ^ { B N } , p _ { S i } ^ { N B }$ , and $p _ { S i } ^ { B B }$ are shown in the appendix, $m { = } l ,$ 2, 3, 4, and k=1, 2.

This conclusion can be summarized from Propositions A1–A4 in the

appendix.

Because of complexity, it is intractable to analyze the monotonicity of the equilibrium solutions. Alternatively, we resort to a numerical study for the analysis. Using the same data as in Section 4.3, we demonstrate the follower platform’s blockchain adoption strategy.

Because the follower platform, platform $j ,$ can make its decisions after observing the dominant platform’s (platform i) decisions, the fol lower platform’s adoption strategy should closely rely on the dominant platform’s choice. However, Fig. 2(a) shows that regardless of whether the dominant platform applies blockchain technology, in the upper right-hand side section, the follower platform will never use blockchain technology to authenticate its information; likewise, in the lower lefthand side section, the platform always has the incentive to apply blockchain technology. In these two sections, the corresponding strategy is also the follower platform’s dominant blockchain adoption strategy. Only in the middle area, which is a relatively small section compared with the upper and lower sections, does the follower platform’s decision depend on the dominant platform’s choice.

Fig. 2(b) demonstrates the dominant platform’s blockchain adoption strategy. As the leading platform, platform i can choose whether to adopt blockchain technology to authenticate its information by considering consumers’ beliefs and blockchain costs. Because the dominant platform makes decisions in the first stage, it also needs to predict how the follower platform will react after observing its decisions. Consequently, in the area where the follower platform has to wait for the dominant platform’s decision (the intermediate section in Fig. 2(a)), the leader platform i needs to assess which strategy, B or N, is better for platform j if it chooses B or N. After balancing which strategy is platform j’s best response action, the dominant platform can evaluate which strategy is better. We summarize the conclusions in the following Fig. 3 (a).

Fig. 3(a) reveals the equilibrium blockchain adoption strategy. Similarly, the strategy is a threshold-type policy again. In equilibrium, both platforms will choose to adopt blockchain technology to authen ticate their information when the blockchain cost and consumers’ belief lie on the lower left-hand side of Fig. 3(a); however, neither of them will apply this technology when the cost and belief are within the upper right-hand side of Fig. 3(a). In the middle area, anticipating how the follower platform will respond, platform i decides to choose blockchain technology, in which platform j is better off if it ignores blockchain technology after observing that platform i uses the technology. Conse quently, in this scenario, the BN strategy achieves equilibria<sup>5</sup>.

## 5.2. Variable information cost

Usually, disclosing information incurs checking, verifying, and updating costs to ensure that the information is accurate; thus, we consider the unit cost of disclosing information in this extension.

We redefine c as the variable information cost when blockchain technology is not applied, and $c _ { B }$ is the variable information cost pre mium when blockchain technology is adopted. Using the demand defined in Section $^ { 4 , }$ we know that when both platforms ignore block chain technology, their objective functions are as follows:

$$
\pi_ {V, i} ^ {N N} = (p _ {i} - c \cdot b _ {i}) \cdot D _ {i} ^ {N N} - t \cdot b _ {i} ^ {2} / 2, i = 1, 2,
$$

where the subscript V refers to the variable information cost case.

When only one of the two platforms applies blockchain technology to authenticate the information, the objective functions are as follows:

$$
\pi_ {V, i} ^ {B N} = (p _ {i} - (c + c _ {B}) \cdot b _ {i}) \cdot D _ {i} ^ {B N} - t \cdot b _ {i} ^ {2} / 2,
$$

![](/api/attachments/PC25MHJZ/fulltext/images/0c1b3fbdf2aea1c10a87aa1633e3cc6a100bb8c160b433a6e0c180043b075a12.jpg)  
(a) Platform j

![](/api/attachments/PC25MHJZ/fulltext/images/c3e2e976cf48afcf69bb2a63371ace52598cffe6f3dbc265773a7ef429fdd4a9.jpg)  
(b) Platform i

Fig. 2.. Blockchain adoption strategy.  
![](/api/attachments/PC25MHJZ/fulltext/images/135b49c1eff6cfa95d9e719675ca45a747114f2fee3eb6db424c6a419a5a9f32.jpg)  
(a) Stackelberg game

![](/api/attachments/PC25MHJZ/fulltext/images/82b5ac2b63a9ae2c81a0e1ec5c2c88b207de9cf7d2ff736f7b03e34e5122d8b7.jpg)  
(b) Variable information cost  
Fig. 3. Equilibrium blockchain adoption strategy.

$$
\pi_ {V, j} ^ {B N} = \left(p _ {j} - c \cdot b _ {i}\right) \cdot D _ {j} ^ {B N} - t \cdot b _ {j} ^ {2} / 2.
$$

Finally, when both platforms implement blockchain technology simultaneously, the corresponding objective functions are as follows:

$$
\pi_ {V, i} ^ {B B} = \left(p _ {i} - \left(c + c _ {B}\right) \cdot b _ {i}\right) \cdot D _ {i} ^ {B B} - t \cdot b _ {i} ^ {2} / 2, i = 1, 2, j = 3 - i.
$$

Following a similar procedure stated in Section $^ { 4 , }$ we can obtain the equilibrium information disclosure strategies as follows.

Proposition 6. The equilibrium information disclosure strategies when considering variable information costs are as follows:

(1) In Strategy-[VNN], $\begin{array} { r } { b _ { V i } ^ { N N } = \frac { ( \delta - c ) a } { ( 2 - \beta ) ( ( 2 - \gamma ) c \delta + t ) - ( ( 1 - \beta ) c + \delta ) ( ( 1 - \gamma ) \delta + c ) } ; } \end{array}$

(2) In Strategy-[VBN]/[VNB], $\begin{array} { r } { \begin{array} { r } { b _ { V i } ^ { B N } = \frac { A _ { 1 } B _ { 2 2 } - A _ { 2 } B _ { 2 1 } } { B _ { 1 2 } B _ { 2 1 } - B _ { 1 1 } B _ { 2 2 } } , b _ { V j } ^ { B N } = \frac { A _ { 2 } B _ { 1 1 } - A _ { 1 } B _ { 1 2 } } { B _ { 1 2 } B _ { 2 1 } - B _ { 1 1 } B _ { 2 2 } } ; } \end{array} } \end{array}$

(3) In Strategy- $\begin{array} { r } { [ \nabla \mathrm { B B } ] , b _ { V i } ^ { B B } \ = \frac { ( 1 - c - c _ { b } ) a } { ( 2 - \beta ) ( ( 2 - \gamma ) ( c + c _ { b } ) + t ) - ( c + c _ { b } + 1 - \gamma ) ( ( c + c _ { b } ) ( 1 - \beta ) + 1 ) } . } \end{array}$

This proposition can be summarized from Propositions $A 5 { - } A 7$ in the appendix.

However, unfortunately, it is too complicated to derive the optimal blockchain adoption strategies for both platforms. Instead, we resort to a numerical study to illustrate the equilibrium strategy. To confirm the outcomes derived from the numerical analysis, we choose $c = 0 . 3 , 0 . 3 5 ,$ $0 . 4 , 0 . 4 5 , 0 . 5 , 0 . 5 5 , \mathrm { a n d } 0 . 6 ; c _ { B } = 0 . 4 , 0 . 4 5 , 0 . 5 , 0 . 5 5 , \mathrm { a n d } 0 . 6 ; \gamma = 0 . 3 5 , \nonumber$ $0 . 4 , 0 . 4 5 , 0 . 5 , 0 . 5 5 , 0 . 6 , 0 . 6 5 ;$ and $\delta = 0 . 3 5 , 0 . 4 , 0 . 4 5 , 0 . 5 , 0 . 5 5 , 0 . 6 ,$ 0.65, and $0 . 7 ^ { 6 }$ . For each pair of parameters, we change the value of the consumers’ belief and blockchain cost to examine the equilibrium blockchain technology adoption strategies; for example, when $c = 0 . 4 { \mathrm { : } }$ $\gamma = 0 . 5 ,$ , δ and $c _ { B } ,$ , respectively, we take 21 discrete values from 0.4 to 1 and from 0 to 0.6. Because the numerical results show no qualitative change in our conclusions when using different parameter values, we choose this case as a representative example. The equilibrium block chain adoption strategies are shown in Fig. 3(b), which is similar to the conclusions derived in Section 4.

## 5.3. Supply chain model

Typically, because of bilateral transactions, it is difficult to achieve validation in the supply chain. However, validation is one of the key strengths of blockchain technology, which will enhance the trust of supply chain members in shared information [3]. For example, Maersk and IBM jointly developed a platform for global trade that uses block chain technology to improve the trust and information transparency of supply chain partners and increaze transaction efficiency [29]. There fore, in this extension, we incorporate upstream suppliers and consider the case where two suppliers produce substitutable products for their exclusive platform that competes in the market. Specifically, supplier i supplies product i at unit cost $c _ { s }$ for its exclusive platform i at the unit wholesale price w . Platform i decides whether to adopt blockchain technology to authenticate its disclosed information and sells the product in the market at unit price w + $- U _ { i } ,$ where $U _ { i }$ is the fixed markup price determined by platform i. For simplicity, we assume suppliers and platforms make their decisions simultaneously. This is actually a competitive supply chain model, with the platforms being the Stackel berg leader.

When neither of the two platforms uses blockchain technology, the objective functions for suppliers and retailers are as follows:

$$
\pi_ {C, S i} ^ {N N} = (w _ {i} - c _ {S}) \cdot D _ {i} ^ {N N}, i = 1, 2,
$$

$$
\pi_ {C, R i} ^ {N N} = (U _ {i} - c) \cdot D _ {i} ^ {N N} - t \cdot b _ {i} ^ {2} / 2, i = 1, 2,
$$

where the subscript C refers to the supply chain model, S stands for the supplier, R represents the platform, and $\scriptstyle { p _ { i } = w _ { i } + U _ { i } }$

When only one of two platforms adopts blockchain technology to authenticate the information, the objective functions for suppliers and platforms are as follows:

$$
\pi_ {C, S i} ^ {B N} = (w _ {i} - c _ {S}) \cdot D _ {i} ^ {B N}, i = 1, 2,
$$

$$
\pi_ {C, R i} ^ {B N} = (U _ {i} - c - c _ {B}) \cdot D _ {i} ^ {B N} - t \cdot b _ {i} ^ {2} / 2,
$$

$$
\pi_ {C, S j} ^ {B N} = \left(w _ {j} - c _ {S}\right) \cdot D _ {j} ^ {B N}, j = 3 - i,
$$

$$
\pi_ {C, R j} ^ {B N} = (U _ {j} - c) \cdot D _ {j} ^ {B N} - t \cdot b _ {j} ^ {2} / 2.
$$

When both platforms decide to apply blockchain technology, the corresponding objective functions are as follows:

$$
\pi_ {C, S i} ^ {B B} = (w _ {i} - c _ {S}) \cdot D _ {i} ^ {B B}, i = 1, 2,
$$

$$
\pi_ {C, R i} ^ {B B} = (U _ {i} - c - c _ {B}) \cdot D _ {i} ^ {B B} - t \cdot b _ {i} ^ {2} / 2, i = 1, 2.
$$

Again, following a similar process and with some algebra, the optimal information disclosure strategies are as follows:

Proposition 7. The equilibrium information disclosure strategies $f o r$ platforms under two competing supply chains are as follows:

(1) In Strategy- $\begin{array} { r } { { \cdot } [ \mathrm { C N N } ] , b _ { C , i } ^ { N N } = \frac { a - ( 1 - \beta ) ( c + c _ { S } ) } { ( 3 - 2 \beta ) t + ( \gamma - 1 ) \delta ^ { 2 } } \delta , } \end{array}$

(2) In Strategy-[CBN]/[CNB], $\begin{array} { r } { b _ { C i } ^ { B N } = \frac { A _ { C 1 } A _ { C 6 } - A _ { C 4 } A _ { C 3 } } { A _ { C 5 } A _ { C 3 } - A _ { C 2 } A _ { C 6 } } , b _ { C j } ^ { B N } = \frac { A _ { C 4 } A _ { C 2 } - A _ { C 1 } A _ { C 5 } } { A _ { C 5 } A _ { C 3 } - A _ { C 2 } A _ { C 6 } } , } \end{array}$

(3) In Strategy-[CBB], $\begin{array} { r } { b _ { C 1 } ^ { B B } = b _ { C 2 } ^ { B B } = \frac { a - ( 1 - \beta ) ( c + c _ { B } + c _ { S } ) } { 2 ( 1 - \beta ) t + t + \gamma - 1 } , } \end{array}$

where $i = 1 , 2 , j = 3 - i $

This proposition can be summarized from Propositions A8–A10 in the appendix.

Because of the complexity, we also conduct a numerical study to investigate equilibrium blockchain adoption strategies. Using the same parameter values in Section $^ { 4 , }$ we obtain the platforms’ equilibrium blockchain adoption strategy and suppliers’ blockchain preference, as shown in Fig. 4. Here, the equilibrium strategy is the same as that for the base case summarized in Section 4.4, thus showing that the upstream suppliers do not lead to a qualified difference.

It is worth noting that the platforms are responsible for blockchain technology adoption strategies in the chain-to-chain competition model. The platform only needs to focus on whether the adoption of blockchain technology can benefit itself, regardless of whether the technology is also beneficial to upstream suppliers. Nevertheless, we find that the decision of the platform may also benefit suppliers. For example, for the overlapped part of Fig. 4(a) and (b), the upper right (lower left) area indicates that forgoing (applying) blockchain technology will benefit both suppliers and platforms.

## 6. Conclusions and future research

Blockchain technology can authenticate each transaction and elim inate consumers’ doubts about retailers’ disclosed information. In the current paper, we have examined the equilibrium information disclo sure policy and blockchain adoption strategy by considering two plat forms selling two substitutable products and playing the Nash game, in which there are three cases: (1) both platforms ignore blockchain technology (case NN), and thus consumers doubt the platforms’ dis closed information; (2) one of the platforms adopts blockchain tech nology (case BN or/and NB), in which case one of the platforms uses blockchain technology and consumers believe that only the information from this platform is accurate; and (3) both platforms adopt blockchain technology (case BB), in which the two platforms have to pay for the blockchain cost and consumers believe that all the information is accurate.

We formulated the platforms’ objective functions in each case, analyzed the corresponding optimal information disclosure policy, and derived the equilibrium blockchain adoption strategies. The results show that there are two threshold values for the blockchain cost. First, when the blockchain cost is less than a small cost, the dominant strategy for both platforms is to adopt blockchain technology to authenticate disclosed information, and here, the amount of information is greater than that of the nonblockchain case. This indicates that applying blockchain technology not only benefits both platforms but also brings more authentic information to the market. However, when the cost is

![](/api/attachments/PC25MHJZ/fulltext/images/c0f3bbe69fa90c2330b6f993a75ffe91a64cf0360e5d3e36b786874ddfcc6dd8.jpg)  
(a) Platforms'Equilibrium

![](/api/attachments/PC25MHJZ/fulltext/images/b345442dbe29c86c86570ea6c9dc254063fcb7eaed9dd20d14cce75e4ce04263.jpg)  
(b) Suppliers' Preference  
Fig. 4.. Equilibrium blockchain adoption strategy/preference.

[11 H. Allcott. R.J. Sweeney. The role of sales agents in information disclosure: evidence from a field experiment. Manag, Sci, 63 (1) (2017) 21–39

larger than the larger cost, the dominating strategy for both platforms is to ignore blockchain technology, and the market will thus be crowded with unauthenticated information. When the cost is between the two values, a mixed strategy occurs. In the mixed strategy, the strategy that adopts blockchain technology may tend to release more information than when it does not use blockchain technology. Furthermore, it may also have the incentive to release more authentic information than a platform that does not apply blockchain technology. Because of the complexity of these situations, we conduct an extensive numerical analysis of the results. We found that the impact of consumers’ beliefs on the information disclosure policy and equilibrium blockchain adoption strategy is less than that of the blockchain cost. Our conclusion reveals that blockchain technology may not only benefit the platform using it but also provide more authentic and reliable information for the market. To check the robustness of our conclusions, we extended the analysis to three cases: the Stackelberg game case, the variable blockchain cost case, and the supply chain case. Because the expressions are more so phisticated than those in the Nash game, we conducted an extensive numerical study. We found that the main conclusions are still valid.

In the current paper, we have focused on the deterministic demand to derive the information disclosure policy and the equilibrium blockchain strategies. The first direction of future research is to extend the model to cover the stochastic demand with multiple players, such as upstream suppliers, to investigate who has the incentive to apply blockchain technology, i.e., the supplier or the platform. We can also identify the conditions under which a supply chain could be coordinated when a supplier or platform chooses to apply blockchain technology. In addi tion, it would also be an interesting direction to examine the perfor mance differences under different supply chain and power structures. Finally, information sharing between the two platforms is a valuable topic to pursue.

## Author statement

In the cooperation process of the article, I was mainly responsible for the model development and the derivation and calculation of the analytical and numerical results, while Prof. Yao-Yu Wang was mainly responsible for the interpretation of the results and the writing of the article. Prof. Jiancai Wang was mainly responsible for the re-calculation and the language of the paper. We confirm that this study has not been submitted to other journals before, and has no copyright and ethical problems. We agree to be accountable for all aspects of the study in ensuring that questions related to the accuracy or integrity of any part of the study are appropriately investigated and resolved.

## Acknowledgment

The research was supported in part by National Natural Science Foundation of China (Grant Nos. 71872064, 72071137, 71671119 and 71871024), in part by Shanghai Pujiang Program (Grant No. 18PJC025), in part by The Ministry of Education of Humanities and Social Science Project (Grant No. 18YJAZH046), in part by Qinglan Project of Jiangsu Province, and in part by Zhongying Young Scholar Project.

## Supplementary materials

Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.im.2021.103506.

## References

[2] S. Ba, Establishing online trust through a community responsibility system, Decis.

[3] V. Babich, G. Hilary, Distributed ledgers and operations: what operations management researchers should know about blockchain technology, Manuf. Serv. Oper. Manag. 22 (2) (2020) 223–240.

[4] C. Bai, J. Sarkis, A supply chain transparency and sustainability technology appraisal model for blockchain technology, Int. J. Prod. Res. 58 (7) (2020) 2142–2162.

[5] A. Basu, S. Bhaskaran, R. Mukherjee, An analysis of search and authentication strategies for online matching platforms. Manag, Sci. 65 (5) (2019) 2412–2431

[6] E. Branco. M. Sun. J.M. Villas-Boas. Too much information? Information provision and search costs, Mark, Sci. 35 (4) (2016) 605–618

[7] A.A. Choi, D. Cho, D. Yim, J.Y. Moon, W. Oh, When seeing helps believing: the interactive effects of previews and reviews on e-book purchases, Inf. Syst. Res. 30 (4) (2019) 1164–1183.

[8] T.M. Choi, L. Feng, R. Li, Information disclosure structure in supply chains with rental service platforms in the blockchain technology era, Int. J. Prod. Econ. 221 (2020), 107473.

[9] L. Chu, H. Zhang, Optimal preorder strategy with endogenous information control, Manag, Sci, 57 (6) (2011) 1055–1077.

[10] K. Christidis, M. Devetsikiotis, Blockchains and smart contracts for the internet of things, IEEE Access 4 (2016) 2292–2303.

[11] A. Dolgui, D. Ivanov, S. Potryasaev, B. Sokolov, M. Ivanova, F. Werner, Blockchainoriented dynamic modelling of smart contract design and execution in the supply chain, Int. J. Prod. Res. 58 (7) (2020) 2184–2199.

[12] L. Gao, Z. Li, B. Shou, Information acquisition and voluntary disclosure in an export-processing system, Prod. Oper. Manag. 23 (5) (2014) 802–816.

[13] Z.J. Gu, Y. Xie, Facilitating fit revelation in the competitive market, Manag. Sci. 59 (5) (2013) 1196–1212.

[14] X. Guan, Y. Wang, Z. Yi, Y.J. Chen, Inducing consumer online reviews vi disclosure, Prod. Oper. Manag. (2020), https://doi.org/10.1111/poms.13199.

[15] L. Guo, Y. Zhao, Voluntary quality disclosure and market interaction, Mark. Sci. 28 (3) (2009) 488–501.

[16] G.M. Hastig, M.S. Sodhi, Blockchain for supply chain traceability: business requirements and critical success factors, Prod. Oper. Manag. 29 (4) (2020) 935–954.

[17] M. Iansiti, K.R. Lakhanl, The truth about blockchain, Harv. Bus. Rev. 95 (1) (2017) 118–127.

[18] J.W. Kim, J.H. Lim, IT investments disclosure, information quality, and factors influencing managers’ choices, Inf. Manag. 48 (2011) 114–123.

[19] S.Y. Lee, L. Qiu, A. Whinston, Sentiment manipulation in online platforms: an analysis of movie tweets, Prod.Oper. Manag. 27 (3) (2018) 393–416.

[20] H. Li, X. Shi, Discriminatory information disclosure, Am. Econ. Rev. 107 (11) (2017) 3363–3385.

[21] McKenzie, J. (2018). Why blockchain won’t fix food safety-yet. https://thecounter. org/blockchain-food-traceability-walmart-ibm/ The Counter 5 Yegrs. [Accessed on 29 November. 2020l

[22] D.H. McKnight, V. Choudhury, C. Kacmar, Developing and validating trust measures for e-commerce: an integrative typology, Inf. Syst. Res. 13 (3) (2002) 334–359.

[23] P. Milgrom, What the seller won’t tell you: persuasion and disclosure in markets,

[24] S. Mondal, K.P. Wijewardena, S. Karuppuswami, N. Kriti, D. Kumar, P. Chahal, Blockchain inspired RFID-based information architecture for food supply chain, IEEE Internet Things J. 6 (3) (2019) 5803–5813.

[25] Mougayar, W. (2015). A decision tree for blockchain applications: problems, opportunities or capabilities? Startup Management. http://startupmanagement.org/ 2015/11/30/a-decision-tree-for-blockchain-applications-problems-opportunities-o r-capabilities/ [Accessed on 30 November, 2020]

[26] Nakamoto, S. (2008). Bitcoin: a peer-to-peer electronic cash system. Bitcoin. http:// bitcoin.org/en/bitcoin-paper. [Accessed on 29, May, 2020].

[27] M. Pournader, Y. Shi, S. Seuring, S.C.L. Koh, Blockchain applications in supply chains, transport and logistics: a systematic review of the literature, Int. J. Prod. Res. 58 (7) (2020) 2063–2081.

[28] S. Saberi, M. Kouhizadeh, J. Sarkis, Blockchain technology: a panacea or pariah for resources conservation and recycling, Resour. Conserv. Recycl. 130 (2018) 80–81.

[29] Scott, T. (2018). TradeLens: how IBM and Maersk are sharing blockchain to build a global trade platform. IBM Think Blog. https://www.ibm.com/blogs/think/2018/ 11/tradelens-how-ibm-and-maersk-are-sharing-blockchain-to-build-a-global-trade platform/ [Accessed on 30, November, 2020].

[30] J.D. Shulman, T.C. Anne, R.C. Savaskan, Optimal restocking fees and information Oper. Manag. 11 (4) (2009) 577–594.

[31] Y. Wang, J.H. Han, B.D. Paul, Understanding blockchain technology for future supply chains: a systematic literature review and research agenda, Supply Chain Manag. An Int. J. 24 (1) (2019) 62–84.

[32] Y. Wang, M. Singgih, J. Wang, M. Rit, Making sense of blockchain technology: how will it transform supply chains? Int. J. Prod. Econ. 211 (2019) 221–236.

[33] J. Yan, X. Li, Y. Shi, S. Sun, H. Wang, The effect of intention analysis-based fraud detection systems in repeated supply chain quality inspection: a context of learning and contract. Inf, Manag. (2020). https://doi,org/10.1016/i,im,2019.103177.

[34] J. Yoon, S. Talluri, H. Yildiz, C. Sheu, The value of blockchain technology implementation in international trades under demand volatility risk. Int. J. Prod Res. 58 (7) (2020) 2163–2183.

[35] J.L. Zhao, S. Fan, J. Yan, Overview of business innovations and research opportunities in blockchain and introduction to the special issue, Financ. Innov. 2 (28) (2016) 2–7.

[36] T. Zhang, G. Li, K.K. Lai, J.W.K. Leung, Information disclosure strategies for the intermediary and competitive sellers. Eur, J. Oper, Res. 271 (2018) 1156–1173

[37] J.C. Zimmer, R.E. Arsal, M. Al-Marzouq, V. Grover, Investigating online information disclosure: effects of information relevance, trust and risk, Inf. Manag. 47 (2010) 115–123.

Yao-Yu Wang received the Ph.D degree from the City University of Hong Kong, and University of Science and Technology of China. He is a professor of Management Science and Engineering at the Soochow University, Suzhou, Jiangsu, China. His research interests include supply chain management, social media, and platform operations. He has pub lished more than 30 papers in Journals such as Information System Journal, Information and Management, European Journal of Operational Research, IEEE Transactions on Engineering Management, Computers& Operations Research, International Journal of Production Research, Journal of the Operational Research Society, Computers & Industrial Engineering, and among others.

Feng Tao received the Ph.D. degree from the City University of Hong Kong, and University of Science and Technology of China. He is an associate professor of Management Science and Engineering with East China University of Science and Technology, Shanghai, China. He has authored more than 10 papers in journals such as European Journal of Operational Research, IEEE Transactions on Engineering Management, Journal of the Operational Research Society, International Journal of Production Research, Computers & Industrial Engineering, Computers and Operations Research, International Transactions in Operational Research, and among others. His research interests include inventory management, operations, and supply chain management.

Jian-Cai Wang received the Ph.D. degree in Management Science and Engineering from Tsinghua University, Beijing, China. He is currently a professor with the School of Man agement and Economics, Beijing Institute of Technology (BIT). Before joining BIT, He worded in the University of Hong Kong, as a Research Assistant Professor. He has authored almost 30 articles in peer-reviewed academic journals, including European Journal of Operational Research, Computers and Industrial Engineering, International Journal of Produc tion Economics, International Journal of Production Research, International Transactions in Operational Research, Journal of the Operational Research Society, and among others. His research interests include empirical and modeling analyses in supply chain management.
