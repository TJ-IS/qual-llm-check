---
otero_id: 2298
otero_key: "SEQG6BHQ"
title: "Information Security Outsourcing with System Interdependency and Mandatory Security Requirement"
authors: "Kai-Lung Hui; Wendy Hui; Wei T. Yue"
year: "2012"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222290304"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/SEQG6BHQ/fulltext/images/d3713c968cd423dd192fd510084262d7fcfd31bdf3042088fedf68a5449348e5.jpg)

# Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# Information Security Outsourcing with System Interdependency and Mandatory Security Requirement

Kai-Lung Hui <sup>a</sup> , Wendy Hui <sup>b</sup> & Wei T. Yue

<sup>a</sup> Department of Information Systems, Business Statistics, and Operations Management, Hong Kong University of Science and Technology

<sup>b</sup> Hong Kong University of Science and Technology

<sup>c</sup> Department of Information Systems, City University of Hong Kong Published online: 09 Dec 2014.

To cite this article: Kai-Lung Hui , Wendy Hui & Wei T. Yue (2012) Information Security Outsourcing with System Interdependency and Mandatory Security Requirement, Journal of Management Information Systems, 29:3, 117-156

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222290304

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms &

Conditions of access and use can be found at http://www.tandfonline.com/page/termsand-conditions

# Information Security Outsourcing with System Interdependency and Mandatory Security Requirement

Kai -Lun g Hui, Wend y Hui, and Wei T. Yue

Kai-Lung Hui is an associate professor in the Department of Information Systems, Business Statistics, and Operations Management at the Hong Kong University of Science and Technology. He holds a Ph.D. in information systems from the Hong Kong University of Science and Technology. His research interests include information security and privacy, electronic commerce, and social interaction. His research has been published in scholarly journals, including American Economic Review: Papers and Proceedings, Management Science, Journal of Management Information Systems, and MIS Quarterly.

Wendy Hui is a senior lecturer at Curtin University. She holds a Ph.D. in information systems from the Hong Kong University of Science and Technology. She has taught in Zayed University and University of Nottingham Ningbo China. Her current research interests include information security and quantitative research methods. Her work has appeared in IS journals, including Journal of Management Information Systems, Decision Support Systems, and IEEE Transactions on Systems, Man and Cybernetics Part A.

Wei T. Yue is an associate professor in the Department of Information Systems at City University of Hong Kong. He holds a Ph.D. in management information systems from Purdue University. He has done extensive research in the area of information security. His work has appeared in journals including Management Science, Information Systems Research, Journal of Management Information Systems, and Decision Support Systems.

Abst ract : The rapid growth of computer networks has led to a proliferation of information security standards. To meet these security standards, some organizations outsource security protection to a managed security service provider (MSSP). However, this may give rise to system interdependency risks. This paper analyzes how such system interdependency risks interact with a mandatory security requirement to affect the equilibrium behaviors of an MSSP and its clients. We show that a mandatory security requirement will increase the MSSP’s effort and motivate it to serve more clients. Although more clients can benefit from the MSSP’s protection, they are also subjected to greater system interdependency risks. Social welfare will decrease if the mandatory security requirement is high, and imposing verifiability may exacerbate social welfare losses. Our results imply that recent initiatives such as issuing certification to enforce computer security protection, or encouraging auditing of managed security services, may not be advisable.

Key w ords and ph rases: information security, information security outsourcing, interdependency risks, mandatory security requirement, security compliance.

Typically, the outsourcer . . . has a central operations room with lots of monitors displaying plenty of monitoring output. Oversubscribed staff attempt to process the barrage of alerts, but focus primarily on the top three to five clients listed on a whiteboard in the corner. If you aren’t on the whiteboard, nobody is looking after your gear. [10]

Recent report s h ave underscored th e growth of securit y out sourcing. For example, more than 30 percent of firms are now outsourcing some part of their security functions [30]. The managed security service provider (MSSP) market in North America is expected to hit a revenue of \$3.9 billion in 2016 [50]. A recent survey found that 55 percent and 44 percent of firms are either outsourcing or planning to outsource, respectively, penetration tests and security assessments [40]. The security services that are outsourced range from managing firewalls to implementing security architecture [55]. Firms are also taking greater responsibility in meeting regulatory-driven security requirements, such as the Payment Card Industry Data Security Standard (PCI DSS) or the Gramm–Leach–Bliley Act. Indeed, many firms have highlighted regulatory compliance as a motivating factor for outsourcing; in particular, 77 percent of firms considered regulatory compliance to be either a “very important” or an “important” priority in their information security activities [40].

Increasingly, firms are required to compare their information security activities to established performance expectations in security. This phenomenon, known as “base-lining” [56], is mostly spearheaded by external forces, such as the government, professional organizations such as the Information Systems Audit and Control Association (ISACA) or the Information Systems Security Association (ISSA), and service providers [44]. An indirect consequence of base-lining is that the quality of the protected systems has to meet well-defined security requirements, such as reviewing access logs regularly, adopting clear reporting standards, and so forth. It may not be easy for firms to fulfill these security requirements. For example, the PCI DSS requires firms to conduct vulnerability scanning and penetration tests with a thirdparty qualified security assessor on a quarterly basis [48]. For firms that do not possess the know-how to manage their own information security functions, outsourcing the protection to an MSSP has become an attractive option [50, 53]. Besides having better expertise and state-of-the-art facilities, an MSSP enjoys economies of scale [49] and often provides complementary services, such as the detection and prevention of security breaches [12, 13].

Despite its many advantages, information security outsourcing may homogenize the architecture or platform of the clients’ security systems, which may effectively “endogenize” the security risks of all the clients [37]. Essentially, any security breach of a client may now spill over to other clients because of the shared architecture and/ or platform. As an illustrative example, in 2009, the Chinese government proposed that all personal computers be installed with the Green Dam Youth Escort (GDYE) software, which later was found to contain remotely exploitable vulnerabilities [57]. If a hacker could successfully penetrate one client’s system and exploit the GDYE vulnerabilities, then it may be able to compromise the systems of thousands of other clients via the same vulnerabilities. In this case, the clients’ systems became virtually “connected” via the use of the common GDYE software. Similarly, in 2010, a successful attack on the database of Silverpop, a popular e-mail service provider with more than 105 corporate clients, contributed to data losses of a number of Silverpop’s clients, including McDonald’s and Walgreen. It is arguable whether these data losses would have occurred if Silverpop had used a heterogeneous architecture to host its services.

Further, the MSSP may not always deliver a high quality of service. In 2005, CardSystems, which specializes in payment processing, suffered a theft of more than 40 million credit card numbers. Although CardSystems was certified by Savvis, a provider of managed computing and network services, and was believed to have followed the Cardholder Information Security Program (CISP), a later incident response analysis revealed that it did not comply with CISP [60]. The security breach had affected major clients of CardSystems, such as the Merrick Bank.

In 2009, seven restaurants in Louisiana and Mississippi filed a class-action lawsuit against Radiant Systems and Computer World for selling them the Aloha point-of-sale (POS) systems, which were incorrectly described as compliant with the PCI DSS. The suit further alleged that poor business practices related to the Aloha systems had contributed to major data security breaches, which resulted in multiple cases of identity theft. These two examples suggest that the MSSP may not always deliver the promised service quality.

In this paper, we investigate how a mandatory security requirement, such as the GDYE, may affect the extent and benefit of information security outsourcing. In our problem, the clients can choose between outsourcing and in-house development. If they outsource, they would not be able to evaluate or monitor the MSSP’s service. The information asymmetry between the clients and the MSSP may cause the MSSP to shirk its duty and provide substandard security quality. More importantly, the clients who outsource their protection to the MSSP may face system interdependency risks, which may offset the benefit that they obtain from the MSSP’s better protection. Because the clients’ outsourcing decisions are often driven by compliance, the mandatory security requirement is a critical variable that drives some of our key findings.

Our analysis shows that the clients may use the MSSP’s service despite expecting the service quality to be lower than that specified in the service-level agreement (SLA). Such a decision is economically rational because of the need to satisfy the mandatory security requirement.<sup>1</sup> Overall, a stringent mandatory security requirement would shift the surplus from clients to the MSSP. Although it may induce the MSSP to work harder, it would also motivate the MSSP to serve more clients, which indirectly decreases social welfare by spawning a greater interdependency risk.<sup>2</sup> Our analysis shows that the common practice of auditing the MSSP’s effort is less effective than liability-driven SLAs in enhancing social welfare.

We make three contributions. First, we develop an integrated analytical framework that incorporates the key features of security outsourcing. This framework can be readily used to analyze different security initiatives and draw practical insights for firms in the security outsourcing business. Second, we show that recent security trends, such as the establishment of security protection standards or the auditing of MSSPs services [39], can actually reduce social welfare. Third, we extend existing theories in the economics of information security, credence goods, and asymmetric information [2, 3, 19, 20, 58] by critically assessing the robustness of their findings in view of several important contextual characteristics, such as interdependency between clients systems, the presence of hackers who threaten the clients’ information systems, and the presence of industry security regulations.

The rest of this paper is organized as follows. The next section reviews the related literature. We then present our main models and findings. We also extend the model to account for heterogeneous clients, competition, strategic hacking, and shirking clients. We draw managerial and policy implications, and conclude the paper in the last two sections.

## Related Literature

Th ere h as been a grow ing body of l it erat ure on the economics of information security (e.g., [11, 15, 21]). In a pioneering work, Gordon and Loeb [24] model the security investment problem from the welfare-maximizing firm’s perspective, in which security investment would lead to reduced likelihood of security breach, but too high an investment would bring only marginal benefit. Hence, there exists an optimal investment level that maximizes the firm’s profit. Since then, there has been a growing literature that specifically addresses information security investment [27, 32]. Similar to Gordon and Loeb, our model also considers the trade-off between the probability of security breach and security protection efforts. We further allow the clients to outsource security protection to an MSSP, who enjoys greater efficiency in reducing the probability of security breaches. This allows us to extend the analysis in several meaningful ways. First, the clients and the MSSP are engaged in a principal–agent relationship and so information asymmetry becomes prevalent [16]. Second, system interdependency risks arise because the clients share the same security protection platform via the MSSP. Lastly, the possibility to outsource provides an alternative solution for the clients to fulfill the mandatory security requirement.

The literature on information security outsourcing has often assumed that an MSSP will honestly serve the clients (e.g., [17, 18]). In reality, such an assumption may not hold with information asymmetry because clients often cannot fully inspect the quality of the MSSP’s service, which could lead to a shirking of responsibility on the part of the MSSP. Our setting, where the MSSP’s protection effort is related to security breach probability, and the fact that the MSSP is liable for the client’s damage when protection fails, is commonly seen in the product failure and insurance literature (e.g., [46,

51, 52]). Also, the use of software or system liability as an incentive mechanism in managing security risks has been widely proposed (e.g., [4, 31, 47]). For example, August and Tunca [6] analyze the impact of different liability policies on software vulnerability and derive the conditions under which loss liability and patch liability can be effective. They found that patch liability is an effective policy when the software vulnerabilities are not exploited by the attackers immediately.<sup>3</sup> We extend this stream of work by considering how liability should be provided in the presence of system interdependency risks.

A small stream of research has highlighted the importance of system interdependency risks. Kunreuther and Heal [33] examine firms’ optimal decisions regarding security investment when their risks are interdependent. When the number of firms increases, firms have more incentive to underinvest in security. Varian [54] suggests that such behavior is a type of free-riding, much like that observed in the provision of public goods. Yue et al. [59] examine the decisions on how a firm should distribute its security resources between system-specific versus general security protections. Although general protections may curb external attacks, system-specific protections alleviate the threat of system interdependency risks. August and Tunca [5] model interdependency risk arising on the user side due to unpatched software. They discuss the impact of policies such as mandatory patching, patching rebate, and usage tax in managing security risks. In our problem, we restrict system interdependency risks to only clients who are outsourcing to the MSSP (because then they share the same security platform) and analyze how the clientele and quality decisions of the MSSP affect the overall risks of the clients and social welfare.

There is also a growing literature on policy and mechanism design in information security. Ghose and Rajan [23] consider the economic effect of regulatory information disclosure on firms’ security investment, whereby mandatory security disclosure could motivate firms to make optimal production decisions. Lee et al. [34] consider the impact of security standardization when such initiatives can only partially cover the overall security effort in an organization. While security standardization could be done only under verifiable control, Lee et al. found that such standardization could lead to suboptimal results with unverifiable control. Our model also considers a mandatory security requirement (also known as “standardization”), but in a setting whereby shirking of responsibility is possible on both the MSSP’s and the client’s side.

## Basic Model

We st art w ith a simpl e model and ext end it to include other important features of security outsourcing such as system interdependency, strategic hacking, and competition in later sections. Our basic model encompasses the following assumptions:

Assumption 1: There is one client $( \ ^ {  } s h e ^ { \prime \prime } )$ and one MSSP $( " h e ^ { \prime \prime } )$ . The client values her system at v.

Assumption 2: A hacker $( \ ^ { \dots } i t ^ { \prime \prime } )$ attacks the client’s system with probability $a \in I O , I J .$

Assumption 3: The SLA between the client and the MSSP includes a compensa tion term $( { } ^ { \cdots } l i a b i l i t y ^ { , * } ) , \mathrm { \ } \mathrm { \beta } \in \mathrm { \it ~ / 0 , \it ~ I J }$ . If the client suffers a loss of v because of the hacker’s attack, then the MSSP has to compensate her by bv.

Assumption 4: The client’s cost of developing security protection is an increasing convex function, $( I / 2 ) c _ { k } q ^ { 2 } ;$ , where $c _ { \scriptscriptstyle k }$ is a cost coefficient and q denotes the security quality, which represents the probability that the client’s system can deter the hacker’s attack. The corresponding cost for the MSSP is $( l / 2 ) c _ { s } q ^ { 2 }$ where $c _ { s } < c _ { k }$

Assumption 5: v, $c _ { _ { k } } , c _ { _ { s } }$ , and a are public information.

Assumption $6 \colon a \nu \leq c _ { s }$

Assumption 6 ensures that the analysis will not arrive at a corner solution. If $a \nu > c _ { s }$ then the expected loss to the client is excessive, to the extent that she will always engage the highest level of security protection, $q = 1$ . This case is not interesting, and thus we exclude it from the analysis. Figure 1 presents the game sequence.

If the client did not protect her system, her utility would be $u _ { 0 } = ( 1 - a ) \nu$ . If the client developed the protection in-house, her expected utility would be

$$
u _ {k} = \Big [ 1 - a (1 - q _ {k}) \Big ] v - \frac {1}{2} c _ {k} q _ {k} ^ {2},
$$

where $q _ { k }$ denotes the security quality from in-house development.<sup>4</sup> Differentiating $u _ { \scriptscriptstyle k }$ with respect to $q _ { k } ,$ the optimal security quality, $q _ { k } ^ { * } = a \nu / c _ { k }$ . By Assumptions 4 and $^ { 6 , }$ $0 \leq q _ { k } ^ { * } \leq 1$ . The utility of the client from in-house development is then

$$
u _ {k} ^ {*} = (1 - a) v + \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}}.\tag{1}
$$

Since $u _ { k } ^ { * } > u _ { 0 } , u _ { k } ^ { * }$ is the client’s reservation utility.

If the client outsourced the protection, her net utility is

$$
u _ {s} = \left[ 1 - a (1 - q _ {s}) \right] v + a \beta v (1 - q _ {s}) - p,\tag{2}
$$

where p denotes the price charged by the MSSP and $q _ { s }$ denotes the quality of the MSSP’s protection, which is not observable to the client. The second term in Equation (2) is the expected compensation receivable by the client. The MSSP’s profit is

$$
\pi = p - a \beta v (1 - q _ {s}) - \frac {1}{2} c _ {s} q _ {s} ^ {2}.\tag{3}
$$

To induce the client to choose his service, the MSSP has to ensure that the client is no worse off than getting the reservation utility, that is, $u _ { s } \geq u _ { k } ^ { * } .$ . By Equations (1) and (2), we must have

