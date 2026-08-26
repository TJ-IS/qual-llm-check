---
otero_id: 4302
otero_key: "BVAPNAF6"
title: "Risks and Benefits of Signaling Information System Characteristics to Strategic Attackers"
authors: "Marco Cremonini; Dmitri Nizovtsev"
year: "2009"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222260308"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Risks and Benefits of Signaling Information System Characteristics to Strategic Attackers

## Marco Cremonini & Dmitri Nizovtsev

To cite this article: Marco Cremonini & Dmitri Nizovtsev (2009) Risks and Benefits of Signaling Information System Characteristics to Strategic Attackers, Journal of Management Information Systems, 26:3, 241-274

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222260308

![](/api/attachments/BVAPNAF6/fulltext/images/0a26a61e4ee56d25d02d73cf8700dc8c32dcb547112cc24349a51aad83ae87f4.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/BVAPNAF6/fulltext/images/6ff1bd9af74ae174bea5de11c5ecab01ed41b2ba1835c9c0809792d15f00795a.jpg)

Submit your article to this journal ↗

![](/api/attachments/BVAPNAF6/fulltext/images/3c6eb74f5a8a8fa59b142e03f81ced5bf3ed19f0f3ecce872f5853530848174a.jpg)

Article views: 31

![](/api/attachments/BVAPNAF6/fulltext/images/60f709011dbf2cb06d0898f3ec152d6b2b9acb8445f437237e0b75b1175cd112.jpg)

View related articles ↗

![](/api/attachments/BVAPNAF6/fulltext/images/13452e2029e2ca1a34aa9ae457d80ee60c6a6c8b5d1225563f7408dfa240b5c9.jpg)

Citing articles: 2 View citing articles ↗

# Risks and Benefits of Signaling Information System Characteristics to Strategic Attackers

MARCO CREMONINI AND DMITRI NIZOVTSEV

MARCO CREMONINI is an Assistant Professor at the Department of Information Technology of the University of Milan, Italy. He received his Ph.D. in electronic and information technology engineering at the University of Bologna. He previously worked as a Research Assistant at the Institute for Security Technology Studies (ISTS) of Dartmouth College. His research activity is focused on network security, economic aspects of security technologies, privacy, and security in ubiquitous computing.

DMITRI NIZOVTSEV is an Associate Professor at the Washburn University School of Business in Topeka, Kansas. He holds a Ph.D. in economics from Purdue University. His research interests are in applied microeconomics, industrial organization, and economics of information security.

ABSTRACT: The paper uses a game-theoretic setting to examine the interaction between strategic attackers who try to gain unauthorized access to information systems, or “targets,” and defenders of those targets. Our analysis of the attacker–defender interaction shows that well-protected targets can use signals of their superior level of protection as a deterrence tool. This is due to the fact that, all other things being equal, rational attackers motivated by potential financial gains tend to direct their effort toward less-protected targets. We analyze several scenarios differing in the scope of publicly available information about target parameters and discuss conditions under which greater defenders’ ability to signal their security characteristics may improve their welfare. Our results may assist security researchers in devising better defense strategies through the use of deterrence and provide new insight about the efficacy of specific security practices in complex information security environments.

KEY WORDS AND PHRASES: cost–benefit analysis, crime deterrence, games of complete and incomplete information, information security, information warfare, interdependent strategies, signaling.

## Motivation and Prior Research

THIS PAPER DEVELOPS A QUANTITATIVE MODEL that contributes to the understanding of information security practices and can therefore help companies manage information resources and investments in information security technology. The importance of developing such models has been widely recognized in economics $[17]$ , computer science $[26, 33]$ , and dependable computing $[5, 25]$ .

For a long time, research in information security focused on purely engineering solutions and paid little attention to changes in operational environment. Our work shows that such traditional techniques can misjudge the efficacy of a security solution by not considering the strategic nature of the problem and the interdependency between attackers' and defenders' actions. This paper focuses specifically on the behavioral impact of security practices and contributes to the growing body of work focused on applying the economic approach to security investment decisions $[2, 17, 33]$ , especially when those decisions take into account strategic interaction between different parties involved.

Because the main purpose of investing in security is to defend against attacks, acquiring a proper understanding of attackers' behavior is an important step toward better security practices. Prior research offers examples of quantitative techniques used in evaluating attackers' behavior $[4, 28]$ and of explicit models of that behavior $[20, 27, 30]$ . However, in the majority of prior theoretical work, behavior of attackers is modeled as exogenous and its guiding principles remain unclear.

Several decades of empirical cybercrime research have led to the grouping of all attackers into two broad categories: attackers seeking personal gratification—in this case, the motivation could be fame, curiosity, self-esteem, or political antagonism—and attackers looking for monetary gain $[15, 22, 24, 31]$ .¹ Such segmentation is important because the two groups exhibit different behavioral patterns, with financially motivated attackers behaving more rationally and strategically $[19, 34]$ . This difference in motivation and behavior between the two groups naturally affects the optimal choice of defense strategies.

There is evidence that financially motivated attacks are becoming increasingly common $[6, 22, 34]$ , posing a serious threat to information security. Therefore, our approach is in line with the group of papers $[18, 31, 34]$ that treat attackers as rational agents who base their actions on a cost–benefit analysis.

A comprehensive study of security incidents and practices performed in 2008 [6] confirms the validity of this approach. The study points out that cases when attackers start with picking a specific victim target and then adapt the complexity of attacks to its characteristics are rare. Instead, attackers act opportunistically, looking for targets that are poorly protected and therefore easy to breach. According to the study, 85 percent of recorded attacks were opportunistic in nature, and 80 percent of successful attacks required only low to moderate skills [6].

The same study also finds that more than 50 percent of attacks took days, weeks, or even months to develop, counting from attacker's initial entry into a corporate network to the moment when information is finally compromised. This fact indicates that many attacks involve multiple stages and elaborate decisions by attackers. We reasonably assume that attackers base those decisions on rationality and common sense, trying to maximize the returns on their effort. This is precisely the type of attack we are interested in analyzing in this paper.

We examine strategic interaction between attackers and defenders using the tool set of game theory. It is perfectly fit for the analysis of this class of problems as it not only anticipates exogenous changes in the operational environment but also recognizes the effect of one's own actions on the environment. A number of works [9, 10, 11, 12] have already demonstrated the advantages of applying the game-theoretic approach to various security issues. More specifically, several papers model strategic defender-attacker interaction and show that one defender's actions can influence the attacker's choice of targets and therefore create externalities for other defenders [8, 23, 34]. Those papers are, however, silent on the magnitude of the attacks and therefore model the decision to attack as a binary variable. In our work, we extend the set of possible scenarios by studying the endogenous allocation of attackers' effort across multiple targets. Hausken uses the same approach while studying the role of defense system configuration [19] and mechanisms that allow defenders to affect attacker decisions [18], but utilizes specific functional forms in his analysis. In contrast, we derive all of our results for general functional forms. Even more importantly, in all of the aforementioned papers, the characteristics of the targets are common knowledge whereas the focus of our paper is specifically on the role of information and signaling in the formulation of an optimal defense strategy. Our primary contribution consists in endogenizing the information flows between parties involved and demonstrating the effect of those information flows on the outcome of the game.

We start by analyzing the motivation to perform attacks in several different environments. We use our findings to examine individual firms' incentives to make a security investment while treating the characteristics of the environment as exogenous. Finally, we analyze the problem in a game-theoretic setting where the characteristics of the target population are endogenously determined by defenders' choices. In order to explore the effect of the informational structure of the game on its equilibrium outcome, we consider games of complete and incomplete information that differ in defenders' ability to signal their security characteristics.

Overall, our findings suggest that whenever attackers are willing and able to rationally choose between multiple targets, any given security measure affects the information security scene through two mechanisms. One is the commonly recognized preventive effect, or the increased ability of a target to withstand attacks of a given intensity. However, we are also interested in what we call the deterrence effect. $^{2}$ This effect, still largely neglected while devising security practices, consists in the fact that rational attackers spend less effort on better protected targets $[6, 31]$ , which further decreases the frequency of security incidents. Our paper demonstrates that the deterrence effect is no less, and can sometimes be more, pronounced than the preventive one.

Obviously, the deterrence effect is present only if attackers are able to obtain information about targets' security characteristics. This makes the defenders' ability to signal those characteristics an important part of defense strategies. The overall effect of signaling is, however, ambiguous. On one hand, better informed attackers are able to allocate their effort more efficiently, which leads to a greater welfare loss caused by attacks. On the other hand, the presence of more informed attackers increases the incentives for individual firms to invest in security, which decreases the losses from attacks. This ambiguity is resolved in a game-theoretical variant of the model.

We use our findings to discuss various approaches to investments in security technology and make recommendations regarding security practices of individual firms as well as policy recommendations. In particular, we argue that the currently adopted techniques for assessing the economic effects of security investment can severely underestimate their positive effects, therefore leading to misallocation of resources. We also derive conditions under which greater transparency in target characteristics results in a smaller social loss from attacks.

In building our model, we use some findings by Jonsson and Olovsson [20], who contributed to understanding of attackers' behavior by studying it in a laboratory environment. While their work is descriptive rather than analytical in nature, they provide empirical evidence of several distinctive phases of an attack and hypothesize the presence of “behavioral” and “preventive” effects of security measures.

## Model Assumptions

THERE ARE $N_{A}$ ATTACKERS AND $N_{T}$ corporate networks that serve as targets for attacks, where $N_{T} >> N_{A}$ . We assume all attackers are identical, and will examine the behavior of a single representative attacker. Each attacker probes targets sequentially.

Every attack consists of a learning phase, during which the attacker obtains some information about the target, and a standard attack phase. $^{3}$ The length of the learning phase, s, is assumed to be the same for every target. During the standard attack phase that follows, the attacker tries to breach the target by spending a nonnegative amount of effort, $x.^{4}$ That amount of effort is assumed to be bounded, $x \in [0, X]$ , where X is some future date at which target characteristics change substantially enough to make prior attacker efforts and all information previously acquired useless.

Attacker cost function is given by

$$
C (\alpha , \sigma , s, x) = \sigma (s + x) + \alpha C _ {A} (x),
$$

where $C(\alpha,\sigma,0,0)=0$ , $\partial C_{A}/\partial x>0$ , $\partial^{2}C_{A}/\partial x^{2}>0$ . The first term in the above expression represents the opportunity cost of effort, and parameter $\sigma>0$ reflects the value of alternatives to attacking. We assume constant opportunity cost of each unit of attacker's effort. The second component of the cost expression reflects the possibility of attack detection and punishment that would follow. $^{5}$ Parameter $\alpha$ is a characteristic of the defender's intrusion detection system, with higher values of $\alpha$ corresponding to a greater likelihood of attack detection.

The probability that an attack on target i that expends effort $x_{i}$ results in a security breach is given by cumulative probability function $\pi(\mu_{i},x_{i})$ , where $\mu_{i}$ is the amount invested in security by target i. The expected benefit from an attack therefore equals $\pi(\mu_{i},x_{i})\cdot G_{i}$ , where $G_{i}$ is the lump reward, or “loot,” the attacker receives if he or she breaches target i. For the purposes of our analysis, the loot was assumed to be nonrival and nondepletable. $^{6}$ Properties of $\pi(\cdot)$ include $\pi(\mu,0)=0$ , $\pi(\mu,X)\leq1$ , $\partial\pi(\mu,x)/\partial x>0$ , $\partial^{2}\pi(\mu,x)/\partial x^{2}\leq0$ (implying constant or diminishing returns to attacker’s effort), $\partial\pi(\mu,x)/\partial\mu<0$ , $\partial^{2}\pi(\mu,x)/\partial x\partial\mu<0$ (larger investment in security reduces the probability of a breach), $^{7}$ and $\partial^{2}\pi(\mu,x)/\partial\mu^{2}>0$ (diminishing returns to investment). All higher-order derivatives are assumed to equal zero.

Following the approach used in Gordon and Loeb [16], each defender in our model minimizes the expected cost of operating a target, which consists of the cost of security investment and the expected loss from attacks. The attacker's objective is to maximize the return on his or her effort or, in other words, accumulate the largest expected net benefit per unit of effort spent.

## Static Model

## Multiple Identical Targets

IN ORDER TO CAREFULLY EXAMINE ATTACKER'S DECISION to switch between targets, we start by analyzing the variant of the model in which the environment is static and all targets are equally attractive.

