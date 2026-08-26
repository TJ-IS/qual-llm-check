---
otero_id: 9066
otero_key: "V2B54ZAC"
title: "Research Note—Patching the Cloud: The Impact of SaaS on Patching Strategy and the Timing of Software Release"
authors: "Vidyanand Choudhary; Zhe (James) Zhang"
year: "2015"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0601"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/V2B54ZAC/fulltext/images/8c1b68afb081c431dbc3c3af62f3be31e97e3611f4bab5415e8bc3c77f813e21.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Note—Patching the Cloud: The Impact of SaaS on Patching Strategy and the Timing of Software Release

Vidyanand Choudhary, Zhe (James) Zhang

## To cite this article:

Vidyanand Choudhary, Zhe (James) Zhang (2015) Research Note—Patching the Cloud: The Impact of SaaS on Patching Strategy and the Timing of Software Release. Information Systems Research 26(4):845-858. http://dx.doi.org/10.1287/isre.2015.0601

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2015, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/V2B54ZAC/fulltext/images/3a2030195c765cbaf34e47f1c7cc6f7fcbf93eeb2ea8cad0236ba40e457c565c.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

http://dx.doi.org/10.1287/isre.2015.0601 © 2015 INFORMS

# Research Note

# Patching the Cloud: The Impact of SaaS on Patching Strategy and the Timing of Software Release

Vidyanand Choudhary

Paul Merage School of Business, University of California Irvine, Irvine, California 92697, veecee@uci.edu

Zhe (James) Zhang

Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080, jameszhangzhe@utdallas.edu

This paper extends prior research on the software vendors' optimal release time and patching strategy in the context of cloud computing and software as a service (SaaS). Traditionally, users are responsible for running on-premises software; by contrast, a vendor is responsible for running SaaS software, and the SaaS vendor incurs a larger proportion of defect-related costs than a vendor of on-premises software. We examine the effect of this difference on a vendor's choice of when to release software and the proportion of software defects to fix. Surprisingly, we find that, despite incurring a larger proportion of defect-related costs, it is optimal for the SaaS vendor to release software earlier and with more defects, and to patch a smaller proportion of defects, than the on-premises software vendor. Even though the SaaS vendor incurs higher defect-related costs, he obtains a larger profit than the traditional vendor. In addition, we find that for a vendor who uses the SaaS model, the optimal number of defects after patching may be lower than the socially efficient outcome. This occurs despite the fact that the number of defects after patching in the SaaS model is higher than in the traditional on-premises model.

Keywords: software security; cloud; software as a service; patch management; software release time; software maintenance; defect-related costs; economics of information systems; monopoly

History: Rahul Telang, Senior Editor; Amit Mehra, Associate Editor. This paper was received on February 27, 2013, and was with the authors 14 months for 3 revisions.

## 1. Introduction

The adoption of cloud computing and software as a service (SaaS) is growing steadily. Armbrust et al. (2010) point out that SaaS is different from traditional on-premises software in several ways. SaaS is executed on remote hardware, and users access it via the Internet. It features (i) on-demand computing, (ii) subscription pricing, and (iii) remote hosting. Because SaaS software is executed on a vendor's cloud-based hardware, the vendor is responsible for running and maintaining the software and correcting software defects; by contrast, in the on-premises model, the user's information technology (IT) department manages and fixes the software. Under the on-premises model, both users and the vendor incur costs related to the number of software defects (defect-related costs), and under SaaS, the vendor incurs more of the defect-related costs and the users incur less. This paper is focused on the impact of this change in sharing of defect-related costs between users and the vendor. In this paper, we examine how the SaaS model has affected vendors' management of defect-related costs. We find that the new SaaS model alters the traditional vendor's incentives with regard to the timing of software release to the market and his patching strategy, so that the incentives are different for cloud-based software vendors such as Dropbox.com and Salesforce.com.

Costs that are related to the number of defects in the released software include (i) software maintenance costs for preventive maintenance and disaster recovery and (ii) business losses stemming from system unavailability and data loss. Examples of software maintenance costs include additional labor to monitor the software, recover from crashes, develop workarounds, and address customer complaints. Instances of business losses include financial and reputational effects of disruption of business, data loss, data theft, and the opportunity cost of lost business. We refer to the sum of the software maintenance costs and business losses as defect-related costs.

The distribution of defect-related costs between users and a vendor is different in the context of traditional on-premises software than in SaaS. For on-premises software, both categories of defect-related costs are largely borne by users; under SaaS, a significant proportion of costs in the software maintenance category is incurred by the vendor who hosts the software. For example, the investment banking firm Cowen and

Company reduced its software maintenance costs by 25% by subscribing to a cloud-based customer relationship management solution from Salesforce.com (Violino 2009). For both the traditional on-premises and SaaS models, users incur the bulk of the cost of business losses. In 2012, for example, Netflix suffered both reputational and financial business losses when its cloud-based streaming service was disrupted by outages in Amazon Web Services (AWS) infrastructure (Bedigian 2012, Clay 2012), and Netflix offered users a discount for several service disruptions (Albanesius 2011).

This paper is closely related to research by Arora et al. (2006), which examines the difference in the product release time and patching strategy between physical goods and software products. They find that the software released by traditional on-premises software vendors contains more defects than typical manufactured or physical goods, but with fewer defects than the socially efficient outcome because the cost of patching software is a fixed cost, whereas patching physical goods incurs fixed and marginal costs. By contrast to that of Arora et al. (2006), our analysis compares vendors' release and patching strategy under the SaaS and traditional on-premises models. Using the framework of Arora et al. (2006), we find that, despite incurring a greater proportion of defect-related costs, the SaaS vendor releases software earlier and with more defects, but patches a lower proportion of defects than the on-premises software vendor.

We now provide a review of research that examines the software vendor's patching strategy in different contexts. Whereas we compare the patching strategies of the SaaS and traditional on-premises models, Kim et al. (2011) compare the effectiveness of the liability mechanism with the patching mechanism for mitigating users' risk in the context of traditional on-premises software. They find that the patching mechanism is more effective when users' patching cost is low or the vendor's patch-development cost is low. Lahiri (2012) examines patching strategy for pirated copies of on-premises software in the absence of patching costs. Lahiri (2012) shows that the vendor may not provide patching support to users of pirated software to differentiate between legal and pirated copies of the software. The lack of patching support increases the quality differential between the legal and pirated copies of the software, thus providing a greater incentive to consumers to purchase legal copies.

Whereas Kim et al. (2011) and Lahiri (2012) study the software vendors' strategy, August and Tunca (2006) and Cavusoglu et al. (2008) study software users' patch-deployment strategy. Modeling the effect of users' patching costs and the negative network security externalities of unpatched software, August and Tunca (2006) find that a subsidy-based policy outperforms a tax-based policy in the context of traditional on-premises software. Cavusoglu et al. (2008) examine the optimal patch-deployment strategy for users of on-premises software and find that synchronization between patch release and patch deployment can be achieved when users and the vendor share the patching costs.

This paper compares on-premises software with SaaS software. Prior research has also examined differences between SaaS and traditional on-premises software, but has not studied a software vendor's patching strategy. Ma and Seidmann (2008) analyze the differences between the business models of SaaS and traditional on-premises software and find that SaaS could gradually cover the market even when its quality is inferior to on-premises software. August et al. (2014) find that software vendors can provide both SaaS and on-premises versions of their software, to target different segments of the market. Choudhary (2007) compares the software quality of an SaaS vendor with that of a traditional on-premises vendor. He shows that the faster release of new features leads to higher software quality in the SaaS context.

Now we discuss the trade-offs involved in determining the optimal patching and release strategy. A software vendor decides when to release the software based on a balance between the costs of development and its revenue (Mehra et al. 2014). The vendor's cost and revenue trade-offs are related to the number of software defects in the context of both SaaS and traditional on-premises software in this paper. The vendor can reduce the number of software defects by spending more time testing and fixing the software before release, and by patching more defects after release. The vendor should rationalize his product and patching strategy to consider costs across several domains: the opportunity cost of software testing, the cost of developing a patch, and the cost of software maintenance. In addition, decisions regarding these domains have revenue implications for the vendor: users prefer software that is released sooner and has fewer defects. Since the vendor is optimizing his profit across these domains, any change in one domain (such as software maintenance) will cause ripple effects in the other domains.

In this paper, we study the impact of a change in the distribution of defect-related costs on the vendor's release time and patching strategy under SaaS. We describe the model setup in §2 and the results in §3. We conclude with a discussion and directions for future research in §4.

## 2. Model

Our model features a monopoly software vendor selling software to a continuum of heterogeneous consumers.

Figure 1 Timeline from Software Release to Obsolescence  
![](/api/attachments/V2B54ZAC/fulltext/images/e31d71ffc75bb448d611f2a7b71f66afd1bf34f50b6eb496ae38cd68fb0825dc.jpg)

We begin with a description of consumer utility for the software ( $\S2.1$ ). We next describe the vendor's cost and profit functions ( $\S2.2$ ) and then provide the vendor's optimal solution ( $\S2.3$ ).

## 2.1. Consumers' Utility

Using the framework of Arora et al. (2006), we capture the distribution of defect-related costs between software users and the vendor under the SaaS model. Consistent with prior literature, users prefer software that is released sooner, but testing and corrective actions can delay software release, particularly when testing must be completed prior to release. Jiang et al. (2012) describe such a release policy as no postrelease testing. They argue that continuing software testing after release, postrelease testing, is better because it lowers the expected costs. Consistent with postrelease testing, we assume that the vendor can continue to test and fix defects after the software release in both contexts—for both SaaS and on-premises software. We use the term outstanding defects to refer to defects at the release time and the term unpatched defects to refer to defects remaining after patching.

Figure 1 illustrates the framework used in Arora et al. (2006), which measures time backward. The software becomes obsolete at an exogenously specified time owing to industry or technological factors. Therefore, the software has a finite time from the start of software testing to its obsolescence. As shown in Figure 1, the software's lifetime in market $(t)$ is the time from release till obsolescence, and this is the time that the software is available in the market. Because time is measured backward, a higher $t$ implies that the vendor releases the software earlier and the software is available for a longer time to users, in which case they derive more utility from the software. However, the earlier the software is released, the greater the number of defects it will have at the release time, because less time was spent on testing and fixing it. We use $B(t)$ to denote the number of outstanding defects in the software at the time of release, which is a convex function of time in market $(t)$ . Note that the number of defects $B(t)$ is assumed to be finite in the interval from the start of software testing to software obsolescence and infinite otherwise.