$$
p \leq a v q _ {s} + a \beta v (1 - q _ {s}) - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}}.
$$

![](/api/attachments/SEQG6BHQ/fulltext/images/d90bf6a260190cc0c912949da8b33cd2ba3c2f483f34c4925c15a4c21a918f3f.jpg)  
Figure 1. Game Sequence

The MSSP’s problem becomes

$$
\max _ {p, q _ {s}, \beta} \left[ p - a \beta v (1 - q _ {s}) - \frac {1}{2} c _ {s} q _ {s} ^ {2} \right]
$$

$$
\text { s.t. } p \leq a v q _ {s} + a \beta v (1 - q _ {s}) - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}}.
$$

The solution is

$$
q _ {s} ^ {*} = \frac {a v}{c _ {s}},
$$

$$
p ^ {*} = \frac {(a v) ^ {2}}{c _ {s}} + a \beta^ {*} v \left(1 - \frac {a v}{c _ {s}}\right) - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}},
$$

and

$$
\pi^ {*} = \frac {1}{2} (a v) ^ {2} \left(\frac {1}{c _ {s}} - \frac {1}{c _ {k}}\right) > 0
$$

because $c _ { _ k } > c _ { _ s }$ . Lemma 1 summarizes these results:

Lemma 1: In equilibrium, the MSSP will set price and liability such that $p ^ { * } - a \ B ^ { * } \nu ( I - ( a \nu / c _ { s } ) ) = ( ( a \nu ) ^ { 2 } / c _ { s } ) - ( I / 2 ) ( ( a \nu ) ^ { 2 } / c _ { k } )$ . He will exert effort, $q _ { s } ^ { * } = a \nu / c _ { s }$ The client will use the MSSP’s service, and her expected utility will be

$$
u _ {s} ^ {*} = (1 - a) v + \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}}.\tag{4}
$$

The MSSP’s equilibrium profit is

$$
\pi^ {*} = \frac {1}{2} (a v) ^ {2} \left(\frac {1}{c _ {s}} - \frac {1}{c _ {k}}\right).\tag{5}
$$

The proofs of all the results are in the Appendix.

By Equations (1) and (4), $\boldsymbol { u } _ { s } ^ { * } = \boldsymbol { u } _ { k } ^ { * }$ . Because $\pi ^ { * } > 0$ , the availability of the security service improves social welfare. This is obvious because, by assumption, it is more cost-effective for the MSSP to develop the protection than the client. Further, because $c _ { { \scriptscriptstyle k } } > c _ { { \scriptscriptstyle s } } , q _ { { \scriptscriptstyle s } } ^ { * } > q _ { { \scriptscriptstyle k } } ^ { * }$ , which means that the client is better protected when she uses the MSSP’s service.

We now ask: What if the external environment requires the client to attain a minimum level of security? To address this question, we add two assumptions:

Assumption 7: There is a minimum security requirement, q<sub>\_</sub>, $\begin{array} { r } { O \leq { \underline { { q } } } \leq I . } \end{array}$

Assumption 8: The client must develop up to q<sub>\_</sub> if she chooses the in-house option.

She will not be able to verify the $M S S P ' _ { s }$ effort if she outsources the protection.

Assumptions 7 and 8 apply to settings whereby the mandatory security requirement is enforced by third-party certifications. For example, a firm may deploy internal programmers to develop the ISO 27000 requirements. To complete the certification processes, however, its effort will be subject to controls and audits by the relevant certification bodies. By contrast, if a client outsources her protection to a certified MSSP, she could fulfill her security obligation (despite not being able to verify the MSSP’s effort). With Assumption 8, the MSSP could offer a lower level of security quality than that specified in the service contract $( ^ { 6 6 } \mathrm { { s h i r k } ^ { 7 } ) }$ if it is in his best interest to do so.<sup>5</sup>

To analyze the impact of imposing q<sub>\_</sub>, we need to consider two cases:

Case (i): $\underline { { q } } \le q _ { k } ^ { * } = a \nu / c _ { k }$ . The mandatory security requirement is immaterial because it is lower than what the client would choose with in-house development anyway.

Case $( i i ) \colon \underline { { q } } > q _ { k } ^ { * }$ . The client must develop q<sub>\_</sub> if she chooses in-house development, and so her new reservation utility becomes

$$
\breve {u} _ {k} ^ {*} = (1 - a) v + a v \underline {{q}} - \frac {1}{2} c _ {k} \underline {{q}} ^ {2}.\tag{6}
$$

By Equation (1), $\check { u } _ { k } ^ { \ast } - u _ { k } ^ { \ast } = - ( 1 / 2 ) c _ { k } ( \underline { { q } } - ( a \nu / c _ { k } ) ) ^ { 2 } < 0$ , that is, a high mandatory security requirement decreases the reservation utility that the client could obtain from in-house development.<sup>6</sup>

In case (ii), to attract the client, the MSSP must ensure that the client gets at least her (new) reservation utility, $\breve { u } _ { { } _ { k } } ^ { * }$ . By Equations (2) and (6), the constraint on price and liability becomes $p \leq a \nu ( q _ { s } - \underline { { q } } ) + a \beta \nu ( 1 - q _ { s } ) + ( 1 / 2 ) c _ { k } \underline { { q } } ^ { 2 }$ . Following a similar analysis as leading to Lemma 1, our first proposition follows:

Proposition 1: When there is a mandatory security requirement, $\underline { { q } } \mathrm { : }$

(a) $I f { \underline { { q } } } \leq a \nu / c _ { _ k }$ , the results in Lemma 1 apply. The MSSP will supply the security quality stated in the service contract, $q _ { s } ^ { * } = a \nu / c _ { s }$

(b) $I f { \underline { { q } } } > a \nu / c _ { _ k }$ , the MSSP will supply $\breve { q } _ { s } ^ { * } = a \nu / c$ and set price and liability such that

$$
\breve {p} ^ {*} - a \breve {\beta} ^ {*} v \left(1 - \frac {a v}{c _ {s}}\right) = \frac {(a v) ^ {2}}{c _ {s}} - a v \underline {{q}} + \frac {1}{2} c _ {k} \underline {{q}} ^ {2}.
$$

The client’s expected utility is

$$
\bar {u} _ {s} ^ {*} = (1 - a) v + a v \underline {{q}} - \frac {1}{2} c _ {k} \underline {{q}} ^ {2}.\tag{7}
$$

The MSSP’s equilibrium profit is

$$
\overline {{\pi}} ^ {*} = \frac {1}{2} \frac {(a v) ^ {2}}{c _ {s}} + \frac {1}{2} c _ {k} \underline {{q}} ^ {2} - a v \underline {{q}}.\tag{8}
$$

Further, $i f g \le a \nu / c _ { s }$ , the equilibrium service quality exceeds the mandatory requirement; the MSSP will truthfully supply the quality stated in the service contract. By contrast, $i f \underline { { q } } > a \nu / c _ { s }$ , the MSSP will claim to supply q<sub>\_</sub> when in fact supplying only $\breve { q } _ { s } ^ { * } < { \underline { { q } } }$ . The client knows that the MSSP will shirk but will nevertheless use his service.

By Equations (5) and (8),

$$
\bar {\pi} ^ {*} - \pi^ {*} = \frac {1}{2} c _ {k} \underline {{{q}}} ^ {2} + \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}} - a v \underline {{{q}}} = \frac {1}{2} c _ {k} \left(\underline {{{q}}} - \frac {a v}{c _ {k}}\right) ^ {2} > 0,
$$

and so the MSSP earns a higher profit when q<sub>\_</sub> is high. By Equations (4) and (7),

$$
\breve {u} _ {s} ^ {*} - u _ {s} ^ {*} = - \frac {1}{2} c _ {k} \left(\underline {{q}} - \frac {a v}{c _ {k}}\right) ^ {2} <   0,
$$

and so the client’s expected utility decreases. Accordingly, by moving from Lemma 1 to Proposition 1, we see that the mandatory security requirement is immaterial when it is low $( \underline { { q } } \le a \nu / c _ { _ k } )$ , but when it is high $( \underline { { q } } > a \nu / c _ { _ k } )$ , it facilitates the earning of a higher profit by the MSSP. The mandatory security requirement will not change the equilibrium service quality, which is always $a \nu / c _ { s }$ whether q<sub>\_</sub> is imposed or not. Figures 2 and 3 plot how the client’s utility and $\mathrm { M S S P ^ { \prime } s }$ profit vary with $\underline { { q . } } ^ { 7 }$

Further, by Equations (4) and (7), $d u _ { s } ^ { * } / d a = - \nu ( 1 - ( a \nu / c _ { k } ) ) < 0$ and $d \check { u } _ { s } ^ { * } / d a =$ $- \nu ( 1 - q ) < 0$ , and so the client always prefers the attack probability, a, to be small. By contrast, by Equations (5) and (8), dp $^ { * } / d a = a \nu ^ { 2 } ( 1 / c _ { _ s } - 1 / c _ { _ k } ) > 0$ and $d \check { \pi } ^ { * } / d a =$ $\nu ( ( a \nu / c _ { s } ) - q ) < 0$ if and only if $\underline { { q } } > a \nu / c _ { s }$ . So, the MSSP actually prefers the attack probability to increase when there is no mandatory security requirement or when the mandatory security requirement is low.

When $\underline { { q } }$ is immaterial (i.e., Proposition 1a), the MSSP makes a profit mostly from his superior cost efficiency relative to the client, the scale of which increases as the threat from the hacker, a, increases. On the other hand, if $\underline { { q } } > a \nu / c _ { s }$ is high, by rearranging Equation (8), we have

$$
\tilde {\pi} ^ {*} = \frac {1}{2} (a v) ^ {2} \left(\frac {1}{c _ {s}} - \frac {1}{c _ {k}}\right) + \frac {1}{2} c _ {k} \left(\underline {{q}} - \frac {a v}{c _ {k}}\right) ^ {2}.
$$

The first term is identical to $\pi ^ { * }$ in Equation (5) and represents the MSSP’s profit due to his superior cost efficiency, which increases in a. The second term is the supranormal profit due to the fact that the MSSP could shirk but not the client. As a increases, the client would prefer a higher level of security protection, and so the gap between $\underline { { q } }$ and $\boldsymbol { a } \nu / c _ { \boldsymbol { k } }$ (the security level that the client would choose with in-house development) decreases, which implies that the second term decreases in a. Whether $\breve { \pi } ^ { * }$ increases or decreases in $a$ then depends on the balance of these two terms. When $\underline { { q } } > a \nu / c _ { s }$ , the second term prevails. The MSSP would prefer the attack probability to decrease.

![](/api/attachments/SEQG6BHQ/fulltext/images/afb16209374288a490dffa35c7ed4245afdc0bbff64b201bd90573073d0bebd6.jpg)  
Figure 2. Client Utility

![](/api/attachments/SEQG6BHQ/fulltext/images/83753bbdbd2fe17ed94a93f8804e8eecd2e97cbc37dd7ccda5d41797e1ef19e1.jpg)  
Figure 3. MSSP’s Profit

The condition $\underline { { q } } > a \nu / c _ { s }$ in Proposition 1b corresponds to a situation where the client deliberately shifts the compliance responsibility to the MSSP by security outsourcing. The client knows that the MSSP will shirk and underprovide security quality relative to the mandatory security requirement, ${ \mathit { \Omega } } _ { 2 } ^ { q , }$ but she is willing to pay for his service because she knows that her threat from a hacker attack is not high enough to justify developing $\underline { { q } }$ internally. In other words, the client simply pays others to help her satisfy the mandated requirement. As is clear from Lemma 1 and Proposition 1, $\boldsymbol { u } _ { s } ^ { * } + \boldsymbol { \pi } ^ { * } = \breve { \boldsymbol { u } } _ { s } ^ { * } + \breve { \boldsymbol { \pi } } ^ { * }$ So, the mandatory security requirement does not affect social welfare.

Finally, the model presented here can be easily generalized to n clients if the clients are homogeneous and independent, the MSSP’s cost of serving multiple clients exhibits constant economies of scale, and there is no resource constraint. The independence assumption ensures that the MSSP’s optimization problem is separable among the n clients. The homogeneity and the lack of resource constraint assumptions ensure that the MSSP will offer the same contract to all the clients. Then, Lemma 1 and Proposition 1 can be extended directly; the MSSP’s profit is simply the sum of the profit gained from serving each of the n clients.

## Multiple Interdependent Clients

In a netw ork ed economy, computer systems are interdependent [33]. A compromise in one part of a network can spill over to other computers in the same network. For example, a successful attack at one client’s system may cause the MSSP to halt his entire network to ensure that the problem does not propagate. Other clients may also need to check their log files to ensure that there has not been any unauthorized access/ damage to their data. To capture this negative spillover, we modify Assumptions 1, 2, 3, and 4:

Assumption 1 ′: There are n clients and one MSSP. Each client values her system at v. The clients’ systems become interdependent if they outsource to the MSSP. If one client’s system is compromised, then each of the other MSSP’s clients will incur a loss of ev, where e is a small constant.<sup>8</sup>

Assumption 2 ′: A hacker will attack A out of the n clients, where $O \leq A \leq n .$ . The A attacks are independent and uniformly distributed among the n clients. Hence, the probability for each client to be attacked is $a = A / n , O \leq a \leq I .$

Assumption $3 ^ { \prime } { : }$ The SLA between the clients and the MSSP includes a compensation term $( \ ^ { \ast \ast } l i a b i l i t y ^ { , \ast } ) , \beta \in [ O , I J . A $ client whose system is directly compromised (“hacked”) will receive a compensation of bv. Each of the other MSSP’s clients who indirectly suffer harm due to system interdependency will receive bev.

Assumption $4 ^ { \prime } { : }$ Each client’s cost of developing security protection is an increasing convex function, $( I / 2 ) c _ { k } q ^ { 2 } .$ . The corresponding cost for the MSSP is $( I / 2 ) c _ { s } q ^ { 2 } ;$ $c _ { \scriptscriptstyle s } < c _ { \scriptscriptstyle k }$ . The MSSP incurs a separate cost to protect each client.<sup>9</sup>

As before, a client’s expected utility from in-house development is given by Equation (1). Due to the system interdependency, the MSSP may choose not to serve all n clients. Let there be $m \leq n$ clients using the MSSP’s service.<sup>10</sup> Suppose that client $j ,$ $j = 1 , . . . , m$ , outsourced her protection to the MSSP. Her expected utility is

$$
u _ {s, j} = \left(1 - L _ {j}\right) v + L _ {j} \beta_ {j} v - p _ {j},\tag{9}
$$

where

$$
\begin{array}{c} L _ {j} \equiv a (1 - q _ {s, j}) + e \left[ \frac {a (n a - 1) \sum_ {i = 1 , i \neq j} ^ {m} (1 - q _ {s , i})}{n - 1} + \frac {(1 - a) (n a) \sum_ {i = 1 , i \neq j} ^ {m} (1 - q _ {s , i})}{n - 1} \right] \\ = a (1 - q _ {s, j}) + e a \sum_ {i = 1, i \neq j} ^ {m} (1 - q _ {s, i}) \end{array}
$$

denotes the expected loss of client j. The first term in $L _ { j }$ is the probability that the hacker directly and successfully hacked client $j ^ { \circ } \mathrm { s }$ system. The second term in $L _ { j }$ is the expected number of security breaches among the other $m - 1$ MSSP’s clients, multiplied by the spillover (externality) factor, $e . $ 11

Given m clients, the $\mathbf { M S S P } \mathrm { ^ { \circ } s }$ total profit would be

$$
\pi = \sum_ {j = 1} ^ {m} \left(p _ {j} - L _ {j} \beta_ {j} v - \frac {1}{2} c _ {s} q _ {s, j} ^ {2}\right).\tag{10}
$$

To attract the clients to use his service, the prices and liabilities have to satisfy $u _ { s , j } \geq u _ { k } ^ { * }$ that is,

$$
p _ {j} \leq (a - L _ {j}) v + L _ {j} \beta_ {j} v - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}}.
$$

