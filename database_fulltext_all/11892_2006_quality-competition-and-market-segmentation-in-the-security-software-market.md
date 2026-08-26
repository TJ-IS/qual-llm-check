---
otero_id: 11892
otero_key: "CT44SBG4"
title: "Quality Competition and Market Segmentation in the Security Software Market"
authors: "Debabrata Dey; Atanu Lahiri; and Guoying Zhang"
year: "2006"
journal: "MIS Quarterly"
doi: "10.25300/misq/2014/38.2.12"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# QUALITY COMPETITION AND MARKET SEGMENTATION IN THE SECURITY SOFTWARE MARKET<sup>1</sup>

Debabrata Dey and Atanu Lahiri

Michael G. Foster School of Business, University of Washington, Seattle, Seattle, WA 98195 U.S.A. {ddey@uw.edu} {lahiria@uw.edu}

Guoying Zhang Dillard College of Business, Midwestern State University, Wichita Falls, Wichita Falls, TX 76308 U.S.A. {grace.zhang@mwsu.edu}

In recent years, we have witnessed an unprecedented growth in the security software market. This market is now fiercely competitive with hundreds of nearly identical products; yet, the price is high and coverage low. Although recent research has examined such idiosyncrasies and found the existence of a negative network effect as a possible explanation, several important questions still remain: (1) What possibly discourages product differentiation in such a competitive market? (2) Why is versioning absent here? (3) How does the presence of free alternatives in this market impact its structure? We develop a comprehensive oligopoly model, with endogenous quality and versioning decisions, to address these issues. Our analyses reveal that, although the presence of numerous competitors leads to a greater need to differentiate, the network effect in this market works as a counterweight, incentivizing vendors to sacrifice differentiation in favor of collocating in the top end of the quality spectrum. We explain the reasons and implications of this important finding. We further show that this result is robust and applicable even when versioning by competing vendors or the presence of free software is taken into consideration. Furthermore, given that the presence of free software actually intensifies competitive pressure and heightens the need to differentiate, the role of the network effect in abating differentiation becomes even more discernible.

Keywords: Security software, network effect, negative network effect, quality competition, market structure, vertical differentiation, fulfilled expectations equilibrium

## Introduction

The industry of security software, along with that of related hardware and services, has grown rapidly in response to a higher demand for the protection of an ever-increasing base of information technology (IT) infrastructure. According to the Gartner Group (2006, 2012), the worldwide security software revenue has increased at a compound annual rate of 15.6 percent—from nearly US\$6.4 billion in 2004 to about US\$17.7 billion in 2011 (see Figure 1). Understanding the nature of this market and gaining insights on relevant competitive strategies are, therefore, of interest to academicians as much as they are to software vendors and consumers. There are two main categories of security software: (1) off-the-shelf third-party tools, such as antivirus, anti-spyware, web filter, anti-spamware, and anti-phishing, and (2) system components, such as encryption software and firewalls that are usually included in the operating system (Dey et al. 2012). In this research, we examine only the first category, which dominates the security software market and has several major players, including Symantec, Trend Micro, McAfee, Kaspersky, and several dozen others.<sup>2</sup> The security software market is fascinating. A recent survey finds that there are 257 antivirus products in North America and 367 worldwide (OPSWAT 2012); we are, in fact, unaware of any other market, software or otherwise, where so many nearly identical products coexist. Despite the presence of a large number of products, the price for this type of software has remained relatively high. For example, an annual subscription to Norton Internet Security 2012 can cost as much as US\$80; a three-year subscription can cost up to US\$165, which is well above the price of Microsoft Word 2010, a product that enjoys greater monopoly power and also offers a perpetual license. Furthermore, in spite of so many choices in the marketplace, a significant percentage of individual computers are still lacking in basic protection (Eichorn and Smith 2011). Dey et al. (2012) recognize the competitive nature of this market and, using a Cournot oligopoly model, show that the presence of a negative network effect furnishes possible explanations for some of these unique characteristics.<sup>3</sup>

![](/api/attachments/CT44SBG4/fulltext/images/05d5be6ab85e42243565109f711525ce4d74c5e6746bbae8d326935d5d607f9f.jpg)  
Figure 1. Growth of Worldwide Security Software Market (Source: Gartner Group press releases)

What is most fascinating, though, is the fact that all these products happen to be quite similar. This is intriguing because, given the fiercely competitive nature of this market, prior research would actually predict a significant level of quality differentiation among competing products (e.g., Moorthy 1988; Motta 1993; Shaked and Sutton 1982). Yet, as we show in the next section, vertical differentiation is practically absent from this market. Another curious aspect is the presence of free security software, such as the ones now being offered by Avast, AVG, Avira, and Microsoft, among others. Apparently, their introduction in recent years has had little influence on the market structure and the nature of competition. Prior research does not shed any light on these issues. Specifically, three important and related, yet unanswered, questions remain:

Why, despite the highly competitive nature of the security software market, do we observe so little vertical differentiation in practice, when it is well known that such differentiation can ease the competitive pressure?

As a related issue, why is versioning hardly used in the security software market, even when such versioning is often costless and also effective in segmenting consumers heterogeneous in their preference for quality?

What strategy should a vendor adopt in the presence of free software, and how does it impact the overall market?

Central to these issues is the concept of quality, which is absent from related prior research (e.g., Dey et al. 2012). In this work, we develop a comprehensive analytical model to better reflect the current realities of this marketplace by endogenizing the vendors’ quality and versioning decisions as parts of their overall strategy. We also examine how these decisions are impacted by the presence of free software. Although this generalization leads to a more complex model and sacrifices some analytical tractability, it also provides us with the economic tools necessary for a more complete analysis of the security software market. Overall, our model paints a richer picture of the market, leading to critical insights for vendors on quality competition.

One of the important results of this paper is that the network effect, which results from consumers’ free-riding tendencies with respect to indirect security threats (Dey et al. 2012), makes vertical differentiation less appealing. The primary reason quality differentiation is commonly observed in many other markets is that such differentiation allows manufacturers to relax competition. Some manufacturers target valueseeking consumers and others quality-seeking ones, in effect reducing competition among vendors targeting different segments. This way, quality differentiation expands the market coverage by providing cheaper alternatives to valueseeking consumers who are often reluctant to buy expensive high-end products. However, the network effect—which, at a higher level of market coverage, heightens consumers’ freeriding behavior and substantially reduces their willingness-topay (WTP)—makes market expansion a less attractive proposition. In the end, it disincentivizes security software vendors from adopting quality differentiation.

We make three contributions. First, we raise important questions about the security software market—above and beyond what has been addressed before—and find economic intuitions behind its unique structure. These insights are critical not only to software vendors and security experts but also to consumers of such products, and can provide a useful starting point for public policy debates. Second, we show that these insights are robust and applicable in the presence of free software, as well as in situations where vendors are allowed to offer multiple versions. Finally, we make an important methodological contribution. To the best of our knowledge, a Cournot oligopoly model with many players, each potentially offering an arbitrary number of quality levels, has not been previously formulated, let alone studied, in either economics or information systems literature, with or without network effects.

## Real-World Observations about Quality Differentiation

Although quality is a multidimensional concept, in our context, it is a measure of the ability of security software to thwart attacks. In this sense, quality is a vertical attribute here, consistent with the literature on vertical differentiation (e.g., Mussa and Rosen 1978); it is unlikely that, all else equal, a user would prefer a security solution that is less effective in guarding against security threats. A reasonable proxy for this quality or effectiveness against threats could be the set of security-related features a product offers.<sup>4</sup> In this respect, we find that most vendors offer nearly identical products, despite being in a severely competitive market. Consider, for example, the list of antivirus software products shown in Table 1; the products shown in this table are the top 20 products as rated by Top Ten Reviews (2012). It is easy to see that these products charge comparable prices and are quite similar with nearly identical feature content. In particular, almost all of them provide the complete set of protection scope, scanning, and cleaning features, which are central for a software product of this type (Egan 2012). The percent feature coverage reported in Table 1 further indicates that several vendors indeed provide the full range of features while others offer a large majority. In fact, we have looked at many other products and have hardly noticed any significant difference in their feature coverage.

It may be argued, however, that the feature content of a product does not fully reflect its effectiveness and may not be the only indicator of quality. In fact, prior research has considered product ratings from well-known secondary sources as a measure of quality, and has found that “there is no broad consensus across these sources in terms of the perceived quality of these products” (Dey et al. 2013, p. 3993). Further, comparing the ratings from various sources using statistical tests, Dey et al. have shown that there is little variation in the average normalized score across different products, again pointing to a lack of quality differentiation in this market.

This lack of differentiation is intriguing. In practice, when market competition is fierce, vendors often resort to product differentiation, vertical or horizontal. As a result, it is difficult to find an industry where a very large number of firms compete with identical product or service offerings. In the security software market, horizontal differentiation seems impractical, because such a software product runs in the background requiring minimal user interaction and, therefore, has little to do with users’ idiosyncratic preferences. Naturally, one would expect this market to exhibit a significant level of vertical differentiation, a strategy often adopted by vendors to ease the level of competition when consumers differ in their WTP for quality (Moorthy 1988; Motta 1993; Shaked and Sutton 1982). Yet, as discussed above, vertical differentiation in this market is conspicuous in its absence. An important point of this paper is to understand this apparent anomaly, in addition to providing a comprehensive model of competition that considers other noticeable anomalies such as the presence of free software. This understanding is of much significance for vendors and consumers alike, since information security is a major concern these days and the market for security software has become one of the most prominent software markets because of its current size and the rapid growth trajectory.

Table 1. Antivirus Software Features

<table><tr><td>Software</td><td>BD</td><td>Kky</td><td>Pnd</td><td>FS</td><td>AVG</td><td>Avs</td><td>GD</td><td>BG</td><td>Avr</td><td>Est</td><td>Nrt</td><td>Vpr</td><td>TM</td><td>Mcf</td><td>Wrt</td><td>TD</td><td>Nrm</td><td>Esc</td><td>TP</td><td>ZA</td></tr><tr><td colspan="21">Protection Scope:</td></tr><tr><td>Anti-malware</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Anti-virus</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Anti-trojan</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Anti-spyware</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Anti-worm</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Anti-roolkit</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Anti-phishing</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td></td><td>√</td><td>√</td><td>√</td></tr><tr><td colspan="21">Scanning:</td></tr><tr><td>Real-time scanning</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>On-demand scanning</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Scheduled scanning</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Heuristic scanning</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Manual scanning</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Compressed file scanning</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td colspan="21">Cleaning:</td></tr><tr><td>Auto-clean infected files</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Quarantine infected files</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td colspan="21">Internet and E-mail:</td></tr><tr><td>Browser exploits</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr><tr><td>Outbound email protection</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Inbound email protection</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Instant messaging protection</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td></td><td>√</td><td></td></tr><tr><td colspan="21">System-Related:</td></tr><tr><td>Bootable rescue CD</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>Registry startup protection</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Gamer mode protection</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td></tr><tr><td>Auto-USB detection</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td></td><td></td><td>√</td><td></td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td><td></td><td>√</td><td>√</td><td></td></tr><tr><td>Feature Coverage (%)</td><td>100</td><td>100</td><td>100</td><td>87</td><td>100</td><td>96</td><td>91</td><td>96</td><td>91</td><td>100</td><td>100</td><td>96</td><td>87</td><td>91</td><td>87</td><td>83</td><td>78</td><td>100</td><td>83</td><td>87</td></tr><tr><td>Annual Subscription (US $)</td><td>80</td><td>90</td><td>70</td><td>60</td><td>70</td><td>70</td><td>50</td><td>60</td><td>127</td><td>80</td><td>80</td><td>70</td><td>90</td><td>90</td><td>80</td><td>80</td><td>76</td><td>50</td><td>78</td><td>80</td></tr><tr><td colspan="21">BD = BitDefender; Kky = Kaspersky; Pnd = Panda; FS = F-Secure; Avs = Avast; GD = G Data; BG = BullGuard; Avr = Avira; Est = ESET; Nrt = Norton; Vpr = Vipre; TM = Trend Micro; Mcf = McAfee; Wrt = Webroot; TD = Total Defense; Nrm = Norman; Esc = eScan; TP = TrustPort; ZA = ZoneAlarm</td></tr></table>

Source: Feature information from Top Ten Reviews (2012); regular subscription prices from vendor websites, as of December 1, 2012

