---
otero_id: 1454
otero_key: "JSEK4FBC"
title: "Impact of Cyberattacks by Malicious Hackers on the Competition in Software Markets"
authors: "Ravi Sen; Ajay Verma; Gregory R. Heim"
year: "2020"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2019.1705511"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Impact of Cyberattacks by Malicious Hackers on the Competition in Software Markets

Ravi Sen, Ajay Verma & Gregory R. Heim

To cite this article: Ravi Sen, Ajay Verma & Gregory R. Heim (2020) Impact of Cyberattacks by Malicious Hackers on the Competition in Software Markets, Journal of Management Information Systems, 37:1, 191-216, DOI: 10.1080/07421222.2019.1705511

To link to this article: https://doi.org/10.1080/07421222.2019.1705511

![](/api/attachments/JSEK4FBC/fulltext/images/9d8d74ac488193c76c34f6ef8ab149ab1c1edac83619097ffd9b56514b88dc5e.jpg)

View supplementary material

![](/api/attachments/JSEK4FBC/fulltext/images/954c567235830733800ceefbebabfaefc59bea8c79f31f06ee1bb846d6b8f882.jpg)

Published online: 01 Mar 2020.

![](/api/attachments/JSEK4FBC/fulltext/images/6c839610023429593863dc0fc9ff8188f94bdf18df85d02fdf5337b3f747c87d.jpg)

Submit your article to this journal

![](/api/attachments/JSEK4FBC/fulltext/images/c0b911b80db99743754e726258ebbac769c9406302c4ee8b3066d6f5e976ae99.jpg)

View related articles

![](/api/attachments/JSEK4FBC/fulltext/images/d56fd6f91ee9d6b3a4da8e70344e17a2eb66996a8ba4e29627d2bac62c8bc883.jpg)

View Crossmark data

Check for updates

# Impact of Cyberattacks by Malicious Hackers on the Competition in Software Markets

Ravi Sen<sup>a</sup>, Ajay Verma<sup>b</sup>, and Gregory R. Heim<sup>a</sup>

<sup>a</sup>Texas A&M University, College Station, Texas, USA; <sup>b</sup>Guidance, Navigation & Control Engineer, Lockheed Martin Missiles and Fire Control, Grand Prairie, Texas, USA

## ABSTRACT

The number of malicious hacking incidents in our increasingly ITenabled world has been increasing over the years. Conventional wisdom focuses on negative impacts of these malicious hacker activities. We posit that malicious hacker activities also might lead to some unintended consequences, speci<sup>fi</sup>cally related to altering of software market structure, and associated stakeholder consequences. In this study, we model the competition between two software platforms in the presence of malicious hackers who perform cyberattacks against one or both software platforms. We compare a benchmark case where malicious hackers are either absent, or if present do not target the software platforms, against a <sup>fi</sup>rst scenario where only one software platform is targeted, and a second scenario where both software platforms are targeted. Interestingly, we <sup>fi</sup>nd the presence of malicious hackers’ activities is not always detrimental to all software industry stakeholders. In general, the results suggest that the presence of malicious hackers is more likely to result in a competitive market, while their absence is more likely to result in a monopoly. Furthermore, we show that under certain market conditions, the unsecure software platform targeted by hackers potentially can drive its more secure competitor out of the market.

KEYWORDS

Software competition; malicious hackers; software markets; cyberattacks; software platforms

## Introduction

This paper examines stakeholder implications of cyberattacks performed by malicious software hackers on software platform vendors within a single software market sector. In the good old days of the software industry, the term hacker was used as a compliment to describe very clever programmers, without ascribing ethical or moral valence to the actions of such individuals. More recently, the term has taken on negative connotations. Dictionaries today de<sup>fi</sup>ne a hacker as “a person who uses computers to gain unauthorized access to data” [13], and as “a person who secretly gets access to a computer system in order to get information, cause damage, etc.” [32]. While there have been attempts to use other terms to distinguish hackers having malicious intent (e.g., crackers, Black Hats, Grey Hats,<sup>1</sup> unethical hackers), the fact remains that the common understanding of the term hacker is closer to the previously provided de<sup>fi</sup>nitions. As such, in this paper, the term hacker should be understood to mean malicious hackers. We do not focus on ethical/ white hat hackers, security consultants such as pen-testers, or vulnerability discoverers because the actions of these individuals are targeted at and requested by their clients. Moreover, these non-malicious hackers do not exploit software users, release malware, or steal data.

Hacking activities are by no means only a contemporary phenomenon, yet anecdotally they often seem to be. With expanding use of new technology variants, the variety of innovations in hacking modes continues to expand [40]. Technology hacking today results in a huge number of hacking incidents (i.e., over 64,000 in 2015) and results in veri<sup>fi</sup>ed data breaches [17, 38]. Hacker related incidents a<sup>f</sup>ect a large proportion of individuals and lead to large annual stakeholder costs [10, 11, 34]. Annually over the past decade, veri<sup>fi</sup>ed data breaches have been most frequently caused by several variants of software hacking attacks [20, 38]. Hacking activities are so pervasive globally that one can observe the real-time generation of malicious hacking across the globe via resources such as the Kaspersky Cyberthreat Real-Time Map.<sup>2</sup> Yet, neither popular media, nor government studies, nor academic literatures have investigated the role of this malicious hacking activity in shaping the software industry.

In this study, we focus on the activities of malicious hackers and observe that perhaps the net outcome of their hacking e<sup>f</sup>orts is not always bad. The growth of malicious hacking phenomena across major public, private, and governmental organizations motivates the research questions behind this study: What is the impact of malicious hackers’ attacks on competition in software markets? Is the presence of malicious hacker attacks in a marketplace all bad? Or are there some positive consequences (intended or unintended) of malicious hackers’ activities? Among the possible consequences of malicious hacking, the most obvious outcome generally concerns changes in the competitive market that may a<sup>f</sup>ect stakeholder (e.g., end user, corporate client, or software vendor) utility in some manner. Through a stylized model, we examine impacts of the presence of malicious hackers who perform successful cyberattacks against one or several software vendors in a software industry sector. Thus, from among the potential outcomes of malicious hacking, this paper largely focuses on outcomes derived from resultant changes to competition within a software industry sector. Studying this impact of malicious hacker attacks on competition is important because of the wide-ranging and pervasive nature of malicious hacker attacks today, a<sup>f</sup>ecting software industry vendors as well as major users of software and, thus, the competitive structure of many industries.

We investigate these research questions in the context of a software market. We model a market consisting of two competing software platforms in the presence of malicious hackers. We set up a benchmark case where the hackers are either absent or do not target any cyberattacks against the competing software platforms. We then compare the benchmark case against a <sup>fi</sup>rst scenario where one software platform is targeted by cyberattacks, and a second scenario where both software platforms are targeted by cyberattacks. We assume these malicious hacker attacks are successful attacks, since unsuccessful attacks will not lead to repercussions for software vendors or for software users. Through stylized analytical models, we dig into the conventional wisdom that malicious hackers cause only damages and losses for software industry stakeholders. Doing so <sup>fi</sup>lls in a literature gap pertaining to social welfare implications of stakeholders, arising from actions of malicious hackers, and leads to several useful insights concerning the presence of software hacker activities on software market competition.

Interestingly, we <sup>fi</sup>nd the presence of malicious hackers in a software market is a double-edged sword and is not always detrimental to software industry stakeholders. We <sup>fi</sup>nd that the presence of such hackers makes the software market more competitive. As a result, consumers may unintentionally bene<sup>fi</sup>t from the presence of malicious hackers, in short because these hackers tend to target actions proportionally with respect to the software platforms having a large numbers of users. We also observe that under certain conditions an unsecure software platform targeted by hackers potentially can drive its more secure competitor out of the software market. This <sup>fi</sup>nding illustrates contextspeci<sup>fi</sup>c managerial insights useful to the long-term management of software platforms in the presence of malicious hacker activities.

The paper is organized as follows. The second section provides a brief overview of relevant literature. The third section develops the analytical model. The fourth section presents our analysis of implications for software markets. The <sup>fi</sup>nal section concludes with contributions, limitations, and future directions.

## Literature Review

Competition in a marketplace in general, and among software products in particular, has been studied for a long time. Early studies investigated the impact of network e<sup>f</sup>ects on competition between systems [26], competition between standards in a software market [19], and on competition within software markets [8, 18]. More recently, some studies explore the impact of network e<sup>f</sup>ects on software completion between open source and proprietary software products [12, 24, and 35]. Lin [29] explores this same competition under the in<sup>fl</sup>uence of network e<sup>f</sup>ects and varying levels of users’ software skills. Lanzi [28] explores the issue under an assumption that the competing software products are compatible. Since software markets experience two-sided network externalities, researchers have incorporated this factor into studies on competition in software markets [33]. In addition to the role of network e<sup>f</sup>ects on software competition, researchers have also studied the impact of di<sup>f</sup>erent channel strategies and product heterogeneity on competition between software products. For example, Bitzer [6] investigated the impact of product heterogeneity on the competition between open source software (OSS) and commercial software, while Fan et al. [14] analyze the competition between Software-as-a-Service (SaaS) and traditional shrinkwrap software. Finally, some studies investigate the impact of piracy on software markets [e.g., 31].

However, the existing literature on competition between software products or systems has a major gap. To the best of our knowledge, no study investigates the impact of malicious hacker attacks on the competition between software products or software platforms. Without accounting for hacker actions, extant models examine a software producer’s decision about releasing vulnerable software or patching vulnerabilities so hackers cannot attack them [2]. Models also study liability arising from software vulnerabilities [3, 27] and to what extent known software vulnerabilities can a<sup>f</sup>ect software vendor market values [10, 37]. Studies model markets for the generation of software vulnerabilities [25] and competitive market policy aspects of vulnerability discovery and disclosure activities of hackers [9, 36]. Yet, to the best of our knowledge, no prior study examines competitive statics that arise from malicious hacker activity within a software market structure. This situation motivates the following question: Why is it important to understand the impact of malicious hacker attacks on competition in software markets?

