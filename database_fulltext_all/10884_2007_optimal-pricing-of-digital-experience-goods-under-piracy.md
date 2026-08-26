---
otero_id: 10884
otero_key: "HR4ZTHER"
title: "Optimal Pricing of Digital Experience Goods Under Piracy"
authors: "Moutaz Khouja; Sungjune Park"
year: "2007"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222240304"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [University of Otago] On: 27 July 2015, At: 17:59 Publisher: Routledge Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: 5 Howick Place, London, SW1P 1WG

![](/api/attachments/HR4ZTHER/fulltext/images/b01bb9d63718284949d1be636a3bd7740fdaddf8a0e177fdbeb15c56862bbbf8.jpg)

# Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# Optimal Pricing of Digital Experience Goods Under Piracy

Moutaz Khouja <sup>a</sup> & Sungjune Park <sup>b</sup>

<sup>a</sup> The Department of Business Information Systems and Operations Management, The University of North Carolina, Charlotte

<sup>b</sup> The Business Information Systems and Operations Management Department, The University of North Carolina, Charlotte Published online: 08 Dec 2014.

To cite this article: Moutaz Khouja & Sungjune Park (2007) Optimal Pricing of Digital Experience Goods Under Piracy, Journal of Management Information Systems, 24:3, 109-141

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222240304

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

# Optimal Pricing of Digital Experience Goods Under Piracy

MOUTAZ KHOUJA AND SUNGJUNE PARK

MOUTAZ KHOUJA is a Professor in the Department of Business Information Systems and Operations Management at the University of North Carolina at Charlotte. He received a B.S. in Mechanical Engineering, an MBA from the University of Toledo, and a Ph.D. in Operations Management from Kent State University. His research interests are in the areas of inventory management, production planning and control, pricing, forecasting, and agent-based modeling. His publications have appeared in many leading journals, including Computers and Operations Research, Decision Sciences, IIE Transactions, European Journal of Operational Research, International Journal of Production Research, International Journal of Production Economics, Journal of the Operational Research Society, and Omega.

SUNGJUNE PARK is an Assistant Professor in the Business Information Systems and Operations Management Department at the University of North Carolina at Charlotte. He received his B.S and M.S. in Management Science from Korea Advanced Institute of Science and Technology, and Ph.D. in Business Administration from the State University of New York at Buffalo. His research areas include neural networks applications in business, information security, digital piracy, and supply chain management. His research has appeared in International Journal of Production Research and OMEGA.

ABSTRACT: Piracy of digital experience goods such as music recordings has received increased attention in the literature. Much of this research has focused on pricing policies, protection against piracy, and governmental policies in the software industry. In this research, we focus on pricing policies of producers of digital experience goods. We consider a heterogeneous consumer market with different segments, each having a different affinity to piracy. We analyze the effect of different producer pricing policies on the revenue of the creator of the product, who may be different than the producer. Our results indicate that the explicit incorporation of these different consumer segments will cause the producer to charge lower prices and, therefore, lead to higher legal product diffusion. We show that the royalty system does not solve the double marginalization problem and is suboptimal from a supply-chain perspective. Also, the creator of the goods prefers a lower price than the producer’s optimal price, and this tendency increases with the creator’s per unit royalty.

KEY WORDS AND PHRASES: digital experience goods, information goods piracy, music and movie piracy, online piracy, pricing, social welfare.

PIRACY OF INFORMATION GOODS IS A MAJOR PROBLEM facing firms in the software, recorded music, and motion picture industries. Past research has focused on software piracy.

However, losses in the recorded music and motion picture industries due to piracy have grown considerably in the past several years. From an economic viewpoint, tolerating some piracy has been shown to have some positive aspects in that piracy makes a product available to those who cannot afford it, increases the consumer base for a product, and creates positive network externalities [12, 15, 27, 32, 43]. Network externality for a product exists if a consumer’s willingness to pay for the product is influenced by the number of its users [25]. Among other information goods, computer software has been the main focus of network externalities. These positive aspects of product diffusion are less obvious and may work differently in the recorded music and motion picture industries. Nonetheless, music and movies may also exhibit such positive network effect. For example, if an artist becomes popular, through legitimate sales or piracy, then he or she can charge higher prices for concert tickets and higher pay rates for product advertising. Similarly, if a movie has high circulation, then more money can be charged for product advertising that is bundled with it [25].

Industries susceptible to piracy are usually dominated by monopolists who obtain monopoly power through copyright management and protection. Like other monopolies, they are viewed unfavorably because they tend to charge higher prices than would prevail under competition. For example, while Napster was being shut down following accusations that it contributed to piracy, the major record labels such as Warner, Sony, and EMI were also being accused of having violated fair trade practices by threatening retailers not to advertise CDs below certain prices [4].

Among industries suffering from piracy, the recorded music industry is at the forefront. Pirating music has become much easier due to its digitization; the affordability of CD/DVD recorders, which enables consumers to burn their own copies; the adoption of compression technologies such as MP3; and easy access to digitized music files and peer-to-peer (P2P) networks. The Recording Industry Association of America’s (RIAA) 2006 year-end statistics show that sales of CDs have declined since 2001. In 2003, the U.S. sales of music CDs were \$11.2 billion compared to a peak of \$13.2 billion in 2000. This figure increased slightly in 2004 to \$11.4 billion and declined again to \$10.50 billion in 2005 and \$9.2 billion in 2006 [36]. U.S. sales of digital single songs increased from \$138 million in 2004 to \$363 million in 2005 and \$581 million in 2006 [36]. U.S. sales of digital full albums increased from \$45 million in 2004 to \$236 million in 2005 and to \$276 million in 2006 [36]. The decline in CD sales coincides with the development of compression and file-sharing technologies and the declining cost of CD/DVD recorders. Also, since the launch of Napster in 1999, the sales of singles (on CD, cassette, and vinyl) have been decreasing at a remarkable rate with annual sales, in millions, of \$298, \$174, \$106, \$43, \$57, \$35, \$24, and \$15 from 1999 through 2006 [36]. This is in part due to the fact that compressing one song into an MP3 file makes it easy to swap music files. Although Napster, once a popular music swapping site, was shut down in an effort to prevent piracy, alternative file sharing through P2P networks, such as Kazaa, WinMX, and Gnutella, immediately replaced Napster. P2P networks do not require a central server to store files. In 2003, another attempt to reduce piracy was made by the record labels by bringing lawsuits against individual file sharers, and it seems to be working. A survey conducted in 2004 by the Pew Internet & American Life project shows that 14 percent of once music downloaders no longer download, and 38 percent download less because of the RIAA legal campaign [35]. However, a survey by the same group conducted in March 2005 indicates that there has been a slight increase in downloading again [26]. The survey indicates that 36 million Americans downloaded music without authorization and another 10 million got music and video files using e-mail and instant messages.

The effect of online movie piracy is starting to reach levels comparable to those faced by the music industry. The Motion Picture Association of America claims the film industry lost \$3.5 billion in 2004 because of piracy, although this figure does not include losses due to file sharing. In 2007, Viacom filed a lawsuit against Google because of allegedly intentional copyright infringement after Google’s purchase of YouTube [37]. According to the article, Viacom is asking the U.S. District Court to award \$1 billion in damages and an injunction to prevent Google from sharing unauthorized video clips on YouTube.

This paper focuses on piracy of music and motion pictures. The objectives of this paper are (1) to derive the optimal monopolist price in a market where piracy is unavoidable, and (2) to investigate the impact of piracy on different stakeholders— consumers, monopolists, and creators. Our focus is on the music and motion picture industries where the classic network externality that is important for some software products may not exist. The key analytical results show that

• the optimal price of a monopolist who incorporates piracy into the pricing decision is always lower than or equal to the price assuming homogeneous ethical consumers;

• the creator always prefers a lower price than the optimal price set by the monopolist, unless the variable unit cost is zero;

• the creator’s preference for a lower price than the producer’s optimal price increases with the per unit royalty that is proportional to the price paid by consum ers;

• the royalty system does not solve the double marginalization problem and is suboptimal from a supply-chain perspective;

• an online distribution channel that decreases the variable cost per unit will bring the optimal prices of the monopolist and creator closer together and will reduce channel conflict;

• lower prices should be used by the monopolist when the level of piracy is high or when the variable unit cost is small; and

• investments in controlling piracy may not always be beneficial to the monopolist and creator, especially when there are many nonpirating consumers or they are price insensitive.

## Literature Review

strategies, and government policies. Nascimento and Vanhonacker [27] found that skimming pricing strategies are optimal in the absence of piracy. Using a diffusion of innovation model, they found that copy protection is recommended only when sales grow faster than piracy and the cost of protection does not significantly increase the marginal cost. Later, Givon et al. [15] showed a positive side to piracy with a software diffusion model. Conner and Rumelt [12] examined protection strategies in the presence of positive network externalities. Their analysis indicates that, in the presence of positive network externalities, “no protection strategy” can result in a lower price and increased profit. Prasad and Mahajan [32] examined the relationship between the rate of software diffusion and piracy to determine price and the level of piracy that should be tolerated. The authors examined three different cases: a monopoly, a monopoly with multiple generations of software, and a competitive market. Haruvy et al. [19] examined how piracy affects the adoption of subscription software. The authors developed a model in which the producer determines the price and the protection level that maximize the discounted profit stream over the life of the product. Their results indicate that moderate tolerance for piracy can speed up adoption and enables the producer to charge higher prices. The tolerance for piracy decreases when market penetration is quick, information is precise, and positive network externalities are low.

Sundararajan [41] analyzed optimal pricing and technological protection for a monopolist using price discrimination among consumers who are willing to buy variable quantities of a digital good. The author shows that the optimal pricing schedule can be characterized as a combination of a zero-piracy pricing schedule and a piracy-indifferent pricing schedule. In the latter case, consumers are indifferent regarding legal and pirated products. Other findings by network externality–based studies [12, 39, 43] also indicate that allowing piracy can make the producer more profitable.

Chen and Png [8] developed a model that incorporates a penalty for piracy set by the government. The monopolist determines price and piracy monitoring rate. Users may buy the product, pirate it at the risk of enforcement action, or not use the product. The authors show that changes in pricing and monitoring rates have qualitatively different effects on consumers and that from a social welfare perspective, reductions in price are better than increases in monitoring. Chen and Png [9] extended their earlier model to include a tax on copying media and equipment and a government subsidy for legitimate purchases. Consumers are segmented into ethical and unethical groups. Their results indicate that taxing the copying media is better from a social welfare standpoint than imposing a penalty for piracy, and that the best government policy is to subsidize legitimate purchases. Belleflamme [2] considered a case in which copies are of lower quality than originals. The author shows that, although diffusion through piracy increases social welfare, this comes at the expense of the producer’s profits, which may then be insufficient to cover the fixed cost of creation. Thus, if copies are not a low-quality alternative to originals, then piracy is likely to damage welfare in the long run.

An interesting finding by Gopal and Sanders [16] is that deterrent controls, which employ educational and legal campaigns, protect profit better than preventive controls, which use technology to prevent piracy. Also, deterrent controls were shown to be superior from a social welfare perspective. Maximizing social welfare through government policy has been the subject of considerable research [1, 9].

Another important aspect of the music and software industries is the change in distribution channels. Historically, the distribution of music recordings was through brick-and-mortar retail chains. However, recent emergence of legal downloading sites serving as digital online distribution channels such as iTunes is leading to profound changes in the cost structure of the industry. In March 2004, more than 11 million U.S. Internet users visited online music services [35]. A survey conducted by the International Federation of the Phonographic Industry [29] shows that the total recorded music sales increased by 30 percent by 2002 since the introduction of MP3 in 1997, although sales of music CDs and cassette tapes declined. Online music distribution is not limited to the familiar classic client-server model. P2P networks can also be used to distribute digital content over computer networks. Lang and Vragov [23] propose a pricing mechanism for digital content distributed using P2P networks. Even though client-server distribution gives providers control of content supply and promotion, it is limited in capacity and consumer participation in generating additional interest in the product. To overcome these limitations, Lang and Vragov suggest using P2P networks to have the interactive network design serving as a marketing tool and to use the additional storage capacity and bandwidth of P2P networks. The provider in their model has two base prices, a price charged per byte of downloaded files and a price paid per byte of each uploaded file. The authors develop a pricing scheme that results in higher profits and faster content distribution than the client-server mode. Although both distribution modes are susceptible to piracy, P2P may offer some pricing flexibilities that can be used to combat piracy.

Online distribution of digital content is one technological trend that facilitates piracy but may also lead to changes in industry structure and to a decrease in the per unit price. This, in turn, may remove one of the motives for piracy [10]. These changes are most apparent in the music recording industry. As described by Clemons et al. [11], the forces that made “stars” in the music industry captive to record labels, in spite of receiving only 10–15 percent of unit price in royalties, are weakening. Improvements in production technology of music records and the availability of new distribution channels through the Internet are enabling many “stars” to produce and market their own records. Popular singers/groups no longer have to cross-subsidize less profitable ones in the same label’s portfolio. This reduction in the size of the value chain may lead to lower prices and smaller incentives to pirate. Furthermore, it may increase the perceived harm consumers believe they are inflicting on artists, which also leads to less piracy [28].

