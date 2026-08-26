---
otero_id: 3124
otero_key: "QFAU6GTE"
title: "Push or Pull? A Website’s Strategic Choice of Content Delivery Mechanism"
authors: "Dan Ma"
year: "2015"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2015.1029400"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [University of Nebraska, Lincoln] On: 08 September 2015, At: 20:26 Publisher: Routledge Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: 5 Howick Place, London, SW1P 1WG

![](/api/attachments/QFAU6GTE/fulltext/images/83d71b34e59ed43d7d6366f8357b38df8ee287eeb06f6ed5db6527bd13eab622.jpg)

# Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# Push or Pull? A Website’s Strategic Choice of Content Delivery Mechanism

Dan Ma Published online: 06 Jul 2015.

![](/api/attachments/QFAU6GTE/fulltext/images/381ef56c141956e0ce9128a9216a6c6e06e28038998b7d5fb23301301818d664.jpg)

Click for updates

To cite this article: Dan Ma (2015) Push or Pull? A Website’s Strategic Choice of Content Delivery Mechanism, Journal of Management Information Systems, 32:1, 291-321, DOI: 10.1080/07421222.2015.1029400

To link to this article: http://dx.doi.org/10.1080/07421222.2015.1029400

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms &

Conditions of access and use can be found at http://www.tandfonline.com/page/termsand-conditions

# Push or Pull? A Website’s Strategic Choice of Content Delivery Mechanism

DAN MA

DAN MA is an assistant professor of information systems and management at the School of Information Systems, Singapore Management University. She received her Ph.D. from the Carol G. Simon School of Business at the University of Rochester. She specializes in the economics of information technology (IT). Her research interests include the use of game-theoretical models to study the dynamics of competition between software providers, pricing issues for the share of IT services, and the diffusion and impact of new IT technology adoption.

ABSTRACT: Really simple syndication (RSS) technology enables an alternative delivery mechanism for online content. Instead of waiting passively for users to pull online content out, websites can push it to potential users through RSS. This is expected to significantly affect user behavior, website profitability, and market equilibrium. This research uses an economic model to study the impact of RSS adoption and examine whether it increases a website’s profit and competitive advantage. The findings are intriguing: they demonstrate that RSS can either increase or decrease website profit. In a competitive context, RSS adoption can actually be a disadvantage; in some cases, it hurts the adopter but benefits the competitor. Moreover, under certain conditions, the first mover will be worse off when the competitor mimics its adoption decision, which discourages the earlier adoption and thus creates an obstacle to using RSS. Derivation of the adoption equilibria in sequential and simultaneous games shows that multiple market outcomes may result. Finally, regardless of whether or not a website operator adopts RSS, it will still benefit by increasing user awareness of RSS technology, but only up to a certain level. Once this critical awareness level has been reached, websites will not gain by continuing to promote RSS to users. As a whole, these results show how technology adoption will have an impact on firm performance and market outcome, and illustrate the complexity of technology adoption strategy in a competitive setting.

KEY WORDS AND PHRASES: competition, e-commerce, game theory, information economics, online content delivery, RSS.

The Internet is a major platform for information acquisition and distribution to users across the world. As online content grows in amount, size, and complexity, users face information overload [23, 31]. It becomes increasingly difficult to locate and access desired information through the conventional pull method, in which users locate information by performing a search. Web searches are costly [42], taking time and effort, which can range from personally surfing the Internet to using independent agents. Also, during the search process, users bear the additional costs of downloading and viewing online advertisements. Web advertisements—especially large ads with text, graphics, music, or videos—require greater effort to view. Under the conventional pull method, websites are passive. They wait for users to find and visit them by searching, and then initiate the consumption of online content. It is difficult for a website to distinguish itself from competitors who provide the same content and services and adopt similar selling strategies. The conventional pull method, therefore, is inefficient for web content delivery and unsatisfactory on both the supply or website and demand or user sides.

Many websites have started to use the push method, enabled by really simple syndication (RSS) technology, to deliver content. As its name suggests, RSS is easy to use. Websites attach RSS feeds to their online content, and users install on their computers an RSS reader, a downloadable software program.<sup>1</sup> The RSS reader periodically searches RSS feeds, checks for updates, and sends text abstracts, summaries, headlines, and so forth, as well as a link to the user to the full text [10, 19]. The user is kept up to date on content of interest, and can access the full information without performing a search. Most RSS readers can block online ads effectively, so that content of no interest and unwanted ads are filtered out [18].

RSS has spurred a move from the conventional pull method to the push method for online content delivery.<sup>2</sup> The key difference between the two is who initiates delivery [19]. The pull method waits passively for users to access a website and its content; while the push method allows a website to actively create user demand for new information by periodically informing users of its availability [15]. I investigate how the push method affects user online behavior, influences website traffic and profitability, and changes the equilibrium in the marketplace. Using my findings, I provide practical RSS adoption strategies.

Various types of websites have adopted RSS to reach potential Internet users. News portals have embraced the use of RSS. They allow users to access the latest updates of their favorite content—from economics, politics, and science, to sports and entertainment—without a lengthy search [10, 35]. Most consumer media websites have been providing content via RSS feeds, including established outlets such as the BBC, CNN, and the New York Times [9].<sup>3</sup> E-commerce websites have also started using RSS to inform potential consumers of new arrivals and sales. For example, Orbitz launched its RSS collection in 2006. Its feeds update users about new bargains on flights, hotels, and rental cars. eBay, which has long enabled users to save their search terms and opt into daily e-mail summaries of new listings, recently redesigned its U.S. home page to include users’ saved searches in personalized feeds that update in real time [2]. In addition, RSS has been used in many innovative ways. Yahoo! for instance, uses My Yahoo Pages RSS feeds to enable users to create customized webpages, NewsGator and Netvibes offer mobile versions of their feed readers [22], financial institutions are reaching out to clients using RSS feeds [17], and many Twitter accounts receive tweets via RSS [36].

Although some industry data have demonstrated that providing an RSS feed attracts more visitors to a website,<sup>4</sup> other reports have found that too much RSS traffic can trigger problems instead of profits for the website. For example, Robert McLaws, whose Longhorn Blogs was the first to test RSS ads for Google, said that 98 percent of the traffic on his site came from RSS feeds. He complained that RSS feeds are a “bandwidth killer,” and asserted that he was not able to monetize the website or cover server costs [26]. If this is commonly the case, does RSS add value to a website? Is RSS adoption always a good strategy?

Google closed Google Reader, an RSS feed aggregator launched in 2005, in July 2013, based on declining use [3]. Analysis of Forrester Technographics data confirms Google’s claim: between 2008 and 2012, the monthly percentage of U.S. online RSS users remained level at 10–11 percent [33].<sup>5</sup> Although RSS has been welcomed and supported by most websites, it does not seem as attractive to Internet users. What causes this imbalance? Some analysts have found that most users who have not adopted RSS do not understand what it is, and the rest are not aware whether or not they use RSS. They believe that there is a large potential market for RSS to fill – but do websites have any incentive to educate users?

To address these questions, I propose a game-theoretical model to investigate the following aspects of RSS adoption by websites and users. I ask: Who actually benefits from RSS use? Will RSS feeds bring more traffic and higher profit to a website in a competitive marketplace? Does a first-adopter advantage exist for websites? What are the equilibria in both sequential and simultaneous adoption games, and what key factors determine the equilibrium outcome? What are the recommended adoption strategies for a website when competing with another website that has or has not used RSS? How will users’ RSS-awareness rate affect websites? Do websites have an incentive to invest in boosting users’ RSS-awareness?

Almost all research about RSS so far have focused on those technical issues. For example, Blekas, Garofalakis, and Stefanis [2] and Garofalakis and Stefanis [11] examine the use of RSS feeds for effective mobile web browsing. Ning, Jin, and Wu [29] present RSS as a framework that enables ranked searches on the semantic web. Glotzbach, Mohler, and Radwan [13] describe RSS as a creative method of distributing and delivering course information. And Li and Wu [24] discuss RSS use in libraries. Ma [27] is the only exception that studied RSS adoption as a business strategy but it was mainly from one firm's perspective without considering competition equilibrium. In contrast to previous work, I examine RSS from an economic perspective and view RSS adoption as a competitive strategy for reaching potential online users and increasing a website’s competitive capability.

Technology adoption will typically have an impact on firm strategy [14, 39]. Will benefits outweigh costs, in a competitive setting, when a new technology and related business strategy are employed? Previous work has shown that there are no absolutes. One example is third-party software add-ins: Although add-ins enhance the base product’s functionality, they may also decrease the base software producer’s profit [7]. Another example is the online customization strategy, which could be used as a price-discrimination tool for sellers to gain higher profit. Yet Dewan, Jing, and Seidmann [6] show that in a duopoly adoption game, firms face the two competing firms face a prisoner’s dilemma. In a competitive market, it is not always optimal to adopt a customization strategy. To answer for RSS, I investigate RSS adoption strategy.

Offering RSS feeds introduces an alternative channel for web visits—but how does it compete with the conventional pull method of visiting a website? Channel competition [1, 12, 32] and product-line cannibalization have been documented in many scenarios. In some, coexistence of multiple delivery channels or multiple quality-differentiated products has a cannibalization effect [34, 37], leading to lower profits for the provider. Does cannibalization also arise between pull and push methods? I investigate this too.

My findings are interesting. They show that in competition RSS adoption will always bring more traffic to a website, but not necessarily higher profit, suggesting the existence of the cannibalization effect. Further, in certain circumstances, RSS adoption hurts the adopter but benefits the competitor. And in a sequential adoption setting, a website may find it not optimal to be the first adopter—when its competitor follows and adopts RSS at a later time, the first adopter gets hurt—and thus the website should choose not to adopt as a way to protect itself in the competition. These findings illustrate the complexity of RSS adoption strategy in a competitive context. I also derive adoption equilibria in both sequential and simultaneous games, and show that multiple market outcomes can result, depending on the expected revenue contribution from each RSS visitor. So I am able to discuss and suggest different adoption strategies.

I find that all websites, regardless of whether they adopt RSS, will have an incentive to educate users about RSS. This incentive diminishes once users’ RSSawareness level reaches a certain threshold though. My numerical analysis shows that a small percentage of RSS-aware users may be enough to support the market equilibrium; this could explain why users’ RSS adoption rate does not steadily increase. Finally, I relax my model assumptions to incorporate ongoing RSS practices such as RSS advertising.

## The Model

Table 1 lists the parameters and variables used in the model and their definitions.

The market consists of many users who are potential web visitors. Among the whole user population, β percentage of them are aware of RSS, and may use it if RSS feeds are provided. The rest, 1 – β percentage of users, have no knowledge of RSS. β measures users’ RSS-awareness level, and β < 1.

A user wants to access specific online content that is of value b. Under the pull model, the user must log on, browse, and search through multiple web pages until he locates the targeted content and consumes it to get the value b. The website remains “silent” in this process; it passively waits for the user to pull information out of it. In my model, users who use the pull model to access online information are conventional visitors. When they browse, they have access to a large amount of information. Users have different attitudes: some enjoy surfing and obtain high value from $\mathrm { i t , }$ whereas others know what they are interested $\mathrm { i n } . ^ { 6 }$ Meanwhile, web browsing also delivers online ads to users, which take time and effort to download and view. Dewan, Freimer, and Zhang [8] suggest that Internet users are always against ads, and that some may dislike ads more than others do. To capture these user differences, I assume that users’ net value from web browsing, including their gains from obtaining additional online information and their costs from viewing online ads, is heterogeneous, as denoted by x and follows a uniform distribution: $x \sim U [ 0 , a ]$ . In addition, conventional visitors incur search cost S to search for and locate targeted content. They also incur disutility when the website is busy. Heavy traffic may cause problems such as slow delivery of web pages, deteriorated content quality, or delivery failure. These constitute users’ traffic costs wρ, where $\rho$ is the total traffic load of the website and w is a constant. Finally, conventional visitors are assumed to pay $p _ { C }$ to consume online content of interest. Their utility function can be written as $\begin{array} { r } { U _ { C } = x + b - S - w \ p - p _ { C } . } \end{array}$

Table 1. Modeling Notation and Definitions

<table><tr><td>Notation</td><td>Definitions</td></tr><tr><td> $\beta$ </td><td>Percentage of users who are aware of RSS technology</td></tr><tr><td> $b$ </td><td>Value of targeted online content</td></tr><tr><td> $x$ </td><td>A conventional visitor&#x27;s net value from web browsing;  $x \sim U [0, a]$ </td></tr><tr><td> $S$ </td><td>A conventional visitor&#x27;s search costs</td></tr><tr><td> $p_{C}, p_{R}$ </td><td>A conventional (and RSS) visitor&#x27;s expected content-sales revenue contribution</td></tr><tr><td> $\rho$ </td><td>Effective traffic load of the website</td></tr><tr><td> $w$ </td><td>A visitor&#x27;s unit traffic cost</td></tr><tr><td> $A$ </td><td>A conventional visitor&#x27;s expected advertising revenue contribution</td></tr><tr><td> $c$ </td><td>Website&#x27;s unit maintenance cost</td></tr><tr><td> $\theta$ </td><td>Effective traffic load imposed by one RSS user,  $\theta < 1$ </td></tr><tr><td> $N, N_{C}, N_{R}$ </td><td>Total number of visitors, number of conventional visitors, and number of RSS visitors to a website:  $N = N_{R} + N_{C}$ </td></tr><tr><td> $x^{i}$ </td><td>Marginal visitor in Case  $i: i = <0,0>, <1,0>, <0,1>, \text{or } <1,1>$ </td></tr><tr><td> $\rho_{j}^{i}$ </td><td>Effective traffic load of website  $j$  in Case  $i: j = A \text{ or } B \text{ and } i = <0,0>, <1,0>, <0,1>, \text{or } <1,1>$ </td></tr><tr><td> $r, r_{1}, r_{2}$ </td><td>Percent of conventional users visiting website A in Case  $<1,0>, \text{Percent of conventional users visiting website A in Case } <1,1>, \text{Percent of RSS users visiting website A in Case } <1,1>$ </td></tr><tr><td> $N_{j}^{i}, N_{C,j}^{i}, N_{R,j}^{i}$ </td><td>Total number of visitors, number of conventional visitors, and number of RSS visitors to website  $j$  in Case  $i: j = A \text{ or } B \text{ and } i = <0,0>, <1,0>, <0,1>, \text{or } <1,1>$ </td></tr><tr><td> $\pi_{j}^{i}$ </td><td>Profit of website  $j$  in Case  $i: j = A \text{ or } B \text{ and } i = <0,0>, <1,0>, <0,1>, \text{or } <1,1>$ </td></tr></table>