Malicious hacker attacks on technology are not a modern phenomenon. One of the earliest examples of malicious hacking was the disruption of John Ambrose Fleming’s public demonstration of Guglielmo Marconi’s wireless telegraphy technology by Nevil Maskelyne [30]. In 1903, Maskelyne managed to “hack” the demonstration and send insulting Morse code messages through the auditorium’s projector during this demonstration [30]. More recently, in January 2016 account information for at least 500 million Yahoo users was hacked,<sup>3</sup> and in May 2017, data on 143 million Americans was exposed by Equifax.<sup>4</sup>

It has been established that security breaches caused by malicious hackers lead to disruptions and downtime in the targeted systems, causing <sup>fi</sup>nancial loss for the users of these systems. The users of the software systems incur other costs as well. For instance, industrial users may have to pay additional insurance premiums [22] for using software known to have weak security. As a result, potential users are more likely to favor software that has stronger security. Moreover, existing software users can punish a vendor of vulnerable software by switching to a competing vendor, or delaying their software upgrade purchases, while potential customers may avoid buying the vulnerable software product [37]. Finally, Wright [39] argues that users of software will act rationally, which implies that all else held equal (e.g., similar features and functionality), a user should choose more secure software over less secure software. Since malicious hackers often intentionally draw attention to software security (or a lack thereof), it is reasonable to assume that the presence of malicious hackers should impact competition in a software market.

The question remains as to the nature of the malicious hacker impact on market competition. In this study, we address this issue. We contribute by modeling a software market as a duopoly, with malicious hackers targeting either one or both of the competing software platforms. The results show that in the absence of malicious hackers, the most likely equilibrium market structure is a monopoly. Interestingly, when hackers target at least one of the competing software products, the resulting market structure is more competitive. As such, malicious hackers can be seen to play a potentially useful role in ensuring more competitive software marketplaces. We contribute by demonstrating potential software industry outcomes under di<sup>f</sup>erent sets of possible market conditions.

## Software Market Model

In this section, we <sup>fi</sup>rst develop a model of competition within a software market where competing software platforms are targeted by malicious hackers. In the following section, we then analyze this model for equilibrium outcomes, followed by a discussion of the results.

## Software Market

For any software category, we assume that two broad software platforms (e.g., Android vs. iOS; Apache vs. IIS) re<sup>fl</sup>ect the software market structure su<sup>fi</sup>ciently accurately. We will refer to these software platforms by the terms Software X and Software Y, or just X and Y for simplicity. Also, we will use the term software, software product, and software platform interchangeably. We assume X and Y compete for the same users (both individuals and organizations). Competition ensures that X and Y vendors behave in such a manner as to prevent the competitor from monopolizing the market. Finally, both X and Y are assumed to contain the essential functional software features sought by potential users, and both software platforms are assumed to meet the usability criteria of all users. This latter assumption is required to ensure that any change in software industry market share that we observe over the long run can be attributed primarily to hacker activities targeted at X and Y. These assumptions are realistic when seen within the context of several software platform markets (e.g., mobile operating systems, mobile communications networks, gaming platforms).

## Market Share

The model assumes X’s and Y’s market share growth is a function of new users who decide to adopt the software, switch from the competing software, and switch to the competing software. This growth rate is restrained by the number of malicious hackers who target each of the software platforms. The generic conceptual model for this growth rate is as follows:

$$
\begin{array}{l} \left( \begin{array}{c} \text {Rate of} \\ \text {Change} \\ \text {of} \\ \text {Market Share} \end{array} \right) = \left( \begin{array}{c} \text {Rate of} \\ \text {New} \\ \text {Users} \\ \text {Adopting} \\ \text {the} \\ \text {Software} \end{array} \right) - \left( \begin{array}{c} \text {Rate of} \\ \text {Existing} \\ \text {Users} \\ \text {Switching} \\ \text {to Competition} \end{array} \right) + \left( \begin{array}{c} \text {Rate of} \\ \text {Users} \\ \text {Switching} \\ \text {from} \\ \text {Competition} \end{array} \right) \\ - \binom {\text {Restraining}} {\text {Effect of}} \\ \text {Hackers} \end{array}\tag{1}
$$

We now develop this equation by making some assumptions, and then under these assumptions, we mathematically describe the various components of the conceptual model.

## Rate of New Users Adopting the Software

The net growth rate of any software is modeled as a function of its intrinsic growth rate (i.e., the growth rate in the absence of any competition), and any restraining e<sup>f</sup>ects of the market share of the competing software and the total market size for this type of software. The conceptual model for the rate of new users adopting each software platform is as follows:

$$
\begin{array}{l} \left( \begin{array}{c} \text {Rate of} \\ \text {New} \\ \text {Users} \\ \text {Adopting} \\ \text {the} \\ \text {Software} \end{array} \right) = \binom {\text {Intrinsic Growth}} {\text {Rate of the Software}} - \binom {\text {Restraining Effect}} {\text {of the Total}} \\ - \binom {\text {Restraining Effect}} {\text {of the Market Share of}} \\ \text {Competing Software} \end{array}\tag{2}
$$

## Intrinsic Growth in Market Share

Intrinsic growth is the growth rate of a software platform in the absence of any competition or malicious hackers. We assume this intrinsic growth to follow an exponential function. We further assume that the population of potential software users for a platform is su<sup>fi</sup>ciently large. As a result, the random <sup>fl</sup>uctuations between individual users are small when compared against the whole population size. Therefore, it is safe to assume each potential user has an equal chance of adopting, say for example, Software X. We denote the probability that a new user adopts Software X as $^ { \mathfrak { c } } a ^ { \mathfrak { n } }$ and a new user adopts Software Y as “b.” At any time t, the market share or user installation base (as a percentage of the total market size) of Software X is $X ( t )$ and of Software Y is Y(t). To account for positive network e<sup>f</sup>ects, we assume that the number of new users of any software platform is proportional to its user installation base at any time “t.” Therefore, the intrinsic growth rates of X and Y are de<sup>fi</sup>ned as follows:

$$
\left. \begin{array}{l} (\text { Intrinsic   Growth   Rate   of   the   Software   X }) = a X (t) \\ (\text { Intrinsic   Growth   Rate   of   the   Software   Y }) = b Y (t) \end{array} \right\}\tag{2a}
$$

## Restraining E<sup>f</sup>ect of the Maximum Market Potential

The growth rates of X and Y are adversely a<sup>f</sup>ected by a crowding efect. This crowding e<sup>f</sup>ect is the e<sup>f</sup>ect of the total potential user installation base of Software X and Software Y. The crowding e<sup>f</sup>ect results in a slower pace of adoption as the combined market share of the two competing software platforms moves closer to the maximum market potential. In fact, when the combined market share of the competing software platforms reaches the maximum market potential, the growth of both of the software platforms should be reduced to zero. This crowding e<sup>f</sup>ect is captured in the model as follows:

$$
\left. \begin{array}{l} (\text { Restraining   Effect   of } X (t) + Y (t) \text { on   growth   of } X) = a X (t) (X (t) + Y (t)) \\ (\text { Restraining   Effect   of } X (t) + Y (t) \text { on   growth   of } Y) = b Y (t) (X (t) + Y (t)) \end{array} \right\}\tag{2b}
$$

## Restraining E<sup>f</sup>ect of the Competing Software’s Market Share

The growth rates of the software platforms are adversely a<sup>f</sup>ected by the presence of competition. Since the two software platforms are competing for the same pool of potential software users, the market share of the competing software has a restraining e<sup>f</sup>ect, proportional to its own market share, on the growth rate of the competing software. If we denote the constant of proportionality (i.e. competition coeficient) as $^ { \alpha } { c } ^ { \gamma }$ for Software Y and $^ { \ast } d ^ { \ast }$ for Software X, then the restraining e<sup>f</sup>ect of Software Y on Software X is given by $[ c Y ( t ) ] X ( t )$ and the restraining e<sup>f</sup>ect of X on Y is given by $[ d X ( t ) ] Y ( t )$

$$
\left. \begin{array}{l} (\text {Restraining Effect of Y(t) on the growth of X}) = c X (t) Y (t) \\ (\text {Restraining Effect of X(t) on the growth of Y}) = d Y (t) X (t) \end{array} \right\}\tag{2c}
$$

Substituting Equations 2a, 2b, and 2c into Equation 2 gives us the rate of growth of X and Y:

$$
\left. \begin{array}{l} \frac {d X (t)}{d t} = [ \mathsf {a} - \mathsf {a} (X (t) + Y (t)) - \mathsf {c} Y (t) ] X (t) \\ \frac {d Y (t)}{d t} = [ \mathsf {b} - \mathsf {b} (X (t) + Y (t)) - \mathsf {d} X (t) ] Y (t) \end{array} \right\}\tag{2d}
$$

## Users Switching to or from Competition’s Software

Software users are known to bene<sup>fi</sup>t from network e<sup>f</sup>ects [8, 12, 15, 26]. Therefore, any switching behavior is assumed to be a consequence of positive network e<sup>f</sup>ects. We assume that the likelihood of a user switching to the competing software increases with the market share of the competing software. For example, as the market share of Software X increases, the probability of a user of Y switching to X increases. If the constant of proportionality of a current user switching (or switching coeficient) is assumed to be $s _ { I } > 0 ;$ where : $\boldsymbol { I } = \left( \boldsymbol { X } , \boldsymbol { Y } \right)$ then the market-share dependent probability of a user switching from X to Y is $s _ { X } Y ( t )$ and that of a user switching from Y to X is $s _ { Y } X ( t )$ . Therefore, the expected number of users switching from X to Y is $s _ { X } Y ( t ) X ( t )$ and from Y to X is $s _ { Y } X ( t ) Y ( t )$ , as captured in Equation 3.

$$
\left. \begin{array}{l} (\text { Rate   of   Switching   From   Software   X   to   Software   Y }) = s _ {X} Y (t) X (t) \\ (\text { Rate   of   Switching   From   Software   Y   to   Software   X }) = s _ {Y} X (t) Y (t) \end{array} \right\}\tag{3}
$$

Combining Equations (2d) and (3) gives us the expression for the rate of change in the market share of the two competing software platforms.

$$
\left. \begin{array}{l} \frac {d X (t)}{d t} = [ a (1 - X (t) - Y (t)) - c Y (t) + s Y (t) ] X (t) \\ \frac {d Y (t)}{d t} = [ b (1 - X (t) - Y (t)) - d X (t) - s X (t) ] Y (t) \end{array} \right\}\tag{4}
$$

