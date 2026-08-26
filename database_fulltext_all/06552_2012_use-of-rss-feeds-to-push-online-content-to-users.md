---
otero_id: 6552
otero_key: "YFFSW82T"
title: "Use of RSS feeds to push online content to users"
authors: "Dan Ma"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.09.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Use of RSS feeds to push online content to users

Dan Ma ⁎

School of Information Systems, Singapore Management University, 80 Stamford Road, Singapore 178902, Singapore

## a r t i c l e i n f o

Article history: Received 29 November 2010 Received in revised form 19 July 2012 Accepted 5 September 2012 Available online 14 September 2012

Keywords: PULL PUSH Really Simple Syndication (RSS) Equilibrium Technology adoption

## a b s t r a c t

Many websites use Really Simple Syndication (RSS) feeds to actively push their online content to users rather than waiting for users to pull the content passively. In this paper, I construct a theoretical game model to study the pro<sup>fi</sup>tability of an RSS-PUSH delivery mechanism. The model assumes a general pro<sup>fi</sup>t structure for websites and heterogeneous users. To access valuable online content, users incur a variety of costs. They choose either to visit the website in the conventional way (the PULL model) or, if it is supported by the website, to use RSS (the PUSH model). Interestingly, I show that although the use of the RSS technology always helps a website to attract more users, it may also reduce the website's pro<sup>fi</sup>t. This happens because newly attracted users are not pro<sup>fi</sup>table enough to offset the website's increase in maintenance costs and decrease in advertising revenue. I also demonstrate that RSS adoption can result in <sup>fi</sup>rst-mover disadvantage instead of advantage. Under certain conditions, the bene<sup>fi</sup>ciary of the new technology adoption is not the <sup>fi</sup>rst adopter, but rather its competitor. Applying my <sup>fi</sup>ndings to the practice, I suggest that certain types of websites should not use RSS feeds to deliver online content. In addition, I show that the key to successful RSS advertising is to strike a balance between consistently valuable content and occasional related advertisements. I also derive the maximum volume of advertisements that can be included in RSS feeds.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The Internet has dramatically changed the quantity and types of information that can be presented and shared, and serves as a platform for information acquisition and distribution to users around the world. The conventional way for users to access online information is through a PULL model, in which users seek information on the Web, either by manual searches or the use of independent agents [16]. Though a variety of PULL technologies exist, they all involve Web searching. To locate useful information, the user bears the costs of searching. In addition, during his search, the user also bears the costs of downloading and viewing advertisements, which—especially when they are large or include graphs, music, or videos—can be time-consuming and effortful to view.

As the Internet grows in size and complexity, steadily more information becomes available online. Users face information overload [21,26], and it is not always easy for them to pull content. As a result, there is an increasing demand for a new type of information access and delivery model. The Really Simple Syndication (RSS) technology has emerged over the past decade to meet the demand. RSS serves as a delivery mechanism for websites to push online content to potential users and as an information aggregator and <sup>fi</sup>lter for users [8,12,29]. To use RSS, a website creates RSS feeds that are attached to its content.1 Meanwhile, users install an RSS reader, which is essentially a software program that is downloadable from the Internet. Users select and add RSS feeds into their RSS reader to create a personalized list of content they are interested in. The RSS reader periodically searches the various feeds, checks for the most recent updates, and delivers text abstracts, summaries, headlines, etc., with a link to the full text. In addition, most RSS readers are now able to block online advertisements effectively. Using RSS, valuable online content is pushed to potential users; there is no need to perform manual searches, and irrelevant content and unwanted advertisements are <sup>fi</sup>ltered out [15].<sup>2</sup>

RSS technology allows website owners to shift from the conventional PULL model to the PUSH model for online content delivery.<sup>3</sup> The key difference between the two models is who initiates the delivery. Under the PULL model, websites are passive; they wait for users to visit them after initiating a search. When competing websites provide similar or identical content and services, and when these competing websites are just one click away, it is dif<sup>fi</sup>cult for a website to distinguish itself from others, attract new users, and retain existing ones. Under the PUSH model. however, websites initiate content delivery by informing potential users of updates [11]. They actively create the user's demand for the information being delivered. Once selected by a user to be listed in his RSS reader, the website builds a long-term relationship with the user, which is an advantage in its competition with other websites.

Both websites and users welcomed RSS. In 2005, about 30% of consumer media websites provided content via RSS feeds [4]. By 2008, this number had increased to 50% [17]. The number of RSS feeds grew from 307,000 in 2004 to 13 million in 2005 [3] and to 16 million in 2007, which includes approximately 75,000 professionally published sources such as the BBC, CNN, and The New York Times $\ [ 7 ] . ^ { 4 }$ Many websites use RSS feeds to offer customized pages for users. For example, Yahoo! has RSS feeds for its customizable My Yahoo! pages, and Google has taken steps to introduce a customizable home page [24]. These major Internet companies are also the providers of RSS readers. In 2007, Google bought RSS publishing and analytics service Feedburner for \$100 million, and the new Google Reader became a dominant product in the RSS reader market [20].

More and more professionals now use RSS feeds in a variety of innovative ways. For example, Google Reader, Newsgator, and Netvibes offer mobile versions of their feed readers [20]. Financial institutions are reaching out to clients using RSS feeds [14], and many Twitter users receive their Tweets via RSS [30]. Interest in RSS increases steadily; in 2007, “RSS” was Google's third most frequently searched “what is” term [20]. The RSS-user adoption rate reached 11% among all Internet users in 2008, which is an impressive increase when compared to the rate of 2% three years ago [17]. As pointed out by analysts, among users who haven't adopted RSS, most don't understand what it is; the rest are not sure whether they use RSS or not. It is commonly believed that there is a large potential market for RSS, but suppliers will <sup>fi</sup>rst need to educate users about its bene<sup>fi</sup>ts.

RSS has attracted the interest of researchers, who have begun to study how RSS can be applied to a variety of <sup>fi</sup>elds. Blekas et al. [2,9], for instance, have investigated the use of RSS feeds for effective mobile web browsing. They propose a new technology that uses RSS feeds to scan websites, remove unwanted information, and eventually present a set of packed versions that achieve better content adaptation for use in mobile phones. Ning et al. [25] present RSS as a framework for enabling ranked semantic searches on the semantic web, Glotzbach et al. [10] provide a novel implementation of RSS as a method of distributing and delivering course information, and Li and Wu [22] discuss RSS use in libraries.

This paper differs from previous work in two ways. First, I focus on the use of RSS on a website as an online content delivery method. Second, I conduct a pro<sup>fi</sup>tability analysis for websites and study the economic, rather than technical, aspects of adopting RSS. In this paper, RSS adoption is considered as a strategy for websites to reach and attract potential users; the major research question is whether adoption of the RSS-PUSH delivery model increases pro<sup>fi</sup>ts for websites.

Researchers have shown that there are no absolutes in terms of drawbacks and bene<sup>fi</sup>ts when adopting a new technology or business strategy. One example is third-party software add-ins. Although add-ins enhance the functionality of the base product, it may also increase or decrease pro<sup>fi</sup>t for the base software producer [6]. Another example is the online customization strategy, which can be used as a price-discrimination tool for sellers to gain higher pro<sup>fi</sup>t. Dewan et al. [5], however, have shown that in a simultaneous adoption game, the two competing <sup>fi</sup>rms face a prisoner's dilemma in which it is not necessarily optimal to adopt the customization strategy in a competitive market. Offering RSS feeds introduces a convenient new visiting channel for users, who can now visit the website through either the conventional or the RSS channel. How do these compete with each other? In the literature, channel cannibalization and product-line cannibalization have been documented in many scenarios [27,28]. In some circumstances, the coexistence of multiple delivery channels or multiple products with different qualities will have strong cannibalization effects and result in lower pro<sup>fi</sup>t for the provider. Will cannibalization also occur between conventional PULL and RSS-PUSH channels? Will RSS technology eventually bene<sup>fi</sup>t or hurt the website? These are the research questions addressed here.

In this paper, I look at the decision a website confronts: to provide RSS feeds for its online content or not. The economic impacts of RSS adoption are investigated; I study changes in number of visitors, market share, total traf<sup>fi</sup>c load, and pro<sup>fi</sup>t for the website. Findings are expected to provide insight for practitioners, such as website designers, online advertisers, and individual Internet users.

My analysis shows that offering RSS feeds will always attract more website traf<sup>fi</sup>c, but it may also reduce the website's pro<sup>fi</sup>t. Therefore, the strategy of actively pushing information to users is not always recommended. More interestingly, I <sup>fi</sup>nd that the so-called “<sup>fi</sup>rst mover” advantage may not exist in the RSS adoption scenario. I derive conditions under which RSS adoption is and is not pro<sup>fi</sup>table. The <sup>fi</sup>nding that the success of RSS adoption actually depends on a website's concrete pro<sup>fi</sup>t structure suggests that the PULL and PUSH delivery models are suitable for different types of website. In other words, I show that RSS isn't automatically advantageous [30].