We also seek an answer to a related question: Can segmentation occur in this market as a result of vendors resorting to versioning? Even in the near-monopolistic traditional software market, it is not uncommon that a vendor sells several different versions of the same product. For example, Microsoft packages basically the same Windows operating system differently for home and professional users. Similarly, Oracle offers express versions of its database software to target different market segments. On the other hand, in the security software market, vendors rarely offer degraded or “express” versions simultaneously with their full versions. Symantec, one of the leading vendors, offers only one version of Norton Internet Security; its variations available today differ in dimensions that are not related to quality. For example, an annual subscription is more costly per unit time than a biannual subscription, but this is akin to volume discounting and there is no versioning, per se. Similarly, Norton customers also have the option of purchasing the Norton 360 suite, a bundle containing Norton Internet Security along with other tools such as a 2 GB online storage facility and a utility software for tuning personal computers; there is no versioning in that case either. Similar strategies are also used by other major vendors. Therefore, it is only natural to ask whether a detailed economic model can provide some conceptual support for this anomaly, as well. Besides, this exercise is also critical to ensuring that any result obtained with respect to quality competition is both robust and realistic.

## Literature Review

Researchers have long explored the role of the positive network effect and how it affects competitive outcomes in markets for software and other types of goods (Katz and Shapiro 1985). Unlike traditional software markets, this positive network effect is not observed in the security software market—a consumer’s WTP for security software does not go up when others procure security software. This is because, from the perspective of a consumer, security software is just a tool for preventing security exploitations, and there is hardly any benefit from the compatibility of user data. On the contrary, there is a network effect, which arises from the fact that a consumer’s WTP can, in fact, go down as others procure security software. Such negative network effects have received considerable attention from researchers in recent years. Png and Wang (2009) have shown that the negative network effect arising from strategic hacker behavior can provide a possible explanation for users’ inertia in taking security precautions. As more users adopt security software, hackers find it less profitable to launch new attacks, which, in turn, make the non-adopters less likely to adopt security solutions. Dey et al. (2012) have argued that a negative network effect can also arise from indirect attacks, where a system is not a direct target but could become an eventual target from security exploitations of other systems. Typical examples of indirect attacks include Internet worms and BOTNET agents, which could launch large-scale attacks with the ability to convert ordinary nodes into malicious agents. The larger the market coverage of security software, the less would be the chance that a consumer gets infected from others, and so would be his willingness to subscribe to a security solution.

It is worth mentioning here that, despite some overlap, our model is quite different from the recent literature on application software.

August and Tunca (2006, 2008) and Lahiri (2012) recognize the existence of a similar network effect and develop economic models in which a consumer’s valuation for an application software—or an operating system—depends on the number of unpatched vulnerable copies of that software in the user network. In their models, the larger the number of vulnerable nodes, the lower is the valuation of the application product. What we have here is exactly the opposite: the larger the chance of an indirect infection, the higher is the value of a security software.

Galbreth and Shor (2010) examine the consequences of hackers targeting popular applications or platforms, resulting in a product-level or “localized” network effect. In fact, the positive network effect in Katz and Shapiro and the negative network effect in Galbreth and Shor are both different from the market-level or “global” network effect that we model here: in our case, every user using a security software contributes to the security of all others, irrespective of whether the other users are using the same security software, a different one, or none at all.

Also related to this work is the vast body of literature in economics and marketing that examines the efficacy of vertical differentiation in various settings (e.g., Moorthy 1988; Motta 1993). Often, the conclusion is that differentiation is optimal as it relaxes competition (Shaked and Sutton 1982). Although this stream of work is quite influential, it does not directly apply to information goods. Information goods have a different cost structure (Jones and Mendelson 2011; Shapiro and Varian 1999). Furthermore, network effects are usually not relevant to physical goods. Table 2 provides a comparison of our work with the stream of work on physical goods, as well as the related stream on information goods.

As indicated in Table 2, we endogenize not only the quality decisions of vendors but also their versioning decisions. There is considerable literature on versioning of information goods, and quality differentiation in general. Researchers have argued that versioning is suboptimal for a monopolist, mainly because information goods have a zero marginal cost (Bhargava and Choudhary 2001, 2008). Although earlier research on quality differentiation mostly focused on monopoly, researchers have recently turned their attention to competition. Using a two-stage Bertrand duopoly model, in which competing vendors choose quality in the first stage and price in the second, Wei and Nault (2008) show that the cost structure of information goods makes versioning suboptimal even in competitive settings. Since Jones and Mendelson (2011) use the same two-stage Bertrand setting, following the recommendations of Wei and Nault, they limit themselves to the case in which each vendor offers exactly one version. Jones and Mendelson find that the equilibrium in the market for an information good is more asymmetric vis-à-vis that for a physical good, in the sense that vendors in the former differentiate even more in terms of quality. However, neither work is directly applicable to our context. As mentioned in Table 2, we consider a single-stage Cournot oligopoly, a setting most relevant to the context of security software (Dey et al. 2012). The papers mentioned above also do not consider the presence of any negative network effect that is central to our analysis. Not surprisingly, perhaps, we reach a very different conclusion that the market for an information good can indeed be symmetric, particularly so when it experiences a strong network effect.

## Consumer Model

We consider a market for security software, where consumers (users) are heterogeneous: the amount of benefit from thwarting an attack varies from user to user. In order to capture this heterogeneity, users are indexed by a parameter u that indicates their expected benefit if an attack is thwarted;

it can also be viewed as a proxy for the potential loss to a user from an attack (Gordon and Loeb 2002). Without loss of generality, we normalize the maximum expected benefit to 1.

Assumption 1. The index u is uniformly distributed over the interval [0, 1].

Hackers engage in two types of attacks: mass attacks and targeted attacks (Dey et al. 2012; Png and Wang 2009). These types of attacks can be explained by the choice and chance models of hacker behavior (Ransbotham and Mitra 2009). Mass attacks essentially follow the path of chance; here, hackers create and distribute exploits with the objective of infecting as many computers as possible, and they do not chase specific targets. Targeted attacks, on the other hand, follow a path of choice, where hackers primarily preselect certain targets. In this paper, we develop the model only for mass attacks; extending our analysis to include targeted attacks along the lines of Dey et al. (2012) is conceptually straightforward.

Mass attacks make use of generic exploits that are capable of breaching the security of a large variety of users (CISCO 2011; Ransbotham and Mitra 2009). These attacks consist of direct and indirect attacks. Accordingly, there are two types of benefits to be derived from adopting a security software: direct and indirect. To better understand these benefits, let us first consider a single security software characterized by a quality parameter θ, $0 < \theta \leq 1$ , which can also be viewed as the effectiveness of the security software: by installing the software, a user is able to thwart a fraction θ of all the attacks, direct or indirect. Therefore, if the average rate of direct attacks is λ, user u gets a direct mitigation benefit of λθu per unit time by adopting a security software of quality θ. Henceforth, without loss of generality, we set λ = 1.

Next, we consider the indirect benefit. Unprotected systems might replicate malicious codes and pass them to connected peers. At times, a hacker may attack a system indirectly, after first breaching the security of several other systems and using them as launching pads. In other words, the existence of security software in one system can, indirectly, reduce attacks to others. Let x be the fraction of users who have adopted the security software of quality θ. Then, the probability that a randomly selected node is not breached is θx, implying that the probability of such a node being exploited as a launching pad is simply (1 – θx). Hence, we assume the rate of indirect attacks to be g(1 – θx), where g is a model parameter representing the strength of the network effect from indirect attacks—the higher g is, the larger is the potential indirect benefit. It is now obvious that a larger market share (larger x) leads to a reduction in this indirect benefit, creating an incentive for non-adopters to free-ride on those who have already adopted. At the extreme, if all users are equipped with security software of perfect quality, no user derives any indirect benefit. A user adopting a security software of quality $\theta ,$ therefore, avoids indirect attacks from the unprotected users and derives an indirect benefit of θgu(1 – θx).

<table><tr><td colspan="8">Table 2. Related Literature on Quality Differentiation</td></tr><tr><td>Article</td><td>Product Type</td><td>Competition Model</td><td>Decision Variables</td><td>Versioning Endogeneous</td><td>Quality Endogeneous</td><td>Network Effect Modeled</td><td>Main Finding</td></tr><tr><td>Bhargava and Choudhary (2001) Bhargava and Choudhary (2008)</td><td>Information</td><td>None (Monopoly)</td><td>Quality, price</td><td>Yes</td><td>No</td><td>No</td><td>Versioning is not an optimal strategy for the monopolist provider of a good with zero marginal cost.</td></tr><tr><td>Dey et al. (2012)</td><td>Information</td><td>1-stage Cournot</td><td>Quantity</td><td>No</td><td>No</td><td>Yes</td><td>A negative network effect explains the competitive nature of the security software market, as well as its high price and low coverage.</td></tr><tr><td>Jones and Mendelson (2011)</td><td>Information and physical</td><td>2-stage Bertrand</td><td>Quality, price</td><td>Yes</td><td>Yes</td><td>No</td><td>Markets for information goods are more differentiated than those for physical ones because of the differences in their cost structures.</td></tr><tr><td>Moorthy (1988)</td><td>Physical</td><td>2-stage Bertrand</td><td>Quality, price</td><td>No</td><td>Yes</td><td>No</td><td>Vertical differentiation relaxes price competition.</td></tr><tr><td>Motta (1993)</td><td>Physical</td><td>2-stage Bertrand 2-stage Cournot</td><td>Quality, price Quality, quantity</td><td>No</td><td>Yes</td><td>No</td><td>Bertrand competition leads to a larger quality differentiation than Cournot.</td></tr><tr><td>Shaked and Sutton (1982)</td><td>Physical</td><td>3-stage Bertrand</td><td>Entry, quality, price</td><td>No</td><td>Yes</td><td>No</td><td>A market can sustain at most two firms, and they will differentiate in quality.</td></tr><tr><td>Wei and Nault (2008)</td><td>Information</td><td>2-stage Bertrand</td><td>Quality, price</td><td>Yes</td><td>Yes</td><td>No</td><td>Although versioning may not be optimal otherwise, it can be an effective tool for entry deterrence.</td></tr><tr><td>This work</td><td>Information</td><td>1-stage Cournot</td><td>Quality, quantity</td><td>Yes</td><td>Yes</td><td>Yes</td><td>A negative network effect explains the lack of quality differentiation and versioning in the fiercely competitive security software market.</td></tr></table>

The total benefit (per unit time) to user u from adopting the software of quality θ, in a market with coverage x, can then be written as $B _ { u } = \theta u + \theta g u ( 1 - \theta x ) = \theta u { \big ( } 1 + g ( 1 - \theta x ) { \big ) }$ . Security software products are usually licensed as a subscription for a fixed time period; let $p$ be the subscription price (per unit time). The net benefit to user u from adopting the security software is then given by

$$
B _ {u} - p = \theta u (1 + g (1 - \theta x)) - p\tag{1}
$$

We now extend our analysis by discussing how a consumer would behave when multiple security software products are available to him, each possibly with a different quality level. We assume that a consumer would choose only one of these products.<sup>5</sup> Consider n different products; the quality level of the $i ^ { \mathrm { { t h } } }$ one is denoted by $\theta _ { i } , i = 1 , 2 , . . . , n .$ Therefore, a consumer using the $i ^ { \mathrm { { t h } } }$ product is able to thwart attacks with a probability of $\theta _ { i } .$ . Without loss of generality, we assume the following ordering:

$$
0 \leq \theta_ {1} \leq \theta_ {2} \leq \dots \leq \theta_ {n} \leq 1
$$

Let the market share of the $i ^ { \mathrm { { t h } } }$ product be $x _ { i } , i = 1 , 2 , . . . , n .$ Because a consumer does not use multiple products, the effective probability that a randomly selected node is not breached—and hence cannot be used as a launching pad for indirect attacks—is given by

$$
\begin{array}{r l} \operatorname * {P r} [ \text { Not   breached } ] & = \\ \sum_ {i = 1} ^ {n} \operatorname * {P r} [ \text { Not   breached } | \text { consumer   uses   product } i ] & \times \\ \operatorname * {P r} [ \text { Consumer   uses   product } i ] & = \sum_ {i = 1} ^ {n} \theta_ {i} x _ {i} \end{array}
$$

which can also be viewed as the effective protection or coverage provided by all of the products taken together. Accordingly, we can now generalize (1) to the case of n products and express the net benefit to user u from purchasing $\theta _ { i }$ as

$$
\theta_ {i} u \left(1 + g \left(1 - \sum_ {j = 1} ^ {n} \theta_ {j} x _ {j}\right)\right) - p _ {i}
$$

where $p _ { i }$ is the price for $\theta _ { i } , i = 1 , 2 , . . . , n .$

