---
otero_id: 5812
otero_key: "XYBE3YEA"
title: "Optimal software pricing in the presence of piracy and word-of-mouth effect"
authors: "Yipeng Liu; Hsing Kenneth Cheng; Qian Candy Tang; Enes Eryarsoy"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.032"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal software pricing in the presence of piracy and word-of-mouth effect

Yipeng Liu <sup>a</sup>, Hsing Kenneth Cheng <sup>b,</sup>⁎, Qian Candy Tang <sup>c</sup>, Enes Eryarsoy <sup>d</sup>

<sup>a</sup> Department of Operations and Information Management, The University of Scranton, Scranton, PA 18510, USA <sup>b</sup> Department of Information Systems and Operations Management, Warrington College of Business Administration, University of Florida, Gainesville, FL 32611-7169, USA <sup>c</sup> Nielsen Online, 770 Broadway, New York, NY 10003-9595, USA

<sup>d</sup> Faculty of Management, Sabancı University, Orhanli, Tuzla, 34956 Istanbul, Turkey

## a r t i c l e i n f o

Article history: Received 28 September 2009 Received in revised form 12 November 2010 Accepted 21 November 2010 Available online 26 November 2010

Keywords: Software pricing Software piracy Word-of-mouth effect Bass diffusion model

## a b s t r a c t

We develop an analytical model that embeds empirical <sup>fi</sup>ndings on software diffusion to examine optimal pricing strategies for a spreadsheet software product under coalescing effects of piracy and word-of-mouth through its entire life cycle. We <sup>fi</sup>nd that the demand of the innovators has the most signi<sup>fi</sup>cant impact on the <sup>fi</sup>rm's pricing decision. Our research recommends market skimming pricing strategy if innovators' demand is high and the market penetration pricing strategy is preferred otherwise. Surprisingly, the increase of conversion rate of imitators to buyers never signi<sup>fi</sup>cantly alters the pricing strategy pre-determined by the demand of innovators. Most interestingly, the optimal pro<sup>fi</sup>t from instituting a two prices policy for a software product with <sup>fi</sup>ve years lifespan outperforms that from a one price policy by no more than 4%, a <sup>fi</sup>nding that corroborates the common one price policy observed in reality.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

The software industry frequently reports that software piracy causes huge losses of revenue to software <sup>fi</sup>rms. According to the fourth BSA and IDC Global Software Piracy Study (Business Software Alliance [3]), 43% of the software installed in 2009 on personal computers worldwide was obtained illegally, amounting to \$51.4 billion in global losses [31]. To battle the software piracy problem, most countries provide legal protection for software by extending copyright, patent contract and trade secret legislation, and by recognizing software as another type of literary and artistic work subject to intellectual property right (IPR) protection. Given that software piracy is a criminal offense, it would seem that the act of making, distributing, or buying pirated software is simply a question of the lack of morality of the pirate vs. the non-pirate [25] or the lack of understanding of the copyright laws [14]. On this basis, the Software and Information Industry Association's (SIIA) push for increased legislation and enforcement would appear appropriate [31]. However, there is evidence to suggest that other factors strongly motivate software piracy [15,16]. Alongside the lack of censure for piracy and the low likelihood of being caught, the most common reason offered for pirating software is the high cost of legal software [8,30]. This calls for a review of the pricing of legal software that is perhaps a more effective measure within the control of software <sup>fi</sup>rms in the <sup>fi</sup>ght against software piracy.

Previous research on software piracy and copyright enforcement can be broadly grouped into three themes. The <sup>fi</sup>rst theme has been how the government should respond to information goods piracy by using its various policy instruments. The <sup>fi</sup>rst instrument of government policy relevant to markets of information goods is a subsidy on purchases of the legitimate item. This has been advocated as an effective way to discourage copying of databases [33] and textbooks [10], but not commonly observed in the software market. The second instrument of government policy is penalty. Producers of information goods have repeatedly pressed the U.S. Congress to expand the scope of criminal sanctions and raise the penalties for copyright infringement. Responding to industry sentiment, the Congress passed the No Electronic Theft Act in 1997 and the Digital Millennium Copyright Act (DMCA) in 1998. Unfortunately, these acts seem to face multiple challenges from the legislation, which largely hinge on the level of scrutiny these acts may apply. The third instrument a government can use to <sup>fi</sup>ght piracy is tax, which already has a long tradition in the recorded music industry where “signi<sup>fi</sup>cant piracy opportunity and activity were observed” with strong evidence suggesting the co-existence of “pre-purchase” sampling piracy and “lost sales” piracy [2]. Johnson [19] discussed the implications of a tax on copying, but did not analyze how a producer would adjust its strategy in response to on-line music sharing. Chen and Png [6,7] found that tax is social welfare superior to penalty but inferior to a subsidy strategy.

The second theme of software piracy research is how the software producer should respond to piracy through preventive controls. Even though preventive controls (increasing the cost of piracy by technological means) can be used to combat software piracy, the study of how deep software producers should engage in selective copyright protection, however, remains ambiguous due to a special characteristic of software, namely, demand-side network externality. From an economic viewpoint, “tolerating some piracy has been shown to have some positive aspects in that piracy makes a product available to those who cannot afford it, increases the consumer base for a product, and creates positive network externalities” [20]. Prasad and Mahajan [28] studied the problem of <sup>fi</sup>nding an optimal level of protection for a software monopoly. Results from their study indicate that a monopoly should start with minimum protection of its software but impose maximum protection and maintain it thereafter halfway from the diffusion process. However, due to exogenous legal and social factors, the optimal level of “protection” varies signi<sup>fi</sup>cantly and becomes hard to maintain as the speed of adoption increases. Gopal and Sanders [14] investigated the effects of preventive and deterrent controls (legal sanctions) on software publishers' pro<sup>fi</sup>ts. Their results suggest that preventive controls do not increase publishers' pro<sup>fi</sup>ts – a <sup>fi</sup>nding echoed by Jaisingh in [18], where he found that a stricter piracy policy, such as increasing the perceived cost to using pirated software for end-users, may unexpectedly lead to an increase in piracy and a decrease in product quality.