The MSSP’s problem then becomes

$$
\max _ {p _ {j}, q _ {s, j}, \beta_ {j}, m} \sum_ {j = 1} ^ {m} \left(p _ {j} - L _ {j} \beta_ {j} v - \frac {1}{2} c _ {s} q _ {s, j} ^ {2}\right)
$$

$$
\text { s.t. } p _ {j} \leq (a - L _ {j}) v + L _ {j} \beta_ {j} v - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}} \forall j = 1, \dots , m.
$$

The following lemma characterizes the solution to this problem:

Lemma 2: In equilibrium, the MSSP will set price and liability such that

$$
p _ {j} ^ {*} - T a \beta_ {j} ^ {*} v \left(1 - \frac {T a v}{c _ {s}}\right) = \frac {(T a v) ^ {2}}{c _ {s}} - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}} - a v (T - 1), \quad j = 1, \dots , m ^ {*},
$$

where $T \equiv I + e ( m ^ { * } - I )$ . He will exert the same effort, $q _ { s } ^ { * } = T a { \nu } / { c _ { s } }$ , for all the clients, where $m ^ { * }$ and $q _ { s } ^ { * }$ solve

$$
m ^ {*} = \frac {1}{2} + \frac {a v q _ {s} ^ {*} - \frac {1}{2} c _ {s} \left(q _ {s} ^ {*}\right) ^ {2} - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}}}{2 e a v (1 - q _ {s} ^ {*})}\tag{11}
$$

and

$$
q _ {s} ^ {*} = \frac {a v}{c _ {s}} \left[ 1 + e (m ^ {*} - 1) \right].\tag{12}
$$

$m ^ { * }$ clients will outsource. Their expected utility is the same as in Equation $( 4 ) _ { ; }$ that is, $u _ { s } ^ { * } = ( I - a ) \nu + ( I / 2 ) ( ( a \nu ) ^ { 2 } / c _ { k } )$ . The other $n - m ^ { * }$ clients will stay out but obtain the same utility as the $m ^ { * }$ clients of the MSSP, that is, $\boldsymbol { u } _ { k } ^ { * } = \boldsymbol { u } _ { s } ^ { * }$ . The $M S S P ' _ { s }$ equilibrium profit is

$$
\pi^ {*} = m ^ {*} \left[ \frac {1}{2} \frac {(T a v) ^ {2}}{c _ {s}} - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}} - a v (T - 1) \right].\tag{13}
$$

Comparing Lemma 2 with Lemma 1, with system interdependency, the clients’ utility does not change but the MSSP earns a lower profit per client. System interdependency increases the threat faced by the MSSP’s clients. In order to attract the clients, the MSSP has to ensure that they get at least the in-house development reservation utility, $u _ { k } ^ { * } .$ . So, the MSSP has to internalize the losses arising from system interdependency, which can be achieved by compensating clients whose systems are not directly hacked for harms that they suffer due to spillovers from others.

Further, because the MSSP has to internalize the expected losses due to system interdependency, he will raise the quality of security protection for his clients. Ironically, despite the fact that system interdependency increases the MSSP's clients’ threats, it also enhances their protection against direct hacking. The MSSP’s clients may suffer from others’ security breaches, but their own systems will be less likely to be directly hacked now.<sup>12</sup>

We next investigate the implications of imposing a mandatory security requirement. With Assumptions 7 and 8, Lemma 2 will continue to hold if $\underline { { q } } \le q _ { k } ^ { * } = a \nu / c _ { { } _ { k } } . \operatorname { I f } \underline { { q } } > a \nu / c _ { { } _ { k } }$ the clients’ reservation utility is again given by Equation (6). The prices and liabilities must satisfy $p _ { j } \leq ( a - L _ { j } ) \nu + L _ { j } \beta _ { j } \nu - a \nu \underline { { q } } + ( 1 / 2 ) c _ { k } \underline { { q } } ^ { 2 } .$ . The MSSP’s problem becomes

$$
\max _ {p _ {j}, q _ {s, j}, \beta_ {j}, m} \sum_ {j = 1} ^ {m} \left(p _ {j} - L _ {j} \beta_ {j} v - \frac {1}{2} c _ {s} q _ {s, j} ^ {2}\right),
$$

$$
\text { s.t. } p _ {j} \leq \left(a - L _ {j}\right) v + L _ {j} \beta_ {j} v - a v \underline {{q}} + \frac {1}{2} c _ {k} \underline {{q}} ^ {2} \forall j = 1,..., m.
$$

The procedure to derive the solution to the above problem is similar to that leading to Proposition 1 and Lemma 2. The following proposition characterizes the equilibrium:

Proposition 2: In the presence of system interdependency among the MSSP’s clients, when there is a mandatory security requirement, q<sub>\_</sub>:

(a) $I f { \underline { { q } } } \leq a \nu / c _ { _ k }$ , the results in Lemma 2 apply. The MSSP will supply the security quality stated in the service contract, $q _ { s } ^ { * } = T a \nu / c _ { s }$

(b) $I f \underline { { q } } > a \nu / c _ { _ k } ,$ , the MSSP will supply $\check { q } _ { s } ^ { * } = \check { T } a \nu / c _ { s }$ and set price and liability such that

$$
\check {p} _ {j} ^ {*} - \check {T} a \check {\beta} _ {j} ^ {*} v \left(1 - \frac {\check {T} a v}{c _ {s}}\right) = \frac {\left(\check {T} a v\right) ^ {2}}{c _ {s}} - a v (\check {T} - 1) - a v \underline {{{q}}} + \frac {1}{2} c _ {k} \underline {{{q}}} ^ {2}, \quad j = 1, \dots , \bar {m} ^ {*},
$$

where $\breve { T } \equiv I + e ( \breve { m } ^ { \ast } - I )$ $\breve { m } ^ { * }$ and $\check { q } _ { s } ^ { * }$ solve

$$
\breve {m} ^ {*} = \frac {1}{2} + \frac {a v \bar {q} _ {s} ^ {*} - \frac {1}{2} c _ {s} (\bar {q} _ {s} ^ {*}) ^ {2} - a v \underline {{{q}}} + \frac {1}{2} c _ {k} \underline {{{q}}} ^ {2}}{2 e a v (1 - \bar {q} _ {s} ^ {*})}\tag{14}
$$

and

$$
\stackrel {\smile} {q} _ {s} ^ {*} = \frac {a v}{c _ {s}} \left[ 1 + e (\stackrel {\smile} {m} ^ {*} - 1) \right].\tag{15}
$$

The utility of the $\breve { m } ^ { * }$ clients is the same as in Equation $( 7 ) ,$ , that is, $\breve { u } _ { _ s } ^ { ^ { \ast } } = ( I - a ) \nu +$ $a \nu \underline { { q } } - ( I / 2 ) c _ { k } \underline { { q } } ^ { 2 } .$ . The other $n - \breve { m } ^ { * }$ clients will stay out but obtain the same utility as the m¬ <sup>\*</sup> clients of the MSSP, that is, $\check { u } _ { \scriptscriptstyle k } ^ { \ast } = \check { u } _ { \scriptscriptstyle s } ^ { \ast } .$ . The MSSP’s equilibrium profit is

$$
\breve {\pi} ^ {*} = \breve {m} ^ {*} \left[ \frac {1}{2} \frac {\left(\breve {T} a v\right) ^ {2}}{c _ {s}} + \frac {1}{2} c _ {k} \underline {{q}} ^ {2} - a v \underline {{q}} - a v (\breve {T} - 1) \right].\tag{16}
$$

Similar to the single client case, $i f \underline { { q } } \le \breve { T } a \nu / c _ { s }$ , the equilibrium service quality will exceed the mandatory requirement and the MSSP will be truthful. $I f \underline { { q } } > \breve { T } a \nu / c _ { s }$ the MSSP will claim to supply q<sub>\_</sub> when in fact supplying only $\breve { q } _ { s } ^ { * }$ . The $\breve { m } ^ { * }$ clients again know that the MSSP will shirk, but they will nevertheless use his service.

Here again, if the mandatory security requirement is high $( \underline { { q } } > a \nu / c _ { _ k } )$ , the clients utility will decrease (see Figure 2) because the cost needed to attain such a high requirement exceeds the threat from the hacker. Unlike the single client case, however, the mandatory security requirement will also change the equilibrium service quality when the $\mathrm { M S S P ^ { \prime } s }$ clients’ systems are interdependent, as summarized in the following proposition:

Proposition 3: In the presence of system interdependency among the $M S S P ' _ { s }$ clients, a high mandatory security requirement, $\underline { { q } } > a \nu / c _ { _ k }$ , will increase the equilibrium security service quality and the number of clients outsourcing to the MSSP. It is more likely for the MSSP to truthfully meet the mandatory security requirement.

Figures 4 and 5 illustrate how the security service quality, $\breve { q } _ { s } ^ { * } .$ , and the number of clients outsourcing to the MSSP, $\breve { m } ^ { * }$ , vary with ${ \underline { { q } } } .$

The mandatory security requirement increases the effort needed for in-house development, and so it decreases the clients’ bargaining power against the MSSP. The $\mathbf { M S S P } \mathrm { ^ { \circ } s }$ profit from serving each client would increase, and so he will serve more clients. This increases the overall risk to the $\mathrm { M S S P ^ { \prime } s }$ network due to system interdependency. To ensure that the compensation for security breaches is not excessive, the MSSP will increase his security protection efforts. Hence, the mandatory security requirement will cause more clients to suffer indirect harms from others’ security breaches $( \breve { m } ^ { * } > m ^ { * } )$ , but it will reduce the probability of their systems being directly hacked $( \breve { q } ^ { * } > q ^ { * } )$ . Interestingly, the mandatory security requirement makes the MSSP work harder not because he has an incentive to fulfill the requirement, but because it increases his liability by sending him more clients.

By Proposition 2, the clients who outsource to the MSSP may be variously better or less well protected relative to ${ \underline { { q } } } .$ Although a high $\boldsymbol { \underline { { \underline { { q } } } } }$ increases the protection of some clients (and more clients) against direct hacking $( \check { q } _ { s } ^ { * }$ and $\breve { m } ^ { * }$ increase when $\underline { { q } } > a \nu / c _ { _ k } )$ , it decreases the expected net utility of all clients. From the MSSP’s clients’ perspective, the gain from the $\mathbf { M S S P } \mathrm { ^ { \circ } s }$ protection is offset by the additional threat from the negative spillovers arising from joining an interdependent system. The next proposition shows that such a high mandatory security requirement decreases social welfare too:<sup>13</sup>

![](/api/attachments/SEQG6BHQ/fulltext/images/708b1ee19cb164b9481b38897f907344a897ce41a21642180b67d731a7044db8.jpg)  
Figure 4. Security Service Quality

![](/api/attachments/SEQG6BHQ/fulltext/images/9c2a41a84da2d398a9ea9620c70804ac5258e33e9a3c315fbf125e582217c53f.jpg)  
Figure 5. Number of Outsourcing Clients

Proposition 4: A high mandatory security requirement, $\underline { { q } } > a \nu / c _ { _ k } ,$ , decreases social welfare when the MSSP’s clients are interdependent.

Figure 6 illustrates how the social welfare varies with q<sub>\_</sub>. When $\underline { { q } } > a \nu / c _ { _ k }$ , by Proposition $2 , n - \check { m } ^ { * }$ clients will not be able to outsource and so the high mandatory security requirement would force them to spend more in-house effort. Such extra efforts are socially excessive. Further, by Proposition 3, the high mandatory security requirement would motivate the MSSP to serve more clients. Although more clients can now enjoy the MSSP’s superior cost efficiency, they also increase the size of the MSSP’s network and so increase the system interdependency risks to all outsourcing clients. The MSSP must work harder to protect his clients. This increases the MSSP’s cost and so decreases social welfare as well.

Intuitively, one might think that a high mandatory security requirement should enhance social welfare because it induces the clients and the MSSP to work harder. Propositions 2 and 4, however, indicate otherwise: if the mandatory security requirement is low, it will not affect the equilibrium behaviors; if it is high, then it will expand the MSSP’s clientele, which increases the system interdependency risk and causes wastage in protection efforts. Such a high mandatory security requirement is welfare reducing.

![](/api/attachments/SEQG6BHQ/fulltext/images/5cbbba23bcdede54fc8c45d04c18c445b4ddb63bce3bcad81efcd87983936cc0.jpg)  
Figure 6. Equilibrium Social Welfare

Proposition 4 further characterizes the negative interaction between system interdependency and the mandatory security requirement. By the analysis of the basic model, specifically, Lemma 1 and Proposition 1, without system interdependency, the MSSP will always serve all the clients by supplying the same quality of service. Imposing a mandatory security requirement will only affect the payment from the clients to the MSSP, and it will not affect the equilibrium outcomes. However, when the MSSP’s network exhibits system interdependency, the threat from the hacker to his clients will be amplified. To limit the expected losses of his clients (and to maximize his price), the MSSP will restrict his “output” (i.e., serve fewer clients), which tends to decrease the harm due to spillovers of security breaches. Imposing a high mandatory security requirement, however, will provide a wrong incentive—it encourages the MSSP to serve more clients, which increases the system interdependency risks. The MSSP then has to work harder to address such risks, therefore social welfare decreases. Accordingly, if system interdependency is prevalent (e.g., when an MSSP uses a common set of technology or platform to serve all the clients), imposing a high security requirement is generally not advised.<sup>14</sup>

## Verifiability

So far our analysis has assumed that the clients cannot verify the MSSP’s protection efforts. Prior studies have shown that verifiability plays an instrumental role in facilitating efficient service quality and social welfare [19]. We now investigate if a mandatory security requirement would affect this conclusion. In particular, if the clients can verify the MSSP’s effort, then the MSSP will not be able to shirk and must supply the quality of service specified in the service contract. We modify Assumption 8 as follows:

Assumption $g ^ { \prime } { } _ { ; }$ The client must invest up to q<sub>\_</sub> if she develops the protection inhouse. The client can verify the MSSP’s effort if she outsources the protection.

Referring to Proposition 2b, when the mandatory security requirement, $\underline { { q } } \le \breve { T } a \nu / c _ { s }$ , the MSSP will always truthfully supply the optimal service quality, and so verifiability has no impact on the equilibrium outcome. When $\underline { { q } } > \check { T } a \nu / c _ { s }$ and the MSSP cannot shirk, he must now supply $\check { q } _ { s } ^ { * } = { \underline { { q } } }$ instead of Tèav/c . Perhaps not surprisingly, the inability of the MSSP to choose an optimal $\check { q } _ { s } ^ { * }$ implies a reduction in profit as well as social welfare. The next proposition summarizes the outcome of this scenario:

Proposition 5: With verifiability, $i f \underline { { q } } \le \breve { T } a \nu / c _ { s }$ , the results in Proposition 2 apply; imposing verifiability does not affect the equilibrium outcomes. If, however, $\underline { { q } } > \breve { T } a \nu / c _ { s }$ , then in the equilibrium with verifiability, the MSSP’s profit and social welfare will decrease, but his clients will be better protected against direct hacking.

Without verifiability, when $\underline { { q } } > \check { T } a \nu / c _ { s }$ , by Proposition 2, the MSSP will shirk by supplying a lower quality service, $\check { q } _ { s } ^ { * } = \check { T } a \nu / c _ { s }$ . This decreases the $\mathbf { M S S P } \mathrm { ^ { \circ } s }$ costs and so increases his profit. With verifiability, the MSSP could no longer exploit his clients by shirking. Instead, the MSSP must diligently supply ${ \underline { { q } } } ,$ , which increases his cost and erodes his profit. The MSSP’s effort will be socially excessive because the threat faced by the clients does not call for $\check { q } _ { s } ^ { * } = q$ . Accordingly, imposing verifiability would cause the MSSP to work too hard, which decreases social welfare.