Alternatively, the website can use RSS feeds to push specific online content with value b to potential users. Under the push model, users click on the link sent to them by the RSS software and are taken to the targeted content immediately. Meanwhile, the RSS software will help to block most online ads. Users are able to skip the website browsing and searching process, while also avoiding the cost of viewing unwanted ads. Since these users do not browse the website as conventional visitors do, they will consume less online content. Their total payment for online content consumption is $p _ { R } \leq p _ { C } .$ . These users are RSS visitors. Their utility function is $U _ { R } = b$ $- \ w \rho - p _ { R } ,$ with subscript R indicating RSS visitors.

Let N, $N _ { C } ,$ and $N _ { R }$ be the total number, respectively, of visitors, number of conventional visitors, and number of RSS visitors to a website, and $N = N _ { C } + N _ { R }$ Again, the subscript C is for conventional visitors and R for RSS visitors. Equation 1 gives the profit function of a website:

$$
\pi = A \cdot N _ {c} + p _ {c} \cdot N _ {c} + p _ {R} \cdot N _ {R} - c \cdot \rho .\tag{1}
$$

The website’s revenue consists of two parts, online advertising revenue and content-sales revenue.

First, the website gains advertising revenue $( A \cdot N _ { C } ) . ^ { 7 }$ Conventional visitors, when searching and browsing the site, are exposed to a variety of online ads. The expected advertising revenue from an average conventional visitor is denoted by A. RSS visitors, however, do not contribute to online advertising revenue because they directly access the targeted content through the link provided in RSS feeds.<sup>8</sup> First, I analyze the case of RSS feeds that are ad-free.

Second, the website gains content-sales revenue $( p _ { C } . N _ { C } + p _ { R } . N _ { R } ) . ^ { 9 }$ Conventional and RSS visitors will consume online content, but at different levels. Recall that $p _ { C }$ is the expected content-sales revenue from a conventional visitor, $p _ { R }$ is the expected content-sales revenue from an RSS visitor, and $p _ { C } \geq p _ { R }$

The website bears site-maintenance costs cρ, where c is the unit maintenance cost and ρ is the effective traffic load of the website. Conventional and RSS visitors visit the website in distinct ways, and impose different levels of traffic load. Conventional visitors browse and search the site, downloading and visiting a number of web pages. I normalize the traffic load imposed by a conventional visitor to be 1. RSS visitors skip the search and view only pages with the targeted content. They impose less traffic load, which is assumed to be $\theta , \ \theta < 1$ . So the website’s total effective traffic load can be written as:

$$
\rho = N _ {C} + \theta N _ {R}.\tag{2}
$$

Finally, I make Assumption 1: $S + p _ { c } - a \le b \le S + p _ { c } + a w$ . If the right inequality is violated, the website will always attract all potential users, leading to a fully covered market; if the left inequality is violated, the website will get no visitors, leading to an empty market.

## Competitive Analysis

In this section I analyze the competition between two websites, A and B. When websites take their respective content-delivery methods—to actively push online content to users via RSS or wait for users to pull content from them passively in the conventional way<sup>10</sup>—there are four possible cases.

## Case ${ \mathrm { < 0 , 0 > } }$ : Both Websites Do Not Offer RSS Feeds

When RSS feeds are not offered, users must pull online content from websites. Figure 1 depicts the competitive market segmentation in Case ${ \mathrm { < 0 , 0 > } }$

As in Figure 1, the marginal user—who is indifferent between visiting a website or staying out of the market—is denoted by $x ^ { < 0 , 0 > }$ , where $x ^ { < 0 , 0 > }$ is his net value from web browsing, and the superscript is used to indicate Case ${ \mathrm { < 0 , 0 > } }$ . This user gains zero utility from visiting a website; hence $x ^ { < 0 , 0 > }$ is given by:

$$
x ^ {<   0, 0 >} + b - p _ {c} - S - w \cdot \rho_ {i} ^ {<   0, 0 >} = 0, i = \mathrm{AorB}.\tag{3}
$$

The superscript indicates the case and the subscript indicates websites (A or B) or visitors (C for conventional and R for RSS visitors). For example, ${ \rho } _ { A } ^ { < 0 , 0 > }$ is the traffic load of website A in Case $< 0 , 0 >$

Figure 1 shows that users in $[ x ^ { < 0 , 0 > } , a ]$ , who gain higher net value from web browsing, will choose to visit a website (either A or B with equal probability); whereas users in $[ 0 , x ^ { < 0 , 0 > } ]$ , who gain lower net value from web browsing, will not visit any website. It is easy to see that the two websites will have the same traffic load $\rho _ { i } ^ { < 0 , 0 > } = ( a - x ^ { < 0 , 0 > } ) / 2$ ; i A or B in this case.<sup>11</sup> Solving this problem yields:

● Proposition 1 (No RSS Market Proposition). When both websites do not offer RSS feeds, the marginal user is at $\begin{array} { r } { x ^ { \langle 0 , 0 \rangle } = \frac { - b + p _ { C } + S + a w / 2 } { 1 + w / 2 } } \end{array}$ : The traffic load, number of visitors, and profit for each website are $\rho _ { i } ^ { \left. 0 , 0 \right. } = N _ { i } ^ { \left. 0 , 0 \right. } =$ $\begin{array} { r } { \frac { a + b - p _ { C } - S } { 2 + w } \ a n d \ \pi _ { i } ^ { \langle 0 , 0 \rangle } = \frac { ( a + b - p _ { C } - S ) ( A + p _ { C } - c ) } { 2 + w } , \ i = A o r B . } \end{array}$

Case $^ { < 1 , 0 > }$ and Case $< 0 , 1 > :$ One Website Offers RSS Feeds and the Other Does Not

These two cases are symmetric. Without loss of generality, I study Case $\mathrm { < } 1 , 0 \mathrm { > } ,$ , in which website A adopts RSS whereas website B does not. Note that among the whole user population, only β percentage is aware of RSS technology. These users are called RSS-aware users, who may choose to access online content through RSS. In contrast, the rest—1 – β users—are RSS-unaware; when visiting a website, they always use the conventional pull method regardless of whether RSS feeds are available. I analyze RSS-aware and RSS-unaware users separately. Figure 2 depicts the competitive market outcome in this case.

![](/api/attachments/QFAU6GTE/fulltext/images/af4fe53f1d3d1fd902faca29490917b318c3121b776b05a9cb21a8000801bc5a.jpg)  
Figure 1. The Case <0,0> Market Segmentation

![](/api/attachments/QFAU6GTE/fulltext/images/40b1e5b0991ee5d5887be9eaea90e2735726e2929c090d151aa6a55141fedc65.jpg)  
Figure 2. The Case <1,0> Market Segmentation

First, consider the choices of RSS-aware users. They must now decide whether to visit a website and, if so, which method (RSS or conventional) to use and which website (A or B) to visit. Figure (2a) demonstrates the final market segmentation among RSS-aware users. The RSS-aware user who is indifferent between the two visit methods is denoted by $x ^ { < 1 , 0 > } { } _ { R S S - a w a r e } ,$ and is given by:

$$
x _ {R S S - a w a r e} ^ {<   1, 0 >} + b - p _ {c} - S - w \cdot \rho_ {i} ^ {<   1, 0 >} = b - p _ {R} - w. \rho_ {i} ^ {<   1, 0 >},\tag{4}
$$

where the left side of the equation is the user’s utility from the conventional method and the right side is the utility from the RSS method.

As Figure 2a shows, users whose net value from web browsing is larger than $x ^ { < 1 , 0 > } { } _ { R S S - a w a r e } ,$ namely, those located in $[ x ^ { < 1 , 0 > } { } _ { R S S - a w a r e } , a ]$ , are conventional visitors; there are $\beta \ ( a - x ^ { < 1 , 0 > } { } _ { R S S - a w a r e } )$ of them. Suppose that website A gets r percent of these conventional users and B gets 1 – r percent of them, where r is an endogenous value that needs to be solved in the model. Users whose net value from web browsing is smaller than $x ^ { < 1 , 0 > }$ <sub>RSS-aware</sub>, namely, those located in [0, $x ^ { < 1 , 0 > } { } _ { R S S - a w a r e } ] .$ , will either become RSS visitors (to website A) or simply stay out of the market. So, there are ${ N _ { R } } ^ { < 1 , 0 > }$ RSS visitors in $[ 0 , { x ^ { < 1 , 0 > } } _ { R S S - a w a r e } ]$ , who visit website $\operatorname { A } ;$ the rest, $\beta ~ ( x ^ { < 1 , 0 > } { _ R S S - a w a r e } - N _ { R } ^ { < 1 , 0 > } )$ , stay out of the market.

Next, consider the choices of RSS-unaware users. They will opt either to stay out of the market or to become conventional visitors. Figure 2b depicts the final market segmentation among RSS-unaware users. The one who is indifferent between visiting a website and not visiting any website at all is denoted by $< x ^ { < 1 , 0 > } { } _ { R S S - u n a w a r e } ,$ and is given by:

$$
x ^ {<   1, 0 >} _ {R S S - u n a w a r e} + b - p c - S - w \rho_ {i} ^ {<   1, 0 >} = 0.\tag{5}
$$

Hence, there are $( 1 ~ - ~ \mathsf {  ~ \beta ~ } ) ( a ~ - ~ \mathsf {  ~ x ~ } ^ { < 1 , 0 > } \mathsf {  ~ \beta ~ } _ { R S S - u n a w a r e } )$ conventional visitors in $[ { x ^ { < 1 , 0 > } } _ { R S S - u n a w a r e } , ~ a ] ; ~ r$ percent of them go to website A, and $1 - r \mathrm { \ g o }$ to website B. Users in $[ 0 , x ^ { < 1 , 0 > } { } _ { R S S - u n a w a r e } ]$ stay out of the market.

The following set of equations characterizes the market outcome.

$$
\rho_ {B} ^ {<   1, 0 >} = (1 - r) \{\beta (a - x _ {R S S - a w a r e} ^ {<   1, 0 >}) + (1 - \beta) (a - x _ {R S S - u n a w a r e} ^ {<   1, 0 >}) \}\tag{6}
$$

$$
\rho_ {A} ^ {<   1, 0 >} = r \left\{\beta \left(a - x _ {R S S - a w a r e} ^ {<   1, 0 >}\right) + (1 - \beta) \left(a - x _ {R S S - u n a w a r e} ^ {<   1, 0 >}\right) \right\} + \theta N _ {R} ^ {<   1, 0 >}\tag{7}
$$

$$
b - p _ {R} - w \mathsf {p} _ {A} ^ {<   1, 0 >} = 0\tag{8}
$$

$$
0 \leq N _ {R} ^ {<   1, 0 >} \leq \beta x _ {R S S - a w a r e} ^ {<   1, 0 >}\tag{9}
$$

Equations 6 and 7 show the effective traffic load for each website. Website B has only conventional visitors, either RSS-aware or RSS-unaware. Website A has both conventional visitors, each imposing one unit of traffic load, and RSS visitors, each imposing θ unit of traffic load.<sup>12</sup> Equation 8 shows that in equilibrium, an RSS visitor gains zero utility. Equation 9 yields two boundary conditions: $( 1 ) 0 { \leq } N _ { R } { } ^ { < 1 , 0 > }$ states that there is a nonnegative number of RSS visitors, and (2) $N _ { R } { } ^ { < 1 , 0 > } \le \beta x ^ { < 1 , 0 > } { } _ { R S S - a w a r e }$ states that the number of RSS visitors is bounded by the number of RSS-aware users. Solving these equations gives:

● Proposition 2 (One RSS Market Preposition). When only one website offers RSS:

(1) The marginal user is at $x ^ { < 1 , 0 > } = S + p c - p _ { R }$ . Both websites have the same effective traffic load $\begin{array} { r } { \rho _ { i } ^ { < 1 , 0 > } = \frac { b - p _ { R } } { w } , \ i = A } \end{array}$ or B The website with RSS gets more visitors than the one without.

(2) The website with RSS gains higher profit than the one without, if and only if RSS visitors’ content-sales contribution is high enough: $p _ { R } { > } p ^ { * } { _ R } = \Theta \left( A + p _ { C } \right)$

(3) This market outcome holds if and only if search costs for the conventional method are high, $\begin{array} { r } { S \ge \frac { - b + p _ { R } + a r w } { w r } - p _ { c } + p _ { R } } \end{array}$ and users’ RSS-awareness level is $\begin{array} { r } { h i g h , \beta \geq \frac { w ( S + p _ { C } - p _ { R } - a ) + 2 ( b - p _ { R } ) } { w \theta ( S + p _ { C } - p _ { R } ) } } \end{array}$

See the Appendix for proofs of all of the main results in this article.

