---
otero_id: 13534
otero_key: "YZQ3JWDU"
title: "Risk of using pirated software and its impact on software protection strategies"
authors: "Samuel Shu Kin Kwan; Jeevan Jaisingh; Kar Yan Tam"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.06.014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Risk of using pirated software and its impact on software protection strategies

Samuel Shu Kin Kwan <sup>⁎</sup>, Jeevan Jaisingh, Kar Yan Tam

Department of Information and Systems Management, Hong Kong University of Science and Technology, Hong Kong

Available online 23 June 2007

## Abstract

The software protection strategy of software developer and the inherent risk to end user in using pirated software are two major factors that affect a user's decision on whether to purchase or pirate a software product. This paper analyzes the optimal protection strategy for software developer in horizontally and vertically differentiated markets. We find that the implementation cost of software protection constitutes the primary factor for software developers to determine their software protection strategies However, in a vertically differentiated market, the lower quality product should always adopt a non-protection strategy, regardless of the protection implementation cost. In other cases, protection would only be optimal if the protection implementation cost to the software developer is relatively small. These findings are consistent with anecdotal evidence. © 2007 Elsevier B.V. All rights reserved.

Keywords: Software piracy; Software protection strategy; Horizontal differentiation; Vertical differentiation

## 1. Introduction

According to a global report by Business Software Alliance [2], the software industry is said to have lost more than \$13.08 billion in business during the year 2002 due to software piracy. It remains to be one of the most well known and persistent problems of the IT industry. It is estimated that an average of 39% of all software installed in 2002 were pirated versions [2]. In fact, the situation is deteriorating with the rapid and pervasive application of IT in the modern society.

At the first glance, one may perceive software piracy as just another example of the illegal duplication of other intellectual properties like books, journals, or media contents. However, there are at least two factors that make software piracy a unique type of problem in itself. Firstly, software developers are able to implement protection codes or mechanisms that can effectively and significantly increase the difficulty to pirate. Such measures are usually not available to publishers and producers. The protection of software products can range from the use of hardware “dongles” to just requiring the user to enter a cryptic product key code. Although one may argue that these schemes are usually not unbreakable, they increase the cost for pirates to use illegal copies of software. Of course, the software developer would also need to pay a certain implementation cost for this type of software protection mechanisms. Secondly, there are inherent risks in using pirated software. These risks are unique to the software industry and make software piracy quite different from other forms of illegal duplication of intellectual properties. For instance, due to the unlawful nature of piracy, the quality of pirated software can never be guaranteed. Very often the pirated software would have already been infected with malicious computer virus before it arrives at the hands of the end user.

Also, software is seldom free of defects. Some defects not only result in malfunctioning of the software but also leave “vulnerabilities” for malicious computer hackers to exploit. Very often these defects would only be discovered after the consumer has purchased and used the software for a certain period of time. It is a common practice for software developers to provide post-sale technical support to the legitimate users should there be any subsequent problems. While these types of technical support may exist in a variety of forms, ranging from security patches, features updates, to email or even telephone support, they are usually available only to the paying consumers but not to the pirates. Users of pirated software are at their own risk. It is reasonable to assume that some people would be deterred from pirating in view of this risk.

Cheng et al. [3] attempted to exhaustively enlist the reasons behind people's software purchasing or pirating decisions in an empirical study. In particular, they found “technical support in case of problems” as well as “worry about computer viruses” to be among the ten most important reasons for people to purchase, rather than pirate software.

In the Internet age, the risk of using vulnerable software cannot be overemphasized. The US-CERT Vulnerability Notes Database [9] lists many popular software products that contain critical security vulnerabilities. For example, the various “buffer overrun” vulnerabilities that exist in the popular Oracle 9i product would require software updates available only to registered users. In principle, users of pirated copies of Oracle 9i would have to bear the risk of future attacks exploiting these vulnerabilities, especially if their systems are connected to the Internet. The risk in using pirated software became quite apparent in the recent “Blaster” attack. “Blaster” was an Internet virus that exploited a known vulnerability of the Windows XP software. A timely patch to this vulnerability was actually released by the vendor but was made available only to registered customers. As a result, machines running pirated copies of Windows XP were forced to disconnect from the Internet to prevent from getting exposed to the virus attack.

To summarize, both the software protection mechanism and the risk in using pirated software serve to reduce piracy. The former is mainly a preventive measure that is available to the software developer who needs to weigh the cost and benefit before deciding on what type of protection mechanism, if any, should be adopted. The latter can be considered as a deterrent which means that it is beyond the control of any single party. The effect of risk may depend on a number of factors such as the chance of virus infection through the use of pirated software, the ultimate reliability of the software product,<sup>1</sup> etc. In this paper, we attempt to study the optimal protection strategies for software firms in a duopoly software market, with the explicit consideration of the potential risk in using pirated software due to the lack of technical support. We develop an analytic model that assumes that people can overcome the software protection by bearing a cost of pirating. Users are heterogeneous in the cost of pirating. We will also model the risk in using pirated software in our framework.

We consider a duopoly market under two forms of product differentiation: horizontal and vertical [8]. By horizontal differentiation, we mean that software firms compete with each other by designing features that are unique from its competitor. On the other hand, in a vertically differentiated market, firms compete in the quality of their products. Our main objective is to analyze the optimal protection strategies for software firms under each situation. The rest of the paper is organized as follows: To begin with, we will examine the relevant prior research in the area of software piracy first. We will then develop an analytical model conforming to our observations mentioned above. In particular, we will analyze the problem using two well known market competition paradigms, namely the horizontally differentiated market and the vertically differentiated one.

## 2. Background literature

Intuitively thinking, the existence of piracy should reduce demand and thus profit. It follows that the best strategy for software firms would be to increase the protection level as much as possible so that potential pirates would simply find it very costly to pirate. However, Conner and Rumelt [4] argue that by taking into account the effect of network externalities, as commonly found in software products, a high level of protection may not be optimal for firms. They show that in a monopoly setting, raising software protection would be profit-maximizing only when there is only insignificant effect of network externalities. Otherwise, profit would decrease with an increased protection level because some would-be pirates are forced to do without the software, rather than buying it. However, the model used does not consider strategic interactions in a competitive market as well as the inherent risk in using pirated software.

The work by Shy and Thisse [7] further develops the analysis of optimal software protection strategy by the use of a horizontally differentiated duopoly model. Their findings are similar to those by Conner and Rumelt in that when externalities effects are strong, nonprotection would be optimal for competing software firms. Their model assumes dichotomization in two dimensions. Firstly, consumers are dichotomized into support-oriented or support-independent ones. Supportoriented users choose to buy rather than pirate if the price of software is less than the utility they derive from the support service. Secondly, rather than treating the level of protection level as a continuous variable, firm's protection strategies are dichotomized into either full protection or nil protection. This conforms to the reality in that software products usually come only with a simple protection mechanism that checks for a valid product key, or are just completely unprotected.

However, their model also assumes that end users would have no way to use pirated software if software protection is in place. Unfortunately this is often not true in real life. In fact, end users can usually obtain pirated software with protection mechanism already compromised. Also, most of the time software is only protected by a product key code that can be easily duplicated. Therefore, we believe that it should be more realistic to assume that people can still pirate even though a software product is protected, only that they would need to pay a cost of pirating. The cost for pirating can differ by individual but in general should be small compared with the price of software.

The dichotomization of support-oriented and support-independent consumers does not fully represent the inherent risk in using pirated software as discussed previously. In Shy and Thisse's model, technical support only brings a fixed amount of utility to support-oriented users. However, we believe the lack of technical support would introduce a risk that essentially discounts, in the sense of expected utility, the benefits derivable from using the pirated software.

The concept of risk in using pirated software was first used by Banerjee [1] in his analysis of the software piracy problem from the perspective of social welfare and government policy. In his model, end user simply cannot be certain that a piece of software obtained from illegal sources would indeed work as expected. However, his focus was mainly on governmental monitoring of counterfeiting business.