As shown in Figure 2, consumers self-select themselves into one of the $( n + 1 )$ classes, with u denoting a consumer who is indifferent between quality levels (i – 1) and $i , i = 2 , 3 , . . . , n .$ and $u _ { 1 }$ denoting a consumer who is indifferent between buying $\theta _ { 1 }$ and not buying at all. Setting $p _ { 0 } = \theta _ { 0 } = 0$ , we can characterize the marginal consumer $u _ { i } , i = 1 , 2 , . . . , n ,$ as follows:

$$
\begin{array}{c} \theta_ {i} u _ {i} \left(1 + g \left(1 - \sum_ {j = 1} ^ {n} \theta_ {j} x _ {j}\right)\right) - p _ {i} = \\ \theta_ {i - 1} u _ {i} \left(1 + g \left(1 - \sum_ {j = 1} ^ {n} \theta_ {j} x _ {j}\right)\right) - p _ {i - 1} \end{array}\tag{2}
$$

Let $u _ { n + 1 } = 1$ . Then, from Figure 2, it is clear that, for i = 1, 2, $\ldots , n , x _ { i } = u _ { i + 1 } - u _ { i } ,$ , which can be simplified to obtain $u _ { i } = 1 -$ $\Sigma _ { j = i } ^ { n } x _ { j } .$ . Substituting this and using mathematical induction, the recursion equations in (2) can be solved to obtain the following result, the proof of which, along with all other proofs, is provided in an online appendix.

Lemma 1. Given a set of market shares $x _ { i } , i = 1 , 2 , . . . , n ,$ the market price for the product with quality $\theta _ { i }$ is given by

$$
p _ {i} = \left(1 + g \left(1 - \sum_ {j = 1} ^ {n} \theta_ {j} x _ {j}\right)\right) \left(\theta_ {i} \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) - \sum_ {j = 1} ^ {i - 1} \theta_ {j} x _ {j}\right)\tag{3}
$$

For notational convenience, we will often write $p _ { i } = G H _ { i } ,$ where

$$
\begin{array}{l} G = 1 + g Y, Y = 1 - \sum_ {j = 1} ^ {n} \theta_ {j} x _ {j}, \text { and } \\ H _ {i} = \theta_ {i} \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) - \sum_ {j = 1} ^ {i - 1} \theta_ {j} x _ {j} \end{array}\tag{4}
$$

## Oligopoly Equilibrium

We consider a market with identical vendors, each vendor choosing a quality level and market share. Given their decisions $\pmb { \theta } = ( \theta _ { 1 } , \theta _ { 2 } , . . . , \theta _ { n } )$ and $\pmb { x } = ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } )$ , the market determines the prices according to Lemma 1. In other words, we apply the concept of fulfilled expectations Cournot equilibrium as in Katz and Shapiro (1985).

Dey et al. (2012) discuss why a Cournot competition fits this context a lot better than Bertrand. Security software subscriptions are primarily sold through a vendor’s network of partners—such as computer manufacturers, other software makers, and online services—with whom the vendor must enter into long-term contracts. It is difficult for the vendor to sell a copy outside of its network, even by substantially reducing the price. Because a simple price reduction will not be sufficient to generate significant additional demand, the vendor must “pre-plan” how many subscriptions it actually intends to sell, making the competition more Cournot-like. In fact, each vendor may even name its own price, but the ensuing Bertrand competition would still lead to a Cournot equilibrium, since contracts with its partners essentially amount to “quantity pre-commitment” (Kreps and Scheinkman 1983). Of course, in the end, whether this market is Cournot or Bertrand is “an empirical question or one that is resolved by looking at the details of the context” (Kreps and Scheinkman 1983, p. 27). It turns out that empirical evidence, too, strongly points to a Cournot market: As shown in Table 1, there are many vendors who offer nearly identical products but still command substantial pricing power. Had the market been a Bertrand oligopoly, the prices would have surely fallen to the marginal cost, which is negligible for software.

Regarding the cost of development, we make the following standard assumption (Bhargava and Choudhary 2001; Jones and Mendelson 2011):

<table><tr><td>Do Not Adopt</td><td>Adopt θ1(Market share x1)</td><td>Adopt θ2(Market share x2)</td><td>...</td><td>Adopt θn(Market share xn)</td></tr><tr><td>0</td><td>u1</td><td>u2</td><td>u3</td><td>un</td></tr></table>

Figure 2. Segmentation of the Consumer Market

Assumption 2. The development cost of a product of quality θ is c(θ), satisfying $c ( 0 ) = 0 , c ^ { \prime } ( \theta ) \geq 0$ bounded for θ 0 [0, 1], and $c ^ { \prime \prime } ( \theta ) > 0$ . The marginal cost of a subscription to a vendor is zero.

Commonly used cost functions, such as the quadratic cost function, $c ( \theta ) = \frac { \kappa } { 2 } \theta ^ { 2 }$ , satisfy this assumption. The optimization problem for the $i ^ { \mathrm { { t h } } }$ vendor can now be written as

$$
\begin{array}{l} \underset {\theta_ {i}, x _ {i}} {\text { Max }} R _ {i} = G H _ {i} x _ {i} - c (\theta_ {i}); \\ \text { s.t. } \theta_ {i - 1} \leq \theta_ {i} \leq \theta_ {i + 1}, 0 \leq \sum_ {i = 1} ^ {n} x _ {i} \leq 1 \end{array}\tag{5}
$$

where $G$ and $H _ { i }$ are as in $( 4 ) , \theta _ { 0 } = 0$ as before, and $\theta _ { n + 1 } = 1$ We consider the equilibrium in which all vendors solve (5) simultaneously. The resulting game is quite complex, and a closed form solution is not possible. Fortunately, however, we can derive a set of useful properties of the oligopoly equilibrium.

Proposition 1. In equilibrium, for all $i , k = 1 , 2 , . . . , n ,$ , the following hold:

(i) $H \theta _ { i } > \theta _ { k }$ then $\theta _ { i } x _ { i } > \theta _ { k } x _ { k }$

$$
\sum_ {j = 1} ^ {n} \theta_ {j} x _ {j} \leq \frac {n}{n + 1}.\tag{ii}
$$

(iii) $H \theta _ { i } = \theta _ { k }$ then $x _ { i } = x _ { k }$

(iv) $H \theta _ { i } = 1$ , then $x _ { i }$ is decreasing in $g .$

(v) $H \theta _ { i } = \theta _ { k }$ then $\theta _ { i } , \theta _ { k } \not \ll 1 .$

Proposition 1 provides us with relevant insights about the market structure. It tells us that, when firms are ordered according to their choice of quality levels, their effective market coverages, $\theta _ { \dot { r } } x _ { i } ,$ also exhibit exactly the same order, although their unadjusted market coverage, $x _ { i } ,$ need not have any specific order. The second part of the proposition states that the total effective market coverage is bounded by $\textstyle { \frac { n } { n + 1 } } ~ ;$ it essentially reflects the inefficiencies in this Cournot market—vendors willingly leave a significant portion of the market unprotected in order to drive up the market price. The third part reveals that, when identical vendors choose the same quality level, they are also compelled to choose the same market coverage in a Cournot equilibrium.

The fourth part of the proposition tells us that, even though $x _ { i }$ is not monotonic in g (see Figure 5 and the accompanying discussion later), it is indeed monotonically decreasing in g once $\theta _ { i }$ becomes one. This happens because, once a vendor reaches a ceiling with respect to the quality level, the only decision variable remaining at its disposal is the market share, and the vendor finds it profitable to sacrifice some market share in order to reduce the total effective market coverage and amplify the effect of a higher g on the market price.

According to the last part of Proposition 1, there is no equilibrium where two vendors choose the same quality level below one. This is interesting since it eliminates a number of possible market configurations. Note that, in equilibrium, each vendor has the option of either matching or staying below the quality level of the vendor above it, resulting in a total of 2<sup>n</sup> possibilities overall. Since identical interior solutions can now be ruled out, the number of market configurations in equilibrium immediately reduces to at most (n + 1): in the first configuration, all vendors offer a quality level of one; in the second, all but one do so; in the $i ^ { \mathrm { t h } } , ( n - i + 1 )$ vendors offer a quality level of one, while the other $( i - 1 )$ vendors offer distinct quality levels below one; finally, in the last configuration, all vendors choose unique quality levels below one. This can be clearly seen in Figure 3, where equilibrium quality levels are depicted as a function of g for a market with 10 vendors and $c ( \theta ) = 0 . 1 5 \theta ^ { 2 }$

Figure 3 also shows that, despite the partial substitutability among the decision variables within and across the vendors strategy spaces, the chosen quality levels are all increasing in $^ { g , }$ even though, analytically, this monotonicity cannot be guaranteed for low values of $\cdot _ { g }$ . A material outcome of this observation is that, as g increases, the range of offered quality levels starts getting narrower, thereby making vertical differentiation less and less pronounced.

![](/api/attachments/CT44SBG4/fulltext/images/6b8ce478ecbee554cf984af4c5597871a734c2620f7e86bf3fba549660c0fa2f.jpg)  
Figure 3. Equilibrium Quality Levels as a Function of Network Effect

As evident from Figure 3, the equilibrium market configuration depends heavily on the magnitude of the network effect. For very high values of g—let us call it Region I—all n vendors choose the highest quality level, that is, $\theta _ { i } = 1$ for all $i = 1 , 2 , . . . , n ;$ this is the first market configuration, and it is fully symmetric. As $g$ decreases beyond the threshold $\gamma _ { 1 0 } ^ { - 1 } ( 0 . 3 ) = 2 5 4 . 7$ in Figure 3, later defined as $\gamma _ { n } ^ { - 1 } { \bigl ( } c ^ { \prime } ( 1 ) { \bigr ) }$ in Theorem 2, we enter Region II where the second market configuration prevails; the symmetry ceases to exist and vertical differentiation takes hold—one of the vendors drops its quality level, $\theta _ { \mathrm { 1 : } }$ , to below one, and the other $( n \mathrm { ~ - ~ } 1 )$ vendors continue to maintain their quality levels at one. As g keeps decreasing, we would continue moving from one asymmetric configuration to another, with more and more vendors starting to offer quality levels below one, although always one vendor at a time. The following result is immediate:

Theorem 1. The network effect in the security software market makes vertical differentiation less attractive to vendors: as g increases, the market becomes progressively less segmented with more vendors targeting the top end of the market.

Viewed from a different angle, the primary benefit from vertical differentiation is that it allows vendors to relax competition, as some can target value-seeking consumers and others, quality seeking ones. The resulting expansion in the market must, however, be capped since the network effect and the associated free-riding behavior make such expansion unattractive. At the same time, the network effect also enables the vendors to tolerate a higher level of competition. Consequently, vertical differentiation becomes less appealing at higher values of g. Having discussed, in Theorem 1, the relationship between the network effect and the vendors’ desire to engage in vertical differentiation, we now characterize the threshold for differentiation.

Theorem 2. For the oligopoly market described above, let $\gamma _ { n } ( g )$ be given by

$$
\gamma_ {n} (g) = \frac {\mu_ {n} (g) + v _ {n} (g)}{2 g ^ {2} n ^ {2} (n + 2) ^ {3}}\tag{6}
$$

where

$$
\mu_ {n} (g) = 2 g ^ {3} n ^ {2} + (n + 1) ^ {2} + g ^ {2} \left(n (n + 1) (n + 6) + 4\right) + g \left(n (3 n + 5) + 4\right)
$$

and

$$
v _ {n} (g) = \left(g ^ {2} n ^ {2} - g (3 n + 2) - (n + 1)\right) \sqrt {4 g (1 + g) + (n + 1) ^ {2}}
$$

Then, an inverse of the function $\gamma _ { n } ( g )$ exists. Furthermore, vertical differentiation would be observed if and only if $g < \gamma _ { n } ^ { - 1 } \bigl ( c ^ { \prime } ( 1 ) \bigr )$ ; otherwise, the equilibrium outcome is fully symmetric.

The result in Theorem 2 can be better visualized in Figure 4, where we set $n = 1 0 , c ( \theta ) = \frac { \kappa } { 2 } \theta ^ { 2 }$ , and partition the ( g, κ) space into two regions by $\kappa = \gamma _ { n } ( g )$ . It is clear from this figure that quality differentiation in an oligopoly depends critically on the network effect. To illustrate, assume that $\kappa = 0 . 2 ;$ we can immediately see from Figure 4 that vertical differentiation would cease being a valid strategy when the strength of the network effect, $g ,$ increases to about 168 or beyond. In other words, when $\kappa = 0 . 2$ , some vertical differentiation would always be observed in a traditional market where $g = 0$ , but not in a security software market unless $g < 1 6 8 .$ Hence, differentiation is less likely in the security software market. Viewed alternatively, although differentiation can be a valid strategy, its feasible region shrinks significantly as $g$ increases. Differentiation would be observed in a traditional market as long as the cost parameter is above the dashed line in Figure 4, whereas it needs to be much higher—higher than $\gamma _ { n } ( g )$ —in a market with a negative network effect.