Here, $s = s _ { Y } - s _ { X }$ , where $- \ 1 < s < 1$

## Restraining E<sup>f</sup>ect of Hackers

Malicious hackers could be individuals (e.g., Grey Hats, hactivists), organized groups (e.g., Lulz security, LulzRaft, the Hacker Encrypters, Team Appunity, Swagg Security, or other groups), loosely federated groups of like-minded individuals (e.g., Anonymous), or organized criminals. We model the impact of any of these forms of malicious hackers on the growth rate of competing software as follows. Z(t) represents the number of malicious hackers at any time “t.” We assume $^ { \alpha } e ^ { \gamma }$ to be the probability that the malicious hackers will successfully target Software X and $\ " f \cdot$ to be the probability that malicious hackers will successfully target Software Y. We will also call these probabilities the Restraining Coeficients due to their restraining e<sup>f</sup>ects on the growth of X and Y users, respectively. The value of these coe<sup>fi</sup>cients can be a<sup>f</sup>ected by factors such as the type of vulnerability being targeted, the complexity of the exploit needed to target the vulnerability, the skills set of the hacker, and the resources available to the hackers. We do not explicitly include these factors in the model, because we are interested in only modeling the expected number of malicious hackers actively targeting X and Y. The expected number of hackers targeting X at time t is then $e Z ( t )$ , while the expected number of hackers targeting Y is $f Z ( t )$

We assume that each successful malicious hack results in encouraging more individuals to become malicious hackers. For the sake of simplicity, we assume this conversion rate to be 1. Prior research has established that hacking attempts against a software product or platform appear proportional to the software’s installed user base [21]. Therefore, we assume that the success of each hack is proportional to the number of X and Y users (i.e., the growth in the total number of hackers at any time $\ " { } t \ " { }$ is proportional to X(t) and Y(t), respectively). Thus, the overall hacker growth rate at time t is the sum of $e Z ( t ) X ( t )$ and $f Z ( t ) Y ( t )$ . Furthermore, we assume malicious hackers will leave hacking with a probability of w. Therefore, the number of malicious hackers leaving hacking is $w Z ( t )$ . The overall growth rate of these hackers is then given as follows:

$$
\frac {d Z (t)}{d t} = [ e X (t) + f Y (t) - w ] Z (t)\tag{5}
$$

The restraining e<sup>f</sup>ect of malicious hackers on the overall market share growth rates of Software X and Software Y is proportional to the number of hackers targeting X and Y and the installation base of X and Y. For example, if more malicious hackers are targeting X, and X has a higher installation user base, then a relatively higher number of X users will be a<sup>f</sup>ected by these hacking attacks. Therefore, the market share growth of X will be restrained. The restraining e<sup>f</sup>ect of malicious hackers on X is $e X ( t ) Z ( t )$ and on Y is fY(t)Z(t). Substituting these values into Equation 4b gives the net rate of growth for X and Y in the presence of these hackers.

$$
\left. \begin{array}{l} \frac {d X (t)}{d t} = [ a [ 1 - (X (t) + Y (t)) ] - c Y (t) + s Y (t) - e Z (t) ] X (t) \\ \frac {d Y (t)}{d t} = [ b [ 1 - (X (t) + Y (t)) ] - d X (t) - s X (t) - f Z (t) ] Y (t) \end{array} \right\}\tag{6}
$$

The parameters used in Equations 5 and 6 are summarized in Table 1.

The set of equations (Equations 5 and 6) modeling the growth of Software X and Software Y in the presence of malicious hackers is given as follows:

Variables used in Equations 5 and 6.

<table><tr><td>Parameter</td><td>Meaning</td><td>Values</td></tr><tr><td>a</td><td>Intrinsic growth rate of X or the probability of adoption of Software X (i.e. total number of new users divided by total number of users in a unit time period) in the absence of competition and hackers.</td><td>0 &lt; a &lt; 1</td></tr><tr><td>b</td><td>Intrinsic growth rate of Y or the probability of adoption for Software Y (i.e. total number of new users divided by total number of users in a unit time period) in the absence of competition and hackers.</td><td>0 &lt; b &lt; 1</td></tr><tr><td>s</td><td>Switching Coefficient. s &lt; 0 implies Y is gaining net users due to switching; s &gt; 0 means that X is gaining net users due to switching; and s = 0 implies that neither X nor Y gain any additional users due to switching.</td><td>-1 &lt; s &lt; 1</td></tr><tr><td>c</td><td>Competition Coefficient for the restraining effect of Y on the growth of X</td><td>0 &lt; c &lt; 1</td></tr><tr><td>d</td><td>Competition Coefficient for the restraining effect of X on the growth of Y</td><td>0 &lt; d &lt; 1</td></tr><tr><td>e</td><td>Restraining Coefficient for the restraining effect of hackers on the growth of X</td><td>0 &lt; e &lt; 1</td></tr><tr><td>f</td><td>Restraining Coefficient for the restraining effect of hackers on the growth of Y</td><td>0 &lt; f &lt; 1</td></tr><tr><td>w</td><td>Probability of hackers going mainstream, i.e. becoming legitimate, consulting, becoming white hats, etc.</td><td>0 &lt; w &lt; 1</td></tr></table>

Notes: High Restraining Coe<sup>fi</sup>cient (i.e., e and f) implies poorly secured software. Hackers attack one or the other software, i.e., $\mathbf { e } + \mathbf { f } = 1$ . In any time period $\mathsf { X } ( \mathrm { t } ) + \mathsf { Y } ( \mathrm { t } ) \le 1$ . Therefore, in equilibrium ${ \sf X } + { \sf Y } = 1 .$

$$
\left. \begin{array}{l} \frac {d X}{d t} = [ a - a (X + Y) + s Y - c Y - e Z ] X \\ \frac {d Y}{d t} = [ b - b (X + Y) - s X - d X - f Z ] Y \\ \frac {d Z}{d t} = [ e X + f Y - w ] Z \end{array} \right\}.\tag{7}
$$

Notes: In Equation 7, we replace X(t), Y(t), and Z(t) with X, Y, and Z for simplicity and readability.

The complex system of equations presented in Equation 7 is intractable, that is, the equations do not yield general solutions. Thus, we next analyze this equation system by identifying the system’s equilibrium points and then performing a stability analysis of these equilibrium points.

## Model Analysis — Equilibrium Outcomes

To analyze the stability of the system, following Barnes and Fulford [5] of equations (Equation 7) near the equilibrium points, a linear model about the equilibrium point is used. The linearized model about an equilibrium point $\left( x _ { e } , y _ { e } , z _ { e } \right)$ is given as follows:

$$
\left\{ \begin{array}{c} \frac {d X}{d t} \\ \frac {d Y}{d t} \\ \frac {d Z}{d t} \end{array} \right\} = \left[ \begin{array}{c c c} a (1 - 2 x _ {e}) - (a + c - s) y _ {e} - e z _ {e} & - (a + c - s) x _ {e} & - e x _ {e} \\ - (a + d + s) y _ {e} & b (1 - 2 y _ {e}) - (b + d + s) x _ {e} - f z _ {e} & - f y _ {e} \\ e z _ {e} & f z _ {e} & e x _ {e} + f y _ {e} - w \end{array} \right] \left\{ \begin{array}{c} X - x _ {e} \\ Y - y _ {e} \\ Z - z _ {e} \end{array} \right\}\tag{8}
$$

We next analyze this linearized model (Equation 8) for three key scenarios: (a) when both software platforms are fully secure, that is, they are impervious and thus not targeted by hackers; (b) when only one software is secure, and thus only one software can be targeted by hackers; and (c) when neither of the software platforms are completely secure, and thus both are targeted by hackers.

## Scenario 1 (Benchmark): Both Fully Secured; Hackers Attack Neither Platform

The assumption that malicious hackers target neither software platform enables one to eliminate all terms pertaining to the restraining e<sup>f</sup>ect of hacker activity. The system of equations (see Equation 7) is thus reduced as follows:

$$
\left. \begin{array}{l} \frac {d X}{d t} = [ a - a (X + Y) + s Y - c Y ] X; \\ \frac {d Y}{d t} = [ b - b (X + Y) - s X - d X ] Y \end{array} \right\}\tag{9}
$$

Solving the set of equations in Equation 9, we identify four equilibrium solutions in this scenario:

Equilibrium 1 is $( x _ { e } , y _ { e } ) = ( 0 , 0 )$ ;

Equilibrium 2 is $\left( x _ { e } , y _ { e } \right) = \left( 1 , 0 \right)$ (i.e. monopoly of Software X);

Equilibrium 3 is $( x _ { e } , y _ { e } ) = ( 0 , 1 )$ (i.e. monopoly of Software Y);

Equilibrium 4 is $\begin{array} { r } { ( x _ { e } , y _ { e } ) = \left( \frac { b ( c - s ) } { a ( d + s ) + [ b + ( d + s ) ] ( c - s ) } , \frac { \circ } { [ a + ( c - s ) ] ( d + s ) + b ( c - s ) } \right) } \end{array}$ (i.e. competitive market).

The reduced linear model for this system (from Equation 8) is then given as:

$$
\left\{ \begin{array}{c} \frac {d X}{d t} \\ \frac {d Y}{d t} \end{array} \right\} = \left[ \begin{array}{c c} a (1 - 2 x _ {e}) - (a + c - s) y _ {e} & - (a + c - s) x _ {e} \\ - (b + d + s) y _ {e} & b (1 - 2 y _ {e}) - (b + d + s) x _ {e} \end{array} \right] \left\{ \begin{array}{c} X - x _ {e} \\ Y - y _ {e} \end{array} \right\}
$$

The stability of the equilibrium values is analyzed in Appendix A. The results are summarized in Table 2. As one can see from the stability analysis, the long-term stable equilibriums result in a monopoly market (Equilibrium 2 or 3). From Table 2, we also notice that if the amount of user switching to one software platform overcomes the restraining e<sup>f</sup>ect of the competitor $( s > c { \mathrm { ~ o r ~ } } s < - d )$ , then the competitor cannot have a monopoly. Otherwise $( \mathrm { ~ - ~ } d < s < c )$ , the initial market share will dictate the monopoly outcome. Given a market share of each software platform at the initial condition (say, Y 0 ), there is a particular tipping market share point for software X<sub>ð</sub> <sub>Þ</sub>0 either to win and monopolize the market, or to get obliterated. The only equilibrium in which both of the software platforms can co-exist in the market is Equilibrium 4. However, this equilibrium is unstable and therefore unsustainable mainly due to the destabilizing restraining factors from the competitor software.