This proposition describes the market outcome when only one website offers RSS, and identifies two necessary conditions for this outcome. The first inequality, $S \geq$ $\frac { - b + p _ { R } + a r w } { w r } - p _ { c } + p _ { R }$ is called the nondegeneration condition. The violation of this condition, meaning that the search cost in the conventional visit method is too low, leads to the outcome that $\mathrm { C a s e } < 1 , 0 >$ degenerates to $\mathrm { C a s e } < 0 { , } 0 { > }$ . As a result, no user will choose to use the RSS method even if it is offered. The second inequality, $\beta \geq$ $\frac { w ( S + p _ { C } - p _ { R } - a ) + 2 ( b - p _ { R } ) } { w \theta ( S + p _ { C } - p _ { R } ) }$ ; is called the critical awareness condition. If it is violated, the RSS-awareness among users is too low. As a result, the number of RSS visitors will be limited by the number of RSS-aware users, and the stated market outcome is not valid.<sup>14</sup>

When both conditions hold, this proposition reveals an interesting finding: the RSS adopter (website A) may gain higher or lower profit in competition with the nonadopter (website B). The adopter will gain higher profit than its nonadopter competitor if and only if RSS visitors are able to contribute enough content-sales revenue, exceeding a threshold value ${ p _ { R } } ^ { * }$ . This suggests that the RSS use may not always add value for the adopter in a competitive setting, similar to what has been found in a monopoly setting [27].

## Case <1,1>: Both Websites Offer RSS Feeds

The final market segmentation, in which both websites provide RSS feeds, is shown in Figure 3. Again, the choices of RSS-aware and RSS-unaware users are analyzed separately.

The RSS-aware user who is indifferent between the two methods is denoted by $x ^ { < 1 , 1 > } { } _ { R S S - a w a r e }$ in Figure 3a, and is given by

$$
x _ {R S S - a w a r e} ^ {<   1, 1 >} + b - p _ {c} - S - w \cdot \rho_ {i} ^ {<   1, 1 >} = b - p _ {R} - w \cdot \rho_ {i} ^ {<   1, 1 >}.\tag{10}
$$

Users in $[ x ^ { < 1 , 1 > } { } _ { R S S - a w a r e } , a ]$ are conventional visitors, and there are $\beta ( a - x ^ { < 1 , 1 > }$ RSS-$_ { a w a r e } )$ of them. Website A gets $r _ { 1 }$ percentage of these conventional users and B gets $1 - r _ { 1 }$ percentage. Users in $[ 0 , { x ^ { < 1 , 1 > } } _ { R S S - a w a r e } ]$ will either become RSS visitors or simply stay out of the market. There are ${ N _ { R } } ^ { < 1 , 1 > }$ RSS visitors in $[ 0 , { x ^ { < 1 , 1 > } } _ { R S S - a w a r e } ] ,$ among which $r _ { 2 }$ percentage visit website A and $1 - r _ { 2 }$ percentage visit website B. Here, the values of both $r _ { 1 }$ and $r _ { 2 }$ are endogenously determined. The rest, $\beta ( x ^ { < 1 , 1 > } { } _ { R S S - a w a r e } - N _ { R } { } ^ { < 1 , 1 > } )$ , stay out of the market.

In Figure 3b, the RSS-unaware user who is indifferent between visiting a website or not is denoted by $x ^ { < 1 , 1 > } { } _ { R S S - u n a w a r e } ,$ and is given by:

$$
x ^ {<   1, 1 >} _ {R S S - u n a w a r e} + b - p _ {c} - S - w \cdot \rho_ {i} ^ {<   1, 1 >} = 0.\tag{11}
$$

![](/api/attachments/QFAU6GTE/fulltext/images/997b0eea49f1c29ef5912fc0bfb7cf4371d43f4f041d69bd7c1d44163be4de96.jpg)  
Figure 3. The Case <1,1> Market Segmentation

In total, there are $( I - \beta ) \left( a - x ^ { < 1 , 1 > } { } _ { R S S - u n a w a r e } \right)$ conventional visitors in $[ x ^ { < 1 , 1 > } _ { R S S }$ <sub>unaware</sub>, $a ] ; r _ { 1 }$ percentage of them visit A and $1 - r _ { 1 }$ percentage visit B. Users in $[ 0 , x ^ { < 1 , 1 > }$ <sub>RSS-unaware</sub>] choose to stay out of the market.

The following set of equations characterizes the market outcome:

$$
\begin{array}{l} \rho_ {A} ^ {<   1, 1 >} = r _ {1} \beta (a - x _ {R S S - a w a r e} ^ {<   1, 1 >}) + r _ {1} (1 - \beta) (a - x _ {R S S - u n a w a r e} ^ {<   1, 1 >}) \\ \qquad + \theta r _ {2} N _ {R} ^ {<   1, 1 >} \end{array}\tag{12}
$$

$$
\rho_ {B} ^ {<   1, 1 >} = (1 - r _ {1}) \beta (a - x _ {R S S - a w a r e} ^ {<   1, 1 >}) + (1 - r _ {1}) (1 - \beta)
$$

$$
(a - x _ {R S S - u n a w a r e} ^ {<   1, 1 >}) + \theta (1 - r _ {2}) N _ {R} ^ {<   1, 1 >}\tag{13}
$$

$$
b - p _ {R} - w \rho_ {i} ^ {<   1, 1 >} = 0\tag{14}
$$

$$
0 \leq N _ {R} ^ {<   1, 1 >} \leq \beta x _ {R S S - a w a r e} ^ {<   1, 1 >}\tag{15}
$$

These equations have meanings similar to Equations 6 to 9 in the Case $^ { < 1 , 0 > }$ Equations 12 and 13 are the effective traffic load for websites A and B. There are in total $\beta ( a ~ - ~ x ^ { < 1 , 1 > } { } _ { R S S - a w a r e } ) ~ + ~ ( 1 ~ - ~ \beta ) ~ \cdot ~ ( a ~ - ~ x ^ { < 1 , 1 > } { } _ { R S S - u n a w a r e } )$ conventional visitors; website A gets $r _ { 1 }$ percent and website B gets $( 1 ~ - ~ r _ { 1 } )$ percent. There are in total ${ N _ { R } } ^ { < 1 , 1 > }$ RSS visitors; website A gets $r _ { 2 }$ percent and website B gets $( 1 - r _ { 2 } )$ percent. Equation 14 shows that in equilibrium, an RSS visitor gains zero utility. Equation 15 gives the two boundary conditions. Solving Equations 10 to 15 yields:

● Proposition 3 (Both RSSs Market Prepostion). When both websites offer RSS feeds:

(1) In the symmetric outcome, the marginal visitor is at $x ^ { < I , I > } S + p _ { C } - p _ { R } .$ Both websites get the same effective traffic load: ${ \rho _ { A } } ^ { < 1 , 1 > } = { \rho _ { B } } ^ { < 1 , 1 > } = ( b - p _ { R } ) / w .$ They also gain the same profit: $\begin{array} { r } { \pi _ { i } ^ { < 1 , 1 > } = \frac { ( a - S - p _ { c } + p _ { R } ) \cdot ( A + \hat { p } _ { c } ) } { 2 } + \frac { w ( S + p _ { c } - p _ { R } - a ) + 2 b - \hat { p _ { R } } } { w \theta } } \end{array}$ $\begin{array} { r } { \cdot \ p _ { R } \frac { \left( b - p _ { R } \right) } { w } , \ i = A o r B . } \end{array}$

(2) This market outcome holds if and only if search costs in the conventional visit method are high, $\begin{array} { r } { S \ge \frac { - b + p _ { R } + a w / 2 } { w / 2 } - p _ { c } + p _ { R } } \end{array}$ ; and users’ RSS-awareness level is high, $\begin{array} { r } { \beta \ge \frac { w ( S + p _ { C } - p _ { R } - a ) + 2 \dot { ( } b - p _ { R } ) } { w \theta ( S + p _ { C } - p _ { R } ) } } \end{array}$

Proposition 3 states the Case $< 1 , 1 >$ outcome and the nondegeneration and critical awareness conditions to support it. The two conditions are that the RSS-awareness level among users must exceed a critical threshold, and search cost in the conventional method must be high enough. Although Proposition 3 addresses only symmetric outcomes, I have shown that asymmetric conditions can also exist; and the existence conditions have been derived in the Appendix.

## RSS Adoption Equilibrium Analysis

So far, I have analyzed four possible cases—namely, both websites do not adopt Case <0,0>, only one website adopts Case <0,1> or <1,0>, and both websites adopt Case <1,1>. In the competition, a website’s RSS adoption decision must be strategic: it must expect the competitor’s response, and the interaction between the two websites will determine the market equilibrium. The four cases may or may not appear as the equilibrium outcomes. Analyzing them is meaningful because it serves as a stepping-stone to the final equilibrium to explain the rationale of why one case is the equilibrium outcome and another is not.

I will next study websites’ strategic adoption decisions. I will consider both sequential and simultaneous adoption, identifying and assessing different equilibrium outcomes. My analyses will focus on scenarios in which the nondegeneration condition and critical awareness condition in Propositions 2 and 3 hold.<sup>15</sup> In addition, for Case <1,1>, I will use the symmetric market outcome as stated in Proposition 3.

## Sequential RSS Adoption

Next, I study websites’ sequential adoption decision. The two websites decide to adopt or not adopt RSS in a sequential order. Without loss of generality, let website A be the first decision maker and B be the second. The sequential decision tree is presented in Figure 4.

When a website adopts RSS feeds before its competitor, we call it the first RSS adoption; when a website adopts RSS feeds after its competitor, we call it the second RSS adoption. Before presenting the sequential equilibrium, I study the effects of first and second RSS adoption. I assert Lemma 1, which shows the comparison results for website traffic load, the number of visitors, and the number of conventional and RSS visitors across different cases.

![](/api/attachments/QFAU6GTE/fulltext/images/516b8f21c5238b5166d35d3bff96c96fecbe9035f86432e0b71b767f05d8f026.jpg)  
Figure 4. Decision Tree and Payoffs for Sequential Adoption

● Lemma 1 (Comparison Results for Website Traffic). The results are: (1) Website traffic load $\rho _ { i } ^ { < 0 , 0 > } < \rho _ { A } ^ { < 1 , 0 > } = \rho _ { B } ^ { < 1 , 0 > } = \rho _ { i } ^ { < 1 , 1 > } , i = A$ or B; (2) the total number of visitors $N _ { i } ^ { < 0 , 0 > } < N _ { A } ^ { < 1 , 0 > } < N _ { i } ^ { < 1 , 1 > } < N _ { A } ^ { < 1 , 0 > } , i = A$ or B; and (3) the number of conventional visitors: $N _ { _ { C , A } } ^ { < 1 , 0 > } < N _ { _ { C , i } } ^ { < 1 , 1 > } < N _ { _ { C , i } } ^ { < 0 , 0 > } < N _ { _ { C , B } } ^ { < 1 , 0 > } , i = A \mathrm { o r } B .$

The way to read Lemma 1 is via Table 2, which shows changes after the first and second RSS adoption.

In Table 2, the website that adopts RSS is called the adopting website, and the other is called the competing website. The sign “+” indicates an increase after adoption, “–” indicates a decrease, and “none” indicates no change. As Table 2 shows, the first RSS adoption always brings in more traffic load for both the adopter and its competitor, while the second RSS adoption has no impact on either website’s traffic level. The results for changes in the number of total and conventional visitors are intuitive. The first RSS adoption increases the market size for both websites, whereas the second RSS adoption increases the adopter’s market size but decreases the competitor’s market size. Both the first and second adoptions always decrease the number of conventional visitors to the adopting website and increase the number of conventional visitors to the competing website.

For websites’ profit change after the RSS adoption though, I find there is no definite answer: it can increase or decrease, depending on $p _ { R } ,$ , the expected contentsales revenue per RSS visitor. So I offer:

Proposition 4 (Impact of os Adoption Proposition). There are two critical values for the expected content-sales revenue per RSS visitor, denoted by ${ p _ { R } } ^ { I }$ and ${ p _ { R } } ^ { 2 }$ , and ${ p _ { R } } ^ { I } < { p _ { R } } ^ { 2 }$

(1) Impact of the first RSS adoption is as follows. If $p _ { R } > { p _ { R } } ^ { I }$ , the adopting website’s profit increases; if $p _ { R } ~ < ~ { p _ { R } } ^ { I }$ , the adopting website’s profit decreases. On the other hand, the competing website’s profit always increases.

(2) The impact of second RSS adoption is as follows. $I f p _ { R } > { p _ { R } } ^ { 2 } ,$ , the adopting website’s profit increases but the competing website’s profit decreases; if $p _ { R } < { p _ { R } } ^ { 2 }$ , the adopting website’s profit decreases but the competing website’s profit increases.

The last column in Table 2 summarizes this proposition. The main conclusion is interesting. Adopting RSS technology in a competitive setting, whether as the first adopter or second follower, may not enhance the website’s profits. The first adoption may increase or decrease the adopting website’s profit, but will always increase the competing website’s profit; the second adoption will have the opposite effect on the adopting and competing websites. It will always increase the profit of one website while decreasing the profit of the other, which puts the two websites in a conflict of interest position. Specifically, I highlight several cases in which RSS adoption may decrease the adopter’s profit while increasing its competitor’s profit. For example, when $p _ { R } < { p _ { R } } ^ { 1 }$ , the first RSS adoption will hurt the adopter but benefit the competitor. Another example is that when $p _ { R } <$ ${ p _ { R } } ^ { 2 } .$ , the second RSS adoption will also hurt the adopter but benefit its competitor. In both examples, the beneficiary of the RSS is the competitor, not the adopter.

