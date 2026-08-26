---
otero_id: 6438
otero_key: "MX6QREND"
title: "Mandatory Standards and Organizational Information Security"
authors: "Chul Ho Lee; Xianjun Geng; Srinivasan Raghunathan"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0607"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.130.37.84] On: 02 May 2016, At: 08:29 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/MX6QREND/fulltext/images/b35b3c63e5ca91a6f07e645ad157083b96844b878baab43f7db7acab76f0e35a.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Mandatory Standards and Organizational Information Security

Chul Ho Lee, Xianjun Geng, Srinivasan Raghunathan

## To cite this article:

Chul Ho Lee, Xianjun Geng, Srinivasan Raghunathan (2016) Mandatory Standards and Organizational Information Security. Information Systems Research 27(1):70-86. http://dx.doi.org/10.1287/isre.2015.0607

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/MX6QREND/fulltext/images/7bc0ec7fe571a6b2162bb620d9d4730ce92bef275e4fdf746dff76fa64eab4b5.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Mandatory Standards and Organizational Information Security

Chul Ho Lee

Harbin Institute of Technology, Harbin, Heilongjiang 150001, China, irontigerlee@gmail.com

Xianjun Geng, Srinivasan Raghunathan

Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080 {geng@utdallas.edu, sraghu@utdallas.edu}

andatory security standards that force firms to establish minimum levels of security controls are enforced in intertwined security controls, not all of which can be regulated by standards, but compliance with existing security standards is often used by firms to deflect liability if a security breach occurs. We analyze a stylized setting where a firm has two security controls that are linked in either a serial or a parallel configuration. One control is directly regulated by a security standard, whereas the other one is not. We show that a higher security standard does not necessarily lead to a higher firm security. Furthermore, the conditions under which a higher standard hurts the firm security are sharply different in the two—serial and parallel—configurations. If standard compliance leads to reduced liability for a firm following a breach, such liability reduction in turn weakens the tie between the standard and firm security. Under a setting in which the firm meets the optimal standard set by a policy maker, both firm security and social welfare are higher when the damage to the firm following a breach takes a higher share of the total damage to social welfare, and also when the firm takes a larger share of liability.

Keywords: information security; security regulation; unverifiability

History: Il-Horn Hann, Senior Editor; Kai-Lung Hui, Associate Editor. This paper was received October 17, 2012, and was with the authors 16.5 months for 2 revisions. Published online in Articles in Advance February 15, 2016.

## 1. Introduction

In this networked economy, when an organization’s digital asset or online service is compromised by attacks, damages often go beyond the organizational boundary. For example, in 2009, the information system of a large payment card processor, Heartland Payment Systems (HPS hereafter), was breached, and millions of consumers were affected (Krebs 2009b, Cheney 2010).<sup>1</sup> Security incidents similar to the one at HPS in which the breach of a single firm resulted in large-scale damages to consumers and business ecosystems in general have been occurring on a regular basis; see MacCarthy (2010) for detailed accounts of some high-profile incidents. Increasingly, policy makers in both private and public sectors mandate information security standards upon organizations with the intention not only to protect these organizations but also to protect the value of all stakeholders who entrust their sensitive information to these organizations. Two such prominent policy makers are the PCI Security Standards Council in the private sector, which mandates information security standards—collectively referred to as the Payment Card Industry Data Security Standard (PCI-DSS)—upon all merchants that use major payment cards, and the National Institute of Standards and Technology (NIST), which mandates information security standards on all U.S. governmental agencies.