There are $N_{T}$ potential targets, all of which are identical in the loot size G, security level $\mu$ , and ability to detect attacks $\alpha$ . All of these variables are common knowledge. Attackers may stop probing one target and switch to another one at any time.

An attacker's objective function under the present setup is

$$
\Psi = \frac {\pi (\mu , x) G - C (\alpha , \sigma , x , s)}{s + x}.\tag{1}
$$

By properties of $\pi (\cdot)$ and $C(\cdot)$ , the solution to the attacker's problem exists and is unique.

Proposition 1: In the presence of multiple identical targets, the maximum amount of effort, $\hat{x}$ , an attacker optimally spends on each target is increasing in the size of the loot and the length of the learning phase ( $\partial\hat{x}/\partial G > 0$ , $\partial\hat{x}/\partial s > 0$ ) and decreasing in the likelihood of attack detection and the value of the outside opportunities ( $\partial\hat{x}/\partial\alpha < 0$ , $\partial\hat{x}/\partial\sigma < 0$ ).

The main result of the above proposition may seem counterintuitive and is therefore worth noting. Even if all targets are identical, it may be optimal for an attacker to switch to a different, randomly chosen target before the current one is breached. This is caused by the fact that the prolonged presence at one target may get too conspicuous, thus increasing the probability of detection and punishment. Also note that switching to a new target requires spending s units of effort before the attack starts bearing fruit. Therefore, a longer learning phase makes switching less attractive and induces attackers to spend more effort on any given target before they decide to give up and switch.

## Heterogeneous Targets

In the next variant of the model, all targets are identical in their loot size G, likelihood of attack detection $\alpha$ , and the length of the required learning phase s, but may differ in their security level $\mu$ . The choice of $\mu$ is discrete—each target belongs to either

H-type or L-type, reflecting high or low security level, respectively, where $\mu_{H} > \mu_{L}$ . The distribution of types is exogenous and common knowledge. The attacker finds out the target type at the end of the learning phase.

In this setting, the attacker maximizes his objective function by choosing the upper bound of effort he or she wants to spend on each target type, $\{\hat{x}_H,\hat{x}_L\}$ . The attacker's objective function now takes the form of

$$
\Psi = \frac {\eta (\pi (\mu_ {H} , x _ {H}) G - C (x _ {H} , s)) + (1 - \eta) (\pi (\mu_ {L} , x _ {L}) G - C (x _ {L} , s))}{s + \eta x _ {H} + (1 - \eta) x _ {L}},\tag{2}
$$

where $\eta$ denotes the proportion of H-type targets in the population. Conceptually, Equation (2) is similar to (1) as it still represents attacker's returns on total effort spent.

Proposition 2: Given the presence of targets with different security levels, $\mu_{H} > \mu_{L}$ , the maximum amount of effort spent by an attacker on a target is decreasing in the target security level, $\hat{x}_{H} < \hat{x}_{L}$ . The maximum amount of effort spent on any target is increasing in the length of the learning phase of the attacks and the proportion of H-type targets ( $\partial\hat{x}_{i}/\partial s > 0$ , $\partial\hat{x}_{i}/\partial\eta > 0$ ).

The first result of Proposition 2 allows us to identify two effects of a security investment—the preventive effect and the deterrence effect.

The preventive effect of a security investment is represented by the increase in the target's ability to withstand attacks of a fixed length. This effect is commonly recognized by security practitioners and frequently serves as the basis for quantitative assessment of security solutions.

The deterrence effect consists in the fact that, as stated in the above proposition, a more secure target is less appealing to attackers than a less secure target. Thus, in addition to the aforementioned preventive effect, an increase in a target's security level diverts attackers away from it, which further decreases the probability that the target in question will be breached. In other words, the overall positive effect of increased security is greater than the preventive effect alone may suggest.

There is also an additional comparative static result stating that an increase in the proportion of secure systems decreases the expected benefit an attacker gets from switching to a randomly chosen target, inducing attackers to spend more effort on any given target before switching. This in turn means attackers expose themselves to a greater risk of being detected and the maximized value of their objective function decreases.

We are now able to discuss the effect of the model parameters and the size of the security investment on the expected loss suffered by a target in a unit of time. That expected loss, denoted $\Lambda_{i}$ , is proportional to the damage caused by each breach, the probability that an attack results in a breach, and the frequency of attacks on an individual target, v: $^{8}$

$$
\Lambda_ {i} = \nu \cdot \pi (\mu_ {i}, \hat {x} _ {i}) G \quad i = H, L.\tag{3}
$$

The frequency of attacks equals the frequency of new attacker arrivals at a target. It is the same for all targets and is given by $v = N_{A}/N_{T}\tau$ , where $\tau$ is the average amount of time an attacker spends on a target. $^{9}$ Assuming an infinite time horizon, an individual defender who raises his or her security level from $\mu_{L}$ to $\mu_{H}$ receives a stream of expected benefits with the present value

$$
\Omega = \sum_ {k = 1} ^ {\infty} \frac {\Lambda_ {L} - \Lambda_ {H}}{(1 + \delta) ^ {k}} = \frac {N _ {A} \cdot G (\pi (\hat {x} _ {L} , \mu_ {L}) - \pi (\hat {x} _ {H} , \mu_ {H}))}{\delta \cdot N _ {T} \tau} > 0,\tag{4}
$$

where $\delta$ is the rate at which the defender discounts future losses.

The role of information flows can be examined by contrasting the complete information case outlined above to the one when attackers are unable to observe individual target $\mu$ values. In that case, they are only able to base their choice of effort on the average target characteristics. $^{10}$ As a result, they put the same amount of effort, x, into each target. The expressions for returns on attackers' effort, $\Psi$ , and the benefit defenders get from an upgrade, $\Omega$ , are modified accordingly:

$$
\Psi = \frac {\eta (\pi (\mu_ {H} , x) G - C (x , s)) + (1 - \eta) (\pi (\mu_ {L} , x) G - C (x , s))}{s + x}\tag{5}
$$

$$
\Omega = \frac {N _ {A} \cdot G \left(\pi (\hat {x} , \mu_ {L}) - \pi (\hat {x} , \mu_ {H})\right)}{\delta \cdot N _ {T} \tau}.\tag{6}
$$

We have the following proposition:

Proposition 3: In the presence of multiple targets identical in their loot, individual defenders' benefit from a security investment is greater when attackers are informed about targets' security levels than when attackers are uninformed. When attackers are informed, an increase in the length of the learning phase of the attack, s, decreases the benefit from security investment, $d\Omega/ds < 0$ .

The first result of the above proposition is due to the deterrence effect, which is present only when target security levels are known to attackers. The second result is attributed to the fact that a longer learning phase also increases $\hat{x}_{H}$ and $\hat{x}_{L}$ , therefore the average length of attack, $\tau$ . Thus, an increase in s decreases the frequency of attacks, and this effect always dominates the increased risk of a breach resulting from each attack. Overall, the benefit from security investment, $\Omega$ , decreases.

For brevity, we will henceforth characterize the operational environment in which obtaining target characteristics is easy as “transparent” and the one where it is difficult as “opaque.” The entire Proposition 3 can then be summarized by saying that the more transparent the environment, the more pronounced is the deterrence effect and therefore the overall positive effect of a security investment. This in turn suggests that incentives to invest in security in a transparent environment are greater than in an opaque one.

The result stated above does not imply that, from the social perspective, transparency should always be strictly preferred to opacity. First, greater transparency makes H-type targets better off and L-type targets worse off, which means that one group benefits at the expense of another. Second, when attackers are better informed, they are able to allocate their effort more efficiently, which may result in a greater overall loss to social welfare. The static nature of our analysis presented so far did not allow us to properly evaluate social welfare because it only examines the instantaneous effect of an individual security investment and treats all other factors as fixed and exogenous. This shortcoming is alleviated in the next section.

## Game-Theoretic Model

IN INFORMATION WARFARE, THE BENEFIT AN INDIVIDUAL TARGET GETS from a security investment and therefore the optimal investment decisions depend on actions expected from attackers. However, attackers' strategies in turn depend on the composition of the target population, which is determined by defenders' endogenous choices. Such complex interactions are best understood in a game-theoretic model, several variations of which are examined below.

We study a population of targets whose loot, G, is distributed continuously over the $[0,\infty)$ interval. That distribution, $\varphi(G)$ , is assumed to be common knowledge. All other assumptions from our prior analysis still hold.

The game, presented schematically in Figure 1, starts with all targets having $\mu = \mu_L$ . Each defender then decides whether to raise his or her target's security level to $\mu_H$ by investing $(\mu_H - \mu_L)$ . Next, every attacker spends $s$ units of effort to learn the characteristics of a randomly chosen target. Based on observed target characteristics and beliefs about unobserved ones, each attacker spends some effort attacking the target, and collects the loot if the attack is successful. Both parties behave rationally and expect rational actions from their counterparts. After one round of the game concludes, each attacker is matched with a different target and the game is played over and over again. Because every time there is a new attacker-target pair, the game can be analyzed as if it were played only once.

The greater the loot a defender is protecting, the more benefit he or she derives from investing in security. Therefore targets with greater loot are more likely to invest. A target is indifferent between investing and not investing when the benefit from investment, $\Omega$ , equals the cost of investment, $\Omega(G) = \mu_H - \mu_L$ . The solution to that equation, denoted $\hat{G}$ , defines the distribution of target security types. Targets with $G < \hat{G}$ do not invest and therefore maintain $\mu = \mu_L$ while targets with $G > \hat{G}$ upgrade to $\mu = \mu_H$ (see Figure 2). As a result, in our model, target's choice of the security level, $\mu$ , is positively correlated with its loot, $G$ . Attackers take the resulting distribution of target security types into account while choosing the optimal $\hat{x}$ .

We consider three variants of the game, which differ only in the set of target characteristics known to the attacker at the end of the learning phase, as discussed below in more detail.

![](/api/attachments/BVAPNAF6/fulltext/images/1dfcfabfb853e334ae1d1338b861874dc7a9ae0fbf84079319bd5075478284d9.jpg)  
Figure 1. Sequence of Game Moves

![](/api/attachments/BVAPNAF6/fulltext/images/38a944a045c20927c1fa8cfdc97ce42f2805491919ad44069a8e445794bdf37d.jpg)  
Figure 2. Distribution of Target Loots and Investment Decisions

In the version of the game we call “opaque,” neither $\mu$ nor G ever becomes known to the attacker. As a result, attackers are unable to discriminate among targets and spend the same amount of effort, $\hat{x}$ , on each target.

On the other extreme is the “complete transparency” version of the game, in which an attacker knows both $\mu$ and G once the learning phase of an attack is completed. That information affects the amount of effort, x, an attacker wants to further spend on the target. The expressions for the objective functions are modified accordingly. The attacker's objective is now to not find a single $\hat{x}$ that would apply to all targets, but a $\hat{x} (\mu ,G)$ function that maximizes return on his or her effort.

We also examine an “intermediate” version of the game in which at the end of the learning phase an attacker finds out the target’s security level but not its loot size, which can only be inferred. As a result, the attacker has to treat all targets within the same security level type the same, maximizing his or her objective function with respect to two choice variables, $x_{L}$ and $x_{H}$ . We henceforth refer to this scenario as “partial transparency.”

The following result, while being straightforward, is important because it outlines the principles guiding attacker decisions and is useful in establishing some of the later results:

Proposition 4: When an attacker is able to discriminate across targets, the amount of attacker effort spent on a target is decreasing in observed target security level and increasing in observed or inferred target loot size.

The comparison of all three variants of the game produces the following result:

Proposition 5: For any level of an attacker's effort, $x_{AV}$ , the proportion of targets choosing to perform the upgrade under partial transparency is smaller than under complete transparency.

The intuition behind this result stems from an important difference between the two scenarios. In both cases an increase in $\mu$ deters attackers but under partial transparency attackers are unable to observe individual loots directly and therefore have to base their actions on the expected loot, $\tilde{G}$ , which they infer from the target security level, $\mu_{i}$ . Due to the positive correlation between the actual loot and the security level chosen by defenders, in the partially transparent environment attackers view elevated security level as a signal of greater expected loot. Due to this “loot-signaling” effect, incentives to upgrade under partial transparency are always weaker than under complete transparency, resulting in a greater $\hat{G}$ . The relative ranking between other pairs of scenarios depends on the model parameters.