Technological preventive efforts are often limited in their ef<sup>fi</sup>cacy [17] since they are only effective until the <sup>fi</sup>rst successful hacker and the protection would only be desirable if the protection implementation cost to software publisher is relatively low and the software is of higher quality among its competitors [22]. On the other hand, “legal deterrence (using legal measures to punish users who pirate) relies on enforcement by the government and consumers' awareness of the law” [5], which is beyond the control of software publishers. This makes many researchers [e.g., 9,10,23,27,34] seek methods of combating software piracy through the most conventional business strategy – pricing (the third stream of the research on software piracy). Speci<sup>fi</sup>cally, how to price software in the presence of piracy is a critical problem for software <sup>fi</sup>rms. A higher than optimal price results in more piracy and revenue loss as “software too expensive” is found as the major reason for consumer piracy [8]. Further, it leads to an undesired consequence of a smaller installed base and slower diffusion of the software product. A lower than optimal price has the bene<sup>fi</sup>t of discouraging piracy at the cost of sacri<sup>fi</sup>cing of pro<sup>fi</sup>t. Using complex adaptive systems approach, Khouja et al. [21] analyze pricing decision for software producers whose products can be easily pirated. Their results predict that improvements in technology, speci<sup>fi</sup>cally data communications and the Internet, will eventually erode the pro<sup>fi</sup>tability of a skimming pricing strategy and make a skimming strategy the least preferable approach for software producers. While the software industry has been engaged in piracy proo<sup>fi</sup>ng, academic literature has largely focused on pricing issues without adequately considering such unique software product characteristics such as the network effect. In addition, shadow diffusion of the software parallel to its legal diffusion in the marketplace has been widely acknowledged but few ef<sup>fi</sup>cient pricing strategies exist in response to its in<sup>fl</sup>uence. The purpose of this paper is to <sup>fi</sup>ll this gap.

We develop an analytical model to examine optimal pricing strategies that embeds the empirical <sup>fi</sup>ndings on software diffusion by Givon, et al. [12], who extended the Bass (1969) diffusion mode to study the diffusion of two types of software (spreadsheets and word processors) in the United Kingdom between 1987 and 1992. Givon, et al. [12] considered two forces that help convert potential software users to buyers − the in<sup>fl</sup>uence by a select group of “innovators” and that of “imitators” through their word-of-mouth interactions. Mahajan, et al. [26] note that there is a distinction between the innovators commonly understood from the temporal order of adoption perspective in the context of Rogers [29] and the innovators from the perspective of communication channels in the diffusion of innovation in Bass (1969) diffusion model [1]. The communication channels by which information about an innovation is transmitted in a social system include mass media and interpersonal communications.

Bass [1] labeled those adopters in<sup>fl</sup>uenced by mass media (external in<sup>fl</sup>uence) as innovators and those in<sup>fl</sup>uence by word-of-mouth effect (internal in<sup>fl</sup>uence) as imitators. As our analytical model is based on the empirical <sup>fi</sup>ndings of Givon, et al. [12] − an extension of Bass [1] diffusion model, the “innovators” in our paper refer to those adopters in<sup>fl</sup>uenced by external sources of communication rather than those according to the time of adoption, and present in all stages of the diffusion of innovation.

Innovators are predominantly in<sup>fl</sup>uenced by external factors such as advertising or promotions; hence, they do not pirate. However, of those software users who adopt because of word-of-mouth in<sup>fl</sup>uence, a fraction (φ) of them will purchase and the remainder $( 1 - \varphi )$ will pirate. Tracking empirical data on software diffusion over time, Givon, et al. [12] derive key estimates for the coef<sup>fi</sup>cients of the innovators and imitators, and the conversion rate of software users into buyers due to the word-of-mouth effect, based on which we develop an analytical model to <sup>fi</sup>nd the optimal pricing strategies in this study. Speci<sup>fi</sup>cally, we incorporate the effect of pricing in our analytical model by explicitly making both the coef<sup>fi</sup>cient corresponding to the in<sup>fl</sup>uence of innovators and the legal conversion rate in Givon, et al.'s model [12] as functions of the software price at each time period such that an optimal price can be found in each period to battle against piracy while having software publisher's pro<sup>fi</sup>t maximized.

We <sup>fi</sup>nd that the demand of the innovators has the most signi<sup>fi</sup>cant impact on the <sup>fi</sup>rm's pricing decision that takes both piracy and wordof-mouth effect into account. Our research recommends market skimming pricing<sup>1</sup> strategy if innovators demand is high and the market penetration pricing strategy is preferred otherwise. Further, the increase of conversion rate of imitators to buyers makes the penetration pricing strategy more attractive. Most interestingly, the optimal pro<sup>fi</sup>t from instituting a two-price policy for a software product with <sup>fi</sup>ve years lifespan outperforms that from a one price policy by no more than 4%, a <sup>fi</sup>nding that corroborates the common one price policy observed in reality.

The rest of this paper is organized as follows. In Section 2, we introduce a general multi-period software pricing model that employs the empirical <sup>fi</sup>ndings from prior literature. We report <sup>fi</sup>ndings from computational analyses of the model and describe associated managerial implications in Section 2.1. Section 3 provides concluding remarks and discussions on future research.

## 2. The model

Consider a <sup>fi</sup>rm selling a software product in a market where there are $N _ { t }$ potential customers in the t-th period where $t { = } 1 , . . . , T ,$ and T represents the lifespan of the software from its initial launch until the <sup>fi</sup>nal replacement by a major upgrade or other products. Since at most one copy of the software application is needed for each computer, the total number of computers is used as a proxy of the maximum market potential $N _ { t } .$ The price to charge in each period is $p _ { t } , t = 1 \ldots T .$ The marginal production cost of the software is assumed to be negligible as is the case for digital products.

It has been established in the marketing literature [1,12,24] that there are generally two groups of consumers in the software industry – the “innovators” and the “imitators.” <sup>2</sup> The “innovators” refer to those adopters of the product in<sup>fl</sup>uenced by external factors such as advertising or promotions, while the “imitators” purchase the software because of word-of-mouth in<sup>fl</sup>uence from those who have already adopted the product. The word-of-mouth in<sup>fl</sup>uence on the diffusion of the software in essence is equivalent to the positive network externality effect in economics [4,11,13]. Over time, positive word-of-mouth can create a bandwagon effect as the network becomes more valuable and more people join in the positive feedback loop.

Let $X _ { t - 1 }$ and $Y _ { t - 1 }$ be the cumulative number of buyers and pirates at the end of period t−1 respectively. Assume that each customer acquires only one software package and there are no repeat purchases. Or, equivalently treat repeat purchases as the demand from customers in different periods. Thus, $N _ { t } { - } X _ { t - 1 } { - } Y _ { t - 1 }$ equals the effective market potential for period t. Let a and b represent the “external in<sup>fl</sup>uence” and “internal in<sup>fl</sup>uence” coef<sup>fi</sup>cients for the innovators and imitators respectively. It is shown in Givon, et al. [12] that the word-of-mouth effects from both buyers and pirates are the same. Hence, a single word-of-mouth internal in<sup>fl</sup>uence coef<sup>fi</sup>cient b is suf<sup>fi</sup>cient. Since the word-of-mouth effect re<sup>fl</sup>ects the adopters' overall experience of the product quality and is insensitive to price, we therefore model the effect of pricing on the diffusion of software through the coef<sup>fi</sup>cient of external in<sup>fl</sup>uence in a linear fashion such that

$$
a (p _ {t}) = c - k \cdot p _ {t}\tag{1}
$$

