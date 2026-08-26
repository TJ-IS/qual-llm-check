---
otero_id: 16202
otero_key: "JT2HQD4F"
title: "Contracting Information Security in the Presence of Double Moral Hazard"
authors: "Chul Ho Lee; Xianjun Geng; Srinivasan Raghunathan"
year: "2013"
journal: "Information Systems Research"
doi: "10.1287/isre.1120.0447"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.122.253.212] On: 13 February 2015, At: 08:16 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/JT2HQD4F/fulltext/images/596ef484d9a05f63df58ceda749d32c75cc9a7a9fc29d7d480de2777daadfff2.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Contracting Information Security in the Presence of Double Moral Hazard

Chul Ho Lee, Xianjun Geng, Srinivasan Raghunathan,

## To cite this article:

Chul Ho Lee, Xianjun Geng, Srinivasan Raghunathan, (2013) Contracting Information Security in the Presence of Double Moral Hazard. Information Systems Research 24(2):295-311. http://dx.doi.org/10.1287/isre.1120.0447

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2013, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/JT2HQD4F/fulltext/images/88f9d60f8a5a950b366794a1af5f81b49abceba3e3342574c23164a97cd7fd6f.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Contracting Information Security in the Presence of Double Moral Hazard

Chul Ho Lee

Management Information Systems, Williams College of Business, Xavier University, Cincinnati, Ohio 45207, leec11@xavier.edu

Xianjun Geng

Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080, geng@utdallas.edu

Srinivasan Raghunathan

Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080, sraghu@utdallas.edu

n information security outsourcing, it is the norm that the outsourcing firms and the outsourcers (com-Imonly called managed security service providers, MSSPs) need to coordinate their efforts for better security. Nevertheless, efforts are often private and thus both firms and MSSPs can suffer from double moral hazard. Furthermore, the double moral hazard problem in security outsourcing is complicated by the existence of strong externality and the multiclient nature of MSSP services. In this prescriptive research, we first show that the prevailing contract structure in security outsourcing, bilateral refund contract, cannot solve double moral hazard. Adding breach-contingent sunk cost or external payment cannot solve double moral hazard either. Furthermore, positive externality can worsen double moral hazard. We then propose a new contract structure termed multilateral contract and show that it can solve double moral hazard and induce first-best efforts from all contractual parties when an MSSP serves two or more client firms, regardless of the externality. Firm-side externality significantly affects how payments flow under a multilateral contract when a security breach happens. When the number of client firms for an MSSP increases, we show that the contingent payments under multilateral contracts for any security breach scenario can be easily calculated using an additive method, and thus are computationally simple to implement.

Key words: information security outsourcing; managed security service providers; double moral hazard; externality

History: Ram Gopal, Senior Editor; Jan Stallaert, Associate Editor. This paper was received on November 15, 2010, and was with the authors 7 months for 3 revisions. Published online in Articles in Advance October 5, 2012.

We prefer to think of our (MSSP) service as a co-sourcing or co-managed offering.

—Kerry Bailey, VP of security services, Verizon Business Solutions

## 1. Introduction

The increasing complexity, regulatory requirements, and cost associated with managing information security has motivated many firms to outsource information security functions to managed security service providers (MSSPs). In a 2008 study by Information-Week, 38% of surveyed business technology professionals reported that their organizations are using or considering using MSSPs for their information security needs (George 2008). MSSP services are popular for security infrastructure functions such as spam protection, firewall/virtual private network management, and virus protection, where specialized and experienced MSSPs may provide expertise at a lower cost than their client firms (Schneier 2002, George 2008). Vulnerability assessment offered by MSSPs is also a popular security service as nowadays firms face increasingly complex governmental and industrial security compliance requirements (Mayne 2008).

It is, nevertheless, not cost effective (and sometimes privacy-wise sensitive or technologically infeasible) for a firm to outsource all its information security needs to MSSPs. Few firms outsource access rights management to MSSPs (Vanauken 2006, George 2008). Security forensics, which investigates security breaches after it happens, is also among the least outsourced security functions. A firm’s security outsourcing needs are also related to firm size—small firms may depend more on MSSPs for security needs than large firms would because of the former’s relative lack of in-house expertise (Mayne 2008). Lastly, breaches using social engineering (such as insider hacking or phishing) or through trusted partners cannot be addressed purely by outsourced technological services (Granger 2001, Hayes 2008).

Once security obligations are divided between a firm and its contracted MSSP, having both parties spend and coordinate effort is critical for success—after all, a chain is only as strong as its weakest link.<sup>1</sup> Unfortunately, given the secretive and complex nature of security functions, parties often cannot observe or verify each other’s effort. Furthermore, when security breaches happen, the liabilities often cannot be clearly attributed to only one contractual party. Consequently, a double moral hazard problem can sometimes arise and coordinated efforts are far from given (Cooper and Ross 1985, Al-Najjar 1997, Gupta and Romano 1998, Balachandran and Radhakrishnan 2005). Such double-sided failure in spending adequately on security efforts—the signature characteristic of double moral hazard—is well illustrated by a well-publicized security incident involving a payment card processing company, CardSystems Solutions, and its MSSP, Savvis Inc (Rothke and Mundhenk 2009, Zetter 2009). In June 2005, hackers breached CardSystems Solutions’ information systems and stole 40 million payment card numbers—the largest security breach at that time. Follow-up litigations faulted both parties: CardSystems Solutions is accused of not investing enough in information security, and Savvis is accused of not paying due diligence in providing vulnerability assessment and compliance service.

Double moral hazard is not unique to the information security outsourcing domain. In fact, there is a rich literature on double moral hazard in the economics and accounting literature. Nevertheless, information security domain offers several unique challenges, which have not been addressed by the prior literature. For example, previous studies have largely focused on bilateral contracting arrangements between a single firm and a service provider. In the information security context, however, a MSSP typically serves multiple firms. This allows the MSSP to be more effective in information sharing and more efficient from economy of scale. How the multiclient nature of MSSP industry affects double moral hazard remains understudied. Furthermore, the information security domain exhibits significant externalities, where one firm’s actions affect others. For example, effort spent on securing one firm may lead to broader improvement of security technologies and implementations that benefit other firms in the same group (Varian 2000, Anderson and Moore 2006), which is referred to as positive externality. On the other hand, increased security of one firm may also result in negative externality if this change causes attackers to strategically switch to targeting less-secure firms. To our knowledge, little research exists on how externality affects double moral hazard and its remedies.

In this paper we study double moral hazard and propose prescriptive remedies for the MSSP industry that is characterized by strong externalities and multiple client firms for each MSSP. Specifically, we analyze the following research questions. First, how does double moral hazard affect security performance under bilateral refund contracts? Second, can adding breachcontingent sunk cost or external payment help solve the double moral hazard problem? Third, can externality worsen double moral hazard under bilateral refund contracts? Fourth, is it possible to design better contracts to mitigate double moral hazard? Fifth, if such better contracts exist, how does externality affect the optimal contract structure? Sixth, for a given MSSP, will and how does the number of client firms affect optimal contract structure?

To answer the above research questions, we construct a game-theoretical model in which a single MSSP serves a finite number of firms. To highlight double moral hazard and its impact on firm and MSSP efforts, we posit that no party can observe efforts by others. We further posit that upon a security breach the liability cannot be clearly assigned to only one party, as evident in the real-life case of CardSystems Solutions and Savvis. We consider both positive and negative externalities, i.e., effort exerted by one firm for its own security can either positively or negatively affect the security of other firms. Similarly, effort exerted by the MSSP to protect one client firm may also affect the security of other client firms. To distinguish, we term the former firm-side externality and the latter MSSP-side externality. We start our analysis with bilateral refund contract, which in its simplest form consists of a fixed up-front payment from a firm to a MSSP and a contingent refund/penalty paid by the MSSP to the firm only if security breach happens to the firm. Bilateral refund contracts are popular in security outsourcing in the form of service level agreements (SLAs). For example, one of the largest MSSPs, IBM Internet Security Systems, offers SLAs to its security outsourcing clients with a \$50,000 money-back warranty each time a breach happens.

Although bilateral refund contracts can alleviate single-sided moral hazard in information technology (IT) outsourcing (Whang 1992, Dey et al. 2009, Sen et al. 2009), we show that they are ineffective against double moral hazard intrinsic to security outsourcing. This is consistent with findings in the double moral hazard literature in economics (e.g., Cooper and Ross

1985). The first new contribution of this research is that, even if breach-contingent sunk cost or external payment, in which the MSSP is penalized when a breach occurs but the breached firm is not the recipient of the penalty charged to the MSSP, is added to the bilateral refund contract, it still cannot solve the double moral hazard problem.

Our findings regarding the impact of externality on double moral hazard are also new to the literature. Using a linear model, we show that both positive firm-side externality and positive MSSP-side externality can worsen double moral hazard. This result signifies the importance of studying double moral hazard in the MSSP industry, where strong externality often exists on both firm and MSSP sides.

The ineffectiveness of bilateral refund contracts in solving double moral hazard motivated us to explore alternative and potentially better forms of incentive structures. In this paper we propose a new form of contract—termed multilateral contract—to cope with double moral hazard under externalities and multiple client firms. A multilateral contract differs from a bilateral refund contract in that the contingent ex post payment to a firm depends on other firms’ security status (thus the term “multilateral”).

We show that, in the case where externality does not exist, a simple modification to a bilateral refund contract can lead to the optimal multilateral contract: conditional on a firm being breached, instead of having the MSSP pay this firm the refund as in a bilateral refund contract, a multilateral contract requires the MSSP to pay the same amount of refund to another unbreached firm (or a basket of unbreached firms when there are more than two client firms). This seemingly surprising payment structure turns out to be able to induce socially optimal efforts from all contractual parties.

Note that a multilateral contract works only if the MSSP has more than one client firm—otherwise, there is no proper recipient of the MSSP’s payment upon a security breach. In fact, one MSSP serving multiple client firms is the norm in the security outsourcing industry. Previous research has cited direct cost saving (via cost complementarity) as a reason for this phenomenon (Rowe 2007, Cezar 2009). Our paper shows that having multiple client firms can also benefit security outsourcing from an incentive perspective: with two or more client firms, the MSSP can adopt multilateral contracts that eliminate efficiency loss because of double moral hazard.

When externality exists, simply redirecting refund from the breached firm to another unbreached firm is no longer sufficient to induce socially optimal efforts. Furthermore, firm-side and MSSP-side externalities impact the optimal multilateral contract in fundamentally different ways. We show that, under positive firm-side externality, a breached firm not only should not receive any refund from MSSP, but it needs to pay a further penalty out. On the other hand, under negative firm-side externality, the MSSP should send part of its payment to a breached firm. Compared to firm-side externality, MSSP-side externality only affects the magnitude of payments, yet not the directions they flow.

Our proposed multilateral contract can induce socially optimal efforts regardless of the number of client firms (except for one). For ease of exposition we carry out most analysis using the case of two client firms. We then show that our proposed multilateral contract can be easily scaled to cases with more than two firms. Despite the fact that the number of possible breach scenarios grows exponentially in the number of firms, we show that contingent payments under any breach scenario can be easily calculated using an additive method, and thus remain computationally simple to implement.

## 2. Literature Review

Our work is at the intersection of information systems and economics. On the information systems side, our work is related to IT contracting and especially IT security outsourcing. The contracting literature in the information systems area has focused primarily on outsourcing information systems development functions. One early study, Whang (1992), proposes a game-theoretic model to incorporate incentive and information issues and derives an optimal multiperiod software development contract. Subsequently, Richmond et al. (1992), Wang et al. (1997), and Chalos and Sung (1998) examine the conditions under which firms prefer outsourcing. Recently, Dey et al. (2010) and Sen et al. (2009) compare the performance of various software outsourcing contracts. The research mentioned above focuses on the single-sided moral hazard problem, whereas we consider double moral hazard. Our work also differs from most existing work on IT contracting in that we consider multiple principals.