Consider the comparison between the partially transparent case and the opaque case. Raising security level under partial transparency creates two effects—deterrence and loot signaling—that are not present in the opaque case due to attackers' inability to observe $\mu$ or G. Interestingly, it is possible for the loot-signaling effect to dominate the deterrence effect. When that happens, observing $\mu = \mu_{H}$ may in fact induce greater attacker effort than $\mu = \mu_{L}, \hat{x}_{H} > \hat{x}_{L}$ . This suggests that under some combination of model parameters, some targets may be less likely to upgrade in the partial transparency case than in the opaque case, resulting in $\hat{G}^{PT}(x_{AV}) > \hat{G}^{OP}(x_{AV})$ .¹¹ This is more likely to happen when $x_{AV}$ is low and the $\tilde{G}_{H}/\tilde{G}_{L}$ ratio is large.

The ranking between the completely transparent and opaque cases is similarly ambiguous. On one hand, the deterrence effect present in the complete transparency but not the opaque case increases the benefit a target derives from the higher security level. On the other hand, the fact that in the completely transparent case attackers are better informed about target characteristics helps them allocate their effort more optimally, making them better off than in the opaque case. It is possible in principle for the latter effect to dominate for some targets, making $\Omega^{CT}(x_{AV}) < \Omega^{OP}(x_{AV})$ . Under a fairly restrictive set of conditions, that may result in $\hat{G}^{CT}(x_{AV}) > \hat{G}^{OP}(x_{AV})$ . An example of such a nontrivial ranking of the three cases is shown in panel b of Figure 3.

![](/api/attachments/BVAPNAF6/fulltext/images/2cf22398f077d01797369af7a3e1b3c9c7ff30b1a9e20a61ba29c9ee6f99d47c.jpg)

$\hat{G}$  
![](/api/attachments/BVAPNAF6/fulltext/images/ab98e73242f19d5424b749dab8d73ac6696d15e43d9d365bd9adb4812ba4e6dc.jpg)  
Figure 3. Best Response Correspondences by Attackers and Defenders  
Notes: Gray boxes denote equilibria of the three versions of the game. O, PT, and CT stand for opaque, partial transparency, and complete transparency cases, respectively.

The discussion above pertains only to defenders' responses. Perhaps the more important question deals with the properties of the equilibrium outcome of the game. In all three scenarios, the equilibrium of the game is a combination of attackers' and defenders' choices that are best responses to each other. Defenders' choices are conveniently characterized by $\hat{G}$ . No single variable can uniquely define attackers' choices, but to make the comparison across the three cases possible we use their average effort across targets, $x_{AV}$ , or the maximum attainable return on their effort, $\Psi$ . For any of the three games specified above, a greater value of the attacker objective function corresponds to a greater level of attacker effort, greater probability of a breach, and therefore greater incentive for any given target to elevate the security level. As a result, more targets make security investment $d\hat{G}^{*}/d\Psi<0$ . On the other hand, a smaller $\hat{G}$ , therefore a larger proportion of better protected targets, reduces the maximum returns on effort attackers are able to attain, $d\Psi^{*}/d\hat{G}>0$ . This leads to the following result:

Proposition 6: Each of the three games specified above has a unique equilibrium.

We are especially interested in the effect the informational characteristics of the operational environment have on the equilibrium values of two variables. One is the aforementioned returns on attackers' effort, $\Psi$ , which determines their choice between attacking and alternative occupations. The other is the aggregate social loss from attacks, $\Theta$ , which we set equal to the sum of losses suffered by all targets within a unit of time. Under the adopted specification, the social loss can be linked to the utility derived by an individual attacker by $^{12}$

$$
\Theta = \frac {N _ {A} \int_ {0} ^ {\infty} \pi (\cdot) G \varphi (G) d G}{s + \int_ {0} ^ {\infty} x (\cdot) \varphi (G) d G} = \binom{\int_ {0} ^ {\infty} C (x) \varphi (G) d G}{\Psi + \frac {0}{s + \int_ {0} ^ {\infty} x (\cdot) \varphi (G) d G}} N _ {A}.\tag{7}
$$

Proposition 7: The completely transparent variant of the game always results in a greater equilibrium proportion of targets making security investment and smaller returns on attackers' effort than the partially transparent variant, $\hat{G}^{CT} < \hat{G}^{PT}$ , $\Psi^{CT*} < \Psi^{PT*}$ .

Ranking of each of the two aforementioned cases versus the opaque case remains ambiguous. The intuition behind that ambiguity follows from the discussion accompanying Proposition 5.

Unfortunately, we are unable to establish an unambiguous ranking in terms of social loss from attacks for any of the pairs. Even in the most straightforward comparison between the complete and partial transparency cases, a large loot variance across targets may cause the losses of the targets on the upper bound of the loot distribution in the complete transparency case to outweigh the gains from better protection, as is shown in panel b of Figure 4. Our analysis also suggests that the opaque case can dominate the other two cases in terms of overall social welfare only when the equilibrium values of $\hat{G}$ for all three scenarios are low. This happens because in the other two cases, the reduced proportion of poorly protected alternatives to H-type targets reduces the extent of the deterrence effect and increases the losses of the targets at the upper end of the loot distribution.

Our last result deals with the effect of the size of the attacker and target populations:

Proposition 8: An increase in the number of attackers reduces equilibrium returns on individual attacker effort and increases the proportion of targets performing the upgrade, the average target's loss, and the overall social loss from attacks, $d\Psi/dN_A < 0$ , $d\hat{G}/dN_A < 0$ , $d\Theta/dN_A > 0$ .

An increase in the total number of targets in the population while preserving their distribution the same increases equilibrium returns on individual attacker effort, reduces the proportion of targets performing the upgrade and the average target's loss, and increases the overall social loss from attacks, $d\Psi/dN_{T} > 0$ , $d\hat{G}/dN_{T} > 0$ , $\Theta/N_{T} > d\Theta/dN_{T} > 0$ .

Note that as long as the distribution of target characteristics remains the same, changes in $N_{A}$ or $N_{T}$ affect only defenders' optimal responses to attackers' actions but not attackers' best response function. Thus, ceteris paribus, an increase in the number of attackers increases the benefit each individual target gets from investment in security, therefore inducing more targets to make such an investment. Perhaps an even more noteworthy effect that is often overlooked is associated with an increase in the number of targets. While the chances of each individual target being attacked and therefore incentives to increase security decrease as the population of targets grows, the overall social loss from attacks increases. Such misalignment between individual and social welfare is not uncommon and usually calls for extra policymakers' attention.

⑧  
![](/api/attachments/BVAPNAF6/fulltext/images/42af355292434b8dac32f9ead3e03b0d88fa7a30914ee8b35a6accc951987493.jpg)

![](/api/attachments/BVAPNAF6/fulltext/images/eca21cf08af52640641419e76c7f9dee2becfb922270d8cdab36f6a9fdcf401e.jpg)  
Figure 4. Social Loss from Attacks Under Different Game Specifications

## Numerical Example

We used numerical simulations to confirm our theoretical results. In all of our experiments we used $\pi = \mu^{-\beta}x$ and $C = \sigma(x + s) + \alpha x^{2}/2$ , where $\beta = 1.1$ , $\mu_{L} = 1$ , $\mu_{H} = 2$ , X = 1, $\sigma = 1$ , s = 1, $\alpha = 50$ , $\delta = 0.9$ , $N_{T} = 1,000$ , and $N_{A} = 225$ . We tested a variety of loot distributions, exploring the effect of distribution mean, variance, and skewness on the equilibrium outcome of the game. To separate the effects of the three distribution parameters from each other, we ran three series of experiments:

1. Changing the mean of the distribution while preserving the same variance and skewness.

2. Changing the variance of the distribution while preserving its mean and skewness.

3. Changing the skewness of the distribution while preserving the same mean and variance.

From the defenders' perspective, smaller loot variance across targets favors the transparency approach whereas larger loot variance favors opacity. This occurs because smaller variance reduces attackers' effort allocation inefficiencies in the opaque case and therefore allows attackers to cause a greater social loss. In addition, smaller variance also reduces the $\tilde{G}_H / \tilde{G}_L$ ratio under partial transparency, which weakens the negative loot-signaling effect of a security upgrade and results in a sizable increase in the equilibrium proportion of targets choosing the higher security level.

An increase in the mean of the loot distribution increases the social loss in all three scenarios but has very little effect on $\hat{G}$ or the social loss rankings between scenarios. The skewness of the loot distribution affects both parties' best response correspondences in a nontrivial way. As a result, our experiments with the shape of the loot distribution did not produce any meaningful impact on the relative welfare ranking of the three versions of the game, either.

Table 1. Results from a Numerical Simulation for Three Versions of the Game

<table><tr><td>Distribution of targets&#x27; loots</td><td>Variant of the model</td><td>Returns on attackers&#x27; effort,  $\Psi$ </td><td>Loot of target indifferent to upgrade,  $\hat{G}$ </td><td>Proportion of H-type targets,  $\eta$  (percent)</td><td>Social loss from attacks,  $\Theta$ </td></tr><tr><td rowspan="3">U~[10, 40]</td><td>CT</td><td>0.568</td><td>18.38</td><td>72.1</td><td>707</td></tr><tr><td>PT</td><td>1.202</td><td>26.42</td><td>45.3</td><td>975</td></tr><tr><td>OP</td><td>1.670</td><td>30.44</td><td>31.9</td><td>1,171</td></tr><tr><td rowspan="3">U~[10, 70]</td><td>CT</td><td>2.235</td><td>19.60</td><td>84.0</td><td>1,415</td></tr><tr><td>OP</td><td>2.360</td><td>27.95</td><td>70.1</td><td>1,455</td></tr><tr><td>PT</td><td>2.760</td><td>33.19</td><td>61.4</td><td>1,618</td></tr><tr><td rowspan="3">U~[10, 100]</td><td>OP</td><td>3.927</td><td>24.39</td><td>84.0</td><td>2,085</td></tr><tr><td>CT</td><td>4.614</td><td>21.07</td><td>87.7</td><td>2,391</td></tr><tr><td>PT</td><td>5.080</td><td>41.61</td><td>64.9</td><td>2,541</td></tr></table>

Notes: Results obtained for each distribution are ranked from the one with the smallest social loss caused by attacks to the largest. All values reported are equilibrium values.

Table 1 reports some of our numerical results. Feeling somewhat constrained by the manuscript volume, we only report results for three uniform distributions. Those results are sufficient to illustrate all the possible rankings among the three scenarios. Note that the three distributions we considered differ in both the mean and the variance. The full set of simulation results is available from the authors upon request.

Figure 3 shows the best response correspondences of attackers and defenders as well as the locations of equilibria for all three versions of the game. Note the violation of the “regular” ranking of the defender best-response correspondences in the low attacker effort, low $\hat{G}$ range in panel b, which corresponds to the case of the higher loot variance across targets.

To help the reader understand the structure of the social loss, we also include Figure 4, which shows the relationship between an individual target's loot, $G_{i}$ , and its expected loss, $\Omega$ , under each of the three scenarios. The overall social loss from attacks is represented by the area under each respective curve. One can see that for some targets, the equilibrium expected loss in the transparent case exceeds the expected loss under the other two scenarios. This happens because in the completely transparent setting, attackers know individual $G$ , which allows them to allocate their effort across targets most efficiently. As a result, within a group of targets with the same security level, those with the largest loot attract the most effort and therefore face the biggest expected losses. Panel b of Figure 4 represents the case in which this effect is strong enough to override the deterrence effect and make the complete transparency setting inferior to the opaque one in terms of overall social welfare.

## Discussion and Conclusions

THIS PAPER MAKES SEVERAL CONTRIBUTIONS. First, it demonstrates that when an attacker is able to determine the characteristics of a target he or she is probing, the attacker's optimal strategy is to put more effort into attacking systems with a low security level than into systems with a high security level. This implies that any increase in a target's security level affects the frequency of security incidents and therefore the expected loss from attacks through two separate mechanisms. One is the preventive effect that stems directly from technical characteristics of a target and decreases the probability that an attack of a given magnitude will be successful. The other, the deterrence effect makes the attacker shift his or her effort away from better-protected targets, thus further decreasing the expected frequency of security incidents and the expected loss from attacks.