This result should not be surprising. Existing literature on software competition has investigated these issues at length. For example, in markets with a network e<sup>f</sup>ect and incompatible software platforms (as is the case in this study), there is a natural tendency towards de facto standardization, which means that everyone tends to use the same software platform [26]. This resulting monopoly can be explained by “tipping,” which is the tendency of one system to gain substantial market share relative to its competition once it has gained an initial edge.

For example, simulation of this equation system (Figure 1) with parameters $( a = 0 . 3 6 ,$ $b = 0 . 3 6 , \ c = 0 . 6 4 , \ d = 0 . 1 9 , \ s = 0 . 4 5 )$ and initial market share $Y ( 0 ) = 0 . 8 6$ results in a tipping value of 0.25 for X(0). In static competition models, this tipping phenomenon is re<sup>fl</sup>ected in equilibria in which a single system dominates [26]. In dynamic competition models, tipping is re<sup>fl</sup>ected in equilibria where adoption of the losing system simply stops once a rival system is introduced or accepted in the marketplace [15, 26]. Consumer heterogeneity and product di<sup>f</sup>erentiation tend to limit this tipping phenomenon and to sustain multiple networks. If the rival systems have distinct features sought by certain consumers, two or more systems may be able to survive by catering to consumers who care more about product attributes rather than about network size. In this situation, market equilibrium with multiple incompatible products re<sup>fl</sup>ects the social value of variety. However, in our case, we assume the competing software platforms o<sup>f</sup>er similar functionality, features, and usability to the users. As a result, in the absence of malicious hackers, monopoly is the most likely long-term equilibrium outcome in the market.

Equilibrium values when both Software X and Software Y are secure.

<table><tr><td>Condition</td><td>Equilibrium 1</td><td>Equilibrium 2</td><td>Equilibrium 3</td><td>Equilibrium 4</td></tr><tr><td> $s < -d$ </td><td>Unstable</td><td>Unstable</td><td>Stable</td><td>Unstable</td></tr><tr><td> $-d < s < c$ </td><td>Unstable</td><td>Stable</td><td>Stable</td><td>Unstable</td></tr><tr><td> $c < s$ </td><td>Unstable</td><td>Stable</td><td>Unstable</td><td>Unstable</td></tr></table>

![](/api/attachments/JSEK4FBC/fulltext/images/ad3919048d0e1074215ce428912511d130fc302a9c585cd3e06913bbf73e96f3.jpg)  
(a) Example 1: $X ( \mathrm { { o } ) < ^ { \mathfrak { s } } \mathrm { { t i p p i n g } } }$ point (0.25)"

![](/api/attachments/JSEK4FBC/fulltext/images/1b390a7702cea5da3dae56b59f338d3888fa440e1f8c1e0f4f31d50e8f9e46f9.jpg)  
(b) Example 2: $X ( 0 ) { > } 0 . 2 5 ^ { \circ }$ ‘tipping point (0.25)"  
Initial market edge e<sup>f</sup>ect when switching not enough to overcome competition.

## Scenario 2: One Software Is Targeted by Hackers

The assumption that malicious hackers will only target one software platform eliminates from (Equation 7) the hacking activity terms for one of the software platforms. Without loss of generality, we assume X is targeted by the hackers. Hence, we assume that $e = 1 , f = 0$ , which gives the following reduced set of equations (see Equation 7):

$$
\left. \begin{array}{l} \frac {d X}{d t} = [ a - a (X + Y) + s Y - c Y - Z ] X \\ \frac {d Y}{d t} = [ b - b (X + Y) - s X - d X ] Y \\ \frac {d Z}{d t} = [ X - w ] Z. \end{array} \right\}\tag{10}
$$

The linear model for this system (from Equation 8) is now given as:

$$
\left\{ \begin{array}{c} \frac {d X}{d t} \\ \frac {d Y}{d t} \\ \frac {d Z}{d t} \end{array} \right\} = \left[ \begin{array}{c c c} a (1 - 2 x _ {e}) - (a + c - s) y _ {e} - z _ {e} & - (a + c - s) x _ {e} & - x _ {e} \\ - (a + d + s) y _ {e} & b (1 - 2 y _ {e}) - (b + d + s) x _ {e} & 0 \\ z _ {e} & 0 & x _ {e} - w \end{array} \right] \left\{ \begin{array}{c} X - x _ {e} \\ Y - y _ {e} \\ Z - z _ {e} \end{array} \right\}
$$

Scenario 2 has six equilibrium points, where four of the equilibrium points are shared with Scenario 1 (with hacker state at zero). However, the malicious hackers’ activities in<sup>fl</sup>uence the stability of some of the common equilibrium points. The equilibrium values for the Scenario 2 system of equations (Equation 10) now are as follows.

Equilibrium 1 is $( x _ { e } , y _ { e } , z _ { e } ) = ( 0 , 0 , 0 )$ ;

Equilibrium 2 is $( x _ { e } , y _ { e } , z _ { e } ) = ( 1 , 0 , 0 )$ ; (i.e. monopoly of Software X)

Equilibrium 3 is $( x _ { e } , y _ { e } , z _ { e } ) = ( 0 , 1 , 0 ) ;$ ; (i.e. monopoly of Software Y)

Equilibrium 4 is $\begin{array} { r } { ( x _ { e } , y _ { e } , z _ { e } ) = \left( \frac { b ( c - s ) } { a ( d + s ) + [ b + ( d + s ) ] ( c - s ) } , \frac { a ( d + s ) } { [ a + ( c - s ) ] ( d + s ) + b ( c - s ) } , 0 \right) } \end{array}$ ; (i.e. a competitive market consisting of both X & Y)

Equilibrium 5 is $( x _ { e } , y _ { e } , z _ { e } ) = ( w , 0 , a ( 1 - w ) )$ ; (i.e., monopoly of Software X, with hackers targeting X)

Equilibrium 6 is $\begin{array} { r } { ( x _ { e } , y _ { e } , z _ { e } ) = \Big ( w , ~ \frac { w } { b } ( \delta - s ) , ~ - ( 1 - w ) ( c - s ) + \frac { w ( a + c - s ) ( d + s ) } { b } \Big ) } \end{array}$ (i.e., a competitive market consisting of both X & Y, with hackers targeting X)

We examine the stability of the above equilibrium values in Appendix B. Based on this stability analysis, we observe that the stability of the <sup>fi</sup>rst <sup>fi</sup>ve equilibrium points is determined by the value of the switching constants $^ { \mathfrak { a } } { } _ { \mathcal { S } } ^ { \mathfrak { n } }$ relative to two factors: the restraining factor c of software Y on the growth of $X ;$ and the modi<sup>fi</sup>ed growth δ of software Y in the presence of malicious hackers, where δ is de<sup>fi</sup>ned as $\begin{array} { r } { \delta = \left[ b ( \frac { 1 } { w } - 1 ) - d \right] } \end{array}$

Analysis of equilibrium values when only Software X is targeted by hackers.

<table><tr><td rowspan="2">When s&gt;δ</td><td colspan="6">Equilibrium</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Case 1 c&lt; s</td><td>Unstable</td><td>Unstable</td><td>Unstable</td><td>Unstable</td><td>Stable</td><td>Infeasible</td></tr><tr><td>Case 2 c&gt;s</td><td>Unstable</td><td>Unstable</td><td>Stable</td><td>Unstable</td><td>Stable</td><td>Infeasible</td></tr></table>

Note: $\begin{array} { r } { \delta = \left[ b ( \frac { 1 } { w } - 1 ) - d \right] } \end{array}$

Analysis of equilibrium values when only Software X is Targeted by hacker.

<table><tr><td rowspan="2">When  $s < \delta$ </td><td colspan="6">Equilibrium</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Case 3  $c < s$ </td><td>Unstable</td><td>Unstable</td><td>Unstable</td><td>Unstable</td><td>Unstable</td><td>Stable/Unstable</td></tr><tr><td>Case 4  $c >s$ </td><td>Unstable</td><td>Unstable</td><td>Stable</td><td>Unstable</td><td>Unstable</td><td>Stable/Unstable</td></tr></table>

Notes: δ <sub>¼</sub> b <sup>1</sup><sub>w -</sub> 1   <sub>-</sub> d  .

Note that δ is inversely correlated to the restraining e<sup>f</sup>ect of X on the growth of Y (i.e. d) and the rate at which malicious hackers leave the market (i.e. w). Since the two factors (i.e. c and δ) are independent, the analysis of various equilibriums can be divided into two major groups: (1) s > δ; and $( 2 ) s < \delta .$ . The results for both groups are summarized in Table 3 and Table 4. We <sup>fi</sup>rst analyze the two cases in Table 3, followed by the analysis of Case 3 and Case 4 provided in Table 4.

## Case 1 (Table 3)

Unlike with Scenario 1, which was de<sup>fi</sup>ned by a complete monopoly of X (X has all the market to itself), in this scenario, Equilibrium 2 has become unsustainable for all conditions. This outcome is the direct result of the hackers’ activity and the vulnerability of the platform X. Instead, we have Equilibrium 5 (i.e., monopoly of the unsecure software X) but with market share less than the maximum potential market size that is sustainable (see Case 1 in Table 3). This equilibrium is the only stable equilibrium when the switching rate (from Y to X) is greater than the modi<sup>fi</sup>ed growth rate of software Y (s > δ) and the restraining e<sup>f</sup>ect of Y on the growth of X is less than the switching rate from Y to X (c < s). What this means is that (a) users are leaving Y and moving to X at a higher rate than new users are joining Y, and (b) Y’s restraining e<sup>f</sup>ect on the growth of X is not strong enough to overcome the number of users of Y switching to X. In short, software X has a higher intrinsic growth rate and is attracting more users from software Y than the other way around. As a result, software X tends to end up in a monopoly market state (in the long run) despite being an unsecure software platform. Note that, in this case, it does not matter whether software X is an early or late entrant.