Software defects lead to defect-related costs for users and the vendor. The vendor can develop software patches to fix defects after software release. This reduces the number of defects in the software, but the vendor has to incur patch-development costs. The vendor must determine the proportion of outstanding defects to be patched over the lifetime of the software, $\delta \in [0, 1]$ . This implies that a proportion $(1 - \delta)$ of the defects remain unpatched in the software. Both the number of outstanding defects $B(t)$ at the time of software release and the number of unpatched defects $B(t)(1 - \delta)$ contribute to the defect-related costs of users and the vendor.

For tractability, we assume that the timing and number of patch releases are exogenous (Arora et al. 2006, Kim et al. 2011). Oracle releases patches on a fixed schedule in its quarterly Critical Patch Update. $^{1}$ Similarly, Microsoft is known to release patches on "patch Tuesday," which is the second, and sometimes fourth, Tuesday of each month. The timing of patch release(s) may affect the defect-related costs. Yet, as illustrated by the examples of Oracle and Microsoft, firms may set their patching schedules based on their operational constraints and other factors unrelated to impact of patch release(s) on users' utility. Thus, we do not model this aspect of patch-release management in this paper.

In our model, the software vendor determines the proportion of defects to be patched over the lifetime of the software. We assume that the rate of defect correction and the timing of patch release are exogenous. The vendor may fix defects at a constant rate per unit time or have some time-varying policy for fixing defects as long as the vendor fixes a total of $B(t)\delta$ defects over the lifetime of the software. We use $k(\delta)$ to map the distribution of defects over the lifetime of the software, which follows from this policy, to defect-related costs. Hence, $B(t)k(\delta)t$ is the total defect-related cost for the highest consumer type over the lifetime of the software. The function $k(\delta)$ decreases with $\delta$ at a decreasing rate for $\delta\in[0,1]$ . This implies that the defect-related costs over the lifetime of the software diminish when the vendor patches more defects; the marginal reduction in defect-related costs from patching decreases as more defects are patched. Furthermore, we assume that the cost of patch deployment is negligible for the vendor and users (Arora et al. 2006, Kim et al. 2011).

Utility parameter V is exogenous and represents the baseline utility derived by users from the software when it is defect-free. User taste parameter $\theta$ captures user heterogeneity in the amount of utility a user derives from the software. We assume that $\theta$ is uniformly distributed on the interval [0, 1]. As discussed in §1, the defect-related cost is distributed between the users and the vendor. We use the exogenous parameter $\alpha \in [0, 1]$ to capture the proportion of defect-related costs incurred by the vendor; the remaining $(1 - \alpha)$ proportion of costs is incurred by users. This proportion $\alpha$ is different for traditional on-premises software and SaaS. As discussed in §1, because the vendor bears a greater proportion of defect-related costs with the SaaS model than with the traditional on-premises model, $\alpha$ is larger for SaaS than for traditional on-premises software. The defect-related costs incurred by a user of type $\theta$ who uses the software for the time that it is available in the market are $\theta(1 - \alpha)B(t)k(\delta)t$ . As discussed in the previous paragraph, $B(t)$ is the number of defects at the time of release, and $k(\delta)$ maps the distribution of defects over time to defect-related costs. Note that when $\alpha = 0$ , we obtain the model of traditional on-premises software employed by Arora et al. (2006).

The SaaS pricing structure is typically subscription based. However, since we do not focus on the temporal variation in software price and quality, users who subscribe to SaaS software at the time of software release will continue to subscribe to it for its lifetime. Thus, we model only the total subscription price, which is the total amount for subscribing to SaaS for the lifetime of the software. This total subscription price for SaaS is denoted by p. In §3.3.2, we show that our results derived using the total subscription price are robust to a model where subscription prices are modeled to be per unit time.

The pricing structure under the traditional on-premises model is a one-time price (also denoted by $p$ ). Since the vendor charges only one price, all users who intend to purchase the software will do so at the release time because delaying purchase decreases users' utility.

Consumer utility from purchasing the on-premises software at the release time and from subscribing to the SaaS software for the entire time that it is available in the market is given by

$$
U = \theta [ V - (1 - \alpha) B (t) k (\delta) ] t - p.\tag{1}
$$

We describe the vendor's cost and benefit in §2.2.

## 2.2. Software Vendor

The vendor needs to determine the optimal release time for the software and the proportion of defects to be patched while optimizing his revenue and cost.

The marginal cost of producing the software is zero; however, the vendor incurs a patch-development cost, $FB(t)\delta$ , which depends on the number of defects patched, and F is a scaling parameter. This patch-development cost-scaling parameter is identical in both models: traditional on-premises software and SaaS. Furthermore, Banker and Slaughter (1997) show that there may be economies of scale in software maintenance, which implies that the vendor and users may differ in their ability to manage defect-related costs. Therefore, we use a parameter e (e > 0) to scale the defect-related costs incurred by the vendor relative to users. The monopolist software vendor's profit function from selling on-premises software or an SaaS subscription over the lifetime of the software is

$$
\pi = D (p, t, \delta) p - F B (t) \delta - \alpha e B (t) k (\delta) t,\tag{2}
$$

where $D(p,t,\delta)$ is the endogenous demand, and $\alpha eB(t)k(\delta)t$ is the vendor's share of defect-related costs for the software product. As discussed in §2.1, the proportion of defect-related costs incurred by the vendor ( $\alpha$ ) is larger under the SaaS model than under the on-premises software model.

## 2.3. Vendor's Optimal Strategy

The monopolist vendor determines the optimal price, time in market, and proportion of defects patched simultaneously. The individual rationality constraint implies that users purchase the software only if they derive a nonnegative surplus. Therefore, the consumer who is indifferent between buying and not buying the software is $\tilde{\theta}=p/([V-(1-\alpha)B(t)k(\delta)]t)$ . All consumers of type $\theta$ greater than $\tilde{\theta}$ buy the software; therefore, the market demand function is

$$
D (p, t, \delta) = N \bigg (1 - \frac {p}{[ V - (1 - \alpha) B (t) k (\delta) ] t} \bigg),
$$

where $N$ is the scaling parameter for market size. Substituting the demand function into the vendor's profit function (2), we obtain

$$
\begin{array}{r} \pi = N \bigg (1 - \frac {p}{[ V - (1 - \alpha) B (t) k (\delta) ] t} \bigg) p \\ - F B (t) \delta - \alpha e B (t) k (\delta) t. \end{array}\tag{3}
$$

We then solve for the optimal price $(p^{*})$ , time in market $(t^{*})$ , and proportion of defects patched $(\delta^{*})$ , which maximize the vendor's profit function.

## 3. Results

In this section, we report results on the impact of the distribution of software defect-related costs between users and the vendor on the endogenous variables, such as the software-release time, the proportion of defects patched, and the profit under the SaaS model. We also compare the SaaS vendor's optimal solution to the socially efficient solution.

Figure 2 (Color online) (a) Consumer Utility and (b) the Vendor's Total Cost with Respect to the Software-Release Time t for $\alpha=0.3$ , $\alpha=0.5$ , and $\alpha=0.7$ , Where $B(t)=t^{2}$ , $k(\delta)=5/4-\delta(2-\delta)$ , $\theta=1$ , N=4, $\delta=0.5$ , F=1.5, e=0.8, and V=8  
![](/api/attachments/V2B54ZAC/fulltext/images/f84164f4e1b126642f4813d65799c8bff0cf15e2f3e321a9bafda430935250dd.jpg)

![](/api/attachments/V2B54ZAC/fulltext/images/fdd9a6a69dd202e6a1d5c9f4b9a2209833e98d8c5344156af7120f01c04c93ff.jpg)  
(b)

## 3.1. Comparing a Traditional On-Premises Software Vendor with SaaS

Under the SaaS software model, the vendor incurs a significant proportion of defect-related costs that is greater than the defect-related costs incurred under the traditional on-premises model. Proposition 1 examines the impact of defect-related costs on the vendor's optimal release time for the software.

PROPOSITION 1. When the proportion of defect-related costs incurred by the software vendor increases, the monopolist releases the software earlier ( $dt^{*}/d\alpha > 0$ ) if the market size is sufficiently large (N > 4e). The monopolist releases the software later ( $dt^{*}/d\alpha \leq 0$ ) if the market size is sufficiently small ( $N \leq 4e$ ).

In our model, an SaaS vendor incurs a higher proportion of defect-related costs than a traditional on-premises software vendor because the SaaS vendor is responsible for running the software. This implies that the SaaS vendor incurs higher costs with all else held constant. Therefore, one would expect the SaaS vendor to release software later than the on-premises software vendor, to reduce the number of outstanding defects and defect-related costs. This expectation is consistent with the results of Kim et al. (2011), who show that the vendor has a greater incentive to improve the software quality when the vendor is liable for users' losses. By contrast, Proposition 1 posits that the SaaS vendor releases the software earlier with more defects than a traditional on-premises vendor even if the SaaS vendor expects to incur more defect-related costs. Thus, a key implication of our analysis is that the time-to-market pressure will weigh more heavily for managers than the pressure to develop defect-free software in the context of SaaS. This result generates an empirically testable hypothesis: all else being equal, SaaS software will have a greater number of defects at initial release than traditional on-premises software. SaaS software is designed for large-scale, multitenant use; therefore, in this study we focus on the case where the market size is large $(N > 4e)$ . The proof is provided in the appendix.

The counterintuitive result that the SaaS vendor releases the software earlier than the on-premises software vendor can be understood by examining the impact of the defect-related costs on consumer utility and the vendor's costs. A change in $\alpha$ influences the vendor's decision variables in two ways. First, as seen in Figure 2(a), an increase in $\alpha$ reduces users' concern about defects, and hence pushes the vendor toward an earlier release time, as the level at which the consumer utility is maximized shifts toward a larger value of t. This implies that consumers obtain higher utility if the software is available for a longer time, even though it contains more defects at the time of release. Moreover, the increase in $\alpha$ results in an increase in consumer utility, which allows the SaaS vendor to increase price, and thus leads to higher revenue.