The second important contribution of our paper consists in showing that in some cases, defenders can take advantage of the deterrence effect and make it a useful element of defense strategies by deliberately signaling their target characteristics to attackers. Well-protected targets benefit more from informational transparency because it allows them to separate themselves from less secure ones. This is consistent with existing theoretical research on economics of incomplete asymmetric information $[1]$ , which suggests that the ability to signal one's own type benefits “high-quality products” (well protected, or H-type systems, in the context of our model) and penalizes “low-quality products” (poorly protected, or L-type systems). Conversely, poorly protected targets prefer an opaque environment in which sending such signals is difficult.

While the deterrence effect is commonly recognized and utilized in physical security, taking the form of conspicuous armed guards, warning signs or signals, visible closed-circuit television cameras, and so forth, the information technology (IT) security field seems to be dominated by the view that transparency in security practices is bad because it helps adversaries to circumvent the defense. In this paper, we defend a more balanced view, according to which IT security management may benefit from some trade-off between transparency and secrecy. On the one hand, more informed attackers are able to allocate their effort more efficiently and therefore cause more damage. On the other hand, as we show in this paper, a more transparent environment increases individual incentives to invest in security, which tends to result in a larger equilibrium proportion of firms that choose to make security investments and a smaller aggregate social loss from attacks. Our model incorporates both effects and identifies conditions under which the latter effect dominates the former, therefore making an argument in favor of transparency. For example, our numerical simulations confirm that transparency improves social welfare when the variance in loot size across targets is relatively small.

A similar debate currently surrounds the issue of whether and to what extent competitive or security concerns can justify secrecy of information about a company's management practices. Swire has analyzed both sides of the issue [35] and offered a scenario in which wider disclosure of information can benefit security and competition [36].

Another finding worth mentioning is that the larger the proportion of well-protected targets in the population, the weaker the incentives for the remaining targets to invest in security. This effect is especially pronounced in the setting when attackers are able to determine targets' security levels but not their loot, which is why that setting rarely leads to the best outcome in terms of social welfare.

Our most important result relates to the importance of the scope of information disclosure. We find that signaling the security level, $\mu$ , without also disclosing the loot size, G, may adversely affect defenders since attackers will then perceive a higher security level as a signal of a larger loot. This weakens the deterrence effect and attackers may even put forth more, not less, effort. We show that transparency in both $\mu$ and G is better from the social welfare standpoint since it leads to a larger proportion of targets investing in security than transparency in $\mu$ only.

On the practical level, any policy discussion of transparency versus opacity requires a clear understanding of the distribution of target characteristics and the type and motivation of attackers targets are dealing with. While our paper deals mainly with rational attackers who discriminate among available targets with preference for weakly protected ones, the opaque setting of our model provides some insight on how automatic attacks operate. As Figure 3 demonstrates, optimal defensive responses in those two cases can be substantially different from each other.

Overall, our results support the notion that policies that affect individual incentives tend to be more effective than those carried out through decrees and orders. For example, end users are often blamed for the low state of the overall security because they are not installing software security updates in a timely manner. Our paper suggests that in some cases, a policy shift toward a more transparent environment may be a better way to induce timely patches than enforcing regular upgrades using administrative means. Such an effect of greater transparency matches the findings of August and Tunca, who, upon studying patching strategies, concluded that “both the value generated from software and vendor profits can be significantly improved by mechanisms that target user incentives to maintain software security” [3, p. 1703].

Our paper opens an interesting topic of utilizing deterrence as an element of an IT defense strategy by controlling the amount of information that is made known to attackers. We hope that our analysis adds value to the existing research in the field of information security and opens the way to more work in that direction. This is especially important because currently prevailing security solutions tend to ignore the deterrence effect in spite of the fact that its recognition and a constructive discussion of the specific means of utilizing it could greatly benefit the current state of information security.

We would like to point out several extensions of our model that we view as our next top priorities. First, the majority of security professionals currently agree that financially motivated attackers represent a growing portion of the attacker population $[6, 22]$ , but it is not clear whether that number is large enough to justify the shift in defense strategies from purely technical solutions toward more behavioral ones. Therefore, a better understanding of the composition of the attacker population would help defenders make more informed and therefore better defense strategy choices. The question of the actual composition of the attacker population can be answered only through meticulous empirical research.

Second, our present work treats the informational characteristics of the environment as given whereas in reality they are shaped by defenders' practices as much as, and maybe more than, government policies. Therefore, in the future, we plan to shift our focus more toward analyzing individual defenders' incentives to disclose some of their target characteristics and the effect of those decisions on the overall security landscape. Results of such analysis will be more closely tied to real-world events and may produce more accurate predictions regarding the likely outcomes of the information warfare game.

Another potential extension of our model involves analyzing the effect of the defender population dynamics on attackers' choices and therefore optimal defense strategies. The policy push toward standardization of security policies and practices, the increasing number of firms with online presence and their growing dependence on the Internet for critical business functions, and the changing nature of targets due to virtualization, cloud computing, and so on, are among the trends that deserve close attention of information security researchers.

Acknowledgments: The authors thank the Editor and three well-qualified referees for their thoughtful comments and suggestions. All the remaining errors and omissions are those of the authors.

## NOTES

1. The motivation of the latter group is nicely summarized by Gary Becker in his Nobel lecture: “Rationality implied that some individuals become criminals because of the financial and other rewards from crime compared to legal work, taking account of the likelihood of apprehension and conviction, and the severity of the punishment” [7, p. 7].

2. The presence of the two effects has been pointed out in criminology literature [21] and in the context of antiterrorism policies [14]. The deterrence effect of deploying a specific IT security instrument, an intrusion detection system, is studied in Cavusoglu et al. [11].

3. Such a pattern has been demonstrated empirically $[20]$ . The learning phase may consist of such common reconnaissance operations performed to gather information about potential targets as port scanning, operating system and application fingerprinting, etc.

4. Following Jonsson and Olovsson [20], we measure attack effort in time spent attacking, therefore ignoring possible variations in the intensity of the effort. A similar approach is used in Reinganum [32] to model research activity. A more complex setup is saved for future work.

5. As an attack progresses, it leaves behind a stream of evidence detectable by the defender. Intrusion detection literature [29, 37, 38, 39] maintains that the more suspicious events are observed, the more likely is the next event to lead to attack detection and therefore a punishment. Since the learning phase consists of reconnaissance activity only, we assume that it does not increase the probability of detection. Therefore, an attacker's only cost during that phase is the opportunity cost of effort.

6. Our focus is specifically on human-driven, financially motivated attacks. According to the incident statistics $[6]$ and anecdotal evidence from the IT industry, cases when a target is subject to several such attacks simultaneously are quite rare. Therefore, we were comfortable making this assumption.

7. Because investment in security decreases the probability of a breach, we will also refer to $\mu$ as “security level.”

8. Such a specification calls for two clarifying comments. First, in the context of examples motivating this research, simultaneous attacks on the same target by two or more attackers are rare. Therefore, it is safe to assume that every breach results in the same loss, which justified the use of a linear specification. This simplifies the analysis but does not affect its main results. Second, for notational brevity, we set the defender's loss in the case of a breach equal to the attacker's gain, $G$ .

9. In the body of the paper, we provide expressions only for variables that are most important for the logic of the narrative. All other relevant formulas are provided in Appendix Table A1.

10. A more sophisticated approach to the uninformed attackers case is when attackers infer target characteristics in the Bayesian manner. Such a setup is examined in Cremonini and Nizovtsev [13] and produces results similar to those presented below.

11. From here on, superscripts assigned to some of the variables denote which of the three game variants (opaque, partial transparency, or complete transparency) is being discussed.

12. Alternative specifications of the social loss function are, of course, possible, some of which may also include the cost of the investment. We chose to focus on direct losses from attacks since numerous government documents indicate that those losses constitute the main concern of information security policymakers. In addition, greater social losses and therefore greater returns on effort achieved by attackers are likely to attract more individuals to performing attacks, increasing $N_{A}$ and the social loss.

## REFERENCES

1. Akerlof, G.A. The market for “lemons”: Quality uncertainty and market mechanism. Quarterly Journal of Economics, 84, 3 (1970), 488–500.

2. Anderson, R.J., and Moore, T. Information security economics—and beyond. In A. Menezes (ed.), Advances in Cryptology—CRYPTO 2007. Lecture Notes in Computer Science 4622. Berlin and Heidelberg: Springer, 2007, pp. 68–91.

3. August, T., and Tunca, T.I. Network software security and user incentives. Management Science, 52, 11 (2006), 1703–1720.

4. Avizienis, A.; Laprie, J.; and Randell, B. Fundamental concepts of dependability. Technical Report no. 01145, Laboratoire d'Analyse et d'Architecture des Systemes, Centre National de la Recherche Scientifique, Toulouse, France, 2001.

5. Avizienis, A.; Laprie, J.; Randell, B.; and Landwehr, C. Basic concepts and taxonomy of dependable and secure computing. IEEE Transactions on Dependable and Secure Computing, 1, 1 (2004), 11–33.

6. Baker, W.H.; Hylender, C.D.; and Valentine, J.A. 2008 data breach investigation report. Verizon Business Risk Team, New York, 2008 (available at www.verizonbusiness.com/resources/security/databreachreport.pdf).

7. Becker, G.S. The economic way of looking at behavior. Journal of Political Economy, 101, 3 (1993), 385–409.

8. Bier, V.; Oliveros, S.; and Samuelson, L. Choosing what to protect: Strategic defensive allocation against an unknown attacker. Journal of Public Economic Theory, 9, 4 (2007), 563–587.

9. Cavusoglu, H., and Raghunathan, S. Configuration of detection software: A comparison of decision and game theory approaches. Decision Analysis, 1, 3 (2004), 131–148.

10. Cavusoglu, H.; Mishra, B.; and Raghunathan, S. A model for evaluating IT security investments. Communications of the ACM, 47, 7 (2004), 87–92.

11. Cavusoglu, H.; Mishra, B.; and Raghunathan, S. The value of intrusion detection systems in information technology security architecture. Information Systems Research, 16, 1 (2005), 28–46.

12. Cavusoglu, H.; Raghunathan, S.; and Yue, W.T. Decision theoretic and game-theoretic approaches to IT security investment. Journal of Management Information Systems, 25, 2 (Fall 2008), 281–304.

13. Cremonini, M., and Nizovtsev, D. Understanding and influencing attackers' decisions: Implications for security investment strategies. Paper presented at the Fifth Workshop on the Economics of Information Security (WEIS 2006), Cambridge, UK, June 26–28, 2006.

14. Enders, W., and Sandler, T. What do we know about the substitution effect in transnational terrorism? In A. Silke and G. Ilardi (eds.), Researching Terrorism Trends, Achievements, Failures. Ilford, UK: Frank Cass, 2004, pp. 119–137.

15. Franklin, J.; Paxson, V.; Perrig, A.; and Savage, S. An inquiry into the nature and causes of the wealth of Internet miscreants. In S. De Capitani, P. Syverson, and D. Evans (eds.), Proceedings of the Fourteenth ACM Conference on Computer and Communications Security. New York; ACM Press, 2007, pp. 375–388.

16. Gordon, L.A., and Loeb, M.P. The economics of information security investment. ACM Transactions on Information and System Security, 5, 4 (2002), 438–457.

17. Gordon, L.A., and Loeb, M. Managing Cybersecurity Resources: A Cost-Benefit Analysis. New York: McGraw-Hill, 2005.

18. Hausken, K. Income, interdependence, and substitution effects affecting incentives for security investment. Journal of Accounting and Public Policy, 25, 6 (2006), 629–665.

19. Hausken, K. Strategic defense and attack for series and parallel reliability systems. European Journal of Operational Research, 186, 2 (2008), 856–881.

20. Jonsson, E., and Olovsson, T. A quantitative model of the security intrusion process based on attacker behavior. IEEE Transactions on Software Engineering, 23, 4 (1997), 235–245.

21. Kennedy, D.M. Deterrence and Crime Prevention: Reconsidering the Prospect of Sanction. New York: Routledge, 2008.

22. Kiefer Peretti, K. Data breaches: What the underground world of “carding” reveals. Computer Crime and Intellectual Property Section, U.S. Department of Justice, Washington, DC, 2008 (available at www.usdoj.gov/criminal/cybercrime/DataBreachesArticle.pdf).

23. Kuhnreuther, H., and Heal, G. Interdependent security. Journal of Risk and Uncertainty, 26, 2–3 (2003), 231–249.