Hence, from a social welfare perspective, it is not advisable for the clients to verify or audit the $\mathrm { M S S P ^ { \prime } s }$ effort. Shirking could be good for the society when the security risk is low and when the clients are mandated to have a higher level of security protection. Figure 7 summarizes the equilibrium outcomes with/without verifiability under different mandatory security requirements. The shaded areas correspond to the setting with social welfare losses. Figure 8 plots the social welfare outcomes. It is clear that only our main configuration, without verifiability, would achieve the social optimum for all levels of $\underline { { q } } . ^ { 1 5 }$

Because of asymmetric information, clients often cannot ascertain whether the MSSP will work hard. To address such uncertainty, an increasingly popular practice is to engage security service auditing [39]. Our analysis shows that such auditing may in fact decrease social welfare when there exists a high mandatory security requirement.

We conclude this section by stating the impact if the MSSP cannot commit to compensating the clients in the event of security breaches. Without the compensation, the MSSP will always shirk after the clients have decided to outsource the protection to him. The clients rationally expect this, and so in most cases they would rather choose to develop the security protection in-house. Nevertheless, when the mandatory security requirement is excessively high, the clients may find that it is cheaper to engage the MSSP to satisfy the requirement. Hence, the clients may even be willing to pay the MSSP despite knowing that he will not work hard to protect them. Overall, the social welfare always decreases when the MSSP cannot commit to compensate his clients. Hence, in information security outsourcing, liability (e.g., by including damage-tied compensation terms in the SLA) may play a more important role than auditing.

<table><tr><td>With verifiability</td><td> $m^{*}$  clients outsource,  $q^{*} = \frac{Tav}{c_{s}}$ ; $n - m^{*}$  clients develop in-house, $q_{k} = \frac{av}{c_{k}} < \frac{Tav}{c_{s}}$ ;Utility of each client $= (1 - a)v + \frac{1(av)^{2}}{2c_{k}}$ .MSSP truthfully supplies $q^{*} = \frac{Tav}{c_{s}} > \underline{q}$ ;</td><td> $\breve{m}^{*} > m^{*}$  clients outsource,  $\breve{q}^{*} = \frac{\breve{T}av}{c_{s}}$ ; $n - \breve{m}^{*}$  clients develop in-house, $q_{k} = \underline{q} < \frac{\breve{T}av}{c_{s}}$ ;Utility of each client $= (1 - a)v + av\underline{q} - \frac{1}{2}c_{k}\underline{q}^{2}$ .MSSP truthfully supplies $\breve{q}^{*} = \frac{\breve{T}av}{c_{s}} \geq \underline{q}$ .</td><td> $m_{v}^{*}$  clients outsource,  $q_{v}^{*} = \underline{q}$ ; $n - m_{v}^{*}$  clients develop in-house, $q_{k} = q_{v}^{*} = \underline{q}$ ;Utility of each client $= (1 - a)v + av\underline{q} - \frac{1}{2}c_{k}\underline{q}^{2}$ .MSSP truthfully supplies $q_{v}^{*} = \underline{q}$ .</td></tr><tr><td>Without verifiability(the main model)</td><td> $m^{*}$  clients outsource,  $q^{*} = \frac{Tav}{c_{s}}$ ; $n - m^{*}$  clients develop in-house, $q_{k} = \frac{av}{c_{k}} < \frac{Tav}{c_{s}}$ ;Utility of each client $= (1 - a)v + \frac{1(av)^{2}}{2c_{k}}$ .</td><td> $\breve{m}^{*} > m^{*}$  clients outsource,  $\breve{q}^{*} = \frac{\breve{T}av}{c_{s}}$ ; $n - \breve{m}^{*}$  clients develop in-house, $q_{k} = \underline{q} < \frac{\breve{T}av}{c_{s}}$ ;Utility of each client $=(1 - a)v + av\underline{q} - \frac{1}{2}c_{k}\underline{q}^{2}$ .MSSP truthfully supplies $\breve{q}^{*} = \frac{\breve{T}av}{c_{s}} \geq \underline{q}$ .</td><td> $\breve{m}^{*} > m^{*}$  clients outsource,  $\breve{q}^{*} = \frac{\breve{T}av}{c_{s}}$ ; $n - \breve{m}^{*}$  clients develop in-house, $q_{k} = \underline{q} > \frac{\breve{T}av}{c_{s}}$ ;Utility of each client $=(1 - a)v + av\underline{q} - \frac{1}{2}c_{k}\underline{q}^{2}$ .MSSP shirks by supplying $\breve{q}^{*} = \frac{\breve{T}av}{c_{s}} < \underline{q}$ ;</td></tr><tr><td></td><td> $\frac{av}{c_{k}}$ </td><td> $\frac{\breve{T}av}{c_{s}}$ </td><td> $\underline{q}$ </td></tr></table>

Figure 7. Equilibrium Outcomes

![](/api/attachments/SEQG6BHQ/fulltext/images/fe8846a99aad86945de965a3aa032713c4c3ebf72c8e2320b42c88d4fe9b3bd5.jpg)  
Figure 8. Social Welfare with Different Contracting Instruments

## Extensions

We assess th e robust ness of our findings by relaxing several assumptions in the above analysis. For each of the following extensions we use the model with system interdependency, e, and mandatory security requirement, ${ \underline { { q } } } ,$ as the benchmark.

## Heterogeneous Clients

We first consider the case with heterogeneous clients. Specifically, we modify Assumptions 1′ and 5 as follows:

Assumption $I ^ { \prime \prime } { : }$ There are $n _ { \scriptscriptstyle I }$ high-type and $n _ { o }$ low-type clients, and one MSSP. The high types value their system at $\nu _ { \jmath }$ . The low types value their system at $\nu _ { o } < \nu _ { I }$ The clients’ systems become interdependent if they use the MSSP’s service. If one client’s system is compromised, then each of the other MSSP’s clients will incur a loss of $e \nu _ { t } , t = 0 , I ,$ , where e is an arbitrarily small constant.

Assumption $5 ^ { \prime } \colon \nu _ { o } , \nu _ { _ { I } } , c _ { _ { k } } , c _ { _ s }$ , and a are public information. Further, the MSSP can accurately diagnose and separate the high-type and low-type clients.

Assumption $5 ^ { \prime }$ ensures that the MSSP could assess the reservation utility of the clients, so he does not need to practice indirect price discrimination (e.g., segmenting the clients with incomplete information about their valuations) [41]. Considering indirect price discrimination will complicate the analysis without giving much insight into the influence of a mandatory security requirement. In any case, the MSSP often needs to conduct on-site preassessments before committing to serving the clients.<sup>16</sup> $\mathrm { S o } .$ it is reasonable to assume that the MSSP knows the clients’ values.

Similar to the analysis in the previous section, if client type $t , t = 0 , 1$ , developed the security protection in-house, her net utility would be $u _ { { } _ { k , t } } = ( 1 - a ) \nu _ { { } _ { t } } + ( 1 / 2 ) ( ( a \nu _ { { } _ { t } } ) ^ { 2 } / c _ { { } _ { k } } )$ if $\underline { { q } } < a \nu _ { t } / c _ { k }$ and $u _ { { } _ { k , t } } = ( 1 - a ) \nu _ { { } _ { t } } + a \nu _ { { } _ { t } } \underline { { { q } } } - ( 1 / 2 ) c _ { { } _ { k } } \underline { { { q } } } ^ { 2 }$ otherwise. Suppose that in equilibrium the MSSP would serve $m _ { 1 }$ high-type and $m _ { 0 }$ low-type clients. Then, if client j of type t outsources the protection to the MSSP, her expected net utility would be

$$
u _ {s, t, j} = \left(1 - L _ {t, j}\right) v _ {t} + L _ {t, j} \beta_ {t, j} v _ {t} - p _ {t, j},
$$

where

$$
L _ {t, j} \equiv a (1 - q _ {s, t, j}) + e a \sum_ {i = 1, i \neq j} ^ {m _ {t}} (1 - q _ {s, t, i}) + e a \sum_ {i = 1} ^ {m _ {1 - t}} (1 - q _ {s, 1 - t, i}).
$$

For the clients to outsource to the MSSP, we must have $u _ { s , t , j } \geq u _ { k , t }$ , that is, $p _ { t , j } ^ { } \leq ( 1 - L _ { t , j } ) \nu _ { t } ^ { } +$ $L _ { { _ t } , j } \mathbb { \beta } _ { { _ t } , j } \nu _ { { _ t } } { - u } _ { k , t }$ . The MSSP’s problem becomes

$$
\begin{array}{l} \max _ {p _ {t, j}, q _ {s, t, j}, \beta_ {t, j}, m _ {t}} \sum_ {t = 0, 1} \sum_ {j = 1} ^ {m _ {t}} \left(p _ {t, j} - L _ {t, j} \beta_ {t, j} v _ {t} - \frac {1}{2} c _ {s} q _ {s, t, j} ^ {2}\right) \\ \text { s.t. } p _ {t, j} \leq \left(1 - L _ {t, j}\right) v _ {t} + L _ {t, j} \beta_ {t, j} v _ {t} - u _ {k, t} \forall t = 0, 1 \text { and } j = 1,..., m _ {t}. \end{array}
$$

It is straightforward to show that, in equilibrium,

$$
q _ {s, t, j} ^ {*} = q _ {s, t} ^ {*} = \frac {a \left[ 1 + e \left(m _ {t} ^ {*} - 1\right) \right] v _ {t} + e a m _ {1 - t} ^ {*} v _ {1 - t}}{c _ {s}}\tag{17}
$$

and

$$
m _ {t} ^ {*} = \frac {1}{2} + \frac {(1 - a) v _ {t} + a v _ {t} q _ {s , t} ^ {*} - u _ {k , t} - \frac {1}{2} c _ {s} (q _ {s , t} ^ {*}) ^ {2}}{2 e a v _ {t} (1 - q _ {s , t} ^ {*})} - \frac {m _ {1 - t} ^ {*}}{2} \left(\frac {v _ {1 - t}}{v _ {t}} + \frac {1 - q _ {s , 1 - t} ^ {*}}{1 - q _ {s , t} ^ {*}}\right),\tag{18}
$$

$t = 0 , 1$ . Hence, the two types of clients will receive a different quality of service. Similar to the case with homogeneous clients, the $\mathbf { M S S P } \mathbf { \bar { s } }$ clients will receive better protection against direct hacking because the MSSP will work extra hard to internalize the losses that arise from system interdependency. By Equation (17), the MSSP’s extra effort is a function of the number of each type of clients that he serves, weighted by their valuations for their systems, $\nu _ { _ t }$ . Further, by Equation (18), the two types of clients are substitutes for the MSSP; if he serves more type t clients, then he will serve fewer 1 – t type clients.

Note that Equations (17) and (18) are direct generalizations of the solutions in Lemma 2 and Proposition 2, and so our basic conclusions remain unchanged. If the mandatory security requirement is sufficiently high to the extent that $\underline { { q } } > a \nu _ { _ 1 } / c _ { _ k }$ , then both $m _ { 0 } ^ { * }$ and $m _ { 1 } ^ { * }$ will increase, that is, the MSSP will serve more clients of both types. By Equation (17), the service quality, $q _ { s , t } ^ { * } .$ , is a positive function of $m _ { 0 } ^ { * }$ and $m _ { 1 } ^ { * }$ , and so it will unambiguously increase too.<sup>17</sup>

Because a high security requirement, $\underline { { q } } > a \nu _ { _ 1 } / c _ { _ k }$ , would motivate the MSSP to serve more clients, which is the key reason driving the expected social losses arising from spillovers, and hence, the results in Proposition 4, the incorporation of client heterogeneity will not change our conclusions. A high mandatory security requirement will decrease social welfare, particularly with system interdependency.

## Competition

We next explore the consequence of introducing competition. We modify Assumption 1′ by allowing for z identical MSSPs in the market and keep all the other assumptions. We use the Bertrand–Nash equilibrium concept.

Suppose that z is sufficiently large to the extent of perfect competition. Then, the MSSPs must price their service at marginal cost [19] and therefore earn zero profit. In this case, the MSSPs will not be able to exploit their clients even when there is a high mandatory security requirement. Accordingly, for each MSSP, $\pi = p _ { _ j } - L _ { _ j } \beta _ { _ j } \nu -$ $( 1 / 2 ) c _ { s } q _ { s , j } ^ { 2 } = 0$ , and so $p _ { j } - L _ { j } \beta _ { j } \nu = ( 1 / 2 ) c _ { s } q _ { s , j } ^ { 2 }$ . Substituting $p _ { j }$ into Equation (9) and maximizing, all MSSPs will choose $q _ { c } ^ { ~ * } = ( a \nu / \bar { c } _ { s } ) [ 1 + e ( m _ { c } ^ { * } - 1 ) ]$ . Since the expected loss due to system interdependency increases in m, without other sources of heterogeneity, we will have the same $m _ { c } ^ { * } = n / z$ among all z MSSPs.<sup>18</sup> All the clients will outsource their security protection. Social welfare will be maximized.

Next, if the market is an oligopoly with only a few MSSPs to the extent that $z { \check { m } } ^ { * } \leq n ,$ then the results in Proposition 2 apply. Each MSSP will serve an “island” of m=<sup>\*</sup> clients. The MSSPs will fully exploit the pricing power granted to them by a high mandatory security requirement, and so they will serve too many clients, which escalates the system interdependency risks. Relative to the case with one MSSP, social welfare will increase because more MSSPs could make a profit. But it will still be lower than that in perfect competition because some excluded clients will work too hard, whereas the outsourcing clients will face excessive risks of system spillovers.

Finally, if $z { \check { m } } ^ { * } > n$ but the competition is not keen enough $( \mathrm { i . e . , } z$ is not so large) to drive the MSSPs’ price down to marginal cost, then the equilibrium may feature mixed strategies over m, p (and so b), and $q ,$ and all the clients will outsource to the MSSPs. We leave the exploration of such a mixed strategy equilibrium to future research. Nevertheless, as long as the MSSPs cannot fully exploit their pricing power, the social welfare in this scenario should lie between the perfect competition and the oligopoly cases. Overall, competition tends to weaken the (negative) social welfare impact of a high mandatory security requirement, but it may not completely undo the “damage” of such a requirement.<sup>19</sup>

## Strategic Hacking

We now endogenize the hacker’s choice of attack coverage, A [11, 15, 35, 42]. We follow the structure in Hausken [26] and Png and Wang [42] and modify Assumption $2 ^ { \prime }$ as follows:

Assumption $2 ^ { \prime \prime } \cdot$ : A hacker attacks A out of the n clients, $O \leq A \leq n$ . The total cost of attacking A clients is an increasing convex function, $( l / 2 ) c _ { h } A ^ { 2 } ;$ , where $c _ { _ h }$ is an arbitrary cost coefficient. The hacker obtains a benefit, b, from each successful attack. The A attacks are independent and uniformly distributed among the n clients. Hence, the probability of each client being attacked, $a = A / n , O \leq a \leq I$ The hacker moves simultaneously with the clients and the MSSP.

We separate the analysis into two cases:

Case (i): $\underline { { q } } \le a \nu / c _ { _ k }$ . The equilibrium choices of the clients and MSSP follow Lemma 2. The hacker’s utility function becomes

$$
\begin{array}{c} u _ {h} = b \Bigg [ A \bigg (\frac {m}{n} \bigg) \big (1 - q _ {s} \big) + A \bigg (\frac {n - m}{n} \bigg) \big (1 - q _ {k} \big) \Bigg ] - \frac {1}{2} c _ {h} A ^ {2} \\ = A b \Bigg [ \big (1 - q _ {k} \big) - \frac {m}{n} \big (q _ {s} - q _ {k} \big) \Bigg ] - \frac {1}{2} c _ {h} A ^ {2}. \end{array}\tag{19}
$$

The first term in Equation (19) is the expected number of clients, including those who are variously using/not using the MSSP’s service, whose systems were successfully compromised by the hacker, multiplied by the hacker’s benefit, b. The second term is the hacker’s cost of launching the A attacks. Differentiating with respect to A,

$$
A ^ {*} = \frac {b}{c _ {h}} \left[ \left(1 - q _ {k}\right) - \frac {m}{n} \left(q _ {s} - q _ {k}\right) \right].\tag{20}
$$