Second, Figure 2(b) illustrates that when $\alpha$ increases, the vendor's defect-related costs increase, and the cost curve becomes steeper. The increasing slope of the cost curve pushes the vendor toward a later software-release time (smaller $t$ ). The vendor's optimal release time is determined by the balance of these two forces, as illustrated in Figures 2(a) and 2(b). Increasing consumer utility pushes the vendor toward earlier release, whereas increasing cost pushes the vendor toward later release. It follows that when the consumer utility effect dominates the cost effect, the vendor will release the software earlier. The consumer utility effect is dominant when the market is sufficiently large. Therefore, the SaaS vendor will release the software earlier than a traditional on-premises software vendor when the market is sufficiently large. This completes the intuition for Proposition 1.

PROPOSITION 2. When the proportion of defect-related costs incurred by the software vendor increases, the monopolist patches a lower proportion of defects ( $d\delta^{*}/d\alpha < 0$ ) if the market size is sufficiently large (N > 4e). The vendor patches a greater proportion of defects ( $d\delta^{*}/d\alpha \geq 0$ ) if the market size is sufficiently small ( $N \leq 4e$ ).

Figure 3 (Color online) (a) Consumer Utility and (b) Vendor's Revenue with Respect to $\delta$ for $\alpha = 0.3$ , $\alpha = 0.5$ , and $\alpha = 0.7$ , Where $B(t) = t^2$ , $k(\delta) = 5/4 - \delta(2 - \delta)$ , $\theta = 1$ , $N = 4$ , $t = 2.3$ , $\theta = 1$ , $e = 0.8$ , and $V = 8$  
![](/api/attachments/V2B54ZAC/fulltext/images/742176be70628c94743a72f4f22aca1aa6853d68b7d46b0a3c285c820182084b.jpg)  
(a)  
In light of Proposition 1, which shows that an SaaS vendor will release the software earlier and with more defects, one may naïvely expect the vendor to patch a greater proportion of defects because he incurs a greater share of the defect-related costs. Moreover, Arora et al. (2006) find that, compared with manufacturers of physical goods, a traditional on-premises software vendor will release software earlier but fix more defects after the release. By contrast, Proposition 2 posits that, despite releasing his software earlier, the SaaS vendor patches a smaller proportion of defects than a traditional on-premises vendor when the market is sufficiently large. Proposition 2 suggests that an SaaS vendor should focus more on managing software that contains defects than on fixing software defects relative to a vendor of traditional on-premises software. This insight is discussed further in §4.

Now, we offer the intuition for Proposition 2. Consumer utility increases when a higher proportion of defect-related costs (greater $\alpha$ ) is shifted to the vendor (Figure 3(a)). It is easy to see that this increase in the utility also leads to an increase in the vendor's revenue as the vendor can now charge a higher price (Figure 3(b)). Note that the revenue peaks when the vendor fixes all defects ( $\delta = 1$ ). However, fixing all defects may not be optimal because the patch-development cost could then be very high. Therefore, the vendor's optimal patching strategy may involve patching only some of the defects, although this strategy also leads to lower revenue. The extent of this revenue reduction depends on the slope of the revenue curve. Figure 3(b) shows that the vendor's revenue curve is less steep when $\alpha$ is larger, because a smaller proportion of defect-related costs is incurred by users, thus insulating them from changes in $\delta$ . In other words, when $\alpha$ is larger, there is less reduction in the revenue due to defects left unpatched than the reduction when $\alpha$ is smaller. In Figure 3(b), the revenue difference between patching all defects ( $\delta = 1$ ) and patching a portion of the defects

![](/api/attachments/V2B54ZAC/fulltext/images/bfeeef5420b504b361c5fb38d79b01bc7f3e7a391b2802e9aa776928d3a79045.jpg)  
(b)  
$(\delta = 0.2)$ is $D1$ when $\alpha = 0.7$ , and the difference is $D2$ when $\alpha = 0.3$ . It is clear that the revenue reduction is smaller when $\alpha$ is greater ( $D1 < D2$ ). Since $\alpha$ is larger for SaaS, the revenue reduction is smaller in its case, and that allows the vendor to patch a lower proportion of defects. Intuitively, users are more insulated from defect-related costs under the SaaS model, so the reduction in their willingness to pay due to unpatched defects is naturally less. Now we discuss the impact of the vendor's cost on his patching strategy.

The vendor's costs consist of two components: (i) the patch-development cost $(FB(t)\delta)$ and (ii) the defect-related costs $(\alpha eB(t)k(\delta)t)$ . It is clear that the patch-development cost increases with $\delta$ and does not depend on $\alpha$ . On the other hand, defect-related costs decrease with $\delta$ (Figure 4(a)), and they increase with $\alpha$ as the vendor's share of the defect-related costs increases. The sum of these costs is shown in Figure 4(b), and it can be seen that the level of patching at which the vendor's total cost is minimized increases as $\alpha$ becomes larger. This occurs because the vendor's share of defect-related costs increases, and he therefore has an incentive to patch more defects. This force pushes the vendor to patch a higher proportion of defects in the SaaS context. Finally, we discuss the net impact of revenue and cost on the vendor's patching strategy.

Figure 5 shows that when $\alpha$ increases, the vendor's profit is maximized at a lower proportion of defects patched. This occurs because the revenue effect dominates when the market is sufficiently large, leading the SaaS vendor to patch a smaller proportion of defects. This happens despite higher defect-related costs incurred by the SaaS vendor, as shown in Figure 4(b). Therefore, the SaaS vendor will patch a smaller proportion of defects than a traditional on-premises software vendor when the market is sufficiently large. This completes the intuition for Proposition 2.

Combining the results in Propositions 1 and 2, we can show that when the proportion of defect-related costs incurred by the software vendor increases, the vendor will release the software earlier and patch a lower proportion of defects if the market is sufficiently large. This implies that the SaaS vendor leaves more defects unpatched than a traditional on-premises vendor when the market is sufficiently large. Now we examine the impact of SaaS adoption on the vendor's profit.

Figure 4 (Color online) (a) Vendor's Defect-Related Costs and (b) Total Cost with Respect to $\delta$ for $\alpha = 0.3$ , $\alpha = 0.5$ , and $\alpha = 0.7$ , Where $B(t) = t^2$ , $k(\delta) = 5/4 - \delta(2 - \delta)$ , $N = 4$ , $t = 4$ , $F = 1.5$ , $e = 0.8$ , and $V = 8$  
![](/api/attachments/V2B54ZAC/fulltext/images/c51fc18bdc18a26a799cb0d4bc14056fa8b99b20a9945888cf3ad7c1e6bbd925.jpg)  
(a)

Figure 5 (Color online) Vendor's Profit with Regard to Proportion of Defects Patched $\delta$ for $\alpha = 0.3$ , $\alpha = 0.5$ , and $\alpha = 0.7$ Where $B(t) = t^2$ , $k(\delta) = 5/4 - \delta(2 - \delta)$ , $N = 4$ , $t = 2.3$ , $\theta = 1$ , $F = 1.5$ , $e = 0.8$ , and $V = 8$  
![](/api/attachments/V2B54ZAC/fulltext/images/108b90c9632a14649deed83d015a2cb683bb2e284210b8783d80c35e097e83c6.jpg)

COROLLARY 1. When the proportion of defect-related costs incurred by the software vendor increases, the vendor's optimal profit increases $(d\pi^{*}/d\alpha > 0)$ if the market size is sufficiently large $(N > 4e)$ ; correspondingly, his optimal profit decreases $(d\pi^{*}/d\alpha \leq 0)$ if the market size is sufficiently small $(N \leq 4e)$ .

Corollary 1 follows from Propositions 1 and 2 and shows that the SaaS vendor's optimal profit changes as his share of defect-related costs increases subject to the market size. The vendor obtains a higher profit when the market size is sufficiently large. This implies that an SaaS vendor's profit is higher than a traditional vendor's, even though the SaaS vendor incurs higher

![](/api/attachments/V2B54ZAC/fulltext/images/937e6c710b6e993e1f4e09866dd1568f3cda65ae748a3bde57062a1ecd374755.jpg)  
(b)  
defect-related costs. The intuition of this seemingly surprising result is as follows. When $\alpha$ increases, consumers' defect-related costs decrease, and thus the consumers' willingness to pay increases. The vendor can charge a higher price for the software. Therefore, the vendor's revenue increases when $\alpha$ increases. However, when $\alpha$ increases, the vendor's defect-related costs increase. Since the vendor can centralize the management of defects, the increase in its defect-related costs is smaller than the increase in revenue due to the increase in consumers' willingness to pay for the software. Thus, the vendor's profit increases when $\alpha$ increases.

## 3.2. The Socially Efficient Solution

The socially efficient solution requires the SaaS vendor to set the price at marginal cost. In this subsection, we assume that the vendor's marginal cost of running software on its servers for an additional consumer is zero. Thus, the socially efficient price is zero, and the market is covered. The social welfare function is

$$
\begin{array}{c} S (t, \delta) = N \int_ {0} ^ {1} \theta (V - (1 - \alpha) B (t) k (\delta)) t d \theta \\ - F B (t) \delta - \alpha e B (t) k (\delta) t \\ = \frac {N}{2} (V - (1 - \alpha) B (t) k (\delta)) t \\ - F B (t) \delta - \alpha e B (t) k (\delta) t. \end{array}\tag{4}
$$

We use $t^{S}$ and $\delta^{S}$ to represent the socially efficient release time and proportion of defects patched. Thus $t = t^{S}$ and $\delta = \delta^{S}$ solve the social welfare maximization problem stated in (4). Now, we compare the monopolist vendor's optimal release time and proportion of defects patched with the welfare-maximizing solution (Proposition 3). We also compare the number of defects after patching in these two circumstances (Proposition 4).

PROPOSITION 3. When the proportion of defect-related costs incurred by the software vendor increases, it is socially efficient to release the software earlier $(dt^{S}/d\alpha > 0)$ and patch a lower proportion of defects $(d\delta^{S}/d\alpha < 0)$ if N > 2e, or to release the software later $(dt^{S}/d\alpha \leq 0)$ and patch a higher proportion of defects $(d\delta^{S}/d\alpha \geq 0)$ if $N \leq 2e$ .

Figure 6 Comparison of the Monopolist's Optimal Strategy and the Socially Efficient Solution Where $B(t) = t^2$ , $k(\delta) = 2 - \delta(2 - \delta)$ , $N = 5$ , $F = 1$ , $e = 1$ , and $V = 2$  
![](/api/attachments/V2B54ZAC/fulltext/images/811ed0ac51825c958dc0d95612bc7107909687af92c5afb076caed0324f339cf.jpg)

![](/api/attachments/V2B54ZAC/fulltext/images/5a14efa541bc94da2acace705351652ae92d7bb5fddb0c168c3eb7f49b60bf05.jpg)  
Proportion of defect related cost shifted