Another research strand that deals with pricing products that can be shared [30], rented [46], resold [24, 42], or copied has been developed in economics. The major thesis in this research is that the ability to copy, share, rent, or resell a product affects profitability because legitimate copies have higher value to users because they can be rented, copied, shared, or resold. While this allows producers to charge higher prices, the quantity sold will be smaller due to erosion of demand caused by sharing, rentals, or copying. Varian [46] identifies some conditions under which profits increase because of sharing, renting, or copying. These conditions depend largely on the relative value of the marginal cost of production and the transaction cost of sharing.

Price discrimination is one way a monopolist can increase profit under piracy [3, 18, 22, 46]. In particular, versioning of information goods, where a firm offers the same product in different versions targeted to different consumer segments, is a strategy used by some firms [38]. However, copying music, software, and movies without losing quality is becoming easier than ever as high-speed Internet services are becoming popular [20]. Therefore, versioning a product based on quality is difficult and appropriate pricing and piracy controls are the choices left for the producer to increase profit.

Although price discrimination by quality may not work in the music industry, differential pricing for different music categories [3] or for different market segments [18] may be effective because there are significant piracy differences based on consumer demographics. Surveys on piracy [3, 26] indicate that piracy rates are higher for males and for younger consumers.

A unique aspect of the music and motion picture industries is the royalty system. Record labels usually pay royalties to artists ranging from 10 percent to 15 percent of price or a fixed amount per unit sold [11, 33]. Artists/creators were once considered victims of piracy. A report from Pew Internet & American Life Project reveals, however, that creators do not feel that digital file sharing hurts them [34]. Moreover, only 20 percent of musicians surveyed agreed that RIAA’s legal action against downloaders will benefit them. To our knowledge, there is no research on the impact of piracy on a creator’s revenue.

## Optimal Pricing Under Piracy

PIRACY BEHAVIOR IS FREQUENTLY ANALYZED AS PART of ethical decision making. For a detailed review on consumer ethics research, readers are referred to Vitell [47]. In one particular study, Fullerton et al. [14] calculated a consumer ethics index for 362 consumers. Fullerton et al. identified four consumer groups: (1) permissives, which is a consumer group with tolerant attitudes; (2) situationalists, which is a consumer group that has a slight disdain for ethical breaches; (3) conformists, which is a consumer group who believe that a responsible conduct should be the norm, but this belief is not absolute; and (4) puritans, which is a consumer group whose members live by a strict standard of conduct.

In another study, Thong and Yap [44] tested the ethical decision-making theory of Hunt and Vitell [21] in the context of software piracy. In this model, an individual facing the question of whether to pirate or not can be ethically insensitive and does not perceive the situation to have an ethical dimension. If the individual is ethically sensitive, then he or she performs a deontological and a teleological evaluation of the possible alternatives. The deontological evaluation assesses the rightness or wrongness of behavior of each alternative relative to established deontological norms. The teleological evaluation assesses the perceived consequence of each alternative and the probability of its occurrence. The deontological and teleological evaluations are used by individuals in reaching an ethical judgment and in turn a behavior. The results indicate that this theory is applicable to explaining ethical decision making in software piracy.

Based on the above discussion, we divide consumers into three segments—ethical, indifferent, and pirating. The conformists and situationalists of Fullerton et al.’s study [14] make up our indifferent segment, whereas the permissives and puritans make up the pirating and ethical segments, respectively. From the ethical decision-making theory perspective [44], the wrongness of piracy behavior makes ethical consumers not pirate at all. For the indifferent segment, a pirated copy, albeit a functionally perfect or close to perfect substitute for the original, cannot be a fully perfect substitute due to the wrongness of piracy. This is because these consumers suffer an internal cost when they perform an illegal activity such as piracy [40]. This internal cost was referred to as the moral cost of pirating by Chellappa and Shivendu [6, 7]. For the pirating segment, consumers do not view piracy as wrong and their evaluation depends on the teleological evaluation of consequences and their probabilities.

Each consumer has a valuation for the legitimate product, $u _ { j } ,$ which is uniformly distributed on $[ 0 , U ]$ . Ethical segment consumers never pirate. A consumer in the ethical segment will purchase the product if his or her valuation for the product is larger than price, $u _ { \ i } > P$ . Therefore, the probability that consumer j in the ethical segment will purchase the product is

$$
\int_ {P} ^ {U} \frac {1}{U} d u = 1 - \frac {P}{U},
$$

which results in a linear downward-sloping demand function with a slope of $1 / U .$ Demand for this segment becomes zero at a price of U. Indifferent segment consumers view a pirated copy as an imperfect substitute for a legitimate product. Therefore, if a consumer has a valuation $u _ { { } _ { j } }$ for the legitimate product, then his or her valuation for the pirated copy is $u _ { \ i } - \ q .$ , where $q$ is the penalty for the wrongness of piracy [44]. Each consumer in the indifferent segment has an expected copying and penalty cost, $\tau _ { j }$ , which is uniformly distributed on $[ 0 , T _ { I } ]$ , where $q + T _ { \scriptscriptstyle { I } } < U .$ Indifferent consumer j will purchase a legitimate product if (1) $u _ { \ i } > P$ and (2) the expected gain from purchasing a legitimate product is larger than the expected gain from pirating—that is, $u _ { j } - P > u _ { j } - q - \tau _ { j } .$ . Therefore, the probability that indifferent consumer j will purchase a legitimate product is

$$
\int_ {P} ^ {U} \frac {1}{U} d u \int_ {P - q} ^ {T _ {I}} \frac {1}{T _ {I}} d \tau = \frac {1}{T _ {I} U} (q + T _ {I} - P) (U - P),
$$

which results in a nonlinear downward-sloping demand function that becomes zero at a price of $q + T _ { \ I } < U .$ The above assumption about indifferent segment consumer behavior is equivalent to assuming that their cost of piracy is uniformly distributed on $[ q , q + T _ { I } ]$ , which is similar to assumptions in other models [7]. $\mathrm { I f } q + T _ { I }$ is significantly smaller than $U ,$ then the demand function of this segment can be approximated by a linear demand with slope of $1 / ( q + T _ { r } )$ . In cases when $q + T _ { \scriptscriptstyle I }$ is close to $U ,$ a better linear fit may be obtained using regression analysis.

Pirating segment consumers view pirated copies as a perfect substitute for a legitimate product. Each consumer in the pirating segment has an expected copying and penalty cost, $\tau _ { j } ,$ which is uniformly distributed on $[ 0 , T _ { P } ]$ , where $T _ { \scriptscriptstyle P } < T _ { \scriptscriptstyle I }$ . Pirating consumer j will purchase a legitimate product if $u _ { \ i } > P$ and $u _ { j } - P > u _ { j } - \tau _ { j }$ . Therefore, the probability that pirating consumer j will purchase a legitimate product is

$$
\int_ {P} ^ {U} \frac {1}{U} d u \int_ {P} ^ {T _ {P}} \frac {1}{T _ {P}} d \tau = \frac {1}{T _ {P} U} (T _ {P} - P) (U - P),
$$

which results in a nonlinear downward sloping demand function that becomes zero at a price of $T _ { _ { P } } { < } T _ { _ { I } } { . } \mathrm { I f } T _ { _ { P } }$ is significantly smaller than U, then the demand function of this segment can be approximated by a linear demand with slope of $1 / T _ { P } .$ In cases when $T _ { \scriptscriptstyle P }$ is close to $U ,$ a better linear fit may be obtained using regression analysis. The above analysis indicates that demand of the pirating segment vanishes first at a price of $T _ { { \scriptscriptstyle P } } ,$ followed by the demand of the indifferent segment, which vanishes at price of $q + T _ { r }$ and last the demand of the ethical segment, which vanishes at a price of $U .$

Similar market segmentation was used by Chen and Png [9] in a model that classifies consumers as either unethical or ethical. The choice of three segments is realistic and illustrative. Our analysis applies to more or fewer segments. The relative sizes of the segments will depend on the target market of the product. Products targeted to older consumers or females will likely have a larger proportion of consumers in the ethical segment relative to products targeted to young males [3]. We also assume that the relative distribution of consumers among the three segments is stable over the life of the product. This assumption may not be valid if there is a period of extensive piracy litigation or new piracy prevention technology that may increase the expected cost of piracy. This may cause a change in the slopes of the demand functions of the pirating and indifferent segments.

## The Monopolist’s Problem

We assume that prices are controlled by a profit-maximizing monopolist. The following notation is used:

i = 1, 2, or 3, where 1 denotes the ethical segment, 2 denotes the indifferent segment, and 3 denotes the pirating segment;

F = the fixed cost of product development and marketing;

v = the variable per unit cost of the product;

$D _ { _ i }$ = the quantity demanded by market segment i, a decreasing function of price;

$P _ { _ i }$ = the per unit retail price at which the demand of segment i becomes zero;

$a _ { _ i }$ = the demand of segment i when unit price is zero;

$b _ { _ i }$ = the decrease in demand of segment i due to a \$1 increase in unit price, $b _ { _ i } >$ 0; and

r = fraction of unit price paid to the creator(s) in royalty for each unit sold.

Based on the above analysis of consumer purchase probability, demand for each segment is linearly decreasing in price and is given by

$$
D _ {i} = a _ {i} - b _ {i} P \qquad 0 \leq P \leq \frac {a _ {i}}{b _ {i}}.\tag{1}
$$

The demand for segment i becomes zero at price:

$$
P _ {i} = \frac {a _ {i}}{b _ {i}} \quad i = 1, 2, 3\tag{2}
$$

and

$$
P _ {1} > P _ {2} > P _ {3} \quad \left(\text { i.e., } \frac {a _ {1}}{b _ {1}} > \frac {a _ {2}}{b _ {2}} > \frac {a _ {3}}{b _ {3}}\right),\tag{3}
$$

which implies that as price increases, the demand of the pirating segment vanishes first, followed by the demand of the indifferent segment, and last the demand of the ethical segment.

The total demand $D = \Sigma _ { i = 1 } ^ { 3 } D _ { _ i }$ is a piecewise linear function of price with three price regions $R _ { _ 1 } = ( P _ { _ 2 } , P _ { _ 1 } ] , R _ { _ 2 } = ( P _ { _ 3 } , P _ { _ 2 } ]$ , and $R _ { 3 } = [ 0 , P _ { 3 } ]$ , and is given by