Together with Equations (11) and (12), and $q _ { k } ^ { * } = a \nu / c _ { k }$ , we could solve for the equilibrium m<sup>\*</sup>, $q _ { s } ^ { * } , q _ { k } ^ { * }$ , and $a ^ { * } = A ^ { * } / n$ . Note that since the equilibrium a<sup>\*</sup> is endogenous, the constraint $\underline { { q } } \le a \nu / c _ { _ k }$ is no longer absolute but depends on the strategic actions of the hacker, the MSSP, and the clients.

Case (ii): $\underline { { q } } > a \nu / c _ { _ k }$ . The equilibrium choices of the clients and MSSP follow Proposition 2b. The hacker’s utility function is

$$
u _ {h} = A b \left[ (1 - \underline {{{q}}}) - \frac {m}{n} (q _ {s} - \underline {{{q}}}) \right] - \frac {1}{2} c _ {h} A ^ {2}.\tag{21}
$$

Differentiating with respect to A, we have

$$
\check {A} ^ {*} = \frac {b}{c _ {h}} \left[ (1 - \underline {{q}}) - \frac {m}{n} (q _ {s} - \underline {{q}}) \right].\tag{22}
$$

Together with Equations (14) and (15), we could solve for the equilibrium, $\breve { m } ^ { * }$ $\check { q } _ { s } ^ { \ast } , \check { q } _ { k } ^ { \ast }$ , and $\Breve { a } ^ { * } = \Breve { A } ^ { * } / n$

The explicit solutions to the above problems are intractable. However, from the implicit functions, we could draw the following conclusions:<sup>20</sup>

a. $\partial A ^ { * } / \partial q _ { s } < 0 , \partial \check { A } ^ { * } / \partial q _ { s } < 0 , \partial A ^ { * } / \partial q _ { k } < 0$ , and $\partial \check { A } { } ^ { * } / \partial q _ { _ k } = 0$ . So, the hacker’s attack would generally decrease with the clients’ and MSSP’s protection efforts.

b. $\partial A ^ { * } / \partial m < 0$ and ${ \partial \check { A } ^ { * } } / { \partial m } < 0$ if and only if $q _ { s } \ge q$ . In other words, the likelihood of the hacker’s attack decreases with the size of the clientele of the MSSP only if the MSSP works hard. If the MSSP shirks by undersupplying quality relative to ${ \underline { { q } } } ,$ the hacker would actually tend to launch more attacks as more clients outsource to the MSSP.

