---
otero_id: 15878
otero_key: "FRNQG5ZW"
title: "Decision-Theoretic and Game-Theoretic Approaches to IT Security Investment"
authors: "Huseyin Cavusoglu; Srinivasan Raghunathan; Wei T. Yue"
year: "2008"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222250211"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/FRNQG5ZW/fulltext/images/5dc91e53f02779fb7e19aeb016f72a357f0c23723bd04de6912c963a97f3d52c.jpg)

# Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# Decision-Theoretic and Game-Theoretic Approaches to IT Security Investment

Huseyin Cavusoglu <sup>a</sup> , Srinivasan Raghunathan <sup>b</sup> & Wei T. Yue b

<sup>a</sup> School of Management, University of Texas, Dallas

University of Texas, Dallas Published online: 08 Dec 2014.

To cite this article: Huseyin Cavusoglu , Srinivasan Raghunathan & Wei T. Yue (2008) Decision-Theoretic and Game-Theoretic Approaches to IT Security Investment, Journal of Management Information Systems, 25:2, 281-304

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222250211

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

# Decision-Theoretic and Game-Theoretic Approaches to IT Security Investment

Huse yin Cav uso glu, Srinv as an Ragh un ath an , and Wei T. Yue

Huseyin Cavusoglu is an Assistant Professor of Information Systems in the School of Management at the University of Texas at Dallas. He received his Ph.D. in Management Science with a specialization in Management Information Systems from the University of Texas at Dallas in 2003. His primary research interests include the economics of information security, assessment of the value of IT security, and IT security management. He received several Best Paper awards and nominations in prestigious IS conferences. His research articles have appeared in several journals, including Management Science, Information Systems Research, INFORMS Journal on Computing, INFORMS Decision Analysis, IEEE Transactions on Software Engineering, International Journal of Electronic Commerce, Communications of the ACM, and others. He serves on the steering committee of the Workshop on the Economics of Information Security.

Srinivasan Ragh unath an is a Professor of Information Systems in the School of Management at the University of Texas at Dallas. He obtained a B.Tech. in Electrical Engineering from IIT, Madras, a Post Graduate Diploma in Management from IIM, Calcutta, and a Ph.D. in Business Administration from the University of Pittsburgh. His current research interests are in the economics of information security and the value of collaboration in supply chains. His papers have been published in leading journals such as Management Science, Information Systems Research, various IEEE transactions, IIE transactions, and others. He serves as an associate editor of Information Systems Research and Journal of Information Technology and Management.

Wei T. Yue is an Assistant Professor in the MIS area at the University of Texas at Dallas. He received his Ph.D. in MIS from Purdue University, West Lafayette, Indiana. His current teaching and research interests are in the areas of information security, text mining, and data mining. His work has appeared in several journals, including IEEE Transactions on System, Man, Cybernetics, Electronic Markets, Information Technology and Management, European Journal of Operational Research, and Decision Support Systems. His research won the Best Paper award at the Workshop on Information Technologies and Systems (WITS).

Abstrac t: Firms have been increasing their information technology (IT) security budgets significantly to deal with increased security threats. An examination of current practices reveals that managers view security investment as any other and use traditional decision-theoretic risk management techniques to determine security investments. We argue in this paper that this method is incomplete because of the problem’s strategic nature—hackers alter their hacking strategies in response to a firm’s investment strategies. We propose game theory for determining IT security investment levels and compare game theory and decision theory approaches on several dimensions such as the investment levels, vulnerability, and payoff from investments. We show that the sequential game results in the maximum payoff to the firm, but requires that the firm move first before the hacker. Even if a simultaneous game is played, the firm enjoys a higher payoff than that in the decision theory approach, except when the firm’s estimate of the hacker effort in the decision theory approach is sufficiently close to the actual hacker effort. We also show that if the firm learns from prior observations of hacker effort and uses these to estimate future hacker effort in the decision theory approach, then the gap between the results of decision theory and game theory approaches diminishes over time. The rate of convergence and the extent of loss the firm suffers before convergence depend on the learning model employed by the firm to estimate hacker effort.

Key w ords and ph rases: decision theory, game theory, IT security investments.

Attack s on c omputer systems are inc reasing at a rapid rate. Consequently, information technology (IT) security, once thought a luxury, is getting increased attention among corporate managers. Over the last decade, the annual CSI/FBI security surveys and the Computer Emergency Response Team (CERT ) statistics have shown that the poor state of information security has been presenting significant challenges to firms (www.cert.org/stats/cert\_stats.html) [33]. The recurring events of security breaches have forced many firms to increase their investments in security technologies such as firewalls, intrusion detection systems (IDSs), encryption, biometric and other authentication devices, and access control systems. Although deployment of these technologies may mitigate risks associated with security breaches, firms are unclear about how much to invest in security because the return on security investment (ROSI) is difficult to estimate.

Determining the appropriate level of IT security investment has become one of the critical decisions faced by chief security officers [3]. The central question in security management has changed from what is technically possible to what is economically efficient [24]. Crume points spending on protection should not exceed the value of the asset that we want to protect [14]. In other words, each firm should strike an appropriate balance between its risk exposure and the opportunity to mitigate the risk through investments in security. This balance must be defined within the risk environment of the business, which includes firm and hacker characteristics.

An examination of current business practices in IT security management reveals that managers generally view security investment as any other IT investment and use decision-theoretic risk management and, more commonly, other less-sophisticated techniques to determine security investment level [26]. Although decision theory and other traditional risk analysis methods can provide a useful starting point for determining security investment level, they are incomplete because of the security problem’s strategic nature.

In the security context, strategic nature implies that hackers do not randomly select their targets [13]. Several empirical and theoretical studies support the notion that hackers rationally make their choices based on the amount of effort that will be required to succeed in hacking and the reward from a successful hack, which is partly dependent on how secure the system is [38, 41]. The motivation of hackers will partly determine whether a hacker is strategic. Leeson and Coyne [30] distinguish between fame-driven and profit-driven hackers. In the same vein, Campbell et al. [6] makes a distinction between “sport” hackers, who are not interested in doing anything more than to “take a look around,” and others who derive financial advantage from hacking. While there are numerous fame-driven and sport hackers in the population, the damage caused by profit-minded hackers is much larger [40], causing firms to make security decisions based on actions of these individuals [4]. When a firm faces strategic hackers, the hacker effort, in addition to the firm’s security investment, determines the vulnerability of the system being protected.

The reason for the limitation of traditional models, when applied to analyze IT security problems, can be stated as one simple proposition: They do not allow a firm’s security investment to influence the behavior of hackers. On the contrary, behavioral influences of security technology on hackers have long been recognized by researchers and practitioners in the security community. Cavusoglu et al. [10] showed that the value of IDSs comes from a deterrence effect on hackers. Yue and Çakanyildirim [44] showed that an organization can use a mixture of reactive and proactive responses to the alarms generated by IDSs. Many have pointed out that security should be viewed as a “cat-and-mouse” game played by firms and hackers [2, p. 30]. That is, a “correct” model for analyzing security investments should capture the strategic interaction between the firm and hackers.

Because decision theory is designed to analyze decision making in situations where “nature” is the only “opponent,” it is inadequate to address decisions about security investment.<sup>1</sup> Modeling the interaction between a firm’s and hackers’ decisions requires game theory. Traditional decision theory assumes that the firm views hackers’ effort as exogenous. Although the firm can perform sensitivity analysis with respect to the estimated parameters, a decision-theoretic model still provides only partial solutions. In the game-theoretical model, both the firm’s investment level and the hacker’s effort are endogenously determined.