where c corresponds to maximal coef<sup>fi</sup>cient of external in<sup>fl</sup>uence when the price is zero and k is the price sensitivity parameter of the coef<sup>fi</sup>cient. Thus, the total software adoption due to the external in<sup>fl</sup>uence in the t-th period equals to $a ( p _ { t } ) ( N _ { t } - X _ { t - 1 } - Y _ { t - 1 } )$

The total software adoption due to word-of-mouth effect in the t-th period is described by $\frac { b } { N _ { t } } ( X _ { t - 1 } + Y _ { t - 1 } ) ( N _ { t } - X _ { t - 1 } - Y _ { t - 1 } )$ . This result is derived by multiplying $( N _ { t } - X _ { t - 1 } - Y _ { t - 1 } )$ , the effective market potential at time t, by the in<sup>fl</sup>uence of word-of-mouth effect, which equals the product of cumulative adopters of both buyers and pirates $( X _ { t - 1 } + Y _ { t - 1 } )$ and the coef<sup>fi</sup>cient of internal in<sup>fl</sup>uence b. The division by $N _ { t }$ amounts to normalizing the expression of word-of-mouth effect to make it scale free; see Table 1 for summary of notation.

Assume that out of the software adopters in<sup>fl</sup>uenced by the wordof-mouth effect, a $\varphi ( p _ { t } )$ proportion will buy the software, while the other $1 - \varphi ( p _ { t } )$ proportion will pirate. The φ(p ) corresponds to the legal conversion rate among imitators. Similar to the demand of the innovators, the proportion of buyers is dependent on the price of the software. That is, the proportion of buyers decreases as the price of the software increases. In addition, if the price is zero, there is no need to pirate and all imitators will adopt the software for free. Hence, the following expression captures the proportion of buyers among the imitators due to the word-of-mouth effect.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$N_{t}$  Potential customers (software buyers) in the t-th period (month)
 $p_{t}$  Price to charge in each period
 $X_{t-1}$  Cumulative number of buyers at the end of period t-1
 $Y_{t-1}$  Cumulative number of pirates at the end of period t-1
 $x_{t}$  Number of new software buyers in t-th period
 $y_{t}$  Number of new pirates in t-th period
 $a(p_{t})$  The coefficient of external influence in t-th period when software is sold at price  $p_{t}$ 
b The coefficient of internal influence
c Zero price coefficient of external influence – the proportion of innovators when the price of the software is zero, normalized between 0 and 1
k Price sensitivity parameter of the innovators
e Price sensitivity parameter of imitators
 $\varphi(p_{t})$  Legal conversion rate in t-th period when software is sold at price  $p_{t}$ $p_{prevail}$  The actual price the software was sold during the span of the research
 $p_{max}$  The highest reservation price among innovators in the sense that if the price is set above  $p_{max}$ , no innovator will purchase the software.
 $p_{high}$  The highest reservation price among imitators in the sense that no imitator will purchase the software if the price is set above  $p_{high}$ $\delta$  Discount factor
</div>

$$
\varphi (p _ {t}) = 1 - e \cdot p _ {t}\tag{2}
$$

Therefore, the number of buyers (x ) and pirates $( y _ { t } )$ in the t-th period can be described in Eqs. (3) and (4), respectively. The cumulative number of buyers $\left( X _ { t - 1 } \right)$ and pirates $\left( Y _ { t - 1 } \right)$ at the end of $t - 1$ period are given in Eqs. (5) and (6), respectively.

$$
x _ {t} = \left(a (p _ {t}) + \varphi (p _ {t}) \cdot \frac {b}{N _ {t}} \cdot (X _ {t - 1} + Y _ {t - 1})\right) \cdot (N _ {t} - X _ {t - 1} - Y _ {t - 1})\tag{3}
$$

$$
y _ {t} = (1 - \varphi (p _ {t})) \cdot \frac {b}{N _ {t}} \cdot (X _ {t - 1} + Y _ {t - 1}) \cdot (N _ {t} - X _ {t - 1} - Y _ {t - 1})\tag{4}
$$

$$
X _ {t - 1} = \sum_ {n = 1} ^ {t - 1} x _ {n}\tag{5}
$$

$$
Y _ {t - 1} = \sum_ {n = 1} ^ {t - 1} y _ {n}\tag{6}
$$

Fig. 1 depicts the diffusion dynamics of the software product in the presence of piracy and word-of-mouth effect in our model. <sup>3</sup>

Now we are in a position to present the general software pricing model in the presence of both piracy and word-of-mouth effects as follows.

2.1. The general model: the multi-period multi-price software pricing problem

The following general model captures the multi-period software pricing problem:

$$
\begin{array}{l} \max _ {p _ {t}} \sum_ {t = 1} ^ {T} \frac {p _ {t} x _ {t}}{(1 + \delta) ^ {t - 1}} \\ \text { s.t. } (1), (2), (3), (4), (5), (6), \text { and } \\ 0 \leq a (p _ {t}) \leq 1, \quad 0 \leq \varphi (p _ {t}) \leq 1, \end{array}\tag{7}
$$

$$
x _ {0} = y _ {0} = 0\tag{8}
$$

The software publisher seeks to set the optimal price for each period to maximize the total pro<sup>fi</sup>t throughout the software lifespan by taking into account counteracting effects of piracy and word-ofmouth. Note that the revenue in each period is discounted by a factor $\delta .$ Given price $p _ { t } ,$ the external in<sup>fl</sup>uence coef<sup>fi</sup>cient and the legal conversion rate among imitators in each period are de<sup>fi</sup>ned in Eqs. (1) and (2). In accordance, Eqs. (3) and (4) give the total number of buyers and pirates in period t. The cumulative software adoption due to legal purchase and piracy are calculated in Eqs. (5) and (6). Eq. (7) prescribes that if the price is set too high, there are no innovators and all imitators will pirate. Finally, Eq. (8) gives the initial conditions before the launch of the software.

We note that the above model is analytically intractable to derive any structural insights even for a simpli<sup>fi</sup>ed two-period model with a zero discount rate and a constant market potential for both periods.

![](/api/attachments/XYBE3YEA/fulltext/images/1161efea2418edfbda4b826b6113749e8722208d92301f95ea215343657e442d.jpg)  
Fig. 1. Legal and illegal software diffusion over time.

(The closed-form optimal prices of this simpli<sup>fi</sup>ed two-period model are too complex to be analytically useful.) Further, the word-of-mouth effect from pirates has no impact on the diffusion of the software in the two-period model since there will be no pirates in the <sup>fi</sup>rst period due to the lack of initial copies of available software for them to pirate at the beginning of the <sup>fi</sup>rst period. We thus resort to computational analyses in the next section for further insights into this rather complicated software pricing problem.

## 3. Computational analyses for multiple-period software pricing