c. When $\underline { { q } } \le a \nu / c _ { _ k }$ , that is, the mandatory security requirement is not binding, $( \partial / \partial A ) ( \partial u _ { _ k } / \partial q _ { _ k } ) > 0$ and $( \partial / \partial A ) ( \partial \pi / \partial q _ { \mathrm { s } } ) > 0$ . In other words, the ${ \bf M S S P } \mathrm { \ ' } _ { \mathrm { s } }$ and the clients’ efforts increase with the hacker’s attack. The sign of (∂/∂A)(∂p/∂m) is, however, ambiguous.

d. When $\underline { { q } } > a \nu / c _ { _ k } ,$ that is, the mandatory security requirement is binding, $( \partial / \partial A ) ( \partial \breve { u } _ { _ k } / \partial q _ { _ k } ) = 0$ and $( \partial / \partial A ) ( \partial \breve { \pi } / \partial q _ { \mathrm { { s } } } ) > 0$ . The clients who are not outsourcing will not be affected by a marginal change in A because they have to choose q<sub>\_</sub> anyway. The $\mathbf { M S S P } \mathbf { \vec { s } }$ effort increases with the hacker’s attack. Further, $( \partial / \partial A ) ( \partial \breve { \pi } / \partial m ) > 0$ . Therefore, the number of clients served by the MSSP also increases with the hacker’s attack.

e. When $q > a \nu / c _ { _ k } , \partial \check { A } ^ { \ast } / \partial { { q } } < 0$ . That is, if the mandatory security requirement is binding, further increasing it could indeed decrease the hacker’s attack.

The effect characterized in (e) tends to counteract the welfare-reducing effect of q<sub>\_</sub> in Proposition 4. A high mandatory security requirement may decrease social welfare because of the strategic responses of the MSSP and of the clients to deploy excessive protections. These strategic behaviors, however, do decrease the success rate of attacks, and hence will dissuade the hacker from launching more attacks, which may increase social welfare. The net effect of such a high q<sub>\_</sub> on social welfare is ambiguous.

However, the above analysis rests on the assumption that the hacker can choose to attack any number of clients. What if the hacker faces a binding resource constraint (e.g., time taken to study the clients’ systems and network configurations) so that there is an upper limit of number of clients that it can attack, $\overline { { A } } , A \leq \overline { { A } } \ll n ?$ If $\bar { A }$ is binding, then the hacker’s strategic responses in Equations (20) and (22) become irrelevant. It will always choose the maximum attack intensity, A<sup>ÿ</sup>. The welfare-enhancing effect of a reduced A due to the MSSP’s and the clients’ strategic responses to the mandatory security requirement, q<sub>\_</sub>, that we characterized in (e) above will become moot. Then, obviously, Proposition 4 applies. Imposing a high q<sub>\_</sub> will decrease social welfare particularly when the MSSP’s clients’ systems are interdependent. A high mandatory security requirement may enhance social welfare only when the hacker has slack resources.<sup>21</sup>

Finally, what if the hacker is thrill-seeking in the sense that it attacks the clients systems for pleasure, and it responds by more attacks if the defense put up at the MSSP’s/clients’ side is stronger [26]? In this case, A<sup>\*</sup> would increase with $q _ { s } ^ { * }$ and $q _ { k } ^ { * }$ or $\breve { q } _ { s } ^ { * }$ and $\breve { q } _ { k } ^ { \ast }$ , which would obviously decrease social welfare. It will be undesirable to impose a high mandatory security requirement, ${ \underline { { q } } } ,$ in the presence of such a hacker.

## Shirking Clients

We have assumed that the MSSP can shirk but the clients cannot. What if it is the opposite, that is, the clients can shirk but the MSSP cannot? Obviously, if $\underline { { q } } \le a \nu / c _ { { _ k } } ,$ then Lemma 2 applies because $\underline { { q } }$ is not binding. The MSSP will supply the optimal service quality, $q _ { s } ^ { * } = T a \nu / c _ { s } > a \nu / c _ { k } \geq \underline { { q } } . \mathrm { { I f } } \underline { { q } } > a \nu / c _ { k }$ and the clients can shirk, then the clients will simply ignore the mandatory security requirement. So, by Equation (1), their reservation utility becomes $u _ { k } ^ { \ast } = ( 1 - a ) \nu + ( 1 / 2 ) ( ( a \nu ) ^ { 2 } / c _ { k } )$ for all levels of q<sub>\_</sub>, and by Equations (1) and (9), the pricing constraint is always $p _ { _ { j } } \leq ( a - L _ { _ { j } } ) \nu + L _ { _ { j } } \beta _ { _ { j } } \nu - ( 1 / 2 ) ( ( a \nu ) ^ { 2 } / c _ { _ { k } } )$ Accordingly, Lemma 2 will also apply for all $a \nu / c _ { _ k } < \underline { { q } } \leq T a \nu / c _ { _ s }$

![](/api/attachments/SEQG6BHQ/fulltext/images/ef639a3cbad76cf95678a77ee229a7da369c8be62bd9aae841de6f74a80bc7b5.jpg)  
Figure 9. Comparison of Social Welfare

Next, if $\underline { { q } } > T a \nu / c _ { s } .$ , that is, the mandatory security requirement exceeds what the MSSP will supply voluntarily, then the situation is similar to the setting with verifiability (where the MSSP must also work hard), except that the MSSP’s price for serving each client is subject to a tighter constraint because the clients now have a higher reservation utility, $u _ { k } ^ { * }$ . So, as in Proposition 5, if there is a high mandatory security requirement, $\underline { { q } } > T a \nu / c _ { s }$ , and the MSSP cannot shirk but the clients can, then the MSSP’s profit and social welfare will decrease.

Finally, if we allow both the MSSP and the clients to shirk, then the mandatory security requirement is immaterial. The results in Lemma 2 apply directly.

In fact, our analysis can be conceptually organized as follows: the basic setting with no mandatory security requirement (denote that setting as “no req”) gives rise to Lemma 2, which also gives the first-best social welfare. Proposition 2 builds on “no req” by imposing $\underline { { q } }$ and allowing the MSSP to shirk (denote it as “MSSP shirk”). The analysis of verifiability (Proposition 5) builds on “MSSP shirk” by removing the shirking option from the MSSP (denote it as “diligent”). The analysis here also builds on “MSSP shirk” by removing the shirking option from the MSSP and giving it to the clients (denote this setting as “clients shirk”). Then, Proposition 4 states that the social welfare in “no req” ≥ that in “MSSP shirk.” Proposition 5 says that the social welfare in “MSSP shirk” ≥ that in “diligent,” and the result in this section indicates that the social welfare in “no req” ≥ that in “clients shirk.” Figure 9 shows how the social welfare may vary with $\underline { { q } }$ in these four scenarios.<sup>22</sup> Clearly, the social welfare is highest if we do not impose a high mandatory security requirement.

## Implications

Our main result s indicat e th at wh en cl ient s are l ess capabl e of information security protection, and when they are mandated to enhance their protection, they may outsource to an MSSP despite knowing that he will shirk and underprovide quality. The benefit of such outsourcing, however, may be offset by the interdependency risks [33] that arise when the MSSP serves multiple clients. With system interdependency, a mandatory security requirement may distort the clients’ and the MSSP’s equilibrium behaviors and cause undue social welfare losses.

We found that a stringent mandatory security requirement would shift the surplus from clients to the MSSP, which would cause the MSSP to expand his service coverage to more clients. This could be socially detrimental when the clients’ systems become interconnected after outsourcing to the MSSP. To some extent, the MSSP’s network becomes a “single point of failure”—any security breach of a node may spill over to others.<sup>23</sup> Although the MSSP would exert more effort to protect each of his clients when the size of his network grows, the benefit of such additional efforts will be offset by the increased threat from system spillovers.

There has been a greater call for mandatory security requirements to stem the tide of widespread security concerns. For instance, the Chinese government had proposed that every personal computer (PC) sold in China should be preinstalled with the GDYE software, which was designed to filter content downloaded to the PC. The way GDYE works is similar to antivirus software. Once installed, it will automatically download a list of prohibited sites from an online database and record users’ data. However, it has been found that GDYE itself introduces “remotely exploitable vulnerabilities” [57]. It contains programming errors, which “allow malicious sites to steal private data, send spam, or enlist the PC in a botnet” [57]. The proposed requirement was subsequently eliminated for all home computers because of widespread objections.

Another mandatory security initiative proposed by the industry was to apply the public health model to the Internet [14, 44]. The idea is that computing devices should be granted access to the Internet only if consumers can demonstrate that they are “healthy” (i.e., free of viruses, spyware, and other security vulnerabilities). Consumers must use well-accepted protection mechanisms to secure their computing resources. An infrastructure of “health certificates” can be used to notarize the security check. It is further suggested that “access providers and other organizations must have a way to request health certificates and take appropriate action based upon the information provided” [14, p. 6].

Our analysis suggests that these initiatives should be exercised with caution. Although mandatory security requirements such as the GDYE or “certification of inoculation” may force more clients to outsource and thus help realize cost savings and a higher level of protection, it also opens them to interdependency risks. It is important to recognize system interdependency as a countervailing factor in security outsourcing.

We also examined the impact of a commonly used measure in information security outsourcing—verifiability [19]. Auditing MSSPs’ behaviors (verifiability) has often been regarded as being important for clients. Although verifiability has been found to ensure social efficiency in the contexts of many other credence goods such as medical treatments or mechanical repairs [19], our analysis suggests that we should not impose it in managed security services. The point of departure here is that the “treatment”—a high level of security protection—is mandatory, which will cause excessive protection and outsourcing. The irony is that verifiability would then remove any room for an MSSP to shirk, which generates socially excessive protection.

Our analysis shows that a carefully examined liability, one that is determined according to the expected risk of the clients, would suffice to motivate the MSSP to serve clients efficiently. Ex post compensations may outperform auditing in facilitating security outsourcing.<sup>24</sup>

Finally, we have extended our model by including a heterogeneous mixture of clients, competition, strategic hacking, and shirking clients, and showed that our main conclusions are robust with respect to these variations.

## Conclusions

Informat ion t ech nol ogy out sourcing is inh erentl y costl y—the outsourcer typically needs to invest significant efforts to search for, contract with, and continuously manage a service provider [8]. Notwithstanding these obvious cost considerations, in the case of information security, encouraging too much outsourcing by imposing mandatory security requirements may not be good for the society. It is important to understand the motivations and implications of information security outsourcing before we could devise a proper environment to realize its potential benefits. This study serves just such a purpose.

Our analysis can be extended in multiple ways. We have assumed a monopoly security outsourcing market. Although we have examined the implications of competition, it would be more general to consider heterogeneous MSSPs in terms of their cost structure or security expertise, or perhaps their reputations. Also, we have assumed that the clients can estimate their own risks and therefore know the level of security protection that they need. A full analysis of information security as a credence good should consider settings whereby the clients do not know what they need. It would be important to incorporate the quality of diagnosis in such a setting. It would be interesting to see if a mandatory security requirement and liability would produce similar conclusions in such a setting, too.

Lastly, the success of information security outsourcing arguably rests not only on the MSSPs’ but also on the clients’ efforts. For example, if the clients do not properly secure their internal computer accounts or transmission media, which connect their systems to an MSSP’s network, then their systems will be vulnerable regardless of how much effort the MSSP invests to strengthen security. How the strategic interaction between the MSSP and his clients shapes the quality of a security system, and how the threats posed by malicious hackers affect such strategic interaction, are important questions for future research.

## Not es

1. This result is consistent with industry observations that firms often expend little effort to monitor the MSSP. In particular, only 20 percent of firms in the technology, media, and telecommunications industries would audit their outsourcing service providers’ activities [36]. Two-fifths of large organizations do not include security provisions in their outsourcing contracts at all, including many whose MSSPs are hosting highly confidential information [29].

2. In fact, anecdotal evidence has shown that security outsourcing may not necessarily lead to better security. A recent industry report has indicated that many firms in the United Kingdom believe that their security has neither improved nor deteriorated after using the external services [29]. The Australian Business Assessment of Computer User Security (ABACUS) survey has found that businesses that outsource their computer security are more likely to report breach of security incidents [45]. In this paper, social welfare is defined as the sum of client utility and MSSP’s profit.

3. The literature has also considered cyber insurance as a means to manage information security risks but has mostly concluded that it is ineffective [9]. For a detailed discussion, see Bandyopadhyay et al. [7].

4. Our formulation of client utility, which characterizes the expected loss as the product of the threat of attack, a, security vulnerability, $1 - q _ { k } ,$ and monetary value, v, is similar to that in Gordon and Loeb [24]. Throughout this paper we use the subscripts k for the client and s for the MSSP.

5. Mandatory security requirement is now quite common among organizations. For example, the European Union Data Protection Directive 95/46/EC requires firms to take reasonable measures to secure data from potential abuses. In the United States, the Federal Information Security Management Act of 2002 requires each federal agency to provide appropriate security protection for its systems. The Gramm–Leach–Bliley Act requires financial institutions to protect the security of customer data. The Health Insurance Portability and Accountability Act requires health care providers to adopt appropriate administrative and technical protections of consumers’ health information. In the private sector, the ISO 27000 series requires firms to design and implement good information security management systems. Some professional associations, such as the ISM3 Consortium, are now promoting security maturity models (SMMs) that encompass various sets of security performance targets and systems configurations. In the Shirking Clients extension below we consider the scenario when the client can also shirk with in-house development.

6. We add a breve, <sub>˘</sub>, for all results with a mandatory security requirement.

7. We used the following parameters to generate Figures 2 and $3 \colon c _ { s } = 1 , c _ { k } = 2 .$ , and $\nu = 1 0$ Further, for Figures 4–6, we added $n = 1 5 , A = 0 . 5$ , and $e = 0 . 0 1$ (refer to the discussion in the next section).

8. We assume that e is sufficiently small and that security outsourcing is feasible in the presence of system interdependency. Specifically, $e < ( 1 / ( n - 1 ) ) ( ( c _ { \ast } / a \nu ) - 1 )$ , which, as we s shall see below, ensures that $q \leq 1$

9. For example, the MSSP needs to study each client’s system and devise corresponding procedures and/or adjustments to integrate the security protection functions.

10. Since the clients and the MSSP have common knowledge on all the model parameters, in equilibrium the clients will rationally expect the MSSP’s service coverage, m, and the MSSP will fulfill such an expectation.

11. We model the hacker’s attack as random draws without replacement. So, the expected number of systems (excluding $j )$ compromised by the hacker is the proportion of clients effectively protected by the MSSP, $\Sigma _ { i = 1 , i \neq j } ^ { m } ( \bar { 1 } - q _ { i } ) / ( n - 1 )$ , multiplied by the hacker’s attack coverage, which is, ex post, na – 1 when client j was attacked and na when client j was not attacked. We assume that the client population is sufficiently large relative to the hacker’s attack coverage, A (which, given $n ,$ determines $a )$ , the number of ${ \bf M S S P } \mathrm { ^ { * } s }$ clients, $m ,$ and the spillover, $e ,$ to the extent that $L _ { \mathrm { * } } \leq 1$ . An alternative approach to model this problem is to assume that client j suffers at most once from other clients’ security breaches, which would then ensure that $L _ { \mathrm { \it { i } } } \leq 1$ Such a model is, however, analytically intractable. The key contribution of our analysis lies in accounting for spillover among the $\mathrm { M S S P ^ { \prime } s }$ clients due to security interdependency. The functional form of such spillover is of secondary importance (see also [55]).

12. By Equation (12), because the equilibrium $q _ { s } ^ { * }$ increases in m<sup>\*</sup>, the chance for the MSSP’s clients’ systems to be directly hacked, $a ( 1 - q ^ { * } )$ , decreases with multiple interdependent clients. Their utility in Lemma 2 stays the same as that in Lemma 1 because of the negative spillovers from others.

13. We define social welfare as the sum of all n clients’ utilities and the MSSP’s profit.

14. It is straightforward to prove the “dual” version of Proposition 4—that is, the decrease in social welfare due to system interdependency is particularly large when the mandatory security requirement is high, $\mathrm { \Delta } q > a \nu / c _ { \mathrm { \Delta } _ { k } }$ . The implication is that with a high mandatory security requirement, it is better to encourage the MSSP to “disconnect” his clients. This could be achieved by, for example, using separate server management systems and segmented or independent service platforms. In practice, however, it seems easier to adjust the security requirement level than to change the technology for managed security services.

15. We used the following parameters to generate Figure 8: $n = 1 0 , c _ { s } ^ { \mathrm { ~ ~ } } = 1 , c _ { { \scriptscriptstyle k } } ^ { \mathrm { ~ ~ } } = 1 . 2 5 , \nu = 5 0 ,$ $A = 0 . 0 5 , e = 0 . 0 8$

16. For example, both the IBM Payment Card Industry (PCI) solution and Motorola’s security assessment solution highlight assessment service as a key feature of their solutions.

17. If, however, $a \nu _ { \mathrm { 0 } } / c _ { k } < \underline { { q } } \le a \nu _ { \mathrm { 1 } } / c _ { k }$ , then $u _ { \boldsymbol { k } , 0 }$ will decrease but not $\boldsymbol { u } _ { k , 1 }$ . Because of the substitution between high-type and low-type clients, the net effect of such a q<sub>\_</sub> on the equilibrium $m _ { _ t } ^ { * }$ and $q _ { s , t } ^ { * } , t = 0 , 1$ , and the total number of clients, $m _ { 0 } ^ { * } + m _ { 1 } ^ { * }$ , is ambiguous. Also, it is obvious that when $q \leq a \nu _ { \mathrm { 0 } } / c _ { \mathrm { \varepsilon } _ { k } }$ , then the mandatory security requirement is immaterial.

18. ${ \bar { \mathrm { I f } } } z \geq n$ , each MSSPs will serve one client, and $q _ { s } ^ { * } = a \nu / c _ { s }$

19. Our analysis treats z as an exogenous parameter, and so in the oligopoly setting the MSSPs may still earn an abnormal profit. Realistically, as long as the MSSPs could make a positive profit, the market may continue to evolve with new entrants entering to share the profits. Hence, without other “frictions” or entry barriers, the managed security service market may degenerate into a perfectly competitive one, which, as we have mentioned, is generally good for social welfare. However, factors such as proprietary technology, transaction costs between the MSSP and clients, MSSPs’ reputation, and so forth, may prevent clients from freely switching from one MSSP to another and facilitate an oligopoly.

20. We could only draw the implications based on a partial equilibrium analysis. A complete equilibrium analysis is tedious and analytically intractable.

21. Empirically, using an international panel of attack data, Png et al. [43] has found that the number of information security attacks is not affected by domestic enforcements or unemployment rates. This seems to be consistent with limited hacker resources, that is, a binding A<sup>ÿ</sup>. For further evidence, see Gershwin [22].

22. We used the following parameters to generate Figure 9: $n = 1 0 , c _ { s } ^ { \phantom { } } = 1 , c _ { k } ^ { \phantom { } } = 2 , \nu = 1 0$ $A = 0 . 0 5 , e = 0 . 0 5$

23. In the CardSystems’ failure example that we cited in the Introduction, one wonders if the Merrick Bank would have lost its customers’ credit card numbers had it not outsourced the payment processing to CardSystems. Also, the “clustering” of clients in an MSSP network, such as a cloud-based security platform or the use of common security protocols, naturally makes the network a bigger target for hackers.

24. A related issue is privacy audit. There has been a growing concern about consumer privacy on the Internet (see, e.g., [1, 25, 28, 38]). The European Union and some other countries have enforced the use of privacy protection by data collectors. Many trust seal issuers, such as Truste and BBBOnLine, profess to notarize organizations’ data practices. Our research implies that if the government mandates organizations to protect consumer privacy, then auditing the practices of trust seal issuers may not be advisable. However, the governments should ensure that these trust seal issuers assume a liability ex ante in case of data breaches. This is not commonly practiced at the moment.

## References

1. Acquisti, A., and Gross, R. Predicting social security numbers from public data. PNAS, 106, 27 (2009), 10975–10980.

2. Akerlof, G.A. Quality uncertainty and the market mechanism. Quarterly Journal of Economics, 84, 3 (1970), 488–500.

3. Anderson, R., and Moore, T. The economics of information security. Science, 314 (October 27, 2006), 610–613.

4. Armour, J., and Humphrey, W.S. Software product liability. Technical Report no. CMU/ SEI-93-TR-13, Software Engineering Institute, Carnegie Mellon University, Pittsburgh, 1993.

5. August, T., and Tunca, T.I. Network software security and user incentives. Management Science, 52, 11 (2006), 657–670.

6. August, T., and Tunca, T.I. Who should be responsible for software security? A comparative analysis of liability policies in network environments. Management Science, 57, 5 (2011), 934–959.

7. Bandyopadhyay, T.; Mookerjee V.; and Rao, R.C. Why IT managers don’t go for cyberinsurance products. Communications of the ACM, 52, 11 (2009), 68–73.

8. Barthelemy, J. The hidden costs of IT outsourcing. Sloan Management Review, 42, 3 (2001), 60–69.

9. Bohme, R., and Schwartz, G. Modeling cyber-insurance: Towards a unifying framework. Paper presented at the Ninth Workshop on the Economics of Information Security (WEIS 2010), Harvard University, Cambridge, 2010 (available at http://weis2010.econinfosec.org/papers/ session5/weis2010\_boehme.pdf).

10. Burson, S. Outsourcing information security. CIO.com, January 19, 2010 (available at www .cio.com/article/518513/Outsourcing\_Information\_Security/).

11. Cavusoglu, H.; Raghunathan, S.; and Yue, W.T. Decision-theoretic and game-theoretic approaches to IT security investment. Journal of Management Information Systems, 25, 2 (Fall 2008), 281–304.

12. Cezar, A.; Cavusoglu, H.; and Raghunathan, S. Competition, speculative risks, and IT security outsourcing. In T. Moore, D. Pym, and C. Ioannidis (eds.), Economics of Information Security and Privacy. New York: Springer, 2010, pp. 301–320.

13. Cezar, A.; Cavusoglu, H.; and Raghunathan, S. Outsourcing information security: Contracting issues and security implications. Paper presented at the Ninth Workshop on the Economics of Information Security (WEIS 2010), Harvard University, Cambridge, 2010 (available at http:// weis2010.econinfosec.org/papers/session1/weis2010\_cezar.pdf).

14. Charney, S. Collective defense: Applying public health models to the Internet. Microsoft, Redmond, WA, 2010.

15. Cremonini, M., and Nizovtsev, D. Risks and benefits of signaling information system characteristics to strategic attackers. Journal of Management Information Systems, 26, 3 (Winter 2009–10), 241–274.

16. Dey, D.; Fan, M.; and Zhang, C. Design and analysis of contracts for software outsourcing. Information Systems Research, 21, 1 (2010), 93–114.

17. Ding, W., and Yurcik, W. Outsourcing Internet security: The effect of transaction costs on managed service providers. Paper presented at the International Conference on Telecommunication Systems—Modeling and Analysis, Dallas, TX, November 17–20, 2005.

18. Ding, W.; Yurcik, W.; and Yin, X. Outsourcing Internet security: Economic analysis of incentives for managed security service providers. In X. Deng and Y. Y e (eds.), Internet and Network Economics. Lecture Notes in Computer Science, vol. 3828. Berlin: Springer, 2005, pp. 947–958.

19. Dulleck, U., and Kerschbamer, R. On doctors, mechanics, and computer specialists: The economics of credence goods. Journal of Economic Literature, 44, 1 (2006), 5–42.

20. Emons, W. Credence goods and fraudulent experts. RAND Journal of Economics, 28, 1 (1997), 107–119.

21. Gal-Or, E., and Ghose, A. The economic incentives for sharing security information. Information Systems Research, 16, 2 (2005), 186–208.

22. Gershwin, L.K. Cyber threat trends and U.S. network security. Central Intelligence Agency, Washington, DC, June 21, 2001 (available at www.cia.gov/news-information/speeches-testimony/ 2001/gershwin\_speech\_06222001.html).

23. Ghose, A., and Rajan, U. The economic impact of regulatory information disclosure on information security investments, competition, and social welfare. Paper presented at the Fifth Workshop on Economics of Information Security (WEIS 2006), Cambridge University, Cambridge, 2006 (available at http://weis2006.econinfosec.org/docs/37.pdf).

24. Gordon, L.A., and Loeb, M.P. The economics of information security investment. ACM Transactions on Information and System Security, 5, 4 (2002), 438–457.

25. Hann, I.H.; Hui, K.L.; Lee, T.S.Y.; and Png, I.P.L. Overcoming online information privacy concerns: An information processing theory approach. Journal of Management Information Systems, 42, 2 (Fall 2007), 13–42.

26. Hausken, K. Strategic defense and attack for series and parallel reliability systems. European Journal of Operational Research, 186 (2008), 856–881.

27. Herath, H.S.B., and Herath, T.C. Investments in information security: A real options perspective with Bayesian postaudit. Journal of Management Information Systems, 25, 3 (Winter 2008–9), 337–375.

28. Hui, K.L.; Teo, H.H.; and Lee, T.S.Y. The value of privacy assurance: An exploratory field experiment. MIS Quarterly, 31, 1 (2007), 19–33.

29. Information security breaches survey 2010. Technical Report, PriceWaterhouseCoopers, London, 2010.

30. IT outsourcing statistics 2010/2011. Computer Economics, Irvine, CA, October 2010.

31. Kim, B.C.; Chen, P.-Y.; and Mukhopadhyay, T. The effect of liability and patch release on software security: The monopoly case. Production and Operations Management, 20, 4 (2011), 603–617.

32. Kumar, R.L.; Park, S.; and Subramaniam, C. Understanding the value of countermeasure portfolios in information systems security. Journal of Management Information Systems, 25, 2 (Fall 2008), 241–279.

33. Kunreuther, H., and Heal, G. Interdependent security. Journal of Risk and Uncertainty, 26, 2–3 (2003), 231–249.

34. Lee, C.H.; Geng, X.; and Raghunathan, S. Security standardization in the presence of unverifiable control. Paper presented at the Tenth Workshop on Economics of Information Security (WEIS 2011), George Mason University, Washington, DC, 2011 (available at http:// weis2011.econinfosec.org/papers/Security%20Standardization%20in%20the%20Presence %20of%20Unverifiable%20Co.pdf).

35. Liu, P.; Zang, W.; and Yu, M. Incentive-based modeling and inference of attacker intent, objectives, and strategies. ACM Transactions on Information and System Security, 8, 1 (2005), 1–41.

36. Losing ground: 2009 TMT global security survey. Deloitte, Rotterdam, 2009 (available at www.deloitte.com/assets/Dcom-Global/Local%20Assets/Documents/dtt\_TMT-Security-Survey09-full.pdf).

37. MacArthur, K. McDonald’s says hacker broke into customer database; FBI investigating. Crain’s Chicago Business, December 13, 2010 (available at www.chicagobusiness.com/ article/20101213/NEWS07/101219975/).

38. Mai, B.; Menon, N.M.; and Sarkar, S. No free lunch: Price premium for privacy sealbearing vendors. Journal of Management Information Systems, 27, 2 (Fall 2010), 189–212.

39. Moeller, Robert. IT Audit, Control and Security. Hoboken, NJ: John Wiley & Sons, 2010.

40. Outpacing change: Ernst & Young’s 12th annual global information security survey. Ernst & Young, New York, 2009.

41. Png, I.P.L., and Lehman, D. Managerial Economics. New York: Blackwell, 2002.

42. Png, I.P.L., and Wang, Q.-H. Information security: Facilitating user precautions vis-à- vis enforcement against attackers. Journal of Management Information Systems, 26, 2 (Fall 2009), 97–121.

43. Png, I.P.L.; Wang, C.-Y.; and Wang, Q.-H. The deterrent and displacement effects of information security enforcement: International evidence. Journal of Management Information Systems, 25, 2 (Fall 2008), 125–144.

44. Rice, M.; Butts, J.; Miller, R.; and Shenoi, S. Applying public health strategy to the protection of cyberspace. International Journal of Critical Infrastructure Protection, 3, 3–4 (2010), 118–127.

45. Richards, K., and Davis, B. Computer security incidents against Australian businesses: Predictors of victimisation. Australian Institute of Criminology, Trends & Issues in Crime and Criminal Justice, no. 399, September 2010 (available at www.aic.gov.au/documents/6/9/ F/%7B69FC108B-D437-47E0-9C17-93B5DEFC8D96%7Dtandi399.pdf).

46. Rothschild, M., and Stiglitz, J.E. Equilibrium in competitive insurance markets: An essay on the economics of imperfect information. Review of Economic Studies, 44, 3 (1977), 407–430.

47. Ryan, D.J. Two views on security software liability: Let the legal system decide. IEEE Security & Privacy, 1, 1 (2009), 70–72.

48. Sawyer, J. Tech insights: When to pull the outsourcing trigger. Dark Reading, April 23, 2010 (available at www.darkreading.com/security-services/167801101/security/securityman agement/224600304/index.html).

49. Schneier, B. The case of outsourcing security. Computer, 35, 4 (2002), 20–26.

2010 (available at www.informationweek.com/security/management/more-firms-outsourcingsecurity-to-mssps/225700537/).

51. Spence, M. Consumer misperceptions, product failure and producer liability. Review of Economic Studies, 44, 3 (1977), 561–572.

52. Stiglitz, J.E. Monopoly, non-linear pricing and imperfect information: The insurance market. Review of Economic Studies, 44, 3 (1977), 407–430.

53. Use of IT security outsourcing low but rising as threats grow. Computer Economics, Irvine, CA, June 2009 (available at www.computereconomics.com/custom. cfm?name=postPaymentGateway.cfm&id=1459/).

54. Varian, H.R. System reliability and free riding. In L.J. Camp and S. Lewis (eds.), Economics of Information Security. Novell, MA: Kluwer Academic, 2004, pp. 1–15.

55. Vijayan, J. Outsourcers rush to meet security demand. IT World, March 8, 2001 (available at www.itworld.com/CWSTO57980/).

56. Whitman, M.E., and Mattord, H.J. Principles of Information Security. Boston: Course Technology, Cengage Learning, 2009.

57. Wolchok, S.; Yao, R.; and Halderman, J.A. Analysis of the Green Dam Censorware System. Working paper, Computer Science and Engineering Division, University of Michigan, Ann Arbor, 2009.

58. Wolinsky, A. Competition in markets for credence goods. Journal of Institutional and Theoretical Economics, 151, 1 (1995), 117–131.

59. Yue, W.T.; Cakanyildirim, M.; Ryu, Y.U.; and Liu, D. Network externalities, layered protection and IT security risk management. Decision Support Systems, 44, 1 (2007), 1–16.

60. Zetter, K. In legal first, data-breach suit targets auditor. WIRED, June 2, 2009 (available at www.wired.com/threatlevel/2009/06/auditor\_sued/).

## Appendix

Proof of Lemma 1

Th e Lagrangian funct ion is

$$
\begin{array}{c} \Lambda = p - a \beta v (1 - q _ {s}) - \frac {1}{2} c _ {s} q _ {s} ^ {2} \\ - \lambda \left[ p - a v q _ {s} - a \beta v (1 - q _ {s}) + \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}} \right]. \end{array}
$$

The constraints are:

$$
p \leq a v q _ {s} + a \beta v (1 - q _ {s}) - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}}\tag{A1}
$$

$$
\lambda \geq 0.\tag{A2}
$$

Differentiating with respect to $p , q _ { s } ,$ and $\beta ,$ , we have

$$
\frac {\partial \Lambda}{\partial p} = 1 - \lambda\tag{A3}
$$

$$
\frac {\partial \Lambda}{\partial q _ {s}} = a \beta v - c _ {s} q _ {s} + \lambda a v - \lambda a \beta v\tag{A4}
$$

$$
\frac {\partial \Lambda}{\partial \beta} = - a v (1 - q _ {s}) + \lambda a v (1 - q _ {s}).\tag{A5}
$$

Solving the Equations (A3), (A4), and (A5), we have $\lambda = 1 , q _ { s } ^ { * } = a \nu / c _ { s }$ , and $p ^ { * } - a \ B ^ { * } \nu ( 1 - ( a \nu / c _ { s } ) ) = ( ( a \nu ) ^ { 2 } / c _ { s } ) - ( 1 / 2 ) ( ( a \nu ) ^ { 2 } / c _ { k } )$ . Substitute them into Equations (2) and (3), the client’s utility and MSSP’s profit follow.

## Proof of Proposition 1

Proposition 1a is obvious because $\underline { { q } }$ is not binding. For Proposition 1b, the Lagrangian function is now

$$
\begin{array}{c} \Lambda = p - a \beta v (1 - q _ {s}) - \frac {1}{2} c _ {s} q _ {s} ^ {2} \\ - \lambda \bigg [ p - a v (q _ {s} - \underline {{q}}) - a \beta v (1 - q _ {s}) + \frac {1}{2} c _ {k} \underline {{q}} ^ {2} \bigg ]. \end{array}
$$

The constraints are

$$
p \leq a v (q _ {s} - \underline {{q}}) + a \beta v (1 - q _ {s}) - \frac {1}{2} c _ {k} \underline {{q}} ^ {2}\tag{A6}
$$

$$
\lambda \geq 0.\tag{A7}
$$

Differentiating with respect to $p , q _ { s }$ , and $\beta ,$ , the first-order conditions are identical to Equations (A3), (A4), and (A5). Solving the equations, we have $\lambda = 1 , \breve { q } _ { s } ^ { * } = a \nu / c _ { s }$ , and $\check { p } ^ { * } - a \check { \beta } ^ { * } \nu ( 1 - ( a \nu / c _ { s } ) ) = ( ( a \nu ) ^ { 2 } / c _ { s } ) - a \nu \underline { { q } } + ( 1 / 2 ) c _ { k } \underline { { q } } ^ { 2 }$ . Substitute them into Equations (2) and (3), the client’s utility and $\mathrm { M S S P ^ { \prime } s }$ profit follow.

Finally, because the MSSP always chooses $\breve { q } _ { _ s } ^ { * } = a \nu / c _ { _ s }$ , his effort will match/exceed $\underline { { q } }$ whenever $\underline { { q } } \le a \nu / c _ { _ s }$ . The MSSP will underprovide his service quality relative to $\underline { { q } }$ when $\underline { { q } } > a \nu / c _ { s }$ •

## Proof of Lemma 2

The Lagrangian function is

$$
\begin{array}{c} \Lambda = \sum_ {j = 1} ^ {m} \left(p _ {j} - L _ {j} \beta_ {j} v - \frac {1}{2} c _ {s} q _ {s, j} ^ {2}\right) \\ - \sum_ {j = 1} ^ {m} \lambda_ {j} \left[ p _ {j} - (a - L _ {j}) v - L _ {j} \beta_ {j} v + \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}} \right]. \end{array}
$$

