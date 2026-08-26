---
otero_id: 13846
otero_key: "DGZMD9QE"
title: "Revisiting the incentive to tolerate illegal distribution of software products"
authors: "Atanu Lahiri"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.01.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Revisiting the incentive to tolerate illegal distribution of software products

Atanu Lahiri

Foster School of Business, University of Washington, United States

a r t i c l e i n f o

Available online 25 January 2012

Keywords: Software distribution Patch distribution Software piracy Software security Network effect

## a b s t r a c t

Motivated by the recent strategy switch of a large software producer, this paper revisits the trade-offs associated with tolerating illegal distribution of software products. Conventional wisdom is that a higher level of positive network effects justi<sup>fi</sup>es a tolerant approach on the part of software producers—because illegal distribution leads to more users, ampli<sup>fi</sup>es positive network effects, and creates a greater demand for the legal version. I show that this wisdom does not hold in the context of supporting illegal versions with patches. Patches are used for plugging security vulnerabilities as well as for distributing functionality changes. Software producers have the option of supporting illegal versions with either or both kinds of patches. I <sup>fi</sup>nd that, even in the presence of strong positive network effects, the least tolerant approach of denying illegal versions both kinds of patches can be optimal.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

In the US, 22% of personal computer users use illegal copies of the Windows system; in absolute terms, a staggering 12 million users in this country use illegal copies of the Windows software [13]. Another 13 million illegal copies are in use in China [13]. We need to add to this number the number of illegal copies <sup>fl</sup>oating in all other countries to get an estimate of the total number of illegal copies and the lost revenue; the lost revenue in Microsoft's case is clearly tens of billions of dollars, if not hundreds of billions [7]. Simply put, piracy, for many software products, results in a severe cannibalization of the legal demand and adversely affects pro<sup>fi</sup>ts of their manufacturers.

Piracy problem is often exacerbated by illegal retailers who sell illegal copies at signi<sup>fi</sup>cant discounts vis-à-vis suggested retail prices of original products. These illegal retailers often have excellent understanding of the markets that they operate in, and are very effective in convincing consumers about the economic bene-<sup>fi</sup>ts of acquiring software and other services from them. The existence of this parallel illegal distribution channel makes piracy a very dif<sup>fi</sup>cult problem to deal with. Software manufacturers thus constantly have to look for technologies, legal recourses, and other means to contain this channel. Some common approaches are listed in Section 2.

To curb piracy, software manufacturers typically use a combination of strategies including the Digital Rights Management or DRM technology. Existing research on DRM shows that the manufacturer makes larger pro<sup>fi</sup>ts by tolerating piracy if positive network effects are suf<sup>fi</sup>ciently large [11]. The existing research, however, does not explain whether this relationship between the incentive to tolerate piracy and positive network effects is applicable to other important contexts such as the context of patching. Consequently, the existing research does also not explain why Microsoft, despite bene<sup>fi</sup>ting from large positive networks effects, in recent years, has stopped offering certain software patches to illegal users.

So, what are these patches? Patches are essentially changes to the original software. The changes can be functionality related, security related, or a combination. At times the changes are offered individually, at others they are combined into “service packs.” These days software patches are frequently distributed using the Internet. For instance, Microsoft makes patches for the Windows operating system available through the tool called “Microsoft Update.” If a user has the “automatic update” feature turned on, she receives patches automatically as soon as she goes on-line the very <sup>fi</sup>rst time on or after the second Tuesday of any month (or the very <sup>fi</sup>rst time after the release of a new patch). Alternatively, any user can visit the Microsoft Update site periodically to download and install critical patches. Patches are also common for other software manufacturers and for other types of software. Apple provided 45 patches for “Panther” (10.4) version of its operating system. And, Adobe updated its Acrobat 7 product on average once every 89 days.

What then makes patching a viable instrument for controlling piracy? The answer, in short, is the Internet. The Internet not only serves a channel for patch distribution, it also allows for two way communication that can be used by a software manufacturer to authenticate installations seeking patches. Common authentication techniques rely on unique keys, system signatures, and a database of authentications. Such techniques can easily identify installations that do not meet the End User License Agreements (EULA). Microsoft's “Genuine Advantage” is an example of one such tool that validates installations prior to patch distribution. Armed with such tools that can distinguish between legal and illegal installations, a software manufacturer can limit distribution of its patches to legal installations, thereby creating a “quality gap” or a vertical differentiation between the legal and illegal (pirated) versions of its product. This quality gap reduces the cannibalization of the legal demand by piracy. It is useful to note here that patches are distributed frequently using the Internet, which makes stealing patches almost impossible. Further, as I argue later, for most patches, timely deployment is critical, which means that patches received from illegal sources long after their original releases would be almost worthless. Hence, the manufacturer remains in control of its patch distribution, and retains the ability to in<sup>fl</sup>uence piracy by denying illegal versions certain patches.

It is certainly tempting to think that the value of containing illegal distribution is minimal when the level of positive network effects is large, because reducing piracy can shrink the user base, reducing the leverage from positive network effects [11]. However, the recent strategy switch of Microsoft indicates that exactly the opposite may be true. In 2004, Microsoft decided to provide the Service Pack 2, a major compilation of security and functionality upgrades to its existing Windows XP product, to all users, legal and illegal alike. However, Microsoft has since changed its patching strategy. According to an Associated Press report [1], Microsoft is now following a policy of offering critical security <sup>fi</sup>xes to all users while restricting feature enhancements and functionality related <sup>fi</sup>xes to authenticated copies only. Speci<sup>fi</sup>cally, Microsoft no longer offers feature updates to Internet Explorer, Windows Media Player, or Windows Defender to illegal installations though it still offers security updates to its Windows system to all users.

Microsoft's decision is an interesting one, and is driven by economic considerations. Microsoft, or any software manufacturer for that matter, has four possible strategies to choose from: (PN) offer pirates nothing, (PF) provide pirates only functionality patches/ enhancements, (PS) provide pirates only security fixes, and (PA) provide pirates all patches. First, consider the choice of offering feature enhancements or functionality related <sup>fi</sup>xes to pirates. If users of pirated copies have lesser access to these enhancements and <sup>fi</sup>xes, the quality of their product will be lower than that of the legal product, i.e., the pirated version would suffer from a “functionality gap.” This functionality gap works as an added incentive to prefer the legal product. However, as I have already mentioned, positive network effects, which are exhibited by most software products, complicate this consideration.

What about security related <sup>fi</sup>xes? Not offering these <sup>fi</sup>xes makes pirates more vulnerable to security threats, i.e., makes the pirated version suffer from a “security gap.” While this gap discourages piracy, not securing illegal copies also results in a larger pool of vulnerable machines in the network. A larger vulnerable pool offers a breeding ground for viruses, worms, etc., and can also become a zombie for denial of service (DoS) attacks. It makes the network less secure, and reduces the value of the software to all legal and illegal users [4]. August and Tunca [4] are among the <sup>fi</sup>rst to model this negative network effect. However, they do not consider positive network effects, and, as a result, do not explain what happens when both network effects are simultaneously present.

One may ask why legal users, who have access to patches, should worry about increased security threats. Many legal users, particularly businesses, have their own processes for testing and distributing patches. Such processes often delay applications of critical patches. For example, a corporation may choose to patch its non-critical computers <sup>fi</sup>rst to test the quality of a patch. Also, patching can interfere with day-to-day activities of these corporations or individuals [20]. A small business owner may delay the application of a patch if applying it involves rebooting of its computers and disruption of some time-critical tasks. Such delays create a window of opportunity between the release of a patch and its actual application, which worm-attackers love to exploit. Consider, for example, the Zotob worm attack, which was launched within a day of the release of the relevant patch and the disclosure of the associated vulnerability [12]. Previous worms such as Sasser, Blaster, or Code Red were launched weeks or months after disclosures of corresponding vulnerabilities. Big corporations, most notably the media conglomerates, were completely overwhelmed by the speed of the Zotob attack—all these corporations patched, but they did not patch fast enough.