![](/api/attachments/CT44SBG4/fulltext/images/0594905990f9a13053e09a9309662d5d4f10630ce171681555c2347b125271d0.jpg)  
Figure 4. Product Differentiation Strategy as a Function of κ and g

We now turn our attention to the region below the dashed line in Figure 4. This line represents $\gamma _ { n } ( 0 )$ , the cost threshold for differentiation in a traditional market. Whenever $c ^ { \prime } ( 1 )$ , or κ in Figure $^ { 4 , }$ is below this threshold, differentiation would completely disappear from the market, irrespective of the value of $g - \mathrm { a }$ result consistent with prior literature that the issue of differentiation becomes relevant only when quality is costly (e.g., Jones and Mendelson 2011; Moorthy 1988; Motta 1993). At a glance, the existence of this cost threshold may suggest that, perhaps, there is an alternative explanation for the lack of differentiation in the security software market. It is entirely conceivable that vendors do not differentiate simply because of a low marginal cost of development, and not necessarily because of the network effect. However, a closer examination of this threshold actually makes the argument in favor of the network effect much stronger. To see this, consider a market without this network effect, that is, $g = 0$ . In such a market, whenever the marginal cost is above $\gamma _ { n } ( 0 )$ , vertical differentiation would indeed be observed. Interestingly, though, $\gamma _ { n } ( 0 )$ rapidly approaches zero in a fiercely competitive market.

Proposition 2. In a market without network effects and a large number of vendors, vertical differentiation is optimal. Specifically, the threshold of differentiation is a rapidly decreasing function of the number of vendors: $\begin{array} { r } { \gamma _ { n } ( 0 ) = \frac { 1 } { { ( n + 1 ) } ^ { 2 } } } \end{array}$

Proposition 2 tells us that, absent the network effect, the conspicuous lack of vertical differentiation in a market with hundreds of security software products cannot be reasonably explained.

In order to see how a manufacturer’s other decision (market share) changes with g, we plot the individual market shares and the total market coverage in Figure 5, again for $n = 1 0$ and $c ( \theta ) = 0 . 1 5 \theta ^ { 2 }$ . As can be clearly seen from this figure, the individual market shares are not monotonic in g. They tend to increase for the lower quality vendors and decrease for the higher quality ones. This can be explained as follows. A vendor’s motivation to drop its market share arises out of its desire to increase G. However, not all vendors have the same incentive to increase $G ;$ increasing G helps the vendors at the top end significantly more, because the price for vendor i is $G H _ { i }$ and $H _ { i }$ is increasing in i. At the same time, when these vendors start dropping coverage, it creates an opportunity for others to somewhat expand theirs. In the extreme case of a very high g, when all vendors are concentrated at the top end, they all reduce coverage with g. The implication is clear. A vendor in the security software market should be mindful of its relative position in the quality spectrum when deciding on its market share.

![](/api/attachments/CT44SBG4/fulltext/images/17119aebc07fc823645dc26afb0a4a27c5af0d80805dcccf7e17ae4624b2dc49.jpg)  
(a) Individual Market Share

![](/api/attachments/CT44SBG4/fulltext/images/9fcae890d9d583991e6e1f841241f4ce681af1c6889f3c9d7dae4c92507ea745.jpg)  
(b) Total Market Coverage  
Figure 5. Equilibrium Market Coverage as a Function of Network Effect

Even though individual market shares are not monotonic in g, the total market coverage, $\textstyle \sum _ { j = 1 } ^ { n } x _ { j } .$ , is apparently decreasing (see Figure 5b). This is consistent with our earlier observation that this market is characterized by a low coverage. On the other hand, the effective market coverage, $\begin{array} { r } { \sum _ { j = 1 } ^ { n } \theta _ { j } x _ { j } , , } \end{array}$ is not monotonic; it first increases with g, and then starts decreasing slowly, but, as mentioned in Proposition 1, always remains below the traditional Cournot coverage of $\frac { n } { n + 1 }$ . The intuition is straightforward. When the network effect is low, some vendors target value-seeking consumers with low quality alternatives, substantially increasing the total market coverage. At the same time, though, the lower quality of these products ensures that the effective market coverage still remains low and the free-riding behavior due to the network effect, well under control. As g increases, however, vendors increase their quality levels, which make the free-riding behavior more prominent. To counter, more and more vendors start decreasing their market shares. This, in turn, stalls the rapid increase of the effective market coverage.

## Versioning

We have just shown that the network effect in the security software market reduces the likelihood of differentiation.

However, a couple of questions still remain. One, this result was obtained under an assumption that individual vendors do not version their products. Although prior literature has argued that, absent a marginal cost, versioning is a not an optimal strategy (Bhargava and Choudhary 2001; Jones and Mendelson 2011, Wei and Nault 2008), it is not clear whether it would continue to be so in our setting that is substantially different from those in the prior literature. We use a singlestage Cournot oligopoly with a network effect, whereas Bhargava and Choudhary consider a monopoly, and Jones and Mendelson as well as Wei and Nault consider a two-stage Bertrand competition without network effects. Second, and on a related note, vertical differentiation can still occur as a result of one or more vendors offering multiple versions. Therefore, to explain the lack of differentiation observed in practice, we need to analyze whether versioning could be an effective strategy here.

In fact, for traditional off-the-shelf software products, it is not uncommon for a vendor to offer versions of inferior quality simultaneously with a superior quality product. Usually, the purpose for such an approach is to expand the market so as to increase the positive network effect for users (Jing 2000), although the inferior product might partly cannibalize the superior quality product. However, by now, we have established that the security software market is quite different from the traditional software market. This provides a second motivation behind evaluating whether versioning is still a desirable strategy in the security software market.

In order to examine this issue, we make the following standard assumption of costless versioning (Bhargava and Choudhary 2008; Jones and Mendelson 2011):

Assumption 3. When offering multiple versions, a vendor incurs the development cost only for the highest quality version, and no additional cost for the inferior ones.

Let us now consider the following scenario. There are n different quality levels in the market, out of which $( m + 2 )$ distinct quality levels, $\theta _ { i } , \theta _ { k }$ , and $\theta _ { l _ { t } } , t = 1 , 2 , . . . , m$ , are offered by a single vendor; the possibility that $m = 0$ is not excluded. The remaining $( n - m - 2 )$ are offered by the other vendors, with some possibly engaging in versioning as well; the possibility that this is a monopoly $( \mathrm { i . e . , } n - m - 2 = 0 )$ is also not excluded from this analysis. Without loss of generality, we assume the following ordering:

$$
i > k > l _ {1} > l _ {2} > \dots > l _ {m}, \text { or } \theta_ {i} > \theta_ {k} > \theta_ {l _ {1}} > \theta_ {l _ {2}} > \dots \theta_ {l _ {m}}
$$

Let $R _ { \nu }$ be the revenue (net of the development cost) to this vendor offering $( m ~ + ~ 2 )$ distinct quality levels. Under Assumption $3 , R _ { \nu }$ can be written as

$$
R _ {v} = G H _ {i} x _ {i} + G H _ {k} x _ {k} + G \sum_ {t = 1} ^ {m} H _ {l _ {t}} x _ {l _ {t}} - c (\theta_ {i})
$$

In equilibrium, $R _ { \nu }$ must satisfy the following two first order conditions, among others:

$$
\frac {\partial R _ {v}}{\partial x _ {i}} = \frac {\partial R _ {v}}{\partial x _ {k}} = 0
$$

and must, therefore, also satisfy

$$
\frac {1}{\theta_ {i}} \frac {\partial R _ {v}}{\partial x _ {i}} - \frac {1}{\theta_ {k}} \frac {\partial R _ {v}}{\partial x _ {k}} = 0\tag{7}
$$

Note that

$$
\frac {\partial R _ {v}}{\partial x _ {i}} = G H _ {i} - G \theta_ {i} x _ {i} - g \theta_ {i} x _ {i} H _ {i} - G \theta_ {k} x _ {k} -
$$

$$
g \theta_ {i} x _ {k} H _ {k} - \sum_ {t = 1} ^ {m} x _ {l _ {t}} \left(G \theta_ {l _ {t}} + g \theta_ {i} H _ {l _ {t}}\right)
$$

and

$$
\begin{array}{r l} \frac {\partial R _ {v}}{\partial x _ {k}} & = G H _ {k} - G \theta_ {k} x _ {i} - g \theta_ {k} x _ {i} H _ {i} - G \theta_ {k} x _ {k} - \\ & \quad g \theta_ {k} x _ {k} H _ {k} - \sum_ {t = 1} ^ {m} x _ {l _ {t}} \left(G \theta_ {l _ {t}} + g \theta_ {k} H _ {l _ {t}}\right) \end{array}
$$

Combining the above, we can show

$$
\begin{array}{r l} \frac {1}{\theta_ {i}} \frac {\partial R _ {v}}{\partial x _ {i}} - \frac {1}{\theta_ {k}} \frac {\partial R _ {v}}{\partial x _ {k}} = & \\ \frac {G}{\theta_ {i} \theta_ {k}} \left[ \theta_ {k} \sum_ {j = k} ^ {i - 1} \left(\theta_ {i} - \theta_ {j}\right) x _ {j} + \left(\theta_ {i} - \theta_ {k}\right) \left(\sum_ {j = 1} ^ {k} \theta_ {j} x _ {j} + \sum_ {t = 1} ^ {m} \theta_ {l _ {i}} x _ {l _ {t}}\right) \right] \end{array}\tag{8}
$$

It is clear that the right hand side of (8) is positive, which is a violation of the condition in (7). Since this holds for all values of m and $n ,$ the following result ensues:

Theorem 3. In the market described above, regardless of competitors’ actions, versioning is not optimal for any vendor.

Theorem 3 shows that, even when versioning is an option, no vendor would actually use it. The result has an important implication, which is that all of our earlier analyses remain valid even in settings where the versioning decision is endogenous. Besides, as mentioned previously, this result is also consistent with practice; the common forms of discrimination in the security software market include bundling and discounts for longer subscriptions, but not second-degree discrimination with respect to quality. Together with earlier results, it also explains why some counterintuitive real-world observations—most notably, a lack of segmentation despite severe competition—are consistent with the presence of a negative network effect.

## Free Software

As a final check for the robustness of our analysis, we consider a situation where there are open-source or free software packages available to consumers. Indeed, there are a few free security software packages in the market from vendors such as Avast, AVG, Avira, and Microsoft. Despite the presence of these free products, the paid ones surprisingly continue to command significantly high prices. The main reason is that the free versions are deemed as poor substitutes for the paid ones, as the free versions lack a “wider range of detection features” that are necessary today (Dunn 2011). A case in point is the free antivirus software offered by AVG. Although it is considered the best among the free ones today (Mediati 2012), it lacks some basic features. For example, it does not check e-mail messages for spam and malware, nor does it prevent wireless intrusion. In fact, most experts agree that free security software products are typically “bare bones” and often a tool for market penetration (Bakke 2011; Mediati 2010).

In order to model this in a formal manner, we assume that a consumer can choose between paying for premium security software and obtaining bare-bones free software of quality $\phi$ $> 0 .$ It turns out that the characterization of the marginal consumer $u _ { i } , i = 1 , 2 , . . . , n .$ as given in (2), still holds with slight modification:

$$
\begin{array}{r l} \theta_ {i} u _ {i} & \left(1 + g \left(1 - \sum_ {j = 0} ^ {n} \theta_ {j} x _ {j}\right)\right) - p _ {i} = \\ & \theta_ {i - 1} u _ {i} \left(1 + g \left(1 - \sum_ {j = 0} ^ {n} \theta_ {j} x _ {j}\right)\right) - p _ {i - 1} \end{array}\tag{9}
$$

where $p _ { 0 } = 0$ as before, but $\theta _ { 0 } = \phi$ now denotes the quality level of free software. In addition, since $\begin{array} { r } { x _ { 0 } = 1 - \Sigma _ { j = 1 } ^ { n } x _ { j } } \end{array}$ represents the market covered by free software, we get from (9):

Lemma 2. The market price for the product with quality $\theta _ { i }$ , $i = 1 , 2 , \dots n ,$ is given by

$$
\begin{array}{l} p _ {i} = (1 - \phi) \left(1 + g ^ {\prime} \left(1 - \sum_ {j = 1} ^ {n} \theta_ {j} ^ {\prime} x _ {j}\right)\right) \times \\ \left(\theta_ {i} ^ {\prime} \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) - \sum_ {j = 1} ^ {i - 1} \theta_ {j} ^ {\prime} x _ {j}\right) \end{array}\tag{10}
$$