This outcome was exempli<sup>fi</sup>ed by the dominance of the Windows OS against its rival Apple in the desktop operating systems market in the 1990s. MS Windows was perceived to be the less secure of the two operating systems. As per our results, the other determinant of this outcome is the relationship between Apple’s restraining e<sup>f</sup>ect on the growth of the Windows OS and the rate at which users switched from Apple to the Windows OS. The equilibrium in which the Windows OS dominates the market is feasible and stable irrespective of the aforementioned relationship. If we assume that Apple’s restraining e<sup>f</sup>ect on the growth of the Windows OS was less than the rate at which users switched from Apple to the Windows OS, then Equilibrium 5 in Case 1 (Table 3) represents the outcome. On the other hand, if we assume that Apple’s restraining e<sup>f</sup>ect on the growth of the Windows OS was more than the rate at which users switched from Apple to the Windows OS, then Equilibrium 5 in Case 2 (Table 3) again represents the outcome. This leads us to the discussion of Case 2.

## Case 2 (Table 3)

In this case, software Y (the secure software platform) can have a monopoly (i.e., Equilibrium 3). Just like in Scenario 1, the stability of this equilibrium, in which there is a monopoly of Y (Equilibrium 3), depends upon the restraining e<sup>f</sup>ect of software Y on the growth of software X being more dominant than any switching e<sup>f</sup>ect from Y to $X \ ( c > s )$ . Simply put, Y is able to curtail the growth of X despite some users switching from Y to X. Note that in this case, there is another feasible and stable equilibrium, that is, Equilibrium 5 (Table 3). As per our analysis, both Equilibrium 3 and Equilibrium 5 are stable and exhibit the “tipping” phenomenon based on the relative initial market share. Figure 2 shows simulation results for various initial market conditions, with a set of system parameters given as: (a = 0.33, b = 0.9, c = 0.4, d = 0.23, s = 0.317, e = 1, f = 0, w = 0.828, δ= −0.04).

Figure 2a shows Example 1, where unsecure Software X dominates the market with more users switching from Software Y to Software X in spite of X being a late entrant. However, the dynamics of hackers’ activities ultimately resulted in X losing some market share and <sup>fi</sup>nally stabilizing at Equilibrium 5. The results in Figure 2a show that a slow buildup of hackers’ activities allowed software X to reach and capture the whole market for some duration (Equilibrium 2) before stabilizing at Equilibrium 5. In Figure 2b, the high initial market share of software X encourages early hacker activities to build up, resulting in reaching the equilibrium quicker. In both simulations, Software Y does not survive, whereas Software X dominates the market.

What is interesting to note about these results is that the non-secure software (i.e., X) is the one that is more likely to dominate the market in the long run, whereas the secure software is driven out of the market in the long run. This long-run result holds even when the secure software (i.e., Y) initially has more market share than the unsecure software (i.e., X) at t = 0 (see Figure 2-Example 1). This outcome is due to the result of a positive value of the switching parameter (i.e., s). What could justify the high switching rate from Y to X despite X being less secure? Anderson [4] suggests one reason could be the lack of knowledge on the part of the software users about quality security aspects (e.g. security) of X and Y. Furthermore, under such conditions of information asymmetry, developers of software X have a minimal incentive to spend resources on making more secure software. Despite this, software X can become the dominant software platform by focusing on marketing and promotional activities that encourage the users of Y to switch to X. The result suggests that given a choice between investing in developing more secure software, or investing in marketing campaigns to encourage users of the competing software to switch, the software vendor would be better o<sup>f</sup> by doing the latter. However, early entry of software Y and a relatively large initial market share will allow software Y to overcome the switching factor and monopolize the market (Equilibrium 3 as shown in Figure 2c.).

![](/api/attachments/JSEK4FBC/fulltext/images/f7f335634cb105ac99cf6695150912b4e05e2fd7269d4b4be6411f284b7803d8.jpg)  
(a) Example 1: Slow  
convergence to Equilibrium 5

![](/api/attachments/JSEK4FBC/fulltext/images/8343d077de03f7f6a2819c05e53e2993c54778218091fffdc4ec2039c7f48997.jpg)  
(b) Example 2: Quick  
convergence to Equilibrium 5

![](/api/attachments/JSEK4FBC/fulltext/images/e1ff8d6808bf7df8c89bd2b171b7ad5acd53a7eeac3c5d8414dc68c59d7c7e75.jpg)  
(c) Example 3: Convergence to mple 3: Conve  
Stable equilibrium 3 and 5 for $\begin{array} { r } { s > \delta , } \end{array}$ $c > s$ (Case 2 in Table 3).

## Case 3 (Table 4)

In this case, while the rate at which users switch from Y to X is less than the modi<sup>fi</sup>ed growth rate of Y $( \mathrm { i } . \mathrm { e } . , s < \delta )$ , the restraining e<sup>f</sup>ect of Y on the growth of X is also relatively weak (i.e., c < s). In contrast, for Equilibrium 6, where two competing software platforms co-existing in an equilibrium is feasible, the equilibrium’s stability is governed by various parameter values. If stable, Equilibrium 6 is the only equilibrium in this scenario where the hacker’s activity results in the software market being shared by both competing software platforms in a steady state. If unstable, then the hacker activity results in an alternative dynamic state where the two software platforms coexist together, however their market share is always in <sup>fl</sup>ux. Figure 3 shows two examples of market share and market dynamics phase plots for both situations, using the following market parameters:

Example 1: a = 0.32, b = 0.5, c = 0.4, d = 0.06, s = 0.437, e = 1, f = 0, w = 0.4

Example 2: a = 0.32, b = 0.57, c = 0.4, d = 0.06, s = 0.437, e = 1, f = 0, w = 0.33

Example 1 in Figure 3 shows a case where market dynamics converge and ultimately stabilize at the Equilibrium 6, irrespective of the entry point or initial market share of the two software platforms.

The rate of hackers going to main stream w has a direct impact on the <sup>fi</sup>nal market share of software X. The more the hackers stay, the less will be the share of market for software X. This outcome makes sense since the hackers are only targeting X. On the other hand, the market share of the secure software Y depends on its intrinsic growth (i.e., b). In Example 2 in Figure 3, where no feasible equilibrium exists, the market enters into a stable limit cycle irrespective of market entry point for the two software platforms. To break out of this cycle, X and Y will have to take steps such as investing in marketing and promotion to in<sup>fl</sup>uence their intrinsic growth rates, discourage users from switching to the competition, and encourage hackers to become mainstream stakeholders in the software market (e.g., security consultants, vulnerability researchers).

![](/api/attachments/JSEK4FBC/fulltext/images/d005ce839b6cb1b113150cd3b20733bbd45ce39a0ff973243abd5adb6b8145a5.jpg)

![](/api/attachments/JSEK4FBC/fulltext/images/51a677c23a5d6baf212232b9277daaa0658010a39162ae4483dffff9fcdfe2b4.jpg)

![](/api/attachments/JSEK4FBC/fulltext/images/90ede79d5854b72d2acacdf2fc98896c20d526d722b1a48bd516ffab1c577391.jpg)

![](/api/attachments/JSEK4FBC/fulltext/images/655cae7434b76c2cfbce89f212b0859757637380a6e3cf9162877e83bb8adbf7.jpg)  
Solution converging to stable Equilibrium 6 (market share on the vertical axis).

## Case 4 (Table 4)

In Case 3, the unsecure software’s (i.e., X) existence was supported through its ability to steal users through switching from the other software (i.e., Y). If the switching support to software X is further reduced, for example through aggressive marketing by software Y, $( \mathrm { i } . \mathrm { e } . , \delta { > } s , c { > } s )$ , the existence of X becomes tenuous. However, hacking activity makes it possible that the two software platforms still can coexist. In this case, there are two possible situations: (a) only Equilibrium 3 (i.e., monopoly of Y) is stable; and (b) both Equilibriums 3 and 6 are stable. As in Case 3, the unsecure software can survive in both situations, but unlike in Case 3 its survival is not guaranteed as it depends upon a favorable entry point and limited hacking activity. Figure 4 and Figure 5 show di<sup>f</sup>erent examples of market outcome for the two situations de<sup>fi</sup>ned by the following model parameters:

Situation $4 ; a = 0 . 3 3 , b = 0 . 5 4 , c = 0 . 4 , d = 0 . 3 4 , s = 0 . 3 5 7 , e = l , f = 0 , w = 0 . 2 9 5 8 6 )$

Situation B: $a = 0 . 3 3 , b = 0 . 5 4 , c = 0 . 4 , d = 0 . 3 4 , s = 0 . 3 5 7 , e = 1 , f = 0 , w = 0 . 3 7 5 8 6$

Figure 4 demonstrates three examples for Situation A. Example 1 shows unsecure software X surviving and competing with Y. However, higher hacker activity (Example 2 in Figure 4) or little unfavorable initial market share (Example 3 in Figure 4) results in

![](/api/attachments/JSEK4FBC/fulltext/images/a9491337e6e00b3f923bee4bb891ea77f7ddc03dbfc738881d64925a69b6852f.jpg)  
Case 4 (situation A) – one stable equilibrium. Outcome is shaped by initial entry point and hackers activity.

X being forced out of the market, and Y (the secure software) remains as a monopoly. That is, only Equilibrium 3 is feasible and stable in Situation A.

Figure 5 demonstrates Situation B with two examples. The initial market shares of X and Y, and the level of hacker activity, dictate where the market dynamics converge and which software platform dominates the market. In Example 1, both X and Y coexist in the market (i.e., Equilibrium 6), while in Example 2, Y ends up monopolizing the market in the long run (i.e., Equilibrium 3).

## Scenario 3: Both X and Y Are Attacked by Hackers

Next, we consider what happens if both software X and software Y are attacked by hackers. The set of equations representing this scenario is shown in Equation 11:

$$
\begin{array}{r} \frac {d X}{d t} = [ a - a X - a Y - s Y - c Y - e Z ] X \\ \frac {d Y}{d t} = [ b - b X - b Y + s X - d X - f Z ] Y \\ \frac {d Z}{d t} = [ e X + f Y - w ] Z \end{array}\tag{11}
$$

The linear model for this system (from Equation 8) is given as:

Market Dynamics (Phase Plot)  
![](/api/attachments/JSEK4FBC/fulltext/images/d4f670fa82dfaa0bafd598ddba719ddc4d50e16fffd17ac256af05f604bcad0d.jpg)