<table><tr><td rowspan="2"></td><td colspan="2">Effective traffic load</td><td colspan="2">Total number of visitors</td><td colspan="2">Number of conventional visitors</td><td colspan="2">Profit</td></tr><tr><td>Adopting website</td><td>Competing website</td><td>Adopting website</td><td>Competing website</td><td>Adopting website</td><td>Competing website</td><td>Adopting website</td><td>Competing website</td></tr><tr><td>First adoption</td><td>+</td><td>+</td><td>+</td><td>+</td><td>-</td><td>+</td><td>+ if  $p_R > p_R^1$  - if  $p_R < p_R^1$ </td><td>+</td></tr><tr><td>Second adoption</td><td>none</td><td>none</td><td>+</td><td>-</td><td>-</td><td>+</td><td>+ if  $p_R > p_R^2$  - if  $p_R < p_R^2$ </td><td>+ if  $p_R < p_R^2$  - if  $p_R > p_R^2$ </td></tr></table>

<sub>Impact</sub> <sub>of</sub> <sub>First</sub> <sub>an</sub><sup>d</sup> <sup>Second</sup> <sup>RSS</sup> <sup>A</sup>

Table 2 shows what will happen to the competition outcome if a website adopts RSS. This analysis helps the website to assess the impact of its actions and make a rational adoption decision, which will eventually lead to the adoption equilibrium. To complete the analysis, I now derive the equilibrium outcomes in the sequential setting. Without loss of generality, website A is assumed to be the first decision maker and B the second, consistent with the decision tree in Figure 4, and I offer:

● Proposition 5 (Sequential Equilibrium Proposition). In a sequential adoption game in which website A moves before B, the equilibrium outcome depends on $p _ { R } ,$ , the expected content-sales revenue contribution of an RSS visitor.

(1) $I f p _ { R } < { p _ { R } } ^ { I }$ , the equilibrium is ${ \mathrm { < 0 , 0 > } }$ and both websites do not adopt;

(2) $I f p _ { R } { } ^ { I } < p _ { R } < { p _ { R } } ^ { 2 }$ , the equilibrium $i s < 0 , 1 >$ , then website A does not adopt but B adopts;

(3) $H p _ { R } > { p _ { R } } ^ { 2 }$ , the equilibrium is <1,1> and both websites adopt.

The two critical values, ${ p _ { R } } ^ { 1 }$ and ${ p _ { R } } ^ { 2 }$ , are defined in the Impact of Adoption Proposition (Proposition 4), and $p _ { R } ^ { \mathrm { ~ 1 ~ } } \ < \ p _ { R } ^ { \mathrm { ~ 2 ~ } }$ . The Sequential Equilibrium Proposition (Proposition 5) is depicted in Figure 5.

The interesting finding here is that, in a sequential adoption game, the market outcome <1,0> will never be the equilibrium. Why? This is because when ${ p _ { R } } < { p _ { R } } ^ { 2 }$ a website will always be worse off if it acts as the first RSS adopter: In the range of $p _ { R } < { p _ { R } } ^ { 1 }$ , RSS adoption will reduce the adopting website’s profit instead of increasing it. In the range of $p _ { R } { } ^ { 1 } < p _ { R } < p _ { R } { } ^ { 2 }$ though, the first adopter’s profit will be reduced by the competitor’s subsequent adoption. As a result, the website will choose not to be the first adoptor and thereby protects itself in a sequential game, leading to the equilibrium ${ \mathrm { < 0 , 0 > } }$ when ${ p _ { R } } < { p _ { R } } ^ { 1 }$ and equilibrium $^ { < 0 , 1 > }$ when ${ p _ { R } } ^ { 1 } <$ ${ p _ { R } } < { p _ { R } } ^ { 2 }$

![](/api/attachments/QFAU6GTE/fulltext/images/01d5774c04485fc64bf51ff95a7859b598766d33cde1244fbca70bb15978fbc9.jpg)  
Figure 5. Sequential Adoption Equilibrium

## Simultaneous RSS Adoption

Here, I study websites’ simultaneous adoption decisions.<sup>16</sup> The following proposition shows that multiple equilibria exist in the simultaneous game; which one to emerge will depend on $p _ { R } ,$ which is the expected content-sales revenue contribution of an RSS visitor:

● Proposition 6 (Simultaneous Equilibrium Proposition). In a simultaneous adoption game, the equilibrium outcome depends on $p _ { R } ,$ , the expected contentsales revenue contribution of an RSS visitor.

(1) $I f p _ { R } < { p _ { R } } ^ { 1 }$ , the equilibrium is ${ \mathrm { < 0 , 0 > } }$ and both websites do not adopt;

(2) $I f p _ { R } { } ^ { 1 } < p _ { R } < { p _ { R } } ^ { 2 }$ , the equilibrium is $< 0 , 1 > \mathrm { o r } < 1 , 0 > ,$ , one website adopts but the other does not;

(3) $I f p _ { R } > { p _ { R } } ^ { 2 }$ , the equilibrium is $\mathrm { < } 1 , 1 \mathrm { > } ,$ and both websites adopt.

Different simultaneous equilibria are demonstrated in Figure 6. The two critical values, ${ p _ { R } } ^ { 1 }$ and ${ p _ { R } } ^ { 2 }$ , are defined in the Impact of Adoption Proposition (Proposition $4 ) . ^ { 1 7 }$ In general, my finding shows that when $p _ { R }$ increases, a website’s incentive to adopt RSS increases. Under a large value of $p _ { R } \ ( p _ { R } > { p _ { R } } ^ { 2 } )$ , the $^ { < 1 , 1 > }$ equilibrium—that is, both websites adopt—is more likely. Under a small value of p<sub>R</sub> $( p _ { R } < { p _ { R } } ^ { 1 } )$ , the $\mathrm { < 0 , 0 > }$ equilibrium—that is, neither adopts—is expected. These findings are the same as those in a sequential adoption setting. When $p _ { R }$ is in the middle range $( p _ { R } { } ^ { 1 } < p _ { R } < p _ { R } { } ^ { 2 } )$ , however, the outcomes are different. In the simultaneous equilibrium, it will be either $^ { < 1 , 0 > }$ or $^ { < 0 , 1 > }$ , with an equal chance for either to appear. In the sequential equilibrium, however, the first decision maker—namely, website A—will always choose not to adopt, leading to the $^ { < 0 , 1 > }$ equilibrium. Note that ${ p _ { R } } < { p _ { R } } ^ { 2 }$ suggests ${ p _ { R } } < { p _ { R } } ^ { * }$ , where ${ p _ { R } } ^ { * }$ is the critical value defined in the One RSS Market Proposition (Proposition 2). Hence, in this equilibrium $^ { < 0 , 1 > }$ , website A, the nonadopter, always gains higher profit than website B, the adopter. (See Proposition 2.)

I derived all of the equilibria in the sequential and simultaneous adoption settings. Now I ask: in any equilibrium outcome, will the RSS technology benefit both websites, compared to the benchmark when RSS is not available at all? Or is it possible that the benefits of RSS, in the competition, might be captured by one website solely at the cost of the other? The next proposition offers my answer:

![](/api/attachments/QFAU6GTE/fulltext/images/4488d04d9384eb9d3ab227fd6fd6d611a23a3b6691bff090f26e473d002256b8.jpg)  
Figure 6. Simultaneous Adoption Equilibrium

● Proposition 7. (Benefits of RSS Proposition). In equilibrium, regardless of whether it adopts RSS, a website benefits from the RSS technology. In certain scenarios, the greatest profit improvement does not go to the adopting website, but rather to its competitor.

The proposition suggests that, when RSS is available, a website is always better off, even if it may not use RSS in equilibrium. The following numerical example demonstrates this result graphically. Figure 7 depicts the equilibrium profits. The x-axis has the values of $p _ { R } .$ The value range in which the nondegeneration conditions are satisfied is: $p _ { R } ~ \in ~ [ 1 . 3 , ~ 2 . 6 ]$ , calculated using the One RSS Market Proposition (Proposition 2) and Both RSSs Market Proposition (Proposition 3). I also indicate the two threshold values: ${ p _ { R } } ^ { 1 } \ : = \ : 1 . 6$ and ${ p _ { R } } ^ { 2 } = 2$ , calculated using the Impact of Adoption Proposition (Proposition 4). They result in four ranges: (1) for $p _ { R } \in [ 1 . 3 , ~ 1 . 6 ]$ , the equilibrium is ${ < } 0 , 0 { > }$ for both sequential and simultaneous games; (2) for $p _ { R } \in [ 1 . 6 , 2 ]$ , the equilibrium is $^ { < 0 , 1 > }$ for the sequential game, and $< 0 , 1 > \mathrm { ~ o r ~ } { < } 1 , 0 >$ for the simultaneous game; (3) for $p _ { R } \in [ 2 , 2 . 6 ]$ , the equilibrium is $^ { < 1 , 1 > }$ for both sequential and simultaneous games; and (4) for $p _ { R } > 2 . 6 ,$ the nondegeneration condition is violated and the market outcome falls back to ${ < } 0 , 0 >$ . There are three lines: lines 1 and 3 are the profits of website A and B in the sequential equilibrium respectively, where website A is the first decision maker in the game; line 2 is a website’s profit in the simultaneous equilibrium. These three lines are always above the benchmark profit line that is the horizontal straight line around the value 8.85. This suggests that when one or two websites adopts RSS, both are expected to get higher profits than what they obtain in the benchmark without the RSS technology.

![](/api/attachments/QFAU6GTE/fulltext/images/55a298c5069d17b7c3fce9d850109c7da570eeea5cc19140deab48757698fd66.jpg)  
Figure 7. Equilibrium Profit Comparison  
Notes: The parameter values used in this example are: $b = 8 ; a = 1 0 ; S = 5 ; p _ { C } = 4 ; w = 3 ;$ $\ A = 1 ; c = 0 . 1 ; \theta = 0 . 4$

In addition, the three lines overlap each other in Ranges 1, 3, and 4. In Range 2,<sup>18</sup> however, I show that line 1 > line 2 > line 3, meaning that “the profit of website A in the sequential game” > “the profit of a website in the simultaneous game” > “the profit of website B in the sequential game.” Note that in this case, website A’s strategy in the sequential game is not to adopt. This, as I pointed out, is because website A knows that if it adopts now, it will be hurt by its competitor’s sequential adoption at a later time. As a result, A chooses not to be the first adopter, which protects it from the competitor’s later action. In this scenario, nonadopter A’s profit is improved more than adopter B’s.

## RSS-Awareness Level Analysis

In the analysis so far, the RSS critical awareness condition is required. Only when users’ RSS-awareness level is higher than the critical value $\begin{array} { r } { \beta ^ { * } = \frac { w ( S + p _ { C } - p _ { R } - a ) + 2 ( b - p _ { R } ) } { w \theta ( S + p _ { C } - p _ { R } ) } } \end{array}$ will market outcomes for Cases <1,0> and $^ { < 1 , 1 > }$ hold, as stated in the One RSS Market Proposition (Proposition 2) and Both RSSs Market Proposition (Proposition 3). What will happen if RSS-awareness is lower than $\beta ^ { * 2 }$ How will a website’s profit be affected by the value of β in general? And do websites have any incentive to invest in educating users about RSS technology and therefore increase β? If so, to what level? I answer these questions by extending my analysis to the scenario in which only a small number of users know about RSS, that is, a market with a low RSS-awareness level β.

I investigate Cases <1,0> and <1,1> when $\beta < \beta ^ { \ast }$ . I reanalyze the market segmentation, recalculate the number of RSS and conventional visitors to each website, and rederive the equilibrium profit of each website. I established these following analytical results. (See Lemma 2 and its proof in the Appendix.) (1) When $\beta \ = \ 0$ , the market equilibrium is $^ { < 0 , 0 > }$ . This occurs even if RSS is available, but no one will use it because no user will know about its existence. (2) When $\beta \in ( 0 , \beta ^ { * } )$ , a website’s equilibrium profit is a complex function of β. (3) When $\beta \geq \beta ^ { * }$ , a website’s equilibrium profit is not a function of β. (See the proof of Propositions 2 and 3.) And finally, (4) in any equilibrium j $( j = < 0 , 1 >$ $< 1 , 0 > \ \mathrm { o r } \ < 1 , 1 > )$ , for any website i (i = A or B): $\pi _ { i } ^ { j } ( \beta ^ { * } ) > \pi _ { i } ^ { j } ( \beta = 0 )$ . (See the proof of Proposition 7.)

Based on these findings, I conclude that in the range $\beta \in ( 0 , \beta ^ { * } ]$ , there must be a value, denoted by $\beta _ { o p t i } ,$ which optimizes the website’s profit. This value $\beta _ { o p t i }$ is the optimal RSS-awareness level, in the sense that a website, regardless of whether it offers RSS in the equilibrium, has an incentive to invest and help boost users’ RSS-awareness up to $\beta _ { o p t i }$ . Beyond $\beta _ { o p t i } ,$ the website is no longer interested in doing this.

To demonstrate how the website’s equilibrium profit varies in $\beta ,$ and also to calculate $\beta _ { o p t i } ,$ I rely on numerical analysis. When setting parameter values, there are some “rules” to follow. First, the parameter values of {S, a, b, w, $p _ { C } \}$ must satisfy $S + p _ { C } - a \le b \le S + p _ { C } + a w .$ This is to ensure that Assumption 1 is satisfied. Second, the value of $p _ { R }$ must satisfy the nondegeneration conditions specified in Propositions 2 and 3. In addition, for every set of parameters, I need to calculate the two threshold values ${ p _ { R } } ^ { 1 }$ and ${ p _ { R } } ^ { 2 }$ using Proposition 4, as well as the critical value $\beta ^ { * }$ using Propositions 2 and 3. Figure 8 shows the results from one numerical example, which takes parameter values the same as in Figure 7. Figure 8a shows the two websites’ profits in the <1,0> equilibrium when $p _ { R } { } ^ { 1 } < p _ { R } { } < p _ { R } { } ^ { 2 }$ , and Figure 8b shows their profits in the <1,1> equilibrium when $p _ { R } > { p _ { R } } ^ { 2 } . ^ { 1 9 }$ In addition, the critical RSSawareness level $\beta ^ { * }$ is also highlighted in the figures: $\beta ^ { * } = 0 . 4 1 1$ in the $^ { < 1 , 0 > }$ equilibrium and $\beta ^ { * } = 0 . 1 2 6$ in the <1,1> equilibrium.