![](/api/attachments/V2B54ZAC/fulltext/images/713ad446ce9028a54be3db7c0a00f767218278f825c194071199ca8616a25e97.jpg)  
Proportion of defect related cost shifted

In comparing Proposition 3 with Propositions 1 and 2, we observe that the monopolist's optimal strategy is consistent with the socially efficient outcome when the market is sufficiently large ( $N > 4e$ ) or small ( $N \leq 2e$ ). Interestingly, when the market size is moderate ( $2e < N \leq 4e$ ), the monopolist's optimal strategy is to release the software later and patch a higher proportion of defects, which is different from the socially efficient outcome of releasing the software earlier and patching a lower proportion of defects when a greater proportion of defect-related costs is incurred by the vendor.

PROPOSITION 4. There exist conditions under which the number of software defects after patching is lower under the monopolist's optimal strategy relative to the socially efficient solution.

The number of software defects has been examined in prior research. Kim et al. (2011) assume that the vendor always patches all defects. Arora et al. (2006) report that the monopolist releases software with fewer defects than the socially efficient level, but they do not comment on the number of defects after patching. Proposition 4 shows that the number of unpatched defects in the monopolist's software after patching can be lower than the socially efficient level.

The result in Proposition 4 is illustrated in Figure 6, which shows the following: (i) Both the monopolist and the socially efficient levels of time in the market increase (left plot) and the proportion of defects patched decreases with $\alpha$ (center plot); consequently, the number of defects after patching increases with $\alpha$ (right plot). (ii) As seen in the right plot, the monopolist offers software with fewer defects after patching than the socially efficient level under certain conditions.

These results are driven by the fact that the monopolist vendor serves fewer customers than the socially efficient level. Centralizing the management of defective software on the vendor's side reduces the impact of defects on users. Thus, the extent to which the vendor is affected by this centralization effect depends on the number of users. Since it is optimal for the monopolist to serve fewer customers than the socially efficient solution, there is less effect on the monopolist. As a result, we observe that the rate of change of the monopoly solution with an increase in $\alpha$ is lower than the rate of change at the socially efficient level. Specifically, the first plot in Figure 6 shows that the rate of increase of time in the market is lower for the monopolist than the socially efficient level as $\alpha$ increases. We observe a similar trend in the second plot, which shows a decreasing proportion of defects patched. Combining the observations in the first two plots, we can see that the number of defects after patching increases at a slower rate for the monopolist than the socially efficient level. Therefore, there exist conditions in which the number of unpatched defects for the SaaS monopolist vendor is lower than the socially efficient level, as shown in the third plot of Figure 6.

## 3.3. Robustness Checks

So far, we have assumed that the consumers' taste parameter is distributed uniformly on the interval [0, 1] and the marginal cost of running SaaS for an additional consumer is zero, and we modeled only the total subscription price, which is the total amount for subscribing to SaaS for the lifetime of the software. In this subsection, we examine the robustness of our model and show that the qualitative results in §§3.1 and 3.2 continue to hold when these assumptions are relaxed.

3.3.1. General Distribution of $\theta$ . We assumed that consumers' taste parameter ( $\theta$ ) is distributed uniformly on the interval [0, 1]. Now we relax this assumption and demonstrate the robustness of our qualitative results. We define the probability density function of consumers' taste parameter as $g(\theta)$ and the cumulative density function as $G(\theta)$ , and assume that $g(\theta)/(1-G(\theta))$ is nondecreasing in $\theta$ (Bhargava and Choudhary 2004). We show in the appendix that the qualitative results from

Propositions 1 and 2 hold. Therefore, the insight that an SaaS vendor releases the software earlier and patches a lower proportion of defects than an on-premises software vendor when the market is sufficiently large is robust to the distribution of consumers' taste.

3.3.2. Subscription Price per Unit Time. In this paper, we modeled only the total subscription price, which is the total amount of subscribing to SaaS for the lifetime of the software. Now we show that our results derived from using the total subscription price do not change if we model subscription prices per unit time in the SaaS context. The qualitative results do not change because the monopolist SaaS vendor increases the subscription price per unit time after patch release(s) as consumer utility per unit time increases. Thus, the market demand remains constant over the lifetime of the software. As a result, the prices paid by each consumer in total under the two models, the total subscription price model and the subscription price per unit time model, are identical. We provide additional details about the subscription price per unit time model in the following paragraph and the complete proof in the appendix.

We assume that the vendor releases the software at time t and issues only one software patch during the life of the software. The patch is released at time $\beta \times t$ , where $\beta \in (0,1)$ . The vendor charges $p_{R}$ per unit time starting from the software-release time, t, till the patch-release time, $\beta \times t$ (recall that time is measured backward). After the patch release, consumer utility increases, thus the vendor charges a new subscription price, $p_{p}$ , per unit time from the patch release till software obsolescence. Additionally, we use specific functional forms for the number of defects at the release time, $B(t) = t^{2}$ , and $L_{2}(\delta) = 1 - \frac{4}{5}\delta(2 - \delta)$ to map the proportion of defects to be patched to the defects-related costs per unit time after the patch release.

In the appendix, we show that the optimal subscription price per unit time before the patch release is $p_{R}^{*} = (V - (1 - \alpha)t^{2})/2$ , and the optimal subscription price per unit time after the patch release is $p_{P}^{*} = (V - (1 - \alpha)t^{2}(1 - \frac{4}{5}\delta(2 - \delta)))/2$ . The optimal demand per unit time before and after the patch release is $q_{R}^{*} = q_{P}^{*} = \frac{1}{2}$ . Hence, we find that the optimal demand does not change after the patch release. We also obtain the optimal $\delta^{*}$ and $t^{*}$ , and show that $d\delta^{*}/d\alpha < 0$ and $dt^{*}/d\alpha > 0$ if N > 4e, and $d\delta^{*}/d\alpha \geq 0$ and $dt^{*}/d\alpha \leq 0$ if $N \leq 4e$ . This implies that the SaaS vendor releases the software earlier and patches a lower proportion of defects when the market size is sufficiently large, and vice versa if the market size is sufficiently small. Therefore, the qualitative results from Propositions 1 and 2 continue to hold when we model the subscription prices per unit time.

3.3.3. Nonzero Marginal Cost for SaaS. In this paper, we assumed that the marginal cost of running the software for an additional consumer, such as the cost of server maintenance, is zero. When this cost is positive, the socially efficient solution for SaaS in §3.2 changes because the server maintenance cost is a marginal cost to the vendor. In this subsection, we show that the qualitative findings from Proposition 3 hold true for SaaS when the marginal cost is positive.

When the SaaS vendor's marginal cost is positive $(c > 0)$ , the firm's optimal price in Equation (3) is higher than that in the case of zero marginal cost $(c = 0)$ . Moreover, the socially efficient price is set to the marginal cost, $c$ , and thus the lower limit of the integration of the social welfare function in Equation (4) is also higher than that in the case of zero marginal cost. Thus, it is clear that the market demand in the monopoly solution and that in the socially efficient solution are lower than those in the case of zero marginal cost. Nonetheless, the market demand in the socially efficient case is greater than that in the monopoly case when $c > 0$ . Since there is a greater market demand in the case of the socially efficient solution, the vendor's defect-related costs are centralized at a greater scale. Thus, the number of software defects after patching may be lower under the monopolist's optimal strategy relative to the socially efficient solution in the case of nonzero marginal cost. We provide a numerical proof in the appendix.

## 4. Discussion and Conclusion

In this section we describe our key findings, compare them with the literature to highlight the novelty in our findings, and offer some managerial implications. This paper compares the optimal software-release time and proportion of software defects to be patched for an SaaS software vendor to those for an on-premises software vendor. We show that the SaaS vendor may release software earlier with more defects, and yet patch fewer defects than the on-premises software vendor. Moreover, the SaaS vendor obtains a higher profit when he incurs a greater share of the software defect-related costs. These surprising results can be explained by examining the changes in the vendor's defect-related costs and consumer utility. One might expect a vendor who incurs a larger proportion of defect-related costs to release the software later, which gives him more time to correct defects before software release. However, the lower defect-related cost borne by users reduces the negative impact of defects on users' utility. This gives the vendor an incentive to release the software earlier because it increases consumers' utility and thus the price charged by the vendor. When the market size is large enough, the benefits from earlier release to consumers outweigh the increase in the vendor's defect-related costs because the vendor benefits from the centralization of software maintenance. Similarly, the vendor patches fewer defects because of the reduction in consumers' defect-related costs. In addition, whereas one might expect a monopolist software vendor to provide software of a lower quality than the socially efficient level, we find that an SaaS vendor's software contains fewer unpatched defects than the socially efficient level under certain conditions.

This paper contributes to the literature on software patching and SaaS. The SaaS vendor consolidates software maintenance and acquires some of the software defect-related costs from users. In a similar vein, Kim et al. (2011) consider the transfer of users' costs to a software vendor via a product liability contract, and they show that the vendor improves software quality through this transfer of costs. By contrast, we find that an SaaS vendor can optimally release software earlier with more defects than an on-premises software vendor, despite the transfer of software defect-related costs from users to the vendor under the SaaS model. Note that, according to Kim et al. (2011), the vendor is responsible for the aggregate liability and can only reduce this liability by improving software quality. In our model, the SaaS vendor can also reduce the number of defects, and in addition he can consolidate software maintenance in his facility to better manage software defects. Thus, in our model, the SaaS vendor's ability to manage software defect-related costs lowers his incentive to reduce the number of defects at the time of release. Arora et al. (2006) find that a traditional on-premises vendor releases software with more defects but subsequently fixes more defects than a physical goods manufacturer because the cost of patching has declined. We find that the change in the distribution of defect-related costs between users and the vendor and the consolidation of software maintenance under the SaaS model are also drivers of the vendor's software release and patching strategy.

The trend toward SaaS has different effects on vendors depending on the size of their potential market. The key managerial implication of our research is that managers of cloud-based software should be willing to take risks and release early versions of their software, particularly when the potential market for their product is large. We show that the vendor's profit increases with the proportion of defect-related costs incurred by the vendor. Therefore, another implication of our research is that managers should try to consolidate the maintenance and security-related costs on the vendor's side, thus insulating users from these costs. This would increase users' willingness to pay for the software and lead to higher vendor profits.