where $g ^ { \prime } = g \left( 1 - \phi \right)$ and $\theta _ { j } ^ { \prime } = \frac { \theta _ { j } - \phi } { 1 - \phi }$

Similar to (4), we can define

$$
G ^ {\prime} = (1 - \phi) (1 + g ^ {\prime} Y ^ {\prime}), Y ^ {\prime} = 1 - \sum_ {j = 1} ^ {n} \theta_ {j} ^ {\prime} x _ {j}
$$

and

$$
H _ {i} ^ {\prime} = \theta_ {i} ^ {\prime} \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) - \sum_ {j = 1} ^ {i - 1} \theta_ {j} ^ {\prime} x _ {j}
$$

and write $p _ { i } { = } G ^ { \prime } H _ { i } ^ { \prime }$ . Comparing (10) with (3), it is easy to see that the new problem is structurally the same as the old one. An immediate implication is that Theorem 3 continues to apply, that is, versioning is still not optimal. Therefore, the $i ^ { \mathrm { { t h } } }$ vendor, $i = 1 , 2 , . . . , n .$ , must solve the following optimization problem to decide on its market strategy:

$$
\begin{array}{l} \underset {\theta_ {i} ^ {\prime}, x _ {i}} {M a x} R _ {i} = G ^ {\prime} H _ {i} ^ {\prime} x _ {i} - c \big (\phi + \theta_ {i} ^ {\prime} (1 - \phi) \big); \\ \text {s.t.} \quad \theta_ {i - 1} ^ {\prime} \leq \theta_ {i} ^ {\prime} \leq \theta_ {i + 1} ^ {\prime}, 0 \leq \sum_ {i = 1} ^ {n} x _ {i} \leq 1 \end{array}
$$

If this optimal profit is not positive, the $i ^ { \mathrm { { t h } } }$ vendor would decide not to produce the software at all, that is, $\theta _ { i } = 0 ;$ otherwise, the vendor would produce a quality level $\theta _ { i } > \phi$

A closer examination of (10) reveals that the presence of free software effectively reduces the magnitude of the network effect from g to $g ^ { \prime } = g ( 1 - \phi )$ . Therefore, as g increases, the market still behaves the same way as before, moving from one configuration to another. However, the thresholds (at which the configuration changes) occur at higher values of g. Predictably, the threshold beyond which the market becomes completely symmetric is also shifted by a factor of $\frac { 1 } { 1 - \phi }$

Theorem 4. Even in the presence of free software of quality $\phi < 1$ , the network effect in the security software market makes vertical differentiation less appealing. In particular, some vertical differentiation would be observed as long as $g < \frac { \gamma _ { n } ^ { - 1 } \bigl ( c ^ { \prime } ( 1 ) \bigr ) } { 1 - \phi }$ , where $\gamma _ { n } ( \cdot )$ is as defined by (6); otherwise, the equilibrium outcome is fully symmetric.

It is easy to see that Theorems 1 and 2 become special cases of Theorem 4 when $\phi = 0$ . Figure 6 illustrates Theorem 4 for a market with five potential players, $c ( \theta ) = 0 . 1 5 \theta ^ { 2 }$ , and $\phi = 0 . 2 5$ . As indicated in this figure, the threshold for differentiation is $\frac { \gamma _ { 5 } ^ { - 1 } ( 0 . 3 ) } { 1 - 0 . 2 5 } = 6 4 . 2$ —compared to $\gamma _ { 5 } ^ { - 1 } ( 0 . 3 ) = 4 8 . 2$ for the case where a free product is not available $( \phi = 0 ) -$ implying that the region of differentiation expands in the presence of a free product.

The finding above with regard to the impact of free software actually completes our picture of the market in an interesting manner and strengthens our earlier findings regarding the role of the network effect. As evident from our discussions thus far, there are four factors that impact competition and the extent of differentiation: the cost of quality, the network effect, the number of vendors, and the presence of free software. The higher the cost of quality or the number of vendors, the larger is the intensity of competition and the need for differentiation. The presence of free alternatives has exactly the same effect; it also means increased competitive pressure and an even greater need for differentiation. The only counterweight to all of these three factors favoring differentiation is the network effect, whose presence incentivizes the vendors to control consumers’ free-riding behavior by collocating at the top end of the market while, at the same time, dropping coverage. Thus, without considering a negative network effect and its discernible impact, it is difficult to explain why so many vendors so often choose not to differentiate in quality in an overcrowded marketplace replete with hundreds of competing products including several free ones.

## Some Technical Remarks

So far, we have assumed a development cost function, $c ( \theta ) ,$ with a bounded derivative (see Assumption 2), as well as an upper bound of one on the quality levels. This is a reasonable assumption in our context as these modeling choices closely reflect the realities of the security software market. First, an upper bound of one makes natural sense here since the quality is indexed with the effectiveness of the security software in thwarting attacks. Second, it is not uncommon to have an upper bound for quality because of technological or other related restrictions (e.g., Shaked and Sutton 1982). If such an upper bound is not one, it can be easily normalized to one without any loss of generality.

![](/api/attachments/CT44SBG4/fulltext/images/698bb117acf0ac5de9281bdaa5f0065e9971702a0630c895672f56427318f9e5.jpg)  
Figure 6. Equilibrium Quality Levels in the Presence of Free Software

Let us now consider the situation where the perfect quality is not attainable. Indeed, it is often difficult to anticipate all possible forms of security threats when developing a security software product; as a result, few products are failsafe and 100 percent effective in practice (Elias 2012). It turns out that such a case can be easily modeled with a cost function such as