We believe that the concept of risk is not only applicable to cases when end user purchase software from pirates, but also to cases when end users make illegal copies of licensed software themselves. In fact, as pointed out earlier, the study by Cheng et al. [3] reveals that there are other risks in using pirated software, such as the lack of technical support in case of problems and computer viruses. In the following, market competition, dichotomization of software protection level, as well as the risk in using pirated software will be incorporated into our analytical model.

## 3. Horizontal differentiation

We start with the horizontally differentiated market setting. Namely, we consider the case when competing software firms aim at the same application area (e.g. symbolic computation, graphics design, web authoring, etc.) but produce software with features differentiated from each other. Moreover, each consumer would value each of these differentiated features differently.

For example, consider the desktop operating systems provided by Apple Computer and that by Microsoft. Both operating systems are designed to provide an easyto-use graphical user interface for end users to manage their personal computers. However, some of the features they provide are unique from each other and these differentiated features are valued differently by different camps of consumers.

For simplicity, we model the market as a duopoly and represent the heterogeneity in consumers' preferences for the two different software products using the “linear city” model [6]. In the real software market, very often there would be an innovator firm at the beginning, followed by a number of other software developers who believe it would be profitable to sell similar products in the same application area. However, due to fierce market competition among software developers, usually only a few major players might remain when the market becomes stable. Such a phenomenon of market consolidation can be found in many application areas such as productivity tools, graphics packages, etc. We thus believe that our duopoly model represents an acceptable approximation of reality. We denote the two competing products software 1 (sw ) and software 2 (sw ) respectively.

## 3.1. The firms

Before the software is actually developed, the firm would decide on whether to implement any protection mechanism against unauthorized copying. As discussed earlier, a dichotomization of protection strategy should be more appropriate than a continuous level of protection because software products nowadays are usually shipped with protection by simple product key code checking, or without any protection at all. We denote their decisions on protection strategies by $\eta _ { i } \in \{ 0 , 1 \}$ $( i { = } 1 , 2 )$ where $\eta _ { i } { = } 0$ means firm i has chosen not to implement protection. However, if a firm chooses to implement protection $( \eta _ { i } = 1 )$ , an implementation cost k would be incurred.

Once the firms decide on their protection strategies, they also need to decide the selling price of their software $P _ { i } \left( i \mathrm { = } 1 , 2 \right)$ . It is assumed that firms would act rationally and choose their respective optimal prices to maximize their own profits. Assuming a zero marginal cost of production for simplicity, the profit of a firm is given by:

$$
\pi_ {i} = p _ {i} d _ {i} - k \eta_ {i}\tag{1}
$$

where $d _ { i }$ denotes the demand of the software in concern. In order to determine the optimal price, a firm needs to anticipate the possible reactions of both its competitor and the potential consumers, as detailed in the following.

## 3.2. The consumers

We will assume full participation by consumers in that all consumers either buy or pirate one of the software. There are two main factors, namely benefit and cost, affecting the utility a consumer may derive from using a piece of software:

## 3.2.1. Benefit

The benefit of software would depend on the intrinsic quality of it as well as how its features match the preferences of the user. A piece of software that is highly regarded by one user may not appear to be that useful to another. In our model for horizontally differentiated market, the intrinsic software quality is assumed to be the same for both firms and is denoted by q. On the other hand, consumers are ranked by their preferences of sw to ${ \mathrm { \bf S W } } _ { 2 } ,$ with their relative preference positions denoted by $x \in [ 0 , 1 ]$ . Namely, a consumer with a smaller x would prefer $\mathbf { S } \mathbf { W } _ { 1 }$ more to sw . Considering the deterioration in benefit due to preference mismatch, we model the benefit of $\mathbf { S } \mathbf { W } _ { 1 }$ to a consumer at position x by $q - t x$ where t denotes the benefit degradation factor (i.e. the “transportation cost”) due to preference mismatch. Similarly, the benefit of $\mathbf { S } \mathbf { W } _ { 2 }$ would be $q - t ( 1 - x )$ to the same consumer.

## 3.2.2. Cost

The cost would simply be the selling price of the software in case a consumer purchases it. Prices are denoted by $p _ { 1 }$ and $p _ { 2 }$ for $\mathbf { S } \mathbf { W } _ { 1 }$ and $\mathbf { S } \mathbf { W } _ { 2 }$ respectively. In the case of pirating protected software, a cost for pirating would also be incurred. It is assumed that this cost would depend on individual's characteristics (e.g. technical know-how, available resources for pirating, etc.) but would be more or less similar across different target software to be pirated. As such, the consumer's cost for pirating is modeled to be heterogeneous among consumers but the same for both $\mathbf { S } \mathbf { W } _ { 1 }$ and $\mathrm { \bf S W } _ { 2 } .$ For simplicity, we define the cost for pirating as τz where τ is the homogeneous scaling factor of piracy costs while $z \in [ 0 , 1 ]$ denotes the consumer's heterogeneity in pirating protected software. Essentially, some consumers pay a higher cost than others to pirate a piece of protected software.

As a result, the utility $U _ { b 1 }$ and $U _ { b 2 }$ derived from purchasing sw and $\mathbf { S } \mathbf { W } _ { 2 }$ would be:

$$
U _ {b 1} = q - t x - p _ {1}\tag{2}
$$

$$
U _ {b 2} = q - t (1 - x) - p _ {2}\tag{3}
$$

As mentioned before, users of pirated software are all subject to risk. We may express this risk factor by the expected benefit of using a pirated software copy. Assuming a risk factor of $\phi \in ( 0 , 1 )$ , the utility $U _ { p 1 }$ and $U _ { p 2 }$ for pirating $\mathbf { S } \mathbf { W } _ { 1 }$ and $\mathbf { S } \mathbf { W } _ { 2 }$ would respectively be:

$$
U _ {p 1} = (1 - \phi) (q - t x) - \tau z \eta_ {1}\tag{4}
$$

$$
U _ {p 2} = (1 - \phi) (q - t (1 - x)) - \tau z \eta_ {2}\tag{5}
$$

Namely, $1 - \phi$ is the probability that the pirated software would work perfectly.

## 3.3. The market

Having introduced the essential characteristics of software firms and consumers, we are about to incorporate the two in a competitive market. Namely, we consider a competitive market in a three-stage noncooperative game. In stage 1, software firms set their respective protection strategies $( \eta _ { 1 } , \eta _ { 2 } )$ . In stage 2, firms determine their optimal prices $( p _ { 1 } , p _ { 2 } )$ with the expectation that their profits would be maximized. Lastly in stage 3, consumers choose whether to buy or pirate either one of the software so as to maximize their utilities. The game, in its extensive form, can be illustrated in the following game tree (Fig. 1):

We will study the problem using the Sub-game Perfect Nash Equilibrium (SPNE) concept. That is, both firms would first anticipate the utility-maximizing decisions of consumers that would happen at stage 3. Based on this anticipation and also considering the profitmaximizing behavior of its competitor, a firm determines its profit-maximizing price under the 4 possible protection strategies, namely $( \eta _ { 1 } = 1 , \eta _ { 2 } = 1 ) , ~ ( \eta _ { 1 } = 1 , \eta _ { 2 } = 0 ) , ~ ( \eta _ { 1 } = 0 ,$ $\eta _ { 2 } = 1 )$ and $( \eta _ { 1 } = 0 , \eta _ { 2 } = 0 )$ . Lastly, by comparing the maximized profits at each different protection strategy, the two firms set their optimal protection strategies at stage 1 based on the Nash Equilibrium concept. Before proceeding with the analysis, the utility function of the consumer is restated as follows:

![](/api/attachments/YZQ3JWDU/fulltext/images/fd96cc2b71037f16a8a30310cd9c121055bcf14b34b85ae35de69053037d34db.jpg)  
Fig. 1. Game tree.