Since “zero day exploits” like the Zotob worm are becoming increasingly common, I hypothesize that even users of legal copies, regardless of their willingness to patch, are affected by vulnerable pirated copies, because vulnerable pirated copies increase the possibility of infection in the presence of patching delays and also increase the likelihood of DoS and other malicious attacks on the network. In my model, this negative network effect, which is present even when all legal users are willing to patch, lowers the value of the software product to legal users. It is worth noting that some pirates may not apply patches timely and that giving them patches, therefore, would not improve network security. However, as long as some of them apply promptly, giving everyone security patches would make the network more secure on the margin. My model focuses on this marginal improvement and its impact on pro<sup>fi</sup>ts, and not on the network security in an absolute sense.

The rest of this paper is organized as follows. I <sup>fi</sup>rst discuss the related literature. Next, I present an economic model. Both analytically and numerically, I then examine how different levels of positive and network effects affect the equilibrium pro<sup>fi</sup>t for each of the four patching strategies. I conclude by summarizing main contributions and limitations of my work.

## 2. Literature

This research is related to different streams of literature. One key stream is the economics of networks. Katz and Shapiro [18] examine the role of positive network effects in the context of competition and technology choice using the notion of Fulfilled Expectations Equilibrium, an important economic tool that I also use in this work. The framework in [18] has been further extended by Lee and Mendelson[21], who have investigated, using a two-stage game-theoretic model, vendors' incentives to build compatible products in the presence of network effects.

Another key stream is the economics of managing piracy. Conner and Rumelt [11] apply the notion of Fulfilled Expectations Equilibrium to analyze the monopolist's incentive to tolerate piracy in the presence of positive network effects. They <sup>fi</sup>nd that, when positive network effects are large, the vendor may pro<sup>fi</sup>t more by reducing investments in Digital Rights Management (DRM) technologies, i.e., by implicitly supporting piracy. The reason is that a lower DRM level leads to more illegal users, who contribute to the network effect and legal users' willingness-to-pay for the product. Conner and Rumelt [11], however, do not consider negative network effects, which I examine here. I show that the incentives to tolerate piracy are very different in the presence of negative network effects.

Other researchers also <sup>fi</sup>nd economic reasons to tolerate piracy. Gopal and Sanders [14] show that piracy helps pro<sup>fi</sup>ts when antipiracy measures are able to appropriate a substantial compensation from pirates. Shy and Thisse [24] show that, in a duopoly setting in which support is bundled with purchase, there are incentives for software manufacturers to not implement DRM. They thus extend the <sup>fi</sup>ndings in [11] to the duopoly setting. I do not consider the duopoly setting; instead, I investigate whether the insights from [11] apply to the case of supporting pirates with patches.

Alternative means for controlling piracy are also found in the extant literature on piracy of information goods. Chellappa and Shivendu [8] discuss the possibility of offering free trials to curb piracy of digital experience goods. The idea is that, when consumers are not aware of the true value of the experience good, they resort to piracy. However, if they get an opportunity to try the product and <sup>fi</sup>nd its true value, they are often willing to pay the full price for the product. In another work, Sundararajan [26] investigates how a software manufacturer should optimize its non-linear price schedule in the presence of piracy. There is also some research showing that offering cheaper stripped down versions to price-sensitive consumers can mitigate piracy [27]. My contribution to this stream is that I discuss how patching can be used strategically to stem the adverse effect of piracy on pro<sup>fi</sup>ts.

There is some research that explores the optimal quality decision in the presence of piracy [10,15,16,28]. More recently, Lahiri and Dey [19] show that a monopolist can effectively combat piracy by building higher quality products. In this paper, I do not examine the quality decision. I instead consider the quality gap between the legal and pirated versions and explore how a manufacturer should in<sup>fl</sup>uence that gap by choosing different patching strategies.

Since I address the role played by the quality gap (between legal and illegal versions) in deterring piracy, my work is also closely related to the work on vertical differentiation. Bhargava and Choudhary [5,6] and Jones and Mendelson [17] provide insights into the monopolist's vertical differentiation problem—in their models, the monopolist decides the number of versions to offer. On the contrary, in this paper, the lower quality version is the pirated version, and the manufacturer does not control the decision to offer it. However, the manufacturer can in<sup>fl</sup>uence the quality of the lower version, i.e., that of the pirated product, by employing different patching strategies.

This work is also related to the work on patching of software vulnerabilities. Arora et al. [2] discuss how quickly a newly discovered vulnerability be made public in order to incentivize timely development of patches. There also exists interesting work on negative network effects, which, as mentioned already, arise from not offering security <sup>fi</sup>xes to pirates [3,4]. Unlike [4], this work allows dual network effects, i.e., it considers both positive and negative network effects. Additionally, it considers both functionality enhancements and security <sup>fi</sup>xes, and also explicitly addresses the heterogeneity in piracy costs, which include costs associated with procuring an illegal copy as well as potential legal liabilities.

There are also papers that examine welfare implications of piracy [9,23]. The common <sup>fi</sup>nding in this stream is that piracy improves welfare, because it makes a zero marginal cost good available to a larger user base. The welfare analysis is beyond the scope of this research. In this research, the main focus is to answer the question whether the economic justi<sup>fi</sup>cation for supporting piracy in the presence of positive network effects is applicable to the context of software patching.

## 3. Model

Let the utility of the legal copy to a potential user be $e _ { l } x - p ,$ where e is the quality of the legal copy,<sup>1</sup> x is the intrinsic value of the software (the value of the software to the user in the absence of all network effects), and p is the price. Let the utility of the illegal copy be e x − y, where e is the quality of the illegal version and y is the cost of piracy faced by the user. Therefore, the user, characterized by the tuple $( x , y ) ,$ , buys the legal version if and only if the following Individual Rationality (IR) and Incentive Compatibility (IC) conditions are satis<sup>fi</sup>ed:

$$
e _ {l} x - p \geq 0\tag{IR}
$$

$$
e _ {l} x - p \geq e _ {i} x - y\tag{IC}
$$

Similarly, the user buys the illegal version when the following conditions are satis<sup>fi</sup>ed:

$$
e _ {i} x - y \geq 0\tag{IR}
$$

$$
e _ {i} x - y \geq e _ {l} x - p\tag{IC}
$$

## 3.1. Quality factors

The quality factors, e and $e _ { i } ,$ depend on the software maker's patching strategy as well as the expected sizes of the legal and illegal markets, which equal their realized sizes in the equilibrium. I denote the equilibrium sizes of the legal and illegal markets by q and $q _ { i } ,$ respectively. I denote the total demand by q, i.e., q = q<sub>l</sub> + q<sub>i</sub>. I denote the software maker's patching strategy by I, which is one of the four described earlier, i.e., I ∈ {PN, PA,PS, PF}. The relationship between the quality factors and patching strategies is as described by the following four assumptions (see Table 1 for a summary).

Assumption 1. If all patches are offered to pirates, i.e., I = PA, pirates and legal users are assumed to enjoy the same quality. Speci<sup>fi</sup>cally, e =e =1+e(q), where e(q), the positive network effect, is a nondecreasing function of q and e(0)=0.

Assumption 2. If only security <sup>fi</sup>xes are offered to pirates, i.e., I=PS, e =1+e(q) and e =1+e(q)−β, where 0≤βb1 represents the “functionality gap.”

In the case of Microsoft Windows, functionality patches are essentially feature updates to the Internet Explorer, Windows Media Player, and Windows Defender. The question is whether such patches play a role in determining the network effects. First, positive network effects for most software products are primarily attributable to two factors: (a) incompatible executable programs (e.g., Windows-based executables do not run on Macintosh) and (b) proprietary <sup>fi</sup>le formats (e.g., <sup>fi</sup>les created by Microsoft Of<sup>fi</sup>ce 7 applications are not compatible with other applications). Neither of the above—the Internet Explorer, Windows Media Player, or Windows Defender—seems to be contributing to any of these two sources of positive network effects. Second, Windows Defender is not a security patch, because it is possible to buy a substitute from other security software vendors such as McAfee or Symantec. Hence, it appears to be the case that functionality patches are not determinants of network effects. Thus, it is reasonable to assume that their total value is given by a parameter, namely $\beta ,$ that does not depend on q<sub>i</sub> or q<sub>l</sub>.

Assumptions regarding the quality factors.