The economics of IT security outsourcing has recently become an important issue in information security discipline. For instance, Ding and Yurcik (2005, 2006) and Ding et al. (2005) discuss incentive issues in performance-based contracts using analytical models and numerical simulation. Gal-Or and Ghose (2005) analyze information sharing alliances in terms of sharing security information. Cezar et al. (2010) examine firms’ IT security outsourcing decisions based on the nature of function outsourced. Rowe (2007) finds that firms can benefit from network effects by outsourcing to a same MSSP. Our research differs from the existing security outsourcing literature in that we consider both double moral hazard and externality. Specifically and in contrast to Rowe (2007), we offer an alternative explanation for why multiple firms can benefit from using a same MSSP: multiple firms make it possible to solve the double moral hazard problem using multilateral contracts.

Our work also adds to the literature on double moral hazard, which has received attention in diverse domains over the years—see, for example, Cooper and Ross (1985) in economics and Balachandran and Radhakrishnan (2005) in manufacturing. Cooper and Ross (1985) discuss double moral hazard in the context of product warranties, where a major finding is that bilateral contracts cannot lead to first-best outcomes. In contrast, we show that when multiple clients exist, multilateral contracts can induce firstbest outcomes. In addition, we study the impact of externality on double moral hazard and optimal multilateral contracts.

Balachandran and Radhakrishnan (2005) show that first-best quality can be achieved under double moral hazard if a supplier is not held responsible for a buyer’s defects or if a warranty contract is based on information from incoming inspection. Similarly, Corbett et al. (2005) show that a supplier in a supply chain can achieve first-best by transferring all variable costs to an agent if monitoring is feasible. In the IT development context, Jayanth et al. (2010) examine double moral hazard that arises in requirements assessment phase, and show that the effectiveness of the feedback from the client to the developer plays a critical role in the severity of the moral hazard problem. In contrast to the above papers, our solution for achieving first-best efforts does not depend on monitoring or inspection.

In particular, our work is related to a small number of papers on double moral hazard with multiple agents (Bhattacharyya and Lafontaine 1995, Al-Najjar 1997, Gupta and Romano 1998). Bhattacharyya and Lafontaine (1995) propose revenue sharing contracts between a principal and multiple agents. Al-Najjar (1997) further proposes incentive contracts based on team outcome and argues that it performs better than contracts in Bhattacharyya and Lafontaine (1995) under multiple agents. Unlike our proposed multilateral contract, contracts proposed in the above two papers cannot induce first-best outcomes under a finite number of agents. Gupta and Romano (1998) is closely related to our paper in that they also identify ways to induce first-best solutions in the context of two agents. Our paper differs from Gupta and Romano (1998) in two important ways. First, Gupta and Romano’s (1998) approach depends on a bounded feasible output set for any given efforts (whereas we do not), thus it cannot be applied to modeling security outsourcing.<sup>2</sup> Second, Gupta and Romano (1998) do not consider externality, which is recognized as an important element in IT security (Varian 2000, Anderson and Moore 2006). We next present our game-theoretical model.

## 3. The Model

The model consists of one MSSP and N homogenous firms, where N is a positive integer larger than one. We discuss the case of N = 2 in the main body of this paper. Results for the case of $N > 2$ are qualitatively similar to the ones under $N = 2 ,$ and will be discussed in §6.

The MSSP offers contracted security services to the firms. Security services are broadly classified into two categories: preventive services and detective/corrective services (Straub and Welke 1998). In practice, vendors providing prevention services are more prevalent than those that provide detective and corrective services (Vanauken 2006). In this paper we focus on preventive service contracts, where the goal is to reduce the chance of security breaches. Formally in our model and for firm i (i = 11 2), let P <sup>i</sup> represent the chance of not having a security breach after the contract is implemented. Throughout this paper we use superscript to index firms.

The objective of the contract between firm $i ~ ( i =$ 11 2) and the MSSP is to improve $P ^ { i }$ . In practice investments on various security controls, such as patching, firewalls, and access control, can influence $P ^ { i }$ . For ease of exposition, we refer to the totality of investments the MSSP incurs to protect firm i “the MSSP’s effort for firm $i , \prime \prime$ as $e _ { M } ^ { i }$ . Similarly, we refer to the totality of investments firm i incurs (in addition to the MSSP’s investments) to protect itself “firm $i ^ { \prime } \mathrm { s }$ effort,” as $e _ { F } ^ { i } .$ For notational convenience, let E represent the set of all efforts, i.e., $E = ( e _ { F } ^ { 1 } , e _ { F } ^ { 2 } , e _ { M } ^ { 1 } , e _ { M } ^ { 2 } )$ . Each player’s effort is its private information.

If security breach does not take place on a firm during the contractual period, this firm operates regularly and obtains a constant nonnegative utility $V .$ Alternatively, if this firm is hit by a security breach, we use d to denote the totality of damages this firm suffers. Let damages include opportunity costs—what the firm would have normally gained should the security breach not take place.<sup>3</sup>

Externality. We refer to $\partial P ^ { i } ( E ) / \partial e _ { F } ^ { j }$ as firm-side externality, and ${ \partial P ^ { i } ( E ) } / { \partial e _ { M } ^ { j } }$ as MSSP-side externality, $i , j \in$ 811 29 and $i \neq j$ . For either firm- or MSSP-side externality, we consider three cases. First is no firmside (or MSSP-side) externality, i.e., $\partial P ^ { i } ( E ) / \partial e _ { F } ^ { j } = 0$ (or $\partial P ^ { i } ( E ) / \partial e _ { M } ^ { j } = 0 )$ . Second is positive firm-side (or MSSPside) externality, $\mathrm { i . e . , } \partial P ^ { i } ( E ) / \partial e _ { F } ^ { j } > 0 ( \mathrm { o r } \partial P ^ { i } ( E ) / \partial e _ { M } ^ { j } > 0 )$ One example of positive MSSP-side externality is when the MSSP learns from attacks against one of its customers and uses that knowledge to better protect other customers (Ding et al. 2005). Third is negative firm-side (or MSSP-side) externality, i.e., $\partial P ^ { i } ( E ) / \partial \bar { e } _ { F } ^ { j } < 0$ (or $\partial P ^ { i } ( E ) / \partial e _ { M } ^ { j } < 0 )$ . One example is when attackers strategically pick weak targets: with stronger security protections over one firm, attackers may shift their attention to other firms with relatively lower level of security.

Efforts upon a firm (either by the firm itself or by the MSSP) primarily address this firm’s own security, and externality—if it exists—plays a secondary role in security contracting. As such, we assume $\partial P ^ { i } ( E ) / \partial e _ { F } ^ { i } > | \partial \bar { P } ^ { j } ( E ) / \partial e _ { F } ^ { i } | , \partial \check { P } ^ { i } ( E ) / \partial e _ { M } ^ { i } >$ $| \partial P ^ { j } ( E ) / \partial e _ { M } ^ { i } | , ~ | \partial ^ { 2 } P ^ { i } ( E ) / \partial ( e _ { F } ^ { i } ) ^ { 2 } | ~ > ~ | \partial ^ { 2 } \bar { P ^ { j } } ( E ) / \partial ( e _ { F } ^ { i } ) ^ { 2 } |$ and $| \partial ^ { 2 } P ^ { i } ( E ) / \partial ( \stackrel { i } { e _ { M } ^ { i } } ) ^ { 2 } | > | \partial ^ { 2 } P ^ { j } ( E ) / \partial ( \stackrel { i } { e _ { M } ^ { i } } ) ^ { 2 } |$

We make the stylized assumption on convex cost structures and concave impacts, as follows (see, for example, Gordon and Loeb 2002). For $i \in \{ 1 , 2 \}$ and when effort increases, the prevention probability increases yet at a nonincreasing rate: $\partial P ^ { i } ( \bar { E } ) / \partial e _ { M } ^ { i } \geq \bar { 0 } ,$ $\partial P ^ { i } ( E ) / \partial e _ { F } ^ { i } \geq 0 , \ \partial ^ { 2 } P ^ { i } ( E ) / \partial ( e _ { M } ^ { i } ) ^ { 2 } \leq 0 ,$ and $\partial ^ { 2 } P ^ { i } ( E ) / \partial ( e _ { F } ^ { i } ) ^ { 2 }$ $\leq 0 .$ . Moreover, the cost of effort, $C _ { F } ( e _ { F } ^ { i } ) .$ , is convex with $C _ { F } ^ { \prime } ( e _ { F } ^ { i } ) \ge 0 , \ C _ { F } ^ { \prime } ( 0 ) = 0$ and $C _ { F } ^ { \prime \prime } ( e _ { F } ^ { i } ) > 0$ . Similarly, the cost function of the MSSP, $C _ { M } ( e _ { M } ^ { i } , e _ { M } ^ { j } )$ , satisfies $\partial C _ { M } ( e _ { M } ^ { i } , e _ { M } ^ { J } ) / \partial e _ { M } ^ { i } \geq 0 , \partial C _ { M } ( e _ { M } ^ { i } , e _ { M } ^ { J } ) / \partial e _ { M } ^ { i } | _ { ( e _ { M } ^ { i } , e _ { M } ^ { j } ) = ( 0 , 0 ) } = 0 ,$ and $\partial ^ { 2 } C _ { M } ( e _ { M } ^ { i } , e _ { M } ^ { j } ) / \partial ( e _ { M } ^ { i } ) ^ { 2 } > 0 , i , j \in \{ 1 , 2 \}$ and $i \neq j$

Observability of security breach events. In this paper we focus on cases where breach events are public information among the MSSP and the firms. Breaches can be observable by all contractual parties for a variety of legal, social, and economic reasons. Nowadays firms in the vast majority of the United States—46 states as of October 12, 2010—are legally required to disclose security breaches involving personal information.<sup>4</sup> For breaches that lead to service disruptions to internal employees and external customers, social word-of-mouth can spread breach information. We also emphasize an economic reason for a firm to disclose its breach to its MSSP: often, a firm suffers continuous loss of data and is vulnerable to further compromise of its digital assets until the root cause of a breach is identified and properly dealt with. Therefore, timely disclosure of a breach to its MSSP is in the interest of a firm when the value of promptly patching the breach and limiting the damage outweighs any gains the firm may obtain by hiding the breach.<sup>5</sup>

Table 1 Bilateral Refund Contracts in Practice

<table><tr><td>Security service provider</td><td>Penalty clause</td></tr><tr><td>IBM Managed Security Systems Verizon</td><td>(Refund) credit dependent on incident priority levels.(Refund) credit is either fixed or contingent on the extent of damage depending on security service type.</td></tr><tr><td>Counterpane Internet Security</td><td>(Refund) credit varies and can be up to 100% of fees paid.</td></tr></table>

Sources. http://www-935.ibm.com/services/us/iss/pdf/z125-8466.pdf, http:// www.verizonbusi-ness.com/terms/us/products/security/intrusion/, http://www .ecommerce-journal.com/node/255.

Bilateral refund contract and multilateral contract. We primarily analyze two types of contracts: bilateral refund contract and multilateral contract. A bilateral refund contract between the MSSP and firm i $( i = 1 , 2 )$ consists of two payments: a fixed payment $f ^ { i }$ from the firm to the MSSP upon signing the security contract and a refund $d \phi ^ { i }$ from the MSSP to the firm if it suffers from security breaches.