We analyze the problem of determining IT security investment level from decision theory and game theory perspectives. We consider both sequential and simultaneous games between firm and hackers. We compare results along several dimensions such as the investment level, vulnerability, and payoff from investment. We find that the firm realizes the maximum payoff when the firm and the hacker play a sequential game with the firm as the leader and the hacker as the follower.<sup>2</sup> The sequential setting is important because of the current discussion within regulatory bodies about whether public firms must be mandated to reveal their IT security management policies. Sequential game requires that the firm move before the hacker so that the hacker is able to observe the firm’s investment prior to making his or her decision about effort. Even if the firm and hackers do not play a sequential game, the firm enjoys a higher payoff in the simultaneous game approach compared to the decision theory approach except when the firm’s estimate of the hacker effort is sufficiently accurate. We also show that if the firm learns from prior observations of hacker effort and uses these to estimate the future hacker effort, then the gap between results when decision theory is used and those when they play a simultaneous game approach diminishes over time. The learning model affects the rate of convergence of the decision theory solution to that of when a simultaneous game is played and the extent of loss the firm incurs before convergence by using the decision theory as opposed to the game theory approach.

## Approaches to General IT Investment and IT Security Investment

Research on IT sec urity investments is limited, but research on general IT investment is extensive. Several researchers have developed frameworks for evaluation of IT projects [23, 36]. These frameworks include descriptions of formal processes to evaluate IT investment projects using qualitative and quantitative criteria. Qualitative criteria often consider the impact of IT on internal business processes or external business environment [23]. Quantitative criteria include traditional capital budgeting methods such as discounted cash flow (DCF) analysis. DCF assumes that projects’ costs and benefits can be quantified, which is generally not easy for IT investments. The reason is that IT investments manifest themselves in different dimensions, such as (1) profitability (e.g., increased revenues or decreased costs), (2) productivity (e.g., reduced defect rate), or (3) consumer value (e.g., ease of use or personalized services) [27].<sup>3</sup>

Several other IT evaluation methods have also been proposed in the literature. For instance, Kaplan [25] suggests reversing the DCF process; that is, instead of putting price tags on intangible benefits, organizations should estimate how large these benefits should be in order to justify an IT investment project. In cases where benefits and costs are hard to quantify due to uncertainties, Clemons [12] proposes using probabilitybased tools such as a decision tree in the evaluation process. Researchers have also suggested using real option analysis to evaluate IT investments [5, 28].

The process by which organizations determine investments is much more blurred for IT security projects than for traditional IT projects. A recent survey indicated that four approaches are popular among security managers to determine IT security investments [26]. The first approach, which is the most popular, is fear, uncertainty, and doubt (FUD) [3]. Security vendors have used this strategy to sell investments in security. Although this approach may force organizations to invest in basic security solutions, such as firewalls and antivirus systems, it cannot substitute for a comprehensive security program. The second approach, which is based on the cost-effectiveness of investments, asks the question “What is the most I can get given that I am going to spend \$X?” The primary limitation of this approach is that it does not help an organization decide on how much to invest in security. The third approach uses indirect estimation of dollar value of loss associated with security breaches, such as loss in market value as a result of public announcement of security breaches, as a proxy to estimate real cost of security breaches [8]. While the indirect loss estimates can assess both tangible and intangible costs of security breaches, they are less useful in deciding how much to invest in security. The fourth approach uses the traditional risk or decision analysis framework. The idea is to identify the potential risk of security violations in terms of their damage and likelihood, and then to compute the expected loss [41]. Cavusoglu et al. [9] and Hoo [24] propose using a decision-analytic framework to evaluate different baskets of safeguards from a cost–benefit perspective for IT security investment decisions. Rainer et al. [34] and Sun et al. [42] develop methodologies to assess organizations’ security risks. Longstaff et al. [31] propose a method to assess the efficacy of risk management based on reduction in risk through security investments. Han et al. [20] examine the proper strategic actions that can be taken in order to reduce risks in an interorganizational setting. Our work was inspired by Gordon and Loeb [18], who show that cost considerations may cause firms to decrease their security investment when security vulnerability increases beyond a threshold.

In essence, the above approaches for determining IT security investments are not too different from general IT investment models. However, the context of IT security differs from a general IT investment context. In security, organizations are often dealing with strategic adversaries who are looking for opportunities to exploit vulnerabilities in systems. Hackers attack systems that are vulnerable and those that do not have appropriate controls. To be able to compete, organizations should act strategically when investing in security. When choosing a security investment level, firms cannot treat the risk environment as static. As pointed out by Stoneburner et al. [41], security investment increases the hacker’s cost and when the attacker’s cost becomes larger than its benefit, the hacker may be forced not to attack the firm in the first place. Consequently, to accurately analyze the IT security investment decisions, we need to model threats and vulnerabilities, which are determined by the strategic interactions between organizations and hackers. Game theory is appropriate to model such strategic interactions.

Recently, researchers have begun to investigate information security problems using game-theoretical models. Kunreuther and Heal [29] and Varian [43] study the effect of correlation (which they termed interdependence) between firms’ information security risks. When the security of the whole system depends on investments of individual firms that are part of the system, security has the characteristics of a public good, and free riding occurs [43]. Kunreuther and Heal consider a model in which firms could eliminate security risks through security investments and showed that either all or no firm will invest in security. Hausken [21] shows that firms’ security investments are affected by interdependence, attackers’ income, and whether attackers are able to substitute their efforts among different targets. Cremonini and Nizovtsev [13]<sup>4</sup> show that when attackers can substitute their efforts between targets, the effect of security investment is stronger inducing firms with stronger defense to reveal their protection. Gordon et al. [19] find that when firms share security information, each firm has reduced incentives to invest in information security. In contrast, Gal-Or and Ghose [17] find that security technology investments and security information sharing act as “strategic complements.” Hausken [22] assumes substitutability between own security investment and information received by the other firm, but allowed for complementar ity when the interdependence is negative.

In another stream of research, researchers have developed game-theoretic models of security in assessing the value of individual (such as IDS) and combinations of security mechanisms (such as IDS and firewall) [8, 10, 11]. Cavusoglu and Raghunathan [7] compare decision theory and game theory approaches to the problem of configuring IDSs. Unlike the prior studies in the literature, the focus of our work is not on assessing the value of specific technologies, but on comparing game-theoretic and decision-theoretic approaches to the security investment problem. Consequently, we abstract away from security technologies and model the security investment problem at the firm level.

## Model Framework

We c onsider a firm dec iding th e investment level to protect its information assets from hackers. A security breach would result in a monetary loss L to the firm.<sup>5</sup> The loss can be tangible, such as loss of business due to disruption, or intangible, such as loss in customer trust. The loss may also include costs to repair the damages caused by attacks and liabilities. The firm can reduce the probability of a security breach, s, by investing in security technologies. The probability of breach is also dependent on hackers’ efforts, c, to break into the system. The asset protected by the firm has an inherent vulnerability, v, which represents the probability of breach when the firm does not invest and the hacker does not incur any effort. The inherent vulnerability models the reality that often software security glitches are readily available on the Internet, and hackers do not have to spend any effort to exploit them if the firm does not address such glitches. Thus, we define $s ( \nu , z , c )$ to be the probability of breach based on the firm’s investment level, the attacker’s effort level, and the firm’s inherent vulnerability level. We make the following assumptions about the shape of $s ( \nu , z , c )$

Assumption 1: $s ( \nu , 0 , 0 ) = \nu .$ A firm has an inherent vulnerability level given that there is no effort exerted by the hacker, and no investment is made by the firm.

Assumption $2 \colon s ( 0 , z , c ) = 0 .$ A firm that has zero vulnerability will remain fully protected for any level of investment and hacker effort.

Assumption 3: For all other s(v, z, c), $s _ { _ z } < 0 , s _ { _ z z } > 0 , s _ { _ c } > 0 , s _ { _ c c } < 0 . ^ { 6 }$ Essentially, a higher level of investment results in a lower probability of breach, and investment exhibits a diminishing marginal return in reducing the vulnerability. More effort from the attacker results in a higher probability of successful attack, and hacker effort exhibits a diminishing marginal return in increasing likelihood of success, for a given level of investment and inherent vulnerability.

The assumption about the declining marginal return of investment is motivated by Moitra and Konda [32], who derived the function between system survivability and cost of defense using the CERT incident data. They found that survivability is an increasing concave function of cost, which implies that probability of attack success is a decreasing convex function of investment.

We also impose restrictions on model parameter values so that $s ( \nu , z , c )$ lies between 0 and 1. Specific restrictions depend on the functional form used.