This work also addresses the recent debate as to whether and how websites should add advertisements to their RSS feeds. Despite its nature of <sup>fi</sup>ltering out online advertisements, RSS has caught great attention and interest from the online advertising community. In addition, because the use of RSS typically will attract more traf<sup>fi</sup>c but may not improve pro<sup>fi</sup>ts, publishers have started to move toward monetizing RSS feeds [13]. Google, Yahoo!, Kanoodle, and RSS advertisement networks like Pheedo were the <sup>fi</sup>rst movers of RSS advertising [23,24]. For example, Google's AdSense for Feeds offers contextually targeted advertisements, while Pheedo displays categorized advertisements in RSS feeds [13].<sup>5</sup> To examine how this emerging trend will affect RSS adoption, I extend my model to include RSS advertising. I show that the key for successful RSS advertising is to <sup>fi</sup>nd a balance between consistently high-quality content and occasional related advertisements. If the volume of advertisements is in balance with the volume of content delivered, advertising in RSS feeds is a valid way to improve a website's pro<sup>fi</sup>t. If, however, balance is not attained, publishers may be forced to move to a subscription RSS feed model.

The paper is organized as follows. Section 2 describes the model. Section 3 analyzes a website's RSS adoption decision and its economic impacts. Section 4 extends the analysis by including RSS advertising in the model. Section 5 summarizes my major <sup>fi</sup>ndings, discusses their business implications, and concludes the paper.

## 2. The model

The website offers valuable online content to users (also called website “visitors”). The pro<sup>fi</sup>t function of the website takes the form of

$$
\pi = A * N _ {D} + p * N - c * \rho ,\tag{1}
$$

where N, $N _ { D } ,$ and $N _ { R }$ are the total number of visitors, the number of direct visitors, and the number of RSS visitors to the site, respectively, and $N = N _ { D } + N _ { R } .$ Direct visitors are users who visit the website in the conventional way, by pulling useful information from the site through searches. RSS visitors use RSS technology. They wait for the information to be pushed to them and access it through the link provided by the RSS reader.

The website's revenue comes from two sources: online advertising (A∗N ) and content $( p \ast N )$ . First, the website gains online advertising revenue. Multiple advertising pricing models exist, such as a <sup>fl</sup>at fee to have an advertisement appear for a certain period of time on the website or a payment only when users of the website click on the advertisements. In this paper, however, it does not matter what the concrete advertising pricing method is. All I assume is that direct visitors, when they are searching and browsing the website, are exposed to a variety of online advertisements; hence they generate advertising revenue for the website. The parameter A denotes the expected advertising revenue from an average direct visitor. However, RSS visitors are not signi<sup>fi</sup>cant contributors to the website's advertising revenue, largely because most current RSS software can effectively block online advertisements. RSS visitors access desired content through the link provided in the RSS feeds, skipping the Web-browsing process. As a result, they are not exposed to various advertisements they would otherwise have seen on Web pages. Although there is debate about the bene<sup>fi</sup>ts of adding advertisements to RSS feeds, it is not yet a common phenomenon. My analysis begins by considering RSS feeds without advertisements. Later, in Section 4, I extend the model to include RSS advertising and examine how it may change the results.

The website also gains content-sales revenue $( p \ast N )$ when visitors consume its online content. Depending on the type of website, content-sales revenue may have different names in practice. For instance, on e-commerce websites, it refers to the business pro<sup>fi</sup>t generated from a visitor's online product purchase or service consumption; on news portals that charge visitors for accessing certain speci<sup>fi</sup>c content, it is termed the “view-by-pay” income. Regardless of the website type, content-sales revenue in this paper measures a visitor's nonadvertising value contribution to the website. The parameter p denotes the expected content-sales revenue from a visitor.<sup>6</sup> In the special case that the website offers completely free content, I simply set $p { = } 0 ;$ thus, the model setting is general to include all possible scenarios.

The last term in Eq. (1) is the website's total maintenance costs, which are calculated as the product of the unit maintenance cost c and the website's effective traf<sup>fi</sup>c load of $\rho .$ The detailed expression of ρ is discussed later.

When the website uses the conventional PULL model for content delivery, it passively waits for website visitors. Users log on, browse, and search through the website. After going through a number of web pages, they eventually locate and consume the desired content, which creates a value b to users. Users are heterogeneous in their Web browsing behavior. Some enjoy browsing websites; others have a strong preference for what they are interested in and do not enjoy reviewing unrelated information. To capture this natural difference in the user population, I assume that a user's value from Web browsing, denoted by x, follows a uniform distribution, x\~U[0,a].

When users access online information using the PULL model, as described above, they are called “direct visitors.” A direct visitor incurs three types of costs: (1) Searching costs S. The visitor pays for efforts to search through a number of web pages to reach his desired content. (2) Traf<sup>fi</sup>c costs wρ. Heavy traf<sup>fi</sup>c to the website could cause problems, such as the slow delivery of web pages, deteriorating content quality, and even delivery failure. A visitor therefore incurs disutility when the website is busy, and such disutility increases in the total traf<sup>fi</sup>c load $\rho .$ (3) Anti-advertising costs $C _ { \mathrm { A } } .$ I assume that users, by nature, dislike online advertisements. Downloading and viewing advertisements are thus costly for them.

Hence, the utility of a direct visitor could be written as $U _ { D } =$ $x + b - p - S - C _ { A } - w \rho .$

When the website adopts RSS technology to push its online content to potential users, users are able to skip the searching process. The RSS reader also helps to block online advertisements. RSS visitors therefore avoid the costs of searching and of viewing unwanted advertisements, but they still bear traf<sup>fi</sup>c costs. The utility function for an RSS visitor is $U _ { R } = b - p - w \rho$ .

List of parameters and variables.

<table><tr><td>S</td><td>The search costs (of a direct visitor)</td></tr><tr><td> $C_A$ </td><td>The anti-advertising costs (of a direct visitor)</td></tr><tr><td>w</td><td>The unit traffic costs for a visitor</td></tr><tr><td>ρ</td><td>The effective traffic load of the website</td></tr><tr><td>b</td><td>A visitor&#x27;s value of consuming his interested online content</td></tr><tr><td>x</td><td>A visitor&#x27;s value of the Web browsing, x~U[0,a]</td></tr><tr><td>p</td><td>The expected content-sales revenue per visitor</td></tr><tr><td>A</td><td>The advertising revenue per (direct) visitor</td></tr><tr><td>c</td><td>The unit maintenance costs of the website</td></tr><tr><td>θ</td><td>The effective traffic load imposed by one RSS visitor, θ≤1</td></tr><tr><td> $x^i$ </td><td>The indifferent visitor in case i</td></tr><tr><td> $N_j^i$ </td><td>The total number of visitors to the website j in case i</td></tr><tr><td> $N_{D,j}^i(N_{R,j}^i)$ </td><td>The number of direct (RSS) visitors to the website j in case i</td></tr><tr><td> $ρ_j^i$ </td><td>The effective traffic load of the website j in case i</td></tr><tr><td>K</td><td>A user&#x27;s cost savings from using the RSS technology, K=C_A+S</td></tr><tr><td>M</td><td>The minimal utility from direct visit, M=b-C_A-p-S-aw&lt;0</td></tr></table>

Direct and RSS visitors impose different levels of traf<sup>fi</sup>c load on the website. Direct visitors search, download, and visit a number of pages. The effective traf<sup>fi</sup>c load imposed by a direct visitor is normalized to be 1. RSS visitors skip the searching process and reach the pages containing their desired content in one click. They are likely, therefore, to impose less traf<sup>fi</sup>c, which is assumed to be θ, θ 1.

Hence, a website's effective traf<sup>fi</sup>c load can be expressed as

$$
\rho = N _ {D} + \theta N _ {R}.\tag{2}
$$

Table 1 lists the parameters and variables used in the paper.

Finally, I make Assumption 1 that $C _ { A } + S + p - a \leq b \leq C _ { A } + S +$ $p + a w$ to avoid trivial cases in the analysis. If the right inequality is violated, the website will always attract all users (a fully covered market). If the left inequality is violated, the website will get no visitors at all (an empty market).

## 3. The analysis

## 3.1. The monopoly website

As my benchmark case, I take the case that a monopoly website does not adopt the RSS-PUSH technology and call $\mathrm { i t } \ ^ { \mathrm { * } } \mathrm { C A S E } \ 0 . ^ { \mathrm { * } }$ Users either visit the website using the traditional PULL method or choose to stay out of the market. Fig. 1 demonstrates the market outcome. Users in the segment $[ x ^ { 0 } , a ]$ will visit the website, users in the segment $[ 0 , x ^ { 0 } ]$ will not visit the website, and the marginal visitor, located at $x ^ { 0 } ,$ gains a value of $x ^ { 0 }$ from Web browsing. The total traf<sup>fi</sup>c load to the website is $\rho ^ { 0 } = a - x ^ { 0 } = N ^ { 0 }$

This marginal user $x ^ { 0 }$ is given by $\begin{array} { r } { x ^ { 0 } + b - p - S - C _ { A } - w ( a - x ^ { 0 } ) = 0 . } \end{array}$ Solving it gives the value of

$$
x ^ {0} = \frac {- b + C _ {A} + p + S + a w}{1 + w}.\tag{3}
$$

The website's pro<sup>fi</sup>t is