24. Leeson, P.T., and Coyne, C.J. The economics of computer hacking. Journal of Law, Economics and Policy, 1, 2 (2006), 511–532.

25. Littlewood, B.; Brocklehurst, S.; Fenton, N.; Mellor, P.; Page, S.; Wright, D.; Dobson, J.; McDermid, J.; and Gollmann, D. Towards operational measures of computer security. Journal of Computer Security, 2, 3 (1993), 211–229.

26. Liu, P.; Zang, W.; and Yu, M. Incentive-based modeling and inference of attacker intent, objectives, and strategies. ACM Transactions on Information and System Security, 8, 1 (2005), 78–118.

27. McDermott, J. Attack-potential-based survivability modeling for high-consequence systems. In J.L. Cole and S.D. Wolthusen (eds.), Proceedings of the Third IEEE International Information Assurance Workshop. Los Alamitos, CA: IEEE Computer Society, 2005, pp. 119–130.

28. Nicol, D.M.; Sanders, W.H.; and Trivedi, K.S. Model-based evaluation: From dependability to security. IEEE Transactions on Dependable and Secure Computing, 1, 1 (2004), 48–65.

29. Ning, P.; Cui, Y.; Reeves, D.S.; and Xu, D. Techniques and tools for analyzing intrusion alerts. ACM Transactions on Information and System Security, 7, 2 (2004), 274–318.

30. Ortalo, R.; Deswarte, Y.; and Kaâniche, M. Experiments with quantitative evaluation tools for monitoring operational security. IEEE Transactions on Software Engineering, 25, 5 (1999), 633–650.

31. Png, I.P.L.; Wang, C.Y.; and Wang, Q.H. The deterrent and displacement effects of information security enforcement: International evidence. Journal of Management Information Systems, 25, 2 (Fall 2008), 125–144.

32. Reinganum, J. A dynamic game of R&D: Patent protection and competitive behavior. Econometrica, 50, 3 (1982), 671–688.

33. Schechter, S.E. Computer security strength and risk: A quantitative approach. Ph.D. dissertation, Division of Engineering and Applied Sciences, Harvard University, Cambridge, 2004.

34. Schechter, S.E., and Smith, M.D. How much security is enough to stop a thief? The economics of outsider theft via computer systems and networks. In R.N. Wright (ed.), Financial Cryptography Conference. Lecture Notes in Computer Science 2742. Berlin: Springer, 2003, pp. 122–137.

35. Swire, P.P. A model for when disclosure helps security: What is different about computer and network security? Journal on Telecommunications and High Technology Law, 3, 1 (2004), 163–208.

36. Swire, P.P. A theory of disclosure for security and competitive reasons: Open source, proprietary software, and government agencies. Houston Law Review, 42, 5 (2006), 1333–1380.

37. Valeur, F.; Vigna, G.; Kruegel, C.; and Kemmerer, R.A. A comprehensive approach to intrusion detection alert correlation. IEEE Transactions on Dependable and Secure Computing, 1, 3 (2004), 146–169.

38. Wespi, A.; Debar, H.; Dacier, M.; and Nassehi, M. Fixed- vs. variable-length patterns for detecting suspicious process behavior. Journal of Computer Security, 8, 2–3 (2000), 1–15.

39. Zhou, J.; Heckman, M.; Reynolds, B.; Carlson, A.; and Bishop, M. Modeling network intrusion detection alerts for correlation. ACM Transactions on Information and System Security, 10, 1 (2007), 1–31.

Appendix

Proof of Proposition 1

$$
\Psi = \frac {\pi (\cdot) G - C (\cdot)}{s + x}
$$

First-order condition:

$$
\Phi = \frac {d \Psi}{d x} = \frac {\left(\frac {d \pi}{d x} G - \frac {d C}{d x}\right) (s + x) - \pi (\cdot) G + C (\cdot)}{(s + x) ^ {2}} = 0,
$$

which implies that, at the maximizer, the marginal net benefit of effort equals the average net benefit,

$$
\frac {d \pi (\mu , x)}{d x} G - \frac {d C (\sigma , \alpha , x)}{d x} = \frac {\pi (\mu , x) G - C (\sigma , \alpha , x)}{s + x}
$$

Second-order condition:

$$
\frac {d \Phi}{d x} = \frac {\left(\frac {d ^ {2} \pi}{d x ^ {2}} G - \frac {d ^ {2} C}{d x ^ {2}}\right) (s + x) + \frac {d \pi}{d x} G - \frac {d C}{d x} - \frac {d \pi}{d x} G + \frac {d C}{d x}}{(s + x) ^ {2}} = \frac {\frac {d ^ {2} \pi}{d x ^ {2}} G - \frac {d ^ {2} C}{d x ^ {2}}}{s + x} <   0
$$

$$
\frac {\partial \Phi}{\partial G} = \frac {(s + x) \frac {\partial \pi}{\partial x} - \pi}{(s + x) ^ {2}} = \frac {(s + x) \frac {\partial C}{\partial x} - C}{(s + x) ^ {2}}
$$

by first-order condition and is positive by properties of C. Therefore,

$$
\frac {d \hat {x}}{d G} = \left. \begin{array}{c} - \frac {\partial \Phi}{\partial G} \\ \hline \frac {\partial \Phi}{\partial x} \end{array} \right/ > 0.
$$

$$
\frac {\partial \Phi}{\partial s} = \frac {\frac {\partial \pi}{\partial x} G - \frac {\partial^ {2} C}{\partial x \partial s} (s + x)}{(s + x) ^ {2}} > 0
$$

because

$$
\frac {\partial^ {2} C}{\partial x \partial s} = 0.
$$

Therefore,

$$
\frac {d \hat {x}}{d s} = \left. - \frac {\partial \Phi}{\partial s} \right/ _ {\frac {\partial \Phi}{\partial x}} > 0.
$$

$$
\frac {\partial \Phi}{\partial \alpha} = \frac {- (s + x) \frac {\partial^ {2} C}{\partial x \partial \alpha} + \frac {\partial C}{\partial \alpha}}{(s + x) ^ {2}} <   0
$$

by properties of $C_A$ . Therefore,

$$
\frac {d \hat {x}}{d \alpha} = \left. \begin{array}{c} - \frac {\partial \Phi}{\partial \alpha} \\ \hline \frac {\partial \Phi}{\partial x} \end{array} \right/ <   0.
$$

Q.E.D.

Proof of Proposition 2

Proof of the $\hat{x}_H < \hat{x}_L$ Result

The attacker maximizes

$$
\Psi = \frac {\eta (\pi_ {H} G - C _ {H}) + (1 - \eta) (\pi_ {L} G - C _ {L})}{s + \eta x _ {H} + (1 - \eta) x _ {L}}\tag{A1}
$$

with respect to $x_{L}$ , $x_{H}$ , where $\pi_{i} = \pi(\mu_{i}, x_{i})$ , $C_{i} = C(\alpha_{i}, \sigma, x_{i}, s)$ , i = H, L.

No explicit solution for Equation (A1) exists, therefore we are using differentiation of an implicit function. The two first-order conditions are

$$
\Phi_ {H} = \frac {\partial \Psi}{\partial x _ {H}} = \frac {\eta}{s + \eta x _ {H} + (1 - \eta) x _ {L}} \left(\frac {\partial \pi_ {H}}{\partial x _ {H}} G - \frac {\partial C _ {H}}{\partial x _ {H}} - \psi\right) = 0\tag{A1a}
$$

and

$$
\Phi_ {L} = \frac {\partial \Psi}{\partial x _ {L}} = \frac {1 - \eta}{s + \eta x _ {H} + (1 - \eta) x _ {L}} \left(\frac {\partial \pi_ {L}}{\partial x _ {L}} G - \frac {\partial C _ {L}}{\partial x _ {L}} - \psi\right) = 0.\tag{A1b}
$$

Suppose $\hat{x}_{H} \geq \hat{x}_{L}$ ; then from Equations (A1a) and (A1b) and properties of C,

$$
\frac {d \pi_ {H} (\hat {x} _ {H})}{d x _ {H}} \geq \frac {\mathrm{d} \pi_ {L} (\hat {x} _ {L})}{d x _ {L}}.
$$

However, $\hat{x}_H \geq \hat{x}_L$ also implies

$$
\frac {d \pi_ {H} (\hat {x} _ {H})}{d x _ {H}} \leq \frac {\mathrm{d} \pi_ {H} (\hat {x} _ {L})}{d x _ {L}},
$$

and

$$
\frac {\partial^ {2} \pi (\mu_ {i} , x _ {i})}{\partial x _ {i} \partial \mu_ {i}} <   0 (i = H, L)
$$

and $\mu_{L}<\mu_{H}$ require

$$
\frac {d \pi_ {H} (\hat {x} _ {L})}{d x _ {H}} <   \frac {\mathrm{d} \pi_ {L} (\hat {x} _ {L})}{d x _ {L}},
$$

resulting in a contradiction. Thus, our initial assumption was incorrect, and $\hat{x}_{H} < \hat{x}_{L}$ . Q.E.D.

## Comparative Static Results

General Forms. For a multivariate implicit function, the effect of model parameters on optimal choices in the vicinity of the maximizer is given by

$$
\left[ \frac {\partial \hat {x} _ {i}}{\partial p _ {j}} \right] = - \left[ \frac {\partial^ {2} \Psi}{\partial x _ {- i} \partial x _ {i}} \right] ^ {- 1} \left[ \frac {\partial^ {2} \Psi}{\partial p _ {j} \partial x _ {i}} \right],
$$

where $i \in \{H, L\}$ , $x_{-i} \in \{x_{L}, x_{H}\}$ , $x_{-i} \neq x_{i}$ , and $p_{j}$ is the jth element of the vector of parameters, p. At the maximizer

$$
\frac {\partial^ {2} \Psi}{\partial x _ {H} \partial x _ {L}} = \frac {\partial^ {2} \Psi}{\partial x _ {L} \partial x _ {H}} = 0,
$$

making

$$
D e t \left[ \frac {\partial^ {2} \Psi}{\partial x _ {- i} \partial x _ {i}} \right] = \frac {\partial^ {2} \Psi}{\partial x _ {i} ^ {2}} \cdot \frac {\partial^ {2} \Psi}{\partial x _ {- i} ^ {2}}.
$$

Therefore,

$$
\begin{array}{c} \frac {\partial \hat {x} _ {i}}{\partial p} = \frac {- \left(\frac {\partial^ {2} \Psi}{\partial x _ {- i} ^ {2}} \cdot \frac {\partial^ {2} \Psi}{\partial x _ {i} \partial p} - \frac {\partial^ {2} \Psi}{\partial x _ {i} \partial x _ {- i}} \cdot \frac {\partial^ {2} \Psi}{\partial x _ {- i} \partial p}\right)}{D e t \left[ \frac {\partial^ {2} \Psi}{\partial x _ {- i} \partial x _ {i}} \right]} = - \left(\frac {\partial^ {2} \Psi}{\partial x _ {i} ^ {2}} \cdot \frac {\partial^ {2} \Psi}{\partial x _ {- i} ^ {2}}\right) ^ {- 1} \left(\frac {\partial^ {2} \Psi}{\partial x _ {- i} ^ {2}} \cdot \frac {\partial^ {2} \Psi}{\partial x _ {i} \partial p}\right) \\ = - \left(\frac {\partial^ {2} \Psi}{\partial x _ {i} ^ {2}}\right) ^ {- 1} \frac {\partial^ {2} \Psi}{\partial x _ {i} \partial p}, i = H, L. \end{array}
$$

Second-Order Conditions

$$
\frac {\partial^ {2} \Psi}{\partial x _ {H} ^ {2}} = \frac {\eta \left(\frac {\partial^ {2} \pi_ {H}}{\partial x _ {H} ^ {2}} G - \frac {\partial^ {2} C _ {H}}{\partial x _ {H} ^ {2}}\right)}{s + \eta x _ {H} + (1 - \eta) x _ {L}} <   0
$$

$$
\frac {\partial^ {2} \Psi}{\partial x _ {L} ^ {2}} = \frac {(1 - \eta) \left(\frac {\partial^ {2} \pi_ {L}}{\partial x _ {L} ^ {2}} G - \frac {\partial^ {2} C _ {L}}{\partial x _ {L} ^ {2}}\right)}{s + \eta x _ {H} + (1 - \eta) x _ {L}} <   0.
$$

Effect of $s$