A website reaches its highest profit at $\beta ^ { * }$ , suggesting $\beta _ { o p t i } = \beta ^ { * }$ , regardless of whether it adopts RSS in equilibrium. So both websites have an incentive to invest in educating users about RSS until the critical RSS-awareness level $\beta ^ { * }$ More numerical analyses with different parameter input values showed that the profit function may have different forms in [0, β\*]—linearly or nonlinearly increasing, or first decreasing and then increasing in β. The result $\beta _ { o p t i } = \beta ^ { * }$ always seems to hold though.

These results may explain the discrepancy between websites’ and users’ RSS adoption rates. More than half of the websites today provide RSS feeds, while RSS adoption among users is much lower. It has remained at around 10 percent for the past five years [33]. Why do RSS adoption levels for the two sides not match each other? Should websites exert effort to educate Internet users about RSS? My results provide a possible answer. Users’ RSS-awareness level does not matter, as long as it exceeds a critical level. Especially when $p _ { R }$ is high, the required awareness level $\beta ^ { * }$ among users can be very small. For example, in Figure 8b, $\beta ^ { * }$ is only 12.6 percent, so only a small group of users (12.6 percent) with RSS-awareness will be good enough to support the market equilibrium <1,1>, in which both websites will adopt RSS. Once this 12.6 percent awareness level is reached, websites will not expend effort to promote RSS to users.

## Discussion and Conclusion

The use of RSS feeds on the Internet is an interesting problem to study. Currently, many websites have adopted RSS as a delivery mechanism to actively push online content to potential users, offering them an alternative way to visit websites. Use of RSS is expected to have an impact on both websites and users. My research goal has been twofold. First, I examined the economic impact of RSS adoption on websites in a duopoly market. I studied how RSS adoption by one website, both as first and second adopter, can affect traffic load and profits for both the website and its competitor. I analyzed the market equilibria in both sequential and simultaneous adoption scenarios. Second, I investigated changes in user website visit behavior after a website’s RSS adoption. When RSS feeds are available, who will use them and who will continue to use the conventional pull method? Are RSS-aware and RSS-unaware users affected differently? What is the role of the users’ RSS-awareness level, and should websites expend effort to educate users about RSS technology? I constructed a model to develop answers.

(a). Website's Profits in Equilibrium <1,0>  
![](/api/attachments/QFAU6GTE/fulltext/images/1eeb3c58cfae6311692bbd9a8072415da1554142558b21d75c4be7274627c185.jpg)

(b). Website's Profit in Equilibrium <1,1>  
![](/api/attachments/QFAU6GTE/fulltext/images/ee55dbe3fd9a95af93da1e1aa04eaa52b5cb4babd45d31957e6d75376daf6784.jpg)  
Figure 8. Website’s Profit Versus Users’ RSS-Awareness Level

My results demonstrate the compound effect of technology adoption on firm performance and market outcome in a competitive marketplace. Multiple lessons are learned, not only about RSS but also about other types of technology adoptions. For example, the firm must understand that a larger market share will not always lead to a higher profit. The resulting increased costs may outweigh the gains from the market expansion, making the adoption unprofitable. Also, the first mover will inevitably face the threat of being copied by a competing follower at a later time, especially when the adoption barrier is low. It is therefore important that a firm’s adoption decision should be evaluated from a market perspective by taking the competitor’s behavior into account. Adoption timing is critical. Finally, it is worth investing in users’ technology awareness level as a preparatory step toward a successful adoption.

## Discussion of the Major Results and Their Implications

My results highlight the complexity of a website’s RSS adoption decision. For example, I showed that under certain conditions, RSS adoption can negatively affect a website’s profits. In some scenarios, higher traffic brought on by RSS was accompanied by lower profits. A more interesting finding was that, in a competitive setting, a website’s RSS adoption decision can lead to an increase in profits for the competitor and, at the same time, a decrease in its own profits. The beneficiary of the RSS technology becomes the competitor rather than the adopter, and RSS, rather than offering a competitive advantage, becomes a disadvantage. A website may find itself at a disadvantage if it adopts RSS earlier than its competitor because its profits will be reduced if, later on, the competitor also adopts RSS. In this scenario, both websites will choose not to adopt but rather to wait, leading to the equilibrium that no one uses RSS. Finally, I showed that different equilibria can arise in sequential and simultaneous adoption settings, depending on expected content-sales revenue per RSS visitor. So we may not see unanimous adoption among websites.

My results also reveal that websites have an incentive to boost RSS-awareness among Internet users, but only up to a certain level. I identified a critical RSSawareness level. Before the level is reached, a website will benefit from the increasing number of users who understand RSS, regardless of whether it adopts RSS. So all websites should be interested in educating potential users about RSS technology, because increasing RSS-awareness among users will improve profits for them. When the critical RSS-awareness level has been reached, however, the website’s profits will no longer be affected. As a result, it no longer makes sense to promote RSS technology. This may explain why, in recent years, RSS-awareness among Internet users has increased slowly, though more websites now offer RSS feeds.

My results also suggest that different types of websites are using RSS for different purposes—news portals and bloggers want RSS for increasing publicity, and ecommerce websites use RSS as a tool for improving profits. The finding that only when expected content-sales revenue per RSS visitor is high, RSS adoption will improve the adopting website’s profit, suggests that RSS feeds are most suited to websites that gain high content-sales revenue. E-commerce websites, which gain revenue mainly from selling commodities or providing online services, are likely to enjoy profit improvement from RSS use. In recent years, RSS feeds on e-commerce websites have been used mainly to update users about product arrivals, new deals, top sales, and so on, and the main purpose of RSS use for them is to build relationships with users, create purchase demand, and drive sales [3, 5, 41].

The situation for news portals and bloggers is different. Although RSS originated from these types of websites and has been widely adopted by them, my analysis shows that, for them, RSS may not deliver adequate content-sales revenue because most of these websites offer free online content. So these websites are expected to experience a profit reduction after RSS adoption. This conclusion is consistent with current practice, based on an increasing number of complaints from bloggers that their RSS feeds attract so much traffic load that it is difficult to monetize their sites [26].

So, for what purpose do news portals and bloggers adopt RSS? The fact is that profitability is never their major goal. Instead, they care about nonmonetary objectives: increasing market size, getting public attention, and extending their brands [5].<sup>20</sup> My analysis justifies their RSS adoption: afterward, the total number of visitors always increases and market size grows. (See Table 2.) In fact, lower profits after RSS adoption for news portals and bloggers have led publishers to explore the insertion of ads into RSS feeds, hoping their websites will be better monetized after RSS adoption [26, 30].<sup>21</sup> This validates my results.

## Discussion of Model and Limitations

Although my model is simple, it captures the essential differences between the RSS push and conventional pull methods. Through it, I was able to derive interesting results and apply the findings to generate useful RSS adoption strategies for websites. I acknowledge that reality is more complex than the proposed model. It makes simplifying assumptions that I will discuss next. I will also check the robustness of my results when these assumptions are relaxed, and present potential avenues for future research.

This work analyzes a two-stage sequential adoption game—website A makes the adoption decision first, and then website B, observing A’s choice, makes the decision afterward. In practice, such a decision-making process happens on a long timeline. At any time, a website can adopt RSS and it is not limited to a two-stage setting. When moving from the two-stage to infinite-stage sequential setting, the equilibrium outcomes, stated in the Sequential Equilibrium Proposition (Proposition 5), are expected to change partially. The proposition states that when $p _ { R } { } ^ { 1 } < p _ { R } < p _ { R } { } ^ { 2 }$ , the equilibrium is <0,1>. This is the scenario when website A does not want to adopt before B due to the disadvantage of being the first adopter. Considering a manystage decision process, the same logic will apply to website B: B does not want to adopt before A, and decides to wait as well. As a result, both websites will always wait, and <0,1> will not be equilibrium. Instead, it will lead to <0,0> equilibrium in the region of $p _ { R } { } ^ { 1 } < p _ { R } { } < p _ { R } { } ^ { 2 }$ . Meanwhile, the analyses and outcomes for ${ p _ { R } } < { p _ { R } } ^ { 1 }$ and ${ p _ { R } } > { p _ { R } } ^ { 2 }$ remain unchanged.

In addition, my model assumes that the RSS program is able to block online advertisements effectively. RSS visitors do not contribute to website advertising revenue, as conventional visitors do. In reality, however, advertisers believe that the use of RSS should not be a threat to the online advertising community and are starting to explore the technological potential of RSS advertising [16, 21]. NYTimes.com, Google AdSense, CrispAds, Kanoodle, and Pheedo, have begun inserting targeted text advertisements in their syndication feeds. To incorporate this into my model, I assume that RSS visitors are also exposed to a certain number of simple text advertisements; each RSS visitor therefore contributes to the website’s advertising revenue by $p _ { a d } ,$ where the current model setup is a special case of $p _ { a d } = 0$ . Now the revenue contribution per RSS visitor should be revised from $p _ { R }$ to $( p _ { R } ~ + ~ p _ { a d } )$ . Once using $( p _ { R } ~ + ~ p _ { a d } )$ to replace $p _ { R }$ in all expressions and equations, I find that all derivation steps remain the same, as do lemmas and propositions. There are two consequences under such a revision. First, websites are more likely to adopt RSS, and in both sequential and simultaneous games, the region of equilibrium <1,1> enlarges. Second, the nondegeneration conditions are more difficult to satisfy, meaning that degeneration is more likely to happen with the presence of RSS advertising. Together, I conclude that adding advertisements to RSS feeds could be profit-improving for websites; yet if the volume of advertisements is not in balance with the volume of content, RSS advertising will cancel out RSS use.

Finally, the current model assumes that different users gain different net values from web browsing x but the same value from consuming the specific targeted online content b. One possible extension is to assume that the latter value (b) is also heterogeneous among users. In the current solution, marginal users are characterized by x only (i.e., Equation (3) for Case <0,0>, Equations (4) and (5) for Case <1,0>, and Equations (10) and (11) for Case <1,1>). After revising this assumption, marginal users should be determined by both x and b, and specifically, by the sum of these two values (x + b). As a consequence, to demonstrate the final market segmentation, I need a two-dimensional graph, with one dimension for the value of x and the other for b. There should be an indifference line defined by the value of (x + b) in this two-dimensional space. All users residing in that indifference line are marginal users. Other than this revision, all logic and math derivation steps remain unchanged. As a result, I expect the major conclusions will hold.

Research on RSS could be conducted in other ways as well. For example, the current model considers two homogeneous competing websites. It would be interesting to examine whether similar conclusions could be drawn in the competition between two differentiated websites. In a heterogeneous duopoly setting, I can seek answers to research questions such as, “Is it true that only the cost-efficient website should adopt RSS?” or “Should only the website that gains heavy content-sales revenue offer RSS?” Also, my analytical results suggest that e-commerce websites are likely to be the main beneficiaries of RSS push technology. This theoretical prediction, however, currently has no empirical support. There are two reasons for this. First, use of RSS in ecommerce websites is in its early stages; data on the consequences of RSS use are scarce. Second, websites are cautious when publicizing their revenue and profit information. As time goes by, however, more data will become available, and therefore an empirical paper will be required to check the accuracy of theoretical predictions. People are just starting to explore the potential value of RSS in e-commerce. I expect more advanced RSS-featured business models to be developed and applied to the Internet in the future, which will deserve researchers’ attention.

## Appendix. Proofs of The Main Results

A. Proof for Proposition 2 (One RSS Market Proposition). From Equation 8, I $\mathrm { g e t } \rho _ { A } { } ^ { < 1 , 0 \geq } ( b - p _ { R } ) / w . \mathrm { P l u g g i n g }$ this into Equation 5, I get $x ^ { < 1 , 0 > }$ RSS- $_ { u n a w a r e } = S + p _ { C }$ $p _ { R } .$ . Also, Equation 4 gives $x ^ { < 1 , 0 > } { } _ { R S S - a w a r e } = S + p _ { C } - p _ { R } = x ^ { < 1 , 0 > }$ <sub>RSS-unaware</sub>. So the marginal user, among the RSS-aware and RSS-unaware user group, is the same. I denote this by $x ^ { < 1 , 0 > }$ . Now plugging the above expressions of traffic load and the marginal user into Equations 6 and 7, I get $\begin{array} { r } { r = 1 - \frac { b - p _ { R } } { w ( a - S - p _ { C } + p _ { R } ) } } \end{array}$ . In addition, Equation 7 suggests that $\begin{array} { r } { N _ { R } ^ { < 1 , 0 > } = \frac { r ( S + p _ { C } - p _ { R } ) } { \theta } - \frac { - b + p _ { R } + a r w } { w \theta } } \end{array}$ Next, I plug in $r _ { \mathrm { { + } } }$ ${ N _ { R } } ^ { < 1 , 0 > }$ , and $x ^ { < 1 , 0 > } { } _ { R S S - a w a r e }$ into the boundary condition in Equation 9 and get $\begin{array} { r } { S \ge \frac { - b + p _ { R } + a r w } { w r } - p _ { C } + p _ { R } ; ~ \beta ^ { * } \ge \frac { w ( S + p _ { C } - p _ { R } - a ) + 2 ( b - p _ { R } ) } { w \theta ( S + p _ { C } - p _ { R } ) } } \end{array}$