$$
\pi^ {0} = \rho^ {0} (A + p - c) = \frac {(a + b - C _ {A} - p - S) (A + p - c)}{1 + w}.\tag{4}
$$

I de<sup>fi</sup>ne two variables, M and K.

$$
M = b - C _ {A} - p - S - a w\tag{5}
$$

$$
K = C _ {A} + S\tag{6}
$$

The variable M is a direct visitor's minimal surplus leftover. It is the utility obtained by the direct visitor who gains zero value from Web browsing and when the website is mostly crowded (i.e., the fully covered market with $\rho { = } a ) .$ <sup>7</sup> The variable K measures a user's total cost savings from using the RSS approach (compared to using the direct visit method).

![](/api/attachments/YFFSW82T/fulltext/images/0463d007c898df8c0e939df2e150756a612bee586ae2ab9632fe77038d1bf664.jpg)  
Fig. 1. A monopoly website without the RSS-PUSH technology.

Eqs. (3) and (4) can be written as

$$
x ^ {0} = \frac {| M |}{1 + w} \text {   and   } \pi^ {0} = \frac {(a + M + a w) (A + p - c)}{1 + w}.\tag{7}
$$

Now consider CASE 1, in which the monopoly website adopts the RSS technology. The website uses both PULL and PUSH methods to deliver its online content to potential users. Users can access their desired content using an RSS program or visit the website directly. Their choices depend on the tradeoffs between cost savings (from avoiding searching and downloading advertisements) and utility losses (from skipping the Web browsing). The <sup>fi</sup>nal market segmentation is shown in Fig. 2. There is a user at $x ^ { D R }$ who gains a value of $x ^ { D R }$ from the Web browsing and is indifferent between the two visiting approaches. Therefore, all users in $[ x ^ { D R } , a ]$ are direct visitors and $N _ { D } ^ { 1 } =$ $\dot { ( } a - x ^ { D R } )$ . Among users in $[ 0 , x ^ { D R } ]$ , some will visit the website using an RSS program, while others will not visit at all.<sup>8</sup> Denote the number of RSS visitors by $N _ { R } ^ { 1 } .$ . The values of $x ^ { D R }$ and $N _ { R } ^ { 1 }$ are determined by the following equations.

$$
b - p - w \rho^ {1} = x ^ {D R} + b - p - S - C _ {A} - w \rho^ {1}\tag{8}
$$

$$
b - p - w \rho^ {1} = 0\tag{9}
$$

$$
\rho^ {1} = \left(a - x ^ {D R}\right) + \theta N _ {R} ^ {1} \leq N ^ {1} = \left(a - x ^ {D R}\right) + N _ {R} ^ {1}\tag{10}
$$

The left-hand side of Eq. (8) is the utility for the user $x ^ { D R }$ when he visits through RSS feeds, and the right-hand side is his utility from the direct website visit. So Eq. (8) states that the user $x ^ { D R }$ gains the same utility from both visiting channels and thus is called the “indifferent user.” Eq. (9) states that in equilibrium, an RSS user gains zero total utility; hence, he is indifferent between visiting through RSS and staying out of the market. The reason is as follows. If there is any positive utility, some users in the segment $[ 0 , x ^ { D R } ]$ , who currently choose to stay out of the market, will use RSS to visit the website. This results in a higher traf<sup>fi</sup>c load on the website and reduces the utility for each web visitor. The number of RSS visitors will keep increasing until there is no more positive utility to gain. It then reaches the <sup>fi</sup>nal market equilibrium. In equilibrium, RSS users gain zero utility and the market size will not increase further. Eq. (10) gives the effective traf<sup>fi</sup>c load of the website $\rho ,$ which is always no larger than the total market size of the website $N ^ { 1 }$

Solving these equations and simplifying, I get

$$
x ^ {D R} = C _ {A} + S = K
$$

$$
N _ {R} ^ {1} = \frac {K}{\theta} + \frac {M + K}{w \theta} \geq 0.\tag{11}
$$

12

Eq. (11) states that users' cost savings from RSS, K, de<sup>fi</sup>nes the indifferent user. When users choose between the two visiting methods, they follow a simple rule. Users whose value from Web browsing is less than the cost savings from RSS will use the RSS-PUSH method, while those whose value from Web browsing is more than the cost savings will stick to the traditional PULL method.

The website's pro<sup>fi</sup>t is

$$
\pi^ {1} = \left(a - x ^ {D R}\right) A + \left[ \left(a - x ^ {D R}\right) + N _ {R} ^ {1} \right] p - \left[ \left(a - x ^ {D R}\right) + \theta N _ {R} ^ {1} \right] c.\tag{13}
$$

Next, I compare the two cases, CASE 1 and CASE 0, to examine the impacts of RSS adoption.

Lemma 1. When $K { \le } \frac { | M | } { 1 { + } w }$ CASE 1 with the RSS-PUSH technology degen-<sup>þ</sup>erates to CASE 0 without the RSS-PUSH technology.

Intuitively, when the total cost savings (K) of RSS decrease, fewer users will visit the website through the RSS channel. When K decreases below the critical value ${ \frac { | M | } { 1 + w } } ,$ there are no RSS visitors at all $( N _ { R } ^ { 1 } = 0$ from Eq. (12)). In such a case, although the website supports the RSS-PUSH model, no user will use it. As a result, the number of visitors, the effective traf<sup>fi</sup>c load, and the pro<sup>fi</sup>t of the website are the same as in the benchmark case. CASE 1 degenerates to the benchmark CASE 0, and the adoption of the RSS-PUSH technology has no impact on the market outcome.

It is more interesting to study the non-degeneration situation. The following inequality gives out the non-degeneration condition.

$$
K > \frac {| M |}{1 + w}.\tag{14}
$$

Only when the cost savings from RSS are large enough, relative to users' minimal surplus leftover |M| as de<sup>fi</sup>ned by Eq. (5), will the adoption of RSS-PUSH technology have an impact on users' Web visiting behavior as well as on the traf<sup>fi</sup>c and pro<sup>fi</sup>t of the website.

Denote the traf<sup>fi</sup>c load change $\Delta \rho = \rho ^ { 1 } - \rho ^ { 0 }$ , which is the effective <sup>¼</sup>traf<sup>fi</sup>c load in CASE 1 minus that in the benchmark CASE 0. Similarly, the change in the number of direct visitors and the change in the number of total visitors of the website are $\Delta N _ { D } = N _ { D } ^ { 1 } - N _ { D } ^ { 0 }$ and $\Delta N =$ $N ^ { 1 } { - } N ^ { 0 }$ respectively. My <sup>fi</sup>ndings are summarized in Proposition 1.

Proposition 1. When the non-degeneration condition (14) is satisfied, namely, $K > \frac { | M | } { 1 + w } ,$

1.1) adoption of RSS-PUSH technology increases the total number of visitors, decreases the number of direct visitors, and increases the effective traffic load of the website. That is, $\Delta N > 0 , \Delta N _ { D } { < } 0 , \Delta \rho > 0 .$ In addition, $i f K { \geq } \frac { \left| { M } \right| } { 1 + w ( 1 - \theta ) } ,$ the market is fully covered.

<sup>þ ð Þ</sup>1.2) adoption of RSS-PUSH technology may increase or decrease the website's profit. There is a threshold value $P ^ { * }$ such that when $p { > } P ^ { * }$ the profit of the website increases, and when $p { < } P ^ { * }$ the profit of the website decreases, where the parameter p denotes the expected content-sales revenue from a visitor. The threshold value

![](/api/attachments/YFFSW82T/fulltext/images/d2c2d1ba22ee1fc05c12c8ebdb7bd07c0fdbf6bd137410a1681fad27ca6ea52c.jpg)  
Fig. 2. A monopoly website with the RSS-PUSH technology.

P\* is the smaller root of the following quadratic function (15) and $P ^ { * } > 0$ always.

$$
\left[ \frac {- M}{1 + w} - K \left(1 - \frac {1}{\theta}\right) + \frac {M + K}{w \theta} \right] * p = \left[ \frac {- M}{1 + w} + \frac {M + K}{w} \right] * c - \left[ \frac {- M}{1 + w} + K \right] * A.\tag{15}
$$

Proof.

1.1)

$$
\begin{array}{l} \Delta N = N ^ {1} - N ^ {0} = \frac {- M}{1 + w} - \left[ K \left(1 - \frac {1}{\theta}\right) + \frac {- M - K}{w \theta} \right] > 0 \Longleftrightarrow K \\ \quad > \frac {| M |}{1 + w}. \\ \Delta N _ {D} = (a - x ^ {D R}) - (a - x ^ {0}) = \frac {- M}{1 + w} - K <   0 \Longleftrightarrow K > \frac {| M |}{1 + w}, \\ \Delta \rho = [ (a - x ^ {D R}) + \theta N _ {R} ^ {R S S} ] - (a - x ^ {0}) = \frac {M + K}{w} + \frac {- M}{1 + w} > 0 \Longleftrightarrow K \\ \quad > \frac {| M |}{1 + w}. \end{array}
$$

1.2) When K $> \frac { \left| M \right| } { 1 + w } ,$ I compare the website's pro<sup>fi</sup>t after and before <sup>þ</sup>RSS is adopted.