$$
\begin{array}{c} \frac {\partial \Psi}{\partial s} = \frac {\left(- \eta \frac {\partial C _ {H}}{\partial s} - (1 - \eta) \frac {\partial C _ {L}}{\partial s}\right) (s + \eta x _ {H} + (1 - \eta) x _ {L}) - \Psi (s + \eta x _ {H} + (1 - \eta) x _ {L})}{(s + \eta x _ {H} + (1 - \eta) x _ {L}) ^ {2}} \\ = \frac {- \partial C / \partial s - \Psi}{s + \eta x _ {H} + (1 - \eta) x _ {L}} <   0, \end{array}
$$

supporting the intuitive notion that a longer learning phase of an attack decreases attacker's utility.

$$
\frac {\partial^ {2} \Psi}{\partial x _ {H} \partial s} = \frac {\partial \Phi_ {H}}{\partial s} = \frac {\eta \left(\frac {\partial^ {2} \pi_ {H}}{\partial x _ {H} \partial s} G - \frac {\partial^ {2} C _ {H}}{\partial x _ {H} \partial s} - \frac {\partial \Psi}{\partial s}\right)}{s + \eta x _ {H} + (1 - \eta) x _ {L}}.
$$

Recognizing

$$
\frac {\partial^ {2} \pi_ {H}}{\partial x _ {H} \partial s} = 0,
$$

$$
\frac {\partial^ {2} C _ {H}}{\partial x _ {H} \partial s} = 0
$$

yields

$$
\frac {\partial^ {2} \Psi}{\partial x _ {H} \partial s} = \frac {- \eta \frac {\partial \Psi}{\partial s}}{s + \eta x _ {H} + (1 - \eta) x _ {L}} > 0,
$$

and

$$
\frac {d \hat {x} _ {H}}{d s} = \left. \begin{array}{c} - \frac {\partial^ {2} \Psi}{\partial x _ {H} \partial s} \\ \hline \frac {\partial^ {2} \Psi}{\partial x _ {H} ^ {2}} \end{array} \right/ > 0.
$$

The proof of $d\hat{x}_L / ds > 0$ follows a similar vein.

Effect of η

$$
\frac {\partial \Psi}{\partial \eta} = \frac {\left(\pi_ {H} G - C _ {H}\right) \left(s + x _ {L}\right) - \left(\pi_ {L} G - C _ {L}\right) \left(s + x _ {H}\right)}{\left(s + \eta x _ {H} + (1 - \eta) x _ {L}\right) ^ {2}} <   0
$$

by properties of $\pi$ and $C$ .

Given (A1a) and (A1b), at the respective maximizers

$$
\frac {\partial \Phi_ {H}}{\partial \eta} = \frac {\partial^ {2} \Psi}{\partial x _ {H} \partial \eta} = \frac {- \eta \frac {\partial \Psi}{\partial \eta}}{s + \eta x _ {H} + (1 - \eta) x _ {L}} > 0
$$

$$
\frac {\partial \Phi_ {L}}{\partial \eta} = \frac {\partial^ {2} \Psi}{\partial x _ {L} \partial \eta} = \frac {- (1 - \eta) \frac {\partial \Psi}{\partial \eta}}{s + \eta x _ {H} + (1 - \eta) x _ {L}} > 0
$$

and

$$
\frac {d \hat {x} _ {i}}{d \eta} = \frac {\frac {- \partial \Phi_ {i}}{\partial \eta}}{\frac {\partial \Phi_ {i}}{\partial x _ {i}}} = \frac {\partial \Psi / \partial \eta}{\frac {\partial^ {2} \pi_ {i}}{\partial x _ {i} ^ {2}} G - \frac {\partial^ {2} C _ {i}}{\partial x _ {i} ^ {2}}} > 0, i = H, L.
$$

Q.E.D.

## Proof of Proposition 3

Informed Versus Uninformed Attacker Case

By Proposition 2, in the informed attacker case $\hat{x}_H < \hat{x}_L$ .

The uninformed attacker case can be thought of as optimizing Equation (5) subject to an additional equality constraint, $x_{H} = x_{L} = x_{un}$ , which implies $\Psi_{un}^{*} < \Psi_{inf}^{*}$ and $\hat{x}_{H} > \hat{x}_{un} > \hat{x}_{L}$ , where $\hat{x}_{H}$ and $\hat{x}_{L}$ are the solutions to the optimization problem in the “informed” case and $\hat{x}_{un}$ is the solution for the same set of parameters but an uninformed attacker.

The benefit from investment for the informed and uninformed attacker cases is, respectively,

$$
\Omega_ {\mathrm{inf}} = \frac {\delta \cdot N _ {A} \cdot G}{N _ {T} (s + \eta \tau_ {H} + (1 - \eta) \tau_ {L})} \left(\pi_ {L} (\hat {x} _ {L}) - \pi_ {H} (\hat {x} _ {H})\right)
$$

and

$$
\Omega_ {\mathrm{un}} = \frac {\delta \cdot N _ {A} \cdot G}{N _ {T} (s + \eta \tau_ {H} + (1 - \eta) \tau_ {L})} \left(\pi_ {L} (\hat {x} _ {u n}) - \pi_ {H} (\hat {x} _ {u n})\right).
$$

$\hat{x}_H < \hat{x}_{un} < \hat{x}_L$ and $\partial \pi / \partial x > 0$ imply $\pi_L(\hat{x}_L) > \pi_L(\hat{x}_{un}) > \pi_H(\hat{x}_{un}) > \pi_H(\hat{x}_H)$ . Therefore, $\Omega_{\mathrm{inf}} > \Omega_{un}$ .

Effect of $s$

Differentiation by the chain rule yields

$$
\frac {d \Omega}{d s} = \frac {\partial \Omega}{\partial s} + \frac {\partial \Omega}{\partial \hat {x} _ {H}} \frac {d \hat {x} _ {H}}{d s} + \frac {\partial \Omega}{\partial \hat {x} _ {L}} \frac {d \hat {x} _ {L}}{d s}.\tag{A2}
$$

$$
\frac {\partial \Omega}{\partial s} = \frac {- N _ {A} \cdot G \cdot \left(\pi_ {L} (\hat {x} _ {L}) - \pi_ {H} (\hat {x} _ {H})\right)}{N _ {T} (s + \eta \tau_ {H} + (1 - \eta) \tau_ {L}) ^ {2}} = \frac {- \Omega}{Z} <   0,
$$

where $Z = s + \eta \tau_{H} + (1 - \eta)\tau_{L} > 0,$

$$
\frac {\partial \Omega}{\partial x _ {H}} = \frac {- N _ {A} \cdot G \cdot \frac {\partial \pi_ {H} (\hat {x} _ {H})}{\partial x _ {H}}}{N _ {T} Z} - \frac {\eta \Omega}{Z} <   0
$$

$$
\begin{array}{c} \frac {\partial \Omega}{\partial x _ {L}} = \frac {N _ {A} \cdot G \cdot \left(\frac {\partial \pi_ {L} (\hat {x} _ {L})}{\partial x _ {L}} Z - (\pi_ {L} (\hat {x} _ {L}) - \pi_ {H} (\hat {x} _ {H})) (1 - \eta)\right)}{N _ {T} (s + \eta \tau_ {H} + (1 - \eta) \tau_ {L}) ^ {2}} \\ = \frac {N _ {A} \cdot G \cdot \frac {\partial \pi_ {L} (\hat {x} _ {L})}{\partial x _ {L}}}{N _ {T} Z} - \frac {(1 - \eta) \Omega}{Z}. \end{array}
$$

By Proposition 2,

$$
\frac {d \hat {x} _ {H}}{d s} = \frac {- \left(\partial C / \partial s + \Psi\right)}{\left(\frac {\partial^ {2} \pi_ {H}}{\partial x _ {H} ^ {2}} G - \frac {\partial^ {2} C _ {H}}{\partial x _ {H} ^ {2}}\right) Z} > 0
$$

$$
\frac {d \hat {x} _ {L}}{d s} = \frac {- \left(\partial C / \partial s + \Psi\right)}{\left(\frac {\partial^ {2} \pi_ {L}}{\partial x _ {L} ^ {2}} G - \frac {\partial^ {2} C _ {L}}{\partial x _ {L} ^ {2}}\right) Z} > 0.
$$

Because

$$
\frac {\partial^ {3} \pi}{\partial x ^ {3}} = \frac {\partial^ {3} C}{\partial x ^ {3}} = 0
$$

by assumption, we have

$$
\frac {\partial^ {2} \pi_ {H}}{\partial x _ {H} ^ {2}} G - \frac {\partial^ {2} C _ {H}}{\partial x _ {H} ^ {2}} \geq \frac {\partial^ {2} \pi_ {L}}{\partial x _ {L} ^ {2}} G - \frac {\partial^ {2} C _ {L}}{\partial x _ {L} ^ {2}}
$$

and

$$
\frac {d \hat {x} _ {H}}{d s} \geq \frac {d \hat {x} _ {L}}{d s}.
$$

We can rewrite Equation (A2) as

$$
\begin{array}{c} \frac {d \Omega}{d s} = \frac {\partial \Omega}{\partial s} + \frac {\partial \Omega}{\partial \hat {x} _ {H}} \frac {\partial \hat {x} _ {H}}{\partial s} + \frac {\partial \Omega}{\partial \hat {x} _ {L}} \frac {\partial \hat {x} _ {L}}{\partial s} \leq \frac {\partial \Omega}{\partial s} + \left(\frac {\partial \Omega}{\partial \hat {x} _ {H}} + \frac {\partial \Omega}{\partial \hat {x} _ {L}}\right) \frac {\partial \hat {x} _ {L}}{\partial s} \\ = \frac {- \Omega}{Z} + \left(\frac {N _ {A} \cdot G \cdot \left(\frac {\partial \pi_ {L} (\hat {x} _ {L})}{\partial x _ {L}} - \frac {\partial \pi_ {H} (\hat {x} _ {H})}{\partial x _ {H}}\right)}{N _ {T} Z} - \frac {\Omega}{Z}\right) \frac {\partial \hat {x} _ {L}}{\partial s}. \end{array}
$$

By properties of $\pi$ ,

$$
\frac {\partial \pi_ {L} (\hat {x} _ {L})}{\partial x _ {L}} - \frac {\partial \pi_ {H} (\hat {x} _ {H})}{\partial x _ {H}} <   \frac {\pi_ {L} - \pi_ {H}}{Z},
$$

therefore, $d\Omega/ds < 0$ . Q.E.D.

## Proof of Proposition 4

By one of the maximizer properties, $\Psi$ is maximized when the marginal net benefit from the last unit of effort spent on each target equals the average net benefit from all targets, or in our case the objective function itself:

$$
\frac {\partial \pi (\hat {x})}{\partial x} G - \frac {\partial C (\hat {x})}{\partial x} = \Psi (\hat {x}).
$$

Because $C(\cdot)$ is independent of G and $\mu$ , the difference in the optimal effort across targets is attributed solely to the first term in the above expression. When a rational attacker faces a greater loot, he or she will stop at a smaller value of $\partial\pi/\partial x$ , which, given

$$
\frac {\partial^ {2} \pi (\mu , x)}{\partial x ^ {2}} \leq 0,
$$

corresponds to a greater $\hat{x}$ . By another property of $\pi$ ,

$$
\frac {\partial^ {2} \pi (\mu , x)}{\partial x \partial \mu} <   0,
$$

and a similar logic, a greater $\mu$ induces a smaller attacker effort. Therefore, optimal $\hat{x}$ is decreasing in $\mu$ and increasing in G. Q.E.D.

## Proof of Proposition 5

In all three versions of the game, $\hat{G}$ is the value of G that solves

$$
\Omega (G) = \frac {N _ {A} \cdot G \cdot (\pi (\hat {x} _ {L} (\mu_ {L} , \tilde {G} _ {L}) , \mu_ {L}) - \pi (\hat {x} _ {H} (\mu_ {H} , \tilde {G} _ {H}) , \mu_ {H}))}{\delta \cdot N _ {T} \tau} = \mu_ {H} - \mu_ {L},\tag{A3}
$$

where $\tilde{G}$ denotes attacker's beliefs about the loot associated with a target of a known type $i$ , $i = H, L$ . Under complete transparency, $\tilde{G}_L = \tilde{G}_H = G$ ; under partial transparency,