Finally, using Equation 1, the difference of website A’s and B’s profit can be written as: $\pi _ { A } ^ { < 1 , 0 > } - \pi _ { B } ^ { < 1 , 0 > } = ( A + p _ { C } ) \Big ( N _ { C , 4 } ^ { < 1 , 0 > } - N _ { C , B } ^ { < 1 , 0 > } \Big ) + N _ { R , 4 } ^ { < 1 , 0 > } \cdot p _ { R } > 0 \Leftrightarrow p _ { R } >$ $\begin{array} { r } { \frac { ( A + p _ { C } ) \left( N _ { C , A } ^ { < 1 , 0 > } - N _ { C , B } ^ { < 1 , 0 > } \right) } { N _ { R , A } ^ { < 1 , 0 > } } \equiv p _ { R } ^ { * } . } \end{array}$ . Since $\rho _ { { \scriptscriptstyle A } } ^ { < 1 , 0 > } = N _ { { \cal C } , { \scriptscriptstyle A } } ^ { < 1 , 0 > } + \mathrm { ~ \boldsymbol { \theta } ~ } \cdot N _ { { \scriptscriptstyle B } , { \scriptscriptstyle A } } ^ { < 1 , 0 > } = \rho _ { { \scriptscriptstyle B } } ^ { < 1 , 0 > } = N _ { { \cal C } , { \scriptscriptstyle B } } ^ { < 1 , 0 > } ,$ I have $N _ { C , A } ^ { < 1 , 0 > } - ~ N _ { C , B } ^ { < 1 , 0 > } = \Theta \cdot N _ { R , A } ^ { < 1 , 0 > }$ : As a result, $p _ { R } ^ { * } = \Theta \cdot \left( p _ { C } + A \right)$

B. Proof of Proposition 3 (Both RSSs Market Proposition). Equation 14 gives $\rho _ { i } ^ { < 1 , 1 > } = ( b - p _ { R } ) / w .$ . Plugging this into Equation 11, I get $x ^ { < 1 , 1 > }$ RSS-unaware $= S + p _ { C } -$ $p _ { R } .$ Also, Equation 10 gives $x ^ { < 1 , 1 > } \kappa \substack { S S s - a w a r e } = S + p _ { C } - p _ { R } = x ^ { < 1 , 1 > } u n a w a r e .$ So the marginal user, among the RSS-aware and RSS-unaware user group, is the same. To simplify, I denote it by just $x ^ { < 1 , 1 > }$ . Plugging the expressions of $x ^ { < 1 , 1 > } , \rho _ { i } ^ { < 1 , 1 > }$ , and $r _ { 1 } = r _ { 2 } = 0 . 5$ (since it is for a symmetric equilibrium) into Equations 12 or 13 yields $\begin{array} { r } { N _ { R } ^ { < 1 , 1 > } = \frac { ( S + p _ { C } - p _ { R } ) } { \theta } - \frac { - 2 b + 2 p _ { R } + a w } { w \theta } } \end{array}$ : The boundary condition in Equation 15 thus becomes $\begin{array} { r } { S \ge \frac { - b + p _ { R } + a w / 2 } { w / 2 } - p _ { C } + p _ { R } } \end{array}$ and $\begin{array} { r } { \beta \geq \frac { w \left( S + p _ { C } - p _ { R } - a \right) + 2 \left( b - p _ { R } \right) } { w \theta \left( S + p _ { C } - p _ { R } \right) } } \end{array}$ : Finally, I plug $x ^ { < 1 , 1 > } , N _ { R } ^ { < 1 , 1 > }$ and $\rho _ { i } ^ { < 1 , 1 > }$ into Equation 1 to get the website’s profit.

The above is for a symmetric equilibrium in Case <1,1> since it uses $r _ { 1 } = r _ { 2 } = 0 . 5$ in the derivation. An asymmetric equilibrium may exist in this case. In an asymmetric equilibrium, the expressions of marginal visitor and effective traffic load remain the same as in a symmetric equilibrium, and also the same boundary conditions apply. The value of ${ N _ { R } } ^ { < 1 , 0 > }$ and $r _ { 1 }$ and $r _ { 2 } ,$ however, should be rederived. Using Equations 12 and 14 I obtain $\begin{array} { r } { N _ { R } ^ { < 1 , 1 > } = \frac { - r _ { 1 } ( a - S + p _ { C } - p _ { R } ) } { \theta r _ { 2 } } + \frac { b - p _ { R } } { w \theta r _ { 2 } } } \end{array}$ : By further plugging this expression into $\rho _ { A } ^ { < 1 , 1 > } \rho _ { B } ^ { < \ddot { 1 } , 1 > }$ , and then using Equations 12 and 13, I get $\begin{array} { r } { \frac { 4 r _ { 1 } r _ { 2 } - r _ { 1 } - r _ { 2 } } { 2 r _ { 2 } - 1 } = \frac { b - p _ { R } } { w ( a - S - p _ { C } + p _ { R } ) } } \end{array}$ : That is, in any asymmetric equilibrium, the pair $\{ r _ { 1 } r _ { 2 } \}$ must satisfy this relationship.

C. Proof of Lemma 1 (Comparison Results for Website Traffic). (1) $\begin{array} { r } { \boldsymbol { \rho } _ { A } ^ { < 1 , 0 > } = \boldsymbol { \rho } _ { B } ^ { < 1 , 0 > } = \boldsymbol { \rho } _ { i } ^ { < 1 , 1 > } = \frac { b - p } { w } } \end{array}$ , and $\rho _ { i } ^ { < 0 , 0 > } { < } \rho _ { A } ^ { < 1 , 0 > }$ when the nondegeneration condition holds. (2) First I prove that $N _ { i } ^ { { < } 1 , 1 > } { < } N _ { A } ^ { { < } 1 , 0 > }$ . Note that $x _ { i } ^ { < 1 , 1 > } = x _ { A } ^ { < 1 , 0 > }$ . It means, from Case $< 1 , 0 >$ to Case $^ { < 1 , 1 > }$ , some RSS visitors switch to website B, so $N _ { R , A } ^ { < 1 , 1 > } < N _ { R , A } ^ { < 1 , 0 > }$ , and meanwhile some conventional visitors switch to website A:

$N _ { C , A } ^ { < 1 , 1 > } > N _ { C , A } ^ { < 1 , 0 > }$ . Since $\rho _ { i } ^ { < 1 , 1 > } = \rho _ { A } ^ { < 1 , 0 > }$ , it must be the case that, for website A, the increase of conventional visitors is less than the decrease of RSS visitors. Therefore, the total number of visitors to website A decreases: $N _ { i } ^ { { < } 1 , 1 > } { < } N _ { A } ^ { { < } 1 , 0 > }$ . Also, $N _ { i } ^ { < 1 , 1 > } > N _ { B } ^ { < 1 , 0 > }$ under the nondegeneration condition, and $N _ { i } ^ { < 0 , 0 > } = \boldsymbol { \rho } _ { i } ^ { < 0 , 0 > } { < \rho _ { B } ^ { < 1 , 0 > } } = N _ { B } ^ { < 1 , 0 > }$ . (3) From $x ^ { < 1 , 1 > } \ x ^ { < 1 , 0 > } > x ^ { < 0 , 0 > }$ and $r < 0 . 5$ , it is easy to get $N _ { C , A } ^ { < 1 , 0 > } < N _ { C , i } ^ { < 1 , 1 > } < N _ { C , i } ^ { < 0 , 0 > }$ . To see $N _ { C , i } ^ { < 0 , 0 > } < N _ { C , B } ^ { < 1 , 0 > }$ , note that $N _ { C , i } ^ { < 0 , 0 > } = N _ { i } ^ { < 0 , 0 > } , N _ { C , B } ^ { < 1 , 0 > } = N _ { B } ^ { < 1 , 0 > }$ , and $N _ { i } ^ { < 0 , 0 > } { < } N _ { B } ^ { < 1 , 0 > }$ as shown in (2) above.

D. Proof of Proposition 4 (Benefits of RSS Proposition). (1) The impact of first RSS adoption—from Case <0,0> to Case <1,0>. Consider the impact on the adopting website A. Let $\Delta \pi _ { A } = \pi _ { A } ^ { < 1 , 0 > } - \pi _ { \dot { \mathbb { A } } } ^ { < 1 , 0 > } , \Delta N _ { C , A } = N _ { C , A } ^ { < 1 , 0 > } - \dot { N _ { C , A } ^ { < 0 , 0 > } }$ and $\Delta \rho _ { A } =$ $\rho _ { A } ^ { < 1 , 0 > } - \rho _ { A } ^ { < 0 , 0 > }$ be the changes in the profit, number of conventional visitors, and effective traffic load of website A, respectively. Website A’s profit change can be written as $\Delta \pi _ { \boldsymbol { A } } = ( A + p _ { C } ) \cdot \Delta N _ { C , A } + N _ { R , A } ^ { < 1 , 0 > } \cdot p _ { R } - \Delta \boldsymbol { \rho } _ { \boldsymbol { A } } \cdot \boldsymbol { c } .$ As shown in Lemma 1, $\Delta N _ { C , A } < 0$ , and $\Delta \rho _ { A } > 0$ . Set $\Delta \pi _ { A } = 0 ,$ I get $\begin{array} { r } { p _ { R } = \frac { - \Delta N _ { C , A } \cdot ( A + p _ { C } ) + \Delta \rho _ { { A } } \cdot { c } } { N _ { R , { A } } ^ { < 1 , 0 > } } > 0 } \end{array}$ : Therefore, the quadratic function $\Delta \pi _ { A } ( p _ { C } ) = 0$ always has positive solutions. Further note that $\Delta \pi _ { A } ( p _ { R } = 0 ) < 0$ . There must be a positive solution ${ p _ { R } } ^ { 1 }$ such that (i) $\Delta \pi _ { A } \left( p _ { R } ^ { 1 } \right) = 0 ,$ (ii) $\forall p < p _ { R } ^ { 1 } , \Delta \pi _ { A } ( p ) < 0$ , and (iii) $\forall p > p _ { R } ^ { 1 } , \Delta \pi _ { A } ( p ) > 0$ . So, the profit of the adopting website (website A) will increase after first RSS adoption if and only i $\dot { \cdot } p _ { R } > { p _ { R } } ^ { 1 }$ , and will decrease afterward if and only if ${ p _ { R } } < { p _ { R } } ^ { 1 }$

Also consider the impact on the competing website B. Similarly, I have $\Delta N _ { C , B } =$ $N _ { C , B } ^ { < 1 , 0 > } - N _ { C , B } ^ { < 0 , 0 > } > 0$ and $\Delta \rho _ { B } = \rho _ { B } ^ { < 1 , 0 > } - \rho _ { B } ^ { < 0 , 0 > } > 0$ from Lemma 1, $\Delta \pi _ { B } = \pi _ { B } ^ { < 1 , 0 > } -$ $\pi _ { B } ^ { < 0 , 0 > } = ( A + p _ { C } ) \cdot \Delta N _ { C , B } - \Delta \rho _ { B } \cdot c$ Note that $\begin{array} { r l } { \Delta N _ { C , B } = \Delta N _ { B } } & { { } = \Delta \rho _ { B } , } \end{array}$ so $\Delta \pi _ { B } = ( A + p _ { C } - c ) \cdot \Delta \rho _ { B } > 0$ . Thus, the competing website’s profit always increases after the first RSS adoption.

(2) The impact of second RSS adoption—from Case <1,0> to Case <1,1>. Consider the impact on the adopting website B. Similarly, I define $\Delta N _ { C , B } =$ $N _ { C , B } ^ { < 1 , 1 > } - N _ { C , B } ^ { < 1 , 0 > } , \Delta N _ { R , B } = N _ { R , B } ^ { < 1 , 1 > } - N _ { R , B } ^ { < 1 , 0 > }$ and $\Delta \rho _ { B } = \rho _ { B } ^ { < 1 , 1 > } - \rho _ { B } ^ { < 1 , 0 > }$ . The profit change of website B can then be written as $\Delta \pi _ { B } = \pi _ { B } ^ { < 1 , 1 > } - \pi _ { B } ^ { < 1 , 0 > } = ( A + p c )$ $\Delta N _ { C , B } + \Delta N _ { R , B } \cdot p _ { R } - \Delta \rho _ { B } \cdot c$ Lemma 1 states that $\Delta N _ { C , B } < 0 , \Delta N _ { R , B } > 0$ , and $\Delta \rho _ { B } = 0$ . By setting $\Delta \pi _ { B } = 0$ , I get $\begin{array} { r } { p _ { R } = \frac { \Delta \mathbf { N } _ { C , B } \cdot ( A + p _ { C } ) } { \Delta \mathbf { N } _ { R , B } } \equiv P _ { R } ^ { 2 } > 0 } \end{array}$ Since $\rho _ { B } ^ { < 1 , 0 > } = \rho _ { B } ^ { < 1 , 1 > }$ , the decrease in the number of conventional visitors will just be equal to the increase in the number of RSS visitors multiplied by θ: $N _ { C , B } ^ { < 1 , 1 > } - N _ { C , B } ^ { < 1 , 0 > } = \Theta \cdot \Delta N _ { R , B }$ . So, $p _ { R } ^ { 2 } = \Theta ( A + p _ { C } )$ . As a result, profit of website B increases (decreases) after second RSS adoption if and only $\mathrm { i f } \ p _ { R } > { p _ { R } } ^ { 2 }$ $( p _ { R } < { p _ { R } } ^ { 2 } )$