$$
\Delta \pi = \pi^ {1} - \pi^ {0} = \Delta N _ {D} * A + \Delta N * p - \Delta \rho * c.
$$

If there is no pro<sup>fi</sup>t change, it must be

$$
\Delta \pi = 0 \Longleftrightarrow p = \frac {\Delta \rho * c - \Delta N _ {D} * A}{\Delta N}.\tag{16}
$$

Plugging in the expressions for $\Delta N , \Delta N _ { D }$ and $\Delta \rho ,$ , I get Eq. (15), which is a quadratic function of p. The coef<sup>fi</sup>cient in front of $p ^ { 2 }$ is $( w \theta - 1 - w )$ which is negative.<sup>9</sup> First, I prove that when $p { = } 0 ,$ , the website's pro<sup>fi</sup>t always decreases, namely, $\Delta \pi ( p = 0 ) { < } 0$ . When the <sup>ð Þ¼</sup>website only earns advertising revenue, providing RSS feeds results in fewer direct visitors, and therefore reduces advertising revenue. In addition, the higher traf<sup>fi</sup>c load brought on by RSS feeds requires higher site-maintenance costs. As a result, the website that provides free speci<sup>fi</sup>c content $( p = 0 )$ is worse off after adding RSS feeds.

Next, I show that $\overline { { P } } = \mathrm { a r g m a x } _ { p } \left\{ \Delta \pi ( p ) \right\} > 0$ . In other words, I solve max Δπ and obtain $\overline { { P } } = \frac { b \dot { - } w ( a - S - C _ { A } ) } { 2 } + \frac { \theta c + w \theta A } { 2 ( 1 + w - w \theta ) } .$ . To see $\overline { { { P } } } > 0 ,$ note that Eq. (9) indicates $b - w \rho ^ { 1 } \geq 0 .$ <sup>Þ</sup>Plugging in Eq. (10), it states $b - w ( a - x ^ { D R } ) - \theta N ^ { 1 } \geq 0$ , where $x ^ { D R } = S + { \overset { \cdot } { C } } _ { A } .$ Then it is equivalent to say that $b - w ( a - S - C _ { A } ) \geq 0$ . As a result, $\overline { { P } } > 0$ follows.

Combining the above three <sup>fi</sup>ndings—that (1) the coef<sup>fi</sup>cient in front of $p ^ { 2 }$ is negative, (2) $\Delta \pi ( p = 0 ) { < } 0 ,$ , and (3) $\overline { { P } } = \mathrm { a r g } \mathrm { m } \mathrm { a x } _ { p }$ $\{ \Delta \pi ( p ) \} > 0 - 1$ conclude that the two roots of Eq. (16) must both be <sup>f gð Þ</sup>positive and the threshold value $P ^ { * } > 0 .$ To see that the smaller root is the threshold value P\*, note that when p increases, |M| increases. Hence, the condition (14) becomes less likely to hold. Degeneration takes place before the larger root of p is reached.<sup>10</sup> □

The <sup>fi</sup>ndings from Proposition 1 are shown graphically in Fig. 3. Fig. 3.1 demonstrates the impacts on the website's traf<sup>fi</sup>c load and Fig. 3.2 shows the impacts on the website's pro<sup>fi</sup>t. In both <sup>fi</sup>gures, the OB line de<sup>fi</sup>nes the non-degeneration condition. In the area below the OB line, degeneration happens. In this area, RSS adoption has no impact on the market at all. In the area above the OB line, when RSS-PUSH technology is able to provide large enough cost savings $( K > \frac { | M | } { 1 + w } )$ , RSS attracts users who otherwise would either pay a <sup>þ</sup>traditional direct visit to the website or opt for staying out of the market. As a result, the total number of visitors increases, the number of direct visitors decreases, and the effective traf<sup>fi</sup>c load to the website increases. This result is consistent with practical observations. It has been reported that providing RSS feeds does attract more visitors to a website. According to a New York Times press release, RSS feeds generated 5.9 million page views for their site in just one month, representing a 342% increase over the previous year [31]. News Yahoo! also reported that adding RSS feeds into My Yahoo! attracted 26 million additional visitors in a single month.

However, RSS adoption is not always pro<sup>fi</sup>t-improving for the website. Fig. 3.2 depicts three different regimes for the pro<sup>fi</sup>t change after the adoption. When degeneration happens (i.e., below the OB line), the website's pro<sup>fi</sup>t remains unchanged (regime c). When degeneration does not happen (i.e., above the OB line), the website's pro<sup>fi</sup>t could increase (regime b) or decrease (regime a), depending on the expected content-sales revenue from a visitor p. The intuition is as follows. The RSS-PUSH approach attracts some users away from the direct visiting channel, creating a “cannibalization” between these two visiting methods. It therefore reduces the number of direct visitors to and advertising revenue for the website. In addition, the effective traf<sup>fi</sup>c load of the website always increases (Fig. 3.1), which leads to higher maintenance costs for the website. On the other hand, the higher traf<sup>fi</sup>c load will also bring higher content-sales revenue. Therefore, the <sup>fi</sup>nal pro<sup>fi</sup>t change will depend on whether the increased content-sales revenue can offset the reduction in the adverting revenue as well as the increase in the maintenance costs. Proposition 1 states the existence of a critical value P\* that divides the area above the OB line into two regimes. In regime b the pro<sup>fi</sup>t shows a positive change after RSS adoption, while in regime a it shows a negative change.

To conclude, RSS-PUSH technology does result in improved pro<sup>fi</sup>ts for the website if and only if (1) users' cost savings from RSS is large enough, and (2) the expected content-sales revenue from visitors is high enough. Condition (1) is the non-degeneration condition, and condition (2) ensures that increases in the content-sales revenue are enough to offset reductions in advertising revenue and increases in maintenance costs.

![](/api/attachments/YFFSW82T/fulltext/images/5a65e022ff05c8f2420806633c17ab769abfc623d696b58b575aadac5ee8188a.jpg)  
Fig. 3. Impacts of RSS-PUSH technology adoption.

A direct corollary from Proposition 1 is given below.

Corollary 1. Websites that gain revenues only from advertisements $( i . e . , p { = } 0 )$ should not adopt RSS-PUSH technology.

When $p { = } 0 ,$ the condition $p { > } P ^ { * }$ is not satis<sup>fi</sup>ed (since $P ^ { * } > 0$ always). Therefore, for websites offering free content, RSS-PUSH technology is not a pro<sup>fi</sup>t-improving tool.

Proposition 1 suggests that there is no absolute yes-or-no answer to the RSS adoption question. Depending on the concrete pro<sup>fi</sup>t structure, website owners should consider RSS adoption carefully. Below I provide some general discussions for different types of websites.

Weblogs usually provide visitors with free content and earn little content-sales revenue. They are likely located in the regime (a). After adding RSS feeds, weblogs will observe a large traf<sup>fi</sup>c load brought on by RSS feeds, which imposes heavy maintenance costs but does not bring signi<sup>fi</sup>cant revenue to the site. As a result, RSS adoption on weblogs will make it dif<sup>fi</sup>cult for owners to monetize their content and maintain their sites. Such a <sup>fi</sup>nding coincides and justi<sup>fi</sup>es the complaints from McLaws, Google's RSS advertising pilot, about his blog site.<sup>11</sup>

For news portals such as CNN.com and NYTimes.com, it may or may not be pro<sup>fi</sup>table to adopt RSS technology, depending on the type of content provided on the site. My results suggest that these websites only provide RSS feeds on content that charges a high enough pay-by-view fee $( p > P ^ { * } )$ . In such cases, more visitors after RSS adoption will bring more content-sales revenue, and therefore makes the adoption a pro<sup>fi</sup>table decision. On the other hand, for free online content or content with a low view-by-pay fee p $( p { < } P ^ { * } )$ RSS adoption is not recommended.

E-commerce websites are likely to lie in regime (b), where RSS-PUSH technology can improve pro<sup>fi</sup>ts. These sites gain revenues mainly from selling commodities or providing services to visitors. For them, the expected content-sales revenue from each visitor is high, and more visitors mean greater pro<sup>fi</sup>ts. The <sup>fi</sup>ndings here suggest that they could be the main bene<sup>fi</sup>ciaries of RSS-PUSH technology. Many e-commerce websites have started to use RSS feeds to update potential buyers on the latest product information. For example, the website SHOP.COM offers one-stop shopping, which allows users to buy their favorite brands and products from hundreds of UK online stores. It summarizes and lists RSS feeds in all shopping categories.<sup>12</sup>

## 3.2. The first-mover advantage

Two competing websites, A and $\mathsf { B } ,$ are in the market. They have the same pro<sup>fi</sup>t structure, as shown in Eq. (1). Here, I investigate whether the <sup>fi</sup>rst-mover advantage exists in the RSS adoption scenario. The research question is: If a website adopts RSS technology earlier than its competitor, will RSS bene<sup>fi</sup>t this website?

I start with the benchmark case, CASE 0, where neither website offers RSS feeds. In equilibrium, they must have the same total traf<sup>fi</sup>c load, $\rho _ { A } ^ { 0 } { = } \rho _ { B } ^ { 0 } . { } ^ { 1 3 }$ Otherwise, users will switch from the website with higher traf<sup>fi</sup>c load to the website with lower traf<sup>fi</sup>c load until equivalence is reached.