Prior literature estimates the average lifespan of a software package to be between 3 and 7 years. For example, Strassmann [32] indicated that for a typical corporation, the average software maintenance costs range from twenty to thirty percent of annual spending on software purchases and concluded that the average software lifespan would be around <sup>fi</sup>ve years. Givon, et al. [12] listed the monthly data of the number of total PCs and excel users in 68 periods. Thus, we analyze pricing strategies of software adoption up to 5 years with one month corresponding to one time period (i.e., t=1, …, 60).

Although software publishers could set an optimal price in each period (e.g., each month), we seldom observe frequent price <sup>fl</sup>uctuations in the software industry. One possibility is that software products, unlike airline tickets, do not have outstanding seasonal demand volatility. Another possible explanation for stable prices is that it's impractical to make frequent changes of price across all distributors if the software is sold through multiple channels. Also, there might be psychological effects among consumers that restrict the software publisher from changing the price without a major upgrade of their products, and so on. Therefore, in the computational analyses, we postulate two mechanisms where a software publisher may adopt price changes: (1) There is only one price change throughout the software lifespan, and the software publisher needs to make optimal decisions regarding the two prices to charge and the timing of price change; and (2) Software publisher implements a fourprice strategy by changing the software price every 12 months after its release up to the end of the fourth year. A reason for this pricing strategy is because the fourth year seems to be the cutoff time for many software products (especially for spreadsheet and word processor software) as quite often they will either be replaced by newer versions or remain as the same quality with no major upgrade or functions added after this point. By comparing the results from the four-price and two-price models with single price model, we can infer whether the <sup>fi</sup>rm should consider more frequent price changes. In sum, the problem is <sup>fi</sup>rst described as a two-price, multi-period pricing problem. It is our objective to <sup>fi</sup>nd optimal prices in each stage $( P _ { 1 }$ and $P _ { 2 } )$ and the best timing to change the price. Then we increase the <sup>fl</sup>exibility to software publisher by implementing a four-price strategy and solve for optimal prices in each stage $( P _ { 1 } , P _ { 2 } , P _ { 3 } ,$ , and $P _ { 4 } )$ More importantly, we would like to answer a fundamental question: should the software publisher adopt a market penetration pricing or a market skimming pricing strategy under a long planning horizon?

## 3.1. Parameter estimation

Bass [1] estimated the external in<sup>fl</sup>uence coef<sup>fi</sup>cient $a ( p )$ and internal in<sup>fl</sup>uence coef<sup>fi</sup>cient b for eleven different consumer durable products. The average for the external in<sup>fl</sup>uence coef<sup>fi</sup>cient is 0.0163 and 0.216 for the internal in<sup>fl</sup>uence coef<sup>fi</sup>cient. Lilen and Rangaswamy [24] studied diffusion parameters for 112 products over 10 product categories for different time intervals. For the external in<sup>fl</sup>uence coef<sup>fi</sup>cient, they estimated the average as 0.037 with a median of 0.025, and for the internal in<sup>fl</sup>uence coef<sup>fi</sup>cient the average is 0.327 with a median of 0.280. Givon, et al. [12] studied the diffusion of word processor and spreadsheet software in the United Kingdom from January 1987 to August 1992, and <sup>fi</sup>nd 0.0002 and 0.00069 as the external in<sup>fl</sup>uence coef<sup>fi</sup>cients for word processor and spreadsheet, respectively. They also estimated from empirical data that the internal in<sup>fl</sup>uence coef<sup>fi</sup>cients b for word processors and spreadsheet software are 0.13518 and 0.10399 respectively. The proportion of buyers due to word-of-mouth effect, the φ in Fig. 1, is estimated to be 0.14378 for word processor and 0.12122 for spreadsheet software.

Comparing the coef<sup>fi</sup>cients from Givon, et al. [12] and Bass [1], we <sup>fi</sup>nd that the external in<sup>fl</sup>uence coef<sup>fi</sup>cient for software products is very small $( { \mathrm { i . e . ~ } } \ a ( p ) = 0 . 0 0 0 2 )$ , but relatively large for durable consumer products $( a ( p ) = 0 . 0 1 6 3 )$ . Further, the magnitude of word-of-mouth effect $\left( b / a ( p ) \right)$ for software products (0.13518/ $0 . 0 0 0 2 = 6 7 5 . 9 )$ far exceeds that of consumer durables (0.216/ $0 . 0 1 6 3 = 1 3 . 2 5 )$ . This implies that the word-of-mouth effect plays an important role in the software pricing decision.

Since the diffusion coef<sup>fi</sup>cients for word processor and spreadsheet do not differ signi<sup>fi</sup>cantly as they belong to the same category of of<sup>fi</sup>ce productivity applications, in the analyses that follow we will speci<sup>fi</sup>cally focus on the spreadsheet software. Hence, we set $b { = } 0 . 1 0 3 9 9$ in our experiments. The imitator's price sensitivity parameter e can also be derived with the knowledge that the spreadsheet software (Excel from Microsoft) was sold at \$230 $( p _ { p r e v a i l } )$ from January 1987 to August 1992. Then, from Eq. (2) we have $e = \frac { 1 - \varphi } { p _ { p r e v a i l } } = 0 . 0 0 3 8 2 .$

In order to <sup>fi</sup>nd a close estimation of k, we de<sup>fi</sup>ne $p _ { \mathrm { m a x } }$ as the highest reservation price among innovators in the sense that if the price is set above $p _ { \mathrm { m a x } } ,$ no innovator will purchase the software. That is, $\begin{array} { r } { , 0 = c - k p _ { \operatorname* { m a x } } . } \end{array}$ Further, from Eq. (1), the proportion of innovators, when the price is set at the prevailing price, is given by: $a ( p _ { p r e v a i l } ) = c - k p _ { p r e v a i l } .$ Solving these two equations simultaneously, one <sup>fi</sup>nds that the parameter k is given by $k = \frac { a ( p _ { p r e v a i l } ) } { p _ { \mathrm { { m a x } } } - p _ { p r e v a i l } } .$ . Simple algebraic inspection indicates that higher reservation price $( p _ { \mathrm { m a x } } )$ leads to lower price sensitivity (k) of innovators, which is consistent with common practice. To <sup>fi</sup>nd a close estimation of $p _ { \mathrm { m a x } } ,$ we de<sup>fi</sup>ne $p _ { h i g h }$ as the reservation price of imitators in the sense that no imitator in<sup>fl</sup>uenced by the word-of-mouth effect will purchase the software if the price is set above $p _ { h i g h } .$ . According to Eq. $( 2 ) , 1 - e \cdot p _ { h i g h } = 0 .$ Conceivably, innovators have a higher reservation price than the imitators. Therefore, we specify the maximum allowed price $p _ { \operatorname* { m a x } } = { m \cdot p _ { h i g h } } .$ For simplicity purpose, we choose $m = 2$ by assuming innovators have a reservation price that is twice as much as that of the imitators. Simple algebra indicates: $k = { \frac { a ( p _ { p r e v a i l } ) } { { \frac { m } { e } } - p _ { p r e v a i l } } } = 0 . 0 0 0 0 0 2 3 5 .$