Also consider the impact on the competing website A. Note that $\Delta \pi _ { A } = \pi _ { A } ^ { < 1 , 1 > } - \pi _ { A } ^ { < 1 , 0 > } = \Delta N _ { C , A } \cdot ( p _ { C } + A ) + \Delta N _ { R , A } \cdot p _ { R } - \Delta p _ { B } \cdot c ,$ and $\Delta N _ { C , A } > 0$ 2 $\Delta N _ { R , A } < 0 , p _ { A } = 0 . ~ \mathrm { A t } ~ p _ { R } ^ { 2 } = \Theta \cdot ( A + p _ { C } ) \colon \Delta \pi _ { A } = ( p _ { C } + A ) . \bigl ( \Delta N _ { C , A } + ~ \Delta N _ { R , A } \Theta \bigr )$ . In addition, $\Delta N _ { C , A } = - \Delta N _ { R , A } \theta$ . As a result, $\Delta \pi _ { A } \big ( P _ { R } ^ { 2 } \big ) = 0$ . To conclude, I find that profit of website A increases (decreases) after second RSS adoption if and only if $p _ { R }$ $< { p _ { R } } ^ { 2 } ( p _ { R } > { p _ { R } } ^ { 2 } )$

Finally, I still need to show ${ p _ { R } } ^ { 1 } < { p _ { R } } ^ { 2 } = { p _ { R } } ^ { * }$ , where ${ p _ { R } } ^ { * }$ is given by Proposition 2. Since ${ p _ { R } } ^ { 2 } = \theta \left( A + p _ { C } \right) = { p _ { R } } ^ { \ast }$ , it is obvious that these two values are the same. Next I prove ${ p _ { R } } ^ { 1 } < { p _ { R } } ^ { 2 }$ . One unit of traffic load can “carry” one conventional visitor or 1/θ RSS visitors. From Case <0,0> to Case $\mathrm { < } 1 , 0 \mathrm { > }$ , for website A, the decrease in the number of conventional visitors is $\Delta N _ { C , A } = N _ { C , A } ^ { < 1 , 0 > } - N _ { C , A } ^ { < 0 , 0 > } < 0 \ :$ . So if the traffic load remains unchanged, the increase in the number of RSS visitors should be $\frac { - \Delta \mathrm { N } _ { C , A } } { \theta }$ . However, the traffic load of website A in fact increases, and so the increase in the number of RSS visitors is $\begin{array} { r } { \Delta N _ { R , A } > - \frac { \Delta N _ { C , A } } { \theta } } \end{array}$ Denote it by $\begin{array} { r } { \Delta N _ { R , A } = - \frac { 1 } { \Theta } * \Delta \mathbf { N } _ { C , A } > - \frac { 1 } { \Theta } * \Delta \mathbf { N } _ { C , A } } \end{array}$ , where $0 < \Theta < \theta$ . Substituting it to the expression of $p _ { R } ^ { \mathrm { ~ 1 ~ } } , \mathrm { ~ I ~ }$ get $p _ { R } ^ { 1 } = \left( A + p _ { C } \right) \cdot \Theta + \left( \Theta - \Theta \right) \cdot c$ . Comparing it with $p _ { R } ^ { 2 } = \theta \cdot ( A + p _ { C } )$ , it is easy to see that ${ p _ { R } } ^ { 1 } < { p _ { R } } ^ { 2 }$

E. Proof of Proposition 5 (Sequential Equilibrium Proposition). When website A makes a decision before website B, I need to first analyze B’s best response given A’s action. If website A adopts, the best response of B is to adopt iff $\dot { p } _ { R } > { p _ { R } } ^ { 2 } ;$ and not to adopt $i f f p _ { R } < { p _ { R } } ^ { 2 }$ . If website A does not adopt, the best response of B is to adopt $i f f { p } _ { R } > { p } _ { R } { } ^ { 1 } ;$ ; and not to adopt $i f f p _ { R } < { p _ { R } } ^ { 1 }$

Next I analyze A’s decision, given B’s best response as stated above. Also note that ${ p _ { R } } ^ { 1 } < { p _ { R } } ^ { 2 }$ . When ${ p _ { R } } > { p _ { R } } ^ { 2 }$ , website B’s response is always to adopt. So website A needs to compare $\pi _ { A } ^ { < 0 , 1 > }$ (if it adopts) and $\bar { \pi } _ { A } ^ { < 1 , 1 > }$ (if it does not adopt). I have shown that $p _ { R } { > } p _ { R } { } ^ { 2 } \to \pi _ { A } ^ { < 1 , 1 > } { > } \pi _ { A } ^ { < 0 , 1 > }$ in Proposition 4. So website A will adopt. In this case, the sequential equilibrium will be <1,1>.

When ${ p _ { R } } < { p _ { R } } ^ { 1 }$ , website B’s response is always not to adopt. So website A needs to compare $\pi _ { A } ^ { < 0 , 1 > }$ (if it adopts) and $\pi _ { A } ^ { < 0 , 0 > }$ (if it does not adopt). I have shown that $p _ { R } { < } p _ { R } { } ^ { 1 } \to \pi _ { A } ^ { < 1 , 0 > } { < } \pi _ { A } ^ { < 0 , 0 > }$ in Proposition 4. So website A will not adopt. In this case, the sequential equilibrium will be $\mathrm { < 0 , 0 > }$

When $p _ { R } { } ^ { 1 } < p _ { R } { } < p _ { R } { } ^ { 2 }$ , website B’s response is to adopt if A does not adopt, and not to adopt if A adopts. So website A needs to compare $\overline { { \pi } } _ { A } ^ { < 1 , 0 > }$ (if it adopts) and $\pi _ { A } ^ { < 0 , 1 > }$ (if it does not adopt). I have shown that $p _ { R } { < } p _ { R } { } ^ { * } \to \pi _ { A } ^ { < 1 , 0 > } { < } \pi _ { A } ^ { < 0 , 1 > }$ in Proposition 2 and ${ p _ { R } } ^ { 2 } = p _ { R } { } ^ { * }$ in Proposition 4. So website A will not adopt. In this case, the sequential equilibrium will be $< 0 , 1 >$

F. Proof for Proposition 6 (Simultaneous Equilibrium Proposition). For ${ < } 0 , 0 { > }$ to be an equilibrium, each website must have no incentive to adopt RSS, given the competitor does not adopt, namely, $\pi _ { A } ^ { < 0 , 0 > } > \pi _ { A } ^ { < 1 , 0 > }$ and $\pi _ { B } ^ { < 0 , 0 > } > \bar { \pi _ { B } ^ { < 0 , 1 > } }$ . Due to the symmetry, I only need to prove $\pi _ { A } ^ { < 0 , 0 > } > \pi _ { A } ^ { < 1 , 0 > }$ . The proof of Proposition 4 has shown that $\pi _ { A } ^ { < 0 , 0 > } > \pi _ { A } ^ { < 1 , 0 > } \Leftrightarrow P _ { R } < P _ { R } ^ { 1 }$

For <1,1> to be an equilibrium, each website must have incentive to adopt RSS, given the competitor chooses to adopt, namely, $\pi _ { A } ^ { < 1 , 1 > } > \pi _ { A } ^ { < 0 , 1 > }$ and $\pi _ { B } ^ { < 1 , 1 > } > \pi _ { B } ^ { < 1 , 0 > }$ Similarly, I only need to prove $\pi _ { B } ^ { < 1 , 1 > } > \pi _ { B } ^ { < 1 , 0 > }$ . The proof of Proposition 4 has shown that $\pi _ { B } ^ { < 1 , 1 > } > \pi _ { B } ^ { < 1 , 0 > } \Leftrightarrow P _ { R } < P _ { R } ^ { 2 }$

For $^ { < 1 , 0 > }$ to be an equilibrium, website A must have incentive to adopt RSS, given B does not adopt, namely, $\pi _ { A } ^ { < 1 , 0 > } > \pi _ { A } ^ { < 0 , 0 > } ;$ ; and website B must have no incentive to adopt RSS, given A has adopted, namely, $\pi _ { B } ^ { < 1 , 0 > } > \pi _ { B } ^ { < 1 , 1 > }$ . The proof of Proposition 4 has shown that it means $P _ { R } ^ { 1 } < P _ { R } < P _ { R } ^ { 2 }$ . The same analysis and finding also apply to the equilibrium $^ { < 0 , 1 > }$

G. Proof of Proposition 7 (Benefits of RSS Proposition).Taking Case ${ \mathrm { < } } 0 { , } 0 { \mathrm { > } }$ as the benchmark, I need to prove that in outcomes $< 1 , 0 > , < 0 , 1 >$ and <1,1>, when they are equilibrium, both websites are better off. That is to say, I need to prove that in each of the above equilibriums, each website’s profit is greater than $\pi _ { i } ^ { < 0 , 0 > } , i = A$ or B.

Consider the outcome ${ \ < } 0 , 1 { > } .$ . It is an equilibrium when $p _ { R } { } ^ { 1 } < p _ { R } < p _ { R } { } ^ { 2 }$ , in both sequential and simultaneous games. For website A, it gets the profit ${ \pi _ { \it A } } ^ { < 0 , 1 > }$ , and Table 2 states that $\pi _ { A } ^ { < 0 , 1 > } > \pi _ { A } ^ { < 0 , 0 > }$ : as the competing website, A always becomes better off after first RSS adoption. For website B, it gets the profit ${ \pi _ { B } } ^ { < 0 , 1 > }$ , and Table 2 states that $\pi _ { B } ^ { < 0 , 1 > } > \pi _ { B } ^ { < 0 , 0 > }$ when $p _ { R } > { p _ { R } } ^ { 1 }$ : as the adopting website, B becomes better off after first RSS adoption only if $p _ { R } > { p _ { R } } ^ { 1 }$ . Thus, in this equilibrium, both websites benefit from the RSS technology. In addition, $\pi _ { A } ^ { < 0 , 1 > } > \pi _ { B } ^ { > < 0 , 1 > }$ because $p _ { R } < { p _ { R } } ^ { 2 } = { p _ { R } } ^ { * }$ —Proposition 2 suggests that the RSS nonadopter gains a higher profit than the adopter in the competition when ${ p _ { R } } < { p _ { R } } ^ { * }$

Next, consider the outcome $^ { < 1 , 0 > }$ . It is an equilibrium when $p _ { R } { } ^ { 1 } < p _ { R } < { p _ { R } } ^ { 2 }$ in the simultaneous game. The exact same analysis could be applied, and the same conclusion is reached: in this equilibrium, both websites gain higher profits than in the benchmark, and thus benefit from the RSS technology.

Finally, consider the equilibrium <1,1>. It holds when ${ p _ { R } } > { p _ { R } } ^ { 2 }$ in both sequential and simultaneous games. For website A, it gets the profit $\pi _ { A } { } ^ { < 1 , 1 > }$ , and $\pi _ { A } { } ^ { < 1 , 1 > } >$ $\pi _ { A } ^ { < 0 , 1 > } > \pi _ { A } ^ { < 0 , 0 > }$ . The first inequality holds because from Case $^ { < 0 , 1 > }$ to Case <1,1>, website A, as the adopting website, gets a higher profit after second RSS adoption when ${ p _ { R } } > { p _ { R } } ^ { 2 }$ (see Table 2); and the second inequality holds because from Case ${ \mathrm { < } } 0 { , } 0 { \mathrm { > } }$ to Case <0,1>, website A, as the competing website, gets a higher profit always after first RSS adoption (see Table 2). Since $\pi _ { A } ^ { < 1 , 1 > } = \pi _ { B } ^ { < 1 , 1 > }$ and $\pi _ { A } { } ^ { < 0 , 0 > } =$ ${ \pi _ { B } } ^ { < 0 , 0 > }$ , I also have $\pi _ { B } ^ { < 1 , 1 > } > \pi _ { B } ^ { < 0 , 0 > }$ . To conclude, in this equilibrium, both websites benefit from the RSS technology too.

## H. Lemma 2 and its proof

Lemma 2. When β is small, in both Case <1,0> and Case <1,1>, the marginal user who is aware of RSS, $x ^ { < 1 , 0 > }$ <sub>RSS-aware</sub> and $x ^ { < 1 , 1 > } { } _ { R S S - a w a r e } ,$ remain the same, but the marginal user who is unaware of RSS, $x ^ { < 1 , 0 > }$ <sub>RSS-unaware</sub> and $x ^ { < 1 , 1 > }$ <sub>RSS-unaware</sub>, become smaller.

Proof of Lemma 2. First consider Case <1,0>. The two traffic load Equations 6 and 7 still hold. Among users who are unaware of RSS, shown in Figure 2b, the marginal user $x ^ { < 1 , 0 > } { } _ { R S S - u n a w a r e }$ is given by Equation 5. Among users who are aware of RSS, shown in Figure 2a, the marginal user $x ^ { < 1 , 0 > } { } _ { R S S - a w a r e }$ is given by Equation 4 and ${ x ^ { < 1 , 0 > } } _ { R S S - a w a r e } = S + p _ { C } - p _ { R }$ . But Equation 9 is binding, suggesting that ${ N _ { R } } ^ { < 1 , 0 > }$ $\mathbf { \xi } = \beta \mathbf { \nabla } \cdot \mathbf { \boldsymbol { x } } ^ { < 1 , 0 > } \mathbf { \xi } _ { R S S - a w a r e }$ and that Equation 8 does not hold. It is easy to see that now $x ^ { < 1 , 0 > } { } _ { R S S - a w a r e } \neq x ^ { < 1 , 0 > }$ <sub>RSS-unaware</sub> anymore. Inserting Equation 4 and the binding boundary condition $N _ { R } { } ^ { < 1 , 0 > } = \beta \cdot x ^ { < 1 , 0 > } { } _ { R S S - a w a r e }$ into Equations 6 and 7, I get $( 1 - 2 r ) ( 1 - \beta ) x ^ { < 1 , 0 > } \kappa s s - u n a w a r e = ( 1 - 2 r ) a - \beta ( S + p _ { C } - p _ { R } ) ( 1 - 2 r + \theta )$ ; and inserting Equation 7 into Equation 5, I get $( 1 + w r ( 1 - \mathfrak { s } ) ) x ^ { < 1 , 0 > }$ RSS unaware $= - b + p _ { C } + S + w r a + w \beta ( S + p _ { C } - p _ { R } ) ( \theta - r )$ . These are two equations with <sup>¼  þ þ þ þ ð þ  Þð  Þ</sup>two unknowns (x<sup><1,0></sup><sub>RSS-unaware</sub> and r) and can be solved. The solution is: $\begin{array} { r } { r = \frac { \{ ( 1 - \beta ) ( b - p _ { C } - S ) + a \} - \beta ( S + p _ { C } - p _ { R } ) \{ w \theta ( 1 - \beta ) + 1 + 6 \} } { 2 \{ ( 1 - \beta ) ( b - p _ { C } - S ) + a \} - \beta ( S + p _ { C } - p _ { R } ) \{ w \theta ( 1 - \beta ) + 2 \} } } \end{array}$ . Plugging the solution of $r ,$ I obtain $x ^ { < 1 , 0 > } { } _ { R S S - u n a w a r e } .$ And the website’s profit can be obtained accordingly.