Hackers derive benefits, H, out of security breaches.<sup>7</sup> Previous studies have shown that incentives for hackers may be related to financial gain, curiosity, self-esteem, vandalism, peer approval, public attention, and politics [37, 39]. Hacker effort includes activities that are part of a typical hacking process such as collecting information about the target’s vulnerability, carrying out the attack, and, finally, conducting postattack activity.

We assume that the firm and the hacker are risk neutral. We also assume that all parameters are common knowledge. Both the firm and the hacker maximize their respective payoffs. We derive the firm’s optimal investment levels using decision theory and game theory approaches next.

## Decision Theory Approach

In the decision theory approach, the firm assumes that its decision has no impact on the attacker. Thus, the firm estimates possible hacker efforts along with their probabilities and uses them as parameters in its payoff maximization model to determine the optimal investment level. Let vectors $c \equiv \{ c _ { 1 } , c _ { 2 } , . . . , c _ { n } \}$ and $\boldsymbol \Theta \equiv \{ \boldsymbol \Theta _ { 1 } , \boldsymbol \Theta _ { 2 } , . . . , \boldsymbol \Theta _ { n } \}$ , respectively, represent the estimated hacker efforts and the corresponding probabilities. Figure 1 shows the decision tree representation of the firm’s investment decision z.

The firm maximizes its expected payoff from security investment, which is

$$
g _ {f} = \left[ v - \sum_ {i = 1} ^ {n} \theta_ {i} s (v, z, c _ {i}) \right] L - z.\tag{1}
$$

The first-order condition for the maximization problem is given by

$$
\frac {\partial g _ {f}}{\partial z} = - \frac {\partial}{\partial z} \left(\sum_ {i = 1} ^ {n} \theta_ {i} s (v, z, c _ {i}) L\right) - 1 = 0.\tag{2}
$$

Thus, the optimal investment under the decision theory approach, $z _ { D T } ^ { * }$ satisfies the following equation:

$$
\left(\frac {\partial}{\partial z} \sum_ {i = 1} ^ {n} \theta_ {i} s (v, z, c _ {i})\right) _ {z = z _ {D T} ^ {*}} = - \frac {1}{L}.\tag{3}
$$

Although the firm assumes that its actions do not have any impact on the hacker, the hacker, being strategic, maximizes his or her expected utility by first assessing the firm’s vulnerability. The hacker’s expected utility and the first-order condition are as follows:

$$
g _ {h} = \biggl [ s \Bigl (v, z _ {D T} ^ {*}, c \Bigr) - v \biggr ] H - c\tag{4}
$$

$$
\frac {\partial g _ {h}}{\partial c} = \frac {\partial s (v , z _ {D T} ^ {*} , c)}{\partial c} H - 1.\tag{5}
$$

![](/api/attachments/FRNQG5ZW/fulltext/images/f1904526e3f92aebd53ba344bb0942a749a859d638f873cbd714de865b9a198f.jpg)  
Figure 1. A Decision Tree Representation of the Firm’s Action

Thus, the optimal effort, $c _ { D T } ^ { * }$ satisfies the following equation:

$$
\left(\frac {\partial s (v , z _ {D T} ^ {*} , c)}{\partial c}\right) _ {c = c _ {D T} ^ {*}} = \frac {1}{H}.\tag{6}
$$

Substituting the solutions from Equations (3) and (6) into Equation (1) gives the firm’s expected payoff from security investment.

## Game Theory Approach

In the game theory approach, the firm makes its decision by anticipating the behavior of the strategic hacker in response to its action. The nature of the game that will be played depends on the timings of hacker’s and firm’s actions. We consider two scenarios. In the simultaneous game, the hacker and the firm make, respectively, effort and investment decisions simultaneously. In the sequential game, the firm decides on its investment decision first and then the hacker makes his or her effort decision after learning the firm’s investment decision. Both scenarios are plausible in security contexts. If the firm announces its strategy publicly, say, by revealing the investment it has made in technologies such as firewall, IDS, and authentication systems, and physical monitoring and inspection procedures, then hackers could use this information to assess the vulnerability of the firm. Because investments in technologies are often irreversible, hackers could often verify such information during the initial information-gathering phase of the hacking process and then determine their effort based on such information, which in turn will result in a sequential game being played. For example, the Internal Revenue Service routinely announces its auditing strategy to deter tax evasion, and tax evaders commonly take the auditing strategy into account while determining their strategies. Hackers often employ techniques such as social engineering and digital probes to determine the protection level of a firm before choosing their hacking strategies. However, even if the firm makes its decision first, a sequential game will be played if and only if the hackers are able to observe the firm’s decisions and believe that the firm will not deviate from its decisions. If hackers are unable to verify or do not believe the firm’s decision, then the firm and hackers will play a simultaneous game, in which each party assumes that the other party will adjust its strategy based on the other’s actions. In this section, we analyze both scenarios and identify a Nash equilibrium for each. In a Nash equilibrium, neither player has an incentive to deviate from the equilibrium as long as the other player does not deviate.

The firm’s and the hacker’s payoff functions, respectively, are

$$
g _ {f} = \Big [ v - s (v, z, c) \Big ] L - z\tag{7}
$$

$$
g _ {h} = \Big [ s (v, z, c) - v \Big ] H - c.\tag{8}
$$

## Simultaneous Game Approach

We first solve the simultaneous game. The first-order conditions for the firm and the hacker, respectively, are

$$
\frac {\partial g _ {f}}{\partial z} = - \frac {\partial s (v , z , c)}{\partial z} L - 1\tag{9}
$$

$$
\frac {\partial g _ {h}}{\partial c} = \frac {\partial s (v , z , c)}{\partial c} H - 1.\tag{10}
$$

Solving Equation (9) and Equation (10) simultaneously, we get the optimal investment level for the firm, $z _ { S G } ^ { * } ,$ and optimal effort level for the hacker, $c _ { s _ { G } } ^ { * } ,$ in the simultaneous game. Note that these quantities satisfy the following equation:

$$
\left( \begin{array}{c} \frac {\partial s (v , z , c)}{\partial z} \\ \frac {\partial s (v , z , c)}{\partial c} \end{array} \right) _ {z = z _ {S G} ^ {*}, c = c _ {S G} ^ {*}} = - \frac {H}{L}.\tag{11}
$$

The structure of Equation (11) is similar to that obtained when each side of Equation (3) is divided by the corresponding side of Equation (6).

## Sequential Game Approach

We solve the sequential game using backward induction. That is, the firm determines the hacker’s optimal effort for a given level of investment. Then, the firm makes its investment decision based on this anticipated hacker effort.

Let $c _ { \scriptscriptstyle h } ( z )$ be the solution to Equation (10). Then, the firm’s optimal investment level in the sequential game, $z _ { S E } ^ { * } ,$ satisfies the following condition:

$$
\left(\frac {\partial s (v , z , c _ {h} (z))}{\partial z}\right) _ {z = z _ {S E} ^ {*}} = - \frac {1}{L}.\tag{12}
$$

Further analysis and comparison of solutions under the decision theory and game theory approaches require an explicit functional form for $s ( \nu , z , c )$ . For illustration purposes, we assume the following functional form for $s ( \nu , z , c )$ in the rest of the paper.<sup>8</sup>

$$
s (v, z, c) = v (\gamma c + 1) ^ {\phi} (\alpha z + 1) ^ {- \beta},\tag{13}
$$

where $\begin{array} { r } { \beta \geq 1 , \alpha > 0 , 0 \leq \phi < 1 , \gamma > 0 . } \end{array}$

The above functional form for s satisfies Assumptions A1–A3. Further, we assume that v is sufficiently small to ensure an interior solution and to ensure that $s ( \nu , z , c )$ lies between 0 and 1 in the equilibrium. Gordon and Loeb [18] used a similar function to analyze IT security investments using a decision theory model.<sup>9</sup> For the functional form given in Equation (13), we can compute the following interior optimal solutions for investment levels and hacker efforts in the decision theory, simultaneous game, and sequential game situations.