As Fig. 4 shows, the marginal (direct) visitor is the user who gains a value of $x ^ { 0 }$ from Web browsing. This visitor gains zero net utility, and $x ^ { 0 }$ is given by

$$
U _ {D} \left(x ^ {0}\right) = x ^ {0} + b - p - S - C _ {A} - w \rho_ {i} ^ {0} = 0, i = A \text {   or   } B.\tag{17}
$$

Eq. (17) indicates that this marginal direct user $x ^ { 0 }$ is indifferent between visiting a website (either A or B) and not visiting any website at all. Users who are in $[ x ^ { 0 } , a ]$ will choose to visit a website, A or B, with equal probability, while users who are in $[ 0 , x ^ { 0 } ]$ will choose to stay out of the market.

The two websites share the market equally. The traf<sup>fi</sup>c load for each is $\rho _ { A } ^ { 0 } { = } \rho _ { B } ^ { 0 } { = } ( a { - } x ^ { 0 } ) / 2 .$ . Plugging this into Eq. (17), I get

$$
x ^ {0} = \frac {- b + C _ {A} + p + S + a w / 2}{1 + w / 2}\tag{18}
$$

$$
\rho_ {i} ^ {0} = N _ {i} ^ {0} = \left(a - x ^ {0}\right) / 2 = \frac {a + b - C _ {A} - p - S}{2 + w}, i = A, B\tag{19}
$$

$$
\pi_ {i} ^ {0} = N _ {i} ^ {0} (A + p - c) = \frac {(a + M + a w) (A + p - c)}{2 + w}, i = A, B.\tag{20}
$$

Eqs. (18)–(20) describe the equilibrium outcome in the benchmark case.

Next, I analyze the marketplace, where one website moves <sup>fi</sup>rst to adopt RSS technology and becomes the <sup>fi</sup>rst mover. This is denoted as CASE 1. I investigate how the number of visitors, effective traf<sup>fi</sup>c load, and pro<sup>fi</sup>t of each website changes, <sup>fi</sup>nd out who is/are the bene<sup>fi</sup>ciary of the RSS-PUSH technology, and examine whether a <sup>fi</sup>rst-mover advantage exists for RSS adoption.

Without the loss of generality, I assume that website A adopts RSS technology and becomes the <sup>fi</sup>rst mover. Users now have two decisions to make, namely, which website to visit and which visiting method (RSS or conventional) to use. Denote the user who is indifferent between the two visiting methods by $x ^ { D R } ,$ . As Fig. 5 shows, users in $[ x ^ { D R > } , a ]$ whose value from Web browsing is larger than $x ^ { D R }$ are direct visitors; they visit a website, A or B, in the traditional way. Let us assume that website A gains r percentage of these direct users and website B gains $1 - r$ percentage of them. It is important to note that direct visitors to both websites are mixed in this segment $[ x ^ { D R } , a ]$ . There is no cutting-off interface between website A's direct visitors and website B's direct visitors. Users in $[ 0 , x ^ { D R } ]$ whose value from Web browsing is smaller than $x ^ { D R }$ will either visit website A through the RSS program or choose to stay out of the market. Therefore, in this segment $[ 0 , x ^ { D R } ]$ , there are $N _ { R } ^ { 1 }$ RSS visitors and $( x ^ { D R } - N _ { R } ^ { 1 } )$ out-of-market users. They are mixed together, and there is no cutting-off interface between them.

![](/api/attachments/YFFSW82T/fulltext/images/5e709543009348d5bff60ec65b2fdd1086ade593a7ae68ea355e5d79cd38d857.jpg)  
Fig. 4. Website competition without the RSS-PUSH technology.

For website B, all visitors are direct visitors. The effective traf<sup>fi</sup>c load of website B is equal to its total number of visitors, $\rho _ { B } ^ { 1 } = N _ { B } ^ { 1 } =$ $( 1 - r ) ( a - x ^ { D R } )$

For website A, there are two types of visitors: direct visitors, $r ( a - x ^ { D R } )$ each imposing one unit of effective traf<sup>fi</sup>c load, and RSS visitors, $N _ { R } ^ { 1 } ,$ , each imposing $\theta \leq 1$ unit of effective traf<sup>fi</sup>c load. Therefore, the total effective traf<sup>fi</sup>c load of website A can be written as $\rho _ { A } ^ { 1 } = r ( a - x ^ { D R } ) + \theta N _ { R } ^ { 1 }$ , which is smaller than the total number of visitors to website A, $\rho _ { A } ^ { 1 } { < } N _ { A } ^ { 1 } { = }$ $\begin{array} { r } { r ( a - x ^ { D R } ) + N _ { R } ^ { 1 } . } \end{array}$

The following equations characterize the equilibrium.

$$
b - p - w \rho_ {A} ^ {1} = x ^ {D R} + b - p - S - C _ {A} - w \rho_ {B} ^ {1}\tag{21}
$$

$$
\rho_ {A} ^ {1} = r \left(a - x ^ {D R}\right) + \theta N _ {R} ^ {1} = (1 - r) \left(a - x ^ {D R}\right) = \rho_ {B} ^ {1}\tag{22}
$$

$$
b - p - w \rho_ {A} ^ {1} = 0\tag{23}
$$

$$
N _ {R} ^ {1} > 0.\tag{24}
$$

Eq. (21) de<sup>fi</sup>nes the indifferent user. Eq. (22) states that the two websites in equilibrium will have the same effective traf<sup>fi</sup>c load (but a different number of visitors).

Solving them gives

$$
x ^ {D R} = C _ {A} + S = K\tag{25}
$$

$$
r = 1 - \frac {b - p}{w (a - K)}\tag{26}
$$

$$
N _ {R} ^ {1} = K \frac {r}{\theta} - \frac {- b + p + a r w}{w \theta}.\tag{27}
$$

In this segment, there are <sup>1</sup> N <sub>R</sub> RSS visitors, who visit website A. The rest ( <sup>1DR</sup> x <sub>−</sub> N ) stay out of the market (do not visit any website).

First, note that the indifferent user in this competition setting (Eq. (25)) is exactly the same as the indifferent user in the monopoly setting (Eq. (11)), and that both are equal to the cost savings from RSS, K. Regardless of the market structure (monopoly or competitive), users follow a simple rule to decide their visiting methods: Users whose value from Web browsing is less than cost savings from RSS will use the RSS-PUSH method, while those whose value from Web browsing is more than the cost savings from RSS will stick to the traditional PULL method.

Second, I <sup>fi</sup>nd that, similar to the monopoly setting, to attract a positive number of users, cost savings from the RSS-PUSH method must be large enough, exceeding a given threshold value. Otherwise, CASE 1 degenerates to the benchmark case, CASE 0. In such a situation, even if website A offers RSS feeds, no users will use it. All visitors will still take the conventional direct visiting method.

The non-degeneration condition is

$$
K > \frac {- b + C _ {A} + p + S + a r w}{1 + r w}.\tag{28}
$$

When cost savings provided by RSS increase (i.e., K increases), the number of RSS visitors $( N _ { R } ^ { 1 } )$ also increases (from Eq. (27)). Such an increase comes from two sources. First, some direct visitors switch from the direct method to the RSS method, i.e., $x ^ { D R }$ moves toward the right. Second, some users who would otherwise stay out of the market now decide to visit the website through using RSS feeds.

In contrast, when cost savings from RSS decrease, the opposite happens. As K decreases, the number of RSS visitors keeps declining until the non-degeneration condition (28) is violated; CASE 1 degenerates to the benchmark CASE 0. For the rest of the analysis, I focus on the non-degeneration scenario only.

Lemma 2. In the competition between a website with RSS feeds (website A) and without RSS feeds (website B), when the nondegeneration condition (28) is satisfied,

1) $N _ { A } ^ { 1 } > \rho _ { A } ^ { 1 } = \rho _ { B } ^ { 1 } = N _ { B } ^ { 1 } = N _ { D , B } ^ { 1 } > N _ { D , A } ^ { 1 } .$

2) $\pi _ { A } ^ { 1 } { > } \pi _ { B } ^ { 1 } ~ i f p { > } P _ { 1 }$ and $\pi _ { A } ^ { 1 } { < } \pi _ { B } ^ { 1 } \ i f p { < } P _ { 1 }$ , where the threshold value $P _ { 1 }$ is the smaller positive root of the equation $p = \frac { ( 1 - \angle r ) ( a - K ) A } { ( 2 r - 1 ) ( a - K ) + r K / \theta + ( b - p ) } .$