Now consider Case <1,1>. Using the same logic and using the binding boundary condition $N _ { R } ^ { < 1 , 1 \geq } \mathrm { ~ \boldsymbol { \beta } ~ } \cdot \mathrm { ~ \boldsymbol { \chi } ^ { < 1 , 1 > } ~ } _ { R S S - a w a r e } , \mathrm { ~ I ~ }$ get: $x ^ { < 1 , 1 > } { } _ { R S S - a w a r e } = S + p _ { C } - p _ { R }$ and $\begin{array} { r } { x _ { R S S - u n a w a r e } ^ { < 1 , 1 > } = \frac { - b + p _ { C } + S + w \left\{ a - ( \beta - \theta ) \left( S + p _ { C } - p _ { R } \right) \right\} } { 1 + w \left( 1 - \beta \right) } } \end{array}$ , and $x ^ { < 1 , 1 > } { } _ { R S S - a w a r e } \ \neq \ x ^ { < 1 , 1 > }$ <sub>RSS-unaware</sub>. And the expression for website’s profit can be obtained accordingly.

## NOTES

1. Many RSS readers and software applications are free—such as Feedly, NewsBlur, Digg, and The Old Reader—and numerous online manuals and video tutorials are available to assist users with setup, which usually takes only five to ten minutes.

2. Push describes “anything from broadcasting to selective content delivery using sophisticated evolutionary filtering agents” [20].

3. For example, NYTimes.com lists its free RSS feeds online (www.nytimes.com/services/ xml/rss/index.html). These feeds include news headlines, summaries, and links to the nytimes. com site for full articles.

4. For example, the New York Times reported that its RSS feeds generated 5.9 million page views in March 2005, which represented a 342 percent increase over the previous year and a 39 percent increase over the previous month [40]. And Yahoo! News reported that adding RSS feeds to My Yahoo! attracted 26 million additional visitors in one month.

5. Weekly RSS usage rate for the same period was roughly 4–7 percent, which actually shows a slightly decreasing trend. See blogs.forrester.com/reineke\_reitsma/13-03-15- the\_data\_digest\_usage\_of\_rss\_feeds.

6. This concept is similar to, though not exactly the same as what Stahl [38] proposed. He argued that users have different attitudes toward shopping. Some derive enjoyment purely from shopping itself, while others do not.

7. Advertising revenue support is critical to monetize websites [25]. In practice, multiple pricing models exist for online ads, such as charges per impression or by click-through rate. I assume that online ads lead to disutility for users. As long as this assumption holds, all analyses and results remain valid.

8. Most RSS software can block online ads. Although there has been debate about adding ads to RSS feeds, this is not common.

9. A common business model for websites is to sell some product, experience, content, or service and earn revenues from the sale [4], all of which are considered content-sales revenue in this work.

10. This research sets all else equal for the two competing websites but allows choice of content delivery method, so that the analysis could be focused on the impact of RSS adoption.

11. Otherwise, some users will switch from the higher traffic website to the lower traffic website until equivalence is reached.

12. The two websites have different numbers of visitors but the same amount of effective traffic. Otherwise, some conventional users will switch from the website with higher traffic load to the website with lower traffic load until equivalence is reached.

13. Otherwise, more users will use RSS feeds to visit website A until there is no positive utility left for RSS visits.

14. This situation will be analyzed separately later in the study.

15. If the nondegeneration condition does not hold, Case <1,0> and Case <1,1> are the same as Case <0,0>. No one will use RSS even if it is offered. If the critical awareness condition does not hold, the outcomes described in Propositions 2 and 3 are no longer valid. This will be analyzed separately later in the study. In addition, it is worthwhile to point out that the nondegeneration condition in Case <1,1> is more demanding than that in Case <1,0>, so I only need require that the nondegeneration condition in Case <1,1> hold. The two critical awareness conditions are the same in Case <1,0> and Case <1,1>.

16. In addition to RSS adoption, websites can use other strategies to further optimize profits, such as adjusting the prices of their online products and services, varying specific content coverage, or charging to subscribe to RSS feeds. These potential profit-improving strategies are not within the scope of this research; in this context, the only decision for a website is whether to adopt RSS. This lets me focus on the main research goal: how the RSS adoption decision affects a website’s profitability.

17. They are the same values as in the Sequential Equilibrium Proposition (Proposition 5).

18. This corresponds to the range of $p _ { R } \in \mathsf { \Gamma } [ p _ { R } ^ { \mathrm { ~ 1 ~ } } , p _ { R } ^ { \mathrm { ~ 2 ~ } } ]$

<sup>2</sup>19. In this example, the nondegeneration conditions require $p _ { R } \in [ 1 . 3 , 2 . 6 ]$ , and the two threshold values are ${ p _ { R } } ^ { 1 } = 1 . 6$ and ${ p _ { R } } ^ { 2 } = 2$

20. These sites prefer RSS for content distribution also because of their narrow information coverage and unstable update periods.

21. Most RSS ads now are just a few lines of text, differing in color from the headlines and summaries inside the RSS readers [28].

## REFERENCES

1. Bang, Y.; Lee, D.J.; Han, K.; Hwang, M.; and Ahn, J.H. Channel capabilities, product characteristics, and the impacts of mobile channel introduction. Journal of Management Information Systems, 30, 2 (Fall 2013), 101–125.

2. Blekas, A.; Garofalakis, J.; and Stefanis, V. Use of RSS feeds for content adaptation in mobile web browsing. Proceedings of the 2006 International Cross-Disciplinary Workshop on Web Accessibility (W4A): Building the Mobile Web, 134 (2006), 79–85.

3. Bustos, L. Google reader dying, but RSS lives on for ecommerce. www.getelastic.com/ google-reader-dying-but-rss-lives-on-for-ecommerce.

4. Clemons, E.K. Business models for monetizing Internet applications and web sites: Experience, theory, and predictions. Journal of Management Information Systems, 26, 2 (Fall 2009), 15–41.

5. Cohen, H. RSS and E-commerce: a natural fit. ClickZ Analytics Newsletter, February 2006. www.clickz.com/clickz/column/1709100/rss-e-commerce-a-natural-fit/.

6. Dewan, R.; Jing, B.; and Seidmann, A. Product customization and price competition on the Internet. Management Science, 49, 7 (August 2003), 1055–1070.

7. Dewan, R., and Freimer, M. Consumers prefer bundled add-ins. Journal of Management Information Systems, 20, 6 (Fall 2003), 99–111.

8. Dewan, R.; Freimer, M.; and Zhang, J. Management and valuation of advertisementsupported web sites. Journal of Management Information Systems, 19, 3 (Winter 2002–2003), 87–98.

9. Feedster.com Statistics. 2007. feedster.blogs.com/corporate/overview/index.html.

10. Foley, J. The weblog question. Information Week, 39, January 28, 2005. www.informa tionweek.com/ story/showArticle.jhtm?articleID=59100462&tid=5979/.

11. Garofalakis, J., and Stefanis, V. Using RSS feeds for effective mobile web browsing. Universal Access in the Information Society, 6, 3 (2007), 249–257.

12. Geng, X., and Lee, Y.J. Competing with piracy: A multichannel sequential search approach. Journal of Management Information Systems, 30, 2 (Fall 2013), 159–184.

13. Glotzbach R.J.; Mohler, J.L.; and Radwan, J.E. Syndicated RSS feeds for course information distribution. Journal of Information Technology Education, 7 (2008), 163–183.

14. Granados, N.F.; Kauffman, R.J.; Lai, H.; and Lin, H. Decommoditization, resonance marketing, and information technology: An empirical study of air travel services amid channel conflict. Journal of Management Information Systems, 28, 1 (Fall 2011), 39–74.

15. Guenther, K. The Web gets pushy. CIO Enterprise Section, 12, 7 (1999), 66–67.

16. Housley, S. Advertising in RSS feeds. www.feedforall.com/advertising-in-rss.htm (accessed October 2011).

17. Housley, S. Financial companies use RSS feeds. www.feedforall.com/finance-compa nies-use-rss.htm (accessed October 2012).

18. Hrastnik, R. Unleash the marketing and publishing power of RSS. RSS e-Book, 2005. rss.marketingstudies.net/book/t/.

19. Kapyla, T.; Niemi, I.; and Lehtola, A. Towards an accessible Web by applying PUSH technology. Proceedings of the Fourth ERCIM Workshop on User Interfaces for All, 15 (1998), 15–17.

20. Kendall J., and Kendall, K. Information delivery systems: An exploration of Web PULL and PUSH technologies. Communications of the AIS, 1 (1999), Article 14.

21. Kesmodel, D. E-commerce: Really simple sale? As RSS feeds catch on, advertisers are taking notice. Wall Street Journal, 2005. online.wsj.com/news/articles/ SB112975774167673601/ (October 24, 2005)

22. Kirkpatrick, M. The year in RSS. www.readwriteweb.com/archives/2007\_the\_year\_ in\_ rss.php.

23. Lee, B.K., and Lee, W.N. The effect of information overload on consumer choice quality in an on-line environment. Psychology and Marketing, 21, 3 (March 2004), 159–183.

24. Li, J., and Wu, W.G. RSS made easy: A basic guide for librarians. Medical Reference Services Quarterly, 26, 1 (Spring 2007), 27–35.

25. Lin, M.; Ke, X.; and Whinston, A.B. Vertical differentiation and a comparison of online advertising models. Journal of Management Information Systems, 29, 1 (Summer 2012), 195–236.

26. Hicks, M. Google puts RSS advertising to the test. eWEEK, April 2005. www.pcmag. com/article2/0,2817,1790047,00.asp.

27. Ma, D. Use of RSS feeds to push online content to users. Decision Support Systems, 54 (2012), 740–749.

28. Morrissey, B. RSS feeds becoming hot real estate for online Ads. ADWEEK Report, June 2005. www.adweek.com/news/advertising/rss-feeds-becoming-hot-real-estate-onlineads-79904/.

29. Ning, X.; Jin, H.; and Wu, H. RSS: A framework enabling ranked search on the semantic web. Information Processing and Management, 44 (2008), 893–909.

30. Parker, P. Lessons from the cutting edge: RSS advertising. ClickZ, May 2005. www. clickz.com/clickz/column/1700739/lessons-cutting-edge-rss-advertising/.

31. Quentin, J.; Gilad, R.; and Sheizaf, R. Information overload and the message dynamics of online interaction spaces: A theoretical model and empirical exploration. Information Systems Research, 15, 2 (2004), 194–210.

32. Rajan, B.; Seidmann, A.; and Dorsey, E.R. The competitive business impact of using telemedicine for the treatment of patients with chronic conditions. Journal of Management Information Systems, 30, 2 (Fall 2013), 127–157.

33. Reitsma, R. The data digest: Usage of RSS feeds. Forrester, March 2013. blogs. forrester. com/reineke\_reitsma/13-03-15-the\_data\_digest\_usage\_of\_rss\_feeds/.

34. Ruebeck, C.S. Model exit in a vertically differentiated market: Interfirm competition versus intrafirm cannibalization in the computer hard disk drive industry. Review of Industrial Organization, 26, 1 (February 2005), 27–59.

35. Saucers, M.P. Blogging and RSS. 2nd ed. Medford, New Jersey: Information Today, 2010.

36. Scoble, R. Why haven’t RSS readers gain mass adoption? www.quora.com/Whyhavent-RSS-readers-gained-mass-adoption (accessed November 2012).

37. Shaked, A., and Sutton, J. Multiproduct firms and market structure. RAND Journal of Economics, 21, (1990), 45–62.

38. Stahl, D.O. Oligopolistic pricing with sequential consumer search. American Economic Review, 79, 4 (1989), 700–712.

39. Steinfield, C.; Markus, M.L.; and Wigand, R.T. Through a glass clearly: Standards, architecture, and process transparency in global supply chains. Journal of Management Information Systems, 28, 1 (Fall 2011), 75–108.

40. The New York Times Company reports NYTimes.com’s record-breaking traffic. New York Times Company News Release, April 2006. www.thefreelibrary.com/The+New+York+ Times+ Company+Reports+NYTimes.com’s+Record-Breaking...-a0131620245/.

41. VanBoskirk, S. Organize to support integrated messaging. Forrester Report, 2014. www.forrester.com/Email-marketing-%26-RSS/.

42. Xu, L; Chen, J.; and Whinston, A.B. Oligopolistic pricing with online search. Journal of Management Information Systems, 27, 3 (Winter 2011), 111–142.