We study bilateral refund contracts for two reasons. First, bilateral refund contracts are popularly adopted in security practice. For instance, Table 1 shows a sample of security contracts offered by leading security providers, all of which closely resemble a bilateral refund contract. Second, bilateral refund contracts are widely studied in the service contracting literature (Bhattacharyya and Lafontaine 1995, Kim and Wang 1998), including the information security contracting literature (Ding and Yurcik 2005, 2006; Ding et al. 2005; Fenn et al. 2002; Goo 2010; Liu et al. 2001).

Despite its popularity, in §4 we will show that a bilateral refund contract is not effective in addressing the double moral hazard problem (DMH problem for abbreviation). We therefore will propose an alternative type of contract: multilateral contract. A multilateral contract is a pair-wise contract between the MSSP and firm $\ ( i = 1 , 2 )$ consisting of two components: an ex ante fixed payment $f ^ { i }$ from the firm to the MSSP and an ex post contingent payment between these two parties. We use the term “multilateral” to highlight that the ex post contingent payment in this new contract between the MSSP and firm i depends not only on firm $i ^ { \prime } \mathrm { s }$ own security status, but also on that of other firms. In the case of two client firms, there are four possible security outcomes and thus four contingent payment possibilities $( \phi _ { n n } ^ { i } , \phi _ { b n } ^ { i } , \phi _ { n b } ^ { i } , \phi _ { b b } ^ { i } )$ —where $\phi _ { n n } ^ { i }$ is normalized to zero—in a multilateral contract between the MSSP and firm $i ( i = 1 , 2 )$ , as explained in Table 2. For notational convenience, we use $\Phi ^ { i }$ to represent the set of contingent refunds, i.e., $\Phi ^ { i } = $ $( \bar { \phi _ { b n } ^ { i } } , \phi _ { n b } ^ { i } , \phi _ { b b } ^ { i } )$ for $i = 1 , 2 .$ . We will show in $\ S 5$ that this new type of contract can solve the DMH problem conditional on the MSSP having two or more client firms.

Table 2 Contingent Refund Possibilities Under a Multilateral Contract $( i , j \in \{ 1 , 2 \} , i \neq j )$

<table><tr><td>Security outcomes</td><td>No firm is breached</td><td>Only firm i is breached</td><td>Only firm j is breached</td><td>Both firms i and j are breached</td></tr><tr><td>Payment from the MSSP to firm i</td><td>0</td><td> $d\phi_{bn}^{i}$ </td><td> $d\phi_{nb}^{i}$ </td><td> $d\phi_{bb}^{i}$ </td></tr></table>