Define $L _ { \phantom { } _ { 0 } } = \alpha \beta L , H _ { \phantom { } _ { 0 } } = \gamma \phi H , c _ { \phantom { } _ { 0 } } = \Sigma _ { i = 1 } ^ { n } \theta _ { i } ( \gamma c _ { i } + 1 ) ^ { \phi } .$ Then,

$$
z _ {D T} ^ {*} = \frac {1}{\alpha} \Biggl [ \left(v L _ {0} c _ {0}\right) ^ {\frac {1}{1 + \beta}} - 1 \Biggr ]\tag{14}
$$

$$
c _ {D T} ^ {*} = \frac {1}{\gamma} \left[ \left[ v H _ {0} ^ {(1 + \beta)} \left(L _ {0} c _ {0}\right) ^ {- \beta} \right] ^ {\frac {1}{(1 - \phi) (1 + \beta)}} - 1 \right]\tag{15}
$$

$$
z _ {S G} ^ {*} = \frac {1}{\alpha} \Biggl [ \left[ v H _ {0} ^ {\phi} L _ {0} ^ {1 - \phi} \right] ^ {\frac {1}{1 - \phi + \beta}} - 1 \Biggr ]\tag{16}
$$

$$
c _ {S G} ^ {*} = \frac {1}{\gamma} \left[ \left[ v H _ {0} ^ {(1 + \beta)} L _ {0} ^ {- \beta} \right] ^ {\frac {1}{1 - \phi + \beta}} - 1 \right]\tag{17}
$$

$$
z _ {S E} ^ {*} = \frac {1}{\alpha} \Biggl [ \left[ \nu (1 - \phi) ^ {- (1 - \phi)} H _ {0} ^ {\phi} L _ {0} ^ {1 - \phi} \right] ^ {\frac {1}{1 - \phi + \beta}} - 1 \Biggr ]\tag{18}
$$

$$
c _ {S E} ^ {*} = \frac {1}{\gamma} \left[ \left[ v (1 - \phi) ^ {\beta} (H _ {0}) ^ {(1 + \beta)} L _ {0} ^ {- \beta} \right] ^ {\frac {1}{1 - \phi + \beta}} - 1 \right].\tag{19}
$$

Note that an interior solution exists in the decision theory approach when $\nu < ( L _ { 0 } c _ { 0 } ) ^ { \{ \} } /$ $H _ { 0 } ^ { \phi }$ . In the game theory approach, an interior solution exists when $\nu < L _ { 0 } ^ { \mathrm { \tiny ~ \beta } } / H _ { 0 } ^ { \mathrm { \tiny ~ \phi } }$

## Comparison of Decision Theory and Game Theory Approaches

We c ompare th e th ree approach es on th ree k ey dimensions of interest to the firm—the firm’s payoff, the investment level, and the probability of breach.

# Firm’s Payoff from IT Security Investment

We prove the following result:

Proposition 1: If the hacker is strategic,

(a) the firm’s payoff is higher when the firm and the hacker play the sequential game, with the firm as the leader, than (i) when the firm and the hacker play a simultaneous game and (ii) when the firm assumes that the hacker is nonstrategic, and hence uses the decision theory approach, that is, $g _ { f , S E } ^ { * } \geq g _ { f , D T } ^ { * } , g _ { f , S E } ^ { * } \geq g _ { f , S G } ^ { * } .$

(b) The firm’s payoff is higher when it uses the decision theory approach than when both the firm and the hacker play the simultaneous game if and only $i f c _ { o }$ lies within a range [c\_, c ], that is, $g _ { f , D T } ^ { * } \ge g _ { f , S G } ^ { * }$ if and only $i f \underline { { c } } < c _ { o } < \overline { { c } }$

Proofs for all results are in the Appendix.

Proposition 1 shows that the firm’s payoff is maximum when the firm and hackers play a sequential game. This is consistent with results about the first-mover advantage in the Stackelberg games. By moving first, the firm becomes the leader and the hacker becomes the follower in the sequential game. That is, the hacker reacts to the decisions made by the firm. The firm will obtain the maximum payoff in this scenario because, as the first mover, it has the ability to anticipate the hacker’s reaction and thus optimizes its decision based on the reaction function of the hacker.

Suppose that the firm is unable to move first; then the firm and the hacker will play a simultaneous game when the firm acts strategically. In this case, our result (Proposition 1(a)) that the firm could be better off when it acts nonstrategically (i.e., when it uses decision theory) instead of strategically (i.e., when it uses game theory) to deal with a strategic adversary is counterintuitive. One would expect that the firm would be better off when it takes into account the reaction of the hacker compared to the case when it does not. The counterintuitive result can be explained as follows. Under decision theory, even though the firm may believe that the hacker is nonstrategic, because the firm makes the decision first, and the hacker reacts to the firm’s decision subsequently, the firm may enjoy a first-mover advantage because the firm controls the hacker’s incentives to hack by investing first. However, the firm may either over- or underestimate the hacker effort when it makes its decision. This error in estimation can offset the benefits from acting first. Underestimation of hacker effort leads to lower security investment and higher hacking. Overestimation leads to increased security investment and lower hacking. In both cases, depending on the extent of under- or overestimation, either a higher damage from hacking or a higher level of investment may offset the benefit from the first-mover advantage. In summary, if the firm is able to estimate the hacker effort sufficiently accurately, then the firm is better off using the decision theory than a simultaneous game. Further, the fact that the decision theory approach is better within the range $\underline { { c } } < c _ { 0 } < \overline { { c } }$ is explained by the fact that the firm’s payoff is concave in $c _ { 0 } . \mathrm { A s } \ c _ { 0 }$ increases, the firm increases its investment. But since security investment has a declining marginal return, the payoff starts to decline when $c _ { 0 }$ is greater than a critical value.

## Firm’s Investment Levels and Breach Probabilities

We prove the following result:

Proposition 2:

(a) The investment level when the firm assumes that the hacker is nonstrategic is less than, equal to, or higher than that when the firm assumes that the hacker is strategic and they play a simultaneous game, and the breach probability when the firm assumes that the hacker is nonstrategic is greater than, equal to, or less than that when the firm assumes that the hacker is strategic and they play a simultaneous game if, respectively,

$$
c _ {0} \left[ \begin{array}{l} <   \\ = \\ > \end{array} \right] c _ {S G \_ D T} ^ {2} = \left[ v H _ {0} ^ {(1 + \beta)} L _ {0} ^ {- \beta} \right] ^ {\frac {\phi}{1 - \phi + \beta}}.
$$

(b) The investment level when the firm assumes that the hacker is nonstrategic is less than, equal to, or higher than that when the firm assumes that the hacker is strategic and they play a sequential game, and the breach probability when the firm assumes that the hacker is nonstrategic is greater than, equal to, or less than that when the firm assumes that the hacker is strategic and they play a sequential game if, respectively,

$$
c _ {0} \left[ \begin{array}{l} <   \\ = \\ > \end{array} \right] c _ {S E \_ D T} ^ {2} = \left[ v (1 - \phi) ^ {\frac {(1 - \phi) (1 + \beta)}{\phi}} H _ {0} ^ {(1 + \beta)} L _ {0} ^ {- \beta} \right] ^ {\frac {\phi}{1 - \phi + \beta}}.
$$

(c) The investment level is higher and the breach probability is lower when the firm and the hacker play a sequential game than when they play a simultaneous game, that is, $z _ { s E } ^ { * } \ge z _ { s G } ^ { * } .$

Propositions 2(a) and 2(b) are intuitive. When the firm assumes that the hacker is nonstrategic, if its estimate of the hacker effort is greater than a critical value, it invests more compared to what it would invest if it assumes that the hacker is strategic. Proposition 2(c) shows that if the firm and the hacker play a sequential game, the firm invests more, and consequently deters the hacker more as compared to when they play a simultaneous game. The result about the breach probability is intuitive because the behavior of breach probability is opposite to that of investment level.

We illustrate the theoretical analysis with a numerical example in the following section.

## A Numerical Example