The constraints are

$$
p _ {j} \leq (a - L _ {j}) v + L _ {j} \beta_ {j} v - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}}, \quad j = 1, \dots , m,\tag{A8}
$$

$$
\lambda_ {j} \geq 0, \quad j = 1,..., m.\tag{A9}
$$

For simplicity, we treat m as if it were continuous (alternatively, we could redefine m to be a fraction of n, which must be continuous). Differentiating L with respect to $p _ { j } , q _ { s , j } ;$ , and $\beta _ { j } , j = 1 , . . . , m \colon$

$$
\frac {\partial \Lambda}{\partial p _ {j}} = 1 - \lambda_ {j}\tag{A10}
$$

$$
\frac {\partial \Lambda}{\partial q _ {s , j}} = a [ 1 + e (m - 1) ] (\beta_ {j} v + \lambda_ {j} v - \lambda_ {j} \beta_ {j} v) - c _ {s} q _ {s, j}\tag{A11}
$$

$$
\frac {\partial \Lambda}{\partial \beta_ {j}} = - L _ {j} v + \lambda_ {j} L _ {j} v\tag{A12}
$$

$$
\frac {\partial \Lambda}{\partial m} = \frac {\partial}{\partial m} \sum_ {j = 1} ^ {m} \left[ p _ {j} (1 - \lambda_ {j}) - \lambda_ {j} \beta_ {j} v (1 - \lambda_ {j}) \right]
$$

$$
+ \frac {\partial}{\partial m} \sum_ {j = 1} ^ {m} \left[ \lambda_ {j} (a - L _ {j}) v - \frac {1}{2} c _ {s} q _ {s, j} ^ {2} + \frac {1}{2} \frac {\lambda_ {j} (a v) ^ {2}}{c _ {k}} \right].\tag{A13}
$$

By Equations (A10) and (A12), $\partial \Lambda / \partial p _ { _ i } = 0$ and $\partial \Lambda / \partial \beta _ { _ i } = 0$ imply $\lambda _ { _ i } = 1$ , and so by Equation (A11), the MSSP will select the same quality, $q _ { s , j } ^ { * } = q _ { s }$ for all the clients. Equation (A13) then simplifies to

$$
\frac {\partial \Lambda}{\partial m} = e a v + a v (1 - e) q _ {s} - 2 e a v m (1 - q _ {s}) - \frac {1}{2} c _ {s} (q _ {s}) ^ {2} - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}}.\tag{A14}
$$

Solving all the first-order conditions, we have

$$
m ^ {*} = \frac {1}{2} + \frac {a v q _ {s} ^ {*} - \frac {1}{2} c _ {s} \left(q _ {s} ^ {*}\right) ^ {2} - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}}}{2 e a v (1 - q _ {s} ^ {*})},
$$

$$
q _ {s, j} ^ {*} = q _ {s} ^ {*} = \frac {T a v}{c _ {s}},
$$

and

$$
p _ {j} ^ {*} - T a \beta_ {j} ^ {*} v \left(1 - \frac {T a v}{c _ {s}}\right) = \frac {(T a v) ^ {2}}{c _ {s}} - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {s}} - a v (T - 1),
$$

where $T \equiv 1 + e ( m ^ { * } - 1 ) > 1$ . It is straightforward to show that if e is sufficiently small, the second term in $m ^ { * }$ will be positive, and $q _ { s } ^ { * } < 1$ . Further, with a sufficiently large number of clients, ${ n , m } ^ { * }$ will be bounded between 1 and n. These conditions guarantee that an interior solution exists.

Suppose that the solution characterized by $m ^ { * }$ and $q _ { s } ^ { * }$ is unique. Substituting these results into Equations (9) and (10), we can obtain the clients’ utility in Equation (4) and the MSSP’s profit in Equation (13). Note that because $m ^ { * }$ maximizes $\pi ,$ and, by Equation (13), $\pi = ( 1 / 2 ) ( a \nu ) ^ { 2 } ( ( 1 / c _ { \circ } ) - ( 1 / c _ { \iota } ) ) > 0 \mathrm { ~ i f ~ } m ^ { \circ } = 1$ , the equilibrium $\pi ^ { * } \geq ( 1 / 2 ) ( a \nu ) ^ { 2 } ( ( 1 / c _ { . } ) - ( 1 / c _ { . } ) ) > 0 .$

It remains to be proved that the solution characterized by $m ^ { * }$ and $q _ { s } ^ { * }$ is unique. First, observe that $d q _ { s } ^ { * } / d m ^ { * } = e a \nu / c _ { s }$ , which is a positive constant. So, $q _ { s } ^ { * }$ increases linearly in $m ^ { * }$ . Similarly,

$$
\frac {d m ^ {*}}{d q _ {s} ^ {*}} = \frac {a v - c _ {s} q _ {s} ^ {*} + \frac {1}{2} c _ {s} \left(q _ {s} ^ {*}\right) ^ {2} - \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}}}{2 e a v \left(1 - q _ {s} ^ {*}\right) ^ {2}}.
$$

When $q _ { s } ^ { * } = 0 .$ , dm $^ { * } / d q _ { s } ^ { * } > 0$ . As $q _ { s } ^ { * }$ increases, the numerator in dm $^ { * } / d q _ { s } ^ { * }$ decreases, but, up to $q _ { s } ^ { * } = T a { \nu } / { c _ { s } }$ , dm $^ { * } / d q _ { s } ^ { * } > 0$ . Next, it is straightforward to show that the sign of $d ^ { 2 } m ^ { * } / d ( q _ { s } ^ { * } ) ^ { 2 }$ has the sign of $2 a \nu - c _ { \scriptscriptstyle s } - ( 1 / 2 ) ( ( a \nu ) ^ { 2 } / c _ { \scriptscriptstyle k } )$ , which, given v, $c _ { \scriptscriptstyle k } , c _ { \scriptscriptstyle S } ,$ and $^ { a , }$ is always a constant. Hence, $m ^ { * }$ is either strictly convex or strictly concave in $q _ { s } ^ { * }$ . Since $q _ { s } ^ { * }$ is linear and increasing in $m ^ { * }$ , and $m ^ { * }$ is either strictly convex or strictly concave in $q _ { s } ^ { * }$ , other than the corner solution whereby $m ^ { * } = 1$ and $q _ { s } ^ { * } = a \nu / c _ { s }$ (i.e., the outcome in the single-client case), the $m ^ { * } ( q _ { s } ^ { * } )$ curve and the $q _ { s } ^ { * } ( m ^ { * } )$ curve could intersect at most once, which implies that given selected $\nu , c _ { _ { k } } , c _ { _ { s } } ^ { \mathrm { ~ } }$ , and $^ { a , }$ the solution characterized by $m ^ { * }$ and $q _ { s } ^ { * }$ must exist and is unique.

## Proof of Proposition 2

The Lagrangian function is

$$
\begin{array}{c} \breve {\Lambda} = \sum_ {j = 1} ^ {m} \left(p _ {j} - L _ {j} \beta_ {j} v - \frac {1}{2} c _ {s} q _ {s, j} ^ {2}\right) \\ - \sum_ {j = 1} ^ {m} \lambda_ {j} \left[ p _ {j} - (a - L _ {j}) v - L _ {j} \beta_ {j} v + a v \underline {{q}} - \frac {1}{2} c _ {k} \underline {{q}} ^ {2} \right]. \end{array}
$$

The first-order conditions with respect to $p _ { j } , q _ { s , j } .$ , and $\beta _ { { } _ { j } }$ are identical to Equations (A10), (A11), and (A12), and $\mathbf { S O } ,$ again, the MSSP will select the same service quality, $\breve { q } _ { s , j } ^ { * } = \breve { q } _ { s } ^ { * }$ for all clients who use his service. The first-order condition with respect to m is then

$$
\frac {\partial \check {\Lambda}}{\partial m} = e a v + a v (1 - e) q _ {s} - 2 e a v m (1 - q _ {s}) - \frac {1}{2} c _ {s} (q _ {s}) ^ {2} - a v \underline {{{q}}} + \frac {1}{2} c _ {k} \underline {{{q}}} ^ {2}.\tag{A15}
$$

Solving all the first-order conditions, we have

$$
\bar {m} ^ {*} = \frac {1}{2} + \frac {a v \bar {q} _ {s} ^ {*} - \frac {1}{2} c _ {s} \left(\bar {q} _ {s} ^ {*}\right) ^ {2} - a v \underline {{q}} + \frac {1}{2} c _ {k} \underline {{q}} ^ {2}}{2 e a v \left(1 - \bar {q} _ {s} ^ {*}\right)},
$$

$$
\breve {q} _ {s, j} ^ {*} = \breve {q} _ {s} ^ {*} = \frac {\breve {T a v}}{c _ {s}},
$$

and

$$
\check {p} _ {j} ^ {*} - \check {T} a \check {\beta} _ {j} ^ {*} v \left(1 - \frac {\check {T} a v}{c _ {s}}\right) = \frac {\left(\check {T} a v\right) ^ {2}}{c _ {s}} - a v (\check {T} - 1) - a v \underline {{{q}}} + \frac {1}{2} c _ {k} \underline {{{q}}} ^ {2},
$$

where $\breve { T } \equiv 1 + e ( \breve { m } ^ { * } - 1 ) > 1$ . Here again, if $e$ is sufficiently small and n is sufficiently large, $\breve { q } _ { s } ^ { * } < 1$ and $\breve { m } ^ { * }$ is bounded between 1 and n, which guarantee the existence of an interior solution. The proof of uniqueness then follows a similar procedure as outlined in Lemma 2.

Substitute the above results into Equations (9) and (10), we can obtain the clients utility in Equation (7) and the MSSP’s profit in Equation (16). Because $\breve { m } ^ { * }$ maximizes $\breve { \pi } ,$ and

$$
\bar {\pi} = \frac {1}{2} (a v) ^ {2} \left(\frac {1}{c _ {s}} - \frac {1}{c _ {k}}\right) + \frac {1}{2} c _ {k} \left(\underline {{q}} - \frac {a v}{c _ {k}}\right) ^ {2} > 0
$$

if $\breve { m } ^ { * } = 1$ , the equilibrium $\breve { \pi } ^ { * } > 0$

Finally, because the MSSP always chooses $\breve { q } _ { s } ^ { * } = \breve { T } a \nu / c _ { s }$ , his effort will match/exceed $\underline { { q } }$ whenever $\underline { { q } } \le \breve { T } a \nu / c _ { s }$ . The MSSP will underprovide service quality relative to q<sub>\_</sub> when $\underline { { q } } > \breve { T } a \nu / c _ { s }$