Proposition 2 provides the insight that an SaaS vendor should focus more on managing defects than on fixing defects relative to an on-premises software vendor. In other words, a vendor may benefit from identifying defects that can be managed by the vendor at reasonable costs. This result is interesting because it is usually considered better to have software with fewer defects. Note that since the SaaS delivery model shifts the burden of managing defects from users to the software vendor, users benefit from a reduction in their defect-related costs despite an increase in the number of defects.

Another managerial implication is that a vendor should prioritize fixing defects that primarily affect users over defects that primarily affect the vendor. For example, a common “buffer overflow” defect that can allow a hacker to take control of the system poses a significant risk to user data and therefore should be given high priority. Defects that do not pose a security hazard can sometimes be managed using a manual reboot. Such defects impact the vendor’s maintenance costs and should receive lower priority. Finally, managers often face trade-offs between maintenance costs and software availability. For example, managers can invest in offsite back-ups and run multiple operating system environments to reduce the risk of system downtime. Our results suggest that SaaS managers should invest more in such resources than managers of on-premises systems.

We develop a stylized model to study the change in a vendor's software release and patching strategy under the SaaS model. We consider a limited number of factors, and future research could study other factors that affect vendors' strategy. One such factor is the heterogeneous cost of fixing defects, which are caused by the different levels of effort required to fix them. Similarly, the benefit of fixing defects may also be heterogeneous. Therefore, the vendor may be strategic in deciding which defects to fix, and this decision may be different for SaaS and on-premises software vendors. Moreover, we model total subscription price over the lifetime of the software in the SaaS context. Future research can analyze SaaS firms' patching strategy while incorporating the time dimension in subscription pricing. In addition, we assume that the rate of defect correction and the timing of patch release are exogenous. Thus, we do not investigate the impact of the strategic timing of patch release, and this can be the subject of future research. Finally, we have analyzed a fulfilled expectations game in which users anticipate the vendor's choices. Future research can examine the impact of information asymmetry and boundedly rational consumers.

## Acknowledgments

The authors would like to thank the senior editor, associate editor, and two anonymous reviewers for their helpful and insightful comments.

## Appendix

PROOF OF PROPOSITIONS 1 AND 2. First, by solving the profit-maximizing problem $\max_p \pi(p)$ given $t$ and $\delta$ , where $\pi(p)$ is the vendor's profit function (3), we have $\hat{p} = \frac{1}{2}[V - (1 - \alpha)k(\delta)B(t)]t$ , and we assume $V > (1 - \alpha)k(\delta)B(t)$ .

When we substitute the price $\hat{p}$ into the profit function (3), we obtain

$$
\hat {\pi} (t, \delta , \alpha) = \frac {1}{4} N (V - (1 - \alpha) B (t) k (\delta)) t - F B (t) \delta - \alpha e B (t) k (\delta) t.\tag{5}
$$

We rewrite profit $\hat{\pi}=f(t,\delta;\alpha)=m(V-(1-\alpha)k(\delta)B(t))t-FB(t)\delta-\alpha ek(\delta)B(t)t$ , where m=N/4. Then, we have the first-order conditions (FOCs) with respect to t and $\delta$ , given $\alpha$ , as follows:

$$
m V - F \delta B ^ {\prime} (t) - (m (1 - \alpha) + \alpha e) k (\delta) (B ^ {\prime} (t) t + B (t)) = 0,\tag{6}
$$

$$
- F - (m (1 - \alpha) + \alpha e) k ^ {\prime} (\delta) t = 0.\tag{7}
$$

From (6) and (7) we have two identity equations

$$
\begin{array}{c} \Psi^ {1} (t ^ {*} (\alpha), \delta^ {*} (\alpha), \alpha) = m V - F \delta^ {*} (\alpha) B ^ {\prime} (t ^ {*} (\alpha)) - (m (1 - \alpha) + \alpha e) \\ \cdot k (\delta^ {*} (\alpha)) (B ^ {\prime} (t ^ {*} (\alpha)) t ^ {*} (\alpha) + B (t ^ {*} (\alpha))) \equiv 0; \end{array}
$$

$$
\Psi^ {2} (t ^ {*} (\alpha), \delta^ {*} (\alpha), \alpha) = - F - (m (1 - \alpha) + \alpha e) k ^ {\prime} (\delta^ {*} (\alpha)) t ^ {*} (\alpha) \equiv 0.
$$

By the chain rule, we get

$$
\Psi_ {1} ^ {1} (t ^ {*}, \delta^ {*}, \alpha) \frac {d t ^ {*}}{d \alpha} + \Psi_ {2} ^ {1} (t ^ {*}, \delta^ {*}, \alpha) \frac {d \delta^ {*}}{d \alpha} + \Psi_ {\alpha} ^ {1} (t ^ {*}, \delta^ {*}, \alpha) = 0,
$$

$$
\Psi_ {1} ^ {2} (t ^ {*}, \delta^ {*}, \alpha) \frac {d t ^ {*}}{d \alpha} + \Psi_ {2} ^ {2} (t ^ {*}, \delta^ {*}, \alpha) \frac {d \delta^ {*}}{d \alpha} + \Psi_ {\alpha} ^ {2} (t ^ {*}, \delta^ {*}, \alpha) = 0,
$$

where $\Psi_1^1 = 2k(\delta^*)B'(t^*) + k(\delta^*)B''(t^*)t^* - k'(\delta^*)\delta^*B''(t^*)t^*$ , $\Psi_2^1 = B(t^*)k'( \delta^*)$ , $\Psi_{\alpha}^{1} = ((e - m)k(\delta^*)(B(t^*) + B'(t^*)t^*)) / (m(1 - \alpha) + \alpha e)$ , $\Psi_1^2 = k'( \delta^*)$ , $\Psi_2^2 = k''(\delta^*)t^*$ , and $\Psi_{\alpha}^{2} = ((e - m)k'( \delta^*)t^*) / (m(1 - \alpha) + \alpha e)$ .

By Cramer's rule, we solve the system of equations and get

$$
\frac {d t ^ {*}}{d \alpha} = \frac {\left| \begin{array}{c c} - \Psi_ {\alpha} ^ {1} & \Psi_ {2} ^ {1} \\ - \Psi_ {\alpha} ^ {2} & \Psi_ {2} ^ {2} \end{array} \right|}{\left| \begin{array}{c c} \Psi_ {1} ^ {1} & \Psi_ {2} ^ {1} \\ \Psi_ {1} ^ {2} & \Psi_ {2} ^ {2} \end{array} \right|} \quad \text {and} \quad \frac {d \delta^ {*}}{d \alpha} = \frac {\left| \begin{array}{c c} \Psi_ {1} ^ {1} & - \Psi_ {\alpha} ^ {1} \\ \Psi_ {1} ^ {2} & - \Psi_ {\alpha} ^ {2} \end{array} \right|}{\left| \begin{array}{c c} \Psi_ {1} ^ {1} & \Psi_ {2} ^ {1} \\ \Psi_ {1} ^ {2} & \Psi_ {2} ^ {2} \end{array} \right|}.
$$

Using the second order condition for maximization, the matrix in the denominator in these two expressions is a negative semidefinite matrix. Therefore, this matrix must have a positive determinant, that is

$$
\left| \begin{array}{c c} \Psi_ {1} ^ {1} & \Psi_ {2} ^ {1} \\ \Psi_ {1} ^ {2} & \Psi_ {2} ^ {2} \end{array} \right| > 0.
$$

We have

$$
\left| \begin{array}{c c} - \Psi_ {\alpha} ^ {1} & \Psi_ {2} ^ {1} \\ - \Psi_ {\alpha} ^ {2} & \Psi_ {2} ^ {2} \end{array} \right| = \frac {e - m}{m (1 - \alpha) + \alpha e} t (B (k ^ {\prime}) ^ {2} - B ^ {\prime} t k ^ {\prime \prime} k - k ^ {\prime \prime} k B).
$$