$$
U = \left\{ \begin{array}{l l} q - t x - p _ {1} & \text { if   buy   sw_{1 }} \\ (1 - \phi) (q - t x) - \tau z \eta_ {1} & \text { if   pirate   sw_{1 }} \\ q - t (1 - x) - p _ {2} & \text { if   buy   sw_{2}} \\ (1 - \phi) (q - t (1 - x)) - \tau z \eta_ {2} & \text { if   pirate   sw_{2}} \end{array} \right.\tag{6}
$$

while the profit functions of the two firms are given by:

$$
\begin{array}{l} \pi_ {1} = p _ {1} d _ {1} - k \eta_ {1} \\ \pi_ {2} = p _ {2} d _ {2} - k \eta_ {2} \end{array}\tag{7}
$$

One may easily note from Eqs. (6) and (7) the dynamics of such a market. Firstly, by setting protection level and price, a firm is affecting the decisions of consumers on whether to buy or pirate $\mathbf { S } \mathbf { W } _ { 1 }$ or $\mathrm { \bf S W } _ { 2 } .$ . Such decisions would in turn affect the demands for $\mathbf { S } \mathbf { W } _ { 1 }$ and $\mathbf { S } \mathbf { W } _ { 2 }$ . Finally, the profits of firms are actually determined by the demands for their software, as can be seen from Eq. (7). To continue our analysis, we will first study the demands for $\mathbf { S } \mathbf { W } _ { 1 }$ and $\mathbf { S } \mathbf { W } _ { 2 }$ that result from the utilitymaximizing behavior of consumers.

## 3.4. Demand and profit at equilibrium

We will consider the demand of $\mathbf { S } \mathbf { W } _ { 1 }$ first. To start with, let us focus on the effect of x on the consumer's utility and leave the effect of z alone for the time being. Fig. 2 shows the utility functions for purchasing and for pirating $\mathbf { S } \mathbf { W } _ { 1 }$ at each fixed value of z. Firstly, all utility functions of the consumer are linear in x. For $\mathbf { S } \mathbf { W } _ { 1 }$ , the utilities of the two choices (i.e. buying or pirating) would simply be represented by the two downward-sloping straight lines $U _ { b 1 }$ and $U _ { p 1 }$ . In particular, the slope for buying is −t whereas that for pirating is $- ( 1 - \phi ) t . \mathrm { A s } \phi$ must be within the interval (0,1), $U _ { b 1 }$ would always be steeper than $U _ { p 1 }$ . From Fig. 2, it can be easily seen that consumers in the range $( 0 , x _ { b 1 p 1 } )$ would prefer buying to pirating $\mathbf { S } \mathbf { W } _ { 1 }$ . while those in the range $( x _ { b 1 p i } , 1 )$ would prefer pirating to buying.

![](/api/attachments/YZQ3JWDU/fulltext/images/d4c1e21203d6943cb0639b339988ec395f1efb1e194ebecfe2095431cd22c2c9.jpg)  
Fig. 2. Utilities of buying and pirating sw .

We can now consider the effect of z on the demand. It can be seen from Eq. (6) that different values of z would result in different intercepts of the pirating utility, as shown in Fig. 3. Note that the intersection point $x _ { b 1 p 1 }$ would also be changing with $z .$ Considering $z ,$ the indifference point $x _ { b 1 p 1 }$ becomes a line of indifference between buying and pirating $\mathbf { S } \mathbf { W } _ { 1 }$ . The consumer's utility functions $U _ { b 1 }$ and $U _ { p 1 }$ become 2-dimensional planes in the 3-dimensional space of $( U , x , z )$ . The demand for $\mathbf { S } \mathbf { W } _ { 1 }$ is simply the projection, on the (x,z) plane, of the region where the plane $U _ { b 1 }$ is the highest. Essentially this area is outlined by the indifference line $x _ { b 1 p 1 }$ with respect to z within the interval $z \in [ 0 , 1 ]$

More generally, we can derive the utility-maximizing demands for software from the appropriate lines of indifference, as will be shown later. It should be noted that $U _ { b 1 }$ and $U _ { p 1 }$ may not necessarily intersect within the interval of $x { = } ( 0 , 1 )$ . This could happen when the vertical intercept of $U _ { p 1 }$ is larger than that of $U _ { b 1 }$ , and in this case pirating would always undercut buying. We would not further analyze this case because the firm will doubtlessly need to lower its price or abandon the market as no consumer is buying the product. On the other hand, $U _ { b 1 }$ and $U _ { p 1 }$ would also not intersect when the value of $U _ { p 1 }$ is smaller than that of $U _ { b 1 }$ when $x = 1$ In this case, buying would always undercut pirating. Again, we would not further analyze this case because there is actually no issue of piracy under such a situation. We may now consider the situation when $\mathbf { S } \mathbf { W } _ { 2 }$ also put in the picture. Considering the 2-dimensional space of $( U , x )$ , the utility functions $U _ { b 2 }$ and $U _ { p 2 }$ would simply be two lines having slopes t and $( 1 - \phi )$ t respectively, as shown in Fig. 4.

![](/api/attachments/YZQ3JWDU/fulltext/images/f5a7e299ec3262ffa22f796cf13d49787497ff57848b8d034eb05c83f1611c9f.jpg)  
Fig. 3. Effect of z on demand.

![](/api/attachments/YZQ3JWDU/fulltext/images/f396704f60c9442a51c305d44c7f794e4d387d44765f1c035cb4050d8d132b21.jpg)  
Fig. 4. Utilities of buying and pirating (horizontal differentiation).

We are only interested in the situation when there are non-zero portions of users buying and pirating $\mathbf { S } \mathbf { W } _ { 1 }$ or $\mathbf { S W } _ { 2 } .$ This is equivalent to the following assumption that posits the relations among the intersecting points:

$$
1 > x _ {b 2 p 2} > \mathrm{x} _ {p 1 p 2} > x _ {b 1 p 1} > 0 \forall z \in [ 1, 0 ]\tag{C1}
$$

Now we can consider the 3-dimensional space of $( U ,$ $^ { \dag , z ) }$ . As explained previously, the demands for $\mathbf { S } \mathbf { W } _ { 1 }$ and $\mathbf { S } \mathbf { W } _ { 2 }$ can be derived from the indifference lines $x _ { b 1 p 1 }$ and $x _ { b 2 p 1 }$ . In other words, the demands would simply be the projections on the $^ { ( x , z ) }$ plane as shown in Fig. 5. Based on the utility functions of the consumer as given by Eq. (6), the demands for $\mathbf { S } \mathbf { W } _ { 1 }$ and $\mathbf { S } \mathbf { W } _ { 2 }$ are:

$$
d _ {1} = \int_ {0} ^ {1} x _ {b 1 p 1} \mathrm{d} z = \frac {1}{2} \frac {\tau \eta_ {1} - 2 p _ {1} + 2 q \phi}{t \phi}\tag{8}
$$

$$
d _ {2} = 1 - \int_ {0} ^ {1} x _ {b 2 p 2} \mathrm{d} z = 1 + \frac {1}{2} \frac {\tau \eta_ {2} - 2 p _ {2} + 2 q \phi - 2 t \phi}{t \phi}\tag{9}
$$

That is, the utility-maximizing demands are now entirely in terms of other model parameters, namely the exogenous $q , \phi ,$ t and τ as well as the endogenous $p _ { 1 } , p _ { 2 } ,$ $\eta _ { 1 }$ and $\eta _ { 2 } .$ . Similarly, by substituting the anticipated secondstage demands into Eq. (7), the firms' profit functions $\pi _ { 1 }$ and $\pi _ { 2 }$ can be expressed entirely in terms of the exogenous q, ϕ, t, τ and k as well as the endogenous $p _ { 1 } , p _ { 2 } , \eta _ { 1 }$ and $\eta _ { 2 } .$

![](/api/attachments/YZQ3JWDU/fulltext/images/5ab7f75a21ec0fe9590ecc92599376bdf359a3d07abecae2918f34a639239242.jpg)  
Fig. 5. Demand (horizontal differentiation).

Since firms need to determine optimal prices to maximize their profits, their problems would be:

$$
\begin{array}{l} \max _ {p _ {1}} \pi_ {1} = \max _ {p _ {1}} p _ {1} d _ {1} - k \eta_ {1} \\ = \max _ {p _ {1}} \left(\frac {1}{2} \frac {\tau \eta_ {1} - 2 p _ {1} + 2 q \phi}{t \phi}\right) p _ {1} - k \eta_ {1} \end{array}\tag{10}
$$

$$
\begin{array}{l} \max _ {p _ {2}} \pi_ {2} = \max _ {p _ {2}} p _ {2} d _ {2} - k \eta_ {2} \\ = \max _ {p _ {2}} \left(1 + \frac {1}{2} \frac {\tau \eta_ {2} - 2 p _ {2} + 2 q \phi - 2 t \phi}{t \phi}\right) p _ {2} - k \eta_ {2} \end{array}\tag{11}
$$

Proposition 1. In a horizontally differentiated software market, protection would be optimal for both firms only if $k { < } \frac { \tau ( \tau { + } 4 q \phi ) } { 1 6 t \phi }$ . Otherwise, non-protection would be <sup>/</sup>optimal for both firms.

The Proof of Proposition 1 is shown in the Appendix. We denote the critical value of the protection cost k by $\begin{array} { r } { k ^ { * } = \frac { \tau ( \tau + 4 q \phi ) } { 1 6 t \phi } } \end{array}$ . Note that $k ^ { * }$ is increasing in τ, the pirating <sup>/</sup>cost. Protection would be optimal only if the protection cost is below $k ^ { * }$ which mainly consists of a square term of the

## 4. Vertical differentiation

pirating cost τ of the consumer. This suggests that firms should prefer only a very simple and low-cost protection mechanism or no protection at all.

As shown in the Appendix, the optimal prices, demands and profits of both firm should be symmetrical if they adopt the same protection strategy. In case of protection, the optimal price, demand and profit should be $\begin{array} { r } { p _ { 1 } ^ { * } = p _ { 2 } ^ { * } = \frac { \dot { \tau } + 2 q \phi } { 4 } , \dot { d _ { 1 } ^ { * } } = d _ { 2 } ^ { * } = \frac { \tau + 2 q \phi } { 4 t \phi } } \end{array}$ and $\pi _ { 1 } ^ { * } = \pi _ { 2 } ^ { * } =$ $\frac { \bar { \tau } ^ { 2 } + 4 \bar { \tau } \dot { q } \phi + 4 q ^ { 2 } \bar { \phi } ^ { 2 } - 1 6 k t \dot { \phi } } { 1 6 t \phi }$ respectively. In case of non-protection, <sup>/</sup>the optimal price, demand and profit would be $\bar { p _ { 1 } ^ { * } } = p _ { 2 } ^ { * } =$ $\begin{array} { r } { \frac { q \phi } { 2 } , \dot { d } _ { 1 } ^ { * } = \dot { d } _ { 2 } ^ { * } = \frac { q } { 2 t } } \end{array}$ and $\begin{array} { r } { \pi _ { 1 } ^ { * } = \pi _ { 2 } ^ { * } = \frac { q ^ { 2 } \phi } { 4 t } } \end{array}$ respectively.

<sup>p p</sup>It follows that the optimal profit is increasing in $q$ but decreasing t in, regardless of whether protection is in place or not. Namely, optimal profit increases when software is of higher quality but decreases when the negative effect of preference mismatch (i.e. the transportation cost) is high. Also, when protection is in place, the optimal profit is also increasing in τ, the pirating cost on the consumer side. These very much conform to intuition.

Comparing the optimal prices and demands for protection and non-protection, it can be seen that the optimal prices and demands for non-protection would always be lower than those for protection. In this sense, the protection cost contributes as the major determining factor for firms to adopt protection. On the other hand, the effects of risk $( \mathrm { i . e . } \phi )$ on the optimal price, demand as well as profit are summarized in the following table of comparative statics:

<table><tr><td></td><td> $\frac{\partial p_1^*}{\partial \phi}$ </td><td> $\frac{\partial p_2^*}{\partial \phi}$ </td><td> $\frac{\partial d_1^*}{\partial \phi}$ </td><td> $\frac{\partial d_2^*}{\partial \phi}$ </td><td> $\frac{\partial \pi_1^*}{\partial \phi}$ </td><td> $\frac{\partial \pi_2^*}{\partial \phi}$ </td></tr><tr><td>Both protect</td><td>+</td><td>+</td><td>-</td><td>-</td><td>+’</td><td>+’</td></tr><tr><td>Both not protect</td><td>+</td><td>+</td><td>0</td><td>0</td><td>+</td><td>+</td></tr></table>

+′: positive if τ b 2qϕ.

In general, optimal prices and profits should increase with risk $\cdot ^ { 2 }$ It is also interesting to note that the optimal demands would decrease with risk in case of protection. The intuition behind is that if the software is protected and the risk becomes higher, the firm can charge a higher price and reap a higher profit, although there are actually less buying consumers.

Having considered the case of horizontally differentiated market, we now consider the case when software products are vertically differentiated. By vertical differentiation, we mean that software products compete in quality. In general, the higher quality firm can sell at a higher price and also the preference for quality is assumed to be different across different consumers.

Vertical differentiation is indeed quite common in the software industry. Many popular software magazines and download sites (e.g. PC Magazine, Bytes, download.com, zdnet.com, etc.) offer ratings of software products in terms of a common set of criteria such as ease-of-use, functionalities, etc. to assist consumers in making their purchasing decisions.

The main difference from the analysis of horizontal differentiation would be in the formulation of the consumer's utility functions. Namely, we denote the intrinsic qualities of $\mathbf { \dot { s } } \mathbf { w } _ { 1 }$ and sw by $q _ { 1 }$ and $q _ { 2 }$ respectively. Consumers are now ranked by their preferences to the quality of software, denoted by $\theta \in ( 0 , 1 )$ , instead of by their preferences of product features $( \mathrm { i . e . } x )$ . A consumer with a larger θ would derive more utility from the quality of $\mathbf { S } \mathbf { W } _ { 1 }$ and $\mathrm { \bf S W } _ { 2 } .$ . As such, the benefits of $\mathbf { S } \mathbf { W } _ { 1 }$ and $\mathbf { S } \mathbf { W } _ { 2 }$ to a consumer $\theta$ would be $q _ { 1 } \theta$ and $q _ { 2 } \theta$ respectively. Without loss of generosity, we assume $q _ { 1 } > q _ { 2 }$ Therefore, the utility functions of the consumer are modified as follows:

$$
U = \left\{ \begin{array}{l l} q _ {1} \theta - p _ {1} & \text { if   buy   sw } _ {1} \\ (1 - \phi) q _ {1} \theta - \tau z \eta_ {1} & \text { if   pirate   sw } _ {1} \\ q _ {2} \theta - p _ {2} & \text { if   buy   sw } _ {2} \\ (1 - \phi) q _ {2} \theta - \tau z \eta_ {2} & \text { if   pirate   sw } _ {2} \end{array} \right.\tag{12}
$$

where the definitions of $p _ { 1 } , p _ { 2 } , \tau , z , \eta _ { 1 } , \eta _ { 2 }$ remain the same as in horizontal differentiation.

Consider the consumer's utility when pirating either $\mathbf { S } \mathbf { W } _ { 1 }$ or $\mathbf { S } \mathbf { W } _ { 2 }$ . From Eq. (12), it follows that the slope of consumer's utility with respect to θ when pirating $\mathbf { S } \mathbf { W } _ { 1 }$ would always be steeper than that of pirating $\mathbf { S } \mathbf { W } _ { 2 } .$ . It can be easily seen that when $( \eta _ { 1 } , \eta _ { 2 } )$ is either $( 1 , 1 ) , ( 0 , 1 ) \mathrm { o r } ( 0 , 0 )$ , pirating $\mathbf { S } \mathbf { W } _ { 1 }$ would always dominate pirating $\mathbf { S } \mathbf { W } _ { 2 }$ . When $( \eta _ { 1 }$ $\eta _ { 2 } ) = ( 1 , 0 )$ , pirating sw may dominate pirating $\mathbf { S } \mathbf { W } _ { 1 }$ for some consumers. Denote the point of indifference between pirating $\mathbf { S } \mathbf { W } _ { 1 }$ and $\mathbf { S } \mathbf { W } _ { 2 }$ as $\theta _ { p 1 p 2 }$ , it can be seen that no one would pirate $\mathbf { S } \mathbf { W } _ { 2 }$ unless $\theta _ { p 1 p 2 } > 0$

Now consider the consumer's utility when buying either software. From Eq. (12), it is clear that the slope of consumer's utility with respect to θ when buying $\mathbf { S } \mathbf { W } _ { 1 }$ would always be steeper than that of buying $\mathbf { S } \mathbf { W } _ { 2 }$ . We assume that the point of indifference between buying $\mathbf { S } \mathbf { W } _ { 1 }$ and buying ${ \mathrm { \bf S W } } _ { 2 } ,$ denoted by $\theta _ { b 1 b 2 } .$ lies somewhere between 0 and 1 (i.e. $0 < \theta _ { b 1 b 2 } < 1 )$ . (Without this assumption, buying either software would always dominate buying the other.)

Consider the consumer's utility with respect to θ as shown in Fig. 6. Namely, there will be 4 groups of consumers. Those with $\theta \in [ \theta _ { b 1 b 2 } , 1 ]$ would buy $\mathbf { S } \mathbf { W } _ { 1 }$ and those with $\theta \in [ \theta _ { p 1 b 2 } , \theta _ { b 1 b 2 } ]$ would buy $\operatorname { s w } _ { 2 } .$ . Moreover, those with $\theta \in [ \theta _ { p 1 p 2 } $ $\theta _ { p 1 b 2 } ]$ would choose to pirate $\mathbf { S } \mathbf { W } _ { 1 }$ while those with $\theta \in [ 0 , \stackrel { \cdot } { \theta _ { p 1 b 2 } } ] ( \mathrm { i f } ( \eta _ { 1 } , \eta _ { 2 } ) = ( 1 , 0 )$ and $\theta _ { p 1 p 2 } > 0 )$ would choose to pirate $\mathrm { \bf S W } _ { 2 } .$ However, we assume that even though $\mathbf { S } \mathbf { W } _ { 2 }$ is unprotected, it can only convert a certain portion of consumers from pirating $\mathbf { S } \mathbf { W } _ { 1 }$ to pirating ${ \mathrm { { s w } } } _ { 2 } ,$ mainly because the pirating cost should be relatively small. More formally, we assume the relations among the intersecting points to satisfy the following:

![](/api/attachments/YZQ3JWDU/fulltext/images/c8e1ef26f55ee32bf52ac218d0e4d60dd7335c612852b42f3259518a7707371b.jpg)  
Fig. 6. Consumer’s utility (vertical differentiation).

$$
1 > \theta_ {b 1 b 2} > \theta_ {p 1 b 2} > \theta_ {p 2 b 2} \forall z \in [ 0, 1 ]\tag{C2}
$$

Intuitively, it implies that the price of $\mathbf { S } \mathbf { W } _ { 1 }$ is higher than that of $\mathbf { S } \mathbf { W } _ { 2 }$ and both prices are higher than the pirating cost. Also, the risk of using pirated software is more significant than the quality difference between the products (i.e. $q _ { 2 } { > } ( 1 - \phi ) q _ { 1 }$ such that $U _ { b 2 }$ is always steeper than $U _ { p 2 } )$

Similar to our analysis on the horizontal differentiation case, the demands are given by the corresponding projections of the utility planes onto the $( \theta , z )$ plane, as illustrated by the shaded areas in Fig. 7. Namely, the demands for $\mathbf { S } \mathbf { W } _ { 1 }$ and $\mathbf { S } \mathbf { W } _ { 2 }$ are given by:

$$
d _ {1} = 1 - \int_ {0} ^ {1} \theta_ {b 1 b 2} \mathrm{d} z = 1 - \frac {p _ {1} - p _ {2}}{q _ {1} - q _ {2}}\tag{13}
$$

$$
d _ {2} = \int_ {0} ^ {1} \theta_ {b 1 b 2} \mathrm{d} z - \int_ {0} ^ {1} \theta_ {p 1 b 2} \mathrm{d} z = \frac {p _ {1} - p _ {2}}{q _ {1} - q _ {2}} + \frac {1}{2} \frac {\tau \eta_ {1} - 2 p _ {2}}{q _ {1} (\phi - 1) + q _ {2}}\tag{14}
$$

That is, the utility-maximizing demands would be entirely in terms of the other exogenous model parameters $q _ { 1 } , q _ { 2 } ,$ $\phi , \tau$ and k as well as the endogenous $p _ { 1 } , p _ { 2 } , \eta _ { 1 }$ and $\eta _ { 2 } .$ Since firms need to determine optimal prices to maximize their profits, their problems would be:

$$
\max _ {p _ {1}} \pi_ {1} = \max _ {p _ {1}} p _ {1} d _ {1} - k \eta_ {1} = \max _ {p _ {1}} \left(1 - \frac {p _ {1} - p _ {2}}{q _ {1} - q _ {2}}\right) p _ {1} - k \eta_ {1}\tag{15}
$$

$$
\max _ {p _ {2}} \pi_ {2} = \max _ {p _ {2}} p _ {2} d _ {2} - k \eta_ {2} = \max _ {p _ {2}} \left(\frac {p _ {1} - p _ {2}}{q _ {1} - q _ {2}} + \frac {1}{2} \frac {\tau \eta_ {1} - 2 p _ {2}}{q _ {1} (\varphi - 1) + q _ {2}}\right) p _ {2} - k \eta_ {2}\tag{16}
$$

Proposition 2. In a vertically differentiated software market, non-protection would always be optimal to the lowerquality firm. Protection would be optimal for the higher-quality firm only $\begin{array} { r } { i f k < \frac { \tau \left( 8 q _ { 1 } ^ { 2 } \phi + q _ { 1 } \tau - 8 q _ { 1 } q _ { 2 } \phi - \tau q _ { 2 } \right) } { 4 \left( q _ { 1 } + 3 q _ { 1 } \phi - q _ { 2 } \right) ^ { 2 } } . } \end{array}$

The Proof of Proposition 2 is shown in the Appendix. Again, denote the critical protection cost k by $\begin{array} { r } { k ^ { * } = \frac { \tau \left( 8 q _ { 1 } ^ { 2 } \phi + q _ { 1 } \tau - 8 q _ { 1 } q _ { 2 } \phi - \tau q _ { 2 } \right) } { 4 \left( q _ { 1 } + 3 q _ { 1 } \phi - q _ { 2 } \right) ^ { 2 } } } \end{array}$ . It is apparent that $k ^ { * }$ is always increasing in τ, the pirating cost. Protection would be optimal only if the protection cost is below $k ^ { * }$ which mainly consists of a square term of the pirating cost τ of the consumer. This once again suggests that firms should prefer only a very simple and low-cost protection mechanism or no protection at all.

![](/api/attachments/YZQ3JWDU/fulltext/images/d51740e7e078f3ec24173031540ec2c2f44a9c78113890df9500ed1e4432dab5.jpg)  
Fig. 7. Demands (vertical differentiation).

As shown in the Appendix, the optimal prices, demands as well as profits, if non-protection strategy is adopted by both firms, would be:

$$
\begin{array}{l l l} p _ {1} ^ {*} = \frac {2 q _ {1} \phi (q _ {1} - q _ {2})}{q _ {1} + 3 q _ {1} \phi - q _ {2}} & d _ {1} ^ {*} = \frac {2 q _ {1} \phi}{q _ {1} + 3 q _ {1} \phi - q _ {2}} & \pi_ {1} ^ {*} = \frac {4 q _ {1} ^ {2} \phi^ {2} (q _ {1} - q _ {2})}{(q _ {1} + 3 q _ {1} \phi - q _ {2}) ^ {2}} \\ p _ {2} ^ {*} = \frac {(q _ {1} \phi - q _ {1} + q _ {2}) (q _ {1} - q _ {2})}{q _ {1} + 3 q _ {1} \phi - q _ {2}} & d _ {2} ^ {*} = \frac {q _ {1} \phi}{q _ {1} + 3 q _ {1} \phi - q _ {2}} & \pi_ {2} ^ {*} = \frac {q _ {1} \phi (q _ {1} \phi - q _ {1} + q _ {2}) (q _ {1} - q _ {2})}{(q _ {1} + 3 q _ {1} \phi - q _ {2}) ^ {2}} \end{array}
$$

In particular, the higher-quality firm would charge a higher price and the optimal profit of the higher-quality firm is increasing in $q _ { 1 }$ just like the case of horizontal differentiation. The optimal profit of the lower-quality firm is also increasing in $\phi .$ In case the higher-quality firm chooses to protect, the optimal prices, demands as well as profits of the two firms would become:

$$
\begin{array}{l} p _ {1} ^ {*} = \frac {(4 q _ {1} \phi + \tau) (q _ {1} - q _ {2})}{2 (q _ {1} + 3 q _ {1} \phi - q _ {2})} d _ {1} ^ {*} = \frac {1}{2} \frac {4 q _ {1} \phi + \tau}{q _ {1} + 3 q _ {1} \phi - q _ {2}} \\ \pi_ {1} ^ {*} = \frac {1}{(q _ {1} + 3 q _ {1} \phi - q _ {2}) ^ {2}} (1 6 q _ {1} ^ {3} \phi^ {2} + 8 \tau q _ {1} ^ {2} \phi + q _ {1} \tau^ {2} - 1 6 q _ {1} q _ {2} \phi^ {2} \\ \quad - 8 q _ {1} q _ {2} \phi \tau - q _ {2} \tau^ {2} - 4 k q _ {1} ^ {2} - 2 4 k q _ {1} ^ {2} \phi + 8 k q _ {1} q _ {2} - 3 6 k q _ {1} ^ {2} \phi^ {2} + 2 4 k q _ {1} q _ {2} \phi - 4 k q _ {2} ^ {2}) \end{array}
$$

$$
\begin{array}{l} p _ {2} ^ {*} = \frac {(q _ {1} \phi - q _ {1} + q _ {2} + \tau) (q _ {1} - q _ {2})}{q _ {1} + 3 q _ {1} \phi - q _ {2}} d _ {2} ^ {*} = \frac {q _ {1} \phi (q _ {1} \phi - q _ {1} + \tau + q _ {2})}{(q _ {1} \phi - q _ {1} + q _ {2}) (q _ {1} + 3 q _ {1} \phi - q _ {2})} \\ \pi_ {2} ^ {*} = \frac {q _ {1} \phi (q _ {1} \phi - q _ {1} + \tau + q _ {2}) ^ {2} (q _ {1} - q _ {2})}{(q _ {1} \phi - q _ {1} + q _ {2}) (q _ {1} + 3 q _ {1} \phi - q _ {2}) ^ {2}} \end{array}
$$

Similar to the case of horizontal differentiation, it can be shown that the optimal prices and demands for nonprotection would always be lower than those if the higher quality firm chooses to protect. Again, the protection cost should be the major determining factor for the higher quality firm to choose protection. The effects of risk on the optimal price, demand as well as profit can be seen from the following table of comparative statics:

<table><tr><td></td><td> $\frac{\partial p_{1}^{*}}{\partial \phi}$ </td><td> $\frac{\partial p_{2}^{*}}{\partial \phi}$ </td><td> $\frac{\partial d_{1}^{*}}{\partial \phi}$ </td><td> $\frac{\partial d_{2}^{*}}{\partial \phi}$ </td><td> $\frac{\partial \pi_{1}^{*}}{\partial \phi}$ </td><td> $\frac{\partial \pi_{2}^{*}}{\partial \phi}$ </td></tr><tr><td>Only firm 1 protect</td><td>+&#x27;&#x27;</td><td>+&#x27;&#x27;</td><td>+&#x27;&#x27;</td><td>-&#x27;&#x27;</td><td>+&#x27;&#x27;</td><td>+&#x27;&#x27;</td></tr><tr><td>Both not protect</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td></tr></table>

$+ \mathit { \Pi } ^ { \prime \prime } ;$ positive if $\tau { < } \frac { 4 ( q _ { 1 } { - } q _ { 2 } ) } { 3 } ; { - } \prime \prime ;$ negative if $\tau { < } \frac { 4 ( q _ { 1 } { - } q _ { 2 } ) } { 3 } .$

Namely, optimal prices, demands and profits would all increase with risk if both firms choose the non-protection strategy. In case the higher quality firm chooses to protect, the optimal prices and profits would still increase with risk<sup>3</sup> but the optimal demand for the lower quality product would decrease. Intuitively, a higher risk would lead to a higher demand for the higher quality product but that would essentially reduce the demand of the lower quality product, although it would still result in an increased profit for the lower quality firm due to the increased price.

## 5. Discussion

We have considered the optimal protection strategies under two different types of market differentiations. Our analysis shows that in a vertically differentiated market the lower-quality firm would always prefer nonprotection. Furthermore, protection would be profitmaximizing only if the implementation cost is low.

In reality, we observe that most software developers are still implementing some sort of protection mechanisms in their software products although strong externalities effects are quite universal in the widelyexpanded software business nowadays. Apparently this seems to be inconsistent with the findings from previous researches [4,7]. It is also interesting to note that complicated protection mechanisms are seldom found nowadays. Most software products just employ a simple product key code validation or registration process to guard against unauthorized usage. The duplicated uses of those product key codes are seldom really checked, nor would they prevent the actual usage of the software. The software protection mechanisms used nowadays are observed to be converging to a very simple and common form of product key code validation. It is reasonable to expect that this sort of mechanisms would not be very costly to implement and is likely to be reusable on other software products developed by the same firm, further lowering the average implementation cost of protection.

Anecdotal evidence supports some of our findings. For instance, Maplesoft's Maple and Wolfram's Mathematica can be regarded as two horizontally differentiated products competing in the area of symbolic computation software. They are two incompatible products with different sets of features and employ different file formats although their problem domains are similar. Both of them adopt a simple product key code validation mechanism for protection. It is interesting to find that apart from protection strategy, their listed prices are also very similar. These facts are consistent with our analytical findings.

On the other hand, the Microsoft Office suite and Sun Microsystems' StarOffice package can be regarded as examples of vertically differentiated products. As Microsoft Office has become a de facto standard in the office productivity area, competitors in this application area have to develop products that are compatible with it. Unfortunately, Microsoft Office has been adopting a proprietary file format that prevents others from producing compatible products. StarOffice actually originated from an open-source initiative that attempted to reverse-engineer the proprietary file formats used by Microsoft Office that was believed to be over-priced. As a result, StarOffice is able to read and produce documents and spreadsheets in Microsoft Office format. However, it never achieves full compatibility with Microsoft Office and users may perceive it as a lower-quality product in this sense. Interestingly, Microsoft Office is adopting a protection scheme while StarOffice is not. Again, this is consistent with our analytical findings.

## 6. Conclusion and future work

Our findings show that the primary consideration of software protection strategies should be the implementation cost. This may help explain why complicated protection mechanisms have mostly been driven out of the software market nowadays. Also, the software developer of the lower-quality product would tend to adopt non-protection in order to compete with the higher-quality product in a vertically differentiated market. We have also considered the effects of risk in using pirated software. In both horizontally differentiated or vertically differentiated markets, a firm's profit is found to be increasing with the risk of using pirated software.<sup>4</sup> More interestingly, one may find that risk has a similar positive effect on profit as product quality.

As mentioned in the beginning of this paper, the existence of risk in itself does not prevent the use of pirated software. However, consumers are deterred from doing so in view of the uncertainty introduced by the risk. Gopal and Sanders [5] showed that deterrent measures would be more profit-maximizing than preventive ones for dealing with software piracy. Our findings about the effect of risk also support this argument. We attribute one of the sources of the risk in using pirated software to the unavailability of technical support. However, it should be noted that in this study we do not assume risk to be a parameter controllable by firm. In real life, the risk in using pirated software is subject to many other factors beyond the control of the software firm. We believe that firms can actually affect at least two factors: the reliability of software product and the quality of technical support. Ironically, the value of technical support increases when the reliability of software decreases. It would be interesting to see how these two factors (i.e. reliability and technical support quality) would interact and affect the firm's optimal strategy. We believe that future extension of this study can be developed along this line.

Our analysis does not consider the effect of externalities. Intuitively, firms should merely have less incentive to protect their software if there are strong externalities effects. However, empirical observation shows that most software products are still implementing protection mechanisms, albeit only simple and lowcost ones. In this study, we mainly focus on the effects of protection costs and risk in a competitive market. It would actually be straightforward to extend our model to include externalities effects as well. This could be another possible extension of this work.

Appendix A

Proof of Proposition 1. Based on Eqs. (10) and (11), the respective FOCs and SOCs are:

$$
\mathrm{FOC}: \frac {\partial \pi_ {1}}{\partial p _ {1}} = 0 \Rightarrow \frac {1}{2} \frac {- 4 p _ {1} + \tau \eta_ {1} + 2 q \phi}{t \phi} = 0 \mathrm{SOC}: \frac {\partial^ {2} \pi_ {1}}{\partial p _ {1} ^ {2}} <   0 \Rightarrow - \frac {2}{t \phi} <   0\tag{A1}
$$

$$
\mathrm{FOC}: \frac {\partial \pi_ {2}}{\partial p _ {2}} = 0 \Rightarrow \frac {1}{2} \frac {- 4 p _ {2} + \tau \eta_ {2} + 2 q \phi}{t \phi} = 0 \mathrm{SOC}: \frac {\partial^ {2} \pi_ {2}}{\partial p _ {2} ^ {2}} <   0 \Rightarrow - \frac {2}{t \phi} <   0\tag{A2}
$$

By solving the FOCs of Eqs. (A1) and (A2) simultaneously, the optimal prices $p _ { 1 } ^ { * }$ and $p _ { 2 } ^ { * }$ are derived for the 4 different possible protection strategies, namely $( \eta _ { 1 } = \eta _ { 2 } = 1 ) , ~ ( \eta _ { 1 } = 1 , \eta _ { 2 } = 0 ) , ~ ( \eta _ { 1 } = 0 , \eta _ { 2 } = 1 )$ and $( \eta _ { 1 } = 0 , \eta _ { 2 } = 0 )$ . The optimal prices and resulting profits are shown below:

<table><tr><td></td><td colspan="2">Firm 2: Protect</td><td colspan="2">Firm 2: Not protect</td></tr><tr><td rowspan="2">Firm 1: Protect</td><td> $p_{1}^{*} = \frac{\tau + 2q\phi}{4}$ </td><td> $\pi_{1}^{*} = \frac{\tau^{2} + 4\tau q\phi + 4q^{2}\phi^{2} - 16kt\phi}{16t\phi}$ </td><td> $p_{1}^{*} = \frac{\tau + 2q\phi}{4}$ </td><td> $\pi_{1}^{*} = \frac{\tau^{2} + 4\tau q\phi + 4q^{2}\phi^{2} - 16kt\phi}{16t\phi}$ </td></tr><tr><td> $p_{2}^{*} = \frac{\tau + 2q\phi}{4}$ </td><td> $\pi_{2}^{*} = \frac{\tau^{2} + 4\tau q\phi + 4q^{2}\phi^{2} - 16kt\phi}{16t\phi}$ </td><td> $p_{2}^{*} = \frac{q\phi}{2}$ </td><td> $\pi_{2}^{*} = \frac{q^{2}\phi}{4t}$ </td></tr><tr><td rowspan="2">Firm 1: Not protect</td><td> $p_{1}^{*} = \frac{q\phi}{2}$ </td><td> $\pi_{1}^{*} = \frac{q^{2}\phi}{4t}$ </td><td> $p_{1}^{*} = \frac{q\phi}{2}$ </td><td> $\pi_{1}^{*} = \frac{q^{2}\phi}{4t}$ </td></tr><tr><td> $p_{2}^{*} = \frac{\tau + 2q\phi}{4}$ </td><td> $\pi_{2}^{*} = \frac{\tau^{2} + 4\tau q\phi + 4q^{2}\phi^{2} - 16kt\phi}{16t\phi}$ </td><td> $p_{2}^{*} = \frac{q\psi}{2}$ </td><td> $\pi_{2}^{*} = \frac{q^{2}\phi}{4t}$ </td></tr></table>

The SOCs in Eqs. (A1) and (A2) only require $t , \phi > 0$ that thus should always be satisfied. Constraints in Eq. (C1) are also verified. Comparing the profits resulting from different protection strategies, it follows that when $k { < } \tau ( \tau { + } 4 q \phi ) /$ 16tϕ, protection would be optimal for both firms. Otherwise, non-protection would be the optimal strategy leading to maximum profit. □

Proof of Proposition 2. Based on Eqs. (15) and (16), the respective FOCs and SOCs are:

$$
\mathrm{FOC}: \frac {\partial \pi_ {1}}{\partial p _ {1}} = 0 \Rightarrow \frac {- 2 p _ {1} + q _ {1} - q _ {2} + p _ {2}}{q _ {1} - q _ {2}} = 0 \text {SOC}: \frac {\partial^ {2} \pi_ {1}}{\partial p _ {1} ^ {2}} <   0 \Rightarrow - \frac {2}{q _ {1} - q _ {2}} <   0\tag{A3}
$$

$$
\mathrm{FOC}: \frac {\partial \pi_ {2}}{\partial p _ {2}} = 0 \Rightarrow \frac {1}{2} \frac {- 4 q _ {1} \phi p _ {2} + 2 p _ {1} q _ {1} (\phi - 1) + 2 p _ {1} q _ {2} + \tau \eta_ {1} (q _ {1} - q _ {2})}{(q _ {1} - q _ {2}) [ q _ {1} (\phi - 1) + q _ {2} ]} = 0\tag{A4}
$$

$$
\mathrm{SOC}: \frac {\partial^ {2} \pi_ {2}}{\partial p _ {2} ^ {2}} <   0 \Rightarrow - \frac {2 q _ {1} \phi}{(q _ {1} - q _ {2}) [ q _ {1} (\phi - 1) + q _ {2} ]} <   0
$$

Then, by solving the FOCs in Eqs. (A3) and (A4) simultaneously, the optimal prices $p _ { 1 } ^ { * }$ and $p _ { 2 } ^ { * }$ are obtained for the 4 possible strategies. The optimal prices and resulting profits are:

<table><tr><td></td><td colspan="2">Firm 2: Protect</td><td colspan="2">Firm 2: Not protect</td></tr><tr><td rowspan="2">Firm 1: Protect</td><td> $p_{1}^{*} = \frac{(4q_{1}\phi + \tau)(q_{1} - q_{2})}{2(q_{1} + 3q_{1}\phi - q_{2})}$ </td><td> $\pi_{1}^{*} = A$ </td><td> $p_{1}^{*} = \frac{(4q_{1}\phi + \tau)(q_{1} - q_{2})}{2(q_{1} + 3q_{1}\phi - q_{2})}$ </td><td> $\pi_{1}^{*} = A$ </td></tr><tr><td> $p_{2}^{*} = \frac{(q_{1}\phi - q_{1} + q_{2} + \tau)(q_{1} - q_{2})}{q_{1} + 3q_{1}\phi - q_{2}}$ </td><td> $\pi_{2}^{*} = B - k$ </td><td> $p_{2}^{*} = \frac{(q_{1}\phi - q_{1} + q_{2} + \tau)(q_{1} - q_{2})}{q_{1} + 3q_{1}\phi - q_{2}}$ </td><td> $\pi_{2}^{*} = B$ </td></tr><tr><td rowspan="2">Firm 1: Not protect</td><td> $p_{1}^{*} = \frac{2q_{1}\phi(q_{1} - q_{2})}{q_{1} + 3q_{1}\phi - q_{2}}$ </td><td> $\pi_{1}^{*} = C$ </td><td> $p_{1}^{*} = \frac{2q_{1}\phi(q_{1} - q_{2})}{q_{1} + 3q_{1}\phi - q_{2}}$ </td><td> $\pi_{1}^{*} = C$ </td></tr><tr><td> $p_{2}^{*} = \frac{(q_{1}\phi - q_{1} + q_{2})(q_{1} - q_{2})}{q_{1} + 3q_{1}\phi - q_{2}}$ </td><td> $\pi_{2}^{*} = D - k$ </td><td> $p_{2}^{*} = \frac{(q_{1}\phi - q_{1} + q_{2})(q_{1} - q_{2})}{q_{1} + 3q_{1}\phi - q_{2}}$ </td><td> $\pi_{2}^{*} = D$ </td></tr></table>

where

$$
\begin{array}{l} A = \frac {1}{(q _ {1} + 3 q _ {1} \phi - q _ {2}) ^ {2}} (1 6 q _ {1} ^ {3} \phi^ {2} + 8 \tau q _ {1} ^ {2} \phi + q _ {1} \tau^ {2} - 1 6 q _ {1} q _ {2} \phi^ {2} - 8 q _ {1} q _ {2} \phi \tau - q _ {2} \tau^ {2} - 4 k q _ {1} ^ {2} - 2 4 k q _ {1} ^ {2} \phi + 8 k q _ {1} q _ {2} - 3 6 k q _ {1} ^ {2} \phi^ {2} + 2 4 k q _ {1} q _ {2} \phi - 4 k q _ {2} ^ {2}) \\ B = \frac {q _ {1} \phi (q _ {1} \phi - q _ {1} + \tau + q _ {2}) ^ {2} (q _ {1} - q _ {2})}{(q _ {1} \phi - q _ {1} + q _ {2}) (q _ {1} + 3 q _ {1} \phi - q _ {2}) ^ {2}}, C = \frac {4 q _ {1} ^ {2} \phi^ {2} (q _ {1} - q _ {2})}{(q _ {1} + 3 q _ {1} \phi - q _ {2}) ^ {2}}, D = \frac {q _ {1} \phi (q _ {1} \phi - q _ {1} + q _ {2}) (q _ {1} - q _ {2})}{(q _ {1} + 3 q _ {1} \phi - q _ {2}) ^ {2}} \\ B - D = \frac {q _ {1} \phi \tau (2 q _ {1} \phi - 2 q _ {1} + \tau + 2 q _ {2}) (q _ {1} - q _ {2})}{(q _ {1} \phi - q _ {1} + q _ {2}) (q _ {1} + 3 q _ {1} \phi - q _ {2}) ^ {2}} > 0 \text { and } A - C > 0 \text { iff } k <   \frac {\tau (8 q _ {1} ^ {2} \phi + q _ {1} \tau - 8 q _ {1} q _ {2} \phi - \tau q _ {2})}{4 (q _ {1} + 3 q _ {1} \phi - q _ {2}) ^ {2}} \end{array}
$$

The SOCs for profit maximization are satisfied when $q _ { 2 } > q _ { 1 } ( 1 - \phi )$ , which is actually one of our assumptions. Constraints implied in Eq. (C2) are also verified. It can be seen that the dominant strategy for the lower-quality firm would always be non-protection (i.e. $B { > } B { - } k$ and $D { > } D { - } k )$ . To the higher-quality firm, protection would only be optimal i $\operatorname { f } k { < } \tau ( 8 q _ { 1 } ^ { 2 } \phi + q _ { 1 } \tau - 8 q _ { 1 } q _ { 2 } \phi - \tau q _ { 2 } ) / 4 { ( q _ { 1 } + 3 q _ { 1 } \phi - q _ { 2 } ) } ^ { 2 }$ □

## References

[1] D.S. Banerjee, Software piracy: a strategic analysis and policy instruments, International Journal of Industrial Organization 21 (2003).

[2] Business Software Alliance, Eighth Annual BSA Global Software Piracy Study: Trends in Software Piracy 1994–2002, (Business Software Alliance, 2003).

[3] H.K. Cheng, R.R. Sims, H. Teegen, To purchase or to pirate software: an empirical study, Journal of Management Information Systems 13 (4) (1997).

[4] K.R. Conner, R.P. Rumelt, Software piracy: an analysis of protection strategies, Management Science 37 (2) (1991).

[5] R.D. Gopal, G.L. Sanders, Preventive and deterrent controls for software piracy, Journal of Management Information Systems 13 (4) (1997).

[6] H. Hotelling, Stability in competition, The Economic Journal 39 (153) (1929) 41–57.

[7] O. Shy, J.F. Thisse, A strategic approach to software protection, Journal of Economics & Management Strategy 8 (2) (1999).

[8] J. Tirole, The Theory of Industrial Organization, MIT Press, 1988.

[9] US-CERT, US-CERT Vulnerability Notes (http://www.kb.cert. org/vuls), (US-CERT, 2004).

![](/api/attachments/YZQ3JWDU/fulltext/images/d4eaa94d3522ce1da3da9da82609597585266316ea9e72a841888a2e22093e65.jpg)

Samuel Shu Kin Kwan is the Head of WWW and Server Technology at the Hong Kong University of Science and Technology. He expects to receive his PhD in Information Systems in 2007. As an industry expert with over 20 years of technical and managerial experience, he was engaged in various R&D endeavours such as participating in the Internationalization (I18N) Working Group of the World Wide Web Consortium (W3C) as well as designing the

first client-to-client Mondex Internet Payment solution. His current research interests center around the phenomenon of digital piracy, its behavioral determinants as well as economic and organizational impacts.

![](/api/attachments/YZQ3JWDU/fulltext/images/0c90353f58e1d4322e6ec912e816585d318970da8cdb9ba2c45aed447cc27732.jpg)

Jeevan Jaisingh is an Assistant Professor at the Hong Kong University of Science and Technology. He received his PhD in MIS from Purdue University. His research interests lie in the areas of open source software, piracy, privacy and vulnerability disclosure. His work has been published, or is forthcoming in European Journal of Operational Research, Journal of Organizational Computing and Electronic Commerce, Journal of Electronic Commerce

Research and Journal of Information Technology and Decision Making.  
![](/api/attachments/YZQ3JWDU/fulltext/images/9fc2811f09e9562809f626c1794a659e0532727e0487d737c82d474b6838e6e5.jpg)

Kar Yan Tam is Chair Professor of Information and Systems Management at the Hong Kong University of Science & Technology. His research interests include adoption of information technology, electronic commerce and web personalization. He has published extensively on these topics in major management science and information system journals. He is currently on the editorial board of Information Systems Research and a number

of IS journals. Prof. Tam has extensive consulting experience with major companies including HSBC, Sun Microsystems, Symantec, and Hutchison Telecommunications.
