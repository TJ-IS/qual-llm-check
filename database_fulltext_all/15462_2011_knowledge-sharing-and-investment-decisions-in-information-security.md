---
otero_id: 15462
otero_key: "B7Y2B9E5"
title: "Knowledge sharing and investment decisions in information security"
authors: "Dengpan Liu; Yonghua Ji; Vijay Mookerjee"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.05.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge sharing and investment decisions in information security

Dengpan Liu <sup>a</sup>, Yonghua Ji <sup>b</sup>, Vijay Mookerjee <sup>c,</sup>⁎

<sup>a</sup> College of Business Administration, University of Alabama in Huntsville, United States

<sup>b</sup> School of Business, University of Alberta, Canada

<sup>c</sup> School of Management, University of Texas at Dallas, United States

## a r t i c l e i n f o

Article history: Received 21 December 2009 Received in revised form 19 April 2011 Accepted 19 May 2011 Available online 27 May 2011

Keywords: Security investment Knowledge sharing Coordination scheme Nash equilibrium Taylor series approximation

## a b s t r a c t

We study the relationship between decisions made by two similar <sup>fi</sup>rms pertaining to knowledge sharing and investment in information security. The analysis shows that the nature of information assets possessed by the two <sup>fi</sup>rms, either complementary or substitutable, plays a crucial role in in<sup>fl</sup>uencing these decisions. In the complementary case, we show that the <sup>fi</sup>rms have a natural incentive to share security knowledge and no external in<sup>fl</sup>uence to induce sharing is needed. However, the investment levels chosen in equilibrium are lower than optimal, an aberration that can be corrected using coordination mechanisms that reward the <sup>fi</sup>rms for increasing their investment levels. In the substitutable case, the <sup>fi</sup>rms fall into a Prisoners' Dilemma trap where they do not share security knowledge in equilibrium, despite the fact that it is bene<sup>fi</sup>cial for both of them to do so. Here, the bene<sup>fi</sup>cial role of a social planner to encourage the <sup>fi</sup>rms to share is indicated. However, even when the <sup>fi</sup>rms share in accordance to the recommendations of a social planner, the level of investment chosen by the <sup>fi</sup>rms is sub-optimal. The <sup>fi</sup>rms either enter into an “arms race” where they overinvest or reenact the under-investment behavior found in the complementary case. Once again, this suboptimal behavior can be corrected using incentive mechanisms that penalize for over-investment and reward for increasing the investment level in regions of under-investment. The proposed coordination schemes, with some modi<sup>fi</sup>cations, achieve the socially optimal outcome even when the <sup>fi</sup>rms are risk-averse. Implications for information security vendors, <sup>fi</sup>rms, and social planner are discussed.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

The incidence of cyber-attacks and security breaches has become a major concern in recent times. These attacks have been directed at a wide variety of organizations, ranging from high-pro<sup>fi</sup>le <sup>fi</sup>rms to prestigious universities. Present-day hackers appear to be motivated more by <sup>fi</sup>nancial gains rather than by personal curiosity or thrill seeking behavior [17]. For these reasons, information security has become a vital issue for <sup>fi</sup>rms that use the Internet to conduct business [3,19]. For those <sup>fi</sup>rms that do not directly use the Internet to conduct business, information security is still a concern because these <sup>fi</sup>rms often possess large amounts of sensitive electronic information relating to customer pro<sup>fi</sup>les, product sales, and technical expertise.

This paper considers three important elements that combine to affect a <sup>fi</sup>rm's decisions on information security matters: (1) knowledge sharing, (2) <sup>fi</sup>nancial investments in information security, and (3) the nature of information assets being protected. The <sup>fi</sup>rst two elements – both affecting information security – have been studied in earlier research. The main contribution of this paper is an integrated study of the interaction among these three elements on the information security of <sup>fi</sup>rms. We discuss these elements below.

## 1.1. Knowledge sharing and investment

A direct way for <sup>fi</sup>rms to become more secure is to increase investments in information security. For example, <sup>fi</sup>rms can enhance information security by investing in security technologies such as antivirus software, <sup>fi</sup>rewalls, sophisticated encryptiontechnology, intrusion detection systems, and other hardware devices ([7,11,12,22], [2]). Such investments must be made after carefully trading-off investment costs with the increase in information security that is brought about by the investment.