Proof. The proof for part (1) is straightforward. The proof for part (2) is as follows. Using Eq. (1), website i's pro<sup>fi</sup>t, $i = A$ or B, could be written as ${ \pi } _ { i } ^ { 1 } = { N } _ { D , i } ^ { 1 } \bar { A } + \bar { N } _ { i } ^ { 1 } p - { \rho } _ { i } ^ { 1 } c ,$ , where $N _ { D , i } ^ { 1 }$ is the number of direct visitors, N<sup>1</sup> is the total number of visitors, and $\rho _ { i } ^ { 1 }$ is the effective traf<sup>fi</sup>c load of website i. Denote the websites' pro<sup>fi</sup>t difference by $\Delta \pi = \pi _ { A } ^ { 1 } - \pi _ { B } ^ { 1 } = \Bigl ( N _ { D , A } ^ { 1 } - N _ { D , B } ^ { 1 } \Bigr ) A + \Bigl ( N _ { A } ^ { 1 } - N _ { B } ^ { 1 } \Bigr ) p .$ . Since $\rho _ { A } ^ { 1 } = \rho _ { B } ^ { 1 }$ , the two websites have the same maintenance costs, which can be canceled out. It is easy to show that website A gains higher content-sales revenue, while B gains higher advertising revenue. There must exist a threshold value of p, denoted by $P _ { 1 }$ , such that (i) it is the solution to the equation $\Delta \pi = 0 ; ( \mathrm { i i } )$ for all $p { > } P _ { 1 } , \Delta \pi > 0 ;$ and (iii) for all $p { < } P _ { 1 } ,$ <sup>¼</sup>Δπb0. As a result, this threshold price $P _ { 1 }$ is the root of the equation $\begin{array} { r } { p = \frac { A \ast \left( N _ { D , B } ^ { 1 } - N _ { D , A } ^ { 1 } \right) } { N _ { A } ^ { 1 } - N _ { R } ^ { 1 } } = \frac { ( 1 - 2 r ) ( a - K ) A } { ( 1 - 2 r ) ( a - K ) + r K / \theta + ( b - p ) } . } \end{array}$ In addition, note that when p increases, the non-degeneration condition (28) becomes less likely to hold. Degeneration happens at $p ^ { d } { = } b { - } w r ( a { - } S { - } C _ { A } )$ . Calculate Δπ at this degeneration point and we get $\Delta \pi ( p ^ { d } ) > 0 .$ . This means that degeneration happens before the larger root of p is reached. Hence, the threshold price $P _ { 1 }$ must be the smaller root. □

![](/api/attachments/YFFSW82T/fulltext/images/b7a82cfa3fb1051f13cca6b17f52bc86d2c2da0cf88e83b520dbc2f4d15fdbbe.jpg)  
Fig. 5. Website competition with RSS-PUSH technology.

In equilibrium, all visitors to website B are direct visitors; website A has both direct and RSS visitors. It is easy to see $r { < } \frac { 1 } { 2 } , { } ^ { 1 4 }$ which means that website B serves the majority of direct visitors. As a result, website A, the <sup>fi</sup>rst mover in RSS adoption, owns a larger market share (namely, more visitors) in the competition.<sup>15</sup> However, it may or may not gain higher pro<sup>fi</sup>t compared to the non-adopter (B). Lemma 2 shows that which website gains the higher pro<sup>fi</sup>t depends on the unit content-sales revenue p. Website $\mathsf { A } ,$ which adopts RSS technology, will earn more pro<sup>fi</sup>ts than website B if and only if the value of p exceeds a given threshold value $P _ { 1 } .$ It is interesting to see that the adopter of a new technology may not perform as well as the non-adopter in an economic sense.

Next, I examine who is the bene<sup>fi</sup>ciary of RSS adoption. When website A is the <sup>fi</sup>rst adopter of the RSS PUSH model, will its pro<sup>fi</sup>ts increase? How will this change the competition outcome and affect the competing website? Lemma 3 compares results from before and after RSS adoption for websites A and B, respectively.

## Lemma 3.

(1) $\rho _ { i } ^ { 0 } < \rho _ { A } ^ { 1 } = \rho _ { B } ^ { 1 } , i = A , B ;$

(2) $N _ { i } ^ { 0 } { < } N _ { B } ^ { 1 } { < } N _ { A } ^ { 1 } , i { = } A , B ;$

(3) $N _ { D , A } ^ { 1 } { < } N _ { D , i } ^ { 0 } { < } N _ { D , B } ^ { 1 } , i { = } A , B .$

Proof.

(1) $\begin{array} { r } { \rho _ { A } ^ { 1 } = \rho _ { B } ^ { 1 } = \frac { b - p } { w } } \end{array}$ and $\rho _ { A } ^ { 1 } - \rho _ { i } ^ { 0 } > 0 , i = A , B$ , when the non-<sup>¼ ¼</sup>degeneration condition (28) holds.

(2) Under the non-degeneration condition $( 2 8 ) , N _ { i } ^ { 0 } { = } \rho _ { i } ^ { 0 } { < } \rho _ { B } ^ { 1 } { = } N _ { B } ^ { 1 }$ In addition, $N _ { A } ^ { 1 } { > } N _ { B } ^ { 1 }$ is from Lemma 2, part 1.

(3) From $x ^ { D R } = K > x ^ { 0 }$ and $r { < } { \frac { 1 } { 2 } } ,$ , it is easy to get $N _ { D , A } ^ { 1 } < N _ { D , i } ^ { 0 } , i = A , B .$ To see $N _ { D , i } ^ { 0 } triangle { < } N _ { D , B } ^ { 1 } , \ i { = } A , B ,$ note that $N _ { D , i } ^ { 0 } { = } N _ { i } ^ { 0 } , \ N _ { D , B } ^ { 1 } { = } N _ { B } ^ { 1 }$ , and $N _ { i } ^ { 0 } { < } N _ { B } ^ { 1 }$ □

Lemma 3 describes changes in the effective traf<sup>fi</sup>c load, total market size, and number of direct visitors for both websites respectively. I <sup>fi</sup>nd that after website A's adoption, the effective traf<sup>fi</sup>c load for both websites increases. Although website B stays passive, more (direct) users will visit it, and as a result its market size expands.

Based on Lemma 3, I am able to study the pro<sup>fi</sup>t changes for both websites. Interestingly, I <sup>fi</sup>nd that the pro<sup>fi</sup>t of the adopter (website A) and its competitor (website B) could increase or decrease under different market conditions. This interesting <sup>fi</sup>nding is investigated further and stated in Proposition 2.

Proposition 2. RSS-PUSH technology increases website A's profit if and only if the expected unit content-sales revenue exceeds a threshold value $P _ { 2 } , i . e . , p > P _ { 2 } .$ Otherwise, website A's profit decreases. Meanwhile, RSS adoption will increase or decrease website B's profit depending on the relative magnitude of market parameters p, A, and c.

Proof. Website A is the RSS adopter. I compare its pro<sup>fi</sup>t before and after the RSS adoption. Let $\Delta \bar { \pi } = \pi _ { A } ^ { 1 } - \pi _ { A } ^ { 0 } , ~ \Delta N _ { A } = \bar { N } _ { A } ^ { 1 } - N _ { A } ^ { 0 } , ~ \Delta N _ { D , A } =$ $N _ { D A } ^ { 1 } { - } N _ { D A } ^ { 0 }$ and $\Delta \rho _ { A } = \rho _ { A } ^ { 1 } - \rho _ { A } ^ { 0 }$ <sup>¼ ¼ ¼</sup>be the changes in pro<sup>fi</sup>t, market size, <sup>¼</sup>number of direct visitors, and effective traf<sup>fi</sup>c load of website $\mathsf { A } ,$ respectively. According to Eq. (1), pro<sup>fi</sup>t change can be written as $\Delta \pi = \Delta N _ { A } * p + \Delta N _ { D , A } * A - \Delta \rho _ { A } * c$ . Lemma 3 shows that $\Delta N _ { A } >$ $0 , \Delta N _ { D A } { < } 0$ , and $\Delta \rho _ { A } > 0 .$ . Set $\Delta \pi = 0 .$ I get $p = \frac { - \Delta N _ { D , A } * A + \Delta \rho _ { A } * \ddot { c } } { \textrm { . a n } } >$ ΔN<sub>A</sub> 0: Therefore, the quadratic function $\Delta \pi ( p = 0 ) { < } 0$ always has positive solutions. Further, note that $\Delta \pi ( p = 0 ) { < } 0$ <sup>Þ¼</sup>and $\Delta \pi ( p ^ { d } ) > 0$ where $p ^ { d }$ <sup>ð Þ¼</sup>is the degeneration point at which the non-degeneration condition (28) is binding. There must be a positive solution $P _ { 2 } \in ( 0 , p ^ { d } )$ s.t. (i) $\Delta \pi ( P _ { 2 } ) = 0 , ~ ( \mathrm { i i } ) ~ \forall p < P _ { 2 } , \Delta \pi ( p ) < 0$ and (iii) $\forall p > P _ { 2 } , \Delta \pi ( p ) > 0 .$ <sup>ð Þ ¼ ð Þ ð Þ</sup>Hence, website A's pro<sup>fi</sup>t will increase (decrease) after the RSS adoption if and only if $p { > } P _ { 2 } ( p { < } P _ { 2 } )$ ).

To see the impact of website $\mathsf { A } ^ { \prime } s$ RSS adoption on its competitor, website B, I write $\Delta \pi = \pi _ { R } ^ { < 1 , 0 > } - \pi _ { R } ^ { < 0 , 0 > } = \Delta N _ { B } * p + \Delta N _ { D , B } * A - \Delta \rho * c$ Lemma 3 states that $\Delta \bar { N _ { B } } > 0 , \bar { \Delta N _ { D , B } } > 0 ,$ <sup>-</sup>and $\Delta \rho _ { B } > 0 .$ <sup>- -</sup>. Thus, Δπ could be positive or negative, depending on the relative magnitude of parameters p, A, and c. That means that website B's pro<sup>fi</sup>t could increase or decrease, with no de<sup>fi</sup>nite sign. □