For our numerical example, we use the following parameter values: $\nu = 0 . 9 5 , \alpha = 0 . 2 ,$ $\beta = 2 , \gamma = 2 0 , \phi = 0 . 5 , H = 5 0$ , and $L = 1 0 0$ . Figures 2, 3, and 4 show the comparisons between results under decision theory and game theory approaches. Figures 2 and 3 show that if the firm uses the decision theory approach, then the investment level is increasing and the breach probability is decreasing in the firm’s estimate of the hacker effort, $c _ { 0 } .$ These figures also confirm Proposition 2(a). Specifically, when $c _ { 0 } > 9 . 4 2$ 4 the investment level is higher and the breach probability is lower when the firm uses the decision theory approach than when the firm and the hacker play a simultaneous game. Figure 4 shows that the realized payoff is a concave function of the estimated hacker effort under the decision theory approach, which reflects the trade-off between the first-mover advantage and the risk of overestimation of hacker effort. For the numerical values mentioned above, the firm realizes a higher payoff when it uses the decision theory approach than when the firm and the hacker play a simultaneous game if $c _ { 0 }$ lies between 9.42 and 23.11.

![](/api/attachments/FRNQG5ZW/fulltext/images/28eb0f0b0ba0a85a6164a2b6f69726c94bfbc198fd62edcf96eebbdd1bcb72d2.jpg)  
Figure 2. IT Security Investment

![](/api/attachments/FRNQG5ZW/fulltext/images/02fa0888ddb98beebbd0242c13af6d05a7bcba6ddb656dad787452e11600d6da.jpg)  
Figure 3. Breach Probability

## Dynamic Learning Under the Decision Theory Approach

In our previous analysis of th e dec ision th eory approach , we assumed that the firm and the hacker make their decisions only once and do not change their strategies later. However, over time, the firm and hacker may learn about the behavior of each other, update their estimates, and may adjust their strategies accordingly. Learning is particularly relevant if the firm uses the decision theory approach because the firm may be able to observe hacker behavior and estimate hacker effort more accurately in subsequent periods based on prior observations. Even in game theory, Fudenberg and Levine [16], in their seminal book The Theory of Learning in Games, develop an alternative explanation that the equilibrium in a simultaneous game arises as the long run outcome of a process in which less than fully rational players grope for optimality over time. We analyze the effect of such learning on the attractiveness of the decision theory approach vis-à-vis the game theory approaches in this section.

![](/api/attachments/FRNQG5ZW/fulltext/images/59958becf91d053c80e17c81ac4155cd2f05dfdbfa829e41e39d578a716061e8.jpg)  
Figure 4. Expected Payoff

We assume there are N periods in the investment horizon. During each period t, the firm makes its investment decision, $z _ { D T } ^ { t }$ , and the hacker makes his or her effort decision, $c _ { D T } ^ { t } ,$ for that period. At the end of the period, each player realizes its payoff. Each player also observes the other party’s decision during each period. The firm estimates the hacker effort during each period, $\begin{array} { r } { c _ { { D T } } ^ { \prime } , } \end{array}$ based on observed hacker efforts in preceding period(s) and uses this estimate to make its investment decision. That is, the firm’s strategies will change over time because of learning.

The decision theory solution will depend critically on how the firm updates its estimate of the hacker effort or the learning model employed by the firm. A frequently employed learning model in the economics literature is the exponentially fading memory [1]. This learning model is represented as the following equation:

$$
\overline {{c _ {D T} ^ {t}}} = \sum_ {k = 0} ^ {t - 1} a _ {t k} c _ {D T} ^ {k},\tag{20}
$$

where

$$
a _ {t k} = \rho^ {t - 1 - k} / \sum_ {k = 0} ^ {t - 1} \rho^ {k}, \rho \in [ 0, 1 ].
$$

The weights decrease exponentially as in a geometric progression with ratio ρ, implying that old observations are less relevant than new observations. For ${ \rho } = 0$ , we have myopic estimate, $\overline { { c _ { D T } ^ { t } } } = c _ { D T } ^ { \ t - 1 }$ . For $\rho = 1$ , we have the uniform distribution of weights, $a _ { _ { t k } } = 1 / t .$

![](/api/attachments/FRNQG5ZW/fulltext/images/7ef8590b8f165952e379d5650d44f4d0b127331ffbb2613a067a40143df3c97f.jpg)  
Figure 5. An Illustration of the Convergence of Decision-Theoretic and Game-Theoretic Outcomes

For any given ρ, the firm’s investment level during period t can be computed by substituting $\overline { { c _ { _ { D T } } ^ { t } } }$ for the firm’s estimate of hacker effort during that period. Subsequently, we can compute the hacker effort in each period by substituting the firm’s investment level in the hacker’s first-order condition. Game theorists have explained and analyzed simultaneous game equilibrium in terms of alternating moves by players based on prior observations [35]. Consequently, we predict that the decision theory solution under learning is likely to converge to the equilibrium that will occur when the firm and the hacker play a simultaneous game.<sup>10</sup> This explanation can be illustrated using Figure 5, which shows the reaction functions of the firm and the hacker under a myopic learning policy. $\mathbf { A } \mathrm { t } \ t = 1$ , assume that the firm estimates the hacker effort to be $c _ { D T } ^ { 0 }$ and invests $z _ { D T } ^ { 1 } .$ In response, the hacker reacts with an effort of ${ c } _ { D T } ^ { 1 } ,$ which becomes the firm’s estimate during period 2. The firm invests ${ z _ { D T } ^ { 2 } }$ and the hacker invests an effort of $c _ { D T } ^ { 2 } .$ As this process gets repeated over several periods, we can observe that the hacker and firm decisions converge to the intersection point of the reaction functions, which is the Nash equilibrium for the simultaneous game.

Numerical experiments confirmed that the solution of decision theory under learning converges to the simultaneous game solution irrespective of the learning parameter value. However, as seen in Figures 6 and 7, the convergence patterns in investment and effort levels depend on the learning model employed.

Our primary interest in dynamic analysis of the decision theory approach lies in the convergence properties. Because a theoretical analysis of the effect of the learning parameter on the convergence properties appears to be intractable, we resort to numerical simulations. We used the same parameter values stated under “A Numerical Example.” We generated $c _ { 0 }$ from a uniform distribution over the range [2.2–6.59]. The range represents the case when the error in the firm’s initial estimate, before making any observation of the hacker, is within 50 percent of the final equilibrium solution.<sup>11</sup> We generated $c _ { 0 }$ using Matlab’s random number generator function. We varied the learning parameter ρ from 0 to 1 in increments of 0.1. For each value of ρ, we conducted 100 trials. The reported results represent the averages for these 100 trials.

![](/api/attachments/FRNQG5ZW/fulltext/images/84b4ef70439bd36170ddaf50792b08158d95639fe597af4bcada7828add305d8.jpg)  
Figure 6. Behavior of Investment Level Over Time Under Learning in Decision Theory

![](/api/attachments/FRNQG5ZW/fulltext/images/3b3ecbf450510fee61a3be73b38b5f97afef73b041475ea07f046b0c8875256f.jpg)  
Figure 7. Behavior of Hacker Effort Over Time Under Learning in Decision Theory

We studied the convergence dynamics in two ways. First, we determined the number of time periods required for the decision theory solution to converge to the simultaneous game solution. We assumed that convergence occurred when both firm’s investment level and hacker’s effort level in the decision theory solution came within 5 percent of their respective values in the simultaneous game solution, and stayed within the 5 percent band subsequently. We denote the minimum number of time periods required to achieve convergence as the delay before convergence. Second, we examined the firm’s payoff under the decision theory approach before convergence. The maximum number of periods required for convergence occurs when $\rho = 1$ . We used this maximum value as the time horizon for computing average payoff per period. We computed the firm’s average payoff per period for different ρ values. We denote the difference in the average payoffs under the decision theory with learning approach and the game theory approach as the cost before convergence.

![](/api/attachments/FRNQG5ZW/fulltext/images/b921d900bb4c99846d380dd1772920327c9d4e991fa4007eae8fda1be8b4f7fb.jpg)  
Figure 8. The Effect of the Learning Model on the Periods Required for Convergence