<table><tr><td>Functionality gap</td><td> $\beta$ </td></tr><tr><td>Security gap</td><td> $\delta(q_i)$ </td></tr><tr><td>Positive network effect</td><td> $e(q)$ </td></tr><tr><td>Negative network effect</td><td> $\alpha(q_i)$ </td></tr><tr><td> $I = PN$ </td><td> $e_i = 1 - \beta + e(q) - (\alpha(q_i) + \delta(q_i))$  $e_l = 1 + e(q) - \alpha(q_i)$ </td></tr><tr><td> $I = PA$ </td><td> $e_i = 1 + e(q)$  $e_l = 1 + e(q)$ </td></tr><tr><td> $I = PS$ </td><td> $e_i = 1 - \beta + e(q)$  $e_l = 1 + e(q)$ </td></tr><tr><td> $I = PF$ </td><td> $e_i = 1 + e(q) - (\alpha(q_i) + \delta(q_i))$  $e_l = 1 + e(q) - \alpha(q_i)$ </td></tr></table>

![](/api/attachments/DGZMD9QE/fulltext/images/2b45695e45ee9170e6e649a4b29d0fda651b0a5f2191015f36ac224de1a58397.jpg)  
Fig. 1. Time line.

Assumption 3. If only functionality changes are offered to pirates, $\mathrm { i } . \mathrm { e } . , I { = } \mathrm { P F } ,$ illegal users face an equal or bigger security risk although all users suffer a loss in value due to negative network effects. Speci<sup>fi</sup>cally, $e _ { l } { = } 1 + e ( q ) - { \alpha } ( q _ { i } )$ and $e _ { i } { = } 1 + e ( q ) - { \alpha } ( q _ { i } ) - { \delta } ( q _ { i } )$ , where $\alpha ( q _ { i } )$ represents the negative network effect (the common loss in value arising from pirates not having access to security patches) and $\delta ( q _ { i } )$ represents the “security gap.” Both $\alpha ( q _ { i } )$ and $\delta ( q _ { i } )$ are non-decreasing in $q _ { i } ,$ and $\alpha ( 0 ) = \delta ( 0 ) = 0 .$

Assumption 4. If no patches are offered to pirates, i.e., $I { \bf = P N } ,$ both the “functionality $\boldsymbol { \mathrm { g a p } } ^ { \prime \prime }$ and “security $\boldsymbol { \mathrm { g a p } } ^ { * }$ separate the legal and illegal versions. Speci<sup>fi</sup>cally, $e _ { l } = 1 + e ( q ) - \alpha ( q _ { i } )$ and $e _ { i } = 1 + e ( q ) -$ $\alpha ( q _ { i } ) - \delta ( q _ { i } ) - \beta .$

The assumption here is that $\alpha ( q _ { i } )$ and $\delta ( q _ { i } )$ are non-negative functions of $q _ { i } ,$ the number of illegal users. The reason is that $\alpha ( q _ { i } )$ provides a measure of the “additional” security concerns that legal users face when illegal users are not given security patches. Similarly, $\alpha ( q _ { i } ) + \delta ( q _ { i } )$ is a measure of the “additional” security concerns that illegal users face. Since $\delta ( q _ { i } ) \geq 0$ , the assumptions above imply that illegal users are, on the margin, at least as insecure as legal users are: this is reasonable since legal users remain vulnerable until they patch, while illegal users remain vulnerable for a longer period. Further, the assumption that α(q ) and $\delta ( q _ { i } )$ are functions of $q _ { i }$ does not rule out the possibility that they can be constants.

## 3.2. The time line

My model assumes the following time line (see Fig. 1). As is shown in the <sup>fi</sup>gure, the quality and gap factors become common knowledge before the manufacturer or consumers make their decisions. The assumption that e(.) or β are common knowledge is similar to what we <sup>fi</sup>nd in the existing literature [11]. For example, most users can anticipate that $e ( . )$ is larger for word processing software than it is for security software. Similarly, users often know in advance what patches make up β; e.g., for the Windows system, it is made up of feature updates to the Internet Explorer browser, the Windows Media player, and the Windows Defender tool.

The assumption that $\alpha ( . )$ and $\delta ( . )$ are common knowledge may appear to be a strong assumption in the sense that it is hard for potential consumers to anticipate security threats. Yet, such assumptions have been used in the literature [4], because without them there would be no plausible way for the manufacturer or consumers to decide rationally. They are also not unreasonable in the sense that potential users may be able to estimate—based on the software maker's reputation or by looking at its other products—the impact of likely security threats, and thus they may be able to anticipate $\alpha ( . )$ and $\delta ( . )$

The software manufacturer, who is presumed to be a monopolist facing a zero marginal cost, <sup>fi</sup>rst chooses the patching strategy and the price. Then, each potential user decides whether to purchase a legal copy, or to procure an illegal copy, or to forgo the use of the product completely. The manufacturer and potential users base their decisions on their expectations regarding the sizes of the legal and illegal markets. At the Fulfilled Expectations Equilibrium, their expectations are realized. The equilibrium demand determines the monopolist's revenue. Note that, because I assume a zero marginal cost, I use the terms “revenue” and “pro<sup>fi</sup>t” interchangeably.

## 3.3. Fulfilled Expectations Equilibrium

In a Fulfilled Expectations Equilibrium, the number of users is endogenously determined. I can normalize the market size to 1, without loss of generality. Let $x ,$ the intrinsic value, and $y ,$ the piracy cost, be independently distributed with distribution functions $F ( x )$ and $G ( y )$ respectively.<sup>2</sup> I also assume that these distribution functions are publicly known. However, only each user is assumed to be aware of his own x and $y .$ The IR and IC conditions above then imply that:

$$
\begin{array}{l} q _ {l} = \int_ {p / e _ {l}} ^ {\infty} \int_ {p - (e _ {l} - e _ {i}) x} ^ {\infty} d G (y) d F (x) \\ = 1 - F (p / e _ {l}) - \int_ {p / e _ {l}} ^ {\infty} G (p - (e _ {l} - e _ {i}) x) d F (x) \end{array}\tag{1}
$$

Examining the number of legal users, $q _ { l } ,$ it consists of two parts. The <sup>fi</sup>rst part, $1 - F ( p / e _ { l } )$ is the demand if the price is p and piracy is not possible. This is reduced by the last term, which is the cannibalization of legal demand by piracy. Let me denote this cannibalization quantity by $q _ { c } .$

$$
q _ {c} = \int_ {p / e _ {l}} ^ {\infty} G (p - (e _ {l} - e _ {i}) x) d F (x)
$$

The IR and IC conditions also imply that:

$$
\begin{array}{l} q _ {i} = \int_ {0} ^ {p / e _ {l}} \int_ {0} ^ {e _ {i} x} d G (y) d F (x) + \int_ {p / e _ {l}} ^ {\infty} \int_ {0} ^ {p - (e _ {l} - e _ {i}) x} d G (y) d F (x) \\ = \int_ {0} ^ {p / e _ {l}} G (e _ {i} x) d F (x) + \int_ {p / e _ {l}} ^ {\infty} G (p - (e _ {l} - e _ {i}) x) d F (x) \end{array}\tag{2}
$$

Hence, there are two categories of illegal users: one who are submarginal with respect to price, and their number is represented by the <sup>fi</sup>rst term above, and another who give up the legal version in favor of the pirated copy, and their number, $q _ { c } ,$ , has been de<sup>fi</sup>ned above.

The equilibrium is characterized by the above pair of simultaneous equations in $q _ { l }$ and $q _ { i } , \mathrm { i . e . }$ ., Eqs. (1) and (2). I will, henceforth, assume that the equilibrium is unique and stable.

Note that the right hand sides of 1 and 2 are also functions of $q _ { l }$ and $q _ { i } ,$ because $e _ { l }$ and $e _ { i }$ depend on $q _ { l }$ and $q _ { i \cdot }$ By solving these two equations for a given patching strategy, we can obtain $q _ { l }$ as a function of the price, $p .$ The carrier's problem for a given patching strategy is to then maximize pq . The strategy that leads to the highest maximum value for pq is the optimal patching strategy.

## 4. Homogeneous user base

In this section I assume that the cost of piracy $( y )$ is c for every user, i.e., $G ( y )$ is $. \mathrm { i f } y \ge c$ and it is 0 otherwise. This setting applies to software products designed for a limited audience, such as a statistical analysis tool targeted towards professionals, or a product like Microsoft Student that is intended for use by school-going students.