## Proof of Proposition 3

Differentiating Equations (A14) and (A15) with respect to m, $\partial ^ { 2 } \Lambda / \partial m ^ { 2 } = \partial ^ { 2 } \breve { \Lambda } / \partial m ^ { 2 } =$ $- 2 e a \nu ( 1 - q _ { \mathrm { s } } ) < 0$ , which implies that L and $\breve { \Lambda }$ are strictly concave in $m .$ Now, by Equations (A14) and (A15),

$$
\frac {\partial \check {\Lambda}}{\partial m} - \frac {\partial \Lambda}{\partial m} = \frac {1}{2} c _ {k} \left(\underline {{q}} - \frac {a v}{c _ {k}}\right) ^ {2} > 0,\tag{A16}
$$

and so, given any pairs of m and $q _ { s } , \partial \check { \Lambda } / \partial m > \partial \Lambda / \Delta m$ . Equation (A16) implies that at the $m ^ { * }$ and $q _ { s } ^ { * }$ which maximizes L we must have

$$
\left. \frac {\partial \breve {\Lambda}}{\partial m} \right| _ {m = m ^ {*}, q _ {s} = q _ {s} ^ {*}} > \left. \frac {\partial \Lambda}{\partial m} \right| _ {m = m ^ {*}, q _ {s} = q _ {s} ^ {*}} = 0.
$$

Since $\breve { \Lambda }$ is strictly concave in $m$ ,

$$
\left. \frac {\partial \check {\Lambda}}{\partial m} \right| _ {m = m ^ {*}, q _ {s} = q _ {s} ^ {*}} > 0
$$

necessarily means that the equilibrium $\breve { m } ^ { * } > m ^ { * }$ . This also implies that the optimal security quality,

$$
\check {q} _ {s} ^ {*} = \frac {a v}{c _ {s}} \left[ 1 + e (\check {m} ^ {*} - 1) \right] > q _ {s} ^ {*} = \frac {a v}{c _ {s}} \left[ 1 + e (m ^ {*} - 1) \right].
$$

Finally, by Proposition 2, the MSSP will shirk if and only if $\underline { { q } } > \breve { T } a \nu / c _ { s }$ . If m˘ <sup>\*</sup> increases, T<sup>˘</sup> also increases, and so it is less likely for $\underline { { q } } > \breve { T } a \nu / c _ { s }$ , that is, the MSSP will be less likely to shirk.

## Proof of Proposition 4

To prove this proposition, it is instrumental to compute the first-best social welfare. Let there be $m \leq n$ outsourcing clients. Substituting from Equations (1), (9), and (10), first-best social welfare,

$$
W = (n - m) \left[ (1 - a) v + \frac {1}{2} \frac {(a v) ^ {2}}{c _ {k}} \right] + \sum_ {j = 1} ^ {m} \left[ (1 - L _ {j}) v - \frac {1}{2} c _ {s} q _ {s, j} ^ {2} \right].\tag{A17}
$$

The first term in Equation (A17) is the sum of utility that the “excluded” clients obtain by developing in-house protection (by the analysis in the basic model, the optimal decision of the clients who are not outsourcing is to select $q _ { k } ^ { * } = a \nu / c _ { k }$ , which gives the maximum utility $u _ { k } ^ { \ast } = ( 1 - a ) \nu + ( 1 / 2 ) ( ( a \nu ) ^ { 2 } / c _ { k } ) )$ . The second term in Equation (A17) is the net utility generated for the m outsourcing clients, which is simply the sum of Equations (9) and (10) (when computing social welfare, the transfer payment between the clients and the MSSP is irrelevant).

Differentiating Equation (A17) with respect to $q _ { s , j }$ and $m _ { : }$ , and suppose that the MSSP chooses the same quality level for all clients, it is straightforward to show that the first-order conditions are identical to Equations (A11) and (A14). This implies that the optimal m and $q _ { s }$ that maximize social welfare are identical to Equations (11) and (12), that is, they are also the solution for the case with no mandatory security requirement.

Accordingly, the solution presented in Lemma 2 provides the first-best social welfare. By definition, any deviation of m or $q _ { s , j }$ away from this solution, including the $\breve { m } ^ { * }$ and $\breve { q } _ { s } ^ { * }$ in Proposition 2, that is, Equations (14) and (15), should reduce social welfare.

Next, by Lemma 1 and Proposition 1, with or without ${ \underline { { q } } } ,$ the social welfare from serving each client is always $( 1 - a ) \nu + ( 1 / 2 ) ( ( a \nu ) ^ { 2 } / c _ { \mathrm { { s } } } )$ . Hence, the social welfare from serving all n clients, $W _ { _ { - e } } = n [ ( 1 - a ) \nu + ( 1 / 2 ) ( ( a \nu ) ^ { 2 } / c _ { _ s } ) ]$ . In other words, without system interdependency, the social welfare change due to q<sub>\_</sub>, $\Delta W _ { - e } = 0$

With system interdependency, denote the social welfare with $\underline { { q } } > a \nu / c _ { _ k }$ as W<sup>˘</sup>. Then, by Equation (A17) and the discussion thereafter, we must have $W > { \breve { W } } ,$ and so $W - \breve { W } > \Delta W _ { - { \rho } } = 0$

## Proof of Proposition 5

By Proposition 2, when $\underline { { q } } \le \breve { T } a \nu / c _ { s }$ , it is in the best interest of the MSSP to choose $\breve { q } _ { s } ^ { * } = \breve { T } a \nu / c _ { s }$ , and so imposing verifiability will not affect the equilibrium outcome.

Next, for any $\underline { { q } } > \breve { T } a \nu / c _ { s } ,$ , the solution in Equations (14) and (15) yields the maximum profit for the MSSP, and so any deviation in $\breve { q } _ { s } ^ { * }$ or m˘ <sup>\*</sup> will necessarily reduce the MSSP’s profit. Because all n clients will obtain utility $\check { u } _ { \mathnormal { s } } ^ { \ast } = \check { u } _ { \mathnormal { k } } ^ { \ast } = ( 1 - a ) \nu + a \nu \underline { { q } } - ( 1 / 2 ) c _ { \mathnormal { k } } \underline { { q } } ^ { 2 }$ with or without verifiability, a decrease in the MSSP’s profit directly implies a decrease in social welfare. Finally, when $\underline { { q } } > \breve { T } a \nu / c _ { s }$ , with verifiability, the MSSP’s clients are better protected because they now get q<sub>\_</sub> from the MSSP instead of $\breve { q } _ { s } ^ { * } = \breve { T } a \nu / c _ { s }$

## Proof of Results in Extension: Heterogeneous Clients

The Lagrangian function is

$$
\begin{array}{c} \Lambda = \sum_ {t = 0, 1} \sum_ {j = 1} ^ {m _ {t}} \left(p _ {t, j} - L _ {t, j} \beta_ {t, j} v _ {t} - \frac {1}{2} c _ {s} q _ {s, t, j} ^ {2}\right) \\ - \sum_ {t = 0, 1} \sum_ {j = 1} ^ {m _ {t}} \lambda_ {t, j} \left[ p _ {t, j} - (1 - L _ {t, j}) v _ {t} - L _ {t, j} \beta_ {t, j} v _ {t} + u _ {k, t} \right]. \end{array}
$$

The constraints are

$$
p _ {t, j} \leq \left(1 - L _ {t, j}\right) v _ {t} + L _ {t, j} \beta_ {t, j} v _ {t} - u _ {k, t}, \quad t = 0, 1, j = 1,..., m\tag{A18}
$$

$$
\lambda_ {t, j} \geq 0, t = 0, 1, \quad j = 1,..., m.\tag{A19}
$$

Differentiating L with respect to $p _ { t , j } , q _ { s , t , j } ,$ and $\beta _ { { t } , { j } } , t = 0 , 1 , j = 1 , . . . , m .$

$$
\frac {\partial \Lambda}{\partial p _ {t , j}} = 1 - \lambda_ {t, j}\tag{A20}
$$

$$
\frac {\partial \Lambda}{\partial q _ {s , t , j}} = a \Big [ 1 + e (m _ {t} - 1) \Big ] (\beta_ {t, j} v _ {t} + \lambda_ {t, j} v _ {t} - \lambda_ {t, j} \beta_ {t, j} v _ {t})
$$

$$
+ e a m _ {1 - t} \left(\boldsymbol {\beta} _ {1 - t, j} v _ {1 - t} + \lambda_ {1 - t, j} v _ {1 - t} - \lambda_ {1 - t, j} \boldsymbol {\beta} _ {1 - t, j} v _ {1 - t}\right) - c _ {s} q _ {s, t, j}\tag{A21}
$$

$$
\frac {\partial \Lambda}{\partial \beta_ {t , j}} = - L _ {t, j} v _ {t} + \lambda_ {t, j} L _ {t, j} v _ {t}.\tag{A22}
$$

By Equations (A20) and (A22), $\partial \Lambda / \partial p _ { { } _ { t , j } } = 0$ and $\partial \Lambda / \partial \beta _ { t , i } = 0$ imply $\lambda _ { \scriptscriptstyle t , j } = 1$ , and so by Equation (A21), the MSSP will select the same quality, $q _ { s , t , j } ^ { * } = q _ { s , t }$ , for each type of client. Then,

$$
\begin{array}{c} \frac {\partial \Lambda}{\partial m _ {t}} = (1 - a) v _ {t} + a v _ {t} q _ {s, t} + e a v _ {t} (1 - q _ {s, t}) - 2 e a v _ {t} m _ {t} (1 - q _ {s, t}) \\ - e a m _ {1 - t} (1 - q _ {s, 1 - t}) v _ {t} - u _ {k, t} - \frac {1}{2} c _ {s} q _ {s, t} ^ {2} \\ - e a m _ {1 - t} (1 - q _ {s, t}) v _ {1 - t}. \end{array}\tag{A23}
$$

Substituting $\lambda _ { { } _ { t , j } } = 1$ and rearranging Equations (A21) and (A23):

$$
q _ {s, t} ^ {*} = \frac {a \left[ 1 + e \left(m _ {t} ^ {*} - 1\right) \right] v _ {t} + e a m _ {1 - t} ^ {*} v _ {1 - t}}{c _ {s}},
$$

$$
m _ {t} ^ {*} = \frac {1}{2} + \frac {(1 - a) v _ {t} + a v _ {t} q _ {s , t} ^ {*} - u _ {k , t} - \frac {1}{2} c _ {s} (q _ {s , t} ^ {*}) ^ {2}}{2 e a v _ {t} (1 - q _ {s , t} ^ {*})} - \frac {m _ {1 - t} ^ {*}}{2} \left(\frac {v _ {1 - t}}{v _ {t}} + \frac {1 - q _ {s , 1 - t} ^ {*}}{1 - q _ {s , t} ^ {*}}\right).
$$

Because $( d / d u _ { k , t } ) ( \partial \Lambda / \partial m _ { t } ) < 0 , \mathrm { i f } \underline { { q } } > a \nu _ { 1 } / c _ { k } > a \nu _ { 0 } / c _ { k }$ , then $u _ { k , i }$ will decrease and $\partial \Lambda / \partial m _ { _ t }$ will increase, which implies that the equilibrium $m _ { { t } } ^ { * } , t = 0 , 1$ , will increase. In other words, the MSSP will tend to serve more clients of both types. By Equation (A21) and so Equation (17), the equilibrium $q _ { s , 0 } ^ { * }$ and $q _ { s , 1 } ^ { * }$ will increase too.

If, however, $a \nu _ { \mathrm { 0 } } / c _ { k } < \underline { { q } } \le a \nu _ { \mathrm { 1 } } / c _ { k }$ , then $u _ { k , 0 }$ will decrease but not $\boldsymbol { u } _ { k , 1 }$ . The net effect of such a $\underline { { q } }$ on $\boldsymbol { m } _ { { } _ { t } } ^ { * }$ depends on the relative magnitude of $\nu _ { _ t } ^ { * } , t = 0 , 1$ , and so is ambiguous. Similarly, by Equation (17), $q _ { s , t } ^ { * }$ is a function of $\boldsymbol { m } _ { t } ^ { * }$ , and thus the impact of $\underline { { q } }$ on $q _ { s , t } ^ { * }$ is ambiguous, too.

## Proof of Results in Extension: Competition

The proofs of the first two cases, perfection competition and oligopoly, are already sketched in the text. We argue that for the last case, when $z { \breve { m } } ^ { * } > n$ but the market doe not exhibit perfect competition, no pure strategy equilibrium exists. We sketch the idea below.

Suppose that there exists a pure strategy equilibrium in which the MSSPs choose some fixed prices and service quality. Because $z { \breve { m } } ^ { * } > n .$ , some MSSPs will have “excess capacity” relative to $\breve { m } ^ { * }$ . Then, a marginal reduction in price or a marginal increase in liability would bring a first-order gain in number of clients but a second-order loss in revenue, and so would improve the $\mathbf { M S S P } \mathrm { ^ { \circ } s }$ profit. Similarly, a marginal increase in service quality would bring a first-order gain in number of clients but only a secondorder loss in service cost. $\mathrm { S o } .$ the MSSPs will have incentives to bid down the prices or bid up the liability and service quality. However, they will not want to bid the prices, liabilities, and service quality all the way to the marginal cost because they could make a profit in some middle ranges. Hence, no pure strategy equilibrium exists when $z { \breve { m } } ^ { * } > n ,$ , but the market does not exhibit perfect competition.

Proof of Results in Extension: Strategic Hacking

(a) By Equations (20) and (22),

$$
\frac {\partial A ^ {*}}{\partial q _ {s}} = \frac {\partial \breve {A} ^ {*}}{\partial q _ {s}} = - \frac {b}{c _ {h}} \frac {m}{n} <   0,
$$

$$
\frac {\partial A ^ {*}}{\partial q _ {k}} = - \frac {b}{c _ {h}} \left(1 - \frac {m}{n}\right) <   0,
$$

and, clearly, $\breve { A } ^ { \ast }$ is independent of $q _ { k } ,$ , and so $\partial \check { A } { } ^ { * } / \partial q _ { _ k } = 0$

(b) By Equations (20) and (22),

$$
\frac {\partial A ^ {*}}{\partial m} = - \frac {b}{c _ {h}} \frac {(q _ {s} - q _ {k})}{n} <   0
$$

because, by Proposition 2 and Lemma 2, $q _ { s } > q _ { k }$ . Further,

$$
\frac {\partial \check {A} ^ {*}}{\partial m} = - \frac {b}{c _ {h}} \frac {q _ {s} - \underline {{q}}}{n} <   0
$$

if and only if $q _ { s } > { \underline { { q } } }$ , which, by Proposition 2, happens when the MSSP is honest. (c)

$$
\frac {\partial}{\partial A} \frac {\partial u _ {k}}{\partial q _ {k}} = \frac {v}{n} > 0
$$

and

$$
\frac {\partial}{\partial A} \frac {\partial \pi}{\partial q _ {s}} = \frac {m v}{n} [ 1 + e (m - 1) ] > 0.
$$

(d) For the clients who are not outsourcing, they always have to choose ${ \underline { { q } } } ,$ and so a marginal change in A would not affect their decisions. For the MSSP’s clients,

$$
\frac {\partial}{\partial A} \frac {\partial \check {\pi}}{\partial q _ {s}} = \frac {m v}{n} [ 1 + e (m - 1) ] > 0.
$$

For $q _ { s } \leq { \underline { { q } } } .$

$$
\frac {\partial}{\partial A} \frac {\partial \breve {\pi}}{\partial m} = \frac {v}{n} \Bigl (- \underline {{q}} + q _ {s} \Bigr) - \frac {e v}{n} \bigl (1 - q _ {s} \bigr) \bigl (2 m - 1 \bigr) <   0.
$$

(e) By Equation (22),

$$
\frac {d \breve {A} ^ {*}}{d q} = - \frac {b}{c _ {h}} \left(1 - \frac {m}{n}\right) <   0.
$$

Proof of Results in Extension: Shirking Clients

The proof follows that of Proposition 6 and so we omit it here.