Firms can also improve information security by collaborating and sharing security related knowledge with other <sup>fi</sup>rms. An example of security knowledge sharing is the Information Technology Information Sharing and Analysis Center (IT-ISAC) (https://www.it-isac.org), aimed at facilitating the sharing of information on cyber-security threats and vulnerabilities. This center provides a neutral forum for members to interact with peers from other member companies to share and understand non public details of threats and vulnerabilities. It also provides members a trusted point of contact for information sharing prior to and during incidents. We identify conditions where such examples of knowledge sharing can be expected to naturally occur in equilibrium. In other situations, we <sup>fi</sup>nd that sharing needs to be encouraged (or regulated), i.e., <sup>fi</sup>rms do not naturally share and <sup>fi</sup>nd themselves in a Prisoners' Dilemma.

Knowledge sharing has been broadly studied in the economics literature [9,16,21,24] both within and outside the context of information security. Gordon et al. [5] examine how sharing knowledge (information) across <sup>fi</sup>rms affects the overall investment level in information security products. Gal-Or and Ghose [4] analyze how the sharing of security knowledge by two <sup>fi</sup>rms in<sup>fl</sup>uences security investments and price competition between these <sup>fi</sup>rms. Outside the information security area, Shapiro [16] investigates whether competing <sup>fi</sup>rms can gain by sharing private information on cost with one another and the social welfare effects of such information exchange. Kirby [9] examines the incentives of <sup>fi</sup>rms to share knowledge about an unknown demand parameter. Vives [21] analyzes the effects of different disclosure rules imposed by trade associations on the incentives to share knowledge and on the welfare of consumers, <sup>fi</sup>rms, and society. Ziv [24] endogenizes the incentives for truthful knowledge sharing and develops a mechanism that can make <sup>fi</sup>rms reveal the true value of their private information.

While the economic impacts of information security investments and knowledge sharing have been studied by other researchers (e.g., [4,5]), the interplay between the nature of information assets and how this nature affects decisions concerning the sharing of security knowledge and investments in information security, has not been emphasized. The two types of information assets considered in this study are discussed next.

## 1.2. Nature of information assets

We consider information assets to be complementary or substitutable. Information assets are complementary if the combined information assets of two <sup>fi</sup>rms are of signi<sup>fi</sup>cant value while the information asset of a single <sup>fi</sup>rm is of little value to a hacker. When two <sup>fi</sup>rms possess complementary information, the hacker has an incentive to attack the second <sup>fi</sup>rm only if the hacking attempt at the <sup>fi</sup>rst <sup>fi</sup>rm is successful. Hence, successful hacking attempts at the <sup>fi</sup>rst <sup>fi</sup>rm leads to penetrated cross traf<sup>fi</sup>c toward the other <sup>fi</sup>rm. As an example of complementary information, consider two <sup>fi</sup>rms with overlapping customers: one <sup>fi</sup>rm stores customer names and social security numbers, while the other stores customer names, addresses and phone numbers. Only if information from both <sup>fi</sup>rms is obtained (and appropriately combined) can hackers fraudulently apply for new credit cards, or loans. In such situations, the information security of the two <sup>fi</sup>rms becomes a common concern because it is conceivable that both <sup>fi</sup>rms could be held liable for unauthorized purchases, or suffer from law suits or reputation damage [18]. To better illustrate the complementary information assets, we use another hypothetical motivating example as follows. Assume a <sup>fi</sup>rm has outsourced the job of designing a major component of a new product to a vendor <sup>fi</sup>rm. For instance, in a major commercial airplane company, the tail-section design of a new airplane model was outsourced to a vendor <sup>fi</sup>rm. A hacker who is interested in getting business intelligence regarding the whole design of the new airplane would have to obtain design information from both <sup>fi</sup>rms. Further, it can be assumed that the principal <sup>fi</sup>rm and the vendor make independent security decisions.

Information assets belonging to two <sup>fi</sup>rms are substitutable if the incremental bene<sup>fi</sup>t of attacking the second <sup>fi</sup>rm (after successfully penetrating the <sup>fi</sup>rst one) is lower than the effort to a hacker. Hence, having penetrated one of the <sup>fi</sup>rms, and gained access to the assets there, a hacker would stop. On the other hand, an unsuccessful attempt to penetrate the <sup>fi</sup>rst <sup>fi</sup>rm would lead to deflected cross traf<sup>fi</sup>c — a hacker has incentive to penetrate the second <sup>fi</sup>rm after failing to penetrate the <sup>fi</sup>rst one. It is well known that Walmart and Proctor & Gamble share retail sales information on P&G products at Walmart stores [6]. If a hacker is interested in obtaining such sales information, then successfully penetrating either Walmart or P&G's systems would achieve this goal. Before Walmart and Proctor & Gamble share information, there could be an agreement that the <sup>fi</sup>rm responsible for leaking the information will be held liable. This way, when an information breach happens, only the breached <sup>fi</sup>rm suffers the loss and the other <sup>fi</sup>rm is covered by the agreement.

Each <sup>fi</sup>rm has its own security risk, and such risk has already been addressed extensively [13,20]. It is interesting to note that the nature of information assets stored in <sup>fi</sup>rms can cause the interdependency of security risks between <sup>fi</sup>rms. The security risk interdependency has been an important issue studied in the literature. Ogut et al. [14] show that the interdependency between the security risk of different <sup>fi</sup>rms reduces the incentive to invest in security and to purchase cyberinsurance. Kunreuther and Heal [10] identify both over-investment and under-investment as possible concerns with <sup>fi</sup>rms that have interdependent security risk. Heal and Kunreuther [8] show that a <sup>fi</sup>rm's incentive to invest on security is lowered when other <sup>fi</sup>rms with interdependent security risk do not invest on security. Zhao et al. [23] discuss three risk management approaches to deal with the positive and negative network externalities caused by interdependent security risk. Previous research, however, has not emphasized how the nature of information assets (complementary or substitutable) possessed by <sup>fi</sup>rms affects their knowledge sharing and security investment decisions. As discussed above, this feature of information assets signi<sup>fi</sup>cantly affects hacker incentives and hence, a <sup>fi</sup>rm's knowledge sharing and security investment decisions. Our model provides insights into investment and knowledge sharing decisions in the context of complementary and substitutable information assets. Another important contribution we make is to do with incidencebased coordination schemes that successfully address both underand over-investment concerns raised in the existing literature [10,14,23]. Our <sup>fi</sup>nding that <sup>fi</sup>rms are not willing to share information in the substitutable case contrasts with the <sup>fi</sup>nding by Gal-or and Ghose [4] that an increase in information sharing by one <sup>fi</sup>rm will induce the other <sup>fi</sup>rm to increase its own level of information sharing.

## 1.3. Problem setting

In the problem, two <sup>fi</sup>rms participate in a game in which knowledge sharing and security investment are decision variables. We <sup>fi</sup>rst examine a scenario where the <sup>fi</sup>rms simultaneously make knowledge sharing and security investment decisions. Next we examine a case where the knowledge sharing decision is chosen in accordance to the recommendations of a social planner, followed by a game where the <sup>fi</sup>rms simultaneously choose their investment levels. Finally, we analyze the role of incentive mechanisms designed to correct sub-optimal investment decisions made by two <sup>fi</sup>rms, even when they share at a level that is prescribed by the social planner. Incentive schemes such as ours, are in principle, not uncommon in the information security literature. For example, August and Tunca [1] study the effect of user incentives on software patching under negative network security externalities. However, we propose the role of incentive mechanisms in information security from a different perspective.

A signi<sup>fi</sup>cant result of our analysis is that the substitutable nature of information assets could lead to over-investment (i.e., an “Arms Race” among <sup>fi</sup>rms) that security vendors would have no incentive to correct; on the contrary, vendors could exploit such behavior, for example, by playing one <sup>fi</sup>rm against the other. Furthermore, we show that the bene<sup>fi</sup>ts of sharing security knowledge among such <sup>fi</sup>rms are particularly important because it reduces the over-investment problem. However, because sharing is not an equilibrium outcome here, the role of a social planner to induce the <sup>fi</sup>rms to share is indicated. On the other hand, while <sup>fi</sup>rms that possess complementary information assets can be naturally expected to share security knowledge, such <sup>fi</sup>rms under-invest, i.e., a “Tragedy of Commons” occurs. This problem is less serious because vendors would have an incentive to correct it, for example, by providing security products with features that make it easier for <sup>fi</sup>rms to coordinate their investment decisions.

## 1.4. Implications and managerial insights

We discuss implications for security vendors, <sup>fi</sup>rms and social planner. For security vendors, our focus is on implications for the design of product features that in<sup>fl</sup>uence the sharing effectiveness and those that affect the ability of <sup>fi</sup>rms to implement investment coordination schemes. For <sup>fi</sup>rms, we consider implications for the purchase of security products that affect the sharing effectiveness and the connection between sharing effectiveness and the security budget of the <sup>fi</sup>rm. For the social planner, the focus is on implications for regulating the level of sharing for <sup>fi</sup>rms that make investment decisions in equilibrium.

## 1.4.1. Implications for security vendors

Since <sup>fi</sup>rms under-invest in the complementary case, vendors have an incentive to encourage <sup>fi</sup>rms to coordinate their investments levels. This should encourage vendors to design features in their products that facilitate the exchange of incident information. When the sharing effectiveness increases at relatively small values of the cost of information loss, the impact is to increase the investment level. Thus for small values of the cost of information loss, vendors should try to increase the sharing effectiveness, for example, by designing features that increase security product commonality even when the information technology environment of the two <sup>fi</sup>rms is different. This calls for a common security platform for small <sup>fi</sup>rms (or when the cost of information loss is small). On the other hand, for large <sup>fi</sup>rms (or when the cost of information loss is large), they should customize security products more so that the value of the sharing effectiveness is lowered and <sup>fi</sup>rms are induced to invest more. This insight provides security vendors with a natural way to segment the security product market, i.e., design products that facilitate sharing for small <sup>fi</sup>rms (or <sup>fi</sup>rms where information security is less important), while creating more customized and proprietary products for large <sup>fi</sup>rms (or where information security is more critical).

In the substitutable case, vendors are likely to exploit the fact that <sup>fi</sup>rms do not naturally share since such non-sharing behavior leads to an over-investment in security products. We will say more about this under policy implications. However, when full sharing is regulated, <sup>fi</sup>rms under-invest when the sharing effectiveness is relatively high. Here, the facilitation of coordination through product features will bene<sup>fi</sup>t security vendors to increase their sales of security products. However, given that sharing is a regulated, offequilibrium outcome, market forces naturally shield vendors against such under-investment. On the other hand, there is a perverse incentive for vendors to inhibit coordination for <sup>fi</sup>rms that operate with full sharing but with low sharing ef<sup>fi</sup>ciency. Here, the <sup>fi</sup>rms over-invest — a behavior that security vendors would like to exploit. Thus, in the substitutable case, vendors are less likely to be forthcoming with features in their products that facilitate coordination. This case is one where the role of a social planner is most signi<sup>fi</sup>cant since pure market forces are not likely to correct the over-investment problem.

Our recommendations for vendors may appear contradictory: facilitate coordination in the complementary case, whereas discourage it (or at least not actively seek it) in the substitutable case. We believe, however, that these two situations represent an opportunity for security product vendors. When <sup>fi</sup>rms are identi<sup>fi</sup>ed with complementary information assets, the vendor could encourage coordination by offering to customize the security solutions to these <sup>fi</sup>rms so that coordination is facilitated. On the other hand, when faced with two <sup>fi</sup>rms that possess substitutable assets, the vendor could sell the products without customization for coordination. The above selling approach would, of course, require the vendor to design the product in such a way that late customization of coordination features, depending on the nature of information assets, is viable.

## 1.4.2. Implications for firms

Here, we focus on implications that can be derived from the results of the simultaneous game. In the complementary case, <sup>fi</sup>rms should try to make the sharing effectiveness as large as possible, perhaps, by investing in security technologies that are common to partner <sup>fi</sup>rms, thereby increasing the value of the sharing effectiveness. For example, two <sup>fi</sup>rms with an integrated supply chain and complementary product and sales information, should attempt to build commonalities in their security platforms so as to increase the sharing effectiveness. For the substitutable case, however, the value of the sharing effectiveness is not important since, in equilibrium, the <sup>fi</sup>rms do not share. Another result of the simultaneous game in the complementary case that is useful for <sup>fi</sup>rms to consider is the impact of the sharing effectiveness on the security budget, i.e., the security investment cost. As the sharing effectiveness increases for relatively small values of the cost of information loss, more budget must be allocated for information security. The reverse is true for relatively large values of the cost of information loss. The impact of the cost of information loss is similar for the complementary and substitutable case: not surprisingly in both cases, increasing the cost of information loss leads to a higher level of investment. Finally, in both the complementary and substitutable case, <sup>fi</sup>rms are individually better off when they are regulated to share and when their investment decisions are coordinated so as to minimize social cost.

## 1.4.3. Implications for social planner

Our focus here is on the regulatory role played by the social planner to recommend the level of sharing employed by the <sup>fi</sup>rms. Our results show that there is no need for regulating the level of sharing in the complementary case. This is true irrespective of the goal of the social planner, i.e., social cost minimization or security maximization. However, for the substitutable case, the social planner has an important role to play. This role takes on particular importance because there is no corrective force in the market to curb the tendency of <sup>fi</sup>rms to over-invest. On the contrary, as mentioned earlier, there is the possibility that vendors will exploit this over-investing behavior to increase their sales of security products. By regulating the level of sharing the over-investment problem can be avoided, but a problem of under-investment is created when the sharing effectiveness is relatively high. The under-investment problem, however, has a helpful market force, namely, the security vendor, that is acting to reduce it. Thus the efforts of the social planner are best spent on attempting to reduce over-investment behavior. Interestingly, even in the substitutable case, the social planner with the goal of maximizing the security level has no role to play, since this outcome is naturally achieved in equilibrium by the <sup>fi</sup>rms when they simultaneously choose sharing and investment levels.

The rest of the paper is organized as follows. In Section 2, we introduce a vulnerability function in the presence of knowledge sharing. We next analyze the effect of knowledge sharing on investment decisions in two subsequent sections: in Section 3, we study the complementary case, while the case of substitutable information is discussed in Section 4. In these two sections, we also present incentive schemes that could help <sup>fi</sup>rms coordinate investment decisions in the presence of knowledge sharing. We conclude the paper in Section 5.

## 2. Vulnerability function

We use a vulnerability function P, to represent the probability that a <sup>fi</sup>rm's systems will be breached given a hacking attempt.

Consistent with previous literature [4,5], this breach probability function P depends on a <sup>fi</sup>rm's direct investment on security and the indirect effect of sharing security knowledge with the other <sup>fi</sup>rm. By sharing knowledge, <sup>fi</sup>rms can leverage the investment made by the partner <sup>fi</sup>rm and achieve the same level of security at a lower level of investment. Let x and $x _ { j }$ be the levels of investment in security protection by <sup>fi</sup>rms i and j respectively. Assuming that security investments and knowledge sharing have an additive effect on a <sup>fi</sup>rm's vulnerability [5], <sup>fi</sup>rm i's vulnerability can be expressed as:

$$
P _ {i} = P \left(x _ {i} + \beta_ {j} \eta x _ {j}\right)\tag{1}
$$

where $\beta _ { j } \in [ 0 , 1 ]$ is <sup>fi</sup>rm $j ^ { \prime } s$ sharing level. When $\beta _ { j } = 1$ , <sup>fi</sup>rm j shares fully, and when $\beta _ { j } = 0 ,$ , <sup>fi</sup>rm j does not share at all; a value between zero and one represents partial sharing. The parameter ηın[0, 1] represents the effectiveness of knowledge sharing, similar to the cost spillover parameter in Gal-Or and Ghose [4]. The value of the sharing effectiveness parameter can be related to the similarity of the information technology environments at the two <sup>fi</sup>rms. For instance, if one <sup>fi</sup>rm uses a Linux operating system while the other <sup>fi</sup>rm has a Windows environment, sharing security knowledge may be of less value. In such cases, the value of η would be relatively low.

For most of the results in this paper, we only need to assume a vulnerability function that is decreasing and convex in the effective investment $y ~ ( = x _ { i } + \beta _ { j } \eta x _ { j } )$ , that the <sup>fi</sup>rst and the second derivatives exist for all feasible values of the effective investment, and that

$$
\lim _ {y \to \infty} P (y) \to 0,
$$

implying that the vulnerability asymptotically approaches zero as the effective investment increases. In the next section, we consider the case of two <sup>fi</sup>rms that possess complementary information assets, followed by a section that is devoted to the case of substitutable assets.

## 3. Complementary information

In this section, we consider two similar <sup>fi</sup>rms i and j with complementary information assets. By similar we mean that the two <sup>fi</sup>rms have the same vulnerability function P and the same cost if breached. In the complementary case, after penetrating one <sup>fi</sup>rm, a hacker would need to attack and penetrate the other <sup>fi</sup>rm to derive value. If only one <sup>fi</sup>rm is penetrated, the complementary nature of information ensures that no value accrues to the hacker, and no loss occurs to the <sup>fi</sup>rms. Assuming no prior information on the vulnerability of the <sup>fi</sup>rms, it is reasonable to posit that each <sup>fi</sup>rm is attacked with equal probability. We let the cost of information loss be V for each <sup>fi</sup>rm when both <sup>fi</sup>rms are compromised and zero if only one <sup>fi</sup>rm is compromised. We <sup>fi</sup>rst consider a case where the sharing and investment decisions are made simultaneously and contrast this analysis with the case where sharing is regulated, but the investment decisions are taken in equilibrium.

## 3.1. Investment and sharing: simultaneous equilibrium

Here, we consider two <sup>fi</sup>rms that simultaneously make sharing and investment decisions, i.e., <sup>fi</sup>rm i simultaneously decides on $\beta _ { i }$ and x and <sup>fi</sup>rm j simultaneously decides on $\beta _ { j }$ and $x _ { j } .$ Firm i's expected cost is:

$$
C _ {i} = \frac {1}{2} P (x _ {i} + \beta_ {j} \eta x _ {j}) P (x _ {j} + \beta_ {i} \eta x _ {i}) V + \frac {1}{2} P (x _ {j} + \beta_ {i} \eta x _ {i}) P (x _ {i} + \beta_ {j} \eta x _ {j}) V + x _ {i}\tag{2}
$$

The <sup>fi</sup>rst term is the cost of information loss that occurs from the cross traf<sup>fi</sup>c that comes to <sup>fi</sup>rm j after penetrating <sup>fi</sup>rm i. The second term is the cost of the loss due to cross traf<sup>fi</sup>c from <sup>fi</sup>rm j to <sup>fi</sup>rm i. The third term is the investment cost. Since the <sup>fi</sup>rst two terms are equal, we can rewrite Eq. (2) as:

$$
C _ {i} = P \left(x _ {i} + \beta_ {j} \eta x _ {j}\right) P \left(x _ {j} + \beta_ {i} \eta x _ {i}\right) V + x _ {i}\tag{3}
$$

Similarly, the cost function of <sup>fi</sup>rm j is the following:

$$
C _ {j} = P \left(x _ {j} + \beta_ {i} \eta x _ {i}\right) P \left(x _ {i} + \beta_ {j} \eta x _ {j}\right) V + x _ {j}\tag{4}
$$

Consider <sup>fi</sup>rm $j ^ { \prime } s$ sharing decision, holding <sup>fi</sup>rm i's sharing decision constant. $\mathsf { A } s \beta _ { j }$ increases, $P ( x _ { i } + \beta _ { j } \eta x _ { j } )$ decreases, leading to a decrease in $C _ { j } .$ To minimize $C _ { j } ,$ we should let $\beta _ { j }$ take the maximum value (i.e., a boundary solution) ${ } _ { , \beta _ { j } = 1 }$ . Thus, <sup>fi</sup>rm j's dominant strategy is to share fully. Similarly, <sup>fi</sup>rm i's dominant strategy is also to share fully. Hence, we have the following remark.

Remark 1. If information assets are complementary, then (Full Share, Full Share), i.e., $\beta _ { i } = \beta _ { j } = 1$ , is the Nash Equilibrium.

By sharing more, a <sup>fi</sup>rm can bene<sup>fi</sup>t the other <sup>fi</sup>rm by increasing the security at that <sup>fi</sup>rm. This, in turn, bene<sup>fi</sup>ts the <sup>fi</sup>rm that shares: a stronger security system at the other <sup>fi</sup>rm enhances the total security experienced by the sharing <sup>fi</sup>rm. Therefore, given <sup>fi</sup>rm $i ( j ) ^ { \prime } s$ investment and sharing decisions, <sup>fi</sup>rm j (i) always chooses to share fully, i.e., full sharing is a dominant strategy for <sup>fi</sup>rm j (i). Therefore, $\beta _ { i } = \beta _ { j } = 1$ is a stable outcome.

## 3.2. Comparative statics: simultaneous equilibrium

From the previous discussion, we have seen that in the complementary case, both <sup>fi</sup>rms fully share security knowledge in equilibrium. In this section, we will see how <sup>fi</sup>rms' equilibrium investment level $\left( x _ { e } \right)$ , vulnerability level $\left( P _ { e } \right)$ , and total cost $( C _ { e } )$ change as η (sharing effectiveness) or V (cost of information loss) increase.

## 3.2.1. Investment level

We <sup>fi</sup>rst examine how the equilibrium investment level changes when the cost of information loss increases. As seen earlier, the <sup>fi</sup>rms decide on the equilibrium investment amount while choosing to share fully $( \beta _ { i } = \beta _ { j } = 1 )$ . Firm i's objective is to minimize the total cost (3) by choosing the security investment amount $x _ { i \cdot }$ Since the two <sup>fi</sup>rms are similar, we can focus on symmetric solutions i.e., ${ x } _ { i } = { x } _ { j } = { x } _ { e } ,$ , where $\scriptstyle x _ { e }$ refers to the equilibrium investment amount that should satisfy

$$
P (x _ {e} + \eta x _ {e}) P ^ {\prime} (x _ {e} + \eta x _ {e}) + \frac {1}{(1 + \eta) V} = 0\tag{5}
$$

For a given η, we <sup>fi</sup>rst write the left-hand side of Eq. $( 5 ) \operatorname { a s } f ( x _ { e } , V ) ,$ , and then we have dx $\scriptscriptstyle 2 / d V = ( - \partial f / \partial V ) / ( \partial f / \partial x _ { e } )$ . Since $\partial f / \partial V = - 1 / [ ( 1 + \eta ) V ^ { 2 } ] <$ 0 and $\partial f / \partial x _ { e } = ( 1 + \eta ) { [ ( P ^ { \prime } ) ^ { 2 } + P P ^ { \prime \prime } ] } > 0 ,$ , we have $d x _ { e } / d _ { V } { > } 0 .$ Thus, we make the following remark.

Remark 2. The equilibrium investment level increases with the cost of information loss.

While the above result is not surprising, it is interesting to <sup>fi</sup>nd that the equilibrium security investment can increase or decrease in the sharing effectiveness. To see why this is so, let $f ( \eta , x _ { e } )$ be the left-hand side of Eq. (5). Hence,

$$
\frac {d x _ {e}}{d \eta} = \frac {- \partial f / \partial \eta}{\partial f / \partial x _ {e}}\tag{6}
$$

Because $\partial f / \partial x _ { e } { > } 0$ , the impact of the sharing effectiveness on the equilibrium security investment depends on the sign of $\partial f / \partial \eta$

$$
\frac {\partial f}{\partial \eta} = x _ {e} \left[ (P ^ {\prime}) ^ {2} + P P ^ {\prime \prime} \right] - \frac {1}{(1 + \eta) ^ {2} V}\tag{7}
$$

Note that the <sup>fi</sup>rst term of $\partial f / \partial \eta$ is positive, whereas the second term is negative. When $V {  } 0 ^ { + } , \partial f / \partial \eta { < } 0 ;$ ; hence, $d x _ { e } / d \eta { > } 0$ for any η. When $V \to \infty , \ \partial f / \partial t a > 0 ;$ ; hence $d x _ { e } / d \eta < 0$ for any $\eta .$ Thus for extreme values of $V ,$ the impact of sharing effectiveness on the equilibrium investment can be determined. However, for moderate values of V, the sign of $d x _ { e } / d \eta$ depends on the sharing effectiveness: the equilibrium investment <sup>fi</sup>rst increases and then decreases with the sharing effectiveness.

To provide some intuition for the above result, we observe that this result arises from two opposing forces affecting a <sup>fi</sup>rm's investment level at equilibrium. From Eq. (3), we can see that the cost for <sup>fi</sup>rm i depends on two breach probabilities: $P ( x _ { i } + \beta _ { j } \eta x _ { j } )$ and $P ( x _ { j } + \beta _ { i } \eta x _ { i } )$ . The <sup>fi</sup>rst force arises from the self-breach probability $P ( x _ { i } + \beta _ { j } \eta x _ { j } )$ . Consider the investment decision made by <sup>fi</sup>rm i (x ) holding $x _ { j }$ constant. As the sharing effectiveness increases, due to the bene<sup>fi</sup>t that <sup>fi</sup>rm i gains from <sup>fi</sup>rm $j ^ { \prime } s$ investment, the curve $P ( x _ { i } + \beta _ { j } \eta x _ { j } )$ versus $x _ { i }$ shifts horizontally to the left and the slope reduces accordingly, leading to a reduction in the marginal value of $x _ { i \cdot }$ Thus, based on the self-breach force, <sup>fi</sup>rm i has an incentive to invest less.

The second force is associated with the fact that an investment at <sup>fi</sup>rm i causes a positive network externality on <sup>fi</sup>rm j by increasing firm $j ^ { \prime } s$ security (cross-breach probability $P ( x _ { j } + \beta _ { i } \eta { \bf { x } } _ { i } ) )$ . Due to the complementary nature of the assets, the penetrated cross traf<sup>fi</sup>c coming from j toward i is reduced. When the cost of information loss (V) is small, the equilibrium investment is also relatively small (see Remark 2). For small $V ,$ when the sharing effectiveness increases, <sup>fi</sup>rm i moves to new vulnerability-investment curve that is steeper at the current (and low) investment level, i.e., the marginal value of investment increases. Thus, based on the cross-breach force, for small V, <sup>fi</sup>rm i has an incentive to invest more. The cross-breach force dominates at low levels of V. Hence, the overall impact of increasing sharing effectiveness is to increase the equilibrium level of investment.

We further examine the two underlying forces by using a numerical example. We choose the following parameter values: $a = 0 . 5 , \ b = 0 . 5 , \ \beta _ { i } = \beta _ { j } = 1$ . For the case of small $V ( V = 1 0 )$ , when $\eta = 0 . 1$ , we have the equilibrium investment $x _ { e } = 0 . 2 0 4 ,$ , and show the corresponding probability curves in Table 1. $\mathrm { A t } \ \eta { = } 0 . 1$ , when η increases, for the same security investment, the slope of the selfpenetration probability-investment curve is <sup>fl</sup>atter, which warrants less investment, and the slope of the self-penetration probabilityinvestment curve is steeper, which warrants more investment. Finally, from Eq. (7) we can get $\frac { \partial f } { \partial \boldsymbol { \eta } } \mid _ { \boldsymbol { \eta } = 0 . 1 } = - 0 . 0 5 8$ , which means that $\frac { \partial x _ { e } } { a \eta } \mid \eta = 0 . 1 > 0$ . Numerically, when η increases to $0 . 2 , x _ { e }$ increases to 0.241.

Table 1  
Slopes of probability curves as η increases.

<table><tr><td></td><td> $\eta=0.1$ </td><td> $\eta=0.2$ </td><td>Slope of probability curve</td></tr><tr><td>Slope of self-penetration probability curve:  $\frac{\partial P(x_i + \beta_j \eta x_j)}{\partial x_i} |_{x_e = 0.204}$ </td><td>-0.202</td><td>-0.199</td><td>Becomes flatter as  $\eta$  increases</td></tr><tr><td>Slope of cross-penetration probability curve:  $\frac{\partial P(x_j + \beta_i \eta x_i)}{\partial x_i} |_{x_e = 0.204}$ </td><td>-0.020</td><td>-0.040</td><td>Becomes steeper as  $\eta$  increases</td></tr></table>

When the cost of information loss is large, the equilibrium investment is also relatively large. Therefore, when the sharing effectiveness increases the cross-penetration curve becomes <sup>fl</sup>atter at the current (and high) investment level, i.e., the marginal value of investment decreases. Thus <sup>fi</sup>rm i has incentive to invest less. Since both the self-breach and the cross-breach forces lead to lower investment levels, the overall impact of increasing sharing effectiveness at high values of V is to lower the equilibrium investment.

When the cost of information loss is moderate, the cross-breach force dominates and is positive for small values of the sharing effectiveness. Hence, the investment level increases. For higher values of sharing effectiveness, the cross-breach force becomes less positive and the combined effect of the two forces is negative. Thus, security investment increases <sup>fi</sup>rst, and then decreases, as sharing effectiveness increases.

We also plot a <sup>fi</sup>gure to illustrate the above discussion. As shown in Fig. 1a, when the cost of information loss (V) is small $( \mathsf { V } = 1 0 )$ , as the sharing effectiveness increases, the equilibrium security investment at each <sup>fi</sup>rm keeps increasing. When V is large $( \mathsf { V } = 3 0 )$ , as the sharing effectiveness increases, the equilibrium security investment at each <sup>fi</sup>rm keeps decreasing. When V is moderate $( \mathrm { V } = 2 0 )$ , as the sharing effectiveness increases (see Fig. 1b), the equilibrium security investment at each <sup>fi</sup>rm <sup>fi</sup>rst increases and then decreases.

## 3.2.2. Security level

With some analysis, we show in Appendix A that the equilibrium security level increases with the sharing effectiveness, $\mathrm { i } . \mathrm { e } . , d P _ { e } / d \eta { < } 0$

a  
![](/api/attachments/B7Y2B9E5/fulltext/images/d2d10d966c57d0e43485d3790549fabf560ed242f5f4e9239f03be313e35f2d7.jpg)

![](/api/attachments/B7Y2B9E5/fulltext/images/901e1fe9d512e8c4616c5db087e69734706f8aba2f38870668849bbc178de30f.jpg)  
Fig. 1. Investment for different V.

As the sharing effectiveness increases, every dollar invested in <sup>fi</sup>rm j contributes more toward increasing the security of <sup>fi</sup>rm i. This effect dominates the possible reduction in investment that may occur as the sharing effectiveness increases. It is easy to show that the equilibrium security level increases when the cost of information loss becomes larger. Since d $P _ { e } / d x _ { e } { < } 0$ and $d x _ { e } / d V { > } 0$ , we have $d P _ { e } / d V = ( d P _ { e } / d x _ { e } )$ $( d x _ { e } / d V ) < 0$

## 3.2.3. Total cost

The total cost is the sum of the breach cost and the investment cost. Because $d P _ { e } / d \eta { < } 0 ,$ the breach cost must decrease as the sharing effectiveness increases. However, we have seen earlier that the investment level could increase or decrease with the sharing effectiveness. Thus the impact of sharing effectiveness on the overall cost is not immediately clear. In Appendix A, we show that the total cost to each <sup>fi</sup>rm decreases as the sharing effectiveness increases, i.e., $d C _ { i } / d \eta { < } 0 .$

To understand the above result, consider <sup>fi</sup>rm j's investment level held constant at the equilibrium level. As the sharing effectiveness increases, <sup>fi</sup>rm i can achieve a lower cost without changing the level of investment. However, the optimal change in the investment by <sup>fi</sup>rm i will be such that it further lowers the overall cost. This implies that the new equilibrium overall cost will always be lower with an increase in the sharing effectiveness. Effective sharing is bene<sup>fi</sup>cial to both <sup>fi</sup>rms and hence the <sup>fi</sup>rms should always be able to lower the equilibrium overall cost if η increases.

It can also be shown that the overall equilibrium cost increases with the cost of information loss, V. Thus, $d C _ { e } / d V { > } 0 .$ This effect can be better understood if we think in terms of lowering V and observing the impact on the equilibrium overall cost. Assuming that the previous level of security investment (i.e., before lowering V) is used, it is clear that a lower V will lead to a lower overall cost. However, the optimal change in the investment will be such that it further lowers the overall cost. This implies that the new equilibrium overall cost will always be lower with a decrease in the cost of information loss. Hence, for a higher V, <sup>fi</sup>rms should prepare by expecting higher security costs, which is the sum of the cost of recovering from breach incidents and the cost of investing in security systems.

## 3.3. Sharing regulation

From Section 3.1, we know that if <sup>fi</sup>rms are left to themselves, full sharing $( \mathrm { i } . \mathsf { e } . , \beta = 1 )$ is an equilibrium outcome. The question arises: is it sometimes worthwhile to discourage <sup>fi</sup>rms from full sharing? Assume that <sup>fi</sup>rms are free to choose their security investment levels in equilibrium but the sharing decision is chosen by the social planner. We examine the above question in the context of two possible objectives: (1) maximizing security level, and (2) minimizing social cost. A social planner chooses to minimize social cost when the cost of breach at each <sup>fi</sup>rm can be estimated. However, the cost of breach at each <sup>fi</sup>rm very often includes intangible cost (e.g. the cost of reputation damage), which is dif<sup>fi</sup>cult to measure, so in such cases it makes more sense for the social planner to choose to maximize <sup>fi</sup>rms' security level. The practice of maximizing <sup>fi</sup>rms' security level is not uncommon in industry. For instance, the PCI compliance in retailing industry tends to improve the security levels of the companies in the industry and leaves the cost issues to the complying companies. From a social planner's standpoint, since the <sup>fi</sup>rms are similar, it is suf<sup>fi</sup>cient to optimize each <sup>fi</sup>rm's objective function. We can show that for both of the above objectives, the optimal level of sharing that a social planner would choose is the same as what the <sup>fi</sup>rms would choose in equilibrium. Hence, no sharing regulation is needed. We state these results in the following theorems. The proofs of all the following theorems are provided in Appendix A.

Theorem 1. If complementary information is stored, the optimal level $o f$ sharing chosen by a social planner, $\beta _ { p } ^ { v } ,$ that leads to maximum security is

$$
\beta_ {p} ^ {v} = \arg \min _ {\beta} P (x _ {e} (\beta), \beta) = 1.
$$

Theorem 2. If complementary information is stored, the optimal level of sharing chosen by a social planner, $\beta _ { p } ^ { c } ,$ that leads to minimum cost is

$$
\beta_ {p} ^ {c} = \arg \min _ {\beta} C (x _ {e} (\beta), \beta) = 1.
$$

The results in Theorems (1) and (2) highlight the fact that there is no lack of incentive for the <sup>fi</sup>rms to share. At the same time, the social planner also views sharing as bene<sup>fi</sup>cial; hence, the equilibrium outcome is the same as the one chosen by the social planner.

## 3.4. Coordinating investment levels

We have seen in the previous section that there is no need to regulate the sharing decision, i.e., sharing is a natural outcome of individual cost minimizing behavior. However, another question of importance is the following: from the perspective of minimizing social cost, is there any need to in<sup>fl</sup>uence the investment decisions made in equilibrium by the <sup>fi</sup>rms? Before we address this question, it is necessary to examine whether the sharing decisions will change if the investment decisions are chosen by the social planner. Since the <sup>fi</sup>rms are similar, we let $\chi _ { i } = \chi _ { j } = x ,$ and $\beta _ { i } = \beta _ { j } = \beta .$ We then rewrite Eq. (3) as

$$
C _ {i} = P (x + \beta \eta x) P (x + \beta \eta x) V + x\tag{8}
$$

The total cost from a social perspective (i.e., social cost) is simply twice each <sup>fi</sup>rm's cost. To minimize social cost, it is therefore suf<sup>fi</sup>cient to minimize Eq. (8). It is easy to see that $\beta = 1$ is still the optimal solution since $P$ decreases in $\beta$ for any value of x. We can therefore conclude that full sharing is an equilibrium outcome as well as the optimal one chosen by a social planner at any level of investment, including the socially optimal one.

We consider a social planner with the objective of minimizing social cost, assuming full sharing. To achieve the optimal investment level, we have

$$
\frac {\partial C _ {i}}{\partial x} = 2 (1 + \eta) P (x + \eta x) P ^ {\prime} (x + \eta x) V + 1 = 0\tag{9}
$$

Let us denote the solution to Eq. (9) by $x ^ { * } ,$ the socially optimal level of investment. Comparing the investment levels obtained from Eqs. (9) and (5), we get the following remark.

Remark 3. At equilibrium, the <sup>fi</sup>rms under-invest from the perspective of minimizing overall cost.

The complementary nature of information assets assumes properties of public goods where we expect under-investment by individual <sup>fi</sup>rms in the absence of coordination. The above remark also implies that some form of coordination by a social planner would bene<sup>fi</sup>t both <sup>fi</sup>rms and also reduce social cost. To <sup>fi</sup>nd such a coordination scheme, we do not recommend schemes that directly control the level of investment at each <sup>fi</sup>rm, as it would be dif<sup>fi</sup>cult for the <sup>fi</sup>rms to agree on the actual investment level at each <sup>fi</sup>rm. Instead, we propose an incident-based scheme that minimizes social cost by relying on the number of breach incidents that can be observed by each <sup>fi</sup>rm. However, to develop such a scheme, we <sup>fi</sup>rst present an investment-based scheme that serves as a benchmark for the more practical incident-based scheme.

## 3.4.1. Investment-based scheme

In this scheme, for an investment amount $x _ { i } ,$ <sup>fi</sup>rm i gets a reward $\gamma ( \boldsymbol { x } _ { i } )$ from <sup>fi</sup>rm j and vice versa. The total cost to <sup>fi</sup>rm i under such a coordination scheme is given by

$$
C _ {i} = P \left(x _ {i} + \eta x _ {j}\right) P \left(x _ {j} + \eta x _ {i}\right) V + x _ {i} + \gamma \left(x _ {j}\right) - \gamma \left(x _ {i}\right)\tag{10}
$$

Firm i's equilibrium condition is given by

$$
\frac {\partial C _ {i}}{\partial x _ {i}} = P ^ {\prime} \left(x _ {i} + \eta x _ {j}\right) P \left(x _ {j} + \eta x _ {i}\right) V + \eta P \left(x _ {i} + \eta x _ {j}\right) P ^ {\prime} \left(x _ {j} + \eta x _ {i}\right) V + 1 - \gamma^ {\prime} (x _ {i}) = 0\tag{11}
$$

Since <sup>fi</sup>rms i and $j$ are similar, at equilibrium, we have $x _ { i } = x _ { j } = x .$ After implementing the coordination scheme $\gamma ( \boldsymbol { x } _ { i } )$ , Eqs. (9) and (11) become equivalent. Thus, we have

$$
\gamma^ {\prime} (x _ {i}) | _ {x _ {i} = x} = - (1 + \eta) P (x + \eta x) P ^ {\prime} (x + \eta x) V\tag{12}
$$

We then solve Eq. (12) to get

$$
\gamma (x) = \frac {V}{2} \left[ 1 - (P (x + \eta x)) ^ {2} \right]\tag{13}
$$

The vulnerability function $P ( x + \eta x )$ decreases as the investment level x increases. Therefore the reward $\gamma ( \boldsymbol { x } )$ increases with the investment leve $x ,$ leading the <sup>fi</sup>rms to invest at the socially optimal level. Under the above coordination scheme, the investment level $x _ { i } ^ { * }$ obtained from Eq. (11) minimizes the social cost in Eq. (8).

To implement the investment-based scheme, an independent third party may be needed to monitor and facilitate the payment exchange process. For instance, the third party can observe <sup>fi</sup>rms' security investment, collect deposits from <sup>fi</sup>rms, and reimburse <sup>fi</sup>rms based on the payments speci<sup>fi</sup>ed by the investment-based scheme. Since investment levels may not be easily observable, the two parties could disagree on the actual investment levels and hence, disturb the equilibrium. Thus a coordination scheme that relies on accurately observing investment levels might lead to opportunism; a <sup>fi</sup>rm has an incentive to invest less and report more. We next use the above coordination scheme to derive an incident-based coordination scheme.

## 3.4.2. Incident-based scheme

Here we propose an alternative coordination scheme based on the total number of security incidents, i.e., the number of penetration events, that can be measured with high precision. In this scheme, a <sup>fi</sup>rm rewards the other <sup>fi</sup>rm for maintaining a secure system. The security of a system is measured by the number of penetration incidents that occur. In addition, unlike investment levels that may include costs that are dif<sup>fi</sup>cult to observe, it is easier to audit a <sup>fi</sup>rm's security log <sup>fi</sup>les to verify the reported number of penetration incidents. In this scheme there is no need to distinguish between security incidents that have occurred as a result of direct traf<sup>fi</sup>c versus those that have occurred from cross traf<sup>fi</sup>c.

We assume that potential security incidents (i.e., attack attempts) arrive following a Poisson distribution with rate λ during a planning horizon T. The number of penetration incidents therefore follows a Poisson distribution with rate λP, where P is the <sup>fi</sup>rm vulnerability. We use k to represent the number of incidents and analyze a reward scheme $\beta ( k )$ that satis<sup>fi</sup>es $E [ \beta ( k ) ] = \gamma ( x )$

$$
E [ \beta (k) ] = \gamma (x) = \frac {V}{2} \Big [ 1 - (P (x + \eta x)) ^ {2} \Big ]\tag{14}
$$

Consider an incident-based scheme of the form $\beta ( k ) = C _ { 0 } + C _ { 1 } k +$ $C _ { 2 } k ^ { 2 }$ . Using the properties of the Poisson distribution, we have $E [ k ] =$ λPT and $E [ k ^ { 2 } ] = ( \lambda P T ) ^ { 2 } + \lambda P T .$ . Substituting E[β(k)] into Eq. (14), we <sup>fi</sup>nd the coef<sup>fi</sup>cients $C _ { i }$ as follows:

$$
C _ {0} = \frac {V}{2}, C _ {1} = \frac {V}{2 \lambda^ {2} T ^ {2}}, a n d C _ {2} = - \frac {V}{2 \lambda^ {2} T ^ {2}}\tag{15}
$$

Thus, <sup>fi</sup>rm i will receive a reward β(k) from <sup>fi</sup>rm j given k penetrations into <sup>fi</sup>rm i's system:

$$
\beta (k) = \frac {V}{2} \left(1 + \frac {k - k ^ {2}}{\lambda^ {2} T ^ {2}}\right)\tag{16}
$$

We can see from the above expression that the reward will increase as the number of penetration decreases, i.e., higher the security level, higher the reward. That means that <sup>fi</sup>rms will have an incentive to invest more to reduce the number of penetrations, leading them to the socially optimal level of investment in equilibrium.

## 3.5. Investment coordination under risk aversion

We also study the case when the two <sup>fi</sup>rms are risk-averse. As before, we begin with the less realistic investment-based scheme and use the results of this analysis to propose an incident-based scheme.

## 3.5.1. Investment-based scheme

Using a common form of a risk-averse exponential utility function [15], we have the utility of <sup>fi</sup>rm i given by

$$
R _ {i} = - e ^ {V P _ {i} P _ {j} + x _ {i}}\tag{17}
$$

To achieve the socially optimal level of investment, $x _ { i } = x _ { j } = x ,$ we get

$$
\frac {\partial R _ {i}}{\partial x _ {i}} = - \left[ 2 (1 + \eta) V P P ^ {\prime} + 1 \right] e ^ {V P ^ {2} + x _ {i}} = 0\tag{18}
$$

In the coordination scheme, <sup>fi</sup>rm i receives payment $\gamma ( x _ { i } )$ , and pays <sup>fi</sup>rm j the amount $\gamma ( \boldsymbol { x } _ { j } )$ . Then <sup>fi</sup>rm i's utility becomes

$$
R _ {i} = - e ^ {V P _ {i} P _ {j} + x _ {i} + \gamma (x _ {j}) - \gamma (x _ {i})}\tag{19}
$$

To <sup>fi</sup>nd the equilibrium investment, we have

$$
\frac {\partial R _ {i}}{\partial x _ {i}} = - \left(V P _ {i} ^ {\prime} P _ {j} + \eta V P _ {i} P _ {j} ^ {\prime} + 1 - \gamma^ {\prime} (x _ {i})\right) e ^ {V P _ {i} P _ {j} + x _ {i} + \gamma (x _ {j}) - \gamma (x _ {i})} = 0\tag{20}
$$

Because the coordination scheme is based upon a deterministic quantity, namely the investment levels, the risk-neutral scheme and the risk-averse scheme are identical

$$
\gamma (x) = - V (P (x + \eta x)) ^ {2} / 2\tag{21}
$$

## 3.5.2. Incident-based Scheme

Here, we develop a reward scheme $\beta ( k _ { i } )$ in which <sup>fi</sup>rm i receives a reward $\beta ( k _ { i } )$ for the number of penetrations $k _ { i }$ at its system. Then we have

$$
R _ {i} = - e ^ {V P _ {i} P _ {j} + x _ {i} + \beta (k _ {j}) - \beta (k _ {i})}\tag{22}
$$

If we can ensure that $E [ e ^ { - \beta ( k _ { i } ) } ] = e ^ { - \gamma ( x _ { i } ) }$ for any given $x _ { i } ,$ then the resulting equilibrium condition $( \partial { R _ { i } } / \partial { x _ { i } } )$ will be exactly the same as Eq. (20). Using an analysis similar to that used in Section 3.4, we have

$$
E \left[ e ^ {- \beta \left(k _ {i}\right)} \right] = \sum_ {k _ {i} = 0} ^ {\infty} e ^ {- \beta \left(k _ {i}\right)} \frac {e ^ {- \lambda P T} (\lambda P T) ^ {k _ {i}}}{k _ {i} !}\tag{23}
$$

Using a Taylor Series expansion of $e ^ { - \gamma ( x _ { i } ) } ,$ , and taking the <sup>fi</sup>rst n terms, we get

$$
e ^ {- \gamma (x _ {i})} = \sum_ {i = 1} ^ {n} \frac {\left(V P ^ {2} / 2\right) ^ {i - 1}}{(i - 1) !}\tag{24}
$$

Then, using $\begin{array} { r } { \beta ( k _ { i } ) = - L o g ( 1 + \sum _ { w = 2 } ^ { n } C _ { w } \prod _ { m = 0 } ^ { 2 w - 3 } ( k _ { i } - m ) ) } \end{array}$ and substituting this expression into Eq. (23), we solve the coef<sup>fi</sup>cients $C _ { w } ( w = 2 , . . . , n )$ by equating Eqs. (23) and (24). Finally, we get

$$
\beta \left(k _ {i}\right) = - \operatorname{Log} \left(1 + \sum_ {w = 2} ^ {n} \left[ \frac {(V / 2) ^ {w - 1}}{(w - 1) ! (\lambda T) ^ {2 (w - 1)}} \prod_ {m = 0} ^ {2 w - 3} \left(k _ {i} - m\right) \right]\right)\tag{25}
$$

For a speci<sup>fi</sup>c functional form $P ,$ we can substitute Eq. (25) into $\operatorname { E q . } \left( 2 2 \right)$ and solve for the optimal x<sup>∗</sup> by minimizing the expected value of $R _ { i } .$ We can then compare x<sup>∗</sup> with $x ^ { * }$ (which can be obtained from Eq. (9)) to check the accuracy of the Taylor series approximation and use a suf<sup>fi</sup>cient number of terms to obtain an accurate result. For illustration purposes, consider the speci<sup>fi</sup>c vulnerability functional form $P _ { i } = a / [ 1 + b ( x _ { i } + \eta x _ { j } ) ]$ . In this form, a is the initial probability of threat without any investment, and b a scaling factor associated with the impact of security investments on the breach probability. We let $a = 0 . 1 , b = 0 . 1 , \eta = 0 . 5$ and V=5000. At the social optimum, each <sup>fi</sup>rm's investment level is $x ^ { * } = 1 4 . 0 5$ . Without any coordination, each <sup>fi</sup>rm's equilibrium investment choice $\mathrm { i } s x _ { e } = 9 . 7 7$ , representing an under-investment. Fig. 2 below shows the relationship between x<sup>∗</sup> and n, the number of terms used in Taylor expansion Eq. (24). We can see that, when $n = 5 , x _ { i } ^ { * } = 1 2 . 7 5$ and when $n = 1 0 , x _ { i } ^ { * } = 1 3 . 9 7$ , which is very close to the socially optimal value $x ^ { * } = 1 4 . 0 5$ . Fig. 2 shows that the approximation works very well.

## 4. Substitutable information

In the substitutable information case, once one of the <sup>fi</sup>rms has been compromised, there is little incentive for hackers to attack the other <sup>fi</sup>rm. However, if the <sup>fi</sup>rst attack fails, the other <sup>fi</sup>rm will likely be attacked next. In Section 4.1, we consider two <sup>fi</sup>rms that simultaneously make sharing and investment decisions. Unlike the complementary case, we show in Section 4.2 that the <sup>fi</sup>rms do not naturally share and would bene<sup>fi</sup>t from sharing regulation. In Section $4 . 3 ,$ we examine comparative statics under regulated sharing and in Section 4.4, we develop schemes to coordinate security investment levels under regulated sharing.

![](/api/attachments/B7Y2B9E5/fulltext/images/4750afc5a0ff3baa0fdd63c97b53cd80ac10d6dc3398020b87111fdbcad27ce3.jpg)  
Fig. 2. Accuracy of approximation

## 4.1. Investment and sharing: simultaneous Equilibrium

Here, we consider two <sup>fi</sup>rms that simultaneously make sharing decisions and security investment decisions. As before, because we assume no prior vulnerability information, each <sup>fi</sup>rm will be attacked with probability 1/2. We use U to represent the cost of information loss when a <sup>fi</sup>rm is compromised. Here, we assume that the <sup>fi</sup>rm that is responsible for leaking the information will be held liable. Thus while the other <sup>fi</sup>rm could hurt, its loss would be covered by the <sup>fi</sup>rm that was responsible for leaking the information. The expected cost for <sup>fi</sup>rms i is:

$$
C _ {i} = \frac {1}{2} P \left(x _ {i} + \beta_ {j} \eta x _ {j}\right) U + \frac {1}{2} P \left(x _ {i} + \beta_ {j} \eta x _ {j}\right) \left(1 - P \left(x _ {j} + \beta_ {i} \eta x _ {i}\right)\right) U + x _ {i}\tag{26}
$$

The <sup>fi</sup>rst term represents the loss from a direct attack on <sup>fi</sup>rm i, the second term the loss due to cross traf<sup>fi</sup>c from <sup>fi</sup>rm $i ,$ and the last term the cost of investment in information security. The cost function associated with <sup>fi</sup>rm $j$ is symmetric to Eq. (26). Since the breach probability $P$ decreases in $\beta _ { i } ,$ , it is clear from Eq. (26) that $\partial C _ { i } / \partial \beta _ { i } { > } 0$ Thus to minimize $C _ { i }$ we have $\beta _ { i } = 0$ . Similarly, we have $\beta _ { j } = 0$ for <sup>fi</sup>rm j. Thus, we have the following remark.

Remark 4. If substitutable information assets are stored, then (No Share, No Share), i.e., $\beta _ { i } = \beta _ { j } = 0 ,$ is the Nash Equilibrium.

Unlike the case of complementary information assets, with the substitutable information assets, if <sup>fi</sup>rm j shares knowledge with <sup>fi</sup>rm i, <sup>fi</sup>rm i becomes less vulnerable. As a result, there will be more crosstraf<sup>fi</sup>c from <sup>fi</sup>rm i toward <sup>fi</sup>rm $j ,$ thus hurting <sup>fi</sup>rm j. Given <sup>fi</sup>rm i's investment and sharing decisions, <sup>fi</sup>rm j always chooses not to share, i.e., not sharing is a dominant strategy for <sup>fi</sup>rm j. The same is true for <sup>fi</sup>rm i. Therefore, (No Share, No Share), i.e., $\beta _ { i } = \beta _ { j } = 0 ,$ , is a stable outcome.

## 4.1.2. Comparative statics: Simultaneous game

Here we focus on the impact of the cost of information loss(U) on the equilibrium level of investment, security, and total cost. Note that since the <sup>fi</sup>rms do not share in equilibrium, there is no need to analyze the impact of the sharing effectiveness. We begin with a discussion on how the equilibrium level of investment changes when the cost of information loss increases. At equilibrium, we have

$$
\frac {d x _ {e}}{d U} = \frac {- (2 - P) P ^ {\prime}}{2 P ^ {\prime \prime} - \left[ P P ^ {\prime \prime} + (P ^ {\prime}) ^ {2} \right]}
$$

The numerator is positive, but the sign of the denominator is indeterminate. However, for a vulnerability function that satis<sup>fi</sup>es $P ^ { \prime \prime } ( y ) [ 1 - P ( y ) ] { > } [ P ^ { \prime } ( y ) ] ^ { 2 }$ at equilibrium, we can conclude that the equilibrium level investment increases with the cost of information loss. This observation is quite intuitive: more important information assets demand more security investment. This <sup>fi</sup>nding also holds for the case of complementary information assets.

The condition $P ^ { \prime \prime } ( y ) [ 1 - P ( y ) ] { > } [ P ^ { \prime } ( y ) ] ^ { 2 }$ can be easily veri<sup>fi</sup>ed for any speci<sup>fi</sup>c form of the breach probability function P. However, this condition should not be dif<sup>fi</sup>cult to meet for most reasonable forms of the breach probability function. For example, consider a decreasing convex form of the kind $P ( y ) = 1 / ( 1 + y ) ^ { a } ,$ , a N 0. For this form, it is easy to show that the condition $P ^ { \prime \prime } ( y ) [ 1 - P ( y ) ] { > } [ P ^ { \prime } ( y ) ] ^ { 2 }$ would be met if the breach probability at equilibrium is lower than 0.5. For most forms of P that are convex decreasing, the condition would be met unless the equilibrium breach probability is very high — typical values of this probability, on the other hand, can be expected to be less than 0.05.

We next consider the impact of U on the equilibrium security level. We have d $P _ { e } / d U = ( d P _ { e } / d x _ { e } ) \bullet ( d x _ { e } / d U )$ . Since $d P _ { e } / d x _ { e } { < } 0$ , and $d x _ { e } / d U { > } 0$ we conclude that $d P _ { e } / d U { < } 0 ,$ , i.e., the equilibrium security level of each <sup>fi</sup>rm increases with the cost of information loss. Similar to the case of complementary assets, it can also be shown that the total equilibrium cost increases with the cost of information loss, U. Thus, $d C _ { e } / d U > 0 ,$ implying that the new equilibrium overall cost will always be higher with an increase in the cost of information loss.

## 4.2. Sharing regulation

Similar to the analysis in the complementary case, here we examine whether it is necessary to regulate sharing decisions from the perspective of a social planner. As before, the social planner may have different goals such as, security maximization or social cost minimization. Once again, we <sup>fi</sup>nd that there is no need for regulation if the objective of the social planner is to maximize the security level. This result is stated in the theorem below.

Theorem 3. For a vulnerability function that satisfies $P ^ { \prime \prime } ( y ) [ 1 - P ( y ) ] >$ $[ P ^ { \prime } ( y ) ] ^ { 2 } ($ at equilibrium, the optimal level of sharing chosen by a social planner, $\beta _ { p } ^ { v } ,$ that leads to maximum security is

$$
\beta_ {p} ^ {v} = \arg \min _ {\beta} P (x _ {e} (\beta), \beta) = 0.
$$

The result arises from the fact that <sup>fi</sup>rms become less secure when they share more security knowledge, i.e., $\mathrm { d P } / d \beta { > } 0 ,$ , opposite to the result in the complementary case. Thus, from the perspective of maximizing the security level, the social planner would choose the same sharing decision as what the <sup>fi</sup>rms would choose at equilibrium. Hence, similar to the complementary case, no regulation is needed for maximizing the security level. With more information sharing, <sup>fi</sup>rms can lower their security levels and reduce cost. This cost implication is further described in the next theorem.

Unlike the case of complementary information assets, the substitutable nature of assets changes the regulatory role played by a social planner attempting to minimize the social cost. From the social planner's standpoint, since the <sup>fi</sup>rms are similar, minimizing each individual <sup>fi</sup>rm's cost, is equivalent to minimizing the social cost. Let θ represent the effective sharing level, $\theta > = \beta \eta .$ . Note that the cost function in Eq.(26can be expressed as a function of θ alone. Let $\mathfrak { \theta } _ { 0 } \mathfrak { b } \mathfrak { e }$ the solution to the equation $d C e / d \theta = 0 ,$ , and θ<sup>∗</sup>be the value of θ that minimizes the social cost, subject to the constraint that θ∈[0, 1]. In Appendix $\mathsf { A } ,$ we show that $\theta ^ { * } { = } \operatorname { M i n } ( \theta _ { 0 } , 1 )$ . Next, we determine the optimal sharing level $\beta _ { p } ^ { c }$ as summarized below.

Theorem 4. The optimal level of sharing chosen by a social planner, $\beta _ { p } ^ { c } ,$ that minimizes social costs, where

$$
\beta_ {p} ^ {c} = \arg \min _ {\beta} C (x _ {e} (\beta), \beta)
$$

is given by $\theta ^ { * } / \eta i f \eta { > } \theta ^ { * } ; \beta _ { p } ^ { c } { = } 1$ otherwise.

Comparing the results of Theorem4 andRemark 4, we can conclude that sharing regulation should always be needed since the simultaneous equilibrium sharing level is always zero.

## 4.3. Comparative statics under socially optimal sharing

In this section, we consider two <sup>fi</sup>rms that are regulated to share at the social cost minimizing level $\beta _ { p } ^ { c }$ and examine how the investment level, security level, and total cost change as the sharing effectiveness increases. The equilibrium level of investment x is given by:

$$
\frac {\partial C _ {i}}{\partial x _ {i}} = \frac {U}{2} P ^ {\prime} \left(x _ {i} + \beta_ {p} ^ {c} \eta x _ {j}\right) \left(2 - P \left(x _ {j} + \beta_ {p} ^ {c} \eta x _ {i}\right) - \beta_ {p} ^ {c} \eta P \left(x _ {j} + \beta_ {p} ^ {c} \eta x _ {i}\right)\right) + 1 = 0\tag{27}
$$

## 4.3.1. Optimal level of sharing

We examine how the level of sharing chosen by a social planner will be affected by the sharing effectiveness. One might expect that the social planner chooses a higher level of sharing as the sharing effectiveness increases. However, upon analysis we <sup>fi</sup>nd the exact opposite can be true. This is because sharing level and sharing effectiveness can be complements with respect to achieving the optimal effective sharing level $\theta _ { p } ^ { c } ,$ given by $\operatorname { M i n } ( \theta ^ { * } , \eta )$

Recall that the effective sharing level is chosen optimally by the social planner to minimize the social cost, subject to constraint that $\theta , \beta \in [ 0 , 1 ] .$ When the sharing effectiveness is high $( \eta { > } \theta ^ { * } )$ , then the sharing level prescribed by the social planner $( \beta _ { p } ^ { c } = \theta ^ { * } / \eta )$ decreases with the sharing effectiveness. On the other hand, when the sharing effectiveness is relatively low $( \eta { \le } \theta ^ { * } )$ , the optimal sharing level has to be set at its (maximum) boundary value, i.e., $\beta _ { p } ^ { c } { = } 1$ , to achieve the best solution.

## 4.3.2. Investment level

We are interested in determining the sign of $d x _ { e } / d \eta$ given by

$$
d x _ {e} / d \eta = \left(d x _ {e} / d \theta_ {p} ^ {c}\right) \left(d \theta_ {p} ^ {c} / d \eta\right)
$$

Using Eq. (27), we can write

$$
\frac {d x _ {e}}{d \theta_ {p} ^ {c}} = \frac {- \left[ 2 - \left(1 + \theta_ {p} ^ {c}\right) P \right] x _ {e} P ^ {\prime \prime} + \left[ P + \left(1 + \theta_ {p} ^ {c}\right) P ^ {\prime} x _ {e} \right] P ^ {\prime}}{\left[ 2 - \left(1 + \theta_ {p} ^ {c}\right) \right] \left(1 + \theta_ {p} ^ {c}\right) P ^ {\prime \prime} - (P ^ {\prime}) ^ {2} \left(1 + \theta_ {p} ^ {c}\right) ^ {2}}
$$

The sign of $d x _ { e } / d \theta _ { p } ^ { c }$ is indeterminate; however, for a vulnerability function that satis<sup>fi</sup>es $P ^ { \prime \prime } ( y ) [ 1 - P ( y ) ] { > } [ P ^ { \prime } ( y ) ] ^ { 2 }$ at equilibrium, we show in Appendix A that the equilibrium investment level decreases with the sharing effectiveness, $\mathrm { i } . \mathbf { e } . , d x _ { e } / d \theta _ { p } ^ { c } { < } 0 .$

To determine the sign of $d \theta _ { p } ^ { c } / d \eta ,$ , when $\eta { > } { \theta } ^ { * }$ , we have $\beta _ { p } ^ { c } { = } \theta ^ { * } / \eta ,$ the value of $\theta _ { p } ^ { c }$ will stay at $\theta ^ { * } ,$ , and thus $d \theta _ { p } ^ { c } / d \eta = d x _ { e } / d \eta = 0 ,$ i.e., the equilibrium investment level will not change with the sharing effectiveness; when $\eta \leq \theta ^ { * }$ , we have $\beta _ { p } ^ { c } = 1 , ~ \theta _ { p } ^ { c } = \eta ,$ , and thus $d \theta _ { p } ^ { c } /$ $d \eta = 1$ , and $d x _ { e } / d \eta { < } 0 , \mathrm { i . e . }$ , the equilibrium investment level decreases with the sharing effectiveness.

The impact of sharing effectiveness on the optimal value of the sharing level $( d \theta _ { p } ^ { c } / d \eta )$ can be explained as follows. When the sharing effectiveness is greater than $\theta ^ { * } ,$ the optimal sharing level $\beta _ { p } ^ { c }$ can be adjusted (i.e., lowered) as the sharing effectiveness η increases to ensure that the effective sharing level is held at the optimal value, $\theta _ { p } ^ { c } { = } \theta ^ { * }$ . On the other hand, when the sharing effectiveness is less than or equal to θ<sup>∗</sup>, the optimal effective sharing level, $\theta _ { p } ^ { c } { < } \theta ^ { * }$ , because $\beta \le 1$ Hence, as the sharing effectiveness increases (but remains below θ<sup>∗</sup>), there is no impact on the optimal sharing level, i.e., $\beta _ { p } ^ { c } = 1$

We next explain why the investment level can reduce with an increase in sharing effectiveness $( \mathrm { i } . \mathrm { e } . , d x _ { e } / d \eta < 0 )$ . Note that this effect can be observed only when η is relatively high, $\mathrm { i . e . , } \ \eta { > } \theta ^ { \ast } .$ . As the sharing effectiveness increases, from the perspective of lowering <sup>fi</sup>rm $i \prime s$ self-breach probability $P ( x _ { i } + \beta _ { j } \eta x _ { j } )$ , the marginal value of $x _ { i }$ decreases. Thus, based on the self-breach force, <sup>fi</sup>rm i has an incentive to invest less. Furthermore, the investment at <sup>fi</sup>rm i increases <sup>fi</sup>rm $j ^ { \prime } s$ security, leading to an increase in the de<sup>fl</sup>ected traf<sup>fi</sup>c toward <sup>fi</sup>rm i from <sup>fi</sup>rm j. Therefore <sup>fi</sup>rm i has another reason to invest less. Note that this result is in direct contrast with the complementary case, where the equilibrium level of investment $\left( x _ { e } \right)$ can increase or decrease with the sharing effectiveness depending on the cost of information loss.

## 4.3.3. Security level

Intuitively, we would expect that <sup>fi</sup>rms would become more secure when sharing is more effective; however, our analysis shows that this is not true. For a vulnerability function that satis<sup>fi</sup>es $P ^ { \prime \prime } ( y ) [ 1 - P ( y ) ]$ N $[ P ^ { \prime } ( y ) ] ^ { 2 }$ at equilibrium, we have shown in Appendix A that a <sup>fi</sup>rm's security decreases with the effective sharing level, $\mathrm { i } . \mathrm { e } . , \ d P _ { e } / d \theta _ { p } ^ { c } { > } 0 .$ When ηNθ<sup>∗</sup>, $\theta _ { p } ^ { c } { = } \theta ^ { * }$ , a constant. Hence, we have $d \theta _ { p } ^ { c } / d \eta = 0 ,$ , and thus $d P _ { e } / d \eta { = } ( d P _ { e } / d \theta _ { p } ^ { c } ) ( d \theta _ { p } ^ { c } / d \eta ) { = } 0$ , i.e., the equilibrium security level does not change with the sharing effectiveness. When $\eta \leq \theta ^ { * }$ , we have $\theta _ { p } ^ { c } { = } \eta .$ . Hence, $d \theta _ { p } ^ { c } / d \eta = 1$ , and thus $d P _ { e } / d \eta = ( d P _ { e } / d \theta _ { p } ^ { c } ) ( d \theta _ { p } ^ { c } / d \eta ) =$ $d P _ { e } / d \theta _ { p } ^ { c } { > } 0 ,$ i.e., the equilibrium security level decreases with the sharing effectiveness.

It is surprising to see that when the sharing effectiveness is below a certain threshold, an increase in sharing effectiveness could reduce the security level. An increased in the sharing effectiveness has two opposing effects. On the one hand, <sup>fi</sup>rm i could bene<sup>fi</sup>t from a lower self-breach probability $P ( x _ { i } + \beta _ { j } \eta x _ { j } )$ holding x constant. On the other hand, because de<sup>fl</sup>ected traf<sup>fi</sup>c reduces as <sup>fi</sup>rm j becomes more vulnerable, <sup>fi</sup>rm i has an incentive to lower its investment level in order to make <sup>fi</sup>rm j more vulnerable. The second effect dominates the <sup>fi</sup>rst and hence, the <sup>fi</sup>rm's security level decreases. However, when η is greater than the threshold, the optimal effective sharing level, $\theta _ { p } ^ { c }$ stays the same. Thus the security investment and the security level remain unchanged. This result is opposite to that in the complementary case, where the security level increases with sharing effectiveness.

## 4.3.4. Total cost

The total cost to each <sup>fi</sup>rm is the sum of the breach cost and the investment cost. We have the following result.

Theorem 5. As the sharing effectiveness increases, the total cost to each firm stays the same or decreases depending on the sharing effectiveness.

We have shown that when the sharing effectiveness is relatively low $( \mathrm { i } . \mathrm { e } . , \eta { < } \theta ^ { \ast } )$ , an increase in the sharing effectiveness leads to a lower security level, but at the same time, the investment in security is also lower. Theorem 5 shows that when the sharing effectiveness is suf<sup>fi</sup>ciently low $( \eta < \theta ^ { * } )$ , the total cost monotonically decreases as the sharing effectiveness increases. This effect occurs because the fall in the equilibrium investment level dominates the increase in the penetration cost. On the other hand, when the sharing effectiveness is greater than the threshold, the optimal sharing level will be adjusted to minimize the total cost, and thus the total cost will stay constant at the minimal level.

## 4.4. Coordinating investment levels

Here, we examine whether there is any need to in<sup>fl</sup>uence the investment decisions made in equilibrium by the <sup>fi</sup>rms from the perspective of minimizing the social cost, and if there is, how to achieve this goal. Before we enter this discussion, it is necessary to know whether regulation on sharing decisions would change if the investment decisions are chosen by the social planner under the objective of minimizing the social cost. The relevant result concerning this issue is provided below.

Theorem 6. In the substitutable case, when both sharing and investment decisions are chosen to minimize social cost, then the optimal level of sharing is (Full Share, Full Share), i.e., $\beta _ { i } = \beta _ { j } = 1$

As we can see from Theorem6, if investment decisions are centrally made, then it is optimal that the <sup>fi</sup>rms share fully. On the other hand, recall from Theorem 4 that when the social planner only controlled the level of sharing (i.e., the investments decisions were left to the <sup>fi</sup>rms) then interior solutions for the level of sharing $( \beta _ { p } ^ { c } \le 1 )$ were possible. The presence of an interior solution reveals an interesting insight when contrasted with the corner solution $( \beta = 1 )$ that is always optimal when both the sharing and investment decisions are chosen by the social planner to minimize social cost. The lower level of sharing chosen by the social planner when investment decisions are left to the <sup>fi</sup>rms occurs because the social planner needs to guard against competitive behavior by <sup>fi</sup>rms: one <sup>fi</sup>rm tries to increase its investment in order to hurt the other <sup>fi</sup>rm. Such harmful behavior is most productive when sharing is at its fullest. Hence the social planner must sacri<sup>fi</sup>ce the bene<sup>fi</sup>ts of full sharing to protect the <sup>fi</sup>rms from hurting one another.

If a coordination scheme were in place to guide investment decisions that minimize social cost, the social planner would recommend full sharing. Hence, we develop a coordination scheme under the condition that the <sup>fi</sup>rms share fully. Since the two <sup>fi</sup>rms are similar, we consider a symmetric solution where $x _ { i } = x _ { j } = \mathbf { X } .$ The cost to <sup>fi</sup>rm i is given by

$$
C _ {i} = \frac {1}{2} P (x + \eta x) (2 - P (x + \eta x)) U + x\tag{28}
$$

To achieve the optimal investment level, we have

$$
\frac {\partial C _ {i}}{\partial x} = (1 + \eta) (1 - P (x + \eta x)) P ^ {\prime} (x + \eta x) U + 1 = 0\tag{29}
$$

We conclude the following.

Theorem 7. Under full sharing, when <sup>fi</sup>rms make their own investment decisions, they over-invest when sharing effectiveness is low $( \eta < \eta _ { 1 } )$ and under-invest when sharing effectiveness is high $( \eta > \eta _ { 1 } )$

The value of the threshold η is provided in Appendix A. Similar to the complementary case, we <sup>fi</sup>rst present an investment-based scheme that is less realistic, but serves as a precursor to arrive at the more practical incident-based scheme.

## 4.4.1. Investment-based scheme

We propose the following coordination scheme that minimizes social cost under full sharing: for the security investment o $\dot { \boldsymbol { x } } _ { i } ,$ <sup>fi</sup>rm i pays <sup>fi</sup>rm j the amount γ(x ), and vice versa. The total cost to <sup>fi</sup>rm i is:

$$
C _ {i} = \frac {1}{2} P (x _ {i} + \eta x _ {j}) U + \frac {1}{2} P (x _ {i} + \eta x _ {j}) (1 - P (x _ {j} + \eta x _ {i})) U + x _ {i} + \gamma (x _ {i}) - \gamma (x _ {j})\tag{30}
$$

At equilibrium, we have $\begin{array} { r } { \frac { \partial C _ { i } } { \partial x _ { i } } = 0 } \end{array}$ . Letting $\chi _ { i } = \chi _ { j } = x ,$ we have

$$
P ^ {\prime} (x + \eta x) U - \frac {1}{2} (1 + \eta) P ^ {\prime} (x + \eta x) P (x + \eta x) U + 1 + \gamma^ {\prime} (x) = 0 (3 1)
$$

Also, $x _ { i } = x _ { j } = x ,$ where x should satisfy Eq. (29). To minimize social cost, x should satisfy both Eqs. (29) and (31). Therefore, we have

$$
\gamma^ {\prime} (x) = P ^ {\prime} (x + \eta x) U \left[ \eta - \frac {(1 + \eta) P (x + \eta x)}{2} \right]
$$

Then, we have

$$
\gamma (x) = U \bigg [ \frac {\eta}{1 + \eta} P (x + \eta x) - \frac {(P (x + \eta x)) ^ {2}}{4} \bigg ]\tag{32}
$$

We can see that γ(x) increases with x when η is small, i.e., $\mathrm { i f } \eta < \eta _ { 2 } ,$ then $\gamma \ ^ { \prime } ( x ) { > } 0 ,$ , where the threshold value $\eta _ { 2 }$ satis<sup>fi</sup>es the equation $\eta - ( 1 + \eta ) P ( x + \eta x ) / 2 = 0 .$ . We show in Appendix A that the value of $\eta _ { 1 }$ (in Theorem 7) is the same as $\eta _ { 2 } .$ Over-investment by a <sup>fi</sup>rm leads to a higher payment, thus lowering the tendency to over-invest. However, when η is large $( \eta > \eta _ { 2 } )$ , the proposed scheme would make the payment $\gamma ( \boldsymbol { x } )$ decrease with an increase in investment (i.e., $\gamma ^ { \prime } \left( x \right) < 0 )$ , thus correcting the tendency to under-invest.

## 4.4.2. Incident-based scheme

We next propose an alternative coordination scheme based on the number of security incidents that can be measured with relatively high precision. Denoting the number of security incidents recorded at <sup>fi</sup>rm i by k, a random variable, <sup>fi</sup>rm i's payment satis<sup>fi</sup>es E $[ \beta ( k ) ] = \gamma ( x _ { i } )$ for any given $x _ { i \cdot }$ Note that unlike the scheme proposed in Section 3.4, the current scheme requires making a payment, rather than receiving a reward when security incidents occur.

$$
\beta (k) = \frac {- U}{4 \lambda^ {2} T ^ {2}} k ^ {2} + \left[ \frac {\eta}{(1 + \eta) \lambda T} + \frac {1}{4 \lambda^ {2} T ^ {2}} \right] U k\tag{33}
$$

In the low η region, as k increases, the payment β(k) will decrease. Therefore in this region, <sup>fi</sup>rms will have an incentive to reduce their investment level to incur less payment $\beta ( k )$ . The over-investment is therefore recti<sup>fi</sup>ed through the payment scheme $\beta ( k ) . \operatorname { I f } \eta$ is very high, as k increases, the payment could increase for small $k ,$ but decrease for large k. However, the expected value of the payment β(k) always increases for high η. This means that the expected payment increases with a decrease in investment, thus preventing the under-investment problem in the high η region.

Finally, if the <sup>fi</sup>rms are risk averse, using an analysis similar to that in Section 3.5, a coordination scheme that considers risk-aversion can be easily developed.

## 5. Concluding remarks

This paper emphasizes the importance of jointly considering the incentives of hackers and the nature of information assets being protected in managing the information system security of a <sup>fi</sup>rm. A <sup>fi</sup>rm must consider whether the information it is trying to protect is of value to a hacker by itself, or whether its value is realized only if the <sup>fi</sup>rm's information is combined with the information stored at another <sup>fi</sup>rm. The so-called complementary case – one where the information provides value to hackers only if it is combined with information from another <sup>fi</sup>rm – provides a natural incentive for <sup>fi</sup>rms to collaborate with one another on security intelligence, i.e., sharing of security knowledge that makes both <sup>fi</sup>rms more secure. Therefore, no regulation or external encouragement to induce <sup>fi</sup>rms to share is needed when complementary assets are being protected. This <sup>fi</sup>nding is relevant from the perspective of a social planner: there is no need to regulate the sharing behavior of the <sup>fi</sup>rms irrespective of whether the social planner's goal is to minimize social costs or to maximize <sup>fi</sup>rm security.

However, while sharing is naturally encouraged in the complementary case, the extent of investment made by each <sup>fi</sup>rm falls short of the socially optimal level. In other words, when left alone, <sup>fi</sup>rms underinvest in security. This feature of the equilibrium in the complementary case is an example of “The Tragedy of the Commons.” Aristotle once said: “That which is common to the greatest number has the least care bestowed upon it.” To correct this under-investment, we proposed investment-based and incident-based schemes to coordinate the <sup>fi</sup>rms so as to achieve optimal social welfare (i.e., minimize social cost).

In the substitutable case, it is socially optimal for two <sup>fi</sup>rms to share; however, in equilibrium the <sup>fi</sup>rms engage in a sharing outcome that is similar to the Prisoners' Dilemma: although each <sup>fi</sup>rm would like its partner to share, the dominant strategy is not to share. Thus, the equilibrium outcome is (Not Share, Not Share). This outcome is both individually and socially harmful, calling for external encouragement or inducement (e.g., a tax break provided to <sup>fi</sup>rms if they share) for sharing. The social planner who cares about minimizing social cost recommends the <sup>fi</sup>rms to share, albeit, typically not at the fullest level. While full sharing is optimal if the investment decision is also made by the social planner, it is usually desirable to lower sharing levels if investment decisions are left to the <sup>fi</sup>rms. This is done to protect the <sup>fi</sup>rms from hurting one another: by lowering its investment level one <sup>fi</sup>rm can make the other <sup>fi</sup>rm less secure and a more attractive target for hackers. Similar to the complementary case, we proposed two coordination schemes that minimized social costs. However, in the substitutable case, the coordination scheme was designed to correct for over-investment when the sharing effectiveness is relatively low and correct for underinvestment, otherwise. Thus the substitutable case sometimes exhibited the characteristics of an “Arms Race” whereas at other times the “Tragedy of Commons” was enacted.

An extension that suggests itself is to consider a network of <sup>fi</sup>rms that share knowledge in the sense of an industry alliance. Here the pure extremes of complementary versus substitutable assets get blurred and the existence of asymmetries between <sup>fi</sup>rms becomes important to consider, i.e., while two <sup>fi</sup>rms could be similar, it is unlikely that all <sup>fi</sup>rms in a large group of <sup>fi</sup>rms share the same security characteristics. Another extension is to consider a strategic vendor in the problem, for example one that actively participates in coordination related payments to form a three-way equilibrium between the <sup>fi</sup>rms and a vendor. At a more micro level, some of the ideas in this paper can aid in the design of a security architecture that exploits the analogy between parallel (sequential) structures and the substitutable (complementary) case. Finally, the ideas developed here can also be extended to the (vertical and horizontal) partitioning of database tables to achieve a security objective.

## Appendix A

Proof of $\bf { d } P _ { e } / \bf { d } \eta \mathrm { < } 0 .$ Complementary case.

Let y =x+ ηx. Taking the total differential of Eq. (5) with respect to η, we can get

$$
\frac {d y}{d \eta} = \frac {1}{(1 + \eta) ^ {2} V \left\{\left[ P ^ {\prime} (y) \right] ^ {2} + P (y) P ^ {\prime \prime} (y) \right\}} > 0\tag{34}
$$

Therefore we have $d P ( y ) / d \eta { = } P ^ { \prime } ( y ) d y / d \eta { < } 0$ since $P ^ { \prime } ( y ) { < } 0 .$ . We can conclude that, in the complementary case, then as the sharing effectiveness increases, each <sup>fi</sup>rm becomes more secure. □

Proof of $\mathbf { d C } _ { e } / \mathbf { d } \eta { < } \mathbf { 0 } .$ . Complementary case.

Let $y = x + \eta x .$ . From Eq. (3), when $\beta _ { i } = \beta _ { j } = 1$ , we can get

$$
\frac {d C _ {i}}{d \eta} = 2 P (y) P ^ {\prime} (y) \frac {d y}{d \eta} V + \frac {d x}{d \eta} = \frac {d y}{d \eta} \bigg [ 2 P (y) P ^ {\prime} (y) V + \frac {1}{1 + \eta} \bigg ] - \frac {x}{1 + \eta}\tag{35}
$$

Substituting Eq. (5) into Eq. (35), we have

$$
\frac {d C _ {i}}{d \eta} = - \frac {1}{1 + \eta} \frac {d y}{d \eta} - \frac {x}{1 + \eta}\tag{36}
$$

which is negative since we have dy/dηN0 from Eq. (34).

Proof of Theorem 1. At equilibrium, we have ${ \boldsymbol x } _ { i } = { \boldsymbol x } _ { j } = { \boldsymbol x } _ { e } ,$ and $\beta _ { i } = \beta _ { j } = \beta .$ . Letting $y = x _ { e } + \beta \eta x _ { e } ,$ , we have

$$
P ^ {\prime} (y) P (y) = \frac {- 1}{(1 + \beta \eta) V}\tag{37}
$$

Taking the total differential of Eq. (37) with respect to β, we can get

$$
\frac {d y}{d \beta} = \frac {\eta}{(1 + \beta \eta) ^ {2} V \left\{\left[ P ^ {\prime} (y) \right] ^ {2} + P (y) P ^ {\prime \prime} (y) \right\}} > 0\tag{38}
$$

Since $P ^ { \prime } ( y ) { < } 0 ,$ , we can further conclude that $d P ( y ) / d \beta = P ^ { \prime } ( y ) d y / d \beta < 0 ,$ which means that in the complementary case, when the sharing level increases, each <sup>fi</sup>rm becomes more secure. Thus, to achieve the maximum level of security, <sup>fi</sup>rms should share fully.

Proof of Theorem 2. Let $y = x + \beta \eta x .$ . From Eq. (3), we can get

$$
\begin{array}{l} \frac {d C _ {i}}{d \beta} = 2 P (y) P ^ {\prime} (y) \frac {d y}{d \beta} V + \frac {d x}{d \beta} \\ = \frac {d y}{d \beta} \left[ 2 P (y) P ^ {\prime} (y) V + \frac {1}{1 + \beta \eta} \right] - \frac {\eta x}{1 + \beta \eta} \end{array}\tag{39}
$$

Substituting the equilibrium condition, i.e., $2 P ( y ) P ^ { \prime } ( y ) V + 1 / ( 1 +$ $\beta \eta ) = 0 ,$ into Eq. (39), we have,

$$
\frac {d C _ {i}}{d \beta} = - \frac {1}{1 + \beta \eta} \frac {d y}{d \beta} - \frac {\eta x}{1 + \beta \eta}\tag{40}
$$

which is negative since we have $d y / d \beta > 0$ from Eq. (38). Thus, <sup>fi</sup>rms should fully share security knowledge to minimize the social cost.

Proof of Remark 3. Let $B ( y ) = ( 1 + \eta ) P ( y ) P ^ { \prime } ( y ) V + 1 , y _ { e } = ( 1 + \eta ) x _ { e } ,$ and $y ^ { * } = ( 1 + \eta ) x ^ { * }$ . We could rewrite Eqs. (5) and (9) as

$$
B (y _ {e}) = 0
$$

$$
B \left(y ^ {*}\right) = - (1 + \eta) P \left(x ^ {*} + \eta x ^ {*}\right) P ^ {\prime} \left(x ^ {*} + \eta x ^ {*}\right) > 0
$$

Since $B ^ { \prime } ( y ) { > } 0 ,$ , we conclude that $y ^ { * } { > } y _ { e } ,$ which indicates that $x ^ { * } { > } x _ { e } .$ Proof of Theorem 3. Since <sup>fi</sup>rms i and j are similar, at equilibrium, we $\begin{array} { r } { \mathrm { g e t } \frac { \partial C _ { i } } { \partial x _ { i } } = 0 } \end{array}$ and then let $x _ { i } = x _ { j } = x _ { e }$ and $\beta _ { i } = \beta _ { j } = \beta .$ With $y = x _ { e } +$ $\beta \eta x _ { e } ,$ we have

$$
P ^ {\prime} (y) (2 - P (y)) U - \beta \eta P (y) P ^ {\prime} (y) U + 2 = 0\tag{41}
$$

Taking total derivative with respect to $\beta ,$ we can get

$$
\frac {d y}{d \beta} = \frac {\eta P (y) P ^ {\prime} (y)}{2 P ^ {\prime \prime} (y) - (1 + \beta \eta) \left\{P (y) P ^ {\prime \prime} (y) + [ P ^ {\prime} (y) ] ^ {2} \right\}}\tag{42}
$$

Assuming $( 1 - P ( y ) ) P ^ { \prime \prime } ( y ) { > } ( P ^ { \prime } ( y ) ) ^ { 2 }$ , we can easily conclude that $d y / d \beta < 0$ . Since d $\prime / d \beta = ( 1 + \beta \eta ) d x / d \beta + \eta x ,$ , we have dx/dβb0. Since $P ^ { \prime } ( y ) { < } 0$ , we can easily get

$$
d P / d \beta = (d P / d y) (d y / d \beta) > 0\tag{43}
$$

Thus, <sup>fi</sup>rm security decreases with the sharing level, and the regulation decision should be $\beta _ { p } ^ { \nu } { = } 0 .$ □

Proof of Theorem 4. Let x be the investment amount of <sup>fi</sup>rm i or j at Nash equilibrium, and $\theta = \beta \eta$ , then we have:

$$
\frac {d C _ {i}}{d \theta} = g (x _ {e} (\theta), \theta) \frac {d x _ {e}}{d \theta} + x P ^ {\prime} (x _ {e} + \theta x _ {e}) [ 1 - P (x _ {e} + \theta x _ {e}) ] U\tag{44}
$$

where we de<sup>fi</sup>ne

$$
g (x (\theta), \theta) = (1 + \theta) U P ^ {\prime} (x + \theta x) [ 1 - P (x + \theta x) ] + 1\tag{45}
$$

Using Eq. (41), we can rewrite (45) as

$$
g (x _ {e} (\theta), \theta) = \frac {(1 + \theta) P - 2 \theta}{2 - (1 + \theta) P}\tag{46}
$$

which is positive when θ is small. Then $d C _ { i } / d \theta { < } 0$ when θ is small since we can conclude that $d x _ { e } / d \theta < 0$ from the proof of Theorem 3.

Let $\theta _ { 0 }$ be the solution to the equation d $\Sigma _ { e } / d \theta = 0$ . Let $\theta ^ { * }$ be the value of θ that minimizes the social cost, subject to the constraint that $\theta \in [ 0 , 1 ]$ . We can conclude that if $0 < \theta _ { 0 } < 1$ , then $\theta ^ { * } = a _ { 0 } ;$ otherwise, $\theta ^ { * } = 1$ . Furthermore, $\mathrm { i f } \eta { > } \theta ^ { * }$ , we conclude that $\beta _ { p } ^ { c } = \theta ^ { * } / \eta ; \mathrm { i f } \eta { \le } \theta ^ { * }$ , we conclude that $\beta _ { p } ^ { c } { = } 1$ □

Proof of $d x _ { e } / d \theta _ { p } ^ { c } < 0 .$ . Substitutable case.

Let $y = x _ { e } + \theta _ { p } ^ { c } x _ { e }$ . Since <sup>fi</sup>rms i and j are similar, we can rewrite Eq. (27) as

$$
P ^ {\prime} (y) [ 2 - P (y) ] U - \theta_ {p} ^ {c} P (y) P ^ {\prime} (y) U + 2 = 0\tag{47}
$$

Taking total derivative with respect to $\theta _ { p } ^ { c } ,$ we can get

$$
\frac {d y}{d \theta_ {p} ^ {c}} = \frac {P (y) P ^ {\prime} (y)}{2 P ^ {\prime \prime} (y) - \left(1 + \theta_ {p} ^ {c}\right) \left\{P (y) P ^ {\prime \prime} (y) + [ P ^ {\prime} (y) ] ^ {2} \right\}}\tag{48}
$$

Assuming $[ 1 - P ( y ) ] P ^ { \prime \prime } ( y ) { > } [ P ^ { \prime } ( y ) ] ^ { 2 }$ , we can easily conclude that dy/ $d \theta _ { p } ^ { c } { < } 0$ . Since $d y / d \theta _ { p } ^ { c } = ( 1 + \theta _ { p } ^ { c } ) d x _ { e } / d \theta _ { p } ^ { c } + x ,$ we conclude that $d x _ { e } /$ $d \dot { \theta _ { p } ^ { c } } { < } 0$ □

Proof of $\mathbf { \nabla } \mathbf { d } P _ { e } / \mathbf { d } \theta _ { p } ^ { c } { > } \mathbf { 0 } .$ Substitutable case.

From the proof of $d x / d \theta _ { p } ^ { c } ,$ , assuming $[ 1 - P ( y ) ] P ^ { \prime \prime } ( y ) { > } [ P ^ { \prime } ( y ) ] ^ { 2 } ,$ , we have $d y / d \theta _ { p } ^ { c } { < } 0$ . Since $P ^ { \prime } ( y ) { < } 0$ , we can easily get $d P _ { e } / d \theta _ { p } ^ { c } { = } \left( d P _ { e } / d y \right)$ $( d y / d \theta _ { p } ^ { c } ) { > } 0 .$

Proof of Theorem 5. From the proof of Theorem $^ { 4 , }$ we can infer that: if θ bθ<sup>∗</sup>, then dC/dθb0.

When ηbθ<sup>∗</sup>, we have $\beta _ { p } ^ { c } { = } 1$ , which implies that $\theta _ { p } ^ { c } { = } \eta { < } \theta ^ { * }$ , and thus $d C / d \eta = d C / d \theta _ { p } ^ { c } < 0 ;$ when $\eta \geq \theta ^ { * }$ , we have $\theta _ { p } ^ { c } { = } \theta ^ { * }$ , which implies that $d \theta _ { p } ^ { c } / d \eta = 0 ,$ , and thus d $\begin{array} { r } { \Sigma / d \eta = ( d C / d \theta _ { p } ^ { c } ) ( d \theta _ { p } ^ { c } / d \eta ) = 0 . } \end{array}$

Proof of Theorem 6. To minimize the social cost, we need to minimize the sum of the costs to the two <sup>fi</sup>rms. Since <sup>fi</sup>rms i and j are similar, we let $\chi _ { i } = \chi _ { j } = x ,$ and $\beta _ { i } = \beta _ { j } = \beta . \ \mathsf { S o }$ , we write the objective function as

$$
C _ {s o c i a l} = P (x + \beta \eta x) [ 2 - P (x + \beta \eta x) ] U + 2 x\tag{49}
$$

$$
\frac {d C _ {\text { social }}}{d \beta} = 2 \eta x U P ^ {\prime} (x + \beta \eta x) [ 1 - P (x + \beta \eta x) ] <   0
$$

To minimize the social cost, the social planner should choose the boundary solution $\beta = 1$ . Thus, (Full Share, Full Share) is the optimal sharing strategy determined by the social planner. □

Proof of Theorem 7. We can see that $\cdot ( x ^ { * } ( \eta ) , \eta ) = 0$ from Eq. (29) where g(x(η), η) is de<sup>fi</sup>ned in Eq. (45). Also, the cost function of Eq. (28) should be convex in x to minimize the cost, i.e., we have $\partial g$ $( x ( \eta ) , \eta )$ /artialxN0. When <sup>fi</sup>rms make their own investment decisions, let $\eta _ { 1 }$ be the solution to $g ( x _ { e } ( \theta ) , \theta ) = 0$ under full sharing $( \beta = 1 )$ . Then from the proof of Theorem $^ { 4 , }$ we have $0 < \eta _ { 1 } < \theta _ { 0 } .$

If $\eta { \leq } \eta _ { 1 }$ , then $g ( x _ { e } ( \theta ) , \theta ) > 0$ . Note that $\eta _ { 2 }$ satis<sup>fi</sup>es Eq. (46); hence, $\eta _ { 1 } = \eta _ { 2 }$ . Then we can conclude that $x _ { e } \ge x ^ { * }$ since $g ( x ^ { * } ( \eta ) , \eta ) = 0$ and ∂g $( x ( \eta ) , \eta ) / { \partial x } { > } 0$ . Otherwise, if $\eta { > } \eta _ { 1 }$ , we have ${ x } _ { e } < { x } ^ { * }$

## References

[1] T. August, T.I. Tunca, Network software security and user incentives, Management Science 52 (11) (2006) 1703–1720.

[2] M. Cakanyildirim, W. Yue, Y. Ryu, The management of intrusion detection: con<sup>fi</sup>guration, inspection, and investment, European Journal of Operational Research 195 (2009) 186-204

[3] Q. Chen, M. Schmidt, D. Phan, K. Arnett, E-commerce security threats: awareness, Trust and Practice. International Journal of Information Systems and Change Management 3 (2008) 16–32.

[4] E. Gal-Or, A. Ghose, The economic incentives for sharing security information Information Systems Research 16 (2005) 186–208.

[5] L. Gordon, M. Loeb, W. Lucyshyn, Sharing information on computer systems security: an economic analysis, Journal of Accounting and Public Policy 22 (2003) 461–485.

[6] M. Grean, M.J. Shaw, Book Chapter: Supply-Chain Partnership between P&G and Wal-Mart, E-Business Management, Springer US, 2002, pp. 155–171.

[7] J.T. Hamill, R.F. Deckro, J.M. Kloeber Jr., Evaluating information assurance strategies, Decision Sopport Systems 39 (3) (2005) 463–484.

[8] G. Heal, H. Kunreuther, IDS models of airline security, The Journal of Con<sup>fl</sup>ict Resolution 49 (2) (2005) 201–217.

[9] A. Kirby, Trade associations as information exchange mechanisms, RAND Journal of Economics 19 (1) (1988) 138–146

[10] H. Kunreuther, G. Heal, Interdependent security, Journal of Risk and Uncertainty 26 (2/3) (2003) 231–249.

[11] A. Larsen, Global security survey: virus attack Available at, InformationWeek.com 1999http://www.informationweek.com/743/security.htm

[12] W. Liu, H. Tanaka, M. Kanta, An Empirical Analysis of Security Investment in Countermeasures Based on an Enterprise Survey in Japan, Proc. of the Fifth Workshop on the Economics of Information Security, University of Cambridge, England. 2006.

[13] E.W.T. Ngai, F.K.T. Wat, Dominance approach to risk analysis of computer systems, Decision Support Systems 37 (4) (2004) 485–500.

[14] H. Ogut, N. Menon, S. Raghunathan, Cyber Insurance and IT Security Investment: Impact of Interdependent Risk, Working paper, University of Texas at Dallas, 2005.

[15] J. Pratt, Risk aversion in the small and in the large, Econometrica 32 (1) (1964) 122–136.

[16] C. Shapiro, Exchange of cost information in oligopoly, Review of Economics Studies 53 (3) (1986) 433–446.

[17] P. Stamp, J. Penn, M. Adrian, B. Gray, Increasing Organized Crime Involvement Means More Targeted Attacks, Forrester ResearchAvailable at, http://www. forrester.com/Research/Document/Excerpt/0,7211,37505,00.htmlAugust 2, 2005.

[18] A. Sullivan, Hackers Score Big by Thinking Small, Experts Say. ComputerWorld.com Available at, http://www.andysullivan.com/Hackersthinksmall,June20.htmlJune 21, 2005.

[19] D. Szymanski, T. Hise, e-satisfaction: an initial examination, Journal of Retailing 76 (3) (2000) 309–322.

[20] G.B. Tanna, M. Gupta, H.R. Rao, S. Upadhyaya, Information assurance metric development framework for electronic bill presentment and payment systems using transaction and work<sup>fl</sup>ow analysis, Decision Support Systems 41 (1) (2005) 242–261.

[21] X. Vives, Trade association disclosure rules, incentives to share information, and welfare, RAND Journal of Economics 21 (3) (1990) 409–430.

[22] W.T. Yue, M. Cakanyildirim, Y.U. Ryu, D. Liu, Network externalities, layered protection and IT security risk management, Decision Support Systems 44 (2007) 1–16.

[23] X. Zhao, L. Xue, A. Whinston, Managing Interdependent Information Security Risks: A Study of Cyberinsurance, Managed Security Service and Risk Pooling, 30th International Conference on Information Systems (ICIS), Phoenix, Arizona, 2009.

[24] A. Ziv, Information sharing in oligopoly: the truth-telling problem, RAND Journal of Economics 24 (1993) 455–465.

Dengpan Liu received the PhD degree in Management Science with a concentration in Information Systems from the University of Texas at Dallas in 2006. He is currently an Assistant Professor of Management Information Systems at the University of Alabama, Huntsville. He has published in journals such as Decision Support Systems, Information Systems Research, and Production and Operations Management.

Yonghua Ji is an Associate Professor of MIS in School of Business, University of Alberta. He received his Ph.D. in Management, with a major in MIS, from University of Texas at Dallas. His current research interests include economics of information systems, optimal software development methodologies, and social network. He has published in journals such as INFORMS Journal on Computing, Information Systems Research and Production and Operations Management

Vijay S. Mookerjee holds a Ph.D. in Management, with a major in MIS, from Purdue University.His current research interests include social networks, optimal software development methodologies, storage and cache management, content delivery systems, and the economic design of expert systems and machine learning systems. He has published in and has articles forthcoming in several archival Information Systems, Computer Science, and Operations Research journals. He serves (or has served on) on the editorial board of Management Science, Information Systems Research, INFORMS Journal on Computing, Operations Research, Decision Support Systems, Information Technology and Management, and Journal of Database Management.
