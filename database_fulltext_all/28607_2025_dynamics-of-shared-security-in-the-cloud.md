---
otero_id: 28607
otero_key: "ZSUA4UZB"
title: "Dynamics of Shared Security in the Cloud"
authors: "Nan Clement; Daniel Arce"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.0256"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Dynamics of Shared Security in the Cloud

Nan Clement,<sup>a,</sup>\* Daniel Arce<sup>b</sup>

<sup>a</sup> Sloan School of Management, Massachusetts Institute of Technology, Cambridge, Massachusetts 02142; <sup>b</sup> School of Economic, Political, and Policy Sciences, University of Texas at Dallas, Richardson, Texas 75080

\*Corresponding author

Contact: nanc@mit.edu, https://orcid.org/0000-0001-5431-5719 (NC); darce@utdallas.edu, https://orcid.org/0000-0003-1702-4570 (DA)

Received: April 27, 2023 Revised: October 30, 2023; May 28, 2024 Accepted: June 12, 2024 Published Online in Articles in Advance: July 29, 2024

https://doi.org/10.1287/isre.2023.0256

Copyright: © 2024 INFORMS

Abstract. Cloud services exist under a shared security environment with a dynamic nature; users trade fixed costs for variable costs over time, and both cloud services providers (CSPs) and users contribute to overall security. We investigate the nature of shared security in a dynamic game where users’ security contributions and cloud usage figure into their CSP’s vulnerability. Furthermore, CSPs’ own security contribution takes into account both their users as well as competition with other CSPs. The Markov perfect equilibrium reveals the long-term time patterns of security of the cloud. In par ticular, we identify a novel form of time-path strategic complementary between usage and a CSP’s Markov state of security. This implies that cloud security is an unusual form of impure public good, whereby individual contributions bolstering a CSP’s security endow a selective incentive (private benefit) on others rather than on the contributor alone. Because this increases usage, CSP vulnerability increases over time. At the same time, CSP competition on security may lead to both welfare improvements fo users and lock-in.

History: Martin Bichler, Senior Editor; Yifan Dou, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.0256.

Keywords: cloud security • cloud competition • cybersecurity • information security • shared security • joint responsibility • lock-in • Markov perfect equilibrium • selective incentives

## 1. Introduction

As more businesses move into the cloud and ransomware becomes a big-game-hunting affair, understanding the dynamic structure of cloud security is necessary for cloud services providers (CSPs) and their users alike. For example, Microsoft presently encourages its business users to take shelter in the cloud, building tools that allow its bread-and-butter products to be used on rival cloud services providers and their associated security solutions (Tilley and McMillan 2022). By contrast, Blumenthal (2011) outlines various ways the cloud might be seen as a “new platform for malice.” For example, data centers provide both economies of scale and large targets for malicious actors. Indeed, cloud data breaches cost more and take longer to identify (IBM 2023). On top of this, CSP use introduces a new type of exposure to insider attacks—those with knowledge of the CSP’s architecture, configuration attributes, and parameters (Cansever 2020). August et al. (2014) describe a middle ground, where software as a service (SaaS) poses less undirected cybersecurity risk as compared with its on-site version but more organizational-level directed cybersecurity risk.<sup>1</sup> Such “diversification” may result in less overall risk. Our focus is on the CSP-user dynamics of directed risk in order to evaluate the consequences of taking shelter in the cloud.

This focus in part stems from new guidance issued by the Joint Cybersecurity Advisory (CSA)—authored by the Cybersecurity and Infrastructure Security Agency, the Federal Bureau of Investigation (FBI), and the National Security Agency—where the importance of the cloud is now on par with enterprise environments.<sup>2</sup> The CSA also has an accompanying analysis report (AR21-013A) for further cloud security guidance. All proposed solutions require cloud users to do more to defend their services.<sup>3</sup> Similarly, in the online summit discussing their inaugural Cloud Risk Report (Crowdstrike 2023), Crowdstrike warns that the cloud is the new attack surface because of the way the cloud ends up being the platform for securing multiple forms of computing. Palo Alto Networks (2023) takes it a step further, calling the cloud the dominant attack surface, owing to findings in its “Unit 42 attack surface threat report” that 80% of medium, high, or critical exposures are on assets in the cloud for the organizations analyzed.

The cloud security environment embodies shared security (Tianfield 2012, Almorsy et al. 2016, Al-Otaibi 2021) and joint responsibility (Tajalizadehkhoob et al. 2017)

because both CSPs and users contribute to overall security. Throughout our paper, the term user refers to a firm with a service-level agreement with their CSP. Simply put, shared security and joint responsibility involve security of the cloud, referring to CSPs’ responsibilities toward securing hardware, global infrastructure, virtual machine images within repositories, etc., versus security in the cloud, referring to users’ responsibilities for securing their own network, firewall configurations, etc. Misconfigurations at the interfaces between user and CSP are often susceptible to exploitation, such as in the 2019 Capital One breach on Amazon Web Services (AWS) by a former AWS employee. Another example is users leaving CSP’s default passwords intact. Users must also ensure that they correctly deactivate unused sites in the cloud; otherwise, the sites remain unmaintained with out-of-date security. Data security is an area of joint responsibility for CSPs and users. In addition, the multitenant nature of the cloud implies an interdependent security problem for all users, and it lends itself to class breaks (Arce 2020). Many, if not all, of the major CSPs are known to have had critical crosstenant vulnerabilities, thereby violating cloud isolation (Wiz 2023). Supply chain attacks, such as the Solar Winds intrusion, allow malicious actors to effectively jump between tenants as can faulty or malicious code in execution environments, like platform as a service (PaaS). Multitenancy also facilitates adversaries living off the same cloud as users because the traffic looks similar to CSPs.

We employ a dynamic game to characterize how shared security contributes to a CSP’s security umbrella. By security umbrella, we mean the way that a CSP’s walled garden encourages users to conduct ever more value-producing activities within the cloud because of their familiarity with operating within the walled garden and the tools that CSPs provide for doing so. An example is a CSP employing homomorphic encryption to protect users’ data and allow users to process their data without a key while using various applications.

Dynamic game theory differs from the dynamics associated with repeated games, where the same-stage game occurs in each period. Instead, in a given period, a CSP’s and its users’ security contributions, along with users’ usage of the CSP to create value, may lead to a different game in the subsequent period. Specifically, such choices lead to different states of security and vulnerability in the Markov sense. Given the general dynamic structure of the game under analysis, the approach does not lend itself to explicitly deriving equilibrium strategies or payoffs unless we make strong assumptions about the underlying payoffs. We do not employ such restrictions; the payoff functions in our game are additively separable but are not linear in past, current, or future states. Consequently, equilibrium strategies and payoffs are not derived; instead, we characterize them in terms of Markov perfect equi librium (MPE) and the associated Euler equation. In a dynamic game, strategies are linked over time, and the Euler equation characterizes the evolution of CSP vulnerability given optimal dynamic behavior by CSPs and their users. The Euler equation is useful for characterizing long-term convergence and patterns in CSP vulnerability. These are timely and important issues given that the economics of the cloud are inherently dynamic.

Specifically, operating in the cloud is a decision to trade fixed costs for variable costs, where the latter costs are determined over time on a pay-as-you-go basis, thereby providing flexibility for on-demand variations in capacity at a granular level. Trading fixed costs means that users substantially scale back on fixed information technology (IT) investments and current in-house capacity in order to avoid losses from being over or under IT capacity. Capital expenditures are replaced by operating expenses to better align costs with the dynamics of resource demands. Choosing the cloud is, therefore, a dynamic strategy for users because cloud usage is meant to bear fruit over time through continued reliance on cost savings in the cloud. In view of this, cloud users do not cycle between cloud and enterprise environments on a transitory basis; the economics of neither would pay off. Hence, in contrast to a one-time either/or analy sis of cloud/enterprise choice, our users are in the cloud and expect to be in the cloud for the foreseeable future.

As such, if the likelihood that a user persists in the cloud for the next period is nonzero for every period, then an infinite horizon model is appropriate because neither the user nor the CSP can say with certainty when their relationship will end. In addition, CSPs profits increase when users increase usage, and users only increase usage if they are convinced about operating under the security umbrella. If usage changes over time, the Markovian states of security and vulnerability change as well. Such a modeling approach is consistent with the current reality in which in any given month, 20% of an organization’s cloud attack surface is taken offline and replaced with new or updated ser vices (Palo Alto Networks 2023). Again, this rules out a repeated game approach, where the states do not change by definition, in favor of a dynamic game approach, which is the modeling environment that we investigate. Moreover, once committed to the cloud, a user’s next-best alternative is another CSP. Over time, CSPs are, therefore, also in the business of keeping their users from switching to another CSP and getting users from other CSPs to switch to them, which are other dynamic facets of our model corresponding to cloud economics.

In particular, the security umbrella produces a form of lock-in different from using security and tamper resistance to explicitly hinder users’ ability to switch

CSPs (e.g., Anderson 2001, Lookabaugh and Sicker 2004, Arce 2022). Such lock-in is anticompetitive (Opara-Martins et al. 2014, 2016; Asghari et al. 2016), causing users to employ antilock-in strategies, such as hybrid clouds, cloud management providers or brokers, and regular manual data exportation (Arce 2022). In such scenarios, the CSP works toward lock-in, and users work against it. By contrast, we study an environment corresponding to a CSP’s and its users’ contributions to shared security to create a security umbrella enhancing the value proposition for users. This is in the interest of both users and CSPs. Finally, a thriving user base or CSP may become a more attractive target for malicious actors.

We derive our findings by exploiting the no-switching criterion used both in analyses of lock-in in IT (e.g., Shapiro and Varian 1998, Varian 2004a) and more recently, in platform economics. Specifically, the no-switching criterion is a means for establishing conditions necessary for nonmonopolistic outcomes in platform (or two-sided) markets (e.g., Lee 2014, Arce 2020). From the two-sided markets perspective, cloud services, such as infrastructure as a service (IaaS) and SaaS, are examples of platforms in addition to PaaS. By observation, most platform markets and certainly, the market for CSP services within the cloud stack are not monopolistic. In our model, two CSPs compete by providing a security umbrella that they and their users contribute to. The no-switching constraint both places economic pressure on a CSP’s security provision and enables the characterization of a nonmonopolistic equilibrium outcome where CSPs coexist. In invoking the no-switching criterion, we do not deny that users switch CSPs; they clearly do. Nevertheless, the no-switching criterion has the dual benefit of formalizing how lock-in occurs owing to the user’s value added from the resulting security umbrella and placing CSPs within a competitive structure where security is costly but economically necessary to reduce the potential for users to switch.

Our analysis yields several novel findings. First, after specifying the model itself, a user’s investment in security and that of other users and its CSP are shown to be strategic substitutes. Strategic substitutes are a property of best replies, indicating that it is optimal for a user to decrease its security investment if other users or its CSP increase their security investment. Although strategic substitutes are somewhat expected, the way that others security investments directly affect a user’s per period payoff function varies according to the degree that a user is locked in under a CSP’s security umbrella. Specifically, if a user is not locked in, others’ security investment increases a user’s per period payoff function (known as plain complements). However, over time, a user’s per period payoff can decrease in others’ security investments (known as plain substitutes) because security investments build on each other, thereby increasing the potential for a user to be locked in under the CSP’s security umbrella.

Second, future vulnerability affects a user’s currentperiod decisions regarding its security investment and CSP usage. Specifically, without consideration of future vulnerability, the components of current-period vulnerability change in terms of more current-period usage and less current-period security investment. Indeed, our characterization of the equilibrium via a Euler equation shows that current-period restraint in recognition of its implication for future vulnerability keeps the time path of cloud vulnerability from exploding. The message for managers of CSP users is that decisions regarding both security and usage should account for their relationship with each other and their implications for future vulnerability.

Third, CSP usage increases with the accumulation of security. The direct implication for CSP managers is that security is part of the CSP’s value proposition, which is based on usage fees. A more subtle but highly consequential implication is that security creates previously unidentified selective incentives (private benefits). Specifically, any contribution enhancing the security umbrella—a local public good for the CSP and its users—also increases usage, which is a private benefit. It, therefore, follows that the benefit need not stem only from a user’s own contribution to security. In particular, other users’ security investment or the CSP’s security investment increases a user’s private benefit stemming from increased usage. As the extant literature often focuses on the publicness of cybersecurity or its associated externalities, this private benefit has largely gone unacknowledged. Cloud security is, therefore, an impure public good.

Originating with the seminal treatise of Olson’s (1965), The Logic of Collective Action: Public Goods and the Theory of Groups, selective incentives associated with the provision of public goods are known to increase voluntary contributions. Within groups, the public benefit is often called a collective benefit, and the selective incentive is a noncollective benefit. For example, lobbying by AARP (a collective benefit for all U.S. retirees) is funded by AARP member contributions, and offering private benefits to contributing members, such as discounted insurance and vacation tours, is a noncollective benefit. A nonmonetary example is the “warm glow” that an individual may get as a form of private psychic benefit from voluntarily contributing to a public good (Andreoni 1990). The combination of public goods with selective incentives is known as impure public goods or joint products because the process of creating the public good results in both public and private benefits (Cornes and Sandler 1994). International security alliances are among the most widely studied examples of impure public goods. The security created for members of the alliance is the public good. The ability of domestic troops to not only defend alliance members but also conduct nonmilitary activities, such as disaster relief, in the homeland is a selective incentive. Similarly, the presence of selective incentives stemming from contributions to the security umbrella makes the environment more conducive to collective action. Yet, the resulting increase in usage because of increasing security also increases vulnerability because increasing usage raises the CSP’s attractiveness to malicious actors. This distinction between security and vulnerability does not exist in the economic literature on traditional security, but it has been part and parcel of cybersecurity at least since the work of Gordon and Loeb (2002).

We analyze the shared provision of cybersecurity within a group of users and their CSP, which competes with another CSP. As such, several contributions to the economics literature on public goods result. To begin, contributions to shared security in the cloud produce the security umbrella, providing a public benefit to CSP and users alike by reducing the probability of a breach. Furthermore, users and CSPs conduct their business under the security umbrella. Such business benefits are private to each entity. Yet, the resulting joint products are substantially different from the canonical economic model of selective incentives, where the private benefit is directly linked to one’s own contribution and no one else’s contribution. Here, lowering the probability of a breach is the public benefit, and the private benefit— generating profit under the security umbrella—is not limited to the contributor. Nor is it a function of the contributor’s contribution to the security umbrella. Instead, it is a function of users’ usage and CSP’s charging for usage. Hence, the private benefit is less selective in terms of accruing to the contributor only, but the analysis remains within the categories of impure public goods and joint products. This is the special nature of the benefits of cybersecurity; it is unlike other forms of product differentiation in that cybersecurity is the public good protecting both the private benefits that users receive from using their CSP and the CSP’s ability to generate its own private benefits by charging for the usage that creates users’ benefits. AWS’s stance that security is a major component of the cloud rather than an auxiliary operation (Gariba and Van Der Poll 2017) is consistent with this view.

In addition, the dynamic environment differs from the usual settings for examining impure public goods. In a single-shot setting, players do not base their actions on the past history of playing the game or consider the future implications of their actions on another iteration of the game. In a repeated-game setting, the same-stage game occurs in each period; hence, by definition, the players’ strategies cannot change the Markovian state—the vulnerability of the CSP and its users as well as the level of security—over time. By contrast, the dynamics of our analysis allow for the

Markovian state to change, making the model one of the dynamic joint products (impure public goods over time). Consequently, players’ strategies are both a function of the past history of play and how current decisions influence the future state of play. Private benefits (profits) earned under the security umbrella as an impure public good change over time as well. The result is a novel form of time-path complementarity between usage and shared security measures. Consequently, in our analysis, both decisions and the economic environment are dynamic, consistent with cloud economics and the continuing relationship between CSPs and their users. Together, results on the statespace dynamics of security and vulnerability in the cloud, combined with our contribution to the economic theory of public goods, imply that cloud security is an atypical form of impure public good, wherein individ ual contributions to bolster CSP security endow a selective benefit on others, thereby increasing usage but also exacerbating CSP vulnerability over time.

We now turn from the public goods-security nexus to a fourth contribution of the paper; the welfare implications of the shared security paradigm are somewhat startling. Specifically, user lock-in is often viewed nega tively. Hence, the idea that a CSP’s security umbrella may lead to lock-in is concerning. Indeed, we show that users can be locked in by a less secure, more vulnerable CSP owing to users’ familiarity with the CSP’s security umbrella. At the same time, however, the level of secu rity required to lock in users can exceed the level of security necessary to satisfy users’ participation constraint (PC). This is a welfare improvement for users caused by the lock-in produced by the CSP’s contributions to the security umbrella in order to keep users from switching. The reasoning has to do with CSP secu rity competition resulting in strategic complements, a phenomenon that we now turn to.

Thus far, the contributions of the paper are stated in terms of CSP-user and user-user relationships. As we also consider CSP competition, a fifth contribution is the finding that the level of security of a CSP’s competitor and the level of security necessary for a CSP to continue existing (satisfy the no-switching constraint for its users) are strategic complements. The implication is that in each period, CSPs change their optimal level of security investment in the same direction. Importantly, CSP security competition is tempered; it is neither a race to the bottom because security must satisfy the no-switching constraint nor a war of increasing security levels because a CSP needs to only partially increase its security in response to increased security by its competitor owing to user lock-in under its security umbrella.

The analysis proceeds as follows. We survey closely related research in Section 2 and present our model in Section 3. Section 4 focuses on the optimal path of accumulated vulnerability stemming from users’ optimal

CSP usage under the security umbrella. Because the path does not need to converge to a stationary state, we analyze the path of vulnerability in equilibrium. We further characterize user behavior along the CSP’s time path of vulnerability. In so doing, we provide a novel characterization of security in the cloud as a form of impure public good. In Section 5, we address whether CSP security competition can improve the situation. We present results demonstrating how the security umbrella functions as a form of lock-in, how it influences the non-monoplistic nature of CSP markets, and how it generates welfare improvements for users. In Section 6, we show that our characterizations are robust to specifying security within the CSP as determined by the lowest contributor (weakest link) as well as to quadratic costs of security investment. Section 7 concludes with implications for managers, social planners, regulators, and potential extensions. In total, the message not only is that the cloud is a joint security environment but also that it is a dynamic joint security environment resulting in impure public goods.

## 2. Related Literature