$$
\tilde {G} _ {L} = G _ {L} ^ {A V} = \frac {\int_ {0} ^ {\hat {G}} G \varphi (G) d G}{\int_ {0} ^ {\hat {G}} \varphi (G) d G}
$$

$$
\tilde {G} _ {H} = G _ {H} ^ {A V} = \frac {\int_ {\hat {G}} ^ {\infty} G \varphi (G) d G}{\int_ {\hat {G}} ^ {\infty} \varphi (G) d G}.
$$

Consider the following approximation:

$$
\begin{array}{c} \frac {\pi \left(\hat {x} _ {L} \left(\mu_ {L} , \tilde {G} _ {L}\right) , \mu_ {L}\right) - \pi \left(\hat {x} _ {H} \left(\mu_ {H} , \tilde {G} _ {H}\right) , \mu_ {H}\right)}{\mu_ {H} - \mu_ {L}} \approx - \frac {d \pi}{d \mu} \\ = - \left(\frac {\partial \pi}{\partial \mu} + \frac {\partial \pi}{\partial x} \frac {\partial x}{\partial \mu} + \frac {\partial \pi}{\partial x} \frac {\partial x}{\partial \tilde {G}} \frac {\partial \tilde {G}}{\partial \mu}\right). \end{array}
$$

By properties of $\pi$ ,

$$
\frac {\partial \pi}{\partial \mu} <   0
$$

and

$$
\frac {\partial \pi}{\partial x} > 0.
$$

For both cases considered in this proposition, $\mu$ is observed by attackers, therefore,

$$
\frac {\partial x}{\partial \mu} <   0
$$

and

$$
\frac {\partial x}{\partial \tilde {G}} > 0
$$

by Proposition 4.

Under complete transparency $\tilde{G}=G$ , therefore,

$$
\frac {\partial \tilde {G}}{\partial \mu} = 0,
$$

whereas in the partial transparency case,

$$
\frac {\partial \tilde {G}}{\partial \mu} > 0
$$

due to the positive correlation between $\mu$ and G.

Therefore, the $\pi(\hat{x}_{L}(\mu_{L},\tilde{G}_{L}),\mu_{L})-\pi(\hat{x}_{H}(\mu_{H},\tilde{G}_{H}),\mu_{H})$ term in the complete transparency case is greater than in the partial transparency case.

Furthermore, due to the fact that attackers are best informed under complete transparency, any $x_{AV}$ results in $\tau^{CT} < \tau^{PT}$ . Therefore, $\Omega^{CT}(G) > \Omega^{PT}(G)$ for all G. Given $\partial\Omega/\partial G > 0$ , the value of $\hat{G}$ that solves Equation (A3) is smaller in the complete transparency case, $\hat{G}^{CT} < \hat{G}^{PT}$ . Q.E.D.

## Proof of Proposition 6

We provide a proof only for the complete transparency version of the game as the most complex one; proofs for the other two cases are similar. We denote the maximum attainable return on attacker effort $\Psi^{*}$ . The slope of attacker's best response correspondence in the $(\Psi, \hat{G})$ space is

$$
\frac {d \Psi^ {*}}{d \hat {G}} = \frac {\partial \Psi^ {*}}{\partial \hat {G}} + \sum \frac {\partial \Psi^ {*}}{\partial \hat {x _ {i}}} \frac {\partial \hat {x _ {i}}}{\partial \hat {G}} = \frac {\partial \Psi^ {*}}{\partial \hat {G}}
$$

because by the envelope theorem

$$
\frac {\partial \Psi^ {*}}{\partial \hat {x} _ {i}} = 0
$$

for all i.

We simplify the notation by introducing $B_{i} = \pi(\mu_{i}, x(\mu_{i}, G))G - C(\alpha, x(\mu_{i}, G), s)$ .

Differentiation of the expression for the returns on attacker effort (see Table A1) yields

Table A1. Summary of Variables Used in the Analysis

<table><tr><td>Variant of the game</td><td>Opaque</td><td>Partial transparency</td><td>Complete transparency</td></tr><tr><td>Target security level, μ</td><td>Unknown to attackers</td><td>Known to attackers</td><td>Known to attackers</td></tr><tr><td>Loot, G</td><td>Heterogeneous, unknown to attackers; distribution is common knowledge</td><td>Unknown to attackers, positively correlated with μ</td><td>Known to attackers</td></tr><tr><td>Attackers&#x27; decision variables</td><td>x, same for all targets</td><td> $x_{L} = x(\mu_{L}, G_{L}^{AV})$  and  $x_{H} = x(\mu_{H}, G_{H}^{AV})$ ,same for all targets of each security level, where $\int_{G}^{\hat{G}} G\varphi(G) dG$  $G_{L}^{AV} = \frac{0}{\hat{G}}$  $\int_{0}^{\infty} \varphi(G) dG$  $G_{H}^{AV} = \frac{\hat{G}}{\int_{\hat{G}}^{\infty} \varphi(G) dG}$ </td><td>Target specific  $x(\mu_{i}, G_{i})$ </td></tr></table>

<table><tr><td>Variant of the game</td><td>Opaque</td><td>Partial transparency</td><td>Complete transparency</td></tr><tr><td>Attacker&#x27;s objective function (return on effort, Ψ)</td><td> $\int_{0}^{\hat{G}} (\pi(\mu_L, x)G - C(x))\varphi(G)dG$  $\Psi = \frac{0}{s + x}$  $\int_{+ \hat{G}}^{\infty} (\pi(\mu_H, x)G - C(x))\varphi(G)dG$  $+ \frac{s + x}{s + x}$ </td><td> $\int_{0}^{\hat{G}} (\pi(\mu_L, x_L)G - C(x_L))\varphi(G)dG$  $\Psi = \frac{0}{s + x_L \int_{0}^{\hat{G}} \varphi(G)dG + x_H \int_{\hat{G}}^{\infty} \varphi(G)dG}$  $\int_{+ \hat{G}}^{\infty} (\pi(\mu_H, x_H)G - C(x_H))\varphi(G)dG$  $+ \frac{s + x_L \int_{0}^{\hat{G}} \varphi(G)dG + x_H \int_{\hat{G}}^{\infty} \varphi(G)dG}{}$ </td><td> $\int_{0}^{\hat{G}} [\pi(\mu_L, x(\mu_L, G))G - C(x(\mu_L, G))] \varphi(G)dG$  $\Psi = \frac{0}{s + \int_{0}^{\hat{G}} x(\mu_L, G)\varphi(G)dG + \int_{\hat{G}}^{\infty} x(\mu_H, G)\varphi(G)dG}$  $+ \frac{s + \int_{0}^{\hat{G}} [\pi(\mu_H, x(\mu_H, G))G - C(x(\mu_H, G))] \varphi(G)dG}{s + \int_{0}^{\hat{G}} x(\mu_L, G)\varphi(G)dG + \int_{\hat{G}}^{\infty} x(\mu_H, G)\varphi(G)dG}$ </td></tr><tr><td>Benefit defender receives from a security investment (present value), Ω</td><td> $\Omega = \frac{N_A \cdot G \cdot (\pi(\hat{x}, \mu_L) - \pi(\hat{x}, \mu_H))}{\delta \cdot N_T \cdot \tau^{OP}}$ </td><td> $\Omega = \frac{N_A \cdot G (\pi(\hat{x}_L, \mu_L) - \pi(\hat{x}_H, \mu_H))}{\delta \cdot N_T \cdot \tau^{PT}}$ </td><td> $\Omega = \frac{N_A \cdot G (\pi(\hat{x}(\mu_L, G), \mu_L) - F(\pi(\mu_H, G), \mu_H))}{\delta N_T \tau^{CT}}$ </td></tr><tr><td>Average time attacker spends on a target, τ</td><td> $\tau^{OP} = s + \int_{0}^{\hat{G}} \left( \int_{0}^{\hat{x}} xd\pi(x, \mu_L) + \hat{x} \int_{\hat{x}}^X d\pi(x, \mu_L) \right) \varphi(G)dG$  $+ \int_{\hat{G}}^{\infty} \left( \int_{0}^{\hat{x}} xd\pi(x, \mu_H) + \hat{x} \int_{\hat{x}}^X d\pi(x, \mu_H) \right) \varphi(G)dG$ </td><td> $\tau^{PT} = s + \int_{0}^{\hat{G}} \left( \int_{0}^{\hat{x}_L} xd\pi(x, \mu_L) + \hat{x}_L \int_{\hat{x}_L}^X d\pi(x, \mu_L) \right) \varphi(G)dG$  $+ \int_{\hat{G}}^{\infty} \left( \int_{0}^{\hat{x}_H} xd\pi(x, \mu_H) + \hat{x}_H \int_{\hat{x}_H}^X d\pi(x, \mu_H) \right) \varphi(G)dG$ </td><td> $\tau^{CT} = s + \int_{0}^{\hat{G}} \left( \int_{0}^{\hat{x}(\mu_L, G)} x(\mu_L, G)d\pi(x(\mu_L, G), \mu_L) \right) \varphi(G)dG$  $+ \int_{0}^{\hat{G}} \left( \hat{x}(\mu_L, G) \int_{\hat{x}(\mu_L, G)}^X d\pi(x(\mu_L, G), \mu_L) \right) \varphi(G)dG$  $+ \int_{\hat{G}}^{\infty} \left( \int_{0}^{\hat{x}(\mu_H, G)} x(\mu_H, G)d\pi(x(\mu_H, G), \mu_H) \right) \varphi(G)dG$  $+ \int_{\hat{G}}^{\infty} \left( \hat{x}_H(\mu_H, G) \int_{\hat{x}(\mu_H, G)}^X d\pi(x(\mu_H, G), \mu_H) \right) \varphi(G)dG$ </td></tr></table>

Table A1. Continued

$$
\begin{array}{r l} & {\frac {\partial \Psi^ {*}}{\partial \hat {G}} = \frac {B _ {L} (\hat {G}) \varphi (\hat {G}) - B _ {H} (\hat {G}) \varphi (\hat {G})}{s + \int_ {0} ^ {\hat {G}} x (\mu_ {L} , G) \varphi (G) d G + \int_ {\hat {G}} ^ {\infty} x (\mu_ {H} , G) \varphi (G) d G}} \\ & {- \frac {\Psi^ {*} \cdot (x (\mu_ {L} , \hat {G}) \varphi (\hat {G}) - x (\mu_ {H} , \hat {G}) \varphi (\hat {G}))}{s + \int_ {0} ^ {\hat {G}} x (\mu_ {L} , G) \varphi (G) d G + \int_ {\hat {G}} ^ {\infty} x (\mu_ {H} , G) \varphi (G) d G}} \\ & {= \frac {(B _ {L} (\hat {G}) - \Psi^ {*} \cdot x (\mu_ {L} , \hat {G})) - (B _ {H} (\hat {G}) - \Psi^ {*} \cdot x (\mu_ {H} , \hat {G}))}{s + \int_ {0} ^ {\hat {G}} x (\mu_ {L} , G) \varphi (G) d G + \int_ {\hat {G}} ^ {\infty} x (\mu_ {H} , G) \varphi (G) d G} \varphi (\hat {G}) > 0} \end{array}
$$

by properties of $\pi$ and $C$ .

For the purpose of finding an equilibrium, we limit our interest to vectors of $x$ that can maximize the attacker's utility at some $\hat{G}$ . As $\hat{G}$ increases, making a randomly chosen target more attractive, the attacker has an incentive to switch sooner, $d\hat{x}_i / d\Psi < 0$ . Because $d\tau / dx_i > 0$ , we also have $d\tau / d\Psi < 0$ .

By properties of $\pi (\cdot)$

$$
\frac {d \pi (\hat {x} _ {H} , \mu_ {H})}{d \Psi} <   \frac {d \pi (\hat {x} _ {L} , \mu_ {L})}{d \Psi} <   0.
$$

Then an increase in attacker's utility increases the benefit from a security investment for any loot size,

$$
\frac {d \Omega}{d \Psi} = \frac {N _ {A} \cdot G \left(\frac {d \pi (\hat {x} _ {L} , \mu_ {L})}{d \Psi} - \frac {d \pi (\hat {x} _ {H} , \mu_ {H})}{d \Psi}\right) - \Omega \frac {d \tau}{d \Psi}}{N _ {T} \tau} > 0.
$$

Because $d\Omega / dG > 0$ , this will also reduce the value of $G$ that solves $\Omega(G) = \mu_H - \mu_L$ , resulting in