![](/api/attachments/FRNQG5ZW/fulltext/images/d1f2a4a3f1fc728c23eece08c3305d1d881d36cd81ea1e6488638951b4442640.jpg)  
Figure 9. The Effect of the Learning Model on Firm’s Profit Under the Decision Theory Approach

The results from the numerical simulations are summarized in Figures 8 and 9. We found that the delay before convergence first decreases with ρ and then increases as ρ approaches 1. The results show that for extreme ρ values, in which the firm adopts a myopic approach or uniform weighting scheme for the historical observations, it takes longer for the decision theory results to converge to those under a simultaneous game. Essentially, with the myopic approach, firm’s estimation of hacker’s effort fluctuates as seen in Figures 6 and 7. With the uniform weighing scheme, the fluctuations are more smoothed, but this approach carries a cost of assigning significant weight to information about hacker’s effort from the early periods whereas, in reality, the hacker uses only the most recently observed investment level in choosing his or her effort. Also, the convergence to the game theory solution makes early hacker information irrelevant, and the continuing use of such information could reduce the convergence rate (reciprocal of the delay before convergence). As a result, we find that the moderate values of ρ have faster convergence rates.

The rate of convergence also affects the loss resulting from using decision theory instead of a simultaneous game. In Figure 9, the difference between the payoff when a simultaneous game is played and that when decision theory is used represents the average loss per period the firm incurs by employing decision theory. We should note that the firm’s payoff is the same under when decision theory is used and when a simultaneous game is played after convergence is achieved. We find that the loss increases with an increase in ρ. The primary implication of this analysis is that when a firm uses decision theory to make its security investment, it should use the most recent observation about hacker effort in setting the investment level. However, this strategy may not be optimal if the firm’s objective is to maximize the convergence rate. Maximizing convergence rate requires an optimal weighting scheme for historical observations.

In summary, we find that if the firm employs the traditional decision theory model to set the investment level, then, over time, its behavior is likely to approach that of a firm that uses a simultaneous game. However, because the firm’s payoff when the firm and the hacker play a simultaneous game is still lower compared to that when they play a sequential game, the firm is better off forcing the hacker to play a sequential game, if the firm can control the sequence of actions.

While determining security investment using game theory often yields a superior payoff for the firm than using decision theory, it is difficult to estimate the parameters required by game theory. One of the implications of our results in the last section is that if mangers understand the motivation of hackers and the utility they derive, then they will be able to obtain a superior outcome because they could apply game theory instead of decision theory while deciding security investments. However, results from this section show that learning through observation of hacker efforts could be a substitute for estimation of hacker utility. Hacker efforts are more easily observable than hacker utility, which is latent. Our results show that when managers are unable to estimate hacker utility, they could improve the payoff from security investments if they use observations about past hacker efforts in the decision theory models.

## Conclusions

Current prac tic es in th e IT sec urity area view security investment as any other IT investment and use the traditional decision-theoretic risk management techniques to determine security investment levels. We argued in this paper that this method is incomplete because of the problem’s strategic nature and proposed game-theoretic approaches for the IT security investment problem. We showed that the firm realizes the maximum payoff when the firm and the hacker play a sequential game with the firm as the leader and the hacker as the follower. Sequential game requires that the firm credibly commits and communicates its strategy to the hacker. In the absence of such credible commitment and communication, the firm still enjoys a higher payoff when the firm and the hacker play a simultaneous game compared to when the firm assumes that the hacker is nonstrategic and uses the decision theory approach to determine investments, except when the firm neither underestimates nor overestimates the hacker effort by a significant amount under the decision theory approach. We also showed that if the firm learns about hacker effort from prior observations and uses these to estimate hacker effort when it uses the decision theory approach, then the attractiveness of the game theory approach over decision theory approach reduces.

There seems to be a dichotomy between our results and current business practices, which seem to favor the use of the decision theory approach. We hypothesize several reasons for this dichotomy. One reason could be that firms are truly unaware that hackers are strategic and of the potential benefits of using the game theory approach for the security investment problem. We believe that this paper provides insights to firms on how and why game-theoretic models perform better than decision-theoretic models. Another reason could be that firms view decision theory as a simplification of the more complex game theory approach. The decision theory and game theory models require estimation of several parameters. In some sense, the game theory model requires “deeper” user-specific parameters that are more difficult to obtain. We conjecture that the difficulty in estimation of user-specific parameters is one reason firms may prefer to use decision theory instead of game theory. Several developments are under way to make firms aware of hacker behavior and motivation so that they can apply game-theoretic techniques to make their security-related decisions. For example, organizations such as CERT facilitate sharing of security information and disclosure of vulnerabilities among firms.

In this paper, we assumed that the model parameters are common knowledge to the firm and the hacker. One area that seems particularly interesting for the investment problem is games with incomplete information, in which either the firm or the hacker is uncertain about the other’s payoff. This perspective allows incorporation of uncertainty about the nature of the game being played. Many of these common knowledge-related assumptions have been analyzed by game theorists. We leave the detailed analysis of a model that relaxes the common knowledge assumptions to future research. However, we can speculate that the firm’s uncertainty about the hacker’s utility from attacking will make a game theory solution less attractive than the one presented here. A higher level of uncertainty will reduce the firm’s payoff in the game theory setting, and the advantage of game theory over decision theory will diminish. Another limitation of the study is that its results are applicable only for targeted attacks such as denial of service and industrial espionage, and not for opportunistic attacks such as viruses, worms, phishing, and so on. Given the increasing trend of such opportunistic attacks, it is worthwhile to analyze how firms should protect themselves from such attacks. A realistic model of a security investment problem should incorporate both targeted attacks as well as random attacks. Further, our model assumes that vulnerability function is known to the firm and hackers. In essence, it assumes that vulnerabilities are known. The impact of uncertainty about the vulnerability function can also be explored in future research.

## Notes

1. Fellingham and Newman [15] make the same observation in the auditing context. 2. Formally, this is known as the Stackelberg game.

3. Along these three dimensions, many IT payoff metrics have been proposed in the literature to measure the value of IT investments. However, these are all ex post analyses. Our focus, however, is on ex ante IT security investment decisions.

4. The reader is referred to the annual Workshop on Economics of Information Security for more papers related to security investments. However, none of them studies the issues that we address in this paper.

5. An alternative specification is a model in which L is a random variable with an associated probability distribution. This specification does not change our results qualitatively.

6. s denotes ∂s/∂x and $s _ { _ { x x } } \mathrm { d e n o t e s } \partial ^ { 2 } s / \partial x ^ { 2 }$

7. In this paper, we consider targeted attacks by hackers. Although untargeted attacks, such as worms and viruses, can cause security losses, we restrict our model to targeted attacks such as industrial espionage, denial of service, and intrusions.

8. All of our results can be easily derived when $s ( \nu , z , c )$ has the general form $s ( \nu , z , c ) =$ m(v)n(c)o(z).

9. Since they analyze only the decision theory model, their functional form for s did not incorporate the hacker effort.

10. In general, the convergence will depend critically on the shapes of reaction functions of the two players.

11. We could easily extend the analysis to include the impact of the magnitude of the error on the convergence properties of the decision theory solution.

## Referenc es

1. Barucci, E. Exponentially fading memory learning in forward-looking economic models. Journal of Economic Dynamics and Control, 24, 5 (2000), 1027–1046.

2. Bashir, I.; Serafini, E.; and Wall, K. Securing network software applications: Introduction. Communications of the ACM, 44, 2 (2001), 28–30.

3. Berinato, S. Finally, a return on security spending. CIO Magazine (February 2002) (available at www.cio.com.au/index.php/id;557330171;fp;;fpid;).

4. Bodin, L.D.; Gordon, L.A.; and Loeb, M.P. Evaluating information security investments using the analytic hierarchy process. Communications of the ACM, 48, 2 (2005), 78–83.

5. Campbell, J.A. Real options analysis of the timing of IT investment decisions. Information and Management, 39, 5 (2002), 337–344.