![](/api/attachments/JSEK4FBC/fulltext/images/3fbae4ddcec9b736f4305d3529820af49f9852694a3b8142b8e6762de9eb4f90.jpg)

![](/api/attachments/JSEK4FBC/fulltext/images/287ca2f57a6fdd7108ceff0687927912fa83cf969c6c6bbe5a86e8440d9218c6.jpg)

![](/api/attachments/JSEK4FBC/fulltext/images/eb9a12bdfaaa7f1230442acfe492b8970497e89f421e4255f8895ba7e237722e.jpg)  
Case 4 (situation B) – Two stable equilibrium. Outcome is shaped by initial entry point and <sup>Figure 5.</sup>hackers activity.

$$
\left\{ \begin{array}{c} \frac {d X}{d t} \\ \frac {d Y}{d t} \\ \frac {d Z}{d t} \end{array} \right\} = \left[ \begin{array}{c c c} a (1 - 2 x _ {e}) - (a + c - s) y _ {e} - e z _ {e} & - (a + c - s) x _ {e} & - e x _ {e} \\ - (a + d + s) y _ {e} & b (1 - 2 y _ {e}) - (b + d + s) x _ {e} & f y _ {e} \\ e z _ {0} & f z _ {0} & e x _ {e} + f y _ {e} - w \end{array} \right] \left\{ \begin{array}{c} X - x _ {e} \\ Y - y _ {e} \\ Z - z _ {e} \end{array} \right\}
$$

The equilibrium values for the system of equations (11) are as follows:

Equilibrium 1: $( x _ { e } , y _ { e } , z _ { e } ) = ( 0 , 0 , 0 )$ ;

Equilibrium 2: $( x _ { e } , y _ { e } , z _ { e } ) = ( 1 , 0 , 0 )$ ; (i.e., monopoly of Software X)

Equilibrium 3: $( x _ { e } , y _ { e } , z _ { e } ) = ( 0 , 1 , 0 ) ; ( \mathrm { i . e . }$ , monopoly of Software Y)

Equilibrium 4: $\begin{array} { r } { ( x _ { e } , y _ { e } , z _ { e } ) = \left( \frac { - b ( c - s ) } { a b - ( a + c - s ) ( b + d + s ) } , \frac { - a ( d + s ) } { a b - ( a + c - s ) ( b + d + s ) } , 0 \right) } \end{array}$ ; (i.e., a competitive market consisting of both $X \ \& \ Y )$

Equilibrium $\begin{array} { r } { 5 \colon ( x _ { e } , y _ { e } , z _ { e } ) = \mathopen { } \mathclose \bgroup \left( \frac { w } { e } , 0 , \frac { a ( e - w ) } { e ^ { 2 } } \aftergroup \egroup \right) } \end{array}$ ; (i.e., monopoly of Software X, and the hackers target both X & Y)

Equilibrium 6: $\begin{array} { r } { ( x _ { e } , y _ { e } , z _ { e } ) = \left( \begin{array} { l } { \frac { a f ^ { 2 } + b e [ w - f ] + f w [ s - c ] } { e ( b e - c f ) + f ( a f - d e ) } , \frac { b e ^ { 2 } + a f [ w - f ] - e w [ s + d ] } { e ( b e - c f ) + f ( a f - d e ) } , } \\ { \frac { w s ^ { 2 } + b e ( a - c ) + a f ( b - d ) + d w ( c - s ) + s ( b e - a f ) + w ( c s - a b ) } { e ( b e - c f ) + f ( a f - d e ) } } \end{array} \right) } \end{array}$

(i.e. a competitive market consisting of both X & Y, and the hackers target both X & Y)

Equilibrium 7: $\begin{array} { r } { ( x _ { e } , y _ { e } , z _ { e } ) = \left( 0 , \frac { w } { f } , \frac { b ( f - w ) } { f ^ { 2 } } \right) ( \mathrm { i . e . } } \end{array}$ , monopoly of Software Y, and the hackers target both X & Y)

This setup represents the most general market scenario. Just as where the vulnerability of Software X results in making Equilibrium 2 always unstable, the simultaneous vulnerability of Software Y makes Equilibrium 3 always unstable in this scenario. As the model suggests, the basic nature of the various equilibrium points remains similar to those equilibria obtained in Scenario 1 and Scenario 2. This observation is not surprising since these scenarios are special cases of Scenario 3. For example, in Scenario 2 we saw that the unsecure software X introduced an equilibrium point (i.e., Equilibrium 5 in Scenario 2) corresponding to a case of market monopoly without fully capturing the full market share. In this most general scenario, a similar equilibrium point is expected for Y and is de<sup>fi</sup>ned by Equilibrium 7. However, the simultaneous presence of the restraining e<sup>f</sup>ect of hackers for both software platforms slightly modi<sup>fi</sup>es Equilibrium 5 (and its counterpart Equilibrium 7) from Scenario 2. The restraining parameters (“e” and “f “) also modify Equilibrium 6, which remains the most interesting equilibrium, as it can be a feasible and stable equilibrium with both of the software platforms co-existing. Thus, in this scenario, we expect similar situations.

In this most general case represented by Scenario 3, the <sup>fi</sup>rst four equilibrium points are unstable. All of the parameters that de<sup>fi</sup>ne the software market a<sup>f</sup>ect the dynamics of the market near the last three equilibrium points (Equilibriums 5 to 7), making the corresponding eigenvalues complex functions of these parameters. Thus, the stability of these equilibrium points varies based on the values of the system parameters. Furthermore, not all equilibriums are always feasible, as the equilibrium point may move outside of the scope of variables. As a result, it is di<sup>fi</sup>cult to de<sup>fi</sup>ne the scope of parameters for the feasibility and stability of these equilibriums using an analytical approach. Therefore, we use a numerical approach [5] to test the stability, by using three examples corresponding to di<sup>f</sup>erent values of the parameters (see Appendix C). The results are summarized in Table 5.

Equilibrium 6 Feasible and Stable at Parameter Values: Example 1: $a \ = \ 0 . 3 3 , \ b \ =$ 0.44828, c = 0.4, d = 0.23, s = -0.37931, e = 0.11, f = 0.89, w = 0.1669 (See Appendix C, Figure C1).

Table 4 shows that when hackers target both X and Y, a competitive software market (i.e., Equilibrium 6 in which both X and Y have positive market share) is both feasible and stable, under certain conditions. For this competitive market to evolve as the equilibrium, the software market should be characterized as follows. The probability of a user choosing X (Y) is less than that of choosing Y (X), more X (Y) users are switching to Y (X) than vice versa, and the likelihood of a hacker targeting Y (X) is signi<sup>fi</sup>cantly greater than that of targeting X (Y). While we don’t have empirical data to test these conditions, we do have anecdotal evidence for such a market. These conditions are present in the mobile operating systems market. According to a 2017 Gartner report, Android and iOS, together, account for more than 99 percent of the market share.<sup>5</sup> So this market closely resembles the one modeled in this study. Furthermore, we will represent iOS with X and Android with Y. Android is available on more mobile devices than iOS and Android based products come in a wider price range than iOS based products. Therefore, it is reasonable to assume that the probability of a user choosing X (iOS) is less than that of choosing Y (Android). A search for vulnerabilities in iOS and Android in the National Vulnerability database (NVD)<sup>6</sup> shows that between January 2006 and April 2018, 2587 vulnerabilities were discovered in iOS, and 4676 vulnerabilities were discovered in Android. According to Kaspersky Lab, vulnerabilities are frequently exploited in successful cyberattacks (Kaspersky Lab 2017).<sup>7</sup> Also, since the Android platform is more open compared to iOS, it is slightly more vulnerable to hacks and cyber threats. Therefore, it is safe to assume that hackers are more likely to target Android (Y) than iOS (X). If we use loyalty of the software’s users as a surrogate measure for their likelihood to switch to the competing platform, then some trade publications suggest that Android (Y) users are more loyal than iOS (X) users.<sup>8,9</sup> Therefore, it is safe to assume that more iOS (Y) users are switching to Android (X) than vice versa. As a result, both Android and iOS still exist in the mobile marketplace. Figure 6 shows the US market shares of Android and iOS.

Analysis of equilibrium values when both X & Y are targeted by hackers.

<table><tr><td rowspan="2"></td><td colspan="2">Example 1</td><td colspan="2">Example 2</td><td colspan="2">Example 3</td></tr><tr><td>Feasible</td><td>Stable</td><td>Feasible</td><td>Stable</td><td>Feasible</td><td>Stable</td></tr><tr><td>Equilibrium 1</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Equilibrium 2</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Equilibrium 3</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Equilibrium 4</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Equilibrium 5</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Equilibrium 6*</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Equilibrium 7</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr></table>

Notes: Equilibrium in which the market is shared between competing software. The bold text represents scenarios where the equilibrium is both Feasible & Stable.

Interestingly, if we modify the parameter capturing hacker attacks on iOS and Android and assume that instead of Android being more at risk than iOS, both face the same or approximately the same risk from hackers, then Android is more likely to emerge as the dominant player in the mobile operating systems market. This trend is already evident in the global market for mobile operating systems, as demonstrated by the outcome in Figure 7.

## Conclusion

Attacks by malicious hackers on technological systems are an ongoing managerial challenge. As such, these malicious hackers have become an integral part of the software ecosystem that also consists of software developers and users. Prior research largely focuses on low-level drivers of technology bugs, related malicious hacker exploits, and protection against or remediation of their impacts. However, no research investigates the higher-level strategic impact of the presence of malicious hackers and their activities on the long-term structure of markets for software products, systems, and platforms. This study <sup>fi</sup>lls this gap, by studying whether the presence of malicious hackers within software markets is necessarily a bad thing.

We model a software market to examine the impact of malicious hacker attacks as a restraining e<sup>f</sup>ect on the targeted software’s rate of change in market share. We incorporate factors related to network e<sup>f</sup>ects and consumer switching between competing software platforms. We investigate the competition in this software market both in the absence of, and in the presence of, malicious hacker activities. Using numerical analysis and simulation, we <sup>fi</sup>nd that in many situations, the malicious hacker activities make it possible for multiple competing platforms to co-exist together.