## 3.2. Pricing strategy for the two-price multi-period case

In this section, we explore the impact of the proportion of buyers due to word-of-mouth effect (φ) and the demand of the innovators (c) on the optimal price and pro<sup>fi</sup>t for a software <sup>fi</sup>rm. An exhaustive search over the solution space is conducted to <sup>fi</sup>nd optimal prices as well as the optimal timing for changing the price. In addition, we compare the result against the benchmark case where the price remains unchanged throughout the entire software lifespan to analyze the impact of the price change on the <sup>fi</sup>rm's pro<sup>fi</sup>tability. To study short-term vs. long term effects on the pricing strategy, we ran analyses with various software lifespans.

Through computational analyses, we seek to address the following questions: (1) Should a software <sup>fi</sup>rm adopt a market skimming pricing or a market penetration pricing strategy; and (2) how much is the pro<sup>fi</sup>tability improved by choosing the two-price model over the <sup>fi</sup>xed price model.

## 3.2.1. The impact of c

The parameter c in essence characterizes the demand of innovators. Even though we can't <sup>fi</sup>nd an empirical estimate of c in the literature, it is quite clear that the zero price demand should be higher than the demand under the prevailing price. Therefore we let c vary between [0.0007, 0.0021] in our experiments, corresponding to one to three times of 0.0069 (the demand of innovators under prevailing price estimated in [12]).

Computational analyses show intriguing and yet intuitive results of how innovator's demand affects the pricing strategy of the software <sup>fi</sup>rm. As shown in Fig. 2, the optimal prices in both stages increase as c increases. Penetration pricing strategy is preferred when the demand of innovators is weak (i.e. cb0.0012) and skimming pricing strategy is favored when the demand of innovators is strong $( \mathrm { i } . \mathrm { e } . \ c { > } 0 . 0 0 1 2 )$ When the demand of innovators falls below the threshold value of 0.0012, it puts a potential threat to the diffusion of the software. Under such situation, it is more pro<sup>fi</sup>table for the software <sup>fi</sup>rm to have a lower <sup>fi</sup>rst stage price (often for a short time) to quickly build up the user base and raise the price in the second stage to take advantage of the word-of-mouth (i.e., positive network externalities) effect. However, when the demand of innovators is relatively strong, it is more pro<sup>fi</sup>table for the software <sup>fi</sup>rm to skim the innovators by setting a higher price in the <sup>fi</sup>rst stage. At a later stage, however, when the software becomes readily available and it is harder to control piracy, the <sup>fi</sup>rm lowers its price with an aim to sell more copies at a cheaper price to the imitators. Finally, when the demand of innovators is growing stronger as re<sup>fl</sup>ected by an increasing value of c, the optimal total pro<sup>fi</sup>t grows accordingly as shown in Fig. 3.

## 3.2.2. The impact of φ

The proportion of buyers due to word-of-mouth effect, φ, represents the proportion of those imitators in<sup>fl</sup>uenced by the wordof-mouth effect who “convert” to buyers. Consequently, $( 1 - \varphi )$ proportion of those imitators choose to pirate the software. From extensive computational analyses, we observe that the change of φ never signi<sup>fi</sup>cantly alters the pricing strategy within the feasible range of parameter values. Instead, the optimal pricing strategy is primarily pre-determined according to the chosen value of c. Figs. 4 and 5 plot the optimal <sup>fi</sup>rst and second stage prices with various φ's under either strong demand $( c = 0 . 0 0 1 4 )$ or weak demand $\left( c = 0 . 0 0 1 \right)$ of innovators. We choose φ in the range of [0.08, 0.16] for the shown experiments as it is consistent with the empirical estimates of the legal conversion rate for spreadsheet software. As φ increases, the <sup>fi</sup>rm realizes more pro<sup>fi</sup>t since more imitators prefer to purchase rather than pirate. At the same time, we observe that the optimal prices in each stage are also increasing in φ. This result is intuitive, as a higher “conversion” rate of imitators implies less price sensitivity, which leads to a higher price set by the <sup>fi</sup>rm. Once again, we <sup>fi</sup>nd the skimming pricing $\left( P _ { 1 } > P _ { 2 } \right)$ is favored when the demand of innovators is strong (i.e. $c = 0 . 0 0 1 4 )$ but the gap between the optimal <sup>fi</sup>rst and second stage prices is shrinking as $\varphi$ increases, suggesting the penetration strategy is making up the ground and possibly become optimal for large enough φ. Similarly, we <sup>fi</sup>nd that penetration pricing $\left( P _ { 1 } < P _ { 2 } \right)$ is preferred when the demand of innovators is weak and the gap between $P _ { 1 }$ and $P _ { 2 }$ enlarges indicating the penetration strategy will remain optimal as $\varphi$ increases. Under both situations, the increase of the legal conversion rate (φ) make penetration strategy more attractive to the software <sup>fi</sup>rm.

![](/api/attachments/XYBE3YEA/fulltext/images/3896a0960b7bc760a575700c2025fe267c0a51a225e63a0ae2995a26f2009b68.jpg)  
Fig. 2. Optimal two prices with various c's (60 periods).

![](/api/attachments/XYBE3YEA/fulltext/images/4d473ffcba0e6458ff59e3c4d16270c2f94a79b8b60eb53aa2e0a9ab8bdce791.jpg)  
Fig. 3. Optimal pro<sup>fi</sup>t with various c's (60 periods).

## 3.2.3. The impact of software lifespan

Figs. 6 and 7 depict optimal prices and pro<sup>fi</sup>ts for various software lifespans. When the planning horizon increases, the software <sup>fi</sup>rm charges a lower price but bringing in a higher pro<sup>fi</sup>t. A possible explanation of this result is that with a longer software lifespan, the network externality effect becomes signi<sup>fi</sup>cant such that it pays off to set a lower price to build up a larger user base and sell to more people who are in<sup>fl</sup>uenced by the word-of-mouth effect. Once again, we <sup>fi</sup>nd that optimal pricing strategy is not affected by the change of the software lifespan (for those software with more than 24 months planning horizon).

## 3.2.4. Pricing strategy: market penetration or market skimming?

Using the coef<sup>fi</sup>cient values derived from past empirical studies, we <sup>fi</sup>nd from all computational analyses that the market skimming pricing is always preferred for software products when the demand of innovators is high. Penetration pricing is favored otherwise. Figs. 2–6 provide examples of prices with respect to different values of c, φ, and software lifespan. This result is rather intuitive as one would expect the <sup>fi</sup>rm to set a lower price when introducing a software product in order to bene<sup>fi</sup>t from positive network externalities under the case of a low demand from the innovators group. In the event of a strong demand from the innovators, the <sup>fi</sup>rm prefers to deliberately slow the diffusion of the software among the imitators group in order to make more pro<sup>fi</sup>ts from the innovators by setting a higher price in the <sup>fi</sup>rst stage.