From this expression, the term $t(B(k')^{2}-B'tk''k-k''kB)<0$ , and if m>e, then

$$
\left| \begin{array}{c c} - \Psi_ {\alpha} ^ {1} & \Psi_ {2} ^ {1} \\ - \Psi_ {\alpha} ^ {2} & \Psi_ {2} ^ {2} \end{array} \right| > 0.
$$

Therefore, $dt^{*} / d\alpha > 0$ , when $m > e$ . If $m \leq e$ , then

$$
\left| \begin{array}{c c} - \Psi_ {\alpha} ^ {1} & \Psi_ {2} ^ {1} \\ - \Psi_ {\alpha} ^ {2} & \Psi_ {2} ^ {2} \end{array} \right| \leq 0,
$$

and $dt^{*} / d\alpha \leq 0$

Furthermore, we have

$$
\left| \begin{array}{c c} \Psi_ {1} ^ {1} & - \Psi_ {\alpha} ^ {1} \\ \Psi_ {1} ^ {2} & - \Psi_ {\alpha} ^ {2} \end{array} \right| = \frac {e - m}{m (1 - \alpha) + \alpha e} k ^ {\prime} (k (B - B ^ {\prime} t) + t ^ {2} B ^ {\prime \prime} (k ^ {\prime} \delta - k)).
$$

From this expression, the term $k'(k(B-B't)+t^{2}B''(k'\delta-k))>0$ , and if m>e, then

$$
\left| \begin{array}{c c} \Psi_ {1} ^ {1} & - \Psi_ {\alpha} ^ {1} \\ \Psi_ {1} ^ {2} & - \Psi_ {\alpha} ^ {2} \end{array} \right| <   0.
$$

Therefore, $d\delta^{*}/d\alpha < 0$ , when m > e. If $m \leq e$ , then

$$
\left| \begin{array}{c c} \Psi_ {1} ^ {1} & - \Psi_ {\alpha} ^ {1} \\ \Psi_ {1} ^ {2} & - \Psi_ {\alpha} ^ {2} \end{array} \right| \geq 0,
$$

and $d\delta^{*} / d\alpha \geq 0$ .

By replacing m = N/4, we have that if N > 4e, then $dt^{*}/d\alpha > 0$ and $d\delta^{*}/d\alpha < 0$ , and if $N \leq 4e$ , then $dt^{*}/d\alpha \leq 0$ and $d\delta^{*}/d\alpha \geq 0$ .

Hence, we have Propositions 1 and 2. $\square$

PROOF OF COROLLARY 1. According to the envelope theorem, at optimality, $d\pi^{*} / d\alpha = \partial \pi^{*} / \partial \alpha = (N / 4 - e)k(\delta^{*})B(t^{*})t^{*}$ .

Since k > 0, $B(t) > 0$ , and t > 0 for all values in the feasible parameter space, we have $d\pi^{*}/d\alpha > 0$ when e < N/4 and $d\pi^{*}/d\alpha \leq 0$ when $e \geq N/4$ . Hence, we have Corollary 1. ☐

PROOF OF PROPOSITION 3. Note that the social welfare function in (4) can be represented by $S(t, \delta) = f(t, \delta; N/2, \alpha)$ , where $f(t, \delta; m, \alpha) = m(V - (1 - \alpha)k(\delta)B(t))t - FB(t)\delta - \alpha e k(\delta)B(t)t$ is defined in the proof for Propositions 1 and 2. This means $S(t, \delta) = f(t, \delta; m, \alpha)$ , where $m = N/2$ . Thus, if $m > e$ , which is $N > 2e$ , then $dt^S / d\alpha > 0$ and $d\delta^S / d\alpha < 0$ ; if $m < e$ , which is $N \leq 2e$ , then $dt^S / d\alpha \leq 0$ and $d\delta^S / d\alpha \geq 0$ . Hence, we have Proposition 3.

PROOF OF PROPOSITION 4. As defined in the proof of Propositions 1–3, the vendor's profit is $\hat{\pi}(t, \delta) = f(m = N/4)$ , and the social welfare function is $S(t, \delta) = f(m = N/2)$ . From (6) and (7), we can write $\delta^{*} = \delta^{*}(m)$ and $t^{*} = t^{*}(m)$ , which exist and are differentiable, and satisfy the following identity equations:

$$
\begin{array}{r l} \Psi^ {1} (t ^ {*} (m), \delta^ {*} (m), m) = & m V - F \delta^ {*} (m) B ^ {\prime} (t ^ {*} (m)) - (m (1 - \alpha) + \alpha e) \\ & \cdot k (\delta^ {*} (m)) (B ^ {\prime} (t ^ {*} (m)) t ^ {*} (m) + B (t ^ {*} (m))) \equiv 0; \end{array}
$$

$$
\Psi^ {2} (t ^ {*} (m), \delta^ {*} (m), m) = - F - (m (1 - \alpha) + \alpha e) k ^ {\prime} (\delta^ {*} (m)) t ^ {*} (m) \equiv 0.
$$

We differentiate these two identity equations with respect to $m$

$$
\begin{array}{l} \frac {d \delta^ {*}}{d m} B (t) k ^ {\prime} (\delta) + \frac {d t ^ {*}}{d m} (k (\delta) (2 B ^ {\prime} (t) + t B ^ {\prime \prime} (t)) - t \delta k ^ {\prime} (\delta) B ^ {\prime \prime} (t)) \\ = \frac {\alpha e B (t) k (\delta) + t B ^ {\prime} (t) (\alpha e k (\delta) - (m (1 - \alpha) + \alpha e) \delta k ^ {\prime} (\delta))}{m (m (1 - \alpha) + \alpha e)}, \\ \frac {d t ^ {*}}{d m} B (t) k ^ {\prime} (\delta) + \frac {d \delta^ {*}}{d m} t B (t) k ^ {\prime \prime} (\delta) = - \frac {t (1 - \alpha) B (t) k ^ {\prime} (\delta)}{m (1 - \alpha) + \alpha e}. \end{array}
$$

By solving the two equations, we obtain $d\delta^{*} / dm > 0$ and $dt^{*} / dm > 0$ for $\alpha \in [0,1]$ .

Furthermore, we observe that in the proof for Propositions 1 and 2, both $dt^{*}/d\alpha$ and $d\delta^{*}/d\alpha$ have a common coefficient, $C(m)=(e-m)/(m(1-\alpha)+\alpha e)$ , and the value of the remaining components of $dt^{*}/d\alpha$ and $d\delta^{*}/d\alpha$ do not change when $\alpha$ is fixed. Since the socially efficient solution is associated with $m = N / 2$ , the vendor's optimal solution is associated with $m = N / 4$ , and $|C(m = N / 2)| > |C(m = N / 4)|$ , we have $0 < dt^{*} / d\alpha < dt^{S} / d\alpha$ and $d\delta^{S} / d\alpha < d\delta^{*} / d\alpha < 0$ when $N > 4e$ .

This leads to $d(B(t^{S})(1-\delta^{S}))/d\alpha > d(B(t^{*})(1-\delta^{*}))/d\alpha > 0$ , which means the number of unpatched defects $B(t^{S})(1-\delta^{S})$ is increasing at a faster rate than the monopolist's optimal strategy when N > 4e.

To verify the existence of conditions where $B(t^S)(1 - \delta^S) > B(t^*)(1 - \delta^*)$ , we substitute $B(t) = t^2$ , $k(\delta) = 2 - \delta(2 - \delta)$ , $N = 5$ , $F = 1$ , $e = 1$ , and $V = 2$ . We find that when $\alpha = 0$ , $t^S = 0.701$ , $\delta^S = 0.715$ , $B(t^S)(1 - \delta^S) = 0.140$ , and $t^* = 0.622$ , $\delta^* = 0.357$ , and $B(t^*)(1 - \delta^*) = 0.249$ . Therefore, the number of defects after patching under the socially efficient solution is fewer than that under the vendor's optimal solution, $B(t^S)(1 - \delta^S) < B(t^*)(1 - \delta^*)$ , at $\alpha = 0$ . We also checked that when $\alpha = 0.9$ , $t^S = 0.973$ , $\delta^S = 0.553$ , and $B(t^S)(1 - \delta^S) = 0.423$ , and $t^* = 0.673$ , $\delta^* = 0.276$ , and $B(t^*)(1 - \delta^*) = 0.328$ . It is reversed, $B(t^S)(1 - \delta^S) > B(t^*)(1 - \delta^*)$ , at $\alpha = 0.9$ . Furthermore, it can be verified that $B(t^S)(1 - \delta^S) > B(t^*)(1 - \delta^*)$ when $\alpha > 0.708$ , and $B(t^S)(1 - \delta^S) \leq B(t^*)(1 - \delta^*)$ when $\alpha \leq 0.708$ .

Therefore, there exist conditions under which the number of software defects after patching is lower under the monopolist's optimal strategy relative to the socially efficient solution. Hence, we have Proposition 4. $\square$

## Robustness Check for General Distribution of $\theta$

We assume that $\theta$ is distributed on the interval $[0, \bar{\theta}]$ , with a probability distribution function $g()$ and a cumulative distribution function $G()$ . We also assume that the hazard function, $g(\theta) / (1 - G(\theta))$ , is nondecreasing in $\theta$ . Let $Z = [V - (1 - \alpha)B(t)k(\delta)]t$ . Then, the demand for the SaaS software can be written as $N(1 - G(\hat{\theta}))$ , where $\hat{\theta} = p/Z$ is the indifferent consumer type. The vendor's profit function is $\pi = pN(1 - G(\hat{\theta})) - \alpha eB(t)k(\delta)t - FB(t)\delta$ . The optimal price $p^*$ is the solution to the following FOC:

$$
(1 - G (\hat {\theta})) - \frac {p}{Z} g (\hat {\theta}) = 0.\tag{8}
$$

Since $g(\theta) / (1 - G(\theta))$ is nondecreasing in $\theta$ , this ensures a unique solution, $p^*$ , to the equation in (8). It also ensures a unique $\theta^* = p^* / Z$ .

The vendor's FOCs for $t$ and $\delta$ (envelope theorem) are

$$
\begin{array}{r l} & N \frac {p ^ {2}}{Z ^ {2}} g (\theta^ {*}) (V - (1 - \alpha) k (\delta) (B ^ {\prime} (t) t + B (t))) \\ & \qquad - \alpha e k (\delta) (B ^ {\prime} (t) t + B (t)) - F B ^ {\prime} (t) \delta = 0, \end{array}
$$

$$
N \frac {p ^ {2}}{Z ^ {2}} g (\theta^ {*}) (- (1 - \alpha) k ^ {\prime} (\delta) B (t)) t - \alpha e k ^ {\prime} (\delta) B (t) t - F B (t) = 0.
$$

Using (8) and substituting $s = N\theta^{*}(1 - G(\theta^{*}))$ , we can rewrite the two FOCs as

$$
\begin{array}{r} s V - (s (1 - \alpha) + \alpha e) k (\delta) (B ^ {\prime} (t) t + B (t)) - F B ^ {\prime} (t) \delta = 0, \\ - (s (1 - \alpha) + \alpha e) k ^ {\prime} (\delta) t - F = 0. \end{array}\tag{9}
$$

(10)

These two FOCs are similar to the two FOCs (6) and (7) in the proof for Propositions 1 and 2: $mV - F\delta B'(t) - (m(1 - \alpha) + \alpha e)k(\delta)(B'(t)t + B(t)) = 0$ and $-F - (m(1 - \alpha) + \alpha e)k'(\delta)t = 0$ . The FOCs in Equations (9) and (10) contain $s$ instead of $m$ as in (6) and (7). The proof for Propositions 1 and 2 shows that the impact of $\alpha$ on $t^*$ and $\delta^*$ depends on the relative value of $m$ . Similarly, the impact of $\alpha$ should depend on the relative value of $s$ . Note that $s > e$ can be written as $N > e / (\theta^{*}(1 - G(\theta^{*})))$ . It is easy to show that if $N > e / (\theta^{*}(1 - G(\theta^{*})))$ , then $dt^{*} / d\alpha > 0$ and $d\delta^{*} / d\alpha < 0$ , and if $N \leq e / (\theta^{*}(1 - G(\theta^{*})))$ , then $dt^{*} / d\alpha \leq 0$ and $d\delta^{*} / d\alpha \geq 0$ . This implies that the SaaS vendor releases the software earlier and patches a lower proportion of defects when the market size is sufficiently large ( $N > e / (\theta^{*}(1 - G(\theta^{*})))$ ).

Therefore, our results about the vendor's software release and patching strategy hold in the case where the consumers' taste parameter follows a general distribution.

Hence, we show that Propositions 1 and 2 hold for a general distribution of $\theta$ .

## Robustness Check for Subscription Pricing Scheme

We extend the model in §2 by considering a single patch release, which enhances the software quality. The vendor changes the subscription price immediately after the patch release. We assume that the vendor releases a single patch, and the timing of the patch release is exogenous.