$$
D = \left\{ \begin{array}{l l} \left(a _ {1} + a _ {2} + a _ {3}\right) - \left(b _ {1} + b _ {2} + b _ {3}\right) P & \text { if } P \in R _ {3} \\ \left(a _ {1} + a _ {2}\right) - \left(b _ {1} + b _ {2}\right) P & \text { if } P \in R _ {2} \\ a _ {1} - b _ {1} P & \text { if } P \in R _ {1}. \end{array} \right.\tag{4}
$$

The demand is only from ethical consumers if $P \in R _ { \ast }$ , ethical and indifferent consumers if $P \in R _ { 2 } ,$ , and all consumers if $P \in R _ { 3 } . \mathrm { A }$ graph of each segment’s demand and aggregate demand are shown in Figure 1.

The total profit of the monopolist is total revenue minus total cost, which is made up of the royalty paid to the creator, the variable cost, and the fixed cost. The profit function is

$$
\pi = (P - v - r P) D - F.\tag{5}
$$

Using Equation (4), π can be written as

$$
\pi = \left\{ \begin{array}{l l} \pi_ {3} = \Big [ \big (a _ {1} + a _ {2} + a _ {3} \big) - \big (b _ {1} + b _ {2} + b _ {3} \big) P \Big ] (P - v - r P) - F & \text { if } P \in R _ {3} \\ \pi_ {2} = \Big [ \big (a _ {1} + a _ {2} \big) - \big (b _ {1} + b _ {2} \big) P \Big ] (P - v - r P) - F & \text { if } P \in R _ {2} \\ \pi_ {1} = \big (a _ {1} - b _ {1} P \big) (P - v - r P) - F & \text { if } P \in R _ {1}. \end{array} \right.\tag{6}
$$

![](/api/attachments/HR4ZTHER/fulltext/images/a821cf8195a224197b12a1cd2d40a83651a4ae8b4e84a72aa5ce0276fde67350.jpg)  
a. Demand for Each Consumer Segment

![](/api/attachments/HR4ZTHER/fulltext/images/161572a063d4b56b35ba33b79b7465e497539552533a564cf6111255ec8d3694.jpg)  
b. Aggregate Demand Function  
Figure 1. Demand Function

An example of the profit function is shown in Figure 2. The function consists of three concave parabolas. The vertex of each parabola $\pi _ { _ i }$ may be in $R _ { _ i }$ making it a local optimum, or it may not. However, if $\nu / ( 1 - r ) < a _ { _ { 1 } } / b$ (which implies that there is a positive price for which demand is positive and the monopolist can cover the variable cost and the royalty), then Theorem 1 shows that at least one $\pi _ { _ i }$ has its maximum in a valid region. Let $\mathbf { \boldsymbol { a } } _ { j } = \Sigma _ { i = 1 } ^ { j } \boldsymbol { a } _ { i }$ and $\beta _ { j } = \Sigma _ { i = 1 } ^ { j } b _ { i }$ , which implies

$$
\alpha_ {3} = a _ {1} + a _ {2} + a _ {3} \text { and } \beta_ {3} = b _ {1} + b _ {2} + b _ {3}
$$

$$
\alpha_ {2} = a _ {1} + a _ {2} \text { and } \beta_ {2} = b _ {1} + b _ {2}
$$

and

$$
\alpha_ {1} = a _ {1} \text {   and   } \beta_ {1} = b _ {1}.
$$

![](/api/attachments/HR4ZTHER/fulltext/images/54b4327768d2d77e0f9c5642845896fdda3c5cae54d408096ad2d7410e3951d8.jpg)  
Figure 2. The Monopolist’s Profit Function

Further analysis shows that each $\pi _ { _ i }$ in Equation (6) has an unrestricted maximum of

$$
\pi_ {M i} ^ {*} = \frac {\left[ \alpha_ {i} (1 - r) - \beta_ {i} v \right] ^ {2}}{4 \beta_ {i} (1 - r)} - F \quad i = 1, 2, 3\tag{7}
$$

at price

$$
P _ {M i} ^ {*} = \frac {\alpha_ {i}}{2 \beta_ {i}} + \frac {\nu}{2 (1 - r)} \quad i = 1, 2, 3,\tag{8}
$$

which may or may not be in the valid portion of $\pi _ { _ i \cdot }$ We develop two properties of the demand function parameters that follow from the assumption in inequality (3). The properties are stated in Lemmas 1 and 2 in the Appendix. By Lemma 2 and Equation (8), the prices that maximize $\pi _ { 1 } , \pi _ { 2 }$ , and $\pi _ { _ 3 }$ satisfy $P _ { { } _ { M 1 } } ^ { * } > P _ { { } _ { M 2 } } ^ { * } > P _ { { } _ { M 3 } } ^ { * }$ . This result is used to prove Theorem 1, which implies that it is not possible to have local maximum at any $P _ { \mathrm { { \scriptsize ~ i } } } ( i = 1 , 2 , 3 )$ (the points where the slope changes in the demand function).

Theorem 1: $H f \nu / ( l - r ) < a _ { \prime } / b _ { \prime }$ , then the profit maximizing price of the monopolist has the form

$$
P _ {M} ^ {*} = \frac {\alpha_ {i}}{2 \beta_ {i}} + \frac {v}{2 (1 - r)} \quad i = 1, 2, \text {   or   } 3.\tag{9}
$$

Proof: See the Appendix.

The royalty paid to the creator is given by

$$
\rho = D r P.\tag{10}
$$

The creator also obtains revenue from other sources which we do not include in Equation (10), such as live performances, TV performances, advertising, merchandise, and so on. Using Equation (4), ρ can be written as

$$
\rho = \left\{ \begin{array}{l l} \rho_ {3} = \left[ \left(a _ {1} + a _ {2} + a _ {3}\right) - \left(b _ {1} + b _ {2} + b _ {3}\right) P \right] r P & \text { if } P \in R _ {3} \\ \rho_ {2} = \left[ \left(a _ {1} + a _ {2}\right) - \left(b _ {1} + b _ {2}\right) P \right] r P & \text { if } P \in R _ {2} \\ \rho_ {1} = \left(a _ {1} - b _ {1} P\right) r P & \text { if } P \in R _ {1}. \end{array} \right.\tag{11}
$$

Further analysis shows that each $\boldsymbol { \rho } _ { i }$ in Equation (11) has an unrestricted maximum of

$$
\rho_ {O i} ^ {*} = \frac {r \alpha_ {i} ^ {2}}{4 \beta_ {i}} \quad i = 1, 2, 3\tag{12}
$$

at price

$$
P _ {O i} ^ {*} = \frac {\alpha_ {i}}{2 \beta_ {i}} \qquad i = 1, 2, 3,\tag{13}
$$

which may or may not be in the valid portion of $\rho _ { i }$

Corollary 1: The royalty maximizing price of the creator has the form

$$
P _ {O} ^ {*} = \frac {\alpha_ {i}}{2 \beta_ {i}} \quad i = 1, 2, \text {   or   } 3.\tag{14}
$$

Proof: See the Appendix.

By Theorem 1, to find the monopolist’s optimal price, three prices $P _ { M 1 } ^ { * } , P _ { M 2 } ^ { * }$ , and $P _ { M 3 } ^ { * }$ are computed using $( \mathsf { a } _ { _ 1 } , \mathsf { \beta } _ { 1 } ) , ( \mathsf { a } _ { _ 2 } , \mathsf { \beta } _ { 2 } )$ , and $( \mathsf { a } _ { _ 3 } , \mathsf { \beta } _ { 3 } )$ , respectively, in Equation (8). Profits for prices satisfying $P _ { _ { M i } } ^ { * } \in R _ { _ { i } } \left( i = 1 , 2 , 3 \right)$ are computed using Equation (7) and the best price is selected. By Corollary 1 to find the creator’s optimal price, three prices $P _ { o 1 } ^ { * } , P _ { o 2 } ^ { * }$ , and $P _ { O 3 } ^ { * }$ are computed using $( \mathsf { a } _ { _ 1 } , \mathsf { \beta } _ { _ 1 } ) , ( \mathsf { a } _ { _ 2 } , \mathsf { \beta } _ { _ 2 } )$ , and $( \mathfrak { a } _ { _ 3 } , \mathfrak { \beta } _ { _ 3 } )$ , respectively, in Equation (13). Royalties for prices satisfying $P _ { o i } ^ { * } \in R _ { i } \left( \mathrm { i } = 1 , 2 , 3 \right)$ are computed using Equation (12) and the best price is selected.

Theorem 2: $H \nu > O ,$ then the creator’s royalty-maximizing price is less than the monopolist’s profit-maximizing price.

Proof: See the Appendix.

In other words, Theorem 2 implies that the creator faces a royalty loss because the monopolist sets the price. If the profit-maximizing price and the royalty-maximizing price fall in the same price region $R _ { \ i } ,$ this loss in royalty, denoted by $\kappa ,$ is computed using Equations (9), (11), and (14) as

$$
\kappa = \frac {r \beta_ {i} v ^ {2}}{4 (1 - r) ^ {2}}.\tag{15}
$$

The magnitude of the royalty loss depends on the parameters $\beta _ { i } , r ,$ and $\nu ,$ which has three implications. First, by joining the campaign to prevent piracy, which decreases the slope of the demand curve $( \mathrm { i . e . , \boldsymbol { \beta } _ { i } } )$ , the creator decreases potential royalty loss from the monopolist’s pricing policy. Second, it is better for the creator if the monopolist charges less than his or her optimal price, in spite of the royalty being a percentage of price. Furthermore, because $d \kappa / d r = \beta _ { i } \nu ^ { 2 } ( 1 + r ) / [ 4 ( 1 - r ) ^ { 3 } ] > 0 .$ , the creator’s preference for a lower price is even stronger when his or her royalty share of price is large. The creator’s royalty loss by agreeing to the monopolist’s optimal price is higher if the monopolist’s price and creator’s price fall in different regions.

In the above analysis, we assumed a physical distribution channel is used. However, the creator of the digital good is likely to prefer a digital online distribution because it reduces variable unit cost, and thus reduces price conflict with the monopolist. If the variable unit cost is zero, the optimal price of the monopolist also becomes optimal for the creator.

## Royalty Negotiation Between the Creator and the Monopolist

By Theorem 2, if the variable cost is positive, the monopolist prefers a higher price than the creator desires. This phenomenon is part of a problem known as double marginalization [45]. Double marginalization arises in two-stage supply chains and leads to smaller product quantity being sold at a higher price and less revenue than if the two parties merge. The structure of the industry in our model produces a similar suboptimal solution because the creator can be considered the upstream supplier. The total revenue in our model is $\boldsymbol \Phi = \boldsymbol \pi + \boldsymbol \rho$ . The revenue-maximizing price is given by Corollary 2.

Corollary 2: The revenue-maximizing price of the industry has the form

$$
P _ {I} ^ {*} = \frac {\alpha_ {i}}{2 \beta_ {i}} + \frac {v}{2} \quad i = 1, 2, \text {   or   } 3.\tag{16}
$$

## Proof: See the Appendix.

By Corollary 2 and Theorem 1, the monopolist’s preferred price does not maximize industry revenue except for the trivial cases of zero royalty rate or zero variable cost.

Solutions to double marginalization include vertical integration, revenue sharing, and resale price maintenance. Revenue sharing through the royalty system is well established in the music and publishing industries. This royalty system, however, does not eliminate the double marginalization problem because the system is based on the retail price of the product and not total profit of both monopolist and creator. The initial motivation of the royalty system was in fact not to resolve double marginalization. It was rather to facilitate artists’ creativity by furnishing them with an incentive to create.

The royalty rate is usually negotiated as a percentage of price before a creator signs a contract. If the creator and the monopolist try to reach a point where both parties agree, the negotiated royalty rate would represent a fair rate based on each party’s negotiation power. Therefore, creators focus mainly on obtaining the best royalty rate. To analyze the negotiation between the creator and the monopolist, let $r _ { \scriptscriptstyle N }$ be the negotiated royalty rate of the creator; $P _ { \scriptscriptstyle { N } }$ be the price resulting from negotiation; and ω be the negotiating power of the creator, which depends on many factors including the popularity of the artist and the investment needed by the record label.

At $r = r _ { \mathrm { { } } _ { N } }$ if $P _ { \scriptscriptstyle { N } }$ is set to $P _ { M } ^ { * }$ , the monopolist’s profit is at a maximum $( \mathrm { i } . \mathrm { e } . , \pi _ { M } ^ { * } )$ , whereas if $P _ { \scriptscriptstyle { N } }$ is set to $P _ { o } ^ { * } ,$ the creator’s royalty is at a maximum $( \mathrm { i } . \mathrm { e } . , \rho _ { M } ^ { * } )$ . We use the following measure of the creator’s negotiating power:

$$
\omega = \left(\frac {\pi_ {M} ^ {*} - \pi_ {N}}{\pi_ {M} ^ {*} - \pi_ {O}}\right) / \left(\frac {\rho_ {O} ^ {*} - \rho_ {N}}{\rho_ {O} ^ {*} - \rho_ {M}}\right).\tag{17}
$$

$\pi _ { { \scriptscriptstyle M } } ^ { * } - \pi _ { o }$ measures the difference between the monopolist’s profit if he or she has complete control over price (best scenario for the monopolist) and if the creator has complete control over price (worst scenario for the monopolist). Likewise, $\rho _ { o } ^ { * } - \rho _ { { \scriptscriptstyle M } }$ measures the difference between the creator’s royalty if he or she has complete control over price and if the monopolist has complete control over price. $\omega = 1$ indicates that both the monopolist and the creator move the same distance from their best to worst positions on a relative basis. $\Theta = 0$ indicates that the monopolist sets the price at his or her optimal value resulting in $\pi _ { _ { M } } ^ { * } = \pi _ { _ { N } } . \infty > 1$ indicates that the price is closer to the creator’s best position than the monopolist’s best position. Figure 3 shows the different regions in terms of negotiating power of the two parties. A creator trying to maximize royalty should negotiate not only the royalty rate but also price. As Figure 3 shows, all $( P _ { _ { N } } , r _ { _ { N } } )$ on $\omega = 1$ indicate that both the creator and the monopolist have moved the same relative distance from their best positions. In area C, the monopolist has given up more on a relative basis, whereas in area M, the creator has given up more. The figure indicates that if the creator negotiates a larger royalty rate while leaving price under the monopolist’s control, then the monopolist responds by increasing the price, which actually may cause a decline in the creator’s royalty.

For a given negotiated royalty $r _ { N }$ and a creator–monopolist power distribution, a negotiated price occurs on the iso-power curve representing that distribution. Thus, by solving Equation (17) for $P _ { N } ,$ the price given a creator’s power of ω occurs at

$$
P _ {N} = \frac {\alpha_ {i}}{2 \beta_ {i}} + \frac {v}{2 (1 - r _ {N}) (1 + \sqrt {\omega})}.\tag{18}
$$

![](/api/attachments/HR4ZTHER/fulltext/images/95247817fd6f8a27801f6d97826702f7fdb29d74034820202e7800217e783d4e.jpg)  
Figure 3. Iso-Power Curve

At ${ \mathfrak { \omega } } = 1 , P _ { _ N } = ( P _ { _ O } + P _ { _ M } ) / 2$ , which implies that each party moves halfway between their best and worst positions.

Equation (16) shows that the revenue-maximizing price $( P _ { I } ^ { * } )$ does not depend on the royalty rate because ϕ is a function of price alone. Therefore, if the price is set to $\boldsymbol { P } _ { I } ^ { * }$ , revenue is maximized. Substituting $\boldsymbol { P } _ { \boldsymbol { N } } = \boldsymbol { P } _ { \boldsymbol { I } } ^ { * }$ <sup>\*</sup> into Equation (18) yields the royalty rate at which the negotiated price is revenue maximizing as a function of the creator’s power. This royalty rate is

$$
r _ {I} ^ {*} = \frac {\sqrt {\omega}}{1 + \sqrt {\omega}}.\tag{19}
$$

The revenue-maximizing royalty rate increases at a decreasing rate as ω increases as shown in Figure 4. $\mathrm { A t } \odot = 1$ the figure shows $r _ { _ { I } } ^ { ^ { * } } = 0 . 5$ . For example, a revenue-sharing program between movie studios and Blockbuster video rental, which increased industry revenue, used a royalty rate close to 0.5 [5, 13].

The above analysis indicates that a more cooperative approach to negotiation along with redistribution of the additional revenue as a result of using $\boldsymbol { P } _ { _ { I } } ^ { * }$ is of benefit to both the creator and the monopolist. The additional revenue from $\boldsymbol { P } _ { I } ^ { * }$ is

$$
\Delta \varphi = \varphi \left(P _ {I} ^ {*}\right) - \varphi \left(P _ {N}\right) = \frac {\beta_ {i} v ^ {2} \left(r _ {N} - r _ {I} ^ {*}\right) ^ {2}}{4 \left(1 - r _ {N}\right) ^ {2}}.\tag{20}
$$

A simple way to redistribute the additional revenue is to determine the relative distance each party should be from its best position (i.e., the value of ω). Using this value of ω, the corresponding $r _ { _ { I } } ^ { \ast }$ is computed using Equation (19) and then price is set at the revenue-maximizing value of $\boldsymbol { P } _ { I } ^ { * }$

![](/api/attachments/HR4ZTHER/fulltext/images/10cb5d9ec39181dc91701be988ffd0f490732b11af67092f349ab186c381aa11.jpg)  
Figure 4. The Industry Revenue-Maximizing Royalty Rate

## An Optimistic Monopolist and the Ethical Consumer Focus

SUPPOSE A MONOPOLIST ASSUMES, ALBEIT UNREALISTICALLY, that piracy can be mostly eliminated and treats all consumers as ethical. The monopolist’s profit with this misjudgment can decrease because of using an incorrect demand function. Hence, the focus of the analysis in this section is on understanding the effect of this misjudgment on the monopolist’s profit and the creator’s royalty. The monopolist treats all consumers as ethical and uses the demand function

$$
D = \left(a _ {1} + a _ {2} + a _ {3}\right) - \frac {b _ {1} \left(a _ {1} + a _ {2} + a _ {3}\right)}{a _ {1}} P,\tag{21}
$$

in which demand vanishes at $a _ { _ 1 } / b _ { _ 1 }$ . The monopolist’s optimal price ${ P _ { \mathrm { ~ } _ { E } } } ^ { * }$ is given by

$$
P _ {E} ^ {*} = \frac {a _ {1}}{2 b _ {1}} + \frac {v}{2 (1 - r)}.\tag{22}
$$

## The Cost of Ethical Focus to the Monopolist

If the monopolist ignores piracy, then Theorem 3 shows that doing so will frequently decrease profits.

Theorem 3: If the true optimal price $P _ { _ M } ^ { \ast } \in R , i = 2 o r 3$ , then the ethical focus’s optimal price $P _ { \phantom { * } E } ^ { * }$ is larger than $P _ { { _ M } } ^ { \ast } . \qquad H P _ { { _ M } } ^ { \ast } \in R _ { \widehat { t } } ,$ then $P _ { M } ^ { * } = P _ { E } ^ { * }$

Proof: See the Appendix.

Theorem 3 implies that the ethical focus’s optimal price is the same as the true optimal price $P _ { \ M } ^ { * }$ if both prices fall in $R _ { \mathrm { _ 1 } } .$ This happens when ethical consumers dominate the market. For example, the recorded music market prior to digitization and the Internet was dominated by ethical consumers due to the difficulty of pirating. This made $R _ { 1 }$ wider and increased the probability of $P _ { \ M } ^ { * }$ falling in $R _ { \mathrm { 1 ^ { \prime } } }$ . Therefore, keeping a high price in $R _ { _ 1 }$ and focusing on controlling piracy would have been the best strategy for the record labels. As copying technology improved, $R _ { 1 }$ narrowed and the probability that $P _ { \ M } ^ { * }$ would fall in $R _ { 2 }$ or $R _ { 3 }$ increased. If, in spite of this change, the monopolist keeps the price at $P _ { \phantom { * } { E } } ^ { * }$ Theorem 3 indicates that if the true optimal price falls in regions 2 or $3 \ ( \mathrm { i . e . , } \ P _ { M 2 } ^ { \ast }$ or $P _ { M 3 } ^ { * }$ is optimal), this misjudgment causes the monopolist to charge a suboptimal price. Let us define

$$
\overline {{{{\alpha}}}} _ {j} = \alpha_ {j} - a _ {1} \text {   and   } \overline {{{{\beta}}}} _ {j} = \beta_ {j} - b _ {1} \quad \text {   for   } j = 2 \text {   or   } 3.\tag{23}
$$

$\overline { { \alpha } } _ { j }$ represents the consumer base of the indifferent and pirating segments $\operatorname { i f } j = 3$ and the consumer base of the indifferent segment $\operatorname { i f } j = 2 . { \overline { { \beta } } } _ { \mathrm { { i } } }$ represents the total demand slope for the indifferent and pirating segments $\mathrm { i f } j = 3$ and the slope for the indifferent segment demand if $j = 2$ . If $P _ { M j } ^ { * } , j = 2$ or 3, is optimal and $P _ { \ E } ^ { * }$ is in $R _ { 1 }$ , the cost of the misjudgment θ is

$$
\theta = \pi^ {*} - \pi_ {P = P _ {E} ^ {*}} = \frac {1 - r}{4} \left[ \frac {\left(a _ {1} + \overline {{\alpha}} _ {j}\right) ^ {2}}{b _ {1} + \overline {{\beta}} _ {j}} - \frac {a _ {1} ^ {2}}{b _ {1}} \right] - \frac {\overline {{\alpha}} _ {j}}{2} v + \frac {\overline {{\beta}} _ {j}}{4 (1 - r)} v ^ {2}.\tag{24}
$$

By Theorem 1, θ is always positive. Taking the derivative of θ with respect to (w.r.t.) $\overline { { \mathsf { \beta } } } _ { j }$ yields

$$
\frac {\partial \theta}{\partial \overline {{\beta}} _ {j}} = \frac {1 - r}{4} \left(\frac {v}{1 - r} + \frac {a _ {1} + \overline {{\alpha}} _ {j}}{b _ {1} + \overline {{\beta}} _ {j}}\right) \left(\frac {v}{1 - r} - \frac {a _ {1} + \overline {{\alpha}} _ {j}}{b _ {1} + \overline {{\beta}} _ {j}}\right).\tag{25}
$$

Because v is relatively small and $a _ { _ i }$ is expected to be much larger than $b _ { _ i } ( i = 1 , 2 , 3 )$ ${ \partial \Theta } / { \partial { \overline { { \beta } } } _ { j } } < 0$ , which implies that a decrease in $\overline { { \mathsf { \beta } } } _ { j }$ will result in an increase in the cost of misjudgment. Therefore, a monopolist investing in piracy control to decrease $\overline { { \mathsf { \beta } } } _ { j }$ will have one of two outcomes: (1) $P _ { \ M } ^ { * } = P _ { \ E } ^ { * }$ and are in $R _ { \mathrm { 1 } } ,$ or (2) $P _ { M 2 } ^ { * }$ or $P _ { M 3 } ^ { * }$ remains optimal. In the second case, because ∂θ/∂β<sup>ÿ</sup> < 0, investment in piracy control without changing price will increase the cost of misjudgment.

Taking the derivative of θ w.r.t. v yields

$$
\frac {\partial \theta}{\partial v} = \frac {1}{2} \left(\frac {\overline {{\beta}} _ {j} v}{1 - r} - \overline {{\alpha}} _ {j}\right).\tag{26}
$$

If $\overline { { \alpha } } _ { j }$ is large, $\partial \theta / \partial \nu < 0$ , which implies that the misjudgment cost increases as the variable cost decreases. This indicates that if the indifferent and pirating segments consumer base is large and the monopolist uses an online distribution channel with small variable cost, he or she will have a larger misjudgment cost than if he or she was using a traditional distribution channel with higher variable unit cost. Therefore, it is critical for the monopolist to change the pricing policy as he or she moves to online distribution channels with low variable unit cost.

If $P _ { _ { E } } ^ { * }$ fall in the same region as $P _ { M j } ^ { * }$ (i.e., in region $R _ { 2 }$ or $R _ { _ 3 } ) _ { \cdot }$ , Theorem 3 again implies that the true optimal price $\boldsymbol { P } _ { M } ^ { * }$ is lower than the ethical focus’s price $P _ { \phantom { * } { E } } ^ { * }$ The cost of misjudgment, given that $P _ { _ { M j } } ^ { * } , j = 2$ or 3, is optimal and $P _ { \phantom { * } E } ^ { * }$ is in the same region as $P _ { M j } ^ { * } ,$ is

$$
\theta = \frac {(1 - r) \left(a _ {1} \overline {{\beta}} _ {j} - b _ {1} \overline {{\alpha}} _ {j}\right) ^ {2}}{4 b _ {1} ^ {2} (b _ {1} + \overline {{\beta}} _ {j})} \quad \text { if } P _ {M} ^ {*} \text { and } P _ {E} ^ {*} \in R _ {2} \text { or } P _ {M} ^ {*} \text { and } P _ {E} ^ {*} \in R _ {3}.\tag{27}
$$

We are again interested in the sign of ${ \hat { o } } \Theta / { \hat { o } } { \overline { { \beta } } } _ { j } .$ which is calculated as

$$
\frac {\partial \theta}{\partial \overline {{\beta}} _ {j}} = \frac {(1 - r) (a _ {1} \overline {{\beta}} _ {j} - b _ {1} \overline {{\alpha}} _ {j}) (b _ {1} (a _ {1} + \overline {{\alpha}} _ {j}) + a _ {1} (b _ {1} + \overline {{\beta}} _ {j}))}{4 b _ {1} ^ {2} (b _ {1} + \overline {{\beta}} _ {j}) ^ {2}}.\tag{28}
$$

By Lemma $1 , a _ { _ 1 } \beta _ { _ i } - b _ { _ 1 } \alpha _ { _ i } > 0$ , which can be rewritten as $a _ { 1 } ( b _ { 1 } + \overline { { \beta } } _ { i } ) - b _ { 1 } ( a _ { 1 } + \overline { { \alpha } } _ { i } ) > 0$ Therefore, $a _ { 1 } \overline { { \beta } } _ { { } _ { j } } - b _ { 1 } \overline { { \alpha } } _ { { } _ { j } } > 0$ and ${ \hat { \partial } } \Theta / { \hat { \partial } } { \overline { { \beta } } } _ { i } > 0$ . This implies that if the monopolist wants to keep the price high, then he or she should invest in piracy control. The extent of the investment depends on the cost of piracy controls and the distribution of the consumers among the three segments.

## The Cost of the Monopolist’s Ethical Focus to the Creator

Ignoring the existence of indifferent and pirating consumers may cause further erosion in the creator’s royalty. If $P _ { M i ^ { 3 } } ^ { * } j = 2$ or 3, is optimal and $P _ { _ { E } } ^ { * }$ is in $R _ { \scriptscriptstyle 1 }$ , the cost of the misjudgment to the creator is

$$
\begin{array}{c} \zeta = \rho_ {P = P _ {M} ^ {*}} - \rho_ {P = P _ {E} ^ {*}} = \frac {r}{4} \Bigg (\frac {\left(a _ {1} + \overline {{\alpha}} _ {j}\right) ^ {2}}{b _ {1} + \overline {{\beta}} _ {j}} - \frac {a _ {1} ^ {2}}{b _ {1}} - \frac {\overline {{\beta}} _ {j}}{\left(1 - r\right) ^ {2}} v ^ {2} \Bigg) \\ P _ {M} ^ {*} \in R _ {2} \cup R _ {3} \text {and} P _ {E} ^ {*} \in R _ {1}. \end{array}\tag{29}
$$

The sign of $\zeta$ is inconclusive, which implies that the monopolist’s misjudgment may not be harmful to the creator. If both the variable unit cost and the creator’s royalty share are large, the creator may benefit from the monopolist’s misjudgment. On the other hand, if the variable unit cost is small, then the creator is less likely to benefit from the monopolists misjudgment. In the extreme case where the variable cost is zero, Equation (29) shows that the creator is worse off. The derivative of $\xi$ w.r.t. $\overline { { \mathsf { \beta } } } _ { j }$ is

$$
\frac {\partial \zeta}{\partial \overline {{\beta}} _ {j}} = - \frac {r}{4} \left(\frac {\left(a _ {1} + \overline {{\alpha}} _ {j}\right) ^ {2}}{\left(b _ {1} + \overline {{\beta}} _ {j}\right) ^ {2}} + \frac {v ^ {2}}{(1 - r) ^ {2}}\right) <   0,\tag{30}
$$

which implies that the monopolist’s policy of decreasing ${ \overline { { \mathsf { \beta } } } } _ { j }$ further increases the cost to the creator’s royalty if $P _ { M 2 } ^ { * }$ or $P _ { M 3 } ^ { * }$ remains optimal. In other words, if there is a relatively large number of ethical consumers and the monopolist decides to keep the suboptimal price $P _ { \phantom { * } _ { E } } ^ { * }$ in $R _ { _ 1 }$ , the policy of preventing piracy will increase the creator’s loss of royalty.

Because ${ \partial \zeta } / { \partial \nu } < 0$ and ${ \partial \zeta } / { \partial r } < 0$ , the cost of the misjudgment to the creator increases more as r and v get smaller. Therefore, if the creator accepts a low royalty share and the monopolist uses an online channel, then it is critical for the creator that the monopolist agrees to a low-price policy.

If $P _ { M j } ^ { * } , j = 2$ or 3, is optimal and $P _ { \ E } ^ { * }$ falls in the same region as $P _ { M j } ^ { * } ,$ the cost of the monopolist’s misjudgment to the creator is

$$
\zeta = r \left[ \frac {\left(a _ {1} \overline {{\beta}} _ {j} - b _ {1} \overline {{\alpha}} _ {j}\right) ^ {2}}{4 b _ {1} ^ {2} \left(b _ {1} + \overline {{\beta}} _ {j}\right)} + \frac {\left(a _ {1} \overline {{\beta}} _ {j} - b _ {1} \overline {{\alpha}} _ {j}\right)}{2 b _ {1} (1 - r)} v \right]\tag{31}
$$

$$
\text { if } P _ {M} ^ {*} \text { and } P _ {E} ^ {*} \in R _ {2} \text { or } P _ {M} ^ {*} \text { and } P _ {E} ^ {*} \in R _ {3}.
$$

The derivative of $\zeta$ w.r.t. ${ \overline { { \mathsf { \beta } } } } _ { i }$ is

$$
\frac {\partial \zeta}{\partial \overline {{\beta}} _ {j}} = r \left[ \frac {\left(a _ {1} \overline {{\beta}} _ {j} - b _ {1} \overline {{\alpha}} _ {j}\right) \left(\overline {{\alpha}} _ {j} b _ {1} + 2 a _ {1} b _ {1} + a _ {1} \overline {{\beta}} _ {j}\right)}{4 b _ {1} ^ {2} \left(b _ {1} + \overline {{\beta}} _ {j}\right) ^ {2}} + \frac {a _ {1}}{2 b _ {1} (1 - r)} v \right].\tag{32}
$$

Because $a _ { 1 } \overline { { \mathsf { B } } } _ { j } - b _ { 1 } \overline { { \mathsf { a } } } _ { j } > 0 , \hat { \sigma } \zeta / \hat { \sigma } \overline { { \mathsf { B } } } _ { j } > 0$ , which implies that the creator should join the monopolist’s piracy prevention campaign. Unlike the previous case, ${ \partial \zeta } / { \partial \nu } > 0$ and ${ \partial \zeta } / { \partial r } > 0$ , which implies that the cost of misjudgment to the creator increases the royalty share and increases as the variable unit cost increases.

## Numerical Examples

Consider a record label selling music CDs to three consumer segments—ethical, indifferent, and pirating. The label pays 10 percent of revenue in royalty $( r = 0 . 1 0 )$ . Fixed cost is $F = \$ 1,000,000$ and variable unit cost is $\nu = \$ 4$ . We solve the example for two demand cases. In the first case, the ethical segment is the largest. In the second, the pirating segment is the largest. For each case, we obtain the monopolist’s optimal price, taking into account the characteristics of the three segments, and compare it to the prices the monopolist obtains under (1) a demand function which assumes all consumers are ethical, and (2) a demand function which aggregates all segments into one homogeneous segment and uses linear regression to estimate the demand.

## The Ethical Segment Dominates the Market

This may be the case of classical music. We use $( a _ { 1 } , b _ { 1 } ) = ( 1 5 0 , 0 0 0 , 3 , 0 0 0 ) , ( a _ { 2 } , b _ { 2 } ) =$ (100,000, 4,000), and $( a _ { 3 } , b _ { 3 } ) = ( 5 0 , 0 0 0 , 5 , 0 0 0 )$ . Demand vanishes at prices of \$10, \$25, and \$50, for the pirating, indifferent, and ethical segments, respectively. Therefore, $R _ { 1 } = ( 2 5 , 5 0 ] , R _ { 2 } = ( 2 5 , 1 0 ]$ , and $R _ { 3 } = [ 0 , 1 0 ]$ , and

$$
D = \left\{ \begin{array}{l l} 3 0 0, 0 0 0 - 1 2, 0 0 0 P & \text { if } P \in R _ {3} \\ 2 5 0, 0 0 0 - 7, 0 0 0 P & \text { if } P \in R _ {2} \\ 1 5 0, 0 0 0 - 3, 0 0 0 P & \text { if } P \in R _ {1}. \end{array} \right.
$$

The monopolist’s optimal price and profit are $P _ { _ M } ^ { * } = \ S 2 0 . 0 8$ and $\pi ^ { * } = \mathbb { S } 5 4 0 , 0 4 0$ . The creator receives $\rho = \$ 219,757$ , but by Theorem 2, he or she could have earned $\rho ^ { * } =$ \$223,214 if the price was $P _ { o } ^ { * } = \ S 1 7 . 8 6$

If the record label assumes all consumers are ethical, the estimated demand function has an intercept of $3 0 0 { , } 0 0 0$ and demand vanishes at a price of \$50. Using Equation (22), the optimal monopolist’s price is $P _ { _ { E } } ^ { * } = \ S 2 7 . 2 2$ , at which profit is $\pi _ { _ { E } } ^ { * } = \mathbb { S } 4 0 0 , 8 3 3$ Ignoring the characteristics of the pirating and indifferent consumers decreases profit by 25.8 percent. Royalty at this price is $\rho _ { E } ^ { * } = \up$ 186,019$ , which is a decrease of 15.4 percent from the royalty if the monopolist incorporated the different characteristics of consumers in pricing.

If the monopolist estimates demand using linear regression from a random sample of consumers, least squares regression results in $D = 2 4 3 , 0 0 0 - 5 , 5 2 0 P$ . Using Equation (22), the optimal price is $P _ { _ R } ^ { ^ * } { = } \$ 24.23$ , at which profit is $\pi _ { R } ^ { * } { = } \$ 431 ,343$ , where the subscript R denotes the results using least squares regression. By aggregating all consumers into one segment, profit decreases by 20.1 percent. The creator’s royalty is $\rho _ { R } ^ { * } = \up$ 194,757$ which is a decrease of 11.4 percent from the royalty that would have been earned if the monopolist incorporated the different characteristics of consumers in pricing.

## The Pirating Segment Dominates the Market

This may be the case of hip-hop music where young males are a majority of consumers. We use $( a _ { 1 } , b _ { 1 } ) = ( 1 0 0 , 0 0 0 , 2 , 0 0 0 ) , ( a _ { 2 } , b _ { \it 2 } ) = ( 1 5 0 , 0 0 0 , 6 , 0 0 0 )$ , and $( a _ { _ 3 } , b _ { _ 3 } ) = ( 4 5 0 , 0 0 0$ 45,000). Demand vanishes at prices of \$10, \$25, and \$50, for pirating, indifferent, and ethical segments, respectively. The demand is

$$
D = \left\{ \begin{array}{l l} 7 0 0, 0 0 0 - 5 3, 0 0 0 P & \text { if } P \in R _ {3} \\ 2 5 0, 0 0 0 - 8, 0 0 0 P & \text { if } P \in R _ {2} \\ 1 0 0, 0 0 0 - 2, 0 0 0 P & \text { if } P \in R _ {1}. \end{array} \right.
$$

The monopolist’s optimal price and profit are $P _ { _ M } ^ { * } = \ S 1 7 . 8 5$ and $\pi ^ { * } = \mathbb { S } 2 9 3 , 3 6 8$ . The creator receives $\rho = \$ 191,362$ , but by Theorem 2, he or she could have earned $\rho ^ { * } =$ \$231,132 if the price was set at $P _ { o } ^ { * } = \mathbb { S } 6 . 6 0$

If the record label assumes all consumers are ethical, the estimated demand curve has an intercept of 700,000 and the demand vanishes at a price of \$50. Using Equation (22), the optimal price is $P _ { \mathrm { \varepsilon } } ^ { * } = \$ 27 .22$ , at which the monopolist loses $\$ 66,111$ Royalty is $\rho _ { E } ^ { * } = \up$ 124,012$ , which is a decrease of 35.2 percent from the royalty that would have been earned if the monopolist incorporated the different characteristics of consumers.

Suppose the monopolist estimates the demand curve using linear regression from a random sample of consumers. The resulting demand is $D = 3 7 4 , 5 0 0 0 - 9 , 6 8 0 P$ . Using

Equation (22), the optimal price is $P _ { _ R } ^ { * } = \ S 2 1 . 5 7$ , at which the profit is $\pi _ { _ R } ^ { * } = \ S 1 9 3 , 7 8 5 .$ Ignoring the characteristics of pirating and indifferent consumers decreases profit by 33.9 percent. Royalty is $\rho _ { R } ^ { * } = \up$ 167 ,07 4$ , which is a decrease of 12.7 percent from the royalty which would have been earned if the monopolist had incorporated the different characteristics of consumers in pricing.

## Introduction of Online Music Distribution

In the above examples, the variable cost was set to $\nu = \$ 4$ due to the costs of producing, packaging, and distributing CDs. Because of MP3 technology and the Internet, it is possible to sell music online with v close to zero. Selling music online may involve additional fixed costs such as setting up an online store. Thus, we increase the fixed cost by 25 percent and reduce the variable unit cost to \$0.50. Table 1 summarizes the results for different cost parameters. Due to a smaller variable cost, the monopolist’s optimal price for classical music decreased by 9.7 percent from \$20.08 to \$18.13. However, there was a larger price drop from \$17.85 to \$6.88 for hip-hop music. The monopolist’s profit increase of \$365,501 for hip-hop music due to the online channel is much larger than the increase of \$156,875 for classical music. Royalty increased for classical music by \$3,403, whereas the royalty in the hip-hop music case increased by \$39,361.

The example indicates that a price-cutting strategy should be used when variable unit cost is low and pirating consumers dominate the market. Another implication is that for products for which ethical consumers dominate the market, there is less incentive to switch to an online distribution.

## Legal Sales and Social Welfare

WE FIRST DERIVE THE QUANTITY OF LEGITIMATE UNITS SOLD at the monopolist’s true optimal price and compare it to the quantity sold at the ethical focus’s optimal price. Next, we derive consumers’ surplus and social welfare from the sales of legitimate units at those prices. The number of legitimate units sold at the monopolist’s optimal price, denoted by $q _ { M } ^ { * } ,$ is given by

$$
q _ {M} ^ {*} = D \Big (P _ {M} ^ {*} \Big) = \left\{ \begin{array}{l l} \big (a _ {1} + a _ {2} + a _ {3} \big) - \big (b _ {1} + b _ {2} + b _ {3} \big) P _ {M} ^ {*} & \text {if} P _ {M} ^ {*} \in R _ {3} \\ \big (a _ {1} + a _ {2} \big) - \big (b _ {1} + b _ {2} \big) P _ {M} ^ {*} & \text {if} P _ {M} ^ {*} \in R _ {2} \\ a _ {1} - b _ {1} P _ {M} ^ {*} & \text {if} P _ {M} ^ {*} \in R _ {1}. \end{array} \right.\tag{33}
$$

The number of legitimate units sold at the ethical focus’s price $\boldsymbol { P } _ { E } ^ { * } ,$ denoted by $q _ { E } ^ { * } ,$ is given by

$$
q _ {E} ^ {*} = D \Big (P _ {E} ^ {*} \Big) = \left\{ \begin{array}{l l} \big (a _ {1} + a _ {2} + a _ {3} \big) - \big (b _ {1} + b _ {2} + b _ {3} \big) P _ {E} ^ {*} & \text { if } P _ {E} ^ {*} \in R _ {3} \\ \big (a _ {1} + a _ {2} \big) - \big (b _ {1} + b _ {2} \big) P _ {E} ^ {*} & \text { if } P _ {E} ^ {*} \in R _ {2} \\ a _ {1} - b _ {1} P _ {E} ^ {*} & \text { if } P _ {E} ^ {*} \in R _ {1}. \end{array} \right.\tag{34}
$$

<sub>ptimal</sub> <sub>Solutions</sub> <sub>for</sub> <sub>Different</sub> <sub>Mus</sub>i<sup>c</sup> <sup>Markets</sup> <sup>and</sup> <sup>Distribu</sup>

<table><tr><td rowspan="2">Music type</td><td colspan="2">Cost parameters</td><td colspan="3">Price</td><td colspan="3">Profit</td><td colspan="3">Royalty</td></tr><tr><td> $v$ </td><td> $F$ </td><td> $P_{M}^{*}$ </td><td> $P_{E}^{*}$ </td><td> $P_{R}^{*}$ </td><td> $\pi_{M}^{*}$ </td><td> $\pi_{E}^{*}$ </td><td> $\pi_{R}^{*}$ </td><td> $\rho_{M}$ </td><td> $\rho_{E}$ </td><td> $\rho_{R}$ </td></tr><tr><td rowspan="2">Classical</td><td>4.0</td><td>1,000,000</td><td>20.08</td><td>27.22</td><td>24.23</td><td>540,040</td><td>400,833</td><td>431,343</td><td>219,757</td><td>186,019</td><td>194,757</td></tr><tr><td>0.5</td><td>1,250,000</td><td>18.13</td><td>25.28</td><td>22.29</td><td>696,915</td><td>400,208</td><td>588,218</td><td>223,160</td><td>187,477</td><td>209,468</td></tr><tr><td rowspan="2">Hip-hop</td><td>4.0</td><td>1,000,000</td><td>17.85</td><td>27.22</td><td>21.57</td><td>293,368</td><td>-66,111</td><td>193,785</td><td>191,362</td><td>124,012</td><td>167,074</td></tr><tr><td>0.5</td><td>1,250,000</td><td>6.88</td><td>25.28</td><td>19.62</td><td>658,869</td><td>-149,861</td><td>346,285</td><td>230,723</td><td>124,985</td><td>182,533</td></tr></table>

As Figure 5 shows, $q _ { { \scriptscriptstyle M } } ^ { * } \ge q _ { { \scriptscriptstyle E } } ^ { * }$ because demand is decreasing in P and, by Theorem 3, $P _ { \phantom { * } { E } } ^ { * } \geq P _ { \phantom { * } { M } } ^ { * }$ In general, a higher price results in less legitimate product diffusion. Therefore, the monopolist will sell a smaller quantity at a higher price if he or she assumes all consumers are ethical. The difference in the quantity sold, denoted by $\Psi ,$ , is given by

$$
\psi = q _ {M} ^ {*} - q _ {E} ^ {*} = \frac {1}{2} \left(\overline {{\alpha}} _ {j} - \frac {\overline {{\beta}} _ {j}}{1 - r} v\right) \quad \text { if } P _ {M} ^ {*} \in R _ {2} \text { or } R _ {3} \text { and } P _ {E} ^ {*} \in R _ {1}.\tag{35}
$$

The loss in legitimate sales due to the ethical focus is largest for small variable unit cost and small creator’s royalty share. Because ${ \hat { o } } \Psi / { \hat { o } } { \overline { { \beta } } } _ { i } < 0$ , the monopolist’s effort to lower $\overline { { \beta } } _ { i }$ —that is, curtail piracy—results in more loss in legitimate sales.

If both $P _ { \ M } ^ { * }$ and $P _ { _ { E } } ^ { * }$ fall in $R _ { 2 }$ or $R _ { 3 }$ , the difference in quantity is given by

$$
\psi = \frac {1}{2} \left(P _ {1} \overline {{\beta}} _ {j} - \overline {{\alpha}} _ {j}\right) \quad \text { if } P _ {M} ^ {*} \text { and } P _ {E} ^ {*} \in R _ {2} \text { or } P _ {M} ^ {*} \text { and } P _ {E} ^ {*} \in R _ {3}.\tag{36}
$$

Unlike the first case, the effort to reduce piracy by lowering $\overline { { \mathsf { \beta } } } _ { j }$ decreases the gap between $q _ { M } ^ { * }$ and $q _ { E } ^ { * }$ . In this case, the monopolist’s effort to decrease $\overline { { \mathsf { \beta } } } _ { j }$ increases consumers’ willingness to pay for the product and also increases legitimate sales among indifferent and pirating consumers, therefore reducing the gap in Equation (36).

Some consumers whose reservation prices are not met will pirate, which can lead to higher social welfare. Unlike this utilitarian interpretation of social welfare used in other studies [9], we calculate social welfare from the sale of legitimate units only. We consider only legitimate sales because, for many products whose creator is different than the producer, piracy decreases the creator’s royalty. The increase in consumers surplus $( G _ { c s } )$ due to incorporating piracy depends on the regions where $P _ { M } ^ { * }$ and $P _ { \ E } ^ { * }$ fall. If both $P _ { \ E } ^ { * }$ and $P _ { M } ^ { * }$ are in $R _ { 1 } , P _ { E } ^ { * } = P _ { M } ^ { * }$ and there is no change in consumers’ surplus. All other cases will result in an increase in consumers’ surplus. For simplicity, we show the expression for the increase in consumer surplus for only one case, ${ P ^ { * } } _ { { _ M } } \in R _ { _ 2 }$ and $P _ { { \scriptscriptstyle E } } ^ { * } \in R _ { _ { 1 } } .$ , out of five possible cases

$$
G _ {C S} = \int_ {P _ {M} ^ {*}} ^ {P _ {2}} \left(\alpha_ {2} - \beta_ {2} P\right) d P + \int_ {P _ {2}} ^ {P _ {E} ^ {*}} \left(\alpha_ {1} - \beta_ {1} P\right) d p \quad \text { if } P _ {M} ^ {*} \in R _ {2} \text { and } P _ {E} ^ {*} \in R _ {1}.\tag{37}
$$

Closed-form expressions for the increase in consumers’ surplus can be obtained for all five cases. When $P _ { \mathbf { \Phi } _ { M } } ^ { * } \in R _ { 2 }$ and $P _ { { \cal E } } ^ { * } \in { \cal R } _ { 1 }$

$$
G _ {C S} = \frac {1}{8} \left[ \frac {3 a _ {1} ^ {2}}{b _ {1}} + \frac {4 a _ {2} ^ {2}}{b _ {2}} - \frac {3 (a _ {1} + a _ {2}) ^ {2}}{b _ {1} + b _ {2}} - \frac {2 a _ {2} v}{(1 - r)} + \frac {b _ {2} v ^ {2}}{(1 - r) ^ {2}} \right] \quad \text { if } P _ {M} ^ {*} \in R _ {2} \text { and } P _ {E} ^ {*} \in R _ {1}.\tag{38}
$$

Equation (38) shows that for realistic demand parameters, the increase in consumers surplus due to incorporating piracy is largest when variable unit cost is small (without causing $\boldsymbol { P } _ { M } ^ { * }$ to change regions).

![](/api/attachments/HR4ZTHER/fulltext/images/ec9effc586dfc3d8a3bec16ffd6a08260d5a2b37171d71f8f2c8fbc4a0726c9e.jpg)  
a. $P _ { \ M } ^ { * }$ and $P _ { \phantom { * } _ { E } } ^ { * }$ Are in Different Regions

![](/api/attachments/HR4ZTHER/fulltext/images/889509ededcf95df088fc0a39680294436d58c00f9756988a8c3b05f9b91a7ec.jpg)  
b. $\boldsymbol { P } _ { M } ^ { * }$ and $P _ { \ E } ^ { * }$ Are in the Same Region  
Figure 5. Legitimate Product Sales and Consumers’ Surplus

The change in consumers’ surplus is shown in Figure 5. If the monopolist changes price from $P _ { \phantom { * } E } ^ { * }$ to $P _ { M } ^ { * } ,$ consumers’ surplus increases. Figure 5 shows the increase in surplus when $P _ { \ E } ^ { * }$ and $\boldsymbol { P } _ { M } ^ { * }$ are in same region (Figure 5a) or are in different regions (Figure 5b). The increase in consumers’ surplus from using $P _ { M } ^ { * }$ instead of $P _ { \ E } ^ { * }$ is the sum of areas A and B. The figure shows that not only indifferent consumers’ surplus increases (area A), but ethical consumers’ surplus increases as well (area B).

Consistent with the literature [9, 16], we include consumers’ and monopolist’s surplus in the social welfare function. We also include the creator’s royalty, which is not usually considered in other models. The increase in social welfare due to the consideration of piracy is given by

$$
G _ {S W} = \pi_ {M} ^ {*} + \rho_ {M} ^ {*} + C S _ {M} ^ {*} - \left(\pi_ {E} ^ {*} + \rho_ {E} ^ {*} + C S _ {E} ^ {*}\right).\tag{39}
$$

The exact expression for $G _ { _ { S W } }$ depends on the regions where $\boldsymbol { P } _ { M } ^ { * }$ and $P _ { _ { E } } ^ { * }$ fall. For simplicity, we analyze one case where $P _ { \mathbf { \Phi } _ { M } } ^ { * } \in R _ { 2 }$ and $P _ { \mathrm { ~ } E } ^ { * } \in R _ { 1 }$ , for which the increase in social welfare is

$$
\begin{array}{c} G _ {S W} = \frac {1}{8} \left[ \frac {a _ {1} ^ {2} b _ {2} ^ {2} + a _ {2} ^ {2} b _ {1} (4 b _ {1} + 3 b _ {2}) - 2 a _ {1} a _ {2} b _ {1} b _ {2}}{b _ {1} b _ {2} (b _ {1} + b _ {2})} \right. \\ \left. + \frac {2 a _ {2} (2 r - 3) v}{(1 - r)} - \frac {b _ {2} (4 r - 3) v ^ {2}}{(1 - r) ^ {2}} \right] \quad \text { if } P _ {M} ^ {*} \in R _ {2} \text { and } P _ {E} ^ {*} \in R _ {1}. \end{array}\tag{40}
$$

For small variable unit cost, numerical analysis shows that the increase in social welfare due to incorporating piracy is largest when the creator’s royalty share is small.

The previous numerical examples are analyzed from a social welfare perspective, and the results are summarized in Table 2. $\mathrm { A t } \ \nu = \mathbb { S } 4$ , changing the price from $P _ { \ E } ^ { * }$ to $P _ { M } ^ { * }$ results in \$785,996 and \$1,095,290 increases in social welfare for classical and hip-hop music, respectively. The increase in social welfare is larger for hip-hop music and this increase becomes even larger when $\nu = \$ 0.50$ . For classical music, the change in the distribution channel results in a \$386,320 increase in social welfare compared to a \$2,280,416 increase for hip-hop music. Changing the distribution channel to reduce variable unit cost is more important to increasing social welfare when the pirating segment dominates the market. The largest increase in social welfare occurs when the monopolist incorporates piracy and the pirating and indifferent segments dominate the market for a product with small variable unit cost.

## Conclusion, Limitations, and Suggestions for Future Research

IN THIS PAPER, WE EXAMINED THE PRICING POLICY of a monopolist in a market with piracy. Consumers were divided into three segments based on their affinity toward piracy. The model shows that the monopolist is better off by explicitly considering the existence of piracy. Incorporating piracy causes the monopolist to lower the price to capture more demand from indifferent and pirating consumers. The extent to which piracy affects pricing depends on the relative size and price sensitivity of the three consumer segments. The monopolist’s profits will decrease if he or she ignores piracy in a market dominated by pirating and indifferent consumers. This is especially true when variable unit cost is small. The results are consistent with those of Gopal and Sanders [17], who assert that monopolists will be hardly profitable if they assume a market susceptible to piracy is the same as a market without piracy.

The paper also examined the royalty of the creators of information goods. Royalty may decrease due to two reasons. First, a monopolist incorporating piracy into pricing will set the price above the royalty-maximizing price. Second, if the monopolist ignores piracy, this price will be even farther from the royalty-maximizing price leading to further increase in the loss of royalty. The loss of royalty decreases as variable unit cost decreases.

<table><tr><td rowspan="2">Music type</td><td colspan="2">Cost parameters</td><td colspan="3">Price</td><td colspan="3">Legitimate sales</td><td colspan="3">Social welfare</td></tr><tr><td> $v$ </td><td> $F$ </td><td> $P_{M}^{*}$ </td><td> $P_{E}^{*}$ </td><td> $P_{R}^{*}$ </td><td> $q_{M}^{*}$ </td><td> $q_{E}^{*}$ </td><td> $q_{R}^{*}$ </td><td> $\omega_{M}$ </td><td> $\omega_{E}$ </td><td> $\omega_{R}$ </td></tr><tr><td rowspan="2">Classical</td><td>4</td><td>1,000,000</td><td>20.08</td><td>27.22</td><td>24.23</td><td>109,444</td><td>68,333</td><td>80,368</td><td>2,151,089</td><td>1,365,093</td><td>1,623,177</td></tr><tr><td>0.5</td><td>1,250,000</td><td>18.13</td><td>25.28</td><td>22.29</td><td>123,056</td><td>74,167</td><td>93,980</td><td>2,537,409</td><td>1,504,468</td><td>1,964,267</td></tr><tr><td rowspan="2">Hip-hop</td><td>4</td><td>1,000,000</td><td>17.85</td><td>27.22</td><td>21.57</td><td>107,222</td><td>45,556</td><td>77,470</td><td>1,672,018</td><td>576,728</td><td>1,204,710</td></tr><tr><td>0.5</td><td>1,250,000</td><td>6.88</td><td>25.28</td><td>19.62</td><td>335,278</td><td>49,444</td><td>93,026</td><td>3,952,434</td><td>586,312</td><td>1,538,429</td></tr></table>

<sub>Legiti</sub>m<sup>ate</sup> <sup>Sales</sup> <sup>and</sup> <sup>Social</sup>

Results indicate that there is no single pricing strategy that is best in a given information goods industry. The pricing strategy should be based on the characteristics of consumers for the product. For example, classical music has an older audience than hip-hop music, and action movies draw an audience dominated by young males. These differences indicate differences in piracy within even the same industry and, therefore, imply the need for different pricing strategies within that industry.

Incorporating piracy into pricing results in higher social welfare. In addition to increasing the monopolist’s profit and the creator’s royalty, incorporating piracy increases the number of products sold, which results in greater consumer surplus. The increase in social welfare from incorporating piracy is largest when variable unit cost and creator’s royalty share are small.

The proposed models has several limitations. The model does not consider creator’s revenue from other sources such as live performances, TV performances, advertising, and so on. Increased product diffusion through legitimate sales and piracy will increase the creator’s revenue from these sources [25]. Second, the model does not consider different modes of online distribution. While the client-server mode is the most familiar, P2P networks may provide a distribution alternative [23]. Also, online distribution offers the ability to have a music album unbundled. Traditionally, record labels sold complete albums through retail stores (e.g., Best Buy) or direct channels (e.g., Amazon). Single songs are sold the same way but that practice is limited to popular songs. With increased bandwidth, consumers can download their favorite song or two through online retailers such as iTunes for a fraction of the full album price.

We do not distinguish between types of piracy. Piracy can take place online through file sharing or can be done by burning a CD. The latter requires a blank CD and a CD recorder but may provide better quality [31]. These two types of piracy may have different rates. Since the introduction of file sharing, music CD sales have been on the decline [48], which may indicate increased piracy due to file sharing. In addition, the profile of consumers who use each type of piracy may be different. Also, we assume that the relative distribution of consumers among the three segments is stable over the life of the product. Extensive publicized piracy litigation may cause a temporary or permanent change in the demand functions of the three consumer segments.

There are several areas for future research. One area is the viability of using distribution channels as a way of versioning the product. While Shapiro and Varian [38] suggest using quality to create different versions, versioning may be accomplished by offering the product in traditional physical form or having the product downloaded at different stages of the product life cycle. When downloading, consumers have to use their own storage medium and their copy may be of inferior quality. However, they can obtain such a copy at a significant discount. Although offering this option may cannibalize higher-margin traditional channel sales, there is no research on the extent of this cannibalization. A possible way to avoid the cannibalization is to start offering the traditional physical product only through retailers for a short duration and then make it available online. Early on, price-insensitive consumers will purchase the product, which may reduce the cannibalization caused by the online version.

Acknowledgments: The authors thank three anonymous referees for their helpful suggestions. This research was funded, in part, by a grant from BarclayAmerican Summer Research Award and the Belk College of Business, University of North Carolina–Charlotte.

## REFERENCES

1. Banerjee, D.S. Software piracy: A strategic analysis and policy instruments. International Journal of Industrial Organization, 21, 1 (2003), 97–127.

2. Belleflamme, P. Pricing information goods in the presence of copying. Working Paper no. 463, Department of Economics, Queen Mary University, London, 2002 (available at www .econ.qmul.ac.uk/papers/doc/wp463.pdf).

3. Bhattacharjee, S.; Gopal, R.D.; and Sanders, G.L. Digital music and online sharing: Software piracy 2.0? Communications of the ACM, 46, 7 (2003), 107–111.

4. Bishop, J. Who are the pirates? The politics of piracy, poverty, and greed in a globalized music market. Popular Music and Society, 27, 1 (2004), 101–106.

5. Cachon, G.P., and Lariviere, M.A. Supply chain coordination with revenue-sharing contracts: Strengths and limitations. Management Science, 51, 1 (2005), 30–44.

6. Chellappa, R.K., and Shivendu, S. Economic implications of variable technology standards for movie piracy in a global context. Journal of Management Information Systems, 20, 2 (Fall 2003), 137–168.

7. Chellappa, R.K., and Shivendu. S. Managing piracy: Pricing and sampling strategies for digital experience goods in vertically segmented markets. Information Systems Research, 16, 4 (2005), 400–417.

8. Chen, Y., and Png, I. Software pricing and copyright enforcement: Private profit vis-à- vis social welfare. In P. De and J.I. DeGross (eds.), Proceedings of the Twentieth International Conference on Information Systems. Atlanta: Association for Information Systems, 1999, pp. 119–123.

9. Chen, Y., and Png, I. Information goods pricing and copyright enforcement: Welfare analysis. Information Systems Research, 14, 1 (2003), 107–123.

10. Cheng, H.K.; Sims, R.R.; and Teegen, H. To purchase or to pirate software: An empirical study. Journal of Management Information Systems, 13, 4 (Spring 1997), 49–60.

11. Clemons, E.K.; Gu, B.; and Lang, K.R. Newly vulnerable markets in an age of pure information products: An analysis of online music and online news. Journal of Management Information Systems, 19, 3 (Winter 2002–3), 17–41.

12. Conner, K.R., and Rumelt, R.P. Software piracy: An analysis of protection strategies. Management Science, 37, 2 (1991), 125–139.

13. Dana, J.D., and Spier, K.E. Revenue sharing and vertical control in the video rental industry. Journal of Industrial Economics, 49, 3 (2001), 223–245.

14. Fullerton, S.; Kerch, K.B.; and Dodge, H.R. Consumer ethics: An assessment of individual behavior in the market place. Journal of Business Ethics, 15, 7 (1996), 805–814.

15. Givon, M.; Mahajan, V.; and Muller, E. Software piracy: Estimation of lost sales and the impact on software diffusion. Journal of Marketing, 59, 1 (1995), 29–37.

16. Gopal, R.D., and Sanders, G.L. Preventive and deterrent controls for software piracy. Journal of Management Information Systems, 13, 4 (Spring 1997), 29–47.

17. Gopal, R.D., and Sanders, G.L. International software piracy: Analysis of key issues and impacts. Information Systems Research, 9, 4 (1998), 380–397.

18. Gopal, R.D., and Sanders, G.L. Global software piracy: You can’t get blood out of a turnip. Communications of the ACM, 43, 9 (2000), 83–89.

19. Haruvy, E.; Mahajan, V.; and Prasad, A. The effect of piracy on the market penetration of subscription software. Journal of Business, 77, 2 (2004), S81–S108.

20. Horrigan, J. 55% of adult Internet users have broadband at home or work. Pew Internet & American Life Project, Washington, DC, April 2004 (available at www.pewinternet.org/pdfs/ PIP\_Broadband04.DataMemo.pdf).

21. Hunt, S.D., and Vitell, S.J. A general theory of marketing ethics. Journal of Macromarketing, 6, 1 (1986), 5–16.

22. King, S.P., and Lampe, R. Network externalities, price discrimination and profitable piracy. Information Economics and Policy, 15, 3 (2003), 271–290.

23. Lang, K.R., and Vragov, R. A pricing mechanism for digital content distribution over computer networks. Journal of Management Information Systems, 22, 2 (Fall 2005), 121–139.

24. Liebowitz, S.J. Durability, market structure, and new-used goods models. American Economic Review, 72, 4 (1982), 816–824.

25. Liebowitz, S.J., and Watt, R. How to best ensure remuneration for creators in the market for music? Copyright and its alternatives. Journal of Economic Surveys, 20, 4 (2006), 513–545.

26. Madden, M., and Rainie, L. Music and video downloading moves beyond P2P. Pew Internet & American Life Project, Washington, DC, March 2005 (available at www.pewinternet .org/pdfs/PIP\_Filesharing\_March05.pdf).

27. Nascimento, F., and Vanhonacker, W.R. Optimal strategic pricing of reproducible consumer products. Management Science, 34, 8 (1988), 921–937.

28. Nunes, J.C.; Hsee, C.K.; and Weber, E.U. Why are people so prone to steal software? The effect of cost structure on consumer purchase and payment intentions. Journal of Public Policy & Marketing, 23, 1 (2004), 43–53.

29. Online music report. IFPI, London, January 2004 (available at www.ifpi.org/content/ library/digital-music-report-2004.pdf).

30. Ordover, J.A., and Willig, R.D. On the optimal provision of journals qua sometimes shared goods. American Economic Review, 68, 3 (1978), 324–338.

31. Peitz, M., and Waelbroeck, P. Piracy of digital products: A critical review of the theoretical literature. Information Economics & Policy, 18, 4 (2006), 449–476.

32. Prasad, A., and Mahajan, V. How many pirates should a software firm tolerate? An analysis of piracy protection on the diffusion of software. International Journal of Research in Marketing, 20, 4 (2003), 337–353.

33. Premkumar, G.P. Alternate distribution strategies for digital music. Communications of the ACM, 46, 9 (2003), 89–95.

34. Rainie, L., and Madden, M. Preliminary findings from a Web survey of musicians and songwriters. Pew Internet & American Life Project, Washington, DC, May 2004 (available at www.pewinternet.org/pdfs/PIP\_Musicians\_Prelim\_Findings.pdf).

35. Rainie, L.; Madden, M.; Hess, D.; and Mudd, G. The state of music downloading and filesharing online. Pew Internet & American Life Project and Comscore Media Metrix, Washington, DC, April 2004 (available at www.pewinternet.org/pdfs/PIP\_Filesharing\_April\_04.pdf).

36. Recording Industry Association of America. 2006 year-end statistics: 2006 U.S. manufacturers’ unit shipments and value chart. Washington, DC, 2007 (available at www.riaa. com/keystatistics.php).

37. Roberts, P.F. Viacom, Google in court over YouTube. InfoWorld, 29, 12 (March 19, 2007), 11–12.

38. Shapiro, C., and Varian, H.R. Versioning: The smart way to sell information. Harvard Business Review, 76, 6 (1998), 106–114.

39. Shy, O., and Thisse, J.F. A strategic approach to software protection. Journal of Economics and Management Strategy, 8, 2 (1999), 163–190.

40. Solomon, S.L., and O’Brien, J.A. The effect of demographic factors on attitudes toward software piracy. In R. DeJoie, G. Fowler, and D. Paradice (eds.), Ethical Issues in Information Systems. Boston: Boyd & Fraser Publishing, 1991, pp. 161–181.

41. Sundararajan, A. Managing digital piracy: Pricing and protection. Information Systems Research, 15, 3 (2004), 287–308.

42. Swan, P.L. Alcoa: The influence of recycling on monopoly power. Journal of Political Economy, 88, 1 (1980), 76–99.

43. Takeyama, L. The welfare implications of unauthorized reproduction of intellectual property in the presence of network externalities. Journal of Industrial Economics, 62, 2 (1994), 155–166.

44. Thong, J.Y.L., and Yap, C.S. Testing an ethical decision-making theory: The case of softlifting. Journal of Management Information Systems, 15, 1 (Summer 1998), 213–237.

45. Tirole, J. The Theory of Industrial Organization. Cambridge, MA: MIT Press, 1988.

46. Varian, H.R. Buying, sharing and renting information goods. Journal of Industrial Economics, 48, 4 (2000), 473–488.

47. Vitell, S.J. Consumer ethics research: Review, synthesis and suggestions for the future. Journal of Business Ethics, 43, 1–2 (2003), 33–47.

48. Zentner, A. Measuring the effect of file sharing on music purchases. Journal of Law & Economics, 49, 1 (2006), 63–90.

## Appendix

Lemma 1: $a _ { j } / b _ { j } < \mathrm { a } _ { _ { k } } / \beta _ { _ { k } } f o r k \leq j a n d j = 2 , 3$

Proof: Because $a _ { j } / b _ { j } = P _ { j } , a _ { j } = b _ { j } P _ { j }$ . By Equation (3), $a _ { _ i } > b _ { _ i } P _ { _ j }$ for $i < j .$

Because

$$
\frac {\alpha_ {k}}{\beta_ {k}} = \frac {\sum_ {i = 1} ^ {k} a _ {i}}{\sum_ {i = 1} ^ {k} b _ {i}} = \frac {a _ {1} + \ldots + a _ {k}}{\sum_ {i = 1} ^ {k} b _ {i}} > \frac {b _ {1} P _ {j} + \ldots + b _ {k} P _ {j}}{\sum_ {i = 1} ^ {k} b _ {i}} = P _ {j},
$$

then $\alpha _ { _ k } / \beta _ { _ k } > a _ { _ j } / b _ { _ j } . Q . E . D$

Lemma 2: $\alpha _ { _ { j - l } } / \beta _ { _ { j - l } } > \alpha _ { _ { j } } / \beta _ { _ { j } } f o r j = 2 , 3 .$

Proof: Let $\mathsf { a } _ { { } _ { j - I } } / \beta _ { { } _ { j - I } } = L$ . Then, from Lemma 1, $a _ { _ j } < b _ { _ j } L$

Because

$$
\frac {\alpha_ {j}}{\beta_ {j}} = \frac {\alpha_ {j - 1} + a _ {j}}{\beta_ {j - 1} + b _ {j}} <   \frac {\beta_ {j - 1} L + b _ {j} L}{\beta_ {j - 1} + b _ {j}} = L,
$$

then $\alpha _ { j - I } / \beta _ { j - I } > a _ { j } / b _ { j } . \ Q . E . D$ .

## Proof of Theorem 1

In order to have an optimal price other than that given by Equation (8), $P ^ { * }$ should be at one of the slope change points on the demand function—that is, $P ^ { * } = a _ { j } / b _ { j } , j = 2$ or 3, and

$$
\frac {d \pi_ {j}}{d P} > 0 \text {   at   } P = P ^ {*} \text {   and   } \frac {d \pi_ {j - 1}}{d P} <   0 \text {   at   } P = P ^ {*}.\tag{A1}
$$

Because $d \pi _ { i } / d P$ can be simplified to

$$
\frac {d \pi_ {i}}{d P} = - 2 \beta_ {i} (1 - r) \left(P - P _ {M i} ^ {*}\right)
$$

and

$$
P _ {M i} ^ {*} = \frac {\alpha_ {i} (1 - r) + \beta_ {i} v}{2 \beta_ {i} (1 - r)} = \frac {\alpha_ {i}}{2 \beta_ {i}} + \frac {v}{2 (1 - r)},\tag{A2}
$$

condition (A1) simplifies to $P _ { { \scriptscriptstyle M } ( j - 1 ) } ^ { \ast } < a _ { { \scriptscriptstyle j } } / b _ { { \scriptscriptstyle j } } < P _ { { \scriptscriptstyle M } j } ^ { \ast }$ By Lemma 2, $P _ { M ( j - 1 ) } ^ { * } > P _ { M j } ^ { * }$ , which leads to a contradiction. Q.E.D.

## Proof of Corollary 1

Corollary 1 directly follows from Theorem 1 because the function $\rho$ is a special case of π in which $1 - r$ is replaced with r and $F = \nu = 0 . \mathrm { Q . E . D }$

## Proof of Corollary 2

Because

$$
\pi + \rho = D (P - v - r P) - F + D r P = D (P - v) - F,
$$

ϕ is same as π with $r = 0$ . Therefore, Equation (16) directly follows from Theorem 1. Q.E.D.

## Proof of Theorem 2

The proof is presented in two parts:

(1) When $P _ { o } ^ { * }$ and $\boldsymbol { P } _ { M } ^ { * }$ fall in the same demand function segment and (2) when they fall in different segments (i.e., $R _ { 3 } = [ 0 , P _ { 3 } ] , R _ { 2 } = ( P _ { 1 } , P _ { 2 } ]$ , or $R _ { \scriptscriptstyle 1 } = ( P _ { \scriptscriptstyle 2 } , P _ { \scriptscriptstyle 1 } ) )$ , then by Equations (8) and (13)

$$
P _ {M} ^ {*} = P _ {O} ^ {*} + \frac {\nu}{2 (1 - r)}.\tag{A3}
$$

Because $\nu > 0$ and $r < 1$ , then $P _ { M } ^ { * } > P _ { o } ^ { * } .$

(2) Now suppose $P _ { { M } } ^ { * } < P _ { { O } } ^ { * } , P _ { { O } } ^ { * }$ and $\boldsymbol { P } _ { M } ^ { * }$ are on two different demand function segments that can occur if (a) $P _ { o } ^ { * } = P _ { o 1 } ^ { * } \in R _ { 1 }$ and $P _ { _ M } ^ { ^ * } = P _ { _ { M 2 } } ^ { ^ * } \in R _ { _ 2 } , \left( { \mathfrak { b } } \right) P _ { _ O } ^ { ^ * } = P _ { _ { O 1 } } ^ { ^ * } \in R _ { _ 1 }$ and $P _ { M } ^ { * } =$ $P _ { _ { M 3 } } ^ { ^ { * } } \in R _ { 3 } , \mathrm { o r } \left( \mathrm { c } \right) P _ { _ { O } } ^ { ^ * } = P _ { _ { O 2 } } ^ { ^ * } \in R _ { 2 }$ and $P _ { _ M } ^ { \ast } = P _ { _ M 3 } ^ { \ast } \in \mathbb { R } _ { _ 3 }$

Case (a). If ${ P ^ { * } } _ { o } \in R _ { 1 }$ , then $P _ { M 1 } ^ { * }$ which is greater than $P _ { o 1 } ^ { * }$ , must be a valid solution in $R _ { \mathfrak { r } }$ . Because $P _ { { M } } ^ { * } = P _ { { M } 2 } ^ { * }$ , the following inequality holds:

$$
\pi_ {2} ^ {*} - \pi_ {1} ^ {*} > 0,\tag{A4}
$$

where $\pi _ { i } ^ { * }$ is the profit-maximizing solution with demand parameters $\mathbf { \alpha } _ { a }$ and $\beta _ { i }$ . Using Equation (6):

$$
\pi_ {2} ^ {*} - \pi_ {1} ^ {*} = \frac {1}{4} \left[ - \frac {\left(a _ {2} (2 a _ {i} + a _ {2}) b _ {1} - a _ {1} ^ {2} b _ {2}\right) (1 - r)}{b _ {1} (b _ {1} + b _ {2})} - 2 b _ {2} v \left(\frac {a _ {2}}{b _ {2}} - \frac {v}{2 (1 - r)}\right) \right].\tag{A5}
$$

Because $P _ { M 2 } ^ { * } \in R _ { 2 }$

![](/api/attachments/HR4ZTHER/fulltext/images/a0f58f98297a910b509f846384a73b4c4bf7a2f52295fc82ffbb174a5372dd89.jpg)  
Figure A1. Two Royalty Functions $( \mathsf { p } _ { 2 } , \mathsf { p } _ { 3 } )$ in $R _ { 3 }$

$$
P _ {M 2} ^ {*} = \frac {\alpha_ {2}}{2 \beta_ {2}} + \frac {v}{2 (1 - r)} \leq \frac {a _ {2}}{b _ {2}} \Rightarrow 0 <   \frac {\alpha_ {2}}{2 \beta_ {2}} \leq \frac {a _ {2}}{b _ {2}} + \frac {v}{2 (1 - r)}.\tag{A6}
$$

This implies that the second term inside the brackets in Equation (A5) is negative. Therefore, showing that the first term inside the brackets is negative will lead to a contradiction with inequality (A4). This is shown in three parts:

(a)(i) Suppose $P _ { o 2 } ^ { * } \in R _ { 2 } .$ . Because $\boldsymbol { P } _ { o } ^ { * } = \boldsymbol { P } _ { o 1 } ^ { * }$ , then $\rho _ { 1 } ^ { * } > \rho _ { 2 } ^ { * } ,$ , where $\boldsymbol { \rho } _ { i } ^ { * }$ is the royaltymaximizing solution with demand parameters $\mathrm { \bf q } _ { i }$ and $\beta _ { i }$ . Using Equation (11) to find $\boldsymbol { \rho } _ { 1 } ^ { * } - \boldsymbol { \rho } _ { 2 } ^ { * }$ and simplifying it gives

$$
\rho_ {1} ^ {*} - \rho_ {2} ^ {*} = \frac {1}{4} r \left[ \frac {\left(a _ {2} \left(2 a _ {1} + a _ {2}\right) b _ {1} - a _ {1} ^ {2} b _ {2}\right)}{b _ {1} \left(b _ {1} + b _ {2}\right)} \right] > 0.\tag{A7}
$$

Thus, the first term in Equation (A5) is also negative, therefore leading to a contradiction with $\pi _ { \gamma } ^ { * } - \pi _ { 1 } ^ { * } > 0$

(a)(ii) If $P _ { o 2 } ^ { * } \in R _ { 1 }$ , then $P _ { M 2 } ^ { * }$ must be in $R _ { _ 1 }$ because $P _ { M 2 } ^ { * } > P _ { O 2 } ^ { * }$ . This contradicts $P _ { \ M } ^ { * } =$ $P _ { { M } ^ { 2 } } ^ { * } \in R _ { 2 }$

(a)(iii) If $P _ { o 2 } ^ { * } \in R _ { 3 }$ , the same contradiction with $\pi _ { 2 } ^ { * } > \pi _ { 1 } ^ { * }$ occurs as in case (a)(i) because $\rho _ { 1 } ^ { * } > \rho _ { 2 } ^ { * }$ can also be shown. Using Equation (11)

$$
\rho_ {3} - \rho_ {2} = r (a _ {3} - b _ {3} P) P > 0\tag{A8}
$$

for all $P \in R _ { * }$ as is shown in Figure A1. By Lemma 2, $P _ { O 3 } ^ { * } < P _ { O 2 } ^ { * } ,$ and hence $P _ { O 3 } ^ { * } \in R _ { 3 }$ Furthermore, $\boldsymbol { \rho } _ { 3 } ^ { * }$ is larger than any $\rho _ { 3 }$ for $P \in R _ { * }$ . Together with Equation (A8), this implies that $\boldsymbol { \rho } _ { 3 } ^ { * } > \boldsymbol { \rho } _ { 2 } ^ { * }$ . Because $P _ { o } ^ { * } = P _ { o 1 } ^ { * } \in R _ { 1 } , \rho _ { 1 } ^ { * }$ is greater than any valid ${ \boldsymbol \rho } _ { i } ^ { * }$ , which leads to $\boldsymbol { \rho } _ { 1 } ^ { * } > \boldsymbol { \rho } _ { 3 } ^ { * }$ . Therefore, $\boldsymbol { \rho } _ { 1 } ^ { \ast } > \boldsymbol { \rho } _ { 3 } ^ { \ast } > \boldsymbol { \rho } _ { 2 } ^ { \ast } ,$ which implies $\rho _ { 1 } ^ { * } > \rho _ { 2 } ^ { * } .$ . This contradicts $\pi _ { 2 } ^ { * } > \pi _ { 1 } ^ { * }$ We showed that every possible range of $P _ { o 2 } ^ { * } ( R _ { 1 } , R _ { 2 }$ , and $R _ { * } )$ leads to the contradiction for case (a). Similar arguments can be constructed for cases (b) and (c). Q.E.D.

## Proof of Theorem 3

Let $P _ { \ E } ^ { * }$ be the optimal price when all consumers are assumed to behave ethically. Using the demand function in Equation (21), the optimal price $P _ { \ E } ^ { * }$ is given as Equation (22). By Lemma 2

$$
\frac {a _ {1}}{2 b _ {1}} = \frac {\alpha_ {1}}{2 \beta_ {1}} > \frac {\alpha_ {2}}{2 \beta_ {2}} > \frac {\alpha_ {3}}{2 \beta_ {3}}.\tag{A9}
$$

Let $R _ { \mathfrak { r } }$ be the region where the true optimal price falls. From Equations (A9) and (8), $P _ { _ { E } } ^ { * } { > } P _ { _ { M } } ^ { * } \mathrm { i f } i { > } 1$ and $P _ { _ { E } } ^ { * } = P _ { _ { M i } } ^ { * } \mathrm { i f } i = 1 . \mathrm { Q . E . D }$