![](/api/attachments/XYBE3YEA/fulltext/images/16f32188f565e9e0b7a90a8c5bc106d6b70fcf00a4190632e0bff72418341ddb.jpg)  
Fig. 4. Optimal two prices with various φ's (c=0.0014).

![](/api/attachments/XYBE3YEA/fulltext/images/3c047e1c926cd32ae9c2e2cd06c415df0bbb91bd78e7ec2f07c5b8e4b2e5d1d1.jpg)  
Fig. 5. Optimal two prices with various φ's (c = 0.001)

## 3.2.5. Optimal timing of price change

Fig. 8 shows an example of optimal timing of price change with different software lifespans. We observe that when the planning horizon increases, the <sup>fi</sup>rm should hold the optimal <sup>fi</sup>rst stage price for a longer time before switching to a different price in the second stage. In addition, the optimal timing of price change often lies between 15 months and 20 months after the initial release.

![](/api/attachments/XYBE3YEA/fulltext/images/4e21da384aac3435491fb45a3d7b9063eb21cb0f8266a13bb5865833f7422de3.jpg)  
Fig. 6. Optimal two prices with various lifespan (c=0.0014).

![](/api/attachments/XYBE3YEA/fulltext/images/48c78ce35bfa87df06e6a32f463e867a185658c26b77ad4a3ef906046e0c3fcb.jpg)  
Fig. 7. Optimal pro<sup>fi</sup>ts with various lifespan (c=0.0014).

![](/api/attachments/XYBE3YEA/fulltext/images/58e0985436a1f9a296d9dec353460f4790cf38ad5fca0afdb42fba3bb1634875.jpg)  
Fig. 8. Optimal price change time.

## 3.2.6. Two-price vs. one-price benchmark

In the one-price benchmark case, the software <sup>fi</sup>rm <sup>fi</sup>nds the single best price that will result in the highest possible pro<sup>fi</sup>t throughout the software lifespan. We observe from extensive computational experiments that the optimal single price is in between the optimal prices in the two-price model. Fig. 9 shows the optimal single-price and the optimal two prices for the same parameter setup.

It is quite clear that the software <sup>fi</sup>rm will realize less pro<sup>fi</sup>t from implementing one-price than from the two-price policy. Fig. 10 plots the percentage of pro<sup>fi</sup>t gain by adopting the two-price policy vs. the one-price benchmark policy with the same parameter setup. Using the baseline parameters conforming to empirical data, a somewhat striking result from Fig. 10 is that the pro<sup>fi</sup>t difference between twoprice policy and one-price benchmark case is rather insigni<sup>fi</sup>cant as evidenced by the pro<sup>fi</sup>t gain never exceeds 4%. This <sup>fi</sup>nding lends support for the one <sup>fi</sup>xed pricing of software packages commonly adopted in the industry. We also note that, the curly shaped pro<sup>fi</sup>t gain pattern is consistent with the switch of the pricing strategies from penetration to skimming as c increases. The <sup>fi</sup>rst decreasing then increasing pro<sup>fi</sup>t gain curve corresponds to the dying out of the penetration strategy and then the rise of the skimming strategy.

## 3.3. Pricing strategy for the four-price multi-period case

Software publishers are hesitant to employ two-price strategy due to the insigni<sup>fi</sup>cant pro<sup>fi</sup>t gain over the one price policy. Fixed single price strategy, though simple to implement, does not enable the software publishers to either make the most of the pricing tool to battle against piracy or to take advantage of the word-of-mouth interactions among users. Implementing a four-price strategy, however, provides the perfect balance between the two. By changing software price every 12 months after its release up to the end of the fourth year, software publishers are free from the headache of estimating the optimal price changing time, but obtain enough <sup>fl</sup>exibility to raise or lower their product prices to reap the word-ofmouth bene<sup>fi</sup>ts. More importantly, in the subsequent subsections we show that implementing the four-price strategy results in a substantial pro<sup>fi</sup>t improvement over the single price policy from at least 10% to upward of almost 25%.

![](/api/attachments/XYBE3YEA/fulltext/images/50296860ead9cbfa98677296c8a0cc099a313338d2ecd08eb230bce9fbe325a6.jpg)  
Fig. 9. Optimal <sup>fi</sup>xed price (P) and two prices $( P _ { 1 } , P _ { 2 } )$ with various c's.

![](/api/attachments/XYBE3YEA/fulltext/images/dd8fb18e8d6f4712fd5d2fade3bec21a0094aabed00a926eb2cae4ed2fab4961.jpg)  
Fig. 10. Pro<sup>fi</sup>t gain from two-price policy with various c's.

Using the same parameter estimations about spreadsheet software and same data set regarding PC and Excel sales in U.K. reported in Givon, et al. [12], we analyze the impact of different parameters on software publishers' pricing decisions under the four-price strategy.

## 3.3.1. The impact of c

Computational analyses show similar results compared to our <sup>fi</sup>ndings in two-price model about how innovator's demand affects the pricing strategy of the software <sup>fi</sup>rm. As shown in Fig. 11, the maximized pro<sup>fi</sup>t of the software <sup>fi</sup>rm increases when the demand potential of innovators c increases. Penetration strategy is preferred when the demand potential of innovators is low and skimming pricing strategy is desirable otherwise. Due to the multi-price nature, we manage to observe the transition process where the pricing strategy shifts from penetration to skimming, as demonstrated by some intermediate phases where the optimal prices rise <sup>fi</sup>rst $\left( P _ { 1 } { < } P _ { 2 } \right)$ but then decline $\left( P _ { 3 } { > } P _ { 4 } \right)$ as c increases. As the demand potential of innovators c grows stronger, optimal prices $P _ { 1 }$ through $P _ { 4 }$ all increase with the increase of c.

## 3.3.2. The impact of φ

Not surprisingly, we <sup>fi</sup>nd that the choice of optimal pricing strategy remains dominated by the demand of innovators as we vary the legal conversion rate φ from 8% to 16% in the four-price model. The increase of φ increases both optimal prices and pro<sup>fi</sup>ts for the software <sup>fi</sup>rm, but never alters the optimal choice of penetration or skimming pricing strategy.

![](/api/attachments/XYBE3YEA/fulltext/images/35c72b10379c1ce95271fa813fb6fdd73ff6537fe03f5d67f55df7d21ca968f9.jpg)  
Fig. 11. Optimal four prices with various c's (60 periods)

## 3.3.3. Four-price vs. two-price vs. one-price benchmark