We <sup>fi</sup>nd that in the absence of malicious hacker activities, a software market is more likely to become a monopoly in the long term. When malicious hackers are present and they predominantly target only one of the competing platforms, the market is again more likely to end up a monopoly in theory. In practice, we have the example of MS Windows dominating the market for desktop operating systems in the 1990s, even when it was the platform most frequently targeted by malicious hackers. In this scenario, a market consisting of both competing software platforms is feasible and stable. However, the stability of this market structure depends on the number of users switching from one software to another software, and the number of active malicious hackers targeting one of the competing software platforms. When the malicious hackers target both of the competing software platforms, their activity introduces a new co-existing equilibrium (i.e., Equilibrium 6) and modi<sup>fi</sup>ed monopoly equilibriums (i.e., Equilibriums 5 and 7) that result in various complex market dynamics. We observe that, due to the hackers’ presence, the two competing software platforms can coexist: (a) in a stable state at Equilibrium 6 irrespective of entry point and initial conditions (e.g., the market for mobile operating systems); (b) in stable cyclic or market <sup>fl</sup>ux conditions irrespective of entry point and initial conditions; (c) in an entry point and initial conditions dependent stable state at Equilibrium 6 — where unfavorable initial conditions can tip the market towards monopoly equilibriums (Equilibrium 5 and 7); and (d) in an entry point and initial conditions dependent cyclic or <sup>fl</sup>ux state – where the unfavorable initial conditions can tip the market toward monopoly equilibriums (Equilibriums 5 and 7).