The main conclusion here is very interesting. It shows that a <sup>fi</sup>rst-mover advantage may not exist for RSS-PUSH technology. There is a threshold value $P _ { 2 }$ such that only when a website's expected unit content-sales revenue exceeds this value, RSS adoption will be capable of bringing in higher pro<sup>fi</sup>t for the <sup>fi</sup>rst mover. More interestingly, I show that RSS adoption may actually decrease the adopter's pro<sup>fi</sup>t while increasing its competitor's pro<sup>fi</sup>t. In such a case, the only bene<sup>fi</sup>ciary is the adopting website's competitor; <sup>fi</sup>rst-mover advantage becomes <sup>fi</sup>rst-mover disadvantage, as stated in Corollary 2.

Corollary 2. When $p { = } 0 ,$ , RSS adoption always decreases the adopting website A's profit but increases its competitor, website B's, profit, i.e., $\pi _ { B } ^ { 1 } { > } \pi _ { i } ^ { 0 } { > } \pi _ { A } ^ { 1 } { \stackrel { \textstyle . } { i } } { = } A , B .$

Proof. Since $p { = } 0 { < } P _ { 2 }$ , using Proposition 2, the inequality $\pi _ { i } ^ { 0 } { > } \pi _ { A } ^ { 1 }$ follows directly. In order to see $\pi _ { B } ^ { 1 } { > } \pi _ { i } ^ { 0 } ,$ I calculate $\bar { \pi _ { i } ^ { 0 > } } - \pi _ { B } ^ { 1 } =$ $( A - c ) \textstyle \left( { \frac { 1 } { 2 } } \left( a - x ^ { 0 } \right) - ( 1 - r ) ( a - K ) \right) , i = A , B .$ . When $p { = } 0 ,$ <sup>¼</sup>, it must be $A - c { \geq } 0 .$ <sup>ð Þð Þ ¼</sup>. Otherwise, website B cannot survive in both cases. In addition, $\scriptstyle \left( { \frac { 1 } { 2 } } \left( a - x ^ { 0 } \right) - ( 1 - r ) ( a - K ) \right) < 0$ must hold under the non-degeneration <sup>ð Þð Þ</sup>condition (28). As a result, $\pi _ { i } ^ { 0 } - \pi _ { B } ^ { 1 } { < } 0$ follows. □

## 4. Extension of the model: adding advertisements to RSS feeds

The analyses so far have assumed that the RSS program is able to block online advertisements effectively. Hence, unlike direct visitors, RSS visitors do not bear anti-advertising costs $C _ { A } .$ Intuitively, such an assumption will tend to (1) increase users' incentive to use RSS feeds (note that $C _ { A }$ is a part of K); and (2) decrease the website's incentive to offer RSS feeds. RSS technology seems like a potential threat to the Internet advertising community. However, advertisers believe that the use of RSS feeds should not mean the end of online advertising; in addition, they are starting to explore the technology potential of RSS advertising [13,19]. NYTimes.com, Google, Yahoo!, Kanoodle, and RSS advertising networks like Pheedo have began inserting targeted text advertisements in their syndication feeds. Most RSS advertisements are just a few lines of text that differ in color from the headlines and summaries delivered by RSS aggregators [24]. RSS users are therefore exposed to a certain amount of simple text advertising. In what follows, I examine how adding advertisements to RSS feeds might affect my results.

When RSS users are exposed to a certain amount of advertisements, they contribute to the advertising revenue by $\delta , \ 0 { \le } \delta { \le } 1$ where $\delta = 0$ is the case that all advertisements are blocked by the RSS program and $\delta = 1$ is the extreme case that RSS cannot block advertisements at all. After having redone all the analyses, I <sup>fi</sup>nd my results robust to this assumption change. The only revision is that the expression of cost savings from RSS should be $K = S + ( 1 - \delta ) C _ { A } .$ All other expressions and equations remain the same, as do lemmas and propositions. Major <sup>fi</sup>ndings and conclusions still hold.

Next, I derive the largest quantity of advertisements that could be added to RSS feeds. Consider the non-degeneration conditions, inequalities (14) and (28) in the monopoly and competition scenario, respectively. After adding advertisements, total savings from RSS decline. The left part of the two conditions becomes smaller, while the right part is unchanged. These inequalities are therefore more likely to be violated, and degeneration is more likely to happen when more advertisements are added to RSS feeds. Studying the binding conditions for these inequalities, I obtain the upper bound of δ, denoted by δ\*. If too many advertisements are added to RSS feeds, exceeding this upper bound $\delta ^ { * } ,$ no visitors will use the RSS channel, and degeneration occurs.

Proposition 3. Advertisements can be added to RSS feeds, but there is an upper limit on the quantity. The maximum amount of advertisements, denoted by $\delta ^ { * } ,$ is given below. If this upper limit is exceeded, no users will use RSS to visit the website.