Yet, are mandatory standards effective in improving organizational information security? Anecdotal evidence in academia and in business practice seems to paint a puzzling picture where tighter standards have not necessarily led to better security. For example, Miller and Tucker (2010) present anecdotal evidence that the mandatory adoption of encryption software has not decreased publicized data loss cases. For another example, since the 2004 implementation of the PCI-DSS, the number of annual publicized security breaches in the business sector in the United States actually increased for three out of four years from 2004 to 2008 (http://www.datalossdb.org).

This paper analytically studies the impact of mandatory standards on overall firm security, and in particular we pay attention to when and how mandatory standards can harm firm security. Our investigation starts with the observation that, in industrial practices, a mandatory standard can influence a firm’s overall security through multiple intertwined mechanisms as listed below. First, a mandatory security standard directly influences firm investment on any security control that is explicitly regulated (hereafter, verifiable control).<sup>2</sup> For example, U.S. companies that accept credit cards need to invest in encrypting outgoing transaction data, as required under the PCI-DSS.<sup>3</sup>

Second, and interestingly, security standards do not regulate all possible security controls. For example, PCI-DSS does not regulate the security of internal communication within a firm, even though past attacks—such as the aforementioned one on HPS—provide evidence that internal communication can be a target for attackers (Krebs 2009a, Cheney 2010). Hereafter we refer to any security control not regulated as an unverifiable control.<sup>4</sup> For a firm that deploys multiple security controls in a comprehensive protection plan, its investment on each of those controls can be interdependent. Therefore, even if a standard does not explicitly regulate a control, it may still indirectly affect a firm’s investment on this unverifiable control due to the firm’s strategic balancing of investments on all controls.

There are a variety of reasons why security standards do not cover all possible controls. Costs for writing and enforcing standards can be economically prohibitive for some controls. For example, given the large variety, complexity, and environmental contingency of exceptions (also called tickets) generated by an intrusion detection system (IDS), it would be cost prohibitive for a policy maker to write a detailed enough standard regulating what the correct response to every possible exception should be.<sup>5</sup> In addition, information security is a fast-evolving field where new security threats constantly emerge. Policy makers may overlook the importance of some existing controls or simply cannot foresee security controls not yet invented at the time of a security standard’s inception.<sup>6</sup> Finally, security controls involving human diligence—especially ones that deal with social engineering—are difficult to measure or to use as court evidence (Whitman and Mattord 2009, pp. 443–447).

Third, after a breach happens, it is not rare for a firm to cite their compliance with existing security standards for reducing its financial liability (Navetta 2009). Major payment card companies such as Visa and WorldPay explicitly allow merchants to use compliance as a liability reduction tool: Visa states that “it may waive fines in the event of a data compromise if there is no evidence of non-compliance with PCI-DSS and Visa rules” (Visa 2015). WorldPay further “provides an indemnity waiver of up to \$30,000 in approved costs” if a merchant complies with PCI-DSS (WorldPay 2014). Legal authorities also evidently cite compliance in past lawsuits and settlements. For example, following the much publicized information security breach at TJX Companies during 2005–2006, when TJX entered into an assurance with the Attorney Generals of several U.S. states to settle the cases brought against it, the legal agreement specifically asked TJX to provide documentation regarding its compliance with the PCI-DSS standards before establishing the settlement conditions (http://oag.ca.gov/ system/files/attachments/press\_releases/n1757\_tjx assurancesofcompliance.pdf).<sup>7</sup> Such ex post usage of standard compliance as a liability reduction tool can have ex ante implications on firm investment on any unverifiable security control.

In this research we explicitly acknowledge the above three mechanisms through which a mandatory standard can directly or indirectly affect firm security. We ask the following specific research questions:

1. How does a standard affect firm security when both verifiable and unverifiable controls exist? In particular, when and how can a tighter standard harm firm security?

2. How does the use of compliance as a liability reduction tool affect firm security?

3. How are optimal standard, firm security, and social welfare affected by key model constructs?

4. What are the consequences if a policy maker ignores the unverifiability issue when setting the standard?

In this paper we address these research questions using a game-theoretical model in which the overall firm security is dependent on two security controls. One control is verifiable, i.e., this control is explicitly regulated in a verifiable manner by the policy maker. The other is unverifiable and cannot be regulated by the policy maker.

It turns out the answer to how a standard affects firm security depends critically on how the two controls are connected to each other and to the digital asset to be protected—which we refer to as security configuration. We compare two fundamental configurations: serial, under which the digital asset is compromised only if both security controls are breached, and parallel, under which the digital asset is compromised if either security control is breached.

Our first finding is that, under serial configuration, firm security can decrease in the standard when the standard is not too high, even in the absence of any liability reduction from complying with the standard. Intuitively, a tighter standard directly results in more investment by the firm on the verifiable control, yet indirectly results in less investment on the unverifiable control due to a substitution effect between the two controls. The latter can dominate the former (thus resulting in lower overall firm security) only if the standard is not too high. Furthermore, if the firm’s investment on the verifiable control can reduce its share of liability, the firm’s overall security can decrease more in the standard.

On the other hand, our second finding is that, under parallel configuration, firm security decreases in the standard only when both of the following conditions hold: the firm’s investment on the verifiable control significantly reduces its liabilities upon breach and the standard is already high enough (note that this contrasts with the requirement of an upper bound on the standard under the serial configuration). Intuitively, under parallel configuration and without the liability reduction mechanism, the firm investments on the two controls are complements: a tighter standard both directly induces more investment on the verifiable control and indirectly induces more investment on the unverifiable control. When there is a strong liability reduction effect, however, it diminishes the firm’s incentive to invest on the unverifiable control. We show that, only when the standard is high enough, it is possible for the liability reduction effect to dominate the complementarity effect, thus resulting in lower overall security.

Our third finding concerns the relationship between the damage a firm suffers from a security breach and its investment on security controls. One might intuitively think that the higher the damage is, the more a firm cares about its security, and thus the less likely the firm will be to reduce its own overall security in the face of a tighter standard. Our third finding, however, overturns this intuition for a serial configuration: we show that a firm that cares more about security may react to a tighter standard by reducing its overall security even when a firm that cares less does not.

Our last two findings relate to policy maker decision and social welfare. Under a setting in which the firms meet the optimal standard set by a policy maker, we find that both firm security and social welfare are higher when the damage to the firm following a breach takes a higher share of the total damage to social welfare, and also when the firm takes a larger share of liability. This finding holds for both serial and parallel configurations.

Our last major finding concerns the consequences when the policy maker ignores the unverifiability issue when setting the standard. Under the serial configuration, ignoring the unverifiable control (and thus not taking it into consideration during standard setting) always leads the policy maker to set a standard higher than what is socially optimal. Under the parallel configuration, this overshooting behavior in standard setting happens when the damage to the firm following a breach is small enough relative to the total damage to social welfare. This overshooting behavior by the policy maker has two possible detrimental consequences: the cost of security investment is overly high and the resulting firm security can be lower than the optimal level.

The rest of this paper is organized as follows. In §2 we review the relevant literature. We present our model in §3. We analyze how the standard affects firm investments and overall firm security for parallel and serial configurations in §4. We then analyze the policy maker’s standard setting problem, as well as social welfare, in §5. Section 6 presents two model extensions. The first extension considers a boundedly rational policy maker that naively ignores the unverifiable control. The second extension considers an uncertainty in determining whether the verifiable control, unverifiable control, or both were compromised in a security breach. We discuss managerial implications and conclude this paper in §7.

## 2. Literature Review

Since security standards as a strategy to manage information security is a recent development, the extant research on this topic is limited. Much of the prior work on security standards has taken a descriptive approach to the standard setting problem and focused on principles that should govern information security standards (Keblawi and Sullivan 2007, Ross 2007, Morse and Raval 2008, Culnan and Williams 2009). Some of the recent work has empirically examined the impact of standards and laws related to breach disclosure and data encryption on security incidents. Romanosky et al. (2011) show that the adoption of data-breach disclosure laws has a marginal effect in reducing identity thefts. Miller and Tucker (2010) show that adoption of encryption software because of safe harbor provisions in breach notification regulations increases the incidents of publicized data losses, partly because of carelessness with respect to other protection activities on the part of those that should protect the information asset.

To our knowledge, Hui et al. (2013) is the only other paper that uses an analytical approach to show that an overly stringent security regulation can harm the security of firms. Our research differs from that of Hui et al. (2013) in several aspects. Hui et al. (2013) consider an outsourcing context in which multiple firms contract with a common security service provider, whereas we do not consider outsourcing. The key dynamic in the work of Hui et al. (2013) that leads to the result of tighter regulation harming firm security is a spillover effect: a shared security infrastructure at the common security provider implies that security risks are also shared. By contrast, we focus on the interplay between a single firm’s investments on verifiable and unverifiable security controls.

Although the extant literature on security standards is sparse, extensive work has been carried out on standards in other settings. Of particular relevance is the literature on financial auditing standards. Dye (1993) shows that the average quality of audits may decline as auditing standards become tougher. Willekens et al. (1996) argue that the increased difficulty of firing a compliant auditor that follows standards can reduce rather than increase the quality of audit work supplied. Schwartz (1997) finds that the socially optimal commitment according to auditing standards is achievable if the auditor’s legal liability regime is one of strict liability and is independent of the actual investment. Whereas research in the auditing standards literature models auditing as a single observable activity on which standards can be imposed, we consider a model in which multiple security controls exist and standards cannot be imposed on all of them.

Several recent studies in information security suggest that software vendors should take more liability upon security breaches to induce higher investment from them regarding software security (Ryan 2003, Cusumano 2004, Schneier 2008). August and Tunca (2011) further compare various liability mechanisms and show no one mechanism always dominates others. Kim et al. (2011) compares liability with patch release and shows either can be effective in some cases. Whereas the above studies look at the direct role of liability over information security, our research differs in that we examine the moderating role of liability on the relationship between standards and information security.

Besides security standards, the information security literature also touches on a wide range of topics such as optimal security investment, sharing of security information among firms, and empirical evidence of damages caused by security breaches. Hausken (2006b) shows that the particular shape of the marginal return curve (with respect to security investment) matters when a firm decides its optimal investment level. Regarding interfirm information sharing, Gordon et al. (2003) shows that encouraging the sharing of security information among firms without proper incentive mechanisms may result in a decreased level of information security because of free riding. Hausken (2006a) also shows free riding under interdependent information security among firms. Hausken (2007) advocates for an active role of social planners in regulating the sharing of security information. On the empirical side, a number of papers provide financial evidence regarding the damages caused by breaches: Campbell et al. (2003) find that if a breach involves a public company’s confidential information, the stock market reacts significantly and negatively. Cavusoglu et al. (2004) find that the change in market value of a breach firm is affected by firm type, firm size, and the time of breach. Our research contributes to the information security literature by examining the role of security standard in incentivizing firm investments when not all security controls are verifiable.

Our work is also related to the literature on incomplete contracts with unverifiable services. Bernheim and Whinston (1998) show it is often optimal to specify an incomplete contract when some aspects of performance are unverifiable. Battigalli and Maggi (2002) further propose optimal contracts with rigidity and discretion if writing a contract is very costly. Our research differs in that we consider security configurations, a dynamic specific to the information security context.

## 3. The Model

The model consists of a firm that is responsible for protecting a digital asset using two security controls and one policy maker that sets security standards that the firm must follow.

## 3.1. Security Controls

As modern information systems are getting increasingly complex, organizations often find themselves having a multitude of security weaknesses to address. Accordingly, a common practice is for organizations to deploy multiple security controls (controls in short) in a comprehensive protection plan, such as multiple firewalls to safeguard all entrances to a corporate network. In this paper we consider a parsimonious case in which, to protect the digital asset, the firm invests in two security controls, $V$ and $N . ^ { 8 }$ For each security control $i , i \in \{ \dot { V } , N \}$ , let $e _ { i }$ represent the probability that the firm can successfully prevent breach of this control. Notation $e _ { i }$ reflects the firm’s costly effort on control i— the higher the effort, the lower the breach probability.

To exert effort $e _ { i } ,$ the firm incurs a cost of $C _ { i } ( e _ { i } ) _ { }$ , which is a monotonically increasing and convex function with $C _ { i } ^ { \prime } ( 0 ) { = } 0$ for $i \in \{ V , N \}$ (for a similar stylized cost model, see, for example, Gordon and Loeb 2002). To be consistent with reality where perfect security is rarely possible regardless of related investment, we make the following assumption to ensure that neither the policy maker nor the firm will choose perfect security in equilibrium: $C _ { i } ^ { \prime } ( 1 ) = \infty$ for $i \in \{ V , N \}$ . For notational convenience, we denote marginal cost function as $c _ { i } \equiv C _ { i } ^ { \prime }$ and inverse marginal cost function as $r _ { i } \equiv c _ { i } ^ { - 1 }$ We make the following assumptions regarding the marginal cost functions:

Assumption 1. $( 1 - e _ { N } ) c _ { N } ^ { \prime } ( e _ { N } ) / c _ { N } ( e _ { N } )$ is weakly decreasing in $e _ { N } .$ , and $e _ { N } c _ { N } ^ { \prime } ( e _ { N } ) / c _ { N } ( e _ { N } )$ is weakly increasing in $e _ { N }$

Assumption 1 is not very restrictive in that it holds for commonly used cost function forms including power functions of any order, exponential functions, and polynomial functions with positive coefficients.

## 3.2. Security Configurations

We next describe the relationship between the two security controls and the security of the digital asset, which we refer to as security configuration. Let function $\omega ( e _ { V } , e _ { N } )$ denote the probability that security controls do not successfully protect the digital asset. We consider two basic and commonly seen relationships: serial and parallel configurations. Under serial configuration, the digital asset is compromised only if both security controls are breached, i.e.,

$$
\omega (e _ {V}, e _ {N}) = (1 - e _ {V}) (1 - e _ {N}).\tag{1}
$$

The serial configuration fits situations where attackers have to break through a combination of security controls to reach a digital asset. One example is the popular practice by firms to adopt both a firewall and an IDS to guard a network entrance, where a hacker has to render both ineffective to get access to internal data (Cavusoglu et al. 2009). The serial configuration also fits situations where firms are more concerned about service disruptions rather than unauthorized access of information (Loch et al. 1992). For example, a popular defense against denial-of-service (DoS) attacks for Web service operators is to mirror their services to multiple distributed Web servers. If one server experiences service outage due to DoS attacks, other redundant servers can take over and resume the service. Therefore, attackers will have to successfully take down all mirror sites to black out a Web service.

Under parallel configuration, the digital asset is compromised if either security control is breached

$$
\omega (e _ {V}, e _ {N}) = 1 - e _ {V} e _ {N}.\tag{2}
$$

One commonly seen example of the parallel configuration is a corporate network that is linked to the Internet at multiple access points, where each access point is secured by a separate firewall. Breaking any such firewall will then expose internal data to an attacker. Another example is when the digital asset is stored or can be assessed at multiple venues, e.g., one in an operational database and another in a backup server; breaching either server will lead to the leak of the digital asset.

Note that in practice, security configurations can be a complex combination of the aforementioned basic ones. $\mathrm { A s }$ a first theoretical exploration on understanding the impact of security configurations on the effectiveness of security regulation in the presence of an unverifiable control, we focus on the above two basic security configurations.

## 3.3. Security Regulation and Verifiability of Security Controls

Although the direct control of security efforts is in the hands of the firm, a policy maker can indirectly affect firm efforts through regulatory standards (such as the PCI-DSS) on any verifiable security control. In this paper we consider the case where security control V is verifiable to the policy maker, whereas N is not. For example, and in the context of reducing firewall breaches, control V can be the frequency of external review of firewall rule sets that is contractually verifiable and thus enforceable by the policy maker. (In PCI-DSS version 1.2.1, this is regulated under item 1.1.6.) Control N can be a firm’s managerial effort spent on discouraging employees from visiting external websites that are irrelevant to their jobs, whereas such effort is hard to monitor, quantify, and later use as court evidence should a breach happen.

As a result, the policy maker can only mandate a standard s for control ${ \check { V } } ,$ which is a verifiable effort threshold that the firm must match or exceed. For example, item 1.1.6 in PCI-DSS version 1.2.1 requires a firm to “review firewall and router rule sets at least every six months” (PCI Security Standards Council 2009, p. 15). In other words, once the policy maker sets $s ,$ the firm cannot pick any $e _ { V } < s .$ . For the scope of this paper, we focus on security standards that have strict enforcement power, so that the affected firm has to unconditionally confirm. Two widely applicable examples are NIST security standards and the PCI-DSS. NIST standards are mandatory for all affected U.S. governmental agencies (Keblawi and Sullivan 2007). The PCI-DSS is mandatory for any merchant that “accepts, transmits or stores any cardholder data” (http://www.pcicomplianceguide.org/pci-faqs $- 2 / \# 2 )$ . Also, we only consider $s \in [ 0 , 1 )$ , where the upper bound means that the policy maker will never demand perfect security (and is consistent with our assumption that $c _ { i } ( 1 ) = \infty$ for $i \in \{ V , N \} )$ 5.

Figure 1 Timing of the Model

<table><tr><td>Policy maker announces standard s for control V</td><td>Firm exerts efforts ev and eN in security controls V and N, respectively</td><td>Payoff/damage realized depending on whether information asset is compromised</td></tr><tr><td>Period 1</td><td>Period 2</td><td>Period 3</td></tr></table>

## 3.4. Payoff Structure of the Firm

Note that the firm’s primary business can be (and in practice often is) different from security provision. For example, the primary business function of HPS is to process payment card transactions, whereas it invests in security to protect this primary function. We focus on security issues in this paper and assume that, notwithstanding a security compromise, the firm earns a positive business profit of $W _ { F }$ . We further assume that $W _ { F }$ is large enough so that the firm will not exit the market merely due to information security concerns. We model the firm’s payoff structure as follows:

$$
U _ {F} = W _ {F} - \omega (e _ {V}, e _ {N}) (1 - k e _ {V}) D _ {F} - C _ {V} (e _ {V}) - C _ {N} (e _ {N}).\tag{3}
$$

In (3), term $( 1 - k e _ { V } ) D _ { F }$ represents the damage to the firm if the digital asset is compromised. This damage consists of two components: $1 - k e _ { V }$ and $D _ { F }$ . The first component, $1 - k e _ { V }$ 1 captures the liability reduction effect of a security standard: the higher $e _ { V }$ is, the lower the damage to the firm $\mathrm { i s . ^ { 9 } }$ Because $e _ { N }$ is unverifiable, this liability reduction effect depends only on $e _ { V } . { } ^ { 1 0 }$ We refer to k as liability reduction factor; $0 \leq k < 1$ . The second component, $D _ { F } ,$ is the firm’s maximum damage under full liability. Let $D _ { F }$ include opportunity costs, i.e., what the firm would have gained should the compromise not take place.

## 3.5. Payoff Structure of the Policy Maker

The policy maker aims to maximize social welfare as follows:

$$
U _ {S W} = W _ {S W} - \omega (e _ {V}, e _ {N}) D _ {S W} - C _ {V} (e _ {V}) - C _ {N} (e _ {N}),\tag{4}
$$

where $W _ { S W } > W _ { F }$ and $D _ { S W } > D _ { F }$

Figure 1 shows the timing of the model, which is a sequential-move game with three periods. The policy maker first announces the standard, $s ,$ for control $V .$ The firm then chooses its investments $e _ { V }$ and $e _ { N }$ on the security controls. Payoff is realized depending on whether the information asset is compromised.

## 4. The Impact of Standard on Firm Security

In this section we study how the security standard influences a firm’s overall security; that is, we assume that the policy maker has announced a standard in Period 1, and we examine how this standard affects the firm’s security. We first consider the serial configuration, and then consider the parallel configuration.

## 4.1. Serial Configuration

We use subscript $^ { \prime \prime } \mathrm { S } { \cal C } ^ { \prime \prime }$ to denote results for the serial configuration. Given any standard $s _ { S C }$ for control V that is imposed by the policy maker, the firm’s optimization problem is

$$
\begin{array}{l} \max _ {e _ {V}, e _ {N}} U _ {F} \\ = W _ {F} - (1 - e _ {V}) (1 - e _ {N}) (1 - k e _ {V}) D _ {F} - C _ {V} (e _ {V}) - C _ {N} (e _ {N}) \\ \text { s.t. } e _ {V} \geq s _ {\mathrm{SC}}. \end{array} \tag {5}
$$

For convenience, define $\hat { s } _ { S C }$ as the solution to $( 1 -$ $r _ { N } ( ( 1 - \hat { s } _ { S C } ) ( 1 - k \hat { s } _ { S C } ) D _ { F } ) ) ( 1 - 2 k \hat { s } _ { S C } + k ) D _ { F } = c _ { V } ( \hat { s } _ { S C } )$ Solving the above maximization problem, we get the following:

<sup>Lemma</sup> <sup>1.</sup> Under serial configuration and given standard $s _ { S C }$ for control $V ,$ the firm’s effort on the verifiable control is $e _ { V } ^ { * } = \hat { s } _ { S C } \ i f s _ { S C } \leq \hat { s } _ { S C }$ and is $e _ { V } ^ { * } = s _ { S C } \ i f \ s _ { S C } > \hat { s } _ { S C } ,$ and its effort on the unverifiable control is

$$
e _ {N} ^ {*} = r _ {N} ((1 - e _ {V} ^ {*}) (1 - k e _ {V} ^ {*}) D _ {F}).\tag{6}
$$

Proofs of all lemmas and propositions are in Online Appendix A (available as supplemental material at http://dx.doi.org/10.1287/isre.2015.0607). Lemma 1 has three implications. First, Lemma 1 shows that a security standard $s _ { S C }$ matters only when it is above a minimal threshold $\hat { s } _ { S C }$ . This is intuitive because the firm’s own unconstrained incentive in security investment is stronger than what the policy maker mandates if the standard is too low. Second, if the standard is tight enough $( \mathbf { i . e . } , s _ { S C } > \hat { s } _ { S C } )$ , the firm will simply match its effort on the verifiable control with this standard. Third, if the standard is tight enough, it also indirectly and negatively influences the firm effort on the unverifiable control, $e _ { N } ,$ through two distinct dynamics, which we refer to as the substitution effect and the liability reduction effect. Intuitively, under the serial configuration, the firm’s investments on the two controls are substitutes: an increase of investment on one control reduces the marginal impact of the other control on firm security. The substitution effect refers to the dynamic that a higher standard $s _ { S C }$ (and thus a higher effort on the verifiable control) decreases the marginal value of $e _ { N }$ on reducing the breach probability $( \mathrm { i . e . , o n } \omega )$ , thus leading to a diminished $e _ { N } ^ { * }$ . This is evident from term $( 1 - e _ { V } ^ { * } )$ on the right-hand side of (6). The standard also influences the firm effort through a liability reduction effect: because a higher investment on the verifiable control reduces the firm’s share of liability should a breach happen, it reduces the firm’s incentive in further securing its digital asset through the unverifiable control, thus resulting in a reduced $e _ { N } ^ { * }$ This is evident from term $( 1 - k e _ { V } ^ { * } )$ on the right-hand side of (6).

Now we analyze how the standard affects the firm’s overall security (or firm security in short), as measured by $1 - \omega ( e _ { V } , \bar { e _ { N } } ) = \bar { 1 } - ( 1 - e _ { V } ) ( 1 - e _ { N } )$ . Given any $s _ { S C } ,$ from Lemma 1 we know this overall security under serial configuration can be expressed as

$$
\begin{array}{l} 1 - \omega (e _ {V} ^ {*} (s _ {S C}), e _ {N} ^ {*} (s _ {S C})) \\ = 1 - (1 - e _ {V} ^ {*} (s _ {S C})) (1 - r _ {N} ((1 - e _ {V} ^ {*} (s _ {S C})) \\ \cdot (1 - k e _ {V} ^ {*} (s _ {S C})) D _ {F})). \end{array}\tag{7}
$$

We next show that the substitution effect alone may generate the result that increasing the security standard can reduce overall firm security. Denote by $\underline { { D } } _ { F }$ the solution to $( 1 - r _ { N } ( \underline { { D } } _ { F } ) ) / ( r _ { N } ^ { \prime } ( \underline { { D } } _ { F } ) \dot { \underline { { D } } } _ { F } ) = 1$ , and by s the solution to

$$
\frac {1 - r _ {N} ((1 - \underline {{s}}) (1 - k \underline {{s}}) D _ {F})}{r _ {N} ^ {\prime} ((1 - \underline {{s}}) (1 - k \underline {{s}}) D _ {F}) (1 - \underline {{s}}) (1 - k \underline {{s}}) D _ {F}} = 2 - \frac {1 - k}{1 - k \underline {{s}}}.
$$

<sup>Proposition</sup> <sup>1.</sup> Under the serial configuration, if $D _ { F } >$ $\underline { { D } } _ { F }$ and $\underline { { s } } > \hat { s } _ { S C } ,$

(i) firm security is not affected by security standard $s _ { S C }$ $i f s _ { S C } \leq \hat { s } _ { S C } .$

(ii) firm security is strictly decreasing in security standard $s _ { S C } ~ i f \hat { s } _ { S C } < s _ { S C } < \underline { { s } } ,$

(iii) firm security is strictly increasing in security standard $s _ { S C } ~ i f ~ s _ { S C } > { \underline { { s } } } .$

Part (ii) of Proposition 1 shows that when $D _ { F } >$ $\underline { { D } } _ { F }$ and $\underline { s } > \hat { s } _ { S C } .$ , increasing the standard—as long as it is bounded within $( \hat { s } , \bar { s } ) \mathrm { - } \mathrm { c a n }$ harm firm security regardless of whether the liability reduction effect exists or not. To understand why the standard being upper bounded by $\underline { s }$ is a necessary condition for this interesting result, we next isolate and then compare the direct effect of the standard on control V and the indirect effect of it on control N . Because firm security contains a multiplicative function as in $( 7 ) .$ , we use a logarithm transformation of the overall breach probability $( \mathrm { i . e . , } \omega )$ for easier graphical comparison

$$
\begin{array}{r l} & {\ln (\omega) = \ln \big [ (1 - e _ {V} ^ {*} (s _ {S C})) (1 - e _ {N} ^ {*} (s _ {S C})) \big ]} \\ & {\qquad = \ln (1 - s _ {S C}) + \ln (1 - r _ {N} ((1 - s _ {S C}) (1 - k s _ {S C}) D _ {F})).} \end{array}
$$

Figure 2 (Color online) Breach Probabilities of the Verifiable and the Unverifiable Controls as a Function of $ { \boldsymbol { s } } _ { s c }$  
![](/api/attachments/MX6QREND/fulltext/images/72dba6359257968af785aa802f1eeea1abf7a03c6604777a8ad46fc65b55e4a1.jpg)  
Note. For Figure 2, we use $D _ { F } = 2 , 0 0 0 , 0 0 0 , k = 0 . 1$ , and $C _ { i } ( \pmb { \theta } _ { i } ) = \pmb { e } ^ { 1 0 \pmb { e } _ { i } }$ $1 0 e _ { i } - 1$ . We pick this sample cost function because it ensures zero (very high) marginal cost at zero (full) effort level.

Figure 2 illustrates the direct effect $( \ln ( 1 - s _ { S C } ) )$ , the indirect effect $( \ln ( 1 - r _ { N } ( ( 1 - s _ { S C } ) ( 1 - k s _ { S C } ) D _ { F } ) ) )$ , and the overall breach probability ln45—all with logarithm transformation. Intuitively, the smaller $s _ { S C }$ is, the faster (slower) the indirect (direct) effect changes in $s _ { S C } { \mathrm { - i . e . , } }$ the solid (dashed) line in Figure 2 is steeper (flatter) when $s _ { S C }$ is smaller. Formally,

$$
\begin{array}{r l} & d \ln (1 - e _ {N} ^ {*} (s _ {S C})) / d s _ {S C} \\ & = \frac {r _ {N} ^ {\prime} ((1 - s _ {S C}) (1 - k s _ {S C}) D _ {F}) (1 + k - 2 k s _ {S C}) D _ {F}}{1 - r _ {N} ((1 - s _ {S C}) (1 - k s _ {S C}) D _ {F})} > 0, \end{array}
$$

and $d \ln ( 1 - e _ { V } ^ { \ast } ( s _ { S C } ) ) / d s _ { S C } = - 1 / ( 1 - s _ { S C } ) < 0$ . Note that $\underline { s }$ is the threshold value where d ln $( 1 - e _ { N } ^ { * } ( s _ { S C } ) ) / d s _ { S C } =$ $| d \ln ( 1 - e _ { V } ^ { * } ( s _ { S C } ) ) / d s _ { S C } |$ . Therefore, for any standard $s < { \underline { { s } } } ,$ the change in the indirect effect dominates the opposite change in the direct effect $( \mathrm { i . e . , ~ } d \ln ( 1 - e _ { N } ^ { * } ( s _ { S C } ) ) / \bar { d } s _ { S C } >$ $| d \ln ( \bar { 1 } - e _ { V } ^ { * } ( s _ { S C } ) ) / d s _ { S C } | )$ , thus resulting in a reduction of firm security.

Proposition 1 requires $\underline { s } > \hat { s } _ { S C } . ^ { 1 1 }$ In Online Appendix B, we show that with a mild assumption regarding the firm’s unconstrained security investment (that holds for commonly used cost function forms including power functions, exponential functions, and negative logarithmic functions), $\underline { { s } } > \hat { s } _ { S C }$ holds true for any form of the cost functions as long as $D _ { F }$ is sufficiently large.<sup>12</sup>

Proposition 1 also requires $D _ { F } > \underline { { { D } } } _ { F }$ . Intuitively, from Equation (6) we know a larger $D _ { F }$ implies a larger $e _ { N } ^ { * } ,$ and consequently a greater substitution effect. When $D _ { F }$ is high enough $( \mathrm { i } . \mathrm { e } . , D _ { F } > \underline { { { D } } } _ { F } )$ , and given $\begin{array} { r } { s _ { S C } < \underline { s } . } \end{array}$ , the substitution effect alone is large enough so that, when the standard increases, the reduction in $e _ { N } ^ { * }$ dominates the increment in $e _ { V } ^ { * }$ in terms of driving the overall

## Figure 3 (Color online) The Impact of Standard $s _ { S C }$ on $\pmb { \theta } _ { N } ^ { * }$ and Firm Security

![](/api/attachments/MX6QREND/fulltext/images/f587c1247bd348468389372480c940c6c3ee2058721dfac1532729484b451f7e.jpg)  
Note. $D _ { F } = 2 0 , c _ { V } ( e _ { V } ) = e _ { V } / ( 1 - e _ { V } )$ , and $c _ { N } ( e _ { N } ) = e _ { N } / ( 1 - e _ { N } )$

firm security. When $\boldsymbol { D } _ { F } \le \underline { { \boldsymbol { D } } } _ { F } ,$ however, the substitution effect alone is not sufficient in driving the result that security decreases in standard for any standard range:

<sup>Proposition</sup> <sup>2.</sup> Under the serial configuration, if $D _ { F } <$ $\underline { { D } } _ { F }$ and $\underline { { s } } > \hat { s } _ { S C } ,$

(i) firm security is not affected by security standard $s _ { S C }$ $i f s _ { S C } \leq \hat { s } _ { S C } .$ J

(ii) firm security is strictly decreasing in security standard $s _ { S C } \ i f$ the liability reduction factor k is large enough $( i . e . , k > ( 1 - r _ { N } ( D _ { F } ) ) / ( r _ { N } ^ { \prime } ( D _ { F } ) D _ { F } ) - 1 )$ and $\hat { s } _ { S C } < s _ { S C } < \underline { { s } } ,$ (iii) firm security is strictly increasing in security standard $s _ { S C }$ otherwise.

As shown in the left side of Figure 3, a strong liability reduction effect (i.e., a large k)—on top of the substitution effect—further dampens the firm’s incentive to invest in control N . When k is large enough and the standard is not too high, the firm’s scaling-back of investment on control N can be significant enough to pull down its overall security as shown by the solid line in the right side of Figure 3.

Interestingly, if the standard is very high, it is less likely that a strong liability reduction effect can harm overall firm security. Intuitively, when the standard is very high, the firm invests heavily on control $V ,$ which is then the primary driver of overall firm security. Consequently the firm’s investment on control N is always minimal regardless of how strong the liability reduction effect is; this diminishes the role of the liability reduction effect in driving firm security.

We next turn our attention to the role of $D _ { F }$ in influencing firm security. A higher $D _ { F }$ implies that the firm cares more about security. One might then intuitively think that the higher $D _ { F }$ is, the less likely it is a higher standard will harm the firm’s overall security. The next proposition shows that, however, this intuition is not accurate.

![](/api/attachments/MX6QREND/fulltext/images/26e69df7cf5b59163afe0e45f13a8cb2fe3fb40e57e84805f2a860d81bc2821e.jpg)

<sup>Proposition</sup> <sup>3.</sup> Under the serial configuration, $\partial { \underline { { s } } } / \partial D _ { F }$ $\geq 0 .$

Recall that $\underline { s }$ is the threshold standard level below which a tighter standard hurts firm security (conditional on the standard being higher than $\hat { s } _ { S C } )$ . Proposition 3 says that the more a firm cares about its security $( \mathrm { i . e . , }$ the higher $D _ { F } { \mathrm { i s } } )$ , the higher this threshold level is. This proposition thus implies that when the policy maker increases the security standard, a firm that cares more about security may react by reducing its overall security even when a firm that cares less does not. This result is illustrated in Figure 4. In this example, $D _ { F } = 5 , 0 0 0 , 0 0 0$ $( D _ { F } = 1 0 , 0 0 0 , 0 0 0 )$ represents the case where the firm cares less (more) about its own security. When $0 . 9 3 \leq$ $s _ { S C } < 0 . 9 6 ,$ the firm that cares less about security always responds to a marginally tighter standard by increasing its overall security (see the dashed line), whereas the firm that cares more responds to a marginally tighter standard by decreasing its overall security (see the solid line).

Figure 4 (Color online) Firm Security Under Different Levels of Damage $D _ { F }$  
![](/api/attachments/MX6QREND/fulltext/images/94d82845469e4298736c3a63e5f096234db29a419a2a3fe6cc744d83c0960493.jpg)  
Note. $C _ { i } ( \pmb { \theta } _ { i } ) = e ^ { 1 0 \pmb { e } _ { i } } - 1 0 \pmb { e } _ { i } - 1$ and k = 009.

Figure 5 (Color online) Investment and Marginal Investment on Unverifiable Control Under Different Levels of $D _ { F }$  
![](/api/attachments/MX6QREND/fulltext/images/ff87f505675c03ec8ddce79b8acb8d75d814bccdd7773e28f7e55a0965ed0c12.jpg)  
The intuition behind this striking result lies in how a tighter standard marginally affects firm security. For notational convenience, let $\dot { f } ( s _ { S C } , D _ { F } )$ denote firm security $( \mathrm { i . e . , } 1 - \omega )$ under serial configuration for any given standard $s _ { S C }$ and damage $D _ { F } .$ . By partially differentiating firm security with respect to $s _ { S C } ,$ we see that the marginal firm security consists of three components: a constant (the first term of the right-hand side in Equation (8)), the marginal value of a firm’s investment on the unverifiable control (the second term), and the investment on the unverifiable control (the third term);

$$
\begin{array}{r l} & {\frac {\partial f (s _ {S C} , D _ {F})}{\partial s _ {S C}}} \\ & {\qquad = 1 + (1 - s _ {S C}) \frac {\partial e _ {N} ^ {*} (s _ {S C} , D _ {F})}{\partial s _ {S C}} - e _ {N} ^ {*} (s _ {S C}, D _ {F}).} \end{array}\tag{8}
$$

We now check how the last two terms on the righthand side of Equation (8) react to the damages and provide the intuition for these terms.

Regarding the second term, ceteris paribus, the more a firm cares about its security, the more it scales back its marginal investment on the unverifiable control (than the firm that cares less), i.e., $\partial ( \partial e _ { N } ^ { * } ( s _ { S C } , D _ { F } ) / \partial s _ { S C } ) / \partial D _ { F } < 0$ . This change in diminishing marginal value of a firm’s investment on the unverifiable control is illustrated in Figure 5(a) on the first-order differentiation of $e _ { N } ^ { * }$ over $s _ { S C } \colon$ in absolute terms, this change is always larger under $D _ { F } =$ 1010001000 (see the solid line) than that under $D _ { F } =$ 510001000 (see the dashed line). Intuitively, the firm that cares more always invests at a much higher cost level on the unverifiable control. When the standard increases, however, the increased investment on the verifiable control diminishes the marginal value of a firm’s investment on the unverifiable one, and a higher $D _ { F }$ amplifies this diminishing marginal value, thus resulting in more scaling back of investment.

Regarding the third term, the firm that cares more about security has a higher investment on the unverifiable control (than the firm that cares less), i.e., $\partial e _ { N } ^ { * } ( s _ { S C } , D _ { F } ) / \partial D _ { F } > 0$ . As illustrated in Figure 5(b), $e _ { N } ^ { * } ( s )$ is larger under $D _ { F } = 1 0 , 0 0 0 , 0 0 0$ (solid line) than under $D _ { F } \bar { = } 5 , 0 0 0 , 0 0 0$ (dashed line). When the standard increases, the increased investment on the verifiable control discourages a firm from making an investment on the unverifiable control because of the substitution effect, and a higher $D _ { F }$ strengthens this substitution effect.

(b) The impact of S<sub>SC</sub> on e<sub>N</sub><sup>\*</sup>  
![](/api/attachments/MX6QREND/fulltext/images/c0a1e6b9c73eb328082cbcd40601d4ecdc7ef31afceb5b543b39a640305ff5e3.jpg)

To summarize, a higher $D _ { F }$ discourages the firm more in terms of investing in the unverifiable control in the face of a tighter security standard because of both the diminishing marginal value (the second term) and the diminishing value (the third term) with respect to $e _ { N } ^ { * }$

## 4.2. Parallel Configuration

We now analyze how the security standard influences firm security under parallel configuration. We use the subscript $^ { \prime \prime } \bar { \mathrm { P } } { \cal C } ^ { \prime \prime }$ for this case. For any given standard $s _ { P C }$ on control V , the firm’s optimization problem is

$$
\begin{array}{l} \max _ {e _ {V}, e _ {N}} U _ {F} \\ = W _ {F} - (1 - e _ {V} e _ {N}) (1 - k e _ {V}) D _ {F} - C _ {V} (e _ {V}) - C _ {N} (e _ {N}) \\ \text { s.t. } e _ {V} \geq s _ {P C}. \end{array} \tag {1}\tag{9}
$$

Define $\hat { s } _ { P C }$ as the solution to $k D _ { F } + r _ { N } ( \hat { s } _ { P C } ( 1 - k \hat { s } _ { P C } )$ $D _ { F } ) ( 1 - 2 \bar { k } \tilde { s } _ { P C } ) D _ { F } = c _ { V } ( \hat { s } _ { P C } )$ . Solving the above maximization problem, we get the following:

<sup>Lemma</sup> <sup>2.</sup> Under parallel configuration and given standard $s _ { P C } \ f o r$ control $\scriptstyle { \dot { V } } ,$ the firm’s effort on the verifiable control is $e _ { V } ^ { * } = \hat { s } _ { P C } \ i f \ s _ { P C } \leq \hat { s } _ { P C }$ and is $e _ { V } ^ { * } = s _ { P C } \ i f \ s _ { P C } > \hat { s } _ { P C } ,$ and its effort on the unverifiable control is

$$
e _ {N} ^ {*} = r _ {N} (e _ {V} ^ {*} (1 - k e _ {V} ^ {*}) D _ {F}).\tag{10}
$$

There are three similarities between serial and parallel configurations in terms of the firm’s response to a security standard. First, a low enough standard $( \mathrm { i . e . , }$ $s _ { P C } \leq \hat { s } _ { P C } \sp { \mathrm { ~ ~ } } )$ has no impact on firm investments. Second, if

## Figure 6 (Color online) Firm Security as a Function of $s _ { P C }$ Under Parallel Configuration

![](/api/attachments/MX6QREND/fulltext/images/40a77e7335165d2608be7238a373b704fcd7f738b2b0b6038a0d7bcfee8c3966.jpg)  
Note. $D _ { F } = 3 , 0 0 0$ and $C _ { i } ( \pmb { \theta } _ { i } ) = e ^ { 6 \pmb { e } _ { i } } - 6 \pmb { \theta } _ { i } - 1 .$

the standard is high enough $( \mathrm { i } . \mathrm { e } . , s _ { P C } > \hat { s } _ { P C } )$ , the firm’s investment on the verifiable control will match the standard, i.e., $e _ { V } ^ { * } = s _ { P C }$ . Third, the liability reduction effect continues to influence investment on the unverifiable control under the parallel configuration, as evident from term $( 1 - k e _ { V } ^ { * } )$ on the right-hand side of (10).

The parallel configuration, nevertheless, differs from the serial configuration in that, under the former, the standard indirectly and positively influences the firm effort on the unverifiable control—evident from term $e _ { V } ^ { * }$ on the right-hand side of (10). We refer to this indirect effect as the “complementarity $e f f e c t . ^ { \prime \prime }$ Intuitively, under the parallel configuration, the firm’s investment on one control is effective only if the investment on the other control is not disproportionally low.

Taking both the liability reduction effect and complementarity effect together, (10) implies that the firm investment on the unverifiable control is decreasing in standard if and only if $s _ { P C } > 1 / ( 2 k )$ . Intuitively, a higher standard reduces the firm’s share of liability more, and thus disincentivizes it from investing in the unverifiable control.

The next proposition summarizes how the standard affects overall firm security under the parallel configuration, as measured by $1 - \omega ( e _ { V } ^ { * } ( s _ { P C } ) , e _ { N } ^ { * } ( s _ { P C } ) ) =$ $e _ { V } ^ { * } ( s _ { P C } ) \cdot r _ { N } ( e _ { V } ^ { * } ( s _ { P C } ) ( 1 - k e _ { V _ { - } } ^ { * } ( s _ { P C } ) ) D _ { F } )$ . Denote <sup>¯</sup>k as the unique solution to $r _ { N } ( ( 1 - \bar { k } ) D _ { F } ) / ( r _ { N } ^ { \prime } ( ( 1 - \bar { k } ) D _ { F } ) ( 1 - \bar { k } )$ ${ D _ { F } } \bar { ) = } 1 / ( 1 - \bar { k } ) - 2$ and s¯ as the unique solution to

$$
\frac {r _ {N} (\bar {s} (1 - k \bar {s}) D _ {F})}{r _ {N} ^ {\prime} (\bar {s} (1 - k \bar {s}) D _ {F}) (\bar {s} (1 - k \bar {s}) D _ {F})} = \frac {1}{1 - k \bar {s}} - 2.
$$

<sup>Proposition</sup> <sup>4.</sup> Under the parallel configuration,

(i) firm security is not affected by security standard $s _ { P C }$ $i f s _ { P C } \leq \hat { s } _ { P C } .$

(ii) firm security is strictly decreasing in security standard $s _ { P C } \ i f \ k > \bar { k }$ and $s _ { P C } > \mathrm { m a x } \{ \hat { s } _ { P C } , \bar { s } , 1 / ( 2 k ) \}$

(iii) firm security is strictly increasing in security standard $s _ { P C }$ otherwise.

![](/api/attachments/MX6QREND/fulltext/images/531737074bbe1be966554713d8132c14752955193ff1fd5fc656726637257f95.jpg)

Part (ii) of Proposition 4 says that a higher standard reduces firm security only when both of the following conditions hold: the liability reduction effect is strong enough and the standard is high enough. The intuition behind the necessity of a strong liability reduction effect is analogous to that under the serial configuration: the higher k is, the less the firm suffers under a breach, and thus the less the firm is willing to invest in the unverifiable control (as illustrated by the left plot in Figure 6).

When it comes to the necessity of a high standard, a higher $s _ { P C }$ intensifies the marginal impact of $k$ on $e _ { N } ^ { * } .$ Therefore, when the standard is already high and when it further increases, the liability reduction effect incentivizes the firm to significantly reduce its effort on the unverifiable control to the extent that it dominates the firm’s increased effort on the verifiable control, thus resulting in decreased overall firm security. Note that, as illustrated by the right plot in Figure $^ { 6 , }$ decreased overall firm security can happen only if the liability reduction effect is above a threshold value $\bar { k } ;$ otherwise, even the strongest possible standard (and resulting reduced liability) cannot induce enough reduction in the security of the unverifiable control that dominates the security improvement on the verifiable control.

A comparison of Part (ii) of Proposition 1 and Part (ii) of Proposition 4 reveals an important insight regarding the difference between the serial and parallel configurations: firm security can decrease in the standard under both configurations, albeit in different ranges $o f$ standards. Under the serial configuration, firm security can decrease in standard only under relatively low standard. In sharp contrast, under the parallel configuration, firm security can decrease in the standard only under relatively high standard. Interestingly, under the parallel configuration, this reduction of investment on the unverifiable control plays an increasingly significant role to overall firm security when the standard increases, whereas under the serial configuration it actually plays a diminishing role because of the substitution effect between the two security controls.

We also briefly comment on when part (ii) of Proposition 4 is feasible, i.e., when all of $\bar { k } , \hat { \hat { s } } _ { P C } ,$ and s¯ will be less than 1. In proving Proposition 4, we have shown that $\bar { s } < 1$ for any $k > \bar { k }$ (see the end of its proof). From the definition of $\hat { s } _ { P C }$ it is straightforward that $\hat { s } _ { P C } < 1$ always holds, because otherwise the firm will incur an infinite cost of security investment. Therefore, the feasibility issue depends solely on when $\bar { k } < 1 \mathrm { - i n }$ Online Appendix B we show that $\bar { k } < 1$ as long as $\begin{array} { r } { D _ { F } > \operatorname* { l i m } _ { \sigma \to 0 ^ { + } } r _ { N } ( \sigma ) / r _ { N } ^ { \prime } ( \sigma ) } \end{array}$ . In other words, as long as the security damage to the firm, $D _ { F } .$ , is higher than a cost-related ratio limit lim $_ { \cdot \sigma \to 0 ^ { + } } r _ { N } ( \sigma ) / r _ { N } ^ { \prime } ( \sigma )$ , part (ii) of Proposition 4 is feasible.<sup>13</sup> We next study the decision of the policy maker and the implications to social welfare.

## 5. Policy Maker Decision and Social Welfare Analysis

In this section we study standard setting by the policy maker in Period 1. We assume that the policy maker aims to maximize social welfare. Specifically, we study how the optimal standard, firm security, and social welfare are affected by three key model constructs2 the security configuration, the liability reduction factor k, and the ratio of damages to the firm and to social welfare, $D _ { F } / D _ { S W }$ . One analytical challenge in this section is that, because of the complexity of the model, it is infeasible to describe an explicit solution of the policy maker’s optimal standard. Accordingly, we employ a combination of analytical and numerical tools to get insights on the above questions.

We first consider the serial configuration. Recall from Lemma 1 that $e _ { N } ( s _ { S C } ) = r _ { N } ( ( 1 - s _ { S C } ^ { - } ) ( 1 - k s _ { S C } ) D _ { F } )$ if $S _ { S C } > \hat { s } _ { S C }$ . Note that, if $\mathit { s } _ { S C } \leq \hat { \mathit { s } } _ { S C } ,$ s does not affect the social welfare. Let

$$
\begin{array}{l} s _ {S C} ^ {*} = \underset {s _ {S C}} {\arg \max} U _ {S W} \\ = W _ {S W} - (1 - s _ {S C}) (1 - r _ {N} ((1 - s _ {S C} (1 - k s _ {S C}) D _ {F})) D _ {S W} \\ \quad - C _ {V} (s _ {S C}) - C _ {N} (r _ {N} ((1 - s _ {S C}) (1 - k s _ {S C}) D _ {F})). \end{array} \tag {11}
$$

We ignore the uninteresting case of $s _ { S C } ^ { * } \leq \hat { s } _ { S C }$ in the rest of the discussion. The next proposition shows how the liability reduction factor k and the ratio of damages to the firm and to social welfare $D _ { F } / D _ { S W }$ affect social welfare under this optimal standard:

<sup>Proposition</sup> <sup>5.</sup> Under serial configuration, $i f s _ { S C } ^ { * } > \hat { s } _ { S C } ,$ the optimal social welfare $U _ { S W } ( s _ { S C } ^ { * } )$ decreases in the liability reduction factor k and increases in the ratio of damages to the firm and to social welfare $D _ { F } / D _ { S W }$

We next consider the parallel configuration and derive a result similar to Proposition 5. From Lemma 2 we have that, under any effective standard, $e _ { N } ( s _ { P C } ) =$ $r _ { N } ( s _ { P C } ( 1 - k s _ { P C } ) D _ { F } )$ if $s _ { P C } > \hat { s } _ { P C }$ . Therefore, let

$$
\begin{array}{c} s _ {P C} ^ {*} = \underset {s _ {P C}} {\arg \max} U _ {S W} \\ = W _ {S W} - (1 - s _ {P C} r _ {N} (s _ {P C} (1 - k s _ {P C}) D _ {F})) D _ {S W} \\ - C _ {V} (s _ {P C}) - C _ {N} (r _ {N} (s _ {P C} (1 - k s _ {P C}) D _ {F})). \end{array}\tag{12}
$$

We consider only the interesting case of $s _ { P C } ^ { * } > \hat { s } _ { P C }$ in the rest of the discussion.

<sup>Proposition</sup> <sup>6.</sup> Under parallel configuration, $i f s _ { P C } ^ { * } >$ $\hat { s } _ { P C } ^ { \phantom { \dagger } } ,$ , the optimal social welfare $U _ { S W } ( s _ { P C } ^ { * } )$ decreases in the liability reduction factor k and increases in the ratio of damages to the firm and to social welfare $D _ { F } / D _ { S W }$

Propositions 5 and 6 together have three implications for policy makers. First, they show that in the presence of the unverifiable control, allowing liability reduction for the firm will be detrimental to social welfare. Intuitively, the existence of control N leads to a moral hazard problem that the liability reduction effect exacerbates: the less the liability the firm shoulders, the less incentive for the firm to invest in this unverifiable control N conditional on that it has already met the standard on control V .

Propositions 5 and 6 also show that the maximum share of the total security damage that the firm shoulders, $D _ { F } / D _ { S W } ,$ , positively affects social welfare.<sup>14</sup> Intuitively, the higher this ratio is, the more the firm’s incentive is aligned with that of the social planner. Note, however, that the first-best outcome (i.e., maximum social welfare if both controls are verifiable) is still not obtainable even if this ratio $D _ { F } / D _ { S W }$ is 1 because of the liability reduction effect.

Recall from §4 that the security configuration plays a prominent role in driving the firm’s investment decisions: the serial configuration results in a substitution effect, whereas the parallel configuration results in a sharply different complementarity effect. By contrast, the security configuration plays a less important role for social welfare analysis: Propositions 5 and 6 show that the comparative statics regarding social welfare are qualitatively similar under both security configurations.

We next conduct several numerical studies regarding how k and $D _ { F } / D _ { S W }$ affect the optimal standard and firm security. We use an exponential cost function $C _ { i } ( e _ { i } ) = \exp ( 1 0 e _ { i } ) - 1 0 e _ { i } - 1$ where $i \in \{ V , N \}$ . For robustness check, we tried a wide range of parameter values and also tried quadratic form for the cost functions; the findings are robust to these variations except when noted. For illustration purposes, below we use

## Figure 7 (Color online) The Impact of k and $D _ { F } / D _ { S W }$ on Firm Security Under Serial Configuration

![](/api/attachments/MX6QREND/fulltext/images/dcb286abc6ff36863293f5610cf329c1117d963513f5e25e13248ef7d2e9146b.jpg)

(b) The impact of $D _ { F } / D _ { S W }$ on firm security (k = 0.1)  
![](/api/attachments/MX6QREND/fulltext/images/08f25e4faf6ea6285c5811d5ae1ff0332d4d4b80d16dfafcf57274cc97efaca7.jpg)

Figure 8 (Color online) The Impact of k and $D _ { F } / D _ { S W }$ on Firm Security Under Parallel Configuration  
(a) The impact of k on firm security $( D _ { F } = 2 \times 1 0 ^ { 4 } )$  
![](/api/attachments/MX6QREND/fulltext/images/045d8cc59cd13c61ec7ed242b6351ffe646d79e141baa9400b9b018b54d21500.jpg)

(b) The impact of $D _ { F } / D _ { S W }$ on firm security (k = 0.1)  
![](/api/attachments/MX6QREND/fulltext/images/9ef4c68d2f24146ce6826990fb632bfdfff55bafc391ab410787a8cfd4656843.jpg)

parameter values $W _ { S W } = 1 0 ^ { 5 }$ and $D _ { S W } = 4 \times 1 0 ^ { 4 }$ for the figures.

We first show the results regarding how k and $D _ { F } / D _ { S W }$ affect the firm security (given that the optimal standard set by the policy maker is higher than $\hat { s } _ { S C }$ or $\hat { s } _ { P C } )$ where the intuitions are easier to see. Figures 7 and 8 show the results for the serial and parallel configurations, respectively. Interestingly, the numerical results show that the overall firm security decreases in k and increases in $D _ { F } / D _ { S W }$ . This result is robust to the two security configurations, robust to a wide range of parameter values we tried, and robust to both the exponential and the quadratic cost functions that we considered. Note that this numerical finding regarding firm security is aligned with our analytical findings regarding social welfare in Propositions 5 and 6. Intuitively, when either k increases or $D _ { F } / D _ { S W }$ decreases, the firm’s moral hazard problem exacerbates and her incentive to invest in security decreases. The numerical results in Figures 7 and 8 show that, even though the policy maker is aware of the firm’s moral hazard problem on control N , she cannot completely remedy this moral hazard problem by standard setting because of the unverifiability of control N .

We next discuss the results regarding how k and $D _ { F } / D _ { S W }$ affect the optimal standard set by the policy maker, as illustrated by Figures 9 and 10 for the serial and parallel configurations, respectively. As illustrated by Figure 10, the numerical results show that, under the parallel configuration, the optimal standard decreases in k and increases in $D _ { F } / D _ { S W }$ . This result is robust to a wide range of parameter values we tried and robust to both the exponential and the quadratic cost functions that we considered. The results in Figure 10 are also aligned with the earlier results in Figure 8. Intuitively, under the parallel configuration, a higher standard implies a higher firm security as long as the standard is not too high (i.e., upper bounded by s¯; recall Proposition 4). It turns out, as the numerical results show, in equilibrium the policy maker will never set a standard higher than s¯. Therefore, the firm security is increasing in the optimal standard, which explains the similar trends in Figures 8 and 10.

The numerical results under the serial configuration (see Figure 9) paint a sharply different picture than those under the parallel configuration. First, the impact of k on the optimal standard depends critically on the magnitude of $D _ { F }$ : when $D _ { F }$ is large enough, the optimal standard $s _ { S C } ^ { * }$ is monotonically decreasing in $k ,$ as illustrated by the dashed line in the left plot in Figure 9; nevertheless, when $D _ { F }$ is small enough, the optimal standard $s _ { S C } ^ { * }$ increases in k when k is not too large, as illustrated by the solid line in the left plot in Figure 9. To understand why $D _ { F }$ plays a critical role here, first recall from Proposition 3 that s is an increasing function of $D _ { F }$ . Therefore, when $D _ { F }$ is small enough, e.g., $D _ { F } { = } 2 \times 1 0 ^ { 4 }$ , as for the solid line in the figure, s is small, and thus the range (for the standard) under which the firm security decreases in the standard is narrow. Consequently, the optimal standard is more likely to be out of this range, and therefore the firm security is more likely to increase in the standard. The solid line in the left plot in Figure 9 thus implies that, up to $k = 0 . 8$ , when k increases (and thus the moral hazard problem worsens), the policy maker should increase the mandatory standard to benefit the firm security. When $D _ { F }$ is large enough, e.g., $D _ { F } = 3 . 9 \times 1 0 ^ { 4 }$ as for the dashed line in the figure, s is now large, and thus the firm security is more likely to decrease in the standard. Therefore, reducing the standard will now benefit the firm security.

Figure 9 (Color online) The Impact of k and $D _ { F } / D _ { S W }$ on Optimal Standard Under Serial Configuration  
![](/api/attachments/MX6QREND/fulltext/images/d73dad5fa70d2daa9b15163cd355d62dbc8aafde596f05d045e9e7d4304b2a28.jpg)

The impact of $D _ { F } / D _ { S W }$ on optimal standard  
![](/api/attachments/MX6QREND/fulltext/images/84f34a618e8bececb41a13b1fba6e682d9cdc5aa10f244986ca1738dd4ee09e7.jpg)

Figure 10 (Color online) The Impact of k and $D _ { F } / D _ { s w }$ on Optimal Standard Under Parallel Configuration  
![](/api/attachments/MX6QREND/fulltext/images/a50be37a7fe18790419179132a75a513c2ba91f248b30662b042cfd44d4fd270.jpg)

![](/api/attachments/MX6QREND/fulltext/images/3288583ec4ab61f5dd05b563a281eb19ed99c72a0a43737ab5fd3af204a98984.jpg)

The right plot in Figure 9 shows that, under the serial configuration, the optimal standard decreases in the ratio $\bar { D _ { F } } / \bar { D } _ { S W } .$ . Intuitively, when $D _ { F } / D _ { S W }$ increases, the incentive of the firm is increasingly aligned with that of the policy maker. Consequently, by reducing the standard, although the policy maker will induce a lower direct investment on the verifiable control by the firm, she is increasingly likely to induce an indirect higher firm investment on the unverifiable control (recall the substitution effect under the serial configuration). The right plot in Figure 9 shows that the indirect effect dominates the direct effect under the serial configuration regardless of the value of k.

In summary, using a combination of analytical and numerical tools, we find that both the firm security and the social welfare (under the optimal standard set by the policy maker) are decreasing in the liability reduction factor k and increasing in the ratio of damages to the firm and to social welfare $D _ { F } / D _ { S W }$ . This result is robust to both security configurations and to the particular parameter values we tried. The impacts of k and $D _ { F } / D _ { S W }$ on the optimal standard, however, are dependent on the security configurations. The impact of k on the optimal standard also depends on the magnitude of $D _ { F }$

## 6. Extensions

We consider two model extensions. In the first extension, we consider a boundedly rational policy maker that naively ignores the unverifiable security control. In the second extension, we allow the liability reduction effect to be contingent on which security control is breached.

## 6.1. Consequences of the Policy Maker Ignoring the Verifiability Issue

An important message in our paper so far is that a policy maker needs to take unverifiable controls into consideration when setting standards on verifiable controls. In practice, however, anecdotal evidence suggests that policy makers do not always take such caution over unverifiable controls. In the HPS case, for example, attackers penetrated through “data in transit”—data that was moving in networks rather than stored in databases. During postbreach analysis, the chief executive officer of HPS “emphasized that the same method of attack focused on stealing data in transit had been applied many times prior to Heartland’s breach” (Cheney 2010, p. 4). The PCI Security Standards Council, nevertheless, neither warned merchants of this potential security vulnerability nor amended related PCI-DSS mandates before it hit HPS.

In this extension, we are interested in understanding the security and social welfare implications if the policy maker naively ignores the unverifiable control. To this end, we first introduce a benchmark model where a naïve policy maker ignores the unverifiable security control (and thus naively believes that control V is solely responsible for the firm security). We then compare the policy maker’s decision under this benchmark model with the one under our base model (which we refer to as the original model).

For convenience, define $\hat { s } ^ { B M }$ as the solution to $( 1 -$ $2 k \hat { s } ^ { B M } + k ) D _ { F } = c _ { V } ( \hat { s } ^ { B M } )$ . Under the benchmark model and for any standard $s ,$ because the naïve policy maker ignores the unverifiable security control, she incorrectly believes that the firm faces the following optimization problem:

$$
\max _ {e _ {V}} U _ {F} ^ {B M} = W _ {F} - (1 - e _ {V}) (1 - k e _ {V}) D _ {F} - C _ {V} (e _ {V}) \text {s.t.} e _ {V} \geq s.
$$

Consequently, the naïve policy maker incorrectly believes that the firm’s effort will be $\hat { e } _ { V } ^ { * } = \hat { s } ^ { B M } \mathrm { ~ i f ~ } s \stackrel { < } { \leq } \hat { s } ^ { B M }$ and $\hat { e } _ { V } ^ { * } = s \ \mathrm { i f } \ s > \hat { s } ^ { B M }$ . The policy maker’s optimization problem can then be framed as

$$
\max _ {s} U _ {S W} ^ {B M} = W _ {S W} - (1 - s) D _ {S W} - C _ {V} (s) \quad \text { s.t. } s \geq \hat {s} ^ {B M}.
$$

The solution to this benchmark problem, $\mathrm { i . e . , }$ the benchmark standard, is $s = s ^ { B M } \equiv \mathrm { m a x } \{ r _ { V } ( D _ { S W } ) , \hat { s } ^ { B M } \}$

We next compare the benchmark standard $s ^ { B M }$ with the original standard under the serial configuration $s _ { S C } ^ { * }$ and under the parallel configuration $s _ { P C } ^ { * } ,$ respectively.

<sup>Proposition</sup> <sup>7.</sup> Under serial configuration, $i f s _ { S C } ^ { * } > \hat { s } _ { S C } .$ the benchmark standard $s ^ { B M }$ is higher than the original standard $s _ { S C } ^ { * }$

<sup>Proposition</sup> <sup>8.</sup> Under parallel configuration, $i f s _ { P C } ^ { * } >$ ma $\langle \hat { s } _ { P C } , 1 / ( 2 k ) \}$ , the benchmark standard $s ^ { B M }$ is higher than the original standard $s _ { P C } ^ { * }$

Propositions 7 and 8 show that when the naïve policy maker ignores the unverifiable control, she may overshoot in setting the standard under both security configurations. To see the intuition, recall that a standard has a direct effect (on the verifiable control) and an indirect effect (on the unverifiable control). Regarding the direct effect, the naïve policy maker overestimates the marginal value of the standard on the verifiable control because she is not aware that the firm investment on the unverifiable control also helps prevent attacks. This direct-effect bias incentivizes her to overshoot in setting the standard. Regarding the indirect effect, first note that under the serial configuration (or under the parallel configuration with a high liability reduction factor $k > \tilde { 1 / } ( 2 s ) )$ , it is a substitution effect: a higher standard leads to a lower firm investment on control N $( { \bf i . e . } , d e _ { N } ^ { * } ( s ) / d s < 0 )$ . The naïve policy maker, nevertheless, does not account for this substitution effect while setting the standard. This indirect-effect bias also incentivizes her to overshoot in setting the standard.

There are two possible detrimental consequences when the policy maker sets a standard higher than what is optimal. One straightforward consequence is on the cost side: a higher-than-optimal standard forces a firm to overinvest on the verifiable security control. The other detrimental consequence is on the benefit side: a tighter standard does not always result in better firm security. This model extension thus contributes a unique angle to the understanding of why the continuous tightening of security standards in recent years has not led to a steady decline of security breaches.

## 6.2. Contingent Liability Reduction

In the base model we assumed that when a breach happens, the liability reduction effect always applies and at a constant level k regardless of which control is breached. In this extension we analyze the case where whether and how the liability reduction applies is contingent on the answers to two questions: First, which of the two security controls is breached? Second, can the court (or any authority with jurisdiction over liability) identify the breached control? We limit our discussion to the parallel configuration because, under the serial configuration, both controls have to be compromised for a breach to happen. Our analysis shows that the intuition of our prior analysis of the parallel configuration (see Proposition 4 and its following discussion) carries over in this extension.

Formally, when a breach happens under the parallel configuration, there are three possibilities: the verifiable control V is breached, the unverifiable control N is breached, or both are breached—they are represented by the three root branches in Figure 11, where the number on each branch is the probability of this branch. Following a breach, we assume that the court (or any authority with jurisdiction over liability) can identify the truth (i.e., which control is responsible for the breach) with probability $1 - \mu .$ . As shown in the HPS and the Hannaford Bros. cases, litigation following a breach can last for years, and courts often find it hard to identify the root cause of a breach. Therefore, we assume $1 - \mu < 1 , { \mathrm { i . e . , ~ } } \mu > 0 .$

Figure 11 (Color online) Contingent Liability Reduction  
![](/api/attachments/MX6QREND/fulltext/images/d25cff94af183780b047992e85c0fcb57282681055c7aa544df9a7a4620b01be.jpg)

We differentiate between three levels of liability reduction effects. If indeed the firm’s verifiable control V is breached and if the court is able to identify this truth (the thick solid lines in Figure 11), the fact that V is breached despite the firm’s confirmation with the security standard implies that the firm rightfully deserves liability reduction. We assume that under this case the firm receives the best liability reduction (i.e., $k = k _ { H } )$ . If the breach is solely because the unverifiable control N is compromised, and if the court is able to identify this truth (the dotted line in Figure 11), the firm receives no liability reduction $( \mathrm { i . e . , } k = \mathrm { \bar { 0 } } )$ . Regardless of which control is compromised, if the court is not able to identify the truth (the thin solid lines in Figure 11), the firm receives some, but not the best, liability reduction $( \mathrm { i } . \mathrm { e } . , k = k _ { 0 } ,$ where $0 < k _ { 0 } < k _ { { \scriptscriptstyle H } } ) .$ 15

For convenience, denote $\bar { \mu }$ as the unique solution to

$$
\frac {r _ {N} ((1 - \bar {\mu}) D _ {F})}{r _ {N} ^ {\prime} ((1 - \bar {\mu}) D _ {F}) (1 - \bar {\mu}) D _ {F}} = \frac {1}{1 - \bar {\mu}} - 2,
$$

$\bar { k } _ { 0 }$ as the unique solution to

$$
\frac {r _ {N} ((1 - \bar {k} _ {0} \mu) D _ {F})}{r _ {N} ^ {\prime} ((1 - \bar {k} _ {0} \mu) D _ {F}) (1 - \bar {k} _ {0} \mu) D _ {F}} = \frac {1}{1 - \bar {k} _ {0} \mu} - 2,
$$

and s¯ as the unique solution to

$$
\begin{array}{c} r _ {N} (\bar {s} ((1 - \mu) + \mu (1 - k _ {0} \bar {s}) D _ {F}) \\ \hline r _ {N} ^ {\prime} (\bar {s} ((1 - \mu) + \mu (1 - k _ {0} \bar {s})) D _ {F}) (\bar {s} ((1 - \mu) + \mu (1 - k _ {0} \bar {s})) D _ {F}) \\ = \frac {1}{1 - k _ {0} \mu \bar {s}} - 2. \end{array}
$$

The next proposition extends our base-model result, Proposition 4, to the extension with contingent liability reduction as depicted by Figure 6:

Proposition 9 (Contingent Liability Reduction). Under the parallel configuration and given a contingent liability reduction effect, a higher standard results in a lower firm security if and only if $\mu > \bar { \mu } , k _ { 0 } > \bar { k } _ { 0 } ,$ and $s _ { P C } > \operatorname* { m a x } \{ \hat { s } _ { P C } , \bar { s } , 1 / ( 2 k _ { 0 } \mu ) \}$

A comparison between Propositions 4 and 9 shows that the insight we got under the base model continues to hold under contingent liability reduction: a higher standard leads to a lower firm security only if the standard is high enough and the liability reduction effect is also high enough. Therefore, having the liability reduction effect contingent on which control being compromised and whether courts can find the truth out does not affect the key insight in our base model.

That said, a new observation in this extension is that Proposition 9 requires $\mu$ to be large enough $( \mu > \bar { \mu } )$ i.e., the chance that the court cannot pinpoint the culprit control for a security breach is high enough. Our Proposition 9 thus has an important implication: even if the parties involved in a breach attempt to investigate which control is responsible for the breach, and that ex post there is a chance (albeit not a sure one) that such an investigation can discover the truth, ex ante the firm may still choose to strategically and significantly reduce its effort on the unverifiable control if the firm believes that the ex post investigation cannot always reveal the truth.

## 7. Managerial Implications and Concluding Remarks

This paper is a first study on how security standards affect a firm’s security investments and its overall security when standards cannot cover all firm security controls. Key issues considered are security configurations (namely, how security controls together protect firm security), liability in security compliance, standard setting, and the consequences of ignoring the unverifiability issue by the policy maker. This research has a number of managerial implications that challenge common wisdom in security practice and regulation.

First, this research shows strikingly that a tighter security standard mandated by the government or trade unions can sometimes have the unintentional consequence of harming overall firm security. Intuitively, although a tight standard applies to all security controls that it regulates, it may lead a firm to strategically reduce its investment on security controls that are not explicitly regulated. We show that such an investment reduction on unverifiable security controls may overwhelm the incremental investment on verifiable security controls, thus leading to overall lower firm security. Remarkably, under the serial configuration, this result (that tighter standard hurts firm security) can take place even if there is no liability reduction effect. Under the parallel configuration, however, a strong liability reduction effect is necessary for this counterintuitive result.

Second, the conditions for tighter standards hurting firm security depend critically on the security configuration. Under the serial configuration, it can happen only if the standard is not too high. Under the parallel configuration, however, it can happen only if the standard is high enough.

Third, under the serial configuration we show that a firm that cares more about security (i.e., suffers a higher damage upon breach) may react to a tighter standard by reducing its overall security even when a firm that cares less does not. This result implies that when policy makers contemplate imposing tighter standards, they should not take it for granted that firms that care more about security will be more likely to respond by improving their overall security.

Fourth, when a policy maker is able to set an optimal standard that maximizes social welfare, we show that both firm security and social welfare are decreasing in the liability reduction factor and increasing in the ratio between the damages to the firm and to social welfare following a breach. This result suggests that although it is well-known that rewarding firms for standard compliance before a breach can incentivize firms to beef up security, rewarding firms for standard compliance after a breach—in the form of reduced liability—can harm social welfare.

Fifth, we show that if a policy maker ignores the unverifiability issue when setting the standard on the verifiable security control, she might overshoot— i.e., setting a standard higher than what is socially optimal. Overshooting a standard can have negative consequences on both the cost and benefit sides: it leads to inefficient security investments, and it may also result in security worse than the socially optimal level.

This first research on security regulation in the presence of unverifiable controls can be extended in a number of ways. First, in practice, security configurations can be more complicated than the two basic forms discussed in this paper, and can involve more than two controls. The question of whether a complicated security configuration can always be decomposed into the two basic forms is intriguing. Second, subject to data availability, our research offers a number of empirically testable results, such as the ones on how security configuration affects a firm’s investment on unverifiable controls. A follow-up empirical study will be valuable because there is limited research that empirically studies how security standards affect firm investment on security controls and attacker strategy.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2015.0607.

## Acknowledgments

This work was partially supported by the Natural Science Foundation of China [Grants 71490724, 71532004, and 71531013].

## References

August T, Tunca TI (2011) Who should be responsible for software security? A comparative analysis of liability policies in network environments. Inform. Systems Res. 19(1):48–70.

Battigalli P, Maggi G (2002) Rigidity, discretion, and the costs of writing contracts. Amer. Econom. Rev. 92(4):798–817.

Bernheim B, Whinston M (1998) Incomplete contracts and strategic ambiguity. Amer. Econom. Rev. 88(4):902–932.

Campbell K, Gordon L, Loeb M, Zhou L (2003) The economic cost of publicly announced information security breaches: Empirical evidence from the stock market. J. Comput. Security 11(3): 431–448.

Cavusoglu H, Mishra B, Raghunathan S (2004) The effect of Internet security breach announcements on shareholder wealth. Internat. J. Electronic Commerce 9(1):69–104.

Cavusoglu H, Raghunathan S, Cavusoglu H (2009) Configuration of and interaction between information security technologies: The case of firewalls and intrusion detection systems. Inform. Systems Res. 20(2):198–217.

Cheney J (2010) Heartland payment systems: Lessons learned from a data breach. White paper, Federal Reserve Bank of Philadelphia, Philadelphia. Accessed October 15, 2015, https:// www.phil.frb.org/consumer-credit-and-payments/paymentcards-center/publications/discussion-papers/2010/d-2010- january-heartland-payment-systems.pdf.

Coase RH (1937) The nature of the firm. Economica 4(16): 386–405.

Culnan M, Williams C (2009) How ethics can enhance organizational privacy: Lessons from the choicepoint and TJX data breaches. MIS Quart. 33(4):673–687.

Cusumano MA (2004) Who is liable for bugs and security flaws in software? Comm. ACM 47(3):25–27.

Dayton S (2014) Illinois Supreme Court reverses \$43 million verdict against Ford in automotive products-liability case. Accessed October 15, 2015, http://product-liability.weil.com/ uncategorized/illinois-supreme-court-reverses-43-million-verdict -against-ford-in-automotive-products-liability-case/.

Dye R (1993) Auditing standards, legal liability, and auditor wealth. J. Political Econom. 101(5):887–914.

Gordon LA, Loeb MP (2002) The economics of information security investment. ACM Trans. Inform. System Security 5(4): 438–457.

Gordon LA, Loeb M, Lucyshyn W (2003) Sharing information on computer systems security: An economic analysis. J. Accounting Public Policy 22(6):461–485.

Hausken K (2006a) Income, interdependence, and substitution effects affecting incentives for security investment. J. Accounting Public Policy 25(6):629–665.

Hausken K (2006b) Returns to information security investment: The effect of alternative information security breach functions on optimal investment and sensitivity to vulnerability. Inform. Systems Frontiers 8(5):338–349.

Hausken K (2007) Information sharing among firms and cyber attacks. J. Accounting Public Policy 26(6):639–688.

Hui KL, Hui W, Yue WT (2013) Information security outsourcing with system interdependency and mandatory security requirement. J. Management Inform. Systems 29(3):117–156.

Keblawi F, Sullivan D (2007) The case for flexible NIST security standards. Computer 40(6):19–26.

Kim BC, Chen P, Mukhopadhyay T (2011) The effect of liability and patch release on software security: The monopoly case. Production Oper. Management 20(4):603–617.

Krebs R (2009a) Hackers test limits of credit card security standards. Washington Post (April 16), voices.washingtonpost.com/ securityfix/2009/04/the\_number\_scale\_and\_sophistic.html.

Krebs R (2009b) Payment processor breach may be largest ever. Washington Post (January 20), voices.washingtonpost.com/securityfix/ 2009/01/payment\_processor\_breach\_may\_b.html.

Loch K, Carr H, Warkentin M (1992) Threats to information systems: Today’s reality, yesterday’s understanding. MIS Quart. 16(2): 173–186.

MacCarthy M (2010) Information security policy in the U.S. retail payments industry. Workshop Econom. Inform. Security, Cambridge, MA.

Miller A, Tucker C (2010) Encryption and data loss. Workshop Econom. Inform. Security, Cambridge, MA.

Morse E, Raval V (2008) PCI DSS: Payment card industry data security standards in context. Comput. Law Security Report 24(6):540–554.

National Institute of Standards and Technology (2010) Guide for assessing the security controls in federal information systems and organizations. Accessed January 22, 2016, http:// csrc.nist.gov/publications/nistpubs/800-53A-rev1/sp800-53A-rev1- final.pdf.

Navetta D (2009) PCI DSS incident response: The legal perspective. InfoLawGroup (July 8), http://www.infolawgroup.com/2009/07/ credit-cards/pci-dss-incident-response-the-legal-perspective/.

PCI Security Standards Council (2009) Payment card industry data security standard: Requirements and security assessment procedures, version 1.2.1. July 2009, https://www .pcisecuritystandards.org/documents/pci\_dss\_v1-2.pdf.

Romanosky S, Telang R, Acquisti A (2011) Do data breach disclosure laws reduce identity theft? J. Policy Anal. Management 30(2): 256–286.

Ross R (2007) Managing enterprise security risk with NIST standards. Computer 40(8):88–91.

Ryan DJ (2003) Two views on security software liability: Let the legal system decide. IEEE Security Privacy 1(1):70–72.

Schneier B (2008) Software makers should take responsibility. The Guardian (July 16), http://www.guardian.co.uk/technology/ 2008/jul/17/internet.security.

Schwartz R (1997) Legal regimes, audit quality and investment. Accounting Rev. 72(3):385–406.

Simon H (1981) The Sciences of the Artificial (MIT Press, Cambridge, MA).

Vijayan J (2010) Court gives preliminary OK to \$4M consumer settlement in Heartland case. ComputerWorld (May 7). http:// www.computerworld.com/s/article/9176431/.

Visa (2015) Compliance fines. Accessed January 2015, https://web .archive.org/web/20150607013755/http://usa.visa.com/merchants/ protect-your-business/cisp/index.jsp.

Whitman ME, Mattord HJ (2009) Management of Information Security (Thomson Course Technology, Boston).

Willekens M, Steele A, Miltz D (1996) Audit standards and auditor liability: A theoretical model. Accounting Bus. Res. 26(3):249–264.

Williamson OE (1975) Markets and Hierarchies: Analysts and Antitrust Implications (Free Press, New York).

WorldPay (2014) Financial protection. Accessed January 2014, https://web.archive.org/web/20140214094144/http://www .worldpay.us/pci-compliance.