6. Campbell, P.; Calvert, B.; and Boswell, B. Security+ Guide to Network Security Fundamentals. Boston: Course Technology, 2003.

7. Cavusoglu, H., and Raghunathan, S. Configuration of detection software: A comparison of decision and game theory approaches. INFORMS Decision Analysis, 1, 3 (2005), 131–148.

8. Cavusoglu, H.; Mishra, B.; and Raghunathan, S. The effect of Internet security breach announcements on market value: Capital market reaction for breached firms and Internet security developers. International Journal of Electronic Commerce, 9, 1 (2004), 69–105.

9. Cavusoglu, H.; Mishra, B.; and Raghunathan, S. A model for evaluating IT security investments. Communications of the ACM, 47, 7 (2004), 87–92.

10. Cavusoglu, H.; Mishra, B.; and Raghunathan, S. The value of intrusion detection systems in information technology security architecture. Information Systems Research, 16, 1 (2005), 28–46.

11. Cavusoglu, H.; Raghunathan, S.; and H. Cavusoglu. Configuration of and interaction between information security technologies: The case of firewalls and intrusion detection systems. Information Systems Research, forthcoming (2008).

12. Clemons, E.K. Evaluation of strategic investments in information technology. Communications of the ACM, 34, 1 (1991), 22–36.

13. Cremonini, M., and Nizovtsev, D. Understanding and influencing attackers’ decisions: Implications for security investment strategies. Paper presented at the Workshop on the Economics of Information Security (WEIS), Cambridge, UK, June 26–28, 2006.

14. Crume, J. Inside Internet Security: What Hackers Don’t Want You To Know. Harlow, UK: Addison-Wesley, 2001.

15. Fellingham, J.C., and Newman, D.P. Strategic considerations in auditing. Accounting Review, 60, 4 (October 1985), 634–650.

16. Fudenberg, D., and Levine, D.K. The Theory of Learning in Games. Cambridge, MA: MIT Press, 1998.

17. Gal-Or, E.A., and Ghose, A. The economic incentives for sharing security information. Information Systems Research, 16, 2 (2005), 186–208.

18. Gordon, L.A., and Loeb, M.P. The economics of information security investment. ACM Transactions on Information and System Security, 5, 4 (2002), 438–457.

19. Gordon, L.A.; Loeb, M.P.; and Lucyshyn, W. Sharing information on computer systems: An economic analysis. Journal of Accounting and Public Policy, 22, 6 (2003), 461–485.

20. Han, K.; Kauffman, R.J.; and Nault, B.R. Information exploitation and interorganizational systems ownership. Journal of Management Information Systems, 21, 2 (Fall 2004), 109–135.

21. Hausken, K. Income, interdependence, and substitution effects affecting incentives for security investment. Journal of Accounting and Public Policy, 25, 6 (2006), 629–665.

22. Hausken, K. Strategic defense and attack for series and parallel reliability systems. European Journal of Operational Research, 186, 2 (2008), 856–881.

23. Hitt, L.M.; Frei, F.X.; and Harker, P.T. How firms decide on technology. In R.E. Litan and A.M. Santomero (eds.), Brookings/Wharton Papers on Financial Services. Washington, DC: Brookings Institution Press, 1999, pp. 93–136.

24. Hoo, K.J.S. How much security is enough? A risk management approach to computer security. Ph.D. dissertation, Department of Marketing, Stanford University, 2000.

25. Kaplan, R.S. Must CIM be justified by faith alone. Harvard Business Review, 64, 2 (March–April 1986), 87–95.

26. Karofsky, E. Return on security investment: Calculating the security investment equation. Secure Business Quarterly, 1, 2 (2001).

27. Kohli, R.; Sherer, S.A.; and Baron, A. Editorial—IT investment payoff in e-business environments: Research issues. Information Systems Frontiers, 5, 3 (2003), 239–247.

28. Kumar, R.L. A note on project risk and option values of investments in information technologies. Journal of Management Information Systems, 13, 1 (Summer 1996), 187–193.

29. Kunreuther, H., and Heal, G. Interdependent security. Journal of Risk and Uncertainty, 26, 3 (2003), 231–249.

30. Leeson, P., and Coyne, C.J. The economics of computer hacking. Journal of Law, Economics and Policy, 1, 2 (2006), 511–532.

31. Longstaff, T.; Chittister, C.; Pethia, R.; and Haimes, Y. Are we forgetting the risk of information technology? IEEE Computer, 33, 12 (December 2000), 43–51.

32. Moitra, S.D., and Konda, S.L. The survivability of network systems: An empirical analysis.

CMU/SEI-2000-TR -021, Software Engineering Institute/Computer Emergency Response Team (SEI/CERT ) Report, Carnegie Mellon University, Pittsburgh, PA, December 2000.

33. Power, R. 2002 CSI/FBI computer crime and security survey. Computer Security Journal, 17, 2 (Spring 2002), 29–51.

34. Rainer, R.K.; Snyder, C.A.; and Carr, H.H. Risk analysis for information technology. Journal of Management Information Systems, 8, 1 (Summer 1991), 129–148.

36. Rockart, J.F.; Earl, M.J.; and Ross, J.W. Eight imperatives for the new IT organization. Sloan Management Review, 38, 1 (1996), 43–55.

37. Rothke, B. Hackers then and now: Answers to some perennial questions. Computer Security Journal, 16, 3 (2000), 11–14.

38. Schechter, S.E., and Smith, M.D. How much security is enough to stop a thief? In R.N. Wright (ed.), Proceedings of the Seventh International Financial Cryptography Conference. New York: Springer-Verlag, 2003, pp. 122–137.

39. Shaw, D.S.; Post, J.M.; and Ruby, K.G. Inside the minds of the insider. Security Management, 43, 12 (December 1999), 34–44.

40. Sieberg, D. Hackers shift focus to financial gain. CNN.com (available at www.cnn. com/2005/TECH/internet/09/26/identity.hacker/).

41. Stoneburner, G.; Goguen, A.; and Feringa, A. Risk management guide for information technology systems. National Institute of Standards and Technology Special Publications 800–30, White Paper, U.S. Department of Commerce, Gaithersburg, MD, 2002.

42. Sun, L.; Srivastava, R.P.; and Mock, T.J. An information systems security risk assessment model under the Dempster–Shafer theory of belief functions. Journal of Management Information Systems, 22, 4 (Spring 2006), 109–142.

43. Varian, H. System reliability and free riding. Paper presented at the Workshop on the Economics of Information Security (WEIS), Berkeley, CA, May 16–17, 2002.

44. Yue, W., and Çakanyildirim, M. Intrusion prevention in information systems: Reactive and proactive response. Journal of Management Information Systems, 24, 1 (Summer 2007), 329–353.

## Appendix

## Proof for Proposition 1

(a) Proof for $g _ { f , S E } ^ { * } \geq g _ { f , S G } ^ { * } ;$ Assume that the optimal investment and optimal payoff in the simultaneous game model are $z _ { S G } ^ { * }$ and $g _ { f , S G } ( z _ { S G } ^ { * } )$ . In a sequential game model, if the firm selects $z _ { S G } ^ { * } ,$ it will receive a payoff of $g _ { f , S G } ( z _ { S G } ^ { * } )$ because the hacker will react with an effort level of $c _ { S G } ^ { * } .$ . However, given that the firm optimizes over investment level, its optimal payoff can never be worse than $g _ { f , S G } ( z _ { S G } ^ { * } )$ . Or, more specifically, $g _ { f , S E } ( z _ { S E } ^ { * } ) \geq g _ { f , S G } ( z _ { S G } ^ { * } )$

The proof for $g _ { f , S E } ^ { * } \geq g _ { f , D T } ^ { * }$ is similar to that of $g _ { f , S E } ^ { * } \geq g _ { f , S G } ^ { * } .$

(b) The benefit under decision theory model is