A principal-agent model. As illustrated by Table $^ { 1 , }$ in practice it is often the MSSP who takes the initiative in proposing the structure and refund level of a contract to potential client firms.<sup>6</sup> Accordingly, we use the following principal-agent setup (where the MSSP is the principal) to capture the dynamics of this model, as shown in Figure 1. In stage 1, the MSSP acts as the Stackelberg leader in offering a bilateral contract $( f ^ { i } , \phi ^ { i } )$ (or a multilateral contract $( f ^ { i } , \Phi ^ { i } ) )$ to firm i $( i = 1 , 2 )$ , in which $f ^ { i }$ is a fixed payment from firm i to the MSSP upon signing of the contract, and $\phi ^ { i }$ (or ê<sup>i</sup>5 is the refund schedule or contingent payment schedule depending on security outcomes. In stage 2, firm i can accept or reject the contract offer.<sup>7</sup> If firm i rejects the offer, the game between this firm and the MSSP ends, firm i obtains an outside-option utility $\underline { { { U } } } _ { F } ,$ and the MSSP obtains an outside-option utility $\underline { { U } } _ { M }$ plus the utility from serving the other firm.<sup>8</sup> In stage 3 and conditional on contract acceptance, each player chooses its effort $e _ { F } ^ { i }$ or $e _ { M } ^ { i } , i \in \{ 1 , \stackrel { . } { 2 } \}$ 1 to maximize its own expected utility given the agreed contract terms. Security outcomes are realized thereafter, and refunds or contingent payments are accordingly paid.<sup>9</sup>

Throughout our paper, both the MSSP and the firms are assumed to be self-interested risk-neutral agents. We carry out our analysis in the next three sections.

## 4. Externality and Double Moral Hazard Under Bilateral Refund Contracts

In this section we study bilateral refund contracts. As a benchmark, we start by characterizing the socially optimal (i.e., first-best) outcome. Throughout this section and unless otherwise noted, we assume $N = 2 ,$ i.e., there are two client firms. The equilibrium concept we use is subgame Perfect Nash Equilibrium (Fudenberg and Tirole 1998, p. 69).

## 4.1. First-Best Benchmark

In this subsection we characterize the socially optimal benchmark, under which the expected social welfare—the summation of the expected payoffs of the MSSP and the two firms—is maximized. Given all efforts $E ,$ this expected social welfare is

$$
\begin{array}{c} S W (E) = 2 V - \big ((1 - P ^ {1} (E)) + (1 - P ^ {2} (E)) \big) d - C _ {F} (e _ {F} ^ {1}) \\ - C _ {F} (e _ {F} ^ {2}) - C _ {M} (e _ {M} ^ {1}, e _ {M} ^ {2}). \end{array} \tag {1}\tag{1}
$$

Therefore, first-best efforts satisfy

$$
E ^ {*} = \underset {E} {\arg \max} S W (E).\tag{2}
$$

Specifically, for $i , j = 1$ 1 2 and $i \neq j ,$ the first-best effort of firm $i , \stackrel { \cdot } { e } _ { F } ^ { i * }$ , satisfies

$$
\bigg (\frac {\partial P ^ {i} (E)}{\partial e _ {F} ^ {i}} + \frac {\partial P ^ {j} (E)}{\partial e _ {F} ^ {i}} \bigg) d - C _ {F} ^ {\prime} (e _ {F} ^ {i}) = 0.\tag{3}
$$

The first-best effort of the MSSP for firm $i , e _ { M } ^ { i * }$ , satisfies

$$
\bigg (\frac {\partial P ^ {i} (E)}{\partial e _ {M} ^ {i}} + \frac {\partial P ^ {j} (E)}{\partial e _ {M} ^ {i}} \bigg) d - \frac {\partial C _ {M} (e _ {M} ^ {i} , e _ {M} ^ {j})}{\partial e _ {M} ^ {i}} = 0.\tag{4}
$$

Hereafter we refer to $E ^ { * } = ( e _ { F } ^ { 1 * } , e _ { F } ^ { 2 * } , e _ { M } ^ { 1 * } , e _ { M } ^ { 2 * } )$ as firstbest security efforts, or FBS efforts in short. It is straightforward that $E ^ { * }$ is unique under the convex cost structure. We call the social welfare under FBS efforts, denoted by $S W ^ { * } \equiv S W ( E ^ { * } )$ , the first-best outcome.

The above analysis applies to the case of $N = 2 .$ In general, for any $N \geq 1 { \bar { } }$ , let $E _ { N } ^ { * }$ denote the FBS efforts and $S W _ { N } ^ { * }$ denote the first-best outcome. We provide an analysis of FBS efforts under any N in the Extension section. To be consistent with earlier notations, we may suppress subscripts from $E _ { N } ^ { * }$ and SW<sup>∗</sup> when $N = 2$ . We also define $S W _ { 0 } ^ { * } = 0 .$ . In this paper we make the following assumption regarding SW <sup>∗</sup><sub>N</sub> :

Assumption 1. <sub>For</sub> <sub>any</sub> $N \geq 1 , S W _ { N } ^ { * } > S W _ { N - 1 } ^ { * } +$ $\underline { { U } } _ { F } + \underline { { U } } _ { M }$

Assumption 1 says that, conditional on FBS efforts, having a firm outsource its security to the MSSP creates more overall value (as compared to no security outsourcing) regardless of the size of the MSSP’s current client pool. Therefore, in this paper we limit our analysis to the case where, if all involved parties are properly incentivized, the services an MSSP offers are socially beneficial.

Figure 1 Timing of the Principal-Agent Model  
![](/api/attachments/JT2HQD4F/fulltext/images/39eb11969c12ae0b7bb31e9c523b06386488e5b4e30cddf8220d7142dc6ef215.jpg)

## 4.2. Double Moral Hazard Under Bilateral Refund Contracts

When the MSSP and the firms aim to maximize their own respective payoffs instead of the social welfare, their incentives may not be aligned. In this subsection we characterize equilibrium efforts under bilateral refund contracts, and prove that they can never match FBS efforts. We also analyze equilibrium refund levels under bilateral refund contracts.

Under bilateral refund contracts $( f ^ { i } , \phi ^ { i } ) , i = 1 , 2 ,$ firm i’s expected payoff is

$$
\begin{array}{r l} & U _ {F} ^ {i} (E) = V - f ^ {i} - (1 - P ^ {i} (E)) d \\ & \qquad + (1 - P ^ {i} (E)) \phi^ {i} d - C _ {F} (e _ {F} ^ {i}). \end{array}\tag{5}
$$

The MSSP’s expected payoff is

$$
\begin{array}{c} U _ {M} (E) = f ^ {i} + f ^ {j} - (1 - P ^ {i} (E)) \phi^ {i} d - (1 - P ^ {j} (E)) \phi^ {j} d \\ - C _ {M} (e _ {M} ^ {i}, e _ {M} ^ {j}), \end{array}\tag{6}
$$

where $i , j \in \{ 1 , 2 \} , i \neq j$ . We call the principal-agent problem under bilateral refund contracts Problem $R ,$ as shown below. Note that Problem R consists of two pair-wise bilateral refund contracts: $( f ^ { 1 } , \phi ^ { 1 } )$ between the MSSP and firm 1, and $( f ^ { 2 } , \phi ^ { 2 } )$ between the MSSP and firm 2.

<sup>Problem</sup> R. Optimal bilateral refund contracts between self-interested players.

$$
\max _ {f ^ {1}, f ^ {2}, \phi^ {1}, \phi^ {2}} U _ {M} (\hat {e} _ {F} ^ {1}, \hat {e} _ {F} ^ {2}, \hat {e} _ {M} ^ {1}, \hat {e} _ {M} ^ {2})\tag{7}
$$

subject to $\hat { e } _ { F } ^ { i }$ ∈ arg max $U _ { F } ^ { i } ( e _ { F } ^ { i } , \hat { e } _ { F } ^ { j } , \hat { e } _ { M } ^ { i } , \hat { e } _ { M } ^ { j } )$

(8)

$$
(\hat {e} _ {M} ^ {1}, \hat {e} _ {M} ^ {2}) \in \underset {(e _ {M} ^ {1}, e _ {M} ^ {2})} {\arg \max} U _ {M} (e _ {M} ^ {1}, e _ {M} ^ {2}, \hat {e} _ {F} ^ {1}, \hat {e} _ {F} ^ {2})\tag{9}
$$

$$
\begin{array}{l} \text {IR constraints for the firms and} \\ \text {the MSSP.} \end{array}\tag{10}
$$

For any given pair of contracts $( f ^ { 1 } , \phi ^ { 1 } )$ and $( f ^ { 2 } , \phi ^ { 2 } )$ that the players agreed upon exiting stage $2 , \hat { e } _ { F } ^ { i }$ represents firm i’s subgame-perfect equilibrium effort in stage 3 and is decided by its incentive compatibility (IC) constraint (8), i = 11 2. Similarly, $( \hat { e } _ { M } ^ { 1 } , \hat { e } _ { M } ^ { 2 } )$ represent the MSSP’s subgame-perfect equilibrium efforts and are decided by its IC constraint (9). For notational convenience, let $\hat { E } = ( \hat { e } _ { F } ^ { 1 } , \hat { e } _ { F } ^ { 2 } , \hat { e } _ { M } ^ { 1 } , \hat { e } _ { M } ^ { 2 } )$ denote the set of these subgame-perfect equilibrium efforts in stage 3. Note that all efforts and payoffs are functions of the parameters of the contracts $( { \dot { f } } ^ { 1 } , \phi ^ { 1 } )$ and $( f ^ { 2 } , \phi ^ { 2 } )$ as apparent from expressions (5) and (6); we omit them in the above expressions for succinctness of expression.

Equation (10) is a placeholder for all possible individual rationality (IR) constraints for each firm and the MSSP. For ease of exposition of Problem R, we assume for this section only that all these IR constraints are satisfied. This model simplification does not affect the generality of our analysis: our goal in this subsection is to show that bilateral refund contracts cannot lead to the first-best outcome; if we can prove this result without the IR constraints, it will apparently be true with the IR constraints.

Equation (7) represents the MSSP’s optimal contract offer in stage 1 given subgame-perfect equilibrium efforts.

We first analyze player efforts in stage 3 under any given contracts. Given contracts $( f ^ { 1 } , \breve { \phi ^ { 1 } } )$ and $( f ^ { 2 } , \phi ^ { \bar { 2 } } )$ and (8), the individually optimal effort for firm $i , \ : \hat { e } _ { F } ^ { i } ,$ satisfies

$$
\frac {\partial P ^ {i} (E)}{\partial e _ {F} ^ {i}} (1 - \phi^ {i}) d - C _ {F} ^ {\prime} (e _ {F} ^ {i}) = 0.\tag{11}
$$

Given $( f ^ { 1 } , \phi ^ { 1 } ) , ( f ^ { 2 } , \phi ^ { 2 } )$ , and (9), the individually optimal effort of the MSSP for firm $i , \hat { e } _ { M } ^ { i } ,$ satisfies

$$
\frac {\partial P ^ {i} (E)}{\partial e _ {M} ^ {i}} \phi^ {i} d + \frac {\partial P ^ {j} (E)}{\partial e _ {M} ^ {i}} \phi^ {j} d - \frac {\partial C _ {M} (e _ {M} ^ {i} , e _ {M} ^ {j})}{\partial e _ {M} ^ {i}} = 0.\tag{12}
$$

Equations (11) and (12) together decide player efforts under any given bilateral refund contracts. It is straightforward to verify that second-order conditions hold. Note that these efforts do not depend on the fixed payments. Therefore we can write these efforts as functions of the refund schedules, i.e., $\hat { e } _ { F } ^ { i } ( \phi ^ { i } , \phi ^ { j } )$ and $\hat { e } _ { M } ^ { i } ( \phi ^ { i } , \phi ^ { j } )$ for $i = 1 , 2$ . In other words, $\hat { E } =$ $\hat { E } ( \phi ^ { 1 } , \ddot { \phi } ^ { 2 } )$ . Hereafter we call the equilibrium efforts by the MSSP and the firms under any bilateral refund contract, $\mathrm { i . e . , } \hat { E } ( \phi ^ { 1 } , \phi ^ { 2 } )$ , second-best security effort functions, or SBS effort functions in short. The following lemma shows that SBS efforts, under any given bilateral refund contracts, will never equal to FBS efforts.

<sup>Lemma</sup> <sup>1.</sup> Bilateral refund contracts never lead to FBS efforts. Furthermore, a firm’s (the MSSP’s) effort decreases (increases) in refund level.

All proofs are in Appendix A in the online supplement. Note that, though we used the case of two firms to prove Lemma 1, it is straightforward to show that this result regarding refund contracts applies to any number of firms.

Lemma 1 is consistent with previous research on DMH (starting from Cooper and Ross 1985). Because a refund is a monetary transfer from one contractual party to another, it serves dual and opposite incentive roles: it punishes the sender and at the same time inevitably rewards the receiver. For example, consider the simple case without externality: reducing the refund level to zero can completely solve the moral hazard problem on firm side as evident from comparing (3) and (11), yet at the same time worsens it on MSSP side; similarly, increasing the refund level to one can completely solve the moral hazard problem on MSSP side as evident from comparing (4) to (12), yet at the same time worsens it on firm side. It is thus impossible to solve both parties’ moral hazard problems under bilateral refund contracts at the same time.

Using backward induction, we next discuss the MSSP’s contract offer in stage 1. Given $\hat { E } ( \phi ^ { 1 } , \phi ^ { 2 } )$ , the MSSP chooses $( f ^ { 1 } , \phi ^ { 1 } )$ and $( f ^ { 2 } , \phi ^ { 2 } )$ to maximize its expected utility $\bar { U } _ { M } ( f ^ { 1 } , f ^ { 2 } , \phi ^ { 1 } , \phi ^ { 2 } , \hat { E } ( \phi ^ { 1 } , \phi ^ { 2 } ) )$

<sup>Lemma</sup> <sup>2.</sup> The MSSP’s optimal bilateral refund contracts $( \hat { f } ^ { 1 } , \hat { \phi } ^ { 1 } )$ and $( \hat { f } ^ { 2 } , \hat { \phi } ^ { 2 } )$ satisfy

$$
\begin{array}{l} (\hat {\phi} ^ {1}, \hat {\phi} ^ {2}) = \underset {(\phi^ {1}, \phi^ {2})} {\arg \max} \left\{U _ {M} (f ^ {1}, f ^ {2}, \phi^ {1}, \phi^ {2}, \hat {E} (\phi^ {1}, \phi^ {2})) \right. \\ \quad + U _ {F} ^ {1} (f ^ {1}, f ^ {2}, \phi^ {1}, \phi^ {2}, \hat {E} (\phi^ {1}, \phi^ {2})) \\ \quad + U _ {F} ^ {2} (f ^ {1}, f ^ {2}, \phi^ {1}, \phi^ {2}, \hat {E} (\phi^ {1}, \phi^ {2})) \}. \end{array} \tag {1}\tag{13}
$$

Lemma 2 reveals an important insight regarding MSSP behavior: in stage 1 the values of $\phi ^ { \mathrm { i } }$ and $\phi ^ { \breve { 2 } }$ chosen by the MSSP (to maximize its own profits) are such that no other values of $\phi ^ { 1 }$ and $\phi ^ { 2 }$ can result in a higher value of the total payoffs of all players conditional on function $\hat { \hat { E } } ( \phi ^ { 1 } , \phi ^ { 2 } ) . ^ { 1 0 ^ { \cdot } 1 1 }$ This surprising result regarding MSSP behavior in stage 1 is due to the fact that a refund contract has two components: an ex post refund and an ex ante fixed payment. It is the ex ante fixed payment that aligns the incentive of the self-interested MSSP with total-payoff maximization at stage 1. Intuitively, suppose the MSSP chooses $( \phi ^ { 1 } , \phi ^ { 2 } ) \breve { \neq } ( \hat { \phi } ^ { 1 } , \hat { \phi } ^ { 2 } )$

Then, by switching to $( \hat { \phi } ^ { 1 } , \hat { \phi } ^ { 2 } )$ , the MSSP can induce higher total payoffs conditional on $\hat { E } ( \phi ^ { 1 } , \phi ^ { 2 } )$ . Note that the MSSP can induce any arbitrary sharing of the total payoffs among all players by altering the ex ante fixed payments $f ^ { 1 }$ and ${ \bar { \ f } } ^ { 2 } ,$ and thus the right choice of these fixed payments can result in a higher payoff for every player under $( \hat { \phi } ^ { 1 } , \hat { \phi } ^ { 2 } )$ than that under $( \phi ^ { 1 } , \phi ^ { 2 } )$ . Hereafter we refer to the total payoffs under any bilateral refund contracts with $( \hat { \phi } ^ { 1 } , \hat { \phi } ^ { 2 } )$ the secondbest outcome.

## 4.3. Generalized Bilateral Refund Contracts with Sunk Cost or External Payment

In this subsection only we consider a variation of the bilateral refund contract that seemingly breaks the dual role that a refund serves: for $i = 1 , \bar { 2 } ,$ , consider a generalized bilateral refund contract—generalized contract in short— $- ( f ^ { i } , \phi ^ { i } , \mu ^ { i } )$ between the MSSP and firm $i ,$ where $f ^ { i }$ and $\phi ^ { i }$ are as defined before. This new contract differs in that, if the firm suffers from security breaches during the contractual period, the MSSP not only sends a refund $\phi ^ { i } d$ to firm i, but also suffers an additional penalty $\mu ^ { i } d$ that is either a sunk cost or a payment to an external entity other than the firms. Examples of sunk costs after a breach include litigation costs and reputation loss.<sup>12</sup> Examples of payments to external entities include governmental fines and donations to a charity.<sup>13</sup> We use subscript G to differentiate this generalized contract from the one discussed in the last subsection. For ease of exposition, we limit our discussion in this subsection to the case without externality.<sup>14</sup> To analyze this generalized contract, we need to differentiate between two cases based on whether $\mu ^ { i } d$ is still counted as a part of the social welfare SW.

<sup>Proposition</sup> <sup>1.</sup> Generalized bilateral refund contracts with sunk cost or external payment never lead to FBS efforts.

Proposition 1 says unambiguously that adding a sunk cost or external payment component to bilateral refund contracts cannot resolve the DMH problem. The intuition is most easily seen when $\mu ^ { i } d$ is included in the measure of social welfare (SW). This fits the scenario where $\mu ^ { i } d$ is a payment to an external entity and this entity’s utility is included in the social welfare.

In this case, let $U _ { t h i r d }$ denote the expected utility of this third party, we then have $S W _ { G } ( E _ { G } ^ { ^ { \bullet } } ) = U _ { M G } + \bar { U _ { F G } ^ { 1 } } +$ $U _ { F G } ^ { 2 } + U _ { t h i r d }$ . However, Lemma 2 says that in stage 1 the self-interested MSSP will only propose contracts that maximize the total expected utility of the two firms and itself, i.e., $U _ { M G } + \bar { U } _ { F G } ^ { 1 } + U _ { F G } ^ { 2 }$ , which does not equal to the social welfare. Therefore the MSSP does not have incentive to induce FBS efforts.

When $\mu ^ { i } d$ is excluded from the measure of social welfare SW, the intuition involves an “moving firstbest target” observation.<sup>15</sup> Now the expected social welfare is changed from Equation (1) to

$$
\begin{array}{l} S W _ {G} (E _ {G}) \\ = 2 V - (1 - P ^ {1} (E _ {G})) (1 + \mu^ {1}) d - (1 - P ^ {2} (E _ {G})) \\ \quad \cdot (1 + \mu^ {2}) d - C _ {F} (e _ {F G} ^ {1}) - C _ {F} (e _ {F G} ^ {2}) - C _ {M} (e _ {M G} ^ {1}, e _ {M G} ^ {2}). \end{array}\tag{14}
$$

This fits the scenario where $\mu ^ { i } d$ represents a reputation loss, or a payment to an external entity whereas this entity’s utility is not counted as part of the social welfare. From (14) and given no externality, FBS efforts satisfy $( \partial \dot { P ^ { i } } ( E _ { G } ) / \partial \stackrel { \smile } { e _ { F G } } ) \cdot ( 1 + \mu ^ { i } ) d - C _ { F } ^ { \prime } ( \stackrel { \smile } { e _ { F G } ^ { i } } ) = 0$ and $( \partial P ^ { i } ( E _ { G } ) / \partial e _ { M G } ^ { i } ) ( 1 + \mu ^ { i } ) d - \partial C _ { M } ( e _ { M G } ^ { i } , e _ { M G } ^ { j } ) / \nonumber$ $\partial e _ { M G } ^ { i } = 0$ whereas both involves $\mu ^ { i } . \ i , j = 1 , 2$ and $i \neq j$ . In other words, FBS efforts in stage 3 are functions of the additional penalties $( \mu ^ { 1 } , \mu ^ { 2 } )$ because excluding $\mu ^ { i } d$ from the measure of social welfare SW alters the first-best benchmark—and thus resulting in a moving first-best target—in expression (14). Now the FBS efforts for all players will be accordingly adjusted higher as compared to the case without such additional penalty at any given refund level. To match such augmented FBS efforts, the generalized contracts will need to impose a total penalty upon the MSSP that is steeper than just $\mu ^ { i } d \cdot$ —the exact number turns out to be $\mu ^ { \hat { i } } d + d .$ . Consequently, no matter how much reputation loss the MSSP suffers (or external payments the MSSP gives that do not count in the social welfare) following security breaches, it still needs to pay a refund equaling to d to the breached firm in order to induce FBS efforts on itself. This refund $d ,$ nevertheless, induces a firm to exert less effort than the FBS one.

We next turn out attention to the impact of externality on the DMH problem.

## 4.4. The Impact of Externality on Double Moral Hazard: A Linear Model

As we discussed in the Introduction, externality plays a critical role in IT security contracting. We are interested in two questions related to externality. First, is it possible for externality to exacerbate the DMH problem and to increase the gap between FBS and SBS efforts under bilateral refund contracts? Second, what forms of contracts, if any, can induce FBS efforts in the security market even when externality exists? We address the first question in this subsection and the second one in §5; we offer affirmative answers to both questions. In this subsection only, we focus on a linear model in which prevention probability is a linear combination of effort levels, i.e.,

$$
P ^ {i} = a e _ {F} ^ {i} + b e _ {M} ^ {i} + \lambda_ {F} e _ {F} ^ {j} + \lambda_ {M} e _ {M} ^ {j},
$$

where $a$ and $b$ are positive constants; $\lambda _ { F }$ and $\lambda _ { M }$ are constants.<sup>16</sup> We use $\lambda _ { F }$ to measure firm-side externality and $\lambda _ { M }$ to measure MSSP-side externality. Cost functions are assumed to be quadratic, i.e., $\check { C _ { F } } ( e _ { F } ^ { i } ) = \alpha ( e _ { F } ^ { i } ) ^ { 2 }$ and $C ^ { M } ( e _ { M i } , e _ { M j } ) = \beta ( e _ { M } ^ { i } ) ^ { \hat { 2 } } + \beta ( e _ { M } ^ { j } ) ^ { 2 } .$ , where  and $\beta$ are positive constants. We assume that firm-side externality, $\lambda _ { F } ,$ is upper bounded by $\alpha ( b + \lambda _ { M } ) ^ { 2 } / ( \beta a )$ so that optimal refund is nonnegative.

Under this linear model and given a symmetric refund contract $( f , \phi )$ for both firms, from (11) we know that the individually optimal effort for firm $i ,$ $\hat { e } _ { F } ^ { i } ,$ is $\hat { e } _ { F } ^ { i } = a d ( 1 - \phi ) / ( 2 \alpha )$ . From (12) we know that the individually optimal effort of the MSSP, ${ \hat { e } } _ { M } ^ { i } ,$ is $\hat { e } _ { M } ^ { i } = $ $( b + \lambda _ { M } ) \phi \dot { d } / ( 2 \dot { \beta } )$ . Equilibrium refund level $\phi$ should maximize total profit $U _ { M } + U _ { F } ^ { 1 } + U _ { F } ^ { 2 }$ subject to these effort levels.

<sup>Lemma</sup> <sup>3.</sup> In the linear model, the equilibrium refund level is

$$
\phi^ {*} = (\alpha (b + \lambda_ {M}) ^ {2} - a \beta \lambda_ {F}) / (\alpha (b + \lambda_ {M}) ^ {2} - a ^ {2} \beta).
$$

We are now ready to characterize the impacts of externality on the DMH problem and optimal player strategies. First is the relationship between externality, optimal refund, and efforts:

<sup>Proposition</sup> <sup>2.</sup> In the linear model, when firm-side externality increases, refund level  decreases, firm effort increases, and MSSP effort decreases; when MSSP-side externality increases, refund level $\phi$ increases, firm effort decreases, and MSSP effort increases.

The relationship between externality and optimal refund is illustrated in Figure 2, where parameter values are as follows: $a = \bar { 0 . 3 } , b = 0 . 3 , \alpha = 0 . 4 , \beta = 0 . 4 ,$ $\lambda _ { F } = 0 ( \mathrm { o r } \lambda _ { M } = 0 ) V = 4 , d = 2 0 , f = 1 0 0 .$ . Firmside and MSSP-side externalities have opposite effects on the optimal refund level. Intuitively, when firmside externality increases, the marginal benefit of a firm’s effort on the other firm increases, which in turn implies that the marginal impact of a firm’s effort on total profit increases. Reducing the refund level in this case helps alleviate the moral hazard problem on firm side and induce firms to exert more effort. On the other hand, when MSSP-side externality increases, it is optimal to increase the refund level (i.e., taking more money away from the MSSP) in order to induce the MSSP to exert more effort.

Figure 2 The Impacts of Externalities on Refund Level

<table><tr><td>As externality from firm becomes more positive</td><td>As externality from MSSP becomes more positive</td></tr><tr><td></td><td></td></tr></table>

Next we study how externality affects the DMH problem. The DMH problem leads contractual parties to exert efforts less than the FBS efforts. First note that, from (3) and (4), the FBS efforts for the linear model are $e _ { F } ^ { i * } = d ( a + \lambda _ { F } ) / ( 2 \alpha )$ and $e _ { M } ^ { i \ast } = d ( b + \lambda _ { M } ) / ( 2 \beta )$ . The next proposition shows how much less effort a party exerts under different externalities.

<sup>Proposition</sup> <sup>3.</sup> In the linear model,

(a) when firm-side externality increases, the gap between FBS effort and SBS effort for either a firm or the MSSP increases;

(b) when MSSP-side externality increases, the gap between FBS effort and SBS effort for a firm increases, and the gap between FBS effort and SBS effort for the MSSP increases if and only i $^ { c } \lambda _ { M } \in ( - a \sqrt { \beta / \alpha } - b , a \sqrt { \beta / \alpha } - b )$

Proposition 3(a) shows that positive externality can worsen the DMH problem by increasing the gap between FBS and SBS efforts of all players. Intuitively, when firm-side externality becomes increasingly positive, Proposition 2 says that refund level will decrease, and thus the MSSP will exert lesser effort than socially optimal (and thus the larger gap). The intuition behind increasing gap between FBS and SBS efforts for a firm is less obvious: on one hand, a lower refund level incentivizes the firm to exert a higher SBS effort; on the other hand, the firm’s FBS effort should also be higher because of a higher firmside externality. Proposition 3(a) says that, when firmside externality increases, a firm’s SBS effort always increases at a lesser rate than its FBS effort. This is because the FBS effort $e _ { F } ^ { i * }$ internalizes the externality and therefore is increasing in $\lambda _ { F } ,$ yet the individual firm does not fully internalize the externality.

The intuition behind MSSP-side externality in Proposition 3(b) is analogous to the above. Nevertheless, now the MSSP’s SBS effort increases at a lesser rate than its FBS effort only when the MSSP-side externality is neither too positive nor too negative (i.e., $\lambda _ { M } \in ( - a \sqrt { \beta / \alpha } - b , a \sqrt { \beta / \alpha } - b ) )$ . Intuitively, the MSSP and firms differ in how they internalize the externality: as noted before, a firm does not directly internalize the externality (it only indirectly does it through $\phi ^ { * } )$ when choosing its effort; in contrast, the MSSP, whose total payoff is affected by the security status of both firms, does internalize the externality directly.

We next study whether the DMH problem can be solved under a new contract structure.

## 5. Using Multilateral Contracts to Solve the Double Moral Hazard Problem

In this section we analyze an alternative contract structure—multilateral contract—and show that it can induce FBS efforts from all players when there are multiple client firms. Externalities will affect optimal design of multilateral contracts. We limit our attention to the case of two firms and delegate other cases— which are qualitatively analogous to the case of two firms—to §6.

Recall that a multilateral contract between the MSSP and firm i (i = 11 2) is a pair-wise contract that consists of two components: an ex ante fixed payment $f ^ { i }$ from the firm to the MSSP and an ex post contingent payment between these two parties. The contingent payment depends not only on the security status of firm $i ,$ but also on the security status of the other firm as illustrated in Figure 3, where there are four possible security breach scenarios. We limit our attention to symmetric multilateral contracts, which as we show in this section will be sufficient to induce FBS efforts.

Figure 3 Multilateral Contracts Under Positive or Negative Externalit

<table><tr><td>Security breach in both firms</td><td>Security breach in firm F1</td><td>Security breach in firm F2</td><td>No security breach</td></tr><tr><td rowspan="2"><img src="/api/attachments/JT2HQD4F/fulltext/images/4ea43a6d5ff6b0eeb4daff33fe713584ce4da3f9e588ae9c146107353c982ba4.jpg"/></td><td rowspan="2"><img src="/api/attachments/JT2HQD4F/fulltext/images/ac19b8f6ffdb7040c609078ea74d69d5e58c2ca53db908f762d38274dff628cf.jpg"/></td><td rowspan="2"><img src="/api/attachments/JT2HQD4F/fulltext/images/f7561d176dbbefb688d04b4db120f230e6fb49f7f3fbe0bf390574221b595a6a.jpg"/></td><td>M</td></tr><tr><td>F1 F2</td></tr></table>

For $i = 1 , 2 ,$ , the contingent payment from the MSSP to firm i can take four possible values: $d \phi _ { b b }$ when both firms are breached; $d \phi _ { b n }$ when only firm i is breached; $d \phi _ { n b }$ when only firm $~ j ~ ( j \neq i )$ is breached; and $d \phi _ { n n }$ when neither firm is breached. A positive contingent payment means money goes from the MSSP to the firm; a negative contingent payment means the reverse. Without loss of generality, we normalize $\phi _ { n n }$ to zero. Let ê represent the set of contingent refunds, i.e., $\Phi = ( \phi _ { b n } , \phi _ { n b } , \phi _ { b b } )$

Under multilateral contracts, all ex post contingent payments are among the firms and the MSSP, therefore the first-best benchmark remains the same as the one in §4.1, and FBS efforts are determined by Equations (3) and (4).

Given multilateral contract 4f 1 ê5 for every firm, firm i’s expected payoff is

$$
\begin{array}{r l} U _ {F} ^ {i} (E) & = V - f - (1 - P ^ {i} (E)) d + (1 - P ^ {i} (E)) P ^ {j} (E) \phi_ {b n} d \\ & \quad + P ^ {i} (E) (1 - P ^ {j} (E)) \phi_ {n b} d + (1 - P ^ {i} (E)) \\ & \cdot (1 - P ^ {j} (E)) \phi_ {b b} d - C _ {F} (e _ {F} ^ {i}). \end{array} \tag {15}
$$

The MSSP’s expected payoff is

$$
\begin{array}{r l} U _ {M} (E) & = 2 f - (1 - P ^ {i} (E)) P ^ {j} (E) (\phi_ {b n} + \phi_ {n b}) d \\ & \quad - P ^ {i} (E) (1 - P ^ {j} (E)) (\phi_ {n b} + \phi_ {b n}) d - (1 - P ^ {i} (E)) \\ & \quad \cdot (1 - P ^ {j} (E)) 2 \phi_ {b b} d - C _ {M} (e _ {M} ^ {i}, e _ {M} ^ {j}), \end{array} \tag {16}
$$

where $i , j \in \{ 1 , 2 \} , i \neq j$ . We call the principal-agent problem under multilateral contracts Problem M, as shown below. We use header “˜” to denote equilibrium results under multilateral contracts. All IC constraints are similar between Problem M and Problem R (see §4.2). Problem $M ,$ however, differs from Problem R in three aspects. First, firm and MSSP payoff functions are now represented by Equations (15) and (16), respectively. Second, the optimization problem in expression (17) now use variables 4f 1 ê5 instead of $\stackrel { \cdot } { ( { f } ^ { 1 } , { f } ^ { 2 } , { \phi } ^ { 1 } , \stackrel { \cdot } { \phi ^ { 2 } } ) }$ 5. Third, we now explicitly model IR constraints for firm and MSSP in (20) and (21), respectively.<sup>17</sup>

<sup>Problem</sup> M. Optimal multilateral contracts between self-interested players.

$$
\max _ {f, \Phi} U _ {M} (\tilde {e} _ {F} ^ {1}, \tilde {e} _ {F} ^ {2}, \tilde {e} _ {M} ^ {1}, \tilde {e} _ {M} ^ {2})\tag{17}
$$

subject to $\tilde { e } _ { F } ^ { i } \in$ arg max $U _ { F } ^ { i } ( e _ { F } ^ { i } , \tilde { e } _ { F } ^ { j } , \tilde { e } _ { M } ^ { i } , \tilde { e } _ { M } ^ { j } )$

$$
i = 1, 2 \text { and } i \neq j\tag{18}
$$

$$
(\tilde {e} _ {M} ^ {1}, \tilde {e} _ {M} ^ {2}) \in \underset {(e _ {M} ^ {1}, e _ {M} ^ {2})} {\arg \max} U _ {M} (e _ {M} ^ {1}, e _ {M} ^ {2}, \tilde {e} _ {F} ^ {1}, \tilde {e} _ {F} ^ {2})\tag{19}
$$

$$
\begin{array}{c} U _ {F} ^ {i} (\tilde {e} _ {F} ^ {i}, \tilde {e} _ {F} ^ {j}, \tilde {e} _ {M} ^ {i}, \tilde {e} _ {M} ^ {j}) \geq \underline {{U}} _ {F}, \\ i = 1, 2 \text { and } i \neq j \\ U _ {M} (\tilde {e} _ {F} ^ {i}, \tilde {e} _ {F} ^ {j}, \tilde {e} _ {M} ^ {i}, \tilde {e} _ {M} ^ {j}) \geq 2 \underline {{U}} _ {M}, \\ i = 1, 2 \text { and } i \neq j. \end{array}\tag{20}
$$

(21)

Note that all payoffs and efforts are functions of the parameters of the contracts $( f , \Phi )$ as apparent from payoff expressions (15) and (16); we omit them in the above expressions for succinctness of expression. Let $\tilde { E } = ( \tilde { e } _ { F } ^ { 1 } , \overleftarrow { \tilde { e } } _ { F } ^ { 2 } , \tilde { e } _ { M } ^ { 1 } , \tilde { e } _ { M } ^ { 2 } )$ denote the set of subgameperfect equilibrium efforts in stage 3 for any given multilateral contracts. Constraints (18) and (19) in Problem M determine ${ \tilde { E } } ,$ thus $\tilde { E }$ can be written as a function of the contingent payments agreed by all players before entering stage 3, i.e., $\tilde { E } = \tilde { E } ( \Phi )$ . Conditional on $\tilde { E } ( \Phi )$ and all IR constraints holding, the MSSP will propose a multilateral contract $( f , \Phi )$ to each firm that maximizes the MSSP’s own expected utility $U _ { M } ( f , \Phi , \tilde { E } ( \Phi ) )$ .

<sup>Lemma</sup> <sup>4.</sup> The MSSP’s optimal multilateral contract $( \tilde { f } , \tilde { \Phi } )$ to each firm satisfies

$$
\begin{array}{r l} & {\tilde {\Phi} = \underset {\Phi} {\arg \max} \big \{U _ {M} (f, \Phi , \tilde {E} (\Phi))} \\ & {\qquad + U _ {F} ^ {1} (f, \Phi , \tilde {E} (\Phi)) + U _ {F} ^ {2} (f, \Phi , \tilde {E} (\Phi)) \big \}.} \end{array}\tag{22}
$$

Figure 4 Multilateral Contract Under No Externality

<table><tr><td>Security breach in both firms</td><td>Security breach in one firm</td><td>Security breach in one firm</td><td>No security breach</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

The insight behind Lemma 4 is analogous to the one behind Lemma 2. The fixed payment component in a multilateral contract enables the MSSP to propose any arbitrary sharing of expected surplus. Consequently, the self-interested MSSP has incentive to propose a Pareto-dominant contingent payment plan in stage 1 such that the total expected payoffs of all firms and itself can be maximized conditional on equilibrium effort functions E4ê5 <sup>˜</sup> in stage 3. Lemma 4 thus simplifies our analysis in stage 1 as we only need to consider Pareto-dominant contingent payment plans.

## 5.1. Optimal Multilateral Contracts Under No Externality

We first discuss the simpler case of no externality. Recall that a key insight regarding the ineffectiveness of bilateral refund contracts in solving the DMH problem is that a refund is both a punishment and a reward. A higher refund rewards breached firms and punishes the MSSP more when security breach occurs, and thus induces firms to exert less effort (than socially optimal); similarly, a lower refund induces the MSSP to exert less effort. Our proposed multilateral contract aims to remove the reward role that a refund plays. Denote $\Phi _ { N E } ^ { * } = ( \phi _ { b n } = 0 , \phi _ { n b } = 1 _ { \mathrm { . } }$ $\phi _ { b b } = 1 )$ , i.e., this is a contingent payment plan under which the MSSP rewards a firm with amount d only if the other firm is breached. Subscript $\mathbf { \Omega } ^ { \prime \prime } \mathbf { N } \mathbf { E } ^ { \prime \prime }$ stands for no externality. Figure 4 illustrates $\Phi _ { N E } ^ { * }$ ${ \cal U } _ { F } ^ { i } ( f , \Phi _ { N E } ^ { * } , \tilde { E } ( \Phi _ { N E } ^ { * } ) )$ then represents firm i’s expected payoff given stage 3 equilibrium effort functions $\tilde { E } ( \cdot )$ and stage 1 contingent payment plan $\Phi _ { N E } ^ { * }$ . Let $\bar { U } _ { F N E } \equiv$ $U _ { F } ^ { i } ( 0 , \Phi _ { N E } ^ { * } , \tilde { E } ( \Phi _ { N E } ^ { * } ) )$ denote a firm’s expected payoff under $\Phi _ { N E } ^ { * }$ and if the MSSP does not charge any ex ante fixed payment.

<sup>Proposition</sup> <sup>4.</sup> Under no externality, in stage 1 the self-interested MSSP will propose the following multilateral contract to firm $i , i = { \dot { 1 } } , { \dot { 2 } }$

• a fixed payment $f _ { N E } ^ { * } \equiv \bar { U } _ { F N E } - \underline { { U } } _ { F }$ from firm i to the MSSP upon signing the security contract,<sup>18</sup>

• and contingent payment plan $\Phi _ { N E } ^ { * } ~ ( i . e . , f i r m ~ i$ receives ex post payment d only if the other firm is breached).

In stage 2, firm i accepts the contract offer. This multilateral contract induces FBS efforts E<sup>∗</sup> from all players in stage 3.

The optimal multilateral contract $( f _ { N E } ^ { * } , \Phi _ { N E } ^ { * } )$ under no externality differs sharply from a refund contract in that a firm does not receive a refund when security breach happens only to itself, as illustrated in Figure 4. Instead, when only one firm is breached, refund goes to the firm that remains secure—which on the surface seems surprising. Intuitively, such a contract punishes both contractual parties when breach happens: the breached firm suffers from the breach itself and from not receiving a refund for the breach, and the MSSP suffers from the refund paid to the other secure firm. When this bilateral penalty is severe enough (i.e., at an amount of d), it solves the moral hazard problems on both sides of the contract, thus leading to FBS efforts from all players.

One important observation from Proposition 4 is that a multilateral contract applies only when the MSSP has at least two client firms: the firm receiving a payment needs to be different from the firm suffering a security breach. Prior research on MSSP has offered a number of explanations on why it is beneficial for an MSSP to recruit multiple client firms (Rowe 2007, Cezar 2009). Our research offers one new explanation on why having multiple client firms for the same MSSP can be beneficial: when the MSSP and firms have misaligned incentives, multilateral contracts upon multiple clients can solve the DMH problem that stems from incentive misalignment.

## 5.2. Optimal Multilateral Contracts Under Positive or Negative Externality

When externality exists, simply redirecting refund from a breached firm to another firm is no longer sufficient in inducing FBS efforts from all players. The next proposition shows the optimal multilateral contracts under externality. For convenience, denote $\Phi ^ { * } =$ $( \phi _ { b n } ^ { * } , \phi _ { n b } ^ { * } , \phi _ { b b } ^ { * } )$ , where $\phi _ { b b } ^ { * } = 1$

$$
\phi_ {b n} ^ {*} = - 2 \frac {\partial P ^ {j} (E) / \partial e _ {F} ^ {i}}{\partial P ^ {i} (E) / \partial e _ {F} ^ {i} - \partial P ^ {j} (E) / \partial e _ {F} ^ {i}} \bigg | _ {E = E ^ {*}}, \quad \mathrm{and}
$$

$$
\phi_ {n b} ^ {*} = \frac {\partial P ^ {i} (E) / \partial e _ {F} ^ {i} + \partial P ^ {j} (E) / \partial e _ {F} ^ {i}}{\partial P ^ {i} (E) / \partial e _ {F} ^ {i} - \partial P ^ {j} (E) / \partial e _ {F} ^ {i}} \bigg | _ {E = E ^ {*}}.
$$

Let $\bar { U } _ { F } \equiv U _ { F } ^ { i } ( 0 , \Phi ^ { * } , \tilde { E } ( \Phi ^ { * } ) )$ denote a firm’s expected payoff under $\Phi ^ { * }$ and if the MSSP does not charge any ex ante fixed payment.

<sup>Proposition</sup> <sup>5.</sup> When externality exists, the optimal multilateral contract between the MSSP and firm $i ~ ( i =$ 11 2) consists of a fixed payment $f ^ { * } \equiv \bar { U } _ { F } - U _ { F }$ from firm i to the MSSP upon signing the security contract and contingent payment plan $\Phi ^ { * }$

This multilateral contract induces FBS efforts from all players.

Proposition 5 has a number of implications. First, compared to the case without externality, a major impact of externality on the optimal multilateral contract is the introduction of contingent payment $\phi _ { b n } ^ { * }$ between firm i and the MSSP when security breach happens to only firm i. To which direction this contingent payment flows depends only on firm-side externality, as we summarize next:

<sup>Corollary</sup> <sup>1.</sup> If firm-side externality is positive, under the optimal multilateral contract firm $i ( i = 1 , 2 )$ pays a contingent payment of $d | \phi _ { b n } ^ { * } |$ to the MSSP if firm i is the only breached firm. If firm-side externality is negative, this contingent payment flows in the reverse direction. The MSSP-side externality does not have any impact on the direction of the payment flow.

Corollary 1 is straightforward by examining the sign of $\phi _ { b n } ^ { * }$ in Proposition 5. Contingent payments in the optimal multilateral contract under all security breach scenarios are illustrated in Figure 5, where 5(a)/5(b) is under positive/negative firm-side externality.

The contingent payment from firm i to the MSSP when only firm i is breached and when firm-side externality is positive seems surprising as it adds insult to injury: firm i already suffers from the breach itself, and the optimal contract calls for an additional penalty of $\lceil d \rceil \phi _ { b n } ^ { * } \rceil$ on this firm. Intuitively and everything else remaining unchanged, when firm-side externality is positive, the marginal return from firmside effort (and thus the optimal FBS firm effort) is higher compared to the case without externality. However, the firms do not account for this externality while maximizing their own utility. Therefore, by punishing firm i more via $d | \phi _ { b n } ^ { * } |$ when breach happens to this firm only, the optimal multilateral contract can induce firm i to try to reduce the chance of facing such a severe damage by investing more in its effort (compared to its optimal effort under no externality). The magnitude of optimal $d | \phi _ { b n } ^ { * } |$ ensures that firm i’s increased effort exactly matches the FBS effort under positive firm-side externality.

A second implication of Proposition 5 is related to the MSSP’s compensation and how the multilateral contract leads to FBS effort from the MSSP. Recall that a key reason that a bilateral refund contract cannot induce FBS efforts from all players is that a refund is both a penalty to the party that pays (which leads to higher effort) and a reward to the party that receives it (which leads to a lower effort). Under positive firmside externality, the MSSP is the recipient of payment $d | \phi _ { b n } ^ { * } |$ when only firm i is breached, which by itself disincentivizes the MSSP from exerting effort. To account for this payment to the MSSP, the optimal multilateral contract calls for an equal amount of payment from the MSSP to the other unbreached firm on top of d that the MSSP would have paid under no externality:

$$
\phi_ {n b} ^ {*} d = d + (- \phi_ {b n} ^ {*} d).\tag{23}
$$

<sup>Corollary</sup> <sup>2.</sup> Under multilateral contracts, externality does not affect the MSSP’s total payment to firms for any security breach scenario.

Figure 5(a) Optimal Multilateral Contracts Under Positive Firm-Side Externality

<table><tr><td>Security breach in both firms</td><td>Security breach in firm 1 only</td><td>Security breach in firm 2 only</td><td>No security breach</td></tr><tr><td><img src="/api/attachments/JT2HQD4F/fulltext/images/bcbcb6bee44c9eeaeaee8ce5472e58a4880d532b38cf4f1530320c6d5e3c0f89.jpg"/></td><td></td><td></td><td></td></tr></table>

Figure 5(b) Optimal Multilateral Contracts Under Negative Firm-Side Externality

<table><tr><td>Security breach in both firms</td><td>Security breach in firm 1 only</td><td>Security breach in firm 2 only</td><td>No security breach</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

Corollary 2 follows from Equation (23) and the fact that the MSSP’s total payment to firms when both firms are breached or neither is breached is the same as the ones in Proposition 4. Corollary 2 says that the optimal multilateral contract controls firm effort and MSSP effort through different mechanisms. The contract directly affects firm effort by imposing additional penalty (refund) when breach happens and when firm-side externality is positive (negative). In contrast, the contract does not directly alter the MSSP’s payoff under various externality scenarios. Instead, the multilateral contract changes the self-interested MSSP’s profit maximizing problem to a problem of maximizing social welfare conditional on firms putting in FBS efforts. This is easily seen by plugging contingent payments in Proposition 5 into the MSSP’s expected payoff function (recall Equation (16)): for $i , j \in \{ 1 , 2 \} , i \not = j$

$$
U _ {M} (\Phi^ {*}) = 2 f - ((1 - P ^ {i} (E)) + (1 - P ^ {j} (E))) d - C _ {M} (e _ {M} ^ {i}, e _ {M} ^ {j}).
$$

Taking first-order condition with respect to $e _ { M } ^ { i } ,$ we get the same condition for optimal $e _ { M } ^ { i }$ as the one in Equation (4) when we analyzed social optimum conditional on firms putting in FBS efforts. Therefore, to account for externality, we only need to adjust the optimal contract to change the payoff structure for the firms, as FBS effort from the firms will then induce FBS effort from the MSSP even if the MSSP’s payoff structure remains the same regardless of externality. After all, it is the firms, and not the MSSP, that fail to account for the externality while they maximize their own utility.

A third implication of Proposition 5 is that the existence of multiple client firms for the same MSSP plays a critical role in enabling multilateral contracts. When a security breach happens to firm i in the case of positive firm-side externality, the MSSP is punished by amount $d ,$ and firm i is punished by amount $d | \phi _ { b n } ^ { * } \mathbf { \bar { | } }$ For these penalties to be effective, it is critical that neither of these two payments goes back to these two parties. Instead, it is necessary to have a second firm $\stackrel { \cdot } { j } ( j \neq i )$ that serves as the recipient of these two payments. Therefore our paper offers an alternative explanation based on the DMH problem on why it is beneficial for an MSSP to serve multiple client firms.

In the next section we extend our model to three or more client firms.

6. Extension to Three or More Firms In this section we extend the model from two client firms to any finite number, $N ,$ of client firms, where integer $N > 1$ . We also use subscript $^ { \prime \prime } N ^ { \prime \prime }$ to denote this extension. The social welfare is now

$$
\begin{array}{c} S W _ {N} (E _ {N}) = N V - \sum_ {i = 1} ^ {N} (1 - P ^ {i} (E _ {N})) d - \sum_ {i = 1} ^ {N} C _ {F} (e _ {F N} ^ {i}) \\ - C _ {M} (e _ {M N} ^ {1}, e _ {M N} ^ {2}, \dots , e _ {M N} ^ {N}), \end{array} \tag {1}\tag{24}
$$

where ${ \cal E } _ { \scriptscriptstyle N } ~ = ~ ( e _ { \scriptscriptstyle F N } ^ { 1 } , e _ { \scriptscriptstyle F N } ^ { 2 } , \ldots , e _ { \scriptscriptstyle F N } ^ { N } , e _ { \scriptscriptstyle M N } ^ { 1 } , e _ { \scriptscriptstyle M N } ^ { 2 } , \ldots , e _ { \scriptscriptstyle M N } ^ { N } )$ Therefore FBS efforts, $E _ { N } ^ { * } ,$ satisfy

$$
\sum_ {j = 1} ^ {N} \frac {\partial P ^ {j} (E _ {N})}{\partial e _ {F N} ^ {i}} d - C _ {F} ^ {\prime} (e _ {F N} ^ {i}) = 0 \quad \mathrm{for} 1 \leq i \leq N,\tag{25}
$$

and

$$
\sum_ {j = 1} ^ {N} \frac {\partial P ^ {j} (E _ {N})}{\partial e _ {M N} ^ {i}} d - \frac {\partial C _ {M}}{\partial e _ {M N} ^ {i}} = 0 \quad \mathrm{for} 1 \leq i \leq N.\tag{26}
$$

Directly solving for the optimal contingent payment plan for a general N is computationally cumbersome because the number of breach scenarios we need to consider grows in the number of firms. Instead, we first observe in Figure 5 that, under $N = 2$ and given that n $( n = 0 , 1 , 2 )$ firms are breached, the net ex post payment out of the MSSP is a simple linear function nd. In other words, under optimal multilateral contracts the MSSP pays an ex post net payment of d for every breached firm.<sup>19</sup> As we will show shortly, it turns out this observation holds true for optimal multilateral contracts under any $N \geq 2$ . Hereafter we limit our attention to multilateral contracts under which, if firm i is breached, the MSSP pays d for this breach and this breached firm pays d for this breach, where constant $\gamma$ is to be determined.<sup>20</sup> The sum of these two payments, $d + \gamma d ,$ , is then evenly distributed to the other $\mathsf { \bar { N } } - 1$ firms through the intermediation of the MSSP. Given such a contingent payment plan, the MSSP’s expected payoff is

$$
\begin{array}{c} U _ {M N} (E) = N f - \sum_ {i = 1} ^ {N} (1 - P ^ {i} (E _ {N})) d \\ - C _ {M} (e _ {M N} ^ {1}, e _ {M N} ^ {2}, \ldots , e _ {M N} ^ {N}). \end{array}\tag{27}
$$

Differentiating (27) with respect to $e _ { M N } ^ { i } ,$ the resulting first order condition is identical to (26).

For $1 \leq i \leq N _ { \cdot }$ , firm i’s expected payoff is

$$
\begin{array}{l} U _ {F N} ^ {i} (E _ {N}) = V - f - (1 - P ^ {i} (E _ {N})) (d + \gamma d) \\ \qquad + \sum_ {j = 1, j \neq i} ^ {N} (1 - P ^ {j} (E _ {N})) \frac {d + \gamma d}{N - 1} - C _ {F} (e _ {F N} ^ {i}). \end{array}\tag{28}
$$

On the right-hand side of (28), the second item is the damage to firm i plus the payment it sends to the MSSP if it is breached. The third item is the total payment it receives if other firms are breached. Differentiating (28) with respect to $e _ { F N } ^ { i } ,$ , we know the firm’s stage 3 effort satisfies

$$
\begin{array}{l} \frac {\partial P ^ {i} (E _ {N})}{\partial e _ {F N} ^ {i}} (d + \gamma d) \\ - \sum_ {j = 1, j \neq i} ^ {N} \frac {\partial P ^ {j} (E _ {N})}{\partial e _ {F N} ^ {i}} \frac {d + \gamma d}{N - 1} - C _ {F} ^ {\prime} (e _ {F N} ^ {i}) = 0. \end{array}\tag{29}
$$

<sup>19</sup> Again, under multilateral contracts such a payment does not necessarily go to the breached firm.

$^ { 2 0 } \mathrm { ~ A ~ }$ negative  means the breached firm receives d. Also note that, when $N = 2 , \gamma = - \phi _ { b n }$

The above contingent payment plan can induce FBS efforts if and only if the solution (of firm effort) to $( 2 5 ) , E _ { N } ^ { * } ,$ is also a solution to (29). Therefore contract optimality requires

$$
\gamma = \left. \left(\frac {\frac {N}{N - 1} \sum_ {j = 1 , j \neq i} ^ {N} \frac {\partial P ^ {j} (E _ {N})}{\partial e _ {F N} ^ {i}}}{\frac {\partial P ^ {i} (E _ {N})}{\partial e _ {F N} ^ {i}} - \frac {1}{N - 1} \sum_ {j = 1 , j \neq i} ^ {N} \frac {\partial P ^ {j} (E _ {N})}{\partial e _ {F N} ^ {i}}}\right) \right| _ {E _ {N} = E _ {N} ^ {*}}.\tag{30}
$$

We can now provide a complete characterization of the optimal multilateral contracts for any N .

<sup>Proposition</sup> <sup>6.</sup> Given N firms, the optimal multilateral contract between the MSSP and firm $i ~ \left( 1 \leq i \leq N \right)$ consists of a fixed payment $f _ { N } ^ { * } \equiv \bar { U } _ { F N } - \underline { { U } } _ { F }$ from firm i to the MSSP upon signing the security contract and contingent payment plan ê<sup>∗</sup> as following:

If n $( 1 \leq n \leq N )$ firms are breached,

(i) the net total payment by the MSSP is nd3

(ii) if firm i is not breached, it receives a total payment o $f { ( n / ( N - 1 ) ) ( 1 + \gamma ) } d$ from the MSSP;

(iii) if firm i is breached, it pays a total payment of $( \gamma - ( ( n - 1 ) / ( N - 1 ) ) ( 1 + \gamma ) ) d$ to the MSSP.<sup>21</sup>

This multilateral contract induces FBS efforts from all players.

In Proposition $6 , ~ \bar { U } _ { F N } \equiv U _ { F N } ^ { i } ( 0 , \Phi _ { N } ^ { * } , E _ { N } ^ { * } )$ denotes a firm’s expected payoff under $\Phi _ { N } ^ { * }$ and if the MSSP does not charge any ex ante fixed payment. Proposition 6 shows that multilateral contracts are able to induce FBS efforts regardless of the number of client firms (except for one firm). Compared to the case of two firms in Proposition $5 ,$ Proposition 6 offers a number of new insights. First, the optimal total net payments from the MSSP under a given security breach scenario is a simple linear function of the number of breached firms. Therefore increasing the number of client firms does not complicate the MSSP’s side of a multilateral contract.

Second, a firm’s net payment in a multilateral contract is slightly more complicated to calculate because this net payment depends on all firms’ security status. Nevertheless, this net payment remains computationally simple as it can be derived simply by adding up all contingent payments triggered by each breached firm. In summary, our proposed multilateral contracts can be extended to the case of three or more client firms, and remains computationally simple for implementation.

Although our proposed multilateral contract is new to the MSSP industry, similar contracts that condition the ex post payment to a firm on the performance of many other firms exist in other industries. One such prominent example is value-based purchasing (VBP)

that is recently adopted by the federal agency in charge of Medicare (Bastide 2011, Crothall Healthcare 2011, Wood-Buhlman and Matthes 2011 and Zwiener 2011).<sup>22</sup> Under VBP, the Medicare reimbursement a hospital receives at the end of a fiscal year depends on this hospital’s performance percentile among all participating hospitals. This percentile in turn is a function of the total hospital pool size, this focal hospital’s performance and the number of hospitals that perform worse than this hospital. Similar to VBP, under our proposed multilateral contracts a firm’s ex post contingent payment is a function of the total number of firms, whether this focal firm is breached or not (i.e., a binary performance measure) and the number of other firms that are breached.

Another direct implication of VBP is that adding or removing a hospital from the pool will affect the percentile measures, and thus the ex post Medicare reimbursements, of all remaining hospitals. VBP addresses this adding/removing firms issue using two ways. First, because reimbursement payments are explicit functions of the number of participating hospitals, such adding/removing dynamics will not invalidate all existing contracts (or trigger large-scale contract rewriting) as long as all measures are calculated based on ex post total number of hospitals. Similarly, under our proposed multilateral contracts the contingent payment plan is also an explicit function of the number of client firms. Second, VBP updates contract terms only periodically. New subscribers are grandfathered into current year’s contract terms, and updates to the contract terms take place only on a yearly base. Understandably, such periodic adjustments are a trade-off between the cost-savings from avoiding too-frequent contract updates and the efficiency loss because of suboptimal contracts offered to new subscribers between plan years. Similarly, when the cost of updating security contracts is high, an MSSP can consider adjusting multilateral contracts only periodically to balance between possible interim contractual inefficiencies and cost savings from less frequent contract changes.

We should acknowledge that our proposed multilateral contract has its limitations. For it to be effective, information regarding security breach needs to be public information among all contractual parties. This is the case, for example, when personal information is involved and laws require mandatory disclosure, or when information disclosure is essential for patching up security holes. Payments under multilateral contracts are contingent on the number of client firms that an MSSP services, which can change over time and depends on how successful the MSSP can acquire clients.<sup>23</sup>

## 7. Concluding Remarks

We examined the double moral hazard problem that arises in information security outsourcing using a prescriptive framework and a principal-agent setup. Strong externality effects of security efforts and the multiclient nature of MSSP services complicate the double moral hazard problem in security outsourcing. We showed that the prevailing contract structure in security outsourcing, bilateral refund contract, cannot solve double moral hazard. Adding sunk cost or external payment to a bilateral refund contract cannot solve double moral hazard either. Furthermore, under this contract, positive externality can worsen double moral hazard. We proposed multilateral contract structure and showed that it can solve double moral hazard and induce optimal efforts from all contractual parties when an MSSP serves two or more client firms. Firm-side externality significantly affects how payments flow under a multilateral contract when a security breach happens. When the number of client firms for an MSSP increases, we showed that the contingent payments under multilateral contracts for any security breach scenario can be easily calculated using an additive method, and thus are computationally simple to implement.

Note that not all information security outsourcing practices suffer from the double moral hazard problem. In scenarios where MSSP and firm efforts can be directly observed and verified, simpler contracts can be written to directly mandate player efforts. Alternatively, when the liabilities upon a security breach can be unequivocally attributed to (and subsequently enforced upon) only one side of a contract, contractual parties are facing multiple single-sided rather than double-sided moral hazard problems. Our research applies to scenarios where efforts are private to contractual parties and it is infeasible (or cost prohibitive) to clearly assign the liabilities of a breach to only one party.<sup>24</sup> The effectiveness of our proposed multilateral contracts also depends on contractual parties’ ability to observe security breaches.<sup>25</sup> This is the case, for example, when firms are legally required to disclose security breaches. Alternatively, a firm may need to disclose a security incidence to its MSSP in order to collaboratively discover and patch the root cause.

The research can be extended in several directions. One possibility is to analyze the role of costly monitoring in reducing double moral hazard in information security outsourcing. We assumed that the players are risk neutral. Another possibility is to analyze how the optimal contracts would change if the players are risk averse. In practice firms sometimes purchase insurances to cover loss when breaches take place. How insurance affects security contracting is also a research possibility.<sup>26</sup>

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.1120.0447.

## References

Allen J, Gabbard D, May C (2003) Outsourcing managed security services. Whitepaper, Carnegie Mellon Software Engineering Institute. Available at http://www.cert.org/archive/pdf/omss .pdf.

Al-Najjar N (1997) Incentive contracts in two-sided moral hazards with multiple agents. J. Econom. Theory 74(1):174–195.

Anderson R, Moore T (2006) The economics of information security. Science 314(27):610–613.

Arce I (2003) The weakest link revisited. IEEE Security and Privacy 1(2):72–76.

Balachandran KR, Radhakrishnan S (2005) Quality implications of warranties in a supply chain. Management Sci. 51(8):1266–1277.

Bastide K (2011) Health care reform presents challenges for Howard Regional Health system. Indiana Economic Digest (April 15). Available at http://www.indianaeconomicdigest.net/main.asp ?SectionID=31&SubSectionID=135&ArticleID=59429.

Bhattacharyya S, Lafontaine F (1995) Double-sided hazard and the nature of share contracts. RAND J. Econom. 26(4):761–781.

Cezar A (2009) Essays on information security and risk management. Ph.D. Dissertation, The University of Texas at Dallas.

Cezar A, Cavusoglu H, Raghunathan S (2010) Outsourcing information security: Contracting issues and security implications. Ninth Workshop on Economics of Information Security, (WEIS 2010), Cambridge, MA.

Chalos P, Sung J (1998) Outsourcing decisions and managerial incentives. Decision Sci. 29(4):901–919.

Cooper R, Ross TW (1985) Product warranties and double moral hazard. RAND J. Econom. 16(1):103–113.

Corbett CJ, DeCroix GA, Ha AY (2005) Optimal shared-savings contracts in supply chains: Linear contracts and double moral hazard. Eur. J. Oper. Res. 163(3):653–667.

Crothall Healthcare (2011) Patient Satisfaction News (Jan. 13). Available at http://media.crothall.com/global/news/2011-01 \_Patient\_Satisfaction\_News.pdf

Dey D, Fan M, Zhang C (2010) Design and analysis of contracts for software outsourcing. Inform. Systems Res. 21(1):93–114.

Ding W, Yurcik W (2005) Outsourcing Internet security: The effect of transaction costs on managed service providers. Internat. Conf. Telecommunication Systems, Modeling Anal., Dallas, TX, 17–20.

Ding W, Yurcik W (2006) Economics of Internet security outsourcing: Simulation results based on the Schneider model. Fifth Workshop on the Economics of Securing the Information Infrastructure, (WEIS 2006), Washington, DC, 1–22.

Ding W, Yrucik W, Yin X (2005) Outsourcing Internet security: Economic analysis of incentives for managed security service providers. First Internat. Workshop on Internet and Network Econom., Hong Kong, China, 947–958.

Fenn C, Shooter R, Allan K (2002) IT security outsourcing: How safe is your IT security? Comput. Law and Security Rep. 18(2):109–111.

Fudenberg D, Tirole J (1998) Game Theory (The MIT Press, Cambridge, MA).

Gal-Or E, Ghose A (2005) The economic incentives for sharing security information. Inform. Systems Res. 16(2):186–208.

George R (2008) Security to go: Is it time to shop MSSPs? InformationWeek (November 1). Available at http://www .informationweek.com/news/showArticle.jhtml?articleID=211800247.

Goo J (2010) Structure of service level agreements (SLA) in IT outsourcing: The construct and measurement. Inform. Systems Frontiers 12(2):185–205.

Gordon LA, Loeb MP (2002) The economics of information security investment. ACM Trans. Inform. System Security 5(4):438–457.

Granger S (2001) Social Engineering Fundamentals, Part 1: Hacker Tactics. SecurityFocus (December 18), http://www .securityfocus.com/infocus/1527.

Gupta S, Romano RE (1998) Monitoring the principal with multiple agents. RAND J. Econom. 29(2):427–442.

Hayes F (2008) Frankly speaking: Business partners are a prime attack vector. Computerworld (June 23), http://www .computerworld.com/s/article/320953/Attack\_Vector.

Jayanth R, Jacob VS, Radhakrishnan S (2010) Vendor and client interaction for requirement assessment in software development: Implications for feedback process. Inform. Systems Res. 22(2):289–305.

Kim SK, Wang S (1998) Linear contracts and the double moralhazard. J. Econom. Theory 82(2):342–378.

Liu Z, Squillante MS, Wolf JL (2001) On maximizing service-levelagreement profits. Proc. 3rd ACM Conf. Electronic Commerce, New York, NY, 213–223.

Mayne M (2008) Outsourcing made easy. SC Magazine (December 1) 26. Available at http://www.scmagazineuk.com/ outsourcing-made-easy/article/121804/.

Richmond W, Seidmann A, Whinston A (1992) Incomplete contracting issues in information systems development outsourcing. Decision Support Systems 8(5):459–477.

Rothke B, Mundhenk D (2009) Sue the Auditor and Shut Down the Firm (July 9). Available at http://www.csoonline .com/article/496923/Sue\_the\_Auditor\_and\_Shut\_Down\_the\_Firm.

Rowe B (2007) Will outsourcing IT security lead to a higher social level of security? Sixth Workshop on Economics of Information Security, (WEIS 2007) Pittsburgh, PA.

Schneier B (2002) The case for outsourcing security. Computer 35(4):20–26.

Sen S, Raghu TS, Vinze A (2009) Demand heterogeneity in IT infrastructure services: Modeling and evaluation of a dynamic approach to defining service levels. Inform. Systems Res. 20(2):258–276.

Straub DW, Welke RJ (1998) Coping with systems risk: Security planning models for management decision making. MIS Quart. 22(4):441–469.

Vanauken J (2006) Hired guns. Network Comput. (August 3):39–50.

Varian HR (2000) Managing online security risks. NewYork Times (June 1), http://people.ischool.berkeley.edu/<sup>\~</sup>hal/people/ hal/NYTimes/2000-06-01.html.

Varian HR (2003) System reliability and free riding. Sadeh, ed. Fifth Internat. Conf. Electronic Commerce (ACM, New York), 355–366.

Wang ET, Barron T, Seidmann A (1997) Contracting structures for custom software development: The impacts of informational rents and uncertainty on internal development and outsourcing. Management Sci. 43(12):1726–1744.

Whang S (1992) Contracting for software development. Management Sci. 38(3):307–324.

Wood-Buhlman N, Matthes N (2011) The time to prepare for value-based purchasing is now. Whitepaper, Press Ganey. Available at http://www.pressganey.com/Documents\_secure/ White%20Papers/VBP\_TimeToPrepareIsNow.pdf?viewFile.

Zetter K (2009) In Legal First, Data-Breach Suit Targets Auditor, Wired (June 2). Available at http://www.wired.com/ threatlevel/2009/06/auditor\_sued/.

Zwiener M (2011) Overview of CMS Proposal for Value Based Purchasing. Available at http://www.nrcpicker.com/Events/ Conferences/Documents/Forms/AllItems.aspx.