Our most important <sup>fi</sup>nding after implementing the four-price strategy comes into light when we compare the pro<sup>fi</sup>t gains between four-price and two-price models while using single price strategy as the benchmark. Unlike what we observed in the two-price model where the pro<sup>fi</sup>t difference between implementing two-price and single price strategy is rather insigni<sup>fi</sup>cant with the maximum improvement less than 4%, four-price strategy shows signi<sup>fi</sup>cant pro<sup>fi</sup>t improvement over the single price benchmark with maximum improvement close to 25%. It is worth noting that the lower the demand of innovators (smaller c), the higher pro<sup>fi</sup>t gain delivered by employing four-price strategy. The same observation holds true for two-price strategy when the demand of innovators is weak (i.e. cb0.0012). One possible explanation to this result could be that the weak demand requires better pricing strategy to exploit the word-ofmouth effect and to extract more pro<sup>fi</sup>ts. However, as the demand of innovators rises, the pricing strategy becomes less important.

## 4. Concluding remarks

In this paper, we examined the pricing policy of a software <sup>fi</sup>rm in a market with both piracy and word-of-mouth (positive network externalities) effects. While prior literature has studied the piracy problem from various perspectives, the implications of both the piracy and network effect on the diffusion of the software and hence the pro<sup>fi</sup>tability of the software <sup>fi</sup>rm in a multi-period setting has not been analyzed. Incorporating the empirical <sup>fi</sup>ndings of [12], we show how a software <sup>fi</sup>rm can develop an optimal pricing policy that maximizes the total pro<sup>fi</sup>t for its software products with various lifespans.

As commonly modeled in the past literature about new product diffusion, we divide consumers into two groups (innovators and imitators) based on their af<sup>fi</sup>nity toward piracy. Our extended diffusion model shows that potential consumers at each time period t are in<sup>fl</sup>uenced by the size of the current installed base (including legal and pirate users), the price and the word-of-mouth effect simultaneously. Ideally, the software <sup>fi</sup>rm foresees the impact and varies the price of its product in each period to battle against piracy while having its pro<sup>fi</sup>t maximized. In reality, however, we do not observe frequent price <sup>fl</sup>uctuations in the software industry. As a result we turn our analyses to the settings where only one price change is permitted and focus on the impact of the change of parameters (e.g., the word-of-mouth, software lifespan etc.) over the <sup>fi</sup>rm's decision whether to adopt market penetration or skimming pricing strategy. Our research recommends that market skimming strategy be adopted if the demand of innovators is high, and penetration strategy is preferred otherwise. We also <sup>fi</sup>nd that the change of other parameters such as the conversion rate from users to buyers and the lifespan of software rarely alter the pricing strategy within the feasible range of parameter values, suggesting that the demand of innovators, especially the zero price demand of innovators plays a more in<sup>fl</sup>uential role.

Our extensive computational analyses provide practical value to the industry practitioners as the setup of the experiments are based on empirical <sup>fi</sup>ndings of extant research. Like all information goods, software products are easy and cheap to copy and distribute. This research addresses the fundamental question of weighing the gain from positive network externality and the <sup>fi</sup>nancial loss due to piracy and provides further guidelines on how the <sup>fi</sup>rm should price their products to take both effects into account.

Our research is not without limitations. First, our analytical model is based on empirical results of a software market reported 15 years ago [12], and a different market characteristic may lead to different managerial implications. In our paper, we used the empirical data in [12] as the baseline values and explored the impact of a wide range of different coef<sup>fi</sup>cients of external in<sup>fl</sup>uence (c) and conversion rates (φ) on the <sup>fi</sup>rm's optimal pricing policy. The insights from the changes of c's and φ's reported in Figs. 2–5 and Figs. 9–14 should provide useful guidelines to managers when they have a <sup>fi</sup>rm grasp of the parameter values in today's market.<sup>4</sup> Second, our model focuses on a monopoly software producer. With the exception of the dominance of Microsoft in the of<sup>fi</sup>ce productivity software and personal computer operating systems, the competition in other parts of the software market is intense. It should be of interest to consider the impact on the pricing strategy in a competitive market. Third, our model studies the optimal pricing policy for a new software product. As time goes by, the <sup>fi</sup>rm may release a major upgrade and offer a lower price to owners of the previous version. How to optimally price the upgrade along would be an interesting extension to our study. Further, we <sup>fi</sup>nd that there is a lack of empirical research on the zero price demand of innovators and how price sensitive they are to software, which should be worthwhile topics for future research.

![](/api/attachments/XYBE3YEA/fulltext/images/6f099c1960e129b617c975986beb222e6b5a2c9412714e5d4045397856223281.jpg)  
Fig. 12. Optimal two prices with various φ's (c=0.001).

![](/api/attachments/XYBE3YEA/fulltext/images/edccaa963652a8b8c7df79e9bb4a5a48df9702c8dcd116d868db48abcfba3a70.jpg)  
Fig. 13. Optimal two prices with various φ's (c=0.0014).

![](/api/attachments/XYBE3YEA/fulltext/images/1a1c3b45a74b0fa893900924791357880dd99e6c35afac248de308604d2de0d6.jpg)  
Fig. 14. Pro<sup>fi</sup>t gain four-price vs. two-price (c=0.0014).

## Acknowledgements

We thank three anonymous reviewers for their very useful comments that help substantially improve the paper. The second author gratefully acknowledges the 2006 summer research grant of Warrington College of Business Administration of University of Florida. This paper is dedicated in memory of Professor Julian Keilson (1924–1999), an American mathematician, who inspired us to work on this topic. Any remaining errors belong to the authors.

## References

[1] F.M. Bass, A new product growth model for consumer durables, Management Science 15 (1969) 215–227.

[2] S. Bhattacharjee, R. Gopal, K. Lertwachara, J.R. Marsden, Whatever happened to payola? An empirical analysis of online music sharing, Decision Support Systems 42 (2006) 104–120.

[3] Business Software Alliance. Global software piracy report 2009, http://portal.bsa. org/globalpiracy2009/studies/globalpiracystudy2009.pdf.

[4] L.M.B. Cabral, D.J. Salant, G.A. Woroch, Monopoly pricing with network externalities, International Journal of Industrial Organization 17 (2) (1999) 199–214.

[5] R.K. Chellapa, S. Shivendu, Managing piracy: pricing and sampling strategies for digital experience goods in vertically segmented markets, Information System Research. 16 (4) (2005) 400–417.

[6] Y. Chen, I.P.L. Png, Software pricing and copyright enforcement: private pro<sup>fi</sup>t vis-à-vis social welfare. Proceedings of the 20th International Conference on Information Systems (ICIS), 1999, pp. 119–123.

[7] Y. Chen, I.P.L. Png, Information goods pricing and copyright enforcement: welfare analysis, Information Systems Research 14 (2003) 107–123.