I continue to denote the distribution function of the intrinsic value (x) by F(x). I do not assume any speci<sup>fi</sup>c form for $F ( x )$ just as I do not for $e ( q )$ $\delta ( q _ { i } )$ and $\alpha ( q _ { i } )$ . Instead, I use properties of <sup>fi</sup>xed points [22] to evaluate the equilibrium demand and the revenue at the pro<sup>fi</sup>t maximizing price. If $\dot { p } { \leq } c ,$ irrespective of the patching strategy pursued:

$$
q _ {l} (p; I) = 1 - F \left(\frac {p}{1 + e (q _ {l} (p ; I))}\right)\tag{3}
$$

$$
q _ {i} (p; I) = 0\tag{4}
$$

In this scenario, no one pirates. Consequently, all patching strategies are equivalent. We now state this simple observation as a Lemma

Lemma 1. When $p { \leq } c ,$ irrespective of the patching strategy pursued, no one uses the pirated product. Therefore, all four patching strategies lead to the same profit.

In reality, this scenario, in which $p { \leq } c ,$ cannot be ruled out. The manufacturer may <sup>fi</sup>nd it optimal to choose a price that is less than or equal to c in the event c is large enough. Henceforth, we denote the solution to Eq. (3) by q<sup>∗</sup>(p).

We can now turn to the more interesting case where c is not very high, and the manufacturer <sup>fi</sup>nds it optimal to choose a price higher than c. When $p { > } C ,$ there are two possibilities. In one, the value of functionality patches is so large that no one uses the illegal version if it is denied the func tionality patch. This case occurs when $p ( 1 + e ( q _ { l } ^ { * } ( p ) ) - \beta ) { \leq } c ( 1 + e ( q _ { l } ^ { * } ( p ) ) )$ ). In this case, the demand for the legal and illegal versions are as follows:

$$
q _ {l} (p; I) = \left\{ \begin{array}{c l} 1 - F \bigg (\frac {p}{1 + e (q _ {l} (p ; I))} \bigg), & \text {if} I = P N, \\ 0, & \text {if} I = P A, \\ 1 - F \bigg (\frac {p}{1 + e (q _ {l} (p ; I))} \bigg), & \text {if} I = P S, \\ 1 - F \bigg (\frac {p - c}{\delta (q _ {i} (p ; I))} \bigg), & \text {if} I = P F. \end{array} \right.\tag{5}
$$

$$
q _ {i} (p; I) = \left\{ \begin{array}{c l} 0, & \text {if} I = P N, \\ 1 - F \bigg (\frac {c}{1 + e (q _ {l} (p ; I) + q _ {i} (p ; I))} \bigg), & \text {if} I = P A, \\ 0, & \text {if} I = P S, \\ F \bigg (\frac {p - c}{\delta (q _ {i} (p ; I))} \bigg) - F \bigg (\frac {c}{1 + e (q _ {l} (p ; I) + q _ {i} (p ; I)) - (\alpha (q _ {i} (p ; I)) + \delta (q _ {i} (p ; I)))} \bigg) & \text {if} I = P F. \end{array} \right.\tag{6}
$$

Note that the illegal demand above is non-negative only for PF and PA, i.e., only when functionality patches are offered. Otherwise, the cost of piracy, c, is so high relative to the value of the product minus functionality patches that no one uses the illegal version. Therefore, for PN and PS the demand for the legal version is what it would be in the absence of piracy. For PF, the demand, however, will depend on the security gap, $\delta ( q _ { i } )$

Lemma 2. When $p { > } c$ and $p ( 1 + e ( q _ { l } ^ { * } ( p ) ) - \beta ) { \leq } c ( 1 + e ( q _ { l } ^ { * } ( p ) ) )$ , the optimal patching strategy is either PN or PS.

In the only remaining case, in which $p { > } c$ and $p ( 1 + e ( q _ { l } ^ { * } ( p ) ) - \beta ) > c ( 1 + e ( q _ { l } ^ { * } ( p ) ) )$ , the equilibrium is given by the following equations:

$$
q _ {l} (p; I) = \left\{ \begin{array}{c l} 1 - F \bigg (\frac {p - c}{\beta + \delta (q _ {i} (p ; I))} \bigg), & \text { if } I = P N, \\ 0, & \text { if } I = P A, \\ 1 - F \bigg (\frac {p - c}{\beta} \bigg), & \text { if } I = P S, \\ 1 - F \bigg (\frac {p - c}{\delta (q _ {i} (p ; I))} \bigg), & \text { if } I = P F. \end{array} \right.\tag{7}
$$

$$
q _ {i} (p; I) = \left\{ \begin{array}{l l} F \bigg (\frac {p - c}{\beta + \delta (q _ {i} (p ; I))} \bigg) - F \bigg (\frac {c}{1 - \beta + e (q _ {l} (p ; I) + q _ {i} (p ; I)) - (\alpha (q _ {i} (p ; I)) + \delta (q _ {i} (p ; I)))}, \bigg) & \text {if} I = P N, \\ 1 - F \bigg (\frac {c}{1 + e (q _ {l} (p ; I) + q _ {i} (p ; I))} \bigg), & \text {if} I = P A, \\ F \bigg (\frac {p - c}{\beta} \bigg) - F \bigg (\frac {c}{1 - \beta + e (q _ {l} (p ; I) + q _ {i} (p ; I))} \bigg), & \text {if} I = P S, \\ F \bigg (\frac {p - c}{\delta (q _ {i} (p ; I))} \bigg) - F \bigg (\frac {c}{1 + e (q _ {l} (p ; I) + q _ {i} (p ; I)) - (\alpha (q _ {i} (p ; I)) + \delta (q _ {i} (p ; I)))} \bigg) & \text {if} I = P F. \end{array} \right.\tag{8}
$$

Lemma 3. When $p { > } c$ and $p ( 1 + e ( q _ { \iota } ^ { \ast } ( p ) ) - \beta ) > c ( 1 + e ( q _ { \iota } ^ { \ast } ( p ) ) )$ ), the optimal patching strategy is PN.

![](/api/attachments/DGZMD9QE/fulltext/images/b46e715fdc0668796b3e9940facdb683ca45c7ca0121b0da42306484c1e2deed.jpg)  
Fig. 2. Pro<sup>fi</sup>t vs. price for α=1, δ=1/2, β=1/8, e=1, and c=1/4.

It is evident from the three Lemmas above that PN weakly dominates the other strategies in each case. Hence, the theorem below follows.

Theorem 1. When all users face the same piracy cost, the optimal patching strategy is PN, i.e., it is optimal to not offer any patches to the pirates.

This is a simple, yet interesting, result. It shows that Microsoft's current strategy for its Windows system, PS, is not optimal for software prod ucts that have homogeneous user bases. In Microsoft's defense, the Windows system is used by businesses, professionals, individual users, stu dents, etc., and it is likely that these Windows users differ in their piracy costs—piracy costs are typically very high for businesses or professionals due to legal reasons and often low for students or other individuals. Another interesting aspect of this result is that, regardless of the positive network effect, not supporting pirates in any fashion turns out to be the best strategy. Clearly, this aspect is in con<sup>fl</sup>ict with earlier research that advocates supporting pirates in the presence of strong positive network effects. In later sections, I present results that cast additional doubts on earlier research and also explain why the results of this paper differ from earlier research.

The lesson, in summary, is that, when consumers are homogeneous with regard to the cost of piracy, they all have the incentive to switch to the illegal product unless the price of the legal product is suf<sup>fi</sup>ciently low or its quality is suf<sup>fi</sup>ciently high vis-à-vis that of the illegal product. The best option, is, therefore, to create as big a quality gap as possible in order to enhance the pricing power.

## 4.1. Numerical experiments: homogeneity in the piracy cost

Though the theorem makes it clear that PN is optimal, it is important to examine visually how different patching strategies impact pro<sup>fi</sup>ts. Fig. 2 shows how the pro<sup>fi</sup>ts for PN, PS, and PF compare at different prices when the cost of piracy is 0.25 for any consumer. It does not show PA, because, by assumption, PA leads to a zero pro<sup>fi</sup>t. The <sup>fi</sup>gure assumes that the distribution of the intrinsic value is uniform over [0, 2] and that the network effect and security gap functions are as follows: $\alpha ( q _ { i } ) = \alpha q _ { i } , \delta ( q _ { i } ) = \delta q _ { i }$ , and $e ( q ) = e q$ . The parameters—α, δ, β, e, and c—are as mentioned in the caption of the <sup>fi</sup>gure. As can be seen from the <sup>fi</sup>gure, PN dominates PF and PS at all prices above 0.25. At 0.25 and below, PN and PS are equivalent but both dominate PF. Therefore, PN weakly dominates PF and PS across the board, as is predicted by Theorem 1.

## 5. Heterogeneous user base

In this section, I assume that the cost of piracy (y) is 0 for a fraction t of the potential users and that it is very large for the rest, i.e., G(y) is t at any <sup>fi</sup>nite non-negative y while $G ( + \infty ) = 1 . { \ : } S 0 ,$ , while a fraction t chooses between buying and pirating, the remaining $( 1 - t )$ fraction chooses between buying and not using the software. This case essentially considers a setting, in which a fraction t of the market comprises individuals unlikely to face signi<sup>fi</sup>cant legal liabilities, and the rest comprises businesses and professionals, for whom the potential legal consequence of pi rating is extremely severe. This case, therefore, is more suitable to software products such as the Microsoft Windows operating system.

Instead of assuming that the intrinsic value distribution is identical for both types of users, I here assume that the distribution for the former group to be $F _ { 1 } ( x )$ and the distribution for the others to be $F _ { 2 } ( x ) , { \mathrm { i } } . \mathsf { e } .$ ., allow the possibility that the distributions of x and y are dependent. This generalization is necessary because the two groups are likely to have different intrinsic value distributions. The case, in which $F _ { 1 } ( x ) = F _ { 2 } ( x )$ would, therefore, be a special case of this model. Again, I do not assume speci<sup>fi</sup>c functional forms for $F _ { 1 } ( x )$ and $F _ { 2 } ( x )$ . The equilibrium lega and illegal demands in this case are as follows.

$$
q _ {l} (p; I) = \left\{ \begin{array}{l l} t \bigg (1 - F _ {1} \bigg (\frac {p}{\beta + \delta (q _ {i} (p ; I))} \bigg) \bigg) + (1 - t) \bigg (1 - F _ {2} \bigg (\frac {p}{1 + e (q _ {l} (p ; I) + q _ {i} (p ; I)) - \alpha (q _ {i} (p ; I))} \bigg) \bigg), & \text {if} I = P N, \\ (1 - t) \bigg (1 - F _ {2} \bigg (\frac {p}{1 + e (q _ {l} (p ; I) + q _ {i} (p ; I))} \bigg) \bigg), & \text {if} I = P A, \\ t \bigg (1 - F _ {1} \bigg (\frac {p}{\beta} \bigg) \bigg) + (1 - t) \bigg (1 - F _ {2} \bigg (\frac {p}{1 + e (q _ {l} (p ; I) + q _ {i} (p ; I))} \bigg) \bigg), & \text {if} I = P S, \\ t \bigg (1 - F _ {1} \bigg (\frac {p}{\delta (q _ {i} (p ; I))} \bigg) \bigg) + (1 - t) \bigg (1 - F _ {2} \bigg (\frac {p}{1 + e (q _ {l} (p ; I) + q _ {i} (p ; I)) - \alpha (q _ {i} (p ; I))} \bigg) \bigg), & \text {if} I = P F. \end{array} \right.\tag{9}
$$

![](/api/attachments/DGZMD9QE/fulltext/images/eefc28420ffd2ef4256fa807f2f4d8326cb149f812122412f107496b2f9bb267.jpg)  
Fig. 3. Pro<sup>fi</sup>t vs. price for α=3/2, δ=1/8, β=1/8 and $e = 1 / 2 .$

$$
q _ {i} (p; I) = \left\{ \begin{array}{c l} t F _ {1} \bigg (\frac {p}{\beta + \delta (q _ {i} (p ; I))} \bigg), & \text { if } I = P N, \\ t, & \text { if } I = P A, \\ t F _ {1} \bigg (\frac {p}{\beta} \bigg), & \text { if } I = P S, \\ t F _ {1} \bigg (\frac {p}{\delta (q _ {i} (p ; I))} \bigg), & \text { if } I = P F. \end{array} \right.\tag{10}
$$

Theorem 2. When consumers are heterogeneous with regard to their piracy costs as described above, the following holds:

(a). PS, the strategy of offering only the security related patches to pirates, dominates PA, the strategy of offering all patches.

(b). PN, the strategy of not offering any patches to pirates, dominates PF, the strategy of offering only the functionality patches.

(c). Therefore, the optimal strategy is either PS, the strategy of offering only the security patches to pirates, or PN, the strategy of not offering any patches.

(d). If the positive network effect is so high that no user with a high piracy cost forgoes the use of the software product (i.e., if the market is covered) PN is the optimal strategy

The key difference between the homogeneity case and the heterogeneity case is, therefore, that PS is suboptimal for the former but not for the latter. Theorem 2 is also consistent with Microsoft's recent strategy switch with regard to its Windows operating system. The Windows system serves a heterogeneous consumer base. For Windows Vista, Microsoft has decided to pursue PS, the strategy of offering only security patches to pirates; according to the theorem, this strategy is superior to PA, the strategy of offering all patches to pirates, which Microsoft pre viously used.

![](/api/attachments/DGZMD9QE/fulltext/images/b3a7f57c37a8aaf86624d5eeee810cba09c8ad8e601cc129abbe639860b17278.jpg)  
Fig. 4. Pro<sup>fi</sup>t vs. price for α=3/2, δ=1/8, β=1/8 and e=2.

Table 2  
Optimal pro<sup>fi</sup>t for δ= 1/8 and β= 1/8.

<table><tr><td></td><td>α=1.00</td><td>α=1.25</td><td>α=1.50</td><td>α=1.75</td></tr><tr><td rowspan="4">e=0.50</td><td>PN: 0.271</td><td>PN: 0.266</td><td>PN: 0.262</td><td>PN: 0.257</td></tr><tr><td>PS: 0.267</td><td>PS: 0.267</td><td>PS: 0.267</td><td>PS: 0.267</td></tr><tr><td>PF: 0.214</td><td>PF: 0.209</td><td>PF: 0.204</td><td>PF: 0.199</td></tr><tr><td>PA: 0.209</td><td>PA: 0.209</td><td>PA: 0.209</td><td>PA: 0.209</td></tr><tr><td rowspan="4">e=0.75</td><td>PN: 0.283</td><td>PN: 0.279</td><td>PN: 0.275</td><td>PN: 0.271</td></tr><tr><td>PS: 0.274</td><td>PS: 0.274</td><td>PS: 0.274</td><td>PS: 0.274</td></tr><tr><td>PF: 0.224</td><td>PF: 0.220</td><td>PF: 0.216</td><td>PF: 0.211</td></tr><tr><td>PA: 0.214</td><td>PA: 0.214</td><td>PA: 0.214</td><td>PA: 0.214</td></tr><tr><td rowspan="4">e=1.00</td><td>PN: 0.292</td><td>PN: 0.289</td><td>PN: 0.285</td><td>PN: 0.282</td></tr><tr><td>PS: 0.279</td><td>PS: 0.279</td><td>PS: 0.279</td><td>PS: 0.279</td></tr><tr><td>PF: 0.232</td><td>PF: 0.229</td><td>PF: 0.225</td><td>PF: 0.222</td></tr><tr><td>PA: 0.218</td><td>PA: 0.218</td><td>PA: 0.218</td><td>PA: 0.218</td></tr><tr><td rowspan="4">e=1.25</td><td>PN: 0.299</td><td>PN: 0.296</td><td>PN: 0.294</td><td>PN: 0.291</td></tr><tr><td>PS: 0.283</td><td>PS: 0.283</td><td>PS: 0.283</td><td>PS: 0.283</td></tr><tr><td>PF: 0.238</td><td>PF: 0.236</td><td>PF: 0.233</td><td>PF: 0.230</td></tr><tr><td>PA: 0.222</td><td>PA: 0.222</td><td>PA: 0.222</td><td>PA: 0.222</td></tr></table>

In this scenario as well, PN can be the best choice, if positive network effects are suf<sup>fi</sup>ciently strong. In reality, the market may not be completely covered. However, as we will soon see, the basic insight that a larger positive network effect tilts the balance in favor of PN, the strategy of not offering anything to pirates, still holds in a wider context. This is indeed surprising given well-known results in the literature that recommend a piracy-friendly approach in the presence of strong positive network effects [11]. I explain the intuition while discussing the numerical example below.

## 5.1. Numerical experiments: heterogeneity in the piracy cost

The equilibrium is not easy to solve in the closed form for types of heterogeneity that are more complex than the one described above. However, a great deal of insights can still be obtained by numerically solving Eqs. (1) and (2), which I present here. Also, in a real-life setting, it is unlikely that the distribution of the piracy cost will be centered at one or two mass points. Therefore, in this numerical example, I consider a more general form of consumer heterogeneity with regard to piracy costs: speci<sup>fi</sup>cally, I assume that the piracy cost is uniformly distributed. Since I am using a more general form here, neither can I limit my analysis to PS and PN only nor can I rule out PF and PA based on Theorem 2. Hence, I consider all four strategies in order to numerically verify to what extent the insights provided by Theorem 2 applies, and also explore circumstances in which PS dominates PN or vice versa.

The examples shown in Figs. 3 and 4 assume the following forms for the network effect and security gap functions: α $\mathop { ' } { q _ { i } } ) = \alpha q _ { i } , \delta ( q _ { i } ) = \delta q _ { i }$ and $e ( q ) = e q ,$ , where α, δ, and e are positive constants. Further, they assume that the distribution of the intrinsic value (x) is uniform over [0, 2], and the distribution of the cost of piracy (y) is uniform over [0, 1]; assuming both to be distributed uniformly over [0, 1] leads to similar re sults; but assuming identical distributions is not necessary. Recall that, for each strategy, I must <sup>fi</sup>rst solve q for different values of the price, p, in order to <sup>fi</sup>nd out the pro<sup>fi</sup>t at different price levels for that strategy; only then I will be able to compare different strategies.

Figs. 3 and 4 show how, for two different sets of parameter values, the equilibrium pro<sup>fi</sup>t varies with respect to the price for different patching strategies. Parameter values assumed for each <sup>fi</sup>gure are as mentioned below the <sup>fi</sup>gure. For each <sup>fi</sup>gure, I need to look at the maximum pro<sup>fi</sup>ts for the four strategies, i.e., I need to examine the peaks of the four pro<sup>fi</sup>t curves. The one with the highest peak corresponds to the optimal patching strategy.

In both <sup>fi</sup>gures PS outperforms PA; i.e., the peak of the pro<sup>fi</sup>t curve for PS is higher than that for PA. Further, PF and PA turn out to be dom inated in both situations, which is consistent with Theorem 2. Interestingly, PN outperforms PS in Fig. 4 but PS outperforms PN in Fig. 3. Note that the two <sup>fi</sup>gures assume identical parameter values except that Fig. 4 assumes a higher level of positive network effects (i.e.,a higher value for e). These two <sup>fi</sup>gures thus indicate that a strong positive network effect does not justify a more piracy-friendly approach. As is depicted by these two <sup>fi</sup>gures, a higher level of e indeed requires a more restrictive approach, again contradicting the <sup>fi</sup>ndings in [11]. In other words, the optimalit of PN at higher levels of positive network effects holds in a wider context

Let us now examine how the impact of the positive network effect depends on the level of negative network effects. Table 2 shows how op timal pro<sup>fi</sup>ts for the four strategies compare for different combinations of α, the level of negative network effects, and e, the level of positive net work effects. The table continues to assume the same parameter values for the other parameters, i.e., it assumes that β=1/8 and δ=1/8. The optimal strategy for each combination of and e is shown in bold.

There are two things that we can immediately infer from the table: one is that a higher level of negative network effects (i.e., a larger α) increases the attractiveness of PS, and the other is that a higher level of positive network effects (i.e., a larger e) increases the attractiveness of PN. Therefore, near the right-top corner of the table, the optimal strategy is PS. But, as we move towards the left-bottom corner, the optimal strategy becomes PN.

The fact that a larger α requires PS is not very surprising; it con<sup>fi</sup>rms our intuition that not securing illegal copies in the network can substantially lower the legal demand when negative network effects are large. However, what is counterintuitive is that a higher leve of positive network effects in this case requires PN, the least piracy-friendly approach. As we know from the existing literature, a higher level of positive network effects usually requires pursuit of strategies that lead to a larger user base, including strategies that lead to more illegal users.

I now explain why my results regarding positive network effects differ from those in the literature. Conner and Rumelt [11] focus on DRM The primary effect of DRM is on costs involved in procuring an illegal copy. When piracy costs go up, some pirates forgo the use of the software product and the user base shrinks. When the level of positive network effects is large, this shrinkage translates to a substantial decline in the legal users' willingness-to-pay for the product. As a result, the equilibrium demand curve shifts inwards, leading to lower pro<sup>fi</sup>ts.

On the contrary, denying pirates patches primarily impacts the gap between the legal and illegal versions of the product. It is still true that lowering the quality of the illegal version shrinks the user base. However, that shrinkage is only a secondary effect. The primary effect of strategic patching is on the cannibalization quantity. When strong positive network effects drive up the overall demand, i.e., the combined demand for the legal and illegal versions, it becomes necessary to ensure that it also translates to a higher demand for the legal product. As I show here, one way to incentivize users to adopt the legal product is to employ the restrictive strategy of limiting all patch distributions to legal users only.

Coming back to the Microsoft's situation, there are two possibilities: (a) its Windows system experiences a high α, making PS the optimal choice, or (b) the Windows system experiences a higher e vis-à-vis α, making PN the optimal choice, but Microsoft still uses PS to avoid negative publicity and public scrutiny likely to result from malicious attacks on computers running the Windows software. As is evident from the experiments above, PA does not seem an attractive option, which is perhaps why Microsoft no longer considers it an alternative. Interestingly, Table 2 shows that, both the gap between PN and PA and the one between PS and PA widen as e, the level of positive network effects, increases. PA therefore, appears to be an unlikely choice for any software maker whose products bene<sup>fi</sup>t from strong positive network effects. For them, as already mentioned, PN is the most effective option.

## 6. Conclusion

In this paper, I examine whether a software producer can bene<sup>fi</sup>t by offering certain patches free of cost to illegal users of its products, and, speci<sup>fi</sup>cally, whether doing so is an attractive option when positive network effects are large.

Offering security related patches to illegal users certainly makes the network more secure and increases legal users' willingness-topay for the product. But, doing so reduces the incentive to prefer the legal version to the illegal version. Offering functionality related patches also reduces the incentive to buy the legal version, but doing so contributes to the user base and positive network effects. In short, offering illegal users either kind of patches has its own upsides and downsides. I examine a model in which these two intertwined trade-offs are present simultaneously. I then study the equilibrium demand and optimal pro<sup>fi</sup>t for each strategy. The equilibrium model yields the following insights:

• The consumer heterogeneity with respect to piracy costs plays an important role in determining which patching strategy is optimal. Speci<sup>fi</sup>cally, offering security patches is often optimal when consumers are heterogeneous with regard to their piracy costs. When they are homogeneous, not offering pirates anything is the best strategy.

• A large positive network effect, contrary to prescriptions of the prior economic research on piracy, requires a less piracy-friendly strategy of not offering anything to pirates.

The <sup>fi</sup>rst insight is important because it has an implication for manufacturers. If a product is used by a diverse group of users (e.g., Microsoft's Windows System or Of<sup>fi</sup>ce Suite, which are used by both businesses as well as individuals), offering security patches can be reasonable: different user groups are likely to have different piracy costs; business or professionals will probably have a higher piracy cost on account of legal reasons, whereas younger individuals, who are unlikely to be legally pursued (see the recent New York Times article [25]), will have a much lower cost. However, the same strategy of offering security patches may not work when there is little heterogeneity, as it may be the case with certain products, such as Microsoft Dynamics, Microsoft Dynamics CRM, or Microsoft Project, which are all primarily used by businesses, or with Microsoft Student that is aimed at school-going students, or with a statistical software tool that is aimed at researchers. In summary, the implication is that products targeted to a single homogeneous market need to have a more restrictive patching policy than do products with a broader appeal, such as many Microsoft and Adobe products. When there is heterogeneity in piracy costs, it is easier to incentivize consumers with high piracy costs to buy it. However, when there is little or no heterogeneity, all consumers are attracted towards piracy, unless the price of the legal product is suf<sup>fi</sup>ciently low or the quality of the legal product is suf<sup>fi</sup>ciently higher than that of its pirated counterpart. In this situation, it is optimal for the manufacturer to degrade the pirated version as much as possible in order to incentivize them to pay a substantial price for the legal version.

The second insight makes it clear why, contrary to the common wisdom, stronger positive network effects may require a less piracyfriendly and a more restrictive patching strategy of not offering any patches to pirates. It shows that strategic patching and DRM are very different approaches to managing piracy. DRM and strategic patching both reduce piracy. However, DRM raises costs of piracy, which makes some illegal users forgo the use of the product, shrinking the overall user base in the process. A smaller user base cannot leverage high levels of positive network effects, and, as a result, it often means lower pro<sup>fi</sup>ts for the producer. On the other hand, strategic patching does not aim at raising piracy costs per se. It instead focuses on curbing the cannibalization of the legal demand by piracy. Hence, it is often the best choice when the overall demand is large due to strong positive network effects, and the critical task facing the software producer is that of translating the strong overall demand to a strong demand for the legal version. This <sup>fi</sup>nding is important because it shows that software producers enjoying strong positive network effects for their products need not follow the practice of encouraging illegal channels as often as recommended.

While the result regarding the reduced incentive to tolerate piracy in the presence of network effects is intriguing, it needs to be interpreted conservatively. As is true for any analytical work, this work examines a stylized setting. There are issues that have not been considered. One such issue is the manufacturer's ability to in<sup>fl</sup>uence piracy costs. The manufacturer may be able to increase the piracy cost to a user, either by implementing DRM or by pursuing legal options. I do not explicitly consider this issue in this work. However, considering this issue should not fundamentally alter the results of this paper. The distribution of the piracy cost may change as a result of the manufacturer's actions, but the main result will not change.

There is another issue, which is competition. In the case of hightechnology products, the common form of competition is differentiated price competition. While <sup>fi</sup>rms compete on price, they also compete on feature and quality. It is unlikely that any user would consider a Mac a perfect substitute for a PC. As long as the products are suf<sup>fi</sup>ciently differentiated and the market structure is that of a monopolistic competition, the insights of this work will apply. However, if they are close substitutes, the results may not apply: <sup>fi</sup>ercer competition will likely make the competing <sup>fi</sup>rms more supportive of piracy—because piracy can boost their install-bases and contribute towards positive network effects critical to establishing a dominant position. It is quite possible that, in earlier stages of the product life-cycle, the <sup>fi</sup>rms will tolerate piracy, but, at a later point in time, the largest or the most dominant <sup>fi</sup>rm will stop supporting the pirates, just as is predicted here. Additional research is, therefore, needed to <sup>fi</sup>nd out what would happen in a duopoly or oligopoly setting. Similarly, additional research is also needed to explore settings in which a software product is offered in multiple versions, e.g., Professional, Home Premium, etc. Despite these limitations, this paper would have achieved its objective if it has convinced the reader about the need to revisit the results of prior research, which claim that positive network effects offer manufacturers greater incentives to support piracy.

## Acknowledgments

I wish to thank participants of the 2011 Hawaii International Conference on System Sciences and the anonymous review team for their valuable comments.

## Appendix A. Lemmas, Proofs of Theorems

Lemma 4. Let $g ( x ; \ t ) \colon [ 0 , 1 ] \times T \to [ 0 , 1 ] ,$ , where x is a variable, t is a parameter, T is any ordered set, and $\forall t { \in } T , g ( x , t )$ is continuous in x and has a unique fixed point $x ( t ) . I f g ( x ; t )$ is monotone non-decreasing in t, so is x(t).

Proof of Lemma 4. The proof follows immediately from Corollary 1 of Milgrom and Roberts [22].

Lemma 5. Let $I _ { 1 }$ and $I _ { 2 }$ be two distinct patching strategies, i.e., $I _ { 1 } ,$ I ∈{PN, PA, PS, PF}. $I f ~ q _ { l } ( p ; ~ I _ { 1 } ) \geq q _ { l } ( p ; ~ I _ { 2 } ) ~ \forall p ,$ then $m a x _ { p } ( p q _ { l } ( p ;$ I-$\begin{array} { r } { \mathbf { \sigma } _ { 1 } ) ) \geq m a x _ { p } ( p q _ { l } ( p ; I _ { 2 } ) ) , i . e . } \end{array}$ , patching strategy ${ \bf \nabla } \cdot I _ { 1 }$ dominates patching strategy I<sub>2</sub> from the seller's viewpoint.

Proof of Lemma 5. Let the optimal prices for $I _ { 1 }$ and $I _ { 2 }$ be $p _ { 1 }$ and $p _ { 2 }$ respectively. $p _ { 1 } q _ { l } ( p _ { 1 } ; I _ { 1 } ) \ge p _ { 2 } q _ { l } ( p _ { 2 } ; I _ { 1 } )$ by optimality of $p _ { 1 } ,$ and it follows from q<sub>l</sub>(p<sub>2</sub>; $I _ { 1 } ) \ge q _ { l } ( p _ { 2 } ;$ I ) that p q (p ; $I _ { 1 } ) \ge p _ { 2 } q _ { l } ( p _ { 2 } ; ~ I _ { 2 }$ ). Therefore, $p _ { 1 } q _ { l } ( p _ { 1 } ; I _ { 1 } ) \ge p _ { 2 } q _ { l } ( p _ { 2 } ; I _ { 2 } )$

Proof of Lemma 1. The proof follows immediately from Eq. (7).

Proof of Lemma 2. The proof requires using Eq. (5), which is restated below, and 6. PA is obviously suboptimal. The demand in the case of PN or PS is obtained by solving:

$$
q _ {l} (p) = 1 - F \left(\frac {p}{1 + e \left(q _ {l} (p)\right)}\right).
$$

Therefore, the demand is $q _ { l } ^ { * } ( p )$ . The demand in the case of PF is obtained by solving:

$$
q _ {l} = 1 - F \left(\frac {p - c}{\delta (q _ {i})}\right).
$$

Without loss of generality, let $\delta ( q _ { i } ) = \gamma \delta ( q _ { i } )$ , where $\gamma = 1$ to begin with. Now, consider what would happen if γ increases slightly. Speci<sup>fi</sup>cally, let us consider how a new equilibrium would be attained. Clearly, the right hand side of Eq. (6) (i.e., the expression for $q _ { i } ,$ for the case PF) would decrease with γ. Therefore, by Lemma $4 , q _ { i } ,$ for a given $q _ { l } ,$ would be lower. Let us denote this new q by $q _ { i } ^ { 1 }$ . Substituting $q _ { i } ^ { 1 }$ into the expression for $q _ { l } \left( \mathrm { i . e . } \right.$ , the equation immediately above this paragraph), we would get a new value for $q _ { l } ,$ say $q _ { l } ^ { 1 }$ , which we will then have to substitute back into Eq. (6) to continue with the tatonnement process. If the equilibrium was stable to begin with, q must rise during the course of these iterations, as, otherwise, q would continue to drift lower (because of the network effect, $e ( q ) )$ , and, eventually, at the end of the tatonnement, both q and q would be reduced to zero, contradicting the notion of a stable equilibrium. Intuitively as well, this makes perfect sense, a small γ should imply that the pirated product competes very well with legal product, while a large γ should imply much less competition from the pirated product and a higher demand for the legal product.

Since a higher γ means a higher $q _ { l }$ at the same price $p ,$ the equilibrium pro<sup>fi</sup>t is increasing in $\gamma .$ In other words, if the manufacturer had the opportunity to control $\gamma ,$ it would have increased it at least until the point the pirated product got completely wiped out, ending up with a demand that is identical to what PN or PS leads to. Therefore, the maximum pro<sup>fi</sup>t that the manufacturer can make in the case of PF is no higher than what it makes in the case of PN or PS.

Proof of Lemma 3. When $p { > } c ,$ , Eq. (7) implies that $q _ { l } ( p ; P N ) \ge q _ { l } ( p ;$ PS) ∀p (since $\delta ( q _ { i } ) \geq 0 )$ . It follows from Lemma 5 that PN dominates PS. Also, PS trivially dominates PA.

Comparing PN and PF requires an argument similar to what we have used for Lemma 2. In a very similar manner, we can argue that the equilibrium pro<sup>fi</sup>t in the case of PN is decreasing in $\beta .$ Therefore, the pro<sup>fi</sup>t would be the lowest when $\beta = 0 .$ . However, when $\beta = 0 ,$ the pro<sup>fi</sup>t would be the same as what it is for PF. Therefore, at any $\beta > 0 ,$ , PN is superior to PF.

Proof of Theorem 1. The proof follows immediately from Lemmas 1, $^ { 2 , }$ and 3.

## Proof of Theorem 2.

(a)–(c) From Eqs. (9) and (10) it follows that:

$$
q _ {l} (p; P A) = (1 - t) \left(1 - F _ {2} \left(\frac {p}{1 + e (q _ {l} (p ; P A) + t)}\right)\right).\tag{11}
$$

and, that:

$$
\begin{array}{l} q _ {l} (p; P S) - t \left(1 - F _ {1} \left(\frac {p}{\beta}\right)\right) \\ = (1 - t) \left(1 - F _ {2} \left(\frac {p}{1 + e \left(q _ {l} (p ; P S) + t F _ {1} \left(\frac {p}{\beta}\right)\right)}\right)\right) \\ = (1 - t) \left(1 - F _ {2} \left(\frac {p}{1 + e \left(q _ {l} (p ; P S) - t \left(1 - F _ {1} \left(\frac {p}{\beta}\right)\right) + t\right)}\right)\right). \end{array}\tag{12}
$$

Comparing Eqs. (11) and (12), we get:

$$
q _ {l} (p; P S) - t \left(1 - F _ {1} \left(\frac {p}{\beta}\right)\right) = q _ {l} (p; P A).
$$

Therefore, at any price $q _ { l } ( p ; \ P S ) { \geq } q _ { l } ( p ; \ P A )$ . And, it follows from Lemma 5 that PS dominates PA. Now, for both PN and PS, we have:

$$
q (p; I) = t + (1 - t) \left(1 - F _ {2} \left(\frac {p}{1 + e (q (p ; I)) - \alpha \left(q _ {i} (p ; I)\right)}\right)\right),\tag{13}
$$

where q(p; $I ) = q _ { l } ( p ; I ) + q _ { i } ( p ; I )$

Eq. (10) and Lemma 4 imply that $q _ { i } ( p ; P F ) \ge q _ { i } ( p ; P N )$ . Since the right hand side of Eq. (13) is a decreasing function of $q _ { i } ( p ; I )$ , it follows from Lemma 4 that q(p; $P F ) { \le } q ( p ; ~ P N )$ Since q (p; $P F ) { \geq } q _ { i } ( p ; ~ P N )$ and $q _ { l } ( p ; ~ P F ) + q _ { i } ( p ; ~ P F ) = q ( p ;$ $P F ) { \leq } q ( p ; P N ) { = } q _ { l } ( p ; P N ) + q _ { i } ( p ; P N )$ , it must be true that q (p; $P N ) { \geq } q _ { l } ( p ; P F )$ and that PN dominates PS (by Lemma 5).

(d) When e(q) is so large that the market is covered, $q _ { l } ( p ; I ) =$ $1 - q _ { i } ( p ; I )$ . The rest of the proof is similar—using Eq. (10), one can show that $q _ { i } ( p ; \ P N ) \le q _ { i } ( p ; \ P S )$ , which would then imply that $q _ { l } ( p ; P N ) \ge q _ { l } ( p ;$ PS) and that PN is optimal (by Lemma 5).

## References

[1] AP, Microsoft to cripple computers running pirated copies of Vista, WSJ.com, , October 4 2006.

[2] A. Arora, R. Telang, H. Xu, Optimal time disclosure of software vulnerabilities, Management Science 54 (2008) 642–656.

[3] T. August, T. Tunca, Network software security and user incentives, Management Science 52 (2006) 1703–1720.

[4] T. August, T. Tunca, Let the pirates patch? An economic analysis of network software security patch restrictions, Information Systems Research 19 (2008) 48–70.

[5] H. Bhargava, V. Choudhary, Information goods and vertical differentiation, Journal of Management Information Systems 18 (2001) 89–106.

[6] H. Bhargava, V. Choudhary, Research note: when is versioning optimal for information goods? Management Science 54 (2008) 1029–1035.

[7] BSA, Sixth Annual BSA-IDC Global Software 08 Piracy Study, Business Software Alliance Publication, May 2009.

[8] R. Chellappa, S. Shivendu, Managing digital piracy: pricing and sampling strategies for digital experience goods in vertically segmented markets, Information Systems Research 16 (2005) 400–417.

[9] Y.N. Chen, I. Png, Information goods pricing and copyrights enforcement: welfare analysis, Information Systems Research 14 (2003) 107–123.

[10] W.Y. Cho, B.H. Ahn, Versioning of information goods under the threat of piracy, Information Economics and Policy 22 (2010) 332–340.

[11] K. Conner, R. Rumelt, Software piracy: an analysis of protection of strategies, Management Science 37 (1991) 125–139.

[12] J. Evers, Windows worms knocking out computers, CNETNews.com, , August 17 2005.

[13] I. Fried, In an effort to boost sales of Windows, Microsoft has its sights set on its nearest competitor, CNETNews.com, February 3 2005.

[14] R. Gopal, G. Sanders, Preventive and deterrent controls for software piracy, Journal of Management Information Systems 14 (1997) 29–47.

[15] S. Jain, Digital piracy: a competitive analysis, Marketing Science 27 (2008) 610–626.

[16] J. Jaisingh, Impact of piracy on innovation at software <sup>fi</sup>rms and implications for piracy policy, Decision Support Systems 46 (2009) 763–773.

[17] R. Jones, H. Mendelson, Information goods vs. industrial goods: cost structure and competition, Management Science 57 (2011) 164–176.

[18] M. Katz, C. Shapiro, Network externalities, competition, and compatibility, The American Economic Review 75 (1985) 424–440.

[19] A. Lahiri, D. Dey, The effect of piracy on the quality of information goods, Working Paper, 2011 Available at, SSRN:http://ssrn.com/abstract=1868659

[20] E. Larkin, Critical Windows security patch butts heads with HP software PCWorld.com, , April 17 2006.

[21] D. Lee, H. Mendelson, Adoption of information technology under network effects, Information Systems Research 18 (2007) 395–413.

[22] P. Milgrom, J. Roberts, Comparing equilibria, The American Economic Review 84 (1994) 441–459.

[23] I. Novos, M. Waldman, The effect of increased copyright protection: an analytical approach, Journal of Political Economy 92 (1984) 236–246.

[24] O. Shy, J.-F. Thisse, A strategic approach to software protection, Journal of Economics and Management Strategy 8 (1999) 163–190.

[25] B. Sisario, To slow piracy, internet providers ready penalties, NYTimes.com, , Jul 7 2011.

[26] A. Sundararajan, Nonlinear pricing of information goods, Management Science 50 (2004) 1660–1673.

[27] S.Y. Wu, P.-Y. Chen, Versioning and piracy control for digital information goods, Operations Research 56 (2008) 157–172.

[28] S.Y. Wu, P.-Y. Chen, G. Anandalingam, Fighting information goods with versioning, in: Proceedings of the Twenty-Fourth International Conference on Information Systems (2003) p. Paper 51.

![](/api/attachments/DGZMD9QE/fulltext/images/6217f6dc5492dd08430adcc7244dd75fdb064bee27a3e9860143b57e4e12ef74.jpg)  
Atanu Lahiri is an Assistant Professor of Information Systems at the Foster School of Business, University of Washington. He received his PhD from the Simon School of Business, University of Rochester. His research interests include pricing of telecommunication services, economics of software security and piracy, and application of information technology in healthcare. His earlier work has appeared in the Journal of Management Information Systems and the Journal of the American College of Radiology. His recent work is to appear in Manufacturing & Service Operations Management.