$$
\delta^ {*} = \left\{ \begin{array}{l l} \frac {b - p + w (S + C _ {A} - a)}{(1 + w) C _ {A}} & \text { monopoly   website } \\ \frac {b - p + w r (S + C _ {A} - a)}{(1 + w r) C _ {A}} & \text { competitive - duopoly   website }. \end{array} \right.
$$

Recall that an average direct visitor reads one unit of online advertisements during his Web browsing and searching process. Proposition 3 states that a website should allow no more than $\frac { b - p + w ( S + \dot { C } _ { A } - a ) } { ( 1 + w ) C _ { A } }$ <sup>ð Þþ</sup>units of advertisements to be inserted in its RSS feeds if it is the monopoly in the market, and no more than $\frac { b - p + w r ( S + C _ { A } - a ) } { ( 1 + w r ) C _ { A } }$ units of adver-<sup>ð Þþ</sup>tisements if it is competing with another website. This upper limit δ\* monotonically increases in b, the value of the online content. Hence, all else equal. with more valuable online content, the website is able to insert more advertisements in its RSS feeds and still not cause degeneration. This upper limit $\delta ^ { * }$ monotonically decreases in p, the price of the online content. Hence, all else equal, for more expensive online content, the website should be careful not to add too many RSS advertisements, since it is easy to cause degeneration. In addition, this upper limit also decreases in $C _ { A } ,$ users' anti-advertising costs. When viewing and downloading online advertisements are more costly on the users' side, RSS advertising has a tighter upper bound. As a result, the website should strictly control the amount of RSS advertisements to avoid degeneration.

## 5. Discussion

RSS software programs serve as both an information aggregator and <sup>fi</sup>lter for Internet users and a new content-delivery mechanism for websites. In this paper, I develop an analytical model to study the economic impacts of RSS-PUSH technology. My model considers two-sided decision-making problems. The website must decide whether to provide RSS feeds so that its online content can be pushed to potential users periodically and actively. If it does, users must decide whether to employ RSS technology to visit a website or just use the traditional PULL method to search and locate their desired content. Although the model in this paper describes only a simple scenario for RSS application, it captures the most salient features of RSS-PUSH technology. It is able, therefore, to provide valuable insight. My major <sup>fi</sup>ndings are summarized and discussed as follows.

First, I show that although RSS technology can always have positive impacts on a website's market size, it can also have a negative effect on its pro<sup>fi</sup>t. I identify situations in which the higher traf<sup>fi</sup>c load brought on by RSS is accompanied by a lower pro<sup>fi</sup>t. This happens when revenue increments from the higher traf<sup>fi</sup>c load are not enough to offset the increase in maintenance costs and decrease in advertising revenue. More interestingly, if a website is competing with another and is the <sup>fi</sup>rst to adopt RSS, the outcome may be that the competitor sees pro<sup>fi</sup>t gains while the <sup>fi</sup>rst mover faces pro<sup>fi</sup>t reductions. I derive the conditions under which this will happen, and suggest that in such cases, the bene<sup>fi</sup>ciary of the new technology adoption is not the <sup>fi</sup>rst adopter, but rather its “inactive” competitor. RSS adoption, therefore, results in <sup>fi</sup>rst-mover disadvantage instead of advantage. This important <sup>fi</sup>nding offers an explanation for recent complaints from some websites that after RSS adoption, they have dif<sup>fi</sup>culty handling heavy traf<sup>fi</sup>c and monetizing their sites. It also serves as a cautionary note for websites that are considering RSS adoption: The RSS-PUSH model is not a cost-free content-delivery mechanism. A careful cost-and-bene<sup>fi</sup>t analysis is needed when making the adoption decision. Certain types of websites—for example, websites that offer free online content or whose revenue is mainly from advertising—should not offer RSS feeds. For them, RSS use, though facilitating information delivery to users, cannot be justi<sup>fi</sup>ed from an economic point of view. In addition, I also try to tackle the recent debate regarding adding advertisements to RSS feeds. I <sup>fi</sup>nd that potential visitors follow a simple rule when considering how to access the online content. They will opt for the RSS technology only if it offers cost savings larger than a given threshold value. Adding advertisements to RSS feeds, obviously, will reduce cost savings and, hence, reduce users' incentive to use RSS feeds. Though it is possible for websites to insert simple text advertisements into their RSS feeds, there is an upper bound on the quantity that can be added. Beyond this limit, the RSS model fails to attract users. The maximum quantity of advertisements is derived in the paper.

The model used here makes assumptions to simplify its analyses. Admittedly, the reality is much more complicated. Here I provide some discussion of model limitations and explore the potential impacts on results if certain assumptions are changed.

First, in the current model, users are heterogeneous only in terms of their Web browsing habits. Different users gain different values (x) from Web browsing, but they all gain the same value (b) from consuming online content. One possible extension is to assume that the value (b) is also heterogeneous among users.<sup>16</sup> Note that the total value for a user from visiting a website comes from both parts, $( x + b )$ . In the current solution, indifferent users are characterized by x only (refer to Figs. 1, 2, 4, and 5). In the new scenario, indifferent users will be determined by both x and b, speci<sup>fi</sup>cally, the sum of these two values. As a consequence, existing Figs. 1, 2, 4, and 5 should be revised. Two-dimensional graphs are needed to show the <sup>fi</sup>nal market segmentation. Indifferent users are those located in a linespace de<sup>fi</sup>ned by the value of $( x + b ) . ^ { 1 7 }$ Other than that, however, all logic, expressions, and math derivations remain the same. For example, the critical value K from Eq. (6), representing cost savings from RSS, remains unchanged. Equations that describe the equilibrium in both markets (Eqs. (8)–(10) and (21)–(23)) remain unchanged. As a result, major conclusions should still hold quantitatively.

Second, in the current model, the two competing websites are homogeneous. The purpose of making such an assumption is to focus analysis on the impacts of RSS adoption. It is interesting, however, to see how two differentiated websites will compete with each other if RSS is used by one of them. Some interesting research questions could be addressed in the heterogeneous duopoly setting, including “Is it true that only the cost-ef<sup>fi</sup>cient website that has lower maintenance costs should adopt RSS?” or “Is it true that only the website that gains more content-sales revenue should offer RSS?” In addition, this paper exclusively examines the existence of <sup>fi</sup>rst-mover advantage in RSS adoption. It would be interesting to investigate whether being a secondary RSS-adopter is a pro<sup>fi</sup>table strategy or not. It is also intriguing to study the adoption equilibrium outcome in a simultaneous setting: Would we see “all websites adopt RSS” as the market equilibrium? If this does happen, are all players, including websites and users, better off with this new technology? The answers are beyond the scope of this article, but merit future research.

Finally, based on my results, I assert that e-commerce websites are likely to be the main bene<sup>fi</sup>ciaries of RSS-PUSH technology.<sup>18</sup> This theoretical predication, however, has no empirical data to support it thus far, for two reasons. First, use of RSS in e-commerce websites is in an early stage. There is not much mature evidence to show the impact of its use yet. Second, websites are especially cautious about publicizing revenue and pro<sup>fi</sup>t information. Hence, at present, this model only could serve as a tool to predict the commercial value of RSS. As time goes by, these results should be supported by more real industrial data.

Business applications for RSS technology are still in a formative stage. RSS technology is a powerful tool that, when correctly used, can rede<sup>fi</sup>ne electronic commerce, revolutionize online content, and enhance Internet communication. Users are just beginning to explore its potential value. As more websites provide RSS feeds and more Internet users use the technology, more advanced RSS-featured business models will be developed. The following are some potential ways of using RSS on e-commerce websites. First, the primary use of RSS is to give potential consumers real-time transmission of online product and price information. This increases their purchase probability and, therefore, creates more business opportunities. Second, the use of RSS offers tremendous potential for mass customization. E-commerce sites could develop dynamic RSS feeds, for instance, that send customized offers to target users. Such RSS applications would bene<sup>fi</sup>t both sides, by allowing online sellers to segment the market and gain higher pro<sup>fi</sup>ts, and online buyers to <sup>fi</sup>nd desired products more easily.

## References

[1] S. Aughton, Google Turns to RSS News Feeds for Placing Ads, PC PRO, April 2005

[2] A. Blekas, J. Garofalakis, V. Stefanis, Use of RSS feeds for content adaptation in mobile web browsing, in: International Cross-Disciplinary Workshop on Web Accessibility, 2006, pp. 79–85.

[3] BusinessWeekOnline, RSS keeps booming. article available at http://www. businessweek.com/technology/tech\_stats/rss050923.htm, 2006.

[4] W. Davis, Two of three online mags have web-only advertisers, Online Media Daily, June 2005. article available at http://publications.mediapost.com/index cfm?fuseaction=Articles.san&s=31662&Nid=14155&p=276816.

[6] R. Dewan, M. Freimer, Consumers prefer bundled add-ins, Journal of Management Information Systems 20 (3) (Winter 2003–04).

[5] R. Dewan, B. Jing, A. Seidmann, Product customization and price competition on the internet, Management Science 49 (8) (August 2003) 1055–1070.

[7] Feedster.com statistics. article available at 2007.

[8] J. Foley, The weblog question, Information Week, 2005.

[9] J. Garofalakis, V. Stefanis, Using RSS feeds for effective mobile web browsing, Universal Access in the Information Society 6 (3) (2007) 249–257.

[10] R.J. Glotzbach, J.L. Mohler, J.E. Radwan, RSS as a Course Information Delivery Method, 2008.

[11] K. Guenther, The Web gets pushy, CIO Enterprise Section, 12(7), 1999

[12] B. Hammersley, Content Syndication with RSS, 1st edition O'Reilly Media, April 2003.

[13] S. Housley, Advertising in RSS feeds. article available at http://www.feedforall. com/advertising-in-rss.htm, retrieved on Oct 2011.

[14] S. Housley, Financial companies use RSS feeds. article available at http://www. feedforall.com/<sup>fi</sup>nance-companies-use-rss.htm, retrieved on Oct 2011.

[15] R. Hrastnik, Unleash the Marketing & Publishing Power of RSS, 2005

[16] T. Kapyla, I. Niemi, A. Lehtola, Towards an Accessible Web by Applying PUSH Technology, 2000.

[17] J.M. Katz, Forrester Research Report on the State of RSS, Oct 2008.

[18] J. Kendall, K. Kendall, Information delivery systems: an exploration of web PULL and PUSH technologies, Communications of the AIS 1 (1999).

[19] D. Kesmodel, E-commerce; really simple sale? As RSS feeds catch on, advertisers are taking notice, Wall Street Journal (Oct 2005).

[20] M. Kirkpatrick, The year in RSS. article available at http://www.readwriteweb. com/archives/2007\_the\_year\_in\_rss.php, December 2007.

[21] B.-K. Lee, W.-N. Lee, The effect of information overload on consumer choice quality in an on-line environment, Psychology and Marketing 21 (3) (March 2004) 159–183.

[22] J. Li, W.G. Wu, RSS made easy: a basic guide for librarians, Medical Reference Services Quarterly 26 (1) (Spring 2007).

[23] D. Morgan, RSS advertising, coming fast. article available at http://www.clickz. com/clickz/column/1697607/rss-advertising-coming-fast, April 2005.

[24] B. Morrissey, RSS feeds becoming hot real estate for online ads, Adweek report, June 2005.

[25] X. Ning, h. Jin, H. Wu, RSS: a framework enabling ranked search on the semantic web, Information Processing and Management 44 (2) (March 2008) 893–909.

[26] J. Quentin, R. Gilad, R. Sheizaf, Information overload and the message dynamics of online interaction spaces: a theoretical model and empirical exploration, Information System Research 15 (2) (June 2004).

[27] C.S. Ruebeck, Inter<sup>fi</sup>rm competition versus intra<sup>fi</sup>rm cannibalization in the computer hard disk drive industry, Review of Industrial Organization 26 (1) (February 2005).

[28] A. Shaked, J. Sutton, Multiproduct <sup>fi</sup>rms and market structure, RAND Journal of Economics 21 (1990) 45–62

[29] M.P. Saucers, Blogging and RSS, Second edition Information Today, Inc., October 2010.

[30] R. Scoble, article available at http://www.quora.com/Why-havent-RSS-readersgained-mass-adoption, 2011.

[31] The New York Times Company, NYTimes.com's record-breaking traf<sup>fi</sup>c for March, The New York Times Company News Release, April 2006.

Dan Ma received her Ph.D. from the Carol G. Simon School of Business at University of Rochester. She is now the assistant professor of the School of Information Systems (SIS) at Singapore Management University. She specializes in Information System and Management.

Dr. Ma is interested in the economics of IT. Her works include, but are not limited to the following research areas: the use of game theoretical model to study the dynamics of competition between software providers, pricing issues for the share IT services, and the diffusion and impact of new IT technology adoption. She has published in journals (JMIS and ITM) and several major conferences (ICIS, HICSS, CIST, WISE, AMCIS, etc.). Meanwhile, the research work of Dr. Ma has been applied to practical cases. She uses her analytical model and <sup>fi</sup>ndings to help IDA (SINGAPORE) to conduct cost and bene<sup>fi</sup>t analysis for their potential grid service users.