The relationships between CSPs and their users are undeniably complex. This is further complicated by the actions of malicious actors when it comes to cloud security. Consequently, all theoretical analyses of the cloud, including our analysis, focus a magnifying glass on the facets of interest in order to better understand their contribution to the broader picture.

This section reviews related studies that our analysis builds upon in order to capture the shared security implications of continuing relationships between CSPs and their users and ongoing competition between CSPs. Furthermore, like our study, these studies are expressed in terms of economic relationships rather than in terms of the underlying hardware and software architectures of the cloud.

For example, in August et al. (2014), the facet under magnification is the difference between the externality associated with indirect attacks on users within an organization employing patchable on-site software versus the externality associated with directed attacks on organizations subscribing to the SaaS version. Our study complements their focus on the patching actions of on-site software users by instead examining the security interaction between CSPs and CSP users, consistent with taking shelter in the cloud. Furthermore, their game is dynamic as it is in extensive (multistage) form, whereas the time dimension is static as the game is played but once (single shot). It is consistent with an either/or decision to use on-site software or its cloud version. By contrast, we study a game in extensive form with a time dynamic meant to capture the continuing relationship between CSP and user, consistent with cloud economics, and additionally, we consider the possibility that users may switch CSPs. Hence, the extensive form played at any point in time varies according to the state variables determined by prior play.

In contrast to the August et al. (2014) analysis of on-site versus SaaS versioning within a monopoly setting, Zhang et al. (2020) consider security and customization competition between on-site software and SaaS monopolies. SaaS is less customizable than its on-site competitor and involves a usage fee. These two facets discourage usage in such a way that a high-security loss environment leads to lower expected losses for SaaS users as compared with a low-security-loss on-site environment with greater usage. The implication fo the on-site vendor is that in low-loss environments, security and customization are substitute inputs but that under high-loss environments, they are complementary inputs. Once again, the analysis is in terms of a single-shot extensive-form game. It implies a negative security externality only, whereas the time dynamics under investigation in our analysis additionally allow for both the possibility of switching and benefits (selective incentives) to accrue from continued operation under a CSP’s security umbrella. The latter can lead to lock-in, which again, is a dynamic phenomenon.

Although the competitive environments of August et al. (2014) and Zhang et al. (2020) consider a single monopoly producing on-site and cloud versions or an on-site monopoly competing with a cloud monopoly, two studies consider the role of cybersecurity in determining nonmonopolistic outcomes. Arce (2020) subjects security to the same two-sided market disciplinary forces shaping a CSP’s pricing structure and other strategies. In particular, security must satisfy (i) no-switching constraints for users and (ii) CSP incentive compatibility constraints that are functions of the crossplatform distri bution of users. Security or lack thereof is an influential predictor of users’ switching behavior (Wilms et al. 2018). By comparing the level of security to keep current users from switching with the level of security needed to acquire additional users, Arce (2020) characterizes when a CSP market is imperfectly competitive versus monopolistic. The novelty is the characterization in terms of security (i.e., a symbiosis exists between CSP market structure and security). The dynamics consid ered are coalitional (relating to whether users switch o not). There is no time dimension.

By contrast, Sen et al. (2020) consider a coupled pair of differential equations for the market share of competing software vendors. The rate of change of a vendor’s market share is increasing in the adoption rate of new users “birthed” into the market. It is decreasing in the rate of existing users switching to the competition and increasing in the rate of users switching from the competition, with the propensity to switch given exogenously. Finally, the amount of hacking directed at the vendor restrains market share. Monopoly is possible with or without hacking, but imperfect competition is only possible under the presence of hackers. Hence, rather than viewing hackers as unilaterally bad, their presence can foster security competition within the software market, meaning duopoly or oligopoly rather than monopoly. In Sen et al. (2020), there are differences in hacker propensities to target a particular vendor but no competition in terms of costly vendor investment in cybersecurity over time. Our study includes the latter.

More to the point, security-enhancing actions are not part of cloud users’ strategy sets in August et al. (2014), Arce (2020), Sen et al. (2020), or Zhang et al. (2020). To wit, there is no shared security. Here, CSPs compete on the basis of security, and their respective users take security-enhancing actions, as prescribed by users’ and CSPs’ shared responsibilities, CSA’s security guidance, and Crowdstrike’s and Palo Alto Networks’ characterizations of the cloud as attack surface.

Our research adds to various aspects of the literature on public goods by exploring dynamic collective action among asymmetric contributors, where individual benefits hinge on a probabilistic public good. Cornes and Sandler (1994) demonstrate that for impure public goods, where individual contributions yield both public and private benefits, contributions become strategic complements instead of strategic substitutes. In cloud security, individual contributions reduce breach probabilities, a public good, allowing for users and CSPs to generate private benefits in the form of profits. Here, individual security contributions can be strategic complements or substitutes depending upon the underlying dynamics.

In this way, our analysis establishes the dynamics of cloud security as a distinct paradigm from dynamic public goods games in economics, which primarily examine global environmental concerns, such as climate change or carbon emissions, culminating in analyses such as Harstad (2012) and Battaglini and Harstad (2016). These are modeled as either a public good or commons. The difference is that for a public good, players’ actions generate a public benefit at a private cost, with the cost resulting from the individual’s action only. In a commons (Ostrom 1990), players’ actions generate a public cost and a private benefit, with the benefit resulting from an individual’s action only. By definition, the global nature of the public good or commons does not generate impure public goods, joint products, or selective incentives. By contrast, in the present analysis, one cannot ignore that the very purpose of contributing to the cloud security umbrella as public good is the profits generated by operating the cloud or within the cloud. The model, therefore, includes public benefits and private costs, and in addition, it includes a private benefit (profits) that is a selective incentive contingent on the public benefit (security umbrella). Moreover, because the aforementioned environmental problems are global, players are treated as identical. Here, the CSP and its users have obvious asymmetries and do not have identical profit functions. Users privately benefit from using the cloud. CSPs benefit from charging for usage and attempt to lock in users. There is, therefore, no global counterpart to the Euler equation that we derive for CSP vulnerabil ity, which stems from the reality of user-CSP asymmetry in the first place, if shared security is to have any mean ing whatsoever, and the CSP’s and users’ selective incen tives for contributing to security. The Euler equation characterizes the intertemporal relationship between selective incentives and contributions to the security umbrella in terms of the time path of vulnerability. Furthermore, the security umbrella is localized to the CSP and its users. There is no analog to switching from one CSP to another for global public goods or commons. Nor is there any global analog to CSPs competing with each other on the basis of security, with the potential for switching that affects CSPs’ security levels.

Finally, dynamic public goods games are plagued by free riding, which is normally addressed through reward and punishment strategies as part of international protocols. Here, no such carrots and sticks are needed because the natural presence of selective incentives under the security umbrella encourages collective action. Hence, the time path of vulnerability need not be explosive. As a whole, user-CSP asymmetry, the potential for switching CSPs, and the impureness of security as a public good all contribute to a novel environment for dynamically characterizing cloud security, thereby setting it apart from dynamic analyses of global public goods.

## 3. The Model

Our focus is on how security-enhancing actions of CSPs and their users create a security umbrella under which users determine whether they stay with their CSP or switch and the degree that they use their chosen CSP. Given users’ potential to switch, CSPs compete on the basis of platform benefits and how the security umbrella facilitates continued access to such benefits. Upon choosing a CSP, users determine the extent that they do business while using their CSP as a platform. Together, overall security effort and usage determine a CSP’s vulnerability (i.e., its appeal to malicious actors based on the security umbrella and the level of business activity occurring under it).

Table 1 lists the notation for the variables in our analy sis. The model itself is presented and explained below.

## 3.1. Players

Two CSPs and N(N � 2n) identical cloud service users exist in the market. Initially (t � 0), n random users are subscribers of CSP 1, and the other half are subscribers of CSP 2. A duopolistic setting facilitates a competitive environment under which CSPs realize that security is not only a technical issue but that it affects users’ decision to stay with their incumbent CSP or switch. Security is thereby a determinant of CSPs’ competitive environment (Arce 2020, Sen et al. 2020). This provides insights for other kinds of CSP markets (e.g., oligopoly) as well.

Table 1. Notation

<table><tr><td></td><td>Definition</td></tr><tr><td> $s_{cspj,t}$ </td><td>CSP  $j$ &#x27;s strategy: security investment in period  $t$ </td></tr><tr><td> $s_{i,t}$ </td><td>User  $i$ &#x27;s strategy: security investment in period  $t$ </td></tr><tr><td> $\alpha$ </td><td>Marginal contribution of the CSP  $j$ &#x27;s security investment</td></tr><tr><td> $k$ </td><td>Per unit cost from security investment for a user</td></tr><tr><td> $K$ </td><td>Per unit cost from security investment for the CSP</td></tr><tr><td> $y_{i,t}$ </td><td>User  $i$ &#x27;s strategy: cloud service usage in period  $t$ </td></tr><tr><td> $b(y_{i,t})$ </td><td>Nonsecurity-related net benefit from using  $y_{i,t}$  for a user</td></tr><tr><td> $B(y_{i,t})$ </td><td>Subscription profit from user  $i$  for the CSP</td></tr><tr><td> $S_{j,t}$ </td><td>State variable: accumulated security investment on CSP  $j$ </td></tr><tr><td> $S_{i,t}$ </td><td>State variable: accumulated security investment by user  $i$ </td></tr><tr><td> $S_{cspj,t}$ </td><td>State variable: accumulated security investment by CSP  $j$ </td></tr><tr><td> $V_{j,t}$ </td><td>State variable: accumulated vulnerability on CSP  $j$ </td></tr><tr><td> $p(V_{j,t})$ </td><td>Probability of a successful attack on user  $i$  on CSP  $j$ </td></tr><tr><td> $\tilde{p}(V_{j,t})$ </td><td>Probability of a successful attack on CSP  $j$ </td></tr><tr><td> $c$ </td><td>Per unit cost of a successful attack for a user</td></tr><tr><td> $C$ </td><td>Per unit cost of a successful attack for the CSP</td></tr><tr><td> $v_{j,t}$ </td><td>Marginal vulnerability attributed to user  $i$ </td></tr><tr><td> $1 - \delta_S$ </td><td>Depreciation speed (decay rate) of past security investment</td></tr><tr><td> $1 - \delta_V$ </td><td>Depreciation speed (decay rate) of past vulnerability</td></tr><tr><td> $\delta$ </td><td>Discount factor for the optimal value function</td></tr><tr><td> $\lambda$ </td><td>Per unit switching cost</td></tr><tr><td> $u_{i,t}$ </td><td>User  $i$ &#x27;s per period payoff in period  $t$ </td></tr><tr><td> $U_{i,t}$ </td><td>User  $i$ &#x27;s lifetime payoff at the end of period  $t$ </td></tr><tr><td> $\pi_{j,t}$ </td><td>CSP  $j$ &#x27;s per period payoff in period  $t$ </td></tr><tr><td> $\Pi_{j,t}$ </td><td>CSP  $j$ &#x27;s lifetime payoff at the end of period  $t$ </td></tr></table>

## 3.2. Strategies and Timing

Figure 1 summarizes the timing of the game in each period. First, CSPs $j \in \{ 1 , 2 \}$ choose their security investment, $s _ { c s p j , t } ,$ given their number of users. This determines the “out-of-the-box” baseline level of security, which is, of course, susceptible to zero days and may be otherwise augmented or compromised by user behavior.

Given $s _ { c s p j , t } ,$ users follow by determining their security investment, $s _ { i , t }$ . Part of what goes into $s _ { i , t }$ are user configurations and permissions, which are known to be prime determinants of security. Another part of $s _ { i , t }$ is assessing what is meant by the $\mathrm { C S P ^ { \prime } s }$ out-of-the-box security each time the CSP updates. For example, in mean time before failure, when CSPs develop a new cloud service, users devote $s _ { i , t }$ worth of hours testing its security or paying a third-party validator to do so. Users can also test new versions of the service as released, spending $s _ { i , t }$ worth of hours, or again, pay a validator to do so. Another example is the life cycle of security architecture, where given $s _ { c s p j , t } ,$ users can choose to rearchitect their security system or purchase security services from their CSP, spending $s _ { i , t }$ in total.

After these steps determine the security umbrella, users purchase $y _ { i , t }$ units of cloud services based upon their configurations given the current state of security.

## 3.3. State Variables and Information

Our analysis revolves around two payoff-related state variables: accumulated security investment and accumulated vulnerability. The states summarize the history in previous periods and directly figure into currentperiod payoffs.

Given individual security investments in period t by user i of CSP $j , s _ { i , t } ,$ and the security investment by its $\mathrm { C S P } , ~ j , ~ s _ { c s p j , t } ,$ state variable total accumulated security investment on CSP j at the end of period $t , S _ { j , t } ,$ is

$$
\begin{array}{r l} & S _ {j, t} = \sum_ {\tau = 0} ^ {t} \sum_ {i} \delta_ {S} ^ {\tau} [ \alpha s _ {c s p j, \tau} + s _ {i, \tau} ] \\ & \qquad = s _ {i, t} + \alpha s _ {c s p j, t} + \sum_ {i ^ {\prime} \neq i} s _ {i ^ {\prime}, t} + \delta_ {S} S _ {j, t - 1}, \end{array}\tag{1}
$$

where $1 - \delta _ { S } \in [ 0 , 1 ]$ is the depreciation speed (decay rate) of past security investment. The term $\alpha > 0$ recognizes that the CSP’s security efforts can have a different marginal effect on overall security relative to users efforts. Tianfield (2012) identifies how this relative effect can vary across IaaS, PaaS, and SaaS, causing the security responsibilities of CSP and users to differ between service layers of the cloud stack. Similarly, the MITRE ATT&CK matrix for the cloud includes phenomena under the purview of CSPs and users that differ between layers in the cloud stack. Hence, α is not indexed by subscript j because it corresponds to the relative contribution of a CSP within a particular class of service (layer within the cloud stack) rather than across different classes of service. In equilibrium, we conduct comparative statics with respect to α.

Figure 1. Timing  
![](/api/attachments/ZSUA4UZB/fulltext/images/9e53189fab6ec969a4f14cb99d5ce39782552ee66f52605b763b4b76de33118a.jpg)

Taking the effect of the CSP and users’ security contributions to be a function of their aggregate sum is in keeping with regarding the cloud as the attack surface. Evidence drawn from data and observations from realworld cyberattacks indicates an impressive diversity of tactics, techniques, and procedures (TTPs) on the part of cloud adversaries (Crowdstrike 2023). Examples of cloud penetration TTPs include exploiting insecure CSP default settings, user misconfigurations, containers without internal security, corporate subnets without multifactor authentication (MFA), open ports or servers to conduct a man-in-the-cloud attack, and abuse of cloud resources, such as occurs with coin mining. Indeed, even misconfigurations have variations, such as excessive permissions, disabled logging features, and publicly accessible cloud storage buckets. Similarly, the proliferation of Application Programming Interface (API) calls and privileges available to control API access broadens the attack surface. A summation aggregator indicates the extent that CSPs and users address the multiplicity of security issues inherent in the cloud. It, therefore, follows that subsequent states of security are also derived from the (discounted) sum of past security actions.

Total accumulated security investment on CSP j at the end of period $t , S _ { j , t } .$ , can also be written as the sum of

CSP $j ^ { \prime } \mathbf { s }$ accumulated security investment, $S _ { c s p j , t } ,$ and user’s accumulated individual security investment, $S _ { i , t } \mathrm { : }$

$$
S _ {j, t} = \alpha S _ {c s p j, t} + \sum_ {i} S _ {i, t},
$$

where $\begin{array} { r } { S _ { c s p j , t } = \sum _ { \tau = 0 } ^ { t } \delta _ { S } ^ { \tau } s _ { c s p j , \tau } } \end{array}$ and $\begin{array} { r } { S _ { i , t } = \sum _ { \tau = 0 } ^ { t } \delta _ { S } ^ { \tau } s _ { i , \tau } . } \end{array}$