The software is released at time t, and $\delta$ proportion of the defects are patched at time $\beta \times t$ , where $\beta \in (0,1)$ . Recall that time t is measured backward, and the software becomes obsolete at time zero.

The SaaS vendor. The SaaS vendor charges subscription price $p_R$ per unit time from release (t) till patch release ( $\beta t$ ), and charges a subscription price $p_P$ per unit time from patch release ( $\beta t$ ) till software obsolescence.

The consumer surplus per unit time for a type $\theta$ from the release time, t, to the patch-release time, $\beta \times t$ , is

$$
U _ {R} = \theta [ V - (1 - \alpha) B (t) L _ {1} ] - p _ {R}.
$$

We use $L_{1}$ to translate the number of defects at the software-release time to defect-related costs for the consumer type $\theta = 1$ .

The SaaS vendor charges a subscription price $p_P$ per unit time after the patch release. The consumer surplus per unit time for a user of type $\theta$ from the patch-release time to software obsolescence is

$$
U _ {P} = \theta [ V - (1 - \alpha) B (t) L _ {2} (\delta) ] - p _ {P}.
$$

Function $L_{2}(\delta)$ represents the defect-related costs, which are a function of the proportion of defects patched; $L_{2}(\delta)$ is a decreasing function of $\delta$ and the marginal rate of decrease reduces.

The number of defects in the period before the patch release is $B(t)$ , and that after patch release is $B(t)(1-\delta)$ . For the consumer type $\theta=1$ , the defect-related costs $B(t)L_{1}$ per unit time from $B(t)$ defects are incurred for a length of time $(1-\beta)t$ , and the defect-related costs $B(t)L_{2}(\delta)$ per unit time from $B(t)(1-\delta)$ defects are incurred for a length of time $\beta t$ . Thus, the total defect-related costs per unit time are $B(t)(L_{1}(1-\beta)+L_{2}(\delta)\beta)t$ over the lifetime of the software and are equivalent to the total defect-related costs $B(t)k(\delta)t$ in the manuscript.

For tractability, we use $L_{1} = 1$ , $L_{2}(\delta) = (1 - \frac{4}{5}\delta (2 - \delta))$ , and $B(t) = t^2$ . Thus, the consumer surplus per unit time from the release time to the patch-release time is $U_{R} = \theta [V - (1 - \alpha)t^{2}] - p_{R}$ .

The marginal consumer type $\hat{\theta}$ who is indifferent between buying the software and not buying from the release time to the patch-release time is $\hat{\theta} = p_R / (V - (1 - \alpha)t^2)$ . It follows that the demand per unit time from $t$ to $\beta t$ in a market of size $N$ is $q_{R} = N(1 - p_{R} / (V - (1 - \alpha)t^{2}))$ . The cumulative profit of the SaaS vendor from the release time $(t)$ to the patch-release time $(\beta t)$ is $\pi_R = (q_Rp_R - \alpha et^2)(1 - \beta)t = [N(1 - p_R / (V - (1 - \alpha)t^2))p_R - \alpha et^2](1 - \beta)t$ .

The marginal consumer type $\hat{\theta}$ who is indifferent between buying the software and not buying from the patch-release time to software obsolescence is $\hat{\theta} = p_{P} / (V - (1 - \alpha)t^{2}(1 - \frac{4}{5}\delta(2 - \delta)))$ . The demand per period from the patch-release time $\beta t$ to software obsolescence is $q_{P} = N(1 - p_{P} / (V - (1 - \alpha)t^{2}(1 - \frac{4}{5}\delta(2 - \delta))))$ , and the cumulative profit of the SaaS vendor from the patch release to the software obsolescence is $\pi_{P} = [N(1 - p_{P} / (V - (1 - \alpha)t^{2}(1 - \frac{4}{5}\delta(2 - \delta))))p_{P} - \alpha et^{2}(1 - \frac{4}{5}\delta(2 - \delta))] \beta t - Ft^{2}\delta$ .

Summing up the profit per unit time before the patch release and after the patch release, we have the vendor's total profit for the time the software is available in the market

$$
\pi (p _ {R}, p _ {P}, t, \delta) = \pi_ {R} (p _ {R}, t) + \pi_ {P} (p _ {P}, t, \delta).\tag{11}
$$

Solving for the optimal subscription prices to (11), we have $p_R^* = (V - (1 - \alpha)t^2) / 2$ and $p_P^* = (V - (1 - \alpha)t^2(1 - \frac{4}{5}\delta(2 - \delta))) / 2$ , and the demands are $q_R^* = q_P^* = \frac{1}{2}$ . The total subscription price is $t(1 - \beta)p_R^* + t\beta p_p^* = t(1 - \beta)((V - (1 - \alpha)t^2) / 2) + t\beta ((V - (1 - \alpha)\cdot t^2(1 - \frac{4}{5}\delta(2 - \delta))) / 2) = [V - (1 - \alpha)t^2(1 - \beta(\frac{4}{5}\delta(2 - \delta)))]t / 2$ .

Hence, the optimal cumulative profit of the SaaS vendor over the lifetime of the software is

$$
\begin{array}{r} \pi^ {*} (t, \delta) = \frac {t}{2 0} (5 N V - 2 0 F t \delta + (N (1 - \alpha) + 4 \alpha e) \\ \cdot (4 \beta \delta (2 - \delta) - 5) t ^ {2}) t. \end{array}\tag{12}
$$

On-premise software vendor. In the case of traditional on-premises software, the vendor charges a one-time price $p_{on-premise}$ , and the consumer utility is as follows:

$$
\begin{array}{r l} U _ {\text {on - premise}} = & \theta [ V - (1 - \alpha) B (t) L _ {1} ] t (1 - \beta) \\ & + \theta [ V - (1 - \alpha) B (t) L _ {2} (\delta) ] \beta t - p _ {\text {on - premise}}. \end{array}
$$

We use $L_{1}=1$ , $L_{2}(\delta)=(1-\frac{4}{5}\delta(2-\delta))$ , and $B(t)=t^{2}$ , as in the SaaS case. Thus,

$$
\begin{array}{l} U _ {\text {on - premise}} = \theta [ V - (1 - \alpha) t ^ {2} ] t (1 - \beta) \\ \qquad + \theta \bigg [ V - (1 - \alpha) t ^ {2} \bigg (1 - \frac {4}{5} \delta (2 - \delta) \bigg) \bigg ] \beta t - p _ {\text {on - premise}} \\ \qquad = \theta \bigg [ V - (1 - \alpha) t ^ {2} \bigg (1 - \beta \bigg (\frac {4}{5} \delta (2 - \delta) \bigg) \bigg) \bigg ] t - p _ {\text {on - premise}}. \end{array}
$$

The vendor's profit function is $\pi_{\mathrm{on - premise}} = q_{\mathrm{on - premise}} \times p_{\mathrm{on - premise}} - \alpha e t^2 (1 - \beta (\frac{4}{5}\delta (2 - \delta))) t - F t^2 \delta$ .

We solve for the optimal price, $p_{\mathrm{on - premise}}^{*} = ([V - (1 - \alpha)t^{2}(1 - \beta(\frac{4}{5}\delta (2 - \delta)))]t) / 2$ , and the optimal demand is $q_{\mathrm{on - premise}}^{*} = \frac{1}{2}$ . This optimal price is identical to that of the total subscription price in the case of SaaS. The optimal demands are also identical to the optimal demands before and after the patch release in the cases of SaaS, $q_{\mathrm{on - premise}}^{*} = q_{R}^{*} = q_{P}^{*}$ .

The on-premises vendor's optimal profit is $\pi_{\mathrm{on - premise}}^{*}(t,\delta) = (t / 20)(5NV - 20Ft\delta +(N(1 - \alpha) + 4\alpha e)(4\beta \delta (2 - \delta) - 5)t^2)t$ which is identical to the SaaS vendor's optimal profit in Equation (12). This implies that the profit-maximizing problem is identical in the context of the one-time price for on-premises software and in the case of the subscription price per unit time for SaaS, with respect to t and $\delta$ .

Now we derive the Propositions 1 and 2 to show that our results hold when the SaaS subscription price is defined per unit time.

After solving FOCs, we have the following results:

$$
t ^ {*} = \frac {(5 F - 2 a \beta t) ^ {2} + \sqrt {(5 F - 2 a \beta t) ^ {4} + 7 5 a ^ {3} N V (\beta t) ^ {2}}}{1 5 a ^ {2} \beta t},
$$

and $\delta^{*}=1-5F/(2\beta ta)$ , where $a=N(1-\alpha)+4\alpha e>0$ . We assume $2a\beta t-5F>0$ , so that $\delta^{*}>0$ .

Substitute b = N - 4e; we have

$$
\begin{array}{l} \frac {d t ^ {*}}{d \alpha} = \frac {b}{3 0 a ^ {3} \beta t} \\ \qquad \cdot \bigg [ a \beta t \bigg (8 (5 F - 2 a \beta t) - \frac {2 2 5 a ^ {2} N V \beta t - 8 (5 F - 2 a \beta t) ^ {3}}{c} \bigg) \\ \qquad + 4 ((5 F - 2 a \beta t) ^ {2} + c) \bigg ], \\ \text {where} c = \sqrt {(5 F - 2 a \beta t) ^ {4} + 7 5 a ^ {3} N V (\beta t) ^ {2}} > 0. \end{array}
$$

The term inside the square brackets is as follows:

$$
\begin{array}{l} a \beta t \bigg (8 (5 F - 2 a \beta t) - \frac {2 2 5 a ^ {2} N V \beta t - 8 (5 F - 2 a \beta t) ^ {3}}{c} \bigg) \\ \quad + 4 ((5 F - 2 a \beta t) ^ {2} + c) \\ = \frac {1}{c} \cdot (a \beta t (8 (5 F - 2 a \beta t) c - 2 2 5 a ^ {2} N V \beta t + 8 (5 F - 2 a \beta t) ^ {3}) \\ \quad + 4 (5 F - 2 a \beta t) ^ {2} c + 4 (5 F - 2 a t _ {p}) ^ {4} + 3 0 0 a ^ {3} N V (\beta t) ^ {2}) \\ > \frac {1}{c} \cdot \bigg (\bigg (a \beta t - \frac {5}{2} F \bigg) (8 (5 F - 2 a \beta t) c - 2 2 5 a ^ {2} N V \beta t \\ \quad + 8 (5 F - 2 a \beta t) ^ {3}) + 4 (5 F - 2 a \beta t) ^ {2} c + 4 (5 F - 2 a \beta t) ^ {4} \\ \quad + 3 0 0 a ^ {3} N V (\beta t) ^ {2} \bigg) \\ = \frac {1}{c} \bigg (- 4 (2 a \beta t - 5 F) ^ {2} c - 2 2 5 a ^ {2} N V \beta t \bigg (a \beta t - \frac {5}{2} F \bigg) \\ \quad - 4 (2 a \beta t - 5 F) ^ {4} + 4 (5 F - 2 a \beta t) ^ {2} c + 4 (5 F - 2 a \beta t) ^ {4} \\ \quad + 3 0 0 a ^ {3} N V (\beta t) ^ {2} \bigg) \\ = \frac {3 0 0 a ^ {3} N V (\beta t) ^ {2} - 2 2 5 a ^ {2} N V \beta t (a \beta t - (5 / 2) F)}{c} \\ = \frac {7 5 a ^ {2} N V \beta t (a \beta t + (1 5 / 2) F)}{c} > 0. \end{array}
$$