![](/api/attachments/JSEK4FBC/fulltext/images/fb37556d96099879bbde66c947fdb8386ea3649e1b0ca233bb9f9d7605e1c72f.jpg)  
Subscriber share held by smartphone OS in the United States 2012-2018 (https://www.statista.com).<sup>10</sup>

![](/api/attachments/JSEK4FBC/fulltext/images/2235bd780975f7a0339813daba40c0bdbb6646297d9b61edc2097d6d07f8bec2.jpg)  
Subscriber share held by smartphone OS in the United States 2012-2018 (generated from Statista at https://www.statista.com).

## Contributions and Policy Implications

The theoretical, managerial, and policy implications of our results are as follows. First, the results add to our understanding of competition in software markets. The <sup>fi</sup>ndings illustrate the important, even though unintended, consequence of the presence of malicious hackers in the software ecosystem. That is, malicious hackers can foster competition among software vendors. Second, given these theoretical implications, managers can take into account the presence of malicious hackers in their markets, while making policies regarding software development and technology management investment decisions. For example, in a case where malicious hackers target only one of two competing software platforms, the software targeted can still end up monopolizing the market as long as its vendor invests su<sup>fi</sup>ciently in campaigns that encourage more users to switch to using the non-secure software. Third, from a regulatory policy perspective, the results should encourage a balanced debate regarding the pros and cons of malicious hacker activities.

The common public policy opinion is that malicious hackers are only bad for the software industry ecosystem and software markets. Yet, there are some hacker advocates, particularly in the open source community, who believe hackers often do more good than harm, by drawing our attention to security <sup>fl</sup>aws in popular software. This study illustrates another (albeit unintended) bene<sup>fi</sup>t of hacker activities. The study <sup>fi</sup>ndings show that by encouraging competition among software vendors, the hackers provide software platform users with more choices, and therefore any other bene<sup>fi</sup>ts associated with more choices in the marketplace. Therefore, before making ad hoc policy, such as making all hacker activities completely illegal, a more calibrated approach may be needed.

What should government policy do? The study results showing the unintended bene<sup>fi</sup>t of malicious hacking should not be taken as support for all such activities. Some hacker activities can be classi<sup>fi</sup>ed as malicious (e.g., because the target user has not given the hacker permission to engage in such activity) but harmless. For example, the intentions of the malicious hacker could be taken into account in any law, and if it can be proved that the intentions are to cause harm (e.g., identify theft, data breach, and <sup>fi</sup>nancial fraud), then legal rami<sup>fi</sup>cations should be more severe. However, hacking activities that do not result in harm to individuals, organizations, and nations should be treated less severely. For example, activities of hackers, commonly referred to as Grey Hats, that is, those hackers who discover vulnerabilities in a system without the owner’s permission or knowledge, and then report their <sup>fi</sup>ndings to the owner, vendor of the vulnerable software/system, bug bounty programs,<sup>11</sup> and/or government agencies (e.g., NIST’s National Vulnerability Database<sup>12</sup>) or other such forums (e.g. CVE<sup>13</sup>), should not be treated on par with malicious (or Black Hat) hackers. However, the Computer Fraud and Abuse Act (CFAA), a 1980s-era law originally designed to punish and deter intrusions into government and <sup>fi</sup>nancial-industry computer systems — the main federal law still used today to punish hackers — is often applied to all hacking activities, irrespective of the intention of the hacker. For example, many legal and popular publications have debated the legal outcomes regarding the conviction of Andrew Aurnheimer for exposing 114,000 emails of iPad customers to AT&T due to a vulnerability in the AT&T website, the prosecution of Aaron Swartz for downloading (without subscription) JSTOR research articles, and the conviction of Mathew Keys for providing a password to a Los Angeles Times website account [23]. Those parties in favor of modifying the CFAA law (e.g., the Electronic Frontier Foundation) are however not having much success in changing policy. In fact, the U.S. federal government’s intention of doubling down on its policy e<sup>f</sup>orts to curb cybercrime via CFAA was evident in President’s Obama’s 2015 State of the Union Address. This study shows that an indiscriminate policy of targeting all hacker activities under the CFAA law is not necessarily consistent with good public policy. More speci<sup>fi</sup>- cally, the sentencing guidelines under CFAA are very strict and very broadly de<sup>fi</sup>ned. While vandalizing physical property usually carries some <sup>fi</sup>ne, a jail sentence of a few weeks, and/or community service,<sup>14</sup> vandalizing a website could result in a jail sentence of several years! This study provides analytical support to those who argue that CFAA policies, especially with respect to its sentencing guidelines, should be modi<sup>fi</sup>ed to protect the interests of software security researchers and ethical hackers. Such a policy update should include speci<sup>fi</sup>c guidelines on vulnerability research and disclosure such that ethical hackers do not break the law. For example, if a hacker discovers vulnerability, informs the vendor of the software product <sup>fi</sup>rst, and then discloses the vulnerability to the public, then he should not be prosecuted. However, currently under the CFAA, even the act of discovering software vulnerability could be a criminal activity [7].

What can the software industry do? The software industry, while not a big fan of hacking activities, has come to accept the presence of hackers as a key stakeholder in the software ecosystem. Many industry vendors and users actually have taken steps already to reduce their risk from unethical hacking by encouraging ethical hacking. Ethical hacking activities will result in more secure software and thereby it will reduce the risks from unethical hacking. For example:

● Software developers such as PayPal, Google, and Firefox have Vulnerability Rewards programs (VRP) that encourage hackers to discover and responsibly disclose vulnerabilities [1, 16, and 41].

● Software producers such as Apple and Microsoft sponsor and encourage hacking competition (e.g., Pwn2Own) to identify vulnerabilities in their products.

● Software producers paying ethical hackers to test their products for software vulnerabilities [e.g., 20].

● As part of risk assessment, industrial software users now often will hire consulting <sup>fi</sup>rms sta<sup>f</sup>ed with ethical hackers to audit the security of their systems. In fact, all leading consulting <sup>fi</sup>rms have cybersecurity divisions that provide pen-testing services to their clients. Some user <sup>fi</sup>rms, such as United Airlines, employ resources of individual ethical hackers using bug-<sup>fi</sup>nder loyalty program bonuses.<sup>15</sup>

In short, by incorporating known hackers into the operational activities and processes of software producing and software using <sup>fi</sup>rms, the managers of those <sup>fi</sup>rms indeed can bene<sup>fi</sup>t from reduced hacking activities from unethical hackers. These ongoing policy changes within select leading-edge <sup>fi</sup>rms illustrate the potential implications of our modeling exercise. If one or more <sup>fi</sup>rms are successful in eliminating attacks from unethical hackers, then Scenario 1, where no malicious hacking exists, or Scenario 2, where not all of the competition is targeted comes into play. In both these scenarios, the <sup>fi</sup>rms competing in various software market segments would bene<sup>fi</sup>t from a lack of competition. However, this is not necessarily a good outcome for the software users. These scenarios leave the users less well o<sup>f</sup> because: (a) lack of competition is not good for consumers; and (b) in case of Scenario 2, they risk cyberattacks from unethical hackers.

## Potential Limitations and Future Research Directions

As with any modeling study, the model documented in this paper exhibits potential limitations that provide opportunities for additional study of related issues. As analytical studies are built on speci<sup>fi</sup>c modeling assumptions, researchers might always improve the rigor of <sup>fi</sup>ndings by examining di<sup>f</sup>erent modeling frameworks and di<sup>f</sup>erent assumptions. While there are known to be several categories of hacker attacks, in this manuscript we view malicious hacker attacks as a generic construct, and do not disentangle the e<sup>f</sup>ects of di<sup>f</sup>erent hacking types. Given we are modeling industry level outcomes, we also are unable to incorporate into our model variables such as the attack severity. Perhaps future researchers can extend the work here to examine how di<sup>f</sup>erent types of hacker attacks, severity of attacks, and bene<sup>fi</sup>ts/harms of attacks, among other issues, may a<sup>f</sup>ect the competitive software market structure. Finally, while we focus on long-term equilibriums of the software market, future research might extend the examination to focus on (a) short-run impacts of hacker actions on software market competition and (b) the associated social welfare implications resulting from a competitive software market.

## Notes

1. https://us.norton.com/internetsecurity-emerging-threats-what-is-the-di<sup>f</sup>erence-betweenblack-white-and-grey-hat-hackers.html

2. https://cybermap.kaspersky.com/

3. https://investor.yahoo.net/releasedetail.cfm?ReleaseID=990570

4. https://www.consumer.ftc.gov/blog/2017/09/equifax-data-breach-what-do

5. https://www.gartner.com/newsroom/id/3859963

6. https://nvd.nist.gov/

7. https://securelist.com/exploits-how-great-is-the-threat/78125/

8. http://www.applemust.com/are-android-users-really-more-loyal-than-iphone-users/

9. https://appleinsider.com/articles/18/03/08/survey-calls-android-buyers-more-loyal-but-moreusers-are-still-switching-to-ios

10. There is one data point for Blackberry/Microsoft because of their short partnership at that time.

11. https://hackerone.com/bug-bounty-programs

12. https://nvd.nist.gov/

13. https://cve.mitre.org/

14. http://www.criminaldefenselawyer.com/crime-penalties/federal/Vandalism.htm

15. https://www.united.com/web/en-US/content/contact/bugbounty.aspx

## References

1. Algarni, A.M.; and Malaiya, Y.K. Software vulnerability markets: Discoverers and buyers. International Journal of Computer, Electrical, Automation, Control and Information Engineering, 8, 3 (2014), 480–490.

2. Arora, A.; Caulkins, J.P.; and Telang, R. Sell <sup>fi</sup>rst, <sup>fi</sup>x later: Impact of patching on software quality. Management Science, 52, 3 (March 2006), 465–471.

3. August, T.; and Tunca, T.I. Who should be responsible for software security? A comparative analysis of liability policies in network environments. Management Science, 57, 5 (May 2011), 934–959.

4. Anderson, R. Why information security is hard- An economic perspective. 17th Annual Computer Security Applications Conference (ACSAC’01), IEEE Computer Society, December, 2001. https://www.acsac.org/2001/papers/110.pdf, (accessed March 12, 2017).

5. Barnes, R.; and Fulford, G.R. Mathematical Modelling with Case Studies: A Diferential Equations Approach using Maple and MATLAB. Boca Raton, FL: CRC Press, 2002, pp. 99–109.

6. Bitzer, J. Commercial versus open source software: The role of product heterogeneity in competition. Economic Systems, 28, 4 (December 2004), 369–381.

7. Brewster, T. US cybercrime laws being used to target security researchers. The Guardian, Thursday 29 May 2014. https://www.theguardian.com/technology/2014/may/29/uscybercrime-laws-security-researchers.

8. Brynjolfsson, E. and Kemerer, C.F. Network externalities in microcomputer software: An econometric analysis of the spreadsheet market. Management Science, 42, 12 (December 1996), 1627–1647.

9. Cavusoglu, H.; Cavusoglu, H.; and Raghunathan, S. E<sup>fi</sup>ciency of vulnerability disclosure mechanisms to disseminate vulnerability knowledge. IEEE Transactions on Software Engineering, 33, 3 (March 2007), 171–185.

10. Cavusoglu, H.; Mishra, B.; and Raghunathan, S. The e<sup>f</sup>ect of internet security breach announcements on market value: capital market reactions for breached <sup>fi</sup>rms and internet security developers. International Journal of Electronic Commerce, 9, 1 (2004), 69.

11. CBS. These Cybercrime Statistics Will Make You Think Twice About Your Password: Where’s The CSI Cyber Team When You Need Them? CBS.com, March 3, 2015. http:// www.cbs.com/shows/csi-cyber/news/1003888/these-cybercrime-statistics-will-make-youthink-twice-about-your-password-where-s-the-csi-cyber-team-when-you-need-them -/(accessed November 2, 2016).

12. Economides, N.; and Katsamakas, E. Two-sided competition of proprietary vs. open source technology platforms and the implications for the software industry. Management Science, 52, 7 (July 2006), 1057–1071.

13. English Oxford Living Dictionaries. Accessed on August 25 2019: https://en.oxforddiction aries.com/de<sup>fi</sup>nition/hacker

14. Fan, M.; Kumara, S.; and Whinston, A.B. Short-term and long-term competition between providers of shrink-wrap software and software as a service. European Journal of Operational Research, 196, 2, 16 (July 2009), 661–671.

15. Farrell, J.; and Saloner, G. Installed base and compatibility: Innovation, product pronouncements, and predation. The American Economic Review, 76, 5 (December 1986), 940–955.

16. Finifter, M.; Akhawe, D.; and Wagner, D. An empirical study of vulnerability rewards programs. Presented at 22<sup>nd</sup> USENIX Security Symposium, August 14-16, Washington DC.

Accessed on August 25 2019: https://www.usenix.org/conference/usenixsecurity13/technicalsessions/presentation/<sup>fi</sup>nifter.

17. Finkle, J. 6 more stores attacked by same hack as target: Firm. Reuters, January $1 7 ^ { \mathrm { t h } }$ 2014. http://www.hu<sup>fi</sup>ngtonpost.com/2014/01/17/six-other-stores-are-bein\_n\_4618414.html (accessed January 22, 2014).

18. Gallaugher, J.M., and Wang, Y. Understanding network e<sup>f</sup>ects in software markets: Evidence from web server pricing. MIS Quarterly, 26, 4 (December 2002), 303–327.

19. Gandal, N. Competing compatibility standards and network externalities in the PC software market. The Review of Economics and Statistics, 77, 4 (November 1995), 599–608.

20. Gander, K. Microsoft pays out \$100,000 to hacker who exposed Windows security <sup>fl</sup>aws. Independent, Thursday 10 October 2013.

21. Garcia, A.; Sun, Y.; and Shen, J. Dynamic platform competition with malicious users. Dynamic Games and Applications 4, 3 (2014), 209–308.

22. Gordon, L.A.; Loeb, M.P.; and Sohail, T. A Framework for using insurance for cyber risk management. Communications ACM, 46, 3 (2003), 81–85.

23. Gustin, S. U.S. “Hacker” crackdown sparks debate over computer-fraud law. Time, March 19, 2013. Accessed on August 25 2019: http://business.time.com/2013/03/19/u-s-hackercrackdown-sparks-debate-over-computer-fraud-law/.

24. Jaisingh, J.; See-To, E.; and Tam, KY. The impact of open source software on the strategic choices of <sup>fi</sup>rms developing proprietary software. Journal of Management Information Systems, 25, 3 (2008), pp.243–277.

25. Kannan. K.; and Telang, R. Market for software vulnerabilities? Think again. Management Science, 51, 5 (May 2005) 726–740.

26. Katz, M. L.; and Shapiro, C. Systems competition and network e<sup>f</sup>ects. The Journal of Economic Perspectives, 8, 2 (Spring 1994), 93–115.

27. Kim, B. C.; Chen, P.; and Mukhopadhyay, T. (2010b). The e<sup>f</sup>ect of liability and patch release on software security: The monopoly case. Production and Operations Management, 20, 4, 603–617.

28. Lanzi, D. Competition and open source with perfect software compatibility. Information Economics and Policy, 21, 3 (August 2009), 192–200.

29. Lin, L. Impact of user skills and network e<sup>f</sup>ects on the competition between open source and proprietary software. Electronic Commerce Research and Applications, 7, 1 (Spring 2008), 68–81.

30. Marks, P. Dot-dash-diss: The gentleman hacker’s 1903 lulz. New Scientist. Issue 2844, December 27, 2011. (accessed October 14, 2013).

31. Marshall, A. Causes, e<sup>f</sup>ects and solutions of piracy in the computer software market. Review of Economic Research on Copyright Issues, 4, 1 (2007), 63–86.

32. Merriam-Webster Dictionary Accessed on August 25 2019: http://www.merriam-webster. com/dictionary/hacker.

33. Rochet, J.; and Tirole, J. Platform competition in two-sided markets. Journal of the European Economic Association, 1, 4 (June 2003), 990–1029.

34. Samtani, S.; Chinn, R.; Chen, H.; and Nunamaker, J.F. Exploring emerging hacker assets and key hackers for proactive cyber threat intelligence. Journal of Management Information Systems, 34, 4 (2017), 1023–1053.

35. Sen, R. A Strategic analysis of competition between open source and proprietary software. Journal of Management Information Systems, 24, 1 (Summer 2007), 233–257.

36. Swire, P.P. A model for when disclosure helps security: What is di<sup>f</sup>erent about computer and network security? In M.F. Grady and F. Parisi (eds.), The Law and Economics of Cybersecurity. Cambridge: Cambridge University Press, 2005, pp. 29–70.

37. Telang, R.; and Wattal, S. An empirical analysis of the impact of software vulnerability announcements on <sup>fi</sup>rm stock price. IEEE Transactions on Software Engineering, 33, 8 (August 2007), 544–557.

38. Verizon. 2016 Data Breach Investigations Report. http://www.verizonenterprise.com/verizoninsights-lab/dbir/2016/(accessed November 2, 2016).

39. Wright, C.S. Software, vendors and reputation: An analysis of the dilemma in creating secure software. Lecture Notes in Computer Science, 6802 (2011), 346–360.

40. Zetter, K. The biggest security threats we’ll face in 2016. Wired.com, January 1, 2016. https://www. wired.com/2016/01/the-biggest-security-threats-well-face-in-2016/. (accessed on November 2, 2016).

41. Zhao, M.; Grossklags, J.; and Liu, P. An empirical study of web vulnerability discovery ecosystems. In Proceeding CCS ‘15 Proceedings of the 22nd ACM SIGSAC Conference on Computer and Communications Security, 2015, pp. 1105–1117.

## About the Authors

Ravi Sen (rsen@mays.tamu.edu; corresponding author) is an Associate Professor at Mays Business School, Texas A&M. He received his Ph.D. from the University of Illinois at Urbana-Champaign. His research interests include cybersecurity, open source software, and economics of electronic commerce. Dr. Sen has published in Journal of Management Information Systems, Decision Sciences, International Journal of Electronic Commerce, Communications of AIS, and other journals.

Ajay Verma (ajay.verma@lmco.com) is a Senior Engineer at Lockheed Martin Missiles and Fire Control, involved in innovative conceptual design of new systems. Dr. Verma received his Ph.D. from Texas A&M University. He was previously Senior Research Scientist for Knowledge Based Systems, where he was principal investigator for innovative research sponsored by Department of Defense. His research interests include simulation and modelling, dynamic analysis and control of large multi-agent complex systems, system optimization, control, and guidance of aerospace systems.

Gregory R. Heim (gheim@mays.tamu.edu) is the Janet and Mark H. Ely \`83 Professor in the Department of Information & Operations Management, Mays Business School at Texas A&M University. He holds Ph.D. in Business Administration from the Carlson School of Management at the University of Minnesota. Dr. Heim’s research focuses on service and e-service/e-retail operations, management of technology, supply chain management, and quality management. He is a Department Editor of the Technology Management area of Journal of Operations Management and Senior Editor of Production and Operations Management.