$$
g _ {f, D T} ^ {*} = \left[ v - \left[ v \left(H _ {0}\right) ^ {\phi (1 + \beta)} \left(L _ {0} c _ {0}\right) ^ {- \beta} \right] ^ {\frac {1}{(1 - \phi) (1 + \beta)}} \right] L - \frac {1}{\alpha} \left[ v L _ {0} c _ {0} \right] ^ {\frac {1}{1 + \beta}}.
$$

The first-order condition is given by

$$
\begin{array}{l} \frac {\partial g _ {f , D T} ^ {*}}{\partial c _ {0}} = \left[ \frac {\beta L}{(1 - \phi) (1 + \beta)} \left[ v (H _ {0}) ^ {\phi (1 + \beta)} (L _ {0}) ^ {- \beta} \right] ^ {\frac {1}{(1 - \phi) (1 + \beta)}} \right] c _ {0} ^ {\frac {- \beta}{(1 - \phi) (1 + \beta)} - 1} \\ - \frac {1}{\alpha (1 + \beta)} \left[ v L _ {0} \right] ^ {\frac {1}{1 + \beta}} c _ {0} ^ {\frac {1}{1 + \beta} - 1} = 0, \end{array}
$$

which gives the optimal value of $c _ { 0 }$ as

$$
c _ {0} ^ {*} = \left[ v (1 - \phi) ^ {\frac {(1 - \phi) (1 + \beta)}{\phi}} H _ {0} ^ {(1 + \beta)} L _ {0} ^ {- \beta} \right] ^ {\frac {\phi}{1 - \phi + \beta}}.
$$

Substituting the above value of $c _ { 0 } ^ { * }$ in $g _ { f , D T } ^ { * }$ , we find that $g _ { f , D T } ^ { * } = g _ { f , S E } ^ { * }$ . Hence, the best solution for decision theory is the same as the sequential game solution.

The second derivative of payoff under decision theory with respect to $c _ { 0 }$ is given by

$$
\begin{array}{l} \frac {\partial^ {2} g _ {f , D T} ^ {*}}{\partial c _ {0} ^ {2}} = \left[ \frac {- \beta L (1 + 2 \beta - \phi - \beta \phi)}{(1 - \phi) ^ {2} (1 + \beta) ^ {2}} \left[ v (H _ {0}) ^ {\phi (1 + \beta)} (L _ {0}) ^ {- \beta} \right] ^ {\frac {1}{(1 - \phi) (1 + \beta)}} \right] c _ {0} ^ {\frac {- \beta}{(1 - \phi) (1 + \beta)} - 2} \\ \quad + \frac {\beta}{\alpha (1 + \beta) ^ {2}} [ v L _ {0} ] ^ {\frac {1}{1 + \beta}} c _ {0} ^ {\frac {1}{1 + \beta} - 2} \\ = - \left\{\left[ \left[ \frac {\alpha L \beta}{1 - \phi} + \frac {\alpha L (1 + \beta - \phi)}{(1 - \phi) ^ {2}} \right] \left[ v (H _ {0}) ^ {\phi (1 + \beta)} (L _ {0}) ^ {- \beta} \right] ^ {\frac {1}{(1 - \phi) (1 + \beta)}} \right] c _ {0} ^ {\frac {- \beta}{(1 - \phi) (1 + \beta)}} \right. \\ \quad \left. - [ v L _ {0} ] ^ {\frac {1}{1 + \beta}} c _ {0} ^ {\frac {1}{1 + \beta}} \right\} \frac {\beta c _ {0} ^ {- 2}}{\alpha (1 + \beta) ^ {2}}. \end{array}
$$

Applying the first-order condition to the above equation, we get

$$
\frac {\partial^ {2} g _ {f , D T} ^ {*}}{\partial c _ {0} ^ {2}} = \left\{\left[ - \frac {\alpha L (1 + \beta - \phi)}{(1 - \phi) ^ {2}} \right] \left[ v (H _ {0}) ^ {\phi (1 + \beta)} (L _ {0}) ^ {- \beta} \right] ^ {\frac {1}{(1 - \phi) (1 + \beta)}} c _ {0} ^ {\frac {- \beta}{(1 - \phi) (1 + \beta)}} \right\} \frac {\beta c _ {0} ^ {- 2}}{\alpha (1 + \beta) ^ {2}} \leq 0.
$$

Thus, the firm’s payoff function under decision theory is strictly concave in $c _ { 0 } .$ . We know from part (a) of Proposition 1 that $g _ { f , S E } ^ { * } \geq g _ { f , S G } ^ { * } .$ . Hence, we can also say $g _ { f , D T } ^ { * } ( c _ { 0 } ^ { * } ) \geq g _ { f , S G } ^ { * } .$ Given that $\partial ^ { 2 } g _ { _ { f , D T } } ^ { \mathrm { ~ * ~ } } / \partial c _ { _ { 0 } } ^ { 2 } \leq 0$ , we can establish that $g _ { f , D T } ^ { * } \ge g _ { f , S G } ^ { * }$ if and only if $\underline { { c } } <  { c _ { \mathrm { 0 } } } < \bar { c }$

## Proof for Proposition 2

The following equations compare the firm’s investment levels under the three approaches:

$$
z _ {S G} ^ {*} - z _ {D T} ^ {*} = \frac {1}{\alpha} \bigg [ v H _ {0} ^ {\phi} L _ {0} ^ {(1 - \phi)} \bigg ] ^ {\frac {1}{1 - \phi + \beta}} - \frac {1}{\alpha} \big [ v L _ {0} c _ {0} \big ] ^ {\frac {1}{1 + \beta}}
$$

$$
z _ {S E} ^ {*} - z _ {D T} ^ {*} = \frac {1}{\alpha} \left[ \left[ v (1 - \phi) ^ {- (1 - \phi)} H _ {0} ^ {\phi} L _ {0} ^ {(1 - \phi)} \right] ^ {\frac {1}{1 - \phi + \beta}} \right] - \frac {1}{\alpha} \left[ v L _ {0} c _ {0} \right] ^ {\frac {1}{1 + \beta}}
$$

$$
z _ {S G} ^ {*} - z _ {S E} ^ {*} = \frac {1}{\alpha} \bigg [ v H _ {0} ^ {\phi} L _ {0} ^ {(1 - \phi)} \bigg ] ^ {\frac {1}{1 - \phi + \beta}} - \frac {1}{\alpha} \Bigg [ \bigg [ v (1 - \phi) ^ {- (1 - \phi)} H _ {0} ^ {\phi} L _ {0} ^ {(1 - \phi)} \bigg ] ^ {\frac {1}{1 - \phi + \beta}} \Bigg ].
$$

The following equations compare the breach probabilities under the three approaches:

$$
s _ {S G} ^ {*} - s _ {D T} ^ {*} = \left[ - \left[ v H _ {0} ^ {\phi} L _ {0} ^ {- \beta} \right] ^ {\frac {1}{1 - \phi + \beta}} + \left[ v H _ {0} ^ {\phi (1 + \beta)} \left(L _ {0} c _ {0}\right) ^ {- \beta} \right] ^ {\frac {1}{(1 - \phi) (1 + \beta)}} \right]
$$

$$
s _ {S E} ^ {*} - s _ {D T} ^ {*} = \left[ - \left[ v (1 - \phi) ^ {\beta} H _ {0} ^ {\phi} L _ {0} ^ {- \beta} \right] ^ {\frac {1}{1 - \phi + \beta}} + \left[ v H _ {0} ^ {\phi (1 + \beta)} \left(L _ {0} c _ {0}\right) ^ {- \beta} \right] ^ {\frac {1}{(1 - \phi) (1 + \beta)}} \right]
$$

$$
s _ {S G} ^ {*} - s _ {S E} ^ {*} = \Bigg [ - \bigg [ v H _ {0} ^ {\phi} L _ {0} ^ {- \beta} \bigg ] ^ {\frac {1}{1 - \phi + \beta}} + \bigg [ v (1 - \phi) ^ {\beta} H _ {0} ^ {\phi} L _ {0} ^ {- \beta} \bigg ] ^ {\frac {1}{1 - \phi + \beta}} \Bigg ].
$$

Proposition 2 follows from simple algebraic manipulations of the above equations and therefore is omitted.