Based on the results, it is clear that the sign of $dt^{*}/d\alpha$ depends on the sign of b. We have if N > 4e, then b > 0 and $dt^{*}/d\alpha > 0$ , and if $N \leq 4e$ , then $b \leq 0$ and $dt^{*}/d\alpha \leq 0$ . Proposition 1 says that $dt^{*}/d\alpha > 0$ when N > 4e, and $dt^{*}/d\alpha \leq 0$ when $N \leq 4e$ .

Since $\delta^{*} = 1 - 5F / (2\beta ta)$ , we have $d\delta^{*} / d\alpha = -5Fb / (2\beta ta^{2})$ . It is clear that if $N > 4e$ , then $b > 0$ and $d\delta^{*} / d\alpha < 0$ , and if $N \leq 4e$ , then $b \leq 0$ and $d\delta^{*} / d\alpha \geq 0$ . Proposition 2 says that $d\delta^{*} / d\alpha < 0$ when $N > 4e$ , and $d\delta^{*} / d\alpha \geq 0$ when $N \leq 4e$ .

Therefore, Propositions 1 and 2 hold in the case where SaaS subscription price is defined per unit time. The results when the SaaS vendor charges a subscription price per unit time are consistent with the results when the vendor charges a total subscription price for SaaS.

## Positive Marginal Cost of Serving Users (c > 0)

The SaaS software vendor may incur a marginal cost $c$ of serving consumers. Without loss of generality, we use a linear demand function $D(p_{mc}) = \alpha - \beta p_{mc}$ to represent the market demand function we defined in §2.2. Thus, under the monopolist vendor's optimal case, the profit function is $\pi(p_{mc}) = (\alpha - \beta p_{mc})(p_{mc} - c) - \phi$ , where $\phi$ is the fixed cost, patch-development cost, and defect-related cost incurred by the vendor. This is equivalent to the profit function in (3). After solving the profit maximization problem, the optimal price is $p_{mc}^{*} = (\alpha + c\beta)/(2\beta)$ , the market demand is $D(p_{mc}^{*}) = (\alpha - c\beta)/2$ , and the vendor's optimal profit is $\pi(p_{mc}^{*}) = (\alpha - c\beta)^{2}/(4\beta) - \phi$ . On the other hand, the socially efficient solution requires the price to be set at the marginal cost $p_{mc}^{s} = c$ . Thus, the market share is $D(p_{mc}^{s}) = \alpha - c\beta$ , and the optimal social welfare is $S(p_{mc}^{s}) = \int_{c}^{\alpha/\beta} (\alpha - \beta p) dp - \phi = (\alpha - c\beta)^{2}/(2\beta) - \phi$ .

It is easy to see that the two demands are $D(p_{mc}^{*}) = (\alpha - c\beta)/2$ and $D(p_{mc}^{s}) = \alpha - c\beta$ , and they decrease as the marginal cost, c, increases. Nonetheless, $D(p_{mc}^{s}) > D(p_{mc}^{s})$ .

Now, we can run a numeric calculation to compare the number of defects after patching between the vendor's optimal solution and the socially efficient solution. We rewrite the profit function in Equation (3) as follows:

$$
\begin{array}{c} \pi = N \bigg (1 - \frac {p}{[ V - (1 - \alpha) B (t) k (\delta) ] t} \bigg) (p - c) \\ - F B (t) \delta - \alpha e B (t) k (\delta) t. \end{array}
$$

When the marginal cost of serving users is positive, the vendor will charge the same price as the marginal cost, c, under the socially efficient case. Thus, only the consumers who have a higher valuation subscribe to the software. The social welfare function in Equation (4) is modified as follows:

$$
\begin{array}{c} S (t, \delta) = N \int_ {c / ((V - (1 - \alpha) B (t) k (\delta)) t)} ^ {1} (\theta (V - (1 - \alpha) B (t) k (\delta)) t - c)   d \theta \\ - F B (t) \delta - \alpha e B (t) k (\delta) t. \end{array}
$$

To be consistent, we take the same functional forms and parameter values used in the proof of Proposition 4: $B(t) = t^2$ , $k(\delta) = 2 - \delta(2 - \delta)$ , $N = 5$ , $F = 1$ , $e = 1$ , and $V = 2$ . We get

$$
\begin{array}{c} \pi (t, \delta) = \frac {1}{4} t (1 0 - 4 t \delta - t ^ {2} (5 - \alpha) (2 - (2 - \delta) \delta)) \\ - \frac {5 c}{2} \bigg (1 - \frac {c}{4 t - 2 t ^ {3} (1 - \alpha) (2 - (2 - \delta) \delta)} \bigg), \end{array}
$$

$$
\begin{array}{c} S (t, \delta) = \frac {1}{2} t (1 0 - 2 t \delta - t ^ {2} (5 - 3 \alpha) (2 - (2 - \delta) \delta)) \\ - 5 c \bigg (1 - \frac {c}{4 t - 2 t ^ {3} (1 - \alpha) (2 - (2 - \delta) \delta)} \bigg). \end{array}
$$

We find that when the vendor's marginal cost is $c = 0.1$ and $\alpha = 0$ , we have $t^S = 0.701$ , $\delta^S = 0.712$ , and $B(t^S)(1 - \delta^S) = 0.141$ , and $t^* = 0.621$ , $\delta^* = 0.348$ , and $B(t^*)(1 - \delta^*) = 0.251$ . Therefore, the number of defects after patching under the socially efficient solution is fewer than that under the vendor's optimal solution, $B(t^S)(1 - \delta^S) < B(t^*)(1 - \delta^*)$ , at $\alpha = 0$ . We also checked that when c=0.1 and $\alpha=0.9$ , $t^{S}=0.972$ , $\delta^{S}=0.552$ , and $B(t^{S})(1-\delta^{S})=0.422$ , and $t^{*}=0.671$ , $\delta^{*}=0.273$ , and $B(t^{*})(1-\delta^{*})=0.327$ . It is reversed, $B(t^{S})(1-\delta^{S})>B(t^{*})(1-\delta^{*})$ , at $\alpha=0.9$ . Furthermore, it can be verified that $B(t^{S})(1-\delta^{S})>B(t^{*})(1-\delta^{*})$ when $\alpha>0.706$ , and $B(t^{S})(1-\delta^{S})\leq B(t^{*})(1-\delta^{*})$ when $\alpha\leq0.706$ .

Therefore, there exist conditions under which the number of software defects after patching is lower under the monopolist's optimal strategy relative to the socially efficient solution with a positive marginal cost. The result of Proposition 4 holds when the marginal cost of serving consumers is positive.

## References

Albanesius C (2011) Netflix issuing 3 percent credit for Tuesday streaming outage. PC Magazine (March 24), http://www.pcmag.com/article2/0,2817,2382533,00.asp.

Anderson R, Moore T (2006) The economics of information security. Science 314(5799):610–613.

Armbrust M, Fox A, Griffith R, Joseph AD, Katz R, Konwinski A, Zaharia M (2010) A view of cloud computing. Comm. ACM 53(4):50–58.

Arora A, Caulkins JP, Telang R (2006) Research note–Sell first, fix later: Impact of patching on software quality. Management Sci. 52(3):465–471.

August T, Tunca TI (2006) Network software security and user incentives. Management Sci. 52(11):1703–1720.

August T, Niculescu M, Shin H (2014) Cloud implications on software network structure and security risks. Inform. Systems Res. 25(3):489–510.

Banker RD, Slaughter SA (1997) A field study of scale economies in software maintenance. Management Sci. 43(12):1709–1725.

Bedigian L (2012) Netflix has a bone to pick with Amazon. Forbes (December 26). http://www.forbes.com/sites/benzingainsights/2012/12/26/netflix-has-a-bone-to-pick-with-amazon/.

Bhargava HK, Choudhary V (2004) Economics of an information intermediary with aggregation benefits. Inform. Systems Res. 15(1):22–36.

Cavusoglu H, Cavusoglu H, Zhang J (2008) Security patch management: Share the burden or share the damage? Management Sci. 54(4):657–670.

Choudhary V (2007) Comparison of software quality under perpetual licensing and software as a service. J. Management Inform. Systems 24(2):141–165.

Clay K (2012) Amazon AWS takes down Netflix on Christmas Eve. Forbes (December 24). http://www.forbes.com/sites/kellyclay/2012/12/24/amazon-aws-takes-down-netflix-on-christmas-eve/.

Jiang Z, Sarkar S, Jacob VS (2012) Postrelease testing and software release policy for enterprise-level systems. Inform. Systems Res. 23(3, part 1):635–657.

Kannan K, Telang R (2005) Market for software vulnerabilities? Think again. Management Sci. 51(5):726–740.

Kim BC, Chen PY, Mukhopadhyay T (2011) The effect of liability and patch release on software security: The monopoly case. Production Oper. Management 20(4):603–617.

Lahiri A (2012) Revisiting the incentive to tolerate illegal distribution of software products. Decision Support Systems 53(2):357–367.

Ma D, Seidmann A (2008) The pricing strategy analysis for the "software-as-a-service" business model. Altmann J, Neumann D, Fahringer T, eds. Grid Economics and Business Models (Springer, Berlin), 103–112.

Mehra A, Seidmann A, Mojumder P (2014) Product life-cycle management of packaged software. Production Oper. Management 23(3):366–378.

Violino B (2009) Why Cowen and Co. moved into the cloud. Information Management (June 15), http://www.information-management.com/news/news/cowen\_cloud\_computing\_sales\_growth-10015599-1.html.