$$
c (\theta) = \left\{ \begin{array}{l l} \frac {\kappa}{2} \theta^ {2} & \text { if } \theta \leq \theta_ {\max} \\ + \infty & \text { otherwise } \end{array} \right.
$$

where $\theta _ { m a x } < 1$ is the highest quality level attainable in practice. In that case, one can set the upper bound in our model, $\theta _ { n + 1 } , \mathrm { t o } \ \theta _ { m a x }$ instead of one, and all our results easily extend. In particular, when $g$ increases, the segmentation in the market reduces, with more and more vendors choosing the quality level of $\theta _ { m a x }$

Nonetheless, in order to ascertain the robustness of our results, we also consider a cost function whose derivative is not bounded at $\theta = 1$ . Examples include functions such as $c ( \theta ) = \kappa { \left( \frac { \theta } { 1 - \theta } \right) } ^ { \prime }$ , where $\kappa > 0$ and $r \geq 1 . ^ { 6 }$ Clearly, for such a function, a corner solution of the form $\theta _ { i } = 1$ is no longer possible. ${ \mathrm { Y e t } } ,$ all results, except Theorem 2, hold as stated. Interestingly, in spirit, Theorem 2 still remains relevant in the following sense:

Given an arbitrarily small $\epsilon > 0 ,$ it is always possible to find a threshold such that, when g is above this threshold, all quality levels are within an -neighborhood of one.

In essence, all vendors choose quality levels that become closer and closer as g increases. We illustrate this in Figure 7 for $n = 5 , c ( \theta ) = { \frac { \kappa \theta } { 1 - \theta } } , { \mathrm { a n d ~ } } \kappa = 0 . 0 1$

## Conclusion

The motivation for this work is largely rooted in the unique structure of the market for off-the-shelf security software. One of the interesting characteristics of this market is that there are a large number of vendors who sell nearly identical products. It is, in fact, very hard to find another market with anything remotely similar. We have examined offerings from several major players in this market and found little evidence of product differentiation. Furthermore, we have found that vendors in this market rarely use other segmentation strategies, such as providing multiple versions of their products. All of these are extremely unusual for any fiercely competitive market with a large number of competitors.

Although prior research has identified a negative network effect as the reason for some of the unique characteristics of this market, such as its low coverage and high price, the literature has largely ignored issues pertaining to quality competition, market segmentation, and versioning. In this work, we propose a comprehensive model to address all of these issues. We fully endogenize vendors’ quality and versioning decisions and also consider the presence of free alternatives in order to better understand what strategies might be useful for vendors in this highly competitive market.

![](/api/attachments/CT44SBG4/fulltext/images/5c8c817b97bc96628338d6b4566b0f505236ca53687c2279b4f5c758b8b9e483.jpg)  
Figure 7. Equilibrium Quality Levels for Unbounded cN(1)

We consider an oligopoly market in which vendors make their quality and market share decisions simultaneously. We also incorporate a network effect that arises from a consumer’s desire to free-ride when others around him deploy security solutions and thereby reduce his chances of getting an indirect infection. We find that, for a market with n vendors, there are at most (n + 1) possible equilibrium configurations (see Figure 3). At higher levels of the network effect (that is, at a high g), the equilibrium market configuration is the one in which there is no differentiation. In this symmetric configuration, all vendors locate themselves at the very top of the market, in line with practical observations made earlier. However, as Theorem 2 shows, when the network effect falls below a threshold, differentiation can take hold. Theorem 1 further establishes that, as g continues to decrease, the asymmetry in the market can become even more pronounced, with more and more vendors starting to spread across the quality spectrum. In summary, we find evidence that the lack of differentiation in this market is consistent with the presence of a strong negative network effect.

It is somewhat surprising that differentiation is an unlikely choice in this competitive market, because the primary effect of quality differentiation is that of easing competition (Moorthy 1988; Shaked and Sutton 1982). Jones and Mendelson (2011) have even shown that markets for information goods are likely to be more asymmetric than other markets, with vendors preferring a larger level of differentiation. In our case, however, when different firms target different segments, the market coverage expands, which, in turn, can significantly increase consumers’ free-riding tendency in the presence of the network effect. Therefore, when the network effect is strong, it becomes optimal for vendors to completely avoid quality differentiation and also shrink the overall market coverage. This intuition is further corroborated by Figure 5, which shows that, as g increases, more and more vendors start dropping their market shares. Also, as shown in the figure, the total market coverage steadily declines as g increases, again coinciding with real-life observations regarding the lack of coverage in this market. This insight with respect to quality competition is indeed valuable as it reveals how vendors can respond to the prevailing network effect by suitably positioning their products in the marketplace, as well as by adjusting their market shares.

We also examine whether segmentation in this market could occur as a result of some vendors resorting to versioning their products. Versioning of information goods is often costless as a lower version can easily be created by deactivating certain features from a higher version. Yet, prior research has shown that, when all versions have the same zero marginal cost, versioning is often suboptimal. We find that this insight extends even to our rather complex oligopoly setting in which each vendor chooses an arbitrary number of quality levels as well as their market shares in the presence of the network effect. The net implication is clear. Strategies that seek to segment the consumer market are often not as useful for security software vendors as they are for manufacturers of other products.

Finally, we examine how this market would behave in the presence of free software. We find that the basic insights regarding the impact of the network effect on quality differentiation remain applicable in this wider setting. The presence of free software itself makes differentiation more appealing to vendors and expands the region of differentiation. Therefore, when this effect is accounted for, the absence of differentiation becomes even harder to explain without acknowledging the role of the network effect. This analysis, in other words, lends additional support to our central argument about quality differentiation.

Overall, our results shed new light on the unique structure of the security software market and generate practical insights for vendors, security experts, and consumers, as well as provide a useful starting point for policy debates. At the same time, interestingly, the lack of differentiation observed in this market and the underlying theoretical explanation provided in this work together imply that the results from prior research (Dey et al. 2012), which were obtained without considering the quality dimension, are also robust in a real-world setting.

There are several directions in which our results can be extended. First, in traditional off-the-shelf application software markets, nonlinear pricing through volume licensing is quite common. One could investigate whether nonlinear pricing is useful in the context of security software as well and whether that will impact the result concerning vertical differentiation. Besides, vendors from traditional software markets are entering the security software market, and Internet service providers are also offering security software to their subscribers, leading to new forms of market competition. These new competition patterns could be another interesting area of study. We are examining some of these issues in our ongoing efforts to better understand both persisting and emerging trends.

## Acknowledgments

A preliminary version of this work was presented at the $4 6 ^ { \mathrm { t h } }$ Hawaii International Conference on System Sciences (HICSS-2013); we gratefully acknowledge the valuable feedback received from the participants of the conference. We would also like to thank the referees and editors of this journal for their constructive comments.

## References

August, T., and Tunca, T. I. 2006. “Network Software Security and User Incentives,” Management Science (52:11), pp. 1703-1720.

August, T., and Tunca, T. I. 2008. “Let the Pirates Patch? An Economic Analysis of Network Software Security Patch Restrictions,” Information Systems Research (19:1), pp. 48-70.

Bakke, D. 2011. “6 Reasons Why You Should Pay for Antivirus Software,” Vipre Security News (http://vipresecuritynews.com/ 2011/09/21/6-reasons-why-you-should-pay-for-antivirussoftware/).

Bhargava, H. K., and Choudhary, V. 2001. “Information Goods and Vertical Differentiation,” Journal of Management Information Systems (18:20, pp. 89-106.

Bhargava, H. K., Choudhary, V. 2008. “Research Note: When Is Versioning Optimal for Information Goods?,” Management Science (54:5), pp. 1029-1035.

CISCO. 2011. “Email Attacks: This Time it’s Personal,” Security White Paper (http://www.cisco.com/en/US/prod/collateral/ vpndevc ps10128/ps10339/ps10354/targeted attacks.pdf).

Dey, D., Lahiri, A., and Zhang, G. 2012. “Hacker Behavior, Network Effects, and the Security Software Market,” Journal of Management Information Systems (29:2), pp. 77-108.

Dey, D., Lahiri, A., and Zhang, G. 2013. “Quality Competition in the Security Software Market,” in Proceedings of the 46<sup>th</sup> Hawaii International Conference on System Sciences, Los Alamitos, CA: IEEE Computer Society Press, pp. 3992-4001.

Dunn, J. E. 2011. “Microsoft Security Essentials Struggle in New Antivirus Tests,” PC World, May 4 (http://www.pcworld. com/article/227187/microsoft\_security\_essentials\_struggles\_in \_new\_antivirustests.html).

Egan, M. 2012. “12 Features to Look for When Buying Security Software,” PC Advisor (http://www.pcadvisor.co.uk/buyingadvice/security/3349388/12-features-look-for-when-buyingsecurity-software).

Eichorn, K., and Smith, J. 2011. “McAfee Releases Online Banking Safety Guide for the 47 Percent of Consumers Who Are Under Protected,” McAfee Press Release (http://www. mcafee.com/us/about/news/2011/q3/20110803-01.aspx).

Elias, J.-C. 2012. “No Perfect Internet Security Software,” Kaspersky Lab Press Center (http://usa.kaspersky.com/about-us/presscenter/in-the-news/no-perfect-internet-security-software).

Galbreth, M. R., and Shor, M. 2010. “The Impact of Malicious Agents on the Enterprise Software Industry,” MIS Quarterly (34:3), pp. 595-612.

Gartner Group. 2006. “Gartner Says Security Software Revenue Totaled \$7.4 Billion in 2005,” Press Release (http://www. gartner.com/it/page.jsp?id=496491).

Gartner Group. 2012. “Gartner Says Security Software Market Grew 7.5 Percent in 2011,” Press Release (http://www.gartner. com/it/page.jsp?id=1996415).

Gordon, L. A., and Loeb, M. P. 2002. “The Economics of Information Security Investment,” ACM Transactions on Information and System Security (5:4), pp. 438-457.

Jing, B. 2000. “Versioning Information Goods with Network Externalities.,” in Proceedings of the 21<sup>st</sup> International Conference on Information Systems, Brisbane, Australia, December 10-13, pp. 1-12.

Jones, R., and Mendelson, H. 2011. “Information Goods vs. Industrial Goods: Cost Structure and Competition,” Management Science (57:1), pp. 164-176.

Katz, M. L., and Shapiro, C. 1985. “Network Externalities, Competition and Compatibility,” American Economic Review (75:3), pp. 424-440.

Kreps, D. M., and Scheinkman, J. A. 1983. “Quantity Precommitment and Bertrand Competition Yield Cournot Outcomes,” The Bell Journal of Economics (14:2), pp. 326-337.

Lahiri, A. 2012. “Revisiting the Incentive to Tolerate Illegal Distribution of Software Products,” Decision Support Systems (53:2), pp. 357-367.

Langa, F. 2010. “Run Multiple Antivirus Applications on One PC,” Windows Secrets (http://windowssecrets.com/langalistplus/run-multiple-antivirus-applications-on-one-pc/).

Mediati, N. 2010. “Free vs. Fee: Free and Paid Antivirus Programs Compared,” PC World (http://www.pcworld.com/article/ 210589/free\_vs\_fee\_free\_and\_paid\_antivirus\_programs\_ compared.html).

Mediati, N. 2012. “Free Antivirus You Can Trust,” PC World (http://www.pcworld.com/article/254121/free\_antivirus\_you\_ can\_trust.html).

Moorthy, K. S. 1988. “Product and Price Competition in a Duopoly,” Marketing Science (7:2), pp. 141-168.

Motta, M. 1993. “Price vs. Quantity Competition,” The Journal of Industrial Economics (41:2), pp. 113-131.

Mussa, M., and Rosen, S. 1978. “Monopoly and Product Quality,” Journal of Economic Theory (18), pp. 301-317.

OPSWAT. 2012. “Security Industry Market Share Analysis,” Market Share Report, March (http://www.opswat.com/ sites/default/files/OPSWAT-market-share-report-march-2012.pdf).

Png, I. P. L., and Wang, Q.-H. 2009. “Information Security: Facilitating User Precautions vis-à-vis Enforcement Against Attackers,” Journal of Management Information Systems (26:2), pp. 97-121.

Ransbotham, S., and Mitra, S. 2009. “Choice and Chance: A Conceptual Model of Paths to Information Security Compromise,” Information Systems Research (20:1), pp. 121-139.

Shaked, A., and Sutton, J. 1982. “Relaxing Price Competition through Product Differentiation,” The Review of Economic Studies (49:1), pp. 3-13.

Shapiro, C., and Varian, H. R. 1999. Information Rules: A Strategic Guide to the Network Economy, Boston: Harvard Business School Press.

Top Ten Reviews. 2012. “Internet Security Suites Software Review,” TopTenReviews.Com (http://internet-security-suitereview.toptenreviews.com/; accessed November 7, 2012).

Wei, X., and Nault, B. R. 2008. “Vertically Differentiated Information Goods: Monopoly Power Through Versioning,” unpublished paper, Haskayne School of Business, University of Calgary ( http://ssrn.com/abstract=1677561).

## About the Authors

Debabrata Dey is currently the Marion B. Ingersoll Professor of Information Systems at the Foster School of Business, University of Washington. He received his Ph.D. from the Simon School of Business, University of Rochester. His papers have appeared in Management Science, Operations Research, Information Systems Research, ACM Transactions on Database Systems, IEEE on Knowledge and Data Engineering, Journal of Management Information Systems, and INFORMS Journal on Computing, among other journals. He has also served as a senior editor for Information Systems Research and as an associate editor for Management Science, Information Systems Research, and MIS Quarterly.

Atanu Lahiri is an assistant professor at the Foster School of Business, University of Washington. He received his Ph.D. from the Simon School of Business, University of Rochester. His research interests include pricing of information goods and application of information technology in healthcare. His papers have appeared in Management Science, Information Systems Research, Journal of Management Information Systems, Decision Support Systems, and Manufacturing & Service Operations Management.

Guoying Zhang is an associate professor at the Dillard College of Business Administration, Midwestern State University. She received her Ph.D. from the Foster School of Business, University of Washington. Her research and teaching interests include information security and economics of information systems. Her work has appeared in Journal of Management Information Systems and Decision Support Systems.

# QUALITY COMPETITION AND MARKET SEGMENTATION IN THE SECURITY SOFTWARE MARKET

Debabrata Dey and Atanu Lahiri

Michael G. Foster School of Business, University of Washington, Seattle, Seattle, WA 98195 U.S.A. {ddey@uw.edu} {lahiria@uw.edu}

Guoying Zhang Dillard College of Business, Midwestern State University, Wichita Falls, Wichita Falls, TX 76308 U.S.A. {grace.zhang@mwsu.edu}

## Appendix A

## Proofs

## Proof of Lemma 1

Setting $u _ { n + 1 } = 1$ , from Figure 2, we can find the market coverage of $\theta _ { j } , j = 1 , 2 , . . . , n , \mathrm { a s } x _ { j } = u _ { j + 1 } - u _ { j }$ , which can be summed over j to obtain $\begin{array} { r } { u _ { i } = 1 - \Sigma _ { j = i } ^ { n } x _ { j } . } \end{array}$ . Substituting this into (2) for i = 1 and noting that $p _ { 0 } = \theta _ { 0 } = 0$ , we find

$$
p _ {1} = G \theta_ {1} u _ {1} = G \theta_ {1} \left(1 - \sum_ {j = 1} ^ {n} x _ {j}\right)\tag{A1}
$$

We will now prove the lemma by induction. It is clear that (3) reduces to (A1) for i = 1. Let (3) hold for $i = k ,$ implying

$$
p _ {k} = G \Bigg (\theta_ {k} \Bigg (1 - \sum_ {j = k} ^ {n} x _ {j} \Bigg) - \sum_ {j = 1} ^ {k - 1} \theta_ {j} x _ {j} \Bigg)
$$

We substitute this into (2) for $i = k + 1$ to obtain

$$
\begin{array}{l} p _ {k + 1} = G \left(\theta_ {k + 1} - \theta_ {k}\right) u _ {k + 1} + p _ {k} \\ = G \left(\theta_ {k + 1} - \theta_ {k}\right) \left(1 - \sum_ {j = k + 1} ^ {n} x _ {j}\right) + G \left(\theta_ {k} \left(1 - \sum_ {j = k} ^ {n} x _ {j}\right) - \sum_ {j = 1} ^ {k - 1} \theta_ {j} x _ {j}\right) \\ = G \left(\theta_ {k + 1} - \theta_ {k}\right) \left(1 - \sum_ {j = k + 1} ^ {n} x _ {j}\right) + G \left(\theta_ {k} \left(1 - \sum_ {j = k + 1} ^ {n} x _ {j}\right) - \theta_ {k} x _ {k} - \sum_ {j = 1} ^ {k} \theta_ {j} x _ {j} + \theta_ {k} x _ {k}\right) \\ = G \left(\theta_ {k + 1} \left(1 - \sum_ {j = k + 1} ^ {n} x _ {j}\right) - \sum_ {j = 1} ^ {k} \theta_ {j} x _ {j}\right) \end{array}
$$

In other words, if (3) holds for i = k, then it also holds for $i = k + 1$ . Since (3) holds for i = 1, the proof is now complete. #

## Proof of Proposition 1

(i) Since $R _ { i } = x _ { i } G H _ { i } - c ( \theta _ { i } )$ and $x _ { i } < 1$ , we can use the first order condition with respect to $x _ { i }$ to obtain

$$
\frac {\partial R _ {i}}{\partial x _ {i}} = G H _ {i} - G \theta_ {i} x _ {i} - g H _ {i} \theta_ {i} x _ {i} = 0 \Leftrightarrow \theta_ {i} x _ {i} = \frac {G H _ {i}}{G + g H _ {i}}
$$

Therefore, we get

$$
\theta_ {i} x _ {i} - \theta_ {k} x _ {k} = \frac {G H _ {i}}{G + g H _ {i}} - \frac {G H _ {k}}{G + g H _ {k}} = \frac {G ^ {2} \left(H _ {i} - H _ {k}\right)}{(G + g H _ {i}) (G + g H _ {k})}
$$

Now, from definition of $H _ { l } , l = 1 , 2 , . . . , n .$ we get

$$
\begin{array}{r l} H _ {l} - H _ {l - 1} & = \left(\theta_ {l} \left(1 - \sum_ {j = l} ^ {n} x _ {j}\right) - \sum_ {j = 1} ^ {l - 1} \theta_ {j} x _ {j}\right) - \left(\theta_ {l - 1} \left(1 - \sum_ {j = l - 1} ^ {n} x _ {j}\right) - \sum_ {j = 1} ^ {l - 2} \theta_ {j} x _ {j}\right) \\ & = \left(\theta_ {l} - \theta_ {l - 1}\right) \left(1 - \sum_ {j = l} ^ {n} x _ {j}\right) \end{array}
$$

Since $\theta _ { i } > \theta _ { k }$ implies that $i > k ,$ summing the above over $l ,$ we get

$$
H _ {i} - H _ {k} = \sum_ {l = k + 1} ^ {i} \left(H _ {l} - H _ {l - 1}\right) = \sum_ {l = k + 1} ^ {i} \left(\theta_ {l} - \theta_ {l - 1}\right) \left(1 - \sum_ {j = l} ^ {n} x _ {j}\right)\tag{A2}
$$

Now, since $\theta _ { i } > \theta _ { k }$ , there must exist some $l , k < l \leq i ,$ such that $\theta _ { l } - \theta _ { l - 1 } > 0$ , implying that the right hand side of (A2) is strictly greater than zero. Thus, $H _ { i } - H _ { k } > 0$ and, hence, $\theta _ { i } x _ { i } - \theta _ { k } x _ { k } > 0$ , which completes the proof.

(ii) First, we note that, for all $i = 1 , 2 , . . . , n .$

$$
Y - \theta_ {i} x _ {i} = \frac {G - 1}{g} - \frac {G H _ {i}}{G + g H _ {i}} = \frac {G (G - 1) - g H _ {i}}{g (G + g H _ {i})} = \frac {Y - H _ {i} + g Y ^ {2}}{G + g H _ {i}}
$$

which, of course, means that $Y \ge H _ { i } \Rightarrow Y \ge \theta _ { i } x _ { i }$ . Next, we also know that

$$
\begin{array}{l} Y - H _ {i} = \left(1 - \sum_ {j = 1} ^ {n} \theta_ {j} x _ {j}\right) - \theta_ {i} \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) + \sum_ {j = 1} ^ {i - 1} \theta_ {j} x _ {j} = \left(1 - \sum_ {j = i} ^ {n} \theta_ {j} x _ {j}\right) - \theta_ {i} \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) \\ \geq \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) - \theta_ {i} \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) = (1 - \theta_ {i}) \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) \geq 0 \end{array}
$$

Therefore, $Y \geq H _ { i } ,$ , and hence $Y \ge \theta _ { \ast } x _ { i }$ , for all $i = 1 , 2 , . . . , n$ . Summing both sides over $i ,$ we get

$$
n Y \geq \sum_ {i = 1} ^ {n} \theta_ {i} x _ {i} = 1 - Y \Leftrightarrow Y \geq \frac {1}{n + 1} \Leftrightarrow \sum_ {i = 1} ^ {n} \theta_ {i} x _ {i} = 1 - Y \leq \frac {n}{n + 1}
$$

(iii) $\operatorname { I f } \theta _ { i } = \theta _ { k }$ then for every $l , k < l \leq i , \theta _ { l } - \theta _ { l - 1 } = 0$ . Therefore, from $( \mathrm { A } 2 ) , H _ { i } - H _ { k } = 0$ implying $\theta _ { i } x _ { i } - \theta _ { k } x _ { k } = 0 \mathrm { o r } x _ { i } = x _ { k } .$

(iv) From the proof of part (ii), we know that $Y \ge \theta _ { i } x _ { i }$ . Therefore,

$$
\frac {\partial^ {2} R _ {i}}{\partial g \partial \theta_ {i}} = x _ {i} \left(\left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) \left(Y - \theta_ {i} x _ {i}\right) + x _ {i} \sum_ {j = 1} ^ {i - 1} \theta_ {j} x _ {j}\right) \geq 0
$$

On the other hand, from the proof of part (i), we know that $\begin{array} { r } { \theta _ { i } x _ { i } = \frac { G H _ { i } } { G + g H _ { i } } } \end{array}$ ; we can then show that

$$
\frac {\partial^ {2} R _ {i}}{\partial g \partial x _ {i}} = Y H _ {i} - \theta_ {i} x _ {i} (H _ {i} + Y) = - \frac {H _ {i} ^ {2}}{G + g H _ {i}} <   0
$$

In other words, when g increases, the first order response by a vendor to this change is to increase quality and decrease market share. However, when $\theta _ { i } = 1$ , the vendor cannot increase quality any further and its only first order response would be to decrease its market share. Since such a response complements other vendors’ actions, in equilibrium, $x _ { i }$ must decrease.

(v) We prove this part by contradiction. Let there be an equilibrium with $\theta _ { i } = \theta _ { k } < 1$ , for some $k < i ,$ with $1 \leq i , k \leq n$ . We know that vendor i solves the following maximization problem:

$$
\underset {\theta_ {i}, x _ {i}} {\text { Max }} R _ {i} = x _ {i} G \left(\theta_ {i} \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) - \sum_ {j = 1} ^ {i - 1} \theta_ {j} x _ {j}\right) - c (\theta_ {i})
$$

Since $\theta _ { i } < 1$ (by assumption), the first order condition with respect to $\theta _ { i }$ must be satisfied:

$$
\frac {\partial R _ {i}}{\partial \theta_ {i}} = x _ {i} \left(G \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) - g x _ {i} \left(\theta_ {i} \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) - \sum_ {j = 1} ^ {i - 1} \theta_ {j} x _ {j}\right)\right) - c ^ {\prime} (\theta_ {i}) = 0
$$

Furthermore, since $\theta _ { i } = \theta _ { j } ,$ , for al ${ \mid } j , k { \leq } j { < } i ,$ we know from above that the market shares of these vendors would be equal. We set $\theta _ { k } = \dots =$ $\theta _ { i } = \theta$ and $x _ { k } = \ l _ { \dots } = x _ { i } = x$ to get

$$
\begin{array}{l} c ^ {\prime} (\theta) = G x \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) - g x ^ {2} \theta \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) + g x ^ {2} \sum_ {j = 1} ^ {i - 1} \theta_ {j} x _ {j} \\ = G x \left(1 - \sum_ {j = k} ^ {n} x _ {j} + \sum_ {j = k} ^ {i - 1} x _ {j}\right) - g x ^ {2} \theta \left(1 - \sum_ {j = k} ^ {n} x _ {j} + \sum_ {j = k} ^ {i - 1} x _ {j}\right) + g x ^ {2} \left(\sum_ {j = 1} ^ {k - 1} \theta_ {j} x _ {j} + \sum_ {j = k} ^ {i - 1} \theta_ {j} x _ {j}\right) \\ = G x \left(1 - \sum_ {j = k} ^ {n} x _ {j} + (i - k) x\right) - g x ^ {2} \theta \left(1 - \sum_ {j = k} ^ {n} x _ {j} + (i - k) x\right) + g x ^ {2} \left(\sum_ {j = 1} ^ {k - 1} \theta_ {j} x _ {j} + (i - k) \theta x\right) \\ = G x \left(1 - \sum_ {j = k} ^ {n} x _ {j} + (i - k) x\right) - g x ^ {2} \theta \left(1 - \sum_ {j = k} ^ {n} x _ {j}\right) + g x ^ {2} \sum_ {j = 1} ^ {k - 1} \theta_ {j} x _ {j} \end{array}\tag{A3}
$$

We now consider how the revenue of the $k ^ { \mathrm { { ^ { t h } } } }$ vendor changes with the quality of its own product:

$$
\frac {\partial R _ {k}}{\partial \theta_ {k}} = G x \left(1 - \sum_ {j = k} ^ {n} x _ {j}\right) - g x ^ {2} \theta \left(1 - \sum_ {j = k} ^ {n} x _ {j}\right) + g x ^ {2} \sum_ {j = 1} ^ {k - 1} \theta_ {j} x _ {j} - c ^ {\prime} (\theta)
$$

Substituting (A3) into the above expression, we get $\frac { \partial R _ { k } } { \partial \theta _ { k } } = - G x ^ { 2 } \big ( i - k \big ) < 0$ , which is a violation of the first order condition for an interior solution. #

## Proof of Theorem 1

We first show that there exists a g beyond which all vendors offer a quality level of one. To see this, consider vendor 1. Its profit is given by $R _ { 1 } = x _ { 1 } G H _ { 1 } - c ( \theta _ { 1 } )$ . Therefore,

$$
\frac {\partial R _ {1}}{\partial \theta_ {1}} = x _ {1} \left(1 - \sum_ {j = 1} ^ {n} x _ {j}\right) \left(G - g \theta_ {1} x _ {1}\right) - c ^ {\prime} \left(\theta_ {1}\right)
$$

From (4), $Y = 1 - \Sigma _ { j = 1 } ^ { n } \theta _ { j } x _ { j }$ <sub>j</sub> and $G = 1 + g Y$ . Furthermore, from the proof of Proposition 1(i), we know that $\begin{array} { r } { \theta _ { 1 } x _ { 1 } = \frac { G H _ { 1 } } { G + g H _ { 1 } } } \end{array}$ in equilibrium. Therefore, we have

$$
G - g \theta_ {1} x _ {1} \geq \frac {(1 + g Y) ^ {2}}{1 + g (H _ {1} + Y)} \geq \frac {(1 + g Y) ^ {2}}{1 + 2 g Y}
$$

The last inequality results from the fact that $H _ { 1 } \leq Y ;$ see the proof of Proposition 1(ii). Now, from that proof, we also know that $\textstyle Y \geq { \frac { 1 } { n + 1 } }$ , so $\textstyle g Y \geq { \frac { g } { n + 1 } }$ . Furthermore, $\frac { { \left( 1 + g Y \right) } ^ { 2 } } { 1 + 2 g Y }$ is an increasing function of $_ { g Y . }$ . Hence, we can write

$$
G - g \theta_ {1} x _ {1} \geq \frac {(1 + g Y) ^ {2}}{1 + 2 g Y} \geq \frac {\left(1 + \frac {g}{n + 1}\right) ^ {2}}{1 + \frac {2 g}{n + 1}} = \frac {(n + 1 + g) ^ {2}}{(n + 1) (n + 1 + 2 g)}
$$

which is clearly an increasing function of $g .$ Since $c ^ { \prime } ( 1 )$ is bounded, for a sufficiently large g, we will have

$$
\left. \frac {\partial R _ {1}}{\partial \theta_ {1}} \right| _ {\theta_ {1} = 1} \geq x _ {1} \left(1 - \sum_ {j = 1} ^ {n} x _ {j}\right) \frac {(n + 1 + g) ^ {2}}{(n + 1) (n + 1 + 2 g)} - c ^ {\prime} (1) > 0
$$

Since $c \left( \cdot \right)$ is an increasing convex function, the above means that, in equilibrium, an interior solution is not possible and $\theta _ { \scriptscriptstyle 1 } = 1$ . This, in turn, implies that $\theta _ { i } = 1$ , for all $i = 2 , . . . , n .$ . In other words, there must exist a threshold for g—we characterize this threshold as $\gamma _ { n } ^ { - 1 } ( c )$ in Theorem 2—beyond which vertical differentiation would disappear.

We now consider what happens when g starts decreasing below this threshold. Of course, if the development cost is negligible, trivially, all vendors would continue to offer a quality level of one, irrespective of the value of g. However, if the development cost is significant, some vendors would have to drop their quality level below one, but we will show that they can do so only one vendor at a time. To prove this last claim, suppose that two vendors drop the quality level to below one at the same time. At the value of g where this occurs, these vendors must be barely at the same interior solution. However, from the proof of Proposition 1(v), it is clear that no two vendors can have the same interior solution. Therefore, when g decreases, vendors would not only drop their quality levels from one, but would also do so only one at a time, while maintaining the order of their quality levels. Equivalently, as g increases, their qualities would reach one at different values of g. It is also clear from the proof of Proposition 1(iv) that, once a quality level reaches one, it cannot drop when g increases further. Taken together, it is clear that, as g increases, the segmentation level in the market gradually decreases. #

## Proof of Theorem 2

To prove the existence of the inverse function, it is sufficient to show that $\gamma _ { n } ( g )$ is a strictly monotonic function. It turns out that $\begin{array} { r } { \frac { \partial { \gamma } _ { n } ( g ) } { \partial g } > 0 } \end{array}$ To see this, we observe that

$$
\frac {\partial \gamma_ {n} (g)}{\partial g} = \frac {A - B}{2 g ^ {3} n ^ {2} (n + 2) ^ {3} \sqrt {4 g (1 + g) + (n + 1) ^ {2}}}
$$

where

$$
\begin{array}{l} A = 2 + 8 g + 8 g ^ {2} + 6 n + 1 3 g n + 1 0 g ^ {2} n + 6 n ^ {2} + 8 g n ^ {2} + 2 g ^ {3} n ^ {2} + 4 g ^ {4} n ^ {2} + 2 n ^ {3} + 3 g n ^ {3}, \\ B = C \sqrt {4 g (1 + g) + (n + 1) ^ {2}}, \quad \text { and } \\ C = 2 + 4 g + 4 n + 5 g n + 2 n ^ {2} + 3 g n ^ {2} - 2 g ^ {3} n ^ {2} \end{array}
$$

Now $A ^ { 2 } - B ^ { 2 } = 4 g ^ { 3 } \big ( 1 + g \big ) ^ { 2 } n ^ { 2 } \big ( n + 2 \big ) ^ { 3 } D$ , where $D = 4 g + 2 n - 2 - g n$ ; hence, $A ^ { 2 } > B ^ { 2 } , \operatorname { o r } A > B .$ , as long as $D > 0 . \ \mathrm { H } g \leq 2$ , D is always positive. Therefore, we only consider the case where $g > 2 .$ In that case, $D > 0$ if and only if $\begin{array} { r } { n < \frac { 2 { \left( 2 g - 1 \right) } } { g - 2 } } \end{array}$ . Suppose not. Then, there is $\mathtt { a } \delta \ge 0$ such that $\begin{array} { r } { n = \delta + \frac { 2 { { \left( { 2 g - 1 } \right) } } } { { { g - 2 } } } } \end{array}$ . Substituting this n into C leads to

$$
C = \frac {3 2 (1 - g) ^ {3} (1 + g) ^ {2}}{(g - 2) ^ {2}} + \frac {\delta (8 (1 - 2 g) g ^ {3} + 2 9 g ^ {2} - 2 g - 1 6)}{g - 2} + (2 + 3 g - 2 g ^ {3}) \delta^ {2}
$$

The first and the third terms are clearly negative since $g > 2$ . Furthermore, since $\delta \geq 0 ,$ when $g > 2$ , it can be shown, after some algebra, that the second term cannot be positive. Therefore, $C < 0 ,$ implying $B < 0$ . Since A > 0 always, this, in turn, implies that $A > B ,$ which completes the proof of the first part

For the second part, we note that the oligopoly equilibrium can be in only one of $( n + 1 )$ regions. Let Region I denote the range of g values with the first market configuration, where all vendors offer the quality level of one. Similarly, let Region II be the range for the second one, where only the lowest quality vendor, namely vendor 1, offers a quality level below one $( \theta _ { 1 } < 1 )$ . Vertical differentiation will be observed as soon as the equilibrium outcome moves out of Region I. Therefore, we only need to examine the boundary between Regions I and II. In both the regions, $\theta _ { 2 } = \theta _ { 3 } = \ldots = \theta _ { n } = 1$ , and it follows from Proposition 1(iii) that $x _ { 2 } = x _ { 3 } = \ldots = x _ { n } .$ Let $x _ { h }$ denote this common market share. The optimization problem of vendor 1 can, therefore, be simplified to

$$
\operatorname * {M a x} _ {\theta_ {1}, x _ {1}} R _ {1} = x _ {1} \theta_ {1} (1 - (n - 1) x _ {h} - x _ {1}) (1 + g (1 - (n - 1) x _ {h} - \theta_ {1} x _ {1})) - c (\theta_ {1});
$$

$$
\text { s   .   t   . } \quad \theta_ {1} > 0, \quad (n - 1) x _ {h} + x _ {1} \leq 1
$$

The following first order condition must be satisfied by the solution of the unconstrained problem:

$$
\frac {\partial R _ {1}}{\partial \theta_ {1}} = x _ {1} (1 - (n - 1) x _ {h} - x _ {1}) (1 + g (1 - (n - 1) x _ {h} - \theta_ {1} x _ {1})) - g x _ {1} ^ {2} \theta_ {1} (1 - (n - 1) x _ {h} - x _ {1}) - c ^ {\prime} (\theta_ {1}) = 0
$$

Since, at the boundary of Regions I and $\begin{array} { r } { \mathrm { I I } , \theta _ { \mathrm { l } } = 1 } \end{array}$ , we substitute it above to obtain

$$
c ^ {\prime} (1) = x _ {1} \bigl (1 - (n - 1) x _ {h} - x _ {1} \bigr) \bigl (1 + g \bigl (1 - (n - 1) x _ {h} - 2 x _ {1} \bigr) \bigr) = \gamma_ {n}\tag{A4}
$$

Now, when $\theta \mathrm { { s } }$ are all one, first order conditions with respect to $x _ { i } , i = 1 , 2 , . . . , n ,$ result in

$$
x _ {h} = x _ {1} = x = \frac {(1 + 2 g) (n + 1) - \sqrt {4 g (1 + g) + (n + 1) ^ {2}}}{2 g n (n + 2)}
$$

which can be substituted into (A4) to obtain

$$
\gamma_ {n} (g) = \frac {\mu_ {n} (g) + v _ {n} (g)}{2 g ^ {2} n ^ {2} (n + 2) ^ {3}}
$$

where

$$
\mu_ {n} (g) = 2 g ^ {3} n ^ {2} + (n + 1) ^ {2} + g ^ {2} (n (n + 1) (n + 6) + 4) + g (n (3 n + 5) + 4)
$$

and

$$
v _ {n} (g) = \left(g ^ {2} n ^ {2} - g (3 n + 2) - (n + 1)\right) \sqrt {4 g (1 + g) + (n + 1) ^ {2}}
$$

Therefore, the condition $c ^ { \prime } ( 1 ) > \gamma _ { n } ( g )$ —which is equivalent to $g < \gamma _ { n } ^ { - 1 } { \bigl ( } c ^ { \prime } ( 1 ) { \bigr ) }$ —ensures that the outcome is not in Region I. #

## Proof of Proposition 2

Since $\gamma _ { n } ( g ) = \frac { \mu _ { n } ( g ) + \nu _ { n } ( g ) } { 2 g ^ { 2 } n ^ { 2 } ( n + 2 ) ^ { 3 } }$ , using l’Hospital’s rule twice, we get

$$
\gamma_ {n} (0) = \lim _ {g \rightarrow 0} \gamma_ {n} (g) = \frac {\mu_ {n} ^ {\prime \prime} (0) + v _ {n} ^ {\prime \prime} (0)}{4 n ^ {2} (n + 2) ^ {3}}
$$

The result follows directly from the above. #

## Proof of Theorem 3

Recall that

$$
R _ {v} = G H _ {i} x _ {i} + G H _ {k} x _ {k} + G \sum_ {t = 1} ^ {m} H _ {l _ {t}} x _ {l _ {t}} - c (\theta_ {i})
$$

where, as before

$$
G = 1 + g Y, \quad Y = 1 - \sum_ {j = 1} ^ {n} \theta_ {j} x _ {j}, \quad \text { and } \quad H _ {i} = \theta_ {i} \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) - \sum_ {j = 1} ^ {i - 1} \theta_ {j} x _ {j}
$$

Therefore, we have

$$
\frac {\partial G}{\partial x _ {j}} = - g \theta_ {j} \quad \text { and } \frac {\partial H _ {i}}{\partial x _ {j}} = \left\{ \begin{array}{l l} - \theta_ {i} & \text { if   } j \geq i \\ - \theta_ {j} & \text { otherwise } \end{array} \right.
$$

Combining the above, we can write

$$
\begin{array}{r l} \frac {\partial R _ {v}}{\partial x _ {i}} & = G H _ {i} + x _ {i} \left(G \frac {\partial H _ {i}}{\partial x _ {i}} + H _ {i} \frac {\partial G}{\partial x _ {i}}\right) + x _ {k} \left(G \frac {\partial H _ {k}}{\partial x _ {i}} + H _ {k} \frac {\partial G}{\partial x _ {i}}\right) + \sum_ {t = 1} ^ {m} x _ {l _ {t}} \left(G \frac {\partial H _ {l _ {t}}}{\partial x _ {i}} + H _ {l _ {t}} \frac {\partial G}{\partial x _ {i}}\right) \\ & = G H _ {i} - G \theta_ {i} x _ {i} - g \theta_ {i} x _ {i} H _ {i} - G \theta_ {k} x _ {k} - g \theta_ {i} x _ {k} H _ {k} - \sum_ {t = 1} ^ {m} x _ {l _ {t}} \left(G \theta_ {l _ {t}} + g \theta_ {i} H _ {l _ {t}}\right) \end{array}
$$

and

$$
\begin{array}{l} \frac {\partial R _ {v}}{\partial x _ {k}} = x _ {i} \left(G \frac {\partial H _ {i}}{\partial x _ {k}} + H _ {i} \frac {\partial G}{\partial x _ {k}}\right) + G H _ {k} + x _ {k} \left(G \frac {\partial H _ {k}}{\partial x _ {k}} + H _ {k} \frac {\partial G}{\partial x _ {k}}\right) + \sum_ {t = 1} ^ {m} x _ {l _ {t}} \left(G \frac {\partial H _ {l _ {t}}}{\partial x _ {k}} + H _ {l _ {t}} \frac {\partial G}{\partial x _ {k}}\right) \\ = G H _ {k} - G \theta_ {k} x _ {i} - g \theta_ {k} x _ {i} H _ {i} - G \theta_ {k} x _ {k} - g \theta_ {k} x _ {k} H _ {k} - \sum_ {t = 1} ^ {m} x _ {l _ {t}} \left(G \theta_ {l _ {t}} + g \theta_ {k} H _ {l _ {t}}\right) \end{array}
$$

The above expressions lead to

$$
\begin{array}{r l} \frac {1}{\theta_ {i}} \frac {\partial R _ {v}}{\partial x _ {i}} - \frac {1}{\theta_ {k}} \frac {\partial R _ {v}}{\partial x _ {k}} & = \frac {1}{\theta_ {i} \theta_ {k}} \left[ \theta_ {k} \frac {\partial R _ {v}}{\partial x _ {i}} - \theta_ {i} \frac {\partial R _ {v}}{\partial x _ {k}} \right] \\ & = \frac {G}{\theta_ {i} \theta_ {k}} \left[ (\theta_ {k} H _ {i} - \theta_ {i} H _ {k}) + (\theta_ {i} - \theta_ {k}) (\theta_ {k} x _ {k} + \sum_ {t = 1} ^ {m} \theta_ {l _ {t}} x _ {l _ {t}}) \right] \end{array}\tag{A5}
$$

We now observe

$$
\begin{array}{l} \theta_ {k} H _ {i} - \theta_ {i} H _ {k} = \theta_ {i} \theta_ {k} \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) - \theta_ {k} \sum_ {j = 1} ^ {i - 1} \theta_ {j} x _ {j} - \theta_ {i} \theta_ {k} \left(1 - \sum_ {j = k} ^ {n} x _ {j}\right) + \theta_ {i} \sum_ {j = 1} ^ {k - 1} \theta_ {j} x _ {j} \\ = \theta_ {i} \theta_ {k} \sum_ {j = k} ^ {i - 1} x _ {j} + (\theta_ {i} - \theta_ {k}) \sum_ {j = 1} ^ {k - 1} \theta_ {j} x _ {j} - \theta_ {k} \sum_ {j = k} ^ {i - 1} \theta_ {j} x _ {j} \\ = (\theta_ {i} - \theta_ {k}) \sum_ {j = 1} ^ {k - 1} \theta_ {j} x _ {j} + \theta_ {k} \sum_ {j = k} ^ {i - 1} \theta_ {i} x _ {j} - \theta_ {k} \sum_ {j = k} ^ {i - 1} \theta_ {j} x _ {j} \\ = (\theta_ {i} - \theta_ {k}) \sum_ {j = 1} ^ {k - 1} \theta_ {j} x _ {j} + \theta_ {k} \sum_ {j = k} ^ {i + 1} (\theta_ {i} - \theta_ {j}) x _ {j} \end{array}
$$

Substituting this into (A5) leads to

$$
\frac {1}{\theta_ {i}} \frac {\partial R _ {v}}{\partial x _ {i}} - \frac {1}{\theta_ {k}} \frac {\partial R _ {v}}{\partial x _ {k}} = \frac {G}{\theta_ {i} \theta_ {k}} \left[ \theta_ {k} \sum_ {j = k} ^ {i - 1} \left(\theta_ {i} - \theta_ {j}\right) x _ {j} + \left(\theta_ {i} - \theta_ {k}\right) \left(\sum_ {j = 1} ^ {k} \theta_ {j} x _ {j} + \sum_ {t = 1} ^ {m} \theta_ {l _ {i}} x _ {l _ {t}}\right) \right]
$$

Since $\theta _ { i }$ is the largest among all the versions provided, it is easy to see that the right hand side of the above expression is positive, which is a violation of the condition in (7). #

## Proof of Lemma 2

This proof is similar to that of Lemma 1. We can show that (9) implies

$$
p _ {i} = \left(1 + g \left(1 - \sum_ {j = 0} ^ {n} \theta_ {j} x _ {j}\right)\right) \left(\theta_ {i} \left(1 - \sum_ {j = i} ^ {n} x _ {j}\right) - \sum_ {j = 0} ^ {i - 1} \theta_ {j} x _ {j}\right)
$$

Substituting $x _ { 0 } = 1 - \Sigma _ { j = 1 } ^ { n } x _ { j }$ and $\theta _ { 0 } = \phi$ and rearranging terms, we get (10). #

## Proof of Theorem 4

It is similar to the proofs of Theorems 1 and 2, with $g ^ { \prime } = g ( 1 - \phi )$