[8] H.K. Cheng, R.R. Sims, H. Teegen, To purchase or to pirate software: an empirical study, Journal of Management Information Systems 13 (1997) 49–60.

[9] K.R. Conner, R.P. Rumelt, Software piracy: an analysis of protection strategies Management Science 37 (2) (1991) 125–139.

[10] D. de Freitas, The <sup>fi</sup>ght against piracy, International Publishers Association, Paris, France, 1994.

[11] G. Ellison, D. Fudenberg, Word-of-mouth communication and social learning, The Quarterly Journal of Economics 110 (1) (1995) 93–125.

[12] M. Givon, V. Mahajan, E. Muller, Software piracy: estimation of lost sales and the impact on software diffusion, Journal of Marketing 59 (1995) 29–37.

[13] B. Godenberg, B. Libai, E. Muller, Talk of the network: a complex systems look at the underlying process of word-of-mouth, Marketing Letters 12 (1) (2001) 211–223.

[14] R.D. Gopal, G.L. Sanders, Preventive and deterrent controls for software piracy, Journal of Management Information Systems 13 (44) (1997) 29–48.

[16] R.D. Gopal, G.L. Sanders, Global software piracy: you can't get blood out of a turnip, Communications of the ACM 43 (9) (2000) 82–89.

[17] J. Berst, Why technology can't stop music piracy, ZDNET Anchor Desk, 2002, http: //www.zdnet.com/anchordesk/stories/story/0,10738,2677668,00.html

[18] J. Jaisingh, Impact of piracy on innovation at software <sup>fi</sup>rms and implications for piracy policy, Decision Support Systems 46 (2009) 763–773.

[19] W. Johnson, The economics of copying, Journal of Political Economy 93 (1985) 158–173.

[20] M. Khouja, S. Park, Optimal pricing of digital experience goods under piracy Journal of Management Information Systems 24 (3) (Winter 2007) 109–141.

[21] M. Khouja, M. Hadzikadic, H.K. Rajagopalan, L.S. Tsay, Application of complex adaptive systems to pricing of reproducible information goods. Decision Support Systems 44 (2008) 725–739.

[22] S.K. Kwan, J. Jaisingh, K.Y. Tam, Risk of using pirated software and its impact on software protection strategies, Decision Support Systems 25 (2008) 504–516.

[23] Y.M. Li, C.H. Lin, Pricing schemes for digital content with DRM mechanisms, Decision Support Systems 47 (2009) 528–539.

[24] G. Lilen, A. Rangaswamy, Diffusion models: managerial applications and software, ISBM Report 7 (1999)

[25] J.M. Logsdon, J.K. Thompson, R.A. Reid, Software piracy: is it related to level of moral judgment? Journal of Business Ethics 13 (1994) 849–857.

[26] V. Mahajan, E. Muller, R.K. Srivastava, Determination of adopter categories by using innovation diffusion models, Journal of Marketing Research 27 (1990) 37–50.

[27] A.G. Peace, D.F. Galletta, J.Y.L. Thong, Software piracy in the workplace: a model and empirical test, Journal of Management Information Systems 20 (1) (2003) 153–177.

[28] A. Prasad, V. Mahajan, How many pirates should a software <sup>fi</sup>rm tolerate?– an analysis of piracy protection on the diffusion of software, International Journal of Research in Marketing 20 (2003) 337–353.

[29] E.M. Rogers, Diffusion of Innovations, third ed. The Free Press, New York, 1983.

[30] R.R. Sims, H.K. Cheng, H. Teegen, Toward a pro<sup>fi</sup>le of student software piraters, Journal of Business Ethics 15 (1996) 839–849.

[31] Software, Information Industry Association (SIIA), SIIA Report on Global Software Piracy (2009).

[32] A.P. Strassmann, Bogus payback: easy answers create long term problems, Computerworld (1998).

[33] L.D. Tyson, A.E.F. Sherry, Statutory protection for databases: economic and public policy issues, Testimony before the Senate Committee on Judiciary, Oct. 1997.

[34] D.L. Venkatesh, S. Srinivasan, S.C. Kumbhakar, Software piracy: estimation of lost sales and the impact on software diffusion, Journal of Marketing 59 (1995) 29–37.

![](/api/attachments/XYBE3YEA/fulltext/images/cad07add7b9e722a561fe8e1e21865d94243fa16ca679ac16593bc810a50fffe.jpg)  
Dr. Yipeng Liu is an Assistant Professor in the Department of Operations and Information Management at Kania School of Management at the University of Scranton. He received his Ph.D. in information systems from Department of Information Systems and Operations Management at the University of Florida, in 2009. Dr. Liu has published papers in journals such as Information Systems Research, Journal of Management Information Systems, Decision Support Systems, European Journal of Operational Research, Lecture notes in Business Information Processing, and others

![](/api/attachments/XYBE3YEA/fulltext/images/613385c16d9d1e0bd100287a2dfb03c3741f8619f7ab6e7ef85e1a209f9e688f.jpg)

Dr. Hsing Kenneth Cheng received his Ph.D. in computers and information systems from William E. Simon Graduate School of Business Administration, University of Rochester in 1992. He is Associate Professor of Information Systems and Walter J. Matherly Professor at the Department of Information Systems and Operations Management of Warrington College of Business Administration, The University of Florida. Prior to joining UF, he served on the faculty at The College of William and Mary from 1992 to 1998. His research interests focus on modeling the impact of Internet technology on software development and marketing, and the national debate on net neutrality. Dr. Cheng has co-edited several special issues in various information systems journals. He has served on the program committee of many information systems conferences and workshops, and is a program co-chair for the 2003 Workshop on E-Business.

![](/api/attachments/XYBE3YEA/fulltext/images/508922079e6c6fe2dfba766f6f342a951a4e2cc03f33c8664e0d83bdbaecf402.jpg)

Dr. Qian (Candy) Tang received her Ph.D. in Information Systems from Warrington College of Business Administration, University of Florida, in 2004. She has worked as an Assistant Professor in the Department of Information Systems, School of Computing, National University of Singapore. Dr. Tang is a statistician at Nielsen Online. Her current research focuses on online audience measurement, empirical analysis of online traf<sup>fi</sup>c and individual behavior on social network. Her work has appeared in Decision Support Systems, IEEE Transactions on Engineering Management and Journal of Management Information Systems.

![](/api/attachments/XYBE3YEA/fulltext/images/8cb595c7a92d5457084445920499113f5c1802b0034c162a3d31c7be1281cc73.jpg)

Dr. Enes Ervarsoy is an assistant professor in the Faculty of Management at Sabanci University. His research focuses on applications of OR and machine learning/data mining techniques on problems that are important from business point of view. He particularly concentrates on SVMs, information retrieval, association rule mining. His other research areas are pricing of information goods, scheduling, and telecommunications (network design).