Our second state variable is vulnerability, $V _ { t } .$ A ${ \mathrm { C S P ' s } }$ ex ante vulnerability is a function of users’ attractiveness to malicious actors, the CSP’s attractiveness to malicious actors, and malicious actors’ efforts (Gordon and Loeb 2002, Cavusoglu et al. 2014, Fedele and Roner 2022). The idea behind Gordon–Loeb vulnerability as used in the extant literature on optimal cybersecurity expenditure is as follows. The probability of a successful attack is a composite function of the probability of an attack and security expenditure/effort. The probability of an attack is determined by the vulnerability of the target (CSP and users). How is this part of the composite function determined? First, an attack has to happen, which means that the target is attractive to malicious actors. Given that we do not have an active malicious actor in the game, ex ante vulnerability is mainly a measure of target attractiveness to malicious actors. Such attractiveness is a function of the amount and value of user’s usage, $y _ { t } ,$ occurring. A flourishing CSP with a growing number of users is more attractive ex ante, with all their personally identifiable information, proprietary secrets, passcodes, ransomware prospects, and business disruption opportunities at risk. This is a “rob banks because that is where the money $\mathrm { i s } ^ { \prime \prime }$ theory of attractiveness to malicious actors.<sup>4</sup> It is also commensurate with the market share theory and evidence of targeting by malicious actors, whereby platforms with a larger market share receive at least their relative share of malicious targeting (O’Donnell 2008, Garcia et al. 2014, Vasek et al. 2015, Arce 2018, Geer et al. 2020). It is also consistent with the evolution of ransomware to be a big-game-hunting phenomenon. Second, the extent of usage also matters. In this way, data storage and word processing in the cloud correspond to greater usage than word processing only. Moreover, usage can create weakness in an information system, system security procedures, internal controls, or implementation that could be exploited or triggered by a malicious actor and result in a security breach (Stoneburner et al. 2002).

At the same time, ex post vulnerability is also a function of ${ \mathrm { C S P ' s } }$ and their users’ security investment. Given usage-determined malicious actors’ interests in the CSP and its users, the ultimate success of an attack depends on the amount of security provided. Part of our contribution is recognizing that usage and hence, vulnerability, depend on security. The decision to store data in the cloud is likely conditional on a greater level of security than that for using cloud-based word processing. It follows that selective incentives (profits) depend on security. Furthermore, this implies that vulnerability becomes an endogenously determined state variable rather than a parameter in the model.

To the best of our knowledge, this is the first analysis to consider the symbiosis between security and vulnerability by treating vulnerability endogenously. By contrast, in extensions of the Gordon and Loeb (2002) decision-theoretic model of optimal security expenditure to game-theoretic settings, the level of vulnerability is taken as a parameter open to ex post comparative statics analysis (Fedele and Roner 2022). Here, instead, the level of vulnerability is an endogenously determined state variable. Moreover, as our analysis is dynamic, rather than comparative statics, we characterize the time path of vulnerability via a Euler equation. In particular, vulnerability over time is a function of the selective incentives generated by cloud security.

Consequently, in period (stage) t, given ex ante aggregate vulnerability, $V _ { j , t - 1 }$ , the ex post marginal vulnerability attributed to user $i , v _ { i , t } ,$ , is

$$
v _ {i, t} = y _ {i, t} - s _ {i, t}.
$$

Given users i of platform $j ,$ state variable total accumulated (ex post) vulnerability on platform j at the end of period t is defined as

$$
V _ {j, t} = \sum_ {\tau = 0} ^ {t} \sum_ {i} \delta_ {V} ^ {\tau} [ \underbrace {(y _ {i , \tau} - s _ {i , \tau})} _ {v _ {i, \tau}} - \alpha s _ {c s p j, \tau} ]
$$

$$
V _ {j, t} = \delta_ {V} V _ {j, t - 1} + \sum_ {i ^ {\prime} \neq i} y _ {i ^ {\prime}, t} + y _ {i, t} - S _ {j, t},\tag{2}
$$

where $\delta _ { V } \in [ 0 , 1 ]$ is the persistence of past vulnerabilities left unaddressed by $S _ { j , t } , S _ { j , t - 1 } , S _ { j , t - 2 } , . .$ : or not taken offline in periods $t - 1 , t - 2 , . .$ : as part of these security strategies. In contrast to our justification of cloud security as a summation-determined public good, expressing the vulnerability state variable in terms of the sum of individual user vulnerability is a simplifying assumption. Vulnerability is taken to be a function of the concentration of resources using the CSP, net of security. Nonlinearities with respect to vulnerability instead arise within users’ and CSPs’ expected payoff functions.

Finally, in a Markov perfect equilibrium, the state variables determine the information structure upon which players condition optimal strategies. At the beginning of state $t ,$ the players know the pair $( V _ { j , t - 1 } ,$ $S _ { j , t - 1 } )$ ). In addition, the number of potential state pairs, $( \dot { V } _ { j , t } , S _ { j , t } )$ , is finite. This is a standard assumption necessary for the existence of a Markov perfect equilibrium.

## 3.4. Cybersecurity

Beginning at least with Gordon and Loeb (2002), the probability of a successful attack is a function of ex post vulnerability, $p ( V _ { j , t } )$ , rather than only a function of total security effort, $p ( S _ { j , t } )$ . In expressing the probability of a successful attack in terms of vulnerability, we capture the effects of its components $s _ { i , t } , s _ { c s p j , t } ,$ , and $y _ { i , t }$ on cloud security. It easily holds at the extreme, where governments having large $V _ { j , t } { ' s }$ are targeted by advanced persistent threats with the commensurate effect on $p ( V _ { j , t } )$ . At the same time, security efforts reduce vulnerability, $V _ { j , t } ,$ , and therefore, the probability of a successful attack.

We define $p ( V _ { j , t } )$ to be monotonically increasing and convex in $V _ { j , t }$ . The accumulated vulnerability of platform j determines every user’s probability of being attacked. It is intentionally modeled in this way to capture the multitenant nature of cloud services, where one user’s security can impact cotenants’ security. Critical crosstenant vulnerabilities violating cloud isolation are increasingly documented (Wiz 2023). By contrast, term $\tilde { p } ( V _ { j , t } )$ is the probability that the CSP suffers a successful attack as a function of ex post vulnerability. It satisfies the same monotonicity and convexity assumptions as $p ( V _ { j , t } )$

## 3.5. Payoffs

A user’s payoff at time t has several components: the benefit from using cloud services under the ${ \mathrm { C S P ' s } }$ security umbrella, the probability of a successful material attack on this benefit, the cost incurred from a material impact, security investment costs, and the cost incurred from a possible platform switch:

$$
\begin{array}{c} u _ {i, t} = p (V _ {j, t}) [ (1 - c) b (y _ {i, t}) ] + (1 - p (V _ {j, t})) b (y _ {i, t}) \\ - k s _ {i, t} - \lambda S _ {j, t - 1} \end{array}\tag{3}
$$

$$
u _ {i, t} = (1 - p (V _ {j, t}) c) b (y _ {i, t}) - k s _ {i, t} - \lambda S _ {j, t - 1},\tag{4}
$$

where function $b ( y _ { i , t } )$ measures the net benefits arising from using $y _  i , $ cloud services under the security umbrella.

Benefit $b ( y _ { i , t } ) , b ^ { \prime } > 0 , b ^ { \prime \prime } < 0$ captures every nonsecurityrelated aspect stemming from the cloud service (revenues gained from $y _ { i , t } ,$ the price of $y _ { i , t }$ usage, etc.). Similar benefit functions facilitating analyses of specific facets of a platform can be found in Lee (2014) and Arce (2020). The term $c \in ( 0 , 1 )$ captures the percentage cost of a successful attack, and k captures the per unit (opportunity) cost from security investment. Cybersecurity costs are linear in $s _ { i , t }$ because this fits the evidence (Neuhaus and Plattner 2013). Indeed, theoretical models with diminishing returns (increasing average cost) raise concerns about their applicability to cybersecurity (Heitzenrater and Simpson 2016a, b). Contingent payoff component $\lambda S _ { j , t - 1 }$ is the per unit switching cost, λ, times state variable $S _ { j , t - 1 } ,$ the accumulated security investment on the incumbent platform. It becomes part of a user’s payoff only if they switch CSPs. The idea is that familiarity with CSP j’s security umbrella makes it costly to switch to a CSP with a different security umbrella and attendant protocols. In contrast to standard analyses where lock-in is the outcome of one actor’s actions, usually the vendor, $\lambda S _ { j , t - 1 }$ is jointly determined by users and their CSP through $S _ { j , t - 1 }$ . An alternative is Arce (2022), where users and their CSP interact to determine the marginal degree of lock-in, equivalent to λ in our model. Here, instead, the magnitude of lock-in is jointly determined. Finally, the expression shows that security is not only another dimension of product differentiation. The security umbrella is the gateway to the benefits associated with a CSP’s services, $b ( y _ { i , t } )$ . Specifically, a decrease in the probability of a successful breach owing to the actions of any user creates a selective incentive for other users in the form of $( 1 - p ( V _ { j , t } ) c ) b ( y _ { i , t } )$

CSP j’s per period payoff takes a similar form:

$$
\pi_ {j, t} = \tilde {p} (V _ {j, t}) [ (1 - C) n B (y _ {i, t}) ]
$$

$$
+ (1 - \tilde {p} (V _ {j, t})) n B (y _ {i, t}) - K s _ {c s p j, t}\tag{5}
$$

$$
\pi_ {j, t} = (1 - \tilde {p} (V _ {j, t}) C) n B (y _ {i, t}) - K s _ {c s p j, t}.\tag{6}
$$

The term $K > 0$ measures the CSP’s per unit cost of security investment, and $C \in ( 0 , 1 )$ measures the ${ \mathrm { C S P ' s } }$ per unit cost of a successful attack. Function $n B ( y _ { i , t } )$ measures the profit generated by n users’ subscription to the CSP. As is the case for $b ( y _ { i , t } ) , n B ( y _ { i , t } )$ summarizes all nonsecurity aspects of providing cloud services. The term $( 1 - \tilde { p } ( \dot { V _ { j , t } } ) \dot { C } ) n B ( y _ { i , t } ) \dot $ is the CSP’s selective incentive. Given $C \in ( 0 , 1 )$ , CSPs always want more users.

## 3.6. Equilibrium

We close our model by studying the symmetric Markov perfect equilibrium of the game. A player’s strategy in period t is Markov (or state space) if its history dependence is only a function of the information provided by the values of the state variables at the start of period $t ,$ $( V _ { j , t - 1 } , S _ { j , t - 1 } )$ , rather than the entire specifics of the past history of play. The number of strategies for a player is, therefore, not greater than the (finite) number of states, $( V _ { j , t - 1 } , S _ { j , t - 1 } ) _ { \cdot }$ , rather than the number of potential histories. Moreover, the exact time sequence $\stackrel { \star } { \{ } s _ { j , \tau }  , s _ { i , \tau } , y _ { i , \tau } \} _ { \tau = 0 } ^ { t - 1 }$ determining state (history) $( V _ { j , t - 1 } , S _ { j , t - 1 } )$ does not matter. A Markov strategy is stationary if, whenever $( V _ { j , t - 1 } ,$ $\boldsymbol { S } _ { j , t - 1 } \big ) = ( \boldsymbol { V } _ { j , \hat { t } - 1 } , \boldsymbol { S } _ { j , \hat { t } - 1 } ) , t \neq \hat { t } ,$ , then a player takes the same strategy in state $( V _ { j , t - 1 } , S _ { j , t - 1 } )$ as in state $( V _ { j , \hat { t } - 1 } ,$ $S _ { j , \hat { t } - 1 } )$ . That is, a player takes the same actions for the same state values (information) independently of the time of the state. The assumption is justifiable given our game’s infinite horizon. Stationary strategies are Markov perfect if they are subgame perfect for the game in stage t for every t. MPE is a powerful tool for dynamic games because the state variables summarize both the history of play and the information structure.<sup>5</sup> Consequently, at the beginning of period $t ,$ users make strategic choices knowing the values of $V _ { j , t - 1 }$ and $S _ { j , t - 1 } ,$ and their optimal value function only depends on the resultant states. As such, best replies are truly reaction functions.

Finally, in addition to being symmetric MPE, the equilibria also satisfy a no-switching constraint. As expressed in users’ period t utility function, switching CSPs costs $\lambda S _ { j , t - 1 }$ . Switching costs refer to the sunk costs incurred for operating under a new CSP’s security umbrella because practices and protocols under the old security umbrella no longer apply. For example, given information structure $( \hat V _ { 1 , t - 1 } , \hat S _ { 1 , t - 1 } )$ in period t, a user’s optimal value function for staying with CSP 1 is $U _ { s t a y }$ $\left( V _ { 1 , t - 1 } , S _ { 1 , t - 1 } \right)$ . If the user switches to CSP 2, their value function is $U _ { s w i t c h } ( V _ { 2 , t - 1 } , S _ { 2 , t - 1 } , S _ { 1 , t - 1 } )$ instead, with argument $S _ { 1 , t - 1 }$ referring to the associated switching costs and corresponding information structure. Users do not switch from CSP 1 to CSP 2 if $U _ { s t a y } ( V _ { 1 , t - 1 } , S _ { 1 , t - 1 } )$ $\ge U _ { s w i t c h } ( V _ { 2 , t - 1 } , S _ { 2 , t - 1 } , S _ { 1 , t - 1 } )$ . A similar constraint holds for establishing conditions whereby CSP 2 users do not switch to CSP 1. Shapiro and Varian (1998) and Varian (2004a) introduce the no-switching constraint to examine factors locking users into information technologies and vendors. Later, Lee (2014) and Arce (2020) use no-switching constraints to establish conditions whereby information technology platforms coexist. We employ the no-switching constraint to characterize both user lock-in and CSP security competition. At its roots, the no-switching criterion is related to the coalition-proof Nash equilibrium refinement (Bernheim et al. 1987, Kahn and Mookherjee 1992) for establishing conditions that rule out tipping into a CSP monopoly.

## 3.7. Initial Characteristics

We conclude this section by characterizing the strategic relationships among users and between users and their CSP. Specifically, plain complements are a property of whether others’ strategies increase a player’s payoff, and strategic substitutes are a property of best replies (Eaton 2002, chapter 10): that is, whether the players strategies move in opposite directions. The following propositions characterize whether an increase in the security investments of other users or their CSP increases user i’s payoff (plain complements) and if it decreases user i’s security investment and the rate that it changes (strategic substitutes).

Proposition 1. In the absence of lock-in $( \lambda = 0 )$ , users’ and their $C S P { s }$ security investments are plain complements for their stage t (per period) payoffs, $\frac { \partial u _ { i , t } } { \partial s _ { i ^ { \prime } } , t } > 0$ and $\frac { \partial u _ { i , t } } { \partial s _ { c s p j } , t } > 0$ . With finite lock-in costs, plain complements require

$$
b (y _ {i, t}) \frac {\partial p (V _ {j , t})}{\partial V _ {j , t}} \delta_ {V} ^ {t} > \lambda \delta_ {S} ^ {t}.
$$

Proof. All proofs are in the Online Appendix. w

The condition for plain complements characterizes how competition between CSPs impacts the nature of security investment. Suppose that the switching cost does not bind. In that case, other users’ and the CSP’s efforts to enhance security provide a public good to user i. By contrast, once switching cost λ binds, such efforts may eventually be harmful if the marginal cost of their efforts in terms of lock-in, $\lambda \delta _ { S } ^ { t } ,$ exceeds the marginal reduction in vulnerability that they bring about, $b ( y _ { i , t } ) \frac { \partial p ( V _ { j , t } ) } { \partial V _ { i , t } } \delta _ { V } ^ { t }$ . In a world where $\delta _ { V }$ is sufficiently lower than $\delta _ { S } ,$ the plain complements relationship is also broken. For example, if $\delta _ { S }$ is large, the decay rate of technology, $1 - \delta _ { S }$ , is so small that only past security investment matters, and current-period efforts do not figure much into a user’s calculus. Overall, the novel implication is that others’ security investments can be plain complements (increase other users payoffs) at one point in time and plain substitutes (decrease other users’ payoffs) later in the same game.

Proposition 2. Other users’ security investments are strategic substitutes for user i’s security investment:

$$
\frac {\partial u _ {i , t} ^ {2}}{\partial s _ {i , t} \partial s _ {i ^ {\prime} , t}} <   0.
$$

The term $\partial u _ { i , t } / \partial s _ { i , i }$ derives a user’s best reply (reaction) function. Hence, the second derivative of the term with respect to $s _ { i ^ { \prime } , t }$ characterizes the user’s best reply function with respect to the security strategy of another user, $i ^ { \prime } \neq i ,$ and the second derivative with respect to $s _ { c s p j , t }$ characterizes the user’s best reply function with respect to their CSP’s security strategy. A negative sign means that the user’s best response security effort decreases in the security effort of other users, known as strategic substitutes.

Indeed, for the CSP’s security investment $, \frac { \partial u _ { i , t } ^ { 2 } } { \partial s _ { i , t } \partial s _ { c s p j , t } }$ i also negative.

Proposition 3. The larger the $C S P { s }$ responsibility for joint security for the service in question, $\alpha ,$ the smaller the user’s best reply to the CSP’s security investment. That $i s ,$ strategic substitutes between CSP and users are exacerbated:

$$
\frac {\partial u _ {i , t} ^ {2}}{\partial s _ {i , t} \partial s _ {c s p j , t}} = b (y _ {i, t}) \delta_ {V} \frac {\partial p ^ {2} (V _ {j , t})}{\partial V _ {j , t} ^ {2}} (- \alpha \delta^ {t}) <   0.
$$

The larger α is, the more the ${ \mathrm { C S P ' s } }$ security investment decreases the user’s marginal benefit of their own security investment. Yet, users are not absolved from the joint security problem, even though the cloud service they contract for may require greater security responsibility on the part of the CSP. In particular, the upper layer of cloud infrastructure (the control plane), which users are responsible for securing, has increasingly become vulnerable to attacks introduced by misconfigurations and human error (Torkura et al. 2021).

Together, Propositions 2 and 3 epitomize the joint security problem. For example, 55% of the respondents to a Ponemon Institute survey of cloud users believe that the in-house IT security leader is not responsible for ensuring their organization’s safe use of cloud computing resources (Ponemon Institute 2014). To the extent that such beliefs may be rational on the part of users, as indicated by Propositions 2 and 3, it is inefficient if CSPs do not follow through with the tools at their disposal to aid users. For example, AWS knew that Capital One had the misconfiguration leading to their 2019 breach but did not communicate it to Capital One or other users with similar misconfigurations.

## 4. Locked-in Users

We begin with a baseline model where users are locked into their CSP. In this case, λ → ∞; therefore, users do not switch CSPs, and CSPs know it.

In dynamic games, the players maximize their lifetime payoffs, which are the discounted sum of their payoffs in each period, t. For user i of CSP j,

$$
U _ {i, j} = \sum_ {t = 0} ^ {\infty} \delta^ {t} u _ {i, t} (\cdot),
$$

where $u _ { i , t } ( \cdot )$ is the payoff in period t, δ is the discount factor, and the horizon is infinite. An infinite horizon captures the nonzero probability that CSPs and their users interact for another period.

In an MPE, players’ payoffs are transformed into optimal value functions, which themselves are represented as only a function of the state variables summarizing the history of play:

$$
U _ {i, t} = U _ {i, t} (V _ {j, t - 1}, S _ {j, t - 1}).
$$

State variables $V _ { j , t - 1 }$ and $S _ { j , t - 1 }$ <sub>1</sub> are known at the start of period t. When users select their security investment and usage in period $t ,$ they do so understanding the joint effect on their current-period payoff, $u _ { i , t } ( \cdot )$ . In addition, users are forward looking and realize that their choices figure into determining $S _ { j , t }$ and $V _ { j , t }$ . Given discount factor $\delta ,$ users select $s _ { i , t } { ' } \mathbf { s }$ and $y _ { i , t } ^ { \prime } \mathrm { \mathbf { s } }$ to maximize $U _ { i , t } ( \cdot )$ with these two effects in mind:

$$
U _ {i, t} (V _ {j, t - 1}, S _ {j, t - 1}) = \max _ {s _ {i, t}, y _ {i, t}} \{u _ {i, t} (\cdot) + \delta U _ {i, t + 1} (V _ {j, t}, S _ {j, t}) \}.\tag{7}
$$

This is the familiar Bellman equation in dynamic programming expressed in terms of the user’s optimal value function, $U _ { i , t } ( V _ { j , t - 1 } , S _ { j , t - 1 } ) ;$ ; current-period payoff, $u _ { i , t } ( \cdot ) ;$ and discounted continuation value, $\delta U _ { i , t + 1 }$ $\left( V _ { j , t } , S _ { j , t } \right)$ . When finding a best reply, each player holds the strategies of the other players constant, and in an MPE, others’ strategies are additionally unchanging in that they are also stationary in equivalent states. It, therefore, follows that Equation (7) can be re-expressed in terms of the optimal value function at the given states without reference to the time period:

$$
U _ {i} (V _ {j, t - 1}, S _ {j, t - 1}) = \max _ {s _ {i, t}, y _ {i, t}} \{u _ {i, t} (\cdot) + \delta U _ {i} (V _ {j, t}, S _ {j, t}) \}.\tag{8}
$$

Consequently, finding a best reply is a dynamic programming problem for each of the players (Friedman 1976, Haurie et al. 2012). This is because when finding a best reply, player i holds the strategies of the other players constant $( \mathrm { e . g . } , \partial y _ { i ^ { \prime } , t } / \partial y _ { i , t } = 0 , \bar { \forall } i ^ { \prime } \neq i )$

The solution to (8) must also be subgame perfect within period t. Figure 1 lays out our solution procedure. Usage, $y _ { i , t } ,$ is chosen last; hence, by backward induction, we solve for it first. With respect to $\delta U _ { i } ( V _ { j , t } , S _ { j , t } ) , V _ { j , t }$ is a function of $y _ { i , t }$ <sub>t</sub> via state Equation (2). Given the expression for $u _ { i , t } ( \cdot )$ in (4), the associated first-order condition is

$$
\begin{array}{l} \frac {\partial U _ {i} (V _ {j , t - 1} , S _ {j , t - 1})}{\partial y _ {i , t}} = (1 - p (V _ {j, t}) c) \frac {\partial b}{\partial y _ {i , t}} - c b \frac {\partial p (V _ {j , t})}{\partial V _ {j , t}} \frac {\partial V _ {j , t}}{\partial y _ {i , t}} \\ + \delta \frac {\partial U _ {i} (V _ {j , t} , S _ {j , t})}{\partial V _ {j , t}} \frac {\partial V _ {j , t}}{\partial y _ {i , t}} = 0. \end{array} \tag {9}
$$

Setting ${ { \partial b } } / { { \partial y } _ { i , t } } = { b ^ { \prime } }$ and substituting $\partial V _ { j , t } / \partial y _ { i , t } = 1$ (from Equation (2)),

$$
\begin{array}{c} \frac {\partial U _ {i} (V _ {j , t - 1} , S _ {j , t - 1})}{\partial y _ {i , t}} = (1 - p (V _ {j, t}) c) b ^ {\prime} - c b \frac {\partial p (V _ {j , t})}{\partial V _ {j , t}} \\ + \delta \frac {\partial U _ {i} (V _ {j , t} , S _ {j , t})}{\partial V _ {j , t}} = 0, \end{array}\tag{10}
$$

where $\frac { \partial U _ { i } ( V _ { j , t } , S _ { j , t } ) } { \partial V _ { j , t } }$ is unknown.

Equation (10) is the best reply function (reaction function) for $y _ { i , t }$ in implicit function form. Prior to analyzing this function, unknown term $\frac { \partial \bar { U } _ { i } ( V _ { j , t } , S _ { j , t } ) } { \partial V _ { j , t } }$ needs to be characterized. To this end, we follow the Benveniste and Scheinkman (1979) procedure, as operationalized in the proof of Lemma 1.

Lemma 1. A user’s optimal value function decreases in total vulnerability at an increasing rate:

$$
\begin{array}{l} \frac {\partial U _ {i} (V _ {j , t - 1} , S _ {j , t - 1})}{\partial V _ {j , t - 1}} = - \delta_ {V} (1 - p (V _ {j, t}) c) b ^ {\prime} <   0 \\ \frac {\partial^ {2} U _ {i} (V _ {j , t - 1} , S _ {j , t - 1})}{\partial V _ {j , t - 1} ^ {2}} = \delta_ {V} ^ {2} \frac {\partial p (V _ {j , t})}{\partial V _ {j , t}} c b ^ {\prime} > 0, \end{array}
$$

where $c \in ( 0 , 1 )$ ) and $b ^ { \prime } > 0 .$ . Updating $\frac { \partial U _ { i } ( V _ { t - 1 } , S _ { t - 1 } ) } { \partial V _ { j , t - 1 } }$ one period yields

$$
\frac {\partial U _ {i} (V _ {j , t} , S _ {j , t})}{\partial V _ {j , t}} = - \delta_ {V} (1 - p (V _ {j, t + 1}) c) b ^ {\prime} <   0,
$$

which is the unknown term in Equation (10).

By characterizing the final term in Equation (10), we establish that $\mathrm { C S P }$ users must consider both the effect of usage on the probability of a breach, the second term in Equation (10), and the future effect of usage on their value function, the third term in Equation (10). Both effects subtract from the benefits of current usage as expressed by the first term in Equation (10). Moreover, these effects are not constant from period to period. It begs the question of how these rates of change balance (or not) as reflected by the time path of vulnerability resulting from optimal usage and security (i.e., a Euler equation).

## 4.1. The Euler Equation

Our model is quite general; no functional forms are spe cified for per period payoffs, the probability of a breach, and so on. In such circumstances, the Euler equation assists in characterizing the associated dynamics (Dechert 1997, Josa-Fombellida and Rinco´n-Zapatero 2008). Here, the Euler equation shows the relationship between optimal levels of $V _ { j , t }$ and $V _ { j , t + 1 }$ . In deriving the Euler equation, we characterize the optimal path of accumulated vulnerability. The path of users’ behavior is addressed in the next subsection. Moreover, neither extensive form games nor repeated games generate a Euler equation as an output. The Euler equation is an advantage of the dynamic game approach.

Substituting the value for $\partial U _ { i } / \partial V _ { j , t }$ from Lemma 1 into the first-order condition (reaction function) for $y _ { i , t }$ in Equation (10) immediately yields the Euler equation for the dynamics of accumulated vulnerability.

Proposition 4. The Euler equation for the optimal level of accumulated vulnerability is

$$
\frac {\partial U _ {i} (V _ {j , t - 1} ^ {*} , S _ {j , t - 1})}{\partial V _ {j , t - 1} ^ {*}} = \delta_ {V} \left[ - b c \frac {\partial p (V _ {j , t} ^ {*})}{\partial V _ {j , t} ^ {*}} + \delta \frac {\partial U _ {i} (V _ {j , t} ^ {*} , S _ {j , t})}{\partial V _ {j , t} ^ {*}} \right],\tag{11}
$$

where $\begin{array} { r } { \frac { \partial p ( V _ { j , t } ) } { \partial V _ { j , t } } > 0 \ : a n d \frac { \partial p ^ { 2 } ( V _ { j , t } ) } { \partial V _ { j , t } ^ { 2 } } > 0 . } \end{array}$

From Lemma 1 and shifted down one period, the Euler equation can also be expressed as

$$
\begin{array}{l} (1 - p (V _ {j, t - 1} ^ {*}) c) b ^ {\prime} (y _ {i, t - 1}) - b (y _ {i, t - 1}) c \frac {\partial p (V _ {j , t - 1} ^ {*})}{\partial V _ {j , t - 1} ^ {*}} \\ = \delta \delta_ {V} (1 - p (V _ {j, t} ^ {*}) c) b ^ {\prime} (y _ {i, t}). \end{array}\tag{12}
$$

The Euler equation lends itself to several characterizations of our model. One way to view the Euler equation is as the intertemporal relationship between the marginal costs of accumulated vulnerability in the current and future periods (McKay et al. 2017). From Equation (11), the term $- \delta _ { V } b c \frac { \partial p ( V _ { j , t } ^ { * } ) } { \partial V _ { j , t } ^ { * } } < 0$ measures the extent that current vulnerability influences optimal vulnerability by increasing the likelihood of a breach. The term $\begin{array} { r } { \delta \frac { \partial U _ { i } \left( V _ { j , t } ^ { * } , S _ { j , t } \right) } { \partial V _ { j , t } ^ { * } } < 0 } \end{array}$ measures the extent that future vulnerability influences optimal vulnerability. Hence, in the absence of future vulnerability considerations, current vulnerability is too high. In other words, a nondynamic (single-shot) approach leads to excessive vulnerability in each period.

Another way to view the Euler equation is from the perspective of the interim equilibrium when users maximize their value function by choosing $y _ { i , t }$ <sub>t</sub>. In this subgame, Equation (12) characterizes the optimal path of accumulated vulnerability. On this path, given a certain level of $V _ { j , t - 1 } ^ { * } ,$ the left-hand side of Equation (12) is constant, and the equilibrium level of $V _ { j , t } ^ { * }$ can be predicted by $V _ { j , t - 1 } ^ { * } ,$ provided that inverse function $p ^ { - 1 } ( \cdot )$ exists.

Proposition 5. The equilibrium path of accumulated vulnerability is

$$
\frac {\partial V _ {j , t} ^ {*}}{\partial V _ {j , t - 1} ^ {*}} = \frac {b ^ {\prime} (y _ {i , t - 1}) \frac {\partial p (V _ {j , t - 1} ^ {*})}{\partial V _ {j , t - 1} ^ {*}} + b (y _ {i , t - 1}) \frac {\partial^ {2} p (V _ {j , t - 1} ^ {*})}{\partial^ {2} V _ {j , t - 1} ^ {*}}}{\delta \delta_ {V} b ^ {\prime} (y _ {i , t}) \frac {\partial p (V _ {j , t} ^ {*})}{\partial V _ {j , t} ^ {*}}} > 0.\tag{13}
$$

Vulnerability, which increases with usage, builds upon itself. The increase in vulnerability over time justifies CSA’s concern with security in the cloud. It also identifies the trade-off inherent in taking shelter under the CSP’s security umbrella. We, therefore, turn to the question of whether the path of accumulative vulnerability converges or not.

Specifically, the Euler equation additionally lends itself toward comparative statics of the parameters and their implications for (non-)convergence. The numerator of Equation (13) comes from the first-order conditions for $V _ { j , t - 1 } ^ { * }$ (see the proof of Proposition 5). Yet, a user’s payoff function is not linear in $V _ { j , t - 1 } ^ { * }$ , and so, neither are the terms in the numerator of Equation (13). The denominator of Equation (13) is a function of $V _ { j , t } ^ { * }$ discounted by both δ and $\delta _ { V } .$

Figure 2. Vulnerability Conditions  
![](/api/attachments/ZSUA4UZB/fulltext/images/3a5e9466aa23193ecc650d4d2ad9e1716863e5398979563dffff131055f7c376.jpg)

Consequently, by Proposition $5 ,$ convergence of the optimal path of $V _ { j , t } ^ { * }$ <sub>t</sub> depends on δ and $\delta _ { V . }$ <sub>.</sub> For example, in extreme cases, if $\delta = 0$ (or $\delta _ { V } = 0 )$ , decision making becomes static. From Figure 2, the path of $V _ { j , t } ^ { * }$ is explosive because users’ and CSPs’ preferences for the future (δ) do not keep vulnerability in check or because their recognition of the carryover in vulnerability from one period to the next $( \delta _ { V } )$ does not keep vulnerability in check. Managers need to realize that this is a consequence of an absence of concern with how vulnerability builds on itself. One way to influence managerial behavior in this direction is through the guidance provided by the aforementioned CSA document on joint security in the cloud. In the absence of managerial action, social planners must act if the market itself cannot motivate the users to sufficiently contribute to the security umbrella.

By contrast, if $\delta = 1$ and $\delta _ { V } = 1$ , the optimal path is less volatile because users hold past, current, and future vulnerability in equal regard. Indeed, in this case, one cannot rule out $\partial V _ { j , t } ^ { * } / \partial V _ { j , t - 1 } ^ { * } \leq 1$ , and $V _ { j , t } ^ { * }$ converges. Contrasting these conditions shows how important it is for CSPs and social planners to gauge users’ attitudes toward the future, the past, and the resulting vulnerability.

If δ � 1 and $\delta _ { V } = 1$ , Equation (13) becomes

$$
\frac {\partial V _ {j , t} ^ {*}}{\partial V _ {j , t - 1} ^ {*}} = \frac {b ^ {\prime} (y _ {i , t - 1}) \frac {\partial p (V _ {j , t - 1} ^ {*})}{\partial V _ {j , t - 1} ^ {*}}}{b ^ {\prime} (y _ {i , t}) \frac {\partial p (V _ {j , t} ^ {*})}{\partial V _ {j , t} ^ {*}}} + \frac {b (y _ {i , t - 1}) \frac {\partial^ {2} p (V _ {j , t - 1} ^ {*})}{\partial^ {2} V _ {j , t - 1} ^ {*}}}{b ^ {\prime} (y _ {i , t}) \frac {\partial p (V _ {j , t} ^ {*})}{\partial V _ {j , t} ^ {*}}}.\tag{14}
$$

From Equation (14), the optimal path depends on the possible range of changes in functions $b ( y _ { i , t } )$ and $p ( y _ { i , t } )$ . For example, if the numerator $b _ { t - 1 } ^ { \prime } p _ { t - 1 } ^ { \prime } + b _ { t - 1 } p _ { t - 1 } ^ { \prime \prime }$ is exactly the same as the denominator $b _ { t } ^ { \prime } p _ { t } ^ { \prime } ,$ , then $\partial V _ { j , t } ^ { * } / \partial V _ { j , t - 1 } ^ { * } = 1$ . From Figure $2 , V _ { j , t } ^ { * }$ reaches a steady state. In more general cases, the term $b ( y _ { i , t - 1 } )$ is the net profit/benefit from using the cloud. As such, it is the largest value in Equation (14). The terms $b ^ { \prime } ( y _ { i , t } ) > 0$ and $b ^ { \prime } ( y _ { i , t - 1 } ) > 0$ are marginal profit, which is clearly less than total profit, $b ( y _ { i , t - 1 } )$

We assume convexity in the model $b ^ { \prime \prime } ( \cdot ) < 0 ,$ , so changes in $b ^ { \prime } ( \cdot )$ from period t � 1 to period t will not be too big if usage is large.

The large $b ( y _ { i , t } )$ value in Equation (14) is weighted by $p ^ { \prime \prime }$ , and the smaller $b ^ { \prime } ( y _ { i , t } )$ value is weighted by $p ^ { \prime } .$ Moreover, breach probability $p ( V _ { j , t } )$ is a small number with even smaller changes. Indeed, as we allow $V _ { j , t }$ to take a large range of values to accommodate large-scale usage and security investments, $p ( V _ { j , t } )$ will not be overly convex. Hence, weights $p ^ { \prime \prime }$ on $b ( y _ { i , t } )$ and $p ^ { \prime }$ on $b ^ { \prime } ( y _ { i , t } )$ stay small for large usage values, $y _ { i , t } ,$ and corresponding vulnerability. Thus, as illustrated in Figure $^ { 2 , }$ when $\delta = \mathsf { 1 } , \delta _ { V } = \mathsf { 1 }$ , and $p ^ { \prime \prime } \ll p ^ { \prime } .$ , it is possible that $\left\lceil \partial V _ { j , t } ^ { * } \right.$ $\partial V _ { j , t - 1 } ^ { * } \leq 1$

In less extreme cases, as $\delta _ { V }$ increases, $V _ { j , t } ^ { * } { } ^ { \prime } \mathbf { s }$ response to $V _ { j , t - 1 } ^ { * }$ decreases. If vulnerability depreciates slower (higher $\delta _ { V } )$ , the impact of $V _ { j , t - 1 } ^ { * }$ on $\boldsymbol { V } _ { j , t } ^ { * ^ { - } }$ decreases. It is similar to the case for $\delta ;$ if users are more forward look ing (higher δ), they use fewer CSP services in the current period owing to their concern for future vulnerability.

With this in mind, Figure 3 illustrates how CSP managers can track the crucial variables identified in Proposition 5 to design a vulnerability prediction algorithm. Specifically, the comparative statics discussed above for the factors and parameters impacting the model are listed on the left-hand side of Figure 3. In the center of Figure $^ { 3 , }$ corresponding real-world observations for each factor are listed. “Estimate users’ cloud productivity” is important to understand $b ( \cdot ) , b ^ { \prime } ( \cdot ) .$ , and $b ^ { \prime \prime } ( \cdot )$ “Track external risk factors” is useful to predict $p ( \cdot ) ,$ $p ^ { \prime } ( \cdot )$ , and $p ^ { \prime \prime } ( \cdot )$ (Howard 2023, Hubbard and Seiersen 2023). As stated previously, $p ^ { \prime \prime }$ plays an important role in the prediction as it is the weight on the large net profit/benefit from using the cloud, $b ( \cdot )$ . “Survey or estimate users’ risk preference” is to check whether users are more forward looking (higher δ). “Survey or estimate users’ attitudes toward past incidents” is to know vulnerability depreciation speed, $\delta _ { V } .$ . Successful cloud security requires a combination of marginal analysis, risk analysis, and dynamic decision making. Our results also highlight the theoretical importance of risk preferences (Hedlund 2000, Safi and Browne 2023) and cybersecurity behavior (Acquisti et al. 2017, Dutta and Sanyal 2023).

Figure 3. What Goes into the Vulnerability Prediction Box?  
![](/api/attachments/ZSUA4UZB/fulltext/images/7eebd96b2a85bcdcd4c114e13bd835280e541451a5cad99b4f93cc781b06cf00.jpg)  
Notes. This figure shows how our model can serve as a manual for designing a prediction algorithm for cloud vulnerability. The external shock that impact the users’ cloud productivity and cyber risk and the changes in users’ attitude toward the past and the future that impact the tota vulnerability results should enter the prediction algorithm, as in Proposition $5 ,$ where the dynamic path of total vulnerability is $\frac { \partial V _ { j , t } ^ { * } } { \partial V _ { j , t - 1 } ^ { * } } =$ b<sup>′</sup> (y<sub>i, t�1</sub>) <sup>∂p(V∗j, t�1</sup> <sup>)</sup><sub>∂V∗</sub> , � + b(y<sub>i, t�1</sub> ) <sup>∂2p(V∗j, t�1</sup> <sup>)</sup> =δδ b<sup>′</sup>(y ) <sup>∂p(V∗j, t)</sup> ∂<sup>2</sup>V<sup>∗</sup> ∂V<sup>∗</sup><sub>j, t</sub>

The purpose and subsequent actions stemming from such predictions are shown on the right-hand side of Figure 3. For $\mathrm { C S P }$ managers, predicting the vulnerability path helps in competing on security and maintaining business continuity. If the predicted vulnerability is not favorable, CSPs can adjust the total accumulated $S _ { j , t }$ . Section 5 discusses how CSPs target total accumulated $S _ { j , t }$ and its impact on competition. Alternatively, CSPs or social planners can require minimum contributions for all users. Two-factor authentication is an example. This raises issues related to compliance and the costly verification of compliance that are beyond the scope of our paper.

## 4.2. Users’ Behavior on the Optimal Path

The following propositions stem from the Euler equation and characterize the dynamics of the interdependent behavior of users in a shared security environment. Forward-looking users understand that their investment into security affects other users’ usage based on the new security level.

Proposition 6. On the optimal path of vulnerability, $V _ { j , t } ^ { * } ,$ equilibrium usage, $y _ { i , t } ^ { * } ,$ increases with the size of security umbrella $S _ { j , t } .$

$$
\frac {\partial y _ {i , t} ^ {*}}{\partial S _ {j , t}} > 0.
$$

The safer the CSP is as a whole, the more comfortable users are with increasing their usage. Furthermore, this finding is novel because it identifies a statebased strategic complementarity between $y _ { i , t } ^ { * }$ and $S _ { j , t } .$ Several implications follow. First, one can view security umbrella $S _ { j , t }$ as an impure public good because it provides a selective (private) benefit to user i in the form of increased $y _ { i , t }$ and $b ( y _ { i , t } )$ . Second, the increase in $S _ { j , t }$ need not be because of an increase in $s _ { i , t }$ . In other words, much of a user’s security umbrella and resulting increase in usage is because of the security investments of its CSP and other users. Finally, one cannot forget that a $\mathrm { C S P ^ { \prime } s }$ business model relies on usage fees; hence, security adds to the ${ \mathrm { C S P ' s } }$ value proposition by increasing $y _ { i , i }$ <sub>t</sub>. The resulting selective incentives stemming from the benefits of usage and charging for usage under the security umbrella establish cloud security as a novel impure public goods paradigm.

The impure nature of the shared security model impacts users’ behavior. The next proposition further clarifies the effect, which requires the following defini tion of a user’s accumulated individual security investment:

$$
S _ {i, t} = \sum_ {t} \delta_ {S} ^ {t} s _ {i, t} = s _ {i, t} + \delta_ {S} S _ {i, t - 1}.
$$

Proposition 7. A user’s vulnerability increases in any othe user’s accumulated security investment. For al $i ^ { \prime } \neq i , \dot { c } s p j ,$

$$
\frac {\partial v _ {i , t}}{\partial S _ {i ^ {\prime} , t}} > 0.
$$

Such increased vulnerability is of concern to users and CSPs, affecting their investment in security. Cloud user managers should evaluate the long-term risks associated with potential vulnerabilities when selecting CSPs. CSP managers should diligently monitor cloud security. The next subsection characterizes users’ opti mal investment in security. We examine CSPs’ optimal investment in security in Section 5.

## 4.3. Users’ Optimal Value Function with Respect to Security

Having characterized vulnerability, we now turn to user security. Recall from Proposition 1 that, owing to the potential for lock-in, a user’s per period payoff can either be increasing or decreasing in other users’ or thei ${ \mathrm { C S P ' s } }$ security investment (i.e., pure complements or pure substitutes). Yet, in a dynamic game, users maximize a value function, not per period payoffs, and the value function from period t onward is a function of state $( V _ { j , t - 1 } , S _ { j , t - 1 } )$ . Recall that Lemma 1 characterizes the behavior of users’ value function with respect to vulnerability state $V _ { j , t - 1 }$ as $\partial U _ { i } / \partial V _ { j , t - 1 } < 0$ . The following lemma characterizes the behavior of users’ value function with respect to security state $S _ { j , t - 1 }$

Lemma 2. A user’s optimal value function increases in accumulated security investment:

$$
\frac {\partial U _ {i} (V _ {j , t - 1} , S _ {j , t - 1})}{\partial S _ {j , t - 1}} = \delta_ {S} k > 0.
$$

Lemma 2 establishes that ${ \partial U _ { i } } / { \partial S _ { j , t - 1 } }$ is a constant. That is, there is no time- and state-dependent Euler equation with respect to the effect of current aggregate security on future aggregate security. The dynamics of shared security arise when security interacts with usage $( \mathrm { i . e . , }$ , the Euler equation for vulnerability) (Equation (12)).

When selecting a CSP, users need to assess not only current security capabilities but also potential longterm vulnerabilities. As the threat landscape evolves, the vulnerabilities in cloud infrastructures can also increase. To safeguard against this, it is advisable for user managers to avoid “keeping all their eggs in one basket.” For CSP managers, we suggest that cloud security needs monitoring, control, and testing; and we provide a way to design the vulnerability prediction algorithm. For this algorithm, we especially point out CSPs’ need for understanding users’ risk and time preferences.

As usage/vulnerability is predicated on security, we turn to the ${ \mathrm { C S P ' s } }$ security decision, which involves security’s effect on user lock-in, CSP competition, and the public goods paradigm underlying the shared security model.

## 5. Cybersecurity and Cloud Symbiosis

The previous section shows that security encourages users’ usage of the cloud and that the resulting vulnerability calls for close monitoring of cloud security. Moreover, CSPs’ motivations for contributing to the security umbrella differ from the “benevolent dictator” model of governmental provision of public goods. In particular, CSPs monetarily benefit from secure cloud usage and also strategically employ security to compete with other CSPs. In this section, we consider the case where users have the ability to switch CSPs $( \mathrm { i . e . , }$ $\lambda \in [ 0 , \infty ) )$ , and we characterize the $( S _ { j , t - 1 } , \lambda )$ pairs such that users do not switch. This produces symbiotic results, whereby the no-switching condition has implications for cumulative security investment, $S _ { j , t } ,$ , and cybersecurity, $p ( V _ { j , t } )$ , and the two variables lock in users via value creation under the CSP’s security umbrella, which users themselves help to create.

## 5.1. No-Switching Condition

We examine the no-switching constraint from the perspective of CSP 1 and its users. A similar analysis holds for CSP 2 and its users. Investment in security has two effects influencing a user’s choice to stay. First, it reduces the probability of a breach by reducing vulnerability, $V _ { 1 , t } ;$ second, it increases switching cost, $\lambda S _ { 1 , t - 1 } ,$ because of familiarity with the CSP’s security umbrella. The question is as follows. What level of CSP security investment satisfies the no-switching criterion? This is an economic factor affecting security design.

We define the no-switching constraint as follows. User i on CSP 1 chooses to stay if its optimal value on CSP 1 is greater than or equal to the optimal value generated by switching to CSP 2. Once again, the next-best alternative for users is another CSP because (i) our analysis is, effectively, ex post to the cloud/enterprise decision analyzed by August et al. (2014) and Zhang et al. (2020), among others, and (ii) once a user is in the cloud, the economics of the cloud make another CSP the logical next-best alternative.

Furthermore, instead of referring to the effect of CSP 1’s investment in security, $s _ { c s p 1 , t } ,$ on its no-switching constraint, we can instead refer to CSP 1’s choice of $S _ { 1 , t } .$ By backward induction, we solve for the $y _ { i , t } \mathrm { ' s }$ for CSP 1’s users and then, the $s _ { i , t } { ' } s$ for the same users. Given the $s _ { i , t } ^ { \phantom { } } { } ^ { \prime } \mathbf { s } ,$ , CSP 1’s choice of $s _ { c s p 1 , }$ <sub>t</sub> determines $S _ { 1 , }$ <sub>t</sub> because it is the only degree of freedom left. It follows that by backward induction, CSP 1 ultimately determines $S _ { 1 , t }$ It is similarly the case in period t � 1 for $s _ { c s p 1 , t - 1 }$ and $S _ { 1 , t - 1 }$ . Equivalent logic holds for CSP 2 with respect to $S _ { 2 , t }$ and $S _ { 2 , t - 1 }$ . Moreover, a CSP’s persistence in the market requires that its no-switching constraint is met. As providing security is costly for the CSP, we can focus on CSP 1’s choice of $S _ { 1 , t }$ to meet its no-switching constraint instead of its choice of $s _ { c s p 1 , t }$ to maximize its optimal value function.

In period t, if user i stays with CSP 1, its stage t payoff is

$$
u _ {i, t} ^ {s t a y} = [ 1 - c p (V _ {1, t}) ] b (y _ {i, t}) - k s _ {i, t},
$$

and then, the optimal value function of a user staying with CSP 1 is

$$
\begin{array}{c} U _ {s t a y} (V _ {1, t - 1}, S _ {1, t - 1}) = [ 1 - c p (V _ {1, t}) ] b (y _ {i, t}) - k s _ {i, t} \\ + \delta U (V _ {1, t}, S _ {1, t}). \end{array}
$$

If switching to CSP 2, the user’s stage t payoff is

$$
u _ {i, t} ^ {s w i t c h} = [ 1 - c p (V _ {2, t}) ] b (y _ {i, t}) - k s _ {i, t} - \lambda S _ {1, t - 1},
$$

and their optimal value function is

$$
\begin{array}{l} U _ {s w i t c h} (V _ {2, t - 1}, S _ {2, t - 1}, S _ {1, t - 1}) \\ = [ 1 - c p (V _ {2, t}) ] b (y _ {i, t}) - k s _ {i, t} - \lambda S _ {1, t - 1} + \delta U (V _ {2, t}, S _ {2, t}). \end{array}
$$

As an aside, in an oligopolistic situation, we would instead take the value of $\bar { u _ { i , t } ^ { s w i t c h } }$ for a CSP j user to be the value of the solution to

$$
\max _ {j ^ {\prime} \neq j} [ 1 - c p (V _ {j ^ {\prime}, t}) ] b (y _ {i, t}) - k s _ {i, t} - \lambda S _ {j, t - 1}.
$$

Lemma 3. From Lemma 2 and the definition of $U _ { s w i t c h } ,$

$$
\begin{array}{c} \frac {\partial U _ {s t a y} (V _ {1 , t - 1} , S _ {1 , t - 1})}{\partial S _ {1 , t - 1}} = \delta_ {S} k > 0 \\ \frac {\partial U _ {s w i t c h} (V _ {2 , t - 1} , S _ {2 , t - 1} , S _ {1 , t - 1})}{\partial S _ {1 , t - 1}} = - \lambda <   0. \end{array}
$$

Hence, CSP 1 selects $S _ { 1 , t - 1 }$ , understanding that a higher value helps to keep users from switching. However, the user ultimately makes the stay or switch decision by comparing $U _ { s t a y }$ and $U _ { s w i t c h }$ . By the onedeviation principle (Blackwell 1965), the no-switching condition holds in equilibrium if $U _ { s t a y } \geq U _ { s w i t c h }$ . Furthermore, in a symmetric MPE, if the one-deviation principle holds for user i, then no other CSP 1 user can benefit from switching. CSP 1 must at least ensure that

$$
U _ {s t a y} (V _ {1, t - 1}, S _ {1, t - 1}) = U _ {s w i t c h} (V _ {2, t - 1}, S _ {2, t - 1}, S _ {1, t - 1}).
$$

Lemma 4. CSP 1 must ensure that $S _ { 1 , t - 1 }$ is at least

$$
\begin{array}{l} S _ {1, t - 1} ^ {\min} = \frac {1}{\lambda} \Bigg \{\delta_ {S} k (S _ {2, t - 1} - S _ {1, t - 1} ^ {\min}) - \delta_ {V} b ^ {\prime} \{[ 1 - p (V _ {2, t}) c ] V _ {2, t - 1} \\ \qquad - [ 1 - p (V _ {1, t}) c ] V _ {1, t - 1} \} \\ \qquad + \frac {1}{2} \frac {\partial p (V _ {2 , t})}{\partial V _ {2 , t}} \delta_ {V} ^ {2} c b ^ {\prime} V _ {2, t - 1} ^ {2} \\ \qquad - \frac {1}{2} \frac {\partial p (V _ {1 , t})}{\partial V _ {1 , t}} \delta_ {V} ^ {2} c b ^ {\prime} V _ {1, t - 1} ^ {2} \Bigg \}. \end{array}
$$

Moreover, lock-in allows for cases where users will not switch, even though

$$
S _ {1, t - 1} <   S _ {2, t - 1}; V _ {1, t - 1} > V _ {2, t - 1}.
$$

Keeping a higher level of $S _ { j , t - 1 }$ increases users’ optimal value of staying and reduces their optimal value of switching. However, Lemma 4 shows that it is possible that a user stays even when the other CSP has more accumulated security investment and less accumulated vulnerability. The user is, indeed, locked in under their CSP’s security umbrella. Furthermore, when users do not switch in equilibrium, the resulting dynamics are as given in Section 3.

This is what we mean when we recommend that CSP managers should pay attention to users’ reactions to past cloud breaches and call for more behavioral research in security. The perception of vulnerability, security technology, and the future impact of current behavior determine the evolution of cloud security.

We now turn to a market characterization of CSP security.

Proposition 8. $S _ { 1 , t - 1 } ^ { m i n }$ and $S _ { 2 , t - 1 }$ are strategic complements:

$$
\frac {\partial S _ {1 , t - 1} ^ {m i n}}{\partial S _ {2 , t - 1}} = \frac {\delta_ {S} k}{\lambda + \delta_ {S} k} > 0.
$$

Hence, if CSP 2 increases its security, CSP 1 increases its security as well to keep users from switching.

At the same time, lock-in via a security umbrella reduces the intensity of security competition and, in turn, reduces equilibrium $S _ { j , t - 1 } ^ { m i n } .$ . To see this, without lock-in $( \lambda = 0 ) , \ \hat { \partial } S _ { 1 , t - 1 } ^ { m i n } / \partial S _ { 2 , t - 1 } = 1$ , and CSP 1 adjusts $S _ { 1 , t - 1 } ^ { m i n }$ to a change in $S _ { 2 , t - 1 }$ on a one-to-one basis. By contrast, for finite $\mathrm { ~  ~ \lambda ~ } \ne 0 , 0 < \partial S _ { 1 , t - 1 } ^ { m i n } / \partial S _ { 2 , t - 1 } < 1$ , and CSP 1 only partially adjusts to an increase in $S _ { 2 , t - 1 }$ . CSP security competition is neither a race to the bottom nor a war of increasing security levels. The no-switching requirements on security explain the former, and partial adjustment explains the latter. A partial reaction to the change in the security level of a rival—whether an increase or a decrease—indicates that security dynamics ultimately settle within a “Goldilocks” region for CSPs.

Our final basis of comparison is when the user is locked in (no switching is possible). In this case, $\lambda \to \infty$ , and by Lemma $4 , S _ { 1 , t - 1 } ^ { m i n } = 0$ : Intuitively, if users are locked in, then the no-switching constraint is not binding. If the no-switching constraint is not binding, the user’s participation constraint must instead bind. That is, security must be sufficient to induce the user to voluntarily participate. Voluntarily taking shelter in the cloud implies that users are not coerced into their relationships with CSPs.

From the Taylor expansion in the proof of Lemma 4, when a user is locked in,

$$
\begin{array}{r l} & U _ {1} (V _ {1, t - 1}, S _ {1, t - 1}) = \delta_ {S} k S _ {1, t - 1} - \delta_ {V} [ 1 - p (V _ {1, t}) c ] b ^ {\prime} V _ {1, t - 1} \\ & \qquad + \frac {1}{2} \frac {\partial P (V _ {1 , t})}{\partial V _ {1 , t}} \delta_ {V} ^ {2} c b ^ {\prime} V _ {1, t - 1} ^ {2}. \end{array}
$$

The PC requires $U _ { 1 , t - 1 } \geq 0$ . Solving this inequality for $S _ { 1 , t - 1 }$

$$
\begin{array}{c} S _ {1, t - 1} ^ {p c} = \frac {1}{\delta_ {S} k} \Bigg \{\delta_ {V} [ 1 - p (V _ {1, t}) c ] b ^ {\prime} V _ {1, t - 1} \\ - \frac {1}{2} \frac {\partial P (V _ {1 , t})}{\partial V _ {1 , t}} \delta_ {V} ^ {2} c b ^ {\prime} V _ {1, t - 1} ^ {2} \Bigg \}. \end{array}\tag{15}
$$

The PC for users of CSP 2 similarly requires

$$
\begin{array}{c} S _ {2, t - 1} ^ {p c} = \frac {1}{\delta_ {S} k} \Bigg \{\delta_ {V} [ 1 - p (V _ {2, t}) c ] b ^ {\prime} V _ {2, t - 1} \\ - \frac {1}{2} \frac {\partial p (V _ {2 , t})}{\partial V _ {2 , t}} \delta_ {V} ^ {2} c b ^ {\prime} V _ {2, t - 1} ^ {2} \Bigg \}. \end{array}\tag{16}
$$

In general, a user is effectively locked in if the PC for their CSP is the binding constraint. This raises the interesting possibility that users are effectively locked in under finite values of switching costs, λ. Verification necessitates a comparison of $S _ { j , t - 1 } ^ { m i n }$ versus $S _ { j , t - 1 } ^ { p c }$

Proposition 9. The user’s participation constraint is the binding constraint instead of the no-switching constraint, $S _ { j , t - 1 } ^ { p c } > S _ { j , t - 1 } ^ { m i n }$ , when the marginal cost of accumulated security from lock-in, λ, exceeds the marginal benefit of accumulated security for users, $\partial U _ { i } ( S _ { j , t - 1 } , \bar { V _ { j , t - 1 } } ) / \partial S _ { j , t - 1 }$ , which by Lemma 1, equals $\delta _ { S } k .$ . That is, the participation constraint is the binding constraint if

$$
\lambda > \delta_ {S} k.
$$

In this case, the users of both CSPs are effectively locked in.

Figure 4. (Color online) Platform Competition: The Lower Bound of Total Accumulated Security Investment  
![](/api/attachments/ZSUA4UZB/fulltext/images/6fbf18bf5937dfe309602ad9c4b13b40392b55b54c973cd2a4d94abbaa24a4b7.jpg)  
Notes. The figure shows the lower bound of security technology, the accumulated total security investment $S _ { j , t - 1 }$ when CSPs compete with security. The lower bound depends on the switching cost. When the switching cost λ is lower than the marginal benefit of accumulated security for users $\delta _ { S k }$ , the nonswitching condition $S _ { j , t - 1 } ^ { m i n }$ is bigger than the participation constraint $S _ { j , t - 1 } ^ { p c }$ , and when the switching cost is too high, the participating users will never switch.

Note first that lock-in is no longer akin to $\lambda \to \infty$ The requirement instead becomes $\lambda > \delta _ { S } k$ . Figure 4 shows two different sets of linear relationships between the no-switching constraint $S _ { j , t - 1 } ^ { m i n }$ and the participation constraint $S _ { j , t - 1 } ^ { p c } ,$ one for when switching cost λ is above the threshold and one for when λ is below it. If switching cost λ is high, the binding constraint is the participation constraint $S _ { j , t - 1 } ^ { p c }$ . As shown in Figure 4, the no-switching constraint is smaller than the participation constraint when λ is higher than the threshold; thus, the plane is less steep. In this case, the participation constraint is enough to lock in users because the no-switching constraint is smaller than the participation constraint in a flatter plane. Cloud user managers need to balance security with the potential for lock-in.

By contrast, if switching cost λ is instead lower than the marginal benefit of accumulated security for users, $\delta _ { S } k$ , the no-switching constraints are instead the binding constraints. The plane is steeper in Figure 4 because the no-switching constraint supersedes the participation constraint. As such, (i) users’ PCs are not binding, which is a welfare improvement as users are no longer held to their reservation utilities; (ii) the no-switching constraints are the mechanism for establishing nonmonopolistic platform competition (Lee 2014; Arce 2020, 2022); and (iii) if $S _ { j , t - 1 } < \bar { S } _ { j , t - 1 } ^ { m i n } ,$ , whereas $S _ { j ^ { \prime } , t - 1 } \geq S _ { j ^ { \prime } , t - 1 } ^ { m i n } ,$ the result is a monopoly outcome in favor of CSP $j ^ { \prime } .$ Cybersecurity is a driver of nonmonopolistic outcomes in CSP markets.

By extension, for heterogeneous users, the relevant economic variable is the marginal benefit of cumulative security of the marginal user (i.e., the user whose no-switching constraint is binding for the CSP). Furthermore, CSPs can do this by bolstering their security umbrella in two possible ways: increasing their own security investment and/or their users’ security investment. Examples capturing both possibilities include offering blockchains and homomorphic encryption to users. This suggests a hastening from subscriptionbased CSPs that turn users’ fixed costs into variable ones toward CSPs offering advantages under their security umbrella.

Finally, we assume that $\delta _ { V } < 1 ( \mathrm { i . e . } ,$ , old vulnerabilities are addressed over time). This may be as simple as taking them offline as annually occurs when, on average, 20% of an organization’s cloud attack surface is taken offline and replaced with new or updated services (Palo Alto Networks 2023). Instead, it is possible for a vulnerability to become more severe as time passes if left unaddressed and online.<sup>6</sup> Consequently, in Table 2, we address an extension where $\delta _ { V } > 1$ and its implications. The main effects of $\delta _ { V } > 1$ are as follows. First, from the Euler Equation (13), the larger δ is, the more it dampens $\partial V _ { j , t } \big / \partial V _ { j , t - 1 }$ via users’ under standing of the future impact of vulnerability. Second, the $\mathrm { C S P ^ { \prime } s }$ relative responsibility within the cloud stack, $\alpha ,$ offsets the negative impact of the persistence of vul nerability on its optimal value function. Third, the final two terms in the equation in Lemma 4 show that the sign of ${ \partial S _ { t - 1 } ^ { m i n } } / { \partial \delta _ { V } }$ is partially determined by the difference $V _ { 2 , t - 1 } ^ { 2 } \stackrel { \cdot } { - } V _ { 1 , t - 1 } ^ { 2 }$ . When this difference is positive, it is likely that $\partial S _ { t - 1 } ^ { \tilde { m i n } } / \partial \delta _ { V } > 0$ . Given that CSP 2 is CSP 1’s competitor, when $V _ { 2 , t - 1 } ^ { 2 }$ increases, CSP 2 addresses the problem by increasing its security, and CSP 1 responds in kind because of the strategic complements characterized by Proposition 8. The value of $\delta _ { V }$ determines the degree of the response. If vulnerabilities are addressed or taken offline over time, $\delta _ { V } < 1$ , the response is tempered, consistent with our “Goldilocks” result. If vulnerability persists and builds, $\delta _ { V } > 1$ , a race to the bottom or an arm’s race can result.

## 5.2. CSPs and the Path of Vulnerability

In the end, the combination of usage and security determines vulnerability. Furthermore, as shown in our analysis of the Euler equation for vulnerability, users’ consideration of the future impact of usage on vulnerability or lack thereof determines whether the path of vulnerability stays within a sustainable range or instead, explodes. The implications for CSPs are as follows.

Table 2. The Value of $\delta _ { V }$ Reflects How Vulnerability Is Addressed over Time

<table><tr><td> $\delta_V$  value</td><td>Implication</td><td>Long-term vulnerability path</td><td> $\frac{\partial\Pi_i(V_{j,t},S_{j,t})}{\partial V_{j,t-1}}=-\delta_V\frac{K}{\alpha}$ </td><td>Security competition</td></tr><tr><td> $\delta_V<1$ </td><td>Many vulnerabilities are not applicable in the next period as they have been addressed or taken offline. Residual vulnerability impacts through breach probability function  $p(V_t)$ .</td><td>Cloud vulnerability may explode, diminish, or converge depending on the degree of forward-looking behavior with respect to usage and security.</td><td>CSPs&#x27; share of security for their layer in the cloud stack,  $\alpha$ , matters less with respect to the buildup of vulnerability.</td><td>Tempered strategic complements settling in a “Goldilocks” range</td></tr><tr><td> $\delta_V>1$ </td><td>Vulnerabilities that are not addressed and remain online become a bigger problem in the next period, amplifying  $p(V_t)$ .</td><td>When cloud users understand that vulnerability accumulates quickly, there is a greater likelihood cloud security converges.</td><td>CSPs&#x27; share of security for their layer in the cloud stack,  $\alpha$ , matters more as it offsets  $\delta_V$ .</td><td>Intensified strategic complements with a race to the bottom or arm&#x27;s race possible</td></tr></table>

Given discount factor $\delta ,$ the CSPs’s value function is

$$
\Pi_ {j, t} (V _ {j, t - 1}, S _ {j, t - 1}) = \max _ {s _ {c s p j, t}} \{\pi_ {j, t} (\cdot) + \delta \Pi_ {j, t + 1} (V _ {j, t}, S _ {j, t}) \}.\tag{17}
$$

This is the ${ \mathrm { C S P } } ^ { \prime } { \mathrm { s } }$ Bellman equation expressed in terms of the optimal value function, $\begin{array} { r l } { \hat { \Pi } _ { j , t } ( V _ { j , t - 1 } , \hat { S } _ { j , t - 1 } ) ; } & { { } } \end{array}$ ; the currentperiod payoff, $\pi _ { j , t } = ( 1 - \tilde { p } ( V _ { j , t } ) \dot { C } ) n B ( \dot { y } _ { i , t } ) - K s _ { c s p j , t } ;$ and the discounted continuation value, $\delta \Pi _ { j , t + 1 } ( \dot { V } _ { j , t } , S _ { j , t } )$ (Table 2).

Proposition 10. CSP profits decrease in vulnerability at a constant rate equal to the discounted value of the cost/benefit ratio of CSP security:

$$
\frac {\partial \Pi_ {j} (V _ {j , t} , S _ {j , t})}{\partial V _ {j , t - 1}} = - \delta_ {V} \frac {K}{\alpha}.\tag{18}
$$

Table 3 illustrates the impact of different levels of the marginal contribution of CSP security investment, α. The value of α impacts users’ usage, users’ security contribution, and CSP’s security investment. Column 2 in Table 3 shows that users’ marginal benefit from the CSPs’ investment increases in α. Column 3 in Table 3 shows that users’ inclination to contribute to the security umbrella decreases in α. Column 4 in Table 3 shows that CSPs’ lifetime payoff is less sensitive to vulnerability as α increases. Overall, in an environment where CSPs’ marginal security contribution is higher than the users’ marginal security contribution, $\alpha > 1$ , both usage and vulnerability are higher.

The various values of α represent different layers in the cloud stack with different security technology architectures. CSP managers should realize the nature of the security technology, and we discuss why CSP managers should lower the complexity and reduce future security orchestration costs in Section 6.2 below.

Table 3. The Impact of Marginal CSP Security Contribution

<table><tr><td>α value</td><td> $\frac{\partial u_{i,t}}{\partial s_{cspj,t}}>0$ </td><td> $\frac{\partial u_{i,t}^{2}}{\partial s_{i,t}\partial s_{cspj,t}}<0$ </td><td> $\frac{\partial\Pi_{j}}{\partial V_{j,t-1}}<0$ </td><td>Influences</td></tr><tr><td>α = 2</td><td> $2b(y_{i,t})\frac{\partial p(V_{j,t})}{\partial V_{j,t}}[\delta_{V}^{t}]$ </td><td> $-2b(y_{i,t})\frac{\partial p^{2}(V_{j,t})}{\partial V_{j,t}^{2}}\delta_{V}^{t}$ </td><td> $-\delta_{V}\frac{K}{2}$ </td><td>Users are more inclined to increase usage and less inclined to contribute to the security umbrella. CSPs are less inclined to invest in security. Vulnerability increases.</td></tr><tr><td>α = 1</td><td> $b(y_{i,t})\frac{\partial p(V_{j,t})}{\partial V_{j,t}}[\delta_{V}^{t}]$ </td><td> $-b(y_{i,t})\frac{\partial p^{2}(V_{j,t})}{\partial V_{j,t}^{2}}\delta_{V}^{t}$ </td><td> $-\delta_{V}K$ </td><td>The outcome on vulnerability is neutral because there is no relative difference between the marginal impact of CPS vs. user contributions to the security umbrella.</td></tr><tr><td>α = 0.5</td><td> $0.5b(y_{i,t})\frac{\partial p(V_{j,t})}{\partial V_{j,t}}[\delta_{V}^{t}]$ </td><td> $-0.5b(y_{i,t})\frac{\partial p^{2}(V_{j,t})}{\partial V_{j,t}^{2}}\delta_{V}^{t}$ </td><td> $-2\delta_{V}K$ </td><td>Users are less inclined to increase usage and more inclined to contribute to the security umbrella. The platform is more motivated to invest in security. Vulnerability decreases.</td></tr></table>

Notes. CSPs can have amplified marginal effect on security investment from advanced security measures and promptly respond to emerging threats that lead to α > 1, and α < 1 can be because CSPs’ investment accelerates homogeneity that leads to correlated failure (Chen et al. 2011) The second column shows the users’ marginal benefit from CSP’s investment at different α’s. The third column is the marginal change in the user’s best reply with respect to CSP’s investment. The fourth column is the constant marginal cost of vulnerability for the platform.

Furthermore, as the only way that a CSP can directly decrease vulnerability is by increasing security, CSPs are in the business of providing security. Indeed, the proof of the proposition shows that a $\mathrm { C S P ^ { \prime } s }$ security investment only impacts its optimal value function by reducing total vulnerability. Hence, in no way can security be considered auxiliary to the CSP’s core value proposition. This can be seen in that the greater a CSP’s relative weight in providing shared security for the service in question, $\alpha ,$ the less vulnerability reduces CSP profits.

CSPs, therefore, face a trade-off in that increased usage both increases revenues and increases vulnerability. However, unlike $\begin{array} { r } { \frac { \bar { \partial } \bar { U _ { j } } ( \bar { V _ { j , t - 1 } } , \bar { S _ { j , t - 1 } } ) } { \partial V _ { j , t - 1 } } } \end{array}$ for users, which is a function of both $V _ { j , t - 1 }$ and $\dot { V } _ { j , t } ,$ , thereby leading to a Euler equation, there is no carryover from one period to the next for $\frac { \partial \Pi _ { j } ( \boldsymbol { V } _ { j , t - 1 } , S _ { j , t - 1 } ) } { \partial V _ { j , t - 1 } } .$ . From Proposition 5, vulnerability increases and builds upon itself through usage. It is of particular concern if users’ path of vulnerability is explosive. Indeed, it is ultimately indicative of a potential fallacy of composition stemming from users taking shelter within the cloud. The fallacy can occur because (i) aggregate vulnerability increases over time because the cloud itself becomes the attack surface, (ii) CSPs’ dynamic value function is decreasing in aggregate vulnerability, and (iii) users’ dynamic value function is decreasing in aggregate vulnerability. There is a difference between individual user benefits from taking shelter in the cloud and their aggregate implications. Ultimately, cloud security depends on whether users and cloud managers have the foresight to understand that the cloud is a dynamic shared security environment.

## 6. Variations on the Theme

In this section, we consider benefit and cost variations on the model. Specifically, what happens if (i) the public benefits of cloud security are determined by a weakest-link aggregator or if (ii) the costs of security investment are quadratic?

## 6.1. Weakest-Link Security

A variation on the security umbrella being a function of the sum of all participants’ security investment is that it is instead determined solely by the participant making the lowest investment (Varian 2004b). In contrast to summation, this security aggregator is known as weakest link, wherein the initial period $S _ { j , t } ^ { w l }$ is defined as

$$
S _ {j, t} ^ {w l} = \min \{\alpha s _ {c s p j, t}, s _ {i, t} | i \text { uses   CSP } j \}.\tag{19}
$$

For example, if all but one participant uses both survey (alphanumeric) passwords and multifactor authentication, but participant ℓ is using a lower level of security—no MFA—then the security umbrella is determined by par ticipant $\ell ^ { \prime } { \mathrm { s } }$ lowest level of security and participant $\ell ^ { \prime } { \mathrm { s } }$ alone. By definition, the use of MFA by everyone else has no effect on overall security.

Consequently, in equilibrium, all security investments are symmetric in the following way:

$$
\alpha s _ {c s p j, t} = s _ {i, t} = s _ {i ^ {\prime}, t} \forall i, i ^ {\prime} \mathrm{usingCSP} j.\tag{20}
$$

That is, security investments are strategic complements.

Cloud environments where the weakest link applies are as follows.

• The marginal impact of security investment on the security umbrella is zero for all but the one participant (ℓ) whose security investment is lowest (Hirshleifer 1983).

• Security investments among the CSP and its users are strategic complements by definition.

• The associated network is serial (i.e., no redundancy is built in (Hausken 2002)).

• There is one malicious actor. If instead, members are attacked by a population of malicious actors, the underlying weakest-leak aggregator is converted into a summation aggregator of security investment (Floreˆncio and Herley 2013), consistent with Equation (1), in which case all preceding results continue to hold. Anderson (2008) argues that defenders themselves (CSP and users) have an incentive to convert the weakest link into summation through increased security testing.

• The lone malicious actor has the expertise to exploit the vulnerability constituting the weakest link. Our interest lies in identifying when differences arise between summation and the weakest link and in identifying the intuition that carries from summation to the weakest link.

Given the dynamic nature of our analysis, the weakestlink version of the security umbrella, $\dot { S } _ { j , t } ^ { w l } ,$ , follows from applying the process of induction to Equation (19). That is,

$$
S _ {j, t} ^ {w l} = \min \{\alpha s _ {c s p j, t} + \delta_ {S} S _ {j, t - 1} ^ {w l}, s _ {i, t} + \delta_ {S} S _ {j, t - 1} ^ {w l} | i \text {uses CSPj} \}.\tag{1'}
$$

This expression differs significantly from that given for the security umbrella under summation $( S _ { j , t }$ in Equation (1)) because current contributions in period t $( s _ { c s p j , t } , s _ { i , t } , s _ { i ^ { \prime } , t } , \dots )$ are not added together in any period. Moreover, if there is no carryover from one period to the next, then $\delta _ { S } = 0$ . In this case, players would have to resolve all the coordination problems identified by Equation (20) and solved in previous periods. Irrespective of the value of $\delta _ { S } ,$ , the equilibrium levels of security investment in period t satisfy Equation (20).

To close the model, a user’s period t utility is again expressed as in Equation (4), with $S _ { j , t - 1 } ^ { w l }$ replacing $S _ { j , t - 1 }$ . The same replacement applies to the definition of cumulative vulnerability in Equation (2) and the Bellman equation in (8).

In terms of prior results, Proposition 4 characterizing the Euler equation for vulnerability continues to hold, as does Proposition 5 on the accumulated path of vulnerability because these results are derived for given levels of $S _ { j , t } , S _ { j , t - 1 } \not = 0$ no matter how they are constructed.<sup>7</sup>

Proposition 6 relating increasing usage to an increase in the size of the security umbrella, $S _ { j , t } ^ { w l } ,$ holds as well. Consequently, the characterization of security umbrella $S _ { j , t } ^ { w l }$ as a novel form of dynamic impure public good remains true. In summary, all main results on vulnerability dynamics in the cloud remain largely intact.

The exception is Proposition 7, relating increased usage to a marginal increase in security of any other user (or the CSP). It no longer holds because under the weakest link, unilateral marginal increases in $s _ { i , t }$ or $s _ { c s p j , t }$ do not change $S _ { j , t } ^ { w l }$ except if the change stems from the one participant whose security investment is uniquely lowest (participant ℓ).

Proposition 11. Under the weakest link, a user’s vulnerability only increases in participant ℓ’s security investment, $s _ { \ell , t }$

By contrast, in summation, vulnerability is increasing in the security investment of any individual participant and not just ℓ.

Finally, given that $S _ { j , t - 1 } ^ { w l }$ replaces $S _ { j , t - 1 }$ throughout, the weakest-link analog to Lemma 2 can be stated without proof.

Lemma 1 $\begin{array} { r l } { \pmb { 5 . } } & { { } \frac { \partial U _ { i } ( V _ { j , t - 1 } , S _ { j , t - 1 } ^ { w l } ) } { \partial S _ { j , t - 1 } ^ { w l } } = \delta _ { S } k = \frac { \partial U _ { s t a y } ( V _ { 1 , t - 1 } , S _ { 1 , t - 1 } ^ { w l } ) } { \partial S _ { 1 , t - 1 } ^ { w l } } } \end{array}$ and $\frac { \partial U _ { s w i t c h } ( V _ { 2 , t - 1 } , S _ { 2 , t - 1 } , S _ { 1 , t - 1 } ^ { w l } ) } { \partial S _ { 1 , t - 1 } ^ { w l } } = - \lambda .$

In comparing Lemmas 2 and 5, even though $S _ { j , t - 1 }$ and $S _ { j , t - 1 } ^ { w l }$ are constructed differently, users’ value functions change identically for identical marginal changes in $S _ { j , t - 1 }$ and $S _ { j , t - 1 } ^ { w l }$ . From a technical perspective, this implies that the Taylor expansions for $\hat { U } _ { s t a y } ( \mathrm { \hat { V } } _ { j , t - 1 } , S _ { j , t - 1 } )$ and $U _ { s w i t c h } ( V _ { j ^ { \prime } , t - 1 } , S _ { j ^ { \prime } , t - 1 } , S _ { j , t - 1 } )$ based on the partial derivatives in Lemmas 2 and 5 have similar structure, with $S _ { j , t - 1 } ^ { w l }$ replacing $S _ { j , t - 1 }$ for the case of the weakest link.

We turn now from characterizing vulnerability to characterizing security. From Equation (20), equilibrium security investment is symmetric under the weakest link: $\alpha s _ { c s p j , t - 1 } = s _ { i , t - 1 }$ . In addition, the CSP prefers that $S _ { j , t - 1 } ^ { w l }$ satisfies its no-switching constraint $( \mathrm { i . e . } , S _ { j , t } ^ { w l } =$ $S _ { j , t - 1 } ^ { m i n } \neq 0 ) ;$ ; otherwise, eventually, the CSP has no users. This raises the question of whether the CSP can set $\alpha s _ { c s p j , t - 1 }$ such that $s _ { i , t - 1 } = \alpha s _ { c s p j , t - 1 }$ and $S _ { j , t } ^ { w l } = S _ { j , t - 1 } ^ { m i n }$ . Multiple results in the extant literature show that this is the case. First, in the original treatment of the weakest link, Hirshleifer (1983) suggests that the preferences of one of the agents determine the outcome among the range of symmetric equilibria. The CSP can do this by contractually specifying $s _ { i , t - 1 } = \alpha s _ { c s p j , t - 1 }$ . Second, within an experimental/behavioral analysis of the weakest link, Harrison and Hirshleifer (1989) show that a sequential structure results in a subgame perfect equi librium where players coordinate on the observable action taken by the first mover. In the model under study, the $\mathrm { C S } \dot { \mathrm { P } }$ moves first in selecting its preferred security level. Third, within a dynamic learning context, Arce (2001) shows that leading by example facilitates coordination on the leader’s preferred outcome. Finally, in proposing the weakest link as one possible form of security technology, Varian (2004b) cites Sandler and Arce (2001), who show how preplay communication facilitates correlation of strategies. As the CSP is likely the only participant that knows who all of its users are, such communication falls to the CSP.

To recap, $\alpha s _ { c s p j , t - 1 }$ is such that $s _ { i , t - 1 } = \alpha s _ { c s p j , t - 1 }$ and $S _ { j , t - 1 } ^ { w l } = S _ { j , t - 1 } ^ { m i n } .$ . By Lemma $5 ,$ the Taylor series approximations of $\bar { U } _ { i } ( V _ { j , t - 1 } , S _ { j , t - 1 } ^ { w l } ) , U _ { s t a y } ( V _ { j , t - 1 } , S _ { j , t - 1 } ^ { w l } ) _ { i }$ , and $U _ { s w i t c h } ( V _ { j ^ { \prime } , t - 1 } , S _ { j ^ { \prime } , t - 1 } , S _ { j , t - 1 } ^ { w l } )$ share the same structures as $U _ { i } ( V _ { j , t - 1 } , S _ { j , t - 1 } ) , U _ { s t a y } ( \overleftarrow { V } _ { j , t - 1 } , S _ { j , t - 1 } )$ , and $U _ { s w i t c h } ( V _ { j ^ { \prime } , t - 1 } ,$ $S _ { j ^ { \prime } , t - 1 } , S _ { j , t - 1 } )$ ). It follows that the following market characterization of security competition between CSPs can be stated without proof because it closely follows the proof of Proposition 8.

Proposition 12. Under weakest-link security, the two $C S P { ^ { \prime } s }$ levels of security are strategic complements:

$$
\frac {\partial S _ {1 , t - 1} ^ {m i n}}{\partial S _ {2 , t - 1}} = \frac {\partial S _ {2 , t - 1} ^ {m i n}}{\partial S _ {1 , t - 1}} = \frac {\delta_ {S} k}{\lambda + \delta_ {S} k} > 0.
$$

Our findings on CSP security competition are robust to the weakest link. Hence, the discussion following Proposition 8 similarly applies (Table 4).

## 6.2. Quadratic Security Investment Cost

This subsection considers a variation whereby cybersecurity investments have quadratic costs. Quadratic costs potentially make security investments more grad ual than linear costs because quadratic costs can make it prohibitively costly to make lump sum security investments. At the same time, however, this does not imply that the cheapest security options are those implemented first because the marginal effect on generating profits under the security umbrella must also be taken into account, as does the no-switching constraint. By contrast, in dynamic global public goods games without selective incentives and no analog to the no-switching constraint, the cheapest technological solutions are im plemented first (Battaglini and Harstad 2016). Hence, quadratic costs have yet to be considered in our envi ronment of impure public goods. Moreover, irrespective of the cost structure, the weakest-link outcome always satisfies the equilibrium condition in Equation (20). We, therefore, return to the case where $S _ { j , t }$ is constructed from the sum of individual contributions as in Equation (1).

Table 4. Cost Function Comparison

<table><tr><td>Name</td><td>Functional form</td><td>Context</td><td>Results</td><td>Implications</td></tr><tr><td>Linear</td><td> $\Gamma_{i,t}(s_{i,t}) = k s_{i,t}$ </td><td>Cost function reflects the observed nature of security technology at the time of Neuhaus and Plattner (2013).</td><td> $S_{j,t-1}^{min}$  and  $S_{j',t-2}$  are strategic complements.</td><td>Security competition provides welfare improvement.</td></tr><tr><td>Quadratic</td><td> $\Gamma_{i,t}(S_{j,t},S_{j,t-1}) = \frac{k}{2}(S_{j,t}^2 - \delta_S^2 S_{j,t-1}^2) [s_{j,t} \text{ affects } S_{j,t} \text{ through Equation (1)}]$ </td><td>Lump sum security investment is less likely. Evolving security technology builds off the existing security stock and can be concentrated with the CSP (high α).</td><td>Degree of strategic complementarity diminishes.</td><td>Less security required to lock in users.</td></tr></table>

Cloud environments where quadratic security costs potentially arise include the following.

• Several open-source security technologies are widely adopted on a cloud platform. An update in these opensource security technologies means reconfiguration with all other security tools.

• Updates and additional security heavily depend on the complications of existing measures.

• Security responsibilities are shared but concentrated: for example, if the CSP has a large α.

In these scenarios, the marginal cost of increasing security depends on the whole technology. As such, the quadratic form better captures the costs of investment in security.

In dynamic analyses of public goods provision with evolving technology, Battaglini and Harstad (2016) propose an individual cost function $\Gamma _ { i , t } ( S _ { j , t } , S _ { j , t - 1 } )$ ) that depends on both technology (here, security) investment in current period $t , s _ { i , t } ;$ the state of existing technology, $S _ { j , t } ;$ and the technology stock, $S _ { j , t - 1 }$ . This implies that the marginal cost of user i depends on the total security level of the CSP, $S _ { j , t } ,$ where $s _ { i , t }$ contributes to $S _ { j , t }$ through Equation (1). For example, when a CSP sells a large body of active and interrelated security products, any change to security means rearchitecting and reorchestrating the complicated system of security tools. This results in the following quadratic cost function (Battaglini and Harstad 2016):

$$
\Gamma_ {i, t} (S _ {j, t}, S _ {j, t - 1}) = \frac {k}{2} (S _ {j, t} ^ {2} - \delta_ {S} ^ {2} S _ {j, t - 1} ^ {2}),
$$

implying that user i’s payoff at time t becomes

$$
u _ {i, t} = (1 - p (V _ {j, t}) c) b (y _ {i, t}) - \frac {k}{2} (S _ {j, t} ^ {2} - \delta_ {S} ^ {2} S _ {j, t - 1} ^ {2}) - \lambda S _ {j, t - 1},\tag{\( (4'') \}
$$

In contrast to constant marginal cost k in the linear setting, Battaglini and Harstad (2016) assume that the marginal cost of contributing to a public good is linear in the existing technology. Here, this translates into the marginal cost of security investment being linear in the existing security level, $\dot { S } _ { j , t } \mathrm { : }$

$$
\frac {\partial \Gamma_ {i , t} (\cdot)}{\partial S _ {j , t}} = k S _ {j, t}.
$$

Regarding prior results, Propositions 1–3 do not change. Compared with the linear cost function, increasing marginal cost implies a higher impact of $\delta _ { S } .$ . The lower the decay rate for security technology (higher $\delta _ { S } )$ , the more possible it is that a break in the plain complement relationship occurs over time. The initial characteristics of plain complements under both linear and quadratic cost function scenarios call for a dynamic horizon because plain complements may transform into plain substitutes as security measures accumulate. Given $S _ { j , t } , S _ { j , t - 1 } \neq 0 ,$ all main results on vulnerability continue to hold, as is the case for the weakest-link variation.

Quadratic costs do not change the conclusion of Lemma 2 as the users’ optimal value function remains increasing in accumulated security investment. What changes is that the marginal benefit of security technology for users is now linear in the stock of security technology.

Lemma 6. Under quadratic costs, the users’ marginal benefit from accumulated security is a function of the past technology stock,

$$
\frac {\partial U _ {i} (V _ {j , t - 1} , S _ {j , t - 1})}{\partial S _ {j , t - 1}} = \delta_ {S} ^ {2} k S _ {j, t - 1} \geq 0,
$$

implying in equilibrium that users benefit from technology that builds upon itself. Moreover,

$$
\frac {\partial U _ {i}}{\partial S _ {j , t - 1}} = \delta_ {S} ^ {2} k S _ {j, t - 1} \Rightarrow \frac {\partial^ {2} U _ {i}}{\partial S _ {j , t - 1} ^ {2}} = \delta_ {S} ^ {2} k, \frac {\partial U _ {i}}{\partial S _ {j , t - 1} \partial V _ {j , t - 1}} = 0.
$$

As Lemma $2$ is an intermediate result used to derive the values of $U _ { s t a y } ( V _ { j , t - 1 } , S _ { j , t - 1 } )$ and $U _ { s w i t c h } ( V _ { j ^ { \prime } , t - 1 } ,$ $S _ { j ^ { \prime } , t - 1 } , S _ { j , t - 1 } )$ ) via Taylor expansion, so too is Lemma 6 an intermediate result to derive these value functions for the case of quadratic costs. This alters the characterization of

CSP 1’s no-switching level of security in the following way.

Lemma 7. Under quadratic security costs, in order to satisfy the no-switching criterion, CSP 1 must ensure that $S _ { 1 , t - 1 }$ is at least $S _ { 1 , t - 1 } ^ { m i n \dagger }$ , where

$$
\left(1 + 2 \frac {1}{\lambda} \delta_ {S} ^ {2} k S _ {1, t - 1} ^ {m i n q}\right) S _ {1, t - 1} ^ {m i n q} = \frac {1}{\lambda} \delta_ {S} k S _ {2, t - 1} + [ \Psi + \Omega ]
$$

given Ψ and Ω as defined in the proof of Lemma 4.

A similar result holds for CSP 2. Both Lemmas 6 and 7 are intermediate results for characterizing the effect of quadratic costs on CSP security competition. In particular, we have Proposition 13.

Proposition 13. Under quadratic costs, the two CSP’s levels of security are strategic complements:

$$
\frac {\partial S _ {1 , t - 1} ^ {m i n q}}{\partial S _ {2 , t - 1}} = \frac {\delta_ {S} k}{\lambda (1 + 4 \frac {1}{\lambda} \delta_ {S} ^ {2} k S _ {1 , t - 1} ^ {m i n q})} > 0,
$$

with the degree of strategic complementarity diminishing for large $S _ { 1 , t - 1 } ^ { m i n q }$

If the cost of security investment is quadratic in the level of security, as security accumulates, average cost increases, and marginal cost exceeds average cost. This leads to diminishing returns on investment.

Hence, if the current state of security, $S _ { 1 , t - 1 } ^ { m i n q } ,$ , is large, competition only provides a limited incentive for increasing security because of the trade-off between the marginal benefit of security and increasing marginal costs stemming from the already large $S _ { 1 , t - 1 } ^ { m i n q }$ . This exaggerates the anticompetitive effect of switching costs by reducing the need to increase $S _ { 1 , t - 1 } ^ { m i n q }$ to prevent users from switching. Mathematically, in comparing the competitive effect on $S _ { 1 , t - 1 } ^ { m i n q }$ for quadratic costs and $S _ { 1 , t - 1 } ^ { m i n }$ for linear costs, $\frac { \partial S _ { 1 , t - 1 } ^ { m i n q } } { \partial S _ { 2 , t - 1 } } < \frac { \partial S _ { 1 , t - 1 } ^ { m i n } } { \partial S _ { 2 , t - 1 } }$ . It is easier to use security to lock in users under quadratic costs. User managers should be concerned if future security investment involves updating a complicated security architecture.

## 7. Conclusion

We study the nature of shared cloud security and cloud security competition among platforms. By its very nature, cloud security is a shared security model, meaning that security is a public good created by users’ and their ${ \mathrm { C S P ' s } }$ collaborative contributions. Furthermore, cloud security is provided within a competitive environment and is an impure public good in that selective incentives—in the form of user profits created by operating within the cloud and CSP profits for operating the cloud—are joint products stemming from cloud security. In addition, cloud security takes place within a dynamic environment. Users trade fixed costs for variable costs that change with on-demand usage and capacity over time. Finally, competitive provision of cloud security and the potential for lock-in imply that users’ security investments can be either strategic complements or strategic substitutes in any given period. In this way, cloud security stands apart as a public goods paradigm, as enumerated in Table 5.

## 7.1. Implications

We adopt a novel lens theorizing cloud security as an impure public good paradigm and provide practical guidelines for cloud managers. Table 6 summarizes our findings. We discuss them in terms of theoretical and managerial implications.

7.1.1. Theoretical Implications. Rather than deterministically creating a public good, users’ and CSP security investments jointly determine breach probabilities. That is, users and their CSP have joint responsibility in creating a public good that we call the “security umbrella,” under which users and their CSP conduct cloud-related activities. Notably, the private benefits (profits) from operating under the security umbrella or operating the cloud itself make cloud security a form of impure public good. The fact that these private benefits are not functionally tied to individual contributions but stem from the security umbrella sets cloud security apart from how selective incentives manifest themselves in traditional models of impure public goods.

Indeed, it is also the case that one can think of the security umbrella as the creation of a commons because private usage of the cloud under the security umbrella is an individual decision. Increased usage increases vulnerability, which is a function of both usage and security. In this way, overexploitation of the commons has a dynamic analog in our model in the form of a potentially explosive path of vulnerability. What keeps vulnerability in check is (i) contributions to shared security, which is an institutional arrangement in the sense of Ostrom (1990), and (ii) managerial understand ing of the dynamic implications of cloud usage, an insight resulting from our theoretical approach.

Our methodology is closest to the dynamic analysis of homogeneous contributors providing global (environmental) public goods in Battaglini and Harstad (2016). Obvious theoretical differences include user-CSP asymmetry and CSP security competition. Enhancing security reduces expected breaches for CSPs as well, but CSPs also use security as a feature to compete for more users, charge for more usage, and potentially lock users in. The private incentives of CSPs differ substantially from that of governmental provision of public goods a \` la Samuelson (1954). In sum, our findings contribute to the public goods literature by characterizing dynamic collective action with asymmetric contributors whose private benefit depends upon a probabilistic public good (i.e., the cloud security paradigm).

Table 5. Cloud Security as a Public Goods Paradigm

<table><tr><td>Factor</td><td>Reference</td><td>Implications</td><td>CSP variation</td></tr><tr><td>Role of government intervention in providing public goods</td><td>Samuelson (1954)</td><td>As private markets tend to underprovide public goods because of the free-rider problem, public goods are ideally provided by the government.</td><td>Cloud security is a public good involving joint responsibilities by asymmetric private entities (CSP and users).</td></tr><tr><td>Selective incentives</td><td>Olson (1965)</td><td>Selective incentives tied to individual contributions can diminish free riding.</td><td>Individual contributions create a “cloud security umbrella” under which all parties involved derive selective incentives (profits). Furthermore, these selective incentives can create their own set of problems in the form of increased vulnerabilities if users ignore the future implications of their actions.</td></tr><tr><td>Private solutions</td><td>Ostrom (1990)</td><td>When actions to create private benefits also create public costs—known as a commons—voluntary organizations can do a better job of governing the commons than markets or government intervention.</td><td>Actions to create a public good (cloud security umbrella) come at a private cost. Selective incentives in the form of profits and market incentives in the form of no-switching conditions on CSP security investment are the mechanisms for shared responsibility in the cloud.</td></tr><tr><td>Impure public goods</td><td>Cornes and Sandler (1994)</td><td>Individual contributions create both a public good available to all and a private benefit (selective incentive) specific to the contributor and their level of contribution. Turns individual contributions into strategic complements.</td><td>Individual contributions to the security umbrella create public goods by reducing breach probabilities. Expected selective incentives stemming from usage and charging for usage are not specific to the contributor or their level of contribution. Individual contributions can be strategic complements or substitutes.</td></tr><tr><td>Dynamic analysis of providing global public goods</td><td>Battaglini and Harstad (2016)</td><td>International environmental agreements and protocols can overcome free riding of homogeneous contributors over time.</td><td>User-CSP asymmetry, where the public good stemming from shared responsibility is exclusive to the platform. No switching constraint binds, whereas it is vacuous in a global context.</td></tr><tr><td>Evolving technology</td><td>Battaglini and Harstad (2016)</td><td>Relaxing functional form—quadratic costs do not drive the results.</td><td>Users&#x27; time path of vulnerability and strategic complementarity in CSP security competition are robust to quadratic costs and weakest-link aggregation technology.</td></tr></table>

7.1.2. Managerial Implications. Our paper provides actionable managerial implications. Characterizing shared security as an impure public good differentiates cloud security from on-premises counterparts. Cloud users should consider long-term security and avoid keeping all their eggs in one basket as cloud vulnerability increases. Consequently, although the current cybersecurity mantra is to take refuge in the cloud, we anticipate a future point of inflection involving judicious cloud repatriation or CSP diversification rather than full retrenchment.

In the near term, our theoretical findings provide guidelines for designing a vulnerability algorithm emphasizing CSPs’ need to understand users’ risk and time preferences. The observables include tracking external factors normally employed in cyber risk prediction. We also recommend including estimates of users’ cloud productivity and attitudes toward past incidents. These needs call for more behavioral research in cybersecurity.

Furthermore, we find that CSPs’ efforts to keep users from switching result in economically determined

Table 6. Summary of Findings and Contributions

<table><tr><td>Aspect under study</td><td>Findings</td><td>Theoretical implications</td><td>Current practice</td><td>Practical implications</td></tr><tr><td>Selective incentive</td><td rowspan="2">Whether security investments among users or by users and the CSP itself are strategic substitutes or complements in any given period depends on the future potential for lock-in.Shared security is an impure public good where asymmetric actors (CSP and users) generate selective incentives for themselves and others, the latter being a unique property of cloud security as an impure public good.Vulnerability can explode in equilibrium.The dynamic path depends on external risk and users&#x27; cloud productivity, risk, and time preferences.</td><td rowspan="2">Instead of vulnerability being an exogenous parameter, as is the case in analyses of optimal security expenditure, it is now a strategic variable determining a Markov state in each period.The public good enters the utility function through a breach probability function.Selective incentives (CSP and user profits) hinge on the public good (security umbrella).Marginal values of selective incentives characterize the time path of vulnerability through the Euler equation.</td><td rowspan="2">Shared responsibility model with limited platform liability.Many users take refuge in the cloud without understanding the shared responsibility model.No existing tool considers all these dynamic factors.</td><td rowspan="4">Cloud security needs monitoring, control, and testing that is different from on-premises counterparts because of shared responsibility for a virtual and ephemeral environment.Users should consider long-term vulnerability when choosing CSP usage and their own security investment.Judiciously repatriate cloud assets to avoid keeping all eggs in one basket as cloud vulnerability increases.Provide a way to design the prediction algorithm. The algorithm can be found in Figure 3.CSPs should understand users&#x27; risk and time preferences.CSP security investments and products are indicators of competition.Users need to balance security with the potential for lock-in.CSP managers need to recognize that security competition is neither a race to the bottom nor an arm&#x27;s race. Markets and levels within the cloud stack can be stratified in terms of security.Shared responsibility varies with layers in the cloud stack.CSP managers should recognize the nature of the security technology and related costs. They should aim to lower the complexity of security architecture and reduce future orchestrating costs.</td></tr><tr><td>Long-term security pattern</td></tr><tr><td>CSP competition</td><td>CSP efforts to keep users from switching result in economically determined security requirements.Security facilitates a nonmonopolistic CSP market with strategic complements in security competition between CSPs.Lock-in effect of security undermines the effect of competition.</td><td>Include security as a strategic variable in models of platform competition.CSP competition reduces security underprovision without governmental intervention.CSPs are not government; they benefit from safe operation through selective incentives.</td><td>Model is consistent with the coexistence of major cloud providers: Amazon Web Services, Microsoft Azure, and Google Cloud.</td></tr><tr><td>Evolving security technology</td><td>CSPs and users have different marginal productivities of security investment.Provides an explanation of the disparity between security technology and security results.With quadratic cost, strategic security competition is weaker.</td><td>Security technology affects competition by changing the cost function.Security technology has a lock-in effect.</td><td>CSPs are rapidly dominating security technology by selling security services, as in Table 7.</td></tr></table>

Table 
7. Security Competition: Expanding Security Services Offered by Cloud Service Providers

early-on security services is done by using the Wayback Machine Internet Archive. The previously existing services are highlighted in bold. Notes. The table shows that quickly developing new security products is a focus for all three main CSPs: AWS, Azure, and Google Cloud. The access day was July 17th, 2023. The comparison of

security requirements facilitating a nonmonopolistic market. However, the lock-in effect of security investments undermines the effect of competition. Cloud security can be used as an indicator of competition, and user managers need to recognize the lock-in effect of security technology.

Surprisingly, the level of security needed to lock in users can be greater than that required to participate in the CSP. This is an unexpected welfare improvement stemming from lock-in. Our results also provide an explanation of how shared responsibility varies between layers in the cloud stack.

The last two columns in Table 6 contain our suggestions regarding current cloud security practices. For users, cloud security within a shared security model should not be regarded the same as on-premise security but as a public good reflecting interdependence with other users and their CSP. When selecting CSPs and determining the best security practices to implement with a CSP, it is crucial for users to assess the long-term risks associated with potential vulnerabilities.

For CSPs, cloud security should be diligently monitored if for no other reason than to transform security from a weakest-link model of shared security into a summation model (Anderson 2008).

Otherwise, noncommensurate behavior by users would completely offset the effects of these security products. In such an environment, cloud security is a priority for CSP managers as it becomes a marketing point in addition to being an operational goal along with reliability. Coming full circle, user managers need to realize that they can be locked into a less secure CSP than prescribed by their risk preferences. User practices to counteract lock-in include hybrid clouds, cloud brokers, and containerization (Arce 2022).

The complexity of security technology also determines the long-term health of security technology development. If security technology architecture is too complicated and if the orchestrating cost for each update is too high, the positive effect of competition on security is diminished. We encourage CSP managers to review the technical logic underlying their expanding line of security products in Table 7 and to consider a product environment where core security technology is compartmentalized so that it does not trigger increasing marginal costs for future security investments.

## 7.2. Limitations and Future Directions

Our study is subject to a few limitations.

For example, we address user-CSP asymmetry, which relaxes the traditional assumption of homogeneous players in dynamic public goods games, but we do not consider user heterogeneity. With user heterogeneity, a difference arises between the actions of the marginal user and the average user, which affects efficiency.

Moreover, heterogeneous users may sort themselves into CSP clubs.

Similarly, although the selective incentives we identify lessen the need for government intervention in security provision, government intervention or open standards can lessen the resulting effect of security lock-in. Little is known about the current state of security technology on cloud platforms and the extent of lock-in effects. Multihoming and security costs of multihoming are also interesting extensions as little is known about the relationship between interoperability and security as well as its competitive consequences. We see potential in future work to improve our understanding of different paths of cloud security technology development and their impact on the nature of the shared security environment.

We provide a generalizable model where these variations are possible, and we leave these important variations for future study.

## 7.3. Concluding Remarks

We provide a dynamic model for examining shared cloud security in terms of both contributions to an impure public good by a cloud security provider and its users and security as a strategic variable in cloud services competition. Specifically, we identify state-based strategic complementarities stemming from these phenomena as determining the long-term path of cloud security. Overall, this study provides a novel understanding of the role of security in the cloud, highlighting it as a new form of public goods paradigm. These findings have important implications for both cloud and user managers for sharing responsibility for cloud security.

## Endnotes

<sup>1</sup> Undirected risk associated with on-site versions stems from malicious actors targeting many individual users in any system running the version. Directed risk stems from malicious actors targeting a particular cloud system version, thereby affecting many organizations at once.

<sup>2</sup> See https://www.cisa.gov/news/2022/02/09/cisa-fbi-nsa-andinternational-partners-issue-advisory-ransomware-trends-2021.

<sup>4</sup> The phrase is attributed to bank robber Willy Sutton, who was one of the first to appear on the FBI’s “Most Wanted” list.

<sup>6</sup> We thank an anonymous reviewer for raising this issue.

<sup>7</sup> As Equation (20) holds for $\alpha s _ { c s p j , t } = s _ { i , t } = 0 ,$ , we establish $S _ { j , t } ^ { w l } , S _ { j , t - 1 } ^ { w l } \neq 0$ below.

## References

Acquisti A, Adjerid I, Balebako R, Brandimarte L, Cranor LF, Koman duri S, Leon PG, et al. (2017) Nudges for privacy and security: Understanding and assisting users’ choices online. ACM Comput. Surveys 50(3):1–41.

Al-Otaibi YD (2021) A shared two-way cybersecurity model for enhancing cloud service sharing for distributed user applications. ACM Trans. Internet Tech. 22(2):1–17.

Almorsy M, Grundy J, Mu¨ ller I (2016) An analysis of the cloud computing security problem. Proc. APSEC 2010 Cloud Workshop (Sydney, Australia).

Anderson R (2001) Why information security is hard—An economic perspective. Seventeenth Annual Comput. Security Appl. Conf. (IEEE, Piscataway, NJ), 358–365

Anderson R (2008) Security Engineering: A Guide to Building Dependable Distributed Systems (John Wiley & Sons, Hoboken, NJ).

Andreoni J (1990) Impure altruism and donations to public goods: A theory of warm-glow giving. Econom. J. 100(401):464–477.

Arce DG (2001) Leadership and the aggregation of international col lective action. Oxford Econom. Papers 53(1):114–137.

Arce DG (2018) Malware and market share. J. Cybersecurity 4(1): tyy010.

Arce DG (2020) Cybersecurity and platform competition in the cloud Comput. Security 93:101774.

Arce DG (2022) Security-induced lock-in in the cloud. Bus. Inform. Systems Engrg. 64(4):501–513.

Asghari H, van Eeten M, Bauer JM (2016) Economics of cybersecurity Bauer JM, Latzer M, eds. Handbook on the Economics of the Internet (Edward Elgar Publishing, Cheltenham, UK), 11–41.

August T, Niculescu MF, Shin H (2014) Cloud implications on soft ware network structure and security risks. Inform. Systems Res. 25(3):489–510.

Battaglini M, Harstad B (2016) Participation and duration of environmental agreements. J. Political Econom. 124(1):160–204.

Benveniste LM, Scheinkman JA (1979) On the differentiability of the value function in dynamic models of economics. Econometrica 47(3):727–732.

Bernheim BD, Peleg B, Whinston MD (1987) Coalition-proof Nash equilibria. I. Concepts. J. Econom. Theory 42(1):1–12.

Blackwell D (1965) Discounted dynamic programming. Ann. Math. Statist. 36(1):226–235

Blumenthal MS (2011) Is security lost in the clouds? Comm. Strategies 1(81):69–86.

Cansever D (2020) Security games with insider threats. Zhu Q, Baras JS, Poovendran R, Chen J, eds. Internat. Conf. Decision Game Theor Security (Springer, Berlin, Heidelberg), 502–505.

Cavusoglu H, Raghunathan S, Yue WT (2014) Decision-theoretic and game-theoretic approaches to IT security investment. J. Management Inform. Systems 25(2):281–304.

Chen Py, Kataria G, Krishnan R (2011) Correlated failures, diversification, and information security risk management. MIS Quart. 35(2):397–422.

Cornes R, Sandler T (1994) The comparative static properties of the impure public good model. J. Public Econom. 54(3):403–421.

Crowdstrike (2023) 2023 Cloud risk report. Technical report, Crowdstrike Austin, TX.

Dechert WD (1997) Non cooperative dynamic games: A control theoretic approach. Working paper, University of Houston, Houston.

Dutta A, Sanyal P (2023) Examining the effects of virtual work on cybersecurity behavior. SAIS 2023 Proc. 21 (AIS Electronic Library, Atlanta).

Eaton B (2002) Applied Microeconomic Theory: Selected Essays of B. Curti Eaton (Edward Elgar Publishing, Cheltenham, UK).

Fedele A, Roner C (2022) Dangerous games: A literature review on cybersecurity investments. J. Econom. Surveys 36(1):157–187.

Floreˆncio D, Herley C (2013) Where do all the attacks go? Schneier B, ed. Economics of Information Security and Privacy III (Springer, New York), 13–33.

Friedman JW (1976) Oligopoly and the Theory of Games, vol. 8 (North Holland, Amsterdam).

Garcia A, Sun Y, Shen J (2014) Dynamic platform competition with malicious users. Dynam. Games Appl. 4(3):290–308.

Gariba ZP, Van Der Poll JA (2017) Security failure trends of cloud computing. 2017 IEEE 3rd Internat. Conf. Collaboration Internet Comput. (CIC) (IEEE, Piscataway, NJ), 247–256.

Geer D, Jardine E, Leverett E (2020) On market concentration and cybersecurity risk. J. Cyber Policy 5(1):9–29.

Gordon LA, Loeb MP (2002) The economics of information security investment. ACM Trans. Inform. System Security 5(4):438–457.

Harrison GW, Hirshleifer J (1989) An experimental evaluation of weakest link/best shot models of public goods. J. Political Econom. 97(1):201–225.

Harstad B (2012) Climate contracts: A game of emissions, investments, negotiations, and renegotiations. Rev. Econom. Stud. 79(4):1527–1557.

Haurie A, Krawczyk JB, Zaccour G (2012) Games and Dynamic Games, vol. 1 (World Scientific Publishing, Singapore).

Hausken K (2002) Probabilistic risk analysis and game theory. Risk Anal. 22(1):17–27.

Hedlund J (2000) Risky business: Safety regulations, risk compensation, and individual behavior. Injury Prevention 6(2):82–89.

Heitzenrater C, Simpson A (2016a) A case for the economics of secure software development. Gates C, Bohme R, Egelman S, Mannan M, eds. Proc. 2016 New Security Paradigms Workshop (ACM, New York), 26–29.

Heitzenrater C, Simpson A (2016b) Software security investment: The right amount of a good thing. 2016 IEEE Cybersecurity Develop ment (SecDev) (IEEE, Piscataway, NJ), 53–59.

Hirshleifer J (1983) From weakest-link to best-shot: The voluntary provision of public goods. Public Choice 41(3):371–386.

Howard R (2023) Cybersecurity First Principles: A Reboot of Strategy and Tactics (John Wiley & Sons, Hoboken, NJ).

Hubbard DW, Seiersen R (2023) How to Measure Anything in Cybersecu rity Risk (John Wiley & Sons, Hoboken, NJ).

IBM (2023) Cost of a data breach. Technical report, IBM Security, Armonk, NY.

Josa-Fombellida R, Rinco´n-Zapatero JP (2008) Markov perfect Nash equilibrium in stochastic differential games as solution of a generalized Euler equations system. Universidad Carlos III de Madrid Working Paper 08-67 Series 31, Calle Madrid, Getafe, Spain.

Kahn CM, Mookherjee D (1992) The good, the bad, and the ugly: Coa lition proof equilibrium in infinite games. Games Econom. Behav. 4(1):101–121.

Lee RS (2014) Competing platforms. J. Econom. Management Strategy 23(3):507–526.

Lookabaugh T, Sicker DC (2004) Security and lock-in. Camp LJ, Lewis S, eds. Economics of Information Security, Advances in Information Security, vol. 12 (Springer, Boston), 225–246.

McKay A, Nakamura E, Steinsson J (2017) The discounted Euler equation: A note. Economica 84(336):820–831.

Neuhaus S, Plattner B (2013) Software security economics: Theory, in practice. Bo¨hme R, ed. The Economics of Information Security and Privacy (Springer, Berlin), 75–92.

O’Donnell AJ (2008) When malware attacks (anything but windows). IEEE Security Privacy 6(3):68–70.

Olson M (1965) The Logic of Collective Action: Public Goods and the Theory of Groups, vol. 124 (Harvard University Press, Cambridge, MA).

Opara-Martins J, Sahandi R, Tian F (2014) Critical review of vendor lock-in and its impact on adoption of cloud computing. Shoniregun CA, ed. Internat. Conf. Inform. Soc. (i-Society 2014) (IEEE, Piscataway, NJ), 92–97.

Opara-Martins J, Sahandi R, Tian F (2016) Critical analysis of vendor lock-in and its impact on cloud computing migration: A business perspective. J. Cloud Comput. 5(1):1–18.

Ostrom E (1990) Governing the Commons: The Evolution of Institutions for Collective Action (Cambridge University Press, Cambridge, UK).

Palo Alto Networks (2023) Unit 42 attack surface threat report. Techni cal report, Palo Alto Networks, Santa Clara, CA.

Ponemon Institute (2014) Data breach: The cloud multiplier effect. Technical report, Ponemon Institute, Traverse City, MI.

Safi R, Browne GJ (2023) Detecting cybersecurity threats: The role of the recency and risk compensating effects. Inform. Systems Frontiers 25(3):1277–1292

Samuelson PA (1954) The pure theory of public expenditure. Rev Econom. Statist. 36(4):387–389.

Sandler T, Arce D (2001) Transnational public goods: Strategies and institutions. Eur. J. Political Econom. 17(3):493–516.

Sen R, Verma A, Heim GR (2020) Impact of cyberattacks by maliciou hackers on the competition in software markets. J. Management Inform. Systems 37(1):191–216.

Shapiro C, Varian HR (1998) Information Rules: A Strategic Guide to the Network Economy (Harvard Business Press, Boston)

Stoneburner G, Goguen A, Feringa A (2002) Risk management guide for information technology systems. NIST Special Publication Report No. 800-30, NIST, Gaithersburg, MD.

Tajalizadehkhoob S, Van Goethem T, Korczyn´ski M, Noroozian A, Bo¨hme R, Moore T, Joosen W, van Eeten M (2017) Herding vulnerable cats: A statistical approach to disentangle joint responsibility for web security in shared hosting. Proc. 2017 ACM SIGSAC Conf. Comput. Comm. Security (Special Interest Group on Security, Audit and Control (SIGSAC), Dallas, TX), 553–567.

Tianfield H (2012) Security issues in cloud computing. Wang J, Milla´n JdR, Choi S, eds. 2012 IEEE Internat. Conf. Systems Man Cybernetic (SMC) (IEEE, Piscataway, NJ), 1082–1089.

Tilley A, McMillan R (2022) Microsoft’s new security chief says it is time to take shelter in the cloud. Wall Street J. (February 23), B1.

Torkura KA, Sukmana MI, Cheng F, Meinel C (2021) Continuous auditing and threat detection in multi-cloud infrastructure. Comput. Security 102:102124.

Varian HR (2004a) Competition and market power. Varian HR, Farrell J, Shapiro C, eds. The Economics of Information Technology: An Introduction, Raffaele Mattioli Lectures (Cambridge University Press Cambridge, UK), 1–48.

Varian HR (2004b) System reliability and free riding. Camp LJ, Lewis S, eds. Economics of Information Security, Advances in Information Security, vol. 12 (Springer, Boston), 1–15.

Vasek M, Wadleigh J, Moore T (2015) Hacking is not random: A casecontrol study of webserver-compromise risk. IEEE Trans. Dependable Secure Comput. 13(2):206–219.

Wilms K, Stieglitz S, Ma¨ller B (2018) Feeling safe on a fluffy cloud: How cloud security and commitment affect users switching intention. Proc. Thirty Ninth Conf. Inform. Systems (ICIS, San Francisco).

Wiz (2023) 2023 state of the cloud. Technical report, Wiz, New York

Zhang Z, Nan G, Tan Y (2020) Cloud services vs. on-premises software: Competition under security risk and product customization. Inform. Systems Res. 31(3):848–864

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