$$
\frac {d \hat {G} ^ {*}}{d \Psi} <   0.
$$

The opposite signs of the two best-response correspondence slopes in the $\{\hat{G},\Psi\}$ space imply the uniqueness of the Nash equilibrium. Q.E.D.

## Proof of Proposition 7

Because attackers are best informed in the complete transparency case, $\Psi^{CT*}(\hat{G}) > \Psi^{PT*}(\hat{G})$ for all $\hat{G}$ , which, given $\partial\Psi^{*}/\partial\hat{G} > 0$ , implies that in that version of the game attackers can attain the same utility level at a smaller $\hat{G}$ than in the partial transparency version. Furthermore, $\hat{G}^{CT*}(\Psi) < \hat{G}^{PT*}(\Psi)$ for all $\Psi$ . As a result, the equilibrium value of $\hat{G}$ in the complete transparency game will always be smaller, $\hat{G}^{CT*}(\Psi^{CT*}) < \hat{G}^{PT*}(\Psi^{PT*})$ .

Under complete transparency, attackers' ability to discriminate across targets of the same security type makes the optimal effort increase in $G$ given the target type. This implies $x^{CT*}(\mu_L,\hat{G}) > x^{PT*}(\mu_L,\hat{G}), x^{PT*}(\mu_H,\hat{G}) > x^{CT*}(\mu_H,\hat{G})$ , and $\pi^{CT}(\mu_L,x^*(\mu_L,\hat{G})) > \pi^{PT}(\mu_L,x^*(\mu_L,\hat{G})) > \pi^{PT}(\mu_H,x^*(\mu_H,\hat{G})) > \pi^{CT}(\mu_H,x^*(\mu_H,\hat{G}))$ .

Under partial transparency, the only variation in the benefit the attacker derives from targets of a given type, $B_{i}=\pi(\mu_{i},\hat{x}(\mu_{i},\tilde{G}_{i}))G_{i}-C(\alpha,\hat{x}(\mu_{i},\tilde{G}_{i}),s)=\pi_{i}G_{i}-C_{i}$ , is attributed to the differences in the loot size,

$$
\frac {d B _ {i} ^ {P T}}{d G} = \frac {\partial B _ {i}}{\partial G _ {i}}.
$$

In the complete transparency case,

$$
\frac {d B _ {i} ^ {C T}}{d G _ {i}} = \frac {\partial B _ {i}}{\partial G _ {i}} + \frac {\partial B _ {i}}{\partial \hat {x}} \frac {\partial \hat {x}}{\partial G _ {i}} > \frac {d B _ {i} ^ {P T}}{d G _ {i}}.
$$

Changing the game environment from partial to complete transparency while preserving the same $\hat{G}$ will allow attackers to derive a greater net benefit from at least some targets due to better information and more optimal allocation of effort resulting from it. The greatest increase in $B_{i}$ among all L-type targets will occur at the upper boundary of the L-range, $G = \hat{G}$ . This implies that the relative increase in the net benefit derived from all L-targets will be smaller than for the target with $G = \hat{G}$ ,

$$
\frac {B _ {L} ^ {C T} \left(\hat {G}\right)}{B _ {L} ^ {P T} \left(\hat {G}\right)} > \frac {\int_ {0} ^ {\hat {G}} B _ {L} ^ {C T} \left(G\right) \varphi \big (G \big) d G}{\int_ {0} ^ {\hat {G}} B _ {L} ^ {P T} \left(G\right) \varphi \big (G \big) d G} > 1.
$$

Given $x^{CT*}(\mu_L, \hat{G}) > x^{PT*}(\mu_L, \hat{G})$ (due to attackers' ability to discriminate across targets) and $\partial C / \partial x > 0$ , we have

$$
\frac {\pi_ {L} ^ {C T} \left(\hat {G}\right)}{\pi_ {L} ^ {P T} \left(\hat {G}\right)} > \frac {B _ {L} ^ {C T} \left(\hat {G}\right)}{B _ {L} ^ {P T} \left(\hat {G}\right)} > \frac {\int_ {0} ^ {\hat {G}} B _ {L} ^ {C T} \left(G\right) \varphi \big (G \big) d G}{\int_ {0} ^ {\hat {G}} B _ {L} ^ {P T} \left(G\right) \varphi \big (G \big) d G} > 1.
$$

$$
\int_ {\hat {G}} ^ {\infty} B _ {H} ^ {P T} (G) \varphi (G) d G > \int_ {\hat {G}} ^ {\infty} B _ {H} ^ {C T} (G) \varphi (G) d G
$$

and

$$
\pi_ {H} ^ {P T} (\hat {G}) > \pi_ {H} ^ {C T} (\hat {G})
$$

further imply

$$
\frac {\pi_ {L} ^ {C T} \left(\hat {G}\right) - \pi_ {H} ^ {C T} \left(\hat {G}\right)}{\pi_ {L} ^ {P T} \left(\hat {G}\right) - \pi_ {H} ^ {P T} \left(\hat {G}\right)} > \frac {\int_ {0} ^ {\hat {G}} B _ {L} ^ {C T} \left(G\right) \varphi \big (G \big) d G + \int_ {\hat {G}} ^ {\infty} B _ {H} ^ {C T} \left(G\right) \varphi \big (G \big) d G}{\int_ {0} ^ {\hat {G}} B _ {L} ^ {P T} \left(G\right) \varphi \big (G \big) d G + \int_ {\hat {G}} ^ {\infty} B _ {H} ^ {P T} \left(G\right) \varphi \big (G \big) d G}.
$$

The $\Omega (G) = \mu_H - \mu_L$ condition valid for both cases requires

$$
\frac {\hat {G} ^ {P T}}{\hat {G} ^ {C T}} = \frac {\pi_ {L} ^ {C T} (\hat {G} ^ {C T}) - \pi_ {H} ^ {C T} (\hat {G} ^ {C T})}{\pi_ {L} ^ {P T} (\hat {G} ^ {P T}) - \pi_ {H} ^ {P T} (\hat {G} ^ {P T})}. \frac {\tau^ {P T}}{\tau^ {C T}}.
$$

Due to the greater efficiency of attackers' effort in the complete transparency case, a larger portion of attacks will be successful and we have

$$
\frac {\tau^ {C T}}{s + \int_ {0} ^ {\hat {G}} x (\mu_ {L} , G) \varphi (G) d G + \int_ {\hat {G}} ^ {\infty} x (\mu_ {H} , G) \varphi (G) d G} <   \frac {\tau^ {P T}}{s + x (\mu_ {L} , \tilde {G} _ {L}) + x (\mu_ {H} , \tilde {G} _ {H})},
$$

therefore,

$$
\begin{array}{l} \frac {\hat {G} ^ {P T}}{\hat {G} ^ {C T}} > \frac {\pi_ {L} ^ {C T} (\hat {G} ^ {C T}) - \pi_ {H} ^ {C T} (\hat {G} ^ {C T})}{\pi_ {L} ^ {P T} (\hat {G} ^ {P T}) - \pi_ {H} ^ {P T} (\hat {G} ^ {P T})} \cdot \frac {s + x (\mu_ {L} , \tilde {G} _ {L}) + x (\mu_ {H} , \tilde {G} _ {H})}{s + \int_ {0} ^ {\hat {G}} x (\mu_ {L} , G) \varphi (G) d G + \int_ {\hat {G}} ^ {\infty} x (\mu_ {H} , G) \varphi (G) d G} \\ = \frac {\pi_ {L} ^ {C T} (\hat {G} ^ {C T}) - \pi_ {H} ^ {C T} (\hat {G} ^ {C T})}{\pi_ {L} ^ {P T} (\hat {G} ^ {P T}) - \pi_ {H} ^ {P T} (\hat {G} ^ {P T})} \cdot \frac {\int_ {0} ^ {\hat {G} ^ {P T}} B _ {L} ^ {P T} (G) \varphi (G) d G + \int_ {\hat {G} ^ {P T}} ^ {\infty} B _ {H} ^ {P T} (G) \varphi (G) d G}{\int_ {0} ^ {\hat {G} ^ {C T}} B _ {L} ^ {C T} (G) \varphi (G) d G + \int_ {\hat {G} ^ {C T}} ^ {\infty} B _ {H} ^ {C T} (G) \varphi (G) d G} \cdot \frac {\Psi^ {C T *} (\hat {G} ^ {C T})}{\Psi^ {P T *} (\hat {G} ^ {P T})}. \end{array}
$$

Due to the fact that attackers associate the high security level with a greater expected loot, we always have

$$
\begin{array}{c} \frac {\pi_ {L} ^ {C T} \left(\hat {G} ^ {C T}\right) - \pi_ {H} ^ {C T} \left(\hat {G} ^ {C T}\right)}{\int_ {0} ^ {\hat {G} ^ {C T}} B _ {L} ^ {C T} (G) \varphi (G) d G + \int_ {\hat {G} ^ {C T}} ^ {\infty} B _ {H} ^ {C T} (G) \varphi (G) d G} \\ > \frac {\pi_ {L} ^ {P T} \left(\hat {G} ^ {P T}\right) - \pi_ {H} ^ {P T} \left(\hat {G} ^ {P T}\right)}{\int_ {0} ^ {\hat {G} ^ {P T}} B _ {L} ^ {P T} (G) \varphi (G) d G + \int_ {\hat {G} ^ {P T}} ^ {\infty} B _ {H} ^ {P T} (G) \varphi (G) d G}. \end{array}
$$

Therefore,

$$
\frac {\hat {G} ^ {P T}}{\hat {G} ^ {C T}} > \frac {\Psi^ {C T *} (\hat {G} ^ {C T})}{\Psi^ {P T *} (\hat {G} ^ {P T})}
$$

and, consequently,

$$
\frac {\Psi^ {C T *} (\hat {G}) - \Psi^ {P T *} (\hat {G})}{\hat {G} ^ {P T} (\Psi) - \hat {G} ^ {C T} (\Psi)} <   \frac {\Psi^ {P T *} (\hat {G})}{\hat {G} ^ {C T} (\Psi)}.
$$

The convexity of attackers' best response function, $\Psi^{*}(\hat{G})$ , implies

$$
\frac {\partial \Psi^ {*}}{\partial \hat {G}} > \frac {\Psi^ {C T *} (\hat {G})}{\hat {G} ^ {C T} (\Psi)}.
$$

Combining all the inequalities together yields

$$
\frac {\partial \Psi^ {*}}{\partial \hat {G}} > \frac {\Psi^ {C T *} (\hat {G})}{\hat {G} ^ {C T} (\Psi)} > \frac {\Psi^ {P T *} (\hat {G})}{\hat {G} ^ {C T} (\Psi)} > \frac {\Psi^ {C T *} (\hat {G}) - \Psi^ {P T *} (\hat {G})}{\hat {G} ^ {P T} (\Psi) - \hat {G} ^ {C T} (\Psi)}
$$

and, therefore, $\Psi^{CT*}(\hat{G}^{CT*}) < \Psi^{PT*}(\hat{G}^{PT*})$ . Q.E.D.

## Proof of Proposition 8

As long as $N_{T} >> N_{A}$ , variations in neither in $N_{A}$ nor $N_{T}$ affect attackers' best response functions, $\Psi(\hat{G})$ and $x_{AV}(\hat{G})$ .

When $N_A$ increases, $\hat{G}$ has to decrease in order for $\Omega(G) = \mu_H - \mu_L$ to hold. Due to the shapes of attacker's and defender's best response correspondences (see Proposition 6), equilibrium values of $\hat{G}, \Psi$ , and $x$ decrease but by a factor smaller than the initial increase in $N_A$ . As a result,

$$
\frac {d \Theta}{d N _ {A}} > 0.
$$

Similarly, an increase in $N_{T}$ causes $\hat{G}$ to increase in order for $\Omega(G) = \mu_{H} - \mu_{L}$ to hold. Defenders' best response correspondence shifts toward greater values of $\hat{G}$ . By proof of Proposition 6, this causes the equilibrium values of $\Psi$ and $x$ and therefore the entire bracketed term in Equation (7) to increase as well, resulting in

$$
\frac {d \Theta}{d N _ {T}} > 0.
$$

Because the equilibrium value of $\Psi$ increases by a smaller factor than does $N_{T}$ , the average target's loss decreases,

$$
\frac {\Theta}{N _ {T}} > \frac {d \Theta}{d N _ {T}} > 0.
$$

Q.E.D.
